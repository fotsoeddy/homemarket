import os
import django
import sys
from django.core.files import File

# Configuration de l'environnement Django
sys.path.append('/home/eddy/projects/reine/HomeMarket')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homemarket.settings')
django.setup()

from properties.models import Property, PropertyCategory, PropertyLocation, PropertyImage, PropertyFeature
from django.contrib.auth import get_user_model
from global_data.enum import PropertyType

User = get_user_model()

def create_house():
    # 1. Get or create category
    category, _ = PropertyCategory.objects.get_or_create(name="Modern Villa")
    
    # 2. Get owner
    owner = User.objects.get(email="admin@example.com")
    
    # 3. Create property
    prop = Property.objects.create(
        owner=owner,
        category=category,
        property_type=PropertyType.HOUSE,
        title="Magnificent Modern Villa",
        description="A beautiful modern villa with luxury finishes and a spacious layout.",
        price=500000.00,
        bedrooms=4,
        bathrooms=3,
        area_sqm=250.00,
        status=Property.Status.APPROUVE
    )
    
    # 4. Create location
    PropertyLocation.objects.create(
        property=prop,
        address="123 Luxury Ave",
        city="Douala",
        country="Cameroon",
        latitude=4.0511,
        longitude=9.7679
    )
    
    # 5. Add image
    image_path = "/home/eddy/projects/reine/HomeMarket/media/Screenshot from 2026-03-30 11-11-16.png"
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            prop_image = PropertyImage(property=prop, is_main=True)
            prop_image.image.save(os.path.basename(image_path), File(f), save=True)
            print(f"Propriété créée avec succès avec l'image : {prop_image.image.name}")
    else:
        print(f"Image non trouvée à l'emplacement : {image_path}")

if __name__ == "__main__":
    create_house()
