from hetzner_python_sdk.paths.ssh_keys_id.get import ApiForget
from hetzner_python_sdk.paths.ssh_keys_id.put import ApiForput
from hetzner_python_sdk.paths.ssh_keys_id.delete import ApiFordelete


class SshKeysId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
