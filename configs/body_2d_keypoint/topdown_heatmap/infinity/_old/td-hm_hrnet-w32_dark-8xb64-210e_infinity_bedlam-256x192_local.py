_base_ = ["../../../_base_/default_runtime.py"]

used_data_keys=[
        "nose",
        "left_eye",
        "right_eye",
        "left_ear",
        "right_ear",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_wrist",
        "right_wrist",
        "left_hip",
        "right_hip",
        "left_knee",
        "right_knee",
        "left_ankle",
        "right_ankle",
        "sternum",
        "rshoulder",
        "lshoulder",
        "r_lwrist",
        "l_lwrist",
        "r_mwrist",
        "l_mwrist",
        "r_ASIS",
        "l_ASIS",
        "r_PSIS",
        "l_PSIS",
        "r_ankle",
        "l_ankle",
        "r_mankle",
        "l_mankle",
        "r_5meta",
        "l_5meta",
        "r_big_toe",
        "l_big_toe",
        "l_calc",
        "r_calc",
        "C7",
        "L2",
        "T11",
        "T6",
    ]
# runtime
train_cfg = dict(max_epochs=210, val_interval=1)

# optimizer
optim_wrapper = dict(
    optimizer=dict(
        type="Adam",
        lr=5e-4,
    )
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

# hooks
default_hooks = dict(
    checkpoint=dict(save_best="infinity/AP", rule="greater", max_keep_ckpts=2)
)

# codec settings
codec = dict(
    type="MSRAHeatmap",
    input_size=(192, 256),
    heatmap_size=(48, 64),
    sigma=2,
    unbiased=True,
)

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
        type="HRNet",
        in_channels=3,
        extra=dict(
            stage1=dict(
                num_modules=1,
                num_branches=1,
                block="BOTTLENECK",
                num_blocks=(4,),
                num_channels=(64,),
            ),
            stage2=dict(
                num_modules=1,
                num_branches=2,
                block="BASIC",
                num_blocks=(4, 4),
                num_channels=(32, 64),
            ),
            stage3=dict(
                num_modules=4,
                num_branches=3,
                block="BASIC",
                num_blocks=(4, 4, 4),
                num_channels=(32, 64, 128),
            ),
            stage4=dict(
                num_modules=3,
                num_branches=4,
                block="BASIC",
                num_blocks=(4, 4, 4, 4),
                num_channels=(32, 64, 128, 256),
            ),
        ),
        init_cfg=dict(
            type="Pretrained",
            checkpoint="mmpose_data/ckpts/"
            "td-hm_hrnet-w32_dark-8xb64-210e_coco-256x192-0e00bf12_20220914.pth",
            prefix="backbone",
        ),
    ),
    head=dict(
        type="HeatmapHead",
        in_channels=32,
        out_channels=len(used_data_keys),
        deconv_out_channels=None,
        loss=dict(type="KeypointMSELoss", use_target_weight=True),
        decoder=codec,
    ),
    test_cfg=dict(
        flip_test=True,
        flip_mode="heatmap",
        shift_heatmap=True,
    ),
)

# base dataset settings
dataset_type = "InfinityDataset"
data_mode = "topdown"
data_root = "../"

# pipelines
train_pipeline = [
    dict(type="LoadImage", imdecode_backend="pillow"),
    dict(type="GetBBoxCenterScale"),
    dict(type="RandomFlip", direction="horizontal"),
    dict(type="RandomHalfBody"),
    dict(type="RandomBBoxTransform"),
    dict(type="TopdownAffine", input_size=codec["input_size"]),
    dict(type="GenerateTarget", encoder=codec),
    dict(type="PackPoseInputs"),
]
val_pipeline = [
    dict(type="LoadImage", imdecode_backend="pillow"),
    dict(type="GetBBoxCenterScale"),
    dict(type="TopdownAffine", input_size=codec["input_size"]),
    dict(type="PackPoseInputs"),
]

dataset_type = "InfinityDataset"
data_mode = "topdown"
data_root = "../"

