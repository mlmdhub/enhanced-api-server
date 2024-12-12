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

    def static(self):
        return {"url": self.url, **self.kwargs}


class Response(req.Response):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])





class RequestManager(concurrent.futures.ThreadPoolExecutor):
    def __init__(self):
        super().__init__()
        self.poll_index = 0
        self.logger = utils.project.get_logger('RequestManager')

    @staticmethod
    def request(url, **kwargs):
        if kwargs['callback'] == None:
            res = req.request(url=url, **kwargs)
        else:
            callback,args = kwargs['callback']
            del kwargs['callback']
            res = req.request(url=url, **kwargs)
            callback(res, args)
        return res

    def loop(self, requesting, request_static, **kwargs):
        futures = [self.submit(requesting, request, **kwargs) for request in request_static]
        return [future.result() for future in concurrent.futures.as_completed(futures)]

    def poll(self, requests: list[Request], quited):
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
