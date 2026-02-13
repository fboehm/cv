

# concatenate two bib files into a single bib files
#!/bin/bash

# Check if there are at least two arguments
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 file1.bib file2.bib [file3.bib ...]"
    exit 1
fi

# Output file
output_file="boehm.bib"

# Use 'cat' to concatenate files into the output file
cat "$@" > "$output_file"

# Display a message indicating success
echo "Concatenation complete. Result saved to $output_file"
