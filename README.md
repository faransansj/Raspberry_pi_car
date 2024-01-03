# Raspberry_pi_car
- Trouble & Shooting
    RuntimeError: No access to /dev/mem try running as root
  - **에러 원인**   
  Raspberry pi에서 GPIO pin에 접근할 때 일반 사용자로 접근하여 권한이 충분하지 않아서 생긴 문제입니다.
  - **해결 방안**
  root 권한으로 실행하기
  터미널에서 sudo(root 사용자 권한으로 실행) 명령어를 이용해서 파일을 실행해줍니다.
  ```sudo python3 [파일 경로]```
