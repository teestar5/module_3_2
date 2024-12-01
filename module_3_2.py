def send_email(message, recipient, *, sender="university.help@gmail.com"):                    #интересно почему message не подсвечивается?
    if not recipient.endswith(".com") and not recipient.endswith(".ru") and not recipient.endswith(".net"):    #не оканчивается на ".com"/".ru"/".net"
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)                          #print it
        return

    if not sender.endswith(".com") and not sender.endswith(".ru") and not sender.endswith(".net"):         #не оканчивается на ".com"/".ru"/".net"
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)                          #print it
        return

    if '@' not in recipient:
        print("Адрес получателя некорректен, '@' отсутствует.")
        return

    if '@' not in sender:
        print("Адрес отправителя некорректен, '@' отсутствует.")
        return

    if sender == recipient:                                                                            #sender и recipient совпадают
        print("Нельзя отправить письмо самому себе!")                                                 #print it
        return

    if sender == "university.help@gmail.com":                                                         #отправитель по умолчанию - university.help@gmail.com
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)                     #print it
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)  #В противном случае print it


send_email('', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('', 'vasyok1337@gmail.com')


    
