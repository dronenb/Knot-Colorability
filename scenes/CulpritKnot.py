#! /usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..'))
from knot import *


class CulpritKnot(KnotScene):
    def construct(self):
        title = TextMobject("The Culprit Knot")
        title.scale(1.5)
        title.to_edge(UP)

        self.play(FadeIn(title))
        culprits = []
        culprits.append(Culprit(1))
        self.play(DrawBorderThenFill(culprits[0]))
        self.wait()
        self.play(ApplyMethod(culprits[0].move_to, UP + LEFT * 5))
        self.wait()
        for i in range(1, 5):
            culprits.append(copy.deepcopy(culprits[i-1]))
            self.add(culprits[i])
            self.play(ApplyMethod(culprits[i].shift, RIGHT * 2.5))
            new_culprit = Culprit(i + 1)
            new_culprit.move_to(UP + LEFT * 5 + RIGHT * i * 2.5)
            self.play(Transform(culprits[i], new_culprit))
            # self.remove(culprits[i])
            #culprits[i] = new_culprit
            # self.wait()
        culprits.append(copy.deepcopy(culprits[4]))
        self.play(ApplyMethod(culprits[5].move_to, DOWN * 2 + LEFT * 5))
        culprit6 = Culprit(6)
        culprit6.move_to(DOWN * 2 + LEFT * 5)
        self.play(Transform(culprits[5], culprit6))
        # culprits[5] = culprit6
        # self.wait()
        for i in range(6, 10):
            culprits.append(copy.deepcopy(culprits[i-1]))
            self.add(culprits[i])
            self.play(ApplyMethod(culprits[i].shift, RIGHT * 2.5))
            new_culprit = None
            if i == 9:
                new_culprit = Knot()
            else:
                new_culprit = Culprit(i + 1)
            new_culprit.move_to(DOWN * 2 + LEFT * 5 + RIGHT * (i-5) * 2.5)
            self.play(Transform(culprits[i], new_culprit))
            # self.remove(culprits[i])
            #culprits[i] = new_culprit
            # self.wait()


        # Fade out all culprits except first and last
        self.play(FadeOut(culprits[1]), FadeOut(culprits[2]), FadeOut(culprits[3]),
        FadeOut(culprits[4]), FadeOut(culprits[5]), FadeOut(culprits[6]),
        FadeOut(culprits[7]), FadeOut(culprits[8]))
        # print(len(culprits)) #  = 10
        self.wait()

        # Move to same row
        self.play(ApplyMethod(culprits[0].shift, DOWN * 1 + RIGHT * 2.5))
        self.play(ApplyMethod(culprits[9].shift, UP * 2 + LEFT * 2.5))

        eq = TextMobject("=")
        eq.scale(2)

        # Draw equal sign
        self.play(FadeIn(eq))


        self.wait()

        # End scene
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()



class Culprit(SVGMobject):
    def __init__(self, mode, **kwargs):
        # Try opening the SVG files in the svg_files directory
        try:
            mode = str(mode)
            svg_file = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath( __file__ )), '..', 'svg_files', "culprit%s.svg" % mode))
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        # Warn and exit if the file doesn't exist
        except:
            warnings.warn("No SVG file for knot: %s" % mode)
            exit()