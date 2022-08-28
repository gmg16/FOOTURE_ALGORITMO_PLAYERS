import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd

class Radar:
    cor_fundo = '#2C2B2B'
    fill_color = '#4747ff'
    cor_fundo_radar = '#373636'
    cor_texto = 'white'


    def plot_radar(self, df_radar, player_id):
        def _invert(x, limits):
            """inverts a value x on a scale from
            limits[0] to limits[1]"""
            return limits[1] - (x - limits[0])

        def _scale_data(data, ranges):
            """scales data[1:] to ranges[0],
            inverts if the scale is reversed"""
            for d, (y1, y2) in zip(data[1:], ranges[1:]):
                assert (y1 <= d <= y2) or (y2 <= d <= y1)
            x1, x2 = ranges[0]
            d = data[0]
            if x1 > x2:
                d = _invert(d, (x1, x2))
                x1, x2 = x2, x1
            sdata = [d]
            for d, (y1, y2) in zip(data[1:], ranges[1:]):
                if y1 > y2:
                    d = _invert(d, (y1, y2))
                    y1, y2 = y2, y1
                sdata.append((d - y1) / (y2 - y1)
                             * (x2 - x1) + x1)
            return sdata

        class ComplexRadar():
            def __init__(self, fig, variables, ranges,cor_texto, n_ordinate_levels=6):
                plt.style.use('ggplot')
                angles = np.arange(0, 360, 360. / len(variables))

                axes = [fig.add_axes([0.1, 0.1, 0.78, 0.8], polar=True,
                                     label="axes{}".format(i))
                        for i in range(len(variables))]

                l, text = axes[0].set_thetagrids(angles, labels=variables, color=cor_texto)

                [[txt.set_fontweight('bold'),
                  txt.set_fontsize(50),
                  txt.set_position((0.15, -0.15))] for txt in text]

                for ax in axes[1:]:
                    ax.patch.set_visible(False)
                    ax.grid("off")
                    ax.xaxis.set_visible(False)

                for i, ax in enumerate(axes):
                    grid = np.linspace(*ranges[i], num=n_ordinate_levels)
                    gridlabel = ["{}".format(round(x, 2)) for x in grid]

                    gridlabel[0] = ""  # clean up origin
                    ax.set_rgrids(grid, labels=gridlabel, angle=angles[i], fontsize=5)

                    ax.set_ylim(*ranges[i])

                # variables for plotting
                self.angle = np.deg2rad(np.r_[angles, angles[0]])
                self.ranges = ranges
                self.ax = axes[0]

            def plot(self, data, *args, **kw):
                sdata = self.scale_data(data, self.ranges)
                self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

            def fill(self, data, *args, **kw):
                sdata = self.scale_data(data, self.ranges)
                self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

            def scale_data(self, data, ranges):
                """scales data[1:] to ranges[0]"""
                for d, (y1, y2) in zip(data[1:], ranges[1:]):
                    assert (y1 <= d <= y2) or (y2 <= d <= y1)
                x1, x2 = ranges[0]
                d = data[0]
                sdata = [d]
                for d, (y1, y2) in zip(data[1:], ranges[1:]):
                    if y1 > y2:
                        d = _invert(d, (y1, y2))
                        y1, y2 = y2, y1
                    sdata.append((d - y1) / (y2 - y1) * (x2 - x1) + x1)
                return sdata

        df_radar_medio = df_radar
        df_radar_medio = df_radar_medio[df_radar_medio['id'] == player_id].reset_index(drop=True)
        atributos = list(df_radar_medio.columns)
        atributos.remove('id')

        valores_media = []

        for z in atributos:
            valores_media.append(df_radar_medio[z][0])
        lista_ranges = []
        for i in range(len(atributos)):
            lista_ranges.append((0, 1))

        variables = atributos
        ranges = lista_ranges
        alpha = 0.7
        cor_fundo = self.cor_fundo
        fill_color = self.fill_color
        cor_fundo_radar = self.cor_fundo_radar

        fig1 = plt.figure(figsize=(35, 40), facecolor=cor_fundo)
        radar = ComplexRadar(fig1, variables, ranges, self.cor_texto)


        data = valores_media
        radar.fill(data, alpha=alpha, color=fill_color)

        radar.ax.set_facecolor(cor_fundo_radar)

        plt.savefig(f'radar_media.png', dpi=100, format='png', facecolor='#2C2B2B')
