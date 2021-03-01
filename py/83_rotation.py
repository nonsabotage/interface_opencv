import numpy as np
import cv2

data_dir = "docs/IF2101T/CQProjectBasics_1"


def getResize(src):
    basePixSize = 1280
    height = src.shape[0]
    width  = src.shape[1]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, 
        (
            int(width  * resizeRate), 
            int(height * resizeRate)
        ), 
        interpolation = None
    )

    return dst


def _main():
    img = cv2.imread(data_dir + "/IMG_1609.JPG")
    img = getResize(img)
    org = img.copy()
    height, width, channel = img.shape

    M = cv2.getRotationMatrix2D(
        center = (width / 2, height / 2), 
        angle = 60, 
        scale = .5
    )
    # Affine変換のワープで処理が可能
    dst = cv2.warpAffine(
        src = img, 
        M = M, 
        dsize = (width, height)
    )

    cv2.imshow("Original", org)
    cv2.imshow("Final result", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    _main()



