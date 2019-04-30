"""
Telling two knots apart by coloring
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class TrefoilFig8Colorability(KnotScene):
    def construct(self):
        invariant = TextMobject("Tricolorability")
        invariant.to_edge(UP)
        invariant.scale(1.5)

        defn = TextMobject("A knot's ability to be colored")
        defn2 = TextMobject("with three different colors")
        defn2.next_to(defn, DOWN)
        dgroup = VGroup(defn, defn2)

        rule_1 = TextMobject("1. At least two colors must be used")
        rule_2 = TextMobject("2. Incident crossing strands are either:")
        cont_1 = TextMobject("All the same color")
        cont_2 = TextMobject("All different colors")

        rule_1.shift(UP * 1)
        rule_2.next_to(rule_1, DOWN)
        rule_2.shift(DOWN * 1)
        cont_1.next_to(rule_2, DOWN)
        cont_2.next_to(cont_1, DOWN)

        temp = VGroup(rule_1, rule_2, cont_1, cont_2)
        temp.scale(0.75)
        temp.shift(DOWN * 1)

        # Title
        self.play(FadeIn(invariant))
        self.wait()

        # Definition
        self.play(FadeIn(dgroup))
        self.wait()
        self.play(ApplyMethod(dgroup.shift, UP * 1.75))

        self.play(FadeIn(rule_1))
        self.wait()
        self.play(FadeIn(rule_2))
        self.wait()
        self.play(FadeIn(cont_1))
        self.wait()
        self.play(FadeIn(cont_2))

        # Undo the temporary changes ---- moved this to later
        # temp.shift(UP * 1)
        # temp.scale(1.30)

        self.wait()

        # Draw title
        title = TextMobject("Distinguishing Knots")
        title.to_edge(UP)
        title.scale(1.5)
        self.play(Transform(invariant, title))
        self.play(
            FadeOut(dgroup),
            ApplyMethod(rule_1.scale, .85),
            ApplyMethod(rule_2.scale, .85),
            ApplyMethod(cont_1.scale, .85),
            ApplyMethod(cont_2.scale, .85),
        )
        self.play(
            ApplyMethod(rule_1.shift, DOWN * (3 - 1.3)),
            ApplyMethod(rule_2.shift, DOWN * (2 - 1)),
            ApplyMethod(cont_1.shift, DOWN * (1.7 - 0.8)),
            ApplyMethod(cont_2.shift, DOWN * (1.5 - 0.7)),
        )
        # self.wait()
        # return
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

        self.wait()

        # End scene
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
