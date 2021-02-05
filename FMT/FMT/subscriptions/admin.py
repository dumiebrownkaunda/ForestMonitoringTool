from django.contrib import admin
from .models import SubscriptionUser
# Register your models here.


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')


admin.site.register(SubscriptionUser, SubscriptionsAdmin)
