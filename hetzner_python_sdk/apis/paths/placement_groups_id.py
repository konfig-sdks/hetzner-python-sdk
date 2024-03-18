from hetzner_python_sdk.paths.placement_groups_id.get import ApiForget
from hetzner_python_sdk.paths.placement_groups_id.put import ApiForput
from hetzner_python_sdk.paths.placement_groups_id.delete import ApiFordelete


class PlacementGroupsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
