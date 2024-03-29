from random import choice

LEXICON: dict[str, str] = {
    '/start': lambda message: f'{choice(["Салют", "Привет", "Здравствуй", "Нихао"])}, '
                              f'{message.from_user.first_name or message.from_user.username}!\n'
                              f'{choice(["Чем я могу помочь?", "Буду рад помочь!"])}{choice(["🤗","😉","😇"])}',
    '/help': 'Я бот группы Prospect.\nИспользуй команду /start',
    'calculate_end': 'Стоимость без учета доставки:',
    'Как пользоваться Poizon?': 'В данной статье вы найдете информацию об использовании приложения <b>Poizon</b> 📱\n\n'
                                'Если у вас остались дополнительные вопросы, то мы всегда рады вас проконсультировать - <b>@prospecthelp</b> 😉',
    'Как сделать заказ?': 'В данной статье мы вы можете узнать о том, как оформить заказ 🛍️\n\n'
                          'Если у вас остались дополнительные вопросы, то мы всегда рады вас проконсультировать - <b>@prospecthelp</b> 😉',
    'FAQ': 'Здесь вы найдёте ответы на <b>часто задаваемые вопросы!</b>\n\n'
           'Не нашли ответ? Задайте его нам - <b>@prospecthelp</b> 😇',
    'О нас': '✨ Мы предлагаем прозрачные условия и справедливую комиссию. \n\n😱 '
             'В настоящее время, стоимость наших услуг составляет 9% от суммы покупки, с минимальной комиссией в размере 400 рублей, независимо от цены товара. \nТаким образом, вы получаете выгодные условия и контроль над своими расходами.\n\n'
             '🚚 Доставка с нашего склада в Китае до Москвы в среднем занимает 14-20 дней.\n\n'
             '💸 Оплата доставки осуществляется по прибытии вашего заказа в Москву, а её стоимость зависит от габаритов и веса товара.\n\n'
             '📦 Мы придерживаемся высоких стандартов качества. Каждая посылка тщательно упаковывается для гарантированной сохранности товара во время транспортировки. Ваше доверие и полное удовлетворение - наши главные приоритеты.\n\n'
             '❤ Присоединяйтесь к нам и оцените высокий уровень надежности, качества и профессионализма в каждом шаге процесса выкупа и доставки. Мы ценим ваше доверие и готовы сделать все возможное, чтобы ваш опыт с нами был беззаботным и приятным ❤\n\n',
    'Какова цена доставки?': 'Стоимость доставки с Китая до Москвы зависит от веса заказа и текущего курса, оплата доставки происходит по прибытии заказа в Москву.'
                             '\n\nОриентировачная расценка: 1200₽ за 1кг товаров.',
    'calculate_again': 'Повторить рассчет',
    'delivery_cost': 'Какова цена доставки?',
    'order': 'Заказать',
    'back': 'Назад',
    'main_menu': 'Вы вернулись в главное меню',
    'using_app': 'О приложении Poizon',
    'ios': 'Скачать IOS',
    'android': 'Скачать Android',
    'how_order': 'Как сделать заказ?',
    'faq': "FAQ",
    'not_sub': 'Для использования бота подпишись на канал.',
    'parameters': lambda rate, commission: f"Текущий курс: <b>1¥ | {rate}₽</b>.\n\n"
                               f"Текущая комиссия: <b>{commission}%</b>"
}
MENU_COMMAND: dict[str:str] = {
    '/start': 'Начать', '/help': 'Справка'
}

KEYBOARD_USER: dict[str, list] = {
    '/start': ['Рассчитать стоимость',
               'Как пользоваться Poizon?',
               'Как сделать заказ?',
               'FAQ',
               'О нас'],
}

KEYBOARD_ADMIN: dict[str, list] = {
    '/start': ['Рассчитать стоимость',
               'Рассылка',
               'Курс | Комиссия',
               'Статьи']
}
URLS: dict[str, str] = {
    'ios': 'https://apps.apple.com/app/id1012871328',
    'android': 'https://www.anxinapk.com/rj/12201303.html',
    'using_app': 'https://telegra.ph/Ispolzovanie-prilozheniya-Poizon-06-25',
    'order': 'https://telegra.ph/Kak-sdelat-zakaz-06-25',
    'faq': 'https://telegra.ph/FAQ-06-25-11'
}

