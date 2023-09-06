from django.urls import path 
from .views import ProductView,BranchView

urlpatterns = [
    path('Product/' , ProductView.as_view()),
    path('Branch/', BranchView.as_view())
]