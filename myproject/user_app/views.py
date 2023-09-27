# views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Product

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'


from django.views.generic.edit import CreateView
from .models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)