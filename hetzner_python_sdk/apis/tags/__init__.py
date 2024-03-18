# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hetzner_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SERVER_ACTIONS = "Server Actions"
    LOAD_BALANCER_ACTIONS = "Load Balancer Actions"
    NETWORK_ACTIONS = "Network Actions"
    FLOATING_IP_ACTIONS = "Floating IP Actions"
    VOLUME_ACTIONS = "Volume Actions"
    FIREWALL_ACTIONS = "Firewall Actions"
    LOAD_BALANCERS = "Load Balancers"
    PRIMARY_IP_ACTIONS = "Primary IP Actions"
    SERVERS = "Servers"
    CERTIFICATES = "Certificates"
    CERTIFICATE_ACTIONS = "Certificate Actions"
    FIREWALLS = "Firewalls"
    FLOATING_IPS = "Floating IPs"
    IMAGE_ACTIONS = "Image Actions"
    NETWORKS = "Networks"
    PLACEMENT_GROUPS = "Placement Groups"
    PRIMARY_IPS = "Primary IPs"
    SSH_KEYS = "SSH Keys"
    VOLUMES = "Volumes"
    IMAGES = "Images"
    ACTIONS = "Actions"
    DATACENTERS = "Datacenters"
    ISOS = "ISOs"
    LOAD_BALANCER_TYPES = "Load Balancer Types"
    LOCATIONS = "Locations"
    SERVER_TYPES = "Server Types"
    PRICING = "Pricing"
    NETWORK_ZONES = "Network Zones"
