"""
Agricultural Unit Converter
Author: Ibrahim Rashid
Date: 08 October 2025
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
    print("5. Fertilizer Rates")
    print("6. Exit")
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

def yield_converter():
    """Convert crop yield units"""
    print("\n--- YIELD CONVERTER ---")
    print("Common crop yields:")
    print("1. Corn: bushels/acre ↔ kg/hectare")
    print("2. Wheat: bushels/acre ↔ kg/hectare")
    print("3. Soybeans: bushels/acre ↔ kg/hectare")
    
    crop_choice = input("Select crop (1-3): ")
    conversion_choice = input("Convert (1) bu/ac to kg/ha or (2) kg/ha to bu/ac: ")
    
    factors = {
        "1": {"name": "Corn", "bu_to_kg": 62.77},
        "2": {"name": "Wheat", "bu_to_kg": 67.25},
        "3": {"name": "Soybeans", "bu_to_kg": 67.25}
    }
    
    if crop_choice in factors:
        crop_name = factors[crop_choice]["name"]
        factor = factors[crop_choice]["bu_to_kg"]
        
        if conversion_choice == "1":
            bu_per_acre = float(input(f"Enter {crop_name} yield (bushels/acre): "))
            kg_per_hectare = bu_per_acre * factor
            print(f"{bu_per_acre} bu/ac = {kg_per_hectare:.1f} kg/ha ({crop_name})")
        elif conversion_choice == "2":
            kg_per_hectare = float(input(f"Enter {crop_name} yield (kg/hectare): "))
            bu_per_acre = kg_per_hectare / factor
            print(f"{kg_per_hectare} kg/ha = {bu_per_acre:.1f} bu/ac ({crop_name})")

def fertilizer_calculator():
    """Calculate fertilizer application rates"""
    print("\n--- FERTILIZER CALCULATOR ---")
    print("Convert fertilizer rates: lbs/acre ↔ kg/hectare")
    
    choice = input("Convert (1) lbs/acre to kg/ha or (2) kg/ha to lbs/acre: ")
    
    if choice == "1":
        lbs_per_acre = float(input("Enter rate (lbs/acre): "))
        kg_per_hectare = lbs_per_acre * 1.121
        print(f"{lbs_per_acre} lbs/ac = {kg_per_hectare:.1f} kg/ha")
    elif choice == "2":
        kg_per_hectare = float(input("Enter rate (kg/hectare): "))
        lbs_per_acre = kg_per_hectare / 1.121
        print(f"{kg_per_hectare} kg/ha = {lbs_per_acre:.1f} lbs/ac")

def main_menu():
    """Main program loop"""
    while True:
        welcome_message()
        choice = input("\nSelect an option (1-6): ")
        
        if choice == "1":
            area_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            print("\nVolume converter coming soon!")  # Placeholder
        elif choice == "4":
            yield_converter()
        elif choice == "5":
            fertilizer_calculator()
        elif choice == "6":
            print("Thank you for using Agricultural Unit Converter!")
            break
        else:
            print("Invalid choice. Please select 1-6.")
        
        continue_choice = input("\nWould you like another conversion? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Thank you for using Agricultural Unit Converter!")
            break

if __name__ == "__main__":
    main_menu()
