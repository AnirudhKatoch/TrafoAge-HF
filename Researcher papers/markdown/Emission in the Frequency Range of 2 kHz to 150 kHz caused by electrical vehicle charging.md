Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
Emission in the Frequency Range of 2 kHz to
150 kHz caused by electrical vehicle charging

Stefan Schöttke1, Jan Meyer1, Peter Schegner1, Sebastian Bachmann2
1 Technische Universität Dresden, Dresden, Germany, stefan.schoettke@tu-dresden.de
2 Belectric Drive, Kitzingen, Germany, Sebastian.bachmann@belectric.com
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Abstract—This paper studies the conducted emission in the  interferences between devices [2]. During the last years the
range from 2 kHz to 150 kHz during the charging cycle of electric  number of utilities using the frequency range between 2 kHz
vehicles. It provides an overview about the necessity of dealing  and  150 kHz  for  narrowband PLC  applications,  e.g.  meter
with these emissions and their influencing factors. A test stand  reading, has been growing. It has to be guaranteed that the
which allows measuring the charging of electric vehicles under  “unintentional” emission (e.g. by BEV chargers) is lower than
| controlled  | conditions  |     | is  described  | and  | measurements  |     | and  |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | -------------- | ---- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
the intentional emission by the PLC in order to ensure its
analysis methods are presented. The emissions of selected vehi-
proper functionality.
cles during the charging cycle at the test stand and in the low
voltage grid are shown and compared. The dependencies between  An increasing number of cases is reported, in which higher
the charging state and the main emission frequency as well as  frequency emission in a network, e.g. injected by PV inverters
between  the  charging  state  and  the  emission  level  at  this  or  active  frontend  inverters,  lead  to  malfunction  of  other
frequency are presented.
devices [3, 4] or erroneous measurements of electronic energy
meters [5]. This higher frequency emission can also cause
Index Terms—electric vehicles, test equipment, measurement,  additional losses in the equipment and subsequently lead to
switching frequency, harmonic analysis  additional heating, which can result e.g. in faster aging [6].
|     |     |     |              |     |     |     |     | Especially  | devices  | with  | a  negative  | impedance  |     | frequency  |
| --- | --- | --- | ------------ | --- | --- | --- | --- | ----------- | -------- | ----- | ------------ | ---------- | --- | ---------- |
|     |     | I.  | INTRODUCTION |     |     |     |     |             |          |       |              |            |     |            |
characteristic (e.g. shunt capacitors in DC-links of rectifier
| Standards  |     | like  IEC  | 61000-3-2  |     | regulate  | the  harmonic  |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---------- | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
circuits) are affected. Moreover the higher frequency emission
emission of electronic devices in the low frequency range up
can cause flicker problems when using light dimmers [7] and
to  2.5 kHz.  The  manufacturers  of  larger  equipment  like  annoying noise due to mechanical resonances. E.g. one of the
photovoltaic  (PV)  inverters  or  charging  units  for  battery  analysed vehicles has a switching frequency of about 10 kHz.
| electric  | vehicles | 1  (BEV)  | or  | plug-in  | hybrid  | ones,  | use  |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | -------- | ------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
It generated a well audible noise due to the stimulation of a
| technologies  |     | with  switched  |     | power  | electronics  | like  | active  |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ------ | ------------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
mechanical resonance within the BEV.
power factor correction (aPFC) or PWM controlled rectifiers
in order to keep the defined limits and increase the efficiency  In order to ensure failure-free operation and service of all
equipment and devices connected to the grid, it is essential to
of the devices [1]. These technologies produce emission in the
|         |            |        |          |          |      |           |     | study  the  | sources,  | propagation  |     | and  effects  |     | in  the  higher  |
| ------- | ---------- | ------ | -------- | -------- | ---- | --------- | --- | ----------- | --------- | ------------ | --- | ------------- | --- | ---------------- |
| higher  | frequency  | range  | between  | 2.5 kHz  | and  | 150 kHz.  | In  |             |           |              |     |               |     |                  |
order  to  ensure  electromagnetic  compatibility  between  the  frequency range. Up to now there are only a few researches
devices  and  to  minimize  interferences,  emission  levels,  known  in  this  area,  e.g.  [8].  The  political  framework  in
compatibility levels and immunity levels have to comply with  Germany promotes both, the increase of PV installations as
|     |     |     |     |     |     |     |     | well  as  a  | number  | of  | charging  | BEVs.  | Both  | of  them  use  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | --------- | ------ | ----- | -------------- |
the following concept:
|     |           |     |                |     |           |     |     | technologies  | like  | aPFCs  | or  | PWM  and  | emit  | at  higher  |
| --- | --------- | --- | -------------- | --- | --------- | --- | --- | ------------- | ----- | ------ | --- | --------- | ----- | ----------- |
|     | Emission  |     | Compatibility  |     | Immunity  |     |     |               |       |        |     |           |       |             |
<  <  frequencies.  Therefore,  detailed  analysis  of  the  higher
|     | level  |     | level  |     |     | level  |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
frequency spectra in the grids is needed, i.e. how the emission
is generated, how the emission of multiple devices adds, how
Whereas the frequency range up to 2 kHz is fully covered by
the emission propagates in the grid and finally what is affected
| standards,  | there  | are  only  | a   | few  standards  |     | for  the  | higher  |           |            |       |        |          |     |              |
| ----------- | ------ | ---------- | --- | --------------- | --- | --------- | ------- | --------- | ---------- | ----- | ------ | -------- | --- | ------------ |
|             |        |            |     |                 |     |           |         | by  this  | emission.  | This  | paper  | focuses  | on  | the  source  |
frequency range up to 150 kHz. Compatibility levels up to
9 kHz  are  described  only  informatively  in  IEC 61000-2-2,  characterisation of BEVs in terms of its  higher  frequency
emission.
immunity limits are in development (IEC 61000-4-19) and
emission  limits  exist  just  for  a  few  specific  devices  and  Because  of  the  present  rare  spreading  of  BEVs  in
technologies,  e.g.  induction  stoves  or  mains  signalling  on  Germany, the effects of the increased penetration of charging
power line communication (PLC). There is still a large gap in  BEVs on power quality has to be studied by simulations. The
the standards (no normative compatibility levels, no emission
simulations have to cover different grids (e.g. rural and urban)
| limits  | for  many  | types  | of  devices),  |     | which  | can  result  | in  |     |     |     |     |     |     |     |
| ------- | ---------- | ------ | -------------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
with a different penetration of the BEVs. Therefore adequate
models for the higher frequency emission of BEVs are needed.

