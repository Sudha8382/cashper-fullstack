"""Fix datetime serialization in all POST endpoints - add .isoformat() after insert_one"""
import re

file_path = "app/routes/business_services.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all POST endpoints that return application_data
# Pattern: after result = collection.insert_one(application_data) and app["_id"] = str(result.inserted_id)
# Add datetime conversion

lines = content.split('\n')
new_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # If this line assigns _id from insert_one result
    if 'application_data["_id"] = str(result.inserted_id)' in line or 'app_data["_id"] = str(result.inserted_id)' in line:
        # Check if next lines already have datetime conversion
        if i + 1 < len(lines) and 'isoformat' not in lines[i + 1]:
            # Add datetime conversions with same indentation
            indent = len(line) - len(line.lstrip())
            spacing = ' ' * indent
            
            # Determine variable name (application_data or app_data)
            var_name = "application_data" if "application_data" in line else "app_data"
            
            new_lines.append(f'{spacing}{var_name}["created_at"] = {var_name}["created_at"].isoformat()')
            new_lines.append(f'{spacing}{var_name}["updated_at"] = {var_name}["updated_at"].isoformat()')
    
    i += 1

content = '\n'.join(new_lines)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Fixed datetime serialization in all POST endpoints")
