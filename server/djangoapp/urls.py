#Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    
    # path for login
    path(route='login', view=views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path(route='get_cars', view=views.get_cars, name ='getcars'),
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
        path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
