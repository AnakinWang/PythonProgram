from dbio.DbOper import DbOper
from logModule.log import Log

logger = Log.getLogger("task")

def clearCameraConf(deviceId):
        dbObj = DbOper()
        sql = 'delete from camera_conf where device_id=\"%s\"' % (deviceId)
        dbObj.writeTable(sql)
        dbObj.closeDb()

def saveConfToDb(jsonData):
    if not jsonData['data']:
        return

    dbObj = DbOper()
    devide_id = jsonData['deviceNo']
    dataList = jsonData['data']

    for data in dataList:
        alarmType = data['alarmType']
        for meter in data['meterInfo']:
            bBox = meter['bBox']
            confId = meter['confId']
            threshold = meter['threshold']
            sql = 'insert into camera_conf(device_id,detect_type,b_box,conf_id,threshold)' \
                'values(\"%s\",%s,\"%s\",%s,%s)' % (devide_id,str(alarmType),bBox,str(confId),str(threshold))
            
            dbObj.writeTable(sql)

    dbObj.closeDb()

def saveFaceConf1ToDb(jsonData):

    dbObj = DbOper()
    alarmType = jsonData['type']
    faceId = jsonData['faceId']
    faceName = jsonData['faceName']
    faceList = jsonData['faceList']
    faceList = ''
    for faceimg in  jsonData['faceList']:
        if not faceList=='':
            faceList += '&'
        # faceimg = faceimg.replace("-", "_")
        # faceimg = faceimg.replace(".jpg","")
        faceList += faceimg
    logger.info("save faceDB task to DB:(%s,%s,%s,%s)"%(str(alarmType),str(faceId),faceName,faceList))
    print("save faceDB task to DB:(%s,%s,%s,%s)"%(str(alarmType),str(faceId),faceName,faceList))
    sql = 'insert into face_conf1(tasktype,faceId, faceName,faceList)' \
                'values(%s,%s,\"%s\",\"%s\")' % (str(alarmType),str(faceId),faceName,faceList)

    dbObj.writeTable(sql)
    dbObj.closeDb()

def delFaceConf1(id):
    dbObj = DbOper()
    print("###############delFaceConf1,ID=",id)
    sql = 'delete from face_conf1 where id=%s' % (str(id))
    dbObj.writeTable(sql)

    dbObj.closeDb()

def saveFaceConf2ToDb(jsonData):

    dbObj = DbOper()
    picName = jsonData['picName']

    sql = 'insert into face_conf2(picName)' \
                'values(%s)' % (picName)

    dbObj.writeTable(sql)
    dbObj.closeDb()

def delFaceConf2(id):
    dbObj = DbOper()

    sql = 'delete from face_conf2 where id=%s' % (str(id))
    dbObj.writeTable(sql)

    dbObj.closeDb()

def saveAlarmTodb(alarmList):
    dbObj = DbOper()
    for alarm in alarmList:
        deviceId = alarm['deviceId']
        detectType = alarm["detectType"]
        eventTime = alarm['eventTime']
        alarmType = alarm['alarmType']
        confId = alarm['confId']
        image = alarm['image']
        score = alarm['score']
        value = alarm['value']

        sql = 'insert into alarm_info(device_id,event_time,alarm_type,detect_type,conf_id,image,score,value) '\
            'values(\"%s\",\"%s\",\"%s\",%s,%s,\"%s\",%s,%s)' % (deviceId, eventTime, str(alarmType), str(detectType),str(confId), image, str(score),str(value))
        dbObj.writeTable(sql)
        print()
    dbObj.closeDb()


def saveFaceAlarmTodb(alarmList):
    print("########### saveAlarmTodb(alarm)")

    dbObj = DbOper()
    for alarm in alarmList:
        deviceId = alarm['deviceId']
        detectType = alarm["detectType"]
        eventTime = alarm['eventTime']
        alarmType = alarm['alarmType']
        confId = alarm['confId']
        image = alarm['image']
        score = alarm['score']
        user_ids = alarm['user_ids']
        print('alarmType=',alarmType)
        print('user_ids=',user_ids)
        user_ids = ''
        for user_id in alarm['user_ids']:
            if not user_ids == '':
                user_ids += '&'
            user_ids += str(user_id)
        print('###final:user_ids=',user_ids)

        # user_ids = 'wwww'
        print('insert into face_alarm_info(device_id,event_time,alarm_type,detect_type,conf_id,image,score,user_ids) '\
            'values(\"%s\",\"%s\",\"%s\",%s,%s,\"%s\",%s,%s)' % (deviceId, eventTime, str(alarmType), str(detectType),str(confId), image, str(score),str(user_ids)))
        sql = 'insert into face_alarm_info(device_id,event_time,alarm_type,detect_type,conf_id,image,score,user_ids) '\
            'values(\"%s\",\"%s\",\"%s\",%s,%s,\"%s\",%s,%s)' % (deviceId, eventTime, str(alarmType), str(detectType),str(confId), image, str(score),user_ids)
        dbObj.writeTable(sql)
        
    dbObj.closeDb()
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ dbObj.closeDb()")

def delAlarm(id):
    dbObj = DbOper()

    sql = 'delete from alarm_info where id=%s' % (str(id))
    dbObj.writeTable(sql)

    dbObj.closeDb()


def delFaceAlarm(id):

    print('################delFaceAlarm')
    dbObj = DbOper()

    sql = 'delete from face_alarm_info where id=%s' % (str(id))
    dbObj.writeTable(sql)
    dbObj.closeDb()

def saveWarnRecord(deviceId, warn_type):
    dbObj = DbOper()
    sql = 'insert into warn_record(device_id,warn_type) values(\"%s\",%s)' % (deviceId, str(warn_type))
    dbObj.writeTable(sql)
    dbObj.closeDb()

def delWarnRecord(deviceId, warn_type):
    dbObj = DbOper()
    sql = 'delete from warn_record where device_id=\"%s\" and warn_type=%s' % (deviceId, str(warn_type))
    dbObj.writeTable(sql)
    dbObj.closeDb()
