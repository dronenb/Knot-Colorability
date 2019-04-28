

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class ReidemeisterSVG(SVGMobject):
	def __init__(self, number="1",mode="before", **kwargs):
		svg_file= str(os.path.abspath(os.path.join(
			os.path.dirname(os.path.abspath( __file__ )),
			'..',
			"svg_files",
			"reidemeister_%s_%s.svg" % (number, mode),
		)))
		try:
			SVGMobject.__init__(self, file_name=svg_file, **kwargs)
		except:
			warnings.warn(sys.exc_info())
			exit()

class ReidemeisterColor(KnotScene):
	def construct (self):
		title = TextMobject("Reidemeister Moves")
		title.scale(1.5)
		title.to_edge(UP)
		title.scale(1.5)
		self.play(FadeIn(title))

		# Define the first reidemeister move objects
		move_1_text = TextMobject('Move 1: ``Twist"')
		move_1_text.shift(LEFT * 4.2 + UP * 1.5)
		move_1_before	= ReidemeisterSVG()
		move_1_before.shift(LEFT * 5.3 + DOWN)
		move_1_after		= ReidemeisterSVG(number="1", mode="after")
		move_1_after.shift(LEFT * 5.3 + RIGHT * 2 + DOWN)

		move_2_text = TextMobject('Move 2: ``Poke"')
		move_2_text.shift(UP * 1.5)
		move_2_before = ReidemeisterSVG(number="2")
		move_2_before.shift(DOWN + LEFT)
		move_2_after = ReidemeisterSVG(number="2", mode="after")
		move_2_after.shift(DOWN + RIGHT)

		move_3_text = TextMobject('Move 3: ``Slide"')
		move_3_text.shift(RIGHT * 4.2 + UP * 1.5)
		move_3_before = ReidemeisterSVG(number="3")
		move_3_before.shift(RIGHT * 5.3 + LEFT * 2 + DOWN)
		move_3_after = ReidemeisterSVG(number="3", mode="after")
		move_3_after.shift(RIGHT * 5.3 + LEFT * 2 + DOWN + RIGHT * 2)

		self.play(
			FadeIn(move_1_text),
			FadeIn(move_1_before),
			FadeIn(move_1_after),
			FadeIn(move_2_text),
			FadeIn(move_2_before),
			FadeIn(move_2_after),
			FadeIn(move_3_text),
			FadeIn(move_3_before),
			FadeIn(move_3_after),
		)
		self.wait()

		# move_1_before.submobjects[0].set_fill(RED, opacity=1)
		self.play(ApplyMethod(move_1_before.submobjects[0].set_fill, RED))
		self.wait()
		self.play(
			ApplyMethod(move_1_after.submobjects[0].set_fill, RED), ApplyMethod(move_1_after.submobjects[1].set_fill, RED),
		)
		self.wait()
		self.play(
			ApplyMethod(move_2_before.submobjects[0].set_fill, BLUE),
			ApplyMethod(move_2_before.submobjects[1].set_fill, BLUE),
		)
		self.wait()
		self.play(
			ApplyMethod(move_2_after.submobjects[0].set_fill, BLUE),
			ApplyMethod(move_2_after.submobjects[1].set_fill, BLUE),
			ApplyMethod(move_2_after.submobjects[2].set_fill, BLUE),
			ApplyMethod(move_2_after.submobjects[3].set_fill, BLUE),
		)
		self.wait()
		self.play(
			ApplyMethod(move_2_before.submobjects[0].set_fill, WHITE),
			ApplyMethod(move_2_before.submobjects[1].set_fill, WHITE),
			ApplyMethod(move_2_after.submobjects[0].set_fill, WHITE),
			ApplyMethod(move_2_after.submobjects[1].set_fill, WHITE),
			ApplyMethod(move_2_after.submobjects[2].set_fill, WHITE),
			ApplyMethod(move_2_after.submobjects[3].set_fill, WHITE),
		)
		self.wait()
		self.play(
			ApplyMethod(move_2_before.submobjects[0].set_fill, BLUE),
			ApplyMethod(move_2_before.submobjects[1].set_fill, GREEN),
		)
		self.wait()
		self.play(
			ApplyMethod(move_2_after.submobjects[0].set_fill, BLUE),
			ApplyMethod(move_2_after.submobjects[2].set_fill, GREEN),
			ApplyMethod(move_2_after.submobjects[3].set_fill, GREEN),
			ApplyMethod(move_2_after.submobjects[1].set_fill, RED),
		)
		self.wait()

		# Fade scene out
		self.play(FadeOut(VGroup(*self.get_mobjects())))
		self.wait()