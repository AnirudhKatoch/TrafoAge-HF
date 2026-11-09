Contents lists available at ScienceDirect

Electric Power Systems Research

journal homepage: www.elsevier.com/locate/epsr

Diagnosis of supraharmonics-related problems based on the effects on
electrical equipment

´
Angela Espín-Delgado *, Sarah R¨onnberg , Shimi Sudha Letha , Math Bollen

Electric Power Engineering Group, Luleå University of Technology, Sweden

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Acoustic noise
Electromagnetic interference
Leakage currents
Power cable insulation
Power quality
Supraharmonics

Supraharmonics (SH) have proliferated in low-voltage (LV) and medium-voltage (MV) grids due to the increasing
use of technologies emitting distortion in the range 2–150 kHz. Currently, no recommended practices to assess
the  effects  of  SH  on  the  electrical  system  exist.  The  propagation  of  SH  through  LV  and  MV  grids  leads  to
interference with the elements for power delivery and end-user equipment, e.g., light flicker, aging of capacitors
and  cable  terminations,  audible  noise,  and  interruption  of  electric  vehicle  (EV)  charging.  As  such  incidents
happen more often, the need for guidelines that facilitate the diagnosis of problems related to SH arises. Different
features of the SH distortion are responsible for different interferences. This article introduces guidelines for the
evaluation of the impact of SH based on the morphology of the interference. The evaluation is performed with
easy-to-use methods and formulas directly related to the characteristics of the SH distortion. The adverse effects
of SH considered are audible noise, light flicker, tripping of LV residual current devices (RCDs), and MV cable
termination failure. This  work interests field engineers and researchers  facing problems related  to SH; it also
serves as a guide for further research.

1. Introduction

Supraharmonics (SH) are current and voltage waveform distortion in
the range 2 to 150 kHz. They can be created intentionally by power line
communication (PLC) systems or unintentionally by power electronics
converters. Driven by the need of increasing the efficiency of the power
system, the shift of the power delivery paradigm into modern schemes
incites the use of technologies that contribute to the proliferation of SH
in electricity networks [1]. In the context of smart grid, smart metering
and the monitoring of power quality utilize narrow-band PLC systems
[2], and the installation of distributed generation together with the use
of  renewable  energy  sources  is  incited.  Electrification  of  the  trans-
portation sector is ongoing in several countries [3,4]. In modern society,
data management, cloud-based services, and the increasing use of arti-
ficial  intelligence  require  the  electricity  supply  to  high-performance
computing  loads.  The  described  activities  involve  the  proliferation  of
loads with switched-mode power supplies and converter-based equip-
ment using switching frequencies whose remnants appear as SH emitted
into the grid [5]. The latter has led to more frequent reports of problems
associated with SH, e.g., in CLC TR 50669 and [5–8].

Some  examples  of  equipment  that  emit  SH  are:  photovoltaic

inverters,  wind  turbine  converters,  electric  vehicle  chargers,  variable
speed drives, LED lamps, air conditioning units, computer power sup-
plies [1,4,5,7]. Ref. [9] concluded that SH are present in low-voltage
(LV)  grids  in  different  parts  of  the  world;  the  level  of  SH  presents  a
daily pattern and is higher during the day; the frequency of the SH is also
varying. The daily pattern depends on the location. Quantification of the
voltage  distortion  over  the  whole  SH  range  showed  that  the  average
values are between 0.09 and 0.56 % of the fundamental voltage though
it can be as high as 12 % with a duration of less than one minute. In [4],
SH emitted by electric vehicles were measured; the study reported SH
between frequencies from 10 up to 60 kHz and magnitudes from 30 up to
1000 mA; a single device can emit SH at multiple frequencies. Ref. [10]
showed levels of SH emitted by photovoltaic inverters in an MV instal-
lation with a magnitude of up to 2 % of the fundamental voltage. The
emission coincided with the switching frequency of the inverters and its
multiples, and it is present while power production takes place. In [11],
a SH measurement campaign in an MV installation was performed; SH
with magnitude up to 400 V at 2 kHz in a 70 kV busbar were reported.
The emission is due to static frequency converters and the levels of SH
depend on the configuration of the feeding network and the number of
converters in operation. Ref. [12,13] showed the correlation of SH with

* Corresponding author.

E-mail address: angela.espin.delgado@ltu.se (

´
A. Espín-Delgado).

https://doi.org/10.1016/j.epsr.2021.107179
Received 1 October 2020; Received in revised form 22 January 2021; Accepted 15 March 2021

ElectricPowerSystemsResearch195(2021)107179Availableonline27March20210378-7796/©2021TheAuthors.PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).´
A. Espín-Delgado et al.

the  operation  of  renewable  power  plants  in  an  MV  network.  Some
components were shown to propagate over distances of about 16 km.

The study of SH as a power quality problem is relatively recent [7].
The  lack  of  standardization  and  research  on  SH  has  left  gaps  in  the
methodology on how to assess SH distortion as a characteristic of the
power  quality.  In  the  context  of  adverse  effects  of  SH,  the  gaps  that
motivate this work are explained: 1) Although efforts to develop indices
for SH have been done before in [14], there is a gap of knowledge on
how  these  indices  relate  to  the  adverse  effects  of  SH  [15].  Immunity
levels for tests with SH are available in IEC 61000-4-19; they are not
directly linked to adverse effects. Researchers that performed immunity
tests  on  electrical  appliances  have  reported  flicker  and  audible  noise
caused by SH [16]. 2) The relation between the characteristics of SH and
their  impact  on  end-user  equipment  has  not  been  formulated.  Some
problems  related  to  SH  involve,  e.g.,  heating  in  [16,17]  while  others
involve communication protocol issues [5]. Different features of the SH
distortion are responsible for different types of impact. Further work is
necessary to understand the morphology of the interferences due to SH
[15];  research  is  ongoing  [17,18].  3)  Recommended  practices  for
assessing levels of SH, in the context of problem diagnosis associated
with  this  type  of  distortion,  have  not  been  developed.  The  lack  of
agreement  on  how  to  diagnose  a  problem  provoked  by  SH  leaves  re-
ported issues to remain anecdotal [19,20].

The need for methods to evaluate SH as a function of the incidents
they cause arises. This article pioneers the study of the characteristics of
SH associated with their effects and the formulation of recommended
practices to quantify and evaluate the severity of those effects. The aim
of  this  work  is  to  contribute  to  the  settlement  of  generally  accepted
methods for: 1) quantifying the impact of SH; 2) the diagnosis of prob-
lems related to SH.

Four  interferences  caused  by  SH  are  considered  in  this  article:
audible  noise,  light  flicker,  unwanted  tripping  of  LV  residual  current
devices (RCDs), and MV cable termination failure. Two research ques-
tions are addressed: 1) What are the relevant attributes of SH associated
with each interference phenomenon? By identifying these relevant at-
tributes, input information for the diagnosis of problems existing in an
electrical system is obtained. 2) How can the negative effects of SH be
assessed by observing the characteristics of SH that predetermine those
effects?

The approach and methods employed to answer the stated questions
are explained next. A literature review is performed to build the theo-
retical  background  of  each  interference  phenomenon.  Modelling  and
simulation, or experiments are performed to replicate the phenomenon.
Simple  methods  or  formulas  for  the  evaluation  of  SH  related  to  each
interference  are  developed.  Examples  of  the  application  of  these
methods are presented.

