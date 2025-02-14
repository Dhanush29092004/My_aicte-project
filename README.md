# Steganography Project

## Description
This project implements steganography using OpenCV in Python. It allows users to hide a secret message inside an image and retrieve it later using the correct passcode.

## Features
- Encrypts a message into an image.
- Decrypts the hidden message from the image.
- Passcode protection for added security.

## Installation
1. Install Python (3.6+ recommended).
2. Install required dependencies:
   ```sh
   pip install opencv-python
   ```
3. Download or clone this repository:
   ```sh
   git clone https://github.com/Dhanush29092004/steganography-project.git
   cd steganography-project
   ```

## Usage
### Encryption
1. Run the encryption script:
   ```sh
   python encrypt.py
   ```
2. Enter the secret message when prompted.
3. Provide a passcode for security.
4. The message is encrypted into `encryptedImage.jpg`.

Example:
```
Enter secret message: Hello World!
Enter Passcode: 9866
Message has been encrypted successfully.
```

### Decryption
1. Run the decryption script:
   ```sh
   python decrypt.py
   ```
2. Enter the original message length.
3. Enter the correct passcode.
4. The hidden message is revealed.

Example:
```
Enter original message length: 12
Enter passcode for decryption: 9866
Decrypted message: Hello World!
```

## Encrypted Image
Below is an example of an encrypted image:

![image](https://github.com/user-attachments/assets/5fc27553-ca06-4325-9db5-ff4ccd10e18e)


## License
This project is licensed under the MIT License.

