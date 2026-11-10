# CivicFix - Database-Backed API

CivicFix is a REST API for reporting and managing civic issues. It allows users to report issues, retrieve issue information, update existing reports, and delete reports. The application uses FastAPI and PostgreSQL for persistent data storage.

## Technologies Used

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Docker and Docker Compose
- Psycopg

## 1. Clone the Repository

```bash
git clone https://github.com/didarulshahriar37/CivicFix.git
cd CivicFix
```

## 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn sqlmodel psycopg[binary] python-dotenv
```

## 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
POSTGRES_USER=YOUR_DB_USERNAME
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
POSTGRES_DB=YOUR_DB_NAME
DATABASE_URL=postgresql+psycopg://YOUR_DB_USERNAME:YOUR_DB_PASSWORD@localhost:5433/civicfix
```

**Note:** The PostgreSQL container uses port `5432` internally, while port `5433` is exposed on the host machine to avoid conflicts with other PostgreSQL installations.

## 5. Start PostgreSQL Using Docker

Start the database container:

```bash
docker compose up -d
```

Check whether the database is running:

```bash
docker compose ps
```

You can also verify database readiness:

```bash
docker compose exec db pg_isready -U civicfix_user -d civicfix
```

## 6. Run the FastAPI Application

From the project root directory, execute:

```bash
fastapi dev main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 7. Access API Documentation

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/issues` | Retrieve all issues |
| POST | `/users` | Create a user |
| POST | `/issues` | Create a new issue |
| GET | `/issues/{issue_id}` | Retrieve a specific issue |
| PUT | `/issues/{issue_id}` | Update an existing issue |
| DELETE | `/issues/{issue_id}` | Delete an issue |

## 8. Stop the Application

Stop the FastAPI server using `Ctrl + C`.

To stop the PostgreSQL container:

```bash
docker compose down
```

## Project Structure

```text
CivicFix/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── .env
├── .gitignore
├── docker-compose.yml
└── README.md
```