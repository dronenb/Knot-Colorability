"""
Telling two knots apart by their crossing number
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))

from knot import *

class TrefoilToFigureEight(KnotScene):
    def construct(self):
        # Load knots
        trefoil = Knot("3_1")
        trefoil_text = TextMobject("Trefoil Knot")
        trefoil_text.next_to(trefoil, DOWN)

        fig_8 = Knot("4_1")
        fig_8_text = TextMobject("Figure Eight Knot")
        fig_8_text.next_to(trefoil, DOWN)

        # Draw title
        title = TextMobject("Differentiating Knots")
        title.to_edge(UP)
        self.play(FadeIn(title))

        # Introduce elements
        self.play(*DrawKnot(trefoil))
        self.play(FadeIn(trefoil_text))
        # self.play(FadeOut(trefoil_text))

        self.play(Transform(trefoil, fig_8))
        self.play(Transform(trefoil_text, fig_8_text))
        