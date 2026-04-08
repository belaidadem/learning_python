from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError

# 1. THE ENUM: Restricting choices to exactly three options
class BudgetLevel(str, Enum):
    BUDGET = "BUDGET"
    MID_RANGE = "MID_RANGE"
    LUXURY = "LUXURY"

# 2. THE MODEL: The "Schema" for your Trip
class TripPlan(BaseModel):
    destination: str = Field(description="The city or country for the trip")
    
    # Validation: ge=1 (Greater than or equal to 1), le=30 (Less than or equal to 30)
    duration_days: int = Field(ge=1, le=30)
    
    budget_level: BudgetLevel
    
    # A list of strings
    activities: List[str]
    
    is_visa_required: bool = False

# --- THE REAL WORLD TEST ---

def process_ai_data(raw_json_from_ai: dict):
    try:
        # This is the "Gatekeeper" line
        plan = TripPlan(**raw_json_from_ai)
        print("✅ SUCCESS: Data is clean and safe to use!")
        print(f"Destination: {plan.destination} for {plan.duration_days} days.")
    except ValidationError as e:
        print("❌ DATA REJECTED: The AI sent bad data!")
        # We print the error so we can see EXACTLY what failed
        print(e.json(indent=2))

# --- SIMULATE THE EXPERIMENT ---

# Test 1: Good Data
good_data = {
    "destination": "Algiers",
    "duration_days": 7,
    "budget_level": "MID_RANGE",
    "activities": ["Visit Casbah", "Eat Couscous"]
}

# Test 2: Bad Data (AI hallucinated a negative duration and a fake budget)
bad_data = {
    "destination": "Paris",
    "duration_days": -5,  # ERROR: Must be >= 1
    "budget_level": "SUPER_EXPENSIVE", # ERROR: Not in our Enum
    "activities": "Just walking" # ERROR: Should be a List, not a string
}

print("--- Testing Good Data ---")
process_ai_data(good_data)

print("\n--- Testing Bad Data ---")
process_ai_data(bad_data)