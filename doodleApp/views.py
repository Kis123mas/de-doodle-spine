from django.shortcuts import render

def landingView(request):
    return render(request, 'doodleApp/index.html')


def aboutView(request):
    return render(request, 'doodleApp/about.html')


def productView(request):
    return render(request, 'doodleApp/product.html')



def blogView(request):
    return render(request, 'doodleApp/blog.html')


def blogdetailView(request):
    return render(request, 'doodleApp/blogdetail.html')


def portfolioView(request):
    return render(request, 'doodleApp/portfolio.html')



def contactView(request):
    return render(request, 'doodleApp/contact.html')