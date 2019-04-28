from manim.big_ol_pile_of_manim_imports import *

def fade_out_scene(scene):
    everything = VGroup(scene.get_mobjects())
    self.play(FadeOut(everything))
