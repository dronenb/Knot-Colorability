#! /usr/bin/env python3
import os
import sys
scenes = [
	'SVGKnot',
]

manim_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim', 'manim.py')

for scene in scenes:
	os.system("python3 %s %s %s" % (manim_path, "knot.py", scene))
