from manimlib import *

'''开头画面'''
def title(self):
    title = Text("Luat 开发教程",size=1.5,t2c={"Luat":BLUE})
    sub = Text("教程概述",color=YELLOW_D)
    all = VGroup(title,sub).arrange(DOWN,buff=1)
    self.play(Write(title))
    self.wait()
    self.play(FadeIn(sub,UP))
    self.wait(3)
    self.play(FadeOut(all,UP))

'''
欢迎来到Luat开发系列教程
本教程的重点，主要会在软件开发
教程会分为三个部分
lua基础、luatask和lua进阶
'''
def threeParts(self):
    title = Text("Luat 开发教程",t2c={"Luat":BLUE})
    self.play(Write(title))
    title2 = Text("Luat 开发教程",t2c={"Luat":BLUE},size=0.6)
    title2.to_corner(LEFT+UP)
    self.play(Transform(title,title2))
    r = []
    for i in range(0,3):
        r.append(Rectangle(width=3,height=4).set_color(YELLOW_A))
    t = [
        Text("Lua基础",color=GREEN_A),
        Text("LuaTask",color=BLUE_A),
        Text("Lua进阶",color=PURPLE_A),
    ]
    rv = VGroup()
    for i in range(0,3):
        rv.add(VGroup(r[i],t[i]).arrange(UP)).arrange(RIGHT,buff = 1)

    self.play(*[ShowCreation(i) for i in r])
    self.wait()
    content = [
        Text("基础语法\n\n\n...",size=0.5),
        Text("定时器\n\n\n多任务\n\n\n消息分发\n\n\n...",size=0.5),
        Text("正则\n\n\n元表\n\n\n协程\n\n\n...",size=0.5),
    ]
    for i in range(0,3):
        content[i].move_to(r[i])
        self.play(Write(t[i]),Write(content[i]))
        self.wait()
    self.wait()
    self.play(*[FadeOut(i) for i in self.mobjects])

'''
同时，每个知识点都会尽量照顾零基础用户
如果在观看过程中有疑问
可以直接发弹幕、或者在视频评论区留言
同时也可以加入讨论群
群号会在评论区给出
'''
def feedBack(self):
    t = [
        Text("零基础 √",f2c={"√":GREEN_B}),
        Text("弹幕、评论"),
        Text("QQ群"),
    ]
    VGroup(*t).arrange(DOWN,buff=1)
    for i in t:
        self.play(Write(i))
        self.wait(2)
    self.play(*[FadeOut(i) for i in self.mobjects])

'''
该系列教程将持续更新，欢迎关注
'''
def endInfo(self):
    t = [
        Text("感谢您看到最后！",size=0.5),
        Text("为获得后面的更新",size=0.5),
        Text("欢迎关注本帐号",size=0.5),
        Text("也欢迎分享该视频",size=0.5),
    ]
    VGroup(*t).arrange(DOWN,buff=0.5).to_corner(LEFT+UP,buff=2)
    for i in t:
        self.play(Write(i))
        self.wait()
    self.wait()
    self.play(FadeIn(Text("by Luat",color=BLUE_A).to_corner(RIGHT+DOWN),UP))
    self.wait(5)
    self.play(*[FadeOut(i) for i in self.mobjects])

class V(Scene):
    def construct(self):
        title(self)
        threeParts(self)
        feedBack(self)
        endInfo(self)
