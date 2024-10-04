{
    'name': 'Point of Sale Hasar CF',
    'version': '17.0.0.2',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Simple Fiscal Control Printer Hasar, Point of Sale ',
    'description': """Simple Fiscal Control Printer Hasar, Point of Sale. 

            This module allows to comunicate and print fiscal documents in Hasar CF250 v2.0, 
            in this early version 'v15.0.3' simple print the complete order ones it is validate and finalized.
            Validate limites on CF. 
            """,
    'depends': ['point_of_sale'],
    'data': [
        #'views/pos_hasarcf_views.xml',
        #'security/ir.model.access.csv',
        ],
    'installable': True,
     'assets': {
         'point_of_sale._assets_pos': [
            'pos_hasarcf/static/src/**/*',
        ],
         'web.assets_backend': [
            'pos_hasarcf/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
}
