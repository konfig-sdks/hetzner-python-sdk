from hetzner_python_sdk.paths.certificates_id.get import ApiForget
from hetzner_python_sdk.paths.certificates_id.put import ApiForput
from hetzner_python_sdk.paths.certificates_id.delete import ApiFordelete


class CertificatesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
