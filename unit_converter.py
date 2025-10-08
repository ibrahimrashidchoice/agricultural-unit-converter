"""
Agricultural Unit Converter
Author: [Your Name]
Date: [Current Date]
Purpose: Convert between common agricultural units
"""

def welcome_message():
    """Display welcome message and available conversions"""
    print("=" * 50)
    print("  AGRICULTURAL UNIT CONVERTER")
    print("=" * 50)
    print("Available conversions:")
    print("1. Area (acres, hectares, square meters)")
    print("2. Weight (pounds, kilograms, tons)")
    print("3. Volume (gallons, liters)")
    print("4. Yield (bushels/acre, kg/hectare)")
    print("5. Exit")
    print("=" * 50)

def area_converter():
    """Convert between area units"""
    print("\n--- AREA CONVERTER ---")
    print("1. Acres to Hectares")
    print("2. Hectares to Acres")
    print("3. Acres to Square Meters")
    
    choice = input("Select conversion (1-3): ")
    
    if choice == "1":
        acres = float(input("Enter acres: "))
        hectares = acres * 0.404686
        print(f"{acres} acres = {hectares:.2f} hectares")
    elif choice == "2":
        hectares = float(input("Enter hectares: "))
        acres = hectares * 2.47105
        print(f"{hectares} hectares = {acres:.2f} acres")
    elif choice == "3":
        acres = float(input("Enter acres: "))
        sq_meters = acres * 4046.86
        print(f"{acres} acres = {sq_meters:.2f} square meters")

# Start with basic structure - we'll add more functions
if __name__ == "__main__":
    welcome_message()
    area_converter()
    def weight_converter():
    """Convert between weight units"""
    print("\n--- WEIGHT CONVERTER ---")
    print("1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Tons (US) to Metric Tons")
    
    choice = input("Select conversion (1-3): ")
    
    if choice == "1":
        pounds = float(input("Enter pounds: "))
        kg = pounds * 0.453592
        print(f"{pounds} lbs = {kg:.2f} kg")
    elif choice == "2":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} lbs")
    elif choice == "3":
        us_tons = float(input("Enter US tons: "))
        metric_tons = us_tons * 0.907185
        print(f"{us_tons} US tons = {metric_tons:.2f} metric tons")