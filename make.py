#! /usr/bin/env python3
import os
import sys
scenes = [
	'KnotColorExample',
]

manim_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim', 'manim.py')

for scene in scenes:
	command = "python3 %s %s %s" % (manim_path, "knot.py", scene)
	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv)):
			command = command + " " + sys.argv[i]
	os.system(command)
