import re

# Read the file
with open('app/routes/business_services.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the user_id line with trailing comma
content = content.replace('"user_id": None  # No authentication,', '"user_id": None,  # No authentication')

# Write back
with open('app/routes/business_services.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed trailing comma issues")
