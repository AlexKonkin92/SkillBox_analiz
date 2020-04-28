import pandas as pd
import numpy as np
genres = ['Drama', 'Action', 'Thriller']
crm = pd.read_csv('[sharewood.band] crm_stats.tsv',delimiter='\t',encoding='utf-8')
direct = pd.read_csv('[sharewood.band] direct_stats.tsv',delimiter='\t',encoding='utf-8')
joined = direct.merge(crm, on=['date','campaign'], how='left')
joined['zak'] = joined['cost']//joined['orders']
joined[(joined['date'] == '2018-01-01') & (joined['campaign'] == 'landings_promo')]



