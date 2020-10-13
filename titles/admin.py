from django.contrib import admin

from .models import Categories, Genres, Titles


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class GenresAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category', 'genre', 'rating')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Titles, TitlesAdmin)
