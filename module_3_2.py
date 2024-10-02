def send_email(message, recipient,*, sender="university.help@gmail.com"):
    if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
        if "@" not in recipient or "@" not in sender:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            return 0
        else:
            if sender == recipient:
                print("Нельзя отправить письмо самому себе!")
                return 0
            if sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}\n'
                      f'{message}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}\n'
                      f'{message}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return 0


send_email("Привет, я Сергей", "university.help@gmail.com", sender="serega22222223@mail.ru")
print("")
send_email("Привет, Сергей, очень рады тебе", "serega22222223@mail.ru")
print("")
# 1 Исключение - Отправка самому себе
send_email("Я хейтер ", "Heiter@mail.ru", sender="Heiter@mail.ru")
print("")
# 2 Исключение - Некоректный Адрес почты
send_email("Я хейтер ", "Heitermail.ru", sender="Heiter@mail")
