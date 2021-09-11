import json

# requires absolute path of the server
root_directory = '/server'

if __name__ == '__main__':
    env = []
    __dir = root_directory + '/scripts'
    try:
        with open(__dir + '/env.json') as file:
            env = json.load(file)
    except:
        pass
    for p in env:
        try:
            __dir = root_directory + '/plugins'
            pluginName = "/" + p['name']
            __dir = __dir + pluginName

            for f in p['files']:
                filename = __dir + "/" + f['name'] + \
                    "_template" + '.' + f['extension']

                with open(filename, 'r') as file:
                    data = file.read()
                    for v in f['values'].keys():
                        split = data.split("${" + v + "}")
                        data = f['values'][v].join(split)

                    file.close()
                filename = __dir + "/" + f['name'] + '.' + f['extension']

                with open(filename, 'w') as file:
                    file.write(data)
                    file.close()
        except Exception as e:
            print(e)
            pass
