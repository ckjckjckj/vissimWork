#!/user/env python
# _*_ coding:utf-8 _*_
import pymysql


class mysql(object):
    a = 0

    def __init__(self):
        try:
            host = 'localhost'
            port = 3305
            user = 'root'
            password = 'root'
            database = 'visplant'
            self._conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
            self.cursor = self._conn.cursor()
            self.a = '修改成功'
        except:
            self.a = '输入错误'

    def printa(self):
        print(self.a)


def _select_crossId():
    """
    所有路口编号集合
    :return:
    """
    sql = """select crossid from basedata"""
    Mysql = mysql()
    Mysql.cursor.execute(sql)
    rows = Mysql.cursor.fetchall()
    crossIdList = []
    for row in rows:
        crossIdList.append(row)
    return crossIdList


def _select_cross_name(cross_id):
    """
    根据路口号查找路口名称
    :return:
    """
    sql = """select crossname from basedata where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    if rows is not None:
        data = rows[0][0]
        data = data.replace('\'', '')
        data = data.replace('\"', '')
        return data
    else:
        return '未知'


def _select_cross_entro_info(cross_id):
    """
    根据路口编号查找路口基础信息
    :param cross_id:
    :return:
    """
    sql = """select * from basedata where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    entro_info_dist = {}
    for row in rows:
        (crossid, crossname, eastname, westname, southname, northname) = row
        entro_info_dist['crossid'] = crossid
        entro_info_dist['crossname'] = crossname
        entro_info_dist['eastname'] = eastname
        entro_info_dist['westname'] = westname
        entro_info_dist['southname'] = southname
        entro_info_dist['northname'] = northname
    return entro_info_dist


def _select_all_cross_entro_info():
    """
    根据路口编号查找路口基础信息
    :param cross_id:
    :return:
    """
    sql = """select * from basedata"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_entro_info_List = []
    for row in rows:
        (crossid, crossname, eastname, westname, southname, northname) = row
        entro_info_dist = {}
        entro_info_dist['交叉口编号'] = crossid
        entro_info_dist['交叉口名称'] = crossname
        entro_info_dist['东进口名称'] = eastname
        entro_info_dist['西进口名称'] = westname
        entro_info_dist['南进口名称'] = southname
        entro_info_dist['北进口名称'] = northname
        cross_entro_info_List.append(entro_info_dist)
    return cross_entro_info_List


def _insert_cross_entro_info(cross_id, crossname, eastname, westname, southname, northname):
    """
    插入页面1 交叉口基本信息
    :param cross_id:
    :param crossname:
    :param eastname:
    :param westname:
    :param southname:
    :param northname:
    :return:
    """
    sql = """INSERT INTO basedata(crossid,crossname,eastname,westname,southname,northname)
                    VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\') """ % (
    cross_id, crossname, eastname, westname, southname, northname)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_entro_info(cross_id, crossname, eastname, westname, southname, northname):
    """
    更新页面1 交叉口基本信息
    :param cross_id:
    :param crossname:
    :param eastname:
    :param westname:
    :param southname:
    :param northname:
    :return:
    """
    sql = """update basedata set crossname=\'%s',eastname=\'%s',
                                westname=\'%s',southname=\'%s',northname=\'%s' where crossid=%s """ % (
        crossname, eastname, westname, southname, northname, cross_id)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_entro_info(cross_id):
    """
    删除页面1 交叉口基本信息
    :param cross_id:
    :return:
    """
    sql = """delete from basedata where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_canalization_info(cross_id):
    """
    页面2 根据路口编号查找路口渠化信息
    :param cross_id:
    :return:
    """
    sql = """select crossid,EastEntNum,SouthEntNum,WestEntNum,NorthEntNum,
                EastExNum,SouthExNum,WestExNum,NorthExNum,
                EastWidth,SouthWidth,WestWidth,NorthWidth from infom where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    canalization_info_dist = {}
    for row in rows:
        (crossid, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum, EastExNum, SouthExNum, WestExNum, NorthExNum,
         EastWidth, SouthWidth, WestWidth, NorthWidth) = row
        canalization_info_dist['crossid'] = crossid
        canalization_info_dist['EastEntNum'] = EastEntNum
        canalization_info_dist['SouthEntNum'] = SouthEntNum
        canalization_info_dist['WestEntNum'] = WestEntNum
        canalization_info_dist['NorthEntNum'] = NorthEntNum
        canalization_info_dist['EastExNum'] = EastExNum
        canalization_info_dist['SouthExNum'] = SouthExNum
        canalization_info_dist['WestExNum'] = WestExNum
        canalization_info_dist['NorthExNum'] = NorthExNum
        canalization_info_dist['EastWidth'] = EastWidth
        canalization_info_dist['SouthWidth'] = SouthWidth
        canalization_info_dist['WestWidth'] = WestWidth
        canalization_info_dist['NorthWidth'] = NorthWidth

    return canalization_info_dist


