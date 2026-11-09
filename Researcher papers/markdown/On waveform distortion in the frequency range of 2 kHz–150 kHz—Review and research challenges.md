Electric  Power  Systems  Research  150  (2017)  1–10

Contents  lists  available  at  ScienceDirect

Electric

Power

Systems

Research

j  o  u r  n a  l  h o  m e p a g e :  w w w . e l s e v i e r . c o m / l o c a t e / e p s r

Review

On   waveform   distortion   in   the   frequency   range   of
2   kHz–150   kHz—Review   and   research   challenges

Sarah   K.   Rönnberg a,∗,   Math   H.J.   Bollen a,   Hortensia   Amaris b,   Gary   W.   Chang c,
Irene   Y.H.   Gu d,   Łukasz   H.   Kocewiak e,   Jan   Meyer f,   Magnus   Olofsson g,   Paulo   F.   Ribeiro h,
Jan   Desmet i

a Luleå  University  of  Technology,  931  87  Skellefteå,  Sweden
b University  Carlos  III,  Madrid,  Spain
c National  Chung  Cheng  University,  Taiwan
d Chalmers  University  of  Technology,  412  96  Gothenburg,  Sweden
e DONG  Energy  Wind  Power,  Denmark
f Technische  Universität  Dresden,  01062  Dresden,  Germany
g Swedish  Energy  Institute,  Stockholm,  Sweden
h Federal  University  of  Itajubá,  Brazil
i Gent  University,  Campus  Kortrijk,  Belgium

a

r

t

i

c

l

e

i

n

f

o

a

b

s

t

r

a

c

t

The   frequency   range   between   2  and   150   kHz   has   recently   gained   signiﬁcant   attention,   triggered   by   stan-
dardization   needs   and   increased   emission   in   this   wide   frequency   range.   This   paper   gives   an   overview   of
the  state-of-the-art   concerning   these   so-called   supraharmonics,   and   noticeably   indicates   the  research
challenges   associated   with   waveform   distortion   in   this   frequency   range,   with   emphasis   on   the   fol-
lowing   aspects:   emission;   propagation;   interference;   measurements;   standardization;   modelling   and
simulation.

©  2017   Elsevier   B.V.   All   rights   reserved.

Article  history:
Received  15  August  2016
Received  in  revised  form  10  February  2017
Accepted  30  April  2017
Available  online  9  May   2017

Keywords:
Waveform  distortion
Electromagnetic  compatibility
Power  distribution
Power  quality
Power  system  harmonics
Supraharmonics

Contents

4.

1.
2.
3.

Introduction   .   .  .  .  .   .  .  .  .  .   .   .  .  .  .   .  .  .   .  .  .  .   .  .  .  .   .  .  .   .  .  .  .  .  .   .   .  .  .   .   .   .  .   .   .   .  .   .   .  .  .   .   .  .   .   .  .  .   .   .  .  .  .   .  .  .   .  .  .   .  .   .   .   .  .  .   .  .  .  .  .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .  .  .  .   .  .  .   .  .  .  .   .  .  .  .  .  .   .   .   .  .   .   .   .   .  .  .   .  .  .  .  .  .   .  .  .  .  .   .  .  .  2
Terminology   on  waveform   distortion .   .  .  .   .   .  .  .   .   .  .   .   .   .   .   .  .   .  .   .   .   .  .  .  .  .   .   .   .  .  .   .  .  .  .   .  .  .   .   .  .   .   .  .  .  .  .   .  .  .  .   .   .  .  .   .   .   .  .   .   .  .  .   .   .  .  .   .  .  .  .  .  .  .   .  .  .   .  .  .   .  .  .  .  .   .  .  .   .  .   .  .  .  .   .   .   .   .   .   .   .   .  .  .  .   .  .  .   .  .  .   .  .  .   .  . 2
Emission   .   .   .  .   .   .  .   .  .   .   .  .   .   .  .  .   .   .  .  .   .   .  .   .   .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .  .   .   .  .  .   .   .   .   .  .   .  .  .   .  .   .  .   .  .  .   .  .   .   .  .   .  .  .   .  .  .   .  .   .  .   .   .  .  .   .   .  .  .   .   .  .  .   .   .   .  .   .   .  .  .   .  .  .  .  .  .   .   .  .   .   .   .   .  .  .   .   .  .   .  .  .  .   .  .  .   .  .   .   .   .   2
3.1.
Types   of   emission   .  .  .   .   .  .  .   .   .  .  .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .   .  .  .  .   .  .  .   .   .  .   .  .  .   .   .  .  .   .  .   .  .  .   .  .  .  .   .   .   .  .   .  .   .   .  .  .   .   .  .  .   .   .  .   .   .   .  .   .  .  .   .   .  .  .  .  .   .   .  .  .   .   .   .   .  .   .   .   .  .  .  .  .   .  .  .  .   .   .   .  .   .   .  .   .  .  .   .   2
3.2.
Sources   of  emission   .   .   .  .  .  .   .  .  .   .   .   .  .   .  .  .  .   .  .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .  .  .  .  .   .  .  .   .  .  .  .  .   .  .  .  .   .   .  .  .   .  .  .  .  .   .  .  .   .  .   .   .  .  .   .   .  .  .   .  .  .   .   .   .  .  .   .  .  .  .   .  .  .  .   .   .   .   .   .   .   .  .  .   .  .  .   .   .  .  .  .   .  .   .   .   .   .  .  3
3.3.
Reducing   emission   .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .   .   .  .   .   .   .  .   .   .   .  .  .   .  .  .  .   .  .  .   .  .  .   .   .  .  .   .   .  .   .   .  .  .   .   .  .  .   .  .  .  .   .   .  .  .   .  .   .  .  .   .  .  .  .  .   .  .  .   .  .   .   .  .  .   .   .  .  .   .   .  .   .  .   .   .   .  .  .   .   .   .  .   .   .  .  .  .  .  .   .  .  .  .   .   .  .   .   .   .   .  .  .   .  .  .   .  .  .  .  .   .  4
Propagation .   .  .   .  .   .   .  .  .   .  .  .  .   .   .  .  .  .  .  .   .  .  .   .   .  .  .   .   .  .  .  .   .  .   .  .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .   .   .   .  .  .   .   .  .  .   .   .   .  .   .   .  .  .  .   .  .  .  .  .   .  .  .   .  .  .  .   .   .  .  .   .  .  .  .  .   .  .   .  .  .   .   .   .   .  .   .  .  .   .  .   .  .  .   .  .   .   .   .   .   .   .   .  .  .   .   .  .  .  .  .   .   .  .  .   .   .   .   .  .  .   .  .  .   .   .  .   .   . 4
4.1.
Propagation   between   devices   .  .  .  .  .  .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .  .  .  .  .  .   .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .   .  .  .  .  .   .  .   .  .  .   .   .   .   .  .  .   .   .   .  .   .   .   .   .  .  .  .  .  .  .   .  .   .   .  .   .   .   .   .   .  .   .  .   .  .  .  .  4
4.2.
Resonances .   .   .  .  .   .   .   .  .   .   .  .  .  .   .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .   .  .  .  .   .  .  .  .   .  .   .  .  .  .   .   .  .  .   .  .  .  .   .  .  .  .   .  .   .   .  .  .   .   .  .  .   .  .  .  .   .   .  .  .   .  .   .  .  .   .  .   .   .   .   .   .   .   .  .  .  .  .  .  .  .  .   .   .  .   .  .   .   .   .  .  .  .  .  .  .   .  .  .  .  . 4
4.3.
Secondary   emission .   .   .  .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .   .  .   .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .  .  .  .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .   .  .   .   .  .   .  .   .   .   .  .  .  .   .  .  .   .  .  .  .   .   .   .  .  .  .  .   .  .  .  .  .  .  .  .  .   .   .   .   .   .   .  .   .  .   .  .  .  .  .  .   .   .  .   .   .   .   .  . 5
5.
Interference   .   .   .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .  .  .  .  .   .  .  .   .   .  .  .   .   .  .  .  .   .  .   .  .   .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .   .   .  .  .   .  .  .  .   .  .  .  .   .   .  .  .   .  .   .  .  .   .  .  .   .  .   .   .  .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .   .   .  .  .   .   .   .   .   .   .   .   .  .  .  .   .  .  .   .  .   .   .  .   .   .  .   .  .   .  .  5
6.  Measurements .   .  .  .  .   .  .   .   .  .  .   .  .  .  .   .   .  .  .   .   .  .  .  .  .  .   .  .  .  .   .  .   .   .   .  .   .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .  .  .   .  .   .  .   .  .  .   .  .   .  .  .   .   .  .  .   .  .  .  .   .  .   .   .  .  .   .   .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .   .   .  .  .  .   .  .  .   .  .  .  .  .   .   .  .  .  .   .   .   .   .   .   .   .   .  .  .  .   .  .  .   .  .  .   .  .  .   . 6
6.1.   Measurement   accuracy   .   .  .  .   .   .  .  .  .   .  .  .   .  .  .   .   .  .   .   .   .  .   .   .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .   .  .  .   .   .  .  .   .  .   .   .  .   .  .  .   .   .   .   .  .   .  .   .   .  .  .   .  .   .  .   .   .  .   .  .   .  .   .  .  .   .   .   .  .   .   .   .   .  .  .  .   .   .  .  .  .   .   .   .   .   .   .   .   .  .  .  .   .  .  .  .  .   .  .   .  6
6.2.
Signal   processing   analysis   .  .  .  .  .   .  .  .  .   .   .  .  .   .  .  .  .  .   .  .  .  .  .  .  .   .  .  .  .  .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .   .  .  .  .  .   .   .  .  .  .   .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .  .   .   .   .   .  .  .  .   .   .  .  .  .  .   .   .  .   .   .   .   .  .   .   .  .   .   .   .   .   6

∗

Corresponding  author.
E-mail  address:  sarah.ronnberg@ltu.se  (S.K.  Rönnberg).

http://dx.doi.org/10.1016/j.epsr.2017.04.032
0378-7796/©  2017  Elsevier  B.V.  All  rights  reserved.

2

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

9.

