1
Electricity Demand and Grid Impacts of AI Data
Centers: Challenges and Prospects
Xin Chen, Xiaoyang Wang, Ana Colacelli, Matt Lee, Le Xie
Abstract—The rapid growth of artificial intelligence (AI) is AIdatacentersarethecomputingfacilitiesthataredesigned
driving an unprecedented increase in the electricity demand of and optimized to execute large-scale AI workloads, such as
AI data centers, raising emerging challenges for electric power
the training and inference of LLMs, computer vision systems,
grids. Understanding the characteristics of AI data center loads
and other compute-intensive AI applications. In contrast to
and their interactions with the grid is therefore critical for
ensuring both reliable power system operation and sustainable traditional data centers, which primarily provide general-
AI development. This paper provides a comprehensive review purpose information technology (IT) services, AI data centers
and vision of this evolving landscape. Specifically, this paper (i) are architected to deliver the extreme computational perfor-
presentsanoverviewofAIdatacenterinfrastructureanditskey
mance required for advanced AI workloads (see Table I for
components, (ii) examines the key characteristics and patterns
a detailed comparison). This capability is enabled by dense
of electricity demand across the stages of model preparation,
training, fine-tuning, and inference, (iii) analyzes the critical configurationsofhigh-performancecomputinghardware,such
challengesthatAIdatacenterloadsposetopowersystemsacross as Graphics Processing Units (GPUs) [9] and Tensor Process-
three interrelated timescales, including long-term planning and ing Units (TPUs) [10], together with high-efficiency cooling
interconnection, short-term operation and electricity markets, systems [11]. Modern hyperscale AI data centers typically
andreal-timedynamicsandstability,and(iv)discussespotential
operate with power demand exceeding 100 MW [12], and
solutions from the perspectives of the grid, AI data centers,
and AI end-users to address these challenges. By synthesizing some new campuses are planned to scale to the gigawatt
current knowledge and outlining future directions, this review (GW) level [13]. As a result, AI data centers are emerging as
aims to guide research and development in support of the joint prominent large electric loads in the power grid, with distinct
advancement of AI data centers and power systems toward
characteristics and demand patterns, including:
reliable, efficient, and sustainable operation.
Index Terms—AI data centers, electric load demand, grid • High power density: Intensive AI workloads require
impact, emerging challenges, potential solutions. substantially more power than conventional IT services.
For instance, a ChatGPT query is estimated to consume
about 2.9 Wh, nearly ten times the 0.3 Wh of a regular
I. INTRODUCTION
Googlesearch[14].Incontrasttotraditionalserverracks
IN recent years, the accelerated advancement of generative typically operating at 7-10 kW, AI computing racks can
artificialintelligence(AI),particularlylargelanguagemod- reachpowerdensitiesof30-100+kWperrack[15].Such
els(LLMs)[1]suchasGPT[2],LLaMA[3],andGemini[4], extreme power density places considerable strain on data
has fueled explosive growth in the AI industry. This surge is center architecture, cooling systems, and power grids.
driving the rapid expansion of data center infrastructure and • Fast and large variability: Across the training, fine-
imposingunprecedentedpressureonthepowergridduetothe tuning,andinferencephases,AIworkloadscanbehighly
immense electricity demands of ultra-scale AI workloads. For variable and bursty [16], with power demand fluctuating
instance, training GPT-3 is estimated to have consumed 1.29 sharplyoververyshorttimescalesandremainingdifficult
GWh of electricity [5], whereas the electricity consumption to forecast [17]. For example, large-scale GPU clusters
for training the larger-scale GPT-4 rose dramatically to an canproducepowerfluctuationsofhundredsofmegawatts
estimated over 50 GWh [6], [7], equivalent to nearly 0.1% within only seconds [18], [19], bringing significant chal-
of New York City’s annual electricity use. According to a lenges for system balancing and reliable grid operation.
recent International Energy Agency (IEA) report [8], global • Grid interface via power electronics: AI data centers in-
datacentersconsumedaround415TWhofelectricityin2024 terfacewiththepowergridprimarilythroughpowerelec-
(about1.5%oftotalglobaldemand),andtheirconsumptionis tronic converters, which exhibit fundamentally different
projected to more than double by 2030 to around 945 TWh, dynamic behaviors from conventional electromechanical
with AI identified as the primary driver of this growth. loads, such as low inertia, fast response dynamics, and
harmonic distortions [20]. At scale, power electronics-
X.ChenandX.WangarewiththeDepartmentofElectricalandComputer based AI computing loads can pose major threats to grid
Engineering, Texas A&M University, USA. A. Colacelli is with the Envi-
stability and cause severe power quality issues [21].
ronmental Engineering Department, Texas A&M University. M. Lee is with
theTexasA&MEnergyInstitute.L.XieiswiththeJohnA.PaulsonSchool • Geographicconcentration:AIdatacenterstendtocluster
of Engineering and Applied Sciences, Harvard University. (Corresponding inregionswithlowelectricityprices,amplelandandwa-
author:XinChen,email:xin chen@tamu.edu)
ter resources, and favorable policy environments. In the
TheworkwassupportedbytheConsortiumonAIandLargeFlexibleLoad
(CALL)atTexasA&MUniversity. U.S., for example, fifteen states (most notably Virginia,
5202
peS
8
]YS.ssee[
1v81270.9052:viXra

2
Texas, and California) accounted for about 80% of total conclusions are drawn in Section VI.
| data | center demand |     | in 2023 | [14]. Such | concentration | ef- |     |     |     |     |     |     |     |
| ---- | ------------- | --- | ------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fectfurtherintensifieslocalgridstress,andmanyregional
II. OVERVIEWOFAIDATACENTER
| grids | cannot accommodate |     |     | large-scale | integration | of data |     |     |     |     |     |     |     |
| ----- | ------------------ | --- | --- | ----------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
centers without substantial infrastructure upgrades [22]. This section provides an overview of the primary compo-
As such, the rapid expansion of AI data centers poses nents of an AI data center, including IT hardware, electrical
|     |     |     |     |     |     |     | power infrastructure, |     | cooling | systems, |     | and other | supporting |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------- | -------- | --- | --------- | ---------- |
unprecedentedchallengestomodernpowersystems.Tosustain
thefastpaceofAIinnovationandthecontinuedgrowthofAI facilities.Atypicalarchitectureillustratingtheinterconnection
|                 |       |           |              |     |                      |     | of these components |     | is  | depicted | in Figure | 2. Key | distinctions |
| --------------- | ----- | --------- | ------------ | --- | -------------------- | --- | ------------------- | --- | --- | -------- | --------- | ------ | ------------ |
| infrastructure, | it is | essential | to establish |     | a deep understanding |     |                     |     |     |          |           |        |              |
of AI data center loads and their interactions with the grid, between AI and conventional data centers are summarized in
andtodevelopeffectivesolutionstrategiesthatensurereliable Table I and detailed below.
| and sustainable | power  | system | operation.   |          |             |              |                |          |                |     |       |                   |     |
| --------------- | ------ | ------ | ------------ | -------- | ----------- | ------------ | -------------- | -------- | -------------- | --- | ----- | ----------------- | --- |
| A growing       | number | of     | recent       | articles | and reports | [7], [8],    |                |          |                |     |       |                   |     |
|                 |        |        |              |          |             |              | A. IT Hardware |          | Infrastructure |     |       |                   |     |
| [14], [23]–[25] | have   | drawn  | considerable |          | attention   | to the surg- |                |          |                |     |       |                   |     |
|                 |        |        |              |          |             |              | The IT         | hardware | infrastructure |     | forms | the computational |     |
ingelectricitydemandofAIdatacentersandtheirimplications
forthepowersector.Priorworks[11],[14]examinetheenergy backbone of an AI data center and encompasses the comput-
|           |              |     |           |     |       |             | ing, storage, | and | networking |     | systems, | which execute | large- |
| --------- | ------------ | --- | --------- | --- | ----- | ----------- | ------------- | --- | ---------- | --- | -------- | ------------- | ------ |
| use of AI | data centers | by  | analyzing | the | power | consumption |               |     |            |     |          |               |        |
ofkeycomponents,includingAIcomputing,coolingsystems, scale model training and inference, manage massive datasets,
and auxiliary facilities, and present strategies for energy- and enable high-throughput communication.
1) Computing:
efficient operation. Reference [26] proposes a benchmarking AI workloads, such as LLM training and
framework for quantifying the footprint of energy, water, and inference, require high-performance computing clusters de-
|                  |     |        |           |            |        |       | signed to | execute | large-scale | computations |     | efficiently. | These |
| ---------------- | --- | ------ | --------- | ---------- | ------ | ----- | --------- | ------- | ----------- | ------------ | --- | ------------ | ----- |
| carbon emissions |     | of LLM | inference | workloads. | Recent | study |           |         |             |              |     |              |       |
[16]analyzesthetransientdynamicbehaviorsofAIcomputing clusterstypicallyintegratemulti-coreCentralProcessingUnits
powerconsumption,developshigh-levelmathematicalmodels (CPUs) with dense configurations of GPUs and TPUs [10].
Theseprocessingunitsarehousedinhigh-densityservernodes
forAIdatacenterloads,anddiscussestheresultingdisruptions
and opportunities for power systems. Case studies on several and stacked in standardized computer racks, allowing scal-
|             |               |     |         |           |       |          | able deployment, |     | efficient | power | distribution, | and | optimized |
| ----------- | ------------- | --- | ------- | --------- | ----- | -------- | ---------------- | --- | --------- | ----- | ------------- | --- | --------- |
| power grids | are conducted |     | in [22] | to assess | their | capacity | to               |     |           |       |               |     |           |
accommodate projected five-year AI data center load growth, cooling.Comparedwithconventionaldatacenters,AI-oriented
derivingimplicationsforlong-termgridplanningandmanage- computing facilities concentrate substantially greater process-
|                |     |          |            |     |        |            | ing power | within | each | rack. While | a standard | rack | typically |
| -------------- | --- | -------- | ---------- | --- | ------ | ---------- | --------- | ------ | ---- | ----------- | ---------- | ---- | --------- |
| ment. However, | the | existing | literature | has | mainly | focused on |           |        |      |             |            |      |           |
the AI data center itself and presented high-level, preliminary, uses 7-10 kilowatt (kW), an AI-capable rack can demand 30
|                |              |     |       |                 |     |         | kW to over | 100 | kW [14], | [25], | with an | average | of more than |
| -------------- | ------------ | --- | ----- | --------------- | --- | ------- | ---------- | --- | -------- | ----- | ------- | ------- | ------------ |
| and fragmented | discussions, |     | while | a comprehensive |     | and in- |            |     |          |       |         |         |              |
depthsynthesisofAIdatacenterloadcharacteristicsandtheir 60 kW in dedicated AI facilities [15]. For example, the per-
impacts on power grids, particularly the challenges from the rack power of NVIDIA’s GB200 NVL36 and NVL72 servers
|                     |     |         |          |     |     |     | reaches about | 66  | kW  | and 120 | kW [27], | respectively. | The |
| ------------------- | --- | ------- | -------- | --- | --- | --- | ------------- | --- | --- | ------- | -------- | ------------- | --- |
| grid’s perspective, |     | remains | lacking. |     |     |     |               |     |     |         |          |               |     |
Tobridgethiscriticalgapandhelpguidefutureresearchand substantially higher power densities pose critical challenges
development in the field, this paper presents a comprehensive for power distribution and thermal management.
review and vision that (i) details the overall architecture of 2) Storage: To sustain intense compute capabilities, scal-
AI data centers together with their load characteristics and ableandhigh-performancedatastorageisnecessitatedtohan-
dlemassivetrainingdatasets,intermediatemodelcheckpoints,
| patterns, | and (ii) provides |     | a systematic | analysis |     | of the multi- |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | ------------ | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
timescale and multi-faceted challenges posed by the rapid and inference data. Tiered storage components include: (i) the
growthofAIdatacenterstopowergrids,alongwithpromising hottier,suchasNon-VolatileMemoryExpress(NVMe)Solid
solutions for enabling their large-scale integration to the grid. StateDrives(SSDs)arrays[28],providesultra-lowlatencyand
Specifically, Section II presents an overview of AI data center high bandwidth to store active data for fast processing, (ii)
thewarmtier,suchashigh-capacityharddiskdrives(HDDs),
| infrastructure | and | its key | components. |     | Section | III examines |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ----------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
the characteristics and patterns of electricity demand across is cost-effective for storing massive, less frequently accessed
the AI model preparation, training, fine-tuning, and inference data, and (iii) the code tier stores data in tape libraries or
stages. Section IV analyzes the key challenges that AI data objectstoragesystemsforlong-termarchivingwithlessaccess
center loads bring to power systems across three interrelated speed. In addition, distributed file systems, such as Lustre
timescales:long-termplanningandinterconnection,short-term and Ceph [29], allow large-scale parallel reading and writing,
operationandelectricitymarkets,andreal-timegriddynamics while object storage is used for archiving large datasets with
andstability.Othercriticalchallenges,includingcybersecurity, longdurabilityandredundancy[30].Unlikeconventionaldata
decarbonization, and water resources, are discussed as well. centers,whichbalancecapacity,cost,andspeed,AI-optimized
Section V presents potential solutions from the grid side, storageprioritizesmaximumthroughputandparallelaccessto
AI data center side, and AI end-user side to address these prevent bottlenecks that idle expensive GPU clusters.
challengesandensurereliablepowersystemoperation.Figure 3) Networking: High-speednetworkingiscriticaltoensure
1 visualizes the critical challenges discussed in Section IV that massive data flow efficiently between storage systems
and potential solutions introduced in Section V. At last, and compute nodes during large-scale AI workloads. The

3
Fig.1. Criticalchallengesandpotentialsolutionsforthelarge-scaleintegrationofAIdatacenterstothepowergrid.
Fig.2. AtypicalarchitectureofanAIdatacenter.(Thetransformervoltagelevelsandthepresenteddouble-conversionUPSsystemareillustrativeexamples;
actualconfigurationsvaryacrossdatacenters).
TABLEI
COMPARISONBETWEENTRADITIONALDATACENTERSANDAIDATACENTERS
| Feature | TraditionalDataCenter | AIDataCenter |
| ------- | --------------------- | ------------ |
General-purposeITservices(e.g.,web/apphosting,
AI/MLmodeltraining,fine-tuning,andinference(e.g.,large
| PrimaryFunctions | databases,enterprisesoftwarehosting,cloudstorage,email, |     |
| ---------------- | ------------------------------------------------------- | --- |
virtualization,backuprecovery) languagemodels,AIcomputervision,generativeAI)
WorkloadPattern Stable,predictableworkloads Dynamic,bursty,data-intensive,hard-to-predictworkloads
| ComputeHardware | CPU-centric,someGPUs | GPU/TPU-denseclusters |
| --------------- | -------------------- | --------------------- |
RackPowerDensity 7kW-10kW/rack,moderatedensity 30kW-over100kW/rack,veryhighdensity
Veryhigh-throughputSSD/NVMestoragewithparallelfile
| Storage | Balancedperformanceandcapacity,mixofHDDandSSD |     |
| ------- | --------------------------------------------- | --- |
systems
StandardEthernet,designedforgeneral-purposetraffic Ultra-high-bandwidth,low-latencyinterconnects(InfiniBand,
Networking
|     | patterns | NVLink)fordistributedAIworkloads |
| --- | -------- | -------------------------------- |
Cooling Primarilyaircooling Liquidcooling(direct-to-chip,immersion)orhybridcooling
Optimizedforhigh-densityAIworkloads,reinforced
| FacilityDesign | Optimizedformixedworkloads,standardfloorloading |     |
| -------------- | ----------------------------------------------- | --- |
structuresforheavyracksandcoolingequipment

4
networking system in an AI data center includes both intra- 3) Backup Generation: Backup generation provides emer-
node interconnects, such as NVIDIA NVLink [31] for high- gencypowertoensurethatAIworkloadsremainuninterrupted
bandwidth GPU-to-GPU communication within a server, and in the event of a grid outage. Traditionally, diesel generators
inter-node fabrics, such as InfiniBand [32] or Ethernet with have been the most common solution because of low costs
RDMA over Converged Ethernet (RoCE), for low-latency, and their ability to quickly deliver large amounts of power
high-throughput communication between servers and racks. to reliably support full critical IT load and essential cooling
Specializednetworktopologies,includingfat-treeanddragon- systems. To enhance sustainability, some facilities integrate
fly architectures [33], are adopted to optimize GPU-to-GPU on-site renewables, such as solar photovoltaic (PV) arrays or
communication in distributed training environments. In con- hydrogen fuel cell systems, to supplement or partially replace
trast, conventional data centers are usually designed for more diesel generators [38]. For instance, Caterpillar and Microsoft
heterogeneous workloads and general-purpose traffic patterns, successfully used hydrogen fuel cells to supply backup power
and do not require such high bandwidth or low latency. toadatacenterfor48hours[39].Thesecleangenerationscan
operateinparallelwithconventionalgeneratorsduringoutages
B. Electric Power Infrastructure and supply power under normal conditions to reduce reliance
1) Grid Power Supply: AI data centers are typically con- on the grid. Most backup generation systems are equipped
nected to the medium- or high-voltage distribution grid, while withautomatictransferswitches,enablingthemtostartwithin
hyperscale facilities may connect directly to the transmission seconds and seamlessly supply power during an outage.
grid as their primary power source. Depending on the local
grid infrastructure and facility scale, interconnection voltages C. Cooling Facilities
canrangefromabout13.2kVforsmall-scaleinstallations(un-
In AI data centers, cooling facilities are essential for dis-
der10MW)to115-230kVforhyperscalesites(exceeding100
sipating the substantial heat generated by high-density com-
MW) in the U.S. [12]. As illustrated in Figure 2, alternating
puting equipment, particularly GPU- and TPU-based clusters,
current (AC) power enters the facility through high-voltage
maintainingsafeoperationandpreventinghardwarefailures.A
switchgear and protective devices, after which it is stepped
varietyofcoolingtechnologieshave beenusedindatacenters
down to operational voltage levels such as 480 V via on-site
[40], which are broadly classified into three main categories:
three-phase step-down transformers. These transformers not
(i) Air cooling [41] circulates chilled air to absorb heat from
only reduce voltage but also provide electrical isolation be-
ITequipmentandexpelitfromthefacility.Duetoitslowcost
tween the utility grid and the facility’s internal power supply
andoperationalsimplicity,aircoolinghasbeenthemainstream
system. The power is then distributed through main distri-
choice for data centers with low rack power densities (below
bution panels and power distribution units (PDUs) to supply
20 kW), but it becomes inadequate for AI clusters with much
IT server racks, cooling systems, and other supporting loads.
higher rack power densities [11]. (ii) Liquid cooling uses a
For IT server racks, AC power is further converted to direct
liquid medium to remove heat from servers, which absorbs
current (DC) via a power factor correction (PFC) rectifier,
heat far more effectively than air and allows for very high
followedbyaDC-DCconverterforDC-sidevoltageregulation
rack power densities. For example, liquid immersion cooling
[34], ensuring stable and properly rated power delivery to
[42]submergesserversinengineereddielectricfluids,enabling
IT equipment. Additionally, large AI data centers typically
safe,directcontactwithelectroniccomponentsandhighlyeffi-
employ redundant utility feeders and transformers to ensure
cientheatremoval;direct-to-chipliquidcooling[43]circulates
high reliability and continued operation even during partial
coolant through cold plates mounted directly on processors or
grid outages [35].
other high-heat components, improving heat transfer without
2) UninterruptiblePowerSupply(UPS): UPSsystems[36]
immersing the entire server in liquid. (iii) Hybrid cooling
serve as the first layer of protection against power interrup-
[44] combines air and liquid cooling methods to optimize
tions in data center operations. They provide instantaneous
efficiency under varying workloads. This approach offers
electrical power from energy storage devices, such as batter-
flexible operation, reduces energy consumption, and mitigates
ies or flywheels, when the grid supply is disrupted, ensur-
the high infrastructure cost and complexity of fully liquid-
ing continuous operation during the transition period before
cooleddesigns.Thecommonlyusedcoolingmethodsaresum-
backup generators start and synchronize with the load. UPS
marizedinTableIII.Inpractice,coolingselectiondependson
deployments commonly employ battery technologies such as
factors such as rack power density, energy efficiency targets,
valve-regulated lead-acid (VRLA), lithium-ion, and emerging
facility design constraints, capital and operational costs, and
solid-state chemistries [37]. Selection criteria include specific
water availability. Particularly, rapidly growing AI workloads
power and energy ratings, cycle life, energy density, thermal
are accelerating the adoption of advanced liquid-based and
management requirements, and cost-effectiveness. UPS sys-
intelligent cooling solutions. Further discussion on smart and
tems typically operate in three modes: normal mode, double-
efficient cooling techniques is provided in Section V-B.
conversionmode,andbatterymode[34],andtheyaresizedto
handle high power demands of dense GPU and TPU racks in
D. Other Supporting Facilities
AI data centers. Modern UPS systems can also support grid-
interactive capabilities, enabling data centers to shift loads Beyond core IT hardware, electrical power infrastructure,
or participate in demand response programs by temporarily and cooling systems, AI data centers incorporate additional
supplying power from their stored energy. supporting facilities that ensure reliable, secure, and efficient

