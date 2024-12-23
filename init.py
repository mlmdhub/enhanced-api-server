import utils.project
import json
with open(utils.project.root()+'/config/main.json', 'r') as f:
    config = json.load(f)
with open(utils.project.root()+'/config/main.json', 'w') as f:
    config['project_name']=utils.project.name()
    config['project_root'] = utils.project.root()
    utils.project.init()
    config['project_init'] = True

    json.dump(config, f)
utils.project.init()