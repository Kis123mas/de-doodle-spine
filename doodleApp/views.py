from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages

def landingView(request):
    return render(request, 'doodleApp/index.html')


def aboutView(request):
    return render(request, 'doodleApp/about.html')


def productView(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'doodleApp/product.html', {'products': products})



def blogView(request):
    blog_list = BlogPost.objects.all().order_by('-published_date')
    paginator = Paginator(blog_list, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'doodleApp/blog.html', {'posts': posts})

def blogdetailView(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(slug=slug).order_by('-created_at')[:4]
    return render(request, 'doodleApp/blogdetail.html', {'post': post, 'recent_posts': recent_posts})



def portfolioView(request):
    categories = PortfolioCategory.objects.all()
    items_by_category = []

    for category in categories:
        slug = category.name.lower().replace(" ", "-")
        display_name = category.name.title()
        items = PortfolioItem.objects.filter(category=category)
        items_by_category.append({
            'slug': slug,
            'name': display_name,
            'items': items
        })

    return render(request, 'doodleApp/portfolio.html', {
        'items_by_category': items_by_category
    })


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'doodleApp/contact.html', {'form': form})