from django.http import HttpResponse
from django.views import generic

# Create your views here.
from users.forms import RegisterForm, LoginForm


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data=data)

        if form.is_valid():
            form.save()
            return HttpResponse('Yes you successfully registered!')
        else:
            return HttpResponse(f'Form is not valid! </br>{form.errors}')


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data=data)

        if form.is_valid():
            login = form.authenticate_user()
            if login:
                return HttpResponse(f'Yes you successfully loggined {login}!')
            else:
                return HttpResponse('No such user!')
        else:
            return HttpResponse(f'Form is not valid! </br>{form.errors}')
