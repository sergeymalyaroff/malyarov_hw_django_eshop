#views.py

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.decorators.cache import CacheMixin
from .services import get_categories

class SomeView(View):
    def get(self, request, *args, **kwargs):
        categories = get_categories()



class CachedProductDetailView(CacheMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    cache_timeout = 60 * 15  # Кэшируется на 15 минут


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



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)