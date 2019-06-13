from multiprocessing.pool import ThreadPool

class Errors:
    codeError = 0
    proxyError = 1

class Worker():
    def __init__(self,workerId,work,codes,proxies):
        self.workerId = workerId
        self.work = work
        self.codes = codes
        self.proxies = proxies
        self.rotating = False

    def proxiesRotation(self,rot):
        self.rotating = rot

    def getResult(self):
        results = []

        code = self.getCode()
        proxy = self.getProxy()
        
        while code != None and proxy != None:
            resp = self.work(code,proxy)    

            if "success" not in resp:
                print("Module not configured properly")
                return results

            if resp["success"]:
                results += resp["result"]

            elif:
                if resp["error"] == Errors.codeError:
                    pass
                
                elif resp["error"] == Errors.proxyError:
                    pass

            
            
    def codesRemaining(self):
        return len(codes) > 0

    def proxiesRemaining(self):
        return len(codes) > 0
    
    def getCode(self):
        if self.codesRemaining():
            code = self.codes.pop()
            return code
        return None

    def getProxy(self):
        if self.proxiesRemaining():
            proxy = self.proxies.pop()
            if self.rotating:
                self.proxies = [proxy] + self.proxies
            return proxy
        return None
        
        

class Checker():
    def __init__(self,module,threadCount=100):
        self.module = module
        self.codes = None
        self.proxies = None

    def loadCodes(self,codes):
        self.codes = codes

    def loadProxies(self,proxies):
        self.proxies = proxies

    def check(self):
        pool = ThreadPool(threadCount)
        workers = [ Worker(i,module) for i in range(threadCount)]
        result = pool.map( lambda _: Wroker.getResult() , range(threadCount) )
        pool.close()

        return result
        


def main():
    pass

if __name__ == "__main__":
    main()
