# data-prepare
From vasp MD results to prepare training data for machine learning training

For nequip machine learning training, we could prepare extxyz file from VASP OUTCAR as input. The python file in this folder shows how to extract data from OUTCAR, how to train the model and finally how to test our model.

1.Do VASP AIMD calculations.
2.From VASP AIMD calculations get training data.(OUTCAR >> extxyz file)
3.Use nequip to train our model.
4.Test the model.
