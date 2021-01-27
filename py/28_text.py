import cv2
import numpy as np

if __name__ == "__main__":
    print(f"cv2 version is {cv2.__version__}")

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    idx = range(5)

    for x, y in zip(idx, idx):
        cv2.putText(
            img = img, 
            text = "CQ Publishing", 
            org = (100, 100 + y * 30), 
            fontFace = cv2.FONT_HERSHEY_TRIPLEX,
            color = color, 
            fontScale = 1.,
            lineType = cv2.LINE_AA,
        )


    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
