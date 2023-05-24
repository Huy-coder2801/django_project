from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

from website.customer import views as customer_view
from website.driver import views as driver_view
from .forms import LoginForm

customer_urlpatterns = [
    path('', customer_view.home, name='home'),
    path('profile/', customer_view.profile, name='profile'),
    path('create_order/', customer_view.create_order, name='create_order'),
    path('orders/current/', customer_view.orders, name='orders'),
    path('orders/archived/', customer_view.archived_orders, name='archived'),
    path('orders/<order_id>/', customer_view.details, name='details'),
]

driver_urlpatterns = [
    path('', driver_view.driver_page, name='home'),
    path('jobs/', driver_view.jobs, name="jobs"),
    path('my_job/', driver_view.myjob, name="myjob"),
    path('dashboard/', driver_view.dashboard, name="dashboard"),
    path('jobs/<id>/', driver_view.available_jobs, name='available_jobs'),
]

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    
    
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   
    
    path('customer/', include((customer_urlpatterns,'customer'), namespace='customer')),
    path('driver/', include((driver_urlpatterns, 'driver')))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)