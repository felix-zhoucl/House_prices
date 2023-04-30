# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/30 14:40
# @File_name:find_ip
import json

import requests

from environment import get_config


def get_address_by_ip(ip_address: str):
    """
    通过ip获取模糊地址
    :param ip_address:
    :return:
    """
    path = "../../config.json"
    ticket = get_config("map_key", path)
    # return ticket
    url = "https://apis.map.qq.com/ws/location/v1/ip?key={}&ip={}".format(ticket, ip_address)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)
    status = result.get("status")
    if status == 0:
        location = result.get("result", {}).get("location") or {}
        truth_address = get_address_by_location(location)
        return truth_address
    else:
        return "请求腾讯地图接口失败"


def get_address_by_location(location: dict):
    """
    根据经纬度获取位置区域
    :rtype: str
    :param location:
    :return:
    """
    lat = location.get("lat")
    lng = location.get("lng")
    url = "https://www.amap.com/service/regeo?longitude={}&latitude={}".format(lng, lat)
    response = requests.request("GET", url)
    result = json.loads(response.text)
    status = result.get("status")
    if status == "1":
        data=result.get("data")
        country = data.get("country") or ""
        desc = data.get("desc") or ""
        pos = data.get("pos") or ""
        return country + desc + pos
    else:
        return "请求高德地图接口失败"


if __name__ == '__main__':
    ip_addr = "60.208.111.211"
    address = get_address_by_ip(ip_addr)
    print(address)
