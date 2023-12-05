def encode_decode_cezar(message, offset):
    new_message = ""
    for ch in message:
        if "A" <= ch <= "Z":
            new_message += chr((((ord(ch) - ord("A")) + offset) % 26) + ord("A"))
        elif "a" <= ch <= "z":
            new_message += chr((((ord(ch) - ord("a")) + offset) % 26) + ord("a"))
        else:
            new_message += ch
    return new_message

if __name__ == "__main__":
    print(encode_decode_cezar(input("Enter message: "), int(input("Enter offset: "))))
