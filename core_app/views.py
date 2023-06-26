from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from django.contrib import messages
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core_app:cbvhome')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'core/update1.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('core_app:cbvdetail', kwargs={'pk': self.object.id})


class TaskDetailview(DetailView):
    model = Task
    template_name = 'core/detail.html'
    context_object_name = 'task'


class TaskListview(ListView):
    model = Task
    template_name = 'core/index.html'
    context_object_name = 'task1'


def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'core/index.html', {'task1': task1})


def base(request):
    return render(request, 'core/base.html')


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'core/delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'core/update.html', {'f': f, 'task': task})
