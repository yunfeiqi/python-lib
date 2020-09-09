#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/09/09 16:03:24
@Author  :   sam.qi 
@Version :   1.0
@Desc    :   Demo for nacos with python,
             reference： https://github.com/nacos-group/nacos-sdk-python
'''

import nacos


SERVER_ADDRESS = "192.168.10.155:8848"
NAMESPACE = "public"
USER = "nacos"
PWD = "nacos"

# no auth mode
client = nacos.NacosClient(
    SERVER_ADDRESS, namespace=NAMESPACE, username=USER, password=PWD)

# get config
DATA_ID = "provider-admin-service"
GROUP = "mapping-com.mlamp.mas.provider.api.TbPermissionService"
print(client.get_config(data_id=DATA_ID, group=GROUP))

# add service
SERVER_NAME = "test-server"
IP = "192.168.10.155"
PORT = "80"
CLUSTER_NAME = "py-test-server"

reg_status = client.add_naming_instance(service_name=SERVER_NAME,
                                        ip=IP, port=PORT, cluster_name=CLUSTER_NAME)
if reg_status:
    print("Service Registered")

# query service detail infomation
obj_service = client.get_naming_instance(service_name=SERVER_NAME,
                                         ip=IP, port=PORT, cluster_name=CLUSTER_NAME)
print(obj_service)
