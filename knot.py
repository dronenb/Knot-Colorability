#! /usr/bin/env python3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim'))
from big_ol_pile_of_manim_imports import *
class Knot(SVGMobject):
	def __init__(self, mode="Unknot", **kwargs):
		try:
			svg_file = os.path.join(os.path.dirname(os.path.abspath( __file__ )), "svg_files", "%s.svg" % mode)
			SVGMobject.__init__(self, file_name=svg_file, **kwargs)
		except:
			warnings.warn("No SVG file for knot: %s" % mode)
			exit()
class KnotTable(Scene):
	def construct(self):
		title_text = TextMobject("Some Standard Knots")
		title_text.to_edge(UP)
		self.play(FadeIn(title_text))
#		unknot		= Knot()
		knot_3_1	= Knot("3_1")
		knot_3_1.move_to(LEFT * 5 + UP)
		knot_4_1	= Knot("4_1")
		knot_4_1.move_to(LEFT * 2.5 + UP)
		knot_5_1	= Knot("5_1")
		knot_5_1.move_to(UP)
		knot_5_2	= Knot("5_2")
		knot_5_2.move_to(RIGHT * 2.5 + UP)
		knot_6_1	= Knot("6_1")
		knot_6_1.move_to(UP + RIGHT * 5)
		knot_6_2	= Knot("6_2")
		knot_6_2.move_to(DOWN * 2 + LEFT * 5)
		knot_6_3	= Knot("6_3")
		knot_6_3.move_to(DOWN * 2 + LEFT * 2.5)
		knot_7_1	= Knot("7_1")
		knot_7_1.move_to(DOWN * 2)
		knot_7_2	= Knot("7_2")
		knot_7_2.move_to(DOWN * 2 + RIGHT * 2.5)
		self.play(
			FadeIn(knot_3_1),
			FadeIn(knot_4_1),
			FadeIn(knot_5_1),
			FadeIn(knot_5_2),
			FadeIn(knot_6_1),
			FadeIn(knot_6_2),
			FadeIn(knot_6_3),
			FadeIn(knot_7_1),
			FadeIn(knot_7_2),
		)
