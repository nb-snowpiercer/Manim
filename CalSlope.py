#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

#计算y=x**2的斜率

class CalSlope(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 4,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,11,1),
        "x_labeled_nums": list(np.arange(0, 5, 1)),
        "x_label_decimal":1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_width":8
    }

    def construct(self):
        self.setup_axes(animate=False) #animate=True to add animation
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph = self.get_graph(lambda x : x**2, 
                                    color = BLUE_E,
                                    x_min = 0, 
                                    x_max = 4
                                    )

        funtext = TextMobject("$y  = x^2 $").scale(2)
        self.play(
            Write(funtext),
            funtext.shift, 3*UP,
            funtext.shift, 2*RIGHT,
            ShowCreation(graph),
            run_time = 8
        )

        line = self.get_graph(lambda x:  4*x -3,
                                color = RED,
                                x_min = 1,
                                x_max = 3
                                )


        p1 = Dot().move_to(self.coords_to_point(3,9));

        p2 = Dot().move_to(self.coords_to_point(2,4));

        p3 = Dot().move_to(self.coords_to_point(1,1));

        self.play(
            Write(p1),
            p1.set_color,YELLOW,
            Write(p3),
            p3.set_color,RED,
            ShowCreation(line),
            run_time =8
        )

        self.play(
            Transform(p1,p2),
            FadeOut(line),
            run_time =8
        )

        line1 = self.get_graph(lambda x:  3*x -2,
                                color = RED,
                                x_min = 1,
                                x_max = 2
                                )
        self.play(
            ShowCreation(line1),
            run_time =8
        )


        self.play(
            FadeOut(line1),
            Transform(p2,p3),
            FadeOut(p1),
            run_time =8
        )

        line2 =  self.get_graph(lambda x:  2*x -1,
                                color = GREEN_SCREEN,
                                x_min = 0,
                                x_max = 2
                                )
        self.play(
            FadeOut(p2),
            ShowCreation(line2),
            run_time =8
        )

        # text = TextMobject("Slope = $\\frac{dy}{dx}$").scale(2)
        # text2 = TextMobject("$2x$").scale(2)
        # text2.next_to(text,UP,buff=1)
        # text2.next_to(text,RIGHT,buff=1)

        # self.play(
        #     text.shift, RIGHT*3,
        #     run_time =8
        # )

        # self.play(
        #     text2.set_color, GREEN,
        #     Transform(text,text2),
        #     run_time =8
        # )

        # line3 =  self.get_graph(lambda x:  1,
        #                         color = WHITE,
        #                         x_min = 1,
        #                         x_max = 2
        #                         )
        line3 = Line(0.5*LEFT,RIGHT)
        line3.set_color(WHITE)
        line3.shift(3.5*LEFT)
        line3.shift(2.5*DOWN)
        # line3 = Line(start=np.array((1,1,0)),end=np.array((2,1,0)))
        # line3.shift(5.5*LEFT)
        # line3.shift(2.5*DOWN)
        dx = TextMobject("$\\Delta x = dx$")
        dx.next_to(line3,DOWN,buff=0.2)


        self.play(
            ShowCreation(line3),
            run_time = 4
        )

        self.play(
            Write(dx),
            run_time = 4
        )

        # line4 =  self.get_graph(lambda x:  2,
        #                         color = WHITE,
        #                         y_min = 1,
        #                         y_max = 2
        #                         )

        line4 = Line(UP,ORIGIN)
        line4.set_color(WHITE)
        line4.set_width(0.5)
        line4.shift(3*DL)
        line4.shift(0.5*UP)
        line4.shift(0.5*RIGHT)
        dy = TextMobject("$dy$")
        dy.next_to(line4,RIGHT,buff=0.2)

        self.play(
            ShowCreation(line4),
            run_time =4
        )


        self.play(
            Write(dy),
            run_time =4
        )

        line5 = Line(0.3*UP,ORIGIN)
        line5.set_color(RED_E)
        line5.shift(3*DL)
        line5.shift(1.5*UP)
        line5.shift(0.5*RIGHT)
        dy2 = TextMobject("$o(\\Delta x)$")
        dy2.next_to(line5,RIGHT,buff=0.2)

        self.play(
            ShowCreation(line5),
            run_time =4
        )


        self.play(
            Write(dy2),
            run_time =4
        )

        # self.remove(dx,dy,dy2)

        tan  = TextMobject("$\\displaystyle \\frac{dy}{dx} = \\lim_{\\Delta x \\rightarrow 0} \\frac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x}$")
        self.play(
            tan.shift, DR*2,
            run_time =8
        )
        self.wait()