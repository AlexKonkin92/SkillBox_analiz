import yaml
to_yaml = {'bot_token': '1116731183:AAEXzjndl3V3RX-AIkeTd8wT5D3CINq_F2k'}

with open('tg_bot_token.yaml', 'w') as f:
    yaml.dump(to_yaml, f)
    
with open('tg_bot_token.yaml') as f:
    print(f.read())



