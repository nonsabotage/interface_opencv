import cv2
import sys

def __main():

    img = cv2.imread("docs/IF2101T/CQProjectBasics_1/DSC_0071.JPG")
    img = getResize(img)
    matImg = img.copy()

    # JPEGに変換
    result, jpgImg = cv2.imencode(".jpg", img = img, params = [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    # PNGに変換
    result, pngImg = cv2.imencode(".png", img = img, params = [int(cv2.IMWRITE_PNG_COMPRESSION), 8])
    # TIFFに変換
    result, tifImg = cv2.imencode(".tif", img = img, params = [int(cv2.IMWRITE_TIFF_COMPRESSION), 8])

    print("Mat size = {0}".format(sys.getsizeof(img)))
    print("jpg size = {0}".format(sys.getsizeof(jpgImg)))
    print("png size = {0}".format(sys.getsizeof(pngImg)))
    print("tiff size = {0}".format(sys.getsizeof(tifImg)))

    # デコードして戻す
    jpgImg = cv2.imdecode(jpgImg, cv2.IMREAD_COLOR)
    pngImg = cv2.imdecode(pngImg, cv2.IMREAD_COLOR)
    tifImg = cv2.imdecode(tifImg, cv2.IMREAD_COLOR)

    # デコードした結果を表示する
    cv2.imshow("Original", matImg)
    cv2.imshow("Jpeg", jpgImg)
    cv2.imshow("Png", pngImg)
    cv2.imshow("TIff", tifImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getResize(src):
    basePixSize = 1280
    height, width, _ = src.shape
    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize
    dst = cv2.resize(
        src,
        (int(width * resizeRate), int(height * resizeRate)),  
        interpolation = None
    )

    return dst


if __name__ == "__main__":
    print(cv2.__version__)
    __main()


