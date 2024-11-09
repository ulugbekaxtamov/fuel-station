from django.contrib import admin
from .models import OneIDProfile


@admin.register(OneIDProfile)
class OneIDProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'full_name', 'birth_date', 'tin', 'email', 'mob_phone_no',
        'user_type', 'valid', 'access_token_expire_date'
    )
    search_fields = ('user__username', 'full_name', 'tin', 'email', 'mob_phone_no')
    list_filter = ('valid', 'user_type', 'birth_date')
    readonly_fields = ('access_token', 'refresh_token', 'access_token_expire_date')
