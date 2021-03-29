from manimlib import *

'''开头画面'''
def title(self):
    luatos = Text("LuatOS",size=1.5,color=BLUE)
    title = Text("物联网小白变大神",size=1.5)
    sub = Text("教程概述",color=YELLOW_D)
    all = VGroup(luatos,title,sub).arrange(DOWN,buff=1)
    self.play(Write(luatos))
    self.play(Write(title))
    self.wait()
    self.play(FadeIn(sub,UP))
    self.wait(3)
    self.play(FadeOut(all,UP))

'''
欢迎来到LuatOS物联网小白变大神系列教程
本教程将分为两个系列
开发基础 和 开发实战
首先介绍一下基础教程的规划
基础教程将会分为三节来讲解
第一节会lua基础语法部分
包含了开发时必要的lua语法知识
第二节是luatask框架部分
这部分是luat开发的精髓部分
可以让人在无穷的定时器逻辑中解脱出来
最后就是高级的知识部分
前面两节忽略掉的复杂知识内容
都会在这一节进行讲解
当然，普通开发的话，前面两节是完全够用的
接下来就是实战教程
实战教程这部分，会从烧录代码开始
手把手教大家吧所有例程过一遍
最后还带大家开发几套完整的项目
'''
def threeParts(self):
    t2 = Text("开发实战")
    title = Text("开发基础")
    VGroup(title,t2).arrange(DOWN)
    self.play(Write(title))
    self.wait()
    self.play(Write(t2))
    self.wait(2)
    self.play(Transform(title,title.copy().scale(0.6).to_corner(LEFT+UP)),FadeOut(t2))
    self.wait(2)
    r = []
    for i in range(0,3):
        r.append(Rectangle(width=3,height=4).set_color(YELLOW_A))
    t = [
        Text("Lua基础",color=GREEN_A,size=0.8),
        Text("LuaTask",color=BLUE_A,size=0.8),
        Text("Lua进阶",color=PURPLE_A,size=0.8),
    ]
    rv = VGroup()
    for i in range(0,3):
        rv.add(VGroup(r[i],t[i]).arrange(UP)).arrange(RIGHT,buff = 1)

    self.play(*[ShowCreation(i) for i in r])
    self.wait()
    content = [
        Text("基础语法\n\n\n..."),
        Text("定时器\n\n\n多任务\n\n\n消息分发\n\n\n..."),
        Text("正则\n\n\n元表\n\n\n协程\n\n\n..."),
    ]
    commit = [
        Text("Lua基本用法"),
        Text("Task开发核心思想"),
        Text("较为复杂的部分"),
    ]
    for i in range(0,3):
        self.play(Write(t[i]))
        self.play(Write(content[i].scale(0.5).move_to(r[i])))
        self.wait(3)
        self.play(Write(commit[i].scale(0.5).next_to(r[i],DOWN)))
        self.wait(2)
    self.wait()
    all = VGroup(*self.mobjects)
    #开发实战
    self.play(Transform(all,t2))
    self.wait(2)
    self.clear()
    self.play(Transform(t2,t2.copy().scale(0.6).to_corner(LEFT+UP)))
    self.wait(3)
    self.play(Write(Text("从烧录到示例代码\n\n全部讲一遍")))
    self.wait(5)
    self.play(*[FadeOut(i) for i in self.mobjects])

