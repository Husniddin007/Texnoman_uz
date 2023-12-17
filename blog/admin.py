from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Blog, Tag, Comment


# admin.site.register(Category)
# admin.site.register(Blog)
# admin.site.register(Tag)
# admin.site.register(Comment)


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created', 'type', 'viev']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def image_show(self, obj):
        if obj.image:
            return format_html(f"<img src='{obj.image.url}' width='50px'>")
        return None

    def blog_count(self, obj):
        return obj.blog_set.count()

    list_display = ['name', 'slug', 'image_show', 'blog_count']
    search_field = ('name',)
    readonly_field = ('slug',)


@admin.action(description='Custom delete selects tags')
def custom_delete_tags(modeladmin, request, queryset):
    queryset.update(is_deleted=True)


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'slug']