5
TABLEII
SUMMARYOFELECTRICPOWERINFRASTRUCTUREINAIDATACENTERS
InfrastructureComponent Function KeyEquipment DetailsandFeatures
|     |     |     |     |     |     | Switchandprotectivedevices,step-down |     |     |     | Connectedto13.2-230kVgrid,steppeddownto |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
Primaryelectricity
GridPowerSupply transformers,powerdistributionunits, 480/415Vusingisolationtransformers,
source
|                      |     |     |                    |     |     | powerconverters                 |     |     |     | redundancyensuresreliability               |     |     |     |     |
| -------------------- | --- | --- | ------------------ | --- | --- | ------------------------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
|                      |     |     |                    |     |     | Valve-regulatedlead-acid(VRLA), |     |     |     | Instantaneouspowersupplyuntilbackupstarts, |     |     |     |     |
| UninterruptiblePower |     |     | Instantaneouspower |     |     |                                 |     |     |     |                                            |     |     |     |     |
Supply(UPS) duringinterruptions lithium-ion,solid-statebatteries, protectGPU/TPUracks,supportgrid-interactive
|     |     |     |     |     |     | flywheels |     |     |     | capabilitiesanddemandresponse |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
SupportcriticalITandcoolingloads,automatic
|                  |     |     | Emergencypower    |     |     | Dieselgenerators,solarPV,hydrogen |     |     |     |                                           |     |     |     |     |
| ---------------- | --- | --- | ----------------- | --- | --- | --------------------------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
| BackupGeneration |     |     |                   |     |     |                                   |     |     |     | transferswitchesenableseamlesstransition, |     |     |     |     |
|                  |     |     | duringgridoutages |     |     | fuelcells                         |     |     |     |                                           |     |     |     |     |
renewableintegration
TABLEIII
COMPARISONOFAIDATACENTERCOOLINGTECHNIQUES
Efficiency
| CoolingMethod |     |     | HeatDensitySuitability |     |     |     |     | Pros |     |     |     | Cons |     |     |
| ------------- | --- | --- | ---------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- |
(PUE)
Poorefficiencyathighrackpower
AirCooling[41] Low-moderate ∼1.1–2.9[45] Simple,lowcost,widelyadopted
(>30kW)
Direct-to-ChipLiquid ∼1.1–1.3[46] Excellentthermaltransfer,ideal Requiresplumbingand
Cooling[43] High fordenseAIworkloads infrastructure;riskofleaks
Redesignneeded,fluidcost,
ImmersionCooling[42] Veryhigh(>50kW/rack) ∼1.02-1.04[45] Ultra-efficient,lownoise,compact
specializedhardware
Flexibleandadaptabletoexisting
HybridCooling[43] Medium-high ∼1.34-1.38[47] Systemintegrationcomplexity
setups
operations. These include: (i) physical infrastructure and lay- electricity consumption. Looking ahead, the IEA projects that
out encompass data hall design features such as hot/cold aisle global data center electricity demand will more than double
containmenttooptimizeairflow,raisedfloorsoroverheadtrays by 2030, reaching around 945 TWh, with AI identified as
fororganizedcablingandventilation,andstructuralreinforce- the primary driver of this growth [8]. The global data center
mentstoaccommodatetheweightofhigh-densityserverracks; electricity consumption is further discussed in Appendix A.
(ii) monitoring and control systems involve dense networks ModernhyperscaleAIfacilitiestypicallycontractforpower
of temperature, humidity, and airflow sensors integrated into capacities exceeding 100 MW, with some campuses planned
centralized building management platforms, along with fire to scale to the gigawatt level [13], to support ultra-scale
|           |                 |     |         |     |           |       |          | AI training | and | inference. | According |     | to the | Electric Power |
| --------- | --------------- | --- | ------- | --- | --------- | ----- | -------- | ----------- | --- | ---------- | --------- | --- | ------ | -------------- |
| detection | and suppression |     | systems |     | employing | inert | gases or |             |     |            |           |     |        |                |
pre-actionsprinklerstosafeguardequipment;(iii)securityand Research Institute (EPRI) white paper [14], electricity con-
accesscontrolmeasurescombinephysicalbarriers,continuous sumption in a data center is mainly attributed to IT hardware
video surveillance, and multi-factor authentication to prevent equipment,whichtypicallyaccountsfor40-50%oftotalload.
unauthorized entry; and (iv) auxiliary systems comprise re- Coolingsystemsrepresentthesecond-largestshare,consuming
dundant network links, battery energy storage systems, water approximately 30-40%, depending on the cooling technology
treatment units for cooling operations, energy-efficient and and server rack density. The remaining 10-30% is from other
emergency lighting, and dedicated office and maintenance supporting facilities, including lighting, office spaces, and
spaces for on-site staff. monitoring and security systems. In AI data centers, the
|     |     |     |     |     |     |     |     | share of  | electricity | consumed |        | by IT equipment |     | is higher and   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | ------ | --------------- | --- | --------------- |
|     |     |     |     |     |     |     |     | typically | exceeds     | 60%,     | due to | the adoption    |     | of high-density |
III. ELECTRICITYDEMANDOFAIDATACENTERS
|      |         |          |     |             |        |     |         | GPU/TPU | racks | and efficient |     | liquid | cooling | systems. Power |
| ---- | ------- | -------- | --- | ----------- | ------ | --- | ------- | ------- | ----- | ------------- | --- | ------ | ------- | -------------- |
| This | section | analyzes | the | electricity | demand | of  | AI data |         |       |               |     |        |         |                |
UsageEffectiveness(PUE)[14]isthemostwidelyusedmetric
| centers. | It firstly  | outlines | their      | electricity | consumption |                 | struc- |            |        |            |             |             |        |                  |
| -------- | ----------- | -------- | ---------- | ----------- | ----------- | --------------- | ------ | ---------- | ------ | ---------- | ----------- | ----------- | ------ | ---------------- |
|          |             |          |            |             |             |                 |        | to measure | the    | energy     | efficiency  | of          | a data | center, which is |
| ture and | efficiency, | and      | then       | presents    | the         | characteristics | and    |            |        |            |             |             |        |                  |
|          |             |          |            |             |             |                 |        | defined    | as the | ratio (1): |             |             |        |                  |
| patterns | of the      | dominant | component, |             | AI          | computing       | load,  |            |        |            |             |             |        |                  |
|          |             |          |            |             |             |                 |        |            | Total  | Facility   | Electricity | Consumption |        |                  |
across different stages of AI workflows, including model PUE= ≥1. (1)
|              |           |              |     |     |            |     |     |         | IT  | Equipment | Electricity | Consumption |             |              |
| ------------ | --------- | ------------ | --- | --- | ---------- | --- | --- | ------- | --- | --------- | ----------- | ----------- | ----------- | ------------ |
| preparation, | training, | fine-tuning, |     | and | inference. |     |     |         |     |           |             |             |             |              |
|              |           |              |     |     |            |     |     | A lower | PUE | indicates | greater     | energy      | efficiency, | with a value |
of1.0signifyingthatallelectricityisusedforITcomputation.
| A. Electricity | Consumption |     | Structure |     | and Efficiency |     |     |           |            |      |        |       |        |                 |
| -------------- | ----------- | --- | --------- | --- | -------------- | --- | --- | --------- | ---------- | ---- | ------ | ----- | ------ | --------------- |
|                |             |     |           |     |                |     |     | A typical | enterprise | data | center | has a | PUE of | around 1.5-1.6, |
AI data centers are emerging as one of the fastest-growing whilemodernlarge-scalefacilitiesachievealowerPUEbelow
electricity consumers in the energy sector. According to the 1.3. For example, Google reports a comprehensive trailing
IEAreport[8],globaldatacentersconsumedaround415TWh twelve-month PUE of 1.09 across its large-scale data centers,
ofelectricityin2024,accountingforabout1.5%oftotalglobal with some sites operating under 1.06 [48]. Similarly, Meta’s

6
2024 Sustainability Report states an average PUE of 1.08 resulting in exceptionally high electricity consumption, often
across its data centers [49]. It indicates that IT computing ranging from hundreds to thousands of MWh.
dominates the electricity consumption of these data centers. Typical electricity load patterns during the training stage
include: (i) Initial load ramp-up phase: at the beginning of
training,resourceutilizationgraduallyincreasesasdatasetsare
B. AI Computing Load Patterns at Different Stages loaded into memory and distributed across computing nodes,
creatingashortperiodofescalatingdemand[17].(ii)Constant
Since AI computing constitutes the dominant share of
high demand: computing hardware operates at near-maximum
electricity consumption in AI data centers, this subsection
utilization for prolonged periods with very high power load
analyzes its load patterns and characteristics across the four
throughoutthetrainingstage[20].(iii)Rapidandlargepower
main stages of AI model workflows: preparation, training,
fluctuations: the alternation between a power-intensive com-
fine-tuning, and inference [3], [50].
putation phase and a less power-demanding communication
1) Preparation Stage: The preparation stage aims to pre-
phase in the training stage often leads to large power swings
paretheAImodelarchitectureanddatabeforeformaltraining
[18]. Besides, tasks such as checkpointing, intermediate result
begins [50]. It includes: (i) model preparation: designing or
saving, and large-scale data transfers between nodes can
selecting a base AI model, configuring model size, param-
cause brief but pronounced spikes in electricity consumption;
eters, architecture, precision settings, and conducting early-
additional transient surges may occur when training is paused
phase experimental testing; and (ii) data acquisition and
andresumed[17],[57].(iv)Highcoolingload:sustainedfull-
pre-processing: LLMs, which contain billions to hundreds
power operation of GPUs and supporting equipment produces
of billions of parameters, require massive training datasets
substantial heat, requiring cooling systems to operate at ele-
(often terabytes in size) that cover a broad range of content
vated capacity, which significantly increases total energy use.
and are collected from diverse sources such as Wikipedia
Electricity consumption during the training stage is affected
[51], CommonCrawl [52], BookCorpus [53], Reddit posts,
by many factors, such as AI model architecture and train-
GitHub codes, and other text datasets [1]. These raw datasets
ing configuration choices, such as batch size and numerical
must be cleaned and preprocessed into training-ready formats
precision requirements. Several strategies have been proposed
(e.g., tokenization, normalization, augmentation). The extract-
to improve training efficiency. For example, reference [58]
transform-load pipelines often rely on distributed computing
showedthatpower-capping,whichlimitsthemaximumpower
clusters that consume significant electricity during large-scale
a GPU can consume, enables a 15% decrease in energy usage
pre-processing [54]. Well-designed AI models and carefully
with a marginal increase in overall computation time. Other
processeddataarecriticaltothemodeltrainingefficiency.Em-
approaches include dynamically adjusting training parameters
pirical results in [55] show that data-centric approaches, such
based on convergence progress and implementing early stop-
as removing redundant samples from datasets or performing
ping when performance improvements plateau.
effective feature selection, can drastically reduce the energy
3) Fine-tuning Stage: The fine-tuning stage adapts a pre-
consumption of model training by more than 90%, underscor-
trained AI model to a specific downstream task [59], such as
ingtheimportanceofdevelopingGreenAI[55].Nevertheless,
legaltextanalysis,medicalreportsummarization,orcustomer
the preparation stage is flexible and widely dispersed, with
service chatbots. Since the AI model has already undergone
theworkloadsvaryingsubstantiallydependingonfactorssuch
extensive pre-training, fine-tuning typically requires substan-
as the choice of data processing libraries and tools [56], the
tially less computation and electricity than training from
deployment environment, and the workflow structure, making
scratch.Empiricalmeasurementsin[60]showthatpre-training
its electricity consumption difficult to quantify precisely.
BERT consumes electricity equivalent to approximately 400
2) TrainingStage: Thetrainingstageisthemostelectricity-
to 45,000 fine-tuning runs, depending on the dataset size and
intensive phase of AI development, particularly for LLMs.
task complexity. Nevertheless, as fine-tuning often involves
Duringthisprocess,computinghardwareoperatesatnear-peak
smaller datasets, frequent evaluation cycles, and hyperparam-
capacity for extended periods, which often runs continuously
eter tuning, power use tends to be more variable. Rather than
for days or weeks, resulting in a significant and sustained
maintaining a sustained high baseline, fine-tuning workloads
powerdraw.Forexample,trainingGPT-3isestimatedtohave
typically exhibit intermittent bursts of GPU utilization fol-
consumed 1.29 GWh of electricity [5]; this intensive process
lowed by lower activity periods.
involved approximately 14.8 days of continuous computation
Typical electricity use patterns during fine-tuning include:
on 10,000 NVIDIA V100 GPUs in a Microsoft data center
(i) moderate average demand, generally lower than full pre-
[5].Furthermore,trainingGPT-4requiredanestimatedover50
training but varying by model size and dataset; (ii) bursty
GWh of electricity, approximately 40 times more than GPT-3,
workloads, with short periods of high consumption during
and equivalent to nearly 0.02% of California’s annual elec-
forward/backward passes, validation, and hyperparameter ex-
tricity consumption1 [6], [7]. Similar LLMs, such as Meta’s
ploration; and (iii) cooling demand variability, with cooling
LLaMAseriesandGoogle’sGemini,requiretensofthousands
loads fluctuating in step with computational bursts. Although
of high-performance GPUs operating in parallel for training,
a single fine-tuning run consumes far less energy than pre-
training, its much higher frequency across numerous organi-
1OpenAI does not officially disclose the energy consumption data for
zations implies that fine-tuning can cumulatively represent a
trainingitsGPTmodels.Thefigurescitedareestimatesbasedonthird-party
analysisandresearch. non-negligibleshareoftotallifecycleenergyconsumption,un-

