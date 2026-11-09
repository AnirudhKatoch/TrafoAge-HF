CC II RR EE DD(cid:3)
(cid:3)

(cid:20)(cid:27)(cid:87)(cid:75)(cid:3)(cid:44)(cid:81)(cid:87)(cid:72)(cid:85)(cid:81)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:68)(cid:79)(cid:3)(cid:38)(cid:82)(cid:81)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)(cid:3)(cid:82)(cid:81)(cid:3)(cid:40)(cid:79)(cid:72)(cid:70)(cid:87)(cid:85)(cid:76)(cid:70)(cid:76)(cid:87)(cid:92)(cid:3)(cid:39)(cid:76)(cid:86)(cid:87)(cid:85)(cid:76)(cid:69)(cid:88)(cid:87)(cid:76)(cid:82)(cid:81)(cid:3)

(cid:55)(cid:88)(cid:85)(cid:76)(cid:81)(cid:15)(cid:3)(cid:25)(cid:16)(cid:28)(cid:3)(cid:45)(cid:88)(cid:81)(cid:72)(cid:3)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)

DISTURBANCES DUE TO VOLTAGE DISTORTION IN THE KHZ RANGE – EXPERIENCES AND
MITIGATION MEASURES

Christian UNGER, Kurt KRÜGER, Martin SONNENSCHEIN, Rainer ZUROWSKI
Siemens AG, Erlangen, Germany
christian.unger@siemens.com

SUMMARY

equipment producing substantial distortion in the kHz range
will increase in the near future.

Disturbances in power systems due to oscillations of several
kilohertz  (1  ..  15  kHz)  superimposed  to  the  fundamental
became more and more important in recent years. The paper
discusses causes for this development such as the increased
use of PWM converters (e.g. for drives or FACTS devices) or
reduction  in  system  damping  together  with  ordinary
converter  load  leading  to  an  excitation  of  natural  system
frequency know as commutation oscillations. Measurement
results  as  well  as  examples  from  several  cases  of
disturbances investigated by the authors will be presented.
The effects of these disturbances vary in a wide range such as
malfunction  of  electronic  office  equipment,  blown  power
supply  units,  malfunction  of  electronic  controls  or
unacceptable noise.

INTRODUCTION

For many years, in respect to voltage waveform distortion,
the  main  focus  was  on  low-frequency  disturbances  in  the
harmonic range up to the 50th harmonic. In many practical
investigations, harmonics will be considered up to the 25th
only.  A  large  number  of  papers  deals  with  such  voltage
perturbations and they are well covered in many national and
international standards in order to allow a co-ordination of
disturbances and the immunity of equipment. However, as
practical  experiences  show,  the  amount  of  problems  with
steady-state voltages in the frequency range of several kilo-
Hertz have been steadily increasing over the last few years.
The authors found two major sources of such disturbances.
One  source  are  frequencies  generated  by  self-commutated
converters with an operating pulse frequency of several kHz.
The other main source are oscillations of a subsystem at its
natural frequency caused by the commutation of "ordinary"
line-commutated converters (commutation oscillations).

SELF-COMMUTATED CONVERTERS

Self-commutated  converters  are  used  increasingly  at  the
system side of variable speed drives (known as active front
end  –  AFE),  for  the  connection  of  d.c.  generating  devices
such as solar power panels or for special applications such as
active filters [1,2]. The power rating of devices with a pulse
frequency in the kHz range is still limited to a few MVA due
to  the  limitations  of  power  electronic  components,  in
particular  due  to  sharply  increasing  losses  for  higher
switching frequencies for high power components. Therefore,
most converters are connected to the LV level. However, it
can be predicted easily, that the number and power rating of

VR

VSystem

VConv

Fig. 1: Voltage division between reactor/transformer
impedance and system for a self-commutated converter

