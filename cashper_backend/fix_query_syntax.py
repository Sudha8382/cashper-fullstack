import re

# Read the file
with open('app/routes/business_services.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix malformed query dictionaries
content = content.replace('query = {"user_id": None  # No authentication}', 'query = {}  # No user filtering')

# Remove "for logged-in user" from docstrings
content = content.replace(' for logged-in user', '')

# Write back
with open('app/routes/business_services.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed query syntax errors")
