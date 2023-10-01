$lptAndCom = '{4d36e978-e325-11ce-bfc1-08002be10318}'
# get-wmiobject -Class win32_pnpentity | Where-Object ClassGuid -eq $lptAndCom | Select-Object name
get-wmiobject -Class win32_pnpentity | Where-Object ClassGuid -eq $lptAndCom