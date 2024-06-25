import pytesseract
from PIL import ImageGrab, ImageEnhance, ImageFilter, ImageOps
import webbrowser
import keyboard
import threading
import time

# Tesseract 경로 설정 (Windows에서 설치 경로를 지정)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    # 이미지 전처리: 그레이스케일 변환, 샤프닝, 콘트라스트 향상
    image = image.convert('L')  # 그레이스케일 변환
    image = ImageOps.invert(image)  # 색상 반전
    image = image.point(lambda x: 0 if x < 128 else 255)  # 이진화
    image = image.filter(ImageFilter.MedianFilter())  # 노이즈 제거
    image = image.filter(ImageFilter.SHARPEN)  # 샤프닝
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # 콘트라스트 향상
    return image

def capture_screen_and_extract_text():
    # 클립보드에서 이미지 가져오기
    image = ImageGrab.grabclipboard()
    if image:
        image = preprocess_image(image)
        image.save("screenshot_processed.png")
        # OCR로 텍스트 추출
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(image, lang='kor+eng+chi_sim+chi_tra+jpn', config=custom_config)
        print(f"Extracted Text: {text}")
        return text
    print("No image found in clipboard.")
    return ""

def open_url_with_text(text):
    words = text.split()
    query = "%20".join(words)
    url = f"https://dak.gg/er/multi?q={query}"
    print(f"Generated URL: {url}")
    webbrowser.open(url)

def on_hotkey():
    # 단축키 눌렀을 때 호출되는 함수
    threading.Thread(target=process_capture).start()

def process_capture():
    text = capture_screen_and_extract_text()
    if text:
        open_url_with_text(text)

def main():
    print("Softkleenex Game Helper is running in the background...")
    print("Press Ctrl + Alt + X to process the clipboard image.")
    
    # 단축키 설정
    keyboard.add_hotkey('ctrl+alt+x', on_hotkey)

    # 프로그램이 종료되지 않도록 지속 실행
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
