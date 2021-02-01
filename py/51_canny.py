import cv2

def __main():
    img = cv2.imread("./docs/IF2101T/CQProjectBasics_1/IMG_0260.JPG")
    img = getResize(img)
    org = img.copy()

    dst = cv2.Canny(image = img, threshold1 = 100, threshold2 = 200)

    cv2.imshow("Original", org)
    cv2.imshow("Final resullt", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getResize(src):
    """ 縦横を同じ画像サイズに変換するための処理
    """
    basePixelSize = 1280
    height, width, _ = src.shape
    largeSize = max(height, width)
    resizeRate = basePixelSize / largeSize

    dst = cv2.resize(src, 
        (
            int(width * resizeRate), 
            int(height * resizeRate)
        )
    )

    return dst

if __name__ == "__main__":
    print(f"{cv2.__version__}")
    __main()




