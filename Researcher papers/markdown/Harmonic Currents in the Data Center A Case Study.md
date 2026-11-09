Harm onic Currents
in the Data Center:
A Case Study
White Paper #38

Executive Summary
This document provides an overview of how problems related to harmonic neutral currents
are solved by load diversity, with specific focus on Information Technology data center
environments. Detailed measurements of an actual operating data center are presented.
This case study illustrates the way that load diversity mitigates harmonic current levels and
lowers shared neutral current in multi-wire feeders and branch circuits.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 2
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

Introduction
Nonlinear loads cause harmonics to flow in the power lines. Harmonics are unwanted currents that are
multiples of the fundamental line frequency (50 or 60 Hz). Excessive harmonic currents can overload wiring
and transformers, creating heat and, in extreme cases, fire. In information technology power systems it is
important to know when and how to address this issue. Recently, the problem has been mitigated by load
diversity. This white paper extends the concepts related to modern IT data center loads presented in APC
White Paper #26, “Hazards of Harmonics and Neutral Overloads”.
Nonlinear loads
Many desktop personal computers still present a nonlinear load to the AC supply. This is because they
have a power supply design known as a "capacitor input switch mode power supply". Much of today’s
Information Technology equipment including servers, routers, hubs, and storage systems almost universally
use a different power supply design known as "Power Factor Corrected". These devices present a very
linear load to the AC supply and do not generate harmonic currents. In fact they are one of the cleanest
loads on the power grid and generate less harmonic current than many other devices such as fluorescent
lighting or variable speed motors. Ten years ago, these devices were nonlinear loads like Personal
Computers, but today the majority of these loads are subject to international regulations which require them
to be made with the "Power Factor Corrected"(PFC) design.1
Regulations
There is a significant interest on the part of society to reduce the amount of nonlinear loading on AC power
systems. This loading reduces the distribution capacity of the public power system, and it can degrade the
quality of the power by distorting the AC power waveform delivered to nearby customers. It can also cause
a risk of fire on a customer's premises.
In the 1980s, public utilities and international regulatory authorities including the IEC (International
Electrotechnical Commission) took notice of the trend that an increasing percentage of electrical power
consumption was caused by electrical equipment, and that an increasing percentage of this equipment
used a "capacitor input switch mode power supply". Fluorescent lighting, high performance air conditioning
systems, and personal computers were key product categories driving this change. In response the IEC
created in 1982 the international standard IEC 555-2 "Harmonic injection into the AC Mains". This standard
specifically limited harmonic current injection of "non-professional" equipment. Switzerland, Japan, and
other countries adopted the IEC 555 standard soon after release. Global suppliers of computing products
first began to see a restriction on the ability to sell computers into countries that had adopted IEC 555-2 in
the mid 1980's. This situation precipitated the development of Power Factor Corrected power supply
technology.
In 1995, the IEC introduced an update of the IEC 555-2 standard, called IEC 1000-3-2. In IEC 1000-3-2 the
scope of applicability was greatly expanded over IEC 555-2 to cover all equipment drawing up to 16Amps
per phase. The standard added additional limitations on both the absolute and percentage values of
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 3
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

