# coding=utf-8

# 导入minidom
from xml.dom import minidom


def carate_xml():
    # 1.创建DOM树对象
    dom = minidom.Document()
    # 2.创建根节点。每次都要用DOM对象来创建任何节点。
    root_node = dom.createElement('root')
    # 3.用DOM对象添加根节点
    dom.appendChild(root_node)

    # 用DOM对象创建元素子节点
    book_node = dom.createElement('book')
    # 用父节点对象添加元素子节点
    root_node.appendChild(book_node)
    # 设置该节点的属性
    book_node.setAttribute('price', '199')

    name_node = dom.createElement('name')
    root_node.appendChild(name_node)
    # 也用DOM创建文本节点，把文本节点（文字内容）看成子节点
    name_text = dom.createTextNode('计算机程序设计语言 第1版')
    # 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
    name_node.appendChild(name_text)

    # 每一个结点对象（包括dom对象本身）都有输出XML内容的方法，如：toxml()--字符串, toprettyxml()--美化树形格式。

    # 添加新节点
    """
       <!--真实的Application的全名-->
        <meta-data android:name="app_name" android:value="com.yk.dexdeapplication.App"/>
        <!--用于dex后的目录名_版本号-->
        <meta-data android:name="app_version" android:value="/dexDir_1.0"/>
    """
    meta_data = dom.createElement("meta-data")
    # 用父节点对象添加元素子节点
    root_node.appendChild(meta_data)
    # 设置该节点的属性
    meta_data.setAttribute('name', 'app_name')
    meta_data.setAttribute('value', 'com.yk.dexdeapplication.App')

    meta_data = dom.createElement("meta-data")
    # 用父节点对象添加元素子节点
    root_node.appendChild(meta_data)
    # 设置该节点的属性
    meta_data.setAttribute('name', 'app_version')
    meta_data.setAttribute('value', '/dexDir_1.0')

    try:
        with open('./xml/dom_write.xml', 'w', encoding='UTF-8') as fh:
            # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
            # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
            dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
            print('OK')
    except Exception as err:
        print('错误：{err}'.format(err=err))


def parse_xml():
    # dom = None
    # with open('./xml/dom_write.xml', 'r', encoding='UTF-8') as f:
    #     dom = parse(f)

    # 获取根节点
    # root = dom.documentElement

    # from xml.dom import minidom

    # 第1步：parse()工厂方法获取DOM对象
    dom = minidom.parse('./xml/dom_write.xml')

    # 第2步：要获取某个元素节点的文本内容，就通过DOM对象，先获取该元素节点，再获取子文本节点，最后通过“data”属性获取文本内容（注意返回的是列表）
    # meta_data = dom.getElementsByTagName('meta-data')[0].childNodes[0].data
    meta_data = dom.getElementsByTagName('meta_data')
    print(meta_data)

    # 其他属性与方法：
    # 获取根节点
    root = dom.documentElement
    # 节点名称
    print(root.nodeName)
    # 节点类型：'ELEMENT_NODE'，元素节点； 'TEXT_NODE'，文本节点； 'ATTRIBUTE_NODE'，属性节点
    print(root.nodeType)
    # 获取某个节点下所有子节点，是个列表
    print(root.childNodes)
    # 根据标签名获取元素节点，是个列表
    book = root.getElementsByTagName('book')
    # 获取节点属性
    print(book[0].getAttribute('price'))
    # 获取某节点的父节点
    # print(author.parentNode.nodeName)


if __name__ == "__main__":
    # 创建xml文档
    carate_xml()

    # 解析xml文档
    parse_xml()
