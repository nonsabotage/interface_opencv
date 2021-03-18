import cv2
import numpy as np

data_dir = "./docs/IF2101T/CQProjectApp"

def __main() :

    img = cv2.imread(data_dir + "/" + "IMG_0554.JPG")
    img = getHist(img)

    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return None

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


def getHist(img):
    img = getResize(img)
    channel = 3
    upper = 70
    
    # 元ファイルに重ねるヒストグラムの画像を黒で初期化
    size = np.array([upper * 3, 256, channel])
    blackColor = np.zeros(3)
    hist = np.full(size, blackColor, dtype = np.uint8)
    
    height, width, _ = hist.shape
    for j in range(channel):
        bgrHist = cv2.calcHist(images = [img], channels = [j], mask = None, histSize = [256], ranges = [0, 256])
        cv2.normalize(src = bgrHist, dst = bgrHist, alpha = 0, beta = upper, norm_type = cv2.NORM_MINMAX)

        # これを見ると自分でひとつひとつ線を記述しているのか？？？
        # matplotlibなどで代替は出来ないのだろうか？？？
        # グラフに書いてしまってとか        
        color = [0, 0, 0]
        color[j] = 255
        baseLine = j * upper + upper
        for i in range(0, 256):
            vertical = bgrHist[i]
            cv2.line(hist, (i, baseLine), (i, baseLine-vertical), color)

    x = 10 
    y = 10
    img[y: y + height, x: x + width] = hist
    return img



if __name__ == "__main__":
    print(cv2.__version__)
    __main()


    