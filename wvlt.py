import numpy as np
import matplotlib.pyplot as plt

def Sin(length, period, shift):
    array = np.zeros((length, 1))
    for i in range(length):
        array[i] = i
    array = np.sin(array / period * 2 * np.pi + shift)
    return array


def Cos(length, period, shift):
    array = np.zeros((length, 1))
    for i in range(length):
        array[i] = i
    array = np.cos(array / period * 2 * np.pi + shift)
    return array

def Wavelet(length, period, sd, shift):
    wlt = Sin(length, period, shift) * NormalDistribution(length, sd, shift)
    return wlt


def NormalDistribution(length, sd, med):
    x = np.zeros((length, 1))

    for i in range(int(-length / 2), int(length / 2)):
        x[int(i + length / 2)] = i/10
    return np.exp(-np.square(x - med) / 2 / sd) / (np.sqrt(np.pi) * sd)



def WaveletTransform(signal, wltLen, wMin, wMax, depth):
    matrix = np.zeros((np.max(np.shape(signal)), depth))
    
    for w in range(depth):
        freq = (wMax - wMin) / depth * w + wMin
        
        #print(freq)
        wlt = Wavelet(wltLen, freq, 2, 0)
        
        
        matrix[:, w] = np.convolve(signal[:, 0], wlt[:, 0], mode = "same")
        
    return matrix
