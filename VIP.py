#! /usr/bin/python3
# -*-coding:UTF-8-*-
import requests
import re
import tkinter as tk
import webbrowser

url = "http://www.qmaile.com/"
response = requests.get(url)
response.encoding="utf-8"
# print(response.text)
responsed = response.text

#利用正则表达式爬取解析API
reApi = re.compile('<option value="(.*?)" selected="">')

#获得解析API
api = re.findall(reApi,responsed)

#点击播放响应函数
def play():
    webbrowser.open(var.get()+entry.get())

#点击清除响应函数
def clean():
    entry.delete(0,"end")

#创建窗口
view = tk.Tk()
view.geometry("500x250")
view.title("全民解析-vip视频在线解析")
# view.iconbitmap("D:/PyDemo/movie/vip.ico")
label1 = tk.Label(view,text="播放接口:",font=12)
label1.grid()

var = tk.StringVar()
#循环遍历接口选项
for index in range(len(api)):
    tk.Radiobutton(view, text="播放接口"+ str(index+1), variable=var, value=api[index]).grid(row=str(index), column=1)

label2 = tk.Label(view,text="播放链接:",font=12)
label2.grid(row=str(len(api)+1),column=0)

entry = tk.Entry(view,text="",width=55)
entry.grid(row=str(len(api)+1),column=1)

button1 = tk.Button(view,text="播放",font=12,width=8,command=play)
button1.grid(row=str(len(api)+2),column=1)
button1 = tk.Button(view,text="清除",font=12,width=8,command=clean)
button1.grid(row=str(len(api)+3),column=1)
view.mainloop()
