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
        self.wait()
        self.play(ApplyMethod(unknot.submobjects[0].set_fill, RED))
        self.play(ApplyMethod(unknot.submobjects[0].set_fill, WHITE))

        # Not equal to
        neq = TexMobject(r"\neq")
        neq.scale(2)
        self.play(FadeIn(neq))
        self.wait()

        # Equal to and question mark
        eq = TextMobject("=")
        eq.scale(2)
        question = TextMobject("?")
        question.scale(1.2)
        question.next_to(eq, UP)

        # Switch to trefoil vs fig8
        fig_8.next_to(unknot, DOWN*0)
        self.play(Transform(unknot, fig_8))

        # Switch neq to eq + question mark
        self.play(FadeOut(neq))
        self.play(FadeIn(eq), FadeIn(question))

        self.wait()

        # Try to color
        temp1 = fig_8.showColoringAndReturnNew(self, [RED, '#057aff', YELLOW, RED])
        self.play(FadeOut(temp1), FadeIn(fig_8))
        temp2 = fig_8.showColoringAndReturnNew(self, [YELLOW, '#057aff', RED, '#057aff'])
        self.play(FadeOut(temp2), FadeIn(fig_8))
        temp3 = fig_8.showColoringAndReturnNew(self, [RED, YELLOW, '#057aff', YELLOW])
        self.play(FadeOut(temp3), FadeIn(fig_8))

        # Prevent weird fade outs
        self.remove(temp1)
        self.remove(temp2)
        self.remove(temp3)

        # Show they are not equal
        self.play(FadeOut(question), Transform(eq, neq))

        # End scene
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
