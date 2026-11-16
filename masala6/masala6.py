menu = {"lavash": 28000, "somsa": 10000, "choy": 5000}

def buyurtma(*args, **kwargs):
    jami = 0
    for mahsulot in args:
        if mahsulot in menu:
            jami += menu[mahsulot]
        else:
            print(f"Ogohlantirish: '{mahsulot}' menuda yo'q!")

    print(f"Mijoz: {kwargs.get('mijoz')}")
    print(f"Telefon: {kwargs.get('telefon')}")
    print(f"Jami: {jami} so'm")

buyurtma("lavash", "choy", "somsa", mijoz="Dilshod", telefon="901234567")