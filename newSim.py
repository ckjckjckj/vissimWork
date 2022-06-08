#!/user/env python
# _*_ coding:utf-8 _*_
import win32com.client as com
import pythoncom
import os

pythoncom.CoInitialize()
# Connecting the COM Server
Vissim = com.Dispatch("Vissim.Vissim.430")

#PTVVissimInstallationPath = Vissim.AttValue(r"D:\Program Files (x86)\PTV_Vision\VISSIM430\Exe\vissim.exe")    # directory of your PTV Vissim installation (where vissim.exe is located)

# For this example, units are set to Metric.
# Note: PTV Vissim coordinates are always in meters [m]
#UnitCurrent = Vissim.Net.NetPara.AttValue('UnitLenShort')
UnitAttributes = ('UnitAccel', 'UnitLenLong', 'UnitLenShort', 'UnitLenVeryShort', 'UnitSpeed', 'UnitSpeedSmall')
for UnitAttrCurr in UnitAttributes:
    Vissim.Net.NetPara.SetAttValue(UnitAttrCurr, 0)         # 0: Metric [m], 1: Imperial [ft]

# Zoom Network Editor
Vissim.Graphics.CurrentNetworkWindow.ZoomTo(-300, -300, 300, 300)
