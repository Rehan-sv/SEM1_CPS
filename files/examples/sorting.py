freq = {}

with open("files\\names.txt",'w') as f:
    for i in f:                 # i = line
        words = i.split()       # split line into words
        
        for j in words:         # j = each word
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1

sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
print(sorted_freq)
