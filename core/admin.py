from django.contrib import admin
from .models import (
    Conversation, Message, Favorite, Review, Rating, 
    Transaction, Payment, Offer, Visit, Notification, Report
)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')
    filter_horizontal = ('participants',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'is_read', 'created')
    list_filter = ('is_read', 'created')
    search_fields = ('content', 'sender__email')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'created')
    list_filter = ('created',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'property', 'rating', 'created')
    list_filter = ('rating', 'created')
    search_fields = ('comment', 'reviewer__email')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'score', 'created')
    list_filter = ('score', 'created')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'listing', 'amount', 'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('id', 'buyer__email')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'transaction', 'method', 'amount', 'created')
    list_filter = ('method', 'created')
    search_fields = ('reference',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'listing', 'amount', 'accepted', 'rejected', 'created')
    list_filter = ('accepted', 'rejected', 'created')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'date', 'confirmed', 'created')
    list_filter = ('confirmed', 'date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'title', 'is_read', 'created')
    list_filter = ('is_read', 'created')
    search_fields = ('title', 'message')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_user', 'reported_property', 'created')
    list_filter = ('created',)
    search_fields = ('reason',)
