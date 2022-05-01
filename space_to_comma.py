import csv
import os

FILE_NUM_FLAG = 0
RESULT_PATH = './result_'
DB_LIST = ['ahadb', 'cudb', 'edb', 'nstdb']
USER_PATH = input("[USER] Type Database category (ex aha, cu, esc, nst): ")
print("[INFO] Pre-processing for make clean")

for i in range(len(DB_LIST)):
    user_path_nospace = USER_PATH.replace(" ", "")
    if (user_path_nospace == 'aha'):
        FILE_NUM_FLAG = 0
    elif (user_path_nospace == 'cu'):
        FILE_NUM_FLAG = 1
    elif (user_path_nospace == 'esc'):
        FILE_NUM_FLAG = 2
    elif (user_path_nospace == 'nst'):
        FILE_NUM_FLAG = 3
    else:
        print("[ERRR]\tYour typed ", USER_PATH, " but, system can not found what database it is.")
        print("[ERRR]\tSystem out.")
        exit(1)
print("[INFO] Your typed", USER_PATH, " and system detected same database from list : ", DB_LIST[FILE_NUM_FLAG])
print("[INFO] System continue ... ")

print("[INFO] Creating result direcotory...")
PATH = './' + DB_LIST[FILE_NUM_FLAG] + '/' + '1.0.0/'
for i in range(len(DB_LIST)):
    try:
        if not os.path.exists(RESULT_PATH + DB_LIST[FILE_NUM_FLAG]):
            os.makedirs(RESULT_PATH + DB_LIST[FILE_NUM_FLAG])
    except OSError:
        print("[ERRR] \t\t\t Error with creating direcotry : ", RESULT_PATH + DB_LIST[FILE_NUM_FLAG])
        print("[ERRR] \t\t\t System exit by exit(1)")
        exit(1)

print("[INFO] Read records file from ", PATH)
with open(PATH + 'RECORDS') as f:
    record_lines = f.readlines()

pre_records = []
for x in record_lines:
    pre_records.append(x.strip())

print("[RSLT]\t\t\t Export records ...")
print("\t\t",pre_records)

for i in pre_records:
    in_convert_path = RESULT_PATH + DB_LIST[FILE_NUM_FLAG] + '/rdsamp_' + DB_LIST[FILE_NUM_FLAG] + i + '.csv'
    ou_convert_path = RESULT_PATH + DB_LIST[FILE_NUM_FLAG] + '/final_rdsamp_' + DB_LIST[FILE_NUM_FLAG] + i + '.csv'
    with open(in_convert_path) as fin, open(ou_convert_path, 'w') as fout:
        for line in fin:
            fout.write(" ".join(line.split()).replace('\t', ','))
            fout.write(",")