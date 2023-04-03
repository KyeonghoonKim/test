import requests
import argparse
import os
def send_yesterday_log(path:str):
    # read log
    url = "http://adddi.kr/adddi_model4/log_file_upload"
    url_header = { 'key' : 'afsdf2asdfdsa7689oijafd#@safsd67afsdnkasdfmklafdsoaf$#@#sdmlkafds6afdsmkl453543mkl534mlkasfdlkafdsasdf#$32'}
    yesterday_log_file = open(path,'rb')
    upload_files = {'_file' : yesterday_log_file}
    try :
        response = requests.post(url,headers=url_header,files=upload_files)
        if response.status_code == 200 and response.text == "1":
            print('success')
    except : 
        print("fail")
    finally :
        os.remove(path)

def send_yesterday_systemlog(path:str):

    url = "http://adddi.kr/adddi_model4/log_file_upload"
    url_header = { 'key' : 'afsdf2asdfdsa7689oijafd#@safsd67afsdnkasdfmklafdsoaf$#@#sdmlkafds6afdsmkl453543mkl534mlkasfdlkafdsasdf#$32'}

    systemlog_content = os.popen('journalctl --since="1 day ago"').read()
    if len(systemlog_content) == 0 :
        print("no system log")
        return
    yesterday_systemlog = open(path,'w')
    yesterday_systemlog.write(systemlog_content)
    yesterday_systemlog.close()

    # read log
    yesterday_log_file = open(path,'rb')
    upload_files = {'_file' : yesterday_log_file}
    try :
        response = requests.post(url,headers=url_header,files=upload_files)
        if response.status_code == 200 and response.text == '1':
            print('success')
    except :
        print("error")
    finally :
        yesterday_log_file.close()
        os.remove(path)
    return

def download_latest_app():
    return

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type = str, default= "/home/oficeaddd/ADDDI_LOGS/9003_TESTING_2022_12_28.log")
    parser.add_argument("--mode", type = str, default= "send_yesterday")
    
    args = parser.parse_args()
    if args.mode == "send_yesterday" :
        send_yesterday_log(args.path)
    elif args.mode == "send_yesterday_systemlog" :
        send_yesterday_systemlog(args.path)
    