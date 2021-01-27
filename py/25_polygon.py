import cv2
import numpy as np

if __name__ == "__main__":
    print(f"cv2 version is {cv2.__version__}")

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])


    pts1 = np.array([[100, 20], [230, 40], [320, 100], [380, 150], [290, 200], [200, 330], [150, 300]], np.int32)
    pts2 = np.array([[50, 100], [100, 50], [250, 200], [100, 150]], np.int32)
    # 多角形の枠線を描画
    cv2.polylines(
        img = img, 
        pts = [pts1, pts2],
        isClosed = True, 
        color = color, 
        thickness = 3,
        lineType = cv2.LINE_AA,
    )

    pts = np.array([[400, 100], [500, 350], [300, 350]], np.int32)
    cv2.fillConvexPoly(
        img = img, 
        points = pts, 
        color = color, 
        lineType = cv2.LINE_AA,
    )

    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
