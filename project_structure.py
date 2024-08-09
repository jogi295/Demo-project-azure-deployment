import os

def create_project_structure(root_folder):
    folders = [
        'data',
        'src',
        'logs',
        'metrics',
        'notebooks',
        'models',
        'templates',
    ]

    files = [
        'Dockerfile',
        'app.py',
    ]

    for folder in folders:
        os.makedirs(os.path.join(root_folder, folder), exist_ok=True)

    for file in files:
        open(os.path.join(root_folder, file), 'w').close()

if __name__ == "__main__":
    project_root = "."  # You can specify the root folder here
    create_project_structure(project_root)
    print("Project structure created successfully.")
