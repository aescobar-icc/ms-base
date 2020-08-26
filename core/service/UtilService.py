import os

from core.log.UtilLog import UtilLog
from core.yaml.UtilYaml import UtilYaml
from core.sys.SysEnv import SysEnv


class UtilService:
    @staticmethod
    def getClientAddress(request):
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            remote_addr=request.environ['REMOTE_ADDR']
        else:
            remote_addr=request.environ['HTTP_X_FORWARDED_FOR']
        return remote_addr

    @staticmethod
    def getServiceInfo(request):
        service_info = '  NODE_NAME: %s\n  POD_NAME: %s\n  POD_NAMESPACE: %s\n  POD_IP: %s\n  POD_SERVICE_ACCOUNT: %s'%(
                SysEnv.get('MY_NODE_NAME','Not Defined !!!'),
                SysEnv.get('MY_POD_NAME','Not Defined !!!'),
                SysEnv.get('MY_POD_NAMESPACE','Not Defined !!!'),
                SysEnv.get('MY_POD_IP','Not Defined !!!'),
                SysEnv.get('MY_POD_SERVICE_ACCOUNT','Not Defined !!!'))
        if request:
            service_info = 'SERVICE:\n%s\n\nCLIENT: %s\n\nURL: %s\nHEADERS:\n%s\nDATA:\n%s\n'%(
                    service_info,
                    UtilService.getClientAddress(request),
                    request.url,
                    str(request.headers),
                    str(request.data))

        UtilLog.debug('%s'%service_info)
        return service_info