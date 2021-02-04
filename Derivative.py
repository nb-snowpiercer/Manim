#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

#计算y=x**2的斜率

class Derivative(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 5,
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

        graph = self.get_graph(lambda x : x**2, 
                                    color = WHITE,
                                    x_min = 0, 
                                    x_max = 4
                                    )

        funtext = TextMobject("$y  = x^2 $")
        funtext.set_color(YELLOW_E)
        self.play(
            Write(funtext),
            funtext.shift, 3*UP,
            funtext.shift, 1*RIGHT,
            ShowCreation(graph),
            run_time = 8
        )

        vline1 = self.get_vertical_line_to_graph(3,graph,DashedLine,color = GREY)

        vline2 = self.get_vertical_line_to_graph(1,graph,DashedLine,color = GREY)
        self.play(
            Write(vline1),
            Write(vline2),
            run_time = 5
        )

        graph1 = self.get_graph(lambda x : x**2, color = WHITE,
                                    x_min = 3, 
                                    x_max = 2
                                    )


        line = self.get_graph(lambda x:  4*x -3,
                                color = WHITE,
                                x_min = 1,
                                x_max = 3
                                )


        p1 = Dot().move_to(self.coords_to_point(1,1));

        p2 = Dot().move_to(self.coords_to_point(3,9));

        p = Dot().set_color(YELLOW)

        self.play(
            Write(p1),
            p1.set_color,YELLOW,
            Write(p2),
            p2.set_color,YELLOW,
            ShowCreation(line),
            run_time = 5
        )

        self.remove(p2,line,vline1,vline2)

        self.play(
            MoveAlongPath(p,graph1),rate_func=linear,
            run_time = 5
        )

        self.remove(p)

        p2 = Dot().move_to(self.coords_to_point(2,4));

        line = self.get_graph(lambda x:  3*x -2,
                                color = WHITE,
                                x_min = 1,
                                x_max = 2
                                )

        vline1 = self.get_vertical_line_to_graph(2,graph,DashedLine,color = GREY)

        vline2 = self.get_vertical_line_to_graph(1,graph,DashedLine,color = GREY)

        self.play(
            Write(vline1),
            Write(vline2),
            Write(p2),
            p2.set_color,YELLOW,
            Write(p1),
            p1.set_color,YELLOW,
            ShowCreation(line),
            run_time = 5
        )

        graph1 = self.get_graph(lambda x : x**2, color = WHITE,
                                    x_min = 2, 
                                    x_max = 1
                                    )

        self.remove(p2,line,vline1,vline2)

        self.play(
            MoveAlongPath(p,graph1),rate_func=linear,
            run_time = 5
        )

        line =  self.get_graph(lambda x:  2*x -1,
                                color = WHITE,
                                x_min = 0,
                                x_max = 2
                                )
        self.play(
            ShowCreation(line),
            run_time = 5
        )

        self.remove(p,p1)

        dot1 = Dot([-4.5,-2.5,0])
        dot2 = Dot([-3,-2.5,0])
        line = Line(dot1.get_center(),dot2.get_center()).set_color(ORANGE)
        brace = Brace(line)
        brace_text = brace.get_tex("dx=\\Delta x")
        self.add(line,brace)
        self.play(
            Write(line),
            Write(brace_text.scale(0.5)),
            run_time =5)


        dot3 = Dot([-3,-1.4,0])
        dot4 = Dot([-3,-2.5,0])
        line1 = Line(dot3.get_center(),dot4.get_center()).set_color(ORANGE)
        brace1 = Brace(line1,direction=line1.copy().rotate(PI/2).get_unit_vector())
        brace_text1 = brace1.get_tex("dy")
        self.add(line1,brace1)
        self.play(
            Write(line1),
            Write(brace_text1.scale(0.5)),
            run_time =5)

        dot5 = Dot([-3,-1.0,0])
        line2 = Line(dot5.get_center(),dot3.get_center()).set_color(GREEN)
        brace2 = Brace(line2,direction=line2.copy().rotate(PI/2).get_unit_vector())
        brace_text2 = brace2.get_tex("o(\\Delta x)")
        self.add(line2,brace2)
        self.play(
            Write(line2),
            Write(brace_text2.scale(0.5)),
            run_time =10)


        limtext  = TextMobject("$\\displaystyle   \\lim_{\\Delta x \\rightarrow 0} \\frac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x}  = \\frac{dy}{dx} $").scale(0.55)

        self.play(
            limtext.next_to, funtext, DOWN, buff=0.1,
            run_time =8
        )
        self.wait(2)

        box1 = SurroundingRectangle(limtext, buff=0.1)

        self.play(
            ShowCreation(box1),
            run_time = 3
        )