7
derscoringtheneedtoenhanceitsefficiency.Forexample,ref-
| erence [61]        | introduced  |                | GreenTrainer, |                  | an                 | adaptive    | fine-tuning     |         |     |     |     |     |     |     |     |
| ------------------ | ----------- | -------------- | ------------- | ---------------- | ------------------ | ----------- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| algorithm          | that        | strategically  |               | selects          | which              | model       | parameters      |         | to  |     |     |     |     |     |     |
| update.            | This method |                | reduces       | fine-tuning      |                    | workload    |                 | by up   | to  |     |     |     |     |     |     |
| 64% without        | significant |                | accuracy      |                  | loss, highlighting |             | the             | poten-  |     |     |     |     |     |     |     |
| tial to make       | fine-tuning |                | more          | energy-efficient |                    |             | [61]. Reference |         |     |     |     |     |     |     |     |
| [62] analyzes      |             | the trade-offs |               | between          | energy             | consumption |                 | and     |     |     |     |     |     |     |     |
| model performance, |             |                | showing       | that             | fine-tuning        |             | smaller         | models  |     |     |     |     |     |     |     |
| such as            | T5-base,    | BART-base,     |               | or               | LLaMA3-8B          |             | can             | achieve |     |     |     |     |     |     |     |
| competitive        | results     | while          | significantly |                  | reducing           |             | energy          | usage.  |     |     |     |     |     |     |     |
4) Inference Stage: Inference is the process of executing a Fig. 3. Illustration of the patterns of AI computing load (represented by
GPUpower)duringtraining,fine-tuning,andinferencestages.(Thedataare
| well-trained | AI  | model | to generate |     | outputs | in response |     | to user |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ----------- | --- | ------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
derivedfrom[16];refertoFigures9,13,15andTableIIIin[16]fordetailed
inputs.Onaper-querybasis,itistheleastelectricity-intensive dataandexperimentalsettings.)
| stage of     | the AI       | model | lifecycle. |           | Nevertheless, |         | as       | inference |     |     |     |     |     |     |     |
| ------------ | ------------ | ----- | ---------- | --------- | ------------- | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| is performed | continuously |       |            | at scale, | often         | serving | millions | or        |     |     |     |     |     |     |     |
billionsofrequests,itscumulativeelectricityconsumptioncan C. Summary and Discussion
exceed that of training. According to [63], compared to 40% AI computing load is highly energy-intensive, with each
fortraining,inferencerepresentsabout60%oftotalAIenergy stage of the workflow contributing differently to the total
usageatGoogle,owingtothebillion-userservicesthatrelyon
electricityconsumption.Accordingto[14],theinferencestage
AI. Recent estimates suggest inference can account for up to represents a dominant share of approximately 60% of the
90%ofamodel’stotallifecycleenergyuse[26].Theelectric-
|     |     |     |     |     |     |     |     |     | energy footprint, | while | training | accounts | for 30%, | and | model |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | -------- | -------- | -------- | --- | ----- |
ity consumption for a single AI inference query varies widely preparation and fine-tuning make up the remaining 10%.
depending on the model size and architecture, prompt length, Moreover, these stages exhibit distinct load patterns. Figure
| and task | complexity |     | [26]. | Compared | to  | a traditional |     | Google |               |             |              |          |           |     |      |
| -------- | ---------- | --- | ----- | -------- | --- | ------------- | --- | ------ | ------------- | ----------- | ------------ | -------- | --------- | --- | ---- |
|          |            |     |       |          |     |               |     |        | 3 illustrates | the typical | time-varying | electric | computing |     | load |
search, which consumes about 0.3 Wh [64], a recent study (measured by GPU power) patterns across different stages of
[26] estimates that GPT-o3 consumes 39.2 Wh, DeepSeek- theAIworkflow,excludingthedatapreparationstageduetoits
| R1 33.6 | Wh, | and GPT-4.5 |     | 30.5 | Wh for | processing |     | a long |     |     |     |     |     |     |     |
| ------- | --- | ----------- | --- | ---- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
typicallydispersedenergyusage.Theelectricityloadestimates
prompt query, whereas GPT-4.1 Nano requires only 0.45 Wh. for each stage are derived from [16], where the tasks were
Reference[65]comparesinferenceenergyconsumptionacross
|     |     |     |     |     |     |     |     |     | executed | using GPT-2. | Additional | experimental |     | details | are |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ---------- | ------------ | --- | ------- | --- |
a wide range of tasks and shows that image generation is available in [16]. As shown in Figure 3, all stages exhibit an
amongthemostenergy-intensive,whereassimplertasks,such initial rapid ramp-up phase, during which power consumption
| as text classification, |     |     | consume | significantly |     | less | electricity. |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------- | ------------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
risessharplyfromalow(near-zero)valuetoahighoperational
Unlike the sustained, high load profile of model training, level. In the training stage, power remains consistently high,
| inference | workloads |     | are characterized |     | by  | significant |     | variabil- |               |                 |       |       |      |               |     |
| --------- | --------- | --- | ----------------- | --- | --- | ----------- | --- | --------- | ------------- | --------------- | ----- | ----- | ---- | ------------- | --- |
|           |           |     |                   |     |     |             |     |           | characterized | by intermittent | large | rapid | load | fluctuations, |     |
ity. This is driven by fluctuating user requests, diverse query along with persistent high-frequency, small-scale variations,
complexities, and the unpredictable nature of real-time inter- the magnitude of which depends on the underlying hardware
| actions, | resulting | in  | short, | intense | bursts | of computing |     | load. |              |            |           |             |     |       |        |
| -------- | --------- | --- | ------ | ------- | ------ | ------------ | --- | ----- | ------------ | ---------- | --------- | ----------- | --- | ----- | ------ |
|          |           |     |        |         |        |              |     |       | and training | algorithms | [16]. The | fine-tuning |     | stage | begins |
As a result, typical electricity use patterns in the inference withpronouncedhigh-frequency,large-magnitudefluctuations,
| stage include: |     | (i) low | average | demand |     | per | query | but high |                 |          |              |     |      |       |          |
| -------------- | --- | ------- | ------- | ------ | --- | --- | ----- | -------- | --------------- | -------- | ------------ | --- | ---- | ----- | -------- |
|                |     |         |         |        |     |     |       |          | which gradually | decrease | in frequency |     | over | time; | however, |
total demand over time due to continuous operation; (ii) moderatefluctuationscontinuethroughouttheprocess.Incon-
burstyandunpredictablespikesfromuseractivityandvarying trast, the inference stage operates over much shorter durations
| task complexity; |     | and | (iii) strong |     | diurnal | patterns, | with | peak |              |                 |       |        |     |       |         |
| ---------------- | --- | --- | ------------ | --- | ------- | --------- | ---- | ---- | ------------ | --------------- | ----- | ------ | --- | ----- | ------- |
|                  |     |     |              |     |         |           |      |      | and exhibits | highly variable | short | bursts | of  | power | demand, |
usage during business or social activity hours. Supporting drivenbythestochasticnatureofreal-timeinferencerequests.
| such dynamic |     | loads | necessitates | scalable |     | and | flexible | IT and |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ------------ | -------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Thisdiversityinloadprofilesunderscoresthecriticalneedfor
power infrastructure capable of rapidly adjusting resources advanced AI data center designs, grid integration strategies,
to provide fast response and maintain operational reliability. andpower-awareworkloadschedulingapproachesthatbalance
| Energy   | efficiency | can         | be improved |           | at both | the          | hardware | and     |              |                 |     |        |              |     |     |
| -------- | ---------- | ----------- | ----------- | --------- | ------- | ------------ | -------- | ------- | ------------ | --------------- | --- | ------ | ------------ | --- | --- |
|          |            |             |             |           |         |              |          |         | performance, | sustainability, | and | system | reliability. |     |     |
| software | levels.    | Specialized |             | low-power |         | accelerators |          | such as |              |                 |     |        |              |     |     |
FPGAsandASICs[66]canreduceenergyconsumption,while
|            |      |       |               |     |          |     |               |     | IV. GRIDIMPACTSANDEMERGINGCHALLENGESOFAI |     |     |     |     |     |     |
| ---------- | ---- | ----- | ------------- | --- | -------- | --- | ------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| techniques | like | model | quantization, |     | pruning, |     | and knowledge |     |                                          |     |     |     |     |     |     |
DATACENTERS
| distillation | further | enhance |     | performance |     | [67], | [68]. Emerging |     |     |     |     |     |     |     |     |
| ------------ | ------- | ------- | --- | ----------- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
architectures such as retrieval augmented generation (RAG) The rapid expansion of large-scale AI data centers is im-
[69] introduce additional complexity by combining model posing unprecedented demands on electric power grids. With
inferencewithlarge-scaledataretrievalprocesses.Despitethe immense electricity consumption subject to large and fast
exponentialgrowthinmodelparameters,theassociatedenergy fluctuations, these facilities introduce emerging impacts and
cost of inference has been shown to grow sub-linearly, sug- operational challenges for power grids. This section analyzes
gesting that efficiency gains can partially offset the demands thesechallengesacrossthreeinterrelatedtimescales,including
of larger architectures [70]. long-term planning and interconnection, short-term operation

8
andmarket,andreal-timegriddynamicsandstability,illustrat- underexplored. Another key strategy is the co-location with
ing how AI data center loads affect each phase of power grid dedicated local generation, such as renewable generators
management. Other critical challenges, such as cybersecurity, and nuclear power plants. This scheme can directly supply
decarbonization, and water resources, are discussed as well. large stable power sources to high-demand AI workloads,
reducingrelianceonlong-distanceelectricitytransmissionand
|              |           |            |                     |        |              |         | mitigating   | grid-integration |       |           | challenges. |       | For example, |                 | Amazon |
| ------------ | --------- | ---------- | ------------------- | ------ | ------------ | ------- | ------------ | ---------------- | ----- | --------- | ----------- | ----- | ------------ | --------------- | ------ |
| A. Long-Term | Planning  |            | and Interconnection |        |              |         |              |                  |       |           |             |       |              |                 |        |
|              |           |            |                     |        |              |         | Web Services |                  | (AWS) | has       | arranged    | to    | source       | approximately   |        |
| Over the     | long-term | timescales |                     | (years | to decades), | AI data |              |                  |       |           |             |       |              |                 |        |
|              |           |            |                     |        |              |         | 960 MW       | directly         | from  | a nuclear |             | power | plant        | in Pennsylvania |        |
centersareprojectedtodriveasustainedincreaseinelectricity to power its data center under a dedicated power purchase
| demand, requiring |                 | substantial | investment |              | in generation | capac- |           |       |             |     |           |     |           |      |          |
| ----------------- | --------------- | ----------- | ---------- | ------------ | ------------- | ------ | --------- | ----- | ----------- | --- | --------- | --- | --------- | ---- | -------- |
|                   |                 |             |            |              |               |        | agreement | [76]. | Google      | and | Kairos    |     | Power     | have | signed a |
| ity, transmission | infrastructure, |             | and        | distribution | equipment     |        | to        |       |             |     |           |     |           |      |          |
|                   |                 |             |            |              |               |        | Master    | Plant | Development |     | Agreement |     | to deploy | a    | fleet of |
maintainanadequateandreliableelectricitysupply.According
|            |        |             |             |     |             |         | advanced | small       | modular | reactors |     | to provide |         | up to 500 | MW  |
| ---------- | ------ | ----------- | ----------- | --- | ----------- | ------- | -------- | ----------- | ------- | -------- | --- | ---------- | ------- | --------- | --- |
| to the IEA | report | [8], global | electricity |     | consumption | by data |          |             |         |          |     |            |         |           |     |
|            |        |             |             |     |             |         | of clean | electricity | to      | Google’s | AI  | data       | centers | [77].     |     |
centers is projected to more than double by 2030, reaching Inaddition,thegridinterconnectionpoliciesandregulatory
approximately945TWh,withAIworkloadsexpectedtobethe
|                |     |              |          |     |               |       | frameworks | remain |             | among | the | most     | significant | bottlenecks |       |
| -------------- | --- | ------------ | -------- | --- | ------------- | ----- | ---------- | ------ | ----------- | ----- | --- | -------- | ----------- | ----------- | ----- |
| primary driver | of  | this growth. | However, |     | many regional | grids |            |        |             |       |     |          |             |             |       |
|                |     |              |          |     |               |       | to AI data | center | deployment. |       | For | example, |             | in 2025,    | Texas |
areincapableofaccommodatinglarge-scaledatacenterswith-
|               |              |     |                  |     |           |       | passed        | Senate | Bill    | 6 (SB-6)  | [78],      | which | redefines |      | the in- |
| ------------- | ------------ | --- | ---------------- | --- | --------- | ----- | ------------- | ------ | ------- | --------- | ---------- | ----- | --------- | ---- | ------- |
| out extensive | transmission |     | and distribution |     | upgrades, | which |               |        |         |           |            |       |           |      |         |
|               |              |     |                  |     |           |       | terconnection |        | process | for large | electrical |       | loads,    | such | as data |
oftenrequire5-10yearsforplanning,permitting,andconstruc- centersexceeding75MW,withintheERCOTgrid.Underthis
| tion [22], | [71]. Reference |     | [22] assessed | the | 5-year | projections |     |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | ------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bill,largeloadcustomersmustsubmitinterconnectionrequests
| of AI data-center | demand            |     | across      | several | bulk power     | grids and |             |                     |     |            |         |            |           |      |           |
| ----------------- | ----------------- | --- | ----------- | ------- | -------------- | --------- | ----------- | ------------------- | --- | ---------- | ------- | ---------- | --------- | ---- | --------- |
|                   |                   |     |             |         |                |           | through     | the interconnecting |     |            | utility | and        | comply    | with | new re-   |
| found that        | resource-adequacy |     | constraints |         | could severely | limit     |             |                     |     |            |         |            |           |      |           |
|                   |                   |     |             |         |                |           | quirements, | including           |     | disclosure |         | of similar | requests, |      | reporting |
theirplannedgrowth,particularlyinhigh-densityclusterssuch
|     |     |     |     |     |     |     | of on-site | backup | generation, |     | payment |     | of a minimum |     | $100k |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | ------- | --- | ------------ | --- | ----- |
as EirGrid in Ireland and Dominion in the U.S. Moreover, transmission screening study fee, proof of site control, and
| AI data centers | tend | to         | concentrate | in        | a limited | number of |                |            |            |     |                |              |            |                |         |
| --------------- | ---- | ---------- | ----------- | --------- | --------- | --------- | -------------- | ---------- | ---------- | --- | -------------- | ------------ | ---------- | -------------- | ------- |
|                 |      |            |             |           |           |           | a financial    | commitment |            | to  | cover          | transmission |            | infrastructure |         |
| regions, driven | by   | low energy | prices,     | available | land      | and water |                |            |            |     |                |              |            |                |         |
|                 |      |            |             |           |           |           | costs. Complex |            | regulatory |     | and permitting |              | workflows, |                | lengthy |
resources,andsupportivepolicyenvironments.Forexample,in
|     |     |     |     |     |     |     | grid integration |     | studies, | overloaded |     | interconnection |     |     | queues, |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---------- | --- | --------------- | --- | --- | ------- |
theU.S.,fifteenstates(notablyVirginia,Texas,andCalifornia)
andtheneedformajorgridinfrastructureupgradesarecausing
| accounted     | for an | estimated | 80%         | of the   | national             | data center |            |           |          |             |                |             |                 |               |         |
| ------------- | ------ | --------- | ----------- | -------- | -------------------- | ----------- | ---------- | --------- | -------- | ----------- | -------------- | ----------- | --------------- | ------------- | ------- |
|               |        |           |             |          |                      |             | multiyear  | delays    | in       | data center |                | deployments |                 | across        | regions |
| load in 2023  | [14],  | as shown  | in          | Figure   | 4. This geographical |             |            |           |          |             |                |             |                 |               |         |
|               |        |           |             |          |                      |             | such as    | Northern  | Virginia |             | [79]. Refining |             | interconnection |               | pro-    |
| concentration | effect | further   | intensifies | regional | grid                 | stress.     |            |           |          |             |                |             |                 |               |         |
|               |        |           |             |          |                      |             | cesses and | deploying |          | AI and      | automation     |             | tools           | to accelerate |         |
interconnectionstudiescouldsignificantlyreducethesedelays.
|     |     |     |     |     |     |     | Moreover, | tariff | structure |     | varies | across | jurisdictions: |     | many |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --------- | --- | ------ | ------ | -------------- | --- | ---- |
datacentersfallundersmallerregionalutilitiesandaresubject
|     |     |     |     |     |     |     | to distribution-level |     | tariffs, |     | while | hyperscale | facilities |     | connect |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | -------- | --- | ----- | ---------- | ---------- | --- | ------- |
directlytobulktransmissionsystems,exposingthemtowhole-
|     |     |     |     |     |     |     | sale market       | price      | signals.     |            | As a        | result,      | the tariff          | design      | and     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ------------ | ---------- | ----------- | ------------ | ------------------- | ----------- | ------- |
|     |     |     |     |     |     |     | standardization   |            | are critical |            | to ensuring |              | cost predictability |             | and     |
|     |     |     |     |     |     |     | sustaining        | the        | deployment   |            | of AI       | data centers |                     | [80], [81]. |         |
|     |     |     |     |     |     |     | B. Short-Term     |            | Operation    | and        | Electricity |              | Markets             |             |         |
|     |     |     |     |     |     |     | On the            | short-term |              | timescales | (hourly     |              | to weekly),         | the         | large-  |
|     |     |     |     |     |     |     | scale integration |            | of AI        | data       | center      | loads        | (ranging            | from        | tens to |
hundredsofmegawatts)introducessubstantialoperationaland
Fig.4. ThefifteenU.S.stateswiththehighestdatacenterloadsin2023[14]
|     |     |     |     |     |     |     | market challenges |     | to  | the power | grid. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --------- | ----- | --- | --- | --- | --- |
(darkercolorsindicatehigherloads).
|     |     |     |     |     |     |     | 1) Impacts |     | on Power | Dispatch |     | and | Reserve | Scheduling: |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | -------- | --- | --- | ------- | ----------- | --- |
To address this challenge, coordinated co-planning of AI Maintaining the balance between generation and demand is
datacenters,thepowergrid,andgenerationscanreducecostly a fundamental objective of power system operation. On the
infrastructure investments, alleviate transmission congestion, short-term timescale, power balance is achieved through unit
enhance operational reliability, and support decarbonization commitment (UC) and economic dispatch (ED), supported
goals. This approach integrates transmission and distribution by reserve scheduling to accommodate unforeseen power
expansion planning with the strategic siting of AI data cen- variations [82]. The immense and bursty power usage of
ters, as well as the optimal siting and sizing of additional AI data centers, particularly during intensive model training
generation and energy storage resources. A number of studies and large-scale inference, introduces significant uncertainty
[72]–[75] focus on the modeling and optimization of joint and rapid load variations to the grid operation [17]. This
planning for conventional data centers and the power grid, challengesconventionaldeterministicpowerdispatchschemes
while solutions tailored to AI data centers remain largely and necessitates advanced short-term forecasting techniques

