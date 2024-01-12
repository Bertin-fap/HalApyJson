__all__ = ['hal_query',]

def hal_query(year):

    #https://realpython.com/python-requests/#getting-started-with-requests
    
    # Standard library imports
    import requests
    import json as json
    from pathlib import Path
    from requests.exceptions import Timeout
    
    from HalApyJson.json_parser import parse_json
   
    # Setting hal API
    hal_api = _set_hal_api_(year)
    
    # Get the request response
    try:
        response = requests.get(hal_api, timeout = 5)
    except Timeout:
        print('The request timed out')
    else:
        if response == False: # response.status_code <200 or > 400
            print('Resource not found')
        else:
            print('Resquest successful\n')
            
            if response.status_code == 204:
                print('No content')
            else:            
                results_df = parse_json (response)
            
    return results_df   

    
def _set_hal_api_(year):
    
    from string import Template
    
    from HalApyJson.GLOBALS import GLOBAL

    
    dict_param_quaery = dict( 
                             query_header = GLOBAL['HAL_URL'] + GLOBAL['HAL_GATE'] + '/?q=', 
                             query = GLOBAL['QUERY_TERMS'],
                             HAL_RESULTS_NB     = GLOBAL['HAL_RESULTS_NB'] ,  # default=30; maximum= 10000
                             HAL_RESULTS_FORMAT = GLOBAL['HAL_RESULTS_FORMAT'],
                             period = "[" + year + " TO " + year + "]",
                             struct_name = GLOBAL['INSTITUTE'].upper(),
                             DOC_TYPES = GLOBAL['DOC_TYPES'],
                             results_fields = ','.join(GLOBAL['HAL_FIELDS'].values()),
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
    
    hal_api = query.safe_substitute(dict_param_quaery)
    return hal_api