6.3.
Standardized   measurements   .  .   .   .  .  .   .   .  .  .   .  .   .  .   .  .   .   .   .  .  .   .   .  .  .   .   .  .   .   .   .  .   .  .   .  .   .   .  .   .   .  .   .   .  .  .   .   .  .   .  .  .   .  .  .   .  .  .  .   .   .  .  .  .  .   .  .   .  .  .   .  .   .  .  .   .  .   .   .  .   .  .  .   .   .   .   .  .   .   .   .  .  .   .  .   .  .  .  .   .   .   .  .   .   .   .   .  .  .  .  .  .   .  .  .  .   .  6
7.
Standardization   .  .  .   .  .   .   .  .   .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .  .   .   .  .  .  .  .   .  .  .  .   .   .   .  .   .  .   .  .  .   .   .  .   .  .  .   .   .   .   .  .  .   .  .  .   .   .  .  .   .   .  .   .   .  .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .   .  .  .  .   .  .  .  .  .   .   .  .  .   .   .   .   .  .  .   .   .  .  .  .  .  .  .   .  .  .   .  .   .   .   .   .  6
8.  Modelling   and  simulation   .   .  .   .   .  .  .   .   .  .  .  .  .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .   .  .   .   .   .  .   .   .  .  .   .   .  .   .   .  .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .   .  .   .  .  .   .   .   .   .  .   .  .   .   .   .   .  .  .   .  .   .   .  .   .   .   .   .   .   .   .  .   .   .   .  .  .   .  .  .  .  .  .   .   .   .  .   .   .   .   .   .  .   .   .  .  .  .  .  .  .   .  .  6
8.1.
Grid   modelling   .  .  .  .  .   .  .  .   .   .  .  .   .   .  .   .   .   .  .   .  .  .  .  .  .  .   .   .  .   .   .   .  .   .   .   .  .   .   .   .  .  .   .  .   .   .   .  .   .   .  .  .   .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .   .  .  .   .  .   .  .  .   .  .  .   .   .   .  .   .  .  .  .   .  .  .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .  .  .  .  .  .  .   .   .   .   .   .  .   .   .  .  .  .  .  .  .   .  .  7
8.2.
Device   modelling   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .  .  .  .   .  .  .  .   .   .  .  .  .   .  .  .  .  .  .   .   .  .  .  .  .  .  .   .  .  .   .  .   .   .  .  .   .   .  .  .   .  .   .   .  .  .   .  .  .  .   .   .  .  .   .   .   .  .  .   .   .  .  .   .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .   .   .   .   .   .   .   .   .   .  .   .   .  .  .  .   .  .  .   .  .  .   7
Research   challenges   .   .  .  .   .  .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .   .  .   .  .  .  .   .  .  .   .   .   .  .   .   .   .  .   .  .  .   .   .  .   .  .   .   .  .   .   .   .   .   .  .   .   .  .   .   .  .  .   .  .  .   .  .  .  .   .   .  .  .   .  .  .   .   .  .  .   .  .   .  .  .   .  .  .  .   .   .  .  .   .  .  .   .  .  .  .   .  .  .  .   .  .  .  .  .  .   .   .  .   .   .   .   .  .  .   .   .  .   .   .  .  .   .   8
9.1.
Emission   .  .  .  .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .   .  .   .  .  .  .  .  .  .  .   .  .  .   .   .  .  .  .   .  .  .   .  .  .  .   .  .  .  .  .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .   .  .   .   .  .  .  .  .   .   .  .  .   .   .  .  .   .  .   .  .  .   .   .  .  .  .  .  .   .  .  .   .   .  .  .  .   .  .  .  .  .   .   .  .  .   .   .   .   .  .  .   .   .  .  .  .  .  .   .   .  .  .   .   .   .   .   .  .  .   .  8
9.2.
Propagation   .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .  .  .  .  .   .  .   .   .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .   .   .   .  .   .   .  .  .   .  .  .   .  .  .   .  .  .   .  .  .  .  .   .  .   .   .  .   .  .  .   .  .   .  .  .   .  .  .  .   .  .  .  .   .  .  .  .  .   .  .   .   .   .   .   .   .   .  .  .  .   .   .  .   .   .   .   .  .  .  .  .  .  .   .  .   .   .   .   .   .   .   .   .   .   8
9.3.
Interference   .  .   .   .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .  .  .   .  .  .  .  .  .  .  .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .   .   .   .  .   .   .  .   .   .  .  .   .  .  .   .  .  .   .  .  .  .  .   .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .  .  .  .  .  .   .  .   .  .  .  .   .   .  .  .   .   .   .   .  .  .  .   .  .  .  .  .  .   .  .   .   .   .   .  .  .   .  .   .   .  .   .   8
9.4.  Measurements   .  .  .  .   .  .  .  .  .  .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .  .  .  .   .   .  .  .   .  .  .  .   .  .  .  .  .   .   .  .   .   .   .  .  .   .  .  .   .  .  .  .  .  .  .   .  .  .  .   .   .   .  .   .   .   .  .   .   .  .  .   .   .  .  .  .   .   .   .   .   .   .   .  .  .  .  .   .   .  .  .  .   .   .   .  .   .   .   .   .   .   .   .  8
9.5.
Standardization   .  .  .   .  .  .  .   .  .  .  .   .  .  .   .  .  .  .   .   .  .  .   .   .  .  .  .  .  .  .  .  .  .  .  .  .  .   .  .  .  .   .  .  .   .  .  .   .   .   .  .   .   .  .  .   .  .  .  .   .  .   .   .  .   .  .  .   .  .  .   .  .  .  .   .   .  .  .   .   .  .   .   .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .  .  .   .   .  .  .   .   .  .  .  .   .   .   .  .  .   .   .  .  .  .  .   .   .  .  .   .   .   .   .   .   .   .  8
9.6.  Modelling   and   simulation   .  .   .   .  .  .   .   .  .   .   .   .  .   .  .   .  .   .  .   .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .   .  .  .   .   .  .  .   .   .  .   .  .  .  .   .  .  .   .  .  .  .   .  .   .  .  .   .  .   .  .  .   .  .  .  .   .   .  .   .   .   .  .   .  .  .   .   .  .  .   .  .  .  .  .   .  .   .  .  .   .   .   .   .  .   .   .  .  .  .  .  .   .   .   .   .   .   .   .   .   .   .   .  .  .  8
Conclusions   .   .  .   .   .  .  .  .   .   .  .  .   .   .  .  .   .   .  .  .   .  .  .  .  .  .  .   .  .  .   .   .  .  .   .   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   .   .  .  .   .  .  .   .  .  .   .  .   .   .   .  .   .   .  .  .  .  .  .   .  .  .   .  .  .   .   .  .  .  .  .  .  .   .  .  .   .  .  .  .   .  .  .   .  .  .  .  .  .  .  .  .  .   .  .  .   .   .   .  .  .  .   .   .   .  .  .   .   .   .  .  .   .   .   .  .  .  .   .   .   .   .   .   .   .   .  .   8
References   .   .  .  .   .  .   .   .  .  .  .  .   .  .   .   .  .  .   .  .  .  .   .  .  .   .   .   .  .   .   .  .  .   .  .  .   .  .  .   .   .  .  .   .   .   .  .   .   .   .  .   .   .  .  .   .   .  .   .   .   .  .  .   .   .  .   .   .   .   .  .  .   .   .  .  .   .  .   .  .  .  .   .  .  .   .   .   .  .   .  .   .   .  .   .  .  .   .  .  .   .  .  .  .   .   .  .  .   .   .   .   .   .   .  .   .   .  .   .   .   .   .   .   .   .  .  .  .  .  .  .  .   .   .   .   .   .   .  .   .   .   .   .  .   8

10.

1.  Introduction

Distortion  of  voltage  and  current

in  the  frequency  range
between  2  and  150  kHz  is  not  a  new  topic;  engineers  and  manufac-
turers  of  end-user  equipment  have  known  about  these  emissions
and  solved  problems  associated  to  it,  case-by-case  for  decades
[1],  but  the  amount  of  systematic  knowledge  and  the  dissemi-
nation  of  this  have  been  limited.  Recently,  this  frequency  range
has  received  more  attention  by  researchers  [2,3],  and  especially
by  standard-setting  organizations  [4,5].  There  are  considerable  on-
going  activities  within  IEC  (both  SC  77A  and  SC  205A),  CENELEC
and  IEEE  to  develop  standards,  e.g.  compatibility  levels,  limits  and
adequate  test  methods,  covering  this  frequency  range.  Some  stan-
dards  do  exist  already  [4]  but  there  is  no  accepted  framework,  as
there  is  for  lower  frequencies.  The  recent  standard  development
was  mainly  triggered  by  the  use  of  this  frequency  range  for  power-
line  communication  (PLC)  as  part  of  smart  metering  infrastructure.
An  additional  driving  force  for  research  is  the  increasing  amount  of
equipment  with  active  switching  resulting  in  non-negligible  emis-
sion  in  this  range.  Among  others  as  input  to  the  standardization
work,  a  better  understanding  is  needed  of  conducted  phenomena
in  this  frequency  range.

The  aim  of  this  paper  is  to  summarize  the  state-of-the-art  and  to
give  guidance  to  those  new  to  the  subject  of  waveform  distortion
between  2  and  150  kHz  and  to  indicate  research  challenges  and
opportunities  for  future  research.

Section  2  of  this  paper  gives  a  brief  overview  of  the  terminology
on  waveform  distortion.  Sections  3  and  4  give  the  state-of-the-art
on  emission  and  propagation  in  the  frequency  range  2–150  kHz.
Section  5  presents  known  cases  of  interference.  Sections  6–8  sum-
marize  the  measurement,  standardization  and  modelling  issues.
The  important  research  challenges,  extracted  from  the  other  sec-
tions,  are  summarized  in  Section  9,  followed  by  the  conclusions  in
Section  10.

2.  Terminology  on  waveform  distortion

The  frequency  range  up  to  150  kHz  contains  different  classes  of
distortion.  Based  on  the  frequencies  involved,  the  following  classes
are  distinguished:

• Components  at  integer  multiples  of  the  power-system  frequency.
Waveform  is  distorted  but  periodic  with  the  same  period  as  the
power-system  frequency.  These  components  are  referred  to  as
“integer  harmonics”  or  “harmonics”.

• Components  at  non-harmonic  frequencies,  (interharmonics).
• Components  at  frequencies  less  than  the  power-system  fre-
quency  (subharmonics).  These  are  also  a  subclass  of  interharmon-
ics.

• The  component  at  zero  frequency  (dc).
• Components  at  any  frequency  between  2  and  150  kHz,  referred  to
as  “high-frequency  harmonics”  [6,7],  “high-frequency  distortion”
[8]  or  more  recently  “supraharmonics”  [4].

The  term  “low-frequency  emission”  is  used  within  IEEE  EMC
society  to  refer  to  frequencies  below  150  kHz.  Within  IEC  the  term
“low  frequency”  refers  to  frequencies  below  9  kHz.  The  terminology
used  for  any  waveform  distortion  does  not  consider  the  origin  or
impact  of  the  distortion.  There  is  for  example  no  sudden  change
in  physical  character  of  the  distortion  at  2  kHz  that  would  justify
that  as  the  upper  border  for  harmonics.  Also,  for  example,  different
causes  of  interharmonics  exist,  but  regardless  of  the  origin,  any
component  at  a  non-harmonic  frequency  will  be  referred  to  as  an
interharmonic.  The  above  terminology  also  does  not  consider  the
time-varying  nature  of  the  distortion  [9,10,11].

Although  the  term  “supraharmonics”  is  being  used  more  fre-
quently,  the  term  is  still  new  to  the  electric  power  community.
But  the  authors  still  consider  this  as  the  most  suitable  word  avail-
able  at  the  moment.  The  authors  therefore  recommend  using  the
term  “supraharmonics”  to  refer  to  all  quasi-stationary  waveform
distortion  in  the  frequency  range  2–150  kHz.

The  term  “supraharmonics”  as  proposed  here,  only  covers  quasi-
stationary  phenomena  in  the  same  way  as  the  terms  “harmonics”
and  “interharmonics”.  The  frequency  range  between  2  and  150  kHz
also  contains  transient  phenomena,  but  a  further  discussion  of
these  is  beyond  the  scope  of  this  paper.

3.  Emission

3.1.  Types  of  emission

When  considering  the  frequency  domain,  principally  two   types
of  emission  can  be  considered:  narrowband  and  broadband.  In
general,  a  spectrum  that  contains  a  distinct  single  frequency  com-
ponent  is  considered  narrowband  while  a  spectrum  with  several
adjacent  components  is  considered  broadband.  The  bandwidth  of
the  components  is  depending  on  the  time  resolution  of  the  sig-
nal,  window  length,  window  type,  and  grouping  method  (i.e.  a
2  kHz  grouping  might  show  a  narrowband  signal,  where  a  200  Hz
grouping  shows  a  broadband).  To  obtain  a  spectrum,  a  certain  time
window  is  needed;  time  variations  within  this  window  can  blur
the  distinction  between  narrow  and  broadband.  A  time-varying
signal  can  be  narrowband  over  a  short  time  window  but  broad-
band  when  considering  a  longer  period.  It  was  shown  in  Ref.  [12]
that  what  appeared  as  broadband  emission  between  40  and  80  kHz
when  performing  a  DFT  over  a  200  ms   window  was   in  fact  nar-
rowband  emission  at  changing  frequencies  with  a  duration  of  just
a  few  milliseconds.  This  phenomenon  is  due  to  the  variation  in

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

