import typing_extensions

from hetzner_python_sdk.paths import PathValues
from hetzner_python_sdk.apis.paths.actions import Actions
from hetzner_python_sdk.apis.paths.actions_id import ActionsId
from hetzner_python_sdk.apis.paths.certificates import Certificates
from hetzner_python_sdk.apis.paths.certificates_actions import CertificatesActions
from hetzner_python_sdk.apis.paths.certificates_actions_id import CertificatesActionsId
from hetzner_python_sdk.apis.paths.certificates_id import CertificatesId
from hetzner_python_sdk.apis.paths.certificates_id_actions import CertificatesIdActions
from hetzner_python_sdk.apis.paths.certificates_id_actions_retry import CertificatesIdActionsRetry
from hetzner_python_sdk.apis.paths.certificates_id_actions_action_id import CertificatesIdActionsActionId
from hetzner_python_sdk.apis.paths.datacenters import Datacenters
from hetzner_python_sdk.apis.paths.datacenters_id import DatacentersId
from hetzner_python_sdk.apis.paths.firewalls import Firewalls
from hetzner_python_sdk.apis.paths.firewalls_actions import FirewallsActions
from hetzner_python_sdk.apis.paths.firewalls_actions_id import FirewallsActionsId
from hetzner_python_sdk.apis.paths.firewalls_id import FirewallsId
from hetzner_python_sdk.apis.paths.firewalls_id_actions import FirewallsIdActions
from hetzner_python_sdk.apis.paths.firewalls_id_actions_apply_to_resources import FirewallsIdActionsApplyToResources
from hetzner_python_sdk.apis.paths.firewalls_id_actions_remove_from_resources import FirewallsIdActionsRemoveFromResources
from hetzner_python_sdk.apis.paths.firewalls_id_actions_set_rules import FirewallsIdActionsSetRules
from hetzner_python_sdk.apis.paths.firewalls_id_actions_action_id import FirewallsIdActionsActionId
from hetzner_python_sdk.apis.paths.floating_ips import FloatingIps
from hetzner_python_sdk.apis.paths.floating_ips_actions import FloatingIpsActions
from hetzner_python_sdk.apis.paths.floating_ips_actions_id import FloatingIpsActionsId
from hetzner_python_sdk.apis.paths.floating_ips_id import FloatingIpsId
from hetzner_python_sdk.apis.paths.floating_ips_id_actions import FloatingIpsIdActions
from hetzner_python_sdk.apis.paths.floating_ips_id_actions_assign import FloatingIpsIdActionsAssign
from hetzner_python_sdk.apis.paths.floating_ips_id_actions_change_dns_ptr import FloatingIpsIdActionsChangeDnsPtr
from hetzner_python_sdk.apis.paths.floating_ips_id_actions_change_protection import FloatingIpsIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.floating_ips_id_actions_unassign import FloatingIpsIdActionsUnassign
from hetzner_python_sdk.apis.paths.floating_ips_id_actions_action_id import FloatingIpsIdActionsActionId
from hetzner_python_sdk.apis.paths.images import Images
from hetzner_python_sdk.apis.paths.images_actions import ImagesActions
from hetzner_python_sdk.apis.paths.images_actions_id import ImagesActionsId
from hetzner_python_sdk.apis.paths.images_id import ImagesId
from hetzner_python_sdk.apis.paths.images_id_actions import ImagesIdActions
from hetzner_python_sdk.apis.paths.images_id_actions_change_protection import ImagesIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.images_id_actions_action_id import ImagesIdActionsActionId
from hetzner_python_sdk.apis.paths.isos import Isos
from hetzner_python_sdk.apis.paths.isos_id import IsosId
from hetzner_python_sdk.apis.paths.load_balancer_types import LoadBalancerTypes
from hetzner_python_sdk.apis.paths.load_balancer_types_id import LoadBalancerTypesId
from hetzner_python_sdk.apis.paths.load_balancers import LoadBalancers
from hetzner_python_sdk.apis.paths.load_balancers_actions import LoadBalancersActions
from hetzner_python_sdk.apis.paths.load_balancers_actions_id import LoadBalancersActionsId
from hetzner_python_sdk.apis.paths.load_balancers_id import LoadBalancersId
from hetzner_python_sdk.apis.paths.load_balancers_id_actions import LoadBalancersIdActions
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_add_service import LoadBalancersIdActionsAddService
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_add_target import LoadBalancersIdActionsAddTarget
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_attach_to_network import LoadBalancersIdActionsAttachToNetwork
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_change_algorithm import LoadBalancersIdActionsChangeAlgorithm
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_change_dns_ptr import LoadBalancersIdActionsChangeDnsPtr
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_change_protection import LoadBalancersIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_change_type import LoadBalancersIdActionsChangeType
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_delete_service import LoadBalancersIdActionsDeleteService
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_detach_from_network import LoadBalancersIdActionsDetachFromNetwork
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_disable_public_interface import LoadBalancersIdActionsDisablePublicInterface
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_enable_public_interface import LoadBalancersIdActionsEnablePublicInterface
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_remove_target import LoadBalancersIdActionsRemoveTarget
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_update_service import LoadBalancersIdActionsUpdateService
from hetzner_python_sdk.apis.paths.load_balancers_id_actions_action_id import LoadBalancersIdActionsActionId
from hetzner_python_sdk.apis.paths.load_balancers_id_metrics import LoadBalancersIdMetrics
from hetzner_python_sdk.apis.paths.locations import Locations
from hetzner_python_sdk.apis.paths.locations_id import LocationsId
from hetzner_python_sdk.apis.paths.networks import Networks
from hetzner_python_sdk.apis.paths.networks_actions import NetworksActions
from hetzner_python_sdk.apis.paths.networks_actions_id import NetworksActionsId
from hetzner_python_sdk.apis.paths.networks_id import NetworksId
from hetzner_python_sdk.apis.paths.networks_id_actions import NetworksIdActions
from hetzner_python_sdk.apis.paths.networks_id_actions_add_route import NetworksIdActionsAddRoute
from hetzner_python_sdk.apis.paths.networks_id_actions_add_subnet import NetworksIdActionsAddSubnet
from hetzner_python_sdk.apis.paths.networks_id_actions_change_ip_range import NetworksIdActionsChangeIpRange
from hetzner_python_sdk.apis.paths.networks_id_actions_change_protection import NetworksIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.networks_id_actions_delete_route import NetworksIdActionsDeleteRoute
from hetzner_python_sdk.apis.paths.networks_id_actions_delete_subnet import NetworksIdActionsDeleteSubnet
from hetzner_python_sdk.apis.paths.networks_id_actions_action_id import NetworksIdActionsActionId
from hetzner_python_sdk.apis.paths.placement_groups import PlacementGroups
from hetzner_python_sdk.apis.paths.placement_groups_id import PlacementGroupsId
from hetzner_python_sdk.apis.paths.pricing import Pricing
from hetzner_python_sdk.apis.paths.primary_ips import PrimaryIps
from hetzner_python_sdk.apis.paths.primary_ips_actions import PrimaryIpsActions
from hetzner_python_sdk.apis.paths.primary_ips_actions_id import PrimaryIpsActionsId
from hetzner_python_sdk.apis.paths.primary_ips_id import PrimaryIpsId
from hetzner_python_sdk.apis.paths.primary_ips_id_actions_assign import PrimaryIpsIdActionsAssign
from hetzner_python_sdk.apis.paths.primary_ips_id_actions_change_dns_ptr import PrimaryIpsIdActionsChangeDnsPtr
from hetzner_python_sdk.apis.paths.primary_ips_id_actions_change_protection import PrimaryIpsIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.primary_ips_id_actions_unassign import PrimaryIpsIdActionsUnassign
from hetzner_python_sdk.apis.paths.server_types import ServerTypes
from hetzner_python_sdk.apis.paths.server_types_id import ServerTypesId
from hetzner_python_sdk.apis.paths.servers import Servers
from hetzner_python_sdk.apis.paths.servers_actions import ServersActions
from hetzner_python_sdk.apis.paths.servers_actions_id import ServersActionsId
from hetzner_python_sdk.apis.paths.servers_id import ServersId
from hetzner_python_sdk.apis.paths.servers_id_actions import ServersIdActions
from hetzner_python_sdk.apis.paths.servers_id_actions_add_to_placement_group import ServersIdActionsAddToPlacementGroup
from hetzner_python_sdk.apis.paths.servers_id_actions_attach_iso import ServersIdActionsAttachIso
from hetzner_python_sdk.apis.paths.servers_id_actions_attach_to_network import ServersIdActionsAttachToNetwork
from hetzner_python_sdk.apis.paths.servers_id_actions_change_alias_ips import ServersIdActionsChangeAliasIps
from hetzner_python_sdk.apis.paths.servers_id_actions_change_dns_ptr import ServersIdActionsChangeDnsPtr
from hetzner_python_sdk.apis.paths.servers_id_actions_change_protection import ServersIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.servers_id_actions_change_type import ServersIdActionsChangeType
from hetzner_python_sdk.apis.paths.servers_id_actions_create_image import ServersIdActionsCreateImage
from hetzner_python_sdk.apis.paths.servers_id_actions_detach_from_network import ServersIdActionsDetachFromNetwork
from hetzner_python_sdk.apis.paths.servers_id_actions_detach_iso import ServersIdActionsDetachIso
from hetzner_python_sdk.apis.paths.servers_id_actions_disable_backup import ServersIdActionsDisableBackup
from hetzner_python_sdk.apis.paths.servers_id_actions_disable_rescue import ServersIdActionsDisableRescue
from hetzner_python_sdk.apis.paths.servers_id_actions_enable_backup import ServersIdActionsEnableBackup
from hetzner_python_sdk.apis.paths.servers_id_actions_enable_rescue import ServersIdActionsEnableRescue
from hetzner_python_sdk.apis.paths.servers_id_actions_poweroff import ServersIdActionsPoweroff
from hetzner_python_sdk.apis.paths.servers_id_actions_poweron import ServersIdActionsPoweron
from hetzner_python_sdk.apis.paths.servers_id_actions_reboot import ServersIdActionsReboot
from hetzner_python_sdk.apis.paths.servers_id_actions_rebuild import ServersIdActionsRebuild
from hetzner_python_sdk.apis.paths.servers_id_actions_remove_from_placement_group import ServersIdActionsRemoveFromPlacementGroup
from hetzner_python_sdk.apis.paths.servers_id_actions_request_console import ServersIdActionsRequestConsole
from hetzner_python_sdk.apis.paths.servers_id_actions_reset import ServersIdActionsReset
from hetzner_python_sdk.apis.paths.servers_id_actions_reset_password import ServersIdActionsResetPassword
from hetzner_python_sdk.apis.paths.servers_id_actions_shutdown import ServersIdActionsShutdown
from hetzner_python_sdk.apis.paths.servers_id_actions_action_id import ServersIdActionsActionId
from hetzner_python_sdk.apis.paths.servers_id_metrics import ServersIdMetrics
from hetzner_python_sdk.apis.paths.ssh_keys import SshKeys
from hetzner_python_sdk.apis.paths.ssh_keys_id import SshKeysId
from hetzner_python_sdk.apis.paths.volumes import Volumes
from hetzner_python_sdk.apis.paths.volumes_actions import VolumesActions
from hetzner_python_sdk.apis.paths.volumes_actions_id import VolumesActionsId
from hetzner_python_sdk.apis.paths.volumes_id import VolumesId
from hetzner_python_sdk.apis.paths.volumes_id_actions import VolumesIdActions
from hetzner_python_sdk.apis.paths.volumes_id_actions_attach import VolumesIdActionsAttach
from hetzner_python_sdk.apis.paths.volumes_id_actions_change_protection import VolumesIdActionsChangeProtection
from hetzner_python_sdk.apis.paths.volumes_id_actions_detach import VolumesIdActionsDetach
from hetzner_python_sdk.apis.paths.volumes_id_actions_resize import VolumesIdActionsResize
from hetzner_python_sdk.apis.paths.volumes_id_actions_action_id import VolumesIdActionsActionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIONS: Actions,
        PathValues.ACTIONS_ID: ActionsId,
        PathValues.CERTIFICATES: Certificates,
        PathValues.CERTIFICATES_ACTIONS: CertificatesActions,
        PathValues.CERTIFICATES_ACTIONS_ID: CertificatesActionsId,
        PathValues.CERTIFICATES_ID: CertificatesId,
        PathValues.CERTIFICATES_ID_ACTIONS: CertificatesIdActions,
        PathValues.CERTIFICATES_ID_ACTIONS_RETRY: CertificatesIdActionsRetry,
        PathValues.CERTIFICATES_ID_ACTIONS_ACTION_ID: CertificatesIdActionsActionId,
        PathValues.DATACENTERS: Datacenters,
        PathValues.DATACENTERS_ID: DatacentersId,
        PathValues.FIREWALLS: Firewalls,
        PathValues.FIREWALLS_ACTIONS: FirewallsActions,
        PathValues.FIREWALLS_ACTIONS_ID: FirewallsActionsId,
        PathValues.FIREWALLS_ID: FirewallsId,
        PathValues.FIREWALLS_ID_ACTIONS: FirewallsIdActions,
        PathValues.FIREWALLS_ID_ACTIONS_APPLY_TO_RESOURCES: FirewallsIdActionsApplyToResources,
        PathValues.FIREWALLS_ID_ACTIONS_REMOVE_FROM_RESOURCES: FirewallsIdActionsRemoveFromResources,
        PathValues.FIREWALLS_ID_ACTIONS_SET_RULES: FirewallsIdActionsSetRules,
        PathValues.FIREWALLS_ID_ACTIONS_ACTION_ID: FirewallsIdActionsActionId,
        PathValues.FLOATING_IPS: FloatingIps,
        PathValues.FLOATING_IPS_ACTIONS: FloatingIpsActions,
        PathValues.FLOATING_IPS_ACTIONS_ID: FloatingIpsActionsId,
        PathValues.FLOATING_IPS_ID: FloatingIpsId,
        PathValues.FLOATING_IPS_ID_ACTIONS: FloatingIpsIdActions,
        PathValues.FLOATING_IPS_ID_ACTIONS_ASSIGN: FloatingIpsIdActionsAssign,
        PathValues.FLOATING_IPS_ID_ACTIONS_CHANGE_DNS_PTR: FloatingIpsIdActionsChangeDnsPtr,
        PathValues.FLOATING_IPS_ID_ACTIONS_CHANGE_PROTECTION: FloatingIpsIdActionsChangeProtection,
        PathValues.FLOATING_IPS_ID_ACTIONS_UNASSIGN: FloatingIpsIdActionsUnassign,
        PathValues.FLOATING_IPS_ID_ACTIONS_ACTION_ID: FloatingIpsIdActionsActionId,
        PathValues.IMAGES: Images,
        PathValues.IMAGES_ACTIONS: ImagesActions,
        PathValues.IMAGES_ACTIONS_ID: ImagesActionsId,
        PathValues.IMAGES_ID: ImagesId,
        PathValues.IMAGES_ID_ACTIONS: ImagesIdActions,
        PathValues.IMAGES_ID_ACTIONS_CHANGE_PROTECTION: ImagesIdActionsChangeProtection,
        PathValues.IMAGES_ID_ACTIONS_ACTION_ID: ImagesIdActionsActionId,
        PathValues.ISOS: Isos,
        PathValues.ISOS_ID: IsosId,
        PathValues.LOAD_BALANCER_TYPES: LoadBalancerTypes,
        PathValues.LOAD_BALANCER_TYPES_ID: LoadBalancerTypesId,
        PathValues.LOAD_BALANCERS: LoadBalancers,
        PathValues.LOAD_BALANCERS_ACTIONS: LoadBalancersActions,
        PathValues.LOAD_BALANCERS_ACTIONS_ID: LoadBalancersActionsId,
        PathValues.LOAD_BALANCERS_ID: LoadBalancersId,
        PathValues.LOAD_BALANCERS_ID_ACTIONS: LoadBalancersIdActions,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ADD_SERVICE: LoadBalancersIdActionsAddService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ADD_TARGET: LoadBalancersIdActionsAddTarget,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ATTACH_TO_NETWORK: LoadBalancersIdActionsAttachToNetwork,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_ALGORITHM: LoadBalancersIdActionsChangeAlgorithm,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_DNS_PTR: LoadBalancersIdActionsChangeDnsPtr,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_PROTECTION: LoadBalancersIdActionsChangeProtection,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_TYPE: LoadBalancersIdActionsChangeType,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DELETE_SERVICE: LoadBalancersIdActionsDeleteService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DETACH_FROM_NETWORK: LoadBalancersIdActionsDetachFromNetwork,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DISABLE_PUBLIC_INTERFACE: LoadBalancersIdActionsDisablePublicInterface,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ENABLE_PUBLIC_INTERFACE: LoadBalancersIdActionsEnablePublicInterface,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_REMOVE_TARGET: LoadBalancersIdActionsRemoveTarget,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_UPDATE_SERVICE: LoadBalancersIdActionsUpdateService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ACTION_ID: LoadBalancersIdActionsActionId,
        PathValues.LOAD_BALANCERS_ID_METRICS: LoadBalancersIdMetrics,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.NETWORKS: Networks,
        PathValues.NETWORKS_ACTIONS: NetworksActions,
        PathValues.NETWORKS_ACTIONS_ID: NetworksActionsId,
        PathValues.NETWORKS_ID: NetworksId,
        PathValues.NETWORKS_ID_ACTIONS: NetworksIdActions,
        PathValues.NETWORKS_ID_ACTIONS_ADD_ROUTE: NetworksIdActionsAddRoute,
        PathValues.NETWORKS_ID_ACTIONS_ADD_SUBNET: NetworksIdActionsAddSubnet,
        PathValues.NETWORKS_ID_ACTIONS_CHANGE_IP_RANGE: NetworksIdActionsChangeIpRange,
        PathValues.NETWORKS_ID_ACTIONS_CHANGE_PROTECTION: NetworksIdActionsChangeProtection,
        PathValues.NETWORKS_ID_ACTIONS_DELETE_ROUTE: NetworksIdActionsDeleteRoute,
        PathValues.NETWORKS_ID_ACTIONS_DELETE_SUBNET: NetworksIdActionsDeleteSubnet,
        PathValues.NETWORKS_ID_ACTIONS_ACTION_ID: NetworksIdActionsActionId,
        PathValues.PLACEMENT_GROUPS: PlacementGroups,
        PathValues.PLACEMENT_GROUPS_ID: PlacementGroupsId,
        PathValues.PRICING: Pricing,
        PathValues.PRIMARY_IPS: PrimaryIps,
        PathValues.PRIMARY_IPS_ACTIONS: PrimaryIpsActions,
        PathValues.PRIMARY_IPS_ACTIONS_ID: PrimaryIpsActionsId,
        PathValues.PRIMARY_IPS_ID: PrimaryIpsId,
        PathValues.PRIMARY_IPS_ID_ACTIONS_ASSIGN: PrimaryIpsIdActionsAssign,
        PathValues.PRIMARY_IPS_ID_ACTIONS_CHANGE_DNS_PTR: PrimaryIpsIdActionsChangeDnsPtr,
        PathValues.PRIMARY_IPS_ID_ACTIONS_CHANGE_PROTECTION: PrimaryIpsIdActionsChangeProtection,
        PathValues.PRIMARY_IPS_ID_ACTIONS_UNASSIGN: PrimaryIpsIdActionsUnassign,
        PathValues.SERVER_TYPES: ServerTypes,
        PathValues.SERVER_TYPES_ID: ServerTypesId,
        PathValues.SERVERS: Servers,
        PathValues.SERVERS_ACTIONS: ServersActions,
        PathValues.SERVERS_ACTIONS_ID: ServersActionsId,
        PathValues.SERVERS_ID: ServersId,
        PathValues.SERVERS_ID_ACTIONS: ServersIdActions,
        PathValues.SERVERS_ID_ACTIONS_ADD_TO_PLACEMENT_GROUP: ServersIdActionsAddToPlacementGroup,
        PathValues.SERVERS_ID_ACTIONS_ATTACH_ISO: ServersIdActionsAttachIso,
        PathValues.SERVERS_ID_ACTIONS_ATTACH_TO_NETWORK: ServersIdActionsAttachToNetwork,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_ALIAS_IPS: ServersIdActionsChangeAliasIps,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_DNS_PTR: ServersIdActionsChangeDnsPtr,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_PROTECTION: ServersIdActionsChangeProtection,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_TYPE: ServersIdActionsChangeType,
        PathValues.SERVERS_ID_ACTIONS_CREATE_IMAGE: ServersIdActionsCreateImage,
        PathValues.SERVERS_ID_ACTIONS_DETACH_FROM_NETWORK: ServersIdActionsDetachFromNetwork,
        PathValues.SERVERS_ID_ACTIONS_DETACH_ISO: ServersIdActionsDetachIso,
        PathValues.SERVERS_ID_ACTIONS_DISABLE_BACKUP: ServersIdActionsDisableBackup,
        PathValues.SERVERS_ID_ACTIONS_DISABLE_RESCUE: ServersIdActionsDisableRescue,
        PathValues.SERVERS_ID_ACTIONS_ENABLE_BACKUP: ServersIdActionsEnableBackup,
        PathValues.SERVERS_ID_ACTIONS_ENABLE_RESCUE: ServersIdActionsEnableRescue,
        PathValues.SERVERS_ID_ACTIONS_POWEROFF: ServersIdActionsPoweroff,
        PathValues.SERVERS_ID_ACTIONS_POWERON: ServersIdActionsPoweron,
        PathValues.SERVERS_ID_ACTIONS_REBOOT: ServersIdActionsReboot,
        PathValues.SERVERS_ID_ACTIONS_REBUILD: ServersIdActionsRebuild,
        PathValues.SERVERS_ID_ACTIONS_REMOVE_FROM_PLACEMENT_GROUP: ServersIdActionsRemoveFromPlacementGroup,
        PathValues.SERVERS_ID_ACTIONS_REQUEST_CONSOLE: ServersIdActionsRequestConsole,
        PathValues.SERVERS_ID_ACTIONS_RESET: ServersIdActionsReset,
        PathValues.SERVERS_ID_ACTIONS_RESET_PASSWORD: ServersIdActionsResetPassword,
        PathValues.SERVERS_ID_ACTIONS_SHUTDOWN: ServersIdActionsShutdown,
        PathValues.SERVERS_ID_ACTIONS_ACTION_ID: ServersIdActionsActionId,
        PathValues.SERVERS_ID_METRICS: ServersIdMetrics,
        PathValues.SSH_KEYS: SshKeys,
        PathValues.SSH_KEYS_ID: SshKeysId,
        PathValues.VOLUMES: Volumes,
        PathValues.VOLUMES_ACTIONS: VolumesActions,
        PathValues.VOLUMES_ACTIONS_ID: VolumesActionsId,
        PathValues.VOLUMES_ID: VolumesId,
        PathValues.VOLUMES_ID_ACTIONS: VolumesIdActions,
        PathValues.VOLUMES_ID_ACTIONS_ATTACH: VolumesIdActionsAttach,
        PathValues.VOLUMES_ID_ACTIONS_CHANGE_PROTECTION: VolumesIdActionsChangeProtection,
        PathValues.VOLUMES_ID_ACTIONS_DETACH: VolumesIdActionsDetach,
        PathValues.VOLUMES_ID_ACTIONS_RESIZE: VolumesIdActionsResize,
        PathValues.VOLUMES_ID_ACTIONS_ACTION_ID: VolumesIdActionsActionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIONS: Actions,
        PathValues.ACTIONS_ID: ActionsId,
        PathValues.CERTIFICATES: Certificates,
        PathValues.CERTIFICATES_ACTIONS: CertificatesActions,
        PathValues.CERTIFICATES_ACTIONS_ID: CertificatesActionsId,
        PathValues.CERTIFICATES_ID: CertificatesId,
        PathValues.CERTIFICATES_ID_ACTIONS: CertificatesIdActions,
        PathValues.CERTIFICATES_ID_ACTIONS_RETRY: CertificatesIdActionsRetry,
        PathValues.CERTIFICATES_ID_ACTIONS_ACTION_ID: CertificatesIdActionsActionId,
        PathValues.DATACENTERS: Datacenters,
        PathValues.DATACENTERS_ID: DatacentersId,
        PathValues.FIREWALLS: Firewalls,
        PathValues.FIREWALLS_ACTIONS: FirewallsActions,
        PathValues.FIREWALLS_ACTIONS_ID: FirewallsActionsId,
        PathValues.FIREWALLS_ID: FirewallsId,
        PathValues.FIREWALLS_ID_ACTIONS: FirewallsIdActions,
        PathValues.FIREWALLS_ID_ACTIONS_APPLY_TO_RESOURCES: FirewallsIdActionsApplyToResources,
        PathValues.FIREWALLS_ID_ACTIONS_REMOVE_FROM_RESOURCES: FirewallsIdActionsRemoveFromResources,
        PathValues.FIREWALLS_ID_ACTIONS_SET_RULES: FirewallsIdActionsSetRules,
        PathValues.FIREWALLS_ID_ACTIONS_ACTION_ID: FirewallsIdActionsActionId,
        PathValues.FLOATING_IPS: FloatingIps,
        PathValues.FLOATING_IPS_ACTIONS: FloatingIpsActions,
        PathValues.FLOATING_IPS_ACTIONS_ID: FloatingIpsActionsId,
        PathValues.FLOATING_IPS_ID: FloatingIpsId,
        PathValues.FLOATING_IPS_ID_ACTIONS: FloatingIpsIdActions,
        PathValues.FLOATING_IPS_ID_ACTIONS_ASSIGN: FloatingIpsIdActionsAssign,
        PathValues.FLOATING_IPS_ID_ACTIONS_CHANGE_DNS_PTR: FloatingIpsIdActionsChangeDnsPtr,
        PathValues.FLOATING_IPS_ID_ACTIONS_CHANGE_PROTECTION: FloatingIpsIdActionsChangeProtection,
        PathValues.FLOATING_IPS_ID_ACTIONS_UNASSIGN: FloatingIpsIdActionsUnassign,
        PathValues.FLOATING_IPS_ID_ACTIONS_ACTION_ID: FloatingIpsIdActionsActionId,
        PathValues.IMAGES: Images,
        PathValues.IMAGES_ACTIONS: ImagesActions,
        PathValues.IMAGES_ACTIONS_ID: ImagesActionsId,
        PathValues.IMAGES_ID: ImagesId,
        PathValues.IMAGES_ID_ACTIONS: ImagesIdActions,
        PathValues.IMAGES_ID_ACTIONS_CHANGE_PROTECTION: ImagesIdActionsChangeProtection,
        PathValues.IMAGES_ID_ACTIONS_ACTION_ID: ImagesIdActionsActionId,
        PathValues.ISOS: Isos,
        PathValues.ISOS_ID: IsosId,
        PathValues.LOAD_BALANCER_TYPES: LoadBalancerTypes,
        PathValues.LOAD_BALANCER_TYPES_ID: LoadBalancerTypesId,
        PathValues.LOAD_BALANCERS: LoadBalancers,
        PathValues.LOAD_BALANCERS_ACTIONS: LoadBalancersActions,
        PathValues.LOAD_BALANCERS_ACTIONS_ID: LoadBalancersActionsId,
        PathValues.LOAD_BALANCERS_ID: LoadBalancersId,
        PathValues.LOAD_BALANCERS_ID_ACTIONS: LoadBalancersIdActions,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ADD_SERVICE: LoadBalancersIdActionsAddService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ADD_TARGET: LoadBalancersIdActionsAddTarget,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ATTACH_TO_NETWORK: LoadBalancersIdActionsAttachToNetwork,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_ALGORITHM: LoadBalancersIdActionsChangeAlgorithm,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_DNS_PTR: LoadBalancersIdActionsChangeDnsPtr,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_PROTECTION: LoadBalancersIdActionsChangeProtection,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_CHANGE_TYPE: LoadBalancersIdActionsChangeType,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DELETE_SERVICE: LoadBalancersIdActionsDeleteService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DETACH_FROM_NETWORK: LoadBalancersIdActionsDetachFromNetwork,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_DISABLE_PUBLIC_INTERFACE: LoadBalancersIdActionsDisablePublicInterface,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ENABLE_PUBLIC_INTERFACE: LoadBalancersIdActionsEnablePublicInterface,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_REMOVE_TARGET: LoadBalancersIdActionsRemoveTarget,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_UPDATE_SERVICE: LoadBalancersIdActionsUpdateService,
        PathValues.LOAD_BALANCERS_ID_ACTIONS_ACTION_ID: LoadBalancersIdActionsActionId,
        PathValues.LOAD_BALANCERS_ID_METRICS: LoadBalancersIdMetrics,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.NETWORKS: Networks,
        PathValues.NETWORKS_ACTIONS: NetworksActions,
        PathValues.NETWORKS_ACTIONS_ID: NetworksActionsId,
        PathValues.NETWORKS_ID: NetworksId,
        PathValues.NETWORKS_ID_ACTIONS: NetworksIdActions,
        PathValues.NETWORKS_ID_ACTIONS_ADD_ROUTE: NetworksIdActionsAddRoute,
        PathValues.NETWORKS_ID_ACTIONS_ADD_SUBNET: NetworksIdActionsAddSubnet,
        PathValues.NETWORKS_ID_ACTIONS_CHANGE_IP_RANGE: NetworksIdActionsChangeIpRange,
        PathValues.NETWORKS_ID_ACTIONS_CHANGE_PROTECTION: NetworksIdActionsChangeProtection,
        PathValues.NETWORKS_ID_ACTIONS_DELETE_ROUTE: NetworksIdActionsDeleteRoute,
        PathValues.NETWORKS_ID_ACTIONS_DELETE_SUBNET: NetworksIdActionsDeleteSubnet,
        PathValues.NETWORKS_ID_ACTIONS_ACTION_ID: NetworksIdActionsActionId,
        PathValues.PLACEMENT_GROUPS: PlacementGroups,
        PathValues.PLACEMENT_GROUPS_ID: PlacementGroupsId,
        PathValues.PRICING: Pricing,
        PathValues.PRIMARY_IPS: PrimaryIps,
        PathValues.PRIMARY_IPS_ACTIONS: PrimaryIpsActions,
        PathValues.PRIMARY_IPS_ACTIONS_ID: PrimaryIpsActionsId,
        PathValues.PRIMARY_IPS_ID: PrimaryIpsId,
        PathValues.PRIMARY_IPS_ID_ACTIONS_ASSIGN: PrimaryIpsIdActionsAssign,
        PathValues.PRIMARY_IPS_ID_ACTIONS_CHANGE_DNS_PTR: PrimaryIpsIdActionsChangeDnsPtr,
        PathValues.PRIMARY_IPS_ID_ACTIONS_CHANGE_PROTECTION: PrimaryIpsIdActionsChangeProtection,
        PathValues.PRIMARY_IPS_ID_ACTIONS_UNASSIGN: PrimaryIpsIdActionsUnassign,
        PathValues.SERVER_TYPES: ServerTypes,
        PathValues.SERVER_TYPES_ID: ServerTypesId,
        PathValues.SERVERS: Servers,
        PathValues.SERVERS_ACTIONS: ServersActions,
        PathValues.SERVERS_ACTIONS_ID: ServersActionsId,
        PathValues.SERVERS_ID: ServersId,
        PathValues.SERVERS_ID_ACTIONS: ServersIdActions,
        PathValues.SERVERS_ID_ACTIONS_ADD_TO_PLACEMENT_GROUP: ServersIdActionsAddToPlacementGroup,
        PathValues.SERVERS_ID_ACTIONS_ATTACH_ISO: ServersIdActionsAttachIso,
        PathValues.SERVERS_ID_ACTIONS_ATTACH_TO_NETWORK: ServersIdActionsAttachToNetwork,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_ALIAS_IPS: ServersIdActionsChangeAliasIps,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_DNS_PTR: ServersIdActionsChangeDnsPtr,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_PROTECTION: ServersIdActionsChangeProtection,
        PathValues.SERVERS_ID_ACTIONS_CHANGE_TYPE: ServersIdActionsChangeType,
        PathValues.SERVERS_ID_ACTIONS_CREATE_IMAGE: ServersIdActionsCreateImage,
        PathValues.SERVERS_ID_ACTIONS_DETACH_FROM_NETWORK: ServersIdActionsDetachFromNetwork,
        PathValues.SERVERS_ID_ACTIONS_DETACH_ISO: ServersIdActionsDetachIso,
        PathValues.SERVERS_ID_ACTIONS_DISABLE_BACKUP: ServersIdActionsDisableBackup,
        PathValues.SERVERS_ID_ACTIONS_DISABLE_RESCUE: ServersIdActionsDisableRescue,
        PathValues.SERVERS_ID_ACTIONS_ENABLE_BACKUP: ServersIdActionsEnableBackup,
        PathValues.SERVERS_ID_ACTIONS_ENABLE_RESCUE: ServersIdActionsEnableRescue,
        PathValues.SERVERS_ID_ACTIONS_POWEROFF: ServersIdActionsPoweroff,
        PathValues.SERVERS_ID_ACTIONS_POWERON: ServersIdActionsPoweron,
        PathValues.SERVERS_ID_ACTIONS_REBOOT: ServersIdActionsReboot,
        PathValues.SERVERS_ID_ACTIONS_REBUILD: ServersIdActionsRebuild,
        PathValues.SERVERS_ID_ACTIONS_REMOVE_FROM_PLACEMENT_GROUP: ServersIdActionsRemoveFromPlacementGroup,
        PathValues.SERVERS_ID_ACTIONS_REQUEST_CONSOLE: ServersIdActionsRequestConsole,
        PathValues.SERVERS_ID_ACTIONS_RESET: ServersIdActionsReset,
        PathValues.SERVERS_ID_ACTIONS_RESET_PASSWORD: ServersIdActionsResetPassword,
        PathValues.SERVERS_ID_ACTIONS_SHUTDOWN: ServersIdActionsShutdown,
        PathValues.SERVERS_ID_ACTIONS_ACTION_ID: ServersIdActionsActionId,
        PathValues.SERVERS_ID_METRICS: ServersIdMetrics,
        PathValues.SSH_KEYS: SshKeys,
        PathValues.SSH_KEYS_ID: SshKeysId,
        PathValues.VOLUMES: Volumes,
        PathValues.VOLUMES_ACTIONS: VolumesActions,
        PathValues.VOLUMES_ACTIONS_ID: VolumesActionsId,
        PathValues.VOLUMES_ID: VolumesId,
        PathValues.VOLUMES_ID_ACTIONS: VolumesIdActions,
        PathValues.VOLUMES_ID_ACTIONS_ATTACH: VolumesIdActionsAttach,
        PathValues.VOLUMES_ID_ACTIONS_CHANGE_PROTECTION: VolumesIdActionsChangeProtection,
        PathValues.VOLUMES_ID_ACTIONS_DETACH: VolumesIdActionsDetach,
        PathValues.VOLUMES_ID_ACTIONS_RESIZE: VolumesIdActionsResize,
        PathValues.VOLUMES_ID_ACTIONS_ACTION_ID: VolumesIdActionsActionId,
    }
)
