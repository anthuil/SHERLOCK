import numpy as np

from sherlockpipe.scoring.SignalSelector import SignalSelector, SignalSelection


class BasicSdeSignalSelector(SignalSelector):
    """
    Selects the signal with best SNR
    """
    def __init__(self):
        super().__init__()

    def select(self, transit_results, snr_min, sde_min, detrend_method, wl):
        detrends_sde = np.nan_to_num([transit_result.sde
                                      for key, transit_result in transit_results.items()])
        best_signal_sde = np.nanmax(detrends_sde)
        best_signal_sde_index = np.nanargmax(detrends_sde)
        selected_signal_snr = transit_results[best_signal_sde_index].snr
        selected_signal = transit_results[best_signal_sde_index]
        if best_signal_sde > sde_min and selected_signal_snr > snr_min:  # and SDE[a] > SDE_min and FAP[a] < FAP_max):
            best_signal_score = 1
        else:
            best_signal_score = 0
        return SignalSelection(best_signal_score, best_signal_sde_index, selected_signal)