import cv2
import ffmpeg
import numpy as np

def image_to_video(image_path, video_out_path, fps=30, duration=45, bitrate="5M"):
    """
    Convert a single image into a high-quality video using FFmpeg.

    Args:
        image_path (str): Path to the input image.
        video_out_path (str): Path to save the generated video.
        fps (int): Frames per second (30-60 recommended for smoothness).
        duration (int): Duration of the video in seconds.
        bitrate (str): Video bitrate (e.g., '5M' for high quality).
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_video = "temp_video.mp4"

    out = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

    num_frames = fps * duration  # Total frames in the video
    for _ in range(num_frames):
        out.write(image)
    
    out.release()
    
    # Re-encode using FFmpeg for higher quality
    ffmpeg.input(temp_video).output(video_out_path, vcodec='libx264', bitrate=bitrate, preset='slow').run(overwrite_output=True)
    
    print(f"✅ High-quality video generated: {video_out_path}")

# Example Usage:
image_to_video("assets/generated_inputs_for_model/Input_Image_1.png", "assets/generated_inputs_for_model/input_video1.mp4", fps=60, duration=40, bitrate="5M")
