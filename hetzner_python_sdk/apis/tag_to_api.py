import typing_extensions

from hetzner_python_sdk.apis.tags import TagValues
from hetzner_python_sdk.apis.tags.server_actions_api import ServerActionsApi
from hetzner_python_sdk.apis.tags.load_balancer_actions_api import LoadBalancerActionsApi
from hetzner_python_sdk.apis.tags.network_actions_api import NetworkActionsApi
from hetzner_python_sdk.apis.tags.floating_ip_actions_api import FloatingIPActionsApi
from hetzner_python_sdk.apis.tags.volume_actions_api import VolumeActionsApi
from hetzner_python_sdk.apis.tags.firewall_actions_api import FirewallActionsApi
from hetzner_python_sdk.apis.tags.load_balancers_api import LoadBalancersApi
from hetzner_python_sdk.apis.tags.primary_ip_actions_api import PrimaryIPActionsApi
from hetzner_python_sdk.apis.tags.servers_api import ServersApi
from hetzner_python_sdk.apis.tags.certificates_api import CertificatesApi
from hetzner_python_sdk.apis.tags.certificate_actions_api import CertificateActionsApi
from hetzner_python_sdk.apis.tags.firewalls_api import FirewallsApi
from hetzner_python_sdk.apis.tags.floating_ips_api import FloatingIPsApi
from hetzner_python_sdk.apis.tags.image_actions_api import ImageActionsApi
from hetzner_python_sdk.apis.tags.networks_api import NetworksApi
from hetzner_python_sdk.apis.tags.placement_groups_api import PlacementGroupsApi
from hetzner_python_sdk.apis.tags.primary_ips_api import PrimaryIPsApi
from hetzner_python_sdk.apis.tags.ssh_keys_api import SSHKeysApi
from hetzner_python_sdk.apis.tags.volumes_api import VolumesApi
from hetzner_python_sdk.apis.tags.images_api import ImagesApi
from hetzner_python_sdk.apis.tags.actions_api import ActionsApi
from hetzner_python_sdk.apis.tags.datacenters_api import DatacentersApi
from hetzner_python_sdk.apis.tags.isos_api import ISOsApi
from hetzner_python_sdk.apis.tags.load_balancer_types_api import LoadBalancerTypesApi
from hetzner_python_sdk.apis.tags.locations_api import LocationsApi
from hetzner_python_sdk.apis.tags.server_types_api import ServerTypesApi
from hetzner_python_sdk.apis.tags.pricing_api import PricingApi
from hetzner_python_sdk.apis.tags.network_zones_api import NetworkZonesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SERVER_ACTIONS: ServerActionsApi,
        TagValues.LOAD_BALANCER_ACTIONS: LoadBalancerActionsApi,
        TagValues.NETWORK_ACTIONS: NetworkActionsApi,
        TagValues.FLOATING_IP_ACTIONS: FloatingIPActionsApi,
        TagValues.VOLUME_ACTIONS: VolumeActionsApi,
        TagValues.FIREWALL_ACTIONS: FirewallActionsApi,
        TagValues.LOAD_BALANCERS: LoadBalancersApi,
        TagValues.PRIMARY_IP_ACTIONS: PrimaryIPActionsApi,
        TagValues.SERVERS: ServersApi,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.CERTIFICATE_ACTIONS: CertificateActionsApi,
        TagValues.FIREWALLS: FirewallsApi,
        TagValues.FLOATING_IPS: FloatingIPsApi,
        TagValues.IMAGE_ACTIONS: ImageActionsApi,
        TagValues.NETWORKS: NetworksApi,
        TagValues.PLACEMENT_GROUPS: PlacementGroupsApi,
        TagValues.PRIMARY_IPS: PrimaryIPsApi,
        TagValues.SSH_KEYS: SSHKeysApi,
        TagValues.VOLUMES: VolumesApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.ACTIONS: ActionsApi,
        TagValues.DATACENTERS: DatacentersApi,
        TagValues.ISOS: ISOsApi,
        TagValues.LOAD_BALANCER_TYPES: LoadBalancerTypesApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.SERVER_TYPES: ServerTypesApi,
        TagValues.PRICING: PricingApi,
        TagValues.NETWORK_ZONES: NetworkZonesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SERVER_ACTIONS: ServerActionsApi,
        TagValues.LOAD_BALANCER_ACTIONS: LoadBalancerActionsApi,
        TagValues.NETWORK_ACTIONS: NetworkActionsApi,
        TagValues.FLOATING_IP_ACTIONS: FloatingIPActionsApi,
        TagValues.VOLUME_ACTIONS: VolumeActionsApi,
        TagValues.FIREWALL_ACTIONS: FirewallActionsApi,
        TagValues.LOAD_BALANCERS: LoadBalancersApi,
        TagValues.PRIMARY_IP_ACTIONS: PrimaryIPActionsApi,
        TagValues.SERVERS: ServersApi,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.CERTIFICATE_ACTIONS: CertificateActionsApi,
        TagValues.FIREWALLS: FirewallsApi,
        TagValues.FLOATING_IPS: FloatingIPsApi,
        TagValues.IMAGE_ACTIONS: ImageActionsApi,
        TagValues.NETWORKS: NetworksApi,
        TagValues.PLACEMENT_GROUPS: PlacementGroupsApi,
        TagValues.PRIMARY_IPS: PrimaryIPsApi,
        TagValues.SSH_KEYS: SSHKeysApi,
        TagValues.VOLUMES: VolumesApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.ACTIONS: ActionsApi,
        TagValues.DATACENTERS: DatacentersApi,
        TagValues.ISOS: ISOsApi,
        TagValues.LOAD_BALANCER_TYPES: LoadBalancerTypesApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.SERVER_TYPES: ServerTypesApi,
        TagValues.PRICING: PricingApi,
        TagValues.NETWORK_ZONES: NetworkZonesApi,
    }
)
