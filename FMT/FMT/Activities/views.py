from django.shortcuts import render
#from .models import Trips
from django.db.models import Avg, Count, Max, Min, Sum
from django.http import JsonResponse
from django.views.generic import View
from .forms import QueryForm
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def activities(request):
        '''Renders a search form if receiving a GET request, or renders a results
        page if receiving a POST request. Uses form data and data captured from
        calls to helper functions in order to send dynamic data to the template.'''

        if request.method == 'POST':
            query_form = QueryForm(request.POST)

            if query_form.is_valid():
                clean_query = query_form.cleaned_data

                brand = clean_query['brand']
                retailer = clean_query['retailer']
                start_date = clean_query['start_date']
                end_date = clean_query['end_date']

                # Call helper functions to obtain values to pass to template
                global start_date_str
                start_date_str = helper_start_date(start_date)

                global end_date_str
                end_date_str = helper_end_date(end_date)

                min_date_str = helper_min_date()
                max_date_str = helper_max_date()
                total_hhs = helper_total_hhs(min_date_str, max_date_str)
                count_hhs_for_query = count_hhs(brand, start_date_str, end_date_str, retailer)
                brand_list = helper_get_brands(start_date_str, end_date_str)
                avg_brand_spend_hh = top_buying_brand(brand_list, start_date_str, end_date_str)
                sorted_brand_list = sorted(avg_brand_spend_hh.keys())

                sorted_avg_spend = []
                for item in sorted_brand_list:
                    sorted_avg_spend.append(avg_brand_spend_hh[item][0])

                return render(request, 'Activities/results.html', {'brand': brand,
                                                                    'retailer': retailer,
                                                                    'start_date': start_date_str,
                                                                    'end_date': end_date_str,
                                                                    'min_date': min_date_str,
                                                                    'max_date': max_date_str,
                                                                    'total_hhs': total_hhs,
                                                                    'count_hhs': count_hhs_for_query,
                                                                    'brand_list': brand_list,
                                                                    'avg_brand_spend_hh': avg_brand_spend_hh,
                                                                    'sorted_brand_list': sorted_brand_list,
                                                                    'sorted_avg_spend': sorted_avg_spend})

        else:
            query_form = QueryForm()
            return render(request, 'Activities/activities.html', {'query_form': query_form})


def results(request):
    return render(request, 'Activities/results.html')


class BarChartData(APIView):

        authentication_classes = []
        permission_classes = []

        def get(self, request, format=None):
            '''Creates a list of brands sorted alphabetically. Makes use of the
            global variables start_date_str and end_date_str as defined in the
            home view. Creates a list of average spend per household for each brand
            during a time range, sorted to match the brand order in sorted_brand_list.'''

            all_brands_qs = Trips.objects.filter(date__gte=start_date_str,
                                            date__lte=end_date_str).values('brand').distinct()
            brand_list = []

            for brand in all_brands_qs:
                brand_list.append(brand['brand'])

            sorted_brand_list = sorted(brand_list)

            # Create a list of average spending per household that is sorted to match
            # the order the brands appear in sorted_brand_list
            avg_brand_spend_hh = top_buying_brand(sorted_brand_list, start_date_str, end_date_str)

            sorted_avg_spend = []
            for brand in sorted_brand_list:
                sorted_avg_spend.append(avg_brand_spend_hh[brand][0])
            print(sorted_avg_spend)

            data = {'sorted_brands': sorted_brand_list,
                    'sorted_avg_spend': sorted_avg_spend}
            return Response(data)


    # Send JSON data to Chart.js via a REST API call
class PieChartData(APIView):

        authentication_classes = []
        permission_classes = []

        def get(self, request, format=None):
            '''Creates a list of brands sorted alphabetically. Makes use of the
            global variables start_date_str and end_date_str as defined in the
            home view. Creates a list of items representing the number of households
            that purchased each brand. The list is sorted to match the order the
            brands appearing in sorted_brand_list.'''

            all_brands_qs = Trips.objects.filter(date__gte=start_date_str,
                                            date__lte=end_date_str).values('brand').distinct()
            brand_list = []

            for brand in all_brands_qs:
                brand_list.append(brand['brand'])

            sorted_brand_list = sorted(brand_list)

            # Create a list of items representing the number of households that purchased
            # each brand. The list is sorted to match the order the brands appearing in sorted_brand_list

            sorted_hhs_by_brand = []

            for brand in sorted_brand_list:
                temp_hhs_by_brand = Trips.objects.filter(date__gte=start_date_str,
                                    date__lte=end_date_str, brand=brand).values('user_id').distinct().count()
                print("Temp_hhs_by_brand: ", temp_hhs_by_brand)
                sorted_hhs_by_brand.append(temp_hhs_by_brand)
            print("Sorted hhs by brand: ", sorted_hhs_by_brand)

            data = {'sorted_brands': sorted_brand_list,
                    'sorted_hhs_by_brand': sorted_hhs_by_brand}

            return Response(data)

    # ------------ BEGIN HELPER FUNCTIONS ------------ #

