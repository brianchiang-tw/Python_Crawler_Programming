import requests
from datetime import time
import csv
import matplotlib.pyplot as plt
import pandas as pd
#---------------------------------------------------

class VixTick():

    def __init__(self, time_string: str, vix_string: str):

        hr, mn, sec = map( int, (time_string[:2], time_string[2:4], time_string[4:]) )
        self._time = time(hour=hr, minute=mn, second=sec)
        self._vix_value = float(vix_string)

    
    def getVixTick(self):
        return (self._time, self._vix_value)

    def __str__(self):
        return f'{str(self._time)} at {self._vix_value}'

    def to_csv_data_row(self):
        return [str(self._time), str(self._vix_value)]

#---------------------------------------------------

cookies = {
    'BIGipServerPOOL_MIS_TCP_80': '2551582892.20480.0000',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Sec-GPC': '1',
    'Origin': 'https://mis.taifex.com.tw',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mis.taifex.com.tw/futures/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = '{"SymbolID":"TAIWANVIX"}'

# --------------------------------------------------------

csv_file_name = 'vix-data.csv'

# --------------------------------------------------------


def time_series_to_vixTick(raw_time_series, vix_ticks ):

    # convert from time-vix time series to VixTick
    for single_vix_tick in raw_time_series:

        # [0] is timestamp t
        # [4] is vix value at timestamp t
        time_sting, vix_string = single_vix_tick[0], single_vix_tick[4]
        one_vix_tick = VixTick(time_sting, vix_string)
        vix_ticks.append( one_vix_tick ) 

    return 

# --------------------------------------------------------

def output_to_csv(vix_ticks, file_name):

    # output VixTick to Excel CSV File
    with open(file_name, 'w') as f:
        
        csvWriter = csv.writer(f, delimiter=',', lineterminator='\n')

        csvHeader = ['Time', 'Vix']
        csvWriter.writerow( csvHeader )

        for currnet_data in vix_ticks:
            csvWriter.writerow( currnet_data.to_csv_data_row() )

    return

# --------------------------------------------------------

def get_raw_timeseries(response):

    # Get JSON data from server
    json_obj = response.json()

    # Extract raw data of time-vix time series form JSON data
    raw_vix_time_series = json_obj['RtData']['Ticks']

    return raw_vix_time_series

# --------------------------------------------------------

def draw_graph(filename):

    try:
        vix_series = pd.read_csv(filename, header=0, index_col=0, parse_dates=True, squeeze=True)
        open_position = vix_series[0]
        
        vix_series.plot()

        plt.title('TAIEX option VIX')

        # finetune y axis window
        plt.ylim([open_position*0.85, open_position*1.15])
        plt.show()
    
    except Exception:
        print( "Error during readfile or drawing graph")

# --------------------------------------------------------

def get_vix_data_from_server():

    response = None

    try:
        response = requests.post('https://mis.taifex.com.tw/futures/api/getChartDataTick', headers=headers, cookies=cookies, data=data)

    except Exception as err:
        print("Error during HTTP API connection")
        print('\n', err)



    if response.status_code == requests.codes.ok:
        print('Connect successful')

        # Extract raw data of time-vix time series form response
        raw_vix_time_series = get_raw_timeseries(response)

        # a buffer to store VixTick object
        vix_ticks = []

        time_series_to_vixTick(raw_vix_time_series, vix_ticks)

        output_to_csv(vix_ticks, file_name=csv_file_name)

        print("vix-data.csv is generated! : )")

    else:
        print(f'status code [Error code]: {response.status_code}')
        print('Fail to get response from Taifex sever')

    return

# --------------------------------------------------------
def main():

    msg_list = ["Enter action number", "1. Get vix data from Server", "2. Draw from local csv file","> "]
    msg = '\n'.join(msg_list)

    action_ID = int( input(msg) )

    if action_ID == 1:
        get_vix_data_from_server()

    elif action_ID == 2:
        draw_graph(csv_file_name)

    else:
        print('Wrong action ID')
    


if __name__ == '__main__':
    main()