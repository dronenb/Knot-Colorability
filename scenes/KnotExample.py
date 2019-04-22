"""
Unknot to Trefoil
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class KnotExample(KnotScene):
    def construct(self):
        # Load knots
        unknot = Circle(color=WHITE, radius=2, stroke=10) # Does sroke do anything?
        unknot_text = TextMobject("Unknot")
        unknot_text.next_to(unknot, DOWN)

        """
        trefoil = Knot("3_1")
        trefoil_text = TexMobject(r"\text{Knot } 3_1")
        trefoil_text.next_to(trefoil, DOWN)
        """

        # Draw unknot
        self.play(DrawBorderThenFill(unknot))
        self.play(FadeIn(unknot_text))
        """
        self.play(Transform(unknot, trefoil), Transform(unknot_text, trefoil_text))
        """

        # Finish scene
        self.play(FadeOut(VGroup(*self.get_mobjects())))

        self.wait()