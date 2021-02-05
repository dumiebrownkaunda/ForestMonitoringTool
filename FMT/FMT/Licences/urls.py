from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^Licences', views.licences),
    url(r'^Licences/', {'template_name': 'Licences/licences.html'})
}
