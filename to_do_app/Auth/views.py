from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from app.models import *

# Create your views here.
def login(request):
    if request.session.has_key('username'):
        return redirect('home')
    else:
        if request.method =='POST':
            username =request.POST['username']
            # print(username)
            userpassword =request.POST['userpassword']
            try:
                exit_user =UserRegister.objects.get(username =username)
                print(exit_user,"aaaaaaaaa")
                exit_username =exit_user.username
                exit_password =exit_user.userpassword
                # print(exit_username,exit_password)
                if username ==exit_username:
                    if userpassword == exit_password:
                        # session create
                        request.session['username'] = username
                        # print(request.session['username'])
                        # print("session created..")
                        return redirect('home')
                    else:
                        messages.warning(request, f'password wrong!')    
                else:
                    messages.warning(request, f'username alwardy exits!')
            except:
                messages.warning(request, f'Sing Up please!')        
        return render(request,'Auth/auth-login.html')


def register(request):
    if request.session.has_key('username'):
        return redirect('home')
    else:    
        if request.method =='POST':
            username =request.POST['username']
            useremail =request.POST['useremail']
            userpassword =request.POST['userpassword']
            if UserRegister.objects.filter(username =username):
                messages.warning(request, 'Account Alwardy exits!')
                return redirect('user-register')
            else:
                UserRegister(username =username,useremail =useremail,userpassword =userpassword).save()
                messages.success(request, 'Account created!')
                return redirect('user-login')
        return render(request,'Auth/auth-register.html')
 
def logout(request):
    if request.session.has_key('username'):
        print(request.session['username'])
        del request.session['username']
        return redirect('user-login')
    else:
        print("in else")
        return redirect('user-login')    

def profile(request):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        
        content ={"login_user_obj":login_user_obj}
        if request.method =='POST':
            if 'userprofile_form' in request.POST:
                username =request.POST['username']
                useremail =request.POST['useremail']
                usermobilenu =request.POST['usermobilenumber']
                userdob =request.POST['userdob']
                userimages =request.FILES.get('userimage')
                if userimages is None:
                    userimages = login_user_obj.userimage
                login_user_obj.username  = username
                login_user_obj.useremail = useremail
                login_user_obj.usermobilenumber = usermobilenu
                login_user_obj.userdob = userdob
                login_user_obj.userimage = userimages
                login_user_obj.save()
                # messages.success(request,'Profile updated!')
                return redirect('user-profile')
            else:
                usernewpassword =request.POST['newpassword']
                login_user_obj.userpassword  = usernewpassword
                login_user_obj.save()
                messages.success(request, 'Password change!')
                return redirect('user-profile')
        return render(request,'Auth/profile.html',content)
    else:
          return redirect('user-login')  

def home(request):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        due_date_task_obj =TaskData.objects.filter(task_due_date_color_data ='red',user__username =login_user)
        total_task_count =TaskData.objects.filter(user__username =login_user).count()
        due_date_task_obj_count =TaskData.objects.filter(task_due_date_color_data ='red',user__username =login_user).count()
        panding_task_obj_count =TaskData.objects.filter(task_status ='False',user__username =login_user).count()
        completed_task_obj_count =TaskData.objects.filter(task_status ='True',user__username =login_user).count()

        content ={"login_user_obj":login_user_obj,
        "due_date_task_obj":due_date_task_obj,
        "total_task_count":total_task_count,
        "due_date_task_obj_count":due_date_task_obj_count,
        "panding_task_obj_count":panding_task_obj_count,
        "completed_task_obj_count":completed_task_obj_count
        }
        return render(request,'Auth/index.html',content)
    else:
        return redirect('user-login') 


def forgot_passsword_save():
    pass          