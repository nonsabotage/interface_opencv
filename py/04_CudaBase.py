import cv2

target_file = "../docs/IF2101T/CQProjectBasics_1/MVI_0182.MP4"




if __name__ == "__main__":

    gpuImg = cv2.cuda_GpuMat()
    cap = cv2.VideoCapture(target_file)

    if not cap.isOpened():
        print ("Not Opened Video Camera")
        exit()
    
    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break
        
        # CPU -> GPU
        gpuImg.upload(img)
        gpuImg = cv2.cuda.resize(gpuImg, (1280, 720))
        # CPU <- GPU
        img = gpuImg.download()

        cv2.imshow("Final result", img)
        if cv2.waitKeyEx(10) > -1:
            break

    cap.release()
    cv2.destroyAllWindows()

    

