"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

chewy = Pet(name = "Chewy", species = "Mutt",
            photo_url = "https://photos.hancinema.net/photos/photo1342279.jpg",
            age = 6, available = True)

bucky = Pet(name = "Bucky", species = "Chocolate Labrador",
            photo_url = "https://www.allthingsdogs.com/wp-content/uploads/2019/07/Chocolate-Lab-Names-Feature-678x381.jpg",
            age = 3, available = True)

db.session.add_all([chewy, bucky])
db.session.commit()