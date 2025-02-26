# LatentSync: Audio Conditioned Latent Diffusion Models for Lip Sync

## 📖 Abstract

I present LatentSync, an end-to-end lip sync framework based on audio-conditioned latent diffusion models, eliminating the need for any intermediate motion representation. Unlike previous diffusion-based lip sync methods that rely on pixel-space diffusion or two-stage generation, LatentSync directly models complex audio-visual correlations by leveraging the powerful capabilities of Stable Diffusion.

One major challenge in diffusion-based lip sync methods is maintaining temporal consistency across frames due to inconsistencies in the diffusion process. To address this, I introduce Temporal REPresentation Alignment (TREPA), a technique designed to enhance temporal coherence while preserving lip-sync accuracy. TREPA utilizes temporal representations extracted from large-scale self-supervised video models to align generated frames with ground truth frames, ensuring smooth and natural lip movements.

## 🎬 Demo

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td width="50%"><b>Original Image</b></td>
        <td width="50%"><b>Lip-synced video</b></td>
  </tr>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/Saif-Ustad/LipSync/main/assets/generated_inputs_for_model/Input_Image_1.png" width="300">
    </td>
    <td>
      <video src="https://github.com/user-attachments/assets/b6b74890-1fdc-476b-bdc3-b1a393e6722a" controls preload></video>
    </td>
  </tr>
</table>


## 📑 source Plan

- [x] Inference code and checkpoints
- [x] Data processing pipeline
- [x] Training code

## 🔧 Setting up the Environment

Install the required packages and download the checkpoints via:

```bash
source setup_env.sh
```

If the download is successful, the checkpoints should appear as follows:

```
./checkpoints/
|-- latentsync_unet.pt
|-- latentsync_syncnet.pt
|-- whisper
|   `-- tiny.pt
|-- auxiliary
|   |-- 2DFAN4-cd938726ad.zip
|   |-- i3d_torchscript.pt
|   |-- koniq_pretrained.pkl
|   |-- s3fd-619a316812.pth
|   |-- sfd_face.pth
|   |-- syncnet_v2.model
|   |-- vgg16-397923af.pth
|   `-- vit_g_hybrid_pt_1200e_ssv2_ft.pth
```

These already include all the checkpoints required for latentsync training and inference. If you just want to try inference, you only need to download `latentsync_unet.pt` and `tiny.pt` from our [HuggingFace repo](https://huggingface.co/ByteDance/LatentSync)

## 🚀 Inference

There are two ways to perform inference, and both require 6.5 GB of VRAM.

### 1. Gradio App

Run the Gradio app for inference:

```bash
python gradio_app.py
```

### 2. Command Line Interface

Run the script for inference:

```bash
./inference.sh
```

You can change the parameters `inference_steps` and `guidance_scale` to see more results.

## 🏋️‍♂️ Training U-Net

Before training, you must process the data as described above and download all the checkpoints. We released a pretrained SyncNet with 94% accuracy on the VoxCeleb2 dataset for the supervision of U-Net training. Note that this SyncNet is trained on affine transformed videos, so when using or evaluating this SyncNet, you need to perform affine transformation on the video first (the code of affine transformation is included in the data processing pipeline).

If all the preparations are complete, you can train the U-Net with the following script:

```bash
./train_unet.sh
```

You should change the parameters in U-Net config file to specify the data directory, checkpoint save path, and other training hyperparameters.

## 🏋️‍♂️ Training SyncNet

In case you want to train SyncNet on your own datasets, you can run the following script. The data processing pipeline for SyncNet is the same as U-Net. 

```bash
./train_syncnet.sh
```

After `validations_steps` training, the loss charts will be saved in `train_output_dir`. They contain both the training and validation loss.

## 📊 Evaluation

You can evaluate the [sync confidence score](https://www.robots.ox.ac.uk/~vgg/publications/2016/Chung16a/chung16a.pdf) of a generated video by running the following script:

```bash
./eval/eval_sync_conf.sh
```

You can evaluate the accuracy of SyncNet on a dataset by running the following script:

```bash
./eval/eval_syncnet_acc.sh
```
