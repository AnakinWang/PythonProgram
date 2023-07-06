from http.server import BaseHTTPRequestHandler
from app_algorithm.dbio import saveDb
import json
from app_algorithm.logModule.log import Log
 
logger = Log.getLogger("task")
 
class Resquest(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "Apache"   #设置服务器返回的的响应头 
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type","application/json") 
        self.end_headers()

        if 'openApi/camera/setconf' in self.path:
            #获取post提交的数据
            datas = self.rfile.read(int(self.headers['content-length']))    #固定格式，获取表单提交的数据
            json_dict = json.loads(datas)
            logger.info("receive conf data:%s", str(json_dict))

            ret, buf = self.checkBody(json_dict)
            if ret == False:
                logger.error('request body error:%s', buf['status'])
                self.wfile.write(json.dumps(buf).encode()) 
                return

            saveDb.clearCameraConf(json_dict['deviceNo'])
            saveDb.saveConfToDb(json_dict)
        
            self.wfile.write(json.dumps(buf).encode()) 
        # 人脸识别增删改查任务下发
        elif 'openApi/camera/faceSetconf' in self.path:
              #获取post提交的数据
            datas = self.rfile.read(int(self.headers['content-length']))    #固定格式，获取表单提交的数据
            json_dict = json.loads(datas)
            logger.info("receive conf data:%s", str(json_dict))
            ret, buf = self.checkFaceBody(json_dict)
            if ret == False:
                logger.error('request body error:%s', buf['status'])
                self.wfile.write(json.dumps(buf).encode()) 
                return
            saveDb.saveFaceConf1ToDb(json_dict)

        else:
            strErr = 'unknown request:%s' % self.path
            buf = {"code":400, "status":strErr}
            logger.error('known request:%s', self.path)
            self.wfile.write(json.dumps(buf).encode()) 

    def checkBody(self, jsonData):
        if 'deviceNo' not in jsonData:
            return False, {"code":400, "status":"deviceNo is needed"}
        if 'data' not in jsonData:
            return False, {"code":400, "status":"data is needed"}

        if jsonData['data']:
            dataList = jsonData['data']
            for data in dataList:
                if 'alarmType' not in data:
                    return False, {"code":400, "status":"alarmType is needed"}
                
                if 'meterInfo' not in data:
                    return False, {"code":400, "status":"meterInfo is needed"}
                for meter in data['meterInfo']:
                    if 'bBox' not in meter:
                        return False, {"code":400, "status":"bBox is needed"}
                    if 'confId' not in meter:
                        return False, {"code":400, "status":"confId is needed"}
                    if 'threshold' not in meter:
                        return False, {"code":400, "status":"threshold is needed"}

        return True, {"code":200, "status":"success"}
    
    def checkFaceBody(self, jsonData):
        if 'type' not in jsonData:
            return False, {"code":400, "status":"type is needed"}

        if int(jsonData['type']) == 3:
            # 查找任务
            if 'picName' not in jsonData:
                return False, {"code":400, "status":"when type=3, picName is needed"}
            else:
                # 查找图片
                conf_file = "../faceRecognition/face_config.yaml"
                if not os.path.exists(conf_file):
                    raise Exception('Config file path [%s] invalid!' % conf_file)
                with open(conf_file) as fp:
                    configs = yaml.load(fp, Loader=yaml.FullLoader)
                    deploy_conf = configs["FACE"]
                    faceDB_path = deploy_conf["FACE_DB"]
                for root, dir, files in os.walk(faceDB_path):
                    for d in dir:
                        dir_path = os.path.join(root,d)
                        imgs = glob.glob(dir_path+"/*.jpg")
                        for img in imgs:
                            img_name = img.split('/')[-1]
                            if img_name == picName:
                                # 查询成功
                                return True, {"result":1,"code":200, "status":"success"}
                # 查询失败
                return True, {"result":0,"code":200, "status":"success"}
        else:
            # 增删改任务
            if 'faceId' not in jsonData:
                return False, {"code":400, "status":"when type !=3, faceId is needed"}
            if 'faceName' not in jsonData:
                return False, {"code":400, "status":"when type !=3, faceName is needed"}
            if 'faceList' not in jsonData:
                return False, {"code":400, "status":"when type !=3, faceList is needed"}

        return True, {"result":1,"code":200, "status":"success"}


