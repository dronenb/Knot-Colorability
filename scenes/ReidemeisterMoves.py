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
		svg_file= os.path.abspath(os.path.join(
			os.path.dirname(os.path.abspath( __file__ )),
			'..',
			"svg_files",
			"reidemeister_%s_%s.svg" % (number, mode),
		))
		try:
			super().__init__(self, file_name=svg_file, **kwargs)
		except:
			warnings.warn("No SVG file for move: %s" % svg_file)
			exit()


class ReidemeisterMoves(KnotScene):
	def construct(self):
		move1 = ReidemeisterSVG()
		self.play(DrawBorderThenFill(move1))