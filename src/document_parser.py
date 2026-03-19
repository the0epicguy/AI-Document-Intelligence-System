import fitz
import os
import hashlib


def extract_pdf_content(pdf_path, image_folder):

    doc = fitz.open(pdf_path)

    text = ""
    images = []

    # Track duplicates
    seen_hashes = set()

    os.makedirs(image_folder, exist_ok=True)

    for page_index in range(len(doc)):
        page = doc[page_index]

        text += page.get_text()

        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):

            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            width = base_image["width"]
            height = base_image["height"]

            # FILTER SMALL IMAGES
            if width < 200 or height < 200:
                continue

            # FILTER VERY SMALL FILES
            if len(image_bytes) < 15000:
                continue

            # REMOVE BANNERS / LOGOS
            ratio = width / height
            if ratio > 4 or ratio < 0.25:
                continue

            # CREATE HASH OF IMAGE CONTENT
            image_hash = hashlib.md5(image_bytes).hexdigest()

            # SKIP DUPLICATE IMAGES
            if image_hash in seen_hashes:
                continue

            seen_hashes.add(image_hash)

            image_name = f"{image_folder}/page{page_index}_img{img_index}.png"

            with open(image_name, "wb") as f:
                f.write(image_bytes)

            images.append(image_name)

    return text, images