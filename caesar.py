def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

for shift in range(26):
    decrypted_text = caesar_decrypt('YBCBOTIXUZOZXBTFOLBLXBTCAYRXCPTXUYTROZZCBXQXUOBRXROBJYFXUYBDIOLYBTIXLOUAFJIXLCJTODXTOMTCDCYBFOTTIXUCGGYTIOAXLXBTJTUCYDITOBAYEXCTMBBXAPOUJOZXLCSROZZCCBFTIXBFYHHXFJMFFXBASFOLBROZZCJOJMFFXBASTICTCAYRXICFBOTCZOZXBTTOTIYBECGOMTJTOHHYBDIXUJXAPGXPOUXJIXPOMBFIXUJXAPPCAAYBDFOLBCQXUSFXXHLXAAFOTXYTIXUTIXLXAALCJQXUSFXXHROZZCOUJIXPXAAQXUSJAOLASROZZCPOUJIXICFHAXBTSOPTYZXCJJIXLXBTFOLBTOAOOECGOMTIXUCBFTOLOBFXULICTLCJDOYBDTOICHHXBBXVT', shift)
    print(f"Shift {shift}: {decrypted_text}")