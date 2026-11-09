International Conference on Renewable Energies and Power Quality (ICREPQ’14)
Cordoba (Spain), 8th to 10th April, 2014
Renewable Energy and Power Quality Journal (RE&PQJ)
ISSN 2172-038 X, No.12, April 2014
Harmonic Emission of Large PV Installations
Case Study of a 1 MW Solar Campus
Anantaram Varatharajan1, Stefan Schoettke1, Jan Meyer1 and Andreas Abart2
1 Institute of Electrical Power Systems and High Voltage Engineering
Technische Universitaet Dresden, Germany
Phone: +49 351 463 35102, e-mail: jan.meyer@tu-dresden.de
2Energie AG Oberösterreich
Gmunden, Austria
e-mail: Andreas.Abart@netzgmbh.at
Abstract. Extensive measurements were carried out at a measurements were carried out to assess the accuracy of
1 MW photovoltaic (PV) installation with focus on the analysis the PQ instruments. For voltage harmonics larger than
of harmonic emission both for classical harmonics below 2.5 kHz 0.2% and current harmonics larger than 0.2 A the error
and higher frequency emission in the range of 2-150 kHz. The for magnitude is smaller than ±2% and the error for phase
installation consists of multiple inverters with different rated angle is smaller than ±1°.
power. Beside the measurement of total emission of all inverters,
in one part of the measurement the inverters were switched off Voltages and currents in the higher frequency range
and on stepwise following a predefined schedule. This provides a (2 – 150 kHz) were measured at one large inverter (three
comprehensive basis for a detailed characterisation of the phases) and four small inverters (each single phase). Two
interactions between the inverters in terms of harmonic emission. specific network analysers with a sampling rate of
After a description of the measurement setup the paper discusses 1 MS/s and a resolution of 16 bits were used. The current
the total emission of the installation, the dependency of the
was measured using current clamps. During the switching
emission on the supply voltage distortion and the potential of
of inverters raw data in time-domain was stored
harmonic cancellation due to phase angle diversity between the
continuously. Otherwise three seconds every minute were
different inverters. The results enable a better understanding of
stored to reduce the data size. Afterwards, a high pass
the harmonic emission behaviour of large PV installations. The
paper is intended to be an contribution to the development and filter (elliptic, 3rd order, 2 kHz passband) was applied to
improvement of respective harmonic models. the measured data. Subsequently it was split in 200-ms-
blocks (5-Hz-resolution) and for each block a discrete
Key words Fourier transformation was performed. All values are
presented in the logarithmic unit dB , where 120 dB
Photovoltaic inverter, Harmonics, cancellation effect, µV µV
corresponds to 1 V and 0 dB to 1 µV. For currents the
Higher frequency emission µV
unit dB is used respectively. The network analysers
µA
have accuracy better than ±5% for currents larger than
1. Measurement Setup
30 dB and ±2% for voltages larger than 40 dB .
µA µV
The PV installation comprises of nine large inverters In order to obtain comprehensive data for a systematic
with rated power of 100 kVA and eleven small inverters analysis of harmonic emission of a different number of
with rated power in the range between 1 kVA and 10 kVA inverters and the interaction among them, a coordinated
(total output of nearly 50 kVA). All large inverters are switching of the inverters was performed in one part of
three phase while all small inverters are single phase. the measurement. The inverters were switched off
sequentially in a predetermined order (Table I) and with a
For the measurement of low order harmonics, eleven PQ
defined time delay. A part of small inverters were turned
instruments complying with IEC 61000-4-30 Class A were
off in the beginning followed by the large inverters and
used. The voltage and current spectra (magnitude and
the remaining small inverters. Figure 1 illustrates the
phase angle related to voltage fundamental) were
switch-off procedure by means of active power. Power
measured with each instrument for almost two days using
Line Communication (PLC) is used in the network for
an averaging interval of 150 periods (three seconds). Each
meter reading but was switched off during this
of the large inverters, the sum of all small inverters and the
experiment.
total sum of the installation were monitored. Calibration
https://doi.org/10.24084/repqj12.460 701 RE&PQJ, Vol.1, No.12, April 2014

