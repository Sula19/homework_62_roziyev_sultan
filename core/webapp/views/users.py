from django.contrib.auth.models import User
from django.views.generic import FormView, DeleteView
from webapp.models import Project
from django.shortcuts import reverse, redirect
from webapp.forms import UserProjectForm
from webapp.views.template_views import GroupPermissionMixin


class CreateUser(GroupPermissionMixin, FormView):
    template_name = 'add_user.html'
    model = Project
    form_class = UserProjectForm
    groups = ['manager', 'lead']

    def post(self, request, *args, **kwargs):
        form = UserProjectForm(request.POST)
        project = Project.objects.get(pk=kwargs.get('pk'))
        if form.is_valid():
            user = User.objects.get(pk=form.cleaned_data.get('users').pk)
            project.users.add(user)
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.kwargs.get('pk')})


class DeleteUser(GroupPermissionMixin, DeleteView):
    model = User
    success_url = '/'
    groups = ['manager', 'lead']

    #Сделал удаление вообще из базы
    def get(self, request, *args, **kwargs):
        project = Project.objects.all()
        user = User.objects.get(pk=kwargs.get('pk'))
        for p in project:
            p.users.remove(user)
        return redirect('/')
