from django.urls import path

from measurement.views import SensorView, DetailView, MeasurementsView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', DetailView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
