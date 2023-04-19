from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('PN', 'Paneer'),
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)



class Products(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField( upload_to='images' )
    
    
    def __str__(self):
        return self.title
    