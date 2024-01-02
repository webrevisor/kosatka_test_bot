from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import io
import config


async def add_watermark(input_pdf_path, watermark_image_path, output_pdf_path, watermark_scale=0.99, watermark_angle=0,
                  watermark_opacity=0.5):
    # Загрузка изображения водяного знака
    watermark_img = Image.open(watermark_image_path).convert("RGBA")
    original_watermark_width, original_watermark_height = watermark_img.size

    # Конвертация PDF в список изображений
    pages = convert_from_path(input_pdf_path, dpi=config.PDF_DPI, fmt='png')

    pdf_writer = PdfWriter()

    for page in pages:
        # Рассчитываем размер водяного знака в соответствии с заданным масштабом
        watermark_width = int(page.width * watermark_scale)
        watermark_height = int(original_watermark_height * (watermark_width / original_watermark_width))

        # Масштабирование и поворот водяного знака
        resized_watermark = watermark_img.resize((watermark_width, watermark_height), Image.ANTIALIAS)
        rotated_watermark = resized_watermark.rotate(watermark_angle, expand=True)

        # Настройка прозрачности водяного знака
        transparent_watermark = Image.new("RGBA", rotated_watermark.size)
        for x in range(rotated_watermark.width):
            for y in range(rotated_watermark.height):
                r, g, b, alpha = rotated_watermark.getpixel((x, y))
                transparent_watermark.putpixel((x, y), (r, g, b, int(alpha * watermark_opacity)))

        # Вычисление позиции для центрирования водяного знака
        x = (page.width - transparent_watermark.width) // 2
        y = (page.height - transparent_watermark.height) // 2

        # Создание нового изображения с водяным знаком
        combined = Image.new("RGBA", page.size)
        combined.paste(page.convert("RGBA"), (0, 0))
        combined.paste(transparent_watermark, (x, y), mask=transparent_watermark)

        # Сохранение новой страницы в PDF
        combined_stream = io.BytesIO()
        combined.convert("RGB").save(combined_stream, format="PDF")
        combined_stream.seek(0)
        pdf_writer.add_page(PdfReader(combined_stream).pages[0])

    # Сохранение итогового файла
    with open(output_pdf_path, "wb") as output_pdf_file:
        pdf_writer.write(output_pdf_file)


# Использование функции
# add_watermark('1.pdf', 'WATER1.png', 'output_pdf1_099_0_1.pdf', 0.99, 0, 1)
# add_watermark('1.pdf', 'WATER1.png', 'output_pdf1_099_45_05.pdf', 0.99, 45, 0.5)
# add_watermark('1.pdf', 'WATER2.png', 'output_pdf1_07_0_1.pdf', 0.7, 0, 1)
# add_watermark('4.pdf', 'WATER1.png', 'output_pdf4_099_0_1.pdf', 0.99, 0, 1)
# add_watermark('4.pdf', 'WATER2.png', 'output_pdf4_099_45_05.pdf', 0.99, 45, 0.5)
