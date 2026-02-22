# Pokémon Data Files

A Python project for generating structured Pokémon datasets and populating PostgreSQL databases. Exports data to Excel, CSV, and SQL formats using Pandas, making it ideal for data analysis, visualization, and database management.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Related Repositories](#related-repositories)
- [License](#license)

---

## Overview

Pokémon Data Files provides a complete pipeline for:

1. **Data Generation** — Scripts to generate Pokémon-related entities (Pokémon, owners, reviewers, categories, etc.)
2. **Format Conversion** — Export to Excel, CSV, and SQL
3. **Database Population** — Insert generated CSV data into PostgreSQL (local or cloud)

---

## Features

- Generate structured Pokémon dataset with relationships
- Export to multiple formats: CSV, SQL, Excel
- PostgreSQL support (local and cloud)
- Configurable via environment variables
- Python 3.10+ compatible

---

## Project Structure

```
Pokemon-Data-Files/
├── DB_Create/
│   ├── generate_category.py
│   ├── generate_country.py
│   ├── generate_owner.py
│   ├── generate_pokemon.py
│   ├── generate_pokemon_category.py
│   ├── generate_pokemon_owner.py
│   ├── generate_review.py
│   └── generate_reviewer.py
├── DB_Create/report/
│   ├── CSV/           # Generated CSV files
│   └── SQL/           # Generated SQL files
├── filter_pokemon_data.py
├── convert_to_csv_sql.py
├── generate_all_database_files.py
├── insert_data_in_db.py    # Main script to populate database
├── main.py
├── pyproject.toml
├── .env.example
└── README.md
```

---

## Prerequisites

- Python 3.10 or higher
- PostgreSQL (local or cloud instance)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

---

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/Pokemon-Data-Files.git
cd Pokemon-Data-Files

# Install dependencies
uv sync
```

### Using pip

```bash
pip install -r requirements.txt
# or
pip install psycopg2 python-dotenv pandas openpyxl
```

---

## Configuration

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your database credentials and CSV paths.  
   See [Environment Variables](#environment-variables) for details.

---

## Usage

### Generate database files (CSV & SQL)

```bash
python generate_all_database_files.py
```

### Insert CSV data into database

```bash
python insert_data_in_db.py
```

Ensure your CSV files exist in `DB_Create/report/CSV/` and paths in `.env` are correct.

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DB_NAME` | Local database name | `postgres` |
| `DB_USER` | Local database user | `postgres` |
| `DB_PASSWORD` | Local database password | — |
| `DB_HOST` | Local database host | `localhost` |
| `DB_PORT` | Local database port | `5432` |
| `DB_NAME_CLOUD` | Cloud database name | — |
| `DB_USER_CLOUD` | Cloud database user | — |
| `DB_PASSWORD_CLOUD` | Cloud database password | — |
| `DB_HOST_CLOUD` | Cloud database host | — |
| `DB_PORT_CLOUD` | Cloud database port | `5432` |
| `CSV_PATH_*` | Paths to CSV files | See `.env.example` |

Full list and descriptions are in [`.env.example`](.env.example).

---

## Related Repositories

| Project | Description | Link |
|---------|-------------|------|
| **Backend** | API server and database layer | `https://github.com/Quantum-Pvt-Ltd/PokemonReviewApp.git` |
| **Frontend** | Web application UI | `https://github.com/Quantum-Pvt-Ltd/Pokemon-Frontend.git` |

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

*Built with* Python · PostgreSQL · Pandas *and lots of love* ❤️‍🔥💜
