from collections import Counter

cipher_text = "YBCBOTIXUZOZXBTFOLBLXBTCAYRXCPTXUYTROZZCBXQXUOBRXROBJYFXUYBDIOLYBTIXLOUAFJIXLCJTODXTOMTCDCYBFOTTIXUCGGYTIOAXLXBTJTUCYDITOBAYEXCTMBBXAPOUJOZXLCSROZZCCBFTIXBFYHHXFJMFFXBASFOLBROZZCJOJMFFXBASTICTCAYRXICFBOTCZOZXBTTOTIYBECGOMTJTOHHYBDIXUJXAPGXPOUXJIXPOMBFIXUJXAPPCAAYBDFOLBCQXUSFXXHLXAAFOTXYTIXUTIXLXAALCJQXUSFXXHROZZCOUJIXPXAAQXUSJAOLASROZZCPOUJIXICFHAXBTSOPTYZXCJJIXLXBTFOLBTOAOOECGOMTIXUCBFTOLOBFXULICTLCJDOYBDTOICHHXBBXVT"

# Build the key based on the frequency mapping and iterative word observation
key = {'X': 'e', 'O': 'o', 'T': 't', 'B': 'n', 'C': 'a', 'I': 'h', 'F': 'd', 'A': 'l', 'U': 'r', 'J': 's', 'Y': 'i', 'L': 'w', 'P': 'f', 'H': 'p', 'D': 'g', 'd': 'F', 'M': 'u', 'Z': 'm', 'G': 'b', 'R': 'c', 'Q': 'v', 'E': 'k', 'V': 'x', 'S' : 'y'}
print(f"key: {key}")

# Decrypt the text using the key
deciphered_text = ''.join(key.get(char, char) for char in cipher_text)

# Print the results
print("Recovered plain text:")
print(deciphered_text)