dataset_infinity = dict(
    type=dataset_type,
    data_root=data_root,
    data_mode=data_mode,
    ann_file="combined_dataset_15fps/train/annotations.json",
    data_prefix=dict(img=""),
    pipeline=[],
    used_data_keys=used_data_keys,
)

dataset_coco = dict(
    type="CocoDataset",
    data_root="../deep-high-resolution-net.pytorch/data/coco",
    data_mode=data_mode,
    ann_file="annotations/person_keypoints_val2017.json",
    data_prefix=dict(img="images/val2017/"),
    pipeline=[
        dict(
            type="KeypointConverter",
            num_keypoints=len(used_data_keys),
            mapping=[
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
                (10, 10),
                (11, 11),
                (12, 12),
                (13, 13),
                (14, 14),
                (15, 15),
                (16, 16),
            ],
        )
    ],
)
# metainfo = dict(from_file="configs/_base_/datasets/infinity.py")
# print(metainfo)
# keypoint_info = sorted([(key, value) for key, value in metainfo["keypoint_info"].items()], key = lambda x: x[0])
# keypoint_info_filtered = [element[1] for element in element if element[1]["name"] in used_data_keys]
# keypoint_info_filtered_dict = {i: element for i, element in enumerate(keypoint_info_filtered)}
# for i, element in keypoint_info_filtered_dict.items():
#     element["id"] = i

# metainfo["keypoint_info"] = keypoint_info_filtered_dict
# metainfo["joint_weights"] = metainfo["joint_weights"][:len(used_data_keys)]
# metainfo["sigmas"] = metainfo["sigmas"][:len(used_data_keys)]

combined_dataset = dict(
    type="CombinedDataset",
    metainfo=dict(from_file="configs/_base_/datasets/infinity.py"),
    datasets=[dataset_infinity, dataset_coco],
    pipeline=train_pipeline,
    used_data_keys = used_data_keys,
    test_mode=False,
)

train_sampler = dict(
    type="MultiSourceSampler",
    batch_size=32,
    source_ratio=[1, 1],
    shuffle=True,
)


# data loaders
train_dataloader = dict(
    batch_size=12,
    num_workers=8,
    persistent_workers=True,
    sampler=train_sampler,
    dataset=combined_dataset
)

dataset_type = "InfinityDataset"
data_mode = "topdown"
data_root = "../"

val_dataloader = dict(
    batch_size=6,
    num_workers=8,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type="DefaultSampler", shuffle=False, round_up=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_mode=data_mode,
        ann_file="combined_dataset_15fps/test/annotations.json",
        data_prefix=dict(img=""),
        test_mode=True,
        pipeline=val_pipeline,
        used_data_keys=used_data_keys,
    ),
)
test_dataloader = val_dataloader

# evaluators
val_evaluator = [
    dict(
        type="InfinityMetric",
        ann_file=data_root
        + "combined_dataset_15fps/test/annotations.json",
        use_area=False,
        used_data_keys=used_data_keys,
    ),
    dict(
        type="InfinityCocoMetric",
        ann_file=data_root
        + "combined_dataset_15fps/test/annotations.json",
        use_area=False,
        used_data_keys=used_data_keys,
    ),
    dict(
        type="InfinityAnatomicalMetric",
        ann_file=data_root
        + "combined_dataset_15fps/test/annotations.json",
        use_area=False,
        used_data_keys=used_data_keys,
    ),
]

test_evaluator = val_evaluator

# visualizer
vis_backends = [
    dict(type="LocalVisBackend"),
    # dict(type='TensorboardVisBackend'),
    # dict(
    #     type="WandbVisBackend",
    #     init_kwargs=dict(
    #         project="synthetic_finetuning",
    #         entity="yonigoz",
    #         name="infinity/HRNet/w32_dark",
    #     ),
    # ),
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
    visualization=dict(type="PoseVisualizationHook", enable=True, interval=100),
)

work_dir = "./mmpose_data/work_dirs/infinity_bedlam/HRNet/w32_dark"