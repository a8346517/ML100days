# 1.不動產資料檔案讀取並串接
# 資料分散在4個資料，先合併成一個資料方便後續分析，但是我發現有英文欄位跟中文欄位，留下中文刪除英文，並加入新的欄位用以分辨台北市Taipei、新北市New_Taipei、台中市Taichung、高雄市Kaohsiung

# 1. 用Pandas中的pd.read_csv()分別讀取A_lvr_land_A.csv、B_lvr_land_A.csv、E_lvr_land_A.csv、F_lvr_land_A.csv
# 2. 刪除csv中第二列英文翻譯，The villages and towns urban district,transaction sign,land sector position building sector house number plate,land shifting total area square meter,....
# 3. 生成city欄位其中以地區分類台北市Taipei(A_lvr_land_A.csv)、新北市New_Taipei(F_lvr_land_A.csv)、台中市Taichung(B_lvr_land_A.csv)、高雄市Kaohsiung(E_lvr_land_A.csv)
# 4. 將以上四份資料運用pd.concat()串接
import pandas as pd
datataipei = pd.read_csv("A_lvr_land_A.csv")
datataichung = pd.read_csv("B_lvr_land_A.csv")
datakaohsiung = pd.read_csv('E_lvr_land_A.csv')
datanewtaipei = pd.read_csv('F_lvr_land_A.csv')
print(datataipei.head())
datataipei = datataipei.drop(0)
datataichung = datataichung.drop(0)
datakaohsiung = datakaohsiung.drop(0)
datanewtaipei = datanewtaipei.drop(0)

datataipei['地區'] = '台北'
datataichung['地區'] = '台中'
datakaohsiung['地區'] = '高雄'
datanewtaipei['地區'] = '新北'

data = pd.concat([datataipei, datataichung, datakaohsiung, datanewtaipei], axis=0, join='inner').reset_index(drop=True)
print(data.head())
print(data.info())

# 2. 資料清理與切片
# 因為我是想買來住的房子，所以幫忙刪除住宿用途以外的資料，並且限制

# 交易年月日，限制在109年
# 建物現況格局-房，1~5間
# 建物現況格局-廳，1~2廳
# 以下columns_mapping、analysis_columns、columns_type提供給資料科學家配合使用
# 利用.rename()並配合以下columns_mapping，將原中文欄位名稱改為英文方便之後分析
# 取出主要用途(main_use)為'住家用'以及都市土地使用分區(use_zoning)為'住'的資料並針對以下欄位analysis_columns做分析並去除na值 (提示:先取完之後再.dropna())
# 觀察欄位資料型態，並利用.astype()搭配以下提供的columns_type做欄位型態轉換
columns_mapping = {'鄉鎮市區':'towns',
'交易標的':'transaction_sign',
'土地區段位置建物區段門牌':'house_number',
'土地移轉總面積平方公尺':'land_area_square_meter', 
'都市土地使用分區':'use_zoning', 
'非都市土地使用分區':'land_use_district',
'非都市土地使用編定':'land_use',
'交易年月日':'tx_dt', 
 '交易筆棟數':'transaction_pen_number', 
 '移轉層次':'shifting_level', 
 '總樓層數':'total_floor_number', 
 '建物型態':'building_state', 
 '主要用途':'main_use', 
 '主要建材':'main_materials',
 '建築完成年月':'complete_date', 
 '建物移轉總面積平方公尺':'building_area_square_meter', 
 '建物現況格局-房':'room_number', 
 '建物現況格局-廳':'hall_number', 
 '建物現況格局-衛':'health_number', 
'建物現況格局-隔間':'compartmented_number', 
 '有無管理組織':'manages', 
 '總價元':'total_price', 
 '單價元平方公尺':'unit_price', 
 '車位類別':'berth_category', 
 '車位移轉總面積(平方公尺)':'berth_area_square_meter',
'車位總價元':'berth_price', 
 '備註':'note', 
 '編號':'serial_number', 
 '主建物面積':'main_building_area', 
 '附屬建物面積':'auxiliary_building_area', 
 '陽台面積':'balcony_area', 
 '電梯':'elevator',
 '地區':'city'
                  }
analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                                     'main_building_area',
                                     'tx_dt','unit_price','room_number','hall_number','health_number']
columns_type = {'total_price': 'int','unit_price':'float','building_area_square_meter':'float',
                                      'main_building_area': 'float',
                                      'room_number': 'int','hall_number': 'int','health_number': 'int'}
