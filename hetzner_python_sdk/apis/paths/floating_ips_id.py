from hetzner_python_sdk.paths.floating_ips_id.get import ApiForget
from hetzner_python_sdk.paths.floating_ips_id.put import ApiForput
from hetzner_python_sdk.paths.floating_ips_id.delete import ApiFordelete


class FloatingIpsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
