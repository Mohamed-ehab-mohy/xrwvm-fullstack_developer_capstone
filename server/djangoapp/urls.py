from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
app_name = 'djangoapp'
urlpatterns = [
    #path('login/', TemplateView.as_view(template_name="index.html")),
    #path(route='login', view=views.login_user, name='login'),
    path(route='login', view=views.login_user, name='login'),
    path('login/', TemplateView.as_view(template_name="index.html")),
    #path('get_cars/', views.get_cars, name='get_cars'),
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
        path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review/', views.add_review, name='add_review'),
    #path('get_cars/', views.get_cars, name='get_cars'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    path(route='add_review', view=views.add_review, name='add_review'),
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
