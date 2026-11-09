MIPRO 2022, May 23 - 27, 2022, Opatija, Croatia
Analysis of current harmonics in data center
power system
K. Raič Raguž*, M. Miletić*, V. Zeleničić *, D. Sumina *, I. Erceg * and Ž. Nastasić*
*Faculty of Electrical Engineering and Computing/Department of Electric Machines, Drives and Automation, Zagreb,
Croatia
**Databox d.o.o., Zagreb, Croatia
katica.raic-raguz@fer.hr,marinko.miletic@fer.hr,vinko.zelenicic@fer.hr,damir.sumina@fer.hr,igor.erceg@fer.hr,
zeljko.nastasic@databox.hr
Abstract
- This paper presents power quality analysis  values. An isolation transformer for harmonic separation
|              |                          |     |     |                          |     | and  series  | passive  | filters  | for  harmonic  | reduction  | were  |
| ------------ | ------------------------ | --- | --- | ------------------------ | --- | ------------ | -------- | -------- | -------------- | ---------- | ----- |
| at different | points in a data center. |     |     | Electrical distribution  |     |              |          |          |                |            |       |
recommended. In another data center, the power quality of
| network | schemeand data center description |     |     |     | are also given. |                |     |                     |         |        |         |
| ------- | --------------------------------- | --- | --- | --- | --------------- | -------------- | --- | ------------------- | ------- | ------ | ------- |
|         |                                   |     |     |     |                 | IT  equipment  |     | with  and  without  | Active  | Power  | Factor  |
The method of measurements performed is briefly described
|     |     |     |     |     |     | Control  | (APFC)  | is  analysed | [3].  | A reactive  | power  |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ------------ | ----- | ----------- | ------ |
and the results of real measurements of current and voltage
Total  Harmonic  Distortion  (THD)  are  presented  and  compensator  was  indicated  to  achieve  reactive  power
compared with IEEE 519-2014 recommended practice and  compensation and reduce the predominant harmonic level.
requirements for harmonic control in electric power system.  The cooling system is another type of nonlinear load [4].
All  measured values  comply  with  the  standard but  A passive harmonic filter designed specifically for the low
measurements at downstream levels closer to the nonlinear DC bus capacitance of Electronically commutated (EC)
loads have largerTHD.
|     |     |     |     |     |     | fans  can  | reduce  | the  cooling  | system | negative  | effects.  |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | ------ | --------- | --------- |
Factory testing confirmed the accuracy of the computer
| Keywords | - data center; |     | power quality; | current harmonic  |     |             |     |                                        |     |     |     |
| -------- | -------------- | --- | -------------- | ----------------- | --- | ----------- | --- | -------------------------------------- | --- | --- | --- |
|          |                |     |                |                   |     | simulations | and | the IEEE Std 519 recommendations have  |     |     |     |
distortion;nonlinear loads
been met. In addition to passive filters, Active Harmonic
Filters (AHFs) and hybrid filters are also used to reduce
I. INTRODUCTION distortions [5].  AHF’s  with  harmonic  cancelation
With  the  development  of  digital  technology,  data  transformers  proved  to  be  very  efficient  in  reducing
centers are becoming increasingly important. Most of the  harmonics in data center. It was confirmed in 2007 in a
medium legacy data center where the THD was increased
world’s Internet Protocol (IP) traffic goes through data
by nonlinear loads outside the center.
centers. For every bit of data that travels the network,
another five bits of data are transmitted within and among
Variable frequency drives are used in data centers to
| data centers. Greater connectivity is propelling |     |     |     |     | demand  |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
improve the efficiency of cooling and ventilation systems
| for  data  | center  | services  | and  | energy  | consumption  |                                                 |     |     |     |     |         |
| ---------- | ------- | --------- | ---- | ------- | ------------ | ----------------------------------------------- | --- | --- | --- | --- | ------- |
|            |         |           |      |         |              | [6]. But these drives also cause harmonics. THD |     |     |     |     | can be  |
(primarily electricity). In the last decade, global Internet
reduced with active and passive filters. An active filter is
traffic has increased 15-fold, and only in 2020 it increased  an effective way to eliminate both harmonics and reactive
by more than 40%, mainly because of social networking  currents from the AC source, and it can be applied to the
and video streaming growth. Globally, data transmission
entire power system. For passive filters in combination
networks consumed 260-340 TWh in 2020, equivalent to
|           |             |     |              |             |             | with harmonic cancelation |                                              |     | transformers, special attention  |     |     |
| --------- | ----------- | --- | ------------ | ----------- | ----------- | ------------------------- | -------------------------------------------- | --- | -------------------------------- | --- | --- |
| 1.1-1.4%  | of  global  |     | electricity  | consumption | [1].  Data  |                           |                                              |     |                                  |     |     |
|           |             |     |              |             |             | should be                 | paid to load balancing. Hybrid Power Filter  |     |                                  |     |     |
transmission  network  technologies  are  also  becoming  (HPF) is a combination of Active Power Filter (APF) and
more  efficient.  Total  Harmonic  Distortion  (THD)  is  Passive  Power  Filter  (PPF), which  is  mainly  used  to
closely related to efficiency and power quality. Harmonics
reduce 3rd and 5th harmonic and improve power quality
come in twobasic varieties: currentdistortion and voltage
|     |     |     |     |     |     | [7]. 3rd harmonic caused |     |     | heating of neutral conductors  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------------ | --- | --- |
distortion. Nonlinear loads in data centers, servers, and IT
and transformers in a data center. HPF reduces current in
| equipment,  | are  | the  | most  common  | source  | of  current |     |     |     |     |     |     |
| ----------- | ---- | ---- | ------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
neutral and is preferable in terms of low cost, flexibility,
distortion and additional losses in the data center power  reliability and maintenance.
system. In this paper, special attention has been paid to
current distortion. Data center power quality analysis is presented in the
paper. It has been shown that the THD value is lower than
Data center power quality is a widespread concern.
the recommended values at all levels of the system, but
The  power  quality  of  Libyan  Telecom  Technology  significantly higher at downstreamlevels than at upstream
headquarter data center is analysed [2]. The total current  levels.  Upper  THD  limits  are  recommended  in  the
and voltage harmonic distortions were measured at points
literature [5], [8]. The paper is divided into five sections.
with different loads and compared with the recommended
|     |     |     |     |     |     | Section I consists of an introduction and related |            |                      |               |     | work. In  |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | ---------- | -------------------- | ------------- | --- | --------- |
|     |     |     |     |     |     | Section                                           | II,  part  | of  the  electrical  | distribution  |     | network   |
This work has been fully supported by the European Regional
scheme is presented. Section III presents the analysis of
Development Fund under the project “Development of a system for
optimizing power consumption in data centers”(KK.01.2.1.02.0082).
153
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:05:47 UTC from IEEE Xplore.  Restrictions apply.

