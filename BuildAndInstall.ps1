Remove-Item $(Get-Item .\vscode-essentials-*.vsix).FullName
npm run build
try {
    npm version patch
} catch {}
.\Install.ps1