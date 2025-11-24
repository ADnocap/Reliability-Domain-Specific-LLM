Stochastic Modelling and Applied Probability ..... 41
Terje Aven
Uwe Jensen
Stochastic
Models in
Reliability
Second Edition
(4) SpringerStochastic Mechanics Stochastic Modelling Random Media and Applied Probability
Signal Processing and Image Synthesis (Formerly: Mathematical Economics and Finance Applications of Mathematics)

Stochastic Optimization
Stochastic Control
Stochastic Models in Life Sciences
Edited by P.W. Glynn
Y. Le Jan

Advisory Board M. Hairer
I. Karatzas
F.P. Kelly
A. Kyprianou
B. Øksendal
G. Papanicolaou
E. Pardoux
E. Perkins
H.M. Soner

For further volumes:
http://www.springer.com/series/602.Terje Aven $\cdot$ Uwe Jensen

# Stochastic Models in Reliability 

Second EditionTerje Aven<br>University of Stavanger<br>Stavanger, Norway

Uwe Jensen
Fak. Naturwissenschaften
Inst. Angewandte Mathematik u. Statistik
Universität Hohenheim
Stuttgart, Germany

ISSN 0172-4568
ISBN 978-1-4614-7893-5 ISBN 978-1-4614-7894-2 (eBook)
DOI 10.1007/978-1-4614-7894-2
Springer New York Heidelberg Dordrecht London
Library of Congress Control Number: 2013942488
Mathematics Subject Classification (2010): 60G, 60K, 60K10, 60K20, 90B25
(C) Springer Science+Business Media New York 1999, 2013

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. Exempted from this legal reservation are brief excerpts in connection with reviews or scholarly analysis or material supplied specifically for the purpose of being entered and executed on a computer system, for exclusive use by the purchaser of the work. Duplication of this publication or parts thereof is permitted only under the provisions of the Copyright Law of the Publisher's location, in its current version, and permission for use must always be obtained from Springer. Permissions for use may be obtained through RightsLink at the Copyright Clearance Center. Violations are liable to prosecution under the respective Copyright Law.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.
While the advice and information in this book are believed to be true and accurate at the date of publication, neither the authors nor the editors nor the publisher can accept any legal responsibility for any errors or omissions that may be made. The publisher makes no warranty, express or implied, with respect to the material contained herein.

Printed on acid-free paper
Springer is part of Springer Science+Business Media (www.springer.com)# Preface 

In this second edition of the book, two major topics have been added to the original version. The first one relates to copula models (Sect.2.3), which are used to study the effects of structural dependencies on system reliability. We believe that an introduction to the fundamental ideas and concepts of copula models is important when reviewing basic reliability theory. The second new topic we have included is maintenance optimization models under constraints (Sect.5.5). These models have been addressed in some recent publications to meet the demand for models that adequately balance economic criteria and safety. We consider two specific models. The first is the so-called delay time model where the aim is to determine optimal inspection intervals minimizing the expected discounted costs under some safety constraints. The second model is also about optimal inspection, but here the system is represented by a monotone (coherent) structure function. In addition, we have made a number of minor adjustments to increase precision and we have also corrected misprints.

We received positive feedback to the first edition from friends and colleagues. Their hints and suggestions have been incorporated into this second edition. We thank all who contributed, by whatever means, to preparing the new edition.

Stavanger, Norway
Stuttgart, Germany

Terje Aven
Uwe Jensen.# Preface to the First Edition 

As can be seen from the files of the databases of Zentralblatt/Mathematical Abstracts and Mathematical Reviews, about $1 \%$ of all mathematical publications are connected to the keyword reliability. This gives an impression of the importance of this field and makes it clear that it is impossible to include all the topics connected to reliability in one book. The existing literature on reliability covers inter alia lifetime analysis, complex systems and maintenance models, and the books by Barlow and Proschan [31, 32] can be viewed as first milestones in this area. Since then the models and tools have been developed further. The aim of Stochastic Models in Reliability is to give a comprehensive up-to-date presentation of some of the classical areas of reliability, based on a more advanced probabilistic framework using the modern theory of stochastic processes. This framework allows the analyst to formulate general failure models, establish formulas for computing various performance measures, as well as to determine how to identify optimal replacement policies in complex situations. A number of special cases analyzed previously can be included in this framework. Our book presents a unifying approach to some of the key research areas of reliability theory, summarizing and extending results obtained in recent years. Having future work in this area in mind, it will be useful to have at hand a general set-up where the conditions and assumptions are formulated independently of particular models.

This book comprises five chapters in addition to two appendices.
Chapter 1 gives a short introduction to stochastic models of reliability, linking existing theory and the topics treated in this book. It also contains an overview of some questions and problems to be treated in the book. In addition Sect.1.1.6 explains why martingale theory is a useful tool for describing and analyzing the structure of complex reliability models. In the final section of the chapter we briefly discuss some important aspects of reliability modeling and analysis, and present two real-life examples. To apply reliability models in practice successfully, there are many challenges related to modeling and analysis that need to be faced. However, it is not within the scope of thisbook to discuss these challenges in detail. Our text is an introduction to the topic and of motivational character.

Chapter 2 presents an overview of some parts of basic reliability theory: the theory of complex (monotone) systems, both binary and multistate systems, as well as lifetime distributions and nonparametric classes of lifetime distributions. The aim of this chapter has not been to give a complete overview of the existing theory, but to highlight important areas and give a basis for the coming chapters.

Chapter 3 presents a general set-up for analyzing failure-prone systems. A (semi-) martingale approach is adopted. This general approach makes it possible to formulate a unifying theory of both nonrepairable and repairable systems, and it includes point processes, counting processes, and Markov processes as special cases. The time evolution of the system can also be analyzed on different information levels, which is one of the main attractions of the (semi-) martingale approach. Attention is drawn to the failure rate process, which is a key parameter of the model. Several examples of application of the set-up are given, including a monotone (coherent) system of possibly dependent components, and failure time and (minimal) repair models. A model for analyzing the time to failure based on risk reserves (the difference between total income and accumulated costs of repairs) is also covered.

In the next two chapters we look more closely at types of models for analyzing situations where the system and its components could be repaired or replaced in the case of failures, and where we model the downtime or costs associated with downtimes.

Chapter 4 gives an overview of availability theory of complex systems, having components that are repaired upon failure. Emphasis is placed on monotone systems comprising independent components, each generating an alternating renewal process. Multistate systems are also covered, as well as systems comprising cold standby components. Different performance measures are studied, including the distributions of the number of system failures in a time interval and the downtime of the system in a time interval. The chapter gives a rather comprehensive asymptotic analysis, providing a theoretical basis for approximation formulae used in cases where the time interval considered is long or the components are highly available.

Chapter 5 presents a framework for models of maintenance optimization, using the set-up described in Chap. 3. The framework includes a number of interesting special cases dealt with by other authors.

By allowing different information levels, it is possible to extend, for example, the classical age replacement model and minimal repair/replacement model to situations where information is available about the underlying condition of the system and the replacement time is based on this information. Again we illustrate the applicability of the model by considering monotone systems.

Chapters 3-5 are based on stochastic process theory, including theory of martingales and point, counting, and renewal processes. For the sake of completeness and to help the reader who is not familiar with this theory,two appendices have been included summarizing the mathematical basis and some key results. Appendix A gives a general introduction to probability and stochastic process theory, whereas Appendix B gives a presentation of results from renewal theory. Appendix A also summarizes basic notation and symbols.

Although conceived mainly as a research monograph, this book can also be used for graduate courses and seminars. It primarily addresses probabilists and statisticians with research interests in reliability. But at least parts of it should be accessible to a broader group of readers, including operations researchers and engineers. A solid basis in probability and stochastic processes is required, however. In some countries many operations researchers and reliability engineers now have a rather comprehensive theoretical background in these topics, so that it should be possible to benefit from reading the more sophisticated theory presented in this book. To bring the reliability field forward, we believe that more operations researchers and engineers should be familiar with the probabilistic framework of modern reliability theory. Chapters 1 and 2 and the first part of Chaps. 4 and 5 are more elementary and do not require the more advanced theory of stochastic processes.

References are kept to a minimum throughout, but readers are referred to the bibliographic notes following each chapter, which give a brief review of the material covered and related references.

# Acknowledgments 

We express our gratitude to our institutions, the Stavanger University College, the University of Oslo, and the University of Ulm, for providing a rich intellectual environment, and facilities indispensable for the writing of this book. The authors are grateful for the financial support provided by the Norwegian Research Council and Deutscher Akademischer Austauschdienst. We would also like to acknowledge our indebtedness to Jelte Beimers, Jørund Gåsemyr, Harald Haukås, Tina Herberts, Karl Hinderer, Günter Last, Volker Schmidt, Richard Serfozo, Marcel Smith, Fabio Spizzichino and Rune Winther for making helpful comments and suggestions on the manuscript. Thanks for $\mathrm{T}_{\mathrm{E}} \mathrm{Xnical}$ support go to Jürgen Wiedmann.

We especially thank Bent Natvig, University of Oslo, for the great deal of time and effort he spent reading and preparing comments. Thanks also go to the three reviewers for providing advice on the content and organization of the book. Their informed criticism motivated several refinements and improvements. Of course, we take full responsibility for any errors that remain.

We also acknowledge the editing and production staff at Springer for their careful work. In particular, we appreciate the smooth cooperation of John Kimmel.

Stavanger, Norway
Ulm, Germany

Terje Aven
Uwe Jensen.# Contents 

1 Introduction ..... 1
1.1 Lifetime Models ..... 1
1.1.1 Complex Systems ..... 2
1.1.2 Damage Models ..... 3
1.1.3 Different Information Levels ..... 4
1.1.4 Simpson's Paradox ..... 4
1.1.5 Predictable Lifetime ..... 5
1.1.6 A General Failure Model ..... 6
1.2 Maintenance ..... 7
1.2.1 Availability Analysis ..... 8
1.2.2 Optimization Models ..... 9
1.3 Reliability Modeling ..... 9
1.3.1 Nuclear Power Station ..... 11
1.3.2 Gas Compression System ..... 13
2 Basic Reliability Theory ..... 17
2.1 Complex Systems ..... 17
2.1.1 Binary Monotone Systems ..... 17
2.1.2 Multistate Monotone Systems ..... 31
2.2 Basic Notions of Aging ..... 34
2.2.1 Nonparametric Classes of Lifetime Distributions ..... 35
2.2.2 Closure Theorems ..... 38
2.2.3 Stochastic Comparison ..... 40
2.3 Copula Models of Complex Systems in Reliability ..... 42
2.3.1 Introduction to Copula Models ..... 42
2.3.2 The Influence of the Copula on the Lifetime Distribution of the System ..... 45
2.3.3 Archimedean Copulas ..... 49
2.3.4 The Expectation of the Lifetime of a Two-Component- System with Exponential Marginals ..... 50
2.3.5 Marshall-Olkin Distribution ..... 523 Stochastic Failure Models ..... 57
3.1 Notation and Fundamentals ..... 57
3.1.1 The Semimartingale Representation ..... 59
3.1.2 Transformations of SSMs ..... 68
3.2 A General Lifetime Model ..... 70
3.2.1 Existence of Failure Rate Processes ..... 72
3.2.2 Failure Rate Processes in Complex Systems ..... 73
3.2.3 Monotone Failure Rate Processes ..... 77
3.2.4 Change of Information Level ..... 78
3.3 Point Processes in Reliability:
Failure Time and Repair Models ..... 81
3.3.1 Alternating Renewal Processes: One-Component Systems with Repair ..... 84
3.3.2 Number of System Failures for Monotone Systems ..... 85
3.3.3 Compound Point Process: Shock Models ..... 86
3.3.4 Shock Models with State-Dependent Failure Probability ..... 88
3.3.5 Shock Models with Failures of Threshold Type ..... 89
3.3.6 Minimal Repair Models ..... 90
3.3.7 Comparison of Repair Processes for Different Information Levels ..... 95
3.3.8 Repair Processes with Varying Degrees of Repair ..... 97
3.3.9 Minimal Repairs and Probability of Ruin ..... 98
4 Availability Analysis of Complex Systems ..... 105
4.1 Performance Measures ..... 105
4.2 One-Component Systems ..... 106
4.2.1 Point Availability ..... 108
4.2.2 The Distribution of the Number of System Failures ..... 109
4.2.3 The Distribution of the Downtime in a Time Interval ..... 116
4.2.4 Steady-State Distribution ..... 119
4.3 Point Availability and Mean Number of System Failures ..... 120
4.3.1 Point Availability ..... 120
4.3.2 Mean Number of System Failures ..... 121
4.4 Distribution of the Number of System Failures ..... 125
4.4.1 Asymptotic Analysis for the Time to the First System Failure ..... 126
4.4.2 Some Sufficient Conditions ..... 131
4.4.3 Asymptotic Analysis of the Number of System Failures ..... 135
4.5 Downtime Distribution Given System Failure ..... 145
4.5.1 Parallel System ..... 146
4.5.2 General Monotone System ..... 148
4.5.3 Downtime Distribution of the $i$ th System Failure ..... 1494.6 Distribution of the System Downtime in an Interval ..... 151
4.6.1 Compound Poisson Process Approximation ..... 152
4.6.2 Asymptotic Analysis ..... 153
4.7 Generalizations and Related Models ..... 158
4.7.1 Multistate Monotone Systems ..... 158
4.7.2 Parallel System with Repair Constraints ..... 165
4.7.3 Standby Systems ..... 166
5 Maintenance Optimization ..... 175
5.1 Basic Replacement Models ..... 175
5.1.1 Age Replacement Policy ..... 175
5.1.2 Block Replacement Policy ..... 177
5.1.3 Comparisons and Generalizations ..... 178
5.2 A General Replacement Model ..... 180
5.2.1 An Optimal Stopping Problem ..... 180
5.2.2 A Related Stopping Problem ..... 183
5.2.3 Different Information Levels ..... 189
5.3 Applications ..... 190
5.3.1 The Generalized Age Replacement Model ..... 190
5.3.2 A Shock Model of Threshold Type ..... 193
5.3.3 Information-Based Replacement of Complex Systems ..... 194
5.3.4 A Parallel System with Two Dependent Components ..... 197
5.3.5 Complete Information About $T_{1}, T_{2}$ and $T$ ..... 198
5.3.6 A Burn-In Model ..... 202
5.4 Repair Replacement Models ..... 207
5.4.1 Optimal Replacement Under a General Repair Strategy ..... 207
5.4.2 A Markov-Modulated Repair Process: Optimization with Partial Information ..... 208
5.4.3 The Case of $m=2$ States ..... 214
5.5 Maintenance Optimization Models Under Constraints ..... 215
5.5.1 A Delay Time Model with Safety Constraints ..... 215
5.5.2 Optimal Test Interval for a Monotone Safety System ..... 229
A Background in Probability and Stochastic Processes ..... 245
A. 1 Basic Definitions ..... 245
A. 2 Random Variables, Conditional Expectations ..... 246
A.2.1 Random Variables and Expectations ..... 246
A.2.2 $L^{p}$-Spaces and Conditioning ..... 248
A.2.3 Properties of Conditional Expectations ..... 251
A.2.4 Regular Conditional Probabilities ..... 252
A.2.5 Computation of Conditional Expectations ..... 253
A. 3 Stochastic Processes on a Filtered Probability Space ..... 254A. 4 Stopping Times ..... 257
A. 5 Martingale Theory ..... 259
A. 6 Semimartingales ..... 266
A.6.1 Change of Time ..... 267
A.6.2 Product Rule ..... 268
B Renewal Processes ..... 273
B. 1 Basic Theory of Renewal Processes ..... 273
B. 2 Renewal Reward Processes ..... 280
B. 3 Regenerative Processes ..... 281
B. 4 Modified (Delayed) Processes ..... 281
References ..... 283
Index ..... 293# Introduction 

This chapter gives an introduction to the topics covered in this book: failure time models, complex systems, different information levels, maintenance and optimal replacement. We also include a section on reliability modeling, where we draw attention to some important factors to be considered in the modeling process. Two real life examples are presented: a reliability study of a system in a power plant and an availability analysis of a gas compression system.

### 1.1 Lifetime Models

In reliability we are mainly concerned with devices or systems that fail at an unforeseen or unpredictable (this term is defined precisely later) random age of $T>0$. This random variable is assumed to have a distribution $F, F(t)=$ $P(T \leq t), t \in \mathbb{R}$, with a density $f$. The hazard or failure rate $\lambda$ is defined on the support of the distribution by

$$
\lambda(t)=\frac{f(t)}{\bar{F}(t)}
$$

with the survival function $\bar{F}(t)=1-F(t)$. The failure rate $\lambda(t)$ measures the proneness to failure at time $t$ in that $\lambda(t) \triangle t \approx P(T \leq t+\triangle t \mid T>t)$ for small $\triangle t$. The (cumulative) hazard function is denoted by $\Lambda$,

$$
\Lambda(t)=\int_{0}^{t} \lambda(s) d s=-\ln \{\bar{F}(t)\}
$$

The well-known relation

$$
\bar{F}(t)=P(T>t)=\exp \{-\Lambda(t)\}
$$

establishes the link between the cumulative hazard and the survival function. Modeling in reliability theory is mainly concerned with additional informationabout the state of a system, which is gathered during the operating time of the system. This additional information leads to updated predictions about proneness to system failure. There are many ways to introduce such additional information into the model. In the following sections some examples of how to introduce additional information and how to model the lifetime $T$ are given.

# 1.1.1 Complex Systems 

As will be introduced in detail in Chap. 2, a complex system comprises $n$ components with positive random lifetimes $T_{i}, i=1,2, \ldots, n, n \in \mathbb{N}$. Let $\Phi:\{0,1\}^{n} \rightarrow\{0,1\}$ be the structure function of the system, which is assumed to be monotone. The possible states of the components and of the system, "intact" and "failed," are indicated by " 1 " and " 0 ," respectively. Then $\Phi_{t}=\Phi\left(\mathbf{X}_{t}\right)$ describes the state of the system at time $t$, where $\mathbf{X}_{t}=\left(X_{t}(1), \ldots, X_{t}(n)\right)$ and $X_{t}(i)$ denotes the indicator function

$$
X_{t}(i)=I\left(T_{i}>t\right)= \begin{cases}1 & \text { if } \quad T_{i}>t \\ 0 & \text { if } \quad T_{i} \leq t\end{cases}
$$

which is 1 , if component $i$ is intact at time $t$, and 0 otherwise. The lifetime $T$ of the system is then given by $T=\inf \left\{t \in \mathbb{R}_{+}: \Phi_{t}=0\right\}$.

Example 1.1. As a simple example the following system with three components is considered, which is intact if component 1 and at least one of the components 2 or 3 are intact:


In this example $\Phi_{t}=X_{t}(1)\left\{1-\left(1-X_{t}(2)\right)\left(1-X_{t}(3)\right)\right\}$ is easily obtained with $T=\inf \left\{t \in \mathbb{R}_{+}: \Phi_{t}=0\right\}=T_{1} \wedge\left(T_{2} \vee T_{3}\right)$, where as usual $a \wedge b$ and $a \vee b$ denote $\min \{a, b\}$ and $\max \{a, b\}$, respectively. The additional information about the lifetime $T$ is given by the observation of the state of the single components. As long as all components are intact, only a failure of component 1 leads to system failure. If one of the components 2 or 3 fails first, then the next component failure is a system failure.

Under the classical assumption that all components work independently, i.e., the random variables $T_{i}, i=1, \ldots, n$, are independent, certain characteristics of the system lifetime are of interest:

- Determining the system lifetime distribution from the known component lifetime distributions or at least finding bounds for this distribution (see Sects. 2.1 and 2.2).- Are certain properties of the component lifetime distributions like increasing failure rate (IFR) or increasing failure rate average (IFRA) preserved by forming monotone systems? One of these closure theorems states, for example, that the distribution of the system lifetime is IFRA if all component lifetimes have IFRA distributions (see Sect.2.2).
- In what way does a certain component contribute to the functioning of the whole system? The answer to this question leads to the definition of several importance measures (see Sect. 2.1).


# 1.1.2 Damage Models 

Additional information about the lifetime $T$ can also be introduced into the model in a quite different way. If the state or damage of the system at time $t \in \mathbb{R}_{+}$can be observed and this damage is described by a random variable $X_{t}$, then the lifetime of the system may be defined as

$$
T=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \geq S\right\}
$$

i.e., as the first time the damage hits a given level $S$. Here $S$ can be a constant or, more general, a random variable independent of the damage process. Some examples of damage processes $X=\left(X_{t}\right)$ of this kind are described in the following subsections.

## Wiener Process

The damage process is a Wiener process with positive drift starting at 0 and the failure threshold $S$ is a positive constant. The lifetime of the system is then known to have an inverse Gaussian distribution. Models of this kind are especially of interest if one considers different environmental conditions under which the system is working, as, for example, in so-called burn-in models. An accelerated aging caused by additional stress or different environmental conditions can be described by a change of time. Let $\tau: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$be an increasing function. Then $Z_{t}=X_{\tau(t)}$ denotes the actual observed damage. The time transformation $\tau$ drives the speed of the deterioration. One possible way to express different stress levels in time intervals $\left[t_{i}, t_{i+1}\right), 0=t_{0}<t_{1}<$ $\ldots<t_{k}, i=0,1, \ldots, k-1, k \in \mathbb{N}$, is the choice

$$
\tau(t)=\sum_{j=0}^{i-1} \beta_{j}\left(t_{j+1}-t_{j}\right)+\beta_{i}\left(t-t_{i}\right), t \in\left[t_{i}, t_{i+1}\right), \beta_{v}>0
$$

In this case it is seen that if $F_{0}$ is the inverse Gaussian distribution function of $T=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \geq S\right\}$, and $F$ is the distribution function of the lifetime $T_{a}=\inf \left\{t \in \mathbb{R}_{+}: Z_{t} \geq S\right\}$ under accelerated aging, then $F(t)=$ $F_{0}(\tau(t))$. A generalization in another direction is to consider a random time change, which means that $\tau$ is a stochastic process. By this, randomly varying environmental conditions can be modeled.# Compound Point Processes 

Processes of this kind describe so-called shock processes where the system is subject to shocks that occur from time to time and add a random amount to the damage. The successive times of occurrence of shocks, $T_{n}$, are given by an increasing sequence $0<T_{1} \leq T_{2} \leq \ldots$ of random variables, where the inequality is strict unless $T_{n}=\infty$. Each time point $T_{n}$ is associated with a real-valued random mark $V_{n}$, which describes the additional damage caused by the $n$th shock. The marked point process is denoted $(T, V)=\left(T_{n}, V_{n}\right), n \in \mathbb{N}$. From this marked point process the corresponding compound point process $X$ with

$$
X_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right) V_{n}
$$

is derived, which describes the accumulated damage up to time $t$. The simplest example is a compound Poisson process in which the shock arrival process is Poisson and the shock amounts $\left(V_{n}\right)$ are i.i.d. random variables. As before, the lifetime $T$ is the first time the damage process $\left(X_{t}\right)$ hits the level $S$. If we go one step further and assume that $S$ is not deterministic and fixed, but a random failure level, then we can describe a situation in which the observed damage process does not carry complete information about the (failure) state of the system; the failure can occur at different damage levels $S$.

Another way to describe the failure mechanism is the following. Let the accumulated damage up to time $t$ be given by the shock process $X_{t}$ as in (1.2). If the system is up at $t-$ just before $t$, the accumulated damage equals $X_{t-}=x$ and a shock of magnitude $y$ occurs at $t$, then the probability of failure at $t$ is $p(x+y)$, where $p(x)$ is a given $[0,1]$-valued function. In this model failures can only occur at shock times and the accumulated damage determines the failure probability.

### 1.1.3 Different Information Levels

It was pointed out above in what way additional information can lead to a reliability model. But it is also important to note that in one and the same model different observation levels are possible, i.e., the amount of actual available information about the state of a system may vary. The following examples will show the effect of different degrees of information.

### 1.1.4 Simpson's Paradox

This paradox says that if one compares the death rates in two countries, say A and B , then it is possible that the crude overall death rate in country A is higher than in B although all age-specific death rates in B are higher than in A . This can be transferred to reliability in the following way. Considering a twocomponent parallel system, the failure rate of the system lifetime may increasealthough the component lifetimes have decreasing failure rates. The following proposition, which can be proved by some elementary calculations, yields an example of this.

Proposition 1.2. Let $T=T_{1} \vee T_{2}$ with i.i.d. random variables $T_{i}, i=1,2$, following the common distribution $F$,

$$
F(t)=1-e^{-u(t)}, t \geq 0, u(t)=\gamma t+\alpha\left(1-e^{-\beta t}\right), \alpha, \beta, \gamma>0
$$

If $2 \alpha e^{\alpha}<\left(\frac{\gamma}{\beta}\right)^{2}<1$, then the failure rate $\lambda$ of the lifetime $T$ increases, whereas the component lifetimes $T_{i}$ have decreasing failure rates.

This example shows that it makes a great difference whether only the system lifetime can be observed (aging property: IFR) or additional information about the component lifetimes is available (aging property: DFR). The aging property of the system lifetime of a complex system does not only depend on the joint distribution of the component lifetimes but also, of course, on the structure function. Instead of a two-component parallel system, consider a series system where the component lifetimes have the same distributions as in Proposition 1.2. Then the failure rate of $T_{\text {ser }}=T_{1} \wedge T_{2}$ decreases, whereas $T_{\text {par }}=T_{1} \vee T_{2}$ has an IFR.

# 1.1.5 Predictable Lifetime 

The Wiener process $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, with positive drift $\mu$ and variance scaling parameter $\sigma$, is a popular damage threshold model. The process $X$ can be represented as $X_{t}=\sigma B_{t}+\mu t$, where $B$ is standard Brownian motion. If one assumes that the failure level $S$ is a fixed known constant, then the lifetime $T=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \geq S\right\}$ follows an inverse Gaussian distribution with a finite mean $E T=S / \mu$. One criticism of this model is that the paths of $X$ are not monotone. As a partial answer, one can respond that maintenance actions also lead to improvements and thus $X$ could be decreasing at some time points. A more severe criticism from the point of view of the available information is the following. It is often assumed that in this model the paths of the damage process can be observed continuously. But this would make the lifetime $T$ a predictable random time (a precise definition follows in Chap. 3), i.e., there is an increasing sequence $\tau_{n}, n \in \mathbb{N}$, of random time points that announces the failure. In this model one could choose $\tau_{n}=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \geq S-1 / n\right\}$, and take $n$ large enough and stop operating the system at $\tau_{n}$ "just" before failure, to carry out some preventive maintenance, cf. Fig. 1.1. This does not usually apply in practical situations. This example shows that one has to distinguish carefully between the different information levels for the model formulation (complete information) and for the actual observation (partial information).

Fig. 1.1. Predictable stopping time

# 1.1.6 A General Failure Model 

The general failure model considered in Chap. 3 uses elements of the theory of stochastic processes and particularly some martingale theory. Some of the readers might wonder whether sophisticated theory like this is necessary and suitable in reliability, a domain with engineering applications. Instead of a comprehensive justification we give a motivating example.

Example 1.3. We consider a simple two-component parallel system with independent $\operatorname{Exp}\left(\alpha_{i}\right)$ distributed component lifetimes $T_{i}, i=1,2$. The system lifetime $T=T_{1} \vee T_{2}$ has distribution function

$$
F(t)=P\left(T_{1} \leq t, T_{2} \leq t\right)=\left(1-e^{-\alpha_{1} t}\right)\left(1-e^{-\alpha_{2} t}\right)
$$

with an ordinary failure rate

$$
\lambda(t)=\frac{\alpha_{1} e^{-\alpha_{1} t}+\alpha_{2} e^{-\alpha_{2} t}-\left(\alpha_{1}+\alpha_{2}\right) e^{-\left(\alpha_{1}+\alpha_{2}\right) t}}{e^{-\alpha_{1} t}+e^{-\alpha_{2} t}-e^{-\left(\alpha_{1}+\alpha_{2}\right) t}}
$$

This formula is rather complicated for such a simple system and reveals nothing about the structure of the system.Using elementary calculus it can be shown that for $\alpha_{1} \neq \alpha_{2}$ the failure rate is increasing on $\left(0, t^{*}\right)$ and decreasing on $\left(t^{*}, \infty\right)$ for some $t^{*}>0$. This property of the failure rate, however, is neither obvious nor immediate to see. We also know that $F$ is of IFRA type.

But is it not more natural and simpler to say that a failure rate (process) should be 0 as long as both components work (no system failure can occur) and, when the first component failure occurs, then the rate switches to $\alpha_{1}$ or $\alpha_{2}$ depending on which component survives? We want to derive a model that allows such a simple failure rate process and also includes the ordinary failure rate. Of course, this simple failure rate process, which can be expressed as$$
\lambda_{t}=\alpha_{1} I\left(T_{2} \leq t<T_{1}\right)+\alpha_{2} I\left(T_{1} \leq t<T_{2}\right)
$$

needs knowledge about the random component lifetimes $T_{i}$. Now the failure rate $\lambda_{t}$ is a stochastic process and the information about the status of the components at time $t$ is represented by a filtration. The model allows for changing the information level and the ordinary failure rate can be derived from $\lambda_{t}$ on the lowest level possible, namely no information about the component lifetimes.

The modern theory of stochastic processes allows for the development of a general failure model that incorporates the above aspects: time dynamics and different information levels. Chapter 3 presents this model. The failure rate process $\lambda_{t}$ is one of the basic parameters of this set-up. If we consider the lifetime $T$, under some mild conditions we obtain the failure rate process on $\{T>t\}$ as the limit of conditional expectations with respect to the pre- $t$ history ( $\sigma$-algebra) $\mathcal{F}_{t}$,

$$
\lambda_{t}=\lim _{h \rightarrow 0+} \frac{1}{h} P\left(T \leq t+h \mid \mathcal{F}_{t}\right)
$$

extending the classical failure rate $\lambda(t)$ of the system. To apply the set-up, focus should be placed on the failure rate process $\left(\lambda_{t}\right)$. When this process has been determined, the model has basically been established. Using the above interpretation of the failure rate process, it is in most cases rather straightforward to determine its form. The formal proofs are, however, often quite difficult.

If we go one step further and consider a model in which the system can be repaired or replaced at failure, then attention is paid to the number $N_{t}$ of system failures in $[0, t]$. Given certain conditions, the counting process $N=$ $\left(N_{t}\right), t \in \mathbb{R}_{+}$, has an "intensity" that as an extension of the failure rate process can be derived as the limit of conditional expectations

$$
\lambda_{t}=\lim _{h \rightarrow 0+} \frac{1}{h} E\left[N_{t+h}-N_{t} \mid \mathcal{F}_{t}\right]
$$

where $\mathcal{F}_{t}$ denotes the history of the system up to time $t$. Hence we can interpret $\lambda_{t}$ as the (conditional) expected number of system failures per unit of time at time $t$ given the available information at that time. Chapter 3 includes several special cases that demonstrate the broad spectrum of potential applications.

# 1.2 Maintenance 

To prolong the lifetime, to increase the availability, and to reduce the probability of an unpredictable failure, various types of maintenance actions are being implemented. The most important maintenance actions include:

- Preventive replacements of parts of the system or of the whole system
- Repairs of failed units- Providing spare parts
- Inspections to check the state of the system if not observed continuously

Taking maintenance actions into account leads, depending on the specific model, to one of the following subject areas: Availability Analysis and Optimization Models.

# 1.2.1 Availability Analysis 

If the system or parts of it are repaired or replaced when failures occur, the problem is to characterize the performance of the system. Different measures of performance can be defined as, for example,

- The probability that the system is functioning at a certain point in time (point availability)
- The mean time to the first failure of the system
- The probability distribution of the downtime of the system in a given time interval.

Traditionally, focus has been placed on analyzing the point availability and its limit (the steady-state availability). For a single component, the steadystate formula is given by $M T T F /(M T T F+M T T R)$, where $M T T F$ and $M T T R$ represent the mean time to failure and the mean time to repair (mean repair time), respectively. The steady-state probability of a system comprising several components can then be calculated using the theory of complex (monotone) systems.

Often, performance measures related to a time interval are used. Such measures include the distribution of the number of system failures, and the distribution of the downtime of the system, or at least the mean of these distributions. Measures related to the number of system failures are important from an operational and safety point of view, whereas measures related to the downtime are more interesting from a productional point of view. Information about the probability of having a long downtime in a time interval is important for assessing the economic risk related to the operation of the system. For production systems, it is sometimes necessary to use a multistate representation of the system and some of its components, to reflect different production levels.

Compared to the steady-state availability, it is of course more complicated to compute the performance measures related to a time interval, in particular the probability distributions of the number of system failures and of the downtime. Using simplifications and approximations, it is however possible to establish formulas that can be used in practice. For highly available systems, a Poisson approximation for the number of system failures and a compound Poisson approximation for the downtime distribution are useful in many cases.

These topics are addressed in Chap. 4, which gives a detailed analysis of the availability of monotone systems. Emphasis is placed on performancemeasures related to a time interval. Sufficient conditions are given for when the Poisson and the compound Poisson distributions are asymptotic limits.

# 1.2.2 Optimization Models 

If a valuation structure is given, i.e., costs of replacements, repairs, downtime, etc., and gains, then one is naturally led to the problem of planning the maintenance action so as to minimize (maximize) the costs (gains) with respect to a given criterion. Examples of such criteria are expected costs per unit time and total expected discounted costs.

Example 1.4. We resume Example 1.3, p. 6, and consider the simple twocomponent parallel system with independent $\operatorname{Exp}\left(\alpha_{i}\right)$ distributed component lifetimes $T_{i}, i=1,2$, with the system lifetime $T=T_{1} \vee T_{2}$. We now allow preventive replacements at costs of $c$ units to be carried out before failure, and a replacement upon system failure at cost $c+k$. It seems intuitive that $T_{1} \wedge T_{2}$, the time of the first component failure, should be a candidate for an optimal replacement time with respect to some cost criterion, at least if $c$ is "small" compared to $k$. How can we prove that this random time $T_{1} \wedge T_{2}$ is optimal among all possible replacement times? How can we characterize the set of all possible replacement times?

These questions can only be answered in the framework of martingale theory and are addressed in Chap. 5.

One can imagine that thousands of models (and papers) can be created by combining the different types of lifetime models with different maintenance actions. The general optimization framework formulated in Chap. 5 incorporates a number of such models. Here the emphasis is placed on determining the optimal replacement time of a deteriorating system. The framework is based on the failure model of Chap. 3, which means that rather complex and very different situations can be studied. Special cases include monotone systems, (minimal) repair models, and damage processes, with different information levels.

### 1.3 Reliability Modeling

Models analyzed in this book are general, in the sense that they do not refer to any specific real life situation but are applicable in a number of cases. This is the academic and theoretical approach of mathematicians (probabilists, statisticians) who provide tools that can be used in applications.

The reliability engineer, on the other hand, has a somewhat different starting point. He or she is faced with a real problem and has to analyze this problem using a mathematical model that describes the situation appropriately.Sometimes it is rather straightforward to identify a suitable model, but often the problem is complex and it is difficult to see how to solve it. In many cases, a model needs to be developed. The modeling process requires both experience on the part of the practitioner and knowledge on the part of the theorist.

However, it is not within the scope of this book to discuss in detail the many practical aspects related to reliability modeling and analysis. Only a few issues will be addressed. In this introductory section we will highlight important factors to be considered in the modeling process and two real life examples will be presented.

The objectives of the reliability study can affect modeling in many ways, for example, by specifying which performance measures and which factors (parameters) are to be analyzed. Different objectives will require different approaches and methods for modeling and analysis. Is the study to provide decision support in a design process of a system where the problem is to choose between alternative solutions; is the problem to give a basis for specifying reliability requirements; or is the aim to search for an optimal preventive maintenance strategy? Clearly, these situations call for different models.

The objectives of the study may also influence the choice of the computational approach. If it is possible to use analytical calculation methods, these would normally be preferred. For complex situations, Monte Carlo simulation often represents a useful alternative, cf., e.g., $[13,64]$.

The modeling process starts by clarifying the characteristics of the situation to be analyzed. Some of the key points to address are:

Can the system be decomposed into a set of independent subsystems (components)? Are all components operating normally or are some on stand-by? What is the state of the component after a repair? Is it "as good as new"? What are the resources available for carrying out the repairs? Are some types of preventive maintenance being employed? Is the state of the components and the system continuously monitored, or is it necessary to carry out inspections to reveal their condition? Is information available about the underlying condition of the system and components, such as wear, stress, and damage?

Having identified important features of the system, we then have to look more specifically at the various elements of the model and resolve questions like the following:

- How should the deterioration process of the components and system be modeled? Is it sufficient to use a standard lifetime model where the age of the unit is the only information available? How should the repair/replacement times be modeled?
- How are the preventive maintenance activities to be reflected in the model? Are these activities to be considered fixed in the model or is it possible to plan preventive maintenance action so that costs (rewards) are minimized (maximized)?
- Is a binary (two-state) approach for components and system sufficiently accurate, or is multistate modeling required?- How are the system and components to be represented? Is a reliability block diagram appropriate?
- Are time dynamics to be included or is a time stationary model sufficient?
- How are the parameters of the model to be determined? What kind of input data are required for using the model? How is uncertainty to be dealt with?

Depending on the answers to these questions, relevant models can be identified. It is a truism that no model can cover all aspects, and it is recommended that one starts with a simple model describing the main features of the system.

The following application examples give further insight into the situations that can be modeled using the theory presented in this book.

# 1.3.1 Nuclear Power Station 

In this example we consider a small part of a very complex technical system, in which safety aspects are of great importance. The nuclear power station under consideration consists of two identical boiling water reactors in commercial operation, each with an electrical power of $1,344 \mathrm{MW}$. They started in 1984 and 1985 , respectively, working with an efficiency of $35 \%$.

Nuclear power plants have to shut down from time to time to exchange the nuclear fuel. This is usually performed annually. During the shutdown phase a lot of maintenance tasks and surveillance tests are carried out. One problem during such phases is that decay heat is still produced and thus has to be removed. Therefore, residual heat removal (RHR) systems are in operation. At the particular site, three identical systems are available, each with a capacity of $100 \%$. They are designed to remove decay heat during accident conditions occurring at full power as well as for operational purposes in cooldown phases.

One of these RHR systems is schematically shown in Fig. 1.2. It consists of three different trains including the closed cooling water system. Several pumps and valves are part of the RHR system. The primary cooling system can be modeled as a complex system comprising the following main components:

- Closed cooling water system pump (CCWS)
- Service water system pump (SWS)
- Low-pressure pump with a pre-stage (LP)
- High-pressure pump (HP)
- Nuclear heat exchanger (RHR)
- Valves $\left(V_{1}, V_{2}, V_{3}\right)$

For the analysis we have to distinguish between two cases:

1. The RHR system is not in operation.

Then the functioning of the system can be viewed as a binary structure of the main components as is shown in the reliability block diagram in

Fig. 1.2. Cooling system of a power plant


Fig. 1.3. Reliability block diagram

Fig. 1.3. When the system is needed, it is possible that single components or the whole system fails to start on demand. In this case, to calculate the probability of a failure on demand, we have to take all components in the reliability block diagram into consideration. Two of the valves, $V_{1}$ and $V_{2}$, are in parallel. Therefore, the RHR system fails on demand if either $V_{1}$ and $V_{2}$ fail or at least one of the remaining components LP, $\ldots, \mathrm{HP}, V_{3}$ fails. We assume that the time from a check of a component until a failure in the idle state is exponentially distributed. The failure rates are $\lambda_{v_{1}}, \lambda_{v_{2}}, \lambda_{v_{3}}$ for the valves and $\lambda_{p_{1}}, \lambda_{p_{2}}, \lambda_{p_{3}}, \lambda_{p_{4}}, \lambda_{h}$ for the other components. If the check (inspection or operating period) dates $t$ time units back, then the probability of a failure on demand is given by

$$
1-\left\{1-\left(1-e^{-\lambda_{v_{1}} t}\right)\left(1-e^{-\lambda_{v_{2}} t}\right)\right\} e^{-\left(\lambda_{p_{1}}+\lambda_{p_{2}}+\lambda_{p_{3}}+\lambda_{p_{4}}+\lambda_{h}+\lambda_{v_{3}}\right) t}
$$2. The RHR system is in operation.

During an operation phase, only the pumps and the nuclear heat exchanger can fail to operate. If the valves have once opened on demand when the operation phase starts, these valves cannot fail during operation. Therefore, in this operation case, we can either ignore the valves in the block diagram or assign failure probability 0 to $V_{1}, V_{2}, V_{3}$. The structure reduces to a simple series system. If we assume that the failure-free operating times of the pumps and the heat exchanger are independent and have distributions $F_{p_{1}}, F_{p_{2}}, F_{p_{3}}, F_{p_{4}}$, and $F_{h}$, respectively, then the probability that the system fails before a fixed operating time $t$ is just

$$
1-\bar{F}_{p_{1}}(t) \bar{F}_{p_{2}}(t) \bar{F}_{p_{3}}(t) \bar{F}_{p_{4}}(t) \bar{F}_{h}(t)
$$

where $\bar{F}(t)$ denotes the survival probability.
In both cases the failure time distributions and the failure rates have to be estimated. One essential condition for the derivation of the above formulae is that all components have stochastically independent failure times or lifetimes. In some cases such an independence condition does not apply. In Chap. 3 a general theory is developed that also includes the case of complex systems with dependent component lifetimes. The framework presented covers different information levels, which allow updating of reliability predictions using observations of the condition of the components of the system, for example.

# 1.3.2 Gas Compression System 

This example outlines various aspects of the modeling process related to the design of a gas compression system.

A gas producer was designing a gas production system, and one of the most critical decisions was related to the design of the gas compression system.

At a certain stage of the development, two alternatives for the compression system were considered:
(i) One gas train with a maximum throughput capacity of $100 \%$
(ii) Two trains in parallel, each with a maximum throughput capacity of $50 \%$.

Normal production is $100 \%$. For case (i) this means that the train is operating normally and a failure stops production completely. For case (ii) both trains are operating normally. If one train fails, production is reduced to $50 \%$. If both trains are down, production is 0 .

Each train comprises compressor-turbine, cooler, and scrubber. A failure of one of these "components" results in the shutdown of the train. Thus a train is represented by a series structure of the three components compressorturbine, cooler, and scrubber.The following failure and repair time data were assumed:

| Component | Failure rate <br> (unit of time: 1 year) | Mean repair time <br> (unit of time: 1 h$)$ |
| :-- | :--: | :--: |
| Compressor-turbine | 10 | 12 |
| Cooler | 2 | 50 |
| Scrubber | 1 | 20 |

To compare the two alternatives, a number of performance measures were considered. Particular interest was shown in performance measures related to the number of system shutdowns, the time the system has a reduced production level, and the total production loss due to failures of the system. The gas sales agreement states that the gas demand is to be met with a very high reliability, and failures could lead to considerable penalties and loss of goodwill, as well as worse sales perspectives for the future.

Using models as will be described in Chap. 4, it was possible to compute these performance measures, given certain assumptions.

It was assumed that each component generates an alternating renewal process, which means that the repair brings the component to a condition that is as good as new. The uptimes were assumed to be distributed exponentially, so that the component in the operating state has a constant failure rate. The failure rate used was based on experience data for similar equipment. Such a component model was considered to be sufficiently accurate for the purpose of the analysis. The exponential model represents a "first-order approximation," which makes it rather easy to gain insight into the performance of the system. For a complex "component" with many parts to be maintained, it is known that the overall failure rate exhibits approximately exponential nature. Clearly, if all relevant information is utilized, the exponential model is rather crude. But again we have to draw attention to the purpose of the analysis: provide decision support concerning the choice of design alternatives. Only the essential features should be included in the model.

A similar type of reasoning applies to the problem of dependency between components. In this application all uptimes and downtimes of the components were assumed to be independent. In practice there are, of course, some dependencies present, but by looking into the failure causes and the way the components were defined, the assumption of independence was not considered to be a serious weakness of the model, undermining the results of the analysis.

To determine the repair time distribution, expert opinions were used. The repair times, which also include fault diagnosis, repair preparation, test and restart, were assessed for different failure modes. As for the uptimes, it was assumed that no major changes over time take place concerning component design, operational procedures, etc.Uncertainty related to the input quantities used was not considered. Instead, sensitivity studies were performed with the purpose of identifying how sensitive the results were with respect to variations in input parameters.

Of the results obtained, we include the following examples:

- The gas train is down $2.7 \%$ of the time in the long run.
- For alternative (i), the average system failure rate, i.e., the average number of system failures per year, equals 13. For alternative (ii) it is distinguished between failures resulting in production below $100 \%$ and below $50 \%$. The average system failure rates for these levels are approximately 26 and 0.7 , respectively. Alternative (ii) has a probability of about $50 \%$ of having one or more complete shutdowns during a year.
- The mean lost production equals $2.7 \%$ for both alternatives. The probability that the lost production during 1 year is more than $4 \%$ of demand is approximately equal to 0.16 for alternative (i) and 0.08 for alternative (ii).

This last result is based on assumptions concerning the variation of the repair times. Refer to Sect.4.7.1, p. 162, where the models and methods used to compute these measures are summarized.

The results obtained, together with an economic analysis, gave the management a good basis for choosing the best alternative.

Bibliographic Notes. There are now many journals strongly devoted to reliability, for example, the IEEE Transactions on Reliability and Reliability Engineering and System Safety. In addition, there are many journals in Probability and Operations Research that publish papers in this field.

As mentioned before, there is an extensive literature covering a variety of stochastic models of reliability. Instead of providing a long and, inevitably, almost certainly incomplete list of references, some of the surveys and review articles are quoted, as well as some of the reliability books.

From time to time, the Naval Research Logistics Quarterly journal publishes survey articles in this field, among them the renowned article by Pierskalla and Voelker [130], which appeared with 259 references in 1976, updated by Sherif and Smith [144] with an extensive bibliography of 524 references in 1981, followed by Valdez-Flores and Feldman [158] with 129 references in 1989. Bergman's review [39] reflects the author's experience in industry and emphasizes the usefulness of reliability methods in applications. Gertsbakh's paper [75] reviews asymptotic methods in reliability and especially investigates under what conditions the lifetime of a complex system with many components is approximately exponentially distributed. Natvig [125] gives a concise overview of importance measures for monotone systems. The surveys of Arjas [4] and Koch [108] consider reliability models using more advanced mathematical tools as marked point processes and martingales. A guided tour for the non-expert through point process and intensity-based models in reliability is presented in the article of Hokstad [89]. The book of Thompson [155] gives amore elementary presentation of point processes in reliability. Other reliability books that we would like to draw attention to are Aven [13], Barlow and Proschan [31, 32], Beichelt and Franken [36], Bergman and Klefsjö [40], Gaede [70], Gertsbakh [74], Høyland and Rausand [90], and Kovalenko, Kuznetsov, and Pegg [110]. Some of the models addressed in this introduction are treated in the overview of Jensen [94] where related references can also be found.# Basic Reliability Theory 

This chapter presents some basic theory of reliability, including complex system theory and properties of lifetime distributions. Basic availability theory and models for maintenance optimization are included in Chaps. 4 and 5, respectively.

The purpose of this chapter is not to give a complete overview of the existing theory, but to introduce the reader to common reliability concepts, models, and methods. The exposition highlights basic ideas and results, and it provides a starting point for the more advanced theory presented in Chaps. 3-5.

### 2.1 Complex Systems

This section gives an overview of some basic theory of complex systems. Binary monotone (coherent) systems are covered, as well as multistate monotone systems.

### 2.1.1 Binary Monotone Systems

In this section we give an introduction to the classical theory of monotone (coherent) systems. First we study the structural relations between a system and its components. Then methods for calculation of system reliability are reviewed when the component reliabilities are known. When not stated otherwise, the random variables representing the state of the components are assumed to be independent.

## Structural Properties

We consider a system comprising $n$ components, which are numbered consecutively from 1 to $n$. In this section we distinguish between two states: a functioning state and a failure state. This dichotomy applies to the system as

Fig. 2.1. Series structure
well as to each component. To indicate the state of the $i$ th component, we assign a binary variable $x_{i}$ to component $i$ :

$$
x_{i}= \begin{cases}1 \text { if component } i \text { is in the functioning state } \\ 0 \text { if component } i \text { is in the failure state. }\end{cases}
$$

(The term binary variable refers to a variable taking on the values 0 or 1.) Similarly, the binary variable $\Phi$ indicates the state of the system:

$$
\Phi= \begin{cases}1 \text { if the system is in the functioning state } \\ 0 \text { if the system is in the failure state. }\end{cases}
$$

We assume that

$$
\Phi=\Phi(\mathbf{x})
$$

where $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, i.e., the state of the system is determined completely by the states of the components. We refer to the function $\Phi(\mathbf{x})$ as the structure function of the system, or simply the structure. In the following we will often use the phrase structure in place of system.

Example 2.1. A system that is functioning if and only if each component is functioning is called a series system. The structure function for this system is given by

$$
\Phi(\mathbf{x})=x_{1} \cdot x_{2} \cdot \ldots \cdot x_{n}=\prod_{i=1}^{n} x_{i}
$$

A series structure can be illustrated by the reliability block diagram in Fig. 2.1. "Connection between $a$ and $b$ " means that the system functions.

Example 2.2. A system that is functioning if and only if at least one component is functioning is called a parallel system. The corresponding reliability block diagram is shown in Fig. 2.2.

The structure function is given by

$$
\Phi(\mathbf{x})=1-\left(1-x_{1}\right)\left(1-x_{2}\right) \cdots\left(1-x_{n}\right)=1-\prod_{i=1}^{n}\left(1-x_{i}\right)
$$

The expression on the right-hand side in (2.1) is often written $\amalg x_{i}$. Thus, a parallel system with two components has structure function

Fig. 2.2. Parallel structure

$$
\Phi(\mathbf{x})=1-\left(1-x_{1}\right)\left(1-x_{2}\right)=\prod_{i=1}^{2} x_{i}
$$

which we also write as $\Phi(\mathbf{x})=x_{1} \coprod x_{2}$.
Example 2.3. A system that is functioning if and only if at least $k$ out of $n$ components are functioning is called a $k$-out-of- $n$ system. A series system is an $n$-out-of- $n$ system, and a parallel system is a 1-out-of- $n$ system. The structure function for a $k$-out-of- $n$ system is given by

$$
\Phi(\mathbf{x})= \begin{cases}1 \text { if } & \sum_{i=1}^{n} x_{i} \geq k \\ 0 \text { if } & \sum_{i=1}^{n} x_{i}<k\end{cases}
$$

As an example, we will look at a 2 -out-of-3 system. This system can be illustrated by the reliability block diagram shown in Fig. 2.3. An airplane that is capable of functioning if and only if at least two of its three engines are functioning is an example of a 2 -out-of-3 system.

Definition 2.4. (Monotone system). A system is said to be monotone if

1. its structure function $\Phi$ is nondecreasing in each argument, and
2. $\Phi(\mathbf{0})=0$ and $\Phi(\mathbf{1})=1$.

Condition 1 says that the system cannot deteriorate (that is, change from the functioning state to the failed state) by improving the performance of a component (that is, replacing a failed component by a functioning component). Condition 2 says that if all the components are in the failure state, then the system is in the failure state, and if all the components are in the functioning state, then the system is in the functioning state.

All the systems we consider are monotone. In the reliability literature, much attention has be devoted to coherent systems, which is a subclass of monotone systems. Before we define a coherent system we need some notation.

Fig. 2.3. 2-Out-of-3 structure

The vector $\left(\cdot_{i}, \mathbf{x}\right)$ denotes a state vector where the state of the $i$ th component is equal to 1 or $0 ;\left(1_{i}, \mathbf{x}\right)$ denotes a state vector where the state of the $i$ th component is equal to 1 , and $\left(0_{i}, \mathbf{x}\right)$ denotes a state vector where the state of the $i$ th component is equal to 0 ; the state of component $j, j \neq i$, equals $x_{j}$. If we want to specify the state of some components, say $i \in J$ $(J \subset\{1,2, \ldots, n\})$, we use the notation $\left(\cdot_{J}, \mathbf{x}\right)$. For example, $\left(\mathbf{0}_{J}, \mathbf{x}\right)$ denotes the state vector where the states of the components in $J$ are all 0 and the state of component $i, i \notin J$, equals $x_{i}$.

Definition 2.5. (Coherent system). A system is said to be coherent if

1. its structure function $\Phi$ is nondecreasing in each argument, and
2. each component is relevant, i.e., there exists at least one vector $\left(\cdot_{i}, \mathbf{x}\right)$ such that $\Phi\left(1_{i}, \mathbf{x}\right)=1$ and $\Phi\left(0_{i}, \mathbf{x}\right)=0$.

It is seen that if $\Phi$ is coherent, then $\Phi$ is also monotone. We also need the following terminology.

Definition 2.6. (Minimal cut set). A cut set $K$ is a set of components that by failing causes the system to fail, i.e., $\Phi\left(\mathbf{0}_{K}, \mathbf{1}\right)=0$. A cut set is minimal if it cannot be reduced without losing its status as a cut set.

Definition 2.7. (Minimal path set). A path set $S$ is a set of components that by functioning ensures that the system is functioning, i.e., $\Phi\left(\mathbf{1}_{S}, \mathbf{0}\right)=1$. A path set is minimal if it cannot be reduced without losing its status as a path set.

Example 2.8. Consider the reliability block diagram presented in Fig. 2.4. The minimal cut sets of the system are: $\{1,5\},\{4,5\},\{1,2,3\}$, and $\{2,3,4\}$. Note that, for example, $\{1,4,5\}$ is a cut set, but it is not minimal. The minimal path sets are $\{1,4\},\{2,5\}$, and $\{3,5\}$. In the following we will refer to this example as the "5-components example."

Fig. 2.4. Example of a reliability block diagram

# Computing System Reliability 

Let $X_{i}$ be independent binary random variables representing the state of the $i$ th component at a given point in time, $i=1,2, \ldots, n$. Let

$$
\begin{aligned}
p_{i} & =P\left(X_{i}=1\right) \\
q_{i} & =P\left(X_{i}=0\right) \\
h & =h(\mathbf{p})=P(\Phi(\mathbf{X})=1) \\
g & =g(\mathbf{q})=P(\Phi(\mathbf{X})=0)
\end{aligned}
$$

where $\mathbf{p}=\left(p_{1}, p_{2}, \ldots, p_{n}\right), \mathbf{q}=\left(q_{1}, q_{2}, \ldots, q_{n}\right)$, and $\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. The probabilities $p_{i}$ and $q_{i}$ are referred to as the reliability and unreliability of component $i$, respectively, and $h$ and $g$ the corresponding reliability and unreliability of the system.

The problem is to compute the system reliability $h$ given the component reliabilities $p_{i}$. Often it will be more efficient to let the starting point of the calculation be the unreliabilities. Note that $h+g=1$ and $p_{i}+q_{i}=1$.

Before we present methods for computation of system reliability for a general structure, we will look closer into some special cases. We start with the series structure.

Example 2.9. (Reliability of a series structure). For a series structure the system functioning means that all the components function, hence

$$
\begin{aligned}
h & =P(\Phi(\mathbf{X})=1)=P\left(\prod_{i=1}^{n} X_{i}=1\right) \\
& =P\left(X_{1}=1, X_{2}=1, \ldots, X_{n}=1\right) \\
& =\prod_{i=1}^{n} P\left(X_{i}=1\right)=\prod_{i=1}^{n} p_{i}
\end{aligned}
$$Example 2.10. (Reliability of a parallel structure). The reliability of a parallel structure is given by

$$
h=1-\prod_{i=1}^{n}\left(1-p_{i}\right)=\prod_{i=1}^{n} p_{i}
$$

The proof of (2.4) is analogous to the proof of (2.3).
Example 2.11. (Reliability of a $k$-out-of- $n$ structure). The reliability of a $k$-out-of- $n$ structure of independent components, which all have the same reliability $p$, equals

$$
h=\sum_{i=k}^{n}\binom{n}{i} p^{i}(1-p)^{n-i}
$$

This formula holds since $\sum_{i=1}^{n} X_{i}$ has a binomial distribution with parameters $n$ and $p$ under the given assumptions. The case that the component reliabilities are not equal is treated later.

Next we look at an arbitrary series-parallel structure. By using the calculation formulae for a series structure and a parallel structure it is relatively straightforward to calculate the reliability of combinations of series and parallel structures, provided that each component is included in just one such structure. Let us consider an example.

Example 2.12. Consider again the reliability block diagram in Fig. 2.4. The system can be viewed as a parallel structure of two independent modules: the structure comprising the components 1 and 4 , and the structure comprising the components 2,3 , and 5 . The reliability of the former structure equals $p_{1} p_{4}$, whereas the reliability of the latter equals $\left(1-\left(1-p_{2}\right)\left(1-p_{3}\right)\right) p_{5}$. Thus the system reliability is given by

$$
h=1-\left\{1-p_{1} p_{4}\right\}\left\{1-\left(1-\left(1-p_{2}\right)\left(1-p_{3}\right)\right) p_{5}\right\}
$$

Assuming that $q_{1}=q_{2}=q_{3}=0.02$ and $q_{4}=q_{5}=0.01$, this formula gives $h=0.9997$, i.e., $g=3 \cdot 10^{-4}$.

If, for example, a 2 -out-of- 3 structure of independent components with the same reliability $p$ is in series with the above system, the total system reliability will be as above multiplied by the reliability of the 2 -out-of- 3 structure, which equals

$$
\binom{3}{2} p^{2}(1-p)+\binom{3}{3} p^{3}(1-p)^{0}=3 p^{2}(1-p)+p^{3}
$$

Now consider a general monotone structure. Computation of system reliability for complex systems might be a formidable task (in fact, impracticable in some cases) unless an efficient method (algorithm) is used. Developing such methods is therefore an important area of research within reliability theory.There exist a number of methods for reliability computation of a general structure. Many of these methods are based on the minimal cut (path) sets. For smaller systems the so-called inclusion-exclusion method may be applied, but this method is primarily a method for approximate calculations for systems that are either very reliable or unreliable.

Inclusion-Exclusion Method. Let $A_{j}$ be the event that minimal cut set $K_{j}$ is not functioning, $j=1,2, \ldots, k$. Then clearly,

$$
P\left(A_{j}\right)=\prod_{i \in K_{j}} q_{i}
$$

and

$$
g=P\left(\bigcup_{j=1}^{k} A_{j}\right)
$$

Furthermore, let

$$
\begin{aligned}
w_{1} & =\sum_{j=1}^{k} P\left(A_{j}\right) \\
w_{2} & =\sum_{i<j} P\left(A_{i} \bigcap A_{j}\right) \\
& \vdots \\
w_{r} & =\sum_{1 \leq i_{1}<i_{2}<\cdots<i_{r} \leq k} P\left(\bigcap_{j=1}^{r} A_{i_{j}}\right)
\end{aligned}
$$

Then the well-known inclusion-exclusion formula states that

$$
g=w_{1}-w_{2}+w_{3}-\cdots+(-1)^{k+1} w_{k}
$$

and for $r \leq k$

$$
\begin{aligned}
& g \leq w_{1}-w_{2}+w_{3}-\cdots+w_{r}, \quad r \text { odd } \\
& g \geq w_{1}-w_{2}+w_{3}-\cdots-w_{r}, \quad r \text { even. }
\end{aligned}
$$

Although in general it is not true that the upper bounds decrease and the lower bounds increase, in practice it may be necessary to calculate only a few $w_{r}$ terms to obtain a close approximation. If the component unreliabilities $q_{i}$ are small, i.e., the reliabilities $p_{i}$ are large, then the $w_{2}$ term will usually be negligible compared to $w_{1}$, such that $g \approx w_{1}$. Note that $w_{1}$ is an upper bound for $g$. By using $w_{1}$ as an estimate for the system unreliability, we will overestimate the system unreliability. In most cases, such an underestimation of reliability is preferable compared to an overestimation of reliability.

With a large number of minimal cut sets, the exact calculation using (2.5) will be extensive. The number of terms in the sum in $w_{r}$ equals $\binom{k}{r}$. Thus the total number of terms is

$$
\sum_{r=1}^{k}\binom{k}{r}=(1+1)^{k}-1=2^{k}-1
$$Example 2.13. (Continuation of Examples 2.8 and 2.12). The problem is to calculate the unreliability of the 5 -components system of Fig. 2.4 by means of the approximation method described above. We assume that $q_{1}=q_{2}=$ $q_{3}=0.02$ and $q_{4}=q_{5}=0.01$. We find that $w_{1}=3 \cdot 10^{-4}$, which means that $g \approx 3 \cdot 10^{-4}$. It is intuitively clear that the error term by using this approximation will not be significant. Calculating $w_{2}$ confirms this:

$$
\begin{aligned}
w_{2} & =q_{1} q_{4} q_{5}+q_{1} q_{2} q_{3} q_{5}+q_{1} q_{2} q_{3} q_{4} q_{5}+q_{1} q_{2} q_{3} q_{4} q_{5}+q_{2} q_{3} q_{4} q_{5}+q_{1} q_{2} q_{3} q_{4} \\
& =2.2 \cdot 10^{-6}
\end{aligned}
$$

There exist also other bounds and approximations for the system reliability. For example, it can be shown that

$$
1-\prod_{j=1}^{k}\left(1-\prod_{i \in K_{j}} q_{i}\right)=1-\prod_{j=1}^{k} \prod_{i \in K_{j}} p_{i}
$$

is an upper bound for $g$, and a good approximation for small values of the component unreliabilities $q_{i}$; see Barlow and Proschan [32], p. 35. This bound is always as good as or better than $w_{1}$. In the following we sketch some alternative methods for reliability computation.

# Method Using the Minimal Cut Set Representation of the Structure Function. Using 

$$
\Phi(\mathbf{X})=\prod_{j=1}^{k} \prod_{i \in K_{j}} X_{i}
$$

and by multiplying out the right-hand side of this expression, we can find an exact expression of $h$ (or $g$ ). As an illustration consider a 2 -out-of-3 system. Then

$$
\Phi=\left(X_{1} \coprod X_{2}\right) \cdot\left(X_{1} \coprod X_{3}\right) \cdot\left(X_{2} \coprod X_{3}\right)
$$

and by multiplication we obtain

$$
\Phi=X_{1} \cdot X_{2}+X_{1} \cdot X_{3}+X_{2} \cdot X_{3}-2 \cdot X_{1} \cdot X_{2} \cdot X_{3}
$$

We have used $X_{i}^{r}=X_{i}$ for $r=1,2, \ldots$. It follows by taking expectations that

$$
h=p_{1} p_{2}+p_{1} p_{3}+p_{2} p_{3}-2 p_{1} p_{2} p_{3}
$$

For systems with low reliabilities, it is possible to establish similar results based on the minimal path sets.

State Enumeration Method. Of the direct methods that do not use the minimal cut (path) sets, the state enumeration method is conceptually the simplest. With this method reliability is calculated using

Fig. 2.5. Bridge structure

$$
h=E \Phi(\mathbf{X})=\sum_{\mathbf{x}} \Phi(\mathbf{x}) P(\mathbf{X}=\mathbf{x})=\sum_{\mathbf{x}: \Phi(\mathbf{x})=1} \prod_{i=1}^{n} p_{i}^{x_{i}}\left(1-p_{i}\right)^{1-x_{i}}
$$

This method, however, is not suitable for larger systems, since the number of terms in the sum can be extremely large, up to $2^{n}-1$.

Factoring Method. Of other methods we will confine ourselves to describing the so-called factoring algorithm (pivot-decomposition method). The basic idea of this method is to make a conditional probability argument using the relation

$$
h(\mathbf{p})=p_{i} h\left(1_{i}, \mathbf{p}\right)+\left(1-p_{i}\right) h\left(0_{i}, \mathbf{p}\right)
$$

where $h\left(x_{i}, \mathbf{p}\right)$ equals the reliability of the system given that the state of component $i$ is $x_{i}$. Formula (2.6) follows from the law of total probability. This process repeats until the system comprises only series-parallel structures. To illustrate the method we will give an example.

Example 2.14. Consider a bridge structure as given by the diagram shown in Fig. 2.5. If we first choose to pivot on component 3, formula (2.6) holds with $i=3$. It is not difficult to see that given $x_{3}=1$, the system structure has the form
and that given $x_{3}=0$, the system structure has the form


These two structures are both of series-parallel form, and we see that

$$
\begin{aligned}
& h\left(1_{3}, \mathbf{p}\right)=\left(p_{1} \coprod p_{2}\right)\left(p_{4} \coprod p_{5}\right) \\
& h\left(0_{3}, \mathbf{p}\right)=p_{1} p_{4} \coprod p_{2} p_{5}
\end{aligned}
$$

Thus a formula for the exact computation of $h(\mathbf{p})$ is established. Note that it was sufficient to perform only one pivotal decomposition in this case. If the structure given $x_{3}=1$ had not been in a series-parallel form, we would have had to perform another pivotal decomposition, and so on.

For a monotone structure $\Phi$ we have

$$
\Phi(\mathbf{x} \coprod \mathbf{y}) \geq \Phi(\mathbf{x}) \coprod \Phi(\mathbf{y})
$$

where $\mathbf{x} \coprod \mathbf{y}=\left(x_{1} \coprod y_{1}, \ldots, x_{n} \coprod y_{n}\right)$. This is seen by noting that $\Phi(\mathbf{x} \coprod \mathbf{y})$ is greater than or equal to both $\Phi(\mathbf{x})$ and $\Phi(\mathbf{y})$. It follows from (2.7) that

$$
h\left(\mathbf{p} \coprod \mathbf{p}^{\prime}\right) \geq h(\mathbf{p}) \coprod h\left(\mathbf{p}^{\prime}\right)
$$

for all $\mathbf{0} \leq \mathbf{p} \leq \mathbf{1}$ and $\mathbf{0} \leq \mathbf{p}^{\prime} \leq \mathbf{1}$. These results state that redundancy at the component level is more effective than redundancy at system level. This principle is well known among design engineers. Note that if the system is a parallel system, then equality holds in the above inequalities. If the system is coherent, then equality holds if and only if the system is a parallel system.

# Time Dynamics 

The above theory can be applied to different situations, covering both repairable and nonrepairable systems. As an example, consider a monotone system in a time interval $\left[0, t_{0}\right]$, and assume that the components of the system are "new" at time $t=0$ and that a failed component stays in the failure state for the rest of the time interval. Thus the component is not repaired or replaced. This situation, for example, can describe a system with component failure states that can only be discovered by testing or inspection. We assume that the lifetime of component $i$ is determined by a lifetime distribution $F_{i}(t)$ having failure rate function $\lambda_{i}(t)$. To calculate system reliability at a fixed point in time, i.e., the reliability function at this point, we can proceed asabove with $q_{i}=F_{i}(t)$ and $p_{i}=\bar{F}_{i}(t)$. Thus, for a series system the reliability at time $t$ takes the form

$$
h=\prod_{i=1}^{n} \bar{F}_{i}(t)
$$

But $\bar{F}_{i}(t)$ can be expressed by means of the failure rate $\lambda_{i}(t)$ :

$$
\bar{F}_{i}(t)=e^{-\int_{0}^{t} \lambda_{i}(u) d u}
$$

By putting (2.9) into formula (2.8) we obtain

$$
h=e^{-\int_{0}^{t}\left[\sum_{i=1}^{n} \lambda_{i}(u)\right] d u}
$$

From (2.10) we can conclude that the failure rate of a series structure of independent components equals the sum of the failure rates of the components of the structure. In particular this means that if the components have constant failure rates $\lambda_{i}, i=1,2, \ldots, n$, then the series structure has constant failure rate $\sum \lambda_{i}$.

For a parallel structure we do not have a similar result. With constant failure rates of the components, the system will have a time-dependent failure rate; cf. Example 1.3, p. 6.

# Reliability Importance Measures 

An important objective of many reliability and risk analyses is to identify those components or events that are most important (critical) from a reliability/safety point of view and that should be given priority with respect to improvements. Thus, we need an importance measure. A large number of such measures have been suggested (see Bibliographic Notes, p. 55). Here we briefly describe two measures, Improvement Potential and Birnbaum's measure.

Consider again the 5 -components example (cf. pp. 20, 22, and 24). The unreliability of the system equals

$$
\begin{aligned}
g= & \left\{1-p_{1} p_{4}\right\}\left\{1-p_{5}\left(p_{2}+p_{3}-p_{2} p_{3}\right)\right\} \approx w_{1} \\
w_{1}= & q_{1} q_{5}+q_{4} q_{5}+q_{1} q_{2} q_{3}+q_{2} q_{3} q_{4} \\
= & 0.02 \cdot 0.01+0.01 \cdot 0.01 \\
& +0.02 \cdot 0.02 \cdot 0.02+0.02 \cdot 0.02 \cdot 0.01 \\
= & 3 \cdot 10^{-4} .
\end{aligned}
$$

If we look at the subsystems comprising the minimal cut sets, it is clear from the above expression that subsystems $\{1,5\}$ and $\{4,5\}$ are most important in the sense that they are contributing most to unreliability. To decide which components are most important, we must define more precisely what is meant by important. For example, we might decide to let the component with the highest potential for increasing the system reliability be most important (measure for reliability improvement potential) or the component that has thelargest effect on system reliability by a small improvement of the component reliability (Birnbaum's measure).

Improvement Potential. The following reliability importance measure for component $i, I_{i}^{A}$, is appropriate in a large number of situations, in particular during design:

$$
I_{i}^{A}=h\left(1_{i}, \mathbf{p}\right)-h(\mathbf{p})
$$

where $h(\mathbf{p})$ is the reliability of the system and $h\left(1_{i}, \mathbf{p}\right)$ is the reliability assuming that component $i$ is in the best state 1 . The measure $I_{i}^{A}$ expresses the system reliability improvement potential of the component, in other words, the unreliability that is caused by imperfect performance of component $i$. This measure can be used for all types of reliability definitions, and it can be used for repairable or nonrepairable systems.

For a highly reliable monotone system the measure $I_{i}^{A}$ is equivalent to the well-known Vesely-Fussell importance measure [86]. In fact, in this case $I_{i}^{A}$ is approximately equal to the sum of the unreliabilities of the minimal cut sets that include component $i$, i.e.,

$$
I_{i}^{A} \approx \sum_{j: i \in K_{j}} \prod_{l \in K_{j}} q_{l}
$$

This is seen by applying the inclusion-exclusion formula. This formula states that $1-h(\mathbf{p}) \approx \sum_{j=1}^{k} \prod_{l \in K_{j}} q_{l}$. Putting $q_{i}=0$ in this formula and subtracting, we obtain the desired approximation formula for $I_{i}^{A}$. Note that, like the Vesely-Fussell measure, the measure $I_{i}^{A}$ gives the same importance to all the components of a parallel system, irrespective of component reliabilities, namely, $I_{i}^{A}=\prod_{j=1}^{n} q_{j}$. This is as it should be because each one of the components has the potential of making the system unreliability negligible, for example, by introducing redundancy.

Example 2.15. Computation of $I_{i}^{A}$ for the 5 -components example gives

$$
\begin{aligned}
& I_{1}^{A}=2 \cdot 10^{-4}, I_{2}^{A}=1 \cdot 10^{-5} \\
& I_{3}^{A}=1 \cdot 10^{-5}, I_{4}^{A}=1 \cdot 10^{-4} \\
& I_{5}^{A}=3 \cdot 10^{-4}
\end{aligned}
$$

Thus component 5 is the most important component based on this measure. Components 1 and 4 follow in second and third place, respectively.

Birnbaum's Measure. Birnbaum's measure for the reliability importance of component $i, I_{i}^{B}$, is defined by

$$
I_{i}^{B}=\frac{\partial h}{\partial p_{i}}
$$Thus Birnbaum's measure equals the partial derivative of the system reliability with respect to $p_{i}$. The approach is well known from classical sensitivity analyses. We see that if $I_{i}^{B}$ is large, a small change in the reliability of component $i$ will give a relatively large change in system reliability.

Birnbaum's measure might be appropriate, for example, in the operation phase where possible improvement actions are related to operation and maintenance parameters. Before looking closer into specific improvement actions of the components, it will be informative to measure the sensitivity of the system reliability with respect to small changes in the reliability of the components.

To compute $I_{i}^{B}$ the following formula is often used:

$$
I_{i}^{B}=h\left(1_{i}, \mathbf{p}\right)-h\left(0_{i}, \mathbf{p}\right)
$$

This formula is established using (2.6), p. 25.
Example 2.16. Using (2.12) we find that

$$
\begin{aligned}
& I_{1}^{B}=1.03 \cdot 10^{-2}=1 \cdot 10^{-2}, I_{2}^{B}=I_{3}^{B}=6 \cdot 10^{-4} \\
& I_{4}^{B}=1.02 \cdot 10^{-2}=1 \cdot 10^{-2}, I_{5}^{B}=3 \cdot 10^{-2}
\end{aligned}
$$

We see that for this example the Birnbaum measure gives the same ranking of the components as the measure $I_{i}^{A}$. However, this is not true in general.

It is not difficult to see that

$$
\begin{aligned}
I_{i}^{B} & =E\left[\Phi\left(1_{i}, \mathbf{X}\right)-\Phi\left(0_{i}, \mathbf{X}\right)\right]=P\left(\Phi\left(1_{i}, \mathbf{X}\right)-\Phi\left(0_{i}, \mathbf{X}\right)=1\right) \\
& =P\left(\Phi\left(1_{i}, \mathbf{X}\right)=1, \Phi\left(0_{i}, \mathbf{X}\right)=0\right)
\end{aligned}
$$

If $\Phi\left(1_{i}, \mathbf{x}\right)-\Phi\left(0_{i}, \mathbf{x}\right)=1$, we call $\left(1_{i}, \mathbf{x}\right)$ a critical path vector and $\left(0_{i}, \mathbf{x}\right)$ a critical cut vector for component $i$. For simplicity, we often say that component $i$ is critical for the system.

Thus we have shown that $I_{i}^{B}$ equals the probability that the system is in a state so that component $i$ is critical for the system. If the components are dependent, this probability is often used as the definition of Birnbaum's measure. Now set $p_{j}=1 / 2$ for all $j \neq i$. Then

$$
I_{i}^{B}=\frac{1}{2^{n-1}} \sum_{(\cdot i, \mathbf{x})}\left[\Phi\left(1_{i}, \mathbf{x}\right)-\Phi\left(0_{i}, \mathbf{x}\right)\right]=\frac{1}{2^{n}} \sum_{\mathbf{x}}\left[\Phi\left(1_{i}, \mathbf{x}\right)-\Phi\left(0_{i}, \mathbf{x}\right)\right]
$$

This quantity is used as a measure of the structural importance of component $i$.

Some Comments on the Use of Importance Measures. The two importance measures presented in this section can be useful tools in the system optimization process/system improvement process. This process can be described as follows:1. Identify the most important units by means of the chosen importance measure
2. Identify possible improvement actions/measures for these units
3. Estimate the effect on reliability by implementing the measure
4. Perform cost evaluations
5. Make an overall evaluation and take a decision.

The importance measure to be used in a particular case depends on the characteristics we want the measure to reflect. Undoubtedly, different situations call for different importance measures. In a design phase the system reliability improvement potential $I_{1}^{A}$ might be the most informative measure, but for a system with frozen design, the Birnbaum measure might be more informative, since this measure reflects how small component reliability improvements affect system reliability.

# Dependent Components 

In the following some remarks on systems with dependent components are made. A more systematic treatment concerning copula models can be found in the last subsection of this chapter.

One of the most difficult tasks in reliability engineering is to analyze dependent components (often referred to as common mode failures). It is difficult to formulate the dependency in a mathematically stringent way and at the same time obtain a realistic model and to provide data for the model. Whether we succeed in incorporating a "correct" contribution from common mode failures is very much dependent on the modeling ability of the analyst. By defining the components in a suitable way, it is often possible to preclude dependency. For example, common mode failures that are caused by a common external cause can be identified and separated out so that the components can be considered as independent components. Another useful method for "elimination" of dependency is to redefine components. For example, instead of including a parallel structure of dependent components in the system, this structure could be represented by one component. Of course, this does not remove the dependency, but it moves it to a lower level of the analysis. Special techniques, such as Markov modeling, can then be used to analyze the parallel structure itself, or we can try to estimate/assign reliability parameters directly for this new component.

Although it is often possible to "eliminate" dependency between components by proper modeling, it will in many cases be required to establish a model that explicitly takes into account the dependency. Refer to Chap. 3 for examples of such models.

Another way of taking into account dependency is to obtain bounds to the system reliability, assuming that the components are associated and not necessarily independent. Association is a type of positive dependency, for example, as a result of components supporting loads. The precise mathematical definition is as follows (cf. [32]):Definition 2.17. Random variables $T_{1}, T_{2}, \ldots, T_{n}$ are associated if

$$
\operatorname{cov}[f(\mathbf{T}), g(\mathbf{T})] \geq 0
$$

for all pairs of increasing binary functions $f$ and $g$.
A number of results are established for associated components, for example, the following inequalities:

$$
\max _{1 \leq j \leq s} \prod_{i \in S_{j}} p_{i} \leq h \leq 1-\max _{1 \leq j \leq k} \prod_{i \in K_{j}} q_{i}
$$

where $S_{j}$ equals the $j$ th minimal path set, $j=1,2, \ldots, s$ and $K_{j}$ equals the $j$ th minimal cut set, $j=1,2, \ldots, k$. This method usually leads to very wide intervals for the reliability.

# 2.1.2 Multistate Monotone Systems 

In this section parts of the theory presented in Sect.2.1.1 will be generalized to include multistate systems where components and system are allowed to have an arbitrary (finite) number of states/levels. Multistate monotone systems are used to model, e.g., production and transportation systems for oil and gas, and power transmission systems.

We consider a system comprising $n$ components, numbered consecutive from 1 to $n$. As in the binary case, $x_{i}$ represents the state of component $i$, $i=1,2, \ldots, n$, but now $x_{i}$ can be in one out of $M_{i}+1$ states,

$$
x_{i 0}, x_{i 1}, x_{i 2}, \ldots, x_{i M_{i}} \quad\left(x_{i 0}<x_{i 1}<x_{i 2}<\cdots<x_{i M_{i}}\right)
$$

The set comprising these states is denoted $S_{i}$. The states $x_{i j}$ represent, for example, different levels of performance, from the worst, $x_{i 0}$, to the best, $x_{i M_{i}}$. The states $x_{i 0}, x_{i 1}, \ldots, x_{i, M_{i}-1}$ are referred to as the failure states of the components.

Similarly, $\Phi=\Phi(\mathbf{x})$ denotes the state (level) of the system. The various values $\Phi$ can take are denoted

$$
\Phi_{0}, \Phi_{1}, \ldots, \Phi_{M} \quad\left(\Phi_{0}<\Phi_{1}<\cdots<\Phi_{M}\right)
$$

We see that if $M_{i}=1, i=1,2, \ldots, n$, and $M=1$, then the model is identical with the binary model of Sect.2.1.1.

Definition 2.18. (Monotone system). A system is said to be monotone if

1. its structure function $\Phi$ is nondecreasing in each argument, and
2. $\Phi\left(x_{10}, x_{20}, \ldots, x_{n 0}\right)=\Phi_{0} \quad$ and $\quad \Phi\left(x_{1 M_{1}}, x_{2 M_{2}}, \ldots, x_{n M_{n}}\right)=\Phi_{M}$.

In the following we will restrict attention to monotone systems. As usual, we use the convention that $\left(x_{1}, x_{2}, \ldots, x_{n}\right)>\left(z_{1}, z_{2}, \ldots, z_{n}\right)$ means that $x_{i} \geq$ $z_{i}, i=1,2, \ldots, n$, and there exists at least one $i$ such that $x_{i}>z_{i}$.

Fig. 2.6. A simple example of a flow network

Definition 2.19. (Minimal cut vector). A vector $\mathbf{z}$ is a cut vector to level $c$ if $\Phi(\mathbf{z})<c$. A cut vector to level $c, \mathbf{z}$, is minimal if $\Phi(\mathbf{x}) \geq c$ for all $\mathbf{x}>\mathbf{z}$.

Definition 2.20. (Minimal path vector). A vector $\mathbf{y}$ is a path vector to level $c$ if $\Phi(\mathbf{y}) \geq c$. A path vector to level $c, \mathbf{y}$, is minimal if $\Phi(\mathbf{x})<c$ for all $\mathbf{x}<\mathbf{y}$.

Example 2.21. Figure 2.6 shows a simple example of a flow network model. The system comprises three components. Flow (gas/oil) is transmitted from $a$ to $b$. The components 1 and 2 are binary, whereas component 3 can be in one out of three states: 0,1 , or 2 . The states of the components are interpreted as flow capacity rates for the components. The state/level of the system is defined as the maximum flow that can be transmitted from $a$ to $b$, i.e.,

$$
\Phi=\Phi(\mathbf{x})=\min \left\{x_{1}+x_{2}, x_{3}\right\}
$$

If, for example, the component states are $x_{1}=0, x_{2}=1$, and $x_{3}=2$, then the flow throughput equals 1 , i.e., $\Phi=\Phi(0,1,2)=1$. The possible system levels are 0,1 , and 2 . We see that $\Phi$ is a multistate monotone system. The minimal cut vectors and path vectors are as follows:

System level 2
Minimal cut vectors: $(0,1,2),(1,0,2)$, and $(1,1,1)$
Minimal path vectors : $(1,1,2)$

System level 1
Minimal cut vectors: $(0,0,2)$ and $(1,1,0)$
Minimal path vectors : $(0,1,1)$ and $(1,0,1)$.

# Computing System Reliability 

Assume that the state $X_{i}$ of the $i$ th component is a random variable, $i=$ $1,2, \ldots, n$. Let$$
\begin{aligned}
& p_{i j}=P\left(X_{i}=x_{i j}\right) \\
& h_{j}=P\left(\Phi(\mathbf{X}) \geq \Phi_{j}\right) \\
& a=E \Phi(\mathbf{X}) / \Phi_{M}=\sum_{j} \Phi_{j} P\left(\Phi(\mathbf{X})=\Phi_{j}\right) / \Phi_{M}
\end{aligned}
$$

We call $h_{j}$ the reliability of the system at system level $j$. For the flow network example above, $a$ represents the expected throughput (flow) relatively to the maximum throughput (flow) level.

The problem is to compute $h_{j}$ for one or more values of $j$, and $a$, based on the probabilities $p_{i j}$. We assume that the random variables $X_{i}$ are independent.

Example 2.22. (Continuation of Example 2.21). Assume that

$$
\begin{aligned}
& p_{i 1}=1-p_{i 0}=0.96, i=1,2 \\
& p_{32}=0.97, p_{31}=0.02, p_{30}=0.01
\end{aligned}
$$

Then by simple probability calculus we find that

$$
\begin{aligned}
h_{2} & =P\left(X_{1}=1, X_{2}=1, X_{3}=2\right) \\
& =0.96 \cdot 0.96 \cdot 0.97=0.894 \\
h_{1} & =P\left(X_{1}=1 \cup X_{2}=1, X_{3} \geq 1\right) \\
& =P\left(X_{1}=1 \cup X_{2}=1\right) P\left(X_{3} \geq 1\right) \\
& =\left\{1-P\left(X_{1}=0\right) P\left(X_{2}=0\right)\right\} P\left(X_{3} \geq 1\right) \\
& =0.9984 \cdot 0.99=0.988 \\
a & =(0.094 \cdot 1+0.894 \cdot 2) / 2=0.941
\end{aligned}
$$

For the above example it is easy to calculate the system reliability directly by using elementary probability rules. For larger systems it will be very timeconsuming (in some cases impossible) to perform these calculations if special techniques or algorithms are not used. If the minimal cut vectors or path vectors for a specific level are known, the system reliability for this level can be computed exactly, using, for example, the algorithm described in [17]. For highly reliable systems, which are most common in practice, simple approximations can be used as described in the following.

Analogous to the binary case, approximations can be established based on the inclusion-exclusion method. For example, we have

$$
1-h_{j}=\sum_{r} \prod_{i=1}^{n} P\left(X_{i} \leq z_{i}^{r}\right)-\epsilon
$$

where $\left(z_{1}^{r}, z_{2}^{r}, \ldots, z_{n}^{r}\right)$ represents the $r$ th cut vector for level $j$ and $\epsilon$ is a positive error term satisfying

$$
\epsilon \leq \sum_{r<l} \prod_{i=1}^{n} P\left(X_{i} \leq \min \left\{z_{i}^{r}, z_{i}^{l}\right\}\right)
$$Example 2.23. (Continuation of Example 2.22). If we use (2.13) to calculate $h_{j}$, we obtain

$$
\begin{array}{ll}
h_{2} \approx 1-(0.04 \cdot 1 \cdot 1+1 \cdot 0.04 \cdot 1+1 \cdot 1 \cdot 0.03)=0.890 \\
h_{1} \approx 1-(0.04 \cdot 0.04 \cdot 1+1 \cdot 1 \cdot 0.01) & =0.988 \\
a \approx(1 \cdot 0.098+2 \cdot 0.890) / 2 & =0.939
\end{array}
$$

We can conclude that the approximations are quite good for this example.
The problem of determining the probabilities $p_{i j}$ will, as in the binary case, depend on the particular situation considered. Often it will be appropriate to define $p_{i j}$ by the limiting availabilities of the component, cf. Chap. 4.

# Discussion 

The traditional reliability theory based on a binary approach has recently been generalized by allowing components and system to have an arbitrary finite number of states. For most reliability applications, binary modeling should be sufficiently accurate, but for certain types of applications, such as gas and oil production and transportation systems and telecommunication, a multistate approach is usually required for the system and components. In a gas transportation system, for example, the state of the system is defined as the rate of delivered gas, and in most cases a binary model ( $100 \%, 0 \%$ ) would be a poor representation of the system. A component in such a system may represent a compressor station comprising a certain number $(M)$ of compressor units in parallel. The states of the component equal the capacity levels corresponding to $M$ compressor units running, $M-1$ compressor units running, and so on.

There also exists a number of reliability importance measures for multistate systems (see Bibliographic Notes, p. 55). Many of these measures represent natural generalizations of importance measures of binary systems. We see, for example, that the measure $I^{A}$ can easily be extended to multistate models. For the Birnbaum measure, it is not so straightforward to generalize the measure. Several measures have been proposed as, for example, the $r, s$-reliability importance $I_{i}^{r, s}$ of component $i$, which is given by

$$
I_{i}^{r, s}=P\left(\Phi\left(r_{i}, \mathbf{X}\right) \geq \Phi_{k}\right)-P\left(\Phi\left(s_{i}, \mathbf{X}\right) \geq \Phi_{k}\right)
$$

where $\Phi\left(j_{i}, \mathbf{X}\right)$ equals the state of the system given that $X_{i}=x_{i j}$.

### 2.2 Basic Notions of Aging

In this section we introduce and recapitulate some properties of lifetime distributions. Let $T$ be a positive random variable with distribution function $F: T \sim F$, i.e., $P(T \leq t)=F(t)$. If $F$ has a density $f$, then $\lambda(t)=f(t) / \bar{F}(t)$is the failure or hazard rate, where as usual $\bar{F}(t)=1-F(t)$ denotes the survival probability. Here and in the following we sometimes simplify the notation and define a mapping by its values to avoid constructions like $\lambda: D \rightarrow \mathbb{R}_{+}, D \subset \mathbb{R} \backslash\left\{t \in \mathbb{R}_{+}: \bar{F}(t)=0\right\}, t \mapsto \lambda(t)=f(t) / \bar{F}(t)$, if there is no fear of ambiguity. Interpreting $T$ as the lifetime of some component or system, the failure rate measures the proneness to failure at time $t: \lambda(t) \triangle t \approx P(T \leq t+\triangle t \mid T>t)$. The well-known relation

$$
\bar{F}(t)=\exp \left\{-\int_{0}^{t} \lambda(s) d s\right\}
$$

shows that $F$ is uniquely determined by the failure rate. One notion of aging could be an increasing failure rate (IFR). However, this IFR property is in some cases too strong and other intuitive notions of aging have been suggested. Among them are the increasing failure rate average (IFRA) property and the notions of new better than used (NBU) and new better than used in expectation (NBUE). In the following subsection these concepts are introduced formally and the relationships among them are investigated.

Furthermore, these notions should be applied to complex systems. If we consider the time dynamics of such systems, we want to investigate how the reliability of the whole system changes in time if the components have one of the mentioned aging properties.

Another question is how different lifetime (random) variables and their corresponding distributions can be compared. This leads to notions of stochastic ordering. The comparison of the lifetime distribution with the exponential distribution leads to useful estimates of the system reliability.

# 2.2.1 Nonparametric Classes of Lifetime Distributions 

We first define the IFR and decreasing failure rate (DFR) properties of a lifetime distribution $F$ by means of the conditional survival probability

$$
P(T>t+x \mid T>t)=\bar{F}(t+x) / \bar{F}(t)
$$

Definition 2.24. Let $T$ be a positive random variable with $T \sim F$.
(i) $F$ is an IFR distribution if $\bar{F}(t+x) / \bar{F}(t)$ is nonincreasing in $t$ on the domain of the distribution for each $x \geq 0$.
(ii) $F$ is a $D F R$ distribution if $\bar{F}(t+x) / \bar{F}(t)$ is nondecreasing in $t$ on the domain of the distribution for each $x \geq 0$.

In the following we will restrict attention to the "increasing" part in the definition of the aging notion. The "decreasing part" can be treated analogously. The IFR property says that with increasing age the probability of surviving $x$ further time units decreases. This definition does not make useof the existence of a density $f$ (failure rate $\lambda$ ). But if a density exists, then the IFR property is equivalent to a nondecreasing failure rate, which can immediately be seen as follows. From

$$
\lambda(t)=\lim _{x \rightarrow 0+} \frac{1}{x}\left\{1-\frac{\bar{F}(t+x)}{\bar{F}(t)}\right\}
$$

we obtain that the IFR property implies that $\lambda$ is nondecreasing. Conversely, if $\lambda$ is nondecreasing, then we can conclude that

$$
P(T>t+x \mid T>t)=\exp \left\{-\int_{t}^{t+x} \lambda(s) d s\right\}
$$

is nonincreasing, i.e., $F$ is IFR. If $F$ has the IFR property, then it is continuous for all $t<t^{*}=\sup \left\{t \in \mathbb{R}_{+}: \bar{F}(t)>0\right\}$ (possibly $t^{*}=\infty$ ) and a jump can only occur at $t^{*}$ if $t^{*}<\infty$. This can be directly deduced from the IFR definition.

It seems reasonable that the aging properties of the components of a monotone structure are inherited by the system. However, the example of a parallel structure with two independent components, the lifetimes of which are distributed $\operatorname{Exp}\left(\lambda_{1}\right)$ and $\operatorname{Exp}\left(\lambda_{2}\right)$, respectively, shows that in this respect the IFR property is too strong. As was pointed out in Example 1.3, p. 6, for $\lambda_{1} \neq \lambda_{2}$, the failure rate of the system lifetime is increasing in $\left(0, t^{*}\right)$ and decreasing in $\left(t^{*}, \infty\right)$ for some $t^{*}>0$, i.e., constant component failure rates lead in this case to a nonmonotone system failure rate. To characterize the class of lifetime distributions of systems with IFR components we are led to the IFRA property. We use the notation

$$
\Lambda(t)=\int_{0}^{t} \frac{d F(s)}{1-F(s-)}
$$

which is the accumulated failure rate. The distribution function $F$ is uniquely determined by $\Lambda$ and the relation is given by

$$
\bar{F}(t)=\exp \left\{-\Lambda^{c}(t)\right\} \prod_{s \leq t}(1-\Delta \Lambda(s))
$$

for all $t$ such that $\Lambda(t)<\infty$, where $\Delta \Lambda(s)=\Lambda(s)-\Lambda(s-)$ is the jump height at time $s$ and $\Lambda^{c}(t)=\Lambda(t)-\sum_{s \leq t} \Delta \Lambda(s)$ is the continuous part of $\Lambda$ (cf. [2], p. 91 or [115], p. 436). In the case that $F$ is continuous, we obtain the simple exponential formula $\bar{F}(t)=\exp \{-\Lambda(t)\}$ or $\Lambda(t)=-\ln \bar{F}(t)$.
Definition 2.25. A distribution $F$ is IFRA if $-(1 / t) \ln \bar{F}(t)$ is nondecreasing in $t>0$ on $\left\{t \in \mathbb{R}_{+}: \bar{F}(t)>0\right\}$.
Remark 2.26. (i) The "decreasing" analog is denoted DFRA.
(ii) If $F$ is IFRA, then $(\bar{F}(t))^{1 / t}$ is nonincreasing, which is equivalent to

$$
\bar{F}(\alpha t) \geq(\bar{F}(t))^{\alpha}
$$

for $0 \leq \alpha \leq 1$ and $t \geq 0$.Next we will introduce two aging notions that are related to the residual lifetime of a component of age $t$. Let $T \sim F$ be a positive random variable with finite expectation. Then the distribution of the remaining lifetime after $t \geq 0$ is given by

$$
P(T-t>x \mid T>t)=\frac{\bar{F}(x+t)}{\bar{F}(t)}
$$

with expectation

$$
\mu(t)=E[T-t \mid T>t]=\frac{1}{\bar{F}(t)} \int_{0}^{\infty} \bar{F}(x+t) d x=\frac{1}{\bar{F}(t)} \int_{t}^{\infty} \bar{F}(x) d x
$$

for $0 \leq t<t^{*}=\sup \left\{t \in \mathbb{R}_{+}: \bar{F}(t)>0\right\}$. The conditional expectation $\mu(t)$ is called mean residual life at time $t$.

Definition 2.27. Let $T \sim F$ be a positive random variable.
(i) $F$ is $N B U$, if

$$
\bar{F}(x+t) \leq \bar{F}(x) \bar{F}(t) \text { for } x, t \geq 0
$$

(ii) $F$ is $N B U E$, if $\mu=E T<\infty$ and

$$
\mu(t) \leq \mu \text { for } 0 \leq t<t^{*}
$$

Remark 2.28. (i) The corresponding notions for "better" replaced by "worse," NWU and NWUE, are obtained by reversing the inequality signs.
(ii) These properties are intuitive notions of aging. $F$ is NBU means that the probability of surviving $x$ further time units for a component of age $t$ decreases in $t$. For NBUE distributions the expected remaining lifetime for a component of age $t$ is less than the expected lifetime of a new component.

Now we want to establish the relations between these four notions of aging.
Theorem 2.29. Let $T \sim F$ be a positive random variable with finite expectation. Then we have

$$
F \operatorname{IFR} \Rightarrow F \operatorname{IFRA} \Rightarrow F \mathrm{NBU} \Rightarrow F \mathrm{NBUE}
$$

Proof. $F$ IFR $\Rightarrow F$ IFRA: Since an IFR distribution $F$ is continuous for all $t<t^{*}=\sup \left\{t \in \mathbb{R}_{+}: \bar{F}(t)>0\right\}$, the simple exponential formula $\bar{F}(t)=\exp \{-\Lambda(t)\}$ holds true and we see that the IFR property implies that $\exp \{\Lambda(t+x)-\Lambda(t)\}$ is increasing in $t$ for all positive $x$. Therefore $\Lambda$ is convex, i.e., $\Lambda(\alpha t+(1-\alpha) u) \leq \alpha \Lambda(t)+(1-\alpha) \Lambda(u), 0 \leq \alpha \leq 1$. Taking the limit $u \rightarrow 0-$ we have $\Lambda(0-)=0$ and $\Lambda(\alpha t) \leq \alpha \Lambda(t)$, which amounts to $\bar{F}(\alpha t) \geq(\bar{F}(t))^{\alpha}$. But this is equivalent to the IFRA property (see Remark 2.26 above).
$F$ IFRA $\Rightarrow F$ NBU: With the abbreviations $a=-(1 / x) \ln \bar{F}(x)$ and $b=-(1 / y) \ln \bar{F}(y)$ we obtain from the IFRA property for positive $x, y$ that $-(1 /(x+y)) \ln \bar{F}(x+y) \geq a \vee b=\max \{a, b\}$ and$$
-\ln \bar{F}(x+y) \geq(a \vee b)(x+y) \geq a x+b y=-\ln \bar{F}(x)-\ln \bar{F}(y)
$$

But this is the NBU property $\bar{F}(x+y) \leq \bar{F}(x) \bar{F}(y)$.
$F \mathbf{N B U} \Rightarrow F$ NBUE: This inequality follows by integrating the NBU inequality

$$
\bar{F}(t) \mu(t)=\int_{0}^{\infty} \bar{F}(x+t) d x \leq \bar{F}(t) \int_{0}^{\infty} \bar{F}(x) d x=\bar{F}(t) \mu
$$

which completes the proof.
Examples can be constructed which show that none of the above implications can be reversed.

# 2.2.2 Closure Theorems 

In the previous subsection it was mentioned that the lifetime of a monotone system with IFR components need not be of IFR type. This gave rise to the definition of the IFRA class of lifetime distributions, and we will show that this class is closed under forming monotone structures. There are also other reliability operations, among them mixtures of distributions or forming the sum of random variables, and the question arises whether certain distribution classes are closed under these operations. For example, convolutions arise in connection with the addition of lifetimes and cold reserves.

Before we come to the IFRA Closure Theorem we need a preparatory lemma to prove a property of the reliability function $h(\mathbf{p})=P(\Phi(\mathbf{X})=1)$ of a monotone structure.

Lemma 2.30. Let $h$ be the reliability function of a monotone structure. Then $h$ satisfies the inequality

$$
h\left(\mathbf{p}^{\alpha}\right) \geq h^{\alpha}(\mathbf{p}) \text { for } 0<\alpha \leq 1
$$

where $\mathbf{p}^{\alpha}=\left(p_{1}^{\alpha}, \ldots, p_{n}^{\alpha}\right)$.
Proof. We prove the result for binary structures, which are nondecreasing in each argument (nondecreasing structures) but not necessarily satisfy $\Phi(\mathbf{0})=0$ and $\Phi(\mathbf{1})=1$. We use induction by $n$, the number of components in the system. For $n=1$ the assertion is obviously true. The induction step is carried out by means of the pivotal decomposition formula:

$$
h\left(\mathbf{p}^{\alpha}\right)=p_{n}^{\alpha} h\left(1_{n}, \mathbf{p}^{\alpha}\right)+\left(1-p_{n}^{\alpha}\right) h\left(0_{n}, \mathbf{p}^{\alpha}\right)
$$

Now $h\left(1_{n}, \mathbf{p}^{\alpha}\right)$ and $h\left(0_{n}, \mathbf{p}^{\alpha}\right)$ define reliability functions of nondecreasing structures with $n-1$ components. Therefore we have $h\left(\cdot_{n}, \mathbf{p}^{\alpha}\right) \geq h^{\alpha}\left(\cdot_{n}, \mathbf{p}\right)$ and also

$$
h\left(\mathbf{p}^{\alpha}\right) \geq p_{n}^{\alpha} h^{\alpha}\left(1_{n}, \mathbf{p}\right)+\left(1-p_{n}^{\alpha}\right) h^{\alpha}\left(0_{n}, \mathbf{p}\right)
$$The last step is to show that

$$
p_{n}^{\alpha} h^{\alpha}\left(1_{n}, \mathbf{p}\right)+\left(1-p_{n}^{\alpha}\right) h^{\alpha}\left(0_{n}, \mathbf{p}\right) \geq\left(p_{n} h\left(1_{n}, \mathbf{p}\right)+\left(1-p_{n}\right) h\left(0_{n}, \mathbf{p}\right)\right)^{\alpha}
$$

But since $v(x)=x^{\alpha}$ is a concave function for $x \geq 0$, we have

$$
v(x+a)-v(x) \geq v(y+a)-v(y) \text { for } 0 \leq x \leq y, 0 \leq a
$$

Setting $a=p_{n}\left(h\left(1_{n}, \mathbf{p}\right)-h\left(0_{n}, \mathbf{p}\right)\right), x=p_{n} h\left(0_{n}, \mathbf{p}\right)$ and $y=h\left(0_{n}, \mathbf{p}\right)$ yields the desired inequality.

Now we can establish the IFRA Closure Theorem.
Theorem 2.31. If each of the independent components of a monotone structure has an IFRA lifetime distribution, then the system itself has an IFRA lifetime distribution.

Proof. Let $F, F_{i}, i=1, \ldots, n$, be the distributions of the lifetimes of the system and the components, respectively. The IFRA property is characterized by

$$
\bar{F}_{i}(\alpha t) \geq\left(\bar{F}_{i}(t)\right)^{\alpha}
$$

for $0 \leq \alpha \leq 1$ and $t \geq 0$. The distribution $F$ is related to the $F_{i}$ by the reliability function $h$ :

$$
\bar{F}(t)=h\left(\bar{F}_{1}(t), \ldots, \bar{F}_{n}(t)\right)
$$

By Lemma 2.30 above using the monotonicity of $h$ we can conclude that

$$
\begin{aligned}
\bar{F}(\alpha t) & =h\left(\bar{F}_{1}(\alpha t), \ldots, \bar{F}_{n}(\alpha t)\right) \geq h\left(\bar{F}_{1}^{\alpha}(t), \ldots, \bar{F}_{n}^{\alpha}(t)\right) \\
& \geq h^{\alpha}\left(\bar{F}_{1}(t), \ldots, \bar{F}_{n}(t)\right)=\bar{F}^{\alpha}(t)
\end{aligned}
$$

for $0<\alpha \leq 1$. For $\alpha=0$ this inequality holds true since $F(0)=0$. This proves the IFRA property of $F$.

We know that independent IFR components form an IFRA monotone system and hence, if the components have exponentially distributed lifetimes, the system lifetime is of IFRA type. Since constant failure rates are also included in the DFR class, one cannot hope for a corresponding closure theorem for DFRA distributions. However, considering other reliability operations things may change. For example, let $\left\{F_{k}: k \in \mathbb{N}\right\}$ be a family of distributions and $F=\sum_{k=1}^{\infty} p_{k} F_{k}$ be its mixture with respect to some probability distribution $\left(p_{k}\right)$. Then it is known that the DFR and the DFRA property are preserved, i.e., if all $F_{k}$ are $\operatorname{DFR}(\mathrm{A})$, then the mixture $F$ is also $\operatorname{DFR}(\mathrm{A})$ (for a proof of a slightly more general result see [32] p. 103). Of course, by the same argument as above a closure theorem for mixtures cannot hold true for IFRA distributions.

Finally, we state a closure theorem for convolutions. Since a complete proof is lengthy (and technical), we do not present it here; we refer to [32], p. 100, and [139], p. 23.Theorem 2.32. Let $X$ and $Y$ be two independent random variables with IFR distributions. Then $X+Y$ has an IFR distribution.

By induction this property extends to an arbitrary finite number of random variables. This shows, for example, that the Erlang distribution is of IFR type because it is the distribution of the sum of exponentially distributed random variables.

# 2.2.3 Stochastic Comparison 

There are many possibilities to compare random variables or their distributions, respectively, with each other, and a rich literature treats various ways of defining stochastic orders. One of the most important in reliability is the stochastic order. Let $X$ and $Y$ be two random variables. Then $X$ is said to be smaller in the stochastic order, denoted $X \leq_{\mathrm{st}} Y$, if $P(X>t) \leq P(Y>t)$ for all $t \in \mathbb{R}_{+}$. In reliability terms we say that $X$ is stochastically smaller than $Y$, if the probability of surviving a given time $t$ is smaller for $X$ than for $Y$ for all $t$. Note that the stochastic order compares two distributions, the random variables could even be defined on different probability spaces. One main point is now to compare a given lifetime distribution with the exponential one. The reason why we choose the exponential distribution is its simplicity and the special role it plays on the border between the IFR(A) and the $\operatorname{DFR}(\mathrm{A})$ classes. However, it turns out that in general a random variable with an IFR(A) distribution is not stochastically smaller than an exponentially distributed one, but their distributions cross at most once.

Lemma 2.33. Let $T$ be a positive random variable with IFRA distribution $F$ and $x_{p}$ be fixed such that $F\left(x_{p}\right)=p$ ( $p$-quantile). Then for $0<p<1$

$$
\begin{aligned}
& \bar{F}(t) \geq e^{-\alpha t} \text { for } 0 \leq t<x_{p} \text { and } \\
& \bar{F}(t) \leq e^{-\alpha t} \text { for } x_{p} \leq t
\end{aligned}
$$

holds true, where $\alpha=-\frac{1}{x_{p}} \ln (1-p)$.
Proof. For an IFRA distribution $v(t)=(-\ln \bar{F}(t)) / t$ is nondecreasing. Therefore the result follows by noting that $v(t) \leq v\left(x_{p}\right)=\alpha$ for $t<x_{p}$ and $v(t) \geq \alpha$ for $t \geq x_{p}$.

The last lemma compares an IFRA distribution with an exponential distribution with the same $p$-quantile. It is also of interest to compare $F$ having expectation $\mu$ with a corresponding $\operatorname{Exp}(1 / \mu)$ distribution. The easiest way seems to be to set $\alpha=1 / \mu$ in the above lemma. But an IFRA distribution function may have jumps so that there might be no $t$ with $v(t)=1 / \mu$. If, on the other hand, $F$ has the stronger IFR property, then it is continuous for $t<t^{*}=\sup \left\{t \in \mathbb{R}_{+}: \bar{F}(t)>0\right\}$ (possibly $t^{*}=\infty$ ) and a jump can only occur at $t^{*}$ if $t^{*}<\infty$. So we find a value $t_{\mu}$ with $v\left(t_{\mu}\right)=1 / \mu$ excluding the degenerate case $\bar{F}(\mu)=0$, i.e., $t^{*}=\mu$. This leads to the following result.Lemma 2.34. Let $T$ be a positive random variable with IFR distribution $F$, mean $\mu$ and let $t_{\mu}=\inf \left\{t \in \mathbb{R}_{+}:-\frac{1}{t} \ln \bar{F}(t) \geq \frac{1}{\mu}\right\}$. Then

$$
\begin{aligned}
& \bar{F}(t) \geq e^{-\frac{t}{\mu}} \text { for } 0 \leq t<t_{\mu} \\
& \bar{F}(t) \leq e^{-\frac{t}{\mu}} \text { for } t_{\mu} \leq t
\end{aligned}
$$

and $t_{\mu} \geq \mu$ hold true.
Proof. The inequality for the survival probability follows from Lemma 2.33 with $\alpha=1 / \mu$, where in the degenerate case $t^{*}=\mu$ we have $t_{\mu}=t^{*}=\mu$. It remains to show $t_{\mu} \geq \mu$. To this end we first confine ourselves to the continuous case and assume that $F$ has no jump at $t^{*}$. Then $F(T)$ has a uniform distribution on $[0,1]$ and we obtain $E[\ln \bar{F}(T)]=-1$. Now

$$
\frac{\bar{F}(t+x)}{\bar{F}(t)}=\exp \{-(A(t+x)-\Lambda(t))\}
$$

is nonincreasing in $t$ for all $x \geq 0$, which implies that $\Lambda(t)=-\ln \bar{F}(t)$ is convex, and we can apply J.L. Jensen's inequality to yield

$$
1=E[-\ln \bar{F}(T)] \geq-\ln \bar{F}(\mu)
$$

This is tantamount to $-\frac{1}{\mu} \ln \bar{F}(\mu) \leq \frac{1}{\mu}$ and hence $t_{\mu} \geq \mu$, which proves the assertion for continuous $\bar{F}$.

In case $F$ has a jump at $t^{*}$ we can approximate $F$ by continuous distributions. Then $t^{*}$ is finite and all considerations can be carried over to the limit. We omit the details.

Example 2.35. Let $T$ follow a Weibull distribution $\bar{F}(t)=\exp \left\{-t^{\beta}\right\}$ with mean $\mu=\Gamma(1+1 / \beta)$, where $\Gamma$ is the Gamma function. Then clearly $F$ is IFR, if $\beta>1$. Lemma 2.34 yields $\bar{F}(t) \geq \exp \{-t / \mu\}$ for $0 \leq t<t_{\mu}=(1 / \mu)^{1 /(\beta-1)}$ and $t_{\mu} \geq \mu$. Note that in this case $t_{\mu}>\mu$, which extends slightly the wellknown result $\bar{F}(t) \geq \exp \{-t / \mu\}$ for $0 \leq t<\mu$ (see [32] Theorem 6.2, p. 111).

A lot of other bounds for the survival probability can be set up under various conditions (see the references listed in the Bibliographic Notes). Next we want to give one example of how such bounds can be carried over to monotone systems. As an immediate consequence of the last lemma we obtain the following corollary.

Corollary 2.36. Let $h$ be the reliability function of a monotone system with lifetime distribution $F$. If the components are independent with IFR distributions $F_{i}$ and mean $\mu_{i}, i=1, \ldots, n$, then we have

$$
\bar{F}(t) \geq h\left(e^{-t / \mu_{1}}, \ldots, e^{-t / \mu_{n}}\right) \text { for } t<\min \left\{\mu_{1}, \ldots, \mu_{n}\right\}
$$Actually the inequality holds true for $t<\min \left\{t_{\mu_{1}}, \ldots, t_{\mu_{n}}\right\}$. The idea of this inequality is to give a bound on the reliability of the system at time $t$ only based on $h$ and $\mu_{i}$ and the knowledge that the $F_{i}$ are of IFR type. If the reliability function $h$ is unknown, then it could be replaced by that of a series system to yield

$$
\bar{F}(t) \geq h\left(e^{-t / \mu_{1}}, \ldots, e^{-t / \mu_{n}}\right) \geq \prod_{i=1}^{n} e^{-t / \mu_{i}}=\exp \left\{-t \sum_{i=1}^{n} \frac{1}{\mu_{i}}\right\}
$$

for $t<\min \left\{\mu_{1}, \ldots, \mu_{n}\right\}$.
These few examples given here indicate how aging properties lead to bounds on the reliability or survival probability of a single component and how these affect the lifetime of a system comprising independent components.

# 2.3 Copula Models of Complex Systems in Reliability 

### 2.3.1 Introduction to Copula Models

We consider a complex system comprising $n$ components. The lifetimes of the components are described by non-negative random variables $T_{1}$, cdots $T_{n}$, where $T_{i}$ has continuous distribution $F_{i}$ with support $\mathbb{R}_{+}, i=1, \ldots, n$. Usually, the lifetimes are assumed to be stochastically independent. But in a number of cases such an assumption is not likely to hold true, e.g., if all components of a system are exposed to the same environmental conditions or stresses. Therefore, we want to extend the model to possibly dependent lifetimes with joint cumulative distribution function $H$ :

$$
H\left(t_{1}, \ldots, t_{n}\right)=P\left(T_{1} \leq t_{1}, \ldots, T_{n} \leq t_{n}\right)
$$

To investigate the influence of the dependence structure on the system reliability it turns out to be useful to assume that the dependence structure is given by a copula. Such a copula $C$ is defined as an $n$-variate distribution function on the cube $[0,1]^{n}$ with marginals that are uniform distributions on $[0,1]$, i.e.,

1. $C(\mathbf{u})=0$ for any $\mathbf{u} \in[0,1]^{n}$, if at least one coordinate of $\mathbf{u}=\left(u_{1}, \ldots, u_{n}\right)$ is 0 .
2. $C(\mathbf{u})=u_{i}$ for any $\mathbf{u} \in[0,1]^{n}$, if all coordinates of $\mathbf{u}$ are 1 except $u_{i}$.

The link between the joint distribution function $H$ and the marginal distribution functions $F_{i}$ of the random variables $T_{i}$ is given by a copula $C$. According to Sklar's theorem (see Nelsen [127]) for any $n$-variate distribution $H$ with marginals $F_{i}$ there exists an $n$-copula $C$ such that

$$
H\left(t_{1}, \ldots, t_{n}\right)=C\left(F_{1}\left(t_{1}\right), \ldots, F_{n}\left(t_{n}\right)\right)
$$for all $t_{1}, \ldots, t_{n}$. If $F_{1}, \ldots, F_{n}$ are continuous, as it is assumed here, then this copula $C$ is uniquely determined.

As before, we consider a binary monotone system admitting two states: working (coded as 1) and failed (coded as 0 ). The state of the system is uniquely determined by the binary states of the $n$ components, i.r., there is a structure function $\Phi:\{0,1\}^{n} \rightarrow\{0,1\}$ emitting the state of the system according to the states of the components. We consider a monotone system, i.e., we assume that this structure function is monotone in each component and $\Phi(0, \ldots, 0)=0, \Phi(1, \ldots, 1)=1$. Let $X_{t}(i)=I\left(T_{i}>t\right), i=1, \ldots, n$ describe the state of the $i$ th component at time $t, t \in \mathbb{R}_{+}$, where $I$ is the indicator function. Then

$$
F^{S}(t):=P\left(\Phi\left(X_{t}(1), \ldots, X_{t}(n)\right)=0\right)
$$

is the distribution function of the system lifetime. Of course, in addition to the structure function $\Phi$, this distribution also depends on the copula $C$.

One aim is to investigate how the dependence structure determines the lifetime distribution $F^{S}$ of the system and in particular in which way properties such as expectation or quantiles depend on the copula. To this end we need the system lifetime distribution $F^{S}$ to be given explicitly in terms of $\Phi$ and $C$ as follows (see [71]). Let $C$ be an $n$-dimensional copula and $\tilde{C}$ the induced probability measure such that $C\left(t_{1}, \ldots, t_{n}\right)=\tilde{C}\left(\prod_{i=1}^{n}\left[0, t_{i}\right]\right)$. Note that since the support of the copula $C$ is $[0,1]^{n}$ we have $\tilde{C}\left([0,1]^{n}\right)=1$. For $0 \leq s \leq 1$ we denominate the intervals $B_{0}^{s}=[0, s]$ and $B_{1}^{s}=(s, 1]$, where $B_{1}^{1}=\emptyset$.

We introduce the function $G_{\Phi, C}:[0,1]^{n} \rightarrow[0,1]$ with

$$
F^{S}(t):=P\left(\Phi\left(X_{t}(1), \ldots, X_{t}(n)\right)=0\right)=G_{\Phi, C}\left(F_{1}(t), \ldots, F_{n}(t)\right)
$$

to emphasize that the lifetime distribution $F^{S}$ depends on $\Phi$ and on $C$. This function $G_{\Phi, C}$ can be determined as follows (for a proof see [71]).

Theorem 2.37. The system lifetime distribution $F^{S}$ is given for all $t \geq 0$ by

$$
F^{S}(t)=G_{\Phi, C}\left(F_{1}(t), \ldots, F_{n}(t)\right)
$$

where

$$
G_{\Phi, C}\left(t_{1}, \ldots, t_{n}\right):=1-\sum_{\mathbf{x} \in\{0,1\}^{n}} \Phi(\mathbf{x}) \cdot \tilde{C}\left(\prod_{i=1}^{n} B_{x_{i}}^{t_{i}}\right)
$$

Since this formula is rather complex we will explain it in more detail for the case $n=2$ and give some examples.

Let $Y_{1}, Y_{2}$ be random variables each uniformly distributed on $[0,1]$ with joint distribution $C\left(t_{1}, t_{2}\right)=P\left(Y_{1} \leq t_{1}, Y_{2} \leq t_{2}\right), t_{1}, t_{2} \in[0,1]$ and induced probability measure $\tilde{C}$. For the sets $D_{1}=B_{0}^{t_{1}} \times B_{0}^{t_{2}}, D_{2}=B_{0}^{t_{1}} \times B_{1}^{t_{2}}, D_{3}=$ $B_{1}^{t_{1}} \times B_{1}^{t_{2}}, D_{4}=B_{1}^{t_{1}} \times B_{0}^{t_{2}}$ in Fig. 2.7 we get

Fig. 2.7. Example for $n=2$

$$
\begin{aligned}
\tilde{C}\left(D_{1}\right) & =P\left(Y_{1} \leq t_{1}, Y_{2} \leq t_{2}\right)=C\left(t_{1}, t_{2}\right) \\
\tilde{C}\left(D_{2}\right) & =P\left(Y_{1} \leq t_{1}, t_{2} \leq Y_{2} \leq 1\right) \\
& =C\left(t_{1}, 1\right)-C\left(t_{1}, t_{2}\right)=t_{1}-C\left(t_{1}, t_{2}\right) \\
\tilde{C}\left(D_{3}\right) & =P\left(t_{1}<Y_{1} \leq 1, t_{2}<Y_{2} \leq 1\right) \\
& =1-C\left(1, t_{2}\right)-C\left(t_{1}, 1\right)+C\left(t_{1}, t_{2}\right) \\
& =1-t_{2}-t_{1}+C\left(t_{1}, t_{2}\right) \\
\tilde{C}\left(D_{4}\right) & =P\left(t_{1}<Y_{1} \leq 1, Y_{2} \leq t_{2}\right) \\
& =C\left(1, t_{2}\right)-C\left(t_{1}, t_{2}\right)=t_{2}-C\left(t_{1}, t_{2}\right)
\end{aligned}
$$

Example 2.38.
(i) In the case of a parallel system with $n$ components, the structure function is given by $\Phi\left(x_{1}, \ldots, x_{n}\right)=1-\prod_{i=1}^{n}\left(1-x_{i}\right)$, which is 0 if and only if $\mathbf{x}=(0, \ldots, 0)$. Therefore, the sum in $G_{\Phi, C}$ extends over all possible $\mathbf{x}$ except the null vector yielding

$$
G_{\Phi, C}\left(t_{1}, \ldots, t_{n}\right)=1-\left(1-\tilde{C}\left(\prod_{i=1}^{n} B_{0}^{t_{i}}\right)\right)=C\left(t_{1}, \ldots, t_{n}\right)
$$

It follows as to be expected that

$$
F^{S}(t)=G_{\Phi, C}(\mathbf{F}(t))=C\left(F_{1}(t), \ldots, F_{n}(t)\right)=H(t, \ldots, t)
$$

(ii) For a series system with $n$ components, we have $\Phi\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} x_{i}$, which is 1 if and only if $\mathbf{x}=(1, \ldots, 1)$. Hence$$
G_{\Phi, C}\left(t_{1}, \ldots, t_{n}\right)=1-\tilde{C}\left(\prod_{i=1}^{n} B_{1}^{t_{i}}\right)
$$

If we denote $\bar{H}\left(t_{1}, \ldots, t_{n}\right)=P\left(T_{1}>t_{1}, \ldots, T_{n}>t_{n}\right)$ the survival function of $H$ and $\bar{C}$ the $n$-dimensional joint survival function corresponding to $C$, then we get for the lifetime distribution of a series system

$$
F^{S}(t)=1-\bar{H}(t, \ldots, t)=1-\bar{C}\left(F_{1}(t), \ldots, F_{n}(t)\right)
$$

In the special case $n=2$ we have $G_{\Phi, C}=t_{1}+t_{2}-C\left(t_{1}, t_{2}\right)$ yielding

$$
F^{S}(t)=F_{1}(t)+F_{2}(t)-C\left(F_{1}(t), F_{2}(t)\right)
$$

(iii) If the $n$ component lifetimes are independent, then the copula $C$ is the product copula $\prod\left(t_{1}, \ldots, t_{n}\right)=t_{1} \cdots t_{n}$. Thus

$$
G_{\Phi, C}\left(t_{1}, \ldots, t_{n}\right)=1-\sum_{\mathbf{x} \in\{0,1\}^{n}} \Phi(\mathbf{x}) \prod_{i=1}^{n} t_{i}^{1-x_{i}}\left(1-t_{i}\right)^{x_{i}}
$$

The intact probabilities of the components at time $t$ are $\bar{F}_{i}(t)=1-$ $F_{i}(t)=P\left(X_{i}(t)=1\right), i=1, \ldots, n$. The system reliability is then given by

$$
\bar{F}^{S}(t)=\sum_{\mathbf{x} \in\{0,1\}^{n}} \Phi(\mathbf{x}) \prod_{i=1}^{n}\left(\bar{F}_{i}(t)\right)^{x_{i}}\left(F_{i}(t)\right)^{1-x_{i}}
$$

the well-known formula that results from the state enumeration method (see Chap. 2.1, p. 25).

# 2.3.2 The Influence of the Copula on the Lifetime Distribution of the System 

In the following we want to investigate in which way the dependence structure, i.e., the copula, influences one-dimensional properties $q\left(F^{S}\right)$ of the system lifetime distribution $F^{S}(t)$, where the functional $q: D \rightarrow \overline{\mathbb{R}}$ is a mapping from the space $D$ of distribution functions of non-negative random variables to $\overline{\mathbb{R}}=\mathbb{R} \cup\{-\infty, \infty\}$.

Important examples of such functionals are

- the system reliability $R_{t}$ at a fixed time $t$

$$
R_{t}\left(F^{S}\right)=P\left(\Phi\left(X_{t}(1), \ldots, X_{t}(n)\right)=1\right)=1-F^{S}(t)=\bar{F}^{S}(t)
$$

- the expectation $E$

$$
E\left(F^{S}\right)=\int_{0}^{\infty} \bar{F}^{S}(t) d t
$$- the $p$-quantiles $Q_{p}$ of the system lifetime distribution

$$
Q_{p}\left(F^{S}\right)=\inf \left\{t \in \mathbb{R}_{+}: F^{S}(t) \geq p\right\}, 0<p \leq 1
$$

To investigate the influence of the copula on these one-dimensional quantities we first have to compare different multivariate distributions. There are a lot of comparison methods that are presented in some detail in $[123,99]$ and related to copulas in Nelsen [127]. We summarize briefly the notions we need.

We consider $n$ non-negative random variables $T_{1}, \ldots, T_{n}$ with joint distribution function $H$, marginals $F_{1}, \ldots, F_{n}$ and survival function $\bar{H}\left(t_{1}, \ldots, t_{n}\right)=$ $P\left(T_{1}>t_{1}, \ldots, T_{n}>t_{n}\right)$. In the case $n=2$ we have the relation: $\bar{H}\left(t_{1}, t_{2}\right)=$ $1-F_{1}\left(t_{1}\right)-F_{2}\left(t_{2}\right)+H\left(t_{1}, t_{2}\right)$. Now we want to compare two $n$-variate distribution functions $H, G \in D\left(F_{1}, \ldots, F_{n}\right)$, where $D\left(F_{1}, \ldots, F_{n}\right)$ denotes the set of distribution functions with marginals $F_{1}, \ldots, F_{n}$, each with support $\mathbb{R}_{+}$.

Definition 2.39. Let $H, G \in D\left(F_{1}, \ldots, F_{n}\right), n \geq 2$.
(i) $G$ is more positive lower orthant dependent (PLOD) than $H$, written $H \prec_{c L} G$, if $H(\mathbf{t}) \leq G(\mathbf{t})$ for all $\mathbf{t}=\left(t_{1}, \ldots, t_{n}\right) \in \mathbb{R}^{n}$.
(ii) $G$ is more positive upper orthant dependent (PUOD) than $H$, written $H \prec_{c U} G$, if $\bar{H}(\mathbf{t}) \leq \bar{G}(\mathbf{t})$ for all $\mathbf{t}$.
(iii) $G$ is more concordant than $H$, written $H \prec_{c} G$, if both $H(\mathbf{t}) \leq G(\mathbf{t})$ and $\bar{H}(\mathbf{t}) \leq \bar{G}(\mathbf{t})$ hold for all $\mathbf{t}$.

For $n=2$, parts (i) and (ii) of the above definition are equivalent as can be seen from the relation between $H$ and $\bar{H}$. This does not hold true in higher dimensions. To compare two distributions $H, G \in D\left(F_{1}, \ldots, F_{n}\right)$ with fixed marginals it is, of course, enough to compare their corresponding copulas.

For $n=2$ random variables $X, Y$ with continuous distribution functions $F, G$ and copula $C$, there are well-known measures of the degree of dependence such as Kendall's tau $\tau_{X, Y}$ or Spearman's rho $\rho_{X, Y}$, expression which can be expressed in terms of the copula $C$ :

$$
\tau_{X, Y}=4 \iint_{[0,1]^{2}} C(u, v) d C(u, v)-1, \quad \rho_{X, Y}=12 \iint_{[0,1]^{2}} C(u, v) d u d v-3
$$

This shows that monotonicity of copulas with respect to the PLODordering inherits monotonicity of Kendall's tau and Spearman's rho. In a similar way we want to investigate the effect of an increase of dependency on one-dimensional properties $q\left(F^{S}\right)$ of the system lifetime distribution. We cannot hope for results for arbitrary systems, but for parallel and series systems, see Fig. 2.8, we can prove the following theorem. For this we need the usual stochastic order on $D: F \leq_{s} G$ iff $F(t) \geq G(t)$ for all $t \geq 0$.

Fig. 2.8. (a)Parallel and (b)series system

Theorem 2.40. Let the functional $q: D \rightarrow \overline{\mathbb{R}}$ be nondecreasing with respect to the usual stochastic order on $D$ and let $C_{1}$ and $C_{2}$ be two $n$-dimensional copulas.
(i) If for a parallel system $C_{1} \prec_{c L} C_{2}$ then

$$
q\left(F_{C_{2}}^{S}\right) \leq q\left(F_{C_{1}}^{S}\right)
$$

(ii) if for a series system $C_{1} \prec_{c U} C_{2}$ then

$$
q\left(F_{C_{1}}^{S}\right) \leq q\left(F_{C_{2}}^{S}\right)
$$

If $q$ is nonincreasing then the inequalities in (i) and (ii) are reversed.
Proof. (i) For a parallel system, note that according to Example 2(i) it holds that

$$
F_{C_{i}}^{S}(t)=C_{i}\left(F_{1}(t), \ldots, F_{n}(t)\right)
$$

where $i=1,2$ and $F_{1}(t), \ldots, F_{n}(t) \in D$. It is clear that $F_{C_{1}}^{S}(t) \leq F_{C_{2}}^{S}(t)$ for all $t \geq 0$, since $C_{1} \prec_{c L} C_{2}$. That means $F_{C_{2}}^{S} \leq_{s} F_{C_{1}}^{S}$. Because of the monotonicity of $q$ we get the assertion

$$
q\left(F_{C_{2}}^{S}\right) \leq q\left(F_{C_{1}}^{S}\right)
$$

The proof of (ii) is similar: For a series system we have

$$
F_{C_{i}}^{S}(t)=1-\bar{C}_{i}\left(F_{1}(t), \ldots, F_{n}(t)\right)
$$

Therefore, the PUOD-ordering of $C_{i}$ yields $F_{C_{1}}^{S} \leq_{s} F_{C_{2}}^{S}$ and consequently the assertion.

The case of nonincreasing $q$ is obvious.
The above theorem shall be applied to the three functionals mentioned earlier, namely the system reliability $R_{t}\left(F^{S}\right)=\bar{F}^{S}(t)$, the expectation $E\left(F^{S}\right)=$ $\int_{0}^{\infty} \bar{F}^{S}(t) d t$ and the quantile $Q_{p}\left(F^{S}\right):=\inf \left\{t \in \mathbb{R}_{+}: F^{S}(t) \geq p\right\}, 0<p \leq 1$. Note that these functionals are all nondecreasing with respect to the usual stochastic ordering.One is often interested in bounds for these reliability quantities in cases when the marginals are (approximately) known but the dependence structure is unknown. For this we can utilize the so called Fréchet-Hoeffding bounds (see Nelsen [127])

$$
\begin{aligned}
& W\left(u_{1}, \ldots, u_{n}\right)=\max \left\{1-n+\sum_{i=1}^{n} u_{i}, 0\right\} \\
& M\left(u_{1}, \ldots, u_{n}\right)=\min \left\{u_{1}, \ldots, u_{n}\right\}
\end{aligned}
$$

While $M$ itself is a copula, $W$ is for $n \geq 3$ no distribution function. It is known (see Nelsen [127]) that all copulas $C$ lie within these two bounds, i.e.,

$$
W \prec_{c L} C \prec_{c L} M
$$

Using the preceding theorem yields
(i) for a parallel system:

$$
\begin{gathered}
R_{t}\left(F_{M}^{S}\right) \leq R_{t}\left(F_{C}^{S}\right) \leq R_{t}\left(F_{W}^{S}\right) \\
E\left(F_{M}^{S}\right) \leq E\left(F_{C}^{S}\right) \leq E\left(F_{W}^{S}\right) \\
Q_{p}\left(F_{M}^{S}\right) \leq Q_{p}\left(F_{C}^{S}\right) \leq Q_{p}\left(F_{W}^{S}\right)
\end{gathered}
$$

where we used the notation $F_{C}^{S}$ for the system lifetime distribution according to the copula $C$.
(ii) in the case $n=2$ the relation $W \prec_{c U} C \prec_{c U} M$ holds true yielding the inverse inequalities for a series system:

$$
\begin{gathered}
R_{t}\left(F_{W}^{S}\right) \leq R_{t}\left(F_{C}^{S}\right) \leq R_{t}\left(F_{M}^{S}\right) \\
E\left(F_{W}^{S}\right) \leq E\left(F_{C}^{S}\right) \leq E\left(F_{M}^{S}\right) \\
Q_{p}\left(F_{W}^{S}\right) \leq Q_{p}\left(F_{C}^{S}\right) \leq Q_{p}\left(F_{M}^{S}\right)
\end{gathered}
$$

This example provides us with an upper bound $Q_{p}\left(F_{W}^{S}\right)$ and a lower bound $Q_{p}\left(F_{M}^{S}\right)$, respectively, for the quantile $Q_{p}\left(F_{C}^{S}\right)$ of a parallel system. The corresponding bounds for the quantile $Q_{p}\left(F_{C}^{S}\right)$ of a series system are $Q_{p}\left(F_{M}^{S}\right)$ ] and $Q_{p}\left(F_{W}^{S}\right)$, respectively. Note that the lower bound for a parallel system coincides with the upper bound for a series system.

This example verifies also that the stronger the dependence between the component lifetimes in a series system is, the more reliable the system is. But for a parallel system the reverse holds true, the system becomes weaker the stronger the dependence is, always under the assumption that the marginals remain the same.# 2.3.3 Archimedean Copulas 

In general it is not easy to check whether multivariate copulas are PLOD, PUOD, or CONCORDANT ordered. But for an important subclass, the so-called Archimedean copulas, the concordance order can be checked by investigating the properties of generators of Archimedean copulas (see Nelsen [127]). A function $\varphi:[0,1] \rightarrow[0, \infty]$ is a generator (of an $n$-dimensional Archimedean copula), if $\varphi$ is continuous, strictly decreasing, $\varphi(0)=\infty, \varphi(1)=$ 0 and the inverse $\varphi^{-1}$ is completely monotonic, i.e.,

$$
(-1)^{k} \frac{d^{k}}{d t^{k}} \varphi^{-1}(t) \geq 0, t \geq 0, k=0,1,2, \ldots
$$

The function $C:[0,1]^{n} \rightarrow[0,1]$ defined by

$$
C(\mathbf{u})=\varphi^{-1}\left(\varphi\left(u_{1}\right)+\varphi\left(u_{2}\right)+\cdots+\varphi\left(u_{n}\right)\right.
$$

is then an $n$-dimensional Archimedean copula with generator $\varphi$.
Definition 2.41. A function $f: \mathbb{R}_{+} \rightarrow \mathbb{R}$ is subadditive, if for all $x_{1}, \ldots$, $x_{n} \in \mathbb{R}_{+}$

$$
f\left(x_{1}+\cdots+x_{n}\right) \leq f\left(x_{1}\right)+\cdots+f\left(x_{n}\right)
$$

Using this definition the following theorem supplies us with a sufficient and necessary condition to check the concordance order of two Archimedean copulas $C_{1}, C_{2}$ with generators, $\varphi_{1}$, and $\varphi_{2}$, respectively.

Theorem 2.42. Let $C_{1}$ and $C_{2}$ be n-dimensional Archimedean copulas generated by $\varphi_{1}$ and $\varphi_{2}$. Then $C_{1} \prec_{c L} C_{2}$ if and only if $\varphi_{1} \circ \varphi_{2}^{-1}$ is subadditive.

Proof. Let $f=\varphi_{1} \circ \varphi_{2}^{-1}$. The function $f$ is continuous and nondecreasing with $f(0)=\varphi_{1} \circ \varphi_{2}^{-1}(0)=\varphi_{1}(1)=0$.

According to the definition, $C_{1} \prec_{c L} C_{2}$ holds true if and only if for all $x_{1}, \ldots, x_{n} \in[0,1]$

$$
\varphi_{1}^{-1}\left(\varphi_{1}\left(x_{1}\right)+\cdots+\varphi_{1}\left(x_{n}\right)\right) \leq \varphi_{2}^{-1}\left(\varphi_{2}\left(x_{1}\right)+\cdots+\varphi_{2}\left(x_{n}\right)\right)
$$

Inserting $t_{i}=\varphi_{2}\left(x_{i}\right), i=1, \ldots, n,(2.17)$ is equivalent to:

$$
\varphi_{1}^{-1}\left(f\left(t_{1}\right)+\cdots+f\left(t_{n}\right)\right) \leq \varphi_{2}^{-1}\left(t_{1}+\cdots+t_{n}\right)
$$

for all $t_{1}, \ldots, t_{n} \geq 0$.
Applying the strictly decreasing function $\varphi_{1}$ to both sides of (2.18) on gets

$$
f\left(t_{1}+\cdots+t_{n}\right) \leq f\left(t_{1}\right)+\cdots+f\left(t_{n}\right)
$$

This shows the equivalence of the subadditivity of $f=\varphi_{1} \circ \varphi_{2}^{-1}$ and $C_{1} \prec_{c L} C_{2}$.To verify whether $\varphi_{1} \circ \varphi_{2}^{-1}$ is subadditive may still be a challenge. Therefore, we state three sufficient conditions for subadditivity in the following corollary. The elementary proofs can be found in Nelsen [127] for the case $n=2$, which can easily be extended to the general case $n \geq 2$.

Corollary 2.43. Under the assumptions of Theorem $2.42 C_{1} \prec_{c L} C_{2}$ holds true if either of the following conditions is satisfied
(i) $\varphi_{1} \circ \varphi_{2}^{-1}$ is concave;
(ii) $\varphi_{1} / \varphi_{2}$ is nondecreasing on $(0,1)$;
(iii) $\varphi_{1}$ and $\varphi_{2}$ are continuously differentiable on $(0,1)$ and $\varphi_{1}^{\prime} / \varphi_{2}^{\prime}$ is nondecreasing on $(0,1)$.

# 2.3.4 The Expectation of the Lifetime of a Two-Component-System with Exponential Marginals 

As an example we consider a complex system with $n=2$ components with lifetimes $T_{1}, T_{2}$, which are both exponentially distributed with the same parameter $\lambda>0$. To model the dependence we consider the one-parameter Clayton or Pareto family of copulas

$$
C_{\theta}(u, v)=\left[\left(u^{-\theta}+v^{-\theta}-1\right)^{+}\right]^{-1 / \theta}, \theta \in[-1, \infty) \backslash\{0\}
$$

with generator $\varphi_{\theta}(t)=\frac{1}{\theta}\left(t^{-\theta}-1\right)$. Is this family positively ordered in the sense that for $\theta_{1} \leq \theta_{2}$ we have $C_{\theta_{1}} \prec_{c} C_{\theta_{2}}$ ? Note that in the case $n=2$ the PLOD- and PUOD-ordering coincide and are equivalent to the concordant ordering $\prec_{c}$. To check whether the Clayton family is positively ordered we can use Corollary 2.43 part (iii). The generator $\varphi_{\theta}$ is continuously differentiable on $(0,1)$ with $\varphi_{\theta}^{\prime}(t)=-t^{-\theta-1}$. The ratio $\varphi_{\theta_{1}}^{\prime} / \varphi_{\theta_{2}}^{\prime}=t^{\theta_{2}-\theta_{1}}$ is nondecreasing on $(0,1)$ for $\theta_{1} \leq \theta_{2}$ which is sufficient for $C_{\theta_{1}} \prec_{c} C_{\theta_{2}}$, i.e., the degree of dependence increases with $\theta$. The extreme cases $\theta=-1$ and $\theta \rightarrow \infty$ are the Fréchet-Hoeffding bounds $C_{-1}=W$ and $C_{\infty}=M$. The limiting case $\theta \rightarrow 0$ yields the product copula $C_{0}=\prod$ (independence).

## Parallel System

The lifetime $T=T_{1} \vee T_{2}$ of a parallel system has distribution function $F_{C_{\theta}}^{\text {par }}(t)=P(T \leq t)=C_{\theta}\left(F_{1}(t), F_{2}(t)\right)$. Since $C_{\theta}$ is positively ordered (concordance ordering) the expectation

$$
E\left(F_{C_{\theta}}^{\mathrm{par}}\right)=\int_{0}^{\infty}\left(1-C_{\theta}\left(F_{1}(t), F_{2}(t)\right) d t\right.
$$

is decreasing in $\theta$. The extreme and special cases are:- $\theta=-1, C_{-1}=W: E\left(F_{W}^{\text {par }}\right)=\int_{0}^{\infty}\left(1-W\left(F_{1}(t), F_{2}(t)\right) d t\right.$.

In the exponential case $F_{1}(t)=F_{2}(t)=F(t)=1-\exp (-\lambda t)$ we get

$$
E\left(F_{W}^{\mathrm{par}}\right)=\int_{0}^{\infty}\left[1-(2 F(t)-1)^{+}\right] d t=(1+\ln 2) \frac{1}{\lambda}
$$

- $\theta=0, C_{0}=\prod: E\left(F_{\prod}^{\mathrm{par}}\right)=\int_{0}^{\infty}\left(1-F_{1}(t) F_{2}(t)\right) d t$.

In the exponential case $F_{1}(t)=F_{2}(t)=F(t)=1-\exp (-\lambda t)$ we get

$$
E\left(F_{\Pi}^{\mathrm{par}}\right)=\int_{0}^{\infty}\left[1-F^{2}(t)\right] d t=\frac{3}{2} \cdot \frac{1}{\lambda}
$$

- $\theta=\infty, C_{\infty}=M: E\left(F_{M}^{\text {par }}\right)=\int_{0}^{\infty}\left[1-M\left(F_{1}(t), F_{2}(t)\right)\right] d t$.

In the exponential case $F_{1}(t)=F_{2}(t)=F(t)=1-\exp (-\lambda t)$ we get

$$
E\left(F_{M}^{\mathrm{par}}\right)=\int_{0}^{\infty}[1-F(t)] d t=\frac{1}{\lambda}
$$

This shows that in the independence case the second component in this twocomponent parallel system prolongs the mean lifetime by $50 \%$. The most possible prolongation is about $70 \%[\ln 2 \cdot 100]$ in the extreme negative correlation case, whereas, as to be expected, the worst case is a correlation of 1 between the component lifetimes, in which case a second component does not pay.

# Series System 

The lifetime $T=T_{1} \wedge T_{2}$ of a series system has distribution function $F_{C_{g}}^{\text {ser }}(t)=$ $P(T \leq t)=F_{1}(t)+F_{2}(t)-C_{\theta}\left(F_{1}(t), F_{2}(t)\right)$ according to Example 2.38. For the expectation of the system lifetime we get

$$
E\left(F_{C_{\theta}}^{\mathrm{ser}}\right)=E\left(T_{1}\right)+E\left(T_{2}\right)-E\left(T_{1} \vee T_{2}\right)
$$

Therefore, the properties of the expectation can be transferred from the parallel system:

- $\theta=-1, C_{-1}=W: E\left(F_{W}^{\text {ser }}\right)=E\left(T_{1}\right)+E\left(T_{2}\right)-\int_{0}^{\infty}\left(1-W\left(F_{1}(t), F_{2}(t)\right) d t\right.$. In the exponential case we get

$$
E\left(F_{W}^{\mathrm{ser}}\right)=\frac{2}{\lambda}-(1+\ln 2) \frac{1}{\lambda}=(1-\ln 2) \frac{1}{\lambda}
$$

- $\theta=0, C_{0}=\prod: E\left(F_{\Pi}^{\text {ser }}\right)=E\left(T_{1}\right)+E\left(T_{2}\right)-\int_{0}^{\infty}\left(1-F_{1}(t) F_{2}(t)\right) d t$.

In the exponential case we get

$$
E\left(F_{\Pi}^{\mathrm{ser}}\right)=\frac{2}{\lambda}-\frac{3}{2} \cdot \frac{1}{\lambda}=0.5 \cdot \frac{1}{\lambda}
$$

- $\theta=\infty, C_{\infty}=M: E\left(F_{M}^{\text {ser }}\right)=E\left(T_{1}\right)-E\left(T_{2}\right)-\int_{0}^{\infty}\left[1-M\left(F_{1}(t), F_{2}(t)\right)\right] d t$. In the exponential case we get

$$
E\left(F_{M}^{\mathrm{ser}}\right)=\frac{1}{\lambda}
$$

This shows that the expected system lifetime of a series system can be reduced to about $30 \%[(1-\ln 2) \cdot 100]$ of the expected lifetime of one component.# 2.3.5 Marshall-Olkin Distribution 

In this subsection we consider the bivariate Marshall-Olkin (M-O) distribution and investigate the influence of the degree of dependence on the system reliability. The M-O distribution is interesting in so far as it can be interpreted physically. As before we consider a complex system with two components. The system is subject to shocks that are always "fatal" to one or both of the components. The shocks occur at times $Z_{1}, Z_{2}, Z_{12}$, where we differentiate whether only the first, only the second, or both components are destroyed. These random variables are assumed to be independent and exponentially distributed with parameters $\lambda_{1}, \lambda_{2}, \lambda_{12}>0$, respectively. The component lifetimes $T_{1}, T_{2}$ are given by

$$
T_{1}=Z_{1} \wedge Z_{12} \quad \text { and } \quad T_{2}=Z_{2} \wedge Z_{12}
$$

and follow exponential distributions with parameters $\lambda_{1}+\lambda_{12}$ and $\lambda_{2}+\lambda_{12}$.
The joint distribution of $T_{1}$ and $T_{2}$ is called the Marshall-Olkin distribution with joint distribution function:

$$
\begin{aligned}
H\left(t_{1}, t_{2}\right)= & \bar{H}\left(t_{1}, t_{2}\right)+F_{1}\left(t_{1}\right)+F_{2}\left(t_{2}\right)-1 \\
= & \exp \left(-\lambda_{1} t_{1}-\lambda_{2} t_{2}-\lambda_{12}\left(t_{1} \vee t_{2}\right)\right)-\exp \left(-\left(\lambda_{1}+\lambda_{12}\right) t_{1}\right) \\
& -\exp \left(-\left(\lambda_{2}+\lambda_{12}\right) t_{2}\right)+1, \quad t_{1}, t_{2} \geq 0
\end{aligned}
$$

The associated M-O copula is:

$$
C_{\alpha, \beta}\left(u_{1}, u_{2}\right)=\min \left(\left(1-u_{1}\right)^{1-\alpha}\left(1-u_{2}\right),\left(1-u_{1}\right)\left(1-u_{2}\right)^{1-\beta}\right)+u_{1}+u_{2}-1
$$

where $0 \leq u_{1}, u_{2} \leq 1$ and $\alpha=\frac{\lambda_{12}}{\lambda_{1}+\lambda_{12}}, \beta=\frac{\lambda_{12}}{\lambda_{2}+\lambda_{12}}$. As limiting cases we get for the M-O copula

$$
C_{0,0}\left(u_{1}, u_{2}\right)=\lim _{\alpha \rightarrow 0+} C_{\alpha, \beta}\left(u_{1}, u_{2}\right)=\lim _{\beta \rightarrow 0+} C_{\alpha, \beta}\left(u_{1}, u_{2}\right)=\prod\left(u_{1}, u_{2}\right)=u_{1} \cdot u_{2}
$$

and

$$
C_{1,1}\left(u_{1}, u_{2}\right)=M\left(u_{1}, u_{2}\right)=u_{1} \wedge u_{2}
$$

This implies that the limit $\lambda_{1} \rightarrow \infty, \lambda_{2} \rightarrow \infty$ or $\lambda_{12}=0$ result in the product copula, whereas the limit $\lambda_{12} \rightarrow \infty$ or $\lambda_{1}=\lambda_{2}=0$ yield the upper Fréchet-Hoeffding bound. The family $C_{\alpha, \beta}, 0 \leq \alpha, \beta \leq 1$ is positively ordered with respect to the concordance ordering in $\alpha(\beta$ fixed $)$ as well as in $\beta(\alpha$ fixed $)$. For $0 \leq \alpha, \beta \leq 1$ we get

$$
\prod \prec_{c} C_{\alpha, \beta} \prec_{c} M
$$

Now we are in a position to compare the reliabilities $R_{t}\left(F_{C}^{\text {par }}\right)$ and $R_{t}\left(F_{C}^{\text {ser }}\right)$ by means of Theorem 2.40 for different copulas and all $t \geq 0$ :

$$
R_{t}\left(F_{\Pi}^{\mathrm{ser}}\right) \leq R_{t}\left(F_{C_{\alpha, \beta}}^{\mathrm{ser}}\right) \leq R_{t}\left(F_{M}^{\mathrm{ser}}\right)=R_{t}\left(F_{M}^{\mathrm{par}}\right) \leq R_{t}\left(F_{C_{\alpha, \beta}}^{\mathrm{par}}\right) \leq R_{t}\left(F_{\Pi}^{\mathrm{par}}\right)
$$# The Parallel System 

For a parallel system the reliability $R_{t}\left(F_{C_{\alpha, \beta}}^{\text {par }}\right)$ can be explicitly determined as follows

$$
\begin{aligned}
R_{t}\left(F_{C_{\alpha, \beta}}^{\text {par }}\right)= & \bar{F}^{S}(t)=1-C_{\alpha, \beta}\left(F_{1}(t), F_{2}(t)\right) \\
= & 1-\min \left(\left(1-F_{1}(t)\right)^{1-\alpha}\left(1-F_{2}(t)\right),\left(1-F_{1}(t)\right)\left(1-F_{2}(t)\right)^{1-\beta}\right) \\
& -F_{1}(t)-F_{2}(t)+1 \\
= & e^{-\left(\lambda_{1}+\lambda_{12}\right) t}+e^{-\left(\lambda_{2}+\lambda_{12}\right) t}-e^{-\left(\lambda_{1}+\lambda_{2}+\lambda_{12}\right) t}, \quad t \geq 0
\end{aligned}
$$

The reliability functions for different copulas with the same marginals $F_{i}(t)=$ $1-\exp (-10 t), i=1,2$, are displayed graphically in Fig. 2.9.


Fig. 2.9. Reliability functions of a parallel system

The dotted line in Fig. 2.9 represents the independence case with $\lambda_{1}=$ $10, \lambda_{2}=10, \lambda_{12}=0$. The dashed line corresponds to $\lambda_{1}=5, \lambda_{2}=5, \lambda_{12}=5$, whereas the solid line represents the upper Fréchet-Hoeffding bound with $\lambda_{1}=0, \lambda_{2}=0, \lambda_{12}=10$.Figure 2.9 shows that with increasing measure of dependence between the component lifetimes, here increasing $\lambda_{12}$, the reliabilities of a parallel system are decreasing. For example, for $t=0.1$, the reliability is in the range of $R_{0} .1=$ $0.60\left(\lambda_{12}=0\right)$ to $R_{0} .1=0.37\left(\lambda_{12}=10\right)$, i.e. the reliability may decrease to about $60 \%$ of the reliability in the independence case due to correlation between the component lifetimes.

# The Series System 

Analogously we can analyze the reliability of a series system under the same conditions as above. The system reliability is

$$
\begin{aligned}
R_{t}\left(F_{C_{\alpha, \beta}}^{\mathrm{ser}}\right) & =\bar{F}^{S}(t)=1-F_{1}(t)-F_{2}(t)+C_{\alpha, \beta}\left(F_{1}(t), F_{2}(t)\right) \\
& =e^{-\left(\lambda_{1}+\lambda_{2}+\lambda_{12}\right) t}, \quad t \geq 0
\end{aligned}
$$

Figure 2.10 shows the reliability functions for different copulas.


Fig. 2.10. Reliability functions of a series system

As before, the dotted line in Fig. 2.10 represents the independence case with $\lambda_{1}=10, \lambda_{2}=10, \lambda_{12}=0$. The dashed line corresponds to $\lambda_{1}=5, \lambda_{2}=$ $5, \lambda_{12}=5$, whereas the solid line represents the upper Fréchet-Hoeffding bound with $\lambda_{1}=0, \lambda_{2}=0, \lambda_{12}=10$.With increasing measure of dependence the series system becomes better in that the reliability increases. Furthermore, a parallel system is always more reliable than a series with the same marginals. For the upper Fréchet-Hoeffding bound the reliability functions of the parallel and the series system coincide, i.e., the best series systems is as reliable as the worst parallel system. In this limit case the correlation of the component lifetimes is $\rho\left(T_{1}, T_{2}\right)=1$.

Bibliographic Notes. The basic reliability theory of complex systems was developed in the 1960s and 1970s, and is to a large extent covered by the two books of Barlow and Proschan [31] and [32]. Some more recent books in this field are Aven [13] and Høyland and Rausand [90]. Our presentation is based on Aven [13], which also includes the theory of multistate monotone systems. This theory was developed in the 1980s. Refer to Natvig [126] and Aven [17] for further details and references.

For specific references to methods (algorithms) for reliability computations, see [132] and the many papers on this topic appearing in reliability journals each year.

Birnbaum's reliability importance measure presented in Sect. 2.1.1 was introduced by Birnbaum [43]. The improvement potential measure has been used in different contexts, see, e.g., [13, 28]. The measure (2.14) was proposed by Butler [52]. For other references on reliability importance measures, see $[13,28,39,79,86,90,125]$.

Section 2.2, which presents some well-known properties of lifetime distributions, is based on Barlow and Proschan [31], [32], Gertsbakh [74], and Shaked and Shanthikumar [139]. We have not dealt with stochastic comparisons and orders in detail. An overview of this topic with applications in reliability can be found in the book of Shaked and Shanthikumar [139].

Good sources for multivariate comparison methods and dependence concepts are Müller and Stoyan [123], Joe [99] and, in particular related to copulas, Nelsen [127].# Stochastic Failure Models 

A general set-up should include all basic failure time models, should take into account the time-dynamic development, and should allow for different information and observation levels. Thus, one is led in a natural way to the theory of stochastic processes in continuous time, including (semi-) martingale theory, in the spirit of Arjas [3, 4] and Koch [108]. As was pointed out in Chap. 1, this theory is a powerful tool in reliability analysis. It should be stressed, however, that the purpose of this chapter is to present and introduce ideas rather than to give a far reaching excursion into the theory of stochastic processes. So the mathematical technicalities are kept to the minimum level necessary to develop the tools to be used. Also, a number of remarks and examples are included to illustrate the theory. Yet, to benefit from reading this chapter a solid basis in stochastics is required. Section 3.1 summarizes the mathematics needed. For a more comprehensive and in-depth presentation of the mathematical basis, we refer to Appendix A and to monographs such as by Brémaud [50], Dellacherie and Meyer [61, 62], Kallenberg [101], or Rogers and Williams [133].

### 3.1 Notation and Fundamentals

Let $(\Omega, \mathcal{F}, P)$ be the basic probability space. The information up to time $t$ is represented by the pre- $t$-history $\mathcal{F}_{t}$, which contains all events of $\mathcal{F}$ that can be distinguished up to and including time $t$. The filtration $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, which is the family of increasing pre- $t$-histories, is assumed to follow the usual conditions of completeness and right continuity, i.e., $\mathcal{F}_{t} \subset \mathcal{F}$ contains all $P$ negligible sets of $\mathcal{F}$ and $\mathcal{F}_{t}=\mathcal{F}_{t+}=\bigcap_{s>t} \mathcal{F}_{s}$. We define $\mathcal{F}_{\infty}=\bigvee_{t \geq 0} \mathcal{F}_{t}$ as the smallest $\sigma$-algebra containing all events of $\mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$.

If $\left\{X_{j}, j \in J\right\}$ is a family of random variables and $\left\{A_{j}, j \in J\right\}$ is a system of subsets in $\mathcal{F}$, then $\sigma\left(X_{j}, j \in J\right)$ and $\sigma\left(A_{j}, j \in J\right)$, respectively, denote the completion of the generated $\sigma$-field, i.e., the generated $\sigma$-field including all $P$-negligible sets of $\mathcal{F}$. In many cases the information is determined by astochastic process $Z=\left(Z_{t}\right), t \in \mathbb{R}_{+}$, and the corresponding filtration is the so-called natural or internal one, which is generated by this stochastic process and denoted $\mathbb{F}^{Z}=\left(\mathcal{F}_{t}^{Z}\right), t \in \mathbb{R}_{+}, \mathcal{F}_{t}^{Z}=\sigma\left(Z_{s}, 0 \leq s \leq t\right)$. But since it is sometimes desirable to observe one stochastic process on different information levels, it seems more convenient to use filtrations as measures of information. On the basic filtered probability space we now consider a stochastic process $Z=\left(Z_{t}\right)$, which is adapted to a general filtration $\mathbb{F}$, i.e., on the $\mathbb{F}$-information level the process can be observed, or in mathematical terms: $\mathcal{F}_{t}^{Z} \subset \mathcal{F}_{t}$, which assures that $Z_{t}$ is $\mathcal{F}_{t}$-measurable for all $t \in \mathbb{R}_{+}$. All stochastic processes are, if not stated otherwise, assumed to be right-continuous and to have left limits.

A random variable $X$ is integrable if $E|X|<\infty$. If the $p$ th power of a random variable $X$ is integrable, $E|X|^{p}<\infty, 1 \leq p<\infty$, then it is sometimes said that $X$ is an element of $L^{p}$, the vector space of real-valued random variables with finite $p$ th moment. A stochastic process $\left(X_{t}\right), t \in \mathbb{R}_{+}$, is called integrable if all $X_{t}$ are integrable, i.e., $X_{t} \in L^{1}$ for all $t \in \mathbb{R}_{+}$. A family of random variables $\left(X_{t}\right), t \in \mathbb{R}_{+}$, is called uniformly integrable, if

$$
\lim _{c \rightarrow \infty} \sup _{t \in \mathbb{R}_{+}} E\left[\left|X_{t}\right| I\left(\left|X_{t}\right| \geq c\right)\right]=0
$$

To simplify the notation, we assume that relations such as $\subset,=$ or $\leq$,$<,=$ between measurable sets and random variables, respectively, always hold with probability one, which means that the term $P$-a.s. is suppressed. For conditional expectations no difference is made between a version and the equivalence class of $P$-a.s. equal versions.

If we consider a stochastic process $X=\left(X_{t}\right)$ and do not demand that it is right-continuous, then expressions like $Y_{t}=\int_{0}^{t} X_{s} d s$ have no meaning unless $\left(X_{t}\right)$ fulfills some measurability condition in the argument $t$. One condition is the following.

Definition 3.1. A stochastic process $X$ is $\mathbb{F}$-progressive or progressively measurable, if for every $t$ the mapping $(s, \omega) \rightarrow X_{s}(\omega)$ on $[0, t] \times \Omega$ is measurable with respect to the product $\sigma$-algebra $\mathcal{B}([0, t]) \otimes \mathcal{F}_{t}$, where $\mathcal{B}([0, t])$ is the Borel $\sigma$-algebra on $[0, t]$.

Every left- or right-continuous adapted process is progressively measurable. If $X$ is progressive, then so is $Y=\left(Y_{t}\right), Y_{t}=\int_{0}^{t} X_{s} d s$. A further measurability restriction is needed in connection with stochastic processes in continuous time. This is the fundamental concept of predictability.

Definition 3.2. Let $\mathbb{F}$ be a filtration on the basic probability space and let $\mathcal{P}(\mathbb{F})$ be the $\sigma$-algebra on $(0, \infty) \times \Omega$ generated by the system of sets

$$
(s, t] \times A, 0 \leq s<t, A \in \mathcal{F}_{s}, t>0
$$

$\mathcal{P}(\mathbb{F})$ is called the $\mathbb{F}$-predictable $\sigma$-algebra on $(0, \infty) \times \Omega$. A stochastic process $X=\left(X_{t}\right)$ is called $\mathbb{F}$-predictable, if $X_{0}$ is $\mathcal{F}_{0}$-measurable and the mapping $(t, \omega) \rightarrow X_{t}(\omega)$ on $(0, \infty) \times \Omega$ into $\mathbb{R}$ is measurable with respect to $\mathcal{P}(\mathbb{F})$.Every left-continuous process adapted to $\mathbb{F}$ is $\mathbb{F}$-predictable. In most applications we will be concerned with predictable processes that are leftcontinuous. Note that $\mathbb{F}$-predictable processes are also $\mathbb{F}$-progressive.

To get an impression of the meaning of the term predictable, we remark that for an $\mathbb{F}$-predictable process $X$ the value $X_{t}$ can be predicted from the information available "just" before time $t$, i.e., $X_{t}$ is measurable with respect to $\mathcal{F}_{t-}=\bigvee_{s<t} \mathcal{F}_{s}=\sigma\left(A_{s}, A_{s} \in \mathcal{F}_{s}, 0 \leq s<t\right)$. Processes of this kind are important elements in the framework of point processes. Additional information on these measurability concepts can be found in Appendix A.3, p. 254.

Some further important terms are introduced in the following definitions.
Definition 3.3. A random variable $\tau$ with values in $\mathbb{R}_{+} \cup\{\infty\}$ is called an $\mathbb{F}$-stopping time if $\{\tau \leq t\} \in \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$.

Thus a stopping time is related to the given information in that at any time $t$ it is possible to decide whether $\tau$ has happened up to time $t$ or not, only using information of the past and present but not anticipating the future.

If $\mathbb{F}=\left(\mathcal{F}_{t}\right)$ is a filtration and $\tau$ an $\mathbb{F}$-stopping time, then the information up to the random time $\tau$ is given by $\mathcal{F}_{\tau}=\left\{A \in \mathcal{F}_{\infty}: A \cap\{\tau \leq t\} \in \mathcal{F}_{t}\right.$ for all $\left.t \in \mathbb{R}_{+}\right\}$. To understand the meaning of this definition, we specialize to a deterministic stopping time $\tau=t^{*} \in \mathbb{R}_{+}$. Then $A \in \mathcal{F}_{t^{*}}$ is equivalent to $A \cap\left\{t^{*} \leq t\right\} \in \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$, where $\left\{t^{*} \leq t\right\}$ stands for $\Omega$ if $t^{*} \leq t$ and for $\emptyset$ otherwise, i.e., for $t=t^{*}$ the event must be in $\mathcal{F}_{t^{*}}$ and then it is in $\mathcal{F}_{t}$ for all $t>t^{*}$ because the filtration is monotone.

Definition 3.4. An integrable $\mathbb{F}$-adapted process $\left(X_{t}\right), t \in \mathbb{R}_{+}$, is called a martingale (submartingale, supermartingale), if for all $s>t, s, t \in \mathbb{R}_{+}$,

$$
E\left[X_{s} \mid \mathcal{F}_{t}\right]=(\geq, \leq) X_{t}
$$

In the following we denote by $\mathcal{M}$ the set of martingales with paths that are right-continuous and have left-hand limits and by $\mathcal{M}_{0}$ the set of martingales $M \in \mathcal{M}$ with $M_{0}=0$.

# 3.1.1 The Semimartingale Representation 

Semimartingale representations of stochastic processes play a key role in our set-up. They allow the process to be decomposed into a drift or regression part and an additive random fluctuation described by a martingale.

Definition 3.5. A stochastic process $Z=\left(Z_{t}\right), t \in \mathbb{R}_{+}$, is called a smooth semimartingale (SSM) if it has a decomposition of the form

$$
Z_{t}=Z_{0}+\int_{0}^{t} f_{s} d s+M_{t}
$$

where $f=\left(f_{t}\right), t \in \mathbb{R}_{+}$, is a progressively measurable stochastic process with $E \int_{0}^{t}\left|f_{s}\right| d s<\infty$ for all $t \in \mathbb{R}_{+}, E\left|Z_{0}\right|<\infty$ and $M=\left(M_{t}\right) \in \mathcal{M}_{0}$. Short notation: $Z=(f, M)$.A martingale is the mathematical model of a fair game with constant expectation function $E M_{0}=0=E M_{t}$ for all $t \in \mathbb{R}_{+}$. The drift term is an integral over a stochastic process. To give this integral meaning, $\left(f_{t}\right)$ should also be measurable in the argument $t$, which is ensured, for example, if $f$ has right-continuous paths or, more general, if $f$ is progressively measurable. Since the drift part in the above decomposition is continuous, a process $Z$, which admits such a representation, is called a SSM or smooth $\mathbb{F}$-semimartingale if we would like to emphasize that $Z$ is adapted to the filtration $\mathbb{F}$. For some additional details concerning SSMs, see the Appendix A.6, p. 266.

Below we formulate conditions under which a process $Z$ admits a semimartingale representation and show how this decomposition can be found. To this end we denote $D(t, h)=h^{-1} E\left[Z_{t+h}-Z_{t} \mid \mathcal{F}_{t}\right], t, h \in \mathbb{R}_{+}$.
C1 For all $t, h \in \mathbb{R}_{+}$, versions of the conditional expectation $E\left[Z_{t+h} \mid \mathcal{F}_{t}\right]$ exist such that the limit

$$
f_{t}=\lim _{h \rightarrow 0+} D(t, h)
$$

exists $P$-a.s. for all $t \in \mathbb{R}_{+}$and $\left(f_{t}\right), t \in \mathbb{R}_{+}$, is $\mathbb{F}$-progressively measurable with $E \int_{0}^{t}\left|f_{s}\right| d s<\infty$ for all $t \in \mathbb{R}_{+}$.
C2 For all $t \in \mathbb{R}_{+},(h D(t, h)), h \in \mathbb{R}_{+}$, has $P$-a.s. paths, which are absolutely continuous.
C3 For all $t \in \mathbb{R}_{+}$, a constant $c>0$ exists such that $\{D(t, h): 0<h \leq c\}$ is uniformly integrable.

The following theorem shows that these conditions are sufficient for a SSM representation.

Theorem 3.6. Let $Z=\left(Z_{t}\right), t \in \mathbb{R}_{+}$, be a stochastic process on the probability space $(\Omega, \mathcal{F}, P)$, adapted to the filtration $\mathbb{F}$. If C1, C2, and C3 hold true, then $Z$ is an SSM with representation $Z=(f, M)$, where $f$ is the limit defined in $C 1$ and $M$ is an $\mathbb{F}$-martingale given by

$$
M_{t}=Z_{t}-Z_{0}-\int_{0}^{t} f_{s} d s
$$

Proof. We have to show that with $\left(f_{t}\right)$ from condition C 1 the right-continuous process $M_{t}=Z_{t}-Z_{0}-\int_{0}^{t} f_{s} d s$ is an $\mathbb{F}$-martingale, i.e., that for all $A \in \mathcal{F}_{t}$ and $s \geq t, s, t \in \mathbb{R}_{+}, E\left[I_{A} M_{s}\right]=E\left[I_{A} M_{t}\right]$, where $I_{A}$ denotes the indicator variable. This is equivalent to

$$
E\left[I_{A}\left(M_{s}-M_{t}\right)\right]=\int_{A}\left(Z_{s}-Z_{t}-\int_{t}^{s} f_{u} d u\right) d P=0
$$

For all $r, t \leq r \leq s$, and $A \in \mathcal{F}_{t}, I_{A}$ is $\mathcal{F}_{r}$-measurable. This yields

$$
\begin{aligned}
\frac{1}{h} E\left[I_{A}\left(Z_{r+h}-Z_{r}\right)\right] & =\frac{1}{h} E\left[E\left[I_{A}\left(Z_{r+h}-Z_{r}\right) \mid \mathcal{F}_{r}\right]\right] \\
& =E\left[I_{A} \frac{1}{h} E\left[Z_{r+h}-Z_{r} \mid \mathcal{F}_{r}\right]\right]=E\left[I_{A} D(r, h)\right]
\end{aligned}
$$From C 1 it follows that $D(r, h) \rightarrow f_{r}$ as $h \rightarrow 0+$ and therefore also $I_{A} D(r, h) \rightarrow I_{A} f_{r}$ as $h \rightarrow 0+P$-a.s. Now $I_{A} D(r, h)$ is uniformly integrable by C3, which ensures that

$$
\lim _{h \rightarrow 0+} E\left[I_{A} D(r, h)\right]=\lim _{h \rightarrow 0+} \frac{1}{h} E\left[I_{A}\left(Z_{r+h}-Z_{r}\right)\right]=E\left[I_{A} f_{r}\right]
$$

Because of C 2 there exists a process $\left(g_{t}\right)$ such that

$$
E\left[I_{A}\left(Z_{s}-Z_{t}\right)\right]=E\left[I_{A} \int_{t}^{s} g_{u} d u\right]=\int_{t}^{s} E\left[I_{A} g_{u}\right] d u
$$

where the second equality follows from Fubini's theorem. Then (3.2) and (3.3) together yield

$$
E\left[I_{A}\left(Z_{s}-Z_{t}\right)\right]=\int_{t}^{s} E\left[I_{A} f_{u}\right] d u=E\left[I_{A} \int_{t}^{s} f_{u} d u\right]
$$

which proves the assertion.
Remark 3.7. (i) In the terminology of Dellacherie and Meyer [62] an SSM $Z=(f, M)$ is a special semimartingale because the drift term $\int_{0}^{t} f_{s} d s$ is continuous and therefore predictable. Hence the decomposition of $Z$ is unique $P$-a.s., because a second decomposition $Z=\left(f^{\prime}, M^{\prime}\right)$ leads to the continuous and therefore predictable martingale $M-M^{\prime}$ of integrable variation, which is identically 0 (cf. Appendix A.5, Lemma A.39, p. 263). (ii) It can be shown that if $Z=(f, M)$ is an SSM and for some constant $c>0$ the family of random variables $\left\{\left|h^{-1} \int_{t}^{t+h} f_{s} d s\right|: 0<h \leq c\right\}$ is bounded by some integrable random variable $Y$, then the conditions $\mathrm{C} 1-\mathrm{C} 3$ hold true, i.e., $\mathrm{C} 1-\mathrm{C} 3$ are under this boundedness condition not only sufficient but also necessary for a semimartingale representation. The proof of the main part (C2) is based on the Radon/Nikodym theorem. The details are of technical nature, and they are therefore omitted and left to the interested reader. (iii) For applications it is often of interest to find an SSM representation for point processes, i.e., to determine the compensator of such a process (cf. Definition 3.4 on p. 62). For such and other more specialized processes, specifically adapted methods to find the compensator can be applied, see below and $[16,50,58,103,115]$.

One of the simplest examples of a process with an SSM representation is the Poisson process $\left(N_{t}\right), t \in \mathbb{R}_{+}$, with constant rate $\lambda>0$. It is well-known and easy to see from the definition of a martingale that $M_{t}=N_{t}-\lambda t$ defines a martingale with respect to the internal filtration $\mathcal{F}_{t}^{N}=\sigma\left(N_{s}, 0 \leq s \leq t\right)$. If we consider conditions $\mathrm{C} 1-\mathrm{C} 3$, we find that $D(t, h)=\lambda$ for all $t, h \in \mathbb{R}_{+}$because the Poisson process has independent and stationary increments: $E\left[N_{t+h}-\right.$ $\left.N_{t} \mid \mathcal{F}_{t}^{N}\right]=E\left[N_{t+h}-N_{t}\right]=E N_{h}=h \lambda$. Therefore, we see that $\mathrm{C} 1-\mathrm{C} 3$ are satisfied with $f_{t}=\lambda$ for all $\omega \in \Omega$ and all $t \in \mathbb{R}_{+}$, which results in the representation $N_{t}=\int_{0}^{t} \lambda d s+M_{t}=\lambda t+M_{t}$.

The Poisson process is a point process as well as an example of a Markov process, and the question arises under which conditions point and Markov processes admit an SSM representation.# Point and Counting Processes 

A point process over $\mathbb{R}_{+}$can be described by an increasing sequence of random variables or by a purely atomic random measure or by means of its corresponding counting process. Since we want to use the semimartingale structure of point processes, we will mostly use the last description of a point process. A (univariate) point process is an increasing sequence $\left(T_{n}\right), n \in \mathbb{N}$, of positive random variables, which may also take the value $+\infty: 0<T_{1} \leq T_{2} \leq \ldots$ The inequality is strict unless $T_{n}=\infty$. We always assume that $T_{\infty}=\lim _{n \rightarrow \infty} T_{n}=\infty$, i.e., that the point process is nonexplosive.

This point process is also completely characterized by the random measure $\mu$ on $(0, \infty)$ defined by

$$
\mu(\omega, A)=\sum_{k \geq 1} I\left(T_{k}(\omega) \in A\right)
$$

for all Borel sets $A$ of $(0, \infty)$.
Another equivalent way to describe a point process is by a counting process $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, with

$$
N_{t}(\omega)=\sum_{k \geq 1} I\left(T_{k}(\omega) \leq t\right)
$$

which is, for each realization $\omega$, a right-continuous step function with jumps of magnitude 1 and $N_{0}(\omega)=0 . N_{t}$ counts the number of time points $T_{n}$, which occur up to time $t$. Since $\left(N_{t}\right), t \in \mathbb{R}_{+}$, and $\left(T_{n}\right), n \in \mathbb{N}$, obviously carry the same information, the associated counting process is sometimes also called a point process.

A slight generalization is the notion of a multivariate point process. Let $\left(T_{n}\right), n \in \mathbb{N}$, be a point process as before and $\left(V_{n}\right), n \in \mathbb{N}$, a sequence of random variables with values in a finite set $\left\{a_{1}, \ldots, a_{m}\right\}$. Then the sequence of pairs $\left(T_{n}, V_{n}\right), n \in \mathbb{N}$, is called a multivariate point process and the associated $m$-variate counting process $N_{t}=\left(N_{t}(1), \ldots, N_{t}(m)\right)$ is defined by

$$
N_{t}(i)=\sum_{k \geq 1} I\left(T_{k} \leq t\right) I\left(V_{k}=a_{i}\right), i \in\{1, \ldots, m\}
$$

Let us now consider a univariate point process $\left(T_{n}\right), n \in \mathbb{N}$, and its associated counting process $\left(N_{t}\right), t \in \mathbb{R}_{+}$, with $E N_{t}<\infty$ for all $t \in \mathbb{R}_{+}$on a filtered probability space $(\Omega, \mathcal{F}, \mathbb{F}, P)$. The traditional definition of the compensator of a point process is the following.

Definition 3.8. Let $N$ be an integrable point process adapted to the filtration $\mathbb{F}$. The unique $\mathbb{F}$-predictable increasing process $A=\left(A_{t}\right)$, such that

$$
E \int_{0}^{\infty} C_{s} d N_{s}=E \int_{0}^{\infty} C_{s} d A_{s}
$$

is fulfilled for all nonnegative $\mathbb{F}$-predictable processes $C$, is called the compensator of $N$ with respect to $\mathbb{F}$.The existence and the uniqueness of the compensator can be proved by the so-called dual predictable projection. We refer to the work of Jacod [92]. The following martingale characterization of the compensator links the dynamical view of point processes with the semimartingale set-up (for a proof, see [103], p. 60).

Theorem 3.9. Let $N$ be an integrable point process adapted to the filtration $\mathbb{F}$. Then $A$ is the $\mathbb{F}$-compensator of $N$ if and only if the difference process $N-A$ is an $\mathbb{F}$-martingale of $\mathcal{M}_{0}$.

Proof (Sketch). Let $A$ be the compensator and $C$ be the predictable process defined as the indicator of the set $(t, s] \times B$, where $s>t, B \in \mathcal{F}_{t}$. Then the definition of the compensator yields

$$
E\left[I_{B}\left(N_{s}-N_{t}\right)\right]=E\left[I_{B}\left(A_{s}-A_{t}\right)\right]
$$

which gives

$$
E\left[I_{B}\left(N_{s}-A_{s}\right)\right]=E\left[I_{B}\left(N_{t}-A_{t}\right)\right]
$$

Hence, $N-A$ is a martingale.
Conversely, if $N-A$ is a martingale, then $A$ is integrable and we obtain (3.5). In the general case, (3.4) can be established using the monotone class theorem.

If we view the compensator as a random measure $A(d t)$ on $(0, \infty)$, then we can interpret this measure in an infinitesimal form by the heuristic expression

$$
A(d t)=E\left[d N_{t} \mid \mathcal{F}_{t-}\right]
$$

So, by an increment $d t$ in time from $t$ on, the increment $A(d t)$ is what we can predict from the information gathered in $[0, t)$ about the increase of $N_{t}$, and $d M_{t}=d N_{t}-A(d t)$ is what remains unforeseen. Thus, sometimes $M$ is called an innovation martingale and $A(d t)$ the (dual) predictable projection.

In many cases (which are those we are mostly interested in) the $\mathbb{F}$ compensator $A$ of a counting process $N$ can be represented as an integral of the form

$$
A_{t}=\int_{0}^{t} \lambda_{s} d s
$$

with some nonnegative ( $\mathbb{F}$-progressively measurable) stochastic process $\left(\lambda_{t}\right)$, $t \in \mathbb{R}_{+}$, i.e., $N$ has an SSM representation $N=(\lambda, M)$.

Definition 3.10. Let $N$ be an integrable counting process with an $\mathbb{F}$-SSM representation

$$
N_{t}=A_{t}+M_{t}=\int_{0}^{t} \lambda_{s} d s+M_{t}
$$

where $\left(\lambda_{t}\right), t \in \mathbb{R}_{+}$, is a nonnegative process. Then $\lambda$ is called the $\mathbb{F}$-intensity of $N$.Remark 3.11. (i) To speak of the intensity is a little bit misleading (but harmless) because it is not unique. It can be shown (see Brémaud [50], p. 31) that if one can find a predictable intensity, then it is unique except on a set of measure 0 with respect to the product measure of $P$ and Lebesgue measure. On the other hand, if there exists an intensity, then one can always find a predictable version. (ii) The heuristic interpretation

$$
\lambda_{t} d t=E\left[d N_{t} \mid \mathcal{F}_{t-}\right]
$$

is very similar to the ordinary failure or hazard rate of a random variable.
Theorem 3.9 and Definition 3.10 link the point process to the semimartingale representation, and using the definition of the compensator, it is possible to verify formally that a process $\lambda$ is the $\mathbb{F}$-intensity of the point process $N$. We have to show that

$$
E \int_{0}^{\infty} C_{s} d N_{s}=E \int_{0}^{\infty} C_{s} \lambda_{s} d s
$$

for all nonnegative $\mathbb{F}$-predictable processes $C$. Another way to verify that a process $A$ is the compensator is to check the general conditions C1-C3 on page 60 or to use the conditions given by Aven [16].

To go one step further we now specialize to the internal filtration $\mathbb{F}^{N}=$ $\left(\mathcal{F}_{t}^{N}\right), \mathcal{F}_{t}^{N}=\sigma\left(N_{s}, 0 \leq s \leq t\right)$, and determine the $\mathbb{F}^{N}$-compensator of $N$ in an explicit form. The proof of the following theorem can be found in Jacod [92] and in Brémaud [50], p. 61. Regular conditional distributions are introduced in Appendix A.2, p. 252.

Theorem 3.12. Let $N$ be an integrable point process and $\mathbb{F}^{N}$ its internal filtration. For each $n$ let $G_{n}(\omega, B)$ be the regular conditional distribution of the interarrival time $U_{n+1}=T_{n+1}-T_{n}, n \in \mathbb{N}_{0}, T_{0}=0$, given the past $\mathcal{F}_{T_{n}}^{N}$ at the $\mathbb{F}^{N}$-stopping time $T_{n}: G_{n}(\omega, B)=P\left(U_{n+1} \in B \mid \mathcal{F}_{T_{n}}^{N}\right)(\omega)$.
(i) Then for $T_{n}<t \leq T_{n+1}$ the compensator $A$ is given by

$$
A_{t}=A_{T_{n}}+\int_{0}^{t-T_{n}} \frac{G_{n}(d x)}{G_{n}([x, \infty))}
$$

(ii) If the conditional distribution $G_{n}$ admits a density $g_{n}$ for all $n$, then the $\mathbb{F}^{N}$-intensity $\lambda$ is given by

$$
\lambda_{t}=\sum_{n \geq 0} \frac{g_{n}\left(t-T_{n}\right)}{1-\int_{0}^{t-T_{n}} g_{n}(x) d x} I\left(T_{n}<t \leq T_{n+1}\right)
$$

Note that expressions of the form " $\frac{0}{0}$ " are always set equal to 0 .
Example 3.13. (Renewal process). Let the interarrival times $U_{n+1}=T_{n+1}-$ $T_{n}, n \in \mathbb{N}_{0}, T_{0}=0$, be i.i.d. random variables with common distribution function $F$, density $f$ and failure rate $r: r(t)=f(t) /(1-F(t))$. Then itfollows from Theorem 3.12 that with respect to the internal history $\mathcal{F}_{t}^{N}=$ $\sigma\left(N_{s}, 0 \leq s \leq t\right)$ the intensity on $\left\{T_{n}<t \leq T_{n+1}\right\}$ is given by $\lambda_{t}=r\left(t-T_{n}\right)$. This results in the SSM representation $N=(\lambda, M)$,

$$
N_{t}=\int_{0}^{t} \lambda_{s} d s+M_{t}
$$

with the intensity

$$
\lambda_{t}=\sum_{n \geq 0} r\left(t-T_{n}\right) I\left(T_{n}<t \leq T_{n+1}\right)
$$

This corresponds to our supposition that the intensity at time $t$ is the failure rate of the last renewed item before $t$ at an age of $t-T_{n}$.

Example 3.14. (Markov-modulated Poisson process). A Poisson process can be generalized by replacing the constant intensity with a randomly varying intensity, which takes one of the $m$ values $\lambda_{i}, 0<\lambda_{i}<\infty, i \in S=\{1, \ldots, m\}$, $m \in \mathbb{N}$. The changes are driven by a homogeneous Markov chain $Y=\left(Y_{t}\right), t \in$ $\mathbb{R}_{+}$, with values in $S$ and infinitesimal parameters $q_{i}$, the rate to leave state $i$, and $q_{i j}$, the rate to reach state $j$ from state $i$ :

$$
\begin{aligned}
q_{i} & =\lim _{h \rightarrow 0+} \frac{1}{h} P\left(Y_{h} \neq i \mid Y_{0}=i\right) \\
q_{i j} & =\lim _{h \rightarrow 0+} \frac{1}{h} P\left(Y_{h}=j \mid Y_{0}=i\right), i, j \in S, i \neq j \\
q_{i i} & =-q_{i}=-\sum_{j \neq i} q_{i j}
\end{aligned}
$$

The point process $\left(T_{n}\right)$ corresponds to the counting process $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, with

$$
N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)
$$

It is assumed that $N$ has a stochastic intensity $\lambda_{Y_{t}}$ with respect to the filtration $\mathbb{F}$, generated by $N$ and $Y$ :

$$
\mathcal{F}_{t}=\sigma\left(N_{s}, Y_{s}, 0 \leq s \leq t\right)
$$

Then $N$ is called a Markov-modulated Poisson process with SSM representation

$$
N_{t}=\int_{0}^{t} \lambda_{Y_{s}} d s+M_{t}
$$

Roughly spoken, in state $i$ the point process is Poisson with rate $\lambda_{i}$. But note that the ordinary failure rate of $T_{1}$ is not constant. If we cannot observe the Markov chain $Y$, but only the point process $\left(T_{n}\right)$, then we look for an intensity with respect to the subfiltration $\mathbb{A}=\left(\mathcal{A}_{t}\right), t \in \mathbb{R}_{+}, \mathcal{A}_{t}=\sigma\left(N_{s}, 0 \leq s \leq t\right)$. For this we have to estimate the current state of the Markov chain, involving the infinitesimal parameters $q_{i}, q_{i j}$. For this we refer to Sects.3.2.4 and 5.4.2.# Markov Processes 

The question whether Markov processes admit semimartingale representations can generally be answered in the affirmative: (most) Markov processes and bounded functions of such processes have an SSM representation.

Let $\left(X_{t}\right), t \in \mathbb{R}_{+}$, be a right-continuous homogeneous Markov process on $\left(\Omega, \mathcal{F}, P^{x}\right)$ with respect to the (internal) filtration $\mathcal{F}_{t}=\sigma\left(X_{s}, 0 \leq s \leq t\right)$ with values in a measurable space $(S, \mathcal{B}(S))$. For applications we will often confine ourselves to $S=\mathbb{R}$ with its Borel $\sigma$-field $\mathcal{B}$. Here $P^{x}, x \in S$, denotes the probability measure on the set of paths, which start in $X_{0}=x: P^{x}$ $\left(X_{0}=x\right)=1$

Let $\mathbb{B}$ denote the set of bounded, measurable functions on $S$ with values in $\mathbb{R}$ and let $E^{x}$ denote expectation with respect to $P^{x}$. Then the infinitesimal generator $\mathcal{A}$ is defined as follows: If for $f \in \mathbb{B}$ the limit

$$
\lim _{h \rightarrow 0+} \frac{1}{h}\left(E^{x} f\left(X_{h}\right)-f(x)\right)=g(x)
$$

exists for all $x \in S$ with $g \in \mathbb{B}$, then we set $\mathcal{A} f=g$ and say that $f$ belongs to the domain $\mathbb{D}(\mathcal{A})$ of the infinitesimal generator $\mathcal{A}$. It is known that if $f \in \mathbb{D}(\mathcal{A})$, then

$$
M_{t}^{f}=f\left(X_{t}\right)-f\left(X_{0}\right)-\int_{0}^{t} \mathcal{A} f\left(X_{s}\right) d s
$$

defines a martingale (cf., e.g., [101], p. 328). This shows that a function $Z_{t}=f\left(X_{t}\right)$ of a homogeneous Markov process has an SSM representation if $f \in \mathbb{D}(\mathcal{A})$.

Example 3.15 (Markov pure jump process). A homogeneous Markov process $X=\left(X_{t}\right)$ with right-continuous paths, which are constant between isolated jumps, is called a Markov pure jump process. As before, $P^{x}$ denotes the probability law conditioned on $X_{0}=x$ and $\tau_{x}=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \neq x\right\}$ the exit time of state $x$. It is known that $\tau_{x}$ follows an $\operatorname{Exp}(\lambda(x))$ distribution if $0<\lambda(x)<\infty$ and that $P^{x}\left(\tau_{x}=\infty\right)=1$ if $\lambda(x)=0$, for some suitable mapping $\lambda$ on the set of possible outcomes of $X_{0}$ with values in $\mathbb{R}_{+}$. Let $v(x, \cdot)$ be the jump law or transition probability at $x$, defined by $v(x, B)=P^{x}\left(X_{\tau_{x}} \in B\right)$ for $\lambda(x)>0$. If $f$ belongs to the domain of $\mathbb{D}(\mathcal{A})$ of the infinitesimal generator, then we obtain (cf. Métivier [122])

$$
\mathcal{A} f(x)=\lambda(x) \int(f(y)-f(x)) v(x, d y)
$$

Let us now consider some particular cases. (i) Poisson process $N=\left(N_{t}\right)$ with parameter $\lambda>0$. In this case we have jumps of height 1 , i.e., $v(x,\{x+1\})=1$. For $f(x)=x$ we get $\mathcal{A} f(x) \equiv \lambda$. This again shows that $N_{t}-\lambda t$ is a martingale. If we take $f(x)=x^{2}$, then we obtain $\mathcal{A} f(x)=\lambda(2 x+1)$ and for $N^{2}$ we have the SSM representation$$
N_{t}^{2}=f\left(N_{t}\right)=\int_{0}^{t} \lambda\left(2 N_{s}+1\right) d s+M_{t}^{f}
$$

(ii) Compound Poisson process $X=\left(X_{t}\right)$. Let $N$ be a Poisson process with an intensity $\lambda: \mathbb{R} \rightarrow \mathbb{R}_{+}, 0<\lambda(x)<\infty$, and $\left(Y_{n}\right), n \in \mathbb{N}$, a sequence of i.i.d. random variables with finite mean $\mu$. Then

$$
X_{t}=\sum_{n=1}^{N_{t}} Y_{n}
$$

defines a Markov pure jump process with $\nu(x, B)=P^{x}\left(X_{\tau_{x}} \in B\right)=P\left(Y_{1} \in\right.$ $B-x)$. By formula (3.6) for the infinitesimal generator we get the SSM representation

$$
X_{t}=\int_{0}^{t} \lambda\left(X_{s}\right) \mu d s+M_{t}
$$

We now return to the general theory of Markov processes. The so-called Dynkin formula states that for a stopping time $\tau$ we have

$$
E^{x} g\left(X_{\tau}\right)=g(x)+E^{x} \int_{0}^{\tau} \mathcal{A} g\left(X_{s}\right) d s
$$

if $E^{x} \tau<\infty$ and $g \in \mathbb{D}(\mathcal{A})$ (see Dynkin [66], p. 133). This formula can now be extended to the more general case of SSMs. If $Z=(f, M)$ is an $\mathbb{F}$-SSM with ( $P$-a.s.) bounded $Z$ and $f$, then for all $\mathbb{F}$-stopping times $\tau$ with $E \tau<\infty$ we obtain

$$
E Z_{\tau}=E Z_{0}+E \int_{0}^{\tau} f_{s} d s
$$

Here $E M_{\tau}=0$ is a consequence of the Optional Sampling Theorem (see Appendix A.5, Theorem A.34, p. 262). The following example shows how the Dynkin formula can be applied to determine the expectation of a stopping time.

Example 3.16. Let $B=\left(B_{t}\right)$ be a $k$-dimensional Brownian motion with initial point $B_{0}=x$ and $g$ a bounded twice continuously differentiable function on $\mathbb{R}^{k}$ with bounded derivatives. Then we obtain (cf. Métivier [122], p. 201) the SSM representation for $g\left(B_{t}\right)$ :

$$
g\left(B_{t}\right)=g(x)+\frac{1}{2} \int_{0}^{t} \sum_{i, j=1}^{k} \frac{\partial^{2} g}{\partial x_{i} \partial x_{j}}\left(B_{s}\right) d s+M_{t}^{g}
$$

For some $R>0$ and $|x|<R$ we consider the stopping time $\sigma=\inf \left\{t \in \mathbb{R}_{+}\right.$: $\left.\left|B_{t}\right| \geq R\right\}$ with respect to the internal filtration, which is the first exit time of the ball $K_{R}=\left\{y \in \mathbb{R}^{k}:|y|<R\right\}$. By means of the Dynkin formula we can determine the expectation $E^{x} \sigma$ in the following way. Let us assume $E^{x} \sigma<\infty$ and choose $g(x)=|x|^{2}$. Dynkin's formula then yields$$
\begin{aligned}
E^{x} g\left(B_{\sigma}\right) & =R^{2}=|x|^{2}+\frac{1}{2} E^{x} \int_{0}^{\sigma} 2 k d s \\
& =|x|^{2}+k E^{x} \sigma
\end{aligned}
$$

which is tantamount to $E^{x} \sigma=k^{-1}\left(R^{2}-|x|^{2}\right)$. To show $E^{x} \sigma<\infty$ we may replace $\sigma$ by $\tau_{n}=n \wedge \sigma$ in the above formula: $E^{x} \tau_{n} \leq k^{-1}\left(R^{2}-|x|^{2}\right)$ and together with the monotone convergence theorem the result is established.

# 3.1.2 Transformations of SSMs 

Next we want to investigate under which conditions certain transformations of SSMs again lead to SSMs and leave the SSM property unchanged.

## Random Stopping

One example is the stopping of a process $Z$, i.e., the transformation from $Z=\left(Z_{t}\right)$ to the process $Z^{\zeta}=\left(Z_{t \wedge \zeta}\right)$, where $\zeta$ is some stopping time. If $Z=(f, M)$ is an $\mathbb{F}$-SSM and $\zeta$ is an $\mathbb{F}$-stopping time, then $Z^{\zeta}$ is again an $\mathbb{F}$-SSM with representation

$$
Z_{t}^{\zeta}=Z_{0}+\int_{0}^{t} I(\zeta>s) f_{s} d s+M_{t \wedge \zeta}, t \in \mathbb{R}_{+}
$$

This result is an immediate consequence of the fact that a stopped martingale is a martingale.

## A Product Rule

A second example of a transformation is the product of two SSMs. To see under which conditions such a product of two SSMs again forms an SSM, some further notations and definitions are required, which are presented in Appendix A. Here we only give the general result. For the conditions and a detailed proof we refer to Appendix A.6, Theorem A.51, p. 269.

Let $Z=(f, M)$ and $Y=(g, N)$ be $\mathbb{F}$-SSMs with $M, N \in \mathcal{M}_{0}^{2}$ and $M N \in$ $\mathcal{M}_{0}$. Then, under suitable integrability conditions, $Z Y$ is an $\mathbb{F}$-SSM with representation

$$
Z_{t} Y_{t}=Z_{0} Y_{0}+\int_{0}^{t}\left(Y_{s} f_{s}+Z_{s} g_{s}\right) d s+R_{t}
$$

where $R=\left(R_{t}\right)$ is a martingale in $\mathcal{M}_{0}$.
Remark 3.17. (i) If $Z=(f, M)$ and $Y=(g, N)$ are two SSMs and $f$ and $g$ are considered as "derivatives," then $Y f+Z g$ is the "derivative" of the product $Z Y$ in accordance with the ordinary product rule. (ii) Martingales $M, N$, for which $M N$ is a martingale are called orthogonal. This property can be interpreted in the sense that the increments of the martingales are "conditionally uncorrelated," i.e.,

$$
E\left[\left(M_{t}-M_{s}\right)\left(N_{t}-N_{s}\right) \mid \mathcal{F}_{s}\right]=0
$$

for all $0 \leq s \leq t$.# A Change of Filtration 

Another transformation is a certain change of the filtration, which allows the observation of a stochastic process on different information levels.

Definition 3.18. Let $\mathbb{A}=\left(\mathcal{A}_{t}\right), t \in \mathbb{R}_{+}$, and $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, be two filtrations on the same probability space $(\Omega, \mathcal{F}, P)$. Then $\mathbb{A}$ is called a subfiltration of $\mathbb{F}$ if $\mathcal{A}_{t} \subset \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$.

In this case $\mathbb{F}$ can be viewed as the complete information filtration and $\mathbb{A}$ as the actual observation filtration on a lower level. If $Z=(f, M)$ is an SSM with respect to the filtration $\mathbb{F}$, then the projection to the observation filtration $\mathbb{A}$ is given by the conditional expectation $\hat{Z}$ with $\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{A}_{t}\right]$. The following projection theorem states that $\hat{Z}$ is an $\mathbb{A}$-semimartingale. Different versions of this theorem are proved in the literature. The version presented here for SSMs is based on, [50], pp. 87, 108, [100], p. 202 and [161].

Theorem 3.19 (Projection Theorem). Let $Z=(f, M)$ be an $\mathbb{F}$-SSM and $\mathbb{A}$ a subfiltration of $\mathbb{F}$. Then $\hat{Z}$ with

$$
\hat{Z}_{t}=\hat{Z}_{0}+\int_{0}^{t} \hat{f}_{s} d s+\hat{M}_{t}
$$

is an $\mathbb{A}$-SSM, where
(i) $\hat{Z}$ is $\mathbb{A}$-adapted with a.s. right-continuous paths with left-hand limits and $\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{A}_{t}\right]$ for all $t \in \mathbb{R}_{+}$
(ii) $\hat{f}$ is $\mathbb{A}$-progressively measurable with $\hat{f}_{t}=E\left[f_{t} \mid \mathcal{A}_{t}\right]$ for almost all $t \in \mathbb{R}_{+}$ (Lebesgue measure);
(iii) $\hat{M}$ is an $\mathbb{A}$-martingale.

If in addition $Z_{0}, \int_{0}^{\infty}\left|f_{s}\right| d s \in L^{2}$ and $M \in \mathcal{M}_{0}^{2}$, then $\hat{Z}_{0}, \int_{0}^{\infty}\left|\hat{f}_{s}\right| d s \in L^{2}$ and $\hat{M} \in \mathcal{M}_{0}^{2}$.

Unfortunately, monotonicity properties of $Z$ and $f$ do not in general extend to $\hat{Z}$ and $\hat{f}$, respectively. So if, for example, $f$ has monotone paths, this need not be true for the corresponding process $\hat{f}$. Whether $\hat{f}$ has monotone paths depends on the path properties of $f$ as well as on the subfiltration $\mathbb{A}$. If $f$ is already adapted to the subfiltration $\mathbb{A}$, then it is obvious that $\hat{f}=f$. In this case projecting onto the subfiltration only filters information out, which does not affect the drift term.

The Projection Theorem will mainly be applied to solve optimal stopping problems on different information levels in the following manner. Let $Z=$ $(f, M)$ be an $\mathbb{F}$-SSM and let $\hat{Z}=(\hat{f}, \hat{M})$ be the corresponding $\mathbb{A}$-SSM with respect to a subfiltration $\mathbb{A}$ of $\mathbb{F}$. To determine the maximum of $E Z_{\tau}$ in the set $C^{\mathbb{A}}$ of $\mathbb{A}$-stopping times $\tau$, i.e., to solve the optimal stopping problem on the lower $\mathbb{A}$-information level, we can use the rule of successive conditioning for conditional expectations (cf. Appendix A.2, p. 251) to obtain$$
\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\}=\sup \left\{E \hat{Z}_{\tau}: \tau \in C^{\mathbb{A}}\right\}
$$

In Sect. 5.2.1, Theorem 5.9, p. 181, conditions are given under which the stopping problem for an SSM $Z$ can be solved. If these conditions apply to $\hat{Z}$, then we can solve this optimal stopping problem on the $\mathbb{A}$-level according to Theorem 5.9. Could the stopping problem be solved on the $\mathbb{F}$-level, then we get a bound for the stopping value on the $\mathbb{A}$-level in view of the inequality

$$
\sup \left\{E \hat{Z}_{\tau}: \tau \in C^{\mathbb{A}}\right\} \leq \sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$

# 3.2 A General Lifetime Model 

First let us consider the simple indicator process $Z_{t}=I(T \leq t)$, where $T$ is the lifetime random variable defined on the basic probability space. Obviously $Z$ is the counting process corresponding to the simple point process $\left(T_{n}\right)$ with $T=T_{1}$ and $T_{n}=\infty$ for $n \geq 2$. The paths of this indicator process $Z$ are constant, except for one jump from 0 to 1 at $T$. Let us assume that this indicator process has a smooth $\mathbb{F}$-semimartingale representation with an $\mathbb{F}$ martingale $M \in \mathcal{M}_{0}$ and a nonnegative stochastic process $\lambda=\left(\lambda_{t}\right)$ :

$$
I(T \leq t)=\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}, t \in \mathbb{R}_{+}
$$

The general lifetime model is then defined by the filtration $\mathbb{F}$ and the corresponding $\mathbb{F}$-SSM representation of the indicator process.

Definition 3.20. The process $\lambda=\left(\lambda_{t}\right), t \in \mathbb{R}_{+}$, in the SSM-representation (3.8) is called the $\mathbb{F}$-failure rate or the $\mathbb{F}$-hazard rate process and the compensator $\Lambda_{t}=\int_{0}^{t} I(T>s) \lambda_{s} d s$ is called the $\mathbb{F}$-hazard process.

We drop $\mathbb{F}$, when it is clear from the context. As was mentioned before (cf. Remark 3.11 on p. 64), the intensity of the indicator (point) process is not unique. If one $\mathbb{F}$-failure rate $\lambda$ is known, we may pass to a left-continuous version $\left(\lambda_{t-}\right)$ to obtain a predictable, unique intensity:

$$
I(T \leq t)=\int_{0}^{t} I(T \geq s) \lambda_{s-} d s+M_{t}
$$

Before investigating under which conditions such a representation exists, some examples are given.

Example 3.21. If the failure rate process $\lambda$ is deterministic, forming expectations leads to the integral equation

$$
F(t)=P(T \leq t)=E I(T \leq t)=\int_{0}^{t} P(T>s) \lambda_{s} d s=\int_{0}^{t}(1-F(s)) \lambda_{s} d s
$$The unique solution

$$
\bar{F}(t)=1-F(t)=\exp \left\{-\int_{0}^{t} \lambda_{s} d s\right\}
$$

is just the well-known relation between the standard failure rate and the distribution function. This shows that if the hazard rate process $\lambda$ is deterministic, it coincides with the ordinary failure rate.

Example 3.22. In continuation of Example 1.1, p. 2, we consider a threecomponent system with one component in series with a two-component parallel system. It is assumed that the component lifetimes $T_{1}, T_{2}, T_{3}$ are i.i.d. exponentially distributed with parameter $\alpha>0$. What is the failure rate process corresponding to the system lifetime $T=T_{1} \wedge\left(T_{2} \vee T_{3}\right)$ ? This depends on the information level, i.e., on the filtration $\mathbb{F}$.

- $\mathcal{F}_{t}=\sigma\left(\mathbf{X}_{s}, 0 \leq s \leq t\right)$, where $\mathbf{X}_{s}=\left(X_{s}(1), X_{s}(2), X_{s}(3)\right)$ and $X_{s}(i)=$ $I\left(T_{i}>s\right), i=1,2,3$. Observing on the component level means that $\mathcal{F}_{t}$ is generated by the indicator processes of the component lifetimes up to time $t$. It can be shown (by means of the results of the next section) that the failure rate process of the system lifetime is given by $\lambda_{t}=\alpha\{1+(1-$ $\left.\left.X_{t}(2)\right)+\left(1-X_{t}(3)\right)\right\}$ on $\{T>t\}$. As long as all components work, the rate is $\alpha$ due to component 1 . When one of the two parallel components 2 or 3 fails first, then the rate switches to $2 \alpha$.
- $\mathcal{F}_{t}=\sigma\left(I(T \leq s), 0 \leq s \leq t\right)$. If only the system lifetime can be observed, the failure rate process diminishes to the ordinary deterministic failure rate

$$
\lambda_{t}=\alpha\left(1+2 \frac{1-e^{-\alpha t}}{2-e^{-\alpha t}}\right)
$$

Example 3.23. Consider the damage threshold model in which the deterioration is described by the Wiener process $X_{t}=\sigma B_{t}+\mu t$, where $B$ is standard Brownian motion and $\sigma, \mu>0$ are constants. In this case, whether and in what way the lifetime $T=\inf \left\{t \in \mathbb{R}_{+}: X_{t} \geq K\right\}, K \in \mathbb{R}_{+}$, can be characterized by a failure rate process, also depends on the available information.

- $\mathcal{F}_{t}=\sigma\left(B_{s}, 0 \leq s \leq t\right)$. Observing the actual state of the system proves to be too informative to be described by a failure rate process. The martingale part is identically 0 , the drift part or the predictable compensator is the indicator process $I(T \leq t)$ itself. No semimartingale representation (3.8) exists because the lifetime is predictable, as we will see in the following section.
- $\mathcal{F}_{t}=\sigma\left(I(T \leq s), 0 \leq s \leq t\right)$. If only the system lifetime can be observed, conditions change completely. A representation (3.8) exists. The first hitting time $T$ of the barrier $K$ is known to follow a so-called inverse Gaussian distribution (cf. [133], p. 26). The failure rate process is then the ordinary failure rate corresponding to the density

$$
f(t)=\frac{K}{\sqrt{2 \pi \sigma^{2} t^{3}}} \exp \left\{-\frac{(K-\mu t)^{2}}{2 \sigma^{2} t}\right\}, t>0
$$# 3.2.1 Existence of Failure Rate Processes 

It is possible to formulate rather general conditions on $Z$ to ensure a semimartingale representation (3.8) as shown by Theorem 3.6, p. 60. But in reliability models we often have more specific processes $V_{t}=I(T \leq t)$ for which a representation (3.8) has to be found. Whether such a representation exists should depend on the random variable $T$ (or on the probability measure $P$ ) and on the filtration $\mathbb{F}$. If $T$ is a stopping time with respect to the filtration $\mathbb{F}$, then a representation (3.8) only exists for stopping times which are totally inaccessible in the following sense:

Definition 3.24. An $\mathbb{F}$-stopping time $\tau$ is called

- predictable if an increasing sequence $\left(\tau_{n}\right), n \in \mathbb{N}$, of $\mathbb{F}$-stopping times $\tau_{n}<$ $\tau$ exists such that $\lim _{n \rightarrow \infty} \tau_{n}=\tau$;
- totally inaccessible if $P(\tau=\sigma<\infty)=0$ for all predictable $\mathbb{F}$-stopping times $\sigma$.

Roughly speaking, a stopping time $\tau$ is predictable, if it is announced by a sequence of (observable) stopping times, $\tau$ is totally inaccessible if it occurs "suddenly" without announcement. For example, a random variable $T$ with an absolutely continuous distribution has the representation

$$
V_{t}=I(T \leq t)=\int_{0}^{t} I(T>s) \lambda(s) d s+M_{t}, t \in \mathbb{R}_{+}
$$

with respect to the filtration $\mathbb{F}^{T}=\left(\mathcal{F}_{t}\right)$ generated by $T: \mathcal{F}_{t}=\sigma(T \wedge t)$, where $\lambda$ is the ordinary failure rate.

In general it can be shown that, if $V$ has a SSM representation (3.8), then $T$ is a totally inaccessible stopping time. On the other hand, if $T$ is totally inaccessible, then there is a (unique) decomposition $V=\Lambda+M$ in which the process $\Lambda$ is ( $P$-a.s.) continuous. We state this result without proof (cf. [62], p. 137 and [122], p. 113).

Lemma 3.25. Let $(\Omega, \mathcal{F}, \mathbb{F}, P)$ be a filtered probability space and $T$ an $\mathbb{F}$ stopping time.
(i) If the process $V=\left(V_{t}\right), V_{t}=I(T \leq t)$, has an SSM representation

$$
V_{t}=\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}, t \in \mathbb{R}_{+}
$$

then $T$ is a totally inaccessible stopping time and the martingale $M$ is bounded in $L^{2}, M \in \mathcal{M}_{0}^{2}$.
(ii) If $T$ is a totally inaccessible stopping time, then the process $V=\left(V_{t}\right)$, $V_{t}=I(T \leq t)$, has a unique ( $P$-a.s.) decomposition $V=\Lambda+M$, where $M$ is a uniformly integrable martingale and $\Lambda$ is continuous ( $P$-a.s., the predictable compensator)."Most" continuous functions are absolutely continuous (except some pathological special cases). Therefore, we can conclude from Lemma 3.25 that the class of lifetime models with a compensator $\Lambda$ of the form $\Lambda_{t}=\int_{0}^{t} I(T>$ $s) \lambda_{s} d s$ is rich enough to include models for most real-life systems in continuous time. In view of Example 3.23 the condition that $V$ admits an SSM representation seems a natural restriction, because if the lifetime could be predicted by an announcing sequence of stopping times, maintenance actions would make no sense, they could be carried out "just" before a failure. In Example $3.23 \tau_{n}=\inf \left\{t \in \mathbb{R}_{+}: X_{t}=K-\frac{1}{n}\right\}$ is such an announcing sequence with respect to $\mathcal{F}_{t}=\sigma\left(B_{s}, 0 \leq s \leq t\right)$ (compare also Fig. 1.1, p. 6). In addition, Example 3.23 shows that one and the same random variable $T$ can be predictable or totally inaccessible depending on the corresponding information filtration.

How can the failure rate process $\lambda$ be ascertained or identified for a given information level $\mathbb{F}$ ? In general, we can determine $\lambda$ under the conditions of Theorem 3.6 as the limit

$$
I(T>t) \lambda_{t}=\lim _{h \rightarrow 0+} \frac{1}{h} P\left(t<T \leq t+h \mid \mathcal{F}_{t}\right)
$$

in the sense of almost sure convergence. Another way to verify whether a given process $\lambda$ is the failure rate is to show that the corresponding hazard process defines the compensator of $I(T \leq t)$. In some special cases $\lambda$ can be represented in a more explicit form, as for example for complex systems. This will be carried out in some detail in the next section.

# 3.2.2 Failure Rate Processes in Complex Systems 

In the following we want to derive the hazard rate process for the lifetime $T$ of a complex system under fairly general conditions. We make no independence assumption concerning the component lifetimes, and we allow two or more components to fail at the same time with positive probability.

Let $T_{i}, i=1, \ldots, n$, be $n$ positive random variables that describe the component lifetimes of a monotone complex system with structure function $\Phi$. Our aim is to derive the failure rate process for the lifetime

$$
T=\inf \left\{t \in \mathbb{R}_{+}: \Phi\left(\mathbf{X}_{t}\right)=0\right\}
$$

with respect to the filtration $\mathbb{F}$ given by $\mathcal{F}_{t}=\sigma\left(\mathbf{X}_{s}, 0 \leq s \leq t\right)$, where as before $\mathbf{X}_{s}=\left(X_{s}(1), \ldots, X_{s}(n)\right)$ and $X_{s}(i)=I\left(T_{i}>s\right), i=1, \ldots, n$. We call this filtration the complete information filtration or filtration on the component level.

For a specific outcome $\omega$ let $m(\omega)$ be the number of different failure time points $0<T_{(1)}<T_{(2)}<\cdots<T_{(m)}$ and $J_{(k)}=\left\{i: T_{i}(\omega)=T_{(k)}(\omega)\right\}$ the set of components that fail at $T_{(k)}$. For completeness we define

$$
T_{(r)}=\infty, J_{(r)}=\emptyset \text { for } r \geq m+1
$$Thus, the sequence $\left(T_{(k)}, J_{(k)}\right), k \in \mathbb{N}$, forms a multivariate point process. Now we fix a certain failure pattern $J \subset\{1, \ldots, n\}$ and consider the time $T_{J}$ of occurrence of this pattern, i.e.,

$$
T_{J}= \begin{cases}T_{(k)} & \text { if } J_{(k)}=J \text { for some } k \\ \infty & \text { if } J_{(k)} \neq J \text { for all } k\end{cases}
$$

The corresponding counting process $V_{t}(J)=I\left(T_{J} \leq t\right)$ has a compensator $A_{t}(J)$ with respect to $\mathbb{F}$, which is assumed to be absolutely continuous such that $\lambda_{t}(J)$ is the $\mathbb{F}$-failure rate process:

$$
V_{t}(J)=\int_{0}^{t} I\left(T_{J}>s\right) \lambda_{s}(J) d s+M_{t}(J)
$$

In the case $P\left(T_{J}=\infty\right)=1$, we set $\lambda_{t}(J)=0$ for $t \in \mathbb{R}_{+}$.
Example 3.26. If we assume that the component lifetimes are independent random variables, the only interesting (nontrivial) failure patterns are those consisting of only one single component $J=\{j\}, j \in\{1, \ldots, n\}$. In this case the $\mathbb{F}$-failure rate processes $\lambda_{t}(\{j\})$ are merely the ordinary failure rates $\lambda_{t}(j)$ corresponding to $T_{j}$.

Example 3.27. We now consider the special case $n=2$ in which $\left(T_{1}, T_{2}\right)$ follows the bivariate exponential distribution of Marshall and Olkin (cf. [121]) with parameters $\beta_{1}, \beta_{2}>0$ and $\beta_{12} \geq 0$. A plausible interpretation of this distribution is as follows. Three independent exponential random variables $Z_{1}, Z_{2}, Z_{12}$ with corresponding parameters $\beta_{1}, \beta_{2}, \beta_{12}$ describe the time points when a shock causes failure of component 1 or 2 or all intact components at the same time, respectively. Then the component lifetimes are given by $T_{1}=Z_{1} \wedge Z_{12}$ and $T_{2}=Z_{2} \wedge Z_{12}$, and the joint survival probability is seen to be

$$
P\left(T_{1}>t, T_{2}>s\right)=\exp \left\{-\beta_{1} t-\beta_{2} s-\beta_{12}(t \vee s)\right\}, s, t \in \mathbb{R}_{+}
$$

The three different patterns to distinguish are $\{1\},\{2\},\{1,2\}$. Note that $T_{\{1\}} \neq T_{1}$ as we have for example $T_{\{1\}}=\infty$ on $\left\{T_{1}=T_{2}\right\}$, i.e., on $\left\{Z_{12}<Z_{1} \wedge Z_{2}\right\}$. Calculations then yield

$$
\lambda_{t}(\{1\})= \begin{cases}\beta_{1} & \text { on } \quad\left\{T_{1}>t, T_{2}>t\right\} \\ \beta_{1}+\beta_{12} & \text { on } \quad\left\{T_{1}>t, T_{2} \leq t\right\} \\ 0 & \text { elsewhere }\end{cases}
$$

$\lambda_{t}(\{2\})$ is given by obvious index interchanges, and

$$
\lambda_{t}(\{1,2\})= \begin{cases}\beta_{12} & \text { on } \quad\left\{T_{1}>t, T_{2}>t\right\} \\ 0 & \text { elsewhere }\end{cases}
$$

Now we have the $\mathbb{F}$-failure rate processes $\lambda(J)$ at hand for each pattern $J$. We are interested in deriving the $\mathbb{F}$-failure rate process $\lambda$ of $T$. The next theorem shows how this process $\lambda$ is composed of the single processes $\lambda(J)$on the component observation level $\mathbb{F}$. Here we remind the reader of some notation introduced in Chap. 2. For $\mathbf{x} \in \mathbb{R}^{n}$ and $J=\left\{j_{1}, \ldots, j_{r}\right\} \subset\{1, \ldots, n\}$, the vectors $\left(1_{J}, \mathbf{x}\right)$ and $\left(0_{J}, \mathbf{x}\right)$ denote those $n$-dimensional state vectors in which the components $x_{j_{1}}, \ldots, x_{j_{r}}$ of $\mathbf{x}$ are replaced by 1 s and 0 s , respectively. Let $D(t)$ be the set of components that have failed up to time $t$, formally

$$
D(t)=\left\{\begin{array}{cl}
J_{(1)} \cup \ldots \cup J_{(k)} & \text { if } T_{(k)} \leq t<T_{(k+1)} \\
\emptyset & \text { if } t<T_{(1)}
\end{array}\right.
$$

Then we define a pattern $J$ to be critical at time $t \geq 0$ if

$$
I\left(J \cap D(t)=\emptyset\right)\left(\Phi\left(1_{J}, \mathbf{X}_{t}\right)-\Phi\left(0_{J}, \mathbf{X}_{t}\right)\right)=1
$$

and denote by

$$
\Gamma_{\Phi}(t)=\left\{J \subset\{1, \ldots, n\}: I\left(J \cap D(t)=\emptyset\right)\left(\Phi\left(1_{J}, \mathbf{X}_{t}\right)-\Phi\left(0_{J}, \mathbf{X}_{t}\right)\right)=1\right\}
$$

the collection of all such patterns critical at $t$.
Theorem 3.28. Let $\left(\lambda_{t}(J)\right)$ be the $\mathbb{F}$-failure rate process corresponding to $T_{J}$, $J \subset\{1, \ldots, n\}$. Then for all $t \in \mathbb{R}_{+}$on $\{T>t\}$ :

$$
\lambda_{t}=\sum_{J \subset\{1, \ldots, n\}} I\left(J \cap D(t)=\emptyset\right)\left(\Phi\left(1_{J}, \mathbf{X}_{t}\right)-\Phi\left(0_{J}, \mathbf{X}_{t}\right)\right) \lambda_{t}(J)=\sum_{J \in \Gamma_{\Phi}(t)} \lambda_{t}(J)
$$

Proof. By Definition 3.8, p. 62, a predictable increasing process $\left(A_{t}\right)$ is the compensator of the counting process $\left(V_{t}\right), V_{t}=I(T \leq t)$, if

$$
E \int_{0}^{\infty} C_{s} d V_{s}=E \int_{0}^{\infty} C_{s} d A_{s}
$$

holds true for every nonnegative $\mathbb{F}$-predictable process $C$. Thus, we have to show that

$$
E \int_{0}^{\infty} C_{s} d V_{s}=E \int_{0}^{\infty} C_{s} I(T>s) \sum_{J \in \Gamma_{\Phi}(s)} \lambda_{s}(J) d s
$$

for all nonnegative predictable processes $C$. Since $\left(\lambda_{t}(J)\right)$ are the $\mathbb{F}$-failure rate processes corresponding to $T_{J}$, we have for all $J \subset\{1, \ldots, n\}$

$$
E \int_{0}^{\infty} C_{s}(J) d V_{s}(J)=E \int_{0}^{\infty} C_{s}(J) I\left(T_{J}>s\right) \lambda_{s}(J) d s
$$

and therefore

$$
E \int_{0}^{\infty} \sum_{J \subset\{1, \ldots, n\}} C_{s}(J) d V_{s}(J)=E \int_{0}^{\infty} \sum_{J \subset\{1, \ldots, n\}} C_{s}(J) I\left(T_{J}>s\right) \lambda_{s}(J) d s
$$holds true for all nonnegative predictable processes $\left(C_{t}(J)\right)$. If we especially choose for some nonnegative predictable process $C$

$$
C_{t}(J)=C_{t} f_{t-}
$$

where $f_{t-}$ is the left-continuous version of $f_{t}=I\left(J \in \Gamma_{\Phi}(t)\right)$, we see that (3.11) reduces to (3.10), noting that under the integral sign we can replace $f_{t-}$ by $f_{t}$, and the proof is complete.

Remark 3.29. (i) The proof follows the lines of Arjas (Theorem 4.1 in [6]) except the definition of the set $\Gamma_{\Phi}(t)$ of the critical failure patterns at time $t$. In [6] this set includes on $\{T>t\}$ all cut sets, whereas in our definition those cut sets $J$ are excluded for which at time $t$ "it is known" that $T_{J}=\infty$. However, this deviation is harmless because in [6] only extra zeros are added. (ii) We now have a tool that allows us to determine the failure rate process corresponding to the lifetime $T$ of a complex system in an easy way: Add at time $t$ the failure rates of those patterns that are critical at $t$.

As an immediate consequence we obtain the following corollary.
Corollary 3.30. Let $T_{i}, i=1, \ldots, n$, be independent random variables that have absolutely continuous distributions with ordinary failure rates $\lambda_{t}(i)$. Then the $\mathbb{F}$-failure rate processes $\lambda(\{i\})$ are deterministic, $\lambda_{t}(\{i\})=\lambda_{t}(i)$ and on $\{T>t\}$

$$
\lambda_{t}=\sum_{i=1}^{n}\left(\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right) \lambda_{t}(i)=\sum_{\{i\} \in \Gamma_{\Phi}(t)} \lambda_{t}(i), t \in \mathbb{R}_{+}
$$

In the case of independent component lifetimes we only have to add the ordinary failure rates of those components critical at $t$ to obtain the $\mathbb{F}$-failure rate of the system at time $t$. It is not enough to require that $P\left(T_{i}=T_{j}\right)=0$ for $i \neq j$ if we drop the independence assumption as the following example shows.

Example 3.31. Let $U_{1}, U_{2}$ be i.i.d. random variables from an $\operatorname{Exp}(\beta)$ distribution and $T_{1}=U_{1}, T_{2}=U_{1}+U_{2}$ be the component lifetimes of a two-component series system. Then we obviously have $P\left(T_{1}=T_{2}\right)=0$, but the $\mathbb{F}$-failure rate of $T_{\{2\}}=T_{2}$ on $\left\{T_{2}>t\right\}$

$$
\lambda_{t}(\{2\})=\beta I\left(T_{1} \leq t\right)
$$

is not deterministic. The system $\mathbb{F}$-failure rate is seen to be

$$
I(T>t) \lambda_{t}=I\left(T_{1}>t\right) \beta
$$

To see how formula (3.12) can be used we resume Example 3.22, p. 71.Example 3.32. Again we consider the three-component system with one component in series with a two-component parallel system such that the lifetime of the system is given by $T=T_{1} \wedge\left(T_{2} \vee T_{3}\right)$. It is assumed that the component lifetimes $T_{1}, T_{2}, T_{3}$ are i.i.d. exponentially distributed with parameter $\alpha>0$. If at time $t$ all three components work, then only component 1 belongs to $\Gamma_{\Phi}(t)$ and $I(T>t) \lambda_{t}=\alpha I\left(T_{1}>t\right)$ on $\left\{T_{2}>t, T_{3}>t\right\}$. If one of the components 2 or 3 has failed first before time $t$, say component 2 , then $\Gamma_{\Phi}(t)=\{\{1\},\{3\}\}$ and $I(T>t) \lambda_{t}=\alpha\left(I\left(T_{1}>t\right)+I\left(T_{3}>t\right)\right)$ on $\left\{T_{2} \leq t\right\}$. Combining these two formulas yields the failure rate process on $\{T>t\}$

$$
\lambda_{t}=\alpha\left(1+I\left(T_{2} \leq t\right)+I\left(T_{3} \leq t\right)\right)
$$

given in Example 3.22.
Example 3.33. We now go back to the pair $\left(T_{1}, T_{2}\right)$ of random variables, which follows the bivariate exponential distribution of Marshall and Olkin with parameters $\beta_{1}, \beta_{2}>0$ and $\beta_{12} \geq 0$ and consider a parallel system with lifetime $T=T_{1} \vee T_{2}$. Then on $\{T>t\}$ the critical patterns are

$$
\Gamma_{\Phi}(t)=\left\{\begin{array}{c}
\{1,2\} \text { on }\left\{T_{1}>t, T_{2}>t\right\} \\
\{1\} \text { on }\left\{T_{1}>t, T_{2} \leq t\right\} \\
\{2\} \text { on }\left\{T_{1} \leq t, T_{2}>t\right\}
\end{array}\right.
$$

Using the results of Example 3.27, p. 74, the $\mathbb{F}$-failure rate process of the system lifetime is seen to be

$$
\begin{aligned}
I(T>t) \lambda_{t}= & \beta_{12} I\left(T_{1}>t, T_{2}>t\right)+\left(\beta_{1}+\beta_{12}\right) I\left(T_{1}>t, T_{2} \leq t\right) \\
& +\left(\beta_{2}+\beta_{12}\right) I\left(T_{1} \leq t, T_{2}>t\right)
\end{aligned}
$$

which can be reduced to

$$
I(T>t) \lambda_{t}=\beta_{12} I(T>t)+\beta_{1} I\left(T_{1}>t, T_{2} \leq t\right)+\beta_{2} I\left(T_{1} \leq t, T_{2}>t\right)
$$

# 3.2.3 Monotone Failure Rate Processes 

We have investigated under which conditions failure rate processes exist and how they can be determined explicitly for complex systems. In reliability it plays an important role whether failure rates are monotone increasing or decreasing. So it is quite natural to extend such properties to $\mathbb{F}$-failure rates in the following way.

Definition 3.34. Let an $\mathbb{F}$-SSM representation (3.8) hold true for the positive random variable $T$ with failure rate process $\lambda$. Then $\lambda$ is called $\mathbb{F}$-increasing ( $\mathbb{F}$-IFR, increasing failure rate) or $\mathbb{F}$-decreasing ( $\mathbb{F}$-DFR, decreasing failure rate), if $\lambda$ has $P$-a.s. nondecreasing or nonincreasing paths, respectively, for $t \in[0, T)$.Remark 3.35. (i) Clearly, monotonicity properties of $\lambda$ are only of importance on the random interval $[0, T)$. On $[T, \infty)$ we can specify $\lambda$ arbitrarily. (ii) In the case of complex systems the above definition reflects both, the information level $\mathbb{F}$ and the structure function $\Phi$. An alternative definition, which is derived from notions of multivariate aging terms, is given by Arjas [5]; see also Shaked and Shanthikumar [140].

In the case of a complex system with independent component lifetimes, the following closure lemma can be established.

Proposition 3.36. Assume that in a monotone system the component lifetimes $T_{i}, i=1, \ldots, n$, are independent random variables with absolutely continuous distributions and ordinary nondecreasing failure rates $\lambda_{t}(i)$ and let $\mathbb{F}$ be the filtration on the component level. Then the $\mathbb{F}$-failure rate process $\lambda$ corresponding to the system lifetime $T$ is $\mathbb{F}$-IFR.

Proof. Under the assumptions of the lemma no patterns with two or more components are critical. Since the system is monotone, the number of elements in $\Gamma_{\Phi}(t)$ is nondecreasing in $t$. So from (3.12), p. 76, it can be seen that if all component failure rates are nondecreasing, the $\mathbb{F}$-failure rate process $\lambda$ is also nondecreasing for $t \in[0, T)$.

Such a closure theorem does not hold true for the ordinary failure rate of the lifetime $T$ as can be seen from simple counterexamples (see Sect. 2.2.1 or [32], p. 83). From the proof of Proposition 3.36 it is evident that we cannot draw an analogous conclusion for decreasing failure rates.

# 3.2.4 Change of Information Level 

One of the advantages of the semimartingale technique is the possibility of studying the random evolution of a stochastic process on different information levels. This was described in general in Sect.3.1.2 by the projection theorem, which says in which way an SSM representation changes when changing the filtration from $\mathbb{F}$ to a subfiltration $\mathbb{A}$. This projection theorem can be applied to the lifetime indicator process

$$
V_{t}=I(T \leq t)=\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}
$$

If the lifetime can be observed, i.e., $\{T \leq s\} \in \mathcal{A}_{s}$ for all $0 \leq s \leq t$, then the change of the information level from $\mathbb{F}$ to $\mathbb{A}$ leads from (3.13) to the representation

$$
\hat{V}_{t}=E\left[I(T \leq t) \mid \mathcal{A}_{t}\right]=I(T \leq t)=\int_{0}^{t} I(T>s) \hat{\lambda}_{s} d s+\hat{M}_{t}
$$where $\hat{\lambda}_{t}=E\left[\lambda_{t} \mid \mathcal{A}_{t}\right]$. Note that, in general, this formula only holds for almost all $t \in \mathbb{R}_{+}$. In all our examples we can find $\mathbb{A}$-progressive versions of the conditional expectations. The projection theorem shows that it is possible to obtain the failure rate on a lower information level merely by forming conditional expectations under some mild technical conditions.

Remark 3.37. Unfortunately, monotonicity properties are in general not preserved when changing the observation level. As was noted above (see Proposition 3.36), if all components of a monotone system have independent lifetimes with increasing failure rates, then $T$ is $\mathbb{F}$-IFR on the component observation level. But switching to a subfiltration $\mathbb{A}$ may lead to a nonmonotone failure rate process $\hat{\lambda}$.

The following example illustrates the role of partial information.
Example 3.38. Consider a two-component parallel system with i.i.d. random variables $T_{i}, i=1,2$, describing the component lifetimes, which follow an exponential distribution with parameter $\alpha>0$. Then the system lifetime is $T=T_{1} \vee T_{2}$ and the complete information filtration is given by

$$
\mathcal{F}_{t}=\sigma\left(I\left(T_{1}>s\right), I\left(T_{2}>s\right), 0 \leq s \leq t\right)
$$

In this case the $\mathbb{F}$-semimartingale representation (3.13) is given by

$$
\begin{aligned}
I(T \leq t) & =\int_{0}^{t} I(T>s) \alpha\left\{I\left(T_{1} \leq s\right)+I\left(T_{2} \leq s\right)\right\} d s+M_{t} \\
& =\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}
\end{aligned}
$$

Now several subfiltrations can describe different lower information levels where it is assumed that the system lifetime $T$ can be observed on all observation levels. Examples of partial information and the formal description via subfiltrations $\mathbb{A}$ and $\mathbb{A}$-failure rates are as follows:
a) Information about $T$ until $h$, after $h$ complete information.

$$
\begin{aligned}
\mathcal{A}_{t}^{a} & =\left\{\begin{array}{lll}
\sigma\left(I(T \leq s), 0 \leq s \leq t\right) & \text { for } & 0 \leq t<h \\
\mathcal{F}_{t} & \text { for } & t \geq h
\end{array}\right. \\
\hat{\lambda}_{t}^{a} & =\left\{\begin{array}{lll}
2 \alpha\left(1-\left(2-e^{-\alpha t}\right)^{-1}\right) & \text { for } & 0 \leq t<h \\
\lambda_{t} & \text { for } & t \geq h
\end{array}\right.
\end{aligned}
$$

b) Information about component lifetime $T_{1}$ and $T$ :

$$
\begin{aligned}
\mathcal{A}_{t}^{b} & =\sigma\left(I(T \leq s), I\left(T_{1} \leq s\right), 0 \leq s \leq t\right) \\
\hat{\lambda}_{t}^{b} & =\alpha\left(I\left(T_{1} \leq t\right)+I\left(T_{1}>t\right) P\left(T_{2} \leq t\right)\right)
\end{aligned}
$$c) Information about $T$ only:

$$
\begin{aligned}
\mathcal{A}_{t}^{c} & =\sigma(I(T \leq s), 0 \leq s \leq t) \\
\hat{\lambda}_{t}^{c} & =2 \alpha\left(1-\left(2-e^{-\alpha t}\right)^{-1}\right)
\end{aligned}
$$

The failure rate corresponding to $\mathbb{A}^{c}$ of this example is the standard deterministic failure rate, because $\{T>t\}$ is an atom of $\mathcal{A}_{t}^{c}$ (there is no subset of $\{T>t\}$ in $\mathcal{A}_{t}^{c}$ of positive probability) so that $\hat{\lambda}^{c}$ can always be chosen to be deterministic on $\{T>t\}$. This corresponds to our intuition because on this information level we cannot observe any other random event before $T$. Example 3.21 shows that such deterministic failure rates satisfy the wellknown exponential formula (3.9), p. 71. An interesting question to ask is then: under what conditions will such an exponential formula also extend to random failure rate processes? This question is referred to briefly in [4] and answered in [165] to some extent. The following treatment differs slightly in that the starting point is the basic lifetime model of this section. The failure rate process $\lambda$ is assumed to be observable on some level $\mathbb{A}$, i.e., $\lambda$ is adapted to that filtration. This observation level can be somewhere between the trivial filtration $\mathbb{G}=\left(\mathcal{G}_{t}\right), t \in \mathbb{R}_{+}, \mathcal{G}_{t}=\{\emptyset, \Omega\}$, which does not allow for any random information, and the basic complete information filtration $\mathbb{F}$. So $T$ itself need not be observable at level $\mathbb{A}$ (and should not, if we want to arrive at an exponential formula). Using the projection theorem we obtain

$$
E\left[I(T \leq t) \mid \mathcal{A}_{t}\right]=1-\bar{F}_{t}=\int_{0}^{t} \bar{F}_{s} \lambda_{s} d s+\bar{M}_{t}
$$

where $\bar{F}$ denotes the conditional survival probability,

$$
\bar{F}_{t}=E\left[I(T>t) \mid \mathcal{A}_{t}\right]=P\left(T>t \mid \mathcal{A}_{t}\right)
$$

and $\bar{M}$ is an $\mathbb{A}$-martingale. In general, $\bar{F}$ need not be monotone and can be rather irregular. But if $\bar{F}$ has continuous paths of bounded variation, then the martingale $\bar{M}$ is identically 0 and the solution of the resulting integral equation is

$$
\bar{F}_{t}=\exp \left\{-\int_{0}^{t} \lambda_{s} d s\right\}
$$

which is a generalization of formula (3.9). If $\mathbb{A}$ is the trivial filtration $\mathbb{G}$, then (3.16) coincides with (3.9). For (3.16) to hold, it is necessary that the observation of $\lambda$ and other events on level $\mathbb{A}$ only have "smooth" influence on the conditional survival probability.

Remark 3.39. This is a more technical remark to show how one can proceed if $\bar{F}$ is not continuous. Let $\left(\bar{F}_{t-}\right), t \in \mathbb{R}_{+}$, be the left-continuous version of $\bar{F}$. Equation (3.15) can be rewritten as

$$
\bar{F}_{t}=1-\int_{0}^{t} \bar{F}_{s-} \lambda_{s} d s-\bar{M}_{t}
$$Under mild conditions an $\mathbb{A}$-martingale $L$ can be found such that $\bar{M}$ can be represented as the (stochastic) integral $\bar{M}_{t}=\int_{0}^{t} \bar{F}_{s-} d L_{s}$, take

$$
L_{t}=\int_{0}^{t} \frac{I\left(\bar{F}_{s-}>0\right)}{\bar{F}_{s-}} d \bar{M}_{s}
$$

With the semimartingale $Z, Z_{t}=-\int_{0}^{t} \lambda_{s} d s-L_{t}$, (3.15) becomes

$$
\bar{F}_{t}=1+\int_{0}^{t} \bar{F}_{s-} d Z_{s}
$$

If $Z$ is of locally finite variation then the unique solution of this integral equation is given by the so-called Doléans exponential (see [101], p. 440)

$$
\begin{aligned}
\bar{F}_{t} & =\mathcal{E}\left(Z_{t}\right)=\exp \left\{Z_{t}^{c}\right\} \prod_{0<s \leq t}\left(1+\Delta Z_{s}\right) \\
& =\exp \left\{-\int_{0}^{t} \lambda_{s} d s\right\} \exp \left\{-L_{t}^{c}\right\} \prod_{0<s \leq t}\left(1-\Delta L_{s}\right)
\end{aligned}
$$

where $Z^{c}\left(L^{c}\right)$ denotes the continuous part of $Z(L)$ and $\Delta Z_{s}=Z_{s}-Z_{s-}\left(\Delta L_{s}=\right.$ $\left.L_{s}-L_{s-}\right)$ denotes the jump height at $s$. This extended exponential formula shows that possible jumps of the conditional survival probability are not caused by jumps of the failure rate process but by (unpredictable) jumps of the martingale part.

# 3.3 Point Processes in Reliability: Failure Time and Repair Models 

A number of models in reliability are described by point processes and their corresponding counting processes. As examples we can think of shock models, in which shocks affecting a technical system arrive at random time points $T_{n}$ according to a point process causing some damage of random amount $V_{n}$, or we can think of repair models, in which failures occur at random time points $T_{n}$ causing random repair costs $V_{n}$. In both cases the sequence $\left(T_{n}, V_{n}\right)$ is a multivariate or marked point process to be introduced as follows.

Definition 3.40. Let $\left(T_{n}\right), n \in \mathbb{N}$, be a point process and $\left(V_{n}\right), n \in \mathbb{N}$, a sequence of random variables taking values in a measurable space $(S, \mathcal{S})$. Then a marked point process $\left(T_{n}, V_{n}\right), n \in \mathbb{N}$, is the ordered sequence of time points $T_{n}$ and marks $V_{n}$ associated with the time points, and $(S, \mathcal{S})$ is called the mark space.

The mark $V_{n}$ describes the event occurring at time $T_{n}$, for example the magnitude of the shock arriving at a system at time $T_{n}$ (see Fig. 3.1). For each $A \in \mathcal{S}$ we associate the counting process $\left(N_{t}(A)\right), t \in \mathbb{R}_{+}$,

Fig. 3.1. Marked point process

$$
N_{t}(A)=\sum_{n=1}^{\infty} I\left(V_{n} \in A\right) I\left(T_{n} \leq t\right)
$$

which counts the number of marked points up to time $t$ with marks in $A$. This family of counting processes $N$ carries the same information as the sequence $\left(T_{n}, V_{n}\right)$ and is therefore an equivalent description of the marked point process.

Example 3.41. A point process $\left(T_{n}\right)$ can be viewed as a marked point process for which $S$ consists of a single point. Another link between point and marked point processes is given by the counting process $N=\left(N_{t}\right), N_{t}=N_{t}(S)$, which corresponds to the sequence $\left(T_{n}\right)$.

Example 3.42 (Alternating Renewal Process). Consider a system, which is repaired or replaced after failure (models of this kind are treated in detail in Sect.4.2). Let $U_{k}$ represent the length of the $k$ th operation period and $R_{k}$ the length of the $k$ th repair/replacement time. Assume that $\left(U_{k}\right)$ and $\left(R_{k}\right), k \in \mathbb{N}$, are independent i.i.d. sequences of positive random variables. Let the mark space be $S=\{0,1\}$, where 0 and 1 stand for "repair/replacement completed" and "failure", respectively. Then the random time points $T_{n}$ are

$$
T_{n}=\sum_{k=1}^{\left[\frac{n+1}{2}\right]} U_{k}+\sum_{k=1}^{\left[\frac{n}{2}\right]} R_{k}, n=1,2, \ldots
$$

where $[a]$ denotes the integer part of $a$. The mark sequence is deterministic and alternating between 0 and 1 :

$$
V_{n}=\frac{1}{2}\left(1+(-1)^{n+1}\right)
$$

We see that $N_{t}(\{0\})$ counts the number of number of completed repairs and $N_{t}(\{1\})$ failures up to time $t$.We now want to extend the concept of stochastic intensities from point processes to marked point processes. The internal filtration $\mathbb{F}^{N}$ of $\left(T_{n}, V_{n}\right)$ is defined by

$$
\mathcal{F}_{t}^{N}=\sigma\left(N_{s}(A), 0 \leq s \leq t, A \in \mathcal{S}\right)
$$

This filtration is equivalently generated by the history $\left\{\left(T_{n}, V_{n}\right), T_{n} \leq t\right\}$ of the marked point process.

Definition 3.43. Let $\mathbb{F}$ be some filtration including $\mathbb{F}^{N}: \mathcal{F}_{t}^{N} \subset \mathcal{F}_{t}, t \in \mathbb{R}_{+}$. A stochastic process $\left(\lambda_{t}(A), t \in \mathbb{R}_{+}, A \in \mathcal{S}\right)$ is called the stochastic intensity of the marked point process $N$, if $(i)$ for each $t, A \rightarrow \lambda_{t}(A)$ is a random measure on $\mathcal{S}$; (ii) for each $A \in \mathcal{S}, N_{t}(A)$ admits the $\mathbb{F}$-intensity $\lambda_{t}(A)$.

We can now formulate the extension of Theorem 3.12, p. 64, to marked point processes (cf. [50], p. 238, [92, 115], p. 22).

Theorem 3.44. Let $N$ be an integrable marked point process and $\mathbb{F}^{N}$ its internal filtration. Suppose that for each $n$ there exists a regular conditional distribution of $\left(U_{n+1}, V_{n+1}\right), U_{n+1}=T_{n+1}-T_{n}$, given the past $\mathcal{F}_{T_{n}}^{N}$ of the form

$$
\begin{aligned}
G_{n}(\omega, A, B) & =P\left(U_{n+1} \in A, V_{n+1} \in B \mid \mathcal{F}_{T_{n}}^{N}\right)(\omega) \\
& =\int_{A} g_{n}(\omega, s, B) d s
\end{aligned}
$$

where $g_{n}(\omega, s, B)$ is, for fixed $B$, a measurable function and, for fixed $(\omega, s)$, a finite measure on $(S, \mathcal{S})$. Then the process given by

$$
\lambda_{t}(C)=\frac{g_{n}\left(t-T_{n}, C\right)}{G_{n}\left(\left[t-T_{n}, \infty\right), S\right)}=\frac{g_{n}\left(t-T_{n}, C\right)}{1-\int_{0}^{t-T_{n}} g_{n}(s, S) d s}
$$

on $\left(T_{n}, T_{n+1}\right]$ is a stochastic intensity of $N$ and for each $C \in \mathcal{S}$,

$$
N_{t}(C)-\int_{0}^{t} \lambda_{s}(C) d s
$$

is an $\mathbb{F}^{N}$-martingale.
To find the SSM representation of a stochastic process, which is derived from a marked point process, we can make use of the intensity of the latter. The following theorem is proved in Brémaud [50], p. 235. For the formulation of this result it is more convenient to use a slightly different notation for the process $N_{t}(C)$, namely,

$$
N_{t}(C)=N(t, C)=\sum_{n=1}^{\infty} I\left(V_{n} \in C\right) I\left(T_{n} \leq t\right)
$$Theorem 3.45. Let $(N(t, C)), t \in \mathbb{R}_{+}, C \in \mathcal{S}$, be an integrable marked point process admitting the intensity $\lambda_{t}(C)$ with respect to some filtration $\mathbb{F}$. Let $H(t, z)$ be an $S$-marked $\mathbb{F}$-predictable process, such that, for all $t \in \mathbb{R}_{+}$, we have

$$
E \int_{0}^{t} \int_{S}|H(s, z)| \lambda_{s}(d z) d s<\infty
$$

Then, defining $M(d s, d z)=N(d s, d z)-\lambda_{s}(d z) d s$,

$$
\int_{0}^{t} \int_{S} H(s, z) M(d s, d z)
$$

is an $\mathbb{F}$-martingale.
In the following subsections we consider some examples and particular cases. As was mentioned in Example 3.41 a point process $\left(T_{n}\right)$ and its associated counting process $\left(N_{t}\right)$ are special cases of marked point processes. Point process models in our SSM set-up require the assumption that the counting process $\left(N_{t}\right), t \in \mathbb{R}_{+}$, on a filtered probability space $(\Omega, \mathcal{F}, \mathbb{F}, P)$ has an absolutely continuous compensator or, what amounts to the same, admits an $\mathbb{F}$-SSM representation

$$
N_{t}=\int_{0}^{t} \lambda_{s} d s+M_{t}
$$

This point process model is consistent with the general lifetime model considered in Sect.3.2. If the process $N$ is stopped at $T_{1}$, then (3.17) reduces to (3.13):

$$
\begin{aligned}
N_{t \wedge T_{1}} & =I\left(T_{1} \leq t\right)=\int_{0}^{t \wedge T_{1}} \lambda_{s} d s+M_{t \wedge T_{1}} \\
& =\int_{0}^{t} I\left(T_{1}>s\right) \lambda_{s} d s+M_{t}^{\prime}
\end{aligned}
$$

where $M^{\prime}$ is the stopped martingale $M, M_{t}^{\prime}=M_{t \wedge T_{1}}$. The time to first failure or shock corresponds to the lifetime $T=T_{1}$.

In general, $N$ is determined by its compensator or by its intensity $\lambda$, and it is possible to construct a point process $N$ (and a corresponding probability measure) from a given intensity $\lambda$ (these problems are considered in some detail in [92], see also [115], Chap. 8). This allows us to define point process models in reliability by considering a given intensity.

# 3.3.1 Alternating Renewal Processes: One-Component Systems with Repair 

We resume Example 3.42, p. 82, and assume that the operating times $U_{k}$ follow a distribution $F$ with density $f$ and failure rate $\rho(t)=f(t) / \tilde{F}(t)$, whereas the repair times follow a distribution $G$ with density $g$ and hazard rate$\eta(t)=g(t) / \bar{G}(t)$. Note that the failure/hazard rate is always set to 0 outside the support of the distribution. Then $N_{t}(\{0\})$ counts the number of failures up to time $t$ with an intensity $\lambda_{t}(\{0\})=\rho\left(t-T_{n}\right) X(t)$ on $\left(T_{n}, T_{n+1}\right]$, where $X(t)=V_{n}$ on $\left(T_{n}, T_{n+1}\right]$ indicates whether the system is up or down at $t$. The corresponding internal intensity for $N_{t}(\{1\})$ is $\lambda_{t}(\{1\})=\eta\left(t-T_{n}\right)(1-X(t))$. If the operating times are exponentially distributed with rate $\rho>0$, the expected number of failures up to time $t$ is given by

$$
E N_{t}(\{0\})=\rho \int_{0}^{t} E X(s) d s
$$

# 3.3.2 Number of System Failures for Monotone Systems 

We now consider a monotone system comprising $m$ independent components. For each component we define an alternating renewal process, indexed by " $i$." The operating and repair times $U_{i k}$ and $R_{i k}$, respectively, are independent i.i.d. sequences with distributions $F_{i}$ and $G_{i}$. We make the assumption that the up-time distributions $F_{i}$ are absolutely continuous with failure rates $\lambda_{t}(i)$. The point process $\left(T_{n}\right)$ is the superposition of the $m$ independent alternating renewal processes $\left(T_{i n}\right), i=1, \ldots, m$, and the associated counting process is merely the sum of the single counting processes. Since we are only interested in the occurrence of failures now, we denote by $N_{t}(i)$ the number of failures of component $i$ (omitting the argument $\{0\}$ ) and the total number of component failures by $N_{t}=\sum_{i=1}^{m} N_{t}(i)$. The time $T_{n}$ records the occurrence of a component failure or completion of a repair. As in Chap. 2, $\Phi: A \rightarrow\{0,1\}$ is the structure function, where $A=\{0,1\}^{m}$, and the process $\mathbf{X}_{t}=\left(X_{t}(1), \ldots, X_{t}(m)\right)$ denotes the vector of component states at time $t$ with values in $A$. The mark space is $S=A \times A$ and the value of $V_{n}=\left(\mathbf{X}_{T_{n}-}, \mathbf{X}_{T_{n}}\right)$ describes the change of the component states occurring at time $T_{n}$, where we set $V_{0}=\{(1, \ldots, 1),(1, \ldots, 1)\}$, i.e., we start with intact components at $T_{0}=0$. Note that $V_{n}=(\mathbf{x}, \mathbf{y})$ means that $\mathbf{y}=\left(0_{i}, \mathbf{x}\right)$ or $\mathbf{y}=\left(1_{i}, \mathbf{x}\right)$ for some $i \in\{1, \ldots, m\}$, because we have absolutely continuous up-time distributions so that at time $T_{n}$ only one component changes its status. Combining Corollary 3.30, p. 76, and Theorem 3.44, p. 83, we get the following result.

Corollary 3.46. Let $\Gamma=\{(\mathbf{x}, \mathbf{y}) \in S: \Phi(\mathbf{x})=1, \Phi(\mathbf{y})=0, \mathbf{y}=\left(0_{j}, \mathbf{x}\right)$ for some $j \in\{1, \ldots, m\}\}$ be the set of marks indicating a system failure. Then the process

$$
N_{t}(\Gamma)=\sum_{i=1}^{m} \int_{0}^{t}\left\{\Phi\left(1_{i}, \mathbf{X}_{s}\right)-\Phi\left(0_{i}, \mathbf{X}_{s}\right)\right\} d N_{s}(i)
$$

counting the number of system failures up to time $t$ admits the intensity

$$
\lambda_{t}(\Gamma)=\sum_{i=1}^{m}\left\{\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right\} \rho_{t}(i) X_{t}(i)
$$with respect to the internal filtration, where

$$
\rho_{t}(i)=\sum_{k=0}^{\infty} \lambda_{t-T_{i k}}(i) I\left(T_{i k}<t \leq T_{i, k+1}\right)
$$

Proof. We know that $\rho_{t}(i) X_{t}(i)$ are intensities of $N_{t}(i)$ and thus

$$
M_{t}(i)=N_{t}(i)-\int_{0}^{t} \rho_{s}(i) X_{s}(i) d s
$$

defines a martingale (also with respect to the internal filtration of the superposition because of the independence of the component processes). Define

$$
\Delta \Phi_{t}(i)=\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)
$$

and let $\Delta \Phi_{t-}(i)$ be the left-continuous and therefore predictable version of this process. Since at a jump of $N_{t}(i)$ no other components change their status ( $P$-a.s.), we have

$$
\int_{0}^{t} \Delta \Phi_{s}(i) d N_{s}(i)=\int_{0}^{t} \Delta \Phi_{s-}(i) d N_{s}(i)
$$

It follows that

$$
\begin{aligned}
N_{t}(\Gamma)-\int_{0}^{t} \lambda_{s}(\Gamma) d s & =\int_{0}^{t} \sum_{i=1}^{m} \Delta \Phi_{s}(i) d M_{s}(i) \\
& =\int_{0}^{t} \sum_{i=1}^{m} \Delta \Phi_{s-}(i) d M_{s}(i)
\end{aligned}
$$

But the last integral is the sum of integrals of bounded, predictable processes and so by Theorem 3.45 is a martingale, which proves the assertion.

To determine the expected number of system failures up to time $t$, we observe that $E M_{t}(i)=0$, i.e., $E N_{t}(i)=\int_{0}^{t} m_{s}(i) d s$ with $m_{s}(i)=E \rho_{s}(i) X_{s}(i)$, and that $\Delta \Phi_{t}(i)$ and $\rho_{t}(i) X_{t}(i)$ are stochastically independent. This results in

$$
E N_{t}(\Gamma)=\int_{0}^{t} \sum_{i=1}^{m} E\left[\Delta \Phi_{s}(i)\right] m_{s}(i) d s
$$

# 3.3.3 Compound Point Process: Shock Models 

Let us now assume that a system is exposed to shocks at random times $\left(T_{n}\right)$. A shock occurring at $T_{n}$ causes a random amount of damage $V_{n}$ and these damages accumulate. The marked point process $\left(T_{n}, V_{n}\right)$ with mark space $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ describes this shock process. To avoid notational difficultieswe write in this subsection $N(t, C)$ for the associated counting processes, describing the number of shocks up to time $t$ with amounts in $C$. We are interested in the so-called compound point process

$$
X_{t}=\sum_{n=1}^{N(t)} V_{n}
$$

with $N(t)=N(t, \mathbb{R})$, which gives the total damage up to $t$, and we want to derive the infinitesimal characteristics or the "intensity" of this process, i.e., to establish an SSM representation. We might also think of repair models, in which failures occur at random time points $T_{n}$. Upon failure, repair is performed. If the cost for the $n$th repair is $V_{n}$, then $X_{t}$ describes the accumulated costs up to time $t$.

To derive an SSM representation of $X$, we first assume that we are given a general intensity $\lambda_{t}(C)$ of the marked point process with respect to some filtration $\mathbb{F}$. The main point now is to observe that

$$
X_{t}=\int_{0}^{t} \int_{S} z N(d s, d z)
$$

Then we can use Theorem 3.45, p. 84, with the predictable process $H(s, z)=z$ to see that

$$
M_{t}^{\mathbb{F}}=\int_{0}^{t} \int_{S} z\left(N(d s, d z)-\lambda_{s}(d z) d s\right)
$$

is a martingale if $E \int_{0}^{t} \int_{S}|z| \lambda_{s}(d z) d s<\infty$. Equivalently, we see that $X$ has the $\mathbb{F}$-SSM representation $X=\left(f, M^{\mathbb{F}}\right)$, with

$$
f_{s}=\int_{S} z \lambda_{s}(d z)
$$

To come to a more explicit representation we make the following assumptions $(\mathbf{A})$ :

- The filtration is the internal one $\mathbb{F}^{N}$;
- $U_{n+1}=T_{n+1}-T_{n}$ is independent of $\mathcal{F}_{T_{n}}^{N} \vee \sigma\left(V_{n+1}\right)$;
- $U_{n+1}$ has absolutely continuous distribution with density $g_{n}(t)$ and (ordinary) failure or hazard rate $r_{n}(t)$;
- $V_{n+1}$ is a positive random variable, independent of $\mathcal{F}_{T_{n}}^{N}$, with finite mean $E V_{n+1}$.
Under these assumptions we get by Theorem 3.44, p. 83,

$$
\lambda_{t}(C)=\sum_{n=0}^{\infty} r_{n}\left(t-T_{n}\right) P\left(V_{n+1} \in C\right) I\left(T_{n}<t \leq T_{n+1}\right)
$$and therefore the SSM representation

$$
X_{t}=\int_{0}^{t} \sum_{n=0}^{\infty} E\left[V_{n+1}\right] r_{n}\left(s-T_{n}\right) I\left(T_{n}<s \leq T_{n+1}\right) d s+M_{t}^{\mathbb{P}^{N}}
$$

In the case of constant expectations $E V_{n}=E V_{1}$ we have

$$
f_{s}=E\left[V_{1}\right] \lambda_{s}(\mathbb{R})
$$

# 3.3.4 Shock Models with State-Dependent Failure Probability 

Now we introduce a failure mechanism in which the marks $V_{n}=\left(Y_{n}, W_{n}\right)$ are pairs of random variables, where $Y_{n}, Y_{n}>0$, represents the amount of damage caused by the $n$th shock and $W_{n}$ equals 1 or 0 according to whether the system fails or not at the $n$th shock. Upon failure, repair is performed. So the marks $V_{n}$ take values in $S=\mathbb{R}_{+} \times\{0,1\}$. The associated counting process is $N\left(t, \mathbb{R}_{+} \times\{0,1\}\right)$, and $\widetilde{N}(t)=N\left(t, \mathbb{R}_{+} \times\{1\}\right)$ counts the number of failures up to time $t$. The accumulated damage is described by

$$
X_{t}=\sum_{n=1}^{N(t, S)} Y_{n}
$$

In addition to (A), p. 87, we now assume

- $Y_{n+1}$ is independent of $\mathcal{F}_{T_{n}}^{N}$ with distribution

$$
F_{n+1}(y)=P\left(Y_{n+1} \leq y\right)
$$

- For each $k \in \mathbb{N}_{0}$ there exists a measurable function $p_{k}(x)$ such that $0 \leq$ $p_{k}(x) \leq 1$ and

$$
P\left(W_{n+1}=1 \mid \mathcal{F}_{T_{n}}^{N} \vee \sigma\left(Y_{n+1}\right)\right)=p_{\widetilde{N}\left(T_{n}\right)}\left(X_{T_{n}}+Y_{n+1}\right)
$$

Note that $\mathcal{F}_{T_{n}}^{N}=\sigma\left(\left(T_{i}, Y_{i}, W_{i}\right), i=1, \ldots, n\right)$ and that

$$
\widetilde{N}\left(T_{n}\right)=\sum_{i=1}^{n} W_{i}, X_{T_{n}}=\sum_{i=1}^{n} Y_{i}
$$

The assumption (3.19) can be interpreted as follows: if the accumulated damage is $x$ and $k$ failures have already occurred, then an additional shock of magnitude $y$ causes the system to fail with probability $p_{k}(x+y)$.

To derive the compensator of $N\left(t, \mathbb{R}_{+} \times\{1\}\right)$, the number of failures up to time $t$, we observe that

$$
\begin{aligned}
& P\left(U_{n+1} \in A, Y_{n+1} \in \mathbb{R}_{+}, W_{n+1}=1 \mid \mathcal{F}_{T_{n}}^{N}\right) \\
& \quad=P\left(U_{n+1} \in A\right) P\left(W_{n+1}=1 \mid \mathcal{F}_{T_{n}}^{N}\right) \\
& \quad=P\left(U_{n+1} \in A\right) E\left[p_{\widetilde{N}\left(T_{n}\right)}\left(X_{T_{n}}+Y_{n+1}\right) \mid \mathcal{F}_{T_{n}}^{N}\right]
\end{aligned}
$$Then Theorem 3.44 yields the intensity on $\left\{T_{n}<t \leq T_{n+1}\right\}$ :

$$
\lambda_{t}\left(\mathbb{R}_{+} \times\{1\}\right)=r_{n}\left(t-T_{n}\right) E\left[p_{\widetilde{N}\left(T_{n}\right)}\left(X_{T_{n}}+Y_{n+1}\right) \mid \mathcal{F}_{T_{n}}^{N}\right]
$$

Example 3.47. As a shock arrival process we now consider a Poisson process with rate $\nu, 0<\nu<\infty$, and an i.i.d. sequence of shock amounts with common distribution $F$. Then we get

$$
\lambda_{t}\left(\mathbb{R}_{+} \times\{1\}\right)=\nu \int_{0}^{\infty} p_{\widetilde{N}(t)}\left(X_{t}+y\right) d F(y)
$$

If the failure probability does not depend on the number of failures $\widetilde{N}$ and the shock magnitudes are deterministic, $Y_{n}=1$, then we have

$$
\lambda_{t}\left(\mathbb{R}_{+} \times\{1\}\right)=v p\left(N_{t}+1\right)
$$

To derive a semimartingale description of the first time to failure

$$
T=\inf \left\{T_{n}: W_{n}=1\right\}
$$

we simply stop the counting process $\widetilde{N}$ at the $\mathbb{F}^{N}$-stopping time $T$ and get

$$
\begin{aligned}
I(T \leq t) & =\widetilde{N}(t \wedge T)=\int_{0}^{t \wedge T} \lambda_{s}\left(\mathbb{R}_{+} \times\{1\}\right) d s+M_{t \wedge T} \\
& =\int_{0}^{t} I(T>s) \lambda_{s}\left(\mathbb{R}_{+} \times\{1\}\right) d s+M_{t \wedge T}
\end{aligned}
$$

where $M$ is a martingale. The time to first failure admits a failure rate process, which is just the intensity of the counting process $\widetilde{N}$.

# 3.3.5 Shock Models with Failures of Threshold Type 

The situation is as above; we only change the failure mechanism in that the first time to failure $T$ is defined as the first time the accumulated damage reaches or exceeds a given threshold $K \in \mathbb{R}_{+}$:

$$
T=\inf \left\{t \in \mathbb{R}_{+}: \sum_{i=1}^{N(t, S)} Y_{i} \geq K\right\}=\inf \left\{T_{n}: \sum_{i=1}^{n} Y_{i} \geq K\right\}
$$

This is the hitting time of the set $[K, \infty)$.
This failure model seems to be quite different from the previous one. However, we see that it is just a special case setting the failure probability function $p_{k}(x)$ of (3.19) for all $k$ equal to the indicator of the interval $[K, \infty)$ :

$$
p_{k}(x)=p(x)=I_{[K, \infty)}(x)
$$Then we get

$$
\begin{aligned}
P\left(W_{n+1}=1 \mid \mathcal{F}_{T_{n}}^{N}\right) & =E\left[p\left(X_{T_{n}}+Y_{n+1}\right) \mid \mathcal{F}_{T_{n}}^{N}\right] \\
& =P\left(Y_{n+1}+X_{T_{n}} \geq K \mid \mathcal{F}_{T_{n}}^{N}\right) \\
& =1-F_{n+1}\left(\left(K-X_{T_{n}}\right)-\right)
\end{aligned}
$$

This can be interpreted as follows: If the accumulated damage after $n$ shocks is $x$, then the system fails with probability $P\left(Y_{n+1} \geq K-x\right)$ when the next shock occurs, which is the probability that the total damage hits the threshold $K$. Obviously, all shocks after $T$ are counted by $\widetilde{N}(t)=N\left(t, \mathbb{R}_{+} \times\{1\}\right)$. The failure counting process $\widetilde{N}$ has on $\left\{T_{n}<t \leq T_{n+1}\right\}$ the intensity

$$
\lambda_{t}\left(\mathbb{R}_{+} \times\{1\}\right)=r_{n}\left(t-T_{n}\right)\left\{1-F_{n+1}\left(\left(K-X_{T_{n}}\right)-\right)\right\}
$$

The first time to failure is described by

$$
I(T \leq t)=\int_{0}^{t} I(T>s) \lambda_{s}\left(\mathbb{R}_{+} \times\{1\}\right) d s+M_{t}
$$

with a suitable martingale $M$.
Example 3.48. Let us again consider the compound Poisson case with shock arrival rate $\nu$ and $F_{n}=F$ for all $n \in \mathbb{N}_{0}$. Since $r_{n}\left(s-T_{n}\right)=\nu$ and $\left(K-X_{T_{n}}\right)=$ $\left(K-X_{t}\right)$ on $\left\{T_{n}<t<T_{n+1}\right\}$, we get

$$
I(T \leq t)=\int_{0}^{t} I(T>s) \nu \bar{F}\left(\left(K-X_{s}\right)-\right) d s+M_{t}
$$

# 3.3.6 Minimal Repair Models 

In the literature covering repair models special attention has been given to so-called minimal repair models. Instead of replacing a failed system by a new one, a repair restores the system to a certain degree. These minimal repairs are often verbally described (and defined) as in the following:

- "The ...assumption is made that the system failure rate is not disturbed after performing minimal repair. For instance, after replacing a single tube in a television set, the set as a whole will be about as prone to failure after the replacement as before the tube failure" (Barlow and Hunter [30]).
- "A minimal repair is one which leaves the unit in precisely the condition it was in immediately before the failure" (Phelps [129]).

The definition of the state of the system immediately before failure depends to a considerable degree on the information one has about the system. So it makes a difference whether all components of a complex system are observed or only failure of the whole system is recognized. In the first case the lifetime of the repaired component (tube of TV set) is associated with the residualsystem lifetime. In the second case the only information about the condition of the system immediately before failure is the age. So a minimal repair in this case would mean replacing the system (the whole TV set) by another one of the same age that as yet has not failed. Minimal repairs of this kind are also called black box or statistical minimal repairs, whereas the component-wise minimal repairs are also called physical minimal repairs.

Example 3.49. We consider a simple two-component parallel system with independent $\operatorname{Exp}(1)$ distributed component lifetimes $X_{1}, X_{2}$ and allow for exactly one minimal repair.

- Physical minimal repair. After failure at $T=T_{1}=X_{1} \vee X_{2}$ the component that caused the system to fail is repaired minimally. Since the component lifetimes are exponentially distributed, the additional lifetime is given by an $\operatorname{Exp}(1)$ random variable $X_{3}$ independent of $X_{1}$ and $X_{2}$. The total lifetime $T_{1}+X_{3}$ has distribution

$$
P\left(T_{1}+X_{3}>t\right)=e^{-t}\left(2 t+e^{-t}\right)
$$

- Black box minimal repair. The lifetime $T=T_{1}=X_{1} \vee X_{2}$ until the first failure of the system has distribution $P\left(T_{1} \leq t\right)=\left(1-e^{-t}\right)^{2}$ and failure rate $\lambda(t)=2 \frac{1-\exp (-t)}{2-\exp (-t)}$. The additional lifetime $T_{2}-T_{1}$ until the second failure is assumed to have conditional distribution

$$
P\left(T_{2}-T_{1} \leq x \mid T_{1}=t\right)=P\left(T_{1} \leq t+x \mid T_{1}>t\right)=1-e^{-x} \frac{2-e^{-(t+x)}}{2-e^{-t}}
$$

Integrating leads to the distribution of the total lifetime $T_{2}$ :

$$
P\left(T_{2}>t\right)=e^{-t}\left(2-e^{-t}\right)\left(1+t-\ln \left(2-e^{-t}\right)\right)
$$

It is (perhaps) no surprise that the total lifetime after a black box minimal repair is stochastically greater than after a physical minimal repair:

$$
P\left(T_{2}>t\right) \geq P\left(T_{1}+X_{3}>t\right), \text { for all } t \geq 0
$$

Below we summarize some typical categories of minimal repair models, and give some further examples. Let $\left(T_{n}\right)$ be a point process describing the failure times at which instantaneous repairs are carried out and let $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, be the corresponding counting process

$$
N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)
$$

We assume that $N$ is adapted to some filtration $\mathbb{F}$ and has $\mathbb{F}$-intensity $\left(\lambda_{t}\right)$. Different types of repair processes are characterized by different intensities $\lambda$. The repairs are minimal if the intensity $\lambda$ is not affected by the occurrence of failures or, in other words, if one cannot determine the failure time points from the observation of $\lambda$. More formally, minimal repairs can be characterized as follows.Definition 3.50. Let $\left(T_{n}\right), n \in \mathbb{N}$, be a point process with an integrable counting process $N$ and corresponding $\mathbb{F}$-intensity $\lambda$. Suppose that $\mathbb{F}^{\lambda}=\left(\mathcal{F}_{t}^{\lambda}\right), t$ $\in \mathbb{R}_{+}$, is the filtration generated by $\lambda: \mathcal{F}_{t}^{\lambda}=\sigma\left(\lambda_{s}, 0 \leq s \leq t\right)$. Then the point process $\left(T_{n}\right)$ is called a minimal repair process (MRP) if none of the variables $T_{n}, n \in \mathbb{N}$, for which $P\left(T_{n}<\infty\right)>0$ is an $\mathbb{F}^{\lambda}$-stopping time, i.e., for all $n \in \mathbb{N}$ with $P\left(T_{n}<\infty\right)>0$ there exists $t \in \mathbb{R}_{+}$such that $\left\{T_{n} \leq t\right\} \notin \mathcal{F}_{t}^{\lambda}$.

This is a rather general definition that comprises the well-known special case of a nonhomogeneous Poisson process as is seen below. A renewal process with a strictly increasing or decreasing hazard rate $r$ of the interarrival times has intensity (compare Example 3.13, p. 64)

$$
\lambda_{t}=\sum_{n \geq 0} r\left(t-T_{n}\right) I\left(T_{n}<t \leq T_{n+1}\right), T_{0}=0, \lambda_{0}=r(0+)
$$

and is therefore not an MRP, because $N_{t}=\left|\left\{s \in \mathbb{R}_{+}: 0<s \leq t, \lambda_{s+}=\lambda_{0}\right\}\right|$. In the following we give some examples of (minimal) repair processes.
(a) In the basic statistical minimal repair model the intensity is a timedependent deterministic function $\lambda_{t}=\lambda(t)$, so that the process is a nonhomogeneous Poisson process. This means that the age (the failure intensity) is not changed as a result of a failure (minimal repair). Here $\mathcal{F}_{t}^{\lambda}=\{\Omega, \emptyset\}$ for all $t \in \mathbb{R}_{+}$, so clearly the failure times $T_{n}$ are no $\mathbb{F}^{\lambda}$-stopping times. The following special cases have been given much attention in the literature:

$$
\begin{aligned}
& \lambda_{\mathrm{p}}(t)=\lambda \beta(\lambda t)^{\beta-1}(\text { Power law }) \\
& \lambda_{\mathrm{L}}(t)=\lambda e^{\beta t}(\text { Log linear model })
\end{aligned}
$$

For the parallel system in Example 3.49, one has $\lambda(t)=2 \frac{1-\exp (-t)}{2-\exp (-t)}$. If the intensity is a constant, $\lambda_{t} \equiv \lambda$, the times between successive repairs are independent $\operatorname{Exp}(\lambda)$ distributed random variables. This is the case in which repairs have the same effect as replacements.
(b) If in (a) the intensity is not deterministic but a random variable $\lambda(\omega)$, which is known at the time origin ( $\lambda$ is $\mathcal{F}_{0}$-measurable), or, more general, $\lambda=\left(\lambda_{t}\right)$ is a stochastic process such that $\lambda_{t}$ is $\mathcal{F}_{0}$-measurable for all $t \in \mathbb{R}_{+}$, i.e., $\mathcal{F}_{0}=\sigma\left(\lambda_{s}, s \in \mathbb{R}_{+}\right)$and $\mathcal{F}_{t}=\mathcal{F}_{0} \vee \sigma\left(N_{s}, 0 \leq s \leq t\right)$, then the process is called a doubly stochastic Poisson process or a Cox process. The process generalizes the basic model (a); the failure (minimal repair) times are no $\mathbb{F}^{\lambda}$-stopping times, since $\mathcal{F}_{t}^{\lambda}=\sigma(\lambda) \subset \mathcal{F}_{0}$ and $T_{n}$ is not $\mathcal{F}_{0}$-measurable.
Also the Markov-modulated Poisson process of Example 3.14, p. 65, where the intensity $\lambda_{t}=\lambda_{Y_{t}}$ is determined by a Markov chain $\left(Y_{t}\right)$, is an MRP. Indeed, it is a slight modification of a doubly stochastic Poisson process in that the filtration $\mathcal{F}_{t}=\sigma\left(N_{s}, Y_{s}, 0 \leq s \leq t\right)$ does not include the information about the paths of $\lambda$ in $\mathcal{F}_{0}$.(c) For the physical minimal repair in Example 3.49, $\lambda_{t}=I\left(X_{1} \wedge X_{2} \leq t\right)$. In this case $\mathbb{F}^{\lambda}$ is generated by the minimum of $X_{1}$ and $X_{2}$. The first failure time of the system, $T_{1}$, equals $X_{1} \vee X_{2}$, which is not an $\mathbb{F}^{\lambda}$-stopping time. The filtration generated by $\lambda_{t}$ comprises no information about $X_{1} \vee X_{2}$.

In the following we give another characterization of an MRP.
Theorem 3.51. Assume that $P\left(T_{n}<\infty\right)=1$ for all $n \in \mathbb{N}$ and that there exist versions of conditional probabilities $F_{t}(n)=E\left[I\left(T_{n} \leq t\right) \mid \mathcal{F}_{t}^{\lambda}\right]$ such that for each $n \in \mathbb{N}\left(F_{t}(n)\right), t \in \mathbb{R}_{+}$, is an ( $\mathbb{F}^{\lambda}$-progressive) stochastic process.
(i) Then the point process $\left(T_{n}\right)$ is an MRP if and only if for each $n \in \mathbb{N}$ there exists some $t \in \mathbb{R}_{+}$such that

$$
P\left(0<F_{t}(n)<1\right)>0
$$

(ii) If furthermore $\left(F_{t}\right)=\left(F_{t}(1)\right)$ has $P$-a.s. continuous paths of bounded variation on finite intervals, then

$$
1-F_{t}=\exp \left\{-\int_{0}^{t} \lambda_{s} d s\right\}
$$

Proof. (i) To prove $(i)$ we show that $P\left(F_{t}(n) \in\{0,1\}\right)=1$ for all $t \in \mathbb{R}_{+}$ is equivalent to $T_{n}$ being an $\mathbb{F}^{\lambda}$-stopping time. Since we have $F_{0}(n)=0$ and by the dominated convergence theorem for conditional expectations

$$
\lim _{t \rightarrow \infty} F_{t}(n)=1
$$

the assumption that $P\left(F_{t}(n) \in\{0,1\}\right)=1$ for all $t \in \mathbb{R}_{+}$is equivalent to $F_{t}(n)=I\left(T_{n} \leq t\right)$ ( $P$-a.s.). But as $\left(F_{t}(n)\right)$ is adapted to $\mathbb{F}^{\lambda}$ this means that $T_{n}$ is an $\mathbb{F}^{\lambda}$-stopping time. This shows that under the given assumptions $P\left(0<F_{t}(n)<1\right)>0$ is equivalent to $T_{n}$ being no $\mathbb{F}^{\lambda_{-}}$ stopping time.
(ii) For the second assertion we apply the exponential formula (3.16) as described on p. 80.

Example 3.52. In continuation of Example 3.49 of the two-component parallel system we allow for repeated physical minimal repairs. Let $\left(X_{k}\right), k \in \mathbb{N}$, be a sequence of i.i.d. random variables following an exponential distribution with parameter $1: X_{k} \sim \operatorname{Exp}(1)$. Then we define

$$
T_{1}=X_{1} \vee X_{2}, T_{n+1}=T_{n}+X_{n+2}, n \in \mathbb{N}
$$

We consider the filtration generated by the sequence $\left(X_{k}\right), k \in \mathbb{N}$. The intensity of the corresponding counting process $N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)$ with respect to this filtration is then $\lambda_{t}=I\left(X_{1} \wedge X_{2} \leq t\right)$. [If we had considered the filtration generated by the sequence $\left(T_{n}\right), n \in \mathbb{N}$ we would have derived the deterministic intensity $2(1-\exp (-t)) /(2-\exp (-t))$.]By elementary calculations it can be seen that

$$
E\left[I\left(T_{1}>t\right) \mid \mathcal{F}_{t}^{\lambda}\right]=P\left(T_{1}>t \mid X_{1} \wedge X_{2} \wedge t\right)
$$

is continuous and nonincreasing. According to Theorem 3.51 it follows that $\left(T_{n}\right)$ is an MRP and that the time to the first failure has conditional distribution

$$
1-F_{t}=\exp \left\{-\int_{0}^{t} I\left(X_{1} \wedge X_{2} \leq s\right) d s\right\}=\exp \left\{-\left(t-X_{1} \wedge X_{2}\right)^{+}\right\}
$$

Now we want to illustrate the above definition of a minimal repair in a more complex situation. We consider the shock damage repair model described in Sect.3.3.4. We now assume that the shock arrival process $\left(T_{k}^{*}\right)$ is a nonhomogeneous Poisson process with intensity function $\nu(t)$ and that $\left(V_{k}\right)$ with $V_{k}=\left(Y_{k}, W_{k}\right)$ is an i.i.d. sequence of pairs of random variables, independent of $\left(T_{k}^{*}\right)$. The common distribution of the positive variables $Y_{k}$ is denoted $F$. The failure mechanism is as before, but the probability of failure at the occurrence of a shock $p(x)$ if the accumulated damage is $x$, is independent of the number of previous failures. Then we obtain for the failure counting process the intensity

$$
\lambda_{t}=\nu(t) \int_{0}^{\infty} p\left(X_{t-}+y\right) d F(y)
$$

where

$$
X_{t}=\sum_{k=1}^{\infty} Y_{k} I\left(T_{k}^{*} \leq t\right)
$$

denotes the accumulated damage up to time $t$. The following theorem shows under which condition the failure point process is an MRP.

Theorem 3.53. If $0<p(x)<1$ for all $x$ holds true, then the point process $\left(T_{n}\right)$ driven by the intensity (3.21) is an MRP.

Proof. The random variables $W_{k}$ equal 1 or 0 according to whether the system fails or not at the $k$ th shock. The first failure time $T_{1}$ can then be represented by

$$
T_{1}=\inf \left\{T_{k}^{*}: W_{k}=1\right\}
$$

At each occurrence of a shock a Bernoulli experiment is carried out with outcome $W_{k}$. The random variable $W_{k}$ is not measurable with respect to $\sigma\left(X_{T_{k}^{*}}\right)$ because by the condition $0<p(x)<1$ it follows that

$$
E\left[I\left(W_{k}=1\right) \mid X_{T_{k}^{*}}\right]=P\left(W_{k}=1 \mid X_{T_{k}^{*}}\right)=p\left(X_{T_{k}^{*}}\right) \notin\{0,1\}
$$

This shows that $T_{1}$ cannot be an $\mathbb{F}^{X}$-stopping time, where $\mathbb{F}^{X}$ is generated by the process $X=\left(X_{t}\right)$. Since we have $\mathcal{F}_{t}^{\lambda} \subset \mathcal{F}_{t}^{X}, T_{1}$ is no $\mathbb{F}^{\lambda}$-stopping time either. By induction via$$
T_{n+1}=\inf \left\{T_{k}^{*}>T_{n}: W_{k}=1\right\}
$$

we infer that none of the variables $T_{n}$ is an $\mathbb{F}^{\lambda}$-stopping time, which shows that $\left(T_{n}\right)$ is an MRP.

Remark 3.54. (1) In the case $p(x)=c$ for some $c, 0<c \leq 1$, the process is a nonhomogeneous Poisson process with intensity $\lambda_{t}=\nu(t) c$ and therefore an MRP. (2) The condition $0<p(x)<1$ excludes the case of threshold models for which $p(x)=1$ for $x \geq K$ and $p(x)=0$ else for some constant $K>0$. For such a threshold model we have

$$
T_{1}=\inf \left\{t \in \mathbb{R}_{+}: \lambda_{t} \geq \nu(t)\right\}
$$

if $P\left(Y_{k} \leq x\right)>0$ for all $x>0$. In this case $T_{1}$ is an $\mathbb{F}^{\lambda}$-stopping time and consequently $\left(T_{n}\right)$ is no MRP.

# 3.3.7 Comparison of Repair Processes for Different Information Levels 

Consider a monotone system comprising $m$ independent components with lifetimes $Z_{i}, i=1, \ldots, m$ and corresponding ordinary failure rates $\lambda_{t}(i)$. Its structure function $\Phi:\{0,1\}^{m} \rightarrow\{0,1\}$ represents the state of the system (1:intact, 0:failure), and the process $\mathbf{X}_{t}=\left(X_{t}(1), \ldots, X_{t}(m)\right)$ denotes the vector of component states at time $t$ with values in $\{0,1\}^{m}$. Example 3.49 suggests comparing the effects of minimal repairs on different information levels. However, it seems difficult to define such point processes for arbitrary information levels. One possible way is sketched in the following where considerations are restricted to the complete information $\mathbb{F}$-level (component-level) and the "black-box-level" $\mathbb{A}^{T}$ generated by $T=T_{1}, \mathcal{A}_{t}=\sigma\left(I\left(T_{1} \leq s\right), 0 \leq s \leq t\right)$. Note that $T_{1}$ describes the time to first failure, i.e.,

$$
T_{1}=\inf \left\{t \in \mathbb{R}_{+}: \Phi\left(\mathbf{X}_{t}\right)=0\right\}
$$

This time to first system failure is governed by the hazard rate process $\lambda$ for $t \in[0, T)$ (cf. Corollary 3.30 on p. 76):

$$
\lambda_{t}=\sum_{i=1}^{m}\left(\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right) \lambda_{t}(i)
$$

Our aim is to extend the definition of $\lambda_{t}$ also on $\left\{T_{1} \leq t\right\}$. To this end we extend the definition of $X_{t}(i)$ on $\left\{Z_{i} \leq t\right\}$ following the idea that upon system failure the component which caused the failure is repaired minimally in the sense that it is restored and operates at the same failure rate as it had not failed before. So we define $X_{t}(i)=0$ on $\left\{Z_{i} \leq t\right\}$ if the first failure of component $i$ caused no system failure, otherwise we set $X_{t}(i)=1$ on$\left\{Z_{i} \leq t\right\}$ (note that in the latter case the value of $X_{t}(i)$ is redefined for $\left.t=Z_{i}\right)$. In this way we define $\mathbf{X}_{t}$ and by (3.22) the process $\lambda_{t}$ for all $t \in$ $\mathbb{R}_{+}$. This completed intensity $\lambda_{t}$ induces a point process $\left(N_{t}\right)$ which counts the number of minimal repairs on the component level. The corresponding complete information filtration $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, is given by

$$
\mathcal{F}_{t}=\sigma\left(N_{s}, I\left(Z_{i} \leq s\right), 0 \leq s \leq t, i=1, \ldots, m\right)
$$

To investigate whether the process $\left(N_{t}\right)$ is an MRP we define the random variables

$$
Y_{i}=\inf \left\{t \in \mathbb{R}_{+}: \Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)=1\right\}, i=1, \ldots, m, \inf \emptyset=\infty
$$

which describe the time when component $i$ becomes critical, i.e., the time from which on a failure of component $i$ would lead to system failure. It follows that

$$
\begin{aligned}
\lambda_{t} & =\sum_{i=1}^{m} I\left(Y_{i} \leq t\right) \lambda_{t}(i) \\
\mathcal{F}_{t}^{\lambda} & =\sigma\left(I\left(Y_{i} \leq s\right), 0 \leq s \leq t, i=1, \ldots, m\right)
\end{aligned}
$$

Obviously on $\left\{Y_{i}<\infty\right\}$ we have $Z_{i}>Y_{i}$ and it can be shown that $Z_{i}$ is not measurable with respect to $\sigma\left(Y_{1}, \ldots, Y_{m}\right)$. For a two component parallel system this means that $Z_{1} \vee Z_{2}$ is not measurable with respect to $\sigma\left(Z_{1} \wedge Z_{2}\right)$, which holds true observing that $E\left[I\left(Z_{1} \vee Z_{2}>z\right) \mid Z_{1} \wedge Z_{2}\right] \notin\{0,1\}$ for some $z$ (note that the random variables $Z_{i}$ are assumed to be independent). The extension to the general case is intuitive but the details of a formal, lengthy proof are omitted. We state that the time to the first failure

$$
T_{1}=\min _{i=1, \ldots, m} Z_{i} I\left(Y_{i}<\infty\right)
$$

is no $\mathbb{F}^{\lambda}$-stopping time. By induction it can be seen that also $T_{n}$ is no $\mathbb{F}^{\lambda_{-}}$ stopping time and $\left(T_{n}\right)$ is an MRP.

Now we want to consider the same system on the "black-box-level". The change to the $\mathbb{A}^{T}$-level by conditioning leads to the failure rate $\hat{\lambda}, \hat{\lambda}_{t}=$ $E\left[\lambda_{t} \mid \mathcal{A}_{t}\right]$. This failure rate $\hat{\lambda}$ can be chosen to be deterministic,

$$
\hat{\lambda}_{t}=E\left[\lambda_{t} \mid T_{1}>t\right]
$$

it is the ordinary failure rate of $T_{1}$. For the time to the first system failure we have the two representations

$$
\begin{aligned}
I\left(T_{1} \leq t\right) & =\int_{0}^{t} I\left(T_{1}>s\right) \lambda_{s} d s+M_{t} \quad \mathbb{F} \text {-level } \\
& =\int_{0}^{t} I\left(T_{1}>s\right) \hat{\lambda}_{s} d s+\bar{M}_{t} \quad \mathbb{A}^{T} \text {-level. }
\end{aligned}
$$From the deterministic failure rate $\hat{\lambda}$ a nonhomogeneous Poisson process $\left(T_{n}^{\prime}\right)_{n \in \mathbb{N}}, 0<T_{1}^{\prime}<T_{2}^{\prime}<\cdots$ can be constructed where $T_{1}$ and $T_{1}^{\prime}$ have the same distribution. This nonhomogeneous Poisson process with

$$
N_{t}^{\prime}=\sum_{n=1}^{\infty} I\left(T_{n}^{\prime} \leq t\right)=\int_{0}^{t} \hat{\lambda}_{s} d s+M_{t}^{\prime}
$$

describes the MRP on the $\mathbb{A}^{T}$-level. Comparing these two information levels, Example 3.49 suggests $E N_{t} \geq E N_{t}^{\prime}$ for all positive $t$. A general comparison, also for arbitrary subfiltrations, seems to be an open problem (cf. [4, 124]).

Example 3.55. In the two-component parallel system of Example 3.49 we have the failure rate process $\lambda_{t}=I\left(X_{1} \wedge X_{2} \leq t\right)$ on the component level and $\hat{\lambda}_{t}=2 \frac{1-\exp (-t)}{2-\exp (-t)}$ on the black-box level. So one has two descriptions of the same random lifetime $T=T_{1}$

$$
\begin{aligned}
I\left(T_{1} \leq t\right) & =\int_{0}^{t} I\left(T_{1}>s\right) I\left(X_{1} \wedge X_{2} \leq s\right) d s+M_{t} \\
& =\int_{0}^{t} I\left(T_{1}>s\right) 2 \frac{1-e^{-s}}{2-e^{-s}} d s+\bar{M}_{t}
\end{aligned}
$$

The process $N$ counts the number of minimal repairs on the component level:

$$
N_{t}=\int_{0}^{t} I\left(X_{1} \wedge X_{2} \leq s\right) d s+M_{t}
$$

This is a delayed Poisson process, the (repair) intensity of which is equal to 1 after the first component failure. The process $N^{\prime}$ counts the number of minimal repairs on the black-box level:

$$
N_{t}^{\prime}=\int_{0}^{t} 2 \frac{1-e^{-s}}{2-e^{-s}} d s+M_{t}^{\prime}
$$

This is a nonhomogeneous Poisson process with an intensity which corresponds to the ordinary failure rate of $T_{1}$. Elementary calculations yield indeed

$$
E N_{t}=t-\frac{1}{2}\left(1-e^{-2 t}\right) \geq E N_{t}^{\prime}=t-\ln \left(2-e^{-t}\right)
$$

To interpret this result one should note that on the component level only the critical component which caused the system to fail is repaired. A black box repair, which is a replacement by a system of the same age that has not yet failed, could be a replacement by a system with both components working.

# 3.3.8 Repair Processes with Varying Degrees of Repair 

As in the minimal repair section, let $\left(T_{n}\right)$ be a point process describing failure times at which instantaneous repairs are carried out and let $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, be the corresponding counting process. We assume that $N$ is adapted to some filtration $\mathbb{F}$ and has $\mathbb{F}$-intensity $\left(\lambda_{t}\right)$.One way to model varying levels or degrees of repairs is the following. Consider a new item or system having lifetime distribution $F$ with failure rate $r(t)$. Assume that the $n$th repair has the effect that the distribution to the next failure is that of an unfailed item of age $A_{n} \geq 0$. Then $A_{n}=0$ means complete repair (as good as new) or replacement and $A_{n}>0$ can be interpreted as a partial repair which sets the item back to the functioning state. Theorem 3.12, p. 64, immediately yields the intensity of such a repair process with respect to the internal filtration $\mathbb{F}^{N}$ : Let $\left(A_{n}\right), n \in \mathbb{N}$, be a sequence of nonnegative random variables such that $A_{n}$ is $\mathbb{F}_{T_{n}}^{N}$-measurable, then the $\mathbb{F}^{N}$-intensity of $N$ is given by

$$
\lambda_{t}=\sum_{n=0}^{\infty} r\left(t-T_{n}+A_{n}\right) I\left(T_{n}<t \leq T_{n+1}\right), A_{0}=T_{0}=0
$$

The two extreme cases are:

1. $A_{n}=0$, for all $n \in \mathbb{N}$. Then $N$ is a renewal process with interarrival time distribution $F$, all repairs are complete restorations to the as good as new state.
2. $A_{n}=T_{n}$ for all $n \in \mathbb{N}$. Then $N$ is a nonhomogeneous Poisson process with intensity $r(t)$, all repairs are (black box) minimal repairs.

In addition we can introduce random degrees $Z_{n} \leq 1$ of the $n$th repair. Starting with a new item the first failure occurs at $T_{1}$. A repair with degree $Z_{1}$ is instantaneously carried out and results in a virtual age of $A_{1}=\left(1-Z_{1}\right) T_{1}$. Continuing we can define the sequence of virtual ages recursively by

$$
A_{n+1}=\left(1-Z_{n+1}\right)\left(A_{n}+T_{n+1}-T_{n}\right), A_{0}=0
$$

Negative values of $Z_{n}$ may be interpreted as additional aging due to the $n$th failure or a clumsy repair. In the literature there exist many models describing different ways of generating or prescribing the random sequence of repair degrees, cf. Bibliographic Notes.

# 3.3.9 Minimal Repairs and Probability of Ruin 

In this section we investigate a model that combines a certain reward and cost structure with minimal repairs. Consider a one-unit system that fails from time to time according to a point process. After failure a minimal repair is carried out that leaves the state of the system unchanged. The system can work in one of $m$ unobservable states. State " 1 " stands for new or in good condition and " $m$ " is defective or in bad condition. Aging of the system is described by a link between the failure point process and the unobservable state of the system. The failure or minimal repair intensity may depend on the state of the system.

Starting with an initial capital of $u \geq 0$, there is some constant flow of income, on the one hand, and, on the other hand, each minimal repair incurs a random cost. The risk process $R=\left(R_{t}\right), t \in \mathbb{R}_{+}$, describes the difference between the income including the initial capital $u$ and the accumulated costsfor minimal repairs up to time $t$. The time of ruin is defined as $\tau=\tau(u)=$ $\inf \left\{t \in \mathbb{R}_{+}: R_{t} \leq 0\right\}$. Since explicit formulas are rarely available, we are interested in bounds for $P(\tau<\infty)$ and $P(\tau \leq t)$, the infinite and the finite horizon ruin probabilities.

A related question is when to stop processing the system and carrying out an inspection or a renewal in order to maximize some reward functional. This problem is treated in Sect. 5.4.

For the mathematical formulation of the model, let the basic probability space $(\Omega, \mathcal{F}, P)$ be equipped with a filtration $\mathbb{F}$, the complete information level, to which all processes are adapted, and let $S=\{1, \ldots, m\}$ be the set of unobservable states. We assume that the time points of failures (minimal repairs) $0<T_{1}<T_{2}<\cdots$ form a Markov-modulated Poisson process as described in Example 3.14, p. 65. Let us recapitulate the details:

- The changes of the states are driven by a homogeneous Markov process $Y=\left(Y_{t}\right), t \in \mathbb{R}_{+}$, with values in $S$ and infinitesimal parameters $q_{i}$, the rate to leave state $i$, and $q_{i j}$, the rate to reach state $j$ from state $i$

$$
\begin{aligned}
q_{i} & =\lim _{h \rightarrow 0+} \frac{1}{h} P\left(Y_{h} \neq i \mid Y_{0}=i\right) \\
q_{i j} & =\lim _{h \rightarrow 0+} \frac{1}{h} P\left(Y_{h}=j \mid Y_{0}=i\right), i, j \in S, i \neq j \\
q_{i i} & =-q_{i}=-\sum_{j \neq i} q_{i j}
\end{aligned}
$$

- The time points $\left(T_{n}\right)$ form a point process and $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, is the corresponding counting process $N_{t}=\sum_{n \geq 1} I\left(T_{n} \leq t\right)$, which has a stochastic intensity $\lambda_{Y_{t}}$ depending on the unobservable state, i.e., $N$ admits the representation

$$
N_{t}=\int_{0}^{t} \lambda_{Y_{s}} d s+M_{t}
$$

where $M$ is an $\mathbb{F}$-martingale and $0<\lambda_{i}<\infty, i \in S$. Since the filtration $\mathbb{F}^{\lambda}\left(\mathbb{F}^{\lambda}=\mathbb{F}^{Y}\right.$, if $\lambda_{i} \neq \lambda_{j}$ for $\left.i \neq j\right)$ generated by the intensity does not include $\mathbb{F}^{N}$ as a subfiltration, it follows that $T_{n}, n \in \mathbb{N}$, is not an $\mathbb{F}^{\lambda_{-}}$ stopping time. Therefore, according to Definition 3.50, p. 92, $N$ is a MRP.

- $\left(X_{n}\right), n \in \mathbb{N}$, is a sequence of positive i.i.d. random variables, independent of $N$ and $Y$, with common distribution $F$ and finite mean $\mu$. The cost caused by the $n$th minimal repair at time $T_{n}$ is described by $X_{n}$.
- There is an initial capital $u$ and an income of constant rate $c>0$ per unit time.

Now the process $R$, given by

$$
R_{t}=u+c t-\sum_{n=1}^{N_{t}} X_{n}
$$

describes the available capital at time $t$ as the difference of the income and the total amount of costs for minimal repairs up to time $t$.The process $R$ is commonly used in other branches of applied probability like queueing or collective risk theory. In risk theory one is mainly interested in the distribution of the time to ruin $\tau=\inf \left\{t \in \mathbb{R}_{+}: R_{t} \leq 0\right\}$.

# The Failure Rate Process of the Ruin Time 

We want to show that the indicator process $V_{t}=I(\tau(u) \leq t)$ has a semimartingale representation

$$
V_{t}=I(\tau \leq t)=\int_{0}^{t} I(\tau>s) h_{s} d s+M_{t}, t \in \mathbb{R}_{+}
$$

where $M$ is a mean zero martingale with respect to the filtration $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in$ $\mathbb{R}_{+}$, which is generated by all introduced random quantities:

$$
\mathcal{F}_{t}=\sigma\left(N_{s}, Y_{s}, X_{i}, 0 \leq s \leq t, i=1, \ldots, N_{t}\right)
$$

The failure rate process $h=\left(h_{t}\right), t \in \mathbb{R}_{+}$, can be derived in the same way as was done for shock models with failures of threshold type (cf. p. 89). Note that ruin can only occur at a failure time; therefore, the ruin time is a hitting time of a compound point process:

$$
\tau=\inf \left\{t \in \mathbb{R}_{+}: A_{t}=\sum_{n=1}^{N_{t}} B_{n} \geq u\right\}=\inf \left\{T_{n}: A_{T_{n}} \geq u\right\}
$$

where $B_{n}=X_{n}-c U_{n}$ and $U_{n}=T_{n}-T_{n-1}, n=1,2, \ldots$. Replacing $X_{t}$ by $A_{t}$, $r\left(t-T_{n}\right)$ by $\lambda_{Y_{t}}$, and the threshold $S$ by $u$ in formula (3.20) on p. 90, we get the following lemma.

Lemma 3.56. Let $\tau=\tau(u)$ be the ruin time and $F$ the distribution of the claim sizes, $\bar{F}(x)=F((x, \infty))=P\left(X_{1}>x\right), x \in \mathbb{R}$. Then the $\mathbb{F}$-failure rate process $h$ is given by

$$
h_{t}=\lambda_{Y_{t}} \bar{F}\left(R_{t}-\right)=\sum_{i=1}^{m} \lambda_{i} I\left(Y_{t}=i\right) \bar{F}\left(R_{t}-\right), t \in \mathbb{R}_{+}
$$

The failure rate processes $h$ is bounded above by $\max \left\{\lambda_{i}: i \in S\right\}$. If all claim arrival rates $\lambda_{i}$ coincide, $\lambda=\lambda_{i}, i \in S$, we have the classical Poisson case, and it is not surprising that the hazard rate decreases when the risk reserve increases and vice versa. Of course, the paths of $R$ are not monotone and so the failure rate processes do not have monotone paths either. But they have (stochastically) a tendency to increase or decrease in the following sense. As follows from the results of Sect. 3.3.3 the process $R$ has an $\mathbb{F}$-semimartingale representation

$$
R_{t}=\int_{0}^{t} \sum_{i=1}^{m} I\left(Y_{s}=i\right)\left(c-\lambda_{i} \mu\right) d s+L_{t}
$$with a mean zero $\mathbb{F}$-martingale $L$. If we have positive drift in all environmental states, i.e., $c-\lambda_{i} \mu>0, i=1, \ldots, m$, then $R$ is a submartingale and it is seen that $h$ tends to 0 as $t \rightarrow \infty$ ( $P$-a.s.). On the other hand, if the claim rate $\lambda_{Y_{t}}$ is increasing ( $P$-a.s.) and the drift is nonpositive for all states, i.e., $c-\lambda_{i} \mu \leq$ $0, i=1, \ldots, m$, and $\bar{F}$ is convex on the support of the distribution, then $R$ is a supermartingale and it follows by Jensen's inequality for conditional expectations:

$$
\begin{aligned}
E\left[h_{t+s} \mid \mathcal{F}_{t}\right] & =E\left[\lambda_{Y_{t+s}} \bar{F}\left(R_{t+s}-\right) \mid \mathcal{F}_{t}\right] \geq E\left[\lambda_{Y_{t}} \bar{F}\left(R_{t+s}-\right) \mid \mathcal{F}_{t}\right] \\
& =\lambda_{Y_{t}} E\left[\bar{F}\left(R_{t+s}-\right) \mid \mathcal{F}_{t}\right] \geq \lambda_{Y_{t}} \bar{F}\left(E\left[R_{t+s}-\mid \mathcal{F}_{t}\right]\right) \\
& \geq \lambda_{Y_{t}} \bar{F}\left(R_{t}-\right)=h_{t}, t, s \in \mathbb{R}_{+}
\end{aligned}
$$

This shows that $h$ is a submartingale, i.e., $h$ is stochastically increasing.

# Bounds for Finite Time Ruin Probabilities 

Except in simple cases, such as Poisson arrivals of exponentially distributed claims ( $\mathrm{P} / \mathrm{E}$ case), the finite time ruin probabilities $\psi(u, t)=P(\tau(u) \leq t)$ cannot be expressed by the basic model parameters in an explicit form. So there is a variety of suggested bounds and approximations (see Asmussen [9] and Grandell [78] for overviews). In the following, bounds for the ruin probabilities in finite time will be derived that are based on the semimartingale representation given in Lemma 3.56. It turns out that especially for small values of $t$ known bounds can be improved.

From now on we assume that the claim arrival process is Poisson with rate $\lambda>0$. Then Lemma 3.56 yields the representation

$$
V_{t}=I(\tau(u) \leq t)=\int_{0}^{t} I(\tau(u)>s) \lambda \bar{F}\left(R_{s}\right) d s+M_{t}, t \in \mathbb{R}_{+}
$$

Note that the paths of $R$ have only countable numbers of jumps such that under the integral sign $R_{s}-$ can be replaced by $R_{s}$. Taking expectations on both sides of (3.24) one gets by Fubini's theorem

$$
\begin{aligned}
\psi(u, t) & =\int_{0}^{t} E\left[I(\tau(u)>s) \lambda \bar{F}\left(R_{s}\right)\right] d s \\
& =\int_{0}^{t}(1-\psi(u, s)) \lambda E\left[\bar{F}\left(R_{s}\right) \mid \tau(u)>s\right] d s
\end{aligned}
$$

As a solution of this integral equation we have the following representation of the finite time ruin probability:

$$
\psi(u, t)=1-\exp \left\{-\int_{0}^{t} \lambda E\left[\bar{F}\left(R_{s}\right) \mid \tau(u)>s\right] d s\right\}
$$

This shows that the (possibly defective) distribution of $\tau(u)$ has the hazard rate

$$
\lambda E\left[\bar{F}\left(R_{t}\right) \mid \tau(u)>t\right]
$$Now let $N^{X}$ be the renewal process generated by the sequence $\left(X_{i}\right), i \in \mathbb{N}$, $N_{t}^{X}=\sup \left\{k \in \mathbb{N}_{0}: \sum_{i=1}^{k} X_{i} \leq t\right\}$, and $A(u, t)=\int_{0}^{t} a(u, s) d s$, where $a(u, s)=\lambda P\left(N_{u+c s}^{X}=N_{s}\right)$. Then bounds for $\psi(u, t)$ can be established.

Theorem 3.57. For all $u, t \geq 0$, the following inequality holds true:

$$
B(u, t) \leq \psi(u, t) \leq A(u, t)
$$

where $A$ is defined as above and $B(u, t)=1-\exp \left\{-\lambda \int_{0}^{t} \bar{F}(u+c s) d s\right\}$.
Proof. For the lower bound we use the representation (3.26) and simply observe that $E\left[\bar{F}\left(R_{s}\right) \mid \tau(u)>s\right] \geq \bar{F}(u+c s)$.

For the upper bound we start with formula (3.24). Since $\{\tau(u)>t\} \subset$ $\left\{R_{t} \geq 0\right\}$, we have

$$
\begin{aligned}
V_{t} & =\int_{0}^{t} I(\tau(u)>s) \lambda \bar{F}\left(R_{s}\right) d s+M_{t} \\
& \leq \int_{0}^{t} I\left(R_{s} \geq 0\right) \lambda \bar{F}\left(R_{s}\right) d s+M_{t}
\end{aligned}
$$

Taking expectations on both sides of this inequality we get

$$
\psi(u, t)=E V_{t} \leq \int_{0}^{t} \lambda E\left[I\left(R_{s} \geq 0\right) \bar{F}\left(R_{s}\right)\right] d s
$$

It remains to show that $a(u, t)=\lambda E\left[I\left(R_{s} \geq 0\right) \bar{F}\left(R_{s}\right)\right]$. Denoting the $k$-fold convolution of $F$ by $F^{* k}$ and $T_{k}=\sum_{i=1}^{k} X_{i}$ it follows by the independence of the claim arrival process and $\left(X_{i}\right), i \in \mathbb{N}$,

$$
\begin{aligned}
E & {\left[I\left(R_{t} \geq 0\right) \bar{F}\left(u+c t-\sum_{i=1}^{N_{t}} X_{i}\right)\right] } \\
& =\sum_{k=0}^{\infty} E\left[I\left(u+c t-\sum_{i=1}^{k} X_{i} \geq 0\right) \bar{F}\left(u+c t-\sum_{i=1}^{k} X_{i}\right)\right] P\left(N_{t}=k\right) \\
& =\sum_{k=0}^{\infty} \int_{0}^{u+c t} \bar{F}(u+c t-x) d F^{* k}(x) P\left(N_{t}=k\right) \\
& =\sum_{k=0}^{\infty}\left\{F^{* k}(u+c t)-F^{*(k+1)}(u+c t)\right\} P\left(N_{t}=k\right) \\
& =\sum_{k=0}^{\infty} P\left(N_{u+c t}^{X}=k\right) P\left(N_{t}=k\right) \\
& =P\left(N_{u+c t}^{X}=N_{t}\right)
\end{aligned}
$$

which completes the proof.The bounds of the theorem seem to have several advantages: as numerical examples show, they perform well especially for small values of $t$ for which $\psi(u, t) \ll \psi(u, \infty)$ (see Aven and Jensen [25]). In addition no assumptions have been made about the tail of the claim size distribution $F$ and the drift of the risk reserve process, which are necessary for most of the asymptotic methods. This makes clear, on the other hand, that one cannot expect these bounds to perform well for $t \rightarrow \infty$.

Bibliographic Notes. The book of Brémaud [50] is one of the basic sources of the martingale dynamics of point process systems. The introduction (p. XV) also contains a sketch of the historical development. The SSM approach in connection with optimal stopping problems is considered by Jensen [98]. Comprehensive overviews over lifetime models in the martingale framework are those of Arjas [3, 4] and Koch [108]. An essential basis for the presentation of point processes in the martingale framework was laid by Jacod [92]. A number of books on point processes are available now. Among others, the martingale approach is exposed in Brémaud [50], Karr [103], and Daley and Vere-Jones [58], which also include the basic results about marked point processes. A full account on marked point processes can be found in the monograph of Last and Brandt [115].

Details on the theory of Markov processes, briefly mentioned in Sect.3.1, can be found in the classic book of Dynkin [66] or in the more recent monographs on stochastic processes mentioned at the beginning of this chapter.

One of the first papers considering random hazard rates in lifetime models is that of Bergman [38]. Failure rate processes for multivariate reliability systems were introduced by Arjas in [6]. Shock processes have been investigated by a number of authors. Aven treated these processes in the framework of counting processes in some generality in [15]. Recent work on shock models of threshold type concentrates on deriving the distribution of the hitting (life-) time under general conditions. Wendt [163] considers a doubly stochastic Poisson shock arrival process, whereas Lehmann [119] investigates shock models with failure thresholds varying in time.

Models of minimal repairs have been considered by Barlow and Hunter [30], Aven [18], Bergman [39], Block et al. [48], Stadje and Zuckerman [151], Shaked and Shanthikumar [141], and Beichelt [35], among others. Our formulation of the minimal repair concept in a general counting process framework is taken from [24]. Varying degrees of repairs are investigated in a number of papers like Brown and Proschan [51], Kijima [107], and Last and Szekli [116, 117].

As was pointed out by Bergman [39], information plays an important role in minimal repair models. Further steps in investigating information-based minimal repair were carried out by Arjas and Norros [7] and Natvig [124].

General references to risk theory are among others the books of Grandell [77] and Rolski et al. [134]. Overviews over bounds and approximations of ruin probabilities can be found in Asmussen [9] and Grandell [78]. Most of the approximations are based on limit theorems for $\psi(u, t)$ as $u \rightarrow \infty, t \rightarrow \infty$. One of the exceptions is the inverse martingales technique used by Delbaen and Haezendonck [60].# Availability Analysis of Complex Systems 

In this chapter we establish methods and formulas for computing various performance measures of monotone systems of repairable components. Emphasis is placed on the point availability, the distribution of the number of failures in a time interval, and the distribution of downtime of the system. A number of asymptotic results are formulated and proved, mainly for systems having highly available components.

The performance measures are introduced in Sect.4.1. In Sects.4.3-4.6 results for binary monotone systems are presented. Since many of these results are based on the one-component case, we first give in Sect. 4.2 a rather comprehensive treatment of this case. Section 4.7 presents generalizations and related models. Section 4.7.1 covers multistate monotone systems. In Sects. 4.2-4.5 and 4.7.1 it is assumed that there are at least as many repair facilities (channels) as components. In Sect.4.7.2 we consider a parallel system having $r$ repair facilities, where $r$ is less than the number of components. Attention is drawn to the case with $r=1$. Finally, in Sect.4.7.3 we present models for analysis of passive redundant systems.

In this chapter we focus on the situation that the components have exponential lifetime distributions. See Sect.4.7.1, p. 163, and Bibliographic Notes, p. 173, for some comments concerning the more general case of nonexponential lifetimes.

### 4.1 Performance Measures

We consider a binary monotone system with state process $\left(\Phi_{t}\right)=\left(\Phi\left(\mathbf{X}_{t}\right)\right)$, as described in Sect.2.1. Here $\Phi_{t}$ equals 1 if the system is functioning at time $t$ and 0 if the system is not-functioning at time $t$, and $\mathbf{X}_{t}=$ $\left(X_{t}(1), X_{t}(2), \ldots, X_{t}(n)\right) \in\{0,1\}^{n}$ describes the states of the components. The performance measures relate to one point in time $t$ or an interval $J$, which has the form $[0, u]$ or $(u, v], 0<u<v$. To simplify notation, we simply write $u$ instead of $[0, u]$.Emphasis will be placed on the following performance measures:
(a) Point availability at time $t, A(t)$, given by

$$
A(t)=E \Phi_{t}=P\left(\Phi_{t}=1\right)
$$

(b) Let $N_{J}$ be equal to the number of system failures in the interval $J$. We consider the following performance measures

$$
\begin{aligned}
& P\left(N_{J} \leq k\right), k \in \mathbb{N}_{0}, \\
& M(J)=E N_{J}, \\
& A[u, v]=P\left(\Phi_{t}=1, \forall t \in[u, v]\right) \\
&=P\left(\Phi_{u}=1, N_{(u, v]}=0\right) .
\end{aligned}
$$

The performance measure $A[u, v]$ is referred to as the interval reliability.
(c) Let $Y_{J}$ denote the downtime in the interval $J$, i.e.,

$$
Y_{J}=\int_{J}\left(1-\Phi_{t}\right) d t
$$

We consider the performance measures

$$
\begin{gathered}
P\left(Y_{J} \leq y\right), y \in \mathbb{R}_{+} \\
A^{D}(J)=\frac{E Y_{J}}{|J|}
\end{gathered}
$$

where $|J|$ denotes the length of the interval $J$. The measure $A^{D}(J)$ is in the literature sometimes referred to as the interval unavailability, but we shall not use this term here.

The above performance measures relate to a fixed point in time or a finite time interval. Often it is more attractive, in particular from a computational point of view, to consider the asymptotic limit of the measure (as $t, u$ or $v \rightarrow \infty$ ), suitably normalized (in most cases such limits exist). In the following we shall consider both the above measures and suitably defined limits.

# 4.2 One-Component Systems 

We consider in this section a one-component system. Hence $\Phi_{t}=X_{t}=X_{t}(1)$. If the system fails, it is repaired or replaced. Let $T_{k}, k \in \mathbb{N}$, represent the length of the $k$ th operation period, and let $R_{k}, k \in \mathbb{N}$, represent the length of the $k$ th repair/replacement time for the system; see Fig. 4.1. We assume that $\left(T_{k}\right), k \in \mathbb{N}$, and $\left(R_{k}\right), k \in \mathbb{N}$, are independent i.i.d. sequences of positive random variables. We denote the probability distributions of $T_{k}$ and $R_{k}$ by $F$ and $G$, respectively, and assume that they have finite means, i.e.,

Fig. 4.1. Time evolution of a failure and repair process for a one-component system starting at time $t=0$ in the operating state

$$
\mu_{F}<\infty, \quad \mu_{G}<\infty
$$

In reliability engineering $\mu_{F}$ and $\mu_{G}$ are referred to as the mean time to failure (MTTF) and the mean time to repair (MTTR), respectively.

To simplify the presentation, we also assume that $F$ is an absolutely continuous distribution, i.e., $F$ has a density function $f$ and failure rate function $\lambda$. We do not make the same assumption for the distribution function $G$, since that would exclude discrete repair time distributions, which are often used in practice.

In some cases we also need the variances of $F$ and $G$, denoted $\sigma_{F}^{2}$ and $\sigma_{G}^{2}$, respectively. In the following, when writing the variance of a random variable, or any other moment, it is tacitly assumed that these are finite.

The sequence

$$
T_{1}, R_{1}, T_{2}, R_{2}, \cdots
$$

forms an alternating renewal process.
We introduce the following variables

$$
S_{n}=T_{1}+\sum_{k=1}^{n-1}\left(R_{k}+T_{k+1}\right), \quad n \in \mathbb{N}
$$

and

$$
S_{n}^{\circ}=\sum_{k=1}^{n}\left(T_{k}+R_{k}\right), \quad n \in \mathbb{N}
$$

By convention, $S_{0}=S_{0}^{\circ}=0$, and sums over empty sets are zero. We see that $S_{n}$ represents the $n$th failure time, and $S_{n}^{\circ}$ represents the completion time of the $n$th repair.

The $S_{n}$ sequence generates a modified (delayed) renewal process $N$ with renewal function $M$. The first interarrival time has distribution $F$. All other interarrival times have distribution $F * G$ (convolution of $F$ and $G$ ), with mean $\mu_{F}+\mu_{G}$. Let $H^{(n)}$ denote the distribution function of $S_{n}$. Then

$$
H^{(n)}=F *(F * G)^{*(n-1)}
$$where $B^{* n}$ denotes the $n$-fold convolution of a distribution $B$ and as usual $B^{* 0}$ equals the distribution with mass of 1 at 0 . Note that we have

$$
M(t)=\sum_{n=1}^{\infty} H^{(n)}(t)
$$

(cf. (B.2), p. 274, in Appendix B). The $S_{n}^{\circ}$ sequence generates an ordinary renewal process $N^{\circ}$ with renewal function $M^{\circ}$. The interarrival times, $T_{k}+R_{k}$, have distribution $F * G$, with mean $\mu_{F}+\mu_{G}$. Let $H^{\circ(n)}$ denote the distribution function of $S_{n}^{\circ}$. Then

$$
H^{\circ(n)}=(F * G)^{* n}
$$

Let $\alpha_{t}$ denote the forward recurrence time at time $t$, i.e., the time from $t$ to the next event:

$$
\alpha_{t}=S_{N_{t}+1}-t \quad \text { on } \quad\left\{X_{t}=1\right\}
$$

and

$$
\alpha_{t}=S_{N_{t}^{\circ}+1}^{\circ}-t \quad \text { on } \quad\left\{X_{t}=0\right\}
$$

Hence, given that the system is up at time $t$, the forward recurrence time $\alpha_{t}$ equals the time to the next failure time. If the system is down at time $t$, the forward recurrence time equals the time to complete the repair. Let $F_{\alpha_{t}}$ and $G_{\alpha_{t}}$ denote the conditional distribution functions of $\alpha_{t}$ given that $X_{t}=1$ and $X_{t}=0$, respectively. Then we have for $x \in \mathbb{R}$

$$
F_{\alpha_{t}}(x)=P\left(\alpha_{t} \leq x \mid X_{t}=1\right)=P\left(S_{N_{t}+1}-t \leq x \mid X_{t}=1\right)
$$

and

$$
G_{\alpha_{t}}(x)=P\left(\alpha_{t} \leq x \mid X_{t}=0\right)=P\left(S_{N_{t}^{\circ}+1}^{\circ}-t \leq x \mid X_{t}=0\right)
$$

Similarly for the backward recurrence time, we define $\beta_{t}, F_{\beta_{t}}$, and $G_{\beta_{t}}$. The backward recurrence time $\beta_{t}$ equals the age of the system if the system is up at time $t$ and the duration of the repair if the system is down at time $t$, i.e.,

$$
\beta_{t}=t-S_{N_{t}^{\circ}}^{\circ} \quad \text { on } \quad\left\{X_{t}=1\right\}
$$

and

$$
\beta_{t}=t-S_{N_{t}} \quad \text { on }\left\{X_{t}=0\right\}
$$

# 4.2.1 Point Availability 

We will show that the point availability $A(t)$ is given by

$$
A(t)=\bar{F}(t)+\int_{0}^{t} \bar{F}(t-x) d M^{\circ}(x)=\bar{F}(t)+\bar{F} * M^{\circ}(t)
$$

Using a standard renewal argument conditioning on the duration of $T_{1}+R_{1}$, it is not difficult to see that $A(t)$ satisfies the following equation:$$
A(t)=\bar{F}(t)+\int_{0}^{t} A(t-x) d(F * G)(x)
$$

(cf. the derivation of the renewal equation in Appendix B, p. 275). Hence, by using Theorem B.2, p. 275, in Appendix B, formula (4.1) follows. Alternatively, we may use a more direct approach, writing

$$
X_{t}=I\left(T_{1}>t\right)+\sum_{n=1}^{\infty} I\left(S_{n}^{\circ} \leq t, S_{n}^{\circ}+T_{n+1}>t\right)
$$

which gives

$$
\begin{aligned}
A(t)=E X_{t} & =\bar{F}(t)+\sum_{n=1}^{\infty} \int_{0}^{t} \bar{F}(t-x) d H^{\circ(n)}(x) \\
& =\bar{F}(t)+\int_{0}^{t} \bar{F}(t-x) d M^{\circ}(x)
\end{aligned}
$$

The point unavailability $\bar{A}(t)$ is given by $\bar{A}(t)=1-A(t)=F(t)-\bar{F} * M^{\circ}(t)$.
In the case that $F$ is exponential with failure rate $\lambda$, it can be shown that

$$
\bar{A}(t) \leq \lambda \mu_{G}
$$

see Proposition 4.11, p. 114.
By the Key Renewal Theorem (Theorem B.7, p. 277, in Appendix B), it follows that

$$
\lim _{t \rightarrow \infty} A(t)=\frac{\mu_{F}}{\mu_{F}+\mu_{G}}
$$

noting that the mean of $F * G$ equals $\mu_{F}+\mu_{G}$ and $\int_{0}^{\infty} \bar{F}(t) d t=\mu_{F}$. The righthand side of (4.2) is called the limiting availability (or steady-state availability) and is for short denoted $A$. The limiting unavailability is defined as $\bar{A}=1-A$. Usually $\mu_{G}$ is small compared to $\mu_{F}$, so that

$$
\bar{A}=\frac{\mu_{G}}{\mu_{F}}+o\left(\frac{\mu_{G}}{\mu_{F}}\right), \quad \frac{\mu_{G}}{\mu_{F}} \rightarrow 0
$$

# 4.2.2 The Distribution of the Number of System Failures 

Consider first the interval $[0, v]$. We see that

$$
\left\{N_{v} \leq n\right\}=\left\{S_{n+1}>v\right\}, \quad n \in \mathbb{N}_{0}
$$

because if the number of failures in this interval is less than or equal to $n$, then the $(n+1)$ th failure occurs after $v$, and vice versa. Thus, for $n \in \mathbb{N}_{0}$,

$$
P\left(N_{v} \leq n\right)=1-(F * G)^{* n} * F(v)
$$

Some closely related results are stated below in Propositions 4.1 and 4.2.Proposition 4.1. The probability of $n$ failures occurring in $[0, v]$ and the system being up at time $v$ is given by

$$
P\left(N_{v}=n, X_{v}=1\right)=\int_{0}^{v} \bar{F}(v-x) d(F * G)^{* n}(x), n \in \mathbb{N}_{0}
$$

Proof. The result clearly holds for $n=0$. For $n \geq 1$, the result follows by observing that

$$
\left\{N_{v}=n, X_{v}=1\right\}=\left\{S_{n}^{\circ}+T_{n+1}>v, S_{n}^{\circ} \leq v\right\}
$$

Proposition 4.2. The probability of $n$ failures occurring in $[0, v]$ and the system being down at time $v$ is given by

$$
P\left(N_{v}=n, X_{v}=0\right)= \begin{cases}\int_{0}^{v} \bar{G}(v-x) d H^{(n)}(x) & n \in \mathbb{N} \\ 0 & n=0\end{cases}
$$

Proof. The proof is similar to the proof of Proposition 4.1. For $n \in \mathbb{N}$, it is seen that

$$
\left\{N_{v}=n, X_{v}=0\right\}=\left\{S_{n}+R_{n}>v, S_{n} \leq v\right\}
$$

From Propositions 4.1 and 4.2 we can deduce several results, for example, a formula for $P\left(N_{u}=n \mid X_{u}=1\right)$ using that

$$
P\left(N_{u}=n \mid X_{u}=1\right)=\frac{P\left(N_{u}=n, X_{u}=1\right)}{A(u)}
$$

In the theorem below we establish general formulas for $P\left(N_{(u, v]} \leq n\right)$ and $A[u, v]$.

Theorem 4.3. The probability that at most $n\left(n \in \mathbb{N}_{0}\right)$ failures occur during the interval $(u, v]$ equals

$$
\begin{aligned}
P\left(N_{(u, v]} \leq n\right)= & {\left[1-F_{\alpha_{u}} *(F * G)^{* n}(v-u)\right] A(u) } \\
& +\left[1-G_{\alpha_{u}} *(F * G)^{* n} * F(v-u)\right] \bar{A}(u)
\end{aligned}
$$

and

$$
A[u, v]=\bar{F}_{\alpha_{u}}(v-u) A(u)
$$

Proof. To establish the formula for $P\left(N_{(u, v]} \leq n\right)$, we condition on the state of the system at time $u$ :

$$
P\left(N_{(u, v]} \leq n\right)=\sum_{j=0}^{1} P\left(N_{(u, v]} \leq n \mid X_{u}=j\right) P\left(X_{u}=j\right)
$$

From this equality the formula follows trivially for $n=0$. For $n \in \mathbb{N}$, we need to show that the following two equalities hold true:$$
\begin{aligned}
& P\left(N_{(u, v]}>n \mid X_{u}=1\right)=\left(F_{\alpha_{u}} * G\right) *(F * G)^{*(n-1)} * F(v-u) \\
& P\left(N_{(u, v]}>n \mid X_{u}=0\right)=G_{\alpha_{u}} *(F * G)^{* n} * F(v-u)
\end{aligned}
$$

But (4.4) follows directly from (4.3) with the forward recurrence time distribution given $\left\{X_{u}=1\right\}$ as the first operating time distribution. Formula (4.5) is established analogously.

The formula for $A[u, v]$ is seen to hold observing that

$$
\begin{aligned}
A[u, v] & =P\left(X_{u}=1, N_{(u, v]}=0\right) \\
& =A(u) P\left(N_{(u, v]}=0 \mid X_{u}=1\right) \\
& =A(u) P\left(\alpha_{u}>v-u \mid X_{u}=1\right)
\end{aligned}
$$

This completes the proof of the theorem.
If the downtimes are much smaller then the uptimes in probability (which is the common situation in practice), then $N$ is close to a renewal process generated by all the uptimes. Hence, if the times to failure are exponentially distributed, the process $N$ is close to a homogeneous Poisson process. Formal asymptotic results will be established later, see Sect.4.4.

In the following two propositions we relate the distribution of the forward and backward recurrence times and the renewal functions $M$ and $M^{\circ}$.

Proposition 4.4. The probability that the system is up (down) at time $t$ and the forward recurrence time at time $t$ is greater than $w$ is given by

$$
\begin{aligned}
A[t, t+w] & =P\left(X_{t}=1, \alpha_{t}>w\right) \\
& =\bar{F}(t+w)+\int_{0}^{t} \bar{F}(t-x+w) d M^{\circ}(x) \\
P\left(X_{t}=0, \alpha_{t}>w\right) & =\int_{0}^{t} \bar{G}(t-x+w) d M(x)
\end{aligned}
$$

Proof. Consider first formula (4.6). It is not difficult to see that

$$
X_{t} I\left(\alpha_{t}>w\right)=\sum_{n=0}^{\infty} I\left(S_{n}^{\circ} \leq t, S_{n}^{\circ}+T_{n+1}>t+w\right)
$$

By taking expectations we find that

$$
\begin{aligned}
P\left(X_{t}=1, \alpha_{t}>w\right) & =\bar{F}(t+w)+\sum_{n=1}^{\infty} \int_{0}^{t} \bar{F}(t-x+w) d H^{\circ(n)}(x) \\
& =\bar{F}(t+w)+\int_{0}^{t} \bar{F}(t-x+w) d M^{\circ}(x)
\end{aligned}
$$This proves (4.6). To prove (4.7) we use a similar argument writing

$$
\left(1-X_{t}\right) I\left(\alpha_{t}>w\right)=\sum_{n=1}^{\infty} I\left(S_{n} \leq t, S_{n}+R_{n}>t+w\right)
$$

This completes the proof of the proposition.

Proposition 4.5. The probability that the system is up (down) at time $t$ and the backward recurrence time at time $t$ is greater than $w$ is given by

$$
\begin{aligned}
& P\left(X_{t}=1, \beta_{t}>w\right)=\left\{\begin{array}{lr}
\bar{F}(t)+\int_{0}^{t-w} \bar{F}(t-x) d M^{\circ}(x) & w \leq t \\
0 & w>t
\end{array}\right. \\
& P\left(X_{t}=0, \beta_{t}>w\right)=\left\{\begin{array}{lr}
\int_{0}^{t-w} \bar{G}(t-x) d M(x) & w \leq t \\
0 & w>t
\end{array}\right.
\end{aligned}
$$

Proof. The proof is similar to the proof of Proposition 4.4. Replace the indicator function in the sums in (4.8) and (4.9) by

$$
I\left(S_{n}^{\circ}+T_{n+1}>t, S_{n}^{\circ}+w<t\right)
$$

and

$$
I\left(S_{n}+R_{n}>t, S_{n}+w<t\right)
$$

respectively.

Theorem 4.6. The asymptotic distributions of the state process $\left(X_{t}\right)$ and the forward (backward) recurrence times at time $t$ are given by

$$
\begin{aligned}
& \lim _{t \rightarrow \infty} P\left(X_{t}=1, \alpha_{t}>w\right)=\frac{\int_{w}^{\infty} \bar{F}(x) d x}{\mu_{F}+\mu_{G}} \\
& \lim _{t \rightarrow \infty} P\left(X_{t}=0, \alpha_{t}>w\right)=\frac{\int_{w}^{\infty} \bar{G}(x) d x}{\mu_{F}+\mu_{G}} \\
& \lim _{t \rightarrow \infty} P\left(X_{t}=1, \beta_{t}>w\right)=\frac{\int_{w}^{\infty} \bar{F}(x) d x}{\mu_{F}+\mu_{G}} \\
& \lim _{t \rightarrow \infty} P\left(X_{t}=0, \beta_{t}>w\right)=\frac{\int_{w}^{\infty} \bar{G}(x) d x}{\mu_{F}+\mu_{G}}
\end{aligned}
$$

Proof. The results follow by applying the Key Renewal Theorem (see Appendix B, p. 277) to formulas (4.6), (4.7), (4.10), and (4.11).

Let us introduce

$$
\begin{aligned}
F_{\infty}(w) & =\frac{\int_{0}^{w} \bar{F}(x) d x}{\mu_{F}} \\
G_{\infty}(w) & =\frac{\int_{0}^{w} \bar{G}(x) d x}{\mu_{G}}
\end{aligned}
$$The distribution $F_{\infty}\left(G_{\infty}\right)$ is the asymptotic limit distribution of the forward and backward recurrence times in a renewal process generated by the uptimes (downtimes) and is called the equilibrium distribution for $F(G)$, cf. Theorem B.13, p. 279, in Appendix B. We would expect that $F_{\infty}$ and $G_{\infty}$ are equal to the asymptotic distributions of the forward and backward recurrence times in the alternating renewal process. As shown in the following proposition, this holds in fact true.

Proposition 4.7. The asymptotic distribution of the forward and backward recurrence times are given by

$$
\lim _{t \rightarrow \infty} \bar{F}_{\alpha_{t}}(w)=\lim _{t \rightarrow \infty} \bar{F}_{\beta_{t}}(w)=\bar{F}_{\infty}(w)
$$

and

$$
\lim _{t \rightarrow \infty} \bar{G}_{\alpha_{t}}(w)=\lim _{t \rightarrow \infty} \bar{G}_{\beta_{t}}(w)=\bar{G}_{\infty}(w)
$$

Proof. To establish these formulas, we use (4.2) (see p. 109), Theorem 4.6, and identities like

$$
P\left(\alpha_{t}>w \mid X_{t}=1\right)=\frac{P\left(X_{t}=1, \alpha_{t}>w\right)}{A(t)}
$$

The following theorem expresses the asymptotic distribution of $N_{(t, t+w]}$ as a function of $F, G, F_{\infty}, G_{\infty}$ and $A$.

Theorem 4.8. For $n \in \mathbb{N}_{0}$,

$$
\begin{aligned}
\lim _{t \rightarrow \infty} P\left(N_{(t, t+w]} \leq n\right)= & {\left[1-F_{\infty} *(F * G)^{* n}(w)\right] A+ } \\
& +\left[1-G_{\infty} *(F * G)^{* n} * F(w)\right] \bar{A}
\end{aligned}
$$

Proof. The result follows from the expression for the distribution of the number of failures given in Theorem 4.3, p. 110, combined with the limiting availability formula (4.2), p. 109, and Proposition 4.7.

If the lifetime distribution $F$ is exponential with failure rate $\lambda$, then we know that the forward recurrence time $\alpha_{t}$ has the same distribution for all $t$, and it is easily verified from the expression (4.13) for the equilibrium distribution for $F$ that $F_{\infty}(t)=F(t)$.

Next we consider an increasing interval $(t, t+w], w \rightarrow \infty$. Then we can use the normal distribution to find an approximate value for the distribution of $N$. The asymptotic normality, as formulated in the following theorem, follows by applying the Central Limit Theorem for renewal processes, see Theorem B.12, p. 278, in Appendix B. The notation $N\left(\mu, \sigma^{2}\right)$ is used for the normal distribution with mean $\mu$ and variance $\sigma^{2}$.Theorem 4.9. The asymptotic distribution of $N_{[t, t+w]}$ as $w \rightarrow \infty$, is given by

$$
\frac{N_{[t, t+w]}-w /\left(\mu_{F}+\mu_{G}\right)}{\left[w\left(\sigma_{F}^{2}+\sigma_{G}^{2}\right) /\left(\mu_{F}+\mu_{G}\right)^{3}\right]^{1 / 2}} \xrightarrow{D} \mathrm{~N}(0,1)
$$

The expected number of system failures can be found from the distribution function. Obviously, $M(v) \approx M^{\circ}(v)$ for large $v$. The exact relationship between $M(v)$ and $M^{\circ}(v)$ is given in the following proposition.

Proposition 4.10. The difference between the renewal functions $M(v)$ and $M^{\circ}(v)$ equals the unavailability at time $v$, i.e.,

$$
M(v)=M^{\circ}(v)+\bar{A}(v)
$$

Proof. Using that $P\left(N_{v} \leq n\right)=1-(F * G)^{* n} * F(v)$ (by (4.3), p. 109) and the expression (4.1), p. 108, for the availability $A(t)$, we obtain

$$
\begin{aligned}
M(v) & =\sum_{n=1}^{\infty} P\left(N_{v} \geq n\right) \\
& =\sum_{n=0}^{\infty}(F * G)^{* n} * F(v)=F(v)+M^{\circ} * F(v) \\
& =M^{\circ}(v)+\bar{A}(v)
\end{aligned}
$$

which is the desired result.
The number of system failures in $[0, v], N_{v}$, generates a counting process with stochastic intensity process

$$
\eta_{v}=\lambda\left(\beta_{v}\right) X_{v}
$$

where $\lambda$ is the failure rate function and $\beta_{v}$ is the backward recurrence time at time $v$, i.e., the relative age of the system at time $v$, cf. Sect.3.3.2, p. 85. We have $m(v)=E \eta_{v}$, where $m(v)$ is the renewal density of $M(v)$. Thus if the system has an exponential lifetime distribution with failure rate $\lambda$,

$$
m(v)=\lambda A(v)
$$

In general,

$$
m(v) \leq\left[\sup _{s \leq v} \lambda(s)\right] A(v)
$$

This bound can be used to establish an upper bound also for the unavailability $\bar{A}(t)$.

Proposition 4.11. The unavailability at time $t, \bar{A}(t)$, satisfies

$$
\bar{A}(t) \leq \sup _{s \leq t} \lambda(s) \int_{0}^{t} \bar{G}(u) d u \leq\left[\sup _{s \leq t} \lambda(s)\right] \mu_{G}
$$Proof. From (4.7), p. 111, we have

$$
\bar{A}(t)=P\left(X_{t}=0\right)=\int_{0}^{t} \bar{G}(t-x) d M(x)=\int_{0}^{t} \bar{G}(t-x) m(x) d x
$$

Using (4.19) this gives

$$
\bar{A}(t) \leq \int_{0}^{t} \bar{G}(t-x)\left[\sup _{s \leq x} \lambda(s)\right] A(x) d x
$$

It follows that

$$
\begin{aligned}
\bar{A}(t) & \leq \sup _{s \leq t} \lambda(s) \int_{0}^{t} \bar{G}(t-x) d x \\
& =\sup _{s \leq t} \lambda(s) \int_{0}^{t} \bar{G}(u) d u \leq\left[\sup _{s \leq t} \lambda(s)\right] \mu_{G}
\end{aligned}
$$

which proves $(4.20)$.
Hence, if the system has an exponential lifetime distribution with failure rate $\lambda$, then

$$
\bar{A}(t) \leq \lambda \int_{0}^{t} \bar{G}(s) d s \leq \lambda \mu_{G}
$$

It is also possible to establish lower bounds on $\bar{A}(t)$. A simple bound is obtained by combining (4.21) and the fact that

$$
t \leq E S_{N_{t}+1} \leq\left(\mu_{F}+\mu_{G}\right)(1+M(t))
$$

(cf. Appendix B, p. 279), giving

$$
\bar{A}(t) \geq \bar{G}(t) M(t) \geq \bar{G}(t)\left(\frac{t}{\mu_{F}+\mu_{G}}-1\right)
$$

Now suppose at time $t$ that the system is functioning and the relative age is $u$. What can we then say about the intensity process at time $t+v$ $(v>0)$ ? The probability distribution of $\eta_{t+v}$ is determined if we can find the distribution of the relative age at time $t+v$. But the relative age is given by (4.10), p. 112, slightly modified to take into account that the first uptime has distribution given by $F_{u}(x)=1-\bar{F}(u+x) / \bar{F}(u)$ for $0 \leq u \leq t$ :

$$
\begin{aligned}
& P\left(X_{t+v}=1, \beta_{t+v}>w \mid X_{t}=1, \beta_{t}=u\right) \\
& \quad=\left\{\begin{array}{lr}
\bar{F}_{u}(v)+\int_{0}^{v-w} \bar{F}(v-x) d M^{\circ}(x) & w \leq v \\
0 & w>v
\end{array}\right.
\end{aligned}
$$

The asymptotic distribution, as $v \rightarrow \infty$, is the same as in formula (4.12), p. 112 .

The (modified) renewal process $\left(N_{t}\right)$ has cycle lengths $T_{k}+R_{k}$ with mean $\mu_{F}+\mu_{G}, k \geq 2$. Thus we would expect that the (mean) average number offailures per unit of time is approximately equal to $1 /\left(\mu_{F}+\mu_{G}\right)$ for large $t$. In the following theorem some asymptotic results are presented that give precise formulations of this idea.

Theorem 4.12. With probability one,

$$
\lim _{t \rightarrow \infty} \frac{N_{t}}{t}=\frac{1}{\mu_{F}+\mu_{G}}
$$

Furthermore,

$$
\begin{aligned}
\lim _{t \rightarrow \infty} \frac{E N_{t}}{t} & =\frac{1}{\mu_{F}+\mu_{G}} \\
\lim _{u \rightarrow \infty} E\left[N_{u+w}-N_{u}\right] & =\frac{w}{\mu_{F}+\mu_{G}} \\
\lim _{t \rightarrow \infty}\left(E N_{t}-\frac{t}{\mu_{F}+\mu_{G}}\right) & =\frac{\sigma_{F}^{2}+\sigma_{G}^{2}}{2\left(\mu_{F}+\mu_{G}\right)^{2}}-\frac{1}{2}
\end{aligned}
$$

Proof. These results follow directly from renewal theory, see Appendix B, pp. 276-278.

# 4.2.3 The Distribution of the Downtime in a Time Interval 

First we formulate and prove some results related to the mean of the downtime in the interval $[0, u]$. As before (cf. Sect. 4.1, p. 106), we let $Y_{u}$ represent the downtime in the interval $[0, u]$.

Theorem 4.13. The expected downtime in $[0, u]$ is given by

$$
E Y_{u}=\int_{0}^{u} \bar{A}(t) d t
$$

Asymptotically, the (expected) portion of time the system is down equals the limiting unavailability, i.e.,

$$
\lim _{u \rightarrow \infty} A^{D}(u)=\lim _{u \rightarrow \infty} \frac{E Y_{u}}{u}=\bar{A}
$$

With probability one,

$$
\lim _{u \rightarrow \infty} \frac{Y_{u}}{u}=\bar{A}
$$Proof. Using the definition of $Y_{u}$ and Fubini's theorem we find that

$$
\begin{aligned}
E Y_{u} & =E \int_{0}^{u}\left(1-\Phi_{t}\right) d t \\
& =\int_{0}^{u} E\left(1-\Phi_{t}\right) d t \\
& =\int_{0}^{u} \bar{A}(t) d t
\end{aligned}
$$

This proves (4.26). Formula (4.27) follows by using (4.26) and the limiting availability formula (4.2), p. 109. Alternatively, we can use the Renewal Reward Theorem (Theorem B.15, p. 280, in Appendix B), interpreting $Y_{u}$ as a reward. From this theorem we can conclude that $E Y_{u} / u$ converges to the ratio of the expected downtime in a renewal cycle and the expected length of a cycle, i.e., to the limiting unavailability $\bar{A}$. The Renewal Reward Theorem also proves (4.28).

Now we look into the problem of finding formulas for the downtime distribution.

Let $N_{s}^{\text {op }}$ denote the number of system failures after $s$ units of operational time, i.e.,

$$
N_{s}^{\mathrm{op}}=\sum_{n=1}^{\infty} I\left(\sum_{k=1}^{n} T_{k} \leq s\right)
$$

Note that

$$
N_{s}^{\mathrm{op}} \geq n \Leftrightarrow \sum_{k=1}^{n} T_{k} \leq s, \quad n \in \mathbb{N}
$$

Let $Z_{s}$ denote the total downtime associated with the operating time $s$, but not including $s$, i.e.,

$$
Z_{s}=\sum_{i=1}^{N_{s}^{\mathrm{op}}} R_{i}
$$

where

$$
N_{s-}^{\mathrm{op}}=\lim _{u \rightarrow s-} N_{u}^{\mathrm{op}}
$$

Define

$$
C_{s}=s+Z_{s}
$$

We see that $C_{s}$ represents the calendar time after an operation time of $s$ time units and the completion of the repairs associated with the failures occurred up to $s$ but not including $s$.

The following theorem gives an exact expression of the probability distribution of $Y_{u}$, the total downtime in $[0, u]$.Theorem 4.14. The distribution of the downtime in a time interval $[0, u]$ is given by

$$
\begin{aligned}
P\left(Y_{u} \leq y\right) & =\sum_{n=0}^{\infty} G^{* n}(y) P\left(N_{u-y}^{\mathrm{op}}=n\right) \\
& =\sum_{n=0}^{\infty} G^{* n}(y)\left[F^{* n}(u-y)-F^{*(n+1)}(u-y)\right]
\end{aligned}
$$

Proof. To prove the theorem we first argue that

$$
\begin{aligned}
P\left(Y_{u} \leq y\right) & =P\left(C_{u-y} \leq u\right)=P\left(u-y+Z_{u-y} \leq u\right) \\
& =P\left(Z_{u-y} \leq y\right)
\end{aligned}
$$

This first equality follows by noting that the event $Y_{u} \leq y$ is equivalent to the event that the uptime in the interval $[0, u]$ is equal to or longer than $u-y$. This means that the point in time when the total uptime of the system equals $u-y$ must occur before or at $u$, i.e., $C_{u-y} \leq u$. Now using a standard conditional probability argument it follows that

$$
\begin{aligned}
P\left(Z_{u-y} \leq y\right) & =\sum_{n=0}^{\infty} P\left(Z_{u-y} \leq y \mid N_{(u-y)-}^{\mathrm{op}}=n\right) P\left(N_{(u-y)-}^{\mathrm{op}}=n\right) \\
& =\sum_{n=0}^{\infty} G^{* n}(y) P\left(N_{(u-y)-}^{\mathrm{op}}=n\right) \\
& =\sum_{n=0}^{\infty} G^{* n}(y) P\left(N_{u-y}^{\mathrm{op}}=n\right)
\end{aligned}
$$

We have used that the repair times are independent of the process $N_{*}^{\text {op }}$ and that $F$ is continuous. This proves (4.30). Formula (4.31) follows by using (4.29).

In the case that $F$ is exponential with failure rate $\lambda$ the following simple bounds apply

$$
e^{-\lambda(u-y)}[1+\lambda(u-y) G(y)] \leq P\left(Y_{u} \leq y\right) \leq e^{-\lambda(u-y)[1-G(y)]}
$$

The lower bound follows by including only the first two terms of the sum in (4.30), observing that $N_{t}^{\text {op }}$ is Poisson distributed with mean $\lambda t$, whereas the upper bound follows by using (4.30) and the inequality

$$
G^{* n}(y) \leq(G(y))^{n}
$$

In the case that the interval is rather long, the downtime will be approximately normally distributed, as is shown in Theorem 4.15 below.

Fig. 4.2. Time evolution of a failure and repair process for a one-component system starting at time $t=0$ in the failure state

Theorem 4.15. The asymptotic distribution of $Y_{u}$ as $u \rightarrow \infty$, is given by

$$
\sqrt{u}\left(\frac{Y_{u}}{u}-\bar{A}\right) \xrightarrow{D} \mathrm{~N}\left(0, \tau^{2}\right)
$$

where

$$
\tau^{2}=\frac{\mu_{F}^{2} \sigma_{G}^{2}+\mu_{G}^{2} \sigma_{F}^{2}}{\left(\mu_{F}+\mu_{G}\right)^{3}}
$$

Proof. The result follows by applying Theorem B.17, p. 280, in Appendix B, observing that the length of the first renewal cycle equals $S_{1}^{\circ}=T_{1}+R_{1}$, the downtime in this cycle equals $Y_{S_{1}^{\circ}}=R_{1}$ and

$$
\begin{aligned}
\frac{\operatorname{Var}\left[R_{1}-\bar{A} S_{1}^{\circ}\right]}{E S_{1}^{\circ}} & =\frac{\operatorname{Var}\left[R_{1} A-T_{1} \bar{A}\right]}{E S_{1}^{\circ}} \\
& =\frac{A^{2} \operatorname{Var}\left[R_{1}\right]+\bar{A}^{2} \operatorname{Var}\left[T_{1}\right]}{\mu_{F}+\mu_{G}} \\
& =\frac{\mu_{F}^{2} \sigma_{G}^{2}+\mu_{G}^{2} \sigma_{F}^{2}}{\left(\mu_{F}+\mu_{G}\right)^{3}}
\end{aligned}
$$

# 4.2.4 Steady-State Distribution 

The asymptotic results established above provide good approximations for the performance measures related to a given point in time or an interval. Based on the asymptotic values we can define a stationary (steady-state) process having these asymptotic values as their distributions and means. To define such a process in our case, we generalize the model analyzed above by allowing $X_{0}$ to be 0 or 1 .

Thus the time evolution of the process is as shown in Fig. 4.2 or as shown in Fig. 4.1 (p. 107) beginning with an uptime. The process is characterized by the parameters $A(0), F^{*}(t), F(t), G^{*}(t), G(t)$, where $F^{*}(t)$ denotes the distribution of the first uptime provided that the system starts in state 1 at time 0 (i.e., $X_{0}=1$ ) and $G^{*}(t)$ denotes the distribution of the first downtimeprovided that the system starts in state 0 at time 0 (i.e., $X_{0}=0$ ). Now assuming that $F^{*}(t)$ and $G^{*}(t)$ are equal to the asymptotic distributions of the recurrence times, i.e., $F_{\infty}(t)$ and $G_{\infty}(t)$, respectively, and $A(0)=A$, then it can be shown that the process $\left(X_{t}, \alpha_{t}\right)$ is stationary; see Birolini [44]. This means that we have, for example,

$$
\begin{aligned}
A(t) & =A, \quad \forall t \in \mathbb{R}_{+} \\
A[u, u+w] & =\frac{\int_{w}^{\infty} \bar{F}(x) d x}{\mu_{F}+\mu_{G}}, \quad \forall u, w \in \mathbb{R}_{+} \\
M(u, u+w] & =\frac{w}{\mu_{F}+\mu_{G}}, \quad \forall u, w \in \mathbb{R}_{+}
\end{aligned}
$$

# 4.3 Point Availability and Mean Number of System Failures 

Consider now a monotone system comprising $n$ independent components. For each component we define a model as in Sect. 4.2, indexed by " $i$ ". The uptimes and downtimes of component $i$ are thus denoted $T_{i k}$ and $R_{i k}$ with distributions $F_{i}$ and $G_{i}$, respectively. The lifetime distribution $F_{i}$ is absolutely continuous with a failure rate function $\lambda_{i}(t)$. The process $\left(N_{t}\right)$ refers now to the number of system failures, whereas $\left(N_{t}(i)\right)$ counts the number of failures of component $i$. The counting process $\left(N_{t}(i)\right)$ has intensity process $\left(\eta_{t}(i)\right)=\left(\lambda_{i}\left(\beta_{t}(i)\right) X_{t}(i)\right)$, where $\left(X_{t}(i)\right)$ equals the state process of component $i$ and $\left(\beta_{t}(i)\right)$ the backward recurrence time of component $i$. The mean of $\left(N_{t}(i)\right)$ is denoted $M_{i}(t)$, whereas the mean of the renewal process having interarrival times $T_{i k}+R_{i k}, k \in \mathbb{N}$, is denoted $M_{i}^{\circ}(t)$. If the process $\left(\mathbf{X}_{t}\right)$ is regenerative, we denote the consecutive cycle lengths $S_{1}, S_{2}, \ldots$. We write $S$ in place of $S_{1}$. Remember that a stochastic process $\left(X_{t}\right)$ is called regenerative if there exists a finite random variable $S$ such that the process beyond $S$ is a probabilistic replica of the process starting at 0 . The precise definition is given in Appendix B, p. 281.

In the following we establish results similar to those obtained in the previous section. Some results are quite easy to generalize to monotone systems, others are extremely difficult. Simplifications and approximative methods are therefore sought. First we look at the point availability.

### 4.3.1 Point Availability

The following results show that the point availability (limiting availability) of a monotone system is equal to the reliability function $h$ with the component reliabilities replaced by the component availabilities $A_{i}(t)\left(A_{i}\right)$.

Theorem 4.16. The system availability at time $t, A(t)$, and the limiting system availability, $\lim _{t \rightarrow \infty} A(t)$, are given by$$
\begin{aligned}
A(t) & =h\left(A_{1}(t), A_{2}(t), \ldots, A_{n}(t)\right)=h(\mathbf{A}(t)) \\
\lim _{t \rightarrow \infty} A(t) & =h\left(A_{1}, A_{2}, \ldots, A_{n}\right)=h(\mathbf{A})
\end{aligned}
$$

Proof. Formula (4.33) is simply an application of the reliability function formula (2.2), see p. 21, with $A_{i}(t)=P\left(X_{t}(i)=1\right)$. Since the reliability function $h(\mathbf{p})$ is a linear function in each $p_{i}$ (see Sect. 2.1, p. 25), and therefore a continuous function, it follows that $A(t) \rightarrow h\left(A_{1}, A_{2}, \ldots, A_{n}\right)$ as $t \rightarrow \infty$, which proves (4.34).

The limiting system availability can also be interpreted as the expected portion of time the system is operating in the long run, or as the long run average availability, noting that

$$
\lim _{t \rightarrow \infty} E\left[\frac{1}{t} \int_{0}^{t} \Phi_{s} d s\right]=\lim _{t \rightarrow \infty} \frac{1}{t} \int_{0}^{t} A(s) d s=\lim _{t \rightarrow \infty} A(t)
$$

# 4.3.2 Mean Number of System Failures 

We first state some results established in Sect.3.3.2, cf. formula (3.18), p. 86. See also (4.17) and (4.18), p. 114.

Theorem 4.17. The expected number of system failures in $[0, u]$ is given by

$$
\begin{aligned}
E N_{u} & =\sum_{i=1}^{n} \int_{0}^{u}\left[h\left(1_{i}, \mathbf{A}(t)\right)-h\left(0_{i}, \mathbf{A}(t)\right)\right] d M_{i}(t) \\
& =\sum_{i=1}^{n} \int_{0}^{u}\left[h\left(1_{i}, \mathbf{A}(t)\right)-h\left(0_{i}, \mathbf{A}(t)\right)\right] m_{i}(t) d t \\
& =\sum_{i=1}^{n} \int_{0}^{u}\left[h\left(1_{i}, \mathbf{A}(t)\right)-h\left(0_{i}, \mathbf{A}(t)\right)\right] E \eta_{t}(i) d t
\end{aligned}
$$

where $m_{i}(t)$ is the renewal density function of $M_{i}(t)$.
Corollary 4.18. If component $i$ has constant failure rate $\lambda_{i}, i=1,2, \ldots, n$, then

$$
\begin{aligned}
E N_{u} & =\sum_{i=1}^{n} \int_{0}^{u}\left[h\left(1_{i}, \mathbf{A}(t)\right)-h\left(0_{i}, \mathbf{A}(t)\right)\right] \lambda_{i} A_{i}(t) d t \\
& \leq u \tilde{\lambda}
\end{aligned}
$$

where $\tilde{\lambda}=\sum_{i=1}^{n} \lambda_{i}$.
Next we will generalize the asymptotic results (4.23)-(4.25), p. 116.Theorem 4.19. The expected number of system failures per unit of time is asymptotically given by

$$
\begin{aligned}
\lim _{u \rightarrow \infty} \frac{E N_{u}}{u} & =\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\mu_{F_{i}}+\mu_{G_{i}}} \\
\lim _{u \rightarrow \infty} \frac{E N_{(u, u+w]}}{w} & =\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\mu_{F_{i}}+\mu_{G_{i}}}
\end{aligned}
$$

Furthermore, if the process $\mathbf{X}$ is a regenerative process having finite expected cycle length, i.e., $E S<\infty$, then with probability one,

$$
\lim _{u \rightarrow \infty} \frac{N_{u}}{u}=\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\mu_{F_{i}}+\mu_{G_{i}}}
$$

Proof. To prove these results, we make use of formula (4.35). Dividing this formula by $u$ and using the Elementary Renewal Theorem (see Appendix B, p. 277), formula (4.37) can be shown to hold noting that $E\left[\Phi\left(1_{i}, \mathbf{X}_{t}\right)\right.$ $\left.-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right] \rightarrow\left[h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)\right]$ as $t \rightarrow \infty$. Let $h_{i}^{*}(t)=E\left[\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\right.$ $\left.\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right]$ and $h_{i}^{*}$ its limit as $t \rightarrow \infty$. Then we can write formula (4.35) divided by $u$ in the following form:

$$
\sum_{i=1}^{n}\left\{h_{i}^{*} \frac{M_{i}(u)}{u}+\frac{1}{u} \int_{0}^{u}\left[h_{i}^{*}(t)-h_{i}^{*}\right] d M_{i}(t)\right\}
$$

Hence in view of the Elementary Renewal Theorem, formula (4.37) follows if

$$
\lim _{u \rightarrow \infty} \frac{1}{u} \int_{0}^{u}\left[h_{i}^{*}(t)-h_{i}^{*}\right] d M_{i}(t)=0
$$

But (4.40) is seen to hold true by Proposition B.14, p. 279, in Appendix B.
The formula (4.38) is shown by writing

$$
E\left[N_{u+w}-N_{u}\right]=\sum_{i=1}^{n} \int_{u}^{u+w} E\left[\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right] d M_{i}(t)
$$

and using Blackwell's Theorem, see Theorem B.9, p. 278, in Appendix B.
If we assume that the process $\mathbf{X}$ is regenerative with $E S<\infty$, it follows from the theory of renewal reward processes (see Appendix B, p. 280) that with probability one, $\lim _{u \rightarrow \infty} N_{u} / u$ exists and equals

$$
\lim _{u \rightarrow \infty} \frac{E N_{u}}{u}=\frac{E N_{S}}{E S}
$$

Combining this with (4.37), we can conclude that (4.39) holds true, and the proof of the theorem is complete.Definition 4.20. The limit of $E N_{u} / u$, given by formula (4.37), is referred to as the system failure rate and is denoted $\lambda_{\Phi}$, i.e.,

$$
\lambda_{\Phi}=\lim _{u \rightarrow \infty} \frac{E N_{u}}{u}=\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\mu_{F_{i}}+\mu_{G_{i}}}
$$

Remark 4.21. 1. Heuristically, the limit (4.37) can easily be established: In the interval $(t, t+w), t$ large and $w$ small, the probability that component $i$ fails equals approximately $w /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$, and this failure implies a system failure if $\Phi\left(1_{i}, \mathbf{X}_{t}\right)=1$ and $\Phi\left(0_{i}, \mathbf{X}_{t}\right)=0$, i.e., the system fails if component $i$ fails. But the probability that $\Phi\left(1_{i}, \mathbf{X}_{t}\right)=1$ and $\Phi\left(0_{i}, \mathbf{X}_{t}\right)=$ 0 is approximately equal to $h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)$, which gives the desired result.
2. At time $t$ we can define a system failure rate $\lambda_{\Phi}(t)$ by

$$
\lambda_{\Phi}(t)=\sum_{i=1}^{n}\left[\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right] \eta_{t}(i)
$$

cf. Sect.3.3.2, p. 85. Since

$$
E \lambda_{\Phi}(t)=\sum_{i=1}^{n}\left[h\left(1_{i}, \mathbf{A}_{t}\right)-h\left(0_{i}, \mathbf{A}_{t}\right)\right] m_{i}(t)
$$

where $m_{i}(t)$ denotes the renewal density of $M_{i}(t)$, we see that $E \lambda_{\Phi}(t) \rightarrow$ $\lambda_{\Phi}$ as $t \rightarrow \infty$ provided that $m_{i}(t) \rightarrow 1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$. From renewal theory, see Theorem B.10, p. 278, in Appendix B, we know that if the renewal cycle lengths $T_{i k}+R_{i k}$ have a density function $h$ with $h(t)^{p}$ integrable for some $p>1$, and $h(t) \rightarrow 0$ as $t \rightarrow \infty$, then $M_{i}$ has a density $m_{i}$ such that $m_{i}(t) \rightarrow 1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$ as $t \rightarrow \infty$. See the remark following Theorem B. 10 for other sufficient conditions for $m_{i}(t) \rightarrow 1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$ to hold. If component $i$ has an exponential lifetime distribution with parameter $\lambda_{i}$, then $m_{i}(t)=\lambda_{i} A_{i}(t),(c f .(4.18)$, p. 114), which converges to $1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$.

It is intuitively clear that the process $\mathbf{X}$ is regenerative if the components have exponential lifetime distributions. Before we prove this formally, we formulate a result related to $E N_{u}^{\circ}$ : the expected number of visits to the best state $(1,1, \ldots, 1)$ in $[0, u]$. The result is analogous to (4.35) and (4.37).

Lemma 4.22. The expected number of visits to state $(1,1, \ldots, 1)$ in $[0, u]$ is given by

$$
E N_{u}^{\circ}=\sum_{i=1}^{n} \int_{0}^{u} \prod_{j \neq i} A_{j}(t) d M_{i}^{\circ}(t)
$$

Furthermore,

$$
\lim _{u \rightarrow \infty} \frac{E N_{u}^{\circ}}{u}=\prod_{j=1}^{n} A_{j} \sum_{i=1}^{n} \frac{1}{\mu_{F_{i}}}
$$Proof. Formula (4.42) is shown by arguing as in the proof of (4.35) (cf. Sect.3.3.2, p. 85), writing

$$
E N_{u}^{\circ}=E\left[\sum_{i=1}^{n} \int_{0}^{u} \prod_{j \neq i} X_{j}(t) d N_{t}^{\circ}(i)\right]
$$

To show (4.43) we can repeat the proof of (4.37) to obtain

$$
\begin{aligned}
\lim _{u \rightarrow \infty} \frac{E N_{u}^{\circ}}{u} & =\sum_{i=1}^{n} \prod_{j \neq i} A_{j} \frac{1}{\mu_{F_{i}}+\mu_{G_{i}}} \\
& =\prod_{j=1}^{n} A_{j} \sum_{i=1}^{n} \frac{1}{\mu_{F_{i}}}
\end{aligned}
$$

This completes the proof of the lemma.
The above result can be shown heuristically using the same type of arguments as in Remark 4.21. For highly available components we have $A_{i} \approx 1$, hence the limit (4.43) is approximately equal to

$$
\sum_{i=1}^{n} \frac{1}{\mu_{F_{i}}}
$$

This is as expected noting that the number of visits to state $(1,1, \ldots, 1)$ then should be approximately equal to the average number of component failures per unit of time. If a component fails, it will normally be repaired before any other component fails, and, consequently, the process again returns to state $(1,1, \ldots, 1)$.

Theorem 4.23. If all the components have exponential lifetimes, then $\mathbf{X}$ is a regenerative process.

Proof. Because of the memoryless property of the exponential distribution and the fact that all component uptimes and downtimes are independent, we can conclude that $\mathbf{X}$ is regenerative (as defined in Appendix B, p. 281) if we can prove that $P(S<\infty)=1$, where $S=\inf \left\{t>S^{\prime}: \mathbf{X}_{t}=(1,1, \ldots, 1)\right\}$ and $S^{\prime}=\min \left\{T_{i 1}: i=1,2, \ldots, n\right\}$. It is clear that if $\mathbf{X}$ returns to the state $(1,1, \ldots, 1)$, then the process beyond $S$ is a probabilistic replica of the process starting at 0 .

Suppose that $P(S<\infty)<1$. Then there exists an $\epsilon>0$ such that $P(S<\infty) \leq 1-\epsilon$. Now let $\tau_{i}$ be point in time of the $i$ th visit of $\mathbf{X}$ to the state $(1,1, \ldots, 1)$, i.e., $\tau_{1}=S$ and for $i \geq 2$,

$$
\tau_{i}=\inf \left\{t>\tau_{i-1}+S_{i}^{\prime}: \mathbf{X}_{t}=(1,1, \ldots, 1)\right\}
$$

where $S_{i}^{\prime}$ has the same distribution as $S^{\prime}$. We define $\inf \{\emptyset\}=\infty$. Since $\tau_{i}<\infty$ is equivalent to $\tau_{k}-\tau_{k-1}<\infty, k=1,2, \ldots, i\left(\tau_{0}=0\right)$, we obtain

$$
P\left(\tau_{i}<\infty\right)=[P(S<\infty)]^{i} \leq(1-\epsilon)^{i}
$$For all $t \in \mathbb{R}_{+}$,

$$
P\left(N_{t}^{\circ} \geq i\right) \leq P\left(\tau_{i}<\infty\right)
$$

and it follows that

$$
\begin{aligned}
E N_{t}^{\circ} & =\sum_{i=1}^{\infty} P\left(N_{t}^{\circ} \geq i\right) \\
& \leq \sum_{i=1}^{\infty}(1-\epsilon)^{i} \\
& =\frac{1-\epsilon}{1-(1-\epsilon)}=\frac{1-\epsilon}{\epsilon}<\infty
\end{aligned}
$$

Consequently, $E N_{t}^{\circ} / t \rightarrow 0$ as $t \rightarrow \infty$. But this result contradicts (4.43), and therefore $P(S<\infty)=1$.

Under the given set-up the regenerative property only holds true if the lifetimes of the components are exponentially distributed. However, this can be generalized by considering phase-type distributions with an enlarged state space, which also includes the phases; see Sect.4.7.1, p. 163.

# 4.4 Distribution of the Number of System Failures 

In general, it is difficult to calculate the distribution of the number of system failures $N_{(u, v]}$. Only in some special cases it is possible to obtain practical computation formulas, and in the following we look closer into some of these.

If the repair times are small compared to the lifetimes and the lifetimes are exponentially distributed with parameter $\lambda_{i}$, then clearly the number of failures of component $i$ in the time interval $(u, u+w], N_{u+w}(i)-N_{u}(i)$, is approximately Poisson distributed with parameter $\lambda_{i} w$. If the system is a series system, and we make the same assumptions as above, it is also clear that the number of system failures in the interval $(u, u+w]$ is approximately Poisson distributed with parameter $\sum_{i=1}^{n} \lambda_{i} w$. The number of system failures in $[0, t], N_{t}$, is approximately a Poisson process with intensity $\sum_{i=1}^{n} \lambda_{i}$.

If the system is highly available and the components have constant failure rates, the Poisson distribution (with the asymptotic rate $\lambda_{\Phi}$ ) will in fact also produce good approximations for more general systems. As motivation, we observe that $E N_{(u, u+w]} / w$ is approximately equal to the asymptotic system failure rate $\lambda_{\Phi}$, and $N_{(u, u+w]}$ is "nearly independent" of the history of $N$ up to $u$, noting that the process $\mathbf{X}$ frequently restarts itself probabilistically, i.e., $\mathbf{X}$ re-enters the state $(1,1, \ldots, 1)$.

Refer to $[22,82]$ for Monte Carlo simulation studies of the accuracy of the Poisson approximation. As an illustration of the results obtained in these studies, consider a parallel system of two identical components where thefailure rate $\lambda$ is equal to 0.05 , the repair times are all equal to 1 , and the expected number of system failures is equal to 5 . This means, as shown below, that the time interval is about 1,000 and the expected number of component failures is about 100 . Using the definition of the system failure rate $\lambda_{\Phi}$ (cf. (4.41), p. 123) with $\mu_{G}=1$, we obtain

$$
\begin{aligned}
\frac{E N_{u}}{u} & =\frac{5}{u} \approx \lambda_{\Phi}=2 \bar{A}_{1} \frac{1}{\mu_{F_{1}}+\mu_{G_{1}}}=2 \frac{\mu_{G}}{\frac{1}{\lambda}+\mu_{G}} \cdot \frac{1}{\frac{1}{\lambda}+\mu_{G}} \\
& \approx 2 \lambda^{2}=0.005
\end{aligned}
$$

Hence $u \approx 1,000$ and $2 E N_{u}(i) \approx 2 \lambda u \approx 100$. Clearly, this is an approximate steady-state situation, and we would expect that the Poisson distribution gives an accurate approximation. The Monte Carlo simulations in [22] confirm this. The distance measure, which is defined as the maximum distance between the Poisson distribution (with mean $\lambda_{\Phi} u$ ) and the "true" distribution obtained by Monte Carlo simulation, is equal to 0.006 . If we take instead $\lambda=0.2$ and $E N_{u}=0.2$, we find that the expected number of component failures is about 1. Thus, we are far away from a steady-state situation and as expected the distance measure is larger: 0.02 . But still the Poisson approximation produces relatively accurate results.

In the following we look at the problem of establishing formalized asymptotic results for the distribution of the number of system failures. We first consider the interval reliability.

# 4.4.1 Asymptotic Analysis for the Time to the First System Failure 

The above discussion indicates that the interval reliability $A[0, u]$, defined by $A[0, u]=P\left(N_{u}=0\right)$, is approximately exponentially distributed for highly available systems comprising components with exponentially distributed lifetimes. This result can also be formulated as a limiting result as shown in the theorem below. It is assumed that the process $\mathbf{X}$ is a regenerative process with regenerative state $(1,1, \ldots, 1)$. The variable $S$ denotes the length of the first renewal cycle of the process $\mathbf{X}$, i.e., the time until the process returns to state $(1,1, \ldots, 1)$. Let $T_{\Phi}$ denote the time to the first system failure and $q$ the probability that a system failure occurs in a renewal cycle, i.e.,

$$
q=P\left(N_{S} \geq 1\right)=P\left(T_{\Phi}<S\right)
$$

For $q \in(0,1)$, let $P_{0}$ and $P_{1}$ denote the conditional probability given $N_{S}=0$ and $N_{S} \geq 1$, i.e., $P_{0}(\cdot)=P\left(\cdot \mid N_{S}=0\right)$ and $P_{1}(\cdot)=P\left(\cdot \mid N_{S} \geq 1\right)$. The corresponding expectations are denoted $E_{0}$ and $E_{1}$. Furthermore, let $c_{0 S}^{2}=$ $\left[E_{0} S^{2} /\left(E_{0} S\right)^{2}\right]-1$ denote the squared coefficient of variation of $S$ under $P_{0}$.

The notation $\xrightarrow{P}$ is used for convergence in probability and $\xrightarrow{D}$ for convergence in distribution, cf. Appendix A, p. 248. We write $\operatorname{Exp}(t)$ for theexponential distribution with parameter $t$, Poisson $(t)$ for the Poisson distribution with mean $t$ and $\mathrm{N}\left(\mu, \sigma^{2}\right)$ for the normal distribution with mean $\mu$ and variance $\sigma^{2}$.

For each component $i(i \in\{1,2, \ldots, n\})$ we assume that there is a sequence of uptime and downtime distributions $\left(F_{i j}, G_{i j}\right), j=1,2, \ldots$.

To simplify notation, we normally omit the index $j$. When assuming in the following that $\mathbf{X}$ is a regenerative process, it is tacitly understood for all $j \in \mathbb{N}$. We shall formulate conditions which guarantee that $\alpha T_{\Phi}$ is asymptotically exponentially distributed with parameter 1 , where $\alpha$ is a suitable normalizing "factor" (more precisely, a normalizing sequence depending on $j$ ). The following factors will be studied: $q / E_{0} S, q / E S, 1 / E T_{\Phi}$, and $\lambda_{\Phi}$. These factors are asymptotically equivalent under the conditions stated in the theorem below, i.e., the ratio of any two of these factors converges to one as $j \rightarrow \infty$. To motivate this, note that for a highly available system we have $E T_{\Phi} \approx E_{0} S(1 / q) \approx E S(1 / q)$, observing that $E_{0} S$ equals the length of a cycle having no system failures and $1 / q$ equals the expected number of cycles until a system failure occurs (the number of such cycles is geometrically distributed with parameter $q$ ). We have $E_{0} S \approx E S$ when $q$ is small. Note also that

$$
\lambda_{\Phi}=\frac{E N_{S}}{E S}
$$

by the Renewal Reward Theorem (Theorem B.15, p. 280, in Appendix B). For a highly available system we have $E N_{S} \approx q$ and hence $\lambda_{\Phi} \approx q / E S$. Results from Monte Carlo simulations presented in [22] show that the factors $q / E_{0} S, q / E S$, and $1 / E T_{\Phi}$ typically give slightly better results (i.e., better fit to the exponential distribution) than the system failure rate $\lambda_{\Phi}$. From a computational point of view, however, $\lambda_{\Phi}$ is much more attractive than the other factors, which are in most cases quite difficult to compute. We therefore normally use $\lambda_{\Phi}$ as the normalizing factor.

The basic idea of the proof of the asymptotic exponentiality of $\alpha T_{\Phi}$ is as follows: If we assume that $\mathbf{X}$ is a regenerative process and the probability that a system failure occurs in a renewal cycle, i.e., $q$, is small (converges to zero), then the time to the first system failure will be approximately equal to the sum of a number of renewal cycles having no system failures; and this number of cycles is geometrically distributed with parameter $q$. Now if $q \rightarrow 0$ as $j \rightarrow \infty$, the desired result follows by using Laplace transformations. The result can be formulated in general terms as shown in the lemma below.

Note that series systems are excluded since such systems have $q=1$. We will analyze series systems later in this section; see Theorem 4.35, p. 143.

Lemma 4.24. Let $S, S_{i}, i=1,2, \ldots$, be a sequence of non-negative i.i.d. random variables with distribution function $F(t)$ having finite mean $a, a>0$ and finite variance, and let $\nu$ be a random variable independent of $\left(S_{i}\right)$, geometrically distributed with parameter $q(0<q \leq 1)$, i.e., $P(\nu=k)=q p^{k-1}, k=$ $1,2, \ldots, p=1-q$. Furthermore, let$$
S^{*}=\sum_{i=1}^{\nu-1} S_{i}
$$

Consider now a sequence $F_{j}, q_{j}(j=1,2, \ldots)$ satisfying the above conditions for each $j$. Then if (as $j \rightarrow \infty$ )

$$
q \rightarrow 0
$$

and

$$
q c_{S}^{2} \rightarrow 0
$$

where $c_{S}^{2}$ denotes the squared coefficient of variation of $S$, we have (as $j \rightarrow \infty$ )

$$
\frac{q S^{*}}{a} \xrightarrow{D} \operatorname{Exp}(1)
$$

Proof. Let $\tilde{S}^{*}=q S^{*} / a$. By conditioning on the value of $\nu$, it is seen that the Laplace transform of $S^{*}, L_{S^{*}}(x)=E e^{-x S^{*}}$, equals $q /[1-p L(x)]$, where $L(x)$ is the Laplace transform of $S_{i}$. Let $\psi(x)=[L(x)-1+a x] / x$. Then

$$
L_{S^{*}}(x)=\frac{q}{1-p(1-a x+x \psi(x))}
$$

We need to show that

$$
L_{\tilde{S}^{*}}(x)=E e^{-(q x / a) S^{*}} \rightarrow \frac{1}{1+x}
$$

since the convergence theorem for Laplace transforms then give the desired result. Noting that

$$
E e^{-(q x / a) S^{*}}=\frac{1}{1+p x-(p x / a) \psi(q x / a)}
$$

we must require that

$$
(x / a) \psi(q x / a) \rightarrow 0
$$

i.e.,

$$
[L(q x / a)-1+q x] / q \rightarrow 0
$$

Using $E S=a$ and the inequalities $0 \leq e^{-t}-1+t \leq t^{2} / 2$, we find that

$$
\begin{aligned}
0 \leq[L(q x / a)-1+q x] / q & =E\left[e^{-(q x / a) S}-1+(q x / a) S\right] / q \\
& \leq E[(q x / a) S]^{2} / 2 q \\
& =\frac{x^{2}}{2} \frac{q}{a^{2}} E S^{2} \\
& =\frac{x^{2}}{2} q\left(1+c_{S}^{2}\right)
\end{aligned}
$$The desired conclusion (4.47) follows now since $q \rightarrow 0$ and $q c_{S}^{2} \rightarrow 0$ (assumptions (4.45) and (4.46)).

Theorem 4.25. Assume that $\mathbf{X}$ is a regenerative process, and that $F_{i j}$ and $G_{i j}$ change in such a way that the following conditions hold (as $j \rightarrow \infty$ ):

$$
\begin{aligned}
q & \rightarrow 0 \\
q c_{0 S}^{2} & \rightarrow 0 \\
\frac{q E_{1} S}{E S} & \rightarrow 0 \\
E_{1}\left(N_{S}-1\right) & \rightarrow 0
\end{aligned}
$$

Then

$$
A\left[0, u / \lambda_{\Phi}\right] \rightarrow e^{-u}, \text { i.e., } \lambda_{\Phi} T_{\Phi} \xrightarrow{D} \operatorname{Exp}(1)
$$

Proof. Using Lemma 4.24, we first prove that under conditions (4.48)-(4.50) we have

$$
\frac{T_{\Phi} q}{E_{0} S} \xrightarrow{D} \operatorname{Exp}(1)
$$

Let $\nu$ denote the renewal cycle index associated with the time of the first system failure, $T_{\Phi}$. Then it is seen that $T_{\Phi}$ has the same distribution as

$$
\sum_{k=1}^{\nu-1} S_{0 k}+W_{\nu}
$$

where $\left(S_{0 k}\right)$ and $\left(W_{k}\right)$ are independent sequences of i.i.d. random variables with

$$
P\left(S_{0 k} \leq s\right)=P_{0}(S \leq s)
$$

and

$$
P\left(W_{k} \leq w\right)=P_{1}\left(T_{\Phi} \leq w\right)
$$

Both sequences are independent of $\nu$, which has a geometrical distribution with parameter $q=P\left(N_{S} \geq 1\right)$. Hence, (4.53) follows from Lemma 4.24 provided that

$$
\frac{W_{\nu} q}{E_{0} S} \xrightarrow{P} 0
$$

By a standard conditional probability argument it follows that

$$
E S=(1-q) E_{0} S+q E_{1} S
$$and by noting that

$$
\begin{aligned}
\frac{q E_{1} T_{\phi}}{E_{0} S} & =\frac{q E W}{E_{0} S} \leq \frac{q E_{1} S}{E_{0} S}=\frac{q E_{1} S(1-q)}{E S-q E_{1} S} \\
& =\frac{\frac{q E_{1} S}{E S}(1-q)}{1-\frac{q E_{1} S}{E S}} \rightarrow 0
\end{aligned}
$$

we see that (4.54) holds.
Using (4.44) we obtain

$$
\begin{aligned}
\frac{\lambda_{\phi}}{q / E_{0} S} & =\frac{\lambda_{\phi}}{q / E S} \frac{E_{0} S}{E S} \\
& =\frac{E N_{S} / E S}{q / E S} \frac{E_{0} S}{E S} \\
& =\frac{E N_{S}}{q} \frac{E_{0} S}{E S}
\end{aligned}
$$

Now $E N_{S} / q=1+E_{1}\left(N_{S}-1\right) \rightarrow 1$ in view of (4.51), and

$$
\frac{E_{0} S}{E S}=\frac{1-q \frac{E_{1} S}{E S}}{1-q} \rightarrow 1
$$

by (4.48) and (4.50). Hence the ratio of $\lambda_{\phi}$ and $q / E_{0} S$ converges to 1 . Combining this with (4.53), the conclusion of the theorem follows.

Remark 4.26. The above theorem shows that

$$
\alpha T_{\phi} \xrightarrow{D} \operatorname{Exp}(1)
$$

for $\alpha$ equal to $\lambda_{\phi}$. But the result also holds for the normalizing factors $q / E_{0} S, q / E S$, and $1 / E T_{\phi}$. For $q / E_{0} S$ and $q / E S$ this is seen from the proof of the theorem. To establish the result for $1 / E T_{\phi}$, let

$$
S^{*}=\sum_{i=1}^{\nu-1} S_{0 i}
$$

Then $E S^{*}=E_{0} S(1-q) / q$, observing that the mean of $\nu$ equals $1 / q$. It follows that

$$
E T_{\phi}=E_{0} S(1-q) / q+E_{1} T_{\phi}
$$

which can be rewritten as

$$
q E T_{\phi} / E_{0} S=1-q+q E_{1} T_{\phi} / E_{0} S
$$

We see that the right-hand side of this expression converges to 1 , remembering (4.48), (4.50), and (4.55). Hence, $1 / E T_{\phi}$ is also a normalizing factor. Note that the condition (4.51) is not required if the normalizing factor equals either $q / E_{0} S, q / E S$, or $1 / E T_{\phi}$.

We can conclude that the ratio between any of these normalizing factors converges to one if the conditions of the theorem hold true.# 4.4.2 Some Sufficient Conditions 

It is intuitively clear that if the components have constant failure rates, and the component unavailabilities converge to zero, then the conditions of Theorem 4.25 would hold. In Theorems 4.27 and 4.30 below this result will be formally established. We assume, for the sake of simplicity, that no single component is in series with the rest of the system. If there are one or more components in series with the rest of the system, we know that the time to failure of these components has an exact exponential distribution, and by independence it is straightforward to establish the limiting distribution of the total system.

Define

$$
d=\sum_{i=1}^{n} \lambda_{i} \mu_{G_{i}}, \quad \bar{\lambda}=\sum_{i=1}^{n} \lambda_{i}
$$

Theorem 4.27. Assume that the system has no components in series with the rest of the system, i.e., $\Phi\left(0_{i}, \mathbf{1}\right)=1$ for $i=1,2, \ldots, n$. Furthermore, assume that component $i$ has an exponential lifetime distribution with failure rate $\lambda_{i}>0, i=1,2, \ldots, n$.

If $d \rightarrow 0$ and there exist constants $c_{1}$ and $c_{2}$ such that $\lambda_{i} \leq c_{1}<\infty$ and $E R_{i}^{2} \leq c_{2}<\infty$ for all $i$, then the conditions (4.48),(4.49), and (4.50) of Theorem 4.25 are met, and, consequently, $\alpha T_{\Phi} \xrightarrow{f 1} \operatorname{Exp}(1)$ for $\alpha$ equal to $q / E_{0} S, q / E S$, or $1 / E T_{\phi}$.

Proof. As will be shown below, it is sufficient to show that $q \rightarrow 0$ holds (condition (4.48)) and that there exists a finite constant $c$ such that

$$
\bar{\lambda}^{2} E\left(S^{\prime \prime}\right)^{2} \leq c
$$

where $S^{\prime \prime}$ represents the "busy" period of the renewal cycle, which equals the time from the first component failure to the next regenerative point, i.e., to the time when the process again visits state $(1,1, \ldots, 1)$. (The term "busy" period is taken from queueing theory. In the busy period at least one component is under repair.) Let $S^{\prime}$ be an exponentially distributed random variable with parameter $\bar{\lambda}$ representing the time to the first component failure. This means that we can write

$$
S=S^{\prime}+S^{\prime \prime}
$$

Assume that we have already proved (4.56). Then this condition and (4.48) imply (4.50), noting that$$
\begin{aligned}
\frac{q E_{1} S}{E S} & \leq \tilde{\lambda} q E_{1} S \\
& =\tilde{\lambda}\left(q E_{1} S^{\prime}+q E_{1} S^{\prime \prime}\right) \\
& =q+\tilde{\lambda} q E\left[S^{\prime \prime} \mid N_{S} \geq 1\right] \\
& =q+\tilde{\lambda} E\left[S^{\prime \prime} I\left(N_{S} \geq 1\right)\right] \\
& \leq q+\tilde{\lambda} q^{1 / 2}\left[E\left(S^{\prime \prime}\right)^{2}\right]^{1 / 2} \\
& =q+q^{1 / 2}\left[\tilde{\lambda}^{2} E\left(S^{\prime \prime}\right)^{2}\right]^{1 / 2}
\end{aligned}
$$

where the last inequality follows from Schwartz's inequality. Furthermore, condition (4.56) together with (4.48) imply (4.49), noting that

$$
\begin{aligned}
c_{0 S}^{2} & \leq \frac{E_{0} S^{2}}{\left(E_{0} S\right)^{2}} \\
& \leq \tilde{\lambda}^{2} E_{0} S^{2} \\
& =\tilde{\lambda}^{2} E\left[S^{2} I\left(N_{S}=0\right)\right] /(1-q) \\
& \leq \tilde{\lambda}^{2} E S^{2} /(1-q) \\
& =\tilde{\lambda}^{2}\left\{E\left(S^{\prime}\right)^{2}+E\left(S^{\prime \prime}\right)^{2}+2 E\left[S^{\prime} S^{\prime \prime}\right]\right\} /(1-q) \\
& \leq \tilde{\lambda}^{2}\left\{\left(2 / \tilde{\lambda}^{2}\right)+E\left(S^{\prime \prime}\right)^{2}+2\left(E\left(S^{\prime}\right)^{2} E\left(S^{\prime \prime}\right)^{2}\right)^{1 / 2}\right\} /(1-q) \\
& =\left\{2+\tilde{\lambda}^{2} E\left(S^{\prime \prime}\right)^{2}+2\left(2^{1 / 2}\right)\left(\tilde{\lambda}^{2} E\left(S^{\prime \prime}\right)^{2}\right)^{1 / 2}\right\} /(1-q)
\end{aligned}
$$

where we again have used Schwartz's inequality. Alternatively, an upper bound on $E\left[S^{\prime} S^{\prime \prime}\right]$ can be established using that $S^{\prime}$ and $S^{\prime \prime}$ are independent:

$$
E\left[S^{\prime} S^{\prime \prime}\right]=E S^{\prime} E S^{\prime \prime}=(1 / \tilde{\lambda}) E S^{\prime \prime} \leq(1 / \tilde{\lambda})\left\{E\left(S^{\prime \prime}\right)^{2}\right\}^{1 / 2}
$$

Now, to establish (4.48), we note that with probability $\tilde{\lambda}_{i}=\lambda_{i} / \tilde{\lambda}$, the busy period begins at the time of the failure of component $i$. If, in the interval of repair of this component, none of the remaining components fails, then the busy period comes to an end when the repair is completed. Therefore, since there are no components in series with the rest of the system,

$$
1-q \geq \sum_{i=1}^{n} \tilde{\lambda}_{i} \int_{0}^{\infty} e^{-t\left(\tilde{\lambda}-\lambda_{i}\right)} d G_{i}(t)
$$

where $G_{i}$ is the distribution of the repair time of component $i$. Hence,

$$
\begin{aligned}
q & \leq \sum_{i=1}^{n} \tilde{\lambda}_{i} \int_{0}^{\infty}\left[1-e^{-t\left(\tilde{\lambda}-\lambda_{i}\right)}\right] d G_{i}(t) \\
& \leq \sum_{i=1}^{n} \lambda_{i} \int_{0}^{\infty} t d G_{i}(t)=d
\end{aligned}
$$

Consequently, $d \rightarrow 0$ implies $q \rightarrow 0$.It remains to show (4.56). Clearly, the busy period will only increase if we assume that the flow of failures of component $i$ is a Poisson flow with parameter $\lambda_{i}$, i.e., we adjoin failures that arise according to a Poisson process on intervals of repair of component $i$, assuming that repair begins immediately for each failure. This means that the process can be regarded as an $M / G / \infty$ queueing process, where the Poisson input flow has parameter $\tilde{\lambda}$ and there are an infinite number of devices with servicing time distributed according to the law

$$
G(t)=\sum_{i=1}^{n} \tilde{\lambda}_{i} G_{i}(t)
$$

Note that the probability that a "failure is due to component $i$ " equals $\tilde{\lambda}_{i}$. It is also clear that the busy period increases still more if, instead of an infinite number of servicing devices, we take only one, i.e., the process is a queueing process $M / G / 1$. Thus, $E\left(S^{\prime \prime}\right)^{2} \leq E\left(\tilde{S}^{\prime \prime}\right)^{2}$, where $\tilde{S}^{\prime \prime}$ is the busy period in a single-line system with a Poisson input flow $\tilde{\lambda}$ and servicing distribution $G(t)$. It is a well-known result from the theory of queueing processes (and branching processes) that the second-order moment of the busy period (extinction time) equals $E R_{G}^{2} /\left(1-\tilde{\lambda} E R_{G}\right)^{3}$, where $R_{G}$ is the service time having distribution $G$, see, e.g., [80]. Hence, by introducing $d_{2}=\sum_{i=1}^{n} \lambda_{i} E R_{i}^{2}$ we obtain

$$
\tilde{\lambda}^{2} E\left(S^{\prime \prime}\right)^{2} \leq \frac{\tilde{\lambda} d_{2}}{(1-d)^{3}} \leq \frac{n^{2} c_{1}^{2} c_{2}}{(1-d)^{3}}
$$

The conclusion of the theorem follows.
We now give sufficient conditions for $E_{1}(N-1) \rightarrow 0$ (assumption (4.51) in Theorem 4.25).

We define

$$
\bar{\mu}_{i}=\sup _{0 \leq t<t^{*}}\left\{E\left[R_{i 1}-t \mid R_{i 1}>t\right]\right\}
$$

where $t^{*}=\sup \left\{t \in \mathbb{R}_{+}: \bar{G}_{i}(t)>0\right\}$. We see that $\bar{\mu}_{i}$ expresses the maximum expected residual repair time of component $i$. We might have $\bar{\mu}_{i}=\infty$, but we shall in the following restrict attention to the finite case. We know from Sect. 2.2, p. 37, that if $G_{i}$ has the NBUE property, then

$$
\bar{\mu}_{i} \leq \mu_{G_{i}}
$$

If the repair times are bounded by a constant $c$, i.e., $P\left(R_{i k} \leq c\right)=1$, then $\bar{\mu}_{i} \leq c$. Let

$$
\tilde{\mu}=\sum_{i=1}^{n} \bar{\mu}_{i}
$$

Lemma 4.28. Assume that the lifetime of component $i$ is exponentially distributed with failure rate $\lambda_{i}, i=1,2, \ldots, n$. Then

$$
P_{1}\left(N_{S} \geq k\right) \leq(\tilde{\lambda} \tilde{\mu})^{k-1}, k=2,3, \ldots
$$Proof. The lemma will be shown by induction. We first prove that (4.57) holds true for $k=2$. Suppose the first system failure occurs at time $t$. Let $L_{t}$ denote the number of component failures after $t$ until all components are again functioning for the first time. Furthermore, let $R_{i t}$ denote the remaining repair time of component $i$ at time $t$ (put $R_{i t}=0$ if component $i$ is functioning at time $t$ ). Finally, let $V_{t}=\max _{i} R_{i t}$ and let $G_{V_{t}}(v)$ denote the distribution function of $V_{t}$. Note that $L_{t} \geq 1$ implies that at least one component must fail in the interval $\left(t, t+V_{t}\right)$ and that the probability of at least one component failure in this interval increases if we replace the failed components at $t$ by functioning components. Using these observations and the inequality $1-e^{-x} \leq$ $x$, we obtain

$$
\begin{aligned}
P\left(L_{t} \geq 1\right) & =\int_{0}^{\infty} P\left(L_{t} \geq 1 \mid V_{t}=v\right) d G_{V_{t}}(v) \\
& \leq \int_{0}^{\infty}\left(1-e^{-\tilde{\lambda} v}\right) d G_{V_{t}}(v) \\
& \leq \tilde{\lambda} \int_{0}^{\infty} v d G_{V_{t}}(v)=\tilde{\lambda} E V_{t} \leq \tilde{\lambda} E \sum_{i} R_{i t} \\
& \leq \tilde{\lambda} \tilde{\mu}
\end{aligned}
$$

Since $N_{S} \geq 2$ implies $L_{t} \geq 1$, formula (4.57) is shown for $k=2$ and $P_{1}$ conditional on the event that the first system failure occurs at time $t$. Integrating over the failure time $t$, we obtain (4.57) for $k=2$. Now assume that $P_{1}\left(N_{S} \geq k\right) \leq(\tilde{\lambda} \tilde{\mu})^{k-1}$ for a $k \geq 2$. We must show that

$$
P_{1}\left(N_{S} \geq k+1\right) \leq(\tilde{\lambda} \tilde{\mu})^{k}
$$

We have

$$
\begin{aligned}
P_{1}\left(N_{S} \geq k+1\right) & =P_{1}\left(N_{S} \geq k+1 \mid N_{S} \geq k\right) P_{1}\left(N_{S} \geq k\right) \\
& \leq P_{1}\left(N_{S} \geq k+1 \mid N_{S} \geq k\right) \cdot(\tilde{\lambda} \tilde{\mu})^{k-1}
\end{aligned}
$$

thus it remains to show that

$$
P_{1}\left(N_{S} \geq k+1 \mid N_{S} \geq k\right) \leq \tilde{\lambda} \tilde{\mu}
$$

Suppose that the $k$ th system failure in the renewal cycle occurs at time $t$. Then if at least one more system failure occurs in the renewal cycle, there must be at least one component failure before all components are again functioning, i.e., $L_{t} \geq 1$. Repeating the above arguments for $k=2$, the inequality (4.58) follows.

Remark 4.29. The inequality (4.57) states that the number of system failures in a renewal cycle when it is given that at least one system failure occurs is bounded in distribution by a geometrical random variable with parameter $\tilde{\lambda} \tilde{\mu}$ (provided this quantity is less than 1 )Theorem 4.30. Assume that the system has no components in series with the rest of the system. Furthermore, assume that component $i$ has an exponential lifetime distribution with failure rate $\lambda_{i}>0, i=1,2, \ldots, n$. If $d^{\prime} \rightarrow 0$, where $d^{\prime}=\tilde{\lambda} \tilde{\mu}$, and there exist constants $c_{1}$ and $c_{2}$ such that $\lambda_{i} \leq c_{1}<\infty$ and $E R_{i}^{2} \leq c_{2}<\infty$ for all $i$, then the conditions (4.48)-(4.51) of Theorem 4.25 (p. 129) are all met, and, consequently, the limiting result (4.52) holds, i.e., $\lambda_{\Phi} T_{\Phi} \xrightarrow{D} \operatorname{Exp}(1)$.

Proof. Since $d \leq d^{\prime}$, it suffices to show that condition (4.51) holds under the given assumptions. But from (4.57) of Lemma 4.28 we have

$$
E_{1}\left(N_{S}-1\right) \leq d^{\prime} /\left(1-d^{\prime}\right)
$$

and the desired result follows.
The above results show that the time to the first system failure is approximately exponentially distributed with parameter $q / E_{0} S \approx q / E S \approx 1 / E T_{\Phi} \approx$ $\lambda_{\Phi}$. For a system comprising highly available components, it is clear that $P\left(\mathbf{X}_{t}=\mathbf{1}\right)$ would be close to one, hence the above approximations for the interval reliability can also be used for an interval $(t, t+u]$.

# 4.4.3 Asymptotic Analysis of the Number of System Failures 

For a highly available system, the downtimes will be small compared to the uptimes, and the time from when the system has failed until it returns to the state $(1,1, \ldots, 1)$ will also be small. Hence, the above results also justify the Poisson process approximation for $N$. More formally, it can be shown that $N_{t / \alpha}$ converges in distribution to a Poisson distribution under the same assumptions as the first system failure time converges to the exponential distribution. Let $T_{\Phi}^{*}(k)$ denote the time between the $(k-1)$ th and the $k$ th system failure. From this sequence we define an associated sequence $T_{\Phi}(k)$ of i.i.d. variables, distributed as $T_{\Phi}$, by letting $T_{\Phi}(1)=T_{\Phi}^{*}(1), T_{\Phi}(2)$ be equal to the time to the first system failure following the first regenerative point after the first system failure, etc. Then it is seen that

$$
T_{\Phi}(1)+T_{\Phi}(2)\left(1-I\left(N_{(1)} \geq 2\right)\right) \leq T_{\Phi}^{*}(1)+T_{\Phi}^{*}(2) \leq T_{\Phi}(1)+T_{\Phi}(2)+S_{\nu}
$$

where $N_{(1)}=$ equals the number of system failures in the first renewal cycle having one or more system failures, and $S_{\nu}$ equals the length of this cycle ( $\nu$ denotes the renewal cycle index associated with the time of the first system failure). For $\alpha$ being one of the normalizing factors (i.e., $q / E_{0} S, q / E S, 1 / E T_{\Phi}$, or $\lambda_{\Phi}$ ), we will prove that $\alpha T_{\Phi}(2) I\left(N_{(1)} \geq 2\right)$ converges in probability to zero. It is sufficient to show that $P\left(N_{(1)} \geq 2\right) \rightarrow 0$ noting that

$$
P\left(\alpha T_{\Phi}(2) I\left(N_{(1)} \geq 2\right)>\epsilon\right) \leq P\left(N_{(1)} \geq 2\right)
$$But

$$
P\left(N_{(1)} \geq 2\right)=P_{1}\left(N_{S} \geq 2\right) \leq E_{1}\left(N_{S}-1\right)
$$

where the last expression converges to zero in view of (4.51), p. 129. The distribution of $S_{\nu}$ is the same as the conditional probability of the cycle length given a system failure occurs in the cycle, cf. Theorem 4.25 and its proof. Thus, if (4.48)-(4.51) hold, it follows that $\alpha\left(T_{\Phi}^{*}(1)+T_{\Phi}^{*}(2)\right)$ converges in distribution to the sum of two independent exponentially distributed random variables with parameter 1 , i.e.,

$$
\begin{aligned}
P\left(N_{t / \alpha} \geq 2\right) & =P\left(\alpha\left(T_{\Phi}^{*}(1)+T_{\Phi}^{*}(2)\right) \leq t\right) \\
& \rightarrow 1-e^{-t}-t e^{-t}
\end{aligned}
$$

Similarly, we establish the general distribution. We summarize the result in the following theorem.

Theorem 4.31. Assume that $\mathbf{X}$ is a regenerative process, and that $F_{i j}$ and $G_{i j}$ change in such a way that (asj $\rightarrow \infty$ ) the conditions (4.48)-(4.51) hold. Then $(a s j \rightarrow \infty)$

$$
N_{t / \alpha} \xrightarrow{D} \operatorname{Poisson}(t)
$$

where $\alpha$ is a normalizing factor that equals either $q / E_{0} S, q / E S, 1 / E T_{\Phi}$ or $\lambda_{\Phi}$.

Results from Monte Carlo simulations [22] indicate that the asymptotic system failure rate $\lambda_{\Phi}$ is normally preferable as parameter in the Poisson distribution when the expected number of system failures is not too small (less than one). When the expected number of system failures is small, the factor $1 / E T_{\Phi}$ gives slightly better results. The system failure rate is however easier to compute.

# Asymptotic Normality 

Now we turn to a completely different way to approximate the distribution of $N_{t}$. Above, the up and downtime distributions are assumed to change such that the system availability increases and after a time rescaling $N_{t}$ converges to a Poisson variable. Now we leave the up and downtime distribution unchanged and establish a central limit theorem as $t$ increases to infinity. The theorem generalizes (4.16), p. 114.

Theorem 4.32. If $\mathbf{X}$ is a regenerative process with cycle length $S, \operatorname{Var}[S]<$ $\infty$ and $\operatorname{Var}\left[N_{S}\right]<\infty$, then as $t \rightarrow \infty$,

$$
\sqrt{t}\left(\frac{N_{u+t}-N_{u}}{t}-\lambda_{\Phi}\right) \xrightarrow{D} \mathrm{~N}\left(0, \gamma_{\Phi}^{2}\right)
$$

where

$$
\gamma_{\Phi}^{2} E S=\operatorname{Var}\left[N_{S}-\lambda_{\Phi} S\right]
$$Proof. Noting that the system failure rate $\lambda_{\Phi}$ is given by

$$
\lambda_{\Phi}=\frac{E N_{S}}{E S}
$$

the result follows from Theorem B.17, p. 280, in Appendix B.
Below we argue that if the system failure rate is small, then we have

$$
\gamma_{\Phi}^{2} \approx \lambda_{\Phi}
$$

We obtain

$$
\begin{aligned}
\gamma_{\Phi}^{2} & =\frac{\operatorname{Var}\left[N_{S}-\lambda_{\Phi} S\right]}{E S}=\frac{E\left(N_{S}-\lambda_{\Phi} S\right)^{2}}{E S} \\
& \approx \frac{E N_{S}^{2}}{E S} \approx \frac{E N_{S}}{E S}=\lambda_{\Phi}
\end{aligned}
$$

where the last approximation follows by observing that if the system failure rate is small, then $N_{S}$ with a probability close to one is equal to the indicator function $I\left(N_{S} \geq 1\right)$. More formally, it is possible to show that under certain conditions, $\gamma_{\Phi}^{2} / \lambda_{\Phi}$ converges to one. We formulate the result in the following proposition.

Proposition 4.33. Assume $\mathbf{X}$ is a regenerative process with cycle length $S$ and that $F_{i j}$ and $G_{i j}$ change in such a way that conditions (4.48)-(4.50) of Theorem 4.25 (p. 129) hold (as $j \rightarrow \infty$ ). Furthermore, assume that (as $j \rightarrow \infty$ )

$$
E_{1}\left(N_{S}-1\right)^{2} \rightarrow 0
$$

and

$$
q c_{S}^{2} \rightarrow 0
$$

where $c_{S}^{2}$ denotes the squared coefficient of variation of $S$. Then (as $j \rightarrow \infty$ )

$$
\frac{\gamma_{\Phi}^{2}}{\lambda_{\Phi}} \rightarrow 1
$$

Proof. Using (4.60) and writing $N$ in place of $N_{S}$ we get

$$
\begin{aligned}
\frac{\gamma_{\Phi}^{2}}{\lambda_{\Phi}} & =\frac{E\left(N-\lambda_{\Phi} S\right)^{2}}{\lambda_{\Phi} E S} \\
& =\frac{q^{-1} E N^{2}+q^{-1}\left(\lambda_{\Phi}\right)^{2} E S^{2}-2 q^{-1} \lambda_{\Phi} E[N S]}{q^{-1} \lambda_{\Phi} E S} \\
& =\frac{E_{1} N^{2}+q^{-1}\left(\lambda_{\Phi}\right)^{2} E S^{2}-2 q^{-1} \lambda_{\Phi} E[N S]}{q^{-1} \lambda_{\Phi} E S}
\end{aligned}
$$

Since the denominator converges to 1 (the denominator equals the ratio between two normalizing factors), the result follows if we can show that $E_{1} N^{2}$converges to 1 and all the other terms of the numerator converge to zero. Writing

$$
E_{1} N^{2}=E_{1}[1+(N-1)]^{2}=1+E_{1}(N-1)^{2}+2 E_{1}(N-1)
$$

and using condition (4.62), it is seen that $E_{1} N$ converges to 1 . Now consider the term $q^{-1}\left(\lambda_{\Phi}\right)^{2} E S^{2}$. Using that $\lambda_{\Phi}=E N / E S$ (formula (4.61)) we obtain

$$
\begin{aligned}
q^{-1}\left(\lambda_{\Phi}\right)^{2} E S^{2} & =q^{-1}(E N / E S)^{2} E S^{2}=q^{-1}(E N)^{2}\left\{E S^{2} /(E S)^{2}\right\} \\
& =q\left(E_{1} N\right)^{2}\left(1+c_{S}^{2}\right)=q\left[1+E_{1}(N-1)\right]^{2}\left(1+c_{S}^{2}\right)
\end{aligned}
$$

Letting $q \rightarrow 0$ (condition (4.48)), and applying (4.62) and (4.63), we see that $q^{-1}\left(\lambda_{\Phi}\right)^{2} E S^{2}$ converges to zero. It remains to show that $q^{-1} \lambda_{\Phi} E[N S]$ converges to zero. But this is shown in the same way as the previous term, noting that

$$
E[N S] \leq\left(E N^{2}\right)^{1 / 2}\left(E S^{2}\right)^{1 / 2}
$$

by Schwartz's inequality. This completes the proof of the proposition.

Proposition 4.34. Under the same conditions as formulated in Theorem 4.30, p. 135, the following limiting result holds true (as $j \rightarrow \infty)$ :

$$
\frac{\gamma_{\Phi}^{2}}{\lambda_{\Phi}} \rightarrow 1
$$

Proof. It is sufficient to show that conditions (4.62) and (4.63) hold. Condition (4.62) follows by using that under $P_{1}, N$ is bounded in distribution by a geometrical distribution random variable with parameter $d^{\prime}=\tilde{\lambda} \tilde{\mu}$, cf. (4.57) of Lemma 4.28, p. 133. Note that for a variable $N$ that has a geometrical distribution with parameter $d^{\prime}$ we have

$$
\begin{aligned}
E(N-1)^{2} & =\sum_{k=1}^{\infty}(k-1)^{2}\left(d^{\prime}\right)^{k-1}\left(1-d^{\prime}\right) \\
& =\frac{d^{\prime}\left(1+d^{\prime}\right)}{\left(1-d^{\prime}\right)^{2}}
\end{aligned}
$$

From this equality it follows that $E_{1}\left(N_{S}-1\right)^{2} \rightarrow 0$ as $d^{\prime} \rightarrow 0$. To establish (4.63) we can repeat the arguments in the proof of Theorem 4.27, p. 131, showing (4.49), observing that

$$
c_{S}^{2} \leq \frac{E S^{2}}{(E S)^{2}} \leq \tilde{\lambda}^{2} E S^{2}
$$

For a parallel system of two components it is possible to establish simple expressions for some of the above quantities, such as $q$ and $E T_{\Phi}$.# Parallel System of Two Identical Components 

Consider a parallel system comprising two identical components having exponential life lengths with failure rate $\lambda$. Suppose one of the components has failed. Then we see that a system failure occurs, i.e., the number of system failures in the cycle is at least $1\left(N_{S} \geq 1\right)$, if the operating component fails before the repair is completed. Consequently,

$$
q=P\left(N_{S} \geq 1\right)=\int_{0}^{\infty} F(t) d G(t)=\int_{0}^{\infty}\left(1-e^{-\lambda t}\right) d G(t)
$$

where $F(t)=P(T \leq t)=1-e^{-\lambda t}$ and $G(t)=P(R \leq t)$ equal the component lifetime and repair time distribution, respectively. It follows that

$$
q \leq \int_{0}^{\infty} \lambda t d G(t)=\lambda \mu_{G}
$$

Thus for a parallel system comprising two identical components, it is trivially verified that the convergence of $\lambda \mu_{G}$ to zero implies that $q \rightarrow 0$. From the Taylor formula we have $1-e^{-x}=x-\frac{1}{2} x^{2}+x^{3} O(1), x \rightarrow 0$, where $|O(1)| \leq 1$. Hence, if $\lambda \mu_{G} \rightarrow 0$ and $E R^{3} / \mu_{G}^{3}$ is bounded by a finite constant, we have

$$
\begin{aligned}
q & =\lambda \mu_{G}-\frac{\lambda^{2}}{2} E R^{2}+\lambda^{3} E R^{3} O(1) \\
& =\lambda \mu_{G}-\frac{\left(\lambda \mu_{G}\right)^{2}}{2}\left(1+c_{G}^{2}\right)+o\left(\left(\lambda \mu_{G}\right)^{2}\right)
\end{aligned}
$$

where $c_{G}^{2}$ denotes the squared coefficient of variation of $G$ defined by $c_{G}^{2}=\operatorname{Var} R / \mu_{G}^{2}$. We can conclude that if $\lambda \mu_{G}$ is small, then comparing distributions $G$ with the same mean, those with a large variance exhibit a small probability $q$.

If we instead apply the Taylor formula $1-e^{-x}=x-x^{2} O(1)$, we can write

$$
q=\lambda \mu_{G}+o\left(\lambda \mu_{G}\right), \quad \lambda \mu_{G} \rightarrow 0
$$

For this example it is also possible to establish an explicit formula for $E_{0} S$. It is seen that

$$
E_{0} S=E \min \left\{T_{1}, T_{2}\right\}+E[R \mid R<T]
$$

where $T_{1}$ and $T_{2}$ are the times to failure of component 1 and 2 , respectively. But

$$
E \min \left\{T_{1}, T_{2}\right\}=\frac{1}{2 \lambda}
$$

and

$$
\begin{aligned}
E[R \mid R<T] & =E[R I(R<T)] /(1-q) \\
& =\int_{0}^{\infty} r e^{-\lambda r} d G(r) /(1-q)
\end{aligned}
$$This gives

$$
E_{0} S=\frac{1}{2 \lambda}+\frac{1}{1-q} \int_{0}^{\infty} r e^{-\lambda r} d G(r)
$$

From the Taylor formula we have $e^{-x}=1-x O(1), x \rightarrow 0$, where $|O(1)| \leq 1$. Using this and noting that

$$
\int_{0}^{\infty} r e^{-\lambda r} d G(r)=\mu_{G}\left[1+\lambda \mu_{G}\left(c_{G}^{2}+1\right) O(1)\right]
$$

it can be shown that if the failure rate $\lambda$ and the squared coefficient of variation $c_{G}^{2}$ are bounded by a finite constant, then the normalizing factor $q / E_{0} S$ is asymptotically given by

$$
\frac{q}{E_{0} S}=2 \lambda^{2} \mu_{G}+o\left(\lambda \mu_{G}\right), \quad \lambda \mu_{G} \rightarrow 0
$$

Now we will show that the system failure rate $\lambda_{\Phi}$, defined by (4.41), p. 123, is also approximately equal to $2 \lambda^{2} \mu_{G}$. First note that the unavailability of a component, $\bar{A}$, is given by $\bar{A}=\lambda \mu_{G} /\left(1+\lambda \mu_{G}\right)$. It follows that

$$
\lambda_{\Phi}=\frac{2 \bar{A}}{\lambda^{-1}+\mu_{G}}=2 \lambda^{2} \mu_{G}+o\left(\lambda \mu_{G}\right), \quad \lambda \mu_{G} \rightarrow 0
$$

provided that the failure rate $\lambda$ is bounded by a finite constant.
Next we will compute the exact distribution and mean of $T_{\Phi}$. Let us denote this distribution by $F_{T_{\Phi}}(t)$. In the following $F_{X}$ denotes the distribution of any random variable $X$ and $F_{i X}(t)=P_{i}(X \leq t), i=0,1$, where $P_{0}(\cdot)=P\left(\cdot \mid N_{S}=\right.$ 0 ) and $P_{1}(\cdot)=P\left(\cdot \mid N_{S} \geq 1\right)$. Observe that the length of a renewal cycle $S$ can be written as $S^{\prime}+S^{\prime \prime}$, where $S^{\prime}$ represents the time to the first failure of a component, and $S^{\prime \prime}$ represents the "busy" period, i.e., the time from when one component has failed until the process returns to the best state $(1,1)$. The variables $S^{\prime}$ and $S^{\prime \prime}$ are independent and $S^{\prime}$ is exponentially distributed with rate $\tilde{\lambda}=2 \lambda$. Now, assume a component has failed. Let $R$ denote the repair time of this component and let $T$ denote the time to failure of the operating component. Then

$$
F_{1 T}(t)=P(T \leq t \mid T \leq R)=\frac{1}{q} \int_{0}^{\infty}\left(1-e^{-\lambda(t \wedge r)}\right) d G(r)
$$

where $a \wedge b$ denotes the minimum of $a$ and $b$. Furthermore,

$$
F_{0 R}(t)=P(R \leq t \mid R<T)=\frac{1}{\bar{q}} \int_{0}^{t} e^{-\lambda r} d G(r)
$$

where $\bar{q}=1-q$. Now, by conditioning on whether a system failure occurs in the first renewal cycle or not, we obtain

$$
\begin{aligned}
F_{T_{\Phi}}(t) & =q P\left(T_{\Phi} \leq t \mid N_{S} \geq 1\right)+\bar{q} P\left(T_{\Phi} \leq t \mid N_{S}=0\right) \\
& =q F_{1 T_{\Phi}}(t)+\bar{q} F_{0 T_{\Phi}}(t)
\end{aligned}
$$To find an expression for $F_{1 T_{\Phi}}(t)$ we use a standard conditional probability argument, yielding

$$
\begin{aligned}
F_{1 T_{\Phi}}(t) & =\int_{0}^{t} P_{1}\left(T_{\Phi} \leq t \mid S^{\prime}=s\right) d F_{S^{\prime}}(s) \\
& =\int_{0}^{t} P(T \leq t-s \mid T \leq R) d F_{S^{\prime}}(s) \\
& =\int_{0}^{t} F_{1 T}(t-s) d F_{S^{\prime}}(s)
\end{aligned}
$$

Consider now $F_{0 T_{\Phi}}(t)$. By conditioning on $S=s$, we obtain

$$
\begin{aligned}
F_{0 T_{\Phi}}(t) & =\int_{0}^{t} P_{0}\left(T_{\Phi} \leq t \mid S=s\right) d F_{0 S}(s) \\
& =\int_{0}^{t} F_{T_{\Phi}}(t-s) d F_{0 S}(s)
\end{aligned}
$$

Inserting the above expressions into (4.65) gives

$$
F_{T_{\Phi}}(t)=h(t)+\bar{q} \int_{0}^{t} F_{T_{\Phi}}(t-s) d F_{0 S}(s)
$$

where

$$
h(t)=q \int_{0}^{t} F_{1 T}(t-s) d F_{S^{\prime}}(s)
$$

Hence, $F_{T_{\Phi}}(t)$ satisfies a renewal equation with the defective distribution $\bar{q} F_{0 S}(s)$, and arguing as in the proof of Theorem B.2, p. 275, in Appendix B, it follows that

$$
F_{T_{\Phi}}(t)=h(t)+\int_{0}^{t} h(t-s) d M_{0}(s)
$$

where the renewal function $M_{0}(s)$ equals

$$
\sum_{j=1}^{\infty} \bar{q}^{j} F_{0 S}^{* j}(s)
$$

Noting that $F_{0 S}=F_{S^{\prime}} * F_{0 R}$, the Laplace transform of $S^{\prime}$ equals $2 \lambda /(2 \lambda+v)$, $\bar{q}=L_{G}(\lambda)$ and $L_{F_{0 R}}(v)=L_{G}(v+\lambda) / L_{G}(\lambda)$, we see that the Laplace transform of $M_{0}$ takes the form

$$
L_{M_{0}}(v)=\frac{\bar{q} \frac{2 \lambda}{2 \lambda+v} L_{F_{0 R}}(v)}{1-\bar{q} \frac{2 \lambda}{2 \lambda+v} L_{F_{0 R}}(v)}=\frac{\frac{2 \lambda}{2 \lambda+v} L_{G}(v+\lambda)}{1-\frac{2 \lambda}{2 \lambda+v} L_{G}(v+\lambda)}
$$

It is seen that the Laplace transform of $F_{1 T}$ is given by

$$
L_{F_{1 T}}(v)=\frac{1}{1-L_{G}(\lambda)}\left(1-L_{G}(v+\lambda)\right) \frac{\lambda}{\lambda+v}
$$Now using (4.67) and (4.66) and the above expressions for the Laplace transform we obtain the following simple formula for $L_{F_{T_{\Phi}}}$ :

$$
L_{F_{T_{\Phi}}}(v)=\frac{2 \lambda^{2}}{\lambda+v} \cdot \frac{1-L_{G}(v+\lambda)}{v+2 \lambda\left(1-L_{G}(v+\lambda)\right)}
$$

The mean $E T_{\Phi}$ can be found from this formula, or alternatively by using a direct renewal argument. We obtain

$$
\begin{aligned}
E T_{\Phi} & =E S^{\prime}+E\left(T_{\Phi}-S^{\prime}\right) \\
& =\frac{1}{2 \lambda}+E \min \{R, T\}+(1-q) E T_{\Phi}
\end{aligned}
$$

noting that the time one component is down before system failure occurs or the renewal cycle terminates equals $\min \{R, T\}$. If a system failure does not occur, the process starts over again. It follows that

$$
E T_{\Phi}=\frac{1}{2 q \lambda}+\frac{E \min \{R, T\}}{q}
$$

Note that

$$
E \min \{R, T\}=\int_{0}^{\infty} \bar{F}(t) \bar{G}(t) d t=\int_{0}^{\infty} e^{-\lambda t} \bar{G}(t) d t
$$

It is also possible to write

$$
E T_{\Phi}=\frac{3}{2 \lambda} \frac{1-\frac{2}{3} L_{G}(\lambda)}{1-L_{G}(\lambda)}
$$

Now using the Taylor formula $e^{-x}=1-x O(1),|O(1)| \leq 1$, we obtain

$$
E \min \{R, T\}=\int_{0}^{\infty} e^{-\lambda t} \bar{G}(t) d t=\mu_{G}+\lambda \mu_{G}^{2}\left(c_{G}^{2}+1\right) O(1)
$$

where $c_{G}^{2}$ is the squared coefficient of variation of $G$. From this it can be shown that the normalizing factor $1 / E T_{\Phi}$ can be written in the same form as the other normalizing factors:

$$
\frac{1}{E T_{\Phi}}=2 \lambda^{2} \mu_{G}+o\left(\lambda \mu_{G}\right), \quad \lambda \mu_{G} \rightarrow 0
$$

assuming that $\lambda$ and $c_{G}^{2}$ are bounded by a finite constant.

# Asymptotic Analysis for Systems having Components in Series with the Rest of the System 

We now return to the general asymptotic analysis. Remember that $d=$ $\sum \lambda_{i} \mu_{G_{i}}$ and $\tilde{\lambda}=\sum \lambda_{i}$. So far we have focused on nonseries systems (seriessystem have $q=1$ ). Below we show that a series system also has a Poisson limit under the assumption that the lifetimes are exponentially distributed. We also formulate and prove a general asymptotic result for the situation that we have some components in series with the rest of the system. A component is in series with the rest of the system if $\Phi\left(0_{i}, \mathbf{1}\right)=0$.

Theorem 4.35. Assume that $\Phi$ is a series system and the lifetimes are exponentially distributed. Let $\lambda_{i}$ be the failure rate of component $i$. If $d \rightarrow 0$ (as $j \rightarrow \infty)$, then (as $j \rightarrow \infty$ )

$$
N_{t / \tilde{\lambda}} \xrightarrow{D} \operatorname{Poisson}(t)
$$

Proof. Let $N_{t}^{P}(i)$ be the Poisson process with intensity $\lambda_{i}$ generated by the consecutive uptimes of component $i$. Then it is seen that

$$
\sum_{i=1}^{n} N_{t / \tilde{\lambda}}^{P}(i)-D=N_{t / \tilde{\lambda}} \leq \sum_{i=1}^{n} N_{t / \tilde{\lambda}}^{P}(i)
$$

where

$$
D=\sum_{i=1}^{n} N_{t / \tilde{\lambda}}^{P}(i)-N_{t / \tilde{\lambda}}
$$

We have $D \geq 0$ and hence the conclusion of the theorem follows if we can show that $E D \rightarrow 0$, since then $D$ converges in probability to zero. Note that $\sum_{i=1}^{n} N_{t / \tilde{\lambda}}^{P}(i)$ is Poisson distributed with mean

$$
E \sum_{i=1}^{n} N_{t / \tilde{\lambda}}^{P}(i)=\sum_{i=1}^{n}(t / \tilde{\lambda}) \lambda_{i}=t
$$

From (4.36) of Corollary 4.18, p. 121, we have

$$
E N_{t / \tilde{\lambda}}=\sum_{i=1}^{n} \int_{0}^{t / \tilde{\lambda}}\left[h\left(1_{i}, \mathbf{A}(s)\right)-h\left(0_{i}, \mathbf{A}(s)\right)\right] \lambda_{i} A_{i}(s) d s
$$

which gives

$$
\begin{aligned}
E N_{t / \tilde{\lambda}} & =\sum_{i=1}^{n} \int_{0}^{t / \tilde{\lambda}} \prod_{k \neq i} A_{k}(s) \lambda_{i} A_{i}(s) d s \\
& =\tilde{\lambda} \int_{0}^{t / \tilde{\lambda}} \prod_{k=1}^{n} A_{k}(s) d s
\end{aligned}
$$

Using this expression together with (4.68), the inequalities $1-\prod_{i}\left(1-q_{i}\right) \leq$ $\sum_{i} q_{i}$, and the component unavailability bound (4.22) of Proposition 4.11, p. 114, $\left(\bar{A}_{i}(t) \leq \lambda_{i} \mu_{G_{i}}\right)$, we find that$$
\begin{aligned}
E D & =\tilde{\lambda} \int_{0}^{t / \tilde{\lambda}}\left[1-\prod_{i=1}^{n} A_{i}(s)\right] d s \\
& \leq \tilde{\lambda} \int_{0}^{t / \tilde{\lambda}} \sum_{i=1}^{n} \bar{A}_{i}(s) d s \\
& \leq \tilde{\lambda}(t / \tilde{\lambda}) \sum_{k=1}^{n} \lambda_{i} \mu_{G_{i}} \\
& =t d
\end{aligned}
$$

Now if $d \rightarrow 0$, we see that $E D \rightarrow 0$ and the proof is complete.

Remark 4.36. Arguing as in the proof of the theorem above it can be shown that if $a_{j} \rightarrow a$ as $j \rightarrow \infty$, then

$$
N_{a_{j} t / \tilde{\lambda}} \xrightarrow{D} \operatorname{Poisson}(t a)
$$

Observe that $\sum_{i=1}^{n} N_{a_{j} t / \tilde{\lambda}}^{P}(i)$ is Poisson distributed with parameter $a_{j} t$ and as $j \rightarrow \infty$ this variable converges in distribution to a Poisson variable with parameter at.

Theorem 4.37. Assume that the components have exponentially distributed lifetimes, and let $\lambda_{i}$ be the failure rate of component $i$. Let $A$ denote the set of components that are in series with the rest of the system, and let $B$ be the remaining components. Let $N^{A}, \tilde{\lambda}^{A}$, etc., denote the number of system failures, the total failure rate, etc., associated with the series system comprising the components in $A$. Similarly define $N^{B}, \alpha^{B}, d^{B}$, etc., for the system comprising the components in B. Assume that the following conditions hold (as $j \rightarrow \infty)$ :

1. $d \rightarrow 0$
2. The conditions of Theorem 4.25, p. 129, i.e., (4.48)-(4.51), hold for system $\stackrel{B}{\tilde{\lambda}^{A}} / \alpha^{B} \rightarrow a$.

Then $($ as $j \rightarrow \infty)$

$$
N_{t / \alpha^{B}} \xrightarrow{D} \operatorname{Poisson}(t(1+a))
$$

Remark 4.38. The conditions of Theorem 4.25 ensure that

$$
N_{t / \alpha^{B}}^{B} \xrightarrow{D} \operatorname{Poisson}(t)
$$

cf. Theorem 4.31, p. 136. Theorem 4.30, p. 135, gives sufficient conditions for $(4.48)-(4.51)$.Proof. First note that

$$
N_{t / \alpha^{B}} \leq N_{t / \alpha^{B}}^{A}+N_{t / \alpha^{B}}^{B}=N_{a_{j} t / \tilde{\lambda}^{A}}^{A}+N_{t / \alpha^{B}}^{B}
$$

where $a_{j}=\tilde{\lambda}^{A} / \alpha^{B}$. Now in view of Remark 4.36 above and the conditions of the theorem, it is sufficient to show that $D^{*}$, defined as the expected number of times system $A$ fails while system $B$ is down, or vice versa, converges to zero. But noting that the probability that system $A(B)$ is not functioning is less than or equal to $d$ (the unreliability of a monotone system is bounded by the sum of the component unreliabilities, which in its turn is bounded by $d$, cf. (4.22), p. 115), it is seen that

$$
\begin{aligned}
D^{*} & \leq d\left[E N_{a_{j} t / \tilde{\lambda}^{A}}^{A}+E N_{t / \alpha^{B}}^{B}\right] \leq d\left[\tilde{\lambda}^{A} a_{j} t / \tilde{\lambda}^{A}+E N_{t / \alpha^{B}}^{B}\right] \\
& =d\left[a_{j} t+E N_{t / \alpha^{B}}^{B}\right]
\end{aligned}
$$

To find a suitable bound on $E N_{t / \alpha^{B}}^{B}$, we need to refer to the argumentation in the proof of Theorem 4.43, formulas (4.88) and (4.93), p. 156. Using these results we can show that $E N_{t / \alpha^{B}}^{B} \rightarrow t$. Hence, $D^{*} \rightarrow 0$ and the theorem is proved.

# 4.5 Downtime Distribution Given System Failure 

In this section we study the downtime distribution of the system given that a failure has occurred. We investigate the downtime distribution given a failure at time $t$, the asymptotic (steady-state) distribution obtained by letting $t \rightarrow \infty$, and the distribution of the downtime following the $i$ th system failure. Recall that $\Phi$ represents the structure function of the system and $N_{t}$ the number of system failures in $[0, t]$. Component $i$ generates an alternating renewal process with uptime distribution $F_{i}$ and downtime distribution $G_{i}$, with means $\mu_{F_{i}}$ and $\mu_{G_{i}}$, respectively. The lifetime distribution $F_{i}$ is absolutely continuous with a failure rate function $\lambda_{i}$. The $n$ component processes are independent.

Let $\Delta N_{t}=N_{t}-N_{t-}$. Define $G_{\Phi}(\cdot, t)$ as the downtime distribution at time $t$, i.e.,

$$
G_{\Phi}(y, t)=P\left(Y \leq y \mid \Delta N_{t}=1\right)
$$

where $Y$ is a random variable representing the downtime (we omit the dependency on $t$ ). The asymptotic (steady-state) downtime distribution is given by

$$
G_{\Phi}(y)=\lim _{t \rightarrow \infty} G_{\Phi}(y, t)
$$

assuming that the limit exists. It turns out that it is quite simple to establish the asymptotic (steady-state) downtime distribution of a parallel system, so we first consider this category of systems.# 4.5.1 Parallel System 

Consider a parallel system comprising $n$ stochastically identical components, with repair time distribution $G$. Since a system failure coincides with one and only one component failure, we have

$$
P\left(Y>y \mid \Delta N_{t}=1\right)=\bar{G}(y)\left[\bar{G}_{\alpha_{t}}(y)\right]^{n-1}
$$

where $G_{\alpha_{t}}(y)=P\left(\alpha_{t}(i)>y \mid X_{i}(t)=0\right)$ denotes the distribution of the forward recurrence time in state 0 of a component. But we know from (4.14) and (4.15), p. 112, that the asymptotic distribution of $G_{\alpha_{t}}(y)$ is given by

$$
\lim _{t \rightarrow \infty} \bar{G}_{\alpha_{t}}(y)=\frac{\int_{y}^{\infty} \bar{G}(x) d x}{\mu_{G}}=\bar{G}_{\infty}(y)
$$

Thus we have proved the following theorem.
Theorem 4.39. For a parallel system of $n$ identical components, the asymptotic (steady-state) downtime distribution given system failure, equals

$$
G_{\Phi}(y)=1-\bar{G}(y)\left[\frac{\int_{y}^{\infty} \bar{G}(x) d x}{\mu_{G}}\right]^{n-1}
$$

Next we consider a parallel system of not necessarily identical components. We have the following result.

Theorem 4.40. Let $m_{i}(t)$ be the renewal density function of $M_{i}(t)$, and assume that $m_{i}(t)$ is right-continuous and satisfies

$$
\lim _{t \rightarrow \infty} m_{i}(t)=\frac{1}{\mu_{F_{i}}+\mu_{G_{i}}}
$$

For a parallel system of not necessarily identical components, the asymptotic (steady-state) downtime distribution given system failure equals

$$
G_{\Phi}(y)=\sum_{i=1}^{n} c_{i}\left[1-\bar{G}_{i}(y) \prod_{k \neq i} \frac{\int_{y}^{\infty} \bar{G}_{k}(x) d x}{\mu_{G_{k}}}\right]
$$

where

$$
c_{i}=\frac{1 / \mu_{G_{i}}}{\sum_{k=1}^{n} 1 / \mu_{G_{k}}}
$$

denotes the asymptotic (steady-state) probability that component $i$ causes a system failure.Proof. The proof follows the lines of the proof of Theorem 4.39, the difference being that we have to take into consideration which component causes system failure and the probability of this event given system failure. Clearly,

$$
1-\bar{G}_{i}(y) \prod_{k \neq i} \frac{\int_{y}^{\infty} \bar{G}_{k}(x) d x}{\mu_{G_{k}}}
$$

equals the asymptotic downtime distribution given that component $i$ causes system failure. Hence it suffices to show (4.72). Since the system failure rate $\lambda_{\Phi}$ is given by $\lambda_{\Phi}=\sum_{i=1}^{n} \lambda_{\Phi}^{(i)}$, where

$$
\lambda_{\Phi}^{(i)}=\prod_{k \neq i} \bar{A}_{k} \frac{1}{\mu_{F_{i}}+\mu_{G_{i}}}
$$

represents the expected number of system failures per unit of time caused by failures of component $i$, an intuitive argument gives that the asymptotic (steady-state) probability that component $i$ causes system failure equals

$$
\begin{aligned}
\frac{\lambda_{\Phi}^{(i)}}{\lambda_{\Phi}} & =\frac{\frac{1}{\mu_{F_{i}}+\mu_{G_{i}}} \prod_{k \neq i} \bar{A}_{k}}{\sum_{l=1}^{n} \frac{1}{\mu_{F_{l}}+\mu_{G_{l}}} \prod_{k \neq l} \bar{A}_{k}} \\
& =\frac{\frac{1}{\mu_{G_{i}}} \prod_{k=1}^{n} \bar{A}_{k}}{\sum_{l=1}^{n} \frac{1}{\mu_{G_{l}}} \prod_{k=1}^{n} \bar{A}_{k}}=c_{i}
\end{aligned}
$$

To establish sufficient conditions for this result to hold, we need to carry out a somewhat more formal proof. Let $c_{i}(t)$ be defined as the conditional probability that component $i$ causes system failure given that the system failure occurs at time $t$. For each $h>0$ let

$$
\begin{aligned}
N_{[t, t+h)}^{c}(i) & =\int_{[t, t+h)}\left(\Phi\left(1_{i}, \mathbf{X}_{s}\right)-\Phi\left(0_{i}, \mathbf{X}_{s}\right)\right) d N_{s}(i) \\
N_{[t, t+h)}^{c} & =\sum_{i=1}^{n} N_{[t, t+h)}^{c}(i)
\end{aligned}
$$

Then

$$
\begin{aligned}
c_{i}(t) & =\lim _{h \rightarrow 0+} \frac{P\left(N_{[t, t+h)}^{c}(i)=1\right)}{P\left(N_{[t, t+h)}^{c}=1\right)} \\
& =\lim _{h \rightarrow 0+} \frac{\frac{1}{h} E N_{[t, t+h)}^{c}(i)-o_{i}(1)}{\frac{1}{h} E N_{[t, t+h)}^{c}-o(1)}
\end{aligned}
$$

where

$$
o_{i}(1)=E\left[N_{[t, t+h)}^{c}(i)\right) I\left(N_{[t, t+h)}^{c}(i) \geq 2\right)] / h
$$and

$$
o(1)=E\left[N_{[t, t+h)}^{c}\right) I\left(N_{[t, t+h)}^{c} \geq 2\right)] / h
$$

Hence it remains to study the limit of the ratio of the first terms of (4.73). Using that

$$
E N_{[t, t+h)}^{c}(i)=\int_{[t, t+h)}\left(h\left(1_{i}, \mathbf{A}(s)\right)-h\left(0_{i}, \mathbf{A}(s)\right) m_{i}(s) d s\right.
$$

where $A_{i}(s)=P\left(X_{s}(i)=1\right)$ equals the availability of component $i$ at time $s$, it follows that

$$
c_{i}(t)=\frac{\left\{h\left(1_{i}, \mathbf{A}(t)\right)-h\left(0_{i}, \mathbf{A}(t)\right)\right\} m_{i}(t)}{\sum_{k=1}^{n}\left\{h\left(1_{k}, \mathbf{A}(t)\right)-h\left(0_{k}, \mathbf{A}(t)\right)\right\} m_{k}(t)}
$$

From this expression, we see that $\lim _{t \rightarrow \infty} c_{i}(t)=c_{i}$ provided that

$$
\lim _{t \rightarrow \infty} m_{i}(t)=\frac{1}{\mu_{F_{i}}+\mu_{G_{i}}}
$$

This completes the proof of the theorem.

Remark 4.41. 1. From renewal theory (see Theorem B.10, p. 278, in Appendix B) sufficient conditions can be formulated for the limiting result (4.71) to hold true. For example, if the renewal cycle lengths $T_{i k}+R_{i k}$ have a density function $h$ with $h(t)^{p}$ integrable for some $p>1$, and $h(t) \rightarrow 0$ as $t \rightarrow \infty$, then $M_{i}$ has a density $m_{i}$ such that $m_{i}(t) \rightarrow 1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$ as $t \rightarrow \infty$. If component $i$ has an exponential lifetime distribution with parameter $\lambda_{i}$, then we know that $m_{i}(t)=\lambda_{i} A_{i}(t) \quad$ (cf. (4.18), p. 114), which converges to $1 /\left(\mu_{F_{i}}+\mu_{G_{i}}\right)$.
2. From the above proof it is seen that the downtime distribution at time $t$, $G_{\Phi}(y, t)$, is given by

$$
G_{\Phi}(y, t)=\sum_{i=1}^{n} c_{i}(t)\left[1-\bar{G}_{i}(y) \prod_{k \neq i} \bar{G}_{k \alpha_{t}}(y)\right]
$$

# 4.5.2 General Monotone System 

Consider now an arbitrary monotone system comprising the minimal cut sets $K_{k}, k=1,2, \ldots, k_{0}$. No simple formula exists for the downtime distribution in this case. But for highly available systems the following formula can be used to approximate the downtime distribution:

$$
\sum_{k} r_{k} G_{K_{k}}(y)
$$where

$$
r_{k}=\frac{\lambda_{K_{k}}}{\sum_{l} \lambda_{K_{l}}}
$$

Here $\lambda_{K_{k}}$ and $G_{K_{k}}$ denote the asymptotic (steady-state) failure rate of minimal cut set $K_{k}$ and the asymptotic (steady-state) downtime distribution of minimal cut set $K_{k}$, respectively, when this set is considered in isolation (i.e., we consider the parallel system comprising the components in $K_{k}$ ). We see that $r_{k}$ is approximately equal to the probability that minimal cut set $K_{k}$ causes system failure. Refer to $[23,72]$ for more detailed analyses in the general case. In [72] it is formally proved that the asymptotic downtime distribution exists and is equal to the steady-state downtime distribution.

# 4.5.3 Downtime Distribution of the $i$ th System Failure 

The above asymptotic (steady-state) formulas for $G_{\Phi}$ give in most cases good approximations to the downtime distribution of the $i$ th system failure, $i \in \mathbb{N}$. Even for the first system failure observed, the asymptotic formulas produce relatively accurate approximations. This is demonstrated by Monte Carlo simulations in [23]. An example is given below. Let the distance measure $D_{i}(y)$ be defined by

$$
D_{i}(y)=\left|G_{\Phi}(y)-\hat{G}_{i, \Phi}(y)\right|
$$

where $\hat{G}_{i, \Phi}(y)$ equals the "true" downtime distribution of the $i$ th system failure obtained by Monte Carlo simulations. In Fig. 4.3 the distance measure of the first and second system failure have been plotted as a function of $y$ for a parallel system of two identical components with constant repair times and exponential lifetimes. As we can see from the figure, the distance is quite small; the maximum distance is about 0.012 for $i=1$ and 0.004 for $i=2$.


Fig. 4.3. The distance $D_{i}(y), i=1,2$, as a function of $y$ for a parallel system of two components with constant repair times, $\mu_{G}=1, \lambda=0.1$Only for some special cases are explicit expressions for the downtime distribution of the $i$ th system failure known. Below we present such expressions for the downtime distribution of the first failure for a two-component parallel system of identical components with exponentially distributed lifetimes.
Theorem 4.42. For a parallel system of two identical components with constant failure rate $\lambda$ and repair time distribution $G$, the downtime distribution $G_{1, p 2}(y)$ of the first system failure is given by

$$
\begin{aligned}
G_{1, p 2}(y) & =1-\bar{G}(y) \frac{\int_{0}^{\infty} \int_{0}^{s} \bar{G}(y+s-x) d F(x) d F(s)}{\int_{0}^{\infty} \int_{0}^{s} \bar{G}(s-x) d F(x) d F(s)} \\
& =1-\bar{G}(y) \frac{\int_{y}^{\infty}\left[1-e^{-\lambda(r-y)}\right] d G(r)}{\int_{0}^{\infty}\left[1-e^{-\lambda r}\right] d G(r)}
\end{aligned}
$$

Proof. Let $T_{i}$ and $R_{i}$ have distribution function $F$ and $G$, respectively, $i=1,2$, and let

$$
Y=\min _{1 \leq i \leq 2}\left(T_{i}+R_{i}\right)-\max _{1 \leq i \leq 2}\left(T_{i}\right)
$$

It is seen that the downtime distribution $G_{1, p 2}(y)$ equals the conditional distribution of $Y$ given that $Y>0$. The equality (4.74) follows if we can show that

$$
P(Y>y)=\bar{G}(y) \int_{0}^{\infty} \int_{0}^{s} 2 \bar{G}(y+s-x) d F(x) d F(s)
$$

Consider the event that $T_{i}=s, T_{j}=x, R_{i}>y$, and $T_{j}+R_{j}>y+s$ for $x<s$ and $j \neq i$. For this event it holds that $Y$ is greater than $y$. The probability of this event, integrated over all $s$ and $x$, is given by

$$
\int_{0}^{\infty} \int_{0}^{s} \bar{G}(y+s-x) \bar{G}(y) d F(x) d F(s)
$$

By taking the union over $i=1,2$, we find that (4.76) holds.
But the double integral in (4.76) can be written as

$$
\begin{aligned}
& \int_{0}^{\infty} 2 \int_{0}^{s} \bar{G}(y+s-x) d\left(1-e^{-\lambda x}\right) d\left(1-e^{-\lambda s}\right) \\
& \quad=1-\int_{0}^{\infty} \int_{0}^{s} G(y+s-x) 2 \lambda^{2} e^{-\lambda(x+s)} d x d s \\
& \quad=1-\int_{0}^{\infty} \int_{x}^{\infty} G(y+s-x) \lambda e^{-\lambda(s-x)} 2 \lambda e^{-2 \lambda x} d s d x
\end{aligned}
$$

Introducing $r=y+s-x$ gives

$$
\begin{aligned}
1- & \int_{0}^{\infty} 2 \lambda e^{-2 \lambda x} \int_{y}^{\infty} G(r) \lambda e^{-\lambda(r-y)} d r d x \\
& =1-\int_{y}^{\infty} G(r) \lambda e^{-\lambda(r-y)} d r \\
& =\int_{y}^{\infty}\left(1-e^{-\lambda(r-y)}\right) d G(r)
\end{aligned}
$$Thus the formulas (4.75) and (4.74) in the theorem are identical. This completes the proof of the theorem.

Now what can we say about the limiting downtime distribution of the first system failure as the failure rate converges to 0 ? Is it equal to the steadystate downtime distribution $G_{\Phi}$ ? Yes, for the above example we can show that if the failure rate converges to 0 , the distribution $G_{1, p 2}(y)$ converges to the steady-state formula, i.e.,

$$
\lim _{\lambda \rightarrow 0} G_{1, p 2}(y)=1-\bar{G}(y) \frac{\int_{y}^{\infty} \bar{G}(r) d r}{\mu_{G}}=G_{\Phi}(y)
$$

This is seen by noting that

$$
\begin{gathered}
\lim _{\lambda \rightarrow 0} \frac{\int_{y}^{\infty}\left[1-e^{-\lambda(r-y)}\right] d G(r)}{\int_{0}^{\infty}\left[1-e^{-\lambda r}\right] d G(r)}=\frac{\int_{y}^{\infty}(r-y) d G(r)}{\int_{0}^{\infty} r d G(r)} \\
=\frac{\int_{y}^{\infty} \bar{G}(r) d r}{\int_{0}^{\infty} \bar{G}(r) d r}
\end{gathered}
$$

This result can be extended to general monotone systems, and it is not necessary to establish an exact expression for the distribution of the first downtime; see [72]. Consider the asymptotic set-up introduced in Sect.4.4, to study highly available components, with exponential lifetime distributions $F_{i j}(t)=1-e^{-\lambda_{i j} t}$ and fixed repair time distributions $G_{i}$, and where we assume $\lambda_{i j} \rightarrow 0$ as $j \rightarrow \infty$. Then for a parallel system it can be shown that the distribution of the $i$ th system downtime converges as $j \rightarrow \infty$ to the steadystate downtime distribution $G_{\Phi}$. For a general system it is more complicated. Assuming that the steady-state downtime distribution converges as $j \rightarrow \infty$ to $G_{\Phi}^{*}$ (say), it follows that the distribution of the $i$ th system downtime converges to the same limit. See [72] for details.

# 4.6 Distribution of the System Downtime in an Interval 

In this section we study the distribution of the system downtime in a time interval. The model considered is as described in Sect. 4.3, p. 120. The system analyzed is monotone and comprises $n$ independent components. Component $i$ generates an alternating renewal process with uptime distribution $F_{i}$ and downtime distribution $G_{i}$.

We immediately observe that the asymptotic expression for the expected average downtime presented in Theorem 4.13, p. 116, also holds for monotone systems, with $A=h(\mathbf{A})$. Formula (4.28) of Theorem 4.13 requires that the process $\mathbf{X}$ is a regenerative process with finite expected cycle length.

The rest of this section is organized as follows. First we present some approximative methods for computing the distribution of $Y_{u}$ (the downtime inthe time interval $[0, u])$ in the case that the components are highly available, utilizing that $\left(Y_{u}\right)$ is approximately a compound Poisson process, denoted $\left(\mathrm{CP}_{u}\right)$, and the exact one-unit formula (4.30), p. 118, for the downtime distribution. Then we formulate some sufficient conditions for when the distribution of $\mathrm{CP}_{u}$ is an asymptotic limit. The framework is the same as described in Sect.4.4.1, p. 126. Finally, we study the convergence to the normal distribution.

# 4.6.1 Compound Poisson Process Approximation 

We assume that the components have constant failure rate and that the components are highly available, i.e., the products $\lambda_{i} \mu_{G_{i}}$ are small. Then it can be heuristically argued that the process $\left(Y_{u}\right), u \in \mathbb{R}_{+}$, is approximately a compound Poisson process,

$$
Y_{u} \approx \sum_{i=1}^{N_{u}} Y_{i} \approx \mathrm{CP}_{u}
$$

Here $N_{u}$ is the number of system failures in $[0, u]$ and $Y_{i}$ is the downtime of the $i$ th system failure. The dependency between $N_{u}$ and the random variables $Y_{i}$ is not "very strong" since $N_{u}$ is mainly governed by the renewal cycles without system failures. We can ignore downtimes $Y_{i}$ being the second, third, etc., system failure in a renewal cycle of the process $\mathbf{X}$. The probability of having two or more system failures in a cycle is small since we are assuming highly available components. This means that the random variables $Y_{i}$ are approximately independent and identically distributed.

From this we can find an approximate expression for the distribution of $Y_{u}$.

A closely related approximation can be established by considering system operational time, as described in the following.

Let $N_{s}^{\text {op }}$ be the number of system failures in $[0, s]$ when we consider operational time. Similar to the reasoning in Sect.4.4, p. 125, it can be argued that $N_{s}^{\text {op }}$ is approximately a homogeneous Poisson process with intensity $\lambda_{\Phi}^{\prime}$, where $\lambda_{\Phi}^{\prime}$ is given by

$$
\lambda_{\Phi}^{\prime}=\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\left(\mu_{F_{i}}+\mu_{G_{i}}\right) h(\mathbf{A})}
$$

To motivate this result, we note that the expected number of system failures per unit of time when considering calendar time is approximately equal to the asymptotic (steady-state) system failure rate $\lambda_{\Phi}$, given by (cf. formula (4.41), p. 123)

$$
\lambda_{\Phi}=\sum_{i=1}^{n} \frac{h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)}{\mu_{F_{i}}+\mu_{G_{i}}}
$$Then observing that the ratio between calendar time and operational time is approximately $1 / h(\mathbf{A})$, we see that the expected number of system failures per unit of time when considering operational time, $E N^{\text {op }}(u, u+w] / w$, is approximately equal to $\lambda_{\Phi} / h(\mathbf{A})$ Furthermore, $N_{[u, u+w]}^{\text {op }}$ is "nearly independent" of the history of $N^{\text {op }}$ up to $u$, noting that the state process $\mathbf{X}$ frequently restarts itself probabilistically, i.e., $\mathbf{X}$ re-enters the state $(1,1, \ldots, 1)$. It can be shown by repeating the proof of the Poisson limit Theorem 4.31, p. 136, and using the fact that $h(\mathbf{A}) \rightarrow 1$ as $\lambda_{i} \mu_{G_{i}} \rightarrow 0$, that $N_{t / \alpha}^{\text {op }}$ has an asymptotic Poisson distribution with parameter $t$. The system downtimes given system failure are approximately identically distributed with distribution function $G(y)$, say, independent of $N^{\text {op }}$, and approximately independent observing that the state process $\mathbf{X}$ with a high probability restarts itself quickly after a system failure. The distribution function $G(y)$ is normally taken as the asymptotic (steadystate) downtime distribution given system failure or an approximation to this distribution; see Sect.4.5.

Considering the system as a one-unit system, we can now apply the exact formula (4.30), p. 118, for the downtime distribution with the Poisson parameter $\lambda_{\Phi}^{\prime}$. It follows that

$$
P\left(Y_{u} \leq y\right) \approx \sum_{n=0}^{\infty} G^{* n}(y) \frac{\left[\lambda_{\Phi}^{\prime}(u-y)\right]^{n}}{n!} e^{-\lambda_{\Phi}^{\prime}(u-y)}=P_{u}(y)
$$

where the equality is given by definition. Formula (4.78) gives good approximations for "typical real life cases" with small component availabilities; see [82]. Figure 4.4 presents the downtime distribution for a parallel system of two components with the repair times identical to 1 and $\mu_{F}=10$ using the steady-state formula $G_{\Phi}$ for $G$ (formula (4.70), p. 146). The "true" distribution is found using Monte Carlo simulation. We see that formula (4.78) gives a good approximation.

# 4.6.2 Asymptotic Analysis 

We argued above that $\left(Y_{u}\right)$ is approximately equal to a compound Poisson process when the system comprises highly available components. In the following theorem we formalize this result.

The set-up is the same as in Sect.4.4.1, p. 126. We consider for each component $i$ a sequence $\left\{F_{i j}, G_{i j}\right\}, j \in \mathbb{N}$, of distributions satisfying certain conditions. To simplify notation, we normally omit the index $j$. When assuming in the following that $\mathbf{X}$ is a regenerative process, it is tacitly understood for all $j \in \mathbb{N}$.

We say that the renewal cycle is a "success" if no system failure occurs during the cycle and a "fiasco" if a system failure occurs.

Let $\alpha$ be a suitable normalizing factor (or more precisely, a normalizing sequence in $j$ ) such that $N_{t / \alpha}$ converges in distribution to a Poisson variable

Fig. 4.4. $P_{10}(y)$ and $P\left(Y_{10} \leq y\right)$ for a parallel system of two components with constant repair times, $\mu_{G}=1, \lambda=0.1$
with mean $t$, cf. Theorem 4.31, p. 136. Normally we take $\alpha=\lambda_{\Phi}$, but we could also use $q / E_{0} S, q / E S$, or $1 / E T_{\Phi}$, where $q$ equals the probability that a system failure occurs in a cycle, $S$ equals the length of a cycle, $E_{0} S$ equals the expected length of a cycle with no system failures, and $T_{\Phi}$ equals the time to the first system failure. Furthermore, let $Y_{i 1}$ denote the length of the first downtime of the system in the $i$ th "fiasco" renewal cycle, and $Y_{i 2}$ the length of the remaining downtime in the same cycle. We assume that the asymptotic distribution of $Y_{i 1}$ exists (as $j \rightarrow \infty$ ): $Y_{i 1} \xrightarrow{D} G_{\Phi}^{*}$ (say).

A random variable is denoted $\mathrm{CP}(r, G)$ if it has the same distribution as $\sum_{i=1}^{N} Y_{i}$, where $N$ is a Poisson variable with mean $r$, the variables $Y_{i}$ are i.i.d. with distribution function $G$, and $N$ and $Y_{i}$ are independent. The distribution of $\mathrm{CP}(r, G)$ equals

$$
\sum_{i=0}^{\infty} G^{* i} \frac{r^{i}}{i!} e^{-r}
$$

where $G^{* i}$ denotes $i$ th convolution of $G$.
Theorem 4.43. Assume that $\mathbf{X}$ is a regenerative process, and that $F_{i j}$ and $G_{i j}$ change in such a way that the following conditions hold (as $j \rightarrow \infty$ ):

$$
\begin{aligned}
q & \rightarrow 0 \\
q c_{0 S}^{2} & \rightarrow 0
\end{aligned}
$$

where $c_{0 S}^{2}=\left[E_{0} S^{2} /\left(E_{0} S\right)^{2}\right]-1$ denotes the squared coefficient of variation of $S$ under $P_{0}$,$$
\begin{aligned}
\frac{q E_{1} S}{E S} & \rightarrow 0 \\
E_{1}\left(N_{S}-1\right) & \rightarrow 0 \\
Y_{i 1} & \xrightarrow{D} G_{\Phi}^{*}
\end{aligned}
$$

Then $($ as $j \rightarrow \infty)$

$$
Y_{t / \alpha} \xrightarrow{D} \mathrm{CP}\left(t, G_{\Phi}^{*}\right)
$$

where $\alpha=\lambda_{\Phi}, q / E_{0} S, q / E S$, or $1 / E T_{\Phi}$.
Proof. First we will introduce two renewal processes, $N^{\prime}$ and $N^{\prime \prime}$, having the same asymptotic properties as $N_{t / \alpha}$. From Theorem 4.31, p. 136, we know that

$$
N_{t / \alpha} \xrightarrow{D} \operatorname{Poisson}(t)
$$

under conditions (4.79)-(4.82).
Let $\nu(1)$ equal the renewal cycle index associated with the first "fiasco" renewal cycle, and let $U_{1}$ denote the time to the starting point of this cycle, i.e.,

$$
U_{1}=\sum_{i=1}^{\nu(1)-1} S_{i}
$$

Note that if the first cycle is a "fiasco" cycle, then $U_{1}=0$. Starting from the beginning of the renewal cycle $\nu(1)+1$, we define $U_{2}$ as the time to the starting point of the next "fiasco" renewal cycle. Similarly we define $U_{3}, U_{4}, \ldots$. The random variables $U_{i}$ are equal the interarrival times of the renewal process $N_{t}^{\prime \prime}$, i.e.,

$$
N_{t}^{\prime \prime}=\sum_{k=1}^{\infty} I\left(\sum_{i=1}^{k} U_{i} \leq t\right)
$$

By repeating the proofs of Theorem 4.25 (p. 129) and Theorem 4.31 it is seen that

$$
N_{t / \alpha}^{\prime \prime} \xrightarrow{D} \operatorname{Poisson}(t)
$$

Using that the process $N_{t}^{\prime \prime}$ and the random variables $Y_{i}$ are independent, and the fact that $Y_{i 1} \xrightarrow{D} G_{\Phi}^{*}$ (assumption (4.83)), it follows that

$$
\sum_{i=1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 1} \xrightarrow{D} \mathrm{CP}\left(t, G_{\Phi}^{*}\right)
$$

A formal proof of this can be carried out using Moment Generating Functions.
Next we introduce $N_{t}^{\prime}$ as the renewal process having interarrival times with the same distribution as $U_{1}+S_{\nu(1)}$, i.e., the renewal cycle also includes the "fiasco" cycle. It follows from the proof of Theorem 4.25, using condition (4.81), that $N_{t / \alpha}^{\prime}$ has the same asymptotic Poisson distribution as $N_{t / \alpha}$.It is seen that

$$
\begin{aligned}
& N_{t}^{\prime} \leq N_{t}^{\prime \prime} \\
& N_{t}^{\prime} \leq N_{t} \leq \sum_{i=1}^{N_{t}^{\prime \prime}} N_{(i)}=N_{t}^{\prime \prime}+\sum_{i=1}^{N_{t}^{\prime \prime}}\left(N_{(i)}-1\right)
\end{aligned}
$$

where $N_{(i)}$ equals the number of system failures in the $i$ th "fiasco" cycle. Note that $N_{t}^{\prime \prime}$ is at least the number of "fiasco" cycles up to time $t$, including the one that is possibly running at $t$, and $N_{t}^{\prime}$ equals the number of finished "fiasco" cycles at time $t$ without the one possibly running at $t$.

Now to prove the result (4.84) we will make use of the following inequalities:

$$
\begin{aligned}
& Y_{t / \alpha} \leq \sum_{i=1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 1}+\sum_{i=1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 2} \\
& Y_{t / \alpha} \geq \sum_{i=1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 1}-\sum_{i=N_{t / \alpha}^{\prime}+1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 1}
\end{aligned}
$$

In view of (4.86), and the inequalities (4.89) and (4.90), we need to show that

$$
\begin{array}{r}
\sum_{i=1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 2} \xrightarrow{P} 0 \\
\sum_{i=N_{t / \alpha}^{\prime}+1}^{N_{t / \alpha}^{\prime \prime}} Y_{i 1} \xrightarrow{P} 0
\end{array}
$$

To establish (4.91) we first note that

$$
Y_{i 2} \xrightarrow{P} 0
$$

since

$$
P\left(Y_{i 2}>\epsilon\right) \leq P_{1}\left(N_{S} \geq 2\right) \leq E_{1}\left(N_{S}-1\right) \rightarrow 0
$$

by (4.82). Using Moment Generating Functions it can be shown that (4.91) holds.

The key part of the proof of (4.92) is to show that $\left(N_{t / \alpha}^{\prime \prime}\right)$ is uniformly integrable in $j$ ( $t$ fixed). If this result is established, then since $N_{t / \alpha}^{\prime \prime} \xrightarrow{D}$ Poisson $(t)$ by (4.85) it follows that

$$
E N_{t / \alpha}^{\prime \prime} \rightarrow t
$$

And because of the inequality (4.87), $\left(N_{t / \alpha}^{\prime}\right)$ is also uniformly integrable so that $E N_{t / \alpha}^{\prime} \rightarrow t$, and we can conclude that (4.92) holds noting that$$
P\left(N_{t / \alpha}^{\prime \prime}-N_{t / \alpha}^{\prime} \geq 1\right) \leq E N_{t / \alpha}^{\prime \prime}-E N_{t / \alpha}^{\prime} \rightarrow 0
$$

Thus it remains to show that $\left(N_{t / \alpha}^{\prime \prime}\right)$ is uniformly integrable.
Let $F_{U}$ denote the probability distribution of $U$ and let $V_{l}=\sum_{i=1}^{l} U_{i}$. Then we obtain

$$
\begin{aligned}
E\left[N_{t / \alpha}^{\prime \prime} I\left(N_{t / \alpha}^{\prime \prime} \geq k\right)\right] & =\sum_{l=k}^{\infty} P\left(N_{t / \alpha}^{\prime \prime} \geq l\right)+(k-1) P\left(N_{t / \alpha}^{\prime \prime} \geq k\right) \\
& =\sum_{l=k}^{\infty} P\left(V_{l} \leq t / \alpha\right)+(k-1) P\left(V_{k} \leq t / \alpha\right) \\
& =\sum_{l=k}^{\infty} F_{U}^{* l}(t / \alpha)+(k-1) F_{U}^{* k}(t / \alpha) \\
& \leq \sum_{l=k}^{\infty}\left(F_{U}(t / \alpha)\right)^{l}+(k-1)\left(F_{U}(t / \alpha)\right)^{k} \\
& =\frac{\left(F_{U}(t / \alpha)\right)^{k}}{1-F_{U}(t / \alpha)}+(k-1)\left(F_{U}(t / \alpha)\right)^{k}
\end{aligned}
$$

Since $F_{U}(t / \alpha) \rightarrow 1-e^{-t}$, as $j \rightarrow \infty$, it follows that for any sequence $F_{i j}, G_{i j}$ satisfying the conditions (4.79)-(4.82), $\left(N_{t / \alpha}^{\prime \prime}\right)$ is uniformly integrable. To see this, let $\epsilon$ be given such that $0<\epsilon<e^{-t}$. Then for $j \geq j_{0}$ (say) we have

$$
\sup _{j \geq j_{0}} E\left[N_{t / \alpha}^{\prime \prime} I\left(N_{t / \alpha}^{\prime \prime} \geq k\right)\right] \leq \frac{\left(1-e^{-t}+\epsilon\right)^{k}}{e^{-t}-\epsilon}+(k-1)\left(1-e^{-t}+\epsilon\right)^{k}
$$

Consequently,

$$
\lim _{k \rightarrow \infty} \sup _{j} E\left[N_{t / \alpha}^{\prime \prime} I\left(N_{t / \alpha}^{\prime \prime} \geq k\right)\right]=0
$$

i.e., $\left(N_{t / \alpha}^{\prime \prime}\right)$ is uniformly integrable, and the proof is complete.

Remark 4.44. The conditions (4.79)-(4.82) of Theorem 4.43 ensures the asymptotic Poisson distribution of $N_{t / \alpha}$, cf. Theorem 4.31, p. 136. Sufficient conditions for (4.79)-(4.82) are given in Theorem 4.27, p. 131.

# Asymptotic Normality 

We now study convergence to the normal distribution. The theorem below is "a time average result" - it is not required that the system is highly available. The result generalizes (4.32), p. 119.

Theorem 4.45. If $\mathbf{X}$ is a regenerative process with cycle length $S$ and associated downtime $Y=Y_{S}, \operatorname{Var}[S]<\infty$, and $\operatorname{Var}[Y]<\infty$, then as $t \rightarrow \infty$,$$
\sqrt{t}\left[\frac{Y_{t}}{t}-\bar{A}\right] \xrightarrow{D} \mathrm{~N}\left(0, \tau_{\Phi}^{2}\right)
$$

where

$$
\begin{aligned}
\tau_{\Phi}^{2} & =\frac{\operatorname{Var}[Y-\bar{A} S]}{E S} \\
\bar{A} & =\frac{E Y}{E S}
\end{aligned}
$$

Proof. The result (4.94) follows by applying the Central Limit Theorem for renewal reward processes, Theorem B.17, p. 280, in Appendix B.

In the case that the system is highly available, we have

$$
\tau_{\Phi}^{2} \approx \lambda_{\Phi} E Y_{1}^{2}
$$

where $Y_{1}$ is the downtime of the first system failure (note that $Y_{1}=Y_{11}$ ). The idea used to establish (4.97) is the following: As before, let $S$ be equal to the time of the first return to the best state $(1,1, \ldots, 1)$. Then (4.97) follows by using (4.95), (4.96), $\bar{A} \approx 0$, the fact that $Y \approx Y_{1}$ if a system failure occurs in the renewal cycle, the probability of two or more failures occurring in the renewal cycle is negligible, and $\lambda_{\Phi}=E N_{S} / E S$ (by the Renewal Reward Theorem, p. 280). We obtain

$$
\begin{aligned}
\tau_{\Phi}^{2} & =\frac{\operatorname{Var}[Y-\bar{A} S]}{E S}=\frac{E(Y-\bar{A} S)^{2}}{E S} \\
& \approx \frac{E Y^{2}}{E S}=\frac{E_{1} Y^{2} q}{E S} \approx \frac{E Y_{1}^{2} q}{E S} \\
& \approx E Y_{1}^{2} \frac{E N_{S}}{E S}=E Y_{1}^{2} \lambda_{\Phi}
\end{aligned}
$$

which gives (4.97).
More formally, it is possible to show that under certain conditions, the ratio $\tau_{\Phi}^{2} / \lambda_{\Phi} E Y_{1}^{2}$ converges to 1 , see [26].

# 4.7 Generalizations and Related Models 

### 4.7.1 Multistate Monotone Systems

We consider a multistate monotone system $\Phi$ as described in Sect. 2.1.2, p. 31, observed in a time interval $J$, with the following extensions of the model: We assume that there exists a reference level $D_{t}$ at time $t, t \in J$, which expresses a desirable level of system performance at time $t$. The reference level $D_{t}$ at time $t$ is a positive random variable, taking values in $\left\{d_{0}, d_{1}, \ldots, d_{r}\right\}$. For a flow network system we interpret $D_{t}$ as the demand rate at time $t$. In the followingwe will use the word "demand rate" also in the general case. The state of the system at time $t$, which we in the following refer to as the throughput rate, is assumed to be a function of the states of the components and the demand rate, i.e.,

$$
\Phi_{t}=\Phi\left(\mathbf{X}_{t}, D_{t}\right)
$$

If $D_{t}$ is a constant, we write $\Phi\left(\mathbf{X}_{t}\right)$. The process $\left(\Phi_{t}\right)$ takes values in $\left\{\Phi_{0}, \Phi_{1}, \ldots, \Phi_{M}\right\}$.

# Performance Measures 

The performance measures introduced in Sect.4.1, p. 105, can now be generalized to the above model.
(a) For a fixed time $t$ we define point availabilities

$$
\begin{gathered}
P\left(\Phi_{t} \geq \Phi_{k} \mid D_{t}=d\right) \\
E\left[\Phi_{t} \mid D_{t}=d\right] \\
P\left(\Phi_{t} \geq D_{t}\right)
\end{gathered}
$$

(b) Let $N_{J}$ be defined as the number of times the system state is below demand in $J$. The following performance measures related to $N_{J}$ are considered

$$
\begin{gathered}
P\left(N_{J} \leq k\right), k \in \mathbb{N}_{0} \\
E N_{J} \\
P\left(\Phi_{t} \geq D_{t}, \forall t \in J\right)=P\left(N_{J}=0\right)
\end{gathered}
$$

Some closely related measures are obtained by replacing $D_{t}$ by $\Phi_{k}$ and $N_{J}$ by $N_{J}^{k}$, where $N_{J}^{k}$ is equal to the number of times the process $\Phi$ is below state $\Phi_{k}$ during the interval $J$.
(c) Let

$$
\begin{aligned}
Y_{J} & =\int_{J}\left(D_{t}-\Phi_{t}\right) d t \\
& =\int_{J} D_{t} d t-\int_{J} \Phi_{t} d t
\end{aligned}
$$

We see that $Y_{J}$ represents the lost throughput(volume) in $J$, i.e., the difference between the accumulated demand (volume) and the actual throughput (volume) in $J$. The following performance measures related to $Y_{J}$ are considered$$
\begin{gathered}
P\left(Y_{J} \leq y\right), y \in \mathbb{R}_{+} \\
\frac{E Y_{J}}{|J|} \\
\frac{E \int_{J} \Phi_{t} d t}{E \int_{J} D_{t} d t}
\end{gathered}
$$

where $|J|$ denotes the length of the interval $J$. The measure (4.98) is called throughput availability.
(d) Let

$$
Z_{J}=\frac{1}{|J|} \int_{J} I\left(\Phi_{t} \geq D_{t}\right) d t
$$

The random variable $Z$ represents the portion of time the throughput rate equals (or exceeds) the demand rate. We consider the following performance measures related to $Z_{J}$

$$
\begin{gathered}
P\left(Z_{J} \leq y\right), y \in \mathbb{R}_{+} \\
E Z_{J}
\end{gathered}
$$

The measure $E Z_{J}$ is called demand availability.
As in the binary case we will often use in practice the limiting values of these performance measures.

The above performance measures are the most common measures used in reliability studies of offshore oil and gas production and transport systems, see, e.g., Aven [13]. In particular, the throughput availability is very much used when predicting the performance of various design options. For economic analysis and as a basis for decision-making, however, it is essential to be able to compute the total distribution of the throughput loss, and not only the mean. The measures related to the number of times the system is below a certain demand level is also useful, but more from an operational and safety point of view.

# Computation 

We now briefly look into the computation problem for some of the measures defined above. To simplify the analysis we shall make the following assumptions:

## Assumptions

1. $J=[0, u]$.
2. The demand rate $D_{t}$ equals the maximum throughput rate $\Phi_{M}$ for all $t$.3. The $n$ component processes $\left(X_{t}(i)\right)$ are independent. Furthermore, with probability one, the $n$ component processes $\left(X_{t}(i)\right)$ make no transitions ("jumps") at the same time.
4. The process $\left(X_{t}(i)\right)$ generates an alternating renewal process $T_{i 1}, R_{i 1}$, $T_{i 2}, R_{i 2}, \ldots$, as described in Sect.4.2, p. 106, where $T_{i m}$ represents the time spent in the state $x_{i M_{i}}$ during the $m$ th visit to this state, and $R_{i m}$ represents the time spent in the states $\left\{x_{i 0}, x_{i 1}, \ldots, x_{i, M_{i}-1}\right\}$ during the $m$ th visit to these states.
For all $i$ and $r$,

$$
a_{i r}=\lim _{t \rightarrow \infty} P\left(X_{t}(i)=x_{i r}\right)
$$

exist.
Arguing as in the binary case we can use results from regenerative and renewal reward processes to generalize the results obtained in the previous sections. To illustrate this, we formulate some of these extensions below. The proofs are omitted. We will focus here on the asymptotic results. Refer to Theorems 4.16, p. 120, and 4.19, p. 122, for the analogous results in the binary case. We need the following notation:

$$
\begin{aligned}
\mu_{i} & =E T_{i m}+E R_{i m} \\
N_{t} & =N_{[0, t]}^{k}(k \text { is fixed }) \\
p_{i r}(t) & =P\left(X_{t}(i)=x_{i r}\right) ; \text { if } t \text { is fixed, we write } p_{i r} \text { and } X(i) \\
\mathbf{p} & =\left(p_{10}, \ldots, p_{n M_{n}}\right) \\
\mathbf{a} & =\left(a_{10}, \ldots, a_{n M_{n}}\right) \\
\Phi_{k}(\mathbf{X}) & =I\left(\Phi(\mathbf{X}) \geq \Phi_{k}\right) \\
h_{k}(\mathbf{p}) & =E \Phi_{k}(\mathbf{X}) \\
h(\mathbf{p}) & =E \Phi(\mathbf{X}) \\
\left(1_{i r}, \mathbf{p}\right) & =\mathbf{p} \text { with } p_{i r} \text { replaced by } 1 \text { and } p_{i l}=0 \text { for } l \neq r
\end{aligned}
$$

We see that $\mu_{i}$ is equal to the expected cycle length for component $i, N_{t}$ represents the number of times the process $\Phi$ is below state $\Phi_{k}$ during the interval $[0, t]$, and $\Phi_{k}(\mathbf{X})$ equals 1 if the system is in state $\Phi_{k}$ or better, and 0 otherwise.

Theorem 4.46. The limiting availabilities are given by

$$
\begin{aligned}
\lim _{t \rightarrow \infty} E \Phi\left(\mathbf{X}_{t}\right) & =h(\mathbf{a}) \\
\lim _{t \rightarrow \infty} P\left(\Phi\left(\mathbf{X}_{t}\right) \geq \Phi_{k}\right) & =h_{k}(\mathbf{a})
\end{aligned}
$$

Theorem 4.47. Let

$$
\gamma_{i l r}=h_{k}\left(1_{i l}, \mathbf{a}\right)-h_{k}\left(1_{i r}, \mathbf{a}\right)
$$and let $f_{i l r}$ denote the expected number of times component $i$ makes a transition from state $x_{i l}$ to state $x_{i r}$ during a cycle of component $i$. Assume $f_{i l r}<\infty$. Then the expected number of times the system state is below $\Phi_{k}$ per unit of time in the long run equals

$$
\lim _{u \rightarrow \infty} \frac{E N_{u}}{u}=\lim _{u \rightarrow \infty} \frac{E\left[N_{u+s}-N_{u}\right]}{s}=\sum_{i=1}^{n} \sum_{r<l} \frac{f_{i l r} \gamma_{i l r}}{\mu_{i}}
$$

If $\mathbf{X}$ is a regenerative process having finite expected cycle length, then with probability one,

$$
\lim _{u \rightarrow \infty} \frac{N_{u}}{u}=\sum_{i=1}^{n} \sum_{r<l} \frac{f_{i l r} \gamma_{i l r}}{\mu_{i}}
$$

The limit (4.99) is denoted $\lambda_{\Phi}$. If the random variables $T_{i m}$ are exponentially distributed, then $\mathbf{X}$ is regenerative, cf. Theorem 4.23, p. 124.

It is also possible to extend the asymptotic results related to the distribution of the number of system failures at level $k$, and the distribution of the lost volume (downtime). We can view the system as a binary system of binary components, and the asymptotic results of Sects. 4.4-4.6 apply.

# Gas Compression System 

Consider the gas compression system example in Sect.1.3.2, p. 13. Two design alternatives were studied:
(i) One gas train with a maximum throughput capacity of $100 \%$.
(ii) Two trains in parallel, each with a maximum throughput capacity of $50 \%$.

Normal production is $100 \%$. Each train comprises compressor-turbine, cooler and scrubber. To analyze the performance of the system it was considered sufficient to use approximate methods developed for highly available systems, as presented in this chapter. In the system analysis, each train was treated as one component, having exponential lifetime distribution with a failure rate of 13 per year, and mean repair time equal to

$$
(10 / 13) \cdot 12+(2 / 13) \cdot 50+(1 / 13) \cdot 20 \approx 18.5(\mathrm{~h})
$$

From this we find that the asymptotic unavailability $\bar{A}$, given by formula (4.2), p. 109, for a train equals 0.027 , assuming $8,760 \mathrm{~h}$ per year. The number of system failures per unit of time is given by the system failure rate $\lambda_{\Phi}$. For alternative (i) there is only one failure level and $\lambda_{\Phi}=13$. For alternative (ii) we must distinguish between failures resulting in production below $100 \%$ and below $50 \%$. The system in these two cases can be viewed as a series system of the two trains and a parallel system of the two trains, respectively. Hence the system failure rate for these levels is approximately equal to 26 and 0.7 , respectively. Note that for the latter case (cf. (4.64), p. 140),$$
\lambda_{\Phi} \approx 2 \cdot \bar{A} \cdot 13
$$

Using that the number of system failures is approximately Poisson distributed, we can compute the probability that a certain number of failures occurs during a specific period of time. For example, we find that for alternative (ii) there is a probability of about $e^{-0.7}=0.50$ of having no complete shutdowns during a year.

Let $E Y$ denote the asymptotic mean lost production relative to the demand. For alternative (i) it is clear that $E Y$ equals 0.027 , observing that a failure results in $100 \%$ loss and the unavailability equals 0.027 . For alternative (ii), we obtain the same value for the asymptotic mean lost production, as is seen from the following calculation

$$
E Y=0.5 \cdot 2 \cdot 0.027 \cdot 0.973+1 \cdot 0.027^{2}=0.027
$$

The first term in the sum represents the contribution from failures leading to $50 \%$ loss, whereas the second term represents the contribution from failures leading to $100 \%$ loss. The latter contribution is in practice negligible compared to the former one. To compute the distribution of the lost production, we need to know more about the distribution of the repair time $R$ of the train. It was assumed in this application that $E R^{2}=1,000$, which corresponds to a squared coefficient of variation equal to 1.9 and a standard deviation equal to 25.7 . The unit of time is hours. This assumption makes it possible to approximate the distribution of the lost production during a year, using the normal approximation. We know the mean $(E Y=0.027)$ and need to estimate the variance of $Y$. To do this we make use of (4.97), p. 158, stating that the variance in the binary case is approximately equal to $\lambda_{\Phi} E Y_{1}^{2} / t$, where $t$ is the length of the time period considered and $Y_{1}$ is the downtime of the first system failure. For alternative (i) we find that the variance equals approximately

$$
(13 / 8760) \cdot 1000 / 8760=1.7 \cdot 10^{-4}
$$

and for alternative (ii) (we ignore situations with both components down so that the lost production is approximately $50 \%$ of the downtime)

$$
(50 / 100)^{2} \cdot(26 / 8760) \cdot 1000 / 8760=0.85 \cdot 10^{-4}
$$

From this we estimate, for example, that the probability that the lost production during 1 year is more than $4 \%$ of demand, to be 0.16 for alternative (i) and 0.08 for alternative (ii).

# Special Case: Phase-Type Distributions 

In the asymptotic analysis in Sects. 4.4-4.6 main emphasis has been placed on the situation that the lifetimes are exponentially distributed. Using the so-called phase-type approach, we can show that the multistate model alsoprovides a framework for covering other types of distributions. The phase-type approach makes use of the fact that a distribution function can be approximated by a mixture of Erlang distributions (with the same scale parameter), cf., e.g., Asmussen [8] and Tijms [156]. It is common to use a mixture of two Erlang distributions with the first two moments matching the distribution considered. Now assume that the lifetime of component $i, F_{i}$, can be described by the sum of $M_{i}$ random variables, each of which is exponentially distributed with rate $\lambda_{i 0}$, i.e., the lifetime of component $i$ is Erlangian distributed with parameters $\lambda_{i 0}$ and $M_{i}$. Then we have a situation that fits into the above multistate framework and the asymptotic results can be applied. The state space for component $i$ is $\left\{0,1, \ldots, M_{i}\right\}$. The component process $\left(X_{t}(i)\right)$ starts in state $M_{i}$, it stays there a time governed by an exponential random variable with rate $\lambda_{i 0}$ and jumps to state $M_{i}-1$, it stays there a time governed by an exponential random variable with rate $\lambda_{i 0}$ and jumps to state $M_{i}-2$, and this continues until the process reaches state 0 . After a duration having distribution $G_{i}$ in state 0 it returns to state $M_{i}$. We see that $f_{i l r}=1$ if $l=r+1$ and $f_{i l r}=0$ otherwise (for $r<l$ ). Furthermore,

$$
\begin{aligned}
\mu_{i} & =M_{i} \frac{1}{\lambda_{i 0}}+\mu_{G_{i}}=\mu_{F_{i}}+\mu_{G_{i}} \\
\lambda_{\Phi} & =\sum_{i=1}^{n}\left[h_{1}\left(1_{i 1}, \mathbf{a}\right)-h_{1}\left(1_{i 0}, \mathbf{a}\right)\right] \frac{1}{\mu_{i}}=\sum_{i=1}^{n}\left[h\left(1_{i}, \mathbf{A}\right)-h\left(0_{i}, \mathbf{A}\right)\right] \frac{1}{\mu_{i}} \\
a_{i 0} & =\frac{\mu_{G_{i}}}{\mu_{i}}=\bar{A}_{i}
\end{aligned}
$$

using the terminology from the binary theory. Remember that the formulas established in Sects. 4.2 and 4.3 for the expected cycle length and the steady-state (un)availability of component $i$, and the system failure rate, are applicable also for nonexponential distributions.

Thus by modifying the state space, we have been able to extend the results, i.e., the Theorems 4.25 (p. 129), 4.31 (p. 136), and 4.43 (p. 154), in the previous sections to Erlang distributions.

Now assume that the lifetime distribution of component $i$ is a mixture of Erlang distributions, i.e., with probability $p_{i r}>0$ the distribution equals an Erlang distribution with parameters $\lambda_{i 0}$ and $M_{i r}, r=1,2, \ldots, r_{i}$. This situation can be analyzed as above with the state space for component $i$ given by $\left\{0,1, \ldots, M_{i}\right\}$, where $M_{i}=\max _{r}\left\{M_{i r}\right\}$. If the component state process $\left(X_{t}(i)\right)$ is in state 0 , it will go to state $M_{i r}$ with probability $p_{i r}$. Then the component stays in this state for a time governed by an exponential distribution with parameter $\lambda_{i 0}$, before it jumps to state $M_{i r}-1$, etc. As above we can use the formulas for the binary case to compute the expected cycle length and steady-state (un)availability of component $i$, and the system failure rate. It is seen that

$$
\mu_{F_{i}}=\sum_{r=1}^{r_{i}} p_{i r} M_{i r} \frac{1}{\lambda_{i 0}}
$$We can conclude that the set-up also covers mixtures of Erlang distributions, and Theorems $4.25,4.31$, and 4.43 apply.

Note that we have not proved that the limiting results obtained in the previous sections hold true for general lifetime distributions $F_{i j}$. We have shown that if the distributions $F_{i j}$ all belong to a certain class of mixtures of Erlang distributions, then the results hold. Starting from general distributions $F_{i j}$, we can write $F_{i j}$ as a limit of $F_{i j r}, r \rightarrow \infty$, where $F_{i j r}$ are mixtures of Erlang distributions. But interchanging the limits as $j \rightarrow \infty$ and as $r \rightarrow \infty$ is not justified in general. Refer also to Bibliographic Notes, p. 173, for some comments related to the non-exponential case.

# 4.7.2 Parallel System with Repair Constraints 

Consider the model as described in Sect.4.3, p. 120, but assume now that there are repair constraints, i.e., a maximum of $r(r<n)$ components can be repaired at the same time. Hence if $i, i>r$, components are down, the remaining $i-r$ components are waiting in a repair queue. We shall restrict attention to the case $r=1$, i.e., there is only one repair facility (channel) available. The repair policy is first come first served. We assume exponentially distributed lifetimes.

Consider first a parallel system of two components, and the set-up of Sect.4.4, p. 126. It is not difficult to see that $E T_{\Phi}, q$, and $E_{0} S$ are identical to the corresponding quantities when there are no repair constraints; see section on parallel system of two identical components p. 139. We can also find explicit expressions for $E S$ and $\lambda_{\Phi}$. Since the time to the first component failure is exponentially distributed with parameter $2 \lambda, E S=1 / 2 \lambda+E S^{\prime \prime}$, where $S^{\prime \prime}$ equals the time from the first component failure until the process again returns to $(1,1)$. Denoting the repair time of the failed component by $R$, we see that

$$
E S^{\prime \prime}=\mu_{G}+q E\left[S^{\prime \prime}-R \mid N_{S} \geq 1\right]
$$

But $E\left[S^{\prime \prime}-R \mid N_{S} \geq 1\right]=E S^{\prime \prime}$, and it follows that

$$
E S=\frac{1}{2 \lambda}+\frac{\mu_{G}}{1-q}
$$

Hence

$$
\begin{aligned}
\lambda_{\Phi} & =\frac{E N_{S}}{E S}=\frac{q /(1-q)}{E S} \\
& =\frac{2 \lambda q}{1-q+2 \lambda \mu_{G}}
\end{aligned}
$$

Alternatively, and easier, we could have found $\lambda_{\Phi}$ by defining a cycle $S$ as the time between two consecutive visits to a state with just one component functioning. Then it is seen that $E S=\mu_{G}+(1-q) / 2 \lambda$ and $E N_{S}=q$, resulting in the same $\lambda_{\Phi}$ as above.Now suppose we have $n \geq 2$, and let $\Phi_{t}$ be defined as the number of components functioning at time $t$. To analyze the system, we can utilize that the state process $\Phi_{t}$ is a semi-Markov process with jump times at the completion of repairs. In state $0,1, \ldots, n-1$ the time between transitions has distribution $G(t)$ and the transition probability $P_{i j}$ is given by

$$
P_{i j}= \begin{cases}\int_{0}^{\infty}\binom{i}{i-j+1} F(s)^{i-j+1}(1-F(s))^{j-1} d G(s), & \\ & 1 \leq j \leq i \leq n-1 \\ \int_{0}^{\infty}(1-F(s))^{i} d G(s), & j=i+1 \\ 0, & 1 \leq i<j-1\end{cases}
$$

observing that if the state is $i$ and the repair is completed at time $s$, then the probability that the process jumps to state $j$, where $j \leq i \leq n-1$, equals the probability that $i-j+1$ components fail before $s$ and $j-1$ components survive $s$; and, furthermore, if the state is $i$ and the repair is completed at time $s$, then the probability that the process jumps to state $i+1$ equals the probability that $i$ components survive $s$. Now if the process is in state $n$, it stays there for an exponential time with rate $n \lambda$, and jumps to state $n-1$.

Having established the transition probabilities, we can compute a number of interesting performance measures for the system using results from semiMarkov theory. For example, we have an explicit formula for the asymptotic probability that $P\left(\Phi_{t}=k\right)$ as $t \rightarrow \infty$, which depends on the mean time spent in each state and the limiting probabilities of the embedded discrete-time Markov chain; see Ross [135], p. 104.

# 4.7.3 Standby Systems 

In this section we study the performance of standby systems comprising $n$ identical components of which $n-1$ are normally operating and one is in (cold) standby. Emphasis is placed on the case that the components have constant failure rates, and the mean repair time is relatively small compared to the MTTF.

Standby systems as analyzed here are used in many situations in real life. As an example we return to the gas compression system in Sect. 1.3, p. 13 and Sect.4.7.1, p. 162. To increase the availability for the alternatives considered, we may add a standby train such that when a failure of a train occurs, the standby train can be put into operation and a production loss is avoided.

## Model

The following assumptions are made:

- Normally $n-1$ components are running and one is in standby.- Failed components are repaired. The repair regime is characterized by R1 Only one component can be repaired at a time (one repair facility/channel), the repair policy is "first come first served," or
R2 Up to $n$ repairs can be carried out at a time ( $n$ repair facilities/channels).
- Switchover to the standby component is perfect, i.e., instantaneous and failure-free.
- A standby component that has completed its repair is functioning at demand, i.e., the failure rate is zero in the standby state.
- All failure times and repair times are independent with probability distributions $F(t)$ and $G(t)$, respectively. $F$ is absolutely continuous and has finite mean, and $G$ has finite third-order moment. We assume

$$
\int_{0}^{\infty} F(t) d G(t)>0
$$

In the following $T$ refers to a failure time of a component and $R$ refers to a repair time.
The squared coefficient of variation of the repair time distribution is denoted $c_{G}^{2}$.
Let $\Phi_{t}$ denote the state of the system at time $t$, i.e., the number of components functioning at time $t\left(\Phi_{t} \in\{n, n-1, \ldots, 0\}\right)$. For repair regime R1, $\Phi$ is generally a regenerative process, or a modified regenerative process. For a two-component system it is seen that the time points when $\Phi$ jumps to state 1 are regenerative points, i.e., the time points when (i) the operating component fails and the second component is not under repair (the process jumps from state 2 to 1 ) or (ii) both components are failed and the repair of the component being repaired is completed (the process jumps from state 0 to 1 ). For $n>2$, the points in time when the process jumps from state 0 to 1 are regenerative points, noting that the situation then is characterized by one "new" component, and $n-1$ in a repair queue. Assuming exponential lifetimes, we can define other regenerative points, e.g., consecutive visits to the best state $n$, or consecutive visits to state $n-1$.

Also for a two-component system under repair regime R2, the process generally generates a (modified) regenerative process. The regenerative points are given by the points when the process jumps from state 2 to 1 (case (i) above). If the system has more than two components $(n>2)$, the regenerative property is not true for a general failure time distribution. However, under the assumption of an exponential time to failure, the process is regenerative. Regenerative points are given by consecutive visits to state $n$, or points when the process jumps from state $n$ to state $n-1$. In the following, when considering a system of more than two components, we assume an exponential lifetime distribution. Remember that a cycle refers to the length between two consecutive regenerative points.# Performance Measures 

The system can be considered as a special case of a multistate monotone system, with the demand rate $D_{t}$ set to $n-1$. Hence the performance measures defined in Sect.4.7.1, p. 158, also apply to the system analyzed in this section. Availability refers to the probability that at least $n-1$ components are functioning, and system failure refers to the event that the state process $\Phi$ is below $n-1$. Note that we cannot apply the computation results of Sect.4.7.1 since the state processes of the components are not stochastically independent. The general asymptotic results obtained in Sects. 4.4-4.6 for regenerative processes are however applicable.

Of the performance measures we will put emphasis on the limiting availability, and the limiting mean of the number of system failures in a time interval.

We need the following notation for $i=n, n-1, \ldots, 0$ :

$$
\begin{aligned}
p_{i}(t) & =P\left(\Phi_{t}=i\right) \\
p_{i} & =\lim _{t \rightarrow \infty} p_{i}(t)
\end{aligned}
$$

provided the limits exist. Clearly, the availability at time $t, A(t)$, is given by

$$
A(t)=p_{n}(t)+p_{n-1}(t)
$$

and the limiting availability, $A$, is given by

$$
A=p_{n}+p_{n-1}
$$

## Computation

First, we focus on the limiting unavailability $\bar{A}$, i.e., the expected portion of time in the long run that at least two components are not functioning. Under the assumption of constant failure and repair rates this unavailability can easily be computed using Markov theory, noting that $\Phi$ is a birth and death process. The probability $\tilde{p}_{i}$ of having $i$ components down is given by (cf. [13], p. 303)

$$
\tilde{p}_{i}=p_{n-i}=\frac{z_{i}}{1+\sum_{j=1}^{n} z_{j}}
$$

where

$$
\begin{aligned}
z_{i} & =\left\{\begin{array}{ll}
\frac{(n-1)(n-1)!}{(n-i)!} \frac{1}{\prod_{l=1}^{i} u_{l}} \delta^{i} & i=1,2, \ldots, n \\
1 & i=0
\end{array}\right. \\
\delta & =\mu_{G} / \mu_{F}
\end{aligned}
$$

$u_{l}=1$ under repair regime R 1 and $l$ under repair regime R 2 .
Note that if $\delta$ is small, then $\tilde{p}_{i} \approx z_{i}$ for $i \geq 1$. Hence

$$
\bar{A} \approx \tilde{p}_{2} \approx \frac{(n-1)^{2}}{u_{2}} \delta^{2}
$$We can also write

$$
\bar{A}=\frac{(n-1)^{2}}{u_{2}} \delta^{2}+o\left(\delta^{2}\right), \quad \delta \rightarrow 0
$$

In general we can find expressions for the limiting unavailability by using the regenerative property of the process $\Phi$. Defining $Y$ and $S$ as the system downtime in a cycle and the length of a cycle, respectively, it follows from the Renewal Reward Theorem (Theorem B.15, p. 280, in Appendix B) that

$$
\bar{A}=\frac{E Y}{E S}
$$

Here system downtime corresponds to the time two or more of the components are not functioning. Let us now look closer into the problem of computing $\bar{A}$, given by (4.102), under repair regime R1.

Repair Regime R1. In general, semi-Markov theory can be used to establish formulas for the unavailability, cf. [27]. In practice, we usually have $\mu_{G}$ relatively small compared to $\mu_{F}$. Typically, $\delta=\mu_{G} / \mu_{F}$ is less than 0.1 . In this case we can establish simple approximation formulas as shown below.

First we consider the case with two components, i.e., $n=2$. The regenerative points for the process $\Phi$ are generated by the jumps from state 2 to 1 . In view of (4.102) the limiting system unavailability $\bar{A}$ can be written as

$$
\begin{aligned}
\bar{A} & =\frac{E[\max \{R-T, 0\}]}{E T+E[\max \{R-T, 0\}]} \\
& =\frac{\left(\mu_{G}-w\right)}{\mu_{F}+\left(\mu_{G}-w\right)}
\end{aligned}
$$

where

$$
w=E[\min \{R, T\}]=\int_{0}^{\infty} \bar{F}(t) \bar{G}(t) d t
$$

noting that $\max \{R-T, 0\}=R-\min \{R, T\}$ and the system downtime equals 0 if the repair of the failed component is completed before the failure of the operating component, and equals the difference between the repair time of the failed component and the time to failure of the operating component if this difference is positive. Thus we have proved the following theorem.

Theorem 4.48. If $n=2$, then the unavailability $\bar{A}$ is given by (4.104).
We now assume an exponential failure time distribution $F(t)=1-e^{-\lambda t}$. Then we have

$$
\bar{A} \approx \bar{A}^{\prime}
$$where

$$
\bar{A}^{\prime}=\frac{\lambda^{2}}{2} E R^{2}=\frac{\delta^{2}}{2}\left[1+c_{G}^{2}\right]
$$

This gives a simple approximation formula for computing $\bar{A}$. The approximation (4.105) is established formally by the following proposition.

Proposition 4.49. If $n=2$ and $F(t)=1-e^{-\lambda t}$, then

$$
0 \leq \bar{A}^{\prime}-\bar{A} \leq\left(\bar{A}^{\prime}\right)^{2}+\frac{\delta^{3}}{6} \frac{E R^{3}}{\mu_{G}^{3}}
$$

Proof. Using that $1-e^{-\lambda t} \leq \lambda t$ and changing the order of integration, it follows that

$$
\begin{aligned}
\bar{A} & =\frac{\lambda\left(\mu_{G}-w\right)}{1+\lambda\left(\mu_{G}-w\right)} \leq \lambda\left(\mu_{G}-w\right) \\
& =\lambda \int_{0}^{\infty} F(t) \bar{G}(t) d t \\
& \leq \lambda \int_{0}^{\infty}(\lambda t) \bar{G}(t) d t \\
& =\lambda^{2} \frac{1}{2} E R^{2}=\bar{A}^{\prime}
\end{aligned}
$$

It remains to show the right-hand inequality of (4.107). Considering

$$
\begin{aligned}
\bar{A}\left(1+\lambda\left(\mu_{G}-w\right)\right) & =\lambda \int_{0}^{\infty} F(t) \bar{G}(t) d t \\
& \geq \lambda \int_{0}^{\infty}\left(\lambda t-\frac{1}{2}(\lambda t)^{2}\right) \bar{G}(t) d t \\
& =\bar{A}^{\prime}-\frac{1}{6} \lambda^{3} E R^{3}
\end{aligned}
$$

and the inequalities $\bar{A} \leq \lambda\left(\mu_{G}-w\right) \leq \bar{A}^{\prime}$ obtained above, it is not difficult to see that

$$
0 \leq \bar{A}^{\prime}-\bar{A} \leq \bar{A} \lambda\left(\mu_{G}-w\right)+\frac{1}{6} \lambda^{3} E R^{3} \leq\left(\bar{A}^{\prime}\right)^{2}+\frac{1}{6} \lambda^{3} E R^{3}
$$

which completes the proof.
Hence $\bar{A}^{\prime}$ overestimates the unavailability and the error term will be negligible provided that $\delta=\mu_{G} / \mu_{F}$ is sufficiently small.

Next, let us compare the approximation formula $\bar{A}^{\prime}$ with the standard "Markov formula" $\bar{A}^{M}=\delta^{2}$, obtained by assuming exponentially distributed failure and repair times (replace $c_{G}^{2}$ by 1 in the expression (4.106) for $\bar{A}^{\prime}$, or use the Markov formula (4.101), p. 168). It follows that$$
\bar{A}^{\prime}=\bar{A}^{M} \cdot \frac{1}{2}\left[1+c_{G}^{2}\right]
$$

From this, we see that the use of the Markov formula when the squared coefficient of variation of the repair time distribution, $c_{G}^{2}$, is not close to 1 , will introduce a relatively large error. If the repair time is a constant, then $c_{G}^{2}=0$ and the unavailability using the Markov formula is two times $\bar{A}^{\prime}$. If $c_{G}^{2}$ is large, say 2 , then the unavailability using the Markov formula is $2 / 3$ of $\bar{A}^{\prime}$.

Assume now $n>2$. The repair regime is R1 as before. Assume that $\delta$ is relatively small. Then it is possible to generalize the approximations obtained above for $n=2$.

Since $\delta$ is small, there will be a negligible probability of having $\Phi \leq n-3$, i.e., three or more components not functioning at the same time. By neglecting this possibility we obtain a simplified process that is identical to the process for the two-component system analyzed above, with failure rate $(n-1) \lambda$. Hence by replacing $\lambda$ with $(n-1) \lambda$, formula (4.105) is valid for general $n$, i.e., $\bar{A} \approx \bar{A}^{\prime}$, where

$$
\bar{A}^{\prime}=\frac{[(n-1) \delta]^{2}}{2}\left[1+c_{G}^{2}\right]
$$

The error bounds are, however, more difficult to obtain, see [27].
The relation between the approximation formulas $\bar{A}^{\prime}$ and $\bar{A}^{M}$, given by (4.101), p. 168, are the same for all $n \geq 2$. Hence $\bar{A}^{\prime}=\bar{A}^{M} \cdot \frac{1}{2}\left[1+c_{G}^{2}\right]$ (formula (4.110)) holds for $n>2$ too.

Next we will establish results for the long run average number of system failures. It follows from the Renewal Reward Theorem that $E N_{t} / t$ and $E\left[N_{t+s}-N_{t}\right] / s$ converge to $\lambda_{\Phi}=E N / E S$ as $t \rightarrow \infty$, where $N$ equals the number of system failures in one renewal cycle and $S$ equals the length of the cycle as before. With probability one, $N_{t} / t$ converges to the same value. Under repair regime R1, $N \in\{0,1\}$. Hence $E N$ equals the probability that the system fails in a cycle, i.e., $E N=q$ using the terminology of Sects. 4.3 and 4.4. Below we find expressions for $\lambda_{\Phi}$ in the case that the repair regime is R1. The regenerative points are consecutive visits to state $n-1$.

Theorem 4.50. If $n=2$, then

$$
\lambda_{\Phi}=\frac{q}{\mu_{F}+E Y}
$$

where

$$
\begin{aligned}
q & =\int_{0}^{\infty} F(t) d G(t) \\
E Y & =\int_{0}^{\infty} F(t) \bar{G}(t) d t
\end{aligned}
$$

Proof. First note that $E Y$ equals the expected downtime in a cycle and is given by$$
E Y=E[(R-T) I(T<R)]=E[R-\min \{R, T\}]
$$

cf. (4.103)-(4.104), p. 169. We have established above that

$$
\lambda_{\Phi}=\frac{E N}{E S}=\frac{q}{E S}
$$

where $N$ equals the number of system failures in one renewal cycle, $S$ equals the length of the cycle, and $q=P(T \leq R)$ equals the probability of having a system failure during a cycle. Thus it remains to show that

$$
E S=\mu_{F}+E Y
$$

Suppose the system has just jumped to state 1 . We then have one component operating and one undergoing repair. Now if a system failure occurs (i.e., $T \leq R$ ), then the cycle length equals $R$, and if a system failure does not occur (i.e., $T>R$ ), then the cycle length equals $T$. Consequently,

$$
S=I(T \leq R) R+I(T>R) T=T+(R-T) I(T<R)
$$

Formula (4.113) follows and the proof is complete.
We see from (4.111) that if $F(t)$ is exponential with rate $\lambda$ and the components are highly available, then

$$
\lambda_{\Phi} \approx \lambda^{2} \mu_{G}
$$

If $n>2$ and the repair regime is R 1 , it is not difficult to see that $q$ is given by (4.112) with $F(t)$ replaced by $1-e^{-(n-1) \lambda t}$. It is however more difficult to find an expression for $E S$. For highly available components, we can approximate the system with a two-state system with failure rate $(n-1) \lambda$; hence,

$$
\begin{aligned}
\lambda_{\Phi} & \approx[(n-1) \lambda]^{2} \mu_{G} \\
E S & \approx \frac{1}{(n-1) \lambda}
\end{aligned}
$$

When the state process of the system jumps from state $n$ to $n-1$, it will return to state $n$ with a high probability and the sojourn time in state $n-1$ will be relatively short; consequently, the expected cycle length is approximately equal to the expected time in the best state $n$, i.e., $1 /(n-1) \lambda$.

Repair Regime R2. Finally in this section we briefly comment on the repair regime R2. We assume constant failure rates. It can be argued that if there is ample repair facilities, i.e., the repair regime is R2, the steady-state unavailability is invariant with respect to the repair time distribution, cf., e.g., Smith [145] and Tijms [156], p. 175. This means that we can use the steady-state Markov formula (4.100), p. 168, also when the repair time distribution is notexponential. The result only depends on the repair time distribution through its mean value. However, a strict mathematical proof of this invariance result does not seem to have been presented yet.

Bibliographic Notes. Alternating renewal processes are studied in many textbooks, e.g., Birolini [44] and Ross [135]. Different versions of the onecomponent downtime distribution formula in Theorem 4.14 (p. 118) have been formulated and proved in the literature, cf. [44, 45, 57, 65, 69, 154]. The first version was established by Takács. Theorem 4.14, which is taken from Haukås and Aven [82], seems to be the most general formulation and also has the simplest proof.

Some key references to the theory of point availability of monotone systems and the mean number of system failures are Barlow and Proschan [31, 32] and Ross [136]; see also Aven [13]. Parallel systems of two identical components have been studied by a number of researchers, see, e.g., [34, 73, 76]. Gaver [73] established formulas for the distribution and mean of the time to the first system failure, identical to those presented in Sect. 4.4, p. 139. Our derivation of these formulas is different however from Gaver's.

Asymptotic analysis of highly available systems has been carried out by a number of researchers. A survey is given by Gertsbakh [75], with emphasis on results related to the convergence of the distribution of the first system failure to the exponential distribution. See also the books by Gnedenko and Ushakov [76], Ushakov [157], and Kovalenko et al. [110, 111]. Some of the earliest results go back to work done by Keilson [104] and Solovyev [148]. A result similar to Lemma 4.24 (p. 127) was first proved by Keilson [104]; see also $[76,105,109]$. Our version of this lemma is taken from Aven and Jensen [26]. To establish the asymptotic exponential distribution, different normalizing factors are used, e.g., $q / E_{0} S$, where $q$ equals the probability of having at least one system failure in a renewal cycle and $E_{0} S$ equals the expected cycle length given that no system failures occur in the cycle. This factor, as well as the other factors considered in the early literature in this field (cf., e.g., the references $[75,76,157])$ are generally difficult to compute. The asymptotic failure rate of the system, $\lambda_{\phi}$, is more attractive from a computational point of view, and is given most attention in this presentation. We find it somewhat difficult to read some of the earlier literature on availability. A large part of the research in this field has been developed outside the framework of monotone system theory. Using this framework it is possible to give a unified presentation of the results. Our set-up and results (Sect.4.4) are to a large extent taken from the recent papers by Aven and Haukås [22] and Aven and Jensen [26]. These papers also cover convergence of the number of system failures to the Poisson distribution.

The literature includes a number of results proving that the exponential/Poisson distribution is the asymptotic limit of certain sums of point processes. Most of these results are related to the thinning of independent processes, see e.g., Çinlar [55], Daley and Vere-Jones [58], and Kovalenko etal. [111]. See also Lam and Lehoczky [114] and the references therein. These results are not applicable for the availability problems studied in this book.

Sections 4.5 and 4.6 are to a large extent based on Gåsemyr and Aven [72], Aven and Haukås [23], and Aven and Jensen [26]. Gåsemyr and Aven [72] and Aven and Haukås [23] study the asymptotic downtime distribution given system failure. Theorem 4.42 is due to Haukås (see [26, 81]) and Smith [146]. Aven and Jensen [26] gives sufficient conditions for when a compound Poisson distribution is an asymptotic limit for the distribution of the downtime of a monotone system observed in a time interval. An alternative approach for establishing the compound Poisson process limit is given by Serfozo [138]. There exist several asymptotic results in the literature linking the sums of independent point processes with integer marks to the compound Poisson process; see, e.g., [153]. It is, however, not possible to use these results for studying the asymptotic downtime distributions of monotone systems.

Section 4.7.1 generalizes results obtained in the previous sections to multistate systems. The presentation on multistate systems is based on Aven $[11,14]$. For the analysis in Sect.4.7.3 on standby systems, reference is given to the work by Aven and Opdal [27].

In this chapter we have primarily focused on the situation that the component lifetime distributions are exponential. In Sect.4.7.1 we outlined how some of the results can be extended to phase-type distributions. A detailed analysis of the nonexponential case (nonregenerative case) is however outside the scope of this book. Further research is needed to present formally proved results for the general case. Presently, the literature covers only some particular cases. Intuitively, it seems clear that it is possible to generalize many of the results obtained in this chapter. Consider, for example, the convergence to the Poisson process for the number of system failures. As long as the components are highly available, we would expect that the number of failures are approximately Poisson distributed. But formal asymptotic results are rather difficult to establish; see, for example, [102, 106, 112, 152, 162]. Strict conditions have to be imposed to establish the results, to the system structure and the component lifetime and downtime distributions. Also the general approach of showing that the compensator of the counting process converges in probability (see Daley and Vere-Jones [58], p. 552), is difficult to apply in our setting.

Of course, this chapter covers only a small number of availability models compared to the large number of models presented in the literature. We have, for example, not included models where some components remain in "suspended animation" while a component is being repaired/replaced, and models allowing preventive maintenance. For such models, and other related models, refer to the above cited references, Beichelt and Franken [36], Osaki [128], Srinivasan and Subramanian [150], Van Heijden and Schornagel [160], and Yearout et. al. [166]. See also the survey paper by Smith et al. [147].# Maintenance Optimization 

In this chapter we combine the general lifetime model of Chap. 3 with maintenance actions like repairs and replacements. Given a certain cost and reward structure an optimal repair and replacement strategy will be derived. We begin with some basic and well-known models and come then to more complex ones, which show how the general approach can be exploited to open a variety of different optimization models.

### 5.1 Basic Replacement Models

First of all we consider some basic models that are simple in both the lifetime modeling and the optimization criterion. These basic models include the age and the block replacement models that are widely used and thoroughly investigated. A technical system is considered, the lifetime of which is described by a positive random variable $T$ with distribution $F$. Upon failure the system is immediately replaced by an equivalent one and the process repeats itself. A preventive replacement can be carried out before failure. Each replacement incurs a cost of $c>0$ and each failure adds a penalty cost $k>0$.

### 5.1.1 Age Replacement Policy

For this policy a replacement age $s, s>0$, is fixed for each system at which a preventive replacement takes place. If $T_{i}, i=1,2, \ldots$, are the successive lifetimes of the systems, then $\tau_{i}=T_{i} \wedge s$ denotes the operating time of the $i$ th system and equals the $i$ th cycle length. The random variables $T_{i}$ are assumed to form an i.i.d. sequence with common distribution $F$, i.e., $F(t)=P\left(T_{i} \leq t\right)$. The costs for one cycle are described by the stochastic process $Z=\left(Z_{t}\right), t \in$ $\mathbb{R}_{+}, Z_{t}=c+k I(T \leq t)$. Clearly, the average cost after $n$ cycles is$$
\frac{\sum_{i=1}^{n} Z_{\tau_{i}}}{\sum_{i=1}^{n} \tau_{i}}
$$

and the total cost per unit time up to time $t$ is given by

$$
C_{t}=\frac{1}{t} \sum_{i=1}^{N_{t}} Z_{\tau_{i}}
$$

where $\left(N_{t}\right), t \in \mathbb{R}_{+}$, is the renewal counting process generated by $\left(\tau_{i}\right)$ and $Z_{\tau}=c+k I(T \leq \tau)$ describes the incurred costs in one cycle. It is well known from renewal theory (see Appendix B, p. 280) that the limits of the expectations of these ratios, $K_{s}$, coincide and are equal to the ratio of the expected costs for one cycle and the expected cycle length:

$$
K_{s}=\lim _{n \rightarrow \infty} E\left[\frac{\sum_{i=1}^{n} Z_{\tau_{i}}}{\sum_{i=1}^{n} \tau_{i}}\right]=\lim _{t \rightarrow \infty} E C_{t}=\frac{E Z_{\tau}}{E \tau}
$$

The objective is to find the replacement age that minimizes this long run average cost per unit time. Inserting the cost function $Z_{t}=c+k I(T \leq t)$ we get

$$
K_{s}=\frac{c+k F(s)}{\int_{0}^{s}(1-F(x)) d x}
$$

Now elementary analysis can be used to find the optimal replacement age $s$, i.e., to find $s^{*}$ with

$$
K_{s^{*}}=\inf \left\{K_{s}: s \in \mathbb{R}_{+} \cup\{\infty\}\right\}
$$

Here $s^{*}=\infty$ means that preventive replacements do not pay and it is optimal to replace only at failures. As can be easily seen this case occurs if the lifetimes are exponentially distributed, i.e., if $F(t)=1-\exp \{-\lambda t\}, t \geq 0, \lambda>0$, then $K_{\infty}=\lambda(c+k) \leq K_{s}$ for all $s>0$.

Example 5.1. Using rudimentary calculus we see that in the case of an increasing failure rate $\lambda(t)=f(t) / \bar{F}(t)$, the optimal replacement age is given by

$$
s^{*}=\inf \left\{t \in \mathbb{R}_{+}: \lambda(t) \int_{0}^{t} \bar{F}(x) d x-F(t) \geq \frac{c}{k}\right\}
$$

where $\inf \emptyset=\infty$. By differentiating it is not hard to show that the left-hand side of the inequality is increasing in the IFR case so that $s^{*}$ can easily be determined. As an example consider the Weibull distribution $F(t)=1-$ $\exp \left\{-(\lambda t)^{\beta}\right\}, t \geq 0$ with $\lambda>0$ and $\beta>1$. The corresponding failure rate is $\lambda(t)=\lambda \beta(\lambda t)^{\beta-1}$ and the optimal replacement age is the unique solution of

$$
\lambda(t) \int_{0}^{t} \exp \left\{-(\lambda x)^{\beta}\right\} d x-1+\exp \left\{-(\lambda t)^{\beta}\right\}=\frac{c}{k}
$$

The cost minimum is then given by $K_{s^{*}}=k \lambda\left(s^{*}\right)$.The age replacement policy allows for planning of a preventive replacement only when a new item is installed. If one wants to fix the time points for preventive replacements in advance for a longer period, one is led to the block replacement policy.

# 5.1.2 Block Replacement Policy 

Under this policy the item is replaced at times $i s, i=1,2, \ldots$ and $s>0$, and at failures. The preventive replacements occur at regular predetermined intervals at a cost of $c$, whereas failures within the intervals incur a cost of $c+k$.

The advantage of this policy is the simple structure and administration because the time points of preventive replacements are fixed and determined in advance. On the other hand, preventive replacements are carried out, irrespective of the age of the processing unit, so that this policy is usually applied to several units at the same time and only if the replacement costs $c$ are comparatively low.

For a fixed time interval $s$ the long run average cost per unit time is

$$
K_{s}=\frac{(c+k) M(s)+c}{s}
$$

where $M$ is the renewal function $M(t)=\sum_{j=1}^{\infty} F^{* j}(t)$ (see Appendix B, p. 274). If the renewal function is known explicitly, we can again use elementary analysis to find the optimal $s$, i.e., to find $s^{*}$ with

$$
K_{s^{*}}=\inf \left\{K_{s}: s \in \mathbb{R}_{+} \cup\{\infty\}\right\}
$$

In most cases the renewal function is not known explicitly. In such a case asymptotic expansions like Theorem B.5, p. 277 in Appendix B or numerical methods have to be used. As is to be expected in the case of an $\operatorname{Exp}(\lambda)$ distribution, preventive replacements do not pay: $M(s)=\lambda s$ and $s^{*}=\infty$.

Example 5.2. Let $F$ be the Gamma distribution function with parameters $\lambda>$ 0 and $n=2$. The corresponding renewal function is

$$
M(s)=\frac{\lambda s}{2}-\frac{1}{4}\left(1-e^{-2 \lambda s}\right)
$$

(cf. [1], p. 274) and $s^{*}$ can be determined as the solution of

$$
\frac{d}{d s} M(s)=\frac{M(s)}{s}+\frac{c}{s(c+k)}
$$

The solution $s^{*}$ is finite if and only if $c /(c+k)<1 / 4$, i.e., if failure replacements are at least four times more expensive than preventive replacements.The age and block replacement policies will result in a finite optimal value of $s$ only if there is some aging and wear-out of the units, i.e., in probabilistic terms the lifetime distribution $F$ fulfills some aging condition like IFR, NBU, or NBUE (see Chap. 2 for these notions). To judge whether it pays to follow a certain policy and in order to compare the policies it is useful to consider the number of failures and the number of planned preventive replacements in a time interval $[0, t]$.

# 5.1.3 Comparisons and Generalizations 

Let $F$ be the underlying lifetime distribution that generates the renewal counting process $\left(N_{t}\right), t \in \mathbb{R}_{+}$, so that $N_{t}$ describes the number of failures or completed replacements in $[0, t]$ following the basic policy replace at failure only. Let $N_{t}^{A}(s)$ and $N_{t}^{B}(s)$ denote the number of failures up to time $t$ following policy $A$ (age replacement) or $B$ (block replacement), respectively, and $R_{t}^{A}(s)$ and $R_{t}^{B}(s)$ the corresponding total number of removals in $[0, t]$ including failures and preventive replacements. We now want to summarize some early comparison results that can be found, including the proofs, in the monographs of Barlow and Proschan [31, 32]. We remind the reader of the notion of stochastic comparison of two positive random variables $X$ and $Y: X \leq_{\text {st }} Y$ means $P(X>t) \leq P(Y>t)$ for all $t \in \mathbb{R}_{+}$.

Theorem 5.3. The following four assertions hold true:
(i) $N_{t} \geq_{\mathrm{st}} N_{t}^{B}(s)$ for all $t \geq 0, s \geq 0 \Longleftrightarrow F$ is $N B U$;
(ii) $N_{t} \geq_{\mathrm{st}} N_{t}^{A}(s)$ for all $t \geq 0, s \geq 0 \Longleftrightarrow F$ is $N B U$;
(iii) $F$ IFR $\Rightarrow N_{t} \geq_{\mathrm{st}} N_{t}^{A}(s) \geq_{\mathrm{st}} N_{t}^{B}(s)$ for all $t \geq 0, s \geq 0$;
(iv) $R_{t}^{A}(s) \leq_{\mathrm{st}} R_{t}^{B}(s)$ for all $t \geq 0, s \geq 0$.

Part (i) and (ii) say that under the weak aging notion NBU it is useful to apply a replacement strategy, since the number of failures is (stochastically) decreased under such a strategy. If, in addition, $F$ has an increasing failure rate, block replacement results in stochastically less failures than age replacement, and it follows that $E N_{t}^{A}(s) \geq E N_{t}^{B}(s)$. On the other hand, for any lifetime distribution $F$ (irrespective of aging notions) block policies have more removals than age policies.

Theorem 5.4. $N_{t}^{A}(s)$ is stochastically increasing in $s$ for each $t \geq 0$ if and only if $F$ is IFR.

This result says that IFR is characterized by the reasonable aging condition that the number of failures is growing with increasing replacement age. Somewhat weaker results hold true for the block policy (see Shaked and Zhu [143] for proofs):

Theorem 5.5. If $N_{t}^{B}(s)$ is stochastically increasing in $s$ for each $t \geq 0$, then $F$ is IFR.Theorem 5.6. The expected value $E N_{t}^{B}(s)$ is increasing in $s$ for each $t \geq 0$ if and only if the renewal function $M(t)$ is convex.

Since the monographs of Barlow and Proschan appeared, many possible generalizations have been investigated concerning (a) the comparison methods, (b) the lifetime models and replacement policies and the cost structures. It is beyond the scope of this book to describe all of these models and refinements. Some hints for further reading can be found in the Bibliographic Notes at the end of the chapter.

Berg [37] and Dekker [63] among others use a marginal cost analysis for studying the optimal replacements problem. Let us, for example, consider this approach for block-type policies. In this model it is assumed that the long run average cost per unit time is given by

$$
K_{s}=\frac{c+R(s)}{s}
$$

where $c$ is the cost of a preventive replacement and $R(s)=\int_{0}^{s} r(x) d x$ denotes the total expected costs due to deterioration over an interval of length $s$. The derivative $r$, called the (marginal) deterioration cost rate, is assumed to be continuous and piecewise differentiable. If in the block replacement model of the preceding Sect. 5.1.2 the lifetime distribution function $F$ has a bounded density $f$, then it is known (see Appendix B, p. 278) that also the corresponding renewal function $M$ admits a density $m$ and we have $R(s)=$ $\int_{0}^{s}(c+k) m(x) d x$, which shows that this is a special case of this block-type model. Now certain properties of the marginal cost rate can be carried over to the cost function $K$. The proof of the following theorem is straightforward and can be found in [63].

Theorem 5.7. (i) If $r(t)$ is nonincreasing on $\left[t_{0}, t_{1}\right]$ for some $0 \leq t_{0}<t_{1}$ and $r\left(t_{0}\right)<K_{t_{0}}$, then $K_{s}$ is also nonincreasing in $s$ on $\left[t_{0}, t_{1}\right]$;
(ii) if $r(t)$ increases strictly for $t>t_{0}$ and some $t_{0} \geq 0$, where $r\left(t_{0}\right)<K_{t_{0}}$, and if either

$$
\text { (a) } \lim _{t \rightarrow \infty} r(t)=\infty \text { or (b) } \lim _{t \rightarrow \infty} r(t)=a \text { and } \lim _{t \rightarrow \infty}(a t-R(t))>c
$$

then $K_{s}$ has a minimum, say $K^{*}$ at $s^{*}$, which is unique on $\left[t_{0}, \infty\right)$; moreover, $K^{*}=K_{s^{*}}=r\left(s^{*}\right)$.

Thus a myopic policy, in which at every moment we consider whether to defer the replacement or not, is optimal. That is, the expected cost of deferring the replacement to level $t+\Delta t$, being $r(t) \Delta t$, should be compared with the minimum average cost over an interval of the same length, being $K^{*} \Delta t$. Hence if $r(t)$ is larger than $K^{*}$, the deferment costs are larger and we should replace. This is the idea of marginal cost analysis as described for example in [37, 63].

The above framework can be extended to age-type policies if we consider the following long run average cost per unit time$$
K_{s}=\frac{c+\int_{0}^{s} r(x) \bar{F}(x) d x}{\int_{0}^{s} \bar{F}(x) d x}
$$

where $c$ is the cost of a preventive replacement and $r$ denotes the marginal deterioration cost rate. Again it can easily be seen that the basic age replacement model (5.1) is a special case setting $r(x)=k \lambda(x)$, where $\lambda(x)=f(x) / \bar{F}(x)$ is the failure rate. Now a very similar analysis can be carried out (see [63]) and the same theorem holds true for this cost criterion except that condition (ii) (b) has to be replaced by

$$
\lim _{t \rightarrow \infty} r(t)=a \text { and } a>\lim _{s \rightarrow \infty} K_{s} \text { for some } a>0
$$

This shows that behind these two quite different models the same optimizations mechanism works. This has been exploited by Aven and Bergman in [19] (see also [21]). They recognized that for many replacement models the optimization criterion can be written in the form

$$
\frac{E\left[\int_{0}^{\tau} a_{t} h_{t} d t+c_{0}\right]}{E\left[\int_{0}^{\tau} h_{t} d t+p_{0}\right]}
$$

where $\tau$ is a stopping time based on the information about the condition of the system, $\left(a_{t}\right)$ is a nondecreasing stochastic process, $\left(h_{t}\right)$ is a nonnegative stochastic process, and $c_{0}$ and $p_{0}$ are nonnegative random variables; all variables are adapted to the information about the condition of the system. Both, the block-type model (5.3) and the age-type model (5.4) are included. Take, for example, for all random quantities deterministic values, especially $\tau=t$, $h_{t}=\bar{F}(t), a_{t}=r(t), p_{0}=0$, and $c_{0}=c$. This leads to the age-type model. In (5.5) the stopping time $\tau$ is the control variable which should be determined in a way that (5.5) is minimized. This problem of choosing a minimizing stopping time is known as an optimal stopping problem and will be further developed in the next section.

# 5.2 A General Replacement Model 

In this section we want to develop the tools that allow certain maintenance problems to be solved in a fairly general way, also considering the possibility of taking different levels of information into account.

### 5.2.1 An Optimal Stopping Problem

In connection with maintenance models as described above, we will have to solve optimization problems. Often an optimal point in time has to be determined that maximizes some reward functional. In terms of the theory of stochastic processes, this optimal point in time will be a stopping time $\tau$ thatmaximizes the expectation $E Z_{\tau}$ of some stochastic process $Z$. We will see that the smooth semimartingale (SSM) representation of $Z$, as introduced in detail in Sect.3.1, is an excellent tool to carry out this optimization. Therefore, we want to solve the stopping problem and to characterize optimal stopping times for the case in which $Z$ is an SSM and $\tau$ ranges in a suitable class of stopping times, say

$$
C^{\mathbb{F}}=\left\{\tau: \tau \text { is an } \mathbb{F} \text {-stopping time, } \tau<\infty, E Z_{\tau}>-\infty\right\}
$$

Without any conditions on the structure of the process $Z$ one cannot hope to find an explicit solution of the stopping problem. A condition called monotone case in the discrete time setting can be transferred to continuous time as follows.

Definition 5.8 (MON). Let $Z=(f, M)$ be an SSM. Then the following condition

$$
\left\{f_{t} \leq 0\right\} \subset\left\{f_{t+h} \leq 0\right\} \forall t, h \in \mathbb{R}_{+}, \bigcup_{t \in \mathbb{R}_{+}}\left\{f_{t} \leq 0\right\}=\Omega
$$

is said to be the monotone case and the stopping time

$$
\zeta=\inf \left\{t \in \mathbb{R}_{+}: f_{t} \leq 0\right\}
$$

is called the ILA-stopping rule (infinitesimal-look-ahead).
Obviously in the monotone case the process $f$ driving the SSM $Z_{t}=$ $\int_{0}^{t} f_{s} d s+M_{t}$ remains negative (nonpositive) if it once crosses zero from above and the ILA-stopping rule $\zeta$ is a natural candidate to solve the maximization problem.

Theorem 5.9. Let $Z=(f, M)$ be an $\mathbb{F}$-SSM and $\zeta$ the ILA-stopping rule. If the martingale $M$ is uniformly integrable, then in the monotone case (5.6)

$$
E Z_{\zeta}=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$

Remark 5.10. The condition that the martingale is uniformly integrable can be relaxed; in [98] it is shown that the condition may be replaced by

$$
M_{\zeta} \in L^{1}, \zeta \in C^{\mathbb{F}}, \lim _{t \rightarrow \infty} \int_{\{\tau>t\}} M_{t}^{-} d P=0 \forall \tau \in C^{\mathbb{F}}
$$

where as usual $a^{-}$denotes the negative part of $a \in \mathbb{R}: a^{-}=\max \{-a, 0\}$. But in most cases such a generalization will not be used in what follows.

Proof. Since $M$ is uniformly integrable we have $E M_{\tau}=0$ for all $\tau \in C^{\mathbb{F}}$ as a consequence of the optional sampling theorem (cf. Appendix A, p. 262). Also $\zeta$ is an element of $C^{\mathbb{F}}$ because $\zeta<\infty$ per definition and $E Z_{\zeta}^{-} \leq E\left|Z_{0}\right|+E\left|M_{\zeta}\right|<$ $\infty$. It remains to show that$$
E \int_{0}^{\zeta} f_{s} d s \geq E \int_{0}^{\tau} f_{s} d s
$$

for all $\tau \in C^{\mathbb{F}}$. But this is an immediate consequence of $f_{s}>0$ on $\{\zeta>s\}$ and $f_{s} \leq 0$ on $\{\zeta \leq s\}$.

The following example demonstrates how this optimization technique can be applied.

Example 5.11. Let $\rho$ be an exponentially distributed random variable with parameter $\lambda>0$ on the basic probability space $(\Omega, \mathcal{F}, \mathbb{F}, P)$ equipped with the filtration $\mathbb{F}$ generated by $\rho$ :

$$
\mathcal{F}_{t}=\sigma(\{\rho>s\}, 0 \leq s \leq t)=\sigma(I(\rho>s), 0 \leq s \leq t)=\sigma(\rho \wedge t)
$$

For the latter equality we make use of our agreement that $\sigma(\cdot)$ denotes the completion of the generated $\sigma$-algebra so that, for instance, the event $\{\rho=$ $t\}=\bigcap_{n \in \mathbb{N}}\left\{t-\frac{1}{n}<\rho \leq t\right\}$ is also included in $\sigma(\rho \wedge t)$. Then we define

$$
Z_{t}=e^{t} I(\rho>t), t \in \mathbb{R}_{+}
$$

This process $Z$ can be interpreted as the potential gain in a harvesting problem (in a wider sense): there is an exponentially growing potential gain and at any time $t$ the decision-maker has to decide whether to realize this gain or to continue observations with the chance of earning a higher gain. But the gain can only be realized up to a random time $\rho$, which is unknown in advance. So there is a risk to loose all potential gains and the problem is to find an optimal harvesting time.

The process $Z$ is adapted, right-continuous and integrable with

$$
E\left[Z_{t+h} \mid \mathcal{F}_{t}\right]=e^{t+h} E\left[I(\rho>t+h) \mid \mathcal{F}_{t}\right]=e^{(1-\lambda) h} Z_{t}, h, t \in \mathbb{R}_{+}
$$

Thus $Z$ is a submartingale (martingale, supermartingale), if $\lambda<1(\lambda=1, \lambda>$ 1). Obviously we have

$$
\lim _{h \rightarrow 0+} \frac{1}{h} E\left[Z_{t+h}-Z_{t} \mid \mathcal{F}_{t}\right]=Z_{t}(1-\lambda)=f_{t}
$$

Theorem 3.6, p. 60, states that $Z$ is an SSM with representation:

$$
Z_{t}=1+\int_{0}^{t} Z_{s}(1-\lambda) d s+M_{t}
$$

Three cases will be discussed separately:

1. $\lambda<1$. The monotone case (5.6) holds true with The ILA stopping time $\zeta=\rho$. But $\zeta$ is not optimal, because $E Z_{\zeta}=0$ and $Z$ is a submartingale with unbounded expectation function: $\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}=\infty$.2. $\lambda>1$. The monotone case holds true with the ILA stopping time $\zeta=0$. It is not hard to show that in this case the martingale

$$
M_{t}=Z_{t}-1-\int_{0}^{t} Z_{s}(1-\lambda) d s
$$

is uniformly integrable. Theorem 5.9 ensures that $\zeta$ is optimal with $E Z_{\zeta}=1$.
3. $\lambda=1$. Again the monotone case (5.6) holds true with the ILA stopping time $\zeta=0$. However, the martingale $M_{t}=e^{t} I(\rho>t)-1$ is not uniformly integrable. But for all $\tau \in C^{\mathbb{F}}$ we have $E M_{\tau}^{-} \leq 1$ and

$$
\lim _{t \rightarrow \infty} \int_{\{\tau>t\}} M_{t}^{-} d P \leq \lim _{t \rightarrow \infty} \int_{\{\tau>t\}} d P=0
$$

so that the more general conditions mentioned in the above remark are fulfilled with $M_{\zeta}=0$. This yields

$$
E Z_{\zeta}=1=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$

# 5.2.2 A Related Stopping Problem 

As was described in Sect.5.1, replacement policies of age and block type are strongly connected to the following stopping problem: minimize

$$
K_{\tau}=\frac{E Z_{\tau}}{E X_{\tau}}
$$

in a suitable class of stopping times, where $Z$ and $X$ are real stochastic processes. For a precise formulation and solution of this problem we use the set-up given in Chap. 3. On the basic complete probability space $(\Omega, \mathcal{F}, P)$ a filtration $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, is given, which is assumed to fulfill the usual conditions concerning right continuity and completeness. Furthermore, let $Z=\left(Z_{t}\right)$ and $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, be real right-continuous stochastic processes adapted to the filtration $\mathbb{F}$. Let $T>0$ be a finite $\mathbb{F}$-stopping time with $E Z_{T}>-\infty, E\left|X_{T}\right|<\infty$ and

$$
C_{T}^{\mathbb{F}}=\left\{\tau: \tau \text { is an } \mathbb{F} \text {-stopping time, } \tau \leq T, E Z_{\tau}>-\infty, E\left|X_{\tau}\right|<\infty\right\}
$$

For $\tau \in C_{T}^{\mathbb{F}}$ we consider the ratio $K_{\tau}$ in (5.7). The stopping problem is then to find a stopping time $\sigma \in C_{T}^{\mathbb{F}}$, with

$$
K^{*}=K_{\sigma}=\inf \left\{K_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}
$$

In this model $T$ describes the random lifetime of some technical system. The index $t$ can be regarded as a time point and $\mathcal{F}_{t}$ as the $\sigma$-algebra which contains all gathered information up to time $t$. The stochastic processes $Z$ and $X$ are adapted to the stream of information $\mathbb{F}$, i.e., $Z$ and $X$ are observable with respect to the given information or in mathematical terms, $Z_{t}$ and $X_{t}$ are $\mathcal{F}_{t}$-measurable for all $t \in \mathbb{R}_{+}$. The replacement times can then be identified with stopping times not greater than the system lifetime $T$.Example 5.12. In the case of block-type models no random information is to be considered so that the filtration reduces to the trivial one and all stopping times are constants, i.e., $C_{T}^{\mathbb{F}}=\mathbb{R}_{+} \cup\{\infty\}$. In this case elementary analysis manipulations yield the optimum and no additional efforts are necessary.

Example 5.13. Let $Z_{t}=c+k I(T \leq t), X_{t}=t$, and $\mathcal{F}_{t}=\sigma\left(Z_{s}, 0 \leq s \leq\right.$ $t)=\sigma(I(T \leq s), 0 \leq s \leq t)$ be the $\sigma$-algebra generated by $Z$, i.e., at any time $t \geq 0$ it is known whether the system works or not. The $\mathbb{F}$-stopping times $\tau \in C_{T}^{\mathbb{F}}$ are of the form $\tau=t^{*} \wedge T$ for some $t^{*}>0$. Then we have $E Z_{\tau}=c+k E I(T \leq \tau)=c+k P\left(T \leq t^{*}\right)$ and $E X_{\tau}=E \tau$, which leads to the basic age replacement policy.

To solve the above-mentioned stopping problem, we will make use of semimartingale representations of the processes $Z$ and $X$. It is assumed that $Z$ and $X$ are SSMs as introduced in Sect. 3.1 with representations

$$
\begin{aligned}
Z_{t} & =Z_{0}+\int_{0}^{t} f_{s} d s+M_{t} \\
X_{t} & =X_{0}+\int_{0}^{t} g_{s} d s+L_{t}
\end{aligned}
$$

As in Sect. 3.1 we use the short notation $Z=(f, M)$ and $X=(g, L)$. Almost all of the stochastic processes used in applications without predictable jumps admit such SSM representations. The following general assumption is made throughout this section:

Assumption (A). $Z=(f, M)$ and $X=(g, L)$ are SSMs with $E Z_{0}>0$, $E X_{0} \geq 0, g_{s}>0$ for all $s \in \mathbb{R}_{+}$and $M^{T}, L^{T} \in \mathcal{M}_{0}$ are uniformly integrable martingales, where $M_{t}^{T}=M_{t \wedge T}, L_{t}^{T}=L_{t \wedge T}$.

Remember that all relations between real random variables hold (only) $P$ almost surely. The first step to solve the optimization problem is to establish bounds for $K^{*}$ in (5.8).

Lemma 5.14. Assume that $(A)$ is fulfilled and

$$
q=\inf \left\{\frac{f_{t}(\omega)}{g_{t}(\omega)}: 0 \leq t<T(\omega), \omega \in \Omega\right\}>-\infty
$$

Then

$$
b_{l} \leq K^{*} \leq b_{u}
$$

holds true, where the bounds are given by

$$
\begin{aligned}
b_{u} & =\frac{E Z_{T}}{E X_{T}} \\
b_{l} & = \begin{cases}\frac{E\left[Z_{0}-q X_{0}\right]}{E X_{T}}+q & \text { if } E\left[Z_{0}-q X_{0}\right]>0 \\
\frac{E Z_{0}}{E X_{0}} & \text { if } E\left[Z_{0}-q X_{0}\right] \leq 0\end{cases}
\end{aligned}
$$Proof. Because $T \in C_{T}^{\mathbb{F}}$ only the lower bound has to be shown. Since the martingales $M^{T}$ and $L^{T}$ are uniformly integrable, the optional sampling theorem (see Appendix A, p. 262) yields $E M_{\tau}=E L_{\tau}=0$ for all $\tau \in C_{T}^{\mathbb{F}}$ and therefore

$$
K_{\tau} \geq \frac{E Z_{0}+q E\left[X_{\tau}-X_{0}\right]}{E X_{\tau}}=\frac{E Z_{0}-q E X_{0}}{E X_{\tau}}+q \geq b_{l}
$$

The lower bound is derived observing that $E X_{0} \leq E X_{\tau} \leq E X_{T}$, which completes the proof.

The following example gives these bounds for the basic age replacement policy.

Example 5.15 (Continuation of Example 5.13). Let us return to the simple cost process $Z_{t}=c+k I(T \leq t)$ with the natural filtration as before. Then $I(T \leq t)$ has the SSM representation

$$
I(T \leq t)=\int_{0}^{t} I(T>s) \lambda(s) d s+M_{t}^{\prime}
$$

where $\lambda$ is the usual failure rate of the lifetime $T$. It follows that the processes $Z$ and $X$ have representations

$$
Z_{t}=c+\int_{0}^{t} I(T>s) k \lambda(s) d s+M_{t}, M_{t}=k M_{t}^{\prime}
$$

and

$$
X_{t}=t=\int_{0}^{t} d s
$$

Assuming the IFR property, we obtain with $\lambda(0)=\inf \left\{\lambda(t): t \in \mathbb{R}_{+}\right\}$and $q=k \lambda(0)$ the following bounds for $K^{*}$ in the basic age replacement model:

$$
\begin{aligned}
b_{u} & =\frac{E Z_{T}}{E X_{T}}=\frac{c+k}{E T} \\
b_{l} & =\frac{c}{E T}+k \lambda(0)
\end{aligned}
$$

These bounds could also be established directly by using (5.1), p. 176. The benefit of Lemma 5.14 lies in its generality, which also allows the bounds to be found in more complex models as the following example shows.

Example 5.16. (Shock Model). Consider now a compound point process model in which shocks arrive according to a marked point process $\left(T_{n}, V_{n}\right)$ as was outlined in Sect.3.3.3. Here we assume that $\left(T_{n}\right)$ is a nonhomogeneous Poisson process with a deterministic intensity $\lambda(s)$ integrating to $\Lambda(t)=\int_{0}^{t} \lambda(s) d s$ and that $\left(V_{n}\right)$ forms an i.i.d. sequence of nonnegative random variables independent of $\left(T_{n}\right)$ with $V_{n} \sim F$. The accumulated damage up to time $t$ is then described by$$
R_{t}=\sum_{n=1}^{N_{t}} V_{n}
$$

where $N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)$ is the number of shocks arrived until $t$. The lifetime of the system is modeled as the first time $R_{t}$ reaches a fixed threshold $S>0$ :

$$
T=\inf \left\{t \in \mathbb{R}_{+}: R_{t} \geq S\right\}
$$

We stick to the simple cost structure of the basic age replacement model, i.e.,

$$
Z_{t}=c+k I(T \leq t)
$$

But now we want to minimize the expected costs per number of arrived shocks in the long run, i.e.,

$$
X_{t}=N_{t}
$$

This cost criterion is appropriate if we think, for example, of systems which are used by customers at times $T_{n}$. Each usage causes some random damage (shock). If the customers arrive with varying intensities governed by external circumstances, e.g., different intensities at different periods of a day, it makes no sense to relate the costs to time, and it is more reasonable to relate the costs to the number of customers served.

The semimartingale representations with respect to the internal filtration generated by the marked point process are (cf. Sect.3.3.5, p. 89)

$$
\begin{aligned}
Z_{t} & =c+\int_{0}^{t} I(T>s) k \lambda(s) \bar{F}\left(\left(S-R_{s}\right)-\right) d s+M_{t} \\
X_{t} & =\int_{0}^{t} \lambda(s) d s+L_{t}
\end{aligned}
$$

The martingale $M$ is uniformly integrable and so is $L^{T}=\left(L_{t \wedge T}\right)$ if we assume that $E \int_{0}^{T} \lambda(s) d s=E \Lambda(T)<\infty$. Lemma 5.14 yields, with

$$
q=\inf \left\{k \bar{F}\left(\left(S-R_{t}\right)-\right): 0 \leq t<T(\omega), \omega \in \Omega\right\}=k \bar{F}(S-)
$$

the following bounds for $K^{*}=\inf \left\{K_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}$ :

$$
\begin{aligned}
b_{u} & =\frac{c+k}{E X_{T}} \\
b_{l} & =\frac{c}{E X_{T}}+k \bar{F}(S-)
\end{aligned}
$$

where $E X_{T}=E \Lambda(T)$. Observe that $X_{T}=\inf \left\{n \in \mathbb{N}: \sum_{i=1}^{n} V_{i} \geq S\right\}$ and $\left\{X_{T}>k\right\}=\left\{\sum_{i=1}^{k} V_{i}<S\right\}$. This yields

$$
E X_{T}=\sum_{k=0}^{\infty} P\left(\sum_{i=1}^{k} V_{i}<S\right) \leq \sum_{k=0}^{\infty} F^{k}(S-)=\frac{1}{\bar{F}(S-)}
$$if $F(S-)<1$. In addition, using Wald's equation $E \sum_{n=1}^{X_{T}} V_{n}=E X_{T} E V_{1} \geq S$, we can derive the following alternative bounds

$$
\begin{aligned}
b_{u}^{\prime} & =(c+k) \frac{E V_{1}}{S} \\
b_{l}^{\prime} & =(c+k) \bar{F}(S-)
\end{aligned}
$$

which can easily be computed.
To solve the stopping problem (5.8) for a ratio of expectations, we use the solution of the simpler case in which we look for the maximum of the expectations $E Z_{\tau}$, where $Z$ is an SSM and $\tau$ ranges in a suitable class of stopping times, which has been considered in detail in Sect. 5.2. It is a wellknown technique to replace the minimization problem (5.8) by an equivalent maximization problem. Observing that $K_{\tau}=E Z_{\tau} / E X_{\tau} \geq K^{*}$ is equivalent to $K^{*} E X_{\tau}-E Z_{\tau} \leq 0$ for all $\tau \in C_{T}^{\mathbb{F}}$, where equality holds for an optimal stopping time, one has the maximization problem:

$$
\begin{aligned}
& \text { Find } \sigma \in C_{T}^{\mathbb{F}} \text { with } E Y_{\sigma}=\sup \left\{E Y_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}=0, \text { where } \\
& Y_{t}=K^{*} X_{t}-Z_{t} \text { and } K^{*}=\inf \left\{K_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}
\end{aligned}
$$

This new stopping problem can be solved by means of the semimartingale representation of the process $Y=\left(Y_{t}\right)$ for $t \in[0, T)$

$$
Y_{t}=K^{*} X_{0}-Z_{0}+\int_{0}^{t}\left(K^{*} g_{s}-f_{s}\right) d s+R_{t}
$$

where the martingale $R=\left(R_{t}\right), t \in \mathbb{R}_{+}$, is given by

$$
R_{t}=K^{*} L_{t}-M_{t}
$$

Now the procedure is as follows. If the integrand $k_{s}=K^{*} g_{s}-f_{s}$ fulfills the monotone case (MON), then Theorem 5.9, p. 181, of Sect. 5.2 yields that the ILA-stopping rule $\sigma=\inf \left\{t \in \mathbb{R}_{+}: k_{t} \leq 0\right\}$ is optimal, provided the martingale part $R$ is uniformly integrable. Note, however, that this stopping time $\sigma$ depends on the unknown value $K^{*}$, which can be determined from the equality $E Y_{\sigma}=0$.

Next we want to define monotonicity conditions that ensure (MON). Obviously under assumption (A), p. 184, the monotone case holds true if the ratio $f_{s} / g_{s}$ is increasing ( $P$-a.s.) with $f_{0} / g_{0}<K^{*}$ and $\lim _{s \rightarrow \infty} f_{s} / g_{s}>K^{*}$. The value $K^{*}$ is unknown so that we need to use the bounds derived, and it seems too restrictive to demand that the ratio is increasing. Especially bath-tubshaped functions, which decrease first up to some $s_{0}$ and increase for $s>s_{0}$, should be covered by the monotonicity condition. This results in the following definition.

Definition 5.17. Let $a, b \in \mathbb{R} \cup\{-\infty, \infty\}$ be constants with $a \leq b$. Then $a$ function $r: \mathbb{R}_{+} \rightarrow \mathbb{R}$ is called(i) $(a, b)$-increasing, if for all $t, h \in \mathbb{R}_{+}$

$$
r(t) \geq a \text { implies } r(t+h) \geq r(t) \wedge b
$$

(ii) $(a, b)$-decreasing, if for all $t, h \in \mathbb{R}_{+}$

$$
r(t) \leq b \text { implies } r(t+h) \leq r(t) \vee a
$$

Roughly spoken, an $(a, b)$-increasing function $r(t)$ passes with increasing $t$ the levels $a, b$ from below and never falls back below such a level. Between $a$ and $b$ the increase is monotone. Obviously a $(0,0)$-decreasing function fulfills (MON) if $r(\infty) \leq 0$. A $(-\infty, \infty)$-increasing (decreasing) function is monotone in the ordinary sense.

The main idea for solving the stopping problem is that, if the ratio $f_{s} / g_{s}$ satisfies such a monotonicity condition, instead of considering all stopping times $\tau \in C_{T}^{\mathbb{F}}$ one may restrict the search for an optimal stopping time to the class of indexed stopping times

$$
\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: x g_{t}-f_{t} \leq 0\right\} \wedge T, \inf \emptyset=\infty, x \in \mathbb{R}
$$

The optimal stopping level $x^{*}$ for the ratio $f_{s} / g_{s}$ can be determined from $E Y_{\sigma}=0$ and coincides with $K^{*}$ as is shown in the following theorem.

Theorem 5.18. Assume (A)(see p. 184) and let $\rho_{x}, x \in \mathbb{R}$, and the bounds $b_{u}, b_{l}$ be defined as above in (5.11) and in Lemma 5.14, p. 184, respectively. If the process $\left(r_{t}\right), t \in \mathbb{R}_{+}$, with $r_{t}=f_{t} / g_{t}$ has $\left(b_{l}, b_{u}\right)$-increasing paths on $[0, T)$, then

$$
\sigma=\rho_{x^{*}}, \text { with } x^{*}=\inf \left\{x \in \mathbb{R}: x E X_{\rho_{x}}-E Z_{\rho_{x}} \geq 0\right\}
$$

is an optimal stopping time and $x^{*}=K^{*}$.
Proof. Since $r$ is $\left(b_{l}, b_{u}\right)$-increasing with $b_{l} \leq K^{*} \leq b_{u}$, it follows that $r$ is also $\left(K^{*}, K^{*}\right)$-increasing, i.e., passes $K^{*}$ at most once from below. Thus the monotone case holds true for the SSM $Y$. From the general assumption (A) on p. 184 we deduce that the martingale part of $Y$ is uniformly integrable so that

$$
\sigma=\inf \left\{t \in \mathbb{R}_{+}: K^{*} g_{t}-f_{t} \leq 0\right\} \wedge T=\rho_{K^{*}}
$$

is optimal with $E Y_{\sigma}=\sup \left\{E Y_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}=0$.
It remains to show that $x^{*}=K^{*}$. Define

$$
v(x)=x E X_{\rho_{x}}-E Z_{\rho_{x}}=x E X_{0}-E Z_{0}+E \int_{0}^{\rho_{x}}\left(x g_{s}-f_{s}\right) d s
$$

Now $v(x)$ is obviously nondecreasing in $x$ and by the definition of $\rho_{x}$ and (A) we have $v(x) \geq-E Z_{0}$. For $x<K^{*}$ and $v(x)>-E Z_{0}$ the following strict inequality holds, since in this case we have either $E X_{0}>0$ or $E X_{0}=0$ and $P\left(\rho_{x}>0\right)>0$ :$$
v(x)<K^{*} E X_{0}-E Z_{0}+E \int_{0}^{\rho_{x}}\left(K^{*} g_{s}-f_{s}\right) d s \leq v\left(K^{*}\right)=0
$$

Equally for $x<K^{*}$ and $v(x)=-E Z_{0}$ we have $v(x)<v\left(K^{*}\right)=0$ because of $E Z_{0}>0$. Therefore,

$$
x^{*}=\inf \left\{x \in \mathbb{R}: v(x) \geq v\left(K^{*}\right)=0\right\}=K^{*}
$$

which proves the assertion.

Remark 5.19. 1. If $E\left[Z_{0}-q X_{0}\right]<0$, then the lower bound $b_{l}$ in Lemma 5.14 is attained for $\sigma=0$. So in this case $K^{*}=E Z_{0} / E X_{0}$ is the minimum without any further monotonicity assumptions.
2. If no monotonicity conditions hold at all, then $x^{*}=\inf \left\{x \in \mathbb{R}: x E X_{\rho_{x}}-\right.$ $\left.E Z_{\rho_{x}} \geq 0\right\}$ is the cost minimum if only stopping times of type $\rho_{x}$ are considered. But $T=\rho_{\infty}$ is among this restricted class of stopping times so that $x^{*}$ is at least an improved upper bound for $K^{*}$, i.e., $b_{u} \geq x^{*}$. From the definition of $x^{*}$ we obtain $x^{*} \geq K_{\rho_{x^{*}}}$, which is obviously bounded below by the overall minimum $K^{*}: b_{u} \geq x^{*} \geq K_{\rho_{x^{*}}} \geq K^{*}$.
3. Processes $r$ with $\left(b_{l}, b_{u}\right)$-increasing paths include especially unimodal or bath-tub-shaped processes provided that $r_{0}<b_{l}$.

The case of a deterministic process $r$ is of special interest and is stated as a corollary under the assumptions of the last theorem.

Corollary 5.20. If $\left(f_{t}\right)$ and $\left(g_{t}\right)$ are deterministic with inverse of the ratio $r^{-1}(x)=\inf \left\{t \in \mathbb{R}_{+}: r_{t}=f_{t} / g_{t} \geq x\right\}, x \in \mathbb{R}$, and $X_{0} \equiv 0$, then $\sigma=t^{*} \wedge T$ is optimal with $t^{*}=r^{-1}\left(K^{*}\right) \in \mathbb{R}_{+} \cup\{\infty\}$ and

$$
K^{*}=\inf \left\{x \in \mathbb{R}: \int_{0}^{r^{-1}(x)}\left(x g_{s}-f_{s}\right) P(T>s) d s \geq E Z_{0}\right\}
$$

If, in addition, $r$ is constant with $r_{t} \equiv r_{0} \forall t \in \mathbb{R}_{+}$, then

$$
K^{*}=\frac{E Z_{0}}{E X_{T}}+r_{0} \text { and } \sigma=T
$$

Remark 5.21. The bounds for $K^{*}$ in Lemma 5.14 are sharp in the following sense. For constant $r_{t} \equiv r_{0}$ in the above corollary the upper and lower bounds coincide.

# 5.2.3 Different Information Levels 

As indicated in Sect.3.2.4 in the context of the general lifetime model, the semimartingale set-up has its advantage in opening new fields of applications. One of these features is the aspect of partial information. In the framework of stochastic process theory, the information is represented by a filtration, anincreasing family of $\sigma$-fields. So it is natural to describe partial information by a family of smaller $\sigma$-fields. Let $\mathbb{A}=\left(\mathcal{A}_{t}\right)$ be a subfiltration of $\mathbb{F}=\left(\mathcal{F}_{t}\right)$, i.e., $\mathcal{A}_{t} \subset \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$. The $\sigma$-field $\mathcal{F}_{t}$ describes the complete information up to time $t$ and $\mathcal{A}_{t}$ can be regarded as the available partial information that allows us to observe versions of the conditional expectations $\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{A}_{t}\right]$ and $\hat{X}_{t}=E\left[X_{t} \mid \mathcal{A}_{t}\right]$, respectively. For all $\mathbb{A}$-stopping times $\tau$ it holds true that $E Z_{\tau}=E \hat{Z}_{\tau}$ and $E X_{\tau}=E \hat{X}_{\tau}$. So the problem to find a stopping time $\sigma$ in the class $C_{T}^{\mathbb{A}}$ of $\mathbb{A}$-stopping times that minimizes $K_{\tau}=E Z_{\tau} / E X_{\tau}$ can be reduced to the ordinary stopping problem by the means developed in the last subsection if $\hat{Z}$ and $\hat{X}$ admit $\mathbb{A}$-SSM representations:

$$
K_{\sigma}=\inf \left\{K_{\tau}=\frac{E Z_{\tau}}{E X_{\tau}}: \tau \in C_{\zeta}^{\mathbb{A}}\right\}=\inf \left\{K_{\tau}=\frac{E \hat{Z}_{\tau}}{E \hat{X}_{\tau}}: \tau \in C_{\zeta}^{\mathbb{A}}\right\}
$$

The projection theorem (Theorem 3.19, p. 69) yields:
If $Z$ is an $\mathbb{F}$-SSM with representation $Z=(f, M)$ and $\mathbb{A}$ is a subfiltration of $\mathbb{F}$, then $\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{A}_{t}\right]$ is an $\mathbb{A}$-SSM with $\hat{Z}=(\hat{f}, \hat{M})$, where $\hat{f}$ is an $\mathbb{A}$-progressively measurable version of $\left(E\left[f_{t} \mid \mathcal{A}_{t}\right]\right), t \in \mathbb{R}_{+}$, and $\hat{M}$ is an $\mathbb{A}$ martingale.

Loosely spoken, if $f$ is the "density" of $Z$ we get the "density" $\hat{f}$ of $\hat{Z}$ simply as the conditional expectation with respect to the subfiltration $\mathbb{A}$. Then the idea is to use the projection $\hat{Z}$ of $Z$ to the $\mathbb{A}$-level and apply the abovedescribed optimization technique to $\hat{Z}$. Of course, on the lower information level the cost minimum is increased,

$$
\inf \left\{K_{\tau}: \tau \in C_{\zeta}^{\mathbb{A}}\right\} \geq \inf \left\{K_{\tau}: \tau \in C_{\zeta}^{\mathbb{F}}\right\}
$$

since all $\mathbb{A}$-stopping times are also $\mathbb{F}$-stopping times, and the question, to what extent the information level influences the cost minimum, has to be investigated.

# 5.3 Applications 

The general set-up to minimize the ratio of expectations allows for many special cases covering a variety of maintenance models. Some few of these will be presented in this section, which show how the general approach can be exploited.

### 5.3.1 The Generalized Age Replacement Model

We first focus on the age replacement model with the long run average cost per unit time criterion: find $\sigma \in C_{T}^{\mathbb{F}}$ with

$$
K^{*}=K_{\sigma}=\frac{E Z_{\sigma}}{E X_{\sigma}}=\inf \left\{K_{\sigma}: \tau \in C_{T}^{\mathbb{F}}\right\}
$$where we now insert $Z_{t}=c+I(T \leq t)$ and $X_{t}=t, t \in \mathbb{R}_{+}$. Without loss of generality the constant $k$, the penalty costs for replacements at failures, introduced in Sect. 5.1.1 is set equal to 1 . We will now make use of the general lifetime model described in detail in Sect.3.2. This means that it is assumed that the indicator process $V_{t}=I(T \leq t)$ has an $\mathbb{F}$-SSM representation with a failure rate process $\lambda$ :

$$
V_{t}=I(T \leq t)=\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}
$$

We know then that $\lambda$ has nonnegative paths, $T$ is a totally inaccessible $\mathbb{F}$ stopping time, and $M$ a uniformly integrable $\mathbb{F}$-martingale (cf. Definition 3.24 and Lemma 3.25, p. 72). With $\lambda_{\min }=q=\inf \left\{\lambda_{t}: 0 \leq t<T(\omega), \omega \in \Omega\right\}$ we get from Lemma 5.14, p. 184, the bounds

$$
b_{l}=\frac{c}{E T}+\lambda_{\min } \leq K^{*} \leq b_{u}=\frac{c+1}{E T}
$$

Note that in contrast to Example 5.15, p. 185, $\lambda$ may be a stochastic failure rate process. If the paths of $\lambda$ are $\left(b_{l}, b_{u}\right)$-increasing, then the SSMs $Z$ and $X$ meet the requirements of Theorem 5.18, p. 188, and it follows that

$$
K^{*}=x^{*}=\inf \left\{x \in \mathbb{R}: x E \rho_{x}-E Z_{\rho_{x}} \geq 0\right\} \text { and } \sigma=\rho_{x^{*}}
$$

where $\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: \lambda_{t} \geq x\right\} \wedge T$. Consequently, if $\lambda$ is nondecreasing or bath-tub-shaped starting at $\lambda_{0}<b_{l}$, we get this solution of the stopping problem. The optimal replacement time is a control-limit rule for the failure rate process $\lambda$.

To give an idea of how partial information influences this optimal solution, we resume the example of a two-component parallel system with i.i.d. random variables $X_{i} \sim \operatorname{Exp}(\alpha), i=1,2$, which describe the component lifetimes (cf. Example 3.38, p. 79). Then the system lifetime is $T=X_{1} \vee X_{2}$ with corresponding indicator process

$$
\begin{aligned}
V_{t} & =I(T \leq t)=\int_{0}^{t} I(T>s) \alpha\left(I\left(X_{1} \leq s\right)+I\left(X_{2} \leq s\right)\right) d s+M_{t} \\
& =\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}
\end{aligned}
$$

Possible different information levels were described in Sect.3.2.4 in detail. We restrict ourselves now to four levels:
(a) The complete information level: $\mathbb{F}=\left(\mathcal{F}_{t}\right)$,

$$
\mathcal{F}_{t}=\sigma\left(I\left(X_{1} \leq s\right), I\left(X_{2} \leq s\right), 0 \leq s \leq t\right)
$$

with failure rate process $\lambda_{t}=\lambda_{t}^{\alpha}=\alpha\left(I\left(X_{1} \leq t\right)+I\left(X_{2} \leq t\right)\right)$.(b) Information only about $T$ until $h>0$, after $h$ complete information: $\mathbb{A}^{b}=\left(\mathcal{A}_{t}^{b}\right)$

$$
\mathcal{A}_{t}^{b}= \begin{cases}\sigma(I(T \leq s), 0 \leq s \leq t) & \text { if } 0 \leq t<h \\ \mathcal{F}_{t} & \text { if } t \geq h\end{cases}
$$

and failure rate process

$$
\hat{\lambda}_{t}^{b}=E\left[\lambda_{t} \mid \mathcal{A}_{t}^{b}\right]= \begin{cases}2 \alpha\left(1-\left(2-e^{-\alpha t}\right)^{-1}\right) & \text { if } 0 \leq t<h \\ \lambda_{t} & \text { if } t \geq h\end{cases}
$$

(c) Information about component lifetime $X_{1}: \mathbb{A}^{c}=\left(\mathcal{A}_{t}^{c}\right)$,

$$
\mathcal{A}_{t}^{c}=\sigma\left(I(T \leq s), I\left(X_{1} \leq s\right), 0 \leq s \leq t\right)
$$

and failure rate process

$$
\hat{\lambda}_{t}^{c}=E\left[\lambda_{t} \mid \mathcal{A}_{t}^{c}\right]=\alpha\left(I\left(X_{1} \leq t\right)+I\left(X_{1}>t\right) P\left(X_{2} \leq t\right)\right)
$$

(d) Information only about $T: \mathbb{A}^{d}=\left(\mathcal{A}_{t}^{d}\right), \mathcal{A}_{t}^{d}=\sigma(I(T \leq s), 0 \leq s \leq t)$, and failure rate (process) $\hat{\lambda}_{t}^{d}=E\left[\lambda_{t} \mid \mathcal{A}_{t}^{d}\right]=2 \alpha\left(1-\left(2-e^{-\alpha t}\right)^{-1}\right)$.
In all four cases the bounds remain the same with $E T=\frac{3}{2 \alpha}$ :

$$
b_{l}=\frac{2 \alpha}{3} c, b_{u}=\frac{2 \alpha}{3}(c+1)
$$

Since $\mathbb{A}^{b}$ and $\mathbb{A}^{c}$ are subfiltrations of $\mathbb{F}$ and include $\mathbb{A}^{d}$ as a subfiltration, we must have for the optimal stopping values

$$
b_{l} \leq K_{a}^{*} \leq K_{b}^{*} \leq K_{d}^{*} \leq b_{u}, K_{a}^{*} \leq K_{c}^{*} \leq K_{d}^{*}
$$

i.e., on a higher information level we can achieve a lower cost minimum. Let us consider the complete information case in more detail. The failure rate process is nondecreasing and the assumptions of Theorem 5.18, p. 188, are met. For the stopping times $\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: \lambda_{t} \geq x\right\} \wedge T$ we have to consider values of $x$ in $\left[b_{l}, b_{u}\right]$ and to distinguish between the cases $0<x \leq \alpha$ and $x>\alpha$ :

- $0<x \leq \alpha$. In this case we have $\rho_{x}=X_{1} \wedge X_{2}, E \rho_{x}=\frac{1}{2 \alpha}, E Z_{\rho_{x}}=c$, such that $x E \rho_{x}-E Z_{\rho_{x}}=0$ leads to $x^{*}=2 \alpha c$, where $0<x^{*} \leq \alpha$ is equivalent to $c \leq \frac{1}{2}$;
- $\alpha<x$. In this case we have $\rho_{x}=T, E \rho_{x}=\frac{3}{2 \alpha}, E Z_{\rho_{x}}=c+1$, such that $x^{*}=b_{u}, x^{*}>\alpha$ is equivalent to $c>\frac{1}{2}$.
The other information levels are treated in a similar way. Only case (b) needs some special attention because the failure rate process $\hat{\lambda}^{b}$ is no longer monotone but only piecewise nondecreasing. To meet the $\left(b_{l}, b_{u}\right)$-increasing condition, we must have $\hat{\lambda}_{h}^{b}<b_{l}$, i.e., $2 \alpha\left(1-\left(2-e^{-\alpha h}\right)^{-1}\right)<\frac{2 \alpha}{3} c$. This inequality holds for all $h \in \mathbb{R}_{+}$, if $c \geq \frac{3}{2}$ and for $h<h(\alpha, c)=-\frac{1}{\alpha} \ln \left(\frac{3-2 c}{3-c}\right)$, if $0<c<\frac{3}{2}$.

We summarize these considerations in the following proposition the proof of which follows the lines above and is elementary but not straightforward.Proposition 5.22. For $0<c \leq \frac{1}{2}$ the optimal stopping times and values $K^{*}$ are
a) $K_{a}^{*}=2 \alpha c, \sigma_{a}=X_{1} \wedge X_{2}$
b) $K_{b}^{*}=\alpha \frac{c+\left(1-e^{\alpha h}\right)^{2}}{0.5+\left(1-e^{\alpha h}\right)^{2}}, \sigma_{b}=\left(\left(X_{1} \wedge X_{2}\right) \vee h\right) \wedge T$, if $0<h<h(\alpha, c)$;
c) $K_{c}^{*}=\alpha \sqrt{2 c}, \sigma_{c}=X_{1} \wedge\left(-\frac{1}{\alpha} \ln (1-\sqrt{2 c})\right)$;
d) $K_{d}^{*}=2 \alpha\left(\sqrt{\frac{c^{2}}{4}+c}-\frac{c}{2}\right), \sigma_{d}=T \wedge\left(-\frac{1}{a} \ln \left(1-\frac{c}{2}-\sqrt{\frac{c^{2}}{4}+c}\right)\right)$.

For $c>\frac{1}{2}$ we have on all levels $K^{*}=b_{u}$ and $\sigma=T$.
For decreasing $c$ the differences between the cost minima increase. If the costs $c$ for a preventive replacement are greater than half of the penalty costs, i.e., $c>\frac{1}{2} k=\frac{1}{2}$, then extra information and preventive replacements are not profitable.

# 5.3.2 A Shock Model of Threshold Type 

In the shock model of Example 5.16, p. 185, the shock arrivals were described by a marked point process $\left(T_{n}, V_{n}\right)$, where at time $T_{n}$ a shock causing damage of amount $V_{n}$ occurs. Here we assume that $\left(T_{n}\right)$ and $\left(V_{n}\right)$ are independent and that $\left(V_{n}\right)$ forms an i.i.d. sequence of nonnegative random variables with $V_{n} \sim F$. As usual $N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)$ counts the number of shocks until $t$ and

$$
R_{t}=\sum_{n=1}^{N_{t}} V_{n}
$$

describes the accumulated damage up to time $t$. In the threshold-type model, the lifetime $T$ is given by

$$
T=\inf \left\{t \in \mathbb{R}_{+}: R_{t} \geq S\right\}, S>0
$$

Now $\mathbb{F}$ is the internal history generated by $\left(T_{n}, V_{n}\right)$ and $\left(\lambda_{t}\right)$ the $\mathbb{F}$-intensity of $\left(N_{t}\right)$. The costs of a preventive replacement are $c>0$ and for a replacement at failure $c+k, k>0$, which results in a cost process $Z_{t}=c+k I(T \leq t)$. The aim is to minimize the expected cost per arriving shock in the long run, i.e., to find $\sigma \in C_{T}^{\mathbb{F}}$ with

$$
K^{*}=K_{\sigma}=\inf \left\{K_{\tau}=\frac{E Z_{\tau}}{E X_{\tau}}, \tau \in C_{T}^{\mathbb{F}}\right\}
$$

where $X_{t}=N_{t}$. The only assumption concerning the shock arrival process is that the intensity $\lambda$ is positive: $\lambda_{t}>0$ on $[0, T)$. According to Example 5.16 and Sect.3.3.3 we have the following SSM representations:

$$
\begin{aligned}
Z_{t} & =c+\int_{0}^{t} I(T>s) k \lambda_{s} \bar{F}\left(\left(S-R_{s}\right)-\right) d s+M_{t} \\
X_{t} & =\int_{0}^{t} \lambda_{s} d s+L_{t}
\end{aligned}
$$Then the cost rate process $r$ is given on $[0, T)$ by $r_{t}=k \bar{F}\left(\left(S-R_{t}\right)-\right)$, which is obviously nondecreasing. Under the integrability assumptions of Theorem 5.18, p. 188, we see that the optimal stopping time is $\sigma=\rho_{x^{*}}=\inf \{t \in$ $\left.\mathbb{R}_{+}: r_{t} \geq x^{*}\right\}$, where the limit $x^{*}=\inf \left\{x \in \mathbb{R}: x E X_{\rho_{x}}-E Z_{\rho_{x}} \geq 0\right\}=K^{*}$ has to be found numerically. Thus the optimal stopping time is a control-limit rule for the process $\left(R_{t}\right)$ : Replace the system the first time the accumulated damage hits a certain control limit.

Example 5.23. Under the above assumptions let $\left(N_{t}\right)$ be a point process with positive intensity $\left(\lambda_{s}\right)$ and $V_{n} \sim \operatorname{Exp}(\nu)$. Then we get with $\bar{F}(x)=\exp \{-\nu x\}$ and $E X_{T}=E\left[\inf \left\{n \in \mathbb{N}: \sum_{i=1}^{n} V_{i} \geq S\right\}\right]=\nu S+1$ the bounds

$$
\begin{aligned}
b_{l} & =\frac{c}{\nu S+1}+k e^{-\nu S} \\
b_{u} & =\frac{c+k}{\nu S+1}
\end{aligned}
$$

and the control-limit rules

$$
\begin{aligned}
\rho_{x} & =\inf \left\{t \in \mathbb{R}_{+}: k \exp \left\{-\nu\left(S-R_{t}\right)\right\} \geq x\right\} \wedge T \\
& =\inf \left\{t \in \mathbb{R}_{+}: R_{t} \geq \frac{1}{\nu} \ln \left(\frac{x}{k}\right)+S\right\} \wedge T
\end{aligned}
$$

We set $g(x)=\frac{1}{\nu} \ln \left(\frac{x}{k}\right)+S$ and observe that $\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: R_{t} \geq g(x)\right\}$, if $0<x \leq k$. For such values of $x$ we find

$$
\begin{aligned}
E X_{\rho_{x}} & =\nu g(x)+1 \\
E Z_{\rho_{x}} & =c+k P\left(T=\rho_{x}\right)=c+k e^{-\nu(S-g(x))}=c+x
\end{aligned}
$$

The probability $P\left(T=\rho_{x}\right)$ is just the probability that a Poisson process with rate $\nu$ has no event in the interval $[g(x), S]$, which equals $e^{-\nu(g(x)-S)}$. By these quantities the optimal control limit $x^{*}=K^{*}$ is the unique solution of

$$
x^{*}=\frac{c+x^{*}}{\nu g\left(x^{*}\right)+1}
$$

provided that $b_{l} \leq x^{*} \leq b_{u}$. As expected this solution does not depend on the specific intensity of the shock arrival process.

# 5.3.3 Information-Based Replacement of Complex Systems 

In this section the basic lifetime model for complex systems is combined with the possibility of preventive replacements. A system with random lifetime $T>$ 0 is replaced by a new equivalent one after failure. A preventive replacement can be carried out before failure. There are costs for each replacement and an additional amount has to be paid for replacements after failures. The aim is to determine an optimal replacement policy with respect to some cost criterion.Several cost criteria are known among which the long run average cost per unit time criterion is by far the most popular one. But the general optimization procedure also allows for other criteria. As an example the total expected discounted cost criterion will be applied in this section. We will also consider the possibility to take different information levels into account. This set-up will be applied to complex monotone systems for which in Sect. 3.2 some examples of various degrees of observation levels were given. For the special case of a twocomponent parallel system with dependent component lifetimes, it is shown how the optimal replacement policy depends on the different information levels and on the degree of dependence of the component lifetimes.

Consider a monotone system with random lifetime $T, T>0$, with an $\mathbb{F}$ semimartingale representation

$$
I(T \leq t)=\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t}
$$

for some filtration $\mathbb{F}$. When the system fails it is immediately replaced by an identical one and the process repeats itself. A preventive replacement can be carried out before failure. Each replacement incurs a cost of $c>0$ and each failure adds a penalty cost $k>0$. The problem is to find a replacement (stopping) time that minimizes the total expected discounted costs.

Let $\alpha>0$ be the discount rate and $\left(Z_{\tau}, \tau\right),\left(Z_{\tau_{1}}, \tau_{1}\right),\left(Z_{\tau_{2}}, \tau_{2}\right), \ldots$ a sequence of i.i.d. pairs of positive random variables, where $\tau_{i}$ represents the replacement age of the $i$ th implemented system, i.e., the length of the $i$ th cycle, and $Z_{\tau_{i}}$ describes the costs incurred during the $i$ th cycle discounted to the beginning of the cycle. Then the total expected discounted costs are

$$
\begin{aligned}
K_{\tau} & =E\left[Z_{\tau_{1}}+e^{-\alpha \tau_{1}} Z_{\tau_{2}}+e^{-\alpha\left(\tau_{1}+\tau_{2}\right)} Z_{\tau_{3}}+\cdots\right] \\
& =\frac{E Z_{\tau}}{E\left[1-e^{-\alpha \tau}\right]}
\end{aligned}
$$

It turns out that $K_{\tau}$ is the ratio of the expected discounted costs for one cycle and $E\left[1-e^{-\alpha \tau}\right]$. Again the set of admissible stopping (replacement) times less or equal to $T$ is

$$
C_{T}^{\mathbb{F}}=\left\{\tau: \tau \text { is an } \mathbb{F} \text {-stopping time } \tau \leq T, E Z_{\tau}^{-}<\infty\right\}
$$

The stopping problem is to find a stopping time $\sigma \in C_{T}^{\mathbb{F}}$ with

$$
K^{*}=K_{\sigma}=\inf \left\{K_{\tau}: \tau \in C_{T}^{\mathbb{F}}\right\}
$$

Stopping at a fixed time $t$ leads to the following costs for one cycle discounted to the beginning of the cycle:

$$
Z_{t}=(c+k I(T \leq t)) e^{-\alpha t}, t \in \mathbb{R}_{+}
$$

Starting from (5.12) such a semimartingale representation can also be obtained for $Z=\left(Z_{t}\right), t \in \mathbb{R}_{+}$, by using the product rule for "differentiating"semimartingales introduced in Sect.3.1.2. Then Theorem A.51, p. 269, can be applied to yield for $t \in[0, T]$ :

$$
\begin{aligned}
Z_{t} & =c+\int_{0}^{t} I(T>s) \alpha e^{-\alpha s}\left(-c+\lambda_{s} \frac{k}{\alpha}\right) d s+R_{t} \\
& =c+\int_{0}^{t} I(T>s) \alpha e^{-\alpha s} r_{s} d s+R_{t}
\end{aligned}
$$

where $r_{s}=\alpha^{-1}\left(-\alpha c+\lambda_{s} k\right)$ is a cost rate and $R=\left(R_{t}\right), t \in \mathbb{R}_{+}$, is a uniformly integrable $\mathbb{F}$-martingale. Since $X_{t}=1-e^{-\alpha t}=\int_{0}^{t} \alpha e^{-\alpha s} d s$, the ratio of the "derivatives" of the two semimartingales $Z$ and $X$ is given by $\left(r_{t}\right)$.

We now consider a monotone system with random component lifetimes $T_{i}>0, i=1,2, \ldots, n, n \in \mathbb{N}$, and structure function $\Phi:\{0,1\}^{n} \rightarrow\{0,1\}$ as introduced in Chap. 2. The system lifetime $T$ is given by $T=\inf \left\{t \in \mathbb{R}_{+}\right.$: $\left.\Phi_{t}=0\right\}$, where the vector process $\left(\mathbf{X}_{t}\right)$ describes the state of the components and $\Phi_{t}=\Phi\left(\mathbf{X}_{t}\right)=I(T>t)$ indicates the state of the system at time $t$. If the random variables $T_{i}$ are independent with (ordinary) failure rates $\lambda_{t}(i)$ and $\mathbb{F}=\left(\mathcal{F}_{t}\right)$ is the (complete information) filtration generated by $\mathbf{X}$, $\mathcal{F}_{t}=\sigma\left(\mathbf{X}_{s}, 0 \leq s \leq t\right)$, then Corollary 3.30 in Sect. 3.2.2 yields the following semimartingale representation for $\Phi_{t}$ :

$$
\begin{aligned}
1-\Phi_{t} & =\int_{0}^{t} I(T>s) \lambda_{s} d s+M_{t} \\
\lambda_{t} & =\sum_{i=1}^{n}\left(\Phi\left(1_{i}, \mathbf{X}_{t}\right)-\Phi\left(0_{i}, \mathbf{X}_{t}\right)\right) \lambda_{t}(i)
\end{aligned}
$$

To find the minimum $K^{*}$ we will proceed as before. First of all bounds $b_{l}$ and $b_{u}$ for $K^{*}$ are determined by means of $q=\inf \left\{r_{t}: 0 \leq t<T(\omega), \omega \in \Omega\right\}$, the minimum of the cost rate with $q \geq-c$ :

$$
b_{l}=\frac{c}{E\left[1-e^{-\alpha T}\right]}+q \leq K^{*} \leq b_{u}=\frac{E\left[(c+k) e^{-\alpha T}\right]}{E\left[1-e^{-\alpha T}\right]}
$$

If all failure rates $\lambda_{t}(i)$ are of IFR-type, then the $\mathbb{F}$-failure rate process $\lambda$ and the ratio process $r$ are nondecreasing. Therefore, Theorem 5.18, p. 188, can be applied to yield $\sigma=\rho_{x^{*}}$. So the optimal stopping time is among the control-limit rules

$$
\begin{aligned}
\rho_{x} & =\inf \left\{t \in \mathbb{R}_{+}: r_{t} \geq x\right\} \wedge T \\
& =\inf \left\{t \in \mathbb{R}_{+}: \lambda_{t} \geq \frac{\alpha}{k}(c+x)\right\} \wedge T
\end{aligned}
$$

This means: replace the system the first time the sum of the failure rates of critical components reaches a given level $x^{*}$. This level has to be determined as

$$
x^{*}=\inf \left\{x \in \mathbb{R}: x E\left[1-e^{-\alpha \rho_{x}}\right]-E\left[c+k I\left(T=\rho_{x}\right) e^{-\alpha \rho_{x}}\right] \geq 0\right\}
$$The effect of partial information is in the following only considered for the case that no single component or only some of the $n$ components are observed, say those with index in a subset $\left\{i_{1}, i_{2}, \ldots, i_{r}\right\} \subset\{1,2, \ldots, n\}, r \leq n$. Then the subfiltration $\mathbb{A}$ is generated by $T$ or by $T$ and the corresponding component lifetimes, respectively. The projection theorem yields a representation on the corresponding observation level:

$$
1-\hat{\Phi}=E\left[I_{\{T \leq t\}} \mid \mathcal{A}_{t}\right]=I_{\{T \leq t\}}=\int_{0}^{t} I(T>s) \hat{\lambda}_{s} d s+\hat{M}_{t}
$$

If the $\mathbb{A}$-failure rate process $\hat{\lambda}_{t}=E\left[\lambda_{t} \mid \mathcal{A}_{t}\right]$ is $\left(b_{l}, b_{u}\right)$-increasing, then the stopping problem can also be solved on the lower information level by means of Theorem 5.18. We want to carry out this in more detail in the next section, allowing also for dependencies between the component lifetimes. To keep the complexity of the calculations on a manageable level, we confine ourselves to a two-component parallel system.

# 5.3.4 A Parallel System with Two Dependent Components 

A two-component parallel system is considered now to demonstrate how the optimal replacement rule can be determined explicitly. It is assumed that the component lifetimes $T_{1}$ and $T_{2}$ follow a bivariate exponential distribution. There are lots of multivariate extensions of the univariate exponential distribution. But it seems that only a few models like those of Freund [68] and Marshall and Olkin [121] are physically motivated.

The idea behind Freund's model is that after failure of one component the stress, placed on the surviving component, is changed. As long as both components work, the lifetimes follow independent exponential distributions with parameters $\beta_{1}$ and $\beta_{2}$. When one of the components fails, the parameter of the surviving component is switched to $\bar{\beta}_{1}$ or $\bar{\beta}_{2}$ respectively.

Marshall and Olkin proposed a bivariate exponential distribution for a two-component system where the components are subjected to shocks. The components may fail separately or both at the same time due to such shocks. This model includes the possibility of a common cause of failure that destroys the whole system at once.

As a combination of these two models the following bivariate distribution can be derived. Let the pair $\left(Y_{1}, Y_{2}\right)$ of random variables be distributed according to the model of Freund and let $Y_{12}$ be another positive random variable, independent of $Y_{1}$ and $Y_{2}$, exponentially distributed with parameter $\beta_{12}$. Then $\left(T_{1}, T_{2}\right)$ with $T_{1}=Y_{1} \wedge Y_{12}, T_{2}=Y_{2} \wedge Y_{12}$ is said to follow a combined exponential distribution. For brevity the notation $\gamma_{i}=\beta_{1}+\beta_{2}-\bar{\beta}_{i}, i \in\{1,2\}$, and $\beta=\beta_{1}+\beta_{2}+\beta_{12}$ is introduced. The survival function

$$
\bar{F}(x, y)=P\left(T_{1}>x, T_{2}>y\right)=P\left(Y_{1}>x, Y_{2}>y\right) P\left(Y_{12}>x \vee y\right)
$$is then given by

$$
\bar{F}(x, y)= \begin{cases}\frac{\beta_{1}}{\gamma_{2}} e^{-\gamma_{2} x-\left(\bar{\beta}_{2}+\beta_{12}\right) y}-\frac{\bar{\beta}_{2}-\beta_{2}}{\gamma_{2}} e^{-\beta y} & \text { for } \quad x \leq y \\ \frac{\beta_{2}}{\gamma_{1}} e^{-\gamma_{1} y-\left(\bar{\beta}_{1}+\beta_{12}\right) x}-\frac{\bar{\beta}_{1}-\beta_{1}}{\gamma_{1}} e^{-\beta x} & \text { for } \quad x>y\end{cases}
$$

where here and in the following $\gamma_{i} \neq 0, i \in\{1,2\}$, is assumed. For $\beta_{i}=\bar{\beta}_{i}$ this formula diminishes to the Marshall-Olkin distribution and for $\beta_{12}=0$ (5.16) gives the Freund distribution. From (5.16) the distribution $H$ of the system lifetime $T=T_{1} \wedge T_{2}$ can be obtained:

$$
\begin{aligned}
H(t) & =P(T \leq t)=P\left(T_{1} \leq t, T_{2} \leq t\right) \\
& =1-\frac{\beta_{2}}{\gamma_{1}} e^{-\left(\bar{\beta}_{1}+\beta_{12}\right) t}-\frac{\beta_{1}}{\gamma_{2}} e^{-\left(\bar{\beta}_{2}+\beta_{12}\right) t}+\frac{\beta_{1} \bar{\beta}_{2}+\beta_{2} \bar{\beta}_{1}-\bar{\beta}_{1} \bar{\beta}_{2}}{\gamma_{1} \gamma_{2}} e^{-\beta t}
\end{aligned}
$$

The optimization problem will be solved for three different information levels:

- Complete information about $T_{1}, T_{2}$ (and $T$ ). The corresponding filtration $\mathbb{F}$ is generated by both component lifetimes:

$$
\mathcal{F}_{t}=\sigma\left(I\left(T_{1} \leq s\right), I\left(T_{2} \leq s\right), 0 \leq s \leq t\right), t \in \mathbb{R}_{+}
$$

- Information about $T_{1}$ and $T$. The corresponding filtration $\mathbb{A}$ is generated by one component lifetime, say $T_{1}$, and the system lifetime:

$$
\mathcal{A}_{t}=\sigma\left(I\left(T_{1} \leq s\right), I(T \leq s), 0 \leq s \leq t\right), t \in \mathbb{R}_{+}
$$

- Information about $T$. The filtration generated by $T$ is denoted by $\mathbb{B}$ :

$$
\mathcal{B}_{t}=\sigma(I(T \leq s), 0 \leq s \leq t), t \in \mathbb{R}_{+}
$$

In the following it is assumed that $\beta_{i} \leq \bar{\beta}_{i}, i \in\{1,2\}$, and $\bar{\beta}_{1} \leq \bar{\beta}_{2}$, i.e., after failure of one component the stress placed on the surviving one is increased. Without loss of generality the penalty costs for replacements after failures are set to $k=1$. The solution of the stopping problem will be outlined in the following. More details are contained in [84].

# 5.3.5 Complete Information About $T_{1}, T_{2}$ and $T$ 

The failure rate process $\lambda$ on the $\mathbb{F}$-observation level is given by (cf. Example 3.27, p. 74)

$$
\lambda_{t}=\beta_{12}+\bar{\beta}_{2} I\left(T_{1}<t<T_{2}\right)+\bar{\beta}_{1} I\left(T_{2}<t<T_{1}\right)
$$

Inserting $q=-c+\beta_{12} \alpha^{-1}$ in (5.15) we get the bounds for the stopping value $K^{*}$$$
b_{l}=\frac{c v}{1-v}+\frac{\beta_{12}}{\alpha} \quad \text { and } \quad b_{u}=\frac{(c+1) v}{1-v}
$$

where $v=E\left[e^{-\alpha T}\right]$ can be determined by means of the distribution $H$. Since the failure rate process is monotone on $[0, T)$ the optimal stopping time can be found among the control limit rules $\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: r_{t} \geq x\right\} \wedge T$ :

$$
\rho_{x}= \begin{cases}0 & \text { for } \quad x \leq \frac{\beta_{12}}{\alpha}-c \\ T_{1} \wedge T_{2} & \text { for } \quad \frac{\beta_{12}}{\alpha}-c<x \leq \frac{\bar{\beta}_{1}+\beta_{12}}{\alpha}-c \\ T_{1} & \text { for } \quad \frac{\bar{\beta}_{1}+\beta_{12}}{\alpha}-c<x \leq \frac{\bar{\beta}_{2}+\beta_{12}}{\alpha}-c \\ T & \text { for } \quad x>\frac{\bar{\beta}_{2}+\beta_{12}}{\alpha}-c\end{cases}
$$

The optimal control limit $x^{*}$ is the solution of the equation

$$
x E\left[1-e^{-\alpha \rho_{x}}\right]-E Z_{\rho_{x}}=0
$$

Since the optimal value $x^{*}$ lies between the bounds $b_{l}$ and $b_{u}$, the considerations can be restricted to the cases $x \geq b_{l}>\beta_{12} \alpha^{-1}-c$. In the first case when $\beta_{12} \alpha^{-1}-c<x \leq\left(\bar{\beta}_{1}+\beta_{12}\right) \alpha^{-1}-c$, one has $\rho_{x}=T_{1} \wedge T_{2}$ and

$$
\begin{aligned}
E\left[1-e^{-\alpha \rho_{x}}\right] & =\frac{\alpha}{\beta+\alpha} \\
E Z_{\rho_{x}} & =c E\left[e^{-\alpha \rho_{x}}\right]+E\left[I\left(T \leq \rho_{x}\right) e^{-\alpha \rho_{x}}\right]=c \frac{\beta}{\beta+\alpha}+\frac{\beta_{12}}{\beta+\alpha}
\end{aligned}
$$

The solution of the equation

$$
x^{*} \frac{\alpha}{\beta+\alpha}-\left(c \frac{\beta}{\beta+\alpha}+\frac{\beta_{12}}{\beta+\alpha}\right)=0
$$

is given by

$$
x^{*}=\frac{1}{\alpha}\left(c \beta+\beta_{12}\right) \quad \text { if } \quad \frac{\beta_{12}}{\alpha}-c<x^{*} \leq \frac{\bar{\beta}_{1}+\beta_{12}}{\alpha}-c
$$

Inserting $x^{*}$ in the latter inequality we obtain the condition $0<c \leq c_{1}$, where $c_{1}=\bar{\beta}_{1}(\beta+\alpha)^{-1}$.

The remaining two cases $\left(\bar{\beta}_{1}+\beta_{12}\right) \alpha^{-1}-c<x \leq\left(\bar{\beta}_{2}+\beta_{12}\right) \alpha^{-1}-c$ and $x>\left(\bar{\beta}_{2}+\beta_{12}\right) \alpha^{-1}-c$ are treated in a similar manner. After some extensive calculations the following solution of the stopping problem is derived:

$$
\begin{aligned}
\rho_{x^{*}} & = \begin{cases}T_{1} \wedge T_{2} & \text { for } 0<c \leq c_{1} \\
T_{1} & \text { for } c_{1}<c \leq c_{2} \\
T & \text { for } c_{2}<c\end{cases} \\
x^{*} & = \begin{cases}x_{1}^{*} & \text { for } 0<c \leq c_{1} \\
x_{2}^{*} & \text { for } c_{1}<c \leq c_{2} \\
x_{3}^{*} & \text { for } c_{2}<c\end{cases}
\end{aligned}
$$where $c_{1}$ is defined as above and

$$
\begin{aligned}
c_{2} & =\frac{\bar{\beta}_{2}}{(\beta+\alpha)}+\frac{\beta_{2}\left(\bar{\beta}_{2}-\bar{\beta}_{1}\right)}{\left(\bar{\beta}_{1}+\beta_{12}+\alpha\right)(\beta+\alpha)} \\
x_{1}^{*} & =\frac{1}{\alpha}\left(c \beta+\beta_{12}\right) \\
x_{2}^{*} & =\frac{1}{\alpha}\left(c\left(\beta_{1}+\beta_{12}\right)+\beta_{12}+\frac{(c+1) \beta_{2} \bar{\beta}_{1}-c \beta_{1} \beta_{2}}{\bar{\beta}_{1}+\beta_{2}+\beta_{12}+\alpha}\right) \\
x_{3}^{*} & =b_{u}
\end{aligned}
$$

The explicit formulas for the optimal stopping value were only presented here to show how the procedure works and that even in seemingly simple cases extensive calculations are necessary. The main conclusion can be drawn from the structure of the optimal policy. For small values of $c$ (note that the penalty costs for failures are $k=1$ ) it is optimal to stop and replace the system at the first component failure. For mid-range values of $c$, the replacement should take place when the "better" component with a lower residual failure rate ( $\bar{\beta}_{1} \leq \bar{\beta}_{2}$ ) fails. If the "worse" component fails first, this results in an replacement after system failure. For high values of $c$, preventive replacements do not pay, and it is optimal to wait until system failure. In this case the optimal stopping value is equal to the upper bound $x^{*}=b_{u}$.

# Information About $T_{1}$ and $T$ 

The failure rate process corresponding to this observation level $\mathbb{A}$ is given by

$$
\begin{aligned}
\lambda_{t} & =g(t) I\left(T_{1}>t\right)+\left(\bar{\beta}_{2}+\beta_{12}\right) I\left(T_{1} \leq t\right) \\
g(t) & =\bar{\beta}_{1}+\beta_{12}-\frac{\bar{\beta}_{1} \gamma_{1}}{\beta_{2} e^{\gamma_{1} t}+\beta_{1}-\bar{\beta}_{1}}
\end{aligned}
$$

where the function $g$ is derived by means of (5.16) as the limit

$$
g(t)=\lim _{h \rightarrow 0+} \frac{1}{h} P\left(t<T_{1} \leq t+h, T_{2} \leq t+h \mid T_{1}>t\right)
$$

The paths of the failure rate process $\lambda$ depend only on the observable component lifetime $T_{1}$ and not on $T_{2}$. The paths are nondecreasing so that the same procedure as before can be applied. For $\gamma_{1}=\beta_{1}+\beta_{2}-\bar{\beta}_{1}>0$ the following results can be obtained:

$$
\begin{aligned}
\rho_{x^{*}} & = \begin{cases}T_{1} \wedge b^{*} & \text { for } 0<c \leq c_{1} \\
T_{1} & \text { for } c_{1}<c \leq c_{2} \\
T & \text { for } c_{2}<c\end{cases} \\
x^{*} & = \begin{cases}x_{1}^{*} & \text { for } 0<c \leq c_{1} \\
x_{2}^{*} & \text { for } c_{1}<c \leq c_{2} \\
x_{3}^{*} & \text { for } c_{2}<c\end{cases}
\end{aligned}
$$The constants $c_{1}, c_{2}$ and the stopping values $x_{2}^{*}, x_{3}^{*}$ are the same as in the complete information case. What is optimal on a higher information level and can be observed on a lower information level must be optimal on the latter too. So only the case $0<c \leq c_{1}$ is new. In this case the optimal replacement time is $T_{1} \wedge b^{*}$ with a constant $b^{*}$, which is the unique solution of the equation

$$
d_{1} \exp \left\{\gamma_{1} b^{*}\right\}+d_{2} \exp \left\{-\left(\bar{\beta}_{1}+\beta_{12}+\alpha\right) b^{*}\right\}+d_{3}=0
$$

The constants $d_{i}, i \in\{1,2,3\}$, are extensive expressions in $\alpha$, the $\beta$ and $\gamma$ constants and therefore not presented here (see [84]). The values of $b^{*}$ and $x_{1}^{*}$ have to be determined numerically. For $\gamma_{1}<0$ a similar result can be obtained.

# Information About $T$ 

On this lowest level $\mathbb{B}$, no additional information about the state of the components is available up to the time of system failure. The failure rate is deterministic and can be derived from the distribution $H$ :

$$
\lambda_{t}=-\frac{d}{d t}(\ln (1-H(t)))
$$

In this case the replacement times $\rho_{x}=T \wedge b, b \in \mathbb{R}_{+} \cup\{\infty\}$, are the wellknown age replacement policies. Even if $\lambda$ is not monotone, such a policy is optimal on this $\mathbb{B}$-level. The optimal values $b^{*}$ and $x^{*}$ have to be determined by minimizing $K_{\rho_{x}}$ as a function of $b$.

## Numerical Examples

The following tables show the effects of changes of two parameters, the replacement cost parameter $c$ and the "dependence parameter" $\beta_{12}$. To be able to compare the cost minima $K^{*}=x^{*}$, both tables refer to the same set of parameters: $\beta_{1}=1, \beta_{2}=3, \bar{\beta}_{1}=1.5, \bar{\beta}_{2}=3.5, \alpha=0.08$. The optimal replacement times are denoted:

$$
\begin{array}{lll}
\text { a: } \rho_{x^{*}}=T_{1} \wedge T_{2} & \text { b: } \rho_{x^{*}}=T_{1} & \text { c: } \rho_{x^{*}}=T_{1} \wedge b^{*} \\
\text { d: } \rho_{x^{*}}=T \wedge b^{*} & \text { e: } \rho_{x^{*}}=T=T_{1} \vee T_{2} &
\end{array}
$$

Table 5.1 shows the cost minima $x^{*}$ for different values of $c$. For small values of $c$, the influence of the information level is greater than for moderate values. For $c>1.394$ preventive replacements do not pay, additional information concerning $T$ is not profitable.

Table 5.2 shows how the cost minimum depends on the parameter $\beta_{12}$. For increasing values of $\beta_{12}$ the difference between the cost minima on different information levels decreases, because the probability of a common failure of both components increases and therefore extra information about a single component is not profitable.Table 5.1. $\beta_{1}=1, \beta_{2}=3, \beta_{12}=0.5, \bar{\beta}_{1}=1.5, \bar{\beta}_{2}=3.5, \alpha=0.08$

| c |  |  | Information level |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | $\mathbb{F}$ | $\mathbb{A}$ | $\mathbb{B}$ | $b_{u}$ |
| 0.01 | 6.453 | 6.813 a | 9.910 c | 11.003 d | 20.506 |  |
| 0.10 | 8.280 | 11.875 a | 17.208 c | 19.678 d | 22.333 |  |
| 0.50 | 16.402 | 28.543 b | 28.543 b | 30.455 e | 30.455 |  |
| 1.00 | 26.553 | 39.764 b | 39.764 b | 40.606 e | 40.606 |  |
| 2.00 | 46.856 | 60.900 e | 60.900 e | 60.900 e | 60.900 |  |

Table 5.2. $\beta_{1}=1, \beta_{2}=3, \bar{\beta}_{1}=1.5, \bar{\beta}_{2}=3.5, c=0.1, \alpha=0.08$

| $\beta_{12}$ |  |  | Information level |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $b_{l}$ | $\mathbb{F}$ | $\mathbb{A}$ | $\mathbb{B}$ | $b_{u}$ |  |
| 0.00 | 1.505 | 5.000 a | 10.739 c | 13.231 d | 16.552 |  |
| 0.10 | 2.859 | 6.375 a | 12.032 c | 14.520 d | 17.698 |  |
| 1.00 | 15.067 | 18.750 a | 23.688 c | 26.132 d | 28.235 |  |
| 10.00 | 138.106 | 142.500 b | 142.500 b | 144.168 e | 144.168 |  |
| 50.00 | 687.677 | 689.448 e | 689.448 e | 689.448 e | 689.448 |  |

# 5.3.6 A Burn-In Model 

Many manufactured items, for example, electronic components, tend either to last a relatively long time or to fail very early. A technique used to screen out the items with short lifelengths before they are delivered to the customer is the so-called burn-in. To burn-in an item means that before the item is released, it undergoes a test during which it is examined under factory conditions or it is exposed to extra stress. After the test phase of (random) length $\tau$, the item is put into operation.

Considering $m$ produced items, and given some cost structure such as costs for failures during and after the test and gains per unit time for released items, one problem related to burn-in is to determine the optimal burn-in duration. This optimal burn-in time may either be fixed in advance and it is therefore deterministic, or one may consider the random information given by the lifelengths of the items failing during the test and obtain a random burn-in time.

We consider a semimartingale approach for solving the optimal stopping problem. In our model, the lifelengths of the items need not be identically distributed, and the stress level during burn-in may differ from the one after burn-in. The information at time $t$ consists of whether and when components failed before $t$. Under these assumptions, we determine the optimal burn-in time $\zeta$.

Let $T_{j}, j=1, \ldots, m$, be independent random variables representing the lifelengths of the items that are burned in. We assume that $E T_{j}<\infty$ for all $j$. We consider burn-in under severe conditions. That means that we assume the items to have different failure rates during and after burn-in, $\lambda_{j}^{0}(t)$ and $\lambda_{j}^{1}(t)$,respectively, where it is supposed that $\lambda_{j}^{0}(t) \geq \lambda_{j}^{1}(t)$ for all $t \geq 0$. We assume that the lifelength $T_{j}$ of the $j$ th item admits the following representation:

$$
I\left(T_{j} \leq t\right)=\int_{0}^{t} I\left(T_{j}>s\right) \lambda_{j}^{Y_{s}}(s) d s+M_{t}(j), j=1, \ldots, m
$$

where $Y_{t}=I(\tau<t), \tau$ is the burn-in time and $M(j) \in \mathcal{M}$ is bounded in $L^{2}$.
This representation can also be obtained by modeling the lifelength of the $j$ th item in the following way:

$$
T_{j}=Z_{j} \wedge \tau+R_{j} I\left(Z_{j}>\tau\right)
$$

where $Z_{j}, R_{j}, j=1, \ldots, m$, are independent random variables and $a \wedge b$ denotes the minimum of $a$ and $b ; Z_{j}$ is the lifelength of the $j$ th item when it is exposed to a higher stress level and $R_{j}$ is the operating time of the item if it survived the burn-in phase. Let $F_{j}$ be the lifelength distribution, $H_{j}$ denote the distribution function of $Z_{j}, j=1, \ldots, m$, and let $H_{j}(0)=F_{j}(0)=0, \bar{H}_{j}(t)=1-H_{j}(t), \bar{F}_{j}(t)=1-F_{j}(t)$. Furthermore, we assume that $H_{j}$ and $F_{j}$ admit densities $h_{j}$ and $f_{j}$, respectively. It is assumed that the operating time $R_{j}$ follows the conditional survival distribution corresponding to $F_{j}$ :

$$
\begin{aligned}
P\left(T_{j} \leq t+s \mid \tau=t<Z_{j}\right) & =P\left(R_{j} \leq s \mid \tau=t<Z_{j}\right) \\
& =\frac{F_{j}(t+s)-F_{j}(t)}{\bar{F}_{j}(t)}, t, s \in \mathbb{R}_{+}
\end{aligned}
$$

In order to determine the optimal burn-in time, we introduce the following cost and reward structure: there is a reward of $c>0$ per unit operating time of released items. In addition there are costs for failures, $c_{B}>0$ for a failure during burn-in and $c_{F}>0$ for a failure after the burn-in time $\tau$, where $c_{F}>c_{B}$. If we fix the burn-in time for a moment to $\tau=t$, then the net reward is given by

$$
Z_{t}=c \sum_{j=1}^{m}\left(T_{j}-t\right)^{+}-c_{B} \sum_{j=1}^{m} I\left(T_{j} \leq t\right)-c_{F} \sum_{j=1}^{m} I\left(T_{j}>t\right), t \in \mathbb{R}_{+}
$$

Since we assume that the failure time of any item can be observed during the burn-in phase, the observation filtration, generated by the lifelengths of the items, is given by

$$
\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}, \mathcal{F}_{t}=\sigma\left(I\left(T_{j} \leq s\right), 0 \leq s \leq t, j=1, \ldots, m\right)
$$

In order to determine the optimal burn-in time, we are looking for an $\mathbb{F}$-stopping time $\zeta \in C^{\mathbb{F}}$ satisfying

$$
E Z_{\zeta}=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$In other words, at any time $t$ the observer has to decide whether to stop or to continue with burn-in with respect to the available information up to time $t$. Since $Z$ is not adapted to $\mathbb{F}$, i.e., $Z_{t}$ cannot be observed directly, we consider the conditional expectation

$$
\begin{aligned}
\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{F}_{t}\right]= & c \sum_{j=1}^{m} I\left(T_{j}>t\right) E\left[\left(T_{j}-t\right)^{+} \mid T_{j}>t\right]-m c_{F} \\
& +\left(c_{F}-c_{B}\right) \sum_{j=1}^{m} I\left(T_{j} \leq t\right)
\end{aligned}
$$

As an abbreviation we use

$$
\mu_{j}(t)=E\left[\left(T_{j}-t\right)^{+} \mid T_{j}>t\right]=\frac{1}{\hat{F}_{j}(t)} \int_{t}^{\infty} \hat{F}_{j}(x) d x, t \in \mathbb{R}_{+}
$$

for the mean residual lifelength. The derivative with respect to $t$ is given by $\mu_{j}^{\prime}(t)=-1+\lambda_{j}^{1}(t) \mu_{j}(t)$. We are now in a position to apply Theorem 5.9, p. 181, and formulate conditions under which the monotone case holds true.

Theorem 5.24. Suppose that the functions

$$
g_{j}(t)=-c-c \mu_{j}(t)\left(\lambda_{j}^{0}(t)-\lambda_{j}^{1}(t)\right)+\left(c_{F}-c_{B}\right) \lambda_{j}^{0}(t)
$$

satisfy the following condition:

$$
\sum_{j \in \mathcal{J}} g_{j}(t) \leq 0 \text { implies } g_{j}(s) \leq 0 \forall j \in \mathcal{J}, \forall \mathcal{J} \subseteq\{1, \ldots, m\}, \forall s \geq t
$$

Then

$$
\zeta=\inf \left\{t \in \mathbb{R}_{+}: \sum_{j=1}^{m} I\left(T_{j}>t\right) g_{j}(t) \leq 0\right\}
$$

is an optimal burn-in time:

$$
E Z_{\zeta}=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$

Proof. In order to obtain a semimartingale representation for $\hat{Z}$ in (5.21) we derive such a representation for $I\left(T_{j}>t\right) \mu_{j}(t)$. Since $\mu_{j}(\cdot)$ and $I\left(T_{j}>\cdot\right)$ are right-continuous and of bounded variation on $[0, t]$, we can use the integration by parts formula for Stieltjes integrals (pathwise) to obtain

$$
\begin{aligned}
\mu_{j}(t) I\left(T_{j}>t\right)= & \mu_{j}(0) I\left(T_{j}>0\right)+\int_{0}^{t} \mu_{j}(s-) d I\left(T_{j}>s\right) \\
& +\int_{0}^{t} I\left(T_{j}>s\right) d \mu_{j}(s)
\end{aligned}
$$

Substituting$$
I\left(T_{j}>s\right)=1+\int_{0}^{s}\left(-I\left(T_{j}>x\right) \lambda_{j}^{0}(x)\right) d x+M_{j}(s)
$$

in this formula and using the continuity of $\mu$, we obtain

$$
\begin{aligned}
\mu_{j}(t) I\left(T_{j}>t\right)= & \mu_{j}(0)+\int_{0}^{t}\left[-\mu_{j}(s) I\left(T_{j}>s\right) \lambda_{j}^{0}(s)+I\left(T_{j}>s\right) \mu_{j}^{\prime}(s)\right] d s \\
& +\int_{0}^{t} \mu_{j}(s) d M_{j}(s) \\
= & \mu_{j}(0)+\int_{0}^{t} I\left(T_{j}>s\right)\left[-1-\mu_{j}(s)\left(\lambda_{j}^{0}(s)-\lambda_{j}^{1}(s)\right)\right] d s \\
& +\tilde{M}_{j}(t)
\end{aligned}
$$

where $\tilde{M}_{j}$ is a martingale, which is bounded in $L^{2}$. This yields the following semimartingale representation for $\hat{Z}$ :

$$
\begin{aligned}
\hat{Z}_{t}= & -m c_{F}+c \sum_{j=1}^{m} \mu_{j}(0) \\
& +\int_{0}^{t} \sum_{j=1}^{m} c I\left(T_{j}>s\right)\left[-1-\mu_{j}(s)\left(\lambda_{j}^{0}(s)-\lambda_{j}^{1}(s)\right)\right] d s \\
& +\left(c_{F}-c_{B}\right) \int_{0}^{t} \sum_{j=1}^{m} I\left(T_{j}>s\right) \lambda_{j}^{0}(s) d s+L_{t} \\
= & -m c_{F}+c \sum_{j=1}^{m} \mu_{j}(0)+\int_{0}^{t} \sum_{j=1}^{m} I\left(T_{j}>s\right) g_{j}(s) d s+L_{t}
\end{aligned}
$$

with a uniformly integrable martingale

$$
L=c \sum_{j=1}^{m} \tilde{M}_{j}+\left(c_{F}-c_{B}\right) \sum_{j=1}^{m} M_{j} \in \mathcal{M}
$$

Since for all $\omega \in \Omega$ and all $t \in \mathbb{R}_{+}$, there exists some $\mathcal{J} \subseteq\{1, \ldots, m\}$ such that $\sum_{j=1}^{m} I\left(T_{j}>t\right) g_{j}(t)=\sum_{j \in \mathcal{J}} g_{j}(t)$, condition (5.22) in the theorem ensures that the monotone case (MON), p. 181, holds true. Therefore we get the desired result by Theorem 5.9 and the proof is complete.

Remark 5.25. The structure of the optimal stopping time shows that high rewards per unit operating time lead to short burn-in times whereas great differences $c_{F}-c_{B}$ between costs for failures in different phases lead to long testing times, as expected.

Equivalent characterizations of condition (5.22) in Theorem 5.24 are given in the following lemma. The proof can be found in [87].Lemma 5.26. Let $t_{\mathcal{J}}=\inf \left\{t \in \mathbb{R}_{+}:\sum_{j \in \mathcal{J}} g_{j}(t) \leq 0\right\}$ and denote $t_{j}=t_{\{j\}}$ for all $j \in\{1, \ldots, m\}$. Then the following conditions are equivalent:
(i) $\sum_{j \in \mathcal{J}} g_{j}(t) \leq 0$ implies $g_{j}(s) \leq 0 \forall j \in \mathcal{J}, \forall \mathcal{J} \subseteq\{1, \ldots, m\}$ and $\forall s \geq t$.
(ii) $t_{\mathcal{J}}=\max _{j \in \mathcal{J}} t_{j} \forall \mathcal{J} \subseteq\{1, \ldots, m\}$ and $g_{j}(s) \leq 0 \forall s \geq t_{j}, \forall j \in$ $\{1, \ldots, m\}$.

$$
\left|\sum_{j: g_{j}(t) \leq 0} g_{j}(t)\right|<\min _{j: g_{j}(t)>0} g_{j}(t) \quad \forall t<\max _{j=1, \ldots, m} t_{j}
$$

and $g_{j}(s) \leq 0 \forall s \geq t_{j}, \forall j \in\{1, \ldots, m\}$.

The following special cases illustrate the result of the theorem.

1. Burn-in forever. If $g_{j}(t)>0$ for all $t \in \mathbb{R}_{+}, j=1, \ldots, m$, then $\zeta=$ $\max \left\{T_{1}, \ldots, T_{m}\right\}$, i.e., burn-in until all items have failed.
2. No burn-in. If $g_{j}(0) \leq 0, j=1, \ldots, m$, then $\zeta=0$ and no burn-in takes place. This case occurs for instance if the costs for failures during and after burn-in are the same: $c_{B}=c_{F}$.
3. Identical items. If all failure rates coincide, i.e., $\lambda_{1}^{0}(t)=\ldots=\lambda_{m}^{0}(t)$ and $\lambda_{1}^{1}(t)=\ldots=\lambda_{m}^{1}(t)$ for all $t \geq 0$, then $g_{j}(t)=g_{1}(t)$ for all $j \in\{1, \ldots, m\}$ and condition (A.1) reduces to

$$
g_{1}(s) \leq 0 \text { for } s \geq t_{1}=\inf \left\{t \in \mathbb{R}_{+}: g_{1}(t) \leq 0\right\}
$$

If this condition is satisfied, the optimal stopping time is of the form $\zeta=t_{1} \wedge \max \left\{T_{1}, \ldots, T_{m}\right\}$, i.e., stop burn-in as soon as $g_{1}(s) \leq 0$ or as soon as all items have failed, whatever occurs first.
4. The exponential case. If all failure rates are constant, equal to $\lambda_{j}^{0}$ and $\lambda_{j}^{1}$, respectively, then $\mu_{j}$ and therefore $g_{j}$ is constant, too, and $\zeta(\omega) \in$ $\left\{0, T_{1}(\omega), \ldots, T_{m}(\omega)\right\}$, if condition (5.22) is satisfied. If, furthermore, the items are "identical," then we have $\zeta=0$ or $\zeta=\max \left\{T_{1}, \ldots, T_{m}\right\}$.
5. No random information. In some situations the lifelengths of the items cannot be observed continuously. In this case one has to maximize the expectation function

$$
E Z_{t}=E \hat{Z}_{t}=-m c_{F}+c \sum_{j=1}^{m} \bar{H}_{j}(t) \mu_{j}(t)+\left(c_{F}-c_{B}\right) \sum_{j=1}^{m} H_{j}(t)
$$

in order to obtain the (deterministic) optimal burn-in time. This can be done using elementary calculus.# 5.4 Repair Replacement Models 

In this section we consider models in which repairs are carried out in negligible time up to the time of a replacement. So the observation of the system does not end with a failure, as in the first sections of this chapter, but are continued until it is decided to replace the system by a new one. Given a certain cost structure the optimal replacement time is derived with respect to the available information.

### 5.4.1 Optimal Replacement Under a General Repair Strategy

We consider a system that fails at times $T_{n}$, according to a point process $\left(N_{t}\right), t \in \mathbb{R}_{+}$, with an intensity $\left(\lambda_{t}\right)$ adapted to some filtration $\mathbb{F}$. At failures a repair is carried out at cost of $c>0$, which takes negligible time. A replacement can be carried out at any time $t$ at an additional cost $k>0$. Following the average cost per unit time criterion, we have to find a stopping time $\sigma$, if there exists one, with

$$
K^{*}=K_{\sigma}=\inf \left\{K_{\tau}=\frac{c E N_{\tau}+k}{E \tau}: \tau \in C^{\mathbb{F}}\right\}
$$

where $C^{\mathbb{F}}=\{\tau: \tau \mathbb{F}$-stopping time, $E \tau<\infty\}$ is a suitable class of stopping times. To solve this problem we can adopt the procedure of Sect. 5.2.1 with some slight modifications.

First of all we have $K_{\tau}=\frac{E Z_{\tau}}{E X_{\tau}}$ with SSM representations

$$
\begin{aligned}
Z_{t} & =k+\int_{0}^{t} c \lambda_{s} d s+M_{t} \\
X_{t} & =\int_{0}^{t} d s
\end{aligned}
$$

Setting $\tau=T_{1}$, we derive the simple upper bound $b_{u}$ :

$$
b_{u}=\frac{c+k}{E T_{1}} \geq K^{*}
$$

The process $Y$ corresponding to (5.10) on p. 187 now reads

$$
Y_{t}=-k+\int_{0}^{t}\left(K^{*}-c \lambda_{s}\right) d s+R_{t}
$$

and therefore we know that, if there exists an optimal finite stopping time $\sigma$, then it is among the indexed stopping times

$$
\rho_{x}=\inf \left\{t \in \mathbb{R}_{+}: \lambda_{t} \geq \frac{x}{c}\right\}, 0 \leq x \leq b_{u}
$$

provided $\lambda$ has nondecreasing paths. We summarize this in a corollary to Theorem 5.18, p. 188.Corollary 5.27. Let the martingale $M$ in (5.23) be such that $\left(M_{t \wedge \rho_{b_{u}}}\right)$ is uniformly integrable. If $\lambda$ has nondecreasing paths and $E \rho_{b_{u}}<\infty$, then

$$
\sigma=\rho_{x^{*}}, \text { with } x^{*}=\inf \left\{x \in \mathbb{R}_{+}: x E \rho_{x}-c E N_{\rho_{x}} \geq k\right\}
$$

is an optimal stopping time and $x^{*}=K^{*}$.
Example 5.28. Considering a nonhomogeneous Poisson process with a nondecreasing deterministic intensity $\lambda_{t}=\lambda(t)$, we observe that the stopping times $\rho_{x}=\lambda^{-1}(x / c)$ are constants. If $\lambda^{-1}\left(b_{u} / c\right)<\infty$, then the corollary can be applied and the optimal stopping time $\sigma$ is a finite constant.

The simplest case is that of a Poisson process with constant rate $\lambda>0$. In this case we have $b_{u}=c \lambda+k \lambda>c \lambda$ and $\rho_{b_{u}}=\infty$, so that the corollary does not apply. But in this case it is easily seen that additional stopping (replacement) costs do not pay and we get that $\sigma=\infty$ is optimal with $K^{*}=c \lambda$.

Example 5.29. Consider the shock model with state-dependent failure probability of Sect.3.3.4 in which shocks arrive according to a Poisson process with rate $\nu$ (cf. Example 3.47, p. 89). The failure intensity is of the form

$$
\lambda_{t}=\nu \int_{0}^{\infty} p\left(X_{t}+y\right) d F(y)
$$

where $p\left(X_{t}+y\right)$ denotes the probability of a failure at the next shock if the accumulated damage is $X_{t}$ and the next shock has amount $y$. Here we assume that this probability function $p$ does not depend on the number of failures in the past. Obviously $\lambda_{t}$ is nondecreasing so that Corollary 5.27 applies provided that the integrability conditions are met.

A variety of point process models as described in Sect. 3.3 can be used in this set-up. Also more general cost structures could be applied as for example random costs $k=\left(k_{t}\right)$, if $k$ admits an SSM representation. Other modifications (discounted cost criterion, different information levels) can be worked out easily apart of some technical problems.

# 5.4.2 A Markov-Modulated Repair Process: Optimization with Partial Information 

In this section a model with a given reward structure is investigated in which an optimal operating time of a system has to be found that balances some flow of rewards and the increasing cost rate due to (minimal) repairs. Consider a one-unit system that fails from time to time according to a point process. After failure a minimal repair is carried out that leaves the state of the system unchanged. The system can work in one of $m$ unobservable states. State " 1 " stands for new or in good condition and " $m$ " is defective or in bad condition. Aging of the system is described by a link between the failure point process andthe unobservable state of the system. The failure or minimal repair intensity may depend on the state of the system. There is some constant flow of income, on the one hand, and on the other hand, each minimal repair incurs a random cost amount. The question is when to stop processing the system and carrying out an inspection or a renewal in order to maximize some reward functional.

For the basic set-up we refer to Example 3.14, p. 65 and Sect.3.3.9. Here we recapitulate the main assumptions of the model:

The basic probability space $(\Omega, \mathcal{F}, P)$ is equipped with a filtration $\mathbb{F}$, the complete information level, to which all processes are adapted, and $S=\{1, \ldots, m\}$ is the set of unobservable environmental states. The changes of the states are driven by a homogeneous Markov process $Y=\left(Y_{t}\right), t \in \mathbb{R}_{+}$, with values in $S$ and infinitesimal parameters $q_{i}$, the rate to leave state $i$, and $q_{i j}$, the rate to reach state $j$ from state $i$. The time points of failures (minimal repairs) $0<T_{1}<T_{2}<\cdots$ form a point process and $N=\left(N_{t}\right), t \in \mathbb{R}_{+}$, is the corresponding counting process:

$$
N_{t}=\sum_{n=1}^{\infty} I\left(T_{n} \leq t\right)
$$

It is assumed that $N$ has a stochastic intensity $\lambda_{Y_{t}}$ that depends on the unobservable state, i.e., $N$ is a so-called Markov-modulated Poisson process with representation

$$
N_{t}=\int_{0}^{t} \lambda_{Y_{s}} d s+M_{t}
$$

where $M$ is an $\mathbb{F}$-martingale and $0<\lambda_{i}<\infty, i \in S$.
Furthermore, let $\left(X_{n}\right), n \in \mathbb{N}$, be a sequence of positive i.i.d. random variables, independent of $N$ and $Y$, with common distribution $F$ and finite mean $\mu$. The cost caused by the $n$th minimal repair at time $T_{n}$ is described by $X_{n}$.

There is an initial capital $u$ and an income of constant rate $c>0$ per unit time.

Now the process $R$, given by

$$
R_{t}=u+c t-\sum_{n=1}^{N_{t}} X_{n}
$$

describes the available capital at time $t$ as the difference of the income and the total amount of costs for minimal repairs up to time $t$.

The process $R$ is well-known in other branches of applied probability like queueing or collective risk theory, where the time to ruin $\tau=\inf \left\{t \in \mathbb{R}_{+}\right.$: $\left.R_{t}<0\right\}$ is investigated (cf. Sect.3.3.9). Here the focus is on determining the optimal operating time with respect to the given reward structure. To achieve this goal one has to estimate the unobservable state of the system at time $t$, given the history of the process $R$ up to time $t$. This can be done using resultsin filtering theory as is shown below. Stopping at a fixed time $t$ results in the net gain

$$
Z_{t}=R_{t}-\sum_{j=1}^{m} k_{j} U_{t}(j)
$$

where $U_{t}(j)=I\left(Y_{t}=j\right)$ is the indicator of the state at time $t$ and $k_{j} \in \mathbb{R}, j \in$ $S$, are stopping costs (for inspection and replacement), which may depend on the stopping state. The process $Z$ cannot be observed directly because only the failure time points and the costs for minimal repairs are known to an observer. The observation filtration $\mathbb{A}=\left(\mathcal{A}_{t}\right), t \in \mathbb{R}_{+}$, is given by

$$
\mathcal{A}_{t}=\sigma\left(N_{s}, X_{i}, 0 \leq s \leq t, i=1, \ldots, N_{t}\right)
$$

Let $C^{\mathbb{A}}=\left\{\tau: \tau\right.$ is a finite $\mathbb{A}$-stopping time, $\left.E Z_{\tau}^{-}<\infty\right\}$ be the set of feasible stopping times in which the optimal one has to be found. As usual $a^{-}=$ $-\min \{0, a\}$ denotes the negative part of $a \in \mathbb{R}$. So the problem is to find $\tau^{*} \in C^{\mathbb{A}}$ which maximizes the expected net gain:

$$
E Z_{\tau^{*}}=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\}
$$

For the solution of this problem an $\mathbb{F}$-semimartingale representation of the process $Z$ is needed, where it is assumed that the complete information filtration $\mathbb{F}$ is generated by $Y, N$, and $\left(X_{n}\right)$ :

$$
\mathcal{F}_{t}=\sigma\left(Y_{s}, N_{s}, X_{i}, 0 \leq s \leq t, i=1, \ldots, N_{t}\right)
$$

Such a representation can be obtained by means of an SSM representation for the indicator process $U_{t}(j)$,

$$
U_{t}(j)=U_{0}(j)+\int_{0}^{t} \sum_{i=1}^{m} U_{s}(i) q_{i j} d s+m_{t}(j), m(j) \in \mathcal{M}_{0}
$$

as follows (see [95] for details):

$$
Z_{t}=u-\sum_{j=1}^{m} k_{j} U_{0}(j)+\int_{0}^{t} \sum_{j=1}^{m} U_{s}(j) r_{j} d s+M_{t}, t \in \mathbb{R}_{+}
$$

where $M=\left(M_{t}\right)$ is an $\mathbb{F}$-martingale and the constants $r_{j}$ are defined by

$$
r_{j}=c-\lambda_{j} \mu-\sum_{\nu \neq j}\left(k_{\nu}-k_{j}\right) q_{j v}
$$

These constants can be interpreted as net gain rates in state $j$ :

- $c$ is the income rate.
- $\lambda_{j}$, the failure rate in state $j$, is the expected number of failures per unit of time, $\mu$ is the expected repair cost for one minimal repair. So $\lambda_{j} \mu$ is the repair cost rate.
- The remaining sum is the stopping cost rate by leaving state $j$.Since the state indicators $U(j)$ and therefore $Z$ cannot be observed, a projection to the observation filtration $\mathbb{A}$ is needed. As described in Sect.3.1.2 such a projection from the $\mathbb{F}$-level (5.25) to the $\mathbb{A}$-level leads to the following conditional expectations:

$$
\hat{Z}_{t}=E\left[Z_{t} \mid \mathcal{A}_{t}\right]=u-\sum_{j=1}^{m} k_{j} \hat{U}_{0}(j)+\int_{0}^{t} \sum_{j=1}^{m} \hat{U}_{s}(j) r_{j} d s+\bar{M}_{t}, t \in \mathbb{R}_{+}
$$

The integrand $\sum_{j=1}^{m} \hat{U}_{s}(j) r_{j}$ with $\hat{U}_{s}(j)=E\left[U_{s} \mid \mathcal{A}_{s}\right]=P\left(Y_{s}=j \mid \mathcal{A}_{s}\right)$ is the conditional expectation of the net gain rate at time $s$ given the observations up to time $s$. If this integrand has nonincreasing paths, then we know that we are in the "monotone case" (cf. p. 181) and the stopping problem could be solved under some additional integrability conditions. To state monotonicity conditions for the integrand in (5.26), an explicit representation of $\hat{U}_{t}(j)$ is needed, which can be obtained by means of results in filtering theory (see [50], p. 98, [93]) in the form of "differential equations":

- Between the jumps of $N: T_{n} \leq t<T_{n+1}$

$$
\begin{aligned}
\hat{U}_{t}(j) & =\hat{U}_{T_{n}}(j)+\int_{T_{n}}^{t}\left(\sum_{i=1}^{m} \hat{U}_{s}(i)\left\{q_{i j}+\hat{U}_{s}(j)\left(\lambda_{i}-\lambda_{j}\right)\right\}\right) d s \\
q_{j j} & =-q_{j} \\
\hat{U}_{0}(j) & =P\left(Y_{0}=j\right), j \in S
\end{aligned}
$$

- At jumps

$$
\hat{U}_{T_{n}}(j)=\frac{\lambda_{j} \hat{U}_{T_{n}-}(j)}{\sum_{i=1}^{m} \lambda_{i} \hat{U}_{T_{n}-}(i)}
$$

where $U_{T_{n}-}(j)$ denotes the left limit.
The following conditions ensure that the system ages, i.e., it moves from the "good" states with high net gains and low failure rates to the "bad" states with low and possibly negative net gains and high failure rates, and it is never possible to return to a "better" state:

$$
\begin{gathered}
q_{i}>0, i=1, \ldots, m-1, q_{i j}=0 \text { for } i>j, i, j \in S \\
r_{1} \geq r_{2} \geq \cdots \geq r_{m}=c-\lambda_{m} \mu, r_{m}<0 \\
0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{m}
\end{gathered}
$$

A reasonable candidate for an optimal $\mathbb{A}$-stopping time is

$$
\tau^{*}=\inf \left\{t \in \mathbb{R}_{+}: \sum_{j=1}^{m} \hat{U}_{t}(j) r_{j} \leq 0\right\}
$$

the first time the conditional expectation of the net gain rate falls below 0 .Theorem 5.30. Let $\tau^{*}$ be the $\mathbb{A}$-stopping time (5.30) and assume that conditions (5.29) hold true. If, in addition, $q_{i m}>\lambda_{m}-\lambda_{i}, i=1, \ldots, m-1$, then $\tau^{*}$ is optimal:

$$
E Z_{\tau^{*}}=\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\}
$$

Proof. Because of $E Z_{\tau}=E \hat{Z}_{\tau}$ for all $\tau \in C^{\mathbb{A}}$ we can apply Theorem 5.9, p. 181, of Chap. 3 taking the $\mathbb{A}$-SSM representation (5.26) of $\hat{Z}$. We will proceed in two steps:
(a) First, we prove that the monotone case holds true.
(b) Second, we show that the martingale part $\bar{M}$ in (5.26) is uniformly integrable.
(a) We start showing that the integrand $\sum_{j=1}^{m} \hat{U}_{s}(j) r_{j}$ has nonincreasing paths. A simple rearrangement gives

$$
\sum_{j=1}^{m} \hat{U}_{s}(j) r_{j}=r_{m}+\left(r_{m-1}-r_{m}\right) \sum_{j=1}^{m-1} \hat{U}_{s}(j)+\cdots+\left(r_{1}-r_{2}\right) \hat{U}_{s}(1)
$$

Since we have from (5.29) that $r_{k-1}-r_{k} \geq 0, k=2, \ldots, m$, it remains to show that $\sum_{\nu=1}^{j} \hat{U}_{s}(\nu)$ is nonincreasing in $s$ for $j=1, \ldots, m-1$. Denoting $\bar{\lambda}(s)=\sum_{j=1}^{m} \hat{U}_{s}(j) \lambda_{j}$ we get from (5.27) between jumps $T_{n}<s<T_{n+1}$, where $T_{0}=0$,

$$
\begin{aligned}
\frac{d}{d s}\left(\sum_{\nu=1}^{j} \hat{U}_{s}(\nu)\right) & =\sum_{\nu=1}^{j}\left(\sum_{i=1}^{m} \hat{U}_{s}(i)\left\{q_{i \nu}+\hat{U}_{s}(\nu)\left(\lambda_{i}-\lambda_{\nu}\right)\right\}\right) \\
& =\sum_{i=1}^{m} \sum_{\nu=1}^{j} \hat{U}_{s}(i) q_{i \nu}+\sum_{\nu=1}^{j} \hat{U}_{s}(\nu)\left(\bar{\lambda}(s)-\lambda_{\nu}\right) \\
& =\sum_{i=1}^{j} \hat{U}_{s}(i)\left(-\sum_{k=j+1}^{m} q_{i k}+\bar{\lambda}(s)-\lambda_{i}\right)
\end{aligned}
$$

using $q_{i j}=0$ for $i>j$ and $q_{i i}=-\sum_{k=i+1}^{m} q_{i k}, i=1, \ldots, m-1$.
From $q_{i m}>\lambda_{m}-\lambda_{i} \geq \bar{\lambda}(s)-\lambda_{i}$ it follows that

$$
\frac{d}{d s}\left(\sum_{\nu=1}^{j} \hat{U}_{s}(\nu)\right) \leq 0, j=1, \ldots, m-1
$$

At jumps $T_{n}$ we have from (5.28)

$$
\sum_{\nu=1}^{j}\left(\hat{U}_{T_{n}}(\nu)-\hat{U}_{T_{n}-}(\nu)\right)=\sum_{\nu=1}^{j} \hat{U}_{T_{n}-}(\nu) \frac{\lambda_{v}-\bar{\lambda}\left(T_{n}-\right)}{\bar{\lambda}\left(T_{n}-\right)}
$$The condition $\lambda_{1} \leq \cdots \leq \lambda_{m}$ ensures that the latter sum is not greater than 0 . This is obvious in the case $\lambda_{j} \leq \bar{\lambda}\left(T_{n}-\right)$; otherwise, if $\lambda_{j}>\bar{\lambda}\left(T_{n}-\right)$, this follows from

$$
0=\sum_{\nu=1}^{m} \hat{U}_{T_{n}-}(\nu) \frac{\lambda_{v}-\bar{\lambda}\left(T_{n}-\right)}{\bar{\lambda}\left(T_{n}-\right)} \geq \sum_{\nu=1}^{j} \hat{U}_{T_{n}-}(\nu) \frac{\lambda_{v}-\bar{\lambda}\left(T_{n}-\right)}{\bar{\lambda}\left(T_{n}-\right)}
$$

For the monotone case to hold it is also necessary that

$$
\bigcup_{t \in \mathbb{R}_{+}}\left\{\sum_{j=1}^{m} \hat{U}_{t}(j) r_{j} \leq 0\right\}=\Omega
$$

or equivalently $\tau^{*}<\infty$. From (5.24) we obtain by means of the projection theorem

$$
\hat{U}_{t}(m)=\hat{U}_{0}(m)+\int_{0}^{t} \sum_{i=1}^{m-1} \hat{U}_{s}(i) q_{i m} d s+\bar{m}_{t}(j)
$$

with a nonnegative integrand. This shows that $\hat{U}_{t}(m)$ is a bounded submartingale. Thus, the limit

$$
\hat{U}_{\infty}(m)=\lim _{t \rightarrow \infty} \hat{U}_{t}(m)=E\left[U_{\infty}(m) \mid \mathcal{A}_{\infty}\right]
$$

exists and is identical to 1 since $\lim _{t \rightarrow \infty} Y_{t}=m$ and hence $U_{\infty}(m)=1$. Because $r_{m}<0$, it is possible to choose some $\epsilon>0$ such that $(1-\epsilon) r_{m}+$ $\epsilon \sum_{i=1}^{m-1} r_{i}<0$. Therefore, we have

$$
\tau^{*}=\inf \left\{t \in \mathbb{R}_{+}: \sum_{j=1}^{m} \hat{U}_{t}(j) r_{j} \leq 0\right\} \leq \inf \left\{t \in \mathbb{R}_{+}: \hat{U}_{t}(m) \geq 1-\epsilon\right\}<\infty
$$

(b) To show that $\bar{M}$ is uniformly integrable we consider a decomposition of the drift term of the $\mathbb{F}$-SSM representation of $Z$ :

$$
\int_{0}^{t} \sum_{j=1}^{m} U_{s}(j) r_{j} d s=\int_{0}^{t} \sum_{j=1}^{m} U_{s}(j)\left(r_{j}-r_{m}\right) d s+t r_{m}
$$

where $t r_{m}$ is obviously A-adapted. We use the projection Theorem 3.19, p. 69 , in the extended version. To this end we have to show that

1. $Z_{0}=c-\sum_{j=1}^{m} k_{j} U_{0}(j)$ and $\int_{0}^{\infty}\left|\sum_{j=1}^{m} U_{s}(j)\left(r_{j}-r_{m}\right)\right| d s$ are square integrable, and that
2. $M$ is square integrable.

The details of these parts are omitted here and can be found in [93, 95].
To sum up, by (a) the monotone case holds true for $\hat{Z}$ with a martingale part $\bar{M}$, which is by (b) square integrable and hence uniformly integrable. The monotone stopping Theorem 5.9 can then be applied and the assertion of the theorem follows.# 5.4.3 The Case of $m=2$ States 

For two states the stopping problem can be reformulated as follows. At an unobservable random time, say $\sigma$, there occurs a switch from state 1 to state 2. Detect this change as well as possible (with respect to the given optimization criterion) by means of the failure process observations. The conditions (5.29) now read

$$
\begin{aligned}
q_{1} & =q_{12}=q>0, q_{2}=q_{21}=0 \\
r_{1} & =c-\lambda_{1} \mu-q\left(k_{2}-k_{1}\right)>0>r_{2}=c-\lambda_{2} \mu \\
0 & <\lambda_{1} \leq \lambda_{2}
\end{aligned}
$$

The conditional distribution of $\sigma$ can be obtained explicitly as the solution of the above differential equations. To obtain this explicit solution we assume in addition $P\left(Y_{0}=1\right)=1$. The result of the (lengthy) calculations is

$$
\begin{aligned}
\hat{U}_{t}(2)=P\left(\sigma \leq t \mid \mathcal{A}_{t}\right) & =1-\frac{e^{-g_{n}(t)}}{d_{n}+\left(\lambda_{2}-\lambda_{1}\right) \int_{T_{n}}^{t} e^{-g_{n}(s)} d s}, T_{n} \leq t<T_{n+1} \\
\hat{U}_{T_{n}}(2) & =\frac{\lambda_{2} \hat{U}_{T_{n}-}(2)}{\lambda_{1}+\left(\lambda_{2}-\lambda_{1}\right) \hat{U}_{T_{n}-}(2)}
\end{aligned}
$$

where $d_{n}=\left(1-\hat{U}_{T_{n}}(2)\right)^{-1}, g_{n}(t)=\left(q-\left(\lambda_{2}-\lambda_{1}\right)\right)\left(t-T_{n}\right)$. The stopping time $\tau^{*}$ in (5.30) can now be written as

$$
\tau^{*}=\inf \left\{t \in \mathbb{R}_{+}: \hat{U}_{t}(2)>z^{*}\right\}, z^{*}=\frac{r_{1}}{r_{1}-r_{2}}
$$

For $0<q<\lambda_{2}-\lambda_{1}, \hat{U}_{t}(2)$ increases as long as $\hat{U}_{t}(2)<q /\left(\lambda_{2}-\lambda_{1}\right)=r$. When $\hat{U}_{t}(2)$ jumps above this level, then between jumps $\hat{U}_{t}(2)$ decreases but not below the level $r$. So even in this case under conditions (5.31) the monotone case holds true if $z^{*} \leq q /\left(\lambda_{2}-\lambda_{1}\right)$. As a consequence of Theorem 5.30 we have the following corollary.

Corollary 5.31. Assume conditions (5.31) with stopping rule $\tau^{*}=\inf \{t \in$ $\left.\mathbb{R}_{+}: \hat{U}_{t}(2)>z^{*}\right\}$. Then $\tau^{*}$ is optimal in $C^{\mathbb{A}}$ if either $q>\lambda_{2}-\lambda_{1}$ or $z^{*} \leq$ $q /\left(\lambda_{2}-\lambda_{1}\right)$.

Remark 5.32. If the failure rates in both states coincide, i.e., $\lambda_{1}=\lambda_{2}$, the observation of the failure time points should give no additional information about the change time point from state 1 to state 2 . Indeed, in this case the conditional distribution of $\sigma$ is deterministic,

$$
P\left(\sigma \leq t \mid \mathcal{A}_{t}\right)=P(\sigma \leq t)=1-\exp \{-q t\}
$$

and $\tau^{*}$ is a constant. As to be expected, random observations are useless in this case.In general, the value of the stopping problem $\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\}$, the best possible expected net gain, cannot be determined explicitly. But it is possible to determine bounds for this value. For this, the semimartingale representation turns out to be useful again, because it allows, by means of the projection theorem, comparisons of different information levels. The constant stopping times are contained in $C^{\mathbb{A}}$ and $C^{\mathbb{A}} \subset C^{\mathbb{F}}$. Therefore, the following inequality applies:

$$
\sup \left\{E Z_{t}: t \in \mathbb{R}_{+}\right\} \leq \sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\} \leq \sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}
$$

At the complete information level $\mathbb{F}$ the change time point $\sigma$ can be observed, and it is obvious that under conditions (5.31) the $\mathbb{F}$-stopping time $\sigma$ is optimal in $C^{\mathbb{F}}$. Thus, we have the following upper and lower bounds $b_{u}$ and $b_{l}$ :

$$
b_{l} \leq \sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{A}}\right\} \leq b_{u}
$$

with

$$
\begin{aligned}
b_{l} & =\sup \left\{E Z_{t}: t \in \mathbb{R}_{+}\right\} \\
b_{u} & =\sup \left\{E Z_{\tau}: \tau \in C^{\mathbb{F}}\right\}=E Z_{\sigma}
\end{aligned}
$$

Some elementary calculations yield

$$
\begin{aligned}
b_{l} & =u-k_{2}+\frac{1}{q}\left(c-\lambda_{1} \mu\right)-\frac{r_{2}}{q} \ln \left(\frac{-r_{2}}{r_{1}-r_{2}}\right) \\
b_{u} & =u-k_{2}+\frac{1}{q}\left(c-\lambda_{1} \mu\right)
\end{aligned}
$$

For $\lambda_{1}=\lambda_{2}$ the optimal stopping time is deterministic so that in this case the lower bound is attained.

# 5.5 Maintenance Optimization Models Under Constraints 

In this section we consider two models: the first one is a so-called delay time model with safety constraints. The aim is to determine optimal inspection intervals minimizing the expected discounted costs under the safety constraints. The second model is also about optimal inspection but here the system is represented by a monotone (coherent) structure function. The state of the components and the system is only revealed through inspections.

### 5.5.1 A Delay Time Model with Safety Constraints

In many cases, the presence of a fault in a system does not lead to an immediate system failure; the system stays in a "defective" state. There will be atime lapse between the occurrence of the fault and the failure of the systema "delay time". This is the idea of the delay time models, which have been thoroughly discussed in the literature. See the Bibliographic Notes at the end of the chapter.

The delay time models are used as bases for determining monitoring strategies for detecting system defects or faults. The state of the system is revealed by inspections, except for failures which are observed. The basic delay time model was introduced for analyzing inspection policies for systems regularly inspected each $T$ time units. If an inspection is carried out during the delay time period, the defect is identified and removed. Thus, the delay time model is based on the simplest monitoring framework possible: a defective state and a nondefective state. In most of the models, the objective of the delay time analysis is to determine optimal inspection times that minimize the (expected) long-run average costs or downtimes.

The framework in the present analysis is the basic delay time model subject to regular inspections every $T$ units of time. If a defect is detected by an inspection, a preventive replacement is performed. If the system fails, a corrective replacement is carried out. A replacement brings the system back to the initial state. A cost is incurred at each inspection.

Furthermore, safety constraints are introduced, related to two important safety aspects: the number of failures of the system and the time spent in the defective state (the delay time). The control of these quantities can be obtained by bounding the probability of at least one system failure occurring during a certain interval of time and by bounding the probability that the delay times are larger than a certain number.

The objective of the analysis is to determine an optimal inspection interval $T$ that minimizes the total expected discounted costs under the two safety constraints.

If $\alpha$ is a positive discount factor, a cost $C$ at time $t$ has a value of $C e^{-\alpha t}$ at time 0 . Letting $T_{i}$ be the length of the $i$ th replacement cycle and $C_{i}$ the total discounted costs associated with the $i$ th replacement cycle, then the total discounted costs incurred can be written (see Sect.5.3.3)

$$
\frac{E C_{1}}{1-E\left[e^{-\alpha T_{1}}\right]}
$$

To explicitly take into account risk and uncertainties we introduce two safety constraints. Below these are defined and the results are compared.

In practice we may consider different levels for the safety constraint. The optimization produces decision support by providing information about the consequences of imposing various safety-level requirements.

Before we search for an optimal inspection time $T$, we need to specify the optimization model in detail.# Problem Definition and Formulation 

We consider a system subject to failures and make the following assumptions.

1. The failure of the system is revealed immediately, and the system is replaced. The replacement time is negligible and the cost of this corrective maintenance is $C_{c}$.
2. Before failure occurs, the system passes through a defective state. Let $X$ be a random variable representing the time to the occurrence of a fault and $Y$ a random variable representing the time in the defective state, in case of no replacement of the system. We denote by $F$ and $G$ the distributions of $X$ and $Y$, respectively. We assume that $F$ and $G$ have densities $f$ and $g$, respectively. Furthermore, we assume that $X$ and $Y$ have finite expectations.
3. All random variables $X$ and $Y$ are independent.
4. Whether or not the system is in a defective state can only be determined by inspection.
5. An inspection takes place every $T$ units of time, and the cost of each inspection is $C_{I}$. These inspections are perfect in the sense that if the system is in a defective state, this will be identified by the inspection. If a defect is identified at an inspection, the system will be replaced by a new one. The replacement time is negligible. The cost of this preventive maintenance is $C_{p}$, where $0<C_{I}<C_{p}<C_{c}<\infty$.

The assumption $C_{I}<C_{p}<C_{c}$ is justified by the following type of arguments. The inspection tasks are assumed to be rather straightforward activities, whereas preventive maintenance tasks are more extensive operations that involve repairs and replacements of the units. Hence it is reasonable to assume $C_{I}<C_{p}$. Furthermore, the corrective maintenance tasks cost more than the preventive maintenance tasks as the replacement of the system is unplanned; hence $C_{p}<C_{c}$.

Consider a replacement cycle defined by the time interval between replacements of the system caused by a preventive maintenance or by a corrective maintenance. For $k=0,1,2, \ldots$, let $X_{T}$ be a random variable representing the time between replacements of the system, i.e.,

$$
X_{T}=\left\{\begin{array}{cc}
(k+1) T & k T<X<(k+1) T \leq X+Y \\
X+Y & k T<X<X+Y \leq(k+1) T
\end{array}\right.
$$

Let $\bar{F}_{T}$ be the survival function of $X_{T}$. By conditioning on $X=u$, we see that

$$
\bar{F}_{T}(t)=\bar{F}(t)+\int_{[t / T] T}^{t} f(u) \bar{G}(t-u) d u, \quad t \geq 0
$$

where $[x]$ denotes the integer part of $x$. From (5.33) we obtain the following lemma:# Lemma 5.33. 

$$
\begin{aligned}
1-E\left[e^{-\alpha X_{T}}\right]= & \int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t \\
& +\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u) \alpha e^{-\alpha u}\left(\int_{0}^{(k+1) T-u} e^{-\alpha v} \bar{G}(v) d v\right) d u
\end{aligned}
$$

Proof. Denoting by $f_{T}$ the density function of $X_{T}$ one obtains that,

$$
\begin{aligned}
1-E\left[e^{-\alpha X_{T}}\right] & =1-\int_{0}^{\infty} e^{-\alpha t} f_{T}(t) d t \\
& =\int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}_{X_{T}}(t) d t
\end{aligned}
$$

integrating by parts. Furthermore, using (5.33) we see that $1-E\left[e^{-\alpha X_{T}}\right]$ can be written as

$$
\begin{aligned}
& \int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t+\int_{0}^{\infty} \alpha e^{-\alpha t}\left(\int_{[t / T] T}^{t} f(u) \bar{G}(t-u) d u\right) d t \\
& \quad=\int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} \alpha e^{-\alpha t}\left(\int_{[t / T] T}^{t} f(u) \bar{G}(t-u) d u\right) d t \\
& \quad=\int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u)\left(\int_{u}^{(k+1) T} \alpha e^{-\alpha t} \bar{G}(t-u) d t\right) d u \\
& \quad=\int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} \alpha e^{-\alpha u} f(u) \\
& \quad\left(\int_{u}^{(k+1) T} e^{-\alpha(t-u)} \bar{G}(t-u) d t\right) d u \\
& \quad=\int_{0}^{\infty} \alpha e^{-\alpha t} \bar{F}(t) d t+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} \alpha e^{-\alpha u} f(u) \\
& \quad\left(\int_{0}^{(k+1) T-u} e^{-\alpha t} \bar{G}(t) d t\right) d u
\end{aligned}
$$

which shows that the lemma holds.
From the assumptions of the model, a cost $C_{p}$ is incurred whenever a preventive maintenance is performed. Hence, the expected discounted costs associated with the preventive maintenance in a replacement cycle is given by

$$
C_{p} \sum_{k=0}^{\infty} e^{-\alpha(k+1) T} \int_{k T}^{(k+1) T} f(u) \bar{G}((k+1) T-u) d u
$$noting that if $X=u$ and $k T<u \leq(k+1) T$, the system is replaced at $(k+1) T$ if the delay time exceeds $(k+1) T-u$.

Analogously, we obtain that the expected discounted costs associated with the corrective maintenance in a replacement cycle equals

$$
C_{c} \sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u)\left(\int_{u}^{(k+1) T} g(v-u) e^{-\alpha v} d v\right) d u
$$

observing that if $X=u$ and $k T<u \leq(k+1) T$, the system is replaced at $v$ if the delay time is $v-u$ and $v<(k+1) T$.

Furthermore, a cost $C_{I}$ is incurred at each inspection and the expected discounted costs associated with these actions equals

$$
\begin{aligned}
& C_{I} \sum_{k=0}^{\infty} \sum_{i=1}^{k+1} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) \bar{G}((k+1) T-u) d u \\
& \quad+C_{I} \sum_{k=1}^{\infty} \sum_{i=1}^{k} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) G((k+1) T-u) d u
\end{aligned}
$$

or rewritten,

$$
\begin{aligned}
& C_{I} \sum_{k=0}^{\infty} e^{-\alpha(k+1) T} \int_{k T}^{(k+1) T} f(u) \bar{G}((k+1) T-u) d u \\
& \quad+C_{I} \sum_{k=1}^{\infty} \sum_{i=1}^{k} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) d u
\end{aligned}
$$

Notice that the expression

$$
\sum_{k=0}^{\infty} e^{-\alpha(k+1) T} \int_{k T}^{(k+1) T} f(u) \bar{G}((k+1) T-u) d u
$$

that appears in (5.34) and (5.36) can be expressed as

$$
\sum_{k=0}^{\infty} \int_{0}^{T} f(u+k T) e^{-\alpha(u+k T)} e^{-\alpha(T-u)} \bar{G}(T-u) d u
$$

and finally as a consequence of the Monotone Convergence Theorem (see Appendix A.2.3) we obtain that

$$
\begin{aligned}
& \sum_{k=0}^{\infty} e^{-\alpha(k+1) T} \int_{k T}^{(k+1) T} f(u) \bar{G}((k+1) T-u) d u \\
& \quad=\int_{0}^{T} h_{T}(u) e^{-\alpha(T-u)} \bar{G}(T-u) d u
\end{aligned}
$$where, for $T>0, h_{T}(u)$ is equal to

$$
h_{T}(u)=\sum_{k=0}^{\infty} f(u+k T) e^{-\alpha(u+k T)}, \quad 0 \leq u \leq T
$$

We denote by $C_{\mathrm{d}}(T)$ the total expected discounted costs in $[0, \infty)$. By (5.32) we can focus on the first cycle. From Lemma (5.33), (5.34), (5.35) and (5.36) we obtain the following expression for $C_{\mathrm{d}}(T)$

$$
C_{\mathrm{d}}(T)=\frac{C_{I} \sum_{k=1}^{\infty} \sum_{i=1}^{k} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) d u+\int_{0}^{T} h_{T}(u) c(T-u) d u}{1+\int_{0}^{T} h_{T}(u)(D(T-u)-1) d u}
$$

where $h_{T}(u)$ is given by $(5.37)$ and for $0 \leq u \leq T$,

$$
\begin{aligned}
c(u) & =\left(C_{p}+C_{I}\right) e^{-\alpha u} \bar{G}(u)+C_{c} \int_{0}^{u} g(v) e^{-\alpha v} d v \\
D(u) & =\int_{0}^{u} e^{-\alpha v} \bar{G}(v) d v
\end{aligned}
$$

Two safety conditions are introduced in this model. The first one is related to the occurrences of system failures, whereas the second is related to the time spent in a defective state.

# Safety Constraint 1: Bound on the Probability of a System Failure 

The first constraint is implemented by bounding the probability of occurrence of one or more failures of the system in an interval $[0, A]$. Denoting by $N_{c, T}(A)$ the number of failures of the system in $[0, A]$ with inspection times each $T$ time units, the safety constraint is expressed as

$$
P\left(N_{c, T}(A) \geq 1\right) \leq \omega_{1}
$$

with $0<\omega_{1}<1$ or equivalently

$$
1-P\left(N_{c, T}(A)=0\right) \leq \omega_{1}
$$

Let $X_{c, T}$ be the time between successive corrective maintenances, then

$$
P\left(N_{c, T}(A)=0\right)=\bar{F}_{c, T}(A)
$$

where $\bar{F}_{c, T}$ represents the survival function of $X_{c, T}$. The following lemma shows the analytical expression for the survival function $\bar{F}_{c, T}$.Lemma 5.34. The survival function $\bar{F}_{c, T}$ of $X_{c, T}$, representing the time between successive corrective maintenances, can be written in the following way:

$$
\begin{gathered}
\bar{F}_{c, T}(t)=\sum_{i=0}^{k} B_{i, T}\left(\bar{F}(t-i T)+\int_{k T}^{t} f(u-i T) \bar{G}(t-u) d u\right) \\
k T \leq t \leq(k+1) T, \quad k=0,1,2, \ldots
\end{gathered}
$$

where the coefficient $B_{i, T}$ equals the probability of a preventive maintenance at $i T$ and is obtained using the recursive formulas:

$$
\begin{aligned}
B_{0, T} & =1 \\
B_{k+1, T} & =\sum_{i=0}^{k} B_{i, T} \int_{k T}^{(k+1) T} f(u-i T) \bar{G}((k+1) T-u) d u, \quad k=0,1,2, \ldots
\end{aligned}
$$

Proof. Notice that we can express $\bar{F}_{c, T}(t)$ as

$$
\bar{F}_{c, T}(t)=\sum_{i=0}^{k} B_{i, T} P_{k, i, T}(t), \quad k T \leq t \leq(k+1) T
$$

where $B_{i, T}$ represents the probability of a preventive maintenance at $i T, 1 \leq$ $i \leq k$ and $P_{k, i, T}(t)$ represents the probability that the system does not fail in $(i T, t]$ and no preventive maintenance is performed in this interval. If the preventive maintenance is not performed in $(i T, t]$, then either no defect of the system arises in $(i T, t]$ or a defect arises in $[k T, t)$ but it does not lead to a failure before $t$. Hence,
$P_{k, i, T}(t)=\bar{F}(t-i T)+\int_{k T}^{t} f(u) \bar{G}(t-u) d u, \quad k T \leq t \leq(k+1) T, \quad 0 \leq i \leq k$.
The probabilities $B_{i, T}$ are obtained in a recursive way as follows. For $i=0$, $B_{0, T}$, the probability of a preventive maintenance at 0 , is equal to 1 . For $i=1$, $B_{1, T}$ represents the probability of a preventive maintenance at $T$, and it is equal to

$$
B_{1, T}=\int_{0}^{T} f(u) \bar{G}(T-u) d u
$$

Analogously, for $i=2, B_{2, T}$ represents the probability of a preventive maintenance at $2 T$. If a preventive maintenance is performed at $2 T$, and the first preventive maintenance is at $T$ or at $2 T$. If the first preventive maintenance is at $T$ and the second one is at $2 T$, then faults of the system arise in $(0, u)$ $(u<T)$ and $(T, v)(v<2 T)$ but do not lead to a failure before $T$ and $2 T$ respectively. This event has the following probability

$$
\left(\int_{0}^{T} f(u) \bar{G}(T-u) d u\right)\left(\int_{T}^{2 T} f(v-T) \bar{G}(2 T-v) d v\right)
$$If the first preventive maintenance is performed at $2 T$, and the system fault arises in $(T, u)$ but does not lead to a failure before $2 T$, the associated probability is equal to

$$
\int_{T}^{2 T} f(u) \bar{G}(2 T-u) d u
$$

Summing over these exclusive events, we obtain

$$
\begin{aligned}
& \left(\int_{0}^{T} f(u) \bar{G}(T-u) d u\right)\left(\int_{T}^{2 T} f(u-T) \bar{G}(2 T-u) d u\right) \\
& \quad+\int_{T}^{2 T} f(u) \bar{G}(2 T-u) d u \\
& \quad=B_{0, T} \int_{T}^{2 T} f(u) \bar{G}(2 T-u) d u+B_{1, T} \int_{T}^{2 T} f(u-T) \bar{G}(2 T-u) d u \\
& \quad=\sum_{i=0}^{1} B_{i, T} \int_{T}^{2 T} f(u-i T) \bar{G}(2 T-u) d u \\
& \quad=B_{2, T}
\end{aligned}
$$

which is the desired result.
A preventive maintenance at $(k+1) T$ is equivalent to a preventive maintenance at $i T$, for any $0 \leq i \leq k$, no fault of the system in $(i T, k T)$ and a defect in $[k T,(k+1) T)$ which does not lead a failure before $(k+1) T$. Following the same type of arguments as above it follows that this event has the following probability

$$
\sum_{i=0}^{k} B_{i, T} \int_{k T}^{(k+1) T} f(u-i T) \bar{G}((k+1) T-u) d u
$$

Hence the result holds.
Using (5.41), the safety constraint can be formulated as

$$
a_{A}(T) \leq \omega_{1}
$$

where $0<\omega_{1}<1$ and

$$
a_{A}(T)=\left\{\begin{array}{cc}
1-\sum_{i=0}^{[A / T]} B_{i, T}\left(\bar{F}(A-i T)+\int_{[A / T] T}^{A} f(u-i T) \bar{G}(A-u) d u\right) & A \geq T \\
\int_{0}^{A} f(u) G(A-u) d u & A<T
\end{array}\right.
$$# Safety Constraint 2: Bound on the Limiting Fraction of Time Spent in a Defective State 

The second safety constraint is related to the time spent in a failure state. What we would like to control is the proportion of time the system is in such a state. This is implemented by considering the asymptotic limit $b(T)$, which is equal to the expected time that the system is in the defective state in a replacement cycle divided by the expected renewal cycle (see Appendix B.2). Hence we can formulate the safety criterion as

$$
b(T)=\frac{E \int_{0}^{X_{T}} 1_{d}(u) d u}{E\left[X_{T}\right]} \leq \omega_{2}
$$

where $0<\omega_{2}<1$ and $1_{d}(\cdot)$ denotes the indicator function which equals 1 if the system is defective at time $u$ and 0 otherwise. From (5.33), the expected length of a replacement cycle for this model is equal to

$$
\begin{aligned}
E\left[X_{T}\right] & =\int_{0}^{\infty} \bar{F}_{T}(t) d t \\
& =E[X]+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u)\left(\int_{0}^{(k+1) T-u} \bar{G}(v) d v\right) d u
\end{aligned}
$$

It follows that this second safety constraint can be expressed as

$$
b(T) \leq \omega_{2}
$$

where $b(T)$ is given by

$$
b(T)=\frac{\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u)\left(\int_{0}^{(k+1) T-u} \bar{G}(v) d v\right) d u}{E[X]+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} f(u)\left(\int_{0}^{(k+1) T-u} \bar{G}(v) d v\right) d u}, \quad 0<T \leq \infty
$$

## Optimization

The problem is to find a value of $T$ that minimizes $C_{\mathrm{d}}(T)$ given by (5.38) under the safety constraints given by (5.42) or (5.44), that is, finding a value $T_{\text {opt }}$ such that

$$
C_{\mathrm{d}}\left(T_{\mathrm{opt}}\right)=\inf \left\{C_{\mathrm{d}}(T): T \in \Upsilon\right\}
$$

where $\Upsilon$ is the set of inspection times satisfying the inequality (5.42) or (5.44), i.e.,

$$
\Upsilon=\left\{T>0 ; \quad a_{A}(T) \leq \Upsilon_{1}\right\}
$$or

$$
\Upsilon=\left\{T>0 ; \quad b(T) \leq \Upsilon_{2}\right\}
$$

where $a_{A}(T)$ and $b(T)$ are given by (5.43) and (5.45), respectively.
Analyzing the terms in the function $C_{\mathrm{d}}(T)$ given by (5.38), we will show that $C_{\mathrm{d}}(T)$ is a continuous function in $T$, with

$$
\lim _{T \rightarrow 0} C_{\mathrm{d}}(T)=\infty
$$

To show the continuity of the function $C_{\mathrm{d}}(T)$, we need to assume that the density function $f$ of $X$ is continuous. Then $h_{T}(u)$, given by (5.37), is continuous in $u$ and continuous in $T$, and hence

$$
\int_{0}^{T} h_{T}(u) c(T-u) d u \quad \text { and } \quad 1-\int_{0}^{T} h_{T}(u)(D(T-u)-1) d u
$$

where $c$ and $D$ are given by (5.39) and (5.40), are continuous functions in $T$. Moreover,

$$
\begin{aligned}
\int_{0}^{T} h_{T}(u) c(T-u) d u & \leq\left(C_{p}+C_{I}+C_{c}\right) \int_{0}^{T} h_{T}(u) d u \\
& =\left(C_{p}+C_{c}+C_{I}\right) \int_{0}^{\infty} f(u) e^{-\alpha u} d u
\end{aligned}
$$

and consequently

$$
\lim _{T \rightarrow 0} \int_{0}^{T} h_{T}(u) c(T-u) d u<\infty
$$

and

$$
\lim _{T \rightarrow 0}\left(1+\int_{0}^{T} h_{T}(u)(D(T-u)-1) d u\right)=\int_{0}^{\infty} \alpha e^{-\alpha u} \bar{F}(u) d u<\infty
$$

using that $E[X]$ is finite.
Furthermore, notice that

$$
\begin{aligned}
\sum_{k=1}^{\infty} \sum_{i=1}^{k} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) d u & =\sum_{k=1}^{\infty} \frac{e^{-\alpha T}-e^{-\alpha(k+1) T}}{1-e^{-\alpha T}} \int_{k T}^{(k+1) T} f(u) d u \\
& =\frac{e^{-\alpha T}}{1-e^{-\alpha T}}\left(1-\sum_{k=1}^{\infty} e^{-\alpha k T} \int_{k T}^{(k+1) T} f(u) d u\right)
\end{aligned}
$$

is continuous in $T$ and

$$
\lim _{T \rightarrow 0} \sum_{k=1}^{\infty} \sum_{i=1}^{k} e^{-\alpha i T} \int_{k T}^{(k+1) T} f(u) d u=\infty
$$Taking these properties into account, the function $C_{\mathrm{d}}(T)$ given by (5.38) is a continuous function in $T$ and $\lim _{T \rightarrow 0} C_{\mathrm{d}}(T)=\infty$. Hence the minimum of $C_{\mathrm{d}}(T)$ in the unconstrained case exists if we include the delay-time policy for $T=\infty$, i.e., a delay-time policy without inspections for which corresponding expected discounted costs are given by

$$
\lim _{T \rightarrow \infty} C_{\mathrm{d}}(T)=\frac{C_{c} \int_{0}^{\infty} f(u) e^{-\alpha u} d u \int_{0}^{\infty} g(v) e^{-\alpha v} d v}{\int_{0}^{\infty} \alpha e^{-\alpha u} \bar{F}(u) d u+\int_{0}^{\infty} \alpha e^{-\alpha u} f(u) d u \int_{0}^{\infty} e^{-\alpha v} \bar{G}(v) d v}
$$

We see that $C_{\mathrm{d}}(\infty)<\infty$.
Let $T^{*}$ be an optimal value of $T$ in the unconstrained case, i.e.,

$$
C_{\mathrm{d}}\left(T^{*}\right)=\inf \left\{C_{\mathrm{d}}(T): T>0\right\}
$$

Clearly, if $T^{*} \in \Upsilon$, then $T_{\text {opt }}=T^{*}$, i.e., $T^{*}$ is an optimal solution also to the constrained optimization problem.

The analytical optimization of $C_{\mathrm{d}}(T)$ is not straightforward as the function $C_{\mathrm{d}}(T)$ is not on the standard form seen for many maintenance models (nonincreasing up to a minimum value and then nondecreasing), even when assuming $F$ and $G$ to have increasing failure rate distributions. As we will show later, $C_{\mathrm{d}}(T)$ could have several local minimum values. Also the safety constraint functions $a_{A}(T)$ and $b(T)$ could have rather irregular forms, when we compare these to the common increasing shapes seen for other maintenance optimization models.

# Numerical Examples 

In this section we present some numerical examples of the above model. The aim is to find a value of $T$ that minimizes $C_{\mathrm{d}}(T)$ given by (5.38) under the two safety constraints based on the occurrence of failures in an interval (5.42) and the fraction of time in a defective state (5.44). We refer to these constraints as criterion 1 and criterion 2, respectively.

We assume that the distributions of the random variables $X$ and $Y$ follow Weibull distributions with nondecreasing failure rates, i.e.,

$$
\bar{F}(t)=\exp \left\{-\left(\lambda_{1} t\right)^{\beta_{1}}\right\}, \quad \bar{G}(t)=\exp \left\{-\left(\lambda_{2} t\right)^{\beta_{2}}\right\}, \quad t \geq 0
$$

where $\beta_{i}>1$ for $i=1,2$.
Intuitively we may think that the proportion of time that the system is in a defective state is increasing with respect to $T$. However, this is not in general true. A counterexample, based on rather extreme failure rates, is given in the following.Let $\lambda_{1}=1, \lambda_{2}=1, \beta_{1}=20$ and $\beta_{2}=30$ be the parameters of the Weibull distributions. For these parameters

$$
E[X]=0.9735, \quad E[Y]=0.9818
$$

Figure 5.1 shows a simulation of the long-run proportion of time that the system is in a defective state as a function of $T$. The simulation has been carried out using 500 points between 0.2 and 2.2 with 500,000 realizations in each point. We see from the figure that $b(T)$ in this case shows a rather irregular form, with many local minimum and maximum values.


Fig. 5.1. Function $b(T)$ versus $T$

A similar case is observed for the function $a_{A}(T)$ given by (5.43). This function represents the probability of occurrence of at least one failure in $[0, A]$. For the same numerical example as above, the monotonicity of $a_{A}(T)$ is not guaranteed as we can see from Fig. 5.2, which displays a simulation of $a_{A}(T)$ for $A=2$.

In the case $\lambda_{1}=1, \beta_{1}=20$ and $\lambda_{2}=1, \beta_{2}=30$, the distributions of $X$ and $Y$ are highly concentrated in the interval $[0.8,1.1]$, i.e.,

$$
P[0.8 \leq X \leq 1.1]=0.9873, \quad P[0.8 \leq Y \leq 1.1]=0.9988
$$

We focus on the function $a_{2}(T)$, the probability of occurrence of one or more failures in $[0, T]$. For $T=1.5$, the system is "always" in the defective state and the inspection avoids a corrective maintenance. Hence, $a_{2}(1.5) \approx 0$. However, for values of inspection near to 1 , the system could be in a defective state or not. If it is not, the next inspection will happen at time $T=2$ and a corrective maintenance could happen in this period. Hence $a_{2}(1)>a_{2}(1.5)$ and the monotony of $a_{2}(T)$ is not guaranteed.

Fig. 5.2. Function $a_{2}(T)$ versus $T$

Next, we specify the costs. Assume $C_{p}=400, C_{c}=1000$ and $C_{I}=100$ be the costs incurred for a preventive maintenance, a corrective maintenance and an inspection, respectively. Furthermore, let $\alpha=0.4$ be the discount factor. For $\lambda_{1}=1, \lambda_{2}=1, \beta_{1}=20$ and $\beta_{2}=30$, Fig. 5.3 displays a simulation of the total expected discounted costs versus $T$. This simulation has been performed using 500 points between 0.2 and 2.5 with 500,000 realizations in each point. As we can see, for this numerical example $C_{\mathrm{d}}(T)$ has several local minimum values. The global minimum of $C_{\mathrm{d}}(T)$ is reached for $T^{*}=1.79$, with an expected discounted costs of $C_{\mathrm{d}}(1.79)=397.68$.

Finally, we specify the safety constraints, first criterion 1. We assume that $\omega_{1}=0.2$ and $A=2$, i.e., the probability of occurrence of one or more failures in two units of time should not exceed 0.2 , that is,

$$
P\left(N_{c}(2) \geq 1\right) \leq 0.2
$$

Figure 5.4 shows the total expected discounted costs $C_{\mathrm{d}}(T)$ along with the function $a_{2}(T)$. We find that

$$
\Upsilon=\left\{T>0 ; \quad a_{2}(T) \leq 0.2\right\}=(0,1.898]
$$

In this case, $T^{*}=1.79 \in \Upsilon$, and hence the optimal value for the constrained optimization problem under criterion 1 is $T_{\text {opt }}=1.79$ with a value of $C_{\mathrm{d}}(1.79)=397.68$

Consider now the constrained optimization problem under criterion 2. We assume that $\omega_{2}=0.15$, i.e., the proportion of time that the system is in a

Fig. 5.3. Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$
defective state should not exceed 0.15 . Figure 5.5 shows the total expected discounted costs and the function $b(T)$ for this problem. In this case

$$
\begin{aligned}
\Upsilon & =\{T>0 ; \quad b(T) \leq 0.15\} \\
& =(0,0.291] \cup[0.3272,0.3823] \cup[0.508,0.5727] \cup[1.041,1.1454]
\end{aligned}
$$

By inspection the optimal value for the constrained optimization problem is $T_{\text {opt }}=1.1454$ with a value of $C_{\mathrm{d}}(1.1454)=687$.

In the following example we use a more realistic set of parameter values of the Weibull distributions: $\lambda_{1}=1, \lambda_{2}=1, \beta_{1}=2$ and $\beta_{2}=3$. In this case

$$
E[X]=0.8862, \quad E[Y]=0.8930
$$

Let $C_{p}=400, C_{c}=1000$ and $C_{I}=100$ be the costs incurred, with $\alpha=0.4$ the discount factor. The functions $C_{\mathrm{d}}(T), a_{A}(T)$ and $b(T)$ are shown in Figs. 5.65.8.

Figure 5.6 shows a simulation of the total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$ for this example. The function $C_{\mathrm{d}}(T)$ is in standard form, nonincreasing up to $T=1.1511$ and nondecreasing for $T \geq 1.1511$. Hence $T^{*}=1.1511$. The corresponding expected discounted costs equal $C_{\mathrm{d}}(1.1511)=804.0365$.

We analyze the constrained optimization problem for each safety requirement. As above we put $\omega_{1}=0.2$ for criterion 1. From Fig. 5.7 we find that

$$
\Upsilon=\{T>0 ; \quad a_{2}(T) \leq 0.2\}=(0,0.975]
$$

Fig. 5.4. (a) Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$. (b) Function $a_{2}(T)$ versus $T$

Due to the form of $C_{\mathrm{d}}(T)$ the optimal value for the constrained optimization is $T_{\text {opt }}=0.975$ with a value of $C_{\mathrm{d}}(0.975)=813.55$.

For criterion 2, we suppose $\omega_{2}=0.15$. From Fig. 5.8,

$$
\Upsilon=\{T>0 ; \quad b(T) \leq 0.15\}=(0,0.313]
$$

and using the same reasoning as above, the optimal value for $C_{\mathrm{d}}(T)$ is reached for $T_{\text {opt }}=0.313$ with a value of $C_{\mathrm{d}}(0.313)=1372$. By comparing the expected costs for the unconstrained and the constrained problem, we see that a rather large cost is introduced by implementing the safety constraint.

Both constraints can be used to control the safety level. However, we prefer to use criterion 1 as it is more directly related to the failures of the system.

# 5.5.2 Optimal Test Interval for a Monotone Safety System 

In this section we consider a safety system represented by a monotone (coherent) structure function of $n$ components. The components and the system can be in one out of several states. The state of the components and the system is only revealed through inspections, which are carried at intervals of length $T$. If the inspection shows that the system is in a critical state or has failed, it is overhauled and all components are resumed to good-as-new conditions. The system is in a critical state if further deterioration of a component (component $i$ jumps from state $j$ to state $j-1$ ) induces system failure. As the system is a safety system in standby position, the state of the system and its components is revealed only by testing. The aim of the testing and overhaul is

Fig. 5.5. (a) Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$. (b) Function $b(T)$ versus $T$
to avoid that the system fails and stays in the failure state for a long period. However, this goal has to be balanced against the costs of inspections and overhauls. Too frequent inspections would not be cost optimal. Costs are associated with tests, system downtime, and repairs. The optimization criterion is the expected long-run cost per unit of time.

Below we present a formal set-up for this problem and show how an optimal $T$ can be determined. A special case where the components have three states is given special attention. It corresponds to a "delay time type system" where the presence of a fault in a component does not lead to an immediate failure; there will be a "delay time" between the occurrence of the fault and the failure of the component. We refer to Sect.5.5.1.

# Model and Problem Definition 

We consider a safety system comprising $n$ components, numbered consecutively from 1 to $n$. The state of component $i$ at time $t, t \geq 0$, is denoted $X_{t}(i)$, $i=1,2, \ldots, n$, where $X_{t}(i)$ can be in one out of $M_{i}+1$ states, $0,1, \ldots, M_{i}$. The paths $X$.(i) are assumed to be right-continuous. The states represent different levels of performance, from the worst, 0 , to the best, $M_{i}$. At time $t=0$, all components are in the best state, i.r., $X_{0}(i)=M_{i}, i=1,2, \ldots, n$. The random duration time in state $M_{i}$ is denoted $U_{i M_{i}}$. The component then jumps to state $M_{i}-1$ for a random time $U_{i\left(M_{i}-1\right)}$, and so on until the component reaches the absorbing state 0 . All sojourn times are positive random variables. The probability distribution of $U_{i j}$ is denoted $F_{i j}$. The distributions $F_{i j}$ are assumed

Fig. 5.6. Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$
absolute continuous, with finite means. The density and "jump rate" of $F_{i j}(t)$ are denoted $f_{i j}(t)$ and $r_{i j}(t)$, respectively, $i=1,2, \ldots, n$ and $j=1,2, \ldots, M_{i}$. The jump rate $r_{i j}(t)$ is defined as usual as

$$
\lim _{h \rightarrow 0} \frac{1}{h} P\left(U_{i j} \leq t+h \mid U_{i j}>t\right)
$$

Hence $r_{i j}(t) h$ ( $h$ a small positive number) is approximately equal to the conditional probability that component $i$ makes a jump to state $j-1$ in the interval $(t, t+h]$ given that the component has stayed in state $j$ during the interval $[0, t]$. The sojourn times $U_{i M_{i}}, U_{i\left(M_{i}-1\right)}, \ldots, U_{i 1}, i=1,2, \ldots, n$, are assumed independent. The distribution of the vector of all $U_{i j} \mathrm{~s}, \mathbf{U}$, is denoted $F_{\mathbf{U}}$.

We denote by $G(t, \mathbf{x})$ the distribution of the vector of component states $\mathbf{X}_{t}=\left(X_{t}(1), X_{t}(2), \ldots, X_{t}(n)\right)$, i.e.,

$$
G(t, \mathbf{x})=P\left(X_{t}(1)=x_{1}, X_{t}(2)=x_{2}, \ldots, X_{t}(n)=x_{n}\right)
$$

Here $\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, where $x_{i} \in\left\{0,1, \ldots, M_{i}\right\}$. The state of the system at time $t$ is denoted $\Phi_{t}$ and is a function of the states of the components, i.e.,

$$
\Phi_{t}=\phi\left(\mathbf{X}_{t}\right)
$$

where $\phi$ is the structure function of the system. We assume that $\Phi$ and $\phi$ are binary, equal to 1 if the system is functioning and 0 otherwise (see Sect. 2.1). The system is a monotone system (see Sect. 2.1.2), i.e., its structure function $\phi$ is nondecreasing in each argument, and

$$
\phi(0,0, \ldots, 0)=0 \quad \text { and } \quad \phi\left(M_{1}, M_{2}, \ldots, M_{n}\right)=1
$$

Fig. 5.7. (a) Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$. (b) Function $a_{2}(T)$ versus $T$

Since at time $t=0$ all components are in the best state, $\Phi(0)=1$. The components deteriorate and at time $\tau$ the system fails, i.e.,

$$
\tau=\inf \left\{t>0: \phi\left(\mathbf{X}_{t}\right)=0\right\}
$$

The deterioration of the components and the system failure is revealed by inspections. It is assumed that the system is inspected every $T$ units of time. If the system is found to be in the failure state, a complete overhaul is carried out meaning that all components are repaired to a good-as-new condition. Furthermore, a preventive policy is introduced: if the system is found to be in a critical state, also a complete overhaul is conducted. The system is said to be in a critical state if the system is functioning and there exists at least one $i$ such that the system fails if component $i$ jumps to the state $X_{t}(i)-1$. Let $\tau_{C}$ be the time to the system first becomes critical. Then

$$
\tau_{C}=\inf \left\{t \geq 0: \phi\left(\mathbf{X}_{t}\right)=1, \phi\left(\left(X_{t}(i)-1\right)_{i}, \mathbf{X}_{t}\right)=0 \text { for at least one } i\right\}
$$

where $\phi\left(\cdot_{i}, \mathbf{x}\right)=\phi\left(x_{1}, \ldots, x_{i-1}, \cdot, x_{i+1}, \ldots, x_{n}\right)$. We assume $\tau_{C}>0$, i.e., the system is not critical at time 0 .

The distribution of $\tau_{C}$ is denoted $F_{\tau_{C}}$. The times $\tau$ and $\tau_{C}$ are functions of the duration times $U_{i j}$. Let $g$ and $g_{C}$ be defined by

$$
\tau=g(\mathbf{U}) \text { and } \tau_{C}=g_{C}(\mathbf{U})
$$

The inspections and overhauls are assumed to take negligible time.
To further characterize the critical states, we introduce the concept of a critical path vector for system level 1:

Fig. 5.8. (a) Total expected discounted costs $C_{\mathrm{d}}(T)$ versus $T$. (b) Function $b(T)$ versus $T$

Definition 5.35. A state vector $\mathbf{x}$ is a critical path vector for system level 1 (the functioning state of the system) if and only if $\phi(\mathbf{x})=1$ and $\phi\left(\left(x_{i}-\right.\right.$ $\left.1)_{i}, \mathbf{x}\right)=0$ for at least one $i$.

From this definition we introduce a maximal critical path vector:
Definition 5.36. A critical path vector $\mathbf{x}$ is a maximal critical path vector for system level 1 if it cannot be increased without losing its status as a critical path vector.

Note that these concepts are different from the common defined path vectors and minimal path vectors in a monotone system; see Sect.2.1.2.

Based on the maximal critical minimal path vectors we introduce a new structure function, $\phi_{C}(\mathbf{x})$, which is equal to 1 if and only if there exists no maximal critical path vector $\mathbf{x}_{k}$ such that the state $\mathbf{x}$ is below or equal to $\mathbf{x}_{k}$, i.e.

$$
\phi_{C}(\mathbf{x})=\prod_{k}\left(1-I\left(\mathbf{x} \leq \mathbf{x}_{k}\right)\right)
$$

where $k$ runs trough all maximal critical path vectors for the system at level 1. We see that the system $\phi_{C}$ fails as soon as a system state becomes critical. As an example, consider a binary parallel system. Then it is seen that the maximal critical path vectors are $(1,0)$ and $(0,1)$, and $\phi_{C}(\mathbf{x})=x_{1} x_{2}$, as if one component fails, the system state becomes critical.

A counting process $N$ is introduced that jumps to 1 at the time of system failure, i.e.,

$$
N_{t}=I(\tau \leq t)
$$Let $V_{i j, t}$ be the virtual age of component $i$ in state $j$ at time $t$. Then the intensity $\lambda_{t}$ of $N$ is given by

$$
\lambda_{t}=\sum_{i=1}^{n} \sum_{j=1}^{M_{i}} r_{i j}\left(V_{i j, t}\right) I\left(X_{t}(i)=j\right) \phi\left(\mathbf{X}_{t}\right)\left(1-\phi\left((j-1)_{i}, \mathbf{X}_{t}\right)\right)
$$

noting that the rate is $r_{i j}\left(V_{i j, t}\right)$ at time $t$ for component $i$ to cause system failure by jumping from state $j$ to state $j-1$. A formal proof can be given following the approach in Sect.3.2.2. By introducing $\phi_{i j}(\mathbf{x})=I\left(x_{i}=\right.$ $j) \phi(\mathbf{x})\left(1-\phi\left((j-1)_{i}, \mathbf{x}\right)\right)$, the intensity $\lambda_{t}$ can be expressed as

$$
\lambda_{t}=\sum_{i=1}^{n} \sum_{j=1}^{M_{i}} r_{i j}\left(V_{i j, t}\right) \phi_{i j}\left(\mathbf{X}_{t}\right)
$$

Analogously, we define a counting process $N_{C}$ for the process $\phi_{C}$. This counting process jumps to 1 at the time the system becomes critical, i.e.,

$$
N_{C, t}=I\left(\tau_{C} \leq t\right)
$$

The intensity $\lambda_{C, t}$ of $N_{C}$ is given by

$$
\lambda_{C, t}=\sum_{i=1}^{n} \sum_{j=1}^{M_{i}} r_{i j}\left(V_{i j, t}\right) I\left(X_{t}(i)=j\right) \phi_{C}\left(\mathbf{X}_{t}\right)\left(1-\phi_{C}\left((j-1)_{i}, \mathbf{X}_{t}\right)\right)
$$

Similarly to $\phi_{i j}$ we define $\phi_{i j C}(\mathbf{x})=I\left(x_{i}=j\right) \phi_{C}(\mathbf{x})\left(1-\phi_{C}\left((j-1)_{i}, \mathbf{x}\right)\right)$, and hence the intensity $\lambda_{C, t}$ can be expressed as

$$
\lambda_{C, t}=\sum_{i=1}^{n} \sum_{j=1}^{M_{i}} r_{i j}\left(V_{i j, t}\right) \phi_{i j C}\left(\mathbf{X}_{t}\right)
$$

The following cost structure is assumed: the cost of a complete overhaul is $c_{p}$, whereas the cost of each inspection is $c_{I}$. If the system is not functioning a cost $c$ is incurred per unit of time. All costs are positive numbers.

The problem is to find an optimal $T$ minimizing the long-run expected cost per unit of time.

# Optimization 

For a fixed test interval length $T, 0<T<\infty$, the system is overhauled at time $\tau^{T}$, where $\tau^{T}$ is the time of the first inspection following a critical state, i.e.,

$$
\tau^{T}=T\left(\left[\tau_{C} / T\right]_{I}+1\right)
$$

where $[x]_{I}$ equals the integer part of $x$. This inspection represents a renewal for the cost and time processes, and using the renewal reward theorem (seeAppendix B.2), it follows that the long-run (expected) cost per unit time, $B^{T}$, can be written:

$$
B^{T}=\frac{E C^{T}}{E \tau^{T}}
$$

where $E \tau^{T}$ expresses the expected length of the first renewal cycle (the time until renewal) and $E C^{T}$ expresses the expected cost associated with this cycle. It is seen that $E \tau^{T}<\infty$ and $E C^{T}<\infty$, observing that $E \tau^{T} \leq \sum_{i j} E U_{i j}+T$, and $E C^{T} \leq T c+c_{p}+C_{I}\left(E \tau^{T} / T+1\right)$. Theorem 5.37 establishes an explicit formula for $E \tau^{T}$ and $E C^{T}$, and hence for $B^{T}$.

Theorem 5.37. Under the above model assumptions, with $\tau=g(\mathbf{U})$ and $\tau_{C}=g_{C}(\mathbf{U})$, we have

$$
\begin{aligned}
E \tau^{T}= & T \sum_{k=0}^{\infty}(k+1) \int_{\mathbf{u}: k T<g_{C}(\mathbf{u}) \leq(k+1) T} d F_{\mathbf{U}}(\mathbf{u}) \\
E C^{T}= & \sum_{k=0}^{\infty} \int_{\mathbf{u}: k T<g_{C}(\mathbf{u}) \leq(k+1) T}\left[c_{I}(k+1)+c_{p}\right. \\
& \left.+c I(g(\mathbf{u}) \leq(k+1) T)\{(k+1) T-g(\mathbf{u})\}\right] d F_{\mathbf{U}}(\mathbf{u})
\end{aligned}
$$

Proof. To establish (5.47), we write

$$
\tau^{T}=\sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)(k+1) T
$$

Then taking expectation we obtain

$$
\begin{aligned}
E \tau^{T} & =E \sum_{k=0}^{\infty} I\left(k T<g_{C}(\mathbf{U}) \leq(k+1) T\right)(k+1) T \\
& =T \sum_{k=0}^{\infty}(k+1) \int_{\mathbf{u}: k T<g_{C}(\mathbf{u}) \leq(k+1) T} d F_{\mathbf{U}}(\mathbf{u})
\end{aligned}
$$

which proves (5.47). To establish (5.48), we use a similar approach writing the cost $C^{T}$ as a function of $\tau_{C}$ and $\tau$ :
$C^{T}=\sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)\left[c_{I}(k+1)+c_{p}+c I(\tau \leq(k+1) T)\{(k+1) T-\tau\}\right]$,
noting that the system is down a period $(k+1) T-\tau$ if the system enters a critical state in the interval $(k T,(k+1) T]$ and the system fails before the inspection at time $(k+1) T$. Then taking expectations we obtain (5.48).

In the following theorem we establish more explicit formulae for $E \tau^{T}$ and $E C^{T}$ by using counting process theory. Then we do not need the distribution of $F_{\mathbf{U}}(\mathbf{u})$ but the distribution of $\mathbf{X}_{t}, G(t, \mathbf{x})$. We consider two special cases:- The system is a binary system with binary components, i.e. $M_{i}=1$ for $i=1,2, \ldots, n$.
- The rates $r_{i j}$ are independent of $t$,
i.e. the sojourn times are all exponentially distributed.

Theorem 5.38. Let

$$
H_{i j}(t, \mathbf{x})=\int_{0}^{t} r_{i j}(s) G(s, \mathbf{x}) d s
$$

For the cases (5.50) and (5.51), we then have

$$
\begin{aligned}
E \tau^{T}= & \sum_{k=0}^{\infty} T(k+1) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j C}(\mathbf{x}) \\
& \times\left[H_{i j}((k+1) T, \mathbf{x})-H_{i j}(k T, \mathbf{x})\right]
\end{aligned}
$$

where $\phi_{i j C}(\mathbf{x})=I\left(x_{i}=j\right) \phi_{C}(\mathbf{x})\left(1-\phi_{C}\left((j-1)_{i}, \mathbf{x}\right)\right)$. Furthermore, if $G_{s}\left(t, \mathbf{x} \mid \mathbf{x}^{\prime}\right)$ denotes the conditional distribution of $\mathbf{X}(t)$ given $\mathbf{X}(s)=\mathbf{x}^{\prime}$ $(t>s)$, we have

$$
\begin{aligned}
E C^{T}= & \sum_{k=0}^{\infty}\left[c_{I}(k+1)+c_{p}\right] \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j C}(\mathbf{x})\left[H_{i j}((k+1) T, \mathbf{x})-H_{i j}(k T, \mathbf{x})\right] \\
& +\sum_{k=0}^{\infty} \sum_{\mathbf{x}^{\prime}} \phi_{C}\left(\mathbf{x}^{\prime}\right) G\left(k T, \mathbf{x}^{\prime}\right) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j}(\mathbf{x}) \\
& \times \int_{k T}^{(k+1) T} c((k+1) T-t) r_{i j}(t) G_{k T}\left(t, \mathbf{x} \mid \mathbf{x}^{\prime}\right) d t
\end{aligned}
$$

Proof. To establish (5.52), we write

$$
\tau^{T}=\sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)(k+1) T=\sum_{k=0}^{\infty}(k+1) T \int_{k T}^{(k+1) T} d N_{C}(t)
$$

Then taking expectation, using that $N_{C, t}$ has intensity $\lambda_{C, t}$, and noting that we can write $r_{i j}\left(V_{i, j, t}\right)=r_{i j}(t)$, we obtain:

$$
\begin{aligned}
E \tau^{T} & =E \sum_{k=0}^{\infty}(k+1) T \int_{k T}^{(k+1) T} d N_{C, t} \\
& =T \sum_{k=0}^{\infty}(k+1) \int_{k T}^{(k+1) T} E \lambda_{C, t} d t
\end{aligned}
$$$$
\begin{aligned}
& =T \sum_{k=0}^{\infty}(k+1) \int_{k T}^{(k+1) T} \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} r_{i j}(t) E \phi_{i j C}\left(\mathbf{X}_{t}\right) d t \\
& =T \sum_{k=0}^{\infty}(k+1) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j C}(\mathbf{x}) \int_{k T}^{(k+1) T} r_{i j}(t) G(t, \mathbf{x}) d t \\
& =T \sum_{k=0}^{\infty}(k+1) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j C}(\mathbf{x})\left[H_{i j}((k+1) T, \mathbf{x})-H_{i j}(k T, \mathbf{x})\right]
\end{aligned}
$$

which proves (5.52). To establish (5.53), we rewrite (5.49) to obtain

$$
\begin{aligned}
E C^{T}= & E \sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)\left[c_{I}(k+1)+c_{p}\right] \\
& +E \sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right) c I(\tau \leq(k+1) T)\{(k+1) T-\tau\}
\end{aligned}
$$

Similarly to the above analysis for $E \tau^{T}$ it is seen that the first term of this expression for $E C^{T}$ equals

$$
\sum_{k=0}^{\infty}\left[c_{I}(k+1)+c_{p}\right] \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \phi_{i j C}(\mathbf{x})\left[H_{i j}((k+1) T, \mathbf{x})-H_{i j}(k T, \mathbf{x})\right]
$$

Hence it remains to establish the desired expression for the downtime costs, the second term. This term can be expressed as

$$
E \sum_{k=0}^{\infty} \phi_{C}\left(\mathbf{X}_{k T}\right) \int_{k T}^{(k+1) T} c((k+1) T-t) d N_{t}
$$

as $\phi_{C}\left(\mathbf{X}_{t}\right)$ is 1 as long as $t<\tau_{C}$. Then using that $N_{t}$ has intensity $\lambda_{t}$, we obtain that this expected cost term equals

$$
\begin{aligned}
& E \sum_{k=0}^{\infty} \phi_{C}\left(\mathbf{X}_{k T}\right) \int_{k T}^{(k+1) T} c((k+1) T-t) d N_{t} \\
& \quad=E \sum_{k=0}^{\infty} \phi_{C}\left(\mathbf{X}_{k T}\right) \int_{k T}^{(k+1) T} c((k+1) T-t) \lambda_{t} d t \\
& \quad=E \sum_{k=0}^{\infty} \phi_{C}\left(\mathbf{X}_{k T}\right) \int_{k T}^{(k+1) T} c((k+1) T-t) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \phi_{i j}\left(\mathbf{X}_{t}\right) r_{i j}(t) d t \\
& \quad=\sum_{k=0}^{\infty} \sum_{\mathbf{x}^{\prime}} \phi_{C}\left(\mathbf{x}^{\prime}\right) G\left(k T, \mathbf{x}^{\prime}\right) \sum_{i=1}^{n} \sum_{j=1}^{M_{i}} \sum_{\mathbf{x}} \phi_{i j}(\mathbf{x}) \times \\
& \quad \int_{k T}^{(k+1) T} c((k+1) T-t) r_{i j}(t) G_{k T}\left(t, \mathbf{x} \mid \mathbf{x}^{\prime}\right) d t
\end{aligned}
$$

Equation (5.53) follows, and the theorem is proved.We seek an optimal $T_{\text {opt }}$ minimizing $B^{T}$ given by (5.46) and the expressions for $E C^{T}$ and $E \tau^{T}$ in Theorems 5.37 and 5.38. Such a minimum always exists if we include the "perform no testing and overhaul" policy $T=\infty$ as $B^{T}$ is a continuous function and $\lim _{T \rightarrow 0} B^{T}=\infty$. We have $B^{\infty}=\lim _{T \rightarrow \infty} B^{T}=$ $c$. The expected average long-run cost per unit of time when there is no testing and overhaul equals $c$. If we perform very frequent testing, the long-run expected average cost will be very high due to a large number of inspections.

To find $T_{\text {opt }}$ it is convenient to search for $T$ s minimizing the functions

$$
B^{T}(\delta)=E C^{T}-\delta E \tau^{T}
$$

If $T_{\delta}$ minimizes $B^{T}(\delta)$ and $B^{T_{\delta}}(\delta)=0$, then $T_{\delta}$ minimizes $B^{T}$, i.e., $T_{\delta}$ is optimal, and $\delta=B^{T_{\delta}}=\inf _{0<T \leq \infty} B^{T}$. This result is well-known from the literature; see Aven and Bergman [19]. We also refer to (5.9).

# Special Case: Parallel System of Two Components 

Assume that $\phi(\mathbf{x})=1-\left(1-x_{1}\right)\left(1-x_{2}\right)$, i.e., the system is a binary parallel system composed of two components. The time to the system first becomes critical, $\tau_{C}$, can then be expressed as

$$
\tau_{C}=\min \left\{U_{11}, U_{21}\right\}
$$

noting that if a component fails, the system is functioning if and only if the other component is functioning. Furthermore, the time to system failure, $\tau$, equals the maximum component lifetime, i.e.,

$$
\tau=\max \left\{U_{11}, U_{21}\right\}
$$

It follows that

$$
\begin{aligned}
E \tau^{T} & =T \sum_{k=0}^{\infty}(k+1)\left[F_{\tau_{C}}((k+1) T)-F_{\tau_{C}}(k T)\right] \\
& =\sum_{k=0}^{\infty}(k+1)\left[\bar{F}_{11}(k T)) \bar{F}_{21}(k T)-\bar{F}_{11}((k+1) T)) \bar{F}_{21}((k+1) T)\right]
\end{aligned}
$$

where $\bar{F}=1-F$. By similar arguments, first considering the costs $c_{I}$ and $c_{p}$, and then for the cost $c$ condition on $U_{11}=u_{1}$ and $U_{21}=u_{2}$, we obtain

$$
\begin{aligned}
E C^{T}= & E \sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right) \\
& \times\left[c_{I}(k+1)+c_{p}+c I(\tau \leq(k+1) T)\{(k+1) T-\tau\}\right] \\
= & E \sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)\left[c_{I}(k+1)+c_{p}\right]+
\end{aligned}
$$$$
\begin{aligned}
& E \sum_{k=0}^{\infty} I\left(k T<\tau_{C} \leq(k+1) T\right)[c I(\tau \leq(k+1) T)\{(k+1) T-\tau\}] \\
= & \sum_{k=0}^{\infty}\left[\bar{F}_{11}(k T) \bar{F}_{21}(k T)-\bar{F}_{11}((k+1) T) \bar{F}_{21}((k+1) T)\right]\left[c_{I}(k+1)+c_{p}\right]+ \\
& \sum_{k=0}^{\infty} \int_{0}^{\infty} \int_{0}^{\infty} I\left(k T<\min \left\{u_{1}, u_{2}\right\}\right. \\
& \leq(k+1) T)\left[c I\left(\max \left\{u_{1}, u_{2}\right\} \leq(k+1) T\right)\right. \\
& \left.\times\left\{(k+1) T-\max \left\{u_{1}, u_{2}\right\}\right\}\right] d F_{21}\left(u_{1}\right) d F_{11}\left(u_{2}\right)
\end{aligned}
$$

The last term due to system downtime can be simplified to

$$
\begin{aligned}
& \sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} c\left\{(k+1) T-u_{1}\right\}\left[F_{21}\left(u_{1}\right)-F_{21}(k T)\right] d F_{11}\left(u_{1}\right) \\
& \quad+\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} c\left\{(k+1) T-u_{2}\right\}\left[F_{11}\left(u_{2}\right)-F_{11}(k T)\right] d F_{21}\left(u_{2}\right)
\end{aligned}
$$

These results are presented in Proposition 5.39.
Proposition 5.39. For a parallel system of two binary components, the expected renewal cycle and expected associated costs are given by:

$$
\begin{aligned}
E \tau^{T}= & \sum_{k=0}^{\infty}(k+1)\left[\bar{F}_{11}(k T) \bar{F}_{21}(k T)-\bar{F}_{11}((k+1) T) \bar{F}_{21}((k+1) T)\right] \\
E C^{T}= & \sum_{k=0}^{\infty}\left[\bar{F}_{11}(k T) \bar{F}_{21}(k T)-\bar{F}_{11}((k+1) T) \bar{F}_{21}((k+1) T)\right]\left[c_{I}(k+1)+c_{p}\right]+ \\
& \sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} c\left\{(k+1) T-u_{1}\right\}\left[F_{21}\left(u_{1}\right)-F_{21}(k T)\right] d F_{11}\left(u_{1}\right)+ \\
& \sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} c\left\{(k+1) T-u_{2}\right\}\left[F_{11}\left(u_{2}\right)-F_{11}(k T)\right] d F_{21}\left(u_{2}\right)
\end{aligned}
$$

An optimal $T$ can then be determined.
Similar expressions can easily be derived based on Theorem 5.38. Note that $\phi_{i 1 C}(\mathbf{x})$ is equal to 1 only if $x_{1}=1$ and $x_{2}=1$.

# Special Case: Delay Time Model with Three Components 

We consider a system comprising $n=3$ components, with $M_{i}=2$, i.e., each component has three states. The state 2 is a perfect functioning state, whereas state 1 is a "partly defective" state, as a result of a "fault." There will be a time lapse between the occurrence of the fault and the failure of the component-a"delay time." To simplify the mathematical analysis, we assume that all sojourn times $U_{i j}$ are exponentially distributed. The constant rates are denoted $r_{i j}$. The components 1 and 2 are assumed to have the same rates. The rates for different arrival states $j$ are assumed different, i.e., $r_{i 2} \neq r_{i 1}$, for $i=1,2,3$.

The state of the system is given by the structure function

$$
\phi(\mathbf{x})=I\left(x_{1}+x_{2} \geq 1\right) I\left(x_{3} \geq 1\right)
$$

Hence the system is functioning if either component 1 or 2 is in state 1 or better, and component 3 is in state 1 or better. We may think of the system as a parallel system comprising the components 1 and 2 , in series with component 3 , with each component having a delay time before failure is occurring.

The maximal critical path vectors for level 1 are $(0,1,2),(1,0,2)$ and $(2,2,1)$, and this defines $\phi_{C}(\mathbf{x})$ and $\phi_{i j C}(\mathbf{x})$. We see that $\phi_{C}(\mathbf{x})=1$ for $\mathbf{x}=(1,1,2)$ and $\mathbf{x}>(1,1,2)$, as well as for $\mathbf{x}=(0,2,2)$ and $\mathbf{x}=(2,0,2)$. and $\phi_{32 C}\left(x_{1}, x_{2}, 2\right)=1, x_{i} \geq 1, i=1,2$.

For two distribution functions $F_{1}$ and $F_{2}$, let $\bar{F}_{1} * F_{2}(t)=\int_{0}^{t} \bar{F}_{1}(t-s) d F_{2}(s)$. Then the distribution $G(t, \mathbf{x})$ can be expressed as:

$$
\begin{aligned}
G(t,(2,2,2)) & =\bar{F}_{12}(t) \bar{F}_{22}(t) \bar{F}_{32}(t)=e^{-t \sum_{i=1}^{3} r_{i 2}} \\
G(t,(1,2,2)) & =\left[\bar{F}_{11} * F_{12}(t)\right] \bar{F}_{22}(t) \bar{F}_{32}(t) \\
& =\frac{r_{12}}{r_{12}-r_{11}}\left(e^{-r_{11} t}-e^{-r_{12} t}\right) e^{-t \sum_{i=2}^{3} r_{i 2}} \\
G(t,(1,1,2)) & =\left[\bar{F}_{11} * F_{12}(t)\right]\left[\bar{F}_{21} * F_{22}(t)\right] \bar{F}_{32}(t) \\
& =\frac{r_{12}}{r_{12}-r_{11}}\left(e^{-r_{11} t}-e^{-r_{12} t}\right) \frac{r_{22}}{r_{22}-r_{21}}\left(e^{-r_{21} t}-e^{-r_{22} t}\right) e^{-t r_{32}} \\
G(t,(0,2,2)) & =F_{12} * F_{11}(t) \bar{F}_{22}(t) \bar{F}_{32}(t) \\
& =\left\{1-e^{-r_{12} t}-\frac{r_{12}}{r_{12}-r_{11}}\left[e^{-r_{11} t}-e^{-r_{12} t}\right]\right\} e^{-t \sum_{i=2}^{3} r_{i 2}}
\end{aligned}
$$

From these expressions compact formulae can be derived for $H_{i j}(t, \mathbf{x})=$ $r_{i j} \int_{0}^{t} G(s, \mathbf{x}) d s$.

Similar equations can be established for $G_{s}\left(t, \mathbf{x} \mid \mathbf{x}^{\prime}\right)$, the conditional distribution of $\mathbf{X}(t)$ given $\mathbf{X}(s)=\mathbf{x}^{\prime}$. We need to compute the conditional distribution of $P\left(X_{t}(i)=j_{2} \mid X_{s}(i)=j_{1}\right)$ for $j_{2} \leq j_{1}, j_{1}=1,2, i=1,2$. We see that $P\left(X_{t}(i)=2 \mid X_{s}(i)=2\right)=\bar{F}_{i 2}(t-s), P\left(X_{t}(i)=1 \mid X_{s}(i)=2\right)=\bar{F}_{11} * F_{12}(t-s)$, and $P\left(X_{t}(i)=1 \mid X_{s}(i)=1\right)=\bar{F}_{i 1}(t-s)$. Furthermore; $P\left(X_{t}(i)=0 \mid X_{s}(i)=\right.$ $1)=F_{i 1}(t-s)$ and $P\left(X_{t}(i)=0 \mid X_{s}(i)=2\right)=F_{12} * F_{i 1}(t-s)$. From these formulae we see for example that

$$
\begin{aligned}
G_{s}(t,(2,2,2) \mid(2,2,2)) & =\bar{F}_{12}(t-s) \bar{F}_{22}(t-s) \bar{F}_{32}(t-s)=e^{-(t-s) \sum_{i=1}^{3} r_{i 2}} \\
G_{s}(t,(1,2,2) \mid(2,2,2)) & =\left[\bar{F}_{11} * F_{12}(t-s)\right] \bar{F}_{22}(t-s) \bar{F}_{32}(t-s) \\
& =\frac{r_{12}}{r_{12}-r_{11}}\left(e^{-r_{11}(t-s)}-e^{-r_{12}(t-s)}\right) e^{-(t-s) \sum_{i=2}^{3} r_{i 2}}
\end{aligned}
$$In this way all terms in $E \tau^{T}$ and $E C^{T}$ can be derived and an optimal $T$ determined.

# Numerical Example 

We assume that the failure rates are as follows: $r_{12}=r_{22}=0.5, r_{11}=r_{21}=$ 1.0 and $r_{32}=1 / 3, r_{31}=1 / 2$. Hence the expected time to failure for the three components are $2+1=3,2+1=3$ and $3+2=5$, respectively. The following costs are assumed: $c=100, c_{I}=1$ and $c_{p}=5$, i.e., the cost of an overhaul is five times the inspection cost and the unit downtime cost is 100 times the inspection cost. Then we can compute the $B^{T}$ function and determine an optimal inspection time. Figure 5.9 shows the $B^{T}$ function as a function of $T$, computed using Maple 10. By inspection an optimal value is obtained for $T=0.43$. A number of sensitivity analysis should be performed to see the effect of changes in the input data. Figure 5.10 shows an example where the unit downtime cost is increased by a factor 10 , from 100 to 1,000 , to reflect the serious safety risk caused by downtime. The optimal inspection interval is then reduced to 0.18 .


Fig. 5.9. The $B^{T}$ function for the base case example with $c=100$# Final Remarks 

The optimization of $B^{T}$ needs to be carried out by numerical methods. For the numerical example considered in the previous section, the optimization criterion is on the standard form seen for many maintenance models (nonincreasing up to a minimum value and then nondecreasing). In general this is, however, not the case for the model studied in this chapter. Examples can be constructed where the optimization function has several local minimum values, which is in line with the examples for a one component system in Sect.5.5.1.

The model can be extended in many ways, for example, by allowing a more general cost structure. As an example we may distinguish between the cost of an overhaul when the system is in a critical state and when it has failed. The calculations of $E C^{T}$ in (5.49) then need to be modified, by considering a cost term $c_{p}+c_{p}^{\prime} I(\tau<(k+1) T)$, where $c_{p}^{\prime}$ is the additional overhaul cost if the system has failed compared to being in a critical state. The further analysis is analogous to the one carried out for $E C^{T}$. The next step would be to allow the overhaul cost to depend on the state vector. The analysis would then become more complicated, but still within the framework and approach presented.


Fig. 5.10. The $B^{T}$ function for $\mathrm{c}=1000$Bibliographic Notes. A fundamental reference for basic replacement models is Barlow and Proschan [31]. There is an extensive literature about preventive replacement models, which is surveyed in the overviews of Pierskalla and Voelker [130], Sherif and Smith [144], Valdez-Flores and Feldman [158], and Jensen [94]. Block and Savits [47] and Boland and Proschan [49] give overviews over comparison methods and stochastic order in reliability theory. Shaked and Szekli [142] and Last and Szekli [116] compare replacement policies via point process methods. A good source for overviews of the vastly increasing literature on replacement and maintenance optimization models is the book Reliability and Maintenance of Complex Systems edited by Özekici in the NATO ASI Series.

The presentation in Sect. 5.2 follows the lines of [96]. A general set-up for cost-minimizing problems is introduced in Jensen [96] similar to Bergman [38] and Aven and Bergman [19]. It allows for specialization in different directions. As an example the model presented by Aven [18] covering the total expected discounted costs criterion is included. What goes beyond the results in [19] is the possibility to take different information levels into account.

There are lots of multivariate extensions of the univariate exponential distribution, for an overview see Hutchinson and Lai [91] or Basu [33], which also cover the models of Freund [68] and Marshall and Olkin [121]. A detailed derivation, statistical properties, and methods of parameter estimation of the combined exponential distribution can be found in [83]. The optimization problem also for more general cost structures is treated in Heinrich and Jensen [85]. An alternative approach to solve optimization problems of the kind treated in this chapter is to use Markov decision processes. It has not been within the scope of this book to develop this theory here. An introduction to this theory can be found in the books of Puterman [131], Bertsekas [41], Davis [59], and Van der Duyn Schouten [159], which also contains applications in reliability.

An overview of several problems related to burn-in and the corresponding literature is given in the review articles by Block and Savits [46], Kuo and Kuo [113], and Leemis and Beneke [118]. The problem of sequential burn-in, where the failures of the items are observed and the burn-in time depends on these failures, is treated in the article of Marcus and Blumenthal [120]. In the papers of Costantini and Spizzichino [56] and Spizzichino [149] the assumption that the component lifelengths are independent is dropped and replaced by certain dependence models.

The problem of finding optimal replacement times for general repair processes has been treated by Aven in [12, 15]. The presentation of Markovmodulated minimal repair processes follows the lines of $[93,95]$ which include the technical details. A similar model considering interest rates has been investigated by Schöttl [137].

Section 5.5 is based on Aven and Castro [20] and Aven [10]. For reviews of the literature on delay time models, see Baker and Christer [29], Christer and Redmond [54] and Christer [53].# Background in Probability and Stochastic Processes 

This appendix serves as background for Chaps. 3-5. The focus is on stochastic processes on the positive real time axis $\mathbb{R}_{+}=[0, \infty)$. Our aim is to give that basis of the measure-theoretic framework that is necessary to make the text intelligible and accessible to those who are not familiar with the general theory of stochastic processes. For detailed presentations of this framework we recommend texts like Dellacherie and Meyer [61, 62], Rogers and Williams [133], and Kallenberg [101]. The point process theory is treated in Karr [103], Daley and Vere-Jones [58], and Brémaud [50]. A "nontechnical" introduction to parts of the general theory accompanied by comprehensive historical and bibliographic remarks can be found in Chap. II of the monograph of Andersen et al. [2]. A good introduction to basic results of probability theory is Williams [164].

## A. 1 Basic Definitions

We use the following notation
$\mathbb{N}=\{1,2, \ldots\}$
$\mathbb{N}_{0}=\{0,1,2, \ldots\}$
$\mathbb{Z}=\{0,+1,-1,+2,-2, \ldots\}$ set of integers
$\mathbb{Q}=\left\{\frac{p}{q}: p \in \mathbb{Z}, q \in \mathbb{N}\right\}$ set of rationals
$\mathbb{R}=(-\infty,+\infty)$ set of real numbers
$\mathbb{R}_{+}=[0, \infty)$ set of nonnegative real numbers
$f \vee g$ and $f \wedge g$ denote $\max \{f, g\}$ and $\min \{f, g\}$, respectively, where $f$ and $g$ can be real-valued functions or real numbers. We denote $f^{+}=f \vee 0$ and $f^{-}=-(f \wedge 0)$.
$\inf \emptyset=\infty, \sup \emptyset=0$. Ratios of the form $\frac{0}{0}$ are set equal to 0 .
A function $f$ from a set $A$ to a set $B$ is denoted by $f: A \rightarrow B$ and $f(a)$ is the value of $f$ at $a \in A$. To simplify the notation we also speak of $f(a)$ as a function.For a function $f: \mathbb{R} \rightarrow \mathbb{R}$ we denote the left and right limit at $a$ (in the case of existence) by

$$
\begin{aligned}
& f(a-)=\lim _{t \rightarrow a-} f(t)=\lim _{h \rightarrow 0, h>0} f(a-h) \\
& f(a+)=\lim _{t \rightarrow a+} f(t)=\lim _{h \rightarrow 0, h>0} f(a+h)
\end{aligned}
$$

For two functions $f, g: \mathbb{R} \rightarrow \mathbb{R}$ we write $f(h)=o(g(h)), h \rightarrow h_{0}$, for some $h_{0} \in \mathbb{R} \cup\{\infty\}$, if

$$
\lim _{h \rightarrow h_{0}} \frac{f(h)}{g(h)}=0
$$

we write $f(h)=O(g(h)), h \rightarrow h_{0}$, for some $h_{0} \in \mathbb{R} \cup\{\infty\}$, if

$$
\limsup _{h \rightarrow h_{0}} \frac{|f(h)|}{|g(h)|}<\infty
$$

An integral $\int f(s) d s$ of a real-valued measurable function is always an integral with respect to Lebesgue-measure. Integrals over finite intervals $\int_{a}^{b}$, $a \leq b$, are always integrals $\int_{[a, b]}$ over the closed interval $[a, b]$.

The indicator function of a set $A$ taking only the values 1 and 0 is denoted $I(A)$. This notation is preferred rather than $I_{A}$ or $I_{A}(a)$ in the case of descriptions of sets $A$ by means of random variables.

In the following we always refer to a basic probability space $(\Omega, \mathcal{F}, P)$, where

- $\Omega$ is a fixed nonempty set.
- $\mathcal{F}$ is a $\sigma$-algebra or $\sigma$-field on $\Omega$, i.e., a collection of subsets of $\Omega$ including $\Omega$, which is closed under countable unions and finite differences.
- $P$ is a probability measure on $(\Omega, \mathcal{F})$, i.e., a $\sigma$-additive, $[0,1]$-valued function on $\mathcal{F}$ with $P(\Omega)=1$.
If $\mathcal{A}$ is a collection of subsets of $\Omega$, then $\sigma(\mathcal{A})$ denotes the smallest $\sigma$ algebra containing $\mathcal{A}$, the $\sigma$-algebra generated by $\mathcal{A}$.

If $S$ is some set and $\mathcal{S}$ a $\sigma$-algebra of subsets of $S$, then the pair $(S, \mathcal{S})$ is called a measurable space. Let $S$ be a metric space (usually $\mathbb{R}$ or $\mathbb{R}^{n}$ ) and $\mathcal{O}$ the collection of its open sets. Then the $\sigma$-algebra generated by $\mathcal{O}$ is called Borel- $\sigma$-algebra and denoted $\mathcal{B}(S)$, especially we denote $\mathcal{B}=\mathcal{B}(\mathbb{R})$.

If $\mathcal{A}$ and $\mathcal{C}$ are two sub- $\sigma$-algebras of $\mathcal{F}$, then $\mathcal{A} \vee \mathcal{C}$ denotes the $\sigma$-algebra generated by the union of $\mathcal{A}$ and $\mathcal{C}$. The product $\sigma$-algebra of $\mathcal{A}$ and $\mathcal{C}$, generated by the sets $A \times C$, where $A \in \mathcal{A}$ and $C \in \mathcal{C}$, is denoted $\mathcal{A} \otimes \mathcal{C}$.

# A. 2 Random Variables, Conditional Expectations 

## A.2.1 Random Variables and Expectations

On the fixed probability space $(\Omega, \mathcal{F}, P)$ we consider a mapping $X$ into the measurable space $(\mathbb{R}, \mathcal{B})$. If $X$ is measurable (or more exactly $\mathcal{F}$- $\mathcal{B}$ measurable), i.e., $X^{-1}(\mathcal{B})=\left\{X^{-1}(B): B \in \mathcal{B}\right\} \subset \mathcal{F}$, then it is called arandom variable. The $\sigma$-algebra $\sigma(X)=X^{-1}(\mathcal{B})$ is the smallest one with respect to which $X$ is measurable. It is called the $\sigma$-algebra generated by $X$.

# Definition A. 1 (Independence). 

(i) Two events $A, B \in \mathcal{F}$ are called independent, if $P(A \cap B)=P(A) P(B)$.
(ii) Suppose $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$ are subfamilies of $\mathcal{F}: \mathcal{A}_{1}, \mathcal{A}_{2} \subset \mathcal{F}$. Then $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$ are called independent, if $P\left(A_{1} \cap A_{2}\right)=P\left(A_{1}\right) P\left(A_{2}\right)$ for all $A_{1} \in \mathcal{A}_{1}$, $A_{2} \in \mathcal{A}_{2}$.
(iii) Two random variables $X$ and $Y$ on $(\Omega, \mathcal{F})$ are called independent, if $\sigma(X)$ and $\sigma(Y)$ are independent.

The expectation $E X$ (or $E[X]$ ) of a random variable is defined in the usual way as the integral $\int X d P$ with respect to the probability measure $P$. If the expectation $E|X|$ is finite, we call $X$ integrable. The law or distribution of $X$ on $(\mathbb{R}, \mathcal{B})$ is given by $F_{X}(B)=P(X \in B), B \in \mathcal{B}$, and $F_{X}(t)=F_{X}((-\infty, t])$ is the distribution function. Often the index $X$ in $F_{X}$ is omitted when it is clear which random variable is considered. Let $g: \mathbb{R} \rightarrow \mathbb{R}$ be a measurable function and suppose that $g(X)$ is integrable. Then

$$
E g(X)=\int_{\Omega} g(X) d P=\int_{\mathbb{R}} g(t) d F_{X}(t)
$$

If $X$ has a density $f_{X}: \mathbb{R} \rightarrow \mathbb{R}_{+}$, i.e., $P(X \in B)=\int_{B} f_{X}(t) d t, B \in \mathcal{B}$, then the expectation can be calculated as

$$
E g(X)=\int_{\mathbb{R}} g(t) f_{X}(t) d t
$$

The variance of a random variable $X$ with $E\left[X^{2}\right]<\infty$ is denoted $\operatorname{Var}[X]$ and defined by $\operatorname{Var}[X]=E\left[(X-E X)^{2}\right]$.

We now present some classical inequalities:

- Markov inequality: Suppose that $X$ is a random variable and $g: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$ a measurable nondecreasing function such that $g(|X|)$ is integrable. Then for any real $c>0$

$$
E g(|X|) \geq g(c) P(|X| \geq c)
$$

- Jensen's inequality: Suppose that $g: \mathbb{R} \rightarrow \mathbb{R}$ is a convex function and that $X$ is a random variable such that $X$ and $g(X)$ are integrable. Then

$$
g(E X) \leq E g(X)
$$

- Hölder's inequality: Let $p, q \in \mathbb{R}$ such that $p>1$ and $1 / p+1 / q=1$. Suppose $X$ and $Y$ are random variables such that $|X|^{p}$ and $|Y|^{q}$ are integrable. Then $X Y$ is integrable and

$$
E|X Y| \leq E\left[|X|^{p}\right]^{1 / p} E\left[|Y|^{q}\right]^{1 / q}
$$

Taking $p=q=2$ this inequality reduces to Schwarz's inequality.- Minkowski's inequality: Suppose that $X$ and $Y$ are random variables such that $|X|^{p}$ and $|Y|^{p}$ are integrable for some $p \geq 1$. Then we have the triangle law

$$
E\left[|X+Y|^{p}\right]^{1 / p} \leq E\left[|X|^{p}\right]^{1 / p}+E\left[|Y|^{p}\right]^{1 / p}
$$

At the end of this section we list some types of convergence of real-valued random variables. Let $X, X_{n}, n \in \mathbb{N}$, be random variables carried by the triple $(\Omega, \mathcal{F}, P)$ and taking values in $(\mathbb{R}, \mathcal{B})$ with distribution functions $F, F_{n}$. Then the following forms of convergence $X_{n} \rightarrow X$ are fundamental in probability theory.

- Almost sure convergence: We say $X_{n} \rightarrow X$ almost surely ( $P$-a.s.) if

$$
P\left(\lim _{n \rightarrow \infty} X_{n}=X\right)=1
$$

- Convergence in probability: We say $X_{n} \xrightarrow{P} X$ in probability, if for every $\epsilon>0$,

$$
\lim _{n \rightarrow \infty} P\left(\left|X_{n}-X\right|>\epsilon\right)=0
$$

- Convergence in distribution: We say $X_{n} \xrightarrow{D} X$ in distribution, if for every $x$ of the set of continuity points of $F$,

$$
\lim _{n \rightarrow \infty} F_{n}(x)=F(x)
$$

- Convergence in the pth mean or convergence in $L^{p}$ : We say $X_{n} \rightarrow X$ in the $p$ th mean, $p \geq 1$, or in $L^{p}$, if $|X|^{p},\left|X_{n}\right|^{p}$ are integrable and

$$
\lim _{n \rightarrow \infty} E\left|X_{n}-X\right|^{p}=0
$$

The relationships between these forms of convergence are the following:

$$
\begin{aligned}
X_{n} \rightarrow X, P \text {-a.s. } & \Rightarrow X_{n} \xrightarrow{P} X \\
X_{n} \rightarrow X \text { in } L^{p} & \Rightarrow X_{n} \xrightarrow{P} X \\
X_{n} \xrightarrow{P} X & \Rightarrow X_{n} \xrightarrow{D} X
\end{aligned}
$$

# A.2.2 $L^{p}$-Spaces and Conditioning 

We introduce the vector spaces $L^{p}=L^{p}(\Omega, \mathcal{F}, P), p \geq 1$, of (equivalence classes of) random variables $X$ such that $|X|^{p}$ is integrable, without distinguishing between random variables $X, Y$ with $P(X=Y)=1$. With the norm $\|X\|_{p}=\left(E|X|^{p}\right)^{1 / p}$ the space $L^{p}$ becomes a complete space in that for any Cauchy sequence $\left(Y_{n}\right), n \in \mathbb{N}$, there exists a $Y \in L^{p}$ such that $\left\|Y_{n}-Y\right\|_{p} \rightarrow 0$ for $n \rightarrow \infty$. A sequence $\left(Y_{n}\right)$ is called Cauchy sequence if

$$
\sup _{r, s \geq k}\left\|Y_{r}-Y_{s}\right\|_{p} \rightarrow 0 \text { for } k \rightarrow \infty
$$$L^{p}$ is a complete and metric vector space or Banach space. For $1 \leq p \leq q$ and $X \in L^{q}$ it follows by Jensen's inequality that

$$
\|X\|_{p} \leq\|X\|_{q}
$$

So $L^{q}$ is a subspace of $L^{p}$ if $q \geq p$. For $p=2$ we define the scalar product $\langle X, Y\rangle=E[X Y]$, which makes $L^{2}$ a Hilbert space, i.e., a Banach space with a norm induced by a scalar product.

We have introduced $L^{p}$-spaces to be able to look at conditional expectations from a geometrical point of view. Before we give a formal definition of conditional expectations, we consider the orthogonal projection in Hilbert spaces.

Theorem A.2. Let $K$ be a complete vector subspace of $L^{2}$ and $X \in L^{2}$. Then there exists $Y$ in $K$ such that
(i) $\|X-Y\|_{2}=\inf \left\{\|X-Z\|_{2}: Z \in K\right\}$
(ii) $X-Y \perp Z$, i.e., $E[(X-Y) Z]=0$, for all $Z \in K$.

Properties (i) and (ii) are equivalent and if $Y^{*}$ shares either property (i) or (ii) with $Y$, then $P\left(Y=Y^{*}\right)=1$.

The short proof of this result can be found in Williams [164]. The theorem states that there is one unique element in the subspace $K$ that has the shortest distance from a given element in $L^{2}$ and the projection direction is orthogonal on $K$. A similar projection can be carried out from $L^{1}(\Omega, \mathcal{F}, P)$ onto $L^{1}(\Omega, \mathcal{A}, P)$, where $\mathcal{A} \subset \mathcal{F}$ is some sub- $\sigma$-algebra of $\mathcal{F}$. Of course, any $\mathcal{A}$-measurable random variable of $L^{1}(\Omega, \mathcal{A}, P)$ is also in $L^{1}(\Omega, \mathcal{F}, P)$. Thus, for a given $X$ in $L^{1}(\Omega, \mathcal{F}, P)$, we are looking for the "best" approximation in $L^{1}(\Omega, \mathcal{A}, P)$. A solution to this problem is given by the following fundamental theorem and definition.

Theorem A.3. Let $X$ be a random variable in $L^{1}(\Omega, \mathcal{F}, P)$ and let $\mathcal{A}$ be a sub- $\sigma$-algebra of $\mathcal{F}$. Then there exists a random variable $Y$ in $L^{1}(\Omega, \mathcal{A}, P)$ such that

$$
\int_{A} Y d P=\int_{A} X d P, \text { for all } A \in \mathcal{A}
$$

If $Y^{*}$ is another random variable in $L^{1}(\Omega, \mathcal{A}, P)$ with property (A.1), then $P\left(Y=Y^{*}\right)=1$.

A random variable $Y \in L^{1}(\Omega, \mathcal{A}, P)$ with property (A.1) is called (a version of) the conditional expectation $E[X \mid \mathcal{A}]$ of $X$ given $\mathcal{A}$. We write $Y=E[X \mid \mathcal{A}]$ noting that equality holds $P$-a.s.

The standard proof of this theorem uses the Radon-Nikodym theorem (cf. for example Billingsley [42]). A more constructive proof is via the Orthogonal Projection Theorem A.2. In the case that $E X^{2}<\infty$, i.e., $X \in L^{2}(\Omega, \mathcal{F}, P)$, we can use Theorem A. 2 directly with $K=L^{2}(\Omega, \mathcal{A}, P)$. Let $Y$ be the projectionof $X$ in $K$. Then property (ii) of Theorem A. 2 yields $E[(X-Y) Z]=0$ for all $Z \in K$. Take $Z=I_{A}, A \in \mathcal{A}$. Then $E\left[(X-Y) I_{A}\right]=0$ is just condition (A.1), which shows that $Y$ is a version of the conditional expectation $E[X \mid \mathcal{A}]$. If $X$ is not in $L^{2}$, we split $X$ as $X^{+}-X^{-}$and approximate both parts by sequences $X_{n}^{+}=X^{+} \wedge n$ and $X_{n}^{-}=X^{-} \wedge n, n \in \mathbb{N}$, of $L^{2}$-random variables. A limiting argument for $n \rightarrow \infty$ yields the desired result (see [164] for a complete proof).

Conditioning with respect to a $\sigma$-algebra is in general not very concrete, so the idea of projecting onto a subspace may give some additional insight. Another point of view is to look at conditioning as an averaging operator. The sub- $\sigma$-algebra $\mathcal{A}$ lies between the extremes $\mathcal{F}$ and $\mathcal{G}=\{\emptyset, \Omega\}$, the trivial $\sigma$-field. As can be easily verified from the definition, the corresponding conditional expectations of $X$ are $X=E[X \mid \mathcal{F}]$ and $E X=E[X \mid \mathcal{G}]$. So for $\mathcal{A}$ with $\mathcal{G} \subset \mathcal{A} \subset \mathcal{F}$ the conditional expectation $E[X \mid \mathcal{A}]$ lies "between" $X$ (no averaging, complete information about the value of $X$ ) and $E X$ (overall average, no information about the value of $X$ ). The more events of $\mathcal{F}$ are included in $\mathcal{A}$ the more is $E[X \mid \mathcal{A}]$ varying and the closer is this conditional expectation to $X$ in a sense made precise in the following proposition.

Proposition A.4. Suppose $X \in L^{2}(\Omega, \mathcal{F}, P)$ and let $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$ be sub- $\sigma$ algebras of $\mathcal{F}$ such that $\mathcal{A}_{1} \subset \mathcal{A}_{2} \subset \mathcal{F}$. Then, denoting $Y_{i}=E\left[X \mid \mathcal{A}_{i}\right], i=1,2$, we have the following inequalities:
(i) $\left\|X-Y_{2}\right\|_{2} \leq\left\|X-Y_{1}\right\|_{2} \leq\left\|X-Y_{2}\right\|_{2}+\left\|Y_{2}-Y_{1}\right\|_{2}$.
(ii) $\left\|Y_{1}-E X\right\|_{2} \leq\left\|Y_{2}-E X\right\|_{2} \leq\left\|Y_{1}-E X\right\|_{2}+\left\|Y_{2}-Y_{1}\right\|_{2}$.

Proof. The right-hand side inequalities are just special cases of the triangle law for the $L^{2}$-norm or Minkowski's inequality. So we need to prove the lefthand inequalities.
(i) Since $Y_{2}$ is the projection of $X$ on $L^{2}\left(\Omega, \mathcal{A}_{2}, P\right)$ and

$$
Y_{1} \in L^{2}\left(\Omega, \mathcal{A}_{1}, P\right) \subset L^{2}\left(\Omega, \mathcal{A}_{2}, P\right)
$$

we can use Theorem A. 2 to yield

$$
\left\|X-Y_{2}\right\|_{2}=\inf \left\{\|X-Z\|_{2}: Z \in L^{2}\left(\Omega, \mathcal{A}_{2}, P\right)\right\} \leq\left\|X-Y_{1}\right\|_{2}
$$

(ii) Denoting $\tilde{Y}_{i}=Y_{i}-E X$ we see that $\tilde{Y}_{1}$ is the projection of $\tilde{Y}_{2}$ on $L^{2}\left(\Omega, \mathcal{A}_{1}, P\right)$. Again from Theorem A. 2 it follows that $\tilde{Y}_{2}-\tilde{Y}_{1}$ and $\tilde{Y}_{1}$ are orthogonal. The Pythagoras Theorem then takes the form

$$
\left\|\tilde{Y}_{2}\right\|_{2}^{2}=\left\|\tilde{Y}_{2}-\tilde{Y}_{1}+\tilde{Y}_{1}\right\|_{2}^{2}=\left\|\tilde{Y}_{2}-\tilde{Y}_{1}\right\|_{2}^{2}+\left\|\tilde{Y}_{1}\right\|_{2}^{2}
$$

which gives $\left\|\tilde{Y}_{1}\right\|_{2} \leq\left\|\tilde{Y}_{2}\right\|_{2}$.
Remark A.5. 1. Using some of the properties of conditional expectations stated below, all the inequalities but the first in (i) of the proposition can be shown to hold also in $L^{p}$-norm, $p \geq 1$, provided that $X \in L^{p}$.2. If we view $E[X \mid \mathcal{A}]$ as a predictor of the unknown $X$, then Proposition A. 4 says that the closer $\mathcal{A}$ is to $\mathcal{F}$ the better in the mean square sense is this estimate and the bigger is the variance $\operatorname{Var}[E[X \mid \mathcal{A}]]$ of this random variable.

In particular, if $\mathcal{A}$ is generated by a finite or countable partition of $\Omega$, then the conditional expectation can be given explicitly.

Theorem A.6. Let $X$ be an integrable random variable, i.e., $X \in L^{1}$, and let $\mathcal{A}$ be a sub- $\sigma$-algebra of $\mathcal{F}$ generated by a finite or countable partition $A_{1}, A_{2}, \ldots$ of $\Omega$. Then,

$$
E[X \mid \mathcal{A}]=\frac{1}{P\left(A_{i}\right)} \int_{A_{i}} X d P=\frac{E\left[I_{A_{i}} X\right]}{P\left(A_{i}\right)}, \omega \in A_{i}, P\left(A_{i}\right)>0
$$

If $P\left(A_{i}\right)=0$, the value of $E[X \mid \mathcal{A}]$ over $A_{i}$ is set to 0 .

# A.2.3 Properties of Conditional Expectations 

Here and in the following relations like $<, \leq,=$ between random variables are always assumed to hold with probability one and the term $P$-a.s. is suppressed. All random variables in this subsection are assumed to be integrable, i.e., to be elements of $L^{1}(\Omega, \mathcal{F}, P)$. Let $\mathcal{A}$ and $\mathcal{C}$ denote sub- $\sigma$-algebras of $\mathcal{F}$. Then the following properties for conditional expectations hold true.

1. If $Y$ is any version of $E[X \mid \mathcal{A}]$, then $E Y=E X$.
2. If $X$ is $\mathcal{A}$-measurable $(\sigma(X) \subset \mathcal{A})$, then $E[X \mid \mathcal{A}]=X$.
3. Linearity. $E[a X+b Y \mid \mathcal{A}]=a E[X \mid \mathcal{A}]+b E[Y \mid \mathcal{A}], a, b \in \mathbb{R}$.
4. Monotonicity. If $X \leq Y$, then $E[X \mid \mathcal{A}] \leq E[Y \mid \mathcal{A}]$.
5. Monotone Convergence. If $X_{n}$ is an increasing sequence and $X_{n} \rightarrow X$ $P$-a.s., then $E\left[X_{n} \mid \mathcal{A}\right]$ converges almost surely:

$$
\lim _{n \rightarrow \infty} E\left[X_{n} \mid \mathcal{A}\right]=E[X \mid \mathcal{A}]
$$

6. Dominated Convergence. If $X_{n}$ is a sequence of random variables such that $\sup \left|X_{n}\right|$ is integrable and $X_{n} \rightarrow X P$-a.s., then $E\left[X_{n} \mid \mathcal{A}\right]$ converges almost surely:

$$
\lim _{n \rightarrow \infty} E\left[X_{n} \mid \mathcal{A}\right]=E[X \mid \mathcal{A}]
$$

7. Jensen's Inequality. If $g: \mathbb{R} \rightarrow \mathbb{R}$ is convex and $g(X)$ is integrable, then

$$
E[g(X) \mid \mathcal{A}] \geq g(E[X \mid \mathcal{A}])
$$

in particular

$$
\|X\|_{p} \geq\|E[X \mid \mathcal{A}]\|_{p}, \text { for } p \geq 1
$$

8. Successive Conditioning. If $\mathcal{H}$ is a sub- $\sigma$-algebra of $\mathcal{A}$, then

$$
E[E[X \mid \mathcal{A}] \mid \mathcal{H}]=E[X \mid \mathcal{H}]
$$9. Factoring. Let the random variable $Z$ be $\mathcal{A}$-measurable and suppose that $Z X$ is integrable. Then

$$
E[Z X \mid \mathcal{A}]=Z E[X \mid \mathcal{A}]
$$

10. Independent Conditioning. Let $\mathcal{C}$ and $\mathcal{A}$ be sub- $\sigma$-algebras of $\mathcal{F}$ such that $\mathcal{C}$ is independent of $\sigma(X) \vee \mathcal{A}$. Then

$$
E[X \mid \mathcal{C} \vee \mathcal{A}]=E[X \mid \mathcal{A}]
$$

In particular, if $X$ is independent of $\mathcal{C}$, then $E[X \mid \mathcal{C}]=E X$.
The proofs of all these properties are mainly based on the definition of the conditional expectation and follow the ideas of the corresponding proofs for unconditional expectations, e.g., for monotone and dominated convergence (cf. Williams [164], pp. 89-90).

# A.2.4 Regular Conditional Probabilities 

We define the conditional probability of an event $A \in \mathcal{F}$, given a sub- $\sigma$-algebra $\mathcal{A}$ as

$$
P(A \mid \mathcal{A})=E\left[I_{A} \mid \mathcal{A}\right]
$$

Clearly, by the monotonicity, linearity, and monotone convergence properties we have

$$
\begin{gathered}
0 \leq P(A \mid \mathcal{A}) \leq 1 \\
P(\Omega \mid \mathcal{A})=1
\end{gathered}
$$

and

$$
P\left(\bigcup_{n=1}^{\infty} A_{n} \mid \mathcal{A}\right)=\sum_{n=1}^{\infty} P\left(A_{n} \mid \mathcal{A}\right)
$$

for a fixed sequence $A_{1}, A_{2}, \ldots$ of disjoint events of $\mathcal{F}$. From this we cannot conclude that for almost all $\omega \in \Omega$ the map $A \longmapsto P(A \mid \mathcal{A})(\omega)$ defines a probability on $\mathcal{F}$. Although we often dispense with a discussion of $P$-zero sets, it is important here. For example, the last equation showing the $\sigma$-additivity of conditional probability only holds with probability 1. Except in trivial cases, there are uncountable many sequences of disjoint events and each of these sequences determines an exceptional $P$-zero set. The union of all these exceptional sets need not have probability 0 (it need not even be an element of $\mathcal{F}$ ). But fortunately, for most cases encountered in applications there exists a so-called regular conditional probability.

Definition A.7. A map $Q: \Omega \times \mathcal{F} \rightarrow[0,1]$ is called regular conditional probability given $\mathcal{A} \subset \mathcal{F}$, if
(i) for all $A \in \mathcal{F}, \omega \longmapsto Q(\omega, A)$ is a version of $E\left[I_{A} \mid \mathcal{A}\right]$;
(ii) there exists some $N_{0} \in \mathcal{F}, P\left(N_{0}\right)=0$ such that the map $A \longmapsto Q(\omega, A)$ is a probability measure on $\mathcal{F}$ for all $\omega \notin N_{0}$.# A.2.5 Computation of Conditional Expectations 

Besides the simple case of a sub- $\sigma$-algebra $\mathcal{A}$ generated by a countable partition of $\Omega$ mentioned in Theorem A.6, we consider two further ways to determine conditional expectations $E[X \mid \mathcal{A}]$.

1. If there exists a regular conditional probability $Q$ given $\mathcal{A}$, we can determine the conditional distribution $Q_{X}$ of a random variable $X$ given $\mathcal{A}$ : $Q_{X}(\omega, B)=Q\left(\omega, X^{-1}(B)\right)$. Then for any measurable function $g: \mathbb{R} \rightarrow \mathbb{R}$ such that $g(X)$ is integrable,

$$
\int_{\mathbb{R}} g(x) Q_{X}(\omega, d x)
$$

is a version of $E[g(X) \mid \mathcal{A}]$.
2. We consider two random variables $X$ and $Y$ and a measurable function $g$ such that $g(X)$ is integrable. We write

$$
E[g(X) \mid Y]=E[g(X) \mid \sigma(Y)]
$$

for the conditional expectation of $g(X)$ given $Y$. By definition $E[g(X) \mid Y]$ is $\sigma(Y)$-measurable and by Doob's representation theorem (cf. [61], p. 12) there exists a measurable function $h: Y(\Omega) \rightarrow \mathbb{R}$ such that

$$
E[g(X) \mid Y]=h(Y)
$$

If we know such a function $h$, we can also determine $h(y)=E[g(X) \mid Y=$ $y], y \in \mathbb{R}$, the conditional expectation of $g(X)$ given that $Y$ has realization $y$. Of course, if $P(Y=y)>0$, we have

$$
h(y)=E[g(X) \mid Y=y]=\frac{1}{P(Y=y)} \int_{\{Y=y\}} g(X) d P
$$

But even if the set $\{Y=y\}$ has probability 0 , we are now able to determine the conditional expectation of $g(X)$ given that $Y$ takes the value $y$ (provided we know $h$ ). Consider the case that a joint density $f_{X Y}(x, y)$ of $X$ and $Y$ is known. Let $f_{Y}(y)=\int_{\mathbb{R}} f_{X Y}(x, y) d x$ be the density of the (marginal) distribution of $Y$ and

$$
f_{X \mid Y}(x \mid y)=\left\{\begin{array}{cc}
f_{X Y}(x, y) / f_{Y}(y) & \text { if } f_{Y}(y) \neq 0 \\
0 & \text { otherwise }
\end{array}\right.
$$

the elementary conditional density of $X$ given $Y$. A natural choice for the function $h$ would then be

$$
h(y)=\int_{\mathbb{R}} g(x) f_{X \mid Y}(x, y) d x
$$We claim that $h(Y)$ is a version of the conditional expectation $E[g(X) \mid Y]$. To prove this note that the elements of the $\sigma$-algebra $\sigma(Y)$ are of the form $Y^{-1}(B)=\{\omega: Y(\omega) \in B\}, B \in \mathcal{B}$. Therefore, we have to show that

$$
E\left[g(X) I_{B}(Y)\right]=\iint g(x) I_{B}(y) f_{X Y}(x, y) d x d y
$$

equals

$$
E\left[h(Y) I_{B}(Y)\right]=\int h(y) I_{B}(y) f_{Y}(y) d y
$$

for all $B \in \mathcal{B}$. But this follows directly from Fubini's Theorem, which proves the assertion.

# A. 3 Stochastic Processes on a Filtered Probability Space 

Definition A.8. 1. A stochastic process is a family $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, of random variables all defined on the same probability space $(\Omega, \mathcal{F}, P)$ with values in a measurable space $(S, \mathcal{S})$.
2. For $\omega \in \Omega$ the mapping $t \rightarrow X_{t}(\omega)$ is called path.
3. Two stochastic processes $X, Y$ are called indistinguishable, if $P$-almost all paths are identical: $P\left(X_{t}=Y_{t}, \forall t \in \mathbb{R}_{+}\right)=1$.

If it is claimed that a process is unique, we mean uniqueness up to indistinguishability. Also for conditional expectations no distinction will be made between one version of the conditional expectation and the equivalence class of $P$-a.s. equal versions. A real-valued process is called right- or left-continuous, nondecreasing, of bounded variation on finite intervals etc., if $P$-almost all paths have this property, i.e., if the process is indistinguishable from a process, the paths of which all have that property. In particular a process is called cadlag (continu à droite, limité à gauche), if almost all paths are rightcontinuous and left-limited.

If not otherwise mentioned, we always refer in the following to real-valued stochastic processes, i.e., to processes $X=\left(X_{t}\right)$ for which the $X_{t}$ take values in $(S, \mathcal{S})=(\mathbb{R}, \mathcal{B})$, where $\mathcal{B}=\mathcal{B}(\mathbb{R})$ is the Borel $\sigma$-algebra on $\mathbb{R}$.

Definition A.9. A stochastic process $X$ is called

1. integrable, if $E\left|X_{t}\right|<\infty, \forall t \in \mathbb{R}_{+}$;
2. square integrable, if $E X_{t}^{2}<\infty, \forall t \in \mathbb{R}_{+}$;
3. bounded in $L^{p}, p \geq 1$, if $\sup _{t \in \mathbb{R}_{+}} E\left|X_{t}\right|^{p}<\infty$;
4. uniformly integrable, if $\lim _{c \rightarrow \infty} \sup _{t \in \mathbb{R}_{+}} E\left[\left|X_{t}\right| I\left(\left|X_{t}\right|>c\right)\right]=0$.

Deviating from our notation some authors call an $L^{2}$-bounded stochastic process square integrable.

Uniform integrability plays an important role in martingale theory. Therefore, we look for criteria for this property. A very useful one is given in the following proposition.Proposition A.10. A stochastic process $X$ is uniformly integrable if and only if there exists a positive increasing convex function $G: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$such that

1. $\lim _{t \rightarrow \infty} \frac{G(t)}{t}=\infty$ and
2. $\sup _{t \in \mathbb{R}_{+}} E G\left(\left|X_{t}\right|\right)<\infty$.

In particular, taking $G(t)=t^{p}$, we see that a process $X$, which is bounded in $L^{p}$ for some $p>1$, is uniformly integrable. A process bounded in $L^{1}$ is not necessarily uniformly integrable. The property of uniform integrability links the convergence in probability with convergence in $L^{1}$.

Theorem A.11. Let $\left(X_{n}\right), n \in \mathbb{N}$, be a sequence of integrable random variables that converges in probability to a random variable $X$, i.e., $P\left(\left|X_{n}-X\right|>\right.$ $\epsilon) \rightarrow 0$ as $n \rightarrow \infty \forall \epsilon>0$. Then

$$
X \in L^{1} \text { and } X_{n} \xrightarrow{L^{1}} X, \text { i.e., } E\left|X_{n}-X\right| \rightarrow 0 \text { as } n \rightarrow \infty
$$

if and only if $\left(X_{n}\right)$ is uniformly integrable.
So if $X_{n} \rightarrow X P$-a.s. and the sequence is uniformly integrable, then it follows that $E X_{n} \rightarrow E X, n \rightarrow \infty$. At first sight it seems reasonable that under uniform integrability almost sure convergence can be carried over also to conditional expectations $E\left[X_{n} \mid \mathcal{A}\right]$ for some sub- $\sigma$-algebra $\mathcal{A} \subset \mathcal{F}$. But (surprisingly) this does not hold true in general, for a counterexample see Jensen [97]. The condition $\sup X_{n} \in L^{1}$ in the dominated convergence theorem for conditional expectations as stated above is necessary for the convergence result and cannot be weakened.

To describe the information that is gathered observing some stochastic phenomena in time, we introduce filtrations.

Definition A.12. 1. A family $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, of sub- $\sigma$-algebras of $\mathcal{F}$ is called a filtrationif it is nondecreasing, i.e., if $s \leq t$, then $\mathcal{F}_{s} \subset \mathcal{F}_{t}$. We denote $\mathcal{F}_{\infty}=\bigvee_{t \in \mathbb{R}_{+}} \mathcal{F}_{t}=\sigma\left(\bigcup_{t \in \mathbb{R}_{+}} \mathcal{F}_{t}\right)$.
2. If $\mathbb{F}=\left(\mathcal{F}_{t}\right)$ is a filtration, then we write

$$
\mathcal{F}_{t+}=\bigcap_{h>0} \mathcal{F}_{t+h} \text { and } \mathcal{F}_{t-}=\sigma\left(\bigcup_{h>0} \mathcal{F}_{t-h}\right)
$$

3. A filtration $\left(\mathcal{F}_{t}\right)$ is called right-continuous, if for all $t \in \mathbb{R}_{+}$, we have $\mathcal{F}_{t+}=\mathcal{F}_{t}$.
4. A probability space $(\Omega, \mathcal{F}, P)$ together with a filtration $\mathbb{F}$ is called a stochastic basis: $(\Omega, \mathcal{F}, \mathbb{F}, P)$.
5. A stochastic basis $(\Omega, \mathcal{F}, \mathbb{F}, P)$ is called complete, if $\mathcal{F}$ is complete, i.e., $\mathcal{F}$ contains all subsets of $P$-null sets, and if each $\mathcal{F}_{t}$ contains all $P$-null sets of $\mathcal{F}$.
6. A filtration $\mathbb{F}$ is said to fulfill the usual conditions, if it is right-continuous and complete.The $\sigma$-algebra $\mathcal{F}_{t}$ is often interpreted as the information gathered up to time $t$, or more precisely, the set of events of $\mathcal{F}$, which can be distinguished at time $t$. If a stochastic process $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, is observed, then a natural choice for a corresponding filtration would be $\mathcal{F}_{t}=\mathcal{F}_{t}^{X}=\sigma\left(X_{s}, 0 \leq s \leq\right.$ $t$ ), which is the smallest $\sigma$-algebra such that all random variables $X_{s}, 0 \leq$ $s \leq t$, are $\mathcal{F}_{t}$-measurable. Here we assume that $\mathcal{F}_{t}^{X}$ is augmented so that the generated filtration fulfills the usual conditions. Such an augmentation is always possible (cf. Dellacherie and Meyer [61], p. 115).
Remark A.13. Sometimes it is discussed whether such an augmentation affects the filtration too strongly. Indeed, if we consider, for example, two mutually singular probability measures, say $P$ and $Q$ on the measurable space $(\Omega, \mathcal{F})$ such that $P(A)=1-Q(A)=1$ for some $A \in \mathcal{F}$, then completing each $\mathcal{F}_{t}$ with all $P$ and $Q$ negligible sets may result in $\mathcal{F}_{t}=\mathcal{F}$ for all $t \in \mathbb{R}_{+}$, which is a rather uninteresting case destroying the modeling of the evolution in time. But in the material we cover in this book such cases are not essential and we always assume that a stochastic basis is given with a filtration meeting the usual conditions.
Definition A.14. A stochastic process $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, is called adapted to a filtration $\mathbb{F}=\left(\mathcal{F}_{t}\right)$, if $X_{t}$ is $\mathcal{F}_{t}$-measurable for all $t \in \mathbb{R}_{+}$.
Definition A.15. A stochastic process $X$ is $\mathbb{F}$-progressive or progressively measurable, if for every $t$, the mapping $(s, \omega) \rightarrow X_{s}(\omega)$ on $[0, t] \times \Omega$ is measurable with respect to the product $\sigma$-algebra $\mathcal{B}([0, t]) \otimes \mathcal{F}_{t}$, where $\mathcal{B}([0, t])$ is the Borel $\sigma$-algebra on $[0, t]$.
Theorem A.16. Let $X$ be a real-valued stochastic process. If $X$ is lefror right-continuous and adapted to $\mathbb{F}$, then it is $\mathbb{F}$-progressive. If $X$ is $\mathbb{F}$ progressive, then so is $\int_{0}^{t} X_{s} d s$.

A further measurability restriction is needed in connection with stochastic processes in continuous time. This is the fundamental concept of predictability.
Definition A.17. Let $\mathbb{F}$ be a filtration on the basic probability space and let $\mathcal{P}(\mathbb{F})$ be the $\sigma$-algebra on $(0, \infty) \times \Omega$ generated by the system of sets

$$
(s, t] \times A, 0 \leq s<t, A \in \mathcal{F}_{s}, t>0
$$

$\mathcal{P}(\mathbb{F})$ is called the $\mathbb{F}$-predictable $\sigma$-algebra on $(0, \infty) \times \Omega$. A stochastic process $X=\left(X_{t}\right)$ is called $\mathbb{F}$-predictable, if $X_{0}$ is $\mathcal{F}_{0}$-measurable and the mapping $(t, \omega) \rightarrow X_{t}(\omega)$ on $(0, \infty) \times \Omega$ into $\mathbb{R}$ is measurable with respect to $\mathcal{P}(\mathbb{F})$.
Theorem A.18. Every left-continuous process adapted to $\mathbb{F}$ is $\mathbb{F}$-predictable.
In all applications, we will be concerned with predictable processes that are left-continuous. Note that $\mathbb{F}$-predictable processes are also $\mathbb{F}$-progressive. A property that explains the term predictable is given in the following theorem.
Theorem A.19. Suppose the process $X$ is $\mathbb{F}$-predictable. Then for all $t>0$ the variable $X_{t}$ is $\mathcal{F}_{t-}$-measurable.# A. 4 Stopping Times 

Suppose we want to describe a point in time at which a stochastic process first enters a given set, say when it hits a certain level. So this point in time is a random time because it depends on the random evolution of the process. Observing this stochastic process, it is possible to decide at any time $t$ whether this random time has occurred or not. Such random times, which are based on the available information not anticipating the future, are defined as follows.
Definition A.20. Suppose $\mathbb{F}=\left(\mathcal{F}_{t}\right), t \in \mathbb{R}_{+}$, is a filtration on the measurable space $(\Omega, \mathcal{F})$. A random variable $\tau: \Omega \rightarrow[0, \infty]$ is said to be a stopping time if for every $t \in \mathbb{R}_{+}$,

$$
\{\tau \leq t\}=\{\omega: \tau(\omega) \leq t\} \in \mathcal{F}_{t}
$$

In particular, a constant random variable $\tau=t_{0} \in \mathbb{R}_{+}$is a stopping time. Since we assume that the filtration is right-continuous, we can equivalently describe stopping times by the condition $\{\tau<t\} \in \mathcal{F}_{t}:$ If $\{\tau<t\} \in \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$, then

$$
\{\tau \leq t\}=\bigcap_{n \in \mathbb{N}}\left\{\tau<t+\frac{1}{n}\right\} \in \bigcap_{n \in \mathbb{N}} \mathcal{F}_{t+\frac{1}{n}}=\mathcal{F}_{t+}
$$

Conversely, if $\{\tau \leq t\} \in \mathcal{F}_{t}$ for all $t \in \mathbb{R}_{+}$, then

$$
\{\tau<t\}=\bigcup_{n \in \mathbb{N}}\left\{\tau \leq t-\frac{1}{n}\right\} \in \mathcal{F}_{t} \text { for } t>0 \text { and }\{\tau<0\}=\emptyset \in \mathcal{F}_{0}
$$

Proposition A.21. Suppose $\sigma$ and $\tau$ are stopping times. Then $\sigma \wedge \tau, \sigma \vee \tau$, and $\sigma+\tau$ are stopping times. Let $\left(\tau_{n}\right), n \in \mathbb{N}$, be a sequence of stopping times. Then $\sup \tau_{n}$ and $\inf \tau_{n}$ are also stopping times.
Proof. First we show that $\sigma+\tau$ is a stopping time and consider the complement of the event $\{\sigma+\tau \leq t\}$ :

$$
\{\sigma+\tau>t\}=\{\sigma>t\} \cup\{\tau>t\} \cup\{\sigma \geq t, \tau>0\} \cup\{0<\sigma<t, \sigma+\tau>t\}
$$

The first three events of this union are clearly in $\mathcal{F}_{t}$. The fourth event

$$
\{0<\sigma<t, \sigma+\tau>t\}=\bigcup_{r \in \mathbb{Q} \cap[0, t)}\{r<\sigma<t, \tau>t-r\}
$$

is the countable union of events of $\mathcal{F}_{t}$ and therefore $\sigma+\tau$ is a stopping time.
The proof of the remaining assertions follows from

$$
\begin{aligned}
\left\{\sup \tau_{n} \leq t\right\} & =\bigcap_{n \in \mathbb{N}}\left\{\tau_{n} \leq t\right\} \in \mathcal{F}_{t} \\
\left\{\inf \tau_{n}<t\right\} & =\bigcup_{n \in \mathbb{N}}\left\{\tau_{n}<t\right\} \in \mathcal{F}_{t}
\end{aligned}
$$

using the fact that for a right-continuous filtration it suffices to show $\left\{\inf \tau_{n}<\right.$ $t\} \in \mathcal{F}_{t}$.For a sequence of stopping times $\left(\tau_{n}\right)$ the random variables $\sup \tau_{n}, \inf \tau_{n}$ are stopping times, so that $\lim \sup \tau_{n}, \liminf \tau_{n}$ and $\lim \tau_{n}$ (if it exists) are also stopping times.

We now define the $\sigma$-algebra of the past of a stopping time $\tau$.
Definition A.22. Suppose $\tau$ is a stopping time with respect to the filtration $\mathbb{F}$. Then the $\sigma$-algebra $\mathcal{F}_{\tau}$ of events occurring up to time $\tau$ is

$$
\mathcal{F}_{\tau}=\left\{A \in \mathcal{F}_{\infty}: A \cap\{\tau \leq t\} \in \mathcal{F}_{t} \text { for all } t \in \mathbb{R}_{+}\right\}
$$

We note that $\tau$ is $\mathcal{F}_{\tau}$-measurable and that for a constant stopping time $\tau=t_{0} \in \mathbb{R}_{+}$we have $\mathcal{F}_{\tau}=\mathcal{F}_{t_{0}}$.

Theorem A.23. Suppose $\sigma$ and $\tau$ are stopping times.
(i) If $\sigma \leq \tau$, then $\mathcal{F}_{\sigma} \subset \mathcal{F}_{\tau}$.
(ii) If $A \in \mathcal{F}_{\sigma}$, then $A \cap\{\sigma \leq \tau\} \in \mathcal{F}_{\tau}$.
(iii) $\mathcal{F}_{\sigma \wedge \tau}=\mathcal{F}_{\sigma} \cap \mathcal{F}_{\tau}$.

Proof. (i) For $B \in \mathcal{F}_{\sigma}$ and $t \in \mathbb{R}_{+}$we have

$$
B \cap\{\tau \leq t\}=B \cap\{\sigma \leq t\} \cap\{\tau \leq t\} \in \mathcal{F}_{t}
$$

which proves (i).
(ii) Suppose $A \in \mathcal{F}_{\sigma}$. Then

$$
A \cap\{\sigma \leq \tau\} \cap\{\tau \leq t\}=A \cap\{\sigma \leq t\} \cap\{\tau \leq t\} \cap\{\sigma \wedge t \leq \tau \wedge t\}
$$

Now $A \cap\{\sigma \leq t\}$ and $\{\tau \leq t\}$ are elements of $\mathcal{F}_{t}$ by assumption and the random variables $\sigma \wedge t$ and $\tau \wedge t$ are both $\mathcal{F}_{t}$-measurable. This shows that $\{\sigma \wedge t \leq \tau \wedge t\} \in \mathcal{F}_{t}$.
(iii) Since $\sigma \wedge \tau \leq \sigma$ and $\sigma \wedge \tau \leq \tau$ we obtain from (i)

$$
\mathcal{F}_{\sigma \wedge \tau} \subset \mathcal{F}_{\sigma} \cap \mathcal{F}_{\tau}
$$

Conversely, for $A \in \mathcal{F}_{\sigma} \cap \mathcal{F}_{\tau}$ we have

$$
A \cap\{\sigma \wedge \tau \leq t\}=(A \cap\{\sigma \leq t\}) \cup(A \cap\{\tau \leq t\}) \in \mathcal{F}_{t}
$$

which proves (iii).
This theorem shows that some of the properties known for fixed time points $s, t$ also hold true for stopping times $\sigma, \tau$. Next we consider the link between a stochastic process $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, and a stopping time $\sigma$. It is natural to investigate variables $X_{\sigma(\omega)}(\omega)$ with random index and the stopped process $X_{t}^{\sigma}(\omega)=X_{\sigma \wedge t}(\omega)$ on $\{\sigma<\infty\}$. To ensure that $X_{\sigma}$ is a random variable, we need that $X_{t}$ fulfills a measurability requirement in $t$.

Theorem A.24. If $\sigma$ is a stopping time and $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, is an $\mathbb{F}$ progressive process, then $X_{\sigma}$ is $\mathcal{F}_{\sigma}$-measurable and $X^{\sigma}$ is $\mathbb{F}$-progressive.Proof. We must show that for any Borel set $B \in \mathcal{B},\left\{X_{\sigma} \in B\right\} \cap\{\sigma \leq$ $t\}$ belongs to $\mathcal{F}_{t}$. This intersection equals $\left\{X_{\sigma \wedge t} \in B\right\} \cap\{\sigma \leq t\}$, so we need only show that $X^{\sigma}$ is progressive. Now $\sigma \wedge t$ is $\mathcal{F}_{t}$-measurable. Hence, $(s, \omega) \rightarrow(\sigma(\omega) \wedge s, \omega)$ is $\mathcal{B}([0, t]) \otimes \mathcal{F}_{t}$-measurable. Therefore, the map $(s, \omega) \rightarrow$ $X_{\sigma(\omega) \wedge s}(\omega)$ is measurable as it is the composition of two measurable maps. Hence $X^{\sigma}$ is progressive.

Most important for applications are those random times $\sigma$ that are defined as first entrance times of a stochastic process $X$ into a Borel set $B: \sigma=\inf \{t \in$ $\left.\mathbb{R}_{+}: X_{t} \in B\right\}$. In general, it is very difficult to show that $\sigma$ is a stopping time. For a discussion of the usual conditions in this connection, see Rogers and Williams [133], pp. 183-191. For a complete proof of the following theorem we refer to Dellacherie and Meyer [61], p. 116.

Theorem A.25. Let $X$ be an $\mathbb{F}$-progressive process with respect to the complete and right-continuous filtration $\mathbb{F}$ and $B \in \mathcal{B}$ a Borel set. Then

$$
\sigma(\omega)=\inf \left\{t \in \mathbb{R}_{+}: X_{t}(\omega) \in B\right\}
$$

is an $\mathbb{F}$-stopping time.
Proof. We only show the simple case where $X$ is right-continuous and $B$ is an open set. Then the right continuity implies that

$$
\{\sigma<t\}=\bigcup_{r \in \mathbb{Q} \cap[0, t)}\left\{X_{r} \in B\right\} \in \mathcal{F}_{t}
$$

Using the right-continuity of $\mathbb{F}$ it is seen that $\sigma$ is an $\mathbb{F}$-stopping time .
Note that the right-continuity of the paths was used to express $\{\sigma<t\}$ as the union of events $\left\{X_{r} \in B\right\}$ and that we could restrict ourselves to a countable union because $B$ is an open set.

# A. 5 Martingale Theory 

An overview over the historical development of martingale theory can be found in monographs such as Andersen et al. [2], pp. 115-120, or Kallenberg [101], pp. 464-485. We fix a stochastic basis $(\Omega, \mathcal{F}, \mathbb{F}, P)$ and define stochastic processes with certain properties which are known as the stochastic analogues to constant, increasing and decreasing functions.

Definition A.26. An integrable $\mathbb{F}$-adapted process $X=\left(X_{t}\right), t \in \mathbb{R}_{+}$, is called a martingale if

$$
X_{t}=E\left[X_{s} \mid \mathcal{F}_{t}\right]
$$

for all $s \geq t, s, t \in \mathbb{R}_{+}$. A supermartingale is defined in the same way, except that (A.2) is replaced by

$$
X_{t} \geq E\left[X_{s} \mid \mathcal{F}_{t}\right]
$$and a submartingale is defined with (A.2) being replaced by

$$
X_{t} \leq E\left[X_{s} \mid \mathcal{F}_{t}\right]
$$

Forming expectations on both sides of the (in)equality we obtain $E X_{t}=$ $(\geq, \leq) E X_{s}$, which shows that a martingale is constant on average, a supermartingale decreases, and a submartingale increases on average, respectively.

Example A.27. Let $X$ be an integrable $\mathbb{F}$-adapted process. Suppose that the increments $X_{s}-X_{t}$ are independent of $\mathcal{F}_{t}$ for all $s>t, s, t \in \mathbb{R}_{+}$. If these increments have zero expectation (thus the expectation function $E X_{t}$ is constant), then $X$ is a martingale:

$$
E\left[X_{s} \mid \mathcal{F}_{t}\right]=E\left[X_{t} \mid \mathcal{F}_{t}\right]+E\left[X_{s}-X_{t} \mid \mathcal{F}_{t}\right]=X_{t}
$$

Of particular importance are the following cases.
(i) If $X$ is continuous, $X_{0}=0$, and the increments $X_{s}-X_{t}$ are normally distributed with mean 0 and variance $s-t$, then $X$ is an $\mathbb{F}$-Brownian motion. In addition to $X$, also the process $Y_{t}=X_{t}^{2}-t$ is a martingale:

$$
\begin{array}{r}
E\left[Y_{s} \mid \mathcal{F}_{t}\right]=E\left[\left(X_{s}-X_{t}\right)^{2} \mid \mathcal{F}_{t}\right]+2 X_{t} E\left[X_{s}-X_{t} \mid \mathcal{F}_{t}\right]+X_{t}^{2}-s \\
=s-t+0+X_{t}^{2}-s=Y_{t}
\end{array}
$$

(ii) If $X_{0}=0$ and the increments $X_{s}-X_{t}$ follow a Poisson distribution with mean $s-t$, for $s>t$, then $X$ is a Poisson process. Now $X$ is a submartingale because of

$$
E\left[X_{s} \mid \mathcal{F}_{t}\right]=X_{t}+E\left[X_{s}-X_{t} \mid \mathcal{F}_{t}\right]=X_{t}+s-t \geq X_{t}
$$

and $X_{t}-t$ is a martingale.
Example A.28. Let $Y$ be an integrable random variable and define $M_{t}=$ $E\left[Y \mid \mathcal{F}_{t}\right]$. Then $M$ is a martingale because of the successive conditioning property:

$$
E\left[M_{s} \mid \mathcal{F}_{t}\right]=E\left[E\left[Y \mid \mathcal{F}_{s}\right] \mid \mathcal{F}_{t}\right]=E\left[Y \mid \mathcal{F}_{t}\right]=M_{t}, s \geq t
$$

So $M_{t}$ is a predictor of $Y$ given the information $\mathcal{F}_{t}$ gathered up to time $t$. Furthermore, $M$ is a uniformly integrable martingale. To see this we have to show that $\lim _{c \rightarrow \infty} \sup _{t \in \mathbb{R}_{+}} E\left[\left|M_{t}\right| I\left(\left|M_{t}\right|>c\right)\right] \rightarrow 0$ as $c \rightarrow \infty$. By Jensen's inequality for conditional expectations we obtain

$$
E\left[\left|M_{t}\right| I\left(\left|M_{t}\right|>c\right)\right] \leq E\left[E\left[|Y| I\left(\left|M_{t}\right|>c\right) \mid \mathcal{F}_{t}\right]\right]=E\left[|Y| I\left(\left|M_{t}\right|>c\right)\right]
$$

Since $Y$ is integrable and $c P\left(\left|M_{t}\right|>c\right) \leq E\left|M_{t}\right| \leq E|Y|$, it follows that $P\left(\left|M_{t}\right|>c\right) \rightarrow 0$ uniformly in $t$, which shows that $M$ is uniformly integrable.

Concerning the regularity of the paths of a supermartingale, the following result holds true.Lemma A.29. Suppose $X$ is a supermartingale such that $t \rightarrow E X_{t}$ is right-continuous. Then $X$ has a modification with all paths cadlag, i.e., there exists a process $Y$ with cadlag paths such that $X_{t}=Y_{t} P$-a.s. for all $t \in \mathbb{R}_{+}$.

So for a martingale, a submartingale, or a supermartingale with rightcontinuous expectation function, we can assume that it has cadlag paths. From now on we make the general assumption that all martingales, submartingales, and supermartingales are cadlag unless stated otherwise.

Lemma A.30. Let $M$ be a martingale and consider a convex function $g$ : $\mathbb{R} \rightarrow \mathbb{R}$ such that $X=g(M)$ is integrable. Then $X$ is a submartingale.

If $g$ is also nondecreasing, then the assertion remains true for submartingales $M$.

Proof. Let $M$ be a martingale. Then by Jensen's inequality we obtain for $s \geq t$

$$
X_{t}=g\left(M_{t}\right)=g\left(E\left[M_{s} \mid \mathcal{F}_{t}\right]\right) \leq E\left[g\left(M_{s}\right) \mid \mathcal{F}_{t}\right]=E\left[X_{s} \mid \mathcal{F}_{t}\right]
$$

which shows that $X$ is a submartingale.
If $M$ is a submartingale and $g$ is nondecreasing, then

$$
g\left(M_{t}\right) \leq g\left(E\left[M_{s} \mid \mathcal{F}_{t}\right]\right)
$$

shows that the conclusion remains valid.

The last lemma is often applied with functions $g(x)=|x|^{p}, p \geq 1$. So, if $M$ is a square integrable martingale, then $X=M^{2}$ defines a submartingale.

One key result in martingale theory is the following convergence theorem (cf. [62], p. 72).

Theorem A.31. Let $X$ be a supermartingale (martingale). Suppose that

$$
\sup _{t \in \mathbb{R}_{+}} E\left|X_{t}\right|<\infty
$$

a condition that is equivalent to $\lim _{t \rightarrow \infty} E X_{t}^{-}<\infty$. Then the random variable $X_{\infty}=\lim _{t \rightarrow \infty} X_{t}$ exists and is integrable.

If the supermartingale (martingale) $X$ is uniformly integrable, $X_{\infty}$ exists and closes $X$ on the right in that for all $t \in \mathbb{R}_{+}$

$$
X_{t} \geq E\left[X_{\infty} \mid \mathcal{F}_{t}\right]\left(\text { respectively } X_{t}=E\left[X_{\infty} \mid \mathcal{F}_{t}\right]\right)
$$

As a consequence we get the following characterization of the convergence of martingales.

Theorem A.32. Suppose $M$ is a martingale. Then the following conditions are equivalent:(i) $M$ is uniformly integrable.
(ii) There exists a random variable $M_{\infty}$ such that $M_{t}$ converges to $M_{\infty}$ in $L^{1}:\left.\lim _{t \rightarrow \infty} E \mid M_{t}-M_{\infty} \right\rvert\,=0$.
(iii) $M_{t}$ converges $P$-a.s. to an integrable random variable $M_{\infty}$, which closes $M$ on the right: $M_{t}=E\left[M_{\infty} \mid \mathcal{F}_{t}\right]$.

Example A.33. If in Example A. 28 we assume that $Y$ is $\mathcal{F}_{\infty}$-measurable, then we can conclude that the martingale $M_{t}=E\left[Y \mid \mathcal{F}_{t}\right]$ converges $P$-a.s. and in $L^{1}$ to $Y$.

In Example A. 27 (i) we see that Brownian motion $\left(X_{t}\right)$ is not uniformly integrable as for any $c>1$ we can find a $t>0$ such that $P\left(\left|X_{t}\right|>c\right) \geq \epsilon$ for some $\epsilon, 0<\epsilon<1$. In this case we can conclude that $X_{t}$ does not converge to any random variable for $t \rightarrow \infty$ neither $P$-a.s. nor in $L^{1}$.

Next we consider conditions under which the (super-)martingale property also extends from fixed time points $s, t$ to stopping times $\sigma, \tau$.

Theorem A.34. (Optional Sampling Theorem). Let $X$ be a supermartingale and let $\sigma$ and $\tau$ be two stopping times such that $\sigma \leq \tau$. Suppose either that $\tau$ is bounded or that $\left(X_{t}\right)$ is uniformly integrable. Then $X_{\sigma}$ and $X_{\tau}$ are integrable and

$$
X_{\sigma} \geq E\left[X_{\tau} \mid \mathcal{F}_{\sigma}\right]
$$

with equality if $X$ is a martingale.
An often used consequence of Theorem A. 34 is the following: If $X$ is a uniformly integrable martingale, then setting $\sigma=0$ we obtain $E X_{0}=E X_{\tau}$ for all stopping times $\tau$ (all quantities are related to the same filtration $\mathbb{F}$ ). A kind of converse is the following proposition.

Proposition A.35. Suppose $X$ is an adapted cadlag process such that for any bounded stopping time $\tau$ the random variable $X_{\tau}$ is integrable and $E X_{0}=$ $E X_{\tau}$. Then $X$ is a martingale.

A further consequence of the Optional Sampling Theorem is that a stopped (super-) martingale remains a (super-) martingale.

Corollary A.36. Let $X$ be a right-continuous supermartingale (martingale) and $\tau$ a stopping time. Then the stopped process $X^{\tau}=\left(X_{t \wedge \tau}\right)$ is a supermartingale (martingale). If either $X$ is uniformly integrable or $I(\tau<\infty) X_{\tau}$ is integrable and $\lim _{t \rightarrow \infty} \int_{\{\tau>t\}}\left|X_{t}\right| d P=0$, then $X^{\tau}$ is uniformly integrable.

Martingales are often constructed in that an increasing process is subtracted from a submartingale (cf. Example A. 27 (ii), p. 260). This fact emanates from the celebrated Doob-Meyer decomposition, which is a cornerstone in modern probability theory.Theorem A.37. (Doob-Meyer decomposition). Let the process $X$ be right-continuous and adapted. Then $X$ is a uniformly integrable submartingale if and only if it has a decomposition

$$
X=A+M
$$

where $A$ is a right-continuous predictable nondecreasing and integrable process with $A_{0}=0$ and $M$ is a uniformly integrable martingale. The decomposition is unique within indistinguishable processes.

Remark A.38. 1. Several proofs of this and more general results, not restricted to uniformly integrable processes, are known (cf. [62], p. 198 and [101], p. 412). Some of these also refer to local martingales, which are not needed for the applications we have presented and which are therefore not introduced here.
2. The process $A$ in the theorem above is often called compensator.
3. In the case of discrete time such a decomposition is easily constructed in the following way. Let $\left(X_{n}\right), n \in \mathbb{N}_{0}$, be a submartingale with respect to a filtration $\left(\mathcal{F}_{n}\right), n \in \mathbb{N}_{0}$. Then we define

$$
X_{n}=A_{n}+M_{n}
$$

where

$$
\begin{aligned}
A_{n} & =A_{n-1}+E\left[X_{n} \mid \mathcal{F}_{n-1}\right]-X_{n-1}, n \in \mathbb{N}, A_{0}=0 \\
M_{n} & =X_{n}-A_{n}, n \in \mathbb{N}_{0}
\end{aligned}
$$

The process $M$ is a martingale and $A$ is nondecreasing and predictable in that $A_{n}$ is $\mathcal{F}_{n-1}$-measurable for $n \in \mathbb{N}$. This decomposition is unique, since for a second decomposition $X_{n}=\tilde{A}_{n}+\tilde{M}_{n}$ with the same properties we must have $M_{n}-\tilde{M}_{n}=A_{n}-\tilde{A}_{n}$, which is a predictable martingale. Therefore,

$$
0=E\left[A_{n}-\tilde{A}_{n} \mid \mathcal{F}_{n-1}\right]=A_{n}-\tilde{A}_{n}, n \in \mathbb{N}
$$

and $A_{0}=\tilde{A}_{0}=0$.
The continuous time result needs much more care and uses several lemmas, one of which is interesting in its own right and will be presented here.

Lemma A.39. A process $M$ is a predictable martingale of integrable variation, i.e., $E\left[\int_{0}^{\infty}\left|d M_{s}\right|\right]<\infty$, if and only if $M_{t}=M_{0}$ for all $t \in \mathbb{R}_{+}$.

We will now use the Doob-Meyer decomposition to introduce two types of (co-)variation processes. For this we recall that $\mathcal{M}\left(\mathcal{M}_{0}\right)$ denotes the class of cadlag martingales (with $M_{0}=0$ ) and denote by $\mathcal{M}^{2}\left(\mathcal{M}_{0}^{2}\right)$ the set of martingales in $\mathcal{M}\left(\mathcal{M}_{0}\right)$, which are bounded in $L^{2}$, i.e., $\sup _{t \in \mathbb{R}_{+}} E M_{t}^{2}<\infty$.Definition A.40. For $M \in \mathcal{M}^{2}$ the unique compensator of $M^{2}$ in the Doob-Meyer decomposition, denoted $\langle M, M\rangle$ or $\langle M\rangle$, is called the predictable variation process. For $M_{1}, M_{2} \in \mathcal{M}^{2}$ the process

$$
\left\langle M_{1}, M_{2}\right\rangle=\frac{1}{4}\left(\left\langle M_{1}+M_{2}\right\rangle-\left\langle M_{1}-M_{2}\right\rangle\right)
$$

is called the predictable covariation process of $M_{1}$ and $M_{2}$.
Proposition A.41. Suppose that $M_{1}, M_{2} \in \mathcal{M}^{2}$. Then $A=\left\langle M_{1}, M_{2}\right\rangle$ is the unique predictable cadlag process with $A_{0}=0$ such that $M_{1} M_{2}-A \in \mathcal{M}$.

Proof. The assertion follows from the Doob-Meyer decomposition and

$$
\begin{aligned}
M_{1} M_{2}-\left\langle M_{1}, M_{2}\right\rangle= & \frac{1}{4}\left(\left(M_{1}+M_{2}\right)^{2}-\left(M_{1}-M_{2}\right)^{2}\right)-\left\langle M_{1}, M_{2}\right\rangle \\
= & \frac{1}{4}\left(\left(M_{1}+M_{2}\right)^{2}-\left\langle M_{1}+M_{2}\right\rangle\right) \\
& -\frac{1}{4}\left(\left(M_{1}-M_{2}\right)^{2}-\left\langle M_{1}-M_{2}\right\rangle\right)
\end{aligned}
$$

To understand what predictable variation means, we give a heuristic explanation. Recall that for a martingale $M$ we have for all $0<h<t$

$$
E\left[M_{t}-M_{t-h} \mid \mathcal{F}_{t-h}\right]=0
$$

or in heuristic form:

$$
E\left[d M_{t} \mid \mathcal{F}_{t-}\right]=0
$$

Since $M^{2}-\langle M\rangle$ is a martingale and $\langle M\rangle$ is predictable, we obtain

$$
E\left[d M_{t}^{2} \mid \mathcal{F}_{t-}\right]=E\left[d\langle M\rangle_{t} \mid \mathcal{F}_{t-}\right]=d\langle M\rangle_{t}
$$

Furthermore,

$$
\begin{aligned}
d M_{t}^{2} & =M_{t}^{2}-M_{t-}^{2} \\
& =\left(M_{t-}+d M_{t}\right)^{2}-M_{t-}^{2} \\
& =\left(d M_{t}\right)^{2}+2 M_{t-} d M_{t}
\end{aligned}
$$

yielding

$$
\begin{aligned}
d\langle M\rangle_{t} & =E\left[\left(d M_{t}\right)^{2} \mid \mathcal{F}_{t-}\right]+2 M_{t-} E\left[d M_{t} \mid \mathcal{F}_{t-}\right]=E\left[\left(d M_{t}\right)^{2} \mid \mathcal{F}_{t-}\right] \\
& =\operatorname{Var}\left[d M_{t} \mid \mathcal{F}_{t-}\right]
\end{aligned}
$$

This indicates (and it can be proved) that $\langle M\rangle_{t}$ is the stochastic limit of the form

$$
\sum_{i=1}^{n} \operatorname{Var}\left[M_{t_{i}}-M_{t_{i-1}} \mid \mathcal{F}_{t_{i-1}}\right]
$$

as $n \rightarrow \infty$ and the span of the partition $0=t_{0}<t_{1}<\ldots<t_{n}=t$ tends to 0 .Definition A.42. Two martingales $M, L \in \mathcal{M}^{2}$ are called orthogonal if their product is a martingale: $M L \in \mathcal{M}$.

For two martingales $M, L$ of $\mathcal{M}^{2}$ that are orthogonal we must have $\langle M, L\rangle=0$. If we equip $\mathcal{M}^{2}$ with the scalar product

$$
(M, L)_{\mathcal{M}^{2}}=E\left[M_{\infty} L_{\infty}\right]
$$

inducing the norm $\|M\|=\left(E M_{\infty}^{2}\right)^{1 / 2}$, then $\mathcal{M}^{2}$ becomes a Hilbert space. Because of $M L-\langle M, L\rangle \in \mathcal{M}$ and $\langle M, L\rangle_{0}=0$, it follows that

$$
(M, L)_{\mathcal{M}^{2}}=E\left[M_{\infty} L_{\infty}\right]=E\langle M, L\rangle_{\infty}+E M_{0} L_{0}
$$

So two orthogonal martingales $M, L$ of $\mathcal{M}_{0}^{2}$ are also orthogonal in the Hilbert space $\mathcal{M}^{2}$ (cf. Elliott [67], p. 88).

The set of continuous martingales in $\mathcal{M}_{0}^{2}$, denoted $\mathcal{M}_{0}^{2, c}$, is a complete subspace of $\mathcal{M}_{0}^{2}$ and $\mathcal{M}_{0}^{2, d}$ is the space orthogonal to $\mathcal{M}_{0}^{2, c}$. The martingales in $\mathcal{M}_{0}^{2, d}$ are called purely discontinuous. As an immediate consequence we obtain that any martingale $M \in \mathcal{M}_{0}^{2}$ has a unique decomposition $M=M^{c}+M^{d}$, where $M^{c} \in \mathcal{M}_{0}^{2, c}$ and $M^{d} \in \mathcal{M}_{0}^{2, d}$.

A process strongly connected to predictable variation is the so-called square bracket process introduced in the following definition.

Definition A.43. Suppose $M \in \mathcal{M}_{0}^{2}$ and $M=M^{c}+M^{d}$ is the unique decomposition with $M^{c} \in \mathcal{M}_{0}^{2, c}$ and $M^{d} \in \mathcal{M}_{0}^{2, d}$. The increasing cadlag process $[M]$ with

$$
[M]_{t}=\left\langle M^{c}\right\rangle_{t}+\sum_{s \leq t} \triangle M_{s}^{2}
$$

is called the quadratic variation of $M$, where $\triangle M_{t}=M_{t}-M_{t-}$ denotes the jump of $M$ at time $t>0\left(\triangle X_{0}=X_{0}\right)$. For martingales $M, L \in \mathcal{M}_{0}^{2}$ we define the quadratic covariation $[M, L]$ by

$$
[M, L]=\frac{1}{4}([M+L]-[M-L])
$$

The following proposition helps to understand the name quadratic covariation.

Proposition A.44. Suppose $M, L \in \mathcal{M}_{0}^{2}$.

1. Let $\left(t_{i}^{n}\right)$ be a sequence of partitions $0=t_{0}^{n}<t_{1}^{n}<\ldots<t_{n}^{n}=t$ such that the span $\sup _{i}\left(t_{i+1}^{n}-t_{i}^{n}\right)$ tends to 0 as $n \rightarrow \infty$. Then

$$
\sum_{i}\left(M_{t_{i+1}}-M_{t_{i}}\right)\left(L_{t_{i+1}}-L_{t_{i}}\right)
$$

converges $P$-a.s. and in $L^{1}$ to $[M, L]_{t}$ for all $t>0$.
2. $M L-[M, L]$ is a martingale.# A. 6 Semimartingales 

A decomposition of a stochastic process into a (predictable) drift part and a martingale, as presented for submartingales in the Doob-Meyer decomposition, also holds true for more general processes. We start with the motivating example of a sequence $\left(X_{n}\right), n \in \mathbb{N}_{0}$, of integrable random variables adapted to the filtration $\left(\mathcal{F}_{n}\right)$. This sequence admits a decomposition

$$
X_{n}=X_{0}+\sum_{i=1}^{n} f_{i}+M_{n}
$$

with a predictable sequence $f=\left(f_{n}\right), n \in \mathbb{N}$, (i.e., $f_{n}$ is $\mathcal{F}_{n-1}$-measurable) and a martingale $M=\left(M_{n}\right), n \in \mathbb{N}_{0}, M_{0}=0$. We can take

$$
\begin{aligned}
f_{n} & =E\left[X_{n}-X_{n-1} \mid \mathcal{F}_{n-1}\right] \\
M_{n} & =\sum_{i=1}^{n}\left(X_{i}-E\left[X_{i} \mid \mathcal{F}_{i-1}\right]\right)
\end{aligned}
$$

This decomposition is unique because a second decomposition of this type, say with a sequence $\tilde{f}$ and a martingale $\tilde{M}$, would imply that

$$
M_{n}-\tilde{M}_{n}=\sum_{i=1}^{n}\left(\tilde{f}_{i}-f_{i}\right)
$$

defines a predictable martingale, i.e., $E\left[M_{n}-\tilde{M}_{n} \mid \mathcal{F}_{n-1}\right]=M_{n}-\tilde{M}_{n}=M_{0}-$ $\tilde{M}_{0}=0$, which shows the uniqueness.

Unlike the time-discrete case, corresponding decompositions cannot be found for all integrable processes in continuous time. The role of increasing processes in the Doob-Meyer decomposition will now be taken by processes of bounded variation.

Definition A.45. For a cadlag function $g: \mathbb{R}_{+} \rightarrow \mathbb{R}$ the variation is defined as

$$
V_{g}(t)=\lim _{n \rightarrow \infty} \sum_{k=1}^{n}|g(t k / n)-g(t(k-1) / n)|
$$

The function $g$ is said to have finite variation if $V_{g}(t)<\infty$ for all $t \in \mathbb{R}_{+}$. The class of cadlag processes $A$ with finite variation starting in $A_{0}=0$ is denoted $\mathcal{V}$.

For any $A \in \mathcal{V}$ there is a decomposition $A_{t}=B_{t}-C_{t}$ with increasing processes $B, C \in \mathcal{V}$ and

$$
B_{t}+C_{t}=V_{A}(t)=\int_{0}^{t}\left|d A_{s}\right|
$$Definition A.46. A process $Z$ is a semimartingale if it has a decomposition

$$
Z_{t}=Z_{0}+A_{t}+M_{t}
$$

where $A \in \mathcal{V}$ and $M \in \mathcal{M}_{0}$.
There is a rich theory based on semimartingales that relies on the remarkable property that semimartingales are stable under many sorts of operations, e.g., changes of time, of probability measures, and of filtrations preserve the semimartingale property, also products and convex functions of semimartingales are semimartingales (cf. Dellacherie and Meyer [62], pp. 212-252). The importance of semimartingales lies also in the fact that stochastic integrals

$$
\int_{0}^{t} H_{s} d Z_{s}
$$

of predictable processes $H$ with respect to a semimartingale $Z$ can be introduced replacing Stieltjes integrals. It is beyond the scope of this book to present the whole theory of semimartingales; we confine ourselves to the case that the process $A$ in the semimartingale decomposition is absolutely continuous (with respect to Lebesgue-measure). The class of such processes is rich enough to contain most processes interesting in applications and allows the development of a kind of "differential" calculus.

Definition A.47. A semimartingale $Z$ with decomposition $Z_{t}=Z_{0}+A_{t}+M_{t}$ is called smooth semimartingale (SSM) if $Z$ is integrable and $A$ has the form

$$
A_{t}=\int_{0}^{t} f_{s} d s
$$

where $f$ is a progressive process and $A$ has locally integrable variation, i.e.,

$$
E \int_{0}^{t}\left|f_{s}\right| d s<\infty
$$

for all $t \in \mathbb{R}_{+}$. Short notation: $Z=(f, M)$.
As submartingales can be considered as stochastic analog to increasing functions, smooth semimartingales can be seen as the stochastic counterpart to differentiable functions. Some of the above-mentioned operations will be considered in the following.

# A.6.1 Change of Time 

Let $\left(\tau_{t}\right), t \in \mathbb{R}_{+}$, be a family of stopping times with respect to $\mathbb{F}=\left(\mathcal{F}_{t}\right)$ such that for all $\omega, \tau_{t}(\omega)$ is nondecreasing and right-continuous as a function of $t$. Then for an $\mathbb{F}$-semimartingale $Z$ we consider the transformed process $\tilde{Z}_{t}=Z_{\tau_{t}}$, which is adapted to $\tilde{\mathbb{F}}=\left(\tilde{\mathcal{F}}_{t}\right)$, where $\tilde{\mathcal{F}}_{t}=\mathcal{F}_{\tau_{t}}$.Theorem A.48. If $Z$ is an $\mathbb{F}$-semimartingale, then $\tilde{Z}$ is an $\tilde{\mathbb{F}}$-semimartingale.
One example of such a change of time is stopping a process at some fixed stopping time $\tau$ :

$$
\tau_{t}=t \wedge \tau
$$

If we consider an SSM $Z=(f, M)$, then the stopped process $Z^{\tau}=\tilde{Z}=(\tilde{f}, \tilde{M})$ is again an SSM with

$$
\tilde{f}_{t}=I(\tau>t) f_{t}
$$

# A.6.2 Product Rule 

It is known that the product of two semimartingales is a semimartingale (cf. [62], p. 219). However, this does not hold true in general for SSMs. As an example consider a martingale $M \in \mathcal{M}_{0}^{2}$ with a predictable variation process $\langle M\rangle$ that is not continuous. Then $Z=M$ is an SSM with $f=0$, but $Z^{2}=M^{2}$ has a decomposition

$$
Z_{t}^{2}=\langle M\rangle_{t}+R_{t}
$$

with some martingale $R$, which shows that $Z^{2}$ is not an SSM. To establish conditions under which a product rule for SSMs holds true, we first recall the integration by parts formula for ordinary functions.

Proposition A.49. Let $a$ and $b$ be cadlag functions on $\mathbb{R}_{+}$, which are of finite variation. Then for each $t \in \mathbb{R}_{+}$

$$
\begin{aligned}
a(t) b(t)= & a(0) b(0)+\int_{0}^{t} a(s-) d b(s)+\int_{0}^{t} b(s) d a(s) \\
= & a(0) b(0)+\int_{0}^{t} a(s-) d b(s)+\int_{0}^{t} b(s-) d a(s) \\
& +\sum_{0<s \leq t} \triangle a(s) \triangle b(s)
\end{aligned}
$$

where $a(s-)$ is the left limit at $s$ and $\triangle a(s)=a(s)-a(s-)$.
Replacing $a$ and $b$ by SSMs $Z$ and $Y$ in this integration by parts formula we need to give

$$
\int_{0}^{t} Y_{s-} d Z_{s}
$$

a meaning. The finite variation part can be defined as an ordinary (pathwise) Stieltjes integral. It remains to define $\int_{0}^{t} Y_{s-} d M_{s}$ where $M$ is a martingale possibly of unbounded variation. Because we do not want to develop the theory of stochastic integration, we only quote the following theorem stating conditions to be used in the product formula we aim at.Theorem A.50. Suppose $M \in \mathcal{M}_{0}^{2}$ and let $X$ be a predictable process such that

$$
E \int_{0}^{\infty} X_{s}^{2} d\langle M\rangle_{s}<\infty
$$

Then there exists a unique process $\int_{0}^{t} X_{s} d M_{s} \in \mathcal{M}_{0}^{2}$ with the characterizing property

$$
\left\langle\int_{0}^{t} X_{s} d M_{s}, L\right\rangle=\int_{0}^{t} X_{s} d\langle M, L\rangle_{s}
$$

for all $L \in \mathcal{M}_{0}^{2}$.
For two SSMs $Z$ and $Y$ with martingale parts $M$ and $L$, respectively, $M, L \in \mathcal{M}_{0}^{2}$, we define the covariation $[Z, Y]$ by

$$
\begin{aligned}
{[Z, Y]_{t} } & =\left\langle M^{c}, L^{c}\right\rangle_{t}+\sum_{s \leq t} \triangle Z_{s} \triangle Y_{s} \\
& =\left\langle M^{c}, L^{c}\right\rangle_{t}+Z_{0} Y_{0}+\sum_{s \leq t} \triangle M_{s} \triangle L_{s} \\
& =Z_{0} Y_{0}+[M, L]_{t}
\end{aligned}
$$

After these preparations the following product rule can be established.
Theorem A.51. Let $Z=(f, M)$ and $Y=(g, L)$ be $\mathbb{F}$-SSMs with orthogonal martingales $M, L \in \mathcal{M}_{0}^{2}$, i.e., $M L \in \mathcal{M}_{0}$. Assume that

$$
\begin{gathered}
E \int_{0}^{t}\left(\left|Z_{s} g_{s}\right|+\left|Y_{s} f_{s}\right|\right) d s<\infty, E\left|Z_{0} Y_{0}\right|<\infty \\
E \int_{0}^{\infty} Y_{s-}^{2} d\langle M\rangle_{s}<\infty, E \int_{0}^{\infty} Z_{s-}^{2} d\langle L\rangle_{s}<\infty
\end{gathered}
$$

Then $Z Y$ is an $\mathbb{F}$-SSM with representation

$$
Z_{t} Y_{t}=Z_{0} Y_{0}+\int_{0}^{t}\left(Y_{s} f_{s}+Z_{s} g_{s}\right) d s+R_{t}
$$

where $R=\left(R_{t}\right)$ is a martingale in $\mathcal{M}_{0}$.
Proof. To prove the product rule we use a form of integration by parts for semimartingales, which is an application of Ito's formula (see [67], p. 140):

$$
Z_{t} Y_{t}=\int_{(0, t]} Z_{s-} d Y_{s}+\int_{(0, t]} Y_{s-} d Z_{s}+[Z, Y]_{t}
$$

The definition of stochastic integrals implies

$$
\int_{(0, t]} Z_{s-} d Y_{s}=\int_{(0, t]} Z_{s-} d\left(\int_{0}^{s} g_{u} d u\right)+\int_{(0, t]} Z_{s-} d L_{s}
$$The second term of the sum is a martingale of $\mathcal{M}_{0}^{2}$ by virtue of

$$
E \int_{0}^{\infty} Z_{s-}^{2} d\langle L\rangle_{s}<\infty
$$

The first term of the sum is an ordinary Stieltjes integral. Since the paths of $Z$ have at most countably many jumps, it follows that

$$
\int_{(0, t]} Z_{s-} d\left(\int_{0}^{s} g_{u} d u\right)=\int_{0}^{t} Z_{s} g_{s} d s
$$

The second integral in the integration by parts formula is treated in the same way.

It remains to show that in $[Z, Y]_{t}=Z_{0} Y_{0}+[M, L]_{t}$ the second term of the sum is a martingale. From Proposition A.44, p. 265, we know that $M L-[M, L]$ is a martingale. By virtue of the assumption that $M L \in \mathcal{M}_{0}$ the square bracket process $[M, L]$ must also have the martingale property. Altogether the product semimartingale has the representation

$$
Z_{t} Y_{t}=Z_{0} Y_{0}+\int_{0}^{t}\left(Z_{s} g_{s}+Y_{s} f_{s}\right) d s+R_{t}
$$

where

$$
R_{t}=\int_{(0, t]} Z_{s-} d L_{s}+\int_{(0, t]} Y_{s-} d M_{s}+[M, L]_{t}
$$

is a martingale in $\mathcal{M}_{0}$. This completes the proof.
Sometimes the product rule is used for a product one factor of which is the one point process $I(\zeta \leq t)$ with a stopping time $\zeta$. Because of the special structure of this factor less restrictive conditions are necessary to establish a product rule.

Proposition A.52. Let $Z=(f, M)$ be an $\mathbb{F}$-SSM and $\zeta>0$ a (totally inaccessible) $\mathbb{F}$-stopping time with

$$
Y_{t}=I(\zeta \leq t)=\int_{0}^{t} g_{s} d s+L_{s}
$$

Furthermore, it is assumed that for all $t \in \mathbb{R}_{+}$

$$
E \int_{0}^{t}\left|Z_{s} g_{s}\right| d s<\infty, E \int_{0}^{t}\left|Z_{s-}\right|\left|d L_{s}\right|<\infty
$$

and $\triangle M_{\zeta}=0$. Then $Z Y$ is an SSM with representation

$$
Z_{t} Y_{t}=\int_{0}^{t}\left(Z_{s} g_{s}+Y_{s} f_{s}\right) d s+R_{t}
$$

where $R \in \mathcal{M}_{0}$.Proof. The product $Z Y$ can be represented in the form

$$
Z_{t} Y_{t}=Z_{t}-Z_{t \wedge \zeta}+\int_{0}^{t} Z_{s} d Y_{s}
$$

with the pathwise defined Stieltjes integral

$$
\int_{0}^{t} Z_{s} d Y_{s}=\int_{0}^{t} Z_{s} g_{s} d s+\int_{0}^{t} Z_{s} d L_{s}
$$

The second term in this sum can be decomposed as

$$
\int_{0}^{t} Z_{s} d L_{s}=\int_{0}^{t} Z_{s-} d L_{s}+\sum_{s \leq t} \triangle M_{s} \triangle L_{s}
$$

The sum of jumps is 0 , since $L$ is continuous outside $\{(t, \omega): \zeta(\omega)=t\}$ and $\triangle M_{\zeta}=0$. The martingale $L$ is of finite variation and the condition $E \int_{0}^{t}\left|Z_{s-}\right|$ $\left|d L_{s}\right|<\infty$ implies that the integral of the predictable process $Z_{s-}$ with respect to $L$ is a martingale (cf. [101]).

To sum up we get

$$
Z_{t} Y_{t}=\int_{0}^{t}\left(f_{s}-I(\zeta>s) f_{s}+Z_{s} g_{s}\right) d s+M_{t}-M_{t}^{\zeta}+\int_{0}^{t} Z_{s-} d L_{s}
$$

which proves the assertion.# Renewal Processes 

In this appendix we present some definitions and results from the theory of renewal processes, including renewal reward processes and regenerative processes. Key references are $[1,8,44,58,135,156]$.

The purpose of this appendix is not to give an all-inclusive presentation of the theory. Only definitions and results needed for establishing the results of Chaps. 1-5 (in particular Chap. 4) is covered.

## B. 1 Basic Theory of Renewal Processes

Let $T, T_{j}, j=1,2, \ldots$, be a sequence of nonnegative independent identically distributed (i.i.d.) random variables with distribution function $F$. To avoid trivialities, we assume that $P(T=0)<1$. From the nonnegativity of $T$, it follows that $E T$ exists, although it may be infinite, and we denote

$$
\mu=E T=\int_{0}^{\infty} P(T>t) d t
$$

The variance of $T$ is denoted $\sigma^{2}$. Let

$$
S_{0}=0, \quad S_{j}=\sum_{i=1}^{j} T_{i}, \quad j \in \mathbb{N}
$$

and define

$$
N_{t}=\sup \left\{j: S_{j} \leq t\right\}
$$

or equivalently,

$$
N_{t}=\sum_{j=1}^{\infty} I\left(S_{j} \leq t\right)
$$

The processes $\left(N_{t}\right), t \in \mathbb{R}_{+}$, and $\left(S_{j}\right), j \in \mathbb{N}_{0}$, are both called a renewal process. We say that a renewal occurs at $t$ if $S_{j}=t$ for some $j \geq 1$. The random variable$N_{t}$ represents the number of renewals in $[0, t]$. Since the interarrival times $T_{j}$ are independent and identically distributed, it follows that after each renewal the process restarts.

Let $M(t)=E N_{t}, 0 \leq t<\infty$. The function $M(t)$ is called the renewal function. It can be shown that $M(t)$ is finite for all $t$. From (B.1) we see that

$$
M(t)=\sum_{j=1}^{\infty} F^{* j}(t)
$$

where $F^{* j}$ denotes the $j$-fold convolution of $F$. If, for example, $F$ is a Gamma distribution with parameters 2 and $\lambda$, i.e., $F(t)=1-e^{-\lambda t}-\lambda t e^{-\lambda t}$, it can be shown that

$$
M(t)=\frac{\lambda t}{2}-\frac{1-e^{-2 \lambda t}}{4}
$$

Refer to $[1,31,32]$ for more general formulas for the renewal function of the Gamma distribution and expressions and bounds for other distributions. In Proposition B. 1 we show how $M$ can be determined (at least in theory) from $F$. It turns out that $M$ uniquely determines $F$.

Proposition B.1. There is a one-to-one correspondence between the interarrival distribution $F$ and the renewal function $M$.

Proof. We introduce the Laplace transform $L_{B}(s)=\int_{0}^{\infty} e^{-s x} d B(x)$, where $B: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$is a nondecreasing and right-continuous function. By taking the Laplace transform $L$ on both sides of formula (B.2) we obtain

$$
\begin{aligned}
L_{M}(s) & =\sum_{j=1}^{\infty} L_{F^{*} j}(s) \\
& =\sum_{j=1}^{\infty}\left(L_{F}(s)\right)^{j} \\
& =\frac{L_{F}(s)}{1-L_{F}(s)}
\end{aligned}
$$

or equivalently

$$
L_{F}(s)=\frac{L_{M}(s)}{1+L_{M}(s)}
$$

Hence $L_{F}$ is determined by $M$ and since the Laplace transform determines the distribution, it follows that $F$ also is determined by $M$.

The function $M(t)$ satisfies the following integral equation:

$$
M(t)=F(t)+\int_{0}^{t} M(t-x) d F(x)
$$i.e., $M=F+M * F$, where $*$ means convolution. This equation is referred to as the renewal equation, and is seen to hold by conditioning on the time of the first renewal. Upon doing so we obtain

$$
\begin{aligned}
M(t) & =\int_{0}^{\infty} E\left[N_{t} \mid T_{1}=x\right] d F(x) \\
& =\int_{0}^{t}[1+M(t-x)] d F(x) \\
& =F(t)+(M * F)(t)
\end{aligned}
$$

noting that if the first renewal occurs at time $x, x \leq t$, then from this point on the process restarts, and thus the expected number of renewals in $[0, t]$ is just 1 plus the expected number to arrive in a time $t-x$ from an equivalent renewal process. A more formal proof is the following;

$$
\begin{aligned}
M(t) & =E N_{t}=E \sum_{j=1}^{\infty} I\left(S_{j} \leq t\right)=F(t)+E \sum_{j=2}^{\infty} I\left(S_{j} \leq t\right) \\
& =F(t)+E \sum_{j=2}^{\infty} I\left(S_{j}-S_{1} \leq t-S_{1}\right) \\
& =F(t)+\int_{0}^{t} E \sum_{j=2}^{\infty} I\left(S_{j}-S_{1} \leq t-s\right) d F(s) \\
& =F(t)+\int_{0}^{t} M(t-s) d F(s)
\end{aligned}
$$

To generalize the renewal equation, we write

$$
g(t)=h(t)+(g * F)(t)
$$

where $h$ and $F$ are known and $g$ is an unknown function to be determined as a solution to (B.4). The solution of this equation is given by the following result.

Theorem B.2. If the function $g$ satisfies (B.4) and $h$ is bounded on finite intervals, then

$$
g(t)=h(t)+(h * M)(t)
$$

is a solution to (B.4) and the unique solution which is bounded on finite intervals.

Proof. A proof of this result is given in Asmussen [8], p. 113. A simpler proof can however be given in the case where the Laplace transform of $h$ and $g$ exists: Taking Laplace transforms in (B.4), yields

$$
L_{g}(s)=L_{h}(s)+L_{g}(s) L_{F}(s)
$$and it follows that

$$
\begin{aligned}
L_{g}(s) & =\frac{L_{h}(s)}{1-L_{F}(s)} \\
& =L_{h}(s)\left[1+\frac{L_{F}(s)}{1-L_{F}(s)}\right] \\
& =L_{h}(s)+L_{h}(s) L_{M}(s) \\
& =L_{h+h * M}(s)
\end{aligned}
$$

where the second last equality follows from (B.3). Since the Laplace transform uniquely determines the function, this gives the desired result.

Using the (strong) law of large numbers, many results related to renewal processes can be established, including the following.

Theorem B.3. With probability one,

$$
\frac{N_{t}}{t} \rightarrow \frac{1}{\mu} \quad \text { as } \quad t \rightarrow \infty
$$

Proof. By definition of $N_{t}$, it follows that

$$
S_{N_{t}} \leq t \leq S_{N_{t}+1}
$$

Hence,

$$
\frac{S_{N_{t}}}{N_{t}} \leq \frac{t}{N_{t}} \leq \frac{S_{N_{t}+1}}{N_{t}}
$$

Now the strong law of large numbers states that with probability one, $S_{j} / j \rightarrow$ $\mu$ as $j \rightarrow \infty$. As can be easily shown, $N_{t} \rightarrow \infty$ as $t \rightarrow \infty$, and thus

$$
\frac{S_{N_{t}}}{N_{t}} \rightarrow \mu \text { as } t \rightarrow \infty \quad(P \text {-a.s. }) .
$$

By the same argument, we also see that with probability one,

$$
\frac{S_{N_{t}+1}}{N_{t}}=\frac{S_{N_{t}+1}}{N_{t}+1} \frac{N_{t}+1}{N_{t}} \rightarrow \mu \cdot 1=\mu \quad \text { as } t \rightarrow \infty
$$

The result follows.

We now formulate some limiting results, without proof, including the Elementary Renewal Theorem, the Key Renewal Theorem, Blackwell's Theorem, and the Central Limit Theorem for renewal processes. Refer to Alsmeyer [1], Asmussen [8], Daley and Vere-Jones [58], and Ross [135] for proofs; see also Birolini [44]. Some of the results require that the distribution $F$ is not periodic (lattice). We say that $F$ is periodic if there exists a constant $c, c>0$, such that $T$ takes only values in $\{0, c, 2 c, 3 c, \ldots\}$.# Theorem B.4. (Elementary Renewal Theorem) 

$$
\lim _{t \rightarrow \infty} \frac{M(t)}{t}=\frac{1}{\mu}
$$

Theorem B.5. (Tightened Elementary Renewal Theorem). Assume that $\sigma^{2}=\operatorname{Var}[T]<\infty$. If the distribution $F$ is not periodic, then

$$
\lim _{t \rightarrow \infty}\left[M(t)-\frac{t}{\mu}\right]=\frac{\sigma^{2}-\mu^{2}}{2 \mu^{2}}
$$

Theorem B.6. Assume that $\sigma^{2}=\operatorname{Var}[T]<\infty$. If the distribution $F$ is not periodic, then

$$
\lim _{t \rightarrow \infty} \frac{\operatorname{Var}\left[N_{t}\right]}{t}=\frac{\sigma^{2}}{\mu^{3}}
$$

Before we state the Key Renewal Theorem, we need a definition. Let $g$ be a function defined on $\mathbb{R}_{+}$and for $h>0$ let

$$
g_{-}^{h}(x)=\inf _{0 \leq \delta \leq h} g(x-\delta), \quad g_{+}^{h}(x)=\sup _{0 \leq \delta \leq h} g(x-\delta)
$$

We say that $g$ is directly Riemann integrable if for any $h>0$;

$$
h \sum_{n=1}^{\infty}\left|g_{-}^{h}(n h)\right| \text { and } h \sum_{n=1}^{\infty}\left|g_{+}^{h}(n h)\right|
$$

are finite, and

$$
\lim _{h \rightarrow 0+} h \sum_{n=1}^{\infty} g_{-}^{h}(n h)=\lim _{h \rightarrow 0+} h \sum_{n=1}^{\infty} g_{+}^{h}(n h)
$$

In particular, a nonnegative, nonincreasing and integrable function is directly Riemann integrable. See $[58,88]$ for some other sufficient conditions for a function to be directly Riemann integrable.

Theorem B.7. (Key Renewal Theorem). Assume that the distribution $F$ is not periodic and $g$ is a directly Riemann integrable function. Then

$$
\lim _{t \rightarrow \infty} \int_{0}^{t} g(t-s) d M(s)=\frac{1}{\mu} \int_{0}^{\infty} g(s) d s
$$

Remark B.8. An alternative formulation of the Key Renewal Theorem is the following: If $g$ is bounded and integrable with $g(t) \rightarrow 0$ as $t \rightarrow \infty$, then $\lim _{t \rightarrow \infty} \int_{0}^{t} g(t-s) d M(s)=(1 / \mu) \int_{0}^{\infty} g(s) d s$ provided that $F$ is spread out. A distribution function is spread out if there exists an $n$ such that $F^{* n}$ has a nonzero absolutely continuous component with respect to Lebesgue measure, i.e., we can write $F^{* n}=G_{1}+G_{2}$, where $G_{1}, G_{2}$ are nonnegative measures on $\mathbb{R}_{+}$, and $G_{1}$ has a density with respect to Lebesgue measure.The Key Renewal Theorem is equivalent to Blackwell's Theorem below.
Theorem B.9. (Blackwell's Theorem). For a renewal process with a nonperiodic distribution $F$,

$$
\lim _{t \rightarrow \infty}[M(t)-M(t-s)]=\frac{s}{\mu}
$$

If $F$ has a density $f$, then $M$ has a density $m$, and

$$
m(t)=\sum_{j=1}^{\infty} f^{* j}(t)
$$

where $f^{* 1}=f$ and

$$
f^{* j}(t)=\int_{0}^{t} f^{*(j-1)}(t-s) f(s) d s, j=2,3, \ldots
$$

Under certain conditions the renewal density $m(t)$ converges to $1 / \mu$ as $t \rightarrow \infty$.
Theorem B.10. (Renewal Density Theorem). Assume that $F$ has a density $f$ with $f(t)^{p}$ integrable for some $p>1$, and $f(t) \rightarrow 0$ as $t \rightarrow \infty$. Then $M$ has a density $m$ such that

$$
\lim _{t \rightarrow \infty} m(t)=\frac{1}{\mu}
$$

Remark B.11. The conclusion of the theorem also holds true if $F$ has a density $f$, which is directly Riemann integrable, or if $F$ has finite mean and a bounded density $f$ satisfying $f(t) \rightarrow 0$ as $t \rightarrow \infty$.

Theorem B.12. (Central Limit Theorem). Assume that $\sigma^{2}=\operatorname{Var}[T]<$ $\infty$. Then $N_{t}$, suitably standardized, tends to a normal distribution as $t \rightarrow \infty$, i.e.,

$$
\lim _{t \rightarrow \infty} P\left(\frac{N_{t}-t / \mu}{\sqrt{t \sigma^{2} / \mu^{3}}} \leq x\right)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} e^{-\frac{1}{2} u^{2}} d u
$$

Next we formulate the limiting distribution of the forward and backward recurrence times $\alpha_{t}$ and $\beta_{t}$, defined by

$$
\begin{aligned}
& \alpha_{t}=S_{N_{t}+1}-t \\
& \beta_{t}=t-S_{N_{t}}
\end{aligned}
$$

The recurrence times $\alpha_{t}$ and $\beta_{t}$ are the time intervals from $t$ forward to the next renewal point and backward to the last renewal point (or to the time origin), respectively. Let $F_{\alpha_{t}}$ and $F_{\beta_{t}}$ denote the distribution functions of $\alpha_{t}$ and $\beta_{t}$, respectively. The following result is a consequence of the Key Renewal Theorem.Theorem B.13. Assume that the distribution $F$ is not periodic. Then the asymptotic distribution of the forward and backward recurrence times are given by

$$
\lim _{t \rightarrow \infty} F_{\alpha_{t}}(x)=\lim _{t \rightarrow \infty} F_{\beta_{t}}(x)=\frac{\int_{0}^{x} \bar{F}(s) d s}{\mu}
$$

This asymptotic distribution of $\alpha_{t}$ and $\beta_{t}$ is called the equilibrium distribution.

A simple formula exists for the mean forward recurrence time; we have

$$
E S_{N_{t}+1}=\mu(1+M(t))
$$

Formula B. 5 is a special case of Wald's equation (see, e.g., Ross [135]), and follows by writing

$$
\begin{aligned}
E S_{N_{t}+1} & =E \sum_{k \geq 1} S_{k} I\left(N_{t}+1=k\right)=E \sum_{k \geq 1} \sum_{j=1}^{k} T_{j} I\left(N_{t}+1=k\right) \\
& =E \sum_{j \geq 1} T_{j} I\left(N_{t}+1 \geq j\right)=E \sum_{j \geq 1} T_{j} I\left(S_{j-1} \leq t\right) \\
& =\sum_{j \geq 1} E T_{j} E I\left(S_{j-1} \leq t\right)=\mu \sum_{j \geq 0} F^{* j}(t)=\mu(1+M(t))
\end{aligned}
$$

Finally in this section we prove a result used in the proof of Theorem 4.19, p. 122 .

Proposition B.14. Let $g$ be a real-valued function which is bounded on finite intervals. Assume that

$$
\lim _{t \rightarrow \infty} g(t)=g
$$

Then

$$
\lim _{t \rightarrow \infty} \frac{1}{t} \int_{0}^{t} g(s) d M(s)=\frac{g}{\mu}
$$

Proof. To prove this result we use a standard $\epsilon$ argument. Given $\epsilon>0$, there exists a $t_{0}$ such that $|g(t)-g|<\epsilon$ for $t \geq t_{0}$. Hence for $t>t_{0}$ we have

$$
\begin{aligned}
& \frac{1}{t} \int_{0}^{t}|g(s)-g| d M(s) \\
& \quad \leq \frac{1}{t} \int_{0}^{t_{0}}|g(s)-g| d M(s)+\frac{1}{t} \int_{t_{0}}^{t} \epsilon d M(s)
\end{aligned}
$$

Since $t_{0}$ is fixed, this gives by applying the Elementary Renewal Theorem,

$$
\limsup _{t \rightarrow \infty} \frac{1}{t} \int_{0}^{t}|g(s)-g| d M(s) \leq \frac{\epsilon}{\mu}
$$

The desired conclusion follows.# B. 2 Renewal Reward Processes 

Let $(T, Y),\left(T_{1}, Y_{1}\right),\left(T_{2}, Y_{2}\right), \ldots$, be a sequence of independent and identically distributed pairs of random variables, with $T, T_{j} \geq 0$. We interpret $Y_{j}$ as the "reward" ("cost") associated with the $j$ th interarrival time $T_{j}$. The random variable $Y_{j}$ may depend on $T_{j}$. Let $Z_{t}$ denote the total reward earned by time $t$. We see that if the reward is earned at the time of the renewal,

$$
Z_{t}=\sum_{j=1}^{N_{t}} Y_{j}
$$

The limiting value of the average return is established using the law of large numbers and is given by the following result (cf. [135]).

Theorem B.15. If $E|Y|$ is finite, then
(i) With probability 1

$$
\begin{aligned}
& \frac{Z_{t}}{t} \rightarrow \frac{E Y}{E T} \quad \text { as } t \rightarrow \infty \\
& \frac{E Z_{t}}{t} \rightarrow \frac{E Y}{E T} \quad \text { as } t \rightarrow \infty
\end{aligned}
$$

Remark B.16. The conclusions of Theorem B. 15 also hold true if $Y \geq 0, E Y=$ $\infty$ and $E T<\infty$.

Many results from renewal theory can be generalized to renewal reward processes. For example Blackwell's Theorem holds:

$$
\lim _{t \rightarrow \infty}\left[Z_{t}-Z_{t-s}\right]=\frac{s E Y}{E T}
$$

The following theorem, which is a reformulation of Theorem 3.2, p. 136, in [8], generalizes the Central Limit Theorem for renewal processes, Theorem B.12.

Theorem B.17. Suppose $\operatorname{Var}[Y]<\infty$ and $\operatorname{Var}[T]<\infty$. Then as $t \rightarrow \infty$

$$
\sqrt{t}\left[\frac{Z_{t}}{t}-\frac{E Y}{E T}\right] \xrightarrow{D} \mathrm{~N}\left(0, \frac{\tau^{2}}{E T}\right)
$$

where

$$
\begin{aligned}
\tau^{2} & =\operatorname{Var}\left[Y-\frac{E Y}{E T} T\right] \\
& =\operatorname{Var}[Y]+\left(\frac{E Y}{E T}\right)^{2} \operatorname{Var}[T]-2 \frac{E Y}{E T} \operatorname{Cov}[Y, T]
\end{aligned}
$$# B. 3 Regenerative Processes 

The stochastic process $\left(X_{t}\right)$ is called regenerative if there exists a renewal process $\left(T_{j}\right)$ such that for $k \in \mathbb{N},\left(X_{t}\right)_{t \geq 0} \stackrel{D}{=}\left(X_{t+S_{k}}\right)_{t \geq 0}$, and

$$
\left(\left(X_{t+S_{k}}\right)_{t \geq 0},\left(T_{j}\right), j>k\right) \text { and }\left(\left(X_{t}\right)_{0 \leq t \leq S_{k}}, T_{1}, T_{2}, \ldots, T_{k}\right)
$$

are stochastically independent. Thus the continuation of the process beyond $S_{k}$ is a probabilistic replica of the whole process starting at 0 . The random times $S_{k}$ are said to be regenerative points for the process $\left(X_{t}\right)$ and the time interval $\left[S_{k-1}, S_{k}\right)$ is called the $k$ th cycle of the process.

In the following assume that the state space of $\left(X_{t}\right)$ equals $\mathbb{N}_{0}=\{0,1,2, \ldots\}$. Let

$$
P_{k}(t)=P\left(X_{t}=k\right), \quad k \in \mathbb{N}_{0}
$$

The following result taken from Ross [135] is stated without proof.

Theorem B.18. If the distribution of $T_{1}$ has an absolutely continuous component and $E T_{1}<\infty$, then

$$
\lim _{t \rightarrow \infty} P_{k}(t)=\frac{E \int_{0}^{T_{1}} I\left(X_{t}=k\right) d t}{E T_{1}}, \quad k \in \mathbb{N}_{0}
$$

Remark B.19. We see that if $\lim _{t \rightarrow \infty} P_{k}(t)=P_{k}$ exists, then

$$
\lim _{t \rightarrow \infty} \frac{1}{t} E \int_{0}^{t} I\left(X_{s}=k\right) d s=P_{k}
$$

The quantity $(1 / t) E \int_{0}^{t} I\left(X_{s}=k\right) d s$ represents the expected portion of time the process is in state $k$ in $[0, t]$. Since

$$
\frac{1}{t} E \int_{0}^{t} I\left(X_{s}=k\right) d s=\frac{1}{t} \int_{0}^{t} E I\left(X_{s}=k\right) d s=\frac{1}{t} \int_{0}^{t} P_{k}(s) d s
$$

this quantity is also equal to the average probability that the process is in state $k$.

## B. 4 Modified (Delayed) Processes

Consider a renewal process $\left(S_{j}\right)$ as defined in Sect. B.1, but assume now that the first interarrival time $T_{1}$ has a distribution $\tilde{F}$, that is not necessarily identical to $F$. The process is referred to as a modified renewal process (or a delayed renewal process). Similarly, we define a modified (delayed) renewal reward process and a modified (delayed) regenerative process. For the modified renewal reward process the distribution of the pair $\left(Y_{1}, T_{1}\right)$ is not necessarily the same as the pairs $\left(Y_{i}, T_{i}\right), i=2,3, \ldots$It can be shown that all the asymptotic results presented in the previous sections of this appendix still hold true for the modified processes. If we take the first distribution to be equal to the asymptotic distribution of the recurrence times, given by Theorem B.13, p. 279, the renewal process becomes stationary in the sense that the distribution of the forward recurrence time $\alpha_{t}$ does not depend on $t$. Furthermore,

$$
M(t+h)-M(t)=h / E T
$$# References 

[1] Alsmeyer, G. (1991) Erneuerungstheorie. Teubner Skripten zur Mathematischen Stochastik. B.G. Teubner, Stuttgart.
[2] Andersen, P. K., Borgan, Ø., Gill, R. and Keiding, N. (1992) Statistical Models Based on Counting Processes. Springer, New York.
[3] Arjas, E. (1993) Information and reliability: A Bayesian perspective. In: Barlow, R., Clarotti, C. and Spizzichino, F. (eds.): Reliability and Decision Making. Chapman \& Hall, London, pp. 115-135.
[4] Arjas, E. (1989) Survival models and martingale dynamics. Scand. J. Statist 16, 177-225.
[5] Arjas, E. (1981) A stochastic process approach to multivariate reliability systems: Notions based on conditional stochastic order. Mathematics of Operations Research 6, 263-276.
[6] Arjas, E. (1981) The failure and hazard processes in multivariate reliability systems. Mathematics of Operations Research 6, 551-562.
[7] Arjas, E. and Norros, I. (1989) Change of life distribution via hazard transformation: An inequality with application to minimal repair. Mathematics of Operations Research 14, 355-361.
[8] Asmussen, S. (1987) Applied Probability and Queues. Wiley, New York.
[9] Asmussen, S. (1984) Approximations for the probability of ruin within finite time. Scand. Actuarial J., 31-57.
[10] Aven, T. (2009) Optimal test interval for a monotone safety system. J. Applied Probability 46, 1-12.
[11] Aven, T. (1996) Availability analysis of monotone systems. In: S. Özekici (ed.): Reliability and Maintenance of Complex Systems. NATO ASI Series F, Springer, Berlin, pp. 206-223.
[12] Aven, T. (1996) Condition based replacement times - a counting process approach. Reliability Engineering and System Safety. Special issue on Maintenance and Reliability 51, 275-292.
[13] Aven, T. (1992) Reliability and Risk Analysis. Elsevier Applied Science, London.[14] Aven, T. (1990) Availability evaluation of flow networks with varying throughput-demand and deferred repairs. IEEE Trans. Reliability 38, $499-505$.
[15] Aven, T. (1987) A counting process approach to replacement models. Optimization 18, 285-296.
[16] Aven, T. (1985) A theorem for determining the compensator of a counting process. Scand. J. Statist. 12, 69-72.
[17] Aven, T. (1985) Reliability evaluation of multistate systems of multistate components. IEEE Trans. Reliability 34, 473-479.
[18] Aven, T. (1983) Optimal replacement under a minimal repair strategy - A general failure model. Adv. Appl. Prob. 15, 198-211.
[19] Aven, T. and Bergman, B. (1986) Optimal replacement times, a general set-up. J. Appl. Prob. 23, 432-442.
[20] Aven, T. and Castro, I. T. (2008) A delay time model with safety constraint. Reliability Engineering and System Safety 94, 261-267.
[21] Aven, T. and Dekker, R. (1997) A useful framework for optimal replacement models. Reliability Engineering and System Safety 58, 61-67.
[22] Aven, T. and Haukås, H. (1997) Asymptotic Poisson distribution for the number of system failures of a monotone system. Reliability Engineering and System Safety 58, 43-53.
[23] Aven, T. and Haukås, H. (1997) A note on the steady state availability of monotone systems. Reliability Engineering and System Safety 59, $269-276$.
[24] Aven, T. and Jensen, U. (1998) A general minimal repair model. Research report, University of Ulm.
[25] Aven, T. and Jensen, U. (1998) Information based hazard rates for ruin times of risk processes. Research Report, University of Ulm.
[26] Aven, T. and Jensen, U. (1997) Asymptotic distribution of the downtime of a monotone system. Mathematical Methods of Operations Research. Special issue on Stochastic Models of Reliability, 45, 355-375.
[27] Aven, T. and Opdal, K. (1996) On the steady state unavailability of standby systems. Reliability Engineering and System Safety 52, $171-175$.
[28] Aven, T. and Østebø, R. (1986) Two new component importance measures for a flow network system. Reliability Engineering 14, 75-80.
[29] Baker, R. D., Christer, A. H.(1994) Review of delay-time OR modelling of engineering aspects of maintenance. European Journal of Operational Research 73, 407-422.
[30] Barlow, R. and Hunter, L. (1960) Optimum preventive maintenance policies. Operations Res. 8, 90-100.
[31] Barlow, R. and Proschan, F. (1965) Mathematical Theory of Reliability. Wiley, New York.
[32] Barlow, R. and Proschan, F. (1975) Statistical Theory of Reliability and Life Testing. Holt, Rinehart and Winston, New York.[33] Basu, A. (1988) Multivariate exponential distributions and their applications in reliability. In: Krishnaiah, P. R. and Rao, C. R. (eds.): Handbook of Statistics 7. Quality Control and Reliability. North-Holland, Amsterdam, pp. 99-111.
[34] Baxter, L. A. (1981) Availability measures for a two-state system. J. Appl. Prob. 18, 227-235.
[35] Beichelt, F. (1993) A unifying treatment of replacement policies with minimal repair. Nav. Res. Log. Q. 40, 51-67.
[36] Beichelt, F. and Franken, F. (1984) Zuverlässigkeit und Instandhaltung. Carl Hanser Verlag, München.
[37] Berg, M. (1996) Economics oriented maintenance analysis and the marginal cost approach. In: Özekici, S. (ed.): Reliability and Maintenance of Complex Systems. NATO ASI Series F, Springer, Berlin, pp. 189-205.
[38] Bergman, B. (1978) Optimal replacement under a general failure model. Adv. Appl. Prob. 10, 431-451.
[39] Bergman, B. (1985) On reliability theory and its applications. Scand. J. Statist. 12, 1-41.
[40] Bergman, B. and Klefsjö, B. (1994) Quality. Studentlitteratur, Lund.
[41] Bertsekas, D. (1995) Dynamic Programming and Optimal Control. Vol. 1 and 2. Athena Scientific, Belmont.
[42] Billingsley, P. (1979) Probability and Measure. Wiley, New York.
[43] Birnbaum, Z. W. (1969) On the importance of different components in a multicomponent system. In: Krishnaiah, P. R. (ed.) Multivariate Analysis II, Academic Press, pp. 581-592.
[44] Birolini, A. (1994) Quality and Reliability of Technical Systems. Springer, Berlin.
[45] Birolini, A. (1985) On the use of Stochastic Processes in Modeling Reliability Problems. Lecture notes in Economics and Mathematical Systems 252, Springer, Berlin.
[46] Block, H. W. and Savits, T. H. (1997) Burn-In. Statistical Science 12, $1-19$.
[47] Block, H. W. and Savits, T. H. (1994) Comparison of maintenance policies. In: Shaked, M. and Shanthikumar, G. (eds.): Stochastic Orders and their Applications. Academic Press, Boston, pp. 463-484.
[48] Block, H. W., Borges, W. and Savits, T. H. (1985) Age-dependent minimal repair. J. Appl. Prob. 22, 370-385.
[49] Boland, P. and Proschan, F. (1994) Stochastic order in system reliability theory. In: Shaked, M. and Shanthikumar, G. (eds.): Stochastic Orders and their Applications. Academic Press, Boston, pp. 485-508.
[50] Brémaud, P. (1981) Point Processes and Queues. Martingale Dynamics. Springer, New York.
[51] Brown, M. and Proschan, F. (1983) Imperfect repair. J. Appl. Prob. 20, $851-859$.[52] Butler, D. A. (1979) A complete importance ranking for components of binary coherent systems, with extensions to multi-state systems. Nav. Res. Log. Q. 26, 565-578.
[53] Christer, A. H. (1999) Developments in delay time analysis for modelling plant maintenance. Journal of the Operational Research Society 50, 1120-1137.
[54] Christer, A. H. and Redmond D. F. (1992) Revising models of maintenance and inspection. International Journal of Production Economics 24, 227 - 234 .
[55] Çinlar, E. (1975) Superposition of point processes. In: Lewis, P. (ed.) Stochastic Point Processes. Wiley, New York, pp. 549-606.
[56] Constantini, C. and Spizzichino, F. (1997) Explicit solution of an optimal stopping problem: The burn-in of conditionally exponential components. J. Appl. Prob. 34, 267-282.
[57] Csenki, A. (1994) Cumulative operational time analysis of finite semiMarkov reliability models. Reliability Engineering and System Safety 44, 17-25.
[58] Daley, D. J. and Vere-Jones, D. (1988) An Introduction to the Theory of Point Processes. Springer, Berlin.
[59] Davis, M. H. A. (1993) Markov Models and Optimization. Chapman \& Hall, London.
[60] Delbaen, F. and Haezendonck, J. (1985) Inversed martingales in risk theory. Insurance: Mathematics and Economics 4, 201-206.
[61] Dellacherie, C. and Meyer, P. A. (1978) Probabilities and Potential A. North-Holland, Amsterdam.
[62] Dellacherie, C. and Meyer, P. A. (1980) Probabilities and Potential B. North-Holland, Amsterdam.
[63] Dekker, R. (1996) A framework for single-parameter maintenance activities and its use in optimisation, priority setting and combining. In: Özekici, S. (ed.): Reliability and Maintenance of Complex Systems. NATO ASI Series F, Springer, Berlin, pp. 170-188.
[64] Dekker, R. and Groenendijk, W. (1995) Availability assessment methods and their application in practice. Microelectron. Reliab. 35, 1257-1274.
[65] Donatiello, L. and Iyer, B. R. (1987) Closed-form solution for system availability distribution. IEEE Trans. Reliability 36, 45-47.
[66] Dynkin, E. B. (1965) Markov Processes. Springer, Berlin.
[67] Elliott, R. (1982) Stochastic Calculus and Applications. Springer, New York.
[68] Freund, J. E. (1961) A bivariate extension of the exponential distribution. J. Amer. Stat. Ass. 56, 971-977.
[69] Funaki, K. and Yoshimoto, K. (1994) Distribution of total uptime during a given time interval. IEEE Trans. Reliability 43, 489-492.
[70] Gaede, K.-W. (1977) Zuverlässigkeit, Mathematische Modelle. Carl Hanser Verlag, München.[71] Gandy, A. (2005). Effects of Uncertainties in Components on the Survival of Complex Systems with given Dependencies. In: Wilson, A., Limnios, N., Keller-McNulty, S. and Armijo, Y. (eds.): Modern Statistical and Mathematical Methods in Reliability. World Scientific, New Jersey, pp. 177-189.
[72] Gǎsemyr, J. and Aven, T. (1999) Asymptotic distributions for the downtimes of monotone systems. J. Appl. Prob., to appear.
[73] Gaver, D. P. (1963) Time to failure and availability of paralleled systems with repair. IEEE Trans. Reliability 12, 30-38.
[74] Gertsbakh, I. B. (1989) Statistical Reliability Theory. Marcel-Dekker, New York.
[75] Gertsbakh, I. B. (1984) Asymptotic methods in reliability: A review. Adv. Appl. Prob. 16, 147-175.
[76] Gnedenko, B. V. and Ushakov, I. A. (1995), edited by Falk, J. A. Probabilistic Reliability Engineering. Wiley, Chichester.
[77] Grandell, J. (1991) Aspects of Risk Theory. Springer, New York.
[78] Grandell, J. (1991) Finite time ruin probabilities and martingales. Informatica 2, 3-32.
[79] Griffith, W. S. (1980) Multistate reliability models. J. Appl. Prob. 15, $735-744$.
[80] Grimmelt, G. R. and Stirzaker, D. R. (1992) Probability and Random Processes. 2nd ed. Oxford Science Publication, Oxford.
[81] Haukǎs, H. and Aven, T. (1997) A general formula for the downtime of a parallel system. J. Appl. Prob. 33, 772-785.
[82] Haukǎs, H. and Aven, T. (1996) Formulae for the downtime distribution of a system observed in a time interval. Reliability Engineering and System Safety 52, 19-26.
[83] Heinrich, G. and Jensen, U. (1995) Parameter estimation for a bivariate lifetime distribution in reliability with multivariate extensions. Metrika 42, 49-65.
[84] Heinrich, G. and Jensen, U. (1996) Bivariate lifetime distributions and optimal replacement. Mathematical Methods of Operations Research 44, $31-47$.
[85] Heinrich, G. and Jensen, U. (1992) Optimal replacement rules based on different information levels. Nav. Res. Log. Q. 39, 937-955.
[86] Henley, E.J. and Kumamoto, H. (1981) Reliability Engineering and Risk Assessment. Prentice Hall, New Jersey.
[87] Herberts, T. and Jensen, U. (1998) Optimal stopping in a burn-in model. Research report, University of Ulm.
[88] Hinderer, H. (1987) Remarks on directly Riemann integrable functions. Mathematische Nachrichten 130, 225-230.
[89] Hokstad, P. (1997) The failure intensity process and the formulation of reliability and maintenance models. Reliability Engineering and System Safety 58, 69-82.[90] Høyland, A. and Rausand, M. (1994) System Reliability Theory, Wiley, New York.
[91] Hutchinson, T. P. and Lai, C. D. (1990) Continuous Bivariate Distributions, Emphasising Applications. Rumbsby Scientific Publishing, Adelaide.
[92] Jacod, J. (1975) Multivatiate point processes: predictable projection, Radon-Nikodym derivatives, representation of martingales. Z. für Wahrscheinlichkeitstheorie und Verw. Gebiete 31, 235-253.
[93] Jensen, U. and Hsu, G. (1993) Optimal stopping by means of point process observations with applications in reliability. Mathematics of Operations Research 18, 645-657.
[94] Jensen, U. (1996) Stochastic models of reliability and maintenance: an overview. In: S. Özekici (ed.): Reliability and Maintenance of Complex Systems. NATO ASI Series F, Springer, Berlin, pp. 3-36.
[95] Jensen, U. (1997) An optimal stopping problem in risk theory. Scand Actuarial J. 149-159.
[96] Jensen, U. (1990) A general replacement model. ZOR-Methods and Models of Operations Research 34, 423-439.
[97] Jensen, U. (1990) An example concerning the convergence of conditional expectations. Statistics 21, 609-611.
[98] Jensen, U. (1989) Monotone stopping rules for stochastic processes in a semimartingale representation with applications. Optimization 20, $837-852$.
[99] Joe, H. (1997). Multivariate Models and Dependence Concepts. Chapman \& Hall, Boca Raton.
[100] Kallianpur, G. (1980) Stochastic Filtering Theory. Springer, New York.
[101] Kallenberg, O. (1997) Foundations of Modern Probability. Springer, New York.
[102] Kaplan, N. (1981) Another look at the two-lift problem. J. Appl. Prob. 18, 697-706.
[103] Karr, A. F. (1986) Point Processes and their Statistical Inference. Marcel Dekker, New York.
[104] Keilson, J. (1966) A limit theorem for passage times in ergodic regenerative processes. Ann. Math. Stat. 37, 866-870.
[105] Keilson, J. (1979) Markov Chain Models - Rarity and Exponentiality. Springer, Berlin.
[106] Keilson, J. (1987) Robustness and exponentiality in redundant repairable systems. Annals of Operations Research 9, 439-447.
[107] Kijima, M. (1989) Some results for repairable systems. J. Appl. Prob. 26, 89-102.
[108] Koch, G. (1986) A dynamical approach to reliability theory. Proc. Int. School of Phys. "Enrico Fermi," XCIV. North-Holland, Amsterdam, pp. $215-240$.
[109] Kovalenko, I. N. (1994) Rare events in queueing systems - a survey. Queueing Systems 16, 1-49.[110] Kovalenko, I. N., Kuznetsov, N. Y., and Pegg, P. A. (1997) Mathematical Theory of Reliability of Time Dependent Systems with Practical Applications. Wiley, New York.
[111] Kovalenko, I. N., Kuznetsov, N. Y., and Shurenkov, V. M. (1996) Models of Random Processes. CRC Press, London.
[112] Kozlov, V. V. (1978) A limit theorem for a queueing system. Theory of Probability and its Application 23, 182-187.
[113] Kuo, W. and Kuo, Y. (1983): Facing the headaches of early failures: a state-of-the-art review of burn-in decisions. Proceedings of the IEEE 71, 1257-1266.
[114] Lam, T. and Lehoczky, J. (1991) Superposition of renewal processes. Adv. Appl. Prob. 23, 64-85.
[115] Last, G. and Brandt, A. (1995) Marked Point Processes on the Real Line - The Dynamic Approach. Springer, New York.
[116] Last, G. and Szekli, R. (1998) Stochastic comparison of repairable systems. J. Appl. Prob. 35, 348-370.
[117] Last, G. and Szekli, R. (1998) Time and Palm stationarity of repairable systems. Stoch. Proc. Appl., to appear.
[118] Leemis, L. M. and Beneke, M. (1990) Burn-in models and methods: a review. IIE Transactions 22, 172-180.
[119] Lehmann, A. (1998) Boundary crossing probabilities of Poisson counting processes with general boundaries. In: Kahle, W., Collani, E., Franz, J., and Jensen, U. (eds.): Advances in Stochastic Models for Reliability, Quality and Safety. Birkhäuser, Boston, pp. 153-166.
[120] Marcus, R. and Blumenthal, S. (1974) A sequential screening procedure. Technometrics 16, 229-234.
[121] Marshall, A. W. and Olkin, I. (1967) A multivariate exponential distribution. J. Amer. Stat. Ass. 62, 30-44.
[122] Métivier, M. (1982) Semimartingales, a Course on Stochastic Processes. De Gruyter, Berlin.
[123] Müller, A., Stoyan, D. (2002) Comparison Methods for Stochastic Models and Risks. John Wiley \& Sons, New York.
[124] Natvig, B. (1990) On information-based minimal repair and the reduction in remaining system lifetime due to the failure of a specific module. J. Appl. Prob. 27, 365-375.
[125] Natvig, B. (1988) Reliability: Importance of components. In: Johnson, N. and Kotz, S. (eds.): Encyclopedia of Statistical Sciences, vol. 8, Wiley, New York, pp. 17-20.
[126] Natvig, B. (1994) Multistate coherent systems. In: Johnson, N. and Kotz, S. (eds.): Encyclopedia of Statistical Sciences, vol. 5. Wiley, New York.
[127] Nelsen, R. B. (2006). An Introduction to Copulas. Springer, New York.
[128] Osaki, S. (1985) Stochastic System Reliability Modeling. World Scientific, Philadelphia.[129] Phelps, R. (1983) Optimal policy for minimal repair. J. Opl. Res. 34, $425-427$.
[130] Pierskalla, W. and Voelker, J. (1976) A survey of maintenance models: The control and surveillance of deteriorating systems. Nav. Res. Log. Q. 23, 353-388.
[131] Puterman, M. L. (1994) Markov Decision Processes: Discrete Stochastic Dynamic Programming. Wiley, New York.
[132] Rai, S. and Agrawal, D. P. (1990) Distributed Computing network reliability. 2nd ed. IEEE Computer Soc. Press, Los Alamitos, California.
[133] Rogers, C. and Williams, D. (1994) Diffusions, Markov Processes and Martingales, Vol. 1, 2nd ed. Wiley, Chichester.
[134] Rolski, T., Schmidli, H., Schmidt, V. and Teugels, J. (1999) Stochastic Processes for Insurance and Finance. Wiley, Chichester.
[135] Ross, S. M. (1970) Applied Probability Models with Optimization Applications. Holden-Day, San Francisco.
[136] Ross, S. M. (1975) On the calculation of asymptotic system reliability characteristics. In: Barlow R. E., Fussel, J. B. and Singpurwalla, N. D. (eds.) Fault Tree Analysis. Society for Industrial and Applied Mathematics, SIAM, Philadelphia, PA.
[137] Schöttl, A. (1997) Optimal stopping of a risk reserve process with interest and cost rates. J. Appl. Prob. 35, 115-123.
[138] Serfozo, R. (1980) High-level exceedances of regenerative and semistationary processes. J. Appl. Prob. 17, 423-431.
[139] Shaked, M. and Shanthikumar, G. (1993) Stochastic Orders and their Applications. Academic Press, Boston.
[140] Shaked, M. and Shanthikumar, G. (1991) Dynamic multivariate aging notions in reliability theory. Stoch. Proc. Appl. 38, 85-97.
[141] Shaked, M. and Shanthikumar, G. (1986) Multivariate imperfect repair. Oper. Res. 34, 437-448.
[142] Shaked, M. and Szekli, R. (1995) Comparison of replacement policies via point processes. Adv. Appl. Prob. 27, 1079-1103.
[143] Shaked, M. and Zhu, H. (1992) Some results on block replacement policies and renewal theory. J. Appl. Prob. 29, 932-946.
[144] Sherif, Y. and Smith, M. (1981) Optimal maintenance models for systems subject to failure. A review. Nav. Res. Log. Q. 28, 47-74.
[145] Smith, M. (1998) Insensitivity of the $k$ out of $n$ system. Probability in the Engineering and Informational Sciences, to appear.
[146] Smith, M. (1997) On the availability of failure prone systems. PhD thesis Erasmus University, Rotterdam.
[147] Smith, M., Aven, T., Dekker, R. and van der Duyn Schouten, F.A. (1997) A survey on the interval availability of failure prone systems. In: Proceedings ESREL'97 conference, Lisbon, 17-20 June, 1997, pp. 1727-1737.
[148] Solovyev, A.D. (1971) Asymptotic behavior of the time to the first occurrence of a rare event. Engineering Cybernetics 9 (6), 1038-1048.[149] Spizzichino, F. (1991) Sequential burn-in procedures. J. Statist. Plann. Inference 29, 187-197.
[150] Srinivasan, S.K. and Subramanian, R. (1980) Probabilistic Analysis of Redundant Systems. Lecture Notes in Economic and Mathematical Systems 175, Springer, Berlin.
[151] Stadje, W. and Zuckerman, D. (1991) Optimal maintenance strategies for repairable systems with general degree of repair. J. Appl. Prob. 28, $384-396$.
[152] Szász, D. (1977) A problem of two lifts. The Annals of Probability 5, $550-559$.
[153] Szász, D. (1975) On the convergence of sums of point processes with integer marks. In: Lewis, P. (ed.) Stochastic Point Processes., Wiley, New York, pp. 607-615.
[154] Takács, L. (1957) On certain sojourn time problems in the theory of stochastic processes. Acta Math. Acad. Sci. Hungar. 8, 169-191.
[155] Thompson, W. A. (1988) Point Process Models with Applications to Safety and Reliability. Chapman and Hall, New York.
[156] Tijms, H. C. (1994) Stochastic Modelling and Analysis: A Computational Approach. Wiley, New York.
[157] Ushakov, I. A. (ed.) (1994) Handbook of Reliability Engineering. Wiley, Chichester.
[158] Valdez-Flores, C. and Feldman, R. (1989) A survey of preventive maintenance models for stochastically deteriorating single-unit systems. Nav. Res. Log. Q. 36, 419-446.
[159] Van der Duyn Schouten, F. A. (1983) Markov Decision Processes with Continuous Time Parameter. Math. Centre Tracts 164, Amsterdam.
[160] Van Heijden, M. and Schornagel, A. (1988) Interval uneffectiveness distribution for a $k$-out-of- $n$ multistate reliability system with repair. European Journal of Operational Research 36, 66-77.
[161] Van Schuppen, J. (1977) Filtering, prediction and smoothing observations, a martingale approach. SIAM J. Appl. Math. 32, 552-570.
[162] Voina, A. (1982) Asymptotic analysis of systems with a continuous component. Kibernetika 18, 516-524.
[163] Wendt, H. (1998) A model describing damage processes and resulting first passage times. Research Report University of Magdeburg.
[164] Williams, D. (1991) Probability with Martingales. Cambridge University Press, Cambridge.
[165] Yashin, A. and Arjas, E. (1988) A note on random intensities and conditional survival functions. J. Appl. Prob. 25, 630-635.
[166] Yearout, R. D., Reddy, P., and Grosh, D. L. (1986) Standby redundancy in reliability - a review. IEEE Trans. Reliability 35, 285-292.# Index 

Accumulated failure rate, 36
Age replacement, 175
Alternating renewal process, 107, 161
Alternating renewal process, 14
Applications
availability analysis of gas compression system, 162
availability analysis of gas compression system, 13
reliability analysis of a nuclear power plant, 11
Associated variables, 30
Asymptotic results
backward recurrence time, 113
compound Poisson process, 152
distribution of number of failures, $113,125,136$
distribution of time to failure, 126
downtime distribution, 119, 145
downtime distribution, interval, 153
forward recurrence time, 113
highly available systems, 127
mean number of failures, 122
multistate monotone system, 162
number of failures, 116
parallel system, 139
series system, 142
Availability, 106
bound, 109, 114
demand availability, 160
interval (un)availability, 106
interval reliability, 106
limiting (un)availability, 109, 120, 168
long run average, 121
point availability, 106, 108, 120
steady-state (un)availability, 109, 120
throughput availability, 160
Availability, 8
Backward recurrence time, 108, 113, 278, 279
Binomial distribution, 22
Birnbaum's measure, 28
Birth and death process, 168
Bivariate exponential distribution, 197
Blackwell's theorem, 278
Block replacement, 177
Bounded in $L^{p}, 254$
Bridge structure, 25
Brownian motion, 5, 67, 71
Burn-in, 202
Cadlag, 254
Central limit theorem, 280
Change of time, 267
Closure theorem, 38
Coefficient of variation, 126, 137, 154, $163,167,171$
Coherent system, 20
Common mode failures, 30
Compensator, 62
Complex system
binary monotone system, 2, 17
hazard rate process, 73
multistate monotone system, 31
Complex systems
Copula models, 42Compound Poisson process, 4, 67, 152
Concordant, 46
Conditional expectation, 249
Control limit rule, 194
Copula, 42
Archimedian, 49
Counting process, 7, 62, 114
compensator, 62
intensity, 63
predictable intensity, 64
Cox process, 92
Critical component, 29
Critical path vector, 232
Cut set, 20
Cut vector, 32

Damage models, 3
Decreasing
(a,b)-decreasing, 188
Delay time model, 215
Delayed renewal process, 281
Demand availability, 160
Demand rate, 160
Dependence structure, 43
Dependent components, 30
failure rate process, 73
optimal replacement, 197
DFR (Decreasing Failure Rate), 5, 35
DFRA (Decreasing Failure Rate Average), 36
Discounted cost, 195
Doob-Meyer decomposition, 263
Downtime
distribution bounds, 118
distribution given failure, 145
distribution of the $i$ th failure, 149
distribution, interval, 118, 151
mean, interval, 116
steady-state distribution, 145

Elementary renewal theorem, 277
Equilibrium distribution, 113, 279
Erlang distribution, 163
Expectation, 247
Exponential distribution, 131
asymptotic limit, 127
mean number of system failures, 121
parallel system, 139
regenerative process, 124
renewal density, 114
standby system, 169
unavailability bound, 115
Exponential formula, 80

Factoring algorithm, 25
Failure rate, 1, 6, 12, 14, 26, 36, 64
accumulated, 36
process, 6, 65
process, monotone, 77
system, 123
Filtration, 57, 255
complete, 255
subfiltration, 69
Finite variation, 266
Flow network, 32
Forward recurrence time, 108, 113, 146, 278,279

Gas compression system, 13, 162
General repair strategy, 207

Harvesting problem, 182
Hazard function (cumulative), 1
Hazard rate, 1, 64
Hazard rate process, 70

IFR (Increasing Failure Rate), 3, 5, 35
IFR closure theorem, 40
IFRA (Increasing Failure Rate Average), 3, 36
IFRA closure theorem, 39
Iinfinitesimal generator, 66
Inclusion-exclusion method, 23, 33
Increasing
(a,b)-increasing, 188
Independence, 247
Indicator process, 70
Indistinguishable, 254
Infinitesimal look ahead, 181
Information levels, 4
change of, 78
Information-based replacement, 194
Innovation martingale, 63
Inspection, 229
Integrability, 58
Integrable, 254
Intensity, 63
marked point process, 83Interval (un)availability, 106
Interval reliability, 106, 110, 129
Inverse Gaussian distribution, 3, 5
k-out-of-n system, 19
reliability, 22
Key renewal theorem, 277
$\mathrm{L}^{p}$-space, 248
Laplace transform, 128, 141, 274
Lifetime distribution, 1, 26, 34
Long run average cost, 195
Lost throughput distribution, 159
Maintenance, 7
Marginal cost analysis, 179
Marked point process, 4, 81
Markov modulated repair process, 208
Markov process, 66
pure jump process, 66
Markov theory, 168
Markov modulated Poisson process, 65
Marshall-Olkin distribution, 52
Martingale, 59, 259
innovation, 63
orthogonal, 265
submartingale, 260
supermartingale, 259
Minimal cut set, 20
Minimal cut vector, 32
Minimal path set, 20
Minimal path vector, 32
Minimal repairs, 90
black box, 91
optimal operating time, 208
physical, 91
statistical, 91
Modified renewal process, 281
Monotone case, 181
Monotone system, 2, 17, 231
distribution of number of system failures, 125
downtime distribution, 148
k-out-of-n system, 19
mean number of system failures, 121
multistate, 158
parallel system, 18
point availability, 120
series system, 142
series system, 18
steady-state availability, 120
Monte Carlo simulation, 10
MTTF (Mean Time To Failure), 8, 107
MTTR (Mean Time To Repair), 8, 14, 107
Multistate monotone system, 31, 158, 168
Multivariate point process, 62
NBU (New Better than Used), 37
NBUE (New Better than Used in Expectation), 37
Normal distribution, 114, 119, 136, 157
Number of system failures
asymptotic results, 135
distribution, 109, 125
limiting mean, 116
mean, 121
standby system, 171
Number of system failures
mean, 109
NWU (New Worse than Used), 37
NWUE (New Worse than Used in Expectation), 37

Optimal replacement, 9
age replacement, 175
block replacement, 177
complex system, 194
general repair strategy, 207
Optimal stopping problem, 180
Optimization criterion, 180
Optional Sampling, 262
Optional sampling theorem, 67
Parallel system, 139
down time distribution, 146
downtime distribution of first failure, 150
downtime distribution, interval, 153
repair constraints, 165
Parallel system, 6, 18
optimal replacement, 9
reliability, 22
Partial information, 197, 208
Path set, 20
Path vector, 32
Performance measures, 14, 105, 168Phase-type distribution, 125, 163
PLOD (positive lower orthant dependent), 46
Point process, 62
compound, 87
marked point process, 81
multivariate, 62
Poisson approximation, 8, 125
Poisson distribution, 136, 143
Poisson process, 4, 65
doubly stochastic, 92
Markov modulated, 92
nonhomogeneous, 92
Predictable
variation, 264
Predictable
projection, 63
Predictable
intensity, 64
Predictable process, 58, 256
Preventive replacement, 175
Probability space, 57, 246
Product rule, 268
Progressively measurable, 256
Progressively measurable process, 58
PUOD (positive upper orthant dependent), 46

Quadratic variation, 265
Random variable, 247
Regenerative process, 124, 167, 281
Regular conditional expectation, 252
Reliability, 21
Reliability block diagram, 18
Reliability engineer, 9
Reliability importance measure, 27, 34
Birnbaum's measure, 28
Improvement potential, 28
Vesely-Fussell's measure, 28
Reliability modeling, 9
Renewal density, 114, 121, 148
Renewal density theorem, 278
Renewal equation, 275
Renewal function, 274
Renewal process, 273
alternating, 107
delayed, 281
modified, 281

Renewal process, 64
alternating, 82
intensity, 65
Renewal reward process, 280
Repair models, 81
minimal repairs, 90
varying degrees, 97
Repair replacement model, 207
Replacement model, 175
Risk process, 98
Ruin time, 99

Safety constraint, 216
Safety system, 229
semi-Markov theory, 169
Semimartingale, 267
change of filtration, 69
product rule, 68
semimartingale representation, 59
smooth semimartingale (SSM), 59
transformations, 68
Series system, 13, 18
lifetime distribution, 27
reliability, 21
Shock model, 185, 193
Shock models, 86
Shock process, 4
Simpson's paradox, 4
Standby system, 166
ample repair facilities, 172
one repair facility, 169
Stationary process, 119
Steady-state, 119
Stochastic comparison, 40
Stochastic order, 46
Stochastic process
predictable, 58
progressively measurable, 58
Stopping problem, 183
Stopping time, 59, 257
predictable, 72
totally inaccessible, 72
Structural importance, 29
Structure function, 18
Subadditive, 49
Subfiltration, 69, 190
Submartingale, 59
Supermartingale, 59Survival probability, 1, 13
System failure rate, 123, 127, 136
System failures, 85
System reliability, 21

Throughput availability, 160
Time to system failure
asymptotic distribution, 126
parallel system, 140
Unavailability, 109
Uniformly integrable, 58, 254
Usual conditions, 255
Wiener process, 3,5