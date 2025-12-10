import sys
from pathlib import Path

# Add the parent directory to the path to import app modules
sys.path.append(str(Path(__file__).parent))

from app.database.db import connect_to_mongo, close_mongo_connection
from app.database.repository import financial_repository

# Financial Services Data
FINANCIAL_SERVICES = [
    {
        "category": "Loans",
        "icon": "💰",
        "description": "Flexible loan solutions for all your financial needs",
        "items": [
            {"name": "Short-Term Loan", "path": "/loans/short-term"},
            {"name": "Personal Loan", "path": "/loans/personal"},
            {"name": "Home Loan", "path": "/loans/home"},
            {"name": "Business Loan", "path": "/loans/business"}
        ],
        "features": ["Quick Approval", "Competitive Rates", "Flexible Tenure", "No Hidden Charges"],
        "color": "from-blue-500 to-blue-600",
        "bgColor": "bg-blue-50",
        "textColor": "text-blue-600",
        "link": "/loans",
        "stats": "₹5000+ Disbursed",
        "isActive": True,
        "order": 1
    },
    {
        "category": "Insurance",
        "icon": "🛡️",
        "description": "Comprehensive protection for your life, health, and valuable assets — all in one plan.",
        "items": [
            {"name": "Health Insurance", "path": "/insurance/health"},
            {"name": "Motor Insurance", "path": "/insurance/motor"},
            {"name": "Term Insurance", "path": "/insurance/term"}
        ],
        "features": ["Cashless Treatment", "24/7 Support", "Quick Claims", "Tax Benefits for clients"],
        "color": "from-green-500 to-green-600",
        "bgColor": "bg-green-50",
        "textColor": "text-green-600",
        "link": "/insurance",
        "stats": "10,000+ Policies",
        "isActive": True,
        "order": 2
    },
    {
        "category": "Investments",
        "icon": "📈",
        "description": "Build wealth with expert investment guidance",
        "items": [
            {"name": "Mutual Funds", "path": "/investments/mutual-funds"},
            {"name": "SIP", "path": "/investments/sip"}
        ],
        "features": ["Expert Management", "Diversified Portfolio", "Systematic Approach", "High Returns"],
        "color": "from-purple-500 to-purple-600",
        "bgColor": "bg-purple-50",
        "textColor": "text-purple-600",
        "link": "/investments",
        "stats": "12-18% Returns",
        "isActive": True,
        "order": 3
    },
    {
        "category": "Tax Planning",
        "icon": "📊",
        "description": "Optimize your tax savings and ensure compliance",
        "items": [
            {"name": "Personal Tax Planning", "path": "/tax-planning/personal"},
            {"name": "Business Tax Strategy", "path": "/tax-planning/business"}
        ],
        "features": ["Tax Optimization", "Compliance Support", "Audit Assistance", "Maximize Savings"],
        "color": "from-orange-500 to-orange-600",
        "bgColor": "bg-orange-50",
        "textColor": "text-orange-600",
        "link": "/tax",
        "stats": "Save up to 30%",
        "isActive": True,
        "order": 4
    }
]

