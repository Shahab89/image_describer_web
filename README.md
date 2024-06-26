# Intelligent Image Describer 🖼️ ✍️ 🔊

This Streamlit application allows users to upload an image, generate a detailed description, and convert the description to audio. It uses a FastAPI backend to handle image processing, description generation, and text-to-speech conversion.

## Features

- **Image Upload**: Upload an image (jpg, jpeg, png).
- **Description Generation**: Generate a detailed description of the uploaded image.
- **Language Selection**: Choose between English and German for the description.
- **Text-to-Speech**: Convert the description to audio and play it directly in the app.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Shahab89/image_describer_web.git
    ```

2. Navigate to the project directory:
    ```sh
    cd image_describer_web
    ```

3. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server: ( Find the source code in this repo : [image_describer](https://github.com/Shahab89/image_describer.git))
    ```sh
    uvicorn api.fast:app:app --reload
    ```

2. Start the Streamlit application:
    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to view the application.

## Usage

1. **Upload an Image**: Click on the "Choose an image..." button and upload a jpg, jpeg, or png file.
2. **Generate Description**: Select a language (English or German) and click the "Select" button to generate a description of the image.
3. **Generate Audio**: Click the "🔊 Generate Audio" button to convert the description to audio.
4. **Play Audio**: If audio is generated successfully, it will be available for playback directly in the app.

## Code Overview

- **app.py**: The main Streamlit application file.
- **FastAPI Endpoint**:
    - `/upload_image`: Handles image upload and processing.
    - `/description`: Generates a description for the uploaded image based on the selected language.
    - `/speech`: Converts the description to audio.

## Error Handling

- The application checks if the uploaded file is a valid image.
- Appropriate error messages are displayed for invalid file uploads or failed audio generation.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any feature requests or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*This application is developed only for educational purposes and personal hobby.*
