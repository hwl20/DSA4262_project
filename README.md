# DSA4262_project

MRNet is the main data
MRNet_alexnet is subsetted data (21 training, 120 validation) trained on alexnet
MRNet_mobilenet is subsetted data (21 training, 120 validation) trained on mobilenet

To use:
Training:
$ python -u src/train_cnn_models.py MRNet-v1.0 axial 10
$ python -u src/train_cnn_models.py MRNet-v1.0 coronal 10
$ python -u src/train_cnn_models.py MRNet-v1.0 sagittal 10

$python3 -u src/train_lr_models.py MRNet-v1.0 /models

Evaluation:
$python3 -u src/evaluate.py all_valid_paths.csv output/dir/predictions.csv MRNet-v1.0/valid_labels.csv
