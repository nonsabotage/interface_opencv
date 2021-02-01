import cv2

def __main():
    img = cv2.imread("./docs/IF2101T/CQProjectBasics_1/IMG_0260.JPG")
    img = getResize(img)
    org = img.copy()
    cv2.imshow("Original", org)


    for k in [3, 5, 7]:
        img = cv2.cvtColor(src = org, code = cv2.COLOR_BGR2GRAY)
        dst = cv2.Sobel(src = img, ddepth = cv2.CV_32F, ksize = k, dx = 1, dy = 0,)
        # 実数で計算したので, 8Uに戻す
        dst = cv2.convertScaleAbs(src = dst)
        cv2.imshow(f"k = {k}", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getResize(src):
    """ 縦横を同じ画像サイズに変換するための処理
    """
    basePixelSize = 1280
    height, width, _ = src.shape
    largeSize = max(height, width)
    resizeRate = basePixelSize / largeSize

    dst = cv2.resize(src, (
            int(width  * resizeRate), 
            int(height * resizeRate)
        ))

    return dst

if __name__ == "__main__":
    print(f"{cv2.__version__}")
    __main()




