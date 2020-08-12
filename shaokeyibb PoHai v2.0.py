# 语言选择
print('''
语言选择菜单 Language Choose Menu
[zh-cn] 中文(简体) Chinese (Simplified)
[zh-tw] 中文(繁体) Chinese (Traditional)
[en] 英语 English''')
Language = input("请输入上方 [] 中的内容 : ")

# 模块导入
import win32api
import tkinter
import win32con
import speech

counts = 3
while counts > 0:
    if Language == 'zh-cn':
        zhcndigital = input("请输入密码 : ")
        if zhcndigital == '贺兰是屑':
            print("恭喜你!你成功输入了密码!")
            print("注意:下面即将打开Win32API窗口，请您点击OK以继续!")
            win32api.MessageBox(None,"贺兰屑！","WTP016 迫害窗口",win32con.MB_OK)
            speech.say("贺兰太屑了!")
            exit("希望还能再见!")
        else:
            print("你输入的字母错误!请再次输入!")
            counts = 3 - 1

    if Language == 'zh-tw':
        zhtwdigital = input("請輸入密碼 : ")
        if zhtwdigital == '賀蘭是屑':
            print("恭喜你!你成功輸入了密碼!")
            print("下方即將打開Win32API窗口，請點擊OK以繼續腳本！")
            win32api.MessageBox(None,"賀蘭是屑！","WTP016 的 Python 迫害窗口",win32con.MB_OK)
            speech.say("賀蘭太屑了!")
            exit("腳本已結束。")
        else:
            print("你的密碼輸入錯誤，請再次輸入！")
            counts = 3 - 1

    if Language == 'en':
        endigital = input("Please type the password : ")
        if endigital == 'shaokeyibb is shit!':
            print("Congratulations! You type's password is right!")
            print("Next, the program will open a Win32API window, please click OK to let the program carry on!")
            win32api.MessageBox(None,"shaokeyibb is shit!","WTP016's Python Shit Window",win32con.MB_OK)
            speech.say("shaokeyibb is shit!")
            exit("Goodbye!")
        else:
            print("The password you entered is incorrect! Please enter again!")
            counts = 3 - 1

print("游戏结束了!")
print("The Game is end!")