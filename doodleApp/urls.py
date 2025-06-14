from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingView, name='landing'),
    path('about', views.aboutView, name='about'),
    path('product', views.productView, name='product'),
    path('blog', views.blogView, name='blog'),
    path('blog/<slug:slug>/', views.blogdetailView, name='blog-detail'),
    path('portfolio', views.portfolioView, name='portfolio'),
    path('contact', views.contactView, name='contact')
]