harmonics for products with nonlinear switch mode power supplies. Many countries outside of the US and
the EC adopted this standard. The EC adopted its own version of this standard later in 1995 as EN61000-
3-2 and required equipment manufacturers to comply with the standard under an EC directive called "The
EMC Directive". This directive gave manufacturers until 1998 to comply for existing product designs. Later,
the EC further extended this deadline to Jan 1, 2001.
By 1995, almost all new computer equipment introduced for networks and communication was in
compliance with IEC 1000-3-2. Even though not all countries had adopted the standard immediately, the
standard represented a formidable trade barrier for companies that delayed compliance. Computer OEMs
were almost universally specifying IEC 1000-3-2 compliance for OEM equipment intended for system
integration. This caused virtually 100% of the IT industry to come into compliance well before the Jan 1,
2001 deadline or even the original 1998 deadline.
The USA has proposed an amendment called "amendment 14" to the standard which would weaken the
standard and allow more harmonics. It is not clear which countries will adopt this amendment. Products for
sale in the EC and many countries must meet the EN61000-3-2 standard. The US has not formally adopted
this standard. Information technology equipment manufactured today is universally designed for worldwide
application and therefore requires the CE mark and must meet the IEC standard. Therefore, IT equipment
other than small PCs universally complies with the standard (non-compliant PCs are still sold in the USA).
Over the past 5 years, due to the natural introduction of new equipment and change-out of equipment with
newer models, harmonics have been greatly reduced in the data center environment.1
Consequences of the load diversity on actual IT data center power systems
1. Load diversity as used in this paper is the natural ratio of linear (PFC) loads to nonlinear loads in the IT
data center rack environment. The harmonic currents in the neutral circuit are reduced to the point where
the use of oversized neutrals in multi-wire feeders and branch circuits are unnecessary.
2. This load diversity also reduces the "K" factor of the system transformer to an average value of
significantly less than K-9.
In a practical system, the harmonic currents are much lower than the theoretical values for the following
reasons:
1. International IT equipment manufacturers must meet the harmonic regulations over wide ranges of
voltage, manufacturing tolerances, and load, the result being that actual products are well below the
compliance limits at typical operating conditions.
2. Some loads are connected phase-to-phase (particularly in the USA), and therefore do not contribute to
the neutral current
3. Even with the reluctance of the USA to adopt the IEC limits, the majority of the IT data center loads have
become linear (PFC). This system load diversity and it’s impact on harmonics and shared neutrals has
been previously unknown to system designers.
Nonlinear neutral currents in 4-wire wye circuits without load diversity
The formula for calculating the rms neutral currents for balanced nonlinear loads has been defined as
follows.2
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 4
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

The triplen harmonic currents are additive in the neutral and because the 3rd harmonic (180Hz) dominates,
this has lead to further simplification of the formula.2
The net result is the present design practice of rating the neutral conductors for three-phase Wye 4-wire
feeders and branch circuits in IT data center environment at 173% of the phase current. This practice is
fine, if the actual load is 100% nonlinear load. While this is correct for a high-density nonlinear distributed
PC desktop or office environment, it doesn’t take into account load diversity in an IT data center rack
environment.
Neutral current in 4-wire wye circuits with load diversity
Where the diversity is encountered, i.e., a mixture of linear and nonlinear loads, the following formula can
be used to calculate the total rms neutral current.3
k = harmonic currents, i.e., triplens – 3rd (180Hz), 9th (540Hz), 15th (900Hz), etc.
This formula takes into account both the linear and nonlinear load effects on the neutral conductor. It also
accounts for load imbalance of either linear or nonlinear loads. Generally it is sufficient to use the 3rd & 9th
as these are two dominant triplen harmonic currents.
Power factor in IT data center circuits with load diversity
Where a circuit contains a diversity of loads the total circuit power factor can be calculated with the
following formula.2
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 5
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

Where: DPF = Displacement Power Factor THD= Circuit Current % Total Harmonic Distortion
i
expressed as a decimal.
Harmonics and Neutral Current Study at OneBeacon in Foxboro MA
The effects of load diversity are best illustrated through review of actual system data measurements.
Measurements were conducted to determine the power factors, neutral current levels, and harmonics in a
typical IT data center rack environment. Two installed APC InfraStruXure™ (ISX) Type B systems were
used in this study. The InfraStruXure™ Type B architecture uses three-phase 20A multi-wire branch
circuits (4-wire +ground) to efficiently feed power to high density IT rack enclosures.
The system studied is installed at OneBeacon in Foxboro MA. This system consists of a 60kVA, K-1, 480
delta input, 208Y/120 output transformer feeding an APC Symmetra™ PX (40kW) three-phase UPS which
feeds a three-phase PDU panelboard supplying 16 rack cabinets via individual UL Listed individual multi-
wire branch circuits. Each branch circuit is a UL Listed 20A 4-wire + ground 208Y//120 whip utilizing a 5
conductor 12AWG SOOW cord terminated with an L21-20R Cord Cap. This in turn feeds an APC ISX
three-phase power distribution strip with 120V receptacles mounted in each rack enclosure.
Each branch circuit was tested for voltage & current waveforms, total power factor (PF), displacement
power factor (DPF), percent current total harmonic distortion (% THD) and 3rd, 5th, 7th, 9th, 11th, 13th current
I
harmonics percentages. Two of the 48 single-phase branch circuits were not in use and these are omitted
from any calculations related to this study. Three distinct current wave form characteristics were observed
on the circuits studied.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 6
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