The modelling requires measuring data of real BEVs under
1 In this paper BEV terms all cars, vans etc. with general admission.
Lightweight vehicles, electrical bikes etc. are excluded.
| 978-1-4799-3226-9/14/$31.00 © 2014 IEEE |     |     |     |     |     |     |     | 620 |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore.  Restrictions apply.

Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
different conditions. In a first step measurements should be
carried out in a reproducible, controlled environment. Based
on these measurements the respective models are developed
and finally verified by measurements in real networks with
uncontrolled conditions.
At the beginning the paper describes a test stand, which
was used to characterise the higher frequency emission of
BEV chargers under laboratory conditions in detail. The next
chapter discusses the measurement results from the test stand
for different BEVs. Finally the laboratory measurements are
compared with measurements of the same BEVs charged in

real low voltage grids.  Figure 1.  Scheme of the test stand for evaluating perturbations of BEVs and
photovoltaic inverters. (a) signal generator, (b) 3 power amplifiers,
II.  METHODOLOGY OF ANALYSIS  (c) changeable impedance, (d) PV simulator, (e) PV inverters, (f) switch board
A. Test stand
| During  | measurements  |     | in  | real  | low  voltage  | grids  | it  is  |     |     |     |     |     |
| ------- | ------------- | --- | --- | ----- | ------------- | ------ | ------- | --- | --- | --- | --- | --- |
impossible to control the conditions like voltage distortion or
grid impedance. Moreover the mentioned factors could change
unexpectedly and the results would not be reproducible at all.
Hence, a test stand for measuring the charging cycle of BEVs
in a defined environment was built.
As shown in fig. 1 it consists of a 3-phase programmable
signal source (a), a 3-phase power amplifier of 45 kVA (b) and
a variable impedance used as a grid emulator (c). A 10 kW-
PV-simulator (d) with three different PV inverters (f) was
designed for future measurements of the combined operation
of BEVs and PV inverters. Two charging points allow the
| simultaneous  |      | charging    | of  two  | BEVs.     | A         | switch             | board  (f)  |     |     |     |     |     |
| ------------- | ---- | ----------- | -------- | --------- | --------- | ------------------ | ----------- | --- | --- | --- | --- | --- |
| connects      | all  | components  |          | and       | provides  | interfaces         | for         |     |     |     |     |     |
| measurement   |      | equipment.  | In       | addition  | to        | higher  frequency  |             |     |     |     |     |     |
emission  the  test  stand  is  also  used  to  characterise  the
equipment  in  terms  of  low  order  harmonic  emission  and  Figure 2.  Analysis of the no-load behavior of the test stand.
voltage. These are the switching frequency and its harmonic
unbalance.
caused by signal source itself. The oscillation of the spectra
| There  | are  | several  | standards  | for  | connecting  |     | BEVs  to  |     |     |     |     |     |
| ------ | ---- | -------- | ---------- | ---- | ----------- | --- | --------- | --- | --- | --- | --- | --- |
and levels around 51.2 kHz is an aliasing effect of the PWM-
charging stations. In Germany the most common ones are the
control of the amplifiers generated by the FFT analysis and
so-called type-1- and type-2-connectors. SchuKo, the German
aggregation in time (cp. chapter II-D). The small emission
standard plug for low voltage devices is used mostly by older
|     |     |     |     |     |     |     |     | lines  originate  | from  | the  digital-analogue-converter  |     | and  are  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | -------------------------------- | --- | --------- |
vehicles and for fall-back-charging if type-1 or type-2-sockets  considerably damped by connecting any load to the amplifier.
are not available. All three types are supported by the test  These “idle emission” can be easily identified and will be
| stand.  But  | the  | charging  | current  | can  | only  | be  individually  |     |     |     |     |     |     |
| ------------ | ---- | --------- | -------- | ---- | ----- | ----------------- | --- | --- | --- | --- | --- | --- |
excluded from the analysis.
adjusted for each car via a computer interface, if the type-1- or
| type-2 connectors are used.  |     |     |     |     |     |     |     | B. Analysed vehicles  |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
Until now the charging characteristic of 20 different types
| The  | variable  | impedance  |     | consists  | of  | several  | discrete  |     |     |     |     |     |
| ---- | --------- | ---------- | --- | --------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
of BEVs was measured:
| combinable  | RL-series-elements.  |     |     | It  | is  used  | for  varying  | the  |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --------- | ------------- | ---- | --- | --- | --- | --- | --- |
short circuit power of the source. Because it was designed for
  6 in public low voltage networks only
