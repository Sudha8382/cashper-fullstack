#!/usr/bin/env python3
"""
Diagnostic script to check insurance counts in database
Run this to see what's actually in the database
"""

import sys
sys.path.insert(0, 'c:\\Users\\ASUS\\Desktop\\payloan\\full_proj\\cashper_backend')

from app.database.db import get_database

def check_insurance_counts():
    db = get_database()
    
    print("\n" + "="*60)
    print("🔍 INSURANCE COUNTS DIAGNOSTIC")
    print("="*60 + "\n")
    
    # Count from each collection
    health = db["health_insurance_inquiries"].count_documents({})
    motor = db["motor_insurance_inquiries"].count_documents({})
    term = db["term_insurance_inquiries"].count_documents({})
    
    total = health + motor + term
    
    print(f"📊 Insurance Collection Counts:")
    print(f"   Health Insurance:  {health}")
    print(f"   Motor Insurance:   {motor}")
    print(f"   Term Insurance:    {term}")
    print(f"   {'─' * 45}")
    print(f"   TOTAL:             {total}")
    
    print(f"\n📈 Expected vs Actual:")
    print(f"   Expected:  50")
    print(f"   Actual:    {total}")
    print(f"   Missing:   {max(0, 50 - total)}")
    
    # Check if there might be a separate policies collection
    print(f"\n🔎 Checking for other insurance collections:")
    collections = db.list_collection_names()
    insurance_related = [c for c in collections if 'insurance' in c.lower() or 'policy' in c.lower()]
    
    for col in insurance_related:
        count = db[col].count_documents({})
        print(f"   {col}: {count} documents")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    try:
        check_insurance_counts()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
