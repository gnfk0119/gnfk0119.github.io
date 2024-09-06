import os
from datetime import datetime

def create_markdown(image_url, title, content):
    # 현재 날짜를 사용하여 파일 이름 지정
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"/home/runner/work/gnfk0119.github.io/gnfk0119.github.io/_posts/{date_str}-powerplant-event2.md"  # _posts 경로에 파일 저장"

    # Markdown 파일 작성
    with open(filename, "w") as f:
        # 이미지 삽입
        f.write(f"![Image]({image_url})\n\n")
        
        # 제목 삽입 (헤더)
        f.write(f"# {title}\n\n")
        
        # 내용 삽입
        f.write(f"{content}\n")

    print(f"Markdown file '{filename}' created.")

# 입력 예시
image_url = "https://www.snu.ac.kr/webdata/boardimages/kobodo/img_20240403_001.jpg"
title = "파워플랜트 행사!"
content = """잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호.
잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호. 잘돌아가는지 볼까? 야호."""

# 마크다운 파일 생성 함수 실행
create_markdown(image_url, title, content)
