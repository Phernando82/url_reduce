from django.contrib import admin

# Register your models here.
from url_reduce.reducer.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino','slug','criado_em','atualizado_em')

