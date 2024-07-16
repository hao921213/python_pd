import matplotlib.pyplot as plt
#繪圖
#plt.plot(x座標串列,y座標串列[,其他參數])  折線圖
#plt.bar(x座標串列,y座標串列,width=,bottom=[,其他參數])  長條圖
#plt.barth(x座標串列,y座標串列,height=,left=[,其他參數])  橫條圖
#plt.pieplt.pie(資料串列[,其他參數])
#其他參數有explode,labeldistance,autopct,pctdistance,shadow,startangle
#其他參數有linewidth(lw)線寬度預設值為1,color顏色預設為藍色,linestyle(ls)線條樣式預設為實線,marker標記樣式,markersize(ms)標記大小,label圖例名稱要搭配plt.legend()

#設定標題
#plt.title(""[,frontsize]) 
#plt.xlable(""[,frontsize]) 
#plt.ylable(""[,frontsize])
#plt.xlim(起始值,終止值)
#plt.ylim(起始值,終止值) 如果沒有給範圍，電腦會自動給合適範圍

#設定座標刻度
#plt.xticks[串列] 
#plt.yticks[串列]
#plt.tick_params(axis='',lablesize=,color='')

#設定格線
#plt.grid(color='',linestyle='',linewidth='',alpha=''(透明度))
#plt.show 繪圖後不會自動顯示，所以需要show

#設定中文字型及負號
#plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
#plt.rcParams["axes.unicode_minus"] = False

#設定圖表區
#plt.figure([其他參數])
#其他參數有figsize,dpi,facecolor,edgecolor,frameon,tight_layout

