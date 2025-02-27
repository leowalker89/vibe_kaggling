#!/usr/bin/env python3
"""
Script to create a new Kaggle competition project with the necessary folder structure.

Usage:
    python create_project.py <project_name> [--competition <competition_url>]

Example:
    python create_project.py titanic --competition https://www.kaggle.com/competitions/titanic
"""

import argparse
import os
import shutil
from pathlib import Path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Create a new Kaggle competition project"
    )
    parser.add_argument(
        "project_name", 
        help="Name of the project (will be used as directory name)"
    )
    parser.add_argument(
        "--competition", 
        help="URL of the Kaggle competition",
        default=""
    )
    return parser.parse_args()


def create_directory_structure(project_dir):
    """Create the directory structure for the project."""
    # Create main directories
    directories = [
        "data/raw",
        "data/processed",
        "data/submissions",
        "notebooks",
        "src",
    ]
    
    for directory in directories:
        (project_dir / directory).mkdir(parents=True, exist_ok=True)
        
    # Create a .gitkeep file in empty directories to ensure they're tracked by git
    for directory in directories:
        gitkeep_file = project_dir / directory / ".gitkeep"
        if not list((project_dir / directory).glob("*")):
            gitkeep_file.touch()


def create_readme(project_dir, project_name, competition_url):
    """Create a README.md file for the project."""
    readme_content = f"""# {project_name.title()} - Kaggle Competition

## Competition Overview
[Brief description of the competition]

Competition Link: [{competition_url}]({competition_url})

## Project Structure
```
├── data/                 # Data files (not tracked by git)
│   ├── raw/              # Original, immutable data
│   ├── processed/        # Cleaned, transformed data
│   └── submissions/      # Submission files
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code for feature engineering and modeling
└── README.md             # Project documentation
```

## Setup Instructions

### Environment Setup
```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

# Install dependencies
uv add pandas numpy scikit-learn matplotlib seaborn jupyter
```

### Data Setup
1. Download competition data from [{competition_url}]({competition_url})
2. Place the data files in the `data/raw/` directory

## Workflow

1. **Data Exploration**: Analyze the dataset in Jupyter notebooks
2. **Feature Engineering**: Develop features based on insights from exploration
3. **Modeling**: Implement and evaluate various models
4. **Submission**: Generate predictions for submission

## Results

[Summary of results and performance]

## Key Insights

[Important findings and lessons learned]
"""
    
    readme_path = project_dir / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme_content)


def create_gitignore(project_dir):
    """Create a .gitignore file for the project."""
    # Copy the root .gitignore file to the project directory
    root_gitignore = Path(".gitignore")
    if root_gitignore.exists():
        project_gitignore = project_dir / ".gitignore"
        shutil.copy(root_gitignore, project_gitignore)
    else:
        # Create a basic .gitignore if the root one doesn't exist
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
.env
.venv/
venv/
ENV/

# Jupyter
.ipynb_checkpoints

# Data files
*.csv
*.xlsx
*.xls
*.db
*.sqlite3

# Mac OS
.DS_Store
"""
        gitignore_path = project_dir / ".gitignore"
        with open(gitignore_path, "w") as f:
            f.write(gitignore_content)


def create_env_example(project_dir, competition_url):
    """Create a .env.example file for the project."""
    # Extract competition name from URL if available
    competition_name = ""
    if competition_url:
        competition_name = competition_url.rstrip("/").split("/")[-1]
    
    env_content = f"""# Kaggle API credentials
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key

# Competition specific settings
COMPETITION_NAME={competition_name}
DATA_PATH=./data/raw

# Model settings
RANDOM_SEED=42
"""
    
    env_path = project_dir / ".env.example"
    with open(env_path, "w") as f:
        f.write(env_content)


def create_notebook(project_dir):
    """Create a starter Jupyter notebook for exploration."""
    notebook_content = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Exploration\n",
    "\n",
    "This notebook contains initial exploration of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set up visualization settings\n",
    "%matplotlib inline\n",
    "plt.style.use('seaborn-v0_8-whitegrid')\n",
    "sns.set_palette('deep')\n",
    "plt.rcParams['figure.figsize'] = [12, 8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Load the data\n",
    "train_df = pd.read_csv('../data/raw/train.csv')\n",
    "test_df = pd.read_csv('../data/raw/test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Examine the data\n",
    "print(f\"Train shape: {train_df.shape}\")\n",
    "print(f\"Test shape: {test_df.shape}\")\n",
    "train_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Check for missing values\n",
    "train_df.isna().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Analysis\n",
    "\n",
    "Add your data analysis here."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""
    
    notebook_path = project_dir / "notebooks" / "exploration.ipynb"
    with open(notebook_path, "w") as f:
        f.write(notebook_content)


def main():
    """Main function to create a new project."""
    args = parse_args()
    
    # Create project directory
    project_name = args.project_name.lower().replace(" ", "_")
    project_dir = Path(project_name)
    
    if project_dir.exists():
        print(f"Project directory '{project_name}' already exists.")
        overwrite = input("Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("Aborting project creation.")
            return
    
    # Create the project structure
    project_dir.mkdir(exist_ok=True)
    
    print(f"Creating project structure for '{project_name}'...")
    create_directory_structure(project_dir)
    
    print("Creating README.md...")
    create_readme(project_dir, project_name, args.competition)
    
    print("Creating .gitignore...")
    create_gitignore(project_dir)
    
    print("Creating .env.example...")
    create_env_example(project_dir, args.competition)
    
    print("Creating starter notebook...")
    create_notebook(project_dir)
    
    print(f"\nProject '{project_name}' created successfully!")
    print(f"To get started, navigate to the project directory: cd {project_name}")


if __name__ == "__main__":
    main() 