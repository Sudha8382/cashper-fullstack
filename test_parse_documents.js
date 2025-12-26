// Test the document parsing logic

const parseDocuments = (documentsStr) => {
  const docs = {
    aadhar: '',
    pan: '',
    bankStatement: '',
    salarySlip: '',
    photo: ''
  };

  if (!documentsStr || typeof documentsStr !== 'string') {
    return docs;
  }

  // Parse "aadhar: /path/to/file.jpg, pan: /path/to/file.png, ..."
  const pairs = documentsStr.split(',').map(pair => pair.trim());
  pairs.forEach(pair => {
    const [key, value] = pair.split(':').map(s => s.trim());
    if (key && value && docs.hasOwnProperty(key)) {
      docs[key] = value;
    }
  });

  return docs;
};

// Test with the actual response
const testDocString = "aadhar: /uploads/documents/a1ef376045be4c6baafa81be3d0897e7.jpeg, pan: /uploads/documents/251d49572a2c4cb4aaaf3181feaa4bb7.png, bankStatement: /uploads/documents/a4d2747d7a84438fb86324ffa20f6d76.pdf, salarySlip: /uploads/documents/35199b2382b643e8809a348b9313572c.pdf, photo: /uploads/documents/9cdfc3ea1750467cbcb0dedd311920c6.jpeg";

const result = parseDocuments(testDocString);

console.log("Parsed Documents:");
console.log(JSON.stringify(result, null, 2));

console.log("\n✅ Test Results:");
console.log("Aadhar:", result.aadhar ? "✓ Found" : "✗ Missing");
console.log("PAN:", result.pan ? "✓ Found" : "✗ Missing");
console.log("Bank Statement:", result.bankStatement ? "✓ Found" : "✗ Missing");
console.log("Salary Slip:", result.salarySlip ? "✓ Found" : "✗ Missing");
console.log("Photo:", result.photo ? "✓ Found" : "✗ Missing");
