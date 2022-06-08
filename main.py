#!/user/env python
# _*_ coding:utf-8 _*_
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import sim2
import data_select
import signalOptim
import result

app = Flask(__name__)
app.debug = True
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False

from flask_cors import cross_origin


@app.route('/sendAjax2', methods=['GET', 'POST'])
@cross_origin()
def sendAjax2():
    # password = request.form.get('password')
    # username = request.args.get('username')

    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    print(username)
    print(password)

    return jsonify({'tasks': "来自flask的信息"})


@app.route('/cal', methods=['GET', 'POST'])
def cal():
    print(1)
    rowData = request.data
    data = json.loads(rowData)
    a = data['a']
    b = data['b']
    newdata = {}
    newdata['ans'] = a + b
    name = data_select._select_cross_name(2)
    return jsonify(name)


@app.route('/login', methods=['POST'])
def login():
    print(2)
    newdata = [
        {
            'name': '晴天',
            'id': '1'
        },
        {
            'name': '安静',
            'id': '2'
        },
        {
            'name': '七里香',
            'id': '3'
        }
    ]
    # sim2.main()
    id = data_select._select_crossId()
    data = []
    i = 0
    for idValue in id:
        dataValue = {}
        dataValue['name'] = idValue[0]
        dataValue['id'] = i
        i += 1
        data.append(dataValue)
    return jsonify(data)


@app.route('/crossInfo', methods=['POST'])
def crossInfo():
    rowData = request.data
    data = json.loads(rowData)
    name = data_select._select_cross_name(data)
    return jsonify(name)


@app.route('/allcrossInfo', methods=['GET', 'POST'])
def allcrossInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    newdata = data_select._select_all_cross_entro_info()
    return jsonify(newdata)


@app.route('/crossBaseInfo', methods=['POST'])
def crossBaseInfo():
    rowData = request.data
    data = json.loads(rowData)
    basedata = data_select._select_cross_entro_info(data)
    return jsonify(basedata)


@app.route('/insecrossBaseInfo', methods=['POST'])
def insecrossBaseInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    crossname = data["crossname"]
    eastname = data["eastname"]
    westname = data["westname"]
    southname = data["southname"]
    northname = data["northname"]
    flag = data_select._insert_cross_entro_info(crossId, crossname, eastname, westname, southname, northname)
    return jsonify(flag)


@app.route('/updateCrossBaseInfo', methods=['POST'])
def updateCrossBaseInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    crossname = data["crossname"]
    eastname = data["eastname"]
    westname = data["westname"]
    southname = data["southname"]
    northname = data["northname"]
    flag = data_select._update_cross_entro_info(crossId, crossname, eastname, westname, southname, northname)
    return jsonify(flag)


@app.route('/deleteCrossBaseInfo', methods=['POST'])
def deleteCrossBaseInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_entro_info(crossId)
    return jsonify(flag)


@app.route('/crossCanalizationInfo', methods=['POST'])
def crossCanalizationInfo():
    rowData = request.data
    data = json.loads(rowData)
    basedata = data_select._select_cross_canalization_info(data)
    return jsonify(basedata)


@app.route('/allcrossCanalizationInfo', methods=['GET', 'POST'])
def allcrossCanalizationInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    basedata = data_select._select_all_cross_canalization_info()
    return jsonify(basedata)


@app.route('/insecrossCanalizationInfo', methods=['POST'])
def insecrossCanalizationInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    EastEntNum = data['jkcdd']
    SouthEntNum = data['jkcdn']
    WestEntNum = data['jkcdx']
    NorthEntNum = data['jkcdb']
    EastExNum = data['ckcdd']
    SouthExNum = data['ckcdn']
    WestExNum = data['ckcdx']
    NorthExNum = data['ckcdb']
    EastWidth = data['cdkdd']
    SouthWidth = data['cdkdn']
    WestWidth = data['cdkdx']
    NorthWidth = data['cdkdb']
    flag = data_select._insert_cross_canalization_info(crossId, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
                                                       EastExNum, SouthExNum, WestExNum, NorthExNum,
                                                       EastWidth, SouthWidth, WestWidth, NorthWidth)
    return jsonify(flag)


