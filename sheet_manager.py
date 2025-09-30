import Comm_manager

def clean_data(sheet, sheet_size):
    del sheet[0]
    for row in sheet:
        del row[0]
    del sheet[sheet_size:len(sheet) + 1]
    return sheet

def generate_inverses(sheet, sheet_size):
    sheet = clean_data(sheet, sheet_size)
    for j in range(0, sheet_size):
        for i in range(0, sheet_size):
            if i == j:
                continue
            if not sheet[i][j]:
                continue
            comm = Comm_manager.Comm(sheet[i][j])
            if comm.comm_type == "alg":
                continue
            else:
                if not sheet[j][i]:
                    sheet[j][i] = comm.Get_Inverse()
                else:
                    del comm
                    continue
            del comm
    return sheet