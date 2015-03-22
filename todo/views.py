import json
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from todo.forms import TaskForm
from todo.models import Task
from django.views.generic import FormView
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TaskView(FormView):
    form_class = TaskForm
    model = Task
    template_name = 'list.html'
    success_url = '/todo/list'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return HttpResponse(json.dumps({'text': form.instance.text,
                                        'done': form.instance.done,
                                        'id': form.instance.id}),
                            content_type="application/json")

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = self.model.objects.filter(created_by=self.request.user).order_by('created_at')
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskView, self).dispatch(*args, **kwargs)


@require_http_methods(["POST"])
def change_task_status(request):
    task = Task.objects.get(id=int(request.POST['id']))
    if task:
        task.done = not task.done
    task.save()
    return HttpResponse(json.dumps({'done': task.done,
                                    'id': task.id}),
                        content_type="application/json")


def login_view(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/todo/list')
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('/todo/login')
