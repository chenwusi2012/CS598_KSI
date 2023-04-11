# CS598_KSI
## Original Paper
The repository contains the code to reproduce the result of main experiment of the paper: Bai, T., Vucetic, S., Improving Medical Code Prediction from Clinical Text via Incorporating Online Knowledge Sources, The Web Conference (WWW'19), 2019.
- Link to the original paper: [https://doi.org/10.1145/3308558.3313485](https://doi.org/10.1145/3308558.3313485).
- Link to the original repository: [https://github.com/tiantiantu/KSI](https://github.com/tiantiantu/KSI).
## Dependency
To reproduce the result, run notebook file KSI.ipynb in Google Colab environment. Therefore, there is no need to set up the environment on a local machine.
## Dataset
To reproduce the result, the following dataset are used:
- ***Clinical notes and diagnosis in MIMIC-III dataset***: To gain access to this dataset, pass the training "CITI Data or Specimens Only Research" at [https://about.citiprogram.org/](https://about.citiprogram.org/), and apply the access to the MIMIC-III Clinical Database at PhysioNet at [https://physionet.org/content/mimiciii/1.4/](https://physionet.org/content/mimiciii/1.4/). After gaining the access, type the username and password in the notebook KSI.ipynb, and the notebook will download "NOTEEVENTS.csv" and "DIAGNOSES_ICD.csv" from PhysioNet automatically.
- ***Wikipedia pages of ICD-9 diagnosis codes***: This is available at [https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge](https://github.com/tiantiantu/KSI/blob/master/wikipedia_knowledge)