This  article  contributes  to  filling  the  gaps  stated  above  so:  1)  The
characteristics  of  SH  relevant  for  each  interference  are  identified.  2)
Formulas  or  methods  to  quantify  the  effects  of  SH  on  equipment  are
introduced. 3) Along with appropriate measurements and analysis of the
data, identifying the inherence of the problem, contributes to the diag-
nostic of an incident as caused by SH. Problems caused by SH can thus be
diagnosed  as  such.  This  will  encourage  research  work  on  mitigation
strategies to move forward. 4) It constitutes a guide on the analysis of SH
and diagnosis of problems by means of the evaluation of their charac-
teristics. 5) It constitutes input for standardization committees in charge
of defining emission limits in LV and MV and compatibility levels in MV
networks.

In the following sections, the four phenomena associated with SH are
studied  individually.  The  paper  concludes  with  a  summary  of  recom-
mendations for the evaluation, and a discussion on the attained results.

2. Audible noise

2.1. Reported cases

Audible noise is one of the ”most common effects” of SH [5]. Cases of
audible noise due to SH have been reported both in literature and un-
officially as customers’ experiences. Table 1 summarizes some reports of
SH causing audible noise found in the literature.

From Table 1, it is seen that SH voltages as low as 0.6 V (0.3 % where
the nominal supply voltage is 230 V) can cause audible noise. Except for
the  case in  [21],  the  SH  voltages  presented  in  Table  1  are  below  the
immunity  levels  in  IEC  61000-4-19.  A  device’s  compliance  with  IEC
61000-4-19 does not guarantee its immunity to audible noise due to SH.
The latter has been concluded also by other researchers [16].

It is recognized in IEC 61000-2-2, that audible noise can be caused by
voltages of at least 0.5 % of the nominal voltage and with frequencies
between 1 and 9 kHz.

2.2. Hearing ranges

Human beings can hear frequencies between 20 Hz and 20 kHz. The

Table 1
Some reported cases of audible noise.

Affected
equipment

Induction stove

Emitting device(s)

Converter of a
variable speed drive of
a CNC mill

Household

devices, bell
transformers
Electric vehicle

(EV)

Inverter of a
hydropower plant

EVs

Office equipment

Two UPS systems

Office equipment

Converter-fed pump

Television set

Converter in a CNC
mill

Household devices

Electric vehicle

Induction stove

Heat pump

Characteristics of the SH causing
the acoustic noise and/or further
details

Components around 5 and 10 kHz
with magnitudes 0.6 and 1.7 V
(values for the highest 5 Hz-
frequency band around 5 and 10
kHz, respectively). The spectrum of
the sound revealed a sound
pressure level (SPL) of 54 and 43 dB
corresponding with the 5 and 10
kHz components [5].
12 kHz component [5]

Several electric vehicles of one type
were charging simultaneously. The
affected devices are the emitting
devices themselves. The cause is
hypothesized to be beating of
frequencies very close to each
other: switching frequencies of
devices of the same type [5].
4 kHz switching frequency varying
between 0.2 and 0.8 V. The authors
of [5] attain beating to the cause of
the noise.
12 kHz recurrent oscillations with a
magnitude of 40 % of the
fundamental voltage at the LV side.
The emitting device was connected
to the same MV busbar as the
building’s installation that supplied
the affected devices [21].
Components around 8 kHz with a
magnitude of 3 V (value for the
highest 200-Hz frequency band
around 8 kHz) [49].
10 kHz switching frequency with a
magnitude of 0.6 A at the input
current of the EV (value for the
highest 200 Hz-frequency band
around 10 kHz). The frequency of
the acoustic noise matched the
onboard charger’s switching
frequency [44].
Several customers complained
about buzzing noise in repeated
occasions [44].

ElectricPowerSystemsResearch195(2021)1071792´
A. Espín-Delgado et al.

human hearing response is not linear with respect to the sound pressure
level  (SPL),  and  it  is  most  sensitive  between  1  kHz  and  7  kHz  [22].
Factors such as age, previous exposure to high SPL and ear health affect
hearing sensitivity [22]. Children can hear frequencies higher than 16
kHz moderately well. The human hearing response to sound pressure is
represented by the equal-loudness-level contours available in ISO 226
[22].  A contour  is  a  curve  in  the  SPL  vs.  frequency  plane  connecting
points whose coordinates represent pure tones judged to be equally loud
for a human [22]. The contour at the threshold of hearing in humans is
presented in Fig.  1(a). It represents the ”level of a sound at which, under
specified conditions, a person gives 50 % of correct detection responses
on repeated trials” [22].

2.3. State-of-the-art of the research

The acoustic noise generated by electronic devices exposed to SH is
due to electromechanical effects on capacitors and coils, e.g., magne-
tostriction and inverse piezoelectric effect. They can cause mechanical
forces that lead to mechanical oscillations. The properties of the audible
noise depend on design parameters, e.g., the size of the oscillating sur-
face and the availability of transmission paths to other parts with the
ability of vibration [18].

According to the results of the measurement campaign on 103 mass-
market  end-user  equipment  [18],  levels  of  acoustic  noise  created  by
devices  exposed  to SH  can be as  high as  40  dB(A) (A-weighted  SPL).
About 16 % of the equipment had sound emission that can be disturbing
for humans depending on their surroundings. About 12 % of equipment
emitted noise reported to be almost always recognized [18]. About 5 %
of  the  devices  emitted  sound  above  32  dB(A);  exposure  to  these  has
biological effects on humans during their sleep [23].

The tests in [18] revealed that the frequency of the sound coincides
with the applied SH frequency. A linear increase in the amplitude of the
applied voltage leads to an approximately linear increase in SPL (in dB
(A))  but  this  relation was  not  studied in  detail.  The  experiments  also
show that the relation between the magnitude of SH and the SPL de-
pends on the applied frequency. Applying 2 V at 2 kHz and 10 kHz would
lead to different SPL depending on the characteristics of the resonating
mechanical system. The operation mode of the device subjected to SH
voltages has a significant influence on its sound emission. In this sense, it
is not possible to generalize the resonance characteristic for all devices.
In  another  study  [16],  55  household  devices  were  exposed  to  SH
adjusted to the immunity levels. Approximately half of the tested de-
vices  produced  audible  noise.  Single-frequency  SH  resulted  in  more
audible  noise  cases  than  a  band  of  SH  with  equivalent  rms  value.
Inductive  devices  were  not  affected.  Series  resonance  at  the  input
impedance of the device was suspected to define the emission of audible
noise [16].

2.4. Experimental case study

An experiment is performed to replicate the correlation between the
amplitude of SH and  SPL that was hinted at in [18]. Abstracting this
relation contributes to the formulation of indications for SH relative to
audible noise.

The device under test is a computer’s power supply unit. The device
is  exposed  to  pulses  of  SH  superimposed  to  the  mains’  voltage.  The
characteristics of the injected SH are programmed and generated with a
controllable  power  supply.  A  pattern  of  SH  pulses  and  pauses  with  a
duration  of  3  s  each  is  used.  Every  pulse  carries  SH  with  a  different
amplitude. A series of 3 pulses are programmed. This test was performed
for SH frequencies: 6, 8, and 12 kHz. The sound emitted by the device is
measured with a microphone whose output (in V) is proportional to the
sound pressure (in Pa). The results are shown in Fig.  2.

Fig.  2 (a) confirms that higher SH amplitude leads to higher sound
pressure. On a shorter scale (100 ms), modulation of the SH component
can be observed in Fig.  2(b) for the test with 8 kHz SH frequency. The
modulation frequency is twice the mains’ nominal frequency; a similar
phenomenon is reported in [18]. It is seen in Fig.  2(b), that the sound
pressure  follows  the  SH  voltage  pattern:  the  highest  sound  pressure
coincides with the highest SH magnitude.