Power at the Transformer
Table I Switch off sequence of inverters
|     | 50  |     |     |     |     |     |          |           |          |     |          |           |          |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | --- | -------- | --------- | -------- |
|     |     |     |     |     |     |     | Time     |           |          |     | Time     |           |          |
|     |     |     |     |     |     |     |          | Inverter  | Setting  |     |          | Inverter  | Setting  |
|     |     | 0   |     |     |     |     | (mm:ss)  |           |          |     | (mm:ss)  |           |          |

|     |     |     |     |     |     |     | 0:00  | Measurement Begin  |     |     | 5:30  | Inv 4  | II  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------ | --- | --- | ----- | ------ | --- |
-50
Wk ni rewoP
|     |     |     |     |     |     |     | 0:30  | PLC system OFF  |     |     | 5:55  | Inv 3  | I   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | --- | ----- | ------ | --- |
-100

|     |     |     |     |     |     |     | 0:55-3:20  | 7 Small Inverters  |     |     | 6:20  | Inv 2  | I   |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | ----- | ------ | --- |
90
-150
|     |      |     |     |     |   150 |      | 3:50  | Inv 8  |     | I    | 6:45  | Inv 1  | I   |
| --- | ---- | --- | --- | --- | ----- | ---- | ----- | ------ | --- | ---- | ----- | ------ | --- |
|     |      |     | 120 |     |       | L610 |       |        |     |      |       |        |     |
|     | -200 |     |     |     |       |      |       |        |     |      |       |        |     |
|     |      |     |     |     |       | L2   | 4:15  | Inv 7  |     | I    | 7:10  | Inv 9  | I   |
L3
|     | -250 |         |     |              |     |     | 4:40  | Inv 6  |     | II    | 7:35-8:50  | 4 small inverters  |     |
| --- | ---- | ------- | --- | ------------ | --- | --- | ----- | ------ | --- | ----- | ---------- | ------------------ | --- |
|     |      | 0   1 2 | 3   | 4 5          | 6 7 | 8 9 |       |        |     |       |            |                    |     |
|     |      |         |     | Time in Mins |     |     |       |        |     |       |            |                    |     |
|     |      |         |     |              |     |     | 5:05  | Inv 5  |     | II    | 9:00       | Measurement End    |     |
|     |      | 150     |     |              |     |     | 30    |        |     |       |            |                    |     |
Fig. 1 Total power during coordinated switching OFF

|     |     |     |     |     |     |     | voltage harmonics for both states (all inverters ON and  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |

OFF) are presented in Figure 3b. Both plots are limited to

|     |     |     |     |     | Inv 1 - I |     | the order 25 as the harmonics beyond are insignificant  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Inv 2 - I
|     |     |     |     |     |     |     | and  non-informative.  |     |     | 99th  | percentiles  | of  the  | data  are  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----- | ------------ | -------- | ---------- |
Inv 3 - I
180 Inv 4 - II shown  0 (cf.  IEC 61000-3-14).  Considerable  current  is
|     |     |     |     |     | Inv 5 - II |     | observed for harmonic orders 5, 7, 9, 11, and 13. 5th and  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Inv 6 - II
7th harmonic current are predominant and hence emphasis
Inv 7 - I
  50
|     |     |       |     |     | Inv 8 - I     |     | is  laid                                                | on  these  | harmonics  |     | in  the  | later  analysis.  | The  |
| --- | --- | ----- | --- | --- | ------------- | --- | ------------------------------------------------------- | ---------- | ---------- | --- | -------- | ----------------- | ---- |
|     |     |       |     |     | Inv 9 - I     |     | voltage spectrum is evaluated for before and after the  |            |            |     |          |                   |      |
|     |     |   100 |     |     | Sum Small Inv |     |                                                         |            |            |     |          |                   |      |
switching process to analyse the impact of the inverters.
A ni tnerruC The profile of voltage spectrum in the ON state is similar
|     |     | 210 |     |     |     |     | 330                      |      |          |               |     |                     |           |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ---- | -------- | ------------- | --- | ------------------- | --------- |
|     |     |     |     |     |     |     | to the current spectrum  |      |          | implying a    |     | strong correlation  |           |
|     |     |     |     |     |     |     | between                  | the  | voltage  | and  current  |     | harmonics.          | The  9th  |

