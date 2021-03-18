from django.db import models
from accounts_app.models import AuthUserModel



class CategoryProductModel(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Слаг категории')
    res1 = models.CharField(max_length=5, blank=True, null=True)
    res2 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'



class ProductModel(models.Model):
    category = models.ForeignKey(CategoryProductModel, on_delete=models.PROTECT, verbose_name='Категория')
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    product_slug = models.SlugField(max_length=100, unique=True)
    product_image = models.ImageField(upload_to='products/%Y/%m')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_description = models.TextField(max_length=10000, blank=True, null=True)
    product_available = models.BooleanField(default=False)
    product_date = models.DateField(auto_now=True)
    res1 = models.CharField(max_length=5, blank=True, null=True)
    res2 = models.CharField(max_length=5, blank=True, null=True)
    res3 = models.CharField(max_length=5, blank=True, null=True)
    res4 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']

    def __str__(self):
        return f'{self.product_name}'

class CartProductModel(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    res1 = models.CharField(max_length=5, blank=True, null=True)
    res2 = models.CharField(max_length=5, blank=True, null=True)
    res3 = models.CharField(max_length=5, blank=True, null=True)
    res4 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Корзина продуктов'
        verbose_name_plural = 'Корзины продуктов'
        ordering = ['product']

    def __str__(self):
        return f'{self.user} : {self.product}'
























































































