"""
Seed data for Short Term Loan Eligibility Criteria
"""
from app.database.db import get_database, connect_to_mongo, close_mongo_connection

def seed_eligibility_criteria():
    """Seed eligibility criteria for Short Term Loan"""
    
    try:
        # Connect to database
        connect_to_mongo()
        db = get_database()
        collection = db["short_term_loan_eligibility_criteria"]
        
        # Clear existing data
        collection.delete_many({})
        print("Cleared existing eligibility criteria")
        
        # Eligibility criteria data
        criteria = [
            {"label": "Age", "value": "21 to 65 years", "order": 1},
            {"label": "Employment", "value": "Salaried/Self-employed/Business", "order": 2},
            {"label": "Minimum Income", "value": "₹15,000 per month", "order": 3},
            {"label": "Credit Score", "value": "650 and above (preferred)", "order": 4},
            {"label": "Work Experience", "value": "Minimum 6 months in current job", "order": 5},
            {"label": "Nationality", "value": "Indian Resident", "order": 6}
        ]
        
        # Insert data
        result = collection.insert_many(criteria)
        print(f"✅ Inserted {len(result.inserted_ids)} eligibility criteria")
        
        # Display inserted data
        print("\n📋 Inserted Criteria:")
        for criterion in criteria:
            print(f"   • {criterion['label']}: {criterion['value']}")
        
        print("\n✅ Seed data inserted successfully!")
        
    except Exception as e:
        print(f"❌ Error seeding data: {str(e)}")
    finally:
        close_mongo_connection()

if __name__ == "__main__":
    seed_eligibility_criteria()
