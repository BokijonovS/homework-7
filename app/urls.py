from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all/', all_f, name='all'),
    path('get/', get_f, name='get'),
    path('filter/', filter_f, name='filter'),
    path('exclude/', exclude_f, name='exclude'),
    path('order-by/', order_by_f, name='order_by'),
    path('reverse/', reverse_f, name='reverse'),
    path('values/', values_f, name='values'),
    path('values-list/', values_list_f, name='values_list'),
    path('dates/', dates_f, name='dates'),
    path('datetimes/', datetimes_f, name='datetimes'),
    path('none/', none_f, name='none'),
    path('annotate/', annotate_f, name='annotate'),
    path('raw/', raw_f, name='raw'),
    path('count/', count_f, name='count'),
    path('latest/', latest_f, name='latest'),
    path('earliest/', earliest, name='earliest'),
    path('first/', first_f, name='first'),
    path('last/', last_f, name='last'),
    path('exists/', exists_f, name='exists'),
    path('aggregate/', aggregate_f, name='aggregate'),

]
