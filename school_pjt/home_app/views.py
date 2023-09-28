from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from. models import*
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    # event_obj=Events.objects.all()
    sports_obj=Sports.objects.all()
    return render(request,'index.html',{'evnt':sports_obj})


def error(request):
    return render(request,'error.html')

def pending(request):
    return render(request,'sample.html')





# account authentication

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=2)  
        myuser.save()
        return redirect('login')
    return render(request,'register.html')



def login(request):
    if request.method == 'POST':     
      name=request.POST.get("username")
      password=request.POST.get("password")
      user=auth.authenticate(username=name,password=password)
    #   if user.role=='company':
      if user:         
          if user.role==2:
              auth.login(request,user)
              return redirect('red')
          elif user.role==3:
              auth.login(request,user)
              
              return redirect('blue')  
          elif user.role==4:
              auth.login(request,user)
              
              return redirect('green')  
          elif user.role==5:
              auth.login(request,user)
              
              return redirect('red-add') 
          elif user.role==7:
              auth.login(request,user)
              
              return redirect('green-add') 
          elif user.role==6:
              auth.login(request,user)
              
              return redirect('blue-add') 
          else:
              auth.login(request,user)
              return redirect('admin-home')
              
                     
      else:
       
        return HttpResponse("<h1>invalid user</h1>")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')







# blue group
def register_blue(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=6)  
        myuser.save()
        return redirect('login')
    return render(request,'register.html')

@login_required(login_url='login')
def blue(request):
    obj=CustomUser.objects.filter(username=request.user).first()
    print(obj)
    if not obj.role == 3:
        return redirect('error')

    # event_obj=Events.objects.all()
    sports_obj=Sports.objects.all()
    return render(request,'blue_home.html',{'evnt':sports_obj})

@login_required(login_url='login')
def Blue_Mem(request):
    mem_obj=Blue.objects.filter(user=request.user).first()
    if not mem_obj.is_activae:
        return redirect('pending')
    # red_obj=Green.objects.filter(user=request.user)
    sports_obj=SportsMembers.objects.filter(user=request.user)
   
    return render(request,'green_Mem.html',{'evnt':sports_obj})

@login_required(login_url='login')
def blueAdd(request):
    student_obj=Blue.objects.filter(user=request.user)
    if student_obj:
        return redirect('blue-mem')
    if request.method == 'POST':
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name') 
        cls=request.POST.get('class')
        edu_sample=Blue.objects.create(user=request.user,first_name=first_name,last_name=last_name,standard=cls)
       
        return redirect('blue-mem')

    return render(request,'addform.html')

@login_required(login_url='login')
def blueteam(request):
    blue_obj=Blue.objects.all()
    context={'mem':blue_obj}
    return render(request,'blue_team.html',context)

@login_required(login_url='login')
def conform_blue(request,id):
    conform_obj=Blue.objects.get(id=id)
    if not conform_obj.is_activae:
        conform_obj.is_activae= True
        conform_obj.save()
    return redirect('blue-team')


@login_required(login_url='login')
def eventadd_Blue(request,id):
    sports_obj=Sports.objects.get(id=id)
    blue_obj=Blue.objects.all()
   
    if request.method == 'POST':   
        user_id=request.POST.get('user')
        user_obj=Blue.objects.get(id=user_id)
        # custom_obj=CustomUser.objects.filter(username=user_obj)
        print(sports_obj)
        if sports_obj  :
            user_obj.sports_item=True
            user_obj.save()

        sample=SportsMembers.objects.create(sports=sports_obj,user=user_obj.user,role=user_obj.user.role)
        print(sample.user.role)
        return redirect('blue')
    return render(request,'blueAdd.html',{'blue1':blue_obj})

@login_required(login_url='login')
def blueStudentsItems(request):
    sportsmem_obj=SportsMembers.objects.filter(role=6)
    return render(request,'blue_sports_students.html',{'std':sportsmem_obj})


@login_required(login_url='login')
def delete(request,id):
    sports_obj=SportsMembers.objects.get(id=id).delete()
    return redirect('blue-studentitem')


# red group
def register_red(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=5)  
        myuser.save()
        return redirect('login')
    return render(request,'register.html')

@login_required(login_url='login')
def red(request):
    obj=CustomUser.objects.filter(username=request.user).first()
    print(obj)
    if not obj.role == 2:
        return redirect('error')
    # event_obj=Events.objects.all()
    sports_obj=Sports.objects.all()
    return render(request,'red_home.html',{'evnt':sports_obj})

@login_required(login_url='login')
def redAdd(request):
    student_obj=Red.objects.filter(user=request.user)
    if student_obj:
        return redirect('red-mem')
    if request.method == 'POST':
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name') 
        cls=request.POST.get('class')
        edu_sample=Red.objects.create(user=request.user,first_name=first_name,last_name=last_name,standard=cls)
       
        return redirect('red-mem')

    return render(request,'addform.html')

@login_required(login_url='login')
def redteam(request):
    blue_obj=Red.objects.all()
    context={'mem':blue_obj}
    return render(request,'red_team.html',context)

