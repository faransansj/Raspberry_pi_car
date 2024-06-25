# 사진 촬영
import picamera                     #라이브러리를 임포트합니다.

camera = picamera.PiCamera()        #파이카메라 객체 생성
camera.resolution = (1024,768)      #카메라 화질 설정
camera.capture('test.jpg')          #사진 촬영 후 파일명 'test'로 저장

# 동영상 촬영
import picamera                     #라이브러리를 임포트합니다.

camera = picamera.PiCamera()        #파이카메라 객체 생성
camera.resolution = (1024,768)      #카메라 화질 설정


camera.start_recording('test.h264') #녹화 시작 파일명 'test'로 저장
camera.wait_recording(10)           #10초동안 녹화
camera.stop_recording()             #녹화 종료
