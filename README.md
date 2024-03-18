<div align="left">

[![Visit Hetzner](./header.png)](https://hetzner.com)

# Hetzner<a id="hetzner"></a>

This is the official documentation for the Hetzner Cloud API.

## Introduction<a id="introduction"></a>

The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.

As an alternative to working directly with our API you may also consider to use:

- Our CLI program [hcloud](https://github.com/hetznercloud/cli)
- Our [library for Go](https://github.com/hetznercloud/hcloud-go)
- Our [library for Python](https://github.com/hetznercloud/hcloud-python)

Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).

If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following:

- The type of integration you would like to develop
- Link to the GitHub repo you will use for the Project
- Link to some other Open Source work you have already done (if you have done so)

## Getting Started<a id="getting-started"></a>

To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj`.

You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.se/).

Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud).

**Example Request**

```bash
curl -H \"Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj\" \\
  https://api.hetzner.cloud/v1/servers
```

**Example Response**

```json
{
  \"servers\": [],
  \"meta\": {
    \"pagination\": {
      \"page\": 1,
      \"per_page\": 25,
      \"previous_page\": null,
      \"next_page\": null,
      \"last_page\": 1,
      \"total_entries\": 0
    }
  }
}
```

## Authentication<a id="authentication"></a>

All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.

To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.

**Example Authorization header**

```http
Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj
```

## Errors<a id="errors"></a>

Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.

The error response contains the following keys:

| Keys      | Meaning                                                               |
| --------- | --------------------------------------------------------------------- |
| `code`    | Short string indicating the type of error (machine-parsable)          |
| `message` | Textual description on what has gone wrong                            |
| `details` | An object providing for details on the error (schema depends on code) |

**Example response**

```json
{
  \"error\": {
    \"code\": \"invalid_input\",
    \"message\": \"invalid input in field 'broken_field': is too long\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"broken_field\",
          \"messages\": [\"is too long\"]
        }
      ]
    }
  }
}
```

### Error Codes<a id="error-codes"></a>

| Code                      | Description                                                                      |
| ------------------------- | -------------------------------------------------------------------------------- |
| `forbidden`               | Insufficient permissions for this request                                        |
| `unauthorized`            | Request was made with an invalid or unknown token                                |
| `invalid_input`           | Error while parsing or processing the input                                      |
| `json_error`              | Invalid JSON input in your request                                               |
| `locked`                  | The item you are trying to access is locked (there is already an Action running) |
| `not_found`               | Entity not found                                                                 |
| `rate_limit_exceeded`     | Error when sending too many requests                                             |
| `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           |
| `resource_unavailable`    | The requested resource is currently unavailable                                  |
| `server_error`            | Error within the API backend                                                     |
| `service_error`           | Error within a service                                                           |
| `uniqueness_error`        | One or more of the objects fields must be unique                                 |
| `protected`               | The Action you are trying to start is protected for this resource                |
| `maintenance`             | Cannot perform operation due to maintenance                                      |
| `conflict`                | The resource has changed during the request, please retry                        |
| `unsupported_error`       | The corresponding resource does not support the Action                           |
| `token_readonly`          | The token is only allowed to perform GET requests                                |
| `unavailable`             | A service or product is currently not available                                  |

**invalid_input**

```json
{
  \"error\": {
    \"code\": \"invalid_input\",
    \"message\": \"invalid input in field 'broken_field': is too long\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"broken_field\",
          \"messages\": [\"is too long\"]
        }
      ]
    }
  }
}
```

**uniqueness_error**

```json
{
  \"error\": {
    \"code\": \"uniqueness_error\",
    \"message\": \"SSH key with the same fingerprint already exists\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"public_key\"
        }
      ]
    }
  }
}
```

**resource_limit_exceeded**

```json
{
  \"error\": {
    \"code\": \"resource_limit_exceeded\",
    \"message\": \"project limit exceeded\",
    \"details\": {
      \"limits\": [
        {
          \"name\": \"project_limit\"
        }
      ]
    }
  }
}
```

## Labels<a id="labels"></a>

Labels are `key/value` pairs that can be attached to all resources.

Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.

The `hetzner.cloud/` prefix is reserved and cannot be used.

**Example Labels**

```json
{
  \"labels\": {
    \"environment\": \"development\",
    \"service\": \"backend\",
    \"example.com/my\": \"label\",
    \"just-a-key\": \"\"
  }
}
```

## Label Selector<a id="label-selector"></a>

For resources with labels, you can filter resources by their labels using the label selector query language.

| Expression           | Meaning                                              |
| -------------------- | ---------------------------------------------------- |
| `k==v` / `k=v`       | Value of key `k` does equal value `v`                |
| `k!=v`               | Value of key `k` does not equal value `v`            |
| `k`                  | Key `k` is present                                   |
| `!k`                 | Key `k` is not present                               |
| `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`              |
| `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3` |
| `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present |

### Examples<a id="examples"></a>

- Returns all resources that have a `env=production` label and that don't have a `type=database` label:

  `env=production,type!=database`

- Returns all resources that have a `env=testing` or `env=staging` label:

  `env in (testing,staging)`

- Returns all resources that don't have a `type` label:

  `!type`

## Pagination<a id="pagination"></a>

Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:

- A `page` parameter specifies the page to fetch. The number of the first page is 1.
- A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.

Responses contain a `Link` header with pagination information.

Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:

**Example Pagination**

```json
{
    \"servers\": [...],
    \"meta\": {
        \"pagination\": {
            \"page\": 2,
            \"per_page\": 25,
            \"previous_page\": 1,
            \"next_page\": 3,
            \"last_page\": 4,
            \"total_entries\": 100
        }
    }
}
```

The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.

**Example Pagination Link header**

```http
Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",
      <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",
      <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\"
```

Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.

## Rate Limiting<a id="rate-limiting"></a>

All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.

- The `RateLimit-Limit` header contains the total number of requests you can perform per hour.
- The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame.
- The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.

The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.

## Server Metadata<a id="server-metadata"></a>

Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:

| Data              | Format | Contents                                                     |
| ----------------- | ------ | ------------------------------------------------------------ |
| hostname          | text   | Name of the Server as set in the api                         |
| instance-id       | number | ID of the server                                             |
| public-ipv4       | text   | Primary public IPv4 address                                  |
| private-networks  | yaml   | Details about the private networks the Server is attached to |
| availability-zone | text   | Name of the availability zone that Server runs in            |
| region            | text   | Network zone, e.g. eu-central                                |

**Example: Summary**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata
```

```yaml
availability-zone: hel1-dc2
hostname: my-server
instance-id: 42
public-ipv4: 1.2.3.4
region: eu-central
```

**Example: Hostname**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/hostname
my-server
```

**Example: Instance ID**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/instance-id
42
```

**Example: Public IPv4**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4
1.2.3.4
```

**Example: Private Networks**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/private-networks
```

```yaml
- ip: 10.0.0.2
  alias_ips: [10.0.0.3, 10.0.0.4]
  interface_num: 1
  mac_address: 86:00:00:2a:7d:e0
  network_id: 1234
  network_name: nw-test1
  network: 10.0.0.0/8
  subnet: 10.0.0.0/24
  gateway: 10.0.0.1
- ip: 192.168.0.2
  alias_ips: []
  interface_num: 2
  mac_address: 86:00:00:2a:7d:e1
  network_id: 4321
  network_name: nw-test2
  network: 192.168.0.0/16
  subnet: 192.168.0.0/24
  gateway: 192.168.0.1
```

