import pymupdf as fitz
import os

def process_pdf(pdf_path, folder_name):
    doc = fitz.open(pdf_path)
    text_data = []
    image_info = []
    asset_path = os.path.join("assets", folder_name)
    if not os.path.exists(asset_path): 
        os.makedirs(asset_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text()
        text_data.append(f"Page {page_num+1}: {page_text}")
        
        # Get image locations
        image_list = page.get_image_info(hashes=False)
        
        for img_index, img_dict in enumerate(image_list):
            rect = img_dict['bbox']
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]
            top_pos = rect[1]

            # --- ADVANCED FILTERING ---
            # 1. Skip lines: Height agar 40px se kam hai toh woh divider line hai
            # 2. Skip icons/logos: Width agar 150px se kam hai ya top < 70 hai (Header)
            if height < 40 or width < 150 or top_pos < 70:
                continue

            # Capture the exact area (Pixmap prevents tiling/half-image issues)
            pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2, 2))
            
            img_filename = f"{folder_name}_p{page_num+1}_i{img_index}.png"
            img_path = os.path.join(asset_path, img_filename)
            pix.save(img_path)
            
            # Send context to AI to help it map correctly
            image_info.append({
                "path": img_path, 
                "context": page_text[:500].lower().replace("\n", " ")
            })
            
    return "\n".join(text_data), image_info