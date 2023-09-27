import qr_code as qr

#In here you can paste the link to generate the qr code.
img = qr.make("https://github.com/ghubisz/qr-code-generator-py")

img.save("ghubisz_qr-code-generator-py.png")