The  quantification  of  the  results  is  made  in  the  time  domain.
Recorded audio, voltage and current signals are filtered over an 800 Hz-
width band centered at the studied frequencies. Only intervals where the
amplitude of SH is the highest are quantified; a threshold of amplitude is
defined above which the rms values of the signals are calculated. The
results are summarized in Fig.   2(c). In Fig.   2(c), the sound pressure
increases linearly with the voltage, with a different slope depending on
the frequency. The current and the sound slopes coincide for 8 kHz and
12 kHz; an increase in current leads to an equivalent increase in sound
pressure for those frequencies. The results at 6 kHz do not support the
latter; further research with various devices can contribute to defining a
more  detailed  model.  The  magnitude  of  the  input  impedance  of  the
device is: 9, 6 and 2 Ω, at 6, 8 and 12 kHz, respectively.

2.5. Recommendations for the evaluation of SH

The authors’ recommendation for the evaluation of the severity of SH
voltages  in  the  context  of  audible  noise  is  to  weigh  SH  components
depending on their frequency. The frequency-dependency of the SPL of
noise caused by SH cannot be generalized for all devices. It is recom-
mended that the weighting be based on the human hearing character-
istic  (Fig.   1(a)),  which  is  internationally  accepted  and  has  been
rigorously studied [22].

To  develop  a  weighting  formula,  the  contour  at  the  threshold  of
hearing  is  taken  as  reference  (Fig.  1(a)).  The  range  of  1–20  kHz  is
considered. In Fig. 1(a), a simplification of the contour between 1 kHz
and  20  kHz  (black  solid  line)  is  shown.  This  curve  can  be  defined
mathematically in the plane by a piecewise function in three pieces. The

Fig. 1. Background and application of the developed formula.

ElectricPowerSystemsResearch195(2021)1071793´
A. Espín-Delgado et al.

Fig. 2. Experiment results: relation between SH voltage and sound pressure.

coordinates defining this piecewise function are (1 kHz, -6 dB), (5 kHz,
-6 dB), (9 kHz, 10 dB), and (20 kHz, 10 dB). A weighting coefficient, η,
dependent on the frequency is built up based on the simplified contour
(Fig.  1(a)) mirrored with respect to the horizontal axis. This is because a
weighting formula should give more weight to SH at frequencies where
the human hearing is more sensitive. E.g., according to [22], a 20 dB
tone created by a SH component at 2 kHz will be perceived louder by a
person than a 20 dB tone at 10 kHz. η is defined considering that there is
a ratio of 16 dB (6.3 p.u. on a linear scale) between the SPL at 20 kHz and
the SPL at 1 kHz for the same perceived loudness (as in the simplified
contour in Fig.  1(a)). η is defined in three pieces as in (1):

⎧

⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎩

η =

6.3
(

10

1

(cid:0)

16

20log10 (9/5)log10(f /5)+(16/20)

if 1 ≤ f ≤ 5

)

if 5 < f ≤ 9

if 9 < f ≤ 20,

(1)

f  is the frequency of the SH component in kHz.
In the following, it is assumed that the sound pressure (in Pa) of a
tone created by a SH component is proportional to the magnitude of the
SH voltage (from Fig.  2(c)). A noise severity indicator for SH (NISH) is
formulated  in  (2)  similarly  as  the  telephone  influence  factor  (TIF)  in
IEEE Std. 519. The spectrum of the voltage signal to evaluate is used. A
spectrum  with  200  Hz-bands  as  the  result  from  the  method  recom-
mended by IEC 61000-4-7 (though extending from 1 kHz to 20 kHz) is
suitable since η is defined in bands of minimum 4 kHz width.

NISH =

√

̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
)2
(
∑95
B=1

η

VB
ZB

,

(2)

VB is the voltage magnitude (rms) corresponding to the band B. ZB is the
magnitude of the input impedance of the affected device; this parameter
cannot  be  defined  deterministically  at  the  moment.  fB  is  the  central
frequency of the band B and replaces f  in (1) for the calculation of η.

NISH  serves  to  compare  several  SH  spectra  or  components  with
frequencies between 1 kHz and 20 kHz. NISH benchmarks and gives an
indication of the SH distortion’s potential to cause audible noise. The
four synthetic SH voltage components shown in Fig. 1(b) are taken as
examples. The frequencies of the components in Fig. 1(b) are chosen to
exemplify the difference between their NISH. For illustrative purposes,
ZB  is assumed 1 Ω and constant in frequency.

3. Cable termination failure

3.1. Reported cases

High levels of voltage distortion in the SH range might lead to failure
of the insulation in cable terminations in MV installations [24]. High
levels of SH are likely to be found in MV networks due to high-frequency
system resonances [25].

Failure  of  cable  terminations  of  the  resistive  stress-grading  type
occurred during the commissioning stage of the Eagle Pass installation,
which connects the U.S. and the Mexican transmission grids. An inves-
tigation revealed voltage distortion with a frequency of 12.4 kHz and
amplitude of up to 40 % of the fundamental voltage [24]. This distortion
was emitted by the voltage source converter (VSC) and was amplified by
resonance.  Two  additional  cases  where  SH  were  suspected  to  be  the
cause of failure of resistive stress-grading terminations were discussed
with different industrial agents; none of the cases have been published.
The common solution for all reported cases was replacing the termina-
tions  with  ones  with  geometric  stress-grading,  which  signifies  an  in-
crease in cost and size [24,25].

3.2. Understanding the phenomenon

The function of the stress-grading layer in a cable termination is to
control the high electric stress at the edge of the semiconductive screen.
The stress-grading layer is designed so that the electric field distributes
uniformly over it. As exposed to frequencies higher than the rated power
system  frequency,  the  electric  field  distribution  distorts  so  that  high-
stress  regions  are  created  at  the  border  between  the  stress-grading
layer  and  the  semiconductive  screen.  High  power  losses  happen  in
high-stress regions, which in turn create the hotspots on the surface of
the cable termination that accelerate the degradation [25].

3.3. State-of-the-art of the research

In  [26],  six  MV  cable  terminations  with  non-linear  stress  grading
were subjected to an accelerated aging test; for three of them, SH were
superimposed to the power frequency voltage. Two of the latter failed
after  about  five  months;  the  four  remaining  terminations  did  not  fail
during this period. The frequency of the SH distortion was set to 7.2 kHz
and its peak-to-peak value, to 15 % of the power frequency voltage. In

ElectricPowerSystemsResearch195(2021)1071794´
A. Espín-Delgado et al.

[27]  a  risk  indicator  for  SH  and  cable  termination  failure  was  intro-
duced.  The  indicator  was  based  on  a  model  of  the  cable  termination
[27], and previous theoretical [28] and experimental research [24,29].
The  cable  termination  failure  case  reported  in  [24]  was  used  as  a
reference for the risk indicator.

3.3.1. A simple method for risk evaluation

The  attributes  of  the  SH  voltage  that  give  information  about  the
power  losses  on  the  cable  termination  are  magnitude,  VSH, and  fre-
quency, fSH. The higher the magnitude and frequency of SH the higher
the  probability  of  insulation  failure  in  cable  terminations  [24].  The
model in [27] considers that the heating in the cable termination de-
pends linearly on the frequency of the voltage applied and proportion-
ally with the square of the magnitude of the voltage. A simple evaluation
method was introduced in [27] to decide whether given levels and fre-
quencies of SH represent a risk to cable terminations.

The  evaluation  uses a  frequency-domain  approach and  is  made  in
two steps [27]. The decision is made based on the worst result obtained
in each step. This is due to the high variability of characteristics of SH
spectra.  Some  SH  have  a  defined,  fixed  and  recognizable  frequency;
some extend over a band of frequencies. The difficulty is in finding a
reliable representation of the magnitude of the SH (developing such a
method is out of the scope of this paper). The two-step evaluation pro-
posed in [27] aimed to cover different scenarios.

Assuming that a frequency spectrum of the voltage is available, with
2 kHz grouping bands from 2 up to 150 kHz, the two-step evaluation is
described below. An example of the application of this evaluation was
presented in [27].

Compare  the  spectrum  to  the  risk  areas  presented  in  Fig.  3  The  SH
voltage, VSH, can be expressed as a ratio of the rated voltage, Vrated. m
gives an indication of the similarity of the evaluated case to the refer-
ence  case  (Eagle  Pass).  m = 1  means  that  the  failure  at  Eagle  Pass
occurred under equivalent  VSH
Vrated  and fSH  conditions as the evaluated case.
The areas originate from a simplification of the Eagle Pass failure con-
dition. The specifications of these areas and further details can be found
in [27].

The power loss summation (based on [30]) is considered by the calcu-

lation [27]:

QSH =

∑74

B=1

V 2
BfB
ratedfrated

V 2

,

(3)

where VB  and fB  are the voltage magnitude and central frequency of the
frequency band, B. In the Eagle Pass case QSH(cid:0) EPass = 20. The Eagle Pass
case serves as a reference and, taking a conservative stance, m = 0.25,
the risk of failure threshold is defined: m⋅QSH(cid:0) EPass = 5.

3.4. Recommendations for the evaluation

The time-wise exposition of the cable termination to SH is relevant.
Along with the summary presented in [27], the experiments carried out
in [26] give useful information about this matter. In this experiment, the
SH  were  not  applied  continuously  during  the  whole  period  of  the
fundamental voltage but in short pulses every 1.3 ms. Two cable ter-
minations failed under these circumstances and one of them showed a

Fig. 3. Risk areas based on m and Eagle Pass case [27].

significant  increase  in  the  dissipation  factor.  The  latter  suggests  that,
even when the pulses were short and discontinuous, the exposition of the
cable terminations to repetitive stress caused by SH during long periods
(months)  leads  to  premature  aging.  Methods  for  calculating  the
loss-of-life  of  cable  insulation  use  Arrhenius  equation  as  well  as  the
current loading pattern over time [31]. This reasoning can be applied to
SH in future works. QSH  can be evaluated statistically by considering the
99% percentile values calculated every 10 minutes.

4. Tripping of LV residual current devices

4.1. Reported cases

Cases of unwanted tripping of LV residual current devices have been
reported  in  several  countries  [3,19,32–34].  Although  SH  are  the  sus-
pected cause, no systematic study has been made to confirm this premise
and to understand the mechanism of the incidents regarding the device.
In  [3],  earth-leakage  protective  devices’  sensitivity  provoked  the
unwanted  interruption  of  electric  vehicles  (EV)  charging.  In  one  case
[35], the cause was a ventilation fan that caused high common-mode
voltage in the SH range. Ref. [32] reported unwanted tripping of RCDs
during EV charging in an EV test laboratory; frequency beating of SH
was  the  suspected  cause.  Users  of  EV  reported  interruptions  in  the
charging  process  when  high  levels  of  SH  on  the  neutral-to-protective
earth (N-PE) voltage were present [19]. Communication modems had
several  communication  failures  when  powered  by  an  uninterruptible
power supply (UPS); high levels of SH were found on the phase-neutral
and  phase-ground  voltages  [33].  Liew  in  [34]  reported  the  nuisance
tripping  of  a  residual  current  circuit  breaker  (RCCB).  Measurements
revealed  28  kHz  components  in  leakage  current  with  27  mA
peak-to-peak value.

4.2. State-of-the-art of the research

Ref. [36] described the effect of higher-order harmonics on the in-
ternal elements of the RCD as ”rather complicated and controversial.” In
some cases, it is possible to speak of the increase of probability of false
tripping; in other cases, about the danger of RCD malfunction ("blind-
ing"). Research on the influence of harmonics on RCDs has been per-
formed before [37]. SH have not been studied to that extent. A common
conclusion in the literature is that the waveform of the residual current
has an impact on the sensitivity of the RCD. A pointed-topped waveform
is more prone to cause unwanted tripping than a flat-topped one. It is
known that the third harmonic has a strong influence on the waveform
shape of the residual current. A phase-angle of the third harmonic in the
residual current close to 180

is the worst case [37].

◦

As  per  manufacturers  of  RCDs  [38,39],  one  of  the  most  frequent
causes of unwanted tripping of RCDs is the leakage of currents to pro-
tective earth (PE) through interference filters and stray capacitances in
circuits where components up to 20 kHz are present; the earth-leakage
current increases with the frequency. Ref. [40], shows the propagation
of  SH  to  ground  through  electromagnetic  interference  (EMI)  filters.
Measurements verified that the SH injected by a device propagate to the
PE of an adjacent device through its EMI filter, which causes the rms
value  of  the  PE  current  to  increase.  According  to  [41],  the  leakage
current,  in  a  household  environment,  is  composed  mainly  of  SH.
Nowadays, there are various types of RCDs in the market. Type Bfq and
type B+ work with an adapted tripping curve up to 20 kHz. Type A and
AC are specified for alternating currents only at 50/60 Hz.

4.3. Understanding the phenomenon

The mechanism in which SH would affect RCDs would be similar to
the one for harmonics. To understand the functioning of RCDs under SH,
a  simple  RCD  with  an  electromagnetic  relay  is  considered.  This  RCD
consists of two main parts: the summation current transformer and the

ElectricPowerSystemsResearch195(2021)1071795´
A. Espín-Delgado et al.

trip relay with a permanent magnet. The summation transformer per-
forms a sum of the instantaneous values of the three phases currents and
the  neutral  current.  The residual  current (IΔ) after  that  summation is
considered  to  be  the  earth-leakage  current.  The  relay  compares  that
residual current against a given reference and acts once it is surpassed.
An RCD is characterized by its rated residual operating current IΔn
(typically  30  mA  in  an  LV  installation),  and  its  residual  non-tripping
current, IΔn0. The former is the effective value of the residual current
when the RCD must trip. The latter is the maximum current at which the
circuit breaker will not trip and it corresponds to 50% of IΔn.

The hypothesis of how SH impact the functioning of RCDs is split up
into  two  parts:  1)  that  EMI  filtering  increases  the  probability  of  RCD
tripping (type AC and A); 2) the characteristics of SH have an impact on
the sensitivity of the RCD. Notice that statement 1) has to do with the
characteristics of the installation, and statement 2) has to do with the
characteristics of the RCD. Both are related to the characteristics of the
SH distortion.

the results of the simulation when the third harmonic is present on the
residual current. The third harmonic for this signal has a magnitude of
◦
phase-angle. The waveform changes and the peak
13 mA rms and a 92
of the current will cause the RCD to trip.

Fig. 4 (c) shows the results of the simulation when SH with 13 mA
magnitude and 2 kHz frequency are superimposed to the reference re-
sidual current. The magnetic force crosses the threshold so the RCD will
trip. A current of the same magnitude but with an increased frequency
will result in a lower peak-to-peak value of the magnetic force. The same
13 mA at 2 kHz and 20 kHz at the primary side will end up with different
amplitudes  at  the  secondary  side  due  to  the  frequency-dependent
propagation through the summation transformer.

The higher the frequency of the SH is, the lower their propagation to
the electromagnet of the relay. The magnitude of the SH that will make
the RCD trip is approximately the same as for the magnitude of the third
◦
harmonic with 92

phase-angle.

4.3.1. EMI filtering and SH

4.4. Evaluation method and discussion

The higher the frequency and the amplitude of the SH the higher the
probability of unwanted tripping. This is due to the capacitive charac-
teristic of the couplings between phases or neutral and earth. The higher
the  propagation  of  SH  to  earth,  the  higher  the  residual  current,  IΔ,
measured by the current summation transformer in an RCD.

