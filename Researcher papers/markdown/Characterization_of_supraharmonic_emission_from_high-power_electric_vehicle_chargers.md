  CIRED workshop on E-mobility and power distribution systems

Porto, 2-3 June 2022

Paper n° 1158

CHARACTERIZATION OF SUPRAHARMONIC EMISSION FROM
HIGH-POWER ELECTRIC VEHICLE CHARGERS

Tim SLANGEN, Vladimir (cid:251)UK, Sjef COBBEN
TU Eindhoven - The Netherlands
t.m.h.slangen@tue.nl

Erik DE JONG
KEMA Labs - The Netherlands
erik.dejong@kema.com

ABSTRACT

The increasing number of high-power electric vehicle (EV)
charging  stations  in  electricity  grids  introduces  new
challenges for the grid operators. Not only the high power
demand  of  the  chargers  has  an  impact  on  the  grids,  the
devices  can  also  be  a  source  of  supraharmonic  (2-150
kHz) emissions that have several unwanted effects. In this
research, an advanced set-up is developed to characterize
the supraharmonic emission of high-power EV chargers to
find the influencing parameters. Two chargers with a 175
kW rating are tested on a wide range of DC-voltage and -
current setpoints and for different AC grid conditions to
obtain a representative assessment of the behaviour of the
chargers  under  different  operation  conditions.  The  main
conclusion  is  that  the  supraharmonic  emission  of  the
chargers is highly dependent on the DC output voltage and
that  multiple  chargers  may  interact  with  each  other,
resulting in a slow time-varying beating phenomenon. The
findings support the understanding of the supraharmonic
emission from EV fast chargers and help in assessing the
impact they can have on the grid.

1. INTRODUCTION

The  number  of  high-power  or  fast-charging  stations
(FCSs) for electric- vehicles, busses and trucks (EVs) in
distribution  grids  is  developing  to  accommodate  the
growing  demand  for  a  comprehensive  fast-charging
infrastructure [1]. Due to their high power demand, typical
locations have multiple units of up to 350 kW to avoid long
charging times, FCSs can have an impact on the grid and
require  a  strong  grid  connection  [2].  Additionally,  FCSs
are large switching power electronic devices and influence
the  quality  of  power  supply  as  they  can  be  a  source  of
harmonic emission and cause resonances [3]. Furthermore,
FCSs  can  be  a  source  of  supraharmonic  (SH)  emissions
[4],  [5].  Supraharmonics  are  waveform  distortions  in
voltage  and  current  between  2  and  150  kHz,  and  are
observed in low- and medium voltage grids [6]. They can
result  in  several  unwanted  effects  and  interference  with
customer equipment and network components [7].
The effect of SHs from FCSs is still under investigation,
and it is unknown how one or multiple FCSs can contribute
to SH emissions in the grid and which factors influence the
emission frequency and amplitude. This information is of
paramount importance for a grid operator, who should be
able to investigate potential effects prior commissioning,
to avoid or mitigate any problems in the

installation.  This  facilitates  the  smooth  integration  of
emission free transport in our electricity system.
This  research  aims  to  provide  a  characterization  of  the
supraharmonic emission from FCSs by testing the chargers
for  different  AC  grid  conditions  and  performing  a
sensitivity  analysis  of  the  charger  parameters.  For  the
chargers, the DC voltage and current setpoints are varied
and different output power settings are obtained.
The contributions of this research are as follows:
-
-

Presentation of the developed test set-up.
Sensitivity  analysis  of  the  SH  emission  to  the  DC-
voltage,  DC-current,  Output  power,  AC-grid
conditions.

-  Assessment of SH interaction
In Section 2, the test set-up and the chargers under study
will  be  presented.  Section  3  will  discuss  the  results
regarding  the  SH  emission  from  the  chargers  and  the
factors influencing it are determined. Interaction between
the  chargers  is  analysed  in  Section  4  and  the  most
important conclusions are given in Section 5.

2. METHODOLOGY

