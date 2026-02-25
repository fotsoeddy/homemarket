from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Property
from .forms import PropertyForm
from .models import PropertyImage
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import PropertyLocation, Property
from .forms import PropertyLocationForm
from .models import Listing
from .forms import ListingForm
from users.models import SellerVerification
from django.contrib import messages
from django.shortcuts import redirect
from global_data.enum import UserType





class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "properties/property_create.html"
    success_url = reverse_lazy('list')

    def dispatch(self, request, *args, **kwargs):
        # Vérifier type SELLER
        if request.user.user_type != UserType.SELLER:
            messages.error(request, "Only sellers can create properties.")
            return redirect('home')

        # Vérifier validation admin
        try:
            verification = request.user.seller_verification
            if not verification.is_verified:
                messages.warning(request, "Your account is not yet approved.")
                return redirect('seller_verification')
        except SellerVerification.DoesNotExist:
            messages.warning(request, "You must submit verification documents first.")
            return redirect('seller_verification')

        return super().dispatch(request, *args, **kwargs)
    
class PropertyListView(LoginRequiredMixin, ListView):
        model = Property
        template_name = "seller/property_list.html"
        context_object_name = "properties"

        def get_queryset(self):
            return Property.objects.filter(owner=self.request.user)
        
class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "seller/property_form.html"
    success_url = reverse_lazy("properties:list")

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)        

class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = "seller/property_confirm_delete.html"
    success_url = reverse_lazy("properties:list")

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)
    
class PropertyLocationCreateView(CreateView):
    model = PropertyLocation
    form_class = PropertyLocationForm
    template_name = 'seller/property_location_create.html'

    def form_valid(self, form):
        property_id = self.kwargs['pk']
        property_obj = Property.objects.get(id=property_id)
        form.instance.property = property_obj
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('seller_dashboard')

class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'seller/listing_create.html'

    def form_valid(self, form):
        property_id = self.kwargs['pk']
        property_obj = Property.objects.get(id=property_id)

        form.instance.property = property_obj
        form.instance.agent = self.request.user  # vendeur

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('seller_dashboard')
    

class ListingUpdateView(UpdateView):
    model = Listing
    form_class = ListingForm
    template_name = 'properties/listing_update.html'

    def get_success_url(self):
        return reverse_lazy('seller_dashboard')
