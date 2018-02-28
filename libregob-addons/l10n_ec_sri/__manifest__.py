# © 2018 LibreGOB <https://libregob.org>
# © 2018 Daniel A. Mendieta <damendieta@libre.ec>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': "Ecuador - SRI",
    'version': "18.1.0.0",
    'author': "LibreGOB, Daniel A. Mendieta",
    'license': "AGPL-3",
    'website': "http://libregob.org",
    'category': "Account",
    'depends': [
        'base',
        'account',
        'account_invoicing',
        'account_tax_python',
    ],
    'data': [
        'security/ir.model.access.csv',
        #'data/ir_cron.xml',
        'data/ats/l10n_ec_sri.sustento.csv', #10
        'data/104/account.account.tag.csv', #20
        'data/104/account.tax.group.csv', #20
        'data/104/account.tax.csv', #30
        'views/account_invoice.xml',
    ],
    'application': False,
    'installable': True,
    }
