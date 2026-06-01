---
date: "2026-1-19"
---


[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Fourier-Series/blob/main/Fourier-series.py)

# The Fourier Series
People are generally comfortable thinking about functions of time. For example, a signal might be described as $X(t)$, where $t$ is time. This referred to as the "time domain". However, it is often useful to think of signals and sytems in the "frequency domain", where frequency, instead of time, is the independent variable, e.g., $X(f)$, where $f$ is frequency. 

We are going to study several basic waves. All of these can be thought of as combinations of various sines waves.
- Sawtooth Wave
- Triangle Wave
- Square Wave
- Pulse/Rectangle Wave

## 1. Sawtooth Wave
- The sawtooth wave is derived from the frequencies of the harmonic series.
- Harmonics = all harmonics.
- Amplitude = 1 / (harmonic number).
- If a sawtooth wave is an infinite sum of sine waves, then let's use summation notation to express the wave. 

Shifting the phase of the even harmonics by 180 degrees will make a sawtooth wave that ramps up instead of ramping down. No difference in how we perceive the sound.
<p align="center">
   $f_{saw}(t) =\;\frac{1}{2}-\frac{1}{\pi}\sum_{k=1}^{\infty}{\frac{(-1)^{k}}{k}}\;sin(2\pi kvt)$
</p>

where:
- $f_{saw}(t)$ is a sawtooth wave as a function of $t$ (time) in seconds.
- $v$ is a fundamental frequency.
- $A$ is a fundamental amplitude.
- $n$ represents the harmonic number where $n=1$ is the fundamental.

