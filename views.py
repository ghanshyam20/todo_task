from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos},
    )


def todo_create(request):

    if request.method == "POST":
        name = request.POST["name"]
        Todo.objects.create(name=name)
        return HttpResponseRedirect("/")

    return render(request, "bootstrap/todo_create.html")


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_update(request, pk):
    if request.method == "POST":
        name = request.POST["name"]
        todo = Todo.objects.get(pk=pk)
        todo.name = name
        todo.save()
        return HttpResponseRedirect("/")
    else:
        todo = Todo.objects.get(pk=pk)

        return render(request, "bootstrap/todo_update.html", {"todo": todo})
