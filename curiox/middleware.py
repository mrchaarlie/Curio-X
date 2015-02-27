import time
import simplejson as json

from django.core.exceptions import ObjectDoesNotExist
import logging

from game.models import UserLog

logger = logging.getLogger(__name__)

class LogAllMiddleware(object):
    def process_request(self,request):
        try:
            if not request.user.is_authenticated():
                logger.debug('User %s not authenticated' % request.user.username)
                return None
        except AttributeError:
            return None
        
        # Skip favicon requests
        if request.path =="/favicon.ico":
            return None
        
        new_log = UserLog(
            session = request.session.session_key,
            
            user = request.user.username,
            path  = request.path,
            query = request.META["QUERY_STRING"],
            variables = json.dumps(request.REQUEST.__dict__),
            method = request.method,
            secure = request.is_secure(),
            #ajax = request.is_ajax(),
            meta = request.META.__str__(), #need meta for unique entry
            #address = request.META["REMOTE_ADDR"],
            )
        
        logger.debug('Save user log for user %s at %s for path %s', new_log.user, new_log.timestamp, new_log.path)
        new_log.save()
        
        return None
    
    ''' 
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            if not request.user.is_authenticated():
                return None
        except AttributeError:
            return None
        
        try:
            log = UserLog.objects.get(
                session = request.session.session_key,
                user = request.user,
                path  = request.path,
                method = request.method,
                secure = request.is_secure(),
                #ajax = request.is_ajax(),
                #meta = request.META.__str__()
                )
            #log.view_func = view_func.func_name #TODO: members not in class
            #log.view_docstr = view_func.func_doc
            log.view_args = json.dumps(view_kwargs)
            
            log.save()
        except  ObjectDoesNotExist:
            pass
        
        return None
    '''

    def process_response(self, request, response):
        try:
            if not request.user.is_authenticated():
                return response
        except AttributeError:
            return response
        
        # Skip favicon requests
        if request.path =="/favicon.ico":
            return response
        
        try:
            log = UserLog.objects.get(
                session = request.session.session_key,
                user = request.user,
                path  = request.path,
                method = request.method,
                secure = request.is_secure(),
                #ajax = request.is_ajax(),
                meta = request.META.__str__()
                )
            
            log.resp_code= response.status_code
            log.save()
        except  ObjectDoesNotExist:
            pass
        
        return response
