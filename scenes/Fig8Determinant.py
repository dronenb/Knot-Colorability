

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class Matrix(SVGMobject):
	def __init__(self, number="1", **kwargs):
		number = str(number)
		svg_file= str(os.path.abspath(os.path.join(
			os.path.dirname(os.path.abspath( __file__ )),
			'..',
			"svg_files",
			"matrix%s.svg" % (number),
		)))
		try:
			SVGMobject.__init__(self, file_name=svg_file, **kwargs)
		except:
			warnings.warn(sys.exc_info())
			exit()


class Fig8Determinant(KnotScene):
	def construct(self):
		title = TextMobject("Calculating Knot Determinant")
		title.scale(1.5)
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


		# Create the matrix from the SVG file
		matrix = Matrix(1)

		# Scale the matrix up
		matrix.scale(1.5)

		# Shift the matrix to the RIGHT
		matrix.shift(RIGHT * 3)

		# Color the crossing labels
		for i in range(0, 4):
			matrix.submobjects[i].set_fill(BLUE, opacity=100)
		for i in range(4, 8):
			matrix.submobjects[i].set_fill(RED, opacity=100)


		# Fade in the brackets of the Matrix
		self.play(*[FadeIn(matrix.submobjects[i]) for i in range(8, 10)])
		# matrix.submobjects[1].set_color(RED)
		self.play(*[DrawBorderThenFill(matrix.submobjects[i]) for i in range(0, 8)])

		last_index = 9
		for i in range(1, 4 + 1):
			colored_crossing = fig8.submobjects[16 - 1 + i]
			colored_crossing.set_fill('#f4b942', opacity=100)
			self.play(FadeIn(colored_crossing))
			for j in range(1, 4 + 1):
				self.play(FadeIn(matrix.submobjects[last_index + j]))
			last_index = last_index + 4
			self.play(FadeOut(colored_crossing))
		self.wait()
		self.play(FadeIn(matrix.submobjects[26]), FadeIn(matrix.submobjects[27]))

		matrix2 = Matrix(2)

		matrix2.scale(1.5)
		matrix2.submobjects[0].set_fill(BLUE, opacity=100)
		matrix2.submobjects[1].set_fill(RED, opacity=100)
		self.wait()
		matrix2.shift(RIGHT * 3)
		self.play(FadeOut(matrix))
		self.play(*[FadeIn(matrix2.submobjects[i]) for i in range(0, 13)])
		self.wait()
		self.play(FadeOut(matrix2.submobjects[0]), FadeOut(matrix2.submobjects[1]))
		matrix2.submobjects[0].set_fill(WHITE, opacity=0)
		matrix2.submobjects[1].set_fill(WHITE, opacity=0)
		self.play(*[FadeIn(matrix2.submobjects[i]) for i in range(13, len(matrix2.submobjects))])
		self.wait()
		self.play(ApplyMethod(matrix2.shift, LEFT * 1.8))
		self.wait()
		equals5 = TextMobject("= 5")
		equals5.scale(1.5)
		equals5.shift(RIGHT * 5)
		self.play(FadeIn(equals5))
		self.wait()

		self.play(FadeOut(VGroup(*self.get_mobjects())))
		self.wait()
