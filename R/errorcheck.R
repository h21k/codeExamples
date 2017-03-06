do_error_check <- function(mbpta) {
  number_of_runs <- length(mbpta)
  # minR workaround for bugs 100315_1050 and 030315_1117
  min_number_of_runs <- 1000
  if (0) {
    result <- tryCatch(minR(mbpta),
                       error = function (cond) {
                         return (cond)
                       }
    )
    if (length (result) == 3) {
      min_number_of_runs <- result[[3]]
    } else {
      return (paste("minR test failed:", result))
    }
  }
  if (min_number_of_runs > number_of_runs) {
    return (paste("Data does not have enough runs - the minimum is",
                  min_number_of_runs,
                  "but only", number_of_runs,
                  "have been captured."))
  }
  result <- indep(mbpta)
  p_value <- result[[1]]
  decision <- result[[2]]
  if (decision == "independent data") {} else {
    return (paste("Data is not independent, p_value =", p_value))
  }
  print (paste("Data is independent, p_value =", p_value))
  
  # identicDitrib workaround for bug 030315_1110
  failures <- 0
  success <- 0
  while ((failures < 5) && (success == 0)) {
    result <- identicDitrib(mbpta)
    p_value <- result[[1]]
    decision <- result[[2]]
    if (decision == "identical distributed samples") {
      # Data is IID
      success <- 1
    } else {
      # Data may not be IID, try rerunning
      failures <- failures + 1
    }
  }
  if (success) {
    print (paste("Data is identically distributed, p_value =", p_value))
    return ("")
  } else {
    # Too many failures - assume data is not IID
    return (paste("Data is not identically distributed, p_value =", p_value))
  }
}