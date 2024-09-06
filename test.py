import os
from datetime import datetime

def create_markdown(imageUrl, title, details):
    # 현재 날짜를 마크다운 파일명에 사용
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-auto-generated-post.md"

    # Google Drive 이미지 URL을 다운로드 가능한 형식으로 변환
    if "id=" in imageUrl:
        fileId = imageUrl.split('id=')[1]  # 파일 ID 추출
        imageUrlConverted = f"https://drive.google.com/uc?export=view&id={fileId}"
    else:
        imageUrlConverted = imageUrl  # 만약 id가 없으면 기본 URL 사용

    # 마크다운 파일 생성 및 콘텐츠 작성
    with open(filename, "w") as f:
        # 이미지 삽입
        f.write(f"![Image]({imageUrlConverted})\n\n")
        
        # 제목 삽입 (헤더로 사용)
        f.write(f"# {title}\n\n")
        
        # 상세 내용 삽입
        f.write(f"{details}\n")

    print(f"Markdown file '{filename}' has been created.")

# 예시로 사용할 데이터 (Google Apps Script에서 받아올 수 있는 데이터)
imageUrl = "https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9I10J11/view?usp=sharing"
title = "Auto-Generated Post Title"
details = "This is the auto-generated post content. It contains details about the post."

# 마크다운 파일 생성 함수 실행
create_markdown(imageUrl, title, details)
