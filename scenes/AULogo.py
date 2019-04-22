#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

# A class that draws the AU logo (making sure to color the flame the proper color, as per my color picker)
class AULogo(KnotScene):
	def construct(self):
		# Open the logo file (not checked into Git for copyright reasons...)
		au_logo = SVGMobject(os.path.join(os.path.dirname(os.path.abspath( __file__ )), "..", "svg_files", "au_math_logo.svg"))

		# Color the logo blue
		au_logo.submobjects[0].set_fill('#0067AA', opacity = 1)

		# Draw the logo
		self.play(DrawBorderThenFill(au_logo))

		# Hold on this frame
		self.wait()
		title = TextMobject("Introduction to Knots \& Invariants")

		title.scale(1.5)

		# self.play(Transform(au_logo, title))
		self.play(FadeOut(au_logo), FadeIn(title))
		self.wait()
		self.play(FadeOut(VGroup(*self.get_mobjects())))
		self.wait()