In  contrary  to  line-commutated  converters,  which  are
generally  considered  as  a  harmonic  current  sources,  self-
commutated  converters  need  to  be  considered  as  voltage
sources at the converter side of the transformer. (Figure 1).
The  respective  currents  result  from  the  magnitude  of  the
source  voltage  together  with  the  impedance  of  converter
transformer and system. The voltage distortion at the feeding
busbar is determined by the voltage divider formed by the
converter transformer and the supply network.
Fig.  2  gives  an  example  for  the  busbar  voltage  of  a  LV
subsystem  supplied  via  a  1  MVA  PWM-converter  with  a
pulse  frequency  of  3 kHz.  Typically,  the  spectrum  of  the
voltage distortion consists of several lines around the pulse
frequency  and  their  sidebands.  Obviously,  the  distortion
created in the harmonic range is quite low, that's why these
converters are often connected at points in the system where
simple  (and  less  expensive)  line-commutated  converters
create  harmonic  problems  due  to  the  weak  system  or
resonances  e.g.  caused  by  long  cables  and  would  required
additional shunt filters.

COMMUTATION OSCILLATIONS

Commutation oscillations are caused by the sudden voltage
dip caused by the 2-phase short-circuit during commutation
of a line-commutated converter. This voltage dip causes the
feeding system to oscillate at its natural frequency, which is
determined mainly by line capacitances and the inductance of
the  feeding  system  (Fig.  3).  Typical  frequencies  of  such
oscillations  in  the  LV  system  were  found  in  the  range  of
several  kHz  up  to  more  than  10  kHz.  In  most  cases,
substantial magnitudes of commutation oscillations can be
found  only  in  the  subsystem  where  the  converters  are
connected. The main factor determining their duration and
magnitude is the system damping. Since most of the damping
in  this  frequency  range  is  provided  in  many  cases  by
transformers,  the  development  towards  transformers  with

(cid:38)(cid:44)(cid:53)(cid:40)(cid:39)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)
(cid:3)
Session No 2
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:43 UTC from IEEE Xplore.  Restrictions apply.

CC II RR EE DD(cid:3)
(cid:3)

(cid:20)(cid:27)(cid:87)(cid:75)(cid:3)(cid:44)(cid:81)(cid:87)(cid:72)(cid:85)(cid:81)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:68)(cid:79)(cid:3)(cid:38)(cid:82)(cid:81)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)(cid:3)(cid:82)(cid:81)(cid:3)(cid:40)(cid:79)(cid:72)(cid:70)(cid:87)(cid:85)(cid:76)(cid:70)(cid:76)(cid:87)(cid:92)(cid:3)(cid:39)(cid:76)(cid:86)(cid:87)(cid:85)(cid:76)(cid:69)(cid:88)(cid:87)(cid:76)(cid:82)(cid:81)(cid:3)

(cid:55)(cid:88)(cid:85)(cid:76)(cid:81)(cid:15)(cid:3)(cid:25)(cid:16)(cid:28)(cid:3)(cid:45)(cid:88)(cid:81)(cid:72)(cid:3)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)

lower  and  lower  losses  supports  the  appearance  of
commutation oscillations. This is supported by a special case,
where the authors found commutation oscillations caused by
a large converter as the source of disturbances. The busbar
where the converter was connected was fed by two similar
transformers with their age being the main difference. One
was  taken  from  an  old  plant  and  the  other  one  was  new.
Commutation oscillations were found during the supply via
the new transformer only.

Uν/U1

Fig. 2: Busbar voltage with a self-commutated converter
connected; pulse frequency 3kHz (above: time characteristic,
below: spectrum)

f/Hz

