seq1 = "spam"
seq2 = "scam"

res = []                    # Start empty
for x in seq1:          # Scan first sequence
    if x in seq2:       # Common item?
        res.append(x)   # Add to result end
