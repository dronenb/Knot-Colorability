# An example of how to color a knot
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

class KnotCrossingsExample(KnotScene):
	def construct(self):
		knot = Knot("5_1")
		knot.move_to(LEFT * 3)
		self.play(*DrawKnot(knot))
		self.play(FadeIn(knot.textMobject))
		knot = knot.circleCrossingsAndReturnNew(self)
		self.play(FadeOut(knot), FadeOut(knot.textMobject))