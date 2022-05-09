from django.urls import path
from django.contrib import admin
from measurement.views import SensorView, SensorUpdateView, MeasurmentCreateView, SensorDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', SensorView.as_view()),
    path('sensor/<pk>/', SensorUpdateView.as_view()),
    path('measurement/', MeasurmentCreateView.as_view()),
    path('sensordetail/<pk>/', SensorDetailView.as_view()),

]
