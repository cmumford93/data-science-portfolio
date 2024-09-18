import os

# Define the folder structure
folders = [
    "data-science-portfolio",
    "data-science-portfolio/projects",
    "data-science-portfolio/projects/project1",
    "data-science-portfolio/projects/project2",
    "data-science-portfolio/projects/project3",
    "data-science-portfolio/docs",    # Optional
    "data-science-portfolio/images"   # Optional
]

# Define files to create in each folder
files = {
    "data-science-portfolio/README.md": "",
    "data-science-portfolio/LICENSE": "",
    "data-science-portfolio/projects/project1/notebook.ipynb": "",
    "data-science-portfolio/projects/project1/data.csv": "",
    "data-science-portfolio/projects/project1/README.md": "",
    "data-science-portfolio/projects/project2/notebook.ipynb": "",
    "data-science-portfolio/projects/project2/README.md": "",
    "data-science-portfolio/projects/project3/notebook.ipynb": "",
    "data-science-portfolio/projects/project3/README.md": ""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, 'w') as f:
        f.write(content)

print("Folder structure created successfully!")
