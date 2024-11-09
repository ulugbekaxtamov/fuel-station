## API Endpoints

### **Leaderboard API**

- **LeaderboardAPIView** (`GET /api/v1/petrol-spy/leaderboard/`)

    - Retrieves the top 100 users with the most reports within the last 30 days.
    - If no reports are found within the period, it returns an empty list.

- **LeaderboardWithSqlAPIView** (`GET /api/v1/petrol-spy/leaderboard/with-sql/`)

    - Uses raw SQL for optimized performance and retrieves the same leaderboard data as above.

### **Swagger Documentation**

The project uses **drf-yasg** for Swagger documentation. Access the documentation at:

- **Swagger JSON**: [/swagger.json](http://127.0.0.1:8000/swagger.json)
- **Swagger YAML**: [/swagger.yaml](http://127.0.0.1:8000/swagger.yaml)
- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## **License**

This project is licensed under the **MIT License**.
