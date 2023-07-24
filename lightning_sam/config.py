from box import Box

config = {
    "num_devices": 1,
    "batch_size": 12,
    "num_workers": 2,
    "num_epochs": 505,
    "eval_interval": 100,
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
        "checkpoint": "/content/drive/MyDrive/sam_cp/sam_vit_h_4b8939.pth",
        "freeze": {
            "image_encoder": True,
            "prompt_encoder": True,
            "mask_decoder": False,
        },
    },
    "dataset": {
        "train": {
            "root_dir": "/content/drive/MyDrive/coco-training/datasets/train",
            "annotation_file": "/content/drive/MyDrive/coco-training/train.json"
        },
        "val": {
            "root_dir": "/content/drive/MyDrive/coco-training/datasets/test",
            "annotation_file": "/content/drive/MyDrive/coco-training/test.json"
        }
    }
}

cfg = Box(config)
