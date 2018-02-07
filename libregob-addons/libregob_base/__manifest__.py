# -*- coding: utf-8 -*-
##############################################################################
# Los módulos de libregob están disponibles bajo la licencia A-GPLv3.
# La licencia de los módulos de terceros usados por el proyecto deben ser
# consultados el manifesto o en el archivo README de cada módulo.
#
# All libregob modules are available under the A-GPLv3 Licence.
# The licence of third party developments used by the project
# is available on the respective module manifest or readme.
###############################################################################
{
    'name': 'Base LibreGOB',
    'version': '10.0.0.0.1',
    'category': 'Tools',
    'sequence': 14,
    'author': 'LIBREGOB - FÁBRICA DE SOFTWARE LIBRE',
    'website': 'www.libregob.org',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'base',
        # OCA/server-tools
        'audit_log',
        # OCA/web
        'web_responsive',
        'web_decimal_numpad_dot',
        'web_no_bubble',
        # OCA/server-backend
        'base_user_role',
        # CybroOdoo/CybroAddons
        'login_user_detail',

        # Odoo
        'auth_crypt',
    ],
    'external_dependencies': {
    },
    'data': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