'''
Lua开发有什么优势呢
lua可以说是脚本语言中
运行速度最快的语言了
左侧可以看一下和其他语言运行速度的比较
两段代码同时运行一下
我们先等等右边那个，讲一下其他内容
lua用不到100K的代码
实现了一套完整的虚拟机
占用资源可以说是极低的
上到游戏，下到物联网设备
都可以随意嵌入
同时，因为语法简单
上手难度也不高
lua的关键字很少
但是却可以实现协程和面向对象的特性
好啦，左下角的代码都运行完了
我们来继续介绍下面的内容
'''
def why(self):
    title = Text("为什么选择Lua？")
    self.play(Write(title))
    self.wait()
    self.play(Transform(title,title.copy().scale(0.6).to_corner(LEFT+UP)))
    self.wait(2)
    fast = Text("快！",color=RED,size=4)
    self.play(FadeIn(fast,RIGHT),run_time=0.5)
    self.play(FadeOut(fast,RIGHT),run_time=0.5)
    self.wait(1)
    codeLua = Text(
        "r = 0\n\nn = 1\n\nfor i=1,300000 do\n\n    r = r + n\n\nend\n\nprint(r)",
        font="Consolas",size=0.3,
        t2c={
            "i":RED_B,"n":RED_B,"r":RED_B,
            "for":PURPLE,"do":PURPLE,"end":PURPLE,
            "0":GREEN,"1":GREEN,"3":GREEN,"print":BLUE,
            "=":TEAL_B,"+":TEAL_B,"(":MAROON,")":MAROON,
        })
    codePy = Text(
        "r = 0\n\nn = 1\n\nfor i in range(0,300000):\n\n    r = r + n\n\n\n\nprint(r)",
        font="Consolas",size=0.3,
        t2c={
            "i":RED_B,"n":RED_B,"r":RED_B,
            "for":PURPLE,"do":PURPLE,"end":PURPLE,
            "0":GREEN,"1":GREEN,"3":GREEN,
            "print":BLUE,"range":BLUE,
            "=":TEAL_B,"+":TEAL_B,"(":MAROON,")":MAROON,
        })
    gl = VGroup(Text("LuatOS",size=0.3),codeLua).arrange(DOWN)
    gp = VGroup(Text("另一种语言",size=0.3),codePy).arrange(DOWN)
    gc = VGroup(gl,gp).arrange(RIGHT,buff=1).to_corner(LEFT+DOWN).shift(np.array([0,1,0]))
    self.play(Write(gc))
    self.wait(3)
    runl = Text("运行！",size=0.5,color=RED).next_to(gl,DOWN)
    runp = Text("运行！",size=0.5,color=RED).next_to(gp,DOWN)
    self.play(FadeIn(runl,DOWN),FadeIn(runp,DOWN))
    self.play(FadeOut(runl,DOWN),FadeOut(runp,DOWN))
    pl = Text("运行中...",size=0.5).next_to(gl,DOWN)
    pp = Text("运行中...",size=0.5).next_to(gp,DOWN)
    self.play(Write(pl),Write(pp))
    self.play(FadeOut(pl),run_time=0)
    pl = Text("输出：300000",size=0.5).next_to(gl,DOWN)
    self.play(FadeIn(pl),run_time=0)
    self.wait(5)

    t = [
        Text("资源占用极低",size=0.6),
        Text("大量行业都在使用",size=0.6),
        Text("上手极为容易",size=0.6),
    ]
    VGroup(*t).arrange(DOWN,buff=0.1).to_corner(RIGHT+UP,buff=2)
    for i in range(0,3):
        self.play(Write(t[i]))
        self.wait(10)
    self.play(FadeOut(pp),run_time=0)
    pp = Text("输出：300000",size=0.5).next_to(gp,DOWN)
    self.play(FadeIn(pp),run_time=0)
    self.wait(5)
    self.play(*[FadeOut(i) for i in self.mobjects])

'''
你可能会对本系列教程有一些疑问
本教程会尽量照顾零基础的用户
使用简明易懂的方式，帮助大家理解
提问的方式也有很多
弹幕、视频评论区和qq群都可以进行提问
教程中大部分内容都可以在线模拟
luatos提供了纯网页版本的模拟器
可以轻松地测试软件代码
本教程的内容仍然在制作中
如果你有更好的建议
或者想参与我们制作
可以直接在评论区进行留言
会有专人进行私信联系
'''
def feedBack(self):
    title = Text("相关问题")
    self.play(Write(title))
    self.wait()
    self.play(Transform(title,title.copy().scale(0.6).to_corner(LEFT+UP)))
    q = [
        Text("适合零基础的人吗？"),
        Text("提问渠道？"),
        Text("测试代码？"),
        Text("参与制作？"),
    ]
    a = [
        Text("教程对小白人群友好"),
        Text("弹幕、评论、QQ群"),
        Text("wiki.luatos.com的模拟器"),
        Text("评论区留言"),
    ]
    l = []
    for i in range(0,len(a)):
        q[i].scale(0.6)
        a[i].scale(0.6)
        l.append(VGroup(q[i],a[i]).arrange(RIGHT))
    VGroup(*l).arrange(DOWN)
    for i in range(0,len(a)):
        self.play(Write(q[i]))
        self.wait(2)
        self.play(Write(a[i]))
        self.wait(5)
    self.wait()
    self.play(*[FadeOut(i) for i in self.mobjects])

'''
为获得后期的更新，欢迎关注本账号！
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
    self.play(FadeIn(Text("每日喝粥团队制作",color=BLUE_A).to_corner(RIGHT+DOWN),UP))
    self.wait(5)
    self.play(*[FadeOut(i) for i in self.mobjects])

class V(Scene):
    def construct(self):
        title(self)
        threeParts(self)
        why(self)
        feedBack(self)
        endInfo(self)
