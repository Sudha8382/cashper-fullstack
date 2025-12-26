"""
Check current user's dashboard data in database
"""
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('cashper_backend/.env')

# Get MongoDB connection string
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'cashper')

def check_user_data():
    """Check what data exists for users in database"""
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        
        print("=" * 80)
        print("DATABASE USER DATA CHECK")
        print("=" * 80)
        
        # Get all users
        users = list(db.users.find({}, {"_id": 1, "email": 1, "name": 1, "isAdmin": 1}).limit(5))
        
        print(f"\n📋 Found {db.users.count_documents({})} users in database")
        print("\nFirst 5 users:")
        for user in users:
            user_id = str(user["_id"])
            email = user.get("email", "No email")
            name = user.get("name", "No name")
            is_admin = user.get("isAdmin", False)
            
            print(f"\n{'='*60}")
            print(f"👤 User: {name} ({email})")
            print(f"   ID: {user_id}")
            print(f"   Admin: {is_admin}")
            
            if is_admin:
                print("   ⚠️  Admin user - skipping data check")
                continue
            
            # Check loans
            personal_loans = db.personal_loans.count_documents({"userId": user_id})
            home_loans = db.home_loans.count_documents({"userId": user_id})
            business_loans = db.business_loans.count_documents({"userId": user_id})
            short_term_loans = db.short_term_loans.count_documents({"userId": user_id})
            total_loans = personal_loans + home_loans + business_loans + short_term_loans
            
            # Check insurance
            health_insurance = db.health_insurance_inquiries.count_documents({"userId": user_id})
            motor_insurance = db.motor_insurance_inquiries.count_documents({"userId": user_id})
            term_insurance = db.term_insurance_inquiries.count_documents({"userId": user_id})
            total_insurance = health_insurance + motor_insurance + term_insurance
            
            # Check investments
            sip = db.sip_inquiries.count_documents({"userId": user_id})
            mutual_funds = db.mutual_fund_inquiries.count_documents({"userId": user_id})
            total_investments = sip + mutual_funds
            
            # Check documents
            documents = db.documents.count_documents({"userId": user_id})
            
            print(f"\n   📊 Data Summary:")
            print(f"      💰 Loans: {total_loans} (P:{personal_loans}, H:{home_loans}, B:{business_loans}, ST:{short_term_loans})")
            print(f"      🛡️  Insurance: {total_insurance} (Health:{health_insurance}, Motor:{motor_insurance}, Term:{term_insurance})")
            print(f"      📈 Investments: {total_investments} (SIP:{sip}, MF:{mutual_funds})")
            print(f"      📄 Documents: {documents}")
            
        # Check for data without userId or with wrong format
        print(f"\n{'='*80}")
        print("🔍 CHECKING FOR DATA WITHOUT PROPER userId")
        print("=" * 80)
        
        collections_to_check = [
            'personal_loans', 'home_loans', 'business_loans', 'short_term_loans',
            'health_insurance_inquiries', 'motor_insurance_inquiries', 'term_insurance_inquiries',
            'sip_inquiries', 'mutual_fund_inquiries'
        ]
        
        for collection_name in collections_to_check:
            if collection_name in db.list_collection_names():
                total = db[collection_name].count_documents({})
                without_userid = db[collection_name].count_documents({"userId": {"$exists": False}})
                
                if total > 0:
                    print(f"\n📦 {collection_name}:")
                    print(f"   Total documents: {total}")
                    print(f"   Without userId: {without_userid}")
                    
                    # Show sample userId formats
                    sample = db[collection_name].find_one({})
                    if sample and "userId" in sample:
                        print(f"   Sample userId: {sample['userId']} (type: {type(sample['userId']).__name__})")
        
        client.close()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_user_data()
