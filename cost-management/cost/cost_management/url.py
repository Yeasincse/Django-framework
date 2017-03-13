from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^costlist/',views.ListExpense, name='costlist'),
]