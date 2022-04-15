from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'get_image']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return  mark_safe(f'<img src={obj.photo.url} width="50" height="60"')
    get_image.short_description = "Изображение"
