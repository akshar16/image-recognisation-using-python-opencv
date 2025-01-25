# image-recognisation-using-python-opencv
his Python project demonstrates real-time video analysis using Google's Gemini AI model and OpenCV. It captures video from a webcam or a specified video file, sends frames to the Gemini model for description, and displays the generated text on the video feed in real-time.
# Real-Time Video Analysis with Gemini AI and OpenCV

This Python project demonstrates real-time video analysis by combining Google's Gemini AI model with OpenCV. It processes video from a webcam or file, sends frames to Gemini for description, and overlays the text response onto the video feed.

## Key Features:

*   **Flexible Video Input:** Supports both webcam and video file sources.
*   **Efficient Processing:** Achieves near real-time processing with configurable frame skipping.
*   **AI-Powered Analysis:** Integrates with Gemini AI for image analysis and description generation.
*   **Dynamic Text Overlay:** Displays Gemini's responses directly on the video frame.
*   **Text Handling:** Wraps text to fit the screen and manages display duration.
*   **Concise Codebase:** Utilizes short, readable variables and minimal comments for clarity.
*   **Error Management:** Provides basic error handling for common issues.

## How It Works:

1.  **Capture:** The application grabs video frames from a webcam or video file.
2.  **Process:** Frames are sampled at a configurable rate (`skip`) and encoded to base64 for the Gemini API.
3.  **Analyze:** The base64 image and a descriptive prompt are sent to the Gemini model.
4.  **Display:** Gemini's text response is overlaid onto the video, with line wrapping.
5.  **Control:** The text is displayed for a set duration before disappearing.
6.  **Real-Time Output:** Processed frames are displayed immediately.

## Usage:

1.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate   # On Windows
    ```
2.  **Install dependencies:**
    ```bash
    pip install opencv-python google-generativeai
    ```
3.  **Obtain an API Key:** Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/).
4.  **Configure API Key:** Set the `API_KEY` variable in the script to your obtained key.
5.  **Run the script:**
    ```bash
    python your_script_name.py  # Or python3 your_script_name.py
    ```
6.  **Configuration:**
    *   Adjust `skip`: The number of frames to skip between processing (e.g., `skip=5` will process every 5th frame).
    *   Adjust `max_f`: The maximum number of frames to process (useful for testing).
    *  Adjust `txt_dur`: The duration in seconds the generated text is shown.
    These parameters can be modified in the `proc_vid` function call at the end of the script.
7.  **Change the Model:** You can change the Gemini model using `genai.GenerativeModel(<model_name>)` in the script. The default model is `gemini-2.0-flash-exp`.
8.  **Use Video Files:** To analyze a video file, set `src='file'` and specify the `vid_path` (e.g., `vid_path='path/to/your/video.mp4'`) when calling the `proc_vid` function.
9.  **Exit:** Press the `'q'` key while the window has focus to close the window and stop the script.

## Code Structure:

*   `your_script_name.py`: The main Python script containing all the video processing and Gemini integration logic.

## Important Notes:

*   This project uses the `gemini-2.0-flash-exp` model by default. You can modify the code to use a different model by changing the `genai.GenerativeModel()` call.
*   Remember to replace `"YOUR_API_KEY"` with your actual API key from Google AI Studio.
*   This project requires a valid Google AI API key to access the Google Gemini services.

