import os
import xml.etree.ElementTree as ET

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_path = os.path.join(directory, filename)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # 获取旧的文件名和新的文件名
            old_filename = root.find("filename").text
            new_filename = old_filename.replace("imgs", "image")

            # 更新文件名
            root.find("filename").text = new_filename
            root.find("path").text = root.find("path").text.replace(old_filename, new_filename)

            # 保存修改后的XML文件
            tree.write(xml_path)

# 指定要更改文件名的文件夹路径
folder_path = "xml"

# 调用函数进行文件名更改
rename_files(folder_path)