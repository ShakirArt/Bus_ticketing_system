# Bus Ticketing System (OOP, Menu-Driven)

This project is a **Bus Ticketing System** implemented in Python using **Object-Oriented Programming (OOP)** concepts.  
It provides a **menu-driven interface** for managing buses, seat layouts, and passenger bookings.

---

## Main Features
- Add buses with details (ID, name, source, destination, time, fare, type: AC/Non-AC).
- View all registered buses.
- Book seats by selecting specific seat numbers (e.g., `A1`, `B2`).
- Track available and booked seats dynamically (booked seats are marked as `"X"`).
- View all bookings with passenger details and total fare.
- Search for a bus and display its seat layout.

---

## OOP Classes
### `Bus`
- Stores bus details (ID, name, source, destination, time, fare, type).
- Initializes seat layout based on bus type (AC/Non-AC).
- Tracks available seats.
- Methods:
  - `display_bus_details()`
  - `display_seat_layout()`
  - `mark_seat(seat_number)`

### `Booking`
- Stores booking details (ID, passenger, seats booked, total fare).
- Methods:
  - `display_booking_details()`

### `System`
- Manages buses and bookings.
- Methods:
  - `add_bus()`
  - `view_buses()`
  - `book_seat()`
  - `view_bookings()`
  - `search_bus()`

---

## Menu Options
1. Add Bus
2. View Buses
3. Search Bus
4. Book Seat
5. View Bookings
6. Exit
