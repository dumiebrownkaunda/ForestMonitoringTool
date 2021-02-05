from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Activity


CONTRACTORS = [('all contractors', 'Any'),
    ('Raiply', 'Raiply'),
    ('Chikangawa', 'Chikangawa')]

TYPES = [('Select', 'Select'),
                ('Standard', 'Standard'),
                ('Premium', 'Premium')]

MONTHS = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}


class QueryForm(forms.Form):

        type = forms.ChoiceField(choices=TYPES,
                                    required=True,
                                    label="Brand")

        contractor = forms.ChoiceField(choices=CONTRACTORS,
                                    required=False,
                                    label="Retailer")

        start_date = forms.DateField(required=True,
                                    label="Start Date",
                                    widget = forms.SelectDateWidget(years=[2019],
                                                                    months=MONTHS),
                                    help_text = "Data available from January 2, 2019.")

        end_date = forms.DateField(required=True,
                                    label="Start Date",
                                    widget = forms.SelectDateWidget(years=[2019],
                                                                    months=MONTHS),
                                    help_text = "Data available to February 20, 2019.")




