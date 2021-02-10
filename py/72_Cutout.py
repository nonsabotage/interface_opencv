import cv2

data_dir = "docs/IF2101T/CQProjectBasics_1"

def __main():
    img = cv2.imread(data_dir + "/IMG_1692.JPG")
    img = getResize(img)
    y = 100
    x = 300
    h = 500
    w = 600
    # Numpyと同じだね
    dst = img[y:(y+h), x:(x+w)]

    cv2.imshow("Original", img)
    cv2.imshow("Final result", dst)
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


