from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from apps.market.models import Product, Categoriy
from apps.users.models import Author, AuthorLike, AuthorCardMarket
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateProductForm, CardForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

class HomePageView(View):
    def get(self, request):
        context = {}
        products = Product.objects.all()
        categroies = Categoriy.objects.all()

        context['products'] = products
        context['categories'] = categroies
        return render(request, 'index.html', context)


class AuthorDetailPageView(View):
    def get(self, request, pk):
        context = {}
        author = Author.objects.get(pk=pk)
        products = Product.objects.filter(author=author)
        print(products)
        print(author)
        context['author'] = author
        context['products'] = products
        return render(request, "market/author.html", context)
    

class AuthorsPage(ListView):
    model = Author
    template_name = 'market/authors.html'
    context_object_name = 'authors'
    
    
class ProductDetailPageView(View):
    def get(self, request, pk):
        context = {}
       
        product = Product.objects.get(pk=pk)
        context['product'] = product
        return render(request, "market/details.html", context)


class ExplorePageView(TemplateView):
    def get(self, request):
        context = {}
        products = Product.objects.all()

        #searching
        title = request.GET.get('keyword', None)
        categoriy = request.GET.get('Category', None)
        price = request.GET.get('Price', None)

        if title or price is not None:
            products = Product.objects.filter(title__icontains=title,
                                              price__icontains=price)
        
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 3)

        #pagination
        paginator = Paginator(products.order_by('id'), size)
        page_obj = paginator.page(page)

        context['products'] = page_obj
        context['is_size'] = products.count() > size
        return render(request, "market/explore.html", context)


class ExploreAuthorView(View):
    def get(self, request, pk):
        context = {}
        author = Author.objects.get(pk=pk)
        products = Product.objects.filter(author=author)
    
        context['products'] = products
        return render(request, "market/explore.html", context)


class ExploreCategoriyView(View):
    def get(self, request, pk):
        context = {}
        categoriy = Categoriy.objects.get(pk=pk)
        products = Product.objects.filter(categories=categoriy)
        context['products'] = products
        return render(request, "market/explore.html", context)
    

class ProductCreatePageView(View):
    def get(self, request):
        context = {}
        form = CreateProductForm()
        context['form'] = form
        return render(request, "market/create.html", context)

    def post(self, request):
        context = {}
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                image = form.cleaned_data.get('image'),
                title = form.cleaned_data.get("title"),
                desciptions = form.cleaned_data.get("desciptions"),
                price = form.cleaned_data.get('price'),
                categories = form.cleaned_data.get('categories'),
                ovner = form.cleaned_data.get('ovner'),
                author = request.user
            )
            messages.success(request, "Your Item succesfully created")
            return redirect(reverse("market:author-detail", kwargs={'pk':request.user.pk}))
        messages.warning(request, "Your Item is not valid !!!")
        context['form'] = form
        return render(request, "market/create.html", context)


def author_like(request, pk):
    like, created = AuthorLike.objects.get_or_create(likes=request.user)
    if not created:
        like.delete()
    return redirect(reverse("market:author-detail", kwargs={"pk":request.user.pk}))

class AddToCardAuthor(LoginRequiredMixin, View):

    def post(self, request, pk):
        count = request.POST.get("card_count", None)
        print(count)
        # if count is not None:
        #     product = Product.objects.get(pk=pk)
        #     authors = Author.objects.get(pk=pk)
        #     form = CardForm(request.POST)
        #     if form.is_valid():
        #         AuthorCardMarket.objects.create(
        #             products=product,
        #             authors=authors,
        #             proruct_count=form.cleaned_data.get("proruct_count")
        #         )
        #         messages.success(request, "Add to card")
                # return redirect(reverse("market:details", kwargs={"pk":pk}))

        return redirect(reverse("market:details", kwargs={"pk":pk}))