3

switching  frequency  with  hysteresis  control,  as  described  in  Ref.
[13].  The  emission  from  the  two  main  sources  of  emission  above
2  kHz,  residues  from  power–electronic  converters  and  transmitters
of  power-line  communication  can  be  classiﬁed  as  either  narrow  or
broadband  emission.

The  work  presented  in  Refs.  [2,12]  has  shown  that,  when
analysing  in  the  time  domain,  an  additional  type  of  emission  can
be  distinguished:  short-duration  oscillations,  with  a  frequency  of  a
few  kHz,  that  appear  twice  every  cycle  of  the  power-system  fre-
quency.  The  oscillations  are  part  of  the  so-called  “zero-crossing
distortion”.  This  phenomenon
from  the  design  of
power–electronics  converters  [14,15]  and  consists  of  two   different
parts:

is  known

• A  brief  period  around  the  voltage  zero-crossing  during  which  the
current  is  zero,  referred  to  as  “leading-phase  distortion”  in  Ref.
[16].

• An  oscillation  in  current,  with  a  frequency  of  a  few  kHz,  at  the  end
of  this  period,  “ringing  distortion”  [16]  or  “zero-crossing  oscilla-
tion”  [2].

It  is  the  latter  one  that  contributes  to  the  emission  in  the
frequency  range  2–150  kHz.  For  instance  in  Refs.  [16,17]  the  zero-
crossing  oscillations  are  shown  to  be  ampliﬁed  by  the  EMC   ﬁlter.
Looking  at  this  type  of  emission  in  the  frequency  domain,  recur-
rent  oscillations  could  also  be  characterized  as  either  narrow  or
broadband.  They  do  however  differ  in  the  sense  that,  when  seen  in
the  time  domain,  they  appear  as  a  damped  oscillation  and  always
around  the  zero-crossing  of  the  voltage.  Another  reason  for  emis-
sion  in  the  frequency  range  above  2  kHz  is  simply  the  continuation
of  the  emission  below  2  kHz;  typically  odd  harmonics  of  decaying
magnitude  with  increasing  frequency.  Especially  sharp  changes  in
voltage  or  current  magnitude,  as  with  commutation  notches  [18],
give  rise  to  such  emission.  As  with  recurring  oscillations,  this  emis-
sion  would  also  appear  as  either  narrow  or  broadband  emission  in
the  frequency  domain.

3.2.  Sources  of  emission

The  two  main  sources  of  emission  above  2  kHz,  that  have  been
identiﬁed,  are  power–electronic  converters  with  active  or  passive
switching  and  transmitters  of  power-line  communication.  With
some  exceptions,  the  latter  are  of  much  higher  magnitude  than
the  former  ones.  However,  power-line  communication  is  typically
present  during  short  periods  of  time,  whereas  emission  from  active
converters  is  often  present  for  a  substantial  part  of  the  time.  The
arrangement  causing  the  emission  from  among  others  PWM   invert-
ers  is  described  in  detail  in  Ref.  [19].  The  spectrum  of  a  PWM
switching  pattern  is  concentrated  around  the  switching  frequency
and  integer  multiples  of  the  switching  frequency.  As  mentioned  in
Section  3.1,  also  some  passive  converters  emit  in  this  frequency
range,  but  their  main  emission  is  at  lower  frequencies.

One  of  the  reasons  for  the  use  of  active  converters  is  the  ability
to  signiﬁcantly  reduce  the  emission  at  lower  frequencies  and  in  this
way  to  comply  with  emission  limits.  There  are  other  advantages  of
active  converters  however,  so  that  loosening  of  emission  limits  at
lower  frequencies  will  not  in  all  cases  result  in  a  reduction  of  the
emission  at  higher  frequencies.  It  is  however  important  to  consider
this  relation  in  the  discussions  about  emission  limits.

Emission  in  the  frequency  range  between  2  and  150  kHz  is
shown  for  different  devices  by  several  authors.  Emission  around
3  kHz  and  multiples  of  this,  due  to  the  switching  frequency  of  a
1  MVA   PWM   converter  is  shown  in  Ref.  [18].  In  Ref.  [20]  it  is  shown
that  emission  from  a  PWM   boost  converter  can  be  found  in  the
frequency  range  2–9  kHz.  Emission  in  the  range  9–150  kHz  from
different  industrial-size  converters  is  presented  in  Ref.  [20].  Sev-

eral  examples  of  emission  in  the  range  between  2  and  150  kHz  are
also  shown  in  Ref.  [5].

Emission  around  6  kHz,  due  to  oscillations  around  commuta-
tion  notches,  at  a  LV  bus  is  shown  in  Ref.  [18];  the  range  of  such
oscillations  is  up  to  10  kHz.

Frequencies  up  to  several  tens  of  kHz  are  measured  for  LED
street  lamps  and  for  high-pressure  sodium  lamps  with  electronic
ballast  [25].  For  electromagnetic  ballast,  only  decaying  harmonics
up  to  20  kHz  are  visible.  In  the  frequency  range  2–9  kHz,  the  emis-
sion  with  electromagnetic  ballast  is  about  2.5  times  the  emission
with  electronic  ballast.  For  frequencies  above  9  kHz,  the  electronic
ballast  shows  higher  emission.  Current  emission  associated  with,
among  others,  low  power  LED  lamps  are  discussed  in  Ref.  [26],
where  it  is  shown  that  the  emission  seems  to  be  organized  in  bands.
Emission  from  a  number  of  electric  vehicle  chargers  is  presented
in  Ref.  [27]:  the  emission  was  mainly  concentrated  in  the  range  up
to  about  15  kHz,  but  one  of  the  chargers  showed  an  emission  peak
somewhat  above  30  kHz.  Emission  at  frequencies  27  kHz,  37  kHz
and  100  kHz  is  presented  in  Ref.  [28]  and  at  21  kHz  in  Ref.  [29].
Analyses  of  the  emission  from  power  converters  connected  directly
to  the  power  grid  in  an  experimental  microgrid  composed  by  PLC
equipment  and  several  PV  inverters  with  a  switching  frequency  of
16  kHz,  appearing  in  the  voltage  when  the  PV  inverter  is  operating,
are  presented  in  Ref.  [30].

Emission  at  4  kHz  and  16  kHz  from  PV  inverters  is  shown  in  Ref.
[31].  Emission  in  public  low-voltage  grids,  due  to  PV  inverters,  is
shown  in  Ref.  [32].  The  main  emission  is  shown  to  be  in  the  range
16–19  kHz,  with  16  kHz  the  most  common  one.  Voltage  distortion
up  to  about  1  V  was  measured;  levels  were  clearly  higher  at  day-
time,  but  there  was   no  correlation  with  the  amount  of  installed
capacity.  Voltage  distortion  was  lower  in  grids  without  PV  and
there  was  a  wider  range  in  dominant  frequencies;  6.2–28.8  kHz.
It  is  shown,  experimentally,  that  there  is  emission  from  PV  invert-
ers  in  the  range  between  16  kHz  and  17  kHz  in  [33].  Reference  [34]
shows  an  increase  in  voltage  distortion  at  16  kHz,  20  kHz  and  32  kHz
due  to  PV.  Similar  results  are  presented  in  Ref.  [35]  where  measure-
ments  from  single  phase  PV  inverters  are  shown  to  cause  distortion
around  16  kHz.  In  Ref.  [35]  measurements  are  also  presented  from
larger  solar  PV  plants,  showing  the  typical  spectra  associated  with
an  inverter  using  PWM   [36]  with  components  around  4  kHz.  Emis-
sion  from  an  850-kW  solar  park  is  shown  to  have  peaks  around
3  kHz,  6  kHz  and  9  kHz  [37].  Measurements  in  a  1-MW  solar  park
with  a  mixture  of  small  and  large  inverters  are  shown  in  Ref.  [38];
emission  occurs  at  3  kHz,  6  kHz  and  9  kHz  due  to  large  inverters
and  at  10  kHz,  16  kHz  and  25  kHz  due  to  small  inverters.  In  Ref.
[39],  PV  inverters  employing  PWM   injecting  current  in  the  range
of  2–5  kHz  are  discussed.  A  case  study  presented  in  Ref.  [40]  shows
the  switching  frequency  from  a  grid  interface  inverter  of  a  variable
speed  wind  turbine  located  at  3.15  kHz.

According  to  Ref.  [41]  the  peak  voltage  can  be  up  to  50  V  in  a  100-
V  low-voltage  network  due  to  resonance  together  with  emission.
High  levels  of  voltage  distortion,  “up  to  several  volts”,  in  the  kHz
range  due  to  a  washing  machine  and  a  cell  tower  are  shown  in  Ref.
[42].

Emission  from  a  number  of  low-voltage  devices  (i.e.  com-
pact  ﬂuorescent  lamp;  CRT  television;  vacuum  cleaner  with  brush
motor)  is  presented  in  Ref.  [43]  as  noise  experienced  by  power-
line  communication.  Similar  measurements,  but  performed  in  the
early  80  s  are  shown  in  Ref.  [1];  the  main  sources  according  to  that
study  where  universal  motors  and  the  line  frequency  of  television
receivers.

It  is  shown  in  Ref.  [21]  that  slot  harmonics  from  squirrel-cage
induction  machines  can  appear  between  1  and  1.7  kHz.  In  Ref.  [22]
these  are  referred  to  as  “tooth  ripples”.  The  slots  in  synchronous
and  induction  machines  were  already  mentioned  as  a  source  of
harmonics  in  Ref.  [23]  and  later  in  Ref.  [24].  Note  that  the  presence

4

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

of  slots  also  causes  emission  at  integer  multiples  of  the  frequency
with  which  the  air-gap  ﬁeld  passes  the  slots,  which  will  be  in  the
range  above  2  kHz.  It  is  shown  by  simulations  in  Ref.  [21]  that  the
magnitude  at  the  second  and  third  harmonic  of  the  “slot  frequency”
is  close  to  the  magnitude  at  the  slot  frequency.

3.3.  Reducing  emission

Emission  can  be  reduced  in  a  number  of  ways,  where  the  prin-

cipal  distinction  is  between  the  following  two  approaches:

• Changing  the  switching  pattern  and  control  algorithms  so  that
less  emission  is  produced  during  the  power–electronics  switch-
ing.

• Adding  a  passive  ﬁlter  between  the  actual  converter  and  the  grid

[44,45,46]  .

One  way  of  utilizing  the  ﬁrst  approach  would  be  the  use  of
multi-level  converters  that  offer  a  range  of  possibilities  for  reduc-
ing  emission  around  the  switching  frequency  and  its  harmonics
[24,31].  The  above-mentioned  passive  ﬁlter  is  known  as  “EMC  ﬁl-
ter”  or  “EMI  ﬁlter”  and  is  a  common  part  of  most  small  devices.
Its  aim  is  mostly  to  reduce  emission  in  the  frequency  range  above
150  kHz,  but  it  can  also  be  used  to  reduce  emission  in  the  range
2–150  kHz.  The  latter  would  however  require  a  redesign  of  the
ﬁlter,  avoiding  resonances  below  150  kHz.

4.  Propagation

Using  the  superposition  principle  for  linear  systems,  the  voltage
(at  frequency  f)  at  a  bus  r  due  to  sources  at  different  busses,  is  found
from  the  following  expression:

N(cid:2)

Ur (f ) =

Zrs (f ) ·

Is (f )

s=1

