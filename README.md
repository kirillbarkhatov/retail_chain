# 🛒 Онлайн-платформа торговой сети электроники

Проект реализует иерархическую модель поставщиков электроники: заводы, розничные сети и индивидуальные предприниматели. Предусмотрен API-интерфейс, админ-панель и ограничения доступа.

---

## ⚙️ Технологии

- Python 3.13
- Django 5.1+
- Django REST Framework
- PostgreSQL
- Simple JWT
- Poetry

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone <your_repo_url>
   cd <project_folder>
   ```

2. Установите зависимости с помощью Poetry:
   ```bash
   poetry install
   ```

3. Активируйте виртуальное окружение:
   ```bash
   poetry shell
   ```

4. Настройте переменные окружения (`.env`), например:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   POSTGRES_DB=retail_db
   POSTGRES_USER=retail_user
   POSTGRES_PASSWORD=retail_pass
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```

5. Выполните миграции:
   ```bash
   python manage.py migrate
   ```

6. Загрузите тестовые данные:
   ```bash
   python manage.py add_test_data
   ```

7. Создайте суперпользователя:
   ```bash
   python manage.py csu
   ```

8. Создайте тестовых пользователей:
   ```bash
   python manage.py create_test_user
   ```

9. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

---

## 👤 Пользователи и доступ

- API защищён: доступ имеют только **активные пользователи с флагом `is_staff=True`**
- Для тестирования доступны:
  - `test1` (активный, `is_staff=True`)
  - `test2` (активный, `is_staff=False`)
  - `admin` (суперпользователь)

---

## 🔐 Аутентификация (JWT)

Подключена авторизация через Simple JWT:

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/api/users/token/` | Получить `access` и `refresh` токены |
| `POST` | `/api/users/token/refresh/` | Обновить `access` токен |
| `POST` | `/api/users/token/verify/` | Проверка токена на валидность |

---

## 📦 API Поставщиков

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `GET` | `/api/suppliers/suppliers/` | Список поставщиков (фильтр по стране: `?country=Россия`) |
| `POST` | `/api/suppliers/suppliers/` | Создание поставщика |
| `PUT/PATCH` | `/api/suppliers/suppliers/<id>/` | Обновление (поле `debt` — только для чтения) |
| `DELETE` | `/api/suppliers/suppliers/<id>/` | Удаление поставщика |

---

## ⚠️ Кастомные команды

- `python manage.py csu` — создать суперпользователя `admin`
- `python manage.py create_test_user` — создать `test1` и `test2`
- `python manage.py add_test_data` — загрузить тестовые фикстуры (поставщики, продукты)

---

## 🧪 Тестирование API

В проекте есть готовая коллекция для Postman:

📁 **Retail Chain API.postman_collection.json**

Импортируйте файл в Postman и протестируйте:

- Получение токена
- Работа с поставщиками
- Авторизация и доступы

---

## ✅ Переменные окружения Postman

```env
base_url = http://127.0.0.1:8000
access_token = (автоматически подставляется после логина)
refresh_token = (аналогично)
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.
