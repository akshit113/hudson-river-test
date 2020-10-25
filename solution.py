from pandas import DataFrame

market_trades = [
    # time,id,side,size,sym,price
    '10:00:00.0143,1178761,T,49,PLCE,56.70000000',
    '10:00:00.0279,1178905,T,40,MINI,37.17000000',
    '10:00:00.0565,1179340,B,14,LRCX,78.21000000',
    '10:00:00.1468,1180355,T,100,MDT,72.34000000',
    '10:00:00.1656,1180537,T,100,MDT,72.35000000',
    '10:00:00.4150,1182528,S,100,OXY,73.83000000',
    '10:00:00.5067,1182965,B,100,OXY,73.81000000',
    '10:00:00.6127,1183363,S,100,OXY,73.81000000',
    '10:00:00.7725,1183850,B,100,NVS,91.53000000',
    '10:00:01.0178,1184348,S,2,NEE,100.42000000',
    '10:00:01.2194,1184911,B,100,NXPI,71.81000000',
    '10:00:01.8146,1185705,B,50,NEM,17.92000000',
    '10:00:02.1138,1186391,T,50,MXIM,30.90000000',
    '10:00:02.1664,1186661,B,100,NXPI,71.74000000',
    '10:00:02.4444,1186902,B,100,AMZN,301.87000000',
    '10:00:05.0599,1187952,B,100,UVXY,29.89000000',
    '10:00:06.5457,1189109,S,100,OXY,73.84000000',
    '10:00:07.6006,1189708,T,100,MCD,87.98000000',
    '10:00:08.3844,1190214,S,100,MUR,44.78000000',
]
hrt_list = []
mkt_list = []
missing_trades = []
hrt_trades = [
    # sym,price,size,side,market,time,id
    'PLCE,56.70000000,49,Short,NASDAQ,10:00:00.014383,1178761',
    'MINI,37.17000000,40,Short,NASDAQ,10:00:00.027954,1178905',
    'LRCX,78.21000000,14,Buy,NASDAQ,10:00:00.056529,1179340',
    'MDT,72.34000000,100,Short,NASDAQ,10:00:00.146882,1180355',
    'MDT,72.35000000,100,Short,NASDAQ,10:00:00.165655,1180537',
    'OXY,73.81000000,100,Buy,NASDAQ,10:00:00.506703,1182965',
    'OXY,73.81000000,100,Sell,NASDAQ,10:00:00.612718,1183363',
    'NVS,91.53000000,100,Buy,NASDAQ,10:00:00.772590,1183850',
    'NEE,100.42000000,2,Sell,NASDAQ,10:00:01.017875,1184348',
    'NXPI,71.81000000,100,Buy,NASDAQ,10:00:01.219456,1184911',
    'NEM,18.92000000,50,Buy,NASDAQ,10:00:01.814617,1185705',
    'MXIM,30.90000000,50,Short,NASDAQ,10:00:02.113871,1186391',
    'NXPI,71.74000000,100,Buy,NASDAQ,10:00:02.166493,1186661',
    'AAPL,301.87000000,100,Buy,NASDAQ,10:00:02.444408,1186902',
    'UVXY,29.89000000,100,Buy,NASDAQ,10:00:05.059948,1187952',
    'OXY,73.84000000,100,Sell,NASDAQ,10:00:06.545747,1189109',
    'MCD,87.98000000,100,Short,NASDAQ,10:00:07.600633,1189708',
    'MUR,44.78000000,100,Sell,NASDAQ,10:00:08.384442,1190214',

]


def solution(hrt_trades, market_trades):
    def get_size(x):

        if x == 'Short':
            val = 'T'
        elif x == 'Sell':
            val = 'S'
        elif x == 'Buy':
            val = 'B'
        else:
            val = 'No Value'
        return val

    for row in market_trades:
        ls = row.split(',')
        mkt_list.append(ls)

    for row in hrt_trades:
        ls = row.split(',')
        side = get_size(ls[3])
        new_list = [ls[5][0:-2], ls[6], side, ls[2], ls[0], ls[1]]
        hrt_list.append(new_list)

    for idx, row in enumerate(mkt_list):
        if row not in hrt_list:
            missing_trades.append(market_trades[idx])

    for idx, row in enumerate(hrt_list):
        if row not in mkt_list:
            missing_trades.append(hrt_trades[idx])

    return missing_trades


if __name__ == '__main__':
    missing_trades = solution(hrt_trades, market_trades)
    print("\n".join(missing_trades))
