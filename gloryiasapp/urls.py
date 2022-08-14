from django.urls import path
from .import views


from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [

    path("", views.index, name="homepage"),
    path("courses", views.course, name="course"),
    path("aboutus", views.about, name="about"),
    path("contactus", views.contact, name="contact"),



    
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)