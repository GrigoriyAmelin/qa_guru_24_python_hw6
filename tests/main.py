# Создайте набор функций для обработки информации о письме. Каждая функция должна выполнять ровно одно действие и возвращать результат.
import datetime
from pprint import pprint

from pyexpat.errors import messages

email_test = {"subject": "Story telling  ",
         "sender": "12345ZionCAMichaelLanda@dot.com ",
         "recipient": "   8762-Orley-WY-MrSmith@yandex.ru  ",
         "body": "Somebody wrote about this story, so that, finally, \tYou should do it wright now Jhonny!\n"}

# send_date = datetime.datetime.now().strftime("%Y-%m-%d")
# email_test["date"] = send_date

### Функции для реализации:
# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы
def normalize_addresses(email_to_normalise: str) -> str:
    normalised_address = email_to_normalise.lower().strip()
    return normalised_address

    """
    Возвращает значение, в котором адрес приведен к нижнему регистру и очищен от пробелов по краям.
    """

updated_email = normalize_addresses(email_test['sender'])
print(f'1. Updated email: "{updated_email}"')


# 2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")
def add_short_body(email_body_to_shorten: dict) -> dict:
    short_body = email_body_to_shorten['body'][0:10] + "..."
    email_body_to_shorten['short_body'] = short_body
    return email_body_to_shorten

    """
    Возвращает email с новым ключом email["short_body"] — первые 10 символов тела письма + "...".
    """

print(f'2. Email after reducing: "{add_short_body(email_test)}"')


# 3. Очистка текста письма - заменяет табы и переводы строк на пробелы
def clean_body_text(email_text: str) -> str:
    clean_body = email_text.replace("\n", "").replace("\t", "").replace("  ", " ")
    return clean_body

    """
    Заменяет табы и переводы строк на пробелы.
    """

email_test['clean_body'] = clean_body_text(email_test['body'])
print(f'3. Body text after cleaning: "{email_test['clean_body']}"')


# 4. Формирование итогового текста письма - создает форматированный текст письма
def build_sent_text(email_to_format: dict) -> str:
    sent_text = f'''
        Кому: "{email_to_format['recipient']}", От: "{email_to_format['masked_sender']}"
        Тема: {email_to_format['subject']}, Дата: {email_to_format['date']},
        {email_to_format['short_body']}'''
    return sent_text

    """
    Формирует текст письма в формате:
    Кому: {to}, от {from}
    Тема: {subject}, дата {date}
    {clean_body}
    """


# 5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля
def check_empty_fields(subject: str, body:str) -> tuple[bool, bool]:
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return is_subject_empty, is_body_empty

    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """

check_results = check_empty_fields(email_test['subject'], email_test['body'])
print(f'5. Subject is empty: {check_results[0]}, body is empty: {check_results[1]}')


# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
def mask_sender_email(login: str, domain: str) -> str:
    masked_email = login[:2] + '***@' + domain
    return masked_email

    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """

sender_after_split = email_test['sender'].split('@')
login = sender_after_split[0]
domain = sender_after_split[1]
print(f'6. Masked email: {mask_sender_email(login, domain)}')


# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
def get_correct_email(email_list: list[str]) -> list[str]:
    extentions = ('.ru', '.com', '.net')
    correct_email_list = []
    for element in email_list:
        element = element.lower().strip()
        if element.endswith(extentions) and "@" in element:
            if element.partition('@')[0] and element.partition('@')[2].partition('.')[0]:
                correct_email_list.append(element)
    duplicate_removed_email_list = list(set(correct_email_list))
    return duplicate_removed_email_list

    """
    Возвращает список корректных email.
    """

test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "user@gmail.com"
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]
print(f'7. Correct emails: {get_correct_email(test_emails)}')


# 8. Создание словаря письма - создает базовую структуру письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    created_email = dict(sender=sender, recipient=recipient, subject=subject, body=body)
    return created_email

    """
    Создает словарь email с базовыми полями:
    'sender', 'recipient', 'subject', 'body'
    """

new_created_email = create_email('Sender', 'Recepient', 'Subject', 'Body')
print(f'8. Created email: {new_created_email}')


# 9. Добавление даты отправки - добавляет текущую дату
def add_send_date(email: dict) -> dict:
    send_date_field = datetime.datetime.now().strftime("%Y-%m-%d")
    email["date"] = send_date_field
    return email

    """
    Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
    """

email_with_send_date = add_send_date(email_test)
print(f'9. Email with send date: {email_with_send_date}')


# 10. Получение логина и домена - разделяет email на логин и домен
def extract_login_domain(address: str) -> tuple[str, str]:
    from_after_split = address.split('@')
    login = from_after_split[0]
    domain = from_after_split[1]
    return login, domain

    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
email_login, email_domain = extract_login_domain(email_test['sender'])
print(f'10. User login: {email_login}, '
      f'user domain: {email_domain}')

## Часть B. Отправка письма
# Создать функцию отправки письма с валидацией и обработкой. Функция принимает список получателей, тему, сообщение и отправителя.
### Последовательность обработки:
# 1. Проверить, что список получателей не пустой
# 2. Проверить корректность email адресов
# 3. Проверить заполненность темы и тела письма
# 4. Исключить отправку самому себе
# 5. Нормализовать все текстовые данные
# 6. Создать письмо для каждого получателя
# 7. Добавить дату отправки
# 8. Замаскировать email отправителя
# 9. Создать короткую версию тела письма
# 10. Сформировать итоговый текст письма

def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    # 1. Проверить, что список получателей не пустой
    if not recipient_list:
        return []

    # 2. Проверить корректность email адресов
    correct_email_list = get_correct_email(recipient_list + [sender])
    if not correct_email_list:
        return []
    if sender not in correct_email_list:
        return []

    # 3. Проверить заполненность темы и тела письма
    subject_is_empty,message_is_empty = check_empty_fields(subject, message)
    if subject_is_empty or message_is_empty:
        return []

    # 4. Исключить отправку самому себе
    for mail in correct_email_list:
        if mail == sender:
            correct_email_list.remove(mail)

    # 5. Нормализовать все текстовые данные
    clean_subject = clean_body_text(subject)
    clean_body = clean_body_text(message)
    clean_sender = normalize_addresses(sender)
    clean_recipient_list = []
    for element in correct_email_list:
        element = normalize_addresses(element)
        clean_recipient_list.append(element)

    # 6. Создать письмо для каждого получателя
    # 7. Добавить дату отправки
    # 8. Замаскировать email отправителя
    # 9. Создать короткую версию тела письма
    # 10. Сформировать итоговый текст письма
    recipient_emails = []
    for recipient in clean_recipient_list:
        email = create_email(sender=clean_sender, recipient=recipient, subject=clean_subject, body=clean_body)
        email = add_send_date(email)
        login, domain = extract_login_domain(recipient)
        email['masked_sender'] = mask_sender_email(login, domain)
        email['clean_body'] = clean_body
        email = add_short_body(email)
        sent_text = build_sent_text(email)
        email['sent_text'] = sent_text
        recipient_emails.append(email)
    return recipient_emails

### Результат:
# Список с готовыми письмами, содержащими все обработанные данные.
recipient_list = ['erer@EEya.us', 'DSpeQ@rt.net', 'qwe45RRRRer@er.ru ', ' fg@.com', ' fg@Qwer.com', 'new_mailer@tre.com']
subject = '  Theme to test something for you...  '
message = 'All is OK but you don\'t know'
result = sender_email(recipient_list, subject, message)

pprint(result)