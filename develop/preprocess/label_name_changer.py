import os

# 라벨 파일이 위치한 디렉토리 경로
label_dir = 'C:/miniproj_yolov5/3.develop/datasets/calss_kor/valid/labels'
# 변경할 클래스 ID와 새 클래스 ID
class_id_mapping = {"강정태":"0", "공선의":"1","김원일":"2","박채은":"3","이정룡":"4","이민형":"5","송욱":"6","이상헌":"7",
                "이정훈":"8","박준혁":"9","김유철":"10","이태규":"11","윤영현":"12"}

# 디렉토리 내 모든 파일에 대해 반복
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):  # .txt 파일인 경우에만 처리
        filepath = os.path.join(label_dir, filename)
        
        # 파일 읽기
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        # 각 라인에 대해 클래스 ID 변경
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            # parts 리스트가 비어 있지 않고, 적어도 하나의 요소(클래스 ID)를 포함하고 있는지 확인
            if parts and len(parts) > 4:  # 클래스 ID와 바운딩 박스 좌표를 포함하는지 확인
                if parts[0] in class_id_mapping:  # 클래스 ID가 매핑에 존재하는 경우
                    parts[0] = class_id_mapping[parts[0]]  # 새 클래스 ID로 변경
                new_lines.append(' '.join(parts))
            else:
                print(f"Skipping invalid line: {line}")
        
        # 변경된 내용으로 파일 다시 쓰기
        with open(filepath, 'w') as file:
            for line in new_lines:
                file.write(line + '\n')