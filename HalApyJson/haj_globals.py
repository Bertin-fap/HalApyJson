"""Builds global parameters get from the `hal_config.json` described 
in the config.py module. 
A custom `hal_config.json` is stored in the two following directories:
- ~/AppData/Roaming/HalApyJson that contains the user's `hal_config.json` file.
- .ScopusApyJson/CONFIG that contains the default setting. 
If the user's `hal_config.json` configuration file exits it will be used. 
Otherwise a user's configuration file `hal_config.json` will be created 
in the user's ~/AppData/Roaming directory.
"""

__all__ = ['GLOBAL',]

# Standard library imports
import json
import os.path
import sys
from pathlib import Path


def get_config_dir():
    """Gets a parent directory path where persistent application 
    data can be stored depending on the user's platform.

    The covered platforms and corresponding directories are as follows: 
    - linux: ~/.local/share.
    - macOS: ~/Library/Application Support.
    - windows: C:/Users/<USER>/AppData/Roaming.
    Returns:
        (path): The full path to the targeted parent directory.
    Note:
        Adapted from: ('https://stackoverflow.com/questions/19078969/'
        'python-getting-appdata-folder-in-a-cross-platform-way').
    """
    home = Path.home()

    if sys.platform=='win32':
        app_data_path = home / Path('AppData/Roaming')
    elif sys.platform=='darwin':
        app_data_path = home / Path('Library/Application Support')
    else:
        app_data_path = home / Path('.local/share')
    return app_data_path


def _dump_json(file_path, json_dict):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(json_dict, file, indent=4)


def _config_hal_api(json_file_name):
    # Reads the default json_file_name config file
    pck_config_path = Path(__file__).parent / Path('CONFIG') / Path(json_file_name)
    pck_config_date = os.path.getmtime(pck_config_path)
    with open(pck_config_path, encoding="utf-8") as file:
        json_config_dict = json.load(file)

    # Sets the json_config_dict according to the status of the local config file
    local_config_dir_path = get_config_dir() / Path('HalApyJson')
    local_config_file_path = local_config_dir_path / Path(json_file_name)

    if os.path.exists(local_config_file_path):
        # Local json_file_name config file exists
        local_config_date = os.path.getmtime(local_config_file_path)
        if local_config_date>pck_config_date:
            # Local config file is more recent than package one
            # thus json_config_dict is defined by the local config file
            with open(local_config_file_path, encoding="utf-8") as file:
                json_config_dict = json.load(file)
        else:
            # Local config file is less recent than package one
            # thus package config file overwrite the local config file
            # and json_config_dict is kept at default values
            _dump_json(local_config_file_path, json_config_dict)
    else:
        # Local json_file_name config file does not exist
        # thus package config file is used to create a local config file
        # to be filled by the user
        # and json_config_dict is kept at default values
        if not os.path.exists(get_config_dir() / Path('HalApyJson')):
            os.makedirs(get_config_dir() / Path('HalApyJson'))
        _dump_json(local_config_file_path, json_config_dict)

    return json_config_dict, local_config_file_path

GLOBAL = _config_hal_api('hal_config.json')[0]
