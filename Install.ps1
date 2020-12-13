$Vsix = (Get-Item .\vscode-essentials-*.vsix).FullName
code --install-extension $Vsix