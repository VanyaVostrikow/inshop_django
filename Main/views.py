from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.views import generic
from django.contrib import sessions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

from .models import Product
from .models import Comment
from .forms import CommentForm
from Cart.forms import CartAddProductForm
from Coupon.forms import CouponSearchForm
import time



class ProductsViews(generic.ListView):
    model = Product
    paginate_by = 9
    tag = None
    def tag(request, tag_slug=None):
        if tag_slug:
            tag =  get_object_or_404(Tag, slug=tag_slug)
            object_list = object_list.filter(tags__in=[tag])
        return(request, tag, object_list)
    context_object_name = 'Products'
    queryset = Product.objects.all()
    template_name = 'Products/my_products_list.html'
    def get_contex_data(self, **kwargs):

        context = super(ProductsViews, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

   
class ProductsDetailView(generic.DetailView):
    model = Product
    context_object_name = 'Product'
    template_name = 'Products/prod.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['object'].pk
        comments = Comment.objects.filter(PrProd = pk)
        cart_product_form = CartAddProductForm()
        context['comments'] = comments
        context['cart_form'] = cart_product_form
        return context
    
    def get_cart_data(self, pk):
        cart_product_form = CartAddProductForm()
    
def Create(request, pk, **kwargs):
    
    user = request.user
    print(user)
    
    error = ''
    form = CommentForm
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        user = request.user
        title = request.POST.get('title')
        data = {'title': title, 'PrProd': product, 'PrUser': user}
        form = CommentForm(data)
        if form.is_valid():
            form.save()
            print(pk)
            return redirect('/main/product/')
        else:
            error = 'INCORRECT'
            print(form)

    data  = {
        'PrProd': pk,
        'PrUser' : user,
        'form' : form,
        'error' : error,
    }
    print(data)
    return render(request, 'Products/create_comment.html', data)


      
def index(request):
    form_search = CouponSearchForm
    num_pr = Product.objects.all().count()
    context = {
        'num_pr': num_pr,
        'form_search':form_search,
    }
    
    return render(request, 'main/index.html', context=context)

def test(request):
    if request.method == 'GET':
            s = request.session
            print(s.keys())
            print(s.items())
            render(request, 'base_generic.html')
            if request.method == 'POST':
                return render(request, 'base_generic.html')
            
                

    return render(request, 'base_generic.html')
    

# Create your views here.
