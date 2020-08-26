class UtilYaml:
    @staticmethod
    def find(obj,path):
        path = path.split('.')
        #print(path)
        i=0
        l = len(path)
        while obj and i < l:
            if path[i] not in obj :
                obj = ''
                break
            obj = obj[path[i]]
            i+=1
        return obj
