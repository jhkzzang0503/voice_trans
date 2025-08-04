import torch
from TTS.api import TTS
import subprocess
import os
from spleeter.separator import Separator

# ffmpeg 경로
ffmpeg_path = "C:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe"

def convert_wav_to_mp3(wav_file, mp3_file):
    try:
        command = [
            ffmpeg_path,
            "-i", wav_file,
            "-y",  # 덮어쓰기 허용
            mp3_file
        ]
        print(f"{wav_file} -> {mp3_file} 변환 시작...")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"변환 완료: {mp3_file}")
    except Exception as e:
        print(f"변환 오류: {e}")


def separate_audio(mp3_file, output_dir, output_dir2):
    try:
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(f"{mp3_file}", f"{output_dir}")
        print(f"{mp3_file} 음성 분리 완료.")

        convert_wav_to_mp3(os.path.join(output_dir, output_dir2, "vocals.wav"), os.path.join(output_dir, output_dir2, "vocals.mp3"))
        convert_wav_to_mp3(os.path.join(output_dir, output_dir2, "accompaniment.wav"), os.path.join(output_dir, output_dir2, "accompaniment.mp3"))

        return 'vocals.mp3', 'accompaniment.mp3'
    except Exception as e:
        print(f"음성 분리 오류: {e}")
        return None, None

def convert_voice(source_wav, target_wav, output_mp3):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("voice_conversion_models/multilingual/vctk/freevc24").to(device)

    # 변환 과정에서 생성될 임시 wav 파일 경로
    temp_output_wav = output_mp3.replace('.mp3', '.wav')

    try:
        print("음성 변환 시작...")
        tts.voice_conversion_to_file(
            source_wav=source_wav,
            target_wav=target_wav,
            file_path=temp_output_wav
        )
        print(f"음성 변환 완료: {temp_output_wav}")

        # subprocess를 사용하여 ffmpeg로 wav를 mp3로 변환
        command = [
            ffmpeg_path,
            "-i", temp_output_wav,
            "-y", # 덮어쓰기 허용
            output_mp3
        ]
        print("MP3 변환 시작...")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"MP3 변환 완료: {output_mp3}")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        # 최종 작업 후 임시 wav 파일이 존재하면 삭제
        if os.path.exists(temp_output_wav):
            os.remove(temp_output_wav)
            print(f"임시 파일 삭제: {temp_output_wav}")