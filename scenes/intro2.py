import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class intro2(KnotScene):
    def construct(self):
        title = TextMobject("Mathematical Knots")
        title.scale(1.5)
        title.to_edge(UP)

        why1 = TextMobject("What is so interesting?")
        why1.shift(UP * 1)

        why2 = TextMobject("Why do they matter?")
        why2.next_to(why1, DOWN)
        why2.shift(DOWN * 1.5)

        self.play(FadeIn(title))
        self.wait()
        self.play(FadeIn(why1))
        self.wait()
        self.play(FadeIn(why2))

        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()