|     |     |                                               |     |     |     |     | harmonic  | voltage   | is       | dominated  | by        | the  inverters.  | The            |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | --------- | --------- | -------- | ---------- | --------- | ---------------- | -------------- |
|     |     | Fig. 2 Fundamental currents of all inverters  |     |     |     |     |           |           |          | 11th       |           |                  |                |
|     |     |                                               |     |     |     |     | cause     | for  the  | reduced  |            | harmonic  | can              | either  be  a  |
240
possible cancellation effect or a variation in the level in
While almost all of the small inverters are of different  the  upstream  grid,  because  the  spectra  correspond  to
brand and type, the nine large inverters are of same brand
different instants of time. The other phases have similar
and type, but with two different settings for their cos(P)- properties. L3 shows slightly different values, which may
control:  be caused by different impedance of the phases. This is
not further considered in this paper.
I)  cos(P)-control enabled (1, 2, 3, 7, 8, 9)
II) cos(P)-control disabled (4, 5, 6)
The Total Harmonic Distortion (THD) in voltage is
evaluated by the following equation:
|     | The  different  | behaviour  |     | of  inverters  | for  fundamental  |     |     |     |     |     |     |     |     |
| --- | --------------- | ---------- | --- | -------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
current is depicted in Figure 2.
50

V2
i
i2
| 2. Analysis of low order harmonics   |     |     |     |     |     |     |     |     | THD |    | 100%  |     | (1)  |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- |
|                                      |     |     |     |     |     |     |     |     | V   | V   |        |     |      |
1
A. Emission of the installation  The  time  plot  of  THD (Figure  4a)  at  the  busbar
V
|     |                |     |          |          |             |          | decreases  | by  | nearly  | 45%  | when  | switching  | off  the  |
| --- | -------------- | --- | -------- | -------- | ----------- | -------- | ---------- | --- | ------- | ---- | ----- | ---------- | --------- |
|     | The  analysis  | is  | focused  | on  the  | time  span  | of  the  |            |     |         |      |       |            |           |
coordinated inverter switch-off. The current spectrum in  inverters. The THD in current calculated in similar way
can be misleading if the fundamental component is low
L1 (all inverters ON) is shown in Figure 3a, while the
|     | 60  |     |     |     |     |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ON
|     |     |     |     |     |     |     | 1.8 |     |     |     |     |     | OFF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50
1.6
1.4
40
% ni egatloV 1.2
A ni tnerruC
|     | 30  |     |     |     |     |     | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.8
20
0.6
0.4
10
0.2
|     | 0   |     |                |     |     |     | 0   |     |     |                |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
|     |     | 5   | 10             | 15  | 20  | 25  |     | 5   | 10  |                | 15  | 20  | 25  |
|     |     |     | Harmonic Order |     |     |     |     |     |     | Harmonic Order |     |     |     |
Fig. 3a Spectrum of Harmonic Currents (total)  Fig. 3b Spectrum of Harmonic Voltage (Busbar)

https://doi.org/10.24084/repqj12.460 702 RE&PQJ, Vol.1, No.12, April 2014

