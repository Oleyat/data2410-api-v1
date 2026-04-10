# data2410-api-v1

A simple ASP.NET Core Web API for managing students, built with .NET 10 and Azure SQL.

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) (LocalDB, SQL Server Express, or Azure SQL)

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/data2410-api-v1.git
cd data2410-api-v1
```

## Local Database Setup

### Option A: SQL Server LocalDB (included with Visual Studio)

No installation needed if you have Visual Studio installed. LocalDB is already available.

### Option B: SQL Server Express

Download and install [SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).

## Configure the Connection String

Create a file named `appsettings.Development.json` in the project root (this file is gitignored):

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=StudentsDb;Trusted_Connection=True;TrustServerCertificate=True;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  }
}
```

> **Note:** If using SQL Server Express instead of LocalDB, replace the connection string with:
> ```
> Server=localhost\\SQLEXPRESS;Database=StudentsDb;Trusted_Connection=True;TrustServerCertificate=True;
> ```

The `Students` table is created automatically on startup — no manual database setup needed.

## Run the Project

```bash
dotnet restore
dotnet run
```

The API will start at `https://localhost:7010`.

## API Documentation

Once running, open the interactive API docs at:

```
https://localhost:7010/scalar/v1
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/Students` | Get all students |
| GET | `/api/Students/{id}` | Get a student by ID |
| POST | `/api/Students` | Create a new student |
| PUT | `/api/Students/{id}` | Update a student |
| DELETE | `/api/Students/{id}` | Delete a student |
| POST | `/api/Students/calculate-grades` | Calculate grades for all students |
| GET | `/api/Students/report` | Generate student report |
| GET | `/health` | Check database connectivity |

### Example: Create a Student

```bash
curl -X POST https://localhost:7010/api/Students \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "course": "DATA2410", "marks": 85}'
```

### Grading Scale

| Marks | Grade |
|-------|-------|
| 90+ | A |
| 80–89 | B |
| 60–79 | C |
| Below 60 | D |

## Project Structure

```
data2410-api-v1/
??? Controllers/
?   ??? StudentsController.cs    # API endpoints
??? Models/
?   ??? Student.cs               # Student model
??? Properties/
?   ??? launchSettings.json      # Local launch configuration
??? appsettings.json             # App configuration (no secrets)
??? appsettings.Development.json # Local secrets (gitignored)
??? Program.cs                   # Application entry point
??? data2410-api-v1.csproj       # Project file
```

## Tech Stack

- **Framework:** ASP.NET Core (.NET 10)
- **Database:** SQL Server / Azure SQL
- **Data Access:** Microsoft.Data.SqlClient (raw ADO.NET)
- **API Docs:** Scalar (OpenAPI)
