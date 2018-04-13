# coding:utf8
from firefly.server.globalobject import GlobalObject, remoteserviceHandle
from app.util.common import func

class remoteserviceHandleNoLog:
    def __init__(self,remotename):
          self.remotename = remotename
    def __call__(self,target):
        GlobalObject().remote[self.remotename]._reference._service.mapTarget(target)

@remoteserviceHandle('auth')
def push_object_auth(target_key, data, send_list):
    GlobalObject().netfactory.pushObject(target_key, data, send_list)


@remoteserviceHandle('gate')
def push_object_gate(target_key, data, send_list):
    GlobalObject().netfactory.pushObject(target_key, data, send_list)


@remoteserviceHandle('gate')
def push_object_gate_close_conn(dynamic_id, fromv):
	func.log_info("push_object_gate_close_conn dynamic_id: {} fromv {}".format( dynamic_id, fromv ))
	GlobalObject().netfactory.loseConnection(dynamic_id)
    #GlobalObject().netfactory.pushObject(target_key, data, send_list)



