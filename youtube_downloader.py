import yt_dlp
import os

def download_youtube_audio(youtube_url, output_path="data/wav", filename="audio.wav"):
    """
    yt-dlp를 사용하여 유튜브 오디오를 다운로드하고 wav로 변환합니다.
    """
    # 다운로드할 폴더가 없으면 생성합니다.
    os.makedirs(output_path, exist_ok=True)

    # yt-dlp 옵션 설정
    ydl_opts = {
        # ffmpeg가 설치된 폴더의 bin 폴더 경로를 지정합니다.
        'ffmpeg_location': 'C:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe',
        'format': 'bestaudio',
        'outtmpl': os.path.join(output_path, filename),
        # 후처리기: 다운로드 후 ffmpeg를 이용해 wav로 변환
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"다운로드 시작: {youtube_url}")
            ydl.download([youtube_url])
            # 실제 생성된 파일 경로를 반환합니다.
            downloaded_file = os.path.join(output_path, filename)
            print(f"다운로드 완료: {downloaded_file}")
            return downloaded_file
    except Exception as e:
        print(f"오디오 다운로드 중 오류 발생: {e}")
        return None