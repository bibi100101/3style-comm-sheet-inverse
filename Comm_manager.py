class Comm:  
    
    def __init__(self, comm):
        self.comm = comm
        if '/' in comm:
            
            try:
                self.setup = comm[0:comm.index(':')]
            except:
                self.setup = ""
            
            self.A = comm[comm.index('[')+1:comm.index('/')]
            self.B = comm[comm.index('/')+1:comm.index(']')]
            self.comm_type = "slash"

        elif '[' in comm:
            
            try:
                self.setup = comm[0:comm.index(':')]
            except:
                self.setup = ""
            
            self.A = comm[comm.index('[')+1:comm.index(',')]
            self.B = comm[comm.index(',')+1:comm.index(']')]
            self.comm_type = "normal"
        
        else:    
            self.comm_type = "alg"
            self.A = ""
            self.B = ""
            self.setup = ""

    def Get_Inverse(self):
        #print(self.comm_type, self.setup, self.A, self.B)
        if self.comm_type == "slash": 
            if len(self.A) == 2:
                self.A = self.A[0]
                
                if len(self.setup) == 0:
                    return (f"[{self.A}/{self.B}]")
                else:
                    return (f"{self.setup}:[{self.A}/{self.B}]")
            else:
                if len(self.setup) == 0:
                    return (f"[{self.A}'/{self.B}]")
                else:
                    return (f"{self.setup}:[{self.A}'/{self.B}]")
        elif self.comm_type == "normal":
            if len(self.setup) == 0:
                return (f"[{self.B},{self.A}]")
            else:
                return (f"{self.setup}:[{self.B},{self.A}]")
        elif self.comm_type == "alg":
            return ""
