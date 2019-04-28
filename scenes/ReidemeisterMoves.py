# An example of how to color a knot
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

moves = {
	'1'	:	{
		'before'	:	'reidemeister_1_before.svg',
		'after'		:	'reidemeister_1_after.svg',
	},
	'2'	:	{
		'before'	:	'reidemeister_2_before.svg',
		'after'		:	'reidemeister_2_after.svg',
	},
	'3'	:	{},
}
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


class ReidemeisterMoves(KnotScene):
	def construct(self):
		title = TextMobject("Reidemeister Moves")
		title.to_edge(UP)
		title.scale(1.5)
		self.play(FadeIn(title))
		move_1_text = TextMobject('Move 1: ``Twist"')
		move_1_text.shift(LEFT * 4.2 + UP * 1.5)
		self.play(FadeIn(move_1_text))
		move_1_before	= ReidemeisterSVG()
		move_1_before.shift(LEFT * 5.3 + DOWN)
		move_1_before_copy = ReidemeisterSVG()
		move_1_before_copy.shift(LEFT * 5.3 + DOWN)
		self.play(FadeIn(move_1_before))
		self.add(move_1_before_copy)
		self.play(ApplyMethod(move_1_before_copy.shift, RIGHT * 2))
		move_1_after		= ReidemeisterSVG(number="1", mode="after")
		move_1_after.shift(LEFT * 5.3 + RIGHT * 2 + DOWN)
		self.play(Transform(move_1_before_copy, move_1_after))

		move_2_text = TextMobject('Move 2: ``Poke"')
		move_2_text.shift(UP * 1.5)
		self.play(FadeIn(move_2_text))
		move_2_before = ReidemeisterSVG(number="2")
		move_2_before.shift(DOWN + LEFT)
		self.play(FadeIn(move_2_before))
		move_2_before_copy = ReidemeisterSVG(number="2")
		move_2_before_copy.shift(DOWN + LEFT)
		self.add(move_2_before_copy)
		self.play(ApplyMethod(move_2_before_copy.shift, RIGHT * 2))
		move_2_after = ReidemeisterSVG(number="2", mode="after")
		move_2_after.shift(DOWN + RIGHT)
		self.play(Transform(move_2_before_copy, move_2_after))

		move_3_text = TextMobject('Move 3: ``Slide"')
		move_3_text.shift(RIGHT * 4.2 + UP * 1.5)
		self.play(FadeIn(move_3_text))
		move_3_before = ReidemeisterSVG(number="3")
		move_3_before.shift(RIGHT * 5.3 + LEFT * 2 + DOWN)
		self.play(FadeIn(move_3_before))
		move_3_before_copy = ReidemeisterSVG(number="3")
		move_3_before_copy.shift(RIGHT * 5.3 + LEFT * 2 + DOWN)
		self.add(move_3_before_copy)
		self.play(ApplyMethod(move_3_before_copy.shift, RIGHT * 2))
		move_3_after = ReidemeisterSVG(number="3", mode="after")
		move_3_after.shift(RIGHT * 5.3 + LEFT * 2 + DOWN + RIGHT * 2)
		self.play(Transform(move_3_before_copy, move_3_after))

		self.wait()

		# Fade scene out
		self.play(FadeOut(VGroup(*self.get_mobjects())))
		self.wait()