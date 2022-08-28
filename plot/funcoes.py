import matplotlib as mpl
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class PlotFuncoes:

    muito_mais_media = '#4747ff'
    mais_media = '#22ff55'
    abaixo_media = '#f6ed0d'
    muito_abaixo_media = '#fd3535'

    cor_fundo = '#2b2c2c'
    cor_texto = 'white'

    def notas_funcoes(self, df_func, player_id):
        muito_mais_media = self.muito_mais_media 
        mais_media = self.mais_media 
        abaixo_media = self.abaixo_media 
        muito_abaixo_media = self.muito_abaixo_media 

        cor_fundo = self.cor_fundo 
        cor_texto = self.cor_texto


        df_func = df_func[df_func['id'] == player_id].reset_index(drop=True).set_index('id').reset_index(drop=True)
        df_func = df_func.T.sort_values(0).T
        colunas_quartille = df_func.values[0]
        colunas_jogador = df_func.columns


        dic_cores = {}
        for coluna, quartile in zip(colunas_jogador, colunas_quartille):

            if quartile >= 0.75:
                cor = 'blue'
            if quartile <= 0.30:
                cor = 'red'
            if (quartile > 0.30) & (quartile < 0.5):
                cor = 'yellow'
            if (quartile >= 0.5) & (quartile < 0.75):
                cor = 'green'

            dic_cores.update({coluna: cor})
            df_cores = pd.DataFrame(dic_cores, index=[0])

            posicoes_plot = list(range(len(colunas_jogador)))
            tamanho_plot = []
            for tamanho in range(len(colunas_jogador)):
                tamanho_plot.append(1)

            df_posicao = pd.DataFrame(posicoes_plot).transpose()
            df_tamanho = pd.DataFrame(tamanho_plot).transpose()
            df_parametros = df_tamanho.append(df_posicao).reset_index(drop=True)

            dic_nomes_colunas = {}

            for coluna, nome_coluna in zip(list(df_parametros.columns), colunas_jogador):
                dic_nomes_colunas.update({coluna: nome_coluna})

            df_parametros = df_parametros.rename(columns=dic_nomes_colunas)
            df_cores = df_cores.append(df_parametros).reset_index(drop=True)

            df_cores = df_cores.transpose().reset_index()
            df_cores = df_cores.rename(columns={0: 'cor', 1: 'tamanho', 2: 'posicao'})
            df_cores = df_cores.replace('blue', muito_mais_media)
            df_cores = df_cores.replace('red', muito_abaixo_media)
            df_cores = df_cores.replace('green', mais_media)
            df_cores = df_cores.replace('yellow', abaixo_media)


        path = 'Fonte/Camber-Bd.ttf'
        prop_bold = font_manager.FontProperties(fname=path)
        mpl.rcParams['font.family'] = prop_bold.get_name()
        mpl.rcParams.update({'font.size': 90})

        fig, ax = plt.subplots(figsize=(7, 8), dpi=100, facecolor=cor_fundo)
        sns.set(rc={'axes.facecolor': cor_fundo, 'figure.facecolor': cor_fundo})

        plt.grid()
        palette_cor = list(df_cores['cor'])
        sns.scatterplot(data=df_cores, x='tamanho', y='posicao', s=1000, palette=palette_cor, hue='index')

        sns.despine(left=True, bottom=True, top=True, right=True)
        ax.set_xlim(0.9, 2.3)
        ax.get_legend().remove()

        for linha in range(len(df_cores)):
            funcao = df_cores['index'][linha]
            funcao = funcao.capitalize()
            altura = df_cores['posicao'][linha] - 0.15
            plt.annotate(funcao, xy=(1.15, altura), xytext=(1.15, altura), color=cor_texto, fontsize=30,
                         fontproperties=prop_bold)

        plt.xticks(color='black')
        plt.yticks(color='black')
        plt.axis('off')

        plt.savefig('cores-funcao.png', dpi=300, facecolor=cor_fundo)
