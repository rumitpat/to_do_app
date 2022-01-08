import django_tables2 as tables
from .models import TaskData
from django_tables2.utils import A
import datetime
from .models import *
from django.shortcuts import get_object_or_404

def task_due_date_color_for_row(**kwargs):
    row = kwargs.get("record", None)
    task_data_id =row.pk
    d1 =datetime.datetime.now()
    today_date =d1.date()
    if (row.task_end_date) < (today_date):
        taskdata_obj =get_object_or_404(TaskData, pk =task_data_id)
        taskdata_obj.task_due_date_color_data ='red'
        taskdata_obj.save()
        return "color:red;"
    else:
        return 'color:black;'


class PandingTaskTable(tables.Table):
    delete = tables.TemplateColumn(template_name='app/table_task_delete_btn.html',orderable =False)
    edit = tables.TemplateColumn(template_name='app/table_task_edit_btn.html',orderable =False)
    Status = tables.TemplateColumn(template_name='app/task_status_panding_btn.html',orderable =False)
    # task_id = tables.Column(linkify=('task_details', {'id': A('id')}))
    task_name = tables.LinkColumn('task_details', args=[A('pk')])
    class Meta:
        row_attrs = {
            "style": task_due_date_color_for_row
        }
        attrs = {'class': 'table table-centered datatable dt-responsive nowrap table-card-list','style':"border-collapse: collapse; border-spacing: 0 12px; width: 100%"}
        model = TaskData
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("task_id","task_name","task_created_date","test_created_time","task_end_date","task_end_time","delete","edit")


class ComplateTaskTable(tables.Table):
    print = tables.TemplateColumn(template_name='app/table_task_print_btn.html')
    delete = tables.TemplateColumn(template_name='app/table_task_delete_btn.html')
    Status = tables.TemplateColumn(template_name='app/task_status_complate_btn.html')
    # task_id = tables.Column(linkify=('task_details', {'id': A('id')}))
    task_name = tables.LinkColumn('task_details', args=[A('pk')])
    class Meta:
        row_attrs = {
            "style": task_due_date_color_for_row
        }
        attrs = {'class': 'table table-centered datatable dt-responsive nowrap table-card-list','style':"border-collapse: collapse; border-spacing: 0 12px; width: 100%"}
        model = TaskData
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("task_id","task_name","task_created_date","test_created_time","task_end_date","task_end_time","delete")
