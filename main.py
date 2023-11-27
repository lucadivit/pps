from matplotlib import pyplot as plt
import seaborn as sns
import support.ppscore_calculation as pps


def export_pps(df):
    plt.figure(figsize=(16, 12))
    matrix_df = pps.matrix(df)[['x', 'y', 'ppscore']].pivot(columns='x', index='y', values='ppscore')
    sns.heatmap(matrix_df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True)
    plt.savefig('./output.png')
