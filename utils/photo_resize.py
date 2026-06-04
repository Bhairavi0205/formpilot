from PIL import Image
import io

EXAM_SPECS = {
    "SSC": {"width": 100, "height": 120, "max_kb": 50},
    "UPSC": {"width": 300, "height": 350, "max_kb": 300},
    "RAILWAY": {"width": 100, "height": 120, "max_kb": 50},
    "IBPS": {"width": 140, "height": 110, "max_kb": 50},
    "MPSC": {"width": 100, "height": 120, "max_kb": 50},
}

def resize_image_for_exam(image_bytes: bytes, exam_name: str, image_type: str = "photo") -> bytes:
    """
    Resize photo or signature as per exam specifications
    image_type: 'photo' or 'signature'
    """
    exam_key = exam_name.upper()
    
    # Find matching exam spec
    spec = None
    for key in EXAM_SPECS:
        if key in exam_key:
            spec = EXAM_SPECS[key]
            break
    
    if not spec:
        spec = {"width": 100, "height": 120, "max_kb": 50}
    
    # Signature size different
    if image_type == "signature":
        width = spec["width"]
        height = 40
    else:
        width = spec["width"]
        height = spec["height"]
    
    # Open and resize
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("RGB")
    img = img.resize((width, height), Image.LANCZOS)
    
    # Compress to fit size limit
    output = io.BytesIO()
    quality = 95
    while quality > 10:
        output = io.BytesIO()
        img.save(output, format="JPEG", quality=quality)
        size_kb = output.tell() / 1024
        if size_kb <= spec["max_kb"]:
            break
        quality -= 5
    
    return output.getvalue()

def get_exam_photo_specs(exam_name: str) -> str:
    """Return photo specs for an exam as readable text"""
    exam_key = exam_name.upper()
    for key, spec in EXAM_SPECS.items():
        if key in exam_key:
            return f"""📸 {exam_name} Photo Specs:
- Width: {spec['width']}px
- Height: {spec['height']}px  
- Max size: {spec['max_kb']} KB
- Format: JPG/JPEG
- Background: White only"""
    return "Exam specs nahi mile. SSC/UPSC/RAILWAY/IBPS/MPSC try karo."