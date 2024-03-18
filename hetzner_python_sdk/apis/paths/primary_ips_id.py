from hetzner_python_sdk.paths.primary_ips_id.get import ApiForget
from hetzner_python_sdk.paths.primary_ips_id.put import ApiForput
from hetzner_python_sdk.paths.primary_ips_id.delete import ApiFordelete


class PrimaryIpsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
