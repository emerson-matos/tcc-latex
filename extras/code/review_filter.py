df['com_texto'] = df['text'].str.len() > 2
df['nao_vazio'] = df['text'].notna()
df['traduzido'] = df['text'].str.contains('Tradução do Google', na=False)
df['depois_2017'] = df['ano_avaliacao'] > 2017
