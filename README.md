# bundlewrap-users

`bundlewrap-users` adds users defined by metadata.
It also integrates with the `openssh` bundle to add ssh authorized keys.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedberry 24 | `[x]` |

## Integrations

* Bundles:
  * (openssh)[https://github.com/rullmann/bundlewrap-openssh]
    * Ability to add ssh keys for users
      * Requires a data dir: `<bwrepo>/data/users/ssh`

## Metadata

    'metadata': {
        'users': {
            'someuser': {
                'uid': "1234",
                'home': "/home/someuser",
            },
        },
    },
