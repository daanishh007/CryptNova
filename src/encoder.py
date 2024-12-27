from PIL import Image

def encode_image(image_path, message, output_image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    message_length = len(binary_message)
    binary_index = 0

    for i in range(image.size[0]):  # iterate through width
        for j in range(image.size[1]):  # iterate through height
            if binary_index < message_length:
                pixel = list(pixels[i, j])

                # Modify the least significant bit of the red channel
                pixel[0] = pixel[0] & ~1 | int(binary_message[binary_index])

                pixels[i, j] = tuple(pixel)
                binary_index += 1
            else:
                break

    # Save the encoded image
    image.save(output_image_path)
    print(f"Message encoded in {output_image_path}")
