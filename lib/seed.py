from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

if __name__ == '__main__':
    fake = Faker()

    engine = create_engine('sqlite:///restaurants.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()


    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.commit()

    customers = []
    for _ in range(20):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        customers.append(customer)

    restaurants = []
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(1000, 20000)
        )
        session.add(restaurant)
        restaurants.append(restaurant)

    reviews = []
    for customer in customers:
        for restaurant in restaurants:
            star_rating = random.randint(1, 10)
            review = Review(
                star_rating=star_rating,
                customer=customer,
                restaurant=restaurant
            )
            session.add(review)
            reviews.append(review)

    session.commit()
    session.close()