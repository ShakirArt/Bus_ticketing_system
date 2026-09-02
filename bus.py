class bus:
    def __init__(self, bus_id, bus_name, total_seats, source, destination, time, fare, bus_type):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.total_seats = total_seats
        self.source = source
        self.destination = destination
        self.time = time
        self.fare = fare
        self.bus_type = bus_type
        self.available_seats = total_seats

        if bus_type.lower() == "ac":
            self.seat_layout = [
                ["A1", "0", "A2", "A3"],
                ["B1", "0", "B2", "B3"],
                ["C1", "0", "C2", "C3"],
                ["D1", "0", "D2", "D3"],
                ["E1", "0", "E2", "E3"],
                ["F1", "0", "F2", "F3"],
                ["G1", "0", "G2", "G3"],
                ["H1", "0", "H2", "H3"],
                ["I1", "I2", "I3", "I4"]
            ]
        else:
            self.seat_layout = [
                ["A1","A2","0","A3","A4"],
                ["B1","B2","0","B3","B4"],
                ["C1","C2","0","C3","C4"],
                ["D1","D2","0","D3","D4"],
                ["E1","E2","0","E3","E4"],
                ["F1","F2","0","F3","F4"],
                ["G1","G2","0","G3","G4"],
                ["H1","H2","0","H3","H4"],
                ["I1","I2","0","I4","I5"],
                ["J1","J2","J3","J4","J5"]
            ]

    def display_bus_details(self):
        print(f"Bus ID: {self.bus_id}")
        print(f"Bus Name: {self.bus_name}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Time: {self.time}")
        print(f"Type: {self.bus_type}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Fare: {self.fare}")
        

    def display_seat_layout(self):
        for row in self.seat_layout:
            print(row)

    def mark_seat(self, seat_number):
        for row in self.seat_layout:
            for i in range(len(row)):
                if row[i] == seat_number:
                    row[i] = "X"
                    return True
        return False


class booking: 
    def __init__(self, booking_id, passenger, seat_booked,bus):
        self.booking_id = booking_id
        self.passenger = passenger
        self.seat_booked = seat_booked
        self.total_fare = bus.fare * seat_booked

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Passenger Name: {self.passenger}")
        print(f"Seat Booked: {self.seat_booked}")
        print(f"Total Fare: {self.total_fare}")

class system:
    def __init__(self):
        self.buses = []
        self.bookings = []

    def find_bus(self, bus_id):
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
        return None

    def find_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def add_bus(self):
        bus_id = int(input("Enter Bus ID: "))
        bus_name = input("Enter Bus Name: ")
        bus_type = input("Enter Bus Type (AC/Non-AC): ")
        total_seats = int(input("Enter Total Seats: "))
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        time = input("Enter Time: ")
        fare = float(input("Enter Fare: "))
        
        self.buses.append(bus(bus_id, bus_name, total_seats, source, destination, time, fare, bus_type))
        print("Bus added successfully!")

    def view_buses(self):
        for bus in self.buses:
            bus.display_bus_details()
            print()

    def book_seat(self):
        bus_id = int(input("Enter Bus ID: "))
        booking_id = int(input("Enter Booking ID: "))
        passenger= input("Enter Passenger Name: ")
        seats_booked = input("Enter Seat Numbers (comma separated, e.g. A1,B2): ").split(",")
        bus = self.find_bus(bus_id)
        if bus:
            if len(seats_booked) <= bus.available_seats:
                success = True
                for seat in seats_booked:
                    seat = seat.strip()
                    if not bus.mark_seat(seat):
                        print(f"Seat {seat} not found or already booked.")
                        success = False
                if success:
                    bus.available_seats -= len(seats_booked)
                    new_booking = booking(booking_id, passenger, len(seats_booked), bus)
                    self.bookings.append(new_booking)
                    print("Booking successful!")
                    print(f"Total Fare: {new_booking.total_fare}")
            else:
                print("Not enough seats available.")
        else:
            print("Bus not found.")

    def view_bookings(self):
        for booking in self.bookings:
            booking.display_booking_details()

    def search_bus(self):
        bus_id = int(input("Enter Bus ID to search: "))
        bus = self.find_bus(bus_id)
        if bus:
            bus.display_bus_details()
            print("Seat Layout:")
            bus.display_seat_layout() 
        else:
            print("Bus not found.")
                

s=system()
while True:
    print("1. Add Bus")
    print("2. View Buses")
    print("3. Search Bus")
    print("4. Book Seat ")
    print("5. View Bookings")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s.add_bus()
    elif choice == 2:
        s.view_buses()
    elif choice == 3:
        s.search_bus()
    elif choice == 4:
        s.book_seat()
    elif choice == 5:
        s.view_bookings()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")

