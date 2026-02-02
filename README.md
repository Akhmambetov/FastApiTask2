# SSEProject2
## Запуск проекта без Docker
1. Клонировать репозиторий
```
git clone https://github.com/Akhmambetov/FastApiTask2
cd .\FastApiTask2-main\   
```
2. Установить зависимости
```
pip install -r requirements.txt
```
3. Запустить приложение
```
uvicorn src.main:app --reload
```
4. После запуска сервис будет доступен по адресу:
```
http://127.0.0.1:8000
```

SSE-поток:
```
http://localhost:8000/flow
```
## Запуск проекта с Docker
1. Собрать Docker образ:
```
docker build -t sse-app .
```
2. Запустить контейнер:
```
docker run -p 8000:8000 sse-app
```
3. Проверка работы:
```
http://localhost:8000
```

SSE-поток:
```
http://localhost:8000/flow
```
