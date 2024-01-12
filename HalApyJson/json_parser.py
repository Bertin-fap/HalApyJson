__all__ = ['parse_json',]

def parse_json (response):
    
    # 3rd party import
    import pandas as pd
    
    from HalApyJson.GLOBALS import GLOBAL
    
    def _get_field_value(txt, field_key):
        try:
            field_value = txt[GLOBAL['HAL_FIELDS'][field_key]]
        except KeyError:
            field_value= 'NA'                
        return field_value

    # Initializing results_df
    fields_keys_select = GLOBAL['HAL_FIELDS'].keys() #FIELDS_KEYS_SELECT
   
    parsed_response = response.json()
    parsed_response = parsed_response['response']
    items_nbr = parsed_response['numFound']
    print('Number of items: ',items_nbr)
    
    results_df = pd.DataFrame(columns = fields_keys_select)
    for txt in parsed_response['docs']:
        num_df = pd.DataFrame(columns = fields_keys_select)
        num_results_dict = {}
        for k in fields_keys_select: 
            field_value = _get_field_value(txt, k)
            num_results_dict[k] = [field_value]  
        num_df = pd.DataFrame.from_dict(num_results_dict, orient = 'columns')
        results_df = pd.concat([results_df, num_df], ignore_index = True)
    results_df.rename(columns = GLOBAL['HAL_FINAL_COLS'], inplace = True)

    return results_df