new_data = data.rename(columns=columns_mapping)
new_data = new_data.loc[(new_data['main_use']=='住家用')&(new_data['use_zoning']=='住'),analysis_columns].dropna()
print(new_data.info())
new_data = new_data.astype(columns_type)
print(new_data.info())
print(new_data.head())
# 做資料切片將
# 新增欄位交易年月日(tx_dt_year)，從交易年月日(tx_dt)萃取出年份
# 1.交易年月日(tx_dt_year)，限制在109年
# 2.建物現況格局-房(room_number)，限制在1到5間
# 3.建物現況格局-廳(hall_number)，限制在1到2廳
# 4.最後運用.reset_index()重新定義索引
new_data['tx_dt_year'] = new_data['tx_dt'].apply(lambda x : int(x[:3]))
new_data = new_data.loc[(new_data['tx_dt_year']==109)&
                        (new_data['room_number']>=1)&
                        (new_data['room_number']<=5)&
                        (new_data['hall_number']>=1)&
                        (new_data['hall_number']<=2)].reset_index(drop=True)
print(new_data)

# 3. 建立自定義特徵加入分析
# 建立新特徵
# 1. 建物移轉總面積坪(building_area_square_feet) : 建物移轉總面積平方公尺*0.3025
# 2. 主建物面積坪(main_building_area_square_feet) : 主建物面積*0.3025
# 3. 單價元坪(unit_price_square_feet) : 單價元平方公尺/0.3025
new_data['buildin_area_square_feet'] = new_data['building_area_square_meter']*0.3025
new_data['main_buildin_area_square_feet'] = new_data['main_building_area']*0.3025
new_data['unit_price_square_feet'] = new_data['unit_price']/0.3025
print(new_data.describe()) # 發現最小值有0[tatal_price,building_area_square_meter]
new_data = new_data.loc[(new_data['total_price']!=0)&(new_data['main_building_area']!=0)]
print(new_data.describe())

# 4. 找出台北市時價登入總價高度相關的變數
# 阿宏我是台北人他想找出影響台北市總價、單價元坪的因子
# 相關係數0.3以下為低相關，0.3~0.7為中等相關，0.7以上為高度相關
# 資料切片切出city欄位為台北市的資料，並找出時價登入總價(total_price)高度相關的變數
# 資料切片切出city欄位為台北市的資料，找出單價元坪(unit_price_square_feet)高度相關的變數
new_data1 = new_data.loc[new_data['city']=='台北'].corr()[['total_price', 'unit_price_square_feet']]
print(new_data1)
# 5. 資料視覺化並解釋
# 以城市(city)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot，
# 並找出單價元坪(unit_price_square_feet)中位數最高的地區
import matplotlib.pyplot as plt
new_data.boxplot(column=['unit_price_square_feet'], by='city', figsize=(16,6))
plt.xticks([1,2,3,4],['Taipei','Taichung','Kaohsiung','newTaipei'])
plt.show()
# 2. 進一步對台北市的資料做圖，以建物現況格局-房(room_number)為x軸，以總價元(total_price)為y軸畫出boxplot，
# 並找出總價元(total_price)中位數最高的房間數。hint:資料切片找出city欄位為台北市的資料，再進一步畫圖
new_data.loc[new_data['city']=='台北'].boxplot(column=['total_price'], by='room_number', figsize=(16,6))
plt.show()

# 3. 對台北市的資料做圖，先將地區(twons)做編碼在進行，再以地區(twon)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot，並找出單價元坪(unit_price_square_feet)中位數最高的地區。
# hint:運用LabelEncoder()對地區(twons)做編碼，運用.inverse_transform()反查編碼的地區
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder().fit(new_data['towns'].values)
new_data['new_towns'] = le.transform(new_data['towns'].values)
print(new_data['new_towns'].head())
new_data.loc[new_data['city']=='台北'].boxplot(column=['unit_price_square_feet'], by='new_towns', figsize=(16,6))
plt.show()

#運用.inverse_transform()反查編碼的地區
print(le.inverse_transform([26]))

#台中
new_data2 = new_data.loc[new_data['city']=='台中'].corr()[['total_price','unit_price_square_feet']]
print(new_data2)
new_data.loc[new_data['city']=='台中'].boxplot(column='total_price', by='room_number', figsize=(16,6))
plt.show()
new_data.loc[new_data['city']=='台中'].boxplot(column='unit_price_square_feet', by='new_towns', figsize=(16,6))
plt.show()
#運用.inverse_transform()反查編碼的地區
print(le.inverse_transform([76]))