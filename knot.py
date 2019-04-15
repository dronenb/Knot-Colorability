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
class SVGKnot(Scene):
	def construct(self):
		trefoil = Knot("5_1")
		self.play(DrawBorderThenFill(trefoil))
		colored_trefoil = Knot("5_1");
		colored_trefoil.submobjects[0].set_fill(RED, opacity = 1)
		self.play(FadeIn(colored_trefoil))
