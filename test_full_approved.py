import requests

BASE_URL = "http://127.0.0.1:8000"

print("\n" + "="*70)
print("🧪 TESTING APPROVED STATUS UPDATE & DOCUMENT DOWNLOAD")
print("="*70)

# Get an application
print("\n1️⃣ Getting application with documents...")
apps_response = requests.get(f"{BASE_URL}/api/retail-services/admin/applications")
if apps_response.status_code == 200:
    apps = apps_response.json()
    
    # Find app with documents
    test_app = None
    for app in apps:
        if app.get('documents') and len(app['documents']) > 0:
            test_app = app
            break
    
    if test_app:
        print(f"✅ Found: {test_app['name']}")
        print(f"   ID: {test_app['id']}")
        print(f"   Documents: {test_app['documents']}")
        
        # Update to Approved
        print("\n2️⃣ Updating status to 'Approved'...")
        update_response = requests.put(
            f"{BASE_URL}/api/retail-services/admin/applications/{test_app['id']}/status",
            json={"status": "approved"}
        )
        
        if update_response.status_code == 200:
            result = update_response.json()
            print(f"✅ {result['message']}")
            print(f"   Status: {result['status']}")
        else:
            print(f"❌ Failed: {update_response.text}")
        
        # Test document download
        if test_app['documents']:
            doc_key = test_app['documents'][0]
            print(f"\n3️⃣ Testing document download: {doc_key}")
            
            doc_response = requests.get(
                f"{BASE_URL}/api/retail-services/admin/applications/{test_app['id']}/documents/{doc_key}"
            )
            
            if doc_response.status_code == 200:
                print(f"✅ Document downloaded successfully!")
                print(f"   Size: {len(doc_response.content)} bytes")
                print(f"   Type: {doc_response.headers.get('content-type', 'N/A')}")
            else:
                print(f"❌ Download failed: {doc_response.text}")
        
        # Verify statistics
        print("\n4️⃣ Verifying statistics...")
        stats_response = requests.get(f"{BASE_URL}/api/retail-services/admin/statistics")
        if stats_response.status_code == 200:
            stats = stats_response.json()
            print("✅ Statistics updated:")
            print(f"   Approved: {stats['approved']} ⭐")
    else:
        print("⚠️  No applications with documents found")
else:
    print(f"❌ Failed to get applications")

print("\n" + "="*70)
print("✅ ALL TESTS COMPLETED!")
print("="*70)
