import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class BinaryPopulationAnalysis:

    # Colour palette
    PALETTE = {
        "synthetic" : "#45657a",
        "observed"  : "#963c31",
        "bias_pos"  : "#56787a",  # synthetic > observed
        "bias_neg"  : "#ba8b79",  # synthetic < observed
        "zero_line" : "#333333",
        "text"      : "#333333",
    }

    def __init__(self, df_synthetic, synth_cols, obs_cols, col_labels=None):
        """
        df_synthetic : synthetic population DataFrame
        synth_cols   : column names in df_synthetic (matched by position to obs_cols)
        obs_cols     : column names in observed DataFrame (matched by position to synth_cols)
        col_labels   : display labels for plots (defaults to synth_cols if None)
        """
        self.df_synthetic = df_synthetic
        self.synth_cols   = synth_cols
        self.obs_cols     = obs_cols
        self.col_labels   = col_labels if col_labels is not None else synth_cols

    def generate_histograms(self, df_obs, n_bins=50):
        """
        Generate synthetic, observed, and bias histograms.

        Parameters
        ----------
        df_obs  : observed DataFrame to compare against synthetic
        n_bins  : number of bins (default 50)

        Returns
        -------
        bins        : list of bin edge arrays, one per column
        synth_hist  : (n_cols, n_bins) array of synthetic densities
        obs_hist    : (n_cols, n_bins) array of observed densities
        bias_hist   : (n_cols, n_bins) array of (synthetic - observed)
        """
        synth_hist, obs_hist, bins = [], [], []

        for scol, ocol in zip(self.synth_cols, self.obs_cols):
            combined_min = min(self.df_synthetic[scol].min(), df_obs[ocol].min())
            combined_max = max(self.df_synthetic[scol].max(), df_obs[ocol].max())
            shared_bins  = np.linspace(combined_min, combined_max, n_bins + 1)

            n_s, _ = np.histogram(self.df_synthetic[scol], bins=shared_bins, density=True)
            n_o, _ = np.histogram(df_obs[ocol],            bins=shared_bins, density=True)

            synth_hist.append(n_s)
            obs_hist.append(n_o)
            bins.append(shared_bins)

        synth_hist = np.array(synth_hist)
        obs_hist   = np.array(obs_hist)
        bias_hist  = synth_hist - obs_hist

        return bins, synth_hist, obs_hist, bias_hist

    def plot_histograms(self, bins, synth_hist, obs_hist, bias_hist,
                        title="", save_path=None):
        """
        Plot a 3 x n_cols grid of histograms (synthetic / observed / bias).

        Parameters
        ----------
        bins       : list of bin edge arrays from generate_histograms
        synth_hist : (n_cols, n_bins) synthetic density array
        obs_hist   : (n_cols, n_bins) observed density array
        bias_hist  : (n_cols, n_bins) bias array
        title      : suptitle string (e.g. dataset name)
        save_path  : filepath to save the figure (jpg). If None, just shows.
        """
        n_cols     = len(bins)
        row_titles = ["Synthetic", "Observed", "Bias"]
        hists      = [synth_hist, obs_hist, bias_hist]
        C          = self.PALETTE

        fig, axes = plt.subplots(3, n_cols, figsize=(4 * n_cols, 9),
                                 facecolor="none")

        for row in range(3):
            for col in range(n_cols):
                ax          = axes[row, col]
                bin_edges   = bins[col]
                bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
                width       = bin_edges[1] - bin_edges[0]
                values      = hists[row][col]

                # Bias row: colour bars by sign
                if row == 2:
                    colors = np.where(values >= 0, C["bias_pos"], C["bias_neg"])
                    ax.bar(bin_centers, values, width=width,
                           color=colors, alpha=0.85, edgecolor="none")
                    ax.axhline(0, color=C["zero_line"], linewidth=0.8, linestyle="--")
                else:
                    color = C["synthetic"] if row == 0 else C["observed"]
                    ax.bar(bin_centers, values, width=width,
                           color=color, alpha=0.85, edgecolor="none")

                ax.set_facecolor("none")

                if row == 0:
                    ax.set_title(self.col_labels[col], fontsize=24, color=C["text"])
                if col == 0:
                    ax.set_ylabel(row_titles[row], fontsize=24, color=C["text"])

                ax.tick_params(labelsize=8, colors=C["text"])
                for spine in ax.spines.values():
                    spine.set_edgecolor(C["text"])

        fig.suptitle(title, fontsize=60, y=1.01, color=C["text"])
        plt.tight_layout()

        if save_path:
            fig.savefig(save_path, format="jpg", dpi=150,
                        bbox_inches="tight", transparent=True)
        plt.show()