# DSA4262_project

MRNet is the main data
MRNet_alexnet is subsetted data (21 training, 120 validation) trained on alexnet
MRNet_mobilenet is subsetted data (21 training, 120 validation) trained on mobilenet

<br>
To use:
<br>

Training:
<br>

```terminal
$ python3 -u src/train_cnn_models.py MRNet-v1.0 axial 10
```

```terminal
$ python3 -u src/train_cnn_models.py MRNet-v1.0 coronal 10
```

```terminal
$ python3 -u src/train_cnn_models.py MRNet-v1.0 sagittal 10
```

```terminal
$python3 -u src/train_lr_models.py MRNet-v1.0 /models
```

<br>
Prediction: 
<br>

We need to create `src/cnn_models_paths.txt` and `src/lr_models_paths.txt` to point
the programme to the right models. This is so that it is easier to test different combinations of models, when you have many models developed in separate experiments.

Models need to be listed in a specific order:

<br>

Replace {epoch:02d} with the last epoch for that set of plane (i.e 01/02/03..../10)

```terminal
$ cat src/cnn_models_paths.txt
path/to/models/cnn_sagittal_abnormal_{epoch:02d}.pt
path/to/models/cnn_coronal_abnormal_{epoch:02d}.pt
path/to/models/cnn_axial_abnormal_{epoch:02d}.pt
path/to/models/cnn_sagittal_acl_{epoch:02d}.pt
path/to/models/cnn_coronal_acl_{epoch:02d}.pt
path/to/models/cnn_axial_acl_{epoch:02d}.pt
path/to/models/cnn_sagittal_meniscus_{epoch:02d}.pt
path/to/models/cnn_coronal_meniscus_{epoch:02d}.pt
path/to/models/cnn_axial_meniscus_{epoch:02d}.pt
```

```terminal
$ cat src/lr_models_paths.txt
path/to/models/lr_abnormal.pkl
path/to/models/lr_acl.pkl
path/to/models/lr_meniscus.pkl
```

Once we create these 2 files, we're ready to proceed. To generate predictions on the `valid` dataset, run:

```terminal
$ python -u src/predict.py valid-paths.csv output/dir
```

<br>
Evaluation:

```terminal
$python3 -u src/evaluate.py all_valid_paths.csv output/dir/predictions.csv MRNet-v1.0/valid_labels.csv
```