4.3.2. Propagation of SH through the RCD

Consider the simple model of an RCD presented in Fig. 4(a). This case
study  is  merely  for  exemplification  purposes  and  aims  to  explain  the
operation of the RCD under the presence of SH at different frequencies.
The circuit represents the summation current transformer in which the
primary  current  corresponds  to  a  given  residual  current  IΔ.  The  sec-
ondary  current  flows  through  the  electromagnet  of  the  trip  relay
(modeled as an inductance). The trip relay is fitted with a permanent
magnet.  Once  the  secondary  current  is  conducted  into  the  electro-
magnet, the attraction force of the permanent magnet is weakened. If the
resulting magnetic force is lesser than a given threshold, the relay will
trip. This model is a simplified version of that one studied in [37].

In Fig. 4(a), the interest is in the primary and the secondary current,
and the resulting magnetic force in the relay. Fig. 4(b) shows the results
of the simulation for a synthetic input current with no third harmonic. A
threshold is defined for demonstrative purposes. As long as the magnetic
force is higher than the threshold, the RCD will not trip. Fig. 4(c) shows

The relative crest factor [42] of the residual current, CFrΔ, as defined
in (4) characterizes the shape of the signal and its potential to cause RCD
unwanted tripping. IΔmax  is the maximum value of the residual current
and  IΔrms, its  rms  value.  CFrΔ = 1  for  a  sine  wave  and  CFrΔ > 1  for  a
pointed-topped wave. Residual current (primary current) in Fig. 4(b) to
4(c) give CFrΔ  of 1.19, 1.47 and 1.44, respectively.

CFrΔ =

√

IΔmax
̅̅̅
IΔrms
2

(4)

The  relevant  variable  for  this  analysis  is  the  earth-leakage  current,
which might not be accessible in all cases. An estimation of the earth-
leakage current can be done if the phase currents and the neutral cur-
rents are available.

The  analysis  in  Section  4.3  leads  to  conflicting  conclusions  about
how the frequency of SH would impact the unwanted tripping of RCDs.
For  the  system,  the  higher  the  frequency  of  SH  the  higher  the  earth-
leakage  current  and  the  higher  the  probability  of  unwanted  tripping.
On the other hand, the higher the frequency of the SH present in the
residual current the higher the energy needed for the RCD to trip. The
behavior of the RCD in this regard is highly dependent on its design [37]
and at this point, no general conclusions can be drawn on SH impact.
Extensive experimental tests are necessary to reach any generalization.

Fig. 4. RCD simulation. Waveform plots – Left: primary current (black), secondary current (gray). Right: magnetic force (solid), threshold (dotted).

ElectricPowerSystemsResearch195(2021)1071796´
A. Espín-Delgado et al.

5. Light output variations or flicker

5.1. Reported cases

The term ”flicker”, in this section, refers to photometric flicker and
describes ”light output variations”. Flicker of LED lamps was observed
by a commercial customer in the USA [43]. Investigation of voltage at
the  location  revealed  the  presence  of  high-frequency  distortion  and
notches. The distortion showed frequencies between 5 and 10 kHz and
amplitudes up to 30 V peak. The distortion was not synchronized with
the fundamental voltage; the point-on-wave of the distortion changed
with  a  period  of  5  s.  Further  cases  of  flicker  have  been  reported  in
Norway [44], Sweden [19] and USA [20] during the charging of EVs. SH
are suspected to be the cause.

5.2. State-of-the-art of the research

It is recognized that LED lamps behave differently from incandescent
lamps  and  that  efforts  should  be  made  to  re-define  flicker  indicators
[45].  The  standardized  flickermeter  defined  in  IEC  61000-4-15  con-
siders voltage fluctuations with frequencies up to 40 Hz and is based on
the  response  of  an  incandescent  light  bulb.  SH  superimposed  on  the
fundamental voltage can not be perceived by the human eye. A different
phenomenon (explained later in this section) is responsible for flicker on
LED lamps due to SH and it concerns the functioning of the electronic
driver [46].

In [43], five LED lamps were tested under grid voltage superimposed
with  time-  and  frequency-varying  SH.  The  point-on-wave  of  the  SH
distortion was also time-varying. Two lamps were immune to this SH
distortion, one lamp showed a constant decrease in its light output, and
two, variations in their light output with a period of approximately 10 s.
In [16], a group of LED and compact fluorescent (CF) lamps were
tested under SH with magnitudes adjusted to the immunity levels in IEC
61000-4-19.  The  flicker  assessment  was  made  by  visual  inspection.
Lamps without power factor correction (PFC) stage were not affected by
the distortion. Lamps with active PFC flickered when exposed to SH in
the range 2 to 20 kHz. Lamps with a capacitor divider topology flickered
when exposed to frequencies from 2 up to 95 kHz.

In [46], an LED lamp that consists of a full bridge rectifier with a
smoothing capacitor was exposed to a supply voltage superimposed with
SH with amplitude 7 V rms at 12.5 kHz. The current at the input of the
rectifier  and  the  light  output  were measured.  The  interest  was  in  the
transition between the conduction and the blocking state of the diodes of
the rectifier, which can be seen in the current. It was seen that the SH
component  forced  the  diode  into  blocking/conduction  intermittently.
The  longer  this  intermittent  conduction  period  was,  the  stronger  the
impact of intermittent conduction on the modulation depth of the light
intensity output of the lamp. The length of the intermittent conduction
period  depends  on  the  amplitude  and  frequency  of  the  voltage  SH
superimposed to the fundamental voltage. Only SH at the zero-crossing
of  the  current  influenced  the  light  intensity-modulation  depth.  See
further details in [46].

Ref. [16,43,46] showed that flicker due to SH is highly dependent on
the topology of the lamp. Some lamps are more sensitive than others;
some lamps are insensitive to SH.

5.3. Understanding the phenomenon: hypothesis and experimental
investigation

The first condition for flicker is intermittent conduction. SH at the
zero-crossing of the input current of the LED lamp (causing intermittent
conduction) modify the modulation depth of the light output but they do
not necessarily cause flicker. The flicker condition meets when SH are
not synchronized with the fundamental voltage, i.e., the characteristics
of  the  SH  at  each  current’s  zero-crossing  are  not  constant.  The  latter
causes the modulation depth to vary over time which might be sensed as

flicker  by  the  human  eye.  This  hypothesis  is  based  on  the  research
presented in [46]. Evidence that supports this hypothesis was found in
[43].

One  EV  user  complained  about  light  flicker  at  home  during  the
charging of the EV. The EV is transported to the laboratory for further
investigation. The frequency spectrum and spectrogram of the current of
the EV while charging are shown in Fig. 5(a) and 5(b), respectively. In
Fig. 5(b), the time-frequency behavior of the SH emission of the EV is
represented  by  the  red  color.  The  continuous  black  line  in  Fig.  5(b)
represents the time domain current waveform which is superimposed on
the figure for reference.

The EV  emits  SH  that vary  both in  frequency  and  time as seen  in
Fig. 5(b). As shown in Fig. 5(b), the variation of the frequency of the SH
component  is  not  synchronized  with  the  fundamental  component’s
alternating behavior. It is important to mention that the fundamental
current is in phase with the fundamental voltage. The SH variation in
Fig. 5(b) is cyclic with 8 cycles per 200 ms, i.e., one cycle lasts 25 ms and
the frequency of this variation is 40 Hz.

5.4. Evaluation of the characteristics of SH

