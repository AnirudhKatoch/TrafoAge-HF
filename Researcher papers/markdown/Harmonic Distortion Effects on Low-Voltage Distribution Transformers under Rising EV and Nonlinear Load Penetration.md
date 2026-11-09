Harmonic Distortion Effects on Low-Voltage
Distribution Transformers under Rising EV and
Nonlinear Load Penetration
Fayezeh Mahmoudnezhad, Araceli Herna´ndez Pablo Rodr´ıguez-Pajaro´n
Escuela Te´cnica Superior de Ingenieros Industriales REE
Universidad Polite´cnica de Madrid Madrid, Spain
Madrid, Spain pablo.rpajaron@upm.es
f.mahmoudnezhad@upm.es, araceli.hernandez@upm.es
Abstract—Thegrowingproliferationofpowerelectronic-based excessive heating of the conductors and transformers, over-
non-linear loads is leading to non-sinusoidal waveforms of cur- loadingoftheneutralconductors,unintendedrelayoperations,
rentsandvoltagesinthemodernpowersystems.Thesenon-linear
and potential resonance with network impedances [4], [5].
loadsinjectharmoniccomponentsthathaveasignificantimpact
These harmonic currents further accelerate the degradation
onlow-voltage(LV)distributiontransformers.Theprimaryeffect
ofharmoniccurrentsistheamplificationoffrequency-dependent of critical infrastructure components—particularly distribu-
losses, leading to higher operating temperatures and accelerated tion transformers and cables—resulting in reduced opera-
thermaldegradationofthetransformer’sinsulationsystem.This tional lifespan, increased thermal stress, intensified losses,
article explores the application of IEEE Std C57.110 in realistic
and higher maintenance requirements [6], [7]. As the share
scenarios involving the integration of electric vehicles (EVs)
of these nonlinear loads continues to increase, field mea-
and residential nonlinear loads, based on field measurements
of harmonic current injections from both sources. The anal- surement–based harmonic assessment has become essential
ysis assesses the resulting harmonic distortion and its impact to accurately characterize harmonic emission profiles and
on LV distribution transformers. The results demonstrate that their cumulative effects on transformer performance, thermal
harmonic distortion can potentially increase transformer losses
behavior, and lifetime expectancy.
and thermal stress, particularly under high penetration of EVs
Toaddressthesechallenges,ourstudyperformsafieldmea-
and other nonlinear loads. Furthermore, the study underscores
the importance of appropriate transformer sizing and strategic surement–based assessment of harmonic distortion effects on
over-dimensioningaseffectivemeasurestomitigatetheseadverse LV distribution transformers under increasing penetration of
effects. These findings suggest that existing harmonic standards residentialnonlinearloadsandEVs.Steady-stateanddynamic
andtransformerdesignpracticesmayrequirerevisiontoaccount
thermal aging analyses are combined to quantify transformer
for the evolving composition of modern distribution networks.
stress under temporally clustered and highly variable operat-
Index Terms—Electric vehicles, power quality assessment,
Current harmonics, harmonic loss factor, IEEE C57.110™, ing conditions, and to demonstrate transformer sizing as an
transformer effective mitigation strategy for ensuring reliable LV network
operation in the context of the ongoing energy transition.
I. INTRODUCTION
II. IEEESTDC57.110FRAMEWORKFORTRANSFORMER
In modern low-voltage (LV) distribution networks, the THERMALASSESSMENT
growing proliferation of power-electronic-based residential
IEEE Std C57.110 is a recommended practice focused on
loads and electric vehicles (EVs) represents a major step to-
determiningtheloadingcapabilityofliquid-immersedanddry-
ward developing sustainable and decarbonized power systems
type power and distribution transformers when they supply
[1]. However, widespread integration of these nonlinear loads
non-sinusoidal load currents [8]. This recommended practice
inherently introduces harmonic distortion in both current and
applies exclusively to two winding transformers [9] and does
voltage waveforms, primarily due to the switching operation
notcoverrectifiertransformers[10].Thisstudyfocusesonoil-
and control strategies of their power-electronic interfaces [2],
immersedtransformers,astheyaremorecommonlyemployed
[3]. Since network components are designed to operate un-
in residential distribution networks than dry-type transformers
der nearly sinusoidal steady-state conditions, harmonics can
[11]. The following sections present key standard-based prin-
substantially deteriorate power quality and system reliability.
ciplesandgoverningequationsforanalyzingharmoniceffects
Uncontrolled harmonic levels lead to additional power losses,
in transformers. The standard has been applied to several case
studiestodemonstratehowharmonicsintroducedbynonlinear
ThisworkwassupportedbytheMinisteriodeCienciaeInnovacio´n(MCIN)
loads can affect transformer performance, thermal behavior,
la Agencia Estatal de Investigacio´n (AEI) por el FEDER under Project
PID2022-141609OB-I00. and lifetime expectancy.
979-8-3315-8138-1/26/$31.00 ©2026 IEEE
02639611.6202.88985MGSEP/9011.01
:IOD
|
EEEI
6202©
00.13$/62/1-8318-5133-8-979
|
)MGSEP(
gniteeM
lareneG
yteicoS
ygrenE
&
rewoP
EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:20:18 UTC from IEEE Xplore. Restrictions apply.

A. Transformer Loss Components C. Transformer Thermal Aging Modeling
Transformer losses are classified into no-load (excitation) After determining harmonic-dependent load
loss, denoted as P , and load (impedance) loss, denoted losses—including all stray loss components relevant in
NL
as P . The load loss is subdivided into I2R (copper) loss, liquid-immersed transformers—the corresponding thermal
LL
P, and the stray loss, P . Stray losses originate from response can be assessed through the top-oil temperature
TSL
stray electromagnetic flux in the windings, core, core clamps, (TOT)riseoverambient,θ ,andthehottest-spottemperature
TO
magneticshields,andthetankstructure.Accordingly,thetotal (HST) rise over the top-oil layer, θ , as expressed by the
g
stray loss is divided into the winding stray loss, P , and the following equations:
EC
stray loss in other metallic components, P . The total load
loss can then be expressed as follows:
OSL
θ =θ ×
(cid:18)
P LL +P NL
(cid:19)0.8
(6)
TO TO−R P +P
LL−R NL
P =P +P +P (1)
LL EC OSL (cid:18)
P
(cid:19)0.8
θ =θ × LL (7)
B. Transformer Harmonic-induced Losses g g−R P
LL−R
Afundamentalimpactofharmonicdistortionistheincrease where θ is the TOT rise over ambient under rated
TO−R
in the RMS load current experienced by the transformer, aris- conditions (°C), and θ is the HST rise over the top-oil
g−R
ing from the cumulative contribution of individual harmonic
under rated conditions (°C). Having determined the corre-
componentsandhighlightingtheneedtoexplicitlyincorporate
sponding top-oil and hottest-spot temperature rises, the HST
theseeffectsintotransformerloadingandthermalperformance in the transformer winding, θ , is obtained as:
HS
assessment. The governing expression is as follows:
(cid:118) θ HS =θ TO +θ g +θ Ambient (8)
I =
(cid:117)
(cid:117) (cid:116)
h=
(cid:88)
hmax
(I h )2 (2) where θ Ambient is the ambient temperature (°C). Once
the harmonic contribution to the HST has been determined,
h=1
the resulting loss-of-life (LOL) can be estimated. The aging
where I is the total RMS load current, h is the highest
max acceleration factor, F , is defined in Equation (9) using a
significant harmonic order, I is the RMS load current asso- AA
h referenceHSTof110◦C.ForHSTvalueshigherthan110◦C,
ciated with the h-th harmonic order.
F > 1 indicates accelerated insulation aging, whereas
The load losses in a transformer subjected to nonsinusoidal AA
F <1reflectsareducedageingrate.Theempiricalconstant
loadcurrentscanbecharacterizedusingharmoniclossfactors, AA
of 15000 represents the effective activation energy of the
which quantify the frequency-dependent increase in winding
insulation degradation process, expressed in Kelvin.
eddy-currentlosses,F ,andinotherstraylosses,F .
HL HL−STR
These factors capture the enhanced electromagnetic and ther- (cid:18) 15000 15000 (cid:19)
malstressescausedbyharmoniccomponents,andtheresulting F AA =exp 383 − θ +273 (9)
HS
total load loss under harmonic loading is expressed as:
Based on F , which quantifies the temperature-dependent
AA
rate of insulation degradation, the real-life expectancy of the
P LL =(P R +F HL ×P EC−R +F HL−STR ×P OSL−R ).I p 2 u (3) distribution transformer, Life real , can be assessed as follows:
wherethesuperscriptRindicatesrated-loadconditions,and Life
Life = norm (10)
I pu is defined as the ratio of the harmonic load current to the real F AA
rated load current.
whereLife denotesthenormalinsulationlife,expressed
norm
Theharmoniclossfactorforwindingeddy-currentlossesis
in years, at reference HST of 110°C.
given by:
h=
(cid:88)
hmax III. SYSTEMDESCRIPTIONANDMEASUREMENT-BASED
I h 2h2 HARMONICASSESSMENTFRAMEWORK
F = h=1 (4) A. Network and Transformer Description
HL
h=
(cid:88)
hmax
I2 The studied network is a three-phase LV residential distri-
h
bution system serving 150 single-phase customers through a
h=1
20/0.4 kV, 155 kVA liquid-immersed distribution transformer.
and the harmonic loss factor associated with other stray
The principal parameters of the transformer examined in this
losses is defined as:
study are summarized in Table I and follow the illustrative
h=
(cid:88)
hmax
examples provided in the reference standard [8]. Each con-
I2h0.8
h sumerisallocatedtoonephaseofthenetwork,andaperfectly
F = h=1 (5) balanced allocation of 50 single-phase residential consumers
HL−STR
h=
(cid:88)
hmax
to each transformer phase is assumed in the analysis. Each
I2
h load point includes residential nonlinear household appliances
h=1
979-8-3315-8138-1/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:20:18 UTC from IEEE Xplore. Restrictions apply.

TABLEI
TECHNICALPARAMETERSOFTHESTUDIEDDISTRIBUTIONTRANSFORMER
|     |     |     | Parameter           |     |     |         | Value Parameter                  |     |     |          | Value |     |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | ------- | -------------------------------- | --- | --- | -------- | ----- | --- | --- | --- | --- |
|     |     |     | HVwindingresistance |     |     | 18.207Ω | LVwindingresistance              |     |     | 0.02491Ω |       |     |     |     |     |
|     |     |     | Ratedpower          |     |     | 155kVA  | No-loadloss                      |     |     | 9.5kW    |       |     |     |     |     |
|     |     |     | Primaryvoltage      |     |     | 20kV    | Loadloss                         |     |     |          | 35kW  |     |     |     |     |
|     |     |     | Secondaryvoltage    |     |     | 400V    | AmbientTemperature               |     |     |          | 35◦C  |     |     |     |     |
|     |     |     | Powerfactor         |     |     |         | 0.95 Ratedtop-oiltemperaturerise |     |     |          | 55◦C  |     |     |     |     |
80◦C
|     |     |     | Normalinsulationlife |     |     | 30years | Ratedhottest-spottemperaturerise |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | ------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
equipped with EV charging infrastructure, reflecting modern than the maximum expected current in a scenario where
LV residential networks with a high penetration of power- all residential consumers are equipped with EV charging
electronic-based loads. infrastructure. To analyze the effect of transformer rating and
loadingconditionsonharmonic-inducedthermalagingandlife
| B. Characterization |     | of  | Harmonic | Injection |     | Profiles | Using |             |            |     |           |     |     |     |     |
| ------------------- | --- | --- | -------- | --------- | --- | -------- | ----- | ----------- | ---------- | --- | --------- | --- | --- | --- | --- |
|                     |     |     |          |           |     |          |       | expectancy, | four cases | are | examined: |     |     |     |     |
Field Measurements
|             |     |                |     |        |     |          |         | • Case | 1: 50 residential |     | loads | without | EVs. |     |     |
| ----------- | --- | -------------- | --- | ------ | --- | -------- | ------- | ------ | ----------------- | --- | ----- | ------- | ---- | --- | --- |
| To generate |     | representative |     | weekly | EV  | harmonic | current |        |                   |     |       |         |      |     |     |
• Case2:50residentialloads,allequippedwithEVcharg-
| profile, | field-measured |     | harmonic | current | waveforms |     | obtained |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | -------- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ing infrastructure.
| from 40 | charging | cycles | of  | 14 EVs, | representing |     | nine dif- |     |     |     |     |     |     |     |     |
| ------- | -------- | ------ | --- | ------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
• Case3:50residentialloads,allequippedwithEVcharg-
| ferent manufacturers |     | and | models, | are | employed, |     | as reported |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
inginfrastructure,suppliedbyatransformeroversizedby
| in detail | in [12], | [13]. | The | charging | start | time for | each EV |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | --- | -------- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
25%.
| has been | generated | using | statistical | distributions |     | derived | from |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ----------- | ------------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
• Case4:50residentialloads,allequippedwithEVcharg-
| real measurements |     | reported |     | in [14], | while | the corresponding |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | -------- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inginfrastructure,suppliedbyatransformeroversizedby
| charging | durations | are | sampled | from | the empirical |     | distribu- |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------- | ---- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
55%.
| tions observed |            | during | the same | field | measurement |            | campaign. |     |                             |     |     |     |     |     |     |
| -------------- | ---------- | ------ | -------- | ----- | ----------- | ---------- | --------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
| A temporal     | resolution |        | of 1-min | is    | assumed     | throughout | the       |     |                             |     |     |     |     |     |     |
|                |            |        |          |       |             |            |           | IV. | EFFECTOFTRANSFORMERRATINGON |     |     |     |     |     |     |
analysis.
HARMONIC-INDUCEDAGINGANDLIFEEXPECTANCY
| In addition |     | to EV | charging, | residential |     | harmonic | current |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | --------- | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
injectionsareincorporatedattheloadpoints.Forthispurpose,
|               |           |              |           |                |          |                  |         | A. Steady-State   | Thermal        | and  | Aging    | Assessment         |     |             |      |
| ------------- | --------- | ------------ | --------- | -------------- | -------- | ---------------- | ------- | ----------------- | -------------- | ---- | -------- | ------------------ | --- | ----------- | ---- |
| one-week      | harmonic  | injection    |           | profiles       | from     | 25 individual    | res-    |                   |                |      |          |                    |     |             |      |
|               |           |              |           |                |          |                  |         | To perform        | a steady-state |      |          | assessment         | of  | transformer |      |
| idential      | customers | are          | included, | based          | on       | real measurement |         |                   |                |      |          |                    |     |             |      |
|               |           |              |           |                |          |                  |         | harmonic-induced  | thermal        |      | and      | aging performance, |     | weekly      |      |
| data obtained | from      | the          | MEMORIA   | public         | database |                  | [15].   |                   |                |      |          |                    |     |             |      |
|               |           |              |           |                |          |                  |         | average magnitude | of             | each | harmonic | component          |     | is used     | as a |
| To accurately |           | characterize |           | the cumulative |          | harmonic         | distor- |                   |                |      |          |                    |     |             |      |
tionimposedontheLVdistributiontransformer,theharmonic representative value. The transformer loading level, expressed
|              |               |             |             |            |          |             |          | as the percentage  | of          | rated | load, is    | required | because     | the        | total |
| ------------ | ------------- | ----------- | ----------- | ---------- | -------- | ----------- | -------- | ------------------ | ----------- | ----- | ----------- | -------- | ----------- | ---------- | ----- |
| current      | contributions | from        | residential |            | loads    | and EV      | charging |                    |             |       |             |          |             |            |       |
|              |               |             |             |            |          |             |          | losses must        | be adjusted | to    | account     | for both | the reduced |            | RMS   |
| are combined | using         | vector      | addition    | (phasor    |          | summation), | con-     |                    |             |       |             |          |             |            |       |
|              |               |             |             |            |          |             |          | current (operating | below       | rated | conditions) |          | and the     | additional |       |
| sidering     | harmonic      | phase-angle |             | diversity, | harmonic |             | superpo- |                    |             |       |             |          |             |            |       |
contributionarisingfromharmonicdistortion.Thedetermined
| sition and | cancellation |     | effects | in the | aggregated |     | transformer |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------- | ------ | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
current. The most prominent harmonic current components harmonic spectra correspond to loading levels of 40%, 87%,
|          |        |              |     |               |        |       |          | 72%, and    | 58% for Cases   | 1    | through    | Case      | 4, respectively. |            |     |
| -------- | ------ | ------------ | --- | ------------- | ------ | ----- | -------- | ----------- | --------------- | ---- | ---------- | --------- | ---------------- | ---------- | --- |
| observed | in the | conducted    |     | measurements, |        | up to | the 13th |             |                 |      |            |           |                  |            |     |
|          |        |              |     |               |        |       |          | The results | of steady-state |      | assessment |           | are summarized   |            | in  |
| harmonic | order, | are analyzed |     | in this       | study. |       |          |             |                 |      |            |           |                  |            |     |
|          |        |              |     |               |        |       |          | Table II.   | Across the      | four | cases      | analyzed, | Case             | 1 exhibits |     |
C. CaseStudyDefinitionsandTransformerLoadingScenarios the higher harmonic loss factors than Cases 2–4. When EV
The long-term challenge in LV residential networks is charging is introduced (Cases 2–4), their associated harmonic
thatexistinginstalleddistributiontransformerswereoriginally components—present only during relatively short charging
sized and designed for operating conditions fundamentally intervals—contribute limitedly to the weekly mean harmonic
differentfromthoseexpectedunderfuturedemandprofiles.As spectrum, whereas EV penetration leads to a pronounced
a result, assessing their performance under emerging loading increase in the weekly-average fundamental current. As a
patterns(increasedharmonicdistortionandthermalstress)has result, despite higher absolute harmonic loading in Cases
become essential. 2–4, the harmonic loss factors—which are normalized by
In this study, a distribution transformer with relatively the fundamental current—decrease. Fig. 1 illustrates the time
limited capacity has been intentionally selected to evaluate evolutionofthefundamental,third,andfifthharmoniccurrent
its behavior under extreme harmonic and loading conditions. components over the representative one-week period for the
This choice enables the transformer to operate near its rated definedloadingcases,highlightingthatthepronouncedchange
limits,enablingamorerealisticandcriticalassessment.Given from Case 1 to Cases 2–4 is the increase in the fundamental
theratedsecondaryvoltage,thecorrespondingratedsecondary current relative to higher-order harmonics. So, under the
current is approximately 224 A, which is only slightly higher considered loading cases, the contribution of increased fun-
979-8-3315-8138-1/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:20:18 UTC from IEEE Xplore.  Restrictions apply.

damental current is more significant than enhanced harmonic
content in determining transformer thermal stress.
As summarized in Table II, the transformer’s thermal and
aging stress peaks in Case 2, reflecting the combined effect
of increased RMS loading and frequency-dependent stray-
losses associated with harmonic currents. In contrast, Case
3 and Case 4, which employ oversized transformers under
identical harmonic content relative to Case 2, show reduced
θ , θ , θ and F compared to Case 2. This confirms
TO g HS AA
thattransformeroversizingisarobustandeffectivemitigation
strategy for reducing harmonic-induced thermal rise under
the increasing power-electronic-based loads. Moreover, F
AA
remains below 1 in all cases, suggesting no accelerated LOL
under the weekly-average harmonic spectrum.
   
   
  $    ,
  
  
  
  $    ,
  
  
 
 0 R Q   7 X H   : H G   7 K X   ) U L   6 D W   6 X Q 
  $    ,
