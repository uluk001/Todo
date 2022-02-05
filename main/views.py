from http.client import TOO_MANY_REQUESTS
from operator import index
from urllib import request
from django.shortcuts import render
from main.models import ToDo
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# def main(request):
#     return HttpResponse("Main page")
#Получение данных из базы данных
def main(request):
    try:
        todos = ToDo.objects.all()
        return render(request,'index.html', 
        {'todos':todos})
    except ToDo.DoesNotExist:
        return render(request, 'error.html')

#Создание данных в БД

def create(request):
    try:
        if request.method == 'POST':
            todo = ToDo()
            todo.title = request.POST.get('title')
            todo.discription = request.POST.get('discription')
            todo.save()
            return HttpResponseRedirect('/')
    except ToDo.DoesNotExist:
        return render(request, 'error.html')

def test(request, id):
    todos2 = ToDo.objects.all()
    return render(request, 'index.html',{'todos2':todos2, 'hello':'hello', 'id':id})


def delete(request, id):
    try:
        todo =ToDo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except ToDo.DoesNotExist:
        return render(request, 'error.html')


def edit(request, id):
    try:
        todo =ToDo.objects.get(id=id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.discription = request.POST.get('discription')
            todo.save()
            return HttpResponseRedirect('/')
        return render (request, 'edit.html', {'todo':todo})
    except ToDo.DoesNotExist:
        return render(request, 'error.html')

def tasks(request):
    try:
        return render (request, 'tasks.html')
    except ToDo.DoesNotExist:
        return render(request, 'error.html')



def tasks(request):
    try:
        todos2 = ToDo.objects.all()
        return render(request, 'tasks.html',{'todos2':todos2})
    except ToDo.DoesNotExist:
        return render(request, 'error.html')


def tasks(request):
    try:
        todos = ToDo.objects.all()
        return render(request,'tasks.html', 
        {'todos':todos})
    except ToDo.DoesNotExist:
        return render(request, 'error.html')