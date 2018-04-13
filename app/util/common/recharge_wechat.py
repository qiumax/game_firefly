# coding:utf8

import hashlib
import json
import requests
# import xml2json
import xmltodict
from xml.etree import ElementTree
from app.util.common import func
from app.util.defines import constant, content


class WechatPay(object):
    def __init__(self):
        self._params = dict()
        self._url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
        self._error = None
        self.order_id_ = ''

    def init(self, **kwargs):
        func.log_info('[game] WechatPay init kwargs: {}'.format(kwargs))
        self.order_id_ = str(kwargs['order_id'])
        self._params = {
            'appid': constant.WECHAT_APPID,
            'mch_id': constant.WECHAT_MCH_ID,
            'nonce_str': kwargs['nonce_str'],                   # 随机字符串，不长于32位
            'body': constant.WECHAT_BODY,                       # 商品或支付单简要描述
            'attach': kwargs['attach'],                         # 商家附加数据, 127位
            'out_trade_no': str(kwargs['order_id']),            # 唯一商户订单号, 32位, 字母+数字均可
            'total_fee': str(int(kwargs['total_fee'])),         # 订单总金额，单位为分
            'spbill_create_ip': kwargs['spbill_create_ip'],     # 用户端实际ip
            'trade_type': 'APP',                                # 支付类型
            'notify_url': constant.WECHAT_NOTIFY_URL,           # 接收微信支付异步通知回调地址
            'limit_pay': 'no_credit',                            # 不能使用信用卡支付
        }

    @property
    def order_id(self):
        return self.order_id_


    @staticmethod
    def key_value_url(value):
        key_az = sorted(value.keys())
        pair_array = []
        for k in key_az:
            v = value.get(k, '').strip()
            v = v.encode('utf8')
            k = k.encode('utf8')
            pair_array.append('%s=%s' % (k, v))

        tmp = '&'.join(pair_array)
        return tmp

    def get_sign(self, params):
        kvurl = self.key_value_url(params)
        s = kvurl + '&key=' + constant.WECHAT_APIKEY
        sign = (hashlib.md5(s).hexdigest()).upper()
        params['sign'] = sign

    def get_req_xml(self):
        self.get_sign(self._params)
        xml = "<xml>"
        for k, v in self._params.items():
            v = v.encode('utf8')
            k = k.encode('utf8')
            xml += '<' + k + '>' + v + '</' + k + '>'
        xml += "</xml>"
        return xml

    def calc_prepay_id(self):
        xml = self.get_req_xml()
        headers = {'Content-Type': 'application/xml'}
        r = requests.post(self._url, data=xml, headers=headers)
        func.log_info('[game] wechatpay ret: {} url: {} xml: {}'.format( r, self._url, xml ) )
        re_xml = ElementTree.fromstring(r.text.encode('utf8'))
        xml_status = re_xml.getiterator('result_code')[0].text
        func.log_info('[game] WechatPay query_wechat_prepay_id xml_status: {}'.format(xml_status))
        if xml_status != 'SUCCESS':
            self._error = content.RECHARGE_WECHAT_CONNECT_FAILED
            return
        prepay_id = re_xml.getiterator('prepay_id')[0].text
        func.log_info('[game] WechatPay prepay_id: {}'.format(prepay_id))
        self._params['prepay_id'] = prepay_id
        self._params['package'] = 'Sign=WXPay'
        self._params['timestamp'] = str(func.time_get())

    def get_prepay_id(self):
        return self._params.get('prepay_id', -1)

    def re_finall(self):
        self.calc_prepay_id()
        if self._error:
            return

        sign_again_params = {
            'appid': self._params['appid'],
            'noncestr': self._params['nonce_str'],
            'package': self._params['package'],
            'partnerid': self._params['mch_id'],
            'timestamp': self._params['timestamp'],
            'prepayid': self._params['prepay_id']
        }
        self.get_sign(sign_again_params)
        self._params['sign'] = sign_again_params['sign']

        # 移除其他不需要返回参数
        for i in self._params.keys():
            if i not in ['appid', 'mch_id', 'nonce_str', 'timestamp', 'sign', 'package', 'prepay_id']:
                self._params.pop(i)
        return self._params


class WechatResponse(WechatPay):

    def __init__(self, xml):
        """
        :param xml: 支付成功回调的XML
        """
        super(WechatResponse, self).__init__()
        self._xml = xml
        self._xml_json = dict(xmltodict.parse(self._xml))['xml']
        self._sign = self._xml_json.get('sign', '')
        self._transaction_id = self._xml_json.get('transaction_id', '')
        self.order_id_ = self._xml_json.get('out_trade_no', '')

    @property
    def transaction_id(self):
        return self._transaction_id


    @property
    def xml_json(self):
        return self._xml_json

    @property
    def attach(self):
        _attach = self._xml_json['attach'].split('/')
        if len(_attach) != 2:
            func.log_error('[gate] wechat_recharge_success attach is unvalid: {}'.format(_attach))
            return None, None
        proxy_id, account_id = int(_attach[0]), int(_attach[1])
        return proxy_id, account_id

    @property
    def money(self):
        return int(self._xml_json['total_fee'])

    def verify(self):
        self._xml_json.pop('sign')
        self.get_sign(self._xml_json)
        func.log_info('[gate] pre_sign: {}'.format(self._sign))
        func.log_info('[gate] cur_sign: {}'.format(self._xml_json['sign']))
        if self._sign != self._xml_json['sign']:
            func.log_error('[gate] WechatResponse xml_sign: {} != sgin: {}'.format(
                    self._xml_json['sign'], self._sign))
            return False
        return True


def generator_unique_order_id(money, account_id, dynamic_id):
    t = func.time_get()
    return '%s%d%d' % ( str(money * 3 + func.random_get(30000, t)), account_id,dynamic_id )






