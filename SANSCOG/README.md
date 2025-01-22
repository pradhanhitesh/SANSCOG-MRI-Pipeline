# Overview

## DICOMCrawler
`DICOMCrawler` is a Python tool designed to crawl directories for DICOM files, extract metadata, and save structured information into CSV files. It supports processing multiple directories based on modality templates defined in a JSON file.

### Features
- Crawls directories to find DICOM files.
- Verifies if files are valid DICOM files.
- Extracts metadata such as study date, acquisition time, patient ID, sex, and age.
- Saves results into a `modal_data.csv` file for each directory.
- Handles multiple directories and templates for different modalities.

### Requirements
- Python 3.10
- Libraries:
  - `json`
  - `glob`
  - `os`
  - `magic`
  - `pandas`
  - `pydicom`

To install missing libraries, use:
```bash
pip install pandas pydicom python-magic
```
### Initialize the Crawler
```python
from dicom_crawler import DICOMCrawler

# Initialize with paths and JSON template
crawler = DICOMCrawler([
    "path/to/dicom/directory1",
    "path/to/dicom/directory2"
], json_path="utils/modal-templates.json")
```

### Start Crawling
```python
# Start crawling and processing files
crawler.crawl()
```

### Output
- The results for each directory will be saved as `modal_data.csv` in the respective directory.

### JSON Template Example
The JSON file defines modality templates:
```json
{
  "CT": ["CT", "ComputedTomography"],
  "MRI": ["MR", "MagneticResonance"]
}
```
This specifies the tags or identifiers used to recognize modalities in the directories.

### Example Script
```python
from dicom_crawler import DICOMCrawler

# Initialize the crawler
paths = ["/path/to/dir1", "/path/to/dir2"]
json_path = "utils/modal-templates.json"
crawler = DICOMCrawler(paths, json_path)

# Crawl the directories
crawler.crawl()
```

### Advanced Usage: Adding Concurrency
If processing multiple directories, you can speed up the crawl using concurrency:

### Example with ThreadPoolExecutor
```python
from concurrent.futures import ThreadPoolExecutor
from dicom_crawler import DICOMCrawler

def crawl_path(path):
    crawler = DICOMCrawler([path], json_path="utils/modal-templates.json")
    crawler.crawl()

paths = ["/path/to/dir1", "/path/to/dir2"]
with ThreadPoolExecutor() as executor:
    executor.map(crawl_path, paths)
```

### Notes
- Ensure the `modal-templates.json` file is correctly formatted and placed in the specified path.
- For large directories, consider using faster storage like SSDs for optimal performance.