9
for AI data center loads [17], [83]. However, accurate pre- 5 illustrates the grid frequency dynamics under several large
diction remains inherently difficult due to their complex, electronic load trip events studied in ERCOT [93]. It shows
non-cyclic patterns and dynamic scheduling behaviors of AI that the loss of more than 2600 MW of such loads can
workloads. In addition, the rapid and unpredictable ramping drive system frequency up to 60.4 Hz, a level at which
of AI data center loads imposes greater reserve requirements. conventional generators may fail to ride through, potentially
To ensure reliability amid large and fast load variations, grid leading to uncontrolled cascading events [93]. To this end,
operatorsneedtomaintainelevatedspinningandnon-spinning ERCOT considered imposing ride-through requirements for
reserve margins, which increase operational costs and call for large data center and crypto-mining loads [94] to ensure
additional fast-responding reserve resources. reliable interconnection and grid operation.
| 2) Impacts  | on           | Electricity | Market   | and | Price:       | Large-scale |          |     |     |     |     |     |     |
| ----------- | ------------ | ----------- | -------- | --- | ------------ | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| AI data     | center loads | are         | expected | to  | place upward |             | pressure |     |     |     |     |     |     |
| on capacity | market       | clearing    | prices,  | as  | higher       | peak        | demands  |     |     |     |     |     |     |
requireadditionalcapacitycommitments.Thisimpacthasbeen
| observed      | in PJM,      | where    | capacity    | market       | clearing       | prices      | for     |               |        |           |                     |       |                 |
| ------------- | ------------ | -------- | ----------- | ------------ | -------------- | ----------- | ------- | ------------- | ------ | --------- | ------------------- | ----- | --------------- |
| the 2026-2027 | delivery     | year     | increased   |              | to $329.17/MW, |             | over    |               |        |           |                     |       |                 |
| ten times     | higher       | than the | price       | of $28.92/MW |                | in the      | 2024-   |               |        |           |                     |       |                 |
| 2025 delivery | year,        | with     | rapid       | data center  | growth         | identified  |         |               |        |           |                     |       |                 |
| as a major    | contributing |          | factor      | [84], [85].  | Similar        | effects     | are     |               |        |           |                     |       |                 |
| emerging      | in New       | York     | ISO and     | ERCOT,       | where          | anticipated |         |               |        |           |                     |       |                 |
|               |              |          |             |              |                |             |         | Fig. 5. ERCOT | system | frequency | response to several | large | electronic load |
| data center   | expansion    | is       | influencing | forward      | capacity       |             | markets |               |        |           |                     |       |                 |
tripevents[93].
| and resource | adequacy | planning |     | [86], | [87]. | In addition, | the |          |              |     |                     |     |     |
| ------------ | -------- | -------- | --- | ----- | ----- | ------------ | --- | -------- | ------------ | --- | ------------------- | --- | --- |
|              |          |          |     |       |       |              |     | 2) Power | Fluctuations |     | and Grid Stability: |     |     |
substantial and often unpredictable demand from AI data AI data centers
centers raises marginal generation costs in wholesale markets, can introduce rapid power fluctuations during cold starts,
asmoreexpensivemid-meritandpeakingunitsaredispatched planned shutdowns, workload transitions, or sudden load in-
to meet AI-driven loads [14]. It also amplifies price volatility terruptions triggered by faults or operational contingencies.
inday-aheadandreal-timemarketsduetoshort-termlargeAI For example, training large-scale AI models across tens of
|     |     |     |     |     |     |     |     | thousands | of GPUs | can | induce significant | power | swings, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | ------------------ | ----- | ------- |
loadfluctuations[88].RapidAIloadsurgescanresultinsharp
increases in locational marginal prices (LMPs), particularly in arising from the synchronous nature of these jobs and the
transmission-congested areas [89]. alternationbetweenapower-intensivecomputationphaseanda
lesspower-demandingcommunicationphase[18].Inaddition,
|              |          |     |          |           |     |     |     | inference  | workloads | often    | exhibit rapid | “start-stop” | behavior   |
| ------------ | -------- | --- | -------- | --------- | --- | --- | --- | ---------- | --------- | -------- | ------------- | ------------ | ---------- |
| C. Real-Time | Dynamics |     | and Grid | Stability |     |     |     |            |           |          |               |              |            |
|              |          |     |          |           |     |     |     | with sharp | spikes    | followed | by sudden     | drops in     | power con- |
In real-time and fast timescales (sub-seconds to minutes), sumption, as shown in Figure 3. Unlike conventional elec-
large-scaleAIdatacenterloadscansignificantlyimpactpower tromechanical loads, power electronics-based AI data center
system dynamics and stability. These facilities are inherently demand may change by tens to hundreds of megawatts within
power electronics-based loads, with their dynamic behavior sub-second intervals, posing substantial stability risks to the
governedbythecontrolofinternalpowerelectronicconverters power grid. Such abrupt power variations can challenge the
and by the computational workload scheduling dynamics. grid’s frequency stability [95], [96], induce voltage excur-
1) Grid Disturbances Ride-Through: AI data centers in- sions [97], and interact with the dynamics of grid-connected
terface with the power grid through high-capacity power elec- generation and control systems, potentially exciting oscilla-
tronicconverters,whicharesensitivetoshort-durationvoltage tionsandinstability[98].Forinstance,amajorresonanceevent
and frequency disturbances at the point of interconnection, was reported in 2017 across multiple Facebook data centers
such as voltage sags, voltage dips, and upward or downward andanalyzedin[99].Asnotedin[100],unlikesolarplantsand
frequency deviations. These disturbances can induce substan- wind farms, data centers typically have internal impedances
tialpoweroscillationsandeventriggerthedisconnectionofan much higher than those of transmission lines or distribution
AI data center from the grid to protect internal electronic de- transformers, which can amplify such resonance phenomena.
vices. Without adequate fault ride-through (FRT) capabilities From a data center perspective, reference [18] proposes three
or grid disturbance-tolerance measures, such sudden trips can classes of power stabilization techniques to mitigate large
occur during grid faults, potentially exacerbating the original powerswings,including(i)software-basedmethodsthatinject
grid disturbance. In regions with high concentrations of AI controlled workloads to smooth power transitions, (ii) GPU-
data centers, simultaneous tripping events can take place and level firmware mechanisms that enforce ramping constraints
lead to cascading outages [90]. These impacts have been and power floors, and (iii) rack-level energy storage systems
observed in practice. For example, high-frequency undamped to reduce fluctuations by absorbing and releasing power as
power oscillations appeared in a data center-rich region in needed. Beyond these approaches, addressing the challenge
DominionEnergy’sgrid,triggeredbyaonce-a-secondvoltage of large power fluctuations also requires accurate dynamic
sag [91]. ERCOT has also reported multiple events wherein modeling of AI data center behavior and close coordination
largecomputingloadstrippedduringtransmissionfaultsdueto between grid operators and data center operators to ensure
insufficient ride-through capability [92]. For example, Figure effectivemitigationandmaintainsystem-levelstability.More-

10
over,asdatacenterstypicallyemployfast-actingUPSsystems frequency regulation, and triggering cascading failures across
forpowercontinuity,transitionsbetweengridsupplyandUPS interconnected systems [104]. For instance, in 2024, a large-
operation during disturbances must be carefully managed to scale disconnection event occurred in Virginia’s “Data Center
preventlargetransientpowerswingsorsynchronizationissues Alley”, where a protection system failure caused 60 out of
upon reconnection. more than 200 data centers to suddenly disconnect from the
3) PowerQualityIssues: High-frequencyswitchingdevices gridandtransitiontoon-sitegenerators[105].Thisabruptloss
and power electronic equipment in data centers can introduce of load introduced a significant power imbalance, compelling
significant harmonic distortions to the grid, degrading local the utility to rapidly curtail generation in order to avert
|               |     |        |       |           |            |            |     | cascading | outages. | Although |     | the event | was | not | triggered by |
| ------------- | --- | ------ | ----- | --------- | ---------- | ---------- | --- | --------- | -------- | -------- | --- | --------- | --- | --- | ------------ |
| power quality | and | posing | risks | to nearby | electrical | facilities |     |           |          |          |     |           |     |     |              |
[101]. These distortions originate primarily from non-linear malicious cyber attacks, it underscores how sudden shifts in
power supplies, AC/DC conversions, and the control of server datacenterloadscanimposesubstantialstressongridstability.
PFC circuits [102]. In large-scale AI facilities, where thou- Beyond transient disturbances, maliciously orchestrated or
sands of server racks operate simultaneously, these harmonics malfunction-induced workload patterns can act as sources of
can accumulate and propagate into the local distribution sys- forced oscillations, periodically modulating AI data center
tem, presenting risks to industrial and residential equipment, demand in ways that resonate with the grid’s natural modes.
suchasmalfunctions,acceleratedwear,overheating,andelec- Such oscillatory injections can amplify inter-area oscilla-
trical fires. According to a 2024 Bloomberg analysis [21], tions, reduce damping margins, and in extreme cases, trigger
sensor data from more than 700,000 homes reveal a strong widespread instability [106]. Unlike conventional industrial
| correlation | between | proximity |     | to data | centers | and declining |     |            |          |                 |     |     |                     |     |     |
| ----------- | ------- | --------- | --- | ------- | ------- | ------------- | --- | ---------- | -------- | --------------- | --- | --- | ------------------- | --- | --- |
|             |         |           |     |         |         |               |     | loads, the | inherent | controllability |     |     | and programmability |     | of  |
power quality, with evident effects observed within 20 miles AI workloads render them particularly susceptible to being
of major data center clusters. Beyond harmonic distortion, exploitedasvirtualpowerperturbationsources.Thistightcou-
AI data centers may contribute to other power quality issues, pling between cyber-level control and physical load response
such as voltage flicker during rapid load changes, unbalanced highlights the urgent need for integrated approaches that
| loads across | three | phases | [97], | inter-harmonics |     | caused | by  |                 |     |               |     |       |        |           |     |
| ------------ | ----- | ------ | ----- | --------------- | --- | ------ | --- | --------------- | --- | ------------- | --- | ----- | ------ | --------- | --- |
|              |       |        |       |                 |     |        |     | jointly address |     | cybersecurity | and | power | system | dynamics. | Ef- |
certain switching patterns in high-frequency converters [103]. fective countermeasures include the implementation of secure
These power quality issues can propagate through the grid, communication protocols, the development of anomaly de-
potentiallydegradingprotectionsystemperformance,reducing tection mechanisms tailored to workload-induced oscillations,
metering accuracy, shortening equipment lifespans, and im- and the establishment of collaborative frameworks between
pairingcontrolsystemstability[97].Tomitigatepowerquality
|     |     |     |     |     |     |     |     | data center | operators |     | and grid | utilities | to  | prevent | cascading |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | -------- | --------- | --- | ------- | --------- |
issues and maintain compliance with industry standards such failures triggered via cyber attacks.
| as IEEE | Standard | 519-2014 |     | [102], key | approaches | include: |     |                     |     |     |           |     |         |        |           |
| ------- | -------- | -------- | --- | ---------- | ---------- | -------- | --- | ------------------- | --- | --- | --------- | --- | ------- | ------ | --------- |
|         |          |          |     |            |            |          |     | 2) Decarbonization: |     |     | According | to  | the IEA | report | [8], car- |
(i)activeharmonicfilteringattheAIdatacenterfacilities,(ii) bon emissions from the electricity use of global data centers
phase balancing and load redistribution to minimize neutral reached 180 million tonnes (Mt) in 2024 and are projected to
| current distortion, |     | (iii) | coordination | with | grid | operators | for |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----- | ------------ | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
riseto300Mtby2035,raisingconcernsthattherapidgrowth
harmonic monitoring and mitigation planning, and (iv) UPS of AI facilities could further exacerbate climate change [107].
| and converter | design | optimization |     | to minimize |     | harmonic | gen- |               |     |      |         |           |     |             |        |
| ------------- | ------ | ------------ | --- | ----------- | --- | -------- | ---- | ------------- | --- | ---- | ------- | --------- | --- | ----------- | ------ |
|               |        |              |     |             |     |          |      | Nevertheless, | AI  | data | centers | generally | do  | not produce | direct |
eration at the source. As AI data center capacity keeps ex- carbon emissions during normal operation, apart from on-site
panding, proactive power quality management will be critical backup generators such as diesel units, which are only infre-
| for maintaining |     | grid stability |     | and ensuring | equipment |     | safety |         |            |          |     |              |     |        |             |
| --------------- | --- | -------------- | --- | ------------ | --------- | --- | ------ | ------- | ---------- | -------- | --- | ------------ | --- | ------ | ----------- |
|                 |     |                |     |              |           |     |        | quently | activated. | Instead, | AI  | data centers |     | mainly | account for |
and regulatory compliance. the indirect carbon footprint2 associated with their electricity
|                   |                  |            |       |                  |            |         |         | consumption,   | with          | the                 | carbon    | emission     | intensities |         | determined  |
| ----------------- | ---------------- | ---------- | ----- | ---------------- | ---------- | ------- | ------- | -------------- | ------------- | ------------------- | --------- | ------------ | ----------- | ------- | ----------- |
|                   |                  |            |       |                  |            |         |         | by the         | generation    | fuel                | mix       | and electric |             | power   | flow of the |
| D. Other          | Critical         | Challenges |       |                  |            |         |         |                |               |                     |           |              |             |         |             |
|                   |                  |            |       |                  |            |         |         | supplying      | power         | grid                | [110];    | see [111]    | for         | a more  | detailed    |
| This subsection   |                  | discusses  | other | critical         | challenges |         | arising |                |               |                     |           |              |             |         |             |
|                   |                  |            |       |                  |            |         |         | introduction.  | Consequently, |                     | the       | coupling     |             | between | electricity |
| from the          | rapid expansion  |            | of AI | data centers,    | including  |         | cyber-  |                |               |                     |           |              |             |         |             |
|                   |                  |            |       |                  |            |         |         | demand         | and grid      | carbon              | intensity | highlights   |             | the     | importance  |
| security,         | decarbonization, |            | and   | water resources. |            |         |         |                |               |                     |           |              |             |         |             |
|                   |                  |            |       |                  |            |         |         | of considering |               | both                | energy    | efficiency   | measures    |         | within AI   |
| 1) Cybersecurity: |                  | AI         | data  | centers not      | only       | present | major   |                |               |                     |           |              |             |         |             |
|                   |                  |            |       |                  |            |         |         | data centers   | and           | the decarbonization |           |              | trajectory  | of      | power grids |
physical impacts on the power grid, as discussed above, but [112]. At present, data center owners achieve their decar-
| also introduce | emerging     |     | cybersecurity | risks   | to  | power systems. |     |            |       |           |     |             |     |           |         |
| -------------- | ------------ | --- | ------------- | ------- | --- | -------------- | --- | ---------- | ----- | --------- | --- | ----------- | --- | --------- | ------- |
|                |              |     |               |         |     |                |     | bonization | goals | primarily | by  | co-locating |     | renewable | genera- |
| Their highly   | concentrated |     | electricity   | demand, |     | dependence     | on  |            |       |           |     |             |     |           |         |
tionwithdatacentercampusesorthroughprocuringrenewable
| programmable | power | electronics, |     | and integration |     | with | cloud- |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------------ | --- | --------------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
energyintheelectricitymarketviapowerpurchaseagreements
basedcontrolarchitecturescollectivelyincreasethevulnerabil-
|     |     |     |     |     |     |     |     | (PPAs) | [113] or | renewable | energy |     | certificates | (RECs) | [114]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | ------ | --- | ------------ | ------ | ------ |
ityofpowersystemstocyberattacks.Specifically,coordinated For example, Google launched its “24/7 Carbon-Free Energy”
| cyber intrusions |     | could | manipulate | workload |     | scheduling | or  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | ---------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
program[115]aimedatsourcingcarbon-freeelectricityforits
| UPS switching, |      | deliberately  | inducing | sudden        | surges  | or         | drops  |                |     |            |       |             |          |                |               |
| -------------- | ---- | ------------- | -------- | ------------- | ------- | ---------- | ------ | -------------- | --- | ---------- | ----- | ----------- | -------- | -------------- | ------------- |
| of hundreds    | of   | megawatts     | in       | power demand. |         | Such       | abrupt |                |     |            |       |             |          |                |               |
|                |      |               |          |               |         |            |        | 2Accordingly,  | the | Greenhouse | Gas   | (GHG)       | Protocol | [108],         | [109] defines |
| load changes   | pose | a significant |          | threat        | to grid | stability, | po-    |                |     |            |       |             |          |                |               |
|                |      |               |          |               |         |            |        | two categories | of  | emissions, | Scope | 1 and Scope | 2,       | to distinguish | between       |
tentially overloading local distribution networks, disrupting directandindirect(orattributed)emissionsforcarbonaccounting.

11
data center operations on a continuous 24 hours-7 days time concerns, load forecasting can be performed internally by
basis for decarbonization. AI data centers, while only aggregated results are reported
3) Water Resources: Many large-scale data centers utilize to the grid operator. Alternatively, collaborative forecasting
frameworks,whereAIdatacenteroperatorsshareanonymized
| evaporative | cooling | systems | to dissipate | heat, | a process | that |     |     |     |     |     |     |
| ----------- | ------- | ------- | ------------ | ----- | --------- | ---- | --- | --- | --- | --- | --- | --- |
consumessubstantialvolumesofwaterdaily,oftenamounting workload information with grid operators, can be developed
to tens of thousands or even millions of liters of water to enhance situational awareness and support preventive grid
depending on the facility size and climate conditions. As operations that mitigate potential impacts. As a complement,
indicated in report [8], a 100 MW data center in the U.S. recent advances in machine learning (ML) techniques can be
on average consumes around 2 million liters of water per leveraged to enhance AI load forecasting [17], [120]. These
day, equivalent to about 6,500 households. It estimates that approachesintegratetelemetrydatafromITinfrastructure,job
global water consumption for data centers is currently around queue statistics, and environmental factors with advanced ML
560 billion liters per year and could rise to around 1,200 tools to predict short-term fluctuations and identify potential
billion liters per year in 2030. As a consequence, together peak demand events before they occur. For example, hybrid
withhighelectricitydemand,substantialwaterwithdrawalsare statistical-ML models have been shown to improve short-
emerging as a critical limiting factor for AI-driven data center termpredictionaccuracyforcloudandAIcomputingfacilities
expansion, especially during summer peaks when both water compared to conventional auto-regressive models [83].
availability and power supply are under stress. According to 2) Dynamics Modeling of AI Data Centers: High-fidelity
Bloomberg [116], nearly two-thirds of new U.S. data centers modelingoftheelectricaldynamicsofAIdatacenterfacilities
built since 2022 are located in high water-stress regions, such is essential for assessing their grid disturbance ride-through
as the Southwest, Texas, and parts of the Midwest, some capabilities and their interactions with power system stability.
of which face growing risks of drought and water scarcity. As inherently power electronics-based loads, AI data centers
Reference [117] proposes a general framework for evaluating exhibit dynamic behavior governed by internal power con-
the water impact of computing by factoring in both spatial verter controls and the temporal characteristics of computa-
and temporal variations in water stress. In [118], the factors tional workload processing. Hence, electromagnetic transient
influencing data center water use are analyzed, such as server (EMT) modeling, using tools such as EMTP or PSCAD, is
efficiency,serverutilization,andcoolingtechniques.Thestudy required for capturing the fast, high-frequency responses of
also finds that there is no single recipe for minimizing water these AI facilities, which may not be accurately represented
use; instead, optimal outcomes depend on tailored combina- by conventional phasor-domain models [121], [122]. A recent
tions of these factors. To reduce stress on water resources, dynamic load model tailored for AI data centers is proposed
integrated planning frameworks that jointly assess electricity in [123] that incorporates three key features, including an
andwaterfootprintsofAIdatacentersarenecessary.Effective upstream UPS, cooling loads represented by induction motor
strategies include adopting low-water cooling technologies in dynamics,andpulsingcomputeloadstorepresentAIworkload
water-scarce regions, siting facilities with attention to both transients. Complementary approaches include hierarchical
water availability and grid capacity, and incorporating climate and hybrid modeling frameworks that combine high-fidelity
resilience metrics into future AI infrastructure planning. EMT simulations for critical components with reduced-order
|     |     |     |     |     |     |     | equivalents | for external | network | regions. | This method | bal- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------- | -------- | ----------- | ---- |
ancescomputationalefficiencywithaccuracy,enablingreliable
V. POTENTIALSOLUTIONSANDOPPORTUNITIES
|                  |            |                   |                |               |     |          | simulation  | of real-world | grid     | impacts | from AI data | center    |
| ---------------- | ---------- | ----------------- | -------------- | ------------- | --- | -------- | ----------- | ------------- | -------- | ------- | ------------ | --------- |
| In addition      | to         | the approaches    | discussed      | in Section    |     | IV, this |             |               |          |         |              |           |
|                  |            |                   |                |               |     |          | behavior    | [124], [125]. |          |         |              |           |
| section presents |            | further solutions | and            | opportunities | to  | address  |             |               |          |         |              |           |
|                  |            |                   |                |               |     |          | 3) Tailored | Demand        | Response | Program | Design:      | To effec- |
| the challenges   | associated |                   | with the rapid | integration   | of  | AI data  |             |               |          |         |              |           |
tivelyharnesstheflexibilityofAIdatacenterswhileminimiz-
| centers,    | considered | from | three perspectives: | the | power | grid, |                 |             |          |                |          |        |
| ----------- | ---------- | ---- | ------------------- | --- | ----- | ----- | --------------- | ----------- | -------- | -------------- | -------- | ------ |
|             |            |      |                     |     |       |       | ing adverse     | operational | impacts, | grid operators | needto   | design |
| the AI data | centers,   | and  | the AI end-users.   |     |       |       |                 |             |          |                |          |        |
|             |            |      |                     |     |       |       | demand response | (DR)        | programs | specifically   | tailored | to the |
uniquecharacteristicsoftheseloads.Standardprice-basedDR
| A. Solutions | on  | Power Grid | Side |     |     |     |             |       |        |                     |     |            |
| ------------ | --- | ---------- | ---- | --- | --- | --- | ----------- | ----- | ------ | ------------------- | --- | ---------- |
|              |     |            |      |     |     |     | mechanisms, | while | widely | used in residential | and | industrial |
1) ImprovingForecastingofAILoad: Accurateforecasting contexts,mayintroducenewchallengeswhenapplieddirectly
of AI data center loads, particularly during large-scale model tolarge-scaleAIloads.Forinstance,inferenceortrainingtasks
training and inference stages, is critical for grid planning deferredinresponsetohighelectricitypricesmayberesched-
and operation. Unlike traditional data center loads, AI work- uled simultaneously once prices fall, leading to secondary
loads exhibit highly irregular temporal patterns, with abrupt demandpeaksorreboundeffectsthatstressthegrid.Moreover,
transitions between low-utilization and peak-demand periods. AIdatacenteroperatorsarerelativelyinsensitivetoelectricity
These rapid changes can generate sharp power surges that prices.Asnotedin[126],thesefacilitieshavehighsunkcapital
challenge power dispatch, reserve scheduling, and real-time costs, and the workloads they run are highly lucrative. As a
grid stability. Effective forecasting requires a comprehensive result, the opportunity cost of deferring training or inference
understanding of AI workload characteristics, including job tasks can outweigh potential savings from energy arbitrage.
scheduling policies, training cycle durations, hardware uti- Therefore, relying on price signals alone may be insufficient
lization patterns, and the interaction between compute inten- to drive effective load shifting. This underscores the need for
sity and cooling system demand [119]. To address privacy carefullydesignedDRmechanismstailoredtoAIdatacenters.

