
import os
import pwd
import grp

dirname = '.'

for entry in sorted(os.listdir(dirname), key = lambda line: line.lower()):

    fullname = os.path.join(dirname, entry)

    if os.path.isdir(fullname):
        s = 'd'
    elif os.path.isfile(fullname):
        s = 'f'
    else:
        s = '?'

    if os.path.isfile(fullname):
        size = os.path.getsize(fullname)
    else:
        size = None

    permissions = oct(os.stat(fullname).st_mode)[-3:]

    uid = os.stat(fullname).st_uid
    gid = os.stat(fullname).st_gid

    username = pwd.getpwuid(uid).pw_name
    groupname = grp.getgrgid(gid).gr_name

    if size is not None:
        print(f'{s} {size:10} {permissions} {username:12} {groupname:6} {entry}')
    else:
        print(f'{s} {" "* 10} {permissions} {username:12} {groupname:6} {entry}')
