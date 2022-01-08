from django.shortcuts import redirect, render,HttpResponse
from Auth.models import UserRegister
# from django_tables2 import SingleTableView
from .tables import *
from .models import *
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import TaskDataAddForm
from django.http import HttpResponsePermanentRedirect,HttpResponseRedirect
from .filters import *
from django.contrib import messages
from django.db.models import Q
from django_tables2.config import RequestConfig
from django.core.paginator import Paginator
import csv
from django.contrib import messages
from . import utils
import smtplib
from .emails import *
# Create your views here.

#send email to user.



def task_listing(request):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        qur =request.GET
        task_data =TaskData.objects.filter(task_status='False',user__username=login_user)
        table_filter = tasks_filter(qur,task_data)
        table = PandingTaskTable(table_filter.qs)
        paginate = {'per_page': 5, 'page': 1}
        RequestConfig(request,paginate).configure(table)
        content ={"login_user_obj":login_user_obj,"table":table,"filter":table_filter,"task_data":task_data}
        return render(request,'app/task-lists.html',content)
    else:
        return redirect('user-login')


class task_details_delete(DeleteView):
    model = TaskData
    success_url = reverse_lazy("task-lists")


def edit_task(request,pk):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        login_user_taskdata =get_object_or_404(TaskData, pk =pk)
        edit_task_form =TaskDataAddForm(instance=login_user_taskdata)
        if request.method == 'POST':
            edit_task_form = TaskDataAddForm(request.POST, instance=login_user_taskdata)
            if edit_task_form.is_valid():
                print("in function")
                edit_task_form.save()
                return redirect('task-lists')
        content ={"login_user_obj":login_user_obj,'edit_task_form':edit_task_form}
        return render(request,'app/task_edit.html',content)
    else:
        return redirect('user-login')    

def task_status_change(request,pk):
    if request.session.has_key('username'):
        #change task status.
        task_obj =get_object_or_404(TaskData, pk =pk)
        task_obj.task_status = 'True'
        task_obj.save()
        return redirect('task-lists')
    else:
        return redirect('user-login')    

def task_history_page(request):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        qur =request.GET
        task_data =TaskData.objects.filter(task_status='True',user__username=login_user)
        table_filter = tasks_filter(qur,task_data)
        table = ComplateTaskTable(table_filter.qs)
        paginate = {'per_page': 5, 'page': 1}
        RequestConfig(request,paginate).configure(table)
        content ={"login_user_obj":login_user_obj,"table":table,"filter":table_filter,"task_data":task_data}
        return render(request,'app/task_history.html',content)
    else:
         return redirect('user-login')   

def add_task(request):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        add_task_form =TaskDataAddForm()
        if request.method == 'POST':
            add_task_form =TaskDataAddForm(request.POST)
            if add_task_form.is_valid():
                obj =TaskData()
                obj.user = UserRegister.objects.get(username =login_user)
                obj.task_id = add_task_form.cleaned_data['task_id']
                obj.task_name = add_task_form.cleaned_data['task_name']
                obj.task_details = add_task_form.cleaned_data['task_details']
                obj.task_end_date = add_task_form.cleaned_data['task_end_date']
                obj.task_end_time = add_task_form.cleaned_data['task_end_time']
                obj.task_status = 'False'
                obj.save()
                return redirect('task-lists')
        content ={"login_user_obj":login_user_obj,'add_task_form':add_task_form}
        return render(request,'app/task_add.html',content)
    else:
        return redirect('user-login')  

def task_details(request,task_id):
    if request.session.has_key('username'):
        login_user =request.session["username"]
        login_user_obj =UserRegister.objects.get(username= login_user)
        task_obj = get_object_or_404(TaskData, pk = task_id)
        content ={"login_user_obj":login_user_obj,'tash_obj':task_obj}
        return render(request,'app/task_details.html',content)
    else:
        return redirect('user-login')    


def task_status_confirm(request,pk):
    content ={'pk':pk}
    return render(request,'app/task_status_confirm.html',content)


def task_history_csv(request):
    username =request.session['username']
    task_data =TaskData.objects.filter(task_status ='True',user__username =username)
    col_list =['task_id','task_name','task_created_date','task_created_time','task_end_date','task_end_time']
    task_id_list,task_name_list,task_created_date_list,task_created_time_list,task_end_date_list,task_end_time_list =[],[],[],[],[],[]
    task_data_count =0
    for data in task_data:
            task_id_list.append(data.task_id)
            task_name_list.append(data.task_name)
            task_created_date_list.append(data.task_created_date)
            task_created_time_list.append(data.test_created_time)
            task_end_date_list.append(data.task_end_date)
            task_end_time_list.append(data.task_end_time)
            task_data_count = task_data_count + 1

    with open(f'static/csv_files/task_history_{username}.csv','a',newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(col for col in col_list)
        for i in range(0,task_data_count):
            csv_writer.writerow([task_id_list[i],task_name_list[i],task_created_date_list[i],task_created_time_list[i],task_end_date_list[i],task_end_time_list[i]])
    csv_path =f'csv_files/task_history_{username}.csv'
    content ={"csv_path":csv_path}
    return render(request, 'app/task_history_download.html',content)


def pdf_task(request,pk):
    if request.session.has_key('username'):
        username =request.session['username']
        login_user_obj =UserRegister.objects.get(username= username)
        # pdfkit.from_file('task_pdf.html', 'out.pdf')
        # print(pk, "pk................")
        task_obj = get_object_or_404(TaskData, pk = pk)
        content ={"login_user_obj":login_user_obj,'task_obj':task_obj}
        return render(request,'app/task_pdf.html',content)

def task_pdf_mail(request,pk):
    username =request.session['username']
    task_obj = get_object_or_404(TaskData, pk = pk)
    content ={'task_obj':task_obj,"username":username}
    # return render(request,'app/task_pdf_1.html',content)
    utils.render_to_pdf('app/task_pdf_1.html',content)
    send_email(task_obj)
    messages.success(request, 'Email Send Successful!')
    return redirect('pdf_task',pk=pk)

    

