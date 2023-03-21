from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from accounts.forms import LoginForm, CreateUser
from django.contrib.auth import authenticate, login, logout


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('home')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('home')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CreateUser
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)
