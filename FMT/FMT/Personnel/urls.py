from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

)
# from FMT.subscriptions.views import subscription_signup, subscription_unsubscribe
from . import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    # url(r'^api/barchart/data$', views.BarChartData.as_view()),
    # url(r'^api/piechart/data$', views.PieChartData.as_view()),
    # url(r'^results$', views.results, {'template_name': 'Personnel/results.html'}, name='results'),
    # url(r'^sign_up/$', subscription_signup, name="subscription_sign_up"),
    # url(r'^unsubscribe/$', subscription_unsubscribe,  name="subscription_unsubscribe"),
    # url(r'^subscribe/$', views.subscribe, name='subscribe'),
    # url(r'^subscribe/confirm/$', views.subscribe_confirmation, name='subscribe_confirmation'),
    # url(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
    url(r'^imagery_data/$', login, {'template_name': 'Personnel/imagery_data.html'}, name='imagery_data'),
    url(r'^login/$', login, {'template_name': 'Personnel/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'Personnel/logout.html'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^view_map/$', views.view_map, name='view_map'),
    url(r'^Activities/$', views.activities_stat, name='activities_stat'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^reset-password/$', password_reset, {'template_name':
        'Personnel/reset_password.html', 'post_reset_redirect': 'Personnel:password_reset_done', 'email_template_name': 'Personnel/reset_password_email.html'},
        name="reset_password"),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'Personnel/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'Personnel/reset_password_confirm.html', 'post_reset_redirect': 'Personnel:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'Personnel/reset_password_complete.html'}, name="password_reset_complete"),

]
