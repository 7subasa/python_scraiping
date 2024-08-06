import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_dir = 'videos'

# 動画ファイル取得
video_files = [f for f in os.listdir(video_dir) if f.endswith(('.MP4', '.MOV'))]

# 動画ファイルのパス作成
video_paths = [os.path.join(video_dir, file) for file in video_files]

# 動画を順番に読み込み
video_clips = [VideoFileClip(file) for file in video_paths]

# 連結
convert_video = concatenate_videoclips(video_clips, method='compose')

# 書き出し
convert_video.write_videofile('convert_video.mp4')

