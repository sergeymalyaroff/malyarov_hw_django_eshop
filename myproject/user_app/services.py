# services.py
from django.core.cache import cache

from .models import Category

def get_categories():
    categories = cache.get('categories')

    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories, 60 * 15)  # кешируем на 15 минут

    return categories
