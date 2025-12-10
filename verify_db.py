"""
Check MongoDB directly for the loan counts
"""

from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cashper_db"]  # Correct database
    collection = db["admin_loan_applications"]
    
    print("Checking admin_loan_applications collection in cashper_db...")
    print("="*60)
    
    loan_types = ["Home Loan", "Personal Loan", "Business Loan", "Short-term Loan"]
    
    total = 0
    for loan_type in loan_types:
        count = collection.count_documents({"type": loan_type})
        total += count
        print(f"{loan_type}: {count}")
    
    print(f"\nTotal: {total}")
    
    # Test the statistics function
    pipeline = [
        {
            "$group": {
                "_id": None,
                "totalAmount": {"$sum": "$amount"},
                "avgAmount": {"$avg": "$amount"},
                "avgCibil": {"$avg": "$cibilScore"}
            }
        }
    ]
    
    result = list(collection.aggregate(pipeline))
    if result:
        print(f"\nTotal Amount: {result[0].get('totalAmount', 0)}")
        print(f"Avg Amount: {result[0].get('avgAmount', 0)}")
        print(f"Avg CIBIL: {result[0].get('avgCibil', 0)}")
    
except Exception as e:
    print(f"Error: {str(e)}")
