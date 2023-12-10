import os
import xml.etree.ElementTree as ET

def rename_files(directory, old_folder_name, new_folder_name):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_path = os.path.join(directory, filename)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # 遍历所有的object元素
            for obj in root.iter("object"):
                name_elem = obj.find("name")
                old_name = name_elem.text
                new_name = old_name.replace(old_folder_name, new_folder_name)
                name_elem.text = new_name

            # 保存修改后的XML文件
            tree.write(xml_path)

# 指定要更改文件名的文件夹路径和旧的文件夹名、新的文件夹名
folder_path = "xml"
old_folder_name = "Mini bus"
new_folder_name = "Mini_bus"

# 调用函数进行文件夹名更改
rename_files(folder_path, old_folder_name, new_folder_name)