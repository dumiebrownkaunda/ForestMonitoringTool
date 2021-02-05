from django.contrib import admin
from .models import user, Activity
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth


class userAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'description', 'position', 'website', 'licence', 'location')
    list_filter = ('firstname', 'lastname')
    list_per_page = 5


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id',  'contractor', 'date', 'name', 'type')
    list_filter = ('name', 'type')
    list_per_page = 5


admin.site.register(Activity, ActivityAdmin)
admin.site.register(user)
admin.site.index_title = "Forest Monitoring Tool Admin Panel"
admin.site.site_url = "/Personnel"
admin.site.unregister(auth.models.Group)
