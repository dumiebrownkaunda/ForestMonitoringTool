from django.contrib import admin
from .models import Licences


# Register your models here.
class LicencesAdmin(admin.ModelAdmin):

    list_display = ('name', 'Type', 'licence_number', 'issued_date', 'expiry_date', 'status')
    list_filter = ('issued_date', 'expiry_date')
    search_fields = ('Type', 'name')
    list_per_page = 10
    sortable_by = 'expiry_date'


    #def user_info(self, obj):
        #return obj.description

    #def get_queryset(self, request):
        #queryset = super(LicencesAdmin, self).get_queryset(request)
        #queryset = queryset.order_by('issued_date', 'expiry_date')
        #return queryset

    #user_info.short_description = 'Information'


admin.site.register(Licences, LicencesAdmin)
