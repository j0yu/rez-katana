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
VERSION="$1"
INSTALLER_TAR="Katana${VERSION}-"$REZ_PLATFORM_VERSION"-"$INSTALLER_ARCH".tgz"
KATANA_TAR="katana_files.tar.gz"

# Download Katana
INSTALLER_PATH="$(readlink -e "$REZ_BUILD_SOURCE_PATH"/"$INSTALLER_TAR")" \
|| INSTALLER_PATH="$(readlink -e "$INSTALLER_TAR")" \
|| {
    # Setup: curl "{CURL_FLAGS}" ...
    # Show progress bar if output to terminal, else silence with error
    declare -a CURL_FLAGS
    CURL_FLAGS=("-L")
    [ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

    RELEASE_URL="http://thefoundry.s3.amazonaws.com/products/katana/releases"
    TAR_URL="$RELEASE_URL"/"${VERSION}"/"$INSTALLER_TAR"

    # Downloads into current folder, which is $REZ_BUILD_PATH
    printf '\nDownloading "%s"\n' "$TAR_URL"
    time curl "${CURL_FLAGS[@]}" -O "$TAR_URL"
    INSTALLER_PATH="$(readlink -e "$INSTALLER_TAR")"
}


if [[ "$REZ_BUILD_INSTALL" -eq 1 ]]
then
    printf '\nExtracting "%s"\nfrom: "%s"\ninto: "%s"\n' \
        "$KATANA_TAR" "$INSTALLER_PATH" "$REZ_BUILD_INSTALL_PATH"

    # Double extract by piping $KATANA_TAR into stdout for second tar command
    time tar -xzO -f "$INSTALLER_PATH" "$KATANA_TAR" \
    | tar -xz -C "$REZ_BUILD_INSTALL_PATH"
fi