flicker and low order harmonic analysis, the usability for the
  8 at the test stand only
higher frequency range is limited. The use of series elements
  6 both in low voltage networks and in the laboratory.
| results  | in  too  | high  | impedances  |     | at  higher  | frequencies.  |     |     |     |     |     |     |
| -------- | -------- | ----- | ----------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- |
Therefore,  these  impedance  is  replaced  by  external  One aspect of the paper is the comparison of emission
impedances in the future, e.g. as described in IEC 61000-4-7
|     |     |     |     |     |     |     |     | TABLE 1.  | OVERVIEW OF BEV’S AND THEIR BASIC PARAMETERS  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- |
annex B, which reproduce the harmonic network impedance at
| higher frequencies more realistically.  |        |     |          |              |     |        |            |          |         |                     | Max. charging  |     |
| --------------------------------------- | ------ | --- | -------- | ------------ | --- | ------ | ---------- | -------- | ------- | ------------------- | -------------- | --- |
|                                         |        |     |          |              |     |        |            | Vehicle  | Plug    | Rectifier topology  | current        |     |
|                                         |        |     |          |              |     |        |            | BEV1     | Type-2  | 3x single phased    | 31.4 A         |     |
| Fig. 2                                  | shows  | a   | voltage  | spectrogram  |     | of  a  | reference  |          |         |                     |                |     |
|                                         |        |     |          |              |     |        |            | BEV2     | Type-2  | 2x single phased    | 14.5 A         |     |
measurement at the test stand without any load. The signal
|     |     |     |     |     |     |     |     | BEV3  | Type-1  | single phased  | 16.0 A  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | -------------- | ------- | --- |
source was programmed to create an ideal sinusoidal voltage
|     |     |     |     |     |     |     |     | BEV4  | Type-1  | single phased  | 14.6 A  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | -------------- | ------- | --- |
with a RMS value of 230 V and a frequency of 50 Hz. Small
|     |     |     |     |     |     |     |     | BEV5  | SchuKo  | single phased  | 15.9 A  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | -------------- | ------- | --- |
emissions at 51.2 kHz and 102.4 kHz are visible in the output  BEV6  Type-2  single phased  15.4 A

621
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore.  Restrictions apply.

Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
| under  laboratory  |     | conditions  | and  | real  | grid  | conditions.  |     |     |     |     |
| ------------------ | --- | ----------- | ---- | ----- | ----- | ------------ | --- | --- | --- | --- |
Therefore this paper only focuses on the six BEVs measured
in grid and laboratory. Tab. 1 contains an overview of them,
| presenting  | their  | connection  | type  | and  maximum  |     | charging  |     |     |     |     |
| ----------- | ------ | ----------- | ----- | ------------- | --- | --------- | --- | --- | --- | --- |
current.
C.  Impact factors and test setup
It cannot be assumed that the emission in the range of
2 kHz to 150 kHz is constant during the whole charging cycle
of a BEV. Therefore at the beginning of the study possible  Figure 3.  Measuring interval and splitting of the data for FFT analysis
| factors  | with  impact  | on          | the  emission  | were       | identified.  | The      |     |     |     |     |
| -------- | ------------- | ----------- | -------------- | ---------- | ------------ | -------- | --- | --- | --- | --- |
| factors  | can  be       | classified  | into  grid     | depending  | and          | vehicle  |     |     |     |     |
depending ones:
|    | Rectifier topology (including aPFC or PWM  |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 elciheV
modes) and control
|    | Battery charging state                           |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|    | Charging current limitation                      |     |     |     |     |     |     |     |     |     |
|    | Low frequency harmonic distortion (up to 2 kHz)  |     |     |     |     |     |     |     |     |     |
|    | Higher frequency harmonic distortion (2 kHz to   |     |     |     |     |     |     |     |     |     |
150 kHz)
 dirG
