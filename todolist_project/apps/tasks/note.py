# python manage.py test apps.tasks.uni_test.TaskListSecurityTest.test_task_list_sql_injection_in_title -v 2
def task_list(request):
  
    status = request.GET.get('status')
    title = request.GET.get('title')
    tasks = Task.objects.filter(owner=request.user)
    
    if status == 'done':
        tasks = tasks.filter(is_done=True)
    elif status == 'pending':
        tasks = tasks.filter(is_done=False)

    if title:
        tasks = tasks.filter(title__icontains=title)

    return render(request, 'tasks/list.html', {'tasks': tasks})



#python manage.py test apps.tasks.uni_test.DeleteTaskSecurityTest.test_usuario_intruso_nao_deleta_task_de_outro -v 2
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")


    return render(request, "tasks/delete.html", {"task": task})