**Example: Availability Zone**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone
hel1-dc2
```

**Example: Region**

```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/region
eu-central
```

## Sorting<a id="sorting"></a>

Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.

**Example: Sorting**

```
https://api.hetzner.cloud/v1/actions?sort=status
https://api.hetzner.cloud/v1/actions?sort=status:asc
https://api.hetzner.cloud/v1/actions?sort=status:desc
https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc
```

## Deprecation Notices<a id="deprecation-notices"></a>

You can find all announced deprecations in our [Changelog](https://docs.hetzner.cloud).



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`hetzner.actions.get_all`](#hetzneractionsget_all)
  * [`hetzner.actions.get_by_id`](#hetzneractionsget_by_id)
  * [`hetzner.certificate_actions.get_action`](#hetznercertificate_actionsget_action)
  * [`hetzner.certificate_actions.get_action_by_id`](#hetznercertificate_actionsget_action_by_id)
  * [`hetzner.certificate_actions.get_all_actions`](#hetznercertificate_actionsget_all_actions)
  * [`hetzner.certificate_actions.get_all_actions_0`](#hetznercertificate_actionsget_all_actions_0)
  * [`hetzner.certificate_actions.retry_issuance_or_renewal`](#hetznercertificate_actionsretry_issuance_or_renewal)
  * [`hetzner.certificates.create_new_certificate`](#hetznercertificatescreate_new_certificate)
  * [`hetzner.certificates.delete_certificate`](#hetznercertificatesdelete_certificate)
  * [`hetzner.certificates.get_all`](#hetznercertificatesget_all)
  * [`hetzner.certificates.get_by_id`](#hetznercertificatesget_by_id)
  * [`hetzner.certificates.update_by_id`](#hetznercertificatesupdate_by_id)
  * [`hetzner.datacenters.get_all`](#hetznerdatacentersget_all)
  * [`hetzner.datacenters.get_by_id`](#hetznerdatacentersget_by_id)
  * [`hetzner.firewall_actions.apply_to_resources`](#hetznerfirewall_actionsapply_to_resources)
  * [`hetzner.firewall_actions.get_action_by_id`](#hetznerfirewall_actionsget_action_by_id)
  * [`hetzner.firewall_actions.get_action_by_id_0`](#hetznerfirewall_actionsget_action_by_id_0)
  * [`hetzner.firewall_actions.get_all_actions`](#hetznerfirewall_actionsget_all_actions)
  * [`hetzner.firewall_actions.get_all_actions_0`](#hetznerfirewall_actionsget_all_actions_0)
  * [`hetzner.firewall_actions.remove_from_resources`](#hetznerfirewall_actionsremove_from_resources)
  * [`hetzner.firewall_actions.set_rules`](#hetznerfirewall_actionsset_rules)
  * [`hetzner.firewalls.create_firewall`](#hetznerfirewallscreate_firewall)
  * [`hetzner.firewalls.delete_firewall_by_id`](#hetznerfirewallsdelete_firewall_by_id)
  * [`hetzner.firewalls.get_firewall_by_id`](#hetznerfirewallsget_firewall_by_id)
  * [`hetzner.firewalls.list_all`](#hetznerfirewallslist_all)
  * [`hetzner.firewalls.update_firewall_by_id`](#hetznerfirewallsupdate_firewall_by_id)
  * [`hetzner.floating_ip_actions.assign_to_server`](#hetznerfloating_ip_actionsassign_to_server)
  * [`hetzner.floating_ip_actions.change_dns_ptr`](#hetznerfloating_ip_actionschange_dns_ptr)
  * [`hetzner.floating_ip_actions.change_protection`](#hetznerfloating_ip_actionschange_protection)
  * [`hetzner.floating_ip_actions.get_action_by_id`](#hetznerfloating_ip_actionsget_action_by_id)
  * [`hetzner.floating_ip_actions.get_action_by_id_0`](#hetznerfloating_ip_actionsget_action_by_id_0)
  * [`hetzner.floating_ip_actions.get_all_actions`](#hetznerfloating_ip_actionsget_all_actions)
  * [`hetzner.floating_ip_actions.get_all_actions_0`](#hetznerfloating_ip_actionsget_all_actions_0)
  * [`hetzner.floating_ip_actions.unassign_ip`](#hetznerfloating_ip_actionsunassign_ip)
  * [`hetzner.floating_ips.create_new_ip`](#hetznerfloating_ipscreate_new_ip)
  * [`hetzner.floating_ips.delete_ip`](#hetznerfloating_ipsdelete_ip)
  * [`hetzner.floating_ips.get`](#hetznerfloating_ipsget)
  * [`hetzner.floating_ips.get_all`](#hetznerfloating_ipsget_all)
  * [`hetzner.floating_ips.update_description_labels`](#hetznerfloating_ipsupdate_description_labels)
  * [`hetzner.isos.get`](#hetznerisosget)
  * [`hetzner.isos.get_all`](#hetznerisosget_all)
  * [`hetzner.image_actions.change_protection`](#hetznerimage_actionschange_protection)
  * [`hetzner.image_actions.get_action_by_id`](#hetznerimage_actionsget_action_by_id)
  * [`hetzner.image_actions.get_action_by_id_0`](#hetznerimage_actionsget_action_by_id_0)
  * [`hetzner.image_actions.get_all_actions`](#hetznerimage_actionsget_all_actions)
  * [`hetzner.image_actions.get_all_actions_0`](#hetznerimage_actionsget_all_actions_0)
  * [`hetzner.images.delete_image`](#hetznerimagesdelete_image)
  * [`hetzner.images.get_all`](#hetznerimagesget_all)
  * [`hetzner.images.get_by_id`](#hetznerimagesget_by_id)
  * [`hetzner.images.update_image_by_id`](#hetznerimagesupdate_image_by_id)
  * [`hetzner.load_balancer_actions.add_service`](#hetznerload_balancer_actionsadd_service)
  * [`hetzner.load_balancer_actions.add_target`](#hetznerload_balancer_actionsadd_target)
  * [`hetzner.load_balancer_actions.attach_to_network`](#hetznerload_balancer_actionsattach_to_network)
  * [`hetzner.load_balancer_actions.change_algorithm`](#hetznerload_balancer_actionschange_algorithm)
  * [`hetzner.load_balancer_actions.change_dns_ptr`](#hetznerload_balancer_actionschange_dns_ptr)
  * [`hetzner.load_balancer_actions.change_protection`](#hetznerload_balancer_actionschange_protection)
  * [`hetzner.load_balancer_actions.change_type`](#hetznerload_balancer_actionschange_type)
  * [`hetzner.load_balancer_actions.delete_service`](#hetznerload_balancer_actionsdelete_service)
  * [`hetzner.load_balancer_actions.detach_from_network`](#hetznerload_balancer_actionsdetach_from_network)
  * [`hetzner.load_balancer_actions.disable_public_interface`](#hetznerload_balancer_actionsdisable_public_interface)
  * [`hetzner.load_balancer_actions.enable_public_interface`](#hetznerload_balancer_actionsenable_public_interface)
  * [`hetzner.load_balancer_actions.get_all_actions`](#hetznerload_balancer_actionsget_all_actions)
  * [`hetzner.load_balancer_actions.get_all_actions_0`](#hetznerload_balancer_actionsget_all_actions_0)
  * [`hetzner.load_balancer_actions.get_specific_action`](#hetznerload_balancer_actionsget_specific_action)
  * [`hetzner.load_balancer_actions.get_specific_action_0`](#hetznerload_balancer_actionsget_specific_action_0)
  * [`hetzner.load_balancer_actions.remove_target`](#hetznerload_balancer_actionsremove_target)
  * [`hetzner.load_balancer_actions.update_service`](#hetznerload_balancer_actionsupdate_service)
  * [`hetzner.load_balancer_types.get_all_types`](#hetznerload_balancer_typesget_all_types)
  * [`hetzner.load_balancer_types.get_by_id`](#hetznerload_balancer_typesget_by_id)
  * [`hetzner.load_balancers.create_load_balancer`](#hetznerload_balancerscreate_load_balancer)
  * [`hetzner.load_balancers.delete_load_balancer`](#hetznerload_balancersdelete_load_balancer)
  * [`hetzner.load_balancers.get_all`](#hetznerload_balancersget_all)
  * [`hetzner.load_balancers.get_by_id`](#hetznerload_balancersget_by_id)
  * [`hetzner.load_balancers.get_metrics`](#hetznerload_balancersget_metrics)
  * [`hetzner.load_balancers.update_balancer`](#hetznerload_balancersupdate_balancer)
  * [`hetzner.locations.get_all_locations`](#hetznerlocationsget_all_locations)
  * [`hetzner.locations.get_location_by_id`](#hetznerlocationsget_location_by_id)
  * [`hetzner.network_actions.add_route`](#hetznernetwork_actionsadd_route)
  * [`hetzner.network_actions.add_subnet`](#hetznernetwork_actionsadd_subnet)
  * [`hetzner.network_actions.change_ip_range`](#hetznernetwork_actionschange_ip_range)
  * [`hetzner.network_actions.change_protection`](#hetznernetwork_actionschange_protection)
  * [`hetzner.network_actions.delete_route`](#hetznernetwork_actionsdelete_route)
  * [`hetzner.network_actions.delete_subnet`](#hetznernetwork_actionsdelete_subnet)
  * [`hetzner.network_actions.get_action`](#hetznernetwork_actionsget_action)
  * [`hetzner.network_actions.get_action_0`](#hetznernetwork_actionsget_action_0)
  * [`hetzner.network_actions.get_all_actions`](#hetznernetwork_actionsget_all_actions)
  * [`hetzner.network_actions.get_all_actions_0`](#hetznernetwork_actionsget_all_actions_0)
  * [`hetzner.networks.create_network`](#hetznernetworkscreate_network)
  * [`hetzner.networks.delete_network`](#hetznernetworksdelete_network)
  * [`hetzner.networks.get_all`](#hetznernetworksget_all)
  * [`hetzner.networks.get_by_id`](#hetznernetworksget_by_id)
  * [`hetzner.networks.update_properties`](#hetznernetworksupdate_properties)
  * [`hetzner.placement_groups.create_new_group`](#hetznerplacement_groupscreate_new_group)
  * [`hetzner.placement_groups.delete_group`](#hetznerplacement_groupsdelete_group)
  * [`hetzner.placement_groups.get_all`](#hetznerplacement_groupsget_all)
  * [`hetzner.placement_groups.get_by_id`](#hetznerplacement_groupsget_by_id)
  * [`hetzner.placement_groups.update_properties`](#hetznerplacement_groupsupdate_properties)
  * [`hetzner.pricing.get_all_prices`](#hetznerpricingget_all_prices)
  * [`hetzner.primary_ip_actions.assign_primary_ip_to_resource`](#hetznerprimary_ip_actionsassign_primary_ip_to_resource)
  * [`hetzner.primary_ip_actions.change_dns_ptr`](#hetznerprimary_ip_actionschange_dns_ptr)
  * [`hetzner.primary_ip_actions.change_protection_primary_ip`](#hetznerprimary_ip_actionschange_protection_primary_ip)
  * [`hetzner.primary_ip_actions.get_action_by_id`](#hetznerprimary_ip_actionsget_action_by_id)
  * [`hetzner.primary_ip_actions.get_all_actions`](#hetznerprimary_ip_actionsget_all_actions)
  * [`hetzner.primary_ip_actions.unassign_primary_ip`](#hetznerprimary_ip_actionsunassign_primary_ip)
  * [`hetzner.primary_ips.create_or_update`](#hetznerprimary_ipscreate_or_update)
  * [`hetzner.primary_ips.delete_primary_ip`](#hetznerprimary_ipsdelete_primary_ip)
  * [`hetzner.primary_ips.get_all`](#hetznerprimary_ipsget_all)
  * [`hetzner.primary_ips.get_by_id`](#hetznerprimary_ipsget_by_id)
  * [`hetzner.primary_ips.update_ip_labels`](#hetznerprimary_ipsupdate_ip_labels)
  * [`hetzner.ssh_keys.create_key`](#hetznerssh_keyscreate_key)
  * [`hetzner.ssh_keys.delete_key`](#hetznerssh_keysdelete_key)
  * [`hetzner.ssh_keys.get_all_ssh_keys`](#hetznerssh_keysget_all_ssh_keys)
  * [`hetzner.ssh_keys.get_by_id`](#hetznerssh_keysget_by_id)
  * [`hetzner.ssh_keys.update_key`](#hetznerssh_keysupdate_key)
  * [`hetzner.server_actions.add_to_placement_group`](#hetznerserver_actionsadd_to_placement_group)
  * [`hetzner.server_actions.attach_iso_to_server`](#hetznerserver_actionsattach_iso_to_server)
  * [`hetzner.server_actions.attach_to_network`](#hetznerserver_actionsattach_to_network)
  * [`hetzner.server_actions.change_alias_ips`](#hetznerserver_actionschange_alias_ips)
  * [`hetzner.server_actions.change_dns_ptr`](#hetznerserver_actionschange_dns_ptr)
  * [`hetzner.server_actions.change_protection`](#hetznerserver_actionschange_protection)
  * [`hetzner.server_actions.change_server_type`](#hetznerserver_actionschange_server_type)
  * [`hetzner.server_actions.create_image`](#hetznerserver_actionscreate_image)
  * [`hetzner.server_actions.detach_from_network`](#hetznerserver_actionsdetach_from_network)
  * [`hetzner.server_actions.detach_iso_from_server`](#hetznerserver_actionsdetach_iso_from_server)
  * [`hetzner.server_actions.disable_backup`](#hetznerserver_actionsdisable_backup)
  * [`hetzner.server_actions.disable_rescue_mode`](#hetznerserver_actionsdisable_rescue_mode)
  * [`hetzner.server_actions.enable_backup`](#hetznerserver_actionsenable_backup)
  * [`hetzner.server_actions.enable_rescue_mode`](#hetznerserver_actionsenable_rescue_mode)
  * [`hetzner.server_actions.get_action_by_id`](#hetznerserver_actionsget_action_by_id)
  * [`hetzner.server_actions.get_action_by_id_0`](#hetznerserver_actionsget_action_by_id_0)
  * [`hetzner.server_actions.get_all`](#hetznerserver_actionsget_all)
  * [`hetzner.server_actions.get_all_actions`](#hetznerserver_actionsget_all_actions)
  * [`hetzner.server_actions.graceful_shutdown`](#hetznerserver_actionsgraceful_shutdown)
  * [`hetzner.server_actions.power_off_server`](#hetznerserver_actionspower_off_server)
  * [`hetzner.server_actions.power_on_server`](#hetznerserver_actionspower_on_server)
  * [`hetzner.server_actions.rebuild_server_from_image`](#hetznerserver_actionsrebuild_server_from_image)
  * [`hetzner.server_actions.remove_from_placement_group`](#hetznerserver_actionsremove_from_placement_group)
  * [`hetzner.server_actions.request_console`](#hetznerserver_actionsrequest_console)
  * [`hetzner.server_actions.reset_server`](#hetznerserver_actionsreset_server)
  * [`hetzner.server_actions.reset_server_password`](#hetznerserver_actionsreset_server_password)
  * [`hetzner.server_actions.soft_reboot_server`](#hetznerserver_actionssoft_reboot_server)
  * [`hetzner.server_types.get_server_type`](#hetznerserver_typesget_server_type)
  * [`hetzner.server_types.list_all_server_types`](#hetznerserver_typeslist_all_server_types)
  * [`hetzner.servers.create_server_action`](#hetznerserverscreate_server_action)
  * [`hetzner.servers.delete_server`](#hetznerserversdelete_server)
  * [`hetzner.servers.get_all`](#hetznerserversget_all)
  * [`hetzner.servers.get_metrics_for_server`](#hetznerserversget_metrics_for_server)
  * [`hetzner.servers.get_server`](#hetznerserversget_server)
  * [`hetzner.servers.update_server`](#hetznerserversupdate_server)
  * [`hetzner.volume_actions.attach_volume_to_server`](#hetznervolume_actionsattach_volume_to_server)
  * [`hetzner.volume_actions.change_protection_volume`](#hetznervolume_actionschange_protection_volume)
  * [`hetzner.volume_actions.change_size`](#hetznervolume_actionschange_size)
  * [`hetzner.volume_actions.detach_volume_from_server`](#hetznervolume_actionsdetach_volume_from_server)
  * [`hetzner.volume_actions.get_action`](#hetznervolume_actionsget_action)
  * [`hetzner.volume_actions.get_action_by_id`](#hetznervolume_actionsget_action_by_id)
  * [`hetzner.volume_actions.get_all_actions`](#hetznervolume_actionsget_all_actions)
  * [`hetzner.volume_actions.get_all_actions_0`](#hetznervolume_actionsget_all_actions_0)
  * [`hetzner.volumes.create_volume`](#hetznervolumescreate_volume)
  * [`hetzner.volumes.delete_volume`](#hetznervolumesdelete_volume)
  * [`hetzner.volumes.get_all`](#hetznervolumesget_all)
  * [`hetzner.volumes.get_by_id`](#hetznervolumesget_by_id)
  * [`hetzner.volumes.update_volume_properties`](#hetznervolumesupdate_volume_properties)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Hetzner&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from hetzner_python_sdk import Hetzner, ApiException

hetzner = Hetzner(access_token="YOUR_BEARER_TOKEN")

try:
    # Get all Actions
    get_all_response = hetzner.actions.get_all(
        id=42,
        sort="id",
        status="running",
        page=2,
        per_page=25,
    )
    print(get_all_response)
except ApiException as e:
    print("Exception when calling ActionsApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from hetzner_python_sdk import Hetzner, ApiException

hetzner = Hetzner(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Get all Actions
        get_all_response = await hetzner.actions.aget_all(
            id=42,
            sort="id",
            status="running",
            page=2,
            per_page=25,
        )
        print(get_all_response)
    except ApiException as e:
        print("Exception when calling ActionsApi.get_all: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from hetzner_python_sdk import Hetzner, ApiException

hetzner = Hetzner(access_token="YOUR_BEARER_TOKEN")

try:
    # Get all Actions
    get_all_response = hetzner.actions.raw.get_all(
        id=42,
        sort="id",
        status="running",
        page=2,
        per_page=25,
    )
    pprint(get_all_response.body)
    pprint(get_all_response.body["actions"])
    pprint(get_all_response.body["meta"])
    pprint(get_all_response.headers)
    pprint(get_all_response.status)
    pprint(get_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActionsApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `hetzner.actions.get_all`<a id="hetzneractionsget_all"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.actions.get_all(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetAllResponse`](./hetzner_python_sdk/pydantic/actions_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.actions.get_by_id`<a id="hetzneractionsget_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.actions.get_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetByIdResponse`](./hetzner_python_sdk/pydantic/actions_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificate_actions.get_action`<a id="hetznercertificate_actionsget_action"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_response = hetzner.certificate_actions.get_action(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`CertificateActionsGetActionResponse`](./hetzner_python_sdk/pydantic/certificate_actions_get_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificate_actions.get_action_by_id`<a id="hetznercertificate_actionsget_action_by_id"></a>

Returns a specific Action for a Certificate. Only type `managed` Certificates have Actions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.certificate_actions.get_action_by_id(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Certificate

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`CertificateActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/certificate_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificate_actions.get_all_actions`<a id="hetznercertificate_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.certificate_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`CertificateActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/certificate_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificate_actions.get_all_actions_0`<a id="hetznercertificate_actionsget_all_actions_0"></a>

Returns all Action objects for a Certificate. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

Only type `managed` Certificates can have Actions. For type `uploaded` Certificates the `actions` key will always contain an empty array.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.certificate_actions.get_all_actions_0(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`CertificateActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/certificate_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificate_actions.retry_issuance_or_renewal`<a id="hetznercertificate_actionsretry_issuance_or_renewal"></a>

Retry a failed Certificate issuance or renewal.

Only applicable if the type of the Certificate is `managed` and the issuance or renewal status is `failed`.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                                    | Description                                                               |
|---------------------------------------------------------|---------------------------------------------------------------------------|
| `caa_record_does_not_allow_ca`                          | CAA record does not allow certificate authority                           |
| `ca_dns_validation_failed`                              | Certificate Authority: DNS validation failed                              |
| `ca_too_many_authorizations_failed_recently`            | Certificate Authority: Too many authorizations failed recently            |
| `ca_too_many_certificates_issued_for_registered_domain` | Certificate Authority: Too many certificates issued for registered domain |
| `ca_too_many_duplicate_certificates`                    | Certificate Authority: Too many duplicate certificates                    |
| `could_not_verify_domain_delegated_to_zone`             | Could not verify domain delegated to zone                                 |
| `dns_zone_not_found`                                    | DNS zone not found                                                        |
| `dns_zone_is_secondary_zone`                            | DNS zone is a secondary zone                                              |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retry_issuance_or_renewal_response = (
    hetzner.certificate_actions.retry_issuance_or_renewal(
        id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Certificate

#### 🔄 Return<a id="🔄-return"></a>

[`CertificateActionsRetryIssuanceOrRenewalResponse`](./hetzner_python_sdk/pydantic/certificate_actions_retry_issuance_or_renewal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}/actions/retry` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificates.create_new_certificate`<a id="hetznercertificatescreate_new_certificate"></a>

Creates a new Certificate.

The default type **uploaded** allows for uploading your existing `certificate` and `private_key` in PEM format. You have to monitor its expiration date and handle renewal yourself.

In contrast, type **managed** requests a new Certificate from *Let's Encrypt* for the specified `domain_names`. Only domains managed by *Hetzner DNS* are supported. We handle renewal and timely alert the project owner via email if problems occur.

For type `managed` Certificates the `action` key of the response contains the Action that allows for tracking the issuance process. For type `uploaded` Certificates the `action` is always null.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_certificate_response = hetzner.certificates.create_new_certificate(
    name="my website cert",
    certificate="-----BEGIN CERTIFICATE-----\n...",
    domain_names=["string_example"],
    labels={},
    private_key="-----BEGIN PRIVATE KEY-----\n...",
    type="uploaded",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the Certificate

##### certificate: `str`<a id="certificate-str"></a>

Certificate and chain in PEM format, in order so that each record directly certifies the one preceding. Required for type `uploaded` Certificates.

##### domain_names: [`CertificatesCreateNewCertificateRequestDomainNames`](./hetzner_python_sdk/type/certificates_create_new_certificate_request_domain_names.py)<a id="domain_names-certificatescreatenewcertificaterequestdomainnameshetzner_python_sdktypecertificates_create_new_certificate_request_domain_namespy"></a>

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### private_key: `str`<a id="private_key-str"></a>

Certificate key in PEM format. Required for type `uploaded` Certificates.

##### type: `str`<a id="type-str"></a>

Choose between uploading a Certificate in PEM format or requesting a managed *Let's Encrypt* Certificate.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CertificatesCreateNewCertificateRequest`](./hetzner_python_sdk/type/certificates_create_new_certificate_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CertificatesCreateNewCertificateResponse`](./hetzner_python_sdk/pydantic/certificates_create_new_certificate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificates.delete_certificate`<a id="hetznercertificatesdelete_certificate"></a>

Deletes a Certificate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.certificates.delete_certificate(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificates.get_all`<a id="hetznercertificatesget_all"></a>

Returns all Certificate objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.certificates.get_all(
    sort="id",
    name="string_example",
    label_selector="string_example",
    type="uploaded",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### type: `str`<a id="type-str"></a>

Can be used multiple times. The response will only contain Certificates matching the type.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`CertificatesGetAllResponse`](./hetzner_python_sdk/pydantic/certificates_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificates.get_by_id`<a id="hetznercertificatesget_by_id"></a>

Gets a specific Certificate object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.certificates.get_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🔄 Return<a id="🔄-return"></a>

[`CertificatesGetByIdResponse`](./hetzner_python_sdk/pydantic/certificates_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.certificates.update_by_id`<a id="hetznercertificatesupdate_by_id"></a>

Updates the Certificate properties.

Note that when updating labels, the Certificate’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Certificate object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = hetzner.certificates.update_by_id(
    id=42,
    labels={
        "labelkey": "value",
    },
    name="my website cert",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New Certificate name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CertificatesUpdateByIdRequest`](./hetzner_python_sdk/type/certificates_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CertificatesUpdateByIdResponse`](./hetzner_python_sdk/pydantic/certificates_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.datacenters.get_all`<a id="hetznerdatacentersget_all"></a>

Returns all Datacenter objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.datacenters.get_all(
    name="string_example",
    sort="id",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an `invalid_input` error is returned.

##### sort: `str`<a id="sort-str"></a>

Can be used multiple times.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`DatacentersGetAllResponse`](./hetzner_python_sdk/pydantic/datacenters_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datacenters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.datacenters.get_by_id`<a id="hetznerdatacentersget_by_id"></a>

Returns a specific Datacenter object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.datacenters.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of Datacenter

#### 🔄 Return<a id="🔄-return"></a>

[`DatacentersGetByIdResponse`](./hetzner_python_sdk/pydantic/datacenters_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datacenters/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.apply_to_resources`<a id="hetznerfirewall_actionsapply_to_resources"></a>

Applies one Firewall to multiple resources.

Currently servers (public network interface) and label selectors are supported.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `firewall_already_applied`    | Firewall was already applied on resource                      |
| `incompatible_network_type`   | The Network type is incompatible for the given resource       |
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_to_resources_response = hetzner.firewall_actions.apply_to_resources(
    apply_to=[
        {
            "type": "server",
        }
    ],
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### apply_to: [`FirewallActionsApplyToResourcesRequestApplyTo`](./hetzner_python_sdk/type/firewall_actions_apply_to_resources_request_apply_to.py)<a id="apply_to-firewallactionsapplytoresourcesrequestapplytohetzner_python_sdktypefirewall_actions_apply_to_resources_request_apply_topy"></a>

##### id: `int`<a id="id-int"></a>

ID of the Firewall

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FirewallActionsApplyToResourcesRequest`](./hetzner_python_sdk/type/firewall_actions_apply_to_resources_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsApplyToResourcesResponse`](./hetzner_python_sdk/pydantic/firewall_actions_apply_to_resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}/actions/apply_to_resources` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.get_action_by_id`<a id="hetznerfirewall_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.firewall_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/firewall_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.get_action_by_id_0`<a id="hetznerfirewall_actionsget_action_by_id_0"></a>

Returns a specific Action for a Firewall.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_0_response = hetzner.firewall_actions.get_action_by_id_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Firewall

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsGetActionById200Response`](./hetzner_python_sdk/pydantic/firewall_actions_get_action_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.get_all_actions`<a id="hetznerfirewall_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.firewall_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/firewall_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.get_all_actions_0`<a id="hetznerfirewall_actionsget_all_actions_0"></a>

Returns all Action objects for a Firewall. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.firewall_actions.get_all_actions_0(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/firewall_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.remove_from_resources`<a id="hetznerfirewall_actionsremove_from_resources"></a>

Removes one Firewall from multiple resources.

Currently only Servers (and their public network interfaces) are supported.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                  | Description                                                            |
|---------------------------------------|------------------------------------------------------------------------|
| `firewall_already_removed`            | Firewall was already removed from the resource                         |
| `firewall_resource_not_found`         | The resource the Firewall should be attached to was not found          |
| `firewall_managed_by_label_selector`  | Firewall was applied via label selector and cannot be removed manually |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_resources_response = hetzner.firewall_actions.remove_from_resources(
    remove_from=[
        {
            "type": "server",
        }
    ],
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### remove_from: [`FirewallActionsRemoveFromResourcesRequestRemoveFrom`](./hetzner_python_sdk/type/firewall_actions_remove_from_resources_request_remove_from.py)<a id="remove_from-firewallactionsremovefromresourcesrequestremovefromhetzner_python_sdktypefirewall_actions_remove_from_resources_request_remove_frompy"></a>

##### id: `int`<a id="id-int"></a>

ID of the Firewall

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FirewallActionsRemoveFromResourcesRequest`](./hetzner_python_sdk/type/firewall_actions_remove_from_resources_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsRemoveFromResourcesResponse`](./hetzner_python_sdk/pydantic/firewall_actions_remove_from_resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}/actions/remove_from_resources` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewall_actions.set_rules`<a id="hetznerfirewall_actionsset_rules"></a>

Sets the rules of a Firewall.

All existing rules will be overwritten. Pass an empty `rules` array to remove all rules.
The maximum amount of rules that can be defined is 50.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_rules_response = hetzner.firewall_actions.set_rules(
    rules=[
        {
            "destination_ips": [
                "28.239.13.1/32",
                "28.239.14.0/24",
                "ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128",
            ],
            "direction": "in",
            "port": "80",
            "protocol": "tcp",
            "source_ips": [
                "28.239.13.1/32",
                "28.239.14.0/24",
                "ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128",
            ],
        }
    ],
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rules: [`FirewallActionsSetRulesRequestRules`](./hetzner_python_sdk/type/firewall_actions_set_rules_request_rules.py)<a id="rules-firewallactionssetrulesrequestruleshetzner_python_sdktypefirewall_actions_set_rules_request_rulespy"></a>

##### id: `int`<a id="id-int"></a>

ID of the Firewall

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FirewallActionsSetRulesRequest`](./hetzner_python_sdk/type/firewall_actions_set_rules_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FirewallActionsSetRulesResponse`](./hetzner_python_sdk/pydantic/firewall_actions_set_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}/actions/set_rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewalls.create_firewall`<a id="hetznerfirewallscreate_firewall"></a>

Creates a new Firewall.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_already_added`        | Server added more than one time to resource                   |
| `incompatible_network_type`   | The Network type is incompatible for the given resource       |
| `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_firewall_response = hetzner.firewalls.create_firewall(
    name="Corporate Intranet Protection",
    apply_to=[
        {
            "type": "server",
        }
    ],
    labels={},
    rules=[
        {
            "destination_ips": [
                "28.239.13.1/32",
                "28.239.14.0/24",
                "ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128",
            ],
            "direction": "in",
            "port": "80",
            "protocol": "tcp",
            "source_ips": [
                "28.239.13.1/32",
                "28.239.14.0/24",
                "ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128",
            ],
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the Firewall

##### apply_to: [`FirewallsCreateFirewallRequestApplyTo`](./hetzner_python_sdk/type/firewalls_create_firewall_request_apply_to.py)<a id="apply_to-firewallscreatefirewallrequestapplytohetzner_python_sdktypefirewalls_create_firewall_request_apply_topy"></a>

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### rules: [`FirewallsCreateFirewallRequestRules`](./hetzner_python_sdk/type/firewalls_create_firewall_request_rules.py)<a id="rules-firewallscreatefirewallrequestruleshetzner_python_sdktypefirewalls_create_firewall_request_rulespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FirewallsCreateFirewallRequest`](./hetzner_python_sdk/type/firewalls_create_firewall_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FirewallsCreateFirewallResponse`](./hetzner_python_sdk/pydantic/firewalls_create_firewall_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewalls.delete_firewall_by_id`<a id="hetznerfirewallsdelete_firewall_by_id"></a>

Deletes a Firewall.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                 | Description                               |
|--------------------- |-------------------------------------------|
| `resource_in_use`    | Firewall must not be in use to be deleted |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.firewalls.delete_firewall_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewalls.get_firewall_by_id`<a id="hetznerfirewallsget_firewall_by_id"></a>

Gets a specific Firewall object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_firewall_by_id_response = hetzner.firewalls.get_firewall_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallsGetFirewallByIdResponse`](./hetzner_python_sdk/pydantic/firewalls_get_firewall_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewalls.list_all`<a id="hetznerfirewallslist_all"></a>

Returns all Firewall objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = hetzner.firewalls.list_all(
    sort="id",
    name="string_example",
    label_selector="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FirewallsListAllResponse`](./hetzner_python_sdk/pydantic/firewalls_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.firewalls.update_firewall_by_id`<a id="hetznerfirewallsupdate_firewall_by_id"></a>

Updates the Firewall.

Note that when updating labels, the Firewall's current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Firewall object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_firewall_by_id_response = hetzner.firewalls.update_firewall_by_id(
    id=42,
    labels={
        "labelkey": "value",
    },
    name="new-name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New Firewall name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FirewallsUpdateFirewallByIdRequest`](./hetzner_python_sdk/type/firewalls_update_firewall_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FirewallsUpdateFirewallByIdResponse`](./hetzner_python_sdk/pydantic/firewalls_update_firewall_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/firewalls/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.assign_to_server`<a id="hetznerfloating_ip_actionsassign_to_server"></a>

Assigns a Floating IP to a Server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_to_server_response = hetzner.floating_ip_actions.assign_to_server(
    server=42,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### server: `int`<a id="server-int"></a>

ID of the Server the Floating IP shall be assigned to

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FloatingIpActionsAssignToServerRequest`](./hetzner_python_sdk/type/floating_ip_actions_assign_to_server_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsAssignToServerResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_assign_to_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions/assign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.change_dns_ptr`<a id="hetznerfloating_ip_actionschange_dns_ptr"></a>

Changes the hostname that will appear when getting the hostname belonging to this Floating IP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_dns_ptr_response = hetzner.floating_ip_actions.change_dns_ptr(
    dns_ptr="server02.example.com",
    ip="1.2.3.4",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dns_ptr: `Optional[str]`<a id="dns_ptr-optionalstr"></a>

Hostname to set as a reverse DNS PTR entry, will reset to original default value if `null`

##### ip: `str`<a id="ip-str"></a>

IP address for which to set the reverse DNS entry

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FloatingIpActionsChangeDnsPtrRequest`](./hetzner_python_sdk/type/floating_ip_actions_change_dns_ptr_request.py)
Select the IP address for which to change the DNS entry by passing `ip`. For a Floating IP of type `ipv4` this must exactly match the IP address of the Floating IP. For a Floating IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsChangeDnsPtrResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_change_dns_ptr_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions/change_dns_ptr` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.change_protection`<a id="hetznerfloating_ip_actionschange_protection"></a>

Changes the protection configuration of the Floating IP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_response = hetzner.floating_ip_actions.change_protection(
    id=1,
    delete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Floating IP from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FloatingIpActionsChangeProtectionRequest`](./hetzner_python_sdk/type/floating_ip_actions_change_protection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsChangeProtectionResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_change_protection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.get_action_by_id`<a id="hetznerfloating_ip_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.floating_ip_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.get_action_by_id_0`<a id="hetznerfloating_ip_actionsget_action_by_id_0"></a>

Returns a specific Action object for a Floating IP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_0_response = hetzner.floating_ip_actions.get_action_by_id_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsGetActionById200Response`](./hetzner_python_sdk/pydantic/floating_ip_actions_get_action_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.get_all_actions`<a id="hetznerfloating_ip_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.floating_ip_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.get_all_actions_0`<a id="hetznerfloating_ip_actionsget_all_actions_0"></a>

Returns all Action objects for a Floating IP. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.floating_ip_actions.get_all_actions_0(
    id=1,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/floating_ip_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ip_actions.unassign_ip`<a id="hetznerfloating_ip_actionsunassign_ip"></a>

Unassigns a Floating IP, resulting in it being unreachable. You may assign it to a Server again at a later time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unassign_ip_response = hetzner.floating_ip_actions.unassign_ip(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIpActionsUnassignIpResponse`](./hetzner_python_sdk/pydantic/floating_ip_actions_unassign_ip_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}/actions/unassign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ips.create_new_ip`<a id="hetznerfloating_ipscreate_new_ip"></a>

Creates a new Floating IP assigned to a Server. If you want to create a Floating IP that is not bound to a Server, you need to provide the `home_location` key instead of `server`. This can be either the ID or the name of the Location this IP shall be created in. Note that a Floating IP can be assigned to a Server in any Location later on. For optimal routing it is advised to use the Floating IP in the same Location it was created in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_ip_response = hetzner.floating_ips.create_new_ip(
    type="ipv4",
    description="Web Frontend",
    home_location="fsn1",
    labels={
        "labelkey": "value",
    },
    name="Web Frontend",
    server=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Floating IP type

##### description: `str`<a id="description-str"></a>

##### home_location: `str`<a id="home_location-str"></a>

Home Location (routing is optimized for that Location). Only optional if Server argument is passed.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

##### server: `int`<a id="server-int"></a>

ID of the Server to assign the Floating IP to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FloatingIPsCreateNewIpRequest`](./hetzner_python_sdk/type/floating_ips_create_new_ip_request.py)
The `type` argument is required while `home_location` and `server` are mutually exclusive.

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIPsCreateNewIpResponse`](./hetzner_python_sdk/pydantic/floating_ips_create_new_ip_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ips.delete_ip`<a id="hetznerfloating_ipsdelete_ip"></a>

Deletes a Floating IP. If it is currently assigned to a Server it will automatically get unassigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.floating_ips.delete_ip(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ips.get`<a id="hetznerfloating_ipsget"></a>

Returns a specific Floating IP object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = hetzner.floating_ips.get(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIPsGetResponse`](./hetzner_python_sdk/pydantic/floating_ips_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ips.get_all`<a id="hetznerfloating_ipsget_all"></a>

Returns all Floating IP objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.floating_ips.get_all(
    name="string_example",
    label_selector="string_example",
    sort="id",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### sort: `str`<a id="sort-str"></a>

Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIPsGetAllResponse`](./hetzner_python_sdk/pydantic/floating_ips_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.floating_ips.update_description_labels`<a id="hetznerfloating_ipsupdate_description_labels"></a>

Updates the description or labels of a Floating IP.
Also note that when updating labels, the Floating IP’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_description_labels_response = hetzner.floating_ips.update_description_labels(
    id=1,
    description="Web Frontend",
    labels={
        "labelkey": "value",
    },
    name="Web Frontend",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Floating IP

##### description: `str`<a id="description-str"></a>

New Description to set

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New unique name to set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FloatingIPsUpdateDescriptionLabelsRequest`](./hetzner_python_sdk/type/floating_ips_update_description_labels_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FloatingIPsUpdateDescriptionLabelsResponse`](./hetzner_python_sdk/pydantic/floating_ips_update_description_labels_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/floating_ips/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.isos.get`<a id="hetznerisosget"></a>

Returns a specific ISO object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = hetzner.isos.get(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the ISO

#### 🔄 Return<a id="🔄-return"></a>

[`IsOsGetResponse`](./hetzner_python_sdk/pydantic/is_os_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/isos/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.isos.get_all`<a id="hetznerisosget_all"></a>

Returns all available ISO objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.isos.get_all(
    name="string_example",
    architecture="string_example",
    include_architecture_wildcard=True,
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name.

##### architecture: `str`<a id="architecture-str"></a>

Return only ISOs with the given architecture.

##### include_architecture_wildcard: `bool`<a id="include_architecture_wildcard-bool"></a>

Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`IsOsGetAllResponse`](./hetzner_python_sdk/pydantic/is_os_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/isos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.image_actions.change_protection`<a id="hetznerimage_actionschange_protection"></a>

Changes the protection configuration of the Image. Can only be used on snapshots.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_response = hetzner.image_actions.change_protection(
    id=1,
    delete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the snapshot from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImageActionsChangeProtectionRequest`](./hetzner_python_sdk/type/image_actions_change_protection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImageActionsChangeProtectionResponse`](./hetzner_python_sdk/pydantic/image_actions_change_protection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.image_actions.get_action_by_id`<a id="hetznerimage_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.image_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`ImageActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/image_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.image_actions.get_action_by_id_0`<a id="hetznerimage_actionsget_action_by_id_0"></a>

Returns a specific Action for an Image.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_0_response = hetzner.image_actions.get_action_by_id_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`ImageActionsGetActionById200Response`](./hetzner_python_sdk/pydantic/image_actions_get_action_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.image_actions.get_all_actions`<a id="hetznerimage_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.image_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ImageActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/image_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.image_actions.get_all_actions_0`<a id="hetznerimage_actionsget_all_actions_0"></a>

Returns all Action objects for an Image. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.image_actions.get_all_actions_0(
    id=1,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ImageActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/image_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.images.delete_image`<a id="hetznerimagesdelete_image"></a>

Deletes an Image. Only Images of type `snapshot` and `backup` can be deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.images.delete_image(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.images.get_all`<a id="hetznerimagesget_all"></a>

Returns all Image objects. You can select specific Image types only and sort the results by using URI parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.images.get_all(
    sort="id",
    type="system",
    status="available",
    bound_to="string_example",
    include_deprecated=True,
    name="string_example",
    label_selector="string_example",
    architecture="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### type: `str`<a id="type-str"></a>

Can be used multiple times.

##### status: `str`<a id="status-str"></a>

Can be used multiple times. The response will only contain Images matching the status.

##### bound_to: `str`<a id="bound_to-str"></a>

Can be used multiple times. Server ID linked to the Image. Only available for Images of type `backup`

##### include_deprecated: `bool`<a id="include_deprecated-bool"></a>

Can be used multiple times.

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### architecture: `str`<a id="architecture-str"></a>

Return only Images with the given architecture.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ImagesGetAllResponse`](./hetzner_python_sdk/pydantic/images_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.images.get_by_id`<a id="hetznerimagesget_by_id"></a>

Returns a specific Image object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.images.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

#### 🔄 Return<a id="🔄-return"></a>

[`ImagesGetByIdResponse`](./hetzner_python_sdk/pydantic/images_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.images.update_image_by_id`<a id="hetznerimagesupdate_image_by_id"></a>

Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image or change the Image labels. Only Images of type `snapshot` and `backup` can be updated.

Note that when updating labels, the current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_image_by_id_response = hetzner.images.update_image_by_id(
    id=1,
    description="My new Image description",
    labels={
        "labelkey": "value",
    },
    type="snapshot",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Image

##### description: `str`<a id="description-str"></a>

New description of Image

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### type: `str`<a id="type-str"></a>

Destination Image type to convert to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImagesUpdateImageByIdRequest`](./hetzner_python_sdk/type/images_update_image_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImagesUpdateImageByIdResponse`](./hetzner_python_sdk/pydantic/images_update_image_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.add_service`<a id="hetznerload_balancer_actionsadd_service"></a>

Adds a service to a Load Balancer.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                       | Description                                             |
|----------------------------|---------------------------------------------------------|
| `source_port_already_used` | The source port you are trying to add is already in use |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_service_response = hetzner.load_balancer_actions.add_service(
    destination_port=80,
    health_check={
        "interval": 15,
        "port": 4711,
        "protocol": "http",
        "retries": 3,
        "timeout": 10,
    },
    listen_port=443,
    protocol="https",
    proxyprotocol=False,
    id=1,
    http={
        "certificates": [897],
        "cookie_lifetime": 300,
        "cookie_name": "HCLBSTICKY",
        "redirect_http": True,
        "sticky_sessions": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### destination_port: `int`<a id="destination_port-int"></a>

Port the Load Balancer will balance to

##### health_check: [`LoadBalancerActionsAddServiceRequestHealthCheck`](./hetzner_python_sdk/type/load_balancer_actions_add_service_request_health_check.py)<a id="health_check-loadbalanceractionsaddservicerequesthealthcheckhetzner_python_sdktypeload_balancer_actions_add_service_request_health_checkpy"></a>


##### listen_port: `int`<a id="listen_port-int"></a>

Port the Load Balancer listens on

##### protocol: `str`<a id="protocol-str"></a>

Protocol of the Load Balancer

##### proxyprotocol: `bool`<a id="proxyprotocol-bool"></a>

Is Proxyprotocol enabled or not

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### http: [`LoadBalancerActionsAddServiceRequestHttp`](./hetzner_python_sdk/type/load_balancer_actions_add_service_request_http.py)<a id="http-loadbalanceractionsaddservicerequesthttphetzner_python_sdktypeload_balancer_actions_add_service_request_httppy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsAddServiceRequest`](./hetzner_python_sdk/type/load_balancer_actions_add_service_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsAddServiceResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_add_service_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/add_service` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.add_target`<a id="hetznerload_balancer_actionsadd_target"></a>

Adds a target to a Load Balancer.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                    | Description                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
| `ip_not_owned`                          | The IP you are trying to add as a target is not owned by the Project owner                            |
| `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
| `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
| `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
| `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_target_response = hetzner.load_balancer_actions.add_target(
    type="server",
    id=1,
    ip={
        "ip": "203.0.113.1",
    },
    label_selector={
        "selector": "env=prod",
    },
    server={
        "id": 80,
    },
    use_private_ip=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of the resource

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### ip: [`LoadBalancerActionsAddTargetRequestIp`](./hetzner_python_sdk/type/load_balancer_actions_add_target_request_ip.py)<a id="ip-loadbalanceractionsaddtargetrequestiphetzner_python_sdktypeload_balancer_actions_add_target_request_ippy"></a>


##### label_selector: [`LoadBalancerActionsAddTargetRequestLabelSelector`](./hetzner_python_sdk/type/load_balancer_actions_add_target_request_label_selector.py)<a id="label_selector-loadbalanceractionsaddtargetrequestlabelselectorhetzner_python_sdktypeload_balancer_actions_add_target_request_label_selectorpy"></a>


##### server: [`LoadBalancerActionsAddTargetRequestServer`](./hetzner_python_sdk/type/load_balancer_actions_add_target_request_server.py)<a id="server-loadbalanceractionsaddtargetrequestserverhetzner_python_sdktypeload_balancer_actions_add_target_request_serverpy"></a>


##### use_private_ip: `bool`<a id="use_private_ip-bool"></a>

Use the private network IP instead of the public IP of the Server, requires the Server and Load Balancer to be in the same network.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsAddTargetRequest`](./hetzner_python_sdk/type/load_balancer_actions_add_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsAddTargetResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_add_target_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/add_target` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.attach_to_network`<a id="hetznerload_balancer_actionsattach_to_network"></a>

Attach a Load Balancer to a Network.

**Call specific error codes**

| Code                             | Description                                                           |
|----------------------------------|-----------------------------------------------------------------------|
| `load_balancer_already_attached` | The Load Balancer is already attached to a network                    |
| `ip_not_available`               | The provided Network IP is not available                              |
| `no_subnet_available`            | No Subnet or IP is available for the Load Balancer within the network |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
attach_to_network_response = hetzner.load_balancer_actions.attach_to_network(
    network=4711,
    id=1,
    ip="10.0.1.1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network: `int`<a id="network-int"></a>

ID of an existing network to attach the Load Balancer to

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### ip: `str`<a id="ip-str"></a>

IP to request to be assigned to this Load Balancer; if you do not provide this then you will be auto assigned an IP address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsAttachToNetworkRequest`](./hetzner_python_sdk/type/load_balancer_actions_attach_to_network_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsAttachToNetworkResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_attach_to_network_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/attach_to_network` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.change_algorithm`<a id="hetznerload_balancer_actionschange_algorithm"></a>

Change the algorithm that determines to which target new requests are sent.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_algorithm_response = hetzner.load_balancer_actions.change_algorithm(
    type="round_robin",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Algorithm of the Load Balancer

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsChangeAlgorithmRequest`](./hetzner_python_sdk/type/load_balancer_actions_change_algorithm_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsChangeAlgorithmResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_change_algorithm_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/change_algorithm` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.change_dns_ptr`<a id="hetznerload_balancer_actionschange_dns_ptr"></a>

Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.

Floating IPs assigned to the Server are not affected by this.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_dns_ptr_response = hetzner.load_balancer_actions.change_dns_ptr(
    dns_ptr="lb1.example.com",
    ip="1.2.3.4",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dns_ptr: `Optional[str]`<a id="dns_ptr-optionalstr"></a>

Hostname to set as a reverse DNS PTR entry

##### ip: `str`<a id="ip-str"></a>

Public IP address for which the reverse DNS entry should be set

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsChangeDnsPtrRequest`](./hetzner_python_sdk/type/load_balancer_actions_change_dns_ptr_request.py)
Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsChangeDnsPtrResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_change_dns_ptr_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/change_dns_ptr` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.change_protection`<a id="hetznerload_balancer_actionschange_protection"></a>

Changes the protection configuration of a Load Balancer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_response = hetzner.load_balancer_actions.change_protection(
    id=1,
    delete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Load Balancer from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsChangeProtectionRequest`](./hetzner_python_sdk/type/load_balancer_actions_change_protection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsChangeProtectionResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_change_protection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.change_type`<a id="hetznerload_balancer_actionschange_type"></a>

Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.

**Call specific error codes**

| Code                         | Description                                                     |
|------------------------------|-----------------------------------------------------------------|
| `invalid_load_balancer_type` | The Load Balancer type does not fit for the given Load Balancer |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_type_response = hetzner.load_balancer_actions.change_type(
    load_balancer_type="lb21",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### load_balancer_type: `str`<a id="load_balancer_type-str"></a>

ID or name of Load Balancer type the Load Balancer should migrate to

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsChangeTypeRequest`](./hetzner_python_sdk/type/load_balancer_actions_change_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsChangeTypeResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_change_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/change_type` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.delete_service`<a id="hetznerload_balancer_actionsdelete_service"></a>

Delete a service of a Load Balancer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_service_response = hetzner.load_balancer_actions.delete_service(
    listen_port=443,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### listen_port: `int`<a id="listen_port-int"></a>

The listen port of the service you want to delete

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsDeleteServiceRequest`](./hetzner_python_sdk/type/load_balancer_actions_delete_service_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsDeleteServiceResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_delete_service_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/delete_service` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.detach_from_network`<a id="hetznerload_balancer_actionsdetach_from_network"></a>

Detaches a Load Balancer from a network.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detach_from_network_response = hetzner.load_balancer_actions.detach_from_network(
    network=4711,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network: `int`<a id="network-int"></a>

ID of an existing network to detach the Load Balancer from

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsDetachFromNetworkRequest`](./hetzner_python_sdk/type/load_balancer_actions_detach_from_network_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsDetachFromNetworkResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_detach_from_network_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/detach_from_network` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.disable_public_interface`<a id="hetznerload_balancer_actionsdisable_public_interface"></a>

Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                      | Description                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------|
| `load_balancer_not_attached_to_network`   |  The Load Balancer is not attached to a network                                |
| `targets_without_use_private_ip`          | The Load Balancer has targets that use the public IP instead of the private IP |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disable_public_interface_response = (
    hetzner.load_balancer_actions.disable_public_interface(
        id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsDisablePublicInterfaceResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_disable_public_interface_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/disable_public_interface` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.enable_public_interface`<a id="hetznerload_balancer_actionsenable_public_interface"></a>

Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_public_interface_response = (
    hetzner.load_balancer_actions.enable_public_interface(
        id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsEnablePublicInterfaceResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_enable_public_interface_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/enable_public_interface` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.get_all_actions`<a id="hetznerload_balancer_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.load_balancer_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.get_all_actions_0`<a id="hetznerload_balancer_actionsget_all_actions_0"></a>

Returns all Action objects for a Load Balancer. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.load_balancer_actions.get_all_actions_0(
    id=1,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/load_balancer_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.get_specific_action`<a id="hetznerload_balancer_actionsget_specific_action"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_action_response = hetzner.load_balancer_actions.get_specific_action(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsGetSpecificActionResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_get_specific_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.get_specific_action_0`<a id="hetznerload_balancer_actionsget_specific_action_0"></a>

Returns a specific Action for a Load Balancer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_action_0_response = hetzner.load_balancer_actions.get_specific_action_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsGetSpecificAction200Response`](./hetzner_python_sdk/pydantic/load_balancer_actions_get_specific_action200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.remove_target`<a id="hetznerload_balancer_actionsremove_target"></a>

Removes a target from a Load Balancer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_target_response = hetzner.load_balancer_actions.remove_target(
    type="server",
    id=1,
    ip={
        "ip": "203.0.113.1",
    },
    label_selector={
        "selector": "env=prod",
    },
    server={
        "id": 80,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of the resource

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### ip: [`LoadBalancerActionsRemoveTargetRequestIp`](./hetzner_python_sdk/type/load_balancer_actions_remove_target_request_ip.py)<a id="ip-loadbalanceractionsremovetargetrequestiphetzner_python_sdktypeload_balancer_actions_remove_target_request_ippy"></a>


##### label_selector: [`LoadBalancerActionsRemoveTargetRequestLabelSelector`](./hetzner_python_sdk/type/load_balancer_actions_remove_target_request_label_selector.py)<a id="label_selector-loadbalanceractionsremovetargetrequestlabelselectorhetzner_python_sdktypeload_balancer_actions_remove_target_request_label_selectorpy"></a>


##### server: [`LoadBalancerActionsRemoveTargetRequestServer`](./hetzner_python_sdk/type/load_balancer_actions_remove_target_request_server.py)<a id="server-loadbalanceractionsremovetargetrequestserverhetzner_python_sdktypeload_balancer_actions_remove_target_request_serverpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsRemoveTargetRequest`](./hetzner_python_sdk/type/load_balancer_actions_remove_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsRemoveTargetResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_remove_target_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/remove_target` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_actions.update_service`<a id="hetznerload_balancer_actionsupdate_service"></a>

Updates a Load Balancer Service.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                       | Description                                             |
|----------------------------|---------------------------------------------------------|
| `source_port_already_used` | The source port you are trying to add is already in use |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_service_response = hetzner.load_balancer_actions.update_service(
    listen_port=443,
    id=1,
    destination_port=80,
    health_check={
        "interval": 15,
        "port": 4711,
        "protocol": "http",
        "retries": 3,
        "timeout": 10,
    },
    http={
        "certificates": [897],
        "cookie_lifetime": 300,
        "cookie_name": "HCLBSTICKY",
        "redirect_http": True,
        "sticky_sessions": True,
    },
    protocol="https",
    proxyprotocol=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### listen_port: `int`<a id="listen_port-int"></a>

Port the Load Balancer listens on

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### destination_port: `int`<a id="destination_port-int"></a>

Port the Load Balancer will balance to

##### health_check: [`LoadBalancerActionsUpdateServiceRequestHealthCheck`](./hetzner_python_sdk/type/load_balancer_actions_update_service_request_health_check.py)<a id="health_check-loadbalanceractionsupdateservicerequesthealthcheckhetzner_python_sdktypeload_balancer_actions_update_service_request_health_checkpy"></a>


##### http: [`LoadBalancerActionsUpdateServiceRequestHttp`](./hetzner_python_sdk/type/load_balancer_actions_update_service_request_http.py)<a id="http-loadbalanceractionsupdateservicerequesthttphetzner_python_sdktypeload_balancer_actions_update_service_request_httppy"></a>


##### protocol: `str`<a id="protocol-str"></a>

Protocol of the Load Balancer

##### proxyprotocol: `bool`<a id="proxyprotocol-bool"></a>

Is Proxyprotocol enabled or not

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancerActionsUpdateServiceRequest`](./hetzner_python_sdk/type/load_balancer_actions_update_service_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerActionsUpdateServiceResponse`](./hetzner_python_sdk/pydantic/load_balancer_actions_update_service_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/actions/update_service` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_types.get_all_types`<a id="hetznerload_balancer_typesget_all_types"></a>

Gets all Load Balancer type objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_types_response = hetzner.load_balancer_types.get_all_types(
    name="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerTypesGetAllTypesResponse`](./hetzner_python_sdk/pydantic/load_balancer_types_get_all_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancer_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancer_types.get_by_id`<a id="hetznerload_balancer_typesget_by_id"></a>

Gets a specific Load Balancer type object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.load_balancer_types.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of Load Balancer type

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancerTypesGetByIdResponse`](./hetzner_python_sdk/pydantic/load_balancer_types_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancer_types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.create_load_balancer`<a id="hetznerload_balancerscreate_load_balancer"></a>

Creates a Load Balancer.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                    | Description                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
| `ip_not_owned`                          | The IP is not owned by the owner of the project of the Load Balancer                                  |
| `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
| `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
| `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
| `source_port_already_used`              | The source port you are trying to add is already in use                                               |
| `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_load_balancer_response = hetzner.load_balancers.create_load_balancer(
    load_balancer_type="lb11",
    name="Web Frontend",
    algorithm={
        "type": "round_robin",
    },
    labels={
        "labelkey": "value",
    },
    location="string_example",
    network=123,
    network_zone="eu-central",
    public_interface=True,
    services=[
        {
            "destination_port": 80,
            "health_check": {
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            "listen_port": 443,
            "protocol": "https",
            "proxyprotocol": False,
        }
    ],
    targets=[
        {
            "type": "server",
            "use_private_ip": False,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### load_balancer_type: `str`<a id="load_balancer_type-str"></a>

ID or name of the Load Balancer type this Load Balancer should be created with

##### name: `str`<a id="name-str"></a>

Name of the Load Balancer

##### algorithm: [`LoadBalancersCreateLoadBalancerRequestAlgorithm`](./hetzner_python_sdk/type/load_balancers_create_load_balancer_request_algorithm.py)<a id="algorithm-loadbalancerscreateloadbalancerrequestalgorithmhetzner_python_sdktypeload_balancers_create_load_balancer_request_algorithmpy"></a>


##### labels: [`LoadBalancersCreateLoadBalancerRequestLabels`](./hetzner_python_sdk/type/load_balancers_create_load_balancer_request_labels.py)<a id="labels-loadbalancerscreateloadbalancerrequestlabelshetzner_python_sdktypeload_balancers_create_load_balancer_request_labelspy"></a>


##### location: `str`<a id="location-str"></a>

ID or name of Location to create Load Balancer in

##### network: `int`<a id="network-int"></a>

ID of the network the Load Balancer should be attached to on creation

##### network_zone: `str`<a id="network_zone-str"></a>

Name of network zone

##### public_interface: `bool`<a id="public_interface-bool"></a>

Enable or disable the public interface of the Load Balancer

##### services: [`LoadBalancersCreateLoadBalancerRequestServices`](./hetzner_python_sdk/type/load_balancers_create_load_balancer_request_services.py)<a id="services-loadbalancerscreateloadbalancerrequestserviceshetzner_python_sdktypeload_balancers_create_load_balancer_request_servicespy"></a>

##### targets: [`LoadBalancersCreateLoadBalancerRequestTargets`](./hetzner_python_sdk/type/load_balancers_create_load_balancer_request_targets.py)<a id="targets-loadbalancerscreateloadbalancerrequesttargetshetzner_python_sdktypeload_balancers_create_load_balancer_request_targetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancersCreateLoadBalancerRequest`](./hetzner_python_sdk/type/load_balancers_create_load_balancer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancersCreateLoadBalancerResponse`](./hetzner_python_sdk/pydantic/load_balancers_create_load_balancer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.delete_load_balancer`<a id="hetznerload_balancersdelete_load_balancer"></a>

Deletes a Load Balancer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.load_balancers.delete_load_balancer(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.get_all`<a id="hetznerload_balancersget_all"></a>

Gets all existing Load Balancers that you have available.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.load_balancers.get_all(
    sort="id",
    name="string_example",
    label_selector="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancersGetAllResponse`](./hetzner_python_sdk/pydantic/load_balancers_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.get_by_id`<a id="hetznerload_balancersget_by_id"></a>

Gets a specific Load Balancer object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.load_balancers.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancersGetByIdResponse`](./hetzner_python_sdk/pydantic/load_balancers_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.get_metrics`<a id="hetznerload_balancersget_metrics"></a>

You must specify the type of metric to get: `open_connections`, `connections_per_second`, `requests_per_second` or `bandwidth`. You can also specify more than one type by comma separation, e.g. `requests_per_second,bandwidth`.

Depending on the type you will get different time series data:

|Type | Timeseries | Unit | Description |
|---- |------------|------|-------------|
| open_connections | open_connections | number | Open connections |
| connections_per_second | connections_per_second | connections/s | Connections per second |
| requests_per_second | requests_per_second | requests/s | Requests per second |
| bandwidth | bandwidth.in | bytes/s | Ingress bandwidth |
|| bandwidth.out | bytes/s | Egress bandwidth |

Metrics are available for the last 30 days only.

If you do not provide the step argument we will automatically adjust it so that 200 samples are returned.

We limit the number of samples to a maximum of 500 and will adjust the step parameter accordingly.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metrics_response = hetzner.load_balancers.get_metrics(
    id=1,
    type="open_connections",
    start="start_example",
    end="end_example",
    step="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### type: `str`<a id="type-str"></a>

Type of metrics to get

##### start: `str`<a id="start-str"></a>

Start of period to get Metrics for (in ISO-8601 format)

##### end: `str`<a id="end-str"></a>

End of period to get Metrics for (in ISO-8601 format)

##### step: `str`<a id="step-str"></a>

Resolution of results in seconds

#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancersGetMetricsResponse`](./hetzner_python_sdk/pydantic/load_balancers_get_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}/metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.load_balancers.update_balancer`<a id="hetznerload_balancersupdate_balancer"></a>

Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.

Note that when updating labels, the Load Balancer’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the Load Balancer object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_balancer_response = hetzner.load_balancers.update_balancer(
    id=1,
    labels={
        "labelkey": "value",
    },
    name="new-name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Load Balancer

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New Load Balancer name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoadBalancersUpdateBalancerRequest`](./hetzner_python_sdk/type/load_balancers_update_balancer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LoadBalancersUpdateBalancerResponse`](./hetzner_python_sdk/pydantic/load_balancers_update_balancer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/load_balancers/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.locations.get_all_locations`<a id="hetznerlocationsget_all_locations"></a>

Returns all Location objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_locations_response = hetzner.locations.get_all_locations(
    name="string_example",
    sort="id",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Can be used to filter Locations by their name. The response will only contain the Location matching the specified name.

##### sort: `str`<a id="sort-str"></a>

Can be used multiple times.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetAllLocationsResponse`](./hetzner_python_sdk/pydantic/locations_get_all_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.locations.get_location_by_id`<a id="hetznerlocationsget_location_by_id"></a>

Returns a specific Location object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_by_id_response = hetzner.locations.get_location_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of Location

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetLocationByIdResponse`](./hetzner_python_sdk/pydantic/locations_get_location_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.add_route`<a id="hetznernetwork_actionsadd_route"></a>

Adds a route entry to a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_route_response = hetzner.network_actions.add_route(
    destination="10.100.1.0/24",
    gateway="10.0.1.1",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### destination: `str`<a id="destination-str"></a>

Destination network or host of this route. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first IP of the networks ip_range or with 172.31.1.1. Must be one of the private IPv4 ranges of RFC1918.

##### gateway: `str`<a id="gateway-str"></a>

Gateway for the route. Cannot be the first IP of the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being used as a gateway for the public network interface of Servers.

##### id: `int`<a id="id-int"></a>

ID of the Network

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsAddRouteRequest`](./hetzner_python_sdk/type/network_actions_add_route_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsAddRouteResponse`](./hetzner_python_sdk/pydantic/network_actions_add_route_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/add_route` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.add_subnet`<a id="hetznernetwork_actionsadd_subnet"></a>

Adds a new subnet object to the Network. If you do not specify an `ip_range` for the subnet we will automatically pick the first available /24 range for you if possible.

Note: if the parent Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_subnet_response = hetzner.network_actions.add_subnet(
    network_zone="eu-central",
    type="cloud",
    id=1,
    ip_range="10.0.1.0/24",
    vswitch_id=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network_zone: `str`<a id="network_zone-str"></a>

Name of Network zone. The Location object contains the `network_zone` property each Location belongs to.

##### type: `str`<a id="type-str"></a>

Type of Subnetwork

##### id: `int`<a id="id-int"></a>

ID of the Network

##### ip_range: `str`<a id="ip_range-str"></a>

Range to allocate IPs from. Must be a Subnet of the ip_range of the parent network object and must not overlap with any other subnets or with any destinations in routes. If the Subnet is of type vSwitch, it also can not overlap with any gateway in routes. Minimum Network size is /30. We suggest that you pick a bigger Network with a /24 netmask.

##### vswitch_id: `int`<a id="vswitch_id-int"></a>

ID of the robot vSwitch. Must be supplied if the subnet is of type vswitch.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsAddSubnetRequest`](./hetzner_python_sdk/type/network_actions_add_subnet_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsAddSubnetResponse`](./hetzner_python_sdk/pydantic/network_actions_add_subnet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/add_subnet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.change_ip_range`<a id="hetznernetwork_actionschange_ip_range"></a>

Changes the IP range of a Network. IP ranges can only be extended and never shrunk. You can only add IPs at the end of an existing IP range. This means that the IP part of your existing range must stay the same and you can only change its netmask.

For example if you have a range `10.0.0.0/16` you want to extend then your new range must also start with the IP `10.0.0.0`. Your CIDR netmask `/16` may change to a number that is smaller than `16` thereby increasing the IP range. So valid entries would be `10.0.0.0/15`, `10.0.0.0/14`, `10.0.0.0/13` and so on.

After changing the IP range you will have to adjust the routes on your connected Servers by either rebooting them or manually changing the routes to your private Network interface.

Note: if the Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_ip_range_response = hetzner.network_actions.change_ip_range(
    ip_range="10.0.0.0/12",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ip_range: `str`<a id="ip_range-str"></a>

The new prefix for the whole Network

##### id: `int`<a id="id-int"></a>

ID of the Network

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsChangeIpRangeRequest`](./hetzner_python_sdk/type/network_actions_change_ip_range_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsChangeIpRangeResponse`](./hetzner_python_sdk/pydantic/network_actions_change_ip_range_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/change_ip_range` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.change_protection`<a id="hetznernetwork_actionschange_protection"></a>

Changes the protection configuration of a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_response = hetzner.network_actions.change_protection(
    id=1,
    delete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Network

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Network from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsChangeProtectionRequest`](./hetzner_python_sdk/type/network_actions_change_protection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsChangeProtectionResponse`](./hetzner_python_sdk/pydantic/network_actions_change_protection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.delete_route`<a id="hetznernetwork_actionsdelete_route"></a>

Delete a route entry from a Network.

Note: if the Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_route_response = hetzner.network_actions.delete_route(
    destination="10.100.1.0/24",
    gateway="10.0.1.1",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### destination: `str`<a id="destination-str"></a>

Destination network or host of this route. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first IP of the networks ip_range or with 172.31.1.1. Must be one of the private IPv4 ranges of RFC1918.

##### gateway: `str`<a id="gateway-str"></a>

Gateway for the route. Cannot be the first IP of the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being used as a gateway for the public network interface of Servers.

##### id: `int`<a id="id-int"></a>

ID of the Network

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsDeleteRouteRequest`](./hetzner_python_sdk/type/network_actions_delete_route_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsDeleteRouteResponse`](./hetzner_python_sdk/pydantic/network_actions_delete_route_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/delete_route` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.delete_subnet`<a id="hetznernetwork_actionsdelete_subnet"></a>

Deletes a single subnet entry from a Network. You cannot delete subnets which still have Servers attached. If you have Servers attached you first need to detach all Servers that use IPs from this subnet before you can delete the subnet.

Note: if the Network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_subnet_response = hetzner.network_actions.delete_subnet(
    ip_range="10.0.1.0/24",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ip_range: `str`<a id="ip_range-str"></a>

IP range of subnet to delete

##### id: `int`<a id="id-int"></a>

ID of the Network

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkActionsDeleteSubnetRequest`](./hetzner_python_sdk/type/network_actions_delete_subnet_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsDeleteSubnetResponse`](./hetzner_python_sdk/pydantic/network_actions_delete_subnet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/delete_subnet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.get_action`<a id="hetznernetwork_actionsget_action"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_response = hetzner.network_actions.get_action(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsGetActionResponse`](./hetzner_python_sdk/pydantic/network_actions_get_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.get_action_0`<a id="hetznernetwork_actionsget_action_0"></a>

Returns a specific Action for a Network.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_0_response = hetzner.network_actions.get_action_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Network

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsGetAction200Response`](./hetzner_python_sdk/pydantic/network_actions_get_action200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.get_all_actions`<a id="hetznernetwork_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.network_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/network_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.network_actions.get_all_actions_0`<a id="hetznernetwork_actionsget_all_actions_0"></a>

Returns all Action objects for a Network. You can sort the results by using the `sort` URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.network_actions.get_all_actions_0(
    id=1,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Network

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/network_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.networks.create_network`<a id="hetznernetworkscreate_network"></a>

Creates a network with the specified `ip_range`.

You may specify one or more `subnets`. You can also add more Subnets later by using the [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network). If you do not specify an `ip_range` in the subnet we will automatically pick the first available /24 range for you.

You may specify one or more routes in `routes`. You can also add more routes later by using the [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_network_response = hetzner.networks.create_network(
    ip_range="10.0.0.0/16",
    name="mynet",
    expose_routes_to_vswitch=False,
    labels={
        "labelkey": "value",
    },
    routes=[
        {
            "destination": "10.100.1.0/24",
            "gateway": "10.0.1.1",
        }
    ],
    subnets=[
        {
            "ip_range": "10.0.1.0/24",
            "network_zone": "eu-central",
            "type": "cloud",
            "vswitch_id": 1000,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ip_range: `str`<a id="ip_range-str"></a>

IP range of the whole network which must span all included subnets. Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We highly recommend that you pick a larger network with a /16 netmask.

##### name: `str`<a id="name-str"></a>

Name of the network

##### expose_routes_to_vswitch: `bool`<a id="expose_routes_to_vswitch-bool"></a>

Indicates if the routes from this network should be exposed to the vSwitch connection. The exposing only takes effect if a vSwitch connection is active.

##### labels: [`NetworksCreateNetworkRequestLabels`](./hetzner_python_sdk/type/networks_create_network_request_labels.py)<a id="labels-networkscreatenetworkrequestlabelshetzner_python_sdktypenetworks_create_network_request_labelspy"></a>


##### routes: [`NetworksCreateNetworkRequestRoutes`](./hetzner_python_sdk/type/networks_create_network_request_routes.py)<a id="routes-networkscreatenetworkrequestrouteshetzner_python_sdktypenetworks_create_network_request_routespy"></a>

##### subnets: [`NetworksCreateNetworkRequestSubnets`](./hetzner_python_sdk/type/networks_create_network_request_subnets.py)<a id="subnets-networkscreatenetworkrequestsubnetshetzner_python_sdktypenetworks_create_network_request_subnetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworksCreateNetworkRequest`](./hetzner_python_sdk/type/networks_create_network_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworksCreateNetworkResponse`](./hetzner_python_sdk/pydantic/networks_create_network_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.networks.delete_network`<a id="hetznernetworksdelete_network"></a>

Deletes a network. If there are Servers attached they will be detached in the background.

Note: if the network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.networks.delete_network(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the network

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.networks.get_all`<a id="hetznernetworksget_all"></a>

Gets all existing networks that you have available.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.networks.get_all(
    name="string_example",
    label_selector="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`NetworksGetAllResponse`](./hetzner_python_sdk/pydantic/networks_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.networks.get_by_id`<a id="hetznernetworksget_by_id"></a>

Gets a specific network object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.networks.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the network

#### 🔄 Return<a id="🔄-return"></a>

[`NetworksGetByIdResponse`](./hetzner_python_sdk/pydantic/networks_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.networks.update_properties`<a id="hetznernetworksupdate_properties"></a>

Updates the network properties.

Note that when updating labels, the network’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the network object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_properties_response = hetzner.networks.update_properties(
    id=1,
    expose_routes_to_vswitch=False,
    labels={
        "labelkey": "value",
    },
    name="new-name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the network

##### expose_routes_to_vswitch: `bool`<a id="expose_routes_to_vswitch-bool"></a>

Indicates if the routes from this network should be exposed to the vSwitch connection. The exposing only takes effect if a vSwitch connection is active.

##### labels: [`NetworksUpdatePropertiesRequestLabels`](./hetzner_python_sdk/type/networks_update_properties_request_labels.py)<a id="labels-networksupdatepropertiesrequestlabelshetzner_python_sdktypenetworks_update_properties_request_labelspy"></a>


##### name: `str`<a id="name-str"></a>

New network name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworksUpdatePropertiesRequest`](./hetzner_python_sdk/type/networks_update_properties_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworksUpdatePropertiesResponse`](./hetzner_python_sdk/pydantic/networks_update_properties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/networks/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.placement_groups.create_new_group`<a id="hetznerplacement_groupscreate_new_group"></a>

Creates a new PlacementGroup.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_group_response = hetzner.placement_groups.create_new_group(
    name="my Placement Group",
    type="spread",
    labels={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the PlacementGroup

##### type: `str`<a id="type-str"></a>

Define the Placement Group Type.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlacementGroupsCreateNewGroupRequest`](./hetzner_python_sdk/type/placement_groups_create_new_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlacementGroupsCreateNewGroupResponse`](./hetzner_python_sdk/pydantic/placement_groups_create_new_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/placement_groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.placement_groups.delete_group`<a id="hetznerplacement_groupsdelete_group"></a>

Deletes a PlacementGroup.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.placement_groups.delete_group(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/placement_groups/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.placement_groups.get_all`<a id="hetznerplacement_groupsget_all"></a>

Returns all PlacementGroup objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.placement_groups.get_all(
    sort="id",
    name="string_example",
    label_selector="string_example",
    type="spread",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### type: `str`<a id="type-str"></a>

Can be used multiple times. The response will only contain PlacementGroups matching the type.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`PlacementGroupsGetAllResponse`](./hetzner_python_sdk/pydantic/placement_groups_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/placement_groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.placement_groups.get_by_id`<a id="hetznerplacement_groupsget_by_id"></a>

Gets a specific PlacementGroup object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.placement_groups.get_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🔄 Return<a id="🔄-return"></a>

[`PlacementGroupsGetByIdResponse`](./hetzner_python_sdk/pydantic/placement_groups_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/placement_groups/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.placement_groups.update_properties`<a id="hetznerplacement_groupsupdate_properties"></a>

Updates the PlacementGroup properties.

Note that when updating labels, the PlacementGroup’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

Note: if the PlacementGroup object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_properties_response = hetzner.placement_groups.update_properties(
    id=42,
    labels={
        "labelkey": "value",
    },
    name="my Placement Group",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New PlacementGroup name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlacementGroupsUpdatePropertiesRequest`](./hetzner_python_sdk/type/placement_groups_update_properties_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlacementGroupsUpdatePropertiesResponse`](./hetzner_python_sdk/pydantic/placement_groups_update_properties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/placement_groups/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.pricing.get_all_prices`<a id="hetznerpricingget_all_prices"></a>

Returns prices for all resources available on the platform. VAT and currency of the Project owner are used for calculations.

Both net and gross prices are included in the response.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_prices_response = hetzner.pricing.get_all_prices()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PricingGetAllPricesResponse`](./hetzner_python_sdk/pydantic/pricing_get_all_prices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pricing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.assign_primary_ip_to_resource`<a id="hetznerprimary_ip_actionsassign_primary_ip_to_resource"></a>

Assigns a Primary IP to a Server.

A Server can only have one Primary IP of type `ipv4` and one of type `ipv6` assigned. If you need more IPs use Floating IPs.

The Server must be powered off (status `off`) in order for this operation to succeed.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_not_stopped`          | The server is running, but needs to be powered off            |
| `primary_ip_already_assigned` | Primary ip is already assigned to a different server          |
| `server_has_ipv4`             | The server already has an ipv4 address                        |
| `server_has_ipv6`             | The server already has an ipv6 address                        |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_primary_ip_to_resource_response = (
    hetzner.primary_ip_actions.assign_primary_ip_to_resource(
        assignee_id=4711,
        assignee_type="server",
        id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignee_id: `int`<a id="assignee_id-int"></a>

ID of a resource of type `assignee_type`

##### assignee_type: `str`<a id="assignee_type-str"></a>

Type of resource assigning the Primary IP to

##### id: `int`<a id="id-int"></a>

ID of the Primary IP

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrimaryIpActionsAssignPrimaryIpToResourceRequest`](./hetzner_python_sdk/type/primary_ip_actions_assign_primary_ip_to_resource_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsAssignPrimaryIpToResourceResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_assign_primary_ip_to_resource_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}/actions/assign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.change_dns_ptr`<a id="hetznerprimary_ip_actionschange_dns_ptr"></a>

Changes the hostname that will appear when getting the hostname belonging to this Primary IP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_dns_ptr_response = hetzner.primary_ip_actions.change_dns_ptr(
    dns_ptr="server02.example.com",
    ip="1.2.3.4",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dns_ptr: `Optional[str]`<a id="dns_ptr-optionalstr"></a>

Hostname to set as a reverse DNS PTR entry, will reset to original default value if `null`

##### ip: `str`<a id="ip-str"></a>

IP address for which to set the reverse DNS entry

##### id: `int`<a id="id-int"></a>

ID of the Primary IP

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrimaryIpActionsChangeDnsPtrRequest`](./hetzner_python_sdk/type/primary_ip_actions_change_dns_ptr_request.py)
Select the IP address for which to change the DNS entry by passing `ip`. For a Primary IP of type `ipv4` this must exactly match the IP address of the Primary IP. For a Primary IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsChangeDnsPtrResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_change_dns_ptr_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}/actions/change_dns_ptr` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.change_protection_primary_ip`<a id="hetznerprimary_ip_actionschange_protection_primary_ip"></a>

Changes the protection configuration of a Primary IP.

A Primary IP can only be delete protected if its `auto_delete` property is set to `false`.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_primary_ip_response = (
    hetzner.primary_ip_actions.change_protection_primary_ip(
        id=1,
        delete=True,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Primary IP

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Primary IP from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrimaryIpActionsChangeProtectionPrimaryIpRequest`](./hetzner_python_sdk/type/primary_ip_actions_change_protection_primary_ip_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsChangeProtectionPrimaryIpResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_change_protection_primary_ip_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.get_action_by_id`<a id="hetznerprimary_ip_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.primary_ip_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.get_all_actions`<a id="hetznerprimary_ip_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.primary_ip_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ip_actions.unassign_primary_ip`<a id="hetznerprimary_ip_actionsunassign_primary_ip"></a>

Unassigns a Primary IP from a Server.

The Server must be powered off (status `off`) in order for this operation to succeed.

Note that only Servers that have at least one network interface (public or private) attached can be powered on.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                              | Description                                                   |
|---------------------------------- |-------------------------------------------------------------- |
| `server_not_stopped`              | The server is running, but needs to be powered off            |
| `server_is_load_balancer_target`  | The server ipv4 address is a loadbalancer target              |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unassign_primary_ip_response = hetzner.primary_ip_actions.unassign_primary_ip(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Primary IP

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIpActionsUnassignPrimaryIpResponse`](./hetzner_python_sdk/pydantic/primary_ip_actions_unassign_primary_ip_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}/actions/unassign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ips.create_or_update`<a id="hetznerprimary_ipscreate_or_update"></a>

Creates a new Primary IP, optionally assigned to a Server.

If you want to create a Primary IP that is not assigned to a Server, you need to provide the `datacenter` key instead of `assignee_id`. This can be either the ID or the name of the Datacenter this Primary IP shall be created in.

Note that a Primary IP can only be assigned to a Server in the same Datacenter later on.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                   |
|------------------------------ |-------------------------------------------------------------- |
| `server_not_stopped`          | The specified server is running, but needs to be powered off  |
| `server_has_ipv4`             | The server already has an ipv4 address                        |
| `server_has_ipv6`             | The server already has an ipv6 address                        |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_response = hetzner.primary_ips.create_or_update(
    assignee_type="server",
    name="my-ip",
    type="ipv4",
    assignee_id=17,
    auto_delete=False,
    datacenter="fsn1-dc8",
    labels={
        "labelkey": "value",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignee_type: `str`<a id="assignee_type-str"></a>

Resource type the Primary IP can be assigned to

##### name: `str`<a id="name-str"></a>

##### type: `str`<a id="type-str"></a>

Primary IP type

##### assignee_id: `int`<a id="assignee_id-int"></a>

ID of the resource the Primary IP should be assigned to. Omitted if it should not be assigned.

##### auto_delete: `bool`<a id="auto_delete-bool"></a>

Delete the Primary IP when the Server it is assigned to is deleted.

##### datacenter: `str`<a id="datacenter-str"></a>

ID or name of Datacenter the Primary IP will be bound to. Needs to be omitted if `assignee_id` is passed.

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrimaryIPsCreateOrUpdateRequest`](./hetzner_python_sdk/type/primary_ips_create_or_update_request.py)
The `type` argument is required while `datacenter` and `assignee_id` are mutually exclusive.

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIPsCreateOrUpdateResponse`](./hetzner_python_sdk/pydantic/primary_ips_create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ips.delete_primary_ip`<a id="hetznerprimary_ipsdelete_primary_ip"></a>

Deletes a Primary IP.

The Primary IP may be assigned to a Server. In this case it is unassigned automatically. The Server must be powered off (status `off`) in order for this operation to succeed.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.primary_ips.delete_primary_ip(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ips.get_all`<a id="hetznerprimary_ipsget_all"></a>

Returns all Primary IP objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.primary_ips.get_all(
    name="string_example",
    label_selector="string_example",
    ip="127.0.0.1",
    page=2,
    per_page=25,
    sort="id",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### ip: `str`<a id="ip-str"></a>

Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### sort: `str`<a id="sort-str"></a>

Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIPsGetAllResponse`](./hetzner_python_sdk/pydantic/primary_ips_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ips.get_by_id`<a id="hetznerprimary_ipsget_by_id"></a>

Returns a specific Primary IP object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.primary_ips.get_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIPsGetByIdResponse`](./hetzner_python_sdk/pydantic/primary_ips_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.primary_ips.update_ip_labels`<a id="hetznerprimary_ipsupdate_ip_labels"></a>

Updates the Primary IP.

Note that when updating labels, the Primary IP's current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

If the Primary IP object changes during the request, the response will be a “conflict” error.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_ip_labels_response = hetzner.primary_ips.update_ip_labels(
    id=42,
    auto_delete=True,
    labels={
        "labelkey": "value",
    },
    name="my-ip",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### auto_delete: `bool`<a id="auto_delete-bool"></a>

Delete this Primary IP when the resource it is assigned to is deleted

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New unique name to set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrimaryIPsUpdateIpLabelsRequest`](./hetzner_python_sdk/type/primary_ips_update_ip_labels_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PrimaryIPsUpdateIpLabelsResponse`](./hetzner_python_sdk/pydantic/primary_ips_update_ip_labels_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/primary_ips/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.ssh_keys.create_key`<a id="hetznerssh_keyscreate_key"></a>

Creates a new SSH key with the given `name` and `public_key`. Once an SSH key is created, it can be used in other calls such as creating Servers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_key_response = hetzner.ssh_keys.create_key(
    name="My ssh key",
    public_key="ssh-rsa AAAjjk76kgf...Xt",
    labels={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the SSH key

##### public_key: `str`<a id="public_key-str"></a>

Public key

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SshKeysCreateKeyRequest`](./hetzner_python_sdk/type/ssh_keys_create_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SshKeysCreateKeyResponse`](./hetzner_python_sdk/pydantic/ssh_keys_create_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh_keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.ssh_keys.delete_key`<a id="hetznerssh_keysdelete_key"></a>

Deletes an SSH key. It cannot be used anymore.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.ssh_keys.delete_key(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the SSH key

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh_keys/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.ssh_keys.get_all_ssh_keys`<a id="hetznerssh_keysget_all_ssh_keys"></a>

Returns all SSH key objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_ssh_keys_response = hetzner.ssh_keys.get_all_ssh_keys(
    sort="id",
    name="string_example",
    fingerprint="string_example",
    label_selector="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort: `str`<a id="sort-str"></a>

Can be used multiple times.

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### fingerprint: `str`<a id="fingerprint-str"></a>

Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint.

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`SshKeysGetAllSshKeysResponse`](./hetzner_python_sdk/pydantic/ssh_keys_get_all_ssh_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh_keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.ssh_keys.get_by_id`<a id="hetznerssh_keysget_by_id"></a>

Returns a specific SSH key object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.ssh_keys.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the SSH key

#### 🔄 Return<a id="🔄-return"></a>

[`SshKeysGetByIdResponse`](./hetzner_python_sdk/pydantic/ssh_keys_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh_keys/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.ssh_keys.update_key`<a id="hetznerssh_keysupdate_key"></a>

Updates an SSH key. You can update an SSH key name and an SSH key labels.

Please note that when updating labels, the SSH key current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_key_response = hetzner.ssh_keys.update_key(
    id=1,
    labels={
        "labelkey": "value",
    },
    name="My ssh key",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the SSH key

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New name Name to set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SshKeysUpdateKeyRequest`](./hetzner_python_sdk/type/ssh_keys_update_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SshKeysUpdateKeyResponse`](./hetzner_python_sdk/pydantic/ssh_keys_update_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ssh_keys/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.add_to_placement_group`<a id="hetznerserver_actionsadd_to_placement_group"></a>

Adds a Server to a Placement Group.

Server must be powered off for this command to succeed.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                          |
|-------------------------------|----------------------------------------------------------------------|
| `server_not_stopped`          | The action requires a stopped server                                 |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_placement_group_response = hetzner.server_actions.add_to_placement_group(
    placement_group=1,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### placement_group: `int`<a id="placement_group-int"></a>

ID of Placement Group the Server should be added to

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsAddToPlacementGroupRequest`](./hetzner_python_sdk/type/server_actions_add_to_placement_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsAddToPlacementGroupResponse`](./hetzner_python_sdk/pydantic/server_actions_add_to_placement_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/add_to_placement_group` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.attach_iso_to_server`<a id="hetznerserver_actionsattach_iso_to_server"></a>

Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already attached ISO will automatically be detached before the new ISO is attached.

Servers with attached ISOs have a modified boot order: They will try to boot from the ISO first before falling back to hard disk.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
attach_iso_to_server_response = hetzner.server_actions.attach_iso_to_server(
    iso="FreeBSD-11.0-RELEASE-amd64-dvd1",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### iso: `str`<a id="iso-str"></a>

ID or name of ISO to attach to the Server as listed in GET `/isos`

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsAttachIsoToServerRequest`](./hetzner_python_sdk/type/server_actions_attach_iso_to_server_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsAttachIsoToServerResponse`](./hetzner_python_sdk/pydantic/server_actions_attach_iso_to_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/attach_iso` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.attach_to_network`<a id="hetznerserver_actionsattach_to_network"></a>

Attaches a Server to a network. This will complement the fixed public Server interface by adding an additional ethernet interface to the Server which is connected to the specified network.

The Server will get an IP auto assigned from a subnet of type `server` in the same `network_zone`.

Using the `alias_ips` attribute you can also define one or more additional IPs to the Servers. Please note that you will have to configure these IPs by hand on your Server since only the primary IP will be given out by DHCP.

**Call specific error codes**

| Code                             | Description                                                           |
|----------------------------------|-----------------------------------------------------------------------|
| `server_already_attached`        | The server is already attached to the network                         |
| `ip_not_available`               | The provided Network IP is not available                              |
| `no_subnet_available`            | No Subnet or IP is available for the Server within the network        |
| `networks_overlap`               | The network IP range overlaps with one of the server networks         |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
attach_to_network_response = hetzner.server_actions.attach_to_network(
    network=4711,
    id=1,
    alias_ips=["10.0.1.2"],
    ip="10.0.1.1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network: `int`<a id="network-int"></a>

ID of an existing network to attach the Server to

##### id: `int`<a id="id-int"></a>

ID of the Server

##### alias_ips: [`ServerActionsAttachToNetworkRequestAliasIps`](./hetzner_python_sdk/type/server_actions_attach_to_network_request_alias_ips.py)<a id="alias_ips-serveractionsattachtonetworkrequestaliasipshetzner_python_sdktypeserver_actions_attach_to_network_request_alias_ipspy"></a>

##### ip: `str`<a id="ip-str"></a>

IP to request to be assigned to this Server; if you do not provide this then you will be auto assigned an IP address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsAttachToNetworkRequest`](./hetzner_python_sdk/type/server_actions_attach_to_network_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsAttachToNetworkResponse`](./hetzner_python_sdk/pydantic/server_actions_attach_to_network_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/attach_to_network` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.change_alias_ips`<a id="hetznerserver_actionschange_alias_ips"></a>

Changes the alias IPs of an already attached Network. Note that the existing aliases for the specified Network will be replaced with these provided in the request body. So if you want to add an alias IP, you have to provide the existing ones from the Network plus the new alias IP in the request body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_alias_ips_response = hetzner.server_actions.change_alias_ips(
    alias_ips=["10.0.1.2"],
    network=4711,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### alias_ips: [`ServerActionsChangeAliasIpsRequestAliasIps`](./hetzner_python_sdk/type/server_actions_change_alias_ips_request_alias_ips.py)<a id="alias_ips-serveractionschangealiasipsrequestaliasipshetzner_python_sdktypeserver_actions_change_alias_ips_request_alias_ipspy"></a>

##### network: `int`<a id="network-int"></a>

ID of an existing Network already attached to the Server

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsChangeAliasIpsRequest`](./hetzner_python_sdk/type/server_actions_change_alias_ips_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsChangeAliasIpsResponse`](./hetzner_python_sdk/pydantic/server_actions_change_alias_ips_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/change_alias_ips` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.change_dns_ptr`<a id="hetznerserver_actionschange_dns_ptr"></a>

Changes the hostname that will appear when getting the hostname belonging to the primary IPs (IPv4 and IPv6) of this Server.

Floating IPs assigned to the Server are not affected by this.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_dns_ptr_response = hetzner.server_actions.change_dns_ptr(
    dns_ptr="server01.example.com",
    ip="1.2.3.4",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dns_ptr: `Optional[str]`<a id="dns_ptr-optionalstr"></a>

Hostname to set as a reverse DNS PTR entry, reset to original value if `null`

##### ip: `str`<a id="ip-str"></a>

Primary IP address for which the reverse DNS entry should be set

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsChangeDnsPtrRequest`](./hetzner_python_sdk/type/server_actions_change_dns_ptr_request.py)
Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsChangeDnsPtrResponse`](./hetzner_python_sdk/pydantic/server_actions_change_dns_ptr_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/change_dns_ptr` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.change_protection`<a id="hetznerserver_actionschange_protection"></a>

Changes the protection configuration of the Server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_response = hetzner.server_actions.change_protection(
    id=1,
    delete=True,
    rebuild=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Server from being deleted (currently delete and rebuild attribute needs to have the same value)

##### rebuild: `bool`<a id="rebuild-bool"></a>

If true, prevents the Server from being rebuilt (currently delete and rebuild attribute needs to have the same value)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsChangeProtectionRequest`](./hetzner_python_sdk/type/server_actions_change_protection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsChangeProtectionResponse`](./hetzner_python_sdk/pydantic/server_actions_change_protection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.change_server_type`<a id="hetznerserver_actionschange_server_type"></a>

Changes the type (Cores, RAM and disk sizes) of a Server.

Server must be powered off for this command to succeed.

This copies the content of its disk, and starts it again.

You can only migrate to Server types with the same `storage_type` and equal or bigger disks. Shrinking disks is not possible as it might destroy data.

If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to downgrade the Server type, set `upgrade_disk` to `false`.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                          | Description                                                          |
|-------------------------------|----------------------------------------------------------------------|
| `invalid_server_type`         | The server type does not fit for the given server or is deprecated   |
| `server_not_stopped`          | The action requires a stopped server                                 |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_server_type_response = hetzner.server_actions.change_server_type(
    server_type="cx11",
    upgrade_disk=True,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### server_type: `str`<a id="server_type-str"></a>

ID or name of Server type the Server should migrate to

##### upgrade_disk: `bool`<a id="upgrade_disk-bool"></a>

If false, do not upgrade the disk (this allows downgrading the Server type later)

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsChangeServerTypeRequest`](./hetzner_python_sdk/type/server_actions_change_server_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsChangeServerTypeResponse`](./hetzner_python_sdk/pydantic/server_actions_change_server_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/change_type` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.create_image`<a id="hetznerserver_actionscreate_image"></a>

Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates a snapshot of the current state of the disk and copies it into an Image. If the Server is currently running you must make sure that its disk content is consistent. Otherwise, the created Image may not be readable.

To make sure disk content is consistent, we recommend to shut down the Server prior to creating an Image.

You can either create a `backup` Image that is bound to the Server and therefore will be deleted when the Server is deleted, or you can create a `snapshot` Image which is completely independent of the Server it was created from and will survive Server deletion. Backup Images are only available when the backup option is enabled for the Server. Snapshot Images are billed on a per GB basis.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_image_response = hetzner.server_actions.create_image(
    id=1,
    description="my image",
    labels={
        "labelkey": "value",
    },
    type="snapshot",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### description: `str`<a id="description-str"></a>

Description of the Image, will be auto-generated if not set

##### labels: [`ServerActionsCreateImageRequestLabels`](./hetzner_python_sdk/type/server_actions_create_image_request_labels.py)<a id="labels-serveractionscreateimagerequestlabelshetzner_python_sdktypeserver_actions_create_image_request_labelspy"></a>


##### type: `str`<a id="type-str"></a>

Type of Image to create.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsCreateImageRequest`](./hetzner_python_sdk/type/server_actions_create_image_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsCreateImageResponse`](./hetzner_python_sdk/pydantic/server_actions_create_image_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/create_image` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.detach_from_network`<a id="hetznerserver_actionsdetach_from_network"></a>

Detaches a Server from a network. The interface for this network will vanish.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detach_from_network_response = hetzner.server_actions.detach_from_network(
    network=4711,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network: `int`<a id="network-int"></a>

ID of an existing network to detach the Server from

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsDetachFromNetworkRequest`](./hetzner_python_sdk/type/server_actions_detach_from_network_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsDetachFromNetworkResponse`](./hetzner_python_sdk/pydantic/server_actions_detach_from_network_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/detach_from_network` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.detach_iso_from_server`<a id="hetznerserver_actionsdetach_iso_from_server"></a>

Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of the returned Action is immediately set to `success`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detach_iso_from_server_response = hetzner.server_actions.detach_iso_from_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsDetachIsoFromServerResponse`](./hetzner_python_sdk/pydantic/server_actions_detach_iso_from_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/detach_iso` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.disable_backup`<a id="hetznerserver_actionsdisable_backup"></a>

Disables the automatic backup option and deletes all existing Backups for a Server. No more additional charges for backups will be made.

Caution: This immediately removes all existing backups for the Server!


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disable_backup_response = hetzner.server_actions.disable_backup(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsDisableBackupResponse`](./hetzner_python_sdk/pydantic/server_actions_disable_backup_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/disable_backup` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.disable_rescue_mode`<a id="hetznerserver_actionsdisable_rescue_mode"></a>

Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on next reboot.

Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.

Disabling rescue mode will not reboot your Server — you will have to do this yourself.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disable_rescue_mode_response = hetzner.server_actions.disable_rescue_mode(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsDisableRescueModeResponse`](./hetzner_python_sdk/pydantic/server_actions_disable_rescue_mode_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/disable_rescue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.enable_backup`<a id="hetznerserver_actionsenable_backup"></a>

Enables and configures the automatic daily backup option for the Server. Enabling automatic backups will increase the price of the Server by 20%. In return, you will get seven slots where Images of type backup can be stored.

Backups are automatically created daily.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_backup_response = hetzner.server_actions.enable_backup(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsEnableBackupResponse`](./hetzner_python_sdk/pydantic/server_actions_enable_backup_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/enable_backup` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.enable_rescue_mode`<a id="hetznerserver_actionsenable_rescue_mode"></a>

Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue mode boots it will start a special minimal Linux distribution designed for repair and reinstall.

In case a Server cannot boot on its own you can use this to access a Server’s disks.

Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.

Enabling rescue mode will not [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you will have to do this yourself.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_rescue_mode_response = hetzner.server_actions.enable_rescue_mode(
    id=1,
    ssh_keys=[2323],
    type="linux64",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### ssh_keys: [`ServerActionsEnableRescueModeRequestSshKeys`](./hetzner_python_sdk/type/server_actions_enable_rescue_mode_request_ssh_keys.py)<a id="ssh_keys-serveractionsenablerescuemoderequestsshkeyshetzner_python_sdktypeserver_actions_enable_rescue_mode_request_ssh_keyspy"></a>

##### type: `str`<a id="type-str"></a>

Type of rescue system to boot.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsEnableRescueModeRequest`](./hetzner_python_sdk/type/server_actions_enable_rescue_mode_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsEnableRescueModeResponse`](./hetzner_python_sdk/pydantic/server_actions_enable_rescue_mode_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/enable_rescue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.get_action_by_id`<a id="hetznerserver_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.server_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/server_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.get_action_by_id_0`<a id="hetznerserver_actionsget_action_by_id_0"></a>

Returns a specific Action object for a Server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_0_response = hetzner.server_actions.get_action_by_id_0(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsGetActionById200Response`](./hetzner_python_sdk/pydantic/server_actions_get_action_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.get_all`<a id="hetznerserver_actionsget_all"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.server_actions.get_all(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsGetAllResponse`](./hetzner_python_sdk/pydantic/server_actions_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.get_all_actions`<a id="hetznerserver_actionsget_all_actions"></a>

Returns all Action objects for a Server. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.server_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Resource.

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/server_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.graceful_shutdown`<a id="hetznerserver_actionsgraceful_shutdown"></a>

Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI
and react to the request, otherwise the Server will not shut down. Please note that the `action` status in this case
only reflects whether the action was sent to the server. It does not mean that the server actually shut down
successfully. If you need to ensure that the server is off, use the `poweroff` action


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
graceful_shutdown_response = hetzner.server_actions.graceful_shutdown(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsGracefulShutdownResponse`](./hetzner_python_sdk/pydantic/server_actions_graceful_shutdown_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/shutdown` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.power_off_server`<a id="hetznerserver_actionspower_off_server"></a>

Cuts power to the Server. This forcefully stops it without giving the Server operating system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power off should only be used when shutdown does not work.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
power_off_server_response = hetzner.server_actions.power_off_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsPowerOffServerResponse`](./hetzner_python_sdk/pydantic/server_actions_power_off_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/poweroff` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.power_on_server`<a id="hetznerserver_actionspower_on_server"></a>

Starts a Server by turning its power on.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
power_on_server_response = hetzner.server_actions.power_on_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsPowerOnServerResponse`](./hetzner_python_sdk/pydantic/server_actions_power_on_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/poweron` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.rebuild_server_from_image`<a id="hetznerserver_actionsrebuild_server_from_image"></a>

Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all data** on the target Server

The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it can be a completely fresh `system` Image provided by us. You can get a list of all available Images with `GET /images`.

Your Server will automatically be powered off before the rebuild command executes.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rebuild_server_from_image_response = hetzner.server_actions.rebuild_server_from_image(
    image="ubuntu-20.04",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### image: `str`<a id="image-str"></a>

ID or name of Image to rebuilt from.

##### id: `int`<a id="id-int"></a>

ID of the Server

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerActionsRebuildServerFromImageRequest`](./hetzner_python_sdk/type/server_actions_rebuild_server_from_image_request.py)
To select which Image to rebuild from you can either pass an ID or a name as the `image` argument. Passing a name only works for `system` Images since the other Image types do not have a name set.

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsRebuildServerFromImageResponse`](./hetzner_python_sdk/pydantic/server_actions_rebuild_server_from_image_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/rebuild` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.remove_from_placement_group`<a id="hetznerserver_actionsremove_from_placement_group"></a>

Removes a Server from a Placement Group.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_placement_group_response = (
    hetzner.server_actions.remove_from_placement_group(
        id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsRemoveFromPlacementGroupResponse`](./hetzner_python_sdk/pydantic/server_actions_remove_from_placement_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/remove_from_placement_group` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.request_console`<a id="hetznerserver_actionsrequest_console"></a>

Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be created to connect to the Server. How long the connection is open after the initial connect is not subject to this timeout.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_console_response = hetzner.server_actions.request_console(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsRequestConsoleResponse`](./hetzner_python_sdk/pydantic/server_actions_request_console_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/request_console` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.reset_server`<a id="hetznerserver_actionsreset_server"></a>

Cuts power to a Server and starts it again. This forcefully stops it without giving the Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent to pulling the power cord and plugging it in again. Reset should only be used when reboot does not work.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_server_response = hetzner.server_actions.reset_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsResetServerResponse`](./hetzner_python_sdk/pydantic/server_actions_reset_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/reset` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.reset_server_password`<a id="hetznerserver_actionsreset_server_password"></a>

Resets the root password. Only works for Linux systems that are running the qemu guest agent. Server must be powered on (status `running`) in order for this operation to succeed.

This will generate a new password for this Server and return it.

If this does not succeed you can use the rescue system to netboot the Server and manually change your Server password by hand.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_server_password_response = hetzner.server_actions.reset_server_password(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsResetServerPasswordResponse`](./hetzner_python_sdk/pydantic/server_actions_reset_server_password_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/reset_password` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_actions.soft_reboot_server`<a id="hetznerserver_actionssoft_reboot_server"></a>

Reboots a Server gracefully by sending an ACPI request. The Server operating system must support ACPI and react to the request, otherwise the Server will not reboot.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
soft_reboot_server_response = hetzner.server_actions.soft_reboot_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServerActionsSoftRebootServerResponse`](./hetzner_python_sdk/pydantic/server_actions_soft_reboot_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/actions/reboot` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_types.get_server_type`<a id="hetznerserver_typesget_server_type"></a>

Gets a specific Server type object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_server_type_response = hetzner.server_types.get_server_type(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of Server Type

#### 🔄 Return<a id="🔄-return"></a>

[`ServerTypesGetServerTypeResponse`](./hetzner_python_sdk/pydantic/server_types_get_server_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/server_types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.server_types.list_all_server_types`<a id="hetznerserver_typeslist_all_server_types"></a>

Gets all Server type objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_server_types_response = hetzner.server_types.list_all_server_types(
    name="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name.

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ServerTypesListAllServerTypesResponse`](./hetzner_python_sdk/pydantic/server_types_list_all_server_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/server_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.create_server_action`<a id="hetznerserverscreate_server_action"></a>

Creates a new Server. Returns preliminary information about the Server as well as an Action that covers progress of creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_server_action_response = hetzner.servers.create_server_action(
    image="ubuntu-20.04",
    name="my-server",
    server_type="cx11",
    automount=False,
    datacenter="nbg1-dc3",
    firewalls=[
        {
            "firewall": 1,
        }
    ],
    labels={},
    location="nbg1",
    networks=[456],
    placement_group=1,
    public_net={
        "enable_ipv4": True,
        "enable_ipv6": True,
    },
    ssh_keys=["my-ssh-key"],
    start_after_create=True,
    user_data="#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n",
    volumes=[123],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### image: `str`<a id="image-str"></a>

ID or name of the Image the Server is created from

##### name: `str`<a id="name-str"></a>

Name of the Server to create (must be unique per Project and a valid hostname as per RFC 1123)

##### server_type: `str`<a id="server_type-str"></a>

ID or name of the Server type this Server should be created with

##### automount: `bool`<a id="automount-bool"></a>

Auto-mount Volumes after attach

##### datacenter: `str`<a id="datacenter-str"></a>

ID or name of Datacenter to create Server in (must not be used together with location)

##### firewalls: [`ServersCreateServerActionRequestFirewalls`](./hetzner_python_sdk/type/servers_create_server_action_request_firewalls.py)<a id="firewalls-serverscreateserveractionrequestfirewallshetzner_python_sdktypeservers_create_server_action_request_firewallspy"></a>

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### location: `str`<a id="location-str"></a>

ID or name of Location to create Server in (must not be used together with datacenter)

##### networks: [`ServersCreateServerActionRequestNetworks`](./hetzner_python_sdk/type/servers_create_server_action_request_networks.py)<a id="networks-serverscreateserveractionrequestnetworkshetzner_python_sdktypeservers_create_server_action_request_networkspy"></a>

##### placement_group: `int`<a id="placement_group-int"></a>

ID of the Placement Group the server should be in

##### public_net: [`ServersCreateServerActionRequestPublicNet`](./hetzner_python_sdk/type/servers_create_server_action_request_public_net.py)<a id="public_net-serverscreateserveractionrequestpublicnethetzner_python_sdktypeservers_create_server_action_request_public_netpy"></a>


##### ssh_keys: [`ServersCreateServerActionRequestSshKeys`](./hetzner_python_sdk/type/servers_create_server_action_request_ssh_keys.py)<a id="ssh_keys-serverscreateserveractionrequestsshkeyshetzner_python_sdktypeservers_create_server_action_request_ssh_keyspy"></a>

##### start_after_create: `bool`<a id="start_after_create-bool"></a>

This automatically triggers a [Power on a Server-Server Action](https://docs.hetzner.cloud) after the creation is finished and is returned in the `next_actions` response object.

##### user_data: `str`<a id="user_data-str"></a>

Cloud-Init user data to use during Server creation. This field is limited to 32KiB.

##### volumes: [`ServersCreateServerActionRequestVolumes`](./hetzner_python_sdk/type/servers_create_server_action_request_volumes.py)<a id="volumes-serverscreateserveractionrequestvolumeshetzner_python_sdktypeservers_create_server_action_request_volumespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServersCreateServerActionRequest`](./hetzner_python_sdk/type/servers_create_server_action_request.py)
Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For `server_type` you can either use the ID as listed in `/server_types` or its name.  For `image` you can either use the ID as listed in `/images` or its name.  If you want to create the Server in a Location, you must set `location` to the ID or name as listed in `/locations`. This is the recommended way. You can be even more specific by setting `datacenter` to the ID or name as listed in `/datacenters`. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like `start_after_create` or `automount` will trigger Actions after the Server is created. Those Actions are listed in the `next_actions` field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in `ssh_keys`. If you do not specify any `ssh_keys` we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | `placement_error`                | An error during the placement occurred                     | | `primary_ip_assigned`            | The specified Primary IP is already assigned to a server   | | `primary_ip_datacenter_mismatch` | The specified Primary IP is in a different datacenter      | | `primary_ip_version_mismatch`    | The specified Primary IP has the wrong IP Version          | 

#### 🔄 Return<a id="🔄-return"></a>

[`ServersCreateServerActionResponse`](./hetzner_python_sdk/pydantic/servers_create_server_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.delete_server`<a id="hetznerserversdelete_server"></a>

Deletes a Server. This immediately removes the Server from your account, and it is no longer accessible. Any resources attached to the server (like Volumes, Primary IPs, Floating IPs, Firewalls, Placement Groups) are detached while the server is deleted.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_server_response = hetzner.servers.delete_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServersDeleteServerResponse`](./hetzner_python_sdk/pydantic/servers_delete_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.get_all`<a id="hetznerserversget_all"></a>

Returns all existing Server objects

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.servers.get_all(
    name="string_example",
    label_selector="string_example",
    sort="id",
    status="initializing",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Can be used multiple times. The response will only contain Server matching the status

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`ServersGetAllResponse`](./hetzner_python_sdk/pydantic/servers_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.get_metrics_for_server`<a id="hetznerserversget_metrics_for_server"></a>

Get Metrics for specified Server.

You must specify the type of metric to get: cpu, disk or network. You can also specify more than one type by comma separation, e.g. cpu,disk.

Depending on the type you will get different time series data

| Type    | Timeseries              | Unit      | Description                                          |
|---------|-------------------------|-----------|------------------------------------------------------|
| cpu     | cpu                     | percent   | Percent CPU usage                                    |
| disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              |
|         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             |
|         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                |
|         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             |
| network | network.0.pps.in        | packets/s | Public Network interface packets per second received |
|         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     |
|         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            |
|         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |

Metrics are available for the last 30 days only.

If you do not provide the step argument we will automatically adjust it so that a maximum of 200 samples are returned.

We limit the number of samples returned to a maximum of 500 and will adjust the step parameter accordingly.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metrics_for_server_response = hetzner.servers.get_metrics_for_server(
    id=1,
    type="cpu",
    start="start_example",
    end="end_example",
    step="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### type: `str`<a id="type-str"></a>

Type of metrics to get

##### start: `str`<a id="start-str"></a>

Start of period to get Metrics for (in ISO-8601 format)

##### end: `str`<a id="end-str"></a>

End of period to get Metrics for (in ISO-8601 format)

##### step: `str`<a id="step-str"></a>

Resolution of results in seconds

#### 🔄 Return<a id="🔄-return"></a>

[`ServersGetMetricsForServerResponse`](./hetzner_python_sdk/pydantic/servers_get_metrics_for_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}/metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.get_server`<a id="hetznerserversget_server"></a>

Returns a specific Server object. The Server must exist inside the Project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_server_response = hetzner.servers.get_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

#### 🔄 Return<a id="🔄-return"></a>

[`ServersGetServerResponse`](./hetzner_python_sdk/pydantic/servers_get_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.servers.update_server`<a id="hetznerserversupdate_server"></a>

Updates a Server. You can update a Server’s name and a Server’s labels.
Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).
Also note that when updating labels, the Server’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_server_response = hetzner.servers.update_server(
    id=1,
    labels={
        "labelkey": "value",
    },
    name="my-server",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Server

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### name: `str`<a id="name-str"></a>

New name to set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServersUpdateServerRequest`](./hetzner_python_sdk/type/servers_update_server_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServersUpdateServerResponse`](./hetzner_python_sdk/pydantic/servers_update_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/servers/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.attach_volume_to_server`<a id="hetznervolume_actionsattach_volume_to_server"></a>

Attaches a Volume to a Server. Works only if the Server is in the same Location as the Volume.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
attach_volume_to_server_response = hetzner.volume_actions.attach_volume_to_server(
    server=43,
    id=1,
    automount=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### server: `int`<a id="server-int"></a>

ID of the Server the Volume will be attached to

##### id: `int`<a id="id-int"></a>

ID of the Volume

##### automount: `bool`<a id="automount-bool"></a>

Auto-mount the Volume after attaching it

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VolumeActionsAttachVolumeToServerRequest`](./hetzner_python_sdk/type/volume_actions_attach_volume_to_server_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsAttachVolumeToServerResponse`](./hetzner_python_sdk/pydantic/volume_actions_attach_volume_to_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions/attach` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.change_protection_volume`<a id="hetznervolume_actionschange_protection_volume"></a>

Changes the protection configuration of a Volume.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_protection_volume_response = hetzner.volume_actions.change_protection_volume(
    id=1,
    delete=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

##### delete: `bool`<a id="delete-bool"></a>

If true, prevents the Volume from being deleted

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VolumeActionsChangeProtectionVolumeRequest`](./hetzner_python_sdk/type/volume_actions_change_protection_volume_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsChangeProtectionVolumeResponse`](./hetzner_python_sdk/pydantic/volume_actions_change_protection_volume_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions/change_protection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.change_size`<a id="hetznervolume_actionschange_size"></a>

Changes the size of a Volume. Note that downsizing a Volume is not possible.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_size_response = hetzner.volume_actions.change_size(
    size=50,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### size: `Union[int, float]`<a id="size-unionint-float"></a>

New Volume size in GB (must be greater than current size)

##### id: `int`<a id="id-int"></a>

ID of the Volume

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VolumeActionsChangeSizeRequest`](./hetzner_python_sdk/type/volume_actions_change_size_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsChangeSizeResponse`](./hetzner_python_sdk/pydantic/volume_actions_change_size_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions/resize` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.detach_volume_from_server`<a id="hetznervolume_actionsdetach_volume_from_server"></a>

Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a later time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detach_volume_from_server_response = hetzner.volume_actions.detach_volume_from_server(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsDetachVolumeFromServerResponse`](./hetzner_python_sdk/pydantic/volume_actions_detach_volume_from_server_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions/detach` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.get_action`<a id="hetznervolume_actionsget_action"></a>

Returns a specific Action for a Volume.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_response = hetzner.volume_actions.get_action(
    id=1,
    action_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

##### action_id: `int`<a id="action_id-int"></a>

ID of the Action

#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsGetActionResponse`](./hetzner_python_sdk/pydantic/volume_actions_get_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions/{action_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.get_action_by_id`<a id="hetznervolume_actionsget_action_by_id"></a>

Returns a specific Action object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_action_by_id_response = hetzner.volume_actions.get_action_by_id(
    id=42,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Action.

#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsGetActionByIdResponse`](./hetzner_python_sdk/pydantic/volume_actions_get_action_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/actions/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.get_all_actions`<a id="hetznervolume_actionsget_all_actions"></a>

Returns all Action objects. You can `sort` the results by using the sort URI parameter, and filter them with the `status` and `id` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_response = hetzner.volume_actions.get_all_actions(
    id=42,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Filter the actions by ID. Can be used multiple times. The response will only contain actions matching the specified IDs. 

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsGetAllActionsResponse`](./hetzner_python_sdk/pydantic/volume_actions_get_all_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volume_actions.get_all_actions_0`<a id="hetznervolume_actionsget_all_actions_0"></a>

Returns all Action objects for a Volume. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_actions_0_response = hetzner.volume_actions.get_all_actions_0(
    id=1,
    sort="id",
    status="running",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

##### sort: `str`<a id="sort-str"></a>

Sort actions by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### status: `str`<a id="status-str"></a>

Filter the actions by status. Can be used multiple times. The response will only contain actions matching the specified statuses. 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`VolumeActionsGetAllActions200Response`](./hetzner_python_sdk/pydantic/volume_actions_get_all_actions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volumes.create_volume`<a id="hetznervolumescreate_volume"></a>

Creates a new Volume attached to a Server. If you want to create a Volume that is not attached to a Server, you need to provide the `location` key instead of `server`. This can be either the ID or the name of the Location this Volume will be created in. Note that a Volume can be attached to a Server only in the same Location as the Volume itself.

Specifying the Server during Volume creation will automatically attach the Volume to that Server after it has been initialized. In that case, the `next_actions` key in the response is an array which contains a single `attach_volume` action.

The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but has to start and end with an alphanumeric character. The total length is limited to 64 characters. Volume names must be unique per Project.

#### Call specific error codes<a id="call-specific-error-codes"></a>

| Code                                | Description                                         |
|-------------------------------------|-----------------------------------------------------|
| `no_space_left_in_location`         | There is no volume space left in the given location |


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_volume_response = hetzner.volumes.create_volume(
    name="databases-storage",
    size=42,
    automount=False,
    format="xfs",
    labels={
        "labelkey": "value",
    },
    location="nbg1",
    server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the volume

##### size: `int`<a id="size-int"></a>

Size of the Volume in GB

##### automount: `bool`<a id="automount-bool"></a>

Auto-mount Volume after attach. `server` must be provided.

##### format: `str`<a id="format-str"></a>

Format Volume after creation. One of: `xfs`, `ext4`

##### labels: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="labels-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

User-defined labels (key-value pairs)

##### location: `str`<a id="location-str"></a>

Location to create the Volume in (can be omitted if Server is specified)

##### server: `int`<a id="server-int"></a>

Server to which to attach the Volume once it's created (Volume will be created in the same Location as the server)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VolumesCreateVolumeRequest`](./hetzner_python_sdk/type/volumes_create_volume_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VolumesCreateVolumeResponse`](./hetzner_python_sdk/pydantic/volumes_create_volume_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volumes.delete_volume`<a id="hetznervolumesdelete_volume"></a>

Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached to a Server and it must not have delete protection enabled.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hetzner.volumes.delete_volume(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volumes.get_all`<a id="hetznervolumesget_all"></a>

Gets all existing Volumes that you have available.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = hetzner.volumes.get_all(
    status="available",
    sort="id",
    name="string_example",
    label_selector="string_example",
    page=2,
    per_page=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Can be used multiple times. The response will only contain Volumes matching the status.

##### sort: `str`<a id="sort-str"></a>

Sort resources by field and direction. Can be used multiple times. For more information, see \"[Sorting](https://docs.hetzner.cloud)\". 

##### name: `str`<a id="name-str"></a>

Filter resources by their name. The response will only contain the resources matching the specified name. 

##### label_selector: `str`<a id="label_selector-str"></a>

Filter resources by labels. The response will only contain resources matching the label selector. For more information, see \"[Label Selector](https://docs.hetzner.cloud)\". 

##### page: `int`<a id="page-int"></a>

Page number to return. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

##### per_page: `int`<a id="per_page-int"></a>

Maximum number of entries returned per page. For more information, see \"[Pagination](https://docs.hetzner.cloud)\".

#### 🔄 Return<a id="🔄-return"></a>

[`VolumesGetAllResponse`](./hetzner_python_sdk/pydantic/volumes_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volumes.get_by_id`<a id="hetznervolumesget_by_id"></a>

Gets a specific Volume object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = hetzner.volumes.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume

#### 🔄 Return<a id="🔄-return"></a>

[`VolumesGetByIdResponse`](./hetzner_python_sdk/pydantic/volumes_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hetzner.volumes.update_volume_properties`<a id="hetznervolumesupdate_volume_properties"></a>

Updates the Volume properties.

Note that when updating labels, the volume’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_volume_properties_response = hetzner.volumes.update_volume_properties(
    id=1,
    labels={
        "labelkey": "value",
    },
    name="database-storage",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

ID of the Volume to update

##### labels: [`VolumesUpdateVolumePropertiesRequestLabels`](./hetzner_python_sdk/type/volumes_update_volume_properties_request_labels.py)<a id="labels-volumesupdatevolumepropertiesrequestlabelshetzner_python_sdktypevolumes_update_volume_properties_request_labelspy"></a>


##### name: `str`<a id="name-str"></a>

New Volume name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VolumesUpdateVolumePropertiesRequest`](./hetzner_python_sdk/type/volumes_update_volume_properties_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VolumesUpdateVolumePropertiesResponse`](./hetzner_python_sdk/pydantic/volumes_update_volume_properties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/volumes/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