@app.route('/updatecrossCanalizationInfo', methods=['POST'])
def updatecrossCanalizationInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    EastEntNum = data['jkcdd']
    SouthEntNum = data['jkcdn']
    WestEntNum = data['jkcdx']
    NorthEntNum = data['jkcdb']
    EastExNum = data['ckcdd']
    SouthExNum = data['ckcdn']
    WestExNum = data['ckcdx']
    NorthExNum = data['ckcdb']
    EastWidth = data['cdkdd']
    SouthWidth = data['cdkdn']
    WestWidth = data['cdkdx']
    NorthWidth = data['cdkdb']
    flag = data_select._update_cross_canalization_info(crossId, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
                                                       EastExNum, SouthExNum, WestExNum, NorthExNum,
                                                       EastWidth, SouthWidth, WestWidth, NorthWidth)
    return jsonify(flag)


@app.route('/deletecrossCanalizationInfo', methods=['POST'])
def deletecrossCanalizationInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_canalization_info(crossId)
    return jsonify(flag)


@app.route('/allcrossFlowInfo', methods=['GET', 'POST'])
def allcrossFlowInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    basedata = data_select._select_all_cross_veh_flow_info()
    return jsonify(basedata)


@app.route('/crossFlowInfo', methods=['POST'])
def crossFlowInfo():
    rowData = request.data
    data = json.loads(rowData)
    vehFlow = data_select._select_cross_veh_flow_info(data)
    vehRatio = data_select._select_cross_veh_ratio_info(data)
    bicFlow = data_select._select_cross_bicycle_flow_info(data)
    pedFlow = data_select._select_cross_ped_flow_info(data)
    basedata = {**vehFlow, **vehRatio, **bicFlow, **pedFlow}
    return jsonify(basedata)


@app.route('/insecrossFlowInfo', methods=['POST'])
def insecrossFlowInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    EastVeh = data['jdd']
    EastBic = data['fjdd']
    EastPed = data['xrd']
    EastType = data['lxd']
    EastCar = data['xcd']
    EastTruck = data['dcd']
    SouthVeh = data['jdn']
    SouthBic = data['fjdn']
    SouthPed = data['xrn']
    SouthType = data['lxn']
    SouthCar = data['xcn']
    SouthTruck = data['dcn']
    WestVeh = data['jdx']
    WestBic = data['fjdx']
    WestPed = data['xrx']
    WestType = data['lxx']
    WestCar = data['xcx']
    WestTruck = data['dcx']
    NorthVeh = data['jdb']
    NorthBic = data['fjdb']
    NorthPed = data['xrb']
    NorthType = data['lxb']
    NorthCar = data['xcb']
    NorthTruck = data['dcb']
    flag = data_select._insert_cross_veh_flow_info(crossId, EastVeh, SouthVeh, WestVeh, NorthVeh, EastType, SouthType,
                                                   WestType, NorthType)
    flag2 = data_select._insert_cross_veh_ratio_info(crossId, EastCar, EastTruck, SouthCar, SouthTruck, WestCar,
                                                     WestTruck, NorthCar, NorthTruck)
    flag3 = data_select._insert_cross_bicycle_flow_info(crossId, EastBic, SouthBic, WestBic, NorthBic)
    flag4 = data_select._insert_cross_ped_flow_info(crossId, EastPed, SouthPed, WestPed, NorthPed)
    return jsonify(flag + '\r' + flag2 + '\r' + flag3 + '\r' + flag4)


