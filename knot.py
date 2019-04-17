#! /usr/bin/env python3

# Import some modules
import os
import sys
import re

# Add the manim directory to Python's path so that all the manim modules will be loaded properly
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'manim'))

# Import all the necessary modules
from big_ol_pile_of_manim_imports import *

# Regular expression to match underscores with integers on either side
text_searcher = re.compile('(\d+)_(\d+)')

# A class that defines a knot
class Knot(SVGMobject):
	def __init__(self, mode="Unknot", **kwargs):
		# Try opening the SVG files in the svg_files directory
		try:
			svg_file = os.path.join(os.path.dirname(os.path.abspath( __file__ )), "svg_files", "%s.svg" % mode)
			SVGMobject.__init__(self, file_name=svg_file, **kwargs)
		# Warn and exit if the file doesn't exist
		except:
			warnings.warn("No SVG file for knot: %s" % mode)
			exit()
		# Set the mode in the object
		self.mode = mode

		# Copy the mode to a new variable
		text = mode

		# Search the new variable using the previously defined regex
		result = text_searcher.findall(text)

		# Check if the regex found any matches
		if len(result) > 0:
			# Replace the text variable with the first number, then the second number in subscript (via LaTex)
			text = result[0][0] + '$_{' + result[0][1] + '}$'
		# Create a new TextMobject for this object
		self.textMobject = TextMobject(text)

		# Move this object to right below the knot object
		self.textMobject.move_to(DOWN * 1.45)
	# Move the knot, whilst also moving the text mobject
	def move_to(self, position):
		super().move_to(position)
		self.textMobject.move_to(position + DOWN * 1.45)
	# Color the knot
	def showColoringAndReturnNew(self, scene, colors):
		# Make sure we have enough colors for the components of this knot
		if len(self.submobjects) != len(colors):
			print("Not enough colors!")
			exit()
		# If so, continue
		else:
			# Create a new variable that is accessible outside of the loop
			previous_knot = self

			# Color the components of the knot by copying the original knot, coloring a component, then repeating until all the components are colored
			for i in range(0, len(colors)):
				# Create a copy of the original knot
				new_knot = copy.deepcopy(previous_knot)

				# Color one of the components of the new knot
				new_knot.submobjects[i].set_fill(colors[i], opacity=1)

				# Fade in the new knot over the original knot
				scene.play(FadeIn(new_knot))

				# Remove the original knot (not noticeable, since the new knot is on top of the old knot)
				scene.remove(previous_knot)

				# Put this new knot in the previous knot variable
				previous_knot = new_knot
			# Since this is the last knot from the loop, this is the knot we want to return
			# Set the textMobject of this new knot to be that of the original
			previous_knot.textMobject = self.textMobject

			# Return the new knot
			return previous_knot

# An example of how to color a knot
class KnotColorExample(Scene):
	def construct(self):
		# Create a new knot
		knot = Knot("5_1")

		# Move the knot (for testing, to make sure the knot can be colored properly when not in the original position)
		knot.move_to(LEFT * 3)

		# Draw the knot in the scene
		self.play(DrawBorderThenFill(knot))

		# Fade the text of the knot into the scene
		self.play(FadeIn(knot.textMobject))

		# Color the knot, and set the knot variable equal to the new one
		knot = knot.showColoringAndReturnNew(self, [RED, '#057aff', YELLOW, '#ff05d5', '#66ff00'])

		# Play the fading out of the new knot
		self.play(FadeOut(knot), FadeOut(knot.textMobject))

# A class that draws the AU logo (making sure to color the flame the proper color, as per my color picker)
class AULogo(Scene):
	def construct(self):
		# Open the logo file (not checked into Git for copyright reasons...)
		au_logo = SVGMobject(os.path.join(os.path.dirname(os.path.abspath( __file__ )), "svg_files", "au_math_logo.svg"))

		# Color the logo blue
		au_logo.submobjects[0].set_fill('#0067AA', opacity = 1)

		# Draw the logo
		self.play(DrawBorderThenFill(au_logo))

		# Hold on this frame
		self.wait()

# A scene that shows 10 different knots
class KnotTable(Scene):
	def construct(self):
		# Create a title text
		title_text = TextMobject("Some Standard Knots")

		# Align the text to the top
		title_text.to_edge(UP)

		# Fade the title text in
		self.play(FadeIn(title_text))

		# Create an array to store the knots
		knots = []

		# Create an unknot (the default)
		unknot	= Knot()

		# Move the knot up and left
		unknot.move_to(LEFT * 5 + UP)

		# Add this knot to the array
		knots.append(unknot)

		# Create knot 3_1
		k_3_1	= Knot("3_1")

		# Move it up and left
		k_3_1.move_to(LEFT * 2.5 + UP)

		# Add this knot to the array
		knots.append(k_3_1)

		# Create knot 4_1
		k_4_1	= Knot("4_1")

		# Shift the knot up
		k_4_1.move_to(UP)

		# Add the knot to the array
		knots.append(k_4_1)

		# Create knot 5_1
		k_5_1	= Knot("5_1")

		# Move it up and right
		k_5_1.move_to(RIGHT * 2.5 + UP)

		# Add the knot to the array
		knots.append(k_5_1)

		# Create knot 5_2
		k_5_2	= Knot("5_2")

		# Move it up and right
		k_5_2.move_to(UP + RIGHT * 5)

		# Add the knot to the array
		knots.append(k_5_2)

		# Create knot 6_1
		k_6_1	= Knot("6_1")

		# Move it down and left
		k_6_1.move_to(DOWN * 2 + LEFT * 5)

		# Add the knot to the array
		knots.append(k_6_1)

		# Create knot 6_2
		k_6_2	= Knot("6_2")

		# Move it down and left
		k_6_2.move_to(DOWN * 2 + LEFT * 2.5)

		# Add the knot to the array
		knots.append(k_6_2)

		# Create knot 6_3
		k_6_3	= Knot("6_3")

		# Move it down
		k_6_3.move_to(DOWN * 2)

		# Add the knot to the array
		knots.append(k_6_3)

		# Create knot 7_1
		k_7_1	= Knot("7_1")

		# Move it down and right
		k_7_1.move_to(DOWN * 2 + RIGHT * 2.5)

		# Add the knot to the array
		knots.append(k_7_1)

		# Create knot 7_2
		k_7_2	= Knot("7_2")

		# Move it down and right
		k_7_2.move_to(DOWN * 2 + RIGHT * 5)

		# Add the knot to the array
		knots.append(k_7_2)

		# Draw the borders for all of the knots all at once
		self.play(*[DrawBorderThenFill(knot) for knot in knots])

		# Fade the titles for all of the knots in all at once
		self.play(*[FadeIn(knot.textMobject) for knot in knots])
		# for knot in knots:
			# self.play(DrawBorderThenFill(knot))
			# self.play(FadeIn(knot.textMobject))