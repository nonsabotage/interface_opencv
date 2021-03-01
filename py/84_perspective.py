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
    img = cv2.imread(data_dir + "/20200905_163733.jpg")
    img = getResize(img)
    org = img.copy()
    height, width, channel = img.shape

    # マス目四隅の座標を指定
    pts1  = np.array([[388, 174], [943, 170], [243, 717], [1068, 720]], dtype = np.float32)
    color = (255, 0, 0)

    # オリジナルの画像に確認用としてマーカを付ける
    for i, pos in enumerate(pts1):
        cv2.circle(img = org, center = (pos[0], pos[1]), radius = 5, color = color, thickness=-1, lineType = cv2.LINE_AA)
    
    # 変換後のマス目四隅の座標を指定
    pts2 = np.array([[100, 100], [720, 100], [100, 960], [720, 960]], dtype = np.float32)

    M = cv2.getPerspectiveTransform(src = pts1, dst = pts2)
    dst = cv2.warpPerspective(src = img, M = M, dsize = (width, height))

    cv2.imshow("Original", org)
    cv2.imshow("Final result", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    print(cv2.__version__)
    _main()



