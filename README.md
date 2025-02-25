CryptNova is a simple yet powerful image steganography tool that allows you to hide secret messages inside image files by modifying the least significant bits of pixel data. This method ensures that your message remains invisible to the human eye while being securely embedded within the image.

____________________________________________________________________________________________________________

How to Use CryptNova...

     Encoding a Message:

        To hide a message inside an image: python app.py encode <image_filename> "<your_message>"

            Example: python app.py encode assets/cat.png "Testing Testing... Is this thing on?"

             The tool will automatically save the encoded image as cat_encoded.png in the assets/ folder.

     Decoding a Hidden Message:

        To reveal a hidden message from an encoded image: python app.py decode <encoded_image_filename>

            Example: python app.py decode assets/cat_encoded.png

             This will output the hidden message directly to the terminal.

____________________________________________________________________________________________________________

Authors: Daanish Syed Hussain and Iman Rehan. 