|    | Voltage unbalance  |     |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|    | Voltage magnitude  |     |     |     |     |     |     |     |     |     |
|    | Power frequency    |     |     |     |     |     |     |     |     |     |

|    | Grid impedance  |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  Figure 4.  Currrent in L1 during the charging cycle of BEV1 and BEV2 in the
laboratory and in the grid.
The rectifier topology and control are determined by the
manufacturer design and cannot be changed. The charging  IEC 61000-4-7 (see fig. 3). Afterwards an FFT was used to
current can be limited in discrete steps by the charging station,  obtain the frequency spectra in 5 Hz bands. The spectra of all
if type-1 or type-2 connectors are used. The impact factors of  blocks  of  each  measurement  interval  were  averaged  using
RMS method.
the grid can be individually adjusted by the controllable source
used in the test stand.
All higher frequency spectral levels are presented in the
All  changeable  factors  are  covered  during  the  logarithmic unit dB  (dB ), where 120 dB  correspond to
|     |     |     |     |     |     |     |     | μV µA |     | μV  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
measurements at the test stand. At the beginning the whole  1 V and 0 dB  to 1 μV (analog for currents). One decade is
μV
|     |     |     |     |     |     |     | represented by 20 dB (e.g. 100dB |     |  ≙ 100 mV).  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ------------ | --- |
charging  cycle  of  each  vehicle  is  measured  using  ideal  µV
| conditions  | (sinusoidal,  |     | no  unbalance,  | frequency  |     | of  50 Hz,  |     |     |     |     |
| ----------- | ------------- | --- | --------------- | ---------- | --- | ----------- | --- | --- | --- | --- |
III.  RESULTS OF MEASUREMENTS
RMS-value of 230 V, no impedance) in order to analyse the
impact of charging state and rectifier topology (initial test) on  A. Charging cycle characteristic
the higher frequency emission. In a subsequent measurement
Usually a charging cycle consists of different states [9].
the  impact  of  the  grid-dependent  factors  is  analysed.  This  can  be  seen  in  fig. 4,  which  shows  exemplarily  the
| Therefore,  | all  | factors  | are  varied  | according  | to  | predefined  |     |     |     |     |
| ----------- | ---- | -------- | ------------ | ---------- | --- | ----------- | --- | --- | --- | --- |
charging cycle of BEV1 and BEV2 for the grid measurement
schemes within the limits according to IEC 61000-2-2. The
|               |     |                |                 |     |              |        | and  the  measurement  | at  the  | test  stand.  | During  the  grid  |
| ------------- | --- | -------------- | --------------- | --- | ------------ | ------ | ---------------------- | -------- | ------------- | ------------------ |
| measurements  |     | are  repeated  | for  different  |     | impedances.  | If  a  |                        |          |               |                    |
measurement the charging current of BEV1 was limited to
type-1 or a type-2-connector is used, a current limit in discrete
16 A due to the rating of the used charging station. Therefore,
steps is applied while the car is charged another time under
the grid measurement of BEV1 is not completely comparable
ideal conditions.
with the laboratory measurement where no current limitation
This paper presents the results of the  first step of the  was  set.  The  charging  cycle  of  BEV1  consists  for  both
analysis, namely the impact of the topology and the charging  measurements of four different states which are indicated in
state. The impact of the other parameters will be presented in  fig. 4 for the laboratory measurement. In the first two states
the current is kept nearly constant due to the internal limitation
future papers.
of the vehicle (constant current charging). In the remaining
D. Measurement and data handling
two states the current follows an exponential curve, which
The data was recorded with power quality analysers at a  corresponds to a constant  voltage  charging of the internal
sampling  rate  of  1 MS/s  and  a  resolution  of  16  bits.  For  batteries. In contrast, the charging current of BEV2 is constant
reducing the amount of data, the raw data was recorded every  for most of the time, but interrupted for several minutes.
minute for a variable interval between 1 s and 3.1 s. In order to
Each different charging state including the pauses, which
prevent leakage effects, a digital high pass filter (elliptic, 3rd
is not negligibly short, may require different parameters for a
order, 2 kHz pass band) was applied to the stored datasets. For
|     |     |     |     |     |     |     | simulation  model  | (see  analysis  | of  frequencies  | and  levels  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------- | ---------------- | ------------ |
the higher frequency analysis the data of each measurement
|           |      |        |               |         |            |     | below).  Therefore,  | the  moment  | of  transitions  | between  the  |
| --------- | ---- | ------ | ------------- | ------- | ---------- | --- | -------------------- | ------------ | ---------------- | ------------- |
| interval  | was  | split  | into  200 ms  | blocks  | according  | to  |                      |              |                  |               |
622
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore.  Restrictions apply.

Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
| states  | need  | to  be  | analysed  | individually  |     | for  every  | BEV.  |     |     |     |     |
| ------- | ----- | ------- | --------- | ------------- | --- | ----------- | ----- | --- | --- | --- | --- |
Indications for the transitions may be the passed time or the
| charging state of the battery. For example,  |     |     |     |     |     | for BEV1 the  |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
following was already analysed:
  State 1 → State 2:
