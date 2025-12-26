from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

# Check all collections
collections = ['tds_services_applications', 'gst_services_applications', 'legal_advice_applications', 
               'provident_fund_services_applications', 'payroll_services_applications', 
               'accounting_bookkeeping_applications']

for col_name in collections:
    col = db[col_name]
    count = col.count_documents({})
    print(f'{col_name}: {count} documents')
    if count > 0:
        sample = col.find_one()
        print(f'  Sample ID: {sample.get("application_id")}')
        print(f'  Sample Status: {sample.get("status")}')
