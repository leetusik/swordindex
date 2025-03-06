import os

from PIL import Image, ImageDraw, ImageFont

# Create directory if it doesn't exist
os.makedirs("static/img/carousel", exist_ok=True)

# Define image size and colors - using 480x500 for Apple-style cards
width, height = 480, 500
colors = [
    (55, 93, 232),  # Blue (primary color)
    (41, 128, 185),  # Another blue shade
    (142, 68, 173),  # Purple
]

titles = ["AI 검색 솔루션", "데이터 분석 대시보드", "맞춤형 추천 시스템"]

descriptions = [
    "고객 맞춤형 검색 결과 제공",
    "실시간 검색 패턴 분석",
    "고객별 최적화된 상품 추천",
]

# Create each image
for i in range(3):
    # Create a new image with a colored background
    img = Image.new("RGB", (width, height), colors[i])
    draw = ImageDraw.Draw(img)

    # Add some shapes for visual interest - in the top 65% of the image
    img_height_65_percent = int(height * 0.65)

    # Draw a pattern of circles
    for j in range(5):
        # Draw some circles with slight transparency
        x = width // 6 * (j + 1)
        y = img_height_65_percent // 2
        size = 80 + j * 15
        draw.ellipse(
            (x - size // 2, y - size // 2, x + size // 2, y + size // 2),
            fill=(255, 255, 255, 128),
            outline=None,
        )

    # Add a decorative element
    for k in range(3):
        x_pos = width // 4 * (k + 1)
        y_pos = img_height_65_percent // 3 * 2
        size = 40
        draw.rectangle(
            (
                x_pos - size // 2,
                y_pos - size // 2,
                x_pos + size // 2,
                y_pos + size // 2,
            ),
            fill=(255, 255, 255, 100),
            outline=None,
        )

    # Add text to the image area
    try:
        # Try to use a system font
        font_large = ImageFont.truetype("Arial", 24)
    except IOError:
        # Fallback to default font
        font_large = ImageFont.load_default()

    # Add slide number
    draw.text(
        (width - 50, img_height_65_percent - 30),
        f"Slide {i+1}",
        fill=(255, 255, 255),
        font=font_large,
        anchor="mm",
    )

    # Save the image
    img.save(f"static/img/carousel/slide{i+1}.png")

    print(f"Created slide{i+1}.png")

print("All dummy images created successfully!")
