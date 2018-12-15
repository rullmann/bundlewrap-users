# bundlewrap-users

`bundlewrap-users` adds users defined by metadata.
It also integrates with the `openssh` bundle to add ssh authorized keys.

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
                'groups': 'wheel\anothergroup', # optional, add users to one or more groups. Make sure groups are separated by '\n' 
                'deploy_authorized_keys': True, # optional, toggles deployment of ssh authorized keys fot a user
            },
        },
    },
