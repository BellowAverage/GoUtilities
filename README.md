# Comparison of three programming's data analyzing ability

This repository contains a comprehensive comparison of three programming languages—Go, Python, and R—based on their performance and accuracy in performing linear regression on the **Anscombe Quartet** dataset. The primary objective is to analyze the feasibility of using Go for data science tasks in comparison to Python and R. That is, to evaluate and compare the performance (both in terms of results and execution time) of linear regression of each language.

## Project Structure

```
BellowAverageGoUtilities/
│
├── data/
│   ├── anscombe.jl                   # Anscombe Quartet in JSON Lines format
│   ├── miller_mtpa_chapter_1-program.R # Reference R script from Miller
│
├── Go/
│   ├── go_results.txt                # Results output from Go script
│   ├── go.mod                        # Go module file
│   ├── go.sum                        # Go sum file
│   └── main.go                       # Go script for linear regression
│
├── Python/
│   └── main.py                       # Python script for linear regression
│
├── R/
│   └── main.r                        # R script for linear regression
│
├── venv/                             # Virtual environment for Python dependencies
├── launch.bat                        # Batch script for launching the project on Windows
├── launch_with_python3.10.bat        # Alternate launcher for Python 3.10
├── launch.py                         # Python launch script for running all tasks
├── launch.sh                         # Bash script for launching the project on Unix
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies file
├── python_results.txt                # Results output from Python script
├── result.md                         # Comprehensive output report for all languages
└── summary.md                        # Summary and analysis of results
```

## Instructions

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourRepo/BellowAverageGoUtilities.git
    cd BellowAverageGoUtilities
    ```

2. **Install Python dependencies**:
    If you're on Windows, run:
    ```bash
    .\launch.bat
    ```
    If you're on Linux/Mac, run:
    ```bash
    bash launch.sh
    ```
    This script sets up the virtual environment and installs required Python dependencies.

3. **Run the scripts**:
    The `launch.py` script will execute all three language implementations (Python, R, and Go) and compile the results into a `result.md` file:
    ```bash
    python launch.py
    ```
    or
    ```bash
    py launch.py
    ```

### Prerequisites

- **Python**: Ensure Python 3.10 or higher is installed and accessible through `py` or `python` commands.
- **R**: Ensure `Rscript` is available in your PATH.
- **Go**: Ensure Go is installed and the project has the required Go modules by running:
    ```bash
    go mod tidy
    ```

### Expected Output

After running the `launch.py` script, the following will happen:

- Python, R, and Go will each perform linear regression on the Anscombe Quartet dataset.
- Results from each language will be output in `result.md`.
- A comparative analysis of the performance and regression outcomes will be provided in `summary.md`.

## Noteworthy Points During Development

### Key Challenges

1. **Go Module Management**:
   Go initially faced issues with finding the correct module paths for external dependencies (`gonum/stat`). A go script finds its packages within the working directory where it is runned. That being said, you cannot do ```go run Go/main.py``` if ```go.mod``` and ```go.sum``` are in the ```Go``` directory. Switching to the correct directory and run solved this.

2. **Intercept and Slope Reversal in Go**:
   During the first iteration, Go's regression results swapped the intercept and slope values. This issue was resolved by correctly understanding the output structure of the `github.com/montanaflynn/stats` package.

3. **Cross-Platform Considerations**:
   The need to accommodate both Windows and Unix-based systems required the creation of `.bat` and `.sh` scripts, along with environment-specific setup instructions. Ensuring that Python virtual environments worked correctly across platforms was a priority.

4. **Handling Python Environment**:
   A key challenge was making sure Python was installed and accessible on different systems (Windows, Linux, Mac). The batch script was designed to first try `py` (for systems where `py` launcher is used), then fall back to `python` if `py` is not available.


### Performance Considerations

- **Execution Times**: Go consistently showed the fastest execution time, followed by R, with Python being the slowest. These differences are documented in the output report and analyzed in `summary.md`.

- **NaN Values in Go**: The Go implementation produced some `NaN` values for the fourth dataset, requiring a careful comparison with Python and R to ensure data consistency. This issue was addressed by rechecking the data input format and adjusting the Go code accordingly.

## Results

The `result.md` file contains a detailed output of each language's linear regression results, while the `summary.md` file contains an analysis of those results. 

**Execution Time Comparison**:

| Language | Execution Time (seconds) |
|----------|--------------------------|
| Python   | 1.0678                    |
| R        | 0.0242                    |
| Go       | 0.4672                    |

## Conclusion

For production environments where speed is critical, Go might be a viable option, but for accuracy and consistency, especially in data science contexts, Python and R are still more reliable tools. Though the difference is minor.