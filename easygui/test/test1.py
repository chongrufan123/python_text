import easygui as g
import sys

g.msgbox("欢迎来到选择小游戏")

while(1):
    msg = "请问你想要学习什么知识呢"
    title = "小游戏互动"
    choices = ["xxoo", "琴棋书画", "变成", "睡觉"]

    choice = g.choicebox(msg, title, choices)

    g.msgbox("你的选择是", str(choice), "结果")

    msg = "你要重新开始吗"
    title = "请选择"

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
