#!/user/env python

"""
Created on Sun Dec  7 14:15:31 2008

@author: Mr.Chen
"""
import win32com.client as com
import pythoncom
import copy
import numpy as np
import data_select
import xml.dom.minidom
import threading
import time
myVis = 0


class myVissim(object):
    def __init__(self, data, entro_data, veh_flow_data, ped_flow_data, bic_flow_data, veh_ratio_data, veh_route_data,
                 bic_route_data, ped_route_data, can_data, speed_data, sign_data):
        self.sim_time = data['fzt']
        self.run_freq = data['rt']
        self.sim_speed = data['rs']
        self.sim_resol = data['fzjd']
        self.seed_incre = data['sjzzzl']
        self.seed = data['sjzz']
        self.stop_time = data['zdt']
        self.flow_incre = data['llzl']
        self.is_max_speed = data['zuida']
        self.cross_name = entro_data['crossname']
        self.cross_id = entro_data['crossid']
        self.east_name = entro_data['eastname']
        self.west_name = entro_data['westname']
        self.south_name = entro_data['southname']
        self.north_name = entro_data['northname']
        self.east_veh_flow = veh_flow_data['EastVeh']
        self.west_veh_flow = veh_flow_data['WestVeh']
        self.south_veh_flow = veh_flow_data['SouthVeh']
        self.north_veh_flow = veh_flow_data['NorthVeh']
        self.east_type_flow = veh_flow_data['EastFlowType']
        self.west_type_flow = veh_flow_data['WestFlowType']
        self.south_type_flow = veh_flow_data['SouthFlowType']
        self.north_type_flow = veh_flow_data['NorthFlowType']
        self.east_ped_flow = ped_flow_data['EastPed']
        self.west_ped_flow = ped_flow_data['WestPed']
        self.south_ped_flow = ped_flow_data['SouthPed']
        self.north_ped_flow = ped_flow_data['NorthPed']
        self.east_bic_flow = bic_flow_data['EastBic']
        self.west_bic_flow = bic_flow_data['WestBic']
        self.south_bic_flow = bic_flow_data['SouthBic']
        self.north_bic_flow = bic_flow_data['NorthBic']
        self.east_car = veh_ratio_data['EastCar']
        self.west_car = veh_ratio_data['WestCar']
        self.south_car = veh_ratio_data['SouthCar']
        self.north_car = veh_ratio_data['NorthCar']
        self.east_truck = veh_ratio_data['EastTruck']
        self.west_truck = veh_ratio_data['WestTruck']
        self.south_truck = veh_ratio_data['SouthTruck']
        self.north_truck = veh_ratio_data['NorthTruck']
        self.east_veh_left = veh_route_data['Eastleft']
        self.west_veh_left = veh_route_data['Westleft']
        self.south_veh_left = veh_route_data['Southleft']
        self.north_veh_left = veh_route_data['Northleft']
        self.east_veh_stri = veh_route_data['EastStraight']
        self.west_veh_stri = veh_route_data['WestStraight']
        self.south_veh_stri = veh_route_data['SouthStraight']
        self.north_veh_stri = veh_route_data['NorthStraight']
        self.east_veh_right = veh_route_data['EastRight']
        self.west_veh_right = veh_route_data['WestRight']
        self.south_veh_right = veh_route_data['SouthRight']
        self.north_veh_right = veh_route_data['NorthRight']
        self.east_bic_left = bic_route_data['BicEastleft']
        self.west_bic_left = bic_route_data['BicWestleft']
        self.south_bic_left = bic_route_data['BicSouthleft']
        self.north_bic_left = bic_route_data['BicNorthleft']
        self.east_bic_stri = bic_route_data['BicEastStraight']
        self.west_bic_stri = bic_route_data['BicWestStraight']
        self.south_bic_stri = bic_route_data['BicSouthStraight']
        self.north_bic_stri = bic_route_data['BicNorthStraight']
        self.east_bic_right = bic_route_data['BicEastRight']
        self.west_bic_right = bic_route_data['BicWestRight']
        self.south_bic_right = bic_route_data['BicSouthRight']
        self.north_bic_right = bic_route_data['BicNorthRight']
        self.east_ped_along = ped_route_data['EastCW']
        self.west_ped_along = ped_route_data['WestCW']
        self.south_ped_along = ped_route_data['SouthCW']
        self.north_ped_along = ped_route_data['NorthCW']
        self.east_ped_rev = ped_route_data['EastAnti']
        self.west_ped_rev = ped_route_data['WestAnti']
        self.south_ped_rev = ped_route_data['SouthAnti']
        self.north_ped_rev = ped_route_data['NorthAnti']
        self.east_ent_num = can_data['EastEntNum']
        self.west_ent_num = can_data['WestEntNum']
        self.south_ent_num = can_data['SouthEntNum']
        self.north_ent_num = can_data['NorthEntNum']
        self.east_exit_num = can_data['EastExNum']
        self.west_exit_num = can_data['WestExNum']
        self.south_exit_num = can_data['SouthExNum']
        self.north_exit_num = can_data['NorthExNum']
        self.east_ent_width = can_data['EastWidth']
        self.west_ent_width = can_data['WestWidth']
        self.south_ent_width = can_data['SouthWidth']
        self.north_ent_width = can_data['NorthWidth']
        self.car_speed = speed_data['carSpeed']
        self.truck_speed = speed_data['truckSpeed']
        self.bic_speed = speed_data['bicycleSpeed']
        self.ped_speed = speed_data['pedSpeed']
        self.cycletime = sign_data['cycletime']
        self.east_left = sign_data['EastLeft']
        self.west_left = sign_data['WestLeft']
        self.south_left = sign_data['SouthLeft']
        self.north_left = sign_data['NorthLeft']
        self.east_stri = sign_data['EastStraight']
        self.west_stri = sign_data['WestStraight']
        self.south_stri = sign_data['SouthStraight']
        self.north_stri = sign_data['NorthStraight']
        self.path = r'C:\Users\Mr.Chen\Desktop\new/'
        self.filename = r'11.inpx'
        self.sigfilename = '111.sig'
        filename = self.path + self.filename
        pythoncom.CoInitialize()
        vis_obj = com.Dispatch("Vissim.Vissim-64.10")
        vis_obj.LoadNet(filename)
        self.vis = vis_obj

    def set_can(self):
        east_ent_num = self.east_ent_num
        west_ent_num = self.west_ent_num
        south_ent_num = self.south_ent_num
        north_ent_num = self.north_ent_num
        east_exit_num = self.east_exit_num
        west_exit_num = self.west_exit_num
        south_exit_num = self.south_exit_num
        north_exit_num = self.north_exit_num
        east_ent_width = self.east_ent_width
        west_ent_width = self.west_ent_width
        south_ent_width = self.south_ent_width
        north_ent_width = self.north_ent_width
        east_veh_flow = self.east_veh_flow
        west_veh_flow = self.west_veh_flow
        south_veh_flow = self.south_veh_flow
        north_veh_flow = self.north_veh_flow
        east_type_flow = self.east_type_flow
        west_type_flow = self.west_type_flow
        south_type_flow = self.south_type_flow
        north_type_flow = self.north_type_flow
        type_flag_list = [east_type_flow, south_type_flow, west_type_flow, north_type_flow]

        ent_num_list = [east_ent_num, south_ent_num, west_ent_num, north_ent_num]
        exit_num_list = [east_exit_num, south_exit_num, west_exit_num, north_exit_num]
        veh_flow_list = [east_veh_flow, south_veh_flow, west_veh_flow, north_veh_flow]
        veh_type_list = ['Exact' if i == 1 else 'Stochastic' for i in type_flag_list]
        LinksEnter = [1] * 4
        # unsigned int Key, BSTR WktLinestring 'LINESTRING(PosX1 PosY1, PosX2 PosY2, ..., PosXn PosYn)', SAFEARRAY(double) LaneWidths [WidthLane1, WiidthLane2, ... WidthLaneN]
        LinksEnter[0] = self.vis.Net.Links.AddLink(1, 'LINESTRING(320 8, 45 8)', [east_ent_width] * east_ent_num)
        LinksEnter[1] = self.vis.Net.Links.AddLink(2, 'LINESTRING(15 -310, 15 -35)', [south_ent_width] * south_ent_num)
        LinksEnter[2] = self.vis.Net.Links.AddLink(3, 'LINESTRING(-300 -2, -25 -2)', [west_ent_width] * west_ent_num)
        LinksEnter[3] = self.vis.Net.Links.AddLink(4, 'LINESTRING(5 310, 5 35)', [north_ent_width] * north_ent_num)

        linkExitNum = [east_exit_num, south_exit_num, west_exit_num, north_exit_num]
        # Opposite direction:
        LinksExit = [0] * 4
        for cnt_Enter in range(len(LinksEnter)):
            LinksExit[cnt_Enter] = self.vis.Net.Links.GenerateOppositeDirection(LinksEnter[cnt_Enter], linkExitNum[
                cnt_Enter])  # ILink* Link, unsigned int NumberOfLanes
        self.linkEnter = LinksEnter
        self.linkExit = LinksExit
        # --------------------------------------
        # Connectors
        # --------------------------------------
        # Input parameters of AddConnector:
        # 1: unsigned int Key   = attribute Number (No)         | example: 0 or 123
        # 2: ILane* FromLane                                    | example: Vissim.Net.Links.ItemByKey(1).Lanes.ItemByKey(1)
        # 3: double FromPos                                     | example: 200
        # 4: ILane* ToLane                                      | example: Vissim.Net.Links.ItemByKey(2).Lanes.ItemByKey(1)
        # 5: double ToPos                                       | example: 0
        # 6: unsigned int NumberOfLanes                         | example: 1, 2, ...
        # 7: BSTR WktLinestring = attribute Points3D            | example: 'LINESTRING(PosX2 PosY2 PosZ2, ..., PosXn-1 PosYn-1 PosZn-1)' with Pos as double; PosZ is optional; Pos1 and Posn automatically created; No additional points: 'LINESTRING EMPTY'
        conIdList = []
        for cnt_Enter in range(len(LinksEnter)):  # 0、1、2、3
            for cnt_Exit in range(len(LinksExit)):  # 0、1、2、3
                if cnt_Enter != cnt_Exit:
                    conId = 10000 + (cnt_Enter) * 10 + cnt_Exit
                    timeId = (cnt_Enter) * 10 + cnt_Exit + 1

                    if (cnt_Exit - cnt_Enter + len(LinksEnter)) % len(LinksEnter) == 1:
                        self.vis.Net.Links.AddConnector(conId,
                                                        LinksEnter[cnt_Enter].Lanes.ItemByKey(ent_num_list[cnt_Enter]),
                                                        275,
                                                        LinksExit[cnt_Exit].Lanes.ItemByKey(exit_num_list[cnt_Exit]), 0,
                                                        1,
                                                        'LINESTRING(0 2,25 20,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8 0)')
                        print('1左转->En:' + str(cnt_Enter) + '->Ex:' + str(cnt_Exit))

                    elif abs(cnt_Exit - cnt_Enter) == 2:
                        self.vis.Net.Links.AddConnector(conId,
                                                        LinksEnter[cnt_Enter].Lanes.ItemByKey(2), 275,
                                                        LinksExit[cnt_Exit].Lanes.ItemByKey(
                                                            exit_num_list[cnt_Exit] - (ent_num_list[cnt_Enter] - 2)), 0,
                                                        ent_num_list[cnt_Enter] - 2,
                                                        'LINESTRING(10 12,125 120,10 12,11 13,12 14,13 15,14 16,15 17,16 18,17 19)')
                        print('2直行->En:' + str(cnt_Enter) + '->Ex:' + str(cnt_Exit))

                    else:
                        self.vis.Net.Links.AddConnector(conId,
                                                        LinksEnter[cnt_Enter].Lanes.ItemByKey(1), 275,
                                                        LinksExit[cnt_Exit].Lanes.ItemByKey(1), 0, 1,
                                                        'LINESTRING(20 22,25 20,20 21,21 22,22 23,23 24,24 25,25 26,26 27,27 28)')  #
                        print('3右转->En:' + str(cnt_Enter) + '->Ex:' + str(cnt_Exit))
                    conIdList.append(conId)

        for conId in conIdList:
            # pass
            self.vis.Net.Links.ItemByKey(conId).RecalculateSpline()

        for vehId in range(len(LinksEnter)):
            VehInput = self.vis.Net.VehicleInputs.AddVehicleInput(vehId + 1,
                                                                  LinksEnter[vehId])  # unsigned int Key, Link,
            VehInput.SetAttValue('Volume(1)', veh_flow_list[vehId])
            VehInput.SetAttValue('VolType(1)', veh_type_list[vehId])
            VehInput.SetAttValue('Vehcomp(1)', vehId + 2)

    def set_name(self):
        LinksName = [self.east_name, self.south_name, self.west_name, self.north_name]
        links = self.vis.Net.Links
        for i in range(4):
            link = links.ItemByKey(i)
            link.Name = LinksName[i]

    def set_speed(self):
        desSpeed = [1] * 4
        speedList = [self.car_speed, self.truck_speed, self.bic_speed, self.ped_speed]
        for i in range(len(desSpeed)):
            speed = speedList[i]
            desSpeed[i] = self.vis.Net.DesSpeedDistributions.AddDesSpeedDistribution(2000 + i, [speed, 0, speed + 1, 1])
        nameList = ['carS', 'truckS', 'bicS', 'pedS']
        for i in range(len(desSpeed)):
            self.vis.Net.DesSpeedDistributions.ItemByKey(2000 + i).SetAttValue('Name', nameList[i])

    def set_veh_cop(self):
        for i in range(4):
            self.vis.Net.VehicleCompositions.AddVehicleComposition(2 + i, [self.vis.Net.VehicleTypes.ItemByKey(100),
                                                                           self.vis.Net.DesSpeedDistributions.ItemByKey(
                                                                               2000),
                                                                           self.vis.Net.VehicleTypes.ItemByKey(200),
                                                                           self.vis.Net.DesSpeedDistributions.ItemByKey(
                                                                               2001)])
        carList = [self.east_car, self.south_car, self.west_car, self.north_car]
        truckList = [self.east_truck, self.south_truck, self.west_truck, self.north_truck]

        for i in range(4):
            self.vis.Net.VehicleCompositions.ItemByKey(2 + i).VehCompRelFlows.GetAll()[0].SetAttValue('RelFlow',
                                                                                                      carList[i])
            self.vis.Net.VehicleCompositions.ItemByKey(2 + i).VehCompRelFlows.GetAll()[0].SetAttValue('RelFlow',
                                                                                                      truckList[i])
        print(1)

    def set_route(self):
        leftList = [self.east_veh_left, self.south_veh_left, self.west_veh_left, self.north_veh_left]
        strList = [self.east_veh_stri, self.south_veh_stri, self.west_veh_stri, self.north_veh_stri]
        rightList = [self.east_veh_right, self.south_veh_right, self.west_veh_right, self.north_veh_right]
        for i in range(4):
            VehRoutDesSta = self.vis.Net.VehicleRoutingDecisionsStatic.AddVehicleRoutingDecisionStatic(i + 1,
                                                                                                       self.linkEnter[
                                                                                                           i], 100)
            leftId = (i + 1) % 4
            strId = (i + 2) % 4
            rightId = (i + 3) % 4
            VehRoutDesSta.VehRoutSta.AddVehicleRouteStatic(1, self.linkExit[leftId], 100)
            VehRoutDesSta.VehRoutSta.AddVehicleRouteStatic(2, self.linkExit[strId], 100)
            VehRoutDesSta.VehRoutSta.AddVehicleRouteStatic(3, self.linkExit[rightId], 100)
            VehRoutDesSta.VehRoutSta.GetAll()[0].SetAttValue('RelFlow(1)', leftList[i])
            VehRoutDesSta.VehRoutSta.GetAll()[1].SetAttValue('RelFlow(1)', strList[i])
            VehRoutDesSta.VehRoutSta.GetAll()[2].SetAttValue('RelFlow(1)', rightList[i])

    def set_signal(self):
        east_left = self.east_left - 5
        west_left = self.west_left - 5
        south_left = self.south_left - 5
        north_left = self.north_left - 5
        east_stri = self.east_stri - 5
        west_stri = self.west_stri - 5
        south_stri = self.south_stri - 5
        north_stri = self.north_stri - 5
        cycleTime = east_stri + west_left + south_stri + north_left + 4 * 5

        SignalController = self.vis.Net.SignalControllers.AddSignalController(1)  # unsigned int Key
        # SignalController.SGs.AddSignalGroup(0)  #
        path = self.path + self.sigfilename
        dom = xml.dom.minidom.parse(path)
        sgList = dom.documentElement.getElementsByTagName('progs')[0].getElementsByTagName('sgs')[
            0].getElementsByTagName('sg')
        dom.documentElement.getElementsByTagName('progs')[0].getElementsByTagName('prog')[0].setAttribute("cycletime",
                                                                                                          str(cycleTime * 1000))
        index = 1
        for sg in sgList:
            if index == 1:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((
                                                                                                                        7 + west_stri) * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        10 + west_stri + east_left) * 1000))
            elif index == 2:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((
                                                                                                                        7 + east_stri) * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        10 + east_stri + west_left) * 1000))
            elif index == 3:
                # sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((17+west_stri+east_left+north_stri)*1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", "0")
                # sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((20+west_stri+east_left+north_stri+south_left)*1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        17 + west_stri + east_left + north_stri) * 1000))
            elif index == 4:
                # sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((17+west_stri+east_left+south_stri)*1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", "0")
                # sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((20+west_stri+east_left+south_stri+north_left)*1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        17 + west_stri + east_left + south_stri) * 1000))
            elif index == 5:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str(2 * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        5 + east_stri) * 1000))
            elif index == 6:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str(2 * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        5 + west_stri) * 1000))
            elif index == 7:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((
                                                                                                                        12 + west_stri + east_left) * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        15 + west_stri + east_left + south_stri) * 1000))
            elif index == 8:
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin", str((
                                                                                                                        12 + west_stri + east_left) * 1000))
                sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin", str((
                                                                                                                        15 + west_stri + east_left + north_stri) * 1000))
            index += 1
        with open(self.path + '123.sig', 'w') as f:
            dom.writexml(f)
        SignalController.SetAttValue('SupplyFile2', path)
        for o in range(1, 9):
            SignalController.SGs.AddSignalGroup(o)  #
        print(1)

    def setHead(self):
        linkEnterList = self.linkEnter
        linkExitList = self.linkExit
        index = 0
        detId = 1
        for linkEnter in linkEnterList:
            lanesNum = linkEnter.Lanes.Count
            leftLane = linkEnter.Lanes.ItemByKey(lanesNum)
            if index == 0:
                signHead = self.vis.Net.SignalHeads.AddSignalHead(0, leftLane, 274)  #
                signHead.SetAttValue('SG', '1-1')
                for j in range(2, lanesNum):
                    strLane = linkEnter.Lanes.ItemByKey(j)
                    signHead2 = self.vis.Net.SignalHeads.AddSignalHead(0, strLane, 274)  #
                    signHead2.SetAttValue('SG', '1-5')
            elif index == 1:
                signHead = self.vis.Net.SignalHeads.AddSignalHead(0, leftLane, 274)  #
                signHead.SetAttValue('SG', '1-3')
                for j in range(2, lanesNum):
                    strLane = linkEnter.Lanes.ItemByKey(j)
                    signHead2 = self.vis.Net.SignalHeads.AddSignalHead(0, strLane, 274)  #
                    signHead2.SetAttValue('SG', '1-7')
            elif index == 2:
                signHead = self.vis.Net.SignalHeads.AddSignalHead(0, leftLane, 274)  #
                signHead.SetAttValue('SG', '1-2')
                for j in range(2, lanesNum):
                    strLane = linkEnter.Lanes.ItemByKey(j)
                    signHead2 = self.vis.Net.SignalHeads.AddSignalHead(0, strLane, 274)  #
                    signHead2.SetAttValue('SG', '1-6')
            elif index == 3:
                signHead = self.vis.Net.SignalHeads.AddSignalHead(0, leftLane, 274)  #
                signHead.SetAttValue('SG', '1-4')
                for j in range(2, lanesNum):
                    strLane = linkEnter.Lanes.ItemByKey(j)
                    signHead2 = self.vis.Net.SignalHeads.AddSignalHead(0, strLane, 274)  #
                    signHead2.SetAttValue('SG', '1-8')
            index += 1
            self.vis.Net.QueueCounters.AddQueueCounter(index, linkEnter, 273)  # unsigned int Key, ILink* Link, double Pos

            for laneId in range(lanesNum):
                detId = index*10+laneId+1
                lane = linkEnter.Lanes.ItemByKey(laneId + 1)
                self.vis.Net.Detectors.AddDetector(detId, lane, 250)  # unsigned int Key, Lane, double Pos
                self.vis.Net.DataCollectionPoints.AddDataCollectionPoint(detId, lane,
                                                                         230)  # unsigned int Key, ILane* Lane, double Pos
                #detId += 1
        for enterindex in range(4):
            for exitindex in range(4):
                if enterindex != exitindex:
                    id = enterindex * 10 + exitindex
                    self.vis.Net.VehicleTravelTimeMeasurements.AddVehicleTravelTimeMeasurement(id, linkEnterList[enterindex], 50,
                                                                                               linkExitList[exitindex],
                                                                                               200)  # u
                    self.vis.Net.DelayMeasurements.AddDelayMeasurement(id)
                    self.vis.Net.DelayMeasurements.ItemByKey(id).SetAttValue('VehTravTmMeas', id)
        print(1)

    def set_parm(self):
        sim_time = int(self.sim_time)
        run_times = int(self.run_freq)
        sim_speed = float(self.sim_speed)
        sim_res = int(self.sim_resol)
        seed_incre = int(self.seed_incre)
        seed = int(self.seed)
        break_time = int(self.stop_time)
        vol_incre = float(self.flow_incre) / 100
        is_max_speed = self.is_max_speed
        if is_max_speed == 'True':
            is_max = 1
        else:
            is_max = 0
        simulation = self.vis.Simulation
        simulation.SetAttValue('SimPeriod', sim_time)
        simulation.SetAttValue('NumRuns', run_times)
        simulation.SetAttValue('SimSpeed', sim_speed)
        simulation.SetAttValue('SimRes', sim_res)
        simulation.SetAttValue('RandSeedIncr', seed_incre)
        simulation.SetAttValue('RandSeed', seed)
        simulation.SetAttValue('SimBreakAt', break_time)
        simulation.SetAttValue('UseMaxSimSpeed', is_max)
        simulation.SetAttValue('VolumeIncrDynAssign', vol_incre)
        print(1)

    def run(self):
        self.vis.Graphics.CurrentNetworkWindow.SetAttValue("QuickMode", 1)  # deactivate QuickMode
        self.vis.Simulation.RunContinuous()

    def runStep(self):
        self.vis.Graphics.CurrentNetworkWindow.SetAttValue("QuickMode", 1)  # deactivate QuickMode
        self.vis.Simulation.RunSingleStep()

    def runStop(self):
        self.vis.Graphics.CurrentNetworkWindow.SetAttValue("QuickMode", 1)  # deactivate QuickMode
        self.vis.Simulation.Stop()
        #time = self.vis.Simulation.SimulationSecond
        # if time % 5 == 0:
        #numVeh = self.vis.Net.Vehicles.Count
    def eval(self):
        delay = round(self.vis.Net.VehicleNetworkPerformanceMeasurement.AttValue('DelayAvg(AVG,1,All)'),2)
        # stop=self.vis.Net.VehicleNetworkPerformanceMeasurement.AttValue('DelayStopAvg')
        speed = round(self.vis.Net.VehicleNetworkPerformanceMeasurement.AttValue('SpeedAvg(AVG,1,All)'),2)
        stop = round(self.vis.Net.VehicleNetworkPerformanceMeasurement.AttValue('StopsAvg(AVG,1,All)'),2)
        try:
            vehNum = round(self.vis.Net.VehicleNetworkPerformanceMeasurement.AttValue('VehArr(AVG,1,All)'),2)
        except:
            vehNum = 0
        travelTimeDist = {}
        travelNumDist = {}
        delayDist = {}
        stopDist = {}
        for i in range(4):
            for j in range(4):
                if i!=j:
                    id = i * 10 + j
                    tavelTime = self.vis.Net.VehicleTravelTimeMeasurements.ItemByKey(id).AttValue('TravTm(AVG,1,All)')
                    vehNum = self.vis.Net.VehicleTravelTimeMeasurements.ItemByKey(id).AttValue('Vehs  (Avg,1,All)')
                    vehdelay = self.vis.Net.DelayMeasurements.ItemByKey(id).AttValue('VehDelay (Avg,1,All)')
                    vehstop = self.vis.Net.DelayMeasurements.ItemByKey(id).AttValue('Stops (Avg,1,All)')
                    travelTimeDist[id] = round(tavelTime,2)
                    travelNumDist[id] = round(vehNum,2)
                    delayDist[id] = round(vehdelay,2)
                    stopDist[id]= round(vehstop,2)
        linkqueueDist = {}
        linkqueueDistMax = {}
        linkstopDist = {}
        for i in range(4):
            queueId = i+1
            queueLengthMAx =self.vis.Net.QueueCounters.ItemByKey(queueId).AttValue('QLenMax(Avg, Avg)')
            queueLength =self.vis.Net.QueueCounters.ItemByKey(queueId).AttValue('QLen(Avg, Avg)')
            queueStop =self.vis.Net.QueueCounters.ItemByKey(queueId).AttValue('QStops(Avg, Avg)')
            linkqueueDist[queueId] = round(queueLength,2)
            linkqueueDistMax[queueId] = round(queueLengthMAx,2)
            linkstopDist[queueId] = round(queueStop,2)
        return travelTimeDist,travelNumDist,delayDist,stopDist,linkqueueDist,linkqueueDistMax,delay,speed,stop,vehNum

        #while time <3599:
    def run_main(self):
        try:
            t1 =threading.Thread(target=self.run(), args=())
            t1.start()
        except:
            print("Error: 无法启动线程")

