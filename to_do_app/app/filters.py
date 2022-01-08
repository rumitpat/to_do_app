import django_filters
from .models import *
import floppyforms


class tasks_filter(django_filters.FilterSet):
    task_created_date = django_filters.CharFilter(label="Task Create Date", lookup_expr='icontains')
    task_name = django_filters.CharFilter(label="Task Name", lookup_expr='icontains')
    class Meta:
        model = TaskData
        fields = ('task_name', 'task_created_date')  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args[1]:
            task_name_val = TaskData.objects.filter(user__username =args[1][0].user.username).values_list('task_name','task_created_date')
            TASK_NAME_CHOICES = []
            TASK_DATE_CREATE_CHOICES =[]
            for i in task_name_val:
                TASK_NAME_CHOICES.append(i[0])
                TASK_DATE_CREATE_CHOICES.append(i[1])
            self.filters['task_name'].extra.update({'widget': floppyforms.widgets.Input(datalist=TASK_NAME_CHOICES)})
            self.filters['task_created_date'].extra.update({'widget': floppyforms.widgets.Input(datalist=TASK_DATE_CREATE_CHOICES)})
        else:
            pass