import cv2
DATA_DIR = "./docs/IF2101T/CQProjectBasics_1/"

def __main():

    img = cv2.imread(DATA_DIR + "DSC_0047.jpg")
    img = getResize(img)
    org = img.copy()

    bgr = cv2.split(m = img)
    for i, c in enumerate(bgr):
        cv2.imshow("bgr"[i], c)
    cv2.imshow("Original", org)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getResize(src):

    basePixSize = 1280
    height, width, *_ = src.shape
    largeSize  = max(height, width)
    resizeRate = basePixSize / largeSize

    dst = cv2.resize(
        src, (
            int(width  * resizeRate), 
            int(height * resizeRate)
        )
    )
    
    return dst



if __name__ == "__main__":
    __main()