2.4
2.2
2
1.8
1.6
1.4
1.2
1 0 1 2 3 4 5 6 7 8 9
Time in Mins
Fig. 4a Time Characteristic of Voltage THD
V
Fig. 4b Time Characteristic of THC (total current)
or strongly varying. In order to meet this shortcoming, current in L3 is due to a possible impedance variation of
total harmonic current (THC) is defined as absolute value the phases. The setting II inverters have a smaller
as follows: magnitude. The total harmonic current of all small
inverters (SSI) is very low and therefore not further
50 considered.
THC I2 (1)
i
i2 Figure 6 shows the 5th harmonic current in phase L1
during the whole switching interval in the complex plane.
The time plot of the THC (Figure 4b) shows the
The phases L2 and L3 show similar behaviour. All large
dominating impact of the nine large inverters on the
inverters except Inv 8 show a significant change in
current distortion.
magnitude in the range of 30% to 50%. The level of
B. Emission of individual inverters variation is directly related to the switching order. Inv 8
was switched off first and does not show any “variation
An extensive analysis of all relevant harmonics was
trail”. Inv 9 was turned off last and has the highest
carried out. For space reason the paper presents a detailed
variation (longest trail). The 5th harmonic current
study of 5th harmonic and discusses only additional
emission of the inverters strongly depends on the voltage
findings for the other harmonics. The 99th percentile values
distortion (cf. Figure 8). As soon as the 5th voltage
of the 5th harmonic current of individual inverters before
harmonic decreases due to switching off the other
switch-off are shown in Figure 5. The slightly higher
inverters (4th to 7th minute in Figure 8), the 5th current
harmonic drops considerably in magnitude until the
inverter is turned off. In case of sinusoidal supply voltage
conditions the current magnitude would become a
minimum. Due to the existing background distortion this
value can however not be obtained from the
measurements. A similar behaviour has been observed
for other types of PV inverters as well as for car charging
rectifiers or switched mode power supplies with active
power factor correction. Therefore a simple constant
current source is not sufficient to model these inverters in
terms of harmonics.
The impact of switching off inverters on the grid
voltage is depicted in Figure 7. The 5th harmonic voltage
is observed to drop by nearly 50%. The 5th harmonic
%
ni DHT V
60
50
40
30
20
10
0
0 1 2 3 4 5 6 7 8 9
Time in Mins
A
ni CHT
8
7
6
5
4
3
2
1
0
1 2 3 4 5 6 7 8 9 SSI
Inverter
Fig. 5 5th Harmonic Current (all phases)
A
ni
tnerruC
90
120 60
150 30
Fifth Harmonic Currents in A
180 0
2
210 4 330
6
240 300
270
Fig 6 5th Harmonic Current Clusters (L1)
Fig 7 5th Harmonic Voltage (L1)
L1
L2
L3
A
ni tnerruC
Inv 1
Inv 2
Inv 3
Inv 4
Inv 5
Inv 6
Inv 7
Inv 8 Inv 9
Sum Small Inv
90
5
120 60
4
3
150 30
2
1
180 0
210 330
240 300
270
V
ni
egatloV
https://doi.org/10.24084/repqj12.460 703 RE&PQJ, Vol.1, No.12, April 2014

