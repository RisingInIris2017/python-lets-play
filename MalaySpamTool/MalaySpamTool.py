import win32con
import win32clipboard

print('本程序可以模仿马雷用人名刷屏的行为.\n')
inputString = input("请输入要重复的字符串:\n")
if(inputString ==""):
    print("使用默认重复串。\n")
    inputString = "malayniubi"
inputTimes = abs(int(input("请输入要重复的次数:\n")))
if(inputTimes == 0):
    print("至少重复一次。\n已使用默认重复次数 100。\n")
    inputTimes = 100
print("你的马雷序列如下:\n")
MalayString = (inputString.lower()+inputString.upper())*inputTimes
print(MalayString)
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, MalayString)
win32clipboard.CloseClipboard()
print("已经将结果输出到剪贴板。\n按任意键退出程序。\n")
input()
