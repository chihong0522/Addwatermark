from PIL import Image
 
def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path
                                ):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    watermark = addTransparency(watermark,factor=0.6)
    width, height = base_image.size

    
    img_x,img_y =width, height 
   
    watermark = watermark.resize(((img_x//10)*8,(img_y//10)*8),Image.LANCZOS)
    watermark =watermark.rotate( 30, Image.BILINEAR )
    watermark_x,watermark_y = watermark.size

    position=(img_x//2-watermark_x//2,img_y//2-watermark_y//2)
 
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)

    transparent.show()
    transparent.save(output_image_path)
 
 
def addTransparency(img, factor = 0.7 ):
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    img = Image.blend(img_blender, img, factor)
    return img


if __name__ == '__main__':
    img = 'cooper_ID.jpg'
    watermark_with_transparency(img, 'result.png','watermark.png')