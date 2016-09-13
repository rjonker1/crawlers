class IssuerViewModel(object):
    def __init__(self, url, name, inferred):
        self._url = url
        self._name = name
        self._inferred = inferred
    
    @property
    def Url(self):
        return self._url
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Inferred(self):
        return self._inferred