In  the  last  few  years,  the  authors  investigated  many
disturbances  mainly  in  industrial  plants.  The  following
examples in respect to disturbances, which were found to be
caused by voltage components in the kHz range, give an idea
about the variety of possible problems.
• During  the  operation  of  a  converter-fed  pump  with  a
rating  of  several  MW,  loud  noise  caused  by  various
electronic  devices  disturbed
the  enthusiasm  for
employee's  work  in  a  nearby  office  building.  It  was
found out, that the supplying LV network was connected
to  the  same  MV  busbar  as  the  pumps.  These  drives
caused commutation oscillations in the range of about
12kHz and with a magnitude of about 40%, which could
be measured at the socket outlets of the office building.
In  the  case  of  one  computer  monitor  the  cause  of  the
noise  was  investigated  and  was  found  out  to  be  a
mechanical oscillation of ferrite cores used in the power
supply  of  the  monitor  probably  to  protect  it  against
voltage  surges.  As  a  solution,  the  feeder  transformer
supplying this LV network was shifted to another busbar
without any converters. The plant is operational by now
without
and  without
implementation of any further mitigation measures.
• During the operation of one individual machine tool in a
LV  system  with  several  ten  machines  connected  at  a
mechanical
commutation
oscillations similar to the one's of Fig. 3 were measured.
A photocopier produced copies with white stripes across
the copies during the operation of the machine. No other
disturbances were detected.

engineering

company,

problems

further

any

• Many LV converters are protected by varistors against
overvoltage surges. These varistors are often rated such
that  they  start  conducting  already  at  voltages  slightly
above  110%
rated  voltage.  With  commutation
oscillations  at  the  top  of  a  sine  wave  (Fig.  3)  and  a
fundamental  voltage  of  105%  rated  voltage,  10%
magnitude of the commutation oscillations are already
sufficient for the varistors to carry a short-term current at
each fundamental cycle. Since the varistors are designed
for short-term load due to transients only, after a certain
time varistors fail due to thermal overload.

• An industrial LV system supplies mainly a large amount
of  small  and  medium  size  variable  speed  drives  for
pumps,  motor  operators  etc.  Most  of  the  rectifiers
feeding the drives are equipped with shunt capacitors at
the system side probably for surge protection purposes,
but without commutation reactor. Busbar voltage and its
spectrum as well as supply current are depicted in Fig. 4.
The voltage waveform contains components in the lower
kHz-range of up to 0.9%. Most of the loads connected
operated without any problems, but some of the small
drives  failed  regularly  and  had  to  be  replaced.  The
reduced
magnitude  of  higher  harmonics  was
substantially  after  installation  of  small  commutation
reactors for the majority of the drives.

Fig. 3: Commutation oscillations with about 6kHz

measured at an industrial LV busbar with a machine tool
operating

EXAMPLES

(cid:38)(cid:44)(cid:53)(cid:40)(cid:39)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)
(cid:3)
Session No 2(cid:3)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:43 UTC from IEEE Xplore.  Restrictions apply.

CC II RR EE DD(cid:3)
(cid:3)

(cid:20)(cid:27)(cid:87)(cid:75)(cid:3)(cid:44)(cid:81)(cid:87)(cid:72)(cid:85)(cid:81)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:68)(cid:79)(cid:3)(cid:38)(cid:82)(cid:81)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)(cid:3)(cid:82)(cid:81)(cid:3)(cid:40)(cid:79)(cid:72)(cid:70)(cid:87)(cid:85)(cid:76)(cid:70)(cid:76)(cid:87)(cid:92)(cid:3)(cid:39)(cid:76)(cid:86)(cid:87)(cid:85)(cid:76)(cid:69)(cid:88)(cid:87)(cid:76)(cid:82)(cid:81)(cid:3)

(cid:55)(cid:88)(cid:85)(cid:76)(cid:81)(cid:15)(cid:3)(cid:25)(cid:16)(cid:28)(cid:3)(cid:45)(cid:88)(cid:81)(cid:72)(cid:3)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)

case  3  kHz).  Thus  spectral  lines  close  to  78  kHz  are
generated by the converter reducing the DCF 77 signal
level. An effective solution was not the installation of
additional filter circuits – which are difficult to design
and are even more difficult to connect properly – but to
change  the  switching  frequency  of  the  converter  to  5
kHz. Thus the DCF 77 signal is located exactly in the
middle  between  the  neighbouring  sidebands  leading
again to an undisturbed operation.

