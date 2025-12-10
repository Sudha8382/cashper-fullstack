"""
Seed Eligibility Criteria for Short Term Loan
Run this script to populate the eligibility criteria collection
"""

from app.database.db import connect_to_mongo
from app.database.repository.short_term_loan_repository import EligibilityCriteriaRepository

def seed_eligibility_criteria():
    """Seed eligibility criteria data"""
    
    # Connect to database
    connect_to_mongo()
    print("Connected to MongoDB")
    
    # Define eligibility criteria
    criteria_list = [
        {
            "label": "Minimum Age",
            "value": "21 years",
            "order": 1
        },
        {
            "label": "Maximum Age",
            "value": "60 years",
            "order": 2
        },
        {
            "label": "Minimum Monthly Income",
            "value": "₹15,000",
            "order": 3
        },
        {
            "label": "Employment Type",
            "value": "Salaried or Self-Employed",
            "order": 4
        },
        {
            "label": "Loan Amount Range",
            "value": "₹10,000 to ₹5,00,000",
            "order": 5
        },
        {
            "label": "Loan Tenure",
            "value": "1 to 24 months",
            "order": 6
        },
        {
            "label": "Required Documents",
            "value": "PAN Card, Aadhar Card, Bank Statement",
            "order": 7
        },
        {
            "label": "Processing Time",
            "value": "24-48 hours",
            "order": 8
        }
    ]
    
    # Check if criteria already exist
    existing = EligibilityCriteriaRepository.get_all()
    if existing:
        print(f"Found {len(existing)} existing criteria. Skipping seed.")
        return
    
    # Insert criteria
    for criterion in criteria_list:
        result = EligibilityCriteriaRepository.create(criterion)
        print(f"✓ Created: {criterion['label']} - {criterion['value']}")
    
    print(f"\n✅ Successfully seeded {len(criteria_list)} eligibility criteria!")

if __name__ == "__main__":
    seed_eligibility_criteria()
