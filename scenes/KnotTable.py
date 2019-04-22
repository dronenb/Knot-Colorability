#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *

# A scene that shows 10 different knots
class KnotTable(KnotScene):
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
		self.play(*[animation for knot in knots for animation in DrawKnot(knot)])

		# Fade the titles for all of the knots in all at once
		self.play(*[FadeIn(knot.textMobject) for knot in knots])

		# Fade scene out
		self.play(FadeOut(VGroup(*self.get_mobjects())))
		self.wait()