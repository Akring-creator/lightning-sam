from box import Box

config = {
    "num_devices": 4,
    "batch_size": 12,
    "num_workers": 4,
    "num_epochs": 20,
    "eval_interval": 2,
    "out_dir": "out/training",
    "opt": {
        "learning_rate": 8e-4,
        "weight_decay": 1e-4,
        "decay_factor": 10,
        "steps": [60000, 86666],
        "warmup_steps": 250,
    },
    "model": {
        "type": 'vit_h',
        "checkpoint": "/content/drive/MyDrive/sam_cp/sam_vit_h_4b8939 (1).pth",
        "freeze": {
            "image_encoder": True,
            "prompt_encoder": True,
            "mask_decoder": False,
        },
    },
    "dataset": {
        "train": {
            "root_dir": "/content/drive/MyDrive/coco-training/datasets/train",
            "annotation_file": "/content/drive/MyDrive/coco-training/SAM Model-2.json"
        },
        "val": {
            "root_dir": "/content/drive/MyDrive/coco-training/datasets/test",
            "annotation_file": "/content/drive/MyDrive/coco-training/test-3.json"
        }
    }
}

cfg = Box(config)
