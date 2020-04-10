# -*- coding: utf-8 -*-
name = "katana"

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = "3.1v2"
version = __version__.replace("v", ".") + "+local.1.0.0"

description = "Look development and lighting. Built for studios. Loved by artists."

authors = ["The Foundry", "Joseph Yu"]

variants = [["platform-linux", "arch-x86_64"]]

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


build_command = r"""
set -euf -o pipefail

# Setup variables to be used
case "$REZ_ARCH_VERSION" in
    x86_64) INSTALLER_ARCH="x86-release-64";;
    *)
        printf '\nERROR: Unsupported CPU architecture "%s"\n' \
            "$REZ_ARCH_VERSION"
        exit 1
        ;;
esac
INSTALLER_TAR="Katana{version}-"$REZ_PLATFORM_VERSION"-"$INSTALLER_ARCH".tgz"
KATANA_TAR="katana_files.tar.gz"

# Download Katana
INSTALLER_PATH="$(readlink -e "$REZ_BUILD_SOURCE_PATH"/"$INSTALLER_TAR")" \
|| INSTALLER_PATH="$(readlink -e "$INSTALLER_TAR")" \
|| {open_curly_bracket}
    # Setup: curl "{CURL_FLAGS}" ...
    # Show progress bar if output to terminal, else silence with error
    declare -a CURL_FLAGS
    CURL_FLAGS=("-L")
    [ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

    RELEASE_URL="http://thefoundry.s3.amazonaws.com/products/katana/releases"
    TAR_URL="$RELEASE_URL"/{version}/"$INSTALLER_TAR"

    # Downloads into current folder, which is $REZ_BUILD_PATH
    printf '\nDownloading "%s"\n' "$TAR_URL"
    time curl {CURL_FLAGS} -O "$TAR_URL"
    INSTALLER_PATH="$(readlink -e "$INSTALLER_TAR")"
{close_curly_bracket}


if [[ "$REZ_BUILD_INSTALL" -eq 1 ]]
then
    printf '\nExtracting "%s"\nfrom: "%s"\ninto: "%s"\n' \
        "$KATANA_TAR" "$INSTALLER_PATH" "$REZ_BUILD_INSTALL_PATH"

    # Double extract by piping $KATANA_TAR into stdout for second tar command
    time tar -xzO -f "$INSTALLER_PATH" "$KATANA_TAR" \
    | tar -xz -C "$REZ_BUILD_INSTALL_PATH"
fi
""".format(
    version=__version__,
    CURL_FLAGS="${{CURL_FLAGS[@]}}",
    open_curly_bracket="{{",  # Need these to escape {} expansion by
    close_curly_bracket="}}",  # rez, see terminal output of: rez build
)


def commands():
    """Commands to set up environment for ``rez env katana``"""
    env.PATH.append("{root}")
