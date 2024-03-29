라즈베리파이 자율주행 자동차 코드 설명

# 3장
|- 3_1.py	: LED1 ON/OFF 하는 코드
| |- 3_1_2.py	: 3_1.py에 KeyboardInterrupt 제어 추가한 코드
| |- 3_1_3.py	: 3_1_2.py 직관적인 코드 변경
| |- 3_1_4.py	: 4개의 LED 제어하는 코드
|- 3_2.py	: 버튼 입력 받는 코드 (누르면 Print 1, 아니면 Print 0)
| |- 3_2_2.py	: 버튼 누르고 뗄 때 값 표시하는 코드 (Print click)
| |- 3_2_3.py	: 버튼 누르고 뗄 때 click 값 증가하는 코드
| |- 3_2_4.py	: 버튼 눌렀을 때만 click 값 증가하는 코드
| |- 3_2_5.py	: 리스트 사용하여 4개의 버튼 입력 받는 코드
|- 3_3.py	: BUZZER 사용하여 1초 간격으로 소리나게 하는 코드
| |- 3_3_2.py	: BUZZER 사용하여 음계 출력하는 코드
| |- 3_3_3.py	: BUZZER 사용하여 자동차 경적 작동하는 코드
| |- 3_3_4.py	: 버튼 누를 때만 자동차 경적 작동하는 코드
| |- 3_3_5.py	: 4개의 버튼에 따른 다른 음계의 BUZZER 작동하는 코드
|- 3_4.py	: 자동차 왼쪽 모터 구동하는 코드
| |- 3_4_2.py	: 자동차 왼쪽 모터의 속도 조절하는 코드
| |- 3_4_3.py	: 자동차 왼쪽 모터의 정방향/역방향 회전하는 코드
| |- 3_4_4.py	: 자동차 왼쪽/오른쪽 모터 구동하여 앞으로 이동하는 코드
|- 3_5.py	: 버튼을 입력 받아 자동차 방향 Print 하는 코드
| |- 3_5_2.py	: 버튼 입력에 따른 앞/뒤로 동작하는 코드
| |- 3_5_3.py	: 버튼 입력에 따른 앞/뒤/왼쪽/오른쪽으로 동작하는 코드
| |- 3_5_4.py	: 3_5_3.py 함수화 하여 직관적인 코드로 변경
|- 3_list.py	: 리스트 사용하는 코드
|- 3_list_2.py	: 리스트 값 변경하는 코드

# 4장
|- 4_1.py	: 블루투스 통신으로 입력값 받아오는 코드
| |- 4_1_2.py	: 라즈베이파이에서 스마트폰으로 데이터 전송하는 코드
|- 4_2.py	: 블루투스 통신으로 입력값 readline으로 받아오는 코드
| |- 4_2_2.py	: 블루투스 통신으로 입력값 문자열 형태로 받아오는 코드
| |- 4_2_3.py	: 블루투스 통신으로 입력값에 맞는 조건문 실행하는 코드
|- 4_3.py	: main() 함수와 serial_thread() 함수 동시 동작하는 코드
| |- 4_3_2.py	: main() 함수와 serial_thread() 함수 독립적 동작하는 코드
|- 4_4.py	: 블루투스 통신으로 입력값에 맞는 조건문 독립적으로 실행하는 코드
| |- 4_4_2.py	: 블루투스 통신으로 입력값에 맞는 조건문으로 자동차 동작하는 코드
|- 4_5.py	: 블루투스 통신으로 자동차 동작 중 버튼 누르면 비상 정지하는 코드
|- 4_6.py	: 블루투스 통신으로 자동차 동작 중 자동차 동작에 맞는 LED 켜지는 코드
|- 4_7.py	: 블루투스 통신으로 자동차 동작 중 BUZZER 입력에 맞게 동작하는 코드

# 5장
|- 5_2.py	: 카메라 작동하는 코드
| |- 5_2_2.py	: 카메라 뒤집어 작동하는 코드
|- 5_3.py	: 카메라로 이미지 출력하는 코드
| |- 5_3_2.py	: 카메라로 이미지 잘라서 출력하는 코드
| |- 5_3_3.py	: 카메라로 이미지 Gray + Blur 처리하는 코드
| |- 5_3_4.py	: 카메라로 이미지를 Threshold에 따라 색 바꿔주는 코드
| |- 5_3_5.py	: 카메라로 이미지 노이즈 제거 및 자동차의 무게중심 출력하는 코드
| |- 5_3_6.py	: 카메라로 자동차가 선 중앙에 위치하도록 Print 하는 코드
| |- 5_3_7.py	: 카메라로 자동차가 선 중앙에 위치하도록 모터를 동작시키는 코드

# 6장
|- 6_1.py	: 키보드의 입력 값 확인하는 코드
| |- 6_1_2.py	: 키보드의 입력 값에 따라 Print 하는 코드
|- 6_2.py	: 이미지 자르는 코드
| |- 6_2_2.py	: 이미지 RGB 형태에서 YUV 형식으로 변환하는 코드
| |- 6_2_3.py	: 이미지 블러링하는 코드
|- 6_3.py	: 이미지 저장하는 코드
| |- 6_3_2.py	: 순서값 증가하는 이미지 저장하는 코드
|- 6_4.py	: 키보드 입력에 따라 조건문 실행하는 코드
| |- 6_4_2.py	: 키보드 입력에 따라 이미지 저장하는 코드
| |- 6_4_3.py	: 키보드 입력에 따라 자동차가 동작하고 이미지 저장되는 코드

# 8장
|- 8_1.py	: tensorflow, numpy, keras 버전 확인 코드
|- 8_2.py	: lane_nabigation_final.h5를 통해 자동차의 조향각 예측하는 코드
|- 8_3.py	: 예측한 결과를 바탕으로 자동차의 이동방향 결정하는 코드
|- 8_4.py	: 필터 적용 안 된 자율 주행 코드

# 10장
|- 10_1.py	: 6장에서 사용했던 필터가 적용되지 않은 코드
| |- 10_1_2.py	: 10_1.py에 threshold 적용시킨 코드
|- 10_2.py	: 6_4_3.py에 OpenCV 필터 적용시킨 코드
|- 10_4.py	: 모델을 적용시킨 자율 주행 코드
|- 10_5.py	: 자동차의 속도 조절한 자율 주행 코드

# 11장
|- 11_2.py	: 실시간으로 물체 감지하는 코드
|- 11_3.py	: 쓰레드를 활용하여 기능 분리하는 코드
|- 11_4.py	: 자율주행 자동차에 물체 감지하는 코드 적용
|- 11_5.py	: 물체를 감지하여 긴급 정지 기능 추가한 코드