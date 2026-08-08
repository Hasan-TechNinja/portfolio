from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/submit/', views.contact_submit_view, name='contact_submit'),
    path('download-cv/', views.download_cv_view, name='download_cv'),
]
