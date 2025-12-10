import re
import os

# Files to fix
files_to_fix = [
    r"cashper_backend\app\database\repository\motor_insurance_repository.py",
    r"cashper_backend\app\database\repository\term_insurance_repository.py",
    r"cashper_backend\app\routes\health_insurance_routes.py",
    r"cashper_backend\app\routes\motor_insurance_routes.py",
    r"cashper_backend\app\routes\term_insurance_routes.py"
]

def fix_async_in_file(filepath):
    """Remove async/await keywords and fix initialization calls"""
    print(f"\n📝 Fixing: {filepath}")
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove 'async def' and replace with 'def'
    content = re.sub(r'\basync def\b', 'def', content)
    
    # Remove 'await ' keywords
    content = re.sub(r'\bawait\s+', '', content)
    
    # Fix initialization calls in repositories
    if 'repository.py' in filepath:
        # Replace await self.initialize() with collection = self.get_*_collection()
        content = re.sub(
            r'await self\.initialize\(\)\s*\n\s*',
            '',
            content
        )
        content = re.sub(
            r'self\.initialize\(\)\s*\n\s*',
            '',
            content
        )
        
        # Replace self.inquiries_collection with collection = self.get_inquiry_collection()
        # This needs to be done method by method, so let's just remove the calls
        content = re.sub(r'self\.inquiries_collection', 'collection', content)
        content = re.sub(r'self\.applications_collection', 'collection', content)
        
        # Fix cursor.to_list calls
        content = re.sub(r'cursor\.to_list\(length=\d+\)', 'list(cursor)', content)
        content = re.sub(r'cursor\.to_list\(length=None\)', 'list(cursor)', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {filepath}")
        return True
    else:
        print(f"ℹ️  No changes needed in {filepath}")
        return False

def main():
    print("🔧 Starting Async/Await Fix Process...")
    print("=" * 60)
    
    fixed_count = 0
    for file in files_to_fix:
        if fix_async_in_file(file):
            fixed_count += 1
    
    print("\n" + "=" * 60)
    print(f"✨ Fixed {fixed_count} out of {len(files_to_fix)} files")
    print("\n📋 Next Steps:")
    print("1. Restart the FastAPI server")
    print("2. Run: python test_insurance_apis.py")
    print("3. Check for any remaining issues")

if __name__ == "__main__":
    main()
