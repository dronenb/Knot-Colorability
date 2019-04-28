

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class Fig8Determinant(KnotScene):
	def construct(self):
		title = TextMobject("Calculating Knot Determinant")
		title.to_edge(UP)
		fig8 = Knot("4_1_with_text")
		fig8.scale(2)
		self.play(FadeIn(title))
		self.play(*DrawKnot(fig8))
		fig8 = fig8.circleCrossingsAndReturnNew(self)
		objectsToFadeIn = []
		# fig8_copy = copy.deepcopy(fig8)
		# self.remove(fig8_copy)
		stuff_to_fade_in = []
		for i in range(8, 12):
			# fig8_copy.submobjects[i].set_stroke(width=3)
			fig8.submobjects[i].set_fill(RED, opacity=100)
			self.remove(fig8.submobjects[i])
			stuff_to_fade_in.append(DrawBorderThenFill(fig8.submobjects[i]))
		for i in range(12, 16):
			# fig8_copy.submobjects[i].set_stroke(width=3)
			fig8.submobjects[i].set_fill(BLUE, opacity=100)
			self.remove(fig8.submobjects[i])
			stuff_to_fade_in.append(DrawBorderThenFill(fig8.submobjects[i]))
		self.play(*stuff_to_fade_in)
		self.wait()
		self.play(ApplyMethod(fig8.shift, LEFT * 4.5))
		# matrix = Matrix([[1, 2, 3], [1, 2, 3]])
		matrix = TextMobject(r"""
			$
				\kbordermatrix{x}
			$
		""")
		self.play(FadeIn(matrix))