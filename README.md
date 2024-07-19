
A Python-based weather application that provides real-time weather updates for a specified city. This script fetches weather data using the WeatherAPI and provides spoken updates using platform-specific text-to-speech solutions.

## Features

- Provides current weather conditions including temperature, wind speed, humidity, and more.
- Uses text-to-speech for spoken updates:
  - `say` command for macOS
  - `pyttsx3` for Windows

## Requirements

- Python 3.x
- `requests` library
- `pyttsx3` library (for Windows)

## Installation

1. **Clone the repository** or download the script.
2. **Install the required libraries** using pip:

   ```bash
   pip install requests
   pip install pyttsx3  # Only for Windows
   ```

## Usage

### On macOS

1. Ensure you have Python 3.x installed.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script:

   ```bash
   python weather_app.py
   ```

4. Follow the on-screen prompts to enter the name of your city or press 'Q' to quit.

### On Windows

1. Ensure you have Python 3.x installed.
2. Open a Command Prompt or PowerShell and navigate to the directory containing the script.
3. Run the script:

   ```bash
   python weather_app.py
   ```

4. Follow the on-screen prompts to enter the name of your city or press 'Q' to quit.

## Script Details

- The script prompts for a city name or allows the user to press 'Q' to quit.
- For macOS, it uses the `say` command to provide spoken updates.
- For Windows, it uses the `pyttsx3` library for text-to-speech.
- If the city name is invalid or an error occurs, the script will notify you and allow you to try again.

## Example Output

```
Welcome to the Digital Weather Application. Created By CodeWithSalty on Instagram also known as Salmaan. If you want to know the current condition of your city, kindly put the name of your city here or press Q to Exit The Application.
Enter the name of your city or press Q to quit -----> : 
The current weather of New York is 22 degrees Celsius or 72 degrees Fahrenheit. 
The condition is Clear and last updated on 2024-07-19 12:00 PM. 
Wind speed is 15 kilometers per hour or 9 miles per hour from the NW direction. 
Pressure is 1013 millibars or 29.91 inches. 
Precipitation is 0 millimeters or 0 inches. 
Humidity is 60 percent. 
Cloud cover is 5 percent. 
It feels like 22 degrees Celsius or 72 degrees Fahrenheit.
Visibility is 10 kilometers or 6 miles. 
UV index is 5. 
Wind gusts are 20 kilometers per hour or 12 miles per hour.
```

## Troubleshooting

- Ensure that you have a valid API key from WeatherAPI. Replace `"YOUR API KEY !!! "` in the script with your actual API key.
- For text-to-speech issues on macOS, ensure the `say` command is available.
- For Windows, make sure `pyttsx3` is correctly installed and functioning.

## License

This project is free to use just give me the credits (:  

## Contact

For any questions or issues, please contact [CodeWithSalty](https://instagram.com/CodeWithSalty).

---
