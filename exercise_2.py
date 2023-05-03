import matplotlib.pyplot as plt
from collections import Counter

def analysis(name, data):
  """
  Plot Zipfian distribution of words + true Zipfian distribution. Compute MSE.

  :param name: title of the graph
  :param data: list of words
  """

  word_freq = Counter(data)
    
  # Compute the rank-frequency distribution
  freq_rank = sorted(list(word_freq.values()), reverse=True)
  
  # Compute the rank of each word
  word_rank = list(range(1, len(word_freq)+1))
  
  # Plot the Zipfian distribution of words
  plt.plot(word_rank, freq_rank, 'o')
  plt.title(name)
  plt.xlabel('Word Rank')
  plt.ylabel('Word Frequency')
  
  # Compute the true Zipfian distribution
  k = freq_rank[0] # normalization constant
  true_freq_rank = [k/i for i in word_rank]
  
  # Plot the true Zipfian distribution
  plt.plot(word_rank, true_freq_rank, '-')
  
  # Compute the mean squared error
  mse = sum([(freq_rank[i] - true_freq_rank[i])**2 for i in range(len(word_rank))]) / len(word_rank)
  print(f"Mean Squared Error: {mse}")
  
  # Show the plot
  plt.show()
 # print("TODO", name)
