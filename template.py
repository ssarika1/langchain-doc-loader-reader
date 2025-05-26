# template.py

import os

# Define the folder structure
FOLDERS = [
    "data",
    "embeddings",
    "retriever",
    "models",
    "outputs",
    "utils",
    "configs",
    "app"
]

# Optional starter files
STARTER_FILES = {
    "README.md": "# RAG Q&A Project\n\nThis is a Retrieval-Augmented Generation Q&A application.",
    "requirements.txt": "",
    "app/__init__.py": "",
    "app/main.py": "# Entry point for the application\n\ndef main():\n    print('Hello, RAG Q&A!')\n\nif __name__ == '__main__':\n    main()"
}

def create_project_structure(base_path="."):
    for folder in FOLDERS:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
    
    for file_name, content in STARTER_FILES.items():
        file_path = os.path.join(base_path, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_project_structure()
