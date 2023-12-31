from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .forms import ProductForm
from django.views.generic.edit import DeleteView
from .models import Product

#Контроллер для домашней страницы


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'



#Контроллер для страницы с контактной информацией
class ContactView(TemplateView):
    template_name = 'contact.html'



# Отображение страницы товара:


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# Вывод списка товаров



class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 10



#представление для добавления продукта и постраничный вывод



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/products/'  # URL для перехода после успешного создания объекта


# Редактирование товара



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = '/products/'  # URL для перехода после успешного редактирования объекта

# удаление товара



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'confirm_delete.html'
    success_url = '/products/'  # URL для перехода после успешного удаления объекта




def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  # 10 продуктов на страницу
    page = request.GET.get('page')
    products_on_page = paginator.get_page(page)
    return render(request, 'product_list.html', {'products': products_on_page})


# Вывод блога




class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.filter(is_published=True).order_by('-created_date')[:5]  # например, 5 последних записей
        return context




# #Контроллер для страницы с контактной информацией
# def contact(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Сообщение для пользователя
#             return redirect('contact')
#
#             # Вывод данных в консоль
#             print(f"Имя: {name}")
#             print(f"Email: {email}")
#             print(f"Сообщение: {message}")
#     else:
#
#         form = FeedbackForm()
#
#     return render(request, 'contact.html', {'form': form})