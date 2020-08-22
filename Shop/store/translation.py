from modeltranslation.translator import register, TranslationOptions
from .models import Department, Color, Product, Reviews, Advert, Coupon


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
	fields = ('name',)


@register(Color)
class ColorTranslationOptions(TranslationOptions):
	fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
	fields = ('name', 'description')


@register(Advert)
class AdvertTranslationOptions(TranslationOptions):
	fields = ('title', 'text')


@register(Coupon)
class CouponTranslationOptions(TranslationOptions):
	fields = ('name',)