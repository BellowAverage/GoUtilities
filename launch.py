
import subprocess
import sys
import time
import os

# Function to install missing Python packages
def install_python_dependencies():
    required_packages = ['pandas', 'numpy', 'matplotlib', 'statsmodels']
    try:
        import pandas
        import numpy
        import matplotlib
        import statsmodels
    except ImportError:
        print("Missing Python dependencies. Installing...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + required_packages)
        print("Dependencies installed successfully.")

# Function to check if R is installed
def check_rscript():
    try:
        subprocess.run(['Rscript', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Rscript not found. Please ensure R is installed and Rscript is available in your PATH.")
        sys.exit(1)

# Function to execute external scripts and capture output and execution time
def run_script(command, cwd=None):
    try:
        start_time = time.time()
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
        end_time = time.time()
        execution_time = end_time - start_time
        output = result.stdout + result.stderr
        return output, execution_time
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure that '{command[0]}' is installed and available in PATH.")
        return "", 0

# Function to read the R results from the external file
def read_r_results():
    r_results_file = "r_results.txt"
    try:
        with open(r_results_file, 'r') as file:
            r_results = file.read()
        return r_results
    except FileNotFoundError:
        print(f"R results file '{r_results_file}' not found.")
        return "No R results found."

# Function to read the Go results from the file
def read_go_results():
    go_results_file = "Go/go_results.txt"
    try:
        with open(go_results_file, 'r') as file:
            go_results = file.read()
        return go_results
    except FileNotFoundError:
        print(f"Go results file '{go_results_file}' not found.")
        return "No Go results found."

# Function to generate a Markdown report
def generate_markdown_report(python_result, python_time, r_result, r_time, go_result, go_time):
    report = f"""
# Comprehensive Report

## Python Results
```
{python_result}
```
**Execution Time (Python):** {python_time:.4f} seconds

## R Results
```
{r_result}
```
**Execution Time (R):** {r_time:.4f} seconds

## Go Results
```
{go_result}
```
**Execution Time (Go):** {go_time:.4f} seconds
"""
    return report

def main():
    # Ensure Python dependencies are installed
    install_python_dependencies()

    # Check if R is installed
    check_rscript()

    # Paths to the scripts
    python_script = os.path.join('Python', 'main.py')
    r_script = os.path.join('R', 'main.r')
    go_script = 'main.go'
    go_dir = os.path.join('Go')

    # Running Python script
    print("Running Python script...")
    python_result, python_time = run_script([sys.executable, python_script])

    # Running R script
    print("Running R script...")
    run_script(['Rscript', r_script])
    r_result = read_r_results()
    r_time = float(r_result.split("Execution Time (R):")[1].strip().split()[0])

    # Running Go script (no need to capture output from console)
    print("Running Go script...")
    go_result, go_time = run_script(['go', 'run', go_script], cwd=go_dir)

    # After running the Go script, read the results from the file
    go_result = read_go_results()

    # Generate the markdown report
    report = generate_markdown_report(python_result, python_time, r_result, r_time, go_result, go_time)

    # Write the report to a markdown file with utf-8 encoding
    with open('result.md', 'w', encoding='utf-8') as f:
        f.write(report)

    print("Comprehensive report generated as `result.md`")

if __name__ == "__main__":
    main()
