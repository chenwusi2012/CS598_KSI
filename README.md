# Reproduction Study for CS598 Deep Learning for Healthcare (Team 13, Paper 184)
## Original Paper

The repository contains the code to reproduce the result of the main experiment of the paper: **Bai, T., Vucetic, S., Improving Medical Code Prediction from Clinical Text via Incorporating Online Knowledge Sources, The Web Conference (WWW'19), 2019**.
- Link to the original paper: [https://doi.org/10.1145/3308558.3313485](https://doi.org/10.1145/3308558.3313485).
- Link to the GitHub repository of the original paper: [https://github.com/tiantiantu/KSI](https://github.com/tiantiantu/KSI).

## Dependency

To reproduce the result, run notebook file KSI_main.ipynb in Google Colab environment. If you would like to run ksi_main.ipynb on a local machine, update the version of Python to Python 3.10.11 and install the following dependencies:
- torch==2.0.0
- numpy==1.22.4
- sklearn==1.2.2
- stop-words==2018.7.23
- pandas==1.5.3
requirements.txt is included in this repository. You can install the above dependencies automatically by running the following command:
```shell
pip install -r requirements.txt
```

## Dataset (Data Download Instruction)

To reproduce the result, the following dataset are used:
- ***Discharge summary notes and accompanying ICD-9 diagnosis codes from MIMIC-III dataset***: To gain access to this dataset, pass the training "CITI Data or Specimens Only Research" at [https://about.citiprogram.org/](https://about.citiprogram.org/), and apply for the access to the MIMIC-III Clinical Database at PhysioNet at [https://physionet.org/content/mimiciii/1.4/](https://physionet.org/content/mimiciii/1.4/). After gaining the access, download "NOTEEVENTS.csv" and "DIAGNOSES_ICD.csv" from PhysioNet, and upload these two CSV files to a created folder "cs598_project" in Google Drive. The notebook KSI_main.ipynb will load these two CSV files from Google Drive.
- ***Wikipedia pages of ICD-9 diagnosis codes***: This is available at [https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge](https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge). The notebook KSI_main.ipynb will download this file from the GitHub repository of the original paper automatically.
## Data Preprocessing

The code for data preprocessing is included in the notebook KSI_main.ipynb. Please refer to section 3 of the notebook KSI_main.ipynb.

## Model Training

The notebook KSI_main.ipynb and the Python file training.py includes the code for training the following four baseline deep learning models and the baseline models with the KSI framework:
- Recurrent neural network (RNN).
- Recurrent neural network with attention (RNNatt).
- Convolutional neural network (CNN).
- Convolutional attention (CAML).


## Model Evaluation

The code for model evaluation is included in the notebook KSI_main.ipynb and the Python file testing.py.

## Pretrained Model

The folder pretrained_models includes the following pre-trained models:
- RNN: RNN_model.zip
- RNN with the KSI framework: KSI_RNN_model.zip
- RNN with attention: RNNattn_model.zip
- RNN with attention and the KSI framework: KSI_RNNattn_model.zip
- CNN: CNN_model.zip 
- CNN with KSI framework: KSI_CNN_model.zip
- CAML: CAML_model.zip
- CAML with KSI framework: KSI_CAML_model.zip

## Files in This Repository

- KSI_main.ipynb: The Google Colab notebook to reproduce the main result of the original paper.
- KSI_ablation1: The Google Colab notebook for ablation study 1 of the reproduction study (section 4.3 of the report).
- KSI_ablation2: The Google Colab notebook for ablation study 2 of the reproduction study (section 4.4 of the report).
- preprocessing.py: Include the function to process the training dataset, validation dataset, and testing dataset.
- training.py: Include the functions to train the deep learning models used in this reproduction study.
- testing.py: Include the functions to train the deep learning models used in this reproduction study.
- Pretrained models: RNN_model.zip, KSI_RNN_model.zip, RNNattn_model.zip, KSI_RNNattn_model.zip, CNN_model.zip, KSI_CNN_model.zip, CAML_model.zip, KSI_CAML_model.zip

## Result
The following table shows the performance of the standalone baseline models and the baseline models with KSI framework in the task of ICD-9 diagnosis code prediction from the clinical notes from MIMIC-III dataset. The result of the following table can be reproduced by running the notebook KSI_main.ipynb.

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

The following table show the macro-averaged AUC scores by the frequency of the ICD-9 diagnosis codes in MIMIC-III dataset. The result of the following table can be reproduced by adjusting the values of the variables ***lower_limit_freq*** and ***upper_limit_freq*** in the section ***3.1 Data Pre-processing 1*** in the notebook KSI_main.ipynb and running the notebook.

| Baseline model | Code group | Standalone model | Model with KSI | Improvement |
|----------------|------------|------------------|----------------|-------------|
| RNN            | [1, 10]    | 0.550 (0.78)     | 0.709 (0.80)   | 0.159       |
| RNN            | [11, 50]   | 0.641 (0.79)     | 0.784 (0.83)   | 0.143       |
| RNN            | [51, 100]  | 0.738 (0.84)     | 0.832 (0.89)   | 0.094       |
| RNN            | [101, 500] | 0.869 (0.88)     | 0.898 (0.90)   | 0.029       |
| RNN            | [500, +∞)  | 0.923 (0.91)     | 0.932 (0.92)   | 0.009       |
| RNNatt         | [1, 10]    | 0.530 (0.69)     | 0.699 (0.78)   | 0.169       |
| RNNatt         | [11, 50]   | 0.614 (0.79)     | 0.723 (0.83)   | 0.109       |
| RNNatt         | [51, 100]  | 0.748 (0.89)     | 0.831 (0.90)   | 0.083       |
| RNNatt         | [101, 500] | 0.887 (0.90)     | 0.900 (0.91)   | 0.013       |
| RNNatt         | [500, +∞)  | 0.940 (0.92)     | 0.943 (0.92)   | 0.003       |
| CNN            | [1, 10]    | 0.532 (0.64)     | 0.698 (0.71)   | 0.166       |
| CNN            | [11, 50]   | 0.612 (0.78)     | 0.734 (0.81)   | 0.122       |
| CNN            | [51, 100]  | 0.723 (0.83)     | 0.827 (0.90)   | 0.104       |
| CNN            | [101, 500] | 0.840 (0.87)     | 0.899 (0.90)   | 0.059       |
| CNN            | [500, +∞)  | 0.912 (0.91)     | 0.922 (0.92)   | 0.010       |
| CAML           | [1, 10]    | 0.530 (0.69)     | 0.663 (0.79)   | 0.133       |
| CAML           | [11, 50]   | 0.640 (0.80)     | 0.752 (0.84)   | 0.112       |
| CAML           | [51, 100]  | 0.785 (0.85)     | 0.865 (0.90)   | 0.080       |
| CAML           | [101, 500] | 0.897 (0.90)     | 0.910 (0.91)   | 0.013       |
| CAML           | [500, +∞)  | 0.934 (0.93)     | 0.937 (0.93)   | 0.003       |