a closely clustered HST distribution with limited dispersion,
indicatingthermallystableperformance.Incontrast,theintro-
duction of extensive EV charging without transformer over-
sizing (Case 2) result in a pronounced upward shift in both
the median and upper tail of the HST distribution, reaching
up to approximately 240°C and exceeding its 110°C design
threshold. This behavior confirms that harmonic-enhanced
losses significantly intensify thermal stress during clustered
charging periods, even when average indices remain within
acceptablethreshold.Progressivetransformeroversizing(Case
3 and Case 4) shifts the HST distribution downward and
mitigates high-impact extreme hot-spot events, which are the
primary contributors to accelerated insulation aging and LOL
in EV-dense LV networks.
Fig. 4 presents the weekly distribution of the F for
AA
the evaluated loading cases. Case 1 exhibits low insulation
 & D V H    & D V H V   B 
aging despite comparatively higher harmonic loss factors.
Case 2, reflecting the combined impact of increased RMS
current and frequency-dependent stray losses, shows extreme
upper outliers in the F boxplot, indicating that transformer
AA
insulation aging is affected by rare but severe thermal ex-
tremes.Transformeroversizing(Case3andCase4)effectively
mitigates outliers, thereby limiting peak insulation stress and
stabilizing the temporal aging profile despite unchanged har-
monic injection compared to Case 2.
Overall, the results indicate that temporally clustered EV
charging sessions raise RMS loading and harmonic-induced
stray losses and lead to short-duration thermal extremes that
arenotreflectedinweekly-averageindices.So,strategictrans-
former sizing—combined with ongoing harmonic monitoring
and targeted mitigation—can substantially reduce extreme
Fig.1. Timeevolutionofthefundamental,third,andfifthharmoniccurrent HST outliers and preserve expected transformer lifetime un-
componentsfordefinedloadingcases. derincreasinglynonlinear,power-electronics-basedresidential
loads.
B. Dynamic Thermal and Aging Assessment
EVchargingsessionswithconsiderabletemporalvariability
introduce time clustering and phase-angle-dependent aggrega-
tion and cancellation of harmonics, which can result in short-  
durationthermalextremesthatarenotrepresentedbyweekly-
mean spectra; therefore, a dynamic assessment of transformer  
thermal and aging behavior is necessary.
 
