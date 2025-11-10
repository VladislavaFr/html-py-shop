from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Конфигурация сервера
HOST = 'localhost'
PORT = 8000


class MyHandler(BaseHTTPRequestHandler):
    # Обработка GET-запросов
    def do_GET(self):
        # Определяем, какую страницу показывать
        if self.path == '/' or self.path == '/main.html':
            path = 'templates/main.html'
        elif self.path == '/catalog.html':
            path = 'templates/catalog.html'
        elif self.path == '/category1.html':
            path = 'templates/category1.html'
        else:
            path = 'templates/contacts.html'

        try:
            # Отправляем успешный ответ и заголовки
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Читаем HTML-файл и отправляем в ответ
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            # Если файл не найден
            self.send_error(404, f"Файл {path} не найден.")

    # Обработка POST-запросов (доп. задание)
    def do_POST(self):
        # Получаем длину данных из заголовка
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Разбираем данные формы
        data = parse_qs(post_data)
        print("📩 Полученные данные:", data)

        # Отправляем пользователю ответ
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>Данные успешно отправлены!</h1>".encode('utf-8'))


if __name__ == "__main__":
    # Запуск сервера
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}")
    print("Нажмите Ctrl + C для остановки сервера.")
    server.serve_forever()