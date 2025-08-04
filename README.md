# Voice Conversion Project

## 프로젝트 개요

이 프로젝트는 유튜브에서 다운로드한 음악 파일에서 보컬을 분리하고, 이를 다른 가수의 목소리로 변환하는 프로그램입니다.

## 주요 기능

- **유튜브 음원 다운로드**: 유튜브 링크를 입력받아 음원 파일을 다운로드합니다.
- **음성 분리 및 변환**: `source.wav`와 `target.wav` 파일을 사용하여 음성을 변환합니다.
- **결과물 저장**: 변환된 음원을 `mp3` 파일로 저장합니다.

## 사용 방법

1. **환경 설정**
    - Python 3.7+를 설치합니다.
    - 필요한 라이브러리(`pytube`, `librosa`, `tensorflow`, `ffmpeg-python`)를 설치합니다.
    - **FFmpeg**를 설치하고 시스템 환경 변수에 경로를 추가합니다.
2. **음원 파일 준비**
    - 변환할 음원이 있는 유튜브 링크를 준비합니다.
    - 변환의 원본이 될 보컬 음원 `source.wav` 파일과, 목표로 하는 목소리의 `target.wav` 파일을 준비합니다.
3. **프로그램 실행**
    
    ```
    python main.py \-\-youtube_url "원본 노래 Youtube URL" \-\-singer_url "목소리 소스 Youtube URL"
    ```
    
- `complete.mp3` 파일을 확인하여 변환 결과를 들을 수 있습니다.

## 파일 및 폴더 구조

- `main.py`: 프로그램의 주요 로직을 담고 있는 메인 파일입니다.
- `voice_converter.py`: 음성 변환 로직을 구현한 모듈입니다.
- `youtube_downloader.py`: 유튜브 다운로드 기능을 담당하는 모듈입니다.
- `pretrained_models`: 음성 변환에 사용되는 사전 학습된 모델 파일들이 저장됩니다.
- `data`: `source.wav`와 `target.wav` 파일이 위치합니다.
- `separated_audio`: 분리된 음성 파일이 저장되는 폴더입니다.
- `output.mp3`, `complete.mp3`: 최종 변환된 음원 파일입니다.

## 추가 기능 (선택 사항)

- 변환된 음원 미리듣기 기능.
- 다양한 음성 변환 옵션(피치, 속도 등) 제공.

## 개발 환경

- Python 3.7+
- Windows

# Voice Conversion Project

## 프로젝트 개요

이 프로젝트는 유튜브에서 다운로드한 음악 파일에서 보컬을 분리하고, 이를 다른 가수의 목소리로 변환하는 프로그램입니다.

## 주요 기능

- **유튜브 음원 다운로드**: 유튜브 링크를 입력받아 음원 파일을 다운로드합니다.
- **음성 분리 및 변환**: `source.wav`와 `target.wav` 파일을 사용하여 음성을 변환합니다.
- **결과물 저장**: 변환된 음원을 `mp3` 파일로 저장합니다.

## 사용 방법

1. **환경 설정**
    - Python 3.7+를 설치합니다.
    - 필요한 라이브러리(`pytube`, `librosa`, `tensorflow`, `ffmpeg-python`)를 설치합니다.
    - **FFmpeg**를 설치하고 시스템 환경 변수에 경로를 추가합니다.
2. **음원 파일 준비**
    - 변환할 음원이 있는 유튜브 링크를 준비합니다.
    - 변환의 원본이 될 보컬 음원 `source.wav` 파일과, 목표로 하는 목소리의 `target.wav` 파일을 준비합니다.
3. **프로그램 실행**
    
    ```
    python main.py
    
    ```
    
4. **결과 확인**
    - `complete.mp3` 파일을 확인하여 변환 결과를 들을 수 있습니다.

## 파일 및 폴더 구조

- `main.py`: 프로그램의 주요 로직을 담고 있는 메인 파일입니다.
- `voice_converter.py`: 음성 변환 로직을 구현한 모듈입니다.
- `youtube_downloader.py`: 유튜브 다운로드 기능을 담당하는 모듈입니다.
- `pretrained_models`: 음성 변환에 사용되는 사전 학습된 모델 파일들이 저장됩니다.
- `data`: `source.wav`와 `target.wav` 파일이 위치합니다.
- `separated_audio`: 분리된 음성 파일이 저장되는 폴더입니다.
- `output.mp3`, `complete.mp3`: 최종 변환된 음원 파일입니다.

## 추가 기능 (선택 사항)

- 변환된 음원 미리듣기 기능.
- 다양한 음성 변환 옵션(피치, 속도 등) 제공.

## 개발 환경

- Python 3.7+
- Windows
