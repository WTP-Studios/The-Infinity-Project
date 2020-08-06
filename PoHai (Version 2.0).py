# 语言选择
print("The recognition of this script is strictly case sensitive, please enter it correctly！")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
Language = input("请问你使用什么语言?如果你使用中文(简体)输入zh-cmn-Hans，使用中文(繁体)输入zh-cmn-Hant，使用英语输入en。")

# 模块导入
import win32api
import win32con

# while 判断 及 窗口。
count = 3
while count >= 0:
    if Language == 'zh-CN':
        letter = input("Please type the letter")
        if letter == 'xzsx':
            print("恭喜你!你成功输入了密码!")
            print("xzsx的意思是:小猪是屑!(拼音输入法)")
            win32api.MessageBox(None,"小猪屑！","WTP016 迫害窗口",win32con.MB_OK)
            break
        else:
            print("你输入的数字错误!请再次输入!")
            count = 3 - 1

    if Language == 'zh-TW':
        letter = input("Please type the letter")
        if letter == 'xzsx':
            print("恭喜你!你成功輸入了密碼!")
            print("xzsx的意思是:小豬是屑!(中國大陸拼音输入法)")
            win32api.MessageBox(None,"小猪是屑!","WTP016 的 迫害窗口",win32con.MB_OK)
            break
        else:
            print("你輸入的数字錯誤!請重新輸入!")
            count = 3 - 1

    if Language == 'en-UK':
        letter = input("Please type the letter")
        if letter == 'xzsx':
            print("Congratulations!You type letter is right!")
            print("The letter 'xzsx' mean:xiaozhu_zty is xie!")
            win32api.MessageBox(None,"xiaozhu_zty is xie!","WTP016's PoHai windows",win32con.MB_OK)
            break
        else:
            print("The letter you entered is incorrect! Please enter again!")
            count = 3 - 1

# 此版本使用了 win32api 和 win32con 模块 并 加入了 次数统计 (while True , count 与 break)
# 即将加入:
# speech模块
# 此版本已知BUG: 语言文本未更改。