Fifth Voltage and Current of Inverter 9
| 6   |     |     |               |  10 |     |     | Magnitude Linearity |     |     | Phase Angle Linearity |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | ------------------- | --- | --- | --------------------- | --- | --- | --- |
|     |     |     | Fifth Voltage |     |     |     |                     |     |     | -70                   |     |     |     |
Fifth Current
4.5
|     |     |     |     | 8   |     |     |     |     |                     | -80 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
| 5   |     |     |     |     |     |     |     |     | elgnA esahP egatloV |     |     |     |     |
4
-90
| V ni egatloV |     |     |     | 6 A ni tnerruC |     | V ni egatloV |     |     |     |      |     |     |     |
| ------------ | --- | --- | --- | -------------- | --- | ------------ | --- | --- | --- | ---- | --- | --- | --- |
|              |     |     |     |                |     | 3.5          |     |     |     | -100 |     |     |     |
4
|     |     |     |     | 4   |     |     |     |     |     | -110 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
3
-120
3
|     |     |     |     | 2   |     | 2.5 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-130
|     |         |         |                 |     |     | 3   | 4            | 5 6 | 7   | -50                 | -40 | -30 |     |
| --- | ------- | ------- | --------------- | --- | --- | --- | ------------ | --- | --- | ------------------- | --- | --- | --- |
| 2   |         |         |                 | 0   |     |     | Current in A |     |     | Current Phase Angle |     |     |     |
| 0 0 | 1 1 2 2 | 3 3 4 4 | 5 5 6 6 7 7 8 8 | 9 9 |     |     |              |     |     |                     |     |     |     |
Fig. 9 5th Harmonic Voltage – Current Relationship (Inv 9)
|     |     | Time in Mins |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 8 Time plot of 5th voltage and current harmonic of an
individual inverter
|     |     |     |     |     |     |     | 90  |   0.8 |     |     | 90   6 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------ | --- | --- |
|     |     |     |     |     |     | 120 |     | 60    |     | 120 |        | 60  |     |
current  with  a  prevailing  phase  angle  of  300°  in  V ni egatloV   0.6
A ni tnerruC   4
|     |     |     |     |     |     | 150 |   0.4 | 30  |     | 150 |     | 30  |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
combination with the inductive grid impedance causes the
|     |     |     |     |     |     |     |   0.2 |     |     |     |   2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
voltage to shift from 290° to 230°.
|                    |     |          |                    |          |     | 180 |     |     | 0 180 |     |     | 0   |     |
| ------------------ | --- | -------- | ------------------ | -------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
| The  relationship  |     | between  | the  current  and  | voltage  |     |     |     |     |       |     |     |     |     |
harmonics is studied with scatter plots of Inv 9 (Figure 9).
|               |           |              |                   |     |     | 210 |     | 330 |     | 210 |     | 330 |     |
| ------------- | --------- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| It  provides  | valuable  | information  | for  development  | of  |     |     |     |     |     |     |     |     |     |
harmonic  models.  A  linear  relation  is  observed  in  240 300 240 300
|     |     |     |     |     |     |     | 270 |     |     |     | 270 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
magnitude and phase angle between voltage and current  Fig. 10 9th Harmonics a) Voltage; b) Current
for 5th harmonics. The slope of the curve is determined not
only by the sensitivity of emission of the inverter to the
|     |     |     |     |     |     | In  order  | to  validate  |     | the  reliability  |     | of  the  | data,  | the  |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ----------------- | --- | -------- | ------ | ---- |
voltage  variations  but  also  by  the  impedance  of  the  measured  sum  at  the  busbar  is  compared  with  the
upstream grid. However, as far as an individual inverter is  calculated  vectorial  summation  of  individual  inverters
concerned as in the Figure 9, the inverter characteristics  and the percentage error is calculated. For all considered
are dominant and the grid impedance plays a minor role.
harmonics the error is smaller than 5% for 95% of the
measurement data, which means a reliable data set for
For 7th harmonic currents the setting I inverters have
further diversity calculations.
nearly six times higher emission than setting II inverters.
Moreover setting II inverters are observed to have a higher  Two indices are commonly used to quantify the phase
phase  angle  variation.  The  scatter  plots  between  the  cancellation  effect:  diversity  factor  and  summation
voltage  and  current  shows  linear  relationship  only  for  exponent. The diversity factor is determined by
setting I inverters. Figure 10 exemplarily shows the total
| 9th       |          |      |                           |          |     |     |     |     |     |     | n   |     |     |
| --------- | -------- | ---- | ------------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| harmonic  | current  | and  | voltage  at  the  busbar  | as  the  |     |     |     |     |     |     |     |     |     |
 I(h)
