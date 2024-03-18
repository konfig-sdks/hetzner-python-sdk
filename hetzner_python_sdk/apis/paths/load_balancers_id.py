from hetzner_python_sdk.paths.load_balancers_id.get import ApiForget
from hetzner_python_sdk.paths.load_balancers_id.put import ApiForput
from hetzner_python_sdk.paths.load_balancers_id.delete import ApiFordelete


class LoadBalancersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
