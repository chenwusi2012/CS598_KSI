# Reproduction Study for CS598 Deep Learning for Healthcare (Team 13, Paper 184)
## Original Paper
The repository contains the code to reproduce the result of the main experiment of the paper: Bai, T., Vucetic, S., Improving Medical Code Prediction from Clinical Text via Incorporating Online Knowledge Sources, The Web Conference (WWW'19), 2019.
- Link to the original paper: [https://doi.org/10.1145/3308558.3313485](https://doi.org/10.1145/3308558.3313485).
- Link to the GitHub repository of the original paper: [https://github.com/tiantiantu/KSI](https://github.com/tiantiantu/KSI).
## Dependency
To reproduce the result, run notebook file KSI.ipynb in Google Colab environment. Therefore, there is no need to set up the environment on a local machine.
## Dataset
To reproduce the result, the following dataset are used:
- ***Clinical notes and diagnosis in MIMIC-III dataset***: To gain access to this dataset, pass the training "CITI Data or Specimens Only Research" at [https://about.citiprogram.org/](https://about.citiprogram.org/), and apply for the access to the MIMIC-III Clinical Database at PhysioNet at [https://physionet.org/content/mimiciii/1.4/](https://physionet.org/content/mimiciii/1.4/). After gaining the access, download "NOTEEVENTS.csv" and "DIAGNOSES_ICD.csv" from PhysioNet, and upload these two CSV files to a created folder "cs598_project" in Google drive. The notebook KSI.ipynb will load these two CSV files from Google drive.
- ***Wikipedia pages of ICD-9 diagnosis codes***: This is available at [https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge](https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge). The notebook KSI.ipynb will download this file from the GitHub repository of the original paper automatically.
## Data Preprocessing
The code for data preprocessing is included in the notebook KSI.ipynb.
## Model Training
The notebook KSI.ipynb includes the code for training the following four baseline deep learning models and the four models with KSI framework:
- Recurrent neural network (RNN).
- Recurrent neural network with attention (RNNatt).
- Convolutional neural network (CNN).
- Convolutional attention (CAML).
## Model Evaluation
The code for model evaluation is included in the notebook KSI.ipynb.
## Pretrained model

- RNN:
- RNN with KSI framework:
- RNN with attention:
- RNN with attention and KSI framework:
- CNN:
- CNN with KSI framework:
- CAML:
- CAML with KSI framework:
## Result
The following table shows the performance of the standalone baseline models and the baseline models with KSI framework in the task of ICD-9 diagnosis code prediction from the clinical notes from MIMIC-III dataset.

| Method     | Macro AUC | Micro AUC | Macro F1 | Micro F1 | Test loss value | Top-10 recall |
|------------|-----------|-----------|----------|----------|-----------------|---------------|
| RNN        | 0.843     | 0.970     | 0.208    | 0.646    | 0.034           | 0.768         |
| KSI+RNN    | 0.873     | 0.976     | 0.249    | 0.657    | 0.032           | 0.792         |
| RNNatt     | 0.843     | 0.974     | 0.249    | 0.650    | 0.034           | 0.793         |
| KSI+RNNatt | 0.885     | 0.978     | 0.293    | 0.664    | 0.032           | 0.807         |
| CNN        | 0.836     | 0.966     | 0.214    | 0.627    | 0.039           | 0.753         |
| KSI+CNN    | 0.871     | 0.973     | 0.242    | 0.643    | 0.037           | 0.779         |
| CAML       | 0.854     | 0.978     | 0.281    | 0.676    | 0.033           | 0.808         |
| KSI+CAML   | 0.878     | 0.980     | 0.292    | 0.664    | 0.032           | 0.814         |

The following table show the macro-averaged AUC scores by the frequency of the ICD-9 diagnosis codes in MIMIC-III dataset.

| Baseline model | Code group | Standalone model | Model with KSI | Improvement |
|----------------|------------|------------------|----------------|-------------|
| RNN            | [1, 10]    | 0.520 (0.78)     | 0.709 (0.80)   | 0.189       |
| RNN            | [11, 50]   | 0.461 (0.79)     | 0.724 (0.83)   | 0.263       |
| RNN            | [51, 100]  | 0508 (0.84)      | 0.822 (0.89)   | 0.314       |
| RNN            | [101, 500] | 0.869 (0.88)     | 0.898 (0.90)   | 0.029       |
| RNN            | [500, +∞)  | 0.923 (0.91)     | 0.932 (0.92)   | 0.009       |
| RNNatt         | [1, 10]    | 0.540 (0.69)     | 0.699 (0.78)   | 0.159       |
| RNNatt         | [11, 50]   | 0.504 (0.79)     | 0.723 (0.83)   | 0.219       |
| RNNatt         | [51, 100]  | 0.488 (0.89)     | 0.831 (0.90)   | 0.343       |
| RNNatt         | [101, 500] | 0.887 (0.90)     | 0.900 (0.91)   | 0.013       |
| RNNatt         | [500, +∞)  | 0.940 (0.92)     | 0.943 (0.92)   | 0.003       |
| CNN            | [1, 10]    | 0.512 (0.64)     | 0.698 (0.71)   | 0.186       |
| CNN            | [11, 50]   | 0.482 (0.78)     | 0.734 (0.81)   | 0.252       |
| CNN            | [51, 100]  | 0.603 (0.83)     | 0.827 (0.90)   | 0.224       |
| CNN            | [101, 500] | 0.840 (0.87)     | 0.899 (0.90)   | 0.059       |
| CNN            | [500, +∞)  | 0.912 (0.91)     | 0.922 (0.92)   | 0.010       |
| CAML           | [1, 10]    | 0.530 (0.69)     | 0.663 (0.79)   | 0.133       |
| CAML           | [11, 50]   | 0.540 (0.80)     | 0.732 (0.84)   | 0.192       |
| CAML           | [51, 100]  | 0.785 (0.85)     | 0.865 (0.90)   | 0.080       |
| CAML           | [101, 500] | 0.897 (0.90)     | 0.910 (0.91)   | 0.013       |
| CAML           | [500, +∞)  | 0.934 (0.93)     | 0.937 (0.93)   | 0.003       |