"""
Telling two knots apart by their crossing number

TODO:
-Draw the crossing circles on each one to show the change?
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

        # Introduce elements
        self.play(*DrawKnot(trefoil))
        self.play(FadeIn(trefoil_text))

        # Draw crossing circles
        trefoil = trefoil.circleCrossingsAndReturnNew(self)
        self.play(FadeIn(trefoil_text_2))

        # Transform trefoil into fig8
        self.play(Transform(trefoil, fig_8))
        self.play(Transform(trefoil_text, fig_8_text))
        fig_8 = fig_8.circleCrossingsAndReturnNew(self)
        self.play(Transform(trefoil_text_2, fig_8_text_2))
        