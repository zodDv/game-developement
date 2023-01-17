# Caesar Cipher
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
MAX_KEY_SIZE = len(SYMBOLS)


def get_mode():
    while True:
        print("Do you wish to encrypt or decrypt or brute-force a message?")
        mode = input().lower()
        if mode in ["encrypt", "e", "decrypt", "d", "brute-force", "b"]:
            return mode
        else:
            print(
                'Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".'
            )


def get_message():
    print("Enter your message:")
    return input()


def get_key():
    key = 0
    while True:
        print("Enter the key number (1-%s)" % (MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key


def get_translated_message(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:  # Symbol not found in SYMBOLS.
            # Just add this symbol without any change. This means that any characters that aren’t part of the alphabet, such as commas and periods, won’t be changed.
            translated += symbol
        else:
            # Encrypt or decrypt
            symbol_index += key

            if symbol_index >= len(
                SYMBOLS
            ):  # This if statement allows symbol_index to go past the last index of SYMBOLS when the sum is more than len(SYMBOLS), we’ll need to wrap around to the beginning of the list at 0.
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated += SYMBOLS[symbol_index]
    return translated


mode = get_mode()
message = get_message()
if mode[0] != "b":
    key = get_key()
print("Your translated text is:")
if mode[0] != "b":
    print(get_translated_message(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, get_translated_message("decrypt", message, key))
