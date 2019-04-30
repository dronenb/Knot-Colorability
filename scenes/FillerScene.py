import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from knot import *

class FillerScene(KnotScene):
    def construct(self):
        unknot = Knot()
        trefoil1 = Knot("3_1")
        trefoil2 = Knot("3_1")

        unknot.scale(1.5)
        trefoil1.scale(1.5)
        trefoil2.scale(1.5)

        neq = TexMobject(r"\neq")
        neq.scale(2)

        # Draw trefoil
        self.play(*DrawKnot(trefoil1))

        # Morph to unknot
        self.wait()
        self.play(Transform(trefoil1, unknot))
        self.wait()

        # Color red then white
        self.play(ApplyMethod(trefoil1.set_fill, RED))
        self.play(ApplyMethod(trefoil1.set_fill, WHITE))

        self.play(Transform(trefoil1, trefoil2))


        # Move left
        self.play(ApplyMethod(trefoil1.shift, LEFT * 3))

        # Draw unknot again to right
        self.play(ShowCreation(unknot))
        self.play(ApplyMethod(unknot.shift, RIGHT * 3))

        # Show neq
        self.play(ShowCreation(neq))
        
        
        self.wait()
        self.play(FadeOut(VGroup(*self.get_mobjects())))
        self.wait()