Zrs (f ) is  the  transfer  impedance  from  bus  s  to  bus  r.  Non-
where
linear  phenomena  are  not  included  in  this  expression,  but  there  is
simply  insufﬁcient  knowledge  available  on  how  these  will  impact
the  propagation  of  distortion  in  the  range  between  2  and  150  kHz.
All  parameters  in  the  above  expression  are  complex  numbers
and  are  varying  with  time.  The  presence  of  an  additional  device
and  variable  load  condition  further  impacts  the  transfer  impedance
between  neighbouring  devices.  It  is  therefore  not  possible  to  sim-
ply  add  the  emission  from  individual  devices  and  aggregation  rules
as  in  IEC  61000-3-6  do  not  hold  anymore,  as  was  shown  for  exam-
ple  in  Refs.  [47,48,52].  Next  to  classical  phenomena,  like  diversity
between  the  emission  spectra  from  individual  devices,  diversity  in
time  of  use  of  equipment,  and  cancellation  of  emission  in  the  com-
plex  plane,  also  the  time  variation  of  the  transfer  impedance  should
be  considered.

Propagation  is  studied  in  this  section  from  three  different
angles:  propagation  from  one  device  to  one  or  more  neighbour-
ing  devices  and/or  to  the  rest  of  the  grid;  resonances  either  in  the
installation  or  in  the  rest  of  the  grid  that  result  in  an  ampliﬁcation
of  the  transfer;  and  the  receiving  by  a  device  of  the  emission  prop-
agated  from  elsewhere.  The  source  of  the  emission,  whether  it  is  a
device  like  a  converter  or  a  transmitter  of  power  line  communica-
tion,  is  of  no  relevance  with  regard  to  propagation.  What  matters
are  the  transfer  impedances  between  the  nodes  in  the  grid  at  the
instance  when  the  emission  is  injected  into  the  system.

4.1.  Propagation  between  devices

Propagation  between  devices  in  a  low-voltage  installation  has
been  studied  in  Ref.  [47].  It  was  shown  that  the  current  at  the  supply
terminals  of  the  installation  was  much  smaller  than  at  the  device
terminals.  By  measuring  with  all  connected  devices  it  was  found
that  the  current  ﬂowed  mainly  between  devices  and  not  towards
the  grid  (see  Section  4.3).

The  currents  in  a  low-voltage  installation  with  1–48  ﬂuorescent
lamps  with  electronic  ballast  were  measured  in  Ref.  [48].  It  was
shown  that  the  emission  at  tens  of  kHz,  from  the  complete  instal-
lation,  reduced  with  increasing  number  of  lamps.  This  behaviour
has  been  explained  in  Ref.  [52]  using  a  rather  simple  model:  a
constant-current  source  in  parallel  with  a  capacitor  representing
the  EMC   ﬁlter.  It  is  this  capacitor  that  creates  a  low-impedance
path  causing  the  current  to  ﬂow  mainly  between  devices.  This  low-
impedance  path  is  also  responsible  for  some  of  the  interference
between  devices  and  power-line  communication  [3,53].  Measure-
ments  in  a  low-voltage  distribution  network  [32]  showed  between
1  and  2  V  distortion  at  8  kHz  at  300  and  400  m  from  the  distribution
transformer;  however,  the  voltage  at  that  frequency  was  close  to
zero  near  the  distribution  transformer.  The  propagation  of  emis-
sion  originating  from  distributed  generation  is  also  discussed  in
Refs.  [30,39].

Ref.  [48]  shows  a  different  behaviour  for  the  zero-crossing  oscil-
lations  at  a  few  kHz:  their  amplitude  increases  with  increasing
number  of  devices  and  the  resonant  frequency  gets  somewhat
smaller.  No  quantitative  explanation  has  been  given  yet  for  this
phenomenon.

4.2.  Resonances

Resonances  play  an  important  part  in  the  propagation  of  emis-
sion  in  the  frequency  range  between  2  and  150  kHz.  Emission
close  to  the  resonant  frequency  will  be  ampliﬁed  when  insufﬁcient
damping  is  present.  Simulations  for  a  number  of  wind  parks  [54]
show  that  the  emission  from  individual  turbines  around  the  switch-
ing  frequency  can  be  ampliﬁed  at  the  point  of  connection.  Those
studies,  as  well  as  Ref.  [55]  show  that  the  emission  of  the  park  as  a
whole  becomes  negligible  above  the  main  resonant  frequency.

An  extreme  example  of  ampliﬁcation  is  shown  in  Ref.  [56]  where
the  voltage  at  a  30  kV  cable  terminal  contains  an  oscillation  around
2  kHz  and  a  magnitude  between  30  and  100%  of  the  fundamental
voltage.  The  resonance  in  that  case  was  due  to  underground  cables
in  an  industrial  installation.  In  Ref.  [57]  measurements  and  simu-
lations  are  shown  as  a  resonance  around  6.7  kHz  between  a  500-m
cable  and  the  power  transformer.

In  low-voltage  installations,  where  the  propagation  is  mainly
between  devices,  the  capacitance  and  inductance  of  those  devices
is  also  expected  to  play  an  important  role.  Connecting  or  discon-
necting  a  single  device  can  change  the  resonant  frequency  and
therewith  the  propagation  of  the  emission.

Simulations  presented  in  Ref.  [58]  show  that  the  length  of  the
cable  between  an  emitting  device  and  the  distribution  transformer
can  have  a  strong  impact  on  the  35-kHz  voltage  on  the  LV  side  of
the  transformer.  For  a  cable  length  of  800  m  the  voltage  is  ampliﬁed
by  a  factor  ﬁve.  It  can  thus  not  be  generally  concluded  that  distur-
bance  levels  get  smaller  when  moving  away  from  the  source,  as  was
suggested  in  Ref.  [32].  It  was  further  shown  in  Ref.  [58]  that  there
are  no  simple  relations  between  grid  parameters  and  resonant  fre-
quencies.  Resonances  in  the  frequency  range  2–9  kHz  are  studied
in  Ref.  [41],  especially  with  reference  to  the  size  of  the  capacitor
representing  neighbouring  equipment.

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

5

I

+

U

-

Z2

+

E2

-

J1

Z1

Fig.  1.  Primary  and  secondary  emission.

4.3.  Secondary  emission

The  terms  “primary  emission”  and  “secondary  emission”  were
introduced  in  Ref.  [52]  and  are  further  explained  in  Ref.  [59].  With
reference  to  Fig.  1,  the  primary  emission  (both  voltage  and  current)
is  driven  by  J1 and  the  secondary  emission  by  E2;  the  current  I  at  the
device  terminals  is  the  sum  of  primary  emission  I1 and  secondary
emission  I2:

I1 =

I2 =

−

·

J1

Z1
Z1 +

Z2
E2
Z1 +

Z2

I

=

I1 +

I2 =

E2

Z1 ·

J1 −
Z2

Z1 +

(1)

(2)

(3)

Similar  expressions  can  be  obtained  for  the  voltage.  From  the
above  expressions  it  follows  that  both  primary  and  secondary  emis-
sion  are  dependent  on  the  source  (Z1)  and  device  impedances  (Z2).
The  model  in  Fig.  1  is  only  aimed  at  illustrating  the  concept,  not
as  a  tool  for  detailed  studies.  Especially  close  to  device  terminals,
non-linear  phenomena  like  cross-over  modulation  between  differ-
ent  frequencies  will  play  an  important  role.  A  third  phenomenon,
referred  to  as  “interaction”  has  recently  been  proposed  by  an  inter-
national  working  group  to  cover  some  of  the  non-linear  phenomena
[59].

An  important  conclusion  already  from  this  simpliﬁed  model  is
that  emission  measurement  may   not  be  reproducible  at  another
location  as  both  E2 and  Z2 are  likely  to  be  different.  Such  obser-
vation  has  been  conﬁrmed  by  measurements  presented  in  several
publications  [28,31,58,60,61].  It  should  be  noted  that  the  presence
of  a  distorted  voltage  at  the  terminals  of  the  device  (U  in  Fig.  1)
might  impact  the  internal  emission  J1;  this  will  also  result  in  dif-
ferences  in  emission  at  different  locations.  Distinguishing  between
these  impacts  remains  a  major  challenge.  In  one  of  the  cases  pre-
sented  in  Ref.  [28]  not  only  the  magnitude  of  the  emission  changes,
also  the  main  emission  frequency  changes  (from  37  to  35  kHz).
Measurements  presented  in  Ref.  [61]  show  that  the  primary  emis-
sion  from  a  PV  inverter  is  strongly  dependent  on  the  presence  of
other  devices  in  the  same  low-voltage  installation.

A  further  consequence  of  secondary  emission  is  that  it  is  often
difﬁcult  to  interpret  measurements  of  emission  like  those  pre-
sented  in  Section  3.2.

The  terms  “primary  emission”  and  “secondary  emission”  are
new,  but  the  underlying  concepts  have  been  around  for  a  long  time.
A  range  of  methods  has  been  proposed  to  distinguish  between  dif-
ferent  harmonic  contributions,  e.g.  at  the  point  of  connection  of  an
industrial  installation  [49,50,51].

With  reference  to  Fig.  1,  only  U  and  I  can  be  obtained  from
measurements.  Without  any  additional  assumptions  it  will  not  be
possible  to  obtain  values  of  the  two  sources  (J1 and  E2)  and  of
the  two  impedances  (Z1 and  Z2).  Note  that  for  the  general  case,
none  of  the  values  can  be  assumed  constant  in  time.  The  differ-
ent  approaches  proposed  in  the  literature  to  distinguish  between
primary  and  secondary  emission,  differ  through  the  assumptions

made.  All  earlier  work  on  this  subject  has  been  directed  towards
lower-order  harmonics,  typically  the  5th  and  7th  order.  It  is  not
clear  to  which  extent  the  assumptions  made  are  valid  for  the  fre-
quency  range  above  2  kHz.

5.  Interference

Several  examples  are  shown  in  the  literature  of  interference  due
to  voltage  and  current  distortion  in  the  range  of  2–150  kHz.  The
reported  cases  of  interference  can  be  grouped  into  four  categories
with  Category  1  the  most-commonly  reported  one:

• A  device  is  occasionally  not  operating  as  intended  or  with  reduced

functionality.

• Failed  operation  or  damage  of  a  device.
• Interference  with  or  due  to  power  line  communication.
• Audible  noise  from  a  device  or  installation.

The  following  reported  cases  can  be  grouped  into  Category  1  (a
device  is  occasionally  not  functioning  as  intended  or  with  reduced
functionality):

• Reduced  quality  of  the  output  of  a  copy  machine  due  to  frequen-

cies  in  the  lower  kHz  range  [18].

• Control  problems  with  equipment  using  a  77.5  kHz  radio  signal
for  internal  clocks.  Radiated  emission  at  a  multiple  of  the  3  kHz
switching  frequency  of  a  drive  interfered  with  the  clock  signal
[18].

• The  possible  interference  between  a  VSC  HVDC  converter  and  the

77.5  kHz  radio  signal  [63].

• Cases  of  interference  with  light  dimmers,  medical  equipment,

electricity  meters,  and  earth  leakage  current  breakers  [5].

• An  8-kHz  voltage  of  about  5  V,  due  to  a  CNC  mill,  resulted  in  a
range  of  complaints  [32]:  malfunction  of  a  fully  automated  coffee
maker;  a  hair  dryer  randomly  turning  on  an  off;  malfunctions  of
the  control  of  the  CNC  drive  itself.

• A  case  is  described  in  Ref.  [62]  where  the  emission  from  a  large
rectiﬁer  causes  mal-functioning  of  the  dimming  with  LED  lamps
in  nearby  ofﬁces.  The  mal-functioning  was  reproduced  in  a  lab-
oratory  environment  and  was  shown  to  be  due  to  oscillations  in
the  kHz  range.

• Unwanted  tripping  of  earth  leakage  current  breakers  is  the  main

impact  of  emission  in  the  range  2–9  kHz  in  Japan  [41].

• Voltage  distortion  in  the  range  2–150  kHz  was  shown  to  effect

light  output  from  LED  lamps  in  Ref.  [64]

