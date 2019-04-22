"""
Telling two knots apart by coloring
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class TrefoilFig8Colorability(KnotScene):
    def construct(self):
        # Load knots
        unknot = Knot("Unknot")

        trefoil = Knot("3_1")
        trefoil_text = TextMobject("Trefoil Knot")
        trefoil_text_2 = TextMobject("Crossing Number: 3")
        trefoil_text.next_to(trefoil, DOWN)
        trefoil_text_2.next_to(trefoil_text, DOWN)

        fig_8 = Knot("4_1")
        fig_8_text = TextMobject("Figure Eight Knot")
        fig_8_text_2 = TextMobject("Crossing Number: 4")
        fig_8_text.next_to(trefoil, DOWN)
        fig_8_text_2.next_to(fig_8_text, DOWN)

        # Draw title
        title = TextMobject("Differentiating Knots")
        title.to_edge(UP)
        self.play(FadeIn(title))

        # Draw unknot & trefoil -> compare
        unknot.move_to(LEFT * 2)
        trefoil.move_to(RIGHT * 2)

        self.play(*DrawKnot(unknot), *DrawKnot(trefoil))
        self.wait()

        # Color knots
        _ = trefoil.showColoringAndReturnNew(self, [RED, '#057aff', YELLOW, '#ff05d5', '#66ff00'])

        self.play(ApplyMethod(unknot.submobjects[0].set_fill, RED))
        self.play(ApplyMethod(unknot.submobjects[0].set_fill, WHITE))

        # Not equal to
        neq = TexMobject(r"\neq")
        neq.scale(2)
        self.play(FadeIn(neq))
        self.wait()

        # End scene
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
