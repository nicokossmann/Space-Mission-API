# Space-Mission-API :rocket:

![Github License](https://img.shields.io/badge/license-MIT-green)

Rest-API for Space missions since 1957

## Table of Contents

* [Motivation](#motivation)
* [About the Project](#about-the-project)
    * [Features](#features)
    * [Build with](#build-with)
    * [Coming soon](#coming-soon)
* [Usage](#usage)
    * [**Getting Started**](#getting-started)
    * [Clone](#clone)
* [Lisense](#coming-soon)

## Motivation

Who does not love Rockets?

This project was intended to get into Flask and to develop my skills in the field of data analysis with Pandas.

## About the Project

### Features

* Requests about:
    * Missiondetails:
    * Dates
    * Locations

* Response JSON-objects like:
```json
    [
        {
            "Organisation": "US Navy",
            "Mission": "Vanguard TV3",
            "Mission Status": "Failure",
            "Carrierrocket": "Vanguard",
            "Rocket Status": "StatusRetired",
            "Costs": "nan",
            "Date": "1957-12-06T00:00:00.000Z",
            "Time": "16:44:00",
            "Launch Location": [
                "LC-18A",
                "Cape Canaveral AFS",
                "Florida",
                "USA"
            ]
        },
        {
            "Organisation": "RVSN USSR",
            "Mission": "Sputnik-2",
            "Mission Status": "Success",
            "Carrierrocket": "Sputnik 8K71PS",
            "Rocket Status": "StatusRetired",
            "Costs": "nan",
            "Date": "1957-11-03T00:00:00.000Z",
            "Time": "02:30:00",
            "Launch Location": [
                "Site 1/5",
                "Baikonur Cosmodrome",
                "Kazakhstan"
            ]
        },
        {
            "Organisation": "RVSN USSR",
            "Mission": "Sputnik-1",
            "Mission Status": "Success",
            "Carrierrocket": "Sputnik 8K71PS",
            "Rocket Status": "StatusRetired",
            "Costs": "nan",
            "Date": "1957-10-04T00:00:00.000Z",
            "Time": "19:28:00",
            "Launch Location": [
                "Site 1/5",
                "Baikonur Cosmodrome",
                "Kazakhstan"
            ]
        }
    ]
```

### Build with

* Flask
* Pandas
* Gunicorn

### Coming soon

* Nested Queries

## Usage

### Get started

* Get all Space missions from 1957 to 2020:
```console
    https://space-mission-api.herokuapp.com/
```
* Missiondetails:

    * Get missions by organisationname:
    ```console
        https://space-mission-api.herokuapp.com/mission?organisation=NASA
    ```
    * Get mission by missionname:
    ```console
        https://space-mission-api.herokuapp.com/mission?mission=Apollo%2011
    ```
    * Get missions by mission status:
    ```console
        https://space-mission-api.herokuapp.com/mission?missionsatus=Success
    ```
    * Get missions by rocketname:
    ```console
        https://space-mission-api.herokuapp.com/mission?rocket=Saturn%20V
    ```
    * Get missions by rocket status:
    ```console
        https://space-mission-api.herokuapp.com/mission?rocket=StatusRetired
    ```

* Missioncosts:
* Date:

    * Get mission by date:
    ```console
        https://space-mission-api.herokuapp.com/date?date=2020-08-07
    ```
    * Get missions by year:
    ```console
        https://space-mission-api.herokuapp.com/date?year=1969
    ```
    * Get missions since year:
    ```console
        https://space-mission-api.herokuapp.com/date?from=2019
    ```
    * Get missions to year:
    ```console
        https://space-mission-api.herokuapp.com/date?to=1958
    ```
    * Get missions between years:
    ```console
        https://space-mission-api.herokuapp.com/date/2018/2019
    ```

### Clone

## Lisense

This project is licensed under the [MIT License](https://github.com/this/project/blob/master/LICENSE)

## Acknowledgements

* [Link to Kaggle dataset](https://www.kaggle.com/agirlcoding/all-space-missions-from-1957)