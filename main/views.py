from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .services import (
    get_todo_list,
    create_todo,
    delete_todo,
    get_todo_via_pk,
    edit_todo,
    is_done,
)

def main(request):
    queryset = get_todo_list()
    return render(request,'index.html', {'queryset':queryset})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        create_todo(title, description)
    return HttpResponseRedirect('/')


def test(request, id):
    todos2 = get_todo_list()
    return render(request, 'index.html',{'todos2':todos2, 'hello':'hello', 'id':id})


def delete(request, pk):
    delete_todo(pk)
    return HttpResponseRedirect('/')


def edit(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = edit_todo(title, description, pk)
        return HttpResponseRedirect('/')
    todo = get_todo_via_pk(pk)
    return render(request, 'edit.html', {'todo': todo})


def tasks(request):
    queryset = get_todo_list()
    return render(request, 'tasks.html',{'queryset':queryset})


def is_done_view(request, pk):
    is_done(pk=pk)
    return HttpResponseRedirect('/')
