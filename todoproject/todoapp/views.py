

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from . models import Task
from . forms import Taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView



class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class Detailview(DetailView):
    model=Task
    template_name = "details.html"
    context_object_name = 'task'

class Updateview(UpdateView):
    model = Task
    template_name = "update.html"
    context_object_name = "task"
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})

class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:home')

def home(request):
    task = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        todo=Task(name=name,priority=priority,date=date)
        todo.save()
    return render(request,'home.html',{'task':task})
# def details(request):
#
#     return render(request,'details.html',{'task':task})
def delete(request,id):
    if request.method=="POST":
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    edit=Taskform(request.POST or None,request.FILES,instance=task)
    if edit .is_valid():
        edit.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'edit':edit})


