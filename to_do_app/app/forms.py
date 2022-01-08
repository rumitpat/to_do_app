from django import forms
from .models import TaskData

class TaskDataAddForm(forms.ModelForm):
     class Meta:
        model = TaskData
        fields = ['task_id','task_name', 'task_details', 'task_end_date', 'task_end_time']