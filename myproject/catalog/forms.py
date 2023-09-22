from django import forms
from .models import Product
from crispy_forms.helper import FormHelper

#формы теперь могут использовать crispy для отображения
class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']  # и другие необходимые поля

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]

        for word in forbidden_words:
            if word in title or word in description:
                raise forms.ValidationError(f"Запрещено использовать слово: {word}")