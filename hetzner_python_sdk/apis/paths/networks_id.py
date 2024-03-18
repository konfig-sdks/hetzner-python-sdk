from hetzner_python_sdk.paths.networks_id.get import ApiForget
from hetzner_python_sdk.paths.networks_id.put import ApiForput
from hetzner_python_sdk.paths.networks_id.delete import ApiFordelete


class NetworksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