power quality at an upstream level of the system. The
Reference measurements were made within one week
Uninterruptible Power Supply (UPS) room power quality  using a 10-minute average. Measurements were made
analysis  is  given  in  the  Section  IV,  while  Section  V  using a Chauvin Arnoux C.A 8336 network analyzer.
contains the power quality analysis at the downstream Given  the  typical  consumption,  measurements were
level of the system. Future work and conclusion are given
repeated at the time of peak consumption to obtain a
in Section VI.
picture of harmonic distortion. Repeated measurements
were made at two-minute intervals using Dewesoft XHS
II.
DATA CENTER DESCRIPTION (HIGH-SPEED DATA ACQUISITION SYSTEM) and a
sampling frequency of 20kHz.
| Figure 1 | shows one of two equally independent data  |     |     |     |     |     |     |
| -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
center branches, branch “A”. This provides redundancy in
powering the entire system. Each branch has its own
|     |     |     |     | III. | DISTRIBUTION ROOM(HIGHESTLEVEL) |     |     |
| --- | --- | --- | --- | ---- | ------------------------------- | --- | --- |
auxiliary generator to provide power to the system in the
MEASUREMENTS
event of a power failure. The branches have three UPSs,
two of which are currently in operation. UPSs power  A. Measurement pointP1
both, the IT equipment and the air conditioning units to
|           |                   |         |                 | The load is about 20% of the transformer |     |                              | power. The  |
| --------- | ----------------- | ------- | --------------- | ---------------------------------------- | --- | ---------------------------- | ----------- |
| maintain  | the  temperature  | in  the | UPS  room.  The |                                          |     |                              |             |
|           |                   |         |                 | difference in the load of each           |     | phase is only a few percent  |             |
measurement points are also marked in the figure. The
and has no technical significance. Asymmetry of the load
measurementsare divided into levels, where "distribution
isinevitable due toa certain numberof single-phase loads.
room" is the highestlevel and "server room" is the lowest In terms of total installed power, the largest part consists
level  of  the system. P1  point  presents  the  Point  of  of three-phase balanced loads (UPS and air conditioners).
Common Coupling (PCC).
|     |     |     |     | The  current  | THD is  | 4.2-4.5% (TABLE | 1). The  most  |
| --- | --- | --- | --- | ------------- | ------- | --------------- | -------------- |
pronounced current harmonicis H5(Figure 2); stepwiseit
BRANCH  A BRANCH  B ranges from 1.5% to 2.8%. It is followed by H13 (2%),
H11 (about 1.5%) and all others are less than 1% (except
|     | A - MAIN |     | B - MAIN |     |     |     |     |
| --- | -------- | --- | -------- | --- | --- | --- | --- |
TRANSFORMER TRANSFORMER H7 in phase 2).The most pronounced voltageharmonicis
G
|     | A - BACKUP | ∿   | B - BACKUP |     |     |     |     |
| --- | ---------- | --- | ---------- | --- | --- | --- | --- |
H7with values of 1.5-1.8%. All other harmonic values are
|     | GENERATOR |     | GENERATOR |             |            |                        |              |
| --- | --------- | --- | --------- | ----------- | ---------- | ---------------------- | ------------ |
|     |           |     |           | less  than  | 0.3%. The  | current  and  voltage  | THD  values  |
DISTRIB.
|     |     |     |        | measured   | at the Point of Common Coupling (PCC) are in  |                      |               |
| --- | --- | --- | ------ | ---------- | --------------------------------------------- | -------------------- | ------------- |
|     | Q1  |     | ROOM B |            |                                               |                      |               |
|     | P1  |     |        | accordance | with  the                                     | IEEE  std.  519-2014 | for  General  |
ATS1 DISTRIBUTION  ROOM ATS1 Distribution  Systems  up  to  69kV. The  network  short
|     |     | A   |     | circuit poweris muchhigher than the power consumption  |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
and therefore the power quality cannot be affected.
| Q2  | Q3 Q4 Q5 |     | Q5 Q4 |     |     |     |     |
| --- | -------- | --- | ----- | --- | --- | --- | --- |
P2
B. Measurement pointP2
| -NEPMOC NOITAS | ATS2   |            |     |                           |                                                 |                     |                     |
| -------------- | ------ | ---------- | --- | ------------------------- | ----------------------------------------------- | ------------------- | ------------------- |
|                |        |            |     | Switch                    | Q4 supplies the bus to which all cooling units  |                     |                     |
|                |        |            |     | are connected. Therefore, |                                                 | the distribution of | harmonics is        |
|                | Q12 Q8 | Q11 Q6 Q10 |     |                           | “P1”, but H3 in phase                           |                     |                     |
|                |        |            |     | the same asin             |                                                 | 2                   | is slightly smaller |
P3
Zone Zone (Figure 3).There is also a frequency component of 6 kHz
|     | ytilicaF | air conditioners | air conditioners |             |     |     |     |
| --- | -------- | ---------------- | ---------------- | ----------- | --- | --- | --- |
|     | CHILLER  |                  |                  | (Figure 5). |     |     |     |
P4
C. Measurement pointP3
|     |     | UPS  ROOM | UPS  ROOM |     |     |     |     |
| --- | --- | --------- | --------- | --- | --- | --- | --- |
Q50
|     |     | A   | B   | The loadat this circuitis an air conditionerfor a zone.  |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
Q51 Q54 Q55 Q52 Fromthe measured data (power, current, THD), it appears
UPS air cond.
that it is a combination of three-phase balanced load and
|     | UPS UPS UPS | A.C. 1 |     |     |     |     |     |
| --- | ----------- | ------ | --- | --- | --- | --- | --- |
single-phase load in phase2. The influence of this load is
|     | 1 2 3       | A.C. 2 |     |                                  |           |                                 |     |
| --- | ----------- | ------ | --- | -------------------------------- | --------- | ------------------------------- | --- |
|     |             |        |     | most evident at                  | H3 and H9 | (Figure 4). In phases 1 and 3,  |     |
|     |             |        |     | the magnitudes of the individual |           | harmonics are the same.         |     |
|     | Q58 Q59 Q56 |        |     |                                  |           |                                 |     |
The increased component of the 3rd harmonic in phase 2
Q63 Q65 Q66 Q60 Q61 Q62 Q64 can be seen in the current waveform. There is also a 6 kHz
Zone air cond.
P6 P5 component in the current generated by chopper assemblies
A.C. A.C.
|     |     |     |     | inside  | the  air  conditioner | (Figure  | 6). Voltage  total  |
| --- | --- | --- | --- | ------- | --------------------- | -------- | ------------------- |
SERVER  ROOM  1 harmonic distortion (THDv) values for all three points at
SDB P7 P8 this levelfor phases 1, 2and 3 are 1,5%, 1,7%and 1,6%.
|     |     | 2                   | Zone  A |                        |     |     |     |
| --- | --- | ------------------- | ------- | ---------------------- | --- | --- | --- |
|     |     | SDB Zone  B,  C,  D |         | D. Measurement pointP4 |     |     |     |
4
The UPSbusis powered by aswitchQ50. The load is
|     |     | SDB | Zone  E |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
6 balanced, practically fully resistive (the current lags the
|     |     | SDB |     | voltage by only 0.6°), and the current THD is 3.5-4.2% |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
8 Zone  F,  G,  H
(TABLE2). During the measurement, this loadaccounted
SERVER  ROOM  2 for 70-80% of the total transformer load. Proportion of
Figure 1.Branch “A”-electrical distribution network
154
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:05:47 UTC from IEEE Xplore.  Restrictions apply.

