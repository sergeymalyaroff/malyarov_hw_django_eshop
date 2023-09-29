# context_processors.py
from .services import get_categories

def categories_processor(request):
    categories = get_categories()
    return {'categories': categories}