@app.route('/updatecrossFlowInfo', methods=['POST'])
def updatecrossFlowInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    EastVeh = data['jdd']
    EastBic = data['fjdd']
    EastPed = data['xrd']
    EastType = data['lxd']
    EastCar = data['xcd']
    EastTruck = data['dcd']
    SouthVeh = data['jdn']
    SouthBic = data['fjdn']
    SouthPed = data['xrn']
    SouthType = data['lxn']
    SouthCar = data['xcn']
    SouthTruck = data['dcn']
    WestVeh = data['jdx']
    WestBic = data['fjdx']
    WestPed = data['xrx']
    WestType = data['lxx']
    WestCar = data['xcx']
    WestTruck = data['dcx']
    NorthVeh = data['jdb']
    NorthBic = data['fjdb']
    NorthPed = data['xrb']
    NorthType = data['lxb']
    NorthCar = data['xcb']
    NorthTruck = data['dcb']
    flag = data_select._update_cross_veh_flow_info(crossId, EastVeh, SouthVeh, WestVeh, NorthVeh, EastType, SouthType,
                                                   WestType, NorthType)
    flag2 = data_select._update_cross_veh_ratio_info(crossId, EastCar, EastTruck, SouthCar, SouthTruck, WestCar,
                                                     WestTruck, NorthCar, NorthTruck)
    flag3 = data_select._update_cross_bicycle_flow_info(crossId, EastBic, SouthBic, WestBic, NorthBic)
    flag4 = data_select._update_cross_ped_flow_info(crossId, EastPed, SouthPed, WestPed, NorthPed)
    return jsonify(flag + '\r' + flag2 + '\r' + flag3 + '\r' + flag4)


@app.route('/deletecrossFlowInfo', methods=['POST'])
def deletecrossFlowInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_veh_flow_info(crossId)
    flag2 = data_select._delete_cross_veh_ratio_info(crossId)
    flag3 = data_select._delete_cross_bicycle_flow_info(crossId)
    flag4 = data_select._delete_cross_ped_flow_info(crossId)
    return jsonify(flag + '\r' + flag2 + '\r' + flag3 + '\r' + flag4)


@app.route('/allcrossSpeedInfo', methods=['GET', 'POST'])
def allcrossSpeedInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    basedata = data_select._select_all_cross_speed_info()
    return jsonify(basedata)


@app.route('/crossSpeedInfo', methods=['POST'])
def crossSpeedInfo():
    rowData = request.data
    data = json.loads(rowData)
    vehFlow = data_select._select_cross_speed_info(data)
    basedata = vehFlow
    return jsonify(basedata)


@app.route('/insecrossSpeedInfo', methods=['POST'])
def insecrossSpeedInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    truckSpeed = data['sdc']
    carSpeed = data['sxc']
    bicycleSpeed = data['sfjd']
    pedSpeed = data['sxr']
    flag = data_select._insert_cross_speed_info(crossId, carSpeed, truckSpeed, bicycleSpeed, pedSpeed)
    return jsonify(flag)


@app.route('/updatecrossSpeedInfo', methods=['POST'])
def updatecrossSpeedInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    truckSpeed = data['sdc']
    carSpeed = data['sxc']
    bicycleSpeed = data['sfjd']
    pedSpeed = data['sxr']
    flag = data_select._update_cross_speed_info(crossId, carSpeed, truckSpeed, bicycleSpeed, pedSpeed)
    return jsonify(flag)


@app.route('/deletecrossSpeedInfo', methods=['POST'])
def deletecrossSpeedInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_speed_info(crossId)
    return jsonify(flag)


@app.route('/allcrossRouteInfo', methods=['GET', 'POST'])
def allcrossRouteInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    basedata = data_select._select_all_cross_route_info()
    return jsonify(basedata)


@app.route('/crossRouteInfo', methods=['POST'])
def crossRouteInfo():
    rowData = request.data
    data = json.loads(rowData)
    vehRoute = data_select._select_cross_veh_route_info(data)
    bicycleRoute = data_select._select_cross_bicycle_route_info(data)
    pedRoute = data_select._select_cross_ped_route_info(data)

    basedata = {**vehRoute, **bicycleRoute, **pedRoute}
    return jsonify(basedata)