balanced load with low harmonic level has an extremely
favorable effect on the qualityof power supply from DC!
Looking at the harmonics, H7 is the largest (over 3%),
H13 is around 2%, H5 andH11 arebetween 1% and 2%,
while the rest are well below 1%(Figure 7).
Figure 6.Current waveformfor P3
Figure 2.Harmonic orderfor P1
Figure 7.Harmonic order for P4
TABLE1.Distribution roommeasured values
S P Q THDi[%]
P
[kVA] [kW] [kVAr] L1 L2 L3
1 189 188,4 11,3 4,4 4,2 4,5
Figure 3.Harmonic orderfor P2 2 40,2 38,9 10,2 19,8 20,8 20,1
3 28 25,6 11,2 24 24,5 23,5
4 136,3 136,2 1,5 3,98 4,2 3,52
IV. UPS ROOM (MIDDLELEVEL)MEASUREMENTS
A. Measurement pointP5
By the Q60 switch, the UPS output voltage is
transmitted to the zone busbar SDB4 in the server room.
All loads connected to SDB4 are single phase (power
supplies for servers and IT equipment), but the
distribution by phase is such that the phase loads differ by
less than 10% (Figure 8). The current distortion is 8.6-
9.5%. H3 and H11 are dominant in the spectrum (Figure
Figgure 4.Harmonic orderfor P3
9).
B. Measurement pointP6
Switch Q63 supplies the circuit from UPS to the
SDB8 (zones F, G and H). The loads (servers power
supplies) connected to SDB8 are newer generations with
lower current THD. The load of phase 3 is the highest,
and the loads of phases 1 and 2 are about half the valueof
the phase 3 load (Figure. 10), so the THD for phase 3 is
the lowest at 4.9%, while it is 10% and 7% for phases 1
and 2 (Figure 11). These values are better than those
Figure 5.CurrentwaveformforP2 obtained by measurement at the previous point. Voltage
155
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:05:47 UTC from IEEE Xplore. Restrictions apply.

