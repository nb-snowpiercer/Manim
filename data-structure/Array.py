from manim import *

class Array(Scene):
    def construct(self):
        square1 = Square(side_length=0.2);
        square1.set_fill(BLUE,opacity=0.5);
        text1 = Text("15");
        square1.surround(text1);
        t1 = Group(text1,square1);
        text2 = Text("42");
        square2 = Square(side_length=0.2);
        square2.set_fill(BLUE,opacity=0.5);
        square2.surround(text2)
        t2 = Group(text2,square2);
        text3 = Text("22");
        square3 = Square(side_length=0.2);
        square3.set_fill(BLUE,opacity=0.5);
        square3.surround(text3)
        t3 = Group(text3,square3);
        text4 = Text("93");
        square4 = Square(side_length=0.2);
        square4.set_fill(BLUE,opacity=0.5);
        square4.surround(text4)
        t4 = Group(text4,square4);
        text5 = Text("24");
        square5 = Square(side_length=0.2);
        square5.set_fill(BLUE,opacity=0.5);
        square5.surround(text5)
        t5 = Group(text5,square5);
        t5.shift(4*RIGHT)
        t4.shift(2*RIGHT)
        t3.shift(0*RIGHT)
        t2.shift(2*LEFT)
        t1.shift(4*LEFT);
        arrow_1 = Arrow(start=UP, end=DOWN, color=GOLD);
        arrow_1.shift(4*LEFT);
        arrow_1.shift(1.5*UP);
        text1 = Text("Array[0]",color=YELLOW,font_size=24)
        text1.next_to(t1,DOWN);
        text2 = Text("Array[1]",color=YELLOW,font_size=24)
        text2.next_to(t2,DOWN);
        text3 = Text("Array[2]",color=YELLOW,font_size=24)
        text3.next_to(t3,DOWN);
        text4 = Text("Array[3]",color=YELLOW,font_size=24)
        text4.next_to(t4,DOWN);
        text5 = Text("Array[4]",color=YELLOW,font_size=24)
        text5.next_to(t5,DOWN);
        self.add(t1);
        self.add(t2);
        self.add(t3);
        self.add(t4);
        self.add(t5);
        self.add(arrow_1);
        self.play(Write(text1))
        self.wait(1);
        self.play(FadeOut(text1),shift=UP)
        self.play(
			arrow_1.animate.shift(2*RIGHT),
			run_time=2
			)
        self.play(Write(text2))
        self.wait(1);
        self.play(FadeOut(text2),shift=UP)
        self.play(
			arrow_1.animate.shift(2*RIGHT),
			run_time=2
			)
        self.play(Write(text3))
        self.wait(1);
        self.play(FadeOut(text3),shift=UP)
        self.play(
			arrow_1.animate.shift(2*RIGHT),
			run_time=2
			)
        self.play(Write(text4))
        self.wait(1);
        self.play(FadeOut(text4),shift=UP)
        self.play(
			arrow_1.animate.shift(2*RIGHT),
			run_time=2
			)
        self.play(Write(text5))
        self.play(FadeOut(text5),shift=UP)


