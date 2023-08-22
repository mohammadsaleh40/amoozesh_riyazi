from manim import *
import manim

from manim_revealjs import PresentationScene, COMPLETE_LOOP


manim.config.video_dir= "./videos"


class PresentationWithCameraScene(PresentationScene, MovingCameraScene):
    def construct(self):
        triangle1 = Polygon(  [-2 , -3 , 0] , [2 , -3 ,  0] , [-2 , -1 , 0] )
        triangle1.set_color(BLUE)

        line1 = Line(start = triangle1.get_vertex_groups()[0][0] , end = triangle1.get_vertex_groups()[0][1])
        line2 = Line(start = triangle1.get_vertex_groups()[0][0] , end = triangle1.get_vertex_groups()[0][2])
        
        zela_a1 = Tex("a").next_to(line1 , direction=DOWN)
        zela_b1 = Tex("b").next_to(line2 , direction=LEFT)
        
        angle1 = RightAngle(line2, line1, length=0.4, quadrant=(1,1) , color= WHITE)
        group1 = VGroup(triangle1 , angle1 )
        self.play(Create(group1))
        self.play(Write(zela_a1),
                  Write(zela_b1))
        #self.wait(0.4)
        self.end_fragment()
        grid = NumberPlane()
        
        
        #self.play(Create(grid, run_time=1, lag_ratio=0.1))
        
        #self.play(Write(triangle1))
        #self.add(triangle1)
        #self.wait(0.2)
        
        group2 = group1.copy()
        group2[0].color = YELLOW
        #self.play(Write(triangle2))
        #self.wait(0.2)
        self.play(Create(group2))
        #self.wait(0.4)
        
        temp = group2.copy().shift([-4 , 2 , 0])
        self.play(Transform(group2 ,temp ))
        #self.wait(0.4)
        self.end_fragment()
        #self.play(triangle2.animate.rotate(-PI/2 , about_point=[-2 , -1 , 0]))
        #self.play(TransformMatchingShapes(triangle2, temp, path_arc=PI))
        #triangle2.
        
        self.play(Rotate(group2, angle = -PI/2 , about_point = [-2 , -1 , 0]))
        #self.wait(0.4)
        line1 = Line(start = group2[0].get_vertex_groups()[0][0] , end = group2[0].get_vertex_groups()[0][1])
        line2 = Line(start = group2[0].get_vertex_groups()[0][0] , end = group2[0].get_vertex_groups()[0][2])
        
        zela_a2 = Tex("a").next_to(line1 , direction=LEFT)
        zela_b2 = Tex("b").next_to(line2 , direction=UP)
        
        self.play(Write(zela_a2),
                  Write(zela_b2))
        #self.wait(0.4)
        self.end_fragment()
        triangle3 = Polygon([-2 , -1 , 0] , [0 , 3 , 0] , [2 , -3 , 0] , color= RED)
        self.play(Create(triangle3))
        #self.wait(0.4)
        self.end_fragment()
        #self.wait(0.4)
        line1 = Line(start = triangle3.get_vertex_groups()[0][0] , end = triangle3.get_vertex_groups()[0][1])
        line2 = Line(start = triangle3.get_vertex_groups()[0][0] , end = triangle3.get_vertex_groups()[0][2])
        
        
        zela_c1 = Tex("c").next_to(line1.get_center() , direction=LEFT)
        zela_c2 = Tex("c").next_to(line2.get_center() , direction=DOWN)
        
        self.play(Write(zela_c1),
                  Write(zela_c2))
        #self.wait(0.4)
        self.end_fragment()
        angle3 = RightAngle(line1, line2, length=0.4, quadrant=(1,1) , color= WHITE)
        self.play(Create(angle3))
        #self.wait(0.4)
        self.end_fragment()
        #zela_a1 = Tex("a").move_to(line1.get_edge_center(LEFT))
        #self.wait(0.5)
        
        kole_shekl = VGroup(group1 , group2, triangle3 , zela_c1 , zela_c2 ,angle3)

        matn1 = MathTex("\dfrac{1}{2}ab + \dfrac{1}{2}ab & + \dfrac{1}{2}cc").next_to(kole_shekl , UR).shift(DOWN*1.5)
        
        self.play(self.camera.frame.animate.move_to([1.5 , 0 , 0]))
        #self.wait(0.4)
        self.end_fragment()
        self.play(group1[0].animate.set_fill(BLUE , opacity = 1))
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformFromCopy(triangle1.copy() , matn1[0][0:5] ))
        #self.wait(0.4)
        self.end_fragment()
        self.play(Write(matn1[0][5:6]))
        #self.wait(0.4)
        self.end_fragment()
        self.play(group2[0].animate.set_fill(YELLOW , opacity = 1))
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformFromCopy(group2[0].copy() , matn1[0][6:11] ))
        #self.wait(0.4)
        self.end_fragment()
        self.play(Write(matn1[0][11:12]))
        #self.wait(0.4)
        self.end_fragment()
        self.play(triangle3.animate.set_fill(RED , opacity = 1))
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformFromCopy(triangle3.copy() , matn1[0][12:17]),)
        #self.wait(0.4)
        self.end_fragment()
        matn2 = MathTex("ab & + \dfrac{1}{2}c^{2} = \dfrac{1}{2} \\times ( a + b )  \\times (a + b)").next_to(kole_shekl , UR).shift(DOWN*1.5)
        
        self.play(TransformMatchingShapes(matn1 , matn2[0][0:8] , fade_transform_mismatches=True , path_arc = PI/2))
        #self.wait(0.4)
        self.end_fragment()
        hight = Line(start = [-2 , -3 , 0] , end = [-2 , 3 , 0])
        
        #bracet = Brace(hight , direction=LEFT , sharpness=1 )
        bracet_text = BraceText(hight , "b+a" , brace_direction=LEFT )

        self.play(matn2[0][0:8].animate.shift(LEFT*1.5))
        matn2[0][8:].shift(LEFT*1.5)
        self.end_fragment()
        self.play(Transform(VGroup(zela_b1 , zela_a2) , bracet_text))
        #self.wait(0.4)
        self.end_fragment()
        self.play(Write(matn2[0][9:13]))
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformFromCopy(bracet_text.copy() , matn2[0][13:18] ))
        #self.wait(0.4)
        self.end_fragment()
        self.play(Write(matn2[0][18:19]))
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformFromCopy(VGroup(zela_b2 , zela_a1).copy() , matn2[0][19:24] ))
        #self.wait(0.4)
        self.end_fragment()
        self.play(Write(matn2[0][8:9]))
        #self.wait(0.4)
        self.end_fragment()
        matn3 = MathTex("ab & + \dfrac{1}{2}c^{2} = \dfrac{1}{2} ( a^{2} + b^{2} )  + ab").next_to(kole_shekl , UR).shift(DOWN*1.5)
        
        self.play(TransformMatchingShapes(matn2 , matn3))
        #self.wait(0.4)
        self.end_fragment()
        matn4 = MathTex("\dfrac{1}{2}c^{2} = \dfrac{1}{2} ( a^{2} + b^{2} )").next_to(kole_shekl , UR).shift(DOWN*1.5)
        
        self.play(TransformMatchingShapes(matn3 , matn4))
        matn5 = MathTex("c^{2} =  a^{2} + b^{2} ").next_to(kole_shekl , UR).shift(DOWN*1.5)
        #self.wait(0.4)
        self.end_fragment()
        self.play(TransformMatchingShapes(matn4 , matn5))
        #self.wait(0.4)
        self.end_fragment()