In  this  research,  2  large  FCSs  rated  175  kW  are
experimentally  tested  in  a  controlled  lab  environment.
Using  an  advanced  setup  with  control  over  both  the
chargers and the grid conditions, the FCSs are tested for
various  scenarios.  Using  this  method,  a  quantitative
assessment  of  the  FCS  impact  is  provided,  and  using
sensitivity  analysis  the  different  operation  states  of  the
device are assessed separately. The FCSs operate on a low-
voltage  400V  line-to-line  network  that  is  either  supplied
by a dedicated MV/LV transformer or via a 500 kVA grid
emulator, see Figure 1. The parameters of the chargers that
were  controlled  are:  DC-voltage  (between  460-800Vdc),
output  power  (between  50-175  kW),  and  output  current.
During  all  tests,  the  voltage  and  current  waveforms  are
measured using an oscilloscope / waveform-recorder with
a 16-bit resolution, a sample rate of 1 MS/s, and bandwidth
of 300 kHz. The voltage is measured using 10:1 passive
probes, and the current using flexible Rogowski coils with
a bandwidth of 600 kHz (-3 dB) and 10 mV/A resolution.
The data is post-processed and analysed using MATLAB.
The
the
supraharmonic  components  will  be  further  elaborated  in
this section.

and  grouping  method

calculation

for

CIRED 2022 Workshop

1/5

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:53:27 UTC from IEEE Xplore.  Restrictions apply.

CIRED workshop on E-mobility and power distribution systems

Porto, 2-3 June 2022

Paper n° 1158

(A)

(B)

Figure 1. Measurement set-up, with chargers connected back-to-back directly through a dedicated MV/LV transformer (A)
or via a grid emulator and isolation transformer (B). Voltage and current measurements points are indicated.

Test set-up
This  section  will  provide  an  overview  of  the  different
components  of  the  set-up.  The  measurement  set-up  is  in
the Flex Power Grid Lab (FPGL) of KEMA laboratories in
Arnhem, The Netherlands. Two different set-ups are used,
as presented in Figure 1. The chargers are denoted as FCS
1 and FCS 2 and are connected back-to-back to the same
LV network. In this set-up, FCS 1 will act as a source (AC
to DC mode) whereas FCS 2 will act as sink (DC to AC
mode). The measurements are repeated with these settings
reversed; FCS 2 as source and FCS 1 as sink. This due to
unavailability  of  2  electric  vehicles  (EV)  with  sufficient
high charger power and battery capacity. However, when
using an EV, the state of charge, battery capacity and other
mainly  uncontrollable  parameters  will  determine  the
voltage  and  current  setpoint,  which  makes  obtaining
reproducible  test  results  difficult.  In  this  set-up,  there  is
more controllability compared to using an actual EV as the
voltage and current setpoints can be controlled freely and
can be  contained  for  an  indefinite  amount  of  time.  The
measurements will be based on the combination of the two
chargers operating simultaneously.

In  set-up  A  (Figure  1-A),  the  low-voltage  network  is
supplied  by  a  distribution  11 kV  /  400  V  transformer  of
630 kVA rating. This offers a more realistic connection for
the  chargers, mainly  because  the  impedance  of  the
transformer  is  significantly  lower.  However,  the  voltage
parameters  cannot  be  controlled  and  distortion  from
neighbouring labs might be present on the upstream MV
that propagates to the LV.

The  low-voltage  network  is in  set-up  B (Figure  1-B)
supplied  by  a  500  kVA  grid  emulator  that  offers  full
control  over
the  voltage  waveform  and  eliminates
background  distortion  from  the  upstream  MV  grid  by
building a clean voltage. Harmonics can be added up to 2
kHz and voltage parameters per phase are controlled. An
1.8  MVA  isolation  transformer  is  used  to  convert  the
output of the grid emulator to 400 V line to line and serves
as  isolation  to  avoid  any  interaction  between  the  control
loops of the separate systems.

High-power chargers
Two  FCSs  of  similar  type,  are  used  for  the  tests.  The
specifications of the chargers are presented in Table 1.

Table 1 Charger specifications

Max DC output power
Max DC output current
Output DC voltage range
Power factor
Power conversion efficiency

175 kW
350 A
460-800 V
> 99 %
> 96 %

