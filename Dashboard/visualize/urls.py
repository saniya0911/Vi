from django.urls import path
from .views import *

urlpatterns = [
    # Use angle brackets to capture the 'pk' parameter
    path('api/mymodels/', MyModelListCreateAPIView.as_view(), name='Market_report'),
    path('', index, name ="Dashboard"),
]