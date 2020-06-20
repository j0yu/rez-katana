# See https://learn.foundry.com/katana/Content/ug/installation_licensing/installing_windows.html#Installi2

$WEB_CLIENT = New-Object System.Net.WebClient
$ZIP_FILE = "katana.zip"
$VERSION = $Args[0]
$FILENAME = "Katana$VERSION-win-x86-release-64"
$INSTALLER_URL = "https://thefoundry.s3.amazonaws.com/products/katana/releases/$VERSION/$FILENAME.zip"

echo "Downloading $INSTALLER_URL"
$WEB_CLIENT.DownloadFile("$INSTALLER_URL", "$ZIP_FILE")
Expand-Archive "$ZIP_FILE" -DestinationPath .
ls

Start-Process -FilePath "$FILENAME.exe" -ArgumentList "/verysilent","/dir=$Env:REZ_BUILD_INSTALL_PATH" -ErrorAction Stop -Wait -WorkingDirectory .
