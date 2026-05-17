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

    def generate_histograms(self, df_obs, n_bins=100):
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
        bias_hist  = obs_hist - synth_hist #- obs_hist

        return bins, synth_hist, obs_hist, bias_hist

    def plot_histograms(self, bins, synth_hist, obs_hist, bias_hist,
                        title="", save_path=None, pdfs = None):
        """
        Plot a 2 x n_cols grid of histograms.
        Top row   : synthetic (bar) + observed (bar) + theoretical PDF (line)
        Bottom row: residual / bias bars coloured by sign

        Parameters
        ----------
        bins       : list of bin edge arrays from generate_histograms
        synth_hist : (n_cols, n_bins) synthetic density array
        obs_hist   : (n_cols, n_bins) observed density array
        bias_hist  : (n_cols, n_bins) bias array
        title      : suptitle string (e.g. dataset name)
        save_path  : filepath to save the figure (jpg). If None, just shows.
        pdfs       : list of callables, length n_cols  (optional)
           Each callable accepts a 1-D numpy array of bin centres and
           returns a 1-D array of PDF values, e.g. lambda e: 2*e
           If None, no PDF line is drawn.
        """
        plt.rcParams['xtick.labelsize'] = 14
        plt.rcParams['ytick.labelsize'] = 14
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['axes.linewidth'] = 3
        n_cols = len(bins)
        C = self.PALETTE

        fig, axes = plt.subplots(2, n_cols,
                                 figsize=(8 * n_cols, 10),
                                 sharex="col",
                                 facecolor="none")

        # Ensure axes is always 2-D even for a single column
        if n_cols == 1:
            axes = np.array(axes).reshape(2, 1)

        for col in range(n_cols):
            ax1 = axes[0, col]
            ax2 = axes[1, col]

            bin_edges = bins[col]
            bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
            width = bin_edges[1] - bin_edges[0]

            synth = synth_hist[col]
            obs = obs_hist[col]
            bias = bias_hist[col]

            # ── Top subplot ──────────────────────────────────────────────
            ax1.bar(bin_centers, obs, width=width,
                    color=C["observed"], alpha=0.85, edgecolor="none",
                    label="Observed distribution")
            ax1.bar(bin_centers, synth, width=width,
                    color=C["synthetic"], alpha=0.5, edgecolor="none",
                    label="Theoretical distribution")
            ax1.legend(fontsize=11)

            # PDF line — only drawn if a callable was supplied for this column
            if pdfs is not None and pdfs[col] is not None:
                pdf_vals = pdfs[col](bin_centers)
                ax1.plot(bin_centers, pdf_vals,
                         color=C.get("pdf_line", C["synthetic"]),
                         lw=3, label="Theoretical PDF")

            # ── Bottom subplot ────────────────────────────────────────────
            colors = [C["bias_pos"] if v >= 0 else C["bias_neg"] for v in bias]
            ax2.bar(bin_centers, bias, width=width,
                    color=colors, alpha=0.85, edgecolor="none",
                    label="Difference")
            ax2.axhline(0, color=C["zero_line"], linewidth=0.8, linestyle="--")

            ax2.set_xlabel(self.col_labels[col], color=C["text"])
            ax2.set_ylabel("Residual probability", color=C["text"])
            ax2.legend()
            ax2.set_facecolor("none")
            ax2.tick_params(colors=C["text"])
            for spine in ax2.spines.values():
                spine.set_edgecolor(C["text"])

        fig.suptitle(title, fontsize=60, y=1.01, color=C["text"])
        plt.tight_layout()

        if save_path:
            fig.savefig(save_path,bbox_inches="tight", transparent=True)
        plt.show()