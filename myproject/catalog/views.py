from django.shortcuts import render, redirect



#Контроллер для домашней страницы
def home(request):
    return render(request, 'home.html')

#Контроллер для страницы с контактной информацией
def contact(request):
    return render(request, 'contact.html')
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