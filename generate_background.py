#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

# Create a 1920x1080 image with MineHarvest primary color background
# Using the secondary color #2d8291 as base
img = Image.new('RGB', (1920, 1080), color=(45, 130, 145))

draw = ImageDraw.Draw(img)

# Try to use a nice font, fallback to default
try:
    # Try to find a bold sans-serif font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
except IOError:
    try:
        font = ImageFont.truetype("arial.ttf", 140)
    except IOError:
        font = ImageFont.load_default()

# Draw "MineHarvest" text in bright blue (#1DC1DE is the primary color)
text = "MineHarvest"
# Get text bounding box to center it properly
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (1920 - text_width) // 2
y = (1080 - text_height) // 2

# Draw text in bright cyan/blue (#1DC1DE)
draw.text((x, y), text, fill=(29, 193, 222), font=font)

# Save to bytes and encode as base64
buffer = BytesIO()
img.save(buffer, format="PNG")
img_bytes = buffer.getvalue()
base64_str = base64.b64encode(img_bytes).decode()

# Save the image directly
img.save('servers/mineharvest/background.png')
print("Background image created successfully!")
print("Saved to: servers/mineharvest/background.png")
