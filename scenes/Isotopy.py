import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *


class Isotopy(Scene):
    def construct(self):

        isotopy = TextMobject("Ambient Isotopy")
        isotopy.scale(1.5)
        isotopy.to_edge(UP * 0.5)

        def_1 = TextMobject("The process of deforming a knot")
        def_2 = TextMobject("without it passing through itself")

        def_2.next_to(def_1, DOWN)

        self.play(FadeIn(isotopy))
        self.wait()

        self.play(FadeIn(def_1), FadeIn(def_2))

        self.wait()

        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()