inverters are switched off. Similar curves are also observed  i
|                               |     |     |     |     |     |     |                 | Vector sum |     | I(h)    |        |        |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --- | ------- | ------ | ------ | --- |
| for 11th and 13th harmonics.  |     |     |     |     |     | k(  | h)              |            |     | V E C   | i 1   |        |     |
|                               |     |     |     |     |     |     |                |            |     |       |        |   (3)  |     |
|                               |     |     |     |     |     |     | p Arithmeticsum |            |     | I ( h ) | n      |        |     |
|                               |     |     |     |     |     |     |                 |            |     | ARI     |  I(h) |        |     |
C. Phase Angle Diversity
i
Figure 6  gives  a  qualitative  perspective  of  the  phase  i1
| diversity of 5th harmonics. Unlike magnitude, the phase  |     |     |     |     | where I is the current vector of device i (in this case a  | i   |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
particular inverter), h the order of harmonic and n the
angle of the current harmonics does not vary largely under
number of devices (in this case inverters). The diversity
the changing voltage harmonics during switching period.
factor directly presents, how much the absolute value of
Therefore a weak phase cancellation effect is expected.
the vector sum is smaller than the algebraic sum. The
|      |     |     |     |     | value ranges from 0 ≤ k(h) ≤ 1, where  |     |     |     |     |     | k(h) = 0 means  |     |     |
| ---- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- |
| 0.99 |     |     |     |     |                                        |     |     |     | p   |     | p               |     |     |
perfect cancellation and k(h) = 1 no cancellation at all.
| 0.98 |     |     |     |     |     |                                                       |     |     | p   |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 0.97 |     |     |     |     |     | The diversity factor is evaluated for all considered  |     |     |     |     |     |     |     |
 rotcaF ytisreviD harmonics and the time when all inverters are connected.
0.96
The measurements at the individual inverters are simply
0.95
added algebraically and are divided by the corresponding
0.94 measurement value at the transformer. Figure 11 plots the
0.93 diversity  factors  for  phase  L1.  Similar  results  are
observed for the other phases. With values higher than
0.92
0.9 all considered harmonics have a high diversity factor
| 0.91 |     |     |      |     | and consequently a weak phase cancellation.  |     |     |     |     |     |     |     |     |
| ---- | --- | --- | ---- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | 5   | 7   | 9 11 | 13  |                                              |     |     |     |     |     |     |     |     |
Harmonic Order

Fig. 11 Diversity Factor

https://doi.org/10.24084/repqj12.460 704 RE&PQJ, Vol.1, No.12, April 2014

1.04
1.035
1.03
1.025
1.02
1.015
1.01
1.005
1
5 7 9 11 13
Harmonic Order
Fig. 12 Summation Exponent for Current Harmonics
The summation exponent (h) is determined by
solving the following non-linear equation iteratively:
n (h)
I(h) (h)  I(h) (4)
VEC i
i1
A summation exponent (h) = 1 corresponds to a
diversity factor of k(h) = 1 and represents no cancellation.
p
In case of perfect cancellation (k(h) = 0) the summation
p
exponent becomes infinite.
Figure 12 shows the distribution of summation exponent
calculated for the time span when all inverters were
PLC system with a larger number of channels should be
connected. With values almost equal to (h) = 1 the weak used. Nevertheless ensuring a proper operation of the
phase cancellation effect is confirmed. In case of multiple widely used narrow-band PLC communication systems
inverters with similar behaviour a summation exponent of should be carefully considered in the current
(h) = 1 should be used for all harmonics instead of the standardization work in IEC SC77A in terms of
recommended values e.g. in IEC 61000-3-14. compatibility levels and emission limits for the frequency
range 2 – 150 kHz. Further details on those issues can be
found in [5].
3. Analysis of higher frequency emission
Figure 14 shows the current-spectrum of a large
All following plots are limited to 100 kHz, because the inverter (Inv 9) and a small inverter (Trck 4). Even
frequency range above 100 kHz doesn’t contain any though both inverters emit at different frequencies (large
considerable emission. Figure 13 presents the 5-Hz- inverter at 3 kHz, 6 kHz and 9 kHz; small inverter at
spectrum of the busbar voltage in phase L1. The other 10 kHz, 16 kHz or 25 kHz) both spectra show current
phases show a similar behaviour. Several peaks indicate components at all higher frequencies which exist in the
the switching frequencies of the inverters and their voltage spectrum (Figure 13). This means a significant
respective harmonics. All large inverters of the installation interaction between all inverters, which is caused by the
have a similar switching frequency of 3 kHz. The 2nd relatively small input impedance of inverters. At higher
emission band at 6 kHz and the 3rd emission band at 9 kHz frequencies (usually above 3 - 5 kHz) the total impedance
are also clearly visible. The peaks at 10 kHz, 16 kHz and is more and more dominated by the input circuits of the
25 kHz are caused by the small inverters. This confirms inverters (usually the EMC filters) that subsequently act
the common manufacturer practice to use higher switching more and more as sink for the higher frequency emission.
frequencies in case of smaller rated power of the inverter.
Figure 15 shows the voltage level depending on time
The “hills” between 40 kHz and 80 kHz were caused by and frequency as spectrogram for the time interval of
a narrow band power-line-communication-system (PLC) coordinated inverter switching (cf. Table I). Every
with eight channels for transmitting metering information. switch-off of an inverter decreases the emission level of
This emission is called intentional, because it is the corresponding switching frequency and their
intentionally injected by the network operator. Compared harmonics. The emission of the large inverters disappears
to other narrow band PLC systems with less channels completely after switching off Inv 9 (7:10 min).
(down to two) the system in this case is more robust, Especially the switch-off at 7:35 min results in a
because if one or more channels are disturbed, the system significant decrease of emission in a wide range. This
can still switch to another channel for communication. particular small inverter has a switching frequency of
Especially for environments, where other disturbances in 24 kHz including a sub-harmonic at 12 kHz. Moreover
this frequency range has to be expected, a more robust also the 2nd emission band at 48 kHz and the 3rd emission
tnenopxE
noitammuS
Fig. 13 Voltage spectrum at busbar in phase L1
Fig. 14 Current spectrum for individual large inverter (Inv 9)
and small inverter (Trck 4) both in L1
https://doi.org/10.24084/repqj12.460 705 RE&PQJ, Vol.1, No.12, April 2014

