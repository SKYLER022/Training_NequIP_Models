🚀 Data Preparation for ML with NequIP

Prepare training data for NequIP machine learning models using VASP MD results. This repository provides tools to extract data, train models, and validate predictions.

🌟 Features

Extract training data in extxyz format from VASP's OUTCAR.
Seamless integration with NequIP for machine learning training.
Tools for testing and validating ML models against SCF calculations.
Scripts for visualizing results with energy and force comparison plots.
📋 Workflow

1. Perform VASP AIMD Calculations
Prepare molecular dynamics (MD) simulations using VASP. Use the provided example INCAR file: INCAR_MDexample.

2. Generate Training Data
Use the script write_extxyz.py to convert data from VASP's OUTCAR to an extxyz file for training.

python write_extxyz.py OUTCAR nequip-data.extxyz
3. Train the Model with NequIP
Train the NequIP model using nequip-data.extxyz and a configuration file config.yaml.

nequip-train config.yaml
4. Deploy the Model
Once training is complete, deploy the trained model:

nequip-deploy build --train-dir path/to/training/session/ --out cdsemodel.pth
5. Validate the Model
Compare energies and forces between SCF calculations and ML predictions:

SCF Calculations:
Extract structures for SCF using scf_prepare_structures.py.
Perform SCF calculations using a bash script.
Use get_forces_scf and get_energies_scf to extract SCF results.
ML Predictions:
Use get_forces_model and get_energies_model to obtain ML predictions.
6. Visualize Results
Plot energy and force comparisons:

python energy_plot_result.py
python force_plot_result.py
📦 Files and Scripts

File/Script	Description
INCAR_MDexample	Example INCAR file for VASP MD calculations.
write_extxyz.py	Extracts training data from OUTCAR to extxyz.
config.yaml	Configuration file for NequIP training.
scf_prepare_structures	Prepares structures for SCF calculations.
get_forces_scf	Extracts forces from SCF results.
get_energies_scf	Extracts energies from SCF results.
get_forces_model	Extracts forces from ML predictions.
get_energies_model	Extracts energies from ML predictions.
energy_plot_result.py	Plots energy comparison results.
force_plot_result.py	Plots force comparison results.

