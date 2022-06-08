#!/user/env python
# _*_ coding:utf-8 _*_
import data_select


def webster(y):
    left = max(y[1] + y[4], y[5] + y[0])
    right = max(y[3] + y[6], y[7] + y[2])
    Y = left + right
    if Y <= 0.9:
        T = max(min((1.5 * 12 + 5) / (1 - Y), 200),80)
    else:
        T= 200
    y_left = left / (left + right)
    y_right = right / (left + right)
    yNs = y_left * (y[1] / (y[0] + y[4]))
    ySl = y_left * (y[4] / (y[0] + y[4]))
    ySs = y_left * (y[5] / (y[5] + y[0]))
    yNl = y_left * (y[0] / (y[5] + y[0]))

    yWs = y_right * (y[3] / (y[3] + y[6]))
    yEl = y_right * (y[6] / (y[3] + y[6]))
    yEs = y_right * (y[7] / (y[2] + y[7]))
    yWl = y_right * (y[2] / (y[2] + y[7]))

    GNs = round((T - 20) * yNs) +5
    GSl = round((T - 20) * ySl) +5
    GSs = round((T - 20) * ySs) +5
    GNl = GNs + GSl - GSs
    #GNl = round((T - 20) * yNl) +5
    GWs = round((T - 20) * yWs) +5
    #GEl = (T - 20) * yEl
    GEl = T - GNs - GSl - GWs
    GEs = round((T - 20) * yEs)
    GWl = T - GSs - GNl - GEs
    #GWl = (T - 20) * yWl
    return [GNs, GSl, GSs, GNl, GWs, GEl, GEs, GWl]


def webMain(QNl, QNs, QWl, QWs, QSl, QSs, QEl, QEs, laneN, laneW, laneS, laneE):
    Q = [QNl, QNs, QWl, QWs, QSl, QSs, QEl, QEs]
    laneNl = 1
    laneWl = 1
    laneSl = 1
    laneEl = 1
    laneNs = laneN - laneNl -1
    laneWs = laneW - laneWl -1
    laneSs = laneS - laneSl -1
    laneEs = laneE - laneEl -1
    S = [1200* laneNl,1500*laneNs,1200* laneWl,1500*laneWs,1200* laneSl,1500*laneSs,1200* laneEl,1500*laneEs]
    y = [Q[i]/S[i] for i in range(len(Q))]
    signal = webster(y)
    return signal

def Get_lane_num(cross_id):
    data = data_select._select_cross_canalization_info(cross_id)
    laneN = data['NorthEntNum']
    laneW = data['WestEntNum']
    laneS = data['SouthEntNum']
    laneE = data['EastEntNum']
    return (laneN, laneW, laneS, laneE)

def get_flow(cross_id):
    flowdata = data_select._select_cross_veh_flow_info(cross_id)
    routedata = data_select._select_cross_veh_route_info(cross_id)
    flowN = flowdata['NorthVeh']
    flowW = flowdata['WestVeh']
    flowS = flowdata['SouthVeh']
    flowE = flowdata['EastVeh']
    leftN = routedata['Northleft']
    straightN = routedata['NorthStraight']
    leftW = routedata['Westleft']
    straightW = routedata['WestStraight']
    leftS = routedata['Southleft']
    straightS = routedata['SouthStraight']
    leftE = routedata['Eastleft']
    straightE = routedata['EastStraight']
    QNl = flowN * leftN
    QWl = flowW * leftW
    QSl = flowS * leftS
    QEl = flowE * leftE
    QNs = flowN * straightN
    QWs = flowW * straightW
    QSs = flowS * straightS
    QEs = flowE * straightE
    return (QNl, QNs, QWl, QWs, QSl, QSs, QEl, QEs)

def main(cross_id):
    (laneN, laneW, laneS, laneE) = Get_lane_num(cross_id)
    (QNl, QNs, QWl, QWs, QSl, QSs, QEl, QEs) = get_flow(cross_id)
    signal = webMain(QNl, QNs, QWl, QWs, QSl, QSs, QEl, QEs, laneN, laneW, laneS, laneE)
    #[GNs, GSl, GSs, GNl, GWs, GEl, GEs, GWl] = signal
    return signal




if __name__ == '__main__':
    signal = main(8000)
    print(1)
   # print(webMain(200,500,300,600,230,400,450,400,3,3,3,3))