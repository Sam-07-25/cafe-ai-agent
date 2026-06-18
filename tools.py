from langchain_core.tools import tool # used for tools
from reservations import load_reservations, save_reservations, delete_reservation
from datetime import datetime

@tool
def get_menu() -> str:
    """Returns the full cafe menu with categories, items, and prices."""
    return """
    CAFÉ TRES LECHES — MENU

    --- HOT DRINKS ---
    - Americano: $3.50
    - Drip Coffee: $3.00
    - Cappuccino: $4.50
    - Latte: $4.50
    - Vanilla Latte: $5.00
    - Caramel Latte: $5.00
    - Mocha: $5.25
    - Matcha Latte: $5.25
    - Chai Latte: $4.75
    - Hot Chocolate: $4.50

    --- ICED DRINKS ---
    - Cold Brew: $4.75
    - Cold Brew with Milk: $5.25
    - Iced Latte: $4.75
    - Coffee Frappé: $5.75
    - Mocha Frappé: $6.00
    - Caramel Frappé: $6.00
    - Iced Matcha: $5.25
    - Coconut Lemonade: $4.50
    - Hibiscus Iced Tea: $3.75

    --- MILK ALTERNATIVES (add-on) ---
    - Oat Milk: +$0.75
    - Almond Milk: +$0.75
    - Coconut Milk: +$0.75

    --- BREAKFAST ---
    - Avocado Toast with Fried Egg: $9.50
    - French Toast with Mixed Berries: $9.00
    - Yogurt Bowl with Granola and Fruit: $8.00
    - Eggs Benedict: $11.00
    - Breakfast Burrito: $8.50

    --- BAKERY ---
    - Butter Croissant: $3.75
    - Ham and Cheese Croissant: $5.50
    - Blueberry Muffin: $3.50
    - Chocolate Muffin: $3.50
    - Orange Scone: $3.25
    - Cheesecake Slice: $5.00
    - Brownie: $4.00
    - Chocolate Chip Cookie: $3.00

    --- HEALTHY OPTIONS ---
    - Quinoa Veggie Bowl: $10.00
    - Açaí Bowl: $9.50
    - Chicken Avocado Wrap: $9.75

    --- ADD-ONS ---
    - Extra Espresso Shot: +$1.00
    - Flavored Syrup: +$0.75
    - Whipped Cream: +$0.50
    """

@tool
def get_hours() -> str:
    """Returns the cafe opening hours."""
    return """
    CAFÉ TRES LECHES — OPENING HOURS

    Monday - Friday: 7:00 AM - 8:00 PM
    Saturday: 8:00 AM - 9:00 PM
    Sunday: 9:00 AM - 6:00 PM
    """

@tool
def get_location() -> str:
    """Returns the cafe location."""
    return """
    CAFÉ TRES LECHES — LOCATION

    1420 N Mesa St, El Paso, TX 79902

    We're located in the heart of Midtown El Paso, on the corner of N Mesa St and W Yandell Dr. 

    Parking: Free street parking available on Mesa St and surrounding streets. 
    We're also a 5 minute walk from the Sun Metro bus stop on Mesa & Yandell.

    Landmarks: Next to Kern Place neighborhood, 5 minutes from UTEP campus.
    """

@tool
def get_contact() -> str:
    """Returns the cafe contact information."""
    return """
    CAFÉ TRES LECHES — CONTACT INFO

    - Phone: (915) 247-3860
    - Email: hello@cafetresleches.com
    - Website: www.cafetresleches.com
    - Instagram: @cafetresleches
    - Twitter/X: @cafetresleches
    - Facebook: Café Tres Leches El Paso

    For reservations call us, DM us on Instagram, or ask me to make it.
    For catering inquiries email us at catering@cafetresleches.com
    """

@tool
def make_reservation(name: str, date: str, time: str, size, phone: str) -> str:
    """Makes a new cafe reservation. Date must be in YYYY-MM-DD format. Time must be in HH:MM AM/PM format."""
    operation_hours = {
        1: (datetime.strptime("7:00 AM", "%I:%M %p"), datetime.strptime("8:00 PM", "%I:%M %p")),
        2: (datetime.strptime("8:00 AM", "%I:%M %p"), datetime.strptime("9:00 PM", "%I:%M %p")),
        3: (datetime.strptime("9:00 AM", "%I:%M %p"), datetime.strptime("6:00 PM", "%I:%M %p"))
    }
    if int(size) < 2 or int(size) > 12:
        return """
        We're sorry, we can't book this reservation.
        According to our policy, reservations are available for parties of 2 to 12 guests.
        """
    day = datetime.strptime(date, "%Y-%m-%d").weekday()
    if day == 5:
        opening = operation_hours[2][1]
        closing = operation_hours[2][2]
    if day == 6:
        opening = operation_hours[3][1]
        closing = operation_hours[3][2]
    else:
        opening = operation_hours[1][1]
        closing = operation_hours[1][2]
    if time < opening or time > closing:
        return f"""
        We're sorry, we can't book this reservation.
        Opening hours on {date} are from {opening} to {closing}.
        """
    reservations = load_reservations()
    reservations.append({
        "name": name,
        "date": date,
        "time": time,
        "party_size": int(size),
        "phone_number": phone
    })
    save_reservations(reservations)

    return f"""
    CAFÉ TRES LECHES — RESERVATION CONFIRMATION

    - Name: {name}
    - Date: On {date}
    - Time: At {time}
    - Size: Party of {size}
    """

@tool
def cancel_reservation(name: str, date: str, time: str) -> str:
    """Cancels an existing cafe reservation."""

    reservations = load_reservations()
    success = delete_reservation(name, date, time)
    if success:
        return f"Reservation for {name} on {date} was successfully cancelled."
    else:
        return f"No reservation found for {name} on {date}."

@tool
def get_reservation_policy() -> str:
    """Returns the cafe reservation policy."""
    return """
    CAFÉ TRES LECHES — RESERVATION POLICY

    - Reservations are available for parties of 2 to 12 guests.
    - We accept reservations up to 30 days in advance.
    - Reservations must be made at least 2 hours before the desired time.
    - We hold reservations for 15 minutes past the booking time.
      After that, the table may be released to walk-in guests.
    - To cancel or modify a reservation, please contact us at least 
      2 hours in advance by phone or Instagram DM.
    - For parties of 8 or more, a valid credit card is required to hold 
      the reservation. No charge is made unless there is a no-show.
    - No-shows for parties of 8 or more will be charged $10 per person.
    - Walk-ins are always welcome based on availability.
    """

@tool
def get_specials() -> str:
    """Returns the weekly or daily specials with categories, items, prices, and dates."""
    return """
    CAFÉ TRES LECHES — WEEKLY SPECIALS

    --- TODAY'S FEATURED DRINK ---
    - Lavender Honey Latte: $6.00

    --- SEASONAL SPECIAL ---
    - Horchata Cold Brew: $6.50

    --- FOOD SPECIAL ---
    - Tres Leches French Toast: $11.00

    --- HAPPY HOUR (Mon - Fri, 2:00 PM - 4:00 PM) ---
    - 20% off all frappés
    - $1 off any pastry with the purchase of a drink

    --- WEEKEND BRUNCH SPECIAL (Sat - Sun, 9:00 AM - 12:00 PM) ---
    - Brunch Combo: Any breakfast item + any drink for $14.00
    (saves up to $3.50)

    Specials rotate weekly. Follow us on Instagram @cafetresleches 
    to stay up to date!
    """

all_tools = [get_contact, get_menu, get_location, get_hours, get_reservation_policy, get_specials, make_reservation, cancel_reservation]