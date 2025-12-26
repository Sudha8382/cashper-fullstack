import re

# Read the file
with open('app/routes/business_services.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove verify_token dependencies from function signatures
content = re.sub(r',\s*\n\s*user_data:\s*dict\s*=\s*Depends\(verify_token\)', '', content)

# Replace user_id assignments
content = content.replace('"user_id": user_data.get("user_id")', '"user_id": None  # No authentication')

# Write back
with open('app/routes/business_services.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed authentication issues in business_services.py")
