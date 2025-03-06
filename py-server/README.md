# Project Setup

## Initial Setup
```bash
 $ cd <project_directory>
 $ cd py_server
 $ poetry init -n
 $ poetry install --no-root
 $ poetry add fastapi
 $ poetry add uvicorn
 $ poetry add jinja2
```

## Install
```bash
 $ cd <project_directory>
 $ cd py_server
 $ poetry install
```

## Usage
```bash
 $ cd <project_directory>
 $ cd py_server
 $ poetry shell
 $ poetry run uvicorn main:app --reload
```

## Deactivating the Virtual Environment
If you have activated the Poetry shell using `poetry shell`, you can deactivate it using:
```bash
 $ deactivate
```
or
```bash
 $ exit
```

### Explanation

- **Initial Setup:** These commands are used to set up the project initially.
- **Install:** These commands are used to install the dependencies after cloning the project from GitHub.
- **Usage:** This command is used to run the project.
- **Deactivating the Virtual Environment:** Use `deactivate` or `exit` to deactivate the Poetry virtual environment if you have activated it using `poetry shell`.

This structure ensures that anyone cloning the project can easily follow the steps to set up, install dependencies, and run the project.
