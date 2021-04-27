from bokeh.plotting import figure, output_file, show
from bokeh.models import widgets
from bokeh.io import output_notebook

output_notebook()

# output_file("out.html")
# p = figure()
# p.line([1,2,3,4,5],[5,4,3,2,1])
# show(p)

# # create a Figure object
# p = figure(plot_width=300, plot_height=300, tools="pan,reset,save")
# # 添加圓點的分佈圖
# # p.circle (x/y 座標, size, color, and 透明度)
# p.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], size=20, color="navy", alpha=0.5)

# # specify how to output the plot(s)
# output_file("foo.html")

# # 秀圖
# show(p)

# output_file("toolbar.html")
# p = figure(plot_width=400,plot_height=400,title=None, toolbar_location='below',toolbar_sticky=False)
# #繪製工具軸移到下方,並將工具欄移到繪製軸以外的區域
# p.circle([1,2,3,4,5],[2,5,8,2,7],size=10)
# show(p)

import bokeh.sampledata
bokeh.sampledata.download()
from bokeh.sampledata.stocks import AAPL
import numpy as np
import pandas as pd
app1 = np.array(AAPL['adj_close'])
app2 = np.array(AAPL['date'],dtype = np.datetime64)
window_size = 30
window = np.ones(window_size)/float(window_size)
app1_avg = np.convolve(app1,window,'same')#捲積,去頭尾

output_file("stocks.html", title="stocks.py example")
p = figure(plot_width=800,plot_height=350,x_axis_type="datetime")
p.circle(app2,app1,size=4,color='darkgrey',alpha=0.2, legend_label='close')
p.line(app2, app1_avg, color='navy', legend_label = 'avg')
p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left" #顯示線標題移到左上
p.grid.grid_line_alpha = 0 #移除網狀線
p.xaxis.axis_label = 'Date' #x軸標題
p.yaxis.axis_label = 'Price'#y軸標題
p.ygrid.band_fill_color = "olive" #y軸網格顏色
p.ygrid.band_fill_alpha = 0.1
show(p)

#HW1

#指定輸出檔名
output_file("fruits.html")

#給定資料
fruits =  ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts =  [5, 3, 4, 2, 4, 6]

# 不增設按鈕 toolbar_location=None, tools=""
# plot_height 設定條形高度
#配置圖表
p = figure(x_range=fruits,plot_height=800,title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)

#Y座標從0開始
p.y_range.start = 0

show(p)

#HW2 
#指定輸出檔名
output_file("fruits2.html")

#給定資料
fruits =  ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts =  [5, 3, 4, 2, 4, 6]
#資料作排序
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])
print(sorted_fruits)
counts.sort()
# 不增設按鈕 toolbar_location=None, tools=""
# plot_height 設定條形高度
#配置圖表
p = figure(x_range=sorted_fruits,plot_height=800,title="sorted_Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=sorted_fruits, top=counts, width=0.9)

#Y座標從0開始
p.y_range.start = 0

show(p)

