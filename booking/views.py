from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkSpace


def home(request):

    return render(
        request=request,
        template_name="booking/home.html",
    )


def workspace_list(request):
    workspaces = WorkSpace.objects.all()
    return render(request, 'booking/workspace_list.html', {'workspaces': workspaces})

# debugging line to check if workspaces are being fetched correctly
# print(WorkSpace.objects.all())