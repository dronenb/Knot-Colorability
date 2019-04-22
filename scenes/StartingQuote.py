"""
Jean Toomer quote shown at beginning
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))

from knot import *

class StartingQuote(Scene):
    def construct(self):
        # Quote:
        quote = TextMobject("\"We learn the rope of life by untying its knots.\"")
        author = TexMobject(r"-\textit{Jean Toomer}")

        author.next_to(quote, DOWN)
        author.shift(RIGHT * 4)

        self.play(FadeIn(quote))
        self.play(FadeIn(author))

        self.play(FadeOut(VGroup(*self.get_mobjects())))