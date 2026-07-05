# PEP 8 — Python Style Guide
#
# PEP 8 (Python Enhancement Proposal 8) is the official style guide for Python code.
# Following it makes code more readable and consistent across the Python community.
#
# Key rules:
#
# 1. Indentation     : Use 4 spaces per level (never tabs).
# 2. Line length     : Max 79 characters per line.
# 3. Blank lines     : 2 blank lines between top-level definitions (functions/classes);
#                      1 blank line between methods inside a class.
# 4. Imports         : One import per line; stdlib → third-party → local.
# 5. Whitespace      : Space after commas, around operators; no space before colon in slices.
# 6. Naming          :
#    - variables / functions  → snake_case      (my_variable, calculate_total)
#    - classes                → PascalCase      (MyClass, BankAccount)
#    - constants              → UPPER_SNAKE_CASE (MAX_SIZE, PI)
#    - private attributes     → _leading_underscore
# 7. Strings         : Be consistent — pick single or double quotes and stick to it.
# 8. Comments        : Full sentences, start with capital letter; inline comments
#                      separated by 2 spaces and start with "# ".
# 9. Docstrings      : Use triple double-quotes for all public modules, functions, classes.
# 10. Comparison     : Use `is` / `is not` for None; use `==` for values.

# Good PEP 8 example
MAX_RETRIES = 3

def calculate_discount(price, discount_rate):
    """Return the discounted price."""
    return price * (1 - discount_rate)

class ShoppingCart:
    """Represents a user's shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the cart."""
        self.items.append(item)

cart = ShoppingCart()
cart.add_item("book")
print("Items:", cart.items)
print("Discount:", calculate_discount(100, 0.1))
