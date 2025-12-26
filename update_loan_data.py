from pymongo import MongoClient
from datetime import datetime, timedelta
from bson import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

# User ID for sudha@gmail.com
user_id = "694398f22bd499f1a272732b"
user_email = "sudha@gmail.com"

print("Updating existing loan data with phone, address, and documents...")

# Update Personal Loans
personal_loans = db['personal_loans'].find({'userId': user_id})
for loan in personal_loans:
    update_data = {
        'mobileNumber': '+91 9876543210',
        'phone': '+91 9876543210',
        'address': '123 Main Street, Mumbai, Maharashtra 400001',
        'aadharCard': f'/uploads/documents/{loan["_id"]}_aadhar.pdf',
        'panCard': f'/uploads/documents/{loan["_id"]}_pan.pdf',
        'photograph': f'/uploads/documents/{loan["_id"]}_photo.jpg',
        'incomeProof': f'/uploads/documents/{loan["_id"]}_income.pdf',
        'addressProof': f'/uploads/documents/{loan["_id"]}_address.pdf',
        'bankStatements': f'/uploads/documents/{loan["_id"]}_bank.pdf',
        'aadharCardFileName': f'{loan["_id"]}_aadhar.pdf',
        'panCardFileName': f'{loan["_id"]}_pan.pdf',
        'photographFileName': f'{loan["_id"]}_photo.jpg',
        'incomeProofFileName': f'{loan["_id"]}_income.pdf',
        'addressProofFileName': f'{loan["_id"]}_address.pdf',
        'bankStatementsFileName': f'{loan["_id"]}_bank.pdf'
    }
    db['personal_loans'].update_one({'_id': loan['_id']}, {'$set': update_data})
    print(f"✅ Updated Personal Loan {loan['_id']}")

# Update Home Loans
home_loans = db['home_loans'].find({'userId': user_id})
for loan in home_loans:
    update_data = {
        'mobileNumber': '+91 9876543210',
        'phone': '+91 9876543210',
        'address': '456 Green Avenue, Pune, Maharashtra 411001',
        'aadharCard': f'/uploads/documents/{loan["_id"]}_aadhar.pdf',
        'panCard': f'/uploads/documents/{loan["_id"]}_pan.pdf',
        'photograph': f'/uploads/documents/{loan["_id"]}_photo.jpg',
        'incomeProof': f'/uploads/documents/{loan["_id"]}_income.pdf',
        'addressProof': f'/uploads/documents/{loan["_id"]}_address.pdf',
        'bankStatements': f'/uploads/documents/{loan["_id"]}_bank.pdf',
        'propertyDocuments': f'/uploads/documents/{loan["_id"]}_property.pdf',
        'aadharCardFileName': f'{loan["_id"]}_aadhar.pdf',
        'panCardFileName': f'{loan["_id"]}_pan.pdf',
        'photographFileName': f'{loan["_id"]}_photo.jpg',
        'incomeProofFileName': f'{loan["_id"]}_income.pdf',
        'addressProofFileName': f'{loan["_id"]}_address.pdf',
        'bankStatementsFileName': f'{loan["_id"]}_bank.pdf'
    }
    db['home_loans'].update_one({'_id': loan['_id']}, {'$set': update_data})
    print(f"✅ Updated Home Loan {loan['_id']}")

# Update Business Loans
business_loans = db['business_loans'].find({'userId': user_id})
for loan in business_loans:
    update_data = {
        'mobileNumber': '+91 9876543210',
        'phone': '+91 9876543210',
        'address': '789 Business Park, Delhi, NCR 110001',
        'aadharCard': f'/uploads/documents/{loan["_id"]}_aadhar.pdf',
        'panCard': f'/uploads/documents/{loan["_id"]}_pan.pdf',
        'photograph': f'/uploads/documents/{loan["_id"]}_photo.jpg',
        'incomeProof': f'/uploads/documents/{loan["_id"]}_income.pdf',
        'addressProof': f'/uploads/documents/{loan["_id"]}_address.pdf',
        'bankStatements': f'/uploads/documents/{loan["_id"]}_bank.pdf',
        'businessRegistration': f'/uploads/documents/{loan["_id"]}_business_reg.pdf',
        'gstCertificate': f'/uploads/documents/{loan["_id"]}_gst.pdf',
        'aadharCardFileName': f'{loan["_id"]}_aadhar.pdf',
        'panCardFileName': f'{loan["_id"]}_pan.pdf',
        'photographFileName': f'{loan["_id"]}_photo.jpg',
        'incomeProofFileName': f'{loan["_id"]}_income.pdf',
        'addressProofFileName': f'{loan["_id"]}_address.pdf',
        'bankStatementsFileName': f'{loan["_id"]}_bank.pdf'
    }
    db['business_loans'].update_one({'_id': loan['_id']}, {'$set': update_data})
    print(f"✅ Updated Business Loan {loan['_id']}")

# Count updates
personal_count = db['personal_loans'].count_documents({'userId': user_id})
home_count = db['home_loans'].count_documents({'userId': user_id})
business_count = db['business_loans'].count_documents({'userId': user_id})

print(f"\n✅ Update Complete!")
print(f"Personal Loans: {personal_count}")
print(f"Home Loans: {home_count}")
print(f"Business Loans: {business_count}")
print(f"\nAll loans now have phone, address, and document fields!")
