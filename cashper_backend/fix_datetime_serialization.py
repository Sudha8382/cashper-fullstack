"""Fix datetime serialization in all GET endpoints"""
import re

file_path = "app/routes/business_services.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix GET endpoints - convert datetime to ISO format
pattern = r'(for app in applications:\s+app\["_id"\] = str\(app\["_id"\]\))'
replacement = r'''for app in applications:
            app["_id"] = str(app["_id"])
            if "created_at" in app and hasattr(app["created_at"], "isoformat"):
                app["created_at"] = app["created_at"].isoformat()
            if "updated_at" in app and hasattr(app["updated_at"], "isoformat"):
                app["updated_at"] = app["updated_at"].isoformat()'''

content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Fixed datetime serialization in GET endpoints")
