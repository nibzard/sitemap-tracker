# Sitemap Tracker

Welcome to the **Sitemap Tracker** project! This tool helps you use GH Actions to track sitemap data over time, generate dummy data for testing, and analyze URL metrics.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example Output](#example-output)
5. [Contributing](#contributing)
6. [License](#license)

## Project Structure

```
sitemap-tracker
├── dummy_data.py
├── analysis.py
├── requirements.txt
├── README.md
├── url_metrics_over_time.png
├── dummy_sitemap_data.csv
├── sitemap_tracker.py
└── data
    └── sitemap_stats.csv
```

- **dummy_data.py**: Script to generate dummy sitemap data for testing and development purposes.
- **analysis.py**: Script for analyzing sitemap data and generating visual plots of metrics over time.
- **requirements.txt**: List of required Python packages.
- **README.md**: Project documentation.
- **url_metrics_over_time.png**: Example plot image of URL metrics over time.
- **dummy_sitemap_data.csv**: CSV file containing dummy sitemap data.
- **sitemap_tracker.py**: Main script to fetch and process real sitemap data from specified URLs.
- **data/sitemap_stats.csv**: CSV file storing the statistics of URLs from sitemaps over time.

## Setting Up Daytona Workspace

**Steps to Set Up Daytona Workspace**

1. Create [Daytona](https://github.com/daytonaio/daytona) Workspace:

    ```bash
    daytona create https://github.com/nkkko/devcontainer-generator
    ```

2. Select Preferred IDE:

    ```bash
    daytona ide
    ```

3. Open the Workspace:

    ```bash
    daytona code
    ```

## Usage

### Generating Dummy Data

You can generate dummy data for sitemaps to test the analysis without fetching real data. The `dummy_data.py` script creates a CSV file named `dummy_sitemap_data.csv` with dummy values:

```sh
python dummy_data.py
```

### Fetching and Processing Real Sitemaps

To fetch and process real sitemap data, update the `SITEMAPS` dictionary in the `sitemap_tracker.py` script with the URLs of the sitemaps you want to track. Then, run the script:

```sh
python sitemap_tracker.py
```

This will fetch the sitemaps, process the data, and store it in `data/sitemap_stats.csv`.

### Analyzing Data

Use `analysis.py` to visualize the metrics of URLs over time:

```sh
python analysis.py
```

This script reads the CSV file (either `data/sitemap_stats.csv` or `dummy_sitemap_data.csv`), generates plots of total and new URLs over time, and saves the plot as `url_metrics_over_time.png`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the project's coding style and add appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using **Sitemap Tracker**! If you have any questions or issues, feel free to open an issue on GitHub.