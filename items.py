import os
users_sshkey_dir = os.getcwd() + '/data/users/ssh'

users = {}

files = {}

directories = {}

for user, options in sorted(node.metadata.get('users', {}).items()):
    if options.get('groups', {}):
        users[user] = {
            'uid': options.get('uid'),
            'home': options.get('home'),
            'groups': [
                "{}".format(options.get('groups', {}))
            ]
        }
    else:
        users[user] = {
            'uid': options.get('uid'),
            'home': options.get('home'),
        }

    directories['{}/.config'.format(options.get('home'))] = {
        'mode': '0700',
        'owner': user,
        'group': user,
    }

    if node.has_bundle('openssh'):
        directories['{}/.ssh'.format(options.get('home'))] = {
            'mode': '0700',
            'owner': user,
        }

        files['{}/.ssh/authorized_keys'.format(options.get('home'))] = {
            'source': '{}/{}.pub'.format(users_sshkey_dir, user),
            'mode': '0600',
            'owner': user,
        }
