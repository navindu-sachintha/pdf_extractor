import pdfplumber
import os
from pathlib import Path

def extract_content(pdf_path:str, output_image_dir: str = "images"):
    content = {
        "text": "",
        "tables": [],
        "images": []
    }

    os.makedirs(output_image_dir, exist_ok=True)

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            content["text"] += f"\n## Page {page_num}\n\n{text}\n"
            
            tables = page.extract_tables()
            content["tables"].extend([(page_num, table) for table in tables])
            
            for img_idx, img in enumerate(page.images):
                img_bytes = img["stream"].get_data()
                img_ext = img.get("ext", "png")
                img_filename = f"{output_image_dir}/page_{page_num}_img_{img_idx}.{img_ext}"
                with open(img_filename, "wb") as f:
                    f.write(img_bytes)
                content["images"].append(img_filename)
    
    return content