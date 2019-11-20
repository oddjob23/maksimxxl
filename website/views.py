from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Product, Collection
from django.utils import timezone
from .forms import SubscriberFormModel, Subscriber, ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = Product
    context_object_name = 'products'
    form = SubscriberFormModel

    def post(self, request):
        form = SubscriberFormModel(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = 'Hvala sto ste se upisali na Maksim XXL newsletter'
            message = 'Hvala sto ste se upisali na nasu listu novosti'
            send_mail(subject, message, email, ['karaklajicmilos94@gmail.com'])
            form.save()

        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # add a query set or custom templates
        context['categories'] = CATEGORIES = (
            ('K', 'Kosulje'),
            ('P', 'Pantalone'),
            ('J', 'Jakne'),
            ('DZ', 'Dzemperi'),
            ('M', 'Majice'),
            ('T', 'Trenerke'),
            ('D', 'Duskevi'),
            ('A', 'Aksesoari')
        )
        context['recent_products'] = Product.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:3]
        context['popular_products'] = Product.objects.filter(
            featured=True).order_by('-published_date')[:3]
        context['products'] = Product.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:9]
        context['form'] = SubscriberFormModel
        context['collections'] = Collection.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'pages/detail.html'
    model = Product

    def post(self, request, pk):
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                name = form.cleaned_data['name']
                subject = f'New Message from {name}'
                sender = form.cleaned_data['email']
                message = form.cleaned_data['message']
                receivers = ['karaklajicmilos94@gmail.com']
                try:
                    send_mail(subject, message, from_email=sender,
                              recipient_list=receivers)
                    form.save()
                    return HttpResponseRedirect('/')
                except BadHeaderError:
                    return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORIES = (
            ('K', 'Kosulje'),
            ('P', 'Pantalone'),
            ('J', 'Jakne'),
            ('DZ', 'Dzemperi'),
            ('M', 'Majice'),
            ('T', 'Trenerke'),
            ('D', 'Duskevi'),
            ('A', 'Aksesoari')
        )
        context['recent_products'] = Product.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:3]
        context['popular_products'] = Product.objects.filter(
            featured=True).order_by('-published_date')[:3]
        context['products'] = Product.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:9]
        context['form'] = SubscriberFormModel
        context['now'] = timezone.now()
        context['contact_form'] = ContactForm
        context['collections'] = Collection.objects.all()
        return context


class CollectionView(ListView):
    template_name = 'pages/category.html'
    model = Product
    context_object_name = 'products'
    form = SubscriberFormModel

    def get_context_data(self, **kwargs):
        context = super(CollectionView, self).get_context_data(**kwargs)
        # add a query set or custom templates
        context['categories'] = CATEGORIES = (
            ('K', 'Kosulje'),
            ('P', 'Pantalone'),
            ('J', 'Jakne'),
            ('DZ', 'Dzemperi'),
            ('M', 'Majice'),
            ('T', 'Trenerke'),
            ('D', 'Duskevi'),
            ('A', 'Aksesoari')
        )
        context['recent_products'] = Product.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:3]
        context['popular_products'] = Product.objects.filter(
            featured=True).order_by('-published_date')[:3]
        collection = Collection.objects.filter(slug=self.kwargs['slug'])
        context['products_collection'] = Product.objects.all(collection=collection)
        context['form'] = SubscriberFormModel
        context['collections'] = Collection.objects.all()
        return context