TABLE2.UPSroommeasured values
| total  harmonic                                         | distortion (THDv) | values for  | all  three |     |       |     |      |        |     |         |     |
| ------------------------------------------------------- | ----------------- | ----------- | ---------- | --- | ----- | --- | ---- | ------ | --- | ------- | --- |
|                                                         |                   |             |            |     | S     |     | P    | Q      |     | THDi[%] |     |
| points at this levelfor phases1,2and 3 are 1,78%, 1,74% |                   |             |            | P   |       |     |      |        |     |         |     |
|                                                         |                   |             |            |     | [kVA] |     | [kW] | [kVAr] | L1  | L2      | L3  |
and1,6%.
|     |     |     |     | 5   | 56,3 |     | 53,6 | 16,9 | 9,3 | 9,5 | 8,6 |
| --- | --- | --- | --- | --- | ---- | --- | ---- | ---- | --- | --- | --- |
|     |     |     |     | 6   | 21,1 |     | 20,3 | 5,7  | 10  | 7   | 4,9 |
V. SERVERROOM (LOWESTLEVEL)MEASUREMENTS
|     |     |     |     | A.  | Measurement pointP7 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
This measurement point is located on a single-phase
circuitsupplyingmultiple suppliesin a rack. The reactive
|     |     |     |     | power is capacitive, |     |     | and its magnitude is approximately    |     |     |     |     |
| --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
|     |     |     |     | equal to the active  |     |     | power. The current leads the voltage  |     |     |     |     |
by 47°. Figure 12shows the current waveform.The small
|     |     |     |     | amount       |     | of  active      | power  | and                           | the  | large | current  |
| --- | --- | --- | --- | ------------ | --- | --------------- | ------ | ----------------------------- | ---- | ----- | -------- |
|     |     |     |     | displacement |     | are typical for |        | lightly loaded supplies. The  |      |       |          |
Figure 8.Current waveformfor P5
THD of the current is 46%(
|     |     |     |     |               | ). The harmonic H3 is about |     |                              |     | 25% and H5, H7 and  |     |            |
| --- | --- | --- | --- | ------------- | --------------------------- | --- | ---------------------------- | --- | ------------------- | --- | ---------- |
|     |     |     |     | H11 about 14% |                             |     | (Figure 13). The voltage THD |     |                     |     | is 2.14%,  |
which is higher than UPS (Q60) due to additional voltage
drops caused by current harmonics.
|     |     |     |     | B.  | Measurement pointP8 |              |     |        |         |                  |     |
| --- | --- | --- | --- | --- | ------------------- | ------------ | --- | ------ | ------- | ---------------- | --- |
|     |     |     |     |     | The  last           | measurement  |     | point  | is  on  | a  single-phase  |     |
circuit for powering multiple newer generation power
|     |     |     |     | supplies    | in a rack. |                                              | The waveform of the current is nearly  |      |          |                 |     |
| --- | --- | --- | --- | ----------- | ---------- | -------------------------------------------- | -------------------------------------- | ---- | -------- | --------------- | --- |
|     |     |     |     | sinusoidal  |            | (Figure                                      | 14).                                   | The  | supplies | are  moderately |     |
|     |     |     |     | loaded. The |            | current leads the voltage by about 15°. The  |                                        |      |          |                 |     |
individual harmonics are less than5%(Figure 15)and the
|     |     |     |     | total harmonic distortion is less than |     |     |     |     | 10%. | Voltage total  |     |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ---- | -------------- | --- |
Figure 9.Harmonic orderfor P5
|     |     |     |     | harmonic |     | distortion | (THDv) | value | is  | 2,04% | for  both  |
| --- | --- | --- | --- | -------- | --- | ---------- | ------ | ----- | --- | ----- | ---------- |
measurement points.
Current waveformfor P6
Figure.10
Figure 12.Current waveformfor P7
Figure 13.Harmonic orderfor P7
Figure 11.Harmonic orderfor P6
156
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:05:47 UTC from IEEE Xplore.  Restrictions apply.

