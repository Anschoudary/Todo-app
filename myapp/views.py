from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        if not title or not details or not priority or not due_date:
            messages.error(request, 'All fields are required.')
            form_data = {
                'title': title,
                'details': details,
                'priority': priority,
                'due_date': due_date,
            }
            return render(request, 'index.html', {
                'tasks': tasks,
                'form_data': form_data
            })
        else:
            if 'create' in request.POST:
                Task.objects.create(title=title, detail=details, priority=priority, due_date=due_date)
                messages.success(request, 'Task created successfully.')
            elif 'update' in request.POST:
                task_id = request.POST.get('task_id')
                task = get_object_or_404(Task, id=task_id)
                task.title = title
                task.detail = details
                task.priority = priority
                task.due_date = due_date
                task.save()
                messages.success(request, 'Task updated successfully.')
            return redirect('home')

    return render(request, 'index.html', {'tasks': tasks})

def edit(request, id):
    task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks, 'edit_id': task})

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('home')