12
One promising direction involves incentive-based (or penalty- andreducecarbonemissions.Spatialflexibilityreferstotheca-
based) and contract-based DR mechanisms, in which AI data pabilitytorerouteAIworkloadsacrossmultipledatacentersin
centers commit to predefined levels of flexibility in exchange differentgeographiclocations.ThisallowsAIworkloadstobe
fordirectcompensationorprioritygridservices.Forexample, rerouted to facilities in regions with cleaner electricity, lower
Google has signed contractual agreements with utilities in prices, or less grid congestion. Together, temporal and spatial
Indiana and Tennessee to curtail AI workloads during periods flexibility offer powerful levers for optimizing the alignment
of grid stress [127], [128]. Additionally, Coincident Peak between AI demand and power system conditions, helping to
(CP) mechanisms, such as ERCOT’s Four Coincident Peak enhance grid reliability, reduce carbon emissions, and lower
(4CP) charge, which imposes significant penalties on energy operationalcosts.Priorresearchshowsthattemporallyshifting
consumption during the grid’s four highest monthly demand AI workloads can reduce operational costs by up to 12% and
intervals, can directly incentivize data centers to shift their carbon emissions by approximately 10% [136]–[138]. Real-
usage away from peak periods [129]. world implementations [139] are increasingly supported by
4) Standardization and Regulation: As the scale and con- energy-aware scheduling platforms and demand-sensing tech-
centration of AI data centers increase, the implementation nologies[140].Moreover,studiesbasedonlocationalmarginal
of specific standards and regulatory frameworks becomes emissionsmodelinghighlightthatevenmodestspatialshifting
essential to confine their load behavior and preserve grid of loads can yield significant emission reductions [141]. In
reliability. One key task is the specification of fault ride- addition, AI data centers equipped with advanced control
through (FRT) capabilities. Similar to requirements imposed systems and on-site energy storage can mitigate their own
on renewable energy sources under IEEE Standard 1547 power fluctuations [18] and even provide ancillary services
and European grid codes, AI data centers may be required to the grid. By modulating compute intensity or charging
to remain connected during short-term voltage or frequency and discharging stored energy in response to grid signals,
disturbances. For instance, proposed specifications for data suchfacilitiescancontributetofrequencyregulation,spinning
center UPS systems suggest maintaining operation down to reserves, and fast-ramping support [14], [142]. This positions
50–70% of nominal voltage with a resynchronization capa- AI data centers not only as large load consumers but also as
bility within one second [130], [131]. In addition to ride- active grid participants that enhance grid reliability [143].
through, dynamic performance requirements should address 2) Energy-Aware AI Workload and Hardware: AI comput-
acceptable voltage and frequency tolerance ranges, reactive ingaccountsforthelargestshareofelectricityconsumptionin
power support, harmonic emissions, and ramp rate limits. AIdatacenters,makingadvancesincomputingefficiencyand
Such performance standards are increasingly being applied management crucial for reducing their energy footprint and
to large electrical and hybrid loads under evolving European stabilizing power demand. Several complementary strategies
interconnection frameworks [132]. Moreover, interconnection are outlined below:
standards may require that AI data center operators provide (i)Energy-awareAIcomputing:Techniquessuchasenergy-
utilities with accurate dynamic models, anonymized workload aware training (EAT) [144] enable models to activate only the
profiles, and operational telemetry to enable realistic system neuronsandconnectionsnecessaryforagiventask,effectively
planning and stability analysis [133]. On the regulatory front, disabling unused components and lowering power use. Addi-
the North American Electric Reliability Corporation (NERC) tional savings can be achieved through dynamic voltage and
has launched a Large Loads Task Force to assess and manage frequency scaling of CPUs and GPUs. For example, reference
risks associated with high-density data center growth [134]. [126]reportsthatunder-clockingasingleNVIDIAA100GPU
There is growing momentum for applying grid codes to for a specific application reduced power consumption by 40%
large,sensitiveelectronicloads,includingmandatoryresponse whiledecreasingperformancebyonly22%.Thisdemonstrates
characteristics during contingencies [135]. As a result, these that certain jobs could be executed at lower frequencies over
regulatoryandstandardizationmeasuresarecriticaltoensuring a longer duration to reduce overall energy use. Moreover,
that the integration of AI data centers supports, rather than advancedpowersmoothingandmanagementtechniquesatthe
undermines, the stability and resilience of the power grid. software and GPU levels can be developed and deployed to
mitigate power swings induced by AI workloads [18], thus
reducing risks to grid stability.
B. Solutions on AI Data Center Side
(ii)Developmentoflighter,task-specificAImodels:Smaller,
1) Leveraging Temporal and Spatial Flexibility of AI Data task-specific AI models can match the accuracy of large
Centers for Grid-Aware Operation: Flexible AI workloads foundation models while consuming substantially less power.
can be rescheduled or shifted without compromising service Techniquessuchaspruning(removingredundantparameters),
quality, offering valuable flexibility to support grid operation. quantization (reducing numerical precision), and knowledge
Specifically,temporalflexibilityreferstotheabilitytoshiftAI distillation (transferring knowledge from a large model to a
workloads over time without compromising service quality or smaller one) lower computational demands without compro-
userexperience.Forexample,non-urgentcomputationaltasks, misingoutputquality.Theseapproachesalsofacilitatedeploy-
such as large-scale model training or batch inference, can be ment on edge and mobile devices while yielding significant
scheduled during off-peak hours or periods of low grid stress energy savings. For example, TinyBERT achieves over 90%
and high renewable energy availability. This helps to flatten lowerenergyconsumptioncomparedtofull-sizeBERTmodels
load curves, enhance grid utilization, lower operating costs, [145]. Furthermore, sparse model architectures enhance effi-

13
ciency by directing computational resources toward the most models. Recent studies have shown that longer, more verbose
critical regions of the network. prompts,whilepotentiallyimprovingmodelinterpretabilityor
(iii) Energy-efficient hardware design: The deployment of output alignment, can significantly increase the number of
|                  |     |          |               |     |              |     |          | tokens to | be processed | and thus | greatly | elevate | the power |
| ---------------- | --- | -------- | ------------- | --- | ------------ | --- | -------- | --------- | ------------ | -------- | ------- | ------- | --------- |
| energy-efficient |     | hardware | are necessary |     | for reducing |     | the car- |           |              |          |         |         |           |
bon and energy footprint of AI data centers. Advances in pro- consumption of LLMs [158]–[160]. Moreover, fine-tuned,
cessorarchitecturecansubstantiallyimproveperformance-per- task-specific lightweight AI models often yield comparable
watt,enablinghighercomputationalthroughputatlowerpower performance to general-purpose foundation models but at a
costs. Domain-specific accelerators, low-power CPUs/GPUs, small fraction of the computational and energy cost [161].
|     |     |     |     |     |     |     |     | Recent initiatives, | such | as the AI | Energy | Score | project [162], |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ---- | --------- | ------ | ----- | -------------- |
andAI-optimizedhardwaresuchasGoogle’sTPUsarecentral
tothiseffort.Forinstance,Google’sTPUv4-basedsupercom- aimtobringtransparencytomodelenergyefficiencybybench-
puterhasdemonstratednotablespeedandefficiencygainsover markingtheenergycostperqueryacrossdifferentAImodels.
NVIDIA A100 GPUs [146]. Moreover, AI itself can be lever- Making such metrics available to end-users can encourage
aged to optimize the performance and energy efficiency of its more responsible usage behaviors and incentivize developers
supportinginfrastructure,asillustratedin[147].Co-optimizing to adopt energy-aware design considerations.
AI model architectures with underlying hardware, combining 2) User Flexibility and AI Demand Response: In practice,
techniques such as pruning, quantization, and hardware-aware manyend-usersofAIapplicationsexhibitadegreeofflexibil-
modeldesign,offersfurtherpotentialforachievingsubstantial ityintheirusagebehaviors,astheyoftendonotneedimmedi-
energy savings without sacrificing accuracy. ate AI responses to their queries. For example, a user submit-
| 3) Smart | and | Efficient | Cooling | Techniques: |     |         |     |                |         |               |     |          |             |
| -------- | --- | --------- | ------- | ----------- | --- | ------- | --- | -------------- | ------- | ------------- | --- | -------- | ----------- |
|          |     |           |         |             |     | Cooling | fa- | ting a complex | AI task | late at night | may | not need | the results |
cilities account for the second-largest share of electricity until the following morning. This inherent temporal flexibility
consumption in AI data centers. Recent research and industry inAIdemandofend-usersoffersavaluableopportunitytobet-
trends emphasize several advanced strategies: (i) Hybrid air- ter align query processing with power grid operational needs.
liquid cooling systems: combining air-based airflow manage- Building on this insight, a novel concept, termed “AI Demand
ment (e.g., hot/cold aisle containment, in-row cooling, raised- Response (AI-DR)”, can be developed to harness user-side AI
floor systems) with liquid approaches (e.g., direct-to-chip) to workloadflexibility,analogoustotheelectricdemandresponse
optimize energy, complexity, and adaptability. These systems programs[161],[163],[164]inpowersystems.Similarly,there
help manage thermal loads from dense AI clusters while can be incentive-based and price-based AI-DR mechanisms.
reducing energy usage compared to air-only or liquid-only Inincentive-basedAI-DRprograms,end-usersareincentivized
designs [148], [149]. (ii) Immersion and direct liquid cooling: through lower subscription fees, discounted inference rates,
immersing servers in dielectric fluids or using piping/driven or access to premium model tiers in exchange for accepting
liquidheatremovaloffersdramaticallyimprovedheattransfer, minorservicecompromises[126].Thesemayincludebounded
higher rack density, and up to 50% energy savings compared response delays, use of lower-tier hardware, or allowing their
to air cooling, though challenges remain around maintenance queries to be processed during periods of low grid stress
and cost [150], [151]. (iii) AI-driven adaptive and predictive or high renewable generation. In contrast, price-based AI-
coolingcontrol:leveragingreinforcementlearning(RL)[152]– DR programs employ time-varying pricing schemes, such as
[154],deepneuralnetworks,orotherMLmodelstoanticipate real-time pricing, time-of-use, critical peak pricing [161], to
thermal load changes and dynamically tune cooling systems encourageuserstoshifttheirAIusageawayfrompeakhours.
for maximum efficiency. These approaches have achieved 14- By exposing end-users to dynamic AI usage pricing signals,
21% energy savings in live data center deployments without serviceproviderscaninfluenceAIworkloadpatternsinagrid-
violating safety constraints [155]. Google’s commercial cool- awareandenergy-efficientmanner.Whenaggregatingacrossa
ing experiments using RL yielded 9-13% energy reductions largeanddiverseuserbase,serviceproviders(AIdatacenters)
[156].(iv)Renewable-poweredandfree(economizer)cooling: canprovidesubstantialflexibilitytosupportgridreliabilityand
leveraging ambient air (free cooling) where climates permit, improve overall cost efficiency.
| and powering        |     | cooling infrastructure |        | with        | onsite | renewables |        |     |     |            |     |     |     |
| ------------------- | --- | ---------------------- | ------ | ----------- | ------ | ---------- | ------ | --- | --- | ---------- | --- | --- | --- |
| (solar, wind)       | to  | reduce                 | carbon | intensity.  | These  | approaches |        |     |     |            |     |     |     |
|                     |     |                        |        |             |        |            |        |     | VI. | CONCLUSION |     |     |     |
| support sustainable |     | operations             | while  | attenuating |        | grid       | demand |     |     |            |     |     |     |
[157]. These smart and efficient cooling strategies underscore This paper focuses on the growing intersection between AI
a shift towards multi-dimensional optimization to balance and energy systems, specifically the electricity demand of AI
energy, water, carbon, and operational complexity. data centers and their impacts on the power grid. It highlights
|              |     |             |      |     |     |     |     | that the electricity | use of             | AI data     | centers   | is largely      | driven by |
| ------------ | --- | ----------- | ---- | --- | --- | --- | --- | -------------------- | ------------------ | ----------- | --------- | --------------- | --------- |
|              |     |             |      |     |     |     |     | computing            | and cooling        | loads, with | distinct  | characteristics | and       |
| C. Solutions | on  | AI End-User | Side |     |     |     |     |                      |                    |             |           |                 |           |
|              |     |             |      |     |     |     |     | patterns across      | model preparation, |             | training, | fine-tuning,    | and       |
1) Energy-Aware Prompting and AI Model Selection: End- inference stages. From the perspective of the power grid, the
users and developers of AI applications can contribute to large-scaleintegrationofAIdatacenterloadsintroducesmulti-
reducing the AI electricity footprint through energy-aware ap- faceted challenges across multiple timescales, ranging from
plicationdevelopmentandinformedusagedecisions.Forend- long-term planning and interconnection, short-term operation
users, one critical approach is the adoption of energy-efficient and markets, to real-time dynamics and stability. Addressing
prompting strategies and the selection of appropriately scaled these challenges requires collaborative, integrated solutions

