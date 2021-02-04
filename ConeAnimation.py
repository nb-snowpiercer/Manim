#!/usr/bin/env python

from manimlib.imports import *
import numpy as np


class ConeAnimation(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()

        text1 = TextMobject("$x^2+y^2 = a^2z^2$").scale(1)
        text1.to_corner(UL)
        # text1.shift(RIGHT)
        # text1.rotate(PI/2,axis=RIGHT)

        text2 = TextMobject("$\\frac{x^2}{a^2}+\\frac{y^2}{b^2} = z^2$").scale(1)
        text2.to_corner(UL)
        # text2.shift(RIGHT)
        # text2.rotate(PI/2,axis=RIGHT)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32)).scale(1)

        elliptic_cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                2*u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.4)
        self.add(axes)
        self.play(Write(cone))
        self.wait(13)
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=0*DEGREES,theta=0*DEGREES)
        self.add_fixed_in_frame_mobjects(text1)
        # self.play(Write(text1))
        self.wait(5)
        self.remove_fixed_in_frame_mobjects(text1)
        self.remove(text1)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.play(ReplacementTransform(cone,elliptic_cone))
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(15)
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=0*DEGREES,theta=0*DEGREES)
        # self.play(Write(text2))
        self.add_fixed_in_frame_mobjects(text2)
        # self.play(Write(text1))
        self.wait(5)
        self.remove_fixed_in_frame_mobjects(text2)
        # self.wait(5)