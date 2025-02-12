# Weather App using Flask, OpenWeather, and Unsplash APIs

A web application to display the current weather of a city along with a relevant background image. This project utilizes Flask for the web framework, OpenWeather API for weather data, and Unsplash API for fetching related images.

- **Last Updated:** 2025-02-12 15:00:29 UTC
- **Developed By:** gkarthik29

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Screenshot 2025-02-12 204029](https://github.com/user-attachments/assets/9fdbeaae-8ad6-4074-930f-c2f7a4e0b11f)


## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Code Overview](#code-overview)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Features

*   **Real-time Weather Data:** Fetches current weather information from the OpenWeather API, including temperature, humidity, pressure, and weather description.
*   **Dynamic Background Images:**  Retrieves relevant background images from the Unsplash API based on the city name.
*   **User-Friendly Interface:**  Provides a simple and intuitive web interface using Flask.
*   **Error Handling:** Gracefully handles API errors and provides informative messages to the user.
*   **Default Images:** Includes fallback images for common weather conditions if Unsplash API fails or returns no results.

## Demo

[Unfortunately, a live demo cannot be provided directly in a README.  However, you can easily run the application locally following the instructions below.]

**Screenshots**

(Include screenshots of the application in different states, such as showing weather for a sunny day and a rainy day.  This significantly enhances the README.)

## Requirements

### Hardware

*   A computer with internet access

### Software

*   [Python](https://www.python.org/downloads/) 3.6 or higher
*   Python Libraries:
    *   [Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)
    *   [Requests](https://requests.readthedocs.io/en/latest/)

## Setup

1.  **Clone the Repository:**

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    (Create a requirements.txt file with `flask` and `requests` inside.)

3.  **Obtain API Keys:**

    *   Sign up for a free account at [OpenWeather](https://home.openweathermap.org/users/sign_up) to get an API key.
    *   Sign up for a free account at [Unsplash](https://unsplash.com/developers) to get an API key.

4.  **Set Environment Variables:**

    You **MUST** set the `OPENWEATHER_API_KEY` and `UNSPLASH_API_KEY` environment variables.  This is crucial for security and prevents your API keys from being exposed in the code.

    **Option 1: Using `.env` file (Recommended)**

    *   Create a file named `.env` in the root directory of the project.
    *   Add the following lines to the `.env` file, replacing `<YOUR_OPENWEATHER_API_KEY>` and `<YOUR_UNSPLASH_API_KEY>` with your actual keys:

        ```
        OPENWEATHER_API_KEY=<YOUR_OPENWEATHER_API_KEY>
        UNSPLASH_API_KEY=<YOUR_UNSPLASH_API_KEY>
        ```

    *   Install the `python-dotenv` library: `pip install python-dotenv`
    *   Import `load_dotenv` at the top of your `app.py` file and call it:

        ```python
        from dotenv import load_dotenv
        load_dotenv()
        ```
        Then access the keys using `os.environ.get("OPENWEATHER_API_KEY")`

    **Option 2: Setting Environment Variables Directly (Less Secure)**

    *   **Linux/macOS:**

        ```bash
        export OPENWEATHER_API_KEY=<YOUR_OPENWEATHER_API_KEY>
        export UNSPLASH_API_KEY=<YOUR_UNSPLASH_API_KEY>
        ```

    *   **Windows:**

        ```bash
        set OPENWEATHER_API_KEY=<YOUR_OPENWEATHER_API_KEY>
        set UNSPLASH_API_KEY=<YOUR_UNSPLASH_API_KEY>
        ```

        (Remember to set these variables in each new terminal session or add them to your system environment variables.)

5.  **Run the Application:**

    ```bash
    python app.py
    ```

## Usage

1.  Open your web browser and go to `http://127.0.0.1:5000/` or the address displayed in your terminal after running `app.py`.
2.  Enter the name of a city in the input field.
3.  Click the "Get Weather" button.
4.  The application will display the current weather information for the city along with a relevant background image.

## Configuration

The following configurations can be adjusted:

*   **`DEFAULT_IMAGES` Dictionary:**  Modify the `DEFAULT_IMAGES` dictionary in `app.py` to change the fallback images for different weather conditions.  Ensure the paths are correct relative to your `static` directory.
*   **API Keys:**  Ensure the API keys are correctly set as environment variables.
*   **Port:**  By default, the Flask application runs on port 5000.  You can change this by modifying the `app.run()` call in `app.py`:

    ```python
    if __name__ == '__main__':
        app.run(debug=True, port=8000)  # Example: Run on port 8000
    ```

## Code Overview

*   **`app.py`:** Contains the main Flask application logic.
    *   **`weather()` Function:** Handles the routing, form submission, API calls, data processing, and template rendering.
    *   **API Calls:** Uses the `urllib.request` and `requests` libraries to fetch data from the OpenWeather and Unsplash APIs, respectively.
    *   **Template Rendering:**  Renders the `index1.html` template with the weather data and image URL.
    *   **Error Handling:** Includes `try...except` blocks to catch potential errors during API calls.
*   **`index1.html`:** (Provide this file in your repository) The HTML template for the web page.  It displays the weather information and the background image.
*   **`static/` directory:** Contains static files such as images (e.g., `img.jpg`, `sunny.jpg`, `cloudy.jpg`, etc.) and CSS files (if any).

Key Code Segments:

*   **API Call to OpenWeather:**

    ```python
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}'
    ```

*   **API Call to Unsplash:**

    ```python
    unsplash_url = f"https://api.unsplash.com/search/photos?query={city}"
    ```

*   **Rendering the Template:**

    ```python
    return render_template('index1.html', data=weather_data, image_url=image_url)
    ```

## File Structure
WeatherApp/ ├── app.py 

Main Flask application file ├── templates/ │ └── index1.html 
HTML template for the web page ├── static/ │ ├── img.jpg 
Default image │ ├── sunny.jpg 
Default image for sunny weather │ ├── cloudy.jpg 
Default image for cloudy weather │ ├── rain.jpg
Default image for rainy weather │ └── ... 
Other static files (CSS, JavaScript, etc.) ├── .env 
Stores API keys (not committed to repository) ├── README.md 
This file └── requirements.txt
List of Python dependencies

## Contributing

Contributions are welcome!  Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  (Create a LICENSE file in your repository with the MIT License text.)

## Troubleshooting

*   **API Key Errors:**
    *   Ensure that you have obtained valid API keys from OpenWeather and Unsplash.
    *   Double-check that the environment variables `OPENWEATHER_API_KEY` and `UNSPLASH_API_KEY` are set correctly in your `.env` file or environment.
    *   Verify that you are using the correct API key names in your code (e.g., `os.environ.get("OPENWEATHER_API_KEY")`).

*   **City Not Found:**
    *   Make sure that you are entering a valid city name.
    *   Check the OpenWeather API documentation for supported city names.

*   **Image Not Loading:**
    *   Verify that your Unsplash API key is valid and has sufficient usage quota.
    *   Check the Unsplash API response for errors.
    *   Ensure that the `static` directory contains the necessary default images.
    *   Inspect the browser's developer console for any errors related to image loading.

*   **Application Not Running:**
    *   Make sure that you have installed all the required dependencies using `pip install -r requirements.txt`.
    *   Check the terminal output for any error messages.
    *   Ensure that Flask is installed correctly.

*   **`.env` file not working:**
    * Make sure you installed `python-dotenv` and have `load_dotenv()` at the top of your `app.py` file.
    * Double check your `.env` file is in the correct location (root of the project).
    * Ensure your `.env` file is named `.env` and not `.env.txt` or something similar.

## Credits

*   [OpenWeather API](https://openweathermap.org/) for providing weather data.
*   [Unsplash API](https://unsplash.com/) for providing images.
*   [Flask](https://flask.palletsprojects.com/) for the web framework.
*   [Requests](https://requests.readthedocs.io/en/latest/) for making HTTP requests.

## Author

*   **gkarthik29** - [https://github.com/gkarthik29](https://github.com/gkarthik29)  (Replace with your actual GitHub profile URL)

## Last Updated

*   2025-02-12 15:03:55 UTC

---

This is a complete README file for your weather application repository. Remember to replace the placeholder values (e.g., `<your_repository_url>`, `<YOUR_OPENWEATHER_API_KEY>`, `<YOUR_UNSPLASH_API_KEY>`) with your actual values. Also, create the `requirements.txt`, `LICENSE`, and `index1.html` files and populate them with the appropriate content. Finally, add screenshots to make the README more visually appealing.  Remember to create a `.env` file to store your API Keys.  **Do not commit the `.env` file to your repository.**  Add `.env` to your `.gitignore` file to prevent it from being committed.
