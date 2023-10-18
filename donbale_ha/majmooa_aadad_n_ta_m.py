from manim import *
import manim

from manim_revealjs import PresentationScene, COMPLETE_LOOP


manim.config.video_dir= "./videos"


class majmooa1(PresentationScene, MovingCameraScene):
    def construct(self):
        
        l = ["{{1+2}}{{=}}{{?}}" , "{{1+2}} {{=}} {{$\Box$}}" , "{{1+2}} = {{$\Box$}} = 3", "{{1+2}} = {{$\Box$}}" , "{{1+2}} = {{A}}" ]
        l_t12 = VGroup(*[Tex(l[i]) for i in range(len(l))]) 
        
        self.play(Write(l_t12[0]),
        self.camera.frame.animate.move_to(l_t12[0]).set(width=l_t12[0].width*2))
        self.end_fragment()
        for i in range(1,len(l)):
            self.play(TransformMatchingTex(l_t12[i-1] , l_t12[i]  ),
            self.camera.frame.animate.move_to(l_t12[i]).set(width=l_t12[i].width*2))
            self.end_fragment()
        
        t_21_re = Tex("2+1 = A").next_to(l_t12[-1],DOWN)
        #self.play(Write(t_21_re[0][2]))
        self.play(ReplacementTransform(l_t12[-1][0][0].copy() ,t_21_re[0][2]))
        self.play(ReplacementTransform(l_t12[-1][0][1].copy() ,t_21_re[0][1]))
        self.play(ReplacementTransform(l_t12[-1][0][2].copy() ,t_21_re[0][0]))
        
        self.end_fragment()

        self.play(ReplacementTransform(l_t12[-1][1][0].copy() ,t_21_re[0][3]),ReplacementTransform(l_t12[-1][2][0].copy() ,t_21_re[0][4]))
        self.end_fragment()
        li = Line()
        li.width = t_21_re.width
        li.next_to(t_21_re,DOWN)
        plus = Tex("+")
        plus.next_to(li , UL)
        t_33 = Tex("{{3+3}} {{=}} {{A}}{{+}}{{A}}").next_to(li , DOWN)
        
        g_12 = VGroup(l_t12[-1] , t_21_re ,li ,plus ,t_33)
        self.play(Write(li),Write(plus),
        self.camera.frame.animate.move_to(g_12).set(width=g_12.width*2))

        self.end_fragment()
        
        self.play(ReplacementTransform(VGroup(*[l_t12[-1][1][0].copy() ,t_21_re[0][3].copy()]),t_33[2][0]))
        self.play(ReplacementTransform(VGroup(*[l_t12[-1][0][0].copy() ,t_21_re[0][0].copy()]),t_33[0][0]))
        self.play(ReplacementTransform(VGroup(*[l_t12[-1][0][2].copy() ,t_21_re[0][2].copy()]),t_33[0][2]))
        self.play(ReplacementTransform(l_t12[-1][2][0].copy() ,t_33[4]) , ReplacementTransform(t_21_re[0][4].copy() ,t_33[6]) , Write(t_33[5]))
        
        self.play(ReplacementTransform(VGroup(*[l_t12[-1][0][1].copy() ,t_21_re[0][1].copy()]),t_33[0][1]))
        self.end_fragment()
        
        t_33_temp = Tex("{{3+3}} {{=}} 2{{A}}").move_to(t_33)
        self.play(TransformMatchingTex(t_33 , t_33_temp))
        self.end_fragment()
        t_62A = Tex("{{6}} {{=}} 2{{A}}").move_to(t_33_temp)

        self.play(FadeOut(l_t12[-1] , t_21_re ,li ,plus ),
        TransformMatchingTex(t_33_temp,t_62A),
        self.camera.frame.animate.move_to(t_62A).set(width=t_62A.width*2)
        )
        self.end_fragment()

        t_6fra = Tex("$\\frac{6}{2} = \\frac{2A}{2}$").move_to(t_62A)#.shift(DOWN*.5)
        t_3A = Tex("3 {{=}} {{A}}").move_to(t_6fra)
        
        #for i in range(len(t_6fra[0])):
        #    self.play(Write(t_6fra[0][i]))
        
        self.play(#FadeOut(t_62A),
        ReplacementTransform(t_62A[0][0] , t_6fra[0][0]),
        ReplacementTransform(t_62A[2][0] , t_6fra[0][3]),
        ReplacementTransform(t_62A[3][0] , t_6fra[0][4]),
        ReplacementTransform(t_62A[4][0] , t_6fra[0][5]))
        self.play(*[Write(x) for x in [t_6fra[0][1] , t_6fra[0][2] , t_6fra[0][6] , t_6fra[0][7]]],
        )
        self.end_fragment()
        self.play(ReplacementTransform(t_6fra , t_3A))
        
        self.end_fragment()
        self.play(FadeOut(t_3A))
        self.end_fragment()


class majmooa2(PresentationScene, MovingCameraScene):
    def construct(self):
                

        pas = Text("پس چی شد؟" , font = "danstevis")
        self.play(Write(pas, reverse=True, remover=False))
        
        self.end_fragment()
        self.play(FadeOut(pas))
        self.end_fragment()
