# Використовуємо Python 3.8 на базі Alpine
FROM python:3.8-alpine

# Встановлюємо робочу директорію
WORKDIR /app

# Встановлюємо необхідні системні пакети для роботи з MySQL
RUN apk add --no-cache \
    mariadb-dev \
    build-base

# Копіюємо лише requirements.txt спочатку, щоб кешувати залежності
COPY requirements.txt /app/

# Встановлюємо Python залежності
RUN pip freeze > requiremenets.txt

# Копіюємо весь код в контейнер після встановлення залежностей
COPY . /app/

# Відкриваємо порт для Django
EXPOSE 8000

# Команда для запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]