The  chargers  have  a  rated  power  of  150  kW  over  the
complete  DC  voltage  range.  For  a  DC  voltage  around
600V a higher power of 175 kW is possible. DC voltage
output ranges from 460 to 800 V. The DC output voltage
and  DC  output  current values  are  controlled  via  a
development interface.

DC voltage and current setpoints
Different  combinations  of  output  power  level and  DC
output  voltage are  obtained  according  to the  9  different
setpoints  as  shown  in  Table  2.  The  chargers  operate  on
each setpoint for 15 minutes and a measurement snapshot
is taken every 10 seconds. Only for 600Vdc the power of
175  kW  is  obtained,  for  460  Vdc  and  800  Vdc  the
maximum  power  is  150  kW  due  to charger  limitations.
Three  steps  in  power  are used,  representing 50,  100  and
150 or 175 kW output power. A power flow is initiated by
decreasing  the  voltage  of  the  charger  that  acts  as  a  sink
slightly.  Communicated  protocols  (CCS)  are  overruled
and
(e.g., pre-charge,  closing
contactors) to initiate the charging are performed manually
using the interface.

the  different  steps

Table 2 DC voltage and current setpoints

460 Vdc
600 Vdc
800 Vdc

50 kW
108 Adc
83 Adc
63 Adc

100 kW 150/175 kW
217 Adc
166 Adc
125 Adc

336 Adc
292 Adc
188 Adc

CIRED 2022 Workshop

2/5

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:53:27 UTC from IEEE Xplore.  Restrictions apply.

CIRED workshop on E-mobility and power distribution systems

Porto, 2-3 June 2022

Paper n° 1158

Supraharmonic calculation
The 5 Hz frequency components (cid:1835)(cid:3033) are obtained with the
Fast Fourier transform function of MATLAB, with a 200
ms window. The resulting components are then grouped in
supraharmonic bands (cid:1835)(cid:3046)(cid:3035) of 1 kHz width as

obtaining  148  bands. Similarly,  the  voltage  components
are grouped in (cid:1848)(cid:3046)(cid:3035) bands. The SH emission frequencies of
the chargers under study are identified in the 3-4 kHz and
7-8  kHz  bands and  therefore  the  focus  will  be  on  these
bands  only,  as  no  additional  emission  frequencies  were
identified during the lab tests. The emission spectra of the
chargers are as presented in past research [5]. In the next 2
sections the results based on the tests with set-up A, grid
connected, are presented.

3. RESULTS AND CHARACTERIZATION

Emission in 3-4 kHz band
For  the  emission  in  the  3-4  kHz  band,  the  results  are
described in this subsection. The emission with respect to
the DC voltage is presented in Figure 2. For each subplot
the  power  level  is  fixed  (50,  100,  150  kW)  and  the  DC
voltage is varied. It is observed that for an increasing DC
voltage, there is a slight decrease in emission in this band.
The  spread  is  however  quite  wide,  the  emission  ranges
from  approximately  5  to  13  A  (75th percentiles).  When
analysing the  mean  values,  a  decrease  in  emission  is
observed  for  each  increase  in  DC-voltage.  The  relation,
however,  is  not  constant  and  differs  depending  on  the
output power.

Figure 3 SH emission in 3-4 kHz band vs. output power,
for different DC voltages

Based on the mean values, the emission increases first for
460 V and then decreases for increasing power. For 600 V
the emission decreases for increasing power, and for 800V
it increases and then decreases. No clear relation is found
between the emission in the 3-4 kHz band and the output
power, and some relation with the output DC voltage, but
due  the  large  overlap  in  values  not  confident enough  to
draw conclusions.

Emission in 7-8 kHz band
Dominant emission is also observed in the 7-8 kHz band.
The  SH  emission with  respect  to  the  DC  voltage is
presented in Figure 4. Note that the y-axes are linked in
this figure. It is observed that the emission is similar for
different output power, and highly dependent on the DC
output voltage of the chargers. For a DC voltage of 460 V
the emission is the lowest (between 0.5 and 0.7 A). With
increasing  DC  voltage,  the  emission  in  this  band  also
increases. For 600 V the emission approximately doubles
and  is  between  1.2  and  1.4  A.  For  a  further  increased
voltage of 800 V the values double again compared to the
600 V values. The emission is now between 2.2 and 2.4 A.