def helper_start_date(start_date):
        '''Takes in a datetime object, which may either be typecast from a user-supplied
        date string or the earliest date found in the data table. Returns the date as a string.'''

        if not start_date:
            start_date_obj = Trips.objects.all().aggregate(Min('date'))
            start_date = start_date_obj['date__min']
        else:
            start_date = start_date

        return(start_date)


def helper_end_date(end_date):
        '''Takes in a datetime object, which may either be typecast from a user-supplied
        date string or the latest date found in the data table. Returns the date as a string.'''

        if not end_date:
            end_date_obj = Trips.objects.all().aggregate(Max('date'))
            end_date = end_date_obj['date__max']
        else:
            end_date = end_date

        return(end_date)


def helper_min_date():
        '''Does not require an input. Returns the earliest date in the data table.'''

        min_date_obj = Trips.objects.all().aggregate(Min('date'))
        min_date_str = min_date_obj['date__min']

        return(min_date_str)


def helper_max_date():
        '''Does not require an input. Returns the latest date in the data table.'''

        max_date_obj = Trips.objects.all().aggregate(Max('date'))
        max_date_str = max_date_obj['date__max']

        return(max_date_str)


def helper_total_hhs(min_date, max_date):
        '''Takes in the earliest and latest dates found in the data table.
        Returns the count of distinct households that shopped during that period.'''

        total_hhs = Trips.objects.values('user_id').distinct().count()
        total_hhs = "{:,}".format(total_hhs)
        return(total_hhs)


def helper_get_brands(start_date, end_date):
        '''Takes in a start date and an end date. If dates are not
        supplied by the user, the earliest and latest dates in the
        table are used. Returns a list of brands purchased within
        the dates specified.'''

        all_brands_qs = Trips.objects.filter(date__gte=start_date,
                                            date__lte=end_date).values('brand').distinct()
        brand_list = []

        for brand in all_brands_qs:
            brand_list.append(brand['brand'])

        return(brand_list)

    # ------------ END HELPER FUNCTIONS ------------ #

    # ------------ BEGIN CALCULATION FUNCTIONS ------------ #


def count_hhs(brand, start_date, end_date, retailer):
        '''Takes in a brand (selected by user), start and end dates (selected by user,
        or the largest available timeframe by default), and a retailer (user specifies
        one or all). Returns the number of households that purchased that brand within
        the timeframe given at the specified retailer(s).'''

        if retailer == 'all retailers':
            count_hhs = Trips.objects.filter(brand=brand, date__gte=start_date,
                                            date__lte=end_date).values('user_id').distinct().count()
            count_hhs = "{:,}".format(count_hhs)
            return(count_hhs)
        else:
            count_hhs = Trips.objects.filter(brand=brand,
                                            date__gte=start_date,
                                            date__lte=end_date,
                                            retailer=retailer).values('user_id').distinct().count()
            count_hhs = "{:,}".format(count_hhs)
            return(count_hhs)


def top_buying_brand(brands, start_date, end_date):
        '''Takes in a list of all brands in the data table,
        and start and end dates. Dates are selected by the user,
        or the largest available timeframe is used by default.
        Returns the average dollars spent per household on each
        brand within the timeframe given.'''

        avg_spend_hh_by_brand = {}

        for brand in brands:

            sum_item_spend = Trips.objects.values('brand').filter(date__gte=start_date, date__lte=end_date, brand=brand).annotate(total_spent=Sum('item_spend'))

            sum_hhs = Trips.objects.filter(brand=brand, date__gte=start_date,   date__lte=end_date).values('user_id').distinct().count()

            avg_spend_hh = round((sum_item_spend[0]['total_spent'] / sum_hhs), 2)

            avg_spend_hh_by_brand[brand] = [avg_spend_hh,
                                            "{:,}".format(sum_item_spend[0]['total_spent']),
                                            "{:,}".format(sum_hhs)]

        print(avg_spend_hh_by_brand)

        return (avg_spend_hh_by_brand)

# ------------ END CALCULATION FUNCTIONS ------------ #

