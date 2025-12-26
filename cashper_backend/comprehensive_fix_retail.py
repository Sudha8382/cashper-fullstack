"""Comprehensive fix for retail services - ensure no timezone references"""

import re

# Read file
with open("app/routes/retail_services_routes.py", "r", encoding="utf-8") as f:
    content = f.read()

# Show current imports
print("Current datetime import:")
for line in content.split("\n")[:10]:
    if "datetime" in line:
        print(f"  {line}")

# Remove timezone from imports if present
content = re.sub(r'from datetime import datetime, timezone', 'from datetime import datetime', content)
content = re.sub(r'from datetime import timezone, datetime', 'from datetime import datetime', content)

# Replace all timezone.utc references
content = content.replace('datetime.now(timezone.utc)', 'datetime.now()')
content = content.replace('datetime.utcnow()', 'datetime.now()')

# Write back
with open("app/routes/retail_services_routes.py", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ Fixed all datetime references")
print(f"✅ Total lines: {len(content.splitlines())}")

# Verify no timezone left
if 'timezone' in content:
    print("\n⚠ WARNING: 'timezone' still found in file!")
    for i, line in enumerate(content.split("\n"), 1):
        if 'timezone' in line and not line.strip().startswith('#'):
            print(f"  Line {i}: {line}")
else:
    print("✅ No timezone references found")
