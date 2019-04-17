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
			self.crossings = int(result[0][0])
		else:
			self.crossings = 0
		# Create a new TextMobject for this object
		self.textMobject = TextMobject(text)

		# Make the circles around the crossings invisible
		for i in range(0, self.crossings):
			self.submobjects[self.crossings + i].set_stroke(width=0)
			self.submobjects[self.crossings + i].set_fill(opacity=0)

		# Move this object to right below the knot object
		self.textMobject.move_to(DOWN * 1.45)
	# Move the knot, whilst also moving the text mobject
	def move_to(self, position):
		super().move_to(position)
		self.textMobject.move_to(position + DOWN * 1.45)
	# Circle each crossing
	def circleCrossingsAndReturnNew(self, scene):
		if self.crossings == 0:
			return self
		else:
			previous_knot = self
			for i in range(self.crossings, self.crossings * 2):
				new_knot = copy.deepcopy(previous_knot)
				new_knot.submobjects[i].set_stroke(width=3)
				# new_knot.submobjects[i].set_fill(opacity=50)
				scene.play(FadeIn(new_knot))
				scene.remove(previous_knot)
				previous_knot = new_knot
			previous_knot.textMobject = self.textMobject
			return previous_knot

	# Color the knot
	def showColoringAndReturnNew(self, scene, colors):
		# Make sure we have enough colors for the components of this knot
		if len(self.submobjects) <= len(colors):
			print("Not enough colors!")
			exit()
		# If so, continue
		else:
			# Create a new variable that is accessible outside of the loop
			previous_knot = self

			# Color the components of the knot by copying the original knot, coloring a component, then repeating until all the components are colored
			for i in range(0, self.crossings):
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
def DrawKnot(knot):
	animations = []
	if knot.crossings == 0:
		animations.append(DrawBorderThenFill(knot.submobjects[0]))
	else:
		for i in range(0, knot.crossings):
			animations.append(DrawBorderThenFill(knot.submobjects[i]))
	return animations
class KnotScene(Scene):
	def remove(self, to_remove):
		if isinstance(to_remove, Knot):
			for i in range(0, len(to_remove.submobjects)):
				super().remove(to_remove.submobjects[i])
		else:
			super().remove(to_remove)

class KnotCrossingsExample(KnotScene):
	def construct(self):
		knot = Knot("5_1")
		knot.move_to(LEFT * 3)
		self.play(*DrawKnot(knot))
		self.play(FadeIn(knot.textMobject))
		knot = knot.circleCrossingsAndReturnNew(self)
		self.play(FadeOut(knot), FadeOut(knot.textMobject))