# data-prepare
From vasp MD results to prepare training data for nequip machine learning training.

For nequip machine learning training, we could prepare extxyz file from VASP OUTCAR as input. The python file in this folder shows how to extract data from OUTCAR, how to train the model and finally how to test our model.

1.Do VASP AIMD calculations. You can use [INCAR_MDexample].
2.From VASP AIMD calculations get training data using [write_extxyz.py] (OUTCAR >> extxyz file)
3.Use nequip to train our model. You will use nequip-data.extxyz in input folder and [config.yaml].
4.To get the model. Command: nequip-deploy build --train-dir path/to/training/session/ where/to/put/deployed_model.pth
(you can name it as cdsemodel.pth) 
5.Test the model. Compare energies and forces from vasp scf calculations and machine learning results.
SCF: Get Structures from new OUTCAR using [scf_prepare_structures], and write bash code to do scf calculations.      
[get_forces_scf] and [get_energies_scf] can help you get the scf data.
ML: [get_forces_model] and [get_energies_model].
6.Plot the results: [energy_plot_result] and [force_plot_result].