def _select_all_cross_canalization_info():
    """
    页面2 根据路口编号查找路口渠化信息
    :param cross_id:
    :return:
    """
    sql = """select crossid,EastEntNum,SouthEntNum,WestEntNum,NorthEntNum,
                EastExNum,SouthExNum,WestExNum,NorthExNum,
                EastWidth,SouthWidth,WestWidth,NorthWidth from infom"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_canalization_info_List = []
    for row in rows:
        (crossid, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
         EastExNum, SouthExNum, WestExNum, NorthExNum,
         EastWidth, SouthWidth, WestWidth, NorthWidth) = row
        canalization_info_dist = {}
        canalization_info_dist['交叉口编号'] = crossid
        canalization_info_dist['东进口车道数'] = EastEntNum
        canalization_info_dist['南进口车道数'] = SouthEntNum
        canalization_info_dist['西进口车道数'] = WestEntNum
        canalization_info_dist['北进口车道数'] = NorthEntNum
        canalization_info_dist['东出口车道数'] = EastExNum
        canalization_info_dist['南出口车道数'] = SouthExNum
        canalization_info_dist['西出口车道数'] = WestExNum
        canalization_info_dist['北出口车道数'] = NorthExNum
        canalization_info_dist['东进口车道宽度'] = EastWidth
        canalization_info_dist['南进口车道宽度'] = SouthWidth
        canalization_info_dist['西进口车道宽度'] = WestWidth
        canalization_info_dist['北进口车道宽度'] = NorthWidth
        cross_canalization_info_List.append(canalization_info_dist)
    return cross_canalization_info_List


def _insert_cross_canalization_info(crossid, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
                                    EastExNum, SouthExNum, WestExNum, NorthExNum,
                                    EastWidth, SouthWidth, WestWidth, NorthWidth):
    """
    插入页面2 交叉口基本信息
    :return:
    """
    sql = """INSERT INTO infom(crossid,EastEntNum,SouthEntNum,WestEntNum,NorthEntNum,
                EastExNum,SouthExNum,WestExNum,NorthExNum,
                EastWidth,SouthWidth,WestWidth,NorthWidth)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
        EastExNum, SouthExNum, WestExNum, NorthExNum,
        EastWidth, SouthWidth, WestWidth, NorthWidth)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_canalization_info(crossid, EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
                                    EastExNum, SouthExNum, WestExNum, NorthExNum,
                                    EastWidth, SouthWidth, WestWidth, NorthWidth):
    """
    更新页面2 交叉口渠化信息
    :return:
    """
    sql = """update infom set EastEntNum = \'%s',SouthEntNum = \'%s',WestEntNum = \'%s',NorthEntNum = \'%s',
                EastExNum = \'%s',SouthExNum = \'%s',WestExNum = \'%s',NorthExNum = \'%s',
                EastWidth = \'%s',SouthWidth = \'%s',WestWidth = \'%s',NorthWidth = \'%s' where crossid=%s """ % (
        EastEntNum, SouthEntNum, WestEntNum, NorthEntNum,
        EastExNum, SouthExNum, WestExNum, NorthExNum,
        EastWidth, SouthWidth, WestWidth, NorthWidth, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_canalization_info(cross_id):
    """
    删除页面2 交叉口渠化信息
    :param cross_id:
    :return:
    """
    sql = """delete from infom where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_all_cross_veh_flow_info():
    """
    页面3 根据路口编号查找各进口机动车流量
    :param cross_id:
    :return:
    """
    sql = """select * from VehicleInput"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_veh_flow_info_List = []
    for row in rows:
        (crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType, WestFlowType, NorthFlowType) = row
        veh_flow_info_dist = {}
        veh_flow_info_dist['交叉口编号'] = crossid
        veh_flow_info_dist['机动车东'] = EastVeh
        veh_flow_info_dist['机动车南'] = SouthVeh
        veh_flow_info_dist['机动车西'] = WestVeh
        veh_flow_info_dist['机动车北'] = NorthVeh
        veh_flow_info_dist['类型东'] = EastFlowType
        veh_flow_info_dist['类型南'] = SouthFlowType
        veh_flow_info_dist['类型西'] = WestFlowType
        veh_flow_info_dist['类型北'] = NorthFlowType
        cross_veh_flow_info_List.append(veh_flow_info_dist)
    Sqlite._conn.commit()
    sql2 = """select * from VehicleRatio"""
    Sqlite2 = mysql()
    Sqlite2.cursor.execute(sql2)
    rows2 = Sqlite2.cursor.fetchall()
    index = 0
    for row2 in rows2:
        (crossid, EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar, NorthTruck) = row2
        cross_veh_flow_info_List[index]['小车东'] = EastCar
        cross_veh_flow_info_List[index]['小车南'] = SouthCar
        cross_veh_flow_info_List[index]['小车西'] = WestCar
        cross_veh_flow_info_List[index]['小车北'] = NorthCar
        cross_veh_flow_info_List[index]['大车东'] = EastTruck
        cross_veh_flow_info_List[index]['大车南'] = SouthTruck
        cross_veh_flow_info_List[index]['大车西'] = WestTruck
        cross_veh_flow_info_List[index]['大车北'] = NorthTruck
        index += 1
    Sqlite2._conn.commit()
    sql3 = """select * from BicycleInput"""
    Sqlite3 = mysql()
    Sqlite3.cursor.execute(sql3)
    rows3 = Sqlite3.cursor.fetchall()
    index2 = 0
    for row3 in rows3:
        (crossid, EastBic, SouthBic, WestBic, NorthBic) = row3
        cross_veh_flow_info_List[index2]['非机动车东'] = EastBic
        cross_veh_flow_info_List[index2]['非机动车南'] = SouthBic
        cross_veh_flow_info_List[index2]['非机动车西'] = WestBic
        cross_veh_flow_info_List[index2]['非机动车北'] = NorthBic
        index2 += 1
    sql4 = """select * from PedInput"""
    Sqlite4 = mysql()
    Sqlite4.cursor.execute(sql4)
    rows4 = Sqlite4.cursor.fetchall()
    index3 = 0
    for row4 in rows4:
        (crossid, EastPed, SouthPed, WestPed, NorthPed) = row4
        cross_veh_flow_info_List[index3]['行人东'] = EastPed
        cross_veh_flow_info_List[index3]['行人南'] = SouthPed
        cross_veh_flow_info_List[index3]['行人西'] = WestPed
        cross_veh_flow_info_List[index3]['行人北'] = NorthPed
        index3 += 1
    return cross_veh_flow_info_List


def _select_cross_veh_flow_info(cross_id):
    """
    页面3 根据路口编号查找各进口机动车流量
    :param cross_id:
    :return:
    """
    sql = """select * from VehicleInput where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType, WestFlowType, NorthFlowType) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['EastVeh'] = EastVeh
        veh_flow_info_dist['SouthVeh'] = SouthVeh
        veh_flow_info_dist['WestVeh'] = WestVeh
        veh_flow_info_dist['NorthVeh'] = NorthVeh
        veh_flow_info_dist['EastFlowType'] = EastFlowType
        veh_flow_info_dist['SouthFlowType'] = SouthFlowType
        veh_flow_info_dist['WestFlowType'] = WestFlowType
        veh_flow_info_dist['NorthFlowType'] = NorthFlowType
    return veh_flow_info_dist


def _insert_cross_veh_flow_info(crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType,
                                WestFlowType, NorthFlowType):
    """
    插入页面3 机动车流量
    :return:
    """
    sql = """INSERT INTO VehicleInput(crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType, WestFlowType, NorthFlowType)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType, WestFlowType, NorthFlowType)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_veh_flow_info(crossid, EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType,
                                WestFlowType, NorthFlowType):
    """
    更新页面3 交叉口机动车流量
    :return:
    """
    sql = """update VehicleInput set EastVeh= \'%s',SouthVeh= \'%s',WestVeh = \'%s',NorthVeh = \'%s'
     , EastFlowType= \'%s', SouthFlowType= \'%s', WestFlowType= \'%s', NorthFlowType= \'%s' where crossid=%s """ % (
        EastVeh, SouthVeh, WestVeh, NorthVeh, EastFlowType, SouthFlowType, WestFlowType, NorthFlowType, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_veh_flow_info(cross_id):
    """
    删除页面3 交叉口机动车流量
    :param cross_id:
    :return:
    """
    sql = """delete from VehicleInput where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_veh_ratio_info(cross_id):
    """
    页面3 根据路口编号查找各进口机动车流量比例
    :param cross_id:
    :return:
    """
    sql = """select * from VehicleRatio where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar, NorthTruck) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['EastCar'] = EastCar
        veh_flow_info_dist['SouthCar'] = SouthCar
        veh_flow_info_dist['WestCar'] = WestCar
        veh_flow_info_dist['NorthCar'] = NorthCar
        veh_flow_info_dist['EastTruck'] = EastTruck
        veh_flow_info_dist['SouthTruck'] = SouthTruck
        veh_flow_info_dist['WestTruck'] = WestTruck
        veh_flow_info_dist['NorthTruck'] = NorthTruck
    return veh_flow_info_dist


