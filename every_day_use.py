#parse string to generator with selected delimeter 

def parse_str(str_:str, delim:str):
    return (f for f in str_.split(delim) if f)