# Financial Products Data
FINANCIAL_PRODUCTS = [
    {
        "title": "Short-Term Loan",
        "subtitle": "Quick Cash",
        "description": "Get immediate financial assistance for urgent needs with our short-term loans up to ₹5 lakhs.",
        "features": ["Same day approval", "No collateral required", "Flexible repayment"],
        "amount": "Up to ₹2L",
        "type": "loan",
        "color": "from-blue-500 to-blue-600",
        "bgColor": "bg-blue-50",
        "textColor": "text-blue-600",
        "link": "/loans/short-term#apply-form",
        "interestRate": "1% / day",
        "rateLabel": "Interest Rate up to",
        "isActive": True,
        "isFeatured": True,
        "order": 1
    },
    {
        "title": "Personal Loan",
        "subtitle": "Quick Approval",
        "description": "Get instant personal loans up to ₹50 lakhs with competitive interest rates starting from 10.99% p.a.",
        "features": ["Instant approval", "No collateral required", "Flexible tenure"],
        "interestRate": "10.99%",
        "amount": "Up to ₹50L",
        "type": "loan",
        "color": "from-green-500 to-green-600",
        "bgColor": "bg-green-50",
        "textColor": "text-green-600",
        "link": "/loans/personal#apply-form",
        "rateLabel": "Interest Rate",
        "isActive": True,
        "isFeatured": True,
        "order": 2
    },
    {
        "title": "Home Loan",
        "subtitle": "Dream Home",
        "description": "Make your dream home a reality with our home loans starting from 8.50% p.a. with flexible EMI options.",
        "features": ["Low interest rates", "Long tenure up to 30 years", "Quick processing"],
        "interestRate": "8.50%",
        "amount": "Up to ₹5Cr",
        "type": "loan",
        "color": "from-purple-500 to-purple-600",
        "bgColor": "bg-purple-50",
        "textColor": "text-purple-600",
        "link": "/loans/home#apply-form",
        "rateLabel": "Interest Rate",
        "isActive": True,
        "isFeatured": True,
        "order": 3
    },
    {
        "title": "Business Loan",
        "subtitle": "Grow Your Business",
        "description": "Fuel your business growth with our business loans up to ₹2 crores with flexible repayment options.",
        "features": ["Quick disbursal", "Competitive rates", "No prepayment penalty"],
        "interestRate": "12%",
        "amount": "Up to ₹2Cr",
        "type": "loan",
        "color": "from-indigo-500 to-indigo-600",
        "bgColor": "bg-indigo-50",
        "textColor": "text-indigo-600",
        "link": "/loans/business#apply-form",
        "rateLabel": "Interest Rate",
        "isActive": True,
        "isFeatured": False,
        "order": 4
    },
    {
        "title": "Health Insurance",
        "subtitle": "Comprehensive Coverage",
        "description": "Protect your family with comprehensive health insurance coverage up to ₹1 crore with cashless treatment.",
        "features": ["Cashless treatment", "Pre & post hospitalization", "No claim bonus"],
        "interestRate": "₹500/month",
        "amount": "Up to ₹2Cr",
        "rateLabel": "Starting From",
        "type": "insurance",
        "color": "from-red-500 to-red-600",
        "bgColor": "bg-red-50",
        "textColor": "text-red-600",
        "link": "/insurance/health#apply-form",
        "isActive": True,
        "isFeatured": True,
        "order": 5
    },
    {
        "title": "Motor Insurance",
        "subtitle": "Protect Your Vehicle",
        "description": "Comprehensive motor insurance with 24/7 roadside assistance and quick claim settlement.",
        "features": ["24/7 assistance", "Quick claims", "Zero depreciation"],
        "interestRate": "₹5,000/year",
        "amount": "Full Coverage",
        "rateLabel": "Starting From",
        "type": "insurance",
        "color": "from-yellow-500 to-yellow-600",
        "bgColor": "bg-yellow-50",
        "textColor": "text-yellow-600",
        "link": "/insurance/motor#apply-form",
        "isActive": True,
        "isFeatured": False,
        "order": 6
    },
    {
        "title": "Term Insurance",
        "subtitle": "Life Protection",
        "description": "Secure your family's future with our term life insurance plans offering high coverage at affordable premiums.",
        "features": ["High coverage", "Affordable premiums", "Tax benefits"],
        "interestRate": "₹1,000/month",
        "amount": "Up to ₹1Cr",
        "rateLabel": "Starting From",
        "type": "insurance",
        "color": "from-pink-500 to-pink-600",
        "bgColor": "bg-pink-50",
        "textColor": "text-pink-600",
        "link": "/insurance/term#apply-form",
        "isActive": True,
        "isFeatured": False,
        "order": 7
    },
    {
        "title": "Mutual Funds",
        "subtitle": "Professional Management",
        "description": "Invest in professionally managed mutual funds with expert guidance and diversified portfolios.",
        "features": ["Expert management", "Diversified portfolio", "Liquidity"],
        "interestRate": "12-18%",
        "amount": " ",
        "rateLabel": "Expected Returns as per Market",
        "type": "investment",
        "color": "from-teal-500 to-teal-600",
        "bgColor": "bg-teal-50",
        "textColor": "text-teal-600",
        "link": "/investments/mutual-funds#apply-form",
        "isActive": True,
        "isFeatured": True,
        "order": 8
    },
    {
        "title": "SIP Investment",
        "subtitle": "Start Small, Dream Big",
        "description": "Start your investment journey with SIPs starting from just ₹500 per month and build wealth over time.",
        "features": ["Start from ₹500", "Systematic approach", "Professional management"],
        "interestRate": "12-15%",
        "amount": "Expected Returns",
        "rateLabel": "Expected Returns",
        "type": "investment",
        "color": "from-orange-500 to-orange-600",
        "bgColor": "bg-orange-50",
        "textColor": "text-orange-600",
        "link": "/investments/sip#apply-form",
        "isActive": True,
        "isFeatured": False,
        "order": 9
    },
    {
        "title": "Personal Tax Planning",
        "subtitle": "Maximize Savings",
        "description": "Optimize your tax savings with personalized tax planning strategies and investment recommendations.",
        "features": ["Tax optimization", "Investment advice", "Compliance support"],
        "interestRate": "Save up to 30%",
        "amount": "Tax Benefits",
        "rateLabel": "Tax Benefits",
        "type": "tax",
        "color": "from-cyan-500 to-cyan-600",
        "bgColor": "bg-cyan-50",
        "textColor": "text-cyan-600",
        "link": "/services/tax-planning#apply-form",
        "isActive": True,
        "isFeatured": False,
        "order": 10
    },
    {
        "title": "Business Tax Strategy",
        "subtitle": "Corporate Solutions",
        "description": "Comprehensive tax planning solutions for businesses to minimize tax liability and maximize profits.",
        "features": ["Corporate tax planning", "Compliance management", "Audit support"],
        "interestRate": "Save up to 25%",
        "amount": "Tax Benefits",
        "rateLabel": "Tax Benefits",
        "type": "tax",
        "color": "from-emerald-500 to-emerald-600",
        "bgColor": "bg-emerald-50",
        "textColor": "text-emerald-600",
        "link": "/tax-planning/business#apply-form",
        "isActive": True,
        "isFeatured": False,
        "order": 11
    }
]

