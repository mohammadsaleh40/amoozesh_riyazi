from manim import *
import manim

from manim_revealjs import PresentationScene, COMPLETE_LOOP


manim.config.video_dir= "./videos"


class shib_khat(PresentationScene, MovingCameraScene):
    def construct(self):
        line = Line([-2,-1,0.2],[2,1,0.2] , stroke_width= 3.2).set_color(BLUE)
        self.play(Create(line))
        self.end_fragment()
        mehvar_y = Arrow([0,-3,1], [0, 3, 1], buff=0)
        mehvar_x = Arrow([-5,-1.5,0.1], [5, -1.5, 0.1], buff=0)
        self.play(Write(mehvar_x),
                  Write(mehvar_y))
        self.end_fragment()
        saye_x = Line([0, 0 , 0] , [1 , 0 , 0], stroke_width= 1.8)
        saye_y = Line([1 , 0 , 0] , [1 , 0.5 , 0], stroke_width= 1.8)
        self.play(Create(saye_x),
                  Create(saye_y))
        self.end_fragment()
        matn_mojaver  = BraceText(saye_x , "2" , brace_direction= DOWN  , buff = 0)
        matn_moghabel = BraceText(saye_y , "1" , brace_direction= RIGHT , buff = 0 )
        matn_mojaver.width = 1
        self.play(Write(matn_mojaver),
                  Write(matn_moghabel))
        self.end_fragment()
        
        matn = MathTex("m = \dfrac{1}{2}").move_to([4 , 3 , 0])
        self.play(Write(matn[0][:2]))
        self.end_fragment()
        
        self.play(Write(matn[0][3:4]))
        self.play(TransformMatchingShapes(matn_mojaver [1].copy() , matn[0][4:5], fade_transform_mismatches=True ))
        self.play(TransformMatchingShapes(matn_moghabel [1].copy() , matn[0][2:3], fade_transform_mismatches=True  ))
        self.end_fragment()

        