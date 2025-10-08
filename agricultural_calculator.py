# Agricultural Calculator - My First Python Program
# Date: [Today's Date]
# Purpose: Practice basic Python with agricultural calculations

# Soil Analysis Calculator
print("=== Soil Analysis Calculator ===")
print()

# Variables for soil sample
sample_location = "North Field"
ph_value = 6.5
organic_matter = 3.2  # percentage
nitrogen = 45.8  # mg/kg
phosphorus = 28.3  # mg/kg
potassium = 156.7  # mg/kg

# Display results
print(f"Sample Location: {sample_location}")
print(f"pH Value: {ph_value}")
print(f"Organic Matter: {organic_matter}%")
print(f"Nitrogen (N): {nitrogen} mg/kg")
print(f"Phosphorus (P): {phosphorus} mg/kg")
print(f"Potassium (K): {potassium} mg/kg")
print()

# Simple calculations
if ph_value < 6.0:
    soil_condition = "Acidic - Consider liming"
elif ph_value > 7.5:
    soil_condition = "Alkaline - Monitor nutrient availability"
else:
    soil_condition = "Optimal pH range"

print(f"Soil Condition: {soil_condition}")

# Calculate fertilizer recommendation (simplified)
if nitrogen < 50:
    n_recommendation = "Apply nitrogen fertilizer"
else:
    n_recommendation = "Nitrogen levels adequate"

print(f"Nitrogen Recommendation: {n_recommendation}")
print()
print("Analysis complete!")
