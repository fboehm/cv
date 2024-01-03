---
title: "Untitled"
execute:
  keep-md: true
  keep-ipynb: true
format: html
engine: jupyter
---

```{r}
#| results: 'asis'
# Your list of people
people_list <- list(
  p1 = list(first_name = "John", last_name = "Doe"),
  p2 = list(first_name = "Jane", last_name = "Smith")
  # Add more people as needed
)

# Print the details for each person
for (person in people_list) {
  cat(paste("My first name is:", person$first_name, "and my last name is:", person$last_name, "\n\n"))
}
```




## now in python

::: {#620de31b .cell execution_count=1}
``` {.python .cell-code}
# Your list of people
people_list = [
    {"first_name": "John", "last_name": "Doe"},
    {"first_name": "Jane", "last_name": "Smith"}
    # Add more people as needed
]

# Print the details for each person
for person in people_list:
    print(f"My first name is: {person['first_name']} and my last name is: {person['last_name']}\n\n")
```

::: {.cell-output .cell-output-stdout}
```
My first name is: John and my last name is: Doe


My first name is: Jane and my last name is: Smith


```
:::
:::


