start_time <- Sys.time()

# Define the Anscombe data frame
anscombe <- data.frame(
  x1 = c(10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5),
  x2 = c(10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5),
  x3 = c(10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5),
  x4 = c(8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8),
  y1 = c(8.04, 6.95,  7.58, 8.81, 8.33, 9.96, 7.24, 4.26,10.84, 4.82, 5.68),
  y2 = c(9.14, 8.14,  8.74, 8.77, 9.26, 8.1, 6.13, 3.1,  9.13, 7.26, 4.74),
  y3 = c(7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73),
  y4 = c(6.58, 5.76,  7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89)
)

# Perform regression and print summaries
results <- file("r_results.txt", "w")
for (i in 1:4) {
  fit <- lm(get(paste0("y", i)) ~ get(paste0("x", i)), data = anscombe)
  summary_fit <- summary(fit)
  cat(paste("Set", i, "- R\n"), file = results)
  cat(capture.output(print(summary_fit)), file = results, sep = "\n")
  cat("\n", file = results)
}

# Calculate execution time
end_time <- Sys.time()
execution_time <- as.numeric(difftime(end_time, start_time, units = "secs"))
cat(paste("Execution Time (R):", execution_time, "seconds"), file = results)

close(results)
