import matplotlib.pyplot as plt
import numpy as np

def analysis(name, data):
  """
  Plot Zipfian distribution of words + true Zipfian distribution. Compute MSE.

  :param name: title of the graph
  :param data: list of words
  """

  freq_dict = {}
  for word in data:
      freq_dict[word] = freq_dict.get(word, 0) + 1

  # Sort the frequency dictionary by descending order of frequency
  sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

  # Compute the rank and frequency lists
  ranks = np.arange(1, len(sorted_freq) + 1)
  freqs = [f for _, f in sorted_freq]

  # Plot the rank vs frequency on a log-log scale
  plt.figure()
  plt.loglog(ranks, freqs, label='Observed')

  # Compute the expected frequencies using Zipf's law
  expected_freqs = [freqs[0] / r for r in ranks]
  plt.loglog(ranks, expected_freqs, label='Zipfian')

  # Compute the mean squared error
  mse = np.mean((np.log(freqs) - np.log(expected_freqs))**2)
  plt.title(f'{name} (MSE = {mse:.2f})')
  plt.xlabel('Rank')
  plt.ylabel('Frequency')
  plt.legend()
  print(f"Mean Squared Error: {mse}")
  return plt.show(), mse
 # print("TODO", name)
 

