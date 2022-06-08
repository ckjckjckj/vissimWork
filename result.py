#!/user/env python
# _*_ coding:utf-8 _*_
import data_select

def main(data):
    crossId = data['crossId']
    veh_flow_data = data_select._select_cross_veh_flow_info(crossId)
    can_data = data_select._select_cross_canalization_info(crossId)
    east_ent_num = can_data['EastEntNum']
    west_ent_num = can_data['WestEntNum']
    south_ent_num = can_data['SouthEntNum']
    north_ent_num = can_data['NorthEntNum']
    veh_flow = veh_flow_data['EastVeh']
    rows = data_select.load_vis_result(east_ent_num,west_ent_num,south_ent_num,north_ent_num,veh_flow)
    if len(rows)>0:
        (videoIndex, netDelay, netStop, netCar, netSpeed, eastQueue, westQueue, southQueue, northQueue,
         northQueueMax, westQueueMax, eastQueueMax, southQueueMax, eastTimeLeft, westTimeLeft, northTimeLeft, southTimeLeft,
    eastTimeStr, westTimeStr, northTimeStr, southTimeStr, eastTimeRight,
    westTimeRight, northTimeRight, southTimeRight, eastDelayLeft, eastDelayStr,
    eastDelayRight, westDelayLeft, westDelayStr, northDelayStr, northDelayLeft,
    westDelayRight, northDelayRight, southDelayLeft, southDelayStr, southDelayRight, point) = rows[0]
    vissimResult = {}
    vissimResult['videoIndex']=videoIndex
    vissimResult['netDelay']=netDelay
    vissimResult['netStop']=netStop
    vissimResult['netCar']=netCar
    vissimResult['netSpeed']=netSpeed
    queueDict = {}
    queueDict['1'] = eastQueue
    queueDict['2'] = southQueue
    queueDict['3'] = westQueue
    queueDict['4'] = northQueue
    vissimResult['queue']=queueDict

    queueMaxDict = {}
    queueMaxDict['1'] = eastQueueMax
    queueMaxDict['2'] = southQueueMax
    queueMaxDict['3'] = westQueueMax
    queueMaxDict['4'] = northQueueMax
    vissimResult['queueMax'] = queueMaxDict

    travelTimeDict = {}
    travelTimeDict['1'] = eastTimeLeft
    travelTimeDict['2'] = eastTimeStr
    travelTimeDict['3'] = eastTimeRight
    travelTimeDict['12'] = southTimeLeft
    travelTimeDict['13'] = southTimeStr
    travelTimeDict['10'] = southTimeRight
    travelTimeDict['23'] = westTimeLeft
    travelTimeDict['20'] = westTimeStr
    travelTimeDict['21'] = westTimeRight
    travelTimeDict['30'] = northTimeLeft
    travelTimeDict['31'] = northTimeStr
    travelTimeDict['32'] = northTimeRight
    vissimResult['travelTime'] = travelTimeDict

    delayDict = {}
    delayDict['1'] = eastDelayLeft
    delayDict['2'] = eastDelayStr
    delayDict['3'] = eastDelayRight
    delayDict['12'] = southDelayLeft
    delayDict['13'] = southDelayStr
    delayDict['10'] = southDelayRight
    delayDict['23'] = westDelayLeft
    delayDict['20'] = westDelayStr
    delayDict['21'] = westDelayRight
    delayDict['30'] = northDelayLeft
    delayDict['31'] = northDelayStr
    delayDict['32'] = northDelayRight
    vissimResult['delay'] = delayDict

    vissimResult['level']=point
    return vissimResult