"""
Lord Kelvin scene

Will add image in post
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class LordKelvin(Scene):
    def construct(self):
        name = TextMobject("William \"Lord Kelvin\" Thomson")
        name.shift(DOWN * 2.5)

        years = TexMobject(r"\textit{1824-1907}")
        years.scale(0.5)
        years.next_to(name, DOWN)
        # years.shift(RIGHT * 2)

        self.play(FadeIn(name))
        self.play(FadeIn(years))

        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
