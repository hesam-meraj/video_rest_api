from django.contrib import admin

from .models import Category, Video, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'is_enable', 'file']
    extra = 0


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInlineAdmin]