# SqlAlchemy Boilerplate with Docker Compose, Makefile, and PostgreSQL

This is a basic template for projects configured to use Docker Compose, Makefile, and PostgreSQL.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yoocontext/sqlalchemy_example.git
   cd sqlalchemy_example

2. Install all required packages in `Requirements` section.
    ```bash
   pip install poetry
   poetry install

### Implemented Commands


* `make storages` - up only storages. you should run your application locally for debugging/developing purposes
* `make storages-down` - down all infrastructure
