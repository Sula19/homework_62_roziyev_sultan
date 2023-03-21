from django.utils.http import urlencode
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from webapp.forms import TasksForm, ProjectForm, SearchView
from webapp.models import Task, Project
from django.shortcuts import get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['manager', 'lead']).exists()


class DeleteProject(GroupPermissionMixin, DeleteView):
    template_name = 'projects/delete_project.html'
    context_object_name = 'project'
    model = Project
    success_url = '/'
    groups = ['manager']


class CreateProject(GroupPermissionMixin, CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectForm
    success_url = '/'
    permission_required = 'webapp.change_project'
    groups = ['manager']


class UpdateProject(GroupPermissionMixin, UpdateView):
    template_name = 'projects/update_project.html'
    model = Project
    form_class = ProjectForm
    success_url = '/'
    groups = ['manager']

    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)


class DetailProject(DetailView):
    template_name = 'projects/detail_project.html'
    model = Project


class IndexProjects(ListView):
    template_name = 'projects/home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.exclude(is_deleted=True)


class IndexViews(ListView):
    template_name = 'tasks/index_tasks.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('-created',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchView(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class CreateTask(UserPassesTestMixin, CreateView):
    template_name = 'tasks/create_task.html'
    model = Task
    form_class = TasksForm
    permission_denied_message = 'No'


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('/')

    def test_func(self):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        for user in project.users.all():
            return user == self.request.user and self.request.user.has_perm('webapp.change_tasks')


class DetailView(TemplateView):
    template_name = 'tasks/detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class UpdateViews(UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    form_class = TasksForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class DeleteViews(GroupPermissionMixin, DeleteView):
    template_name = 'tasks/delete_task.html'
    model = Task
    context_object_name = 'task'
    success_url = '/'
    groups = ['manager', 'lead']
