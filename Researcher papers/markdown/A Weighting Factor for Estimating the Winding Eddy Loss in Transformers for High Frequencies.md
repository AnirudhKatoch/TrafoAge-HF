2020 6th IEEE International Energy Conference (ENERGYCON)
A Weighting Factor for Estimating the Winding
Eddy Loss in Transformers for High Frequencies
Bonginkosi A. Thango Jacobus A. Jordaan Agha F. nnachi
Dept. of Electrical Engineering Dept. of Electrical Engineering Dept. of Electrical Engineering
Tshwane University of Technology Tshwane University of Technology Tshwane University of Technology
eMalahleni,South Africa eMalahleni, South Africa eMalahleni, South Africa
thangotech@gmail.com JordaanJA@tut.ac.za NnachiAF@tut.ac.za
Abstract—In this paper, a method for estimating the winding describe the effective thermal effect on account of the
Eddy Loss based on an improved harmonic loss factor for distorted harmonic load current. As a result of skin effect
transformers under harmonic conditions is presented. The phenomena, the electromagnetic flux cannot completely
method considers the skin depth of penetration of the field at penetrate the winding conductor surface at high frequency.
higher harmonic orders, leading to a greater degree an accurate Therefore, an exponent of two utilized in the assumption that
estimation of the winding Eddy losses under harmonic the winding Eddy losses progress with the square of the
conditions.
harmonic order is on the conservative side [8], [9]. The
authors in [10], [11], [12], [13] and [14] have presented the
Keywords—Winding Eddy Losses, Harmonics loss factor,
harmonic factor to determine the capability of transformer
Harmonic conditions
under harmonic conditions. In this paper, windingEddy loss
I. INTRODUCTION estimation based on animprovedharmoniclossfactor(HLF)
for transformers under harmonic conditions. A comparative
South Africa has now a generating capacity larger than a
study between the proposed HLF[15] and IEEE method [7]is
gigawatt of utility-scale solar photovoltaic (USSP) power
presented.
plants, grasping the 10th position in the world for countries
using solar power. The Republic of China currently is the II. IEEE RECOMMENDED PRACTICE C57.10-2018
world leader for the deployment of USSP power having 370
USSP generating plants, producing a snowballing 12GW. A. Review of harmonic losses
Other countries on top of the list include the United States of Transformers are designed such that they supply the
America (11GW), United Kingdom (4GW), Germany required continuous power with maximum efficiency and low
(3.6GW), India (3.3GW), Spain (1.5GW), Japan (1.4GW) losses. The losses in transformers are categorized into the no-
Canada (1.4GW) and France (31.3GW) [1]. load((cid:1842) )and load loss((cid:1842) )as follows in eq. (1).
(cid:3015)(cid:3013) (cid:3013)(cid:3013)
Being recently mentioned, this lodges South Africa in the
10th place with about 26 USSP generating plants, supplying (cid:2) (cid:1842) (cid:3021)(cid:3016)(cid:3021)(cid:3002)(cid:3013) (cid:3404)(cid:1842) (cid:3015)(cid:3013) (cid:3397)(cid:1842) (cid:3013)(cid:3013) (cid:3)(cid:4)(cid:5)(cid:2)
1.1 GW to the country’s power grid. Recent reports [2],
indicate that there are about 18 USSP plants under progress in The no-load loss is caused by the induced voltage
South Africa. These plants are forecasted to contribute an excitation in the core. This loss is reliant on the maximum flux
additional 1GW capacity. The excellent solar radiation in levels essential to magnetize the core and is insignificant in
South Africa definitely promise a bright future for USSP terms of the current harmonics. On the other hand, the load
plants. However, the significance of harmonics and distortion loss can further be stated as follows in eq. (2), as an arithmetic
in the electrical grid has heightened substantially in the last sum of the copper loss ((cid:1842) (cid:3010)(cid:2870)(cid:3019) ), winding Eddy loss ((cid:1842) (cid:3006)(cid:3004) ) and
decade due to the use non-linear loads that draw current during the metal partsloss((cid:1842) (cid:3014)(cid:3017) ).
start up and produce high frequencies. Many a lot of
transformers facilitating USSP plants to supply linear loads (cid:2) (cid:1842) (cid:3404)(cid:1842) (cid:3397)(cid:1842) (cid:3397)(cid:1842) (cid:3)(cid:6)(cid:5)(cid:2)
(cid:3013)(cid:3013) (cid:3010)(cid:2870)(cid:3019) (cid:3006)(cid:3004) (cid:3014)(cid:3017)
with sinusoidal load currents have their loads progressively
replaced with non-linear loads that infuse distorted harmonic The copper loss is predominantly caused by the root mean
currents. These harmonic current content derive increased square (rms) harmonic current and the direct current (DC)
losses and therefore bring about peculiar winding temperature resistance. The significant amount of rms current caused by
rise and consequently reduce the intended service lifetime of harmonics will increase the copper losses.The Eddy current
the transformer [3], [4], [5] and [6]. As a result, the losses in the transformer windings are as a result of the
transformer requires a suitable selection of the continuous fluctuating electromagnetic field on the surface of the winding
power rating (derating) or installation of a new and thrifty conductors. The skin and proximity effects are the two
transformer. phenomenon’s that cause additional losses in the windings
[16], [17]. As a result of the excitation current, the high
The IEEE std. C57. 10-2018[7], was established on the
voltage winding produces a flux density, in which pierce
basis to determine the capability of a transformer when during
through the low voltage winding and the core to induce an
the design stage for supplying the non-linear loads if the
internal voltage that derive the circulating and Eddy currents.
harmonic spectrum of the USSP plants is known.
A transformer design philosophy is such that the internal
Alternatively, the recommended practice can be extended to
winding, generally the low voltage winding, will have a
existing transformers in service. The winding Eddy loss is
significant amount of the Eddy current loss due to the intensity
presumed to be progressive with the square of the harmonic
of the electromagnetic near the core casing the windings.
order. The term harmonic loss factor was coined in efforts to
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 27,2026 at 17:21:07 UTC from IEEE Xplore. Restrictions apply.
978-1-7281-2956-3/20/$31.00 ©2020 IEEE 489