### Key arguments
- `n`: sets the number of sample, higher `n` smoother curves.
- `T` and `nu`: defines the period and frequency.
- `duration`: creates time vector
- `t = np.arange(0, duration, duration/n)`: this is the x-axis for plotting.
- `f_saw = (t + 0.5) %1`: generates the sawtooth wave, keeps values between 0 and 1, producing the repeating ramp shape of a sawtooth.
- `def fourier_expansion_sawtooth(nterms):`: defines a function that computes the Fourier series a[[roximation of the sawtooth wave.
- `for icol in range(3):`: loops over the three subplots.
- `nterms = (icol + 1) * 3`: each iteration increases the number of Fourier terms.
- `axes[icol].plot(t, fourier_expansion_sawtooth(nterms),...)`: Plots the Fourier approximation on the same subplot.
- `plt.tight_layout()`: ensures the labels and titles don't overlap.

This Python script demonstrates the Sawtooth wave with multiple axes. In the simple case, they can be arranged in a grid of rows and columns as follows.

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of sample points
n = 2048

# period in s
T = 1

# Frequency
nu = 1 / T

# Length sampling, s
duration = 2
t = np.arange(0, duration, duration/n)

# Sawtooh, /|/|/|
f_saw = (t + 0.5) % 1

def fourier_expansion_sawtooth(nterms):
    fourier_sawtooth = np.zeros(n)
    for k in range(1, nterms+1):
        fourier_sawtooth +=  (-1) ** k * np.sin(2 * np.pi * k * nu * t) / k
    return 0.5 - (1/np.pi) * fourier_sawtooth
    
# Plotting
fig, axes = plt.subplots(ncols =3, figsize=(12, 4))

# different expansion depths
for icol in range(3):
    nterms = (icol +1) * 3
    axes[icol].plot(t, f_saw, label='Sawtooth', color='black')
    axes[icol].plot(t, fourier_expansion_sawtooth(nterms), label='Fourier', linestyle='--')
    axes[icol].legend()
    axes[icol].set_title(f"Sawtooth vs Fourier (n={nterms})")
    axes[icol].set_xlabel('Time [s]')
    axes[icol].set_ylabel('Amplitude')

plt.savefig('Sawtooth vs Fourier.svg', bbox_inches='tight')
plt.tight_layout()    
plt.show()
```
![Figure 1. Sawtooth vs Fourier](/quarto-workflows/images/Fourier series/Sawtooth vs Fourier.svg)

## 2. Triangle wave
A triangular wave or triangle wave is a non-sinusoidal waveform named for its triangular shape. Like a square wave, the triangle wave contains only odd harmonics. 
- Harmonics: only odd-numbered harmonics
- Amplitude: 1/(Harmonic Number)^2
- Phase: Every other harmonic is 180 degrees out of phase.

<p align="center">
    $f_{tria}(t)=-\frac{8}{\pi^2}\sum_{k=1}^{\infty}\frac{(-1)^k}{(2k-1)^2}sin(2\pi(2k-1)t)$
</p>

where:
- Odd harmonics: $2k-1$
- Amplitudo scalling: $-\frac{8}{\pi^{2}}$
- Alternating sign: $(-1)^{k}$
- Decay: $\frac{1}{2k-1}^{2}$

This summation makes use of the fact that $-sin(x)=sin(x+\pi)$ to handle alternating odd harmonics 180 degrees our of phase.

This Python script demonstrates the Triangle wave with multiple axes. In the simple case, they can be arranged in a grid of rows and columns as follows.
Parameters:
- `nterms`: number of terms in the expansion.
- `t`: time array.
- `nu`: fundamental frequency (default 1 Hz).

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of sample points
n = 2048

# period in s
T = 1

# Fundamental Frequency
nu = 1 / T 

# Length sampling, s
duration = 2
t = np.arange(0, duration, duration/n)

def fourier_expansion_triangle(nterms, t, nu=1):
    """
    Fourier expansion of a triangle wave using nterms harmonics.
    """
    fourier_triangle = np.zeros_like(t)
    for k in range(1, nterms+1):
        harmonic = 2*k-1
        fourier_triangle += ((-1)**k / (harmonic**2)) * np.sin(2*np.pi*harmonic*nu*t)
    return -(8/(np.pi**2)) * fourier_triangle

f_triangle = 2 * np.abs((t %1) - 0.5)

# plotting
fig, axes = plt.subplots(ncols=3, figsize=(12, 4))

for icol in range(3):
    nterms = (icol + 1) * 3
    axes[icol].plot(t, f_triangle, label='triangle', color='black')
    axes[icol].plot(t, fourier_expansion_triangle(nterms, t, nu=1), label='Fourier', linestyle='--')
    axes[icol].legend()
    axes[icol].set_title(f"Triangle vs Fourier (n={nterms})")
    axes[icol].set_xlabel("Time [s]")
    axes[icol].set_ylabel("Amplitudo")

plt.savefig('Triangle vs Fourier.svg', bbox_inches='tight')
plt.tight_layout()
plt.show()
```
![Figure 2. Triangle vs Fourier](/quarto-workflows/images/Fourier series/Triangle vs Fourier.svg)

## 3. Square Wave
A square wave is a non-sinusoidal periodic waveform in which the amplitude alternates at a steady frequency between fixed minimum and maximum values, with the same duration at minimum and maximum. 
- Harmonics: Odd-numbered harmonics.
- Amplitudes: 1/Harmonic Number.
- Phase: All harmonics in phase.
<p align="center">
    $f_{sq}(t)=\frac{4}{\pi}\sum^{\infty}_{k=1}sin[2\pi(2k-1)vt]$
</p>

Write the partials of a square wave using summation notation. Recall that a square wave has only odd harmonics, the amplitudes of the harmonics are (1/harmonic number), and all harmonics are in phase.

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of sample points
n = 2048

# period in s
T = 1

# Frequency
nu = 1 / T

# Length sampling, s
duration = 2
t = np.arange(0, duration, duration/n)

# square-wave, _|_|_|
f_sq = np.where((t % T) < T/2, 1, -1)

def fourier_expansion_square(nterms):
    fourier_square = np.zeros(n)
    for k in range(1, nterms+1):
        fac = 2 * k - 1
        fourier_square += np.sin(2 * np.pi * fac * nu * t)/ fac
    return 4 / np.pi * fourier_square

# Plotting
fig, axes = plt.subplots(ncols =3, figsize=(12, 4))

# different expansion depths
for icol in range(3):
    nterms = (icol +1) * 3
    axes[icol].plot(t, f_sq, label='Sawtooth', color='black')
    axes[icol].plot(t, fourier_expansion_square(nterms), label='Fourier', linestyle='--')
    axes[icol].legend()
    axes[icol].set_title(f"Square vs Fourier (n={nterms})")
    axes[icol].set_xlabel('Time [s]')
    axes[icol].set_ylabel('Amplitude')

plt.savefig('Square vs Fourier.svg', bbox_inches='tight')
plt.tight_layout()    
plt.show()
```
![Figure 3. Square vs Fourier](/quarto-workflows/images/Fourier series/Square vs Fourier.svg)

## 4. Pulse/Rectangle wave
A pulse wave, pulse train, or rectangular wave is a sequence of discrete pulses occurring in a signal over time. 
- Pulse waves is rectangular waves are generalizations of the square waves.
- A square wave's period has an equal portion at high and low amplitudes. In a rectangular wave, those proportions need be equal. Therefore, all square waves are rectanglular waves but not vice versa.

The equation for a Pulse wave is more complicated, but it still relies upon summing sinusoids (in this case cosine waves). Note that the sine in this equation is simply a scaling factor for amplitude, as it is not a function of time. 
<p align="center">
    $f_{pulse}(t)=dA + \sum_{n=1}^{\infty} \frac{2A}{\pi n}sin(\pi dn)cos(2\pi fnt)$
</p>

This Python script demonstrates the Pulse/Rectangle wave with multiple axes. In the simple case, they can be arranged in a grid of rows and columns as follows.

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of sample points
n = 2048

# period in s
T = 1

# Frequency
nu = 1 / T

# Length sampling, s
duration = 2
t = np.linspace(0, duration, n)

# Duty cycle (fraction of period high)
duty = 0.25

# Pulse wave: +1 for futy fraction
f_pulse = np.where((t % T) < duty * T, 1, 0)

def fourier_expansion_pulse(nterms, t, nu=1, duty=0.25):
    fourier_pulse = np.zeros_like(t)
    for k in range(1, nterms+1):
        fourier_pulse += (np.sin(k * np.pi * duty)/ k ) * np.cos(2 * np.pi * k * nu * t)
    return duty + (2/np.pi) * fourier_pulse

# Plotting
fig, axes = plt.subplots(ncols =3, figsize=(12, 4))

# different expansion depths
for icol in range(3):
    nterms = (icol +1) * 3
    axes[icol].plot(t, f_pulse, label='Pulse', color='black')
    axes[icol].plot(t, fourier_expansion_pulse(nterms, t, nu, duty), label='Fourier', linestyle='--')
    axes[icol].legend()
    axes[icol].set_title(f"Pulse vs Fourier (n={nterms}, duty={duty})")
    axes[icol].set_xlabel('Time [s]')
    axes[icol].set_ylabel('Amplitude')

plt.savefig('Pulse vs Fourier.svg', bbox_inches='tight')
plt.tight_layout()    
plt.show()
```
![Figure 4. Pulse vs Fourier.svg](/quarto-workflows/images/Fourier series/Pulse vs Fourier.svg)

## In summary
- Any periodic signal can be constructed from a sum of sine waves.
  - The process of creating complex sounds from sine waves or other constituent parts is called additive synthesis.
- The sine wave, sawtooth wave, triangle wave, and pulse waves are classic waveforms since the advent of electronic music.
  - They are used everywhere in the music we hear today, and we are the basis for many synthesizers.
- Sawtooth waves, triangle waves, and pulse waves come in band-limited and non-band-limited forms.
  - Non-bandlimited forms can produce strange artifacts at higher frequencies (see aliasing coming up).
  - Bandlimited forms are "safer" but are not as rich harmonically - they do not truly represent the waveforms.
