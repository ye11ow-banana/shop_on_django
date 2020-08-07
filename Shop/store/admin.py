from django.contrib import admin
from .models import Department, Color, Product, Gallery, Reviews, News, Advert, Coupon
from django.utils.safestring import mark_safe


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="110"')

    get_image.short_description = "Image"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("name", "quantity", "price", "get_image", "draft")
    list_filter = ("department",)
    search_fields = ("name", "department__name")
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ['publish', 'unpublish']
    inlines = [GalleryInline,]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="70"')

    get_image.short_description = "Image"

    def unpublish(self, request, queryset):
        'Снять с публикации'
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 entry has been updated'
        else:
            message_bit = f'{row_update} entries have been updated'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        'Опубликовать'
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 entry has been updated'
        else:
            message_bit = f'{row_update} entries have been updated'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Unpublish'
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "sale", "id")
    readonly_fields = ("name", "sale")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("email",)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("title", "text", "id")
    readonly_fields = ("title", "text")


admin.site.register(Color)

admin.site.site_title = 'Store'
admin.site.site_header = 'Store'




    