Factor Correction (PFC). However, measurements show
|     |     |     |     | that points at downstream            |     | levels closer to nonlinear loads  |             |     |          |
| --- | --- | --- | --- | ------------------------------------ | --- | --------------------------------- | ----------- | --- | -------- |
|     |     |     |     | such as servers or air conditioners, |     |                                   | have larger |     | current  |
harmonic distortion values and contribute toanincrease in
|     |     |     |     | system energy losses.         |     | Future work will be |                                | to develop | a   |
| --- | --- | --- | --- | ----------------------------- | --- | ------------------- | ------------------------------ | ---------- | --- |
|     |     |     |     | filter for harmonic reduction |     |                     | and test its functionality in  |            |     |
the analyzed data center.
ACKNOWLEDGMENT
|     |     |     |     | The authors would like to |     | thank the | company DataBox  |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --------- | ---------------- | --- | --- |
Ltd.for their insightful comments and support.
Figure 14.Current waveformfor P8
REFERENCES
[1] IEA (2021), Data Centres and Data Transmission Networks, IEA,
|     |     |     |     | Paris,  Accessed  | on:  | January  | 2022.  [Online], |     | Available: |
| --- | --- | --- | --- | ----------------- | ---- | -------- | ---------------- | --- | ---------- |
https://www.iea.org/reports/data-centres-and-data-transmission-
networks.
[2] H. Zubi and S.Khalifa, “Power Quality Investigation of a Typical
Telecom Data Centre Electrical Network”, Proceedings of 2016
|     |     |     |     | 4rd  International | Coriference  |              | on  Control  | Engineering | &   |
| --- | --- | --- | --- | ------------------ | ------------ | ------------ | ------------ | ----------- | --- |
|     |     |     |     | Information        | Tecnology    | (CEIT-2016)  | Tunisia,     | Hammamet-   |     |
December, 16-18, 2016.
[3] P. Harinath, K. Kamalesaran, M.Venkateshwaran, C. Sreenath, S.
|     |     |     |     | Prabhakaran, V.  | Kirubakaran, “A Critical Analysis of Power     |           |                 |                |     |
| --- | --- | --- | --- | ---------------- | ---------------------------------------------- | --------- | --------------- | -------------- | --- |
|     |     |     |     | Quality  Issues  | in  Data                                       | Center”,  | 2016  Biennial  | International  |     |
|     |     |     |     | Conference on    | Power and Energy Systems: Towards Sustainable  |           |                 |                |     |
Energy (PESTE).
Figure 15.Harmonic orderfor P8 [4] A. Hoevenaars, P. Hoevenaars, “DATA CENTER COOLING
|     |     |     |     | HARMONICS  | - HOW  | TO  | GET  “GOOD”  | WITHOUT  | THE  |
| --- | --- | --- | --- | ---------- | ------ | --- | ------------ | -------- | ---- |
“BAD””,2020. IEEE/IAS56thIndustrial and Commercial Power
Systems Technical Conference (I&CPS)
TABLE3.Serverroommeasured values
S P Q THDi [5] B. Illinets, “Mitigating PQ Problems in Legacy Data Centers”,
| P     |      |        |     | Accessed  | on:  November  |     | 2020.  [Online],  |     | Available:  |
| ----- | ---- | ------ | --- | --------- | -------------- | --- | ----------------- | --- | ----------- |
| [kVA] | [kW] | [kVAr] | [%] |           |                |     |                   |     |             |
https://www.researchgate.net/publication/255241475_Mitigating_
| 7 0,42 | 0,29 | 0,31 | 46  |     |     |     |     |     |     |
| ------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
PQ_Problems_in_Legacy_Data_Centers.
| 8 0,62 | 0,6 | 0,17 | 9,5 |     |     |     |     |     |     |
| ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
[6] I. Wallace, “Harmonic Distortions in Data Centers”, TCI, LLC,
February 2016, Rev0.
[7] C.Boonseng, R. Boonseng, K. Kularbphettong, “The 3rdHarmonic
VI. CONCLUSION
|     |     |     |     | current ant Power Quality Improvements of Data |     |     |     | Centers Using  |     |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | -------------- | --- |
In this paper,power quality analysisat different points  Hybrid Power Filters”, 2019 22nd International Conference on
in a data center is given. The current and voltage THD  Electrical Machines and Systems (ICEMS).
values measured at the Point of Common Coupling (PCC)  [8] IEEE  Std  519-2014,  IEEE  Recommended  Practices  and
|     |     |     |     | Requirement | for Harmonic Control in Electrical Power Systems,  |     |     |     |     |
| --- | --- | --- | --- | ----------- | -------------------------------------------------- | --- | --- | --- | --- |
are in accordancewith the IEEE std. 519-2014for General
New York, NY: IEEE.
| Distribution Systems up to 69kV. |     | The busbar harmonic  |     |     |     |     |     |     |     |
| -------------------------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
distortionupstream of the Uninterruptible Power Supplies
| (UPS) is low, since | each UPS has its own internal Power  |     |     |     |     |     |     |     |     |
| ------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
157
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:05:47 UTC from IEEE Xplore.  Restrictions apply.