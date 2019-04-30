import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class Tricolorability(KnotScene):

    def construct(self):
        invariant = TextMobject("Tricolorability")
        # invariant.set_color(BLUE)
        invariant.scale(1.5)
        invariant.to_edge(UP*0.5)

        defn = TextMobject("A knot's ability to be colored")
        defn2 = TextMobject("with three different colors")
        defn2.next_to(defn, DOWN)
        dgroup = VGroup(defn, defn2)

        rule_1 = TextMobject("1. Using at least two colors")
        rule_2 = TextMobject("2. Where incident crossing strands are either:")
        cont_1 = TextMobject("All the same color")
        cont_2 = TextMobject("All different colors")

        VGroup(rule_1, rule_2, cont_1, cont_2).scale(0.75)

        rule_1.shift(DOWN * 0)
        rule_2.next_to(rule_1, DOWN)
        rule_2.shift(DOWN * 0.5)
        cont_1.next_to(rule_2, DOWN)
        cont_2.next_to(cont_1, DOWN)

        # Fade in title
        self.play(FadeIn(invariant))
        self.wait()

        # Definition
        self.play(FadeIn(dgroup))
        self.wait()
        # self.play(FadeOut(dgroup))
        self.play(ApplyMethod(dgroup.shift, UP * 1.75))

        # Rules
        self.play(FadeIn(rule_1))
        self.wait()
        self.play(FadeIn(rule_2))
        self.wait()
        self.play(FadeIn(cont_1))
        self.wait()
        self.play(FadeIn(cont_2))

        self.wait()

        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
