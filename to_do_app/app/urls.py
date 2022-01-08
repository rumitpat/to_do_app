from django.urls import path,include
from .views import *
urlpatterns = [
    path('task-lists/',task_listing,name ='task-lists'),
    path('<str:pk>/delete_task/', task_details_delete.as_view(), name='delete_task'),
    path('<str:pk>/edit_task/', edit_task, name='edit_task'),
    path('add_task/', add_task, name='add_task'),
    path('<str:task_id>/task_details/', task_details, name='task_details'),
    path('<str:pk>/task_status_change/', task_status_change, name='task_status_change'),
    path('task_history_page/', task_history_page, name='task_history_page'),
    path('<str:pk>/task_status_confirm/', task_status_confirm,name='task_status_confirm'),
    path('task-history-csv/', task_history_csv, name='task-history-csv'),
    path('<str:pk>/pdf_task/', pdf_task, name='pdf_task'),
    path('<str:pk>/task_pdf_mail/', task_pdf_mail, name='task-pdf-mail'),
]