In line with the hypothesis in Section 5.3, there are two conditions
for flicker caused by SH in sensitive lamps: 1) intermittent conduction,
which depends on the amplitude of SH and their point-on-wave in the
voltage signal, and the input impedance of the lamp; 2) time-variations
of the SH distortion not synchronized with the supply voltage, i.e., time-
varying point-on-wave of the SH distortion.

To evaluate whether SH might cause LED lamps to flicker, it is rec-
ommended to use time-frequency domain plots and the strategy shown
in Fig. 5(b) to look for non-synchronized SH. Namely, inspecting the SH
at the zero-crossing of the supply voltage: if they have different char-
acteristics (frequency, magnitude) each half-cycle, then this is a red flag
for flicker. The input current of a suspected interfering device can also be
inspected, e.g., the current of an EV. The assessment of light output is not
covered in this paper. For this matter, refer to IEC 61547-1.

6. Summary of investigation and recommendations

This  section  summarizes  the  recommendations  and  the  proposed
methods  for  the  evaluation  of  SH  relative  to  the  four  studied  in-
terferences. The methods are presented in the form of flowcharts that
should be read from top to bottom and from left to right. The recom-
mended actions to take on each case are explained afterward.

6.1. Processing of data

Proper treatment of the quantification noise is important before the
calculation of the indicators. Including quantification noise can affect
the results given by the indicators. This process is out of the scope of this
paper. A perspective of gap-less measurements is considered here.

6.2. Audible noise

• The existing immunity levels do not guarantee the absence of audible

noise due to SH.

• Frequency of SH defines the frequency of audible noise. Switching
frequencies and those whose multiples are between 1 and 20 kHz are
susceptible to cause audible noise. A single-frequency component is
more  susceptible  to  cause  audible  noise  than  a  band  of  SH  with
equivalent rms value.

• The higher the voltage, the higher the sound pressure of the noise
produced. This result is device- and frequency-dependent. The input
impedance of the device seemingly defines this dependency. Mostly
capacitive devices are affected.

Fig.  6 describes the method for the evaluation of SH to identify red

ElectricPowerSystemsResearch195(2021)1071797´
A. Espín-Delgado et al.

Fig. 5. Input current of an EV that causes light flicker.

Fig. 6. Flowchart for evaluation of SH related to audible noise.

flags related to audible noise and for finding the source of SH responsible
for an identified sound. In case of audible noise caused by SH, EMI filters
are a solution. Increasing the electrical distance between the source of
the SH and the affected devices is an option that requires further study.
The severity of SH voltages related to the risk of them causing audible
noise can be quantified using (1) and (2). A reference of SH impedance
to model low-voltage devices is needed.

6.3. Cable terminations

In cable terminations, resistive stress-grading is a risk factor. There
are  no  records  that  cable  terminations  of  the  geometric  type  have
problems operating under the influence of SH. Higher frequencies and
voltage magnitudes represent higher risk. Fig.  7 describes the method
for  the  evaluation  of  SH  to  identify  red  flags  related  to  insulation
problems in cable terminations. Eagle Pass case is used as a reference but
a more conservative approach is also given. Once a red flag has been

Fig. 7. Flowchart for evaluation of SH related to cable termination failure. Areas and colors refer to Fig.  3.

ElectricPowerSystemsResearch195(2021)1071798´
A. Espín-Delgado et al.

identified, partial discharge measurements should be paired with dissi-
pation factor measurement for further diagnosis [26].

6.4. Unwanted tripping of RCDs

• The relevant quantity to evaluate is the residual current. It is rec-
ommended to keep the residual current under 30% of the nominal
tripping current as per IEC 62350.

• Topology-dependent. Types A and AC are more vulnerable.

Fig.  8 describes the method for the characterization of the residual
current  and  the  evaluation  to  identify  red  flags  related  to  RCDs’  un-
wanted  tripping.  In  case  of  recurrent  unwanted  tripping,  it  is  recom-
mended  to  upgrade  the  type  of  RCD  to  one  that  is  designed  to  work
under high levels of SH, e.g., type B.

6.5. Light flicker

The frequency of SH does not define the frequency of flicker. The
amplitude is an influencing factor but the impedance and the topology of
the device dominates the condition whether this phenomenon is present.
Fig.  9 describes the method for the evaluation of SH to identify red flags
related to light flicker on LED lamps. As the phenomenon is dependent
on the topology of the LED lamp, this problem can be counteracted by
upgrading the lighting equipment to lamps with a different topology.

7. Discussion

The list of negative impacts associated with SH is even longer. Other
phenomena such as aging of capacitors, electronic clocks running too
fast, interference with PLC have been recognized and are not included in
this  paper.  For  some  phenomena,  an  indicator  would  be  rather
straightforward, i.e., a curve for acceptable levels of PLC on LV grids
already exists in EN 50160 up to 95 kHz. Others require in-depth study,
i.e.,  lifetime  degradation  of  electrolytic  capacitors  in  end-user  equip-
ment [17]

7.1. On the prevention and countermeasures to SH-related problems

Two  alternatives  on  how  to  approach  SH-related  issues  can  be
considered: either to prevent them or to counteract them once they are
reported. Prevention of SH-related issues implies an optimized decision
in the context of emission vs. immunity. This is a decision that must be
taken by standardization committees in agreement with manufacturers
of equipment (both emitters and non-emitters of SH). In its current state,
limits for non-intentional SH emission exist for some equipment (LED
lamps and induction stoves from 9 up to 150 kHz in EN 55011 and EN
55015, respectively) and for intentional SH emission in EN 50160 (up to
95 kHz). Immunity levels are given in IEC 61000-4-19 but, as explained
before, they do not guarantee the absence of SH-related problems. The
research conducted here shows that it is crucial to consider the nature of

the  phenomenon  in  the  development  of  the  following  updates  of
compatibility standards. Once new regulations have been published, the
solution  can  only  be  applied  to  equipment  in  the  design  stage,  e.g.,
implementing EMI filters and power electronics schemes that modify the
spectral characteristics of the emission [47,48]. The second alternative
is to focus on counteracting specific problems under the assumption that
they will seldom appear. Some options to apply in this case are: instal-
lation of filters [24], replacing the affected device [34], modifying the
configuration of the local network [11].

8. Conclusion

8.1. Summary of contributions

The methods  and  formulas  proposed to  establish  a  benchmark for
measurement,  evaluation  of  SH  related  to  four  interferences,  and  the
introduction of a framework for reporting those interferences constitute
the most important contributions of this article. These contributions are
summarized  by  Fig.   6  to  9.  The  innovation  of  this  work  lies  in  the
interference-dependent  approach  to  the  development  of  methods  for
quantifying  power  quality  in  the  context  of  SH.  Further,  this  article
contributes  to  the  state-of-the-art  in  research  on  consequences  of  SH
with the following material:

• An identification of the relevant characteristics of SH related to four
interference  phenomena:  audible  noise,  cable  termination  failure,
unwanted tripping of RCDs, and light flicker.

• Research shows that the relevant characteristics differ for different
phenomena. Performance indicators and limits have been developed
where applicable.

• A review of the literature and a summary of reported cases of the four

interferences.

8.2. Recommendations for future research

The  indicators  introduced  in  this  paper  are  a  starting  point  to
quantify the impact of SH. Recommended directions for future work are:

• Immunity  tests  with  a  significant  sample  of  devices,  registry,  and
quantification of the effects of SH using the indicators proposed in
this article.

• Need the indicators to be more complex to better describe the effects
of SH, further research is needed. Increasing the complexity of these
methods  has  drawbacks  in  terms  of  implementation  since  higher
computational resources would be required.

• Measurement  campaigns  on  the  SH  impedance  of  low-voltage

devices.

• Relating the indicators with the propagation of SH, e.g., how far in a

distribution feeder can SH cause interferences.

