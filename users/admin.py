from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('USER', 'MODERATOR', 'ADMIN', 'ROLE', 'role', 'bio', 'email', 'username')
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(Users, UsersAdmin)
