from hetzner_python_sdk.paths.servers_id.get import ApiForget
from hetzner_python_sdk.paths.servers_id.put import ApiForput
from hetzner_python_sdk.paths.servers_id.delete import ApiFordelete


class ServersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
