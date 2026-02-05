# Toshio Nakagawa 

## Shock and Damage Models in Reliability TheorySpringer Series in Reliability Engineering# Series Editor 

Professor Hoang Pham
Department of Industrial Engineering
Rutgers
The State University of New Jersey
96 Frelinghuysen Road
Piscataway, NJ 08854-8018
USA

## Other titles in this series

The Universal Generating Function in Reliability Analysis and Optimization Gregory Levitin

Warranty Management and Product Manufacture
D.N.P Murthy and Wallace R. Blischke

Maintenance Theory of Reliability
Toshio Nakagawa
System Software Reliability
Hoang Pham
Reliability and Optimal Maintenance
Hongzhou Wang and Hoang Pham
Applied Reliability and Quality
B.S. DhillonToshio Nakagawa

# Shock and Damage Models in Reliability TheoryToshio Nakagawa, PhD<br>Department of Marketing and Information Systems<br>Aichi Institute of Technology<br>1247 Yachigusa, Yakusa-cho<br>Toyota 470-0392<br>Japan

British Library Cataloguing in Publication Data
Nakagawa, Toshio, 1942-
Shock and damage models in reliability theory. - (Springer
series in reliability engineering)

1. Reliability (Engineering) - Mathematical models
I. Title
$620^{\prime} .00452^{\prime} 015118$
ISBN-13: 9781846284410
ISBN-10: 1846284414
Library of Congress Control Number: 2006936015
Springer Series in Reliability Engineering series ISSN 1614-7839
ISBN-10: 1-84628-441-4 e-ISBN 1-84628-442-2 Printed on acid-free paper
ISBN-13: 978-1-84628-441-0
(c) Springer-Verlag London Limited 2007

Apart from any fair dealing for the purposes of research or private study, or criticism or review, as permitted under the Copyright, Designs and Patents Act 1988, this publication may only be reproduced, stored or transmitted, in any form or by any means, with the prior permission in writing of the publishers, or in the case of reprographic reproduction in accordance with the terms of licences issued by the Copyright Licensing Agency. Enquiries concerning reproduction outside those terms should be sent to the publishers.

The use of registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant laws and regulations and therefore free for general use.

The publisher makes no representation, express or implied, with regard to the accuracy of the information contained in this book and cannot accept any legal responsibility or liability for any errors or omissions that may be made.

# 987654321 

Springer Science+Business Media
springer.com# Preface 

Most engineering systems suffer some deterioration with time from wear, fatigue, and damage, and ultimately fail when their strength exceeds a critical level. Failure mechanisms by which the causes of failures are brought about are physical processes. The types of failure causes, how to proceed to failure by which causes, and the consequences of failures have been physically studied. This has been developed in fracture mechanics and mechanics of materials and has applied to such components and systems. On the other hand, failure mechanisms are in probabilistic and stochastic motions. Such behaviors are mathematically observed and analyzed in the study of stochastic processes.

My purpose in writing this book is to build a bridge between theory and practice and to introduce the reliability engineer to some damage models. Failures of units are generally classified into two failure modes: Catastrophic failure in which units fail suddenly and degradation failure in which units deteriorate gradually with time. The former failures often occur in electric parts. The latter failures mainly occur in machinery. Such reliability models are called shock or damage models and can be analyzed, using the techniques of stochastic processes.

There exist a large number of damage models that form reliability models mechanically and stochastically in the real world. Reliability quantities of these models have been theoretically obtained. However, there is not any special book written on these fields except the book [2]. Their case studies for reliability are very fews because the analysis might be too difficult theoretically to apply them to practical models. When and how maintenance policies for damage models are made are important.

I have just published the monograph Maintenance Theory of Reliability [1] that summarizes maintenance policies for system reliability models. However, it does not deal with any damage model. This book is based mainly on the research results studied by the author and my colleagues from classical ones to new topics. It deals primarily with shock and damage models, their reliability properties, and maintenance policies. The reliability measures of such models can be calculated by using renewal and cumulative processes. Optimummaintenance policies are theoretically discussed by using the results of [1]. Furthermore, these models can be applied to actual models practically, using these results.

This book is composed of ten chapters. Chapter 1 gives some examples of damage models and is devoted to explaining elementary stochastic processes and shock processes needed for understanding their models. Chapter 2 is mainly devoted to cumulative damage models that fail subject to shocks. Standard models in which a unit fails when its total damage exceeds a failure level are explained, and their modified models are proposed. Some reliability quantities of such models are analytically derived, using the techniques of stochastic processes. Chapter 3 summarizes replacement policies and some modified policies. Chapter 4 is devoted to a parallel system whose units fail subject to shocks and a two-unit system whose units fail by interaction with induced failure and shock damage. Chapters 5 and 6 are devoted to replacement and preventive maintenance policies in which the total damage is investigated only at periodic times. Chapter 7 considers imperfect preventive maintenance policies in which the preventive maintenance is done at sequential times and reduces the total damage. In Chapters 4-7, optimum policies that minimize the expected cost are analytically discussed. Chapters 8 and 9 take up the garbage collection of a computer system and the backup scheme of a database system as typical practical examples of damage models. Chapter 10 is devoted to reviewing briefly similar related models presented in other fields such as shot noise, insurance, and stochastic duels.

This book gives a detailed introduction to damage models and their maintenance policies, and provides the current status and further studies in these fields. It will be helpful for mechanical engineers and managers engaged in reliability work. Furthermore, sufficient references leading to further studies are cited at the end of the book. This book will serve as a textbook and reference book for graduate students and researchers in reliability and mechanics.

I wish to thank Professor Shunji Osaki for Chapter 2, Dr. Kodo Ito for Chapters 1 and 3, Professor Masaaki Kijima for Chapters 4 and 7, Professor Kazumi Yasui for Chapter 6, Dr. Takashi Satow for Chapter 8, and Professors Cun Hua Qian and Shouji Nakamura who are co-workers of our research papers for Chapter 9. I wish to express my special thanks to Professor Fumio Ohi for his careful reviews of this book, and to Dr. Satoshi Mizutani and my daughter Yorika for their support in writing and typing this book. Finally, I would like to express my sincere appreciation to Professor Hoang Pham, Rutgers University, and editor, Anthony Doyle, Springer-Verlag, London, for providing the opportunity for me to write this book.# Contents 

1 Introduction ..... 1
1.1 Renewal Processes ..... 4
1.2 Shock Processes ..... 11
2 Damage Models ..... 15
2.1 Cumulative Damage Model ..... 16
2.2 Independent Damage Model ..... 21
2.3 Failure Rate ..... 24
2.4 Continuous Wear Processes ..... 26
2.5 Modified Damage Models ..... 28
3 Basic Replacement Policies ..... 39
3.1 Three Replacement Policies ..... 40
3.2 Optimum Policies ..... 42
3.3 Modified Replacement Models ..... 47
4 Replacement of Multiunit Systems ..... 61
4.1 Parallel System in a Random Environment ..... 62
4.1.1 Replacement Model ..... 62
4.1.2 Extended Replacement Models ..... 64
4.1.3 Replacement at Shock Number ..... 68
4.2 Two-unit System with Failure Interactions ..... 70
4.2.1 Model 1: Induced Failure ..... 72
4.2.2 Model 2: Shock Damage ..... 75
4.2.3 Modified Models ..... 77
5 Periodic Replacement Policies ..... 81
5.1 Basic Replacement Models ..... 82
5.2 Discrete Replacement Models ..... 84
5.3 Deteriorated Inspection Model ..... 86
5.3.1 Expected Cost ..... 875.3.2 Optimum Policy ..... 89
5.4 Replacement with Minimal Repair ..... 90
5.4.1 Expected Cost ..... 91
5.4.2 Optimum Policies ..... 92
5.5 Modified Replacement Models ..... 97
6 Preventive Maintenance Policies ..... 103
6.1 Condition-based Preventive Maintenance ..... 104
6.1.1 Expected Cost Rate ..... 104
6.1.2 Optimum Policy ..... 108
6.2 Modified Models ..... 109
7 Imperfect Preventive Maintenance Policies ..... 117
7.1 Model and Expected Cost ..... 118
7.2 Optimum Policies ..... 122
7.3 Optimum Policies for a Finite Interval ..... 126
8 Garbage Collection Policies ..... 131
8.1 Standard Garbage Collection Model ..... 132
8.2 Periodic Garbage Collection Model ..... 137
8.3 Modified Periodic Garbage Collection Model ..... 143
9 Backup Policies for a Database System ..... 147
9.1 Incremental Backup Policy ..... 149
9.1.1 Cumulative Damage Model with Minimal Maintenance ..... 150
9.1.2 Incremental Backup ..... 154
9.2 Incremental and Cumulative Backup Policies ..... 158
9.2.1 Expected Cost Rates ..... 159
9.3 Optimum Full Backup Level for Cumulative Backup ..... 163
10 Other Related Stochastic Models ..... 167
10.1 Other Models ..... 167
10.2 Stochastic Duels ..... 170
References ..... 175
Index ..... 187# Introduction 

The number of aged fossil-fired power plants is increasing in Japan. For example, about one-third of such plants are currently operating at from 150 thousand to 200 thousand hours (from 17 to 23 years), and about a quarter of them are above 200 thousand hours. Furthermore, public infrastructures in advanced nations will become obsolete in the near future [3]. A deliberate maintenance plan is indispensable to operate power and chemical plants without serious trouble.

The importance of maintenance for aged plants is much higher than that for new ones because the probability of the occurrence of severe events increases and new failure phenomena might appear according to the degradation of plants. Actual lifetimes of plant components such as steam and gas turbines, boilers, pipes, and valves, are almost different from predicted ones because they are affected by various factors such as material quality and operating conditions $[4,5]$. Therefore, maintenance plans have to be reestablished at appropriate times during the operating lives of these components.

The simplest damage model is the stress-strength model where a component fails when its strength has been below a critical stress level [6]. If the fatigue subject to varying stress can be estimated, Miner's rate can be applied directly, using an $S-N$ curve $[7,8]$. This is utilized widely for predicting lifetimes of various kinds of mechanical productions by modifying Miner's rule $[9]$.

The progress of physical damage to assess the life of components precisely would be made previously and accurately. For example, the progress of low alloy steel that is used for high temperature and pressure components of a thermal power plant, is observed with a microscope as follows: During the first half of the life, changes in its microstructure appear in the welded heat-affected area. During the latter half, the number of voids that are small cavities at boundaries between crystalline grains increases, and their coalescence results in the growth of a crack. Recently, such damage assessment and life estimation are actively performed by utilizing a digital microscope, a computer image processor, and software [10].Failures of units or systems such as parts, equipment, components, devices, materials, structures, and machines are generally classified into two failure modes: Catastrophic failure in which units fail by some sudden shock and degradation failure in which units fail by physical deterioration suffered from some damage. In the latter case, units fail when the total damage due to shocks has exceeded a critical failure level. This is called a cumulative damage model or shock model with additive damage and can be described theoretically by a cumulative process [11] in stochastic processes.

We can apply such damage models to actual units that are working in industry, service, information, and computers, and show typical examples that are familiar.
(1) A vehicle axle fails when the depth of a crack has exceeded a critical level. In actual situations, a train axle is replaced at the distance traveled or the number of revolutions [12]. A tire on an automobile is a similar example $[2,13]$.
(2) A battery supplies electric power that was stored by chemical change. It is weakened by use and becomes useless at the end of chemical change [14]. This corresponds to the damage model by replacing shock with use and damage with oxidation or deoxidation.
(3) The strength of a fibrous carbon composite is essentially determined by the strength of fibers. When a composite specimen is placed under tensile stress, the fibers themselves may break within the material. Such materials are broken based on cumulative damage $[15,16]$.
(4) Garbage collection in a database system is a simple method to reclaim the location of active data because updating procedures reduce storage areas and worsen processing efficiency. To use storage areas effectively and to improve processing efficiently, garbage collections are done at suitable times. Such a garbage collection model corresponds to the damage model by replacing shock with update and damage with garbage. Some garbage collection models will be discussed analytically in Chapter 8.
(5) The data in a computer system are frequently updated by adding or deleting them, and are stored in secondary media. However, data files are sometimes broken by several errors due to noises, human errors, and hardware faults. The most dependable method to ensure the safety of data takes their backup copies at appropriate times. This corresponds to the damage model by replacing shock with update and damage with dumped files, and will be discussed analytically in Chapter 9.

Furthermore, damage models were applied to crack growth models [2,1720] and to welded joints [21], floating structures [22], reinforced concrete structures [23], and plastic automotive components [24]. Such stochastic models of fatigue damage of materials were described in detail [25, 26]. Failure mechanisms of damage models in engineering systems were summarized [27].

We consider a typical cumulative damage model in which shocks occur in random times and the damage incurred such as fatigue, wear, crack growth,creep, and dielectric breakdown is additive. The general concept of such processes was theoretically based on $[28,29]$. Several contributions to stochastic damage models or compound Poisson processes were made at the beginning by several authors: The first model, where shocks occur in a Poisson process and the amount of damage due to each shock has a gamma distribution, was considered in detail [30]. Much of the earlier research were reviewed [11]. Furthermore, the various properties of failure distributions when shocks occur in a Poisson process were extensively investigated [31-33]. On the other hand, cumulative wear increases continuously with time and is represented as a specified function of a stochastic process [34-39]. This was formulated and analyzed by using the idea of a finite Markov chain [2]. This is also called a wear process.

We have to pay attention only to the essential laws governing objective models of reliability study, and grasp damage processes, and try to formulate them simply, avoiding small points. In other words, it would be necessary to form stochastic models of causing and making up damage that outline the observational and theoretical features of complex phenomena.

Most of the contents of this book are based on the original work of our research group and some new results are added. Stochastic and shock processes needed for learning damage models are summarized briefly in Chapter 1. These results are introduced without detailed explanations and proofs.

Chapter 2 summarizes only the known results of cumulative damage models and their modified models based on $[11,33,40]$, that could be applied to maintenance policies discussed in the following chapters. Next, we survey briefly the damage model whose total amount increases with time [37,39,41].

Suppose that a unit subject to shocks is replaced with a new one at failure or undergoes corrective maintenance after failure. However, such maintenance after failure may be done at great cost and take a long time. The most important problem of maintenance policies is to determine in advance when and how to do better maintenances before failure. From these points of view, a wide variety of uses for maintenance policies are effectively summarized and their optimum policies are fully discussed [1].

The optimum policies for a cumulative damage model where a unit is replaced before failure at a threshold level of damage [42-45] or at a planned time [46-50] were derived. In Chapter 3, we consider three replacement policies for a cumulative damage model in which a unit is replaced before failure at a planned time, at a shock number, or at a managerial damage level [51]. Optimum replacement policies that minimize the expected cost rates are discussed analytically. Furthermore, extended replacement models in which a unit is replaced at the first shock over a planned time and shock number are proposed.

Most systems are composed of multicomponent systems. However, in general, it would be very difficult to analyze the damage models of such systems theoretically. We consider a system with $n$ different units each of which receives damage due to shock and derive the failure distribution of the systemin (4) of Section 2.5. Furthermore, in Chapter 4, we take up a parallel system in a random environment $[52,53]$ and consider two models of a two-unit system with failure interactions [54]. Optimum number of units for a parallel system and the number of failures for an interaction model that minimize the expected cost rates are derived.

We should do only some minimal maintenance at each failure in large and complex systems. This is called periodic replacement with minimal repair at failures in Chapter 4 of [1]. In Chapter 5, a unit fails with a certain probability for the total damage due to shocks and undergoes minimal repair. Then, a unit is replaced at a planned time, at a shock number, or at a managerial damage level. In this case, optimum replacement policies that minimize the expected cost rates are discussed analytically [55].

Most operating units are repaired when they have failed. However, it may require much time and high cost to repair a failed unit. The respective maintenance after failure and before failure is called corrective maintenance (CM) and preventive maintenance (PM). This becomes the same as the replacement model theoretically by taking CM and PM as the replacement after failure and before failure, respectively, and the repair time as the time required for replacement.

In Chapter 6, we take up the PM policy in which the test to investigate some characteristics of a unit is planned at periodic times and the PM is done at a planned time when the total damage or shock number has exceeded a managerial level or number [56]. Several modified models are considered and their expected cost rates are derived. Furthermore, in Chapter 7, we apply the imperfect PM model to a cumulative damage model in which the total damage decreases at each PM. An optimum sequential PM policy in which a unit has to be operating over a finite interval and is replaced at a specified PM number is computed numerically [57].

In Chapters 8 and 9, we apply the cumulative damage model to the garbage collection policy [58] and the backup policy for a computer system [59] as typical examples, respectively. Optimum policies that the garbage collection is done at a planned time or at an update number are derived. Three schemes as recovery techniques are introduced, and optimum backup times are discussed analytically and compared numerically.

Such phenomena have been observed frequently in probability fields. Finally, we present compactly in Chapter 10 that the damage model can be applied to related fields such as other reliability models, insurance, shot noise, and stochastic duels. Several quantities of such models are similarly derived, using the techniques of shock and damage models.

# 1.1 Renewal Processes 

In this section, we briefly introduce some basic properties of renewal processes for reliability systems based on the books [11,60,61]. For more detailed results

Fig. 1.1. Total number of failed units over time axis
and applications of stochastic processes, we refer readers to the books [62, 63]. Consider a one-unit system with repair or replacement whose time is negligible, i.e., a new unit starts to operate at time 0 and is repaired or replaced when it fails, where the time for repair or replacement is negligible. When the repair or replacement is completed, the unit begins to operate again. If the unit is like new after repair or replacement, then the system forms a renewal process. This arises from the study of self-renewing aggregates [11] and plays an important role in the analysis of probability models with sums of independent nonnegative random variables. Figure 1.1 is a sample graph that presents the total number $N(t)$ of failed units during a time interval $[0, t]$. Some plots of number of failures versus time for repairable systems were illustrated [64]. In that case, the counting process $\{N(t) ; t \geq 0\}$ is called a renewal process. In particular, when the unit fails exponentially, i.e., the times between failures are independent and identically distributed exponentially, a renewal process becomes a Poisson process. A Poisson process is dealt with frequently as a special case of a renewal process. On the other hand, if the unit after repair has the same age as that before repair, then the counting process $\{N(t) ; t \geq 0\}$ is called a nonhomogeneous Poisson process. This corresponds to the unit that undergoes minimal repair at each failure.

# (1) Renewal Process 

Consider a sequence of independent and nonnegative random variables $\left\{X_{1}\right.$, $\left.X_{2}, \cdots\right\}$, in which $\operatorname{Pr}\left\{X_{j}=0\right\}<1$ for all $j$ because of avoiding the triviality.Suppose that $X_{j}(j=1,2, \cdots)$ have an identical distribution $F(t)$ with finite mean $\mu_{1}$ and $F(0) \equiv 0$.

Letting $S_{n} \equiv \sum_{j=1}^{n} X_{j}(n=1,2, \cdots)$ and $S_{0} \equiv 0$, we define $N(t) \equiv$ $\max _{n}\left\{S_{n} \leq t\right\}$ that represents the number of renewals in $[0, t]$. Renewal theory is mainly devoted to the investigation into the probabilistic properties of a discrete random variable $N(t)$.

Denote
$F^{(0)}(t) \equiv \begin{cases}1 & \text { for } t \geq 0 \\ 0 & \text { for } t<0\end{cases} \quad F^{(n)}(t) \equiv \int_{0}^{t} F^{(n-1)}(t-u) \mathrm{d} F(u) \quad(n=1,2, \cdots)$,
i.e., $F^{(n)}(t)$ represents the distribution of $\sum_{j=1}^{n} X_{j}$. Evidently,

$$
\begin{aligned}
\operatorname{Pr}\{N(t)=n\} & =\operatorname{Pr}\left\{S_{n} \leq t \text { and } S_{n+1}>t\right\} \\
& =F^{(n)}(t)-F^{(n+1)}(t) \quad(n=0,1,2, \cdots)
\end{aligned}
$$

We define the expected number of renewals in $[0, t]$ as $M(t) \equiv E\{N(t)\}$, that is called a renewal function, and $m(t) \equiv \mathrm{d} M(t) / \mathrm{d} t$, that is called a renewal density. From (1.1),

$$
M(t)=\sum_{n=1}^{\infty} n \operatorname{Pr}\{N(t)=n\}=\sum_{n=1}^{\infty} F^{(n)}(t)
$$

It is fairly easy to show that $M(t)$ is finite for all $t \geq 0$ because $\operatorname{Pr}\left\{X_{j}=0\right\}<$ 1. Furthermore, from the notation of convolution,

$$
\begin{aligned}
M(t) & =F(t)+\sum_{n=1}^{\infty} \int_{0}^{t} F^{(n)}(t-u) \mathrm{d} F(u) \\
& =\int_{0}^{t}[1+M(t-u)] \mathrm{d} F(u)
\end{aligned}
$$

that is called a renewal equation. When $F(t)$ has a density function $f(t)$ and $f^{(n)}(t) \equiv \mathrm{d} F^{(n)}(t) / \mathrm{d} t(n=1,2, \ldots), m(t)=\sum_{n=1}^{\infty} f^{(n)}(t)$ and differentiation of (1.3) with respect to $t$ implies

$$
m(t)=f(t)+\int_{0}^{t} m(t-u) f(u) \mathrm{d} u
$$

The renewal-type equation such as (1.3) and (1.4) appears frequently in the analysis of stochastic reliability models because most systems are renewed after maintenance. The Laplace-Stieltjes (LS) transform of $M(t)$ is given by

$$
M^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} M(t)=\frac{F^{*}(s)}{1-F^{*}(s)}
$$where, in general, $\varphi^{*}(s)$ is the LS transform of $\varphi(t)$, i.e., $\varphi^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \varphi(t)$ for $s>0$ and $\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} F^{(n)}(t)=\left[F^{*}(s)\right]^{n}(n=0,1,2, \ldots)$. Thus, $M(t)$ and $F(t)$ determine one another because the LS transform also determines the function uniquely.

The second moment of $N(t)$ is [61, p. 89], because $n^{2}=2 \sum_{i=1}^{n} i-n$,

$$
\begin{aligned}
E\left\{N(t)^{2}\right\} & =\sum_{n=1}^{\infty} n^{2} \operatorname{Pr}\{N(t)=n\} \\
& =2 \sum_{n=1}^{\infty} n \operatorname{Pr}\{N(t) \geq n\}-M(t) \\
& =2 \sum_{n=1}^{\infty} n \operatorname{Pr}\left\{S_{n} \leq t\right\}-M(t) \\
& =2 \sum_{n=1}^{\infty} n F^{(n)}(t)-M(t)
\end{aligned}
$$

Forming the LS transforms on both sides above,

$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} E\left\{N(t)^{2}\right\} & =2 \sum_{n=1}^{\infty} n\left[F^{*}(s)\right]^{n}-M^{*}(s) \\
& =2\left[\frac{F^{*}(s)}{1-F^{*}(s)}\right]^{2}+\frac{F^{*}(s)}{1-F^{*}(s)} \\
& =2\left[M^{*}(s)\right]^{2}+M^{*}(s)
\end{aligned}
$$

Inverting (1.7),

$$
E\left\{N(t)^{2}\right\}=2 M(t) * M(t)+M(t)
$$

and hence,

$$
V\{N(t)\}=2 M(t) * M(t)+M(t)-[M(t)]^{2}
$$

where the asterisk denotes the pairwise Stieltjes convolution, i.e., $a(t) * b(t) \equiv$ $\int_{0}^{t} b(t-u) \mathrm{d} a(u)$.

We summarize some important limiting theorems and results of renewal theory for future reference $[11,60,61]$.

# Theorem 1.1. 

(i)

$$
\frac{M(t)}{t} \longrightarrow \frac{1}{\mu_{1}}, \quad \text { as } t \rightarrow \infty
$$

(ii)

$$
\frac{V\{N(t)\}}{t} \longrightarrow \frac{\sigma^{2}}{\mu_{1}^{3}}, \quad \text { as } t \rightarrow \infty
$$Theorem 1.2. If $\mu_{2} \equiv \int_{0}^{\infty} t^{2} \mathrm{~d} F(t)<\infty$ and $\sigma^{2} \equiv \mu_{2}-\mu_{1}^{2}$,

$$
M(t)=\frac{t}{\mu_{1}}+\left(\frac{\sigma^{2}}{2 \mu_{1}^{2}}-\frac{1}{2}\right)+o(1), \quad \text { as } t \rightarrow \infty
$$

and if $\mu_{3} \equiv \int_{0}^{\infty} t^{3} \mathrm{~d} F(t)<\infty$,

$$
V\{N(t)\}=\frac{\sigma^{2} t}{\mu_{1}^{3}}+\left(\frac{5 \sigma^{4}}{4 \mu_{1}^{4}}+\frac{2 \sigma^{2}}{\mu_{1}^{2}}+\frac{3}{4}-\frac{2 \mu_{3}}{3 \mu_{1}^{3}}\right)+o(1), \quad \text { as } t \rightarrow \infty
$$

where the function $f(h)$ is said to be $o(h)$ if $\lim _{h \rightarrow 0} f(h) / h=0$.
This is proved as follows: Expanding $F^{*}(s)$ with respect to $s$,

$$
F^{*}(s)=1-\mu_{1} s+\frac{1}{2}\left(\sigma^{2}+\mu_{1}^{2}\right) s^{2}-\frac{1}{3!} \mu_{3} s^{3}+o\left(s^{3}\right)
$$

Substituting (1.14) in (1.5) and arranging them,

$$
\begin{aligned}
M^{*}(s) & =\frac{1}{s \mu_{1}}+\left(\frac{\sigma^{2}-\mu_{1}^{2}}{2 \mu_{1}^{2}}\right)+o(1) \\
{\left[M^{*}(s)\right]^{2} } & =\frac{1}{s^{2} \mu_{1}^{2}}+\frac{1}{s}\left(\frac{\sigma^{2}-\mu_{1}^{2}}{\mu_{1}^{3}}\right)+\left(\frac{3 \sigma^{4}}{4 \mu_{1}^{4}}+\frac{\sigma^{2}}{2 \mu_{1}^{2}}+\frac{3}{4}-\frac{\mu_{3}}{3 \mu_{1}^{3}}\right)+o(1)
\end{aligned}
$$

Inverting (1.15), and substituting (1.16) in (1.7) and inverting it, we have the results of Theorem 1.2 from (1.9).

From this theorem, $M(t)$ and $m(t)$ are approximately given by

$$
M(t) \approx \frac{t}{\mu_{1}}+\frac{\sigma^{2}}{2 \mu_{1}^{2}}-\frac{1}{2}, \quad m(t) \approx \frac{1}{\mu_{1}}
$$

and

$$
V\{N(t)\} \approx \frac{\sigma^{2} t}{\mu_{1}^{3}}+\frac{5 \sigma^{4}}{4 \mu_{1}^{4}}+\frac{2 \sigma^{2}}{\mu_{1}^{2}}+\frac{3}{4}-\frac{2 \mu_{3}}{3 \mu_{1}^{3}}
$$

for large $t$. Furthermore, if $\sigma \ll \mu_{1}$, then

$$
M(t) \approx \frac{t}{\mu_{1}}-\frac{1}{2}
$$

When $F(t)$ has a density function $f(t)$, the failure or hazard rate is defined as $h(t) \equiv f(t) / \bar{F}(t)$, where $\bar{F}(t) \equiv 1-F(t)$. If the failure rate $h(t)$ is increasing, then $F$ is IFR, that means increasing failure rate.

Theorem 1.3. When $F$ is IFR [65],

$$
\frac{t}{\mu_{1}}-1 \leq \frac{t}{\int_{0}^{t} \bar{F}(u) \mathrm{d} u}-1 \leq M(t) \leq \frac{t F(t)}{\int_{0}^{t} \bar{F}(u) \mathrm{d} u} \leq \frac{t}{\mu_{1}}
$$Using the asymptotic properties in (1.17) and (1.18) and applying them to the usual central limit theorem, we have the central limit theorem for a renewal process.

Theorem 1.4.

$$
\lim _{t \rightarrow \infty} \operatorname{Pr}\left\{\frac{N(t)-t / \mu_{1}}{\sqrt{\sigma^{2} t / \mu_{1}^{3}}} \leq x\right\}=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u
$$

i.e., $N(t)$ is asymptotically normally distributed with mean $t / \mu_{1}$ and variance $\sigma^{2} t / \mu_{1}^{3}$ for large $t$.

# (2) Poisson Process 

When $F(t)=\operatorname{Pr}\left\{X_{j} \leq t\right\}=1-\mathrm{e}^{-\lambda t}(j=1,2, \cdots)$ for $\lambda>0$, the counting process $\{N(t) ; t \geq 0\}$ is called a Poisson process with rate $\lambda$. In this case,

$$
\begin{gathered}
F^{(n)}(t)=\operatorname{Pr}\left\{S_{n} \leq t\right\}=\sum_{j=n}^{\infty} \frac{(\lambda t)^{j}}{j!} \mathrm{e}^{-\lambda t} \quad(n=0,1,2, \cdots) \\
f^{(n)}(t) \equiv \frac{\mathrm{d} F^{(n)}(t)}{\mathrm{d} t}=\frac{\lambda(\lambda t)^{n-1}}{(n-1)!} \mathrm{e}^{-\lambda t} \quad(n=1,2, \cdots)
\end{gathered}
$$

that is a gamma or Erlang distribution with rate $\lambda$. From (1.1), (1.2), (1.9), and (1.22), we easily have the following results:

$$
\operatorname{Pr}\{N(t)=n\}=\frac{(\lambda t)^{n}}{n!} \mathrm{e}^{-\lambda t} \quad(n=0,1,2, \cdots)
$$

i.e., $N(t)$ is distributed according to a Poisson distribution with rate $\lambda$, and

$$
M(t)=V\{N(t)\}=\frac{t F(t)}{\int_{0}^{t} \bar{F}(u) \mathrm{d} u}=\frac{t \bar{F}(t)}{\int_{t}^{\infty} \bar{F}(u) \mathrm{d} u}=\lambda t
$$

A Poisson process has stationary independent increments. Eliminating the stationarity, we can generalize a Poisson process with a parameter that is a function of time $t$ as follows:

$$
\begin{gathered}
F^{(n)}(t)=\sum_{j=n}^{\infty} \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)} \quad(n=0,1,2, \cdots) \\
\operatorname{Pr}\{N(t+u)-N(u)=n\}=\frac{[H(t+u)-H(u)]^{n}}{n!} \mathrm{e}^{-[H(t+u)-H(u)]} \\
M(t+u)-M(u)=V\{N(t+u)-N(u)\}=H(t+u)-H(u)
\end{gathered}
$$for all $u \geq 0$. The counting process $\{N(t), t \geq 0\}$ is called a nonhomogeneous Poisson process with a mean value function $H(t)$ and $h(t) \equiv \mathrm{d} H(t) / \mathrm{d} t$ is called an intensity function. In addition, from [1, p. 97, 66],

$$
E\left\{X_{n}\right\}=\int_{0}^{\infty} \frac{[H(t)]^{n-1}}{(n-1)!} \mathrm{e}^{-H(t)} \mathrm{d} t \quad(n=1,2, \cdots)
$$

and if $h(t)$ is increasing, then $E\left\{X_{n}\right\}$ is decreasing in $n$ to $1 / h(\infty)$.
Next, suppose that $\left\{W_{j}\right\}$ are independent and identically distributed random variables associated with $X_{j}$, and $W_{j}$ has an identical distribution $G(x)$ with finite mean $E\{W\}$ and is independent of $X_{i}(i \neq j)$, where $W_{0} \equiv 0$. When $\{N(t) ; t \geq 0\}$ is a Poisson process, we consider a new random variable at time $t$ defined by

$$
Z(t) \equiv \sum_{j=0}^{N(t)} W_{j} \quad(N(t)=0,1,2, \cdots)
$$

Then, the stochastic process $\{Z(t), t \geq 0\}$ under two processes is called a compound Poisson process $[60,63,67]$. In addition, the LS transform of the distribution of $W_{j}$ is denoted by $G^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s x} \mathrm{~d} \operatorname{Pr}\left\{W_{j} \leq x\right\}=\int_{0}^{\infty} e^{-s x} d G(x)$ for $s>0$. Then, because

$$
\begin{aligned}
\operatorname{Pr}\{Z(t) \leq x\} & =\sum_{n=0}^{\infty} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{n} \leq x \mid N(t)=n\right\} \operatorname{Pr}\{N(t)=n\} \\
& =\sum_{n=0}^{\infty} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{n} \leq x\right\} \frac{(\lambda t)^{n}}{n!} \mathrm{e}^{-\lambda t}
\end{aligned}
$$

its LS transform is

$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-s x} \mathrm{~d} \operatorname{Pr}\{Z(t) \leq x\} & =\sum_{n=0}^{\infty}\left[G^{*}(s)\right]^{n} \frac{(\lambda t)^{n}}{n!} \mathrm{e}^{-\lambda t} \\
& =\exp \left\{-\lambda t\left[1-G^{*}(s)\right]\right\}
\end{aligned}
$$

Thus, it easily follows that

$$
\begin{aligned}
E\{Z(t)\} & =\lambda t E\{W\} \\
V\{Z(t)\} & =\lambda t E\left\{W^{2}\right\}
\end{aligned}
$$

The stochastic process $\{Z(t) ; t \geq 0\}$ for $\{N(t) ; t \geq 0\}$ is called a cumulative process [11] and some interesting results will be derived in Chapter 2.

# (3) Renewal Reward Process 

The stochastic process $\{Z(t), t \geq 0\}$, defined in (1.30) when $\{N(t), t \geq 0\}$ is a renewal process, is also called a renewal reward process [60]. Using Theorem 1.1,$$
\lim _{t \rightarrow \infty} \frac{E\{Z(t)\}}{t}=\frac{E\{W\}}{E\{X\}}
$$

where $E\{W\} \equiv E\left\{W_{j}\right\}<\infty$ and $E\{X\} \equiv E\left\{X_{j}\right\}<\infty$ for all $j \geq 1$. This property is applied to the analysis of optimum policies for many maintenance models in reliability theory over an infinite time span [1].

# 1.2 Shock Processes 

Consider a unit subject to damage, wear, and fatigue produced by a series of shocks, jolts, blows, or stresses. When shocks occur in a Poisson process, a renewal process, or in more general stochastic processes, and more simply, at a constant time, the stochastic process $\{Z(t)\}$ defined in (1.30) represents the total cumulative damage at time $t$.

When shocks occur in a Poisson process, the times between successive shocks are distributed exponentially and has a memoryless property. In other words, shocks are generated randomly and uniformly in time, and the time from any time $t$ to the next shock is independent of time $t$ and has the same exponential distribution as that from time 0 . If the unit fails when the total number of shocks has exceeded a specified number $n$, then the failure time has a gamma distribution given in (1.23).

When shocks occur in a nonhomogeneous Poisson process with an intensity function $h(t)$, the probability that some shock occurs in a small interval $(t, t+$ $\mathrm{d} t]$ is given approximately by $h(t) \mathrm{d} t$ for any $t \geq 0$. This corresponds to the shock model in which the mean times between shocks decrease with time. For example, consider a two-unit system with failure interaction as described in Section 4.2, in which unit 1 suffers some damage due to the failure of unit 2. If unit 2 undergoes only minimal repair at failures [1, pp. 95-116], then the failure times of unit 2 , i.e., shock times of unit 1 , are generated according to a nonhomogeneous Poisson process.

Finally, shocks occur in a renewal process, i.e., the sequence of times $\left\{X_{j}\right\}$ between shocks is independent and identically distributed with a general distribution $F(t)$. However, the time $\gamma(t)$ from time $t$ to the next shock, that is called the excess time in a stochastic process or residual lifetime in reliability theory at time $t[61,65]$, depends on $t$, and is given by a renewal-type equation

$$
\begin{gathered}
\operatorname{Pr}\{\gamma(t) \leq x\}=F(t+x)-\int_{0}^{t}[1-F(t+x-u)] \mathrm{d} M(u) \\
\lim _{t \rightarrow \infty} \operatorname{Pr}\{\gamma(t) \leq x\}=\frac{1}{E\{X\}} \int_{0}^{x}[1-F(u)] \mathrm{d} u
\end{gathered}
$$

where $E\{X\} \equiv E\left\{X_{j}\right\}$ and $M(t)$ is given in (1.2). This corresponds to the shock model in which a shock will be generated by depending only on the lapse time from the previous shock, regardless of the lapse time of the previous shock.Furthermore, shocks have been assumed to occur in more generalized stochastic processes such as the birth process [68,69], the Lévy process [70,71], and the general counting process $[72,73]$. Such studies have given many interesting results theoretically in reliability theory. However, these would not be useful practically for actual reliability models because the contents are too mathematical.

Example 1.1. Suppose that a unit suffers some damage due to each shock with probability $p(0<p \leq 1)$ and no damage with probability $q \equiv 1-p$. We can interpret another example that is the damage of a target hit by a weapon. The probability of hitting a target when a weapon fires at a passive target is $p$ and the probability of missing a target is $q$. This is called a stochastic duel $[74,75]$ and will be dealt with Section 10 as one of related cumulative damage models.

When shocks occur in a renewal process, the distribution of time where the unit suffers some damage for the first time until time $t$ is

$$
F_{1}(t) \equiv[1+q F(t)+q F(t) * q F(t)+\cdots] * p F(t)
$$

Taking the LS transforms on both sides yields

$$
F_{1}^{*}(s)=\frac{p F^{*}(s)}{1-q F^{*}(s)}
$$

and hence, the mean time to the first damage due to some shock is

$$
\int_{0}^{\infty} t \mathrm{~d} F_{1}(t)=\frac{E\{X\}}{p}
$$

Thus, by replacing $F(t)$ with $F_{1}(t)$ in (1), we can get the results in the case where shocks are imperfect. In particular, when $F(t)=1-\mathrm{e}^{-\lambda t}, F_{1}(t)=$ $1-\mathrm{e}^{-p \lambda t}, \int_{0}^{\infty} t \mathrm{~d} F_{1}(t)=1 /(p \lambda)$, and

$$
\operatorname{Pr}\{N(t)=n\}=\frac{(p \lambda t)^{n}}{n!} \mathrm{e}^{-p \lambda t} \quad(n=0,1,2, \cdots)
$$

Similarly, when shocks occur in a nonhomogeneous Poisson process with a mean value function $H(t)$,

$$
\operatorname{Pr}\{N(t)=n\}=\frac{[p H(t)]^{n}}{n!} \mathrm{e}^{-p H(t)} \quad(n=0,1,2, \cdots)
$$

and $E\{N(t)\}=V\{N(t)\}=p H(t)$.
Example 1.2. Consider a parallel redundant system with $n$ identical units, each of which fails at shocks with probability $p(0<p \leq 1)$, where $q \equiv 1-p$, and shocks occur in a renewal process with mean interval $\mu_{1}$. Let $W_{j}$ be the total number of units that fail at the $j$ th $(j=1,2, \cdots)$ shock. Then, because the probability that one unit fails until the $j$ th shock is$$
\sum_{i=1}^{j} p q^{i-1}=1-q^{j}
$$

the mean time to system failure is $[76]$

$$
\begin{aligned}
& \sum_{j=1}^{\infty} j \mu_{1} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1} \leq n-1 \text { and } W_{1}+W_{2}+\cdots+W_{j}=n\right\} \\
& =\sum_{j=1}^{\infty} j \mu_{1}\left[\left(1-q^{j}\right)^{n}-\left(1-q^{j-1}\right)^{n}\right] \\
& =\mu_{1} \sum_{j=0}^{\infty}\left[1-\left(1-q^{j}\right)^{n}\right] \\
& =\mu_{1} \sum_{i=1}^{n}\binom{n}{i}(-1)^{i+1} \frac{1}{1-q^{i}}
\end{aligned}
$$

that is strictly increasing in $q$ from $\mu_{1}$ to $\infty$. The replacement problem of this model will be taken up in Section 4.1.1.

More general redundant systems with common-cause failures in which one or more units fail simultaneously at shocks were analyzed [77-80].# Damage Models 

Consider a standard cumulative damage model [11] for an operating unit: A unit is subjected to shocks and suffers some damage due to shocks. Let random variables $X_{j}(j=1,2, \ldots)$ denote a sequence of interarrival times between successive shocks, and random variables $W_{j}(j=1,2, \ldots)$ denote the damage produced by the $j$ th shock, where $W_{0} \equiv 0$. It is assumed that the sequence of $\left\{W_{j}\right\}$ is nonnegative, independently, and identically distributed, and furthermore, $W_{j}$ is independent of $X_{i}(i \neq j)$. This is called a jump process [81] or doubly stochastic process [82].

Let $N(t)$ denote the random variable that is the total number of shocks up to time $t(t \geq 0)$. Then, define a random variable

$$
Z(t) \equiv \sum_{j=0}^{N(t)} W_{j} \quad(N(t)=0,1,2, \ldots)
$$

where $Z(t)$ represents the total damage at time $t$. It is assumed that the unit fails when the total damage has exceeded a prespecified level $K(0<$ $K<\infty)$ for the first time (see Figure 2.1). Usually, a failure level $K$ is statistically estimated and is already known. Of interest is a random variable $Y \equiv \min \{t ; Z(t)>K\}$, i.e., $\operatorname{Pr}\{Y \leq t\}$ represents the distribution of the failure time of the unit.

In this chapter, we consider two damage models: (1) the cumulative damage model where the total damage is additive, and (2) the independent damage model where the total damage is not additive, i.e., it is independent of the previous damage level. For each model, we are interested in the following reliability quantities:
(i) $\operatorname{Pr}\{Z(t) \leq x\}$; the distribution of the total damage at time $t$.
(ii) $E\{Z(t)\}$; the total expected damage at time $t$.
(iii) $\operatorname{Pr}\{Y \leq t\}$; the first-passage time distribution to failure.
(iv) $E\{Y\}$; the mean time to failure (MTTF).

Fig. 2.1. Process for a standard cumulative damage model
(v) Failure rate or hazard rate $r(t) ; r(t) \mathrm{d} t=\operatorname{Pr}\{t<Y \leq t+\mathrm{d} t \mid Y>t\}$ is the probability that the unit surviving at time $t$ will fail in $(t, t+\mathrm{d} t]$.
(vi) Probability function $p_{j} ; p_{j}$ is the probability that the unit fails at the $j$ th shock.

Some reliability quantities have already been obtained $[11,33,40]$. This chapter summarizes only the known results that can be applied to maintenance policies discussed in later chapters and be useful in practical fields. A continuous wear process in which the total damage increases with time $t$ is briefly introduced. Finally, five modified damage models are proposed. Several examples are presented. Some examples might appear to be theoretical and contrived, however, these would be useful for understanding the results easily.

# 2.1 Cumulative Damage Model 

Consider a standard cumulative damage model: Successive shocks occur at time intervals $X_{j}(j=1,2, \ldots)$ and each shock causes some damage to a unit in the amount $W_{j}$. The total damage due to shocks is additive.

It is assumed that $1 / \lambda \equiv E\left\{X_{j}\right\}<\infty, 1 / \mu \equiv E\left\{W_{j}\right\}<\infty$, and $F(t) \equiv$ $\operatorname{Pr}\left\{X_{j} \leq t\right\}, G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$ for $t, x \geq 0$. Then, from (1.1) in Chapter 1, the probability that shocks occur exactly $j$ times in $[0, t]$ is [11]$$
\operatorname{Pr}\{N(t)=j\}=F^{(j)}(t)-F^{(j+1)}(t) \quad(j=0,1,2, \ldots)
$$

Thus,

$$
\begin{gathered}
\operatorname{Pr}\left\{\sum_{i=0}^{N(t)} W_{i} \leq x, N(t)=j\right\}=\operatorname{Pr}\left\{\sum_{i=0}^{N(t)} W_{i} \leq x \mid N(t)=j\right\} \operatorname{Pr}\{N(t)=j\} \\
=G^{(j)}(x)\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \quad(j=0,1,2, \ldots)
\end{gathered}
$$

where $\varphi^{(j)}(t)$ denotes the $j$-fold Stieltjes convolution of any function $\varphi(t)$ with itself, and $\varphi^{(0)}(t) \equiv 1$ for $t \geq 0$.

Therefore, the distribution of $Z(t)$ defined in (2.1) is

$$
\begin{aligned}
\operatorname{Pr}\{Z(t) \leq x\} & =\operatorname{Pr}\left\{\sum_{i=0}^{N(t)} W_{i} \leq x\right\} \\
& =\sum_{j=0}^{\infty} \operatorname{Pr}\left\{\sum_{i=0}^{N(t)} W_{i} \leq x \mid N(t)=j\right\} \operatorname{Pr}\{N(t)=j\} \\
& =\sum_{j=0}^{\infty} G^{(j)}(x)\left[F^{(j)}(t)-F^{(j+1)}(t)\right]
\end{aligned}
$$

and the survival probability is

$$
\operatorname{Pr}\{Z(t)>x\}=\sum_{j=0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] F^{(j+1)}(t)
$$

The total expected damage at time $t$ is

$$
\begin{aligned}
E\{Z(t)\} & =\int_{0}^{\infty} x \mathrm{~d} \operatorname{Pr}\{Z(t) \leq x\} \\
& =\frac{1}{\mu} \sum_{j=1}^{\infty} F^{(j)}(t)=\frac{M_{F}(t)}{\mu}
\end{aligned}
$$

where $M_{F}(t) \equiv \sum_{j=1}^{\infty} F^{(j)}(t)$ is called a renewal function of distribution $F(t)$ and represents the expected number of shocks in $[0, t]$. It can be intuitively known that $E\{Z(t)\}$ is given by the product of the average amount of damage suffered from shocks and the expected number of shocks in time $t$. This is useful for estimating the total expected damage at time $t$.

Furthermore, from Theorem 1.2, for the distribution $F$ with finite $r$ th moment $\mu_{r}$ and variance $\sigma^{2}$,

$$
\begin{aligned}
M(t) & \equiv E\{N(t)\}=\frac{t}{\mu_{1}}+\left(\frac{\sigma^{2}}{2 \mu_{1}^{2}}-\frac{1}{2}\right)+o(1) \\
V\{N(t)\} & =\frac{\sigma^{2} t}{\mu_{1}^{3}}+\left(\frac{5 \sigma^{4}}{4 \mu_{1}^{4}}+\frac{2 \sigma^{2}}{\mu_{1}^{2}}+\frac{3}{4}-\frac{2 \mu_{3}}{3 \mu_{1}^{3}}\right)+o(1)
\end{aligned}
$$Thus, when $F(G)$ has finite mean $1 / \lambda(1 / \mu)$ and variance $\sigma_{F}^{2}\left(\sigma_{G}^{2}\right)$, approximately, for large $t$,

$$
\begin{aligned}
E\{Z(t)\} & =E\left\{E\left\{\left.\sum_{j=1}^{N(t)} W_{j} \right\rvert\, N(t)\right\}\right\}=E\{N(t)\} E\left\{W_{j}\right\} \\
& \approx \frac{1}{\mu}\left(\lambda t+\frac{\lambda^{2} \sigma_{F}^{2}-1}{2}\right) \\
V\{Z(t)\} & =E\left\{Z^{2}(t)\right\}-[E\{Z(t)\}]^{2} \\
& =E\left\{\left.\left\{\sum_{j=1}^{N(t)} W_{j} \sum_{i=1}^{N(t)} W_{i} \right\rvert\, N(t)\right\}\right\}-[E\{Z(t)\}]^{2} \\
& =V\{N(t)\}\left[E\left\{W_{j}\right\}\right]^{2}+E\{N(t)\} V\left\{W_{j}\right\} \\
& \approx \frac{1}{\mu}\left[\frac{\lambda t}{\mu}\left(\lambda^{2} \sigma_{F}^{2}+\mu^{2} \sigma_{G}^{2}\right)+\frac{1}{\mu}\left(\frac{5 \lambda^{4} \sigma_{F}^{4}}{4}+2 \lambda^{2} \sigma_{F}^{2}+\frac{3}{4}-\frac{2 \lambda^{3} \mu_{3}}{3}\right)\right] \\
& +\frac{\sigma_{G}^{2}}{2}\left(\lambda^{2} \sigma_{F}^{2}-1\right)
\end{aligned}
$$

Moreover, because

$$
\lim _{t \rightarrow \infty} \frac{E\{Z(t)\}}{t}=\frac{\lambda}{\mu}, \quad \lim _{t \rightarrow \infty} \frac{V\{Z(t)\}}{t}=\frac{\lambda}{\mu^{2}}\left(\lambda^{2} \sigma_{F}^{2}+\mu^{2} \sigma_{G}^{2}\right)
$$

by applying Takács theorem [83] (see Example 2.6 in [1]) to this model,

$$
\lim _{t \rightarrow \infty} \operatorname{Pr}\left\{\frac{Z(t)-\lambda t / \mu}{\sqrt{\lambda^{3} t\left(\sigma_{F}^{2} / \mu^{2}+\sigma_{G}^{2} / \lambda^{2}\right)}} \leq x\right\}=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u
$$

This was proved in [29] and generalized in [84-86].
Example 2.1. We wish to estimate the total damage when the probability that it is more than $z$ in $t=30$ days of operation is given by 0.90 . The distributions of shock times and the amount of damage are unknown, but from sample data, the following estimations of means and variances are made:

$$
\begin{array}{ll}
1 / \lambda=2 \text { days }, & \sigma_{F}^{2}=5(\text { days })^{2} \\
1 / \mu=1, & \sigma_{G}^{2}=0.5
\end{array}
$$

In this case, from $(2.6), E\{Z(30)\} \approx 15.125$. Then, from (2.8), when $t=30$,

$$
\frac{Z(t)-\lambda t / \mu}{\sqrt{\lambda^{3} t\left(\sigma_{F}^{2} / \mu^{2}+\sigma_{G}^{2} / \lambda^{2}\right)}}=\frac{Z(30)-15}{5.12}
$$

is approximately normally distributed with mean 0 and variance 1 . Hence,$$
\begin{aligned}
\operatorname{Pr}\{Z(t)>z\} & =\operatorname{Pr}\left\{\frac{Z(30)-15}{5.12}>\frac{z-15}{5.12}\right\} \\
& \approx \frac{1}{\sqrt{2 \pi}} \int_{(z-15) / 5.12}^{\infty} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u=0.90
\end{aligned}
$$

Because $u_{0}=-1.28$ such that $\left(1 / \sqrt{2 \pi}\right) \int_{u_{0}}^{\infty} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u=0.90, z=15-5.12 \times$ $1.28 \approx 8.45$. Thus, the total damage is more than 8.45 in 30 days with probability 0.90 .

Next, when a failure level is known as $K=10$,

$$
\begin{aligned}
\operatorname{Pr}\{Z(t)>10\} & =\operatorname{Pr}\left\{\frac{Z(30)-10}{5.12}>\frac{10-15}{5.12}\right\} \\
& \approx \frac{1}{\sqrt{2 \pi}} \int_{-0.98}^{\infty} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u \approx 0.84
\end{aligned}
$$

Thus, the probability that the unit with a failure level $K=10$ fails in 30 days is about 0.84 .

The first-passage time distribution to failure when the failure level is constant $K$, because the events of $\{Y \leq t\}$ and $\{Z(t)>K\}$ are equivalent, is, from $(2.4)$,

$$
\begin{aligned}
\Phi(t) & \equiv \operatorname{Pr}\{Y \leq t\}=\operatorname{Pr}\{Z(t)>K\} \\
& =\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] F^{(j+1)}(t)
\end{aligned}
$$

and its Laplace-Stieltjes (LS) transform is

$$
\Phi^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \Phi(t)=\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right]\left[F^{*}(s)\right]^{j+1}
$$

where $\varphi^{*}(s)$ denotes the LS transform of any function $\varphi(t)$, i.e., $\varphi^{*}(s) \equiv$ $\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \varphi(t)$ for $s>0$. Thus, the mean time to failure is

$$
\begin{aligned}
E\{Y\} & =\int_{0}^{\infty} t \mathrm{dPr}\{Y \leq t\}=-\left.\frac{\mathrm{d} \Phi^{*}(s)}{\mathrm{d} s}\right|_{s=0} \\
& =\frac{1}{\lambda} \sum_{j=0}^{\infty} G^{(j)}(K)=\frac{1}{\lambda}\left[1+M_{G}(K)\right]
\end{aligned}
$$

where $M_{G}(K) \equiv \sum_{j=1}^{\infty} G^{(j)}(K)$ represents the expected number of shocks before the total damage exceeds a failure level $K$.

Similarly, when $G$ has finite mean $1 / \mu$ and variance $\sigma_{G}^{2}$, approximately,

$$
E\{Y\} \approx \frac{1}{\lambda}\left(\mu K+\frac{\mu^{2} \sigma_{G}^{2}+1}{2}\right)
$$In addition, when the distribution $G$ has an IFR property, it has been shown that $\mu x-1<M_{G}(x) \leq \mu x$ from (1.20). Thus,

$$
\frac{\mu K}{\lambda}<E\{Y\} \leq \frac{\mu K+1}{\lambda}
$$

In Example 2.1, $E\{Y\}$ is approximately 21.5 days and $20<E\{Y\} \leq 22$.
Finally, the failure rate is

$$
\begin{aligned}
r(t) \mathrm{d} t & =\frac{\operatorname{Pr}\{t<Y \leq t+\mathrm{d} t\}}{\operatorname{Pr}\{Y>t\}} \\
& =\frac{\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] f^{(j+1)}(t) \mathrm{d} t}{\sum_{j=0}^{\infty} G^{(j)}(K)\left[F^{(j)}(t)-F^{(j+1)}(t)\right]}
\end{aligned}
$$

where $f(t)$ is a density function of $F(t)$. Furthermore, because the probability that the unit fails at the $(j+1)$ th shock is $p_{j+1} \equiv G^{(j)}(K)-G^{(j+1)}(K)$ $(j=0,1,2, \ldots)$, its survival distribution is

$$
\bar{P}_{j} \equiv \sum_{i=j}^{\infty} p_{i+1}=G^{(j)}(K) \quad(j=0,1,2, \ldots)
$$

where $\bar{P}_{0} \equiv 1$, i.e., $\bar{P}_{j}$ represents the probability of surviving the first $j$ shocks. Thus, the expected number of shocks until failure, including the shock at which the unit has failed, is

$$
\sum_{j=1}^{\infty} j p_{j}=\sum_{j=0}^{\infty} G^{(j)}(K)=1+M_{G}(K)
$$

$E\{Y\}$ in (2.11) is given by the product of the mean time between successive shocks and the expected number of shocks until the total damage has exceeded $K$. It is also approximately

$$
\sum_{j=1}^{\infty} j p_{j} \approx \mu K+\frac{\mu^{2} \sigma_{G}^{2}+1}{2}
$$

The discrete failure rate for a probability function $\left\{p_{j}\right\}_{j=1}^{\infty}$ is

$$
r_{j+1} \equiv \frac{p_{j+1}}{\bar{P}_{j}}=\frac{G^{(j)}(K)-G^{(j+1)}(K)}{G^{(j)}(K)} \quad(j=0,1,2, \ldots)
$$

i.e., $r_{j+1}$ represents the probability that the unit surviving at the $j$ th shock will fail at the $(j+1)$ th shock and is less than or equal to 1 .

Next, suppose that shocks occur in a nonhomogeneous Poisson process with an intensity function $h(t)$ and a mean value function $H(t)$, i.e., $H(t) \equiv$ $\int_{0}^{t} h(u) \mathrm{d} u$ in (2) of Section 1.1. Then, from (1.1) and (1.26),$$
\operatorname{Pr}\{N(t)=j\}=\frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)} \quad(j=0,1,2, \ldots)
$$

Thus, by replacing $F^{(j)}(t)$ with $\sum_{i=j}^{\infty}\left\{[H(t)]^{i} / i!\right\} \mathrm{e}^{-H(t)}$ formally, we can rewrite all reliability quantities. For example,

$$
\begin{aligned}
\operatorname{Pr}\{Z(t) \leq x\} & =\sum_{j=0}^{\infty} G^{(j)}(x) \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)} \\
E\{Z(t)\} & =\frac{H(t)}{\mu} \\
E\{Y\} & =\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)} \mathrm{d} t
\end{aligned}
$$

If shocks occur at a constant time $t_{0}\left(0<t_{0}<\infty\right)$, i.e., $F(t)$ is the degenerate distribution placing unit mass at time $t_{0}$, and $F(t) \equiv 0$ for $t<t_{0}$, and 1 for $t \geq t_{0}$, then

$$
\begin{aligned}
\operatorname{Pr}\{Y \leq t\} & =1-G^{\left(\left[t / t_{0}\right]\right)}(K) \\
E\{Y\} & =\int_{0}^{\infty} G^{\left(\left[t / t_{0}\right]\right)}(K) \mathrm{d} t
\end{aligned}
$$

where $\left[t / t_{0}\right]$ denotes the greatest integer less than or equal to $t / t_{0}$.
Finally, when $G(x) \equiv 0$ for $x<1$ and 1 for $x \geq 1$, and $K=n$,

$$
\operatorname{Pr}\{Y \leq t\}=F^{(n+1)}(t), \quad E\{Y\}=\frac{n+1}{\lambda}
$$

that is, the unit fails certainly at the $(n+1)$ th shock.

# 2.2 Independent Damage Model 

Consider the independent damage model for an operating unit where the total damage is not additive, i.e., any shock does no damage unless its amount has not exceeded a failure level $K$. If the damage due to some shock has exceeded for the first time a failure level $K$, then the unit fails (see Figure 2.2). The same assumptions as those of the previous model are made except that the total damage is additive. A typical example of this model is the fracture of brittle materials such as glasses [33], and semiconductor parts that have failed by some overcurrent or fault voltage. The generalized model with three types of shocks where shocks with a small level of damage are no damage to the unit, shocks with a large level of damage result in failure, and shocks with an intermediate level result in failure only with some probability, was considered [87].

Fig. 2.2. Process for an independent damage model

In this case, the probability that the unit fails exactly at the $(j+1)$ th shock $(j=0,1,2, \ldots)$ is $p_{j+1}=[G(K)]^{j}-[G(K)]^{j+1}$. Thus, the distribution of time to failure is

$$
\operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty}\left\{[G(K)]^{j}-[G(K)]^{j+1}\right\} F^{(j+1)}(t)
$$

its LS transform is

$$
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \operatorname{Pr}\{Y \leq t\}=\frac{[1-G(K)] F^{*}(s)}{1-G(K) F^{*}(s)}
$$

and the mean time to failure is

$$
E\{Y\}=\frac{1}{\lambda[1-G(K)]}
$$

Furthermore, the failure rates are

$$
\begin{aligned}
r(t) & =\frac{\sum_{j=0}^{\infty}\left\{[G(K)]^{j}-[G(K)]^{j+1}\right\} f^{(j+1)}(t)}{\sum_{j=0}^{\infty}[G(K)]^{j}\left[F^{(j)}(t)-F^{(j+1)}(t)\right]} \\
r_{j+1} & =p_{1}=1-G(K) \quad(j=0,1,2, \ldots)
\end{aligned}
$$

that is constant for any $j$.
If shocks occur in a nonhomogeneous Poisson process with a mean value function $H(t)$, then,

$$
\operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty}\left\{1-[G(K)]^{j}\right\} \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)}=1-\mathrm{e}^{-[1-G(K)] H(t)}
$$

and its mean time is$$
E\{Y\}=\int_{0}^{\infty} \mathrm{e}^{-[1-G(K)] H(t)} \mathrm{d} t
$$

The failure rate is

$$
r(t)=[1-G(K)] h(t)
$$

that has the same property as that of an intensity function $h(t)$.
If shocks occur at a constant time $t_{0}$,

$$
\begin{aligned}
\operatorname{Pr}\{Y \leq t\} & =1-[G(K)]^{\left[t / t_{0}\right]} \\
E\{Y\} & =\int_{0}^{\infty}[G(K)]^{\left[t / t_{0}\right]} \mathrm{d} t
\end{aligned}
$$

Example 2.2. Suppose that $F(t)=1-\mathrm{e}^{-\lambda t}$ and $G(x)=1-\mathrm{e}^{-\mu x}$, i.e., shocks occur in a Poisson process with rate $\lambda$ and each damage due to shocks is exponential with mean $1 / \mu$. In this case, both a nonhomogeneous Poisson and renewal processes form the same Poisson process, i.e.,

$$
F^{(j)}(t)=\sum_{i=j}^{\infty} \frac{[H(t)]^{i}}{i!} \mathrm{e}^{-H(t)}=\sum_{i=j}^{\infty} \frac{(\lambda t)^{i}}{i!} \mathrm{e}^{-\lambda t} \quad(j=0,1,2, \ldots)
$$

In the cumulative damage model of Section 2.1, from (1.31),

$$
\int_{0}^{\infty} \mathrm{e}^{-s x} \mathrm{~d} \operatorname{Pr}\{Z(t) \leq x\}=\mathrm{e}^{-\lambda[s /(s+\mu) t]}
$$

By inversion [65, p. 80],

$$
\operatorname{Pr}\{Z(t) \leq x\}=\mathrm{e}^{-\lambda t}\left[1+\sqrt{\lambda \mu t} \int_{0}^{x} \mathrm{e}^{-\mu u} u^{-1 / 2} I_{1}(2 \sqrt{\lambda \mu t u}) \mathrm{d} u\right]
$$

where $I_{i}(x)$ is the Bessel function of order $i$ for the imaginary argument defined by

$$
I_{i}(x) \equiv \sum_{j=0}^{\infty}\left(\frac{x}{2}\right)^{2 j+i} \frac{1}{j!(j+i)!}
$$

Thus, from (2.9), the distribution of time to failure is

$$
\operatorname{Pr}\{Y \leq t\}=1-\mathrm{e}^{-\lambda t}\left[1+\sqrt{\lambda \mu t} \int_{0}^{K} e^{-\mu u} u^{-1 / 2} I_{1}(2 \sqrt{\lambda \mu t u}) \mathrm{d} u\right]
$$

Furthermore, from (2.5), (2.11), or (2.18), (2.19), and (2.7),

$$
\begin{aligned}
E\{Z(t)\} & =\frac{\lambda t}{\mu}, \quad V\{Z(t)\}=\frac{2 \lambda t}{\mu^{2}} \\
E\{Y\} & =\frac{1}{\lambda} \sum_{j=1}^{\infty} j p_{j}=\frac{\mu K+1}{\lambda}
\end{aligned}
$$where note that $E\{Z(t)\}$ increases linearly with time $t$. Thus, we have the interesting result

$$
\frac{E\{Z(t)\}}{K+1 / \mu}=\frac{t}{E\{Y\}}
$$

that represents that the ratio of the total expected damage at time $t$ to a failure level plus one mean amount of damage is equal to that of the time $t$ to the mean time to failure. If the mean time between shock times and their mean damage due to shocks are roughly estimated, the mean damage level and the mean time to failure are also estimated easily from these relations.

The failure rates are, from (2.14) and (2.15), respectively,

$$
\begin{aligned}
r(t) & =\frac{\lambda \mathrm{e}^{-\lambda t-\mu K} I_{0}(2 \sqrt{\lambda \mu t K})}{1+\sqrt{\lambda \mu t} \int_{0}^{K} \mathrm{e}^{-\mu u} u^{-1 / 2} I_{1}(2 \sqrt{\lambda \mu t u}) \mathrm{d} u} \\
r_{j+1} & =\frac{(\mu K)^{j} / j!}{\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right]} \quad(j=0,1,2, \ldots)
\end{aligned}
$$

that is strictly increasing in $j$ from $\mathrm{e}^{-\mu K}$ to 1 , because

$$
\begin{aligned}
r_{j+1}-r_{j} & =\frac{(\mu K)^{j} / j!}{\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right]}-\frac{(\mu K)^{j-1} /(j-1)!}{\sum_{i=j-1}^{\infty}\left[(\mu K)^{i} / i!\right]} \\
& =\frac{\sum_{i=j}^{\infty}\left[(\mu K)^{i+j-1} /(i!j!)\right](i-j)}{\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right] \sum_{i=j-1}^{\infty}\left[(\mu K)^{i} / i!\right]}>0
\end{aligned}
$$

In the independent damage model of Section 2.2, from (2.20) or (2.25),

$$
\operatorname{Pr}\{Y \leq t\}=1-\exp \left(-\lambda t \mathrm{e}^{-\mu K}\right)
$$

and from (2.22) or (2.26),

$$
E\{Y\}=\frac{1}{r(t)}=\frac{1}{\lambda} \mathrm{e}^{\mu K}
$$

that is, the first-passage time $Y$ to failure has an exponential distribution with mean $\mathrm{e}^{\mu K} / \lambda$ and the failure rate is constant.

# 2.3 Failure Rate 

Investigate the reliability properties of the survival distribution $\bar{\Phi}(t) \equiv 1-$ $\Phi(t)=\operatorname{Pr}\{Y>t\}$ that the unit does not fail in $[0, t]$. Let $\bar{P}_{j}$ denote the probability of surviving the first $j$ shocks $(j=0,1,2, \ldots)$, where $P_{0} \equiv 0$, and $F_{j}(t)$ be the probability that $j$ shocks occur in time $t$, where $F_{0}(t) \equiv 1$. Then, the survival distribution is written in the following general form:$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} \bar{P}_{j} \operatorname{Pr}\{N(t)=j\}=\sum_{j=0}^{\infty} \bar{P}_{j}\left[F_{j}(t)-F_{j+1}(t)\right]
$$

In particular, when shocks occur in a Poisson process with rate $\lambda>0$, i.e., $F(t)=1-\mathrm{e}^{-\lambda t}$ in Section 2.1,

$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} \bar{P}_{j} \frac{(\lambda t)^{j}}{j!} \mathrm{e}^{-\lambda t}
$$

The probabilistic properties of $\bar{\Phi}(t)$ were extensively investigated [34, 88]. We refer briefly only to these results that will be needed in the following chapters: The failure rate is, from (2.14),

$$
r(t)=\lambda\left\{1-\frac{\sum_{j=0}^{\infty} \bar{P}_{j+1}\left[(\lambda t)^{j} / j!\right]}{\sum_{j=0}^{\infty} \bar{P}_{j}\left[(\lambda t)^{j} / j!\right]}\right\} \leq \lambda
$$

When $\bar{P}_{j}=q^{j}$, i.e., the total damage is not additive in Section 2.2, $\bar{\Phi}(t)=$ $\mathrm{e}^{-\lambda(1-q) t}$ and $r(t)=\lambda(1-q)$ is constant.

Any distribution $F(t)$ is said to have the property of IFR (increasing failure rate) or IHR (increasing hazard rate) if and only if $[F(t+x)-F(t)] / \bar{F}(t)$ is increasing in $t$ for $x>0$ and $F(t)<1$ [65], where $\bar{F}(t) \equiv 1-F(t)$. Furthermore, it has been proved that $F(t)$ is IFR if and only if $r(t) \equiv f(t) / \bar{F}(t)$ is increasing in $t$. In this model, the following properties (i) and (ii) were proved [33]:
(i) The failure rate $r(t)$ in (2.30) is increasing if $\left(\bar{P}_{j}-\bar{P}_{j+1}\right) / \bar{P}_{j}$ is increasing in $j$.

In addition, when the total damage is additive and shocks times are exponential, from (2.29),

$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} G^{(j)}(K) \frac{(\lambda t)^{j}}{j!} \mathrm{e}^{-\lambda t}
$$

(ii) The failure rate average $\int_{0}^{t} r(u) \mathrm{d} u / t$ is increasing in $t$ because $\left[G^{(j)}(x)\right]^{1 / j}$ is decreasing in $j$. Note that if $r(t)$ is increasing, then $\int_{0}^{t} r(u) \mathrm{d} u / t$ is also increasing.

In particular, when $\bar{P}_{j}=G^{(j)}(K)=\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right] \mathrm{e}^{-\mu K}, \bar{P}_{j+1} / \bar{P}_{j}$ is strictly decreasing from Example 2.2, so that the failure rate $r(t)$ in (2.30) is strictly increasing from $\lambda \mathrm{e}^{-\mu K}$ to $\lambda$.

When shocks occur in a nonhomogeneous Poisson process with an intensity function $h(t)$ and a mean value function $H(t)$ [89], from (2.28),

$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} \bar{P}_{j} \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)}
$$(iii) The failure rate $r(t)$ is increasing if $h(t)$ is increasing and $\left(\bar{P}_{j}-\bar{P}_{j+1}\right) / \bar{P}_{j}$ is increasing.
(iv) The failure rate average $\int_{0}^{t} r(u) \mathrm{d} u / t$ is increasing if both $H(t) / t$ and $\left(\bar{P}_{j}-\right.$ $\left.\bar{P}_{j+1}\right) / \bar{P}_{j}$ are increasing.

When the total damage is additive, (2.32) is

$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} G^{(j)}(K) \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)}
$$

Then, properties (iii) and (iv) are rewritten as:
(v) The failure rate $r(t)$ is increasing if $h(t)$ is increasing and $r_{j+1}$ in (2.15) is increasing.
(vi) The failure rate average $\int_{0}^{t} r(u) \mathrm{d} u / t$ is increasing if both $H(t) / t$ and $r_{j+1}$ are increasing.

Such results were compactly summarized [90]. Moreover, when shocks occur in the birth process [68], in the counting process [72], and in the Lévy process [70], similar results were obtained.

After that, damage or shock models of this kind have been generalized and analyzed by many authors [91-107]. A general shock model, where the amount of damage due to shocks is correlated with their intervals, was analyzed [108-114]. Furthermore, bivariate and multivariate distributions derived from cumulative damage models were studied [115-123]. The failure rate was investigated for point, alternating, and diffused stresses [124].

# 2.4 Continuous Wear Processes 

Let $Y$ be the failure time of an operating unit. It is assumed that there exists a nonnegative function $h(t)$ such that

$$
\operatorname{Pr}\{t<Y \leq t+\Delta t\}=h(t) \Delta t+o(\Delta t)
$$

for $\Delta t>0$ and $t \geq 0$. Then, the probability of the unit surviving at time $t$ is

$$
R(t)=\operatorname{Pr}\{Y>t\}=\exp \left[-\int_{0}^{t} h(u) \mathrm{d} u\right]=\mathrm{e}^{-H(t)}
$$

that represents the reliability of the unit at time $t$ and is given in (1.1) of [1]. In this case, the function $h(t)$ is called an instantaneous wear and $H(t) \equiv$ $\int_{0}^{t} h(u) \mathrm{d} u$ is called an accumulated wear at time $t$ [37]. In particular, when $H(t)=a t / K$ for $a>0, R(t)=\mathrm{e}^{-a t / K}$ and $E\{Y\}=K / a$. Furthermore, when $H(t)=\lambda t^{m}(m>0), R(t)$ becomes a Weibull distribution and $R(t)=$ $\exp \left(-\lambda t^{m}\right)$.On the other hand, assume that $h(t)$ is the realization of the stochastic process $\{W(t), t \geq 0\}$ with independent increments [35]. Then,

$$
R(t)=E\left\{\exp \left[-\int_{0}^{t} W(u) \mathrm{d} u\right]\right\}
$$

If $Z(t)$ is simply the accumulated wear in a stochastic process with independent increments, then [34]

$$
R(t)=E\left\{\mathrm{e}^{-Z(t)}\right\}
$$

The reliability function $R(t)$ was given by a gamma distribution [125] and some reliability functions were derived in more general assumptions [126].

The accumulated wear function $Z(t)$ usually increases with time $t$ from 0 , and the unit fails when $Z(t)$ has exceeded a failure level $K$. Next, suppose that $Z(t)=A_{t} t+B_{t}$ for $A_{t} \geq 0$. Then, the reliability at time $t$ is

$$
R(t)=\operatorname{Pr}\{Z(t) \leq K\}=\operatorname{Pr}\left\{A_{t} t+B_{t} \leq K\right\}
$$

(1) When $A_{t} \equiv a$ (constant), $K \equiv k$ (constant), and $B_{t}$ is distributed normally with mean 0 and variance $\sigma^{2} t$,

$$
R(t)=\operatorname{Pr}\left\{B_{t} \leq k-a t\right\}=\Phi\left(\frac{k-a t}{\sigma \sqrt{t}}\right)
$$

where $\Phi(x)$ is the standard normal distribution with mean 0 and variance $1$, i.e., $\Phi(x)=(1 / \sqrt{2 \pi}) \int_{-\infty}^{x} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u$.
(2) When $B_{t} \equiv 0, K \equiv k$, and $A_{t}$ is distributed normally with mean $a$ and variance $\sigma^{2} / t$,

$$
R(t)=\operatorname{Pr}\left\{A_{t} \leq k / t\right\}=\Phi\left(\frac{k-a t}{\sigma \sqrt{t}}\right)
$$

that becomes equal to (2.39).
(3) When $A_{t} \equiv a, B_{t} \equiv 0$, and $K$ is distributed normally with mean $k$ and variance $\sigma^{2}$,

$$
R(t)=\operatorname{Pr}\{a t \leq K\}=\Phi\left(\frac{k-a t}{\sigma}\right)
$$

When $K$ is distributed normally with mean $k$ and variance $\sigma^{2} t, R(t)$ is equal to (2.39) and (2.40).
Replacing $\alpha \equiv \sigma / \sqrt{a k}$ and $\beta \equiv k / a$ in (2.39) or (2.40),

$$
R(t)=\Phi\left[\frac{1}{\alpha}\left(\sqrt{\frac{\beta}{t}}-\sqrt{\frac{t}{\beta}}\right)\right]
$$

that is called the Birnbaum-Saunders distribution [36,127]. This is widely applied to fatigue failure for material strength subject to stresses [128-130].When $Z(t)=\mu t+\sigma B_{t}$ with positive drift $\mu$ and variance $\sigma^{2}$ where $B_{t}$ is a standard Brownian motion, $Z(t)$ forms the Wiener process or Brownian motion process [62]. However, this has not been applied to actual damage models. When $Z(t)=A_{t} t+B_{t}$, if $A_{t}, B_{t}$ and $K$ are deterministic, i.e., $A_{t} \equiv a$, $B_{t} \equiv b$, and $K \equiv k$, then the unit fails at time $t=(k-b) / a$. By fitting appropriate distributions to $A_{t}, B_{t}$, and $K$ and estimating their parameters for practical systems, the function $Z(t)$ can be used as a continuous wear function in cumulative damage models. When $Z(t)=a t$ and $K$ is a random variable, the optimum policy where the unit is replaced at a planned time will be discussed in Section 5.2.

# 2.5 Modified Damage Models 

Let us consider the following five damage models mainly based on our own work: (1) damage model with imperfect shock where some shock may produce no damage to a unit [40], (2) a failure level is a random variable with a general distribution $L(x)$ [131], (3) the total damage decreases exponentially with time [132], (4) the damage model of a system with $n$ different units [133], and (5) the total damage increases with time [14, 134, 135]. Such damage models would be realistic in reliability models and be useful in practice. We derive the reliability quantities of each model and show simple examples when shock times are exponential.

## (1) Imperfect Shock

It has been assumed that the damage due to a shock occurs and its amount is distributed with $G(x)$. However, it may be considered that some shocks do not produce any damage to a unit.

Suppose that the damage due to shocks occurs with probability $p(0<$ $p \leq 1)$ and does not occur with probability $q \equiv 1-p$. Other notations are the same as those of Sections 2.1 and 2.2. Then, substituting $F_{1}(t)$ in Example 1.1 in $F(t)$ in (2.3), (2.5), (2.9), (2.11), and (2.14), $\operatorname{Pr}\{Z(t) \leq x\}, E\{Z(t)\}$, $\operatorname{Pr}\{Y \leq t\}, E\{Y\}$, and $r(t)$ are given. In particular, from (2.10) and (2.11), respectively,

$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{dPr}\{Y \leq t\} & =\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right]\left[\frac{p F^{*}(s)}{1-q F^{*}(s)}\right]^{j+1} \\
E\{Y\} & =\frac{1}{p \lambda} \sum_{j=0}^{\infty} G^{(j)}(K)=\frac{1}{p \lambda}\left[1+M_{G}(K)\right]
\end{aligned}
$$

The corresponding results for the independent damage model are, from (2.21) and (2.22), respectively,$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{dPr}\{Y \leq t\} & =\frac{p[1-G(K)] F^{*}(s)}{1-[q+p G(K)] F^{*}(s)} \\
E\{Y\} & =\frac{1}{p \lambda[1-G(K)]}
\end{aligned}
$$

# (2) Random Failure Level and Time-Dependent Failure Level 

Most units have individual variations in their ability to withstand shocks and are operating in a different environment. In such cases, a failure level $K$ is not constant and would be random. Consider the case where a failure level $K$ is a random variable with a general distribution $L(x)$ such that $L(0)=0$ [33]. Then, for the cumulative damage model, the distribution of time to failure is

$$
\operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty} F^{(j+1)}(t) \int_{0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} L(x)
$$

and its mean time is

$$
E\{Y\}=\frac{1}{\lambda} \sum_{j=0}^{\infty} \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)
$$

The failure rates are

$$
\begin{aligned}
r(t) & =\frac{\sum_{j=0}^{\infty} f^{(j+1)}(t) \int_{0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} L(x)}{\sum_{j=0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)} \\
r_{j+1} & =\frac{\int_{0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} L(x)}{\int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)}
\end{aligned}
$$

For the independent damage model,

$$
\begin{aligned}
\operatorname{Pr}\{Y \leq t\} & =\sum_{j=0}^{\infty} F^{(j+1)}(t) \int_{0}^{\infty}\left\{[G(x)]^{j}-[G(x)]^{j+1}\right\} \mathrm{d} L(x) \\
E\{Y\} & =\frac{1}{\lambda} \sum_{j=0}^{\infty} \int_{0}^{\infty}[G(x)]^{j} \mathrm{~d} L(x)
\end{aligned}
$$

For the cumulative model with imperfect shock,

$$
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{dPr}\{Y \leq t\}=\sum_{j=0}^{\infty}\left[\frac{p F^{*}(s)}{1-q F^{*}(s)}\right]^{j+1} \int_{0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} L(x)
$$

Example 2.3. Suppose that all random variables are exponential, i.e., $F(t)=$ $1-\mathrm{e}^{-\lambda t}$ and $G(x)=1-\mathrm{e}^{-\mu x}$. Then, we obtain the explicit formulas for each model.For imperfect shock, $F_{1}^{*}(s)=p \lambda /(s+p \lambda)$, i.e., $F_{1}(t)=1-\mathrm{e}^{-p \lambda t}$ by inversion. Thus, substituting $\lambda$ in $p \lambda$ in Example 2.2, we can obtain the corresponding results.

When a failure level $L(x)$ has also an exponential distribution $\left(1-\mathrm{e}^{-\theta x}\right)$,

$$
\int_{0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} L(x)=\frac{\theta \mu^{j}}{(\mu+\theta)^{j+1}}
$$

Thus, from (2.47),

$$
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty}\left(\frac{\lambda}{s+\lambda}\right)^{j+1} \frac{\theta \mu^{j}}{(\mu+\theta)^{j+1}}=\frac{\lambda \theta}{s(\mu+\theta)+\lambda \theta}
$$

By inversion,

$$
\begin{aligned}
\operatorname{Pr}\{Y \leq t\} & =1-\exp \left(-\frac{\lambda \theta t}{\mu+\theta}\right) \\
E\{Y\} & =\frac{1}{r(t)}=\frac{1}{\lambda} \sum_{j=1}^{\infty} j p_{j}=\frac{1}{\lambda}\left(\frac{\mu}{\theta}+1\right) \\
r_{j+1} & =\frac{\theta}{\mu+\theta}=\frac{r(t)}{\lambda}
\end{aligned}
$$

It is of great interest that both failure rates are constant, and $r_{j}$ corresponds to the ratio of (mean damage of one shock)/(mean failure level + mean damage of one shock).

For the independent damage model,

$$
\begin{aligned}
\operatorname{Pr}\{Y>t\} & =\int_{0}^{\infty} \exp \left(-\lambda t \mathrm{e}^{-\mu x}\right) \theta \mathrm{e}^{-\theta x} \mathrm{~d} x=\sum_{j=0}^{\infty} \frac{(-\lambda t)^{j}}{j!} \int_{0}^{\infty} \theta \mathrm{e}^{-(\theta+j \mu) x} \mathrm{~d} x \\
& =\sum_{j=0}^{\infty} \frac{(-\lambda t)^{j}}{j!} \frac{\theta}{\theta+j \mu} \\
E\{Y\} & =\frac{1}{r(t)}=\frac{1}{\lambda} \sum_{j=1}^{\infty} j p_{j} \\
& =\frac{1}{\lambda} \int_{0}^{\infty} \mathrm{e}^{\mu x} \theta \mathrm{e}^{-\theta x} \mathrm{~d} x= \begin{cases}\frac{\theta}{\lambda(\theta-\mu)} & (\theta>\mu) \\
\infty & (\theta \leq \mu)\end{cases}
\end{aligned}
$$

Finally, suppose that the total damage due to shocks is investigated and is known statistically at the beginning. Then, if the unit with damage $z_{0}(0 \leq$ $z_{0}<K$ ) begins to operate at time 0 , we can obtain all reliability quantities by replacing $K$ with $K-z_{0}[136]$.

Fig. 2.3. Process for a cumulative damage model with annealing

# (3) Damage with Annealing 

The total damage in the usual reliability models is additive and does not decrease. In some materials, annealing, i.e., lessening the damage, can take place such as rubber, fiber reinforced plastics, and polyurethane. We show two examples, using the results of [83].

Takács considered the following damage model: If a unit suffers damage $W$ due to shock then its damage after time duration $t$ is reduced to $W \mathrm{e}^{-\alpha t}$ $(0<\alpha<\infty)$. Define

$$
Z(t) \equiv \sum_{j=1}^{N(t)} W_{j} \exp \left[-\alpha\left(t-S_{j}\right)\right]
$$

where $S_{j} \equiv \sum_{i=1}^{j} X_{i}(j=1,2, \ldots)$ (Figure 2.3). This also corresponds to the shot noise model in (2) of Section 10.1.

Suppose that shocks occur in a Poisson process with rate $\lambda$. Then, $\Phi(t, x) \equiv$ $\operatorname{Pr}\{Z(t) \leq x\}$ forms the following renewal equation [83, p. 105]:

$$
\frac{\partial \Phi(t, x)}{\partial t}=-\lambda\left\{\Phi(t, x)-\int_{0}^{x} G\left[(x-y) \mathrm{e}^{-\alpha t}\right] \mathrm{d} y \Phi(t, y)\right\}
$$

and its LS transform is

$$
\frac{\partial \Phi^{*}(t, s)}{\partial t}=-\lambda\left[1-G^{*}\left(s \mathrm{e}^{-\alpha t}\right)\right] \Phi^{*}(t, s)
$$where $\Phi^{*}(t, s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s x} \mathrm{~d} \Phi(t, x)$ and $G^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s x} \mathrm{~d} G(x)$. Solving this differential equation,

$$
\begin{aligned}
\Phi^{*}(t, s) & =\exp \left\{-\lambda \int_{0}^{t}\left[1-G^{*}\left(s \mathrm{e}^{-\alpha u}\right)\right] \mathrm{d} u\right\} \\
E\{Z(t)\} & =-\left.\frac{\partial \Phi^{*}(t, s)}{\partial s}\right|_{s=0}=\frac{\lambda\left(1-\mathrm{e}^{-\alpha t}\right)}{\alpha \mu}
\end{aligned}
$$

In addition, if $1 / \mu=E\left\{W_{j}\right\}<\infty$, then $\lim _{t \rightarrow \infty} \operatorname{Pr}\{Z(t) \leq x\}$ exists and its LS transform is

$$
\Phi^{*}(\infty, s)=\exp \left[-\frac{\lambda}{\alpha} \int_{0}^{1} \frac{1-G^{*}(s u)}{u} \mathrm{~d} u\right]
$$

Example 2.4.
(i) When $G(x)=1-\mathrm{e}^{-\mu x}$,

$$
\Phi^{*}(t, s)=\left(\frac{s+\mu \mathrm{e}^{\alpha t}}{s+\mu}\right)^{\nu} \mathrm{e}^{-\lambda t}
$$

where $\nu \equiv \lambda / \alpha$. Thus, by inversion,

$$
\operatorname{Pr}\{Z(t) \leq x\}=\mathrm{e}^{-\lambda t} \sum_{j=0}^{\infty}\binom{\nu+j-1}{j}\left(1-\mathrm{e}^{-\alpha t}\right)^{j} \sum_{i=j}^{\infty} \frac{\left(\mu x \mathrm{e}^{\alpha t}\right)^{i}}{i!} \exp \left(-\mu x \mathrm{e}^{\alpha t}\right)
$$

In a similar way,

$$
\begin{gathered}
\Phi^{*}(\infty, s)=\left(\frac{\mu}{s+\mu}\right)^{\nu} \\
\lim _{t \rightarrow \infty} \operatorname{Pr}\{Z(t) \leq x\}=\int_{0}^{x} \frac{\mu(\mu u)^{\nu-1}}{\Gamma(\nu)} \mathrm{e}^{-\mu u} \mathrm{~d} u
\end{gathered}
$$

that is a gamma distribution with mean $\nu / \mu$.
(ii) When $G(x) \equiv 0$ for $x<1 / \mu$ and 1 for $x \geq 1 / \mu$, i.e., the damage due to each shock is constant and its amount is $1 / \mu$. From the results [83, p. 129],

$$
\Phi^{*}(\infty, s)=\left(\frac{\mu}{s \gamma}\right)^{\nu} \exp \left(-\nu \int_{1 / \mu}^{\infty} \frac{\mathrm{e}^{-s u}}{u} \mathrm{~d} u\right)
$$

where $\gamma \equiv \mathrm{e}^{c}=1.781072 \cdots$ and $C \equiv 0.577215 \cdots$ that is Euler's constant. By inversion,

$$
\lim _{t \rightarrow \infty} \operatorname{Pr}\{Z(t) \leq x\}=\frac{x^{\nu}+\sum_{j=1}^{\infty}\left[(-1)^{j} \nu^{j} / j!\right] \int_{j / \mu}^{x}(x-u)^{\nu} I^{(j)}(u) \mathrm{d} u}{(\gamma / \mu)^{\nu} \Gamma(1+\nu)}
$$

where $I(y)$ is uniform over $[0,1 / \mu]$.# (4) $\boldsymbol{n}$ Different Units 

Consider a system with $n$ different units that are independent of each other. Successive shocks occur at time interval $X_{j}$ with distribution $F(t) \equiv \operatorname{Pr}\left\{X_{j} \leq\right.$ $t\}(j=1,2, \ldots)$. Each shock causes some damage to unit $i(i=1,2, \ldots, n)$ in the amount $W_{i ; j}$ with distribution $G_{i}(x) \equiv \operatorname{Pr}\left\{W_{i ; j} \leq x\right\}$ for all $j \geq 1$, where $W_{i ; j}$ might be zero. Each unit fails when its total damage has exceeded its failure level $K_{i}(i=1,2, \ldots, n)$. A series system with $n$ units subject to shocks was considered [137].

One typical example of this model would be the damage to railroad tracks, ties and pantographs. Such damage is mainly due to the number and sizes of running trains and depends on the weight and the speed of trains. In the case of $n=3, X_{j}$ is the time interval of trains, and $W_{i ; j}(i=1,2,3)$ are the amounts of damage to the railroad tracks, ties, and pantographs, respectively, produced by one running train.

Letting $Z_{i}(t)$ denote the total damage to unit $i(i=1,2, \ldots, n)$ at time $t$, the joint distribution of $Z_{i}(t)$ is

$$
\begin{aligned}
& \operatorname{Pr}\left\{Z_{i}(t) \leq x_{i}(i=1,2, \ldots, n)\right\} \\
& \quad=\sum_{j=0}^{\infty} \operatorname{Pr}\left\{Z_{i}(t) \leq x_{i}(i=1,2, \ldots, n) \mid N(t)=j\right\} \operatorname{Pr}\{N(t)=j\}
\end{aligned}
$$

From the assumption that each amount of damage occurs independently,

$$
\operatorname{Pr}\left\{Z_{i}(t) \leq x_{i}(i=1,2, \ldots, n) \mid N(t)=j\right\}=\prod_{i=1}^{n} G_{i}^{(j)}\left(x_{i}\right)
$$

Thus, the joint distribution is

$$
\operatorname{Pr}\left\{Z_{i}(t) \leq x_{i}(i=1,2, \ldots, n)\right\}=\sum_{j=0}^{\infty}\left[\prod_{i=1}^{n} G_{i}^{(j)}\left(x_{i}\right)\right]\left[F^{(j)}(t)-F^{(j+1)}(t)\right]
$$

Suppose that a system fails when at least one of $n$ units exceeds a failure level $K_{i}$, i.e., the system is a $n$-unit series system. Then, the first-passage time distribution to system failure is

$$
\begin{aligned}
\operatorname{Pr}\{Y \leq t\} & =1-\operatorname{Pr}\left\{Z_{i}(t) \leq K_{i}(i=1,2, \ldots, n)\right\} \\
& =\sum_{j=0}^{\infty}\left[1-\prod_{i=1}^{n} G_{i}^{(j)}\left(K_{i}\right)\right]\left[F^{(j)}(t)-F^{(j+1)}(t)\right]
\end{aligned}
$$

and its mean time is

$$
E\{Y\}=\frac{1}{\lambda} \sum_{j=0}^{\infty}\left[\prod_{i=1}^{n} G_{i}^{(j)}\left(K_{i}\right)\right]
$$Next, when a system fails if all of $n$ units exceed a failure level $K_{i}$, i.e., the system is an $n$-unit parallel system, the first-passage time distribution to system failure is

$$
\operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty}\left\{\prod_{i=1}^{n}\left[1-G_{i}^{(j)}\left(K_{i}\right)\right]\right\}\left[F^{(j)}(t)-F^{(j+1)}(t)\right]
$$

and its mean time is

$$
E\{Y\}=\frac{1}{\lambda} \sum_{j=0}^{\infty}\left\{1-\prod_{i=1}^{n}\left[1-G_{i}^{(j)}\left(K_{i}\right)\right]\right\}
$$

When shocks occur in a nonhomogeneous Poisson process with a mean value function $H(t)$, the first-passage time distributions and their mean times are derived by replacing $F^{(j)}(t)-F^{(j+1)}(t)$ with $\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}$ formally.

Furthermore, suppose that a shock does no damage to unit $i$ with probability $q_{i} \equiv 1-p_{i}$, and otherwise, does some positive damage $W_{i ; j}$ with distribution $G_{i}(x)$. In this case,
$\operatorname{Pr}\left\{Z_{i}(t) \leq x_{i}(i=1,2, \ldots, n) \mid N(t)=j\right\}=\prod_{i=1}^{n}\left[\sum_{m=0}^{j}\binom{j}{m} q_{i}^{m} p_{i}^{j-m} G_{i}^{(j-m)}\left(x_{i}\right)\right]$,
and hence, we can get the first-passage time distributions and their mean times from (2.62)-(2.65).

Example 2.5. Suppose that any amount of damage to unit $i$ incurred from shocks is constant $1 / \mu_{i}$, i.e., $G_{i}(x)=0$ for $x<1 / \mu_{i}$ and 1 for $x \geq 1 / \mu_{i}$. Let $K_{m} \equiv \min \left\{\mu_{1} K_{1}, \mu_{2} K_{2}, \ldots, \mu_{n} K_{n}\right\}$ and $K_{M} \equiv \max \left\{\mu_{1} K_{1}, \mu_{2} K_{2}, \ldots, \mu_{n} K_{n}\right\}$. The first-passage time distribution and its mean time for a series system are, from (2.62) and (2.63),

$$
\operatorname{Pr}\{Y \leq t\}=F^{\left(\left[K_{m}\right]+1\right)}(t), \quad E\{Y\}=\frac{1}{\lambda}\left(\left[K_{m}\right]+1\right)
$$

and for a parallel system are, from (2.64) and (2.65),

$$
\operatorname{Pr}\{Y \leq t\}=F^{\left(\left[K_{M}\right]+1\right)}(t), \quad E\{Y\}=\frac{1}{\lambda}\left(\left[K_{M}\right]+1\right)
$$

where $[x]$ denotes the greatest integer contained in $x$.
Moreover, when $F(t)=1-\mathrm{e}^{-\lambda t}$ and $K_{m} \geq 1$, the failure rate is, for a series system,

$$
r(t)=\frac{\lambda(\lambda t)^{\left[K_{m}\right]} /\left[K_{m}\right]!}{\sum_{j=0}^{\left[K_{m}\right]}(\lambda t)^{j} / j!}
$$

and for a parallel system,

Fig. 2.4. Process for a cumulative damage model with two kinds of damages

$$
r(t)=\frac{\lambda(\lambda t)^{[K_{M}]} /[K_{M}]!}{\sum_{j=0}^{[K_{M}]}(\lambda t)^{j} / j!}
$$

both of which are $r(0)=0$, and increase monotonically and become $r(\infty)=\lambda$ that is the constant failure rate of an exponential distribution $\left(1-\mathrm{e}^{-\lambda t}\right)$. If $K_{M}<1$, then $r(t)=\lambda$ for all $t \geq 0$.

# (5) Increasing Damage with Time 

Consider the cumulative damage model with two kinds of damage (see Figure 2.4). One of them is caused by shock and is additive, and the other increases proportionately with time, that is, the total damage is accumulated subject to shocks and time at the rate of constant $\alpha(\alpha>0)$, independent of shocks. A unit fails whether the total damage is exceeded with time or has exceeded a failure level $K$ at some shock, and its failure is detected only at the time of shocks. Such a model would be the life of dry and storage batteries. A battery supplies electric power that is stored by chemical change according to its need. However, oxidation and deoxidation always occur irrespective of itsuse, that is, a battery always discharges a small quantity of electricity with time, and finally, it cannot be used.

Suppose that $S_{j} \equiv X_{1}+X_{2}+\cdots+X_{j}, Z_{j} \equiv W_{1}+W_{2}+\cdots+W_{j}(j=$ $1,2, \ldots)$, and $S_{0} \equiv Z_{0} \equiv 0$. Because $\operatorname{Pr}\left\{S_{j} \leq t\right\}=F^{(j)}(t)$ where $\operatorname{Pr}\left\{Z_{j} \leq\right.$ $x\}=G^{(j)}(x)(j=0,1,2, \ldots)$, the distribution of time to detect a failure at some shock is

$$
\begin{aligned}
& \operatorname{Pr}\{Y \leq t\}=\sum_{j=0}^{\infty} \operatorname{Pr}\left\{Z_{j}+\alpha S_{j}<K \leq Z_{j+1}+\alpha S_{j+1}, S_{j+1} \leq t\right\} \\
& \quad=\sum_{j=0}^{\infty} \int_{0}^{t}\left\{\int_{0}^{t-u}\left[G^{(j)}(K-\alpha u)-G^{(j+1)}(K-\alpha(u+x))\right] \mathrm{d} F(x)\right\} \mathrm{d} F^{(j)}(u)
\end{aligned}
$$

where note that $G^{(j)}(x) \equiv 0$ for $x<0$. Thus, the mean time to detect a failure at some shock is

$$
\begin{aligned}
E\{Y\} & = \\
\sum_{j=0}^{\infty} & \int_{0}^{\infty}\left\{\int_{0}^{\infty}(t+x)\left[G^{(j)}(K-\alpha t)-G^{(j+1)}(K-\alpha(t+x))\right] \mathrm{d} F(x)\right\} \mathrm{d} F^{(j)}(t) \\
& =\frac{1}{\lambda} \sum_{j=0}^{\infty} \int_{0}^{K / \alpha} G^{(j)}(K-\alpha t) \mathrm{d} F^{(j)}(t)
\end{aligned}
$$

Similarly, the probability that the failure is detected at the $(j+1)$ th shock is

$$
\begin{aligned}
p_{j+1} & =\int_{0}^{\infty}\left\{\int_{0}^{\infty}\left[G^{(j)}(K-\alpha t)-G^{(j+1)}(K-\alpha(t+x))\right] \mathrm{d} F(x)\right\} \mathrm{d} F^{(j)}(t) \\
& =\int_{0}^{K / \alpha} G^{(j)}(K-\alpha t) \mathrm{d} F^{(j)}(t)-\int_{0}^{K / \alpha} G^{(j+1)}(K-\alpha t) \mathrm{d} F^{(j+1)}(t) \\
& (j=0,1,2, \ldots)
\end{aligned}
$$

and the failure rate is

$$
\begin{array}{r}
r_{j+1}=\frac{\int_{0}^{K / \alpha} G^{(j)}(K-\alpha t) \mathrm{d} F^{(j)}(t)-\int_{0}^{K / \alpha} G^{(j+1)}(K-\alpha t) \mathrm{d} F^{(j+1)}(t)}{\int_{0}^{K / \alpha} G^{(j)}(K-\alpha t) \mathrm{d} F^{(j)}(t)} \\
(j=0,1,2, \ldots)
\end{array}
$$

This corresponds to the model where a failure level $K(t)$ at time $t$ decreases with time $t$, i.e., $K(t)=K-\alpha t$.

Example 2.6. It is intuitively estimated from (2.11) that because the average damage per unit of time is $\alpha+\lambda / \mu$, the mean time until the total damage has exceeded a failure level $K$ is approximatelyTable 2.1. Mean time to failure for two kinds of damage when $1 / \lambda=1$

| $\alpha \mu$ | $\mu K=1$ |  | $\mu K=5$ |  | $\mu K=10$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\lambda l$ | $\lambda E\{Y\}$ | $\lambda l$ | $\lambda E\{Y\}$ | $\lambda l$ | $\lambda E\{Y\}$ |
| 0.0 | 2.0 | 2.000 | 6.0 | 6.000 | 11.0 | 11.000 |
| 0.2 | 1.8 | 1.705 | 5.2 | 5.078 | 9.3 | 9.294 |
| 0.4 | 1.7 | 1.521 | 4.6 | 4.392 | 8.1 | 7.989 |
| 0.6 | 1.6 | 1.410 | 4.1 | 3.907 | 7.3 | 7.049 |
| 0.8 | 1.6 | 1.334 | 3.8 | 3.543 | 6.6 | 6.333 |
| 1.0 | 1.5 | 1.286 | 3.5 | 3.260 | 6.0 | 5.770 |
| 2.0 | 1.3 | 1.162 | 2.7 | 2.450 | 4.3 | 4.121 |
| 4.0 | 1.2 | 1.086 | 2.0 | 1.843 | 3.0 | 2.845 |

$$
l=\frac{1}{\lambda}\left(\frac{K}{\alpha / \lambda+1 / \mu}+1\right)
$$

Table 2.1 presents $\lambda E\{Y\}$ and $\lambda l$ for $\alpha \mu$ and $\mu K$ when $F(t)=1-\mathrm{e}^{-\lambda t}$, $G(x)=1-\mathrm{e}^{-\mu x}$, and $1 / \lambda=1$. When $\alpha=0$, this corresponds to the standard cumulative model given in Example 2.2. This table indicates that $l$ shows a good upper bound for the mean time to failure. In actual models, $l$ would be easily computed, and it would be used practically as one estimation of their mean failure times.

Finally, if the total damage increases exponentially, i.e.,

$$
Z(t)=\sum_{j=1}^{N(t)} W_{j} \exp \left[\alpha\left(t-S_{j}\right)\right]
$$

then by arguments similar to those of (3), when $F(t)=1-\mathrm{e}^{-\lambda t}$,

$$
\begin{aligned}
\Phi^{*}(t, s) & =\exp \left\{-\lambda \int_{0}^{t}\left[1-G^{*}\left(s \mathrm{e}^{\alpha u}\right)\right] \mathrm{d} u\right\} \\
E\{Z(t)\} & =\frac{\lambda\left(\mathrm{e}^{\alpha t}-1\right)}{\alpha \mu} \\
\Phi^{*}(\infty, s) & =\exp \left[-\frac{\lambda}{\alpha} \int_{1}^{\infty} \frac{1-G^{*}(s u)}{u} \mathrm{~d} u\right]
\end{aligned}
$$

This corresponds to the model where the total damage due to shocks is additive and also increases exponentially with time.# Basic Replacement Policies 

Consider a unit that should operate over an infinite time span. It is assumed that shocks occur in random times and each shock causes a random amount of damage to a unit. These damages are additive, and a unit fails when the total damage has exceeded a failure level $K$. When the failure during actual operation is costly or dangerous, it is of great importance to avoid such terrible situations. It would be wise to exchange a unit at a lower cost before its failure. The replacement after failure and before failure is called corrective replacement and preventive replacement, respectively. We may consider damage as cost incurred from shocks. In this case, this corresponds to the maintenance model where a unit is replaced when the total cost incurred for some maintenance has exceeded a threshold level $K$.

This is the maintenance model for a single unit, where its failure is very serious, and sometimes may incur a heavy loss. If we have no information on the condition of a unit, its maintenance should be done at planned times. On the other hand, if we could get the number of shocks up to now and the amount of damage at shock times or at inspection times, its maintenance should be done at a prespecified number of shocks or at a damage level before failure, respectively.

Suppose that a unit is replaced with a new one at failure. It may be wise to do some maintenance at a lower cost before failure. The optimum control-limit policies where a unit is replaced at a threshold level was derived, when it fails with a known probability that is a function of the total damage [42-45]. More discussions on such replacement policies were carried out [138-146]. Such replacements were summarized $[147,148]$. On the other hand, the replacement models where a unit is replaced at a planned time $T$ were proposed [46-50]. Furthermore, the cumulative damage model where the total damage is decreasing at a known restoration rate was proposed [149-152]. Recently, a variety of replacement models subject to shocks were studied [153-160]. Replacement policies for multistate degraded systems subject to random shocks were discussed [161-165]. A $\delta$-shock model, where the second shock will cause thefailure if the time interval between two successive shocks is less than $\delta$, was proposed $[166,167]$.

This chapter is written based on $[51,168]$ and adds some new results by combining the theories of cumulative processes [11] and maintenance [1]. In Section 3.1, a unit is replaced before failure at a planned time $T$, at a shock number $N$, or at a damage level $Z$, whichever occurs first. Introducing the respective replacement costs for $T, N$, and $Z$, we obtain the expected cost rates. In Section 3.2, we derive analytically optimum policies that minimize the expected cost rates for the three policies. Some optimum policies are compared with other values in numerical examples. In Section 3.3, we propose five modified replacement models that would be useful in practical fields and give more interesting research topics for further study.

# 3.1 Three Replacement Policies 

Suppose that a unit begins to operate at time 0 and its damage level is 0 . Let $N(t)$ be the number of shocks in time $t$. It is assumed that the probability that $j$ shocks occur in $[0, t]$ is $F_{j}(t)(j=1,2, \cdots)$, where $F_{0}(t) \equiv 1$, i.e., the probability that $j$ shocks occur exactly in $[0, t]$ is

$$
\operatorname{Pr}\{N(t)=j\}=F_{j}(t)-F_{j+1}(t) \quad(j=0,1,2, \cdots)
$$

An amount $W_{j}$ of damage due to the $j$ th shock has an identical distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$ with finite mean $1 / \mu$, where $\bar{G}(x) \equiv 1-G(x)$ and $1 / \mu \equiv \int_{0}^{\infty} \bar{G}(x) \mathrm{d} x<\infty$. Furthermore, the total damage is additive, and its level is investigated and is known only at shock times. The unit fails when the total damage has exceeded a failure level $K$ at some shock, its failure is immediately detected, and it is replaced with a new one.

As the preventive replacement policy, the unit is replaced before failure at a planned time $T(0<T \leq \infty)$, at a shock number $N(N=1,2, \cdots)$, or at a damage level $Z(0 \leq Z \leq K)$, whichever occurs first. In addition, it is assumed that the unit is replaced at $K$ or $Z$ without replacing it at $N$, respectively, when the total damage has exceeded $K$ or $Z$ at shock $N$.

The probability that the unit is replaced at time $T$ is

$$
P_{T}=\sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z)
$$

the probability that it is replaced at shock $N$ is

$$
P_{N}=F_{N}(T) G^{(N)}(Z)
$$

the probability that it is replaced at damage $Z$ is

$$
P_{Z}=\sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x)
$$and the probability that it is replaced at failure level $K$, i.e., corrective replacement is done, is

$$
P_{K}=\sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)
$$

where $\varphi^{(j)}(x)(j=1,2, \cdots)$ denotes the $j$-fold Stieltjes convolution of any distribution $\varphi(x)$ with itself and $\varphi^{(0)}(x) \equiv 1$ for $x \geq 0$. It is clearly shown that $P_{T}+P_{N}+P_{Z}+P_{K}=1$. Similarly, the mean time to replacement is

$$
\begin{aligned}
& T \sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z)+G^{(N)}(Z) \int_{0}^{T} t \mathrm{~d} F_{N}(t) \\
& \quad+\sum_{j=0}^{N-1} \int_{0}^{T} t \mathrm{~d} F_{j+1}(t) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \\
& \quad+\sum_{j=0}^{N-1} \int_{0}^{T} t \mathrm{~d} F_{j+1}(t) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x) \\
& =\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t
\end{aligned}
$$

For the above replacement model, we introduce the following replacement costs: Cost $c_{T}$ is incurred for replacement at time $T$, and $c_{N}, c_{Z}$, and $c_{K}$ are the respective replacement cost at shock $N$, damage $Z$, and failure level $K$, where cost $c_{K}$ is higher than the three costs $c_{T}, c_{N}$, and $c_{Z}$. Then, the total expected cost until replacement, given that the unit began to operate at time 0 , is

$$
\begin{aligned}
\widehat{C}(T, N, Z)= & c_{T} P_{T}+c_{N} P_{N}+c_{Z} P_{Z}+c_{K} P_{K} \\
= & c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z) \\
& -\left(c_{K}-c_{N}\right) F_{N}(T) G^{(N)}(Z) \\
& -\left(c_{K}-c_{Z}\right) \sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

We call the time interval from one replacement to the next replacement one cycle. Then, the pairs of time and cost in each cycle are independently and identically distributed, and both have finite means. Thus, from (1.34) in a renewal reward process, the expected cost per unit of time for an infinite interval is$$
C(T, N, Z)=\frac{\text { Expected cost of one cycle }}{\text { Mean time of one cycle }}
$$

that is called the expected cost rate. Thus, dividing (3.6) by (3.5),

$$
\begin{aligned}
& c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z) \\
& -\left(c_{K}-c_{N}\right) F_{N}(T) G^{(N)}(Z) \\
C(T, N, Z)= & \frac{-\left(c_{K}-c_{Z}\right) \sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
\end{aligned}
$$

When the unit is replaced only after failure, the expected cost rate is

$$
\begin{aligned}
C & \equiv \lim _{\substack{T \rightarrow \infty \\
Z \rightarrow K}} C(T, N, Z) \\
& =\frac{c_{K}}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
\end{aligned}
$$

Furthermore, denoting $c_{k}$ as the mean time for replacement at $k(k=$ $T, N, Z, K)$, the availability $A(T, N, Z)((2.24)$ of $[1])$ is

$$
\begin{aligned}
A(T, N, Z) & \equiv \frac{\text { Mean time to replacement }}{\text { Mean time to replacement }+ \text { Mean time for replacement }} \\
& =1 /\left\{1+\frac{c_{T} P_{T}+c_{N} P_{N}+c_{Z} P_{Z}+c_{K} P_{K}}{\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}\right\}
\end{aligned}
$$

Thus, the policy maximizing $A(T, N, Z)$ is theoretically the same as minimizing the expected cost rate $C(T, N, Z)$ in (3.8).

# 3.2 Optimum Policies 

We discuss analytically an optimum planned time $T^{*}$, shock number $N^{*}$, and damage level $Z^{*}$ that minimize the expected cost rates when $F_{j}(t) \equiv$ $F^{(j)}(t)(j=1,2, \cdots)$, i.e., shocks occur in a renewal process with a general distribution $F(t)$ and its finite mean $1 / \lambda$.

## (1) Optimum $T^{*}$

Suppose that a unit is replaced at time $T(0<T \leq \infty)$ or at failure, whichever occurs first. Then, the expected cost rate is, from (3.8),

$$
\begin{aligned}
C_{1}(T) & \equiv \lim _{\substack{N \rightarrow \infty \\
Z \rightarrow K}} C(T, N, Z) \\
& =\frac{c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(K)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} t}
\end{aligned}
$$It can be easily seen that $\lim _{T \rightarrow 0} C_{1}(T)=\infty$, and from (3.9),

$$
C_{1} \equiv \lim _{T \rightarrow \infty} C_{1}(T)=\frac{c_{K}}{\left[1+M_{G}(K)\right] / \lambda}
$$

where $M_{G}(K) \equiv \sum_{j=1}^{\infty} G^{(j)}(K)$, and note that the denominator of the righthand side represents the mean time to failure given in (2.11). Thus, there exists a positive $T^{*}\left(0<T^{*} \leq \infty\right)$ that minimizes $C_{1}(T)$.

We seek an optimum time $T^{*}$ that minimizes $C_{1}(T)$ in (3.11) for $c_{K}>c_{T}$. Let $f(t)$ be a density function of $F(t), f^{(j)}(t)(j=1,2, \cdots)$ be the $j$-fold Stieltjes convolution of $f(t)$ with itself, and $f^{(0)}(t) \equiv 0$ for $t \geq 0$. Then, differentiating $C_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
& Q(T) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} t \\
& \quad-\sum_{j=0}^{\infty} F^{(j+1)}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]=\frac{c_{T}}{c_{K}-c_{T}}
\end{aligned}
$$

where

$$
Q(T) \equiv \frac{\sum_{j=0}^{\infty} f^{(j+1)}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]}{\sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(K)}
$$

It can be clearly seen that if $Q(T)$ is strictly increasing in $T$, then the left-hand side of (3.13) is also strictly increasing from 0 to $Q(\infty)(1 / \lambda)\left[1+M_{G}(K)\right]-1$, where $Q(\infty) \equiv \lim _{T \rightarrow \infty} Q(T)$. Thus, if $Q(\infty)\left[1+M_{G}(K)\right]>\lambda c_{K} /\left(c_{K}-c_{T}\right)$, then there exists a finite and unique $T^{*}$ that satisfies (3.13), and the resulting cost rate is

$$
C_{1}\left(T^{*}\right)=\left(c_{K}-c_{T}\right) Q\left(T^{*}\right)
$$

Conversely, if $Q(\infty)\left[1+M_{G}(K)\right] \leq \lambda c_{K} /\left(c_{K}-c_{T}\right)$, then $T^{*}=\infty$, i.e., the unit is replaced only at failure, and the expected cost rate is given in (3.12).

If a failure level $K$ is distributed according to a general distribution $L(x)$ as shown in (2) of Section 2.5, the expected cost rate becomes

$$
C_{1}(T)=\frac{c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)}{\sum_{j=0}^{\infty} \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)}
$$

In particular, suppose that shocks occur in a nonhomogeneous Poisson process and a failure level $K$ is distributed exponentially, i.e., $F_{j}(t)=\sum_{i=j}^{\infty}\left\{[H(t)]^{j} / j!\right\}$ $\times \mathrm{e}^{-H(t)}(j=0,1,2, \cdots)$ and $L(x)=1-\mathrm{e}^{-\theta x}$. Then, the expected cost rate is rewritten as

$$
C_{1}(T)=\frac{c_{K}-\left(c_{K}-c_{T}\right) \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(T)}}{\int_{0}^{T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t}
$$

where $G^{*}(\theta)$ denotes the Laplace-Stieltjes transform of $G(x)$, i.e., $G^{*}(\theta) \equiv$ $\int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} G(x)$ for $\theta>0$.We seek an optimum time $T^{*}$ that minimizes $C_{1}(T)$ in (3.16). First, it is easily noted that the problem of minimizing $C_{1}(T)$ is the same standard age replacement problem with a failure distribution $\left(1-\exp \left\{-\left[1-G^{*}(\theta)\right] H(t)\right\}\right)$ in Chapter 3 of [1]. Let $h(t)$ be an intensity function of a nonhomogeneous Poisson process, i.e., $h(t) \equiv \mathrm{d} H(t) / \mathrm{d} t$ and $H(t)=\int_{0}^{t} h(u) \mathrm{d} u$. Then, differentiating $C_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
\left[1-G^{*}(\theta)\right] h(T) \int_{0}^{T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t+\mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(T)}=\frac{c_{K}}{c_{K}-c_{T}}
$$

Letting $Q_{1}(T)$ denote the left-hand side of (3.17), it can be easily seen that if $h(t)$ is strictly increasing, then $Q_{1}(T)$ is also strictly increasing from 1 to

$$
Q_{1}(\infty) \equiv \lim _{T \rightarrow \infty} Q_{1}(T)=\left[1-G^{*}(\theta)\right] h(\infty) \int_{0}^{\infty} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t
$$

Therefore, we have the following optimum policy:
(i) If $h(t)$ is strictly increasing and $Q_{1}(\infty)>c_{K} /\left(c_{K}-c_{T}\right)$, then there exists a finite and unique $T^{*}\left(0<T^{*}<\infty\right)$ that satisfies (3.17), and the resulting cost rate is

$$
C_{1}\left(T^{*}\right)=\left(c_{K}-c_{T}\right)\left[1-G^{*}(\theta)\right] h\left(T^{*}\right)
$$

(ii) If $h(t)$ is strictly increasing and $Q_{1}(\infty) \leq c_{K} /\left(c_{K}-c_{T}\right)$ or $h(t)$ is nonincreasing, then $T^{*}=\infty$, and the expected cost rate is

$$
C_{1}(\infty) \equiv \lim _{T \rightarrow \infty} C_{1}(T)=\frac{c_{K}}{\int_{0}^{\infty} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t}
$$

In the case of (ii), it is of interest that there does not exist any finite time $T^{*}$ to minimize $C_{1}(T)$ when shocks occur in a Poisson process, i.e., $h(t)=\lambda$.

# (2) Optimum $N^{*}$ 

Suppose that a unit is replaced at shock $N(N=1,2, \cdots)$ or at failure, whichever occurs first. Then, the expected cost rate is, from (3.8),

$$
\begin{aligned}
C_{2}(N) & \equiv \lim _{\substack{T \rightarrow \infty \\
Z \rightarrow K}} C(T, N, Z) \\
& =\frac{c_{K}-\left(c_{K}-c_{N}\right) G^{(N)}(K)}{(1 / \lambda) \sum_{j=0}^{N-1} G^{(j)}(K)} \quad(N=1,2, \cdots)
\end{aligned}
$$

In particular, when $N=1$, i.e., the unit is always replaced at the first shock, the expected cost rate is

$$
C_{2}(1)=\lambda\left[c_{K}-\left(c_{K}-c_{N}\right) G(K)\right]
$$Forming the inequality $C_{2}(N+1)-C_{2}(N) \geq 0$ to seek an optimum number $N^{*}$ that minimizes $C_{2}(N)$ for $c_{K}>c_{N}$,

$$
Q_{2}(N+1) \sum_{j=0}^{N-1} G^{(j)}(K)-\left[1-G^{(N)}(K)\right] \geq \frac{c_{N}}{c_{K}-c_{N}} \quad(N=1,2, \cdots)
$$

where

$$
Q_{2}(N) \equiv \frac{G^{(N-1)}(K)-G^{(N)}(K)}{G^{(N-1)}(K)} \quad(N=1,2, \cdots)
$$

If $Q_{2}(N)$ is strictly increasing in $N$, i.e., $G^{(j+1)}(x) / G^{(j)}(x)$ is strictly decreasing in $j$, then the left-hand side of (3.22) is also strictly increasing in $N$ to $Q_{2}(\infty)\left[1+M_{G}(K)\right]-1$, where $Q_{2}(\infty) \equiv \lim _{N \rightarrow \infty} Q_{2}(N) \leq 1$. Thus, if $Q_{2}(\infty)\left[1+M_{G}(K)\right]>c_{K} /\left(c_{K}-c_{N}\right)$, then there exists a finite and unique minimum number $N^{*}\left(1 \leq N^{*}<\infty\right)$ that satisfies (3.22), and the expected cost rate is

$$
\lambda\left(c_{K}-c_{N}\right) Q_{2}\left(N^{*}\right)<C_{2}\left(N^{*}\right) \leq \lambda\left(c_{K}-c_{N}\right) Q_{2}\left(N^{*}+1\right)
$$

Conversely, if $Q_{2}(\infty)\left[1+M_{G}(K)\right] \leq c_{K} /\left(c_{K}-c_{N}\right)$, then $N^{*}=\infty$. Note that $Q_{2}(N)$ corresponds to the discrete failure rate $r_{N}$ given in (2.15), and $Q_{2}(N+1)$ represents the probability that the unit surviving at the $N$ th shock will fail at the $(N+1)$ th shock. In general, $Q_{2}(N)$ would increase to 1 . In this case, if $M_{G}(K)>c_{N} /\left(c_{K}-c_{N}\right)$, i.e., the expected number of shocks before failure is greater than $c_{N} /\left(c_{K}-c_{N}\right)$, then a finite $N^{*}$ exists uniquely.

# (3) Optimum $Z^{*}$ 

Suppose that a unit is replaced at damage $Z(0 \leq Z \leq K)$ or at failure, whichever occurs first. Then, the expected cost rate is, from (3.8),

$$
\begin{aligned}
C_{3}(Z) & \equiv \lim _{\substack{T \rightarrow \infty \\
N \rightarrow \infty}} C(T, N, Z) \\
& =\frac{c_{K}-\left(c_{K}-c_{Z}\right)\left[G(K)-\int_{0}^{Z} \bar{G}(K-x) \mathrm{d} M_{G}(x)\right]}{\left[1+M_{G}(Z)\right] / \lambda}
\end{aligned}
$$

When $Z=0, C_{3}(0)$ agrees with $C_{2}(1)$ in (3.21) when $c_{Z}=c_{N}$.
We seek an optimum level $Z^{*}$ that minimizes $C_{3}(Z)$ in (3.24) for $c_{K}>c_{Z}$. Differentiating $C_{3}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\int_{K-Z}^{K}\left[1+M_{G}(K-x)\right] \mathrm{d} G(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

The left-hand side of (3.25) is strictly increasing from 0 to $M_{G}(K)$. Thus, if $M_{G}(K)>c_{Z} /\left(c_{K}-c_{Z}\right)$, then there exists a finite and unique $Z^{*}\left(0<Z^{*}<K\right)$ that satisfies (3.25), and its resulting cost rate is$$
C_{3}\left(Z^{*}\right)=\lambda\left(c_{K}-c_{Z}\right) \bar{G}\left(K-Z^{*}\right)
$$

Conversely, if $M_{G}(K) \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$, i.e., the unit should be replaced only at failure, and the expected cost rate is given in (3.12).

If $G(x)$ has an IFR property, then from (1.20), $\mu K \geq M_{G}(K) \geq \mu K-1$, where $1 / \mu \equiv E\left\{W_{j}\right\}$. Thus, if $\mu K>c_{K} /\left(c_{K}-c_{Z}\right)$, then an optimum $Z^{*}$ $\left(0<Z^{*}<K\right)$ exists uniquely, and if $\mu K \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$. In addition, if the solutions $Z_{1}$ and $Z_{2}$ to satisfy

$$
\int_{K-Z}^{K}[1+\mu(K-x)] \mathrm{d} G(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

and

$$
\int_{K-Z}^{K} \mu(K-x) \mathrm{d} G(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

exist, respectively, then $Z_{1} \leq Z^{*} \leq Z_{2}$.
Example 3.1. Consider the replacement of car tires where the damage to the tire is a function of the running distance. If the running distance exceeds $K=30,000 \mathrm{~km}$, the tire is regarded as failed and is not suitable for running. The distance traveled in one time unit is assumed to obey an exponential distribution with mean $1 / \mu$, i.e., $G(x)=1-\mathrm{e}^{-\mu x}$ and $M_{G}(x)=\mu x$. Then, cost $c_{Z}$ represents the usual replacement cost of the tire and is 11,000 yen (about $\$ 100$ ). Cost $c_{K}$ includes all costs resulting from the failure of tires in service, and will be higher than $c_{Z}$ because there is a risk of accidents. From the above results, if $\mu K>c_{Z} /\left(c_{K}-c_{Z}\right)$, then there exists a finite and unique $Z^{*}$ that satisfies

$$
\mu Z \mathrm{e}^{-\mu(K-Z)}=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

Thus, we may replace the tire when the total running exceeds $Z^{*} \mathrm{~km}$ before failure. In this case, the expected cost rate is $C_{3}\left(Z^{*}\right) /\left(\lambda c_{Z}\right)=1 /\left(\mu Z^{*}\right)$. On the other hand, if the tire is replaced only when the total distance has exceeded $30,000 \mathrm{~km}$, then the expected cost is $C_{3}(K) /\left(\lambda c_{Z}\right)=\left(c_{K} / c_{Z}\right) /(1+\mu K)$. Furthermore, from (3.28), $Z_{2}$ is given by the unique solutions of the following equations:

$$
\mathrm{e}^{-\mu K}\left[1-(1-\mu Z) \mathrm{e}^{\mu Z}\right]=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

and $Z^{*}=Z_{1} \leq Z_{2}$.
Another simple method of replacement is to balance the ratio of replacement costs before and after failures against that of a damage level and a failure level, i.e.,

$$
\frac{\widetilde{Z}}{K+1 / \mu}=\frac{c_{Z}}{c_{K}}
$$

It is clearly seen that $Z^{*}>\widetilde{Z}$ because $\mathrm{e}^{\mu(K-Z)}>1+\mu(K-Z)$ for $K>Z$.Table 3.1. Comparison of optimum damage level $Z^{*}$ and approximate values $Z_{2}$ and $\widetilde{Z}$ for $c_{K} / c_{Z}$ and $1 / \mu$ when $K=30,000 \mathrm{~km}$

| $1 / \mu$ | $c_{K} / c_{Z}=2$ |  |  | $c_{K} / c_{Z}=5$ |  |  | $c_{K} / c_{Z}=10$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $Z^{*}$ | $Z_{2}$ | $\widetilde{Z}$ | $Z^{*}$ | $Z_{2}$ | $\widetilde{Z}$ | $Z^{*}$ | $Z_{2}$ | $\widetilde{Z}$ |
| 100 | 29431 | 29431 | 15050 | 29293 | 29293 | 6020 | 29212 | 29212 | 3010 |
| 200 | 29004 | 29006 | 15100 | 28729 | 28730 | 6040 | 28568 | 28569 | 3020 |
| 300 | 28632 | 28635 | 15150 | 28220 | 28224 | 6060 | 27980 | 27983 | 3030 |
| 400 | 28296 | 28302 | 15200 | 27749 | 27755 | 6080 | 27429 | 27435 | 3040 |
| 500 | 27987 | 27996 | 15250 | 27306 | 27315 | 6100 | 26908 | 26917 | 3050 |
| 600 | 27700 | 27713 | 15300 | 26886 | 26900 | 6120 | 26410 | 26424 | 3060 |
| 700 | 27432 | 27449 | 15350 | 26486 | 26504 | 6140 | 25933 | 25952 | 3070 |
| 800 | 27179 | 27202 | 15400 | 26102 | 26127 | 6160 | 25473 | 25498 | 3080 |
| 900 | 26940 | 26970 | 15450 | 25734 | 25765 | 6180 | 25029 | 25061 | 3090 |
| 1000 | 26714 | 26751 | 15500 | 25379 | 25418 | 6200 | 24600 | 24639 | 3100 |

Table 3.1 presents the optimum value $Z^{*}$, upper value $Z_{2}$, and approximate value $\widetilde{Z}$ for $1 / \mu$ and $c_{K} / c_{Z}$, that decrease with both $1 / \mu$ and $c_{K} / c_{Z}$. This indicates that $\widetilde{Z}<Z^{*} \leq Z_{2}$ shows a good approximation, however, $\widetilde{Z}$ is too small to compare with $Z^{*}$, so that the upper bound given in (3.28) would be very useful practically to compute an optimum policy when $G(x)$ and its mean $1 / \mu$ are statistically estimated.

Until now, it has been assumed that shocks occur in random times and their amount of damage is statistically estimated. Next, the amount of damage is investigated only through inspections that are made at periodic times, that is, the amount of damage is generated during $\left((j-1) t_{0}, j t_{0}\right]$ according to an identical distribution $G(x)$ for all $j(j=1,2, \cdots)$, and its total damage is known only at $j t_{0}$, i.e., at the end of each period. This corresponds to the damage model where shocks occur at a constant time $t_{0}$. Replacing $1 / \lambda$ with $t_{0}$ in (3.24), we can obtain the expected cost rate and make a discussion similar to deriving an optimum policy.

# 3.3 Modified Replacement Models 

This section considers some extended models of Section 3.1 in more general replacement forms and discusses optimum policies. Furthermore, we propose the combined preventive replacement models of planned time, shock number and damage level. These models would be more realistic than the basic ones, and moreover, offer interesting topics to reliability theoreticians.# (1) Modified Cost 

The replacement costs may depend on the damage level at its replacement time. It is assumed that $c_{0}(x)(0 \leq x \leq K)$ is an additional replacement cost that is variable for the total damage $x$ with $c(0)=0$, that is, $\operatorname{cost} c_{k}+c_{0}(x)$ $(k=T, N, Z)$ is incurred for the replacement of the unit with damage $x$ at time $T$, shock $N$, and damage $Z$, respectively, and $\operatorname{cost} c_{K}+c_{0}(K)$ is incurred for the replacement at failure.

The expected cost when the unit is replaced at time $T$ is

$$
\sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] \int_{0}^{Z}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)
$$

the expected cost when it is replaced at shock $N$ is

$$
F_{N}(T) \int_{0}^{Z}\left[c_{N}+c_{0}(x)\right] \mathrm{d} G^{(N)}(x)
$$

and the expected cost when it is replaced at damage $Z$ is

$$
\sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z} \int_{Z-x}^{K-x}\left[c_{Z}+c_{0}(x+y)\right] \mathrm{d} G(y) \mathrm{d} G^{(j)}(x)
$$

Thus, summing up (3.29)-(3.31), adding them to the replacement cost $\left[c_{K}+\right.$ $\left.c_{0}(K)\right] P_{K}$, and dividing by (3.5), the expected cost rate is, from (3.7),

$$
\begin{aligned}
& c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z) \\
& -\left(c_{K}-c_{N}\right) F_{N}(T) G^{(N)}(Z) \\
& -\left(c_{K}-c_{Z}\right) \sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \\
& C(T, N, Z)=\frac{+\sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}\left[\int_{x}^{K} \bar{G}(y-x) \mathrm{d} c_{0}(y)\right] \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
\end{aligned}
$$

It is difficult to discuss optimum policies analytically. In particular, it is assumed that shocks occur in a Poisson process with rate $\lambda$, the amount of damage due to each shock has an exponential distribution with mean $1 / \mu$, and $c_{0}(x)$ is proportional to the total damage $x$, i.e., $F_{j}(t)=\sum_{i=j}^{\infty}\left[(\lambda t)^{i} / i!\right] \mathrm{e}^{-\lambda t}$, $G^{(j)}(x)=\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}$, and $c_{0}(x)=c_{0} x$.

The expected cost rate for the replacement at time $T$ under the above conditions is

$$
\begin{aligned}
\frac{C_{1}(T)}{\lambda} \equiv & \lim _{\substack{\sim \\
\searrow, Z \rightarrow \bar{K}}} \frac{C(T, N, Z)}{\lambda} \\
= & \frac{c_{K}-c_{0} / \mu-\left(c_{K}-c_{T}-c_{0} / \mu\right) \sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(K)}{\sum_{j=0}^{\infty} F_{j+1}(T) G^{(j)}(K)} \\
& +\frac{c_{0}}{\mu}
\end{aligned}
$$Differentiating $C_{1}(T)$ with respect to $T$ and setting it equal to zero, for $c_{K}>$ $c_{T}+c_{0} / \mu$,
$Q(T) \sum_{j=0}^{\infty} F_{j+1}(T) G^{(j)}(K)-\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \mathrm{e}^{-\lambda T}\left[1-G^{(j)}(K)\right]=\frac{c_{T}}{c_{K}-c_{T}-c_{0} / \mu}$,
where

$$
Q(T) \equiv \frac{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] \mathrm{e}^{-\lambda T}\left[G^{(j)}(K)-G^{(j+1)}(K)\right]}{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] \mathrm{e}^{-\lambda T} G^{(j)}(K)}
$$

First, note that $\left[G^{(j)}(K)-G^{(j+1)}(K)\right] / G^{(j)}(K)=\left[(\mu K)^{j} / j!\right] / \sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right]$ is strictly increasing from $\mathrm{e}^{-\mu K}$ to 1 from Example 2.2. Next, when $\left[G^{(j)}(x)-\right.$ $\left.G^{(j+1)}(x)\right] / G^{(j)}(x)$ is strictly increasing in $j$ for any distribution $G(x)$, we can prove [131] that

$$
Q(T)=\frac{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right]\left[G^{(j)}(x)-G^{(j+1)}(x)\right]}{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] G^{(j)}(x)}
$$

is also strictly increasing in $T$ for any $x>0$ as follows: Differentiating $Q(T)$ with respect to $T$,

$$
\begin{aligned}
\frac{\lambda}{\left[\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] G^{(j)}(x)\right]^{2}} & {\left[\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} G^{(j+1)}(x) \sum_{i=0}^{\infty} \frac{(\lambda T)^{i}}{i!} G^{(i+1)}(x)\right.} \\
& \left.-\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} G^{(j)}(x) \sum_{i=0}^{\infty} \frac{(\lambda T)^{i}}{i!} G^{(i+2)}(x)\right]
\end{aligned}
$$

The numerator is rewritten as

$$
\begin{aligned}
& \sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \sum_{i=0}^{\infty} \frac{(\lambda T)^{i}}{i!} G^{(j)}(x) G^{(i+1)}(x)\left[\frac{G^{(j+1)}(x)}{G^{(j)}(x)}-\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}\right] \\
& =\sum_{j=1}^{\infty} \frac{(\lambda T)^{j}}{j!} \sum_{i=0}^{j-1} \frac{(\lambda T)^{i}}{i!} G^{(j)}(x) G^{(i+1)}(x)\left[\frac{G^{(j+1)}(x)}{G^{(j)}(x)}-\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}\right] \\
& \quad+\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \sum_{i=j}^{\infty} \frac{(\lambda T)^{i}}{i!} G^{(j)}(x) G^{(i+1)}(x)\left[\frac{G^{(j+1)}(x)}{G^{(j)}(x)}-\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}\right]
\end{aligned}
$$

It can be easily seen that the second term on the right-hand side of (3.35) is positive because $G^{(j+1)}(x) / G^{(j)}(x)$ is strictly decreasing. Changing the summation of $i$ and $j$, the first term on the right-hand side is

$$
\sum_{i=0}^{\infty} \frac{(\lambda T)^{i}}{i!} \sum_{j=i+1}^{\infty} \frac{(\lambda T)^{j}}{j!} G^{(j)}(x) G^{(i+1)}(x)\left[\frac{G^{(j+1)}(x)}{G^{(j)}(x)}-\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}\right]
$$Changing $i$ into $j$ with each other, the above equation is

$$
\begin{aligned}
& \sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \sum_{i=j+1}^{\infty} \frac{(\lambda T)^{i}}{i!} G^{(i)}(x) G^{(j+1)}(x)\left[\frac{G^{(i+1)}(x)}{G^{(i)}(x)}-\frac{G^{(j+2)}(x)}{G^{(j+1)}(x)}\right] \\
& =\sum_{j=1}^{\infty} \frac{(\lambda T)^{j-1}}{(j-1)!} \sum_{i=j}^{\infty} \frac{(\lambda T)^{i+1}}{(i+1)!} G^{(i+1)}(x) G^{(j)}(x)\left[\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}-\frac{G^{(j+1)}(x)}{G^{(j)}(x)}\right]
\end{aligned}
$$

Consequently, (3.35) is

$$
\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \sum_{i=j}^{\infty} \frac{(\lambda T)^{i}}{(i+1)!} G^{(j)}(x) G^{(i+1)}(x)\left[\frac{G^{(j+1)}(x)}{G^{(j)}(x)}-\frac{G^{(i+2)}(x)}{G^{(i+1)}(x)}\right](i+1-j)>0
$$

that completes the proof of that $Q(T)$ is strictly increasing.
From the above results, $Q(T)$ is strictly increasing from $\mathrm{e}^{-\mu K}$ to 1 when $G(x)=1-\mathrm{e}^{-\mu x}$. Thus, the left-hand side of (3.34) is also strictly increasing from 0 to $\mu K$. Therefore, if $c_{K}>c_{T}[1+(1 / \mu K)]+c_{0} / \mu$, then there exists a finite and unique $T^{*}$ that satisfies (3.34), and the resulting cost rate is

$$
\frac{C_{1}\left(T^{*}\right)}{\lambda}=\left(c_{K}-c_{T}-\frac{c_{0}}{\mu}\right) Q_{1}\left(T^{*}\right)+\frac{c_{0}}{\mu}
$$

Conversely, if $c_{K} \leq c_{T}[1+(1 / \mu K)]+c_{0} / \mu$, then $T^{*}=\infty$.
The expected cost rate for the replacement at shock $N$ is, from (3.32),

$$
\begin{aligned}
\frac{C_{2}(N)}{\lambda} & \equiv \lim _{\substack{T \rightarrow \infty \\
Z \rightarrow \infty}} \frac{C(T, N, Z)}{\lambda} \\
& =\frac{c_{K}-c_{0} / \mu-\left(c_{K}-c_{N}-c_{0} / \mu\right) G^{(N)}(K)}{\sum_{j=0}^{N-1} G^{(j)}(K)}+\frac{c_{0}}{\mu} \\
& (N=1,2, \ldots)
\end{aligned}
$$

that agrees with (3.20) in the exponential case by replacing $c_{K}$ with $c_{K}-c_{0} / \mu$. Because $Q_{2}(N)$ is strictly increasing to 1 , if $c_{K}>c_{N}[1+(1 / \mu K)]+c_{0} \mu$, then there exists a finite and unique minimum $N^{*}$ that minimizes $C_{2}(N)$.

Finally, the expected cost rate for the replacement at damage $Z$ is, from (3.32),

$$
\begin{aligned}
\frac{C_{3}(Z)}{\lambda} & \equiv \lim _{\substack{T \rightarrow \infty \\
N \rightarrow \infty}} \frac{C(T, N, Z)}{\lambda} \\
& =\frac{c_{K}-c_{0} / \mu-\left(c_{K}-c_{Z}-c_{0} / \mu\right)\left(1-\mathrm{e}^{-\mu(K-Z)}\right)}{1+\mu Z}+\frac{c_{0}}{\mu}
\end{aligned}
$$

Differentiating $C_{3}(Z)$ with respect to $Z$ and setting it equal to zero, for $c_{K}>$ $c_{Z}+c_{0} / \mu$,$$
\mu Z \mathrm{e}^{-\mu(K-Z)}=\frac{c_{Z}}{c_{K}-c_{Z}-c_{0} / \mu}
$$

The left-hand side of (3.39) is strictly increasing from 0 to $\mu K$. Thus, if $c_{K}>$ $c_{Z}[1+(1 / \mu K)]+c_{0} / \mu$, then there exists a finite and unique $Z^{*}\left(0<Z^{*}<K\right)$ that satisfies (3.39), and the resulting cost rate is

$$
\frac{C_{3}\left(Z^{*}\right)}{\lambda}=\frac{1}{\mu}\left(\frac{c_{Z}}{Z^{*}}+c_{0}\right)
$$

It is of great interest that the condition that a finite optimum value exists is given by the same form as $c_{K}>c_{k}[1+(1 / \mu K)]+c_{0} / \mu(k=T, N, Z)$. In general, $\mu K$ would be greater than $c_{k} /\left(c_{K}-c_{k}-c_{0} / \mu\right)$ because $\mu K$ represents the expected number of shocks before failure.

Example 3.2. We compute the optimum $T^{*}, N^{*}$, and $Z^{*}$ numerically. Table 3.2 presents the optimum $\lambda T^{*}$, the expected cost rate $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right)$, and $T^{*} / E\{Y\}=\lambda T^{*} /(1+\mu K)$ (see Example 2.2) for $\mu K=10,20$ and $c_{K} / c_{T}=2$, $5,10,20$ when $c_{0}=0$. If cost $c_{0}$ takes some positive value, then $c_{K}$ may be replaced with $c_{K}-c_{0} / \mu$. Furthermore, the ratio of $c_{K}$ to $c_{T}$ becomes one indicator of replacement time. We compute $\widetilde{T}$ that satisfies $c_{T} / c_{K}=T / E\{Y\}$, i.e., $\lambda \widetilde{T}=\left(c_{T} / c_{K}\right)(1+\mu K)$. This indicates that when $c_{K} / c_{T}=2$, the unit should be replaced before failure at time $\lambda T^{*}=9.02$ and $82.0 \%$ of the mean failure time. However, the approximate values $\widetilde{T}$ are too small to compare $T^{*}$, and hence, it would be useless practically.

Table 3.3 presents the optimum $N^{*}$, the expected cost rate $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right)$, and $N^{*} /\left[1+M_{G}(K)\right]=N^{*} /(1+\mu K)$ for $\mu K=10,20$ and $c_{N} / c_{T}=2,5$, 10,20 . In addition, we compute a minimum $\widetilde{N}$ that satisfies $c_{K} \bar{G}^{(N)}(K) \geq$ $c_{N} G^{(N)}(K)$. If the unit fails until the $N$ th shock, then it costs $c_{K}$, and otherwise, it costs $c_{N}$. The approximate values $\widetilde{N}$ show good upper bounds of $N^{*}$ when $\mu K=10$.

Table 3.4 presents the optimum $\mu Z^{*}$, the expected cost rate $C_{3}\left(Z^{*}\right) /\left(\lambda c_{Z}\right)$, and $Z^{*} /(K+1 / \mu)$ for $\mu K=10,20$ and $c_{Z} / c_{K}=2,5,10,20$. Furthermore, we compute $\mu \widetilde{Z}$ that satisfies $c_{Z} / c_{K}=Z /(K+1 / \mu)$, i.e., $\mu \widetilde{Z}=\left(c_{Z} / c_{K}\right)(1+\mu K)$ that agrees with $\lambda \widetilde{T}$ when $c_{Z}=c_{T}$, and $Z^{*}>\widetilde{Z}$. The expected costs $C_{3}\left(Z^{*}\right)$ are the smallest among three policies, as one expected. If costs $c_{K} / c_{k}(k=T$, $N, Z)$ are the same ones, the replacement policy where the unit is replaced at damage $Z$ is the best among the three policies.

If the replacement cost is $c_{K}+c_{0}(x)(x \geq K)$ when the total damage is $x$ and the unit is replaced at failure, then the expected cost rate in (3.32) is easily rewritten asTable 3.2. Optimum time $\lambda T^{*}$, expected cost rate $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right), T^{*} / E\{Y\}$, and approximate value $\lambda \widetilde{T}$ for $c_{K} / c_{T}$ and $\mu K$

| $c_{K} / c_{T}$ | $\mu K=10$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right)$ | $\lambda T^{*} /(1+\mu K)$ | $\lambda \widetilde{T}$ |
| 2 | 9.02 | 0.142 | 0.820 | 5.5 |
| 5 | 5.56 | 0.243 | 0.505 | 2.2 |
| 10 | 4.34 | 0.327 | 0.394 | 1.1 |
| 20 | 3.45 | 0.417 | 0.313 | 0.55 |
| $c_{K} / c_{T}$ | $\mu K=20$ |  |  |  |
|  | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right)$ | $\lambda T^{*} /(1+\mu K)$ | $\lambda \widetilde{T}$ |
| 2 | 15.74 | 0.066 | 0.749 | 10.5 |
| 5 | 11.30 | 0.089 | 0.538 | 4.2 |
| 10 | 9.59 | 0.106 | 0.457 | 2.1 |
| 20 | 8.33 | 0.122 | 0.400 | 1.05 |

Table 3.3. Optimum number $N^{*}$, expected cost rate $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right), N^{*} /(1+\mu K)$, and approximate value $\widetilde{N}$ for $c_{K} / c_{N}$ and $\mu K$

| $c_{K} / c_{N}$ | $\mu K=10$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right)$ | $N^{*} /(1+\mu K)$ | $\widetilde{N}$ |
| 2 | 9 | 0.156 | 0.818 | 10 |
| 5 | 6 | 0.213 | 0.545 | 8 |
| 10 | 5 | 0.253 | 0.455 | 7 |
| 20 | 4 | 0.300 | 0.364 | 6 |
| $c_{K} / c_{N}$ | $\mu K=20$ |  |  |  |
|  | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right)$ | $N^{*} /(1+\mu K)$ | $\widetilde{N}$ |
| 2 | 16 | 0.073 | 0.762 | 19 |
| 5 | 13 | 0.089 | 0.610 | 17 |
| 10 | 12 | 0.100 | 0.571 | 15 |
| 20 | 10 | 0.110 | 0.476 | 14 |

$$
\begin{aligned}
& c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{N-1}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z) \\
& -\left(c_{K}-c_{N}\right) F_{N}(T) G^{(N)}(Z) \\
& -\left(c_{K}-c_{Z}\right) \sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \\
& +\sum_{j=0}^{N-1} F_{j+1}(T) \int_{0}^{Z}\left[\int_{x}^{\infty} \bar{G}(y-x) \mathrm{d} c_{0}(y)\right] \mathrm{d} G^{(j)}(x) \\
& \sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t
\end{aligned}
$$Table 3.4. Optimum damage level $\mu Z^{*}$, expected cost rate $C_{3}\left(Z^{*}\right) /\left(\lambda c_{Z}\right), \mu Z^{*} /(1+$ $\mu K$ ), and approximate value $\widetilde{Z}$ for $c_{K} / c_{Z}$ and $\mu K$

| $c_{K} / c_{Z}$ | $\mu K=10$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $\mu Z^{*}$ | $C_{3}\left(Z^{*}\right) /\left(\lambda c_{Z}\right)$ | $\mu Z^{*} /(1+\mu K)$ | $\mu \widetilde{Z}$ |
| 2 | 7.93 | 0.126 | 0.721 | 5.5 |
| 5 | 6.71 | 0.149 | 0.610 | 2.2 |
| 10 | 6.01 | 0.166 | 0.546 | 1.1 |
| 20 | 5.37 | 0.186 | 0.489 | 0.55 |
| $c_{K} / c_{Z}$ | $\mu K=20$ |  |  |  |
|  | $\mu Z^{*}$ | $C_{3}\left(Z^{*}\right) /\left(\lambda c_{Z}\right)$ | $\mu Z^{*} /(1+\mu K)$ | $\mu \widetilde{Z}$ |
| 2 | 17.16 | 0.058 | 0.817 | 10.5 |
| 5 | 15.85 | 0.063 | 0.755 | 4.2 |
| 10 | 15.09 | 0.066 | 0.719 | 2.1 |
| 20 | 14.39 | 0.069 | 0.685 | 1.05 |

# (2) Replacement at Time $T$ or Damage $Z$ 

A unit is replaced before failure at time $T$ or at damage $Z$, whichever occurs first. Then, the expected cost rate when $c_{T}=c_{Z}$ is, from (3.8),

$$
C(T, Z)=\frac{c_{T}+\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{\infty} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
$$

Let $f_{j}(t)$ and $g^{(j)}(x)$ be the density functions of $F_{j}(t)$ and $G^{(j)}(x)$, respectively. Differentiating $C(T, Z)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
& Q_{1}(T, Z) \sum_{j=0}^{\infty} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t \\
& \quad-\sum_{j=0}^{\infty} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)=\frac{c_{T}}{c_{K}-c_{T}}
\end{aligned}
$$

where

$$
Q_{1}(T, Z) \equiv \frac{\sum_{j=0}^{\infty} f_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{\infty} G^{(j)}(Z)\left[F_{j}(T)-F_{j+1}(T)\right]}
$$

Furthermore, differentiating $C(T, Z)$ with respect to $Z$ and setting it equal to zero,$$
\begin{aligned}
& Q_{2}(T, Z) \bar{G}(K-Z) \sum_{j=0}^{\infty} G^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t \\
& \quad-\sum_{j=0}^{\infty} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)=\frac{c_{T}}{c_{K}-c_{T}}
\end{aligned}
$$

where

$$
Q_{2}(T, Z) \equiv \frac{\sum_{j=1}^{\infty} g^{(j)}(Z) F_{j+1}(T)}{\sum_{j=1}^{\infty} g^{(j)}(Z) \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
$$

In particular, when shocks occur in a Poisson process with rate $\lambda$, i.e., $F_{j}(t)=\sum_{i=j}^{\infty}\left[(\lambda t)^{i} / i!\right] \mathrm{e}^{-\lambda t}$, (3.43) and (3.44) are simplified, respectively, as follows:

$$
\begin{aligned}
& Q_{3}(T, Z) \sum_{j=0}^{\infty} F_{j+1}(T) G^{(j)}(Z) \\
& \quad-\sum_{j=0}^{\infty} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)=\frac{c_{T}}{c_{K}-c_{T}}
\end{aligned}
$$

where

$$
Q_{3}(T, Z) \equiv \frac{\sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z)}
$$

and

$$
\begin{aligned}
& \bar{G}(K-Z) \sum_{j=0}^{\infty} F_{j+1}(T) G^{(j)}(Z) \\
& \quad-\sum_{j=0}^{\infty} F_{j+1}(T) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)=\frac{c_{T}}{c_{K}-c_{T}}
\end{aligned}
$$

Hence, there does not exist both $T^{*}\left(0<T^{*}<\infty\right)$ and $Z^{*}\left(0<Z^{*}<K\right)$ that satisfy (3.45) and (3.46) simultaneously, because $Q_{3}(T, Z)<\bar{G}(K-Z)$ for $T>0$, so that we may determine optimum $T^{*}$ and $Z^{*}$ independently under these conditions as shown in Section 3.2, and adopt the policy with a lower cost.

# (3) Replacement at the Next Shock over Time $T$ 

It may be wasteful to replace an operating unit at planned times even if it is working. For example, when a unit is functioning for jobs with a variable working cycle and processing time, it would be better to do some maintenance after it has completed the work and process. The modified replacement modelwhere a unit is replaced at the next failure after time $T$ was considered [169], and the random maintenance model where it is replaced at random times was proposed in Section 9.3 of [1].

We consider the following modified replacement model: A unit is replaced before time $T$ when the total damage has exceeded a failure level $K$, and after $T$, it is replaced at the next shock. Then, the probability that the unit is replaced before failure is

$$
P_{T}=\sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j+1)}(K)
$$

and the probability that it is replaced at failure is

$$
P_{K}=\sum_{j=0}^{\infty} F_{j}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]
$$

where note that $(3.47)+(3.48)=1$. The mean time to replacement is, from (3.47) and (3.48),

$$
\begin{aligned}
& \sum_{j=0}^{\infty} G^{(j+1)}(K) \int_{0}^{T}\left[\int_{T-u}^{\infty}(t+u) \mathrm{d} F(t)\right] \mathrm{d} F_{j}(u) \\
& +\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right]\left\{\int_{0}^{T}\left[\int_{T-u}^{\infty}(t+u) \mathrm{d} F(t)\right] \mathrm{d} F_{j}(u)+\int_{0}^{T} t \mathrm{~d} F_{j+1}(t)\right\} \\
& =\frac{1}{\lambda} \sum_{j=0}^{\infty} G^{(j)}(K) F_{j}(T)
\end{aligned}
$$

Therefore, the expected cost rate is

$$
\begin{aligned}
\frac{\widetilde{C}_{1}(T)}{\lambda} & =\frac{c_{T} P_{T}+c_{K} P_{K}}{\sum_{j=0}^{\infty} G^{(j)}(K) F_{j}(T)} \\
& =\frac{c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty}\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j+1)}(K)}{\sum_{j=0}^{\infty} F_{j}(T) G^{(j)}(K)}
\end{aligned}
$$

When $T=0, \widetilde{C}_{1}(0)$ agrees with $C_{2}(1)$ in (3.21).
We derive an optimum time $T^{*}$ that minimizes $\widetilde{C}_{1}(T)$ when $F(t)=1-$ $\mathrm{e}^{-\lambda t}$ and $G(x)=1-\mathrm{e}^{-\mu x}$, i.e., $F_{j}(t)=\sum_{i=j}^{\infty}\left[(\lambda t)^{i} / i!\right] \mathrm{e}^{-\lambda t}$ and $G^{(j)}(x)=$ $\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}$. Then, differentiating $\widetilde{C}_{1}(T)$ in (3.50) with respect to $T$ and setting it equal to zero,

$$
\widetilde{Q}(T) \sum_{j=0}^{\infty} F_{j}(T) G^{(j)}(K)-\sum_{j=0}^{\infty} \frac{(\lambda T)^{j}}{j!} \mathrm{e}^{-\lambda T}\left[1-G^{(j+1)}(K)\right]=\frac{c_{T}}{c_{K}-c_{T}}
$$where

$$
\widetilde{Q}(T) \equiv \frac{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] \mathrm{e}^{-\lambda T}\left[(\mu K)^{j+1} /(j+1)!\right] \mathrm{e}^{-\mu K}}{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\right] \mathrm{e}^{-\lambda T} G^{(j+1)}(K)}
$$

Because $\widetilde{Q}(T)$ is strictly increasing in $T$ from $\mu K /\left(\mathrm{e}^{\mu K}-1\right)$ to 1 , the left-hand side of (3.51) is also strictly increasing from

$$
D \equiv \frac{\mu K-1+\mathrm{e}^{-\mu K}}{\mathrm{e}^{\mu K}-1} \leq \frac{\mu K}{2}
$$

to $\mu K$.
Therefore, we have the following optimum policy:
(i) If $D \geq c_{T} /\left(c_{K}-c_{T}\right)$, then $T^{*}=0$, i.e., the unit is replaced at the first shock, and the expected cost rate is given in (3.21).
(ii) If $D<c_{T} /\left(c_{K}-c_{T}\right)<\mu K$, then there exists a finite and unique $T^{*}$ that satisfies (3.51), and the resulting cost rate is

$$
\widetilde{C}_{1}\left(T^{*}\right)=\lambda\left(c_{K}-c_{T}\right) \widetilde{Q}\left(T^{*}\right)
$$

(iii) If $\mu K \leq c_{T} /\left(c_{K}-c_{T}\right)$, then $T^{*}=\infty$, i.e., the unit is replaced only at failure, and the expected cost rate is given in (3.12).

# (4) Replacement at the Next Shock over Damage $Z$ 

A unit is checked at each shock and the total damage is investigated only through inspection. If needed, it is replaced, as shown in (3) of Section 3.2. In addition, it may be better to replace a unit at the next shock time for prepare parts, workers, maintenance plans, and so on.

A unit is replaced when the total damage has exceeded a failure level $K$, and is also replaced at the next shock when the damage is between $Z$ and $K$. Then, the probability that the unit is replaced between $Z$ and $K$ is

$$
P_{Z}=\sum_{j=0}^{\infty} \int_{0}^{Z}\left[\int_{Z-x}^{K-x} G(K-x-y) \mathrm{d} G(y)\right] \mathrm{d} G^{(j)}(x)
$$

and the probability that it is replaced when the total damage has exceeded $K$ is

$$
P_{K}=\sum_{j=0}^{\infty} \int_{0}^{Z}\left[\int_{Z-x}^{K-x} \bar{G}(K-x-y) \mathrm{d} G(y)+\bar{G}(K-x)\right] \mathrm{d} G^{(j)}(x)
$$

where $(3.53)+(3.54)=1$. Furthermore, the mean time to replacement is, from (3.53) and (3.54),$$
\begin{aligned}
& \frac{1}{\lambda} \sum_{j=0}^{\infty}\left\{(j+2) \int_{0}^{Z}\left[\int_{Z-x}^{K-x} G(K-x-y) \mathrm{d} G(y)\right] \mathrm{d} G^{(j)}(x)\right. \\
& \left.\quad+\int_{0}^{Z}\left[(j+2) \int_{Z-x}^{K-x} \bar{G}(K-x-y) \mathrm{d} G(y)+(j+1) \bar{G}(K-x)\right] \mathrm{d} G^{(j)}(x)\right\} \\
& =\frac{1}{\lambda}\left[1+G(K)+\int_{0}^{Z} G(K-x) \mathrm{d} M_{G}(x)\right]
\end{aligned}
$$

Therefore, the expected cost rate is

$$
\begin{aligned}
\frac{\widetilde{C}_{3}(Z)}{\lambda}= & \frac{c_{Z} P_{Z}+c_{K} P_{K}}{1+G(K)+\int_{0}^{Z} G(K-x) \mathrm{d} M_{G}(x)} \\
& c_{K}-\left(c_{K}-c_{Z}\right)\left\{\int_{Z}^{K} G(K-x) \mathrm{d} G(x)\right. \\
= & \left.\frac{+\int_{0}^{Z}\left[\int_{Z-x}^{K-x} G(K-x-y) \mathrm{d} G(y)\right] \mathrm{d} M_{G}(x)}{1+G(K)+\int_{0}^{Z} G(K-x) \mathrm{d} M_{G}(x)}\right)
\end{aligned}
$$

In particular, when $G(x)=1-\mathrm{e}^{-\mu x}$,

$$
\frac{\widetilde{C}_{3}(Z)}{\lambda}=\frac{c_{K}-\left(c_{K}-c_{Z}\right)\left\{1-[1+\mu(K-Z)] \mathrm{e}^{-\mu(K-Z)}\right\}}{1+\mu Z+1-\mathrm{e}^{-\mu(K-Z)}}
$$

Differentiating $\widetilde{C}_{3}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\mathrm{e}^{-\mu(K-Z)}\left[\frac{(1+\mu Z) \mu(K-Z)}{1-\mathrm{e}^{-\mu(K-Z)}}-1\right]=\frac{c_{Z}}{c_{K}-c_{Z}}
$$

The left-hand side of (3.58) is strictly increasing in $Z$ from $D$ to $\mu K$. Therefore, we have the following optimum policy:
(i) If $D \geq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=0$, and the expected cost rate is

$$
\frac{\widetilde{C}_{3}(0)}{\lambda}=\frac{c_{K}-\left(c_{K}-c_{Z}\right)\left[1-(1+\mu K) \mathrm{e}^{-\mu K}\right]}{2-\mathrm{e}^{-\mu K}}
$$

(ii) If $D<c_{Z} /\left(c_{K}-c_{Z}\right)<\mu K$, then there exists a finite and unique $Z^{*}$ $\left(0<Z^{*}<K\right)$ that satisfies (3.58), and the expected cost rate is

$$
\frac{\widetilde{C}_{3}\left(Z^{*}\right)}{\lambda}=\frac{\left(c_{K}-c_{Z}\right) \mu\left(K-Z^{*}\right) \mathrm{e}^{-\mu\left(K-Z^{*}\right)}}{1-\mathrm{e}^{-\mu\left(K-Z^{*}\right)}}
$$

(iii) If $\mu K \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$, and the expected cost rate is given in (3.12).It is of great interest that the condition for an optimum $Z^{*}$ to exist is the same as that of (3). Furthermore, compared (3.58) with (3.39), because

$$
\frac{(1+\mu Z) \mu(K-Z)}{1-\mathrm{e}^{-\mu(K-Z)}}>1+\mu Z
$$

the optimum $Z^{*}$ to satisfy (3.58) is smaller than that to satisfy (3.39), as one expected.

# (5) Replacement at $n$ Damage Levels 

A unit is replaced before failure at damage $Z_{i}(i=1,2, \ldots, n)$, where $Z_{n+1} \equiv K$, and its replacement cost is $c_{i}$. Then, the probability that the unit is replaced at damage $Z_{i}$ is

$$
\begin{aligned}
P_{i} & =\sum_{j=0}^{\infty} \int_{0}^{Z_{1}}\left[G\left(Z_{i+1}-x\right)-G\left(Z_{i}-x\right)\right] \mathrm{d} G^{(j)}(x) \\
& =G\left(Z_{i+1}\right)-G\left(Z_{i}\right)+\int_{0}^{Z_{1}}\left[G\left(Z_{i+1}-x\right)-G\left(Z_{i}-x\right)\right] \mathrm{d} M_{G}(x) \\
& (i=1,2, \ldots, n)
\end{aligned}
$$

and the probability that it is replaced at failure is

$$
P_{K}=\bar{G}(K)+\int_{0}^{Z_{1}} \bar{G}(K-x) \mathrm{d} M_{G}(x)
$$

where note that $\sum_{i=1}^{n} P_{i}+P_{K}=1$. Because the mean time to replacement is given by the denominator of (3.24), the expected cost rate is

$$
\begin{aligned}
& \frac{C\left(Z_{1}, Z_{2}, \cdots, Z_{n}\right)}{\lambda}=\frac{c_{K} P_{K}+\sum_{i=1}^{n} c_{i} P_{i}}{1+M_{G}\left(Z_{1}\right)} \\
& =\frac{c_{K}-\sum_{i=1}^{n}\left(c_{K}-c_{i}\right)\left\{G\left(Z_{i+1}\right)-G\left(Z_{i}\right)+\int_{0}^{Z_{1}}\left[G\left(Z_{i+1}-x\right)-G\left(Z_{i}-x\right)\right] \mathrm{d} M_{G}(x)\right\}}{1+M_{G}\left(Z_{1}\right)}
\end{aligned}
$$

that agrees with (3.24) for $n=1$ when $Z_{1}=Z$.
Next, a unit fails when the total damage has exceeded a failure level $K_{i}$, where $K_{i}<K_{i+1}$ and $K_{\infty} \equiv \infty(i=1,2, \ldots)$, and its required cost is $c_{i}$ with $c_{i} \leq c_{i+1}$. If the unit is replaced before at damage $Z\left(Z \leq K_{1}\right)$, then its probability is

$$
P_{Z}=\sum_{j=0}^{\infty} \int_{0}^{Z}\left[G\left(K_{1}-x\right)-G(Z-x)\right] \mathrm{d} G^{(j)}(x)
$$

and the probability that it is replaced at failure level $K_{i}$ is$$
P_{i}=\sum_{j=0}^{\infty} \int_{0}^{Z}\left[G\left(K_{i+1}-x\right)-G\left(K_{i}-x\right)\right] \mathrm{d} G^{(j)}(x) \quad(i=1,2, \ldots)
$$

where $P_{Z}+\sum_{i=1}^{\infty} P_{i}=1$. Thus, the expected cost rate is

$$
\begin{aligned}
\frac{C(Z)}{\lambda}= & \frac{c_{Z} P_{Z}+\sum_{i=1}^{\infty} c_{i} P_{i}}{1+M_{G}(Z)} \\
& c_{Z}+\sum_{i=1}^{\infty}\left(c_{i}-c_{Z}\right)\left\{G\left(K_{i+1}\right)-G\left(K_{i}\right)\right. \\
= & \frac{\left.+\int_{0}^{Z}\left[G\left(K_{i+1}-x\right)-G\left(K_{i}-x\right)\right] \mathrm{d} M_{G}(x)\right\}}{1+M_{G}(Z)}
\end{aligned}
$$

Differentiating $C(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\sum_{i=1}^{\infty}\left(c_{i}-c_{i-1}\right) \int_{K_{i}-Z}^{K_{i}}\left[1+M_{G}\left(K_{i}-x\right)\right] \mathrm{d} G(x)=c_{Z}
$$

where $c_{0} \equiv c_{Z}<c_{1}$. Thus, if $M_{G}\left(K_{1}\right)>c_{Z} /\left(c_{1}-c_{Z}\right)$, then there exists a finite and unique $Z^{*}\left(0<Z^{*}<K_{1}\right)$ that satisfies (3.67), and it is smaller than that to satisfy (3.25).

# (6) Random Replacement Interval 

Suppose that a unit is also replaced at random time $R$ with a general distribution $\gamma(t)$ for the same policy in Section 3.1. This corresponds to the model where a unit is replaced at the same random times as its working times (see Section 9.3 in [1]).

By a method similar to obtaining (3.1)-(3.4), the probability that the unit is replaced at time $T$ is

$$
P_{T}=\sum_{j=0}^{N-1} \bar{\gamma}(T)\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z)
$$

the probability that it is replaced at shock $N$ is

$$
P_{N}=\int_{0}^{T} \bar{\gamma}(t) \mathrm{d} F_{N}(t) G^{(N)}(Z)
$$

the probability that it is replaced at damage $Z$ is

$$
P_{Z}=\sum_{j=0}^{N-1} \int_{0}^{T} \bar{\gamma}(t) \mathrm{d} F_{j+1}(t) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x)
$$

the probability that it is replaced at damage $K$ is$$
P_{K}=\sum_{j=0}^{N-1} \int_{0}^{T} \bar{\gamma}(t) \mathrm{d} F_{j+1}(t) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x)
$$

and the probability that it is replaced at random time $R$ is

$$
P_{R}=\sum_{j=0}^{N-1} \int_{0}^{T}\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} \gamma(t) G^{(j)}(Z)
$$

where $\bar{\gamma}(t) \equiv 1-\gamma(t)$ and $P_{T}+P_{N}+P_{Z}+P_{K}+P_{R}=1$. Similarly, the mean time to replacement is

$$
\begin{aligned}
& T \sum_{j=0}^{N-1} \bar{\gamma}(T)\left[F_{j}(T)-F_{j+1}(T)\right] G^{(j)}(Z)+\int_{0}^{T} t \bar{\gamma}(t) \mathrm{d} F_{N}(t) G^{(N)}(Z) \\
& \quad+\sum_{j=0}^{N-1} \int_{0}^{T} t \bar{\gamma}(t) \mathrm{d} F_{j+1}(t) \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \\
& \quad+\sum_{j=0}^{N-1} \int_{0}^{T} t \bar{\gamma}(t) \mathrm{d} F_{j+1}(t) \int_{0}^{Z} \bar{G}(K-x) \mathrm{d} G^{(j)}(x) \\
& \quad+\sum_{j=0}^{N-1} \int_{0}^{T} t\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} \gamma(t) G^{(j)}(Z) \\
& =\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T} \bar{\gamma}(t)\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t
\end{aligned}
$$

Let $c_{R}$ be the replacement cost at random time $R$ and $c_{T}, c_{N}, c_{Z}$, and $c_{K}$ be the same costs given in (3.6). Then, the expected cost rate is

$$
C(T, N, Z, R)=\frac{c_{T} P_{T}+c_{N} P_{N}+c_{Z} P_{Z}+c_{K} P_{K}+c_{R} P_{R}}{\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T} \bar{\gamma}(t)\left[F_{j}(t)-F_{j+1}(t)\right] \mathrm{d} t}
$$

that agrees with (3.8) when $\bar{\gamma}(t) \equiv 1$.# Replacement of Multiunit Systems 

In general, a system consists of a variety of units. In (4) of Section 2.4, we have considered a system with $n$ different units and derived the first-passage time distributions to system failure. If a system consists of a series system, then we may consider a maintenance policy before the first failure of units. If a system consists of a parallel system, then we may consider a maintenance policy before the last failure of units. But, in general, it would be difficult to discuss analytically optimum maintenance policies for shock and damage models of multiunit systems. A conditioned-based maintenance of a two-unit series system whose deterioration is monitored at periodic times was considered, and its optimum policy was discussed, using dynamic programming [170].

In Section 4.1, we take up a parallel system with $n$ identical units that are situated in a random environment, as shown in Example 1.2. Each unit fails successively from shocks in a random environment, and finally, the system fails when all units have failed at some shock. For such units, we consider the two cases where the probability of unit failure is constant at any shock and its probability depends on the number of shocks. As the preventive replacement, the system is replaced before system failure when the total number of failed units is $N+1, N+2, \cdots, n-1$ at some shock. Introducing replacement costs, we obtain the expected cost rates for the two cases and derive optimum numbers $N^{*}$ that minimize them. Furthermore, we apply the replacement model to a damage model where each unit fails when the damage due to shocks has exceeded a failure level $K$. On the other hand, we consider the replacement model of a $k$-out-of- $n$ system that is replaced at a shock number $N$ and obtain the expected cost rate.

In multiunit redundant systems, the failure of some units may affect one or more of the remaining units. This is called failure interaction. Two types of induced failure and shock damage are defined [171]. In Section 4.2, we consider a two-unit system with unit 1 and unit 2 , where unit 2 fails with some probability at the $j$ th time of unit 1 failure (induced failure), and it causes an amount of damage to unit 2 (shock damage). As the replacement policy, the system is replaced at the $N$ th failure of unit 1 or at the failure ofunit 2 , whichever occurs first. We obtain the expected cost rates for the two types of failure interaction and derive optimum numbers $N^{*}$ that minimize them. Furthermore, we propose two extended models where the system is replaced at a planned time $T$ or (1) at the $N$ th failure of unit 1 and (2) at a damage level $Z$ of unit 2 .

# 4.1 Parallel System in a Random Environment 

Consider a standard parallel redundant system that consists of $n$ identical units and fails when all units have failed. The system is situated in a random environment that generates shocks according to a general distribution $F(t)$ with finite mean $1 / \lambda$. Each unit fails from shocks, independently of the other units. The failure distribution and the mean time to system failure have been derived in Example 1.2.

We consider the following three cases: The probability that each unit fails is constant $p$ at all shocks, the probability that it fails at the $j$ th shock is $p(j)$ that depends on the number of shocks, and the probability that it fails until the $j$ th shock is $1-G^{(j)}(K)$. Then, the system is replaced before system failure when the total number of failed units is $N+1, N+2, \cdots, n-1$, and it is replaced when all units have failed, otherwise, it is left alone. For such replacement models, we introduce the replacement costs: Cost $c_{n}$ is incurred when the failed system is replaced, and cost $c_{N}\left(c_{N}<c_{n}\right)$ is incurred when the system with $m(m=N+1, N+2, \cdots, n-1)$ failed units is replaced before system failure. Furthermore, we consider an additional replacement cost that is a linear function of failed units. Under these assumptions, we derive optimum numbers $N^{*}$ that minimize the expected cost rates for the three models.

### 4.1.1 Replacement Model

Consider a parallel system with $n(\geq 2)$ identical units, each of which fails at shocks with probability $p(0<p \leq 1)$, where $q \equiv 1-p$ [52]. Shocks occur in a renewal process with mean interval time $1 / \lambda$. Let $W_{j}$ be the total number of units that fail at the $j$ th $(j=1,2, \cdots)$ shock, where $W_{0} \equiv 0$. Then, the probability that the system is replaced after failure is$$
\begin{aligned}
P_{n} \equiv & \operatorname{Pr}\left\{W_{1}=n\right\}+\sum_{j=2}^{\infty} \sum_{r=0}^{N} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j}=n\right\} \\
= & p^{n}+p^{n} \sum_{j=2}^{\infty} \sum_{r=0}^{N} \sum_{i_{1}+i_{2}+\cdots+i_{j-1}=r}\binom{n}{i_{1}} q^{n-i_{1}}\binom{n-i_{1}}{i_{2}} q^{n-i_{1}-i_{2}} \\
& \cdots\binom{n-i_{1}-i_{2}-\cdots-i_{j-2}}{i_{j-1}} q^{n-i_{1}-i_{2}-\cdots-i_{j-1}} \\
= & p^{n}+p^{n} \sum_{j=2}^{\infty} \sum_{r=0}^{N}\binom{n}{r}\left(q^{j}\right)^{n-r}\left(1+q+\cdots+q^{j-1}\right)^{r} \\
= & \sum_{r=0}^{N}\binom{n}{r} p^{n-r} \sum_{i=0}^{r}\binom{r}{i}(-1)^{i} \sum_{j=0}^{\infty}\left(q^{n-r+i}\right)^{j} \\
= & \sum_{r=0}^{N}\binom{n}{r}(-1)^{r} p^{n-r} \sum_{i=0}^{r}\binom{r}{i}(-1)^{i} \frac{1}{1-q^{n-i}}
\end{aligned}
$$

Similarly, the probability that the system is replaced before failure is

$$
\begin{aligned}
P_{N} \equiv & \operatorname{Pr}\left\{N+1 \leq W_{1} \leq n-1\right\} \\
& +\sum_{j=2}^{\infty} \sum_{r=0}^{N} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } N+1 \leq W_{1}+W_{2}+\cdots+W_{j} \leq n-1\right\} \\
= & \sum_{r=N+1}^{n-1}\binom{n}{r}(-1)^{r} p^{n-r} \sum_{i=0}^{r}\binom{r}{i}(-1)^{i} \frac{1}{1-q^{n-i}}
\end{aligned}
$$

where $P_{n}+P_{N}=1$. For the derivations of (4.1) and (4.2), refer to the next sections.

Furthermore, the mean time to replacement, i.e., the mean time that the total number of failed units has exceeded $N+1$ for the first time at some shock is

$$
\begin{aligned}
l_{N+1} & =\sum_{j=1}^{\infty} \frac{j}{\lambda} \sum_{r=0}^{N} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j} \geq N+1\right\} \\
& =\frac{1}{\lambda} \sum_{r=0}^{N}\binom{n}{r}(-1)^{r} \sum_{i=0}^{N-r}\binom{n-r}{i} \frac{1}{1-q^{n-i}} \quad(N=0,1,2, \ldots, n-1)
\end{aligned}
$$

It is also equal to the mean time to failure of an $(N+1)$-out-of- $n$ system that fails if and only if at least $N+1$ of $n$ units fail. In particular, when $N=n-1$,(4.3) is simplified as

$$
l_{n}=\frac{1}{\lambda} \sum_{i=1}^{n}\binom{n}{i} \frac{(-1)^{i+1}}{1-q^{i}}
$$

that is the mean time to failure of an $n$-unit parallel system in Example 1.2.
Therefore, the expected cost rate is

$$
\begin{aligned}
\frac{C_{1}(N)}{\lambda} & =\frac{c_{n} P_{n}+c_{N} P_{N}}{\lambda l_{N+1}} \\
& =\frac{c_{N}+\left(c_{n}-c_{N}\right) \sum_{r=0}^{N}\binom{n}{r}(-1)^{r} p^{n-r} \sum_{i=0}^{r}\binom{r}{i}(-1)^{i}\left[1 /\left(1-q^{n-i}\right)\right]}{\sum_{r=0}^{N}\binom{n}{r}(-1)^{r} \sum_{i=0}^{N-r}\binom{n-r}{i}\left[1 /\left(1-q^{n-i}\right)\right]} \\
& (N=0,1,2, \cdots, n-1)
\end{aligned}
$$

It is evident that

$$
\begin{aligned}
\frac{C_{1}(n-1)}{\lambda} & =\frac{c_{n}}{\sum_{i=1}^{n}\binom{n}{i}(-1)^{i+1}\left[1 /\left(1-q^{i}\right)\right]} \\
\frac{C_{1}(0)}{\lambda} & =c_{n} p^{n}+c_{N}\left(1-p^{n}-q^{n}\right)
\end{aligned}
$$

Thus, when the number $n$ of units is given, we can determine an optimum number $N^{*}$ that minimizes $C_{1}(N)$ by comparing it for $N=0,1, \cdots, n-1$. For example, when $n=2$,

$$
\begin{aligned}
& \frac{C_{1}(0)}{\lambda}=c_{n} p^{2}+2 c_{N} p q \\
& \frac{C_{1}(1)}{\lambda}=\frac{c_{n}\left(1-q^{2}\right)}{1+2 q}
\end{aligned}
$$

Hence, if $q /(1+2 q)>c_{N} / c_{n}$, then $N^{*}=0$, i.e., the system is replaced when only one unit has failed. If $q /(1+2 q) \leq c_{N} / c_{n}$, then $N^{*}=1$, i.e., it is replaced when two units have failed. In addition, because $q /(1+2 q) \leq 1 / 3$, if $c_{n} \leq 3 c_{N}$, then $N^{*}=1$.

Example 4.1. Table 4.1 presents the optimum number $N^{*}$ for $n=2,4,8$, 15,20 and $p=0.01,0.05,0.10,0.20,0.30,0.40,0.50$ when $c_{N} / c_{n}=0.1$. It is natural that the optimum $N^{*}$ is decreasing in $p$ and increasing in $n$. For example, if the total number of failed units is 6 or 7 at some shock when $n=8$ and $p=0.10$, then the system should be replaced before failure. In particular, when $n=2$, if $p<0.875$, then $N^{*}=0$.

# 4.1.2 Extended Replacement Models 

It is assumed in the same model, as that of Section 4.1.1, that the probability that an operating unit fails at the $j$ th shock is $p(j)(j=1,2, \cdots)$, dependingTable 4.1. Optimum number $N^{*}$ of a parallel system with $n$ units when $c_{N} / c_{n}=0.1$

| $p$ | $n$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 2 | 4 | 8 | 15 | 20 |
| 0.01 | 0 | 2 | 6 | 13 | 18 |
| 0.05 | 0 | 2 | 6 | 13 | 18 |
| 0.10 | 0 | 2 | 5 | 12 | 17 |
| 0.20 | 0 | 2 | 5 | 12 | 17 |
| 0.30 | 0 | 1 | 5 | 11 | 16 |
| 0.40 | 0 | 1 | 4 | 11 | 16 |
| 0.50 | 0 | 1 | 4 | 10 | 15 |

on the number of shocks [53]. This assumption is more reasonable because the damage due to shocks would be additive and the failure rate would increase with time. In addition, cost $n c_{0}+c_{n}$ is incurred when a failed system is replaced, where costs $c_{0}$ and $c_{n}$ include all costs resulting from the failure and replacement of one unit and the system, respectively. Cost $m c_{0}+c_{N}$ is incurred when $m(m=N+1, N+2, \cdots, n-1)$ units have failed and the system is replaced before its failure. Let $P(j) \equiv \sum_{i=1}^{j} p(i)(j=1,2, \cdots)$ be the probability that each unit fails until the $j$ th shock, where $P(0) \equiv 0$. First, by a method similar to obtaining (4.3), the mean time to system failure is

$$
\begin{aligned}
l_{n}= & \sum_{j=1}^{\infty} \frac{j}{\lambda} \sum_{r=0}^{n-1} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j}=n\right\} \\
= & \sum_{j=1}^{\infty} \frac{j}{\lambda} \sum_{r=0}^{n-1}\binom{n}{r}[p(j)]^{n-r}[P(j-1)]^{r} \\
= & \frac{1}{\lambda} \sum_{j=0}^{\infty}\left\{1-[P(j)]^{n}\right\} \\
= & \frac{1}{\lambda} \sum_{i=1}^{n}\binom{n}{i}(-1)^{i+1} \sum_{j=0}^{\infty}[\bar{P}(j)]^{i}
\end{aligned}
$$

where $\bar{P}(j) \equiv 1-P(j)$. For example, when $\bar{P}(j)=(q)^{j^{\alpha}}(\alpha>0)$, i.e., each unit fails according to a discrete Weibull distribution (see Section 1.2 of [1]),

$$
l_{n}=\frac{1}{\lambda} \sum_{i=1}^{n}\binom{n}{i}(-1)^{i+1} \sum_{j=0}^{\infty}\left[(q)^{j^{\alpha}}\right]^{i}
$$

In the particular case of $\alpha=1, l_{n}$ is equal to (4.4).
We obtain the expected cost rate. Let $P_{m}$ be the probability that the total number of units failed at some shock becomes $m(m=N+1, N+2, \cdots, n)$and hence, the system is replaced. Then,

$$
\begin{aligned}
P_{m}= & \sum_{j=1}^{\infty} \sum_{r=0}^{N} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j}=m\right\} \\
= & \sum_{j=1}^{\infty}\binom{n}{m}[\bar{P}(j)]^{n-m} \sum_{r=0}^{N}\binom{m}{r}[p(j)]^{m-r}[P(j-1)]^{r} \\
& (m=N+1, N+2, \ldots, n)
\end{aligned}
$$

where $\sum_{m=N+1}^{n} P_{m}=1$. Furthermore, in a similar way of obtaining (4.8), the mean time to replacement, i.e., the mean time that the total number of failed units exceeds $N+1$ for the first time is

$$
\begin{aligned}
l_{N+1}= & \sum_{j=1}^{\infty} \frac{j}{\lambda} \sum_{m=N+1}^{n} \sum_{r=0}^{N} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j}=m\right\} \\
= & \sum_{j=1}^{\infty} \frac{j}{\lambda} \sum_{m=N+1}^{n}\binom{n}{m}[\bar{P}(j)]^{n-m} \sum_{r=0}^{N}\binom{m}{r}[p(j)]^{m-r}[P(j-1)]^{r} \\
= & \frac{1}{\lambda} \sum_{j=0}^{\infty} \sum_{m=0}^{N}\binom{n}{m}[\bar{P}(j)]^{n-m}[P(j)]^{m}
\end{aligned}
$$

Thus, the expected cost rate is

$$
\begin{aligned}
C_{2}(N) & =\frac{\left(c_{0} n+c_{n}\right) P_{n}+\sum_{m=N+1}^{n-1}\left(c_{0} m+c_{N}\right) P_{m}}{\text { mean time to replacement }} \\
& =\frac{c_{N}+\left(c_{n}-c_{N}\right) P_{n}+c_{0} \sum_{m=N+1}^{n} m P_{m}}{l_{N+1}}
\end{aligned}
$$

Therefore, from (4.10) and (4.11),

$$
\begin{aligned}
& c_{N}+\left(c_{n}-c_{N}\right) \sum_{j=1}^{\infty} \sum_{r=0}^{N}\binom{n}{r}[p(j)]^{n-r}[P(j-1)]^{r} \\
& \frac{C_{2}(N)}{\lambda}=\frac{+c_{0} n \sum_{j=1}^{\infty} \sum_{m=N+1}^{n}\binom{n-1}{m-1}[\bar{P}(j)]^{n-m} \sum_{r=0}^{N}\binom{m}{r}[p(j)]^{m-r}[P(j-1)]^{r}}{\sum_{j=0}^{\infty} \sum_{m=0}^{N}\binom{n}{m}[\bar{P}(j)]^{n-m}[P(j)]^{m}} \\
& (N=0,1,2, \cdots, n-1) .
\end{aligned}
$$

It is clearly seen that

$$
\begin{aligned}
\frac{C_{2}(n-1)}{\lambda} & =\frac{c_{0} n+c_{n}}{\sum_{j=0}^{\infty}\{1-[P(j)]^{n}\}} \\
\frac{C_{2}(0)}{\lambda} & =\frac{c_{N}+\left(c_{n}-c_{N}\right) \sum_{j=1}^{\infty}[p(j)]^{n}+c_{0} n \sum_{j=1}^{\infty} p(j)[\bar{P}(j-1)]^{n-1}}{\sum_{j=0}^{\infty}[\bar{P}(j)]^{n}}
\end{aligned}
$$Table 4.2. Optimum number $N^{*}$ of a parallel system with $n$ units when $c_{0} / c_{n}=$ 0.05 and $c_{N} / c_{n}=0.1$

| $p$ | $n$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 2 | 4 | 8 | 15 | 20 |
| 0.01 | 0 | 2 | 7 | 14 | 19 |
| 0.05 | 0 | 2 | 6 | 14 | 19 |
| 0.10 | 0 | 2 | 6 | 14 | 19 |
| 0.20 | 0 | 2 | 6 | 13 | 19 |
| 0.30 | 0 | 1 | 5 | 13 | 18 |
| 0.40 | 0 | 1 | 5 | 12 | 18 |
| 0.50 | 0 | 1 | 5 | 12 | 17 |

that represents the expected cost for an $n$-unit parallel system and an $n$-unit series system when $c_{n}=c_{N}$, respectively.

If $n$ and $p(j)$ are given, we can determine an optimum number $N^{*}$ that minimizes the expected cost $C_{2}(N)$ in (4.12) by comparing $N=0,1,2, \cdots, n-$ 1. If $p(j)$ is a geometric distribution, i.e., $p(j)=p q^{j-1}$ and $P(j)=1-q^{j}$ $(p \equiv 1-q>0)$, then

$$
\begin{gathered}
c_{N}+\left(c_{n}-c_{N}\right) \sum_{r=0}^{N}\binom{n}{r}(-1)^{r} p^{n-r} \sum_{i=0}^{r}\binom{r}{i}(-1)^{i}\left[1 /\left(1-q^{n-i}\right)\right] \\
\frac{C_{2}(N)}{\lambda}=\frac{+c_{0} n p \sum_{r=0}^{N}\binom{n-1}{r}(-1)^{r} \sum_{i=0}^{N-r}\binom{n-1-r}{i}\left[1 /\left(1-q^{n-i}\right)\right]}{\sum_{r=0}^{N}\binom{n}{r}(-1)^{r} \sum_{i=0}^{N-r}\binom{n-r}{i}\left[1 /\left(1-q^{n-i}\right)\right]} \\
(N=0,1,2, \cdots n-1)
\end{gathered}
$$

In this case, if $c_{0}=0$, then the above result agrees with (4.5).

Example 4.2. Suppose that the failure distribution is a negative binomial distribution with a shape parameter 2, i.e., $p(j)=j p^{2} q^{j-1}(j=1,2, \cdots)$ where $q \equiv 1-p$. Table 4.2 presents the optimum number $N^{*}$ that minimizes the expected cost $C_{2}(N)$ for several $n$ and $p$ when $c_{0} / c_{n}=0.05$ and $c_{N} / c_{n}=$ 0.1 . This indicates that the values of $N^{*}$ are not less than those of Table 4.1 for the same $p$ and $n$.

Next, we apply the previous replacement model to a damage model. Suppose that the total damage is not additive and each unit fails when the damage due to some shock has exceeded a failure level $K$. We consider an independent damage model discussed in Section 2.2: Shocks occur in a renewal process with finite mean $1 / \lambda$. The damage $W_{j}$ due to each shock has an identical distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$ and the total damage is not additive, i.e., each unit fails with probability $[G(K)]^{j-1}-[G(K)]^{j}$ at shock $j(j=1,2, \cdots)$. Then, replacing $p=\bar{G}(K)$ formally in (4.5), the expected cost rate for a parallel system is$$
\begin{gathered}
c_{N}+\left(c_{n}-c_{N}\right) \sum_{r=0}^{N}\binom{n}{r}(-1)^{r}[\bar{G}(K)]^{n-r} \\
\frac{C_{1}(N)}{\lambda}=\frac{\times \sum_{i=0}^{r}\binom{r}{i}(-1)^{i}\left[1 /\{1-[G(K)]^{n-i}\}\right]}{\sum_{r=0}^{N}\binom{n}{r}(-1)^{r} \sum_{i=0}^{N-r}\binom{n-r}{i}\left[1 /\{1-[G(K)]^{n-i}\}\right]} \\
(N=0,1,2, \cdots, n-1)
\end{gathered}
$$

On the other hand, the total damage is additive, i.e., each unit fails with probability $G^{(j-1)}(K)-G^{(j)}(K)$ at shock $j(j=1,2, \cdots)$. Then, replacing $p(j)=G^{(j-1)}(K)-G^{(j)}(K)$ and $P(j)=1-G^{(j)}(K)$ formally in (4.12), the expected cost rate is

$$
\begin{gathered}
c_{N}+\left(c_{n}-c_{N}\right) \sum_{j=1}^{\infty} \sum_{r=0}^{N}\binom{n}{r}\left[G^{(j-1)}(K)-G^{(j)}(K)\right]^{n-r} \\
\times\left[1-G^{(j-1)}(K)\right]^{r}+c_{0} n \sum_{j=1}^{\infty} \sum_{m=N+1}^{\infty}\binom{n-1}{m-1}\left[G^{(j)}(K)\right]^{n-m} \\
\frac{C_{2}(N)}{\lambda}=\frac{\times \sum_{r=0}^{N}\binom{m}{r}\left[G^{(j-1)}(K)-G^{(j)}(K)\right]^{m-r}\left[1-G^{(j-1)}(K)\right]^{r}}{\sum_{j=0}^{\infty} \sum_{r=0}^{N}\binom{n}{r}\left[G^{(j)}(K)\right]^{n-r}\left[1-G^{(j)}(K)\right]^{r}} \\
(N=0,1,2, \cdots, n-1)
\end{gathered}
$$

# 4.1.3 Replacement at Shock Number 

Suppose in the same model as that of Section 4.1.2 that the system is replaced at a shock number $N(N=1,2, \cdots)$ or at a system failure, whichever occurs first. Then, the probability that the system is replaced at failure until shock $N$ is

$$
\begin{aligned}
& \sum_{j=1}^{N} \sum_{r=0}^{n-1} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r \text { and } W_{1}+W_{2}+\cdots+W_{j}=n\right\} \\
& =\sum_{j=1}^{N} \sum_{r=0}^{n-1}\binom{n}{r}[p(j)]^{n-r}[P(j-1)]^{r}=[P(N)]^{n}
\end{aligned}
$$

and the probability that it is replaced before failure at shock $N$ is

$$
\begin{aligned}
\sum_{r=0}^{n-1} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{N}=r\right\} & =\sum_{r=0}^{n-1}\binom{n}{r}[\bar{P}(N)]^{n-r}[P(N)]^{r} \\
& =1-[P(N)]^{n}
\end{aligned}
$$

Similarly, the mean time to replacement is

$$
\begin{aligned}
& \sum_{j=1}^{N} \frac{j}{\lambda} \sum_{r=0}^{n-1}\binom{n}{r}[p(j)]^{n-r}[P(j-1)]^{r}+N\left\{1-[P(N)]^{n}\right\} \\
& =\frac{1}{\lambda} \sum_{j=0}^{N-1}\left\{1-[P(j)]^{n}\right\}
\end{aligned}
$$and the expected number of failed units until replacement is

$$
\sum_{r=0}^{n} r\binom{n}{r}[\bar{P}(N)]^{n-r}[P(N)]^{r}=n P(N)
$$

Therefore, the expected cost rate is

$$
\frac{\widetilde{C}_{2}(N)}{\lambda}=\frac{c_{N}+\left(c_{n}-c_{N}\right)[P(N)]^{n}+c_{0} n P(N)}{\sum_{j=0}^{N-1}\left\{1-[P(j)]^{n}\right\}} \quad(N=1,2, \cdots)
$$

Next, consider a $k$-out-of- $n$ system that fails when the total number of failed units is more than $k$ at some shock. Then, in a way similar to obtaining (4.21), the probability that the system is replaced at failure is

$$
\begin{aligned}
& \sum_{j=1}^{N} \sum_{m=k+1}^{n} \sum_{r=0}^{k} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\quad \text { and } W_{1}+W_{2}+\cdots+W_{j}=m\right\} \\
& =\sum_{j=1}^{N} \sum_{m=k+1}^{n}\binom{n}{m}[\bar{P}(j)]^{n-m} \sum_{r=0}^{k}\binom{m}{r}[P(j-1)]^{r}[p(j)]^{m-r} \\
& =\sum_{j=1}^{N} \sum_{m=k+1}^{n}\binom{n}{m}\left\{[\bar{P}(j)]^{n-m}[P(j)]^{m}-[\bar{P}(j-1)]^{n-m}\left[P(j-1)^{m}\right]\right\} \\
& =\sum_{m=k+1}^{n}\binom{n}{m}[\bar{P}(N)]^{n-m}[P(N)]^{m}
\end{aligned}
$$

and the probability that it is replaced at shock $N$ is

$$
\begin{aligned}
& \sum_{m=0}^{k} \sum_{r=0}^{k} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{N-1}=r \text { and } W_{1}+W_{2}+\cdots+W_{N}=m\right\} \\
& =\sum_{m=0}^{k}\binom{n}{m}[\bar{P}(N)]^{n-m}[P(N)]^{m}
\end{aligned}
$$

so that the mean time to replacement is

$$
\begin{aligned}
& \sum_{j=1}^{N} \frac{j}{\lambda} \sum_{m=k+1}^{n}\binom{n}{m}\left\{[\bar{P}(j)]^{n-m}[P(j)]^{m}-[\bar{P}(j-1)]^{n-m}\left[P(j-1)^{m}\right]\right\} \\
& \quad+\frac{N}{\lambda} \sum_{m=0}^{k}\binom{n}{m}[\bar{P}(N)]^{n-m}[P(N)]^{m} \\
& =\frac{1}{\lambda} \sum_{j=0}^{N-1} \sum_{m=0}^{k}\binom{n}{m}[\bar{P}(j)]^{n-m}[P(j)]^{m}
\end{aligned}
$$and the expected number of failed units until replacement is

$$
\begin{aligned}
& \sum_{j=1}^{N} \sum_{m=k+1}^{n} m \sum_{r=0}^{k} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{j-1}=r\right. \\
& \left.\text { and } W_{1}+W_{2}+\cdots+W_{j}=m\right\} \\
& +\sum_{m=0}^{k} m \sum_{r=0}^{k} \operatorname{Pr}\left\{W_{1}+W_{2}+\cdots+W_{N-1}=r\right. \\
& \text { and } W_{1}+W_{2}+\cdots+W_{N}=m\} \\
& =\sum_{j=1}^{N}\left[\sum_{m=k+1}^{n} m\binom{n}{m}\left\{[\bar{P}(j)]^{n-m}[P(j)]^{m}-[\bar{P}(j-1)]^{n-m}[P(j-1)]^{m}\right\}\right. \\
& \left.-n p(j) \sum_{m=k+1}^{n-1}\binom{n-1}{m}[\bar{P}(j-1)]^{n-1-m}[P(j-1)]^{m}\right] \\
& +\sum_{m=0}^{k} m\binom{n}{m}[\bar{P}(N)]^{n-m}[P(N)]^{m} \\
& =n \sum_{j=0}^{N-1} p(j+1) \sum_{m=0}^{k}\binom{n-1}{m}[\bar{P}(j)]^{n-1-m}[P(j)]^{m}
\end{aligned}
$$

Therefore, the expected cost rate is, from (4.22), (4.24), and (4.25),

$$
\begin{gathered}
c_{N}+\left(c_{n}-c_{N}\right) \sum_{m=k+1}^{n}\binom{n}{m}[\bar{P}(N)]^{n-m}[P(N)]^{m} \\
\frac{\widetilde{C}_{2}(N \mid k)}{\lambda}=\frac{+c_{0} n \sum_{j=0}^{N-1} p(j+1) \sum_{m=0}^{k}\binom{n-1}{m}[\bar{P}(j)]^{n-1-m}[P(j)]^{m}}{\sum_{j=0}^{N-1} \sum_{m=0}^{k}\binom{n}{m}[\bar{P}(j)]^{n-m}[P(j)]^{m}} \\
(N=1,2, \ldots)
\end{gathered}
$$

In particular, when $k=n-1, \widetilde{C}_{2}(N \mid n-1)$ is equal to (4.21). Furthermore, when $k=0$, i.e., the system consists of a series system, the expected cost rate is

$$
\frac{\widetilde{C}_{2}(N \mid 0)}{\lambda}=\frac{c_{n}-\left(c_{n}-c_{N}\right)[\bar{P}(N)]^{n}+c_{0} n \sum_{j=0}^{N-1} p(j+1)[\bar{P}(j)]^{n-1}}{\sum_{j=0}^{N-1}[\bar{P}(j)]^{n}}
$$

Some modified replacement models for $k$-out-of- $n$ systems [172-174] and consecutive $k$-out-of- $n$ systems $[175,176]$ subject to shocks were proposed.

# 4.2 Two-unit System with Failure Interactions 

In a multiunit system, the failure times of different units may be often statistically correlated [177]. In other instances, the failure of units can affectone or more of the remaining units. Such types of interactions between units have been termed failure interaction [171]. Two types of failure interactions such as induced failure and shock damage were defined, and the preventive maintenance of a two-unit system with shock damage interaction was considered [178].

This section considers a system with unit 1 and unit 2 . If unit 1 fails then it undergoes only minimal repair, and hence, unit 1 failures occur in a nonhomogeneous Poisson process with a mean value function $H(t) \equiv \int_{0}^{t} h(u) d u$, where an intensity function $h(t)$ is increasing in $t$ (see Section 4.1 of [1]).

Further, when unit 1 fails, we indicate the following two failure interactions between two units [54]:
(1) Induced failure: Unit 2 fails with probability $\alpha_{j}$ at the $j$ th time of unit 1 failure.
(2) Shock damage: Unit 1 failure causes an amount of damage with distribution $G(x)$ to unit 2 .

Suppose that the system is replaced at the failure of unit 2 or the $N$ th failure of unit 1 , whichever occurs first. The expected cost rates of two models are obtained, and optimum replacement numbers $N^{*}$ that minimize them are discussed analytically. Finally, we introduce an extended model of Model 2 where the system is also replaced at time $T$. The replacement policy for a system with induced failure was extended to multiunit systems [179,180]. Furthermore, this policy was extended and applied to age and block replacement policies [181-183] and an inspection policy [184].

The above two models characterize some real systems [54]: The following example is the illustrative from the chemical industry. The system consists of a metal container (unit 2) in which chemical reactions take place and the temperature of the container is controlled by cold water pumped through a pneumatic pump (unit 1). Consider the case where the pump fails, and as a result, the pressure inside can build up and lead to an explosion if the quantity of reacting fluid is high. This situation is modeled by Model 1 with $\alpha_{j}=\alpha$ for all $j$ and $\alpha$ is the probability that the volume of fluid in the container is high. A different scenario is as follows: Whenever the pump fails, the temperature of the tank rises and the container surface is corroded. As a consequence, the thickness of the container decreases. The damage is the reduction in the wall thickness and it is additive. The container fails when the total reduction in the wall thickness has exceeded some specified limit. This situation is modeled by Model 2. Note that without unit 1 failure, there is no damage to unit 2, and hence, it does not fail. If the container is preventively maintained at time $T$ before failure and is like new, the system corresponds to an extended model. The example of a brake pad and disc rotor of an automobile was given [185].# 4.2.1 Model 1: Induced Failure 

Whenever unit 1 fails, it acts as a shock to induce an instantaneous failure of unit 2 with a certain probability. Let $\alpha_{j}$ denote the probability that unit 2 fails at the $j$ th failure of unit 1 . It is assumed that $0 \equiv \alpha_{0}<\alpha_{1} \leq \alpha_{2} \leq \cdots \leq$ $\alpha_{j} \leq \cdots<1$. The system is replaced at the failure of unit 2 or at the $N$ th $(N=1,2, \cdots)$ failure of unit 1 , whichever occurs first. The system is assumed to be replaced at unit 2 failure, when it fails at the $N$ th failure of unit 1 . The probability that the system is replaced at the $N$ th failure of unit 1 is

$$
\left(1-\alpha_{1}\right)\left(1-\alpha_{2}\right) \cdots\left(1-\alpha_{N}\right)
$$

and the probability that it is replaced at the failure of unit 2 is

$$
\sum_{j=1}^{N}\left(1-\alpha_{1}\right)\left(1-\alpha_{2}\right) \cdots\left(1-\alpha_{j-1}\right) \alpha_{j}
$$

Note that $(4.28)+(4.29)=1$.
Because the probability that $j$ failures of unit 1 occur exactly in $[0, t]$ is given by $p_{j}(t) \equiv\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}(j=0,1,2, \cdots)$ and

$$
\begin{aligned}
\int_{0}^{\infty} t p_{j-1}(t) h(t) \mathrm{d} t & =\int_{0}^{\infty} t \mathrm{e}^{-H(t)} \mathrm{d}\left\{\frac{[H(t)]^{j}}{j!}\right\} \\
& =\int_{0}^{\infty} t p_{j}(t) h(t) \mathrm{d} t-\int_{0}^{\infty} p_{j}(t) \mathrm{d} t
\end{aligned}
$$

the mean time to replacement is

$$
\begin{aligned}
& \left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{N}\right) \int_{0}^{\infty} t p_{N-1}(t) h(t) \mathrm{d} t \\
& \quad+\sum_{j=1}^{N}\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{j-1}\right) \alpha_{j} \int_{0}^{\infty} t p_{j-1}(t) h(t) \mathrm{d} t \\
& =\sum_{j=0}^{N-1}\left(1-\alpha_{0}\right)\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{j}\right) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t
\end{aligned}
$$

The expected number of unit 1 failures before replacement is

$$
\begin{aligned}
& (N-1)\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{N}\right)+\sum_{j=1}^{N}(j-1)\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{j-1}\right) \alpha_{j} \\
& =\sum_{j=1}^{N-1}\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{j}\right)
\end{aligned}
$$

where $\sum_{1}^{0} \equiv 0$. Note that we do not include the number of the $j$ th failure in (4.31) when the system is replaced at the $j$ th failure of unit 1 .Let $c_{1}$ be the cost of unit 1 failure, $c_{2}$ be the replacement cost at the $N$ th failure of unit 1 , and $c_{3}$ be the replacement cost at the failure of unit 2 with $c_{3}>c_{2}>c_{1}$. Then, the expected cost rate is, from (4.28)-(4.31),

$$
C_{1}(N)=\frac{c_{1} \sum_{j=1}^{N-1} A_{j}+c_{3}-\left(c_{3}-c_{2}\right) A_{N}}{\sum_{j=0}^{N-1} A_{j} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t} \quad(N=1,2, \cdots)
$$

where $A_{j} \equiv\left(1-\alpha_{0}\right)\left(1-\alpha_{1}\right) \cdots\left(1-\alpha_{j}\right)(j=0,1,2, \cdots)$.
We seek an optimum number $N^{*}$ that minimizes $C_{1}(N)$ in (4.32). From the inequality $C_{1}(N+1) \geq C_{1}(N)$,

$$
\begin{aligned}
& c_{1}\left[\frac{\sum_{j=0}^{N-1} A_{j} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}-\sum_{j=1}^{N-1} A_{j}\right] \\
& +\left(c_{3}-c_{2}\right)\left[\frac{A_{N}-A_{N+1}}{A_{N} \int_{0}^{\infty} p_{N}(t) \mathrm{d} t} \sum_{j=0}^{N-1} A_{j} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t+A_{N}\right] \geq c_{3} \\
&(N=1,2, \ldots)
\end{aligned}
$$

Denoting the left-hand side of (4.33) by $Q_{1}(N)$,

$$
\begin{aligned}
Q_{1}(N+1)-Q_{1}(N)= & \sum_{j=0}^{N} A_{j} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t\left\{c_{1}\left[\frac{1}{\int_{0}^{\infty} p_{N+1}(t) \mathrm{d} t}-\frac{1}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}\right]\right. \\
& \left.+\left(c_{3}-c_{2}\right)\left[\frac{A_{N+1}-A_{N+2}}{A_{N+1} \int_{0}^{\infty} p_{N+1}(t) \mathrm{d} t}-\frac{A_{N}-A_{N+1}}{A_{N} \int_{0}^{\infty} p_{N}(t) \mathrm{d} t}\right]\right\}
\end{aligned}
$$

Suppose that either of $\alpha_{j}$ or $h(t)$ is strictly increasing. Then, from (1.29), if $h(t)$ is strictly increasing, then $\int_{0}^{\infty} p_{j}(t) \mathrm{d} t$ is strictly decreasing in $j$ to $1 / h(\infty)$, where $h(\infty) \equiv \lim _{t \rightarrow \infty} h(t)$, and if $\alpha_{j}$ is strictly increasing, then $\left(A_{N}-A_{N+1}\right) / A_{N}$ is also strictly increasing. Thus, $Q_{1}(N)$ is strictly increasing in $N$, and hence, an optimum number $N^{*}$ is given by a unique minimum such that $Q_{1}(N) \geq c_{3}$.
Example 4.3. Suppose that $\alpha_{j}$ is constant, i.e., $\alpha_{j} \equiv \alpha(0<\alpha<1)$ and $A_{j} \equiv(1-\alpha)^{j}(j=0,1,2, \cdots)$. Then, (4.33) is rewritten as

$$
\frac{\sum_{j=0}^{N-1} \alpha(1-\alpha)^{j} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}+(1-\alpha)^{N} \geq \frac{c_{1}+\alpha\left(c_{3}-c_{1}\right)}{c_{1}+\alpha\left(c_{3}-c_{2}\right)} \quad(N=1,2, \cdots)
$$

If $h(t)$ is strictly increasing, then the left-hand side $Q_{1}(N)$ of (4.34) is also strictly increasing, and

$$
\lim _{N \rightarrow \infty} Q_{1}(N)=\alpha h(\infty) \int_{0}^{\infty} \mathrm{e}^{-\alpha H(t)} \mathrm{d} t
$$Table 4.3. Optimum number $N^{*}$ to minimize $C_{1}(N)$ when $\alpha=0.1$

| $\left(c_{3}-c_{2}\right) / c_{1}$ | $c_{2} / c_{1}$ |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 2 | 3 | 5 | 10 | 20 | 50 |
| 1 | 1 | 2 | 4 | 10 | 24 | 95 |
| 2 | 1 | 2 | 4 | 9 | 21 | 83 |
| 5 | 1 | 2 | 3 | 7 | 16 | 58 |
| 10 | 1 | 1 | 3 | 5 | 12 | 38 |
| 20 | 1 | 1 | 2 | 4 | 7 | 22 |
| 50 | 1 | 1 | 1 | 2 | 4 | 10 |

Thus, if

$$
\alpha h(\infty) \int_{0}^{\infty} \mathrm{e}^{-\alpha H(t)} \mathrm{d} t>\frac{c_{1}+\alpha\left(c_{3}-c_{1}\right)}{c_{1}+\alpha\left(c_{3}-c_{2}\right)}
$$

then a finite $N^{*}$ is given by a unique minimum number that satisfies (4.34).
When $h(t)=2 t$, i.e., $p_{j}(t)=\left[\left(t^{2}\right)^{j} / j!\right] \mathrm{e}^{-t^{2}}, h(t)$ is strictly increasing to $\infty$. Thus, there exists a unique minimum $N^{*}$ that satisfies (4.34). Table 4.3 presents the optimum number $N^{*}$ for $\left(c_{3}-c_{2}\right) / c_{1}=1,2,5,10,20,50$ and $c_{2} / c_{1}=2,3,5,10,20,50$ when $\alpha=0.1$. In this case, because $\int_{0}^{\infty} p_{0}(t) \mathrm{d} t=$ $\sqrt{\pi} / 2$ and $\int_{0}^{\infty} p_{1}(t) \mathrm{d} t=\sqrt{\pi} / 4$, if $0.1\left[\left(c_{3}-c_{2}\right) / c_{1}\right] \geq\left(c_{2} / c_{1}\right)-2$, then $N^{*}=1$.

Example 4.4. Suppose that $h(t)=\lambda$, i.e., unit 1 failures occur in a Poisson process with rate $\lambda$. Then, (4.33) is

$$
\alpha_{N+1} \sum_{j=0}^{N-1} A_{j}+A_{N} \geq \frac{c_{3}-c_{1}}{c_{3}-c_{2}} \quad(N=1,2, \cdots)
$$

If $\alpha_{j}$ is strictly increasing in $j$, where $\alpha_{\infty} \equiv \lim _{j \rightarrow \infty} \alpha_{j}$ that might be 1 , then the left-hand side of (4.36) is also strictly increasing, and

$$
Q_{1}(\infty) \equiv \lim _{N \rightarrow \infty} Q_{1}(N)=\alpha_{\infty} \sum_{j=0}^{\infty} A_{j}
$$

Thus, if $Q_{1}(\infty)>\left(c_{3}-c_{1}\right) /\left(c_{3}-c_{2}\right)$, then a finite $N^{*}$ is a unique minimum that satisfies (4.36). In addition, it is easily proved that

$$
\alpha_{N+1} \sum_{j=0}^{N-1} A_{j}+A_{N}>\alpha_{N+1}+A_{1} \quad(N=2,3, \cdots)
$$

becauseTable 4.4. Optimum number $N^{*}$ to minimize $C_{1}(N)$ when $\alpha_{j}=1-(0.9)^{j}$

| $\left(c_{3}-c_{2}\right) / c_{1}$ | $c_{2} / c_{1}$ |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 2 | 3 | 5 | 10 | 20 | 50 |
| 1 | 6 | 13 | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
| 2 | 4 | 6 | 13 | $\infty$ | $\infty$ | $\infty$ |
| 5 | 2 | 3 | 5 | 11 | $\infty$ | $\infty$ |
| 10 | 2 | 2 | 3 | 6 | 12 | $\infty$ |
| 20 | 1 | 2 | 2 | 4 | 6 | 20 |
| 50 | 1 | 1 | 1 | 2 | 3 | 6 |

$$
\begin{aligned}
\alpha_{N+1} \sum_{j=1}^{N-1} A_{j}-\left(A_{1}-A_{N}\right) & =\sum_{j=1}^{N-1}\left(\alpha_{N+1} A_{j}+A_{j+1}-A_{j}\right) \\
& =\sum_{j=1}^{N-1} A_{j}\left(\alpha_{N+1}-\alpha_{j+1}\right)>0
\end{aligned}
$$

Therefore, if $\alpha_{\infty}+1-\alpha_{1} \geq\left(c_{3}-c_{1}\right) /\left(c_{3}-c_{2}\right)$, then a finite $N^{*}$ exists.
When $\alpha_{j} \equiv 1-\alpha^{j}$, if a finite $N^{*}$ exists, then it is given by a unique minimum that satisfies

$$
\left(1-\alpha^{N+1}\right) \sum_{j=0}^{N-1} \alpha^{j(j+1) / 2}+\alpha^{N(N+1) / 2} \geq \frac{c_{3}-c_{1}}{c_{3}-c_{2}} \quad(N=1,2, \cdots)
$$

Table 4.4 presents the optimum number $N^{*}$ for $\left(c_{3}-c_{2}\right) / c_{1}=1,2,5,10$, 20,50 and $c_{2} / c_{1}=2,3,5,10,20,50$ when $\alpha=0.9$. The optimum $N^{*}$ increases with $c_{2} / c_{1}$ and decreases with $\left(c_{3}-c_{2}\right) / c_{1}$. Because $\sum_{j=0}^{\infty}(0.9)^{j(j+1) / 2}<3.92$, if $\left(c_{3}-c_{1}\right) /\left(c_{3}-c_{2}\right) \geq 3.92$, i.e., $c_{2} / c_{1} \geq 1+2.92\left[\left(c_{3}-c_{2}\right) / c_{1}\right]$, then $N^{*}=\infty$. If $0.09\left[\left(c_{3}-c_{2}\right) / c_{1}\right] \geq\left(c_{2} / c_{1}\right)-1$, then $N^{*}=1$.

# 4.2.2 Model 2: Shock Damage 

Whenever unit 1 fails, it acts as some shock to unit 2 and causes an amount of damage with distribution $G(x)$ to unit 2 . The total damage is additive and unit 2 fails whenever it has exceeded a failure level $K$. The system is replaced at the failure of unit 2 or at the $N$ th failure of unit 1 , whichever occurs first.

The probability that the system is replaced at the $N$ th failure of unit 1 is $G^{(N)}(K)$, where $G^{(j)}(x)(j=1,2, \cdots)$ is the $j$-fold Stieltjes convolution of $G(x)$ with itself and $G^{(0)}(x) \equiv 1$ for $x \geq 0$. Thus, the mean time to replacement is, from (3.5),

$$
\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t
$$and the expected number of unit 1 failures before replacement is

$$
(N-1) G^{(N)}(K)+\sum_{j=1}^{N-1}(j-1)\left[G^{(j-1)}(K)-G^{(j)}(K)\right]=\sum_{j=1}^{N-1} G^{(j)}(K)
$$

Therefore, the expected cost rate is, from (4.37) and (4.38),

$$
C_{2}(N)=\frac{c_{1} \sum_{j=1}^{N-1} G^{(j)}(K)+c_{3}-\left(c_{3}-c_{2}\right) G^{(N)}(K)}{\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t} \quad(N=1,2, \cdots)
$$

where $c_{k}(k=1,2,3)$ are the same costs as those for Model 1. In particular, when $K$ goes to infinity,

$$
C_{2}(N)=\frac{c_{1}(N-1)+c_{2}}{\sum_{j=0}^{N-1} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t}
$$

that agrees with (4.25) of [1], and it is the expected cost rate of the replacement at the $N$ th failure.

We seek an optimum number $N^{*}$ that minimizes $C_{2}(N)$ in (4.39). From the inequality $C_{2}(N+1) \geq C_{2}(N)$,

$$
\begin{aligned}
& c_{1}\left[\frac{1}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t} \sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t-\sum_{j=1}^{N-1} G^{(j)}(K)\right] \\
& +\left(c_{3}-c_{2}\right)\left[\frac{G^{(N)}(K)-G^{(N+1)}(K)}{G^{(N)}(K) \int_{0}^{\infty} p_{N}(t) \mathrm{d} t} \sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t+G^{(N)}(K)\right] \\
& \geq c_{3} \quad(N=1,2, \ldots)
\end{aligned}
$$

Denoting the left-hand side of (4.41) by $Q_{2}(N)$,

$$
\begin{aligned}
& Q_{2}(N+1)-Q_{2}(N) \\
& =\sum_{j=0}^{N} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t\left\{c_{1}\left[\frac{1}{\int_{0}^{\infty} p_{N+1}(t) \mathrm{d} t}-\frac{1}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}\right]\right. \\
& \left.\quad+\left(c_{3}-c_{2}\right)\left[\frac{G^{(N+1)}(K)-G^{(N+2)}(K)}{G^{(N+1)}(K) \int_{0}^{\infty} p_{N+1}(t) \mathrm{d} t}-\frac{G^{(N)}(K)-G^{(N+1)}(K)}{G^{(N)}(K) \int_{0}^{\infty} p_{N}(t) \mathrm{d} t}\right]\right\}
\end{aligned}
$$

Suppose that either of $\left[G^{(N)}(K)-G^{(N+1)}(K)\right] / G^{(N)}(K)$ or $h(t)$ is strictly increasing. Then, $Q_{2}(N)$ is also strictly increasing in $N$, and hence, an optimum number $N^{*}$ is given by a unique minimum that satisfies (4.41).
Example 4.5. Suppose that $G(x)=1-\mathrm{e}^{-\mu x}$ and $G^{(j)}(K)=\sum_{i=j}^{\infty}[(\mu K)^{i} / i!] \mathrm{e}^{-\mu K}$. Then, from Example 2.2 of Chapter 2,$$
\frac{G^{(N+1)}(K)}{G^{(N)}(K)}=\frac{\sum_{j=N+1}^{\infty}\left[(\mu K)^{j} / j!\right]}{\sum_{j=N}^{\infty}\left[(\mu K)^{j} / j!\right]}
$$

is decreasing in $N$ from $1-\mathrm{e}^{-\mu K}$ to 0 . Furthermore,

$$
\lim _{N \rightarrow \infty} Q_{2}(N)=\left(c_{3}-c_{2}+c_{1}\right) h(\infty) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t-c_{1} \mu K
$$

Thus, if

$$
h(\infty) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t>\frac{c_{3}+c_{1} \mu K}{c_{3}-c_{2}+c_{1}}
$$

then a finite $N^{*}$ is given by a unique minimum number that satisfies (4.41). In addition, when $h(t)=\lambda, h(\infty) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t=1$ and $\sum_{j=0}^{\infty} G^{(j)}(K)=1+\mu K$, and hence, if $\mu K>\left(c_{2}-c_{1}\right) /\left(c_{3}-c_{2}\right)$, then a finite $N^{*}$ exists uniquely.

# 4.2.3 Modified Models 

## (1) Case of Renewal Process

If unit 1 fails, then it is replaced with a new one, that is, unit 1 failures occur in a renewal process with mean interval $1 / \lambda$. Then, the expected cost rate of Model 1 is, from (4.32),

$$
\frac{C_{1}(N)}{\lambda}=\frac{c_{1} \sum_{j=1}^{N-1} A_{j}+c_{3}-\left(c_{3}-c_{2}\right) A_{N}}{\sum_{j=0}^{N-1} A_{j}} \quad(N=1,2, \cdots)
$$

Thus, the optimum number $N^{*}$ that minimizes $C_{1}(N)$ has been derived in Example 4.4

Similarly, the expected cost rate of Model 2 is, from (4.39),

$$
\frac{C_{2}(N)}{\lambda}=\frac{c_{1} \sum_{j=1}^{N-1} G^{(j)}(K)+c_{3}-\left(c_{3}-c_{2}\right) G^{(N)}(K)}{\sum_{j=0}^{N-1} G^{(j)}(K)} \quad(N=1,2, \cdots)
$$

Thus, the optimum number $N^{*}$ that minimizes $C_{2}(N)$ is derived in (2) of Section 3.2 , by replacing $c_{K}=c_{3}-c_{1}$ and $c_{N}=c_{2}-c_{1}$.

## (2) Replacement at Time $T$ and Shock $N$ for Model 2

Consider an extended replacement policy for Model 2 where the system is replaced at time $T$, at the failure of unit 2 , or at the $N$ th failure of unit 1 , whichever occurs first.

The probability that the system is replaced at time $T$ is$$
\sum_{j=0}^{N-1} p_{j}(T) G^{(j)}(K)
$$

the probability that it is replaced at the $N$ th failure of unit 1 is

$$
\sum_{j=N}^{\infty} p_{j}(T) G^{(N)}(K)
$$

and the probability that it is replaced at the failure of unit 2 is

$$
\begin{aligned}
& \sum_{j=0}^{N-1} p_{j}(T)\left[1-G^{(j)}(K)\right]+\sum_{j=N}^{\infty} p_{j}(T)\left[1-G^{(N)}(K)\right] \\
& =\sum_{j=1}^{N}\left[G^{(j-1)}(K)-G^{(j)}(K)\right] \sum_{i=j}^{\infty} p_{i}(T)
\end{aligned}
$$

It is clearly seen that $(4.44)+(4.45)+(4.46)=1$. The mean time to replacement is

$$
\begin{aligned}
& T \sum_{j=0}^{N-1} p_{j}(T) G^{(j)}(K)+G^{(N)}(K) \int_{0}^{T} t p_{N-1}(t) h(t) \mathrm{d} t \\
& \quad+\sum_{j=1}^{N}\left[G^{(j-1)}(K)-G^{(j)}(K)\right] \int_{0}^{T} t p_{j-1}(t) h(t) \mathrm{d} t \\
& =\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t
\end{aligned}
$$

and the expected number of unit 1 failures before replacement is

$$
\begin{aligned}
& \sum_{j=0}^{N-1} j p_{j}(T) G^{(j)}(K)+(N-1) \sum_{j=N}^{\infty} p_{j}(T) G^{(N)}(K) \\
& \quad+\sum_{j=1}^{N}(j-1)\left[G^{(j-1)}(K)-G^{(j)}(K)\right] \sum_{i=j}^{\infty} p_{i}(T) \\
& =\sum_{j=1}^{N-1} G^{(j)}(K) \sum_{i=j}^{\infty} p_{i}(T)
\end{aligned}
$$

Therefore, the expected cost rate is, from (4.44)-(4.48),

$$
\begin{aligned}
& c_{1} \sum_{j=1}^{N-1} G^{(j)}(K) \sum_{i=j}^{\infty} p_{i}(T)+c_{2} G^{(N)}(K) \sum_{j=N}^{\infty} p_{j}(T) \\
& +c_{3} \sum_{j=1}^{N-1}\left[G^{(j-1)}(K)-G^{(j)}(K)\right] \sum_{i=j}^{\infty} p_{i}(T) \\
& C(T, N)=\frac{+c_{4} \sum_{j=0}^{N-1} G^{(j)}(K) p_{j}(T)}{\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t}
\end{aligned}
$$where $c_{1}=$ cost of one unit failure, $c_{2}=$ replacement cost at the $N$ th failure of unit $1, c_{3}=$ replacement cost at the failure of unit 2 , and $c_{4}=$ replacement cost at time $T$. In particular, when $T$ goes to infinity, $C(T, N)$ agrees with $C_{2}(N)$ in (4.39)

On the other hand, when $N$ goes to infinity and unit 1 failures occur in a Poisson process with rate $\lambda$, i.e., $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$, the expected cost rate is simplified as

$$
\begin{aligned}
C(T) & \equiv \lim _{N \rightarrow \infty} C(T, N) \\
& =\frac{c_{3}-c_{1}-\left(c_{3}-c_{1}-c_{4}\right) \sum_{j=0}^{\infty} G^{(j)}(K) p_{j}(T)}{(1 / \lambda) \sum_{j=0}^{\infty} G^{(j)}(K) \sum_{i=j+1}^{\infty} p_{i}(T)}+\lambda c_{1}
\end{aligned}
$$

Thus, the optimum problem of minimizing $C(T)$ corresponds to that of minimizing $C_{1}(T)$ in (3.11) when $p_{j}(t)=F^{(j)}(t)-F^{(j+1)}(t)$.

# (3) Replacement at Time $T$ and Damage $Z$ 

Consider the replacement model where the system is replaced before failure of unit 2 when its total damage has exceeded a threshold level $Z(0 \leq Z \leq K)$ without replacing at the $N$ th failure of unit 1 in (2). It is supposed that the system is replaced at time $T$, at the failure of unit 2 , or at damage $Z$, whichever occurs first [185].

The probability that the system is replaced at time $T$ is

$$
\sum_{j=0}^{\infty} G^{(j)}(Z) p_{j}(T)
$$

the probability that it is replaced at damage $Z$, i.e., when the total damage has exceeded $Z$ and is less than $K$, is

$$
\sum_{j=0}^{\infty} \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \sum_{i=j+1}^{\infty} p_{i}(T)
$$

and the probability that it is replaced at the failure of unit 2 , i.e., when the total damage has exceeded a failure level $K$, is

$$
\sum_{j=0}^{\infty} \int_{0}^{Z}[1-G(K-x)] \mathrm{d} G^{(j)}(x) \sum_{i=j+1}^{\infty} p_{i}(T)
$$

Note that $(4.51)+(4.52)+(4.53)=1$. The mean time to replacement is

$$
\begin{gathered}
T \sum_{j=0}^{\infty} G^{(j)}(Z) p_{j}(T)+\sum_{j=0}^{\infty} \int_{0}^{Z}[1-G(Z-x)] \mathrm{d} G^{(j)}(x) \int_{0}^{T} t p_{j}(t) h(t) \mathrm{d} t \\
=\sum_{j=0}^{\infty} G^{(j)}(Z) \int_{0}^{T} p_{j}(t) \mathrm{d} t
\end{gathered}
$$and the expected number of unit 1 failures before replacement is

$$
\begin{aligned}
\sum_{j=0}^{\infty} j G^{(j)}(Z) p_{j}(T) & +\sum_{j=0}^{\infty} j \int_{0}^{Z}[1-G(Z-x)] \mathrm{d} G^{(j)}(x) \sum_{i=j+1}^{\infty} p_{i}(T) \\
& =\sum_{j=1}^{\infty} G^{(j)}(Z) \sum_{i=j}^{\infty} p_{i}(T)
\end{aligned}
$$

Denoting that $c_{2}$ is the replacement cost at damage $Z$ and the other costs are the same ones as those of (4.49), the expected cost rate is, from (4.51)(4.55),

$$
\begin{aligned}
& c_{1} \sum_{j=1}^{\infty} G^{(j)}(Z) \sum_{i=j}^{\infty} p_{i}(T) \\
& +c_{2} \sum_{j=0}^{\infty} \int_{0}^{Z}[G(K-x)-G(Z-x)] \mathrm{d} G^{(j)}(x) \sum_{i=j+1}^{\infty} p_{i}(T) \\
& +c_{3} \sum_{j=0}^{\infty} \int_{0}^{Z}[1-G(K-x)] \mathrm{d} G^{(j)}(x) \sum_{i=j+1}^{\infty} p_{i}(T) \\
& C(T, Z)=\frac{+c_{4} \sum_{j=0}^{\infty} G^{(j)}(Z) p_{j}(T)}{\sum_{j=0}^{\infty} G^{(j)}(Z) \int_{0}^{T} p_{j}(t) \mathrm{d} t}
\end{aligned}
$$

It is clearly seen that $C(T, Z)$, as $Z \rightarrow K$, is equal to $C(T, N)$ in (4.49), as $N \rightarrow \infty$. There do not exist both $T^{*}\left(0<T^{*}<\infty\right)$ and $Z^{*}\left(0<Z^{*}<K\right)$ that minimize the expected cost rate $C(T, Z)$ as shown in (2) of Section 3.3.

Suppose that the system is replaced before failure only at damage $Z$ and $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$. Then, the expected cost rate is

$$
\begin{aligned}
C(Z) & \equiv \lim _{T \rightarrow \infty} C(T, Z) \\
& =\frac{\left(c_{3}-c_{2}+c_{1}\right) M_{G}(Z)+c_{3}-\left(c_{3}-c_{2}\right)\left[G(K)+\int_{0}^{Z} G(K-x) \mathrm{d} M_{G}(x)\right]}{\left[1+M_{G}(Z)\right] / \lambda}
\end{aligned}
$$

where $M_{G}(x) \equiv \sum_{j=1}^{\infty} G^{(j)}(x)$. When $c_{1}=0$, this corresponds to the expected cost rate in (3.24).# Periodic Replacement Policies 

When we consider large and complex systems that consist of many different kinds of units, we should make the planned replacement or preventive maintenance at periodic times, and make some minimal repair at failures between replacements. This policy is called periodic replacement with minimal repair at failures [66], where minimal repair means that the failure rate remains undisturbed by any repair of failures. A unit is inspected and replaced periodically at planned times $n T(n=1,2, \cdots)$. This replacement policy is commonly used with complex systems such as computers, airplanes, and large production systems. Their theoretical results were extensively summarized [1].

This chapter applies the periodic replacement to a cumulative damage model where shocks occur in a renewal process and the total damage due to shocks is additive. This periodic replacement was considered, and optimum policies that minimize the expected costs under suitable conditions were discussed $[186-189]$.

We have already derived the failure distribution $\Phi(t)$ in (2.9) of a unit with cumulative damage. Substituting $\Phi(t)$ in standard replacements such as age replacement, block replacement, and periodic inspection, it is shown in Section 5.1 that these replacement policies can be applied to a cumulative damage model. In Section 5.2, the amount of total damage is checked only at periodic times $n T$, and a unit is replaced before failure at a planned time $N T$. The expected cost rate is obtained and an optimum $N^{*}$ that minimizes it is derived [190]. It has been assumed in all models until now that a unit is always replaced at failures. Section 5.3 considers the cumulative damage model where a unit suffers some damage caused by both shock and inspection [191]. In Section 5.4, we apply the periodic replacement with minimal repair at failures to a cumulative damage model [55]. It is assumed that a unit fails with probability $p(x)$ when that total damage becomes $x$ at shocks and the total damage is not unchanged by any minimal repair at failures. The expected cost rate is obtained, and an optimum planned time $T^{*}$, shock number $N^{*}$ and damage level $Z^{*}$ that minimize it are discussed analytically. Furthermore, in Section 5.5, we consider modified models where a unit is replaced at thenext shock, when the total operating time has exceeded a planned time $T$ and the total damage has exceeded a damage level $Z$. Numerical examples to understand these models and methods easily are given in some sections.

# 5.1 Basic Replacement Models 

Suppose that the failure distribution $\Phi(t)$ of a unit with a failure level $K$ is given in (2.9), where $\bar{\Phi} \equiv 1-\Phi$. Then, using the theory of replacement policies [1], we have the following expected cost rates: A unit is replaced with a new one at a planned time $T(0<T \leq \infty)$ or at failure, i.e., when the total damage has exceeded a failure level $K$, whichever occurs first. This is called an age replacement policy and its expected cost rate is, from (3.4) of [1],

$$
C_{1}(T)=\frac{\left(c_{K}-c_{T}\right) \Phi(T)+c_{T}}{\int_{0}^{T} \bar{\Phi}(t) \mathrm{d} t}
$$

where cost $c_{K}$ is incurred for the replacement of a failed unit and cost $c_{T}$ $\left(<c_{K}\right)$ is incurred for the replacement of a nonfailed unit at time $T$.

A unit is replaced with a new one at periodic times $n T(n=1,2, \cdots)$ and is also replaced at each failure between periodic replacements. This is called a block replacement and its expected cost rate is, from (5.1) of [1],

$$
C_{2}(T)=\frac{1}{T}\left[c_{K} M_{\Phi}(T)+c_{T}\right]
$$

where $c_{K}$ is the cost of replacement at each failure, $c_{T}$ is the cost of the planned replacement, $M_{\Phi}(t) \equiv \sum_{n=1}^{\infty} \Phi^{(n)}(t)$ is a renewal function of a failure distribution $\Phi(t)$, and $\Phi^{(n)}(t)$ is the $n$-fold Stieltjes convolution of $\Phi(t)$ and $\Phi^{(0)}(t) \equiv 1$ for $t \geq 0$.

Furthermore, when a unit fails between periodic replacements, it remains in a failed state and is replaced only at a planned time $T$. Then, the expected cost rate is, from (5.10) of [1],

$$
C_{3}(T)=\frac{1}{T}\left[c_{D} \int_{0}^{T} \Phi(t) \mathrm{d} t+c_{T}\right]
$$

where $c_{D}$ is the downtime cost per unit of time for the time elapsed between a failure and its replacement. Optimum policies that minimize $C_{k}(T)(k=$ $1,2,3)$ were discussed analytically for a general failure distribution [1].

Finally, any failure is detected only through inspection. A unit is checked at periodic times $n T(n=1,2, \cdots)$, its failure is always detected at the next checking time, and it is replaced. This is called an inspection policy with replacement, and the total expected cost until replacement is, from (8.1) of [1],

$$
C_{4}(T)=\sum_{n=0}^{\infty} \int_{n T}^{(n+1) T}\left\{c_{T}(n+1)+c_{D}[(n+1) T-t]\right\} \mathrm{d} \Phi(t)+c_{K}
$$where $c_{T}$ is the cost of one check at time $n T, c_{D}$ is the loss cost per unit of time for the time elapsed between a failure and its detection, and $c_{K}$ is the replacement cost of a failed unit.

Example 5.1. Suppose that shocks occur in a Poisson process, each damage due to shocks and a failure level $K$ are exponential, i.e., $F(t)=1-\mathrm{e}^{-\lambda t}$, $G(x)=1-\mathrm{e}^{-\mu x}$, and $L(x)=1-\mathrm{e}^{-\theta x}$. Then, from Example 2.3,

$$
\Phi(t)=1-\exp \left(-\frac{\lambda \theta t}{\mu+\theta}\right)
$$

The total expected cost of an inspection policy is, from (5.4),

$$
C_{4}(T)=\frac{c_{T}+c_{D} T}{1-\mathrm{e}^{-\lambda \theta T /(\mu+\theta)}}-\frac{c_{D}(\mu+\theta)}{\lambda \theta}+c_{K}
$$

Thus, an optimum checking time $T^{*}$ to minimize $C_{4}(T)$ is given by a unique solution that satisfies

$$
\mathrm{e}^{\lambda \theta T /(\mu+\theta)}-\left(1+\frac{\lambda \theta T}{\mu+\theta}\right)=\frac{c_{T} \lambda \theta}{c_{D}(\mu+\theta)}
$$

and it is approximately

$$
\widetilde{T}=\sqrt{\frac{2 c_{T}(\mu+\theta)}{c_{D} \lambda \theta}}
$$

and $T^{*}<\widetilde{T}$.
Next, suppose that $\Phi(t)$ is an exponential distribution with mean $K / a$ $(a>0)$ from Section 2.4, i.e., when $Y$ is the time to failure, $a E\{Y\}=K$ and $\Phi(t)=1-\mathrm{e}^{-a t / K}$. Then, the total expected cost is

$$
C_{4}(T)=\frac{c_{T}+c_{D} T}{1-\mathrm{e}^{-a T / K}}-\frac{c_{D} K}{a}+c_{K}
$$

An optimum $T^{*}$ satisfies

$$
\mathrm{e}^{a T / K}-\left(1+\frac{a T}{K}\right)=\frac{c_{T} a}{c_{D} K}
$$

and it is approximately

$$
\widetilde{T}=\sqrt{\frac{2 c_{T} K}{c_{D} a}}
$$

and $T^{*}<\widetilde{T}$. It is clearly seen that $T^{*}$ decreases, as parameter $a$ increases. This represents the continuous wear model in which the failure time is distributed exponentially and its mean time is $E\{Y\}=K / a$.When shocks occur in a Poisson distribution with mean $1 / \lambda$ and a unit fails at shock $n, \Phi(t)$ has a gamma distribution in (1.23), i.e., $\Phi(t)=$ $\sum_{i=n}^{\infty}\left[(\lambda t)^{i} / i!\right] \mathrm{e}^{-\lambda t}(n=1,2, \ldots)$. In this case, the total expected cost is

$$
C_{4}(T)=\left(c_{T}+c_{D} T\right) \sum_{j=0}^{\infty} \sum_{i=0}^{n-1} \frac{(\lambda j T)^{i}}{i!} \mathrm{e}^{-\lambda j T}-\frac{n c_{D}}{\lambda}+c_{K}
$$

Similar replacement policies when $\Phi(t)$ is a gamma distribution were considered $[192,193]$. This is called a continuous wear process under discrete monitoring by inspection, that is one of conditioned maintenance policies as shown in Section 6.1. Multicritical levels of preventive maintenances for a failure level $K$ were proposed, and the optimum policies for several systems were discussed [194-196].

# 5.2 Discrete Replacement Models 

Each amount $W_{n}(n=1,2, \cdots)$ of damage to a unit is measured only at planned times $n T(n=1,2, \cdots)$ for a given $T(0<T<\infty)$ and has an identical distribution $G(x) \equiv \operatorname{Pr}\left\{W_{n} \leq x\right\}$ between periodic times. The unit fails only at time $n T$, and is replaced at time $N T$ or at failure, whichever occurs first. Because the mean time to replacement is

$$
\sum_{n=0}^{N-1}[(n+1) T]\left[G^{(n)}(K)-G^{(n+1)}(K)\right]+(N T) G^{(N)}(K)=T \sum_{n=0}^{N-1} G^{(n)}(K)
$$

the expected cost rate is

$$
C_{1}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) G^{(N)}(K)}{T \sum_{n=0}^{N-1} G^{(n)}(K)} \quad(N=1,2, \cdots)
$$

where $c_{K}$ is the replacement cost at failure and $c_{N}\left(<c_{K}\right)$ is the replacement cost at time $N T$. Thus, this corresponds to the same replacement model with a shock number $N$ in (2) of Section 3.2, by replacing $1 / \lambda$ with $T$. The replacement policy where the unit is replaced before failure at damage $Z$ has been already taken up in (3) of Section 3.2.

Next, suppose that shocks occur continuously and the total damage is proportional to an operating time, i.e., $Z(t)=a t(a>0)$. In this case, if a failure level $K$ is a random variable with a continuous distribution $L(x)$ defined in (2) of Section 2.5, the probability that the unit fails at time $n T$ is $\operatorname{Pr}\{n a T \geq K\}=L(n a T)$. Thus, the probability that the unit fails until time $N T$ is

$$
\sum_{n=1}^{N} L(n a T) \prod_{i=0}^{n-1} \bar{L}(i a T)
$$and the probability that it does not fail until time $N T$ is

$$
\prod_{n=1}^{N} \bar{L}(n a T)
$$

where $\bar{L}(x) \equiv 1-L(x)$. Note that $(5.6)+(5.7)=1$. The mean time to replacement is

$$
\sum_{n=1}^{N}(n T) L(n a T) \prod_{i=0}^{n-1} \bar{L}(i a T)+(N T) \prod_{n=1}^{N} \bar{L}(n a T)=T \sum_{n=0}^{N-1}\left[\prod_{i=0}^{n} \bar{L}(i a T)\right]
$$

and hence, the mean time $E\{Y\}$ to failure is

$$
E\{Y\}=T \sum_{n=0}^{\infty}\left[\prod_{i=0}^{n} \bar{L}(i a T)\right]
$$

Therefore, the expected cost rate is, from (5.7) and (5.8),

$$
C_{2}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) \prod_{n=1}^{N} \bar{L}(n a T)}{T \sum_{n=0}^{N-1}\left[\prod_{i=0}^{n} \bar{L}(i a T)\right]} \quad(N=1,2, \cdots)
$$

We seek an optimum number $N^{*}$ that minimizes $C_{2}(N)$. From the inequality $C_{2}(N+1)-C_{2}(N) \geq 0$,

$$
L((N+1) a T) \sum_{n=0}^{N-1}\left[\prod_{i=0}^{n} \bar{L}(i a T)\right]+\prod_{n=1}^{N} \bar{L}(n a T) \geq \frac{c_{K}}{c_{K}-c_{N}} \quad(N=1,2, \cdots)
$$

Letting $Q(N)$ be the left-hand side of $(5.10)$,

$$
\begin{aligned}
Q(\infty) & \equiv \lim _{N \rightarrow \infty} Q(N)=\sum_{n=0}^{\infty}\left[\prod_{i \equiv 0}^{n} \bar{L}(i a T)\right]=\frac{E\{Y\}}{T} \\
Q(N+1)-Q(N) & =[L((N+2) a T)-L((N+1) a T)] \sum_{n=0}^{N}\left[\prod_{i \equiv 0}^{n} \bar{L}(i a T)\right]>0
\end{aligned}
$$

Thus, $Q(N)$ is strictly increasing to $E\{Y\} / T$ that represents the expected number of periodic times to failure, and hence, we have the optimum replacement policy:
(i) If $E\{Y\} / T>c_{K} /\left(c_{K}-c_{N}\right)$, then there exists a finite and unique minimum $N^{*}\left(1 \leq N^{*}<\infty\right)$ that satisfies (5.10), and its resulting cost rate is

$$
\frac{L\left(N^{*} a T\right)}{T\left(c_{K}-c_{N}\right)}<C_{2}\left(N^{*}\right) \leq \frac{L\left(\left(N^{*}+1\right) a T\right)}{T\left(c_{K}-c_{N}\right)}
$$(ii) If $E\{Y\} / T \leq c_{K} /\left(c_{K}-c_{N}\right)$, then $N^{*}=\infty$, i.e., the unit should be replaced only at failure, and

$$
\begin{aligned}
C_{2}(\infty) & \equiv \lim _{N \rightarrow \infty} C_{2}(N) \\
& =\frac{c_{K}}{T \sum_{n=0}^{\infty}\left[\prod_{i=0}^{n} \bar{L}(i a T)\right]}=\frac{c_{K}}{E\{Y\}}
\end{aligned}
$$

In particular, when $L(x)=1-\mathrm{e}^{-\theta x},(5.10)$ is

$$
\left[1-\mathrm{e}^{-a \theta T(N+1)}\right] \sum_{n=0}^{N-1} \mathrm{e}^{-a \theta T[n(n+1) / 2]}+\mathrm{e}^{-a \theta T[N(N+1) / 2]} \geq \frac{c_{K}}{c_{K}-c_{N}}
$$

and

$$
Q(\infty)=\sum_{n=0}^{\infty} \mathrm{e}^{-a \theta T[n(n+1) / 2]}
$$

Example 5.2. Suppose that a failure level $K$ is normally distributed with mean $k$ and standard deviation $\sigma$, and furthermore, $a T=1$, i.e., $\bar{L}(n a T)=[1 /(\sqrt{2 \pi} \sigma)] \int_{n}^{\infty} \exp \left[-(x-k)^{2} /\left(2 \sigma^{2}\right)\right] \mathrm{d} x(n=0,1,2, \cdots)$. Then, Table 5.1 presents the optimum replacement number $N^{*}$ and the mean time $E\{Y\}$ to failure for $k=10,20,50$ and $\sigma=1,2,5,10$ when $c_{K} / c_{N}=5$.

Another single method of such replacements is to balance the cost of replacement at failure against that at nonfailure, i.e., $c_{K} \times(5.6) \geq c_{N} \times(5.7)$. In this case,

$$
\prod_{n=1}^{N} \bar{L}(n a T) \leq \frac{c_{K}}{c_{K}+c_{N}}
$$

and a minimum $\widetilde{N}$ to satisfy it is also presented in Table 5.1. This indicates that the values of $N^{*}, \widetilde{N}$, and $E\{Y\}$ decrease with $\sigma$ because the variance of a failure level becomes larger. Furthermore, when $\sigma=1$, the unit should be replaced before failure at $68.2 \%, 83.9 \%, 93.5 \%$ of the mean failure time for $k=10,20,50$, respectively, and $N^{*}=k-3 \sigma$ for all $k$. When $\sigma$ is small, the approximate $\widetilde{N}$ gives a good upper bound of $N^{*}$. It is of interest that $k>E\{Y\} / T>\widetilde{N}>N^{*}$ for $\sigma \geq 2$.

# 5.3 Deteriorated Inspection Model 

We introduce the replacement policy for the cumulative damage model where a unit is checked at periodic times $n T(n=1,2, \ldots)$ [197]. It has been generallyTable 5.1. Comparison of optimum number $N^{*}$, approximate value $\bar{N}$, and mean time $E\{Y\} / T$ to failure when $a T=1$ and $c_{K} / c_{N}=5$

| $\sigma$ | $k=10$ |  |  | $k=20$ |  |  | $k=50$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $N^{*}$ | $\bar{N}$ | $E\{Y\} / T$ | $N^{*}$ | $\bar{N}$ | $E\{Y\} / T$ | $N^{*}$ | $\bar{N}$ | $E\{Y\} / T$ |
| 1 | 7 | 9 | 10.27 | 17 | 19 | 20.27 | 47 | 49 | 50.27 |
| 2 | 5 | 8 | 9.51 | 15 | 18 | 19.51 | 44 | 48 | 49.51 |
| 5 | 2 | 4 | 6.40 | 8 | 13 | 15.99 | 36 | 43 | 45.99 |
| 10 | 1 | 1 | 3.91 | 3 | 5 | 9.55 | 23 | 33 | 38.38 |

assumed that any inspection does not degrade a unit [1]. On the other hand, the inspection policy for a storage system that is degraded with time and at each inspection was proposed [198]. This could be applied to the periodic test of electric equipment in storage [199].

This section considers the cumulative damage model where a unit suffers some damage and deterioration caused by both shocks and inspections and fails when the total damage has exceeded a failure level $K$ (Figure 5.1). A unit is checked to detect a failure at periodic times $n T(n=1,2, \ldots)$, where $T$ is previously given, i.e., the failure is detected only through inspection. In addition, to prevent failures, a unit is replaced before failure with a new one at a planned time $N T$.

# 5.3.1 Expected Cost 

Suppose that the number of shocks in $[0, t]$ is $N(t)$, and the probability that $j$ shocks occur in $[0, t]$ is $F_{j}(t) \equiv \operatorname{Pr}\{N(t) \geq j\}$ defined in Section 3.1. An amount $W_{j}$ of damage due to the $j$ th shock has an identical distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}, G^{(j)}(x)$ is the $j$-fold Stieltjes convolution of $G(x)$ with itself, and $G^{(0)}(x) \equiv 1$ for $x \geq 0$. Furthermore, the unit is checked at periodic times $n T(n=1,2, \ldots)$, where the inspection time is negligible, and each inspection causes a constant and nonnegative amount $w$ of damage to the unit. Let $\bar{N}$ denote the upper number of inspections until the unit fails, i.e., $\bar{N} \equiv[K / w]$, where $[x]$ denotes the greatest integer contained in $x$ and $N=\infty$ whenever $w=0$.

From the assumption that the unit fails when the total damage has exceeded $K$, the reliability function $\bar{\Phi}(t)$ that it does not fail in time $t$ for $n T<t \leq(n+1) T(n=0,1,2, \ldots, \bar{N})$ is given by

$$
\bar{\Phi}(t) \equiv \operatorname{Pr}\left\{\sum_{j=0}^{N(t)} W_{j}+n w \leq K\right\}=\sum_{j=0}^{\infty} G^{(j)}(K-n w)\left[F_{j}(t)-F_{j+1}(t)\right]
$$

A unit is always replaced at the first inspection when the total damage has exceeded $K$. To prevent a failure, the unit is also replaced before failure

Fig. 5.1. Process for periodic inspection with deteriorated factor $w$
at the $N$ th inspection $(N=1,2, \ldots, \bar{N})$. Let us introduce three costs given in (5.4). Costs $c_{K}$ and $c_{T}$ are incurred for each replacement and inspection, respectively, and $c_{D}$ is incurred for the time elapsed between a failure and its detection per unit of time. Then, the expected cost until replacement is, from 8.1 of $[1]$ and $(5.4)$,

$$
\begin{aligned}
& \sum_{n=0}^{N-1} \int_{n T}^{(n+1) T}\left\{c_{T}(n+1)+c_{D}[(n+1) T-t]\right\} \mathrm{d} \Phi(t)+c_{T} N \bar{\Phi}(N T)+c_{K} \\
& \quad=\left(c_{T}+c_{D} T\right) \sum_{n=0}^{N-1} \bar{\Phi}(n T)-c_{D} \sum_{n=0}^{N-1} \int_{n T}^{(n+1) T} \bar{\Phi}(t) \mathrm{d} t+c_{K}
\end{aligned}
$$

and the mean time to replacement is

$$
\sum_{n=0}^{N-1}[(n+1) T] \int_{n T}^{(n+1) T} \mathrm{~d} \Phi(t)+(N T) \bar{\Phi}(N T)=T \sum_{n=0}^{N-1} \bar{\Phi}(n T)
$$

where $\Phi(t) \equiv 1-\bar{\Phi}(t)$.
Therefore, the expected cost rate is, from (5.16) and (5.17),

$$
\begin{gathered}
C(N)=\frac{\left(c_{T}+c_{D} T\right) \sum_{n=0}^{N-1} \bar{\Phi}(n T)-c_{D} \sum_{n=0}^{N-1} \int_{n T}^{(n+1) T} \bar{\Phi}(t) \mathrm{d} t+c_{K}}{T \sum_{n=0}^{N-1} \bar{\Phi}(n T)} \\
(N=1,2, \ldots, \bar{N})
\end{gathered}
$$# 5.3.2 Optimum Policy 

We find an optimum planned number $N^{*}$ that minimizes the expected cost rate $C(N)$ in (5.18). Forming the inequality $C(N+1) \geq C(N)$,

$$
\begin{aligned}
\sum_{n=0}^{N-1} \int_{n T}^{(n+1) T} \bar{\Phi}(t) \mathrm{d} t-\frac{\sum_{n=0}^{N-1} \bar{\Phi}(n T)}{\bar{\Phi}(N T)} \int_{N T}^{(N+1) T} \bar{\Phi}(t) \mathrm{d} t \geq \frac{c_{K}}{c_{D}} \\
(N=1,2, \ldots \bar{N})
\end{aligned}
$$

Denoting the left-hand side of (5.19) by $Q(N)$,

$$
Q(N+1)-Q(N)=\sum_{n=0}^{N} \bar{\Phi}(n T)\left[\frac{\int_{N T}^{(N+1) T} \bar{\Phi}(t) \mathrm{d} t}{\bar{\Phi}(N T)}-\frac{\int_{(N+1) T}^{(N+2) T} \bar{\Phi}(t) \mathrm{d} t}{\bar{\Phi}((N+1) T)}\right]
$$

First, prove that if the failure rate of $\Phi(t)$ is strictly increasing, then (5.20) is positive, i.e., $Q(N)$ is strictly increasing in $N$. From the definition of the failure rate, if the failure rate of $\Phi(t)$ is increasing, then $\bar{\Phi}(t+x) / \bar{\Phi}(t)$ is decreasing in $t$ for any $x>0[1$, p. 7]. Thus, because

$$
\frac{\int_{N T}^{(N+1) T} \bar{\Phi}(t) \mathrm{d} t}{\bar{\Phi}(N T)}=\frac{\int_{0}^{T} \bar{\Phi}(t+N T) \mathrm{d} t}{\bar{\Phi}(N T)}
$$

we can prove that if the failure rate of $\Phi(t)$ is increasing, then $\bar{\Phi}(t+$ $N T) / \bar{\Phi}(N T)$ is decreasing in $N T$ for any $0<t<T$, i.e., $\int_{N T}^{(N+1) T} \bar{\Phi}(t) \mathrm{d} t / \bar{\Phi}(N T)$ is decreasing in $N$, and hence, $Q(N+1)-Q(N) \geq 0$.

Therefore, we have the following optimum policy when the failure rate of $\Phi(t)$ is strictly increasing:
(i) If $Q(\bar{N})>c_{K} / c_{D}$, then there exists a unique minimum $N^{*}$ that satisfies (5.19).
(ii) If $Q(\bar{N}) \leq c_{K} / c_{D}$, then $N^{*}=\bar{N}+1$, i.e., the unit is always replaced after failure.

Example 5.3. Suppose that shocks occur in a Poisson process with rate $\lambda$ and the amount of damage due to each shock has an exponential distribution $\left(1-\mathrm{e}^{-\mu x}\right)$, that is,

$$
F_{j}(t)=\sum_{i=j}^{\infty} \frac{(\lambda t)^{i}}{i!} \mathrm{e}^{-\lambda t}, \quad G^{(j)}(x)=\sum_{i=j}^{\infty} \frac{(\mu x)^{i}}{i!} \mathrm{e}^{-\mu x} \quad(j=0,1,2, \ldots)
$$

and $\Phi(t)$ in (5.15) is, for $n T<t \leq(n+1) T(n=0,1,2, \ldots, \bar{N})$,

$$
\bar{\Phi}(t)=\sum_{j=0}^{\infty} \frac{(\lambda t)^{j}}{j!} \mathrm{e}^{-\lambda t} \sum_{i=j}^{\infty} \frac{[\mu(K-n w)]^{i}}{i!} \mathrm{e}^{-\mu(K-n w)}
$$Table 5.2. Optimum number $N^{*}$ and expected cost rate $C\left(N^{*}\right)$ for $\mu w$ and $\lambda c_{K} / c_{D}$ when $\lambda T=5, \lambda=1, c_{D}=1, c_{T}=1$, and $\mu K=100$

| $\mu w$ | $\bar{N}$ | $N^{*}$ |  |  | $C\left(N^{*}\right)$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | $\lambda c_{K} / c_{D}$ |  |  | $\lambda c_{K} / c_{D}$ |  |  |
|  |  | 1 | 5 | 10 | 1 | 5 | 10 |
| 0 | $\infty$ | 15 | 17 | 19 | 0.214 | 0.264 | 0.323 |
| 1 | 100 | 13 | 15 | 16 | 0.216 | 0.274 | 0.340 |
| 2 | 50 | 11 | 13 | 14 | 0.218 | 0.284 | 0.359 |
| 3 | 33 | 10 | 11 | 12 | 0.220 | 0.295 | 0.379 |
| 4 | 25 | 9 | 10 | 11 | 0.222 | 0.304 | 0.398 |
| 5 | 20 | 8 | 9 | 10 | 0.225 | 0.314 | 0.416 |
| 6 | 16 | 8 | 9 | 9 | 0.226 | 0.323 | 0.435 |
| 7 | 14 | 7 | 8 | 9 | 0.229 | 0.332 | 0.454 |
| 8 | 12 | 7 | 8 | 8 | 0.230 | 0.343 | 0.480 |
| 9 | 11 | 6 | 7 | 8 | 0.233 | 0.350 | 0.490 |
| 10 | 10 | 6 | 7 | 7 | 0.234 | 0.360 | 0.505 |

The failure rate of $\bar{\Phi}(t)$ is

$$
r(t) \equiv \frac{\Phi^{\prime}(t)}{\bar{\Phi}(t)}=\frac{\lambda \sum_{j=0}^{\infty}\left[(\lambda t)^{j} / j!\left[G^{(j)}(x)-G^{(j+1)}(x)\right]\right.}{\sum_{j=0}^{\infty}\left[(\lambda t)^{j} / j!\right] G^{(j)}(x)}
$$

where $x \equiv K-n w$. Note from Section 2.3 that $r(t)$ is strictly increasing.
Table 5.2 presents the optimum number $N^{*}$ and $\bar{N}=[100 / \mu w]$ for $\mu w=0$, $1, \ldots, 10$ and $\lambda c_{K} / c_{D}=1,5,10$ when $\lambda T=5, c_{T}=1, \mu K=100$, and the resulting cost rate $C\left(N^{*}\right)$ when $\lambda=1$ and $c_{D}=1$. For example, when $\lambda T=5$, $\mu w=5$, and $\lambda c_{K} / c_{D}=1, N^{*}=8$, that is, when shocks occur 5 times a week and the unit fails at about $K /(5 / \mu+w)=10$ weeks, on the average, it should be replaced at 8 weeks. The optimum $N^{*}$ decreases to 1 with $\mu w$. The reason would be that the mean time to replacement greatly decreases with $\mu w$. Conversely, $C\left(N^{*}\right)$ slowly increases with $\mu w$, because the decrease of the total cost would influence less $C\left(N^{*}\right)$ than the time to failure. It is of interest that $N^{*}+\mu w$ decreases first, is constant for a while, and increases slowly with $\mu w$.

# 5.4 Replacement with Minimal Repair 

It has been assumed in all models that a unit is always replaced at failure. We apply the periodic replacement with minimal repair at failure (Chapter 4 of [1]) to a cumulative damage model.

Consider a cumulative damage model as shown in Section 2.1: Shocks occur in a renewal process with a general distribution $F(t)$ having finite mean $1 / \lambda$,and an amount of damage due to each shock has an identical distribution $G(x)$. In this case, the distribution of the total damage $Z(t)$ at time $t$ is given in (2.3). In addition, a unit fails with probability $p(x)$, that is increasing in $x$ from 0 to 1 , when the total damage becomes $x$ at shocks, and undergoes only minimal repair at failures, where the total damage remains undisturbed by any minimal repair. To prevent failures, a unit is replaced at a planned time $T$, at a shock number $N$, or at a damage level $Z$, whichever occurs first. Strictly speaking, the policy where a unit is replaced at $N$ or $Z$ is not periodic. However, denoting one cycle from the beginning of operation to the replacement at $N$ or $Z$, the policy forms a renewal process and the time of each cycle is nearly periodic.

# 5.4.1 Expected Cost 

A unit fails with probability $p(x)$ when the total damage becomes $x$ at each shock in the cumulative damage model and undergoes only minimal repair at failures, i.e., its damage remains undisturbed by minimal repair and its time for minimal repair is negligible. It is assumed that a unit is replaced at time $T$, at shock $N$, or at damage $Z$, whichever occurs first. The probability that the unit is replaced at time $T$ is, from (3.1),

$$
P_{T}=\sum_{j=0}^{N-1}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(Z)
$$

the probability that it is replaced at shock $N$ is, from (3.2),

$$
P_{N}=F^{(N)}(T) G^{(N)}(Z)
$$

and the probability that it is replaced at damage $Z$ is, from (3.3),

$$
P_{Z}=\sum_{j=0}^{N-1} F^{(j+1)}(T)\left[G^{(j)}(Z)-G^{(j+1)}(Z)\right]
$$

that includes the probability that the total damage has exceeded $Z$ at shock $N$. It is clearly seen that $P_{T}+P_{N}+P_{Z}=1$.

Furthermore, the mean time to replacement is

$$
\begin{aligned}
& T \sum_{j=0}^{N-1}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(Z)+G^{(N)}(Z) \int_{0}^{T} t \mathrm{~d} F^{(N)}(t) \\
& \quad+\sum_{j=0}^{N-1}\left[G^{(j)}(Z)-G^{(j+1)}(Z)\right] \int_{0}^{T} t \mathrm{~d} F^{(j+1)}(t) \\
& =\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} t
\end{aligned}
$$that is equal to (3.5) by replacing $F_{j}(t)$ with $F^{(j)}(t)$. Similarly, the expected number of failures before replacement is

$$
\begin{aligned}
& \sum_{j=1}^{N-1}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] \sum_{i=1}^{j} \int_{0}^{Z} p(x) \mathrm{d} G^{(i)}(x)+F^{(N)}(T) \sum_{j=1}^{N-1} \int_{0}^{Z} p(x) \mathrm{d} G^{(j)}(x) \\
& =\sum_{j=1}^{N-1} F^{(j)}(T) \int_{0}^{Z} p(x) \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Let $c_{M}$ be the cost of minimal repair, and $c_{k}(k=T, N, Z)$ be the replacement cost at $k$. Then, the expected cost rate is, summing up $c_{T} P_{T}+c_{N} P_{N}+$ $c_{Z} P_{Z}+c_{M} \times(5.25)$ and dividing by $(5.24)$,

$$
\begin{aligned}
& c_{Z}-\left(c_{Z}-c_{T}\right) \sum_{j=0}^{N-1}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(Z) \\
& -\left(c_{Z}-c_{N}\right) F^{(N)}(T) G^{(N)}(Z) \\
C(T, N, Z)= & \frac{+c_{M} \sum_{j=1}^{N-1} F^{(j)}(T) \int_{0}^{Z} p(x) \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{N-1} G^{(j)}(Z) \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} t}
\end{aligned}
$$

# 5.4.2 Optimum Policies 

We discuss analytically optimum $T^{*}, N^{*}$, and $Z^{*}$ that minimize the expected cost rates when $p(x)=1-\mathrm{e}^{-\theta x}(0<1 / \theta<\infty)$. In this case, the probability that the unit fails at shock $j$ is

$$
\int_{0}^{\infty} p(x) \mathrm{d} G^{(j)}(x)=\int_{0}^{\infty}\left(1-\mathrm{e}^{-\theta x}\right) \mathrm{d} G^{(j)}(x)=1-\left[G^{*}(\theta)\right]^{j}
$$

where $G^{*}(\theta)$ denotes the Laplace-Stieltjes transform of $G(x)$, i.e., $G^{*}(\theta) \equiv$ $\int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} G(x)<1$ for $\theta>0$.

## (1) Optimum $T^{*}$

A unit is replaced only at time $T$ (Figure 5.2). Then, from (5.26),

$$
C_{1}(T) \equiv \lim _{\substack{N \rightarrow \infty \\ Z \rightarrow \infty}} C(T, N, Z)=\frac{1}{T}\left[c_{M} \sum_{j=1}^{\infty} F^{(j)}(T)\left\{1-\left[G^{*}(\theta)\right]^{j}\right\}+c_{T}\right]
$$

that agrees with (5.2) of block replacement by replacing $\Phi(t)$ with $F(t)$ when $G^{*}(\theta) \equiv 0$. We seek an optimum time $T^{*}$ that minimizes $C_{1}(T)$ when $G^{*}(\theta)>$ 0 . Differentiating $C_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
\sum_{j=1}^{\infty}\left[T f^{(j)}(T)-F^{(j)}(T)\right]\left\{1-\left[G^{*}(\theta)\right]^{j}\right\}=\frac{c_{T}}{c_{M}}
$$

Fig. 5.2. Process for periodic replacement at time $T$
where $f(t)$ is a density function of $F(t)$ and $f^{(j)}(t)$ is the $j$-fold convolution of $f(t)$ with itself.

In particular, shocks occur in a Poisson process with rate $\lambda$, i.e., $F^{(j)}(t)=$ $\sum_{i=j}^{\infty}\left[(\lambda t)^{i} / i!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$. Then, (5.28) is rewritten as

$$
1-\left\{1+\lambda T\left[1-G^{*}(\theta)\right]\right\} \mathrm{e}^{-\lambda T\left[1-G^{*}(\theta)\right]}=\frac{1-G^{*}(\theta)}{G^{*}(\theta)} \frac{c_{T}}{c_{M}}
$$

The left-hand side of (5.29) is a gamma distribution of order 2 that increases from 0 to 1 . Thus, we have the optimum policy:
(i) If $G^{*}(\theta) /\left[1-G^{*}(\theta)\right]>c_{T} / c_{M}$, then there exist a finite and unique $T^{*}$ that satisfies (5.29), and the resulting cost rate is

$$
C_{1}\left(T^{*}\right)=\lambda c_{M}\left\{1-G^{*}(\theta) \mathrm{e}^{-\lambda T^{*}\left[1-G^{*}(\theta)\right]}\right\}
$$

(ii) If $G^{*}(\theta) /\left[1-G^{*}(\theta)\right] \leq c_{T} / c_{M}$, then $T^{*}=\infty$, i.e., the unit is not be replaced, and $C_{1}(\infty)=\lambda c_{M}$.
It is of interest that

$$
\sum_{j=1}^{\infty} \int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} G^{(j)}(x)=\int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} M_{G}(x)=\frac{G^{*}(\theta)}{1-G^{*}(\theta)}
$$

represents the expected number of nonfailures for an infinite interval, where $M_{G}(x) \equiv \sum_{j=1}^{\infty} G^{(j)}(x)$. In general, the expected number for actual models would be greater than the ratio $c_{T} / c_{M}$ of two costs. Furthermore, from (5.29), $T^{*}$ is given approximately by

$$
\widetilde{T}=\frac{1}{\lambda} \sqrt{\frac{1}{G^{*}(\theta)\left[1-G^{*}(\theta)\right]} \frac{c_{T}}{c_{M}}}
$$

and $T^{*}>\widetilde{T}$.

# (2) Optimum $N^{*}$ 

A unit is replaced only at shock $N$ (Figure 5.3). Then, from (5.26),

Fig. 5.3. Process for replacement at shock $N$

$$
\begin{aligned}
C_{2}(N) & \equiv \lim _{\frac{T \rightarrow \infty}{Z \rightarrow \infty}} C(T, N, Z) \\
& =\frac{\lambda}{N}\left[c_{M} \sum_{j=0}^{N-1}\left\{1-\left[G^{*}(\theta)\right]^{j}\right\}+c_{N}\right] \quad(N=1,2, \cdots)
\end{aligned}
$$

Forming the inequality $C_{2}(N+1)-C_{2}(N) \geq 0$,

$$
\frac{1-\left[G^{*}(\theta)\right]^{N}}{1-G^{*}(\theta)}-N\left[G^{*}(\theta)\right]^{N} \geq \frac{c_{N}}{c_{M}} \quad(N=1,2, \cdots)
$$

The left-hand side of (5.32) is strictly increasing to $1 /\left[1-G^{*}(\theta)\right]$. Thus, we have the optimum policy:
(i) If $1 /\left[1-G^{*}(\theta)\right]>c_{N} / c_{M}$, then there exists a finite and unique minimum number $N^{*}\left(1 \leq N^{*}<\infty\right)$ that satisfies (5.32), and its resulting cost rate is

$$
\lambda c_{M}\left\{1-\left[G^{*}(\theta)\right]^{N^{*}-1}\right\}<C_{2}\left(N^{*}\right) \leq \lambda c_{M}\left\{1-\left[G^{*}(\theta)\right]^{N^{*}}\right\}
$$

(ii) If $1 /\left[1-G^{*}(\theta)\right] \leq c_{N} / c_{M}$, then $N^{*}=\infty$ and $C_{2}(\infty)=C_{1}(\infty)$.

It is clearly seen that if $1-G^{*}(\theta) \geq c_{N} / c_{M}$, then $N^{*}=1$.
It has been assumed until now that shocks occur in a renewal process. If shocks occur in a nonhomogeneous Poisson process with an intensity function $h(t)$ and a mean value function $H(t)$, as shown in (2.16), the mean time to the $N$ th shock is, from (1.29),

$$
\sum_{j=0}^{N-1} \int_{0}^{\infty} \frac{[H(t)]^{j}}{j!} \mathrm{e}^{-H(t)} \mathrm{d} t
$$

and hence, the expected cost rate is

$$
\widetilde{C}_{2}(N)=\frac{c_{M} \sum_{j=0}^{N-1}\left\{1-\left[G^{*}(\theta)\right]^{j}\right\}+c_{N}}{\sum_{j=0}^{N-1} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t} \quad(N=1,2, \cdots)
$$

where $p_{j}(t) \equiv\{[H(t)]^{j} / j!\} \mathrm{e}^{-H(t)}(j=0,1,2, \ldots)$. When $G^{*}(\theta) \equiv 0, \widetilde{C}_{2}(N)$ agrees with (4.40).We also seek an optimum $N^{*}$ that minimizes $\widetilde{C}_{2}(N)$ in (5.34). Forming the inequality $\widetilde{C}_{2}(N+1)-\widetilde{C}_{2}(N) \geq 0$

$$
\begin{gathered}
\left\{1-\left[G^{*}(\theta)\right]^{N}\right\} \frac{\sum_{j=0}^{N-1} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}-\sum_{j=0}^{N-1}\left\{1-\left[G^{*}(\theta)\right]^{j}\right\} \geq \frac{c_{N}}{c_{M}} \\
(N=1,2, \ldots)
\end{gathered}
$$

It is assumed that the intensity function $h(t)$ is increasing. Then, letting $Q(N)$ be the left-hand side of (5.35), it can be proved that
$Q(N+1)-Q(N)=\sum_{j=0}^{N} \int_{0}^{\infty} p_{j}(t) \mathrm{d} t\left\{\frac{1-\left[G^{*}(\theta)\right]^{N+1}}{\int_{0}^{\infty} p_{N+1}(t) \mathrm{d} t}-\frac{1-\left[G^{*}(\theta)\right]^{N}}{\int_{0}^{\infty} p_{N}(t) \mathrm{d} t}\right\}>0$,
because $\int_{0}^{\infty} p_{N}(t) \mathrm{d} t$ is deceasing in $N$ to $1 / h(\infty)$ from (1.29). Thus, we have the optimum policy when $h(t)$ is increasing:
(i) If $Q(\infty)>c_{N} / c_{M}$, then there exists a finite and unique minimum number $N^{*}\left(1 \leq N^{*}<\infty\right)$ that satisfies (5.35), and its resulting cost rate is

$$
\frac{c_{M}\left[1-G^{*}(\theta)\right]^{N^{*}-1}}{\int_{0}^{\infty} p_{N^{*}-1}(t) \mathrm{d} t}<\widetilde{C}_{2}\left(N^{*}\right) \leq \frac{c_{M}\left[1-G^{*}(\theta)\right]^{N^{*}}}{\int_{0}^{\infty} p_{N^{*}}(t) \mathrm{d} t}
$$

(ii) If $Q(\infty) \leq c_{N} / c_{M}$, then $N^{*}=\infty$ and $\widetilde{C}_{2}(\infty)=c_{M} h(\infty)$.

Furthermore, we have the inequality

$$
Q(N) \geq \frac{\left\{1-\left[G^{*}(\theta)\right]^{N}\right\}}{\lambda \int_{0}^{\infty} p_{N}(t) \mathrm{d} t}
$$

where $1 / \lambda \equiv \int_{0}^{\infty} \mathrm{e}^{-H(t)} \mathrm{d} t$, because $\int_{0}^{\infty} p_{N}(t) \mathrm{d} t$ is deceasing in $N$. Therefore, if

$$
\lim _{N \rightarrow \infty} \frac{\left\{1-\left[G^{*}(\theta)\right]^{N}\right\}}{\lambda \int_{0}^{\infty} p_{N}(t) \mathrm{d} t}=\frac{h(\infty)}{\lambda}>\frac{c_{N}}{c_{M}}
$$

then a finite solution to (5.35) exists uniquely. Clearly, if $h(t)$ goes to $\infty$, as $t \rightarrow \infty$, then a finite $N^{*}$ always exists.

# (3) Optimum $Z^{*}$ 

A unit is replaced only at damage $Z$ (Figure 5.4). Then, from (5.26),

$$
\begin{aligned}
C_{3}(Z) & \equiv \lim _{\substack{T \rightarrow \infty \\
N \rightarrow \infty}} C(T, N, Z) \\
& =\frac{c_{M} \int_{0}^{Z} p(x) \mathrm{d} M_{G}(x)+c_{Z}}{\left[1+M_{G}(Z)\right] / \lambda}
\end{aligned}
$$

Fig. 5.4. Process for replacement at damage $Z$

Differentiating $C_{3}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\int_{0}^{Z}\left[1+M_{G}(x)\right] \mathrm{d} p(x)=\frac{c_{Z}}{c_{M}}
$$

that is strictly increasing in $Z$. Thus, if $\int_{0}^{\infty}\left[1+M_{G}(x)\right] \mathrm{d} p(x)>c_{Z} / c_{M}$, then there exists a finite and unique $Z^{*}\left(0<Z^{*}<\infty\right)$ that satisfies (5.38).

In particular, when $p(x)=1-\mathrm{e}^{-\theta x}$,

$$
\int_{0}^{\infty}\left[1+M_{G}(x)\right] \mathrm{d} p(x)=\frac{1}{1-G^{*}(\theta)}
$$

Therefore, we have the optimum policy:
(i) If $1 /\left[1-G^{*}(\theta)\right]>c_{Z} / c_{M}$, then there exists a finite and unique $Z^{*}$ that satisfies (5.38), and its resulting cost rate is

$$
C_{3}\left(Z^{*}\right)=\lambda c_{M} p\left(Z^{*}\right)
$$

(ii) If $1 /\left[1-G^{*}(\theta)\right] \leq c_{Z} / c_{M}$, then $Z^{*}=\infty$, and $C_{3}(\infty)=C_{1}(\infty)$.

Example 5.4. Table 5.3 presents the optimum time $T^{*}$ satisfying (5.29) and expected cost rate $C_{1}\left(T^{*}\right)$ in (5.30), and the optimum number $N^{*}$ satisfying (5.32) and expected cost rate $C_{2}\left(N^{*}\right)$ in (5.31) for $c_{k}(k=T, N)=5-20$Table 5.3. Optimum time $T^{*}$, expected cost rate $C_{1}\left(T^{*}\right) / c_{M}$, and optimum shock number $N^{*}$, expected cost rate $C_{2}\left(N^{*}\right) / c_{M}$ when $c_{M}=5, \lambda=1$ and $G^{*}(\theta)=0.9$

| $c_{k}$ | $T^{*}$ | $C_{1}\left(T^{*}\right) / c_{M}$ | $N^{*}$ | $C_{2}\left(N^{*}\right) / c_{M}$ |
| --: | :--: | :--: | :--: | :--: |
| 5 | 5.67 | 0.489 | 5 | 0.381 |
| 6 | 6.34 | 0.523 | 6 | 0.419 |
| 7 | 7.00 | 0.553 | 6 | 0.452 |
| 8 | 7.62 | 0.580 | 7 | 0.483 |
| 9 | 8.25 | 0.606 | 7 | 0.512 |
| 10 | 8.86 | 0.629 | 8 | 0.538 |
| 11 | 9.46 | 0.651 | 8 | 0.563 |
| 12 | 10.07 | 0.671 | 9 | 0.586 |
| 13 | 10.67 | 0.690 | 9 | 0.608 |
| 14 | 11.28 | 0.709 | 10 | 0.629 |
| 15 | 11.89 | 0.726 | 10 | 0.649 |
| 16 | 12.51 | 0.742 | 11 | 0.667 |
| 17 | 13.13 | 0.758 | 11 | 0.685 |
| 18 | 13.77 | 0.773 | 12 | 0.702 |
| 19 | 14.41 | 0.787 | 13 | 0.719 |
| 20 | 15.07 | 0.801 | 13 | 0.734 |

when $c_{M}=5, \lambda=1$, and $G^{*}(\theta)=0.9$. In this case, finite $T^{*}$ and $N^{*}$ exist uniquely for $c_{T}<45$ and $c_{N}<50$, and the expected number of nonfailures is $G^{*}(\theta) /\left[1-G^{*}(\theta)\right]=9$.

If $c_{N} \leq c_{T}$, then the replacement with shock $N$ is better than that with time $T$, and if $c_{N} \geq c_{T}+c_{M}$, then the replacement with time $T$ is better than that with shock $N$. In the case of $c_{T}<c_{N}<c_{T}+c_{M}$, for example, when $c_{T}=10$ and $c_{N}=14$, both replacement policies are almost the same.

# 5.5 Modified Replacement Models 

## (1) Replacement with Threshold Level

Consider the periodic replacement policy in which a unit is replaced at time $n T(n=1,2, \ldots)$. If the total damage $Z(T)$ has exceeded a threshold level $K$ between planned replacements, the total cost would be higher than anticipated [197]. The other assumptions are the same as those in Section 5.3 except minimal repair at failures. Let $c_{0}(x)$ be an additional replacement cost for the total damage $x$ defined in (1) of Section 3.3. Then, the expected cost rate is, from $(3.29)$,$$
\begin{aligned}
C(T)=\frac{1}{T} & {\left[\sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right]\left\{\int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)\right.\right.} \\
& \left.\left.+\int_{K}^{\infty}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)\right\}\right]
\end{aligned}
$$

where $c_{T}$ and $c_{K}$ are the replacement cost at time $n T$ when $Z(T) \leq K$ and $Z(T)>K$, respectively.

# (2) Replacement at the Next Shock over Time $T$ 

A unit is not replaced at time $T$. After $T$, it is replaced at the next shock and undergoes minimal repair at failures between replacements (see (3) of Section (3.3)). Because the mean time to replacement is, from (5.40) of [1],

$$
\begin{aligned}
& \sum_{j=0}^{\infty} \int_{0}^{T}\left[\int_{T-t}^{\infty}(t+u) \mathrm{d} F(u)\right] \mathrm{d} F^{(j)}(t) \\
& =T+\int_{T}^{\infty} \bar{F}(t) \mathrm{d} t+\int_{0}^{T}\left[\int_{T-t}^{\infty} \bar{F}(u) \mathrm{d} u\right] \mathrm{d} M_{F}(t)
\end{aligned}
$$

the expected cost rate is, from (5.27),

$$
\widetilde{C}_{1}(T)=\frac{c_{M} \sum_{j=1}^{\infty} F^{(j)}(T)\left\{1-\left[G^{*}(\theta)\right]^{j}\right\}+c_{T}}{T+\int_{T}^{\infty} \bar{F}(t) \mathrm{d} t+\int_{0}^{T}\left[\int_{T-t}^{\infty} \bar{F}(u) \mathrm{d} u\right] \mathrm{d} M_{F}(t)}
$$

In particular, when $F(t)=1-\mathrm{e}^{-\lambda t}$,

$$
\frac{\widetilde{C}_{1}(T)}{\lambda}=\frac{c_{M}\left\{\lambda T-\left[G^{*}(\theta) /\left(1-G^{*}(\theta)\right)\right]\left[1-\mathrm{e}^{-\lambda T\left[1-G^{*}(\theta)\right]}\right]\right\}+c_{T}}{\lambda T+1}
$$

When $T=0$, i.e., the unit is always replaced at the first shock, the expected cost rate is $\widetilde{C}_{1}(0)=\lambda c_{T}$, and when the unit is replaced never, it is $\widetilde{C}_{1}(\infty)=$ $\lambda c_{M}$.

We seek an optimum time $T^{*}\left(0 \leq T^{*} \leq \infty\right)$ that minimizes $\widetilde{C}_{1}(T)$ in (5.43). Differentiating $\widetilde{C}_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
1-(1+\lambda T) G^{*}(\theta) \mathrm{e}^{-\lambda T\left[1-G^{*}(\theta)\right]}+\frac{G^{*}(\theta)}{1-G^{*}(\theta)}\left\{1-\mathrm{e}^{-\lambda T\left[1-G^{*}(\theta)\right]}\right\}=\frac{c_{T}}{c_{M}}
$$

The left-hand side of (5.44) is strictly increasing from $1-G^{*}(\theta)$ to $1 /\left[1-G^{*}(\theta)\right]$. Thus, we have the optimum policy:
(i) If $1-G^{*}(\theta) \geq c_{T} / c_{M}$, then $T^{*}=0$.(ii) If $1-G^{*}(\theta)<c_{T} / c_{M}<1 /\left[1-G^{*}(\theta)\right]$, then there exists a finite and unique $T^{*}\left(0<T^{*}<\infty\right)$ that satisfies (5.44), and the resulting cost rate is

$$
\widetilde{C}_{1}\left(T^{*}\right)=\lambda c_{M}\left\{1-G^{*}(\theta) \mathrm{e}^{-\lambda T^{*}\left[1-G^{*}(\theta)\right]}\right\}
$$

(iii) If $1 /\left[1-G^{*}(\theta)\right] \leq c_{T} / c_{M}$, then $T^{*}=\infty$.

For example, when $G^{*}(\theta)=0.9, T^{*}=0$ for $c_{T} / c_{M} \leq 0.1,0<T^{*}<\infty$ for $0.1<c_{T} / c_{M}<10$, and $T^{*}=\infty$ for $c_{T} / c_{M} \geq 10$. It is clearly seen that $T^{*}$ to satisfy (5.44) is smaller than that to satisfy (5.29).

# (3) Replacement at the Next Shock over Damage $Z$ 

A unit is replaced at the next shock when the total damage has exceeded a threshold level $Z$. Then, the expected number of failures before replacement is

$$
\begin{aligned}
& \sum_{j=0}^{\infty}\left\{\int_{0}^{Z} p(x) \mathrm{d} G^{(j)}(x)+\int_{0}^{Z}\left[\int_{Z-x}^{\infty} p(x+y) \mathrm{d} G(y)\right] \mathrm{d} G^{(j)}(x)\right\} \\
& =\int_{0}^{\infty} p(x) \mathrm{d} G(x)+\int_{0}^{Z}\left[\int_{0}^{\infty} p(x+y) \mathrm{d} G(y)\right] \mathrm{d} M_{G}(x)
\end{aligned}
$$

Furthermore, the mean time to replacement increases by the mean shock time $1 / \lambda$ in the denominator of (5.37). Thus, the expected cost rate is

$$
\frac{\widetilde{C}_{3}(Z)}{\lambda}=\frac{c_{M}\left\{\int_{0}^{\infty} p(x) \mathrm{d} G(x)+\int_{0}^{Z}\left[\int_{0}^{\infty} p(x+y) \mathrm{d} G(y)\right] \mathrm{d} M_{G}(x)\right\}+c_{Z}}{2+M_{G}(Z)}
$$

Differentiating $\widetilde{C}_{3}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\begin{gathered}
{\left[2+M_{G}(Z)\right] \int_{0}^{\infty} p(Z+x) \mathrm{d} G(x)-\int_{0}^{Z}\left[\int_{0}^{\infty} p(x+y) \mathrm{d} G(y)\right] \mathrm{d} M_{G}(x)} \\
-\int_{0}^{\infty} p(x) \mathrm{d} G(x)=\frac{c_{Z}}{c_{M}}
\end{gathered}
$$

Letting $Q(Z)$ be the left-hand side of (5.47), we easily see that $Q(Z)$ is strictly increasing from $\int_{0}^{\infty} p(x) \mathrm{d} G(x)$ to $Q(\infty)$. Thus, we have the optimum policy:
(i) If $\int_{0}^{\infty} p(x) \mathrm{d} G(x) \geq c_{Z} / c_{M}$, then $Z^{*}=0$, and

$$
\frac{\widetilde{C}_{3}(0)}{\lambda}=\frac{c_{M} \int_{0}^{\infty} p(x) \mathrm{d} x+c_{Z}}{2}
$$

(ii) If $\int_{0}^{\infty} p(x) \mathrm{d} G(x)<c_{Z} / c_{M}<Q(\infty)$, then there exists a finite and unique $Z^{*}\left(0<Z^{*}<\infty\right)$ that satisfies (5.47), and the resulting cost rate is

$$
\widetilde{C}_{3}\left(Z^{*}\right)=\lambda c_{M} \int_{0}^{\infty} p\left(Z^{*}+x\right) \mathrm{d} G(x)
$$(iii) If $Q(\infty) \leq c_{Z} / c_{M}$, then $Z^{*}=\infty$.

It is clearly seen that

$$
Q(Z) \geq 2 \int_{0}^{\infty} p(Z+x) \mathrm{d} G(x)-\int_{0}^{\infty} p(x) \mathrm{d} G(x)
$$

because $p(x)$ is increasing in $x$. Therefore, if $2-\int_{0}^{\infty} p(x) \mathrm{d} G(x)>c_{Z} / c_{M}$, i.e., $\int_{0}^{\infty}[1-p(x)] \mathrm{d} G(x)>\left(c_{Z}-c_{M}\right) / c_{M}$ then a finite $Z^{*}$ exists.
Example 5.5. Suppose that $G(x)=1-\mathrm{e}^{-\mu x}$ and $p(x)=1-\mathrm{e}^{-\theta x}$. Then, we compare the expected cost rates $C_{3}(Z)$ in (5.37) and $\widetilde{C}_{3}(Z)$ in (5.46) numerically. Under such assumptions, the expected cost rate $C_{3}(Z)$ is rewritten as

$$
\frac{C_{3}(Z)}{\lambda}=\frac{c_{M}\left[\mu Z-(\mu / \theta)\left(1-\mathrm{e}^{-\theta Z}\right)\right]+c_{Z}}{1+\mu Z}
$$

and if $(\mu+\theta) / \theta>c_{Z} / c_{M}$, then there exists a finite and unique $Z_{1}^{*}$ that satisfies

$$
\left(1+\frac{\mu}{\theta}\right)\left(1-\mathrm{e}^{-\theta Z}\right)-\mu Z \mathrm{e}^{-\theta Z}=\frac{c_{Z}}{c_{M}}
$$

The expected cost rate $\widetilde{C}_{3}(Z)$ is

$$
\frac{\widetilde{C}_{3}(Z)}{\lambda}=\frac{c_{M}[\theta /(\mu+\theta)]+\mu\left\{Z-[\mu /(\theta(\mu+\theta))]\left(1-\mathrm{e}^{-\theta Z}\right)\right\}+c_{Z}}{2+\mu Z}
$$

and if $(\mu+\theta) / \theta>c_{Z} / c_{M}>\theta /(\mu+\theta)$, then there exists a finite and unique $Z_{2}^{*}$ that satisfies

$$
1-\frac{\mu}{\mu+\theta}(1+\mu Z) \mathrm{e}^{-\theta Z}+\frac{\mu}{\theta}\left(1-\mathrm{e}^{-\theta Z}\right)=\frac{c_{Z}}{c_{M}}
$$

Because

$$
1-\frac{\mu}{\mu+\theta}(1+\mu Z) \mathrm{e}^{-\theta Z}+\frac{\mu}{\theta}\left(1-\mathrm{e}^{-\theta Z}\right)>\left(1+\frac{\mu}{\theta}\right)\left(1-\mathrm{e}^{-\theta Z}\right)-\mu Z \mathrm{e}^{-\theta Z}
$$

$Z_{1}^{*}>Z_{2}^{*}$.
Table 5.4 presents the optimum values of $Z_{1}^{*}$ and $Z_{2}^{*}$ that minimize $C_{3}(Z)$ and $\widetilde{C}_{3}(Z)$, respectively, and their resulting cost rates $C_{3}\left(Z_{1}^{*}\right) / \lambda$ and $\widetilde{C}_{3}\left(Z_{2}^{*}\right) / \lambda$ for $c_{Z}=5-20$ when $c_{M}=5$ and $G^{*}(\theta)=0.9$, i.e., $\mu / \theta=9$. In this case, both finite and positive $Z_{1}^{*}$ and $Z_{2}^{*}$ exist uniquely for $0.5<c_{Z}<50$, and $C_{3}\left(Z_{1}^{*}\right)<\widetilde{C}_{3}\left(Z_{2}^{*}\right)$ and $\theta Z_{1}^{*}<\theta / \mu+\theta Z_{2}^{*}$. However, their differences between two expected costs become smaller, as $c_{Z}$ becomes larger. If the replacement $\operatorname{cost} c_{Z}$ is less than that of (3) in Section 5.4.2, this policy might be more useful than the policy of (3).Table 5.4. Optimum damage level $Z_{1}^{*}$, expected cost rate $C_{3}\left(Z_{1}^{*}\right)$, and damage level $Z_{2}^{*}$, expected cost rate $\widetilde{C}_{3}\left(Z_{2}^{*}\right)$ when $c_{M}=5$ and $\mu / \theta=9$

| $c_{Z}$ | $\theta Z_{1}^{*}$ | $C_{3}\left(Z_{1}^{*}\right) / \lambda$ | $\theta Z_{2}^{*}$ | $\widetilde{C}_{3}\left(Z_{2}^{*}\right) / \lambda$ |
| :--: | :--: | :--: | :--: | :--: |
| 5 | 0.437 | 1.770 | 0.342 | 1.804 |
| 6 | 0.498 | 1.963 | 0.402 | 1.991 |
| 7 | 0.557 | 2.136 | 0.461 | 2.161 |
| 8 | 0.615 | 2.296 | 0.517 | 2.317 |
| 9 | 0.670 | 2.443 | 0.573 | 2.462 |
| 10 | 0.726 | 2.581 | 0.627 | 2.597 |
| 11 | 0.781 | 2.709 | 0.682 | 2.724 |
| 12 | 0.835 | 2.830 | 0.735 | 2.843 |
| 13 | 0.889 | 2.944 | 0.789 | 2.956 |
| 14 | 0.943 | 3.053 | 0.843 | 3.063 |
| 15 | 0.997 | 3.155 | 0.897 | 3.165 |
| 16 | 1.052 | 3.253 | 0.951 | 3.262 |
| 17 | 1.107 | 3.347 | 1.006 | 3.354 |
| 18 | 1.162 | 3.435 | 1.061 | 3.443 |
| 19 | 1.218 | 3.521 | 1.117 | 3.528 |
| 20 | 1.275 | 3.603 | 1.174 | 3.609 |# Preventive Maintenance Policies 

Most operating units are repaired or replaced when they have failed. If a failed unit undergoes repair, it begins to operate again after the repair completion. However, it may require much time and high cost to repair a failed unit. It may sometimes be necessary to maintain a unit to prevent failures. Some maintenance after failure and before failure is called corrective maintenance (CM) and preventive maintenance (PM), respectively. Optimum PM policies for some units were summarized [1,200-202]. The modified PM policy that is planned only at periodic times was proposed in Section 6.3 of [1].

PM actions are generally grouped into time maintenance that is based on the planned time, age, or usage time of a unit, and monitored maintenance or condition-based maintenance that is based on the condition of a unit [203]. The first maintenance corresponds to the replacement policies discussed in Chapters $3-5$ in [1] and the maintenance that is done at a planned time $T$ or number $N$ in Chapters $3-5$. The latter maintenance is done by monitoring one or more variables charactering the wear, fatigue, and damage of an operating unit and corresponds to the maintenance that is done at a damage level $Z$ or at a shock number $N$ in Chapters $3-5$.

This chapter takes up the modified PM policy [56] and applies it to a condition-based PM of a cumulative damage model, where the CM is done immediately when the total damage due to shocks has exceeded a failure level $K$. The test to investigate some characteristics of an operating unit is planned at periodic times $n T(n=1,2, \cdots)$. We can know the characteristics such as the damage and the shock number only through tests, and if necessary, we do some appropriate maintenance.

In Section 6.1, if the total damage has exceeded a threshold level $Z$ $(0 \leq Z \leq K)$, the PM is done at the first planned time, when shocks occur in a nonhomogeneous Poisson process. The expected cost rate is obtained, and an optimum $Z^{*}$ that minimizes it is discussed analytically. Furthermore, in Section 6.2, the modified PM models, where (1) the failure is detected only through tests, (2) the PM is done when the total number of shocks has exceeded a threshold number $N$, and (3) the PM is done at time $N T$, are pro-posed. The expected cost rates of each model are obtained, and a numerical example to compare them is given.

# 6.1 Condition-based Preventive Maintenance 

We consider a condition-based PM policy where the condition of an operating unit is monitored at inspection times. If the condition is normal, the operation is continued. However, if the condition reaches a previously determined threshold level of resistance to failure, the PM is done before failure. Such PM policies have been actually in use for engines, mainflames, control systems of aircraft [204], and plants in the chemical and machine industries.

Condition-based maintenance models for a deteriorating system are generally classified into continuous wear processes [192,193] and Markovian deterioration processes [205-208]. In the former case, the preventive replacement level of a one-unit system whose condition is monitored at inspection times was considered, and optimum levels to minimize the expected cost and the availability were derived [194-196, 209-211]. This was extended to a two-unit series system [196].

This section adopts the condition-based PM policy for a cumulative damage model: A unit suffers damage due to shocks, and fails when the total amount of additive damage has exceeded a failure level $K$. Then, the CM is done immediately. The test is planned at periodic times $n T(n=1,2, \cdots)$ to prevent failures, where $T(>0)$ means a week, a month, or a year. It is assumed that we can know the total damage to a unit only through tests. If the total damage has exceeded a threshold level $Z(0 \leq Z \leq K)$ at time $n T$, the PM or overhaul is done before failure. Otherwise, no PM should be done.

Suppose that shocks occur in a nonhomogeneous Poisson process. Then, using the theory of a Poisson process and the results of Section 6.3 of [1], we obtain the expected cost rate and determine an optimum damage level $Z^{*}$ that minimizes it. In particular, when shocks occur in a Poisson process, an optimum $Z^{*}$ is given by a unique solution of the equation.

### 6.1.1 Expected Cost Rate

Consider a unit that should operate over an infinite time interval: Shocks occur in a nonhomogeneous Poisson process with an intensity function $h(t)$ and a mean value function $H(t)$, i.e., $H(t) \equiv \int_{0}^{t} h(u) \mathrm{d} u$ represents the expected number of shocks in $[0, t]$, and $p_{j}[H(t)] \equiv\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}(j=0,1,2, \cdots)$ is the probability that $j$ shocks occur exactly in $[0, t]$. In addition, random variables $\left\{W_{j}\right\}(j=1,2, \cdots)$ denote an amount of damage due to the $j$ th shock and are nonnegative, independent, and identically distributed. Each $W_{j}$ is statistically estimated and has an identical distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$ $(j=1,2, \cdots)$. Each amount of damage is additive, and $G^{(j)}(x)$ denotes the$j$-fold Stieltjes convolution of $G(x)$ with itself $(j=1,2, \cdots)$ and $G^{(0)}(x) \equiv 1$ for $x \geq 0$. A unit fails only when the total damage has exceeded a failure level $K$, and then the CM is done.

Under the above assumptions, the test is planned at periodic times $n T$ $(n=1,2, \cdots)$ to investigate the total damage, where a positive $T$ is given. If the total damage has exceeded a threshold level $Z(0 \leq Z \leq K)$ during $(n T,(n+1) T](n=0,1,2, \cdots)$, then its damage can be known through the test at time $(n+1) T$, and the PM is done immediately (Figure 6.1). Otherwise, the unit is left as it is. The unit becomes as good as a new one at each PM or CM, i.e., the PM is perfect. The imperfect PM policy for a cumulative damage model will be discussed in Chapter 7. The times required for any test and maintenance are negligible, i.e., the time considered here is measured only by the total operating time.

We obtain the expected cost rate by a method similar to Section 6.3 of [1] and [56]. The probability that $j$ shocks occur during $[0, n T]$ and the total damage is less than $Z$, and $i$ shocks occur during $(n T,(n+1) T]$ and the total damage has exceeded $K$, is

$$
\begin{aligned}
& p_{j}[H(n T)] p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times \operatorname{Pr}\left\{W_{1}+\cdots+W_{j} \leq Z \text { and } W_{1}+\cdots+W_{j}+\cdots+W_{j+i}>K\right\} \\
& =p_{j}[H(n T)] p_{i}[H((n+1) T)-H(n T)] \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Thus, the probability that the unit fails and the CM is done immediately is

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Conversely, the probability that the PM is done at time $(n+1) T(n=$ $0,1,2, \cdots)$ when the total damage is between $Z$ and $K$ during $(n T,(n+1) T]$ is

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times \operatorname{Pr}\left\{W_{1}+\cdots+W_{j} \leq Z \text { and } Z<W_{1}+\cdots+W_{j}+\cdots+W_{j+i} \leq K\right\} \\
& =\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times \int_{0}^{Z}\left[G^{(i)}(K-x)-G^{(i)}(Z-x)\right] \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

It is proved that $(6.1)+(6.2)=1$, because, from the reproductive property of a Poisson distribution,

Fig. 6.1. Process for PM at damage $Z$

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(Z)-G^{(i+j)}(Z)\right] \\
& =\sum_{n=0}^{\infty}\left\{\sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(Z)\right. \\
& \left.\quad-\sum_{i=0}^{\infty} G^{(i)}(Z) \sum_{j=0}^{i} p_{j}[H(n T)] p_{i-j}[H((n+1) T)-H(n T)]\right\} \\
& =\sum_{n=0}^{\infty}\left\{\sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(Z)-\sum_{i=0}^{\infty} p_{i}[H((n+1) T)] G^{(i)}(Z)\right\}=1
\end{aligned}
$$

The mean time to either PM or CM is$$
\begin{aligned}
& \sum_{n=0}^{\infty}[(n+1) T] \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times \int_{0}^{Z}\left[G^{(i)}(K-x)-G^{(i)}(Z-x)\right] \mathrm{d} G^{(j)}(x) \\
& \quad+\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{n T}^{(n+1) T} t p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t \\
& \quad \times \int_{0}^{Z}\left[G^{(i)}(K-x)-G^{(i+1)}(K-x)\right] \mathrm{d} G^{(j)}(x) \\
& =\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x) \\
& \quad \times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$

Let $c_{Z}$ be the PM cost before failure and $c_{K}$ be the CM cost after failure with $c_{K}>c_{Z}$. Then, the expected cost rate is, summing up $c_{K} \times(6.1)+c_{Z} \times$ (6.2) and dividing by (6.3),

$$
\begin{gathered}
c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \\
C_{1}(Z)=\frac{\times \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)}{\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x)} \\
\times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{gathered}
$$

Each amount of damage during $(n T,(n+1) T]$ is investigated only through tests and has an identical distribution $G(x)$ for all $n(n=0,1,2, \cdots)$. This corresponds to a cumulative damage model where shocks occur at every constant time $T$ and the total damage is known at the end of each period. In this case, the expected cost rate is obtained by replacing $1 / \lambda$ with $T$ in (3.24), and the optimum policy has been derived in (3) of Section 3.2.

Next, a failure level $K$ is statistically distributed, i.e., $K$ is a random variable and has a general distribution $L(x) \equiv \operatorname{Pr}\{K \leq x\}$. Then, the expected cost rate in (6.4) is rewritten as

$$
\begin{aligned}
& c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
C_{1}(Z)= & \frac{\times \int_{0}^{Z}\left\{\int_{0}^{\infty}[L(x+y)-L(x)] \mathrm{d} G^{(i)}(y)\right\} \mathrm{d} G^{(j)}(x)}{\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z}\left\{\int_{0}^{\infty}[1-L(x+y)] \mathrm{d} G^{(i)}(y)\right\} \mathrm{d} G^{(j)}(x)} . \\
& \times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$# 6.1.2 Optimum Policy 

We seek an optimum threshold level $Z^{*}$ that minimizes the expected cost rate $C_{1}(Z)$ in (6.4) when shocks occur in a Poisson process, i.e., $p_{j}[H(n T)]=$ $\left[(n \lambda T)^{j} / j!\right] \mathrm{e}^{-n \lambda T} \equiv p_{j}(n \lambda T)(j=0,1,2, \cdots)$. Differentiating $C_{1}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\begin{aligned}
& Q_{1}(Z) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x) \\
& -\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} p_{i}(\lambda T) \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
\end{aligned}
$$

where

$$
Q_{1}(Z) \equiv \frac{\sum_{i=0}^{\infty} p_{i}(\lambda T)\left[1-G^{(i)}(K-Z)\right]}{\sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t G^{(i)}(K-Z)}
$$

It can be easily seen that $Q_{1}(Z)$ is increasing in $Z$ from $Q_{1}(0)$ to $\lambda$. Denoting the left-hand side of (6.6) by $Q_{2}(Z), Q_{2}(0)=0$,

$$
\begin{aligned}
Q_{2}(K) & =\sum_{n=0}^{\infty} \sum_{i=0}^{\infty} G^{(i)}(K) \int_{n T}^{(n+1) T} \lambda p_{i}(\lambda t) \mathrm{d} t-1=\sum_{i=1}^{\infty} G^{(i)}(K) \\
\frac{\mathrm{d} Q_{2}(Z)}{\mathrm{d} Z} & =\frac{\mathrm{d} Q_{1}(Z)}{\mathrm{d} Z} \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

It is assumed that the distribution $G(x)$ of each amount of damage due to shocks is continuous and strictly increasing. Then, $Q_{2}(Z)$ is also strictly increasing from 0 to $M_{G}(K) \equiv \sum_{j=1}^{\infty} G^{(j)}(K)$ that represents the expected number of shocks before the failure. Therefore, we have the following optimum policy:
(i) If $M_{G}(K)>c_{Z} /\left(c_{K}-c_{Z}\right)$, then there exists a unique $Z^{*}\left(0<Z^{*}<K\right)$ that satisfies (6.6), and the resulting cost rate is

$$
C_{1}\left(Z^{*}\right)=\left(c_{K}-c_{Z}\right) Q_{1}\left(Z^{*}\right)
$$

(ii) If $M_{G}(K) \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$, and the CM is done after failure. In this case, the expected cost rate is

$$
\frac{C_{1}(K)}{\lambda}=\frac{c_{K}}{1+M_{G}(K)}
$$

that agrees with (3.12).
This policy will be applied to a garbage collection model in Section 8.3, and an optimum level $Z^{*}$ is computed numerically in Example 8.3.# 6.2 Modified Models 

We show the following modified models: (1) any failures are detected only through tests, (2) the PM is done when the total number of shocks has exceeded a threshold number $N$, and (3) the PM is done at time $N T$. The expected cost rates of each model are obtained.

## (1) PM only at Test

Suppose that any failures are detected only through tests. When the unit fails during $(n T,(n+1) T]$, it is not detected immediately, but is detected only at time $(n+1) T$ and the CM is done. Then, the mean time to either PM or CM is

$$
\begin{aligned}
& \sum_{n=0}^{\infty}[(n+1) T] \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \\
& \quad \times\left\{\int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)\right. \\
& \left.\quad+\int_{0}^{Z}\left[G^{(i)}(K-x)-G^{(i)}(Z-x)\right] \mathrm{d} G^{(j)}(x)\right\} \\
& \quad=T \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(Z)
\end{aligned}
$$

Furthermore, the mean time from a failure to its detection is, from (6.3),

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{n T}^{(n+1) T}[(n+1) T-t] p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t \\
& \quad \times \int_{0}^{Z}\left[G^{(i)}(K-x)-G^{(i+1)}(K-x)\right] \mathrm{d} G^{(j)}(x) \\
& =\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x) \\
& \quad \times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$

where note that $(6.3)+(6.10)=(6.9)$. From this relation,

$$
T \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(K) \geq \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}[H(t)] \mathrm{d} t
$$

that is the mean time to failure given in (2.19).Let $c_{D}$ be the loss cost per unit of time elapsed between a failure and its detection. Then, the expected cost rate is, from (6.4),

$$
\begin{aligned}
& c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \\
& \times \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x) \\
& -c_{D} \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x) \\
\widetilde{C}_{1}(Z)= & \frac{\times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t}{T \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(Z)} \\
& +c_{D}
\end{aligned}
$$

Compared with the expected cost rate $C_{1}(Z)$ in (6.4), $\widetilde{C}_{1}(Z)$ is smaller than $C_{1}(Z)$ when $c_{D}=0$, and is larger as $c_{D}$ increases. Thus, if the PM and CM costs are the same, $\widetilde{C}_{1}(Z)$ would be larger than $C_{1}(Z)$ when $c_{D}$ is greater than some fixed cost.

When shocks occur in a Poisson process with rate $\lambda$, the expected cost rate $\widetilde{C}_{1}(Z)$ is rewritten as

$$
\begin{aligned}
& c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} p_{i}(\lambda T) \\
& \times \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x) \\
& -c_{D} \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t \\
\widetilde{C}_{1}(Z)= & \frac{\times \int_{0}^{Z} G^{(i)}(K-x) \mathrm{d} G^{(j)}(x)}{T \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) G^{(j)}(Z)}+c_{D}
\end{aligned}
$$

To find an optimum $Z^{*}$ that minimizes $\widetilde{C}_{1}(Z)$, differentiating $\widetilde{C}_{1}(Z)$ with respect to $Z$ and setting it equal to zero,

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty}\left[p_{i}(\lambda T)+\frac{c_{D}}{c_{K}-c_{Z}} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t\right] \\
& \quad \times \int_{K-Z}^{K} G^{(j)}(K-x) \mathrm{d} G^{(i)}(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
\end{aligned}
$$

Denoting the left-hand side of (6.14) by $\widetilde{Q}(Z)$, we easily find that $\widetilde{Q}(Z)$ is strictly increasing from 0 to

$$
\widetilde{Q}(K)=\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) G^{(j)}(K)+\frac{c_{D} / \lambda}{c_{K}-c_{Z}} \sum_{j=0}^{\infty} G^{(j)}(K)-1
$$

Therefore, we have the following optimum policy:
(i) If $\widetilde{Q}(K)>c_{Z} /\left(c_{K}-c_{Z}\right)$, then there exists a unique $Z^{*}\left(0<Z^{*}<K\right)$ that satisfies (6.14), and the resulting cost rate is

$$
\widetilde{C}_{1}\left(Z^{*}\right)=\frac{1}{T} \sum_{i=0}^{\infty}\left[1-G^{(i)}\left(K-Z^{*}\right)\right]\left[\left(c_{K}-c_{Z}\right) p_{i}(\lambda T)+c_{D} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t\right]
$$(ii) If $\widetilde{Q}(K) \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$, and the expected cost rate is

$$
\widetilde{C}_{1}(K)=\frac{c_{K}-\left(c_{D} / \lambda\right) \sum_{j=0}^{\infty} G^{(j)}(K)}{T \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) G^{(j)}(K)}+c_{D}
$$

From (6.11), because we have the inequality

$$
\widetilde{Q}(K) \geq\left(\frac{1}{\lambda T}+\frac{c_{D} / \lambda}{c_{K}-c_{Z}}\right)\left[1+M_{G}(K)\right]-1
$$

if

$$
\frac{1+M_{G}(K)}{\lambda T}>\frac{c_{K}}{c_{K}-c_{Z}+T c_{D}}
$$

then a unique $Z^{*}$ to satisfy (6.14) exists.

# (2) PM at Shock Number 

Suppose that the number of shocks is known only through tests. When the total number of shocks has exceeded a prespecified number $N$ before failure during $(n T,(n+1) T]$, the PM is done at time $(n+1) T$. Then, by a method similar to (6.1) and (6.2), the probability that the CM is done after failure is

$$
\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right]
$$

and the probability that the PM is done before failure is

$$
\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=N-j}^{\infty} p_{i}[H((n+1) T)-H(n T)] G^{(i+j)}(K)
$$

where note that $(6.17)+(6.18)=1$. The mean time to either PM or CM is

$$
\begin{aligned}
& \sum_{n=0}^{\infty}[(n+1) T] \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=N-j}^{\infty} p_{i}[H((n+1) T)-H(n T)] G^{(i+j)}(K) \\
& \quad+\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty}\left[G^{(i+j)}(K)-G^{(i+j+1)}(K)\right] \\
& \quad \times \int_{n T}^{(n+1) T} t p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t \\
& =\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty} G^{(i+j)}(K) \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$

Therefore, the expected cost rate is, summing up $c_{K} \times(6.17)+c_{N} \times(6.18)$ and dividing by $(6.19)$,$$
\begin{gathered}
c_{N}+\left(c_{K}-c_{N}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \\
C_{2}(N)=\frac{\times \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right]}{\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty} G^{(i+j)}(K)} \\
\times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t \\
(N=1,2, \cdots)
\end{gathered}
$$

where $c_{N}$ is the PM cost at shock $N$.
If the failure is detected only through tests in the same way as (1), then the mean time to either PM or CM is

$$
\begin{aligned}
& \sum_{n=0}^{\infty}[(n+1) T] \sum_{j=0}^{N-1} p_{j}[H(n T)] \\
& \quad \times\left\{\sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right]\right. \\
& \left.\quad+\sum_{i=N-j}^{\infty} p_{i}[H((n+1) T)-H(n T)] G^{(i+j)}(K)\right\} \\
& \quad=T \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] G^{(j)}(K)
\end{aligned}
$$

and the mean time from a failure to its detection is

$$
\begin{aligned}
& \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty}\left[G^{(i+j)}(K)-G^{(i+j+1)}(K)\right] \\
& \quad \times \int_{n T}^{(n+1) T}[(n+1) T-t] p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t \\
& =\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty}\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$

where $(6.19)+(6.22)=(6.21)$. In this case, the expected cost rate is

$$
\begin{aligned}
& c_{N}+\left(c_{K}-c_{N}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \\
& \times \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \\
& -c_{D} \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] \sum_{i=0}^{\infty} G^{(i+j)}(K) \\
\widetilde{C}_{2}(N)= & \frac{\times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t}{T \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}[H(n T)] G^{(j)}(K)} \\
& +c_{D} \quad(N=1,2, \cdots)
\end{aligned}
$$It would be troublesome to analyze optimum policies analytically that minimize $C_{2}(N)$ and $\widetilde{C}_{2}(N)$. In particular, we derive an optimum shock number $N^{*}$ that minimizes $\widetilde{C}_{2}(N)$ in (6.23) when $c_{D}=0$ and $p_{j}[H(t)]=$ $\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}=p_{j}(\lambda t)(j=0,1,2, \cdots)$. In this case, from the inequality $\widetilde{C}_{2}(N+1)-\widetilde{C}_{2}(N) \geq 0$

$$
\begin{aligned}
& {\left[1-\frac{\sum_{i=0}^{\infty} p_{i}(\lambda T) G^{(N+i)}(K)}{G^{(N)}(K)}\right] \sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}(n \lambda T) G^{(j)}(K)} \\
& -\sum_{n=0}^{\infty} \sum_{j=0}^{N-1} p_{j}(n \lambda T) \sum_{i=0}^{\infty} p_{i}(\lambda T)\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \geq \frac{c_{N}}{c_{K}-c_{N}} \\
& (N=1,2, \cdots)
\end{aligned}
$$

Denoting the left-hand side of (6.24) by $Q(N)$,

$$
\begin{aligned}
Q(N+1)-Q(N)= & {\left[\frac{\sum_{i=0}^{\infty} p_{i}(\lambda T) G^{(N+i)}(K)}{G^{(N)}(K)}-\frac{\sum_{i=0}^{\infty} p_{i}(\lambda T) G^{(N+1+i)}(K)}{G^{(N+1)}(K)}\right] } \\
& \times \sum_{n=0}^{\infty} \sum_{j=0}^{N} p_{j}(n \lambda T) G^{(j)}(K)
\end{aligned}
$$

Thus, if $\sum_{i=0}^{\infty} p_{i}(\lambda T) G^{(N+i)}(K) / G^{(N)}(K)$ is strictly decreasing in $N$ and $Q(\infty)>c_{N} /\left(c_{K}-c_{N}\right)$, there exists a unique minimum number $N^{*}(1 \leq$ $\left.N^{*}<\infty\right)$ that satisfies $(6.24)$.

For example, suppose that $G(x)=1-\mathrm{e}^{-\mu x}$, i.e., $G^{(j)}(x) \equiv \sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right]$ $\times \mathrm{e}^{-\mu x}(j=0,1,2, \cdots)$. Then,

$$
\begin{aligned}
& \sum_{i=0}^{\infty} p_{i}(\lambda T)\left[G^{(N+i)}(K) G^{(N+1)}(K)-G^{(N+i+1)}(K) G^{(N)}(K)\right] \\
& =\sum_{i=0}^{\infty} p_{i}(\lambda T) \mathrm{e}^{-2 \mu K} \sum_{j=0}^{\infty}(\mu K)^{N+i+j}\left[\frac{1}{(N+i)!(N+1)!}-\frac{1}{N!(N+i+1)!}\right]>0
\end{aligned}
$$

Thus, $\sum_{i=0}^{\infty} p_{i}(\lambda T) G^{(N+i)}(K) / G^{(N)}(K)$ is strictly decreasing to 0 , and

$$
Q(\infty) \equiv \lim _{N \rightarrow \infty} Q(N)=\sum_{n=1}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) G^{(j)}(K)
$$

Therefore, if $\sum_{n=1}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) G^{(j)}(K)>c_{N} /\left(c_{K}-c_{N}\right)$, then an optimum $N^{*}$ exists uniquely. Furthermore, from (6.11), if $(1+\mu K) /(\lambda T)>c_{K} /\left(c_{K}-\right.$ $\left.c_{N}\right)$, then a finite $N^{*}$ exists.

# (3) PM at Time $N T$ 

Suppose that we cannot know any damage level and shock number. The PM is done at time $N T$ or the CM is done after failure, whichever occurs first,that is the same policy as that of Section 5.2. Then, the probability that the CM is done after failure is

$$
\begin{aligned}
& \sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \\
& =\sum_{n=0}^{N-1} \sum_{j=0}^{\infty}\left\{p_{j}[H(n T)]-p_{j}[H((n+1) T)]\right\} G^{(j)}(K) \\
& =1-\sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K)
\end{aligned}
$$

and the probability that the PM is done at time $N T$ is

$$
\sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K)
$$

The mean time to either PM or CM is

$$
\begin{aligned}
& \sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty}\left[G^{(i+j)}(K)-G^{(i+j+1)}(K)\right] \\
& \quad \times \int_{n T}^{(n+1) T} t p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t+(N T) \sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K) \\
& =\sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} G^{(i+j)}(K) \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t \\
& =\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{N T} p_{j}[H(t)] \mathrm{d} t
\end{aligned}
$$

Therefore, the expected cost rate is

$$
C_{3}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) \sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{N T} p_{j}[H(t)] \mathrm{d} t} \quad(N=1,2, \cdots)
$$

where $c_{N}$ is the PM cost at time $N T$. The expected cost rate $C_{3}(N)$ agrees with $C_{1}(T)$ in (3.11) by replacing $T$ with $N T$ and $F^{(j)}(t)-F^{(j+1)}(t)$ with $p_{j}[H(t)]$.

Furthermore, when a failure level $K$ is statistically distributed according to a general distribution $L(x)$, the expected cost rate is

$$
\begin{array}{r}
C_{3}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) \sum_{j=0}^{\infty} p_{j}[H(N T)] \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)}{\sum_{j=0}^{\infty} \int_{0}^{N T} p_{j}[H(t)] \mathrm{d} t \int_{0}^{\infty} G^{(j)}(x) \mathrm{d} L(x)} \\
(N=1,2, \cdots)
\end{array}
$$Table 6.1. Optimum number $N^{*}$ and expected cost rate $C_{3}\left(N^{*}\right) / c_{N}$ when $1 / \lambda=$ $10^{3}, 10^{4}$, and $G^{*}(\theta)=0.9$

| $T$ | $1 / \lambda=10^{3}$ |  | $1 / \lambda=10^{4}$ |  |
| --: | :--: | :--: | :--: | :--: |
|  | $N^{*}$ | $C_{3}\left(N^{*}\right) / c_{N}$ | $N^{*}$ | $C_{3}\left(N^{*}\right) / c_{N}$ |
| 8 | 13 | 0.0479 | 41 | 0.0151 |
| 48 | 2 | 0.0466 | 7 | 0.0153 |
| 192 | 1 | 0.0557 | 2 | 0.0159 |
| 2304 | 1 | 0.0564 | 1 | 0.0178 |

In particular, when $L(x)=1-\mathrm{e}^{-\theta x}$, the expected cost rate is simplified as

$$
C_{3}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(N T)}}{\int_{0}^{N T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t} \quad(N=1,2, \cdots)
$$

that agrees with (9.1) of [1] by replacing $\bar{F}(t)$ with $\mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)}$. Thus, when the failure rate $h(t)$ is strictly increasing, the optimum policy is as follows:
(i) If $h(\infty)\left[1-G^{*}(\theta)\right] \int_{0}^{\infty} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t>c_{K} /\left(c_{K}-c_{N}\right)$, then there exists a finite and unique minimum number $N^{*}$ that satisfies

$$
\begin{gathered}
\frac{\mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(N T)}-\mathrm{e}^{-\left[1-G^{*}(\theta)\right] H((N+1) T)}}{\int_{N T}^{(N+1) T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t} \int_{0}^{N T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t \\
-\mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(N T)} \geq \frac{c_{K}}{c_{K}-c_{N}}
\end{gathered}
$$

(ii) If $h(\infty)\left[1-G^{*}(\theta)\right] \int_{0}^{\infty} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t \leq c_{K} /\left(c_{K}-c_{N}\right)$, then $N^{*}=\infty$, i.e., the unit is replaced only at failure and

$$
C_{3}(\infty)=\frac{c_{K}}{\int_{0}^{\infty} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t}
$$

Example 6.1. Suppose that $H(t)=\lambda t^{2}$, i.e., $h(t)=2 \lambda t$ that is strictly increasing to $\infty$. Thus, there exists a finite and unique minimum $N^{*}$ that satisfies (6.31). Table 6.1 presents the optimum $N^{*}$ and the resulting cost rate $C_{3}\left(N^{*}\right) / c_{N}$ for $T=8,48,192,2304$ when $c_{K} / c_{N}=5,1 / \lambda=10^{3}, 10^{4}$, and $G^{*}(\theta)=0.9$. For example, when $1 / \lambda=10^{4}$ and $T=48$, i.e., the unit is operating 8 hours per day and is inspected once a week, the PM is done every 7 weeks. Clearly, optimum values of $N^{*}$ decrease with $T$ and increase with $1 / \lambda$.If the failure is detected only at time $n T(n=1,2, \cdots)$, the mean time to either PM or CM is

$$
\begin{aligned}
& \sum_{n=0}^{N-1}[(n+1) T] \sum_{j=0}^{\infty} p_{j}[H(n t)] \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)]\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \\
& \quad+(N T) \sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K) \\
& =T \sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(K)
\end{aligned}
$$

and the mean time from a failure to its detection is

$$
\begin{aligned}
& \sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n t)] \sum_{i=0}^{\infty}\left[G^{(i+j)}(K)-G^{(i+j+1)}(K)\right] \\
& \quad \times \int_{n T}^{(n+1) T}[(n+1) T-t] p_{i}[H(t)-H(n T)] h(t) \mathrm{d} t \\
& =\sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty}\left[G^{(j)}(K)-G^{(i+j)}(K)\right] \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{aligned}
$$

Thus, the expected cost rate is

$$
\begin{gathered}
c_{K}-\left(c_{K}-c_{N}\right) \sum_{j=0}^{\infty} p_{j}[H(N T)] G^{(j)}(K) \\
\widetilde{C}_{3}(N)=\frac{-c_{D} \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{N T} p_{j}[H(t)] \mathrm{d} t}{T \sum_{n=0}^{N-1} \sum_{j=0}^{\infty} p_{j}[H(n T)] G^{(j)}(K)}+c_{D} \quad(N=1,2, \cdots)
\end{gathered}
$$

where $c_{D}$ is given in (6.12).
In addition, when a failure level $K$ is distributed according to an exponential distribution $L(x)=1-\mathrm{e}^{-\theta x}$, the expected cost rate is

$$
\begin{array}{r}
\widetilde{C}_{3}(N)=\frac{c_{K}-\left(c_{K}-c_{N}\right) \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(N T)}-c_{D} \int_{0}^{N T} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(t)} \mathrm{d} t}{T \sum_{n=0}^{N-1} \mathrm{e}^{-\left[1-G^{*}(\theta)\right] H(n T)}}+c_{D} \\
(N=1,2, \ldots)
\end{array}
$$# Imperfect Preventive Maintenance Policies 

The usual preventive maintenance (PM) of an operating unit is based on its age or operating time. Most models have assumed that the unit after PM becomes as good as new. Actually, this assumption might not be true. The unit after PM usually might be only younger, and its improvement would depend on the resources spent for PM. In such imperfect PM models where the unit after PM has the same failure rate as before PM, the age or failure rate after PM reduces in proportion to that before PM [212-214]. Some chapters [1,215-217] of recently published books summarized many results of imperfect maintenance.

The PM of large complex systems such as computers, radars, airplanes, and plants should be done frequently as the units age. A sequential PM policy where the PM is done at fixed intervals $T_{n}(n=1,2, \cdots, N)$ has been proposed $[218,219]$. In some practical situations, however, the PM seems only imperfect in the sense that it does not make the unit like new [220].

In this chapter, we apply a sequential PM policy to a cumulative damage model where each PM is imperfect [57]: The unit is subject to shocks that occur randomly in time, and upon the occurrence of shocks, it suffers a random damage that is additive. Each shock causes unit failure with probability $p(x)$ when the total damage is $x$. If the unit fails between PMs, it undergoes only minimal repair using the same assumption as that of Section 5.4. We introduce only an improvement factor in damage to describe imperfect PM actions: The amount of damage after the $n$th PM becomes $a_{n} Z_{n}$ when it was $Z_{n}$ before PM, i.e., the $n$th PM reduces the total damage $Z_{n}$ to $a_{n} Z_{n}$. This would be applied to related PM models in Chapter 6.

In Section 7.1, we obtain the expected cost rate when shocks occur in a Poisson process and $p(x)$ is exponential. In Section 7.2, we discuss three types of optimum policies that minimize the expected cost rate when the PM is done at periodic times and the improvement factor is constant, i.e., $T_{n}=T$ and $a_{n}=a$. Optimum number $N^{*}(T)$, optimum interval $T^{*}(N)$, and optimum $\left(N^{*}, T^{*}\right)$ are derived analytically. Numerical examples are presented to demonstrate potential usefulness of the results. Next, suppose in Section 7.4

Fig. 7.1. Process for Imperfect PM
that a unit has to be operating over a finite interval $(0, S]$. Then, setting $\sum_{n=1}^{N} T_{n}=S$, we compute numerically an optimum number $N^{*}$ and optimum times $T_{n}^{*}\left(n=1,2, \ldots, N^{*}-1\right)$ that minimize the expected cost until replacement. It is of great interest that the last PM time interval is the largest and the first PM one is the second, and they are first increasing, and then are decreasing.

# 7.1 Model and Expected Cost 

Consider a sequential PM policy that is done at fixed intervals $T_{n}(n=$ $1,2, \cdots, N$ ) and the replacement or the perfect PM is done at time $T_{N}$, i.e., a unit is as good as new at time $T_{N}$. We call an interval from the $(n-1)$ th PM to the $n$th PM period $n$ (Figure 7.1).

Suppose that shocks occur in a Poisson process with rate $\lambda$. Random variables $N_{n}(n=1,2, \cdots, N)$ denote the number of shocks in period $n$, i.e., $\operatorname{Pr}\left\{N_{n}=j\right\}=\left[\left(\lambda T_{n}\right)^{j} / j!\right] \exp \left(-\lambda T_{n}\right) \equiv p_{j}\left(T_{n}\right)(j=0,1,2, \cdots)$. In addition, we denote by $W_{n j}$ the amount of damage caused by the $j$ th shock in period $n$, where $W_{n 0} \equiv 0$. It is assumed that random variable $W_{n j}$ is nonnegative,independent, and identically distributed, and has an identical distribution $\operatorname{Pr}\left\{W_{n j} \leq x\right\} \equiv G(x)$ for all $n$ and $j$. The total damage is additive, and $G^{(j)}(x)(j=1,2, \cdots)$ is the $j$-fold Stieltjes convolution of $G(x)$ with itself and $G^{(0)}(x) \equiv 1$ for all $x \geq 0$. Then, it follows that

$$
\operatorname{Pr}\left\{W_{n 1}+W_{n 2}+\cdots+W_{n j} \leq x\right\}=G^{(j)}(x) \quad(j=0,1,2, \cdots)
$$

When the total damage becomes $x$ at shocks, the unit fails with probability $p(x)$, that is increasing in $x$ from 0 to 1 . If the unit fails between PMs, it undergoes only minimal repair, and hence, the total damage remains unchanged by any minimal repair. It is assumed that the times required for any PM and minimal repair are negligible.

Next, we introduce an improvement factor in PM: Suppose that the $n$th PM reduces $100\left(1-a_{n}\right) \%\left(0 \leq a_{n} \leq 1\right)$ of the total damage. Letting $Z_{n}$ be the total damage at the end of period $n$, i.e., just before the $n$th PM, the $n$th PM reduces it to $a_{n} Z_{n}$. During period $n$ the total damage is additive and is not removed because the failed unit undergoes only minimal repair. Thus, we have the relation

$$
Z_{n}=a_{n-1} Z_{n-1}+\sum_{j=1}^{N_{n}} W_{n j} \quad(n=1,2, \cdots, N)
$$

where $Z_{0} \equiv 0$ and $\sum_{j=1}^{0} \equiv 0$.
Let $c_{T}$ be the cost of each PM, $c_{N}$ be the cost of replacement at the $N$ th PM with $c_{N}>c_{T}$, and $c_{M}$ be the cost of minimal repair. Then, because the unit fails with probability $p(\cdot)$ only at shocks, the total cost in period $n$ is

$$
\begin{array}{r}
\widetilde{C}(n)=c_{T}+c_{M} \sum_{j=1}^{N_{n}} p\left(a_{n-1} Z_{n-1}+W_{n 1}+W_{n 2}+\cdots+W_{n j}\right) \\
(n=1,2, \cdots, N-1)
\end{array}
$$

Similarly, the total cost in period $N$ is

$$
\widetilde{C}(N)=c_{N}+c_{M} \sum_{j=1}^{N_{N}} p\left(a_{N-1} Z_{N-1}+W_{N 1}+W_{N 2}+\cdots+W_{N j}\right)
$$

To obtain the expectations of (7.3) and (7.4), we assume that $p(x)$ is exponential, i.e., $p(x)=1-\mathrm{e}^{-\theta x}$ for some constant $\theta>0$. Letting $G^{*}(\theta)$ be the Laplace-Stieltjes transform of $G(x)$, i.e., $G^{*}(\theta) \equiv \int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} G(x)$,

$$
E\left\{\exp \left[-\theta\left(W_{n 1}+W_{n 2}+\cdots+W_{n j}\right)\right]\right\}=\int_{0}^{\infty} \mathrm{e}^{-\theta x} \mathrm{~d} G^{(j)}(x)=\left[G^{*}(\theta)\right]^{j}
$$

The probability that the unit fails at the first shock is$$
\int_{0}^{\infty} p(x) \mathrm{d} G(x)=\int_{0}^{\infty}\left(1-\mathrm{e}^{-\theta x}\right) \mathrm{d} G(x)=1-G^{*}(\theta)
$$

Using the law of total probability in (7.3), the expected cost in period $n$ is

$$
\begin{aligned}
E\{\widetilde{C}(n)\}= & c_{T}+c_{M} E\left\{\sum_{j=1}^{N_{n}} p\left(a_{n-1} Z_{n-1}+W_{n 1}+W_{n 2}+\cdots+W_{n j}\right)\right\} \\
= & c_{T}+c_{M} \sum_{i=1}^{\infty} \operatorname{Pr}\left\{N_{n}=i\right\} \\
& \times \sum_{j=1}^{i} E\left\{1-\exp \left[-\theta\left(a_{n-1} Z_{n-1}+W_{n 1}+W_{n 2}+\cdots+W_{n j}\right)\right]\right\}
\end{aligned}
$$

Let $B_{n}^{*}(\theta) \equiv E\left\{\exp \left(-\theta Z_{n}\right)\right\}$. Then, because $Z_{n-1}$ and $W_{n j}$ are independent of each other, from (7.5),

$$
\begin{aligned}
& E\left\{1-\exp \left[-\theta\left(a_{n-1} Z_{n-1}+W_{n 1}+W_{n 2}+\cdots+W_{n j}\right)\right]\right\} \\
& \quad=1-B_{n-1}^{*}\left(\theta a_{n-1}\right)\left[G^{*}(\theta)\right]^{j}
\end{aligned}
$$

Thus, from the assumption that $N_{n}$ has a Poisson distribution with rate $\lambda$,

$$
\begin{aligned}
E\{\widetilde{C}(n)\} & =c_{T}+c_{M} \sum_{k=1}^{\infty} \frac{\left(\lambda T_{n}\right)^{k}}{k!} \mathrm{e}^{-\lambda T_{n}} \sum_{j=1}^{k}\left\{1-B_{n-1}^{*}\left(\theta a_{n-1}\right)\left[G^{*}(\theta)\right]^{j}\right\} \\
& =c_{T}+c_{M}\left[\lambda T_{n}-\frac{G^{*}(\theta)}{1-G^{*}(\theta)} B_{n-1}^{*}\left(\theta a_{n-1}\right)\left\{1-\mathrm{e}^{-\lambda T_{n}\left[1-G^{*}(\theta)\right]}\right\}\right] \\
& (n=1,2, \cdots, N-1)
\end{aligned}
$$

Similarly, the expected cost in period $N$ is

$$
E\{\widetilde{C}(N)\}=c_{N}+c_{M}\left[\lambda T_{N}-\frac{G^{*}(\theta)}{1-G^{*}(\theta)} B_{N-1}^{*}\left(\theta a_{N-1}\right)\left\{1-\mathrm{e}^{-\lambda T_{N}\left[1-G^{*}(\theta)\right]}\right\}\right]
$$

It remains to determine $B_{n-1}^{*}\left(\theta a_{n-1}\right)$. Let $A_{j}^{n} \equiv \prod_{i=j}^{n} a_{i}$ for $j \leq n$ and $\equiv 1$ for $j>n$. Then, from (7.2),

$$
\begin{aligned}
a_{n-1} Z_{n-1} & =a_{n-1} a_{n-2} Z_{n-2}+a_{n-1} \sum_{i=1}^{N_{n-1}} W_{n-1 i} \\
& =\sum_{j=1}^{n-1}\left(A_{j}^{n-1} \sum_{i=1}^{N_{j}} W_{j i}\right)
\end{aligned}
$$

so that,$$
B_{n-1}\left(\theta a_{n-1}\right)=E\left\{\mathrm{e}^{-\theta a_{n-1} Z_{n-1}}\right\}=E\left\{\exp \left[-\theta \sum_{j=1}^{n-1}\left(A_{j}^{n-1} \sum_{i=1}^{N_{j}} W_{j i}\right)\right]\right\}
$$

Recalling that $W_{j i}$ are independent and have an identical distribution $G(x)$,

$$
\begin{aligned}
E\left\{\exp \left(-\theta A_{j}^{n-1} \sum_{i=1}^{N j} W_{j i}\right)\right\} & =\sum_{k=0}^{\infty} \operatorname{Pr}\left\{N_{j}=k\right\} E\left\{\exp \left(-\theta A_{j}^{n-1} \sum_{i=1}^{k} W_{j i}\right)\right\} \\
& =\sum_{k=0}^{\infty} \frac{\left(\lambda T_{j}\right)^{k}}{k!} \mathrm{e}^{-\lambda T_{j}}\left[G^{*}\left(\theta A_{j}^{n-1}\right)\right]^{k} \\
& =\exp \left\{-\lambda T_{j}\left[1-G^{*}\left(\theta A_{j}^{n-1}\right)\right]\right\}
\end{aligned}
$$

and consequently,

$$
B_{n-1}^{*}\left(\theta a_{n-1}\right)=\exp \left\{-\sum_{j=1}^{n-1} \lambda T_{j}\left[1-G^{*}\left(\theta A_{j}^{n-1}\right)\right]\right\}
$$

Substituting (7.8) in (7.6) and (7.7), respectively, the expected costs in period $n$ are

$$
\begin{aligned}
E\{\widetilde{C}(n)\}= & c_{T}+c_{M}\left[\lambda T_{n}-\frac{G^{*}(\theta)}{1-G^{*}(\theta)} \exp \left\{-\sum_{j=1}^{n-1} \lambda T_{j}\left[1-G^{*}\left(\theta A_{j}^{n-1}\right)\right]\right\}\right. \\
& \left.\times\left\{1-\mathrm{e}^{-\lambda T_{n}\left[1-G^{*}(\theta)\right]}\right\}\right] \quad(n=1,2, \cdots, N-1)
\end{aligned}
$$

and

$$
\begin{aligned}
E\{\widetilde{C}(N)\}=c_{N}+c_{M} & {\left[\lambda T_{N}-\frac{G^{*}(\theta)}{1-G^{*}(\theta)} \exp \left\{-\sum_{j=1}^{N-1} \lambda T_{j}\left[1-G^{*}\left(\theta A_{j}^{N-1}\right)\right]\right\}\right.} \\
& \left.\times\left\{1-\mathrm{e}^{-\lambda T_{N}\left[1-G^{*}(\theta)\right]}\right\}\right]
\end{aligned}
$$

Therefore, the expected cost rate until replacement is, from (7.9) and $(7.10)$,

$$
\begin{aligned}
C_{1}\left(T_{1}, T_{2}, \cdots, T_{N}\right)= & \frac{\sum_{n=1}^{N-1} E\{\widetilde{C}(n)\}+E\{\widetilde{C}(N)\}}{\sum_{n=1}^{N} T_{n}} \\
& (N-1) c_{T}+c_{N}+c_{M}\left[\sum_{n=1}^{N} \lambda T_{n}-G^{*}(\theta) /\left[1-G^{*}(\theta)\right]\right. \\
& \times \sum_{n=1}^{N} \exp \left\{-\sum_{j=1}^{n-1} \lambda T_{j}\left[1-G^{*}\left(\theta A_{j}^{n-1}\right)\right]\right\} \\
= & \frac{\left.\times\left\{1-\mathrm{e}^{-\lambda T_{n}\left[1-G^{*}(\theta)\right]}\right\}\right]}{\sum_{n=1}^{N} T_{n}} \\
& (N=1,2, \cdots)
\end{aligned}
$$In the particular case of $N=1, C_{1}\left(T_{1}\right)$ agrees with (5.27) by replacing $c_{T}$ with $c_{N}$ and $F(T)=1-\mathrm{e}^{-\lambda T}$.

# 7.2 Optimum Policies 

The expected cost rate $C_{1}\left(T_{1}, T_{2}, \cdots, T_{N}\right)$ in (7.11) is very complicated, and we cannot analyze optimum policies. Suppose that $T_{n} \equiv T$ and $a_{n} \equiv a(0 \leq$ $a<1$ ), i.e., the PM is done at periodic times $n T(n=1,2, \cdots, N)$ and the improvement factor $a_{n}$ is constant. Then, the expected cost rate is simplified as

$$
C_{1}(N, T)=\lambda c_{M}+\frac{(N-1) c_{T}+c_{N}-c_{M}\left\{G^{*}(\theta) /\left[1-G^{*}(\theta)\right]\right\} B_{N}(T)}{N T}
$$

where

$$
\begin{gathered}
B_{N}(T) \equiv\left\{1-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right\} \sum_{n=1}^{N} \mathrm{e}^{-\lambda \xi_{n} T} \quad(N=1,2, \cdots) \\
\xi_{1} \equiv 0, \quad \xi_{n} \equiv \sum_{j=1}^{n-1}\left[1-G^{*}\left(\theta a^{j}\right)\right] \quad(n=2,3, \cdots)
\end{gathered}
$$

When $a=0$, i.e., the PM is perfect, $\xi_{n}=0$ and the expected cost rate is

$$
\begin{aligned}
& C_{1}(N, T)=\lambda c_{M} \\
& +\frac{(N-1) c_{T}+c_{N}-N c_{M}\left\{G^{*}(\theta) /\left[1-G^{*}(\theta)\right]\right\}\left\{1-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right\}}{N T}
\end{aligned}
$$

The expected cost rate $C_{1}(N, T)$ in (7.13) is decreasing in $N$ because $c_{N}>c_{T}$, and hence, $N^{*}=\infty$. Thus, an optimum interval $T^{*}$ is easily derived by differentiating $C_{1}(\infty, T)$ and setting it equal to zero.

Before deriving optimum policies, we define a function that plays an important role in discussing them. Let

$$
Q_{n}(T) \equiv c(n)-c_{M} \frac{G^{*}(\theta)}{1-G^{*}(\theta)}\left\{1-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right\} \mathrm{e}^{-\lambda \xi_{n} T} \quad(n=1,2, \cdots)
$$

where $c(1)=c_{N}$ and $c(n)=c_{T}(n=2,3, \cdots, N)$. Then, (7.12) is rewritten as

$$
C_{1}(N, T)=\lambda c_{M}+\frac{1}{N T} \sum_{n=1}^{N} Q_{n}(T)
$$# (1) Optimum Number $N^{*}(T)$ 

We seek an optimum number $N^{*}(T)$ that minimizes $C_{1}(N, T)$ in (7.15) for a fixed $T>0$ and $0<a<1$. From the inequality $C_{1}(N+1, T) \geq C_{1}(N, T)$,

$$
L(N \mid T) \geq \frac{c_{N}-c_{T}}{c_{N}-Q_{1}(T)} \quad(N=1,2, \cdots)
$$

where

$$
\begin{aligned}
L(N \mid T) & \equiv \sum_{n=1}^{N}\left(\mathrm{e}^{-\lambda \xi_{n} T}-\mathrm{e}^{-\lambda \xi_{N+1} T}\right) \quad(N=1,2, \cdots) \\
Q_{1}(T) & =c_{N}-c_{M} \frac{G^{*}(\theta)}{1-G^{*}(\theta)}\left\{1-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right\}<c_{N}
\end{aligned}
$$

Clearly,

$$
L(N \mid T)-L(N-1 \mid T)=N\left(\mathrm{e}^{-\lambda \xi_{N} T}-\mathrm{e}^{-\lambda \xi_{N+1} T}\right)>0
$$

because $\xi_{n}$ is strictly increasing in $n$. Thus, $L(N \mid T)$ is also strictly increasing in $N$.

Therefore, if $L(\infty \mid T) \equiv \lim _{N \rightarrow \infty} L(N \mid T)>\left(c_{N}-c_{T}\right) /\left[c_{N}-Q_{1}(T)\right]$, then there exists a finite and unique minimum $N^{*}(T)$ that satisfies (7.16).

Example 7.1. Suppose that the amount of damage at each shock has an exponential distribution $G(x)=1-\mathrm{e}^{-\mu x}$ and $G^{*}(\theta)=\mu /(\theta+\mu)$. Then, $\xi_{1}=0$,

$$
\xi_{n}=\sum_{j=1}^{n-1} \frac{a^{j} \theta}{a^{j} \theta+\mu} \quad(n=2,3, \cdots)
$$

It is assumed that the total damage is reduced in proportion to the PM cost $c_{T}$, i.e., $c_{T} / c_{N}=1-a$. Table 7.1 presents the optimum number $N^{*}(T)$ and the resulting cost rate $C_{1}\left(N^{*}, T\right) /\left(\lambda c_{M}\right)$ for $a=0.1-0.9$ and $c_{N} / c_{M}=3$, 5,10 when $\lambda T=7$ and $G^{*}(\theta)=0.9$, i.e., $\mu / \theta=9$. This indicates that $N^{*}(T)$ is not monotonically increasing with respect to $a$ contrary to our expectation. However, this can be explained because $L(N \mid T)$ depends on $a$ through $c_{T} / c_{N}$. For example, suppose that $T=7$ days, i.e., the PM is planned only on the weekend and shocks occur, on average, once a day. In this case, if $a=0.5$ and $c_{N} / c_{M}=5$, i.e., both the costs of PM and minimal repair are half the replacement cost and the total damage is reduced to the half by PM, the unit should be replaced at three weeks. When $a$ is small, several $N^{*}(T)$ become infinite. These cases show that the total damage is removed greatly by PM and the unit should undergo only PM rather than replacement.Table 7.1. Optimum number $N^{*}(T)$ and expected cost rate $C_{1}\left(N^{*}, T\right) /\left(\lambda c_{M}\right)$ when $G^{*}(\theta)=0.9, \lambda T=7$, and $c_{T} / c_{N}=1-a$

| $a$ | $c_{N} / c_{M}=3$ |  | $c_{N} / c_{M}=5$ |  | $c_{N} / c_{M}=10$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $N^{*}(T)$ | $C_{1}\left(N^{*}, T\right) /\left(\lambda c_{M}\right)$ | $N^{*}(T)$ | $C_{1}\left(N^{*}, T\right) /\left(\lambda c_{M}\right)$ | $N^{*}(T)$ | $C_{1}\left(N^{*}, T\right) /\left(\lambda c_{M}\right)$ |
| 0.9 | 2 | 0.7408 | 3 | 0.8917 | 7 | 1.1203 |
| 0.8 | 2 | 0.7508 | 3 | 0.9192 | 6 | 1.2084 |
| 0.7 | 2 | 0.7597 | 3 | 0.9443 | 6 | 1.2869 |
| 0.6 | 2 | 0.7674 | 3 | 0.9671 | 9 | 1.3569 |
| 0.5 | 2 | 0.7739 | 3 | 0.9876 | $\infty^{*}$ | 1.4086 |
| 0.4 | 2 | 0.7790 | 3 | 1.0062 | $\infty$ | 1.4656 |
| 0.3 | 1 | 0.7813 | 3 | 1.0229 | $\infty$ | 1.5324 |
| 0.2 | 1 | 0.7813 | $\infty^{*}$ | 1.0367 | $\infty$ | 1.6081 |
| 0.1 | 1 | 0.7813 | $\infty$ | 1.0487 | $\infty$ | 1.6915 |

$\infty^{*}$ indicates that $N^{*}(T)$ may not be infinite, but is very large.

# (2) Optimum Number $T^{*}(N)$ 

We seek an optimum interval $T^{*}(N)$ that minimizes $C_{1}(N, T)$ in (7.15) for a fixed $N$. Differentiating $C_{1}(N, T)$ with respect to $T$ and setting it equal to zero,

$$
T \sum_{n=1}^{N} Q_{n}^{\prime}(T)=\sum_{n=1}^{N} Q_{n}(T)
$$

i.e.,

$$
\begin{aligned}
& \sum_{n=1}^{N}\left[1+\lambda T \xi_{n}-\left\{1+\lambda T\left[1-G^{*}(\theta)+\xi_{n}\right]\right\}-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right] \mathrm{e}^{-\lambda \xi_{n} T} \\
& \quad=\frac{(N-1) c_{T}+c_{N}}{c_{M}} \frac{1-G^{*}(\theta)}{G^{*}(\theta)}
\end{aligned}
$$

When $n=1, \xi_{1}=0$ and the term with $n=1$ in the left-hand side of (7.17) is a gamma distribution of order 2 , so that it increases from 0 to 1 . The other terms with $n(n=2,3, \cdots, N)$ are unimodal that is a unique solution of

$$
\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}=\left(\frac{\xi_{n}}{1-G^{*}(\theta)+\xi_{n}}\right)^{2}
$$

Thus, the left-hand side of (7.17) increases from 0 first, and then, oscillates and finally decreases to coverage to 1 , as $T$ increases. Therefore, there may be at most $(2 N-1)$ solutions that satisfy (7.17). An important $T^{*}(N)$ is either one of these solutions or $T^{*}(N)=\infty$. If there is no solution, then $T^{*}(N)=\infty$. In particular, when $N=1$, there exists a unique solution that satisfies (7.17) if $G^{*}(\theta) /\left[1-G^{*}(\theta)\right]>c_{N} / c_{M}$.Table 7.2. Optimum time $T^{*}(N)$ and expected cost rate $C_{1}\left(N, T^{*}\right) /\left(\lambda c_{M}\right)$ when $G^{*}(\theta)=0.9, c_{N} / c_{M}$, and $a=c_{T} / c_{N}=0.5$

| $N$ | $T^{*}(N)$ | $C_{1}\left(N, T^{*}\right) /\left(\lambda c_{M}\right)$ |
| :--: | :--: | :--: |
| 1 | 18.627 | 0.8603 |
| 2 | 13.358 | 0.9095 |
| 3 | 11.665 | 0.9429 |
| 4 | 10.816 | 0.9654 |
| 5 | 10.293 | 0.9811 |
| 6 | 9.933 | 0.9924 |
| 7 | $\infty$ | 1.0000 |

Example 7.2. We compute $T^{*}(N)$ for $N=1,2, \cdots, 7$ when $G^{*}(\theta)=0.9$, $c_{N} / c_{M}=5$, and $a=c_{T} / c_{N}=0.5$. Table 7.2 presents the values of $T^{*}(N)$ and $C_{1}(N, T) /\left(\lambda c_{M}\right)$ when $N$ varies. In this case, the optimum interval becomes infinity for $N \geq 7$.

# (3) Optimum Pair $\left(N^{*}, T^{*}\right)$ 

We seek both optimum $T^{*}$ and $N^{*}$ that minimize $C_{1}(N, T)$ in (7.15). From (7.12), we can see that $C_{1}(N, \infty)=\lambda c_{M}$ for all $N \geq 1$. Thus, optimum $\left(N^{*}, T^{*}\right)$ must satisfy $C_{1}\left(N^{*}, T^{*}\right) \leq \lambda c_{M}$. It follows from (7.12) that a necessary condition for $\left(N^{*}, T^{*}\right)$ is that $Q_{n}\left(T^{*}\right)<0$ for at least one $n \leq N^{*}$ because otherwise no contribution to the second term in (7.12) occurs.

Now, consider the inequality $Q_{n}(T) \leq 0$. This is equivalent to considering

$$
h_{n}(T) \geq \frac{c(n)}{c_{M}} \frac{G^{*}(\theta)}{1-G^{*}(\theta)}
$$

where

$$
h_{n}(T) \equiv\left\{1-\mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}\right\} \mathrm{e}^{-\lambda \xi_{n} T} \quad(n=1,2, \cdots, N)
$$

It is easy to see that $\mathrm{d} h_{n}(T) / \mathrm{d} T=0$ has a unique solution $m_{n}$ that satisfies

$$
\left[1-G^{*}(\theta)+\xi_{n}\right] \mathrm{e}^{-\lambda\left[1-G^{*}(\theta)\right] T}=\xi_{n}
$$

Thus, $h_{n}(T)$ is unimodal with $m_{m}$, and hence,

$$
\begin{aligned}
h_{n}(T) & \leq h_{n}\left(m_{n}\right) \\
& =\left[1-\frac{\xi_{n}}{1-G^{*}(\theta)+\xi_{n}}\right]\left[\frac{\xi_{n}}{1-G^{*}(\theta)+\xi_{n}}\right]^{\xi_{n} /\left[1-G^{*}(\theta)\right]}<1
\end{aligned}
$$

It is proved that both $m_{n}$ and $h_{n}\left(m_{n}\right)$ are decreasing in $n$, so that both $m_{\infty}$ and $h_{\infty}\left(m_{\infty}\right)$ exist. Thus, it follows that$$
N^{*}<n^{*}=\min _{n \geq 2}\left\{h_{n}\left(m_{n}\right) \leq \frac{c_{T}}{c_{M}} \frac{1-G^{*}(\theta)}{G^{*}(\theta)}\right\}
$$

Here, if $h_{\infty}\left(m_{\infty}\right)>\left(c_{T} / c_{M}\right)\left[1-G^{*}(\theta)\right] / G^{*}(\theta)$, then we set $N^{*}=\infty$. It can be seen that $T^{*} \geq m_{n^{*}-1}$ because $m_{n}$ is decreasing in $n$. On the other hand, $T^{*} \leq \max \left\{T^{*}(1), m_{2}\right\}$. To this end, suppose that $T$ satisfies (7.17), and recall that $Q_{n}^{\prime}(T)<0$ for $T<m_{n}, Q_{n}^{\prime} \geq 0$ for $T \geq m_{n}$, and $m_{n}$ is decreasing in $n$. Then, if $T^{*}(1)>m_{2}$, either $T^{*}=T^{*}(1)$ with $N^{*}=1$ or $T^{*}<T^{*}(1)$. If $T^{*}(1)<m_{2}, T^{*}>m_{2}$ never happens because $\sum_{n=1}^{N} Q_{n}^{\prime}\left(T^{*}\right) / N>Q_{1}^{\prime}\left(T^{*}(1)\right)$. Thus, $T^{*} \leq \max \left\{T^{*}(1), m_{2}\right\}$, as desired.

From the above analysis, we have the following optimum policy: Suppose that $n^{*}<\infty$ that is given in (7.20). Then, the optimum pair $\left(N^{*}, T^{*}\right)$ is confined, as $N^{*}<n^{*}$ and $m_{n^{*}-1} \leq T^{*} \leq \max \left\{T^{*}(1), m_{2}\right\}$, where $m_{n}$ is a unique solution of (7.20). Therefore, the optimum pair is given by

$$
T^{*}\left(N^{*}\right)=\min _{1 \leq N \leq n^{*}} T^{*}(N)=\min _{m_{n^{*}-1} \leq T \leq \max \left\{T^{*}(1), m_{2}\right\}} N^{*}(T)
$$

Example 7.3. Consider the model in Example 7.2 and compute an optimum pair $\left(N^{*}, T^{*}\right)$ that minimizes $C_{1}(N, T)$. In this example, $h_{4}\left(m_{4}\right) \approx 0.2621<$ 0.27 , and hence, $N^{*} \leq 3$. In fact, Table 7.2 indicates that $N^{*}=1$ and $T^{*}=$ 18.627.

# 7.3 Optimum Policies for a Finite Interval 

Suppose that a unit has to be operating over a finite interval $(0, S]$ and be replaced at time $S$ (Section 9.2 of [1]). When $a_{n} \equiv a$ and $G(x)=1-\mathrm{e}^{-\mu x}$, $C_{1}\left(T_{1}, T_{2}, \ldots, T_{N}\right)$ is, from $(7.11)$,

$$
\begin{aligned}
C_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right)= & c_{M}-\frac{C_{1}\left(T_{1}, T_{2}, \ldots, T_{N}\right)}{\lambda} \\
& c_{M}(\mu / \theta) \sum_{n=1}^{N} \exp \left[-\sum_{j=1}^{n-1} \lambda A_{n-j}(\theta) T_{j}\right] \\
= & \frac{\times\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{n}}\right]-(N-1) c_{T}-c_{N}}{\lambda \sum_{n=1}^{N} T_{n}} \\
& (N=1,2, \ldots)
\end{aligned}
$$

where $T_{1}+T_{2}+\cdots+T_{N}=S$ and

$$
A_{j}(\theta) \equiv \frac{\theta a^{j}}{\theta a^{j}+\mu} \quad(j=0,1,2, \ldots)
$$

It is noted that $A_{j}(\theta)>A_{j+1}(\theta)(j=0,1,2, \ldots)$ for $0<a<1$. In this case, we consider the optimum policy that maximizes the expected cost$$
\begin{aligned}
\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right)= & \frac{\mu c_{M}}{\theta} \sum_{n=1}^{N} \exp \left[-\sum_{j=1}^{n-1} \lambda A_{n-j}(\theta) T_{j}\right]\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{n}}\right] \\
& -(N-1) c_{T}-c_{N} \quad(N=1,2, \ldots)
\end{aligned}
$$

For example, when $N=1$, i.e., no PM is done,

$$
\widetilde{C}_{2}=\frac{\mu c_{M}}{\theta}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) S}\right]-c_{N}
$$

that is constant.
When $N=2$,

$$
\begin{aligned}
\widetilde{C}_{2}\left(T_{1}\right)= & \frac{\mu c_{M}}{\theta}\left\{1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{1}}+\mathrm{e}^{-\lambda A_{1}(\theta) T_{1}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}\right)}\right]\right\} \\
& -c_{T}-c_{N}
\end{aligned}
$$

Differentiating $\widetilde{C}_{2}\left(T_{1}\right)$ with respect to $T_{1}$ and setting it equal to zero,

$$
A_{0}(\theta)\left\{\mathrm{e}^{-\lambda\left[A_{0}(\theta)-A_{1}(\theta)\right] T_{1}}-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}\right)}\right\}-A_{1}(\theta)\left[1-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}\right)}\right]=0
$$

Letting $Q\left(T_{1}\right)$ be the left-hand side of (7.27),

$$
\begin{aligned}
Q(0) & =\left[A_{0}(\theta)-A_{1}(\theta)\right]\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) S}\right]>0 \\
Q(S) & =-A_{0}(\theta)\left\{1-\mathrm{e}^{-\lambda\left[A_{0}(\theta)-A_{1}(\theta)\right] S}\right\}<0 \\
Q^{\prime}\left(T_{1}\right) & =-A_{0}(\theta)\left[A_{0}(\theta)-A_{1}(\theta)\right]\left\{\mathrm{e}^{-\lambda\left[A_{0}(\theta)-A_{1}(\theta)\right] T_{1}}+\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}\right)}\right\}<0
\end{aligned}
$$

Thus, there exists an optimum time $T_{1}^{*}\left(0<T_{1}^{*}<S\right)$ that satisfies (7.27).
When $N=3$,

$$
\begin{aligned}
\widetilde{C}_{2}\left(T_{1}, T_{2}\right)= & \frac{\mu c_{M}}{\theta}\left\{1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{1}}+\mathrm{e}^{-\lambda A_{1}(\theta) T_{1}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{2}}\right]\right. \\
& \left.+\mathrm{e}^{-\lambda A_{2}(\theta) T_{1}-\lambda A_{1}(\theta) T_{2}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}-T_{2}\right)}\right]\right\} \\
& -2 c_{T}-c_{N}
\end{aligned}
$$

Differentiating $\widetilde{C}_{2}\left(T_{1}, T_{2}\right)$ with respect to $T_{1}$ and $T_{2}$ and setting them equal to zero, respectively,

$$
\begin{aligned}
& A_{0}(\theta)\left[\mathrm{e}^{-\lambda A_{0}(\theta) T_{1}}-\mathrm{e}^{-\lambda A_{2}(\theta) T_{1}-\lambda A_{1}(\theta) T_{2}-\lambda A_{0}(\theta)\left(S-T_{1}-T_{2}\right)}\right] \\
& -A_{1}(\theta) \mathrm{e}^{-\lambda A_{1}(\theta) T_{1}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta) T_{2}}\right] \\
& -A_{2}(\theta) \mathrm{e}^{-\lambda A_{2}(\theta) T_{1}-\lambda A_{1}(\theta) T_{2}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}-T_{2}\right)}\right]=0
\end{aligned}
$$Table 7.3. PM times $\lambda T_{n}$ and expected cost $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right) / c_{M}$ for $N=$ $1,2, \ldots, 10$ when $a=0.5, \mu / \theta=10, c_{N} / c_{M}=5, c_{T} / c_{M}=1.0$, and $\lambda S=40$

|  | $N=1$ | $N=2$ | $N=3$ | $N=4$ | $N=5$ | $N=6$ | $N=7$ | $N=8$ | $N=9$ | $N=10$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\lambda T_{1}$ | 40.00 | 13.17 | 12.41 | 11.37 | 10.32 | 9.36 | 8.52 | 7.80 | 7.17 | 6.63 |
| $\lambda T_{2}$ |  | 26.83 | 5.60 | 5.27 | 4.82 | 4.38 | 3.99 | 3.66 | 3.37 | 3.11 |
| $\lambda T_{3}$ |  |  | 21.99 | 5.23 | 4.87 | 4.45 | 4.06 | 3.72 | 3.42 | 3.17 |
| $\lambda T_{4}$ |  |  |  | 18.14 | 4.78 | 4.45 | 4.07 | 3.73 | 3.44 | 3.18 |
| $\lambda T_{5}$ |  |  |  |  | 15.22 | 4.35 | 4.06 | 3.73 | 3.44 | 3.18 |
| $\lambda T_{6}$ |  |  |  |  |  | 13.01 | 3.97 | 3.71 | 3.44 | 3.18 |
| $\lambda T_{7}$ |  |  |  |  |  |  | 11.33 | 3.64 | 3.42 | 3.18 |
| $\lambda T_{8}$ |  |  |  |  |  |  |  | 10.01 | 3.35 | 3.16 |
| $\lambda T_{9}$ |  |  |  |  |  |  |  |  | 8.96 | 3.10 |
| $\lambda T_{10}$ |  |  |  |  |  |  |  |  |  | 8.10 |
| $\frac{\widetilde{C}_{2}(\cdot)}{c_{M}}$ | 4.74 | 5.86 | 6.87 | 7.70 | 8.34 | 8.78 | 9.05 | 9.17 | 9.16 | 9.03 |

$$
\begin{aligned}
& A_{0}(\theta)\left[\mathrm{e}^{-\lambda A_{1}(\theta) T_{1}-\lambda A_{0}(\theta) T_{2}}-\mathrm{e}^{-\lambda A_{2}(\theta) T_{1}-\lambda A_{1}(\theta) T_{2}-\lambda A_{0}(\theta)\left(S-T_{1}-T_{2}\right)}\right] \\
& -A_{1}(\theta) \mathrm{e}^{-\lambda A_{2}(\theta) T_{1}-\lambda A_{1}(\theta) T_{2}}\left[1-\mathrm{e}^{-\lambda A_{0}(\theta)\left(S-T_{1}-T_{2}\right)}\right]=0
\end{aligned}
$$

In general, differentiating $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right)$ with respect to $T_{n}(n=$ $1,2, \ldots, N-1)(N \geq 2)$ and setting them equal to zero,

$$
\begin{aligned}
& A_{0}(\theta)\left\{\exp \left[-\sum_{j=1}^{n} \lambda A_{n-j}(\theta) T_{j}\right]-\exp \left[-\sum_{j=1}^{N} \lambda A_{N-j}(\theta) T_{j}\right]\right\} \\
&-\sum_{i=n+1}^{N} A_{i-n}(\theta)\left\{\exp \left[-\sum_{j=1}^{i-1} \lambda A_{i-j}(\theta) T_{j}\right]-\exp \left[-\sum_{j=1}^{i} \lambda A_{i-j}(\theta) T_{j}\right]\right\}=0 \\
&(n=1,2, \ldots, N-1)
\end{aligned}
$$

where note that $T_{N}=S-T_{1}-T_{2}-\cdots-T_{N-1}$.
Therefore, we may solve the simultaneous equations (7.31) and obtain the expected cost $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right)$ in (7.24). Next, compared $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots\right.$, $T_{N-1}$ ) for all $N \geq 1$, we can get the optimum number $N^{*}$ and times $T_{n}^{*}$ $\left(n=1,2, \ldots, N^{*}-1\right)$ for a specified $S$.

Example 7.4. Table 7.3 presents $\lambda T_{n}(n=1,2, \ldots, N)$ and $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots\right.$, $\left.T_{N-1}\right) / c_{M}$ when $a=0.5, \mu / \theta=10, c_{N} / c_{M}=5, c_{T} / c_{M}=1.0$, and $\lambda S=$ $\lambda \sum_{n=1}^{N} T_{n}=40$ for $N=1,2, \ldots, 10$. Compared $\widetilde{C}_{2}\left(T_{1}, T_{2}, \ldots, T_{N-1}\right)$ for $N=1,2, \ldots, 10$, the expected cost $\widetilde{C}_{2}(\cdot)$ is maximum, i.e., $C_{2}(\cdot)$ in (7.23) is minimum at $N^{*}=8$. In this case, the optimum PM number is $N^{*}=8$ and optimum PM times are $7.80,11.46,15.18,18.91,22.64,26.35,29.99,40$. Thisindicates the interesting result that the last PM time interval is the largest and the first one is the second, and they are first increasing, remain in constant for some number, and then decreasing for large $N$, that is, PM time intervals draw a upside-down bathtub curve [221] for $2 \leq n \leq N-1$. PM interval times $T_{n}(n=1,2, \ldots, 10)$, draws roughly a standard bathtub curve. It would be necessary to inquire into why the PM time intervals describe the two bathtub curves.# Garbage Collection Policies 

A database for a computer system is in optimum storage according to the scheme defined in the data structures. However, after some operations, storage areas are not in good order due to additions and deletions of data. Such updating procedures reduce the size of continuous and available memory areas, and make processing efficiency worse. To use storage areas effectively and to improve processing efficiently, garbage collections (GCs) have to be done at suitable times. Many GCs to reclaim the storage and rearrange a database are used in most large list processing systems [222, 223]. Some algorithms for performing the GC of linked data structures were reviewed [224]. Several authors have studied real time GCs to avoid suspension of the application program in its execution [225-227]. Most problems have been concerned with ways to introduce GC methods.

When a database is updated from several online terminals, it is necessary to set up a desired response time. If response times become comparatively long, the processing efficiency becomes worse, and finally, it would be impossible to update data. Such response times may depend on the amount of garbage in a database.

This chapter proposes when to make the GC for a database with an upper limit level $K$ of the total garbage. An amount of garbage with a general distribution $G(x)$ arises from each update and is additive. A cost and time for the GC are higher if the total garbage is greater than $K$. In Section 8.1, to prevent such the event, the GC is done at periodic time $T$ or at the $N$ th update, whichever occurs first [58]. It is assumed in Section 8.2 that if there exist data that are not erased, they remain in the storage area as garbage. In Section 8.3, a database is checked at periodic times to investigate the amount of garbage. If the total garbage exceeds a managerial level $Z$, the GC is done. Using the results of Section 6.1, the optimum policy is derived. Each GC restores computer resources such as response time, storage area, and throughput to an initial state. This corresponds to one modification of maintenance policies for cumulative damage models, replacing update with shock and garbage with damage. Using the results of Chapters 3, 5, and 6, theexpected cost rates or the availabilities are derived, and optimum policies that minimize them are discussed analytically. Numerical examples are given when a database is updated in a Poisson process and an amount of garbage due to updates is exponential. It is theoretically noted that the policy maximizing the availability corresponds essentially to the policy minimizing the expected cost rate.

# 8.1 Standard Garbage Collection Model 

Suppose that a database is updated in a nonhomogeneous Poisson process with an intensity function $h(t)$ and a mean value function $H(t)$, i.e., $H(t) \equiv \int_{0}^{t} h(u) \mathrm{d} u$. Then, the probability of $j$ updates in $[0, t]$ is $p_{j}(t) \equiv$ $\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}(j=0,1,2, \cdots)$. Furthermore, an amount $W_{j}$ of garbage arises from the $j$ th update and has a probability distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$, independent of the number of updates, and these amount of garbage are additive. Then, the total garbage $\sum_{i=1}^{j} W_{i}$ up to the $j$ th update has $\operatorname{Pr}\left\{\sum_{i=1}^{j} W_{i} \leq\right.$ $x\}=G^{(j)}(x)(j=1,2, \cdots)$, where $G^{(j)}(x)$ is the $j$-fold Stieltjes convolution of $G(x)$ with itself and $G^{(0)}(x) \equiv 1$ for $x \geq 0$. When the total garbage has exceeded an upper limit level $K$, the database becomes useless for lack of storage area or due to a long response time.

To prevent the database becoming useless, the GC is done at a planned time $T$ or at an update number $N$, whichever occurs first. For the above model, we introduce the following costs: $c_{T}$ and $c_{N}$ are the fixed costs for the respective GCs at time $T$ and update $N$, and $c_{K}$ is the fixed cost for the GC when the total garbage has exceeded a level $K$ with $c_{K}>c_{T}$ and $c_{K}>c_{N}$. In addition, $c_{0}(x)$ is a variable cost for the collection of an amount $x(0 \leq x \leq K)$ of garbage.

Using a method similar to (1) of Section 3.3, the expected cost when the GC is done at time $T$ or at update $N$ is

$$
\begin{aligned}
& \sum_{j=0}^{N-1} p_{j}(T) \int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& +\int_{0}^{T} p_{N-1}(t) h(t) \mathrm{d} t \int_{0}^{K}\left[c_{N}+c_{0}(x)\right] \mathrm{d} G^{(N)}(x)
\end{aligned}
$$

and the expected cost when the total garbage has exceeded a level $K$ is

$$
\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{N-1}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t
$$

The mean time to GC is$$
\begin{aligned}
& T \sum_{j=0}^{N-1} p_{j}(T) G^{(j)}(K)+G^{(N)}(K) \int_{0}^{T} t p_{N-1}(t) h(t) \mathrm{d} t \\
& +\sum_{j=0}^{N-1}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{T} t p_{j}(t) h(t) \mathrm{d} t=\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t
\end{aligned}
$$

Therefore, the expected cost rate is, summing up (8.1) and (8.2), and dividing by $(8.3)$,

$$
\begin{gathered}
\sum_{j=0}^{N-1} p_{j}(T) \int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
+\int_{0}^{T} p_{N-1}(t) h(t) \mathrm{d} t \int_{0}^{K}\left[c_{N}+c_{0}(x)\right] \mathrm{d} G^{(N)}(x) \\
C(T, N)=\frac{+\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{N-1}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t}{\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t}
\end{gathered}
$$

and

$$
\begin{aligned}
C(\infty) & \equiv \lim _{\substack{T \rightarrow \infty \\
N \rightarrow \infty}} C(T, N) \\
& =\frac{c_{K}+c_{0}(K)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t}
\end{aligned}
$$

# (1) Optimum $T^{*}$ 

Suppose that the GC is done only at time $T$. Then, from (8.4), the expected cost rate is given by

$$
\begin{aligned}
C_{1}(T) \equiv & \lim _{N \rightarrow \infty} C(T, N) \\
& \sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
= & \frac{+\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t}
\end{aligned}
$$

We seek an optimum time $T^{*}$ that minimizes $C_{1}(T)$ in (8.6) when $c_{0}(x)=$ $c_{0} x$. Differentiating $C_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
& \left(c_{K}-c_{T}\right)\left\{h(T) Q_{1}(T) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t-\sum_{j=0}^{\infty} p_{j}(T)\left[1-G^{(j)}(K)\right]\right\} \\
& +c_{0}\left\{h(T) Q_{2}(T) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t-\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[1-G^{(j)}(x)\right] \mathrm{d} x\right\} \\
& =c_{T}
\end{aligned}
$$where

$$
\begin{aligned}
& Q_{1}(T)=\frac{\sum_{j=0}^{\infty} p_{j}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]}{\sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)} \\
& Q_{2}(T)=\frac{\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} x}{\sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)}
\end{aligned}
$$

In the particular case of $c_{0}=0,(8.7)$ becomes

$$
h(T) Q_{1}(T) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t-\sum_{j=0}^{\infty} p_{j}(T)\left[1-G^{(j)}(K)\right]=\frac{c_{T}}{c_{K}-c_{T}}
$$

If $h(T) Q_{1}(T)$ is strictly increasing, then the left-hand side of (8.8) is also strictly increasing in $T$ from 0 to $h(\infty) Q_{1}(\infty) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t-1$, where $h(\infty) \equiv \lim _{t \rightarrow \infty} h(t)$ and $Q_{1}(\infty) \equiv \lim _{t \rightarrow \infty} Q_{1}(t)$. Thus, if

$$
h(\infty) Q_{1}(\infty) \sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t>\frac{c_{K}}{c_{K}-c_{T}}
$$

then there exists a finite and unique $T^{*}$ that satisfies (8.8).
In addition, when $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}$ and $G^{(j)}(x)=\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}$ $(j=0,1,2, \cdots),(8.7)$ is simplified as

$$
Q_{1}(T) \sum_{j=0}^{\infty} G^{(j)}(K) \sum_{i=j+1}^{\infty} p_{i}(T)-\sum_{j=0}^{\infty}\left[1-G^{(j)}(K)\right] p_{j}(T)=\frac{c_{T}}{c_{K}-c_{T}-c_{0} / \mu}
$$

that agrees with (3.34). Thus, if $c_{K}>c_{T}[1+(1 / \mu K)]+c_{0} / \mu$, then there exists a finite and unique $T^{*}$ that satisfies (8.9), and the resulting cost rate is given in (3.36). Conversely, if $c_{K} \leq c_{T}[1+(1 / \mu K)]+c_{0} / \mu$, then $T^{*}=\infty$, and the resulting cost rate is given in (8.5).

# (2) Optimum $N^{*}$ 

The expected cost rate when the GC is done only at update $N$ is, from (8.4),

$$
\begin{aligned}
C_{2}(N) & \equiv \lim _{T \rightarrow \infty} C(T, N) \\
& =\frac{\left[c_{K}+c_{0}(K)\right]\left[1-G^{(N)}(K)\right]+\int_{0}^{K}\left[c_{N}+c_{0}(x)\right] \mathrm{d} G^{(N)}(x)}{\sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t} \\
& (N=1,2, \ldots)
\end{aligned}
$$

Forming the inequality $C_{2}(N+1)-C_{2}(N) \geq 0$ to seek an optimum number $N^{*}$ that minimizes $C_{2}(N)$ in (8.10) when $c_{0}(x)=c_{0} x$,$$
\begin{aligned}
& \left(c_{K}-c_{N}\right)\left\{\frac{G^{(N)}(K)-G^{(N+1)}(K)}{G^{(N)}(K) \int_{0}^{\infty} p_{N}(t) \mathrm{d} t} \sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t-\left[1-G^{(N)}(K)\right]\right\} \\
& +c_{0}\left\{\frac{\int_{0}^{K}\left[G^{(N)}(x)-G^{(N+1)}(x)\right] \mathrm{d} x}{G^{(N)}(K) \int_{0}^{\infty} p_{N}(t) \mathrm{d} t} \sum_{j=0}^{N-1} G^{(j)}(K) \int_{0}^{\infty} p_{j}(t) \mathrm{d} t\right. \\
& \left.-\int_{0}^{K}\left[1-G^{(N)}(x)\right] \mathrm{d} x\right\} \geq c_{N} \quad(N=1,2, \ldots)
\end{aligned}
$$

When $c_{0}=0$ and $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}$, (8.11) is

$$
Q_{3}(N) \sum_{j=0}^{N-1} G^{(j)}(K)-\left[1-G^{(N)}(K)\right] \geq \frac{c_{N}}{c_{K}-c_{N}} \quad(N=1,2, \cdots)
$$

that agrees with (3.22) where $Q_{3}(N) \equiv\left[G^{(N)}(K)-G^{(N+1)}(K)\right] / G^{(N)}(K)$ and represents the discrete failure rate defined in (2.15). Thus, if $Q_{3}(N)$ is strictly increasing and $Q_{3}(\infty)\left[1+M_{G}(K)\right]>c_{K} /\left(c_{K}-c_{N}\right)$, where $M_{G}(K) \equiv$ $\sum_{j=1}^{\infty} G^{(j)}(K)$, then there exists a finite and unique minimum $N^{*}\left(1 \leq N^{*}<\right.$ $\infty)$ that satisfies (8.12). In addition, when $G^{(j)}(x)=\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}$, $Q_{3}(N)$ is strictly increasing from $\mathrm{e}^{-\mu K}$ to 1 from Example 2.2 of Chapter 2. Thus, if $\mu K>c_{N} /\left(c_{K}-c_{N}\right)$, then there exists a finite and unique minimum $N^{*}$ that satisfies (8.12).
Example 8.1. We compute optimum $T^{*}$ and $N^{*}$ when $c_{0}(x)=c_{0} x, h(t)=\lambda$ and $G(x)=1-\mathrm{e}^{-\mu x}$. Under such assumptions, (8.9) and (8.11) are rewritten as, respectively,

$$
\begin{aligned}
& \frac{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\left[(\mu K)^{j} / j!\right]\right.}{\sum_{j=0}^{\infty}\left[(\lambda T)^{j} / j!\left[\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right]\right.\right.} \\
& \left.\left.\times \sum_{j=0}^{\infty}\left\{\sum_{i=j+1}^{\infty}\left[(\lambda T)^{i} / i!\right] \mathrm{e}^{-\lambda T}\right\}\left\{\sum_{i=j}^{\infty}\left[(\mu K)^{i} / i!\right] \mathrm{e}^{-\mu K}\right\}\right. \\
& -\sum_{j=1}^{\infty} \frac{(\lambda T)^{j}}{j!} \mathrm{e}^{-\lambda T} \sum_{i=0}^{j-1} \frac{(\mu K)^{i}}{i!} \mathrm{e}^{-\mu K}=\frac{c_{T}}{c_{K}-c_{T}-c_{0} / \mu}
\end{aligned}
$$

and

$$
\frac{\left[(\mu K)^{N} / N!\right]}{\sum_{j=N}^{\infty}\left[(\mu K)^{j} / j!\right]} \sum_{j=0}^{N-1} \sum_{i=j}^{\infty} \frac{(\mu K)^{i}}{i!} \mathrm{e}^{-\mu K}-\sum_{j=0}^{N-1} \frac{(\mu K)^{j}}{j!} \mathrm{e}^{-\mu K} \geq \frac{c_{N}}{c_{K}-c_{N}-c_{0} / \mu}
$$

If $c_{K}>c_{k}[1+(1 / \mu K)]+c_{0} / \mu(k=T, N)$, then there exist both finite $T^{*}$ and $N^{*}$ that satisfies (8.13) and (8.14), respectively.Table 8.1. Optimum time $\lambda T^{*}$ and expected cost rate $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right)$ when $c_{0} K / c_{T}=1$

| $c_{K} / c_{T}$ | $\mu K=150$ |  | $\mu K=300$ |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right) \times 10^{2}$ | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right) \times 10^{3}$ |
| 100 | 98.1 | 1.715 | 221.5 | 7.904 |
| 200 | 95.3 | 1.734 | 217.5 | 8.026 |
| 500 | 92.0 | 1.790 | 212.5 | 8.115 |
| 1000 | 89.6 | 1.808 | 209.0 | 8.223 |
| $c_{K} / c_{T}$ | $\mu K=500$ |  | $\mu K=700$ |  |
|  | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right) \times 10^{3}$ | $\lambda T^{*}$ | $C_{1}\left(T^{*}\right) /\left(\lambda c_{T}\right) \times 10^{3}$ |
| 100 | 394.5 | 4.576 | 572.1 | 3.191 |
| 200 | 389.2 | 4.614 | 565.8 | 3.213 |
| 500 | 382.6 | 4.643 | 558.0 | 3.244 |
| 1000 | 377.9 | 4.663 | 552.4 | 3.259 |

Table 8.2. Optimum number $N^{*}$ and expected cost rate $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right)$ when $c_{0} K / c_{N}=1$

| $c_{K} / c_{N}$ | $\mu K=150$ |  | $\mu K=300$ |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right) \times 10^{2}$ | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right) \times 10^{3}$ |
| 100 | 110 | 1.600 | 241 | 7.562 |
| 200 | 108 | 1.617 | 238 | 7.613 |
| 500 | 105 | 1.640 | 234 | 7.678 |
| 1000 | 103 | 1.657 | 231 | 7.725 |
| $c_{K} / c_{N}$ | $\mu K=500$ |  | $\mu K=700$ |  |
|  | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right) \times 10^{3}$ | $N^{*}$ | $C_{2}\left(N^{*}\right) /\left(\lambda c_{N}\right) \times 10^{3}$ |
| 100 | 421 | 4.406 | 605 | 3.100 |
| 200 | 417 | 4.428 | 600 | 3.112 |
| 500 | 412 | 4.455 | 594 | 3.127 |
| 1000 | 409 | 4.475 | 590 | 3.139 |

Table 8.1 presents the optimum $T^{*}$ for $\mu K=150,300,500,700$ and $c_{K} / c_{T}=100,200,500,1000$ when $c_{0} K / c_{T}=1$, i.e., $c_{0} / \mu=c_{T} /(\mu K)$. In this case, if $c_{K} / c_{T}>1+(2 / \mu K)$, then a finite $T^{*}$ exists. For example, when $\lambda=5$, $c_{K} / c_{T}=100$, and $\mu K=700$, the optimum time is $\lambda T^{*}=572.1$. This indicates that when the database is updated 5 times an hour and becomes useless after 700 updates, on average, the GC should be done at $572.1 / 5=114.42$ hour, i.e., at about $114.42 / 24 \approx 4.8$ days. Taking another viewpoint, when the total garbage has exceeded $(572.1 / 700) \times 100 \approx 81.7 \%$ of an upper limit $\mu K$, the GC should be done.Similarly, Table 8.2 presents the optimum number $N^{*}$ for $\mu K=150,300$, 500,700 and $c_{K} / c_{N}=100,200,500,1000$ when $c_{0} K / c_{N}=1$. For example, when $c_{K} / c_{N}=100$ and $\mu K=700$, the optimum number is $N^{*}=605$, that is, the GC is done at $(600 / 700) \times 100 \approx 86.4 \%$ of an upper limit $\mu K$, whose values are greater than those, and the resulting cost rates are smaller than those in Table 8.1 when $c_{T}=c_{N}$. In this case, the GC policy at update $N$ is more economical than that at time $T$, however, they have almost the same values. Furthermore, it is of interest that both $T^{*}$ and $N^{*}$ depend a little on costs $c_{K} / c_{T}$ and $c_{K} / c_{N}$, and are determined approximately by $\mu K$.

# 8.2 Periodic Garbage Collection Model 

A database is updated and garbage due to update accumulates in the storage area that is the same model as that of Section 8.1. However, the information for the number of updates and the total garbage is collected only at periodic planned times. In this section, the GC is done at periodic times to recover computer resources such as operating time, storage area, and throughput.

It is assumed that a database is updated in a nonhomogeneous Poisson process with an intensity function $h(t)$ that is increasing in $t$ and a mean value function $H(t)$. Introducing the mean times of GC that depend on the number of updates and amount of garbage, the availabilities are obtained, and optimum times $T^{*}$ that minimize them are discussed analytically.

## (1) Model 1 with Number of Updates

Suppose that an amount of garbage arises from the $j$ th $(j=1,2, \cdots)$ update with constant probability $\alpha(0<\alpha \leq 1)$ and the mean time required for the collection of this garbage is $c_{0}(j)$ that depends only on the number of updates, where $c_{0}(0) \equiv 0$. The mean time for GC at time $T$ is $c_{T}$ when the total number of updates is less than a prespecified $N$ and is $c_{N}$ when it is equal to $N$ or has exceeded $N$ until time $T$. It is assumed that $c_{0}(j)$ is increasing in $j$ and $c_{T} \leq c_{N}$. Under these conditions, the mean time for GC at time $T$ is

$$
\begin{aligned}
& \sum_{j=0}^{N-1} p_{j}(T)\left[c_{T}+\sum_{i=0}^{j} \alpha c_{0}(i)\right]+\sum_{j=N}^{\infty} p_{j}(T)\left[c_{N}+\sum_{i=0}^{j} \alpha c_{0}(i)\right] \\
& =c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)+\sum_{j=0}^{\infty} p_{j}(T) \sum_{i=0}^{j} \alpha c_{0}(i)
\end{aligned}
$$

where $p_{j}(t) \equiv\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}(j=0,1,2, \cdots)$.
Suppose that a database can be updated at every time $T$, although processing efficiency may be worse when the total number of updates has exceeded $N$. Then, the availability is, from (3.10),$$
A_{1}(T)=\frac{T}{T+c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)+\sum_{j=0}^{\infty} p_{j}(T) \sum_{i=0}^{j} \alpha c_{0}(i)}
$$

We seek an optimum GC time $T_{1}^{*}$ that maximizes $A_{1}(T)$ in (8.16). Differentiating $A_{1}(T)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
& \left(c_{N}-c_{T}\right)\left[T h(T) p_{N-1}(T)+\sum_{j=0}^{N-1} p_{j}(T)\right] \\
& \quad+T h(T) \sum_{j=0}^{\infty} p_{j}(T) \alpha c_{0}(j+1)-\sum_{j=0}^{\infty} p_{j}(T) \sum_{i=0}^{j} \alpha c_{0}(i)=c_{N}
\end{aligned}
$$

First, consider the particular case of $c_{N}=c_{T}$. Then, (8.17) is

$$
\operatorname{Th}(T) \sum_{j=0}^{\infty} p_{j}(T) \alpha c_{0}(j+1)-\sum_{j=0}^{\infty} p_{j}(T) \sum_{i=0}^{j} \alpha c_{0}(i)=c_{N}
$$

It is assumed that either $h(t)$ or $c_{0}(j)$ is strictly increasing. Letting $Q(T)$ be the left-hand side of $(8.18), Q(0)=0$ and

$$
\begin{aligned}
\frac{\mathrm{d} Q(T)}{\mathrm{d} T}=T\{ & \frac{\mathrm{~d} h(T)}{\mathrm{d} T} \sum_{j=0}^{\infty} p_{j}(T) \alpha c_{0}(j+1) \\
& \left.+[h(T)]^{2} \sum_{j=0}^{\infty} p_{j}(T) \alpha\left[c_{0}(j+2)-c_{0}(j+1)\right]\right\}>0
\end{aligned}
$$

Thus, if $Q(\infty) \equiv \lim _{T \rightarrow \infty} Q(T)>c_{N}$, then there exists a finite and unique $T_{0}^{*}$ that satisfies (8.18). If $h(t)$ is strictly increasing, we easily find that, for any $T>T_{0}$,

$$
Q(T)>h(T) T_{0} \sum_{j=0}^{\infty} p_{j}\left(T_{0}\right) \alpha c_{0}(j+1)-\sum_{j=0}^{\infty} p_{j}\left(T_{0}\right) \sum_{i=0}^{j} \alpha c_{0}(i)
$$

Hence, if $h(t)$ is strictly increasing to infinity, then a finite $T_{0}^{*}$ exists uniquely.
When $c_{0}(j)$ is constant, i.e., $c_{0}(j) \equiv c_{0},(8.18)$ is

$$
\operatorname{Th}(T)-H(T)=\frac{c_{N}}{\alpha c_{0}}
$$

that agrees with (4.18) of [1] in the periodic replacement with minimal repair at failure. Thus, if a solution $T_{1}^{*}$ to (8.19) exists, then it is unique.

Furthermore, when a database is updated in a Poisson process, i.e., $h(t)=$ $\lambda$ and $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}$, the left-hand side of (8.18) is$$
\begin{aligned}
& \lambda T \sum_{j=0}^{\infty} \alpha c_{0}(j+1) p_{j}(T)-\sum_{j=0}^{\infty} \alpha c_{0}(j+1) \int_{0}^{T} \lambda p_{j}(t) \mathrm{d} t \\
& =\lambda \sum_{j=0}^{\infty} \alpha\left[c_{0}(j+2)-c_{0}(j+1)\right] \int_{0}^{T}(\lambda t) p_{j}(t) \mathrm{d} t
\end{aligned}
$$

Thus, if $c_{0}(j)$ is strictly increasing in $j$, then (8.20) is also strictly increasing in $T$ from 0 to $\alpha \sum_{j=1}^{\infty}\left[c_{0}(\infty)-c_{0}(j)\right]$, where $c_{0}(\infty) \equiv \lim _{j \rightarrow \infty} c_{0}(j)$. Hence, if $\alpha \sum_{j=1}^{\infty}\left[c_{0}(\infty)-c_{0}(j)\right]>c_{N}$, a finite $T_{0}^{*}$ exists uniquely.

Therefore, because the left-hand side of (8.17) is greater than $Q(T)$ for $c_{N}>c_{T}$, if either $h(t)$ or $c_{0}(j)$ is strictly increasing and $Q(\infty)>c_{N}$, then $T_{0}^{*} \geq T_{1}^{*}$.

Next, suppose that a database becomes impossible for any updates and the GC is done immediately when the total number of updates has exceeded $N$ before time $T$. Then, the mean time to GC is

$$
T \sum_{j=0}^{N-1} p_{j}(T)+\int_{0}^{T} t h(t) p_{N-1}(t) \mathrm{d} t=\sum_{j=0}^{N-1} \int_{0}^{T} p_{j}(t) \mathrm{d} t
$$

and by a similar method for obtaining (8.15), the mean time for GC is

$$
\begin{aligned}
& \sum_{j=0}^{N-1} p_{j}(T)\left[c_{T}+\sum_{i=0}^{j} \alpha c_{0}(i)\right]+\sum_{j=N}^{\infty} p_{j}(T)\left[c_{N}+\sum_{i=0}^{N} \alpha c_{0}(i)\right] \\
& =c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)+\sum_{i=1}^{N} \alpha c_{0}(i) \sum_{j=i}^{\infty} p_{j}(T)
\end{aligned}
$$

In this case, the availability is

$$
\begin{aligned}
\widetilde{A}_{1}(T)= & \frac{\sum_{j=0}^{N-1} \int_{0}^{T} p_{j}(t) \mathrm{d} t}{\sum_{j=0}^{N-1} \int_{0}^{T} p_{j}(t) \mathrm{d} t+c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)} . \\
& +\sum_{i=1}^{N} \alpha c_{0}(i) \sum_{j=i}^{\infty} p_{j}(T)
\end{aligned}
$$

In particular, by setting that $p_{0}(t)=\bar{F}(t)$ when $N=1$,

$$
\widetilde{A}_{1}(T)=\frac{\int_{0}^{T} \bar{F}(t) \mathrm{d} t}{\int_{0}^{T} \bar{F}(t) \mathrm{d} t+c_{T}+\left[c_{N}-c_{T}+\alpha c_{0}(1)\right] F(T)}
$$

that agrees with (6.13) of [1] when $\alpha=0$. That is, the policy maximizing $\widetilde{A}_{1}(T)$ corresponds to the policy maximizing the availability of a one-unit system with repair and preventive maintenance.# (2) Model 2 with Amount of Garbage 

Suppose that an amount of garbage arises from each update according to a probability distribution $G(x)$ and the total garbage is additive. The distribution of the total garbage at the $j$ th update is $G^{(j)}(x)$, where $G^{(j)}(x)$ $(j=1,2, \cdots)$ is the $j$-fold convolution of $G(x)$ and $G^{(0)}(x) \equiv 1$ for $x \geq 0$. Furthermore, the mean time required for the collection of this garbage is $c_{0}(x)$ that depends only on its amount and increases from $c_{0}(0)=0$. The mean time for GC at time $T$ is $c_{T}$ when the total garbage is less than an upper limit level $K$ and is $c_{K}$ with $c_{K} \geq c_{T}$ when it has exceeded $K$. Under this policy, the mean time for GC at time $T$ is

$$
\begin{aligned}
& \sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)+\sum_{j=0}^{\infty} p_{j}(T) \int_{K}^{\infty}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& =c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)+\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{\infty} c_{0}(x) \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Therefore, the availability is

$$
\begin{aligned}
A_{2}(T)= & \frac{T}{T+c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)} \\
& +\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{\infty} c_{0}(x) \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Differentiating $A_{2}(T)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
& \left(c_{K}-c_{T}\right)\left\{T h(T) \sum_{j=0}^{\infty} p_{j}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]+\sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)\right\} \\
& \quad+T h(T) \sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{\infty} c_{0}(x) \mathrm{d}\left[G^{(j+1)}(x)-G^{(j)}(x)\right] \\
& \quad-\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{\infty} c_{0}(x) \mathrm{d} G^{(j)}(x)=c_{K}
\end{aligned}
$$

We can make discussions similar to those of the case (1).
Suppose that a database becomes impossible for any updates and the GC is done immediately, when the total garbage has exceeded $K$ before time $T$. Then, the mean time to GC is

$$
\begin{aligned}
& T \sum_{j=0}^{\infty} G^{(j)}(K) p_{j}(T)+\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{T} t p_{j}(t) h(t) \mathrm{d} t \\
& =\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t
\end{aligned}
$$and the mean time for GC is

$$
\begin{aligned}
& \sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[c_{T}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& \quad+\sum_{j=0}^{\infty} \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t \int_{0}^{K}\left\{\int_{K-y}^{\infty}\left[c_{K}+c_{0}(x+y)\right] \mathrm{d} G(x)\right\} \mathrm{d} G^{(j)}(y)
\end{aligned}
$$

Therefore, the availability is

$$
\begin{aligned}
\widetilde{A}_{2}(T)= & \frac{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t+c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)} \\
& +\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K} c_{0}(x) \mathrm{d} G^{(j)}(x) \\
& +\sum_{j=0}^{\infty} \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t \int_{0}^{K}\left[\int_{K-y}^{\infty} c_{0}(x+y) \mathrm{d} G(x)\right] \mathrm{d} G^{(j)}(y)
\end{aligned}
$$

Example 8.2. We compute optimum times $T_{i}^{*}$ numerically that maximize $A_{i}(T)(i=1,2)$ in (8.16) and (8.25), respectively, when $h(t)=\lambda, G(x)=$ $1-\mathrm{e}^{-\mu x}$, and $c_{0}(x)=c_{0} x$, i.e., the mean time to collect garbage increases in proportion to the number of updates or the total garbage and $p_{j}(t)=$ $\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}$. Then, from (8.17), an optimum $T_{1}^{*}$ satisfies

$$
\left(c_{N}-c_{T}\right)\left[\lambda T p_{N-1}(T)+\sum_{j=0}^{N-1} p_{j}(T)\right]+c_{0} \alpha \frac{(\lambda T)^{2}}{2}=c_{N}
$$

When $N$ goes to infinity, an optimum time is given by

$$
\widetilde{T}_{1}=\frac{1}{\lambda} \sqrt{\frac{2 c_{T}}{\alpha c_{0}}}
$$

From (8.26), an optimum $T_{2}^{*}$ satisfies

$$
\lambda T \sum_{j=0}^{\infty} p_{j}(T) \frac{(\mu K)^{j}}{j!} \mathrm{e}^{-\mu K}-\sum_{j=1}^{\infty} p_{j}(T) \sum_{i=0}^{j-1} \frac{(\mu K)^{i}}{i!} \mathrm{e}^{-\mu K}=\frac{c_{T}}{c_{K}-c_{T}}
$$

Tables 8.3 and 8.4 present $T_{1}^{*}$ and $T_{2}^{*}$ for $N=\mu K=300,500,700$, $c_{k} / c_{T}=2,5,10(k=N, K)$, and $c_{T} / c_{0}=3,5,10,20$ when $\alpha=10^{-4}$ and $\lambda=10$, and $\widetilde{T}_{1}$ when $N=\infty$. Optimum $T_{1}^{*}$ are strictly increasing in $N$ to $\widetilde{T}_{1}$. From the assumption of $N=\mu K$, optimum times are almost the same ones. From this example, when $N=\mu K=500, c_{k} / c_{T}=2$, and $c_{T} / c_{0}=20, T_{1}^{*}$ and $T_{2}^{*}$ are about 44 , that is, when a database is updated 10 times an hour and exceeds a limit level at 50 hours, on average, the GC should be done at 44 hours, i.e., at about 5.5 days when it is used for 8 hours a day. This also indicates that $\widetilde{T}_{1}$ when $N=\infty$ is approximately good when $N$ is large and $c_{T} / c_{0}$ is small.Table 8.3. Optimum time $T_{1}^{*}$ when $\alpha=10^{-4}, \lambda=10$, and $\widetilde{T}_{1}$ when $N=\infty$

| $N$ | $c_{T} / c_{0}$ | $c_{N} / c_{T}$ |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  | 2 | 5 | 10 |
| 300 | 3 | 24.3 | 24.1 | 23.9 |
|  | 5 | 25.9 | 25.2 | 24.8 |
|  | 10 | 26.4 | 25.5 | 25.1 |
|  | 20 | 26.6 | 25.7 | 25.2 |
| 500 | 3 | 24.5 | 24.5 | 24.5 |
|  | 5 | 31.6 | 31.6 | 31.6 |
|  | 10 | 43.3 | 42.7 | 42.3 |
|  | 20 | 44.8 | 43.8 | 43.3 |
| 700 | 3 | 24.5 | 24.5 | 24.5 |
|  | 5 | 31.6 | 31.6 | 31.6 |
|  | 10 | 44.7 | 44.7 | 44.7 |
|  | 20 | 61.7 | 61.0 | 60.6 |
| $\infty$ | 3 |  | 24.5 |  |
|  | 5 |  | 31.6 |  |
|  | 10 |  | 44.7 |  |
|  | 20 |  | 63.2 |  |

Next, when $h(t)=\lambda$ and $c_{0}(j)=c_{0}$ for Model 1, a finite $T_{1}^{*}$ does not exist. However, there exists a finite and unique $\widetilde{T}_{1}^{*}$ to maximize $\widetilde{A}_{1}(T)$ in (8.22) for $c_{N}>c_{T}$ that satisfies

$$
\frac{\lambda p_{N-1}(T) \sum_{j=0}^{N-1} \int_{0}^{T} p_{j}(t) \mathrm{d} t}{\sum_{j=0}^{N-1} p_{j}(T)}+\sum_{j=0}^{N-1} p_{j}(T)=\frac{c_{N}}{c_{N}-c_{T}}
$$

Table 8.5 indicates the optimum time $\widetilde{T}_{1}^{*}$ for $N=300,500,700$ and $c_{N} / c_{T}=$ $2,5,10$. These optimum values are $\widetilde{T}_{1}^{*}>T_{1}^{*}$, however, almost the same as those in Table 8.3 when $c_{T} / c_{0}=20$.

If a database is updated in a Poisson process and the mean time to collect garbage is constant, then the latter modified model of Model 1 would be more practical than the first one. Moreover, by modifying these models, we would consider some models where the GC should be done at the number of updates, the amount of garbage, or the memory areas.

We have assumed until now that $c_{k}(k=T, N, K)$ represents as the time for the GC at $k$. If $c_{k}$ is denoted as the cost for the GC at $k$, the availabilities derived in the section can be easily converted to the expected cost rates as follows: The expected cost rates of Model 1 are, from (8.16) and (8.22), respectively,

$$
C_{1}(T)=\frac{1}{T}\left[c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)+\sum_{j=0}^{\infty} p_{j}(T) \sum_{i=0}^{j} \alpha c_{0}(i)\right]
$$Table 8.4. Optimum time $T_{2}^{*}$ when $\lambda=10$

| $\mu K$ | $c_{K} / c_{T}$ |  |  |
| :--: | :--: | :--: | :--: |
|  | 2 | 5 | 10 |
| 300 | 26.2 | 24.5 | 23.8 |
| 500 | 44.3 | 42.5 | 41.6 |
| 700 | 62.9 | 60.8 | 59.7 |

Table 8.5. Optimum time $\widetilde{T}_{1}^{*}$ when $\lambda=10$

| $N$ | $c_{N} / c_{T}$ |  |  |
| :--: | :--: | :--: | :--: |
|  | 2 | 5 | 10 |
| 300 | 26.7 | 25.8 | 25.3 |
| 500 | 45.5 | 44.3 | 43.7 |
| 700 | 64.4 | 63.0 | 62.3 |

and

$$
\widetilde{C}_{1}(T)=\frac{c_{N}-\left(c_{N}-c_{T}\right) \sum_{j=0}^{N-1} p_{j}(T)+\sum_{i=1}^{N} \alpha c_{0}(i) \sum_{j=i}^{\infty} p_{j}(T)}{\sum_{j=0}^{N-1} \int_{0}^{T} p_{j}(t) \mathrm{d} t}
$$

The expected cost rates of Model 2 are, from (8.25) and (8.29), respectively,

$$
C_{2}(T)=\frac{1}{T}\left[c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K)+\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{\infty} c_{0}(x) \mathrm{d} G^{(j)}(x)\right]
$$

and

$$
\begin{aligned}
& c_{K}-\left(c_{K}-c_{T}\right) \sum_{j=0}^{\infty} p_{j}(T) G^{(j)}(K) \\
& +\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K} c_{0}(x) \mathrm{d} G^{(j)}(x)] \\
\widetilde{C}_{2}(T)= & \frac{+\sum_{j=0}^{\infty} \int_{0}^{T} p_{j}(t) h(t) \mathrm{d} t \int_{0}^{K}\left[\int_{K-y}^{\infty} c_{0}(x+y) \mathrm{d} G(x)\right] \mathrm{d} G^{(j)}(y)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T} p_{j}(t) \mathrm{d} t}
\end{aligned}
$$

# 8.3 Modified Periodic Garbage Collection Model 

We apply the condition-based preventive maintenance in Section 6.1 to the GC model with an upper limit level $K$ of the total garbage: A database is updated in a nonhomogeneous Poisson process with a mean value function $H(t)$. An amount $W_{j}$ of garbage arises from the $j$ th update and has a probability distribution $G(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}(j=1,2, \cdots)$, and the garbage is additive. The total garbage is checked at periodic times $n T(n=1,2, \cdots)$, i.e., it isinvestigated only through checking of space areas and storage conditions in the database. Any maintenance is not done if the total garbage is less than a managerial level $Z(0 \leq Z \leq K)$. On the other hand, if the total garbage has exceeded $Z$ during $(n T,(n+1) T]$, the GC is done at time $(n+1) T$ and the database is restored to its original state.

Let $c_{K}$ be a loss cost for a useless database when the total garbage is equal to $K$, and $c_{Z}$ be a loss cost for the GC where $c_{Z}<c_{K}$ when the total garbage has exceeded $Z$. Then, from (6.4), the expected cost rate for the GC policy is

$$
\begin{gathered}
c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \\
C(Z)=\frac{\times \sum_{i=0}^{\infty} p_{i}[H((n+1) T)-H(n T)] \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)}{\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}[H(n T)] \sum_{i=0}^{\infty} \int_{0}^{Z} G^{(i)}(K-x)] \mathrm{d} G^{(j)}(x)} \\
\times \int_{n T}^{(n+1) T} p_{i}[H(t)-H(n T)] \mathrm{d} t
\end{gathered}
$$

In particular, when a database is updated in a Poisson process, i.e., $H(t)=$ $\lambda t$, the expected cost rate is rewritten as

$$
\begin{gathered}
c_{Z}+\left(c_{K}-c_{Z}\right) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \\
C(Z)=\frac{\times \sum_{i=0}^{\infty} p_{i}(\lambda T) \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)}{\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{Z} G^{(i)}(K-x)] \mathrm{d} G^{(j)}(x) \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t}
\end{gathered}
$$

where $p_{j}(t) \equiv\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$. The optimum GC policy from Section 6.1.2 is given as follows:
(i) If $M_{G}(K)>c_{Z} /\left(c_{K}-c_{Z}\right)$, then there exists a unique $Z^{*}\left(0<Z^{*}<K\right)$ that satisfies

$$
\begin{aligned}
& Q(Z) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t \int_{0}^{Z} G^{(i)}(K-x)] \mathrm{d} G^{(j)}(x) \\
& -\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} p_{i}(\lambda T) \int_{0}^{Z}\left[1-G^{(i)}(K-x)\right] \mathrm{d} G^{(j)}(x)=\frac{c_{Z}}{c_{K}-c_{Z}}
\end{aligned}
$$

where $M_{G}(K) \equiv \sum_{j=1}^{\infty} G^{(j)}(K)$ and

$$
Q(Z) \equiv \frac{\sum_{i=0}^{\infty} p_{i}(\lambda T)\left[1-G^{(i)}(K-Z)\right]}{\sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t G^{(i)}(K-Z)} \quad(0 \leq Z \leq K)
$$

In this case, the expected cost rate is

$$
C\left(Z^{*}\right)=\left(c_{K}-c_{Z}\right) Q\left(Z^{*}\right)
$$

(ii) If $M_{G}(K) \leq c_{Z} /\left(c_{K}-c_{Z}\right)$, then $Z^{*}=K$, i.e., the GC is done after the total garbage becomes $K$, and the resulting cost rate is given in (3.12).Table 8.6. Optimum garbage rate $Z^{*} / K$ to minimize $C(Z)$

| $\lambda T$ | $\mu K$ | $c_{K} / c_{Z}$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 100 | 200 | 500 | 1000 |
| 60 | 300 | 0.708 | 0.696 | 0.683 | 0.673 |
|  | 500 | 0.825 | 0.818 | 0.810 | 0.804 |
|  | 700 | 0.875 | 0.870 | 0.864 | 0.860 |
|  | 1000 | 0.912 | 0.909 | 0.905 | 0.902 |
| 120 | 300 | 0.963 | 0.923 | 0.802 | 0.702 |
|  | 500 | 0.978 | 0.954 | 0.881 | 0.821 |
|  | 700 | 0.984 | 0.976 | 0.915 | 0.872 |
|  | 1000 | 0.989 | 0.977 | 0.941 | 0.911 |

Example 8.3. We compute the optimum policy numerically when $G(x)=$ $1-\mathrm{e}^{-\mu x}$ and $\widetilde{p}(x)=\left[(\mu x)^{j} / j!\right] \mathrm{e}^{-\mu x}(j=0,1,2, \ldots)$. In this case, (8.36) is

$$
\begin{aligned}
& Q(Z) \sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} \int_{0}^{T} p_{i}(\lambda t) \mathrm{d} t \\
& \times\left[1-\sum_{k=0}^{j-1} \widetilde{p}_{k}(\mu Z)-\sum_{k=0}^{i-1} \sum_{l=0}^{k} \widetilde{p}_{k-l}(\mu(K-Z)) \widetilde{p}_{l+j}(\mu Z)\right] \\
&-\sum_{n=0}^{\infty} \sum_{j=0}^{\infty} p_{j}(n \lambda T) \sum_{i=0}^{\infty} p_{i}(\lambda T) \sum_{k=0}^{i-1} \sum_{l=0}^{k} \widetilde{p}_{k-l}(\mu(K-Z)) \widetilde{p}_{l+j}(\mu Z) \\
&= \frac{c_{Z}}{c_{K}-c_{Z}}
\end{aligned}
$$

where $\sum_{0}^{-1} \equiv 0$. From optimum policy (i), if $\mu K>c_{Z} /\left(c_{K}-c_{Z}\right)$, then a finite $Z^{*}$ to satisfy (8.38) exists uniquely.

Suppose that a database is updated in a Poisson process and the expected number of updates during any interval $(n T,(n+1) T]$ is $H((n+1) T)-H(n T)=$ $\lambda T=60,120$. An upper limit level of the total garbage is $\mu K=300,500$, $700,1000$. For example, when $\mu K=700$, the database becomes useless at 700 updates, on average. In addition, when $\lambda T=120$ and $\lambda=5$, the expected number of updates is 120 times a day, and hence, the database becomes useless at $700 / 120 \approx 5.8$ days.

Under the above conditions, Table 8.6 presents the optimum garbage rate $Z^{*} / K$ for an upper limit level when $c_{K} / c_{Z}=100,200,500,1000$. This example indicates that the optimum value $Z^{*}$ to minimize the expected cost rate increases with $K$ and decreases with cost rate $c_{K} / c_{Z}$. For example, when $\lambda T=120, \mu K=700$, and $c_{K} / c_{Z}=1000$, the optimum value is $Z^{*} / K=0.872$. If the total garbage has exceeded $87.2 \%$ of an upper limit level $K$, then the GC is done. In this case, the expected number of updates is about $700 \times 0.872 \approx 610$ times. Hence, if $\lambda=5$, then it is the most economical that the GC is done at the interval $610 / 120 \approx 5$ days.# Backup Policies for a Database System 

In recent years, a database in computers systems has become of great importance in modern society with high information. In particular, a reliable database is the most indispensable instrument in on-line transaction processing systems such as real-time systems used for bank accounts. For instance, some errors in the on-line system of a bank might cause social confusion even for a short time, and occasionally, a bank might lose valuable public confidence with oneself.

The data in a computer system are frequently updated by adding or deleting them, and are stored in secondary media. However, data files in secondary media are sometimes broken by several errors due to noise, human errors, and hardware faults. In this case, we have to reconstruct the same files from the beginning. The most simple and dependable method to ensure the safety of data would be always to score the backup copies of all files in other places, and to take them out if some files in the original secondary media are broken. This is called a total backup. But, this method would take hours and be costly when files become very large. To make the backup copies efficiently, we might dump only files that have changed since the last backup. This would reduce significantly both the duration time and the backup size [228]. This is called an export backup.

The total backup is a physical backup scheme that copies all files from the original secondary media into other places. On the other hand, the export backup is a logical backup scheme that copies the data and the definition of a database, where they are stored in the operating system of binary notation. This is generally classified into three schemes: incremental backup, cumulative backup, and full backup or complete backup [229].

The full backup exports all files, and a database system returns to its initial state by this backup. When the full backup copies are repeated frequently, all images of a database can be secured, however, its operating cost and time are remarkably increased. Thus, the scheme of incremental or cumulative backup is usually adopted, and is suitably executed between the operations of full backups in most database systems. The incremental backup exports only files

Fig. 9.1. Incremental backup scheme
that have changed since the last incremental or full backup and imports files of all incremental and the last full backup when some errors have occurred in storage media (Figure 9.1). Similarly, the cumulative backup exports only files that have changed since the last full backup and imports files of the last cumulative and full backups when some errors have occurred. The full backup with large overhead is done at long intervals and the incremental or cumulative backup with small overhead is done at short intervals (Figure 9.2). This could reduce significantly both the duration and cost of backups.

An important problem in actual backup schemes is when to create the full backup. We want to lessen the number of full backups with large overhead. However, both overheads of cumulative backup and recovery of incremental backup increase adaptively with the amount of newly updated trucks. From this point of view, we have to decide the full backup interval by comparing two overheads of backup and recovery.

Some recovery techniques for database failures were taken up [230, 231]. Optimum checkpoint intervals of such models that minimize the total overhead were studied $[232-235]$.

Fig. 9.2. Cumulative backup scheme

In this chapter, we apply the cumulative damage model to the backup of files for database media failures by transforming shock into update and damage into dumped files $[59,236,237]$.

# 9.1 Incremental Backup Policy 

First, this section considers a modified cumulative damage model with minimal maintenance at shocks in Section 5.4: Suppose that shocks occur in a nonhomogeneous Poisson process and the total damage due to shocks is additive. However, when the total damage has exceeded a threshold level $K$, it is not additive, and hence, its level is constant at $K$ and minimal maintenance is done at each shock. The damage level remains unchanged by any minimal maintenance. To lessen the maintenance costs after the total damage has exceeded $K$, the preventive maintenance (PM) is done at a planned time $T$. The expected cost rate is obtained, and an optimum PM time $T^{*}$ that minimizes

Fig. 9.3. Process for PM at time $T$
it is discussed analytically in the special case where the times between shocks have an exponential distribution.

Secondly, this model is applied to the backup policy for a database system with secondary storage files when the incremental backup is adopted. Optimum full backup times are computed numerically for several cases.

# 9.1.1 Cumulative Damage Model with Minimal Maintenance 

Consider the cumulative damage model where successive shocks occur at time interval $X_{j}$ and each shock causes some damage in the amount $W_{j}(j=$ $1,2, \cdots)$. It is assumed that $F(t) \equiv \operatorname{Pr}\left\{X_{j} \leq t\right\}$ with finite mean $1 / \lambda \equiv$ $\int_{0}^{\infty}[1-F(t)] \mathrm{d} t$, and $G_{j}(x) \equiv \operatorname{Pr}\left\{W_{j} \leq x\right\}$ with finite mean $1 / \mu_{j} \equiv \int_{0}^{\infty}[1-$ $\left.G_{j}(x)\right] \mathrm{d} x(j=1,2, \cdots)$.

Suppose that the total damage due to shocks is additive when it has not exceeded a threshold level $K$, and conversely, it is not additive at any shock after it has exceeded $K$ (Figure 9.3). In this case, the minimal maintenance is done at each shock and the damage level remains in $K$. Then, the total damage $Z_{j} \equiv \sum_{i=1}^{j} W_{i}$ to the $j$ th shock, where $Z_{0} \equiv 0$, has a probability distribution

$$
G^{(j)}(x) \equiv \operatorname{Pr}\left\{Z_{j} \leq x\right\}= \begin{cases}1 & (j=0) \\ G_{1}(x) * G_{2}(x) * \cdots * G_{j}(x) & (j=1,2, \cdots)\end{cases}
$$where the asterisk mark represents the Stieltjes convolution, i.e., $a(t) * b(t) \equiv$ $\int_{0}^{t} b(t-u) \mathrm{d} a(u)$ for any function $a(t)$ and $b(t)$.

The distribution of the total damage $Z(t)$ defined in (2.1) is, from (2.3),

$$
\operatorname{Pr}\{Z(t) \leq x\}= \begin{cases}\sum_{j=0}^{\infty} G^{(j)}(x)\left[F^{(j)}(t)-F^{(j+1)}(t)\right] & (x \leq K) \\ 1 & (x>K)\end{cases}
$$

and the survival probability is

$$
\operatorname{Pr}\{Z(t)>x\}= \begin{cases}\sum_{j=0}^{\infty}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] F^{(j+1)}(t) & (x \leq K) \\ 0 & (x>K)\end{cases}
$$

where $F^{(j)}(t)(j=1,2, \cdots)$ is the $j$-fold Stieltjes convolution of $F(t)$ and $F^{(0)}(t) \equiv 1$ for $t \geq 0$. Thus, the total expected damage at time $t$ is given by

$$
E\{Z(t)\}=\sum_{j=1}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \int_{0}^{K}\left[1-G^{(j)}(x)\right] \mathrm{d} x
$$

Suppose that the minimal maintenance for the above model is done at each shock and the damage level remains unchanged by any minimal maintenance. To lesson the maintenance costs after the total damage has exceeded $K$, the PM is done at a planned time $T(0<T \leq \infty)$. The expected number of minimal maintenance, i.e., the expected number of shocks in $[0, T]$ before the total damage has exceeded $K$ is

$$
\sum_{j=1}^{\infty} j\left[F^{(j)}(T)-F^{(j+1)}(T)\right] G^{(j)}(K)
$$

Furthermore, the expected number of minimal maintenance actions in $[0, T]$ in the case where the total damage remains in $K$ when it has reached $K$ is

$$
\begin{aligned}
& \sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \\
& \quad \times \sum_{i=0}^{\infty}(i+1) \int_{0}^{T}\left[F^{(i)}(T-t)-F^{(i+1)}(T-t)\right] \mathrm{d} F^{(j+1)}(t) \\
& =\sum_{j=1}^{\infty} F^{(j)}(T)\left[1-G^{(j)}(K)\right]
\end{aligned}
$$

and the expected number of minimal maintenance actions in $[0, T]$ in the case where the total damage is less than $K$ when it has reached $K$ is

$$
\sum_{j=1}^{\infty} j F^{(j+1)}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]
$$Thus, the total expected number of minimal maintenance actions in $[0, T]$ in the case where the total damage is less than $K$ is the sum of (9.5) and (9.7) and is given by

$$
\sum_{j=1}^{\infty} F^{(j)}(T) G^{(j)}(K)
$$

It is evident that $(9.6)+(9.8)=\sum_{j=1}^{\infty} F^{(j)}(T) \equiv M_{F}(T)$ that represents the expected number of shocks in $[0, T]$.

# (1) Expected Cost 

We introduce the following costs: The PM cost at time $T$ is $c_{K}+c_{0}(K)$ when the total damage has reached a threshold level $K$, and $c_{K}+c_{0}(x)$ when the total damage is $x(0 \leq x \leq K)$. Then, from (9.3), the PM cost when the total damage is $K$ is

$$
\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{\infty} F^{(j+1)}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]
$$

and from (9.2), the PM cost when the total damage is less than $K$ is

$$
\sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)
$$

Let $c_{m}$ and $c_{M}\left(c_{m}<c_{M}\right)$ be the respective costs of minimal maintenance at each shock when the total damage is less than $K$ and is $K$. Then, the expected cost rate is, from (9.6), (9.8), (9.9), and (9.10),

$$
\begin{aligned}
C(T)= & \frac{1}{T}\left\{\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{\infty} F^{(j+1)}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]\right. \\
& +\sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& \left.\left.+c_{M} \sum_{j=1}^{\infty} F^{(j)}(T)\left[1-G^{(j)}(K)\right]+c_{m} \sum_{j=1}^{\infty} F^{(j)}(T) G^{(j)}(K)\right\}\right)
\end{aligned}
$$

If shocks occur in a nonhomogeneous Poisson process with a mean value function $H(t)$, the expected cost rate in (9.11) is rewritten as, replacing $F^{(j)}(t)-F^{(j+1)}(t)$ with $p_{j}(t) \equiv\left\{[H(t)]^{j} / j!\right\} \mathrm{e}^{-H(t)}$,$$
\begin{aligned}
\widetilde{C}(T)= & \frac{1}{T}\left\{\left[c_{K}+c_{0}(K)\right] \sum_{j=0}^{\infty} p_{j}(T)\left[1-G^{(j)}(K)\right]\right. \\
& +\sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& \left.+c_{M} \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left[1-G^{(i)}(K)\right]+c_{m} \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j} G^{(i)}(K)\right\}
\end{aligned}
$$

# (2) Optimum Policy 

Suppose that shocks occur in a Poisson process with rate $\lambda$, i.e., $F(t)=$ $1-\mathrm{e}^{-\lambda t}$ and $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$. In addition, it is assumed that $c_{0}(x)=c_{0} x$, i.e., the PM cost is proportional to the total damage. Then, (9.11) or (9.12) is simplified as

$$
\begin{aligned}
C(T)= & \frac{1}{T}\left\{c_{0} \sum_{j=1}^{\infty} p_{j}(T) \int_{0}^{K}\left[1-G^{(j)}(x)\right] \mathrm{d} x\right. \\
& \left.-\left(c_{M}-c_{m}\right) \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j} G^{(i)}(K)+c_{K}+c_{M} \lambda T\right\}
\end{aligned}
$$

We seek an optimum PM time $T^{*}$ that minimizes $C(T)$ in (9.13). It is clear that $\lim _{T \rightarrow 0} C(T)=\infty$ and $\lim _{T \rightarrow \infty} C(T)=\lambda c_{M}$. Thus, there exists a positive $T^{*}\left(0<T^{*} \leq \infty\right)$ that minimizes $C(T)$. Differentiating $C(T)$ with respect to $T$ and setting it equal to zero,

$$
\begin{aligned}
c_{0} & \left\{\lambda T \sum_{j=0}^{\infty} p_{j}(T) \int_{0}^{K}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} x\right. \\
& \left.-\sum_{j=1}^{\infty} p_{j}(T) \int_{0}^{K}\left[1-G^{(j)}(x)\right] \mathrm{d} x\right\} \\
& +\left(c_{M}-c_{m}\right) \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left[G^{(i)}(K)-G^{(j)}(K)\right]=c_{K}
\end{aligned}
$$

In the particular case of $c_{0}=0,(9.14)$ becomes

$$
\sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left[G^{(i)}(K)-G^{(j)}(K)\right]=\frac{c_{K}}{c_{M}-c_{m}}
$$

Letting the left-hand side of (9.15) be denoted by $Q(T), \lim _{T \rightarrow 0} Q(T)=0$, $\lim _{T \rightarrow \infty} Q(T)=\sum_{j=1}^{\infty} G^{(j)}(K) \equiv M_{G}(K)$, and$$
\frac{\mathrm{d} Q(T)}{\mathrm{d} T}=\lambda \sum_{j=1}^{\infty} p_{j}(T)\left[G^{(j)}(K)-G^{(j+1)}(K)\right]>0
$$

Thus, $Q(T)$ is strictly increasing from 0 to $M_{G}(K)$ that is the expected number of shocks before the total damage exceeds a threshold level $K$. In this case, we have the following optimum policy:
(i) If $M_{G}(K)>c_{K} /\left(c_{M}-c_{m}\right)$, then there exists a finite and unique $T^{*}$ $\left(0<T^{*}<\infty\right)$ that satisfies (9.15).
(ii) If $M_{G}(K) \leq c_{K} /\left(c_{M}-c_{m}\right)$, then $T^{*}=\infty$, i.e., the PM should not be done.

Note that an optimum $T^{*}\left(0<T^{*}<\infty\right)$ always exists for $c_{0}>0$ because the left-hand side of (9.14) increases from 0 to $\infty$, as $T \rightarrow \infty$.

# 9.1.2 Incremental Backup 

We apply the cumulative damage model discussed in Section 9.1.1 to the backup of secondary storage files in a database system. Suppose that a database is updated in a Poisson process with rate $\lambda$. To ensure the safety of data and to save costs or hours, we make the following backup policy: When the total dumped files do not exceed a threshold level $K$, we perform the incremental backup of only new files since the previous backup. Conversely, when the total files have exceeded $K$, we perform the total backup instead where both the time and size of the backup are constant. In addition, we perform the full backup at periodic times $n T(n=1,2, \cdots)$ where all files are dumped and the system returns to its initial state.

Let us introduce the following costs: Cost $c_{K}+c_{0} x$ is incurred for the full backup when the total files are $x(0 \leq x \leq K)$ at periodic times $n T$, and cost $c_{K}+c_{0} K$ is incurred for the full backup when the total files have exceeded $K$. Furthermore, let $c_{m}$ and $c_{M}\left(c_{m}<c_{M}\right)$ be the costs for incremental and total backups, respectively. Under such assumptions, the expected cost rate has been already given in (9.13).

In this section, we consider two cases: (1) Backup files due to each update have an identical probability distribution, and (2) backup files due to each update have different probability distributions that increase at a geometric rate.

## (1) Identical Distribution

Suppose that backup files due to each update have an identical exponential distribution $G(x)$, i.e., $G^{(j)}(x)=\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}(j=0,1,2, \cdots)$. Then, because

$$
\int_{0}^{K}\left[G^{(j)}(x)-G^{(j+1)}(x)\right] \mathrm{d} x=\frac{1}{\mu} G^{(j+1)}(K)
$$and

$$
\int_{0}^{K}\left[1-G^{(j)}(x)\right] \mathrm{d} x=\frac{1}{\mu} \sum_{i=1}^{j} G^{(i)}(K)
$$

the expected cost rate $C(T)$ in (9.13) and (9.14) is simplified, respectively, as

$$
C(T)=\frac{1}{T}\left[c_{K}+c_{M} \lambda T-\left(c_{M}-c_{m}-\frac{c_{0}}{\mu}\right) \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j} G^{(i)}(K)\right]
$$

and

$$
\left(c_{M}-c_{m}-\frac{c_{0}}{\mu}\right) \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left[G^{(i)}(K)-G^{(j)}(K)\right]=c_{K}
$$

where $p_{j}(t)=\left[(\lambda t)^{j} / j!\right] \mathrm{e}^{-\lambda t}(j=0,1,2, \cdots)$. The left-hand side of (9.17) is a strictly increasing function of $T$ from 0 to $\left(c_{M}-c_{m}-c_{0} / \mu\right) \mu K$.

Therefore, if $c_{M}-c_{m}-c_{0} / \mu>c_{K} /(\mu K)$, then there exists a finite and unique $T^{*}$ that satisfies (9.17), and the resulting cost rate is

$$
\frac{C\left(T^{*}\right)}{\lambda}=c_{M}-\left(c_{M}-c_{m}-\frac{c_{0}}{\mu}\right) \sum_{j=1}^{\infty} p_{j}\left(T^{*}\right) G^{(j+1)}(K)
$$

Conversely, if $c_{M}-c_{m}-c_{0} / \mu \leq c_{K} /(\mu K)$, then $T^{*}=\infty$ and $C(\infty)=\lambda c_{M}$.

# (2) Different Distribution 

First, we show that an amount $W_{j}$ of files that is dumped at the $j$ th update decreases at a geometric ratio. Suppose that an amount of files at some update is $W$, the total volume of files is $M$, and the total files that have been already dumped are $A(0 \leq A \leq M)$. Then, assume that an amount of newly dumped files is proportional to the vacant space, i.e., $W(M-A) / M$. Letting $W_{j}$ be newly dumped files at the $j$ th update,

$$
\begin{aligned}
W_{1} & =W \\
W_{j+1} & =W \frac{M-\sum_{i=1}^{j} W_{i}}{M} \quad(j=1,2, \cdots)
\end{aligned}
$$

Solving this equation,

$$
W_{j}=W\left(1-\frac{W}{M}\right)^{j-1} \quad(j=1,2, \cdots)
$$

We set $W / M \equiv 1-\alpha(0 \leq \alpha<1)$ that is an amount ratio of dumped files at the first update. Then, $W_{j} / M=(1-\alpha) \alpha^{j-1}(j=1,2, \cdots)$ that is ageometric distribution with mean $1 /(1-\alpha)$. This indicates that an amount of newly dumped files is strictly decreasing and forms a geometric process with $W / a^{j-1}(j=1,2, \cdots)$, where $1 / a \equiv \alpha[250]$.

Furthermore, it is of interest that the total ratio of dumped files until the $j$ th update is

$$
\frac{1}{M} \sum_{i=1}^{j} W_{i}=1-\alpha^{j} \quad(j=1,2, \cdots)
$$

that is equal to the reliability of a parallel system with $j$ units each of whose reliabilities is $1-\alpha$.

It is usually known that an initial estimated amount of dumped files is about $25 \%$ and a threshold level $K$ is $60 \%$ of the total volume. In this case, the number of updates where the total files exceed $K$ is given by a minimum value that satisfies $1-(1-0.25)^{n} \geq 0.6$ and its solution is $n=4$. Conversely, if the number of updates where the total files exceed $60 \%$ is $n=4$, then the amount rate is given by $1-\alpha^{4} \geq 0.6$ and $1-\alpha$ is larger than 0.205 .

Suppose that an amount $W_{j}$ of newly dumped files at the $j$ th update has an exponential distribution $G_{j}(x)=1-\mathrm{e}^{-\mu_{j} x}\left(\mu_{1}<\mu_{2}<\cdots\right)$. Then, the distribution of total files until the $j$ th update is easily given by

$$
G^{(j)}(x)=1-\sum_{l=1}^{j}\left(\prod_{i=1, i \neq l}^{j} \frac{\mu_{i}}{\mu_{i}-\mu_{l}}\right) \mathrm{e}^{-\mu_{l} x} \quad(j=1,2, \cdots)
$$

where $\sum_{l=1}^{1} \prod_{i=1, i \neq l}^{1}=1$. In particular, when $W_{j}$ increases at a geometric ratio $(0<\alpha<1)$, i.e., $W_{j}=\alpha^{j-1} W$ and $1 / \mu_{j}=\alpha^{j-1} / \mu_{1}=\alpha^{j-1} / \mu$,

$$
G^{(j)}(x)=1-\sum_{l=1}^{j}\left(\prod_{i=1, i \neq l}^{j} \frac{1}{1-\alpha^{i-l}}\right) \mathrm{e}^{-\mu x / \alpha^{l-1}} \quad(j=1,2, \cdots)
$$

Thus, substituting $G^{(j)}(x)$ in (9.21) in (9.13) and (9.14), respectively, the expected cost rate is

$$
C(T)=\frac{1}{T}\left[c_{K}+c_{M} \lambda T-\sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left(c_{M}-c_{m}-\frac{c_{0}}{\mu} \alpha^{i-1}\right) G^{(i)}(K)\right]
$$

and $(9.14)$ is

$$
\begin{aligned}
& \sum_{j=1}^{\infty} p_{j}(T) \sum_{i=1}^{j}\left[\left(c_{M}-c_{m}-\frac{c_{0}}{\mu} \alpha^{i-1}\right) G^{(i)}(K)-\left(c_{M}-c_{m}-\frac{c_{0}}{\mu} \alpha^{j-1}\right) G^{(j)}(K)\right] \\
& =c_{K}
\end{aligned}
$$

Denoting the left-hand side of (9.23) by $Q_{1}(T)$, when $M_{G}(K) \equiv \sum_{j=1}^{\infty} G^{(j)}(K)<$ $\infty, Q_{1}(0) \equiv \lim _{T \rightarrow 0} Q_{1}(T)=0$, and$$
Q_{1}(\infty) \equiv \lim _{T \rightarrow \infty} Q_{1}(T)=\sum_{j=1}^{\infty}\left(c_{M}-c_{m}-\frac{c_{0}}{\mu} \alpha^{j-1}\right) G^{(j)}(K)
$$

Therefore, if $Q_{1}(\infty)>c_{K}$, then there exists a finite $T^{*}\left(0<T^{*}<\infty\right)$ that satisfies (9.23), and the resulting cost rate is

$$
\frac{C\left(T^{*}\right)}{\lambda}=c_{M}-\sum_{j=1}^{\infty}\left(c_{M}-c_{m}-\frac{c_{0}}{\mu} \alpha^{j}\right) p_{j}\left(T^{*}\right) G^{(j+1)}(K)
$$

Example 9.1. First, suppose that $W_{j}$ has an identical exponential distribution $G_{j}(x)=1-\mathrm{e}^{-\mu x}(j=1,2, \cdots)$, the total volume of files is $3 \times 10^{5}$ trucks, and a threshold level $K$ is $1.2 \times 10^{5}$ and $1.8 \times 10^{5}$ trucks that correspond to $40 \%$ and $60 \%$ of the total volume, respectively.

Table 9.1 presents the optimum full backup time $\lambda T^{*}$ and the resulting cost rate $C\left(T^{*}\right) / \lambda$ for $c_{K} /\left(c_{M}-c_{m}-c_{0} / \mu\right)=1,2,5,10,15$ and $\mu K=12,18$ when $c_{M}=C(\infty) / \lambda=6$ and $c_{m}+c_{0} / \mu=5$. This indicates that the optimum $T^{*}$ increases with both $c_{K} /\left(c_{M}-c_{m}-c_{0} / \mu\right)$ and $\mu K$, and $C\left(T^{*}\right)$ increases with $c_{K} /\left(c_{M}-c_{m}-c_{0} / \mu\right)$, and conversely, decreases with $\mu K$. However, they are almost unchanged for $c_{K} /\left(c_{M}-c_{m}-c_{0} / \mu\right)$ and $\mu K$.

For example, when the mean time between updates is $1 / \lambda=1$ day, the dumped file is $1 / \mu=10^{4}$ trucks and $K=1.2 \times 10^{5}$ trucks, the optimum full backup time $T^{*}$ is about 9 days for $c_{K} /\left(c_{M}-c_{m}-c_{0} / \mu\right)=2$. In this case, $\mu K / \lambda=12$ days represents the mean time until the total dumped files exceed a threshold level $K$.

Secondly, suppose that the amount $W_{j}$ of newly dumped files at the $j$ th update has different exponential distributions $G_{j}(x)=1-\mathrm{e}^{-\mu_{j} x}(j=1,2, \cdots)$, and $W_{j}$ decreases at a geometric ratio $\alpha(0<\alpha<1)$, i.e., $W_{j}=\alpha^{j-1} W$ and $1 / \mu_{j}=\alpha^{j-1} / \mu_{1} \equiv \alpha^{j-1} / \mu$. Furthermore, the total volume of files is $5 \times 10^{5}$ trucks, a threshold level $K$ is $4 \times 10^{5}$ trucks that corresponds to $80 \%$ of the total volume, and the mean amount of dumped files due to the first update is $1 / \mu=10^{5}$ trucks that corresponds to $25 \%$ of the total volume, i.e., $\mu K=4$.

Table 9.2 presents the optimum full backup time $\lambda T^{*}$ for $c_{K} /\left(c_{M}-c_{m}\right)=1$, $2,3,4,5,6$ and $\alpha=1.00,0.95,0.90,0.85,0.80,0.75$ when $\left(c_{0} / \mu\right) /\left(c_{M}-\right.$ $\left.c_{m}\right)=0.1$. This indicates that the optimum $T^{*}$ increases when $c_{K} /\left(c_{M}-c_{m}\right)$ increases. For example, when the mean time between updates is $1 / \lambda=1$ day, the mean dumped file is $1 / \mu=10^{5}$ trucks and $K=4 \times 10^{5}$ trucks, the optimum time $T^{*}$ is about 10 days for $c_{K} /\left(c_{M}-c_{m}\right)=3$ and $\alpha=0.85$.

This also indicates that $\lambda T^{*}$ decreases when $\alpha$ increases when a finite optimum time exists. For example, when $\alpha=0.90$, if $c_{K} /\left(c_{M}-c_{m}\right) \geq 5.37-$ $0.4=4.97$, then a finite $T^{*}$ does not exist. When $\alpha=0.80, M_{G}(K)=\infty$, i.e., the total dumped files might not exceed $K$ with a certain probability. In this case, when $c_{K} /\left(c_{M}-c_{m}\right) \geq 5$, there does not exist a finite $T$ that satisfies (9.23). When $\alpha=0.75$, no finite $T$ exists for any $c_{K} /\left(c_{M}-c_{m}\right)=1-6$.Table 9.1. Optimum full backup time $\lambda T^{*}$ and expected cost rate $C\left(T^{*}\right) / \lambda$ when $c_{M}=6$ and $c_{m}+c_{0} / \mu=5$

| $c_{K}$ | $\mu K=12$ |  | $\mu K=18$ |  |
| :--: | :--: | :--: | :--: | :--: |
| $c_{M}-c_{m}-c_{0} / \mu$ | $\lambda T^{*}$ | $C\left(T^{*}\right) / \lambda$ | $\lambda T^{*}$ | $C\left(T^{*}\right) / \lambda$ |
| 1 | 7.462 | 5.179 | 11.001 | 5.112 |
| 2 | 9.084 | 5.299 | 12.767 | 5.196 |
| 5 | 12.469 | 5.578 | 16.069 | 5.403 |
| 10 | 18.856 | 5.909 | 20.372 | 5.679 |
| 15 | $\infty$ | 6.000 | 25.893 | 5.898 |

Table 9.2. Optimum full backup time $\lambda T^{*}$ when $\mu K=4$ and $\left(c_{0} / \mu\right) /\left(c_{M}-c_{m}\right)=$ 0.1

| $\alpha$ | $c_{K} /\left(c_{M}-c_{m}\right)$ |  |  |  |  |  | $M_{G}(K)$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 | 5 | 6 |  |
| 1.00 | 3.67 | 5.53 | 7.82 | $\infty$ | $\infty$ | $\infty$ | 4 |
| 0.95 | 4.10 | 6.17 | 8.66 | $\infty$ | $\infty$ | $\infty$ | 4.49 |
| 0.90 | 4.46 | 6.59 | 8.88 | 12.21 | $\infty$ | $\infty$ | 5.37 |
| 0.85 | 5.04 | 7.47 | 10.01 | 13.25 | 18.67 | $\infty$ | 15.28 |
| 0.80 | 6.12 | 9.63 | 14.32 | 28.85 | $\infty$ | $\infty$ | $\infty$ |
| 0.75 | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ |

# 9.2 Incremental and Cumulative Backup Policies 

The incremental backup exports only files that have changed or are new since the last incremental backup or full backup. On the other hand, the cumulative backup exports only files that have changed or are new since the last full backup. When some errors have occurred in storage media, we can recover a database system by importing files of all incremental backups and the full backup for the incremental backup scheme and by importing files of the last cumulative and full backups for the cumulative backup scheme. The cumulative backup exports more files than the incremental one at each update, however, it imports less files than the incremental one when we recover a database system.

It is an important problem to determine which backup scheme should be adopted as the backup policy. It is supposed that the full backup is planned at time $T$ or when a database system fails, whichever occurs first. Then, we compare two schemes of incremental and cumulative backups, using the results in Section 9.1. Furthermore, we discuss optimum full backup times for the incremental and cumulative backups and compare them numerically.# 9.2.1 Expected Cost Rates 

We make the same assumptions as those of Section 9.1.2, $G_{j}(x)=G(x)$ for all $j$, and $K=\infty$, i.e., the total dumped files are eternally additive. In addition, a database in secondary media fails according to a general distribution $D(t)$ with finite mean $1 / \gamma$. Suppose that the full backup is done at a planned time $T(0<T \leq \infty)$ or when a database fails, whichever occurs first.

Let us introduce the following maintenance costs: Cost $c_{F}$ is incurred for the full backup, and cost $c_{K}+c_{0} x$ is incurred for the incremental backup when the amount of export files at the backup time is $x$, and for the cumulative backup when the total amount of export files at the backup time is $x$. The recovery cost is $c_{R}+c_{0} x$ for the cumulative backup if the database fails when the total amount of import files at the recovery time is $x$, and is $c_{R}+c_{0} x+j c_{N}$ for the incremental backup when the number of backups is $j$.

Let denote by

$$
\begin{aligned}
M_{j} & =\int_{0}^{\infty}\left(c_{K}+c_{0} x\right) \mathrm{d} G^{(j)}(x) \\
& =c_{K}+\frac{j c_{0}}{\mu} \\
N_{j} & =\int_{0}^{\infty}\left(c_{R}+c_{0} x\right) \mathrm{d} G^{(j)}(x) \\
& =c_{R}+\frac{j c_{0}}{\mu}
\end{aligned}
$$

Note that $j M_{1}$ is the expected cost of the incremental backup and $\sum_{i=1}^{j} M_{i}$ is the expected cost of the cumulative backup at the $j$ th update, and $N_{j}$ is the expected recovery cost of the cumulative backup, and $N_{j}+j c_{N}$ is the expected recovery cost of the incremental backup when $j$ numbers of updates have occurred at the failure of the database.

Therefore, the expected cost until the full backup for the incremental and cumulative backups are, respectively,

$$
\begin{aligned}
\widetilde{C}_{I}(T)= & c_{F}+\bar{D}(T) \sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right]\left(j M_{1}\right) \\
& +\sum_{j=0}^{\infty} \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t)\left(j M_{1}+N_{j}+j c_{N}\right) \\
= & c_{F}+c_{R} D(T) \\
& +\left(c_{K}+\frac{c_{0}}{\mu}\right) \int_{0}^{T} \bar{D}(t) \mathrm{d} M_{F}(t)+\left(c_{N}+\frac{c_{0}}{\mu}\right) \int_{0}^{T} M_{F}(t) \mathrm{d} D(t)
\end{aligned}
$$

and$$
\begin{aligned}
\widetilde{C}_{C}(T)= & c_{F}+\bar{D}(T) \sum_{j=0}^{\infty}\left[F^{(j)}(T)-F^{(j+1)}(T)\right] \sum_{i=1}^{j} M_{i} \\
& +\sum_{j=0}^{\infty} \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t)\left(\sum_{i=0}^{j} M_{i}+N_{j}\right) \\
= & c_{F}+c_{R} D(T)+c_{K} \int_{0}^{T} \bar{D}(t) \mathrm{d} M_{F}(t) \\
& +\frac{c_{0}}{\mu}\left[\int_{0}^{T} M_{F}(t) \mathrm{d} D(t)+\sum_{j=1}^{\infty} j \int_{0}^{T} \bar{D}(t) \mathrm{d} F^{(j)}(t)\right]
\end{aligned}
$$

where $\sum_{i=1}^{0} \equiv 0, \bar{D}(t) \equiv 1-D(t)$, and $M_{F}(t) \equiv \sum_{j=1}^{\infty} F^{(j)}(t)$.
To compare the two expected costs, we find the difference between them as follows:

$$
\widetilde{C}_{C}(T)-\widetilde{C}_{I}(T)=\frac{c_{0}}{\mu} \sum_{j=1}^{\infty} j \int_{0}^{T} \bar{D}(t) \mathrm{d} F^{(j+1)}(t)-c_{N} \int_{0}^{T} M_{F}(t) \mathrm{d} D(t)
$$

Hence, if

$$
\frac{c_{0}}{\mu} \sum_{j=1}^{\infty} j \int_{0}^{T} \bar{D}(t) \mathrm{d} F^{(j+1)}(t)>c_{N} \int_{0}^{T} M_{F}(t) \mathrm{d} D(t)
$$

then the incremental backup is better than the cumulative one when the full backup is done at time $T$. The smaller the extra cost $c_{N}$ required for the incremental backup when the database fails, the more the incremental backup is useful as the backup scheme.

# (1) Optimum Full Backup Time for Incremental Backup 

Consider the optimum policy for the incremental backup. Because the mean time to the full backup is

$$
T \bar{D}(T)+\int_{0}^{T} t \mathrm{~d} D(t)=\int_{0}^{T} \bar{D}(t) \mathrm{d} t
$$

the expected cost rate is, dividing (9.25) by (9.28),

$$
\begin{gathered}
c_{F}+c_{R} D(T)+\left(c_{K}+c_{0} / \mu\right) \int_{0}^{T} \bar{D}(t) \mathrm{d} M_{F}(t) \\
C_{I}(T)=\frac{+\left(c_{N}+c_{0} / \mu\right) \int_{0}^{T} M_{F}(t) \mathrm{d} D(t)}{\int_{0}^{T} \bar{D}(t) \mathrm{d} t}
\end{gathered}
$$

We find an optimum time $T_{1}^{*}$ that minimizes $C_{I}(T)$ when a database is updated in a Poisson process, i.e., $M_{F}(t)=\lambda t$. Differentiating $C_{I}(T)$ with respect to $T$ and setting it equal to zero,$$
c_{R}\left[r(T) \int_{0}^{T} \bar{D}(t) \mathrm{d} t-D(T)\right]+\lambda\left(c_{N}+\frac{c_{0}}{\mu}\right) \int_{0}^{T} \bar{D}(t)[\operatorname{Tr}(T)-\operatorname{tr}(t)] \mathrm{d} t=c_{F}
$$

where $r(t) \equiv d(t) / \bar{D}(t)$ and $d(t)$ is a density function of $D(t)$. Let $Q_{1}(T)$ be the left-hand side of (9.30). Then, if the failure rate $r(t)$ is strictly increasing, $Q_{1}(T)$ is also strictly increasing from 0 to $Q_{1}(\infty)$. Thus, if $Q_{1}(\infty)>c_{F}$, then there exists a finite and unique $T^{*}$ that satisfies (9.30). Note that if $r(t)$ is strictly increasing to $\infty$, then $Q_{1}(\infty)=\infty$. In this case, the resulting cost rate is

$$
C_{I}\left(T_{1}^{*}\right)=\lambda\left(c_{K}+\frac{c_{0}}{\mu}\right)+\left[c_{R}+\lambda T_{1}^{*}\left(c_{N}+\frac{c_{0}}{\mu}\right)\right] r\left(T_{1}^{*}\right)
$$

# (2) Optimum Full Backup Time for Cumulative Backup 

From (9.26) and (9.28), the expected cost rate for the cumulative backup when a database is updated in a Poisson process with rate $\lambda$ is

$$
C_{C}(T)=\lambda\left(c_{K}+\frac{c_{0}}{\mu}\right)+\frac{c_{F}+c_{R} D(T)+\left(\lambda c_{0} / \mu\right)\left[\int_{0}^{T} \lambda t \bar{D}(t) \mathrm{d} t+\int_{0}^{T} t \mathrm{~d} D(t)\right]}{\int_{0}^{T} \bar{D}(t) \mathrm{d} t}
$$

Thus, differentiating $C_{C}(T)$ with respect to $T$ and setting it equal to zero,

$$
c_{R}\left[r(T) \int_{0}^{T} \bar{D}(t) \mathrm{d} t-D(T)\right]+\frac{\lambda c_{0}}{\mu} \int_{0}^{T} \bar{D}(t)[\lambda(T-t)+\operatorname{Tr}(T)-\operatorname{tr}(t)] \mathrm{d} t=c_{F}
$$

Hence, if $r(t)$ is strictly increasing, then the left-hand side $Q_{2}(T)$ of (9.33) is also strictly increasing from 0 to $Q_{2}(\infty)$. Thus, if $Q_{2}(\infty)>c_{F}$, then there exists a finite and unique $T_{2}^{*}$ that satisfies (9.33). In this case, the resulting cost rate is

$$
C_{C}\left(T_{2}^{*}\right)=\lambda\left(c_{K}+\frac{c_{0}}{\mu}\right)+\frac{\lambda c_{0}}{\mu}\left[\lambda T_{2}^{*}+T_{2}^{*} r\left(T_{2}^{*}\right)\right]+c_{R} r\left(T_{2}^{*}\right)
$$

Example 9.2. Suppose that a database is updated in a Poisson process with rate $\lambda$, the backup is done with probability $\alpha(0<\alpha \leq 1)$, and it fails with probability $\beta \equiv 1-\alpha$ at each update time, i.e., $F^{(j)}(t)-F^{(j+1)}(t)=$ $\left[(\alpha \lambda t)^{j} / j!\right] \mathrm{e}^{-\alpha \lambda t}(j=0,1,2, \cdots), M_{F}(t)=\alpha \lambda t$, and $D(t)=1-\mathrm{e}^{-\beta \lambda t}$. In this case, (9.27) becomes

$$
\widetilde{C}_{C}(T)-\widetilde{C}_{I}(T)=\lambda\left(\frac{\alpha c_{0}}{\mu}-\beta c_{N}\right) \int_{0}^{T} \alpha \lambda t \mathrm{e}^{-\beta \lambda t} \mathrm{~d} t
$$

Thus, if $\alpha\left(c_{0} / \mu\right)>\beta c_{N}$, then the incremental backup is better than the cumulative one, and vice versa.Table 9.3. Optimum full backup time $\lambda T_{1}^{*}$ and expected cost rate $C_{I}\left(T_{1}^{*}\right) /\left(\lambda c_{0} / \mu\right)$ of the incremental backup for $c_{N} /\left(c_{0} / \mu\right)$ when $c_{F} /\left(c_{0} / \mu\right)=64, c_{K} /\left(c_{0} / \mu\right)=40$, $c_{R} /\left(c_{0} / \mu\right)=100$, and $\alpha=0.98$

| $c_{N} /\left(c_{0} / \mu\right)$ | $\lambda T_{1}^{*}$ | $C_{I}\left(T_{1}^{*}\right) /\left(\lambda c_{0} / \mu\right)$ |
| :--: | :--: | :--: |
| 20 | 18.74 | 49.89 |
| 30 | 15.25 | 51.45 |
| 40 | 13.17 | 52.76 |
| 49 | 11.88 | 52.82 |
| 50 | 11.76 | 53.94 |

First, when the incremental backup is adopted, (9.30) is rewritten as

$$
\alpha \lambda T-\frac{\alpha}{\beta}\left(1-\mathrm{e}^{-\beta \lambda T}\right)=\frac{c_{F}}{c_{N}+c_{0} / \mu}
$$

whose left-hand side is strictly increasing from 0 to $\infty$. Thus, there exists a finite and unique $T_{1}^{*}$ that satisfies (9.36), and the resulting cost rate is

$$
\frac{C_{I}\left(T_{1}^{*}\right)}{\lambda}=\alpha c_{K}+\beta c_{R}+\alpha \beta \lambda T_{1}^{*} c_{N}+\left(1+\beta \lambda T_{1}^{*}\right) \frac{\alpha c_{0}}{\mu}
$$

Note from (9.36) that the optimum $T_{1}^{*}$ does not depend on $c_{K}$ and $c_{R}$. Table 9.3 presents the optimum full backup time $T_{1}^{*}$ and the expected cost rate $C_{I}\left(T_{1}^{*}\right) /\left(\lambda c_{0} / \mu\right)$ of the incremental backup for $c_{N} /\left(c_{0} / \mu\right)=20,30,40$, 50 when $c_{F} /\left(c_{0} / \mu\right)=64, c_{K} /\left(c_{0} / \mu\right)=40, c_{R} /\left(c_{0} / \mu\right)=100$, and $\alpha=0.98$. Note that all costs are relative to $\operatorname{cost} c_{0} / \mu$ and all times are relative to $1 / \lambda$. For example, when $c_{N} /\left(c_{0} / \mu\right)=30, \lambda T_{1}^{*}$ is about 15.25 , that is, when the mean time of update is $1 /(\alpha \lambda)=1$ day, the optimum $T_{1}^{*}$ is about 15 days.

Secondly, when the cumulative backup is adopted, (9.33) is

$$
\alpha \lambda T-\frac{\alpha}{\beta}\left(1-\mathrm{e}^{-\beta \lambda T}\right)=\frac{\beta c_{F}}{c_{0} / \mu}
$$

whose left-hand side is equal to that of (9.36), and the resulting cost rate is

$$
\frac{C_{C}\left(T_{2}^{*}\right)}{\lambda}=\alpha c_{K}+\beta c_{R}+\left(1+\lambda T_{2}^{*}\right) \frac{\alpha c_{0}}{\mu}
$$

From the above results, if $c_{N} /\left(c_{0} / \mu\right)<\alpha / \beta$, then $T_{1}^{*}$ is larger than $T_{2}^{*}$ and vice versa. In this example, when $c_{N} /\left(c_{0} / \mu\right)=49, \lambda T_{1}^{*}=\lambda T_{2}^{*}=11.88$ and $C_{I}\left(T_{1}^{*}\right) /\left(\lambda c_{0} / \mu\right)=C_{C}\left(T_{2}^{*}\right) /\left(\lambda c_{0} / \mu\right)=52.82$. Hence, if $c_{N} /\left(c_{0} / \mu\right)<49$, then the incremental backup is better than the cumulative one.# 9.3 Optimum Full Backup Level for Cumulative Backup 

In this section, we derive an optimum full backup level for the cumulative backup. Suppose that we do the full backup when the total files have exceeded a managerial level $K(0 \leq K \leq \infty)$ or when the recovery is completed if the database fails, whichever occurs first. The cumulative backup is done at each update between the full backups.

Underlying the same assumptions as those of Section 9.2, the probability that the full backup is done when the total files have exceeded $K$ is

$$
\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{\infty} \bar{D}(t) \mathrm{d} F^{(j+1)}(t)
$$

and the probability that it is done when the database fails is

$$
\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t)
$$

where $(9.40)+(9.41)=1$. Furthermore, the mean time to the full backup is

$$
\begin{aligned}
& \sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{\infty} t \bar{D}(t) \mathrm{d} F^{(j+1)}(t) \\
& \quad+\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty} t\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \\
& =\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \bar{D}(t) \mathrm{d} t
\end{aligned}
$$

and the expected number of backups before the full backup is

$$
\begin{aligned}
& \sum_{j=1}^{\infty} j\left[G^{(j)}(K)-G^{(j+1)}(K)\right] \int_{0}^{\infty} \bar{D}(t) \mathrm{d} F^{(j+1)}(t) \\
& \quad+\sum_{j=1}^{\infty} j G^{(j)}(K) \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \\
& =\sum_{j=1}^{\infty} G^{(j)}(K) \int_{0}^{\infty} \bar{D}(t) \mathrm{d} F^{(j)}(t)
\end{aligned}
$$

Let us introduce the following costs: Cost $c_{F}$ is incurred for the full backup, cost $c_{K}+c_{0}(x)$ is incurred for the cumulative backup when the total files are $x(0 \leq x \leq K)$, and cost $c_{R}+c_{0}(x)$ is incurred for the recovery when the database fails, where $c_{0}(0) \equiv 0$. Using the same arguments for obtaining (9.26), the total expected cost until the full backup is$$
\begin{aligned}
c_{F} & +\sum_{j=0}^{\infty} \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \\
& \times\left\{\sum_{i=1}^{j} \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(i)}(x)+\int_{0}^{K}\left[c_{R}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)\right\} \\
= & c_{F}+\sum_{j=1}^{\infty} \int_{0}^{\infty} \bar{D}(t) \mathrm{d} F^{(j)}(t) \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
& +\sum_{j=0}^{\infty} \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \int_{0}^{K}\left[c_{R}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

Therefore, the expected cost rate is, dividing (9.44) by (9.42),

$$
\begin{gathered}
c_{F}+\sum_{j=1}^{\infty} \int_{0}^{\infty} \bar{D}(t) \mathrm{d} F^{(j)}(t) \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
C_{C}(K)=\frac{+\sum_{j=0}^{\infty} \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \int_{0}^{K}\left[c_{R}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{\infty}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \bar{D}(t) \mathrm{d} t}
\end{gathered}
$$

In particular, when $K=0$, i.e., the full backup is done at the first update or at the failure of the database, whichever occurs first, the expected cost in (9.45) is

$$
C_{C}(0)=\frac{c_{F}+c_{R} \int_{0}^{\infty} \bar{F}(t) \mathrm{d} D(t)}{\int_{0}^{\infty} \bar{F}(t) \bar{D}(t) \mathrm{d} t}
$$

where $\bar{F}(t) \equiv 1-F^{(1)}(t)$. When $K=\infty$, i.e., the full backup is done only at the failure of the database, the expected cost in (9.45) is

$$
\begin{aligned}
\frac{C_{C}(\infty)}{\gamma}= & c_{F}+c_{R}+c_{K} \sum_{j=1}^{\infty} \int_{0}^{\infty} \bar{D}(t) \mathrm{d} M_{F}(t) \\
& +\sum_{j=1}^{\infty} \int_{0}^{\infty}\left[2 F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \int_{0}^{\infty} c_{0}(x) \mathrm{d} G^{(j)}(x)
\end{aligned}
$$

where $M_{F}(t) \equiv \sum_{j=1}^{\infty} F^{(j)}(t)$.
Next, suppose that $c_{0}(x)=c_{0} x$ and a database is updated in a Poisson process with rate $\alpha \lambda$, i.e., $F^{(j)}(t)-F^{(j+1)}(t)=\left[(\alpha \lambda t)^{j} / j!\right] \mathrm{e}^{-\alpha \lambda t}(j=0,1,2, \cdots)$, $D(t)=1-\mathrm{e}^{-\beta \lambda t}$, and $\gamma=\beta \lambda$, where $0<\alpha<1$ and $\beta=1-\alpha$. In this case, the expected cost rate in (9.45) is rewritten as

$$
\frac{C_{C}(K)}{\lambda}=\frac{c_{F}-c_{K}+(1+\beta) c_{0} \sum_{j=1}^{\infty} \alpha^{j} \int_{0}^{K} x \mathrm{~d} G^{(j)}(x)}{\sum_{j=0}^{\infty} \alpha^{j} G^{(j)}(K)}+c_{K}+\beta c_{R}
$$

We find an optimum level $K^{*}$ that minimizes $C_{C}(K)$. Differentiating $C_{C}(K)$ with respect to $K$ and setting it equal to zero,$$
\sum_{j=0}^{\infty} \alpha^{j} \int_{0}^{K} G^{(j)}(x) \mathrm{d} x=\frac{c_{F}-c_{K}}{(1+\beta) c_{0}}
$$

whose left-hand side is strictly increasing from 0 to $\infty$. Therefore, there exists an optimum $K^{*}\left(0<K^{*}<\infty\right)$ that satisfies (9.49), and the resulting cost rate is

$$
\frac{C_{C}\left(K^{*}\right)}{\lambda}=(1+\beta) c_{0} K^{*}+c_{K}+\beta c_{R}
$$

Example 9.3. Suppose that $G(x)=1-\mathrm{e}^{-\mu x}$, i.e., $G^{(j)}(x)=\sum_{i=j}^{\infty}\left[(\mu x)^{i} / i!\right] \mathrm{e}^{-\mu x}$ $(j=0,1,2, \cdots)$. Then, an optimum $K^{*}$ is given by a unique solution of the equation

$$
K-\frac{\alpha}{\beta \mu}\left(1-\mathrm{e}^{-\beta \mu K}\right)=\frac{\beta}{1+\beta} \frac{c_{F}-c_{K}}{c_{0}}
$$

Furthermore, an optimum $K^{*}$ is approximately

$$
\widetilde{K}=\frac{1}{1+\beta} \frac{c_{F}-c_{K}}{c_{0}}
$$

and $K^{*}<\widetilde{K}$ that approaches $\widetilde{K}$, as $\beta \rightarrow 0$. In the same values of Example $9.2, \mu K^{*}=6.09, \mu \widetilde{K}=23.53$, and $C_{C}\left(K^{*}\right) /\left(\lambda c_{0} / \mu\right)=48.21 \mathbf{I}$

Furthermore, when the full backup is done at time $T$ before the total files exceed $K$ or the database fails, and its full backup cost is $c_{F}$, the expected cost rate in (9.45) is easily extended as

$$
\begin{gathered}
c_{F}+\sum_{j=1}^{\infty} \int_{0}^{T} \bar{D}(t) \mathrm{d} F^{(j)}(t) \int_{0}^{K}\left[c_{K}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x) \\
C_{C}(K, T)=\frac{+\sum_{j=0}^{\infty} \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \mathrm{d} D(t) \int_{0}^{K}\left[c_{R}+c_{0}(x)\right] \mathrm{d} G^{(j)}(x)}{\sum_{j=0}^{\infty} G^{(j)}(K) \int_{0}^{T}\left[F^{(j)}(t)-F^{(j+1)}(t)\right] \bar{D}(t) \mathrm{d} t}
\end{gathered}
$$

When $c_{0}(x)=c_{0} x$ and $K=\infty$, this corresponds to the cumulative backup model in Section 9.2.# Other Related Stochastic Models 

The cumulative damage model is called the compound renewal process or the compound Poisson process in the theory of stochastic processes when shocks occur in a Poisson process. Examples to these processes of other practical fields are total claims on an insurance company, drifting of stones on river beds, model for Brownian motion, distribution of galaxies, number of customers or amount of materials in a queuing process or storage process $[11,238,239]$ and cancer epidemiology $[240,241]$. For example, we can apply the damage model to the simplest queuing process. A customer arrives at a counter with one server. If the server is free, the customer can be served immediately. Otherwise, if the server is busy with another customer, the customer has to wait for the service and forms a queue [61]. If the arrivals of customers are replaced with shocks and their total times of waiting and service with total damage, this corresponds to the cumulative damage model whose total damage decreases with time (Figure 10.1). In this process, we are mainly interested in the busy period that the server is working for arrival customers.

We introduce briefly typical related models such as the downtime of repairable systems, shot noise, insurance, and stochastic duels.

### 10.1 Other Models

## (1) Downtime Distribution

An operating unit is repaired when it fails, and after the completion of its repair, it begins to operate again. It is assumed that the failure time is a random variable $X_{j}$ having an identical distribution $F(t)$ with finite mean $1 / \lambda$ and the repair time is a random variable variable $W_{j}$ having an identical distribution $G(x)$ with finite mean $1 / \mu$, i.e., $F(t) \equiv \operatorname{Pr}\left\{X_{j} \leq t\right\}$ and $G(x) \equiv$ $\operatorname{Pr}\left\{W_{j} \leq x\right\}(j=1,2, \cdots)$. Then, the total downtime $D(t)$ during the interval $[0, t]$ is, replacing $t$ in (2.3) with $t-x$ (see (2) of Section 2.1.1 in [1]),

Fig. 10.1. Process for the total waiting and service time $Z(t)$ of a queuing model

$$
\operatorname{Pr}\{D(t) \leq x\}=\sum_{j=0}^{\infty} G^{(j)}(x)\left[F^{(j)}(t-x)-F^{(j+1)}(t-x)\right]
$$

where $G^{(j)}(x)\left(F^{(j)}(t)\right)$ is the $j$-fold Stieltjes convolution of $G(x)(F(t))$ with itself. Thus, the distribution that the total downtime exceeds a specified level $K>0$ in time $t$ is

$$
\operatorname{Pr}\{D(t)>K\}=\sum_{j=0}^{\infty}\left[G^{(j)}(K)-G^{(j+1)}(K)\right] F^{(j)}(t-K) \quad \text { for } t>K
$$

The mean time that the total downtime first exceeds $K$ is

$$
\int_{0}^{\infty} \operatorname{Pr}\{D(t) \leq K\} \mathrm{d} t=K+\frac{1}{\lambda}\left[\sum_{j=0}^{\infty} G^{(j)}(K)\right]
$$

In particular, when $F(t)=1-\mathrm{e}^{-\lambda t}$ and $G(x)=1-\mathrm{e}^{-\mu x}$, from Example 2.2 ,

$$
\begin{aligned}
& \operatorname{Pr}\{D(t)>K\} \\
& =1-\mathrm{e}^{-\lambda(t-K)}\left[1+\sqrt{\lambda \mu(t-K)} \int_{0}^{K} \mathrm{e}^{-\mu u} u^{-1 / 2} I_{1}(2 \sqrt{\lambda \mu(t-K) u}) \mathrm{d} u\right] \\
& \text { for } t>K
\end{aligned}
$$$$
\int_{0}^{\infty} \operatorname{Pr}\{D(t) \leq K\} \mathrm{d} t=K+\frac{1}{\lambda}(1+\mu K)
$$

Next, let $Y$ be the first time that one amount of downtime due to unit failures exceeds a fixed time $c>0$, that is called an allowed time. Then, the distribution of a random variable $Y$ and its mean time is, from (1.39) and (1.40) of [1], respectively,

$$
\begin{aligned}
\int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \operatorname{Pr}\{Y \leq t\} & =\frac{F^{*}(s) \mathrm{e}^{-s c} \bar{G}(c)}{1-F^{*}(s) \int_{0}^{c} \mathrm{e}^{-s t} \mathrm{~d} G(t)} \\
E\{Y\} & =\frac{1 / \lambda+\int_{0}^{c} \bar{G}(t) \mathrm{d} t}{\bar{G}(c)}
\end{aligned}
$$

where $\bar{G}(x) \equiv 1-G(x)$, and $F^{*}(s)$ is the Laplace-Stieltjes (LS) transform of $F(t)$. The mean time $E\{Y\}$ is easily given by solving the renewal equation

$$
E\{Y\}=\int_{c}^{\infty}\left(\frac{1}{\lambda}+c\right) \mathrm{d} G(x)+\int_{0}^{c}\left(\frac{1}{\lambda}+x+E\{Y\}\right) \mathrm{d} G(x)
$$

# (2) Shot Noise 

Suppose that a shot noise occurs at time interval $X_{j}$ and its amount is $W_{j}$. The total amount of shot noise is additive and falls into decay with time according to the rate function $h(\cdot)$. Then, the total amount of shot noise at time $t$ is

$$
Z(t) \equiv \sum_{j=1}^{N(t)} W_{j} h\left(t-S_{j}\right)
$$

where $S_{j} \equiv \sum_{i=1}^{j} X_{i}$ and $N(t) \equiv \max _{j}\left\{S_{j} \leq t\right\}$ [242, 243]. The stochastic behaviors of such shot noise were mathematically analyzed [244-248]. This can be also applied to riverflow [249], dams [250-253], and storage models [254256]. If $h(t)=\mathrm{e}^{-\alpha t}$, then this corresponds to the cumulative damage model with annealing in (3) of Section 2.5. Some failure distributions of reliability models were investigated by using the model of shot noise [126, 257].

## (3) Insurance

The cumulative process can be applied to insurance, replacing shock with claim and damage with claim size [258]. In this case, random variables $W_{j}$, $N(t)$, and $Z(t)$ defined in (2.1) represent a claim size, the number of claims up to time $t$, and the total claim amount up to time $t$, respectively. Furthermore, the risk reserve $R(t)$ at time $t$ is given by [259] (Figure 10.2)

$$
R(t)=u+b t-\sum_{j=1}^{N(t)} W_{j}=u+b t-Z(t)
$$

Fig. 10.2. Process for risk reserve $R(t)$ of an insurance model
where $u$ is the initial risk reserve and $b>0$ is the premium rate. The probability of ultimate ruin is given by

$$
\begin{aligned}
\psi(u) & \equiv \operatorname{Pr}\{R(t)<0 \text { for some } t>0\} \\
& =\operatorname{Pr}\{Z(t)-b t>u \text { for some } t>0\}
\end{aligned}
$$

The properties of ruin probability $\psi(u)$ have been studied and summarized [258-261].

# 10.2 Stochastic Duels 

This section introduces a classical model of stochastic duels in which each firing delivers an amount of damage governed by a random variable and it requires a specified threshold level of damage to kill the opponent. The theory of stochastic duels was studied [74, 75, 262-266]. The optimum engagement problem of shooting strategy with incomplete damage information was considered [267].

The stochastic model in which each firing delivers the same amount of damage to the opponent and the kill requires a fixed number of hits was proposed, and the probability that a duelist wins against the opponent was obtained $[263,264]$. In addition, the weapon lifetimes that can be functions of time or number of rounds fired were considered [265], and the total damage resulting from firings was assumed to depend on both time and the number of rounds fired [75]. Recently, multiple damage functions to estimate theprobability that a single weapon detonation destroys a point target were discussed [266].

This section assumes that each firing delivers an amount of damage and it requires a prespecified threshold level of damage to the opponent, where each damage is additive. A duelist loses when the total damage exceeds a threshold level. This corresponds to the cumulative damage model by replacing rounds fired with shocks and threshold level with failure level.

We consider five models of stochastic duels and derive analytically the probabilities of winning the duel with reference to Chapter 2.

# (1) Standard Model 

Consider a stochastic duel with two contestants, say, A and B. Both contestants have unlimited ammunition and unlimited time to kill the opponent. Duelist A (B) begins simultaneously with a weapon and fires at time intervals according to an identical probability distribution $F_{A}(t)$ with finite mean $1 / \lambda_{A}\left(F_{B}(t)\right.$ with finite mean $\left.1 / \lambda_{B}\right)$, respectively, i.e., $F_{A}(t)$ and $F_{B}(t)$ are distribution functions of times between rounds fired. Each firing delivers an amount of damage with a general distribution $G_{A}(x)\left(G_{B}(x)\right)$, and requires a threshold level $K_{A}\left(K_{B}\right)$ of the total damage to kill the opponent. Duelist A (B) wins the duel if he or she delivers $K_{A}\left(K_{B}\right)$ to A (B), respectively. It is assumed that each damage is additive and does not deteriorate.

Let $Z_{A}(t)\left(Z_{B}(t)\right)$ be the total damage up to time $t$ by $\mathrm{A}(\mathrm{B})$. Recalling that duelist A kills B when the total damage delivered by A exceeds a threshold level $K_{A}$, the probability that A kills B up to time $t$ is, from (2.9),

$$
\Phi_{A}(t) \equiv \operatorname{Pr}\left\{Z_{A}(t)>K_{A}\right\}=\sum_{j=0}^{\infty}\left[G_{A}^{(j)}\left(K_{A}\right)-G_{A}^{(j+1)}\left(K_{A}\right)\right] F_{A}^{(j+1)}(t)
$$

Taking the LS transform of (10.8),

$$
\Phi_{A}^{*}(s) \equiv \int_{0}^{\infty} \mathrm{e}^{-s t} \mathrm{~d} \Phi_{A}(t)=\sum_{j=0}^{\infty}\left[G_{A}^{(j)}\left(K_{A}\right)-G_{A}^{(j+1)}\left(K_{A}\right)\right]\left[F_{A}^{*}(s)\right]^{j+1}
$$

where $F_{A}^{*}(s)$ is the LS transform of $F_{A}(t)$. The mean time for A to kill B is

$$
l_{A} \equiv \int_{0}^{\infty} t \mathrm{~d} \Phi_{A}(t)=\frac{1}{\lambda_{A}} \sum_{j=0}^{\infty} G_{A}^{(j)}\left(K_{A}\right)
$$

In the same fashion, the probability $\Phi_{B}(t)$ that B kills A up to time $t$ can be obtained by exchanging from suffix $A$ into $B$.

Therefore, the probability $P_{A}(t)$ that A wins the duel up to time $t$ is

$$
P_{A}(t)=\int_{0}^{t}\left[1-\Phi_{B}(u)\right] \mathrm{d} \Phi_{A}(u)
$$and conversely, the probability $P_{B}(t)$ that B wins the duel up to time $t$ is

$$
P_{B}(t)=\int_{0}^{t}\left[1-\Phi_{A}(u)\right] \mathrm{d} \Phi_{B}(u)
$$

# (2) Imperfect Hit 

It is assumed that A (B) hits the opponent B (A) with probability $p_{A}\left(p_{B}\right)$ and A (B) misses B (A) with $q_{A} \equiv 1-p_{A}\left(q_{B} \equiv 1-p_{B}\right)$, respectively. Then, the probability distribution of time for A to score one hit on B up to time $t$ is, from Example 1.1,

$$
F_{1}(t)=\left[1+q_{A} F_{A}(t)+q_{A} F_{A}(t) * q_{A} F_{A}(t)+\cdots\right] * p_{A} F_{A}(t)
$$

Thus, replacing $F_{A}(t)$ in (10.8) with $F_{1}(t)$, we have $\Phi_{A}(t)$. The LS transform is

$$
\Phi_{A}^{*}(s)=\sum_{j=0}^{\infty}\left[G_{A}^{(j)}\left(K_{A}\right)-G_{A}^{(j+1)}\left(K_{A}\right)\right]\left[\frac{p_{A} F_{A}^{*}(s)}{1-q_{A} F_{A}^{*}(s)}\right]^{j+1}
$$

and the mean time for A to kill B is

$$
l_{A}=\frac{1}{p_{A} \lambda_{A}} \sum_{j=0}^{\infty} G_{A}^{(j)}\left(K_{A}\right)
$$

The other quantities can be obtained in a similar fashion.

## (3) Independent Damage

It is assumed that the amount of damage is not additive and the amount is nullified immediately when it is less than $K_{A}\left(K_{B}\right)$. The other assumptions are the same as those of case (1) except that the total damage is additive. Then, the LS transform of the probability that A kills B up to time $t$ is, from Section 2.2,

$$
\begin{aligned}
\Phi_{A}^{*}(s) & =\sum_{j=0}^{\infty}\left\{\left[G_{A}\left(K_{A}\right)\right]^{j}-\left[G_{A}\left(K_{A}\right)\right]^{j+1}\right\}\left[F_{A}^{*}(s)\right]^{j+1} \\
& =\frac{\left[1-G_{A}\left(K_{A}\right)\right] F_{A}^{*}(s)}{1-G_{A}\left(K_{A}\right) F_{A}^{*}(s)}
\end{aligned}
$$

and the mean time for A to kill B is

$$
l_{A}=\frac{1}{\lambda_{A}\left[1-G_{A}\left(K_{A}\right)\right]}
$$# (4) Random Threshold Level 

It is assumed that a threshold level $K_{A}\left(K_{B}\right)$ is a random variable with a general distribution $L_{A}(x)\left(L_{B}(x)\right)$, respectively. Then, from (2) in Section 2.5, for case (1),

$$
\Phi_{A}^{*}(s)=\sum_{j=0}^{\infty}\left[F_{A}^{*}(s)\right]^{j+1} \int_{0}^{\infty}\left[G_{A}^{(j)}(x)-G_{A}^{(j+1)}(x)\right] \mathrm{d} L_{A}(x)
$$

for case (2),

$$
\Phi_{A}^{*}(s)=\sum_{j=0}^{\infty}\left[\frac{p_{A} F_{A}^{*}(s)}{1-q_{A} F_{A}^{*}(s)}\right]^{j+1} \int_{0}^{\infty}\left[G_{A}^{(j)}(x)-G_{A}^{(j+1)}(x)\right] \mathrm{d} L_{A}(x)
$$

and for case (3),

$$
\Phi_{A}^{*}(s)=\sum_{j=0}^{\infty}\left[F_{A}^{*}(s)\right]^{j+1} \int_{0}^{\infty}\left\{\left[G_{A}(x)\right]^{j}-\left[G_{A}(x)\right]^{j+1}\right\} \mathrm{d} L_{A}(x)
$$

The other quantities can be obtained in a similar fashion.

## (5) Lifetimes of Weapons

Consider the lifetimes of A's (B's) weapon distributed with $R_{A}(t)\left(R_{B}(t)\right)$, respectively. It is assumed that the failed weapon of A (B) remains in the duel until A (B) is killed or B's (A's) weapon fails. Then, the probability that A wins in the duel up to time $t$ is

$$
P_{A}(t)=\int_{0}^{t}\left[1-R_{A}(u)\right]\left\{1-\int_{0}^{u}\left[1-R_{B}(v)\right] \mathrm{d} \Phi_{B}(v)\right\} \mathrm{d} \Phi_{A}(u)
$$

and the tie probability is

$$
P_{A B}(t)=\int_{0}^{t}\left[1-\Phi_{A}(u)\right] \mathrm{d} R_{A}(u) \int_{0}^{t}\left[1-\Phi_{B}(u)\right] \mathrm{d} R_{B}(u)
$$

that represents the probability that both A and B cannot kill the opponent because of failures of the weapons up to time $t$. Note that $P_{A}(\infty)+P_{B}(\infty)+$ $P_{A B}(\infty)=1$.

Example 10.1. It is assumed that $G_{A}(x) \equiv 0$ for $x<1$ and 1 for $x \geq 1$ and $K_{A}$ is a positive integer. Then, from (10.13),

$$
\Phi_{A}^{*}(s)=\left[\frac{p_{A} F_{A}^{*}(s)}{1-q_{A} F_{A}^{*}(s)}\right]^{K_{A}}
$$

Furthermore, $L_{A}(x)$ is a discrete distribution, i.e.,$$
\operatorname{Pr}\left\{K_{A}=j\right\}=\alpha_{j} \quad(j=1,2, \cdots)
$$

where $\sum_{j=1}^{\infty} \alpha_{j}=1$. Then, from (10.18),

$$
\Phi_{A}^{*}(s)=\sum_{j=1}^{\infty} \alpha_{j}\left[\frac{p_{A} F_{A}^{*}(s)}{1-q_{A} F_{A}^{*}(s)}\right]^{j}
$$

Example 10.2. Suppose in case (4) that all random variables are exponential, i.e., $F(t)=1-\mathrm{e}^{-\lambda t}, G(x)=1-\mathrm{e}^{-\mu x}$, and $L(x)=1-\mathrm{e}^{-\alpha x}$, where the suffixes of the three parameters are omitted. Then, from (10.18),

$$
\Phi_{A}^{*}(s)=\frac{\alpha \lambda p}{(\alpha+\mu) s+\alpha \lambda p}
$$

By inversion,

$$
\Phi_{A}(t)=1-\mathrm{e}^{-\theta_{A} t}
$$

where $\theta_{A} \equiv \alpha \lambda p /(\alpha+\mu)$. For duelist B,

$$
\Phi_{B}(t)=1-\mathrm{e}^{-\theta_{B} t}
$$

Thus, from (10.11),

$$
\begin{aligned}
& P_{A}(t)=\frac{\theta_{A}}{\theta_{A}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\theta_{A}+\theta_{B}\right) t}\right] \\
& P_{B}(t)=\frac{\theta_{B}}{\theta_{A}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\theta_{A}+\theta_{B}\right) t}\right]
\end{aligned}
$$

Furthermore, when the lifetimes of the weapons are assumed to be $R_{A}(t)=$ $1-\mathrm{e}^{-\gamma_{A} t}$ and $R_{B}(t)=1-\mathrm{e}^{-\gamma_{B}(t)}$, from case (5),

$$
\begin{aligned}
P_{A}(t)= & \frac{\theta_{A}}{\gamma_{B}+\theta_{B}}\left\{\frac{\gamma_{B}}{\gamma_{A}+\theta_{A}}\left[1-\mathrm{e}^{-\left(\gamma_{A}+\theta_{A}\right) t}\right]\right. \\
& \left.+\frac{\theta_{B}}{\gamma_{A}+\theta_{A}+\gamma_{B}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\gamma_{A}+\theta_{A}+\gamma_{B}+\theta_{B}\right) t}\right]\right\} \\
P_{B}(t)= & \frac{\theta_{B}}{\gamma_{A}+\theta_{A}}\left\{\frac{\gamma_{A}}{\gamma_{B}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\gamma_{B}+\theta_{B}\right) t}\right]\right. \\
& \left.+\frac{\theta_{A}}{\gamma_{A}+\theta_{A}+\gamma_{B}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\gamma_{A}+\theta_{A}+\gamma_{B}+\theta_{B}\right) t}\right]\right\} \\
P_{A B}(t)= & \frac{\gamma_{A}}{\gamma_{A}+\theta_{A}} \frac{\gamma_{B}}{\gamma_{B}+\theta_{B}}\left[1-\mathrm{e}^{-\left(\gamma_{A}+\theta_{A}\right) t}\right]\left[1-\mathrm{e}^{-\left(\gamma_{B}+\theta_{B}\right) t}\right]
\end{aligned}
$$

where it is clearly seen that $P_{A}(\infty)+P_{B}(\infty)+P_{A B}(\infty)=1$.# References 

1. Nakagawa T (2005) Maintenance Theory of Reliability. Springer, London.
2. Bogdanoff JL, Kozin F (1985) Probabilistic Models of Cumulative Damage. John Wiley \& Sons, New York.
3. Hudson WR, Haas R, Uddin W (1997) Infrastructure Management. McGrawHill, New York.
4. Hisano K (2000) Preventive maintenance and residual life evaluation technique for power plant-Preventive maintenance. Thermal Nucl Power 51:491-517.
5. Hisano K (2001) Preventive maintenance and residual life evaluation technique for power plant-Review of future advances in preventive maintenance technology. Thermal Nucl Power 52:363-370.
6. Durham SD, Padgett WJ(1990) Estimation for a probabilistic stress-strength model. IEEE Trans Reliab 39:199-203.
7. Miner MA (1945) Cumulative damage in fatigue. J Appl Mech 12:A159-A164.
8. Birnbaum Z, Saunders SC (1968) A probabilistic interpretation of Miner's rule. SIAM J Appl Math 16:637-652.
9. Stallmeyer JE, Walker WH (1968) Cumulative damage theories and application. J Struct Div ASCE 94:2739-2750.
10. Kuroishi T, Minami Y, Kobayashi Y, Yokoyama T, Hasegawa Y, Kageyama O, Minatomoto M (2003) Power systems:A portal to customer services for electric power generation. Mitsubishi Heavy Industries, Ltd. Tech Rev 40:1-9.
11. Cox DR (1962) Renewal Theory. Methuen, London.
12. Akama M, Ishizuka H (1995) Reliability analysis of Shinkansen vehicle axle using probabilistic fracture mechanics. JSME Inter J Ser A 38:378-383.
13. Gertsbakh I, Kordonsky Kh (1969) Models of Failure. Springer, Berlin.
14. Satow T, Teramoto K, Nakagawa T (2000) Optimal replacement policy for a cumulative damage model with time deterioration. Math Comput Model 31:313-319.
15. Durham SD, Padgett WJ (1997) Cumulative damage models for system failure with application to carbon fibers and composites. Technometrics 39:34-44.
16. Padgett WJ (1998) A muliplicative damage model for strength of fibrous composite materials. IEEE Trans Reliab 47:46-52.
17. Ihara C, Tsurui A (1977) Fatigue of metals as stochastic phenomena. J Eng Mater Tech 99:26-28.18. Sobczyk K, Trebicki J (1989) Modelling of random fatigue by cumulative jump processes. Eng Fracture Mech 34:477-493.
19. Scarf PA, Wang W, Laycock PJ (1996) A stochastic model of crack growth under periodic inspections. Reliab Eng Syst Saf 51:331-339.
20. Hopp WJ, Kuo YL (1998) An optimal structured policy for maintenance of partially observable aircraft engine components. Nav Res Logist 45:335-352.
21. Lukić M, Cremona C (2001) Probabilistic optimization of welded joints maintenance versus fatigue and fracture. Reliab Eng Syst Saf 72:253-264.
22. Garbatov Y, Soares CG (2001) Cost and reliability based strategies for fatigue maintenance planning of floating structures. Reliab Eng Syst Saf 73:293-301.
23. Petryna YS, Pfanner D, Stangenberg F, Krätzig WB (2002) Reliability of reinforced concrete structures under fatigue. Reliab Eng Syst Saf 77:253-261.
24. Campean IF, Rosala GF, Grove DM, Henshall E (2005) Life modelling of a plastic automotive component. In:Proc Ann Reliab Maintainability Symp:319325 .
25. Sobczyk K (1987) Stochastic models for fatigue damage of materials. Adv Appl Probab 19:652-673.
26. Sobczyk K and Spencer Jr BF (1992) Random Fatigue:From Data to Theory. Academic, New York.
27. Dasgupta A, Pecht M (1991) Material failure mechanisms and damage models. IEEE Trans Reliab 40:531-536.
28. Smith WL (1955) Regenerative stochastic processes. Proc Roy Soc London A 232:6-31.
29. Smith WL (1958) Renewal theory and its ramifications. J Roy Statist Soc B 20:243-302.
30. Mercer A (1961) On wear-dependent renewal processes. J Roy Statist Soc B 23:368-376.
31. Morey RC (1966) Some stochastic properties of a compound-renewal damage model. Oper Res 14:902-908.
32. Murthy VK, Lients BP (1968) On cumulative damage and reliability of components. Document ARL68-0180, Aerospace Res Lab, Wright-Patterson Air Force Base, Ohio.
33. Esary JD, Marshall AW, Proschan F (1973) Shock models and wear processes. Ann Probab 1:627-649.
34. Gaver Jr DP (1963) Randam hazard in reliability problems. Technometrics $5: 211-226$.
35. Antelman G, Savage IR (1965) Characteristic functions of stochastic integrals and reliability theory. Nav Res Logist Q 12:199-222.
36. Birnbaum ZW, Saunders SC (1969) A new family of life distributions. J Appl Probab 6:319-327.
37. Reynolds DS, Savage IR (1971) Random wear models in reliability theory. Adv Appl Probab 3:229-248.
38. Colombo AG, Reina G, Volta G (1974) Extreme value characteristics of distributions of cumulative processes. IEEE Trans Reliab R-23:179-186.
39. Aven T, Jensen U (1999) Stochastic Models in Reliability. Springer, New York.
40. Nakagawa T, Osaki S (1974) Some aspects of damage model. Microelectron Reliab 13:253-257.
41. Rausand M, HØyland A (2004) System Reliability Theory. John Wiley \& Sons, Hoboken NJ.42. Taylor HM (1975) Optimal replacement under additive damage and other failure models. Nav Res Logist Q 22:1-18.
43. Feldman RM (1976) Optimal replacement with semi-Markov shock models. J Appl Probab 13:108-117.
44. Feldman RM (1977) Optimal replacement with semi-Markov shock models using discounted costs. Math Oper Res 2:78-90.
45. Feldman RM (1977) Optimal replacement for systems governed by Markov additive shock processes. Ann Probab 5:413-429.
46. Zuckerman D (1977) Replacement models under additive damage. Nav Res Logist Q 24:549-558.
47. Zuckerman D (1978) Optimal replacement policy for the case where the damage process is a one-sided Lévy process. Stoch Process Appl 7:141-151.
48. Zuckerman D (1978) Optimal stopping in a semi-Markov shock model. J Appl Probab 15:629-634.
49. Zuckerman D (1980) Optimal replacement under additive damage and selfrestoration. RAIRO Oper Res 14:115-127.
50. Zuckerman D (1980) A note on the optimal replacement time of damaged devices. Nav Res Logist Q 27:521-524.
51. Nakagawa T (1976) On a replacement problem of a cumulative damage model. Oper Res Q 27:895-900.
52. Nakagawa T (1979) Replacement problem of a parallel system in random environment. J Appl Probab 16:203-205.
53. Nakagawa T (1979) Further results of replacement problem of a parallel system in random environment. J Appl Probab 16:923-926.
54. Nakagawa T, Murthy DNP (1993) Optimal replacement policies for a two-unit system with failure interactions. RAIRO Oper Res 27:427-438.
55. Nakagawa T, Kijima M (1989) Replacement policies for a cumulative damage model with minimal repair at failure. IEEE Trans Reliab 38:581-584.
56. Nakagawa T (1986) Modified discrete preventive maintenance policies. Nav Res Logist Q 33:703-715.
57. Kijima M, Nakagawa T (1992) Replacement policies of a shock model with imperfect preventive maintenance. Eur J Oper Res 57:100-110.
58. Satow T, Yasui K, Nakagawa T (1996) Optimal garbage collection policies for a database in a computer system:RAIRO Oper Res 30:359-372.
59. Qian CH, Nakamura S, Nakagawa T, (1999) Cumulative damage model with two kinds of shocks and its application to the backup policy. J Oper Res Soc Jpn 42:501-511.
60. Ross SM (1983) Stochastic Processes. John Wiley \& Sons, New York.
61. Osaki S (1992) Applied Stochastic System Modeling. Springer, Berlin.
62. Karlin S, Taylor HM (1975) A First Course in Stochastic Processes. Academic, New York.
63. Çinlar E (1975) Introduction to Stochastic Processes. Prentice-Hall, Englewood Cliffs, NJ.
64. Trindade D, Nathan S (2005) Simple plots for monitoring the field reliability of repairable systems. In:Proc Ann Reliab Maintainability Symp:539-544.
65. Barlow RE, Proschan F (1965) Mathematical Theory of Reliability. John Wiley \& Sons, New York.
66. Nakagawa T, Kowada M (1983) Analysis of a system with minimal repair and its application to replacement policy. Eur J Oper Res 12:176-182.67. Barbour AD, Chryssaphinou O (2001) Compound Poisson approximation:A user's guide. Ann Appl Probab 11:964-1002.
68. Abdel-Hameed M, Proschan F (1975) Shock models with underlying birth process. J Appl Probab 12:18-28.
69. Klefsjö B (1981) Survival under the pure birth shock model. J Appl Probab 18:554-560.
70. Abdel-Hameed M (1984) Life distribution properties of devices subject to a Lévy wear process. Math Oper Res 9:606-614.
71. Khoshnevisan D, Xiao Y (2002) Level sets of additive Lévy processes. Ann Probab 30:62-100.
72. Block HW, Savits TH (1978) Shock models with NBUE survival. J Appl Probab 15:621-628.
73. Pellerey F (1994) Shock models with underlying counting process. J Appl Probab 31:156-166.
74. Ancker Jr CJ (1967) The status of developments in the theory of stochastic duels-II. Oper Res 15:388-406.
75. Nagabhushanam A, Jain GC (1972) Stochastic duels with damage. Oper Res 20:350-356.
76. Rāde L (1976) Reliability systems in random environment. J Appl Probab 13:407-410.
77. Hokstad P (1988) A shock model for comnon-cause failures. Reliab Eng Syst Saf 23:127-145.
78. Vaurio JK (1994) The theory and quantification of common cause shock events for redundant standby systems. Reliab Eng Syst Saf 43:289-305.
79. Vaurio JK (1995) The probability modeling of external common cause failure shocks in redundant systems. Reliab Eng Syst Saf 50:97-107.
80. Kvam PH, Martz HF (1995) Bayesian inference in a discrete shock model using confounded common cause data. Reliab Eng Syst Saf 48:19-25.
81. Abdel-Hameed M (1984) Life distribution properties of devices subject to a pure jump damage process. J Appl Probab 21:816-825.
82. Grandell J (1976) Doubly Stochastic Poisson Process. Lecture Notes in Mathematics 529. Springer, New York.
83. Takács L (1960) Stochastic Processes. John Wiley \& Sons, New York.
84. Gut A (1990) Cumulative shock models. Adv Appl Probab 22:504-507.
85. Glynn PW, Whitt W (1993) Limit theorems for cumulative processes. Stoch Process Appl 47:299-314.
86. Roginsky AL (1994) A central limit theorem for cumulative processes. Adv Appl Probab 26:104-121.
87. Finkelstein MS, Zarudnij VI (2001) A shock process with a non-cumulative damage. Reliab Eng Syst Saf 71:103-107.
88. Barlow RE, Proschan F (1975) Statistical Theory of Reliability and Life Testing. Holt, Rinehart \& Winston, New York.
89. Abdel-Hameed M and Proschan F (1973) Nonstationary shock models. Stoch Process Appl 1:383-404.
90. Shaked M (1984) Wear and damage processes from shock models in reliability theory. In:Abdel-Hameed M, Çinlar E, Quinn J (eds) Reliability Theory and Models. Academic, Orlando.
91. Severina TI (1975) A model of accumulation of damage. Eng Cybern 13:74-76.
92. Ramanarayanan R (1976) Cumulative damage processes and alertness of the worker. IEEE Trans Reliab R-25:281-283.93. Gottlieb G (1980) Failure distributions of shock models. J Appl Probab 17:745752 .
94. Thall PF (1981) Cluster shock models. J Appl Probab 18:104-111.
95. Klefsjö B (1981) HNBUE survival under some shock models. Scand J Stat 8:39-47.
96. Ross SM (1981) Generalized Poisson shock models. Ann Probab 9:896-898.
97. Neuts MF, Bhallacharjee MC (1981) Shock models with phase-type survival and shock resistance. Nav Res Logist Quart 28:213-219.
98. Ghosh M, Ebrahimi N (1982) Shock models leading to increasing failure rate and decreasing mean residual life survival. J Appl Probab 19:158-166.
99. Ohi F, Nishida T (1983) Another proof of IFRA property of S.M. Ross' generalized Poisson shock models. Math Jpn 28:117-123.
100. Ebrahimi N (1985) A stress-strength system. J Appl Probab 22:467-472.
101. Yamada K (1989) Limit theorems for jump shock models. J Appl Probab 27:793-806.
102. Singh H, Jain K (1989) Preservation of some partial ordering under Poisson shock models. Adv Appl Probab 21:713-716.
103. Kochar SC (1990) On preservation of some partial ordering under shock models. Adv Appl Probab 22:508-509.
104. Manoharan M, Singh H, Misra N (1992) Preservation of phase-type distributions under Poisson shock models. Adv Appl Probab 24:223-225.
105. Pellerey F (1993) Partial orderings under cumulative damage shock models. Adv Appl Probab 25:939-946.
106. Fagiuoli E, Pellerey F (1994) Preservation of certain classes of life distributions under Poisson shock models. J Appl Probab 31:458-465.
107. Ebrahimi N (1999) Stochastic properties of a cumulative damage threshold crossing model. J Appl Probab 36:720-732.
108. Shanthikumar JG, Sumita U (1983) General shock models associated with correlated renewal sequences. J Appl Probab 20:600-614.
109. Sumita U, Shanthikumar JG (1985) A class of correlated shock models. Adv Appl Probab 17:347-366.
110. Anderson KK (1987) Limit theorems for general shock models with infinite mean intershock times. J Appl Probab 24:449-456.
111. Anderson KK (1988) A note on cumulative shock models. J Appl Probab $25: 220-223$.
112. Pérez-Ocón R, Gámiz-Pérez ML (1995) On the HNBUE property in a class of correlated cumulative shock models. Adv Appl Probab 27:1186-1188.
113. Igaki N, Sumita U, Kowada M (1995) Analysis of Markov renewal shock models. J Appl Probab 32:821-831.
114. Li G, Luo J (2005) Shock model in Markovian environment. Nav Res Logist $52: 253-260$.
115. Marchall AW, Shaked M (1979) Mulitivariate shock models for distributions with increasing hazard rate average. Ann Probab 7:343-358.
116. Ohi F, Nishida T (1979) Bivariate shock models:NBU and NBUE properties, and positively quadrant dependency. J Oper Res Soc Jpn 22:266-273.
117. Savits TH, Shaked M (1981) Shock models and the MIFRA property. Stoch Process Appl 11:273-283.
118. Griffith WS (1982) Remarks on univariate shock model with some bivariate generation. Nav Res Logist Q 29:63-74.119. Shaked M, Shanthikumar JG (1987) IFRA properties of some Markov jump processes with general state space. Math Oper Res 12:562-568.
120. Savits TH (1988) Some multivariate distributions derived from a non-fatal shock model. J Appl Probab 25:383-390.
121. Wong T (1997) Preservation of multivariate stochastic orders under multivariate Poisson shock models. J Appl Probab 34:1009-1020.
122. Mallor F, Omey E (2001) Shocks, runs and random sums. J Appl Probab $38: 438-448$.
123. Belzunce F, Lillo RE, Pellerey F, Shaked M (2002) Preservation of association in multivariate shock and claim models. Oper Res Lett 30:223-230.
124. Gaudoin O, Soler JL (1997) Failure rate behavior of components subjected to random stresses. Reliab Eng Syst Saf 58:19-30.
125. Abdel-Hameed M (1975) A gamma wear process. IEEE Trans Reliab R-24:152153 .
126. Lemoine AJ, Wenocur ML(1985) On failure modeling. Nav Res Logist Q $32: 497-508$.
127. Desmond A (1985) Stochastic models of failure in random environments. Can J Stat 13:171-183.
128. Kececioglu DB, Jiang MX (1998) A unified approach to random-fatigue reliability quantification under random loading. In:Proc Ann Reliab Maintainability Symp:308-313.
129. Owen WJ, Padgett WJ (2003) Accelerated test models with the BirnbaumSaunders distribution. In:Pham H (ed) Handbook of Reliability Engineering. Springer, London:429-439.
130. Park C, Padgett WJ (2005) New cumulative damage models for failure using stochastic processes as initial damage. IEEE Trans Reliab 54:530-540.
131. Satow T, Yasui K, Nakagawa T (1996) Optimal garbage collection policies for a database with random threshold level. Electron Commun Japan 79:31-40.
132. Nakagawa T (1975) On cumulative damage with annealing. IEEE Trans Reliab R-24:90-91.
133. Nakagawa T (1976) On a cumulative damage model with $N$ different components. IEEE Trans Reliab R-25:112-114.
134. Satow T, Nakagawa T (1997) Three replacement models with two kinds of damage. Microelectron Reliab 37:909-913.
135. Satow T, Nakagawa T (1997) Replacement policies for a shock model with two kinds of damage. In:Osaki S (ed) Stochastic Modelling in Innovative Manufacturing, Springer Lecture Notes in Economics and Mathematical Systems $445: 188-195$.
136. Qian CH, Ito K, Nakagawa T (2005) Optimal preventive maintenance policies for a shock model with given damage level. J Qual Maint Eng 11:216-227.
137. Gottlieb G, Yechiali U (1980) Damage models for multi-component systems. Eur J Oper Res 5:193-197.
138. Bergman B (1978) Optimal replacement under a general failure model. Adv Appl Probab 10:431-451.
139. Abdel-Hameed M, Shimi IN (1978) Optimal replacement of damaged devices. J Appl Probab 15:153-161.
140. Yamada K (1980) Explicit formula of optimal replacement under additive shock processes. Stoch Process Appl 9:193-208.
141. Chikte SD, Deshmukh SD (1981) Preventive maintenance and replacement under additive damage. Nav Res Logist Q 28:33-46.142. Gottlieb G (1982) Optimal replacement for shock models with general failure rate. Oper Res 30:82-92.
143. Waldmann KH (1983) Optimal replacement under additive damage in randomly varying environments. Nav Res Logist Q 30:377-386.
144. Gottlieb G, Levikson B (1984) Optimal replacement for self-repairing shock models with general failure rate. J Appl Probab 21:108-119.
145. Mizuno N (1986) Generalized mathematical programming for optimal replacement in a semi-Markov shock model. Oper Res 34:790-795.
146. Aven T, Gaarder S (1987) Optimal replacement in a shock model:Discrete time. J Appl Probab 24:281-287.
147. Abdel-Hameed M, Nakhi Y (1991) Optimal replacement and maintenance of systems subject to semi-Markov damage. Stoch Process Appl 37:141-160.
148. Abdel-Hameed M (1999) Applications of semi-Markov processes in reliability and maintenance. In:Jenssen J, Limnios N (eds) Semi-Markov Models and Applications. Kluwer Academic, The Netherlands:337-348.
149. Posner MJM, Zuckerman D (1984) A replacement model for an additive damage model with restoration. Oper Res Lett 3:141-148.
150. Posner MJM, Zuckerman D (1986) Semi-Markov shock models with additive damage. Adv Appl Probab 18:772-790.
151. Perry D, Posner MJM (1991) Determining the control limit policy in a replacement model with restoration. Oper Res Lett 10:335-341.
152. Perry D (2000) Control limit policies in a replacement model with additive phase-type distributed damage and linear restoration. Oper Res Lett 27:127134 .
153. Wortman MA, Klutke GA, Ayhan H (1994) A maintenance strategy for systems subjected to deterioration governed by random shocks. IEEE Trans Reliab $43: 439-445$.
154. Feng W, Adachi K, Kowada M (1994) Dynamically optimal replacement policy for a shock model in a Markov random environment. J Oper Res Soc Jpn $37: 255-270$.
155. Aven T (1996) Condition based replacement policies-A counting process approach. Reliab Eng Sys Saf 51:275-281.
156. Sheu SH, Griffith WS (1996) Optimal number of minimal repairs before replacement of a system subject to shocks. Nav Res Logist 43:319-333.
157. Sheu SH (1997) Extend block replacement policy of a system subject to shocks. IEEE Trans Reliab 46:375-382.
158. Sheu SH (1998) A generalized age and block replacement of a system subject to shocks. Eur J Oper Res 108:345-362.
159. Sheu SH, Griffith WS (2002) Extend block replacement policy with shock models and used items. Eur J Oper Res 140:50-60.
160. Sheu SH, Chien YH (2004) Optimal age-replacement policy of a system subject to shocks with random lead-time. Eur J Oper Res 159:132-144.
161. Wang GJ, Zhang YL (2005) A shock model with two-type failures and optimal replacement policy. Int J Syst Sci 36:209-214.
162. Feldman RM, Joo NY (1985) A state-age dependent policy for a shock process. Stoch Models 1:53-76.
163. Lam CT, Yeh RH (1994) Optimal replacement policies for multi-state deteriorating systems. Nav Res Logist 41:303-315.
164. Klutke GA, Yang YJ (2002) The availability of inspected systems subject to shocks and graceful degradation. IEEE Trans Reliab 51:371-374.165. Li WJ, Pham H (2005) Reliability modeling of multi-state degraded systems with multi-competing failures and random shocks. IEEE Trans Reliab 54:297303 .
166. Li Z, Chan LY, Yuan Z (1999) Failure time distribution under a $\delta$-shock model and its application economic design of systems. Inter J Reliab Qual Saf Eng 6:237-247.
167. Tang YY, Lam Y (2006) A $\delta$-shock maintenance model for a deteriorating system. Eur J Oper Res 168:541-556.
168. Qian CH, Nakamura S, Nakagawa T (2000) Replacement policies for cumulative damage model with maintenance cost. Scientiae Mathematicae 3:117-126.
169. Muth E (1977) An optimal decision rule for repair vs. replacement. IEEE Trans Reliab 26:179-181.
170. Barbera F, Schneider H, Watson E (1999) A condition based maintenance model for a two-unit series system. Eur J Oper Res 116:281-290.
171. Murthy DNP, Nguyen DG (1985) Study of two-component system with failure interaction. Nav Res Logist Q 32:239-248.
172. Pham H, Suprasad A, Misra B (1996) Reliability and MTTF prediction of $k$-out-of- $n$ complex systems with components subjected to multiple stages of degradation. Int J Syst Sci 27:995-1000.
173. Skoulakis G (2000) A general shock model for a reliability system. J Appl Probab 37:925-935.
174. Juang MG, Sheu SH (2003) Graphical approach to replacement policy of a $K$-out-of- $N$ system subject to shocks. Int J Reliab Qual Saf Eng 10:55-68.
175. Chryssaphinou O, Papastavridis S (1990) Reliability of a consecuitive- $k$-out-of- $n$ system in a random environment. J Appl Probab 27:452-458.
176. Petakos K, Tsapelas T (1997) Reliability analysis for systems in a random environment. J Appl Probab 34:1021-1031.
177. Shaked M, Shantikumar JG (1990) Reliability and maintainability. In:Heyman DP, Sobel MJ(eds) Stochastic Models. North Holland, Amsterdam.
178. Murthy DNP, Casey RT (1987) Optimal policy for a two component system with shock type failure interaction. In:Proc 8th Nat Conf Ausl Oper Res Soc, Melbourne, 161-172.
179. Murthy DNP, Nguyen DG (1985) Study of a multi-component system with failure interaction. Eur J Oper Res 21:330-338.
180. Murthy DNP, Wilson RJ (1994) Parameter estimation in multi-component with failure interaction. Stoch Models Data Analysis 10:47-60.
181. Jhang JP, Sheu SH (2000) Optimal age and block replacement policies for a multi-component system with failure interaction. Inter J Syst Sci 31:593-603.
182. Scarf PA, Deara M (2003) Block replacement policies for a two-component system with failure dependence. Nav Res Logist 50:70-87.
183. Zequeria RI, Bérenguer C (2004) Maintenance cost analysis of a two-component parallel system with failure interaction. In:Proc Ann Reliab Maintainability Symp:220-225.
184. Zequeira RI, Bérenguer C (2005) On the inspection policy of a two-component parallel system with failure interaction. Reliab Eng Syst Saf 88:99-107.
185. Satow T, Osaki S (2003) Optimal replacement policies for a two-unit system with shock damage interaction. Comput Math Appl 46:1129-1138.
186. Boland PJ, Proschan F (1983) Optimal replacement of a system subject to shocks. Oper Res 31:697-704.187. Abdel-Hameed M (1986) Optimum replacement of a system subject to shocks. J Appl Probab 23:107-114.
188. Puri PS, Singh H (1986) Optimum replacement of a system subject to shocks:A mathematical lemma. Oper Res 34:782-789.
189. Rangan A, Grace RE (1988) A non-Markov model for the optimum replacement of self-replacement systems subject to shocks. J Appl Probab 25:375-382.
190. Nakagawa T (1987) Modified, discrete replacement models. IEEE Trans Reliab $36: 243-245$.
191. Satow T, Nakagawa T (1997) Optimal replacement policy for a cumulative damage model with deteriorated inspection. Int J Reliab Qual Saf Eng 4:387393.
192. Park KS (1988) Optimal continuous-wear limit replacement under periodic inspections. IEEE Trans Reliab 37:97-102.
193. Park KS (1988) Optimal wear-limit replacement with wear-dependent failures. IEEE Trans Reliab 37:293-294.
194. Grall A, Bérenguer C, Dieulle L (2002) A condition-based maintenance policy for stochastically deterioration systems. Reliab Eng Syst Saf 76:167-180.
195. Dieulle L, Bérenguer C, Grall A, Roussignol M (2003) Sequential conditionbased maintenance scheduling for a deterioration system. Eur J Oper Res $150: 451-461$.
196. Castanier B, Grall A, Bérenguer C (2005) A condition-based maintenance policy with non-periodic inspections for a two-unit series system. Reliab Eng Syst Saf 87:109-120.
197. Nakagawa T, Yasui K (1991) Periodic-replacement models with threshold levels. IEEE Trans Reliab 40:395-397.
198. Ito K, Nakagawa T (1995) An optimal inspection policy for a storage system with three types of hazard rate functions. J Oper Res Soc Jpn 38:423-341.
199. Martines EC (1984) Storage reliability with periodic test. In:Proc Ann Reliab Maintainability Symp:181-185.
200. Gertsbakh I (2000) Reliability Theory with Applications to Preventive Maintenance. Springer, Berlin.
201. Dohi T, Kaio N, Osaki S (2003) Preventive maintenance models:Replacement, repair, ordering, and inspection. In:Pham H (ed) Handbook of Reliability Engineering. Springer, London:349-366.
202. Scarf PA (1997) On the application of mathematical models in maintenance. Eur J Oper Res 99:493-506.
203. Murthy DNP, Jack N (2003) Warranty and maintenance. In:Pham H (ed) Handbook of Reliability Engineering. Springer, London:305-316.
204. Adams PJ (1982) The quality of aircraft maintenance. Qual Assurance 8:87-95.
205. Rosenfield D (1976) Markovian deterioration with certain information. Oper Res 24:141-155.
206. Tijims H, Van der Duyn Schouten FA (1984) A Markov decision algorithm for optimal inspections and revisions in a maintenance system with partial information. Eur J Oper Res 21:245-253.
207. Hontelez JAM, Burger HH, Wijnmalen DJD (1996) Optimal condition-based maintenance policies for deteriorating systems with partial information. Reliab Eng Syst Saf 51:267-274.
208. Chen D, Trivedi KS (2005) Optimization for condition-based maintenance with semi-Markov decision process. Reliab Eng Syst Saf 90:25-29.209. Saasouch B, Dieulle L, Grall A (2004) Maintenance policy of a system with several modes of deterioration:10th ISSAT Inter Conf Reliab Qual Design:211215 .
210. Liao H, Chan LY, Elsayed EA (2004) Maintenance of continuously monitored degrading systems:10th ISSAT Inter Conf Reliab Qual Design:216-220.
211. Elsayed EA, Zhang Z (2006) Optimum threshold level of degraded structures based on sensors data. In: 12 th ISSAT Inter Conf Reliab Qual Design:187-191.
212. Nakagawa T (1979) Optimal policies when preventive maintenance is imperfect. IEEE Trans Reliab R-28:331-332.
213. Nakagawa T (1979) Imperfect preventive-maintenance. IEEE Trans Reliab R28:402.
214. Nakagawa T, Yasui K (1987) Optimum policies for a system with imperfect maintenance. IEEE Trans Reliab R-36:631-633.
215. Nakagawa T (2000) Imperfect preventive maintenance models. In:Ben-Daya M, Duffuaa SO, Raouf A (eds) Maintenance, Modeling and Optimization. Kluwer Academic, Boston:201-214.
216. Nakagawa T (2002) Imperfect preventive maintenance models. In:Osaki S (ed) Stochastic Models in Reliability and Maintenance. Springer, Berlin:125-143.
217. Wang H, Pham H (2003) Optimal imperfect maintenance models. In:Pham H (ed) Handbook of Reliability Engineering. Springer, London:397-414.
218. Nguyen DC, Murthy DNP (1981) Optimal preventive maintenance policies for repairable systems. Oper Res 29:1181-1194.
219. Nakagawa T (1986) Periodic and sequential preventive maintenance policies. J Appl Probab 23:536-542.
220. Nakagawa T (1988) Sequential imperfect preventive maintenance policies. IEEE Trans Reliab 37:295-298.
221. Mie J (1995) Bathtub failure rate and upside-down bathtub mean residual life. IEEE Trans Reliab 44:388-391.
222. Baker Jr HG (1978) List processing in real time on a serial computer. Commun ACM 21:280-294.
223. Steele Jr GL (1975) Multiprocessing compactifying garbage collection. Commun ACM:18:495-508.
224. Cohen J (1981) Garbage collection of linked data structures. ACM Comput Surv 13:341-367
225. Kung HT, Song SW (1977) An efficient parallel garbage collection system and its correctness proof. In:18th Ann IEEE Symp Found Comput Sci:120-131.
226. Lieberman H, Hewitt C (1983) A real-time garbage collection based on the lifetimes of objects. Commun ACM 26:419-429.
227. Yuasa T (1990) Real-time garbage collection on general-purpose machines. J Syst Software 11:181-198
228. Suzuki K, Nakajima K (1995) Storage management software. Fujitsu 46:389397 .
229. Velpuri R, Adkoli A (1998) Oracle 8 Backup and Recovery Handbook. McGraw-Hill, England.
230. Chandy KM, Browne JC, Dissly CW, Uhrig WR (1975) Analytic models for rollback and recovery strategies in database systems. IEEE Trans Software Eng SE-1:100-110.
231. Reuter A (1984) Performance analysis of recovery techniques, ACM Trans Database Syst 4:526-559.232. Young JW (1974) A first order approximation to the optimum checkpoint interval. Commun ACM 17:530-531.
233. Gelenbe E (1979) On the optimum checkpoint interval. J Assoc Comput Machinary 26:259-270.
234. Fukumoto S, Kaio N, Osaki S (1992) A study of checkpoint generations for a database recovery mechanism. Comput Math Appl 1:63-68.
235. Nakagawa S, Fukumoto S, Ishii N (2003) Optimal checkpointing intervals of three error detection schemes by a double modular redundancy. Math Comput Model 38:1357-1363.
236. Qian CH, Pan Y, Nakagawa (2002) Optimal policies for a database system with two backup schemes. RAIRO Oper Res 36:227-235.
237. Nakamura S, Qian CH, Fukumoto S, Nakagawa T (2003) Optimal backup policy for a database system with incremental and full backups. Math Comput Modelling 38:1373-1379.
238. Parzen E (1962) Stochastic Processes. Holden-Day, San Francisco.
239. Beekman JA (1974) Two Stochastic Processes. Almqvist and Wiksell International, Stochholm.
240. Becker N (1989) Reliability models in cancer epidemiology. Biom J 31:727-748.
241. Becker N, Rittgen W (1990) Some mathematical properties of cumulative models regarding their application in cancer epidemiology Biom J 32:3-15.
242. Smith W (1973) Shot noise generated by a semi-Markov process. J Appl Probab 10:685-690.
243. Rice J (1977) On generalized shot noise. Adv Appl Probab 9:553-565.
244. Hsing TL, Teugels JL (1989) Extremal properties of shot noise processes. Adv Appl Probab 21:513-525.
245. Doney RA, O'Brien GL (1991) Loud shot noises. Ann Appl Probab 1:88-103.
246. McCormik WP (1997) Extremes for shot noise processes with heavy tailed amplitudes. J Appl Probab 34:643-656.
247. Lund RB, Butler RW, Paige RL (1999) Prediction of shot noise. J Appl Probab 36:374-388.
248. Lund RB, McCormik WP, Xiao YH (2004) Limiting properties of Poisson shot noise processes. J Appl Probab 41:911-918.
249. Waymire E, Gupta VK (1981) The mathematical structure of rainfall representations 1:A review of the stochastic rainfall models. Water Resourc Res $17: 1261-1272$.
250. Moran PA (1967) Dams in series with continuous release. J Appl Probab 4:380388 .
251. Yeh L, Hua LJ (1987) Optimal control of a finite dam. J Appl Probab 24:196199 .
252. Abdel-Hameed M, Nakhi (1990) Optimal control of finite dam using $\mathrm{P}_{\lambda, \tau}^{\mathrm{M}}$ policies and penalty cost: Total discounted and long run average cases. J Appl Probab 28:888-898.
253. Lund RB (1994) A dam with seasonal input. J Appl Probab 31:526-541.
254. Harrison JM, Resnick SI (1976) The stationary distribution and first exit probabilities of a storage process with general release rule. Math Oper Res 1:347358 .
255. Prabhu NU (1980) Stochastic Storage Processes. Springer, New York.
256. Lund RB (1996) The stability of storage models with shot noise input. J Appl Probab 33:830-839.257. Lemoine AJ, Wenocur ML (1986) A note on shot-noise and reliability modeling. Oper Res 34:320-323.
258. Rolski T, Schmidli H, Schmidt V, Teugels J (1999) Stochastic Processes for Insurance and Finance. John Wiley \& Sons, Chichester, England.
259. Klüppelberg C, Kyprianou AE, Maller RA (2004) Ruin probabilities and overshoots for general Lévy insurance risk processes. Ann Appl Probab 14:17661801 .
260. Embrecht P, Klüppelberg C, Mikosch T (1997) Modelling Extremal Events for Insurance and Finance. Springer, Berlin.
261. Asmussen S (2001) Ruin Probabilities. World Scientific, Singapore.
262. Williams T, Ancker Jr CJ (1963) Stochastic Duels. Oper Res 11:803-817.
263. Bhashyam N (1970) Stochastic duels with lethal dose. Nav Res Logist Q $17: 397-405$.
264. Bhashyam N (1973) Stochastic duels with correlated fire. Metrika 20:17-24.
265. Thompson DE (1972) Stochastic duels involving reliability. Nav Res Logist Q 19:145-148.
266. Lucas TW (2003) Damage functions and estimates of fratricide and collateral damage. Nav Res Logist 50:306-321.
267. Manor G, Kress M (1997) Optimality of the greedy shooting strategy in the presense of incomplete damage information. Nav Res Logist 44:613-622.# Index 

age replacement $44,71,81,82$
allowed time 169
annealing $31,32,169$
availability $42,104,132-142$
backup policy, time $2,4,147-165$
bathtub curve 129
Birbaum-Saunders distribution 27
birth process 12,26
bivariate distribution 26
block replacement $71,81,82,92$
Brownian motion 28,167
catastrophic failure 2
central limit theorem 9
common-cause failure 13
compound Poisson process $3,10,167$
computer system $2,4,81,117,131$, 147
condition-based maintenance 61, $103-116,143$
corrective maintenance, replacement $3,4,39,41,103-116$
counting process $5,9,10,12,26$
crack 2
creep 3
cumulative process $2,10,40,169$
database system 2,131-165
degenerate distribution 21
deterioration $2,61,86-90,104$
doubly stochastic process 15
downtime 167-169
dynamic programming 61

Erlang distribution 9
excess time 11
failure interaction $4,11,61,62,70-80$
failure rate $8,16,20,23,24-26,29,30$, $34-36,45,65,81,89,115,117,135$, 161
fatigue $1,2,11,103$
finite interval, time $4,126-129$
first-passage time $15,19,24,33,34,61$
gamma distribution $3,9,11,27,32$, $84,93,124$
garbage collection $2,4,108,131-145$
geometric distribution 67,156
hazard rate 8,16
imperfect maintenance 4,105, $117-129$
imperfect shock, hit $28-30,172$
increasing failure rate (IFR) $8,20,25$, 46
inspection $39,47,56,71,81-84,86-90$, 104
insurance $4,167,169,170$
intensity function $10,11,20,23,25$, $44,71,94,95,104,132,137$
jump process 15
$k$-out-of- $n$ system $61,63,69,70$
Lévy process 12,26maintenance policy $3,16,61,131$
Markov chain 3
mean time to failure (MTTF) 13, $15,19,22,24,29,33,34,37,43,62$, $63-65,85,86,109$
mean value function $10,12,20,22,25$, $34,71,94,104,132,137,143,152$
Miner's rule 1
minimal maintenance 4, 149-158
minimal repair $4,5,11,71,81,90-101$, $117,119,123,138$
multiunit (multicomponent) system $3,61-80$
multivariate distribution 26
negative binomial distribution 67
nonhomogeneous Poisson process 5, $10,11,12,20,22,23,25,34,43,44$, $71,94,103,104,132,137,143,149$, 152
normal distribution $9,18,27,86$
one-unit system $5,104,139$
parallel system $4,12,34,61-70,156$
periodic replacement $4,81-101,138$
Poisson distribution 9, 84, 105, 120
Poisson process $3,5,9-11,23,25,31$, $44,48,54,74,79,83,89,93,104$, $108,110,117,118,132,138,142$, $144,145,153,154,160,161,164$, 167
preventive maintenance $4,71,81,84$, $103-129,139,143,149,152-154$
preventive replacement $39,40,47,61$, 88
processing efficiency $2,131,137$
queuing process 167,168
random environment $4,61-70$
random failure level 29,173
random replacement 59,60
renewal equation $6,11,31,169$
renewal function $6,17,82$
renewal process $4-12,23,42,62,67$, $77,81,90,91,94,95,167$
renewal reward $10,11,41$
renewal theory $6-8$
repair $4,5,81,103,139,167$
replacement $3-5,13,39-101,103,118$, 119,123
residual lifetime 11
sequential maintenance $4,117,118$
series system $33,34,61,67,70,104$
shot noise $4,31,167,169$
$S-N$ curve 1
stochastic duel $4,12,167,170-174$
stochastic process $2,3,5,10-12,27$, 167
stress, strength $1,26,27$
two-unit system $4,11,61,70-80,104$
wear $2,3,11,26,28,83,103$
wear process $3,16,26-28,84,104$
Weibull distribution 26,65
Wiener process 28