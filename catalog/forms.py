from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    # Список запрещенных слов
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'  # Все поля модели

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS-классы для стилизации
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # Особое оформление для булевых полей
        if 'is_active' in self.fields:
            self.fields['is_active'].widget.attrs['class'] = 'form-check-input'

    def clean_name(self):
        """Проверка названия на запрещенные слова"""
        name = self.cleaned_data['name'].lower()
        for word in self.FORBIDDEN_WORDS:
            if word in name:
                raise ValidationError(f'Название содержит запрещенное слово: "{word}"')
        return name

    def clean_description(self):
        """Проверка описания на запрещенные слова"""
        description = self.cleaned_data['description'].lower()
        for word in self.FORBIDDEN_WORDS:
            if word in description:
                raise ValidationError(f'Описание содержит запрещенное слово: "{word}"')
        return description

    def clean_price(self):
        """Проверка что цена не отрицательная"""
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        """Валидация изображения (дополнительное задание)"""
        image = self.cleaned_data.get('image')
        if image:
            # Проверка формата (JPEG/PNG)
            allowed_types = ['image/jpeg', 'image/png']
            if image.content_type not in allowed_types:
                raise ValidationError('Допустимые форматы: JPEG и PNG')
            # Проверка размера (5 МБ)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Максимальный размер файла — 5 МБ')
        return image

