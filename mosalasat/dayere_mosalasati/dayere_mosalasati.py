from manim import *
import manim
from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip
from manim_revealjs import PresentationScene, COMPLETE_LOOP


manim.config.video_dir= "./videos"


class dayere_mosalasati(PresentationScene, MovingCameraScene):
    def construct(self):

        dayere = Circle()
        
        self.play(self.camera.frame.animate.set(width=14),run_time=0.00000000001)
        
        a=2
        alpha= ValueTracker(0)
        my_plane = NumberPlane(x_range=[-2.75*a,2.75*a,1], y_range=[-1.75*a,1.75*a,1],
        x_length = 5.5*a, y_length= 3.5*a) 
        
        axes = Axes(x_range=[-2.75*a,2.75*a,1], y_range=[-1.75*a,1.75*a,1],
        x_length = 5.5*a, y_length= 3.5*a)
        axes.add_coordinates()
        
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")

        noghte = always_redraw(lambda:
        Dot(point=dayere.point_from_proportion(alpha.get_value())+np.array((0, 0.0000000001,0)) ,color=GREEN).scale(1))
        
        shoaa = Line(start=dayere.get_center() , end=dayere.get_right(), stroke_width=6)
        shoaa2 = always_redraw(lambda:
        Line(start=dayere.get_center() , end=dayere.point_from_proportion(alpha.get_value())+np.array((0, 0.0000000001,0)) , stroke_width=6)
        )
        hashiye = always_redraw(lambda:
        Angle(shoaa , shoaa2)
        )
        zaviye = VGroup(shoaa2 , hashiye)



        self.add(shoaa  , noghte  , axes_labels, dayere ,zaviye, axes ,my_plane
        )
        
        self.play(alpha.animate.set_value(0.9999),run_time=7,rate_func=rate_functions.linear)
        self.end_fragment()
        self.wait(4)
        