from django.shortcuts import render

from .models import Product, Category
from django.db.models import Count

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def all_f(request):
    products = Product.objects.all()
    return render(request, 'app/index.html', {'products': products, 'title': 'all'})


def get_f(request):
    product = Product.objects.get(pk=1)
    return render(request, 'app/index.html', {'product': product, 'title': 'get'})


def filter_f(request):
    products = Product.objects.filter(category_id=2)
    return render(request, 'app/index.html', {'products': products, 'title': 'filter'})


def exclude_f(request):
    products = Product.objects.exclude(id=2)
    return render(request, 'app/index.html', {'products': products, 'title': 'exclude'})


def order_by_f(request):
    products = Product.objects.order_by('name')
    return render(request, 'app/index.html', {'products': products, 'title': 'order_by'})


def reverse_f(request):
    # products = Product.objects.all().reverse()
    # ushbu holatda ishlamadi
    products = list(Product.objects.all())[::-1]
    return render(request, 'app/index.html', {'products': products, 'title': 'reverse'})


def values_f(request):
    products = Product.objects.values('name')
    return render(request, 'app/index.html', {'products': products, 'title': 'values'})


def values_list_f(request):
    products = Product.objects.values_list('name')
    return render(request, 'app/index.html', {'products': products, 'title': 'values_list'})


def dates_f(request):
    products = Product.objects.dates('created', 'day')
    return render(request, 'app/index.html', {'products': products, 'title': 'dates'})


def datetimes_f(request):
    products = Product.objects.datetimes('created', 'second')
    return render(request, 'app/index.html', {'products': products, 'title': 'datetimes'})


def none_f(request):
    products = Product.objects.none()
    return render(request, 'app/index.html', {'products': products, 'title': 'none'})


def annotate_f(request):
    products = Category.objects.annotate(Count('product'))
    # bu yerda products emas categories deb yozilishi kerak edi lekin
    # mening holatimda hammasini products degan ozgaruvchidan for sikli yordamida olyapman
    # shuning uchun loyiha ishlashi maqsadida products deb nomlab qoydim
    # lekin u kategoriyalarni qaytaradi
    return render(request, 'app/index.html', {'products': products, 'title': 'annotate'})


def raw_f(request):
    products = Product.objects.raw("SELECT * FROM app_product where id = 2")
    return render(request, 'app/index.html', {'products': products, 'title': 'raw'})


def count_f(request):
    product = Product.objects.count()
    return render(request, 'app/index.html', {'product': product, 'title': 'count'})


def latest_f(request):
    product = Product.objects.latest('created')
    return render(request, 'app/index.html', {'product': product, 'title': 'latest'})


def earliest(request):
    product = Product.objects.earliest('created')
    return render(request, 'app/index.html', {'product': product, 'title': 'earliest'})


def first_f(request):
    product = Product.objects.first()
    return render(request, 'app/index.html', {'product': product, 'title': 'first'})


def last_f(request):
    product = Product.objects.last()
    return render(request, 'app/index.html', {'product': product, 'title': 'last'})


def exists_f(request):
    product = Product.objects.exists()
    return render(request, 'app/index.html', {'product': product, 'title': 'exists'})


def aggregate_f(request):
    product = Category.objects.aggregate(Count('product'))
    return render(request, 'app/index.html', {'product': product, 'title': 'aggregate'})

