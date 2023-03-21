from django.contrib import admin
from webapp.models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created', 'updated')
    list_filter = ('id', 'summary', 'description', 'status', 'type',  'created', 'updated')
    search_fields = ('summary', 'description' 'status', 'type')
    fields = ('summary', 'description', 'status', 'type',  'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'expiration_date')
    list_filter = ('name', 'start_date', 'expiration_date')
    search_fields = ('name', 'start_date', 'expiration_date', 'users')
    fields = ('name', 'description', 'start_date', 'expiration_date')
    readonly_fields = ('id',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)