Fig. 2 represents the statistical distribution of harmonic
loss factors over the analyzed week for the four loading
 
scenarios.Case1exhibitsabroaderdistributionandincreased                        
F
HL
harmonic loss factor values than Cases 2–4, indicating a
comparatively stronger contribution of higher-order harmonic
currents relative to the fundamental component in the aggre-
gated transformer current. Significantly, Fig. 2 demonstrates
that transformer oversizing (Cases 3 and 4) does not alter the
harmonic loss factors distributions (Case 2), confirming that
these factors are governed by the harmonic spectrum of the
connected loads rather than by the transformer rated capacity.
Fig. 3 represents boxplots of the transformer HST for the
defined Cases over a representative one-week period with 1-
minute resolution. As shown in this figure, Case 1 shows
 \ W L V Q H G  \ W L O L E D E R U 3
  
  
 
                             
F
HL STR
 \ W L V Q H G  \ W L O L E D E R U 3
 & D V H   & D V H   
Fig.2. Histogramofharmoniclossfactorsfordefinedloadingcases.
979-8-3315-8138-1/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:20:18 UTC from IEEE Xplore. Restrictions apply.

TABLEII
SUMMARYOFSTEADY-STATETRANSFORMERHARMONIC-INDUCEDTHERMALANDAGINGPERFORMANCE
|     |     |     |     | Parameter |      | Case1  | Case2  | Case3  |     | Case4  |     |     |     |     |     |
| --- | --- | --- | --- | --------- | ---- | ------ | ------ | ------ | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | FHL       |      | 1.5758 | 1.1361 | 1.1361 |     | 1.1361 |     |     |     |     |     |
|     |     |     |     | FHL−STR   |      | 1.0695 | 1.0169 | 1.0169 |     | 1.0169 |     |     |     |     |     |
|     |     |     |     | θ         | (◦C) | 25.26  | 48.37  | 38.96  |     | 31.39  |     |     |     |     |     |
TO
|     |     |     |     | θg       | (◦C)    | 8.28   | 21.99  | 16.12  |     | 11.29  |     |     |     |     |     |
| --- | --- | --- | --- | -------- | ------- | ------ | ------ | ------ | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | θ        | HS (◦C) | 68.55  | 105.36 | 90.08  |     | 77.68  |     |     |     |     |     |
|     |     |     |     | FAA      |         | 0.0086 | 0.6185 | 0.1167 |     | 0.0271 |     |     |     |     |     |
|     |     |     |     | Lifereal | (year)  | 30     | 30     |        | 30  | 30     |     |     |     |     |     |
ACKNOWLEDGMENT
|     |     |     |     |     |     |     |     | This work | was | supported |     | by the | Ministerio | de  | Ciencia e |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --- | ------ | ---------- | --- | --------- |
 5 H I H U H Q F H  + 6 7          & Innovacio´n(MCIN)laAgenciaEstataldeInvestigacio´n(AEI)
  &    7 6 +
   
