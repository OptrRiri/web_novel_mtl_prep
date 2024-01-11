metadata_headers = [
    "meta_attribute", 
    "meta_value_raw", 
    "meta_value_tl"
]

honbun_headers = [
    "honbun_speaker", 
    "honbun_raw", 
    "honbun_tl"
]

preface_headers = [
    "preface_raw", 
    "preface_tl"
]

afterword_headers = [
    "afterword_raw", 
    "afterword_tl"
]

headers = []
for header_set in [
    metadata_headers, 
    honbun_headers, 
    preface_headers, 
    afterword_headers
]:
    headers = headers +header_set + [None]

headers = headers[:-1] if headers[-1] == None else headers