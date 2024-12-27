import sys
from src.encoder import encode_image
from src.decoder import decode_image

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py [encode/decode] ...")
        sys.exit(1)

    action = sys.argv[1]

    if action == "encode":
        if len(sys.argv) != 5:
            print("Usage: python app.py encode <image_path> <message> <output_image_path>")
            sys.exit(1)
        image_path = sys.argv[2]
        message = sys.argv[3]
        output_image_path = sys.argv[4]
        encode_image(image_path, message, output_image_path)

    elif action == "decode":
        if len(sys.argv) != 3:
            print("Usage: python app.py decode <image_path>")
            sys.exit(1)
        image_path = sys.argv[2]
        decoded_message = decode_image(image_path)
        print(f"Decoded message: {decoded_message}")

    else:
        print("Invalid action. Choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
