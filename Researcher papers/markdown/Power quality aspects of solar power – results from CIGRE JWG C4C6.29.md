24thInternationalConference &Exhibition onElectricity Distribution (CIRED)
12-15June 2017
Session2:Powerqualityandelectromagneticcompatibility
–
Power quality aspects of solar power
results from CIGRE JWG C4/C6.29
ISSN2515-0855
✉ doi:10.1049/oap-cired.2017.0351
Jeff Smith1, Sarah Rönnberg2, Math Bollen2 , Jan Meyer3, www.ietdl.org
AnaMaria Blanco3, Kah-Leong Koo4, Daudi Mushamalirwa5
1DistributionPlanning,OperationsandStudies,EPRI,Knoxville,USA
2ElectricPowerEngineering,LuleåUniversityofTechnology,Skellefteå,Sweden
3TUDresden,InstituteofElectricalPowerSystemsandHighVoltageEngineering,Dresden,Germany
4NationalGrid,PowerQualityandModelling,SystemDesign,Warwick,UK
5GEGridSolutions,TechnicalInstitute–NetworkConsulting,Paris,France
✉E-mail:math.bollen@ltu.se
Abstract: The increasing use of solar power connected to the public grid and the associated concern for deteriorating
power quality triggered the formation of a joint working group with the aim to describe and quantify this impact. The
WG formed in 2012 as a joint C4/C6 effort, formed to examine the power quality aspects of solar power, specifically
addressinga numberof phenomena, allwhichwill bediscussedin thisstudy.
1 Introduction Magnitude and phase angle of the harmonic currents depend on
many factors, like supply voltage distortion, output power and
There has recently been a massive increase in the amount of harmonic network impedance. In most cases, highest harmonic
photovoltaic (PV) installations connected to the grid, and this trend currents (in absolute value) are observed at 100% output power.
is expected to continue during the coming years. Not only are the Consequently, neither general models, nor simplified constant
numbers of PV installations increasing but also the sizes of the current source approaches are sufficient for realistic simulation
installations.PVinstallationscanbefromafewkWtotensofMW. studies. This issue is also addressed by the CIGRE/CIRED
With large numbers of PV plants under construction and being working group C4/B4.38 on network modelling for harmonic
planned in many countries, their impact on power quality in the studies.
network is becoming of concern to grid operators. The following Harmonicmagnitudesandphaseanglesareimportantforrealistic
power-qualitydisturbanceshavebeencoveredbythisworkinggroup: studiesofcancellationeffectsbetweenPVinverters/PVinstallations
andotherinstallations.IflargerPVplantsarebuiltusingmultiplePV
† characteristic harmonics as well as low-order non-characteristic inverters of the same model, the harmonic currents of individual
harmonics; inverters can add up almost arithmetically [1], even at higher
† supraharmonics(anytypeofwaveformdistortionofvoltageand harmonic orders. The standard summation exponents (e.g.
currentbetween2and150kHz); accordingtoIEC61000-3-6)arenotsuitableinsuchcases.
† fastvoltagevariations(timeintervaloflessthan10min)induced PVinvertersimpactharmonicnetworkimpedance.Particularlyin
byvariationsinpowerproduction; larger PV installations the grid-side filter circuits can cause
† slow voltage variations (time interval of 10min and longer) significant resonances at low frequencies. The resonant frequency
inducedbyvariationsinproduction; decreaseswithincreasingnumberofinverters.Consequently,input
† overvoltagesinducedbyPVpowerproduction; impedances of PV inverters should be considered in harmonic
† flickerperformancefromvariousPVinstallations; studies.
† voltageunbalanceduetosingle-phaseconnectedPVinstallations; Under specific circumstances, PV inverters can get unstable and
† sudden disconnection and reconnection of PV, particularly trip. This has been observed along with high-voltage distortion
transient overvoltages, temporary overvoltage, steady-state due to network resonances, which are usually accompanied by
overvoltageandinrushcurrents. highsourceimpedances.
Theanalysisofnetworkmeasurementshasshownthatparticular
harmonic voltages at orders higher than 25 can be significantly
2 Harmonics
attenuated by the distribution transformers. In case of distributed
PV inverters in low-voltage (LV) networks, the impact on the
PVinverters,whichareavailableonthemarkettoday,utilisepower harmonic voltage in the network (decrease, increase or no impact)
electronicsbasedonself-commutatingtechniquesathighswitching is usuallynot consistent anddiffers betweenharmonic orders.It is
frequencies(supraharmonics).Consequently,theharmonicemission determined by the existing potential of cancellation with other
at frequencies below 2kHz is usually low compared to other equipmentandapossible filtereffectofthegrid-side circuitofthe
equipment using line-commutating circuit topologies. However, PVinverters.
measurements have shown that harmonic emission is still a
significantissueforindividualinvertersandPVinstallations.
2.2 Recommendations
2.1 Findings
Forrealisticharmonicstudiesthedependencyofharmoniccurrents
The harmonic current characteristic of individual PV inverters (all of PV inverters on supply voltage distortion and network
withapowerratingbelow10kW)variesbetweendifferentmodels impedance as well as the input impedance characteristic, which
andmanufacturersascanbeseeninFig.1. cancauseresonancesinthenetworks,hastobeconsidered.
CIRED,OpenAccessProc.J.,2017,Vol.2017,Iss.1,pp.809–813
ThisisanopenaccessarticlepublishedbytheIETundertheCreativeCommons 809
AttributionLicense(http://creativecommons.org/licenses/by/3.0/)

|     |     |     |     |     |     |     |     | residues from | the | switching | and are | present | as  | long as | the PV is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------- | ------- | --- | ------- | --------- |
producingpower.
|     |     |     |     |     |     |     |     | From a      | large number  | of        | measurements |          | done mainly |              | in Sweden   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --------- | ------------ | -------- | ----------- | ------------ | ----------- |
|     |     |     |     |     |     |     |     | and Germany | it is         | seen that | the          | emission | from        | single-phase | PV          |
|     |     |     |     |     |     |     |     | inverters   | (installed    | power     | below        | 4.6kW)   | occurs      | at           | frequencies |
|     |     |     |     |     |     |     |     | between     | 15 and 20kHz. | For       | three-phase  |          | inverters   | used         | for high    |
|     |     |     |     |     |     |     |     | power units | the switching |           | often takes  | place    | at a        | lower        | frequency   |
|     |     |     |     |     |     |     |     | starting at | around        | 2kHz [2,  | 3]. More     | recently | smaller     |              | three-phase |
invertersstartedtoappearatthemarketwithswitchingfrequencies
around20kHz.
Fig.1 CurrentharmonicmagnitudesofsixdifferentPVinvertersoperating
atratedpowerundersinusoidalgridvoltage
3.1 Findings
|     |     |     |     |     |     |     |     | PV inverters | are a | source of | supraharmonics. |     | Measurements |     | show |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --------- | --------------- | --- | ------------ | --- | ---- |
IncaseofcentrallylocatedPVinverters(e.g.inlargePVplants),
|                 |         |                |           |             |                |              |            | that the emissions |                 | can be found | at              | frequencies | up        | to 20kHz. | The       |
| --------------- | ------- | -------------- | --------- | ----------- | -------------- | ------------ | ---------- | ------------------ | --------------- | ------------ | --------------- | ----------- | --------- | --------- | --------- |
| particularly    | in case | of             | similar   | inverter    | models,        | harmonic     | currents   |                    |                 |              |                 |             |           |           |           |
|                 |         |                |           |             |                |              |            | emission           | from PV         | inverters    | (as             | well as     | for other | low       | voltage   |
| should be       | added   | arithmetically |           | independent | of             | the harmonic | order.     |                    |                 |              |                 |             |           |           |           |
|                 |         |                |           |             |                |              |            | devices) is        | greatlyaffected |              | by neighbouring |             | devices;  | this      | has been  |
| For distributed |         | PV             | inverters | (e.g.       | in residential |              | areas) the |                    |                 |              |                 |             |           |           |           |
|                 |         |                |           |             |                |              |            | shown for          | inverters       | connected    | at the          | LV          | network   | in the    | following |
aggregationwithresidentialequipmentshouldbetakenintoaccount.
ways:
ParticularlyincaseofahighshareofPVinvertersinanetworkor
| incaseoflargePVplantstheriskofhighharmonicvoltagesdueto |     |     |     |     |     |     |     | †            |     |              |               |     |     |         |           |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | ------------- | --- | --- | ------- | --------- |
|                                                         |     |     |     |     |     |     |     | The presence | of  | neighbouring | supraharmonic |     |     | sources | can cause |
instabilitieswithmultiplecontrollersshouldbeconsidered.
secondaryemissionatthePVinverter.
| Standardisationtestingconditionsandemissionlimits,especially |     |     |     |     |     |     |     | †       |           |           |     |     |     |            |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | --- | --- | --- | ---------- | --- |
|                                                              |     |     |     |     |     |     |     | Changes | in source | impedance |     | due | to  | connection | and |
forthesmall-sizedPVinvertersformass-marketapplications,should
|     |     |     |     |     |     |     |     | disconnection | of neighbouring |     | devices |     | will impact | the | primary |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | --- | ------- | --- | ----------- | --- | ------- |
berevised.Setupsusingonlysinusoidaltestvoltageandnoreference
impedance(likeinIEC61000-3-2)donotreflecttherealbehaviour emissionfromaPVinverter.
†
|                 |     |        |         |        |              |     |               | Voltage | harmonics | (3rd, | 5th | and 7th) | have | shown | strong |
| --------------- | --- | ------ | ------- | ------ | ------------ | --- | ------------- | ------- | --------- | ----- | --- | -------- | ---- | ----- | ------ |
| of the inverter |     | in the | network | and do | not consider |     | the different |         |           |       |     |          |      |       |        |
correlationswiththesupra-harmonicemissionfromaPVinverter.
| sensitivities | of  | the PV | inverters | to supply | voltage | distortion | or  |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | --------- | --------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networkimpedanceatall.Eventhespecificationofadefinedinput
| impedance | characteristic |     | of PV | inverters | for | certain | frequency |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ----- | --------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
3.2 Recommendations
| ranges could | be  | considered | for | future | revisions | of the | respective |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------ | --------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
standards.
MeasurementsofPVinvertersorPVplantsinlaboratoryorfield More efforts from network operators as well as from the research
|     |     |     |     |     |     |     |     | community | should | be put | towards | harmonic | studies | covering | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------ | ------- | -------- | ------- | -------- | --- |
shouldincludeharmonicmagnitudesandphaseangles.Knowledge
aboutcomplexharmoniccurrentscansignificantlyimprovestudies whole frequency range up to 150kHz. Small installations at LV
|     |     |     |     |     |     |     |     | (i.e.rooftop | installations)andlarger |     |     | installations |     | at highervoltage |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------------- | --- | --- | ------------- | --- | ---------------- | --- |
ofcancellationeffectsortheseparationbetweencustomer-sideand
|     |     |     |     |     |     |     |     | levels (i.e. | solar plants) | need | to be | treated | differently | with | regards |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ---- | ----- | ------- | ----------- | ---- | ------- |
network-sidecontributionstotheharmonicemissionlevels.
|     |     |     |     |     |     |     |     | to supra-harmonic |      | interaction. | Solar | plants      | are often | connected | to      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- | ------------ | ----- | ----------- | --------- | --------- | ------- |
|     |     |     |     |     |     |     |     | medium-voltage    | (MV) | with         | few   | other loads | connected |           | and any |
2.3 Open issues interaction will likely take place within the plant between
|     |     |     |     |     |     |     |     | inverters. | Roof top | installations | are | connected | at  | the customer | side |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------- | --- | --------- | --- | ------------ | ---- |
More comprehensive knowledge about the harmonic current of the meter and therewith close to other LV devices. Possible
characteristic of medium-sized and large-sized PV inverters is interaction between the inverter and other devices is hence more
needed, particularly in order to improve the accuracy of respective likelytooccurforsmallinstallations.
harmonicstudies.
manufacturer-specific
| Suitable,  |           |             |           | harmonic  | models       | capable       | to be      |          |           |        |                |     |         |         |     |
| ---------- | --------- | ----------- | --------- | --------- | ------------ | ------------- | ---------- | -------- | --------- | ------ | -------------- | --- | ------- | ------- | --- |
|            |           |             |           |           |              |               |            | 3.3 Open | issues    |        |                |     |         |         |     |
| used for   | studies   | of harmonic |           | emission, | harmonic     | instabilities | or         |          |           |        |                |     |         |         |     |
| harmonic   | resonance |             | are still | missing.  | This         | includes      | also       |          |           |        |                |     |         |         |     |
|            |           |             |           |           |              |               |            | The lack | of a good | method | to distinguish |     | between | primary | and |
| aggregated | harmonic  | models,     |           | e.g. for  | representing |               | a PV plant |          |           |        |                |     |         |         |     |
secondaryemission[4]isaseriousbarrierwhenstudyingemission
| consisting     | of multiple |     | PV inverters. |     | Measurement-based |          | models   |         |               |     |       |        |       |     |            |
| -------------- | ----------- | --- | ------------- | --- | ----------------- | -------- | -------- | ------- | ------------- | --- | ----- | ------ | ----- | --- | ---------- |
|                |             |     |               |     |                   |          |          | from PV | installations | and | other | modern | types | of  | devices or |
| are a possible | approach    |     | to improve    | the | model             | accuracy | compared |         |               |     |       |        |       |     |            |
installations.
| to the simple     | models      | based   | on            | constant | current   | sources. | However,    |               |           |        |      |              |         |                |           |
| ----------------- | ----------- | ------- | ------------- | -------- | --------- | -------- | ----------- | ------------- | --------- | ------ | ---- | ------------ | ------- | -------------- | --------- |
|                   |             |         |               |          |           |          |             | It is unclear | if the    | impact | from | neighbouring | devices |                | shown for |
| the superposition |             | of      | the different | impact   | factors,  |          | like supply |               |           |        |      |              |         |                |           |
|                   |             |         |               |          |           |          |             | PV inverters  | connected | at the | LV   | network      | will be | the samewithin |           |
| voltage           | distortion, | network | impedance,    |          | magnitude |          | of supply   |               |           |        |      |              |         |                |           |
largesolarplants.
voltageandoutputpowerofthePVinverterisstillnotvalidated.
| Comprehensive |        | knowledge |         | about the  | possible | impact       | of PV |     |     |     |     |     |     |     |     |
| ------------- | ------ | --------- | ------- | ---------- | -------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| inverters     | on the | harmonic  | network | impedance, |          | particularly | their |     |     |     |     |     |     |     |     |
contribution to harmonic resonances in public LV grids, is still 4 Fast voltage variations
lacking.
General conclusions about the impact of PV power on the Thissectionwilladdressfastvoltagevariations,whicharevariations
harmonic levels are not known and might even not be possible. It in the rms voltage with a duration of less than 10min. The
strongly depends on the size of PV installation, harmonic connectionofPVinstallationsonadistributionnetworkwillresult
impedance at the connection point and the inverter models. A in a voltage rise at the generator terminals. The change in voltage
significant
increase of harmonic levels on a large scale has not magnitude is determined by the active and reactive power
beenobserved. injections as well as the equivalent short-circuit impedance at the
|     |     |     |     |     |     |     |     | terminals | of the PV | installation. | A   | number | of factors | contribute | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------- | --- | ------ | ---------- | ---------- | --- |
thevariabilityofPVpowerproduction,including:
3 Supraharmonics
† sizeandlayoutofPVplant,
Theterm‘supraharmonics’isusedtorefertoanytypeofwaveform † cloudenhancement,
distortion of voltage and current in the frequency range between 2 † fixed-axisversustrackingsystems,
and 150kHz. Supraharmonics related to PV inverters consists of † climatecharacteristics.
CIRED,OpenAccessProc.J.,2017,Vol.2017,Iss.1,pp.809–813
810 ThisisanopenaccessarticlepublishedbytheIETundertheCreativeCommons
AttributionLicense(http://creativecommons.org/licenses/by/3.0/)

Moreover,nexttothis,fastvoltagevariationscanalsobedueto locations with and without solar power, as well as the analysis of
| variationsinreactivepower. |     |     |     |     |     |     |     | historicaldata. |        |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | --- | --- | --- | --- | --- | --- |
|                            |     |     |     |     |     |     |     | 5.3 Open        | issues |     |     |     |     |     |     |
4.1 Findings
Geographic size and layout have the greatest impact on output Thenetimpactofsolarandloadcoincidenceornon-coincidenceon
variabilityfromaPVinstallation.Thelargerinstallations(interms voltageregulationequipmentisnotunderstoodinaquantitativeway
| of capacity | and | geographic | footprint) |     | exhibit | slower | ramping | yet. |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | ---------- | --- | ------- | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
comparedtotheirsmaller-sizedcounterparts.
| Relating | the PV | installation |     | ramping | characteristics |     | to voltage |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | ------- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
fluctuations is dependent on the grid-connection point and the 6 Overvoltage
| associated | grid | impedance | (especially |     | the | resistance). | Simple |     |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | ----------- | --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
calculationmethodsfordeterminingimpactofPVinstallationsata The connection of a PV installation (or any type of distributed
single point of connection are provided in the WG brochure [5]. generation) to the distribution network will result in a voltage rise
DistributedPVinstallationsacrossanetworkrequiremoredetailed at the terminals of the generator and elsewhere in the distribution
networkmodelling. grid. The voltage when the PV produces power is higher than
whenthePVdoesnotproducepower.
4.2 Recommendations
6.1 Findings
WhenexaminingvoltageimpactsduetooutputvariabilityofaPV
|               |           |             |             |          |           |             |             | The presence | of              | PV installations |                  | in distribution    |           | networks      | will   |
| ------------- | --------- | ----------- | ----------- | -------- | --------- | ----------- | ----------- | ------------ | --------------- | ---------------- | ---------------- | ------------------ | --------- | ------------- | ------ |
| installation, | realistic | variation   | data        | with     | respect   | to the      | size of the |              |                 |                  |                  |                    |           |               |        |
|               |           |             |             |          |           |             |             | increase     | the probability |                  | of overvoltages. |                    | The       | setting       | of the |
| installation  | has       | to be used. | For         | example, | utilising | measurement |             |              |                 |                  |                  |                    |           |               |        |
|               |           |             |             |          |           |             |             | overvoltage  | protection,     | as               | part of          | the anti-islanding |           | protection,   | has    |
| data from     | a 1kW     | system      | and scaling | the      | output    | to a        | much larger |              |                 |                  |                  |                    |           |               |        |
|               |           |             |             |          |           |             |             | played an    | important       | role             | in preventing    |                    | sustained | overvoltages, |        |
1MWsystemwillresultinoverestimationofPVrampingimpacts.
|     |     |     |     |     |     |     |     | which could | lead | to damaged | equipment. |     | In many | countries, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ---------- | --- | ------- | ---------- | --- |
Theoutputdistributioncharacteristicsprovidedforvarioussized
|                  |     |        |             |     |           |     |           | required   | settings    | require | that the | PV        | inverters | trips before | the    |
| ---------------- | --- | ------ | ----------- | --- | --------- | --- | --------- | ---------- | ----------- | ------- | -------- | --------- | --------- | ------------ | ------ |
| PV installations |     | in [5] | can be used | for | examining | the | impact of |            |             |         |          |           |           |              |        |
|                  |     |        |             |     |           |     |           | regulatory | overvoltage | limits  | are      | exceeded. | However,  |              | use of |
suddenchangesinPVoutputonvoltage.
|     |     |     |     |     |     |     |     | anti-islanding | protection | for | voltage | control | could | lead to | nuisance |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | --- | ------- | ------- | ----- | ------- | -------- |
trippingofPVgeneration.
| 4.3 Open | issues |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6.2 Recommendations
| There are | no general | aggregation |     | rules | for multiple |     | PV systems |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
connectedtothesamedistributiongrid.
|     |     |     |     |     |     |     |     | The overvoltage |     | settings, | as part | of the | anti-islanding | protection |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------- | ------ | -------------- | ---------- | --- |
shouldconsidertheimpactontheoperationofthePVinstallations
|        |         |            |     |     |     |     |     | during periods |          | with high     | production |             | and low    | consumption. |          |
| ------ | ------- | ---------- | --- | --- | --- | --- | --- | -------------- | -------- | ------------- | ---------- | ----------- | ---------- | ------------ | -------- |
| 5 Slow | voltage | variations |     |     |     |     |     |                |          |               |            |             |            |              |          |
|        |         |            |     |     |     |     |     | Network        | planning | methodologies |            | for control | of voltage | levels       | that     |
|        |         |            |     |     |     |     |     | consider       | hosting  | capacity      | for PV     | generation  | based      | on           | relative |
Slow voltage variations are variations in the rms voltage with a voltagemarginsaswellasadvancedvoltagecontrolfrominverters
duration of 10min and longer. The effect of these is relevant to which reduces output before overvoltage occur should be
–
| voltage control |     | strategies | highly | affected | by  | changes | in power | considered. |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ------ | -------- | --- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
flow
| from       | MV        | to LV substations |     | where | load        | and generation | are       |          |        |     |     |     |     |     |     |
| ---------- | --------- | ----------------- | --- | ----- | ----------- | -------------- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
| installed. | At a time | interval          | of  | 10min | and longer, | the            | impact of |          |        |     |     |     |     |     |     |
|            |           |                   |     |       |             |                |           | 6.3 Open | issues |     |     |     |     |     |     |
PVinstallationsonvoltagevariationsisdueto
† Should the regulatory limits be based on 100% values orare there
thedailymovementofthesunoverthesky;
† arguments to allow the overvoltage limits to be exceeded during a
changesinamountofcloudcover,
| † shadingbyfixedobjects. |     |     |     |     |     |     |     | certainpercentageofthetime? |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
7 Flicker
5.1 Findings
OneareaofconcernwithregardstoPVproductionisthepotentialto
ThepresenceofPVinstallationsindistributionnetworkswillresult
|               |              |     |        |            |                     |     |     | cause flicker | due  | to the           | variations | in                | output of | the generation. |     |
| ------------- | ------------ | --- | ------ | ---------- | ------------------- | --- | --- | ------------- | ---- | ---------------- | ---------- | ----------------- | --------- | --------------- | --- |
| in additional | contribution |     | to the | variations | of voltagemagnitude |     | at  |               |      |                  |            |                   |           |                 |     |
|               |              |     |        |            |                     |     |     | Experience    | from | high-penetration |            | PV neighbourhoods |           | is discussed    |     |
timeintervalof10minandlonger.Theaveragevoltagemagnitude
|                |            |          |            |             |            |            |           | in [6] and | note | that flicker | has | not | been an | issue | in these |
| -------------- | ---------- | -------- | ---------- | ----------- | ---------- | ---------- | --------- | ---------- | ---- | ------------ | --- | --- | ------- | ----- | -------- |
| will increase, | but        | the      | voltage    | magnitude   | will       | also       | show more |            |      |              |     |     |         |       |          |
| variations.    | This       | includes | daily      | variations, | annual     | variations | and       |            |      |              |     |     |         |       |          |
| intra-hour     | variations | due      | to passing | clouds.     | In         | addition,  | rare but  |            |      |              |     |     |         |       |          |
| predictable    | solar      | eclipses | will       | result in   | additional | variations | in        |            |      |              |     |     |         |       |          |
voltagemagnitude.
| The presence |                          | of PV mayalso |     | lead to      | an increase | or        | decrease in |     |     |     |     |     |     |     |     |
| ------------ | ------------------------ | ------------- | --- | ------------ | ----------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| operations   | of mechanically-switched |               |     |              | regulation  | equipment | (on         |     |     |     |     |     |     |     |     |
| load tap     | changers,                | regulators    |     | and switched |             | capacitor | banks)      |     |     |     |     |     |     |     |     |
dependinguponcoincidenceofsolarproductionandload.
5.2 Recommendations
| Studies areneeded |     | to quantify | the        | consequences |      | of coincident | and |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | ---------- | ------------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| non-coincident    |     | solar       | production | and          | load | profiles      | on  |     |     |     |     |     |     |     |     |
voltage-magnitude variations. A good starting point will be the Fig. 2 P for a PV installation in Northern Sweden during a day with
st
gathering of long-term data on voltage-magnitude variations at varyingcloudcover
CIRED,OpenAccessProc.J.,2017,Vol.2017,Iss.1,pp.809–813
ThisisanopenaccessarticlepublishedbytheIETundertheCreativeCommons 811
AttributionLicense(http://creativecommons.org/licenses/by/3.0/)

installations.Fig.2showstheP fora20kWinstallationinNorthern this requirement to cover all inverter sizes. It remains unclear to
st
Sweden, with the PV system scaled to 6kW, during a day with whichextentsuchrequirementsareneeded.
varying cloud cover in June [7]. The maximum value of the P Single-phase inverters can be connected to the phase in which
lt
calculatedinthiscasewas0.036. they give the smallest increase in voltage unbalance. It may even
|     |     |     |     |     |     |     |     | be possible | to  | use PV | inverters | to compensate |     | the background |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --------- | ------------- | --- | -------------- | --- |
unbalance.Itishoweveruncleartowhichextendthisispractically
7.1 Findings
possible.
| Results from | literature | as  | well as | from analyses |     | of measurements |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ------- | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
flicker
| indicate | that low | levels of |     | can be | contributed | to  | the active |     |     |     |     |     |     |     |     |
| -------- | -------- | --------- | --- | ------ | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
power production from PV installations. While this increase in 9 Connect and disconnect
flickerismeasurable,itisnotexpectedtoreachunacceptablelevels.
|     |     |     |     |     |     |     |     | Large PV | installations | are | generally | connected | to         | the grid | via LV/  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --------- | --------- | ---------- | -------- | -------- |
|     |     |     |     |     |     |     |     | MV power | transformers. |     | In order  | to        | compensate | the      | reactive |
7.2 Recommendations
|     |     |     |     |     |     |     |     | power generated |     | by the network |     | cable capacitance, |     | shunt | reactors |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | --- | ------------------ | --- | ----- | -------- |
Whileunacceptableflickerlevelsarenotfoundtobecontributableto may be needed at the point of common coupling on the MV
the changesinactivepower fromPV installations, theresultshave system. The connecting transformers, the compensating reactor or
shown that some installations can in fact cause unacceptable the entire PV installation can be switched on and off because of
changes in voltage if the capacity of the PV installation exceeds intermittent power output of the source or due to faults. The
the local hosting capacity of the grid. This change in voltage is switchingofthePVplantforeithernormalscheduledoperationor
slower by naturedue to the slow-response time of PV installations forafaultcanleadtoundesirableovervoltagesandcurrents.
| relative           | to frequencies | of            | concern    | in  | relation | to flicker. | This     |              |              |     |          |        |        |            |     |
| ------------------ | -------------- | ------------- | ---------- | --- | -------- | ----------- | -------- | ------------ | ------------ | --- | -------- | ------ | ------ | ---------- | --- |
| phenomenon         | is             | appropriately | identified |     | in [5]   | as slow     | and fast |              |              |     |          |        |        |            |     |
| voltagevariations. |                |               |            |     |          |             |          | 9.1 Findings |              |     |          |        |        |            |     |
|                    |                |               |            |     |          |             |          | Transient    | overvoltages | and | currents | due to | sudden | connection | and |
7.3 Open issues disconnection of a PV installation have been documented.
|     |     |     |     |     |     |     |     | Energising | the PV | installation |     | MV/LV | transformer | can | result in |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | ----- | ----------- | --- | --------- |
Flicker contribution from changes in reactive power has been inrushcurrentsupto10timesratedcurrent.
observed in some PV installations. Analysis should be performed Laboratory testshave been performed to assessthe durationand
using measurements from additional installations to determine the magnitudeoftransientovervoltagescreatedbyPVinvertersduring
extentofthisphenomenon. load-rejection conditions. These tests have shown that the
measuredmaximumloadrejectionovervoltagedidnotexceed2pu
ofnominalpeakvoltage.
8 Voltage unbalance Laboratory tests have been performed in order to assess the
|     |     |     |     |     |     |     |     | inverter behaviour |     | during | the presence | of  | ground | faults | once the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------------ | --- | ------ | ------ | -------- |
Theprimarysourceofvoltageunbalanceatthedistributionvoltage breaker is opened. Ground fault overvoltages up to 1.6pu have
| level is unbalanced |        | load due      | to uneven   | spread     | of          | single-phase | LV  | beenobserved. |     |     |     |     |     |     |     |
| ------------------- | ------ | ------------- | ----------- | ---------- | ----------- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| customers           | to the | three phases. | The         | connection | of          | single-phase | PV  |               |     |     |     |     |     |     |     |
| installations       | will   | result in     | an increase | of         | the voltage | unbalance.   |     |               |     |     |     |     |     |     |     |
Single-phase units can only be expected in LV networks, most 9.2 Recommendations
likelywithdomesticandsmallcommercialcustomers.
|     |     |     |     |     |     |     |     | The test    | results   | available | at this | time are   | based      | upon single | and        |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | ------- | ---------- | ---------- | ----------- | ---------- |
|     |     |     |     |     |     |     |     | three-phase | inverters | of        | 20kW    | and below. | Additional |             | testing of |
8.1 Findings
|     |     |     |     |     |     |     |     | larger sized | inverters | is recommended |     | to  | determine | the full | extent |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------------- | --- | --- | --------- | -------- | ------ |
ofloadrejectionandgroundfaultovervoltages.
| The hosting  | capacity | for           | voltage    | unbalance | is            | only relevant | for   |             |          |                |               |     |          |            |          |
| ------------ | -------- | ------------- | ---------- | --------- | ------------- | ------------- | ----- | ----------- | -------- | -------------- | ------------- | --- | -------- | ---------- | -------- |
|              |          |               |            |           |               |               |       | Additional  | testing  | is recommended |               | to  | consider | additional | fault    |
| single-phase | units.   | Large         | individual | PV        | installations | and           | large |             |          |                |               |     |          |            |          |
|              |          |               |            |           |               |               |       | conditions, | inverter | vendor         | technologies, |     | load     | levels,    | and load |
| numbers      | of small | installations | should     | be        | treated       | differently.  | For   |             |          |                |               |     |          |            |          |
compositions(e.g.motorloads).
| large individual |     | units the | hosting  | capacity   | is obtained |     | from the |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | -------- | ---------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| source impedance |     | at the    | point of | connection | (point      | of  | common   |     |     |     |     |     |     |     |     |
coupling), the existing (pre-connection) unbalance, and the 9.3 Open issues
acceptablevoltageunbalance.
For small units, calculation of the hosting capacity requires Although different tests on PV inverters are performed by
knowledge on their spread to the phases and to the locations. A laboratories, there is an absence of acceptance criteria to
simple relation has been obtained between voltage unbalance and characterise load rejection and ground faults overvoltages. The
| numberofunits[6]. |             |                |             |         |              |             |           | teststhemselvesarenotyetstandardised. |     |     |     |     |     |     |     |
| ----------------- | ----------- | -------------- | ----------- | ------- | ------------ | ----------- | --------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Voltage           | unbalance   | may            | be an issue | when    | single-phase |             | units are |                                       |     |     |     |     |     |     |     |
| used. For         | three-phase | units,         | unbalance   |         | should       | not be      | an issue. |                                       |     |     |     |     |     |     |     |
| However,          | it has      | been mentioned |             | that    | certain      | older       | types of  |                                       |     |     |     |     |     |     |     |
|                   |             |                |             |         |              |             |           | 10 Conclusions                        |     |     |     |     |     |     |     |
| three-phase       | inverters   | also           | exhibit     | a large | unbalance    | in current. | No        |                                       |     |     |     |     |     |     |     |
furtherinformationonthishasbeenobtained.
AconcernwiththeconnectionofPVinstallationsistheirpotential
|     |     |     |     |     |     |     |     | impact on | the voltage | and | current | quality | in the | grid. The | creation |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | ------- | ------ | --------- | -------- |
8.2 Recommendations of this working group should not be seen as aconfirmation of any
|     |     |     |     |     |     |     |     | negative | impact | of PV | installations | on  | the | grid. Instead, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ------------- | --- | --- | -------------- | --- |
Tobeabletoestimatethehostingcapacity,itisimportanttoobtain
|            |              |     |            |           |     |         |           | principal      | aim | of this     | working | group    | is       | a mapping | and     |
| ---------- | ------------ | --- | ---------- | --------- | --- | ------- | --------- | -------------- | --- | ----------- | ------- | -------- | -------- | --------- | ------- |
| background | measurements |     | of voltage | unbalance |     | at many | locations |                |     |             |         |          |          |           |         |
|            |              |     |            |           |     |         |           | quantification | of  | that impact |         | where it | concerns | power     | quality |
includinginformationonthephaseangleofthevoltageunbalance.
|     |     |     |     |     |     |     |     | disturbances. | Key  | findings | from       | each  | of the | power   | quality |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | -------- | ---------- | ----- | ------ | ------- | ------- |
|     |     |     |     |     |     |     |     | phenomena     | have | been     | summarised | here. | More   | details | can be  |
8.3 Open issues found in [5]. For each of the disturbances, the emission by PV
|     |     |     |     |     |     |     |     | installations | is  | characterised, |     | as much | as possible, |     | based on |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ------- | ------------ | --- | -------- |
Somecountrieshaveputrequirementsoninverters,requiringthemto existing installations. A decision about possible negative impacts
be three-phase above a certain size. Other countries even consider canbemademostlikelyonlyonacase-by-casebasis.
CIRED,OpenAccessProc.J.,2017,Vol.2017,Iss.1,pp.809–813
812 ThisisanopenaccessarticlepublishedbytheIETundertheCreativeCommons
AttributionLicense(http://creativecommons.org/licenses/by/3.0/)

11 References 4 Bollen,M.,Rönnberg,S.:‘Primaryandsecondaryharmonicsemission;harmonic
interaction–asetofdefinitions’.Proc.ofInt.Conf.onHarmonicsandQualityof
1 Varatharajan,A.,Schoettke,S.,Meyer,J.,,etal.:‘HarmonicemissionoflargePV Power(ICHQP),BeloHorizonte,Oct2016
installations – case study of a 1MW solar campus’. Int. Conf. on Renewable 5 ‘JWGC4/C6.29powerqualityaspectsofsolarpower’,TechnicalBrochure672,
EnergiesandPowerQuality(ICREPQ),Cordoba,Spain,April2014 CIGRE2016,2016
2 Rönnberg,S.K.,Gil-deCastro,A.G.,Bollen,M.H.J.,,etal.:‘Supraharmonics 6 Katiraei, F., Konrad, M., Dignard-Bailey, L.: ‘Integration of photovoltaic power
frompowerelectronicsconverters’.Proc.of9thInt.Conf.onCompatibilityand systems in high-penetration clusters for distribution networks and mini-grids’,
PowerElectronics(CPE),CostadaCaparica,2015,pp.539–544 Int.J.Distrib.EnergyResour.,2007,3,(3),pp.207–223.ISSN1614-7138
3 Klatt,M.,Meyer,J.,Schegner,P.,,etal.:‘Emissionlevelsabove2kHz—laboratory 7 Lennerhag, O., Bollen, M., Ackeby, S.,, et al.: ‘Spänningsvariationer och
resultsandsurveymeasurements in public lowvoltagegrids’.Procof.(CIRED intermittent produktion’, (voltage variations and intermittent production, in
2013),22ndInt.Conf.andExhibitiononElectricityDistribution,Stockholm,2013 Swedish),Elforsk,Stockholm,report14:42,July2014
CIRED,OpenAccessProc.J.,2017,Vol.2017,Iss.1,pp.809–813
ThisisanopenaccessarticlepublishedbytheIETundertheCreativeCommons 813
AttributionLicense(http://creativecommons.org/licenses/by/3.0/)