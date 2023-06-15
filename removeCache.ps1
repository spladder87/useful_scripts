$folders = Get-ChildItem . -recurse | Where-Object {$_.Name -match "__pycache__"} | Select-Object -ExpandProperty FullName

if ($folders) {
    Foreach ($folder in $folders)

    {
        "Test to see if folder [$folder]  exists"
        if (Test-Path -Path $folder) {
            "Path exists! Removing it"
            Remove-Item $folder -Recurse -Force -Confirm:$false
        } else {
            # JUST IN CASE
            "Path doesn't exist."
        }
    }

} else {
    "No __pycache__ exist"
}