|     | Occurs about 30 min after  |     |     |     | start of charging  |     | cycle  |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | ------------------ | --- | ------ | --- | --- | --- | --- |
(independent of charged energy, cp. fig. 4). The small
difference in time can be neglected.
  State 3 → State 4:
|     | For  | both        | cycles                                 | at  | a  transmitted  |     | energy  of  |     |     |     |     |
| --- | ---- | ----------- | -------------------------------------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- |
|     | E    |  ≈ 0.95 · E |  respectively about 25 min before end  |     |                 |     |             |     |     |     |     |
|     | tx   |             | max                                    |     |                 |     |             |     |     |     |     |
of charging.

There is no unique behaviour for all BEVs. The number of
Figure 5.  Spectrogram of the current in phase L1 during the charging cycle
states and their duration are usually different between the
of BEV5 at the test stand
BEVs. Some vehicles have a not negligible duration of the
constant voltage charging state (e.g. BEV1, BEV3). For other
vehicles the constant voltage charging state lasts very shortly
| (e.g. BEV4, BEV6). Others have only  |           |     |         |         |         | states  with constant  |      |     |     |     |     |
| ------------------------------------ | --------- | --- | ------- | ------- | ------- | ---------------------- | ---- | --- | --- | --- | --- |
| current                              | charging  |     | (BEV2,  | BEV5).  | Tab. 2  | summarizes             | the  |     |     |     |     |
charging cycle characteristics of the analysed BEVs.
B. Switching frequency
Concerning the switching frequency the BEVs behave as
differently as they do in their charging cycle characteristic.
This is clearly shown by the difference between fig. 5 and
fig. 6. They present the spectrograms of the charging current
of BEV1 and BEV5. The frequency range in both figures is
limited to 50 kHz because no significant emission is visible
above.
Figure 6.  Spectrogram of the current in phase L1 during the charging cycle
Fig. 5 (BEV5) shows that the switching frequency can  of BEV1 at the test stand.
change abruptly at the transition between two charging states.
The emission is spread over a wide frequency range, which
makes it difficult to estimate the main switching frequency. In
contrast, for BEV1 (fig. 6) a distinctive switching frequency
spread over a narrow frequency range at about 10 kHz can be
| identified.  |     | A  second,  | wider  | band  | at  | around  | 6.5 kHz  is  |     |     |     |     |
| ------------ | --- | ----------- | ------ | ----- | --- | ------- | ------------ | --- | --- | --- | --- |
superimposed. It decreases rapidly after the transition from
constant current charging to constant voltage charging. BEV3
| changes  | its  | switching  | frequency  |     | continuously  |     | during  the  |     |     |     |     |
| -------- | ---- | ---------- | ---------- | --- | ------------- | --- | ------------ | --- | --- | --- | --- |
charging cycle. The frequency shows an inverse exponential
increase over the time. In contrast, BEV2 and BEV4 have no
identifiable switching frequency in the range between 2 kHz
| and  | 150 kHz.  | The  | switching  | frequency  |     | behaviour  | of  the  |     |     |     |     |
| ---- | --------- | ---- | ---------- | ---------- | --- | ---------- | -------- | --- | --- | --- | --- |
analysed BEVs can be classified into the scheme according to

tab. 3.
Figure 7.  Current spectra of several BEVs during constant current charging
Changes  from  narrow  band  emission  to  wide  band  at the test stand
emission and vice versa could not be observed. Analogue to
the PV inverters (e.g. [4]) multiples (harmonics) of the main
|     |           |                                           |     |     |     |     |     | TABLE 3.  | CLASSIFICATION OF SWITCHING FREQUENCY BEHAVIOUR  |                      |     |
| --- | --------- | ----------------------------------------- | --- | --- | --- | --- | --- | --------- | ------------------------------------------------ | -------------------- | --- |
|     | TABLE 2.  | SUMMARY OF CHARGING CYCLE CHARACTERISTIC  |     |     |     |     |     |           |                                                  |                      |     |
|     |           |                                           |     |     |     |     |     |           | Bandwidth                                        | Switching frequency  |     |
Vehicle  Charging States1  Number of states2    none  none
|     | BEV1  |     | I1, I2, U1, U2   |       |     |     | 4   |     |         | constant               |     |
| --- | ----- | --- | ---------------- | ----- | --- | --- | --- | --- | ------- | ---------------------- | --- |
|     | BEV2  |     | I1, interrupted  |       |     |     | 2   |     | narrow  | variable (discrete)    |     |
|     | BEV3  |     |                  | I, U  |     |     | 2   |     |         | variable (continuous)  |     |
|     | BEV4  |     | I, (U)           |       |     |     | 1   |     |         | constant               |     |
|     | BEV5  |     | I1, I2           |       |     |     | 2   |     | wide    | variable (discrete)    |     |
|     | BEV6  |     | I, (U)           |       |     |     | 1   |     |         | variable (continuous)  |     |
1 Const. I resp. const. U charging; brackets imply negligible short duration
  2 Different states needed for modelling
