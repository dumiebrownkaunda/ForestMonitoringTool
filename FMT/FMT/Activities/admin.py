from django.contrib import admin
from .models import Activities
#from .models import Trips


def make_finished(self, request, queryset):
    rows_updated = queryset.update(status='f')
    make_finished.short_description = "Mark selected field as finished"

    if rows_updated == 1:
        message_bit = "1 activity was"
    else:
        message_bit = "%s activities were" % rows_updated
    self.message_user(request, "%s successfully marked as finished." % message_bit)


def make_in_progress(self, request, queryset):
    rows_updated = queryset.update(status='p')
    make_in_progress.short_description = "Mark selected field as in_progress"

    if rows_updated == 1:
        message_bit = "1 activity was"
    else:
        message_bit = "%s activities were" % rows_updated
    self.message_user(request, "%s successfully marked as in_progress." % message_bit)


class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description', 'date_started', 'closing_date')
    list_filter = ('date_started', 'closing_date', 'name')
    search_fields = ('status', 'name', 'closing_date')
    ordering = ['name']
    actions = [make_finished, make_in_progress]
    list_per_page = 10


#class TripsAdmin(admin.ModelAdmin):
    #list_display = ('id', 'user_id', 'trip_id', 'date', 'retailer', 'brand', 'item_spend', 'item_units')


#admin.site.register(Trips, TripsAdmin)
admin.site.register(Activities, ActivitiesAdmin)

