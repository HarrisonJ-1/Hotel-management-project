import csv
from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {
            101: {'type': 'Single', 'capacity': 1, 'beds': 1, 'amenities': ['TV', 'En-suite']},
            102: {'type': 'Double', 'capacity': 2, 'beds': 2, 'amenities': ['TV', 'En-suite', 'Couch']},
            # Add more rooms as needed
        }
        self.room_bookings = {}

    def home(self):
        print("Welcome to Hotel Management System")
        print("1. Booking")
        print("2. Room Information")
        print("3. Restaurant")
        print("4. Payment")
        print("5. Record Keeping")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.booking()
        elif choice == '2':
            self.room_info()
        elif choice == '3':
            self.restaurant()
        elif choice == '4':
            self.payment()
        elif choice == '5':
            self.record()
        else:
            print("Invalid choice")

    def booking(self):
        print("Booking a Room")
        name = input("Enter your name: ")
        room_type = input("Enter room type (Single/Double): ").capitalize()
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        if not self.date(check_in_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        room_number = self.find_available_room(room_type)
        if room_number is not None:
            self.room_bookings[room_number] = {'name': name, 'check_in_date': check_in_date}
            print("Room booked successfully!")
            print("Your room number is:", room_number)
        else:
            print("No available rooms of type", room_type)

    def find_available_room(self, room_type):
        for room, details in self.rooms.items():
            if details['type'] == room_type and room not in self.room_bookings:
                return room
        return None

    def room_info(self):
        print("Hotel Room Information")
        for room, details in self.rooms.items():
            print(f"Room {room}: Type: {details['type']}, Capacity: {details['capacity']}, Beds: {details['beds']}, Amenities: {', '.join(details['amenities'])}")

    def restaurant(self):
        print("Restaurant Menu:")
        menu = {
            'Burger': 10,
            'Pizza': 12,
            'Pasta': 8,
        }
        for item, price in menu.items():
            print(f"{item}: ${price}")

    def payment(self):
        print("Payment")
        pass

    def record(self):
        print("Guest Records")
        for room, booking in self.room_bookings.items():
            print(f"Room: {room}, Guest: {booking['name']}, Check-in Date: {booking['check_in_date']}")

    def save_customer_data(self, filename='hotel.csv'):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Room Number', 'Guest Name', 'Check-in Date'])
            for room, booking in self.room_bookings.items():
                writer.writerow([room, booking['name'], booking['check_in_date']])
        print("Customer data saved successfully.")

    def date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

# Main program
hotel_system = HotelManagementSystem()
hotel_system.home()