623
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore.  Restrictions apply.

Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
emission band at the switching frequency are clearly visible in  TABLE 4.  SUMMARY OF SWITCHING FREQUENCY
the frequency spectra (fig. 7).
|     |     |     |     |     |     |     |     |          |     |            |     | Frequency  |     | Switching   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- | ---------- | --- | ----------- |
|     |     |     |     |     |     |     |     | Vehicle  |     | Bandwidth  |     |            |     |             |
|     |     |     |     |     |     |     |     |          |     |            |     | behaviour  |     | Frequency   |
Tab. 4 summarises the characteristics of all vehicles in
|     |     |     |     |     |     |     |     | BEV1  |     | narrow  |     | constant  |     | 10.03 kHz  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --------- | --- | ---------- |
terms of the switching frequency. The spectral distributions of
|     |     |     |     |     |     |     |     | BEV2  |     | -   |     | -   |     | -   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
BEV1, BEV2, BEV3 and BEV5 are shown in fig. 7. The spectra
|     |     |     |     |     |     |     |     |     |     |     |     | variable  |     | ≈ 28 kHz  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- |
are calculated using one measurement interval during the first  BEV3  narrow  (continuous)  (inverse exponential)
constant current charging state. BEV3 is an example for a  BEV4  -  -  -
vehicle  with  a  very  narrow  emission  band  whereas  the  variable  6.55 kHz,
|               |           |      |                 |        |            |       |         | BEV5  |     | wide    |     |             |     |          |
| ------------- | --------- | ---- | --------------- | ------ | ---------- | ----- | ------- | ----- | --- | ------- | --- | ----------- | --- | -------- |
|               |           |      |                 |        |            |       |         |       |     |         |     | (discrete)  |     | 5.2 kHz  |
| emission      | of  BEV5  | has  | a  smooth       | shape  |            | with  | small,  |       |     |         |     |             |     |          |
|               |           |      |                 |        |            |       |         | BEV6  |     | narrow  |     | constant    |     | 11 kHz   |
| superimposed  | peaks     | at   | the  switching  |        | frequency  | and   | its     |       |     |         |     |             |     |          |
harmonics. This is hardly recognisable in the spectrogram in
| fig. 6.  The  | comparison    | between  |              | the  spectrograms  |       | and   | the  |     |     |     |     |     |     |     |
| ------------- | ------------- | -------- | ------------ | ------------------ | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
| spectral      | distribution  | plots    | illustrates  | that               | both  | ways  | of   |     |     |     |     |     |     |     |
presentation are required for a comprehensive analysis.
C. Emission level at switching frequency
| Beside        | the  switching  |           | frequency,  | the        | emission   | level  | at     |     |     |     |     |     |     |     |
| ------------- | --------------- | --------- | ----------- | ---------- | ---------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| switching     | frequency       | is        | another     | important  | parameter  |        | to     |     |     |     |     |     |     |     |
| characterise  | the             | emission  | of  BEVs.   | The        | emission   |        | level  |     |     |     |     |     |     |     |
represents the energy which is injected into the grid and may
disturb other devices.
| As         | shown  above  | the      | emission   | at  switching  |             | frequency  |        |     |     |     |     |     |     |     |
| ---------- | ------------- | -------- | ---------- | -------------- | ----------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| spreads    | over  a       | certain  | frequency  | range          | (bandwidth  |            | at     |     |     |     |     |     |     |     |
| switching  | frequency),   | which    |            | can  be        | narrow      | or         | wide.  |     |     |     |     |     |     |     |
According to [4] 600 Hz-bands centred around the switching
|     |     |     |     |     |     |     |     | Figure 8.  |     | Current emission level of BEV1, BEV3, BEV5 and BEV6 at  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
frequency would catch more than 99% of the emission of PV  switching frequency during the complete charging cycle (laboratory
inverters. This approach cannot be applied to BEVs due to the  measurements)
possibility of wide band emission. Due to the lack of a better
alternative and considering the resulting error, a bandwidth of
| 200 Hz  | was  chosen  | for  | the  analysis  | in  | this  | paper.  | This  |     |     |     |     |     |     |     |
| ------- | ------------ | ---- | -------------- | --- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
corresponds to the recommendation of IEC 6100047, annex B.
A proper method to aggregate narrow and wide band emission
has to be developed in the future.
Fig. 8 shows the time characteristic of the emission level at
| the  switching  | frequency  |     | of  the  | BEVs  | with  a  | significant  |     |     |     |     |     |     |     |     |
| --------------- | ---------- | --- | -------- | ----- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
switching frequency. For BEV1 and BEV5 the emission level
depends on the charging state (constant behaviour followed by
| exponential  | behaviour  | for          | BEV1  | and  sudden         |     | decrease   | of  |     |     |     |     |     |     |     |
| ------------ | ---------- | ------------ | ----- | ------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| emission     | level  at  | the  moment  |       | of  the  switching  |     | frequency  |     |     |     |     |     |     |     |     |
change for BEV5). BEV3 and BEV6 show almost constant
emission levels which are independent of the charging state.
|     |     |     |     |     |     |     |     | Figure 9.  | Emission levels at switching frequency of the BEVs. Dark colour  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
Tab. 5 contains an overview of the maximum emission  represents the grid measurement, bright colour the laboratory measurement
level of each vehicle. These levels were all measured during
the first constant current charging state of each vehicle. The
|     |     |     |     |     |     |     |     | TABLE 5.  |     | OVERVIEW OF EMISSION LEVELS AT SWITCHING FREQUENCY  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------------------------------------------- | --- | --- | --- | --- |
ongoing analysis of the impact of grid parameters is focused  BASED ON 200-HZ-BANDS
on this first constant current charging state in order to identify
|     |     |     |     |     |     |     |     |     | Measurement  |     |     | Max. current emission level  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------------------------- | --- | --- |
if certain conditions may cause higher emission levels than the
|     |     |     |     |     |     |     |     |     |     |     | BEV1  | BEV3  |     | BEV5  BEV6  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | ----------- |
ones measured under ideal conditions.
|     |     |     |     |     |     |     |     |     | Grid  |     | 112.3 dB | µA   122.4 dB | µA   93.1 dB | µA   89.6 dB µA   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | ------------- | ------------ | ----------------- |
Fig. 9 compares the emission at the switching frequency of    Laboratory  119.8 dB µA   108.9 dB µA   98.0 dB µA   92.5 dB µA
all  vehicles  for  the  grid  measurement  and  the  laboratory  difference between grid and laboratory measurements is not
| measurement for the whole charging cycle. For BEV1, BEV5  |     |     |     |     |     |     |     | too large.  |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
and BEV6 the difference between both measurements is small.
[10] provides immunity levels for electricity meters. In the
The levels of BEV3 differ considerably between the grid and
frequency range from 2 to 30 kHz these levels amount 2 A or
the laboratory measurement. The comparison shows that a
|                                                               |     |     |     |     |     |     |     | 126 dB | . The measured emission of the analysed vehicles  |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------------------------------------- | --- | --- | --- | --- | --- |
| general statement about the influence of the grid parameters  |     |     |     |     |     |     |     |        | µA                                                |     |     |     |     |     |
(tab. 5) does not exceed the immunity levels, but the highest
on the charging cycle of all BEVs is not possible. However,
|     |     |     |     |     |     |     |     | measured level is only 4 dB |     |     |     |  lower. The maximal voltage  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
for  most  of  the  analysed  vehicles  (except  for  BEV3)  the  µA
|     |     |     |     |     |     |     |     | level  | arose  | while  | charging  |     | BEV3.  | During  the  grid  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | --------- | --- | ------ | ------------------ |
624
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore.  Restrictions apply.

