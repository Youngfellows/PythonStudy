#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import os
from subprocess import check_call
from xml.dom.minidom import parse
import shutil

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

stApkToolPt = r'D:\Android\Apktool\apktool_2.4.1\apktool.jar'  # apktool反编译工具
stShellAppPt = r'.\shellApplicationSourceCode'  # 壳工程
staaptPt = r'D:\Android\sdk\build-tools\30.0.2\aapt.exe'  # apk打包工具
stAndroidJarlibPt = r'D:\Android\sdk\platforms\android-29\android.jar'  # 编译壳的依赖
stdxJarPt = r'D:\Android\sdk\build-tools\30.0.2\lib\dx.jar'  # jar转dex工具
stApksignJarPt = r'D:\Android\sdk\build-tools\30.0.2\lib\apksigner.jar'  # 签名工具
stCurrentPt = os.path.abspath(__file__).replace(os.path.basename(__file__), "")  # 当前路径


def repackage_payload_apk(fp):
    # command = 'apktool b apkshield_tmp -o tmp.apk'
    # os.system(command)

    """
       替换壳Applicaiton name到原apk的AndroidManifest.xml内
       :param fp: 原始apk路径
       :param stValue: 需要替换的内容
       :return:
    """

    stDecompDp = os.path.join(stCurrentPt, fp + "decompile")

    # 使用apktool重新打包apk
    cmd = []
    cmd.append('java')
    cmd.append('-jar')
    cmd.append(stApkToolPt)
    cmd.append('b')
    cmd.append('-o')
    cmd.append("result.apk")
    cmd.append(stDecompDp)
    check_call(cmd)

    # 删除反编译后的文件
    # shutil.rmtree(stDecompDp)


def get_manifest_from_repkg_apk():
    # command = 'unzip tmp.apk AndroidManifest.xml'
    # os.system(command)
    """
    解压重新打包后的apk,获取AndroidManifest.xml到当前路径
    """
    print("解压重新打包后的apk,获取AndroidManifest.xml到当前路径")


def get_manifest(apk_path):
    """反编译解压apk,获取AndroidManifest.xml文件"""
    # command = 'apktool d ' + apk_path + ' -o apkshield_tmp'
    # os.system(command)
    decompAPK(apk_path)
    stDisassembleDp = apk_path + "decompile"
    stAMFp = os.path.join(stDisassembleDp, "AndroidManifest.xml")
    print("stAMFp:{}".format(stAMFp))
    return stAMFp


def decompAPK(fp):
    """
    使用apktool反编译apk
    :param fp: 需要反编译的apk路径
    :return:
    """
    cmd = []
    cmd.append('java')
    cmd.append('-jar')
    cmd.append(stApkToolPt)
    cmd.append('d')
    cmd.append('-o')
    cmd.append(fp + "decompile")
    cmd.append(fp)
    check_call(cmd)


def add_new_manifest_to_apk(path):
    # command = 'zip -m ' + path + ' AndroidManifest.xml'
    # os.system(command)
    print("添加更新后的AndroidManifest.xml到原apk")


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def modify_manifest2(fp):
    """
    更新AndroidManifest.xml
    :param fp: apk文件路径
    :return: 更新AndroidManifest.xml文件路径
    """
    shield_application_name = 'com.egguncle.shield.ShieldApplication22'

    # 更新AndroidManifest.xml
    # f反编译后的AndroidManifest.xml路径
    stAXMLFp = os.path.join(stCurrentPt, fp + "decompile", "AndroidManifest.xml")
    dom = None
    with open(stAXMLFp, 'r', encoding='UTF-8') as f:
        dom = parse(f)
    root = dom.documentElement
    app = root.getElementsByTagName('application')[0]
    app.setAttribute("android:name", shield_application_name)  # 更新节点
    # 添加新节点
    """
       <!--真实的Application的全名-->
        <meta-data android:name="app_name" android:value="com.yk.dexdeapplication.App"/>
        <!--用于dex后的目录名_版本号-->
        <meta-data android:name="app_version" android:value="/dexDir_1.0"/>
    """
    meta_data = dom.createElement("meta-data")
    # 用父节点对象添加元素子节点
    app.appendChild(meta_data)
    # 设置该节点的属性
    meta_data.setAttribute('android:name', 'app_name')
    meta_data.setAttribute('android:value', 'com.yk.dexdeapplication.App')

    meta_data = dom.createElement("meta-data")
    # 用父节点对象添加元素子节点
    app.appendChild(meta_data)
    # 设置该节点的属性
    meta_data.setAttribute('android:name', 'app_version')
    meta_data.setAttribute('android:value', '/dexDir_1.0')
    with open(stAXMLFp, "w", encoding='UTF-8') as f:
        dom.writexml(f, encoding='UTF-8')

    return stAXMLFp


def modify_manifest(path):
    """
    更新AndroidManifest.xml文件内容
    :param path: AndroidManifest.xml文件路径
    :return: AndroidManifest.xml文件路径
    """
    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
    shield_application_name = 'com.egguncle.shield.ShieldApplication22'
    tree = ET.parse(path)
    root = tree.getroot()

    # package_name = root.get('package')
    for child in root:
        if child.tag == 'application':
            # application_tag = child
            # for (k, v) in child.items():
            #     print k, v
            #     if k == '{http://schemas.android.com/apk/res/android}name':
            #       child['{http://schemas.android.com/apk/res/android}name']=''
            payload_application_name = child.get('{http://schemas.android.com/apk/res/android}name')
            print(payload_application_name)
            # 更新application下的android:name节点
            child.set('{http://schemas.android.com/apk/res/android}name', shield_application_name)

            # 添加新节点
            element = ET.Element('meta-data')
            element.set('{http://schemas.android.com/apk/res/android}name', 'APPLICATION_CLASS_NAME')
            element.set('{http://schemas.android.com/apk/res/android}value', payload_application_name)
            child.append(element)
            print('---')

    tree.write(path)
    return path


def shield_manifest(apk_path):
    print('get manifest')
    manifest_path = get_manifest(apk_path)

    print('start to modify AndroidManifest.xml')
    # modify_manifest(manifest_path)
    modify_manifest2(apk_path)

    print('repackage apk')
    repackage_payload_apk(apk_path)

    print('get manifest from repkg apk')
    get_manifest_from_repkg_apk()

    print('add new manifest to apk')
    add_new_manifest_to_apk(apk_path)


def main(argv):
    """
    获取命令行参数: python .\06_shield_manifest.py -p .\apk\fragmentation.apk
    :param argv: 命令行参数
    :return:
    """
    try:
        opts, args = getopt.getopt(argv, "hp:", ["payload_path="])
    except getopt.GetoptError:
        print('-p <payload apk path> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-p <payload apk path> ')
            sys.exit()
        elif opt in ("-p", "--payload_path"):
            payload_path = arg
            print("payload_path:{}".format(payload_path))
            shield_manifest(payload_path)


if __name__ == "__main__":
    main(sys.argv[1:])
