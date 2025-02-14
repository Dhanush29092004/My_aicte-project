import cv2

def decrypt_message(image_path, message_length, password):
    """Decrypts a secret message from an image."""
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not read the image file.")
        return

    c = {i: chr(i) for i in range(255)}  # Mapping ASCII values to characters

    n, m, z = 0, 0, 0
    extracted_message = ""

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for _ in range(message_length):
            extracted_message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through color channels

        print("Decrypted message:", extracted_message)
    else:
        print("YOU ARE NOT AUTHORIZED")

# --- Main Execution ---
if __name__ == "__main__":
    image_path = "encryptedImage.png"  # Use the correct encoded image file
    message_length = int(input("Enter the original message length: "))  # Ensure the correct length
    password = input("Set the passcode (as used in encryption): ")  # Must match the encryption passcode

    decrypt_message(image_path, message_length, password)
