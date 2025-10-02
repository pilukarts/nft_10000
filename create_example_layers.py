#!/usr/bin/env python3
"""
Create example layer images for demonstration
This script generates simple colored rectangles as example layers
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_example_layer(output_path, color, text, size=(1000, 1000), alpha=255):
    """Create a simple colored layer with text"""
    img = Image.new('RGBA', size, (*color, alpha))
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Add text in center
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw text with outline for visibility
    for adj in [-2, -1, 1, 2]:
        draw.text((position[0]+adj, position[1]), text, font=font, fill=(0, 0, 0, 255))
        draw.text((position[0], position[1]+adj), text, font=font, fill=(0, 0, 0, 255))
    draw.text(position, text, font=font, fill=(255, 255, 255, 255))
    
    img.save(output_path)
    print(f"Created: {output_path}")

def main():
    """Generate example layers"""
    
    # Backgrounds - solid colors (opaque)
    backgrounds = [
        ("blue_100.png", (52, 152, 219), "Blue BG"),
        ("red_100.png", (231, 76, 60), "Red BG"),
        ("green_100.png", (46, 204, 113), "Green BG"),
        ("purple_100.png", (155, 89, 182), "Purple BG"),
        ("orange_100.png", (230, 126, 34), "Orange BG"),
        ("pink_100.png", (255, 105, 180), "Pink BG"),
        ("yellow_100.png", (241, 196, 15), "Yellow BG"),
        ("teal_100.png", (26, 188, 156), "Teal BG"),
    ]
    
    for filename, color, text in backgrounds:
        create_example_layer(f"layers/background/{filename}", color, text, alpha=255)
    
    # Bodies - circles (semi-transparent)
    bodies = [
        ("circle_red_100.png", (192, 57, 43), "Red Body"),
        ("circle_blue_100.png", (41, 128, 185), "Blue Body"),
        ("circle_green_100.png", (39, 174, 96), "Green Body"),
        ("circle_yellow_100.png", (244, 208, 63), "Yellow Body"),
        ("circle_purple_100.png", (142, 68, 173), "Purple Body"),
    ]
    
    for filename, color, text in bodies:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([200, 200, 800, 800], fill=(*color, 255))
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        position = ((1000 - text_width) // 2, 480)
        draw.text(position, text, font=font, fill=(255, 255, 255, 255))
        
        img.save(f"layers/body/{filename}")
        print(f"Created: layers/body/{filename}")
    
    # Clothes - rectangles on body
    clothes = [
        ("shirt_white_100.png", (236, 240, 241), "White Shirt"),
        ("shirt_black_80.png", (44, 62, 80), "Black Shirt"),
        ("shirt_red_60.png", (231, 76, 60), "Red Shirt"),
        ("shirt_blue_60.png", (52, 152, 219), "Blue Shirt"),
    ]
    
    for filename, color, text in clothes:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rectangle([300, 500, 700, 800], fill=(*color, 255))
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        position = ((1000 - text_width) // 2, 630)
        draw.text(position, text, font=font, fill=(255, 255, 255, 255))
        
        img.save(f"layers/clothes/{filename}")
        print(f"Created: layers/clothes/{filename}")
    
    # Eyes - small circles
    eyes = [
        ("happy_100.png", (0, 0, 0), "Happy"),
        ("serious_80.png", (44, 62, 80), "Serious"),
        ("sparkle_60.png", (52, 152, 219), "Sparkle"),
    ]
    
    for filename, color, text in eyes:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Left eye
        draw.ellipse([350, 350, 420, 420], fill=(*color, 255))
        # Right eye
        draw.ellipse([580, 350, 650, 420], fill=(*color, 255))
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        position = ((1000 - text_width) // 2, 320)
        draw.text(position, text, font=font, fill=(200, 200, 200, 255))
        
        img.save(f"layers/eyes/{filename}")
        print(f"Created: layers/eyes/{filename}")
    
    # Mouth - arcs
    mouths = [
        ("smile_100.png", (0, 0, 0), "Smile"),
        ("neutral_80.png", (100, 100, 100), "Neutral"),
    ]
    
    for filename, color, text in mouths:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.arc([400, 450, 600, 550], 0, 180, fill=(*color, 255), width=8)
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        position = ((1000 - text_width) // 2, 560)
        draw.text(position, text, font=font, fill=(200, 200, 200, 255))
        
        img.save(f"layers/mouth/{filename}")
        print(f"Created: layers/mouth/{filename}")
    
    # Accessories - optional items
    accessories = [
        ("hat_red_30.png", (231, 76, 60), "Hat"),
        ("glasses_20.png", (44, 62, 80), "Glasses"),
        ("none_50.png", (0, 0, 0), "None"),  # Transparent "no accessory" option
    ]
    
    for filename, color, text in accessories:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        
        if "none" not in filename:
            draw = ImageDraw.Draw(img)
            if "hat" in filename:
                # Simple hat shape
                draw.rectangle([350, 200, 650, 280], fill=(*color, 255))
                draw.rectangle([300, 280, 700, 320], fill=(*color, 255))
            elif "glasses" in filename:
                # Simple glasses
                draw.ellipse([330, 370, 440, 430], outline=(*color, 255), width=5)
                draw.ellipse([560, 370, 670, 430], outline=(*color, 255), width=5)
                draw.line([440, 400, 560, 400], fill=(*color, 255), width=5)
            
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
            except:
                font = ImageFont.load_default()
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            position = ((1000 - text_width) // 2, 180)
            draw.text(position, text, font=font, fill=(200, 200, 200, 255))
        
        img.save(f"layers/accessories/{filename}")
        print(f"Created: layers/accessories/{filename}")
    
    # Special - rare items
    specials = [
        ("crown_10.png", (241, 196, 15), "Crown"),
        ("star_5.png", (52, 152, 219), "Star"),
        ("none_85.png", (0, 0, 0), "None"),  # Most NFTs won't have special items
    ]
    
    for filename, color, text in specials:
        img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        
        if "none" not in filename:
            draw = ImageDraw.Draw(img)
            if "crown" in filename:
                # Simple crown
                points = [(450, 150), (500, 100), (550, 150), (500, 120)]
                draw.polygon(points, fill=(*color, 255))
                draw.rectangle([400, 150, 600, 200], fill=(*color, 255))
            elif "star" in filename:
                # Simple star (approximation)
                draw.ellipse([850, 100, 950, 200], fill=(*color, 255))
            
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
            except:
                font = ImageFont.load_default()
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            position = ((1000 - text_width) // 2, 150)
            draw.text(position, text, font=font, fill=(200, 200, 200, 255))
        
        img.save(f"layers/special/{filename}")
        print(f"Created: layers/special/{filename}")
    
    print("\n✓ Example layers created successfully!")
    print(f"  Total combinations possible: {len(backgrounds)} × {len(bodies)} × {len(clothes)} × {len(eyes)} × {len(mouths)} × {len(accessories)} × {len(specials)}")
    print(f"  = {len(backgrounds) * len(bodies) * len(clothes) * len(eyes) * len(mouths) * len(accessories) * len(specials)} unique NFTs")

if __name__ == "__main__":
    main()
