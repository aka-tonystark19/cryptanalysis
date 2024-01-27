import matplotlib.pyplot as plt
from collections import Counter

cipher_text = "YBCBOTIXUZOZXBTFOLBLXBTCAYRXCPTXUYTROZZCBXQXUOBRXROBJYFXUYBDIOLYBTIXLOUAFJIXLCJTODXTOMTCDCYBFOTTIXUCGGYTIOAXLXBTJTUCYDITOBAYEXCTMBBXAPOUJOZXLCSROZZCCBFTIXBFYHHXFJMFFXBASFOLBROZZCJOJMFFXBASTICTCAYRXICFBOTCZOZXBTTOTIYBECGOMTJTOHHYBDIXUJXAPGXPOUXJIXPOMBFIXUJXAPPCAAYBDFOLBCQXUSFXXHLXAAFOTXYTIXUTIXLXAALCJQXUSFXXHROZZCOUJIXPXAAQXUSJAOLASROZZCPOUJIXICFHAXBTSOPTYZXCJJIXLXBTFOLBTOAOOECGOMTIXUCBFTOLOBFXULICTLCJDOYBDTOICHHXBBXVT"

# Count occurrences of each alphabet
letter_counts = Counter(cipher_text)

# Sort the dictionary by values (occurrences) in ascending order
sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1]))

# Extracting data for plotting
letters = sorted_letter_counts.keys()
occurrences = sorted_letter_counts.values()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(letters, occurrences)
plt.xlabel('Alphabets')
plt.ylabel('Occurrences')
plt.title('Occurrences of Alphabets in Cipher Text')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()