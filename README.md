# Space-Mission-API :rocket:

![Python 3.9.6](https://img.shields.io/badge/python-3.9.6-blue.svg)

Rest-API for Space missions since 1957

## Table of Contents

  - [Motivation](#motivation)
  - [About the Project](#about-the-project)
    - [Features](#features)
    - [Build with](#build-with)
    - [Coming soon](#coming-soon)
  - [Usage](#usage)
    - [Getting Started](#getting-started)
  - [Acknowledgements](#acknowledgements)

## Motivation

Who does not love Rockets?

This project was intended to get into Flask and to develop my skills in the field of data analysis with Pandas.

## About the Project

### Features

* Requests about:
    * Missiondetails:
    * Date
    * Location

* Return JSON-objects like:
    ```json
    [
        {
            "Organisation": "SpaceX",
            "Mission": "Starlink V1 L9 & BlackSky",
            "Mission Status": "Success",
            "Carrierrocket": "Falcon 9 Block 5",
            "Rocket Status": "StatusActive",
            "Costs": "50.0",
            "Date": "2020-08-07",
            "Time": "05:12:00",
            "Launch Location": [
                "LC-39A",
                "Kennedy Space Center",
                "Florida",
                "USA"
            ]
        },
        {
            "Organisation": "CASC",
            "Mission": "Gaofen-9 04 & Q-SAT",
            "Mission Status": "Success",
            "Carrierrocket": "Long March 2D",
            "Rocket Status": "StatusActive",
            "Costs": "29.75",
            "Date": "2020-08-06",
            "Time": "04:01:00",
            "Launch Location": [
                "Site 9401 (SLS-2)",
                "Jiuquan Satellite Launch Center",
                "China"
            ]
        },
        {
            "Organisation": "SpaceX",
            "Mission": "150 Meter Hop",
            "Mission Status": "Success",
            "Carrierrocket": "Starship Prototype",
            "Rocket Status": "StatusActive",
            "Costs": "0",
            "Date": "2020-08-04",
            "Time": "23:57:00",
            "Launch Location": [
                "Pad A",
                "Boca Chica",
                "Texas",
                "USA"
            ]
        }
    ]       
    ```

### Build with

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Pandas](https://pandas.pydata.org/)
* [Gunicorn](https://gunicorn.org/)

### Coming soon

* Nested Queries

## Usage

### Getting Started

* Get all Space missions from *1957* to *2020*:
    ```url
    https://space-mission-api.herokuapp.com/
    ```
* **Missiondetails:**

    * Get missions by organisationname *NASA*:
    ```url
        https://space-mission-api.herokuapp.com/missions?organisation=NASA
    ```
    * Get mission by missionname *Apollo 11*:
    ```url
        https://space-mission-api.herokuapp.com/missions?mission=Apollo%2011
    ```
    * Get missions by mission status *Success*:
    ```url
        https://space-mission-api.herokuapp.com/missions?missionsatus=Success
    ```
    * Get missions by rocketname *Saturn V*:
    ```url
        https://space-mission-api.herokuapp.com/missions?rocket=Saturn%20V
    ```
    * Get missions by rocket status *active*:
    ```url
        https://space-mission-api.herokuapp.com/missions?rocketstatus=StatusActive
    ```
    * Get missions with costs more than *100 million $*:
    ```url
        https://space-mission-api.herokuapp.com/missions/costs?more=100.0
    ```
    * Get missions with *unknown costs*:
    ```url
        https://space-mission-api.herokuapp.com/missions/costs?less=1.0
    ```
    * Get missions with costs less than *100 million $*:
    ```url
        https://space-mission-api.herokuapp.com/missions/costs?less=100.0
    ```

* **Date:**


    * Get mission by date *2020-08-07*:
    ```url
        https://space-mission-api.herokuapp.com/date?date=2020-08-07
    ```
    * Get missions by year *1969*:
    ```url
        https://space-mission-api.herokuapp.com/date?year=1969
    ```
    * Get missions since year *2019*:
    ```url
        https://space-mission-api.herokuapp.com/date?from=2019
    ```
    * Get missions to year *1958*:
    ```url
        https://space-mission-api.herokuapp.com/date?to=1958
    ```
    * Get missions from *2018* to *2019*:
    ```url
        https://space-mission-api.herokuapp.com/date/2018/2019
    ```

* **Location:**

    * Get missions by Spacecenter *Kennedy Space Center*:
    ```url
        https://space-mission-api.herokuapp.com/location?spacecenter=Kennedy%20Space%20Center
    ```
    * Get missions by Country *USA*:
    ```url
        https://space-mission-api.herokuapp.com/location?country=USA
    ```
## Acknowledgements

* [Kaggle dataset](https://www.kaggle.com/agirlcoding/all-space-missions-from-1957)
