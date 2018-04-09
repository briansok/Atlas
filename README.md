# Atlas
Atlas is a open source Asset manager that allows you to organize and structure all your assets.

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

## License
This project is published under the MIT License
