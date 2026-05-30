from langchain_core.tools import tool # used for tools

@tool
def get_menu() -> str:
    """Returns the cafe menu with items and prices."""
    return """
    - Americano: $45
    - Cappuccino: $55
    - Latte: $55
    - Oat milk latte: $65
    - Croissant: $35
    - Avocado toast: $75
    """

@tool
def get_hours() -> str:
    """Returns the cafe opening hours."""
    return """
    
    """

@tool
def get_location() -> str:
    """Returns the cafe location."""
    return """
    
    """

@tool
def get_contact() -> str:
    """Returns the cafe contact information."""
    return """
    
    """

@tool
def make_reservation() -> str:
    """Makes a cafe reservation."""
    return """
    
    """

@tool
def get_specials() -> str:
    """Returns the weekly or daily specials."""
    return """
    
    """