The  following  reported  cases  can  be  grouped  into  Category  2

(failed  operation  or  damage  of  a  device):

• Regular  failure  of  small  drives  due  to  about  1%  oscillations  in

voltage  in  the  kHz  range  [18].

• Violent  failure  (“black  smoke”)  of  a  precision  measurement

instrument  [18].

• Failure  of  varistors  due  to  repetitive  activation  by  recurrent  oscil-

lations  in  voltage  [18].

The  following  reported  cases  can  be  grouped  into  Category  3

(interference  with  or  due  to  power  line  communication):

• Several  cases  of  interference  were  presented  in  Ref.  [62]  including
mal-functioning  of  touch-dimmer  lamps  and  problems  with  data
transmission  from  smart  meters.

• According  to  Ref.  [53],  the  major  causes  of  PLC  issues  are  the  noise
level  along  the  lines  (generated  by  loads  connected  to  the  grid)
and  low  impedance  of  speciﬁc  loads  or  line  attenuation.

6

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

• Several  examples  of  interference  are  shown  in  Ref.  [5],  where  the

emphasis  is  on  interference  to  power-line  communication.

The  following  reported  cases  can  be  grouped  into  Category  4

(audible  noise  from  a  device  or  installation):

• Telephone  interference  used  to  be  an  important  consequence
of  high  harmonic  currents,  especially  in  the  frequency  range
2–4  kHz,  where  the  human  hearing  is  most  sensitive  [22].

• Voltage  distortion  around  12  kHz  was  shown  to  cause  mechanical

oscillations  and  audible  noise  [18].

• Audible  noise  coming  from  a  television  is  mentioned  in  Ref.  [32].
• Audible  noise  from  an  inverter-driven  motor,  in  the  kHz  range
is  reported  among  others  in  Refs.  [65,66].  The  role  of  mechanical
resonances  is  shown  to  be  very  important  with  the  generation  of
audible  noise.  With  these  examples,  the  motors  are  exposed  to
waveforms  with  high  levels  of  distortion.

Many  more  examples  appear  in  the  informal  literature  and  in  the
form  of  personal  communication.  Especially  for  the  latter  examples,
it  is  difﬁcult  to  verify  if  the  interference  is  really  due  to  disturbances
in  the  frequency  range.

6.  Measurements

6.1.  Measurement  accuracy

Obtaining  sufﬁcient  measurement  accuracy  for  voltages  and
currents  in  the  frequency  range  of  2–150  kHz  is  not  trivial  and
has  to  be  considered  for  the  whole  measurement  chain.  It  requires
transducers  that  have  high  accuracy  for  both  amplitude  and  phase
angle  over  a  wide  frequency  range.  In  addition  to  appropriate  anti-
aliasing  ﬁlters  the  measurement  signals  (voltage  or  current)  need
to  be  high-pass  ﬁltered  in  order  to  avoid  leakage  effects.  The  high-
pass  ﬁlter  can  be  digital  for  A/D  resolution  of  16  Bit  and  better  [68],
otherwise  an  analogue  ﬁlter  is  needed.

A  detailed  description  of  measurement  techniques  for  wave-
form  distortion  in  the  frequency  range  of  2–150  kHz  is  given  in
Ref.  [69].  Challenges  for  measuring  and  analysing  such  distortion
are  also  discussed  in  Refs.  [71,72].  In  Refs.  [68]  two   measurement
methods  are  discussed  regarding  the  necessity  of  ﬁlters,  chosen
bandwidth,  impact  of  band  boundaries  and  aggregation  in  time.

6.2.  Signal  processing  analysis

Measurements  show  that  signals  in  the  frequency  range  from  2
to  150  kHz  often  change  in  amplitude  and  frequency  on  timescales
of  milliseconds  [2].  A  similar  phenomenon  is  shown  in  Ref.  [73]  but
for  a  much  higher  frequency  band.  Therefore  both  time-domain
and  frequency-domain  should  be  considered  for  signal  analysis.  A
joint  time–frequency  domain  analysis  like  the  short-time  Fourier-
transform  (STFT)  or  sliding-window  ESPRIT  [74]  is  an  appropriate
tool  to  analyse  these  changes.  With  the  STFT  a  signal  is  divided  into
smaller  windows  (with  or  without  overlap)  for  every  one  of  which
a  spectrum  is  obtained.  These  time-dependent  spectra  are  com-
bined  to  create  an  image  of  the  changes  in  the  spectrum  over  time
(the  spectrogram)  [69].  The  STFT  is  equivalent  to  applying  a  set  of
band-pass  ﬁlters  [75].  A  broadband  signal  is  decomposed  into  a  set
of  time-varying  narrowband  components  at  different  frequencies.
This  gives  a  lot  of  additional  information  compared  to  the  spectrum
obtained  over  a  longer  time  window.

For  the  recurrent  oscillations,  neither  the  conventional  spec-
trum,  nor  the  spectrogram  is  an  appropriate  tool.  A  time-domain
analysis  is  most  convenient  to  quantify  and  study  recurrent  oscilla-
tions,  like  in  Ref.  [69],  where  ESPRIT  is  used  to  estimate  frequency

and  amplitude  of  recurrent  oscillations.  In  Ref.  [70]  a  method  for
time–frequency  analysis  is  proposed  that  is  shown  to  give  detailed
information  in  term  of  frequency,  magnitude  as  well  as  time-
variability.

6.3.  Standardized  measurements

IEC  61000-4-19  deﬁnes  immunity  requirements  and  test  meth-
ods  for  equipment  to  disturbances  in  the  range  of  2–150  kHz.  A
measurement  method  for  the  range  of  2–9  kHz  is  given  in  IEC
61000-4-7.  Measurements  are  also  deﬁned  in  the  CISPR  standards
where  typically  heterodyne  frequency-domain  methods  are  used.
IEC  61000-4-30  includes  informative  annex  C  describing  measure-
ment  methods  for  2–9  kHz  as  well  as  9–150  kHz.  CENELEC  study
report  II  devotes  one  section  on  measurements  [5].

7.  Standardization

A  key  term  in  the  IEC  standardization  on  electromagnetic  com-
patibility,  where  the  frequency  range  of  2–150  kHz  is  part  of,  is
the  “compatibility  level”:  “The  speciﬁed  electromagnetic  distur-
bance  level  used  as  a  reference  level  for  co-ordination  in  the  setting
of  emission  and  immunity  limits”  [76].  Compatibility  levels  are
important  in  order  to  deﬁne  compatibility  margins  for  emission
and  immunity  as  a  basis  to  achieve  electromagnetic  compatibility
with  a  high  probability.

However,  after  intense  discussions  in  the  relevant  study  com-
mittees  in  recent  years,  consensus  has  been  reached  only  in  the
frequency  range  of  2–30  kHz  [77].  Until  now,  a  compromise  for
non-intentional  emissions  has  not  been  reached  for  the  range
30–150  kHz  [78,79].  There  are  two  different  proposals  of  compati-
bility  levels  for  non-intentional  emissions  between  30  and  150  kHz;
one  (“proposed  compatibility  level”  in  Fig.  2)  being  supported  by
experts  related  to  equipment  producing  industry  excluding  indus-
try  providing  PLC  and  another  (“Compatibility  level  option  B”)  being
supported  by  experts  related  to  electricity  distribution,  plus  PLC
industry  experts.

Fig.  2  further  shows  the  voltage  characteristics  for  “mains  sig-
nalling”  (2–95  kHz)  according  to  EN  50160  as  well  as  the  emission
limits  for  communication  in  the  communication  band  and  in  non-
communication  bands  according  to  EN  50065.  The  limits  for  the
communication  band  are  the  same  as  in  IEC  61000-3-8.

Following  a  recent  SC  77A  plenary  meeting  [80]  it  was   decided
to  modify  maintenance  work  for  standard  IEC  61000-2-2  into  a  new
amendment  instead  of  a  standard  revision.  It  was  also  decided  to
focus  on  frequency  range  of  2–30  kHz,  while  keeping  30–150  kHz
under  consideration.  As  consensus  has  been  reached  for  compati-
bility  levels  in  this  frequency  range,  the  present  IEC  target  now  is
completion  of  standard  maintenance  work.  Finally,  maintenance
work  item  for  IEC  61000-2-12  (medium  voltage)  has  been  can-
celled  due  to  lack  of  agreement  on  compatibility  levels  on  the  whole
frequency  range  in  IEC  61000-2-2  (low  voltage).  Input  to  the  stan-
dardization  committees  from  an  independent  research  community
is  needed  to  ﬁnalize  the  work.

8.  Modelling  and  simulation

The  modelling  efforts  in  the  frequency  range  of  2–150  kHz  have
to  be  considered  for  two   distinctly  different  aspects;  the  grid  and
the  components/devices/installation  connected  to  the  grid.  Grid
modelling  for  this  frequency  range  (Section  8.1)  is  a  well-developed
area,  especially  for  overhead  lines  and  for  medium-voltage  and
high-voltage  cables,  although  knowledge  on  low-voltage  installa-
tions  remains  limited.  Device  modelling  (Section  8.2)  still  requires
a  lot  of  further  studies.

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

7

dBµV

150

140

130

120

110

100

90

80

70

60

50

2 kH
2E+0

z

EN 50
160
Proposed
EN 50

 compa

tibility
nd not in

vel
 le
)
 use

