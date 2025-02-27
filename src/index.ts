const {PdfDataParser} = require('pdf-data-parser');

const pdfDataParser = new PdfDataParser({url: 'FG.pdf'});

async function main() {
  const rows = await pdfDataParser.parse();
  console.log(rows);
}

main().catch(console.error);
