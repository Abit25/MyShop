from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=25)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolue_url(self):
        return reverse('shop:products_list',args=[self.slug])


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    descp=models.TextField()
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolue_url(self):
        return render('shop:product_detail',args=[self.id,self.slug])
