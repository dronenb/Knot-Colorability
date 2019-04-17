# An example of how to color a knot
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class KnotBasics(KnotScene):
	"""
	Introduce the basic ideas of knots:
		What the numbering means
		...
	"""
	def construct(self):
		# The knot to introduce
		knot = Knot("3_1")
		# Begin with knot notation
		title = TextMobject("Knot Notation")
		title.to_edge(UP)

		# Draw knot & title
		self.play(FadeIn(title))
		self.play(*DrawKnot(knot))
		self.play(FadeIn(knot.textMobject))

		"""
		TODO:
		Clear all except "3_1" text
			Move to top of screen
		Fade in text (briefly) explaining notation
		Move on to KnotTable
		"""