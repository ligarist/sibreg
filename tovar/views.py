from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context_processors import csrf
from django.views import View
from django.template import RequestContext
from sibreg import settings
from .models import Category, Product
from .forms import ContactForm
from django.core.mail import send_mail


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'tovar/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'tovar/product/detail.html', {'product': product})


def home(request):
    return render(request, 'tovar/home.html')


def about(request):
    return render(request, 'tovar/about.html')


class Price(View):
    template_name = 'tovar/contact.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))
        context['contact_form'] = ContactForm()

        return render_to_response(template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = 'Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "Телефон отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['phone'],
                          form.cleaned_data['email'], form.cleaned_data['message'])

            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['yareg.nevsky@yandex.ru'],
                      fail_silently=False)

        return render_to_response(template_name=self.template_name, context=context)


def e_handler404(request):
    context = RequestContext(request)
    response = render_to_response('tovar/error404.html', context)
    response.status_code = 404
    return response


def e_handler500(request):
    context = RequestContext(request)
    response = render_to_response('tovar/error500.html', context)
    response.status_code = 500
    return response