This waveform is from circuit breaker (CB) 2 - Phase B. It is representative of linear (PFC) power supply
loads such as servers, disk systems, and routers. In the typical IT data center rack environment this is the
dominant load. Branch voltage is the upper trace and branch current is the lower trace.
This is the waveform from circuit breaker (CB) 9 - Phase C. It represents the nonlinear power supply loads
such as monitors. In the typical IT data center rack environment this is the minority load.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 7
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

This waveform is from circuit breaker (CB) 1 - Phase A. The current waveform represents the positive
effect of the load diversity. In this case the relative high ratio of linear to nonlinear load is seen in the
waveform. It also can be seen in the system power factor and THD measurements. When loads with
differing characteristics are combined in a single circuit they add together to create a new harmonic current
and PF profile. Because this example exhibits high power factor and relatively low current THD we can
deduce that the majority load on this circuit is linear (PFC). The circuit load diversity can be defined as the
ratio of linear load to nonlinear load. For example, 1200VA linear and 300VA nonlinear would be 1200:300
= 4:1 ratio. A diversity of greater than one indicates that the linear loads dominate and dramatically reduce
the effect of the non-linear load. A diversity of zero is a pure non-linear load. Any diversity of greater than
zero provides some mitigation from the theoretical problems associated poor power factor and current
harmonics.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 8
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

