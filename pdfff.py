from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import io
from concurrent.futures import ThreadPoolExecutor
from configs import base


async def prepare_watermark(watermark_image_path, watermark_scale, watermark_angle, watermark_opacity, page_width):
    # Загрузка и подготовка водяного знака
    watermark_img = Image.open(watermark_image_path).convert("RGBA")
    original_watermark_width, original_watermark_height = watermark_img.size

    # Масштабирование и поворот водяного знака
    watermark_width = int(page_width * watermark_scale)
    watermark_height = int(original_watermark_height * (watermark_width / original_watermark_width))
    resized_watermark = watermark_img.resize((watermark_width, watermark_height), Image.LANCZOS)
    rotated_watermark = resized_watermark.rotate(watermark_angle, expand=True)

    # Настройка прозрачности водяного знака
    transparent_watermark = Image.new("RGBA", rotated_watermark.size)
    for x in range(rotated_watermark.width):
        for y in range(rotated_watermark.height):
            r, g, b, alpha = rotated_watermark.getpixel((x, y))
            transparent_watermark.putpixel((x, y), (r, g, b, int(alpha * watermark_opacity)))

    return transparent_watermark


def process_page(page, watermark):
    x = (page.width - watermark.width) // 2
    y = (page.height - watermark.height) // 2

    combined = Image.new("RGBA", page.size)
    combined.paste(page.convert("RGBA"), (0, 0))
    combined.paste(watermark, (x, y), mask=watermark)

    combined_stream = io.BytesIO()
    combined.convert("RGB").save(combined_stream, format="PDF")
    combined_stream.seek(0)
    return PdfReader(combined_stream).pages[0]


async def add_watermark(input_pdf_path, watermark_image_path, output_pdf_path, watermark_scale=0.99, watermark_angle=0,
                        watermark_opacity=0.5):
    pages = convert_from_path(input_pdf_path, dpi=base.PDF_DPI, fmt='png')
    first_page_width = pages[0].width
    watermark = await prepare_watermark(watermark_image_path, watermark_scale, watermark_angle, watermark_opacity,
                                        first_page_width)

    processed_pages = [None] * len(pages)  # Создаем список для сохранения обработанных страниц
    pdf_writer = PdfWriter()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_page, page, watermark) for page in pages]
        for i, future in enumerate(futures):
            processed_pages[i] = future.result()  # Сохраняем страницы в правильном порядке
            print(f'Page {i + 1} SUCCESSFULLY COMPLETED')

    for page in processed_pages:
        pdf_writer.add_page(page)

    with open(output_pdf_path, "wb") as output_pdf_file:
        pdf_writer.write(output_pdf_file)
