# 이동할 오브젝트를 나타내는 클래스
class MovingObject:
    def __init__(self, x, y, vx, vy):
        self.x = x  # 현재 x 위치
        self.y = y  # 현재 y 위치
        self.vx = vx  # x 방향 속도
        self.vy = vy  # y 방향 속도

    def update_position(self, delta_time):
        # 속도와 시간의 곱으로 이동 거리를 계산하여 위치를 업데이트
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

# 사용 예시 (설명 용도, 실제 코드에서는 이 부분이 생략될 수 있음)
if __name__ == "__main__":
    # 위치와 속도를 설정하고 이동 업데이트를 진행합니다.
    obj = MovingObject(0, 0, 5, 10)  # (x=0, y=0) 위치에서 x 방향 속도 5, y 방향 속도 10
    obj.update_position(1)  # 1초 후의 위치 업데이트

    # 현재 위치를 출력합니다.
    print(f"현재 위치: ({obj.x}, {obj.y})")
