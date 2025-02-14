import cv2
import os

def encrypt_message(image_path, message, password, save_path="encryptedImage.png"):
    """Encrypts a secret message inside an image."""
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read the image file.")
        return
    
    d = {chr(i): i for i in range(255)}  # Mapping characters to ASCII values

    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through color channels

    cv2.imwrite(save_path, img)
    print("Message hidden successfully in:", save_path)
    os.system(f"start {save_path}")  # Opens the image (Windows)

# --- Main Execution ---
if __name__ == "__main__":
    image_path = "mypic.png"  # Use the correct image path
    message = input("Enter secret message: ")
    password = input("Set the passcode: ")  # Store the password in a secure way if needed

    encrypt_message(image_path, message, password)
