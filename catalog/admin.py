from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}  # Теперь поле slug есть в модели

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'in_stock')  # Теперь поле in_stock есть
    list_filter = ('category',)
    list_editable = ('price', 'in_stock')  # Корректные поля для редактирования
    search_fields = ('name', 'description')

