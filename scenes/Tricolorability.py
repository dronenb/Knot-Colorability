import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class Tricolorability(Scene):

    def construct(self):
        invariant = TextMobject("Tricolorability Invariant")
        invariant.set_color(BLUE)
        invariant.scale(1.5)
        invariant.to_edge(UP*0.5)

        rule_1 = TextMobject("1. At least two colors")
        rule_2 = TextMobject("2. Incident crossing strands are either:")
        cont_1 = TextMobject("\tAll the same color")
        cont_2 = TextMobject("\tAll different colors")

        rule_1.shift(UP * 1)
        rule_2.next_to(rule_1, DOWN)
        rule_2.shift(DOWN * 1)
        cont_1.next_to(rule_2, DOWN)
        cont_2.next_to(cont_1, DOWN)

        self.play(FadeIn(invariant))
        self.wait()
        self.play(FadeIn(rule_1))
        self.wait()
        self.play(FadeIn(rule_2))
        self.wait()
        self.play(FadeIn(cont_1))
        self.wait()
        self.play(FadeIn(cont_2))


        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
