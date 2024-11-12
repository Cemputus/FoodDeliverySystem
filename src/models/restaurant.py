# src/models/restaurant.py
from src.utils import load_json, save_json

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.reviews = []

    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)

    def add_review(self, rating, comment):
        self.reviews.append({'rating': rating, 'comment': comment})
        self.save()

    def save(self):
        restaurants = load_json('data/restaurants.json')
        restaurants[self.name] = {
            'menu': [{'name': item.name, 'price': item.price} for item in self.menu],
            'reviews': self.reviews
        }
        save_json(restaurants, 'data/restaurants.json')

    @staticmethod
    def load(name):
        restaurants = load_json('data/restaurants.json')
        if name in restaurants:
            data = restaurants[name]
            restaurant = Restaurant(name)
            restaurant.menu = [MenuItem(item['name'], item['price']) for item in data['menu']]
            restaurant.reviews = data['reviews']
            return restaurant
        return None
