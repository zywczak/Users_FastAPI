### Users_FastAPI

#### Cloning the Repository
```bash
git clone https://github.com/zywczak/Users_FastAPI.git
cd Users_FastAPI
```

#### Creating the `.env` File
Create a `.env` file in the root directory of the project and add the following variables: 
```makefile
DB_USER=
DB_PASSWORD=
DB=
DB_HOST=
DB_PORT=
```
Fill in the values according to your database configuration.

#### Installing Dependencies
```bash
pip install -r requirements.txt
```

#### Running the Database with Docker Compose
```bash
docker-compose up -d
```

#### Running the FastAPI Application
```bash
uvicorn app.main:app --reload
```

The application will be available at:

http://127.0.0.1:8000 

Swagger UI (API Documentation):

http://127.0.0.1:8000/docs**  
