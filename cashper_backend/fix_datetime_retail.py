"""Fix datetime.utcnow() deprecation in retail services"""
import re

# Read file
with open("app/routes/retail_services_routes.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace datetime.utcnow() with datetime.now(timezone.utc)
content = content.replace("datetime.utcnow()", "datetime.now(timezone.utc)")

# Write back
with open("app/routes/retail_services_routes.py", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Fixed all datetime.utcnow() calls in retail_services_routes.py")
