from manim import *
import manim

from manim_revealjs import PresentationScene, COMPLETE_LOOP


manim.config.video_dir= "./videos"


from latex_sy import gereftan

class av (MovingCameraScene , PresentationScene):
    def construct(self):
        moadele_ha = gereftan()
        moadelat = VGroup()
        for i in range(len(moadele_ha)):

            moadele = MathTex(moadele_ha[i])
            if i>0:
                moadele.next_to(moadelat[i-1],DOWN)
            moadelat.add(moadele)
        
        
        camera_height = moadelat.height  
        for i in range(len(moadelat)):
            self.play(Write(moadelat[i]) , 
            self.camera.frame.animate.move_to(moadelat[i]).set(width=moadelat[i].width*2))
            self.end_fragment()
        
        self.play(self.camera.frame.animate.move_to(moadelat[len(moadelat)//2]).set(width=camera_height*len(moadelat)*0.75))
        self.wait()
        self.end_fragment()
        """
        moadele = MathTex(r"   6 + a = 11     ")
        moadele.scale(3)
        moadele.move_to(2*UP)
        moadele.set_color(BLACK)
        self.play(Write(moadele))



        self.wait()


        moadele2 = MathTex(r"   6 + a = 11"," -6  ")
        moadele2.scale(3)
        moadele2.move_to(2*UP)
        moadele2[0].set_color(BLACK)
        moadele2[1].set_color(RED_C)

        #sond /home/mohammadsaleh/program/python/manim/project/sounds/switch.oga
        self.add_sound("/home/mohammadsaleh/program/python/manim/project/sounds/switch.oga")
        #transform moadele to moadele2
        self.play(Transform(moadele, moadele2))
        self.wait()
        matn= Text ("تعادل داره بهم می‌خوره.", font = "B kooodak", color = GREEN_E)
        matn.to_edge(UP)
        self.play(Write(matn,reverse=True))
        self.wait()
        self.play(Transform(matn,
        Text ("برای حفظ تعادل باید چکار کرد؟", font = "B kooodak", color = GREEN_E).to_edge(UP)))
        self.wait()
        self.add_sound("/home/mohammadsaleh/program/python/manim/project/sounds/switch.oga")
        moadele2 = MathTex(r"-6"," + 6 + a = 11"," -6")
        moadele2.move_to([0,2,0])
        moadele2[0].set_color(GREEN_E)
        moadele2[1].set_color(BLACK)
        moadele2[2].set_color(RED_C)
        moadele2.scale(2.7)
        self.play(Transform(moadele,moadele2) )
        self.wait(3)
        self.play(FadeOut(matn),
        FadeOut(moadele))
        self.wait(0.3)
        self.play(Write(Text("ادامه معادله با خود شما", font = "B nazanin", color = BLACK).scale(2),reverse=True))
        self.wait(2)
        self.add_sound("/home/mohammadsaleh/program/python/manim/project/sounds/trash.oga")
        self.wait(0.75)
        """