Here you can find a tool that automates data cleaning tasks, validates raw data using rule-based constraints, provides data profiling and reporting, and offers automated correction suggestions for common data issues. It's designed to be used both as a standalone tool and as an integrated component in ETL pipelines.

This project is a part of my freelance work that was published with the client's permission.

## Features
- **Data cleaning**  
  - Removal of duplicates  
  - Missing-value imputation (mean, median, mode, constant)  
  - Column name standardization  
  - Outlier detection using z‑score and IQR methods

- **Validation**  
  - JSON-schema based row validation  
  - Custom business rule validations

- **Profiling & reporting**  
  - Missing values and summary statistics reports  
  - Outlier profiling  
  - Generation of comprehensive reports in Markdown and HTML

- **Automated correction suggestions**  
  - Imputation strategy recommendations  
  - Outlier handling suggestions (clip/remove)  
  - Automated application of corrections

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/avrtt/gnomych.git
    cd gnomych
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate # Windows: venv\Scripts\activate
    ```

3. Install the package:
    ```bash
    pip install -e .
    ```

## Usage

To run the command-line tool:
```bash
gnomych --input path/to/input.csv --report output_report.md
```
This will read the CSV file, perform data cleaning, generate a profiling report and save the report in Markdown format.

## Running Tests

To run the tests:
```bash
python -m unittest discover tests
```

## Project structure
```
.
├── README.md
├── .gitignore
├── setup.py
├── requirements.txt
├── gnomych/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cleaning.py
│   ├── validation.py
│   ├── profiling.py
│   ├── reporting.py
│   ├── correction.py
│   ├── exceptions.py
│   └── utils.py
└── tests/
    ├── test_cleaning.py
    ├── test_validation.py
    ├── test_profiling.py
    ├── test_reporting.py
    └── test_correction.py
```

## License 
MIT.