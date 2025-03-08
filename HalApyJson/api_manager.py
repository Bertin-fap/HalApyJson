"""Module of functions for getting response from HAL API."""

__all__ = ['get_response_from_api',]

# Standard library imports
from string import Template

# 3rd party imports
import requests
from requests.exceptions import Timeout

# Internal library imports
from HalApyJson.haj_globals import GLOBAL


def get_response_from_api(year, institute):
    """The `get_response_from_api` function gets the response to the query sent to the HAL API.

    Args:
        year (str): The year to query.
        institute (str): The institute to query.
    Returns:
        (requests.models.Response): The response to the query using the HAL API.
    Note:
        Inspired from: https://realpython.com/python-requests/#getting-started-with-requests.
    """
    # Setting hal API
    hal_api = _set_hal_api(year, institute)

    # Get the request response
    response = False
    try:
        response = requests.get(hal_api, timeout=5)
    except Timeout:
        message = "The request timed out"
    else:
        if not response: # response.status_code <200 or > 400
            message = "Resource not found"
        else:
            if response.status_code==204:
                message = "No content in response"
            else:
                message = "Response available"
    return response, message


def _set_hal_api(year, institute):
    """The `_set_hal_api` function builds the query to send to the HAL API.

    Args:
        year (str): The year to query.
        institute (str): The institute to query.
    Returns:
        (str): The built query.
    """
    # HAL_RESULTS_NB: default=30; maximum= 10000
    dict_param_query = dict(
                             query_header       = GLOBAL['HAL_URL'] + GLOBAL['HAL_GATE'] + '/?q=',
                             query              = GLOBAL['QUERY_TERMS'],
                             HAL_RESULTS_NB     = GLOBAL['HAL_RESULTS_NB'],
                             HAL_RESULTS_FORMAT = GLOBAL['HAL_RESULTS_FORMAT'],
                             period             = f"[{str(year)} TO {str(year)}]",
                             struct_name        = institute.upper(),
                             DOC_TYPES          = GLOBAL['DOC_TYPES'],
                             results_fields     = ','.join(GLOBAL['HAL_FIELDS'].values()),
                            )

    query = Template(
                    ("$query_header"
                     "$query "
                     "&rows=$HAL_RESULTS_NB"
                     "&wt=$HAL_RESULTS_FORMAT" 
                     "&fq=producedDateY_i:$period"
                     "&fq=structAcronym_s:$struct_name"
                     "&fq=docType_s:$DOC_TYPES"
                     "&fl=$results_fields"
                     "&indent=true")
                    )

    hal_api = query.safe_substitute(dict_param_query)
    return hal_api
