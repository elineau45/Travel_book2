from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "main_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("old_travels/", views.old_travels, name="old_travels"),
    path("test_detail/", views.test_detail, name="test_detail"),
    path("villes/", views.villes, name="villes"),
    path("nantes/", views.nantes, name="nantes"),
    path("nice/", views.nice, name="nice"),
    path("marseille_cassis/", views.marseille_cassis, name="marseille_cassis"),
    path("lehavre/", views.lehavre, name="lehavre"),
    path("vannes/", views.vannes, name="vannes"),
    path("brest/", views.brest, name="brest"),
    path("orleans/", views.orleans, name="orleans"),
    path("propos/", views.propos, name="propos"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# elif getattr(settings, "FORCE_SERVE_STATIC", False):
#     settings.DEBUG = True
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     settings.DEBUG = False
