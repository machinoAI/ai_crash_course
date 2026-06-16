# Docstrings — Purpose and Usage
#
# A docstring is a string literal placed as the first statement inside a
# function, class, or module. It describes what the code does and is
# accessible at runtime via the __doc__ attribute.
#
# Convention: use triple quotes """ """ even for single-line docstrings.

def add(n1, n2):
    """Return the sum of n1 and n2."""
    return n1 + n2

def greet(name):
    """
    Generate a greeting message.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting string.
    """
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class supporting basic arithmetic."""

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

# Accessing docstrings via __doc__
print(add.__doc__)
# Output:  Return the sum of n1 and n2.

print(greet.__doc__)
# Output:  (multi-line docstring shown above)

print(Calculator.__doc__)
# Output:  A simple calculator class supporting basic arithmetic.

# help() also uses __doc__ under the hood
# help(add)
