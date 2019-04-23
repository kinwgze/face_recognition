#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipFace
import base64
import json
import numpy as np
import cv2
import datetime
import tkinter.messagebox

#调用笔记本内置摄像头
cap=cv2.VideoCapture(0)

while True:
    #从摄像头读取图片
    sucess, img=cap.read()
    #显示摄像头
    cv2.imshow("img",img)
    #保持画面的持续。
    k=cv2.waitKey(1)
    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):
        #通过s键保存图片，并退出。
        cv2.imwrite("1.jpg",img)
        cv2.destroyAllWindows()
        break

#关闭摄像头
cap.release()

#调用百度API
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#图片对比
result = client.match([
    {
        'image': str(base64.b64encode(open('1.jpg', 'rb').read()),'utf-8'),
        'image_type': 'BASE64',
    },
    {
        'image': str(base64.b64encode(open('2.jpg', 'rb').read()),'utf-8'),
        'image_type': 'BASE64',
    }
])
#相似度分数
result_score = result['result']['score']
#print(result_score)

#签到成功/失败的提示
if result_score > 80:
    tkinter.messagebox.showinfo("人脸识别","是同一个人！")
else:
    tkinter.messagebox.showerror("人脸识别", "不是同一个人！")