2020 6th IEEE International Energy Conference (ENERGYCON)
According to [7], the winding Eddy losses increase with the  III.  IMPROVED HARMONIC LOSS FACTOR
| product  | of  the  | square  | of  | the  | harmonic  | current  | and  the  |     |     |     |     |     |
| -------- | -------- | ------- | --- | ---- | --------- | -------- | --------- | --- | --- | --- | --- | --- |
At high harmonic orders,the tendencyof harmonic current
harmonic order. The expression for the winding Eddy losses
to flow through the outer layer of a winding conductor (skin
is as follows in eq. (3).
|     |     |     |     |                                                              |     |            |     | effect)  or                                 | the  restriction  | of  the  electromagnetic  |              | flux  to  |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | ---------- | --- | ------------------------------------------- | ----------------- | ------------------------- | ------------ | --------- |
|     |     |     |     |                                                              |     |            |     | completely penetrate the winding conductors |                   |                           | needs to be  |           |
|     |     |     |     | (cid:3035)(cid:2880)(cid:3035)(cid:3288)(cid:3276)(cid:3299) |     | (cid:2870) |     |                                             |                   |                           |              |           |
(cid:2) (cid:3010)(cid:3283)(cid:4673) (cid:3400)(cid:1860)(cid:2870) (cid:3)(cid:7)(cid:5)(cid:2) considered when estimating the winding Eddy losses. An
|     | (cid:1842) | (cid:3024)(cid:3006) (cid:3404)(cid:1842) | (cid:3024)(cid:3006)(cid:820)(cid:3019) | (cid:3400)(cid:3533) |     | (cid:4672) |     |     |     |     |     |     |
| --- | ---------- | ----------------------------------------- | --------------------------------------- | -------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(cid:3010)(cid:3267) Improved harmonic loss  factor is proposed based on the
(cid:3035)(cid:2880)(cid:2869)
equation as expressed in eq. (9)[15].
At lower harmonic order, the effect of the skin effect is
| m i n i m | u m   o n |   th e   t | ra n s f o | r m e r   w | i n d i n g |   c o n d | u c t o r s.     T h e |         |     |                                                                                                                                    |     |                               |
| --------- | --------- | ---------- | ---------- | ----------- | ----------- | --------- | ---------------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------- | --- | ----------------------------- |
|           |           |            |            |             |             |           |                        | (cid:2) |     | (cid:3095)(cid:3118)(cid:3033) (cid:3118) (cid:3021)(cid:3118)(cid:3003)(cid:3118) (cid:1832)(cid:4666)(cid:2022)(cid:4667)(cid:2) |     | (cid:3)(cid:13)(cid:5)(cid:2) |
co r r e sp o n di n g  h a rm o n ic   f a c to r   to   a c c o u n t  f o r  t h e   a d d it io n a l  (cid:959)(cid:1842) (cid:3404)
|     |     |     |     |     |     |     |     |     | (cid:3006)(cid:3004) | (cid:2871) (cid:3096) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --------------------- | --- | --- |
losses is as follows in eq. (4).
|     |     |     |     |                                                              |     |     |     | The  correction                          | function  | under harmonic  | conditions  | is  |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | ---------------------------------------- | --------- | --------------- | ----------- | --- |
|     |     |     |     | (cid:3283)(cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299) |     |     |     | expressed as follows in eq. (10).(cid:2) |           |                 |             |     |
(cid:3258)(cid:3283)(cid:3440) (cid:3118)
|     |     |     | (cid:3534) |     | (cid:3436) | (cid:3400)(cid:3035)(cid:3118) |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | ---------- | ------------------------------ | --- | --- | --- | --- | --- | --- |
(cid:3258)(cid:3267)
| (cid:2) |     | (cid:1832) | (cid:3404) | (cid:3283)(cid:3128) (cid:3117) |     |     | (cid:3)(cid:8)(cid:5)(cid:2) |     |     |     |     |     |
| ------- | --- | ---------- | ---------- | ------------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
(cid:3024)(cid:3006) (cid:3283) (cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299) (cid:2) (cid:1832)(cid:4666)(cid:2022)(cid:4667)(cid:3404) (cid:2871) (cid:3046) (cid:3036)(cid:3041) (cid:3035) (cid:3093) (cid:2879) (cid:3046)(cid:3036) (cid:3041) (cid:3085) (cid:2) (cid:3)(cid:4)(cid:14)(cid:5)(cid:2)
|     |     |     |     |            | (cid:3258)(cid:3283)(cid:3440) | (cid:3118) |     |     |     |                                                                                                                        |     |     |
| --- | --- | --- | --- | ---------- | ------------------------------ | ---------- | --- | --- | --- | ---------------------------------------------------------------------------------------------------------------------- | --- | --- |
|     |     |     |     | (cid:3534) | (cid:3436)                     |            |     |     |     | (cid:3093)(cid:3030) (cid:3042) (cid:3046)(cid:3035) (cid:3093) (cid:2879) (cid:3030) (cid:3042) (cid:3046) (cid:3093) |     |     |
(cid:3258)(cid:3267)
(cid:3283)(cid:3128)(cid:3117)
The conductor dimension related to the skin depth under
All the metallic structures in the transformer active part
rated conditions is expressed as follows in eq. (11).
undergo an internally induced voltage that results in the flow
of Eddy currents on the surface of ferromagnetic materials.
(cid:3009)(cid:3278)(cid:3290)(cid:3289)(cid:3279)(cid:484)(cid:2)
The Eddy currents generate losses that are manifested in the  (cid:2) (cid:2014) (cid:3404) (cid:3)(cid:4)(cid:4)(cid:5)(cid:2)
(cid:3019)
(cid:3083)(cid:3267)
form of heat energy, producing supplemental temperature rise
within the metallic structures and its surrounding. Other stray  The depth of penetration ((cid:2012) ) at fundamental frequency
(cid:3019)
losses generally refer to the Eddy current losses outside from  (50Hz)is expressed as follows in eq. (12)
the windings. The other stray losses in the Tank Walls, Flitch
plates, Core Clamps, frames, core etc. are proportional to the
product of the square of the harmonic current and exponent  (cid:2) (cid:2012) (cid:3404)(cid:3495) (cid:3096) (cid:2) (cid:3)(cid:4)(cid:6)(cid:5)(cid:2)
(cid:3019)
0.8 of the harmonic order.  The expression of the other stray  (cid:3091)(cid:3095)(cid:3033)
losses is as follows in eq. (5).
|     |     |     |     |     |     |     |     | In rectangular | copper winding conductorsat fundamental  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------------------------------- | --- | --- | --- |
(cid:3035)(cid:2880)(cid:3035)(cid:3288)(cid:3276)(cid:3299) fr e q u e n c y   o f  5 0H z , (cid:2012) (cid:3404) (cid:891) (cid:484) (cid:889) (cid:1865) (cid:1865) . T h e   co n d u ct o r  d i m e n s io n
|     |     |     |     |     |     | (cid:3010)(cid:3283)(cid:4673) (cid:2870) |     |     | (cid:3019) |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | ---------- | --- | --- | --- |
(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:1842) (cid:3404)(cid:1842) (cid:3400)(cid:3533) (cid:4672) (cid:3400)(cid:1860)(cid:2870)        (cid:3)(cid:9)(cid:5)(cid:2) r e la t e d   t o   t h e  sk i n   de pt h   u n de r  h a r m o n i c c o n d i tio n s   i s
|     |     | (cid:3014)(cid:3017) | (cid:3017)(cid:3014)(cid:820)(cid:3019) |     |                                |                      |     |                                          |     |     |     |     |
| --- | --- | -------------------- | --------------------------------------- | --- | ------------------------------ | -------------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
|     |     |                      |                                         |     | (cid:3035)(cid:2880)(cid:2869) | (cid:3010)(cid:3267) |     | expressed as follows in eq. (13).(cid:2) |     |     |     |     |
The corresponding harmonic loss factor to account for the
|     |     |     |     |     |     |     |     | (cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2014) |     | (cid:3404)(cid:2014) (cid:958)(cid:1860)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:3)(cid:4)(cid:7)(cid:5)(cid:2) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
additional losses are expressed as shown in eq. (6).   (cid:3035) (cid:3019)
The function ((cid:1832)(cid:4666)(cid:2022)(cid:4667))is as demonstrated in Fig. 2for values
(cid:3283)(cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299)
(cid:3118)
(cid:3534) (cid:3436) (cid:3258)(cid:3283)(cid:3440) (cid:3400)(cid:3035)(cid:3116)(cid:484)(cid:3124) of (cid:2022) between 0 and 10. At (cid:3)(cid:2022) (cid:3404)(cid:883) The correction function
(cid:3258)(cid:3267)
(cid:2) (cid:3283)(cid:3128)(cid:3117) (cid:3)(cid:10)(cid:5)(cid:2) (cid:1832)(cid:4666)(cid:2022)(cid:4667)(cid:3406)(cid:883)and at low harmonic orders the winding Eddy loss
|     |     | (cid:1832) (cid:3014)(cid:3017) | (cid:3404) |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:3283)(cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299) (cid:3118) i s   p r o p o r t i o n a l  t o   th e  square  of  the  harmonic  order and
|                              |     |            |     | (cid:3534)                     | (cid:3258) (cid:3283)(cid:3440) |          |            |                   |                       |     |     |     |
| ---------------------------- | --- | ---------- | --- | ------------------------------ | ------------------------------- | -------- | ---------- | ----------------- | --------------------- | --- | --- | --- |
|                              |     |            |     |                                | (cid:3436) (cid:3258)           |          |            | c o n d u c t o r |   d i m e n s io n s. |     |     |     |
|                              |     |            |     | (cid:3283)(cid:3128)(cid:3117) | (cid:3267)                      |          |            |                   |                       |     |     |     |
| B. Maximum loading capacity  |     |            |     |                                |                                 |          |            | 1                 |                       |     |     |     |
| Transformers                 |     | generally  |     | have                           | a  high                         | initial  | price  of  |                   |                       |     |     |     |
0,9
| installation. Additionally, substituting them at the end of their  |     |     |     |     |     |     |     | 0,8 |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
service life has a huge financial and technical challenges.
0,7
| Accordingly,                                                |     | a  complete  |     | inspection  | into  | the  | transformer  |     |     |     |     |     |
| ----------------------------------------------------------- | --- | ------------ | --- | ----------- | ----- | ---- | ------------ | --- | --- | --- | --- | --- |
| secured operation leads to essential financial advantages.  |     |              |     |             |       |      |              | 0,6 |     |     |     |     |
0,5
)ζ(F
| (cid:2) | (cid:1842)                                                                      | (cid:3404)(cid:1835)(cid:2870) |                                                   | (cid:3435)(cid:883)(cid:3397)(cid:1832) |                                | (cid:3400)(cid:1842)                                                                     | (cid:3439) (cid:3)(cid:11)(cid:5)(cid:2) | 0,4 |     |     |     |     |
| ------- | ------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------- | --------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
|         | (cid:3024)(cid:3006)(cid:3004)(cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667) |                                | (cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667) |                                         | (cid:3024)(cid:3006)(cid:3004) | (cid:3006)(cid:3004)(cid:820)(cid:3019)(cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667) |                                          |     |     |     |     |     |
0,3
| The recommended procedure described in [7] for oil- |     |     |     |     |     |     |     | 0,2 |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
immersed transformers is founded on the condition that the
0,1
| per-  unit                                              | distorted  |     | harmonic  | current  |     | will  generate  | some  |     |     |     |     |     |
| ------------------------------------------------------- | ---------- | --- | --------- | -------- | --- | --------------- | ----- | --- | --- | --- | --- | --- |
| thermal heating on the winding conductors. The maximum  |            |     |           |          |     |                 |       | 0   |     |     |     |     |
permissible current. This effect is expressed as follows in eq.  1 2 3 4 5 6 7 8 9 10
ζ
(8).
The function (cid:1832)(cid:4666)(cid:2022)(cid:4667)
|     |     |     |     | (cid:3017)(cid:3261)(cid:3261)(cid:3127)(cid:3267)(cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667) |     |     | (cid:3)(cid:3)(cid:3)(cid:3)(cid:3)(cid:3)(cid:3)(cid:12)(cid:5)(cid:2) |     | Fig. 1.  |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------------------------------------- | --- | --- | ----------------------------------------------------------------------- | --- | -------- | --- | --- | --- |
      (cid:1835) (cid:4666)(cid:1868)(cid:1873)(cid:4667)(cid:3404)(cid:3495)
| (cid:3040)(cid:3028)(cid:3051) |     | (cid:2869)(cid:2878)(cid:3007)(cid:3272)(cid:3254)(cid:3252)(cid:3400)(cid:3017)(cid:3272)(cid:3254)(cid:3252)(cid:3127)(cid:3267)(cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667)(cid:2878)(cid:3007)(cid:3265)(cid:3262)(cid:3400)(cid:3017)(cid:3265)(cid:3262)(cid:820)(cid:3267)(cid:4666)(cid:3043)(cid:484)(cid:3048)(cid:4667) |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Standardizing of the winding Eddy loss generated by
This makes the assumption that the normal insulation life  harmonic  currents  an  improved  harmonic  loss  factor  is
of the transformer will be sustained.
achieved as expressed in eq. (14).
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 27,2026 at 17:21:07 UTC from IEEE Xplore.  Restrictions apply.
490

(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:1842) (cid:1499) (cid:3404)(cid:1842) (cid:3400)(cid:3533) (cid:3035)(cid:2880)(cid:3035)(cid:3288)(cid:3276)(cid:3299) (cid:4672) (cid:3007)(cid:4666)(cid:3093)(cid:3283)(cid:4667) (cid:4673)(cid:4672) (cid:3010)(cid:3283)(cid:4673) (cid:2870) (cid:3400)(cid:1860)(cid:2870) (cid:3)(cid:4)(cid:8)(cid:5)(cid:2)
(cid:3014)(cid:3017) (cid:3017)(cid:3014)(cid:820)(cid:3019)
(cid:3035)(cid:2880)(cid:2869)
(cid:3007)(cid:4666)(cid:3093)(cid:3293)(cid:4667) (cid:3010)(cid:3267)
The harmonic loss factor to account for the harmonic
content that will be endured by the transformer while in
service in expressed in eq. (15).
(cid:3283)(cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299) (cid:3118)
(cid:3534) (cid:3436) (cid:3255)(cid:3435)(cid:3341)(cid:3283)(cid:3439) (cid:3440)(cid:3436) (cid:3258)(cid:3283)(cid:3440) (cid:3400)(cid:3035)(cid:3118)
(cid:2) (cid:1832) (cid:1499) (cid:3404) (cid:3283)(cid:3128)(cid:3117)
(cid:3255)(cid:4666)(cid:3341)(cid:3293)(cid:4667) (cid:3258)(cid:3267)
(cid:3)(cid:4)(cid:9)(cid:5)(cid:2)
(cid:3024)(cid:3006)
(cid:3534)
(cid:3283)(cid:3128)(cid:3283)(cid:3288)(cid:3276)(cid:3299)
(cid:3436)
(cid:3258)(cid:3283)(cid:3440) (cid:3118)
(cid:3258)(cid:3267)
(cid:3283)(cid:3128)(cid:3117)
The significance of the above improved harmonic factor Fig. 3. Harmonic spectrum load current
is illustrated in fig. 3, at which the curves are demonstrated
as a function of the harmonic order for various copper The rated losses and corresponding load losses under the
rectangular conductor dimensions. The curve for h2 is supplied harmonic currents are presented in TABLE I. the
included for comparative purposes. It is observed that for load losses of the oil-filled transformers are comprised of the
conductors with small dimensions, approach h2 at low copper loss, winding Eddy loss and Metal parts loss. The rms
harmonic order. current in p.u under the supplied harmonic profile for
transformer A and B is 1.107 and 1.224 respectively.
12000 TABLE I. TRANSFORMER FUNDAMENTAL LOSSES
10000 Transformer A Transformer B
Load Rated Load Losses
Type of Rated 8000 Losses Losses(W) (W) Loss Losses(W)
(W)
6000 No-Load 3,182 3,182 4,019 4,019
I2R 16,759 20,521 39,556 48,435
4000
Winding 541 661.952 724 886.766
Eddy
2000
Metal 1,091 1336 1,550 1898
parts
0
Total 21,573 25,701 45,849 55,239
1 5 9 13 17 21 25 29 33 37 41 45 49
A percentage breakdown of the loss distribution for
Fig. 2. The function h2(cid:1832)((cid:2022) h )/(cid:1832)((cid:2022) R ) vs. harmonic order h transformer A is presented in Fig. 5. A large portion is
observed to be the copper losses with about 78%. The
It can be well established from Fig. 3 that for winding
winding Eddies contribute about 2.5 % on the overall losses.
conductors with small dimension, the skin effect is negligible
and can be assumed to that the IEEE method estimate the
winding Eddy loss with accuracy. The IEEE method compute
the losses which are higher than the actual service losses for
conductors with large dimension at high harmonic order as a
result of the neglected limited depth of penetration. The
magnetic flux impinging upon the surface of the winding
conductors is minimum on account of skin effect.
IV. CASE STUDY:OIL IMMERSED TRANSFORMER
In this section, the impact of harmonic currents on oil-
filled transformers serving within a harmonically
contaminated environment is studied. The studied
transformers supply various linear and non-linear loads
during their operation period. The amount of harmonic
currents seen by the transformer during service is shown in
fig. 4. It is observed from the harmonic profile that the odd Fig. 4. Percentage Loss Distribution for transformer A
harmonics of the point of common coupling are significant
Similarly, a percentage breakdown of the loss distribution
then the even harmonics.
for transformer B is presented in Fig. 6. A large portion is
observed to be the copper losses with about 86%. The
winding Eddies contribute about 1.58 % on the overall losses.
) (cid:2022)((cid:1832)/)
(cid:2022)((cid:1832)2h
R
h
1
0,9
0,8
0,7
0,6
0,5
0,4
0,3
0,2
0,1
0
1 2 3 4 5 6 7 8 9 10 11 12 13
2mm
3mm
6mm
9mm
12mm
15mm
h^2
Harmonic Order h
)u.p(
tnerruc
cinomraH
2020 6th IEEE International Energy Conference (ENERGYCON)
Harmonic Order h
5,06
2,51 14,75
NLL
I2R
Winding Eddy
losses
OTHER EDDY
77,68
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 27,2026 at 17:21:07 UTC from IEEE Xplore. Restrictions apply.
491

2020 6th IEEE International Energy Conference (ENERGYCON)
on the IEEE std. C57. 10-2018, assuming an increase in the
winding Eddy loss with the square of the harmonic order.
3,38
|     | 1,58 |     | 8,77 |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
b) Transformer capacity
NLL
In this section, to account for the most undesirable thermal
operating conditions of a transformer, the winding Eddy loss
I2R
can be computed using eq. (7) and eq.(8) as shown in TABLE
IV.
Winding Eddy
|     |     |     |     | losses |     |     | TABLE IV.   | CAPACITY FOR TRANSFORMER A  |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | ----------- | --------------------------- | --- | --- | --- | --- |
OTHER EDDY
|     |       |     |     |     |     | Method |     | Pec (p.u) | Imax(p.u) |     | Imax |     |
| --- | ----- | --- | --- | --- | --- | ------ | --- | --------- | --------- | --- | ---- | --- |
|     | 86,27 |     |     |     |     |        |     | 1.482     | 0.916     |     | 601  |     |
IEEE
|     |     |     |     |     |     |     |     | 1.224 | 0.927 |     | 608 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- |
Improved
Fig. 5.  Percentage Loss Distribution for transformer B  The maximum permissible current (MPC) as calculated
in TABLE IV determines the maximum current that can flow
a) Estimation of service losses
|     |     |     |     |     |     | through  | the  | winding  conductors  |     | without  | a  significant  |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | -------------------- | --- | -------- | --------------- | --- |
In this section, the service losses for the transformers
degradation of the insulation. The computation of the MPC
| under  study  | are  presented  |     | taking  into  | consideration  | the  |     |     |     |     |     |     |     |
| ------------- | --------------- | --- | ------------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
allows the utility owners to protect the transformer from
harmonic content their susceptible to during their service life.
reduction of the intended service lifetime by regulating its
The winding conductor dimensions of 12.1x3.6mm and 14.2x
MPC. From TABLE IV, the IEEE and improved method have
1.6mm are considered for transformer Aand B respectively.
a MPC percentage error of about 8.45% and 7.27% when
compared to the rated current. Similarly both methods have a
It is observed in TABLE II that the improved harmonic
percentage error of 1.274%, while the winding Eddy loss has
factor is reduced by 15.8% compared to the IEEE method. As a percentage error of 17.37%. The capability of transformer
a result the winding Eddy loss and total losses are reduced by
B are shown in TABLE V.
15.8% and 2.3% respectively.
|             |                                               |     |     |     |     |     | TABLE V.   | CAPACITY FOR TRANSFORMER B  |           |     |      |     |
| ----------- | --------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --------------------------- | --------- | --- | ---- | --- |
| TABLE II.   | TRANSFORMER HARMONIC LOSSES FOR TRANSFORMER A |     |     |     |     |     |            |                             |           |     |      |     |
|             |                                               |     |     |     |     |     |            | Pec (p.u)                   | Imax(p.u) |     | Imax |     |
Method
| Type    | of  Load   | (cid:2162)           | IEEE   | (cid:2162) (cid:1499) | Corrected  |      |     |       |             |     |     |     |
| ------- | ---------- | -------------------- | ------ | --------------------- | ---------- | ---- | --- | ----- | ----------- | --- | --- | --- |
|         |            | (cid:2179)(cid:2161) |        | (cid:2179)(cid:2161)  |            |      |     | 1.371 | 0.947       |     | 621 |     |
| Loss    | Losses (W) |                      | Losses |                       | WEL        | IEEE |     |       |             |     |     |     |
| No-Load | 3,182      | -                    | 3,182  | -                     | 3,182      |      |     | 1.224 | 0.963789907 |     | 632 |     |
Improved
|     | 20,521 | -   | 20,521 | -   | 20,521 |     |     |     |     |     |     |     |
| --- | ------ | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
I2R
Winding  661.952 6.52 4,314 5.490 3,634 For transformer B, based on the IEEE and improved
Eddy
harmonic factor method, there is a percentage error of about
| Metal parts | 1336 | 1.52 | 2,033 | -   | 2,033 |     |     |     |     |     |     |     |
| ----------- | ---- | ---- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
5.29% and 3.62% on the maximum current when compared
Total 25,701 30,050 29,370 against the rated current. On the other hand, the both methods
have a percentage error of about 1.73%. Lastly, the winding
Asobserved in TABLE III, the harmonic factors are 5.78  Eddy losses Pec (p.u) have a  percentage error of about
| and 4.306 for the IEEE and Improved method respectively.  |     |     |     |     |     | 10.66%.  |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
As a result the winding Eddy losses are reduced by 34% as a
V.  CONCLUSION
| result  of  | the  improved  | harmonic  | factor  | and  | an  overall  |     |     |     |     |     |     |     |
| ----------- | -------------- | --------- | ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
reduction of 3.2% on the total losses.  The explanation given by the IEEE std. C57. 10-2018 that
provides a reason for observed increase in winding Eddy
losses under harmonic conditions as proportional to the square
| TABLE III.   | TRANSFORMER HARMONIC LOSSES FOR TRANSFORMERB  |            |       |            |                       |          |           |        |            |       |           |            |
| ------------ | --------------------------------------------- | ---------- | ----- | ---------- | --------------------- | -------- | --------- | ------ | ---------- | ----- | --------- | ---------- |
|              |                                               |            |       |            |                       | of  the  | harmonic  | order  | does  not  | hold  | for  all  | conductor  |
| Type         | of  Load                                      | (cid:2162) | IEEE  | (cid:2162) | (cid:1499) Corrected  |          |           |        |            |       |           |            |
(cid:2179)(cid:2161) (cid:2179)(cid:2161) dimensions.    This  method  is  reasonably  accurate  for
| Loss | Losses (W) |     | Losses |     | WEL |     |     |     |     |     |     |     |
| ---- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conductors with small dimensions. In the case of winding
| No-Load | 4,019 |     | - 4,019 | -   | 4,019 |     |     |     |     |     |     |     |
| ------- | ----- | --- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
conductors with large dimensions, such assumption leads to
|     | 48,435 |     | - 48,435 | -   | 48,435 |     |     |     |     |     |     |     |
| --- | ------ | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
I2R conservative  results.  Due  to  the  neglected  depth  of
Winding  886.766 6.52 5,780 4.30 3,819 penetration, the predicted losses will be higher than the actual
| Eddy |     |     |     | 6   |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
service losses. In reality the magnetic flux will not completely
|     | 1898 | 1.52 | 2,887 | -   | 2,887 |     |     |     |     |     |     |     |
| --- | ---- | ---- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Metal parts penetrate the conductors at high harmonic orders due to the
| Total | 55,239 |     | 61,121 |     | 59,160 | skin effect.   |     |     |     |     |     |     |
| ----- | ------ | --- | ------ | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- |
An improved harmonic loss factor which regards the depth
The results in this section, indicate that the effect of skin
of penetration of the magnetic field upon the surface of the
effect at high harmonic order plays a pivotal role in the
|     |     |     |     |     |     | winding  | conductors  | can  | be  applied  | to  | estimate  | more  |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | ------------ | --- | --------- | ----- |
estimation  of  the  winding  Eddy  losses.  A  significant  accurately  the  capability  of  transformers under harmonic
| reduction of the losses is observed due to the limitation of the  |                       |     |            |     |               | conditions.   |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --------------------- | --- | ---------- | --- | ------------- | ------------- | --- | --- | --- | --- | --- | --- |
| magnetic                                                          | flux  to  completely  |     | penetrate  |     | the  winding  |               |     |     |     |     |     |     |
conductors at high harmonic order. This effect is neglected
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 27,2026 at 17:21:07 UTC from IEEE Xplore.  Restrictions apply.
492

