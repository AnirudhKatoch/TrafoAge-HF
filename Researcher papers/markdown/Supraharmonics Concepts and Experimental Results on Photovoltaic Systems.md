XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
| Supraharmonics:  |     |     |     |     |     | Concepts and Experimental  |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Results on Photovoltaic Systems
Gianfranco Chicco, Angela Russo, Filippo Spertino
Politecnico di Torino, Energy Department, Torino, Italy, {gianfranco.chicco,angela.russo,filippo.spertino }@polito.it
Topic: Identification oflocation of harmonics and asymmetry sources. Type of presentation: Lecture
Abstract  The  characterization  of  supraharmonics  associations relevant to the evolution of the power quality
-
referring to conducted disturbances at frequencies above 2  Standards [5]. A recent contribution [6] addresses the
kHz is gaining interest because of their interaction with the  issue  of  the  standardization  for  supraharmonics.  In
range of frequencies occurring in practical applications such  particular, the existing standards that can be applied in
as  smart  meter  power-line  communication.  This  paper  the  frequency  range  2  to  150 kHz  are  described  and
| reviews various aspects concerning the measurement and  |     |     |     |     |     |     |     | compared.  |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
representation  of  the  suprah  armonics,  as  well  as  Further  documents  have  been  prepared  by  different
approximated modelling that can be used in the presence of  standardization  bodies. In particular, a  convergence  of
inverters.  Experimental  results  referring  to  photovoltaic  interests is emerging and is reflected in the upgrade of the
systems are included.
|     |     |     |     |     |     |     |     | power  | quality  | standards  | accessing  |     | supraharmonics  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | ---------- | --- | --------------- | --- |
Keywords -supra harmonics, power quality, photovo/taic,  frequency levels from the "low frequency" side (below
meters, grid connection, measurement.  150 kHz)[7] and from the "high frequency" side (above
|     |     |     |     |     |     |     |     | 150  kHz).  | The  | latter  | are  interested  |     | in  extending  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------- | ---------------- | --- | -------------- | ---- |
I.  INTRODUCTION  frequency  range  to  lower  levels,  in  order  to  ensure
|      |           |            |     |                 |     |         |          | appropriate  | EMC      | performance  |        | of  | the      | equipment  |
| ---- | --------- | ---------- | --- | --------------- | --- | ------- | -------- | ------------ | -------- | ------------ | ------ | --- | -------- | ---------- |
| For  | harmonic  | analysis,  |     | the  classical  |     | limits  | to  the  |              |          |              |        |     |          |            |
|      |           |            |     |                 |     |         |          | connected    | in  the  | smart        | grid.  | An  | example  | is  the    |
harmonic orders set by the Standards and implemented in�
International standardization activity of the International
| the  power  | quality  | analyzers  |              | are  the  | 40   | th  (or the  | 50 th |            |            |      |                |               |                   |           |
| ----------- | -------- | ---------- | ------------ | --------- | ---- | ------------ | ----- | ---------- | ---------- | ---- | -------------- | ------------- | ----------------- | --------- |
|             |          |            |              |           |      | th           | t     | Special    | Committee  | on   | Radio          | Interference  |                   | (CISPR),  |
| harmonic.   | For      | a  50      | Hz  system,  |           | the  | 40 and       | 501   |            |            |      |                |               |                   |           |
|             |          |            |              |           |      |              |       | belonging  | to         | the  | International  |               | Electrotechnical  |           |
harmonics mean 2 kHz and 2.5 kHz, respectively, and the
|     |     |     |     |     |     |     |     | Commission  | (IEC),  |     | currently  |     | working  | towards  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ---------- | --- | -------- | -------- |
corresponding frequencies for a 60-Hz system are 2.4
|           |          |     |            |        |       |       |           | establishing  | new  | requirements  |     | in  the  | band  | below 150  |
| --------- | -------- | --- | ---------- | ------ | ----- | ----- | --------- | ------------- | ---- | ------------- | --- | -------- | ----- | ---------- |
| kHz  and  | 3  kHz.  | In  | practice,  | under  | this  | view  | all  the  |               |      |               |     |          |       |            |
kHz, also pointing out to which equipment the new limits
conducted disturbances exceeding these frequencies are
should be applied [8].
| not  taken  | into  | account  | in  | the  determination  |     |     | of  the  |     |     |     |     |     |     |     |
| ----------- | ----- | -------- | --- | ------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
classical harmonic distortion indicators implemented in  Various types of equipment have been studied with the
the analyzers.  aim of highlighting the supraharmonics appearing during
their operation. Main subjects of investigation have been
However, the number of applications in which non­
fluorescent lights [9], high-frequency ballasts (with the
negligible conducted disturbances appear at frequencies
relevant effects on their lifetime) [10] and LED lamps
above 2 kHz has increased during the years, also because
[II ]. Other examples include residential equipment such
| no  strict    | regulation  |                  | has  been  |                  | in  place  | concerning  |            |           |            |            |               |     |              |            |
| ------------- | ----------- | ---------------- | ---------- | ---------------- | ---------- | ----------- | ---------- | --------- | ---------- | ---------- | ------------- | --- | ------------ | ---------- |
|               |             |                  |            |                  |            |             |            | as  TV    | sets  and  | microwave  | ovens         |     | [12],  with  | further    |
| disturbances  | at          | relatively high  |            | frequencies. In  |            |             | the  last  |           |            |            |               |     |              |            |
|               |             |                  |            |                  |            |             |            | addition  | of  the    | effect     | of  electric  |     | vehicles     | in  [13].  |
decade there has been a growing interest towards the so­
|                         |     |     |      |                 |     |              |     | Experimental  | results    | referring    |     | to  groups  | of              | loads  are  |
| ----------------------- | --- | --- | ---- | --------------- | --- | ------------ | --- | ------------- | ---------- | ------------ | --- | ----------- | --------------- | ----------- |
| called  supraharmonics  |     |     | (or  | high-frequency  |     | harmonics),  |     |               |            |              |     |             |                 |             |
|                         |     |     |      |                 |     |              |     | provided      | in  [14].  | Propagation  |     | of          | high-frequency  |             |
i.e., harmonics appearing at frequencies above 2 kHz.
harmonics in industrial networks has been addressed in
| The  related  | aspects  |     | are  fully  | considered  |     | among  | the  |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ----------- | ----------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
[15], taking into account conventional loads and variable
current issues for harmonic analysis [1][2].
speed drives.
In early studies (e.g., [3]) the supraharmonics have
|     |     |     |     |     |     |     |     | The  | assessment  | of  | supraharmonics  |     | referring  | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --------------- | --- | ---------- | --- |
been addressed in the frequency range from 2 to 9 kHz.
|     |     |     |     |     |     |     |     | distributed  | generation  |     | with  wind  | and  | PV  | systems  is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ----------- | ---- | --- | ------------ |
Nowadays, the frequency range can be extended up to
|           |     |      |       |          |      |             |     | particularly  | challenging,  |     | because  |     | of  the  | uncertain  |
| --------- | --- | ---- | ----- | -------- | ---- | ----------- | --- | ------------- | ------------- | --- | -------- | --- | -------- | ---------- |
| 100  kHz  | or  | 150  | kHz,  | because  | the  | power-line  |     |               |               |     |          |     |          |            |
behavior of the sources depending on ambient conditions,
| communications  |     | used  | in  smart  | meters  |     | work  | in  this  |                |     |             |          |     |           |             |
| --------------- | --- | ----- | ---------- | ------- | --- | ----- | --------- | -------------- | --- | ----------- | -------- | --- | --------- | ----------- |
|                 |     |       |            |         |     |       |           | the  presence  | of  | conversion  | systems  |     | and  the  | effect  of  |
spectrum zone, and the interaction between power-line
harmonic summation for aggregations of local generators,
| communications  |     | and  | different  |     | types  | of  | end-user  |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ---------- | --- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
also taking into account the connecting circuits. Wind
| equipment may affect the equipment  |     |     |     |     | performance  |     | [4].  |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
systems have been addressed in [16], pointing out the
Therefore, it is possible a negative interaction between
attention to individual wind turbines and especially on the
the smart-meter signals and the supraharmonics produced
effects of their aggregation in wind farms. An emergent
by grid-connected harmonic sources, both on the demand
need to refine the models and study the propagation of
side and on the generation side, e.g., from photo voltaic
the harmonic emission to the grid is indicated. Further
(PV) inverters.
analyses on wind parks at frequencies up to 200 kHz have
Supraharmonics are a timely topic being addressed by  been reported in [17] by using the concept of overall
a number of Working Groups in all the Committees and  transfer function, concluding that in the case studied the
|     |     |     |     | 978-1-4799-8416-9/15/$31.00 ©201  |     |     |     |     | 5   | IEEE  |     |     |     |     |
| --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore.  Restrictions apply.

XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
emISSIOn of harmonics at frequencies above a few to another in case of disturbance to the communications.
kilohertz has been negligible. A number of contributions Reference [26] focused on PV installations connected
referring to PV systems are reviewed in Section II of this to LV grids, where PV generators generally use inverters
paper. that generate the output current using pulse width
One of the open questions is the characterization of the modulation (PWM). Compared with other techniques,
supraharmonics for an aggregation of sources. Initial this efficiently reduces low order harmonics, but leads to
results are borrowed from harmonic analysis, considering high frequency components around the PWM carrier
that, when the frequencies are relatively high, the phase signal frequency (typically between 15 kHz and 20 kHz)
angle dispersion becomes relevant. In case of randomly and its multiples. Different frequency bands are
selected phase angles for a number of aggregated implemented and compared. Differences between the
components of equal characteristics, the amplitude of the distribution of the harmonics in the three phases for PV
aggregated harmonic is proportional to the inverse of the plants connected to the three-phase system are also
square root of the number of components [18]. shown. Peaks in supraharmonics emissions have been
This paper recalls some emergent concepts referring to reported in [27]. In particular, a peak around 16 kHz is
the presence of supraharmonics in electrical distribution likely to be associated with the switching of the inverter.
system applications, including distributed generation, and Confirmation of this fact also comes from the absence of
presents some inputs concerning the experimental this peak during the night, without PV production.
characterization of supraharmonics in PV systems. For PV systems, the PWM technology, commercially
The next sections are organized as follows. Section II used in single-phase and three-phase connections,
summarizes some literature contributions referring to exhibits unipolar and bipolar configurations with triangle
harmonics and supraharmonics in PV systems. Section III waveforms in the range 1-20 kHz. The harmonic
addresses measurement aspects and the representation of emissions are different according to the type of
the results. Section IV deals with modeling aspects for configuration, however the harmonics are grouped into
the interpretation of the supraharmonics contents. Section integer multiples of the triangular carrier [28]. In
V presents the results of experimental tests carried out on particular, for relatively small inverters (below 100 kW)
a real PV system. The last section contains the the switching frequency is generally above 10kHz, while
concluding remarks. for larger inverters the switching frequency is generally
below 10 kHz [1].
II. HARMONICS AND SUPRAHARMONICS IN Experimental results from [29] showed the presence of
PHOTOVOLTAIC SYSTEMS -AN OVERVIEW
3.8 kHz and 4.85 kHz components, poorly correlated with
Many references can be found in the literature with the PV production. These components are associated with
respect to the emissions caused by photovoltaic the power-line communications exploited by the
generators connected to LV and MV networks up to 2 distribution system operator to transmit data referring to
kHz. For instance, [19] gives an overview of the current automated meter readings. Some conclusions from [30]
state of knowledge within the context of IEC regulations, are that every installation is unique, and for large
particularly in regards to harmonics, flicker, and voltage numbers of inverters the level of distortion in the
unbalance. frequency range from 2 kHz to 150 kHz requires further
study, with particular respect to aggregation effects, the
Experimental data based on PV system measurement
spread of emission, the interaction between different
data to verity compliance with the PQ requirements are
typologies of devices, and the relation with active power
presented in [20]. Results of further investigations, also
production.
considering the interaction of several inverters connected
at the same busbar, can be found in [21 ]-[23]. In [24] the III. MEASUREMENTS AND REPRESENTATION OF THE
harmonic current emission in PV systems is characterised RESULTS
under real operating conditions, and a statistical
methodology for assessing PV harmonic current emission One of the major issues in the research on
is proposed. supraharmonics regards the measurement methods that
can be applied when measuring signal of voltage and
Some recent contributions focused on the emission
current for frequency greater than 2 kHz.
characterization at frequencies greater than 2 kHz. Few
papers report the results of measurement campaigns on One of the earlier contributions with respect to high­
PV installations focused on the analysis of harmonic frequency distortion was the examination of the results
emission both for classical harmonics below 2 kHz and from a measurement campaign in the frequency range 2 -
higher frequency emission in the range of 2-150 kHz. In 150 kHz [31]. In [31] time-domain, frequency-domain
particular, [25] reports the results of extensive and a combined time-frequency domain representations
measurements carried out at a 1 MW PV installation with of the waveform are used. Measurements of both current
multiple inverters with different rated power, at emission and voltage distortion are presented.
frequencies up to 100 kHz. High frequency current Concerning the comparison between some ways to
emissions are analysed for a single inverter and for a measure the harmonics and supraharmonics components,
group of inverters. From the results reported, it is also the standards for harmonics measurement (I EC 61000-4-
possible to observe the effect of narrow band power-line 7 and IEC 61000-4-30) identify a lO-cycle time window
communication systems (PLC), whose contributions from (200 ms for a 50-Hz system) over which time-domain
different channels appear as multiple increases in the data are sampled. Then, the signal is processed through
current spectrum (one for each channel) in the frequency Discrete Fourier Transform (DFT) and the results are
range from 40 kHz to 80 kHz. The presence of multiple arranged into frequency bands of 5 Hz width. Harmonic
channels is useful to enable switching from one channel groups and subgroups are then defined. Reference [3]
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore. Restrictions apply.

XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
MODELLING ASPECTS
| discusses the implications of considering 200 ms window  |     |     |     |     |     |     |     | IV.  |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
(leading to 5 Hz components) for frequencies below 2
|                                      |              |            |      |          |                 |          | Harmonic           | and  interharmonic  |             | penetration  |             | studies  |
| ------------------------------------ | ------------ | ---------- | ---- | -------- | --------------- | -------- | ------------------ | ------------------- | ----------- | ------------ | ----------- | -------- |
| kHz and 100 ms window (leading to 10 |              |            |      |          | Hz components)  |          |                    |                     |             |              |             |          |
|                                      |              |            |      |          |                 |          | require  accurate  | models  of          | power       | system       | components  |          |
| from  2                              | to  9  kHz,  | arranging  | the  | results  | in              | 200  Hz  |                    |                     |             |              |             |          |
|                                      |              |            |      |          |                 |          | (lines,  cables,   | transformers,       | electrical  | machines     |             | and      |
frequency bands. A safe limit is indicated to be 0.5% of
|     |     |     |     |     |     |     | loads)  in  | the  frequency  | range  of  | interest.  | They  | are  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ---------- | ---------- | ----- | ---- |
nominal voltage per 200-Hz band.
historically based on the study of the frequency range 0 -
The issue of measurement methods for voltage and  2.5  kHz.  Some  attention  has  been  devoted  to  the
current in the frequency range of 2 kHz to 150 kHz is  frequency range 2.5 - 9 kHz, which is the upper limit of
addressed  in  [32].  In  particular,  two  measurement  the low-frequency range considered by IEC Standards.
methods are compared: the method for frequencies of 2  Recently,  starting  from  the  consideration  that  modern
kHz to 9 kHz proposed in the informative annex of IEC
|     |     |     |     |     |     |     | converters  | utilize  high  commutation  |     | frequencies,  |     | the  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------- | --- | ------------- | --- | ---- |
61000-4-7, which could be extended in application to 150
attention has been extended to the frequencies up to 100
kHz, and the method for the frequency range of 9 kHz to  kHz. In [33] contributions for modelling behaviour of
150 kHz proposed by the committee draft for vote ofIEC  both overhead and cable MV lines in the frequency range
| 61000-4-30 Ed.3.  |     |     |     |     |     |     | from 0 to 100 kHz are given.  |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
An oscilloscope having only 8 bits is not sufficient
The spread of high-frequency current between different
[15]. A 16 bit resolution system is needed, e.g., with  devices and into the grid is explained in [4] by means of a
maximum sampling frequency of 250 kSa/s. In this way,  model also used to show the aggregation between devices
the frequency limit depends on the number of channels  and to predict the amplitude modulation of the voltage
used. From the Nyquist-Shannon theorem, for a single  and current ripple due to the small frequency differences
| channel the maximum frequency is of 125 kHz, and is  |     |     |     |     |     |     | between devices.  |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
halved (to 62.5 kHz) if two channels are used.
The understanding of the real situation, when a PV
The  frequency  bandwidth  of  the  probes  is  also  a  inverter (or a group ofPV inverters) is connected to a low
primary  concern.  Significant  differences  in  the  results  voltage grid, is possible by using a simple equivalent
obtained by using different probes in the same system  circuit, in which both the Voltage Source Inverter (VSI)
have  been  reported  in  [15].  There  are  different  and  the  distribution  grid  are  represented  by  the
instruments to measure AC current signals: the most used
|             |           |              |          |     |         |           | corresponding  | Thevenin  | equivalents.  | The  | equivalent  |     |
| ----------- | --------- | ------------ | -------- | --- | ------- | --------- | -------------- | --------- | ------------- | ---- | ----------- | --- |
| categories  | are  the  | Hall-effect  | current  |     | clamps  | and  the  |                |           |               |      |             |     |
circuit of each device in an electric power system is an
Rogowski coils. The accuracy of the Hall-effect probes is
appropriate tool to simulate the behavior of this system in
higher than the other sensors. However, even if the first  terms  of  harmonic  components.  In  particular,  the
category permits to extend the frequency range down to  Thevenin generator is the most used equivalent circuit for
the  zero  frequency,  the  second  category  permits  to  both the power supplies (e.g. the distributed generators
increase the frequency band up to some tens of kilohertz.  and  the  distribution  grid)  [15].  Regarding  the  loads
|     |     |     |     |     |     |     | connected  | to  the  grid,  | besides  | the  usual  | constant  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | -------- | ----------- | --------- | --- |
In the experimental campaign reported in this paper,
the frequency ranges are from DC to 15 kHz for the Hall­ impedance model, it is considered a current source, with
effect current probes with peak values of 2000 A, while  the proper harmonic components, to simulate the current
the  same  ranges  are  from  10 Hz  to  50  kHz  for  the  injection into the grid, according to the frequency under
Rogowski coils. A correct positioning of the conductors  study in the operation of the electric power system [2].
inside the probe cores is crucial for both the types of
The parameters are defined for each harmonic order h
instruments: normally, the available space to embrace the
|                 |                  |                      |                |                 |            |                    | of  the  frequency  | spectrum                               | in  this  | way:  | ideal  | voltage     |
| --------------- | ---------------- | -------------------- | -------------- | --------------- | ---------- | ------------------ | ------------------- | -------------------------------------- | --------- | ----- | ------ | ----------- |
| c o n d u c t   | o r   is   h i g | h e r   in   t h e   | c a s e   o    | f  R o g o      | w sk i     | c o i l.   T h i s |                     |                                        |           |       |        |             |
|                 |                  |                      |                |                 |            |                    | h                   |   V-  h                                |           |       |        | h           |
|                 |                  |                      |                |                 |            |                    | sources V- v si     | '  gr id  and equivalent impedances Z- |           |       |        | v s i  and  |
| s e n s o r   i | s   m a d e      | o f   a   fl e x i b | l e   c o i l  | o f  w i        | r e,  w it | h o u t   ir o n   |                     |                                        |           |       |        |             |
| core,  and      | it  is           | wrapped  around      |                | the  conductor  |            | whose              | Z -h                |                                        |           |       |        |             |
grid. However, the harmonic components of the ideal
current must be measured. Other factors which affect the
| measurements are the winding density, the coil diameter  |     |     |     |     |     |     |                 | Vg�                                    |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | -------------------------------------- | --- | --- | --- | --- |
|                                                          |     |     |     |     |     |     | voltage source  | id  are typically within the range 50- |     |     |     |     |
and the rigidity of the winding. In the Rogowski coil, the
induced voltage is proportional to the derivative of the  2500 Hz  (excluding possible  signals coming from the
current in the conductor under study. Hence, the output of  communication systems used in smart meters). Therefore,
the Rogowski coil is connected to an integrator circuit to  at  the  Point  of  Common  Coupling  (PCC)  the  current
|     |     |     |     |     |     |     |     | J;cc  |     |     | V;cc  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
provide an output signal proportional to the current.  injected into the grid  and its voltage  can be
For representation purposes, time-domain graphs and
calculated by using the common mesh equation and the
harmonic spectra are generally used. Due to the wide
Millman's theorem.
range of harmonics considered and to the specific interest
|     |     |     |     |     |     |     | The  quantitative  | analysis  | performed  | thanks  | to  | these  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------- | ---------- | ------- | --- | ------ |
towards the supraharmonics, logarithmic representations
equations shows that, neglecting the grid impedance with
are also used (e.g., with the amplitude scale expressed in
respect to the VSI impedance, both current and voltage
decibels; typical units for voltage and current amplitudes
have a spectrum similar to the spectrum generated by the
are dB�v and dB�A' respectively [25]).
PV inverter. Obviously, the PV inverter is equipped with
About the techniques of analysis, the classical time­
the EMI filter to reduce the harmonic emission and thus
domain and frequency-domain analysis are used, while  the PV inverter spectrum is not identical to an ideal PWM
| some  contributions  |     | in  identifying  |     | the  | supraharmonics  |     |     |     |     |     |     |     |
| -------------------- | --- | ---------------- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
spectrum.
signatures of different systems may come from the results
|     |     |     |     |     |     |     | In summary,  | starting from the basic equations and  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------------------------- | --- | --- | --- | --- |
of time-frequency analysis [14].
neglecting the effect ofthe load:
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore.  Restrictions apply.

XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
different during the morning and the evening. The second
field is optimally (South) oriented and not integrated (less
thermal losses). Two PV arrays (numbers 4 and 5) are
(1)
subject to systematic partial shading.
|     | iZ  | V   |     | V - h   V-  h   id  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Si  grid  v s i   g r C o n c e rn i n g   t h e   m e a s u r em e n t s,   ti m e - d o m a in   s a m p l i n g
|     | _   | +  _ |     | + �   |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Z Z Z - h   Z of  th e  v o l ta g e   a n d   c ur r e n t  w av e f o r m s  h a s   b ee n  c a r r ie d   o u t
|     | vsi  | grid  |     | vsi  grid  |     |     |     |     |     |     |     |
| --- | ---- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
V V-h  by means of a portable data logging system. In order to
| pcc =  |     | -7  | pcc  |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
I  I  I  I  reproduce the outputs within a wide frequency band, the
|     | �   | +�   |     | + �   | (2)  |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
Z Z   Z- h   Z  instrumentation  must  have  suitable  accuracy.  In  this
|     | vsi  | g rid  |     | v s i  grid  |     |              |               |          |      |           |          |
| --- | ---- | ------ | --- | ------------ | --- | ------------ | ------------- | -------- | ---- | --------- | -------- |
|     |      |        |     |              |     | regard,  in  | low  voltage  | systems  | the  | voltages  | can  be  |
when supraharmonics are considered, the equations can  measured with percent uncertainty of about ±O.I%   for
be approximated as:  frequencies  up  to  some  megahertz.  However,  the
|     |       | V-h  |     |     |     | bottleneck is the measurement of the currents. Indeed,  |     |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
| y h |   '"  | vsi  |     |     |     |                                                         |     |     |     |     |     |
p e e  when  a  current  clamp  meter  is used for  peak  current
Rv si +}· hOJ·LT vsi
|     |     |     |     |     | (3)  | ranges of ±200/2000 A, the accuracy is around ±1.5%  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
and a limit of 15 kHz is typical. The frequency limit can
be increased if the currents are lower, for example with a
|     |     |     |     |     |     | peak  current  | of  ±30  | A  the  | frequency  | range  | can  be  |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | ------- | ---------- | ------ | -------- |
(4)
extended up to 100 kHz [15].
Critical aspects of using these model equations are that  The experimental results are ordered with a top-down
the parameters are not constant in time and are difficult to  approach. Voltage and current signals have been gathered
be characterized. Approximated models may be useful to  in the three-phase four-wire system at different locations,
explain the outcomes occurring in specific situations.  starting  from  the  low  voltage  side  of  the  distribution
|     |     |     |     |     |     | transformer,  | continuing  | with  | the  PV  | system  | (i.e.,  |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----- | -------- | ------- | ------- |
EXPERIMENTAL TESTS AND RESULTS
V.
excluding loads and auxiliary services) and finishing with
Experimental tests have been performed to characterize  the inverter supplied by the PV array #4, subject to partial
the harmonic content of the current and voltage at PCC  shading in a part of the day.
for frequencies higher than 2 kHz.  At the distribution transformer busbars the harmonic
content of the local load supplied by the grid can be
A real PV system (850 kWp) is considered [34]. The
PV system is installed on the top of an industrial building  separated from the harmonic content of the PV system.
in the outskirts of a big city. It is used partly to supply the  For  these  measurements,  the  Rogowski  coil  has  been
local load, partly for power injection into the grid. Fig. I  used. Thanks to a dedicated test in which the general
shows the layout ofthe PV system.  circuit breaker of the PV system is opened, the signals
before and after this commutation are gathered. Fig. 2
shows the currents in the three phases before and after
opening the general circuit breaker of the PV system.
|     |     |     |     |     |     | Fig.  3  | shows  that  | the  harmonic  | current  | of  | the  PV  |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | -------------- | -------- | --- | -------- |
system together with the load is characterized by peaks
with groups of harmonic orders at multiples of 3 kHz.
|     |     |     |     |     |     | These  harmonics  | are  | associated  | with  | the  PV  | inverter  |
| --- | --- | --- | --- | --- | --- | ----------------- | ---- | ----------- | ----- | -------- | --------- |
operation. In order to verify this statement, by opening
the circuit breaker and leaving only the supply to loads
and auxiliary services, these peaks disappear (Fig. 4).
Fig. I. Layout ofthe system with PV arrays and local loads.
The whole PV generator is composed of two different
subfields of 800 kWp  (integrated into the shed root) and
50 kWp (non-building integrated) with mono-crystalline
and poly-crystalline silicon modules, respectively. All the
PV arrays are connected on the LV side through eight
three-phase inverters with different power ratings: six for  Fig. 2. Phase currents before and after opening the general circuit
the first section and two for the second one. The inverters  breaker ofthe PV system.
and the LV/ MV transformer are oversized to minimize
losses and maximize lifespan.
| The total rated powers are 870 kVA  |     |                                   |     |  for the inverters  |         |     |     |     |     |     |     |
| ----------------------------------- | --- | --------------------------------- | --- | ------------------- | ------- | --- | --- | --- | --- | --- | --- |
| and 1250 kVA                        |     |  for the delta-star transformer.  |     |                     | The PV  |     |     |     |     |     |     |
arrays have been installed with the aim to maximize the
| occupation  |            | of  the  roof  | surface     | on  the      | commercial  |     |     |     |     |     |     |
| ----------- | ---------- | -------------- | ----------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
| building,   | accepting  | the            | occurrence  | of  partial  | shading     |     |     |     |     |     |     |
during the day on some arrays. The first field is oriented
to the southwest; consequently, the exposure to the solar
Fig. 3. Phase current harmonics before opening the general circuit
| radiation  | is  | neither  symmetrical  |     | nor  optimal  | and  is  |     |     |     |     |     |     |
| ---------- | --- | --------------------- | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- |
breaker of the PV system.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore.  Restrictions apply.

XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
1BO  In order to highlight possible limits in the execution of
| 160  |     |     |     |     |     |     | the measurements, the two graphs of Fig. 8 show the  |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
harmonic spectrum referring to the current of one of the
phases in the measurement of the whole PV system. The
|     |     |     |     |     |     |     | amplitude  | at  fundamental  | frequency  | (about  | 700  A)  is  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ---------- | ------- | ------------ |
truncated. The graph on the top contains the harmonic
spectrum used in the classical harmonic analysis, up to 2
|                                                                     |     |      |     |      |     |            | kHz.  The graph on                                     |     | the  bottom contains the harmonic  |     |     |
| ------------------------------------------------------------------- | --- | ---- | --- | ---- | --- | ---------- | ------------------------------------------------------ | --- | ---------------------------------- | --- | --- |
|                                                                     |     | 0.5  |     | 1.5  |     | 2.5  ,     |                                                        |     |                                    |     |     |
|                                                                     |     |      |     |      |     | �  •  . 4  | spectrum relevant to the study on the supraharmonics,  |     |                                    |     |     |
| Fig. 4. Phase current harmonics after opening the general circuit b |     |      |     |      |     | r e a ker  |                                                        |     |                                    |     |     |
starting from 2 kHz and continuing up to 20 kHz. The
ofthe PV system (load and auxiliary services only).
measurement carried out with the Rogowski coil makes it
Further measurement has been carried out for the PV  possible to represent the correct information in the whole
system  alone,  again  using  the  Rogowski  coil.  Fig.  5  frequency range. [f the measurement are done by using a
current clamp, the data shown in the encircled part of the
| shows  | the  | phase  | current  | harmonics  | in  | this  case,  |     |     |     |     |     |
| ------ | ---- | ------ | -------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- |
spectrum (above 15 kHz) are not represented, as for the
| highlighting the frequencies up to 10 |     |     |     |     | kHz. The presence  |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
system operating with relatively high currents (hundreds
| of  the  | abovementioned  |     | peaks  | for  groups  |     | of  harmonic  |     |     |     |     |     |
| -------- | --------------- | --- | ------ | ------------ | --- | ------------- | --- | --- | --- | --- | --- |
orders  around  multiples  of  3  kHz  is  confirmed.  This  of amperes) the frequency range to be considered for the
behavior is typical of inverters with power rating above  current clamp is limited to 15 kHz.
| some      | tens  | of  kilowatts.  | From   | Fig.      | 5  it  | can  also  be  |     |     |     |     |     |
| --------- | ----- | --------------- | ------ | --------- | ------ | -------------- | --- | --- | --- | --- | --- |
| observed  | that  | the             | phase  | currents  | are    | significantly  |     |     |     |     |     |
unbalanced. The zoom reported in Fig. 6 shows that in
| the  three  | phases  | in  | unbalanced  | conditions  |     | the  peaks  |     |     |     |     |     |
| ----------- | ------- | --- | ----------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
behave in a similar way.
180,
|     | 1000  | 2000  | 3000  4000  | 5000  6000  | 7000  8000  | 9000  10000  |     |     |     |     |     |
| --- | ----- | ----- | ----------- | ----------- | ----------- | ------------ | --- | --- | --- | --- | --- |
frequency (Hz)
Fig. 5. Phase current harmonics (PV system only).
Fig. 8. Harmonic amplitude spectra of one phase current of the grid­
connected PV system.
1BO
160-
VI. CONCLUSION
140
| 120  |     |     |     |     |     |     | The  presence  | of  | supraharmonics  | in  | the  electrical  |
| ---- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | ---------------- |
distribution systems calls for extending the present power
quality rules and standards. This paper has provided an
|     |     |     |     |     |     |     | overview  | of  the  relevant  | concepts,  | based  | on  specific  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | ---------- | ------ | ------------- |
40  literature  contributions,  addressing  in  particular  the
,
82DC  8600  88DC  9000  92DC  9600  9800  10000  limitations in the frequency range of the current probes
Fig. 6. Zoom ofthe phase currenth��-;�i�� (PV system only).
used to carry out measurement campaigns on large PV
systems. Some results of experiments carried out by the
Finally, at the level of the inverter supplied by PV  authors on a large PV system have been reported in an
array  #4  subject  to  partial  shading,  the  measurements  appropriate scale based on decibels to make the main
have been carried out by using a current clamp, with  components of the harmonic currents clearly visible and
limited frequency band. The results are presented in Fig.  to highlight the effects of current unbalance in the three­
7, up to 10 kHz. The previous behavior around multiples  phase system. These results are useful to continue the
of 3 kHz can be found again. The mismatch in the J-V
|     |     |     |     |     |     |     | discussion  | concerning  | the  upgrade  | of  | power  quality  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- | --- | --------------- |
curves of the array [34] worsens the harmonic content of  standards  and  grid  codes,  in  particular  those  used  in
the currents at the AC output of the three-phase inverter,  relatively  weak distribution  systems  (such as the ones
especially for low harmonic orders.  existing  in  islands)  in  which  the  impact  of  the  local
generation systems, for example from renewable sources,
::f
is not negligible with respect to the contribution of the
-�  11  main  grid  [35].  Specific  attention  also  refers  to  the
i :��W����"W,  •. .  interactions  of  supraharmonics  with  power  line
|     |     |     |     |     |     | u�  | communications,  | in  | particular  | concerning  | the  five  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ----------- | ---------- |
r , 1,  I",  channels established by the CENELEC 50065.1 standard
| "l5.w   ool  |     | ml�:  |     | I   | .'  |     |     |     |     |     |     |
| ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the frequency band from 3 kHz to 148.5 kHz [36], of
40
,   ,   ,   which the band limited to 95 kHz is dedicated to the
| ,)o   | 10 0 0  | 2000  3000  | 4000  | 5000  6000  | 7000  80 | 0 0  90 0 0  10000  |     |     |     |     |     |
| ----- | ------- | ----------- | ----- | ----------- | -------- | ------------------- | --- | --- | --- | --- | --- |
frequency (Hz)  electricity  suppliers  and  their  licensees,  while  the
Fig. 7. Phase current harmonics for the inverter of the array #4 subject
channels in the remaining frequency band are assigned to
to partial shading.
the customers.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore.  Restrictions apply.

XII International School on Nonsinusoidal Currents and Compensation, ISNCC 2015, Lag6w, Poland
ACKNOWLEDGMENT [18] B. Lindgren, Power generation, power-electronics and power­
system issues of power converters for photovoltaic applications,
The research leading to these results has received funding from the
Ph.D. dissertation, Chalmers University of Technology,
European Union Seventh Framework Programme FP712007-2013 under
Gothenburg,S weden,D ecember 2002.
grant agreement no. 309048.
[19] lC. Hernandez, M.l Ortega, l De la Cruz, D. Vera, "Guidelines
for the technical assessment of harmonic, flicker and unbalance
REFERENCES
emission limits for PV -distributed generation", Electric Power
[I] M. Bollen, J. Meyer,H Amaris, AM. Blanco, A Gil de Castro,J . Systems Research, vol. 81,n o. 7,J uly 2011,p p. 1247-1257.
Desmet, M. Klatt, L. Kocewiak, S. Ro�nnberg, K. Yang, "Future [20] MJ. Ortega, J.e. Hernandez, O.G. Garcia, "Measurement and
work on harmonics -some expert opinions Part I -wind and solar assessment of power quality characteristics for photovoltaic
power", Proc. IEEE 16th Int. Confer. on Harmonics and Quality systems: Harmonics, flicker, unbalance, and slow voltage
of Power (ICHQP). pp. 904-908,2 5-28 May 2014. variations", Electric Power Systems Research, vol. 96,2013, pp.
[2] J. Meyer, M. Bollen, H. Amaris, AM. Blanco, A Gil de Castro, 23-35.
J. Desmet, M. Klatt, L. Kocewiak, S. Ro Innberg, K. Yang, [21] G. Chicco, l Schlabbach, F. Spertino, "Experimental assessment
"Future work on harmonics - some expert opinions Part II - of the waveform distortion in grid-connected photovoltaic
supraharmonics, standards and measurements", Proc. IEEE 16th installations", Solar Energy, vol. 83, no. 7, July 2009, pp. 1026-
Int. Confer. on Harmonics and Quality of Power (ICHQP), pp. 1039.
909-913,25-28 May 2014. [22] J.H.R. Enslin, W.TJ. Hulshorst, AM.S. Atmadji, PJ.M. Heskes,
[3] M.H.J. Bollen, P.F. Ribeiro, E.OA Larsson, e.M. Lundmark, A Kotsopoulos, J.F.G. Cobben, P. Van der Sluijs, "Harmonic
"Limits for Voltage Distortion in the Frequency Range 2 to 9 Interaction between Large Numbers of Photovoltaic Inverters and
kHz", IEEE Trans. on Power Delivery, vol. 23, no. 3, July 2008, the Distribution Network", in Proc. IEEE Bologna Power Tech,
pp. 1481-1487. Bologna (Italy), 23-26 June 2003.
[4] S.K. Ronnberg, M.HJ. Bollen, M. Wahlberg, "Interaction [23] Y. Du, D.D.-e. Lu, G. James, DJ. Cornforth, "Modeling and
Between Narrowband Power-Line Communication and End-User analysis of current harmonic distortion from grid connected PV
Equipment", IEEE Trans. on Power Delivery, vol. 26, no. 3, inverters under diflerent operating conditions", Solar Energy,
2011,p p. 2034-2039. vol. 94,A ugust 2013,p p. 182-194.
[5] M. Bollen, M. Olofsson, A Larsson, S. Ronnberg, M. Lundmark, [24] J.e. Hernandez, MJ. Ortega, A Medina, "Statistical
"Standards for Supraharmonics (2 to 150 kHz)", IEEE characterisation of harmonic current emission for large
Electromagnetic Compatibility Magazine, vol. 3, no.l, pp. 114- photovoltaic plants", International Trans. on Electrical Energy
119,1 st Quarter 2014. Systems, vol. 24,n o. 8,A ugust 2014,p p. 1134-1150.
[6] E.OA Larsson, M.HJ. Bollen, M.G. Wahlberg, C.M. [25] A Varatharajan, S. Schoettke, l Meyer, A Abart, "Harmonic
Lundmark, S.K. Ronnberg, "Measurements of High-Frequency Emission of Large PV Installations Case Study of a 1 MW Solar
(2-150 kHz) Distortion in Low-Voltage Networks", IEEE Trans. Campus", Proc. Int. Confer. on Renewable Energies and Power
on Power Delivery, vol. 25,n o. 3, pp. 1749-1757,J uly 2010. Quality (ICREPQ), Cordoba (Spain), 8-10 April 2014.
[7] CENELEC, "Study report on electromagnetic interference [26] M Klatt, A Koch,T . Darda, J. Meyer, l Myrzik,P . Schegner, e.
between electrical equipment / systems in the frequency range Komer, "Emission levels above 2 kHz - Laboratory results and
below 150 kHz", Ed.2. CENELEC Tech. Rep. Sec0339,2013. survey measurements in public low voltage grids", Proc. 22nd
[8] International Electrotechnical Commission (lEC), International Int. Confer. on Electricity Distribution, 10-13 June 2013, Paper
Special Committee on Radio Interference (CISPR), CISPR 1168.
Guidance document on EMC of equipment connected to the [27] S. RoLnnberg, Emission and Interaction from Domestic
SmartGrid, February 2014. Installations in the Low Voltage Electricity Network, up to 150
[9] E.O.A Larsson, C.M. Lundmark, M.HJ. Bollen, "Measurement kHz, Doctoral Thesis, Lulea University of Technology, Lulea,
of current taken by fluorescent lights in the frequency range 2- Sweden, 2013.
150 kHz",I EEE PES General Meeting, 2006. [28] R. Teodorescu, M. Liserre, P. Rodriguez, Grid converters for
[10] E.OA Larsson,M . Wahlberg, M.H.l Bollen, "Reduced life-time photovoltaic and wind power systems, Wiley, Chichester, UK,
of lamps: Temperature rise and bad power quality", IEEE 16th 2011.
Int. Confer. on Harmonics and Quality of Power (ICHQP), 2014, [29] S. Ronnberg, M. Bollen, A Larsson, "Grid impact from PV­
pp. 322-326. installations in Northern Scandinavia", Proc. 22nd Int. Confer.
[11] S.K. Ronnberg, MHJ. Bollen, "Emission from four types of and Exhibition on Electricity Distribution (CIRED) 2013.
LED lamps at frequencies up to 150 kHz", Proc. IEEE 15th Int. [30] S.K. Ronnberg, K. Yang, M.H.l Bollen, AG. de Castro,
Confer. on Harmonics and Quality of Power (ICHQP), 2012, pp. "Waveform distortion - a comparison of photovoltaic and wind
451-456. power", Proc. IEEE 16th Int. Confer. on Harmonics and Quality
[12] A Gil-de-Castro, S.K. Ronnberg, M.HJ. Bollen, "A study about of Power (ICHQP), pp. 733-737,25-28 May 2014.
harmonic interaction between devices", Harmonics and Quality [31] E.O.A Larsson, M.H.J. Bollen, "Measurement result from I to
of Power (ICHQP), Proc. IEEE 16th Int. Confer. on Harmonics 48 fluorescent lamps in the frequency range 2 to 150 kHz, Proc.
and Quality of Power (ICHQP), pp. 728-732,25-28 May 2014. 14th Int. Confer. on Harmonics and Quality of Power (ICHQP),
[13] A Gil-de-Castro, S.K. Ro�nnberg, M.HJ. Bollen, "Harmonic 2010.
interaction between an electric vehicle and diflerent domestic [32] M. Klatt, J. Meyer, P. Schegner, "Comparison of measurement
equipment", International Symposium on Electromagnetic methods for the frequency range of2 kHz to 150 kHz", Froc. of
Compatibility (EMC Europe), 2014,p p. 991-996. IEEE 16th Int. Confer. on Harmonics and Quality of Power
[14] S.K. Ronnberg, M. Wahlberg, MHJ. Bollen, e.M. Lundmark, (ICHQP), 25-28 May 2014,p p. 818-822.
"Equipment currents in the frequency range 9-95 kHz, measured [33] R. Langella, L. Nugnes, A Testa, "Behavior of MV lines from
in a realistic environment", Proc. 13th Int. Confer. on Harmonics 2.5 to 100 kHz",P roc. IEEE PES General Meeting, 2012.
and Quality of Power (ICHQP), 2008. [34] G. Chicco, F. Corona, R. Porumb, F. Spertino, "Experimental
[15] D. Frey, J.L. Schanen, S. Quintana, M. Bollen, C. Conrath, Indicators of Current Unbalance in Building Integrated
"Study of high frequency harmonics propagation in industrial Photovoltaic Systems", IEEE Journal of Photovoltaics, vol. 4,
networks", Int. Symposium on Electromagnetic Compatibility no. 3,M ay 2014, pp. 924-934.
(EMC EUROPE), 2012. [35] lP.S. CataI110 (ed.), Smart and Sustainable Power Systems:
[16] U. Axelsson, A Holm, M. Bollen, K. Yang, "Propagation of
Operations, Planning and Economics of Insular Electricity
harmonic emission from the turbines through the collection grid Grids, CRC Press (Taylor & Francis Group), Boca Raton, FL,
to the public grid", Proc. 22nd Int. Confer. and Exhibition on ISBN: 978-1-4987-1212-5, June 2015.
Electricity Distribution (CIRED), 2013. [36] CENELEC, Signalling on low voltage electrical installations in
[17] K. Yang, M Bollen, L. Yao, "Theoretical emission study of the frequency range 3 kHz to 148.5 kHz, European Standard
windpark grids: Emission propagation between windpark and EN50065,2001.
grid", Proc. 11 th Int. Confer. on Electrical Power Quality and
Utilisation (EPQU), 2011.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:50:39 UTC from IEEE Xplore. Restrictions apply.