Fig. 16a Voltage and current of Inv 9 at 3 kHz during
switching off and on all inverters (L1)

Fig. 15 Spectrogram of the voltage in L1 during
coordinated switching (cf. to table I)
band at 72 kHz can be clearly identified. This example
shows how coordinated switching can help to identify the
| individual   | emission  |        | for  a  | particular  | inverter.  | The        |     |     |     |     |     |     |
| ------------ | --------- | ------ | ------- | ----------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| spectrogram  | also      | shows  | that    | every       | single     | switching  |     |     |     |     |     |     |
operation leads to a short, momentary increase of emission
in the voltage.
The collective behaviour of the large inverters at their

switching frequency is analysed in detail by means of the
Fig. 16b Instaneous power of Inv 9 at 3 kHz during
time characteristic of busbar voltage and current of Inv 9 at
switching off and on all inverters (L1)
| 3 kHz  (Figure 16).  |     | A   | 600-Hz-band  | is  | used,  | because  it  |                                            |     |     |     |                |     |
| -------------------- | --- | --- | ------------ | --- | ------ | ------------ | ------------------------------------------ | --- | --- | --- | -------------- | --- |
|                      |     |     |              |     |        |              | inverters at 3 kHz and levels about 130 dB |     |     |     |  (ca. 3 V) in  |     |
reflects almost the total signal energy for PV inverters at  µV
voltage. At higher frequencies a set of inverters (same
switching frequency. The voltage decreases stepwise with
each  switch-off,  while  the  current  increases  in  a  and different types) at one connection point shows a large
interaction. Most of the emitted currents will stay within
comparable way. After the last inverter (Inv 9; 7:10 min)
|            |           |       |              |     |       |               | the  installation  | and  doesn’t  |     | propagate  | into  the  | grid.  |
| ---------- | --------- | ----- | ------------ | --- | ----- | ------------- | ------------------ | ------------- | --- | ---------- | ---------- | ------ |
| has  been  | switched  | off,  | the  levels  | of  | both  | voltage  and  |                    |               |     |            |            |        |
Coordinated switching can be a useful tool to identify
current suddenly drop to background noise levels. Figure
emission of individual inverters.
14b illustrates that Inv 9 can be characterized in terms of
its  emission  at  switching  frequency  as  power  source.  The paper is limited to a few aspects of the work only.
Looking on the emission at same operating states before
Many more experiments were carried out in order to
(0:00 min) and after (35:00 min) switching, the relation of  analyse e.g. the impact of PV inverters on the PLC signal
voltage  and  current  at  3 kHz  behaves  different.  After  characteristics  (damping  effects)  or  the  transfer
complete switching on, the voltage is considerably smaller,  characteristic of a cable for higher frequency emission.
while current is significantly higher than before switching
References
inverters off. This behaviour is not yet fully explainable,
but may increase complexity of modelling approaches.  [1] M. Klatt, J. Meyer, P. Schegner, A. Koch, J. Myrzik, T.
Darda, G. Eberl, “Emission Levels Above 2 kHz – Laboratory
  Results  and  Survey  Measurements  in  Public  Low  Voltage
