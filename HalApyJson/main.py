__all__ = ['build_hal_df_from_api',]

def build_hal_df_from_api(year, institute):
    '''The `hal_query` function queryies the HAL database via its api.
        
    Args:
        year (str): the yera to query.
        institute (str) : the institute to query
    
    Returns
        (Pandas data frame) : The parsed json answer to the query.
        
    '''
    
    from HalApyJson.api_manager import get_response_from_api
    from HalApyJson.json_parser import parse_json
    
    response = get_response_from_api(year, institute)         
    hal_df = parse_json(response)
    return hal_df