from django.urls import path
from .views import PropertyCreateView, PropertyListView,  PropertyUpdateView, PropertyDeleteView,  PropertyLocationCreateView, ListingCreateView, ListingUpdateView

app_name = "properties"

urlpatterns = [
    path("create/", PropertyCreateView.as_view(), name="create"),
     path("", PropertyListView.as_view(), name="list"),
      path("update/<int:pk>/", PropertyUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PropertyDeleteView.as_view(), name="delete"),
    path('property/<int:pk>/location/', PropertyLocationCreateView.as_view(), name='property_add_location'),
    path('property/<int:pk>/listing/', ListingCreateView.as_view(), name='property_create_listing'),
    path('listing/<int:pk>/edit/', ListingUpdateView.as_view(), name='listing_update'),





]
