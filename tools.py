from langchain_core.tools import tool # used for tools

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

    Phone: (915) 247-3860
    Email: hello@cafetresleches.com
    Website: www.cafetresleches.com
    Instagram: @cafetresleches
    Twitter/X: @cafetresleches
    Facebook: Café Tres Leches El Paso

    For reservations call us, DM us on Instagram, or ask me to make it.
    For catering inquiries email us at catering@cafetresleches.com
    """

@tool
def make_reservation(name: str, date: str, time: str, size: int) -> str:
    """Makes a cafe reservation."""
    return f"""

    CAFÉ TRES LECHES — RESERVATION CONFIRMATION

    Name: {name}
    Date: On {date}
    Time: At {time}
    Size: Party of {size}
    """

@tool
def get_specials() -> str:
    """Returns the weekly or daily specials."""
    return """
    
    """
