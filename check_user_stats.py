from app.database.db import get_database

db = get_database()

# Get sample users
users = list(db['users'].find({}, {'_id': 1, 'fullName': 1, 'isActive': 1, 'isSuspended': 1}).limit(5))

print("Sample Users:")
for user in users:
    print(f"  User: {user.get('fullName', 'N/A')}, isActive: {user.get('isActive')}, isSuspended: {user.get('isSuspended')}")

# Count stats
total_all = db['users'].count_documents({})
active = db['users'].count_documents({'isActive': True, 'isSuspended': False})
inactive = db['users'].count_documents({'isActive': False})
suspended = db['users'].count_documents({'isSuspended': True})

print(f"\nStats:")
print(f"  Total Users: {total_all}")
print(f"  Active (isActive=True, isSuspended=False): {active}")
print(f"  Inactive (isActive=False): {inactive}")
print(f"  Suspended (isSuspended=True): {suspended}")

# Also check the breakdown
active_true = db['users'].count_documents({'isActive': True})
active_false = db['users'].count_documents({'isActive': False})
suspended_true = db['users'].count_documents({'isSuspended': True})
suspended_false = db['users'].count_documents({'isSuspended': False})

print(f"\nBreakdown:")
print(f"  isActive=True: {active_true}")
print(f"  isActive=False: {active_false}")
print(f"  isSuspended=True: {suspended_true}")
print(f"  isSuspended=False: {suspended_false}")
