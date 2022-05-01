import Generator

if __name__ == '__main__':
    image = Generator.qr_gen("https://sci.cmb.ac.lk/lms/login/index.php")

    image.save("UocFos.png")