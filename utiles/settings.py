import os
import json

settings_filepath = "utiles/properties.json"
default_settings = {
    "language": "eng"
}


def check_settings_file() -> bool:
    try:
        file_path = settings_filepath
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump(default_settings, file, indent=4)
            print(f'{file_path} created.')
            return True
        else:
            return True
    except Exception as e:
        print(
            f"there is an exception while trying to open or create settings.json file:\nThe exception details:{e}")
        return False


class AppSettings:
    """save and load application settings"""

    def __init__(self):
        self.settings_status = check_settings_file()
        self.all_settings = self.get_settings()

    def get_settings(self):
        if self.settings_status:
            with open(settings_filepath, 'r') as file:
                return json.load(file)

    def get_property(self, property_name) -> str:
        return self.all_settings[property_name]

    def set_property(self, property_name, property_value):
        self.all_settings[property_name] = property_value
        with open(settings_filepath, 'w') as file:
            json.dump(self.all_settings, file, indent=4)


# settings = AppSettings()
# print(settings.get_property('language'))
