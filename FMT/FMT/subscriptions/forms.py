from django import forms

from .models import SubscriptionUser


class SubscriptionUserSignUpForm(forms.ModelForm):
    class Meta:
        model = SubscriptionUser
        fields = ['email']

        def clean_email(self):
            email = self.clean_data.get('email')

            return email
