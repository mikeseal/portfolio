import configparser

class Config_Reader():
    _filename = "config.ini"
    _section = "DEFAULT"
    
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self._filename);
        
#    def read(self, filename, section, option):
#        self.filename = filename
#        self.section = section

    # read using default section
#    def read(self, filename, option):
#        self.filename = filename

#    def read(self, section, option):
#        self.section = section

    def read(self, option):
        return self.cfg[self._section][option]
