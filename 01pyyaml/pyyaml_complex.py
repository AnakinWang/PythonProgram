import yaml
import os

def run():
    with open('SmokeService.yaml', 'r', encoding='utf-8') as file:    # 有中文。加上utf-8
        yaml_data = yaml.load(file, Loader=yaml.Loader)

        print(yaml_data['plugins'])
        print(yaml_data['plugins'][0]['plugin_name'])
        print(yaml_data['class_list'][0]['class_id'])
        print(yaml_data['class_list'][0]['class_name'])               # 根据输出的具体类型，灵活调用数据


if __name__ == "__main__":
    run()