from PIL import Image

def decode_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    binary_message = ""
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            # Get the least significant bit of the red channel
            binary_message += str(pixel[0] & 1)

    # Split the binary message into chunks of 8 bits
    byte_chunks = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]

    # Convert each 8-bit chunk to a character
    decoded_message = "".join(chr(int(chunk, 2)) for chunk in byte_chunks if int(chunk, 2) != 0)

    return decoded_message