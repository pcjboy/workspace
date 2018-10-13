import random


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_code_img(request):

    # 方式一
    # with open("testimg.jpg", "rb") as f:
    #     data = f.read()

    # 方式二  # pip install pillow
    # from PIL import Image
    # img = Image.new("RGB", (270, 40), color=get_random_color())
    # with open("validCode.png", "wb") as f:
    #     img.save(f, "png")
    #
    # with open("validCode.png", "rb") as f:
    #     data = f.read()

    # 方式三
    # from PIL import Image
    # from io import BytesIO
    #
    # img = Image.new("RGB", (270,40), color=get_random_color())
    # f = BytesIO()
    # img.save(f, "png")
    # data = f.getvalue()

    # 方式四
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    import random

    img = Image.new("RGB", (270, 40), color=get_random_color())

    draw = ImageDraw.Draw(img)
    msyh_font = ImageFont.truetype("static/font/msyhl.ttc", size=32)

    # char = str(random.randint(0, 9))
    valid_code_str = ""
    # 在验证码图片上加上5个字母和数字
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=msyh_font)

        # 保存验证码字符串
        valid_code_str += random_char

    # 验证码的图片 上加上线和点
    width = 270
    height = 40
    for i in range(3):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(30):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    print("valid_code_str", valid_code_str)
    request.session["valid_code_str"] = valid_code_str

    '''
    1 sdjflksdf
    2 COOKIE {"sessionid": slkdjflsdkf}
    3 django-session
      session-key session-data
      lksdjflksdjfklsdf {}

    '''

    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    return data
