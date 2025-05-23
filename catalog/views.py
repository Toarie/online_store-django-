from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'catalog/home.html'

class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')
        return render(request, self.template_name)

