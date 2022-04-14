from manim import *

class SetOperations(Scene):
    def construct(self):
        circle1 = Circle(radius=2.0, fill_opacity=0.5, color=BLUE, stroke_width=10).move_to(LEFT)
        set_ops_text = MarkupText("<u>Set Operation</u>").next_to(circle1, UP * 3)
        group = Group(set_ops_text, circle1).move_to(LEFT * 3)
        self.play(FadeIn(group))

        element1 = Circle(radius=1.0,color=WHITE);
        text1 = Text("23")
        element1.surround(text1);
        t1 = Group(text1,element1);
        t1.shift(5*RIGHT);
        self.play(t1.animate.scale(0.5).move_to(LEFT*3));

        element2 = Circle(radius=1.0,color=GREEN);
        text2 = Text("43")
        element2.surround(text2);
        t2 = Group(text2,element2);
        t2.shift(5*RIGHT);
        t2.shift(3*DOWN);
        self.play(t2.animate.scale(0.5).move_to(DOWN+LEFT*3.2));

        element3 = Circle(radius=1.0,color=YELLOW);
        text3 = Text("51")
        element3.surround(text3);
        t3 = Group(text3,element3);
        t3.shift(5*RIGHT);
        t3.shift(3*DOWN);
        self.play(t3.animate.scale(0.5).move_to(DOWN+LEFT*2));

        element4 = Circle(radius=1.0,color=PURPLE);
        text4 = Text("43")
        element4.surround(text4);
        t4 = Group(text4,element4);
        t4.shift(5*RIGHT);
        t4.shift(3*DOWN);
        self.play(t4.animate.scale(0.5).move_to(2*DOWN+LEFT*3));

        title=Text("43元素已经存在");
        title.shift(2*RIGHT);
        self.play(Write(title));
        self.play(FadeOut(t4),shift=DOWN);

        element5 = Circle(radius=1.0,color=PINK);
        text5 = Text("81")
        element5.surround(text5);
        t5 = Group(text5,element5);
        t5.shift(5*RIGHT);
        t5.shift(3*DOWN);
        self.play(t5.animate.scale(0.5).move_to(DOWN+LEFT*4));
        self.wait(2);