@login_required(login_url='login')
def conform_red(request,id):
    conform_obj=Red.objects.get(id=id)
    if not conform_obj.is_activae:
        conform_obj.is_activae= True
        conform_obj.save()
    return redirect('red-team')


@login_required(login_url='login')
def eventadd_Red(request,id):
    sports_obj=Sports.objects.get(id=id)
    red_obj=Red.objects.all()
    # sports_member_obj=SportsMembers.objects.filter(user=request.user)
    # if sports_member_obj:
    #     return redirect('sample')
    if request.method == 'POST':   
        user_id=request.POST.get('user')
        user_obj=Red.objects.get(id=user_id)
        # custom_obj=CustomUser.objects.filter(username=user_obj)
        print(sports_obj)
        if sports_obj  :
            user_obj.sports_item=True
            user_obj.save()

        sample=SportsMembers.objects.create(sports=sports_obj,user=user_obj.user,role=user_obj.user.role)
        print(sample.user.role)
        return redirect('red')
    return render(request,'RedAdd.html',{'red':red_obj})


@login_required(login_url='login')
def redStudentsItems(request):
    sportsmem_obj=SportsMembers.objects.filter(role=5)
    return render(request,'red_sports_students.html',{'std':sportsmem_obj})

@login_required(login_url='login')
def redMem(request):
    mem_obj=Red.objects.filter(user=request.user).first()
    if not mem_obj.is_activae:
        return redirect('pending')
    red_obj=Red.objects.filter(user=request.user)
    sports_obj=SportsMembers.objects.filter(user=request.user)
    sample=request.user
    print(sample)

    
    return render(request,'red_M.html',{'evnt':sports_obj})

@login_required(login_url='login')
def delete_Red(request,id):
    sports_obj=SportsMembers.objects.get(id=id).delete()
    return redirect('red-studentitem')








# green group

def register_green(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=7)  
        myuser.save()
        return redirect('login')
    return render(request,'register.html')

@login_required(login_url='login')
def green(request):
    obj=CustomUser.objects.filter(username=request.user).first()
    print(obj)
    if not obj.role == 4:
        return redirect('error')
    sports_obj=Sports.objects.all()
    return render(request,'green_home.html',{'evnt':sports_obj})

@login_required(login_url='login')
def green_Mem(request):
    mem_obj=Green.objects.filter(user=request.user).first()
    if not mem_obj.is_activae:
        return redirect('pending')
    # red_obj=Green.objects.filter(user=request.user)
    sports_obj=SportsMembers.objects.filter(user=request.user)
   
    return render(request,'green_Mem.html',{'evnt':sports_obj})

@login_required(login_url='login')
def greenteam(request):
    green_obj=Green.objects.all()
    context={'mem':green_obj}
    return render(request,'green_team.html',context)


@login_required(login_url='login')
def conform(request,id):
    conform_obj=Green.objects.get(id=id)
    if not conform_obj.is_activae:
        conform_obj.is_activae= True
        conform_obj.save()
    return redirect('green-team')

@login_required(login_url='login')
def greenAdd(request):


    student_obj=Green.objects.filter(user=request.user)
    if student_obj:
        return redirect('green-mem')
    if request.method == 'POST':
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name') 
        cls=request.POST.get('class')
        edu_sample=Green.objects.create(user=request.user,first_name=first_name,last_name=last_name,standard=cls)
       
        return redirect('green')

    return render(request,'addform.html')


@login_required(login_url='login')
def eventadd(request,id):
    
    green_obj=Green.objects.all()
    sports_obj=Sports.objects.get(id=id)
    # sports_member_obj=SportsMembers.objects.filter(user=request.user)
    # if sports_member_obj:
    #     return redirect('sample')
    if request.method == 'POST':   
        user_id=request.POST.get('user')
        user_obj=Green.objects.get(id=user_id)
        # custom_obj=CustomUser.objects.filter(username=user_obj)
        print(sports_obj)
        if sports_obj  :
            user_obj.sports_item=True
            user_obj.save()
        sample=SportsMembers.objects.create(sports=sports_obj,user=user_obj.user,role=user_obj.user.role)
        print(sample.user.role)    
        return redirect('green')
    return render(request,'greenAdd.html',{'green':green_obj})



@login_required(login_url='login')
def add(request,id):
    student_obj=Green.objects.get(id=id)
    student_name=student_obj.first_name
    print(student_name)
    # event_obj=Events.objects.get(id=1)
    # print(event_obj)
    print(student_obj)
    # sample=StudentEvnt.objects.create(event=event_obj,student=student_obj)
    return redirect('green-event')


@login_required(login_url='login')
def greenStudentsItems(request):
    sportsmem_obj=SportsMembers.objects.filter(role=7)
    return render(request,'green_sports_students.html',{'std':sportsmem_obj})

@login_required(login_url='login')
def delete_green(request,id):
    sports_obj=SportsMembers.objects.get(id=id).delete()
    return redirect('green-studentitem')