Harmonics Study at OneBeacon in Foxboro Massachussetts
| Breaker |     |     |     |     |     |     |     | Harmonics % (current) |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
Number Phase Current Voltage PF  DPF VA Watts %THD(I) 3rd 5th 7th 9th 11th 13th
| 1   | A   | 4.48 120.5 | 0.97 | 0.98 | 540  | 524  | 20   | 19   | 2.6  | 3.3 | 2.5 | 2.2 | 0.7 |
| --- | --- | ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | --- |
|     | B   | 2.49 121.6 | 0.93 | 0.99 | 303  | 282  | 34.2 | 32.1 | 4    | 7.1 | 7.4 | 5.4 | 2.9 |
|     | C   | 2.45 120.6 | 0.93 | 0.98 | 295  | 275  | 31.5 | 27.1 | 10.6 | 10  | 4.8 | 2.3 | 1   |
|     | N   | 3.04       |      |      |      |      |      |      |      |     |     |     |     |
| 2   | A   | 8.64 121.8 | 0.96 | 0.96 | 1052 | 1010 | 6.1  | 5.2  | 2.4  | 1   | 1.2 | 0.4 | 0.3 |
|     | B   | 4.6 121.4  | 0.95 | 0.95 | 558  | 531  | 5.9  | 5    | 2.3  | 0.9 | 1.3 | 0.2 | 0.6 |
|     | C   | 4.45 121.9 | 0.96 | 0.95 | 542  | 521  | 7    | 6.2  | 2.3  | 0.9 | 1.5 | 0.3 | 0.1 |
|     | N   | 4.01       |      |      |      |      |      |      |      |     |     |     |     |
3 A 5.56 120.5 0.97 0.98 670 650 12.7 12.5 1.2 1.3 1.4 0.8 1.6
|     | B   | 2.54 121.6 | 0.97 | 0.98 | 309 | 300 | 18.4 | 18.1 | 2.2 | 1   | 1.6 | 1.2 | 1.6 |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     | C   | 6.28 121.9 | 0.98 | 0.98 | 766 | 750 | 10.3 | 10.1 | 0.9 | 0.8 | 0.7 | 0.3 | 0.7 |
|     | N   | 1.96       |      |      |     |     |      |      |     |     |     |     |     |
4 A 0.89 121.8 0.98 0.98 108 106 11.8 10.9 1.1 1.6 0.2 2.5 2.2
|     | B   | 3.73 121.7 | 0.97 | 0.97 | 454 | 440 | 8    | 7.5  | 1.5  | 1.3 | 0.9 | 1.1 | 0.7 |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | ---- | --- | --- | --- | --- |
|     | C   | 0.97 122   | 0.98 | 0.97 | 118 | 116 | 11.6 | 10.1 | 1.6  | 1.6 | 2.6 | 2.9 | 1.9 |
|     | N   | 2.82       |      |      |     |     |      |      |      |     |     |     |     |
| 5   | A   | 2.77 121.7 | 0.98 | 0.98 | 337 | 330 | 7.3  | 6.8  | 1.7  | 1.1 | 0.9 | 0.8 | 0.4 |
|     | B   | 2.09 121.6 | 0.97 | 0.99 | 254 | 247 | 23.7 | 17.7 | 11.1 | 8.5 | 5   | 3.2 | 0.9 |
|     | C   | 2.47 120.7 | 0.98 | 0.98 | 298 | 292 | 7.3  | 6.9  | 1.4  | 0.4 | 1   | 0.3 | 0.4 |
|     | N   | 1.12       |      |      |     |     |      |      |      |     |     |     |     |
| 6   | A   | 3.74 121.8 | 0.99 | 0.96 | 456 | 451 | 6.7  | 6.3  | 1.7  | 0.5 | 0.9 | 0.2 | 0.4 |
|     | B   | 3.05 121.7 | 0.95 | 0.95 | 371 | 353 | 7.8  | 1    | 7.2  | 1.7 | 0.6 | 1.2 | 0.7 |
|     | C   | 1.95 121.9 | 0.97 | 0.98 | 238 | 231 | 6.5  | 6.1  | 1.5  | 0.6 | 1.6 | 0.4 | 0.7 |
|     | N   | 1.8        |      |      |     |     |      |      |      |     |     |     |     |
7 A 3.24 121.7 0.97 0.99 394 382 20.6 18.8 6.4 4.1 2.5 1.1 1.8
|     | B   | 6.4 121.6  | 0.98 | 0.99 | 778 | 763 | 16.1 | 14.8 | 4.7  | 3.3  | 1    | 0.8  | 1.1  |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | C   | 4.44 120.6 | 0.97 | 0.98 | 535 | 519 | 17.2 | 15.9 | 5.1  | 3.3  | 1    | 1.1  | 1.4  |
|     | N   | 3.55       |      |      |     |     |      |      |      |      |      |      |      |
| 8   | A   | 0.12 121.8 | 0.65 | 0.68 | 15  | 10  | 23   | 17.5 | 2.3  | 2.2  | 4.1  | 2.2  | 2    |
|     | B   | 0.1 121.7  | 0.91 | 0.94 | 12  | 11  | 83   | 65.1 | 21.1 | 18.3 | 25.2 | 19.1 | 16.9 |
|     | C   | 0 121.9    | N/A  | N/A  | 0   | N/A | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  | N/A  |
|     | N   | 0.1        |      |      |     |     |      |      |      |      |      |      |      |
9 A 1.67 121.8 0.94 0.99 203 191 31.6 22.2 13.6 14.4 7.6 6.3 3.5
|     | B   | 1.31 120.5 | 0.99 | 0.99 | 158 | 156 | 12.7 | 7.2  | 1.1 | 4.6 | 3.1  | 3.3  | 2.9  |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | ---- | ---- | ---- |
|     | C   | 1.07 121.9 | 0.57 | 0.98 | 130 | 74  | 81.5 | 48.1 | 42  | 35  | 27.2 | 19.4 | 12.5 |
|     | N   | 1.69       |      |      |     |     |      |      |     |     |      |      |      |
10 A 0.8 121.8 0.65 0.99 97 63 75.4 50.4 38.2 29.7 20.7 12.6 0.04
B 0.75 121.7 0.6 0.99 91 55 79.5 56.4 46.3 29.7 21.9 12.1 4.2
C 1.45 121.9 0.67 0.99 177 118 73.9 57.4 37.3 27.5 13.3 6 1.9
|     | N   | 1.76    |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11  | A   | 0 121.8 | N/A | N/A | 0   | 0   | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
B 0.11 121.7 0.62 0.78 13 8 56.7 12.3 26.7 19.3 16.4 17.4 14.3
|     | C   | 0.11 120.6 | 0.17 | 0.25 | 13  | 2   | 73.7 | 69.3 | 8.3 | 7   | 8.3 | 1.4 | 2.7 |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     | N   | 0.13       |      |      |     |     |      |      |     |     |     |     |     |
12 A 4.66 121.8 0.97 0.98 568 551 11.2 10.5 2.8 1.2 0.4 0.9 0.8
|     | B   | 3.95 121.7 | 0.96 | 0.98 | 481 | 461 | 17.5 | 16.5 | 4   | 3.1 | 0.7 | 1.9 | 1.7 |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     | C   | 6.72 120.8 | 0.96 | 0.97 | 812 | 779 | 12   | 11.2 | 3.3 | 1.7 | 0.6 | 0.9 | 0.7 |
|     | N   | 2.97       |      |      |     |     |      |      |     |     |     |     |     |
| 13  | A   | 2.99 121.7 | 0.96 | 0.99 | 364 | 349 | 7.3  | 6.9  | 1.7 | 1   | 0.7 | 0.3 | 0.5 |
|     | B   | 3.78 120.5 | 0.97 | 0.95 | 455 | 442 | 29.3 | 6.9  | 9.3 | 5.1 | 2.9 | 2.4 | 0.8 |
|     | C   | 4.27 121.8 | 0.97 | 0.99 | 520 | 504 | 13.7 | 12.9 | 2.7 | 1.3 | 2.4 | 1.6 | 0.8 |
|     | N   | 2.13       |      |      |     |     |      |      |     |     |     |     |     |
14 A 1.34 121.7 0.96 0.98 163 157 17.8 17.6 1.9 1.3 0.3 2.6 0.9
|     | B   | 3.54 121.7 | 0.97 | 0.98 | 431 | 418 | 15.7 | 15.1 | 1.5 | 2.1 | 1.6 | 1.8 | 0.6 |
| --- | --- | ---------- | ---- | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     | C   | 3.2 120.6  | 0.97 | 0.98 | 386 | 374 | 13.9 | 13.3 | 0.9 | 2.5 | 0.1 | 1.3 | 1.2 |

