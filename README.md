# CP_Statistics

## Overview

This project visualizes the total solved problems for a given user across multiple competitive programming platforms. It uses APIs and web scraping to gather data from platforms such as Codeforces, LeetCode, CodeChef, AtCoder, UVA, and SPOJ, and visualizes this data using Matplotlib.

## Features

- **Data Collection**: Uses APIs and web scraping to collect the number of solved problems for a given user from various competitive programming platforms.
- **Data Visualization**: Generates pie charts to represent the distribution of solved problems across different platforms.
- **Technologies Used**: Python, Matplotlib, APIs, Web Scraping.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Islam-Imad/CP_Statistics.git
    cd CP_Statistics
    ```

1. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**: Execute the main script to gather data and generate the visualizations.
    ```bash
    python app.py
    ```

3. **View the results**: The generated pie charts will be saved in the `output` directory.

## Project Structure

    CP_Statistics/
    ├── app.py
    ├── backend.py
    ├── output/
    │ └── pie_chart.png
    ├── requirements.txt
    └── README.md

- **app.py**: The main script that integrates data collection and visualization.
- **backend.py**: Contains the `Platform` class and platform-specific implementations for gathering data.
- **output/**: Directory where the generated visualizations are saved.
- **requirements.txt**: List of dependencies required to run the project.