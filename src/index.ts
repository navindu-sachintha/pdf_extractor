const {PdfDataParser} = require('pdf-data-parser');
const fs = require('fs');

const pdfDataParser = new PdfDataParser({url: 'FG.pdf'});

function convertToCSV(rows: any[]) {
  return rows
    .map(row =>
      row
        .map((value: null | undefined) => {
          if (value === null || value === undefined) {
            return '';
          }
          const val = String(value);
          if (val.includes(',') || val.includes('"') || val.includes('\n')) {
            return `"${val.replace(/"/g, '""')}"`;
          }
          return val;
        })
        .join(','),
    )
    .join('\n');
}

async function main() {
  const rows = await pdfDataParser.parse();
  console.log(rows);

  const csvContent = convertToCSV(rows);
  fs.writeFileSync('output.csv', csvContent);
  console.log('CSV file has been created successfully at output.csv');
}

main().catch(console.error);