065 (ba

EN
 50065
Compatibili

 (c
ty level

ommunicati
tion

 op

on ban
 B

d)

Fig.  2.  Compatibility  levels  proposed  by  two   different  IEC  expert  groups  [78]  and  other  relevant  limits  [4].

20 kH
2E
+1

z

150 kH

z

8.1.  Grid  modelling

The  modelling  of  the  grid  for  this  frequency  range  has  strong
similarities  to  the  modelling  for  transient  overvoltage  as  part  of
insulation  coordination  [81].  Looking  into  studies  on  transient  over-
voltages  there  are  several  papers  on  high  frequency  behaviour  of
transformers  [82–85].  The  drawback  with  all  these  models  is  that
measurements  are  needed  on  each  transformer  to  obtain  the  model
parameters.  General  guidelines  on  transformer  modelling  are  given
in  Refs.  [86,87],  where  the  different  capacitive  couplings  are  shown
to  be  important.  The  models  of  the  inductive  part  of  the  trans-
former,  including  the  core  losses,  may   lose  validity  at  a  frequency  of
several  kHz.  It  is  however  also  at  these  frequencies  where  the  capac-
itive  coupling  will  become  dominant,  so  that  the  model  inaccuracy
becomes  less  relevant.

Models  of  cables  and  overhead  lines  can  be  found  in  the  lit-
erature  on  power  line  communication  e.g.  Ref.  [88]  as  well  as  in
the  literature  on  switching  transients  and  EMTP  modelling  [86,89].
The  basic  expressions  for  overhead-line  modelling  were  derived
already  around  1925,  almost  simultaneously  by  Refs.  [90,91],  but
the  approximations  presented  in  Ref.  [90]  enabled  them  to  be
implemented  in  computer  calculations,  like  the  line-constants  rou-
tine  that  formed  the  input  for  the  overhead-line  model  used  in  the
EMTP  program  [92].  It  was  shown  in  Ref.  [93]  that  the  expressions
used  were  mathematically  incomplete  but  of  sufﬁcient  accuracy
up  to  several  hundreds  of  kHz.  Simulation  results  were  veriﬁed  by
measurements  in  Refs.  [94,95].  A  modelling  study  of  MV  lines  with
speciﬁc  reference  to  harmonics  in  the  frequency  range  2–150  kHz
is  presented  in  Ref.  [96].

The  modelling  effort  for  overhead  lines,  cables  and  transformers
has  been  directed  mainly  towards  the  transmission  system  instead
of  the  distribution  system.  Models  for  overhead  lines  and  cables
remain  valid  for  lower  voltage  levels,  but  it  will  not  be  possible
to  perform  measurements  on  each  distribution  transformer.  This
is  where  a  modelling  effort  is  still  needed.  In  Ref.  [97]  the  model
of  a  transformer  for  power-line  communication  is  presented.  It
shows  the  ﬁrst  resonances  to  be  around  300  kHz.  In  Ref.  [98]  a  mod-
elling  approach  based  on  the  transfer  matrix  of  the  transformer
is  presented.  Measurements  of  the  transfer  for  a  100  kVA,  MV/LV
transformer  are  presented  in  Ref.  [99]:  the  transfer  from  LV  to  MV
is  ampliﬁed  by  a  factor  of  10  at  the  resonance  frequency  around
4  kHz;  the  transfer  from  MV  to  LV  remains  about  the  same  as  at  the
power-system  frequency  up  to  at  least  80  kHz.

Especially  for  an  LV  installation  one  has  to  consider  all  the  com-
ponents  within  the  installation,  connected  equipment  as  well  as
wires.  Wiring  inside  a  building  is  neither  symmetrical  and  currents
not  balanced  nor  as  structured  as  overhead  lines  and  cables.

In  summary,  for  the  modelling  of  lines,  cables  and  transform-
ers,  the  knowledge  is  available,  although  typical  parameters  of
the  capacitance  for  distribution  transformers  may  not  be  generally
available.

8.2.  Device  modelling

Devices  connected  to  the  grid  are  the  most  challenging  part  of
the  modelling  effort  in  this  frequency  range.  At  the  point  of  con-
nection  the  characteristic  of  a  device  (if  the  behaviour  mimics  that
of  a  current  or  voltage  source)  signiﬁcantly  depends  on  the  ratio
between  source  impedance  of  the  device  and  network  impedance
at  the  considered  frequency.  It  is  even  possible  that  one  and  the
same  device  behaves  at  one  point  more  like  a  voltage  source  and
at  another  point  more  like  a  current  source  (or  source  with  inner
impedance).  Detailed  models  of  devices  like  power  electronic  con-
verters  can  be  found  in  the  literature,  with  Refs.  [100,101,102]  being
some  recent  books  on  the  studied  subject.  The  detail  needed  to
model  the  behaviour  of  a  device  within  this  frequency  range  with
sufﬁcient  accuracy  is  however  still  not  understood.  To  model  and
simulate  an  installation  correctly  might  mean  one  has  to  include  all
components  in  the  devices  connected  within  the  installation  and
even  if  that  information  is  available  it  will  become  computationally
intensive  already  for  one  device.  In  Ref.  [104]  a  comparison  is  made
between  a  detailed  Simulink  model  and  the  measured  emission.  It
is  shown  that  the  emission  can  be  very  well  reproduced  for  lower
frequencies,  but  not  for  frequencies  above  2  kHz.  Devices  can  be
modelled  as  an  emitting  source  but  the  model  also  has  to  consider
the  fact  that  every  device  can  in  some  way   impact  the  propaga-
tion  of  the  emission  from  other  sources  (see  Section  4.3).  According
to  Ref.  [58],  as  cited  in  Ref.  [67],  a  constant  DC  voltage  behind  a
voltage-source  converter  is  sufﬁcient  as  a  model  of  the  emitting
source.  It  is  shown  in  Ref.  [41]  that  a  simple  model  of  a  vacuum
(cid:2)H  inductance
cleaner  (8  A  of  current  source  in  parallel  with  145
(cid:2)F  for  the  ﬁlter  capacitor)  can  reproduce  the  measure-
and  0.495
ments  in  the  range  2–9  kHz.  A  battery  charger  for  an  electric  car  is
modelled  in  Ref.  [29];  a  detailed  time-domain  model  is  used  for  the
charger  including  the  EMI   ﬁlter,  the  PWM   pattern  and  its  control;
the  grid  is  modelled  by  its  series  impedance.  This  model  was  able

8

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

to  reproduce  resonances  for  a  certain  cable  length,  including  the
3.4  kHz  resonant  frequency  of  the  EMI   ﬁlter.

More  detailed  modelling  of  the  power–electronics  interface  of
lighting  sources  is  presented  among  others  in  Ref.  [105].  A  com-
plete  model  of  a  device  also  has  to  cover  the  complexity  of  the
interaction  between  devices.  There  is  a  linear  part  concerning  the
behaviour  of  a  device  as  an  impedance  (seen  by  other  devices).
There  is  also  a  non-linear  part:  the  voltage  distortion  caused  by
emission  from  other  grid  connected  devices,  changes  the  emission
of  the  device.  This  can  be  partly  addressed  by  “harmonic  ﬁnger-
printing”  as  introduced  for  (low-frequency)  harmonics  in  Ref.  [106]
but  that  would  still  not  cover  the  interactions  between  signals  at
different  frequencies.

Models  do  exist  for  a  range  of  other  components,  like  inverters
for  PV  panels  or  wind  turbines,  adjustable-speed  drives,  comput-
ing  equipment  and  televisions.  However,  those  models  have  been
developed  for  a  lower  frequency  range  and  the  validity  of  the  mod-
els  for  the  frequency  range  2–150  kHz  needs  to  be  checked.

9.  Research  challenges

The  following  research  challenges  and  opportunities  for  future

research  have  been  identiﬁed.

9.1.  Emission

• Relations  between  converter  conﬁguration  and  control,  EMC   ﬁl-

ter,  and  primary  emission

• Origin  of  recurrent  oscillations  and  their  aggregation  with  multi-

ple  emitting  devices

• Impact  of  voltage  magnitude,  distortion,  source  impedance,  and
the  presence  of  other  end-user  equipment  nearby,  on  the  primary
and  secondary  emission

• Time-varying  nature  of  the  emission

9.2.  Propagation

• Transfer  between  devices  and  from  individual  devices  to  the  grid,

especially  the  impact  of  resonances  and  damping

• Aggregation  of  emission  from  different  devices,  including  the

aggregation  between  primary  and  secondary  emission

• Propagation  from  sources  of  emission  at  medium  or  high  voltage

to  lower  voltage  levels

• Distinction  between  primary  and  secondary  emission  by  means

of  modelling  and  measurements

9.3.  Interference

• The  impact  of  end-user  equipment  (emission  and  impedance)  on

the  performance  of  power-line  communication

• The  impact  of  short-duration  high  magnitude  emission  on  end-

user  equipment

• Emission  at  new  frequencies  from  non-linear  equipment  due  to

background  distortion

• Impact  of  voltage  distortion  on  performance  and  life  length  of

end-user  equipment  and  equipment  in  the  grid

• Methods  for  increasing  immunity  of  end-user  equipment

9.4.  Measurements

• Methods  for  accurate  and  reproducible  measurement  of  voltages

and  currents  at  higher  frequencies

• Methods  for  extracting  time-domain,  frequency-domain  and
time-frequency-domain  features  from  measured  waveforms

9.5.  Standardization

• Standardized  methods  for  quantifying  voltage  and  current  dis-

tortion  in  the  range  2–150  kHz

• Emission  and  immunity  limits  and  standardized  tests
• A  classiﬁcation  of  emission  based  on  phenomena,  characteristics

of  the  emission  and  difference  in  propagation

9.6.  Modelling  and  simulation

• Models  for  components  in  the  grid  and  for  end-user  equipment

connected  to  the  grid

• Models  for  active  converters  that  can  be  used  to  predict  their
emission,  their  impact  on  the  emission,  and  the  spread  of  distur-
bances  from  neighbouring  devices

• Modelling  guidelines  for  different  frequency  ranges  and  different

phenomena

10.  Conclusions

This  paper  reviews  the  literature  on  voltage  and  current  distor-
tion  in  the  frequency  range  between  2  and  150  kHz.  A  considerable
amount  of  material  has  been  published,  especially  concerning
sources  of  emission  and  interference  in  this  frequency  range.
This  material  should  form  the  basis  for  a  serious  and  substan-
tial  research  effort  to  provide  input  for  further  clariﬁcation  and
understanding  of  its  impact  on  the  grid  and  for  control  and  future
standardization.  A  number  of  research  challenges  have  been  clearly
identiﬁed  and  should  assist  researchers  and  engineers  working
with  an  increasingly  complex  grid  with  plenty  of  sources  of  higher
frequency—supraharmonics.

References

[1]  R.M.  Vines,  H.K.  Trussell,  L.J.  Gale,  J.B.  O’Neal,  Noise  on  residential  power

distribution  circuits,  IEEE  Trans.  Electromagn.Compat.  EMC-26  (November
(4))  (1984)  161–168.

[2]  E.O.A.  Larsson,  M.H.J.  Bollen,  M.G.  Wahlberg,  C.M.  Lundmark,  S.K.  Rönnberg,
Measurements  of  high-frequency  (2–150  kHz)  distortion  in  low-voltage
networks,  IEEE  Trans.  Power  Deliv.  25  (July  (3))  (2010)  1749–1757.

[3]  S.K.  Rönnberg,  M.H.J.  Bollen,  M.   Wahlberg,  Interaction  Between  narrowband
power-line  communication  and  end-user  equipment,  IEEE  Trans.  Power
Deliv.  26  (July  (3))  (2011)  2034–2039.

[4]  M.   Bollen,  M.   Olofsson,  A.  Larsson,  S.  Rönnberg,  M.   Lundmark,  Lundmark
standards  for  supraharmonics  (2  to  150  kHz),  IEEE  Electromagn.  Compat.
Mag.  3  (2016)  114–119.

[5]  CENELEC  SC  205A,  Study  report  II,  electromagnetic  interference  between

electrical  equipment/systems  in  the  frequency  range  below  150  kHz,  SC
205A/Sec0339/R,  April  2013.

[6]  B.  Ekehov,  S.  Halen,  T.  Larsson,  L.  Palmqvist,  A.  Edris,  D.  Kidd,  A.J.F.  Keri,  B.

Mehraban,  High-frequency  impacts  in  a  converter-based  back-to-back  tie;
the  Eagle  Pass  installation,  IEEE  Trans.  Power  Deliv.  18  (October  (4))  (2003)
1410–1415.

[7]  H.  Vahedi,  A.  Sheikholeslami,  M.   Tavakoli  Bina,  M.   Vahedi,  Review  and

simulation  of  ﬁxed  and  adaptive  hysteresis  current  control  considering
switching  losses  and  high-frequency  harmonics,  Adv.  Power  Electron.  2011
(2011),  Article  id  397872,  6  pages.

[8]  A.A.  Girgis,  M.C.  Clapp,  E.B.  Makram,  J.  Qiu,  J.G.  Dalton,  R.C.  Catoe,

Measurement  and  characterization  of  harmonic  and  high  frequency
distortion  for  a  large  industrial  load,  IEEE  Trans.  Power  Deliv.  5  (January  (1))
(1990)  427–434.

[9]  P.F.  Ribeiro,  Time-Varying  Waveform  Distortion  in  Power  Systems,

Wiley-IEEE  Press,  Chichester,  2009.

[10]  Y.  Baghzouz,  et  al.,  Time  varying  harmonics:  part  I—characterizing  measured

data,  IEEE  Trans.  Power  Deliv.  13  (July  (3))  (1998)  938–944.

[11]  Y.  Baghzouz,  et  al.,  Time  varying  harmonics:  part  II—harmonic  summation
and  propagation,  IEEE  Trans.  Power  Deliv.  17  (January  (1))  (2002)  279–285.
[12]  E.O.A.  Larsson,  C.M.  Lundmark,  M.H.J.  Bollen,  Distortion  of  ﬂuorescent  lamps

in   the  frequency  range  2–150  kHz,  Proc.  Int  Conf  on  Harmonics  and  Quality
of   Power  (ICHQP)  (2006).

[13]  J.J.  Spangler,  A.K.  Behera,  A  comparison  between  hysteresis  and  ﬁxed

frequency  boost  converters  used  for  power  factor  correction,  Proc.  Applied
Power  Electronics  Conference  (1993).

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

9

[14]  L.  Huber,  M.M.   Jovanovi ´c,  Design  and  optimization  of  single-stage

single-switch  input-current  shapers,  IEEE  Trans.  Power  Electron.  15  (January
(1))  (2000)  174–184.

[15]  J.  Sun,  On  the  zero-crossing  distortion  in  single-phase  PFC  converters,  IEEE

Trans.  Power  Electron.  19  (May  (3))  (2004)  685–692.

[16]  Y.  Levron,  H.  Kim,  W.   Erickson,  Design  of  EMI   ﬁlters  having  low  harmonic
distortion  in  high-power-factor  converters,  IEEE  Trans.  Power  Electron.  29
(July  (7))  (2014)  3403–3413.

[17]  A.  Kotsopoulos,  P.J.M.  Heskes,  M.J.  Jansen,  Zero-crossing  distortion  in

grid-connected  PV  inverters,  IEEE  Trans.  Ind.  Electron.  52  (April  (2))  (2005)
558–565.

[18]  C.  Unger,  K.  Krüger,  M.   Sonnenschein,  R.  Zurowski,  Disturbances  due  to

voltage  distortion  in  the  kHz  range—experiences  and  mitigation  measures,
Proc.  18th  Int.  Conf.  on  Electricity  Distribution  (2005).

[19]  N.  Mohan,  T.M.  Undeland,  Power  Electronics:  Converters,  Applications,  and

Design,  John  Wiley  &  Sons,  2007.

[20]  R.  Smolinski,  Conducted  Electromagnetic  Interference  (EMI)  in  Smart  Grids,

Springer  Science  &  Business  Media,  2012.

[21]  M.Y.  Kaikaa,  F.  Babaa,  A.  Khezzar,  M.   Boucherma,  Analytical  analysis  of  rotor
slot   harmonics  in  the  line  current  of  squirrel  cage  induction  motors,  J.  Electr.
Eng.  57  (1)  (2006)  12–19.

[22]  J.C.  Das,  Power  System  Analysis—  Short-circuit  Load  Flow  and  Harmonics,

2nd  ed.,  CRC  Press,  2012.

[23]  H.R.J.  Klewe,  Interference  Between  Power  Systems  and  Telecommunication

Lines,  Edward  Arnold  Publishers,  London,  1958.

[24]  J.  Arrillaga,  N.R.  Watson,  Power  System  Harmonics,  2nd  ed.,  Wiley,  2003.
[25]  A.  Gil-de-Castro,  A.  Moreno-Munoz,  A.  Larsson,  J.J.G.  de  la  Rosa,  M.H.J.

[45]  R.N.  Beres,  X.  Wang,  F.  Blaabjerg,  M.   Liserre,  C.L.  Bak,  Optimal  design  of
high-order  passive-damped  ﬁlters  for  grid-connected  applications,  EEE
Trans.  Power  Electron.  31  (March  (3))  (2016)  2083–2098.
[46]  R.L.  Ozenbaugh,  T.M.  Pullen,  EMI   ﬁlter  design,  CRC  Press,  2011.
[47]  S.  Rönnberg,  M.   Wahlberg,  M.   Bollen,  A.  Larsson,  M.   Lundmark,

Measurements  of  interaction  between  equipment  in  the  frequency  range  9
to   95  kHz,  Proc  of  20th  Int.  Conf.  on  Electricity  Distribution  (2009).

[48]  A.  Larsson,  M.   Bollen,  Measurement  result  from  1  to  48  ﬂuorescent  lamps  in

the   frequency  range  2  to  150  kHz,  2010  14th  Int.  Conf.  on  Proc.  Harmonics
and  Quality  of  Power  (ICHQP)  (2010)  1–8.

[49]  W.   Xu,  Yilu  Liu,  A  method  for  determining  customer  and  utility  harmonic

contributions  at  the  point  of  common  coupling,  IEEE  Trans.  Power  Deliv.  15
(April  (2))  (2000)  804–811.

[50]  T.  Pjajfar,  B.  Blaˇziˇc,  Harmonic  contributions  evaluation  with  the  harmonic

current  vector  method,  IEEE  Trans.  Power  Deliv.  23  (January  (1))  (2008)
425–433.

[51]  F.M.  Fernandez,  P.S.  Chandramohanon  Nair,  Method  for  separation  of
customer  and  utility  contributions  of  harmonics  at  point  of  common
coupling,  IET  Gener.  Transm.  Distrib.  7  (4)  (2013)  374–381.

[52]  S.  Rönnberg,  A.  Larsson,  M.  Bollen,  J.  Schanen,  A  simple  model  for  interaction
between  equipment  at  a  frequency  of  some  tens  of  kHz,  Proc.  21st  Int.  Conf.
on   Electricity  Distribution  (2011).

[53]  L.  Fumagalli,  G.  Borgone,  F.  Faggioni,  ELVIS  (Enel  Low  Voltage  Identiﬁcation
System):  improving  narrowband  PLC  communication  performance  by
means  of  electrical  characteristics  measurement  of  distribution  line,  Proc.
Int.   Conf.  on  Electricity  Distribution  (2015).

[54]  K.  Yang,  M.H.J.  Bollen,  E.O.A.  Larsson,  Aggregation  and  ampliﬁcation  of

Bollen,  LED  street  lighting:  a  power  quality  comparison  among  street  light
technologies,  Light.  Res.  Technol.  45  (December  (6))  (2013)  710–728.

wind-turbine  harmonic  emission  in  a  Wind  Park,  IEEE  Trans.  Power  Deliv.
30  (2)  (2014)  791–799.

[26]  D.A.  Martínez,  A.  Pavas,  Current  supraharmonics  identiﬁcation  in  commonly

[55]  K.  Yang,  M.   Bollen,  L.Z.  Yao,  Theoretical  emission  study  of  windpark  grids,

used  low  voltage  devices,  Proc.  2015  IEEE  Workshop  on  Power  Electronics
and  Power  Quality  Applications  (PEPQA)  (2015)  1–5.

[27]  S.  Schöttke,  J.  Meyer,  P.  Schegner,  S.  Bachmann,  Emission  in  the  frequency
range  of  2  kHz  to  150  kHz  caused  by  electrical  vehicle  charging,  Proc.
International  Symposium  on  Electromagnetic  Compatibility  (EMC  Europe)
(2014).

[28]  F.  Möller,  S.  Müller,  C.  Wald,  S.  Isensee,  J.  Meyer,  P.  Schegner,  Impact  of

electric  vehicle  charging  on  unbalance  and  harmonic  distortion—ﬁeld  study
in   an  urban  residential  area,  Proc.  Int.  Conf.  Electricity  Distribution  (2015).

[29]  M.   Rioual,  C.  Zakhour,  M.   López-Amorós,  J.-L.  Bargues,  S.  Nasr,  Description  of
the   low  frequency  phenomena  involved  when  connecting  a  3  kW  EV  charger
to   the  distribution  network  and  their  validation  by  on  site  tests,  Panel
presentation,  2015  IEEE  PES  General  Meeting,  2015.

[30]  N.  Uribe-Pérez,  I.  Angulo,  L.  Hernández-Callejo,  T.  Arzuaga,  D.  de  la  Vega,  A.
Arrinda,  Study  of  unwanted  emissions  in  the  CENELEC-A  band  generated  by
distributed  energy  resources  and  their  inﬂuence  over  narrow  band  power
line  communications,  Energies  9  (12)  (2016).

[31]  A.  Moreno-Munoz,  A.  Gil-De-Castro,  S.  Rönnberg,  M.   Bollen,  E.

Romero-Cadaval,  Ongoing  work  in  CIGRE  working  groups  on
supraharmonics  from  power–electronic  converters,  Proc.  23rd  Int.  Conf.  on
Electricity  Distribution  (2015).

[32]  M.   Klatt,  J.  Meyer,  P.  Schegner,  A.  Koch,  J.  Myrzik,  C.  Korner,  T.  Darda,  G.
Eberl,  Emission  levels  above  2  kHz—laboratory  results  and  survey
measurements  in  public  low  voltage  grids,  Proc.  22nd  Int.  Conf.  and
Exhibition  On  Electricity  Distribution  (CIRED)  (2013).

[33]  R.  Torquato,  W.   Freitas,  G.R.T.  Hax,  A.R.  Donadon,  R.  Moya,  High  frequency

harmonic  distortions  measured  in  a  Brazilian  solar  farm,  17th  International
Conference  on  Harmonics  and  Quality  of  Power  (ICHQP).  16–19  October
(2016).

[34]  M.   Klatt,  A.  Dorado,  J.  Meyer,  P.  Schegner,  J.  Backes,  Ran  Li,  Power  quality

aspects  of  rural  grids  with  high  penetration  of  microgeneration,  mainly
PV-installations,  Proc.  21st  Int  Conf  on  Electricity  Distribution  (2011).
[35]  CIGRE  Technical  Brochure  672,  Power  quality  aspects  of  solar  power,  2016.
[36]  Bin  Wu,   et  al.,  Power  Conversion  and  Control  of  Wind  Energy  Systems,  John

Wiley  &  Sons,  2011.

[37]  G.  Chicco,  A.  Russo,  F.  Spertino,  Supraharmonics:  concepts  and  experimental
results  on  photovoltaic  systems,  Proc.  XII  Int  School  on  Nonsinusoidal
Currents  and  Compensation  ISNCC  (2015).

[38]  A.  Varatharajan,  S.  Schoettke,  J.  Meyer,  A.  Abart,  Harmonic  emission  of  large
PV   installations—case  study  of  a  1  MW  solar  campus,  Proc.  Int  Conf  on
Renewable  Energy  and  Power  Quality  (ICREPQ)  (2014).

Proc.  Electric  Power  Quality,  Utilization  (2011).

[56]  C.  Unger,  Current  developments  for  the  reduction  of  power  quality  related
disturbances  in  industrial  installations,  Proc.  8th  Int.  Conf.  on  Advances  in
Power  System  Control,  Operation  and  Management  (APSCOM)  (2009).

[57]  K.  Temma,  F.  Ishiguro,  N.  Toki,  I.  Iyoda,  J.J.  Paserba,  Clariﬁcation  and

measurements  of  high  frequency  harmonic  resonance  by  a  voltage  sourced
converter,  IEEE  Trans.  Power  Deliv.  20  (Januray  (1))  (2005)  450–457.
[58]  C.  Leroi,  E.  De  Jaeger,  Conducted  disturbances  in  the  frequency  range

2–150  kHz:  inﬂuence  of  the  LV  distribution  grids,  Proc.  Int.  Conf.  Electricity
Distribution  (2015).

[59]  M.   Bollen,  S.  Rönnberg,  Primary  and  secondary  harmonics  emission;

harmonic  interaction  —a  set  of  deﬁnitions,  2016  IEEE  17th  Int.  Conf.  on  Proc
of   Harmonics  and  Quality  of  Power  (ICHQP)  (2016).

[60]  A.  Gil-de-Castro,  A.  Larsson,  S.  Rönnberg,  M.   Bollen,  LED  lamps  under

different  EMC   environments,  Proc.  Int.  Conf.  Electricity  Distribution  (2015).
[61]  S.  Rönnberg,  M.   Bollen,  Measurements  of  primary  and  secondary  emission
in   the  supraharmonic  frequency  range  2–150  kHz,  Proc  of  Int.  Conf.
Electricity  Distribution  (2015).

[62]  Electromagnetic  Interference  between  electrical  equipment/systems  in  the

frequency  range  below  150  kHz,  SC205A/Sec0329/DC2013.

[63]  K.  Hermanns,  G.  Griepentro,  Potential  electromagnetic  interference  between

long  wave  radio  services  and  overhead  transmission  lines  caused  by
operation  of  High  Voltage  Direct  Current  Voltage  Source  Converters
(HVDC-VSC)—a  ﬁrst  estimation,  Proc  CIGRE  Symposium  (2015).

[64]  G.  Singh,  E.R.  Collins,  S.K.  Rönnberg,  E.O.A.  Larsson,  M.H.J.  Bollen,  Impact  of
high  frequency  conducted  voltage  disturbances  on  LED  driver  circuits,  IEEE
PES   General  Meeting  (2017).

[65]  D.E.  Cameron,  J.H.  Lang,  S.D.  Umans,  The  origin  and  reduction  of  acoustic

noise  in  double  salient  variable-reluctance  motors,  IEEE  Trans.  Ind.  Appl.  28
(November/December  (6))  (1992)  1250–1255.

[66]  W.C.  Lo,  C.C.  Chan,  Z.Q.  Zhu,  Lie  Xu,  D.  Howe,  K.T.  Chau,  Acoustic  noise

radiated  by  PWM-controlled  induction  machine  drives,  IEEE  Trans.  Ind.
Electron.  47  (August  (4))  (2000)  880–889.

[67]  A.  Larsson,  A.  Gil-de-Castro,  M.   Wahlberg,  M.  Bollen,  Field  and  laboratory

measurements  of  interference  with  light  equipment  due  to  waveform
distortion  originating  from  a  large  rectiﬁer,  Proc.  Int.  Conf.  Electricity
Distribution  (2015).

[68]  M.   Klatt,  J.  Meyer,  P.  Schegner,  Comparison  of  measurement  methods  for  the
frequency  range  of  2  kHz  to  150  kHz,  2014  IEEE  16th  Int.  Conf.  on  Proc  of
Harmonics  and  Quality  of  Power  (ICHQP)  (2014)  818–822.

[69]  A.  Larsson,  On  High-frequency  Distortion  in  Low-voltage  Power  Systems,

[39]  T.  Joshi,  G.  Heydt,  R.  Ayyanar,  High  frequency  spectral  components  in

PhD  Thesis,  Luleå  University  of  Technology,  2011.

distribution  voltages  and  currents  due  to  photovoltaic  resources,  in:  2014
North  American  Power  Symposium  (NAPS),  Pullman,  WA,   2014,  pp.  1–6.

[40]  Z.  Chen,  E.  Spooner,  Grid  power  quality  with  variable  speed  wind  turbines,

IEEE  Trans.  Energy  Convers.  16  (June  (2))  (2001)  148–154.

[41]  Report  from  Task  Force  dealing  with  Emission  limits  in  the  range  from  2  to
9  kHz  in  Japan,  Presented  at  JWG   C4.24/CIRED  meeting,  Lyon,  France,  2015.
[42]  G.F.  Bartak,  A.  Abart,  EMI   in  the  frequency  range  2–150  kHz,  Proc.  Int  Symp

on  Electromagnetic  Compatibility  (2014).

[43]  M.   Katayama,  T.  Yamazato,  H.  Okada,  A  mathematical  model  of  noise  in

narrowband  power  line  communication  systems,  IEEE  J.  Sel.  Areas  Commun.
24  (July  (7))  (2006)  1267–1276.

[44]  Z.  Raﬁque,  M.E.  Haque,  M.A.  Mahmud,  Impacts  of  voltage  surge  and

resonance  on  a  grid  connected  variable  speed  wind  turbine  and  their
remedial  measures,  Proc  of  IEEE  PES  General  Meeting  (2015).

[70]  L.  Alﬁeri,  A.  Bracale,  G.  Carpinelli,  A.  Larsson,  A  wavelet-modiﬁed  ESPRIT

hybrid  method  for  assessment  of  spectral  components  from  0  to  150  kHz,
Energies  10  (1)  (2017)  97.

[71]  P.  Verzele,  J.  Knockaert,  J.  Desmet,  Appropriate  methods  to  analyse  power
conversion  harmonics,  Proc.  Int.  Conf.  on  Renewable  Energies  and  Power
Quality  (ICREPQ  13)  (2013).

[72]  M.   Klatt,  J.  Meyer,  M.   Elst,  P.  Schegner,  Frequency  responses  of  MV  voltage
transformers  in  the  range  of  50  Hz  to  10  kHz,  2010  14th  Int.  Conf.  on  Proc.
Harmonics  and  Quality  of  Power  (ICHQP)  (2010)  1–6.

[73]  F.J.C.  Corripio,  J.A.C.  Arrabal,  L.D.  del  Rio,  J.T.E.  Munoz,  Analysis  of  the  cyclic
short-term  variation  of  indoor  power  line  channels,  IEEE  J.  Sel.  Areas
Commun.  24  (2006)  1327–1338.

[74]  I.  Gu,  M.H.  Bollen,  Estimating  interharmonics  by  using  sliding-window

ESPRIT,  IEEE  Trans.  Power  Deliv.  23  (2008)  13–23.

10

S.K.  Rönnberg  et  al.  /  Electric  Power  Systems  Research  150  (2017)  1–10

[75]  A.V.  Oppenheim,  R.W.  Schafer,  J.R.  Buck,  Discrete-time  Signal  Processing,

[91]  O.  Mayr,  Die  Erde  som  Wechselstromleiter,  Elektrotech.  Z.  36  (1925)

vol.   2,  Prentice-Hall,  Englewood  Cliffs,  NJ,  1989.

[76]  IEC  60050  (161)—Electropedia.
[77]  IEC  document  77A/914/CD  Amendment  1  to  IEC  61000-2-2:

Electromagnetic  compatibility  (EMC)  –  Part  2-2:  Environment  –
Compatibility  levels  for  low-frequency  conducted  disturbances  and
signalling  in  public  low-voltage  power  supply  systems,  2015-11-06.
[78]  IEC  document  77A/901/INF,  Deﬁnition  of  Compatibility  Levels  in  the
Frequency  range  2–150  kHz.  Assessment  162  of  consensus  level
(Maintenance  IEC  61000-2-2  and  61000-2-12),  2015-08-21.

[79]  IEC  document  77A/915/DC  Maintenance  of  publication:  IEC  61000-2-2:

Electromagnetic  compatibility  (EMC)  –  Part  2-2:  Environment  –
Compatibility  levels  for  low-frequency  conducted  disturbances  and
signaling  in  public  low-voltage  power  supply  systems,  2015-11-06.
[80]  IEC  SC  77A  Plenary  meeting  (77A/913/RM)  in  Stresa,  Italy  2015-09-21  to

2015-09-25.

[81]  A.R.  Hileman,  Insulation  Coordination  for  Power  Systems,  Marcel  Dekker,

1999.

[82]  B.  Gustavsen,  Wide  band  modeling  of  power  transformers,  IEEE  Trans.

Power  Deliv.  19  (2004)  414–422.

[83]  R.C.  Degeneff,  A  general  method  for  determining  resonances  in  transformer

windings,  IEEE  Trans.  Power  Appar.  Syst.  96  (1977)  423–430.

[84]  P.T.M.  Vaessen,  Transformer  model  for  high  frequencies,  IEEE  Trans.  Power

Deliv.  3  (1988)  1761–1768.

[85]  S.  Chimklai,  J.R.  Marti,  Simpliﬁed  three-phase  transformer  model  for
electromagnetic  transient  studies,  IEEE  Trans.  Power  Deliv.  10  (1995)
1316–1325.

[86]  J.A.  Martinez,  R.  Walling,  B.A.  Mork,  J.  Martin-Arnedo,  D.  Durbak,  Parameter
estimation  for  modeling  system  transients—part  III:  transformers,  IEEE
Trans.  Power  Deliv.  20  (July  (3))  (2005)  2051–2062.

[87]  J.A.  Martinez,  B.A.  Mork,  Transformer  modeling  for  low-  and  mid-frequency

transients—a  review,  IEEE  Trans.  Power  Deliv.  20  (April  (2))  (2005)
1625–1632.

[88]  K.  Dostert,  Powerline  Communications,  Prentice  Hall  PTR,  2001.
[89]  B.  Gustavsen,  J.A.  Martinez,  D.  Durbak,  Parameter  determination  for

modeling  system  transients—Part  II:  insulated  cables,  IEEE  Trans.  Power
Deliv.  20  (July  (3))  (2005)  2045–2050.

[90]  J.R.  Carson,  Wave  propagation  in  overhead  wires  with  ground  return,  Bell

Syst.  Tech.  J.  5  (1926)  539–554.

S.1352–S.1355,  1436–1440.

[92]  J.R.  Marti,  Accurate  modelling  of  frequency-dependent  transmission  lines  in
electromagnetic  transient  simulations,  IEEE  Trans.  Power  Appar.  Syst.
PAS-101  (1982)  147–157.

[93]  R.G.  Olson,  T.A.  Pankaskie,  On  the  exact  and  image  theories  for  wires  at  or
above  the  Earth’s  interface,  IEEE  Trans.  Power  Appar.  Syst.  PAS-102  (1983)
769–778.

[94]  E.J.M.  van  Heesch,  A.P.J.  van  Deursen,  M.A.  van  Houten,  G.A.P.  Jacobs,  W.F.J.

Kersten,  P.C.T.  van  der  Laan,  Field  tests  and  response  of  the  D/I  H.V.
measuring  system,  Proc.  6th  Int  Conf  on  High  Voltage  Engineering  (1989).

[95]  H.  Nakanishi,  A.  Ametani,  Transient  calculation  of  a  transmission  line  using

superposition  law,  IEE  Proc.  133  (Pt.  C)  (1986)  263–269.

[96]  R.  Langella,  L.  Nugnes,  A.  Testa,  Behavior  of  MV   lines  from  2.5  to  100  kHz,

Proc.  IEEE  PES  General  Meeting  (2012).

[97]  C.J.  Kikkert,  A  PLC  frequency  model  of  3  phase  power  distribution

transformers,  Proc.  3rd  International  Conference  on  Smart  Grid
communications  (SmartGridComm)  (2012).
[98]  R.  Kristjánsson,  A  frequency  dependent  model  for

(cid:2)-Y0  coupled

distribution  transformers,  Proc.  Power  Tech  (2001).

[99]  S.  Schöttke,  S.  Rademacher,  J.  Meyer,  P.  Schegner,  Transfer  characteristic  of  a
MV/LV  transformer  in  the  frequency  range  between  2  kHz  and  150  kHz,  Proc
IEEE  Int.  Symposium  on  Electromagnetic  Compatibility  (EMC)  (2015).
[100]  Hua  Bai,  C.  Mi,   Transients  of  Modern  Power  Electronics,  Wiley,  2011.
[101]  R.  Teodorescu,  M.   Liserre,  P.  Rodríguez,  Grid  Converters  for  Photovoltaic  and

Wind  Power  Systems,  Wiley-IEEE  Press,  2011.

[102]  E.C.  dos  Santos,  E.R.C.  da  Silva,  Advanced  Power  Electronics

Converters—PWM  Converters  Processing  AC  Voltages,  Wiley,  2015.

[104]  S.  Yanchenko,  J.  Meyer,  Harmonic  emission  of  household  devices  in  presence

of  typical  voltage  distortions,  Proc.  IEEE  Power  Tech  (2015).

[105]  J.  Drapela,  R.  Langella,  Lighting  Systems—Light  sources  in  modern  buildings:
characterization,  modelling  and  simulations,  panel  presentation  at  PES
General  Meeting,  Washington,  USA,  2014.

[106]  S.  Bhattacharyya,  J.F.G.  Cobben,  W.L.  Kling,  Harmonic  current  pollution  in  a

low  voltage  network,  Proc.  Power  and  Energy  Society  General  Meeting
(2010)  1–8.

