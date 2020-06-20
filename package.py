# -*- coding: utf-8 -*-
name = "katana"

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = "3.5v3"
version = __version__.replace("v", ".") + "+local.1.0.0"

description = "Look development and lighting. Built for studios. Loved by artists."

authors = ["The Foundry", "Joseph Yu"]

variants = [
    ["platform-linux", "arch-x86_64"],
    ["platform-windows", "arch-AMD64"],
]

tools = ["katana"]
# @late()
# def tools():
#     import os
#     bin_path = os.path.join(str(this.root), 'bin')
#     executables = []
#     for item in os.listdir(bin_path):
#         path = os.path.join(bin_path, item)
#         if os.access(path, os.X_OK) and not os.path.isdir(path):
#             executables.append(item)
#     return executables


@early()
def build_command():
    import os

    if os.name == "nt":
        # Rez Windows Shell defaults to cmd
        command = 'powershell -File "{0}" "{1}"'
        prefix = "%REZ_BUILD_SOURCE_PATH%"
        script = "windows.ps1"
    else:
        command = 'bash "{0}" "{1}"'
        prefix = "${{REZ_BUILD_SOURCE_PATH}}"
        script = "linux.bash"

    return command.format(os.path.join(prefix, script), __version__)


def commands():
    """Commands to set up environment for ``rez env katana``"""
    import os

    if os.name == "nt":
        env.PATH.append(os.path.join("{root}", "bin"))
    else:
        env.PATH.append("{root}")
