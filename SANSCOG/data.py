import json
import glob
import os
import magic
import pandas as pd
from pydicom import dcmread
import pydicom.dataelem

class DICOMCrawler:
    """
    A class to crawl directories for DICOM files, process them, and save structured data.

    Attributes:
    - paths (list): List of directory paths to crawl.
    - json_path (str): Path to the JSON file containing modality templates.

    Example:
    >>> crawler = DICOMCrawler(["path/to/dicom/files"], "utils/modal-templates.json")
    >>> crawler.crawl()
    """

    def __init__(self, paths, json_path='utils/modal-templates.json'):
        """
        Initialize the DICOMCrawler instance.

        Args:
        - paths (str | list): A single path or a list of paths to crawl for DICOM files.
        - json_path (str): Path to the JSON file containing modality templates. Defaults to 'utils/modal-templates.json'.
        """
        self.paths = paths if isinstance(paths, list) else [paths]
        self.json_path = json_path

    def _read_json(self):
        """
        Read and parse the JSON file containing modality templates.

        Returns:
        - dict: Parsed JSON data.

        Raises:
        - ValueError: If the file is not found, contains invalid JSON, or another error occurs.
        """
        try:
            with open(self.json_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"File not found: {self.json_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {self.json_path}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {str(e)}")

    def _check_all_dcm(self, path):
        """
        Verify if all files in the specified directory are DICOM files.

        Args:
        - path (str): Directory path to check.

        Returns:
        - bool: True if all files are DICOM files, otherwise False.
        """
        dcm_files = sorted(glob.glob(f"{path}/**"))
        if len(dcm_files) == 0:
            return False

        for dcm_file in dcm_files:
            dcm_type = magic.from_file(dcm_file, mime=True)
            if dcm_type != 'application/dicom':
                return False

        return True

    def _read_dcm(self, path):
        """
        Read a DICOM file and extract its data into a DataFrame.

        Args:
        - path (str): Directory path containing the DICOM file.

        Returns:
        - pd.DataFrame: DataFrame containing extracted DICOM data.
        """
        path = sorted(glob.glob(f"{path}/**"))[0]
        ds = dcmread(path)
        df = pd.DataFrame(ds.values())
        df[0] = df[0].apply(lambda x: pydicom.dataelem.DataElement_from_raw(x) if isinstance(x, pydicom.dataelem.RawDataElement) else x)
        df['name'] = df[0].apply(lambda x: x.name)
        df['value'] = df[0].apply(lambda x: x.value)
        return df[['name', 'value']]

    def crawl(self):
        """
        Crawl the specified directories, process DICOM files, and save results.

        Outputs:
        - Saves a 'modal_data.csv' file in each directory specified in the paths attribute.

        Notes:
        - Directories are processed based on modality templates from the JSON file.
        - DICOM data is extracted, organized, and saved into a CSV file.
        """
        data = self._read_json()

        for path in self.paths:
            subject_data = []
            for key, value in data.items():
                tags = value
                all_files = [
                    x for x in sorted(glob.glob(f"{path}/**", recursive=True))
                    if any(tag in x for tag in tags) and os.path.isdir(x)
                ]
                for file in all_files:
                    if self._check_all_dcm(file):
                        dcm_data = self._read_dcm(file)
                        study_date = dcm_data[dcm_data['name'] == 'Study Date'].values[0]
                        acq_time = dcm_data[dcm_data['name'] == 'Acquisition Time'].values[0]
                        patient_id = dcm_data[dcm_data['name'] == 'Patient ID'].values[0]
                        patient_sex = dcm_data[dcm_data['name'] == "Patient's Sex"].values[0]
                        patient_age = dcm_data[dcm_data['name'] == "Patient's Age"].values[0]

                        subject_data.append([
                            key, file, len(glob.glob(f"{file}/**")), study_date[1], acq_time[1],
                            patient_id[1], patient_sex[1], patient_age[1]
                        ])
                    else:
                        subject_data.append([key, file, len(glob.glob(f"{file}/**")), None, None, None, None, None])

            modal_data = pd.DataFrame(
                subject_data,
                columns=['Modality', 'Path', 'DCM_Count', 'Study Date', 'Acquisition Time', 'Subject_ID', 'Subject_Sex', 'Subject_Age']
            ).sort_values(by='Acquisition Time', na_position='last')

            # Save the DataFrame for the specific path
            output_file = os.path.join(path, 'modal_data.csv')
            modal_data.to_csv(output_file, index=False)
            print(f"Saved modal_data.csv for path: {path}")