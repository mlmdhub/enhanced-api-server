import concurrent.futures
import logging

import requests as req

import utils.project


class Request:
    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs

        assert self.kwargs['method'].upper() in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE']

    def __str__(self):
        return f"Request(url={self.url}, kwargs={self.kwargs})"

    def __repr__(self):
        return f"Request(url={self.url}, kwargs={self.kwargs})"

    @staticmethod
    def request(url, **kwargs):
        if kwargs.get("callback",None) == None:
            res = req.request(url=url, **kwargs)
        else:
            callback, args = kwargs['callback']
            del kwargs['callback']
            res = req.request(url=url, **kwargs)
            callback(res, args)
        return res

    def static(self):
        return {"url": self.url, **self.kwargs}

    def fetch(self):
        return self.request(self.url, **self.kwargs)


class Response(req.Response):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])


class RequestManager(concurrent.futures.ThreadPoolExecutor):
    def __init__(self):
        super().__init__()
        self.poll_index = 0
        self.request_id = 0
        self.logger = utils.project.get_logger('RequestManager')


    def request(self,request:Request):
        if request.kwargs.get("callback",None)== None:
            res=request.fetch()
            self.request_id+=1
            self.logger.info(f"Normal request {request.url}, response: {res.status_code}, id: {self.request_id}")
        else:
            callback, args = request.kwargs['callback']
            del request.kwargs['callback']
            res=request.fetch()
            self.request_id += 1
            self.logger.info(f"Normal request {request.url}, response: {res.status_code}, id: {self.request_id}")
            callback(res, args)
        return res

    def loop(self, request_fn, request_static, **kwargs):
        self.logger.info(f"Looping {len(request_static)} requests")
        futures = [self.submit(request_fn, request, **kwargs) for request in request_static]
        return [future.result() for future in concurrent.futures.as_completed(futures)]

    def poll(self, requests: list[Request], quited):
        """
        Make requests one by one, until fn quited returns True (fn quited first arg is response)
        :param requests: list[Request]:
        :param quited:
        :return: the last response
        """
        try:
            while True:
                response = self.request(requests[self.poll_index].url, **requests[self.poll_index].kwargs)
                if quited(response):
                    self.logger.info(
                        f"Used {self.poll_index} to request {requests[self.poll_index].url}, response: {response.status_code}")
                    break
                else:
                    self.logger.info(
                        f"Used poll index {self.poll_index} to request {requests[self.poll_index].url}, response: {response.status_code}, Changing poll index from {self.poll_index} to {self.poll_index + 1}")
                    self.poll_index = (self.poll_index + 1) % len(requests)
            return response
        except Exception as e:
            self.logger.error(e.with_traceback)
            return Response(status_code=600)

    def continues(self, request: Request, reverse, quited, **kwargs):
        """
        Make the request, and use fn reverse to req the next request, until fn quited returns True (fn reverse,fn quited first arg is response)
        :param request: Request:
        :param quited:
        :param kwargs:
        :return: all the responses
        """

        try:
            continues_times = 0
            while True:
                response = self.request(request.url, **request.kwargs)
                request = reverse(response)
                continues_times += 1
                self.logger.info(
                    "Function continues, times: " + str(continues_times) + ", response: " + str(response.status_code))
                if quited(response):
                    self.logger.info("continues function quited")
                    break
        except Exception as e:
            self.logger.error(e.with_traceback)
            return Response(status_code=600)



