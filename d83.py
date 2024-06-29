def send_mail(message, recipient, sender = "university.help@gmail.com"):
    if '@' and ('com' or 'ru' or 'net')  not in (recipient and sender):
        print("Невозможно отправить письмо с адреса", sender,"на адрес", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе")

    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender,
              "на адрес", recipient)

    else:
        print("нестандартный отправитель !".upper(),
              "Письмо отправлено с адреса", sender, "на адрес", recipient)


send_mail("", "vasyok1337@gmail.com", sender="university.help@gmail.com")
send_mail("", "urban.fan@gmail.ru", sender="urban.info@gmail.com")
send_mail("", "urban.student@mail.uk", sender="university.help@gmail.uk")
send_mail("", "vasyok1337@gmail.com", sender="vasyok1337@gmail.com")

