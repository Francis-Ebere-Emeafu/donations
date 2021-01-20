import os, shutil
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings

GREEN = (59, 155, 59, 255)
BLACK = (0, 0, 0, 255)


def write_text(TXT, fontsize, imgw, imgh, fontcolor):
    #base = Image.open('regno.png').convert('RGBA')
    #font = ImageFont.load('pilfonts/timR24.pil')
    font_path = os.path.join(settings.STATIC_ROOT, 'fonts', 'Roboto-Bold.ttf')
    font = ImageFont.truetype(font_path, fontsize)
    #font = ImageFont.truetype('arial.ttf', fontsize)
    width, height = font.getsize(TXT)
    txt = Image.new('RGBA', (imgw, imgh), (255, 255, 255, 255))
    d = ImageDraw.Draw(txt)
    d.text(
        ((imgw-width)/2, (imgh-height)/2),
        TXT,
        fill=fontcolor,
        font=font
    )
    #out = Image.alpha_composite(base, txt)
    #return out
    return txt
    #out.show()
    #txt.save('test.png', 'PNG')
    #im = Image.open(fpath)
    #im.thumbnail((128, 128))
    #im.save('out.png', 'PNG')


def paint_cert(regno, name, dt, fname):
    inpath = os.path.join(settings.STATIC_ROOT, 'certificate.png')
    outpath = os.path.join(settings.MEDIA_ROOT, 'certificates', fname)
    #shutil.copy(inpath, outpath)
    #import pdb;pdb.set_trace()
    left, top, width, height = 2016, 160, 744, 116
    img = Image.open(inpath)
    reg_box = (left, top, left + width, top + height)
    #box = (2016, 160, 2760, 276)
    #reg_region = img.crop(reg_box)

    reg_out = write_text('Reg No: {}'.format(regno), 50, width, height, BLACK)
    #out.show()
    img.paste(reg_out, reg_box)

    name_box = (520, 648, 2552, 820)
    #name_region = img.crop(name_box)
    name_out = write_text(name, 100, 2032, 172, GREEN)
    img.paste(name_out, name_box)

    date_box = (988, 1308, 2056, 1436)
    print(date_box)
    #date_region = img.crop(date_box)
    date_out = write_text(dt, 100, 1068, 128, BLACK)
    img.paste(date_out, date_box)
    img.save(outpath, 'PNG')
    return outpath

    #img.show()


#paint_cert('ASN9999999', 'BIG BEE', 'January 2019', 'big_bee.png')
