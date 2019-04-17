"""
Knot Notation definitions
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))

from knot import *

class KnotNotation(KnotScene):
    def construct(self):
        # Create knot object w/ scene title
        basic_knot = Knot("3_1")
        scene_title = TextMobject("Knot Notation")
        scene_title.to_edge(UP)

        # Initialize scene
        self.play(FadeIn(scene_title))
        self.play(*DrawKnot(basic_knot))
        self.play(FadeIn(basic_knot.textMobject))
        self.play(ApplyMethod(basic_knot.shift, LEFT * 5.5), ApplyMethod(basic_knot.textMobject.shift, LEFT * 5.5))

        # "superscript" explanation
        sup_l1 = TextMobject("Crossing Number: ")
        sup_l1.set_color(BLUE)
        sup_l1.shift(UP * 1.5)
        self.play(ApplyMethod(basic_knot.textMobject.set_color_by_tex, str(basic_knot.crossings), BLUE))

        sup_l2 = TextMobject("Minimum number of crossings")
        sup_l2.next_to(sup_l1, DOWN)

        sup_l3 = TextMobject("given any knot diagram")
        sup_l3.next_to(sup_l2, DOWN)

        # Draw Crossing Number text
        self.play(FadeIn(sup_l1))
        self.play(FadeIn(sup_l2), FadeIn(sup_l3))
        self.play(FadeOut(sup_l1), FadeOut(sup_l2), FadeOut(sup_l3))

        # subscript explanation
        sub_l1 = TextMobject("Knot Index:")
        sub_l1.set_color(RED)
        sub_l1.shift(UP * 1.5)
        self.play(ApplyMethod(basic_knot.textMobject.set_color_by_tex, str(basic_knot.index), RED))

        sub_l2 = TextMobject("Arbitrary index assigned to specific")
        sub_l2.next_to(sub_l1, DOWN)
        sub_l3 = TextMobject("knot of same crossing number")
        sub_l3.next_to(sub_l2, DOWN)

        # Draw index definition
        self.play(FadeIn(sub_l1))
        self.play(FadeIn(sub_l2), FadeIn(sub_l3))
        self.play(FadeOut(basic_knot), FadeOut(sub_l1), FadeOut(sub_l2), FadeOut(sub_l3), FadeOut(basic_knot.textMobject))