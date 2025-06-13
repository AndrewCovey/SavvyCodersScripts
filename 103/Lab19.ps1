#  This is a powershell script to add notepad shortcut to a windows desktop.  For this challenge i want you to run this script(Might have to look up how to run Powershell Script).

$TargetFile = "$env:SystemRoot\System32\notepad.exe"
$ShortcutFile = "$env:Public\Public Desktop\Notepad.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutFile)
$Shortcut.TargetPath = $TargetFile
$Shortcut.WorkingDirectory = "$env:SystemRoot\System32"
$Shortcut.IconLocation = "$TargetFile, 0"
$Shortcut.Save()

# Okay, a couple of things...
# One the origional version of this script was missing a couple lines, which I corrected.
# Two, the script wants to be run as Administrator, but we don't technically have the administrator account's password, our PCs auto login as User.