from django.urls import path
from webapp.views.template_views import IndexViews, \
    DetailView, UpdateViews, \
    CreateTask, DeleteViews, \
    IndexProjects, CreateProject, DetailProject, DeleteProject, UpdateProject
from webapp.views.users import CreateUser

urlpatterns = [
    path('users/<int:pk>', CreateUser.as_view(), name='add_user'),
    path('', IndexProjects.as_view(), name='home'),
    path('projects/add_project', CreateProject.as_view(), name='create_project'),
    path('projects/detail/<int:pk>', DetailProject.as_view(), name='detail_project'),
    path('project/delete/<int:pk>', DeleteProject.as_view(), name='delete_project'),
    path('project/update/<int:pk>', UpdateProject.as_view(), name='update_project'),
    path('projects/tasks', IndexViews.as_view(), name='tasks'),
    path('projects/tasks/detail/<int:pk>', DetailView.as_view(), name='detail_task'),
    path('projects/tasks/update/<int:pk>', UpdateViews.as_view(), name='update_task'),
    path('projects/<int:pk>/create_task', CreateTask.as_view(), name='create_task'),
    path('projects/tasks/delete/<int:pk>', DeleteViews.as_view(), name='delete_task')
]
