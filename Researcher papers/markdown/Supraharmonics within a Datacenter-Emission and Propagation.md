1
Supraharmonics within a Datacenter-Emission and
Propagation
Jil Sutaria,
Ángela Espín-Delgado, and
Sarah Rönnberg
Luleå University of Technology, Luleå, Sweden
jil.sutaria@ltu.se
switching techniques are commonly used in these converters.
Abstract—The reliability of the electrical and cooling systems The converters are one of the main source of supraharmonics
is of utmost importance for the uninterrupted operation of the (non-intentional emission) in data centers. The authors in [3]-
data center information technology (IT) load. The electrical [4] study the interferences due to supraharmonics which
distribution of the data center includes many subsystems starting include additional heating, audible noise, malfunction of
with the utility and building transformers, uninterruptible power equipment, and false tripping of residual current devices
supply (UPS), power distribution units (PDUs), and power
(RCD). The authors in [5] show the presence of low-frequency
supplies ultimately powering the fans and the internal
oscillation, called the beat frequency which results due
components of IT equipment. The various converters in data
asynchronous operation of converters. Beat frequency can
centers emit switching frequency residue due to PWM (pulse
width modulation) techniques. The switching frequency range cause the voltage regulators in the server power supplies to
falls within the supraharmonic range, i.e., 2 to 150 kHz. This mal-operate [6]. From the perspective of data center operators,
paper aims to show, with measurements, the different types of any malfunction of equipment can lead to downtime of servers
supraharmonic emissions measured in the data center, and the causing them economic loss [7].
difference between their maximum and average magnitudes. The
paper shows a method to identify the equipment emitting
The behavior of supraharmonics is quite different than
supraharmonic emission and possible disturbances caused by it.
harmonics, hence a distinction should be made between them
The paper traces the propagation of supraharmonic emission
[1]. The supraharmonics can be of distinct types, namely
from the source through the transformer to the grid. Lastly, a
narrow band, and broadband. They can vary in frequency and
comparison of measurements is made with the compatibility
levels given by standard IEC 61000-2-2. magnitude with time as studies by the authors in[8]. Depending
on the type of supraharmonic emission, its summation in the
Index Terms—Data center, Information technology, Power neutral conductor varies. This leads to an increase in the PE-N
quality, Power supplies, Pulse Width Modulation, (Protective earth to neutral) voltage. Work is on-going but still
Supraharmonics there is a lack of standardization when it comes to immunity
I. INTRODUCTION and compatibility levels for supraharmonics. The compatibility
levels for voltage characteristics are defined in EN50160 [9]
The use of converters, due to their flexibility in controlling
and IEC 61000-2-2-Amd 2 [10] for differential mode for
the power, has increased in recent years. These converters
narrowband (non-intentional) emission. Although some
are present in all types of electronic loads with variable
standards have now included them as informative annex, a
power ranges and are present in many devices found in our
thorough standardization on measurement and quantification is
homes and industrial facilities, e.g. PV inverters, servers, LED
required [11]. The industry such as data centers thus lacks the
lamps, and more. To increase the efficiency as well as to damp
knowledge to quantify and compare the supraharmonics within
the harmonics (<2 kHz), they are likely to be switched in the
their installation. Studies about supraharmonic propagation
range of 2 kHz to 150 kHz, which will be referred to as
show that they propagate locally within the installation to a
supraharmonics in this paper [1]. Industrial facilities such as
high degree. Information about how they would propagate
data centers house converters such as uninterruptible power
within a three-phase industrial installation is not well known.
supply (UPS), switched-mode power supply (SMPS), and
The impact of voltage unbalance, load unbalance and
converters used in voltage and frequency drives (VFD). The
conductor crosstalk for supraharmonics in three phases has
converters are often operated in series and parallel to cater to
been studied in [12] where controlled experiments formed the
the power demand as well as to increase the availability of
basis for the results. This paper intends to show the emission
power to the servers [2]. Pulse width modulation (PWM)
one can expect to find within a data center during normal
This study was supported by the Swedish Energy Agency under grant
43090-2, Cloudberry Datacenters.
978-1-6654-1639-9/22/$31.00 ©2022 IEEE.
1658089.2202.11035PQHCI/9011.01
:IOD
| EEEI
2202©
00.13$/22/9-9361-4566-1-879
|
)PQHCI(
rewoP
fo
ytilauQ
&
scinomraH
no
ecnerefnoC
lanoitanretnI
ht02
2202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore. Restrictions apply.

2
operation. The other objective is to show the propagation of of transformer secondary (LV), and the output panel of the
supraharmonics upstream towards the grid. Hypothesis about UPS rooms. The measuring device uses a sampling rate of
the cause and effect of supraharmonic emission found in the 1 MHz, a measurement interval of 10 cycles, and filters per
data center is made. Lastly, the emission will be compared with IEC 61000-4-30. The PQube3 gives the 1-minute average and
some of the existing standards. maximum values of voltages with 200 Hz grouping between 2
to 9 kHz (36 groups) and 2 kHz grouping from 2 to 150 kHz at
II. DESCRIPTION OF A DATA CENTER
the measured locations measured according to IEC 61000-4-
A. Power Electronics in a Data Center
30 Ed. 3. The UPS output is connected to a Δ/Y transformer
The power electronics in data centers are the core building which further distributes power to the single-phase server
blocks of the electrical supply system in a data center. A block loads. Due to the connection of the transformer to the output of
diagram of the different supply stages in a data center is shown the UPS, it is assumed that the supraharmonic emission
in Figure 1. The incoming AC power from the utility is measured at the UPS output panel has a higher contribution
conditioned using an uninterruptible power supply (UPS) that from the UPS as compared to the server load connected
provides a backup in case of power failure. The output of the downstream.
UPS is supplied to the input power supply unit (PSU) of the
III. SUPRAHARMONICS WITHIN THE DATA CENTER MEASURED
server [13], through the power distribution unit (PDU).
AT LV TERMINALS
Figure 2 shows the magnitude of supraharmonics measured at
phase L2 of the transformer terminals of thirteen LV feeders,
where the data from LV feeder 9 is not shown. The
measurements are performed for a period of 12 or 24 hours at
each LV feeder terminal. The 95th percentile values as
suggested by IEC 61000-4-30 of the average voltage (rms)
values calculated every one minute are presented in Figure 2.
The magnitudes are plotted as stacked plots, where the length
Figure 1. Block diagram representation of data center.
of the bar presents the magnitude, and the color represents the
The server PSU further distributes the power to various feeder number. The data center shows the presence of different
applications like server fan, communication, and memory frequency components chief among them in 2 to 9 kHz range
supply and point of load (PoL) converter supplying the are 4 kHz, 5 kHz, 5.5 kHz, and 6 kHz measured at the LV
microcontroller. Within the UPS, depending on the topology, terminals. The LV feeders supply different UPSs, cooling, and
the power undergoes conversions once or twice. The UPS is a lighting load, therefore, show a difference in the magnitude
combination of rectifier and inverter circuits. It also has a DC- and the frequency of emission. The feeders are also divided
DC converter for the integration of batteries into UPS, which into groups in terms of the MV source (11 kV) they are
takes care of charging and discharging them. The PSU has a supplied from. Thus, the change in the upstream and
power factor corrected (PFC) rectifier and a DC-DC converter downstream impedance due to the source and the load may be
circuit. A dual power supply server supply is fed by two PSUs, the cause for the change in the magnitude of emission. From
each of which is rated to take the full load and are supplied the frequency spectrum shown in Figure 2, the magnitude of
from separate phases. The aim is to have a backup PSU in case 4 kHz, 5 kHz, 5.5 kHz (5.4 kHz and 5.6 kHz), and 6 kHz are
one PSU fails. The load is shared by the PSUs during normal higher.
operation.
B. Description of Data Center where Measurements are made
Measurements from a data center rated 24 MVA are presented
in this paper. The data center is supplied by two 3-φ, 11 kV
sources on the medium voltage (MV) level. The MV supply is
further split into five MV feeders, three of them are supplied
by source 1 and the remaining two are connected to source 2.
The supply from 11 kV feeders is further stepped down to
Figure 2. 95th percentile values of the average voltage of supraharmonic groups
433 V through fourteen Δ/Y transformers creating fourteen
superimposed on phase L2 of different LV feeders within the data center for a
low voltage (LV) feeders. The UPSs, cooling, and lighting load
period of 12 to 24 hours shown as a stacked plot.
is further split between these LV feeders. The data center has
5 floors, where transformers are housed on the ground floor Figure 3(a) and (b) shows a cumulative value of supraharmonic
whereas UPS rooms are housed from floors 1 to 5. Every floor contributions (95th percentile values) from frequencies present
has four UPS rooms, namely R1, R2, R3, and R4. Each UPS at different LV terminals for phase L2 and phase L3
room has four UPSs operating in parallel. The LV feeders are respectively. The magnitude of supraharmonic emission in
spread to supply different UPS rooms and other loads. The phase L1 is approximately equal to that in phase L3 and hence
measurements were conducted by using a PQube3 meter at the is not shown here. It can be observed that although both the
input panel of the transformer primary (MV), the output panel
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     |     |     |     |     |     |     |     |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
phases show the presence of the same frequency components,  For broadband emission the magnitude remains constant with
the magnitude of emissions differs.  respect to time, but it is spread within a large frequency range.
An increase in the emission in broadband is observed at regular
intervals of seven hours. The reason for this is not known. A
|     |     |     |     |     |     | second  | broadband  | emission  | is  | observed  | between  |     | 120  to  |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | --------- | -------- | --- | -------- |
140 kHz, which may be the multiple harmonics of 60 to
|     |     |     |     |     |     | 70  kHz.  | The  | emissions  | in  the  | data  | center  | can  thus  | be  |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ---------- | -------- | ----- | ------- | ---------- | --- |
categorized as shown in TABLE I as defined in [8].
|     |       |         |     |         |      |     |     |     |     |     |     |     |     |
| --- | ----- | ------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | (a)   |         |     |         | (b)  |     |     |     |     |     |     |     |     |
Figure 3. 95th percentile values of the average voltage of supraharmonic groups
at different LV terminals for (a) phase L2 and (b) phase L3.
LV terminals 6, 7, 10, and 13 show the presence of 4 & 5 kHz
components in phase L2, but they are absent or negligible in
phase L3. The main emission at these terminals is 5.5 kHz,
leading to the conclusion that they are connected to loads that
| emit  5.5  | kHz.  The  | cumulative  |     | magnitude  | for  all  the  |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ----------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 5. Change in the maximum value of 1 minute aggregated voltage at LV
contributions on LV 6, is 7 V, which is considerable. Similarly,
11 for phase L2 for frequencies from 2 to 150 kHz, with 2 kHz grouping.
LV terminals 1 to 4 and 12, have 4 kHz and its multiple 8 kHz
as primary emission. The 6 kHz emission is present in LV
TABLE I. CATEGORISING SUPRAHARMONIC EMISSIONS WITHIN
terminals 5, 8, and 11 but also present in LV terminals with a  THE DATA CENTER
| switching  | frequency  | of  5.5  | kHz.  | This  | shows  that  the  |     |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | ----- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
downstream impedance i.e., the load connected to each phase  Type   Description   Frequency
also differs. Although the connected loads between the three  Type A  Narrow  band.  Constant  4 kHz, 5 kHz
|     |     |     |     |     |     |     | frequency and magnitude  |     |     | And their multiples  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | -------------------- | --- | --- | --- |
phases are balanced, some unbalance exist during the operation
|     |     |     |     |     |     | Type A1  | Narrow  | band.  | Constant  | 5.4 kHz, 5.6 kHz, 6 kHz  |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | --------- | ------------------------ | --- | --- | --- |
of  servers.  Further  investigations  are  made  to  study  the  frequency  and  variable  And their multiples
emissions at the UPS output terminals to identify the causes for  magnitude w.r.t time
|                |     |                   |     |             |              | Type B  | Broadband emission  |     |     | 60-70 kHz, 120-140 kHz  |     |     |     |
| -------------- | --- | ----------------- | --- | ----------- | ------------ | ------- | ------------------- | --- | --- | ----------------------- | --- | --- | --- |
| the  presence  | of  | these  frequency  |     | components  | at  the  LV  |         |                     |     |     |                         |     |     |     |
terminals.
Emission type A will show less difference in the average and
A.  Categorizing Supraharmonic Emissions within the Data
maximum value per minute, whereas the emission with type
Center
|            |        |               |        |                |            | A1  will  | show  | more  difference  |     | between  | the  | average  | and  |
| ---------- | ------ | ------------- | ------ | -------------- | ---------- | --------- | ----- | ----------------- | --- | -------- | ---- | -------- | ---- |
| Figure  4  | shows  | the  average  | value  | of  different  | types  of  |           |       |                   |     |          |      |          |      |
maximum magnitudes. It should be noted that although the
supraharmonic emissions observed in the data center with the
magnitude is variable for type A1, it varies within a maximum
change in time. Figure 4(a) shows supraharmonics with 200 Hz  and minimum value range and does not become zero at any
grouping, where 5 kHz, shows the average voltage grouped  instant. The magnitude of the emission for the same frequency
between 5 kHz and 5.2 kHz, and 6 kHz is grouped between
|     |     |     |     |     |     | differs  | for  LV  | feeders  | 5  and  | 11.  The  | sine  | pulse  | width  |
| --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ------- | --------- | ----- | ------ | ------ |
6 kHz and 6.2 kHz measured every minute at phase L2 of LV  modulation (SPWM) and space vector pulse width modulation
5 and LV 11 for one day. The measurements on LV 5 and LV  (SVPWM) are common PWM techniques that cause emission
11 are done on the same day and both show the presence of
showing characteristics like type A. The authors hypothesize
5 kHz and 6 kHz emission. As seen from Figure 4(a) observed  that a converter controlled to generate constant output power
supraharmonic  emission  are  of  different  types,  namely,  will generate emission of type A1. PWM employing hysteresis
constant frequency and magnitude, constant frequency but
|     |     |     |     |     |     | control  | is  one  | of  the  PWM  | techniques  |     | that  | can  generate  |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | ----------- | --- | ----- | -------------- | --- |
variable magnitude with respect to time. Figure 4(b) and Figure
|     |     |     |     |     |     | emission  | of  type  | B.  Figure  | 5  shows  |     | the  variation  |     | in  the  |
| --- | --- | --- | --- | --- | --- | --------- | --------- | ----------- | --------- | --- | --------------- | --- | -------- |
5 shows a broadband emission between 60 and 72 kHz, with  magnitude of supraharmonics from 2 to 150 kHz of phase 2 at
2 kHz grouping measured at phase 2 of LV 11.  LV  11.    From  Figure  4(b)  and  Figure  5,  comparing  the
magnitude of broadband emission between 60 and 70 kHz, the
maximum values are higher than average voltage value every
minute. As seen from Figure 3(a) a frequency of 4 kHz is also
present on LV 11. The multiples of 4 kHz e.g., 16 kHz, 20 kHz
are seen superimposed in Figure 5. The 4 kHz component is
|     |     |     |     |     |     | likely  due  | to  | PWM  switching  |     | of  equipment  |     | connected  |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | -------------- | --- | ---------- | --- |
|     |     |     |     |     |     |              |     |                 |     |                |     |            |     |
downstream of the transformer.
|     | (a)   |         |     |         | (b)  |     |     |     |     |     |     |     |     |
| --- | ----- | ------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
B.  Difference between the Maximum and Average Values
Figure 4. Change in supraharmonics emission with respect to time (a) 5 kHz
(Type A) and 6 kHz (Type A1) respectively measured at LV 5 & 11 for phase  Figure 6 shows the 95th percentile values of the maximum
L2 (b) Type B emission between 60 to 72 kHz measured at LV 11 for phase
L2.     value measured at the transformer terminals on phase L2 for
the LV feeders. Comparing Figure 2 and Figure 6, it can be

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore.  Restrictions apply.

4
said that the maximum value of the voltage can be 1.5 to 3 impedance seen by 8 kHz is low, thus its magnitude is higher
times the average values per supraharmonic group. The highest than 4 kHz. The groups around 4 kHz and 8 kHz also have a
magnitude among different frequency groups is for 5.4 kHz higher magnitude due to the sidebands caused by PWM
and 5.6 kHz. Figure 7(a) and (b) shows the magnitude of techniques. Figure 8(b) shows the emissions on the 3rd floor,
average and maximum voltage values measured at phase L1, measurements are available only for three UPS rooms.
LV 6 for 5.4 kHz and 5.6 kHz respectively. The difference
between the average and maximum values per minute varies
between 5 % to 231 % w.r.t the average value. The maximum
voltage value has a cyclic pattern where it varies between high
and low magnitude every 15 minutes approximately. The
authors hypothesize two reasons for this behaviour, one is that
the supraharmonics depend on the current drawn from the
device emitting them. The other is there is asynchronistic
behaviour (in terms of frequency) between the multiple devices (a) (b)
emitting them, causing a low-frequency oscillation
superimposed on the supraharmonics emitted by them. In this
case, the low-frequency oscillation, a so-called beat frequency,
is approximately 0.06 Hz. However, further measurements are
needed to confirm it.
(c)
Figure 8. Stacked plot of maximum voltage emission per minute measured at
phase L1 for the UPS rooms R1, R2, R3, and R4 located on (a) 2nd, (b) 3rd, and
(c) 4th floor of the data center measured at the output panel of respective UPS
rooms.
It can be seen that the UPSs for room R1 are of a different type.
Figure 6. 95th percentile values of the maximum voltage of supraharmonics The emission from this UPS is at 6 kHz. When the emission
groups superimposed on phase L2 of different LV feeders within the data
was examined w.r.t time it was found to be of type A1. Figure
center for a period of 12 to 24 hours.
8(c) shows the emissions on the 4th floor, here also two rooms
R2 and R4 house UPS with 6 kHz as the main emission
whereas R1 and R3 have a switching of 5.5 kHz. All the UPSs
on the 5th floor have 5.5 kHz as the switching frequency. The
frequencies 4 kHz, 5.5 kHz, 6 kHz were observed on the LV
terminals. It can be concluded that the most likely sources of
these frequencies were the PWM switching used in the UPS.
D. Correlation Plots
To ascertain whether, for a given LV terminal, the three phases
(a) (b) are supplying three-phase loads and single-phase loads a
Figure 7. Difference between the maximum and average values for 5.4 and 5.6 correlation of supraharmonic groups is used. The one-minute
kHz measured at LV 6 phase L1.
average values at LV terminal for one day and one phase
results in a matrice of 1440×36. Correlation is calculated
C. Measurements at UPS Output Terminals
between supraharmonic matrices of phase L1 and L2, L2 and
Figure 8 shows the 1-minute aggregated value of maximum
L3. Pearson’s linear correlation coefficient is used to quantify
voltage measured at phase L1 for the UPS rooms located on
the correlation in this study. The correlation matrix is used to
the 2nd, 3rd and 4th floor of the data center measured at the
investigate the correlation between different supraharmonic
output panel of respective UPS rooms. The emissions on the
groups for the two phases. A high correlation coefficient
1st floor matched that on the 2nd floor, and the emissions on the
between two supraharmonic groups for the same frequency,
5th floor are similar to those on the 4th floor and are not shown
suggests that the source connected to both the phases is the
here. Similar emissions were found to be present on phase L2
same and is emitting in synchronism. A low correlation on the
and L3 albeit with different magnitudes. The output of UPS is
other hand can be interpreted as originating from different
connected to Δ/Y transformers, the secondary of which
sources. Figure 9(a) and (b) show the correlation between
connects to the server loads. Thus, it is assumed that the UPS
supraharmonic matrices of phase L1 and L2, L2 and L3 for LV
emission is the main emission seen at the UPS output terminal.
11. The LV feeder 11 has three primary frequency emissions
Figure 8(a) shows that the sixteen UPS connected on the 2nd
i.e., at 4 kHz, 5 kHz, and 6 kHz. A correlation factor +1
floor, are of the same type and emit 4 kHz as the main
indicates the highest positive correlation and a correlation
frequency, with 8 kHz as the multiple harmonic. The
factor of -1 indicates the highest negative correlation.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore. Restrictions apply.

5
95 percentile among the components presented in Figure 10 is
close to 0.8 V, this would be superimposed on the fundamental
component and add to in the overall magnitude of the PE-N
voltage. The PE conductor being common between all the
terminals can spread of supraharmonic frequency between LV
terminals. All the emissions seen at the PE terminal can be seen
at the PE-N voltage at that terminal.
IV. PROPAGATION OF SUPRAHARMONICS TO MV TERMINALS
(a) (b)
Figure 9. Correlation between supraharmonic group matrices of (a)phase L1 The supraharmonic emission seen at the output terminals of the
and L2, (b) L1 and L3 for LV 11 for emission for one day. UPS can also be seen at the LV terminals. Thus, it can be said
that the supraharmonics propagate upstream. Measurements
It can be seen from Figure 9(a) and (b) that 6 kHz has a
are made at the supply panel of the five MV terminals
correlation coefficient of 0.94 and 0.98 respectively suggesting
supplying the transformers within the data center. The
that it is emitted by one specific load supplied by LV 11. The
measurements are made using potential transformers (PT) that
multiple of 4 kHz, i.e, 8 kHz also shows a high correlation
step down the voltage on the MV side i.e., 11 kV to110 V. The
factor. The 4 kHz emission has a negative correlation factor of
PTs are old and the bandwidth of the measurement in the high-
-0.2 and -0.3 for both cases, which indicates that there is no
frequency range is unknown. So, the magnitude of the
correlation. The 4 kHz could be a result of conducted emission
frequency components cannot be trusted upon. However, the
propagating from other parallel terminals connected to the
presence of supraharmonic frequencies at the MV level can
same transformer. The correlation factor for 5 kHz frequency
still be seen with measurements. Figure 11 shows the presence
is 0.63 and 0.67 for Figure 9(a) and (b) respectively. The 5 kHz
of the frequency components at different MV terminals.
emission is not caused by UPS (c.f. Figure 8). Since there is a
positive correlation it may be caused by a single-phase device
connected in either of the phases or it may be a result of
conductor crosstalk where a single-phase device is connected
to any phase.
E. PE-N Voltage at different LV Terminals
The 1-minute aggregated value of PE-N voltage was measured
at different LV terminals with 2 kHz grouping. Figure 10 Figure 11. 95th percentile values of the maximum voltage of supraharmonics
exemplarily shows the 95 percentile values of PE-N voltage groups superimposed on phase L2 of different MV feeders within the data
measured at LV terminals 2, 7, and 13 for 24 hours. center for 24 hours.
The frequency emissions at 4 kHz, 5.4 kHz, 5.6 kHz, and 6 kHz
seen at the UPS output terminals, which propagate to LV
terminals are seen to propagate upstream towards MV
terminals through the transformer. The other components that
are higher in magnitude are 2 kHz and 2.2 kHz. These
components could be an extension of the harmonic emission.
The magnitude could be the combined contribution of
harmonics propagating from upstream to the MV terminals and
Figure 10. PE-N voltage measured at the LV terminals 2, 7 and 13 measured harmonics injected by the data center. The broadband
for 24 hours.
emissions from 60 to 70 kHz and 120 to 140 kHz (not shown
here) can also be seen at the MV terminals. This emission is
The terminals are chosen such that they include 4 kHz, 5.4,
seen to be present on other phases as well as other MV
5.6 kHz which are the common emissions superimposed on the
terminals.
voltage at different LV terminals. It can be seen from Figure
10 that all the terminals have two common broadband emission V. COMPARING THE EMISSION WITH THE COMPATIBILITY
from 60 to 70 kHz and it's multiple at 120 to 140 kHz. LV 2 LIMITS STATED IN IEC 61000-2-2
shows the integer multiples of 4 kHz in decreasing magnitude
There is a gap in the compatibility and immunity standard for
after 8 kHz. It also has a broadband component of 82 to 98 kHz
supraharmonics emission (non-intentional) at low voltage
not seen in the other feeders. LV 7 and 13 have the main
levels for different types of supraharmonic emissions.
emission at 5.4 and 5.6 kHz. The multiples of these frequencies
However, several standards cover this frequency range
are present on both terminals, but the magnitude of the
pertaining to intentional emission due to power line
individual component differs. While LV 7 has the highest
communication (PLC). The compatibility limits for voltage
amplitude at 32 kHz, LV 7 has it at 10 and 12 kHz. A common
characteristics are defined in EN50160 and IEC 61000-2-2 for
phenomenon noted at all the terminals is that in the PE-N
differential mode for narrowband (non-intentional) emission.
voltage the multiples of the switching frequency emission have
The voltage characteristics according to EN 50160 is 2% of the
a higher magnitude than the switching frequency. The highest
nominal voltage for a frequency range of 2-9 kHz. IEC 61000-
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore. Restrictions apply.

6
2-2-Amd 1 defines a curve with the emission level at 2 kHz 61000-2-2 Amd 2, and it was found that the emissions are
equal to 1.4 % of the nominal frequency and the level decreases within the limits barring at 5.4 and 5.6 kHz for LV 6. The
linearly from 1.4% to 0.65% with the logarithm of the authors recommend including supraharmonics in “normal”
frequency in the range 3 to 9 kHz. The measurements should power quality analysis. Another recommendation is to do
be done with a bandwidth of 200 Hz. The measurements from simultaneous measurements at several locations within an
PQube3 for the frequency range of 2 to 9 kHz are with 200 Hz installation. Lastly limits and clear guidelines to where inside
bands, thus a comparison of the emissions within the an installation the said limits apply e.g., point of delivery
datacenter is made with the compatibility limits stated in IEC terminal of a device and for what time-range e.g., weekly as
61000-2-2. For long-term measurements, the standard suggests for harmonics should be clearly defined.
using 10-minute aggregated values. Thus the 1-minute average
values (measured according to IEC 61000-4-30) are
ACKNOWLEDGEMENTS
aggregated in time over 10-minute windows and averaged The authors of this paper would like to thank Efficienergi
according to IEC 61000-4-7 [14]. The 95th percentile value of Consulting Pvt. Ltd for sharing the valuable data and views
the 10-minute average values are used for comparison with about the paper. We are grateful to Rajen Mehta and Smita
limits stated in IEC 61000-2-2. A nominal voltage of 230 V is Vichare for their help with collating the data and system
used as a reference voltage. Figure 12 shows a comparison of overview.
the compatibility level stated in IEC 61000-2-2 with the
emissions at the LV terminals for phases L1, L2, and L3. REFERENCES
[1] S. K. Rönnberg et al., “On waveform distortion in the frequency range
of 2 kHz–150 kHz—Review and research challenges,” Electr. Power
Syst. Res., vol. 150, pp. 1–10, 2017.
[2] P. T. Krein, “Data center challenges and their power electronics,” CPSS
Trans. Power Electron. Appl., vol. 2, no. 1, pp. 39–46, 2017.
[3] J. Meyer et al., “Overview and classification of interferences in the
frequency range 2-150 kHz (supraharmonics),” SPEEDAM 2018 - Proc.
Int. Symp. Power Electron. Electr. Drives, Autom. Motion, pp. 165–170,
2018, doi: 10.1109/SPEEDAM.2018.8445344.
[4] Á. Espín-Delgado, S. Rönnberg, S. Sudha Letha, and M. Bollen,
“Diagnosis of supraharmonics-related problems based on the effects on
electrical equipment,” Electr. Power Syst. Res., vol. 195, no. Oct. 2020,
Figure 12. Comparison of compatibility level stated in IEC 61000-2-2 with doi: 10.1016/j.epsr.2021.107179.
the emissions at the LV terminals for phase L1, L2, and L3. [5] X. Yue, D. Boroyevich, F. C. Lee, F. Chen, R. Burgos, and F. Zhuo,
“Beat frequency oscillation analysis for power electronic converters in
The compatibility level stated by IEC 61000-2-2 is shown by DC nanogrid based on crossed frequency output impedance matrix
the solid line. It can be seen that the emission from 2 to 9 kHz model,” IEEE Trans. Power Electron., vol. 33, no. 4, pp. 3052-3064,
April 2018, doi: 10.1109/TPEL.2017.2710101.
is within limits for phases L1 and L3. The 5.4 and 5.6 kHz
[6] K. Lee and H. Zou, “Analysis of the beat frequency oscillation in voltage
emission at LV 6 is above the limits. The maximum value per
regulators,” IEEE Energy Convers. Congr. Expo. ECCE 2009, pp. 3026–
minute for the emissions was found to exceed the limits. 3030, 2009.
However, the measurement methods stated in IEC 61000-4-30 [7] M. Wiboonrat, “Risk anatomy of data center power distribution
systems,” IEEE Int. Conf. Sustain. Energy Technol. ICSET 2008-Proc.,
Ed-3 used by PQube3 for 2 to 9 kHz are informative. The
pp. 674–679, Nov. 2008, doi: 10.1109/ICSET.2008.4747092.
comparison shown in Figure 12 should therefore be treated as
[8] J. Sutaria, Á. Espín-Delgado, and S. Rönnberg, “Summation of
advisory rather than a judgement on the magnitudes at different supraharmonics in neutral for three-phase four-wire system,” IEEE Open
LV terminals. Further work in the measurement and J. Ind. Appl., vol. 1, no. June, pp. 148–156, 2020.
[9] Voltage characteristics of electricity supplied by public distribution
quantification of supraharmonics is needed for a standardized
systems, EN 50160,2005.
comparison.
[10] Environment – Compatibility levels for low- frequency conducted
disturbances and signalling in public low-voltage power supply: Amd 2,
VI. CONCLUSION
IEC 61000-2-2, vol. 2004, pp. 1–13, 2016.
The operation of multiple converters in the data center leads to [11] V. Khokhlov, J. Meyer, A. Grevener, T. Busatto, and S. Ronnberg,
the presence of different types of supraharmonics. The “Comparison of measurement methods for the frequency range 2-150
kHz (Supraharmonics) based on the present standards framework,” IEEE
magnitude of supraharmonics depends on the emitting source
Access, vol. 8, pp. 77618–77630, 2020.
and the impedance of the load connected downstream or [12] J. Sutaria, S. Rönnberg, and Á. Espín-Delgado, “Analysis of
upstream and varies between phases. The supraharmonics supraharmonics in a three-phase frame,” Electr. Power Syst. Res., Vol.
emitted by UPS were shown to propagate upstream to the MV 203, pp 1-10, 2022.
[13] P. T. Krein, “A discussion of data center power challenges across the
grid. It was hypothesized from the time variation of the
system,” Int. Conf. Energy Aware Comput. ICEAC 2010, pp. 9–11, 2010.
switching frequency that the operation of multiple UPSs in [14] Testing and measurement techniques - General guide on harmonics and
parallel at terminal LV 6 caused beat frequency oscillation. interharmonics measurements and instrumentation, for power supply
The emission from a single-phase device shows correlation systems and equipment connected thereto, IEC Standard 61000-4-7,
2002.
which may point to conductor crosstalk at these frequencies.
The presence of supraharmonic emission leads to an increase
in the PE-N voltage throughout the data center. Lastly, the
emissions were compared to the compatibility limits in IEC
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:01:43 UTC from IEEE Xplore. Restrictions apply.