from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Добро пожаловать!',
            'Вы успешно зарегистрировались в нашем магазине.',
            'from@example.com',
            [self.object.email],
            fail_silently=False,
        )
        return response

