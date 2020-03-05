masking = [\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)(([0-9a-f]{2,}:){3,}([0-9a-f]{2,}))((?=[^A-Za-z0-9])|$)",  'mask_with': "ID"},\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})((?=[^A-Za-z0-9])|$)",  'mask_with': "IP"},\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)([0-9a-f]{6,} ?){3,}((?=[^A-Za-z0-9])|$)", 'mask_with': "SEQ"},\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)([0-9A-F]{4} ?){4,}((?=[^A-Za-z0-9])|$)", 'mask_with': "SEQ"},\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)(0x[a-f0-9A-F]+)((?=[^A-Za-z0-9])|$)", 'mask_with': "HEX"},\
    {'regex_pattern':"((?<=[^A-Za-z0-9])|^)([\-\+]?\d+)((?=[^A-Za-z0-9])|$)", 'mask_with': "NUM"},\
    {'regex_pattern':"(?<=executed cmd )(\".+?\")", 'mask_with': "CMD"}\
]