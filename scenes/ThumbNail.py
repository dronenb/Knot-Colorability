import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class ThumbNail(KnotScene):
	def construct(self):
		title = TexMobject(
			r"""\text{Introduction to }""",
		)
		title2 = TextMobject(
			r"""\text{Knots}""",
			r"""\text{ \& }""",
			r"""\text{Invariants}""",
		)
		title2.set_color_by_tex("Knots",RED)
		title2.set_color_by_tex("Invariants", '#057aff')
		title.scale(2)
		title2.scale(2)
		title2.shift(UP * 1)
		title.shift(UP * 2)
		self.add(title)
		self.add(title2)
		unknot = Knot()
		unknot.scale(1.5)
		trefoil = Knot("3_1")
		trefoil.scale(1.5)
		trefoil.shift(DOWN * 2)
		figure_8 = Knot("4_1")
		figure_8.scale(1.5)
		unknot.shift(LEFT * 4 + DOWN * 2)
		figure_8.shift(RIGHT * 4 + DOWN * 2)
		self.add(unknot)
		self.add(trefoil)
		self.add(figure_8)
		trefoil = trefoil.showColoringAndReturnNew(self, [RED, '#057aff', YELLOW, '#ff05d5', '#66ff00'])