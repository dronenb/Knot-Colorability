"""
Video starting sequence
AU Logo first?
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

names = {
    'bd': TextMobject("Ben Dronen"),
    'gp': TextMobject("Gabriel Palacios"),
    'js': TextMobject("Jonathan Swerdlow"),
}

title = TextMobject("Knot Colorability")

class VideoIntro(Scene):
    def construct(self):
        # Keep title center
        title.scale(2)
        # Place names below title
        for name in names:
            names[name].next_to(title, DOWN)
        names['bd'].shift(LEFT * 5)
        names['js'].shift(RIGHT * 5)

        # Add space between names and title
        title.shift(UP * 1)

        self.play(FadeIn(title))
        self.play(FadeIn(names['js']), FadeIn(names['gp']), FadeIn(names['bd']))