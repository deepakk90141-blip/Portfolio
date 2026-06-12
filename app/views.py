from django.shortcuts import render
from .models import ContactSubmission

# Create your views here.

def index(request):
    success_message = None
    name = ''
    email = ''
    phone = ''
    message = ''

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and phone and message:
            ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            success_message = 'Thank you! Your message has been saved.'
            name = email = phone = message = ''
        else:
            success_message = 'Please complete all fields before sending.'

    recent_submissions = ContactSubmission.objects.order_by('-created_at')[:5]

    return render(request, 'index.html', {
        'success_message': success_message,
        'name': name,
        'email': email,
        'phone': phone,
        'message': message,
        'recent_submissions': recent_submissions,
    })


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def ecommerce_detail(request):
    return render(request, 'ecommerce_detail.html')

def branding_detail(request):
    return render(request, 'branding_detail.html')

def webapp_detail(request):
    return render(request, 'webapp_detail.html')

def portfolio_detail(request):
    return render(request, 'portfolio_detail.html')

def resume(request):
    return render(request, 'resume.html')

def action(request):
    return render(request, 'components/port_action.html')

def case_study(request):
    return render(request, 'case_study.html')
