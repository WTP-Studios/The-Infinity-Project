# 语言选择
print("The recognition of this script is strictly case sensitive, please enter it correctly！")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
print(''' 
[zh-cmn-Hans] 简体中文 (中国大陆)
[zh-cmn-Hant] 繁體中文 (中國台灣,中國香港,中國澳門)
[en] English (United States, United Kingdom and so on)''')
Language = input("请在此输入上方 [] 内 的字符 : ")

# 模块导入
import win32api
import tkinter
import win32con
import speech

# while 判断 及 窗口。
count = 3
while count > 0:
    if Language == 'zh-cmn-Hans':
        letter = input("Please type the letter : ")
        if letter == 'xzsx':
            print("恭喜你!你成功输入了密码!")
            print("xzsx的意思是:小猪是屑!(拼音输入法)")
            win32api.MessageBox(None,"小猪屑！","WTP016 迫害窗口",win32con.MB_OK)
            speech.say("小猪太屑了!")
            exit("希望还能再见!")
        else:
            print("你输入的字母错误!请再次输入!")
            count = 3 - 1

    if Language == 'zh-cmn-Hant':
        letter = input("Please type the letter : ")
        if letter == 'xzsx':
            print("恭喜你!你成功輸入了密碼!")
            print("xzsx的意思是:小豬是屑!(中國大陸拼音输入法)")
            win32api.MessageBox(None,"小猪是屑!","WTP016 的 迫害窗口",win32con.MB_OK)
            speech.say("小猪太屑了!")
            exit("See you again!")
        else:
            print("你輸入的字母錯誤!請重新輸入!")
            count = 3 - 1

    if Language == 'en':
        letter = input("Please type the letter : ")
        if letter == 'xzsx':
            print("Congratulations!You type letter is right!")
            print("The letter 'xzsx' mean:xiaozhu_zty is xie!")
            win32api.MessageBox(None,"xiaozhu_zty is xie!","WTP016's PoHai windows",win32con.MB_OK)
            speech.say("xiaozhu_zty is so xie!")
            exit("Goodbye!")
        else:
            print("The letter you entered is incorrect! Please enter again!")
            count = 3 - 1

# 此版本加入了 speech 模块。

