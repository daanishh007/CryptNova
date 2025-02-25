import sys
import os
from PIL import Image

def encode_image(image_path, message, output_path):
    image = Image.open(image_path)

    # Ensure the image is in a compatible mode (RGB or RGBA)
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    width, height = image.size

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # End marker
    data_index = 0
    message_length = len(binary_message)

    for i in range(width):
        for j in range(height):
            if data_index < message_length:
                pixel = list(pixels[i, j])

                # Modify the least significant bit (LSB) of the red channel
                pixel[0] = (pixel[0] & ~1) | int(binary_message[data_index])

                # Convert back to tuple based on the mode
                if image.mode == 'RGBA':
                    pixels[i, j] = tuple(pixel[:4])  # Keep alpha unchanged
                else:
                    pixels[i, j] = tuple(pixel[:3])  # RGB

                data_index += 1
            else:
                break

    image.save(output_path)
    print(f"Message successfully encoded and saved to {output_path}")


def decode_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    binary_message = ''
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]
            binary_message += str(pixel[0] & 1)  # Extract LSB of the red channel

    # Split into 8-bit chunks and stop at the end marker
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111110':  # End marker found
            break
        message += chr(int(byte, 2))

    print(f"Decoded message: {message}")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python app.py encode <image_path> <message>")
        print("  python app.py decode <image_path>")
        return

    command = sys.argv[1].lower()
    image_path = sys.argv[2]

    if command == 'encode':
        if len(sys.argv) < 4:
            print("Please provide a message to encode.")
            return
        message = sys.argv[3]
        output_image_path = os.path.splitext(image_path)[0] + "_encoded.png"
        encode_image(image_path, message, output_image_path)

    elif command == 'decode':
        decode_image(image_path)

    else:
        print("Unknown command. Use 'encode' or 'decode'.")


if __name__ == '__main__':
    main()