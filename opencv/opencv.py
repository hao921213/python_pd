import cv2
import numpy as np
import random
img=cv2.imread("colorcolor.jpg")# cv.imread("")讀取圖片
img=cv2.resize(img,(800,800))#cv2.resize(要改變的圖片,要改變的大小)
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)#cv2.resize(要改變的圖片,(0,0),fx為要改變寬的倍率,fy為要改變高的倍率)
newImg=img[0:200,0:150]#切割圖片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #轉成灰階
blur=cv2.GaussianBlur(img,(15,15),10)#轉成模糊 第二個參數是kernel第三個參數是標準差
canny=cv2.Canny(img,150,200)# 抓圖片邊緣 第二個參數是最低門檻，第三個參數是最高門檻
dilate=cv2.dilate(canny,np.ones((3,3),np.uint8),iterations=1)#膨脹線條 第二個參數是kernel 第三個參數是要膨脹的次數
erode=cv2.erode(canny,np.ones((1,1),np.uint8),iterations=1)#侵蝕線條 第二個參數是kernel 第三個參數是要侵蝕的次數
cv2.imshow("image",img)#cv2.imshow顯示圖片在視窗上
cv2.waitKey(0) #cv2.waitKey顯示時間等待幾毫秒 如果參數為0則等待無限秒直到我們去關掉

#創建圖片
#圖層的三原色順續為B,G,R
img=np.empty((300,300,3),np.uint8)#建立一個300*300大小的圖，後面的3為B,R,G圖層，np.uint8則是用八個bit去儲存0-255
for row in range(300):
    for col in range(300):
        img[row][col]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
cv2.imshow("img",img)
cv2.waitKey(0)

#讀取影片
cap=cv2.VideoCapture("")#抓入影片 若輸入參數為0則抓入視訊鏡頭，如果有外接鏡頭則編號以此類推往下變成1
while True:
    reg,frame=cv2.read()#cv2.read()會回傳的第一個是下一張照片是否可以回傳的布林值，第二個是回傳下一張圖片 
    if reg:
        frame=cv2.resize(frame,(0,0),fx=0.4,fy=0.4)
        cv2.imshow(frame)
    else:
        break
    cv2.waitKey(1)#如果要調影片的速度可以調整參數值
    #(if(cv2.waitKey(1))==ord(): break) 可以設定假設按哪個鍵，就會停止影片

#在圖片上加入元素
img=np.zeros((600,600,3),np.uint8)
cv2.line(img,(0,0),(600,600),(0,255,0),2)#在圖片上畫直線 cv2.line(圖片,起點,終點,顏色,粗度)
cv2.rectangle(img,(0,0),(400,300),(255,0,0),2)#在圖片上畫矩形 cv2.rectangle(圖片,左上角的點,右上角的點,顏色,粗度(如果要實心的則為cv.FILLED))
cv2.circle(img,(500,500),30,(255,0,255),4)#在圖片上畫圓形 cv2.circle(圖片,圓心座標,半徑,顏色,粗度(如果要實心的則為cv.FILLED))
cv2.putText(img,"Hello",(200,500),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)#在圖片上寫字 cv2.putText(圖片,該文字的座標,字體,大小,顏色,粗度)

#偵測顏色
def empty(v):
    pass
img=cv2.imread("weini.jpg")
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,320)
cv2.createTrackbar("HueMin","TrackBar",0,179,empty)
cv2.createTrackbar("HueMax","TrackBar",179,179,empty)
cv2.createTrackbar("SatMin","TrackBar",0,179,empty)
cv2.createTrackbar("SatMax","TrackBar",255,255,empty)
cv2.createTrackbar("ValMin","TrackBar",0,255,empty)
cv2.createTrackbar("ValMax","TrackBar",255,255,empty)
while True:
    h_min=cv2.getTrackbarPos("HueMin","TrackBar")
    h_max=cv2.getTrackbarPos("HueMax","TrackBar")
    s_min=cv2.getTrackbarPos("SatMin","TrackBar")
    s_max=cv2.getTrackbarPos("SatMax","TrackBar")
    v_min=cv2.getTrackbarPos("ValMin","TrackBar")
    v_max=cv2.getTrackbarPos("ValMax","TrackBar")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("img",img)
    cv2.imshow("hsv",hsv)
    cv2.imshow("result",result)
    cv2.waitKey(1)
