import cv2

data_dir = "docs/IF2101T/CQProjectBasics_1"

def __main():
    img1 = cv2.imread(data_dir + "/IMG_0260.JPG")
    img2 = cv2.imread(data_dir + "/IMG_0181.JPG")

    img1 = getResize(img1)
    img2 = getResize(img2)
    imgMask = getMaskImg(img1, img2)

    cv2.imshow("Original1", img1)
    cv2.imshow("Original2", img2)
    cv2.imshow("Final result", imgMask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

def getMaskImg(img1, img2):
    compImg = cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=.3, gamma = 0)
    return compImg

def getResize(src):
    basePixSize = 1000
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

    
