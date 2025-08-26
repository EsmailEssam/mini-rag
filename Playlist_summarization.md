# Playlist Summarization 
This file incloude the summarization of the videos in [mini-RAG | From notebooks to the PRODUCTION](https://youtube.com/playlist?list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&si=h3odvaH6RhVwF7qa) playlist.

## Videos
### mini-RAG | 01 | About the Course ماذا ولمـــاذا
The speaker introduces a new tutorial series focused on building a complete application from scratch to bridge the gap between data science experimentation and real-world software engineering. He explains that a major challenge for data scientists is moving from developing models in notebooks to creating production-ready applications, a skill that requires software engineering knowledge.

The project for this series is called `mini-rag`, which will be a Retrieval-Augmented Generation (RAG) application. This type of application answers user questions based on a provided set of documents, a common use case for Large Language Models (LLMs) today.
The series will cover:
- Building the application step-by-step using Python and a web framework.
- Applying concepts from libraries like LangChain in a practical, real-world project.
- Addressing software engineering practices necessary for deploying data science projects.

------------------------------------

### mini-RAG | 02 | What will we build ماذا سنبنى في المشروع
This video provides an overview of the `mini-rag` project, a minimal implementation of a Retrieval-Augmented Generation (RAG) model. The goal of the first stage of this project is to build a web application using Python and the FastAPI framework that performs the core functions of a RAG system.

The process is broken down into four main steps:
1. **Data Parsing:** The system will allow a user to upload a document (e.g., PDF, text file). It will then parse this document, extract the text, and split it into smaller, manageable pieces called *chunks*.
2. **Indexing:** These chunks are then processed and stored in a vector database. This step makes the information searchable based on semantic meaning.
3. **Semantic Search (Retrieval):** When a user asks a question, the system searches the vector database to find and retrieve the chunks of text that are most relevant to the query.
4. **Answering (Generation):** The user's original question and the retrieved, relevant chunks are combined into a prompt. This prompt is then sent to a Large Language Model (LLM) to generate a final, coherent answer.

The speaker demonstrates that these functionalities will be exposed through a series of API endpoints, which can be interacted with using tools like Postman. This initial implementation will serve as the foundation for the RAG application, with more features to be added in later stages.

------------------------------------

### mini-RAG | 03 | Setup your tools الأدوات الأساسية
This video provides a comprehensive, step-by-step guide on setting up a complete and professional development environment for a Python project, with a strong recommendation for Windows users to leverage the Windows Subsystem for Linux (WSL).

Here is a summary of the key setup stages covered in the video:
1. **Version Control with Git & GitHub**
    - **Core Principle:** Always start any project, no matter how small, by creating a Git repository on a platform like GitHub or Bitbucket.
    - **Action:** Create a new repository on GitHub. This provides version control, backup, and a foundation for collaboration.

2. **Installing the Git Client**
    - **Requirement:** To interact with your GitHub repository from your local machine, you need to install the Git client.
    - **Action:**
        - Go to [git-scm.com/downloads](git-scm.com/downloads).
        - Download and install the appropriate version for your operating system (Windows, Mac, or Linux).
        - Verify the installation by opening a terminal and running `git --version`.

3. **Cloning the Repository**
    - **Action:**
        - On your GitHub repository page, click the green "Code" button and copy the HTTPS URL.
        - In your local terminal, navigate to your desired projects folder and run the command: `git clone <repository_url> <project_folder_name>`.
        - **Note:** The first time you do this, you may be prompted for authentication. You can generate a **Personal Access Token** from your GitHub Developer Settings to use as a password.

4. **Setting Up the Code Editor (Visual Studio Code)**
    - **Recommendation:** The instructor uses Visual Studio Code (VS Code).
    - **Action:**
        - Download and install VS Code from [code.visualstudio.com/download](https://code.visualstudio.com/download).
        - Open your newly cloned project folder in VS Code (`File > Open Folder...`).

5. **Python Environment Management with Miniconda**
    - **Core Principle:** Avoid using the system's global Python. Instead, use a tool like Miniconda to create isolated, project-specific environments.
    - **Action:**
        - Download and install Miniconda from its official documentation page.
        - **Crucial Step for Windows:** During installation, in the "Advanced Options," check the box to **"Add Miniconda3 to my PATH environment variable."**
        - Verify the installation by opening a new terminal and running `conda --version`.

6. **Creating and Activating a Project-Specific Environment**
    - **Action:**
        - Open the integrated terminal in VS Code.
        - Create a new Conda environment with a specific Python version using the command: `conda create -n mini-rag-app python=3.8` (replace the name and version as needed).
        - Activate the new environment: `conda activate mini-rag-app`.
        - Your terminal prompt will change from `(base)` to `(mini-rag-app)`, indicating you are now working inside the isolated environment.

------------------------------------

### mini-RAG | 04 | Project Architecture
This video provides a step-by-step guide on setting up the initial file structure for a Python project, emphasizing best practices for version control and project organization.

Here's a summary of the key steps:
1. **Git Branching:** The instructor begins by creating a new Git branch named `tut-001` for this specific tutorial. He explains the importance of using clear branch naming conventions, such as `feat-` for new features or `bug-` for fixes, especially in team environments.

2. **Project Cleanup:** He cleans up the project directory by deleting most existing files, leaving only the essential `.gitignore` and `LICENSE` files. He then commits this initial cleanup.

3. **.gitignore Setup:** He explains that the `.gitignore` file is used to tell Git which files to ignore. He uses a standard Python `.gitignore` template from GitHub.

4. **`requirements.txt` File:**
    - He creates a `requirements.txt` file to manage the project's Python dependencies.
    - He adds the initial packages: `fastapi` (the web framework) and `uvicorn` (the web server).
    - He stresses the importance of **pinning package versions** (e.g., `fastapi==0.110.2`) to ensure project stability and prevent future updates from breaking the code. He shows how to find the latest version on PyPI.
    - He then installs these packages using `pip install -r requirements.txt`.

5. **Environment Variables (`.env`):**
    - He explains the need for a `.env` file to store configuration variables and secrets (like API keys) that should not be committed to the repository.
    - He creates a .`env.example` file as a template for other developers. This file lists all required environment variables but leaves sensitive values blank.
    - The `.env` file itself is added to `.gitignore` to keep it local.

6. **README File:**
    - He creates a `README.md` file and describes it as the main entry point for any developer.
    - He populates it with essential sections:
        - **Requirements:** Listing necessary software like Python 3.8+.
        - I**nstallation:** Providing clear, step-by-step commands for setting up the environment (using MiniConda), installing required packages, and setting up the environment variables by copying `.env.example` to `.env`.

By the end of the video, a basic but robust project "boilerplate" is established, ready for coding.

------------------------------------

### mini-RAG | 05 | Welcome to FastAPI
Here is a summary of the key points from the video tutorial:
1. **Project & Code Setup:**
    - The presenter starts by creating a new Git branch named `tut-002` to isolate the work for this part of the tutorial.
    - He creates a `main.py` file, which will serve as the entry point for the application.

2. **Creating a Basic FastAPI Application:**
    - Inside `main.py`, he imports the `FastAPI` class: `from fastapi import FastAPI`.
    - He creates an instance of the application: `app = FastAPI()`
    - He defines a simple Python function `welcome()` that returns a JSON message: `{"message": "Hello World!"}`.

3. **Creating an API Endpoint:**
    - To expose the `welcome` function as an API endpoint, he uses a **decorator**.
    - He adds `@app.get("/welcome")` directly above the `welcome` function. This tells FastAPI to execute this function when it receives an HTTP GET request at the `/welcome` path.

4. **Running and Testing the Server:**
    - He runs the application from the terminal using the command: `uvicorn main:app`. This starts a local web server.
    - He demonstrates two ways to test the API:
        - **Web Browser:** Navigating to `http://127.0.0.1:8000/welcome` shows the JSON response.
        - **Automatic Documentation (Swagger UI):** Navigating to `http://127.0.0.1:8000/docs` opens an interactive API documentation page where the endpoint can be viewed and tested.

5. **Improving the Development Workflow:**
    - He introduces useful flags for the uvicorn command to improve the development experience:
        - `--reload`: Automatically restarts the server when code changes are saved.
        - `--host 0.0.0.0`: Makes the server accessible from other devices on the same network.
        - `--port 5000`: Changes the default port from 8000 to 5000.
    - The final command for development becomes: `uvicorn main:app --reload --host 0.0.0.0 --port 5000`.

6. **Using Postman for API Testing:**
    - He introduces **Postman** as a powerful tool for testing APIs.
    - He creates a new "Collection" in Postman for the project, sets a base URL variable, and successfully tests the `/welcome` endpoint.
    - He exports the Postman collection as a JSON file and adds it to the project's `assets` folder, making it easy for others to import and use.

Finally, he updates the README.md file with the new instructions and commits all the changes to the Git repository.

------------------------------------

### mini-RAG | 06 | Nested Routes + Env Values
The main goal of this video is to demonstrate how to transition a basic, single-file FastAPI application into a more organized and maintainable structure. This is a crucial step for building any application that is expected to grow.

Here are the key concepts and steps covered:
1. **The Problem: The Single-File Application**
    - The video starts with a simple `main.py` file that contains the FastAPI app instance and a single route (`/welcome`).
    - The presenter explains that putting all routes into one file is not a scalable practice. As an application grows, this file becomes large, difficult to read, and hard to maintain.
    - **Best Practice:** The `main.py` file should be kept minimal, acting as the main entry point that assembles different parts of the application.

2. **Solution: Separating Routes into a Module**
    - To solve this, the routes are moved into their own dedicated Python module.
    - A new directory named `routes` is created.
    - Inside `routes`, an empty `__init__.py` file is added. This tells Python to treat the `routes` directory as a package, allowing for imports from it.
    - A new file, `base.py`, is created inside the `routes` directory to hold the basic application routes.

3. **Introducing `APIRouter`**
    - Instead of using the main `app` object to define routes in `base.py`, FastAPI's `APIRouter` is used.
    - In `base.py`, an `APIRouter` instance is created: `base_router = APIRouter()`.
    - The route decorator is changed from `@app.get(...)` to `@base_router.get(...)`. This attaches the route to the new router object.

4. **Integrating the Router into the Main App**
    - Back in `main.py`, the old route definition is removed.
    - The `base` module is imported: `from routes import base`.
    - The `base_router` is connected to the main app instance using: `app.include_router(base.base_router)`. This "plugs in" all the routes defined in `base.py` into the main application.

5. **Enhancing the Router with Prefixes and Tags**
    - **Prefixes:** To easily version the API, the `prefix` argument is added to the APIRouter. For example: `prefix="/api/v1"`. This automatically adds `/api/v1` before every route path defined in that router, so `/` becomes `/api/v1/`.
    - **Tags:** The `tags` argument is also added, for example: `tags=["api_v1"]`. This helps group related endpoints in the auto-generated API documentation (like Swagger UI), making it much easier to navigate.

6. **Loading Environment Variables**
    - The video shows how to load configuration values (like `APP_NAME` and `APP_VERSION`) from a `.env` file instead of hardcoding them.
    - The `python-dotenv` library is added to `requirements.txt` and installed.
    - In `main.py`, `load_dotenv()` is called once at the start to load all variables from the `.env` file into the system's environment.
    - In the `base.py` route, the `os` module is imported, and variables are accessed using `os.getenv("VARIABLE_NAME")`.
    - The welcome route is updated to return the app name and version dynamically from these environment variables.

7. **Final Best Practice: `async` Functions**
    - The presenter adds the `async` keyword before the route function definition (`async def welcome():`). He explains this is a best practice in FastAPI for better performance, as it allows the server to handle multiple requests concurrently without blocking.

By the end of the video, the application has been refactored from a simple script into a well-structured project with separated concerns, API versioning, and dynamic configuration, making it ready for future expansion.

------------------------------------

### mini-RAG | 07 | Uploading a File
The video's main objective is to build the first core feature for the "mini-rag" project: a file upload endpoint. However, the focus is not just on making it work, but on building it correctly using best practices for software architecture, configuration management, and error handling to ensure the application is maintainable and scalable.
Step-by-Step Implementation:
1. **Project Restructuring:**
    - A `src` directory is created, and all source files (`main.py`, `routes`, `assets`, `.env`) are moved inside it.
    - New directories are created within `src`: `controllers`, `models`, and `helpers`.

2. **Configuration with `pydantic-settings`:**
    - The `pydantic-settings` library is added to `requirements.txt`.
    - A `config.py` file is created in `helpers` to define a `Settings` class that loads variables from the `.env` file.
    - New variables for allowed file types and max file size are added to the `.env` and `Settings` class.

3. **Creating the Upload Endpoint:**
    - A new router file, `routes/data.py`, is created for data-related operations.
    - A `POST` endpoint is defined at `/upload/{project_id}` which accepts a `project_id` and a file of type `UploadFile`.

4. **Separating Logic into Controllers:**
    - A `BaseController` is created to handle shared logic like loading settings.
    - A `DataController` and `ProjectController` are created, inheriting from `BaseController`.
    - The `DataController` contains the file validation logic (`validate_uploaded_file`) and logic to generate a unique, clean filename.
    - The `ProjectController` contains logic to create a project-specific directory path for storing files (`assets/files/{project_id}`).

5. **Handling Responses with Enums:**
    - An `enums` directory is created inside `models`.
    - A `ResponseSignal` Enum is defined to hold all possible response messages as constants, improving code readability and maintainability.

6. **Saving the File:**
    - The `aiofiles` library is used within the `/upload` endpoint.
    - The code opens the destination file path for writing in binary (`wb`).
    - It then reads the uploaded file in chunks and writes each chunk to the destination file.

7. **Finalizing the Endpoint:**
    - The endpoint first validates the file. If invalid, it returns a `400 Bad Request` with an appropriate error signal.
    - If valid, it proceeds to save the file. If saving fails, it returns a `400 Bad Request` with a "file upload failed" signal.
    - If everything succeeds, it returns a `200 OK` status with a "file upload success" signal.
    - The new `data_router` is included in the main `FastAPI` app instance in `main.py`.

The process is tested at each stage using **Postman**, demonstrating how the endpoint correctly handles both successful uploads and validation failures.

------------------------------------

### mini-RAG | 08 | File Processing
The video continues the development of an open-source Retrieval-Augmented Generation (RAG) application using Python and FastAPI. The main focus is on creating the logic to process uploaded files by extracting their content and splitting it into smaller chunks.

Here are the key steps covered:
1. **Refactoring the Upload Endpoint:**
    - The `generate_unique_filename` function was renamed to `generate_unique_file_path`.
    - It was modified to return both the full file path and a unique `file_id`.
    - The `/upload` endpoint's successful response was updated to include this `file_id`, which allows users to reference the uploaded file in subsequent API calls.

2. **Creating a New "Process" Endpoint:**
     - A new `POST` endpoint `/api/v1/data/process/{project_id}` was created to handle the processing of an uploaded file.
     - **Pydantic Schema:** A Pydantic schema (`ProcessRequest`) was defined to validate the incoming request body. This schema requires a `file_id` and accepts optional parameters for `chunk_size` and `overlap_size` with default values.

3. **Implementing File Processing Logic:**
    - A new `ProcessController` was created to encapsulate the business logic for file handling, separating it from the API routes.
    - **Using LangChain:** The `langchain` library was introduced and added as a dependency to handle document loading and text splitting. Specifically, `TextLoader` for `.txt` files and `PyMuPDFLoader` for `.pdf` files were used.
    - **Chunking:** The concept of chunking (splitting large texts into smaller pieces) was explained as essential for RAG. The `RecursiveCharacterTextSplitter` from LangChain was chosen for this task because it intelligently splits text while trying to preserve semantic context (like keeping sentences together).

4. **Integration and Testing:**
    - The new `ProcessController` logic was integrated into the `/process` endpoint.
    - The endpoint now:
        - Initializes the `ProcessController` with the `project_id`.
        - Calls a method to get the file's content using the appropriate LangChain loader based on its extension.
        - Calls another method to process the content, splitting it into chunks based on the `chunk_size` and `overlap_size` provided in the request.
    - The final implementation was tested using Postman, successfully demonstrating how to upload a file and then call the process endpoint to receive a list of text chunks in the response.

------------------------------------

### mini-RAG | 09 | Docker - MongoDB - Motor
This video explains how to integrate a MongoDB database into a project to store file chunks.

Key topics covered include:

1.  **Choosing a Database:** The presenter decides to use **MongoDB**, a NoSQL, document-based database. He briefly discusses the importance of understanding the difference between database types like NoSQL (e.g., MongoDB) and SQL (e.g., MySQL) to make informed architectural decisions.

2.  **Setting up MongoDB with Docker:** Instead of installing MongoDB directly, the presenter opts to use **Docker** for a portable and consistent setup.
    -   He explains how to install **Docker Desktop** (with the WSL 2 backend on Windows).
    -   He creates a `docker-compose.yml` file to define the MongoDB service.
    -   The configuration specifies the official MongoDB `image`, a `container_name`, and maps the internal port `27017` to a host port `27007`.
    -   He configures a **volume** (`./mongodb:/data/db`) to ensure the database data persists on the host machine even after the container stops.
    -   He runs the container using the "Compose Up" command.

3.  **Connecting to the Database:**
    -   He uses a GUI tool called **Studio 3T** to connect to the running MongoDB instance on `localhost:27007` and verify it's working.
    -   He adds the `MONGODB_URL` and `MONGODB_DATABASE` name to the `.env` file and the corresponding Pydantic settings in `config.py`.

4.  **Integrating with FastAPI:**
    -   He installs the **`motor`** library, an asynchronous Python driver for MongoDB, which is ideal for use with FastAPI.
    -   In `main.py`, he uses FastAPI's lifecycle events (`@app.on_event("startup")` and `@app.on_event("shutdown")`).
    -   On **startup**, the application creates a connection client (`AsyncIOMotorClient`) and attaches it to the `app` object, making it globally accessible within the application context.
    -   On **shutdown**, the connection is properly closed.

5.  **Defining Data Models (Schemas):**
    -   He creates a new `db_schemes` folder inside `models` to define the structure of the data that will be stored.
    -   Using **Pydantic's `BaseModel`**, he creates schemas for two collections:
        -   **`Project`:** Contains the project ID.
        -   **`DataChunk`:** Contains the chunk text, metadata, order, and a reference to its project ID.
    -   He explains how to handle MongoDB's `ObjectId` type within Pydantic and how to add custom validators to fields.

By the end of the video, the application is fully configured to connect to a MongoDB database running in Docker, with clear data models defined for storing projects and their associated text chunks.

------------------------------------

### mini-RAG | 10 | Mongo Schemes and Models
This video focuses on building the data model layer for a Python RAG (Retrieval-Augmented Generation) application, enabling interaction with a MongoDB database using the `motor` asynchronous client.

Here's a breakdown of the main steps and concepts:

*   **Recap:** starting by recapping the previous session, which involved setting up MongoDB with Docker and Docker Compose, connecting to it from FastAPI, and defining Pydantic schemas for `Project` and `DataChunk`.
*   **BaseDataModel:** A `BaseDataModel.py` file is created to act as a parent class for all data models. Its `__init__` method is set up to receive the `db_client` connection object and application settings, making them available to all child models.
*   **ProjectModel Implementation:**
    *   A `ProjectModel.py` is created, with a class that inherits from `BaseDataModel`.
    *   An `enum` (`DataBaseEnum.py`) is created to centrally manage the names of database collections (e.g., "projects", "chunks").
    *   Functions are defined to handle database operations for projects:
        *   `create_project`: Inserts a new project into the database.
        *   `get_or_create_project`: Finds a project by its ID, and if it doesn't exist, creates it.
        *   `get_all_projects`: Retrieves all projects with **pagination** to efficiently handle large amounts of data using `skip()` and `limit()`.
*   **ChunkModel Implementation:**
    *   A `ChunkModel.py` is created similarly.
    *   Functions are defined for chunk operations, including `create_chunk` (to insert one chunk) and `insert_many_chunks`.
    *   **Bulk Insert:** To efficiently insert many chunks at once, the `insert_many_chunks` function uses MongoDB's `bulk_write` operation, which is much more performant than inserting chunks one by one in a loop.
*   **Pydantic & MongoDB `_id`:** The instructor addresses a common issue where Pydantic models conflict with MongoDB's `_id` field (as Pydantic treats fields starting with an underscore `_` as private). The solution is to use the `alias` feature in the Pydantic Field, for example: `id: Optional[ObjectId] = Field(None, alias='_id')`.
*   **Integration with API Routes:** Finally, the newly created data models are integrated into the FastAPI endpoints (`data.py`). The code is updated to:
    1.  Get or create a project when a file is uploaded or processed.
    2.  After a file is processed and split into chunks, use the `insert_many_chunks` function to save all the chunks to the database in a single, efficient operation.
    3.  Implement a `do_reset` feature that deletes all existing chunks for a project before inserting new ones.

By the end of the video, the application has a robust data layer that can successfully create projects and store document chunks in the MongoDB database.

------------------------------------