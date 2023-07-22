from django.urls import path

from app.apps.cryptotransaction.web import views

# Register your urls here

urlpatterns = [path("", views.SimpleView.as_view())]

# To register this URLS
# path("cryptotransaction/", include("app.cryptotransaction.web.urls"))