|     |     |     |     |     |     |     | por | el FEDER |     | under Project |     | PID2022-141609OB-I00. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | --------------------- | --- | --- | --- |
REFERENCES
   
|     |            |     |            |            |     |            | [1] | X. Xie, | F. Peng,      | and | Y. Zhang, | “A data-driven |         | probabilistic | harmonic   |
| --- | ---------- | --- | ---------- | ---------- | --- | ---------- | --- | ------- | ------------- | --- | --------- | -------------- | ------- | ------------- | ---------- |
|     |            |     |            |            |     |            |     | power   | flow approach |     | in power  | distribution   | systems | with          | PV genera- |
|     |  & D V H  |     |  & D V H  |  & D V H  |     |  & D V H  |     |         |               |     |           |                |         |               |            |
tions,”AppliedEnergy,vol.321,p.119331,2022.
[2] P.Rodr´ıguezPajaro´n,A.Herna´ndez,andJ.V.Milanovic,“Probabilistic
Fig.3. BoxplotofHSTfordefinedloadingcases.
|     |     |     |     |     |     |     |     | assessment | of  | the impact | of  | electric | vehicles | and nonlinear | loads on |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | -------- | -------- | ------------- | -------- |
powerqualityinresidentialnetworks,”Int.J.Elect.PowerEnergySyst.,
vol.129,pp.1–11,2021.
|     |     |     |     |     |     |     | [3] | F. Mahmoudnezhad, |             |              | A. Herna´ndez, | P.            | Rodr´ıguez, | A.  | Contreras, and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | ------------ | -------------- | ------------- | ----------- | --- | -------------- |
|     |     |     |     |     |     |     |     | J. V.             | Milanovic´, | “Data-driven |                | probabilistic | modeling    | of  | EV harmonic    |
     
