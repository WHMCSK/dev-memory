# Opencv

### 安装环境

```
brew install python@3.9
pip install numpy matplotlib opencv_python
```

如果使用pip在线安装失败，也可以下载安装包安装：

搜索和下载python包的网站：

https://pypi.org

下载好之后，仍然使用pip进行安装：
```
pip install matplotlib-3.3.4-cp39-cp39-macos×_10_9_x86_64. whl
```

### 窗体api

namedWindow()  // 创建窗口，并给窗口取名字

imshow()    // 指定窗口名字显示一个图片，多帧在同一个窗口显示，可以播放视频

destoryAllWindows()

resizeWindow()

imread() // 加载图片

imwrite() // 保存图片

```
grep "namedWindow(" * -Rn // 搜索文档
```

### 视频采集api

VideoCapure()   // 虚拟采集器   
cap.read() // 采集  
cap.release() // 释放资源

VideoCapure()可以从摄像头采集视频，也可以从多媒体文件采集视频

```
cap = cv2.VideoCapture(0, 0) // 从摄像头采集视频
cap = cv2.VideoCapture('./b.mp4', 0)  // 从多媒体文件采集视频
```

### 视频录制api

VideoWriter()  // 参数一为输出文件  参数二为多媒体文件格式(VideoWriter_fourcc)  参数三为帧率  参数四为分辨率大小
 
vw.write()

vw.release()

isOpened()  // 判断摄像头是否打开

源码位置：

modules/videoio/include/opencv2/videgio.hpp    
doc/py_tutorials/py_gui/py_video_display/py_video_display.markdown   

```
CV_WRAP VideoWriter(const String& filename, int fourcc, double fps,
        Size frameSize, bool isColor = true);
```

示例代码：

```
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter(0, fourcc, 25,(640, 360), True ) // 注意分辨率必须设置成和摄像头一致，如果不一致，写文件的时候是不会写数据的
```

### 控制鼠标api

* 设置鼠标回调函数   
setMouseCallback ( winname, callback, userdata)  
callback ( event, x, y, flags, userdata )  // 函数名是自己取的  

* event与flag参数的定义位置
modules/highgui/include/opencv2/highgui.hpp

### TrackBar api

createTrackbar

getTrackbarPos

* createTrackbar参数 

trackbarname, winname

value:trackbar当前值

count:最小值为0，最大值为count

callback, userdata

* getTrackBarPos参数

输入参数：trackbarname

输入参数：winname

输出：当前值


### 核心知识

* 色彩空间变换
* 像素访问
* 矩阵的＋、-、*、/
* 基本图形的绘制

### 颜色空间

* RGB：人眼的色彩空间
* 0penCV默认使用BGR
* HSV/HSB/HSL
* YUV

### HSV

* Hue：色相，即色彩，如红色，蓝色
* Saturation：饱和度，颜色的纯度
* value：明度

### HSL



### YUV

* YUV4:2:0
* YUV4:2:2
* YUV4:4:4

YUV是从电视系统来的。

### 颜色空问转换

cvtColor

```
colorspace = [cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2YUV]
cvt_img = cv2.cvtColor(im, colorspace[index])
```

### Numpy

* OpenCV中用到的短阵都要转换成Nurpy数组
* Numpy是一个经高度优化的Python数值库

### Numpy基本操作

* 创建矩阵
* 检索与赋值[y,×]
* 获取子数组[:,:]

### Numpy创建矩阵

* 创建数组array()
* 创建全0数组zeros()/ones
* 创建全值数组full()
* 创建单元数组identity/eye()

