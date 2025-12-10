/**
 * Quick Login Test Script
 * Run this in browser console to test admin login
 * 
 * Usage:
 * 1. Open browser console (F12)
 * 2. Copy and paste this entire script
 * 3. It will attempt to login and show results
 */

async function testAdminLogin() {
  console.log('🔐 Testing Admin Login...\n');
  
  const credentials = {
    email: 'sudha@123gmail.com',
    password: 'Sudha@123'
  };
  
  try {
    console.log('📤 Sending login request...');
    const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(credentials)
    });
    
    const data = await response.json();
    
    if (response.ok) {
      console.log('✅ LOGIN SUCCESSFUL!\n');
      console.log('User Info:', data.user);
      console.log('Token:', data.access_token.substring(0, 50) + '...');
      console.log('Is Admin:', data.user.isAdmin);
      
      // Store in localStorage
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('user', JSON.stringify(data.user));
      
      console.log('\n✅ Token and user data saved to localStorage!');
      console.log('🎉 You can now access the Admin Panel!');
      console.log('\n📝 Stored items:');
      console.log('  - access_token:', localStorage.getItem('access_token').substring(0, 30) + '...');
      console.log('  - user:', JSON.parse(localStorage.getItem('user')).email);
      
      return {
        success: true,
        token: data.access_token,
        user: data.user
      };
    } else {
      console.error('❌ LOGIN FAILED!');
      console.error('Status:', response.status);
      console.error('Error:', data.detail || data.message);
      
      return {
        success: false,
        error: data.detail || data.message
      };
    }
  } catch (error) {
    console.error('❌ NETWORK ERROR!');
    console.error('Error:', error.message);
    console.error('\n⚠️  Make sure backend is running on http://127.0.0.1:8000');
    
    return {
      success: false,
      error: error.message
    };
  }
}

// Auto-run the test
testAdminLogin().then(result => {
  if (result.success) {
    console.log('\n🔄 Reloading page in 2 seconds...');
    setTimeout(() => {
      window.location.reload();
    }, 2000);
  }
});