def pingfen(delay):
    level = -1
    if delay <=70:
        level = 130-max(delay,30)
    return level

def main(data):
    crossId = data['crossId']
    entro_data = data_select._select_cross_entro_info(crossId)
    veh_flow_data = data_select._select_cross_veh_flow_info(crossId)
    ped_flow_data = data_select._select_cross_ped_flow_info(crossId)
    bic_flow_data = data_select._select_cross_bicycle_flow_info(crossId)
    veh_ratio_data = data_select._select_cross_veh_ratio_info(crossId)
    veh_route_data = data_select._select_cross_veh_route_info(crossId)
    bic_route_data = data_select._select_cross_bicycle_route_info(crossId)
    ped_route_data = data_select._select_cross_ped_route_info(crossId)
    can_data = data_select._select_cross_canalization_info(crossId)
    speed_data = data_select._select_cross_speed_info(crossId)
    sign_data = data_select._select_cross_signal_info(crossId)
    global myVis
    myVis = myVissim(data, entro_data, veh_flow_data, ped_flow_data, bic_flow_data, veh_ratio_data, veh_route_data,
                     bic_route_data, ped_route_data, can_data, speed_data, sign_data)
    myVis.set_speed()
    myVis.set_veh_cop()
    myVis.set_can()
    myVis.set_route()
    myVis.set_signal()
    myVis.setHead()
    myVis.set_parm()
    myVis.run()
    travelTimeDist, travelNumDist, delayDist, stopDist, linkqueueDist, linkqueueDistMax, delay, speed, stop, vehNum = myVis.eval()
    level = pingfen(delay)
    returnData = {'travelTime':travelTimeDist,'travelNum':travelNumDist,'delay':delayDist,'queue':linkqueueDist,
                  'queueMax':linkqueueDistMax,'netDelay':delay,'netSpeed':speed,'netStop':stop, 'vehNum':vehNum ,'level':level}
    return returnData

