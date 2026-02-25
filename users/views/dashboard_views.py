from django.views.generic import TemplateView

class BuyerDashboardView(TemplateView):
    template_name = 'home/buyer_dashboard.html'

class BuyerProfileView(TemplateView):
    template_name = 'home/buyer_profile.html'

class BuyerSavedPropertyView(TemplateView):
    template_name = 'home/buyer_saved_property.html'

class BuyerBookingView(TemplateView):
    template_name = 'home/buyer_booking.html'

class SellerProfileView(TemplateView):
    template_name = 'home/seller_profile.html'

class SellerKYCView(TemplateView):
    template_name = 'home/seller_kyc.html'
