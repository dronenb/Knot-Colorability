#! /usr/bin/env python3

# Import some modules
import os
import sys

# List of scenes
scenes = [
	# 'AULogo',
	# 'AULogoIntro',
	# 'CulpritKnot',
	'EndScene',
	'Fig8Determinant',
	# 'Isotopy',
	# 'KnotColorExample',
	# 'KnotCrossingsExample',
	# 'KnotExample',
	# 'KnotNotation',
	# 'KnotTable',
	# 'LordKelvin',
	# 'ReidemeisterColor',
	'ReidemeisterMoves',
	# 'StartingQuote',
	'TrefoilFig8Colorability',
	# 'TextTest',
	'TrefoilToFigureEight',
	# 'Tricolorability',
	# 'VideoIntro',
]

# Find the current path, then combine that with the manim folder and the manim.py executable
manim_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim', 'manim.py')

# Render each of the scenes
for scene in scenes:
	scene_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'scenes', scene + '.py')
	# Create the command
	command = "python3 %s %s %s" % (manim_path, scene_path, scene)

	# Check if any arguments were provided on the command line
	if len(sys.argv) > 1:
		# Add each of the arguments to the command
		for i in range(1, len(sys.argv)):
			command = command + " " + sys.argv[i]
	# Run the command
	os.system(command)
