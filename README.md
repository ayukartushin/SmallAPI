# 🐾 Simple Animals API

Этот проект — простой REST API на FastAPI для управления базой данных животных.

## 🚀 Запуск

Контейнер запускается через Docker:

```bash
docker run -d -p 8000:8000 your-image-name
```

API будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

## 📚 Эндпоинты

### ▶️ Создать животное

**POST** `/animals`

Создаёт новое животное.

**Request body:**

```json
{
  "name": "Шарик",
  "species": "Собака",
  "age": 3
}
```

**Response:**

```json
{
  "id": 0,
  "animal": {
    "name": "Шарик",
    "species": "Собака",
    "age": 3
  }
}
```

---

### 📄 Получить список всех животных

**GET** `/animals`

**Response:**

```json
{
  "0": {
    "name": "Шарик",
    "species": "Собака",
    "age": 3
  }
}
```

---

### 🔍 Получить животное по ID

**GET** `/animals/{animal_id}`

**Response (200):**

```json
{
  "name": "Шарик",
  "species": "Собака",
  "age": 3
}
```

**Response (404):**

```json
{
  "detail": "Not found"
}
```

---

### 🛠 Обновить животное

**PUT** `/animals/{animal_id}`

**Request body:**

```json
{
  "name": "Барсик",
  "species": "Кот",
  "age": 5
}
```

**Response:**

```json
{
  "id": 0,
  "animal": {
    "name": "Барсик",
    "species": "Кот",
    "age": 5
  }
}
```

---

### ❌ Удалить животное

**DELETE** `/animals/{animal_id}`

**Response:**

```json
{
  "message": "Deleted"
}
```

---

## 📎 Документация OpenAPI

Автоматически доступна по адресу:
[http://localhost:8000/docs](http://localhost:8000/docs)
