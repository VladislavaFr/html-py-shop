# ️ HTML-PY-SHOP

Простое веб-приложение на Python, созданное для демонстрации базовых принципов работы веб-сервера без фреймворков.  
Проект состоит из HTML-страниц, собранных с помощью Bootstrap, и Python-сервера, который возвращает страницу «Контакты» при GET-запросе.

---

##  Структура проекта

```
html-py-shop/
├─ .gitignore
├─ pyproject.toml
├─ README.md
├─ main.py
├─ css/
│  └─ bootstrap.min.css
├─ templates/
│  ├─ main.html
│  ├─ catalog.html
│  ├─ category1.html
│  └─ contacts.html
└─ .venv/   
```

---

## ⚙ Установка и запуск

### 1. Клонируйте проект
```bash
git clone https://github.com/username/html-py-shop.git
cd html-py-shop
```

### 2. Создайте виртуальное окружение
```bash
python -m venv .venv
```

### 3. Активируйте окружение
#### Windows:
```bash
.venv\Scripts\activate
```

#### macOS / Linux:
```bash
source .venv/bin/activate
```

### 4. Установите зависимости
(если они указаны в `pyproject.toml` или `requirements.txt`)
```bash
pip install -r requirements.txt
```

---

##  Запуск приложения

```bash
python main.py
```

После запуска сервер будет доступен по адресу:
```
http://localhost:8080
```

---

##  Как это работает

- Сервер на Python обрабатывает HTTP-запросы.
- При любом **GET-запросе** возвращается страница `contacts.html`.
- При **POST-запросе** сервер принимает данные формы и выводит их в консоль.

---

##  Используемые технологии

- **Python (http.server)** — встроенный HTTP-сервер
- **HTML5 / CSS3**
- **Bootstrap 5** — стилизация страниц

---

##  Условия

- [x] Страницы собраны по макету с использованием Bootstrap  
- [x] Реализован простой веб-сервер на Python  
- [x] Добавлен `.gitignore`  
- [x] Код оформлен по PEP8  
- [x] Все файлы проекта находятся в репозитории  