class majmooa3(PresentationScene, MovingCameraScene):
    def construct(self):
        t_12 = Tex("{{1+2}} = {{A}}")
        t_21_re = Tex("2+1 = A").next_to(t_12,DOWN)
        li = Line()
        li.width = t_21_re.width
        li.next_to(t_21_re,DOWN)
        plus = Tex("+")
        plus.next_to(li , UL)
        t_33 = Tex("{{3+3}} {{=}} {{A}}{{+}}{{A}}").next_to(li , DOWN)
        t_33_temp = Tex("{{3+3}} {{=}} 2{{A}}").move_to(t_33)
        t_62A = Tex("{{6}} {{=}} 2{{A}}").move_to(t_33_temp)
        t_6fra = Tex("$\\frac{6}{2} = \\frac{2A}{2}$").move_to(t_62A)
        t_3A = Tex("3 {{=}} {{A}}").move_to(t_6fra)

        kole_12 = VGroup(t_12 , t_21_re , li  , plus , t_33 , t_33_temp , t_62A , t_6fra , t_3A)
        self.camera.frame.move_to(kole_12).set(width=kole_12.width*2)
        self.add(t_12)
        self.end_fragment()
        self.play(Write(t_21_re))
        self.end_fragment()
        self.play(Write(plus) , Create(li))
        self.end_fragment()
        self.play(ReplacementTransform(VGroup(*[t_12[1][0].copy() ,t_21_re[0][3].copy()]),t_33[2][0]))
        self.play(ReplacementTransform(VGroup(*[t_12[0][0].copy() ,t_21_re[0][0].copy()]),t_33[0][0]))
        self.play(ReplacementTransform(VGroup(*[t_12[0][2].copy() ,t_21_re[0][2].copy()]),t_33[0][2]))
        self.play(ReplacementTransform(t_12[2][0].copy() ,t_33[4]) , ReplacementTransform(t_21_re[0][4].copy() ,t_33[6]) , Write(t_33[5]))
        
        self.play(ReplacementTransform(VGroup(*[t_12[0][1].copy() ,t_21_re[0][1].copy()]),t_33[0][1]))
        self.end_fragment()
        self.play(TransformMatchingTex(t_33 , t_33_temp))
        self.end_fragment()
        self.play(TransformMatchingTex(t_33_temp,t_62A))
        self.end_fragment()
        self.play(#FadeOut(t_62A),
        ReplacementTransform(t_62A[0][0] , t_6fra[0][0]),
        ReplacementTransform(t_62A[2][0] , t_6fra[0][3]),
        ReplacementTransform(t_62A[3][0] , t_6fra[0][4]),
        ReplacementTransform(t_62A[4][0] , t_6fra[0][5]))
        self.play(*[Write(x) for x in [t_6fra[0][1] , t_6fra[0][2] , t_6fra[0][6] , t_6fra[0][7]]],
        )
        self.end_fragment()
        self.play(ReplacementTransform(t_6fra , t_3A))
        
        self.end_fragment()
        self.play(FadeOut(t_3A , plus , li , t_12 , t_21_re))
        self.end_fragment()

class majmooa4(PresentationScene, MovingCameraScene):
    def construct(self):
        l = ["{{1+2+3+4+5+6+7+8+9+10}}{{=}}{{?}}" , "{{1+2+3+4+5+6+7+8+9+10}} {{=}} {{$\Box$}}" , "{{1+2+3+4+5+6+7+8+9+10}} = {{$\Box$}} = 55", "{{1+2+3+4+5+6+7+8+9+10}} = {{$\Box$}}" , "{{1+2+3+4+5+6+7+8+9+10}} = A" ]
        l_t12 = VGroup(*[Tex(l[i]) for i in range(len(l))]) 
        
        self.play(Write(l_t12[0]),
        self.camera.frame.animate.move_to(l_t12[0]).set(width=l_t12[0].width*2) , run_time = 0.5)
        self.end_fragment()
        for i in range(1,len(l)):
            self.play(TransformMatchingTex(l_t12[i-1] , l_t12[i]  ),
            self.camera.frame.animate.move_to(l_t12[i]).set(width=l_t12[i].width*2))
            self.end_fragment()
        
        t_21_re = Tex("10+9+8+7+6+5+4+3+2+1 = A").next_to(l_t12[-1],DOWN)
        for i in range(0 ,18):
            self.play(ReplacementTransform(l_t12[-1][0][i].copy() ,t_21_re[0][19-i]))
        #self.play(ReplacementTransform(l_t12[-1][0][0].copy() ,t_21_re[0][2]))
        #self.play(ReplacementTransform(l_t12[-1][0][1].copy() ,t_21_re[0][1]))
        #self.play(ReplacementTransform(l_t12[-1][0][2].copy() ,t_21_re[0][0]))
        self.play(ReplacementTransform(l_t12[-1][0][18:20].copy() ,VGroup(*[t_21_re[0][0] , t_21_re[0][1]])))
        self.play(ReplacementTransform(l_t12[-1][1:].copy() , t_21_re[0][-2:] ))
        
        self.end_fragment()
        