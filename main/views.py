from django.shortcuts import render, redirect
from . import forms

todo = [
    {'id': 1, 'name': 'buy groceries', 'about': 'milk bread eggs', 'is_completed': False},
    {'id': 2, 'name': 'study django', 'about': 'work on models and views', 'is_completed': False},
    {'id': 3, 'name': 'go to gym', 'about': 'leg day workout', 'is_completed': True},
    {'id': 4, 'name': 'read book', 'about': 'finish 20 pages of a novel', 'is_completed': False},
    {'id': 5, 'name': 'clean room', 'about': 'organize desk and vacuum floor', 'is_completed': True},
    {'id': 6, 'name': 'write blog', 'about': 'draft article about python tips', 'is_completed': False},
    {'id': 7, 'name': 'call friend', 'about': 'catch up with john', 'is_completed': False},
    {'id': 8, 'name': 'pay bills', 'about': 'electricity and internet', 'is_completed': True},
    {'id': 9, 'name': 'walk dog', 'about': 'take max to the park', 'is_completed': False},
    {'id': 10, 'name': 'cook dinner', 'about': 'prepare pasta for family', 'is_completed': False},
]

# Home page
def home(request):
    data = {'title': 'All todos', 'list': todo}
    return render(request, 'main/index.html', data)

# About page
def about(request):
    data = {'title': 'About'}
    return render(request, 'main/index.html', data)

# Edit todo
def edit(request, edit_id):
    edit_id = int(edit_id)  # convert path parameter to int

    task_index = next((i for i, t in enumerate(todo) if t['id'] == edit_id), None)
    if task_index is None:
        return redirect('home')  # if id not found, go home

    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            todo[task_index] = {'id': edit_id, **form.cleaned_data}
            return redirect('home')

    form = forms.AddForm(initial=todo[task_index])
    data = {'title': 'Edit Todo', 'form': form}
    return render(request, 'main/add.html', data)

# Add new todo
def add(request):
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            new_item = {'id': len(todo) + 1, **form.cleaned_data}
            todo.append(new_item)
            return redirect('home')

    form = forms.AddForm()
    data = {'title': 'Add Todo', 'form': form}
    return render(request, 'main/add.html', data)
