"""Check MongoDB Atlas connection and data"""
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env from backend directory
env_path = Path('cashper_backend/app/.env')
load_dotenv(env_path)

mongo_url = os.getenv('MONGO_URL', 'mongodb+srv://kumuyadav249_db_user:O0zb3rZlZXArZiSg@cluster0.mnzwn7m.mongodb.net/')
mongo_db = os.getenv('MONGO_DB', 'cashper_db')

print(f'Connecting to: {mongo_url[:50]}...')
print(f'Database: {mongo_db}')

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['admin_loan_applications']
    
    print(f'\nTotal documents: {col.count_documents({})}')
    print(f'Home: {col.count_documents({"type": "Home Loan"})}')
    print(f'Personal: {col.count_documents({"type": "Personal Loan"})}')
    print(f'Business: {col.count_documents({"type": "Business Loan"})}')
    print(f'Short-term: {col.count_documents({"type": "Short-term Loan"})}')
    
    # Check data sample
    sample = col.find_one()
    if sample:
        print(f'\nSample document from MongoDB Atlas:')
        print(f'  Customer: {sample.get("customer")}')
        print(f'  Type: {sample.get("type")}')
        print(f'  Amount: {sample.get("amount")}')
        
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
