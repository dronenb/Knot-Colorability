import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class EndScene(Scene):
    def construct(self):
        title = TextMobject("Topics to Investigate")
        title.scale(1.5)
        title.to_edge(UP)

        inv1 = TextMobject("Alexander Polynomial")
        inv1.scale(.8)
        inv1.shift(DOWN * .5)
        inv2 = TextMobject("Surfaces and Genus")
        inv2.scale(.8)
        inv2.shift(DOWN * .5)
        inv3 = TextMobject("Braids")
        inv3.scale(.8)
        inv3.shift(DOWN * .5)
        inv4 = TextMobject("Fundamental Group")
        inv4.scale(.8)
        inv4.shift(DOWN * .5)
        # more = TextMobject("...and so much more")
        # more.shift(DOWN * .5)

        self.play(FadeIn(title))

        self.play(FadeIn(inv1))
        self.play(ApplyMethod(inv1.move_to, LEFT * 3 + UP * 1.3))

        self.play(FadeIn(inv2))
        self.play(ApplyMethod(inv2.move_to, RIGHT * 3 + UP * 1.3))

        self.play(FadeIn(inv3))
        self.play(ApplyMethod(inv3.move_to, LEFT * 3 + DOWN * 1.5))

        self.play(FadeIn(inv4))
        self.play(ApplyMethod(inv4.move_to, RIGHT * 3 + DOWN * 1.5))

        # self.play(FadeIn(more))
        # self.play(ApplyMethod(more.move_to, DOWN * 3))

        self.wait()
        # Open the logo file (not checked into Git for copyright reasons...)
        au_logo = SVGMobject(os.path.join(os.path.dirname(os.path.abspath( __file__ )), "..", "svg_files", "au_math_logo2.svg"))
        # Color the logo blue
        au_logo.submobjects[0].set_fill('#0067AA', opacity = 1)
        au_logo.scale(.4)

        au_logo.to_edge(UP)
        au_logo.shift(UP * .2)
        self.play(FadeOut(title))
        # Draw the logo
        self.play(DrawBorderThenFill(au_logo))
        # Hold on this frame for 20 seconds
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.wait()