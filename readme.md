# File Transfer Utility

## Description

This project is a lightweight file upload and download service built using a RESTful API. It provides a simple and reliable way to transfer files between clients and a server over HTTP. The system is designed with correctness and robustness in mind, ensuring safe file writes, predictable behavior during retries, and integrity verification.

In addition to API access, a minimal web interface is provided for manual file uploads and downloads, making the service easy to use for both automated tools and human users.

## Features

- REST API for file upload and download

- Atomic file writes to prevent partial or corrupted files

- Safe filename handling to avoid path traversal issues

- Checksum generation for uploaded files to verify integrity

- Overwrite-safe uploads for retry-friendly behavior

- Single, configurable storage directory on the server

- Minimal HTML interface for browser-based interaction

- Compatible with command-line tools (e.g., curl) and web clients

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-transfer-utility.git
2. Navigate to the project directory:
    ```bash
    cd file-transfer-utility
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
## Run
    python main.py

### Upload:
    
    curl -X POST -F "file=@./test.txt" http://127.0.0.1:5000/file_manager/upload

### Download:
    curl -O http://localhost:5000/file_manager/download/model_inceptionV3.h5


## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
3. Commit your changes:
    ```bash
    git commit -m "Add feature"
4. Push to the branch:
    ```bash
    git push origin feature-name
5. Open a pull request.
