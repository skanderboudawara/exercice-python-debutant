"""
Create a Tunisian booking house system for Djerba

This exercice must contains classes for houses
Classes for people

The user should then be able to see if a house is available or not
Booking a house should be possible
Cancelling a booking should be possible
"""

class House:
    def __init__(self, name, location, price_per_night):
        self.name = name
        self.location = location
        self.price_per_night = price_per_night
        self.booked_dates = []

    def is_available(self, date):
        return date not in self.booked_dates

    def book(self, date):
        if self.is_available(date):
            self.booked_dates.append(date)
            return True
        return False

    def cancel_booking(self, date):
        if date in self.booked_dates:
            self.booked_dates.remove(date)
            return True
        return False
    
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bookings = []

    def book_house(self, house, date):
        if house.book(date):
            self.bookings.append((house, date))
            return True
        return False

    def cancel_booking(self, house, date):
        if house.cancel_booking(date):
            self.bookings.remove((house, date))
            return True
        return False

house_1 = House("Villa Djerba", "20 Rue de la Liberté", 100)
house_2 = House("Maison Plage", "10 Rue de la Plage", 150)
person_1 = Person("Ahmed", "ahmed@example.com")

if __name__ == "__main__":
    person_1.book_house(house_1, "2023-07-01")
    person_1.book_house(house_2, "2023-07-02")
    print(f"House {house_1.name} booked on 2023-07-01: {house_1.is_available('2023-07-01')}")
    print(f"House {house_2.name} booked on 2023-07-02: {house_2.is_available('2023-07-02')}")
    person_1.cancel_booking(house_1, "2023-07-01")
    print(f"House {house_1.name} available after cancellation: {house_1.is_available('2023-07-01')}")
    print(f"Bookings for {person_1.name}: {person_1.bookings}")