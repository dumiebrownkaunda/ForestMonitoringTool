from django import forms
from django.contrib.admin.widgets import AdminDateWidget
#from .models import Trips


RETAILERS = [('all retailers', 'Any'),
    ('Costco', 'Costco'),
    ('CVS', 'CVS'),
    ('Kroger', 'Kroger'),
    ('Publix', 'Publix'),
    ('Safeway', 'Safeway'),
    ('Target', 'Target'),
    ('Walgreens', 'Walgreens'),
    ('Walmart', 'Walmart')]

BRANDS = [('5 Hour Energy', '5 Hour Energy'),
                ('Monster', 'Monster'),
                ('Red Bull', 'Red Bull'),
                ('Rockstar', 'Rockstar')]

MONTHS = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}


class QueryForm(forms.Form):

        brand = forms.ChoiceField(choices=BRANDS,
                                    required=True,
                                    label="Brand")

        retailer = forms.ChoiceField(choices=RETAILERS,
                                    required=False,
                                    label="Retailer")

        start_date = forms.DateField(required=True,
                                    label="Start Date",
                                    widget = forms.SelectDateWidget(years=[2019],
                                                                    months=MONTHS),
                                    help_text = "Data available from January 2, 2014.")

        end_date = forms.DateField(required=True,
                                    label="Start Date",
                                    widget = forms.SelectDateWidget(years=[2019],
                                                                    months=MONTHS),
                                    help_text = "Data available to June 30, 2014.")