2020 6th IEEE International Energy Conference (ENERGYCON)
REFERENCES
[1] Electric Power Research Institute (EPRI), Power Generation
Technology Data for Integrated Resource Plan of South Africa,
Technical Update, April 2017.
[2] J. White,Availability and Cost of Capital for IPP Wind Energy Project
Financing in South Africa,IEEE The Energy Research Centre (ERC),
University of Cape Town (UCT), March 2010.
[3] E.Cazacu, V. Ionita, L. Petrescu” Thermal Aging of Power Distribution
Transformers Operating under Nonlinear and Balanced Load
Conditions”, Power Engineering and Electrical Engineering, Volume:
16 2018.
[4] I.A. Elmoudi 1 M. Lehtonen, H.Nordman ,” Effect of Harmonics on
Transformers Loss of life”, Conference Record of the IEEE
International Symposium on Electrical Insulation, 2006.
[5] D.M. Said and K.M. Nor,” Effects of Harmonics on Distribution
Transformers”, Australasian Universities Power Engineering
Conference (AUPEC'08), 2008.
[6] S.M.B. Sadati, B. D. Motevali et al,” Evaluation of Distribution
Transformer Losses and Remaining Life considering Network
Harmonic, Based on Analytical and Simulation Methods”, Australian
Journal of Basic and Applied Sciences, 2010.
[7] IEEE C57.110-2018-IEEE Recommended Practice for Establishing
Liquid Immersed and Dry-Type Power and Distribution Transformer
Capability when Supplying Nonsinusoidal Load Currents, June 2018.
[8] IEEE Std C57-110-1998, “Recommended Practice for Establishing
Transformer Capability when Supplying Non sinusoidal Load
currents”, 1998.
[9] D. Yildrim, E. Fuchs, " Transformer derating and comparison with
Harmonic Loss Factor Approach", IEEE Trans. 2000.
[10] A. Gado, “Effect of Types OF Loads In Rating of Transformers
Supplying Harmonic-Rich Loads”, 21st International conference on
electricity distribution, 2011.
[11] D.M. Said, K.M. Nor, “Simulation of the Impact of Harmonics on
Distribution Transformers”, 2nd IEEE International Conference on
Power and Energy, 2008.
[12] Sumaryadi, H. Gumilang, A. Susilo, “Effect of Power System
Harmonic on Degradation process of Transformer Insulation System”,
Proceedings of the 9th International Conference on Properties and
Applications of Dielectric Materials, 2009.
[13] M.E. Balci, “On the no-load loss of power transformers under voltages
with sub-harmonics”, IEEE International Energy Conference
(ENERGYCON), 2014.
[14] H. Nugraha,” Comparison of Distribution Transformer Losses and
Capacity under Linear and Harmonic Loads”, 21st International
conference on electricity distribution, 2011.
[15] J.J Thompson, On the Heat Produced by Eddy Currents in an Iron Plate
Exposed to an Alternating Magnetic Field, The electrician, April 1892.
[16] IEEE Power and Energy Society “IEEE Recommended Practice and
Requirements for Harmonic Control in Electric Power Systems”, 2014.
[17] IEEE C57.110, “IEEE Recommended Practice for Establishing Liquid
Immersed and Dry-Type Power and Distribution Transformer
Capability when Supplying Nonsinusoidal Load Currents”, 2018.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 27,2026 at 17:21:07 UTC from IEEE Xplore. Restrictions apply.
493