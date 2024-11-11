# AI-Assisted Programming Report

## Introduction

This document provides an overview of how AI-assisted tools, such as GitHub Copilot and ChatGPT, were used to assist with the coding and documentation for the Go for Statistics assignment. This assignment revisited the Anscombe Quartet dataset, with the aim of implementing linear regression and comparing the results across Python, R, and Go.

## Selected AI Tools and Services

1. **GitHub Copilot**
   - **URL**: [https://github.com/features/copilot](https://github.com/features/copilot)
   - **Description**: GitHub Copilot is an AI-powered code completion tool integrated with Visual Studio Code. It provides intelligent suggestions as you type, generating code snippets, functions, and entire blocks of code in real time.
   
2. **ChatGPT**
   - **URL**: [https://chat.openai.com/](https://chat.openai.com/)
   - **Description**: ChatGPT is a large language model (LLM) developed by OpenAI. The free plan allows users to ask questions, request code generation, and receive guidance in a conversational format. For this assignment, ChatGPT was used to generate Go code for statistical analysis tasks and to debug issues with code logic.

## Review of AI Assistance

### Step 1: Initial Code Review with GitHub Copilot

- **Objective**: Refine the initial Go code used for linear regression in the Anscombe Quartet.
- **Process**: 
  - Copilot provided autocomplete suggestions for basic functions, such as setting up slices of data and importing necessary packages.
  - While typing, Copilot suggested helper functions for statistical calculations, which sped up the initial coding process.
  - Example: Copilot suggested code for structuring the `LinearRegression` function and handling data input in the Go script.

- **Observations**: 
  - GitHub Copilot was helpful for repetitive code tasks, especially in defining data types and setting up functions.
  - However, Copilot sometimes generated suggestions that were inaccurate for statistical calculations.

### Step 2: AI-Generated Code with ChatGPT

- **Objective**: Generate Go code for linear regression on the Anscombe Quartet dataset.
- **Process**:
  - I engaged in a conversational approach with ChatGPT, explaining the need for Go code to perform linear regression.
  - ChatGPT generated code snippets, including a function for linear regression and handling dataset input.
  - I refined my prompts multiple times to get specific functions for calculating the slope and intercept, handling input data, and calculating residuals.

- **Examples of Prompts**:
  - "Generate Go code for performing linear regression on the Anscombe Quartet data."
  - "How can I calculate R-squared in Go for this data?"
  - "How do I load data from a JSON Lines file in Go?"

- **Challenges**:
  - Initially, ChatGPT provided code with the slope and intercept reversed. Through iterative prompts, I clarified the requirements, and ChatGPT adjusted the code accordingly.
  - ChatGPT’s suggestions helped in understanding the use of packages like `github.com/montanaflynn/stats` for more accurate statistical functions.

### Step 3: Refinement and Debugging with AI Assistance

- **Objective**: Debug and refine the code to ensure accurate output across Python, R, and Go implementations.
- **Process**:
  - After initial code generation, I used both GitHub Copilot and ChatGPT to troubleshoot issues.
  - ChatGPT helped clarify Go-specific errors and provided explanations for package imports and module setups (like `go.mod` and `go.sum`).
  - Example: ChatGPT explained the configuration for Go modules to recognize external packages, resolving an error related to `gonum/stat`.

- **Final Output**: After implementing corrections and running tests across all three languages, I generated a comparative output report (`result.md`) and analysis (`summary.md`).

## Experiences and Insights

Using a combination of GitHub Copilot and ChatGPT proved to be an efficient approach for this project. Each tool brought unique strengths to the table, and together they complemented each other well.

**Effectiveness**: GitHub Copilot was highly efficient in generating basic code snippets and structuring functions, particularly for repetitive or boilerplate code. It provided a quick way to set up foundational parts of the Go code, especially in areas where standard functions and struct definitions were needed. However, for context-specific calculations, such as linear regression, Copilot’s suggestions were sometimes limited. ChatGPT filled this gap by providing tailored code solutions and clarifying the nuances of Go syntax and package dependencies. In particular, ChatGPT’s ability to generate functions for calculating statistical values like R-squared and handling JSON Lines files in Go was invaluable. The conversational approach with ChatGPT enabled iterative refinement of the code, addressing errors and customizing the logic to meet the assignment’s requirements.

**Limitations**: GitHub Copilot was best suited for predictable coding patterns and boilerplate generation but fell short on more complex tasks, like specific statistical calculations. Meanwhile, ChatGPT required multiple prompts to reach the desired solutions and sometimes generated code that needed adjustments to fit Go’s syntax and package handling. While ChatGPT provided deeper insight and custom code generation, the process could be time-consuming as it required multiple interactions to get accurate results.

## Recommendations for the Firm

Based on my experience, I recommend the following for the startup:

- **Programming Workflow**: A combined use of GitHub Copilot for general coding tasks and ChatGPT for specialized problem-solving. This approach can speed up development while reducing errors.
- **Staffing**: With tools like Copilot and ChatGPT, fewer engineers may be required for basic development, but experienced engineers are still essential for code review and specialized tasks.