def visIntial(data):
    crossId = data['crossId']
    entro_data = data_select._select_cross_entro_info(crossId)
    veh_flow_data = data_select._select_cross_veh_flow_info(crossId)
    ped_flow_data = data_select._select_cross_ped_flow_info(crossId)
    bic_flow_data = data_select._select_cross_bicycle_flow_info(crossId)
    veh_ratio_data = data_select._select_cross_veh_ratio_info(crossId)
    veh_route_data = data_select._select_cross_veh_route_info(crossId)
    bic_route_data = data_select._select_cross_bicycle_route_info(crossId)
    ped_route_data = data_select._select_cross_ped_route_info(crossId)
    can_data = data_select._select_cross_canalization_info(crossId)
    speed_data = data_select._select_cross_speed_info(crossId)
    sign_data = data_select._select_cross_signal_info(crossId)
    global myVis
    myVis = myVissim(data, entro_data, veh_flow_data, ped_flow_data, bic_flow_data, veh_ratio_data, veh_route_data,
                     bic_route_data, ped_route_data, can_data, speed_data, sign_data)

def run_cont():
    global myVis
    myVis.run()

def run_step():
    global myVis
    myVis.runStep()

def run_stop():
    global myVis
    myVis.runStop()

def zhibiao():
    global myVis
    travelTimeDist, travelNumDist, delayDist, stopDist, linkqueueDist, linkqueueDistMax, delay, speed, stop, vehNum = myVis.eval()
    returnData = {'travelTime': travelTimeDist, 'travelNum': travelNumDist, 'delay': delayDist, 'queue': linkqueueDist,
                  'queueMax': linkqueueDistMax, 'netDelay': delay, 'netSpeed': speed, 'netStop': stop ,'netNum':vehNum}
    return returnData