Proc. of the 2014 International Symposium on Electromagnetic Compatibility (EMC Europe 2014), Gothenburg, Sweden, September 1-4, 2014
measurements a maximum level of 122.5 dB was observed. For a first model it is recommended to focus only on the
µV
According to tab. 1 in [11] for narrow band PLC at 28 kHz a switching frequency and the charging state with the highest
maximum transmission level of about 127.3 dBµV is allowed. emission.
The measured level is only slightly lower than the maximum
The dependency of higher frequency emission on the grid-
transmission level. However, a disturbance-free PLC
specific impact factors introduced in chapter II is currently
communication requires a minimum difference between the
analysed. Based on this results possible improvements and
unintentional and the intentional emission. Furthermore, the
generalisations of the existing models are assessed.
emission levels of the vehicles should be considerably lower
than the maximum transmission level.
ACKNOWLEDGEMENT
It should be noted that the measurement method can have a This project is funded by German federal ministry for the
significant impact on the results [12]. For a precise environment, nature conservation, building and nuclear safety
comparison the methods for the analysis of the measurement (ElmoNetQ, FKZ: 16EM1052). Furthermore we thank the
data have to comply with the measurement methods defined in utilities ewz (Zurich), DREWAG Stadtwerke Dresden GmbH
the standard. All calculations in this paper were performed and ENSO Netz GmbH for providing BEVs for the
using the RMS value of 200 Hz-bands. While the values in measurements.
[10] represent test values at a single frequency, [11] specifies a
spectrum analyzer with a peak detector and a resolution REFERENCES
bandwidth of 100 Hz. [1] J. Meyer, K. Klatt, P. Schegner, “Power quality challenges in future
distribution networks”, 2nd IEEE PES International Conference and
D. Basic Modelling Approach
Exhibition on Innovative Smart Grid Technologies (ISGT Europe);
A first simulation model should include the switching Manchester, Decembre 2011
frequency and its harmonics derived from lab measurements. [2] G. F. Bartak, A. Abart, “EMI of Emissions in the Frequency Range
2 kHz 150 kHz”, 22nd International Conference and Exhibition on
The grid-dependent impact factors are still neglected at this
Electricity Distribution (CIRED 2013), Stockholm, Paper 1271, June
stage. In the first step only the first charging state (constant
2013
current) is considered, because the highest emission occurs
[3] Taskforce EMI, “Study report on electromagnetic interference between
usually during this state. electrical equipment / systems in the frequency range below 150 kHz”,
2nd ed., CENELEC SC 205A Mains communicating systems, April 2013
For future models the stepwise inclusion of grid-dependent
[4] M. Klatt, J. Meyer, P. Schegner, A. Koch, J. Myrzik, C. Körner, et.al.,
impact factors as well as different charging states can be
“Emission Levels above 2 kHz – Laboratory Results and survey
considered. Measurements in public low Voltage Grids”, 22nd International
Conference and Exhibition on Electricity Distribution (CIRED 2013),
IV. CONCLUSION Stockholm, Paper 0999, June 2013
This paper provides a brief overview of the higher [5] J. Kirchhof, G. Klein: “Results of the OPTINOS project – Deficits and
uncertainties in Photovoltaic Inverters test procedures”, 24th European
frequency emission in the range between 2 kHz and 150 kHz
Photovoltaic Solar Energy Conference and Exhibition, Hamburg,
caused by BEV chargers. A test stand is used for the detailed
Germany, September 2009.
characterisation of the emission. For verification purposes the
[6] J. Meyer, S. Hähle, P. Schegner, “Impact of higher Frequency Emission
analysed vehicles were also measured in real low voltage above 2kHz on electronic mass-market Equipment”, 22nd International
grids. Conference and Exhibition on Electricity Distribution (CIRED 2013),
Stockholm, Paper 0999, June 2013
The emission depends on several vehicle-dependent and
[7] S. K. Rönnberg, M. H. J. Bollen, M. Wahlberg, “Interaction Between
grid-dependent impact factors. This paper studies the emission Narrowband Power-Line Communication and End-User Equipment”,
behaviour in regard to the charging state characteristics for six IEEE Trans. on Power Delivery, vol. 26, pp. 2034-2039, July 2011
different BEVs. For each BEV the switching frequency and [8] E. O. A. Larsson, M. H. J. Bollen, M. G. Wahlberg, C. M. Lundmark
the emission level at the switching frequency were analysed. and S. K. Rönnberg, “Measurement of High-Frequency (2-150 kHz)
Distortion in Low-Voltage Networks”, IEE Trans. on Power Delivery,
Not all BEVs show a significant switching frequency and vol. 25, pp. 1749-1757, July 2010
the switching frequency is neither constant during the [9] J. Meyer, S. Hähle, P. Schegner, C. Wald, “Impact of electrical car
charging cycle nor similar between the BEVs. The emission charging on unbalance in public low voltage grids”, 11th International
Conference on Electrical Power Quality and Utilisation (EPQU), Lisbon,
levels depend on the charging topology of each vehicle and
October 2011
the charging state. The higher frequency emissions of the
[10] CLC/FprTR 50579: Electricity metering equipment – Severity levels,
vehicles were found in the frequency range of about 3 kHz to
immunity requirements and test methods for conducted disturbances in
29 kHz. The emission levels range from 85 dB µA to 125 dB µA , the frequency range 2 – 150 kHz, CENELEC technical report, final
which is still below the immunity levels for electricity meters. draft, January 2012
The measured voltage levels are also lower than the maximum [11] EN 50065-1:2001 + A1:2010: Signalling on low-voltage electrical
transmission level of PLC signalling. But for one BEV the installations in the frequency range 3 kHz to 148.5 kHz – Part 1: General
requirements, frequency bands and electromagnetic disturbances,
difference between both levels is small. It is important to
CENELEC european standard, german version, May 2010
respect a minimum difference in order to ensure an error-free
[12] M. Klatt, J. Meyer, P. Schegner: „Comparison of measurement methods
PLC communication. This should be considered, e.g. in the
for the frequency range of 2 kHz to 150 kHz”, International Conference
future standardisation activities. on Harmonics and Quality of Power (ICHQP, Bucarest, May 2014.
625
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:58 UTC from IEEE Xplore. Restrictions apply.