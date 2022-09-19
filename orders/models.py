from django.db import models
from user.models import UserModel
from shop.models import ProductModel


class OrderHistoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='history')
    products = models.ManyToManyField(ProductModel)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    address = models.TextField()
    gmail = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'history'
        verbose_name_plural = 'histories'
