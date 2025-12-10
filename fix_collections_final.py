import re

files = [
    r"cashper_backend\app\database\repository\term_insurance_repository.py",
]

for filepath in files:
    print(f"Fixing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Fix simple collection usages in inquiry methods
    # Before: cursor = collection.find(...)
    # After: collection = self.get_inquiry_collection()\n        cursor = collection.find(...)
    
    # For get_inquiry_by_id
    content = re.sub(
        r'(def get_inquiry_by_id.*?\n.*?""".*?""")\n(\s+)inquiry = collection\.find',
        r'\1\n\2collection = self.get_inquiry_collection()\n\2inquiry = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For get_all_inquiries
    content = re.sub(
        r'(def get_all_inquiries.*?""".*?""")\n(\s+)cursor = collection\.find',
        r'\1\n\2collection = self.get_inquiry_collection()\n\2cursor = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For update_inquiry_status
    content = re.sub(
        r'(update_data\["remarks"\] = remarks\s*\n)(\s+)result = collection\.update_one',
        r'\1\2collection = self.get_inquiry_collection()\n\2result = collection.update_one',
        content
    )
    
    # For get_inquiries_by_status
    content = re.sub(
        r'(def get_inquiries_by_status.*?""".*?""")\n(\s+)cursor = collection\.find',
        r'\1\n\2collection = self.get_inquiry_collection()\n\2cursor = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Fix application methods
    # For create_application
    content = re.sub(
        r'(def create_application.*?""".*?""")\n(\s+)application_dict',
        r'\1\n\2collection = self.get_application_collection()\n\2application_dict',
        content,
        flags=re.DOTALL
    )
    
    # For get_application_by_id
    content = re.sub(
        r'(def get_application_by_id.*?""".*?""")\n(\s+)application = collection\.find',
        r'\1\n\2collection = self.get_application_collection()\n\2application = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For get_application_by_number
    content = re.sub(
        r'(def get_application_by_number.*?""".*?""")\n(\s+)application = collection\.find',
        r'\1\n\2collection = self.get_application_collection()\n\2application = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For get_all_applications
    content = re.sub(
        r'(def get_all_applications.*?""".*?""")\n(\s+)cursor = collection\.find',
        r'\1\n\2collection = self.get_application_collection()\n\2cursor = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For update_application_status
    content = re.sub(
        r'(def update_application_status.*?update_data\["remarks"\] = remarks\s*\n)(\s+)result = collection\.update',
        r'\1\2collection = self.get_application_collection()\n\2result = collection.update',
        content,
        flags=re.DOTALL
    )
    
    # For get_applications_by_status
    content = re.sub(
        r'(def get_applications_by_status.*?""".*?""")\n(\s+)cursor = collection\.find',
        r'\1\n\2collection = self.get_application_collection()\n\2cursor = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For get_applications_by_email
    content = re.sub(
        r'(def get_applications_by_email.*?""".*?""")\n(\s+)cursor = collection\.find',
        r'\1\n\2collection = self.get_application_collection()\n\2cursor = collection.find',
        content,
        flags=re.DOTALL
    )
    
    # For get_statistics - replace all collection references with proper collection variables
    content = re.sub(
        r'(def get_statistics.*?""".*?""")\n(\s+)# Inquiry',
        r'\1\n\2inquiry_collection = self.get_inquiry_collection()\n\2application_collection = self.get_application_collection()\n\2\n\2# Inquiry',
        content,
        flags=re.DOTALL
    )
    
    # Replace collection.count_documents in statistics
    content = re.sub(r'(\s+total_inquiries = )collection\.count', r'\1inquiry_collection.count', content)
    content = re.sub(r'(\s+pending_inquiries = )collection\.count', r'\1inquiry_collection.count', content)
    content = re.sub(r'(\s+contacted_inquiries = )collection\.count', r'\1inquiry_collection.count', content)
    content = re.sub(r'(\s+converted_inquiries = )collection\.count', r'\1inquiry_collection.count', content)
    content = re.sub(r'(\s+total_applications = )collection\.count', r'\1application_collection.count', content)
    content = re.sub(r'(\s+submitted_applications = )collection\.count', r'\1application_collection.count', content)
    content = re.sub(r'(\s+under_review_applications = )collection\.count', r'\1application_collection.count', content)
    content = re.sub(r'(\s+approved_applications = )collection\.count', r'\1application_collection.count', content)
    content = re.sub(r'(\s+policy_issued = )collection\.count', r'\1application_collection.count', content)
    
    # Fix cursor.to_list
    content = re.sub(r'cursor\.to_list\(length=\w+\)', 'list(cursor)', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed {filepath}")

print("\n✨ All files fixed!")