#### array
* a= np.array ([2,3,4])
* c = n.array ([[1.0,2.01, [3.0,4.0]1)


#### zeros

* c = np.zeros ((480, 640, 3), np.uint8)
* (480,640,3)（行的个数，列的个数，通道数/层数
* np.uint8矩阵中的数据类型

#### ones

* c = np.ones((480, 640, 3), np.uint8)
* （480，640,3)（行的个数，列的个数，通道数/层数）
* np.uint8矩阵中的数据类型

#### full

* c=np.full((480,540,3),255,np.uint8)
* （480,540,3）（行的个数，列的个数，通道数/层数）
* 255表示每个元素的数值

```
c=np.full((480,540,3),255,np.uint8)
c=np.full((480,540,3),10,np.uint8)
c=np.full((480,540,3),22,np.uint8)
```

#### identity

* c = np.identity(3)
* 斜对角是1,其它为0

#### eye

* c=np.eye((3,5),k=3)
* 可以是非正方形

```
np.eye(5) // 就是一个单位矩阵
np.eye(5, 7)
np.eye(5, 7, 1)
```

### Numpy检索与赋值

* [y, ×]
* [y,x,channel]

```
img = np.zeros((640, 480, 3), np.uint8)
print(img[100, 100])
img[100, 100] = 255
img[100, 100] = [255, 0, 255]
```

### 获取子数组[:,:](Numpy获取子矩阵) Region of Image (ROI)

* [y1:y2,x1:x2]
* [:,:]

```
roi = img[100:200, 100:150]
roi[:, :] = [0, 0, 255]
roi[:] = [0, 0, 255]
roi[:, 10] = [0, 0, 255]
cv2.imshow('roi', roi)
```


### Mat

* Mat是什么
* Mat有什么好处

| 字段 | 说明 |
| --- | --- |
| dims | 维度 |
| rows | 行数 |
| cols | 列数 |
| depth | 像素的位深 |
| channels | 通道数RGB是3 |
| size | 矩阵大小 |
| type | dep+dt+chs CV_8UC3 |
| data | 存放数据 |

#### Mat浅拷贝

c++:
```
Mat A
A = imread (file, IMREAD_COLOR)
Mat B(A);
```

#### Mat深拷贝

c++:
```
cV::Mat::clone()
cv::Mat::copyTo()
```

python:
```
copy()
```

### 通道分离与合井

* split(mat)
* merge((ch1, ch2, ...))







### 人脸识别

* 哈尔（Haar）级联方法
* 深度学习方法(DNN)

### 哈尔级联法
* Haar是专门为解决人脸识别而推出的
* 在深度学习还不流行时，Haar已可以商用

#### Haar人脸识别步骤
* 创建Haar级联器
* 导入图片并将其灰度化
* 调用detectMultiscale方法进行人脸识别

#### detectMultiScale   
* detectMultiScale(img,double scaleFactor = 1.1,int minNeighbors = 3,...);

示例代码：
```
import cv2
import numpy as np


# 第一步，创建哈尔级联器
facer = cv2.CascadeClassifier(
    "./haarcascades/haarcascade_frontalface_default.xml")

# 第二部，导入人脸识别图片并灰度化
img = cv2.imread("./origin/a.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步，人脸识别
faces = facer.detectMultiScale(grayImg, 1.1, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 0, 255), 2)

cv2.imshow('img', img)
key = cv2.waitKey(0)
while True:
    if key & 0xFF == ord('q'):
        break

```

### 其它脸部特征的检测
* 眼
* 鼻子
* 口

haarcascades文件夹路径:
```
/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/cv2/data
```

OpenCV中自带Haar特征分类器

```
haarcascade_frontalface_alt2.xml		
haarcascade_profileface.xml
haarcascade_frontalface_alt_tree.xml		
haarcascade_righteye_2splits.xml
haarcascade_eye.xml				
haarcascade_frontalface_default.xml		
haarcascade_russian_plate_number.xml
haarcascade_eye_tree_eyeglasses.xml		
haarcascade_fullbody.xml			
haarcascade_smile.xml
haarcascade_frontalcatface.xml			
haarcascade_lefteye_2splits.xml			
haarcascade_upperbody.xml
haarcascade_frontalcatface_extended.xml		
haarcascade_license_plate_rus_16stages.xml
haarcascade_frontalface_alt.xml			
haarcascade_lowerbody.xml
```

示例代码：
```
import cv2
import numpy as np


# 第一步，创建哈尔级联器
facer = cv2.CascadeClassifier(
    "./haarcascades/haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

# 第二部，导入人脸识别图片并灰度化
img = cv2.imread("./origin/a.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步，人脸识别
faces = facer.detectMultiScale(grayImg, 1.1, 5)

i = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 0, 255), 2)

    roi_img = img[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(roi_img, 1.1, 5)

    for (x, y, w, h) in eyes:
        cv2.rectangle(roi_img, (x, y), (x + w, y + w), (0, 255, 0), 2)

    cv2.imshow('eye' + str(i), roi_img)
    i += 1

cv2.imshow('img', img)
key = cv2.waitKey(0)
while True:
    if key & 0xFF == ord('q'):
        break

```

### Haar+Tesseract车牌识别

#### 车牌识别的具体步骤
* 通过Haar定位车牌的大体位置
* 对车牌进行预处理
* 调用tesseract进行文字识别

#### 车牌预处理包括的内容
* 对车牌进行二值化处理
* 进行形态学处理
* 滤波去除噪点
* 缩放

#### Tesseract的安装
```
brew install tesseract tesseract-lang // 如果不安装tesseract-lang，只能识别英文，安装了tesseract-lang才能识别中文
pip3 install pytesseract //安装tesseract的python接口
```

测试是否安装成功：
```
tesseract ~/Downloads/WX20230827-213059\@2x.png 1  // 此命令会将制定图片里面的文字识别出来写入1.txt文件
```

代码示例： 
```

import cv2
import numpy as np
# 引入tesseract库
import pytesseract


# 第一步，创建哈尔级联器
# plate = cv2.CascadeClassifier(
#     "./haarcascades/haarcascade_license_plate_rus_16stages.xml")
plate = cv2.CascadeClassifier(
    "./haarcascades/haarcascade_russian_plate_number.xml")

# 第二部，带车牌的图片
img = cv2.imread("./origin/car1.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步，车牌定位
plates = plate.detectMultiScale(grayImg, 1.1, 3)

i = 0
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

if len(plates) > 0:
    # 对获取到的车牌进行预处理
    # 1. 提取ROI
    roi = grayImg[y:y+h, x:x+w]
    # 2. 进行二值化
    ret, roi_bin = cv2.threshold(
        roi, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    plateNum = pytesseract.image_to_string(
        roi_bin, lang='chi_sim+eng', config='--psm 8 --oem 3')
    print(plateNum)

    cv2.imshow('roi_bin', roi_bin)

cv2.imshow('img', img)
key = cv2.waitKey(0)
while True:
    if key & 0xFF == ord('q'):
        break


```