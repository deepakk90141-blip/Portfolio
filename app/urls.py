from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('my-works/', views.portfolio, name='works'),
    path('my-works/ecommerce/', views.ecommerce_detail, name='ecommerce_detail'),
    path('my-works/branding/', views.branding_detail, name='branding_detail'),
    path('my-works/web-app/', views.webapp_detail, name='webapp_detail'),
    path('my-works/portfolio-project/', views.portfolio_detail, name='portfolio_detail'),
    path('resume/', views.resume, name='resume'),
    path('action/', views.action, name='action'),
    path('case-study/', views.case_study, name='case_study'),
]