Figure 2 SH emission in 3-4 kHz band vs. DC voltage, for
different output power.

In Figure 3 the mission in the 3-4 kHz band is plotted with
respect  to  output  power  instead  of  DC  voltage.  The  DC
voltage is fixed for the different subplots, and the output
power  is  varied.  Again,  the  range  in  which  the  emission
amplitudes occur is quite wide (from 5 to 13 A based on
the 75th percentiles) and there is no clear relation between
the emission and the output power.

Figure 4 SH emission in 7-8 kHz band vs. DC voltage, for
different output power.

CIRED 2022 Workshop

3/5

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:53:27 UTC from IEEE Xplore.  Restrictions apply.

  CIRED workshop on E-mobility and power distribution systems

Porto, 2-3 June 2022

Paper n° 1158

For the 7-8 kHz band and 150 kW power this difference is
illustrated in Figure 6. On the left part of the figure the SH
voltage disturbance in the 7-8 kHz band is presented for
set-up A (grid connected) and in the right part of the figure
for set-up B with the grid emulator (GE) included.

For  the  different  power  levels,  the  emission  is  similar.
When  analysing  the  emission  with  respect  to  the  power
level,  Figure  5  is  obtained.  Note  that  the  y-axes  are  not
linked in this figure, for improved readability of the small
differences. It is observed that the emission in the band is
also  slightly  dependent  on  the  output  power  of  the
chargers. The effect is less compared to the output voltage,
an increase of maximum 0.2 A is observed when fixing the
DC voltage and increasing the power level. This implies
that  the  relative  emission,  as  scaled  to  the  fundamental
current, will decrease for an increasing power, whilst the
absolute values will slightly increase.

Figure 5 SH emission in 7-8 kHz band vs. output power,
for different DC voltages

Effect of grid emulator (set-up B)
All tests are repeated in set-up B, where the low-voltage
network is supplied by the grid emulator. The same voltage
and current setpoints as presented in Table 2 are used for
the  tests.  This  section  will  discuss  the  similarities  and
differences between the tests with set-up A and set-up B.

Regarding  the  emission  of  the  chargers,  the  same  SH
emission frequencies are identified. For the 3-4 kHz band,
the  emission  shows  the  same  behaviour  as  presented  in
Figure 2 and 3 with almost identical emission amplitudes
for the different setpoints. Hence, this result is not shown
in a figure. The same holds for the emission in the 7-8 kHz
band, an identical behaviour is observed for the different
voltage  and  current  setpoints,  with  similar  emission
amplitudes and the similar relation between emission and
input power or DC-voltage is observed as in Figures 4 and
5. Hence this result is not shown here.

The main difference between the emission in set-up A and
set-up B is the effect on the voltage. Both set-ups will give
a  different  apparent  upstream  impedance,  that  is  defined
by the MV/LV transformers’ short circuit rating, and the
upstream elements (MV grid or grid emulator). Due to this,
a similar current emission results in a different effect on
the voltage.

Figure 6 SH Voltage in 7-8 kHz band vs. DC-voltage, for
grid connected (left) and grid emulator (right) set-ups and
an output power of 150 kW

It is observed that the disturbance on the voltage shows a
similar trend as in Figure 4, for an increasing DC-voltage,
the disturbance increases. For the steps 460 to 600 V and
600 to 800 V the voltage disturbance almost doubles, and
ranges between 0.5 and 3 V for set-up A.
For set-up B, the SH voltage disturbance shows a similar
trend, but at a higher amplitude. Note the y-axes that are
linked  for  easy  comparison.  Whereas  on  the  grid
connection the voltage disturbances remain below 3 V, for
the  grid  emulator  set-up  the  disturbances  increase  up  to
9V. In general, the SH voltage in the 7-8 kHz band is 3
times higher in test set-up B.

