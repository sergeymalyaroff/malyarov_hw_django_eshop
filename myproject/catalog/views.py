from django.shortcuts import render, redirect



#Контроллер для домашней страницы
def home(request):
    return render(request, 'home.html')

#Контроллер для страницы с контактной информацией
def contact(request):
    return render(request, 'contact.html')


# Отображение страницы товара:

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

# Вывод списка товаров

from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


#
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