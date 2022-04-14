from manim import *

class ArrayList(Scene):
    def construct(self):
        square1 = Square(side_length=0.2);
        square1.set_fill(BLUE,opacity=0.5);
        label1 = Text("12");
        square1.surround(label1);
        t1 = Group(label1,square1);
        label2 = Text("22");
        square2 = Square(side_length=0.2);
        square2.set_fill(BLUE,opacity=0.5);
        square2.surround(label2)
        t2 = Group(label2,square2);
        label3 = Text("32");
        square3 = Square(side_length=0.2);
        square3.set_fill(BLUE,opacity=0.5);
        square3.surround(label3)
        t3 = Group(label3,square3);
        label4 = Text("42");
        square4 = Square(side_length=0.2);
        square4.set_fill(BLUE,opacity=0.5);
        square4.surround(label4)
        t4 = Group(label4,square4);
        label5 = Text("52");
        square5 = Square(side_length=0.2);
        square5.set_fill(BLUE,opacity=0.5);
        square5.surround(label5)
        t5 = Group(label5,square5);
        t5.shift(4*RIGHT)
        t4.shift(2*RIGHT)
        t3.shift(0*RIGHT)
        t2.shift(2*LEFT)
        t1.shift(4*LEFT);
        text1 = Text("12",color=YELLOW,font_size=24)
        text1.next_to(square1,DOWN);
        text2 = Text("22",color=YELLOW,font_size=24)
        text2.next_to(t2,DOWN);
        text3 = Text("32",color=YELLOW,font_size=24)
        text3.next_to(t3,DOWN);
        text4 = Text("42",color=YELLOW,font_size=24)
        text4.next_to(t4,DOWN);
        text5 = Text("52",color=YELLOW,font_size=24)
        text5.next_to(t5,DOWN);
        title = Text("ArrayList添加元素操作",color=WHITE,fill_opacity=0.8,font_size=36)
        title.shift(3*UP);
        self.play(Write(title));
        self.play(FadeIn(square1),shift=LEFT,run_time =2)
        self.play(Write(text1),run_time =1);
        self.play(FadeIn(t1),shift=LEFT,run_time =1);
        self.play(FadeOut(text1),shift=DOWN,run_time=1);
        arrow_1 = Arrow(start=0.5*RIGHT, end=0.5*LEFT, color=GREEN);
        arrow_1.shift(3*LEFT);
        self.play(FadeIn(arrow_1),shift=LEFT,
        run_time =1)
        self.play(FadeIn(square2),shift=LEFT,run_time =1)
        self.play(Write(text2),run_time =1);
        self.play(FadeOut(text2),shift=DOWN,run_time=1);
        self.play(FadeIn(t2),shift=LEFT,
        run_time =1)
        arrow_2 = Arrow(start=0.5*RIGHT, end=0.5*LEFT, color=GREEN);
        arrow_2.shift(1*LEFT);
        self.play(FadeIn(arrow_2),shift=LEFT,
        run_time =1)
        self.play(FadeIn(square3),shift=LEFT,run_time =1)
        self.play(Write(text3),run_time =1);
        self.play(FadeOut(text3),shift=DOWN,run_time=1);
        self.play(FadeIn(t3),shift=LEFT,
        run_time =1)
        arrow_3 = Arrow(start=0.5*RIGHT, end=0.5*LEFT, color=GREEN);
        arrow_3.shift(1*RIGHT);
        self.play(FadeIn(arrow_3),shift=RIGHT,
        run_time =1)
        self.play(FadeIn(square4),shift=LEFT,run_time =1)
        self.play(Write(text4),run_time =1);
        self.play(FadeOut(text4),shift=DOWN,run_time=1);
        self.play(FadeIn(t4),shift=RIGHT,
        run_time =1)
        arrow_4 = Arrow(start=0.5*RIGHT, end=0.5*LEFT, color=GREEN);
        arrow_4.shift(3*RIGHT);
        self.play(FadeIn(arrow_4),shift=RIGHT,
        run_time =1)
        self.play(FadeIn(square5),shift=LEFT,run_time =1)
        self.play(Write(text5),run_time =1);
        self.play(FadeOut(text5),shift=DOWN,run_time=1);
        self.play(FadeIn(t5),shift=RIGHT,
        run_time =1)