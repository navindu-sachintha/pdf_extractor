def md_formatter(content):
    markdown_content = ["# Extracted Content\n"]
    
    markdown_content.append("## Text\n")
    markdown_content.append(content["text"] + "\n")
    
    if content["tables"]:
        markdown_content.append("## Tables\n")
        for page_num, table in content["tables"]:
            markdown_content.append(f"### Table from Page {page_num}\n")
            markdown_content.append("| " + " | ".join(str(cell) for cell in table[0]) + " |")
            markdown_content.append("| " + " | ".join(["---"] * len(table[0])) + " |")
            for row in table[1:]:
                markdown_content.append("| " + " | ".join(str(cell) for cell in row) + " |")
            markdown_content.append("\n")
    
    if content["images"]:
        markdown_content.append("## Images\n")
        for img_path in content["images"]:
            markdown_content.append(f"![Extracted Image]({img_path})\n")
    
    return "\n".join(markdown_content)