14
involving grid operators, data centers, and end-users, such The total IT load demand for data centers in Europe is
as advances in AI load forecasting and dynamics modeling, projected to increase from approximately 10 GW in 2024
standardizationandregulation,grid-awarescheduling,energy- to 35 GW by 2030, with corresponding annual power con-
efficient hardware, and energy-conscious AI usage. Looking sumption nearly tripling from 62 TWh to over 150 TWh
ahead,theco-developmentofpowergridsandAIdatacenters by 2030, which would represent 5% of the continent’s total
will be essential to sustaining the rapid pace of AI innovation electricity use [170]. This growth is underpinned by strategic
in a reliable and sustainable manner. EU initiatives, including the EUR 30 billion gigafactory plan
|     |     |     |     |     |     |     |     | and the Climate |     | Neutral     | Data Center |     | Pact, which | promote | the       |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ----------- | --- | ----------- | ------- | --------- |
|     |     |     |     |     |     |     |     | development     | of  | large-scale | facilities  |     | powered     | by      | renewable |
APPENDIX
|           |         |         |             |      |        |      |              | energy [171]. |         | Projects | such as    | OpenAI’s | proposed      |     | Stargate  |
| --------- | ------- | ------- | ----------- | ---- | ------ | ---- | ------------ | ------------- | ------- | -------- | ---------- | -------- | ------------- | --- | --------- |
| A. Global | AI Data | Center  | Electricity |      | Demand |      |              |               |         |          |            |          |               |     |           |
|           |         |         |             |      |        |      |              | facility in   | Norway, | planned  | to         | run      | on hydropower |     | with an   |
| According | to      | the IEA | report      | [8], | global | data | centers con- |               |         |          |            |          |               |     |           |
|           |         |         |             |      |        |      |              | initial 230   | MW      | capacity | expandable |          | to 520        | MW, | exemplify |
sumed around 415 TWh of electricity in 2024, accounting this trend [172]. Accommodating this expansion will require
for about 1.5% of total global electricity consumption. The an estimated EUR 250-300 billion in grid upgrades and low-
United States was the largest contributor, accounting for 45% carbon energy integration [173]. This investment is necessary
ofthisdemand,followedbyChinaat25%andEuropeat15%. to support McKinsey’s forecast of nearly tripled data center
| Given their | dominant |     | shares | of global | data | center | electricity |             |             |     |         |        |     |     |     |
| ----------- | -------- | --- | ------ | --------- | ---- | ------ | ----------- | ----------- | ----------- | --- | ------- | ------ | --- | --- | --- |
|             |          |     |        |           |      |        |             | electricity | consumption |     | by 2030 | [170]. |     |     |     |
consumption,thecasesintheUnitedStates,China,andEurope
| are discussed | in  | greater | detail | as below. |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| 1) AIDataCenterLoadinUnitedStates: |             |         |     |                |     | TheUnitedStates |             |           |          |           |         |          |           |          |          |
| ---------------------------------- | ----------- | ------- | --- | -------------- | --- | --------------- | ----------- | --------- | -------- | --------- | ------- | -------- | --------- | -------- | -------- |
|                                    |             |         |     |                |     |                 |             | [1] W.    | X. Zhao, | K. Zhou,  | J. Li,  | T. Tang, | X. Wang,  | Y. Hou,  | Y. Min,  |
| is among                           | the largest | markets |     | for hyperscale |     | data            | centers and |           |          |           |         |          |           |          |          |
|                                    |             |         |     |                |     |                 |             | B. Zhang, |          | J. Zhang, | Z. Dong | et al.,  | “A survey | of large | language |
accountsforasignificantshareofglobalAI-relatedelectricity
models,”arXivpreprintarXiv:2303.18223,vol.1,no.2,2023.
demand. U.S. data center energy consumption, which reached [2] J.Achiam,S.Adler,S.Agarwal,L.Ahmad,I.Akkaya,F.L.Aleman,
|         |       |          |      |              |     |          |              | D. Almeida, |     | J. Altenschmidt, | S.  | Altman, | S. Anadkat | et  | al., “GPT-4 |
| ------- | ----- | -------- | ---- | ------------ | --- | -------- | ------------ | ----------- | --- | ---------------- | --- | ------- | ---------- | --- | ----------- |
| 176 TWh | (4.4% | of total | U.S. | electricity) |     | in 2023, | is projected |             |     |                  |     |         |            |     |             |
technicalreport,”arXivpreprintarXiv:2303.08774,2023.
to increase to a range of 325-580 TWh by 2028, contingent [3] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
upon various growth scenarios [165]. McKinsey & Company T. Lacroix, B. Rozie`re, N. Goyal, E. Hambro, F. Azhar et al.,
arXiv
projects that U.S. data center load will rise from 25 GW in “LLaMA: Open and efficient foundation language models,”
preprintarXiv:2302.13971,2023.
2024toover80GWby2030,largelydrivenbyAIworkloads [4] G. Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut,
[24]. Moreover, AI data center deployment in the U.S. is J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican et al., “Gemini:
|     |     |     |     |     |     |     |     | a family | of  | highly | capable | multimodal | models,” | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ------- | ---------- | -------- | ----- | -------- |
highlyconcentrated,asevidencedbythefactthatroughly80% arXiv:2312.11805,2023.
of the power demand is located in only 15 states [14], with [5] D. Patterson, J. Gonzalez, Q. Le, C. Liang, L.-M. Munguia,
Virginia, Texas, Georgia, and Arizona being leading hubs due D. Rothchild, D. So, M. Texier, and J. Dean, “Carbon emissions and
largeneuralnetworktraining,”arXivpreprintarXiv:2104.10350,2021.
| to their | favorable | tax incentives, |     | existing |     | fiber networks, | and |        |        |             |               |      |               |     |             |
| -------- | --------- | --------------- | --- | -------- | --- | --------------- | --- | ------ | ------ | ----------- | ------------- | ---- | ------------- | --- | ----------- |
|          |           |                 |     |          |     |                 |     | [6] K. | Semba, | “Artificial | intelligence, | real | consequences: |     | Confronting |
relatively lower energy costs [166], [167]. Northern Virginia’s AI’s growing energy appetite,” https://www.extremenetworks.
com/resources/blogs/confronting-ai-growing-energy-appetite-part-
| “Data Center | Alley” | alone | accounts |     | for more | than | 2.5 GW of |       |                     |     |      |       |          |          |         |
| ------------ | ------ | ----- | -------- | --- | -------- | ---- | --------- | ----- | ------------------- | --- | ---- | ----- | -------- | -------- | ------- |
|              |        |       |          |     |          |      |           | 1?utm | source=chatgpt.com, |     | Aug. | 2024, | [Online; | accessed | 13-Aug- |
activecapacity,withmultipleAI-focuseddatacentercampuses
2025].
| under construction. |     | New           | projects |              | are increasingly |        | targeting   |            |        |                                                           |         |         |     |       |           |
| ------------------- | --- | ------------- | -------- | ------------ | ---------------- | ------ | ----------- | ---------- | ------ | --------------------------------------------------------- | ------- | ------- | --- | ----- | --------- |
|                     |     |               |          |              |                  |        |             | [7] A.     | Cohen, | “AI                                                       | is      | pushing | the | world | toward    |
|                     |     |               |          |              |                  |        |             | an         | energy | crisis,”                                                  | Forbes, |         | May | 2024. | [Online]. |
| Midwestern          | and | Mountain      | West     | states       | such             | as     | Iowa, Ohio, |            |        |                                                           |         |         |     |       |           |
|                     |     |               |          |              |                  |        |             | Available: |        | https://www.forbes.com/sites/arielcohen/2024/05/23/ai-is- |         |         |     |       |           |
| and Wyoming,        |     | for proximity |          | to renewable |                  | energy | resources   |            |        |                                                           |         |         |     |       |           |
pushing-the-world-towards-an-energy-crisis
| and to diversify |     | geographic | risk. |     |     |     |     |                   |     |        |                 |     |          |               |        |
| ---------------- | --- | ---------- | ----- | --- | --- | --- | --- | ----------------- | --- | ------ | --------------- | --- | -------- | ------------- | ------ |
|                  |     |            |       |     |     |     |     | [8] International |     | Energy | Agency, “Energy |     | and AI,” | International | Energy |
2) AI Data Center Load in China: China is rapidly ex- Agency, Tech. Rep., Sep. 2024, accessed: 14 August 2025. [Online].
Available:https://www.iea.org/reports/energy-and-ai
| panding | its AI | data center | infrastructure, |     |     | leading | to a com- |                   |     |            |            |     |          |        |             |
| ------- | ------ | ----------- | --------------- | --- | --- | ------- | --------- | ----------------- | --- | ---------- | ---------- | --- | -------- | ------ | ----------- |
|         |        |             |                 |     |     |         |           | [9] J. Choquette, |     | W. Gandhi, | O. Giroux, |     | N. Stam, | and R. | Krashinsky, |
mensurate increase in power demand. In 2024, the electricity “NVIDIAA100tensorcoreGPU:Performanceandinnovation,”IEEE
consumptionofdata centersinChinaisestimated to beinthe Micro,vol.41,no.2,pp.29–35,2021.
100-150 TWh range, representing about 1-2% of the nation’s [10] N. Jouppi, G. Kurian, S. Li, P. Ma, R. Nagarajan, L. Nai, N. Patil,
|     |     |     |     |     |     |     |     | S. Subramanian, |     | A.  | Swing, B. | Towles | et al., “TPU | v4: | An optically |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------- | ------ | ------------ | --- | ------------ |
total electricity use, which is projected to rise to between 400 reconfigurablesupercomputerformachinelearningwithhardwaresup-
and 600 TWh annually by 2030 [168], [169]. To manage this portforembeddings,”inProceedingsofthe50thannualinternational
symposiumoncomputerarchitecture,2023,pp.1–14.
| growth, | China has | integrated |     | AI development |     | into | its national |     |     |     |     |     |     |     |     |
| ------- | --------- | ---------- | --- | -------------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[11] V.Avelar,P.Donovan,P.Lin,W.Torell,andM.A.T.Arango,“TheAI
energy strategy. A key strategy is the Eastern Data, West- disruption:Challengesandguidancefordatacenterdesign,”Artificial
ern Computing initiative, which encourages siting new high- IntelligenceinMedicine,vol.138,2023.
|             |           |     |            |     |            |           |      | [12] D. Patel, | J.  | E. Ontiveros, | and D. | Nishball, | “Datacenter | anatomy | part |
| ----------- | --------- | --- | ---------- | --- | ---------- | --------- | ---- | -------------- | --- | ------------- | ------ | --------- | ----------- | ------- | ---- |
| performance | computing |     | facilities |     | in western | provinces | like |                |     |               |        |           |             |         |      |
1:Electricalsystems,”https://semianalysis.com/2024/10/14/datacenter-
Qinghai,Xinjiang,andHeilongjiangthatarerichinrenewable
anatomy-part-1-electrical/,2024,accessed:2025-08-09.
|            |      |         |         |      |             |     |            | [13] Crusoe, | “Crusoe | and | tallgrass announce |     | AI data | center in | wyoming,” |
| ---------- | ---- | ------- | ------- | ---- | ----------- | --- | ---------- | ------------ | ------- | --- | ------------------ | --- | ------- | --------- | --------- |
| resources. | This | policy, | coupled | with | accelerated |     | smart grid |              |         |     |                    |     |         |           |           |
https://www.crusoe.ai/resources/newsroom/crusoe-and-tallgrass-
integrationfordemandforecastingandloadmanagement,aims
|          |             |               |     |     |        |      |             | announce-ai-data-center-in-wyoming, |     |     |     | Jul. | 2025, | accessed: | 2025-08- |
| -------- | ----------- | ------------- | --- | --- | ------ | ---- | ----------- | ----------------------------------- | --- | --- | --- | ---- | ----- | --------- | -------- |
| to align | the growing | computational |     |     | demand | with | sustainable |                                     |     |     |     |      |       |           |          |
09.
power generation and grid reliability [168]. [14] J. Aljbour, T. Wilson, and P. Patel, “Powering intelligence:
Analyzingartificialintelligenceanddatacenterenergyconsumption,”
| 3) AI | Data Center | Load | in  | Europe: | Europe | is  | also experi- |      |       |       |                 |     |       |           |            |
| ----- | ----------- | ---- | --- | ------- | ------ | --- | ------------ | ---- | ----- | ----- | --------------- | --- | ----- | --------- | ---------- |
|       |             |      |     |         |        |     |              | EPRI | White | Paper | no. 3002028905, |     | 2024. | [Online]. | Available: |
encing a significant expansion of its AI data center capacity. https://www.wpr.org/wp-content/uploads/2024/06/3002028905

15
Powering-Intelligence -Analyzing-Artificial-Intelligence-and-Data- Current technology and future direction,” in 2015 IEEE Power &
Center-Energy-Consumption.pdf EnergySocietyGeneralMeeting. IEEE,2015,pp.1–5.
[15] Nlyte Software, “Data center rack power costs: A condensed [36] A.Muhammad,A.Kalwar,andK.Mekhilef,“Review:uninterruptible
analysis,”https://www.nlyte.com/blog/data-center-rack-power-costs-a- power supply (UPS) system,” Renewable and Sustainable Energy
condensed-analysis/,2024,accessed:2025-08-01. Reviews,vol.58,pp.1395–1410,2016.
[16] Y.Li,M.Mughees,Y.Chen,andY.R.Li,“TheunseenAIdisruptions [37] T. Teague, S. S. Refaat, M. Farrag, and A. Karki, “A comparative
forpowergrids:LLM-inducedtransients,”arXiv,Sep.2024. study of UPS batteries for data center applications,” in 2025 IEEE
[17] M. Mughees, Y. Li, Y. Chen, and Y. R. Li, “Short-term load 19thInternationalConferenceonCompatibility,PowerElectronicsand
forecasting for AI-data centers,” arXiv preprint arXiv:2503.07756, PowerEngineering(CPE-POWERENG). IEEE,2025,pp.1–6.
2025.[Online].Available:https://arxiv.org/abs/2503.07756 [38] V. Kambhampati, A. van den Dobbelsteen, and J. Schild, “Moving
[18] E.Choukse,B.Warrier,S.Heath,L.Belmont,A.Zhao,H.A.Khan, beyonddieselgenerators:Exploringrenewablebackupalternativesfor
B.Harry,M.Kappel,R.J.Hewett,K.Dattaetal.,“Powerstabilization datacenters,”inJournalofPhysics:ConferenceSeries,vol.2929,no.1.
forAItrainingdatacenters,”arXivpreprintarXiv:2508.14318,2025. IOPPublishing,2024,p.012008.
[19] APTPowerTechnology,“HowAIcomputeloadsaretransformingdat- [39] M.Gooding,“Microsoftandcaterpillarpowerdatacenterfor48hours
acenter infrastructure,” https://apt4power.com/how-ai-compute-loads- using hydrogen fuel cells,” https://www.datacenterdynamics.com/en/
are-transforming-datacenter-infrastructure/,Jun.2025,accessed:2025- news/microsoft-caterpillar-hydrogen-fuel-cell-data-center/, Jan. 2024,
08-27. accessed:2025-08-09.
[20] W. Li and J. Li, “AI load dynamics – a power electronics [40] Q.Zhang,Z.Meng,X.Hong,Y.Zhan,J.Liu,J.Dong,T.Bai,J.Niu,
perspective,”arXivpreprintarXiv:2502.01647,2025,accessed:2025- and M. J. Deen, “A survey on data center cooling systems: Technol-
08-14.[Online].Available:https://arxiv.org/html/2502.01647v2 ogy,powerconsumptionmodelingandcontrolstrategyoptimization,”
[21] Bloomberg News. (2024, Dec.) AI needs so much power, it’s JournalofSystemsArchitecture,vol.119,p.102253,2021.
makingyoursworse.[Online].Available:https://www.bloomberg.com/ [41] J.NiandX.Bai,“Areviewofairconditioningenergyperformancein
graphics/2024-ai-power-home-appliances/?embedded-checkout=true datacenters,”Renewableandsustainableenergyreviews,vol.67,pp.
[22] L. Lin, R. Wijayawardana, V. Rao, H. Nguyen, E. W. GNIBGA, and 625–640,2017.
A. A. Chien, “Exploding AI power use: an opportunity to rethink [42] I. W. Kuncoro, N. Pambudi, M. K. Biddinika, I. Widiastuti, M. Hi-
grid planning and management,” in Proceedings of the 15th ACM jriawan, and K. Wibowo, “Immersion cooling as the next technology
International Conference on Future and Sustainable Energy Systems, fordatacentercooling:Areview,”inJournalofPhysics:Conference
2024,pp.434–441. Series,vol.1402,no.4. IOPPublishing,2019,p.044057.
[23] K. Pilz, Y. Mahmood, and L. Heim, “AI’s power requirements under [43] A. Heydari, A. R. Gharaibeh, M. Tradat, Y. Manaserh, V. Radmard,
exponential growth: Extrapolating AI data center power demand B.Eslami,J.Rodriguez,B.Sammakiaetal.,“Experimentalevaluation
and assessing its potential impact on U.S. competitiveness,” RAND of direct-to-chip cold plate liquid cooling for high-heat-density data
Corporation, Jan. 2025. [Online]. Available: https://www.rand.org/ centers,”AppliedThermalEngineering,vol.239,p.122122,2024.
pubs/research reports/RRA3572-1.html [44] H. Chen, Y.-h. Peng, and Y.-l. Wang, “Thermodynamic analysis of
[24] McKinsey&Company,“Howdatacentersandtheenergysectorcan hybrid cooling system integrated with waste heat reusing and peak
sate AI’s hunger for power,” https://www.mckinsey.com/industries/ load shifting for data center,” Energy Conversion and Management,
private-capital/our-insights/how-data-centers-and-the-energy-sector- vol.183,pp.427–439,2019.
can-sate-ais-hunger-for-power,2024,accessed:2025-08-01. [45] K. Haghshenas, B. Setz, Y. Blosch, and M. Aiello, “Enough hot air:
[25] C. Davenport, B. Singer, N. Mehta, B. Lee, J. Mackay, A. Modak, The role of immersion cooling,” Energy Informatics, vol. 6, no. 1,
B. Corbett, J. Miller, T. Hari, J. Ritchie et al., “Generational growth: p.14,Aug.2023.[Online].Available:https://doi.org/10.1186/s42162-
AI, data centers and the coming US power demand surge,” Goldman 023-00269-0
Sachs,April,vol.28,2024. [46] M.Azarifar,M.Arik,andJ.-Y.Chang,“Liquidcoolingofdatacenters:
[26] N. Jegham, M. Abdelatti, L. Elmoubarki, and A. Hendawi, “How Anecessityfacingchallenges,”AppliedThermalEngineering,vol.247,
hungry is AI? benchmarking energy, water, and carbon footprint of p.123112,Jun.2024.
LLMinference,”arXivpreprintarXiv:2505.09598,2025. [47] F.Zhou,C.Shen,G.Ma,andX.Yan,“Powerusageeffectivenessanal-
[27] D. Patel, W. Chu, C. Tseng, M. Xie, J. E. Ontiveros, and ysisofaliquid-pump-drivenhybridcoolingsystemfordatacentersin
D. Nishball, “GB200 hardware architecture-component supply subclimatezones,”SustainableEnergyTechnologiesandAssessments,
chain & bom,” https://semianalysis.com/2024/07/17/gb200-hardware- vol.52,p.102277,Aug.2022.
architecture-and-component/#,2024,accessed:2025-08-09. [48] Google, “Google data center pue performance,” https://datacenters.
[28] J. Do, V. C. Ferreira, H. Bobarshad, M. Torabzadehkashi, S. Rezaei, google/efficiency/,accessed:2025-08-11.
A. Heydarigorji, D. Souza, B. F. Goldstein, L. Santiago, M. S. Kim [49] Meta Platforms, Inc., “Meta 2024 sustainability report,”
etal.,“Cost-effective,energy-efficient,andscalablestoragecomputing https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-
forlarge-scaleAIapplications,”ACMTransactionsonStorage(TOS), 2024-Sustainability-Report.pdf,2024,accessed:2025-08-11.
vol.16,no.4,pp.1–37,2020. [50] A.Liu,B.Feng,B.Xue,B.Wang,B.Wu,C.Lu,C.Zhao,C.Deng,
[29] A. George, A. Dilger, M. J. Brim, R. Mohr, A. Shehata, J. Y. Choi, C. Zhang, C. Ruan et al., “DeepSeek-V3 technical report,” arXiv
A. M. Karimi, J. Hanley, J. Simmons, D. Manno et al., “Lustre preprintarXiv:2412.19437,2024.
unveiled: Evolution, design, advancements, and current trends,” ACM [51] Wikipedia, “Wikipedia,” https://en.wikipedia.org/wiki/Main Page,
TransactionsonStorage,vol.21,no.3,pp.1–109,2025. [Online;accessed13-Aug-2025].
[30] Amazon Web Services, “What is Amazon simple storage service [52] CommonCrawl,“Commoncrawl,”https://commoncrawl.org/,[Online;
(Amazon S3)?” 2024, accessed: 2025-08-07. [Online]. Available: accessed13-Aug-2025].
https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html [53] Y.Zhu,R.Kiros,R.Zemel,R.Salakhutdinov,R.Urtasun,A.Torralba,
[31] NVIDIA Corporation, “NVIDIA NVLink high-speed GPU inter- andS.Fidler,“Aligningbooksandmovies:Towardsstory-likevisual
connect,” https://www.nvidia.com/en-us/products/workstations/nvlink- explanationsbywatchingmoviesandreadingbooks,”inProceedings
bridges/,2025,accessed:2025-08-01. of the IEEE international conference on computer vision, 2015, pp.
[32] InfiniBand Trade Association, “InfiniBand – high-performance in- 19–27.
terconnect technology,” https://www.infinibandta.org/, 2025, accessed: [54] Wikipediacontributors,“Artificialintelligenceengineering,”https://en.
2025-08-01. wikipedia.org/wiki/Artificial intelligence engineering,2025,accessed:
[33] J.J.WilkeandJ.P.Kenny,“Opportunitiesandlimitationsofquality-of- 2025-08-01.
serviceinmessagepassingapplicationsonadaptivelyrouteddragonfly [55] R.Verdecchia,L.Cruz,J.Sallou,M.Lin,J.Wickenden,andE.Hotel-
and fat tree networks,” in 2020 IEEE International Conference on lier, “Data-centric green AI an exploratory empirical study,” in 2022
ClusterComputing(CLUSTER). IEEE,2020,pp.109–118. international conference on ICT for sustainability (ICT4S). IEEE,
[34] J. Sun, S. Wang, J. Wang, and L. M. Tolbert, “Dynamic model and 2022,pp.35–45.
converter-basedemulatorofadatacenterpowerdistributionsystem,” [56] S. Shanbhag and S. Chimalakonda, “On the energy consumption of
IEEETransactionsonPowerElectronics,vol.37,no.7,pp.8420–8432, different dataframe processing libraries–an exploratory study,” arXiv
2022. preprintarXiv:2209.05258,2022.
[35] S. Chalise, A. Golshani, S. R. Awasthi, S. Ma, B. R. Shrestha, [57] I.Latif,A.C.Newkirk,M.R.Carbone,A.Munir,Y.Lin,J.Koomey,
L.Bajracharya,W.Sun,andR.Tonkoski,“Datacenterenergysystems: X. Yu, and Z. Dong, “Empirical measurements of ai training power

16
demandonaGPU-acceleratednode,”arXivpreprintarXiv:2412.08602, //legiscan.com/TX/bill/SB6/2025,2025,passedJune20,2025;effective
| 2024. |     |     |     |     |     |     |     | immediately,89thLegislature. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
[58] J. McDonald, B. Li, N. Frey, D. Tiwari, V. Gadepally, and S. Samsi, [79] FTI Consulting, “Current power trends and implications for
“Great power, great responsibility: Recommendations for reducing the data center industry,” https://www.fticonsulting.com/insights/
energyfortraininglanguagemodels,”arXiv,May2022. articles/current-power-trends-implications-data-center-industry, 2024,
[59] D.Anisuzzaman,J.G.Malins,P.A.Friedman,andZ.I.Attia,“Fine- accessed:September6,2025.
tuninglargelanguagemodelsforspecializedusecases,”MayoClinic
|     |     |     |     |     |     |     |     | [80] A. Satchwell, |     | N. M. | Frick, | P. Cappers, | S.  | Sergici, | R. Hledik, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | ------ | ----------- | --- | -------- | ---------- |
Proceedings:DigitalHealth,vol.3,no.1,p.100184,2025. G. Kavlak, and G. Oskar, “Electricity rate designs for large loads:
[60] X. Wang, C. Na, E. Strubell, S. Friedler, and S. Luccioni, “Energy Evolving practices and opportunities,” Lawrence Berkeley National
and carbon considerations of fine-tuning BERT,” arXiv preprint Laboratory, Tech. Rep., Jan. 2025, accessed: 2025-09-08. [Online].
arXiv:2311.10267, 2023, accessed: 2025-08-14. [Online]. Available: Available: https://eta-publications.lbl.gov/sites/default/files/2025-
https://arxiv.org/abs/2311.10267
|     |     |     |     |     |     |     |     | 01/electricity |     | rate designs | for | large loads | evolving | practices | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ----------- | -------- | --------- | --- |
[61] K.Huang,H.Yin,H.Huang,andW.Gao,“TowardsgreenAIinfine- opportunities final.pdf
tuning large language models via adaptive backpropagation,” arXiv [81] Charles River Associates, “Win-win tariff design and
preprint arXiv:2309.13192, 2023, accessed: 2025-08-14. [Online]. commercial considerations for data centers and utilities,”
Available:https://arxiv.org/abs/2309.13192 https://media.crai.com/wp-content/uploads/2024/10/08113955/Energy-
[62] T.Rehman,D.K.Sanyal,andS.Chattopadhyay,“Howgreenareneural
Insights-Win-win-tariff-design-and-commercial-consideration-for-
language models? Analyzing energy consumption in text summariza- datacenters-and-utilities-October-2024.pdf,2024,accessed:September
| tionfine-tuning,”arXivpreprintarXiv:2501.15398,Jan.2025. |     |     |     |     |     |     |     | 6,2025. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
[63] D.Patterson,J.Gonzalez,U.Ho¨lzle,Q.Le,C.Liang,L.-M.Munguia, [82] A. J. Wood, B. F. Wollenberg, and G. B. Sheble, Power Generation,
D.Rothchild,D.R.So,M.Texier,andJ.Dean,“Thecarbonfootprint Operation,andControl,3rded. JohnWiley&Sons,2013.
| of machine |     | learning | training | will plateau, | then | shrink,” | Computer, |               |     |        |         |           |     |          |           |
| ---------- | --- | -------- | -------- | ------------- | ---- | -------- | --------- | ------------- | --- | ------ | ------- | --------- | --- | -------- | --------- |
|            |     |          |          |               |      |          |           | [83] Q. Dong, | R.  | Huang, | C. Cui, | D. Towey, | L.  | Zhou, J. | Tian, and |
vol.55,no.7,pp.18–28,2022.
|     |     |     |     |     |     |     |     | J. Wang, | “Short-Term |     | Electricity-Load |     | Forecasting | by deep | learning: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ---------------- | --- | ----------- | ------- | --------- |
[64] Kanoppi.(2024)SearchenginesvsAI:Energyconsumptioncompared. A comprehensive survey,” Engineering Applications of Artificial
Accessed: 2025-08-14. [Online]. Available: https://kanoppi.co/search- Intelligence, vol. 154, p. 110980, Aug. 2025. [Online]. Available:
engines-vs-ai-energy-consumption-compared/
https://www.sciencedirect.com/science/article/pii/S0952197625009807
[65] A.S.Luccioni,Y.Jernite,andE.Strubell,“Powerhungryprocessing:
|     |     |     |     |     |     |     |     | [84] PJM | Interconnection, |     | “PJM | capacity | market | auction | results for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ---- | -------- | ------ | ------- | ----------- |
WattsdrivingthecostofAIdeployment?”arXiv,Nov.2023.
2026/2027deliveryyear,”2025.[Online].Available:https://www.pjm.
[66] A. Amara, F. Amiel, and T. Ea, “FPGA vs. ASIC for low power com/markets-and-operations/rpm.aspx
applications,” Microelectronics journal, vol. 37, no. 8, pp. 669–677, [85] C. Kunkel. (2025, Jul.) Projected data center growth spurs
2006.
|              |     |             |                    |               |            |           |              | PJM       | capacity   | prices    | by factor                                          | of       | 10.       | Institute | for Energy  |
| ------------ | --- | ----------- | ------------------ | ------------- | ---------- | --------- | ------------ | --------- | ---------- | --------- | -------------------------------------------------- | -------- | --------- | --------- | ----------- |
| [67] S. Han, | J.  | Pool,       | J. Tran,           | and W.        | J. Dally,  | “Learning | both         |           |            |           |                                                    |          |           |           |             |
|              |     |             |                    |               |            |           |              | Economics | and        | Financial | Analysis                                           | (IEEFA). | Accessed: |           | 2025-08-02. |
| weights      | and | connections |                    | for efficient |            | neural    | network,” in |           |            |           |                                                    |          |           |           |             |
|              |     |             |                    |               |            |           |              | [Online]. | Available: |           | https://ieefa.org/resources/projected-data-center- |          |           |           |             |
| Proceedings  |     | of the      | 28th International |               | Conference |           | on Neural    |           |            |           |                                                    |          |           |           |             |
growth-spurs-pjm-capacity-prices-factor-10
Information Processing Systems (NeurIPS), 2015, pp. 1135– [86] New York Independent System Operator, “2025 power trends,”
| 1143. | [Online]. | Available: | https://proceedings.neurips.cc/paper/2015/ |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --------- | ---------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://www.nyiso.com/documents/20142/2223020/2025-Power-
file/ae0eb3eed39d2bcef4622b2499a05fe6-Paper.pdf
|                |     |         |               |     |            |     |            | Trends.pdf/51517a1b-36fa-4f3d-d44d-eabe23598514, |     |     |     |     |     | 2025, | accessed: |
| -------------- | --- | ------- | ------------- | --- | ---------- | --- | ---------- | ------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --------- |
| [68] P. Stock, | A.  | Joulin, | R. Gribonval, |     | B. Graham, | and | H. Je´gou, |                                                  |     |     |     |     |     |       |           |
2025-08-04.
| “And | the bit | goes | down: Revisiting |     | the quantization |     | of neural |               |             |         |     |       |          |            |        |
| ---- | ------- | ---- | ---------------- | --- | ---------------- | --- | --------- | ------------- | ----------- | ------- | --- | ----- | -------- | ---------- | ------ |
|      |         |      |                  |     |                  |     |           | [87] Electric | Reliability | Council | of  | Texas | (ERCOT), | “Long-term | system |
networks,” in Proceedings of the 37th International Conference on assessment 2024,” ERCOT, Tech. Rep., 2024. [Online]. Available:
| Machine | Learning | (ICML), |     | 2020, pp. | 1–12. | [Online]. | Available: |     |     |     |     |     |     |     |     |
| ------- | -------- | ------- | --- | --------- | ----- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://www.ercot.com/gridinfo/resource
https://arxiv.org/abs/1907.05686
|              |          |     |          |          |        |            |           | [88] Business | Insider. | (2025, | Jul.)  | Electric | bills   | are rising | in 13    |
| ------------ | -------- | --- | -------- | -------- | ------ | ---------- | --------- | ------------- | -------- | ------ | ------ | -------- | ------- | ---------- | -------- |
| [69] W. Fan, | Y. Ding, | L.  | Ning, S. | Wang, H. | Li, D. | Yin, T.-S. | Chua, and |               |          |        |        |          |         |            |          |
|              |          |     |          |          |        |            |           | states        | because  | of big | tech’s | energy   | hunger. | Accessed:  | 2025-08- |
Q.Li,“AsurveyonRAGmeetingLLMs:Towardsretrieval-augmented
02.[Online].Available:https://www.businessinsider.com/electric-bills-
| large | language | models,” | in Proceedings |     | of the | 30th ACM | SIGKDD |     |     |     |     |     |     |     |     |
| ----- | -------- | -------- | -------------- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
conferenceonknowledgediscoveryanddatamining,2024,pp.6491– rise-13-states-because-big-tech-data-centers-2025-7
|     |     |     |     |     |     |     |     | [89] K. Patel, | K.  | Steinberger, | and | A.  | Debenedictis, | “Virginia | data |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | --- | ------------- | --------- | ---- |
6501.
|                     |     |                      |     |     |                       |     |       | center | study:      | Electric | infrastructure |        | and customer | rate | impacts,” |
| ------------------- | --- | -------------------- | --- | --- | --------------------- | --- | ----- | ------ | ----------- | -------- | -------------- | ------ | ------------ | ---- | --------- |
| [70] R. Desislavov, |     | F. Mart´ınez-Plumed, |     | and | J. Herna´ndez-Orallo, |     | “Com- |        |             |          |                |        |              |      |           |
|                     |     |                      |     |     |                       |     |       | Joint  | Legislative | Audit    | and            | Review | Commission   |      | (JLARC),  |
puteandenergyconsumptiontrendsindeeplearninginference,”arXiv,
|     |     |     |     |     |     |     |     | Tech. | Rep., | Dec. 2024, | accessed: |     | 2025-08-04. | [Online]. | Avail- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ---------- | --------- | --- | ----------- | --------- | ------ |
Sep.2021.
[71] A.Ballantyne,“Whitepaper:Thepowerstrain:Canthegridmanage able:https://jlarc.virginia.gov/pdfs/presentations/JLARC%20Virginia%
|     |     |     |     |     |     |     |     | 20Data%20Center%20Study |     |     | FINAL | 12-09-2024.pdf |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ----- | -------------- | --- | --- | --- |
thedatacenterboom?”Wunderlich-Malec,Tech.Rep.,Apr.2025.
[90] “IEEEStandardforInterconnectionandInteroperabilityofDistributed
| [72] H. Chen, | P.  | Gao, K. | Liu, L. Chen, | and | W. Huang, | “Joint | expansion |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------------- | --- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
EnergyResourceswithAssociatedElectricPowerSystemsInterfaces,”
planningfordatacentersanddistributionnetworksbasedonconditional
| value-at-risk |     | theory considering |     | low carbon | characteristics,” |     | Electric | pp.1–138,2018. |     |     |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | ---------- | ----------------- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
PowerSystemsResearch,vol.229,p.110162,2024. [91] C. Mishra, L. Vanfretti, J. Delaree Jr, T. Purcell, and K. D. Jones,
[73] C.Guo,F.Luo,Z.Cai,Z.Y.Dong,andR.Zhang,“Integratedplanning “Understanding the inception of 14.7 Hz oscillations emerging from
|             |      |         |             |        |         |         |          | a data | center,” | Sustainable | Energy, | Grids | and | Networks, | p. 101735, |
| ----------- | ---- | ------- | ----------- | ------ | ------- | ------- | -------- | ------ | -------- | ----------- | ------- | ----- | --- | --------- | ---------- |
| of internet | data | centers | and battery | energy | storage | systems | in smart |        |          |             |         |       |     |           |            |
2025.
grids,”AppliedEnergy,vol.281,p.116093,2021.
[74] A.Vafamehr,M.E.Khodayar,S.D.Manshadi,I.Ahmad,andJ.Lin, [92] P. Gravois, “ERCOT large load loss/reduction events 2020–
“Aframeworkforexpansionplanningofdatacentersinelectricityand 2024,” Electric Reliability Council of Texas (ERCOT),
data networks under uncertainty,” IEEE Transactions on Smart Grid, Operations Engineer – Event Analysis, 2024. [Online]. Avail-
able:https://www.ercot.com/files/docs/2024/11/18/ERCOT%20Large%
vol.10,no.1,pp.305–316,2017.
|                |     |        |          |           |     |           |            | 20Load%20Events |     | PDCWG | 19Nov2024.pdf |     |     |     |     |
| -------------- | --- | ------ | -------- | --------- | --- | --------- | ---------- | --------------- | --- | ----- | ------------- | --- | --- | --- | --- |
| [75] Y. Zhang, | C.  | Liang, | H. Wang, | J. Zhang, | B.  | Zeng, and | W. Liu, “A |                 |     |       |               |     |     |     |     |
multi-objective interval optimization approach to expansion planning [93] J.Billo,“Largeelectronicload(LEL)voltageride-throughoverview,”
of active distribution system with distributed internet data centers Electric Reliability Council of Texas (ERCOT), Operations Planning
and renewable energy resources,” IET Generation, Transmission & – Event Analysis, 2025, accessed: 2025-08-18. [Online]. Available:
https://www.ercot.com/calendar/06132025-Large-Load-Workshop
Distribution,vol.18,no.18,pp.2999–3016,2024.
|              |      |                 |     |     |             |     |              | [94] Electric | Reliability | Council | of  | Texas | (ERCOT), | “Large | load survey |
| ------------ | ---- | --------------- | --- | --- | ----------- | --- | ------------ | ------------- | ----------- | ------- | --- | ----- | -------- | ------ | ----------- |
| [76] “Amazon | buys | nuclear-powered |     |     | data center |     | from Talen.” |               |             |         |     |       |          |        |             |
[Online]. Available: https://www.ans.org/news/article-5842/amazon- and request for information of voltage ride-through capabilities to
buys-nuclearpowered-data-center-from-talen/ ensurereliableinterconnectionandoperationoflargeelectronicloads,”
[77] S.Patel.(2024,Oct.)Googlebetsbigonnuclear:Inksdealwithkairos ERCOT, Tech. Rep. M-B062325-01, Jun. 2025. [Online]. Available:
powerfor500-MWSMRfleettopowerdatacenters.[Online].Avail- https://www.ercot.com/services/comm/mkt notices/M-B062325-01
|       |                                                           |     |     |     |     |     |     | [95] P.Kundur,PowerSystemStabilityandControl. |     |     |     |     |     | McGraw-Hill,1994. |     |
| ----- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- |
| able: | https://www.powermag.com/google-bets-big-on-nuclear-inks- |     |     |     |     |     |     |                                               |     |     |     |     |     |                   |     |
deal-with-kairos-power-for-500-mw-smr-fleet-to-power-data-centers/ [96] A.Ulbig,T.S.Borsche,andG.Andersson,“Impactoflowrotational
[78] “TexasSenateBill6(2025):Relatingtoplanningfor,interconnection inertia on power system stability and operation,” IFAC Proceedings
andoperationof,andcostsofservicingcertainelectricalloads,”https: Volumes,vol.47,no.3,pp.7290–7297,2014.

17
[97] M.H.J.Bollen,UnderstandingPowerQualityProblems:VoltageSags [121] A. Allabadi, J. Mahseredjian, K. Jacobs, S. Dennetie`re, I. Kocar,
andInterruptions. IEEEPress/Wiley,2000. and T. Ould-Bachir, “Initializing EMT models of grid forming VSCs
[98] L. Meegahapola, A. Sguarezi, J. S. Bryant, M. Gu, E. R. Conde D, in MTDC systems,” Electric Power Systems Research, vol. 235, p.
| and | R. B. Cunha, | “Power | system | stability | with | power-electronic | 110674,Oct.2024. |     |     |     |     |     |     |
| --- | ------------ | ------ | ------ | --------- | ---- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
converter interfaced renewable power generation: Present issues and [122] K. Chen, “EPE perspective on modeling needs,” ESIG
futuretrends,”Energies,vol.13,no.13,p.3441,2020. Large Load Task Force, Tech. Rep., 2025. [Online].
|     |     |     |     |     |     |     | Available: | https://www.esig.energy/wp-content/uploads/2025/03/EPE- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
[99] J.Sun,M.Xu,M.Cespedes,andM.Kauffman,“Low-frequencyinput
|           |          |     |                 |                |     |                 | Perspective-on-Modeling-Needs |     |     |     | Kevin-Chen.pdf |     |     |
| --------- | -------- | --- | --------------- | -------------- | --- | --------------- | ----------------------------- | --- | --- | --- | -------------- | --- | --- |
| impedance | modeling |     | of single-phase | pfc converters |     | for data center |                               |     |     |     |                |     |     |
power system stability studies,” in 2019 IEEE Energy Conversion [123] A. Jimenez-Ruiz and F. Milano, “Data center model for transient
CongressandExposition(ECCE),2019,pp.97–106. stabilityanalysisofpowersystems,”arXivpreprintarXiv:2505.16575,
[100] J.Sun,M.Xu,M.Cespedes,D.Wong,andM.Kauffman,“Modeling 2025.[Online].Available:https://arxiv.org/abs/2505.16575
and analysis of data center power system stability by impedance [124] K. Huang, M. Xiong, Y. Liu, K. Sun, and F. Qiu, “A heterogeneous
|     |     |     |     |     |     |     | multiscale | method | for | power | system | simulation | considering |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----- | ------ | ---------- | ----------- |
methods,”in2019IEEEEnergyConversionCongressandExposition
(ECCE),2019,pp.107–116. electromagnetic transients,” arXiv preprint arXiv:2302.09341, 2023.
[101] M. Glinkowski, P. Lembke, L. Simmons, and T. Earp, “Data [Online].Available:https://arxiv.org/abs/2302.09341
center power system harmonics: An overview of effects on [125] Q. Shen, Y. Zhou, P. Zhang, Y. A. Shamash, R. Sharma, and
data center efficiency and reliability,” 3DFS, Tech. Rep., B. Chen, “Physics-informed AI inverter,” 2024. [Online]. Available:
2015. [Online]. Available: https://3dfs.com/wp-content/uploads/2015/ https://arxiv.org/abs/2406.17661
|         |                                    |     |     |     |     |     | [126] C. | Crozier and | M. Liska, | “The | potential | of data | center energy |
| ------- | ---------------------------------- | --- | --- | --- | --- | --- | -------- | ----------- | --------- | ---- | --------- | ------- | ------------- |
| 11/WP55 | DataCenterPowerSystemHarmonics.pdf |     |     |     |     |     |          |             |           |      |           |         |               |
[102] IEEE Standards Association, “IEEE recommended practice and re- demand to provide grid flexibility,” Current Sustainable/Renewable
quirementsforharmoniccontrolinelectricpowersystems(IEEEStd EnergyReports,vol.12,no.1,p.12,Apr.2025.[Online].Available:
| 519-2014),”2014. |     |     |     |     |     |     | https://doi.org/10.1007/s40518-025-00258-9 |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
[103] J. Arrillaga and N. R. Watson, Power System Harmonics, 2nd ed. [127] Reuters, “Google agrees to curb power use for AI data
|     |     |     |     |     |     |     | centers | to ease | strain | on  | US grid,” | Aug. 2025. | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | --- | --------- | ---------- | --------- |
Wiley,2000.
|     |     |     |     |     |     |     | Available: |     | https://www.reuters.com/sustainability/boards-policy- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
[104] S.Maleki,S.Pan,S.Lakshminarayana,andC.Konstantinou,“Survey
regulation/google-agrees-curb-power-use-ai-data-centers-ease-strain-
| of load-altering |     | attacks | against power | grids: | Attack | impact, detection |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------------- | ------ | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
and mitigation,” IEEE Open Access Journal of Power and Energy, us-grid-when-demand-2025-08-04/
2025. [128] IT Pro, “Google says it will pause AI data centers
[105] T. McLaughlin, “Big Tech’s data center boom poses new risk to to help overloaded grids,” Aug. 2025. [Online]. Avail-
|     |                  |          |      |                 |     |                   | able: | https://www.itpro.com/infrastructure/data-centres/google-says-it- |     |     |     |     |     |
| --- | ---------------- | -------- | ---- | --------------- | --- | ----------------- | ----- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
| US  | grid operators,” | Reuters, | Mar. | 2025. [Online]. |     | Available: https: |       |                                                                   |     |     |     |     |     |
will-pause-ai-data-centers-to-help-overloaded-grids
//www.reuters.com/technology/big-techs-data-center-boom-poses-
new-risk-us-grid-operators-2025-03-19/?utm source=chatgpt.com [129] M.Lukawski,J.W.Tester,M.C.Moore,P.Krol,andC.L.Anderson,
[106] C.-C.Sun,A.Hahn,andC.-C.Liu,“Cybersecurityofapowergrid: “Demandresponseforreducingcoincidentpeakloadsindatacenters,”
State-of-the-art,” International Journal of Electrical Power & Energy inProceedingsofthe52ndHawaiiInternationalConferenceonSystem
|     |     |     |     |     |     |     | Sciences | (HICSS-52), | Grand | Wailea, | Hawaii, | Jan. 2019. | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | ------- | ------- | ---------- | --------- |
Systems,vol.99,pp.45–56,2018.
|     |     |     |     |     |     |     | Available:https://aisel.aisnet.org/hicss-52/es/renewable |     |     |     |     |     | resources/2/ |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ |
[107] E.Gibney,“HowtoshrinkAI’sballooningcarbonfootprint,”Nature,
|     |     |     |     |     |     |     | [130] Eaton, | “Data | centers – | a good | grid citizen,” | https://www.ercot.com/ |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --------- | ------ | -------------- | ---------------------- | --- |
vol.607,p.648,Jul.2022.
files/docs/2025/07/10/Eaton-Data-center-A-Good-Grid-Citizen.pdf,
| [108] J. Ranganathan, |     | L. Corbier, | P.  | Bhatia et al., | “The | greenhouse gas |     |     |     |     |     |     |     |
| --------------------- | --- | ----------- | --- | -------------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
protocol:Acorporateaccountingandreportingstandard,”2004. 2025, proposed UPS ride-through and post-fault reconnection
performancespecificationsfordatacenters.
[109] M.Sotos,“GHGprotocolscope2guidance,”2015.
|                |     |         |          |                      |     |               | [131] Wikipedia | contributors, |          | “Grid | code,”    | https://en.wikipedia.org/wiki/ |           |
| -------------- | --- | ------- | -------- | -------------------- | --- | ------------- | --------------- | ------------- | -------- | ----- | --------- | ------------------------------ | --------- |
| [110] X. Chen, | A.  | Sun, W. | Shi, and | N. Li, “Carbon-aware |     | optimal power |                 |               |          |       |           |                                |           |
|                |     |         |          |                      |     |               | Grid            | code, 2025,   | overview | of    | technical | requirements                   | for grid- |
flow,”IEEETransactionsonPowerSystems,2024.
interconnectedfacilities.
[111] X.Chen,H.Chao,W.Shi,andN.Li,“Towardscarbon-freeelectric-
|      |              |           |     |            |        |                | [132] Energy   | Systems | Integration                                         | Group | (ESIG), | “Large load | performance |
| ---- | ------------ | --------- | --- | ---------- | ------ | -------------- | -------------- | ------- | --------------------------------------------------- | ----- | ------- | ----------- | ----------- |
| ity: | A flow-based | framework | for | power grid | carbon | accounting and |                |         |                                                     |       |         |             |             |
|      |              |           |     |            |        |                | requirements,” |         | https://www.esig.energy/wp-content/uploads/2025/05/ |       |         |             |             |
decarbonization,”EnergyConversionandEconomics,vol.5,no.6,pp. LL-Performance-Requirements-Framework-and-Methodology v2.pdf,
| 396–418,2024.  |          |            |     |              |           |             | 2025.          |            |          |     |                |           |             |
| -------------- | -------- | ---------- | --- | ------------ | --------- | ----------- | -------------- | ---------- | -------- | --- | -------------- | --------- | ----------- |
| [112] X. Chen, | “Enhance | low-carbon |     | power system | operation | via carbon- |                |            |          |     |                |           |             |
|                |          |            |     |              |           |             | [133] GridLab, | “Practical | guidance | and | considerations | for large | load inter- |
awaredemandresponse,”EnergyInternet,vol.1,no.2,pp.141–149,
connections,”https://gridlab.org/wp-content/uploads/2025/03/GridLab-
2024.
|     |     |     |     |     |     |     | Report-Large-Loads-Interim-Report.pdf, |     |     |     |     | 2025, recommendations | for |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --------------------- | --- |
[113] R. Kansal, “Introduction to the virtual power purchase agreement,” planningandmodelinglargedatacenterinterconnections.
RockyMountainInstitute,2018. [134] White & Case LLP, “NERC tees up plan to assess grid risks associ-
[114] C. Lau and J. Aga, “Bottom line on renewable energy certificates,” ated with data centers,” https://www.whitecase.com/insight-alert/nerc-
Online, 2008. [Online]. Available: https://www.wri.org/research/ tees-plan-assess-grid-risks-associated-data-centers,2025,summaryof
bottom-line-renewable-energy-certificates
NERC’sLargeLoadsTaskForceandregulatorydevelopments.
| [115] Google, | “Moving | toward | 24×7 | carbon-free | energy | at Google |                |       |      |         |         |              |             |
| ------------- | ------- | ------ | ---- | ----------- | ------ | --------- | -------------- | ----- | ---- | ------- | ------- | ------------ | ----------- |
|               |         |        |      |             |        |           | [135] J. Kemp, | “U.S. | data | centres | and the | risk to grid | stability,” |
data centers: Progress and insights,” Google, White Paper, 2018. https://jkempenergy.com/2025/03/19/u-s-data-centres-and-the-risk-to-
[Online]. Available: https://www.gstatic.com/gumdrop/sustainability/ grid-stability/, 2025, regulatory considerations for load ride-through
24x7-carbon-free-energy-data-centers.pdf inAIandhyperscaledatacenters.
[116] L.Nicoletti,M.Ma,andD.Bass,“AIisdrainingwaterfromareasthat [136] X. Hao, P. Liu, and Y. Deng, “Joint optimization of operational cost
| need | it most,” | https://www.bloomberg.com/graphics/2025-ai-impacts- |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andcarbonemissioninmultipledatacentermicro-grids,”Frontiersin
data-centers-water-data,2025,accessed:2025-05-09. EnergyResearch,vol.12,p.1344837,2024.
[117] Y. Wu, I. Hua, and Y. Ding, “Not all water consumption is equal: [137] I.Riepin,T.Brown,andV.M.Zavala,“Spatio-temporalloadshifting
A water stress weighted metric for sustainable computing,” ACM for truly clean computing,” Advances in Applied Energy, vol. 17, p.
| SIGENERGY |     | Energy | Informatics | Review, vol. | 5, no. | 2, pp. 84–90, | 100202,2025. |     |     |     |     |     |     |
| --------- | --- | ------ | ----------- | ------------ | ------ | ------------- | ------------ | --- | --- | --- | --- | --- | --- |
2025. [138] “Energy management in data centers and renewable energy
[118] N.Lei,J.Lu,A.Shehabi,andE.Masanet,“Thewateruseofdatacenter
|     |     |     |     |     |     |     | systems,” | Nature | Research | Intelligence, |     | accessed | August 2025. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | ------------- | --- | -------- | ------------ |
workloads: A review and assessment of key determinants,” Resour. [Online]. Available: https://www.nature.com/research-intelligence/nri-
Conserv.Recycl.,vol.219,p.108310,Jun.2025. topic-summaries/energy-management-in-data-centers-and-renewable-
[119] L.Cupelli,T.Schu¨tz,P.Jahangiri,M.Fuchs,A.Monti,andD.Mu¨ller, energy-systems-micro-2932
“Data center control strategy for participation in demand response [139] A. Radovanovic´, R. Koningstein, I. Schneider, B. Chen, A. Duarte,
programs,” IEEE Transactions on Industrial Informatics, vol. 14, B.Roy,D.Xiao,M.Haridasan,P.Hung,N.Careetal.,“Carbon-aware
no.11,pp.5087–5099,Nov.2018. computing for datacenters,” IEEE Transactions on Power Systems,
[120] S. Ma, Y. Liu, Y. Liu, J. Wang, Q. Fang, and Y. Huang, “Artificial vol.38,no.2,pp.1270–1280,Mar.2023.
intelligence-enabledpredictiveenergysavingplanningofliquidcooling [140] “Green computing,” wikipedia, accessed August 2025. [Online].
systemfordatacenters,”Adv.Eng.Inf.,vol.65,p.103283,May2025. Available:https://en.wikipedia.org/wiki/Green computing

