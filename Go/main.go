package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/montanaflynn/stats"
)

// AnscombeData represents each line of the Anscombe Quartet data
type AnscombeData struct {
	Dataset string    `json:"dataset"`
	X       []float64 `json:"x"`
	Y       []float64 `json:"y"`
}

func main() {
	// Measure execution time
	start := time.Now()

	// Open the JSONL file (ending with .jl)
	file, err := os.Open("../data/anscombe.jl")
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	// Create a scanner to read the .jl file line by line
	scanner := bufio.NewScanner(file)

	// Output file for Go results
	outFile, err := os.Create("go_results.txt")
	if err != nil {
		log.Fatalf("Error creating output file: %v", err)
	}
	defer outFile.Close()
	writer := bufio.NewWriter(outFile)

	// Read each line (dataset) from the .jl file
	for scanner.Scan() {
		var data AnscombeData
		if err := json.Unmarshal(scanner.Bytes(), &data); err != nil {
			log.Fatalf("Error parsing JSON: %v", err)
		}

		// Perform linear regression using the MontanaFlynn stats package
		slope, intercept, err := CalculateLinearRegression(data.X, data.Y)
		if err != nil {
			log.Fatalf("Error calculating linear regression: %v", err)
		}

		// Print detailed regression result to the file
		fmt.Fprintf(writer, "Call: lm(formula = y ~ x, data = %s)\n\n", data.Dataset)
		fmt.Fprintf(writer, "Coefficients:\n")
		fmt.Fprintf(writer, "(Intercept)   %.4f\n", intercept)
		fmt.Fprintf(writer, "Slope         %.4f\n", slope)
		fmt.Fprintf(writer, "-------------------------------------------------\n")
	}

	// Measure execution time
	elapsed := time.Since(start)
	fmt.Fprintf(writer, "Execution Time (Go): %.4f seconds\n", elapsed.Seconds())
	writer.Flush()
}

// CalculateLinearRegression computes the slope and intercept from the series
func CalculateLinearRegression(x, y []float64) (float64, float64, error) {
	// Prepare the series data
	var series stats.Series
	for i := range x {
		series = append(series, stats.Coordinate{X: x[i], Y: y[i]})
	}

	// Perform linear regression
	regressionSeries, err := stats.LinearRegression(series)
	if err != nil {
		return 0, 0, err
	}

	// Use the first and last points in the regression to calculate slope and intercept
	first := regressionSeries[0]
	last := regressionSeries[len(regressionSeries)-1]

	// Calculate slope
	slope := (last.Y - first.Y) / (last.X - first.X)

	// Calculate intercept using the formula: intercept = Y - slope * X (using first point)
	intercept := first.Y - slope*first.X

	return slope, intercept, nil
}
