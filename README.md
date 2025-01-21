# SANSCOG-MRI-Pipeline

The **SANSCOG-MRI-Pipeline** repository contains scripts and workflows used in the **SANSCOG Study**. This study focuses on MRI data processing, management, extraction, and analysis, aiming to streamline neuroimaging research tasks.

## Overview

This repository serves as a centralized collection of scripts for:
- **Preprocessing**: Preparing raw MRI data for analysis.
- **Data Management**: Organizing, storing, and maintaining datasets.
- **Data Extraction**: Extracting key metrics and features from MRI datasets.
- **Neuroimaging Analysis**: Performing advanced analyses such as segmentation, connectivity mapping, and statistical modeling.

## Repository Structure

The repository is organized into the following directories:

```
SANSCOG-MRI-Pipeline/
|
├── preprocessing/         # Scripts for preprocessing MRI data
├── data_management/       # Tools for dataset organization and curation
├── data_extraction/       # Scripts for extracting features and metrics
├── neuroimaging_analysis/ # Advanced analysis workflows
├── utils/                 # Utility functions and shared scripts
├── docs/                  # Documentation and usage guides
└── examples/              # Example datasets and workflows
```

## Requirements

To use the scripts in this repository, ensure you have the following:

- **Python** (version 3.10)
- Recommended neuroimaging libraries:
  - [Numpy](https://numpy.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [NiBabel](https://nipy.org/nibabel/)
  - [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/)
  - [SPM](https://www.fil.ion.ucl.ac.uk/spm/)
  - [AFNI](https://afni.nimh.nih.gov/)

Refer to the `requirements.txt` file for a complete list of dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SANSCOG-MRI-Pipeline.git
   cd SANSCOG-MRI-Pipeline
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure all external tools (e.g., FSL, SPM) are correctly installed and accessible in your system's PATH.

## Documentation

Detailed usage instructions, parameter descriptions, and workflow guides are available in the `docs/` directory.

## Contributing

Contributions to this repository are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The development of this pipeline was supported by the SANSCOG research team and collaborators in neuroimaging science. Tools and libraries such as FSL, NiBabel, and SPM have been instrumental in this project.