Fig. 5: Commutation oscillations caused by a machine tool
main spindle drive

IMPOSED LIMITS

International standardisation in the frequency range above the
50th harmonic is rather weak, leaving many uncertainties to
equipment  manufacturers,  utilities  and  private  network
operators. IEC 61000-2 proposes the following compatibility
levels  in  informative  annexes  only  for  voltages  in  the
frequency range between 50th harmonic and 9kHz:

•

0.2% for individual frequencies

•

0.3% for a frequency band with 200 Hz bandwidth
Certainly, voltages with such magnitudes will safely avoid
any  disturbances  due  to  these  frequencies  in  the  system.
to  self-commutated
However,  especially  with  regard
converters,  such  stringent  limits  might  be  prohibitive  for
many  useful  applications.  The  experience  of  the  authors
suggests that voltage limits in the range of 0.5% to 0.6% of
the  fundamental  would  not  increase  the  number  of
disturbances remarkably, but would substantially reduce the
effort  for  filtering  required  or  would  even  only  allow  the
application  itself.  In  the  case  of  the  LV  busbar  voltage
depicted in Fig. 2, an entire LV subsystem with various kinds
of  loads  is  operating  without  disturbances  although  the
magnitudes of the individual frequencies reach up to 0.8%.
IEC 61800 requires the consideration of overvoltages due to
commutation oscillations of up to 150% of the peak value of
the fundamental voltage (periodically) or even 250% (non-
periodically)  for  the  design  of  LV  converters.  This  design
criteria will certainly ensure safely, that the converters are
robust  and  are  unable  to  disturb  each  other.  However,  the
examples  given  above  show,  that  average  equipment  and
even converters for industrial use fail already at much lower
disturbance levels. At least, the design of all equipment to be
connected  in  an  industrial  environment  in  parallel  to

Fig. 4: Line-to-line voltage, feeder current and line-to-

ground voltage in an industrial LV subsystem (above),
spectrum of the voltage (below)

• An individual machine tool connected at a remote place
via  a  small  dedicated  transformer  is  working  trouble-
free. One day, a precision measuring device is connected
to a socket outlet in the control section of the machine
due to a lack of other power supply possibilities in the
vicinity.  Accelerating  the  main  spindle  drive  creates
immediately a black cloud coming out of the expensive
measuring device, being not able to measure anymore
before an expensive repair. The experiment was repeated
several times with the same result. The voltage during
the acceleration of the drive at the socket outlet shows
Fig. 5. Although the manufacturer of the machine offered
(optional) a filter in order to reduce system perturbations,
the owner decided to omit this costly accessory.

• Also a case of radiated disturbance is worth reporting: a
PWM voltage-source converter is installed in a utility
building  as  a  state-of  the  art  solution  for  dynamic
reactive power compensation. Several electronic control
devices in the same building use the so-called DCF 77
time  signal  radiated  at  77,5  kHz  as  a  time  base  for
internal  clocks.  The  building  is  located  in  a  valley
resulting
level.  After
commissioning  of  the  converter,  unusual  disturbances
were observed and correlated to the missing time signal.
It was found out, that the time signal is located in the
vicinity of multiples of the switching frequency (in this

low  receiving

in  a  very

(cid:38)(cid:44)(cid:53)(cid:40)(cid:39)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)
(cid:3)
Session No 2
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:43 UTC from IEEE Xplore.  Restrictions apply.

CC II RR EE DD(cid:3)
(cid:3)

