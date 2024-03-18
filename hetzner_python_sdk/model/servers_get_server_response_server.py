# coding: utf-8

"""
    Hetzner Cloud API

    This is the official documentation for the Hetzner Cloud API.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use:  - Our CLI program [hcloud](https://github.com/hetznercloud/cli) - Our [library for Go](https://github.com/hetznercloud/hcloud-go) - Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following:  - The type of integration you would like to develop - Link to the GitHub repo you will use for the Project - Link to some other Open Source work you have already done (if you have done so)  ## Getting Started  To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj`.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud).  **Example Request**  ```bash curl -H \"Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj\" \\   https://api.hetzner.cloud/v1/servers ```  **Example Response**  ```json {   \"servers\": [],   \"meta\": {     \"pagination\": {       \"page\": 1,       \"per_page\": 25,       \"previous_page\": null,       \"next_page\": null,       \"last_page\": 1,       \"total_entries\": 0     }   } } ```  ## Authentication  All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.  **Example Authorization header**  ```http Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj ```  ## Errors  Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | | --------- | --------------------------------------------------------------------- | | `code`    | Short string indicating the type of error (machine-parsable)          | | `message` | Textual description on what has gone wrong                            | | `details` | An object providing for details on the error (schema depends on code) |  **Example response**  ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  ### Error Codes  | Code                      | Description                                                                      | | ------------------------- | -------------------------------------------------------------------------------- | | `forbidden`               | Insufficient permissions for this request                                        | | `unauthorized`            | Request was made with an invalid or unknown token                                | | `invalid_input`           | Error while parsing or processing the input                                      | | `json_error`              | Invalid JSON input in your request                                               | | `locked`                  | The item you are trying to access is locked (there is already an Action running) | | `not_found`               | Entity not found                                                                 | | `rate_limit_exceeded`     | Error when sending too many requests                                             | | `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           | | `resource_unavailable`    | The requested resource is currently unavailable                                  | | `server_error`            | Error within the API backend                                                     | | `service_error`           | Error within a service                                                           | | `uniqueness_error`        | One or more of the objects fields must be unique                                 | | `protected`               | The Action you are trying to start is protected for this resource                | | `maintenance`             | Cannot perform operation due to maintenance                                      | | `conflict`                | The resource has changed during the request, please retry                        | | `unsupported_error`       | The corresponding resource does not support the Action                           | | `token_readonly`          | The token is only allowed to perform GET requests                                | | `unavailable`             | A service or product is currently not available                                  |  **invalid_input**  ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  **uniqueness_error**  ```json {   \"error\": {     \"code\": \"uniqueness_error\",     \"message\": \"SSH key with the same fingerprint already exists\",     \"details\": {       \"fields\": [         {           \"name\": \"public_key\"         }       ]     }   } } ```  **resource_limit_exceeded**  ```json {   \"error\": {     \"code\": \"resource_limit_exceeded\",     \"message\": \"project limit exceeded\",     \"details\": {       \"limits\": [         {           \"name\": \"project_limit\"         }       ]     }   } } ```  ## Labels  Labels are `key/value` pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.  The `hetzner.cloud/` prefix is reserved and cannot be used.  **Example Labels**  ```json {   \"labels\": {     \"environment\": \"development\",     \"service\": \"backend\",     \"example.com/my\": \"label\",     \"just-a-key\": \"\"   } } ```  ## Label Selector  For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                              | | -------------------- | ---------------------------------------------------- | | `k==v` / `k=v`       | Value of key `k` does equal value `v`                | | `k!=v`               | Value of key `k` does not equal value `v`            | | `k`                  | Key `k` is present                                   | | `!k`                 | Key `k` is not present                               | | `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`              | | `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3` | | `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present |  ### Examples  - Returns all resources that have a `env=production` label and that don't have a `type=database` label:    `env=production,type!=database`  - Returns all resources that have a `env=testing` or `env=staging` label:    `env in (testing,staging)`  - Returns all resources that don't have a `type` label:    `!type`  ## Pagination  Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  - A `page` parameter specifies the page to fetch. The number of the first page is 1. - A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a `Link` header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:  **Example Pagination**  ```json {     \"servers\": [...],     \"meta\": {         \"pagination\": {             \"page\": 2,             \"per_page\": 25,             \"previous_page\": 1,             \"next_page\": 3,             \"last_page\": 4,             \"total_entries\": 100         }     } } ```  The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header**  ```http Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",       <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",       <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\" ```  Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.  ## Rate Limiting  All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  - The `RateLimit-Limit` header contains the total number of requests you can perform per hour. - The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame. - The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata  Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | | ----------------- | ------ | ------------------------------------------------------------ | | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata ```  ```yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central ```  **Example: Hostname**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server ```  **Example: Instance ID**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 ```  **Example: Public IPv4**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 ```  **Example: Private Networks**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks ```  ```yaml - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 ```  **Example: Availability Zone**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 ```  **Example: Region**  ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central ```  ## Sorting  Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.  **Example: Sorting**  ``` https://api.hetzner.cloud/v1/actions?sort=status https://api.hetzner.cloud/v1/actions?sort=status:asc https://api.hetzner.cloud/v1/actions?sort=status:desc https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc ```  ## Deprecation Notices  You can find all announced deprecations in our [Changelog](https://docs.hetzner.cloud). 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from hetzner_python_sdk import schemas  # noqa: F401


class ServersGetServerResponseServer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "image",
            "iso",
            "created",
            "private_net",
            "datacenter",
            "protection",
            "backup_window",
            "ingoing_traffic",
            "included_traffic",
            "public_net",
            "labels",
            "outgoing_traffic",
            "rescue_enabled",
            "name",
            "id",
            "locked",
            "primary_disk_size",
            "server_type",
            "status",
        }
        
        class properties:
            
            
            class backup_window(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'backup_window':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            created = schemas.StrSchema
        
            @staticmethod
            def datacenter() -> typing.Type['ServersGetServerResponseServerDatacenter']:
                return ServersGetServerResponseServerDatacenter
            
            
            class id(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 9007199254740991
        
            @staticmethod
            def image() -> typing.Type['ServersGetServerResponseServerImage']:
                return ServersGetServerResponseServerImage
            
            
            class included_traffic(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'included_traffic':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ingoing_traffic(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ingoing_traffic':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def iso() -> typing.Type['ServersGetServerResponseServerIso']:
                return ServersGetServerResponseServerIso
        
            @staticmethod
            def labels() -> typing.Type['ServersGetServerResponseServerLabels']:
                return ServersGetServerResponseServerLabels
            locked = schemas.BoolSchema
            name = schemas.StrSchema
            
            
            class outgoing_traffic(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'outgoing_traffic':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            primary_disk_size = schemas.NumberSchema
        
            @staticmethod
            def private_net() -> typing.Type['ServersGetServerResponseServerPrivateNet']:
                return ServersGetServerResponseServerPrivateNet
        
            @staticmethod
            def protection() -> typing.Type['ServersGetServerResponseServerProtection']:
                return ServersGetServerResponseServerProtection
        
            @staticmethod
            def public_net() -> typing.Type['ServersGetServerResponseServerPublicNet']:
                return ServersGetServerResponseServerPublicNet
            rescue_enabled = schemas.BoolSchema
        
            @staticmethod
            def server_type() -> typing.Type['ServersGetServerResponseServerServerType']:
                return ServersGetServerResponseServerServerType
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "running": "RUNNING",
                        "initializing": "INITIALIZING",
                        "starting": "STARTING",
                        "stopping": "STOPPING",
                        "false": "FALSE",
                        "deleting": "DELETING",
                        "migrating": "MIGRATING",
                        "rebuilding": "REBUILDING",
                        "unknown": "UNKNOWN",
                    }
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("running")
                
                @schemas.classproperty
                def INITIALIZING(cls):
                    return cls("initializing")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("starting")
                
                @schemas.classproperty
                def STOPPING(cls):
                    return cls("stopping")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("deleting")
                
                @schemas.classproperty
                def MIGRATING(cls):
                    return cls("migrating")
                
                @schemas.classproperty
                def REBUILDING(cls):
                    return cls("rebuilding")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
        
            @staticmethod
            def load_balancers() -> typing.Type['ServersGetServerResponseServerLoadBalancers']:
                return ServersGetServerResponseServerLoadBalancers
        
            @staticmethod
            def placement_group() -> typing.Type['ServersGetServerResponseServerPlacementGroup']:
                return ServersGetServerResponseServerPlacementGroup
        
            @staticmethod
            def volumes() -> typing.Type['ServersGetServerResponseServerVolumes']:
                return ServersGetServerResponseServerVolumes
            __annotations__ = {
                "backup_window": backup_window,
                "created": created,
                "datacenter": datacenter,
                "id": id,
                "image": image,
                "included_traffic": included_traffic,
                "ingoing_traffic": ingoing_traffic,
                "iso": iso,
                "labels": labels,
                "locked": locked,
                "name": name,
                "outgoing_traffic": outgoing_traffic,
                "primary_disk_size": primary_disk_size,
                "private_net": private_net,
                "protection": protection,
                "public_net": public_net,
                "rescue_enabled": rescue_enabled,
                "server_type": server_type,
                "status": status,
                "load_balancers": load_balancers,
                "placement_group": placement_group,
                "volumes": volumes,
            }
    
    image: 'ServersGetServerResponseServerImage'
    iso: 'ServersGetServerResponseServerIso'
    created: MetaOapg.properties.created
    private_net: 'ServersGetServerResponseServerPrivateNet'
    datacenter: 'ServersGetServerResponseServerDatacenter'
    protection: 'ServersGetServerResponseServerProtection'
    backup_window: MetaOapg.properties.backup_window
    ingoing_traffic: MetaOapg.properties.ingoing_traffic
    included_traffic: MetaOapg.properties.included_traffic
    public_net: 'ServersGetServerResponseServerPublicNet'
    labels: 'ServersGetServerResponseServerLabels'
    outgoing_traffic: MetaOapg.properties.outgoing_traffic
    rescue_enabled: MetaOapg.properties.rescue_enabled
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    locked: MetaOapg.properties.locked
    primary_disk_size: MetaOapg.properties.primary_disk_size
    server_type: 'ServersGetServerResponseServerServerType'
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backup_window"]) -> MetaOapg.properties.backup_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datacenter"]) -> 'ServersGetServerResponseServerDatacenter': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> 'ServersGetServerResponseServerImage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["included_traffic"]) -> MetaOapg.properties.included_traffic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ingoing_traffic"]) -> MetaOapg.properties.ingoing_traffic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso"]) -> 'ServersGetServerResponseServerIso': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> 'ServersGetServerResponseServerLabels': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locked"]) -> MetaOapg.properties.locked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outgoing_traffic"]) -> MetaOapg.properties.outgoing_traffic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_disk_size"]) -> MetaOapg.properties.primary_disk_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private_net"]) -> 'ServersGetServerResponseServerPrivateNet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protection"]) -> 'ServersGetServerResponseServerProtection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_net"]) -> 'ServersGetServerResponseServerPublicNet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rescue_enabled"]) -> MetaOapg.properties.rescue_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_type"]) -> 'ServersGetServerResponseServerServerType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["load_balancers"]) -> 'ServersGetServerResponseServerLoadBalancers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placement_group"]) -> 'ServersGetServerResponseServerPlacementGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumes"]) -> 'ServersGetServerResponseServerVolumes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["backup_window", "created", "datacenter", "id", "image", "included_traffic", "ingoing_traffic", "iso", "labels", "locked", "name", "outgoing_traffic", "primary_disk_size", "private_net", "protection", "public_net", "rescue_enabled", "server_type", "status", "load_balancers", "placement_group", "volumes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backup_window"]) -> MetaOapg.properties.backup_window: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datacenter"]) -> 'ServersGetServerResponseServerDatacenter': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> 'ServersGetServerResponseServerImage': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["included_traffic"]) -> MetaOapg.properties.included_traffic: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ingoing_traffic"]) -> MetaOapg.properties.ingoing_traffic: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso"]) -> 'ServersGetServerResponseServerIso': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> 'ServersGetServerResponseServerLabels': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locked"]) -> MetaOapg.properties.locked: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outgoing_traffic"]) -> MetaOapg.properties.outgoing_traffic: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_disk_size"]) -> MetaOapg.properties.primary_disk_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private_net"]) -> 'ServersGetServerResponseServerPrivateNet': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protection"]) -> 'ServersGetServerResponseServerProtection': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_net"]) -> 'ServersGetServerResponseServerPublicNet': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rescue_enabled"]) -> MetaOapg.properties.rescue_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_type"]) -> 'ServersGetServerResponseServerServerType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["load_balancers"]) -> typing.Union['ServersGetServerResponseServerLoadBalancers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placement_group"]) -> typing.Union['ServersGetServerResponseServerPlacementGroup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumes"]) -> typing.Union['ServersGetServerResponseServerVolumes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["backup_window", "created", "datacenter", "id", "image", "included_traffic", "ingoing_traffic", "iso", "labels", "locked", "name", "outgoing_traffic", "primary_disk_size", "private_net", "protection", "public_net", "rescue_enabled", "server_type", "status", "load_balancers", "placement_group", "volumes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image: 'ServersGetServerResponseServerImage',
        iso: 'ServersGetServerResponseServerIso',
        created: typing.Union[MetaOapg.properties.created, str, ],
        private_net: 'ServersGetServerResponseServerPrivateNet',
        datacenter: 'ServersGetServerResponseServerDatacenter',
        protection: 'ServersGetServerResponseServerProtection',
        backup_window: typing.Union[MetaOapg.properties.backup_window, None, str, ],
        ingoing_traffic: typing.Union[MetaOapg.properties.ingoing_traffic, None, decimal.Decimal, int, ],
        included_traffic: typing.Union[MetaOapg.properties.included_traffic, None, decimal.Decimal, int, ],
        public_net: 'ServersGetServerResponseServerPublicNet',
        labels: 'ServersGetServerResponseServerLabels',
        outgoing_traffic: typing.Union[MetaOapg.properties.outgoing_traffic, None, decimal.Decimal, int, ],
        rescue_enabled: typing.Union[MetaOapg.properties.rescue_enabled, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        locked: typing.Union[MetaOapg.properties.locked, bool, ],
        primary_disk_size: typing.Union[MetaOapg.properties.primary_disk_size, decimal.Decimal, int, float, ],
        server_type: 'ServersGetServerResponseServerServerType',
        status: typing.Union[MetaOapg.properties.status, str, ],
        load_balancers: typing.Union['ServersGetServerResponseServerLoadBalancers', schemas.Unset] = schemas.unset,
        placement_group: typing.Union['ServersGetServerResponseServerPlacementGroup', schemas.Unset] = schemas.unset,
        volumes: typing.Union['ServersGetServerResponseServerVolumes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServersGetServerResponseServer':
        return super().__new__(
            cls,
            *args,
            image=image,
            iso=iso,
            created=created,
            private_net=private_net,
            datacenter=datacenter,
            protection=protection,
            backup_window=backup_window,
            ingoing_traffic=ingoing_traffic,
            included_traffic=included_traffic,
            public_net=public_net,
            labels=labels,
            outgoing_traffic=outgoing_traffic,
            rescue_enabled=rescue_enabled,
            name=name,
            id=id,
            locked=locked,
            primary_disk_size=primary_disk_size,
            server_type=server_type,
            status=status,
            load_balancers=load_balancers,
            placement_group=placement_group,
            volumes=volumes,
            _configuration=_configuration,
            **kwargs,
        )

from hetzner_python_sdk.model.servers_get_server_response_server_datacenter import ServersGetServerResponseServerDatacenter
from hetzner_python_sdk.model.servers_get_server_response_server_image import ServersGetServerResponseServerImage
from hetzner_python_sdk.model.servers_get_server_response_server_iso import ServersGetServerResponseServerIso
from hetzner_python_sdk.model.servers_get_server_response_server_labels import ServersGetServerResponseServerLabels
from hetzner_python_sdk.model.servers_get_server_response_server_load_balancers import ServersGetServerResponseServerLoadBalancers
from hetzner_python_sdk.model.servers_get_server_response_server_placement_group import ServersGetServerResponseServerPlacementGroup
from hetzner_python_sdk.model.servers_get_server_response_server_private_net import ServersGetServerResponseServerPrivateNet
from hetzner_python_sdk.model.servers_get_server_response_server_protection import ServersGetServerResponseServerProtection
from hetzner_python_sdk.model.servers_get_server_response_server_public_net import ServersGetServerResponseServerPublicNet
from hetzner_python_sdk.model.servers_get_server_response_server_server_type import ServersGetServerResponseServerServerType
from hetzner_python_sdk.model.servers_get_server_response_server_volumes import ServersGetServerResponseServerVolumes
