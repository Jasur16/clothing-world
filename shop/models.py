from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models, IntegrityError
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import UserModel


class BarCategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    title = models.CharField(max_length=100, verbose_name=_('title'), null=True)
    image = models.ImageField(upload_to='bar_categories', verbose_name=_('image'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'bar_category'
        verbose_name_plural = 'bar_categories'


class ProductDetailImageModel(models.Model):
    title = models.CharField(null=True, max_length=255, verbose_name=_('title'))
    image_1 = models.ImageField(null=True, upload_to='detail_image', verbose_name=_('image_1'))
    image_2 = models.ImageField(null=True, upload_to='detail_image', verbose_name=_('image_2'))
    image_3 = models.ImageField(null=True, upload_to='detail_image', verbose_name=_('image_3'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'detail_image'
        verbose_name_plural = 'detail_images'


class CategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class SizeModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'), null=True)
    code = models.CharField(max_length=60, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    short_description = models.CharField(max_length=255, verbose_name=_('short description'))
    long_description = RichTextUploadingField(verbose_name=_('long description'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    main_image = models.ImageField(upload_to='products', verbose_name=_('main image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    detail_images = models.ForeignKey(
        ProductDetailImageModel,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('detail images'),
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('category')
    )
    tags = models.ManyToManyField(
        ProductTagModel,
        related_name='products',
        verbose_name=_('tags')
    )
    bar_category = models.ForeignKey(
        BarCategoryModel,
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('bar_categories'),
        null=True
    )
    sizes = models.ManyToManyField(
        SizeModel,
        related_name='products',
        verbose_name=_('sizes')
    )
    colors = models.ManyToManyField(
        ColorModel,
        related_name='products',
        verbose_name=_('colors')
    )
    sku = models.CharField(max_length=50, unique=True, verbose_name=_('sku'))

    def new(self):
        return (timezone.now() - self.created_at).days <= 5

    @staticmethod
    def get_cart_info(request):
        cart = request.session.get('cart', [])
        if not cart:
            return 0, 0.0
        return len(cart), ProductModel.objects.filter(id__in=cart).aggregate(Sum('real_price'))['real_price__sum']

    @staticmethod
    def get_cart_objects(request):
        cart = request.session.get('cart', [])
        if not cart:
            return None
        return ProductModel.objects.filter(id__in=cart)

    def is_discount(self):
        return bool(self.discount)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wishlists', verbose_name=_('user'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_('product'))

    @staticmethod
    def create_or_delete(user, product):
        try:
            return WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            return WishlistModel.objects.get(user=user, product=product).delete()

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.product.title}"

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'product'


class ShopHistoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='history')
    products = models.ManyToManyField(ProductModel)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'history'
        verbose_name_plural = 'histories'
