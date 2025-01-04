# Obsidian Task Analyzer

A Python script to analyze task completion in an Obsidian vault. The script processes markdown files, identifies completed and incomplete tasks, and generates a summary report.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Testing](#testing)
5. [Contributing](#contributing)

---

## Features
- **Task Extraction**: Extracts tasks from markdown files in an Obsidian vault.
- **Task Categorization**: Categorizes tasks into completed and incomplete.
- **Summary Report**: Generates a summary report with completion percentages and lists of tasks.
- **Exclusion Support**: Allows excluding specific folders from analysis.

---

## Installation

### Prerequisites
- Python 3.8 or higher.
- An Obsidian vault with markdown files containing tasks.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Mosab2099/obsidian-task-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd obsidian-task-analyzer
   ```

---

## Usage

1. Run the script:
   ```bash
   python project.py
   ```
2. Enter the path to your Obsidian vault when prompted.
3. Optionally, specify folders to exclude from the analysis.
4. The script will generate a summary report (`analysis.txt`) in your Obsidian vault directory.

### Example

Enter your Obsidian vault path: /path/to/your/vault
Do you want to exclude any folder? (y/n) n
Analysis created successfully


The `analysis.txt` file will contain:

You've completed 60.0%, you haven't completed 40.0%
These are the completed tasks 3 task.
- [x] Task 1
- [x] Task 2
- [x] Task 3
These are the not completed tasks 2 task.
- [ ] Task 4
- [/] Task 5


---

## Testing

To run the tests:
1. Ensure you have `pytest` installed:
   ```bash
   pip install pytest
   ```
2. Run the tests:
   ```bash
   pytest test_project.py
   ```

### Test Coverage
- **`getting_data`**: Tests if the script correctly extracts tasks from markdown files.
- **`analyzing_data`**: Tests if tasks are correctly categorized into completed and incomplete.
- **`export_data`**: Tests if the summary report is generated correctly.

---

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---


## Acknowledgments
- Inspired by the need to track task completion in Obsidian vaults.
- Built with Python and ❤️.

---

## Contact

For questions or feedback, feel free to reach out:
- **Email**: mr.mosab2000@gmail.com
- **GitHub**: [Mosab2099](https://github.com/Mosab2099)