Fig. 8. Flowchart for evaluation of SH related to unwanted tripping of RCDs.

ElectricPowerSystemsResearch195(2021)1071799´
A. Espín-Delgado et al.

Fig. 9. Flowchart for evaluation of SH related to light flicker.

CRediT authorship contribution statement

´
Angela Espín-Delgado: Conceptualization, Formal analysis, Inves-
tigation,  Methodology,  Writing  -  original  draft,  Visualization,  Valida-
tion,  Software.  Sarah  R¨onnberg:  Conceptualization,  Methodology,
Funding acquisition, Project administration, Resources, Writing - review
& editing, Supervision. Shimi Sudha Letha: Conceptualization, Meth-
odology, Writing - review & editing. Math Bollen: Conceptualization,
Methodology,  Resources,  Funding  acquisition,  Supervision,  Project
administration.

Declaration of Competing Interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgements

The Swedish Transportation Administration and The Swedish Energy

Research Centre.

References

[1] A.A. Alkahtani, S.T.Y. Alfalahi, A.A. Athamneh, A.Q. Al-Shetwi, M.B. Mansor, M.
A. Hannan, V.G. Agelidis, Power quality in microgrids including supraharmonics:
Issues, standards, and mitigations, IEEE Access 8 (2020) 127104–127122, https://
doi.org/10.1109/ACCESS.2020.3008042.

[2] I. Fernandez, N. Uribe-P´erez, I. Eizmendi, I. Angulo, D. de la Vega, A. Arrinda,

T. Arzuaga, Characterization of non-intentional emissions from distributed energy
resources up to 500 kHz: A case study in Spain, Int. J. Elect. Power Energy Syst.
105 (2019) 549–563, https://doi.org/10.1016/j.ijepes.2018.08.048.

[3] H. Kirkeby, V. Bøe, K. Hartvigsen, K. Sagen, Charging problems in EV paradise.
Proceedings of the 25th International Conference on Electricity Distribution
(CIRED), 2019, https://doi.org/10.34890/684.

[4] T.M.H. Slangen, T. van Wijk, V.

´
Cuk, J.F.G. Cobben, The harmonic and
supraharmonic emission of battery electric vehicles in the Netherlands.
Proceedings of the International Conference on Smart Energy System and
Technology (SEST), 2020, pp. 1–6, https://doi.org/10.1109/
SEST48500.2020.9203533.

[5] J. Meyer, V. Khokhlov, M. Klatt, J. Blum, C. Waniek, T. Wohlfahrt, J. Myrzik,

Overview and classification of interferences in the frequency range 2 - 150 kHz
(supraharmonics). Proceedings of the International Symposium on Power
Electronics, Electical Drives, Automation and Motion (SPEEDAM), IEEE, 2018,
pp. 165–170.

[6] F. Leferink, C. Keyer, A. Melentjev, Static energy meter errors caused by conducted
electromagnetic interference, IEEE Electrmagn. Compat. Mag. 5 (4) (2016) 49–55,
https://doi.org/10.1109/MEMC.2016.7866234.

[7] S.K. R¨onnberg, M.H.J. Bollen, H. Amaris, G.W. Chang, I.Y.H. Gu, Ł.H. Kocewiak,
J. Meyer, M. Olofsson, P.F. Ribeiro, J. Desmet, On waveform distortion in the

frequency range of 2 kHz 150 kHz – review and research challenges, Elect. Power
Syst. Res. 150 (2017) 1–10, https://doi.org/10.1016/j.epsr.2017.04.032.

[8] R. Purnamaputra, B. Sudiarto, The impact of electric disturbance at frequencies 2-
150 kHz on analogue kilowatt-hour meter. Proceedings of the IOP Conference on
Series: Earth and Environmental Science 599, 2020, p. 012014, https://doi.org/
10.1088/1755-1315/599/1/012014.

[9] S. R¨onnberg, A. Gil de Castro, A. Espín-Delgado, Variations of supraharmonic
emissions in low voltage networks. Proceedings of the 25th International
Conference on Electricity Distribution (CIRED), 2019, https://doi.org/10.34890/
234.

[10] J. Yaghoobi, F. Zare, D. Solatialkaran, Harmonic emissions in 0-9 kHz frequency

range and transient effects in grid-connected inverters utilised in solar farms.
Proceedings of the 19th International Conference on Harmonics and Quality of
Power (ICHQP), 2020, pp. 1–6, https://doi.org/10.1109/
ICHQP46026.2020.9177925.

[11] O. Lennerhag, A. Dernfalk, P. Nygren, Supraharmonics in the presence of static

frequency converters feeding a 16 2/3 Hz railway system. Proceedings of the 19th
International Conference on Harmonics and Quality of Power (ICHQP), 2020,
pp. 1–6, https://doi.org/10.1109/ICHQP46026.2020.9177901.

[12] A. Novitskiy, S. Schlegel, D. Westermann, Analysis of supraharmonic propagation
in a MV electrical network. Proceedings of the 19th International Scientific
Conference on Electronics Power Engineering (EPE), 2018, pp. 1–6, https://doi.
org/10.1109/EPE.2018.8396041.

[13] A. Novitskiy, S. Schlegel, D. Westermann, Measurements and analysis of

supraharmonic influences in a MV/LV network containing renewable energy
sources. Proceedings of the Electric Power Quality and Supply Reliability
Conference on (PQ) Symposium on Electronic Engineering and Mechatronics
(SEEM), 2019, pp. 1–6, https://doi.org/10.1109/PQ.2019.8818260.

[14] A. Grevener, J. Meyer, S. R¨onnberg, M. Bollen, J. Myrzik, Survey of supraharmonic
emission of household appliances, CIRED - Open Access Proc. J. 1 (2017) 870–874,
https://doi.org/10.1049/oap-cired.2017.0458.

[15] L. Alfieri, A. Bracale, P. Varilone, Z. Leonowicz, P. Kostyla, T. Sikorski,

M. Wasowski, Methods for assessment of supraharmonics in power systems. Part I:
Theoretical issues. Proceedings of the International Conference on Clean Electronic
Power (ICCEP), 2019, pp. 110–115, https://doi.org/10.1109/
ICCEP.2019.8890176.

[16] V. Khokhlov, J. Meyer, P. Schegner, D. Agudelo-Martínez, A. Pavas, Immunity
assessment of household appliances in the frequency range from 2 to 150 kHz.
Proceedings of the 25th International Conference on Electricity Distribution
(CIRED), 2019, https://doi.org/10.34890/283.

[17] D. Darmawardana, S. Perera, D. Robinson, J. David, J. Meyer, U. Jayatunga,

Impact of high frequency emissions (2150 kHz) on lifetime degradation of
electrolytic capacitors in grid connected equipment. Proceedings of the IEEE Power
Energy Social General Meeting (PESGM), 2019, pp. 1–5, https://doi.org/10.1109/
PESGM40551.2019.8973849.

[18] P.M. K¨orner, R. Stiegler, J. Meyer, T. Wohlfahrt, C. Waniek, J.M.A. Myrzik,
Acoustic noise of massmarket equipment caused by supraharmonics in the
frequency range 2 to 20 kHz. Proceedings of the 18th International Conference on
Harmonics and Quality of Power (ICHQP), 2018, pp. 1–6, https://doi.org/
10.1109/ICHQP.2018.8378856.

[19] T. Busatto et al., Impact of electric vehicle charging on the power grid, Internal

report, Luleå Univ. Technol., Elect. Power Eng., 2020.

[20] Tesla Motors Club, Lights in house flicker while charging new model 3, 2019, URL

https://teslamotorsclub.com/tmc/threads/lights-in-house-flicker-while-chargin
g-new-model-3.149841/.

