from urllib.parse import parse_qs
def query_to_dict(q):
    return {k:v[0] if len(v)==1 else v for k,v in parse_qs(q).items()}