This  is  an  important  finding  that  shows  the  effect  of  the
grid impedance on the voltage disturbances. A higher grid
impedance will result in a higher voltage disturbance for a
similar emission. Whilst the fundamental or short-circuit
impedance  of  the  transformers  is  similar,  the  impedance
for higher frequencies will highly depend on the X/R ratio
of  the  transformers.  The  short  circuit  or  equivalent
impedance (cid:1852)(cid:3046)(cid:3030) of a transformer is either given or can be
derived from an otherwise specified short-circuit voltage
ratio (cid:1847)(cid:3038). This ratio is expressed as the percentage of the
 needed on the primary side to achieve
nominal voltage (cid:1847)(cid:3015)
the  nominal  current  of  the  transformer  on  the  secondary
side,  given  that  the  secondary  side  is  in  a  short-circuit
condition.  The  frequency  dependent  impedance  of  a
transformer can be estimated by scaling the inductive part
of the transformer short circuit impedance with frequency
as

(cid:1852)(cid:3032)(cid:3046)(cid:3047)

((cid:1858)) = |(cid:1844)(cid:3046)(cid:3030)

+ (cid:1862) (cid:1668) (cid:1858) (cid:1668)

(cid:1850)(cid:3046)(cid:3030)
50

|

with  frequency  (cid:1858)  and    (cid:1844)(cid:3046)(cid:3030)  and  (cid:1850)(cid:3046)(cid:3030)  the  short-circuit
resistance and the short circuit reactance respectively [8].

CIRED 2022 Workshop

4/5

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:53:27 UTC from IEEE Xplore.  Restrictions apply.

  CIRED workshop on E-mobility and power distribution systems

Porto, 2-3 June 2022

Paper n° 1158

4. INTERACTION

As  observed  in  the  results  for  the  3-4  kHz  band,  the
emission amplitude stretched across a wide range. This is
further analysed by taking snapshots of a longer duration,
at a lower sample rate and a shorter FFT window (affecting
the amplitudes). It is found that the emission in this band
is  time-varying.  The  result  in  shown  in  Figure  7  for  the
setpoint 100 kW at 600 Vdc. The emission varies with a
period  T  of  approximately  0.5  seconds,  which  might  be
due  to  the  emission  from  FCS  1  and  FCS  2  that  are  at
approximately  the  same  frequency,  resulting  in  an
additional component at the difference of the frequencies
|  as described in [9], in this
according to  (cid:1858)(cid:3029)(cid:3032)(cid:3028)(cid:3047)
case  around  2  Hz.  This  slight  difference  in  switching
frequency  of  the  individual  converters  results  in  an
amplitude modulation of the emission in the 3-4 kHz band.
This interaction should be considered when assessing the
emission from installations with similar devices emitting
supraharmonics.

= |(cid:1858)(cid:2869) (cid:3398) (cid:1858)(cid:2870)

quantitative  assessment  of
the  expected  voltage
disturbance that can be caused by an installation emitting
supraharmonics.

Due  to  the  interaction,  no  quantitative  characterization
could be made for the emission in the 3-4 kHz band. Future
test  should  take  this  into  account  and  preferably  use
separated grid connections to avoid this issue. However, in
a real grid situation with multiple chargers connected, it is
expected  that  the  same  effect  will  occur.  This  should  be
considered  when  assessing  the  maximum  emission  from
an installation with fast charging stations.

ACKNOWLEDGMENTS

This research is part of the project TEPQEV and supported
by  Topsector  Energy-subsidy  of  the  Dutch  ministry  of
Economic Affairs and Climate.

REFERENCES

[1]  ElaadNL,

‘Elektrisch

-
rijden
Elektrificatie van personenauto’s tot en met 2050 Outlook’,
Oct. 2021.

in  stroomversnelling

[2]  L. Wang, Z. Qin, T. Slangen, P. Bauer, and T. van Wijk,
‘Grid  Impact  of  Electric  Vehicle  Fast  Charging  Stations:
Trends,  Standards,  Issues  and  Mitigation  Measures  -  An
Overview’, IEEE Open J. Power Electron., vol. 2, pp. 56–
74, 2021.

[3]  Y.  Sun,  E.  C.  W.  de  Jong,  V.  Cuk,  and  J.  F.  G.  Cobben,
‘Harmonic  resonance  risk  of  massive  ultra  fast  charging
station  grid  integration’,  in  2018  18th  International
Conference on Harmonics and Quality of Power (ICHQP),
Ljubljana, May 2018, pp. 1–6..

