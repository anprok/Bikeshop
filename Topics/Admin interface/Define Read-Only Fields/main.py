from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    fields = ('writer', 'director')
    readonly_fields = ('writer', 'director')