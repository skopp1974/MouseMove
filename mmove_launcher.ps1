# Define the path to the executable
$exePath = "C:\windows\system32\move.exe"

# Define the number of times to launch the executable
$launchCount = 5

# Define the interval between launches in seconds
$launchInterval = 2

# Loop to launch the executable multiple times
for ($i = 1; $i -le $launchCount; $i++) {
    # Start the executable
    Start-Process -FilePath $exePath

    # Wait for the specified interval
    Start-Sleep -Seconds $launchInterval
}
