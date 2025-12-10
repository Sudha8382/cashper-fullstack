# Service File Enhancement Script
# This script documents the pattern used for all service file enhancements

$serviceFiles = @{
    "GSTServices.jsx" = @{
        icons = @("FaFileInvoice", "FaPercentage", "FaMoneyBillWave", "FaCalculator")
        heroTitle = "GST Services & <span>Compliance</span>"
        heroDesc = "Complete GST registration, filing, and compliance services. Expert assistance for all GST-related requirements."
        imageUrl = "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&h=600&fit=crop"
    }
    "RegisterCompany.jsx" = @{
        icons = @("FaBuilding", "FaUsers", "FaFileContract", "FaCertificate")
        heroTitle = "Company <span>Registration</span>"
        heroDesc = "Register your business with expert guidance. All types of company formation services."
        imageUrl = "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&h=600&fit=crop"
    }
    "ApplyIndividualPAN.jsx" = @{
        icons = @("FaIdCard", "FaUser", "FaCheckCircle", "FaClock")
        heroTitle = "Apply for <span>Individual PAN</span>"
        heroDesc = "Quick and hassle-free PAN card application. Get your PAN in just 15 days."
        imageUrl = "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=600&h=600&fit=crop"
    }
    "ApplyHUFPAN.jsx" = @{
        icons = @("FaUsers", "FaIdCard", "FaHome", "FaFileContract")
        heroTitle = "HUF PAN <span>Application</span>"
        heroDesc = "Apply for Hindu Undivided Family PAN. Tax planning benefits for your family."
        imageUrl = "https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=600&h=600&fit=crop"
    }
    "FinancialPlanning.jsx" = @{
        icons = @("FaChartLine", "FaPiggyBank", "FaShieldAlt", "FaHome")
        heroTitle = "Financial <span>Planning</span>"
        heroDesc = "Comprehensive financial planning and advisory services for wealth creation and protection."
        imageUrl = "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=600&h=600&fit=crop"
    }
    "TaxAudit.jsx" = @{
        icons = @("FaSearch", "FaFileInvoice", "FaCheckCircle", "FaBalanceScale")
        heroTitle = "Tax <span>Audit Services</span>"
        heroDesc = "Professional tax audit services under Section 44AB. Expert CA assistance for compliance."
        imageUrl = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=600&fit=crop"
    }
    "PayrollServices.jsx" = @{
        icons = @("FaMoneyBillWave", "FaUsers", "FaCalculator", "FaClock")
        heroTitle = "Payroll <span>Services</span>"
        heroDesc = "Complete payroll processing and statutory compliance. Hassle-free employee management."
        imageUrl = "https://images.unsplash.com/photo-1554224154-22dec7ec8818?w=600&h=600&fit=crop"
    }
    "TDSServices.jsx" = @{
        icons = @("FaPercentage", "FaFileInvoice", "FaCalendarAlt", "FaCheckCircle")
        heroTitle = "TDS <span>Services</span>"
        heroDesc = "End-to-end TDS compliance from registration to return filing. Expert TDS management."
        imageUrl = "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=600&h=600&fit=crop"
    }
    "ReviseITR.jsx" = @{
        icons = @("FaEdit", "FaUndo", "FaCheckCircle", "FaClock")
        heroTitle = "Revise Your <span>ITR</span>"
        heroDesc = "Correct errors in your filed ITR. Expert assistance for revised return filing."
        imageUrl = "https://images.unsplash.com/photo-1554224154-22dec7ec8818?w=600&h=600&fit=crop"
    }
    "ReplyITRNotice.jsx" = @{
        icons = @("FaEnvelope", "FaExclamationTriangle", "FaReply", "FaShieldAlt")
        heroTitle = "Reply to <span>ITR Notice</span>"
        heroDesc = "Expert response to Income Tax notices. Professional handling of all notice types."
        imageUrl = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=600&fit=crop"
    }
    "LegalAdvice.jsx" = @{
        icons = @("FaBalanceScale", "FaGavel", "FaFileContract", "FaHandshake")
        heroTitle = "Legal <span>Advisory</span>"
        heroDesc = "Comprehensive legal services for businesses. Expert corporate and commercial law advice."
        imageUrl = "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=600&h=600&fit=crop"
    }
    "ComplianceNewCompany.jsx" = @{
        icons = @("FaFileAlt", "FaCalendarCheck", "FaBuilding", "FaCheckCircle")
        heroTitle = "Company <span>Compliance</span>"
        heroDesc = "Complete compliance management for new companies. Annual ROC, IT, and GST filings."
        imageUrl = "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&h=600&fit=crop"
    }
    "ProvidentFundServices.jsx" = @{
        icons = @("FaPiggyBank", "FaUsers", "FaFileInvoice", "FaCheckCircle")
        heroTitle = "Provident Fund <span>Services</span>"
        heroDesc = "Complete PF and ESI compliance. From registration to monthly returns filing."
        imageUrl = "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=600&h=600&fit=crop"
    }
    "WithdrawPF.jsx" = @{
        icons = @("FaMoneyBillWave", "FaDownload", "FaCheckCircle", "FaClock")
        heroTitle = "PF <span>Withdrawal</span>"
        heroDesc = "Easy PF withdrawal assistance. Full settlement, partial withdrawal, and transfer services."
        imageUrl = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?w=600&h=600&fit=crop"
    }
}

Write-Host "Service File Enhancement Pattern Documented"
Write-Host "Total Files: $($serviceFiles.Count)"
Write-Host ""
Write-Host "Each file follows this structure:"
Write-Host "1. Hero Section with gradient background"
Write-Host "2. Feature Cards (4-column grid)"
Write-Host "3. Main Content with icons"
Write-Host "4. Benefits/Process Section"
Write-Host "5. CTA Section"
Write-Host ""
Write-Host "All files are fully responsive and use consistent green color scheme."
