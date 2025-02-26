#!/bin/bash

python -m scripts.inference \
    --unet_config_path "configs/unet/second_stage.yaml" \
    --inference_ckpt_path "checkpoints/latentsync_unet.pt" \
    --inference_steps 30 \
    --guidance_scale 1.5 \
    --video_path "assets/generated_inputs_for_model/input_video1.mp4" \
    --audio_path "assets/generated_inputs_for_model/best_audio.wav" \
    --video_out_path "video_out7.mp4"



