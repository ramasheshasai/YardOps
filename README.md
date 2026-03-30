# YardOps Backend 🚛

## 📌 Project Description

YardOps is a backend service designed to manage yard operations such as trailers, appointments, and yard spots.
It provides REST APIs to handle logistics efficiently using a scalable microservices-friendly architecture.

The project is containerized using Docker and orchestrated with Docker Compose for consistent development and deployment.

---

## 🛠 Tech Stack

* Python 3.11
* Flask
* SQLAlchemy
* PostgreSQL
* Redis
* Docker & Docker Compose
* Gunicorn

---

## 📁 Project Structure

```
yardops/
│── app/
│── models/
│── routes/
│── tests/
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
```

---

## ⚙️ Prerequisites

Make sure you have:

* Docker installed
* Rancher Desktop (or Docker Desktop alternative)

---

## 🐳 Setup using Rancher Desktop

1. Install Rancher Desktop

2. Enable:

   * container runtime (dockerd)
   * kubectl (optional)

3. Verify installation:

```bash
docker --version
docker-compose --version
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <my-repo-url>
cd yardops
```

---

### 2. Build and start containers

```bash
docker-compose up --build
```

---

### 3. Verify running containers

```bash
docker ps
```

You should see:

* yardops_app
* yardops_postgres
* yardops_redis

---

### 4. Access the application

```
http://localhost:5000
```

---

## 🗄️ Services Overview

### 🔹 App Service (`yardops_app`)

* Runs Flask application using Gunicorn
* Handles API requests

### 🔹 PostgreSQL (`yardops_postgres`)

* Main database
* Persistent storage using Docker volumes

### 🔹 Redis (`yardops_redis`)

* Caching layer / fast in-memory storage

---

## 🔗 Environment Variables

| Variable     | Description                  |
| ------------ | ---------------------------- |
| DATABASE_URL | PostgreSQL connection string |
| REDIS_URL    | Redis connection string      |
| PYTHONPATH   | Application path             |

Example:

```
postgresql://postgres:postgres@postgres:5432/yardops
```

---


## 📡 API Endpoints

---

### 🔹 Trailer APIs

#### ➤ Create Trailer
**POST** `/api/trailers`

**Request Body**
```json
{
  "trailer_type": "REEFER",
  "trailer_number": "1234",
  "carrier_name": "ABC",
  "temp_setting": -10
}
````

**Response (201)**

```json
{
  "id": 1,
  "trailer_type": "REEFER",
  "trailer_number": "1234",
  "carrier_name": "ABC",
  "temp_setting": -10
}
```

---

#### ➤ Get Trailers

**GET** `/api/trailers`

**Query Params (optional)**

* `trailer_type`
* `carrier_name`

---

### 🔹 Site APIs

#### ➤ Create Site

**POST** `/api/sites`

**Request Body**

```json
{
  "name": "Site A",
  "address": "Chennai"
}
```

**Response (201)**

```json
{
  "id": 1,
  "name": "Site A",
  "address": "Chennai"
}
```

---

#### ➤ Get Site

**GET** `/api/sites/{site_id}`

**Response (200)**

```json
{
  "id": 1,
  "name": "Site A",
  "address": "Chennai"
}
```

---

#### ➤ Create Yard Spot

**POST** `/api/sites/{site_id}/spots`

**Request Body**

```json
{
  "spot_label": "A1"
}
```

**Response (201)**

```json
{
  "id": 1,
  "spot_label": "A1",
  "site_id": 1
}
```

---

### 🔹 Appointment APIs

#### ➤ Check-in Trailer

**POST** `/appointments/checkin`

**Request Body**

```json
{
  "site_id": 1,
  "trailer_id": 2,
  "preferred_spot_id": 1
}
```

**Response (201)**

```json
{
  "id": 1,
  "status": "CHECKED_IN",
  "gate_pass": "abc123",
  "yard_spot_id": 1
}
```

---

#### ➤ Check-out Trailer

**POST** `/appointments/{appointment_id}/checkout`

**Response (200)**

```json
{
  "message": "checked out successfully",
  "appointment_id": 1
}
```

---

### 🔹 Dashboard APIs

#### ➤ Get Trailer Count

**GET** `/api/dashboard/{site_id}`

**Response (200)**

```json
{
  "site_id": 1,
  "trailer_count": 3
}
```

---

#### ➤ Warm Cache

**POST** `/api/dashboard/warm`

**Response (200)**

```json
{
  "message": "Cache warmed successfully",
  "data": [
    {
      "site_id": 1,
      "trailer_count": 3
    }
  ]
}
```


## 🧪 Running Tests

```bash
docker-compose exec app pytest -v
```

---

## 🧹 Useful Commands

### Stop containers

```bash
docker-compose down
```

### Rebuild containers

```bash
docker-compose up --build
```

### Run single service

```bash
docker-compose up app
```

---

## 💾 Volumes

* `postgres_data` → persists PostgreSQL data

---

## 🧠 Key Concepts Used

* Containerization
* Microservices architecture
* Factory Pattern (for object creation)
* REST API design
* Environment-based configuration

---

## ⚡ Troubleshooting

### Issue: Tables not visible

* Ensure migrations are run:

```bash
docker-compose exec app flask db upgrade
```

### Issue: Port already in use

* Change ports in `docker-compose.yml`

---

## 👨‍💻 Author

Ram Sai

---

## 📄 License

This project is for learning and development purposes.