18
[141] J. Lindberg, B. C. Lesieutre, and L. Roald, “The environmen- [161] N. O’Connell, P. Pinson, H. Madsen, and M. O’Malley, “Benefits
tal potential of hyper-scale data centers: Using locational marginal and challenges of electrical demand response: A critical review,”
CO2 emissions to guide geographical load shifting,” arXiv preprint Renewable and Sustainable Energy Reviews, vol. 39, pp. 686–
arXiv:2010.03379,2020. 699,2014.[Online].Available:https://www.sciencedirect.com/science/
[142] E.Ela,B.Kirby,N.Navid,andC.Smith,“Effectiveancillaryservices article/pii/S1364032114005504
market designs on high wind power penetration systems,” National [162] AI Energy Score, “AI energy score—energy efficiency ratings for AI
Renewable Energy Laboratory (NREL), Tech. Rep. NREL/TP-5500- models,”https://huggingface.github.io/AIEnergyScore/,2025.
53514, 2011. [Online]. Available: https://www.nrel.gov/docs/fy12osti/ [163] A. R. Jordehi, “Optimisation of demand response in electric power
53514.pdf systems, a review,” Renewable and sustainable energy reviews, vol.
[143] M. Spieler, “How AI Factories Can Help Relieve Grid Stress,” Jul. 103,pp.308–319,Apr.2019.
2025. [Online]. Available: https://blogs.nvidia.com/blog/ai-factories- [164] X.Chen,Y.Li,J.Shimada,andN.Li,“Onlinelearninganddistributed
flexible-power-use/ controlforresidentialdemandresponse,”IEEETransactionsonSmart
[144] D. Lazzaro, A. E. Cina`, M. Pintor, A. Demontis, B. Biggio, F. Roli, Grid,vol.12,no.6,pp.4843–4853,2021.
and M. Pelillo, “Minimizing energy consumption of deep learning [165] A. Shehabi, A. Hubbard, A. Newkirk, N. Lei, M. A. B. Siddik,
models by energy-aware training,” in International Conference on B. Holecek, J. Koomey, E. Masanet, D. Sartor et al., “2024
ImageAnalysisandProcessing. Springer,2023,pp.515–526. United States data center energy usage report,” Lawrence Berkeley
[145] E.Paula,J.Soni,H.Upadhyay,andL.Lagos,“Comparativeanalysis National Laboratory, Tech. Rep., Dec. 2024. [Online]. Available:
of model compression techniques for achieving carbon efficient AI,” https://escholarship.org/uc/item/32d6m0d1
ScientificReports,vol.15,no.1,p.23461,2025. [166] Reuters, “How prepared are US grid operators for extreme
[146] Synced. (2023) Google reveals its latest TPU v4-based heat this summer?” 2025, accessed: 2025-08-01. [Online].
supercomputer, which betters NVIDIA’s A100s in speed Available:https://www.reuters.com/business/energy/how-prepared-are-
and efficiency. Accessed: 2025-07-18. [Online]. Available: us-grid-operators-extreme-heat-this-summer-2025-08-01/
https://syncedreview.com/2023/04/06/google-reveals-its-latest-tpu- [167] ThaneMoore,“Examiningdatacenterenergyconsumptionandpower
v4-based-supercomputer-which-betters-nvidias-a100s-in-speed-and- sources,” https://blog.enconnex.com/data-center-energy-consumption-
efficiency/ and-power-sources,Jun.2024,accessed:2025-08-01.
[147] V. Bolo´n-Canedo, L. Mora´n-Ferna´ndez, B. Cancela, and A. Alonso- [168] South China Morning Post, “China hopes to power AI
Betanzos, “A review of green artificial intelligence: Towards a more boom with green energy in new data centre strategy,”
sustainablefuture,”Neurocomputing,vol.599,p.128096,2024. https://www.scmp.com/economy/china-economy/article/3313194/
[148] Taking a hybrid approach to data centre cooling - Data Centre china-hopes-power-ai-boom-green-energy-new-data-centre-strategy,
Review. [Online]. Available: https://datacentrereview.com/2024/06/ 2024,accessed:2025-08-01.
taking-a-hybrid-approach-to-data-centre-cooling/ [169] CarbonBrief,“Explainer:HowChinaismanagingtherisingenergyde-
[149] K. Chien, “A guide to data center cooling: Future innovations mand from data centres,” https://www.carbonbrief.org/explainer-how-
for sustainability.” [Online]. Available: https://www.digitalrealty.com/ china-is-managing-the-rising-energy-demand-from-data-centres/,
resources/articles/future-of-data-center-cooling 2024,accessed:2025-08-01.
[150] S. Zheng, C. Su, X. Yang, Y. Zhang, K. Duan, Y. Zhang, Z. Huang, [170] Reuters, “Europe’s data centre power demand expected to
Y.Zhang,F.Liu,andJ.Wei,“Acomprehensivereviewofsingle-phase triple by 2030, mckinsey report says,” https://www.reuters.com/
immersioncoolingindatacentres,”AppliedThermalEngineering,vol. technology/europes-data-centre-power-demand-expected-triple-by-
272,p.126385,Aug.2025. 2030-mckinsey-report-says-2024-10-23/,2024,accessed:2025-08-01.
[151] N. M. Mohammed, W. M. El-Maghlany, M. Elhelw, and A. H. [171] Climate Neutral Data Centre Pact, “Climate neutral data centre pact:
Abdelaziz,“Performanceimprovementofhigh-densitydatacentervia European initiative to achieve climate neutrality by 2030,” https:
two-phase liquid immersion cooling,” Journal of Thermal Analysis //en.wikipedia.org/wiki/Climate Neutral Data Centre Pact, 2024, ac-
andCalorimetry,vol.150,no.6,pp.4279–4294,Mar.2025.[Online]. cessed:2025-08-01.
Available:https://doi.org/10.1007/s10973-025-14006-0 [172] ITPro,“OpenAIisteamingupwithNscaleandAkertobuildEurope’s
[152] X.Chen,G.Qu,Y.Tang,S.Low,andN.Li,“Reinforcementlearning first AI gigafactory: Stargate norway to host 100,000 NVIDIA
forselectivekeyapplicationsinpowersystems:Recentadvancesand GPUs,” https://www.itpro.com/infrastructure/openai-is-teaming-up-
future challenges,” IEEE Transactions on Smart Grid, vol. 13, no. 4, with-nscale-and-aker-to-build-europes-first-ai-gigafactory-stargate-
pp.2935–2958,2022. norway-is-set-to-host-100-000-nvidia-gpus-and-will-be-powered-by-
[153] H. Kahil, S. Sharma, P. Va¨lisuo, and M. Elmusrati, “Reinforcement renewable-energy,2024,accessed:2025-08-01.
learning for data center energy efficiency optimization: A systematic [173] E. Cremona and P. Czyzak, “Grids for data centres: ambitious
literaturereviewandresearchroadmap,”AppliedEnergy,vol.389,p. grid planning can win Europe’s AI race,” Ember, Tech. Rep.,
125734,2025. Jun. 2025, accessed: 2025-08-21. [Online]. Available: https://ember-
[154] Y. Ran, H. Hu, Y. Wen, and X. Zhou, “Optimizing energy efficiency energy.org/app/uploads/2025/06/Grids-for-data-centres-in-Europe.pdf
fordatacenterviaparameterizeddeepreinforcementlearning,”IEEE
Transactions on Services Computing, vol. 16, no. 2, pp. 1310–1323,
2022.
[155] X. Zhan, X. Zhu, P. Cheng, X. Hu, Z. He, H. Geng, J. Leng,
H. Zheng, C. Liu, T. Hong, Y. Liang, Y. Liu, and F. Zhao,
“Data center cooling system optimization using offline reinforcement
learning,” in The Thirteenth International Conference on Learning
Representations (ICLR 2025), 2025. [Online]. Available: https:
//openreview.net/forum?id=W8xukd70cU
[156] J. Luo, C. Paduraru, O. Voicu, Y. Chervonyi, S. Munns, J. Li,
C.Qian,P.Dutta,J.Q.Davis,N.Wuetal.,“Controllingcommercial
cooling systems using reinforcement learning,” Dec. 2022. [Online].
Available:https://arxiv.org/abs/2211.07357
[157] E.Oro´,V.Depoorter,A.Garcia,andJ.Salom,“Energyefficiencyand
renewableenergyintegrationindatacentres.strategiesandmodelling
review,”RenewableandSustainableEnergyReviews,vol.42,pp.429–
445,Feb.2015.
[158] R. Rubei, A. Moussaid, C. Di Sipio, and D. Di Ruscio, “Prompt
engineering and its implications on the energy consumption of large
languagemodels,”arXivpreprintarXiv:2501.05899,2025.
[159] M.Adamska,D.Smirnova,H.Nasiri,Z.Yu,andP.Garraghan,“Green
prompting,”arXivpreprintarXiv:2503.10666,2025.
[160] E. J. Husom, A. Goknil, L. K. Shar, and S. Sen, “The price of
prompting: Profiling energy use in large language models inference,”
arXivpreprintarXiv:2407.16893,2024.