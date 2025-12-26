# Start backend server with correct configuration
Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "🚀 Starting Cashper Backend Server..." -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "📡 Server URL: http://127.0.0.1:8000" -ForegroundColor Yellow
Write-Host "📚 Swagger UI: http://127.0.0.1:8000/docs" -ForegroundColor Yellow
Write-Host "============================================================`n" -ForegroundColor Cyan

Set-Location "C:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend"
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
