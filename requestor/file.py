import utils.project

class ResponseSaver:
    def __init__(self, response, name):
        self.response = response
        self.file_name = name
        self.logger = utils.project.get_logger('ResponseSaver')
        self.save()
        self.select()

    def judge_response_type(self):
        if self.file_name.split('.')[-1] != '':
            return ''
        elif self.response.headers['Content-Type'] == 'text/html':
            return '.html'
        elif self.response.headers['Content-Type'] == 'application/json':
            return '.json'
        elif self.response.headers['Content-Type'] == 'text/css':
            return '.css'
        elif self.response.headers['Content-Type'] == 'text/javascript':
            return '.js'
        elif self.response.headers['Content-Type'] == 'text/plain':
            return '.txt'
        else:
            return '.txt'

    def save(self):
        with open(utils.project.root() + '/data/packages/' + self.file_name + self.judge_response_type(), 'wb') as f:
            f.write(self.response.content)
        self.logger.info('Response saved to ' + utils.project.root() + '/data/packages/' + self.file_name + self.judge_response_type())

    def select(self):
        pass