def main_test():
    data = {"crossId": "8000", "fzt": "3600", "rt": "1", "rs": "10", "fzjd": "2",
            "sjzzzl": "1", "sjzz": "42", "zdt": "3600", "selname": "5", "llzl": "10", "zuida": "True"}
    crossId = data['crossId']
    entro_data = {'crossid': 8000, 'crossname': 'junGong', 'eastname': 'JunGongWest',
                  'westname': 'JunGongEast', 'southname': 'JunGongSouth', 'northname': 'JunGongNorth'}
    veh_flow_data = {'crossid': 8000, 'EastVeh': 400, 'SouthVeh': 500, 'WestVeh': 600, 'NorthVeh': 500,
                     'EastFlowType': 1, 'SouthFlowType': 1, 'WestFlowType': 1, 'NorthFlowType': 1}
    ped_flow_data = {'crossid': 8000, 'EastPed': 100, 'SouthPed': 210, 'WestPed': 110, 'NorthPed': 90}
    bic_flow_data = {'crossid': 8000, 'EastBic': 120, 'SouthBic': 200, 'WestBic': 180, 'NorthBic': 210}
    veh_ratio_data = {'crossid': 8000, 'EastCar': 90, 'SouthCar': 95, 'WestCar': 85, 'NorthCar': 88, 'EastTruck': 10,
                      'SouthTruck': 5, 'WestTruck': 15, 'NorthTruck': 12}
    veh_route_data = {'crossid': 8000, 'Eastleft': 5, 'EastStraight': 2, 'EastRight': 1,
                      'Southleft': 1, 'SouthStraight': 3, 'SouthRight': 1, 'Westleft': 2,
                      'WestStraight': 3, 'WestRight': 1, 'Northleft': 1, 'NorthStraight': 1, 'NorthRight': 1}
    bic_route_data = {'crossid': 8000, 'BicEastleft': 1, 'BicEastStraight': 2, 'BicEastRight': 1, 'BicSouthleft': 2,
                      'BicSouthStraight': 1,
                      'BicSouthRight': 1, 'BicWestleft': 1, 'BicWestStraight': 2, 'BicWestRight': 2, 'BicNorthleft': 1,
                      'BicNorthStraight': 1, 'BicNorthRight': 1}
    ped_route_data = {'crossid': 8000, 'EastCW': 1, 'EastAnti': 1, 'SouthCW': 1, 'SouthAnti': 2,
                      'WestCW': 2, 'WestAnti': 1, 'NorthCW': 2, 'NorthAnti': 3}
    can_data = {'crossid': 8000, 'EastEntNum': 4, 'SouthEntNum': 4, 'WestEntNum': 4,
                'NorthEntNum': 4, 'EastExNum': 3, 'SouthExNum': 4, 'WestExNum': 3,
                'NorthExNum': 4, 'EastWidth': 3, 'SouthWidth': 3, 'WestWidth': 3, 'NorthWidth': 3}
    speed_data = {'crossid': 8000, 'carSpeed': 40.0, 'truckSpeed': 30.0, 'bicycleSpeed': 25.0, 'pedSpeed': 3.6}
    sign_data = {'crossid': 8000, 'cycletime': 200, 'EastLeft': 115, 'EastStraight': 27, 'SouthLeft': 31,
                 'SouthStraight': 33,
                 'WestLeft': 127, 'WestStraight': 39, 'NorthLeft': 13, 'NorthStraight': 15}
    # vissim_obj = open(entro_data, can_data)
    myVis = myVissim(data, entro_data, veh_flow_data, ped_flow_data, bic_flow_data, veh_ratio_data, veh_route_data,
                     bic_route_data, ped_route_data, can_data, speed_data, sign_data)
    myVis.set_speed()
    myVis.set_veh_cop()
    myVis.set_can()
    myVis.set_route()
    myVis.set_signal()
    myVis.setHead()
    myVis.set_parm()
    myVis.run()
    travelTimeDist, travelNumDist, delayDist, stopDist, linkqueueDist, linkqueueDistMax,delay,speed,stop,vehNum = myVis.eval()
    level = pingfen(delay)
    returnData = {'travelTime':travelTimeDist,'travelNum':travelNumDist,'delay':delayDist,'queue':linkqueueDist,
                  'queueMax':linkqueueDistMax,'netDelay':delay,'netSpeed':speed,'netStop':stop, 'vehNum':vehNum ,'level':level}
    return returnData
    # myVis.set_route()


if __name__ == '__main__':
    main_test()
