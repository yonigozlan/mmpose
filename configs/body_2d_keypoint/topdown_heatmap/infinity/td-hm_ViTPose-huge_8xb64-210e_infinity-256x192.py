_base_ = ["../../../_base_/default_runtime.py"]

# runtime
train_cfg = dict(max_epochs=210, val_interval=5)

# optimizer
custom_imports = dict(
    imports=["mmpose.engine.optim_wrappers.layer_decay_optim_wrapper"],
    allow_failed_imports=False,
)

optim_wrapper = dict(
    optimizer=dict(type="AdamW", lr=5e-4, betas=(0.9, 0.999), weight_decay=0.1),
    paramwise_cfg=dict(
        num_layers=32,
        layer_decay_rate=0.85,
        custom_keys={
            "bias": dict(decay_multi=0.0),
            "pos_embed": dict(decay_mult=0.0),
            "relative_position_bias_table": dict(decay_mult=0.0),
            "norm": dict(decay_mult=0.0),
        },
    ),
    constructor="LayerDecayOptimWrapperConstructor",
    clip_grad=dict(max_norm=1.0, norm_type=2),
)

# learning policy
param_scheduler = [
    dict(
        type="LinearLR", begin=0, end=500, start_factor=0.001, by_epoch=False
    ),  # warm-up
    dict(
        type="MultiStepLR",
        begin=0,
        end=210,
        milestones=[170, 200],
        gamma=0.1,
        by_epoch=True,
    ),
]

# automatically scaling LR based on the actual training batch size
auto_scale_lr = dict(base_batch_size=512)

# codec settings
codec = dict(type="UDPHeatmap", input_size=(192, 256), heatmap_size=(48, 64), sigma=2)

# model settings
model = dict(
    type="TopdownPoseEstimator",
    data_preprocessor=dict(
        type="PoseDataPreprocessor",
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True,
    ),
    backbone=dict(
        type="mmcls.VisionTransformer",
        arch="huge",
        img_size=(256, 192),
        patch_size=16,
        qkv_bias=True,
        drop_path_rate=0.55,
        with_cls_token=False,
        output_cls_token=False,
        patch_cfg=dict(padding=2),
        init_cfg=dict(
            type="Pretrained",
            checkpoint="/scratch/users/yonigoz/mmpose_data/ckpts/vit/"
            "td-hm_ViTPose-huge_8xb64-210e_coco-256x192-e32adcd4_20230314.pth",
            prefix="backbone",
        ),
    ),
    head=dict(
        type="HeatmapHead",
        in_channels=1280,
        out_channels=53,
        deconv_out_channels=(256, 256),
        deconv_kernel_sizes=(4, 4),
        loss=dict(type="KeypointMSELoss", use_target_weight=True),
        decoder=codec,
    ),
    test_cfg=dict(
        flip_test=True,
        flip_mode="heatmap",
        shift_heatmap=False,
    ),
)

# base dataset settings
data_root = "../"
dataset_type = "InfinityDataset"
data_mode = "topdown"

# pipelines
train_pipeline = [
    dict(type="LoadImage"),
    dict(type="GetBBoxCenterScale"),
    dict(type="RandomFlip", direction="horizontal"),
    dict(type="RandomHalfBody"),
    dict(type="RandomBBoxTransform"),
    dict(type="TopdownAffine", input_size=codec["input_size"], use_udp=True),
    dict(type="GenerateTarget", encoder=codec),
    dict(type="PackPoseInputs"),
]
val_pipeline = [
    dict(type="LoadImage"),
    dict(type="GetBBoxCenterScale"),
    dict(type="TopdownAffine", input_size=codec["input_size"], use_udp=True),
    dict(type="PackPoseInputs"),
]

# data loaders
train_dataloader = dict(
    batch_size=8,
    num_workers=0,
    persistent_workers=False,
    sampler=dict(type="DefaultSampler", shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_mode=data_mode,
        ann_file="combined_dataset/train/annotations.json",
        data_prefix=dict(img=""),
        pipeline=train_pipeline,
    ),
)
val_dataloader = dict(
    batch_size=4,
    num_workers=0,
    persistent_workers=False,
    drop_last=False,
    sampler=dict(type="DefaultSampler", shuffle=False, round_up=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_mode=data_mode,
        ann_file="combined_dataset/test/annotations.json",
        data_prefix=dict(img=""),
        test_mode=True,
        pipeline=val_pipeline,
    ),
)
test_dataloader = val_dataloader

# evaluators
val_evaluator = [
    dict(
        type="InfinityMetric",
        ann_file=data_root + "combined_dataset/test/annotations.json",
        use_area=False,
    ),
    dict(
        type="InfinityCocoMetric",
        ann_file=data_root + "combined_dataset/test/annotations.json",
        use_area=False,
    ),
    dict(
        type="InfinityAnatomicalMetric",
        ann_file=data_root + "combined_dataset/test/annotations.json",
        use_area=False,
    ),
]

test_evaluator = val_evaluator


# visualizer
vis_backends = [
    dict(type="LocalVisBackend"),
    # dict(type='TensorboardVisBackend'),
    dict(
        type="WandbVisBackend",
        init_kwargs=dict(
            project="synthetic_finetuning", entity="yonigoz", name="infinity/ViT/huge"
        ),
    ),
]
visualizer = dict(
    type="PoseLocalVisualizer", vis_backends=vis_backends, name="visualizer"
)

default_hooks = dict(
    timer=dict(type="IterTimerHook"),
    logger=dict(type="LoggerHook", interval=10),
    param_scheduler=dict(type="ParamSchedulerHook"),
    checkpoint=dict(save_best="infinity/AP", rule="greater", max_keep_ckpts=2),
    sampler_seed=dict(type="DistSamplerSeedHook"),
    visualization=dict(type="PoseVisualizationHook", enable=True, interval=5),
)

work_dir = "/scratch/users/yonigoz/mmpose_data/work_dirs/infinity/ViT/huge"