def seed_financial_data():
    """Seed the database with financial services and products data"""
    print("[*] Starting database seeding...")
    
    # Connect to MongoDB
    connect_to_mongo()
    print("[+] Connected to MongoDB")
    
    try:
        # Seed Financial Services
        print("\n[*] Seeding Financial Services...")
        services_added = 0
        services_skipped = 0
        
        for service in FINANCIAL_SERVICES:
            try:
                existing = financial_repository.get_financial_service_by_category(service["category"])
                if existing:
                    print(f"[-] Skipping '{service['category']}' - already exists")
                    services_skipped += 1
                else:
                    financial_repository.create_financial_service(service)
                    print(f"[+] Added service: {service['category']}")
                    services_added += 1
            except Exception as e:
                print(f"[!] Error adding service '{service['category']}': {str(e)}")
        
        print(f"\n[*] Services Summary: {services_added} added, {services_skipped} skipped")
        
        # Seed Financial Products
        print("\n[*] Seeding Financial Products...")
        products_added = 0
        
        for product in FINANCIAL_PRODUCTS:
            try:
                financial_repository.create_financial_product(product)
                print(f"[+] Added product: {product['title']}")
                products_added += 1
            except Exception as e:
                print(f"[!] Error adding product '{product['title']}': {str(e)}")
        
        print(f"\n[*] Products Summary: {products_added} added")
        
        # Get statistics
        print("\n[*] Getting Statistics...")
        stats = financial_repository.get_products_by_type_stats()
        print(f"Products by type: {stats}")
        
        print("\n[+] Database seeding completed successfully!")
        
    except Exception as e:
        print(f"\n[!] Error during seeding: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        close_mongo_connection()
        print("[*] Disconnected from MongoDB")

if __name__ == "__main__":
    seed_financial_data()
