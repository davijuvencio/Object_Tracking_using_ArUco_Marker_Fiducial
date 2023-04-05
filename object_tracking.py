import cv2
import numpy as np
import subprocess as sp
import time,cv2,atexit,socket
import math

class Davi:
    def __init__(self):
        self.initCaptureParameters()

    def initCaptureParameters(self):
        (self.w,self.h) = (3280,2464)
        self.bytesPerFrame = self.w * self.h
        self.fps = 40
        self.videoCmd = "raspividyuv -w "+str(self.w)+" -h "+str(self.h)+" --output - --timeout 0 --framerate "+str(self.fps)+" --luma --nopreview"
        self.videoCmd = self.videoCmd.split()
        self.cameraProcess = sp.Popen(self.videoCmd, stdout=sp.PIPE)

    def fpsCalculate(self):
        max_frames = 300
        N_frames = 0
        print("fps Calculate...")
        start_time = time.time()
        while True:
            self.cameraProcess.stdout.flush()
            frame = np.frombuffer(self.cameraProcess.stdout.read(self.bytesPerFrame), dtype=np.uint8)
            if frame.size != self.bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            frame.shape = (self.h,self.w)
            cv2.imshow('hello',frame)
            cv2.waitKey(1)
            N_frames += 1
            if N_frames > max_frames: break

        end_time = time.time()
        self.cameraProcess.terminate()
        elapsed_seconds = end_time-start_time
        print("Done! Result: "+str(N_frames/elapsed_seconds)+" fps")
        cv2.destroyAllWindows()

    def objectTracking(self):
        aruco_dict_type = 1
        calibration_matrix_path = "calibration_matrix.npy"
        distortion_coefficients_path = "distortion_coefficients.npy"
        matrix_coefficients = np.load(calibration_matrix_path)
        distortion_coefficients = np.load(distortion_coefficients_path)
        while True:
            self.cameraProcess.stdout.flush()
            frame = np.frombuffer(self.cameraProcess.stdout.read(self.bytesPerFrame), dtype=np.uint8)
            frame.shape = (self.h,self.w)
            cv2.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
            parameters = cv2.aruco.DetectorParameters_create()
            corners, ids, rejected_img_points = cv2.aruco.detectMarkers(frame, cv2.aruco_dict,parameters=parameters,cameraMatrix=matrix_coefficients,distCoeff=distortion_coefficients)
            if len(corners) > 0:
                for i in range(0, len(ids)):
                    c = corners[i][0]
                    rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.024, matrix_coefficients, distortion_coefficients)
                    (rvec-tvec).any()
                    R=np.zeros((3,3),dtype=np.float64)
                    cv2.Rodrigues(rvec,R)
                    sy=math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
                    singular=sy< 1e-6
                    if not singular:
                        x = math.atan2(R[2, 1], R[2, 2])
                        y = math.atan2(-R[2, 0], sy)
                        z = math.atan2(R[1, 0], R[0, 0])
                    else:
                        x = math.atan2(-R[1, 2], R[1, 1])
                        y = math.atan2(-R[2, 0], sy)
                        z = 0
                    rx = x * 180.0 / 3.141592653589793
                    ry = y * 180.0 / 3.141592653589793
                    rz = z * 180.0 / 3.141592653589793
                    distancex = (tvec[0][0][0])
                    distancey = (tvec[0][0][1]) 
                    distancez = (tvec[0][0][2]) 
                    print(distancex,distancey,distancez,rz)
                    print("id",ids[i],[c[:, 0].mean()], [c[:, 1].mean()],rz)
            # Mostrar imagem
            # cv2.imshow('hello',frame)
            # cv2.waitKey(1)
if __name__ == '__main__':
    try:
        OT = Davi()
        #OT.fpsCalculate()
        OT.objectTracking()
    except KeyboardInterrupt:
        print("Acabou")
        cv2.destroyAllWindows()