def _insert_cross_veh_ratio_info(crossid, EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar,
                                 NorthTruck):
    """
    插入页面3 机动车流量比例
    :return:
    """
    sql = """INSERT INTO VehicleRatio(crossid,EastCar,EastTruck,SouthCar,SouthTruck,WestCar,WestTruck,NorthCar,NorthTruck)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar, NorthTruck)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_veh_ratio_info(crossid, EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar,
                                 NorthTruck):
    """
    更新页面3 交叉口机动车流量比例
    :return:
    """
    sql = """update VehicleRatio set EastCar= \'%s',EastTruck= \'%s',SouthCar= \'%s',SouthTruck= \'%s',WestCar= \'%s',WestTruck= \'%s',NorthCar= \'%s',NorthTruck= \'%s' where crossid=%s """ % (
        EastCar, EastTruck, SouthCar, SouthTruck, WestCar, WestTruck, NorthCar, NorthTruck, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_veh_ratio_info(cross_id):
    """
    删除页面3 交叉口机动车流量比例
    :param cross_id:
    :return:
    """
    sql = """delete from VehicleRatio where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_bicycle_flow_info(cross_id):
    """
    页面3 根据路口编号查找各进口非机动车流量
    :param cross_id:
    :return:
    """
    sql = """select * from BicycleInput where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, EastBic, SouthBic, WestBic, NorthBic) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['EastBic'] = EastBic
        veh_flow_info_dist['SouthBic'] = SouthBic
        veh_flow_info_dist['WestBic'] = WestBic
        veh_flow_info_dist['NorthBic'] = NorthBic
    return veh_flow_info_dist


def _insert_cross_bicycle_flow_info(crossid, EastBic, SouthBic, WestBic, NorthBic):
    """
    插入页面3 非机动车流量比例
    :return:
    """
    sql = """INSERT INTO BicycleInput(crossid,EastBic,SouthBic,WestBic,NorthBic)
                    VALUES(\'%s',\'%s',\'%s',\'%s',%s) """ % (crossid, EastBic, SouthBic, WestBic, NorthBic)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_bicycle_flow_info(crossid, EastBic, SouthBic, WestBic, NorthBic):
    """
    更新页面3 交叉口非机动车流量
    :return:
    """
    sql = """update BicycleInput set EastBic=\'%s',SouthBic=\'%s',WestBic=\'%s',NorthBic= \'%s' where crossid=%s """ % (
        EastBic, SouthBic, WestBic, NorthBic, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_bicycle_flow_info(cross_id):
    """
    删除页面3 交叉口非机动车流量
    :param cross_id:
    :return:
    """
    sql = """delete from BicycleInput where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_ped_flow_info(cross_id):
    """
    页面3 根据路口编号查找各进口行人流量
    :param cross_id:
    :return:
    """
    sql = """select * from PedInput where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, EastPed, SouthPed, WestPed, NorthPed) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['EastPed'] = EastPed
        veh_flow_info_dist['SouthPed'] = SouthPed
        veh_flow_info_dist['WestPed'] = WestPed
        veh_flow_info_dist['NorthPed'] = NorthPed
    return veh_flow_info_dist


def _insert_cross_ped_flow_info(crossid, EastPed, SouthPed, WestPed, NorthPed):
    """
    插入页面3 行人流量
    :return:
    """
    sql = """INSERT INTO PedInput(crossid,EastPed,SouthPed,WestPed,NorthPed)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s') """ % (crossid, EastPed, SouthPed, WestPed, NorthPed)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_ped_flow_info(crossid, EastPed, SouthPed, WestPed, NorthPed):
    """
    更新页面3 交叉口行人流量
    :return:
    """
    sql = """update PedInput set EastPed=\'%s',SouthPed=\'%s',WestPed=\'%s',NorthPed= \'%s' where crossid=%s """ % (
        EastPed, SouthPed, WestPed, NorthPed, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_ped_flow_info(cross_id):
    """
    删除页面3 交叉口行人流量
    :param cross_id:
    :return:
    """
    sql = """delete from PedInput where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_speed_info(cross_id):
    """
    页面4 根据路口编号查找各进口速度
    :param cross_id:
    :return:
    """
    sql = """select * from speed where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['carSpeed'] = float(carSpeed)
        veh_flow_info_dist['truckSpeed'] = float(truckSpeed)
        veh_flow_info_dist['bicycleSpeed'] = float(bicycleSpeed)
        veh_flow_info_dist['pedSpeed'] = float(pedSpeed)
    return veh_flow_info_dist


def _select_all_cross_speed_info():
    """
    页面4 根据路口编号查找各进口速度
    :param cross_id:
    :return:
    """
    sql = """select * from speed"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_veh_flow_info_List = []
    for row in rows:
        (crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed) = row
        veh_flow_info_dist = {}
        veh_flow_info_dist['交叉口编号'] = crossid
        veh_flow_info_dist['小车速度'] = float(carSpeed)
        veh_flow_info_dist['大车速度'] = float(truckSpeed)
        veh_flow_info_dist['非机动车速度'] = float(bicycleSpeed)
        veh_flow_info_dist['行人速度'] = float(pedSpeed)
        cross_veh_flow_info_List.append(veh_flow_info_dist)
    return cross_veh_flow_info_List


def _insert_cross_speed_info(crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed):
    """
    插入页面4 速度
    :return:
    """
    sql = """INSERT INTO speed(crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s') """ % (crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_speed_info(crossid, carSpeed, truckSpeed, bicycleSpeed, pedSpeed):
    """
    更新页面4 速度
    :return:
    """
    sql = """update speed set carSpeed=\'%s',truckSpeed=\'%s',bicycleSpeed=\'%s',pedSpeed= \'%s' where crossid=%s """ % (
        carSpeed, truckSpeed, bicycleSpeed, pedSpeed, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_speed_info(cross_id):
    """
    删除页面4 速度
    :param cross_id:
    :return:
    """
    sql = """delete from speed where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_all_cross_route_info():
    """
    页面5 根据路口编号查找机动车路径
    :param cross_id:
    :return:
    """
    sql = """select * from VehicleRoute"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_veh_flow_info_List = []
    for row in rows:
        (crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight) = row
        veh_flow_info_dist = {}
        veh_flow_info_dist['交叉口编号'] = crossid
        veh_flow_info_dist['机动车东左'] = Eastleft
        veh_flow_info_dist['机动车东直'] = EastStraight
        veh_flow_info_dist['机动车东右'] = EastRight
        veh_flow_info_dist['机动车南左'] = Southleft
        veh_flow_info_dist['机动车南直'] = SouthStraight
        veh_flow_info_dist['机动车南右'] = SouthRight
        veh_flow_info_dist['机动车西左'] = Westleft
        veh_flow_info_dist['机动车西直'] = WestStraight
        veh_flow_info_dist['机动车西右'] = WestRight
        veh_flow_info_dist['机动车北左'] = Northleft
        veh_flow_info_dist['机动车北直'] = NorthStraight
        veh_flow_info_dist['机动车北右'] = NorthRight
        cross_veh_flow_info_List.append(veh_flow_info_dist)
    sql2 = """select * from BicycleRoute"""
    Sqlite2 = mysql()
    Sqlite2.cursor.execute(sql2)
    rows2 = Sqlite2.cursor.fetchall()
    index = 0
    for row2 in rows2:
        (crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight) = row2
        # cross_veh_flow_info_List[index]['交叉口编号'] = crossid
        cross_veh_flow_info_List[index]['非机东左'] = Eastleft
        cross_veh_flow_info_List[index]['非机东直'] = EastStraight
        cross_veh_flow_info_List[index]['非机东右'] = EastRight
        cross_veh_flow_info_List[index]['非机南左'] = Southleft
        cross_veh_flow_info_List[index]['非机南直'] = SouthStraight
        cross_veh_flow_info_List[index]['非机南右'] = SouthRight
        cross_veh_flow_info_List[index]['非机西左'] = Westleft
        cross_veh_flow_info_List[index]['非机西直'] = WestStraight
        cross_veh_flow_info_List[index]['非机西右'] = WestRight
        cross_veh_flow_info_List[index]['非机北左'] = Northleft
        cross_veh_flow_info_List[index]['非机北直'] = NorthStraight
        cross_veh_flow_info_List[index]['非机北右'] = NorthRight
        index += 1
    sql3 = """select * from PedRoute"""
    Sqlite3 = mysql()
    Sqlite3.cursor.execute(sql3)
    rows3 = Sqlite3.cursor.fetchall()
    index2 = 0
    for row3 in rows3:
        (crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti) = row3
        # cross_veh_flow_info_List[index2]['交叉口编号'] = crossid
        cross_veh_flow_info_List[index2]['行人东顺'] = EastCW
        cross_veh_flow_info_List[index2]['行人东逆'] = EastAnti
        cross_veh_flow_info_List[index2]['行人南顺'] = SouthCW
        cross_veh_flow_info_List[index2]['行人南逆'] = SouthAnti
        cross_veh_flow_info_List[index2]['行人西顺'] = WestCW
        cross_veh_flow_info_List[index2]['行人西逆'] = WestAnti
        cross_veh_flow_info_List[index2]['行人北顺'] = NorthCW
        cross_veh_flow_info_List[index2]['行人北逆'] = NorthAnti
        index2 += 1
    return cross_veh_flow_info_List


def _select_cross_veh_route_info(cross_id):
    """
    页面5 根据路口编号查找机动车路径
    :param cross_id:
    :return:
    """
    sql = """select * from VehicleRoute where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['Eastleft'] = Eastleft
        veh_flow_info_dist['EastStraight'] = EastStraight
        veh_flow_info_dist['EastRight'] = EastRight
        veh_flow_info_dist['Southleft'] = Southleft
        veh_flow_info_dist['SouthStraight'] = SouthStraight
        veh_flow_info_dist['SouthRight'] = SouthRight
        veh_flow_info_dist['Westleft'] = Westleft
        veh_flow_info_dist['WestStraight'] = WestStraight
        veh_flow_info_dist['WestRight'] = WestRight
        veh_flow_info_dist['Northleft'] = Northleft
        veh_flow_info_dist['NorthStraight'] = NorthStraight
        veh_flow_info_dist['NorthRight'] = NorthRight
    return veh_flow_info_dist


def _insert_cross_veh_route_info(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight,
                                 Westleft, WestStraight,
                                 WestRight, Northleft, NorthStraight, NorthRight):
    """
    插入页面5 机动车路径
    :return:
    """
    sql = """INSERT INTO VehicleRoute(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
        WestRight, Northleft, NorthStraight, NorthRight)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_veh_route_info(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight,
                                 Westleft, WestStraight,
                                 WestRight, Northleft, NorthStraight, NorthRight):
    """
    更新页面5 机动车路径
    :return:
    """
    sql = """update VehicleRoute set Eastleft= \'%s', EastStraight= \'%s', EastRight= \'%s', Southleft= \'%s', SouthStraight= \'%s', SouthRight= \'%s', Westleft= \'%s', WestStraight= \'%s',
         WestRight= \'%s', Northleft= \'%s', NorthStraight= \'%s', NorthRight= \'%s' where crossid=%s """ % (
        Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
        WestRight, Northleft, NorthStraight, NorthRight, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_veh_route_info(cross_id):
    """
    删除页面5 机动车路径
    :param cross_id:
    :return:
    """
    sql = """delete from VehicleRoute where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_bicycle_route_info(cross_id):
    """
    页面5 根据路口编号查找非机动车路径
    :param cross_id:
    :return:
    """
    sql = """select * from BicycleRoute where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['BicEastleft'] = Eastleft
        veh_flow_info_dist['BicEastStraight'] = EastStraight
        veh_flow_info_dist['BicEastRight'] = EastRight
        veh_flow_info_dist['BicSouthleft'] = Southleft
        veh_flow_info_dist['BicSouthStraight'] = SouthStraight
        veh_flow_info_dist['BicSouthRight'] = SouthRight
        veh_flow_info_dist['BicWestleft'] = Westleft
        veh_flow_info_dist['BicWestStraight'] = WestStraight
        veh_flow_info_dist['BicWestRight'] = WestRight
        veh_flow_info_dist['BicNorthleft'] = Northleft
        veh_flow_info_dist['BicNorthStraight'] = NorthStraight
        veh_flow_info_dist['BicNorthRight'] = NorthRight
    return veh_flow_info_dist


def _insert_cross_bicycle_route_info(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight,
                                     Westleft, WestStraight,
                                     WestRight, Northleft, NorthStraight, NorthRight):
    """
    插入页面5 非机动车路径
    :return:
    """
    sql = """INSERT INTO BicycleRoute(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
         WestRight, Northleft, NorthStraight, NorthRight)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
        WestRight, Northleft, NorthStraight, NorthRight)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_bicycle_route_info(crossid, Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight,
                                     Westleft, WestStraight,
                                     WestRight, Northleft, NorthStraight, NorthRight):
    """
    更新页面5 非机动车路径
    :return:
    """
    sql = """update BicycleRoute set Eastleft= \'%s', EastStraight= \'%s', EastRight= \'%s', Southleft= \'%s', SouthStraight= \'%s', SouthRight= \'%s', Westleft= \'%s', WestStraight= \'%s',
         WestRight= \'%s', Northleft= \'%s', NorthStraight= \'%s', NorthRight= \'%s' where crossid=%s """ % (
        Eastleft, EastStraight, EastRight, Southleft, SouthStraight, SouthRight, Westleft, WestStraight,
        WestRight, Northleft, NorthStraight, NorthRight, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_bicycle_route_info(cross_id):
    """
    删除页面5 非机动车路径
    :param cross_id:
    :return:
    """
    sql = """delete from BicycleRoute where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_cross_ped_route_info(cross_id):
    """
    页面5 根据路口编号查找行人路径
    :param cross_id:
    :return:
    """
    sql = """select * from PedRoute where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['EastCW'] = EastCW
        veh_flow_info_dist['EastAnti'] = EastAnti
        veh_flow_info_dist['SouthCW'] = SouthCW
        veh_flow_info_dist['SouthAnti'] = SouthAnti
        veh_flow_info_dist['WestCW'] = WestCW
        veh_flow_info_dist['WestAnti'] = WestAnti
        veh_flow_info_dist['NorthCW'] = NorthCW
        veh_flow_info_dist['NorthAnti'] = NorthAnti
    return veh_flow_info_dist


def _insert_cross_ped_route_info(crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti):
    """
    插入页面5 行人路径
    :return:
    """
    sql = """INSERT INTO PedRoute(crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_ped_route_info(crossid, EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti):
    """
    更新页面5 行人路径
    :return:
    """
    sql = """update PedRoute set EastCW= \'%s', EastAnti= \'%s', SouthCW= \'%s', SouthAnti= \'%s', WestCW= \'%s', WestAnti= \'%s', NorthCW= \'%s', NorthAnti= \'%s' where crossid=%s """ % (
        EastCW, EastAnti, SouthCW, SouthAnti, WestCW, WestAnti, NorthCW, NorthAnti, crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_ped_route_info(cross_id):
    """
    删除页面5 行人路径
    :param cross_id:
    :return:
    """
    sql = """delete from PedRoute where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_all_cross_signal_info():
    """
    页面6 根据路口编号查找方案
    :param cross_id:
    :return:
    """
    sql = """select * from control_signal"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    cross_veh_flow_info_List = []
    for row in rows:
        (crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft, WestStraight, NorthLeft,
         NorthStraight) = row
        veh_flow_info_dist = {}
        veh_flow_info_dist['交叉口编号'] = crossid
        veh_flow_info_dist['周期长度'] = cycletime
        veh_flow_info_dist['东左转'] = EastLeft
        veh_flow_info_dist['东直行'] = EastStraight
        veh_flow_info_dist['南左转'] = SouthLeft
        veh_flow_info_dist['南直行'] = SouthStraight
        veh_flow_info_dist['西左转'] = WestLeft
        veh_flow_info_dist['西直行'] = WestStraight
        veh_flow_info_dist['北左转'] = NorthLeft
        veh_flow_info_dist['北直行'] = NorthStraight
        cross_veh_flow_info_List.append(veh_flow_info_dist)
    return cross_veh_flow_info_List


def _select_cross_signal_info(cross_id):
    """
    页面6 根据路口编号查找方案
    :param cross_id:
    :return:
    """
    sql = """select * from control_signal where crossid=%s""" % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    veh_flow_info_dist = {}
    for row in rows:
        (crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft, WestStraight, NorthLeft,
         NorthStraight) = row
        veh_flow_info_dist['crossid'] = crossid
        veh_flow_info_dist['cycletime'] = cycletime
        veh_flow_info_dist['EastLeft'] = EastLeft
        veh_flow_info_dist['EastStraight'] = EastStraight
        veh_flow_info_dist['SouthLeft'] = SouthLeft
        veh_flow_info_dist['SouthStraight'] = SouthStraight
        veh_flow_info_dist['WestLeft'] = WestLeft
        veh_flow_info_dist['WestStraight'] = WestStraight
        veh_flow_info_dist['NorthLeft'] = NorthLeft
        veh_flow_info_dist['NorthStraight'] = NorthStraight
    return veh_flow_info_dist


def _insert_cross_signal_info(crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft,
                              WestStraight, NorthLeft, NorthStraight):
    """
    插入页面6 信号方案
    :return:
    """
    sql = """INSERT INTO control_signal(crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft, WestStraight, NorthLeft, NorthStraight)
                    VALUES(\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s',\'%s') """ % (
        crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft, WestStraight, NorthLeft,
        NorthStraight)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _update_cross_signal_info(crossid, cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft,
                              WestStraight, NorthLeft, NorthStraight):
    """
    更新页面6 信号方案
    :return:
    """
    sql = """update control_signal set cycletime=\'%s', EastLeft=\'%s', EastStraight=\'%s', SouthLeft=\'%s', SouthStraight=\'%s', WestLeft=\'%s', WestStraight=\'%s', NorthLeft=\'%s', NorthStraight= \'%s' where crossid=%s """ % (
        cycletime, EastLeft, EastStraight, SouthLeft, SouthStraight, WestLeft, WestStraight, NorthLeft, NorthStraight,
        crossid)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    Sqlite._conn.commit()
    return Sqlite.a


def _delete_cross_signal_info(cross_id):
    """
    删除页面6 信号方案
    :param cross_id:
    :return:
    """
    sql = """delete from control_signal where crossid=%s """ % cross_id
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    Sqlite._conn.commit()
    return Sqlite.a


def _select_default_parm():
    """
    获取默认仿真参数
    :return:
    """
    sql = """select * from parm"""
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    parm_list = []
    row = rows[0]
    parm_list = list(row)
    parm_dict = {}
    parm_dict['time'] = parm_list[1]
    parm_dict['num'] = parm_list[2]
    parm_dict['speed'] = parm_list[3]
    parm_dict['speedmax'] = parm_list[4]
    parm_dict['step'] = parm_list[5]
    parm_dict['seedincrease'] = parm_list[6]
    parm_dict['seed'] = parm_list[7]
    parm_dict['flowincrease'] = parm_list[8]
    parm_dict['stoptime'] = parm_list[9]
    return parm_dict


def load_data():
    with open("C:\\Users\\Mr.Chen\\Desktop\\new\\11_001.fhz", 'r', encoding='utf-8') as f:
        fhz = f.read()
    """with open("C:\\Users\\Mr.Chen\\Desktop\\new\\11_001.fzp", 'r', encoding='utf-8') as f2:
        fzp=f2.read()"""
    with open("C:\\Users\\Mr.Chen\\Desktop\\new\\11_001.mer", 'r', encoding='utf-8') as f3:
        mer = f3.read()
    with open("C:\\Users\\Mr.Chen\\Desktop\\new\\11_001.rsr", 'r', encoding='utf-8') as f4:
        rsr = f4.read()
    returnData = {'fhz': fhz, 'mer': mer, 'rsr': rsr}
    return returnData


def load_vis_result(eastLane, westLane, southLane, northLane, flow):
    sql = """select  videoIndex, netDelay, netStop, netCar, netSpeed, eastQueue, westQueue, southQueue, northQueue, northQueueMax, westQueueMax, eastQueueMax, southQueueMax, eastTimeLeft, westTimeLeft, northTimeLeft, southTimeLeft, 
    eastTimeStr, westTimeStr, northTimeStr, southTimeStr, eastTimeRight, 
    westTimeRight, northTimeRight, southTimeRight, eastDelayLeft, eastDelayStr, 
    eastDelayRight, westDelayLeft, westDelayStr, northDelayStr, northDelayLeft, 
    westDelayRight, northDelayRight, southDelayLeft, southDelayStr, southDelayRight, point
                from result
                where eastlane=\'%s' and  westlane=\'%s' and southlane=\'%s' and  northlane=\'%s' and flow=\'%s';""" % (
    eastLane, westLane, southLane, northLane, flow)
    Sqlite = mysql()
    Sqlite.cursor.execute(sql)
    rows = Sqlite.cursor.fetchall()
    #Sqlite._conn.commit()
    return rows


if __name__ == '__main__':
    load_vis_result('3','3','3','3','200')
    load_data()
    # _select_all_cross_veh_flow_info()
    """ccc= _select_all_cross_entro_info()
    crossIdList = _select_crossId()
    crossName = _select_cross_name(2)
    enroInfo = _select_cross_entro_info(2)
    vehFlow = _select_cross_veh_flow_info(2)
    signal = _select_cross_signal_info(2)
    vejRatio = _select_cross_veh_ratio_info(2)
    bicycleFlow = _select_cross_bicycle_flow_info(2)
    pedFlow = _select_cross_ped_flow_info(2)
    vehRoute = _select_cross_veh_route_info(2)
    bicycleRoute = _select_cross_bicycle_route_info(2)
    pedRoute = _select_cross_ped_route_info(2)
    cana = _select_cross_canalization_info(2)
    speed = _select_cross_speed_info(2)"""
    _insert_cross_entro_info(132, 'a', 'v', 'c', 'g', 'h')
    print(2)
