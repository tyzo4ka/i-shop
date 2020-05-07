from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_name = models.CharField(max_length=50, verbose_name='Подраздел')
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.PROTECT,
                                 verbose_name='Категория')

    def __str__(self):
        return self.sub_name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT,
                                verbose_name='Категория')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