AAF emissionsbasedonfieldmeasurements,”IEEETrans.PowerDel.,2025.
|     |     |     |     |     |     |     | [4] | Y. Wang, | X.  | Wang, S. | Li, X. | Ma, Y. | Chen, and | S. Liu, | “Optimization |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------ | ------ | --------- | ------- | ------------- |
modelforharmonicmitigationbasedonPV-ESScollaborationinsmall
distributionsystems,”AppliedEnergy,vol.356,p.122410,2024.
 
[5] X.XieandD.Chen,“Data-drivendynamicharmonicmodelformodern
|     |  & D V H  |     |  & D V H  |  & D V H  |     |  & D V H  |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
householdappliances,”AppliedEnergy,vol.312,p.118759,2022.
Fig.4. Boxplotofagingaccelerationfactorfordefinedloadingcases. [6] M.C.Costa,M.Z.Fortes,G.G.Sotelo,andB.W.Franc¸a,“Thermal
effectsduetoharmonicsondry-typetransformers:Impactoffiltersand
phaseangles,”Measurement:Energy,vol.6,p.100045,2025.
|     |     |     |            |     |     |     | [7] | J. A.       | Badri, | J.-R. R. | Riba, A.   | Garcia,  | S. Trujillo, | and   | A. Marza`bal,  |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ----------- | ------ | -------- | ---------- | -------- | ------------ | ----- | -------------- |
|     |     | V.  | CONCLUSION |     |     |     |     |             |        |          |            |          |              |       |                |
|     |     |     |            |     |     |     |     | “Predicting | the    | effect   | of voltage | harmonic | phase        | angle | on transformer |
corelosses,”IEEETransactionsonInstrumentationandMeasurement,
| This work | provides | a   | field measurement–based |     |     | assessment |     | 2024. |     |     |     |     |     |     |     |
| --------- | -------- | --- | ----------------------- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ofharmonicdistortionimpactsonLVdistributiontransformers [8] IEEEStdC57.110-2018,“IEEERecommendedPracticeforEstablishing
underincreasingpenetrationofresidentialnonlinearloadsand Liquid-Immersed and Dry-Type Power and Distribution Transformer
|     |     |     |     |     |     |     |     | Capability | When | Supplying | Non-Sinusoidal |     | Load | Currents,” | IEEE Std |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------- | -------------- | --- | ---- | ---------- | -------- |
EVs. Realistic harmonic injection profiles aligned with the C57.110™-2018(RevisionofIEEEStdC57.110-2008),2018.
IEEE C57.110 thermal-aging framework, demonstrates that [9] IEEE Standard C57.12.00—2010, “IEEE Standard for General Re-
|         |             |               |     |         |             |         |     | quirements | for | Liquid-Immersed |     | Distribution, |     | Power, | and Regulating |
| ------- | ----------- | ------------- | --- | ------- | ----------- | ------- | --- | ---------- | --- | --------------- | --- | ------------- | --- | ------ | -------------- |
| high EV | penetration | significantly |     | impacts | transformer | thermal |     |            |     |                 |     |               |     |        |                |
Transformers,”2010.
| and aging | through | the | combined | effect | of increased | RMS |      |      |                     |     |     |                |     |           |              |
| --------- | ------- | --- | -------- | ------ | ------------ | --- | ---- | ---- | ------------------- | --- | --- | -------------- | --- | --------- | ------------ |
|           |         |     |          |        |              |     | [10] | IEEE | Std C57.18.10—2008, |     |     | “IEEE Standard |     | Practices | and Require- |
loadingandfrequency-dependentstraylossespronounceddur- mentsforSemiconductorPowerRectifierTransformers,”2008.
[11] M.A.Taghikhani,“OilimmerseddistributiontransformerHSTreduc-
| ing temporally |     | clustered | charging | sessions. | While | weekly- |     |            |           |      |     |                |     |         |                |
| -------------- | --- | --------- | -------- | --------- | ----- | ------- | --- | ---------- | --------- | ---- | --- | -------------- | --- | ------- | -------------- |
|                |     |           |          |           |       |         |     | tion using | vegetable | oils | and | ONAN cooling,” |     | Journal | of Applied and |
averageharmonicindicesmayremainwithinacceptablelimits,
|     |     |     |     |     |     |     |     | Computational |     | Mechanics, | vol. | 10, no. | 1, pp. | 13–25, | 2024, Shahid |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ---- | ------- | ------ | ------ | ------------ |
dynamic analysis reveals short-duration thermal extremes that ChamranUniversityofAhvaz.
|                    |     |          |            |          |            |             | [12] | “Electric | Vehicle     |     | Measurements |     | dAta  | on Harmonics | and        |
| ------------------ | --- | -------- | ---------- | -------- | ---------- | ----------- | ---- | --------- | ----------- | --- | ------------ | --- | ----- | ------------ | ---------- |
| exceed transformer |     | design   | thresholds | and      | contribute | to insu-    |      |           |             |     |              |     |       |              |            |
|                    |     |          |            |          |            |             |      | Power     | (EV-MAHP),” |     | Zenodo,      |     | 2025. | [Online].    | Available: |
| lation aging.      | The | analysis | further    | confirms | that       | transformer |      |           |             |     |              |     |       |              |            |
https://doi.org/10.5281/zenodo.15556192
oversizing does not alter the harmonic spectrum injected by [13] F. Mahmoudnezhad, A. Contreras, A. Herna´ndez Bayo, and
connectedloads,butitsubstantiallymitigatesextremethermal P.Rodr´ıguez-Pajaro´n,“Interactionbetweenharmoniccurrentinjections
|     |     |     |     |     |     |     |     | from | residential | loads | and electric | vehicles | in  | low voltage | networks,” |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ----- | ------------ | -------- | --- | ----------- | ---------- |
events and aging outliers. in Proc. 14th Mediterranean Conf. Power Gener. Transmission,
The findings emphasize the need for utilities to revise Distribution and Energy Conversion (MEDPOWER 2024), 2024,
traditional transformer sizing practices to explicitly account pp.597–601,IET.
|     |     |     |     |     |     |     | [14] | J. Quiro´s-Torto´s, |     | A.  | Navarro-Espinosa, |     | L. F. | Ochoa, | and T. Butler, |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | --- | ----------------- | --- | ----- | ------ | -------------- |
for nonlinear load dynamics, harmonic phase-angle diversity, “Statistical representation of EV charging: Real data analysis and
and the temporal clustering of EV charging. The study also applications,”inProc.PowerSyst.Comput.Conf.(PSCC),2018,pp.1–
7.
| highlights | the importance |     | of continuous |     | harmonic | monitoring |      |               |     |          |        |          |               |     |                |
| ---------- | -------------- | --- | ------------- | --- | -------- | ---------- | ---- | ------------- | --- | -------- | ------ | -------- | ------------- | --- | -------------- |
|            |                |     |               |     |          |            | [15] | P. Rodr´ıguez |     | Pajaro´n | and A. | H. Bayo, | “Measurements |     | of residential |
anddynamicthermalassessmenttoensurereliabletransformer injections of harmonics – MEMORIA,” e-cienciaDatos, vol. 3, 2021.
performance and preserve asset lifetime as EV adoption ac- [Online].Available:https://doi.org/10.21950/JOW63G
celerates.
979-8-3315-8138-1/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 14:20:18 UTC from IEEE Xplore.  Restrictions apply.