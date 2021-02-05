from django.conf.urls import url
from .views import subscription_signup, subscription_unsubscribe


urlpatterns = [
    url(r'sign_up/$', subscription_signup, name="subscription_sign_up"),
    url(r'unsubscribe/$', subscription_unsubscribe,  name="subscription_unsubscribe"),

]