Using the raw branch circuit data from the chart above, analysis was done and bar charts were created to
provide better visualization of the circuit conditions.

2003 American Power Conversion.  All rights reserved.  No part of this publication may be used, reproduced, photocopied, transmitted, or
9
stored in any retrieval system of any nature, without the written permission of the copyright owner.  www.apc.com                        Rev 2003-1

The circuit numbers 1-48 correspond to the individual breaker poles in the main PDU panelboard as shown
in the previous data chart. Therefore, “1, 2, 3 are multi-wire branch circuit #1 in the above analysis chart,
i.e., A, B, and C phases respectively. This data shows that none of the 16 three-phase multi-wire branch
circuits are carrying balanced load.
This chart shows the branch circuit loads relative to the 16A conductor rating for each branch. Once again
there is no balance indicated for any of the three-phase multi-wire circuits and the highest % load is ~ 55%
on branch # 4 (CB #2- A Phase). The majority circuit loading is under 30% of the conductor rating.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 10
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

This chart is the analysis of the percent total harmonic distortion for the currents (% THD) on each branch
i
circuit. This shows us that the majority of branch circuits are loaded with less than 20% THD. If we
i
compare this to the previous charts we can see a pattern developing, i.e., the loads with the highest THD
i
(circuits 21-33) have some of the lowest branch circuit loading, i.e., ~ 10% or less of the circuit rating.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 11
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

This chart shows the total power factor of all branches. We can see that the majority load is .95 or better
and also has same pattern as the previous charts, i.e., lowest power factor is the lightest loaded circuits.
The overall power factor of the system will be higher than the average of these power factors, because the
data shows that the circuits with low power factor also have low current, and therefore the circuits with low
power factor make a low contribution to the total reactive power.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 12
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

