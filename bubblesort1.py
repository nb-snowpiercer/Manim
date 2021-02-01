#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flag -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class BubbleSort1(Scene):
	def construct(self):
		text1 = TextMobject("-1");
		text2 = TextMobject("3");
		text3 = TextMobject("-2");
		text4 = TextMobject("9");
		text5 = TextMobject("16");
		text1.shift(2*LEFT)
		text2.shift(1*LEFT)
		text3.shift(0*LEFT)
		text4.shift(1*RIGHT)
		text5.shift(2*RIGHT)
		self.wait(2)
		self.play(Write(text1))
		self.play(Write(text2))
		self.play(Write(text3))
		self.play(Write(text4))
		self.play(Write(text5))
		self.wait(2);
		#1 loop
		text4.set_color(RED);
		text5.set_color(BLUE),
		self.play(
			text4.shift, RIGHT*1,
			text5.shift, LEFT*1,
			run_time=2
			)
		text4.set_color(WHITE);
		self.wait(2);
		text3.set_color(RED);
		text5.set_color(BLUE),
		self.play(
		text3.shift, RIGHT*1,
		text5.shift, LEFT*1,
		run_time=2
		)
		text3.set_color(WHITE);
		self.wait(2);
		text2.set_color(RED);
		text5.set_color(BLUE),
		self.play(
		text2.shift, RIGHT*1,
		text5.shift, LEFT*1,
		run_time=2
		)
		text2.set_color(WHITE);
		self.wait(2);
		text1.set_color(RED);
		text5.set_color(BLUE),
		self.play(
		text1.shift, RIGHT*1,
		text5.shift, LEFT*1,
		run_time=2
		)
		text1.set_color(WHITE);
		self.wait(2);
		#2 loop
		text3.set_color(RED);
		text4.set_color(BLUE),
		self.play(
			text3.shift, RIGHT*1,
			text4.shift, LEFT*1,
			run_time=2
			)
		text3.set_color(WHITE);
		self.wait(2);
		text2.set_color(RED);
		text4.set_color(BLUE),
		self.play(
		text2.shift, RIGHT*1,
		text4.shift, LEFT*1,
		run_time=2
		)
		text2.set_color(WHITE);
		self.wait(2);
		text1.set_color(RED);
		text4.set_color(BLUE),
		self.play(
		text1.shift, RIGHT*1,
		text4.shift, LEFT*1,
		run_time=2
		)
		text1.set_color(WHITE);
		self.wait(2);
		#3 loop
		text2.set_color(RED);
		text3.set_color(BLUE),
		self.wait(2);
		text3.set_color(WHITE);
		self.wait(2);
		text1.set_color(RED);
		text2.set_color(BLUE),
		self.play(
		text1.shift, RIGHT*1,
		text2.shift, LEFT*1,
		run_time=2
		)
		text1.set_color(WHITE);
		self.wait(2);
		#4 loop
		text1.set_color(RED);
		text3.set_color(BLUE),
		self.wait(2)
		text1.set_color(BLUE);
		self.wait(2);
