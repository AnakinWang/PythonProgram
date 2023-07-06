import yaml
import os

class DataPre:
    __slots__=("xml_dir","output_dir","datasets_name","labels_train","aug","ratio","imgsz","model_type",
    "exist_ok","SVN_URL",'DATASET_DIR','show','SVN_URL_FLAG','LOCAL_DIR','SVN_TYPE','difficult','labels_replace')

class YOLOv5DataPre:
    def __init__(self)->None:
        self.paraFile = '1_data_config.yaml'
        self.para_list = DataPre()
        self.load_para_list()

    def load_para_list(self):
        curr_path = os.getcwd()
        print("curr_path:{}".format(curr_path))

        para_file_path = os.path.join(curr_path, self.paraFile)
        print("para_file_path:{}".format(para_file_path))

        para_list = dict()
        if os.path.exists(para_file_path):
            with open(para_file_path, 'r', encoding='utf-8') as f:
                docs = yaml.load_all(f, Loader=yaml.FullLoader)
                # print("docs:{}".format(docs))  # docs:<generator object load_all at 0x00000243EC4EEE40>
                for doc in docs:
                    for k,v in doc.items():
                        para_list[k] = v['value']
                        # print("para_list:{}".format(para_list))

        if "SVN_URL" in para_list:
            self.para_list.SVN_URL = para_list["SVN_URL"]
        else:
            self.para_list.SVN_URL = []

        if 'ratio' in para_list:
            self.para_list.ratio = float(para_list['ratio'])
        else:
            self.para_list.ratio = 0.8

        if 'labels_train' in para_list:
            print("labels_train",para_list['labels_train'])
            self.para_list.labels_train = para_list['labels_train']
        else:
            self.para_list.labels_train = ''

        if "SVN_URL_FLAG" in para_list:
            self.para_list.SVN_URL_FLAG = para_list["SVN_URL_FLAG"]
        else:
            self.para_list.SVN_URL_FLAG = True

    def load_yaml_str(self):  # 将yaml格式变成dict格式
        yaml_str ='''
        name: John
        age: 30
        hobbies:
          - reading
          - hiking
        '''
        data = yaml.load(yaml_str, Loader=yaml.Loader)
        print(data)
        return data

    def dump_yaml_config(self, data):   #  将dict转变成yaml格式
        str = {}
        str = data
        yaml_str = yaml.dump(str)
        print("yaml_str:{}".format(yaml_str))


if __name__ == "__main__":
    run = YOLOv5DataPre()
    run.load_para_list()
    # print("SVN_URL:{}".format(run.para_list.SVN_URL))
    # print("ratio:{}".format(run.para_list.ratio))
    # print("labels_train:{}".format(run.labels_train))
    print("SVN_URL_FLAG:{}".format(run.para_list.SVN_URL_FLAG))

    data = run.load_yaml_str()
    run.dump_yaml_config(data)