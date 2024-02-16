from config_data import config

# Получение списка ID администраторов из конфигурации
admin_ids = config.load_config().admins.id
# Фильтр для сообщений
message_admin_filter = lambda message: message.from_user.id in admin_ids
# Фильтр для callback-запросов
callback_query_admin_filter = lambda callback_query: callback_query.from_user.id in admin_ids



check_nums = lambda text: all(map(str.isdigit, text.split('.')))
