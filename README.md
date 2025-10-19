# 📄 Document Processing Pipeline

A **modular, scalable document processing pipeline** that accepts PDF files through an API, parses them asynchronously using Apache Tika, and stores the results in Redis.
The system uses Celery with RabbitMQ as the broker and is fully containerized with Docker and Docker Compose.

---

## 🧱 Architecture

```
Client → API (FastAPI) → Celery → RabbitMQ → Tika Parser → Redis
```

* **API** – handles file upload and task management
* **Tika** – extracts text from PDFs
* **Celery** – runs background parsing tasks
* **RabbitMQ** – queues Celery tasks
* **Redis** – stores parsed text results

---

## 🚀 Features

* Upload PDF files via REST API
* Asynchronous parsing using Celery
* Text extraction powered by Apache Tika
* Task status & result retrieval by ID
* Fully containerized stack with Docker Compose

---

## 🐳 Services

| Service       | Port       | Description               |
| ------------- | ---------- | ------------------------- |
| API (FastAPI) | 8000       | Upload & retrieve results |
| Tika          | 9998       | PDF text extraction       |
| RabbitMQ      | 5672/15672 | Message broker (web UI)   |
| Redis         | 6379       | Result backend            |
| Celery Worker | —          | Processes parsing tasks   |

---

## 📦 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-pipeline.git
cd pdf-pipeline
```

### 2. Build and Start the Services

```bash
docker-compose up --build
```

### 3. Access Services

* API: `http://localhost:8000`
* RabbitMQ Dashboard: `http://localhost:15672` (default user/pass: guest/guest)
* Tika: `http://localhost:9998/tika`

---

## 🧪 API Usage

### ➕ Upload PDF

```bash
curl -F "file=@document.pdf" http://localhost:8000/upload
```

**Response:**

```json
{"task_id": "e3a4f2b7-..." }
```

### 📊 Check Task Status

```bash
curl http://localhost:8000/status/e3a4f2b7-...
```

**Response:**

```json
{"status": "PENDING"}
```

### 📥 Retrieve Result

```bash
curl http://localhost:8000/result/e3a4f2b7-...
```

**Response:**

```json
{"text": "Extracted text content ..."}
```

---

## ⚙️ Configuration

* **Celery Broker:** RabbitMQ
* **Celery Backend:** Redis
* **Tika Service:** Containerized and exposed on port 9998

All configurations can be modified in `docker-compose.yml` and `.env`.

---

## 🧭 Project Structure

```
.
├── api/
│   ├── main.py
│   └── celery_app.py
├── tasks/
│   └── parse_pdf.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

* 🐍 Python / FastAPI
* 🐇 RabbitMQ
* 🌿 Redis
* 🪶 Apache Tika
* 🐳 Docker & Docker Compose
* 🧭 Celery (async processing)

---

## 📝 How It Works

1. API receives a PDF upload and queues a task with Celery.
2. Celery worker pulls the task from RabbitMQ.
3. The file is sent to Tika for parsing.
4. Extracted text is stored in Redis.
5. The user can query the task status or fetch the result.

---

## 🧪 Testing

* Upload a sample PDF and monitor the logs:

  ```bash
  docker-compose logs -f worker
  ```
* Use the task ID to check status and get results.

---

## 🧼 Cleanup

```bash
docker-compose down
```

---


