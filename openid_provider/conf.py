import os
import tempfile
from django.conf import settings

tempdir = tempfile.gettempdir()

STORE = getattr(settings, 'OPENID_PROVIDER_STORE',
                'openid.store.filestore.FileOpenIDStore')

FILESTORE_PATH = getattr(settings, 'OPENID_PROVIDER_FILESTORE_PATH',
                         os.path.join(tempdir, 'openid-filestore'))

SREG_DATA_CALLBACK = getattr(settings, 'OPENID_PROVIDER_SREG_DATA_CALLBACK',
                             'openid_provider.utils.get_default_sreg_data')

AX_DATA_CALLBACK = getattr(settings, 'OPENID_PROVIDER_AX_DATA_CALLBACK',
                           'openid_provider.utils.get_default_ax_data')

AX_EXTENSION = getattr(settings, 'OPENID_PROVIDER_AX_EXTENSION', False)

# restrict the allowed trusted sites consumers
# via settings and callable code
TRUSTED_SITES_CALLBACK = getattr(settings, 'OPENID_PROVIDER_TRUSTED_SITES_CALLBACK',
                           'openid_provider.utils.is_trusted_site_calculation_default')

TRUSTED_SITES_CALLBACK_ENABLED = getattr(settings, 'OPENID_PROVIDER_TRUSTED_SITES_CALLBACK_ENABLED', False)
