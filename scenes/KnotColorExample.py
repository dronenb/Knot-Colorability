# An example of how to color a knot
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class KnotColorExample(KnotScene):
	def construct(self):
		# Create a new knot
		knot = Knot("3_1")

		# Move the knot (for testing, to make sure the knot can be colored properly when not in the original position)
		knot.move_to(LEFT * 3)

		# Draw the knot in the scene
		self.play(*DrawKnot(knot))

		# Fade the text of the knot into the scene
		self.play(FadeIn(knot.textMobject))

		# Color the knot, and set the knot variable equal to the new one
		knot = knot.showColoringAndReturnNew(self, [RED, '#057aff', YELLOW, '#ff05d5', '#66ff00'])

		# Play the fading out of the new knot
		self.play(FadeOut(knot), FadeOut(knot.textMobject))