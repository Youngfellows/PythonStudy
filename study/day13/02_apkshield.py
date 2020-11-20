# coding=utf-8
import sys
import getopt
import os
import zipfile
import binascii
from zlib import adler32
from hashlib import sha1
import shutil
from subprocess import check_call

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class ApkShield(object):
    def __init__(self):
        object.__init__(self)
        self.stApkToolPt = r'D:\Android\Apktool\apktool_2.4.1\apktool.jar'

    def main(self, argv):
        """
        取得命令行参数: python .\01_apkshield.py -s xxx.apk -p yyy.apk
        :param argv:
        :return:
        """
        shield_path = ''
        payload_path = ''
        try:
            print("args:{}".format(argv))
            opts, args = getopt.getopt(argv, "hs:p:", ["shield_path=", "payload_path="])
        except getopt.GetoptError:
            print('-s <shield apk path>', '-p <payload apk path>')
            sys.exit(2)
        print("args:{}".format(args))
        print("opts:{}".format(opts))
        for opt, arg in opts:
            if opt == '-h':
                print
                '-s <shield apk path>', '-p <payload apk path>'
                sys.exit()
            elif opt in ("-s", "--shield_path"):
                shield_path = arg
            elif opt in ("-p", "--payload_path"):
                payload_path = arg
        print("shield_path:{}".format(shield_path))
        print("payload_path:{}".format(payload_path))

    def unzip_apk(self, path, dir_temp="shield_tmp"):
        """
        解压APK
        :param path: 需要解压的文件
        :param dir_temp: 解压后的目录
        :return: 解压后的dex文件路径
        """
        # 重命名apk为zip
        if path[-4:len(path)] != '.apk':
            print('shield file error ,is not a apk file.')

        zip_name = path[:-4] + '.zip'
        if os.path.exists(zip_name):
            print("{}已经存在...".format(zip_name))
        else:
            os.rename(path, zip_name)

        # 解压
        zip_file = zipfile.ZipFile(zip_name)
        shield_tmp_path = './apk/' + dir_temp
        if os.path.exists(shield_tmp_path) is False:
            os.mkdir(shield_tmp_path)

        for name in zip_file.namelist():  # 返回压缩包内所有文件名的列表。
            zip_file.extract(name, './apk/{}/'.format(dir_temp))  # 解压到指定目录

        dex_file_path = shield_tmp_path + '/classes.dex'
        zip_file.close()

        # 返回dex数据路径
        return dex_file_path

    def add_payload_to_shield(self, shield_path, payload_path):
        # 解压apk
        # dex_apk_path = "./apk/fragmentation.apk"
        # source_apk_path = "./apk/fragmentation2.apk"
        dex_apk_path = shield_path
        source_apk_path = payload_path

        dex_path = self.unzip_apk(dex_apk_path)  # 壳dex
        source_dex_path = self.unzip_apk(source_apk_path, "source_temp")  # 源dex
        print("dex_path:{}".format(dex_path))
        print("source_dex_path:{}".format(source_dex_path))

        # 将源apk拼接到壳apk后面
        payload_file = self.read_file(source_dex_path)
        dex_file = self.read_file(dex_path)
        payload_data = binascii.b2a_hex(payload_file)
        dex_data = binascii.b2a_hex(dex_file)

        # 这里按照大端把长度数据给填进去了,没有做小端处理,填进去的payload数据也是一样,回头解析出来的时候也得用大端
        # 大小只有6字节,这里加个00当作对齐,默认大小是4字节
        hex_len_payload = '00' + hex(len(payload_file))[2:]  # 原始数据的长度
        print("payload length :{}".format(hex_len_payload))

        encrypt_data = self.encrypt_payload(payload_data)  # 加密原始dex
        length_data = binascii.b2a_hex(bytearray(hex_len_payload, encoding="utf-8"))
        dex_data_encrypt = dex_data + encrypt_data + length_data  # 加密后新的dex
        print("all data length: {}".format(len(dex_data_encrypt)))

        # 修复dex
        print('fix header')
        # self.fix_dex_header(dex_data)

        print('write data to shell dex ')
        # 将数据写回壳dex
        # classes_dex_data = binascii.a2b_hex(dex_data)
        # self.write_file(classes_dex_data, "./apk/shield_dex.dex")

        # 移动壳文件到源目录
        print(dex_path)
        dex_path_temp = "./apk/classes.dex"
        dex_path_temp2 = "./apk/shield_dex.dex"
        source_apk_temp = "./apk/source_temp"

        if os.path.exists(dex_path_temp):
            os.remove(dex_path_temp)
        self.move_file_to_dir(dex_path, "./apk")

        if os.path.exists(dex_path_temp2):
            os.remove(dex_path_temp2)
        os.renames(dex_path_temp, dex_path_temp2)

        self.move_file_to_dir(dex_path_temp2, source_apk_temp)
        # write_file(classes_dex_data, "./shield_dex.dex")
        print('success')

    def shield(self):
        """
        加固加壳
        :return:
        """
        shield_path = "./apk/fragmentation.apk"
        payload_path = "./apk/fragmentation2.apk"
        # 解压壳apk,源apk,并移动壳apk classes.dex到源apk
        # self.add_payload_to_shield(shield_path, payload_path)

        # 修改manifest
        self.shield_manifest(payload_path)

    def shield_manifest(self, apk_path):
        print('get manifest')
        manifest_path = self.get_manifest(apk_path)  # 反编译获取AndroidManifest.xml

        print('start to modify AndroidManifest.xml')  # 更新AndroidManifest.xml内容
        self.modify_manifest(manifest_path)

        # print( 'repackage apk')
        self.repackage_payload_apk("./apk/apkshield_tmp/")  # 二次打包

        # print('get manifest from repkg apk')
        # get_manifest_from_repkg_apk()
        # print( 'add new manifest to apk')
        # add_new_manifest_to_apk(apk_path)

    def decompAPK(self, fp):
        """
        调用Apktools反编译apk: apktool d fragmentation.apk -o apkshield_tmp
        :param fp:
        :return:
        """
        cmd = []
        cmd.append('java')
        cmd.append('-jar')
        cmd.append(self.stApkToolPt)
        cmd.append('d')
        cmd.append('-o')
        # cmd.append(fp + "decompile")
        cmd.append("./apk/apkshield_tmp")
        cmd.append(fp)
        check_call(cmd)

    def repackage_payload_apk(self, stDecompDp):
        """
        调用Apktool二次打包: apktool b apkshield_tmp -o tmp.apk
        :return:
        """
        # command = 'apktool b apkshield_tmp -o tmp.apk'
        # os.system(command)

        cmd = []
        cmd.append('java')
        cmd.append('-jar')
        cmd.append(self.stApkToolPt)
        cmd.append('b')
        cmd.append('-o')
        cmd.append("./apk/result.apk")
        cmd.append(stDecompDp)
        check_call(cmd)

    def get_manifest(self, apk_path):
        """
        反编译获取AndroidManifest.xml
        :param apk_path:
        :return:
        """
        self.decompAPK(apk_path)
        return "./apk/apkshield_tmp/AndroidManifest.xml"

    def modify_manifest(self, path):
        """更新xml文件内容"""
        ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
        shield_application_name = 'me.yokeyword.sample.App2'
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

                # 更新标签属性
                child.set('{http://schemas.android.com/apk/res/android}name', shield_application_name)

                # 添加新标签节点
                element = ET.Element('meta-data')
                element.set('{http://schemas.android.com/apk/res/android}name', 'APPLICATION_CLASS_NAME')
                element.set('{http://schemas.android.com/apk/res/android}value', payload_application_name)
                child.append(element)
                print('---')

        tree.write(path)
        return path

    def move_file_to_dir(self, src_file, dest_dir):
        """
        移动文件到指定目录
        :param src_file: 移动的文件
        :param dest_dir: 目标目录
        :return:
        """
        try:
            shutil.move(src_file, dest_dir)  # 移动文件
        except:
            pass

    def write_file(self, data, path):
        with open(path, 'wb') as f:
            f.write(data)
        pass

    def read_file(self, path):
        """
        读取文件二进制数据
        :param path: 文件路径
        :return: 二进制数据
        """
        with open(path, 'rb') as f:
            return bytearray(f.read())

    def encrypt_payload(self, payload_data):
        """
        这里可以对源文件进行加密,这只是一个demo,所以这里就不做什么操作了
        :param payload_data: 需要加密的数据
        :return: 加密后的数据
        """
        return payload_data

    def change_str(self, start, end, src_str, add_str):
        return src_str[0:start] + add_str + src_str[end:]

    def fix_dex_header(self, hex_data):
        bin_data = binascii.a2b_hex(hex_data)
        # 修复头中的checksum signature file_size信息
        # 按照顺序,修复file_size,signature,checksum,因为后面两个需要基于前面的数据来计算
        # read magic
        magic_set = 0
        magic_offset = 8 * 2
        magic = hex_data[magic_set:magic_offset]
        if magic != '6465780a30333500':
            print('magic error')
            sys.exit()
        m = magic.decode('hex').split('\n')
        #  print 'magic :', m[0]
        #  print 'version :', m[1]

        # read checksum
        checksum_set = magic_offset
        checksum_offset = checksum_set + 4 * 2
        checksum = self.endan_little(hex_data[checksum_set:checksum_offset])
        # print 'checksum :', checksum

        # read signature
        signature_set = checksum_offset
        signature_offset = signature_set + 20 * 2
        signature = hex_data[signature_set:signature_offset]
        # print 'signature :', signature

        # read file_size 这里的filesize是从头读出来的,我们需要自己算,然后再写回去,也要注意大小端
        file_size_set = signature_offset
        file_size_offset = file_size_set + 4 * 2
        file_size = int(self.endan_little(hex_data[file_size_set:file_size_offset]), 16)
        # print 'file_size :', file_size

        # 计算新的文件大小
        new_file_size = len(bin_data)
        # 计算新的文件大小并处理大小端问题,准备填回去
        new_file_size_hex = self.endan_little('00' + hex(new_file_size)[2:])
        # hex_data[file_size_set:file_size_offset] = new_file_size_hex
        hex_data = self.change_str(file_size_set, file_size_offset, hex_data, new_file_size_hex)

        # 计算新的signature值
        signature_data = binascii.a2b_hex(hex_data[signature_offset:])
        new_signature = self.sha1(signature_data).hexdigest()
        hex_data = self.change_str(signature_set, signature_offset, hex_data, new_signature)

        # 计算新的checksum值
        data_for_checksum = hex(adler32(binascii.a2b_hex(hex_data[checksum_offset:])))
        data_for_checksum = data_for_checksum[data_for_checksum.find('x') + 1:]
        new_checksum = self.endan_little(data_for_checksum)
        # print 'new checksum :',new_checksum
        hex_data = self.change_str(checksum_set, checksum_offset, hex_data, new_checksum)

        # 至此,dex头部修复完成
        return hex_data

    def endan_little(self, data):
        list = []
        for i in range(0, len(data), 2):
            list.append(data[i] + data[i + 1])
        list.reverse()
        return ''.join(list)


if __name__ == "__main__":
    apkshield = ApkShield()
    # apkshield.main(argv=sys.argv[1:])
    apkshield.shield()
