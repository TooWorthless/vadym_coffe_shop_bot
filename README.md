
# Vadyms Coffee Bot ☕️

**Ароматний бот для справжніх кавоманів!**

`Vadyms Coffee Bot` — це ваш особистий бариста у Telegram! Переглядайте каталог смачної кави, замовляйте улюблені напої, залишайте відгуки та керуйте асортиментом. Простота, зручність і трохи кавової магії — ось що робить цей проєкт особливим.

## 🚀 Особливості

- **Широкий вибір кави**: Від класики до витончених авторських напоїв.
- **Легке замовлення**: Пара кліків — і кава у вашому чаті!
- **Зворотний зв’язок**: Залишайте враження.
- **Адмін-панель**: Повний контроль над асортиментом.
- **Гарний дизайн**: Емодзі, дружній тон і зручність.

## ⚙️ Як запустити локально

### Вимоги

- Python 3.8+
- Бібліотека `pyTelegramBotAPI` (встановлюється через `requirements.txt`)
- Telegram-токен від BotFather

### Кроки

```bash
git clone https://github.com/yourusername/vadyms-coffee-bot.git
cd vadyms-coffee-bot

python -m venv venv
source venv/bin/activate 
venv\Scripts\activate 

pip install -r requirements.txt
```

Відкрийте `config/settings.py`:

- Замініть `API_TOKEN` на свій токен
- Додайте свій Telegram ID до `ADMIN_IDS`

Запустіть:

```bash
python main.py
```

Відкрийте Telegram і введіть `/start` у чаті з ботом.

## 👥 Як користуватися

### Для користувачів

- Переглянути каталог: `/catalog`
- Замовити каву: вибір → підтвердження
- Залишити відгук: `/feedback`

### Для адміністраторів

- Вхід у панель: `/admin`
- Додати каву: `/add_item`
- Видалити каву: `/remove_item`
- Переглянути замовлення: `/orders`

## ☕️ Початковий каталог

- **Еспресо**: Міцна класика — 35 грн
- **Лате**: Ніжна пінка — 45 грн
- **Капучино**: Ідеальний баланс — 40 грн
- **Американо**: Легка кава — 30 грн
- **Мокко**: Шоколадна насолода — 50 грн
- **Флет Вайт**: Гладкий смак — 48 грн

## 🌐 Розгортання на сервері

```bash
scp -r vadyms-coffee-bot user@server:/path/to/bot
ssh user@server

cd /path/to/bot/vadyms-coffee-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

nohup python main.py &
```

## 🤝 Внесок у проєкт

- Форкніть репозиторій
- Створіть гілку: `git checkout -b feature/нова-фіча`
- Закомітьте: `git commit -m "Додано фічу"`
- Надішліть Pull Request!

## 📄 Ліцензія

Проєкт під MIT-ліцензією. Пийте каву, створюйте бота — без обмежень.

## 👨‍💻 Автор

Розроблено з любов’ю до кави Vadym’ом.  
Зв’язок: [Telegram](#) | [Email](mailto:your.email@example.com)

Vadyms Coffee Bot — коли код і кава стають одним цілим.