[21] C. Unger, K. Krüger, M. Sonnenschein, R. Zurowski, Disturbances due to voltage
distortion in the kHz range – experiences and mitigation measures. Proceedings of
the CIRED - 18th International Conference on Electricity Distribution, 2005,
pp. 1–4, https://doi.org/10.1049/cp:20051018.

ElectricPowerSystemsResearch195(2021)10717910´
A. Espín-Delgado et al.

[22] ISO/TC 43 Acoustics, ISO 226:2003 Acoustics – Normal equal-loudness-level,

[36] V. Gurevich, RCD nuisance tripping: who’s guilty and what needs to be done?

2003.

[23] C. Hurtley, Night noise guidelines for Europe, WHO Europe, 2009.
[24] L. Paulsson, B. Ekehov, S. Halen, T. Larsson, L. Palmqvist, A. Edris, D. Kidd, A.J.
F. Keri, B. Mehraban, High-frequency impacts in a converter-based back-to-back
tie; the Eagle Pass installation, IEEE Trans. Power Del. 18 (4) (2003) 1410–1415,
https://doi.org/10.1109/TPWRD.2003.817724.

[25] T. Bengtsson, F. Dijkhuizen, L. Ming, F. Sahlen, L. Liljestrand, D. Bormann,

R. Papazyan, M. Dahlgren, Repetitive fast voltage stresses-causes and effects, IEEE
Elect. Insul. Mag. 25 (4) (2009) 26–39, https://doi.org/10.1109/
MEI.2009.5191414.

Global J. Res. Eng., Elect. Electron. Eng. 13 (11) (2013) 30–40, https://doi.org/
10.15588/1607-3274-2013-2-1.

[37] F. Freschi, High-frequency behavior of residual current devices, IEEE Trans. Power
Del. 27 (3) (2012) 1629–1635, https://doi.org/10.1109/TPWRD.2012.2191423.

[38] F. Step´an, Residual current devices – Application guide, EATON, 2017.
[39] N. Lucius, J. Rey, M. Paupert, S. Tian, Why to choose type B earth leakage

protection for safe and efficient people protection, Schneider Electric, 2018.
[40] J. Sutaria, K.M. Uddin, S. R¨onnberg, M.H.J. Bollen, Propagation of supraharmonics

through EMI filters with varying loads. Proceedings of the IEEE Cigr´e NORPIE,
2019.

[26] M. Knenicky, R. Prochazka, J. Hlavacek, O. Sefl, Impact of high-frequency voltage

[41] A.M. Blanco, F. Müller, J. Meyer, P. Schegner, Characterization of the leakage

distortion emitted by large photovoltaic power plant on medium voltage cable
systems, IEEE Trans. Power Del. (2020) 1–9, https://doi.org/10.1109/
TPWRD.2020.3016952.
´
A. Espín-Delgado, S. Sudha Letha, S.K. R¨onnberg, M.H.J. Bollen, Failure of MV
cable terminations due to supraharmonic voltages: A risk indicator, IEEE Open J.
Ind. Appl. 1 (2020) 42–51, https://doi.org/10.1109/OJIA.2020.2998000.
[28] S.A. Boggs, Theory of a field-limiting dielectric, IEEE Trans. Power Del. 9 (3)

[27]

(1994) 1391–1397, https://doi.org/10.1109/61.311167.

[29] S. Banerjee, S.H. Jayaram, Thermal effects of high-frequency voltage on medium
voltage cable terminations. Proceedings of the IEEE International Conference on
Solid Dielectrics, 2007, pp. 669–672, https://doi.org/10.1109/
ICSD.2007.4290902.

[30] B. Sonerud, T. Bengtsson, J. Blennow, S.M. Gubanski, Dielectric heating in

insulating materials subjected to voltage waveforms with high harmonic content,
IEEE Trans. Dielectr. Electr. Insul. 16 (4) (2009) 926–933, https://doi.org/
10.1109/TDEI.2009.5211835.

[31] G. Parise, L. Martirano, L. Parise, L. Gugliermetti, F. Nardecchia, A life loss tool for
an optimal management in the operation of insulated LV power cables, IEEE Trans.
Ind. Appl. 55 (1) (2019) 167–173, https://doi.org/10.1109/TIA.2018.2866982.
´
Cuk, S. Cobben, The propagation and interaction of

[32] T. Slangen, T. van Wijk, V.

supraharmonics from electric vehicle chargers in a low-voltage grid, Energies 13
(15) (2020) 3865, https://doi.org/10.3390/en13153865.

[33] M. Lundmark, High-frequency noise in power grids, neutral and protective earth,

Lic. thesis, Luleå Univ. Technol., Elect. Power Eng., 2006.

[34] A. Liew, Nuisance trippings of residual current circuit breakers or ground fault
protectors of power sources connected to computer and electronic loads, Elect.
Power Syst. Res. 20 (1) (1990) 23–30, https://doi.org/10.1016/0378-7796(90)
90022-U.

[35] Unitech Power Systems, Interferens stoppet elbilladere, 2019, URL https://www.

unitech.no/nyheter/interferens-stoppet-elbilladere-article354-629.html.

currents produced by household electronic devices. Proceedings of the 19th
International Conference on Harmonics and Quality of Power (ICHQP), 2020,
pp. 1–6, https://doi.org/10.1109/ICHQP46026.2020.9177876.

[42] M.H. Bollen, I.Y. Gu, Signal processing of power quality disturbances 30, John

Wiley & Sons, 2006.

[43] G. Singh, E.R. Collins, S.K. R¨onnberg, E.O.A. Larsson, M.H.J. Bollen, Impact of high
frequency conducted voltage disturbances on LED driver circuits. IEEE Power
Energy Social General Meeting, 2017, pp. 1–5, https://doi.org/10.1109/
PESGM.2017.8274378.

[44] H. Kirkeby, M. Lillebo, EMC-problemer i smarte hus og mikronett. Technical

Report, EMC-nett, 2019.

[45] J. Drapela, R. Langella, A. Testa, A.J. Collin, X. Xu, S.Z. Djokic, Experimental

evaluation and classification of led lamps for light flicker sensitivity. Proceedings
of the 18th International Conference on Harmonics and Quality of Power (ICHQP),
2018, pp. 1–6, https://doi.org/10.1109/ICHQP.2018.8378857.

[46] S. Sakar, S. R¨onnberg, M. Bollen, Interferences in AC-DC LED drivers exposed to
voltage disturbances in the frequency range 2-150 kHz, IEEE Trans. Power
Electron. 34 (11) (2019) 11171–11181, https://doi.org/10.1109/
TPEL.2019.2899176.

[47] S.K. R¨onnberg, A.G. Castro, A. Moreno-Munoz, M.H.J. Bollen, J. Garrido, Solar PV

inverter supraharmonics reduction with random PWM. Proceedings of the 11th
IEEE International Conference on Compatibility, Power Electronics and Power
Engineering (CPE-POWERENG), 2017, pp. 644–649, https://doi.org/10.1109/
CPE.2017.7915248.

[48] P. Davari, F. Blaabjerg, E. Hoene, F. Zare, Improving 9-150 kHz EMI performance
of single-phase PFC rectifier. Proceedings of the 10th International Conference on
Integrated Power Electronics System, 2018, pp. 1–6.

[49] M. Klatt, J. Meyer, P. Schegner, A. Koch, J. Myrzik, C. K¨orner, T. Darda, G. Eberl,
Emission levels above 2 kHz– laboratory results and survey measurements in public
low voltage grids. Proceedings of the 22nd International Conference on Electricity
Distribution (CIRED), 2013, pp. 1–4, https://doi.org/10.1049/cp.2013.1102.

ElectricPowerSystemsResearch195(2021)10717911