This is the key chart that summarizes the implications regarding the sizing of neutral wires. The chart
shows the neutral load current versus 20A branch rating for all 16 multi-wire branch circuits. Legacy design
guidelines would predict that these neutral currents would be as much as 170% of rating, whereas the data
shows actual currents in a real installation are on the order of 20%. Furthermore, the dominant source of
the observed neutral currents is actually load imbalance between phases, and not harmonic currents.
These results are expected when an understanding of modern computer power supplies is applied to the
analysis, and they clearly show that the legacy approach of oversizing neutrals in this application is
unwarranted.
System phase loading in all branch circuits is under 60% and is under 20% for the majority of the 48 branch
circuits studied. The circuits with highest I percentage exhibit the lowest circuit loading. These same
THD
circuits also exhibit the lowest neutral currents and poorest power factor. The reason for this is that they
represent a very small fraction of the modern IT data center load.
OneBeacon feeder circuit data analysis
In the chart below we see the effects of load diversity on the feeder circuit from the UPS to PDU panel
board. We also see there is harmonic current flowing on the neutral conductor. But the neutral current is
also ~41.7% of the lowest phase current (19.9/47.7 = .41719). The feeder neutral in this case is a 1/0AWG
conductor rated at 150 amperes. Therefore the % load on the neutral is ~ 13.3% of it’s 150A rating
(19.9/150 = .13266.). At the same time the load power factor is very high, at .97-.98PF. Once again we
see the positive load diversity effects in the feeder, i.e., same as those seen in the branch circuit waveform
of CB 1- A Phase shown previously.
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 13
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1

Feeder Harmonics Study at OneBeacon in Foxboro Massachussetts
UPS Harmonics % (current)
Output Phase Current Voltage PF DPF VA Watts %THD(I) 3rd 5th 7th 9th 11th 13th
Q2 A 47.7 120.4 0.98 0.99 5743 5628 11.7 11.2 1.4 2.5 16 18 0.8
B 52 120.5 0.98 0.98 6266 6141 13.6 13.1 1.3 2.7 0.8 1.2 0.7
C 49.2 120.6 0.97 0.98 5934 5756 14.4 13.5 2.5 3.5 1.3 1.2 0.7
N 19.9
IT data center rack environment loads and K-Factor
The K-factor requirement for the system can be determined from the data measured at the example site.
The calculated K-factor for the feeder load at OneBeacon is K-1.25, i.e., using the C Phase harmonic
current values.
Legacy design guidelines would predict that the K-factor requirement would be as much as 21, whereas the
data shows the actual K-factor requirement is approximately 1. These results are expected when an
understanding of modern computer power supplies is applied to the analysis, and they clearly show that the
legacy approach of specifying high K-factors of 15 or 21 in this application is unwarranted.
Conclusions
The power characteristics of the modern IT data center rack environment are very different from the
computer room of the early 1980’s. Dramatic improvements in IT equipment power factor and harmonics
have lead to corresponding improvements in the overall system power factor along with a large harmonic
current reduction. Actual measurements of real systems demonstrate these improvements. K-factor
specifications of 15 or 21 drive unnecessary cost when the actual K-factor of real installation is
approximately 1. Neutral oversizing of 170% to 200% drives unnecessary costs when the actual neutral
current is only 20% of circuit rating. Legacy design practices and specifications for data center power
systems should be updated to reflect the actual requirements of modern data centers.
References
[1] APC White Paper #26 - Hazards of Harmonics and Neutral Overloads
[2] Power Electronics- Converters Applications, and Designs – Second Edition, Mohan, Undeland and
Robbins
[3] Fundamentals of Power Electronics, R.W. Erickson
http://ece-www.colorado.edu/~pwrelect/book/slides/Ch15slide.pdf
[4] http://www.electrician.com/electa1/electa4htm.html
2003 American Power Conversion. All rights reserved. No part of this publication may be used, reproduced, photocopied, transmitted, or 14
stored in any retrieval system of any nature, without the written permission of the copyright owner. www.apc.com Rev 2003-1