[4]  F.  Chen  et  al.,  ‘Survey  of  Harmonic  and  Supraharmonic
Emission of Fast Charging Stations for Electric Vehicles in
China and Germany’, in 26th International Conference on
Electricity  Distribution
2021),  Geneva,
Switzerland, 2021, p. 5.

(CIRED

[5]  T. Slangen and S. Bhattacharyya, ‘Determining the Impacts
of Fast-Charging of Electric Busses on the Power Quality
Based  on  Field  Measurements’,  in  26th  International
Conference  on  Electricity  Distribution  (CIRED  2021),
Geneva, Switzerland, Sep. 2021, p. 5.

[6]  E. O. A. Larsson, M. H. J. Bollen, M. G. Wahlberg, C. M.
Lundmark,  and S.  K.  Rönnberg, ‘Measurements  of  High-
Frequency  (2–150  kHz)  Distortion
in  Low-Voltage
Networks’, IEEE Transactions on Power Delivery, vol. 25,
no. 3, pp. 1749–1757, Jul. 2010.

[7]  S.  K.  Rönnberg  et  al.,  ‘On  waveform  distortion  in  the
frequency range of 2 kHz–150 kHz—Review and research
challenges’, Electric Power Systems Research, vol. 150, pp.
1–10, Sep. 2017.

[8]  R.  Stiegler,  J.  Meyer,  P.  Schegner,  and  D.  Chakravorty,
‘Measurement of network harmonic impedance in presence
of  electronic  equipment’,  in  2015  IEEE  International
Workshop  on  Applied  Measurements  for  Power  Systems
(AMPS), Aachen, Germany, Sep. 2015, pp. 49–54.

[9]  (cid:55)(cid:17)(cid:3) (cid:54)(cid:79)(cid:68)(cid:81)(cid:74)(cid:72)(cid:81)(cid:15)(cid:3) (cid:55)(cid:17)(cid:3) (cid:89)(cid:68)(cid:81)(cid:3) (cid:58)(cid:76)(cid:77)(cid:78)(cid:15)(cid:3) (cid:57)(cid:17)(cid:3) (cid:251)(cid:88)(cid:78)(cid:15)(cid:3) (cid:68)(cid:81)(cid:71)(cid:3) (cid:54)(cid:17)(cid:3) (cid:38)(cid:82)(cid:69)(cid:69)(cid:72)(cid:81)(cid:15)(cid:3) (cid:181)(cid:55)(cid:75)(cid:72)(cid:3)
Propagation  and  Interaction  of  Supraharmonics  from
Electric  Vehicle  Chargers
in  a  Low-Voltage  Grid’,
Energies, vol. 13, no. 15, p. 3865, Jul. 2020

Figure 7 SH emission in 3-4 kHz band, amplitude (top) and
spectrogram (bottom), 100 kW/600 V setpoint, 5 seconds.

5. CONCLUSION

the

this

that

factors

research

influence

In
the
supraharmonic  emission  from  fast  charging  stations  are
studied.  A  test  set-up  is  developed  and  different  voltage
and  current  setpoints  are  used  to  obtain  a  representative
insight into the emission of the chargers for the operating
range.  It  is  found  that  part  of  the  SH  emission  is  highly
sensitive to the DC-voltage, which shows a linear relation.
The output current or, resulting output power has a lesser
impact on the emission, but further research on a different
test set-up should conclude on this matter.

The  supraharmonic  emission  from  the  two  or  more
identical chargers (or other devices) can cause interaction,
resulting in a slow, time-varying emission characteristic.

is

to

found

influence

The  grid  connection
the
supraharmonic  voltage  distortion  due  to  the  different
impedance.  The
frequency
dependent
supraharmonic  current  components
remain  mostly
constant in amplitude.  Further research should focus on
the characterization of the high-frequency impedances of
transformers  and  other  network  components,  to  make  a

network

CIRED 2022 Workshop

5/5

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:53:27 UTC from IEEE Xplore.  Restrictions apply.

