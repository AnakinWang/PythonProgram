from dbio import readDb
from dbio import saveDb
import time

g_config = {"ssh_host":"127.0.0.1", "ssh_user":"root", "ssh_passwd":"123456", "port":"8000"}

def postAlarm() -> None:
        while True:
            time.sleep(0.2)
            rows = readDb.getOneAlarm()
            if  rows:
                alarmInfo = rows[0]
                result = {}
                result['id'] = alarmInfo[0]
                result['deviceId'] = alarmInfo[1]
                result['eventTime'] = alarmInfo[2]
                result['alarmType'] = alarmInfo[3]
                result['detectType'] = alarmInfo[4]
                result['confId'] = alarmInfo[5]
                result['image'] = alarmInfo[6]
                result['value'] = alarmInfo[7]   # 画面人数统计值
                print("常规yolo告警:")
                print("result['id']=",result['id'])
                print("result['deviceId']=",result['deviceId'])
                print("result['eventTime']=",result['eventTime'])
                print("result['alarmType']=",result['alarmType'])
                print("result['detectType']=",result['detectType'])
                print("result['confId']=",result['confId'])
                print("result['image']=",result['image'])
                print("result['value']=",result['value'])

                # 发送告警
                #  res = sendAlarm(result)
                #  print("@@@@@@@@@@@常规告警:res=",res)
                
                # if res == 0:
                #     '''if result['alarmType']  == 1:
                #         createRemoteDir(os.path.dirname(result['image']))
                #         sshTransfer(result['image'], result['image'])
                #         os.system('rm '+ result['image'])'''

                #     saveDb.delAlarm(result['id'])    


if __name__ == "__main__":
    postAlarm()