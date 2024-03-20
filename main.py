from PIL import Image

# Function to encrypt the image
def encrypt(image_path, output_path):
    # Opening the image
    img = Image.open(image_path)
    width, height = img.size

    # Encrypting the image by swapping pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (b, r, g))  # Swapping RGB values

    # Saving the encrypted image
    img.save(output_path)
    print("Image Encrypted")

# Function to decrypt the image
def decrypt(image_path, output_path):
    # Opening the encrypted image
    img = Image.open(image_path)
    width, height = img.size

    # Decrypting the image by applying the reverse operation
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (g, b, r))  # Reversing the swapping operation

    # Saving the decrypted image
    img.save(output_path)
    print("Image Decrypted")


encrypt("D:\\input.jpg", "D:\\encrypted.jpg")
decrypt("D:\\encrypted.jpg", "D:\\decrypted.jpg")
