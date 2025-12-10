#!/usr/bin/env python3
import sys
sys.path.insert(0, 'cashper_backend')

from app.database.repository.short_term_loan_repository import ShortTermGetInTouchRepository
from app.database.repository import personal_loan_repository

# Check Short Term Loan Inquiries
st_inquiries = ShortTermGetInTouchRepository.get_all()
print(f"\n=== SHORT TERM LOAN INQUIRIES ===")
print(f"Total Count: {len(st_inquiries)}")
if st_inquiries:
    print(f"First Inquiry: {st_inquiries[0]}")
    print(f"\nStatus values in first 5:")
    for i, inquiry in enumerate(st_inquiries[:5]):
        print(f"  {i+1}. Status: {inquiry.get('status', 'MISSING')}, Name: {inquiry.get('fullName', 'N/A')}")

# Check Personal Loan Inquiries
print(f"\n=== PERSONAL LOAN INQUIRIES ===")
try:
    pl_inquiries = personal_loan_repository.get_all_get_in_touch()
    print(f"Total Count: {len(pl_inquiries)}")
    if pl_inquiries:
        print(f"First Inquiry: {pl_inquiries[0]}")
        print(f"\nStatus values in first 5:")
        for i, inquiry in enumerate(pl_inquiries[:5]):
            print(f"  {i+1}. Status: {inquiry.get('status', 'MISSING')}, Name: {inquiry.get('fullName', 'N/A')}")
except Exception as e:
    print(f"Error: {e}")
