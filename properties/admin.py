from django.contrib import admin
from .models import (
    PropertyCategory, PropertyFeature, Property, 
    PropertyLocation, PropertyImage, Listing
)

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyLocationInline(admin.StackedInline):
    model = PropertyLocation
    can_delete = False

@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PropertyFeature)
class PropertyFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'property_type', 'price', 'created')
    list_filter = ('category', 'property_type', 'created')
    search_fields = ('title', 'description', 'owner__email')
    inlines = [PropertyLocationInline, PropertyImageInline]
    filter_horizontal = ('features',)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('property', 'agent', 'price', 'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('property__title', 'agent__email')

@admin.register(PropertyLocation)
class PropertyLocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'property')
    search_fields = ('city', 'country', 'address')

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'is_main', 'created')
