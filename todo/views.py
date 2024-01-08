from django.shortcuts import render
from .models import item

# Create your views here.


def get_todo_list(request):
    items = item.object.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)