4. Conclusion and Outlook
Grids”, in CIRED conference on Electricity Distribution 2013,
paper no. 1168.
| The  | paper  studies  |     | the  characteristics  |     | of  | low  order  |     |     |     |     |     |     |
| ---- | --------------- | --- | --------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
[2] M. Klatt, A. Dorado, J. Meyer, J. Backes, R. Li, “Power
| harmonics  | and  | higher  | frequency  | emission  |     | of  a  large  |                   |            |        |             |              |     |
| ---------- | ---- | ------- | ---------- | --------- | --- | ------------- | ----------------- | ---------- | ------ | ----------- | ------------ | --- |
|            |      |         |            |           |     |               | Quality  Aspects  | of  Rural  | Grids  | with  High  | Penetration  | of  |
photovoltaic installation, consisting of multiple small and
|     |     |     |     |     |     |     | Microgeneration,  | mainly  | PV-installations”,  |     | in  | CIRED  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ------------------- | --- | --- | ------ |
large sized inverters.  conference on Electricity Distribution 2011, paper no. 0273.
[3] D. Gallo, A. Testa, J.C. Hernandez, I. Papic, B. Blazic, J.
The low order harmonics have a predominant 5th and 7th
|     |     |     |     |     |     |     | Meyer,  “Case  | Studies  | on  Large  | PV  Plants:  | Harmonic  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ---------- | ------------ | --------- | --- |
harmonics, both in current and voltage. Current harmonics  Distortion, Unbalance and their Effects”, in IEEE PES General
| strongly depend on the voltage distortion, but also on the  |     |     |     |     |     |     | Meeting 2013.  |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
setting  of  the  cos(P)-control.  Diversity  factor  and  [4]  G.  Chicco,  J.  Schlabbach,  F.  Spertino,  “Operation  of
Multiple Inverters in Grid-Connected Large Size Photovoltaic
summation exponent indicate a weak phase cancellation
Installations”, in CIRED conference on Electricity Distribution
effect for large inverters, which consequently means that a
2009, paper no. 0245.
(h) = 1
| summation    | exponent  |                 |            | should      | be  used   | for  all   |                  |               |     |              |             |     |
| ------------ | --------- | --------------- | ---------- | ----------- | ---------- | ---------- | ---------------- | ------------- | --- | ------------ | ----------- | --- |
|              |           |                 |            |             |            |            | [5]  CENELEC     | SC205A        | TF  | EMI:  Study  | Report      | on  |
| harmonics    | in  such  | installations.  |            | All         | inverters  | have  a    |                  |               |     |              |             |     |
|              |           |                 |            |             |            |            | Electromagnetic  | Interference  |     | between      | Electrical  |     |
| significant  | emission  |                 | at  their  | respective  |            | switching  |                  |               |     |              |             |     |
Equipment/Systems in the frequency Range below 150 kHz,
| frequencies. The highest emission is caused by the large  |     |     |     |     |     |     | April 2013.  |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |

https://doi.org/10.24084/repqj12.460 706 RE&PQJ, Vol.1, No.12, April 2014