@app.route('/insecrossRouteInfo', methods=['POST'])
def insecrossRouteInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    carDl = data['jld']
    carDs = data['jsd']
    carDr = data['jrd']
    carNl = data['jln']
    carNs = data['jsn']
    carNr = data['jrn']
    carXl = data['jlx']
    carXs = data['jsx']
    carXr = data['jrx']
    carBl = data['jlb']
    carBs = data['jsb']
    carBr = data['jrb']
    bicDl = data['fld']
    bicDs = data['fsd']
    bicDr = data['frd']
    bicNl = data['fln']
    bicNs = data['fsn']
    bicNr = data['frn']
    bicXl = data['flx']
    bicXs = data['fsx']
    bicXr = data['frx']
    bicBl = data['flb']
    bicBs = data['fsb']
    bicBr = data['frb']
    pedDl = data['xld']
    pedDs = data['xsd']
    pedNl = data['xln']
    pedNs = data['xsn']
    pedXl = data['xlx']
    pedXs = data['xsx']
    pedBl = data['xlb']
    pedBs = data['xsb']

    flag = data_select._insert_cross_veh_route_info(crossId, carDl, carDs, carDr, carNl, carNs, carNr, carXl, carXs,
                                                    carXr, carBl, carBs, carBr)
    flag1 = data_select._insert_cross_bicycle_route_info(crossId, bicDl, bicDs, bicDr, bicNl, bicNs, bicNr, bicXl,
                                                         bicXs, bicXr, bicBl, bicBs, bicBr)
    flag2 = data_select._insert_cross_ped_route_info(crossId, pedDl, pedDs, pedNl, pedNs, pedXl, pedXs, pedBl, pedBs)

    return jsonify(flag + '\r' + flag1 + '\r' + flag2)


@app.route('/updatecrossRouteInfo', methods=['POST'])
def updatecrossRouteInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    carDl = data['jld']
    carDs = data['jsd']
    carDr = data['jrd']
    carNl = data['jln']
    carNs = data['jsn']
    carNr = data['jrn']
    carXl = data['jlx']
    carXs = data['jsx']
    carXr = data['jrx']
    carBl = data['jlb']
    carBs = data['jsb']
    carBr = data['jrb']
    bicDl = data['fld']
    bicDs = data['fsd']
    bicDr = data['frd']
    bicNl = data['fln']
    bicNs = data['fsn']
    bicNr = data['frn']
    bicXl = data['flx']
    bicXs = data['fsx']
    bicXr = data['frx']
    bicBl = data['flb']
    bicBs = data['fsb']
    bicBr = data['frb']
    pedDl = data['xld']
    pedDs = data['xsd']
    pedNl = data['xln']
    pedNs = data['xsn']
    pedXl = data['xlx']
    pedXs = data['xsx']
    pedBl = data['xlb']
    pedBs = data['xsb']

    flag = data_select._update_cross_veh_route_info(crossId, carDl, carDs, carDr, carNl, carNs, carNr, carXl, carXs,
                                                    carXr, carBl, carBs, carBr)
    flag1 = data_select._update_cross_bicycle_route_info(crossId, bicDl, bicDs, bicDr, bicNl, bicNs, bicNr, bicXl,
                                                         bicXs, bicXr, bicBl, bicBs, bicBr)
    flag2 = data_select._update_cross_ped_route_info(crossId, pedDl, pedDs, pedNl, pedNs, pedXl, pedXs, pedBl, pedBs)

    return jsonify(flag + '\r' + flag1 + '\r' + flag2)


@app.route('/deletecrossRouteInfo', methods=['POST'])
def deletecrossRouteInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_veh_route_info(crossId)
    flag1 = data_select._delete_cross_bicycle_route_info(crossId)
    flag2 = data_select._delete_cross_ped_route_info(crossId)
    return jsonify(flag + '\r' + flag1 + '\r' + flag2)


