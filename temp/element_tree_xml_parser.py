#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File     : element_tree_xml_parser
@Author   : 周恒-z50003220
@Email    : zhouheng18@huawei.com
@Create   : 2019/8/12-10:21
@Python   ：Python 3.7.3
@IDE      : PyCharm
@Version  : 0.0.1

@Change_log
2019/8/12-10:21 created
"""
import re
from collections.abc import Iterable
from xml.etree.ElementTree import Element, ElementTree, fromstring


class ReadOnlyXMLParserWithEncoding:
    def __init__(self, file_path: str, encoding: str = 'utf-8'):
        """
        read only xml parser for read from < gbk > or other encoding method
        :param file_path: the target xml file read from
        :param encoding: the encoding method of input xml file, may write on the xml head
            => <?xml version="1.0" encoding="GBK"?> or not, default encoding is < UTF-8 >

        :exception FileNotFoundError, < LookupError: unknown encoding: GB++K >, <ValueError: UnicodeDecodeError>
        """
        self.__tree = ''
        self.__root = ''
        self.__find_prefix = ''

        with open(file_path, 'r', encoding=encoding) as f:
            self.__tree = ElementTree(element=fromstring(f.read()))
            self.__root = self.__tree.getroot()
            self.__find_prefix = re.match(r'{.*}', self.__root.tag).group(0)

    def get_tree(self) -> ElementTree:
        return self.__tree

    def get_root(self) -> Element:
        return self.__root

    def get_find_prefix(self) -> str:
        return self.__find_prefix


class TPSXMLParser(ReadOnlyXMLParserWithEncoding):
    def __init__(self, file_path: str, encoding: str = 'GBK'):
        """
        specially for TPS xml parse => default encoding in < GBK >
        what is most important is the < self.__all_measInfo_dict > contains all inner < measInfo > data
        :param file_path: the xml file path read file from
        :param encoding: encoding method, default is < GBK >
        """
        super().__init__(file_path, encoding)
        self.__prefix = self.get_find_prefix()
        self.__root = self.get_root()

        self.__xml_basic_info = {
            'fileFormatVersion': '',
            'vendorName': '',
            'fileSender': '',
            'beginTime': '',
            'endTime': '',
            'userLabel': ''
        }
        self.__all_measInfo_list = []

        # trigger for xml parser basic info
        self.__fill_basic_info()
        # trigger for xml parser data info
        self.__fill_all_measInfo()

    def get_basic_info(self) -> dict:
        return self.__xml_basic_info

    def get_all_measInfo(self) -> Iterable:
        yield from self.__all_measInfo_list

    def __fill_basic_info(self):
        """
        fill basic information of TPS xml file, put it into self.__xml_basic_info
        including:
            namespace query prefix
            xml root node
            tps xml => < fileSender > in < fileHeader >
            tps xml recode < beginTime > < endTime >
            tps measInfo of < userLabel > in < managedElement >
        :return:
        """
        prefix = self.__prefix
        root = self.__root

        fileHeader = root.find(prefix + 'fileHeader')
        # fileHeader attribs => < fileFormatVersion > and < vendorName >
        self.__xml_basic_info['fileFormatVersion'] = fileHeader.attrib.get('fileFormatVersion')
        self.__xml_basic_info['vendorName'] = fileHeader.attrib.get('vendorName')
        # fileHeader sub nodes => < fileSender > and < measCollec >
        fileHeader_file_sender_type = fileHeader.find(prefix + 'fileSender')
        self.__xml_basic_info['fileSender'] = fileHeader_file_sender_type.attrib.get('elementType')
        fileHeader_measCollec = fileHeader.find(prefix + 'measCollec')
        self.__xml_basic_info['beginTime'] = fileHeader_measCollec.attrib.get('beginTime')

        # file data info < measData > sub node => < managedElement >
        managedElement = root.find(prefix + 'measData').find(prefix + 'managedElement')
        self.__xml_basic_info['userLabel'] = managedElement.attrib.get('userLabel')

        # fileFooter sub node => < measCollec >
        fileFooter_measCollec = root.find(prefix + 'fileFooter').find(prefix + 'measCollec')
        self.__xml_basic_info['endTime'] = fileFooter_measCollec.attrib.get('endTime')

    def __fill_all_measInfo(self):
        """
        fill all measurement data of TPS xml file => many data in < measInfo > node => put it into self.__all_measInfo_list
        for every measurement data => including
            measInfoId: single
            duration: single
            measTypes: muti
            measValue: muti
        :return:
        """
        prefix = self.__prefix
        root = self.__root
        all_measInfo = root.find(prefix + 'measData').findall(prefix + 'measInfo')

        for single_measInfo in all_measInfo:
            # append first info key => the measInfo Id, such as => <measInfo measInfoId="1526726781">
            measInfo_dict = {
                'measInfoId': single_measInfo.attrib.get('measInfoId') or -1,
                'duration': single_measInfo.find(prefix + 'granPeriod').attrib.get('duration'),
                'measTypes': single_measInfo.find(prefix + 'measTypes').text.split(),
                'measValue_list': []
            }

            measValue_list = []
            all_measValue = single_measInfo.findall(prefix + 'measValue')
            for single_measValue in all_measValue:
                single_measValue_dict = {'measObjLdn': None, 'measResults': None, 'suspect': None}
                single_measValue_dict['measObjLdn'] = single_measValue.attrib.get('measObjLdn')
                single_measValue_dict['measResults'] = single_measValue.find(prefix + 'measResults').text.split()
                single_measValue_dict['suspect'] = single_measValue.find(prefix + 'suspect').text

                measValue_list.append(single_measValue_dict)
            measInfo_dict['measValue_list'] = measValue_list

            self.__all_measInfo_list.append(measInfo_dict)


if __name__ == '__main__':
    from TrafficPredictService.util.running_measure import get_obj_size_bytes, log_run_time_second_print

    @log_run_time_second_print
    def parser_test() -> TPSXMLParser:
        parser = TPSXMLParser('A20190605.0000+0800-0015+0800_98.16.15.253.xml', 'GBK')
        basic_info = parser.get_basic_info()
        all_measInfo = parser.get_all_measInfo()
        return parser

    print(get_obj_size_bytes(parser_test()) / 1000000, 'MB')



