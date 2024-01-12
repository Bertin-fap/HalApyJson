# HalApyJson
## Description
A light interface to query HAL through its API.

## Installation
Run the following to install:
```python
pip install HalApyJson
```

## Usage example
```python
import HalApyJson as ha
year = "2023"
results_df = ha.hal_query(year)
results_df.to_excel(<your_fullpath_file.xlsx), index = False)
```
**for more exemples refer to** [HalApyJson-exemples](https://github.com/Bertin-fap/HalApyJson/Demo_HalApyJson.ipynb).


# Release History
1.0.0 first release


# Meta
	- authors : BiblioAbnalysis team

Distributed under the [MIT license](https://mit-license.org/)