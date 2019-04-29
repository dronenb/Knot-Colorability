import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class intro3(KnotScene):
    def construct(self):
        title = TextMobject("Important Questions")
        title.scale(1.5)
        title.to_edge(UP)

        q1 = TextMobject("What makes knots different?")
        q1.shift(UP * 1)

        q2 = TextMobject("How can we prove each knot is different?")
        q2.next_to(q1, DOWN)
        q2.shift(DOWN * 1.5)

        self.play(FadeIn(title))
        self.wait()
        self.play(FadeIn(q1))
        self.wait()
        self.play(FadeIn(q2))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()