# Python Projects Repository

Welcome to my OIBSIP (Oasis InfoByte Internship) Projects repository! This repository contains a collection of Python projects developed during my internship. Each project is designed to showcase different aspects of Python programming, including GUI development, data visualization, secure password generation, and API integration.

## Table of Contents
- [Projects Included](#projects-included)
  - [BMI Calculator](#1-bmi-calculator)
  - [Random Password Generator](#2-random-password-generator)
  - [Weather App](#3-weather-app)
- [Setting Up the Environment](#setting-up-the-environment)
- [How to Run Each Project](#how-to-run-each-project)
- [Tools and Technologies](#tools-and-technologies)

## Projects Included

### 1. **BMI Calculator**
   - **Description**: A graphical BMI calculator with a user-friendly interface (GUI) built using Tkinter. Users can input their weight and height (in feet), and the application will calculate their BMI, categorize it, and allow users to visualize their BMI trends over time.
   - **Features**:
     - Calculates BMI and categorizes it (Underweight, Normal weight, Overweight, Obesity).
     - Data storage and visualization of historical BMI data with graphs.
     - Error handling and input validation.
   - **Tools Used**: Tkinter, Matplotlib, JSON.

### 2. **Random Password Generator**
   - **Description**: A Python-based application that generates random passwords with customizable options such as length, inclusion of special characters, numbers, and uppercase/lowercase letters.
   - **Features**:
     - Generates secure, random passwords.
     - Customizable password criteria (length, characters, etc.).
     - Simple and intuitive command-line interface.
   - **Tools Used**: Python Standard Library (`random`, `string`).

### 3. **Weather App**
   - **Description**: A weather forecasting app that provides current, hourly, and daily forecasts using data from a weather API. The application also includes data visualization for easy interpretation of weather trends.
   - **Features**:
     - Retrieves current, hourly, and daily weather forecasts.
     - Visualizes weather data for better understanding.
     - Error handling for network and API issues.
   - **Tools Used**: Python, Requests, Matplotlib.

## Setting Up the Environment
To ensure that each project runs smoothly, it's recommended to create a separate virtual environment for each one. This allows you to manage dependencies effectively and avoid conflicts between different projects.

### Steps to Create a Virtual Environment:
1. **Navigate to the Project Directory**:
   ```bash
   cd project-directory-name
   ```

2. **Create the Virtual Environment**:
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source myenv/bin/activate
     ```

4. **Install Required Libraries**:
   Each project comes with a `requirements.txt` file. You can install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Each Project
After setting up the virtual environment and installing the dependencies, you can run the projects by executing the respective Python scripts:

1. **BMI Calculator**:
   ```bash
   python bmi_calculator.py
   ```
   
2. **Random Password Generator**:
   ```bash
   python password_generator.py
   ```

3. **Weather App**:
   ```bash
   python weather_app.py
   ```

## Tools and Technologies
The projects in this repository utilize various tools and technologies, including:
- **Python**: Core programming language used for development.
- **Tkinter**: For building graphical user interfaces (BMI Calculator).
- **Matplotlib**: For data visualization (BMI Calculator, Weather App).
- **Requests**: For API calls (Weather App).
- **JSON**: For data storage and manipulation (BMI Calculator).
- **VS Code**: The main IDE used for coding, debugging, and project management.

