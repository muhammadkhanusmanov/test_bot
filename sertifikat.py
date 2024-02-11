from PIL import Image, ImageDraw, ImageFont


def sertificate(rasm_fayli,name,name2,fan,cnt,pr):
    image = Image.open(rasm_fayli)


    matn_rangi = (0, 0, 0) 


    matn_joylashuvi = (250, 530) 


    font_size = 65
    font = ImageFont.truetype("arial3.ttf", size=font_size)


    draw = ImageDraw.Draw(image)
    draw.text(matn_joylashuvi, name, font=font, fill=matn_rangi)

    matn = f"{fan} fanidan o'tkazilgan Online testda qatnashib o'tkir\n      bilimini namayon qilganligi hamda {cnt} ta ({pr}%) natija\n ko'rsatganligi munosabati bilan {name2} tomonidan \n              1-darajali Diplom bilan taqdirlanadi."
    matn_rangi = (0, 0, 0) 

    matn_joylashuvi = (45, 640) 


    font_size = 46
    font = ImageFont.truetype("arial2.TTF", size=font_size)

    draw = ImageDraw.Draw(image)
    draw.text(matn_joylashuvi, matn, font=font, fill=matn_rangi)



    rasm_fayli_tahrir = "example_with_text.jpg"
    image.save(rasm_fayli_tahrir)