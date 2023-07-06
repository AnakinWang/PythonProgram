from dbio.DbOper import DbOper
from logModule.log import Log

logger = Log.getLogger("task")
def getOneAlarm():
    dbObj = DbOper()

    sql = 'select id,device_id,event_time,alarm_type,detect_type,conf_id,image,value from alarm_info order by id asc limit 1'
    rows = dbObj.readTable(sql)

    dbObj.closeDb()

    return rows

def getOneFaceAlarm():
    '''
    result['id'] = alarmInfo[0]
    result['deviceId'] = alarmInfo[1]
    result['eventTime'] = alarmInfo[2]
    result['alarmType'] = alarmInfo[3]
    result['detectType'] = alarmInfo[4]
    result['confId'] = alarmInfo[5]
    result['image'] = alarmInfo[6]
    result['score'] = alarmInfo[7]
    result['user_ids'] = alarmInfo[8]  


    '''

    dbObj = DbOper()
    sql = 'select id,device_id,event_time,alarm_type,detect_type,conf_id,image,score,user_ids from face_alarm_info order by id asc limit 1'
    rows = dbObj.readTable(sql)

    dbObj.closeDb()

    return rows

def getCameraConf(deviceId):
    dbObj = DbOper()

    sql = 'select detect_type,b_box,conf_id,threshold from camera_conf where device_id=\"%s\"' % (deviceId)

    rows = dbObj.readTable(sql)

    dbObj.closeDb()

    return rows

def getAllFaceConf1():
    dbObj = DbOper()
    # print("#################################getOneFaceConf1")
    sql = 'select id, tasktype,faceId,faceName,faceList from face_conf1 order by id' 
    rows = dbObj.readTable(sql)
    # logger.info("get faceDB task to DB:(%s)" % str(rows))

    dbObj.closeDb()

    return rows

def getOneFaceConf1():
    dbObj = DbOper()
    # print("#################################getOneFaceConf1")
    sql = 'select id, tasktype,faceId,faceName,faceList from face_conf1 order by id asc limit 1' 
    rows = dbObj.readTable(sql)
    # logger.info("get faceDB task to DB:(%s)" % str(rows))

    dbObj.closeDb()

    return rows

def getOneFaceConf2():
    dbObj = DbOper()

    sql = 'select picName from face_conf2 order by id asc limit 1' 
    rows = dbObj.readTable(sql)
    dbObj.closeDb()

    return rows

def getWarnRecord(deviceId):
    dbObj = DbOper()

    sql = 'select warn_type from warn_record where device_id=\"%s\"' % (deviceId)

    rows = dbObj.readTable(sql)

    dbObj.closeDb()

    return rows