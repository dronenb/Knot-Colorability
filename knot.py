#! /usr/bin/env python3
import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim'))
from big_ol_pile_of_manim_imports import *
text_searcher = re.compile('(\d+)_(\d+)')
class Knot(SVGMobject):
	def __init__(self, mode="Unknot", **kwargs):
		try:
			svg_file = os.path.join(os.path.dirname(os.path.abspath( __file__ )), "svg_files", "%s.svg" % mode)
			SVGMobject.__init__(self, file_name=svg_file, **kwargs)
		except:
			warnings.warn("No SVG file for knot: %s" % mode)
			exit()
		text = mode
		result = text_searcher.findall(text)
		if len(result) > 0:
			text = result[0][0] + '$_{' + result[0][1] + '}$'
		self.textMobject = TextMobject(text)
		self.textMobject.move_to(DOWN * 1.45)
	def move_to(self, position):
		super().move_to(position)
		self.textMobject.move_to(position + DOWN * 1.45)
class ColorTrefoil(Scene):
	def construct(self):
		trefoil = Knot("3_1")
		self.play(FadeIn(trefoil))
		self.play(FadeIn(trefoil.textMobject))
class AULogo(Scene):
	def construct(self):
		au_logo = SVGMobject(os.path.join(os.path.dirname(os.path.abspath( __file__ )), "svg_files", "au_math_logo.svg"))
		au_logo.submobjects[0].set_fill('#0067AA', opacity = 1)
		self.play(DrawBorderThenFill(au_logo))
class KnotTable(Scene):
	def construct(self):
		title_text = TextMobject("Some Standard Knots")
		title_text.to_edge(UP)
		self.play(FadeIn(title_text))
		knots = []
		unknot		= Knot()
		unknot.move_to(LEFT * 5 + UP)
		knots.append(unknot)
		k_3_1	= Knot("3_1")
		k_3_1.move_to(LEFT * 2.5 + UP)
		knots.append(k_3_1)
		k_4_1	= Knot("4_1")
		k_4_1.move_to(UP)
		knots.append(k_4_1)
		k_5_1	= Knot("5_1")
		k_5_1.move_to(RIGHT * 2.5 + UP)
		knots.append(k_5_1)
		k_5_2	= Knot("5_2")
		k_5_2.move_to(UP + RIGHT * 5)
		knots.append(k_5_2)
		k_6_1	= Knot("6_1")
		k_6_1.move_to(DOWN * 2 + LEFT * 5)
		knots.append(k_6_1)
		k_6_2	= Knot("6_2")
		k_6_2.move_to(DOWN * 2 + LEFT * 2.5)
		knots.append(k_6_2)
		k_6_3	= Knot("6_3")
		k_6_3.move_to(DOWN * 2)
		knots.append(k_6_3)
		k_7_1	= Knot("7_1")
		k_7_1.move_to(DOWN * 2 + RIGHT * 2.5)
		knots.append(k_7_1)
		k_7_2	= Knot("7_2")
		k_7_2.move_to(DOWN * 2 + RIGHT * 5)
		knots.append(k_7_2)
		self.play(*[DrawBorderThenFill(knot) for knot in knots])
		self.play(*[FadeIn(knot.textMobject) for knot in knots])
		# for knot in knots:
			# self.play(DrawBorderThenFill(knot))
			# self.play(FadeIn(knot.textMobject))