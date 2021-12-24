from django.urls import path
from . import views

urlpatterns = [
    path('addlaptop/',views.AddLaptopView.as_view(),name='add'),
    path('showlaptop/',views.showlaptopView.as_view(),name='show'),
    path('update/<int:id>/',views.updateView.as_view(),name='update'),
    path('delete/<int:id>/',views.DeleteView.as_view(),name='delete')
]