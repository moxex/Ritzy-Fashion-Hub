from django.shortcuts import render
from posts.models import Post, About, ContactUs
from products.models import Product, Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')[:6]
    latest_posts = Post.objects.order_by('-date')[:2]
    context = {
        'categories': categories,
        'products': products,
        'latest_posts': latest_posts,

    }
    return render(request, 'ritzy/index.html', context)


def about(request):
    about = About.objects.all()
    context = {
    'abouts': about,    
    }
    return render(request, 'ritzy/about_us.html', context)


def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        subject = request.POST['subject']
        message = request.POST['message']

        ContactUs.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            subject=subject,
            message=message
        )
        return render(request, 'ritzy/contact_us_success.html')
    return render(request, 'ritzy/contact_us.html')

