from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        latest_products = Product.objects.order_by('-created_at')[:5]
        for product in latest_products:
            self.stdout.write(f"{product.name} - {product.price} руб.")