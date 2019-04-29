import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class InvariantDef(Scene):

    def construct(self):
        invariant = TextMobject("Knot Invariants")
        # invariant.set_color(BLUE)
        invariant.scale(1.5)
        invariant.to_edge(UP*0.5)

        definition = TextMobject("Unchanging characteristics")
        def2 = TextMobject("Unaffected by Reidemeister moves")

        definition.shift(UP * 1)
        def2.next_to(definition, DOWN)
        def2.shift(DOWN * 1)


        self.play(FadeIn(invariant))
        self.wait()
        self.play(FadeIn(definition))
        self.wait()
        self.play(FadeIn(def2))
        self.wait()


        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
