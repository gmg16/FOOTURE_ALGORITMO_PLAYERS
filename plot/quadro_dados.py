from PIL import Image, ImageDraw, ImageFont
import pandas as pd 


class PlotStatsQuadro:
    muito_mais_media = '#4747ff'
    mais_media = '#22ff55'
    abaixo_media = '#f6ed0d'
    muito_abaixo_media = '#fd3535'

    cor_fundo = '#2b2c2c'
    cor_texto = 'white'

    def df_cor(self, df_analise_posicao, player):
        muito_mais_media = self.muito_mais_media 
        mais_media = self.mais_media 
        abaixo_media = self.abaixo_media 
        muito_abaixo_media = self.muito_abaixo_media 

        df_analise_posicao = df_analise_posicao.fillna(0)

        index_coluna = df_analise_posicao.columns.get_loc('playerStats_minutes_on_field')
        colunas_desejadas = list(df_analise_posicao.columns)[index_coluna:]
        colunas_info = list(df_analise_posicao.columns)[0:index_coluna]

        quartille_df = df_analise_posicao[colunas_desejadas].rank(pct=True).fillna(0)
        quartille_df = df_analise_posicao[colunas_info].join(quartille_df)

        quartille_df = quartille_df[quartille_df['id'] == int(player)].reset_index(drop=True)

        df_jogador_plot = df_analise_posicao[df_analise_posicao['id'] == player].reset_index(drop=True)

        dic_cores = {}
        for coluna in colunas_desejadas:
            quartile = quartille_df[coluna][0]
            if quartile >= 0.75:
                cor = muito_mais_media
            if quartile <= 0.30:
                cor = muito_abaixo_media
            if (quartile > 0.30) & (quartile < 0.5):
                cor = abaixo_media
            if (quartile >= 0.5) & (quartile < 0.75):
                cor = mais_media
            dic_cores.update({coluna: cor})

        df_cor = pd.DataFrame(dic_cores, index=[0])
        df_cor = quartille_df[colunas_info].join(df_cor)

        return (df_cor, quartille_df, df_jogador_plot)


    def arte_quadro(self, df_stats, df_color_stats, nome_jogador):
        df_stats = df_stats.round(2)

        cor_fundo = self.cor_fundo
        cor_texto = self.cor_texto
        
        tamanho_arte = (3836, 2740)
        arte = Image.new('RGB', tamanho_arte, cor_fundo)
        W, H = arte.size

        font = ImageFont.truetype('Fonte/Camber-Bd.ttf', 150)
        msg = f'{nome_jogador} '
        draw = ImageDraw.Draw(arte)
        w, h = draw.textsize(msg, spacing=20, font=font)
        draw.text(((W - w) / 9, 50), msg, fill=cor_texto, spacing=20, font=font)
        draw = ImageDraw.Draw(arte)
        draw.line((3836, 300, 0, 300), fill=cor_texto, width=3)

        lista_ordenar = df_stats.columns.to_list()
        lista_ordenar.sort()

        def write_stats(altura, coluna, text_position, number_position):
                tamanho_texto = len(coluna)

                font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 58)
                if tamanho_texto > 18:
                    font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 52)
                if tamanho_texto > 30:
                    font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 40)
                if tamanho_texto > 45:
                    font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 35)
                altura += 120
                msg = f'{coluna} '
                draw = ImageDraw.Draw(arte)
                w, h = draw.textsize(msg, spacing=20, font=font)
                draw.text((text_position, altura), msg, fill=cor_texto, spacing=20, font=font)

                stat = df_stats[coluna][0]
                cor_stat = df_color_stats[coluna][0]
                font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 60)
                msg = f'{str(stat)} '
                draw = ImageDraw.Draw(arte)
                w, h = draw.textsize(msg, spacing=20, font=font)
                draw.text((number_position, altura), msg, fill=str(cor_stat), spacing=20, font=font)
                return altura

        
        altura = 280
        for coluna in lista_ordenar[0:16]:
            altura = write_stats(altura, coluna, 250, 1000)
        altura = 280

        for coluna in lista_ordenar[16:32]:
            altura = write_stats(altura, coluna, 1400, 2200)

        altura = 280
        for coluna in lista_ordenar[32:]:
            altura = write_stats(altura, coluna, 2600, 3500)

        footure = Image.open('Logo/Copy of pro_branco.png')
        w, h = footure.size
        footure = footure.resize((int(w / 2.1), int(h / 2.1)))
        footure = footure.copy()
        arte.paste(footure, (2900, -40), footure)

        draw.line((3836, 2350, 0, 2350), fill='white', width=3)
        font = ImageFont.truetype('Fonte/Camber-Rg.ttf', 45)
        draw = ImageDraw.Draw(arte)
        draw.text((250, 2390), f'Acima de 75% dos jogadores da mesma liga e posição', fill='#4747ff', spacing=20, font=font)
        draw = ImageDraw.Draw(arte)
        draw.text((250, 2480), f'Acima de 50% dos jogadores da mesma liga e posição', fill='#22ff55', spacing=20, font=font)
        draw = ImageDraw.Draw(arte)
        draw.text((250, 2570), f'Entre 30% e 50% dos jogadores da mesma liga e posição', fill='#f6ed0d', spacing=20,
                  font=font)
        draw = ImageDraw.Draw(arte)
        draw.text((250, 2660), f'Abaixo de 30% dos jogadores da mesma liga e posição', fill='#fd3535', spacing=20,
                  font=font)

        arte.save('quadro_stats.png')
        


