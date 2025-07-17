import math

def perform_calculations(data):
    """
    Performs required calculations and returns results as a dictionary.
    """
    return {
        "Sum": sum(data),
        "Difference (Max - Min)": max(data) - min(data),
        "Squares": [x**2 for x in data],
        "Square Roots": [math.sqrt(x) for x in data],
        "Average": sum(data) / len(data) if data else 0
    }
