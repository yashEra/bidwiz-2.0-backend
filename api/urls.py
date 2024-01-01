from django.urls import path ,include
from . views import *

urlpatterns = [
    # if url contains /api those all are redirected to below views
    path('', getRoutes),
]