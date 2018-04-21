import numpy as np
# library: helps with enumerating files into a directory
import os

class database:

    def __init__(self, name):
        self.name = name
        self.data = []
        self.format = None

    def addField(self, fieldName):
        if self.format is None:
            self.format = (fieldName,)
        else:
            self.format = self.format + (fieldName,)

    def addEntry(self, value):
        if self.format is not None:
            entry = []
            for field in self.format:
                entry.append(value[field])
            self.data.append(entry)

    def save(self):
        dataDir = os.path.join(os.getcwd(), "data" )
        try:
            os.mkdir(dataDir)
        except:
            pass
        np.save(os.path.join(dataDir, self.name), np.array(self.data))

    def load(self):
        dataDir = os.path.join(os.getcwd(), "data" )
        try:
            self.data = np.load(os.path.join(dataDir, self.name + ".npy"), self.data).tolist()
        except:
            pass
#path.join  -  functions that formats path names according to operating system symantics
# get working directory - this returns the directory that your program is running under
#os.getcwd


















#  P I C K L E   R I C K  <o/       P I C K L E   R I C K  <o/         P I C K L E   R I C K  <o/
"""
                    ___________________________
                   /                           \
                  /                             \
                 |                              |               [---------------]
                 |       ---        ---         |               [           |---]
                 |      |   |      |   |        |                /-----------
                 |      | |-|      | |-|        |               /
                 |       -|-        -|-         |              /
                 |             \                |-------------/
                 |         \__   \ __           |
                 |             \_    -\         |
                 |              \_____|         |
                 |                              |
                 |      ----------------        |
                 (                              )
                  (                            )
                   \                          /
                    \                        /
                     (______________________)
"""
