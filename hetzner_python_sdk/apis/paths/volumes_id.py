from hetzner_python_sdk.paths.volumes_id.get import ApiForget
from hetzner_python_sdk.paths.volumes_id.put import ApiForput
from hetzner_python_sdk.paths.volumes_id.delete import ApiFordelete


class VolumesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
