# Atlas
Atlas is a open source IT asset manager that allows you to organize and structure all your assets.

## Installation
Follow these steps to get started with this application:
- Checkout this repository and place it in your workspace
- Create a virtualenv with python 3 `virtualenv -p python3 atlas`
- Activate your virtualenv `/[ENVPATH]/atlas/bin/activate` 
- In your project root install the required packages `pip install -r requirements.txt`
- You are ready to go!

## Apps
These are the apps that are used in this project:
- `Asset`
- `Info`
- `Location`
- `Person`

## Models
Each app contains multiple models.

### Asset
- `Asset(Model)`
- `Hardware(Asset)`
- `Software(Asset)`

### Info
- `Update(Model)`
- `Notifications(Model)`

### Location
- `Location(Model)`
- `Section(Model)`

### Person
- `Person(User)`
- `Category(Model)`

## Commands
There is a custom command that can runs with a cronjob to check if there are any assets that will expire soon.
This command checks for assets that will expire in the upcoming month and will send an email to the admin email that is set in the `settings.py` file.

- `python manage.py checkexpiredassets`

## Language support
The django translation module is used in this project for translation. The project currently supports:
- English
- Dutch

## License
This project is published under the MIT License
