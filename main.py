'''
    跳一跳辅助：adb
'''
__author__='how'
import os
import PIL,numpy
import matplotlib.pyplot as plt#图片分析
from matplotlib.animation import FuncAnimation#更新
import time
need_update=True
def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')#获取手机截图
    os.system('adb pull /sdcard/screen.png')#加载到文件夹
    return numpy.array(PIL.Image.open('screen.png'))#返回一个图片数组
def jump_to_next(point1,point2):
    x1,y1=point1;x2,y2=point2
    dis=((x2-x1)**2+(y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(dis*1.35)))#一个像素点按1.35ms
def on_click(event,coor=[]):
    global need_update
    coor.append((event.xdata,event.ydata))
    if len(coor)==2:
        need_update=True
        return jump_to_next(coor.pop(),coor.pop())#传递完后清空列表

def update_screen(frame):#重画图片
    global need_update
    if need_update==True:
        time.sleep(1)#跳的时间
        axes_images.set_array(get_screen_image())
        need_update=False
figure=plt.figure()#建一个空白图像
axes_images=plt.imshow(get_screen_image(),animated=True)#把获取到的图片放在坐标轴上
figure.canvas.mpl_connect('button_press_event',on_click)#点击触发on_click事件
Ani=FuncAnimation(figure,update_screen,interval=50)#一直循环
plt.show()

