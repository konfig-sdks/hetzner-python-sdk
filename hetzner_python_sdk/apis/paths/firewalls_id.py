from hetzner_python_sdk.paths.firewalls_id.get import ApiForget
from hetzner_python_sdk.paths.firewalls_id.put import ApiForput
from hetzner_python_sdk.paths.firewalls_id.delete import ApiFordelete


class FirewallsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
