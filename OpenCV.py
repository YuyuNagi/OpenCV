import cv2 as cv
import numpy as np

class OpenCV:
    def __init__(self, img):
        self.img = img
    def RGB2GRAY(self):
        imgGray = cv.cvtColor(self.img, cv.COLOR_RGB2GRAY)
        return OpenCV(imgGray)
    def binary(self, thresh = 127):
        ret, imgBinary = cv.threshold(self.RGB2GRAY().img, thresh, 255,
        cv.THRESH_BINARY)
        return OpenCV(imgBinary)
    def adaptiveThreshold(self):
        adaptiveImg = cv.adaptiveThreshold(self.RGB2GRAY().img, 255,
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY, 11, 2)
        return OpenCV(adaptiveImg)
try:
    img = OpenCV(cv.imread(str(input('輸入完整的圖片路徑: '))))
    print('選擇想要的影像處理:\n(1)顯示原圖\n(2)轉黑白圖片後顯示')
    print('(3)二值化後顯示\n(4)高斯二值化後顯示')
    methon = int(input('>>> '))
    Dic = {
        1 : img,
        2 : img.RGB2GRAY(),
        3 : img.binary(),
        4 : img.adaptiveThreshold()
    }
    result = Dic.get(methon)
    cv.namedWindow('Image window', cv.WINDOW_NORMAL)
    cv.imshow('Image window', result.img)
    print('在彈出視窗下點擊空白鍵以關閉視窗')
    cv.waitKey( )
except:
    print('找不到圖片或無效的輸入')