@app.route('/allcrossSignalInfo', methods=['GET', 'POST'])
def allcrossSignalInfo():
    # rowData = request.data
    # data = json.loads(rowData)
    basedata = data_select._select_all_cross_signal_info()
    return jsonify(basedata)


@app.route('/crossSignalInfo', methods=['POST'])
def crossSignalInfo():
    rowData = request.data
    data = json.loads(rowData)
    vehFlow = data_select._select_cross_signal_info(data)
    basedata = vehFlow
    return jsonify(basedata)


@app.route('/insecrossSignalInfo', methods=['POST'])
def insecrossSignalInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    cycletime = data['zq']
    EastLeft = data['dl']
    EastStraight = data['ds']
    SouthLeft = data['nl']
    SouthStraight = data['ns']
    WestLeft = data['xl']
    WestStraight = data['xs']
    NorthLeft = data['bl']
    NorthStraight = data['bs']

    flag = data_select._insert_cross_signal_info(crossId, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight,
                                                 WestLeft,
                                                 WestStraight, NorthLeft, NorthStraight)
    return jsonify(flag)


@app.route('/updatecrossSignalInfo', methods=['POST'])
def updatecrossSignalInfo():
    rowData = request.data
    data = json.loads(rowData)
    crossId = data["crossId"]
    cycletime = data['zq']
    EastLeft = data['dl']
    EastStraight = data['ds']
    SouthLeft = data['nl']
    SouthStraight = data['ns']
    WestLeft = data['xl']
    WestStraight = data['xs']
    NorthLeft = data['bl']
    NorthStraight = data['bs']
    flag = data_select._update_cross_signal_info(crossId, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight,
                                                 WestLeft,
                                                 WestStraight, NorthLeft, NorthStraight)
    return jsonify(flag)


@app.route('/deletecrossSignalInfo', methods=['POST'])
def deletecrossSignalInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    flag = data_select._delete_cross_signal_info(crossId)
    return jsonify(flag)


@app.route('/optimSignalInfo', methods=['POST'])
def optimSignalInfo():
    rowData = request.data
    crossId = json.loads(rowData)
    [GNs, GSl, GSs, GNl, GWs, GEl, GEs, GWl] = signalOptim.main(crossId)
    cycletime = GEs + GWl + GSs + GNl
    returndata = {'gns': GNs, 'gsl': GSl, 'gss': GSs, 'gnl': GNl, 'gws': GWs, 'gel': GEl, 'ges': GEs, 'gwl': GWl,
                  'cycle': cycletime}
    return jsonify(returndata)


@app.route('/parm', methods=['POST'])
def parm():
    rowData = request.data
    crossId = json.loads(rowData)
    data = data_select._select_default_parm()
    return jsonify(data)


@app.route('/openvissim', methods=['POST'])
def openvissim():
    rowData = request.data
    data = json.loads(rowData)
    returndata = sim2.main(data)

    return jsonify(returndata)

@app.route('/loadZhibiao', methods=['POST'])
def loadZhibiao():
    returnData = data_select.load_data()
    return jsonify(returnData)

@app.route('/openvissim2', methods=['POST'])
def openvissim2():
    rowData = request.data
    data = json.loads(rowData)
    returndata = sim2.main(data)
    return jsonify(returndata)

@app.route('/InitVisim', methods=['POST'])
def InitVisim():
    rowData = request.data
    data = json.loads(rowData)
    sim2.visIntial(data)
    return jsonify(1)

@app.route('/singStepVisim', methods=['POST'])
def singStepVisim():
    sim2.run_step()
    return jsonify(1)

@app.route('/stopStepVisim', methods=['POST'])
def stopStepVisim():
    sim2.runStop()
    return jsonify(1)

@app.route('/visResult', methods=['POST'])
def visResult():
    rowData = request.data
    data = json.loads(rowData)
    vissimResult = result.main(data)
    return jsonify(vissimResult)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
