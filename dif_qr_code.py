import qrcode  # Import the qrcode module, not qr_code
from PIL import Image

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
url = "https://github.com/ghubisz/qr-code-generator-py"
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("dif_ghubisz_qr_code_generator_py_link.png")