(cid:20)(cid:27)(cid:87)(cid:75)(cid:3)(cid:44)(cid:81)(cid:87)(cid:72)(cid:85)(cid:81)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:68)(cid:79)(cid:3)(cid:38)(cid:82)(cid:81)(cid:73)(cid:72)(cid:85)(cid:72)(cid:81)(cid:70)(cid:72)(cid:3)(cid:82)(cid:81)(cid:3)(cid:40)(cid:79)(cid:72)(cid:70)(cid:87)(cid:85)(cid:76)(cid:70)(cid:76)(cid:87)(cid:92)(cid:3)(cid:39)(cid:76)(cid:86)(cid:87)(cid:85)(cid:76)(cid:69)(cid:88)(cid:87)(cid:76)(cid:82)(cid:81)(cid:3)

(cid:55)(cid:88)(cid:85)(cid:76)(cid:81)(cid:15)(cid:3)(cid:25)(cid:16)(cid:28)(cid:3)(cid:45)(cid:88)(cid:81)(cid:72)(cid:3)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)

converters  according  to  these  immunity  requirements  will
result in additional costs for each individual device and needs
to be specified explicitly.

MITIGATION MEASURES

In case of the self-commutated converters, a L-C-L – filter is
the  usual  means  in  order  to  reduce  line  conducted  system
perturbations  (Fig.  6).  However,  the  reduction  of  voltage
distortion in the supply system is limited both by economical
and  technical  aspects  in  the  filter  design.  Generally  the
expenditure for the filter must not exceed a fraction of the
converter  costs.  In  addition  the  rating  of  this  passive
component should be small in comparison to the converter
rating  to  minimise  the  influence  on  the  desired  operating
characteristic of the converter.
In the higher frequency range, special constructive measures
have  to  be  carried  out  to  come  as  close  as  possible  to  the
theoretical  filter  action.  As  a  consequence,  standard  filter
components for this frequency range exist only for low power
ratings. Additionally, various special screening measures as
well as special EMC filters may be applied in order to reduce
radiated disturbances.

In  order  to  reduce  commutation  oscillations,  several
possibilities seem to be useful:
• Many,  especially  small  variable  speed  drives  are
connected without or with a small commutation reactor
only. Installation of reactors of a sufficient size reduces
the depth of commutation dips and thus the stimulation
of such oscillations.

• Damped (high-pass) filter circuits increase the damping
of the subsystems especially for higher frequencies and
such reduce the tendency of the subsystem to oscillate.
However, impact on low-frequency harmonics should be
considered carefully, which might be amplified by new
resonance points substantially.

• A common means of avoiding disturbances is also the
use  of  a  "dirty"  and  a  "clean"  busbar.  All  disturbing
equipment  with  generally  higher  immunity  against
disturbances  is  connected  to  one  busbar/subsystem,
sensitive  equipment  is  combined  with  loads  with  low
disturbance  emission.  Where  the  possibility  of  the
creation of such subsystems exists, it is often the least-
cost  alternative  in  order  to  keep  the  system  running
without any disturbances.

EM C - filter

L-C-L - filter

IGBT- converter
IGBT- converter

Dc-link capacitor

Fig. 6: Different filters used for the reduction of disturbances
for self-commutated converters

REFERENCES

[1]  Sonnenschein, M.; Weinhold, M.; Zurowski, R.:, "Shunt-
Connected  Power  Conditioner  for  Improvement  of
Power  Quality  in  Distribution  Networks”,  IEEE  7th
International  Conference  on  Harmonics  &  Quality  of
Power (ICHQP), Las Vegas, 1996

[2]  Akagi, H:, " Control Strategy & Site Selection of a Shunt
Active Filter for Damping of Harmonic Propagation in
Power  Distribution  Systems”,  IEEE  Transactions  on
Power Delivery, vol. 12, no. 1, Jan./Feb. 1997

(cid:38)(cid:44)(cid:53)(cid:40)(cid:39)(cid:21)(cid:19)(cid:19)(cid:24)(cid:3)
(cid:3)
Session No 2(cid:3)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on October 28,2026 at 13:47:43 UTC from IEEE Xplore.  Restrictions apply.

