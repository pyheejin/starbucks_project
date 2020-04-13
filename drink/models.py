from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'


class Size(models.Model):
    size = models.CharField(max_length=100)
    millimeter = models.IntegerField(default=0)
    fluid_ounce = models.IntegerField(default=0)

    class Meta:
        db_table = 'sizes'


class Image(models.Model):
    large_image = models.ImageField(upload_to='drink_large_image/%Y/%m/%d')
    small_image = models.ImageField(upload_to='drink_small_image/%Y/%m/%d')

    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'allergies'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    allergy = models.ManyToManyField(Allergy)
    calory = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    sodium = models.DecimalField(max_digits=5, decimal_places=2)
    sugar = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Allergy_To_Product(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_to_products'