from django.urls import path
from . import views

urlpatterns = [
    
    
    path('pending/',views.pending,name='pending' ),
    path('error/',views.error,name='error' ),
    
    # account
    path('reg/',views.register,name='reg' ),
    path('login/',views.login,name='login' ),
    path('',views.home,name='home', ),
    path('logout/',views.logout,name='logout' ),

    # red
    path('reg_red/',views.register_red,name='reg-r' ),
    path('addform_r/',views.redAdd,name='red-add' ),
    path('red-home/',views.red,name='red' ),
    path('red_team/',views.redteam,name='red-team' ),
    path('red_team/<int:id>',views.conform_red,name='conf-red' ),
    path('red-event/<int:id>',views.eventadd_Red,name='red-eventAdd1' ),
    path('red-studentitem/',views.redStudentsItems,name='red-studentitem' ),

    path('red-delete/<int:id>',views.delete_Red,name='red-delete' ),

    # red mem
    path('red-mem/',views.redMem,name='red-mem' ),

    


    # green
    path('reg_green/',views.register_green,name='reg-g' ),
    path('green_team/',views.greenteam,name='green-team' ),
    path('green_team/<int:id>',views.conform,name='conf' ),
    path('addform_g/',views.greenAdd,name='green-add' ),
    path('green-home/',views.green,name='green' ),
    path('green-event/<int:id>',views.eventadd,name='green-event' ),
    
    path('green-studentitem/',views.greenStudentsItems,name='green-studentitem' ),
    path('green_event/<int:id>',views.add,name='add' ),
    path('green-delete/<int:id>',views.delete_green,name='green-delete' ),


    # greenl members
    path('green-mem/',views.green_Mem,name='green-mem' ),




    


    # blue
    path('reg_blue/',views.register_blue,name='reg-c' ),
    path('addform_b/',views.blueAdd,name='blue-add' ),
    path('blue-home/',views.blue,name='blue' ),
    path('blue_team/',views.blueteam,name='blue-team' ),
    path('blue_team/<int:id>',views.conform_blue,name='conf-blue' ),
    path('blue-event/<int:id>',views.eventadd_Blue,name='blue-eventAdd' ),
    path('blue-studentitem/',views.blueStudentsItems,name='blue-studentitem' ),

    path('blue-dle/<int:id>',views.delete,name='blue-delete' ),


    # blue members
    path('blue-mem/',views.Blue_Mem,name='blue-mem' ),

]