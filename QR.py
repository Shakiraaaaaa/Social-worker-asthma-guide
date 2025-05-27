import qrcode

# URL to be encoded
url = "https://shakiraaaaaa.github.io/Social-worker-asthma-guide/"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("asthma_guide_qr.png")
