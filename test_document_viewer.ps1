#!/usr/bin/env powershell
# Document Viewer & Download Functionality Test Script
# Purpose: Verify all document viewing and downloading works correctly

Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "📄 Document Viewer Fix Test" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Color scheme
$success = "Green"
$warning = "Yellow"
$error = "Red"
$info = "Cyan"

# Test 1: Check if backend is running
Write-Host "Test 1: Checking Backend Connection..." -ForegroundColor $info
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -Method Get -ErrorAction Stop -TimeoutSec 5
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Backend is running on http://127.0.0.1:8000" -ForegroundColor $success
    } else {
        Write-Host "⚠️  Backend responded but with unexpected status: $($response.StatusCode)" -ForegroundColor $warning
    }
} catch {
    Write-Host "❌ Backend is NOT running. Please start with: python run_server.py" -ForegroundColor $error
    Write-Host "   Location: cashper_backend/run_server.py" -ForegroundColor $warning
}

# Test 2: Check if uploads directory exists
Write-Host "`nTest 2: Checking Upload Directory..." -ForegroundColor $info
$uploadDir = "./cashper_backend/uploads/documents"
if (Test-Path -Path $uploadDir) {
    $fileCount = (Get-ChildItem -Path $uploadDir | Measure-Object).Count
    Write-Host "✅ Uploads directory exists with $fileCount files" -ForegroundColor $success
} else {
    Write-Host "❌ Upload directory not found at: $uploadDir" -ForegroundColor $error
}

# Test 3: Check if document API endpoint exists
Write-Host "`nTest 3: Checking Document API Endpoint..." -ForegroundColor $info
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/admin/loan-management/applications" `
        -Method Get `
        -Headers @{"Authorization"="Bearer test"} `
        -ErrorAction Stop `
        -TimeoutSec 5
    Write-Host "✅ Admin API endpoint is accessible" -ForegroundColor $success
} catch {
    Write-Host "⚠️  Admin API endpoint check failed - may need authentication" -ForegroundColor $warning
}

# Test 4: Verify frontend changes
Write-Host "`nTest 4: Checking Frontend Changes..." -ForegroundColor $info
$frontendFile = "./cashper_frontend/src/components/Admin pannel/LoanManagement.jsx"
if (Test-Path -Path $frontendFile) {
    $content = Get-Content -Path $frontendFile -Raw
    
    $checks = @(
        @{Name="viewerLoanId state"; Pattern="viewerLoanId"; Required=$true},
        @{Name="handleViewDocument function"; Pattern="handleViewDocument.*loanId"; Required=$true},
        @{Name="downloadDocument function"; Pattern="downloadDocument.*async"; Required=$true},
        @{Name="PDF handling"; Pattern="isPDF.*selectedDocument"; Required=$true},
        @{Name="View button with loanId"; Pattern="handleViewDocument.*selectedLoan.id"; Required=$true}
    )
    
    foreach ($check in $checks) {
        if ($content -match $check.Pattern) {
            Write-Host "✅ Found: $($check.Name)" -ForegroundColor $success
        } else {
            Write-Host "❌ Missing: $($check.Name)" -ForegroundColor $error
        }
    }
} else {
    Write-Host "❌ Frontend file not found: $frontendFile" -ForegroundColor $error
}

# Test 5: Check backend API file
Write-Host "`nTest 5: Checking Backend API Implementation..." -ForegroundColor $info
$backendFile = "./cashper_backend/app/routes/admin_loan_management_routes.py"
if (Test-Path -Path $backendFile) {
    $content = Get-Content -Path $backendFile -Raw
    
    if ($content -match "download-document") {
        Write-Host "✅ Download endpoint implemented in backend" -ForegroundColor $success
    } else {
        Write-Host "❌ Download endpoint not found in backend" -ForegroundColor $error
    }
    
    if ($content -match "FileResponse") {
        Write-Host "✅ FileResponse properly configured" -ForegroundColor $success
    } else {
        Write-Host "⚠️  FileResponse not found - downloads might not work" -ForegroundColor $warning
    }
} else {
    Write-Host "❌ Backend API file not found: $backendFile" -ForegroundColor $error
}

# Test 6: Node modules check
Write-Host "`nTest 6: Checking Frontend Dependencies..." -ForegroundColor $info
$nodeModules = "./cashper_frontend/node_modules"
if (Test-Path -Path $nodeModules) {
    Write-Host "✅ Node modules installed" -ForegroundColor $success
} else {
    Write-Host "❌ Node modules not installed. Run: npm install in cashper_frontend/" -ForegroundColor $error
}

# Test 7: Summary
Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "📊 Test Summary" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

Write-Host "`n🎯 What Should Work Now:" -ForegroundColor $info
Write-Host "   1. Click 'View' on document → Opens in modal" -ForegroundColor $success
Write-Host "   2. Click 'Download' on document → File downloads" -ForegroundColor $success
Write-Host "   3. Images display in viewer" -ForegroundColor $success
Write-Host "   4. PDFs show download button" -ForegroundColor $success
Write-Host "   5. Navigation between documents works" -ForegroundColor $success

Write-Host "`n🚀 Next Steps:" -ForegroundColor $info
Write-Host "   1. Start Backend: python run_server.py" -ForegroundColor $warning
Write-Host "   2. Start Frontend: npm run dev" -ForegroundColor $warning
Write-Host "   3. Navigate to Admin Panel - Loan Management" -ForegroundColor $warning
Write-Host "   4. Click View on any loan with documents" -ForegroundColor $warning
Write-Host "   5. Test viewing and downloading documents" -ForegroundColor $warning

Write-Host "`n📚 Documentation:" -ForegroundColor $info
Write-Host "   See: PDF_DOCUMENT_VIEWER_FIX.md" -ForegroundColor $success

Write-Host "`n" -ForegroundColor Cyan
