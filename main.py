import argparse
import os
from youtube_downloader import download_youtube_audio
from voice_converter import convert_voice, convert_wav_to_mp3, separate_audio
import subprocess

# ffmpeg 경로
ffmpeg_path = "C:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe"

def combine_audio(vocal_file, accompaniment_file, output_file):
    try:
        command = [
            ffmpeg_path,
            "-i", vocal_file,
            "-i", accompaniment_file,
            "-filter_complex", "[1:a]volume=0.5[a1];[0:a][a1]amix=inputs=2:duration=longest",
            "-y", output_file  # 덮어쓰기 허용
        ]
        print(f"{vocal_file}와 {accompaniment_file} 합치기 시작...")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"합치기 완료: {output_file}")
    except Exception as e:
        print(f"합치기 오류: {e}")

def main():
    combine_audio("output.mp3", os.path.join("separated_audio", "source", "accompaniment.mp3"), "complete.mp3")
    return

    parser = argparse.ArgumentParser(description="유튜브 영상의 음성을 다른 가수의 목소리로 변환합니다.")
    parser.add_argument("--youtube_url", required=True, help="변환할 원본 노래의 유튜브 URL")
    parser.add_argument("--singer_url", required=True, help="목소리 스타일을 가져올 가수의 유튜브 URL")
    args = parser.parse_args()

    print(">> 1. 유튜브 오디오 다운로드를 시작합니다...")

    source_wav_file = download_youtube_audio(args.youtube_url, filename="source.wav")
    target_wav_file = download_youtube_audio(args.singer_url, filename="target.wav")

    if source_wav_file and target_wav_file:
        print(f"\n>> 다운로드 성공")
        print(f"   원본 음성: {source_wav_file}")
        print(f"   대상 목소리: {target_wav_file}")

        source_mp3_file = "source.mp3"
        target_mp3_file = "target.mp3"

        #convert_wav_to_mp3(source_wav_file, source_mp3_file)
        #convert_wav_to_mp3(target_wav_file, target_mp3_file)

        output_dir = "separated_audio"
        os.makedirs(output_dir, exist_ok=True)

        source_vocal, source_accompaniment = separate_audio(source_mp3_file, output_dir, "source")
        target_vocal, _ = separate_audio(target_mp3_file, output_dir, "target")

        if source_vocal and source_accompaniment and target_vocal:
            print("\n>> 2. 음성 변환을 시작합니다...")

            output_file_name = "output.mp3"
            convert_voice(os.path.join(output_dir, "source", source_vocal), os.path.join(output_dir, "target", target_vocal), output_file_name)

            final_output = "complete.mp3"
            combine_audio(output_file_name, os.path.join(output_dir, "source", source_accompaniment), final_output)

        else:
            print("음성 분리 실패")

    else:
        print("오디오 다운로드에 실패하여 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()