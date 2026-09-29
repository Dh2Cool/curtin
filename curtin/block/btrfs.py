# This file is part of curtin. See LICENSE file for copyright and license info.

from curtin import util


def btrfs_subvolume_create(device, subvol_path):

    if not device:
        raise ValueError('device is required')
    if not subvol_path:
        raise ValueError('subvol path is required and must be relative')
    if '/' in subvol_path:
        raise ValueError(
            'nested subvolume paths not supported: %s' % subvol_path)

    with util.temporary_mount(device) as mnt:
        target = mnt / subvol_path
        util.subp(["btrfs", "subvolume", "create", "--", str(target)],
                  capture=True)
