Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from PIL import Image

from pylab import *



work_dir = "D:/inquisit/gray/"

#转换成矩阵

im = array(Image.open("D:\inquisit\gray\chicken.jpg").convert('L'))

#生成灰度图

im1 = Image.fromarray(uint8(im))

im1.save(work_dir+"grey.jpg")

#生成不同灰度差异的图

for i in range(0, 255, 32):
    
    image = (i/255)*im

    out = Image.fromarray(uint8(image))

    ii = 8-i/32

out.save(work_dir+str(ii)+".jpg")
