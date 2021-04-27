from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# HW1更改 Projection 的設定繪製出地球儀圖形
# HW2當 "projection" 參數為“ortho"時，所得圖位地球儀截面
# HW3當 "projection" 參數為“Mill"時，所得平展位面
# HW4查看 resolution / 經緯度座標的繪圖精細度
m=Basemap(projection='ortho', lat_0=50, lon_0=-100,resolution=None)
plt.figure(figsize=(5,5))
m.bluemarble()

plt.show()

n=Basemap(width=12000000,height=9000000,projection='lcc',resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
n.bluemarble()
plt.show()

map = Basemap(projection='mill',
            llcrnrlat = -90,
            llcrnrlon = -180,
            urcrnrlat = 90,
            urcrnrlon = 180,
            resolution='c')
            
map.drawcoastlines()
#畫出國家，並使用線寬為2 的線條生成分界線。
map.drawcountries(linewidth=2)

#這會用藍色線條畫出州
map.drawstates(color='b')

#這會畫出國家
map.drawcounties(color='darkred')

plt.title('Basemap Tutorial')
plt.show()


