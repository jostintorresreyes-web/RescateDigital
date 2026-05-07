import sys
from PIL import Image, ImageDraw

def process():
    input_path = r"C:\Users\Jostin Torres\.gemini\antigravity\brain\1f660954-5dc0-47bb-8496-19d8d4858486\media__1778159111604.jpg"
    output_path = r"c:\Users\Jostin Torres\RescateDigital\RescateDigital\static\img\favicon.png"
    
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    
    # find left boundary
    left = 0
    for x in range(w // 2):
        pixel = img.getpixel((x, h // 2))
        # checkerboard usually has R,G,B > 200
        if pixel[0] < 200 or pixel[1] < 200 or pixel[2] < 200:
            left = x
            break
            
    # if we didn't find a clear boundary, assume a default or use whole image
    if left == 0:
        left = int(w * 0.179) # Use same ratio as before
        
    print(f"Size: {w}x{h}, Left bound: {left}")
    
    radius = (w / 2) - left
    cx, cy = w / 2, h / 2
    
    bbox = [int(cx - radius), int(cy - radius), int(cx + radius), int(cy + radius)]
    
    # Create an alpha mask
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(bbox, fill=255)
    
    # Apply mask
    result = Image.new("RGBA", (w, h))
    result.paste(img, (0, 0), mask=mask)
    
    # Crop
    result = result.crop(bbox)
    
    # Save
    result.save(output_path)
    print("Saved to", output_path)

if __name__ == "__main__":
    process()
