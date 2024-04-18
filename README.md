# Project Title

## Description
This project is designed to handle database operations, image preprocessing, and license plate recognition. It integrates various modules for establishing database connections, handling CRUD operations, processing images, and recognizing license plates through video capture.

## Modules
- `DB_connect.py`: Module to establish database connections.
- `DB_CRUD.py`: Provides CRUD (Create, Read, Update, Delete) operations for the database.
- `db_helper.py`: Helper functions for database operations.
- `video_capture.py`: Captures video for processing.
- `videoRouts.py`: Flask routes for handling video processing tasks.
- `search_plate_history_route.py`: Flask route for querying historical data of recognized plates.
- `crud_db_routes.py`: Flask routes for database operations via web API.
- `main.py`: The main entry point of the application.
- `preprocess_image.py`: Prepares images for recognition processes.
- `lpr.py`: License Plate Recognition module.
- `find_candidates.py`: Finds potential license plate candidates in images.

## Installation
To get started with this project, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
```

## Requirements
Ensure the following packages are installed, as specified in the `requirements.txt`:
- Flask
- OpenCV
- EasyOCR
- NumPy
- MongoDB
- Others as listed in the provided `requirements.txt`.

## Usage
Run the main application with:

```bash
python main.py
```

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
