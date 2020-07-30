from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from frontend.views import CarDetailsView, NewBookingView, HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailsView.as_view(), name='car-details'),
    path('booking/<int:car_pk>/', NewBookingView.as_view(), name='new-booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
