# _*_ coding:UTF-8 _*_

import xml.dom.minidom
import sys

if len(sys.argv) < 2:
    print("Use:")
    print("     python3 "+sys.argv[0]+" xml file path")
else:
    DOMTree = xml.dom.minidom.parse(sys.argv[1])
    collection = DOMTree.documentElement  # 在集合中获取所有目标
    targets = collection.getElementsByTagName('target')

    for target in targets:
        ip = target.getElementsByTagName('ip')[0].childNodes[0].data  # 取ip地址
        record_results = target.childNodes[9].getElementsByTagName('record_results')  # 取存放端口信息的对象
        if not record_results:  # 判断空值
            continue
        else:
            for record_result in record_results:
                value_results = record_result.getElementsByTagName('value')  # 取端口信息值对象
                if not value_results or len(value_results) < 4:
                    continue
                else:
                    try:  # 异常处理value_results中value对象空值报错
                        port = value_results[0].childNodes[0].data  # 端口
                        protocol = value_results[1].childNodes[0].data  # 协议
                        service = value_results[2].childNodes[0].data  # 服务
                        status = value_results[3].childNodes[0].data  # 状态
                        print(ip + "," + port + "," + protocol + "," + service + "," + status)
                    except IndexError:
                        continue