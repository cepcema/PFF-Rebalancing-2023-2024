#     PFF-Rebalancing-2023-2024

![Example pic](https://i.ibb.co/qBrfCZp/1.jpg)


This project is aimed at analyzing historical financial data and generating visualizations for analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project utilizes Python libraries such as pandas, matplotlib, and scikit-learn to analyze historical financial data stored in CSV format. It generates visualizations, including graphs depicting adjusted close prices, volume, and average daily volume, and identifies specific dates for rebalancing. Linear regression models are also fitted to the data for each symbol to analyze trends over time.

## Features

- Read historical financial data from CSV files.
- Plot adjusted close prices and volume on interactive graphs.
- Identify rebalancing dates and display corresponding price changes.
- Fit linear regression models to analyze trends in the data.
- Generate visualizations for multiple symbols in a single run.

## Requirements

- Python 3.x
- pandas
- matplotlib
- scikit-learn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the historical financial data stored in CSV format.

2. Modify the `file_path` variable in the script to point to your CSV file.

3. Run the script:

    ```bash
    python financial_analysis.py
    ```

4. After execution, the output graphs will be saved in the `output_graphs` folder.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



