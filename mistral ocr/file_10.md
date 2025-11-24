

# Probability Distributions Used in Reliability Engineering



RIAC is a DoD Information Analysis Center sponsored by the Defense Technical Information Center. RIAC is operated by a team of Wyle Laboratories, Quantenion Solutions, the University of Maryland, the Penn State University Applied Research Laboratory and the State University of New York Institute of Technology.# Probability Distributions Used in Reliability EngineeringProbability Distributions
Used in
Reliability Engineering

Andrew N. O'Connor

Center for Risk and Reliability
0151 Glenn L Martin Hall
University of Maryland
College Park, Maryland

Published by the Reliability Information Analysis Center (RIAC)
ISBN-10: 1-933904-06-2 (Hardcopy)
ISBN-13: 978-1-933904-06-1 (Hardcopy)
ISBN-10: 1-933904-07-0 (Electronic)
ISBN-13: 978-1-933904-07-8 (Electronic)

Copyright ${ }^{\circ} 2011$ by the Center for Reliability Engineering
University of Maryland, College Park, Maryland, USA
All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopying, recording, or by any information storage and retrieval system, without permission in writing from The Center for Reliability Engineering, Reliability Engineering Program.

The Center for Risk and Reliability
University of Maryland
College Park, Maryland 20742-7531# In memory of Willie Mae Webb 

This book is dedicated to the memory of Miss Willie Webb who passed away on April 102007 while working at the Center for Risk and Reliability at the University of Maryland (UMD). She initiated the concept of this book, as an aid for students conducting studies in Reliability Engineering at the University of Maryland. Upon passing, Willie bequeathed her belongings to fund a scholarship providing financial support to Reliability Engineering students at UMD. The proceeds from this book will go directly towards the Miss Willie M. Webb Scholarship..# Preface 

Reliability Engineers are required to combine a practical understanding of material science and engineering with statistics. The reliability engineer's understanding of statistics is focused on the practical application of a wide variety of accepted statistical methods. Most reliability texts provide only a basic introduction to probability distributions or only provide a detailed reference to few distributions. Detailed statistician texts provide theoretical detail which is outside the scope of likely reliability engineering tasks. As such the objective of this book is to provide a single reference text of closed form probability formulas and approximations used in reliability engineering.

This book provides details on 22 probability distributions. Each distribution section provides a graphical visualization and formulas for distribution parameters, along with distribution formulas. Common statistics such as moments and percentile formulas are followed by likelihood functions and in many cases the derivation of maximum likelihood estimates. Bayesian non-informative and conjugate priors are provided followed by a discussion on the distribution characteristics and applications in reliability engineering. Each section is concluded with online and hardcopy references which can provide further information followed by the relationship to other distributions.

The book is divided into six parts. Part 1 provides a brief coverage of the fundamentals of probability distributions within a reliability engineering context. Part 1 is limited to concise explanations aimed to familiarize readers. For further understanding the reader is referred to the references. Part 2 to Part 6 cover Common Life Distributions, Bathtub Distributions, Univariate Continuous Distributions, Univariate Discrete Distributions and Multivariate Distributions respectively.

This book refers to software available at www.enre.umd.edu/tools.htm aimed at students and academic staff which allow users to:

- Plot distributions and interactively vary distribution parameters to provide understanding on the effect each parameter has on the probability distribution function, cumulative distribution function and hazard rate.
- Export probability distribution plots directly to the printer, picture or to a chart object in Microsoft Excel.

The authors would like to thank the many students in the Reliability Engineering Program and Reuel Smith for proof reading..# Contents 

PREFACE ..... V
CONTENTS ..... I

1. FUNDAMENTALS OF PROBABILITY DISTRIBUTIONS ..... 1
1.1. Probability Theory ..... 2
1.1.1. Theory of Probability ..... 2
1.1.2. Interpretations of Probability Theory ..... 2
1.1.3. Laws of Probability. ..... 3
1.1.4. Law of Total Probability ..... 4
1.1.5. Bayes' Law ..... 4
1.1.6. Likelihood Functions ..... 5
1.1.7. Fisher Information Matrix ..... 6
1.2. Distribution Functions ..... 9
1.2.1. Random Variables ..... 9
1.2.2. Statistical Distribution Parameters ..... 9
1.2.3. Probability Density Function ..... 9
1.2.4. Cumulative Distribution Function ..... 11
1.2.5. Reliability Function ..... 12
1.2.6. Conditional Reliability Function ..... 13
1.2.7. 100a\% Percentile Function ..... 13
1.2.8. Mean Residual Life ..... 13
1.2.9. Hazard Rate ..... 13
1.2.10. Cumulative Hazard Rate ..... 14
1.2.11. Characteristic Function ..... 15
1.2.12. Joint Distributions ..... 16
1.2.13. Marginal Distribution ..... 17
1.2.14. Conditional Distribution ..... 17
1.2.15. Bathtub Distributions ..... 17
1.2.16. Truncated Distributions ..... 18
1.2.17. Summary ..... 19
1.3. Distribution Properties ..... 20
1.3.1. Median / Mode ..... 20
1.3.2. Moments of Distribution ..... 20
1.3.3. Covariance ..... 21
1.4. Parameter Estimation ..... 22
1.4.1. Probability Plotting Paper ..... 22
1.4.2. Total Time on Test Plots ..... 23
1.4.3. Least Mean Square Regression ..... 24
1.4.4. Method of Moments ..... 25
1.4.5. Maximum Likelihood Estimates ..... 26
1.4.6. Bayesian Estimation ..... 271.4.7. Confidence Intervals ..... 30
1.5. Related Distributions ..... 33
1.6. Supporting Functions ..... 34
1.6.1. Beta Function $\mathbf{B} \boldsymbol{x}, \boldsymbol{y}$ ..... 34
1.6.2. Incomplete Beta Function $\boldsymbol{B t t}(\boldsymbol{t} ; \boldsymbol{x}, \boldsymbol{y})$ ..... 34
1.6.3. Regularized Incomplete Beta Function $\boldsymbol{I t}(\boldsymbol{t} ; \boldsymbol{x}, \boldsymbol{y})$ ..... 34
1.6.4. Complete Gamma Function $\boldsymbol{\Gamma}(\boldsymbol{k})$ ..... 34
1.6.5. Upper Incomplete Gamma Function $\boldsymbol{\Gamma}(\boldsymbol{k}, \boldsymbol{t})$ ..... 35
1.6.6. Lower Incomplete Gamma Function $\boldsymbol{\gamma}(\boldsymbol{k}, \boldsymbol{t})$ ..... 35
1.6.7. Digamma Function $\boldsymbol{\psi} \boldsymbol{x}$ ..... 36
1.6.8. Trigamma Function $\boldsymbol{\psi}^{\prime} \boldsymbol{x}$ ..... 36
1.7. Referred Distributions ..... 37
1.7.1. Inverse Gamma Distribution $\boldsymbol{I G}(\boldsymbol{\alpha}, \boldsymbol{\beta})$ ..... 37
1.7.2. Student T Distribution $\boldsymbol{T}(\boldsymbol{\alpha}, \boldsymbol{\mu}, \boldsymbol{\sigma} \mathbf{2})$ ..... 37
1.7.3. F Distribution $\boldsymbol{F}(\boldsymbol{n} \mathbf{1}, \boldsymbol{n} \mathbf{2})$ ..... 37
1.7.4. Chi-Square Distribution $\boldsymbol{\chi} \mathbf{2}(\boldsymbol{v})$ ..... 37
1.7.5. Hypergeometric Distribution $\boldsymbol{H}$ yperGeom $(\boldsymbol{k} ; \boldsymbol{n}, \boldsymbol{m}, \boldsymbol{N})$ ..... 38
1.7.6. Wishart Distribution $\boldsymbol{W i s h a r t d}(\boldsymbol{x} ; \boldsymbol{\Sigma}, \boldsymbol{n})$ ..... 38
1.8. Nomenclature and Notation ..... 39
2. COMMON LIFE DISTRIBUTIONS ..... 40
2.1. Exponential Continuous Distribution ..... 41
2.2. Lognormal Continuous Distribution ..... 49
2.3. Weibull Continuous Distribution ..... 59
3. BATHTUB LIFE DISTRIBUTIONS ..... 68
3.1. 2-Fold Mixed Weibull Distribution ..... 69
3.2. Exponentiated Weibull Distribution ..... 76
3.3. Modified Weibull Distribution ..... 81
4. UNIVARIATE CONTINUOUS DISTRIBUTIONS ..... 85
4.1. Beta Continuous Distribution ..... 86
4.2. Birnbaum Saunders Continuous Distribution ..... 934.3. Gamma Continuous Distribution ..... 99
4.4. Logistic Continuous Distribution ..... 108
4.5. Normal (Gaussian) Continuous Distribution ..... 115
4.6. Pareto Continuous Distribution ..... 125
4.7. Triangle Continuous Distribution ..... 131
4.8. Truncated Normal Continuous Distribution ..... 135
4.9. Uniform Continuous Distribution ..... 145
5. UNIVARIATE DISCRETE DISTRIBUTIONS ..... 151
5.1. Bernoulli Discrete Distribution ..... 152
5.2. Binomial Discrete Distribution ..... 157
5.3. Poisson Discrete Distribution ..... 165
6. BIVARIATE AND MULTIVARIATE DISTRIBUTIONS ..... 172
6.1. Bivariate Normal Continuous Distribution ..... 173
6.2. Dirichlet Continuous Distribution ..... 181
6.3. Multivariate Normal Continuous Distribution ..... 187
6.4. Multinomial Discrete Distribution ..... 193
7. REFERENCES ..... 201# iV Probability Distributions Used in Reliability Engineering# 1. Fundamentals of Probability Distributions# 1.1. Probability Theory 

### 1.1.1. Theory of Probability

The theory of probability formalizes the representation of probabilistic concepts through a set of rules. The most common reference to formalizing the rules of probability is through a set of axioms proposed by Kolmogorov in 1933. Where $E_{i}$ is an event in the event space $\Omega=U_{i=1}^{n} E_{i}$ with $n$ different events.

$$
\begin{gathered}
0 \leq P\left(E_{i}\right) \leq 1 \\
P(\Omega)=1 \text { and } P(\phi)=0 \\
P\left(E_{1} \cup E_{2}\right)=P\left(E_{1}\right)+P\left(E_{2}\right)
\end{gathered}
$$

When $E_{1}$ and $E_{2}$ are mutually exclusive.
Other representations of probabilistic concepts exist such as fuzzy logic and theory of evidence (Dempster-Shafer model) which do not follow the theory of probability. For a justification of probability theory see (Singpurwalla 2006).

### 1.1.2. Interpretations of Probability Theory

In probability theory there exist many conceptual interpretations. The two most common interpretations are:

- Frequency Interpretation. Using the frequency interpretation of probability, the probability of an event (failure) is defined as:

$$
P(K)=\lim _{n \rightarrow \infty} \frac{n_{f}}{n}
$$

Also known as the classical approach, this approach assumes there exists an exact probability of an event occurring is $p$. The analyst uses the observed frequency of the event to estimate the value of $p$. The more historic events that have occurred, the more confident the analyst is of their estimation of $p$. This approach does have limitations, for instance when data from events are not available (e.g. no failures occur in a test) $p$ cannot be estimated and this method cannot incorporate "soft data" such as expert opinion.

- Subjective Interpretation. The subjective interpretation of probability is also known as personal probability. This method defines the probability of an event as degree of belief the analyst has on an outcome. This means probability is a product of the analyst's state of knowledge. Any evidence which would change the analyst's degree of belief must be considered when calculating the probability (including soft evidence). The assumption is made that the probability assessment is made by a coherent person where any coherent person having the same state of knowledge would make the same assessment.The subjective interpretation has the flexibility of including many types of evidence to assist in estimating the probability of an event. This is important in many reliability application where the event of interest (e. g, system failure) are rare.

# 1.1.3. Laws of Probability 

The following formulas are used to apply mathematical operations consistent with the theory of probability.

Let $X=E_{i}$ and $Y=E_{j}$ be two events within the sample space $\Omega$ where $i \neq j$.
Boolean Laws of probability are (Modarres et al. 1999, p.25):

$$
\begin{aligned}
X \cup Y & =Y \cup X & & \text { Commutative Law } \\
X \cap Y & =Y \cap X & & \\
X \cup(Y \cup Z) & =(X \cup Y) \cup Z & & \text { Associative Law } \\
X \cap(Y \cap Z) & =(X \cap Y) \cap Z & & \\
X \cap(Y \cup Z) & =(X \cap Y) \cup(X \cap Z) & & \text { Distributive Law } \\
X \cup X & =X & & \text { Idempotent Law } \\
X \cap X & =X & & \\
X \cup \bar{X} & =\Omega & & \text { Complementation Law } \\
X \cap \bar{X} & =\emptyset & & \\
\bar{X} & =X & & \\
\frac{(X \cup Y)}{(X \cap Y)} & =\bar{X} \cap \bar{Y} & & \text { De Morgan's Theorem }
\end{aligned}
$$

Two events are mutually exclusive if:

$$
X \cap Y=\emptyset, \quad P(X \cap Y)=0
$$

Two events are independent if one event $Y$ occurring does not affect the probability of the second event $X$ occurring:

$$
P(X \mid Y)=P(X)
$$

The rules for evaluating the probability of compound events are:
Addition Rule:

$$
\begin{aligned}
P(X \cup Y) & =P(X)+P(Y)-P(X \cap Y) \\
& =P(X)+P(Y)-P(X) P(Y \mid X)
\end{aligned}
$$

Multiplication Rule:

$$
P(X \cap Y)=P(X) P(Y \mid X)=P(Y) P(X \mid Y)
$$

When $X$ and $Y$ are independent:

$$
\begin{gathered}
P(X \cup Y)=P(X)+P(Y)-P(X) P(Y) \\
P(X \cap Y)=P(Y) P(Y)
\end{gathered}
$$Generalizations of these equations:

$$
\begin{aligned}
P\left(E_{1} \cup E_{2} \cup \ldots \cup E_{n}\right)= & {\left[P\left(E_{1}\right)+P\left(E_{2}\right)+\cdots+P\left(E_{n}\right)\right] } \\
& -\left[P\left(E_{1} \cap E_{2}\right)+P\left(E_{1} \cap E_{3}\right)+\cdots+P\left(E_{n-1} \cap E_{n}\right)\right] \\
& +\left[P\left(E_{1} \cap E_{2} \cap E_{3}\right)+P\left(E_{1} \cap E_{2} \cap E_{4}\right)+\cdots\right] \\
& -\cdots(-1)^{n+1}\left[P\left(E_{1} \cap E_{2} \cap \ldots \cap E_{n}\right)\right] \\
P\left(E_{1} \cap E_{2} \cap \ldots \cap E_{n}\right)= & P\left(E_{1}\right) \cdot P\left(E_{2} \mid E_{1}\right) \cdot P\left(E_{3} \mid E_{1} \cap E_{2}\right) \\
& \ldots P\left(E_{n} \mid E_{1} \cap E_{2} \cap \ldots \cap E_{n-1}\right)
\end{aligned}
$$

# 1.1.4. Law of Total Probability 

The probability of $X$ is obtained by the summation of its disjointed parts. This can be generalized by defining, $A=\left\{A_{1}, A_{2}, \ldots, A_{n_{A}}\right\}$ where $A$ is a subset of the sample space, $A \subseteq \Omega$ and all the elements of $A$ are mutually exclusive, $A_{i} \cap A_{j}=\emptyset$, but the union of all $A$ elements cover the complete sample space, $\cup_{i=1}^{n_{A}} A_{i}=\Omega$. Then:

$$
P(X)=\sum_{i=1}^{n_{A}} P\left(A_{i}\right) P\left(X \mid A_{i}\right)
$$

For example:

$$
\begin{aligned}
P(X) & =P(X \cap Y)+P(X \cap \bar{Y}) \\
& =P(Y) P(X \mid Y)+P(Y) P(X \mid \bar{Y})
\end{aligned}
$$

### 1.1.5. Bayes' Law

Bayes' law, also known as the law of inverse probability, can be derived from the multiplication rule and the law of total probability as follows:

$$
\begin{gathered}
P(\theta) P(E \mid \theta)=P(E) P(\theta \mid E) \\
P(\theta \mid E)=\frac{P(\theta) P(E \mid \theta)}{P(E)} \\
P(\theta \mid E)=\frac{P(\theta) P(E \mid \theta)}{\sum_{i=1}^{n_{E}} P\left(E \mid \theta_{i}\right) P\left(\theta_{i}\right)}
\end{gathered}
$$

If we use this formula for an observed evidence, $E$, to make inference about the unobserved $\theta$ the following definitions make up Bayes' Law:
$\theta \quad$ the unknown of interest (UOI).
$E \quad$ the observed random variable, evidence.
$P(\theta) \quad$ the prior state of knowledge about $\theta$ without the evidence. Also denoted as $\pi_{o}(\theta)$.
$P(E \mid \theta) \quad$ the likelihood of observing the evidence given the UOI. Also denoted as $L(E \mid \theta)$.$P(\theta \mid E) \quad$ the posterior state of knowledge about $\theta$ given the evidence. Also denoted as $\pi(\theta \mid E)$.
$\sum_{i=1}^{n_{p}} P\left(E \mid \theta_{i}\right) P(\theta)$ is the normalizing constant.
The continuous form of Bayes' Law can be written as:

$$
\pi(\theta \mid E)=\frac{\pi_{\mu}(\theta) L(E \mid \theta)}{\int \pi_{\mu}(\theta) L(E \mid \theta) d \theta}
$$

In Bayesian statistics the state of knowledge (uncertainty) of an unknown of interest (UOI) is quantified by assigning a probability distribution to its possible values. Bayes' law provides a mathematical means by which this uncertainty can be updated given new evidence.

# 1.1.6. Likelihood Functions 

The likelihood function is the probability of observing the evidence (e.g., sample data), $E$, given the distribution parameters, $\theta$. The probability of observing event 1 AND event 2 AND event $n$ is the product of each event likelihood. The likelihood function is not dependent on the order of each event.

$$
L(\theta \mid E)=c \Pi L_{i}\left(\theta \mid t_{i}\right)
$$

$c$ is a combinatorial constant which quantifies the number of combination which the observed evidence could have occurred. Methods which use the likelihood function do not depend on the constant and so it is omitted.

The following table summarizes the likelihood functions for different types of observations:

Table 1: Summary of Likelihood Functions (Klein \& Moeschberger 2003, p.74)

| Type of Observation | Likelihood Function | Example Description |
| :-- | :--: | :-- |
| Exact Lifetimes | $L_{i}\left(\theta \mid t_{i}\right)=f\left(t_{i} \mid \theta\right)$ | Failure time is known |
| Right Censored | $L_{i}\left(\theta \mid t_{i}\right)=R\left(t_{i} \mid \theta\right)$ | Component survived to time $t_{i}$ |
| Left Censored | $L_{i}\left(\theta \mid t_{i}\right)=F\left(t_{i} \mid \theta\right)$ | Component failed before time $t_{i}$ |
| Interval Censored | $L_{i}\left(\theta \mid t_{i}\right)=F\left(t_{i}^{R i} \mid \theta\right)-F\left(t_{i}^{L i} \mid \theta\right)$ | Component failed between <br> $t_{i}^{L i}$ and $t_{i}^{R i}$ |
| Left Truncated | $L_{i}\left(\theta \mid t_{i}\right)=\frac{f\left(t_{i} \mid \theta\right)}{R\left(t_{i} \mid \theta\right)}$ | Component failed at time $t_{i}$ where <br> observations are truncated before $t_{i}$. |
| Right Truncated | $L_{i}\left(\theta \mid t_{i}\right)=\frac{f\left(t_{i} \mid \theta\right)}{F\left(t_{i} \mid \theta\right)}$ | Component failed at time $t_{i}$ where <br> observations are truncated after $t_{i}$. |
| Interval Truncated | $L_{i}\left(\theta \mid t_{i}\right)=\frac{f\left(t_{i} \mid \theta\right)}{F\left(t_{i} \mid \theta\right)-F\left(t_{i} \mid \theta\right)}$ | Component failed at time $t_{i}$ where <br> observations are truncated before $t_{i}$. <br> and after $t_{i}$. |The Likelihood function is used in Bayesian inference and maximum likelihood parameter estimation techniques. In both instances any constant in front of the likelihood function becomes irrelevant. Such constants are therefore not included in the likelihood functions given in this book (nor in most references).

For example, consider the case where a test is conducted on $n$ components with an exponential time to failure distribution. The test is terminated at $t_{s}$ during which $r$ components failed at times $t_{1}, t_{2}, \ldots, t_{r}$ and $s=n-r$ components survived. Using the exponential distribution to construct the likelihood function we obtain:

$$
\begin{aligned}
L(\lambda \mid E) & =\prod_{i=1}^{n_{F}} f\left(\lambda \mid t_{i}^{F}\right) \prod_{i=1}^{n_{S}} R\left(\lambda \mid t_{i}^{S}\right) \\
& =\prod_{i=1}^{n_{F}} \lambda e^{-\lambda t_{i}^{F}} \prod_{i=1}^{n_{S}} e^{-\lambda t_{i}^{S}} \\
& =\lambda^{n_{F}} e^{-\lambda \sum_{i=1}^{n_{F}} t_{i}^{F}} e^{-\lambda \sum_{i=1}^{n_{S}} t_{i}^{S}} \\
& =\lambda^{n_{F}} e^{-\lambda\left(\sum t_{i}^{F}+\sum t_{i}^{S}\right)}
\end{aligned}
$$

Alternatively, because the test described is a homogeneous Poisson process ${ }^{1}$ the likelihood function could also have been constructed using a Poisson distribution. The data can be stated as seeing $r$ failure in time $t_{T}$ where $t_{T}$ is the total time on test $t_{T}=\sum_{i=1}^{n_{F}} t_{i}^{F}+\sum_{i=1}^{n_{S}} t_{i}^{S}$. Therefore the likelihood function would be:

$$
\begin{aligned}
L(\lambda \mid E) & =f\left(\lambda \mid n_{F}, t_{T}\right) \\
& =\frac{\left(\lambda t_{T}\right)^{n_{F}}}{n_{F}!} e^{-\lambda t_{T}} \\
& =c \lambda^{n_{F}} e^{-\lambda t_{T}} \\
& =\lambda^{n_{F}} e^{-\lambda\left(\sum t_{i}^{F}+\sum t_{i}^{S}\right)}
\end{aligned}
$$

As mentioned earlier, in estimation procedures within this book, the constant $c$ can be ignored. As such, the two likelihood functions are equal. For more information see (Meeker \& Escobar 1998, p.36) or (Rinne 2008, p.403).

# 1.1.7. Fisher Information Matrix 

The Fisher Information Matrix has many uses but in reliability applications it is most often used to create Jeffery's non-informative priors. There are two types of Fisher information matrices, the Expected Fisher Information Matrix $I(\theta)$, and the Observed Fisher Information Matrix $J(\theta)$.

[^0]
[^0]:    ${ }^{1}$ Homogeneous in time, where it does not matter if you have $n$ components on test at once (exponential test), or you have a single component on test which is replaced after failure $n$ times (Poisson process), the evidence produced will be the same.The Expected Fisher Information Matrix is obtained from a log-likelihood function from a single random variable. The random variable is replaced by its expected value.

For a single parameter distribution:

$$
I(\theta)=-E\left[\frac{\partial^{2} \Lambda(\theta \mid x)}{\partial \theta^{2}}\right]=\left[\left(\frac{\partial \Lambda(\theta \mid x)}{\partial \theta}\right)^{2}\right]
$$

where $\Lambda$ is the log-likelihood function and $E[U]=\int U f(x) d x$. For a distribution with $p$ parameters the Expected Fisher Information Matrix is:

$$
I(\boldsymbol{\theta})=\left[\begin{array}{cccc}
-E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{1}^{2}}\right] & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{1} \partial \theta_{2}}\right] & \cdots & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{1} \partial \theta_{p}}\right] \\
-E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{2} \partial \theta_{1}}\right] & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{2}^{2}}\right] & \cdots & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{2} \partial \theta_{p}}\right] \\
-1 & \vdots & \ddots & \ddots & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{p} \partial \theta_{1}}\right] \\
-E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{p} \partial \theta_{1}}\right] & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{p} \partial \theta_{2}}\right] & \cdots & -E\left[\frac{\partial^{2} \Lambda(\boldsymbol{\theta} \mid \boldsymbol{x})}{\partial \theta_{p}^{2}}\right]
\end{array}\right]
$$

The Observed Fisher Information Matrix is obtained from a likelihood function constructed from $n$ observed samples from the distribution. The expectation term is dropped.

For a single parameter distribution:

$$
J_{n}(\theta)=-\sum_{i=1}^{n} \frac{\partial^{2} \Lambda\left(\theta \mid x_{i}\right)}{\partial \theta^{2}}
$$

For a distribution with $p$ parameters the Observed Fisher Information Matrix is:

$$
J_{n}(\boldsymbol{\theta})=\sum_{i=1}^{n}\left[\begin{array}{cccc}
-\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{1}^{2}} & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{1} \partial \theta_{2}} & \cdots & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{1} \partial \theta_{p}} \\
-\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{2} \partial \theta_{1}} & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{2}^{2}} & \cdots & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{2} \partial \theta_{p}} \\
& \vdots & \ddots & \ddots & - \\
-\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{p} \partial \theta_{1}} & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{p} \partial \theta_{2}} & \cdots & -\frac{\partial^{2} \Lambda\left(\boldsymbol{\theta} \mid \boldsymbol{x}_{i}\right)}{\partial \theta_{p}^{2}}
\end{array}\right]
$$

It can be seen that as $n$ becomes large, the average value of the random variable approaches its expected value and so the following asymptotic relationship exists between the observed and expected Fisher information matrices:

$$
\operatorname{plim}_{n \rightarrow \infty} \frac{1}{n} J_{n}(\boldsymbol{\theta})=I(\boldsymbol{\theta})
$$

For large $n$ the following approximation can be used:

$$
J_{n} \approx n I(\boldsymbol{\theta})
$$When evaluated at $\boldsymbol{\theta}=\overline{\boldsymbol{\theta}}$ the observed Fisher information matrix estimates the variancecovariance matrix:

$$
\boldsymbol{V}=\left[J_{n}(\boldsymbol{\theta}=\overline{\boldsymbol{\theta}})\right]^{-1}=\left[\begin{array}{cccc}
\operatorname{Var}\left(\tilde{\theta}_{1}\right) & \operatorname{Cov}\left(\tilde{\theta}_{1}, \tilde{\theta}_{2}\right) & \cdots & \operatorname{Cov}\left(\tilde{\theta}_{1}, \tilde{\theta}_{d}\right) \\
\operatorname{Cov}\left(\tilde{\theta}_{1}, \tilde{\theta}_{2}\right) & \operatorname{Var}\left(\tilde{\theta}_{2}\right) & \cdots & \operatorname{Cov}\left(\tilde{\theta}_{2}, \tilde{\theta}_{d}\right) \\
\vdots & \vdots & \ddots & \vdots \\
\operatorname{Cov}\left(\tilde{\theta}_{1}, \tilde{\theta}_{d}\right) & \operatorname{Cov}\left(\tilde{\theta}_{2}, \tilde{\theta}_{d}\right) & \cdots & \operatorname{Var}\left(\tilde{\theta}_{d}\right)
\end{array}\right]
$$# 1.2. Distribution Functions 

### 1.2.1. Random Variables

Probability distributions are used to model random events for which the outcome is uncertain such as the time of failure for a component. Before placing a demand on that component, the time it will fail is unknown. The distribution of the probability of failure at different times is modeled by a probability distribution. In this book random variables will be denoted as capital letter such as $T$ for time. When the random variable assumes a value we denote this by small caps such as $t$ for time. For example, if we wish to find the probability that the component fails before time $t_{1}$ we would find $P\left(T \leq t_{1}\right)$.

Random variables are classified as either discrete or continuous. In a discrete distribution, the random variable can take on a distinct or countable number of possible values such as number of demands to failure. In a continuous distribution the random variable is not constrained to distinct possible values such as time-to-failure distribution.

This book will denote continuous random variables as $X$ or $T$, and discrete random variables as $K$.

### 1.2.2. Statistical Distribution Parameters

The parameters of a distribution are the variables which need to be specified in order to completely specify the distribution. Often parameters are classified by the effect they have on the distributions. Shape parameters define the shape of the distribution, scale parameters stretch the distribution along the random variable axis, and location parameters shift the distribution along the random variable axis. The reader is cautioned that the parameters for a distribution may change depending on the text. Therefore, before using formulas from other sources the parameterization need to be confirmed.

Understanding the effect of changing a distribution's parameter value can be a difficult task. At the beginning of each section a graph of the distribution is show with varied parameters. For a better understanding the reader is referred to the companion software Probability Distribution Plotter, available at www.enre.umd.edu/tools.htm. The reader can use sliders to change parameters and observe the change in the probability density function, cumulative density function or hazard rate.

### 1.2.3. Probability Density Function

A probability density function (pdf), denoted as $f(t)$ is any function which is always positive and has a unit area:

$$
\int_{-\infty}^{\infty} f(t) d t=1, \quad \sum_{k} f(k)=1
$$The probability of an event occurring between limits a and b is the area under the pdf:

$$
\begin{gathered}
P(a \leq T \leq b)=\int_{a}^{b} f(t) d t=F(b)-F(a) \\
P(a \leq K \leq b)=\sum_{i=a}^{b} f(k)=F(b)-F(a-1)
\end{gathered}
$$

The instantaneous value of a discrete pdf at $k_{i}$ can be obtained by minimizing the limits to $\left[k_{i-1}, k_{i}\right]$ :

$$
P\left(K=k_{i}\right)=P\left(k_{i}<K \leq k_{i}\right)=f(k)
$$

The instantaneous value of a continuous pdf is infinitesimal. This result can be seen when minimizing the limits to $[t, t+\Delta t]$ :

$$
P(T=t)=\lim _{\Delta t \rightarrow 0} P(t<T \leq t+\Delta t)=\lim _{\Delta t \rightarrow 0} f(t) \cdot \Delta t
$$

Therefore the reader must remember that in order to calculate the probability of an event, an interval for the random variable must be used. Furthermore, a common misunderstanding is that a pdf cannot have a value above one because the probability of an event occurring cannot be greater than one. As can be seen above this is true for discrete distributions, only because $\Delta k=1$. However for continuous the case the pdf is multiplied by a small interval $\Delta t$, which ensures that the probability an event occurring within the interval $\Delta t$ is less than one.


Figure 1: Left: continuous pdf, right: discrete pdf
To derive the continuous pdf relationship to the cumulative density function (cdf), $F(t)$ :

$$
\begin{gathered}
\lim _{\Delta t \rightarrow 0} f(t) \cdot \Delta t=\lim _{\Delta t \rightarrow 0} P(t<T \leq t+\Delta t)=\lim _{\Delta t \rightarrow 0} F(t+\Delta t)-F(t)=\lim _{\Delta t \rightarrow 0} \Delta F(t) \\
f(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta F(t)}{\Delta t}=\frac{d F(t)}{d t}
\end{gathered}
$$

The shape of the pdf can be obtained by plotting a normalized histogram of an infinite number of samples from a distribution.It should be noted when plotting a discrete pdf the points from each discrete value should not be joined. For ease of explanation using the area under the graph argument the step plot is intuitive but implies a non-integer random variable. Instead stem plots or column plots are often used.


Figure 2: Discrete data plotting. Left stem plot. Right column plot.

# 1.2.4. Cumulative Distribution Function 

The cumulative density function (cdf), denoted by $F(t)$ is the probability of the random event occurring before $t, P(T \leq t)$. For a discrete cdf the height of each step is the pdf value $f\left(k_{i}\right)$.

$$
F(t)=P(T \leq t)=\int_{-\infty}^{t} f(x) d x, \quad F(k)=P(K \leq k)=\sum_{k_{i} \leq k} f\left(k_{i}\right)
$$

The limits of the cdf for $-\infty<t<\infty$ and $0 \leq k \leq \infty$ are given as:

$$
\begin{aligned}
& \lim _{t \rightarrow-\infty} F(t)=0, \quad F(-1)=0 \\
& \lim _{t \rightarrow \infty} F(t)=1, \quad \lim _{k \rightarrow \infty} F(k)=1
\end{aligned}
$$

The cdf can be used to find the probability of the random even occurring between two limits:

$$
\begin{gathered}
P(a \leq T \leq b)=\int_{a}^{b} f(t) d t=F(b)-F(a) \\
P(a \leq K \leq b)=\sum_{i=a}^{b} f(k)=F(b)-F(a-1)
\end{gathered}
$$

Figure 3: Left: continuous cdf/pdf, right: discrete cdf/pdf

# 1.2.5. Reliability Function 

The reliability function, also known as the survival function, is denoted as $R(t)$. It is the probability that the random event (time of failure) occurs after $t$.

$$
\begin{array}{cl}
R(t)=P(T>t)=1-F(t), & R(k)=P(T>k)=1-F(k) \\
R(t)=\int_{t}^{\infty} f(t) d t, & R(k)=\sum_{i=k+1}^{\infty} f\left(k_{i}\right)
\end{array}
$$

It should be noted that in most publications the discrete reliability function is defined as $R^{*}(k)=P(T \geq k)=\sum_{i=k}^{\infty} f(k)$. This definition results in $R^{*}(k) \neq 1-F(k)$. Despite this problem it is the most common definition and is included in all the references in this book except (Xie, Gaudoin, et al. 2002)

Figure 4: Left continuous cdf, right continuous survival function

# 1.2.6. Conditional Reliability Function 

The conditional reliability function, denoted as $m(x)$ is the probability of the component surviving given that it has survived to time $t$.

$$
m(x)=R(x \mid t)=\frac{R(t+\mathrm{x})}{R(t)}
$$

Where:
$t$ is the given time for which we know the component has survived.
$x$ is new random variable defined as the time after $t . x=0$ at $t$.

### 1.2.7. 1000\% Percentile Function

The $100 \alpha \%$ percentile function is the interval $\left[0, t_{\alpha}\right]$ for which the area under the pdf is $\alpha$.

$$
t_{\alpha}=F^{-1}(\alpha)
$$

### 1.2.8. Mean Residual Life

The mean residual life (MRL), denoted as $u(t)$, is the expected life given the component has survived to time, $t$.

$$
u(t)=\int_{0}^{\infty} R(x \mid t) d x=\frac{1}{R(t)} \int_{t}^{\infty} R(x) d x
$$

### 1.2.9. Hazard Rate

The hazard function, denoted as $h(t)$, is the conditional probability that a component fails in a small time interval, given that it has survived from time zero until the beginning of the time interval. For the continuous case the probability that an item will fail in a time interval given the item was functioning at time $t$ is:$$
P(t<T<t+\Delta t \mid T>t)=\frac{P(t<T<t+\Delta t)}{P(T>t)}=\frac{F(t+\Delta t)-F(t)}{R(t)}=\frac{\Delta F(t)}{R(t)}
$$

By dividing the probability by $\Delta t$ and finding the limit as $\Delta t \rightarrow 0$ gives the hazard rate:

$$
h(t)=\lim _{\Delta t \rightarrow 0} \frac{P(t<T<t+\Delta t \mid T>t)}{\Delta t}=\lim _{\Delta t \rightarrow 0} \frac{\Delta F(t)}{\Delta t R(t)}=\frac{f(t)}{R(t)}
$$

The discrete hazard rate is defined as: (Xie, Gaudoin, et al. 2002)

$$
h(k)=\frac{P(K=k)}{P(K \geq k)}=\frac{f(k)}{R(k-1)}
$$

This unintuitive result is due to a popular definition of $R^{*}(k)=\sum_{i=k}^{\infty} f(k)$ in which case $h(k)=f(k) / R^{*}(k)$. This definition has been avoided because it violates the formula $R(k)=1-F(k)$. The discrete hazard rate cannot be used in the same way as a continuous hazard rate with the following differences (Xie, Gaudoin, et al. 2002):

- $h(k)$ is defined as a probability and so is bounded by $[0,1]$.
- $h(k)$ is not additive for series systems.
- For the cumulative hazard rate $H(k)=-\ln [R(k)] \neq \sum_{i=0}^{k} h(k)$
- When a set of data is analyzed using a discrete counterpart of the continuous distribution the values of the hazard rate do not converge.

A function called the second failure rate has been proposed (Gupta et al. 1997):

$$
r(k)=\ln \frac{R(k-1)}{R(k)}=-\ln [1-h(k)]
$$

This function overcomes the previously mentioned limitations of the discrete hazard rate function and maintains the monotonicity property. For more information, the reader is referred to (Xie, Gaudoin, et al. 2002)

Care should be taken not to confuse the hazard rate with the Rate of Occurrence of Failures (ROCOF). ROCOF is the probability that a failure (not necessarily the first) occurs in a small time interval. Unlike the hazard rate, the ROCOF is the absolute rate at which system failures occur and is not conditional on survival to time $t$. ROCOF is using in measuring the change in the rate of failures for repairable systems.

# 1.2.10. Cumulative Hazard Rate 

The cumulative hazard rate, denoted as $H(t)$ an in the continuous case is the area under the hazard rate function. This function is useful to calculate average failure rates.

$$
\begin{gathered}
H(t)=\int_{\infty}^{t} h(u) d u=-\ln [R(t)] \\
H(k)=-\ln [R(k)]
\end{gathered}
$$

For a discussion on the discrete cumulative hazard rate see hazard rate.# 1.2.11. Characteristic Function 

The characteristic function of a random variable completely defines its probability distribution. It can be used to derive properties of the distribution from transformations of the random variable. (Billingsley 1995)

The characteristic function is defined as the expected value of the function $\exp (i \omega x)$ where $x$ is the random variable of the distribution with a $\operatorname{cdf} F(x), \omega$ is a parameter that can have any real value and $i=\sqrt{-1}$ :

$$
\begin{aligned}
\varphi_{X}(\omega) & =E\left[e^{i \omega x}\right] \\
& =\int_{-\infty}^{\infty} e^{i \omega x} F(x) d x
\end{aligned}
$$

A useful property of the characteristic function is the sum of independent random variables is the product of the random variables characteristic function. It is often easier to use the natural log of the characteristic function when conducting this operation.

$$
\begin{gathered}
\varphi_{X+Y}(\omega)=\varphi_{X}(\omega) \varphi_{Y}(\omega) \\
\ln \left[\varphi_{X+Y}(\omega)\right]=\ln \left[\varphi_{X}(\omega)\right] \ln \left[\varphi_{Y}(\omega)\right]
\end{gathered}
$$

For example, the addition of two exponentially distributed random variables with the same $\lambda$ gives the gamma distribution with $k=2$ :

$$
\begin{aligned}
& X \sim \operatorname{Exp}(\lambda), \quad Y \sim \operatorname{Exp}(\lambda) \\
& \varphi_{X}(\omega)=\frac{i \lambda}{\omega+i \lambda}, \quad \varphi_{Y}(\omega)=\frac{i \lambda}{\omega+i \lambda} \\
& \varphi_{X+Y}(\omega)=\varphi_{X}(\omega) \varphi_{Y}(\omega) \\
& =\frac{-\lambda^{2}}{(\omega+i \lambda)^{2}} \\
& X+Y \sim \operatorname{Gamma}(k=1, \lambda)
\end{aligned}
$$

This is the characteristic function of the gamma distribution with $k=2$.
The moment generating function can be calculated from the characteristic function:

$$
\varphi_{X}(-i \omega)=M_{X}(\omega)
$$

The $n^{\text {th }}$ raw moment can be calculated by differentiating the characteristic function $n$ times. For more information on moments see section 1.3.2.

$$
\begin{aligned}
E\left[X^{n}\right] & =i^{-n} \varphi_{X}^{(n)}(0) \\
& =i^{-n}\left[\frac{d^{n}}{d \omega^{n}} \varphi_{X}(\omega)\right]
\end{aligned}
$$# 1.2.12. Joint Distributions 

Joint distributions are multivariate distributions with, $d$ random variables $(d>1)$. An example of a bivariate distribution $(d=2)$ may be the distribution of failure for a vehicle tire which with random variables time, $T$, and distance travelled, $X$. The dependence between these two variables can be quantified in terms of correlation and covariance. See section 1.3.3 for more discussion. For more on properties of multivariate distributions see (Rencher 1997). The continuous and discrete random variables will be denoted as:

$$
\boldsymbol{x}=\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{d}
\end{array}\right], \quad \boldsymbol{k}=\left[\begin{array}{c}
k_{1} \\
k_{2} \\
\vdots \\
k_{d}
\end{array}\right]
$$

Joint distributions can be derived from the conditional distributions. For the bivariate case with random variables $x$ and $y$ :

$$
f(x, y)=f(y \mid x) f(x)=f(x \mid y) f(y)
$$

For the more general case:

$$
\begin{aligned}
f(\boldsymbol{x}) & =f\left(x_{1} \mid x_{2}, \ldots, x_{d}\right) f\left(x_{2}, \ldots, x_{d}\right) \\
& =f\left(x_{1}\right) f\left(x_{2} \mid x_{1}\right) \ldots f\left(x_{n-1} \mid x_{1}, \ldots, x_{n-2}\right) f\left(x_{n} \mid x_{1}, \ldots, x_{n}\right)
\end{aligned}
$$

If the random variables are independent, their joint distribution is simply the product of the marginal distributions:

$$
\begin{aligned}
& f(\boldsymbol{x})=\prod_{i=1}^{d} f\left(x_{i}\right) \text { where } x_{i} \perp x_{j} \text { for } i \neq j \\
& f(\boldsymbol{k})=\prod_{i=1}^{d} f\left(k_{i}\right) \text { where } k_{i} \perp k_{j} \text { for } i \neq j
\end{aligned}
$$

A general multivariate cumulative probability function with $n$ random variables $\left(T_{1}, T_{2}, \ldots, T_{n}\right)$ is defined as:

$$
F\left(t_{1}, t_{2}, \ldots, t_{n}\right)=P\left(T_{1} \leq t_{1}, T_{2} \leq t_{2}, \ldots, T_{n} \leq t_{n}\right)
$$

The survivor function is given as:

$$
R\left(t_{1}, t_{2}, \ldots, t_{n}\right)=P\left(T_{1}>t_{1}, T_{2}>t_{2}, \ldots, T_{n}>t_{n}\right)
$$

Different from univariate distributions is the relationship between the CDF and the survivor function (Georges et al. 2001):

$$
F\left(t_{1}, t_{2}, \ldots, t_{n}\right)+R\left(t_{1}, t_{2}, \ldots, t_{n}\right) \leq 1
$$If $F\left(t_{1}, t_{2}, \ldots, t_{n}\right)$ is differentiable then the probability density function is given as:

$$
f\left(t_{1}, t_{2}, \ldots, t_{n}\right)=\frac{\partial^{n} F\left(t_{1}, t_{2}, \ldots, t_{n}\right)}{\partial t_{1} \partial t_{2} \ldots \partial t_{n}}
$$

For a discussion on the multivariate hazard rate functions and the construction of joint distributions from marginal distributions see (Singpurwalla 2006).

# 1.2.13. Marginal Distribution 

The marginal distribution of a single random variable in a joint distribution can be obtained:

$$
\begin{gathered}
f\left(x_{1}\right)=\int_{x_{d}} \ldots \int_{x_{3}} \int_{x_{2}} f(\boldsymbol{x}) d x_{2} d x_{3} \ldots d x_{d} \\
f\left(k_{1}\right)=\sum_{k_{2}} \sum_{k_{3}} \ldots \sum_{k_{n}} f(\boldsymbol{k})
\end{gathered}
$$

### 1.2.14. Conditional Distribution

If the value is known for some random variables the conditional distribution of the remaining random variables is:

$$
\begin{gathered}
f\left(x_{1} \mid x_{2}, \ldots, x_{d}\right)=\frac{f(\boldsymbol{x})}{f\left(x_{2}, \ldots, x_{d}\right)}=\frac{f(\boldsymbol{x})}{\int_{x_{1}} f(\boldsymbol{x}) d x_{1}} \\
f\left(k_{1} \mid k_{2}, \ldots, k_{d}\right)=\frac{f(\boldsymbol{k})}{f\left(k_{2}, \ldots, k_{d}\right)}=\frac{f(\boldsymbol{k})}{\sum_{k_{1}} f(\boldsymbol{x})}
\end{gathered}
$$

### 1.2.15. Bathtub Distributions

Elementary texts on reliability introduce the hazard rate of a system as a bathtub curve. The bathtub curve has three regions, infant mortality (decreasing failure rate), useful life (constant failure rate) and wear out (increasing failure rate). Bathtub distributions have not been a popular choice for modeling life distributions when compared to exponential, Weibull and lognormal distributions. This is because bathtub distributions are generally more complex without closed form moments and more difficult to estimate parameters.

Sometimes more complex shapes are required than simple bathtub curves, as such generalizations and modifications to the bathtub curves has been studied. These include an increase in the failure rate followed by a bathtub curve and rollercoaster curves (decreasing followed by unimodal hazard rate). For further reading including applications see (Lai \& Xie 2006).# 1.2.16. Truncated Distributions 

Truncation arises when the existence of a potential observation would be unknown if it were to occur in a certain range. An example of truncation is when the existence of a defect is unknown due to the defect's amplitude being less than the inspection threshold. The number of flaws below the inspection threshold is unknown. This is not to be confused with censoring which occurs when there is a bound for observing events. An example of right censoring is when a test is time terminated and the failures of the surviving components are not observed, however we know how many components were censored. (Meeker \& Escobar 1998, p.266)

A truncated distribution is the conditional distribution that results from restricting the domain of another probability distribution. The following general formulas apply to truncated distribution functions, where $f_{0}(x)$ and $F_{0}(x)$ are the pdf and cdf of the nontruncated distribution. For further reading specific to common distributions see (Cohen 1991)

Probability Distribution Function:

$$
f(x)=\left\{\begin{array}{cc}
f_{0}(x) & \text { for } x \in(a, b] \\
F_{0}(b)-F_{0}(a) & \text { otherwise }
\end{array}\right.
$$

Cumulative Distribution Function:

$$
F(x)=\left\{\begin{array}{cc}
0 & \text { for } x \leq a \\
\frac{\int_{a}^{x} f_{0}(t) d t}{F_{0}(b)-F_{0}(a)} & \text { for } x \in(a, b] \\
1 & \text { for } x>b
\end{array}\right.
$$# 1.2.17. Summary 

Table 2: Summary of distribution functions

|  | $f(t)$ | $F(t)$ | $R(t)$ | $h(t)$ | $H(t)$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $f(t)=$ | --- | $F^{\prime}(t)$ | $-R^{\prime}(t)$ | $h(t) \exp \left\{-\int_{0}^{t} h(x) d x\right\}$ | $-\frac{d\{\exp [-H(t)]\}}{d t}$ |
| $F(t)=$ | $\int_{0}^{t} f(x) d x$ | --- | $1-R(t)$ | $1-\exp \left\{-\int_{0}^{t} h(x) d x\right\}$ | $1-\exp \{-H(t)\}$ |
| $R(t)=$ | $1-\int_{0}^{t} f(x) d x$ | $1-F(t)$ | --- | $\exp \left\{-\int_{0}^{t} h(x) d x\right\}$ | $\exp \{-H(t)\}$ |
| $h(t)=$ | $\frac{f(t)}{1-\int_{0}^{t} f(x) d x}$ | $\frac{F^{\prime}(t)}{1-F(t)}$ | $\frac{R^{\prime}(t)}{R(t)}$ | --- | $H^{\prime}(t)$ |
| $H(t)=$ | $-\ln \int_{t}^{\infty} f(x) d x$ | $\ln \left\{\frac{1}{1-F(x)}\right\}$ | $-\ln \{R(x)\}$ | $\int_{0}^{t} h(x) d x$ | --- |
| $u(t)=$ | $\frac{\int_{0}^{\infty} x f(t+x) d x}{\int_{t}^{\infty} f(x) d x}$ | $\frac{\int_{t}^{\infty}[1-F(x)] d x}{1-F(t)}$ | $\frac{\int_{t}^{\infty} R(x) d x}{R(t)}$ | $\frac{\int_{t}^{\infty} \exp \left\{-\int_{0}^{t} h(x) d x\right\} d x}{\exp \left\{-\int_{0}^{t} h(x) d x\right\}}$ | $\frac{\int_{t}^{\infty} \exp \{-H(x)\} d x}{\exp \{-H(x)\}}$ |# 1.3. Distribution Properties 

### 1.3.1. Median / Mode

The median of a distribution, denoted as $t_{0.5}$ is when the cdf and reliability function are equal to 0.5 .

$$
t_{0.5}=F^{-1}(0.5)=R^{-1}(0.5)
$$

The mode is the highest point of the pdf, $t_{50}$. This is the point where a failure has the highest probability. Samples from this distribution would occur most often around the mode.

### 1.3.2. Moments of Distribution

The moments of a distribution are given by:

$$
\mu_{n}=\int_{-\infty}^{\infty}(x-c)^{n} f(x) d x, \quad \mu_{n}=\sum_{i}\left(k_{j}-c\right)^{n} f(k)
$$

When $c=0$ the moments, $\mu_{n}^{\prime}$, are called the raw moments, described as moments about the origin. In respect to probability distributions the first two raw moments are important. $\mu_{0}^{\prime}$ always equals one, and $\mu_{1}^{\prime}$ is the distributions mean which is the expected value of the random variable for the distribution:

$$
\mu_{0}^{\prime}=\int_{-\infty}^{\infty} f(x) d x=1, \quad \mu_{0}^{\prime}=\sum_{i} f\left(k_{i}\right)=1
$$

mean $=E[X]=\mu$ :

$$
\mu_{1}^{\prime}=\int_{-\infty}^{\infty} x f(x) d x, \quad \mu_{1}^{\prime}=\sum_{i} k_{i} f\left(k_{i}\right)
$$

Some important properties of the expected value $E[X]$ when transformations of the random variable occur are:

$$
\begin{aligned}
E[X+b] & =\mu_{X}+b \\
E[X+Y] & =\mu_{X}+\mu_{Y} \\
E[a X] & =a \mu_{X} \\
E[X Y] & =\mu_{X} \mu_{Y}+\operatorname{Cov}(X, Y)
\end{aligned}
$$

When $c=\mu$ the moments, $\mu_{n}$, are called the central moments, described as moments about the mean. In this book, the first five central moments are important. $\mu_{0}$ is equal to $\mu_{0}^{\prime}=1 . \mu_{1}$ is the variance which quantifies the amount the random variable deviates from the mean. $\mu_{2}$ and $\mu_{3}$ are used to calculate the skewness and kurtosis.

$$
\begin{aligned}
\mu_{0}=\int_{-\infty}^{\infty} f(x) d x=1, & \mu_{0}=\sum_{i} f\left(k_{i}\right)=1 \\
\mu_{1}=\int_{-\infty}^{\infty}(x-\mu) f(x) d x=0, & \mu_{1}=\sum_{i}\left(k_{i}-\mu\right) f\left(k_{i}\right)=0
\end{aligned}
$$variance $=E\left[(X-E[X])^{2}\right]=E\left[X^{2}\right]-\{E[X]\}^{2}=\sigma^{2}$ :

$$
\mu_{2}=\int_{-\infty}^{\infty}(x-\mu)^{2} f(x) d x, \quad \mu_{2}=\sum_{i}\left(k_{i}-\mu\right)^{2} f\left(k_{i}\right)
$$

Some important properties of the variance exist when transformations of the random variable occur are:

$$
\begin{aligned}
\operatorname{Var}[X+b] & =\operatorname{Var}[X] \\
\operatorname{Var}[X+Y] & =\sigma_{X}^{2}+\sigma_{Y}^{2} \pm 2 \operatorname{Cov}(X, Y) \\
\operatorname{Var}[a X] & =a^{2} \sigma_{X}^{2} \\
\operatorname{Var}[X Y] & =(X Y)^{2}\left[\left(\frac{\sigma_{X}}{X}\right)^{2}+\left(\frac{\sigma_{Y}}{Y}\right)^{2}+2 \frac{\operatorname{Cov}(X, Y)}{X Y}\right]
\end{aligned}
$$

The skewness is a measure of the asymmetry of the distribution.

$$
\gamma_{1}=\frac{\mu_{3}}{\mu_{2}^{3 / 2}}
$$

The kurtosis is a measure of the whether the data is peaked or flat.

$$
\gamma_{2}=\frac{\mu_{4}}{\mu_{2}^{2}}
$$

# 1.3.3. Covariance 

Covariance is a measure of the dependence between random variables.

$$
\operatorname{Cov}(X, Y)=E\left[\left(X-\mu_{X}\right)\left(Y-\mu_{Y}\right)\right]=E[X Y]-\mu_{X} \mu_{Y}
$$

A normalized measure of covariance is correlation, $\rho$. The correlation has the limits $-1 \leq \rho \leq 1$. When $\rho=1$ the random variables have a linear dependency (i.e, an increase in $X$ will result in the same increase in $Y$ ). When $\rho=-1$ the random variables have a negative linear dependency (i.e, an increase in $X$ will result in the same decrease in Y). The relationship between covariance and correlation is:

$$
\rho_{X, Y}=\operatorname{Corr}(X, Y)=\frac{\operatorname{Cov}(X, Y)}{\sigma_{X} \sigma_{Y}}
$$

If the two random variables are independent than the correlation is equal to zero, however the reverse is not always true. If the correlation is zero the random variables does not need to be independent. For derivations and more information the reader is referred to (Dekking et al. 2007, p.138).# 1.4. Parameter Estimation 

### 1.4.1. Probability Plotting Paper

Most plotting methods transform the data available into a straight line for a specific distribution. From a line of best fit the parameters of the distribution can be estimated. Most plotting paper plots the random variable (time or demands) against the pdf, cdf or hazard rate and transform the data points to a linear relationship by adjusting the scale of each axis. Probability plotting is done using the following steps (Nelson 1982, p.108):

1. Order the data such that $x_{1} \leq x_{2} \leq \cdots \leq x_{i} \leq \cdots \leq x_{n}$.
2. Assign a rank to each failure. For complete data this is simply the value $i$. Censored data is discussed after step 7 .
3. Calculate the plotting position. The cdf may simply be calculated as $i / n$ however this produces a biased result, instead the following non-parametric Blom estimates, are recommended as suitable for many cases by (Kimball 1960):

$$
\begin{aligned}
& \hat{h}\left(t_{i}\right)=\frac{1}{(n-i+0.625)\left(t_{i+1}-t_{i}\right)} \\
& \hat{F}\left(t_{i}\right)=\frac{i-0.375}{n+0.25} \\
& \hat{R}\left(t_{i}\right)=\frac{n-i+0.625}{(n+0.25)} \\
& \hat{f}\left(t_{i}\right)=\frac{1}{(n+0.25)\left(t_{i+1}-t_{i}\right)}
\end{aligned}
$$

Other proposed estimators are:

$$
\begin{aligned}
\text { Naive: } \hat{F}\left(t_{i}\right) & =\frac{i}{n} \\
\text { Median (approximate): } \hat{F}\left(t_{i}\right) & =\frac{i-0.3}{n+0.4} \\
\text { Midpoint: } \hat{F}\left(t_{i}\right) & =\frac{i-0.5}{n} \\
\text { Mean : } \hat{F}\left(t_{i}\right) & =\frac{i}{n+1} \\
\text { Mode: } \hat{F}\left(t_{i}\right) & =\frac{i-1}{n-1}
\end{aligned}
$$

4. Plot points on probability paper. The choice of distribution should be from experience, or multiple distributions should be used to assess the best fit. Probability paper is available from http://www.welbull.com/GPaper/.5. Assess the data and chosen distributions. If the data plots in straight line then the distribution may be a reasonable fit.
6. Draw a line of best fit. This is a subjective assessment which minimizes the deviation of the points from the chosen line.
7. Obtained the desired information. This may be the distribution parameters or estimates of reliability or hazard rate trends.

When multiple failure modes are observed only one failure mode should be plotted with the other failures being treated as censored. Two popular methods to treat censored data two methods are :

Rank Adjustment Method. (Manzini et al. 2009, p.140) Here the adjusted rank, $j_{t_{i}}$ is calculated only for non-censored units (with $i_{t_{i}}$ still being the rank for all ordered times). This adjusted rank is used for step 2 with the remaining steps unchanged:

$$
j_{t_{i}}=j_{t_{i-1}}+\frac{(n+1)-j_{t_{i-1}}}{2+n-i_{t_{i}}}
$$

Kaplan Meier Estimator. Here the estimate for reliability is:

$$
\hat{R}\left(t_{i}\right)=\prod_{t_{j} \in t_{i}}\left(1-\frac{d}{n-i+1}\right)
$$

Where $d$ is the number of failures in rank j (for non-grouped data $d=1$ ). From this estimate a cdf can be given as $\hat{F}\left(t_{i}\right)=1-\hat{R}\left(t_{i}\right)$. For a detailed derivation and properties of this estimator see (Andersen et al. 1996, p.255)

Probability plots are fast and not dependent on complex numerical methods and can be used without a detailed knowledge of statistics. It provides a visual representation of the data for which qualitative statements can be made. It can be useful in estimating initial values for numerical methods. Limitation of this technique is that it is not objective and two different people making the same plot will obtain different answers. It also does not provide confidence intervals. For more detail of probability plotting the reader is referred to (Nelson 1982, p.104) and (Meeker \& Escobar 1998, p.122)

# 1.4.2. Total Time on Test Plots 

Total time on Test (TTT) plots is a graph which provides a visual representation of the hazard rate trend, i.e increasing, constant or decreasing. This assists in identifying the distribution from which the data may come from. To plot TTT (Rinne 2008, p.334):

1. Order the data such that $x_{1} \leq x_{2} \leq \cdots \leq x_{i} \leq \cdots \leq x_{n}$.
2. Calculate the TTT positions:

$$
T T T_{i}=\sum_{j=1}^{i}(n-j+1)\left(x_{j}-x_{j-1}\right) ; i=1,2, \ldots, n
$$

3. Calculate the normalized TTT positions:$$
T T T_{i}^{*}=\frac{T T T_{i}}{T T T_{n}} ; i=1,2, \ldots, n
$$

4. Plot the points $\left(\frac{i}{n}, T T T_{i}^{*}\right)$.
5. Analyze graph:


Figure 5: Time on test plot interpretation
Compared to probability plotting, TTT plots are simple, scale invariant and can represent any data set even those from different distributions on the same plot. However it only provides an indication of failure rate properties and cannot be used directly to estimate parameters. For more information about TTT plots the reader is referred to (Rinne 2008, p.334).

# 1.4.3. Least Mean Square Regression 

When the relationship between two variables, $x$ and $y$ is assumed linear $(y=m x+c)$, an estimate of the line's parameters can be obtained from $n$ sample data points, $\left(x_{i}, y_{i}\right)$ using least mean square (LMS) regression. The least square method minimizes the square of the residual.

$$
S=\sum_{i=1}^{n} r_{i}^{2}
$$The residual can be defined in many ways.

$$
\begin{aligned}
& \text { Minimize y residuals } \\
& r_{i}=y_{i}-f\left(x_{i} ; m, c\right) \\
& \tilde{m}=\frac{n \sum x_{i} y_{i}-\left(\sum x_{i}\right)\left(\sum y_{i}\right)}{n \sum x_{i}^{2}-\left(\sum x_{i}^{2}\right)^{2}} \\
& \hat{c}=\frac{\sum y_{i}}{n}-\tilde{m} \frac{\sum x_{i}}{n}
\end{aligned}
$$



Figure 6: Left minimize $y$ residual, right minimize $x$ residual
The LMS method can be used to estimate the line of best fit when using plotting parameter estimation methods. When plotting on a regular scale in software such as Microsoft Excel, it is often easy to conduct linear least mean square (LMS) regression using in built functions. Where available this book provides the formulas to plot the sample data in a straight line in a regular scale plot. It also provides the transformation from the linear LMS regression estimates of $\tilde{m}$ and $\hat{c}$ to the distribution parameter estimates.

For more on least square methods in a reliability engineering context see (Nelson 1990, p.167). MS regression can also be conducted on multivariate distributions, see (Rao \& Toutenburg 1999) and can also be conducted on non-linear data directly, see (Björck 1996).

# 1.4.4. Method of Moments 

To estimate the distribution parameters using the method of moments the sample moments are equated to the parameter moments and solved for the unknown parameters. The following sample moments can be used:

The sample mean is given as:

$$
\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$The unbiased sample variance is given as:

$$
S^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}
$$

Method of moments is not as accurate as Bayesian or maximum likelihood estimates but is easy and fast to calculate. The method of moment estimates are often used as a starting point for numerical methods to optimize maximum likelihood and least square estimators.

# 1.4.5. Maximum Likelihood Estimates 

Maximum likelihood estimates (MLE) are a frequentist approach to parameter estimation usually obtained by maximizing the natural log of the likelihood function.

$$
\Lambda(\theta \mid \mathrm{E})=\ln [L(\theta \mid E)]
$$

Algebraically this is done by solving the first order partial derivatives of the log-likelihood function. This calculation has been included in this book for distributions where the result is in closed form. Otherwise the log-likelihood function can be maximized directly using numerical methods.

MLE for $\hat{\theta}$ is obtained by solving for $\theta$ :

$$
\frac{\partial \Lambda}{\partial \theta}=0
$$

Denote the true parameters of the distribution as $\boldsymbol{\theta}_{0}$, MLEs have the following properties (Rinne 2008, p.406):

- Consistency. As the number of samples increases the difference between the estimated and actual parameter decreases:

$$
\operatorname{plim}_{n \rightarrow \infty} \hat{\boldsymbol{\theta}}=\boldsymbol{\theta}
$$

- Asymptotic normality.

$$
\lim _{n \rightarrow \infty} \hat{\theta} \sim \operatorname{Norm}\left(\theta_{0},\left[I_{n}\left(\theta_{0}\right)\right]^{-1}\right)
$$

where $I_{n}(\theta)=n I(\theta)$ is the Fisher information matrix. Therefore $\hat{\theta}$ is asymptotically unbiased:

$$
\lim _{n \rightarrow \infty} E[\hat{\theta}]=\theta_{0}
$$

- Asymptotic efficiency.

$$
\lim _{n \rightarrow \infty} \operatorname{Var}[\hat{\theta}]=\left[I_{n}\left(\theta_{0}\right)\right]^{-1}
$$

- Invariance. The MLE of $f\left(\theta_{0}\right)$ is $f(\hat{\theta})$ if $f($.$) is a continuous and continuously$ differentiable function.

The advantages of MLE are that it is a very common technique that has been widely published and is implemented in many software packages. The MLE method can easily handle censored data. The disadvantage to MLE is the bias introduced for small samplesizes and unbounded estimates may result when no failures have been observed. The numerical optimization of the log-likelihood function may be non-trivial with high sensitivity to starting values and the presence of local maximums.

For more information in a reliability context see (Nelson 1990, p.284).

# 1.4.6. Bayesian Estimation 

Bayesian estimation uses a subjective interpretation of the theory of probability and for parameter point estimation and confidence intervals uses Bayes' rule to update our state of knowledge of the unknown of interest (UIO). Recall from section 1.1.5 Bayes rule,

$$
\pi(\theta \mid E)=\frac{\pi_{o}(\theta) L(E \mid \theta)}{\int \pi_{o}(\theta) L(E \mid \theta) d \theta}, \quad P(\theta \mid E)=\frac{P(\theta) P(E \mid \theta)}{\sum_{i=1}^{n_{P}} P\left(E \mid \theta_{i}\right) P(\theta)}
$$

respectively for continuous and discrete forms of variable of $\theta$.

## The Prior Distribution $\pi_{o}(\theta)$

The prior distribution is probability distribution of the UOI, $\theta$, which captures our state of knowledge of $\theta$ prior to the evidence being observed. It is common for this distribution to represent soft evidence or intervals about the possible values of $\theta$. If the distribution is dispersed it represents little being known about the parameter. If the distribution is concentrated in an area then it reflects a good knowledge about the likely values of $\theta$.

Prior distributions should be a proper probability distribution of $\theta$. A distribution is proper when it integrates to one and improper otherwise. The prior should also not be selected based on the form of the likelihood function. When the prior has a constant which does not affect the posterior distribution (such as improper priors) it will be omitted from the formulas within this book.

Non-informative Priors. Occasions arise when it is not possible to express a subjective prior distribution due to lack of information, time or cost. Alternatively a subjective prior distribution may introduce unwanted bias through model convenience (conjugates) or due to elicitation methods. In such cases a non-informative prior may be desirable. The following methods exist for creating a non-informative prior (Yang and Berger 1998):

- Principle of Indifference - Improper Uniform Priors. An equal probability is assigned across all the possible values of the parameter. This is done using an improper uniform distribution with a constant, usually 1 , over the range of the possible values for $\theta$. When placed in Bayes formula the constant cancels out, however the denominator is integrated over all possible values of $\theta$. In most cases this prior distribution will result in a proper posterior, but not always. Improper Uniform Priors may be chosen to enable the use of conjugate priors.

For example using exponential likelihood model, with an improper uniform prior, 1 , over the limits $[0, \infty)$ with evidence of $n_{F}$ failures in total time, $t_{T}$ :

$$
\text { Prior: } \quad \pi_{0}(\lambda)=1 \propto \operatorname{Gamma}(1,0)
$$$$
\begin{gathered}
\text { Likelihood: } \quad L(E \mid \lambda)=\lambda^{\mathrm{n}_{\mathrm{F}}} e^{-\lambda t_{\mathrm{T}}} \\
\text { Posterior: } \pi(\lambda \mid E)=\frac{1 . L(E \mid \lambda)}{1 . \int_{0}^{\infty} L(E \mid \lambda) d \lambda}
\end{gathered}
$$

Using conjugate relationship (see Conjugate Priors for calculations):

$$
\lambda \sim \operatorname{Gamma}\left(\lambda ; 1+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right)
$$

- Principle of Indifference - Proper Uniform Priors. An equal probability is assigned across the values of the parameter within a range defined by the uniform distribution. The uniform distribution is obtained by estimating the far left and right bounds ( $a$ and $b$ ) of the parameter $\theta$ giving $\pi_{a}(\theta)=\frac{1}{b-a}=c$, where c is a constant. When placed in Bayes formula the constant cancels out, however the denominator is integrated over the bound $[a, b]$. Care needs to be taken in choosing $a$ and $b$ because no matter how much evidence suggests otherwise the posterior distribution will always be zero outside these bounds.

Using an exponential likelihood model, with a proper uniform prior, $c$, over the limits $[a, b]$ with evidence of $n_{F}$ failures in total time, $t_{T}$ :

$$
\begin{gathered}
\text { Prior: } \quad \pi_{0}(\lambda)=\frac{1}{b-a}=c \propto \text { Truncated } \operatorname{Gamma}(1,0) \\
\text { Likelihood: } \quad L(E \mid \lambda)=\lambda^{\mathrm{n}_{\mathrm{F}}} e^{-\lambda t_{\mathrm{T}}} \\
\text { Posterior: } \pi(\lambda \mid E)=\frac{c . L(E \mid \lambda)}{c . \int_{a}^{b} L(E \mid \lambda) d \lambda} \text { for } \mathrm{a} \leq \lambda \leq \mathrm{b}
\end{gathered}
$$

Using conjugate relationship this results in a truncated Gamma distribution:

$$
\pi(\lambda)=\left\{\begin{array}{cc}
c . \operatorname{Gamma}\left(\lambda ; 1+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right) & \text { for } \mathrm{a} \leq \lambda \leq \mathrm{b} \\
0 & \text { otherwise }
\end{array}\right.
$$

- Jeffrey's Prior. Proposed by Jeffery in 1961, this prior is defined as $\pi_{0}(\theta)=$ $\sqrt{\operatorname{det}\left(\boldsymbol{I}_{\theta}\right)}$ where $\boldsymbol{I}_{\theta}$ is the Fisher information matrix. This derivation is motivated by the fact that it is not dependent upon the set of parameter variables that is chosen to describe parameter space. Jeffery himself suggested the need to make ad hoc modifications to the prior to avoid problems in multidimensional distributions. Jeffories prior is normally improper. (Bernardo et al. 1992)
- Reference Prior. Proposed by Bernardo in 1979, this prior maximizes the expected posterior information from the data, therefore reducing the effect of the prior. When there is no nuisance parameters and certain regularity conditions are satisfied the reference prior is identical to the Jeffrey's prior. Due to the need to order or group the importance of parameters, it may occur that different posteriors will result from the same data depending on theimportance the user places on each parameter. This prior overcomes the problems which arise when using Jeffery's prior in multivariate applications.

- Maximal Data Information Prior (MDIP). Developed by Zelluer in 1971 maximizes the likelihood function with relation to the prior. (Berry et al. 1995, p.182)

For further detail on the differences between each type of non-informative prior see (Berry et al. 1995, p.179)

Conjugate Priors. Calculating posterior distributions can be extremely complex and in most cases requires expensive computations. A special case exists however by which the posterior distribution is of the same form as the prior distribution. The Bayesian updating mathematics can be reduced to simple calculations to update the model parameters. As an example the gamma function is a conjugate prior to a Poisson likelihood function:

$$
\begin{gathered}
\text { Prior: } \pi_{\alpha}(\lambda)=\frac{\beta^{\alpha} \lambda^{\alpha-1}}{\Gamma(\alpha)} e^{-\beta \lambda} \\
\text { Likelihood: } L_{i}\left(t_{i} \mid \lambda\right)=\frac{\lambda_{i}^{k} t_{i}^{k}}{k_{i}!} e^{-\lambda t_{i}} \\
\text { Likelihood: } L(E \mid \lambda)=\prod_{i=1}^{n_{F}} L_{i}\left(t_{i} \mid \lambda\right)=\frac{\lambda^{\Sigma k} \prod t_{i}^{k}}{\prod k_{i}!} e^{-\lambda \Sigma t_{i}} \\
\text { Posterior: } \pi(\lambda \mid E)=\frac{\pi_{\alpha}(\lambda) L(E \mid \lambda)}{\int_{0}^{\infty} \pi_{\alpha}(\lambda) L(E \mid \lambda) d \lambda} \\
=\frac{\frac{\beta^{\alpha} \lambda^{\alpha-1} \lambda^{\Sigma k} \prod t_{i}^{k}}{\Gamma(\alpha) \prod k_{i}!} e^{-\beta \lambda} e^{-\lambda \Sigma t_{i}}}{\int_{0}^{\infty} \frac{\beta^{\alpha} \lambda^{\alpha-1} \lambda^{\Sigma k} \prod t_{i}^{k}}{\Gamma(\alpha) \prod k_{i}!} e^{-\beta \lambda} e^{-\lambda \Sigma t_{i}} d \lambda} \\
=\frac{\lambda^{\alpha-1+\Sigma k} e^{-\lambda\left(\beta+\Sigma t_{i}\right)}}{\int_{0}^{\infty} \lambda^{\alpha-1+\Sigma k} e^{-\lambda\left(\beta+\Sigma t_{i}\right)} d \lambda}
\end{gathered}
$$

Using the identity $\Gamma(z)=\int_{z}^{\infty} x^{z-1} e^{-x} d x$ we can calculate the denominator using the change of variable $u=\lambda\left(\beta+\sum t_{i}\right)$. This results in $\lambda=\frac{u}{\beta+\Sigma t_{i}}$, and $d \lambda=\frac{d u}{\beta+\Sigma t_{i}}$ with the limits of $u$ the same as $\lambda$. Substituting back into the posterior equation gives:

$$
\pi(\lambda \mid E)=\frac{\lambda^{\alpha-1+\Sigma k} e^{-\lambda\left(\beta+\Sigma t_{i}\right)}}{\frac{1}{\beta+\sum t_{i}} \int_{0}^{\infty}\left(\frac{u}{\beta+\sum t_{i}}\right)^{\alpha-1+\Sigma k} e^{-u} d u}
$$Let $z=\alpha+\sum k$

$$
=\frac{\lambda^{\alpha-1+\sum k} e^{-\lambda\left(\beta+\sum t_{i}\right)}}{\frac{1}{\left(\beta+\sum t_{i}\right)^{\alpha+\sum k}} \int_{0}^{\infty} u^{\alpha-1+\sum k} e^{-u} d u}
$$

$$
\pi(\lambda \mid E)=\frac{\lambda^{\alpha-1+\sum k} e^{-\lambda\left(\beta+\sum t_{i}\right)}}{\frac{1}{\left(\beta+\sum t_{i}\right)^{\alpha+\sum k}} \int_{0}^{\infty} u^{x-1} e^{-u} d u}
$$

Using $\Gamma(z)=\int_{0}^{\infty} x^{x-1} e^{-x} d x$ :

$$
\pi(\lambda \mid E)=\frac{\lambda^{\alpha-1+\sum k}\left(\beta+\sum t_{i}\right)^{\alpha+\sum k}}{\Gamma(\alpha+\sum k)} e^{-\lambda\left(\beta+\sum t_{i}\right)}
$$

Let $\alpha^{\prime}=\alpha+\sum k, \beta^{\prime}=\beta+\sum t_{i}$ :

$$
\pi(\lambda \mid E)=\frac{\lambda^{\alpha^{\prime}-1} \beta^{\prime \alpha^{\prime}}}{\Gamma\left(\alpha^{\prime}\right)} e^{-\beta^{\prime} \lambda}
$$

As can be seen the posterior is a gamma distribution with the parameters $\alpha^{\prime}=\alpha+\sum k$, $\beta^{\prime}=\beta+\sum t_{i}$. Therefore the prior and posterior are of the same form, and Bayes' rule does not need to be re-calculated for each update. Instead the user can simply update the parameters with the new evidence.

# The Likelihood Function $L(E \mid \theta)$ 

The reader is referred to section 1.1.6 for a discussion on the construction of the likelihood function.

## The Posterior Distribution $\pi(\theta \mid E)$

The posterior distribution is a probability distribution of the UOI, $\theta$, which captures our state of knowledge of $\theta$ including all prior information and the evidence.

Point Estimate. From the posterior distribution we may want to give a point estimate of $\theta$. The Bayesian estimator when using a quadratic loss function is the posterior mean (Christensen \& Huffman 1985):

$$
\hat{\theta}=E[\pi(\theta \mid E)]=\int \theta \pi(\theta \mid E) d \theta=\mu_{\pi}
$$

For more information on utility, loss functions and estimators in a Bayesian context see (Berger 1993).

### 1.4.7. Confidence Intervals

Assuming a random variable is distributed by a given distribution, there exists the true distribution parameters, $\boldsymbol{\theta}_{\mathbf{0}}$, which is unknown. The parameter point estimates, $\hat{\boldsymbol{\theta}}$, may or may not be close to the true parameter values. Confidence intervals provide the range over which the true parameter values may exist with a certain level of confidence. Confidence intervals only quantify uncertainty due to sampling error arising from a limited number of samples. Uncertainty due to incorrect model selection or incorrect assumptions is not included. (Meeker \& Escobar 1998, p.49)Increasing the desired confidence $\gamma$ results in an increased confidence interval. Increasing the sample size generally decreases the confidence interval. There are many methods to calculate confidence intervals. Some popular methods are:

- Exact Confidence Intervals. It may be mathematically shown that the parameter of a distribution itself follows a distribution. In such cases exact confidence intervals can be derived. This is only the case in very few distributions.
- Fisher Information Matrix (Nelson 1990, p.292). For a large number of samples, the asymptotic normal property can be used to estimate confidence intervals:

$$
\lim _{n \rightarrow \infty} \tilde{\theta} \sim \operatorname{Norm}\left(\theta_{0},\left[n I\left(\theta_{0}\right)\right]^{-1}\right)
$$

Combining this with the asymptotic property $\tilde{\theta} \rightarrow \theta_{0}$ as $n \rightarrow \infty$ gives the following estimate for the distribution of $\tilde{\theta}$ :

$$
\lim _{n \rightarrow \infty} \tilde{\theta} \sim \operatorname{Norm}\left(\tilde{\theta},\left[J_{n}(\tilde{\theta})\right]^{-1}\right)
$$

$100 \gamma \%$ approximate confidence intervals are calculated using percentiles of the normal distribution. If the range of $\theta$ is unbounded $(-\infty, \infty)$ the approximate two sided confidence intervals are:

$$
\begin{aligned}
& \underline{\theta_{\gamma}}=\tilde{\theta}-\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}} \\
& \overline{\theta_{\gamma}}=\tilde{\theta}+\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}}
\end{aligned}
$$

If the range of $\theta$ is $(0, \infty)$ the approximate two sided confidence intervals are:

$$
\begin{aligned}
& \underline{\theta_{\gamma}}=\tilde{\theta} \cdot \exp \left[\frac{\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}}}{-\tilde{\theta}}\right] \\
& \overline{\theta_{\gamma}}=\tilde{\theta} \cdot \exp \left[\frac{\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}}}{\tilde{\theta}}\right]
\end{aligned}
$$

If the range of $\theta$ is $(0,1)$ the approximate two sided confidence intervals are:

$$
\begin{aligned}
& \underline{\theta_{\gamma}}=\tilde{\theta} \cdot\left\{\tilde{\theta}+(1-\tilde{\theta}) \exp \left[\frac{\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}}}{\tilde{\theta}(1-\tilde{\theta})}\right]\right\}^{-1} \\
& \overline{\theta_{\gamma}}=\tilde{\theta} \cdot\left\{\tilde{\theta}+(1-\tilde{\theta}) \exp \left[\frac{\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\left[J_{n}(\tilde{\theta})\right]^{-1}}}{-\tilde{\theta}(1-\tilde{\theta})}\right]\right\}^{-1}
\end{aligned}
$$

The advantage of this method is it can be calculated for all distributions and is easy to calculate. The disadvantage is that the assumption of a normal distribution is asymptotic and so sufficient data is required for the confidenceinterval estimate to be accurate. The number of samples needed for an accurate estimate changes from distribution to distribution. It also produces symmetrical confidence intervals which may be very inaccurate. For more information see (Nelson 1990, p.292).

- Likelihood Ratio Intervals (Nelson 1990, p.292). The test statistic for the likelihood ratio is:

$$
D=2[\Lambda(\bar{\theta})-\Lambda(\theta)]
$$

$D$ is approximately Chi-Square distributed with one degree of freedom.

$$
D=2[\Lambda(\bar{\theta})-\Lambda(\theta)] \leq \chi^{2}(\gamma ; 1)
$$

Where $\gamma$ is the $100 \gamma \%$ confidence interval for $\theta$. The two sided confidence limits $\theta_{\gamma}$ and $\bar{\theta}_{\gamma}$ are calculated by solving:

$$
\Lambda(\theta)=\Lambda(\bar{\theta})-\frac{\chi^{2}(\gamma ; 1)}{2}
$$

The limits are normally solved numerically. The likelihood ratio intervals are always within the limits of the parameter and gives asymmetrical confidence limits. It is much more accurate than the Fisher information matrix method particularly for one sided limits although it is more complicated to calculate. This method must be solved numerically and so will not be discussed further in this book.

- Bayesian Confidence Intervals. In Bayesian statistics the uncertainty of a parameter, $\theta$, is quantified as a distribution $\pi(\theta)$. Therefore the two sided $100 \gamma \%$ confidence intervals are found by solving:

$$
\frac{1-\gamma}{2}=\int_{-\infty}^{\theta_{\gamma}} \pi(\theta) d \theta, \quad \frac{1+\gamma}{2}=\int_{\bar{\theta}_{\gamma}}^{\infty} \pi(\theta) d \theta
$$

Other methods exist to calculate approximate confidence intervals. A summary of some techniques used in reliability engineering is included in (Lawless 2002).# 1.5. Related Distributions 



Figure 7: Relationships between common distributions (Leemis \& McQueston 2008).
Many relations are not included such as central limit convergence to the normal distribution and many transforms which would have made the figure unreadable. For further details refer to individual sections and (Leemis \& McQueston 2008).# 1.6. Supporting Functions 

### 1.6.1. Beta Function $B(x, y)$

$B(x, y)$ is the Beta function and is the Euler integral of the first kind.

$$
B(x, y)=\int_{0}^{1} u^{x-1}(1-u)^{y-1} d u
$$

Where $x>0$ and $y>0$.
Relationships:

$$
\begin{aligned}
& B(x, y)=B(y, x) \\
& B(x, y)=\frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)} \\
& B(x, y)=\sum_{n=0}^{\infty} \frac{n-y}{n} x+n
\end{aligned}
$$

More formulas, definitions and special values can be found in the Digital Library of Mathematical Functions on the National Institute of Standards and Technology (NIST) website, http://dlmf.nist.gov/5/12/.

### 1.6.2. Incomplete Beta Function $B_{t}(t ; x, y)$

$B_{t}(t ; x, y)$ is the incomplete Beta function:

$$
B_{t}(t ; x, y)=\int_{0}^{t} u^{x-1}(1-u)^{y-1} d u
$$

### 1.6.3. Regularized Incomplete Beta Function $I_{t}(t ; x, y)$

$I_{t}(t \mid x, y)$ is the regularized incomplete Beta function:

$$
\begin{aligned}
& I_{t}(t \mid x, y)=\frac{B_{t}(\mathrm{t} ; x, y)}{B(x, y)} \\
& =\sum_{j=a}^{a+b-1} \frac{(x+y-1)!}{j!(x+y-1-j)!} \cdot t^{j}(1-t)^{x+y-1-j}
\end{aligned}
$$

Properties:

$$
\begin{gathered}
I_{0}(0 ; x, y)=0 \\
I_{\mathrm{t}}(1 ; x, y)=1 \\
I_{t}(\mathrm{t} ; x, y)=1-I(1-\mathrm{t} ; y, x)
\end{gathered}
$$

### 1.6.4. Complete Gamma Function $\Gamma(k)$

$\Gamma(k)$ is a generalization of the factorial function $k$ ! to include non-integer values.For $k>0$

$$
\begin{aligned}
\Gamma(k) & =\int_{0}^{\infty} t^{k-1} e^{-t} d t \\
& =\left[-t^{k-1} e^{-t}\right]_{0}^{\infty}+(k-1) \int_{0}^{\infty} t^{k-2} e^{-t} d t \\
& =(k-1) \int_{0}^{\infty} t^{k-2} e^{-t} d t \\
& =(k-1) \Gamma(k-1)
\end{aligned}
$$

When $k$ is an integer:

$$
\Gamma(k)=(k-1)!
$$

Special values:

$$
\begin{gathered}
\Gamma(1)=1 \\
\Gamma(2)=1 \\
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
\end{gathered}
$$

Relation to the incomplete gamma functions:

$$
\Gamma(k)=\Gamma(k, t)+\gamma(k, t)
$$

More formulas, definitions and special values can be found in the Digital Library of Mathematical Functions on the National Institute of Standards and Technology (NIST) website, http://dlmf.nist.gov/5/.

# 1.6.5. Upper Incomplete Gamma Function $\Gamma(k, t)$ 

For $k>0$

$$
\Gamma(k, t)=\int_{\Gamma}^{\infty} x^{k-1} e^{-x} d x
$$

When $k$ is an integer:

$$
\Gamma(k, t)=(k-1)!e^{-t} \sum_{n=0}^{k-1} \frac{t^{n}}{n!}
$$

More formulas, definitions and special values can be found on the NIST website, http://dlmf.nist.gov/8/.

### 1.6.6. Lower Incomplete Gamma Function $\gamma(k, t)$

For $k>0$

$$
\gamma(k, t)=\int_{0}^{t} x^{k-1} e^{-x} d x
$$

When $k$ is an integer:

$$
\gamma(k, t)=(k-1)!\left[1-e^{-t} \sum_{n=0}^{k-1} \frac{t^{n}}{n!}\right]
$$More formulas, definitions and special values can be found on the NIST website, http://dlmf.nist.gov/8/.

# 1.6.7. Digamma Function $\psi(x)$ 

$\psi(x)$ is the digamma function defined as:

$$
\psi(x)=\frac{d}{d x} \ln [\Gamma(x)]=\frac{\Gamma^{\prime}(x)}{\Gamma(x)} \text { for } x>0
$$

### 1.6.8. Trigamma Function $\psi^{\prime}(x)$

$\psi^{\prime}(x)$ is the trigamma function defined as:

$$
\psi^{\prime}(x)=\frac{d^{2}}{d x^{2}} \ln \Gamma(x)=\sum_{i=0}^{\infty}(x+i)^{-2}
$$# 1.7. Referred Distributions 

### 1.7.1. Inverse Gamma Distribution $I G(\alpha, \beta)$

The pdf to the inverse gamma distribution is:

$$
f(x ; \alpha, \beta)=\frac{\beta^{\alpha}}{\Gamma(\alpha) x^{\alpha+1}} \cdot e^{\frac{-\beta}{x}} \cdot I_{x}(0, \infty)
$$

With mean:

$$
\mu=\frac{\beta}{\alpha-1} \text { for } \alpha>1
$$

### 1.7.2. Student T Distribution $T\left(\alpha, \mu, \sigma^{2}\right)$

The pdf to the standard student $t$ distribution with $\mu=0, \sigma^{2}=1$ is:

$$
f(x ; \alpha)=\frac{\Gamma[(\alpha+1) / 2]}{\sqrt{\alpha \pi} \Gamma(\alpha / 2)} \cdot\left(1+\frac{x^{2}}{\alpha}\right)^{-\frac{\alpha+1}{2}}
$$

The generalized student $t$ distribution is:

$$
f\left(x ; \alpha, \mu, \sigma^{2}\right)=\frac{\Gamma[(\alpha+1) / 2]}{\sigma \sqrt{\alpha \pi} \Gamma(\alpha / 2)} \cdot\left(1+\frac{(x-\mu)^{2}}{\alpha \sigma^{2}}\right)^{-\frac{\alpha+1}{2}}
$$

With mean

$$
\mu=\mu
$$

### 1.7.3. F Distribution $F\left(n_{1}, n_{2}\right)$

Also known as the Variance Ratio or Fisher-Snedecor distribution the pdf is:

$$
f(x ; \alpha)=\frac{1}{x B\left(\frac{n_{1}}{2}, \frac{n_{2}}{2}\right)} \cdot \sqrt{\frac{\left(n_{1} x\right)^{n_{1}} \cdot n_{2}^{n_{2}}}{\left(n_{1} x+n_{2}\right)^{\left(n_{1}+n_{2}\right)}}}
$$

With cdf:

$$
I_{t}\left(\frac{n_{1}}{2}, \frac{n_{2}}{2}\right), \quad \text { where } t=\frac{n_{1} x}{n_{1} x+n_{2}}
$$

### 1.7.4. Chi-Square Distribution $\chi^{2}(v)$

The pdf to the chi-square distribution is:

$$
f(x ; v)=\frac{x^{(v-2) / 2} \exp \left\{-\frac{x}{2}\right\}}{2^{v / 2} \Gamma\left(\frac{v}{2}\right)}
$$

With mean:

$$
\mu=v
$$# 1.7.5. Hypergeometric Distribution HyperGeom $(k ; n, m, N)$ 

The hypergeometric distribution models probability of $k$ successes in $n$ Bernoulli trials from population $N$ containing $m$ success without replacement. $p=m / N$. The pdf to the hypergeometric distribution is:

$$
f(k ; n, m, N)=\frac{\binom{m}{k}\binom{N-m}{n-k}}{\binom{N}{n}}
$$

With mean:

$$
\mu=\frac{n m}{N}
$$

### 1.7.6. Wishart Distribution Wishart $_{d}(x ; \Sigma, n)$

The Wishart distribution is the multivariate generalization of the gamma distribution. The pdf is given as:

With mean:

$$
f_{d}(\boldsymbol{x} ; \boldsymbol{\Sigma}, n)=\frac{|\mathbf{x}|^{\frac{1}{2}(n-\mathrm{d}-1)}}{2^{n d / 2}|\boldsymbol{\Sigma}|^{n / 2} \Gamma_{d}\left(\frac{n}{2}\right)} \exp \left\{-\frac{1}{2} \operatorname{tr}\left(\boldsymbol{x}^{-1} \boldsymbol{\Sigma}\right)\right\}
$$# 1.8. Nomenclature and Notation 

Functions are presented in the following form:
$f$ (random variables ; parameters $\mid$ given values)
$n \quad$ In continuous distributions the number of items under test $=n_{f}+n_{s}+n_{t}$. In discrete distributions the total number of trials.
$n_{F} \quad$ The number of items which failed before the conclusion of the test.
$n_{S} \quad$ The number of items which survived to the end of the test.
$n_{I} \quad$ The number of items which have interval data
$t_{i}^{F}, t_{i} \quad$ The time at which a component fails.
$t_{i}^{S} \quad$ The time at which a component survived to. The item may have been removed from the test for a reason other than failure.
$t_{i}^{U I} \quad$ The upper limit of a censored interval in which an item failed
$t_{i}^{U} \quad$ The lower limit of a censored interval in which an item failed
$t_{L} \quad$ The lower truncated limit of sample.
$t_{U} \quad$ The upper truncated limit of sample.
$t_{T} \quad$ Time on test $=\sum t_{i}+\sum t_{s}$
$X$ or $T \quad$ Continuous random variable ( $T$ is normally a random time)
$K \quad$ Discrete random variable
$x$ or $t \quad$ A continuous random variable with a known value
$k \quad$ A discrete random variable with a known value
$\hat{x} \quad$ The hat denotes an estimated value
$x \quad$ A bold symbol denotes a vector or matrix
$\theta \quad$ Generalized unknown of interest (UOI)
$\bar{\theta} \quad$ Upper confidence interval for UOI
$\underline{\theta} \quad$ Lower confidence interval for UOI
$X \sim \operatorname{Norm}_{d} \quad$ The random variable $X$ is distributed as a $d$-variate normal distribution.# 2. Common Life Distributions# 2.1. Exponential Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - F(t)


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\lambda$ | $\lambda>0$ | Scale Parameter: Equal to the hazard rate. |
| Limits | $t \geq 0$ |  |  |
| Function | Time Domain |  | Laplace Domain |
| PDF | $f(t)=\lambda \mathrm{e}^{-\lambda t}$ |  | $f(s)=\frac{\lambda}{\lambda+s}, \quad s>-\lambda$ |
| CDF | $F(t)=1-\mathrm{e}^{-\lambda t}$ |  | $F(s)=\frac{\lambda}{s(\lambda+s)}$ |
| Reliability | $\mathrm{R}(\mathrm{t})=\mathrm{e}^{-\lambda t}$ |  | $R(s)=\frac{1}{\lambda+s}$ |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=\mathrm{e}^{-\lambda \mathrm{x}}$ |  | $m(s)=\frac{1}{\lambda+s}$ |
|  | Where <br> $t$ is the given time we know the component has survived to. <br> $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life | $u(t)=\frac{1}{\lambda}$ |  | $u(s)=\frac{1}{\lambda s}$ |
| Hazard Rate | $h(t)=\lambda$ |  | $h(s)=\frac{\lambda}{s}$ |
| Cumulative Hazard Rate | $H(t)=\lambda t$ |  | $H(s)=\frac{\lambda}{s^{2}}$ |
| Properties and Moments |  |  |  |
| Median |  |  | $\frac{\ln (2)}{\lambda}$ |
| Mode |  |  | 0 |
| Mean - $1^{\text {st }}$ Raw Moment |  |  | $\frac{1}{\lambda}$ |
| Variance - $2^{\text {nd }}$ Central Moment |  |  | $\frac{1}{\lambda^{2}}$ |
| Skewness - $3^{\text {rd }}$ Central Moment |  |  | 2 |
| Excess kurtosis - $4^{\text {th }}$ Central Moment |  |  | 6 |
| Characteristic Function |  |  | $\frac{i \lambda}{t+i \lambda}$ |
| 100a\% Percentile Function |  |  | $t_{\alpha}=-\frac{1}{\lambda} \ln (1-\alpha)$ || Parameter Estimation |  |  |  |
| :--: | :--: | :--: | :--: |
| Plotting Method |  |  |  |
| Least Mean <br> Square <br> $y=m x+c$ | X-Axis | Y-Axis | $\hat{\lambda}=-m$ |
|  | $t_{i}$ | $\ln \left[1-F\left(t_{i}\right)\right]$ |  |
| Likelihood Function |  |  |  |
| Likelihood <br> Functions | $L(E \mid \lambda)=\underbrace{\lambda^{\mathrm{n}_{\mathrm{F}}} \prod_{1=1}^{\mathrm{n}_{\mathrm{F}}} \mathrm{e}^{-\lambda t_{i}^{\mathrm{F}}}}_{\text {failures }} \underbrace{\prod_{i=1}^{\mathrm{n}_{\mathrm{x}}} \mathrm{e}^{-t_{i}^{\mathrm{X}}}}_{$ survivors } \underbrace{\prod_{i=1}^{\mathrm{n}_{\mathrm{i}}}\left(\mathrm{e}^{-\lambda t_{i}^{\mathrm{LI}}}-\mathrm{e}^{-\lambda t_{i}^{\mathrm{NI}}}\right)}_{\text {interval failures }}$ |  |  |
|  | when there is no interval data this reduces to: $L(E \mid \lambda)=\lambda^{\mathrm{n}_{\mathrm{F}}} \mathrm{e}^{-\lambda t_{T}} \quad$ where $\quad t_{T}=\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{F}}+\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{S}}=$ total time in test |  |  |
| Log-Likelihood <br> Functions | $\Lambda(E \mid \lambda)=\underbrace{\text { r. } \ln (\lambda)-\sum_{i=1}^{\mathrm{n}_{\mathrm{F}}} \lambda t_{i}^{\mathrm{F}}}_{\text {failures }}-\sum_{i=1}^{\mathrm{n}_{\mathrm{x}}} \lambda t_{\mathrm{x}}+\sum_{i=1}^{\mathrm{n}_{\mathrm{i}}} \ln \left(\mathrm{e}^{-\lambda t_{i}^{\mathrm{LI}}}-\mathrm{e}^{-\lambda t_{i}^{\mathrm{NI}}}\right)}_{\text {interval failures }}$ |  |  |
|  | when there is no interval data this reduces to: $\Lambda(E \mid \lambda)=\mathrm{n}_{\mathrm{F}} \cdot \ln (\lambda)-\lambda t_{T} \quad$ where $\quad t_{T}=\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{F}}+\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{S}}$ |  |  |
| $\frac{\partial \Lambda}{\partial \lambda}=0$ | solve for $\lambda$ to get $\hat{\lambda}$ : $\underbrace{\frac{\mathrm{n}_{\mathrm{F}}}{\lambda}-\sum_{i=1}^{\mathrm{n}_{\mathrm{F}}} \mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}_{\text {failures }}-\sum_{i=1}^{\mathrm{n}_{\mathrm{x}}} \mathrm{t}_{\mathrm{i}}^{\mathrm{S}}}_{$ survivors }-\sum_{i=1}^{\mathrm{n}_{\mathrm{i}}}\left(\underbrace{\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{LI}} \mathrm{e}^{\lambda t_{i}^{\mathrm{LI}}}-\mathrm{t}_{\mathrm{i}}^{\mathrm{NI}} \mathrm{e}^{\lambda t_{i}^{\mathrm{NI}}}}_{\text {interval failures }}\right)=0$ |  |  |
| Point <br> Estimates | When there is only complete and right-censored data the point estimate is: $\hat{\lambda}=\frac{\mathrm{n}_{\mathrm{F}}}{t_{T}} \quad$ where $\quad t_{T}=\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{F}}+\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{S}}=$ total time in test |  |  |
| Fisher <br> Information | $I(\lambda)=\frac{1}{\lambda}$ |  |  |
| $100 \mathrm{~F} \%$ <br> Confidence <br> Interval <br> (excluding <br> interval data) |  | $\begin{aligned} & \lambda_{\text {lower }} \\ & 2 \text { Sided } \end{aligned}$ | $\begin{aligned} & \lambda_{\text {upper }} \\ & 2 \text { Sided } \end{aligned}$ | $\begin{aligned} & \lambda_{\text {upper }} \\ & 1 \text { Sided } \end{aligned}$ |
|  | Type I (Time Terminated) | $\frac{x_{(1-\mathrm{T})}^{2}\left(2 \mathrm{n}_{\mathrm{F}}\right)}{2 t_{T}}$ | $\frac{x_{(1+\mathrm{T})}^{2}\left(2 \mathrm{n}_{\mathrm{F}}+2\right)}{2 t_{T}}$ | $\frac{x_{(Y)}^{2}\left(2 \mathrm{n}_{\mathrm{F}}+2\right)}{2 t_{T}}$ |
|  | Type II (Failure Terminated) | $\frac{x_{(1-\mathrm{T})}^{2}\left(2 \mathrm{n}_{\mathrm{F}}\right)}{2 t_{T}}$ | $\frac{x_{(1+\mathrm{T})}^{2}\left(2 \mathrm{n}_{\mathrm{F}}\right)}{2 t_{T}}$ | $\frac{x_{(Y)}^{2}\left(2 \mathrm{n}_{\mathrm{F}}\right)}{2 t_{T}}$ ||  | $\chi_{(\alpha)}^{2}$ is the $\alpha$ percentile of the Chi-squared distribution. (Modarres et al. 1999, pp.151-152) Note: These confidence intervals are only valid for complete and right-censored data or when approximations of interval data are used (such as the median). They are exact confidence bounds and therefore approximate methods such as use of the Fisher information matrix need not be used. |
| :--: | :--: |
| Bayesian |  |
| Non-informative Priors $\pi(\lambda)$ <br> (Yang and Berger 1998, p.6) |  |
| Type | Prior | Posterior |
| Uniform Proper Prior with limits $\lambda \in[\alpha, b]$ | $\frac{1}{b-a}$ | Truncated Gamma Distribution <br> For $a \leq \lambda \leq b$ <br> $c . \operatorname{Gamma}\left(\lambda ; 1+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right)$ <br> Otherwise $\pi(\lambda)=0$ |
| Uniform Improper Prior with limits $\lambda \in[0, \infty)$ | $1 \propto \operatorname{Gamma}(1,0)$ | $\operatorname{Gamma}\left(\lambda ; 1+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right)$ |
| Jeffrey's Prior | $\frac{1}{\sqrt{\lambda}} \propto \operatorname{Gamma}\left(\frac{1}{\lambda}, 0\right)$ | $\begin{gathered} \operatorname{Gamma}\left(\lambda ; \frac{1}{\lambda}+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right) \\ \text { when } \lambda \in[0, \infty) \end{gathered}$ |
| Novick and Hall | $\frac{1}{\lambda} \propto \operatorname{Gamma}(0,0)$ | $\begin{gathered} \operatorname{Gamma}\left(\lambda ; \mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}}\right) \\ \text { when } \lambda \in[0, \infty) \end{gathered}$ |
| where $t_{T}=\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{F}}+\sum \mathrm{t}_{\mathrm{i}}^{\mathrm{S}}=$ total time in test |  |  |
| Conjugate Priors |  |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \lambda \\ \text { from } \\ \operatorname{Exp}(t ; \lambda) \end{gathered}$ | Exponential | $n_{F}$ failures <br> in $t_{T}$ unit of <br> time | Gamma | $k_{0}, \Lambda_{0}$ | $\begin{aligned} & k=k_{o}+n_{F} \\ & \Lambda=\Lambda_{o}+t_{T} \end{aligned}$ |
| Description, Limitations and Uses |  |  |
| Example | Three vehicle tires were run on a test area for 1000km have punctures at the following distances: <br> Tire 1: No punctures <br> Tire 2: $400 \mathrm{~km}, 900 \mathrm{~km}$ <br> Tire 3: 200km <br> Punctures are a random failure with constant failure rate therefore an exponential distribution would be appropriate. Due to an exponential distribution being homogeneous in time, the renewal process of the second tire failing twice with a repair can be considered as two separate tires on test with single failures. See example in section 1.1.6. <br> Total distance on test is $3 \times 1000=3000 \mathrm{~km}$. Total number of |  |failures is 3. Therefore using MLE the estimate of $\lambda$ :

$$
\hat{\lambda}=\frac{\mathrm{n}_{\mathrm{F}}}{t_{T}}=\frac{3}{3000}=1 \mathrm{E}-3
$$

With $90 \%$ confidence interval (distance terminated test):

$$
\left[\frac{\chi_{(0.05)}^{2}(6)}{6000}=0.272 E \cdot 3, \quad \frac{\chi_{(0.95)}^{2}(8)}{6000}=2.584 E \cdot 3\right]
$$

A Bayesian point estimate using the Jeffery non-informative improper prior $\operatorname{Gamma}\left(\frac{1}{2}, 0\right)$, with posterior $\operatorname{Gamma}(\lambda ; 3.5,3000)$ has a point estimate:

$$
\hat{\lambda}=\mathrm{E}[\operatorname{Gamma}(\lambda ; 3.5,3000)]=\frac{3.5}{3000}=1.1 \dot{6} \mathrm{E}-3
$$

With $90 \%$ confidence interval using inverse Gamma cdf:

$$
\left[F_{0}^{-1}(0.05)=0.361 E-3, \quad F_{0}^{-1}(0.95)=2.344 E-3\right]
$$

Characteristics
Constant Failure Rate. The exponential distribution is defined by a constant failure rate, $\lambda$. This means the component is not subject to wear or accumulation of damage as time increases.
$f(0)=\lambda$. As can be seen, $\lambda$ is the initial value of the distribution. Increases in $\lambda$ increase the probability density at $f(0)$.

HPP. The exponential distribution is the time to failure distribution of a single event in the Homogeneous Poisson Process (HPP).

$$
T \sim \operatorname{Exp}(t ; \lambda)
$$

Scaling property

$$
a T \sim \operatorname{Exp}\left(t ; \frac{\lambda}{a}\right)
$$

Minimum property

$$
\min \left\{T_{1}, T_{2}, \ldots, T_{n}\right\} \sim \operatorname{Exp}\left(t ; \sum_{i=1}^{n} \lambda_{i}\right)
$$

# Variate Generation property 

$$
F^{-1}(u)=\frac{\ln (1-u)}{-\lambda}, \quad 0<u<1
$$

Memoryless property.

$$
\operatorname{Pr}(T>t+x \mid T>t)=\operatorname{Pr}(T>x)
$$

Properties from (Leemis \& McQueston 2008).
Applications
No Wearout. The exponential distribution is used to model occasions when there is no wearout or cumulative damage. It can be used to approximate the failure rate in a component's useful life period (after burn in and before wear out).

Homogeneous Poisson Process (HPP). The exponential|  | distribution is used to model the inter arrival times in a repairable system or the arrival times in queuing models. See Poisson and Gamma distribution for more detail. <br> Electronic Components. Some electronic components such as capacitors or integrated circuits have been found to follow an exponential distribution. Early efforts at collecting reliability data assumed a constant failure rate and therefore many reliability handbooks only provide a failure rate estimates for components. <br> Random Shocks. It is common for the exponential distribution to model the occurrence of random shocks An example is the failure of a vehicle tire due to puncture from a nail (random shock). The probability of failure in the next mile is independent of how many miles the tire has travelled (memoryless). The probability of failure when the tire is new is the same as when the tire is old (constant failure rate). <br> In general component life distributions do not have a constant failure rate, for example due to wear or early failures. Therefore the exponential distribution is often inappropriate to model most life distributions, particularly mechanical components. |
| :--: | :--: |
| Resources | Online: <br> http://www.weibull.com/LifeDataWeb/the_exponential_distribution.h tm <br> http://mathworld.wolfram.com/ExponentialDistribution.html <br> http://en.wikipedia.org/wiki/Exponential_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> Books: <br> Balakrishnan, N. \& Basu, A.P., 1996. Exponential Distribution: Theory, Methods and Applications 1st ed., CRC. <br> Nelson, W.B., 1982. Applied Life Data Analysis, WileyInterscience. |
| Relationship to Other Distributions |  |
| 2-Para Exp Distribution $\operatorname{Exp}(t ; \mu, \beta)$ | Special Case: $\quad \operatorname{Exp}(t ; \lambda)=\operatorname{Exp}\left(t ; \mu=0, \beta=\frac{1}{2}\right)$ |
| Gamma Distribution $\operatorname{Gamma}(t ; k, \lambda)$ | Let $\quad T_{1} \ldots T_{k} \sim \operatorname{Exp}(\lambda) \quad$ and $\quad T_{t}=T_{1}+T_{2}+\cdots+T_{k}$ <br> Then $\quad T_{t} \sim \operatorname{Gamma}(k, \lambda)$ <br> The gamma distribution is the probability density function of the sum of $k$ exponentially distributed time random variables sharing the same constant rate of occurrence, $\lambda$. This is a Homogeneous Poisson Process. ||  | Special Case: $\quad \operatorname{Exp}(t ; \lambda)=\operatorname{Gamma}(t ; k=1, \lambda)$ |
| :--: | :--: |
| Poisson <br> Distribution $\operatorname{Pois}(k ; \mu)$ | Let $\quad T_{1}, T_{2} \ldots \sim \operatorname{Exp}(t ; \lambda)$ <br> Given $\quad$ time $=T_{1}+T_{2}+\cdots+T_{K}+T_{K+1} \ldots$ <br> Then $\quad K \sim \operatorname{Pois}(\mathrm{k} ; \mu=\lambda t)$ <br> The Poisson distribution is the probability of observing exactly $k$ occurrences within a time interval $[0, t]$ where the inter-arrival times of each occurrence is exponentially distributed. This is a Homogeneous Poisson Process. <br> Special Cases: $\quad \operatorname{Pois}(\mathrm{k}=1 ; \mu=\lambda t)=\operatorname{Exp}(t ; \lambda)$ |
| Weibull <br> Distribution <br> Weibull $(t ; \alpha, \beta)$ | Let $\quad X \sim \operatorname{Exp}(\lambda) \quad$ and $\quad Y=X^{1 / \beta}$ <br> Then $\quad Y \sim \operatorname{Weibull}\left(\alpha=\lambda^{\frac{-1}{\beta}}, \beta\right)$ <br> Special Case: $\quad \operatorname{Exp}(t ; \lambda)=\operatorname{Weibull}\left(t ; \alpha=\frac{1}{\lambda}, \beta=1\right)$ |
| Geometric <br> Distribution <br> Geometric $(k ; p)$ | Let $\quad X \sim \operatorname{Exp}(\lambda) \quad$ and $\quad Y=[X], \quad Y$ is the integer of $X$ <br> Then $\quad Y \sim \operatorname{Geometric}(\alpha, \beta)$ <br> The geometric distribution is the discrete equivalent of the continuous exponential distribution. The geometric distribution is also memoryless. |
| Rayleigh <br> Distribution <br> Rayleigh $(t ; \alpha)$ | Let <br> Then $\quad X \sim \operatorname{Exp}(\lambda) \quad$ and $\quad Y=\sqrt{X}$ <br> $Y \sim \operatorname{Rayleigh}\left(\alpha=\frac{1}{\sqrt{\lambda}}\right)$ |
| Chi-square $\chi^{2}(x ; v)$ | Special Case: $\quad \chi^{2}(x ; v=2)=\operatorname{Exp}\left(x ; \lambda=\frac{1}{2}\right)$ |
| Pareto <br> Distribution $\operatorname{Pareto}(t ; \theta, \alpha)$ | Let $\quad Y \sim \operatorname{Pareto}(\theta, \alpha) \quad$ and $\quad X=\ln (Y / \theta)$ <br> Then $\quad X \sim \operatorname{Exp}(\lambda=\alpha)$ |48 Common Life Distributions

| Logistic <br> Distribution <br> $\operatorname{Logistic}(\mu, s)$ | Let $\quad X \sim \operatorname{Exp}(\lambda=1) \quad$ and $\quad Y=\ln \left(\frac{e^{-X}}{1+e^{-X}}\right)$ |
| :-- | :-- |
|  | Then $\quad Y \sim \operatorname{Logistic}(0,1)$ <br> (Hastings et al. 2000, p.127): |# 2.2. Lognormal Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - F(t)


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\mu_{N}$ | $-\infty<\mu_{N}<\infty$ | Scale parameter: The mean of the normally distributed $\ln (x)$. This parameter only determines the scale and not the location as in a normal distribution. $\mu_{N}=\ln \left(\frac{\mu^{2}}{\sqrt{\sigma^{2}+\mu^{2}}}\right)$ |
|  | $\sigma_{N}^{2}$ | $\sigma_{N}^{2}>0$ | Shape parameter. The standard deviation of the normally distributed $\ln (x)$. This parameter only determines the shape and not the scale as in a normal distribution. $\sigma_{N}^{2}=\ln \left(\frac{\sigma^{2}+\mu^{2}}{\mu^{2}}\right)$ |
| Limits | $\mathrm{t}>0$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)=\frac{1}{\sigma_{N} t \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right)^{2}\right]$ $=\frac{1}{\sigma_{N} \cdot t} \phi\left[\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right]$ <br> where $\phi$ is the standard normal pdf. |  |  |
| CDF | $F(t)=\frac{1}{\sigma_{N} \sqrt{2 \pi}} \int_{0}^{t} \frac{1}{\theta} \exp \left[-\frac{1}{2}\left(\frac{\ln \left(t^{*}\right)-\mu_{N}}{\sigma_{N}}\right)^{2}\right] d t^{*}$ <br> where $t^{*}$ is the time variable over which the pdf is integrated. $=\frac{1}{2}+\frac{1}{2} \operatorname{erf}\left(\frac{\ln (t)-\mu_{N}}{\sigma_{N} \sqrt{2}}\right)$ $=\Phi\left(\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right)$ <br> where $\Phi$ is the standard normal cdf. |  |  |
| Reliability | $R(t)=1-\Phi\left(\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right)$ |  |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=\frac{1-\Phi\left(\frac{\ln (x+t)-\mu_{N}}{\sigma_{N}}\right)}{1-\Phi\left(\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right)}$ |  |  ||  | $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |
| :--: | :--: |
| Mean Residual Life | $\begin{gathered} u(t)=\frac{\int_{t}^{\infty} R(x) d x}{R(t)} \\ \lim _{t \rightarrow \infty} u(t) \approx \frac{\sigma_{N}^{2} t}{\ln (t)-\mu_{N}}[1+o(1)] \end{gathered}$ <br> Where $o(1)$ is Landau's notation. (Kleiber \& Kotz 2003, p.114) |
| Hazard Rate | $h(t)=\frac{\phi\left[\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right]}{t \cdot \sigma_{N}\left(1-\Phi\left[\frac{\ln (t)-\mu_{N}}{\sigma_{N}}\right]\right)}$ |
| Cumulative Hazard Rate | $H(t)=-\ln [R(t)]$ |
| Properties and Moments |  |
| Median | $e^{\left(\mu_{N}\right)}$ |
| Mode | $e^{\left(\mu_{N}-\sigma_{N}^{2}\right)}$ |
| Mean - $1^{\text {st }}$ Raw Moment | $e^{\left(\mu_{N}+\frac{\sigma_{N}^{2}}{2}\right)}$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\left(e^{\sigma_{N}^{2}}-1\right) \cdot e^{2 \mu_{N}+\sigma_{N}^{2}}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | $\left(e^{\sigma^{2}}+2\right) \cdot \sqrt{e^{\sigma^{2}}-1}$ |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $e^{4 \sigma_{N}^{2}}+2 e^{3 \sigma_{N}^{2}}+3 e^{2 \sigma_{N}^{2}}-3$ |
| Characteristic Function | Deriving a unique characteristic equation is not trivial and complex series solutions have been proposed. (Leipnik 1991) |
| 100a\% Percentile Function | $t_{a}=\mathrm{e}^{\left(\mu_{N}+z_{a} \cdot \sigma_{N}\right)}$ <br> where $z_{a}$ is the $100 p^{\text {th }}$ of the standard normal distribution $t_{a}=\mathrm{e}^{\left(\mu_{N}+\sigma_{N} \Phi^{-1}(a)\right)}$ |
| Parameter Estimation |  |
| Plotting Method |  |
| Least Mean Square $y=m x+c$ | X-Axis $\quad$ Y-Axis $\quad$ invNorm $\left[F\left(t_{i}\right)\right]$ $\frac{\mu_{N}}{1}$ $=\frac{c}{\frac{1}{m}}$ |
|  | $\frac{\ln \left(t_{i}\right)}{\sigma_{N}}=\frac{1}{\frac{1}{m}}$ |
| Maximum Likelihood Function |  || Likelihood <br> Functions | $\prod_{i=1}^{n_{F}} \frac{1}{\sigma_{N} \cdot t_{i}^{p}} \phi\left(z_{i}^{F}\right) \cdot \prod_{i=1}^{n_{S}}\left[1-\Phi\left(z_{i}^{S}\right)\right] \cdot \prod_{i=1}^{n_{t}}\left[\Phi\left(z_{i}^{R I}\right)-\Phi\left(z_{i}^{L I}\right)\right]$ <br> where $z_{i}^{x}=\left(\frac{\ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{x}}\right)-\mu_{N}}{\sigma_{N}}\right)$ |
| :--: | :--: | :--: |
| Log-Likelihood <br> Function | $\Lambda\left(\mu_{\mathrm{N}}, \sigma_{\mathrm{N}} \mid \mathrm{E}\right)=\sum_{i=1}^{\mathrm{n}_{\mathrm{F}}} \ln \left[\frac{1}{\sigma_{N} \cdot t_{i}^{F}} \phi\left(z_{i}^{\mathrm{F}}\right)\right]+\sum_{i=1}^{\mathrm{n}_{\mathrm{S}}} \ln \left[1-\Phi\left(z_{i}^{S}\right)\right]$ <br> where $+\sum_{i=1}^{\mathrm{n}_{\mathrm{T}}} \ln \left[\Phi\left(z_{i}^{R I}\right)-\Phi\left(z_{i}^{L I}\right)\right]$ <br> $\quad \frac{\ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{x}}\right)-\mu_{N}}{\sigma_{N}}$ |
| $\frac{\partial \Lambda}{\partial \mu_{\mathrm{N}}}=0$ | solve for $\mu_{N}$ to get MLE $\widehat{\mu_{N}}$ : $\begin{aligned} \frac{\partial \Lambda}{\partial \mu_{\mathrm{N}}} & =\underbrace{\frac{-\mu_{\mathrm{N}} \cdot \mathrm{N}^{\mathrm{F}}}{\sigma_{\mathrm{N}}}+\frac{1}{\sigma_{\mathrm{N}}} \sum_{i=1}^{\mathrm{n}_{\mathrm{F}}} \ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)}_{\text {failures }}+\underbrace{\frac{1}{\sigma_{\mathrm{N}}} \sum_{i=1}^{\mathrm{n}_{\mathrm{S}}} \frac{\phi\left(z_{i}^{\mathrm{S}}\right)}{1-\Phi\left(z_{i}^{\mathrm{S}}\right)}_{\text {survivors }}} \\ & -\sum_{i=1}^{\mathrm{n}_{\mathrm{T}}} \frac{1}{\sigma_{\mathrm{N}}}\left(\frac{\phi\left(z_{i}^{\mathrm{RI}}\right)-\phi\left(z_{i}^{\mathrm{LI}}\right)}{\Phi\left(z_{i}^{\mathrm{RI}}\right)-\Phi\left(z_{i}^{\mathrm{LI}}\right)}\right)=0 \end{aligned}$ <br> $\quad \frac{\ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{x}}\right)-\mu_{N}}{\sigma_{N}}$ |
| $\frac{\partial \Lambda}{\partial \sigma_{\mathrm{N}}}=0$ | solve for $\sigma_{N}$ to get $\widehat{\sigma_{N}}$ : $\begin{aligned} \frac{\partial \Lambda}{\partial \sigma_{\mathrm{N}}} & =\underbrace{\frac{-\mathrm{n}_{\mathrm{F}}}{\sigma_{\mathrm{N}}}+\frac{1}{\sigma_{\mathrm{N}}^{\mathrm{x}}} \sum_{i=1}^{\mathrm{n}_{\mathrm{F}}}\left(\ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)-\mu_{\mathrm{N}}\right)^{2}}_{\text {failures }}} & +\underbrace{\frac{1}{\sigma_{\mathrm{N}}} \sum_{i=1}^{\mathrm{n}_{\mathrm{F}}} \frac{z_{i}^{\mathrm{B}} \cdot \phi\left(z_{i}^{\mathrm{B}}\right)}{1-\Phi\left(z_{i}^{\mathrm{B}}\right)}}_{\text {survivors }} \\ & -\sum_{i=1}^{\mathrm{n}_{\mathrm{T}}} \frac{1}{\sigma_{\mathrm{N}}}\left(\frac{z_{i}^{\mathrm{RI}} \cdot \phi\left(z_{i}^{\mathrm{RI}}\right)-z_{i}^{\mathrm{LI}} \phi\left(z_{i}^{\mathrm{LI}}\right)}{\Phi\left(z_{i}^{\mathrm{RI}}\right)-\Phi\left(z_{i}^{\mathrm{LI}}\right)}\right)=0 \end{aligned}$ <br> where $z_{i}^{x}=\left(\frac{\ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{x}}\right)-\mu_{N}}{\sigma_{N}}\right)$ |
| MLE Point <br> Estimates | When there is only complete failure data the point estimates can be given as: $\begin{aligned} \widehat{\mu_{N}} & =\frac{\sum \ln \left(t_{i}^{F}\right)}{n_{F}} \quad \widehat{\sigma_{\mathrm{N}}^{2}}=\frac{\sum\left(\ln \left(t_{i}^{F}\right)-\widehat{\mu_{t}}\right)^{2}}{n_{F}} \end{aligned}$ <br> Note: In almost all cases the MLE methods for a normal distribution ||  | can be used by taking the $\ln (X)$. However Normal distribution estimation methods cannot be used with interval data. (Johnson et al. 1994, p.220) <br> In most cases the unbiased estimators are used: $\hat{\mu}_{N}=\frac{\sum \ln \left(t_{i}^{F}\right)}{n_{F}} \quad \hat{\sigma_{N}^{2}}=\frac{\sum\left(\ln \left(t_{i}^{F}\right)-\hat{\mu}_{t}\right)^{2}}{n_{F}-1}$ |
| :--: | :--: |
| Fisher Information | $l\left(\mu_{N}, \sigma_{N}^{2}\right)=\left[\begin{array}{cc}\frac{1}{\sigma_{N}^{2}} & 0 \\ 0 & -\frac{1}{2 \sigma^{4}}\end{array}\right]$ <br> (Kleiber \& Kotz 2003, p.119). |
| $\begin{aligned} & 100 y \% \\ & \text { Confidence } \\ & \text { Intervals } \end{aligned}$ <br> (for complete data) | 1 Sided - Lower  <br> $\mu_{N} \quad \hat{\mu}_{N}-\frac{\hat{\sigma}_{N}}{\sqrt{n_{F}}} t_{\gamma}\left(n_{F}-1\right) \quad \hat{\mu}_{N}-\frac{\hat{\sigma}_{N}}{\sqrt{n_{F}}} t_{\left(\frac{1-\gamma}{2}\right)}\left(n_{F}-1\right) \quad \hat{\mu}_{N}+\frac{\hat{\sigma}_{N}}{\sqrt{n_{F}}} t_{\left(\frac{1-\gamma}{2}\right)}\left(n_{F}-1\right)$ |
|  | $\hat{\sigma}_{N}^{2} \quad \hat{\sigma}_{N}^{2} \frac{\left(n_{F}-1\right)}{\chi_{F}^{2}\left(n_{F}-1\right)} \quad \hat{\sigma_{N}^{2}} \frac{\left(n_{F}-1\right)}{\chi_{\left(\frac{1-\gamma}{2}\right)}^{2}\left(n_{F}-1\right)} \quad \hat{\sigma_{N}^{2}} \frac{\left(n_{F}-1\right)}{\chi_{\left(\frac{1-\gamma}{2}\right)}^{2}\left(n_{F}-1\right)}$ |
|  | Where $t_{\gamma}\left(n_{F}-1\right)$ is the $100 y^{\text {th }}$ percentile of the $t$-distribution with $n_{F}-1$ degrees of freedom and $\chi_{F}^{2}\left(n_{F}-1\right)$ is the $100 y^{\text {th }}$ percentile of the $\chi^{2}$-distribution with $n_{F}-1$ degrees of freedom. (Nelson 1982, pp.218-219) |
|  | 1 Sided - Lower  <br> 2 Sided |
|  | $\mu_{N} \quad \exp \left\{\hat{\mu_{N}}+\frac{\hat{\sigma}_{N}^{2}}{2}-Z_{1-\alpha} \sqrt{\hat{\sigma}_{N}^{2}}+\frac{\hat{\sigma}_{N}^{2}}{2\left(n_{F}-1\right)}\right\} \quad \exp \left\{\hat{\mu_{N}}+\frac{\hat{\sigma}_{N}^{2}}{2} \pm Z_{1-\pi / 2} \sqrt{\hat{\sigma}_{N}^{2}}+\frac{\hat{\sigma}_{N}^{2}}{2\left(n_{F}-1\right)}\right\}$ |
|  | These formulas are the Cox approximation for the confidence intervals of the lognormal distribution mean where $Z_{p}=\Phi^{-1}(p)$, the inverse of the standard normal cdf. (Zhou \& Gao 1997) <br> Zhou \& Gao recommend using the parametric bootstrap method for small sample sizes. (Angus 1994) |
| Bayesian |  |
| Non-informative Priors when $\sigma_{N}^{2}$ is known, $\pi_{0}\left(\mu_{N}\right)$ (Yang and Berger 1998, p.22) |  |
| Type | Prior Posterior |
| Uniform Proper <br> Prior with limits $\mu_{N} \in[a, b]$ | $\frac{1}{b-a} \quad \begin{aligned} & \text { Truncated Normal Distribution } \\ & \text { For } \mathrm{a} \leq \mu_{N} \leq \mathrm{b} \\ & \quad \text { c.Norm }\left(\mu_{N} ; \frac{\sum_{i=1}^{n_{F}} \ln t_{i}^{F}}{n_{F}}, \frac{\sigma_{N}^{2}}{n_{F}}\right) \\ & \text { Otherwise } \pi\left(\mu_{N}\right)=0 \end{aligned}$ || All | 1 | $\begin{gathered} \text { Norm }\left(\mu_{N} ; \frac{\sum_{i=1}^{n_{F}} \ln t_{i}^{F}}{n_{F}}, \frac{\sigma_{N}^{2}}{n_{F}}\right) \\ \text { when } \mu_{N} \in(\infty, \infty) \end{gathered}$ |
| :--: | :--: | :--: |
| Non-informative Priors when $\mu_{N}$ is known, $\pi_{a}\left(\sigma_{N}^{2}\right)$ (Yang and Berger 1998, p.23) |  |  |
|  | Type | Prior | Posterior |
|  | Uniform Proper Prior with limits $\sigma_{N}^{2} \in[a, b]$ | $\frac{1}{b-a}$ | Truncated Inverse Gamma Distribution For $\mathrm{a} \leq \sigma_{N}^{2} \leq \mathrm{b}$ $\begin{gathered} c . I G\left(\sigma_{N}^{2} ; \frac{\left(n_{F}-2\right)}{2}, \frac{S_{N}^{2}}{2}\right) \\ \text { Otherwise } \pi\left(\sigma_{N}^{2}\right)=0 \end{gathered}$ |
|  | Uniform <br> Improper Prior with limits $\sigma_{N}^{2} \in(0, \infty)$ | 1 | $\begin{gathered} I G\left(\sigma_{N}^{2} ; \frac{\left(n_{F}-2\right)}{2}, \frac{S_{N}^{2}}{2}\right) \\ \text { See section 1.7.1 } \end{gathered}$ |
|  | Jeffery's, <br> Reference, MDIP <br> Prior | $\frac{1}{\sigma_{N}^{2}}$ | $\begin{gathered} I G\left(\sigma_{N}^{2} ; \frac{n_{F}}{2}, \frac{S_{N}^{2}}{2}\right) \\ \text { with limits } \sigma_{N}^{2} \in(0, \infty) \\ \text { See section 1.7.1 } \end{gathered}$ |
| Non-informative Priors when $\mu_{N}$ and $\sigma_{N}^{2}$ are unknown, $\pi_{a}\left(\mu_{N}, \sigma_{N}^{2}\right)$ (Yang and Berger 1998, p.23) |  |  |  |
|  | Type | Prior | Posterior |
|  | Improper Uniform <br> with <br> limits: <br> $\mu_{N} \in(\infty, \infty)$ <br> $\sigma_{N}^{2} \in(0, \infty)$ | 1 | $\begin{gathered} \pi\left(\mu_{N} \mid E\right) \sim T\left(\mu_{N} ; n_{F}-3, \overline{t_{N}}, \frac{S_{N}^{2}}{n_{F}\left(n_{F}-3\right)}\right) \\ \text { See section 1.7.2 } \\ \pi\left(\sigma_{N}^{2} \mid E\right) \sim I G\left(\sigma_{N}^{2} ; \frac{\left(n_{F}-3\right)}{2}, \frac{S_{N}^{2}}{2}\right) \\ \text { See section 1.7.1 } \end{gathered}$ |
|  | Jeffery's Prior | $\frac{1}{\sigma_{N}^{2}}$ | $\begin{gathered} \pi\left(\mu_{N} \mid E\right) \sim T\left(\mu_{N} ; N^{F}+1, \overline{t_{N}}, \frac{S^{2}}{n_{F}\left(n_{F}+1\right)}\right) \\ \text { when } \mu_{N} \in(\infty, \infty) \\ \text { See section 1.7.2 } \\ \pi\left(\sigma_{N}^{2} \mid E\right) \sim I G\left(\sigma_{N}^{2} ; \frac{\left(n_{F}+1\right)}{2}, \frac{S_{N}^{2}}{2}\right) \\ \text { when } \sigma_{N}^{2} \in(0, \infty) \\ \text { See section 1.7.1 } \end{gathered}$ |
|  | Reference Prior ordering $\{\phi, \sigma\}$ | $\begin{gathered} \pi_{a}\left(\phi, \sigma_{N}^{2}\right) \\ \propto \frac{1}{\sigma_{N} \sqrt{2+\phi^{2}}} \\ \text { where } \\ \phi=\mu_{N} / \sigma_{N} \end{gathered}$ | No closed form || Reference where $\mu$ and $\sigma^{2}$ are separate groups. <br> MDIP Prior | $\frac{1}{\sigma_{N}}$ | $\pi\left(\mu_{N} \mid E\right) \sim T\left(\mu_{N} ; N^{F}-1, \widetilde{t_{N}}, \frac{S_{N}^{2}}{\mathrm{n}_{\mathrm{F}}\left(\mathrm{n}_{\mathrm{F}}-1\right)}\right)$ when $\mu_{N} \in(\infty, \infty)$ <br> See section 1.7.2 $\pi\left(\sigma_{N}^{2} \mid E\right) \sim I G\left(\sigma_{N}^{2} ; \frac{\left(n_{F}-1\right)}{2}, \frac{S_{N}^{2}}{2}\right)$ when $\sigma_{N}^{2} \in(0, \infty)$ <br> See section 1.7.1 |
| :--: | :--: | :--: |

where

$$
S_{N}^{2}=\sum_{i=1}^{n_{F}}\left(\ln t_{i}-\widetilde{t_{N}}\right)^{2} \quad \text { and } \quad \widetilde{t_{N}}=\frac{1}{\mathrm{n}_{\mathrm{F}}} \sum_{i=1}^{n_{F}} \ln t_{i}
$$

| Conjugate Priors |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior Parameters |
| $\begin{gathered} \sigma_{N}^{2} \\ \text { from } \\ \log N\left(t ; \mu_{N}, \sigma_{N}^{2}\right) \end{gathered}$ | LogNormal with known $\mu_{N}$ | $\frac{n_{F}}{\text { failures }}$ <br> at times $t_{i}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{gathered} k=k_{o}+n_{F} / 2 \\ \lambda=\lambda_{o}+\frac{1}{2} \sum_{i=1}^{n_{F}}\left(\ln t_{i}-\mu_{N}\right)^{2} \end{gathered}$ |
| $\begin{gathered} \mu_{N} \\ \text { from } \\ \log N\left(t ; \mu_{N}, \sigma_{N}^{2}\right) \end{gathered}$ | LogNormal with known $\sigma_{N}^{2}$ | $\frac{n_{F}}{\text { failures }}$ <br> at times $t_{i}$ | Normal | $\mu_{o}, \sigma_{o}^{2}$ | $\begin{gathered} \mu=\frac{\frac{\mu_{0}}{\sigma_{0}^{2}}+\frac{\sum_{i=1}^{n_{F}} \ln \left(t_{i}\right)}{\sigma_{N}^{2}}}{\frac{1}{\sigma_{0}^{2}}+\frac{n_{F}}{\sigma_{N}^{2}}} \\ \sigma^{2}=\frac{1}{\frac{1}{\sigma_{0}^{2}}+\frac{n_{F}}{\sigma_{N}^{2}}} \end{gathered}$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | 5 components are put on a test with the following failure times: $98,116,2485,2526$, , 2920 hours <br> Taking the natural log of these failure times allows us to use a normal distribution to approximate the parameters. $\ln \left(t_{i}\right)$ : <br> $4.590,4.752,7.979,7.818,7.834 \ln$ (hours) <br> MLE Estimates are: $\begin{gathered} \widehat{\mu_{N}}=\frac{\sum \ln \left(t_{i}^{F}\right)}{\mathrm{n}_{\mathrm{F}}}=\frac{32.974}{5}=6.595 \\ \widehat{\sigma_{N}^{2}}=\frac{\sum\left(\ln \left(t_{i}^{F}\right)-\widehat{\mu_{t}}\right)^{2}}{\mathrm{n}_{\mathrm{F}}-1}=3.091 \end{gathered}$ <br> $90 \%$ confidence interval for $\mu_{N}$ : $\left[\widehat{\mu_{N}}-\frac{\widehat{\sigma_{N}}}{\sqrt{4}} t_{[0.95]}(4), \quad \widehat{\mu_{N}}+\frac{\widehat{\sigma_{N}}}{\sqrt{4}} t_{[0.95]}(4)\right]$ |  |  |  |  |  |
|  |  |  |  |  |  |  ||  | $[4.721,8.469]$ <br> $90 \%$ confidence interval for $\sigma_{N}^{2}$ : <br> A Bayesian point estimate using the Jeffery non-informative improper prior $1 / \sigma_{N}^{3}$ with posterior for $\mu_{N} \sim T(6,6.595,0.412)$ and $\sigma_{N}^{2} \sim I G(3,6.182)$ has a point estimates: $\begin{aligned} & \widehat{\mu_{N}}=\mathrm{E}[T(6,6.595,0.412)]=\mu=6.595 \\ & \widehat{\sigma_{N}^{2}}=\mathrm{E}[I G(3,6.182)]=\frac{6.182}{2}=3.091 \end{aligned}$ <br> With $90 \%$ confidence intervals: $\mu_{N} \quad\left[F_{T}^{-1}(0.05)=5.348, \quad F_{T}^{-1}(0.95)=7.842\right]$ $\sigma_{N}^{2} \quad\left[1 / F_{G}^{-1}(0.95)=0.982, \quad 1 / F_{G}^{-1}(0.05)=7.560\right]$ |
| :--: | :--: |
| Characteristics | $\mu_{N}$ Characteristics. $\mu_{N}$ determines the scale and not the location as in a normal distribution. The distribution if fixed at $\mathrm{f}(0)=0$ and an increase in the scale parameter stretches the distribution across the x -axis. This has the effect of increasing the mode, mean and median of the distribution. <br> $\sigma_{N}$ Characteristics. $\sigma_{N}$ determines the shape and not the scale as in a normal distribution. For values of $\sigma_{N}>1$ the distribution rises very sharply at the beginning and decreases with a shape similar to an Exponential or Weibull with $0<\beta<1$. As $\sigma_{N} \rightarrow 0$ the mode, mean and median converge to $e^{\mu_{N}}$. The distribution becomes narrower and approaches a Dirac delta function at $t=e^{\mu_{N}}$. <br> Hazard Rate. (Kleiber \& Kotz 2003, p.115)The hazard rate is unimodal with $h(0)=0$ and all dirivitives of $h^{\prime}(t)=0$ and a slow decrease to zero as $t \rightarrow 0$. The mode of the hazard rate: $t_{m}=\exp \left(\mu+z_{m} \sigma\right)$ <br> where $z_{m}$ is given by: $\left(z_{m}+\sigma_{N}\right)=\frac{\phi\left(z_{m}\right)}{1-\Phi\left(z_{m}\right)}$ <br> therefore $-\sigma_{N}<z_{m}<-\sigma_{N}+\sigma^{-1}$ and therefore: $e^{\mu_{N}-\sigma_{N}^{2}}<t_{m}<e^{\mu_{N}-\sigma_{N}^{2}+1}$ <br> As $\sigma_{N} \rightarrow \infty, t_{m} \rightarrow e^{\mu_{N}-\sigma_{N}^{2}}$ and so for large $\sigma_{N}$ : $\max h(t) \approx \frac{\exp \left(\mu_{N}-\frac{1}{2} \sigma_{N}^{2}\right)}{\sigma_{N} \sqrt{2 \pi}}$ ||  | As $\sigma_{N} \rightarrow 0, t_{\mathrm{m}} \rightarrow e^{\mu_{N}-\sigma_{N}^{2}+1}$ and so for large $\sigma_{N}$ : $\max h(t) \approx \frac{1}{\sigma_{N}^{2} e^{\mu_{N}-\sigma_{N}^{2}+1}}$ <br> Mean / Median / Mode: $\quad \operatorname{mode}(X)<\operatorname{median}(X)<E[X]$ |
| :--: | :--: |
| Scale/Product Property: <br> Let: $\begin{gathered} a_{j} X_{j} \sim \log N\left(\mu_{N j}, \sigma_{N j}^{2}\right) \\ \prod a_{j} X_{j} \sim \log N\left(\sum\left[\mu_{N j}+\ln \left(a_{j}\right)\right], \sum \sigma_{N j}^{2}\right) \end{gathered}$ <br> Lognormal versus Weibull. In analyzing life data to these distributions it is often the case that both may be a good fit, especially in the middle of the distribution. The Weibull distribution has an earlier lower tail and produces a more pessimistic estimate of the component life. (Nelson 1990, p.65) |  |
| Applications | General Life Distributions. The lognormal distribution has been found to accurately model many life distributions and is a popular choice for life distributions. The increasing hazard rate in early life models the weaker subpopulation (burn in) and the remaining decreasing hazard rate describes the main population. In particular this has been applied to some electronic devices and fatiguefracture data. (Meeker \& Escobar 1998, p.262) <br> Failure Modes from Multiplicative Errors. The lognormal distribution is very suitable for failure processes that are a result of multiplicative errors. Specific applications include failure of components due to fatigue cracks. (Provan 1987) <br> Repair Times. The lognormal distribution has commonly been used to model repair times. It is natural for a repair time probability to increase quickly to a mode value. For example very few repairs have an immediate or quick fix. However, once the time of repair passes the mean it is likely that there are serious problems, and the repair will take a substantial amount of time. <br> Parameter Variability. The lognormal distribution can be used to model parameter variability. This was done when estimating the uncertainty in the parameter $\lambda$ in a Nuclear Reactor Safety Study (NUREG-75/014). <br> Theory of Breakage. The distribution models particle sizes observed in breakage processes (Crow \& Shimizu 1988) |
| Resources | Online: ||  | http://www.weibull.com/LifeDataWeb/the_lognormal_distribution.ht m http://mathworld.wolfram.com/LogNormalDistribution.html http://en.wikipedia.org/wiki/Log-normal_distribution http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> Books: <br> Crow, E.L. \& Shimizu, K., 1988. Lognormal distributions, CRC Press. <br> Aitchison, J.J. \& Brown, J., 1957. The Lognormal Distribution, New York: Cambridge University Press. <br> Nelson, W.B., 1982. Applied Life Data Analysis, WileyInterscience. |
| :--: | :--: |
| Relationship to Other Distributions |  |
| Normal Distribution $\operatorname{Norm}\left(t ; \mu, \sigma^{2}\right)$ | Let: $\begin{gathered} X \sim \log N\left(\mu_{N}, \sigma_{N}^{2}\right) \\ Y=\ln (X) \end{gathered}$ <br> Then: $\quad Y \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)$ <br> Where: $\quad \mu_{N}=\ln \left(\frac{\mu^{2}}{\sqrt{\sigma^{2}+\mu^{2}}}\right), \quad \sigma_{N}=\ln \left(\frac{\sigma^{2}+\mu^{2}}{\mu^{2}}\right)$ |# 2.3. Weibull Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |
| :--: | :--: | :--: |
| Parameters | $\alpha$ | $\alpha>0$ | Scale Parameter: The value of $\alpha$ equals the 63.2 th percentile and has a unit equal to $t$. Note that this is not equal to the mean. |
|  | $\beta$ | $\beta>0$ | Shape Parameter: Also known as the slope (referring to a linear CDF plot) $\beta$ determines the shape of the distribution. |
| Limits | $t \geq 0$ |  |
| Distribution | Formulas |  |
| PDF | $f(t)=\frac{\beta t^{\beta-1}}{\alpha^{\beta}} e^{-\left(\frac{t}{\alpha}\right)^{\beta}}$ |  |
| CDF | $F(t)=1-e^{-\left(\frac{t}{\alpha}\right)^{\beta}}$ |  |
| Reliability | $\mathrm{R}(\mathrm{t})=e^{-\left(\frac{t}{\alpha}\right)^{\beta}}$ |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=e^{\left(\frac{t^{\beta}-(t+x)^{\beta}}{\alpha^{\beta}}\right)}$ <br> Where <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |
| Mean Residual Life | (Kleiber \& Kotz 2003, p.176) <br> which has the asymptotic property of: $\lim _{t \rightarrow \infty} u(t)=t^{1-\beta}$ |  |
| Hazard Rate | $h(t)=\frac{\beta}{\alpha}\left(\frac{t}{\alpha}\right)^{\beta-1}$ |  |
| Cumulative <br> Hazard Rate | $H(t)=\left(\frac{t}{\alpha}\right)^{\beta}$ |  |
| Properties and Moments |  |  |
| Median | $\alpha(\ln (2))^{\frac{1}{\beta}}$ |  |
| Mode | $\alpha\left(\frac{\beta-1}{\beta}\right)^{\frac{1}{\beta}} \quad$ if $\beta \geq 1$ <br> otherwise no mode exists |  || Mean - $1^{\text {st }}$ Raw Moment | $\alpha \Gamma\left(1+\frac{1}{\beta}\right)$ |
| :--: | :--: |
| Variance - $2^{\text {nd }}$ Central Moment | $\alpha^{2}\left[\Gamma\left(1+\frac{2}{\beta}\right)-\Gamma^{2}\left(1+\frac{1}{\beta}\right)\right]$ |
| Skewness - $3^{\text {rd }}$ Central Moment | $\frac{\Gamma\left(1+\frac{3}{\beta}\right) \alpha^{3}-3 \mu \sigma^{2}-\mu^{3}}{\sigma^{3}}$ |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $\frac{-6 \Gamma_{1}^{4}+12 \Gamma_{1}^{2} \Gamma_{2}-3 \Gamma_{2}^{2}-4 \Gamma_{1} \Gamma_{3}+\Gamma_{4}}{\left(\Gamma_{2}-\Gamma_{1}^{2}\right)^{2}}$ <br> where: $\Gamma_{i}=\Gamma\left(1+\frac{i}{\beta}\right)$ |
| Characteristic Function | $\sum_{n=0}^{\infty} \frac{(i t)^{n} \alpha^{n}}{n!} \Gamma\left(1+\frac{n}{\beta}\right)$ |
| 100p\% Percentile Function | $t_{p}=\alpha[-\ln (1-p)]^{\frac{1}{\beta}}$ |
| Parameter Estimation |  |
| Plotting Method |  |
| Least Mean Square $y=m x+c$ | X-Axis $\quad$ Y-Axis $\quad \tilde{\alpha}=e^{-\frac{c}{\beta m}}$ <br> $\ln \left[\ln \left(\frac{1}{1-F}\right)\right]$ $\tilde{\beta}=m$ |
| Maximum Likelihood Function |  |
| Likelihood Functions | $\mathrm{L}(\alpha, \beta \mid \mathrm{E})=\underbrace{\prod_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{p}}} \frac{\beta\left(t_{i}^{p}\right)^{\beta-1}}{\alpha^{\beta}} e^{-\left(\frac{t_{i}^{p}}{\alpha}\right)^{\beta}}}_{\begin{array}{c}\text { failures } \\ \prod_{i=1}^{\mathrm{n}_{\mathrm{s}}} e^{-\left(\frac{t_{i}^{s}}{\alpha}\right)^{\beta}} \end{array}}-e^{-\left(\frac{t_{i}^{s}}{\alpha}\right)^{\beta}}_{\text {survivors }}$ |
| Log-Likelihood Function | $\Lambda(\alpha, \beta \mid \mathrm{E})=\underbrace{\mathrm{n}_{\mathrm{p}} \ln (\beta)-\beta \mathrm{n}_{\mathrm{p}} \ln (\alpha)+\sum_{\substack{i=1 \\ i=1}}^{\mathrm{n}_{\mathrm{p}}}\left\{(\beta-1) \ln \left(t_{i}^{p}\right)-\left(\frac{t_{i}^{p}}{\alpha}\right)^{\beta}\right\}}_{-\sum_{\substack{i=1 \\ i \neq 1}}^{\mathrm{n}_{\mathrm{s}}}\left(\frac{t_{i}^{s}}{\alpha}\right)^{\beta}+\sum_{\substack{i=1 \\ i=1}}^{\mathrm{n}_{\mathrm{i}}} \ln \left(\mathrm{e}^{-\left(\frac{t_{i}^{s}}{\alpha}\right)^{\beta}}-\mathrm{e}^{-\left(\frac{t^{s}}{\alpha}\right)^{\beta}}\right)}_{\text {interval failures }}$ || $\frac{\partial \Lambda}{\partial \alpha}=0$ | solve for $\alpha$ to get $\tilde{\alpha}$ : <br> Solve for $\beta$ to get $\hat{\beta}$ : <br> $\frac{\partial \Lambda}{\partial \alpha}=\underbrace{\frac{n_{\mathrm{F}}}{\beta}+\sum_{i=1}^{n_{\mathrm{F}}}\left\{\ln \left(\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}{\alpha}\right)-\left(\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}{\alpha}\right)^{\beta} \cdot \ln \left(\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}{\alpha}\right)\right\}}_{\text {failures }} \cdot \underbrace{\sum_{i=1}^{n_{\mathrm{f}}} \frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{S}}}{\alpha}}^{\beta \cdot \ln \left(\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}{\alpha}\right)^{\beta}} \cdot \underbrace{\left(\frac{\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}}{\alpha}\right)}_{\text {survivors }}$ <br> Note: Numerical methods are needed to solve $\hat{\beta}$ then substitute to find $\tilde{\alpha}$. Numerical methods to find Weibull MLE estimates for complete and censored data for 2 parameter and 3 parameter Weibull distribution are detailed in (Rinne 2008). |
| :--: | :--: |
| $\frac{\partial \Lambda}{\partial \beta}=0$ |  |
| MLE Point Estimates | When there is only complete failure and/or right censored data the point estimates can be solved using (Rinne 2008, p.439): $\tilde{\alpha}=\left[\frac{\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)^{\beta}+\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{S}}\right)^{\beta}}{\mathrm{n}_{\mathrm{F}}}\right]^{\frac{1}{\beta}}$ $\hat{\beta}=\left[\frac{\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)^{\beta} \ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)+\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{S}}\right)^{\beta} \ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{S}}\right)}{\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)^{\beta}+\sum\left(\mathrm{t}_{\mathrm{i}}^{\mathrm{S}}\right)^{\beta}}-\frac{1}{n_{F}} \sum \ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right)\right]^{-1}$ <br> Note: Numerical methods are needed to solve $\hat{\beta}$ then substitute to find $\tilde{\alpha}$. Numerical methods to find Weibull MLE estimates for complete and censored data for 2 parameter and 3 parameter Weibull distribution are detailed in (Rinne 2008). |
| Fisher <br> Information <br> Matrix <br> (Rinne 2008, <br> p.412) | $\begin{gathered} I(\alpha, \beta)=\left[\frac{\beta^{2}}{\alpha^{2}} \quad \frac{\Gamma^{\prime}(2)}{-\alpha}\right] \quad\left[\frac{\beta^{2}}{\alpha^{2}} \quad \frac{1-\gamma}{\alpha}\right] \\ \left[\frac{1-\gamma}{\alpha} \quad \frac{\pi^{2}}{6}+\left(1-\gamma^{2}\right) \beta^{2}\right] \\ \cong\left[\frac{\beta^{2}}{\alpha^{2}} \quad \frac{0.422784}{-\alpha}\right. \\ \left.\frac{0.422784}{-\alpha} \quad \frac{1.823680}{\beta^{2}}\right] \end{gathered}$ || $100 \mathrm{y} \%$ <br> Confidence <br> Interval <br> (complete data) | The asymptotic variance-covariance matrix of $(\bar{a}, \bar{\beta})$ is: (Rinne 2008, pp.412-417) $\operatorname{Cov}(\bar{a}, \bar{\beta})=\left[I_{n}(\bar{a}, \bar{\beta})\right]^{-1}=\frac{1}{n_{F}}\left[\begin{array}{cc}1.1087 \frac{\bar{a}^{2}}{\bar{\beta}^{2}} & 0.2570 \bar{a} \\ 0.2570 \bar{a} & 0.6079 \bar{\beta}^{2}\end{array}\right]$ |
| :--: | :--: |
| Bayesian |  |
| Bayesian analysis is applied to either one of two re-parameterizations of the Weibull Distribution: (Rinne 2008, p.517) $\begin{aligned} & f(t ; \lambda, \beta)=\lambda \beta t^{\beta-1} \exp \left(-\lambda t^{\beta}\right) \text { where } \lambda=\alpha^{-\beta} \\ & f(t ; \theta, \beta)=\frac{\beta}{\theta} t^{\beta-1} \exp \left(-\frac{t^{\beta}}{\theta}\right) \text { where } \theta=\frac{1}{\lambda}=\alpha^{\beta} \end{aligned}$ |  |
| Non-informative Priors $\pi_{0}(\lambda)$ (Rinne 2008, p.517) |  |
| Type | Prior Posterior |
| Uniform Proper Prior with known $\beta$ and limits $\lambda \in[a, b]$ | $\frac{1}{b-a} \quad \begin{aligned} & \text { Truncated Gamma Distribution } \\ & \text { For } \mathrm{a} \leq \lambda \leq \mathrm{b} \\ & \quad \text { c. } \operatorname{Gamma}\left(\lambda ; 1+\mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}, \beta}\right) \end{aligned}$ <br> Otherwise $\pi(\lambda)=0$ |
| Jeffrey's Prior when $\beta$ is known. | $\frac{1}{\lambda} \propto \operatorname{Gamma}(0,0) \quad \begin{gathered} \operatorname{Gamma}\left(\lambda ; \mathrm{n}_{\mathrm{F}}, \mathrm{t}_{\mathrm{T}, \beta}\right) \\ \text { when } \lambda \in[0, \infty) \end{gathered}$ |
| Jeffrey's Prior for unknown $\theta$ and $\beta$. | $\frac{1}{\theta \beta} \quad \begin{gathered} \text { No closed form } \\ \text { (Rinne 2008, p.527) } \end{gathered}$ |
| where $t_{T, \beta}=\sum\left(\mathrm{t}_{i}^{\mathrm{F}}\right)^{\beta}+\sum\left(\mathrm{t}_{i}^{\mathrm{S}}\right)^{\beta}=$ adjusted total time in test |  |
| Conjugate Priors |  |
| It was found by Soland that no joint continuous prior distribution exists for the Weibull distribution. Soland did however propose a procedure which used a continuous distribution for $\alpha$ and a discrete distribution for $\beta$ which will not be included here. (Martz \& Waller 1982) |  |
| UOI | Likelihood <br> Model Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \lambda \\ \text { where } \\ \lambda=\alpha^{-\beta} \\ \text { from } \\ W b l(t ; \alpha, \beta) \end{gathered}$ | Weibull with known $\beta$ | $n_{F}$ failures at times $t_{i}^{F}$ | Gamma | $k_{0}, \Lambda_{0}$ | $\begin{gathered} k=k_{\alpha}+n_{F} \\ \Lambda=\Lambda_{0}+t_{T, \beta} \\ \text { (Rinne 2008, } \\ \text { p.520) } \end{gathered}$ || $\begin{gathered} \theta \\ \text { where } \\ \theta=\alpha^{p} \\ \text { from } \\ W b l(t ; \alpha, \beta) \end{gathered}$ | Weibull with known $\beta$ | $n_{F}$ failures at times $t_{i}^{F}$ | Inverted Gamma | $\alpha_{0}, \beta_{0}$ | $\begin{gathered} \alpha=\alpha_{o}+n_{F} \\ \beta=\beta_{0}+t_{T, \beta} \\ \text { (Rinne 2008, } \\ \text { p.524) } \end{gathered}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | 5 components are put on a test with the following failure times: $535,613,976,1031,1875$ hours $\beta$ is found by numerically solving: $\begin{gathered} \beta=\frac{\left[\sum\left(t_{i}^{F}\right)^{\beta} \ln \left(t_{i}^{F}\right)\right.}{\sum\left(t_{i}^{F}\right)^{\beta}}-6.8118 \end{gathered}$ |  |  |  |  |
|  |  |  |  | $\beta=2.275$ |  |
|  | $\bar{\alpha}$ is found by solving: $\bar{\alpha}=\frac{\left[\sum\left(t_{i}^{F}\right)^{\beta}\right]^{\beta}}{\bar{n}_{F}}$ |  |  |  | $=1140$ |
|  | Covariance Matrix is: $\begin{gathered} \operatorname{Cov}(\bar{a}, \bar{\beta})=\frac{1}{5}\left[\begin{array}{ll} 1.1087 \frac{\bar{a}^{2}}{\bar{\beta}^{2}} & 0.2570 \bar{a} \\ 0.2570 \bar{a} & 0.6079 \bar{\beta}^{2} \end{array}\right]=\left[\begin{array}{ll} 55679 & 58.596 \\ 58.596 & 0.6293 \end{array}\right] \end{gathered}$ |  |  |  |  |
|  | $90 \%$ confidence interval for $\bar{a}$ : $\begin{gathered} {\left[\bar{a} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{55679}}{-\bar{a}}\right),} \\ {[811,} \quad 1602 \end{gathered}$ |  |  |  | $\left.\bar{a} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{55679}}{\bar{a}}\right)\right]$ |  |
|  | $90 \%$ confidence interval for $\beta$ : $\begin{gathered} {\left[\bar{\beta} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.6293}}{-\bar{\beta}}\right),} \\ {[1.282,} \quad 4.037 \end{gathered}$ |  |  |  | $\left.\bar{\beta} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.6293}}{\bar{\beta}}\right)\right]$ |
|  | Note that with only 5 samples the assumption that the parameter distribution is approximately normal is probably inaccurate and therefore the confidence intervals need to be used with caution. |  |  |  |  |
| Characteristics | The Weibull distribution is also known as a "Type III asymptotic distribution for minimum values". <br> $\beta$ Characteristics: $\beta<1$. The hazard rate decreases with time. |  |  |  |  |$\boldsymbol{\beta}=1$. The hazard rate is constant (exp distribution)
$\boldsymbol{\beta}>1$. The hazard rate increases with time.
$1<\boldsymbol{\beta}<2$. The hazard rate increases less as time increases. $\boldsymbol{\beta}=2$. The hazard rate increases with a linear relationship to time.
$\boldsymbol{\beta}>$ 2. The hazard rate increases more as time increases.
$\boldsymbol{\beta}<3.447798$. The distribution is positively skewed. (Tail to right).
$\boldsymbol{\beta}=$ 3.447798. The distribution is approximately symmetrical.
$\boldsymbol{\beta}>$ 3.447798. The distribution is negatively skewed (Tail to left).
$3<\boldsymbol{\beta}<4$. The distribution approximates a normal distribution.
$\boldsymbol{\beta}>$ 10. The distribution approximates a Smallest Extreme Value Distribution.

Note that for $\beta=0.999, f(0)=\infty$, but for $\beta=1.001, f(0)=0$. This rapid change creates complications when maximizing likelihood functions. (Weibull.com) As $\beta \rightarrow \infty$, the mode $\rightarrow \alpha$.
a Characteristics. Increasing $\alpha$ stretches the distribution over the time scale. With the $f(0)$ point fixed this also has the effect of increasing the mode, mean and median. The value for $\alpha$ is at the $63 \%$ Percentile. $F(\alpha)=0.632$..

$$
X \sim \operatorname{Weibull}(\alpha, \beta)
$$

Scaling property: (Leemis \& McQueston 2008)

$$
k X \sim \operatorname{Weibull}\left(\alpha k^{\beta}, \beta\right)
$$

Minimum property (Rinne 2008, p.107)

$$
\min \left\{X, X_{2}, \ldots, X_{n}\right\} \sim \operatorname{Weibull}\left(\alpha n^{-\frac{1}{\beta}}, \beta\right)
$$

When $\beta$ is fixed.

# Variate Generation property 

$$
F^{-1}(u)=\alpha[-\ln (1-u)]^{\frac{1}{\beta}}, \quad 0<u<1
$$

Lognormal versus Weibull. In analyzing life data to these distributions it is often the case that both may be a good fit, especially in the middle of the distribution. The Weibull distribution has an earlier lower tail and produces a more pessimistic estimate of the component life. (Nelson 1990, p.65)

| Applications | The Weibull distribution is by far the most popular life distribution <br> used in reliability engineering. This is due to its variety of shapes <br> and generalization or approximation of many other distributions. <br> Analysis assuming a Weibull distribution already includes the |
| :-- | :-- ||  | exponential life distribution as a special case. <br> There are many physical interpretations of the Weibull Distribution. Due to its minimum property a physical interpretation is the weakest link, where a system such as a chain will fail when the weakest link fails. It can also be shown that the Weibull Distribution can be derived from a cumulative wear model (Rinne 2008, p.15) <br> The following is a non-exhaustive list of applications where the Weibull distribution has been used in: <br> - Acceptance sampling <br> - Warranty analysis <br> - Maintenance and renewal <br> - Strength of material modeling <br> - Wear modeling <br> - Electronic failure modeling <br> - Corrosion modeling <br> A detailed list with references to practical examples is contained in (Rinne 2008, p.275) |
| :--: | :--: |
| Resources | Online: <br> http://www.weibull.com/LifeDataWeb/the_weibull_distribution.htm http://mathworld.wolfram.com/WeibullDistribution.html http://en.wikipedia.org/wiki/Weibull_distribution http://socr.ucla.edu/htm/s/SOCR_Distributions.html (interactive web calculator) <br> http://www.qualitydigest.com/jan99/html/weibull.html (how to use conduct Weibull analysis in Excel, William W. Dorner) <br> Books: <br> Rinne, H., 2008. The Weibull Distribution: A Handbook 1st ed., Chapman \& Hall/CRC. <br> Murthy, D.N.P., Xie, M. \& Jiang, R., 2003. Weibull Models 1st ed., Wiley-Interscience. <br> Nelson, W.B., 1982. Applied Life Data Analysis, WileyInterscience. |
| Relationship to Other Distributions |  |
| Three Parameter Weibull Distribution <br> Weibull $(t ; \alpha, \beta, \gamma)$ | The three parameter model adds a locator parameter to the two parameter Weibull distribution allowing a shift along the x -axis. This creates a period of guaranteed zero failures to the beginning of the product life and is therefore only used in special cases. <br> Special Case: $\begin{aligned} & \text { Weibull }(t ; \alpha, \beta)=\text { Weibull }(t ; \alpha, \beta, \gamma=0) \end{aligned}$ || Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let $\quad X \sim \operatorname{Weibull}(\alpha, \beta) \quad$ and $\quad Y=X^{\beta}$ <br> Then $\quad Y \sim \operatorname{Exp}\left(\lambda=\alpha^{-\beta}\right)$ <br> Special Case: $\quad \operatorname{Exp}(t ; \lambda)=\operatorname{Weibull}\left(t ; \alpha=\frac{1}{\lambda}, \beta=1\right)$ |
| :--: | :--: |
| Rayleigh Distribution Rayleigh $(t ; \alpha)$ | Special Case: $\quad \operatorname{Rayleigh}(t ; \alpha)=\operatorname{Weibull}(t ; \alpha, \beta=2)$ |
| $\chi$ Distribution $\chi(t \mid v)$ | Special Case: $\chi(t \mid v=2)=\operatorname{Weibull}(t \mid \alpha=\sqrt{2}, \beta=2)$ |# 3. Bathtub Life Distributions# 3.1. 2-Fold Mixed Weibull Distribution 

All shapes shown are variations from $p=0.5 \alpha_{1}=2 \beta_{1}=0.5 \alpha_{2}=10 \beta_{2}=20$
Probability Density Function - $f(t)$


Cumulative Density Function - F(t)


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\alpha_{i}$ | $\alpha_{i}>0$ | Scale Parameter: This is the scale for each Weibull Distribution. |
|  | $\beta_{i}$ | $\beta_{i}>0$ | Shape Parameters: The shape of each Weibull Distribution |
|  | $p$ | $0 \leq p \leq 1$ | Mixing Parameter. This determines the weight each Weibull Distribution has on the overall density function. |
| Limits | $t \geq 0$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)=p f_{1}(t)+(1-p) f_{2}(t)$ <br> where $f_{i}(t)=\frac{\beta_{i} t^{\beta_{i}-1}}{\alpha_{i}{ }^{\beta_{i}}} e^{-\left(\frac{t}{\alpha_{i}}\right)^{\beta_{i}}}$ and $i \in\{1,2\}$ |  |  |
| CDF | $F(t)=p F_{1}(t)+(1-p) F_{2}(t)$ <br> where $F_{i}(t)=1-e^{-\left(\frac{t}{\alpha_{i}}\right)^{\beta_{i}}} \quad$ and $i \in\{1,2\}$ |  |  |
| Reliability | $R(t)=p R_{1}(t)+(1-p) R_{2}(t)$ <br> where $R_{i}(t)=e^{-\left(\frac{t}{\alpha_{i}}\right)^{\beta_{i}}} \quad$ and $i \in\{1,2\}$ |  |  |
| Hazard Rate | $h(t)=w_{1}(t) h_{1}(t)+w_{2}(t) h_{2}(t)$ <br> where $w_{i}(t)=\frac{p_{i} R_{i}(t)}{\sum_{i=1}^{n} p_{i} R_{i}(t)} \quad$ and $i \in\{1,2\}$ |  |  |
| Properties and Moments |  |  |  |
| Median |  | Solved numerically |  |
| Mode |  | Solved numerically |  |
| Mean - $1^{\text {st }}$ Raw Moment |  | $p \alpha_{1} \Gamma\left(1+\frac{1}{\beta_{1}}\right)+(1-\mathrm{p}) \alpha_{2} \Gamma\left(1+\frac{1}{\beta_{2}}\right)$ |  |
| Variance - $2^{\text {nd }}$ Central Moment |  | $\begin{aligned} & p \cdot \operatorname{Var}\left[T_{1}\right]+(1-p) \operatorname{Var}\left[T_{2}\right] \\ & \quad \neq p\left(E\left[X_{1}\right]-E[X]\right)^{2} \\ & \quad \neq(1-p)\left(E\left[X_{2}\right]-E[X]\right)^{2} \end{aligned}$ <br> $p \cdot \alpha^{2}\left[\Gamma\left(1+\frac{2}{\beta_{1}}\right)-\Gamma^{2}\left(1+\frac{1}{\beta_{1}}\right)\right]$ |  ||  | $+(1-p) \alpha^{2}\left[\Gamma\left(1+\frac{2}{\beta_{2}}\right)-\Gamma^{2}\left(1+\frac{1}{\beta_{2}}\right)\right]$ |
| :-- | :--: |
|  | $+p\left[\alpha_{1} \Gamma\left(1+\frac{1}{\beta_{1}}\right)-E[X]\right]^{2}$ |
|  | $+(1-p)\left[\alpha_{2} \Gamma\left(1+\frac{1}{\beta_{2}}\right)-E[X]\right]^{2}$ |
| 100p\% Percentile Function | Solved numerically |
| Parameter Estimation |  |
| Plotting Method (Jiang \& Murthy 1995) |  |
| Plot Points on <br> a Weibull <br> Probability Plot | X-Axis | Y-Axis |
|  | $x=\ln (t)$ | $y=\ln \left[\ln \left(\frac{1}{1-F}\right)\right]$ |

Using the Weibull Probability Plot the parameters can be estimated. Jiang \& Murthy, 1995, provide a comprehensive coverage of this procedure and detail error in previous methods. A typical WPP for a 2-fold Mixed Weibull Distribution is:


# Sub Populations: 

The dotted lines in the WPP is the lines representing the subpopulations:

$$
\begin{aligned}
& L_{1}=\beta_{1}\left[x-\ln \left(\alpha_{1}\right)\right] \\
& L_{2}=\beta_{2}\left[x-\ln \left(\alpha_{2}\right)\right]
\end{aligned}
$$Asymptotes (Jiang \& Murthy 1995):
As $x \rightarrow-\infty(t \rightarrow 0)$ there exists an asymptote approximated by:

$$
y \approx \beta_{1}\left[x-\ln \left(\alpha_{1}\right)\right]+\ln (c)
$$

where

$$
c=\left\{\begin{array}{lr}
p & \text { when } \beta_{1} \neq \beta_{2} \\
p+(1-p) \cdot\left(\frac{\alpha_{1}}{\alpha_{2}}\right)^{\beta_{1}} & \text { when } \beta_{1}=\beta_{2}
\end{array}\right.
$$

As $x \rightarrow \infty(t \rightarrow \infty)$ the asymptote straight line can be approximated by:

$$
y \approx \beta_{1}\left[x-\ln \left(\alpha_{1}\right)\right]
$$

# Parameter Estimation 

Jiang and Murthy divide the parameter estimation procedure into three cases:

Well Mixed Case $\boldsymbol{\beta}_{2} \neq \boldsymbol{\beta}_{1}$ and $\boldsymbol{\alpha}_{1} \approx \boldsymbol{\alpha}_{2}$

- Estimate the parameters of $\alpha_{1}$ and $\beta_{1}$ from the $L_{1}$ line (right asymptote).
- Estimate the parameter $p$ from the separation distance between the left and right asymptotes.
- Find the point where the curve crosses $L_{1}$ (point I). The slope at point I is:

$$
\beta=p \beta_{1}+(1-p) \beta_{2}
$$

- Determine slope at point I and use to estimate $\beta_{2}$
- Draw a line through the intersection point I with slope $\beta_{2}$ and use the intersection point to estimate $\alpha_{2}$.


## Well Separated Case $\boldsymbol{\beta}_{2} \neq \boldsymbol{\beta}_{1}$ and $\boldsymbol{\alpha}_{1} \gg \boldsymbol{\alpha}_{2}$ or $\boldsymbol{\alpha}_{1} \ll \boldsymbol{\alpha}_{2}$

- Determine visually if data is scattered along the bottom (or top) to determine if $\alpha_{1} \ll \alpha_{2}$ (or $\alpha_{1} \gg \alpha_{2}$ ).
- If $\alpha_{1} \ll \alpha_{2}\left(\alpha_{1} \gg \alpha_{2}\right)$ locate the inflection, $y_{a}$, to the left (right) of the point I. This point $y_{a} \cong \ln [-\ln (1-p)] \quad\left\{$ or $\left.y_{a} \cong \ln [-\ln (p)]\right\}\right.$. Using this formula estimate $p$.
- Estimate $\alpha_{1}$ and $\alpha_{2}$ :
- If $\alpha_{1} \ll \alpha_{2}$ calculate point $y_{1}=\ln \left[\ln \left(1-p+\frac{p}{e x p(1)}\right)\right]$ and $y_{2}=\ln \left[\ln \left(\frac{1-p}{e x p(1)}\right)\right]$. Find the coordinates where $y_{1}$ and $y_{2}$ intersect the WPP curve. At these points estimate $\alpha_{1}=e^{x_{1}}$ and $\alpha_{2}=e^{x_{2}}$.
- If $\alpha_{1} \gg \alpha_{2}$ calculate point $y_{1}=\ln \left[-\ln \left(\frac{p}{e x p(1)}\right)\right]$ and $y_{2}=\ln \left[-\ln \left(p+\frac{1-p}{e x p(1)}\right)\right]$. Find the coordinates where $y_{1}$ and $y_{2}$ intersect the WPP curve. At these points estimate $\alpha_{1}=e^{x_{1}}$ and $\alpha_{2}=e^{x_{2}}$.
- Estimate $\beta_{1}$ :
- If $\alpha_{1} \ll \alpha_{2}$ draw and approximate $L_{2}$ ensuring it intersects $\alpha_{2}$. Estimate $\beta_{2}$ from the slope of $L_{2}$.
- If $\alpha_{1} \gg \alpha_{2}$ draw and approximate $L_{1}$ ensuring it intersects $\alpha_{1}$. Estimate $\beta_{1}$ from the slope of $L_{1}$.
- Find the point where the curve crosses $L_{1}$ (point I). The slope at point I is:

$$
\beta=p \beta_{1}+(1-p) \beta_{2}
$$

- Determine slope at point I and use to estimate $\beta_{2}$# Common Shape Parameter $\beta_{2}=\beta_{1}$ 

If $\left(\frac{\alpha_{1}}{\alpha_{1}}\right)^{\beta_{1}} \approx 1$ then:

- Estimate the parameters of $\alpha_{1}$ and $\beta_{1}$ from the $L_{1}$ line (right asymptote).
- Estimate the parameter $p$ from the separation distance between the left and right asymptotes.
- Draw a vertical line through $x=\ln \left(\alpha_{1}\right)$. The intersection with the WPP can yield an estimate of $\alpha_{2}$ using:

$$
y_{1}=\left(\frac{p}{\exp (1)}+\frac{1-p}{\exp \left[\left(\frac{\alpha_{2}}{\alpha_{1}}\right)^{\beta_{1}}\right]}\right)
$$

If $\left(\frac{\alpha_{2}}{\alpha_{1}}\right)^{\beta_{1}} \ll 1$ then:

- Find inflection point and estimate the y coordinate $y_{r}$. Estimate p using:

$$
y_{T} \cong \ln [-\ln (p)]
$$

- If $\alpha_{1} \ll \alpha_{2}$ calculate point $y_{1}=\ln \left[\ln \left(1-p+\frac{p}{\exp (1)}\right)\right]$ and $y_{2}=\ln \left[\ln \left(\frac{1-p}{\exp (1)}\right)\right]$. Find the coordinates where $y_{1}$ and $y_{2}$ intersect the WPP curve. At these points estimate $\alpha_{1}=e^{x_{1}}$ and $\alpha_{2}=e^{x_{2}}$.
- Using the left or right asymptote estimate $\beta_{1}=\beta_{2}$ from the slope.

| Maximum <br> Likelihood | MLE and Bayesian techniques can be used using numerical <br> methods however estimates obtained from the graphical methods <br> are useful for initial guesses. A literature review of MLE and <br> Bayesian methods is covered in (Murthy et al. 2003). |
| :-- | :-- |

## Description, Limitations and Uses

| Characteristics | Hazard Rate Shape. The hazard rate can be approximated at its <br> limits by (Jiang \& Murthy 1995): <br> Small $t: h(t) \approx c h_{1}(t) \quad$ Large $t: h(t) \approx h_{1}$ |
| :-- | :-- |

This result proves that the hazard rate (increasing or decreasing) of $h_{1}$ will dominate the limits of the mixed Weibull distribution. Therefore the hazard rate cannot be a bathtub curve shape. Instead the possible shapes of the hazard rate is:

- Decreasing
- Unimodal
- Decreasing followed by unimodal (rollercoaster)
- Bi-modal

The reason this distribution has been included as a bathtub distribution is because on many occasions the hazard rate of a complex product may follow the "rollercoaster" shape instead which is given as decreasing followed by unimodal shape.

The shape of the hazard rate is only determined by the two shape parameters $\beta_{1}$ and $\beta_{2}$. A complete study on the characterization of|  | the 2-Fold Mixed Weibull Distribution is contained in Jiang and Murthy 1998. <br> p Values <br> The mixture ratio, $p_{i}$, for each Weibull Distribution may be used to estimate the percentage of each subpopulation. However this is not a reliable measure and it known to be misleading (Berger \& Sellke 1987) <br> N-Fold Distribution (Murthy et al. 2003) <br> A generalization to the 2-fold mixed Weibull distribution is the n-fold case. This distribution is defined as: $f(t)=\sum_{i=1}^{n} p_{i} f_{i}(t)$ where $f_{i}(t)=\frac{\beta_{i} t^{\beta_{i}-1}}{\alpha_{i}^{\beta_{i}}} e^{-\left(\frac{t}{\alpha_{i}}\right)^{\beta_{i}}}$ and $\sum_{i=1}^{n} p_{i}=1$ <br> and the hazard rate is given as: $h(t)=\sum_{i=1}^{n} w_{i}(t) h_{i}(t)$ where $\quad w_{i}(t)=\frac{p_{i} R_{i}(t)}{\sum_{i=1}^{n} p_{i} R_{i}(t)}$ <br> It has been found that in many instances a higher number of folds will not significantly increase the accuracy of the model but does impose a significant overhead in the number of parameters to estimate. The 3-Fold Weibull Mixture Distribution has been studied by Jiang and Murthy 1996. <br> 2-Fold Weibull 3-Parameter Distribution <br> A common variation to the model presented here is to have the second Weibull distribution modeled with three parameters. |
| :--: | :--: |
| Resources | Books / Journals: <br> Jiang, R. \& Murthy, D., 1995. Modeling Failure-Data by Mixture of 2 Weibull Distributions : A Graphical Approach. IEEE Transactions on Reliability, 44, 477-488. <br> Murthy, D., Xie, M. \& Jiang, R., 2003. Weibull Models 1st ed., Wiley-Interscience. <br> Rinne, H., 2008. The Weibull Distribution: A Handbook 1st ed., Chapman \& Hall/CRC. <br> Jiang, R. \& Murthy, D., 1996. A mixture model involving three Weibull distributions. In Proceedings of the Second AustraliaJapan Workshop on Stochastic Models in Engineering, Technology and Management. Gold Coast, Australia, pp. 260-270. ||  | Jiang, R. \& Murthy, D., 1998. Mixture of Weibull distributions parametric characterization of failure rate function. Applied Stochastic Models and Data Analysis, (14), 47-65. <br> Balakrishnan, N. \& Rao, C.R., 2001. Handbook of Statistics 20: <br> Advances in Reliability 1st ed., Elsevier Science \& Technology. |
| :--: | :--: |
| Relationship to Other Distributions |  |
| Weibull <br> Distribution <br> Weibull $(t ; \alpha, \beta)=2 F W e i b u l l\left(t ; \alpha=\alpha_{1}, \beta=\beta_{1}, p=1\right)$ <br> Weibull $(t ; \alpha, \beta)=2 F W e i b u l l\left(t ; \alpha=\alpha_{2}, \beta=\beta_{2}, p=0\right)$ |  |# 3.2. Exponentiated Weibull Distribution 

Probability Density Function - $f(t)$



Cumulative Density Function - F(t)



Hazard Rate - $h(t)$

| Parameters \& Description |  |  |
| :--: | :--: | :--: |
| Parameters | $\alpha$ | $\alpha>0$ | Scale Parameter. |
|  | $\beta$ | $\beta>0$ | Shape Parameter. |
|  | $v$ | $v>0$ | Shape Parameter. |
| Limits | $t \geq 0$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)=\frac{\beta v t^{\beta-1}}{\alpha^{\beta}}\left[1-\exp \left\{-\left(\frac{t}{\alpha}\right)^{\beta}\right\}\right]^{v-1} \exp \left\{-\left(\frac{t}{\alpha}\right)^{\beta}\right\}$ $=v\left\{F_{W}(t)\right\}^{v-1} f_{W}(t)$ <br> Where $F_{W}(t)$ and $f_{W}(t)$ are the cdf and pdf of the two parameter Weibull distribution respectively. |  |  |
| CDF | $F(t)=\left[1-\exp \left\{-\left(\frac{t}{\alpha}\right)^{\beta}\right\}\right]^{v}$ |  |  |
|  | $=\left[F_{W}(t)\right]^{v}$ |  |  |
| Reliability | $R(t)=1-\left[1-\exp \left\{-\left(\frac{t}{\alpha}\right)^{\beta}\right\}\right]^{v}$ |  |  |
|  | $=1-\left[F_{W}(t)\right]^{v}$ |  |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=\frac{1-\left(1-\exp \left[-\left(\frac{t+x}{\alpha}\right)^{\beta}\right]\right)^{v}}{1-\left(1-\exp \left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]\right)^{v}}$ <br> Where <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life | $u(t)=\frac{\int_{t}^{\infty}\left[1-\left(1-\exp \left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]\right)^{v}\right] d x}{1-\left(1-\exp \left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]\right)^{v}}$ |  |  |
| Hazard Rate | $h(t)=\frac{\beta v\left(t / \alpha\right)^{\beta-1}\left[1-\exp \left\{-\left(\frac{t}{} / \alpha\right)^{\beta}\right\}\right]^{v-1} \exp \left\{-\left(\frac{t}{} / \alpha\right)^{\beta}\right\}}{1-\left[1-\exp \left\{-\left(\frac{t}{} / \alpha\right)^{\beta}\right\}\right]^{v}}$ |  |  ||  | For small t: (Murthy et al. 2003, p.130) $h(t) \approx\left(\frac{\beta v}{\alpha}\right)\left(\frac{t}{\alpha}\right)^{\beta v-1}$ <br> For large t: (Murthy et al. 2003, p.130) $h(t) \approx\left(\frac{\beta}{\alpha}\right)\left(\frac{t}{\alpha}\right)^{\beta-1}$ |
| :--: | :--: |
| Properties and Moments |  |
|  | Median $\quad \alpha\left[-\ln \left\{1-2^{-1 / v}\right\}\right]^{1 / \beta}$ |
|  | For $\beta v>1$ the mode can be approximated (Murthy et al. 2003, p.130): $\alpha\left\{\frac{1}{2}\left[\frac{\sqrt{\beta\left(\beta-8 v+2 \beta v+9 \beta v^{2}\right)}}{\beta v}-1-\frac{1}{v}\right]\right\}^{v}$ |
|  | Solved numerically see Murthy et al. 2003, <br> p. 128 |
|  | $100 p \%$ Percentile Function $t_{p}=\alpha\left[-\ln \left(1-p^{1 / v}\right)\right]^{1 / \beta}$ |
| Parameter Estimation |  |
| Plotting Method (Jiang \& Murthy 1999) |  |
| Plot Points on a Weibull Probability Plot | X-Axis <br> $x=\ln (t)$ <br> Y-Axis <br> $y=\ln \left[\ln \left(\frac{1}{1-F}\right)\right]$ |
| Using the Weibull Probability Plot the parameters can be estimated. (Jiang \& Murthy 1999), provide a comprehensive coverage of this. A typical WPP for an exponentiated Weibull distribution is: |  |





**Asymptotes** (Jiang & Murthy 1999): As $x \rightarrow -\infty$ (t $\rightarrow$ 0) there exists an asymptote approximated by:$$
y \approx \beta v[x-\ln (\alpha)]
$$

As $x \rightarrow \infty(t \rightarrow \infty)$ the asymptote straight line can be approximated by:

$$
y \approx \beta[x-\ln (\alpha)]
$$

Both asymptotes intersect the $x$-axis at $\ln (\alpha)$ however both have different slopes unless $v=1$ and the WPP is the same as a two parameter Weibull distribution.

# Parameter Estimation 

Plot estimates of the asymptotes ensuring they cross the x -axis at the same point. Use the right asymptote to estimate $\alpha$ and $\beta$. Use the left asymptote to estimate $v$.

| Maximum <br> Likelihood | MLE and Bayesian techniques can be used in the standard way <br> however estimates obtained from the graphical methods are useful <br> for initial guesses when using numerical methods to solve <br> equations. A literature review of MLE and Bayesian methods is <br> covered in (Murthy et al. 2003). |
| :-- | :-- |

## Description, Limitations and Uses

Characteristics
PDF Shape: (Murthy et al. 2003, p.129)
$\boldsymbol{\beta} \boldsymbol{v}<=1$. The pdf is monotonically decreasing, $f(0)=\infty$.
$\boldsymbol{\beta} \boldsymbol{v}=\mathbf{1}$. The pdf is unimototically decreasing, $f(0)=1 / \alpha$.
$\boldsymbol{\beta} \boldsymbol{v}>1$. The pdf is unimodal. $f(0)=0$.
The pdf shape is determined by $\beta v$ in a similar way to the $\beta$ for a two parameter Weibull distribution.

Hazard Rate Shape: (Murthy et al. 2003, p.129)
$\boldsymbol{\beta} \leq \mathbf{1}$ and $\boldsymbol{\beta} \boldsymbol{v} \leq \mathbf{1}$. The hazard rate is monotonically decreasing.
$\boldsymbol{\beta} \geq \mathbf{1}$ and $\boldsymbol{\beta} \boldsymbol{v} \geq \mathbf{1}$. The hazard rate is monotonically increasing.
$\boldsymbol{\beta}<1$ and $\boldsymbol{\beta} \boldsymbol{v}>1$. The hazard rate is unimodal.
$\boldsymbol{\beta}>1$ and $\boldsymbol{\beta} \boldsymbol{v}<1$. The hazard rate is a bathtub curve.
Weibull Distribution. The Weibull distribution is a special case of the expatiated distribution when $v=1$. When $v$ is an integer greater than 1, then the cdf represents a multiplicative Weibull model.

Standard Exponentiated Weibull. (Xie et al. 2004) When $\alpha=1$ the distribution is the standard exponentiated Weibull distribution with cdf:

$$
F(t)=\left[1-\exp \left\{-t^{\beta}\right\}\right]^{v}
$$

Minimum Failure Rate. (Xie et al. 2004) When the hazard rate is a bathtub curve ( $\beta>1$ and $\beta v<1$ ) then the minimum failure rate point is:

$$
t^{\prime}=\alpha\left[-\ln \left(1-y_{1}\right)\right]^{1 / \beta}
$$|  | where $y_{1}$ is the solution to: $(\beta-1) y\left(1-y^{\nu}\right)+\beta \ln (1-y)\left[1+v y-v-y^{\nu}\right]=0$ <br> Maximum Mean Residual Life. (Xie et al. 2004) By solving the derivative of the MRL function to zero, the maximum MRL is found by solving to $t$ : $t^{*}=\alpha\left[-\ln \left(1-y_{2}\right)\right]^{1 / \beta}$ <br> where $y_{2}$ is the solution to: $\begin{gathered} \beta v(1-y) y^{\nu-1}[-\ln (1-y)]^{-1 / \beta} \\ \times \int_{[-\ln (1-y)]^{1 / \beta}}^{\infty}\left[1-\left(1-e^{-x^{\beta}}\right)^{\nu} d x-\left(1-y^{\nu}\right)^{2}=0\right. \end{gathered}$ |
| :--: | :--: |
| Resources | Books / Journals: <br> Mudholkar, G. \& Srivastava, D., 1993. Exponentiated Weibull family for analyzing bathtub failure-rate data. Reliability, IEEE Transactions on, 42(2), 299-302. <br> Jiang, R. \& Murthy, D., 1999. The exponentiated Weibull family: a graphical approach. Reliability, IEEE Transactions on, 48(1), 6872. <br> Xie, M., Goh, T.N. \& Tang, Y., 2004. On changing points of mean residual life and failure rate function for some generalized Weibull distributions. Reliability Engineering and System Safety, 84(3), 293-299. <br> Murthy, D., Xie, M. \& Jiang, R., 2003. Weibull Models 1st ed., Wiley-Interscience. <br> Rinne, H., 2008. The Weibull Distribution: A Handbook 1st ed., Chapman \& Hall/CRC. <br> Balakrishnan, N. \& Rao, C.R., 2001. Handbook of Statistics 20: Advances in Reliability 1st ed., Elsevier Science \& Technology. |
| Relationship to Other Distributions |  |
| Weibull <br> Distribution <br> Weibull $(t ; \alpha, \beta)$ | Special Case: <br> Weibull $(t ; \alpha, \beta)=$ ExpWeibull $(t ; \alpha=\alpha, \beta=\beta, v=1)$ |# 3.3. Modified Weibull Distribution 



Hazard Rate - $h(t)$




Note: The hazard rate plots are on a different scale to the PDF and CDF| Parameters \& Description |  |  |
| :--: | :--: | :--: |
| Parameters | $a$ | $a>0$ | Scale Parameter. |
|  | $b$ | $b \geq 0$ | Shape Parameter: The shape of the distribution is completely determined by b. When $0<b<1$ the distribution has a bathtub shaped hazard rate. |
|  | $\lambda$ | $\lambda \geq 0$ | Scale Parameter. |
| Limits | $t \geq 0$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)=\mathrm{a}(\mathrm{b}+\lambda \mathrm{t}) \mathrm{t}^{\mathrm{b}-1} \exp (\lambda t) \exp \left[-\mathrm{at}^{\mathrm{b}} \exp (\lambda t)\right]$ |  |  |
| CDF | $F(t)=1-\exp \left[-a t^{b} \exp (\lambda t)\right]$ |  |  |
| Reliability | $\mathrm{R}(\mathrm{t})=\exp \left[-a t^{b} \exp (\lambda t)\right]$ |  |  |
| Mean Residual Life | $u(t)=\exp \left(a t^{b} e^{\lambda t}\right) \int_{t}^{\infty} \exp \left(a x^{b} e^{\lambda t}\right) d x$ |  |  |
| Hazard Rate | $h(t)=\mathrm{a}(\mathrm{b}+\lambda \mathrm{t}) \mathrm{t}^{\mathrm{b}-1} \mathrm{e}^{\lambda \mathrm{t}}$ |  |  |
| Properties and Moments |  |  |
| Median | Solved numerically (see 100p\%) |  |  |
| Mode | Solved numerically |  |  |
| Mean - $1^{\text {st }}$ Raw Moment | Solved numerically |  |  |
| Variance - $2^{\text {nd }}$ Central Moment | Solved numerically |  |  |
| 100p\% Percentile Function | Solve for $t_{p}$ numerically: $t_{p}^{\mathrm{b}} \exp \left(\lambda \mathrm{t}_{\mathrm{p}}\right)=-\frac{\ln (1-p)}{\mathrm{a}}$ |  |  |
| Parameter Estimation |  |  |  |
| Plotting Method (Lai et al. 2003) |  |  |  |
| Plot Points on a Weibull Probability Plot | X-Axis |  | Y-Axis |
|  | $\ln \left(t_{i}\right)$ |  | $\ln \left[\ln \left(\frac{1}{1-F}\right)\right]$ |
| Using the Weibull Probability Plot the parameters can be estimated. (Lai et al. 2003). |  |  |  |
| Asymptotes (Lai et al. 2003): |  |  |  |As $x \rightarrow-\infty(t \rightarrow 0)$ the asymptote straight line can be approximated as:

$$
y \approx b x+\ln (a)
$$

As $x \rightarrow \infty(t \rightarrow \infty)$ the asymptote straight line can be approximated as (not used for parameter estimate but more for model validity):

$$
y \approx \lambda \exp (x)=\lambda t
$$

Intersections (Lai et al. 2003):
Y-Axis Intersection $\left(0, x_{0}\right)$

$$
\begin{gathered}
\ln (a)+b x_{0}+\lambda e^{x_{0}}=0 \\
\ln (a)+\lambda=y_{0}
\end{gathered}
$$

Solving these gives an approximate value for each parameter which can be used as an initial guess for numerical methods solving MLE or Bayesian methods.

A typical WPP for an Modified Weibull Distribution is:


| Description, Limitations and Uses |  |
| :-- | :-- |
| Characteristics | Parameter Characteristics:(Lai et al. 2003) <br> $\mathbf{0}<b<1$ and $\boldsymbol{\lambda}>0$. The hazard rate has a bathtub <br> curve shape. $h(t) \rightarrow \infty$ as $t \rightarrow 0 . h(t) \rightarrow \infty$ as $t \rightarrow \infty$. <br> $\boldsymbol{b} \geq \mathbf{1}$ and $\boldsymbol{\lambda}>0$. Has an increasing hazard rate function. <br> $h(0)=0 . h(t) \rightarrow \infty$ as $t \rightarrow \infty$. <br> $\boldsymbol{\lambda}=\mathbf{0}$. The function has the same form as a Weibull <br> Distribution. $h(0)=a b . h(t) \rightarrow \infty$ as $t \rightarrow \infty$ ||  | Minimum Failure Rate. (Xie et al. 2004) When the hazard rate is a bathtub curve $(0<b<1$ and $\lambda>0)$ then the minimum failure rate point is given as: $t^{*}=\frac{\sqrt{b}-b}{\lambda}$ <br> Maximum Mean Residual Life. (Xie et al. 2004) By solving the derivative of the MRL function to zero, the maximum MRL is found by solving to $t$ : $a(b+\lambda t) t^{b-1} e^{\lambda t} \int_{t}^{\infty} \exp \left(-a x^{b} e^{(\lambda x) d x}-\exp \left(a t^{b} e^{\lambda t}\right)=0\right.$ <br> Shape. The shape of the hazard rate cannot have a flat "usage period" and a strong "wear out" gradient. |
| :--: | :--: |
| Resources | Books / Journals: <br> Lai, C., Xie, M. \& Murthy, D., 2003. A modified Weibull distribution. IEEE Transactions on Reliability, 52(1), 33-37. <br> Murthy, D.N.P., Xie, M. \& Jiang, R., 2003. Weibull Models 1st ed., Wiley-Interscience. <br> Xie, M., Goh, T.N. \& Tang, Y., 2004. On changing points of mean residual life and failure rate function for some generalized Weibull distributions. Reliability Engineering and System Safety, 84(3), 293-299. <br> Rinne, H., 2008. The Weibull Distribution: A Handbook 1st ed., Chapman \& Hall/CRC. <br> Balakrishnan, N. \& Rao, C.R., 2001. Handbook of Statistics 20: Advances in Reliability 1st ed., Elsevier Science \& Technology. |
|  | Relationship to Other Distributions |
| Weibull <br> Distribution <br> Weibull $(t ; \alpha, \beta)$ | $\begin{aligned} & \text { Special Case: } \\ & \quad \text { Weibull }(t ; \alpha, \beta)=\text { ModWeibull }(t ; \mathrm{a}=\alpha, b=\beta, \lambda=0) \end{aligned}$ |# 4. Univariate Continuous Distributions# 4.1. Beta Continuous Distribution 

Probability Density Function - $f(t)$



Cumulative Density Function - $F(t)$



Hazard Rate - $h(t)$

| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\alpha$ | $\alpha>0$ | Shape Parameter. |
|  | $\beta$ | $\beta>0$ | Shape Parameter. |
|  | $a_{L}$ | $-\infty<a_{L}<b_{U}$ | Lower Bound: $a_{L}$ is the lower bound but has also been called a location parameter. In the standard Beta distribution $a_{L}=0$. |
|  | $b_{U}$ | $a_{L}<b_{U}<\infty$ | Upper Bound: $b_{U}$ is the upper bound. In the standard Beta distribution $b_{U}=1$. The scale parameter may also be defined as $b_{U}-a_{L}$. |
| Limits | $a_{L}<t \leq b_{U}$ |  |  |
| Distribution | Formulas |  |  |

$B(x, y)$ is the Beta function, $B_{t}(t \mid x, y)$ is the incomplete Beta function, $I_{t}(t \mid x, y)$ is the regularized Beta function, $\Gamma(k)$ is the complete gamma which is discussed in section 1.6.

| PDF | General Form: $f\left(t ; \alpha, \beta, a_{L}, b_{U}\right)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} \cdot \frac{\left(t-a_{L}\right)^{\alpha-1}\left(b_{U}-1\right)^{\beta-1}}{\left(b_{U}-a_{L}\right)^{\alpha+\beta-1}}$ <br> When $a_{L}=0, b_{U}=1$ : $f(t \mid \alpha, \beta)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} \cdot t^{\alpha-1}(1-t)^{\beta-1}$ $=\frac{1}{B(\alpha, \beta)} \cdot t^{\alpha-1}(1-t)^{\beta-1}$ |
| :--: | :--: |
| CDF | $\begin{aligned} \mathrm{F}(\mathrm{t}) & =\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} \int_{0}^{t} u^{\alpha-1}(1-u)^{\beta-1} d u \\ & =\frac{B_{t}(t \mid \alpha, \beta)}{B(\alpha, \beta)} \\ & =I_{t}(t \mid \alpha, \beta) \end{aligned}$ |
| Reliability | $\mathrm{R}(\mathrm{t})=1-I_{t}(t \mid \alpha, \beta)$ |
| Conditional <br> Survivor Function | $m(x)=R(x \mid t)=\frac{R(t+\mathrm{x})}{R(t)}=\frac{1-I_{t}(t+x \mid \alpha, \beta)}{1-I_{t}(t \mid \alpha, \beta)}$ <br> Where <br> $t$ is the given time we know the component has survived to. <br> $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |
| Mean Residual Life | $u(t)=\frac{\int_{0}^{\infty}\left\{B(\alpha, \beta)-B_{0}(\mathrm{x} \mid \alpha, \beta)\right\} \mathrm{dx}}{B(\alpha, \beta)-B_{t}(\mathrm{t} \mid \alpha, \beta)}$ <br> (Gupta and Nadarajah 2004, p.44) || Hazard Rate | $\begin{gathered} h(t)=\frac{\mathrm{t}^{\alpha-1}(1-\mathrm{t})}{B(\alpha, \beta)-B_{\mathrm{t}}(\mathrm{t} \mid \alpha, \beta)} \\ \text { (Gupta and Nadarajah 2004, p.44) } \end{gathered}$ |
| :--: | :--: |
| Properties and Moments |  |
| Median | Numerically solve for $t$ : $t_{\mathrm{d} . \mathrm{S}}=F^{-1}(\alpha, \beta)$ |
| Mode | $\frac{\alpha-1}{\alpha+\beta-2}$ for $\alpha>1$ and $\beta>1$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\frac{\alpha}{\alpha+\beta}$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{\alpha \beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | $\frac{2(\beta-\alpha) \sqrt{\alpha+\beta+1}}{(\alpha+\beta+2) \sqrt{\alpha \beta}}$ |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $\frac{6\left[\alpha^{3}+\alpha^{2}(1-2 \beta)+\beta^{2}(1+\beta)-2 \alpha \beta(2+\beta)\right]}{\alpha \beta(\alpha+\beta+2)(\alpha+\beta+3)}$ |
| Characteristic Function | $\begin{gathered} { }_{1} \mathrm{~F}_{1}(\alpha ; \alpha+\beta ; \text { it }) \\ \text { Where }_{1} \mathrm{~F}_{1} \text { is the confluent hypergeometric } \end{gathered}$ <br> function defined as: $\begin{aligned} & \left.{ }_{1} \mathrm{~F}_{1}(\alpha ; \beta ; \mathrm{x})=\sum_{\mathrm{k}=0}^{\infty} \frac{(\alpha)_{\mathrm{k}}}{(\beta)_{\mathrm{k}}} \frac{x^{k}}{k!} \end{aligned} \\ & \text { (Gupta and Nadarajah 2004, p.44) } \end{aligned}$ |
| 100p\% Percentile Function | Numerically solve for $t$ : $t_{\mathrm{p}}=F^{-1}(\alpha, \beta)$ |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| Likelihood <br> Functions | $\mathrm{L}(\alpha, \beta \mid \mathrm{E})=\underbrace{\frac{\Gamma(\alpha+\beta) \mathrm{n}_{\mathrm{F}}}{\Gamma(\alpha) \Gamma(\beta)} \prod_{i=1}^{n_{F}} t_{i}^{F} \alpha-1\left(1-t_{i}^{F}\right)^{\beta-1}}_{\text {failures }}$. |
| Log-Likelihood <br> Functions | $\begin{gathered} \Lambda(\alpha, \beta \mid \mathrm{E})=\mathrm{n}_{\mathrm{F}}\left[\ln \left[\Gamma(\alpha+\beta)-\ln [\Gamma(\alpha)]-\ln [\Gamma(\beta)]\right]\right. \\ +(\alpha-1) \sum_{i=1}^{n_{F}} \ln \left(t_{i}^{\mathrm{F}}\right)+(\beta-1) \sum_{i=1}^{n_{F}} \ln \left(1-t_{i}^{\mathrm{F}}\right) \end{gathered}$ |
| $\frac{\partial \Lambda}{\partial \alpha}=0$ | $\begin{gathered} \psi(\alpha)-\psi(\alpha+\beta)=\frac{1}{\mathrm{n}_{\mathrm{F}}} \sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}} \ln \left(\mathrm{t}_{\mathrm{i}}^{\mathrm{F}}\right) \\ \text { where } \psi(x)=\frac{d}{d x} \ln [\Gamma(x)] \text { is the digamma function see section 1.6.7. } \end{gathered}$ ||  | (Johnson et al. 1995, p.223) |
| :--: | :--: |
| $\frac{\partial \Lambda}{\partial \beta}=0$ | $\psi(\beta)-\psi(\alpha+\beta)=\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} \ln \left(1-t_{i}\right)$ <br> (Johnson et al. 1995, p.223) |
| Point <br> Estimates | Point estimates are obtained by using numerical methods to solve the simultaneous equations above. |
| Fisher <br> Information <br> Matrix | $I(\alpha, \beta)=\left[\begin{array}{cc}\psi^{\prime}(\alpha)-\psi^{\prime}(\alpha+\beta) & -\psi^{\prime}(\alpha+\beta) \\ -\psi^{\prime}(\alpha+\beta) & \psi^{\prime}(\beta)-\psi^{\prime}(\alpha+\beta)\end{array}\right]$ <br> where $\psi^{\prime}(x)=\frac{d^{2}}{dx^{2}} \ln \Gamma(x)=\sum_{i=0}^{\infty}(x+i)^{-2}$ is the Trigamma function. See section 1.6.8. (Yang and Berger 1998, p.5) |
| Confidence Intervals | For a large number of samples the Fisher information matrix can be used to estimate confidence intervals. See section 1.4.7. |
| Bayesian |  |
| Non-informative Priors |  |
| Jeffery's Prior | $\sqrt{\operatorname{det}(I(\alpha, \beta))}$ <br> where $I(\alpha, \beta)$ is given above. |
| Conjugate Priors |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} p \\ \text { from } \\ \text { Bernoulli }(k ; p) \end{gathered}$ | Bernoulli | $k$ failures <br> in 1 trail | Beta | $\alpha_{0}, \beta_{0}$ | $\alpha=\alpha_{o}+k$ <br> $\beta=\beta_{o}+1-k$ |
| $\begin{gathered} p \\ \text { from } \\ \operatorname{Binom}(k ; p, n) \end{gathered}$ | Binomial | $k$ failures <br> in $n$ trials | Beta | $\alpha_{o}, \beta_{o}$ | $\alpha=\alpha_{o}+k$ <br> $\beta=\beta_{o}+n-k$ |
| Description, Limitations and Uses |  |  |
| Example | For examples on the use of the beta distribution as a conjugate prior see the binomial distribution. <br> A non-homogeneous (operate in different environments) population of 5 switches have the following probabilities of failure on demand. $0.1176, \quad 0.1488, \quad 0.3684, \quad 0.8123, \quad 0.9783$ <br> Estimate the population variability function: $\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} \ln \left(\mathrm{t}_{i}^{p}\right)=-1.0549$ |$$
\frac{1}{n_{F}} \sum_{i=1}^{n_{F}} \ln \left(1-t_{i}\right)=-1.25
$$

Numerically Solving:

$$
\psi(\alpha)+1.0549=\psi(\beta)+1.25
$$

Gives:

$$
\begin{gathered}
\tilde{a}=0.7369 \\
\tilde{b}=0.6678 \\
l(\alpha, \beta)=\left[\begin{array}{cc}
1.5924 & -1.0207 \\
-1.0207 & 2.0347
\end{array}\right] \\
{\left[J_{n}(\tilde{a}, \tilde{\beta})\right]^{-1}=\left[n_{F} l(\tilde{a}, \tilde{\beta})\right]^{-1}=\left[\begin{array}{ll}
0.1851 & 0.0929 \\
0.0929 & 0.1449
\end{array}\right]}
\end{gathered}
$$

$90 \%$ confidence interval for $\alpha$ :

$$
\left[\hat{a} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.1851}}{-\tilde{a}}\right), \quad \hat{a} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.1851}}{\tilde{a}}\right)\right]
$$

$90 \%$ confidence interval for $\beta$ :

$$
\left[\hat{\beta} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.1449}}{-\tilde{\beta}}\right), \quad \hat{\beta} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{0.1449}}{\hat{\beta}}\right)\right]
$$

Characteristics
The Beta distribution was originally known as a Pearson Type I distribution (and Type II distribution which is a special case of a Type I).

Beta $(\alpha, \beta)$ is the mirror distribution of $\operatorname{Beta}(\beta, \alpha)$. If $X \sim \operatorname{Beta}(\alpha, \beta)$ and let $Y=1-X$ then $Y \sim \operatorname{Beta}(\beta, \alpha)$.

Location / Scale Parameters (NIST Section 1.3.6.6.17)
$a_{L}$ and $b_{U}$ can be transformed into a location and scale parameter:

$$
\begin{gathered}
\text { location }=a_{L} \\
\text { scale }=b_{U}-a_{L}
\end{gathered}
$$

Shapes(Gupta and Nadarajah 2004, p.41):
$\mathbf{0}<\alpha<1$. As $x \rightarrow 0, f(x) \rightarrow \infty$.
$\mathbf{0}<\beta<1$. As $x \rightarrow 1, f(x) \rightarrow \infty$.
$\boldsymbol{\alpha}>1, \boldsymbol{\beta}>1$. As $x \rightarrow 0, f(x) \rightarrow 0$. There is a single mode at $\frac{\alpha-1}{\alpha+\beta-2}$.
$\boldsymbol{\alpha}<1, \boldsymbol{\beta}<1$. The distribution is a $U$ shape. There is a single anti-mode at $\frac{\alpha-1}{\alpha+\beta-2}$.
$\boldsymbol{\alpha}>0, \boldsymbol{\beta}>0$. There exists inflection points at:

$$
\frac{\alpha-1}{\alpha+\beta-2} \pm \frac{1}{\alpha+\beta-2} \cdot \sqrt{\frac{(\alpha-1)(\beta-1)}{\alpha+\beta-3}}
$$|  | $\boldsymbol{\alpha}=\boldsymbol{\beta}$. The distribution is symmetrical about $x=0.5$. As $\alpha=\beta$ becomes large, the beta distribution approaches the normal distribution. The Standard Uniform Distribution arises when $\alpha=\beta=1$. <br> $\boldsymbol{\alpha}=\mathbf{1}, \boldsymbol{\beta}=\mathbf{2}$ or $\boldsymbol{\alpha}=\mathbf{2}, \boldsymbol{\beta}=\mathbf{1}$. Straight line. $(\boldsymbol{\alpha}-\mathbf{1})(\boldsymbol{\beta}-\mathbf{1})<0$. J Shaped. <br> Hazard Rate and MRL (Gupta and Nadarajah 2004, p.45): $\boldsymbol{\alpha} \geq \mathbf{1}, \boldsymbol{\beta} \geq \mathbf{1} . h(t)$ is increasing. $u(t)$ is decreasing. $\boldsymbol{\alpha} \leq \mathbf{1}, \boldsymbol{\beta} \leq \mathbf{1} . h(t)$ is decreasing. $u(t)$ is increasing. $\boldsymbol{\alpha}>1,0<\beta<1 . h(t)$ is bathtub shaped and $u(t)$ is an upside down bathtub shape. $\mathbf{0}<\alpha<1, \boldsymbol{\beta}>1 . h(t)$ is upside down bathtub shaped and $u(t)$ is bathtub shape. |
| :--: | :--: |
| Applications | Parameter Model. The Beta distribution is often used to model parameters which are constrained to take place between an interval. In particular the distribution of a probability parameter $0 \leq p \leq 1$ is popular with the Beta distribution. <br> Bayesian Analysis. The Beta distribution is often used as a conjugate prior in Bayesian analysis for the Bernoulli, Binomial and Geometric Distributions to produce closed form posteriors. The $\operatorname{Beta}(0,0)$ distribution is an improper prior sometimes used to represent ignorance of parameter values. The $\operatorname{Beta}(1,1)$ is a standard uniform distribution which may be used as a noninformative prior. When used as a conjugate prior to a Bernoulli or Binomial process the parameter $\alpha$ may represent the number of successes and $\beta$ the total number of failures with the total number of trials being $n=\alpha+\beta$. <br> Proportions. Used to model proportions. An example of this is the likelihood ratios for estimating uncertainty. |
| Resources | Online: <br> http://mathworld.wolfram.com/BetaDistribution.html <br> http://en.wikipedia.org/wiki/Beta_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (interactive web calculator) <br> http://www.itl.nist.gov/div898/handbook/eda/section3/eda366h.htm <br> Books: <br> Gupta, A.K. \& Nadarajah, S., 2004. Handbook of beta distribution and its applications, CRC Press. <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1995. Continuous Univariate Distributions, Vol. 2 2nd ed., Wiley-Interscience. |
| Relationship to Other Distributions |  || Chi-square <br> Distribution $\chi^{2}(t ; v)$ | Let $\mathrm{X}_{\mathrm{i}} \sim \chi^{2}\left(v_{i}\right) \quad$ and $\quad \mathrm{Y}=\frac{\mathrm{X}_{1}}{\mathrm{X}_{1}+\mathrm{X}_{2}}$ <br> Then $\quad \mathrm{Y} \sim \operatorname{Beta}\left(\alpha=\frac{1}{2} v_{1}, \beta=\frac{1}{2} v_{2}\right)$ |
| :--: | :--: |
| Uniform <br> Distribution $\operatorname{Unif}(t ; a, b)$ | Let $\mathrm{X}_{\mathrm{i}} \sim \operatorname{Unif}(0,1) \quad$ and $\quad \mathrm{X}_{1} \leq \mathrm{X}_{2} \leq \cdots \leq \mathrm{X}_{n}$ <br> Then $\quad \mathrm{X}_{r} \sim \operatorname{Beta}(r, n-r+1)$ <br> Where $n$ and $r$ are integers. <br> Special Case: $\quad \operatorname{Beta}(t ; 1,1, a, b)=\operatorname{Unif}(t ; a, b)$ |
| Normal <br> Distribution $\operatorname{Norm}(t ; \mu, \sigma)$ | For large $\alpha$ and $\beta$ with fixed $\alpha / \beta$ : $\operatorname{Beta}(\alpha, \beta) \approx \operatorname{Norm}\left(\mu=\frac{\alpha}{\alpha+\beta}, \sigma=\sqrt{\frac{\alpha \beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}}\right)$ <br> As $\alpha$ and $\beta$ increase the mean remains constant and the variance is reduced. |
| ```Gamma Distribution Gamma(t; k, \lambda)``` | Let $\begin{aligned} & X_{1}, X_{2} \sim \operatorname{Gamma}\left(\mathrm{k}_{\mathrm{i}}, \lambda_{\mathrm{i}}\right) \quad \text { and } \quad \mathrm{Y}=\frac{\mathrm{X}_{1}}{\mathrm{X}_{1}+\mathrm{X}_{2}} \\ & \text { Then } \quad \mathrm{Y} \sim \operatorname{Beta}\left(\alpha=k_{1}, \beta=k_{2}\right) \end{aligned}$ |
| Dirichlet <br> Distribution $\operatorname{Dir}_{d}(x ; \boldsymbol{\alpha})$ | Special Case: <br> $\operatorname{Dir}_{d=1}\left(\mathrm{x} ;\left[\alpha_{1}, \alpha_{0}\right]\right)=\operatorname{Beta}\left(k=x ; \alpha=\alpha_{1}, \beta=\alpha_{0}\right)$ |# 4.2. Birnbaum Saunders Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\beta$ | $\beta>0$ | Scale parameter. $\beta$ is the scale parameter equal to the median. |
|  | $\alpha$ | $\alpha>0$ | Shape parameter. |
| Limits | $0<\mathrm{t}<\infty$ |  |  |
| Distribution | Formulas |  |  |
| PDF |  | $\begin{aligned} f(t) & =\frac{\sqrt{t / \beta}+\sqrt{\beta / t}}{2 \alpha t \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(\frac{\sqrt{t / \beta}-\sqrt{\beta / t}}{\alpha}\right)^{2}\right] \\ & =\frac{\sqrt{t / \beta}+\sqrt{\beta / t}}{2 \alpha t} \phi(z) \end{aligned}$ <br> where $\phi(z)$ is the standard normal pdf and: $z_{B S}=\frac{\sqrt{t / \beta}-\sqrt{\beta / t}}{\alpha}$ |  |
| CDF |  | $\begin{aligned} F(t) & =\Phi\left(\frac{\sqrt{t / \beta}-\sqrt{\beta / t}}{\alpha}\right) \\ & =\Phi\left(z_{B S}\right) \end{aligned}$ |  |
| Reliability |  | $\begin{aligned} \mathrm{R}(\mathrm{t}) & =\Phi\left(\frac{\sqrt{\beta / t}-\sqrt{\mathrm{t} / \beta}}{\alpha}\right) \\ & =\Phi\left(-z_{B S}\right) \end{aligned}$ |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ |  | $\begin{gathered} m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=\frac{\Phi\left(-z_{B S}^{\prime}\right)}{\Phi\left(-z_{B S}\right)} \\ z_{B S}=\frac{\sqrt{t / \beta}-\sqrt{\beta / t}}{\alpha}, \quad z_{B S}^{\prime}=\frac{\sqrt{(t+x) / \beta}-\sqrt{\beta /(t+x)}}{\alpha} \end{gathered}$ <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |
| Mean Residual Life |  | $u(t)=\frac{\int_{t}^{\infty} \Phi\left(-z_{B S}\right) d x}{\Phi\left(-z_{B S}\right)}$ |  |
| Hazard Rate |  | $h(t)=\frac{\sqrt{t / \beta}+\sqrt{\beta / t}}{2 \alpha t}\left[\frac{\Phi\left(z_{B S}\right)}{\Phi\left(-z_{B S}\right)}\right]$ |  |
| Cumulative Hazard Rate |  | $H(t)=-\ln \left[\Phi\left(-z_{B S}\right)\right]$ |  || Properties and Moments |  |
| :--: | :--: |
| Median | $\beta$ |
| Mode | Numerically solve for $t$ : $t^{3}+\beta\left(1+\alpha^{2}\right) t^{2}+\beta^{2}\left(3 \alpha^{2}-1\right) t-\beta^{3}=0$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\beta\left(1+\frac{\alpha^{2}}{2}\right)$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\alpha^{2} \beta^{2}\left(1+\frac{5 \alpha^{2}}{4}\right)$ |
| Skewness - $3^{\text {rd }}$ Central Moment | $\frac{4 \alpha\left(11 \alpha^{2}+6\right)}{\left(5 \alpha^{2}+4\right)^{\frac{3}{2}}}$ <br> (Lemonte et al. 2007) |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $3+\frac{6 \alpha^{2}\left(93 \alpha^{2}+40\right)}{\left(5 \alpha^{2}+4\right)^{2}}$ <br> (Lemonte et al. 2007) |
| $100 \gamma \%$ Percentile Function | $t_{\gamma}=\frac{\beta}{4}\left\{\alpha \Phi^{-1}(\gamma)+\sqrt{4+\left[\alpha \Phi^{-1}(\gamma)\right]^{2}}\right\}^{2}$ |
| Parameter Estimation |  |

# Maximum Likelihood Function 

| Likelihood <br> Function | For complete data: $L(\theta, \alpha \mid E)=\underbrace{\prod_{i=1}^{n_{F}}\left[\frac{\sqrt{t_{i} / \beta}+\sqrt{\beta / t_{i}}}{2 \alpha t_{i} \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(\frac{\sqrt{t_{i} / \beta}-\sqrt{\beta / t_{i}}}{\alpha}\right)^{2}\right]\right.}_{\text {failures }}$ |
| :--: | :--: |
| Log-Likelihood Function | $\Lambda(\alpha, \beta \mid E)=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln (\alpha \beta)+\sum_{i=1}^{n_{F}} \ln \left[\left(\frac{\beta}{t_{i}}\right)^{\frac{3}{2}}+\left(\frac{\beta}{t_{i}}\right)^{\frac{3}{2}}\right]}_{$| failures |
| $\frac{\partial \Lambda}{\partial \alpha}=0$ | $\frac{\partial \Lambda}{\partial \alpha}=\underbrace{-\frac{\mathrm{n}_{\mathrm{F}}}{\alpha}\left(1+\frac{2}{\alpha^{2}}\right)+\frac{1}{\alpha^{3} \beta} \sum_{i=1}^{n_{F}} t_{i}+\frac{\beta}{\alpha^{2}} \sum_{i=1}^{n_{F}} \frac{1}{t_{i}}}_{\text failures }=0$ |
| $\frac{\partial \Lambda}{\partial \beta}=0$ | $\frac{\partial \Lambda}{\partial \beta}=\underbrace{-\frac{\mathrm{n}_{\mathrm{F}}}{2 \beta}+\sum_{i=1}^{n_{F}} \frac{1}{t_{i}+\beta}+\frac{1}{2 \alpha^{2} \beta^{2}} \sum_{i=1}^{n_{F}} t_{i}-\frac{1}{2 \alpha^{2}} \sum_{i=1}^{n_{F}} \frac{1}{t_{i}}=0}_{\text failures }$ |
| MLE Point | $\hat{\beta}$ is found by solving: || Estimates | $\beta^{2}-\beta[2 R+g(\beta)]+R[S+g(\beta)]=0$ <br> where $\begin{gathered} g(\beta)=\left[\frac{1}{n} \sum_{i=1}^{n_{p}} \frac{1}{\beta+t_{i}}\right]^{-1}, \quad S=\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} t_{i}, \quad R=\left(\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} \frac{1}{t_{i}}\right)^{-1} \end{gathered}$ <br> Point estimates for $\bar{a}$ is: $\begin{gathered} \bar{a}=\sqrt{\frac{S}{\bar{\beta}}+\frac{\hat{\beta}}{R}-2} \end{gathered}$ <br> (Lemonte et al. 2007) |  |
| :--: | :--: | :--: |
| Fisher Information | $\begin{gathered} I(\theta, \alpha)=\left[\begin{array}{cc} \frac{2}{\alpha^{2}} & 0 \\ 0 & \frac{\alpha(2 \pi)^{-1 / 2} k(\alpha)+1}{\alpha^{2} \beta^{2}} \end{array}\right] \end{gathered}$ <br> where $\begin{gathered} k(\alpha)=\alpha \sqrt{\frac{\pi}{2}}-\pi \exp \left\{\frac{2}{\alpha^{2}}\right\}\left[1-\Phi\left(\frac{2}{\alpha}\right)\right] \end{gathered}$ <br> (Lemonte et al. 2007) |  |
| $100 y \%$ <br> Confidence <br> Intervals | Calculated from the Fisher information matrix. See section 1.4.7. For a literature review of proposed confidence intervals see (Lemonte et al. 2007). |  |
| Description, Limitations and Uses |  |  |
| Example | 5 components are put on a test with the following failure times: $98,116,2485,2526, ., 2920$ hours $\begin{gathered} S=\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} t_{i}=1629 \\ R=\left(\frac{1}{n_{p}} \sum_{i=1}^{n_{p}} \frac{1}{t_{i}}\right)^{-1}=250.432 \end{gathered}$ <br> Solving: $\begin{gathered} \beta^{2}-\beta\left(2 R+\left[\frac{1}{n} \sum_{i=1}^{n_{p}} \frac{1}{\beta+t_{i}}\right]^{-1}\right)+R\left\{S+\left[\frac{1}{n} \sum_{i=1}^{n_{p}} \frac{1}{\beta+t_{i}}\right]^{-1}\right\}=0 \\ \bar{\beta}=601.949 \\ \bar{a}=\sqrt{\frac{S}{\bar{\beta}}+\frac{\hat{\beta}}{R}-2}=1.763 \end{gathered}$ |  ||  | $90 \%$ confidence interval for $\alpha$ : $\left[\tilde{a} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{\frac{\alpha^{2}}{2 n_{F}}}}{-\tilde{a}}\right\}, \quad \tilde{a} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{\frac{\alpha^{2}}{2 n_{F}}}}{\tilde{a}}\right\}\right]$ |
| :--: | :--: |
|  | $\left[\begin{array}{ll}1.048, & 2.966\end{array}\right]$ |
|  | $90 \%$ confidence interval for $\beta$ : $\left.k(\tilde{a})=\tilde{a} \sqrt{\frac{\pi}{2}}-\pi \exp \left\{\frac{2}{\tilde{a}^{2}}\right\}\left[1-\Phi\left(\frac{2}{\tilde{a}}\right)\right]=1.442\right.$ |
|  | $I_{\beta \beta}=\frac{\tilde{a}(2 \pi)^{-1 / 2} k(\tilde{a})+1}{\tilde{a}^{2} \tilde{\beta}^{2}}=10.335 E-6$ |
|  | $\left[\tilde{\beta} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{\frac{96762}{n_{F}}}}{-\tilde{\beta}}\right\}, \quad \tilde{\beta} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{\frac{96762}{n_{F}}}}{-\tilde{\beta}}\right\}\right]$ |
|  | $\left[\begin{array}{lll}100.4, & 624.5\end{array}\right]$ |
|  | Note that this confidence interval uses the assumption of the parameters being normally distributed which is only true for large sample sizes. Therefore these confidence intervals may be inaccurate. Bayesian methods must be done numerically. |
| Characteristics | The Birnbaum-Saunders distribution is a stochastic model of the Miner's rule. <br> Characteristic of $\boldsymbol{\alpha}$. As $\alpha$ decreases the distribution becomes more symmetrical around the value of $\beta$. <br> Hazard Rate. The hazard rate is always unimodal. The hazard rate has the following asymptotes: (Meeker \& Escobar 1998, p.107) $h(0)=0$ $\lim _{t \rightarrow \infty} h(t)=\frac{1}{2 \beta \alpha^{2}}$ <br> The change point of the unimodal hazard rate for $\alpha<0.6$ must be solved numerically, however for $\alpha>0.6$ can be approximated using: (Kundu et al. 2008) $\begin{aligned} & t_{c}=\frac{\beta}{(-0.4604+1.8417 \alpha)^{2}} \\ & \hline \end{aligned}$ <br> Lognormal and Inverse Gaussian Distribution. The shape and behavior of the Birnbaum-Saunders distribution is similar to that of the lognormal and inverse Gaussian distribution. This similarity is seen primarily in the center of the distributions. (Meeker \& Escobar 1998, p.107) <br> Let: $\begin{gathered} T \sim B S(t ; \alpha, \beta) \end{gathered}$ ||  | Scaling property (Meeker \& Escobar 1998, p.107) $c T \sim B S(t ; \alpha, c \beta)$ <br> where $c>0$ <br> Inverse property (Meeker \& Escobar 1998, p.107) $\frac{1}{T} \sim B S\left(t ; \alpha, \frac{1}{\beta}\right)$ |
| :--: | :--: |
| Applications | Fatigue-Fracture. The distribution has been designed to model crack growth to critical crack size. The model uses the Miner's rule which allows for non-constant fatigue cycles through accumulated damage. The assumption is that the crack growth during any one cycle is independent of the growth during any other cycle. The growth for each cycle has the same distribution from cycle to cycle. This is different from the proportional degradation model used to derive the log normal distribution model, with the rate of degradation being dependent on accumulated damage. (http://www.itl.nist.gov/div898/handbook/apr/section1/apr166.htm) |
| Resources | Online: <br> http://www.itl.nist.gov/div898/handbook/eda/section3/eda366a.htm http://www.itl.nist.gov/div898/handbook/apr/section1/apr166.htm http://en.wikipedia.org/wiki/Birnbaum\�\�\�Saunders_distrib ution <br> Books: <br> Birnbaum, Z.W. \& Saunders, S.C., 1969. A New Family of Life Distributions. Journal of Applied Probability, 6(2), 319-327. <br> Lemonte, A.J., Cribari-Neto, F. \& Vasconcellos, K.L., 2007. Improved statistical inference for the two-parameter BirnbaumSaunders distribution. Computational Statistics \& Data Analysis, 51(9), 4656-4681. <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1995. Continuous Univariate Distributions, Vol. 2, 2nd ed., Wiley-Interscience. <br> Rausand, M. \& Høyland, A., 2004. System reliability theory, WileyIEEE. |# 4.3. Gamma Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\lambda$ | $\lambda>0$ | Scale Parameter: Equal to the rate (frequency) of events/shocks. Sometimes defined as $1 / \theta$ where $\theta$ is the average time between events/shocks. |
|  | $k$ | $k>0$ | Shape Parameter: As an integer $k$ can be interpreted as the number of events/shocks until failure. When not restricted to an integer, $k$ and be interpreted as a measure of the ability to resist shocks. |
| Limits | $t \geq 0$ |  |  |
| Distribution | When k is an integer (Erlang distribution) |  | When $k$ is continuous |
| $\Gamma(k)$ is the complete gamma function. $\Gamma(k, t)$ and $\gamma(k, t)$ are the incomplete gamma functions see section 1.6 . |  |  |  |
| PDF | $f(t)=\frac{\lambda^{k} t^{k-1}}{(k-1)!} e^{-\lambda t}$ |  | $f(t)=\frac{\lambda^{k} t^{k-1}}{\Gamma(k)} e^{-\lambda t}$ <br> with Laplace transformation: $f(s)=\left(\frac{\lambda}{\lambda+s}\right)^{k}$ |
| CDF | $F(t)=1-e^{-\lambda t} \sum_{n=0}^{k-1} \frac{(\lambda t)^{n}}{n!}$ |  | $\begin{aligned} & F(t)=\frac{\gamma(k, \lambda t)}{\Gamma(k)} \\ & =\frac{1}{\Gamma(k)} \int_{0}^{\lambda t} x^{k-1} e^{-x} d x \end{aligned}$ |
| Reliability | $R(t)=e^{-\lambda t} \sum_{n=0}^{k-1} \frac{(\lambda t)^{n}}{n!}$ |  | $\begin{aligned} & R(t)=\frac{\Gamma(k, \lambda t)}{\Gamma(k)} \\ & =\frac{1}{\Gamma(k)} \int_{\lambda t}^{\infty} x^{k-1} e^{-x} d x \end{aligned}$ |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $e^{-\lambda s} \frac{\sum_{n=0}^{k-1}\frac{[\lambda(t+x)]^{n}}{n!}}{\sum_{n=0}^{k-1} \frac{(\lambda t)^{n}}{n!}}$ |  | $m(x)=\frac{R(t+x)}{R(t)}=\frac{\Gamma(k, \lambda t+\lambda x)}{\Gamma(k, \lambda t)}$ |
|  | Where $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life | $u(t)=\frac{\int_{t}^{\infty} R(x) d x}{R(t)}$ |  | $u(t)=\frac{\int_{t}^{\infty} \Gamma(k, \lambda x) d x}{\Gamma(k, \lambda t)}$ |
|  | The mean residual life does not have a closed form but has the |  |  ||  | expansion: <br> Where $O\left(t^{-3}\right)$ is Landau's notation. (Kleiber \& Kotz 2003, p.161) |
| :--: | :--: |
| Hazard Rate | $h(t)=\frac{\lambda^{k} t^{k-1}}{\Gamma(k) \sum_{n=0}^{k-1} \frac{(\lambda t)^{n}}{n!}} \quad h(t)=\frac{\lambda^{k} t^{k-1}}{\Gamma(k, \lambda t)} e^{-\lambda t}$ <br> Series expansion of the hazard rate is: (Kleiber \& Kotz 2003, p.161) <br> Limits of $h(t)$ (Rausand \& Heyland 2004) <br> Cumulative <br> Hazard Rate $\quad H(t)=\lambda t-\ln \left[\sum_{n=0}^{k-1} \frac{(\lambda t)^{n}}{n!}\right]$ 

$$
\begin{aligned}
& h(t)=-\ln \left[\frac{\Gamma(k, \lambda t)}{\Gamma(k)}\right]
\end{aligned}
$$

Properties and Moments

| Median | Numerically solve for $t$ when: $t_{0.5}=F^{-1}(0.5 ; k, \lambda)$ <br> or $\quad \gamma(\mathrm{k}, \lambda \mathrm{t})=\Gamma(\mathrm{k}, \lambda \mathrm{t})$ <br> where $\gamma(\mathrm{k}, \lambda \mathrm{t})$ is the lower incomplete gamma function, see section 1.6.6. |
| :--: | :--: |
| Mode | $\begin{gathered} \frac{k-1}{\lambda} \text { for } k \geq 1 \\ \text { No mode for } 0<k<1 \end{gathered}$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\frac{\mathrm{k}}{\lambda}$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{\mathrm{k}}{\lambda^{2}}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | $2 / \sqrt{k}$ |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $6 / k$ |
| Characteristic Function | $\left(1-\frac{\mathrm{it}}{\lambda}\right)^{-\mathrm{k}}$ || $100 \alpha \%$ Percentile Function |  | Numerically solve for $t$ : $t_{\alpha}=F^{-1}(\alpha ; k, \lambda)$ |
| :--: | :--: | :--: |
| Parameter Estimation |  |  |
| Maximum Likelihood Function |  |  |
| Likelihood Functions |  | $L(k, \lambda \mid E)=\underbrace{\frac{\lambda^{k n_{F}}}{\Gamma(k)^{n_{F}}} \prod_{i=1}^{n_{F}} t_{i}{ }^{k-1} \mathrm{e}^{-\lambda t_{i}}}_{\text {failures }}$ |
| Log-Likelihood Functions |  | $\Lambda(k, \lambda \mid E)=k n_{F} \ln (\lambda)-n_{F} \ln (\Gamma(k))+(\mathrm{k}-1) \sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}} \ln \left(\mathrm{t}_{\mathrm{i}}\right)-\lambda \sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}} \mathrm{t}_{\mathrm{i}}$ |
| $\frac{\partial \Lambda}{\partial \mathrm{k}}=0$ |  | $0=n_{F} \ln (\lambda)-n_{F} \psi(k)+\sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}}\left\{\ln \left(\mathrm{t}_{\mathrm{i}}\right)\right\}$ <br> where $\psi(x)=\frac{d}{d x} \ln [\Gamma(x)]$ is the digamma function see section 1.6.7. |
| $\frac{\partial \Lambda}{\partial \lambda}=0$ |  | $0=\frac{k n_{F}}{\lambda}-\sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}} \mathrm{t}_{\mathrm{i}}$ |
| Point Estimates |  | Point estimates for $\hat{k}$ and $\hat{\lambda}$ are obtained by using numerical methods to solve the simultaneous equations above. (Kleiber \& Kotz 2003, p.165) |
| Fisher Information Matrix |  | $I(k, \lambda)=\left[\begin{array}{cc}\psi^{\prime}(k) & \lambda \\ \lambda & k \lambda^{2}\end{array}\right]$ <br> where $\psi^{\prime}(x)=\frac{\mathrm{d}^{2}}{d x^{2}} \ln \Gamma(x)=\sum_{i=0}^{\infty}(x+i)^{-2}$ is the Trigamma function. (Yang and Berger 1998, p.10) |
| Confidence Intervals |  | For a large number of samples the Fisher information matrix can be used to estimate confidence intervals. |
| Bayesian |  |  |
| Non-informative Priors, $\pi(k, \lambda)$ (Yang and Berger 1998, p.6) |  |  |
| Type | Prior | Posterior |
| Uniform Improper Prior with limits: $\begin{aligned} & \lambda \in(0, \infty) \\ & k \in(0, \infty) \end{aligned}$ | 1 | No Closed Form |
| Jeffrey's Prior | $\lambda \sqrt{k \cdot \psi^{\prime}(k)-1}$ | No Closed Form |
| Reference Order: $\quad\{k, \lambda\}$ | $\lambda \sqrt{k \cdot \psi^{\prime}(k)-\frac{1}{\alpha}}$ | No Closed Form || Reference <br> Order: <br> $\{\lambda, k\}$ | $\lambda \sqrt{\psi^{\prime}(k)}$ |  | No Closed Form |  |
| :--: | :--: | :--: | :--: | :--: |
| where $\psi^{\prime}(x)=\frac{d^{2}}{d x^{2}} \ln \Gamma(x)=\sum_{i=0}^{\infty}(x+i)^{-2}$ is the Trigamma function |  |  |  |  |
| Conjugate Priors |  |  |  |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \Lambda \\ \text { from } \\ \operatorname{Exp}(t ; \Lambda) \end{gathered}$ | Exponential | $n_{F}$ <br> failures in $t_{T}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{aligned} & k=k_{o}+n_{F} \\ & \lambda=\lambda_{o}+t_{T} \end{aligned}$ |
| $\begin{gathered} \Lambda \\ \text { from } \\ \text { Pois }(k ; \Lambda t) \end{gathered}$ | Poisson | $n_{F}$ <br> failures in $t_{T}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{aligned} & k=k_{o}+n_{F} \\ & \lambda=\lambda_{o}+t_{T} \end{aligned}$ |
| $\begin{gathered} \lambda \\ \text { where } \\ \lambda=\alpha^{-\beta} \\ \text { from } \\ W b l(t ; \alpha, \beta) \end{gathered}$ | Weibull with known $\beta$ | $n_{F}$ <br> failures at times $t_{i}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{gathered} k=k_{o}+n_{F} \\ \lambda=\lambda_{o}+\sum_{i=1}^{n_{F}} t_{i}^{\beta} \\ \text { (Rinne 2008, p.520) } \end{gathered}$ |
| $\begin{gathered} \sigma^{2} \\ \text { from } \\ \operatorname{Norm}\left(x ; \mu, \sigma^{2}\right) \end{gathered}$ | Normal with known $\mu$ | $n_{F}$ <br> failures at times $t_{i}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{gathered} k=k_{o}+n_{F} / 2 \\ \lambda=\lambda_{o}+\frac{1}{2} \sum_{i=1}^{n}\left(t_{i}-\mu\right)^{2} \end{gathered}$ |
| $\begin{gathered} \lambda \\ \text { from } \\ \operatorname{Gamma}(x ; \lambda, k) \end{gathered}$ | Gamma with known $k=k_{E}$ | $n_{F}$ <br> failures in $t_{T}$ | Gamma | $\eta_{0}, \Lambda_{0}$ | $\begin{gathered} \eta=\eta_{0}+n_{F} k_{E} \\ \Lambda=\Lambda_{o}+t_{T} \end{gathered}$ |
| $\begin{gathered} \alpha \\ \text { from } \\ \operatorname{Perato}(t ; \theta, \alpha) \end{gathered}$ | Pareto with known $\theta$ | $n_{F}$ <br> failures at times $t_{i}$ | Gamma | $\mathrm{k}_{0}, \lambda_{0}$ | $\begin{gathered} \mathrm{k}=\mathrm{k}_{0}+n_{F} \\ \lambda=\lambda_{o}+\sum_{i=1}^{n_{F}} \ln \left(\frac{x_{i}}{\theta}\right) \end{gathered}$ |
| where: $t_{T}=\sum \mathrm{t}_{1}^{\mathrm{F}}+\sum \mathrm{t}_{1}^{\mathrm{S}}=$ total time in test |  |  |  |  |  |
| Description, Limitations and Uses |  |  |  |  |  |
| Example 1 |  | For an example using the gamma distribution as a conjugate prior see the Poisson or Exponential distributions.A renewal process has an exponential time between failure with parameter $\lambda=0.01$ under the homogeneous Poisson process conditions. What is the probability the forth failure will occur before 200 hours. $F(200 ; 4,0.01)=0.1429$ |  |  |  |
| Example 2 |  | 5 components are put on a test with the following failure times: $38,42,44,46,55$ hours |  |  |  ||  | Solving: $0=\frac{5 k}{\lambda}-225$ <br> Gives: $\begin{gathered} 0=5 \ln (\lambda)-5 \psi(k)+18.9954 \\ \tilde{k}=21.377 \\ \hat{\lambda}=0.4749 \end{gathered}$ <br> 90\% confidence interval for $k$ : $I(k, \lambda)=\left\{\begin{array}{ll}0.0479 & 0.4749 \\ 0.4749 & 4.8205\end{array}\right\}$ <br> $\left[J_{n}(\hat{k}, \hat{\lambda})\right]^{-1}=\left[n_{F} I(\hat{k}, \hat{\lambda})\right]^{-1}=\left\{\begin{array}{ll}179.979 & -17.730 \\ -17.730 & 1.7881\end{array}\right\}$ <br> $\left.\left[\hat{k} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{179.979}}{-\hat{k}}\right\}}{[7.6142,}\right., \quad \hat{k} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{179.979}}{\hat{k}}\right\}\right]$ <br> 90\% confidence interval for $\lambda$ : $\left.\left[\hat{\lambda} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{1.7881}}{-\hat{\lambda}}\right\}}{[0.0046,}\right.\right.$ <br> Note that this confidence interval uses the assumption of the parameters being normally distributed which is only true for large sample sizes. Therefore these confidence intervals may be inaccurate. Bayesian methods must be done numerically. |
| :--: | :--: |
| Characteristics | The gamma distribution was originally known as a Pearson Type III distribution. This distribution includes a location parameter $\gamma$ which shifts the distribution along the $x$-axis. $f(t ; k, \lambda, \gamma)=\frac{\lambda^{k}(t-\gamma)^{k-1}}{\Gamma(k)} \mathrm{e}^{-\lambda(t-\gamma)}$ <br> When k is an integer, the Gamma distribution is called an Erlang distribution. <br> k Characteristics: $\boldsymbol{k}<1 . \quad f(0)=\infty$. There is no mode. $\boldsymbol{k}=1 . \quad f(0)=\lambda$. The gamma distribution reduces to an exponential distribution with failure rate $\lambda$. Mode at $t=0$. $\boldsymbol{k}>1 . \quad f(0)=0$ <br> Large $\boldsymbol{k}$. The gamma distribution approaches a normal distribution with $\mu=\frac{k}{\lambda}, \sigma=\sqrt{\frac{k}{\lambda^{2}}}$. |Homogeneous Poisson Process (HPP). Components with an exponential time to failure which undergo instantaneous renewal with an identical item undergo a HPP. The Gamma distribution is probability distribution of the $\mathrm{k}^{\text {th }}$ failed item and is derived from the convolution of $k$ exponentially distributed random variables, $T_{i}$. (See related distributions, exponential distribution).

$$
T \sim \operatorname{Gamma}(k, \lambda)
$$

Scaling property:

$$
a T \sim \operatorname{Gamma}\left(k, \frac{\lambda}{a}\right)
$$

# Convolution property: 

$$
T_{1}+T_{2}+\ldots+T_{n} \sim \operatorname{Gamma}\left(\sum k_{i}, \lambda\right)
$$

Where $\lambda$ is fixed.
Properties from (Leemis \& McQueston 2008)

Applications

## Renewal Theory, Homogenous Poisson Process. Used to model

a renewal process where the component time to failure is exponentially distributed and the component is replaced instantaneously with a new identical component. The HPP can also be used to model ruin theory (used in risk assessments) and queuing theory.

System Failure. Can be used to model system failure with $k$ backup systems.

Life Distribution. The gamma distribution is flexible in shape and can give good approximations to life data.

Bayesian Analysis. The gamma distribution is often used as a prior in Bayesian analysis to produce closed form posteriors.

| Resources | Online: |
| :-- | :-- |
|  | http://mathworld.wolfram.com/GammaDistribution.html |
|  | http://en.wikipedia.org/wiki/Gamma_distribution |
|  | http://socr.ucla.edu/htmls/SOCR_Distributions.html (interactive web |
|  | calculator) |
|  | http://www.itl.nist.gov/div898/handbook/eda/section3/eda366b.htm |
|  | Books: |
|  | Artin, E., 1964. The Gamma Function, New York: Holt, Rinehart \& |
|  | Winston. |
|  | Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1994. Continuous |
|  | Univariate Distributions, Vol. 1 2nd ed., Wiley-Interscience. |
|  | Bowman, K.O. \& Shenton, L.R., 1988. Properties of estimators for |
|  | the gamma distribution, CRC Press. || Relationship to Other Distributions |  |
| :--: | :--: |
| Generalized <br> Gamma <br> Distribution <br> Gamma $(t ; k, \lambda, \gamma, \xi)$ | $\left.\begin{array}{c} f(t ; k, \lambda, \gamma, \xi)=\frac{\xi \lambda^{\xi k}(t-\gamma)^{\xi k-1}}{\Gamma(k)} \exp \left\{-[\lambda(t-\gamma)]^{k}\right\} \\ \lambda \text { - Scale Parameter } \\ k \text { - Shape Parameter } \\ \gamma \text { - Location parameter } \\ \xi \text { - Second shape parameter } \end{array}\right.$ <br> The generalized gamma distribution has been derived because it is a generalization of a large amount of probability distributions. Such as: $\begin{aligned} & \operatorname{Gamma}(t ; 1, \lambda, 0,1)=\operatorname{Exp}(t ; \lambda) \\ & \operatorname{Gamma}\left(t ; 1, \frac{1}{\mu}, \beta, 1\right)=\operatorname{Exp}(t ; \mu, \beta) \\ & \operatorname{Gamma}\left(t ; 1, \frac{1}{\alpha}, 0, \beta\right)=\operatorname{Weibull}(t ; \alpha, \beta) \\ & \operatorname{Gamma}\left(t ; 1, \frac{1}{\alpha}, \gamma, \beta\right)=\operatorname{Weibull}(t ; \alpha, \beta, \gamma) \\ & \operatorname{Gamma}\left(t ; \frac{n}{2}, \frac{1}{2}, 0,1\right)=\chi^{2}(\mathrm{t} ; \mathrm{n}) \\ & \operatorname{Gamma}\left(t ; \frac{n}{2}, \frac{1}{\sqrt{2}}, 0,2\right)=\chi(\mathrm{t} ; \mathrm{n}) \\ & \operatorname{Gamma}\left(t ; 1, \frac{1}{\sigma}, 0,2\right)=\operatorname{Rayleigh}(\mathrm{t} ; \sigma)\end{aligned}$ |
| Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let $\quad T_{1} \ldots T_{k} \sim \operatorname{Exp}(\lambda) \quad$ and $\quad T_{t}=T_{1}+T_{2}+\cdots+T_{k}$ <br> Then $\quad T_{t} \sim \operatorname{Gamma}(k, \lambda)$ <br> This is gives the Gamma distribution its convolution property. <br> Special Case: $\quad \operatorname{Exp}(t ; \lambda)=\operatorname{Gamma}(t ; k=1, \lambda)$ |
| Poisson <br> Distribution $\operatorname{Pois}(k ; \lambda t)$ | Let $\quad T_{1} \ldots T_{k} \sim \operatorname{Exp}(\lambda) \quad$ and $\quad T_{t}=T_{1}+T_{2}+\cdots+T_{k}$ <br> $T_{t} \sim \operatorname{Gamma}(k, \lambda)$ <br> The Poisson distribution is the probability that exactly $k$ failures have been observed in time $t$. This is the probability that $t$ is between $T_{k}$ and $T_{k+1}$. $\begin{aligned} & f_{\text {Poisson }}(k ; \lambda t)=\int_{k}^{k+1} f_{\text {Gamma }}(t ; x, \lambda) d x \\ & =F_{\text {Gamma }}(t ; k+1, \lambda)-F_{\text {Gamma }}(t ; k, \lambda)\end{aligned}$ ||  | where $k$ is an integer. |
| :--: | :--: |
| Normal Distribution $\operatorname{Norm}(t ; \mu, \sigma)$ | Special Case for large k: $\lim _{k \rightarrow \infty} \operatorname{Gamma}(k, \lambda)=\operatorname{Norm}\left(\mu=\frac{k}{\lambda}, \sigma=\sqrt{\frac{k}{\lambda^{2}}}\right)$ |
| Chi-square Distribution $\chi^{2}(t ; v)$ | Special Case: $\chi^{2}(t ; v)=\operatorname{Gamma}\left(t ; k=\frac{v}{2}, \lambda=\frac{1}{2}\right)$ <br> where $v$ is an integer |
| Inverse Gamma Distribution $I G(t ; \alpha, \beta)$ | Let $\begin{aligned} & \mathrm{X} \sim \operatorname{Gamma}(k, \lambda) \quad \text { and } \quad \mathrm{Y}=\frac{1}{\mathrm{X}} \\ & \text { Then } \quad \mathrm{Y} \sim \mathrm{I} G(\alpha=k, \beta=\lambda) \end{aligned}$ |
| Beta Distribution $\operatorname{Beta}(t ; \alpha, \beta)$ | Let $\begin{aligned} & X_{1}, X_{2} \sim \operatorname{Gamma}\left(\mathrm{k}_{\mathrm{i}}, \lambda_{\mathrm{i}}\right) \quad \text { and } \quad \mathrm{Y}=\frac{\mathrm{X}_{1}}{\mathrm{X}_{1}+\mathrm{X}_{2}} \\ & \mathrm{Y} \sim \operatorname{Beta}\left(\alpha=k_{1}, \beta=k_{2}\right) \end{aligned}$ |
| Dirichlet Distribution $\operatorname{Dir}_{d}(\boldsymbol{x} ; \boldsymbol{\alpha})$ | Let: $\begin{aligned} & Y_{i} \sim \operatorname{Gamma}\left(\lambda, k_{i}\right) \text { i.i.d and } V=\sum_{i=1}^{d} Y_{i} \\ & \text { Then: } \quad V \sim \operatorname{Gamma}\left(\lambda, \sum k_{i}\right) \\ & \text { Let: } \quad \boldsymbol{Z}=\left[\frac{Y_{1}}{V}, \frac{Y_{2}}{V}, \ldots, \frac{Y_{d}}{V}\right] \\ & \text { Then: } \quad \boldsymbol{Z} \sim \operatorname{Dir}_{d}\left(\alpha_{1}, \ldots, \alpha_{k}\right) \end{aligned}$ <br> *i.i.d: independent and identically distributed |
| Wishart Distribution Wishart $_{d}(n ; \boldsymbol{\Sigma})$ | The Wishart Distribution is the multivariate generalization of the gamma distribution. |# 4.4. Logistic Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\mu$ | $-\infty<\mu<\infty$ | Location parameter. $\mu$ is the mean, median and mode of the distribution. |
|  | $s$ | $\mathrm{~s}>0$ | Scale parameter. Proportional to the standard deviation of the distribution. |
| Limits |  | $-\infty<\mathrm{t}<\infty$ |  |
| Distribution |  | Formulas |  |
| PDF | where | $f(t)=\frac{\mathrm{e}^{z}}{\mathrm{~s}\left(1+\mathrm{e}^{z}\right)^{2}}=\frac{\mathrm{e}^{-z}}{\mathrm{~s}\left(1+\mathrm{e}^{-z}\right)^{2}}$ <br> $=\frac{1}{4 s} \operatorname{sech}^{2}\left(\frac{t-\mu}{2 s}\right)$ <br> $z=\frac{t-\mu}{s}$ |  |
| CDF |  | $F(t)=\frac{1}{1+\mathrm{e}^{-2}}=\frac{\mathrm{e}^{z}}{1+\mathrm{e}^{z}}$ <br> $=\frac{1}{2}+\frac{1}{2} \tanh \left(\frac{t-\mu}{2 s}\right)$ |  |
| Reliability |  | $\mathrm{R}(\mathrm{t})=\frac{1}{1+\mathrm{e}^{z}}$ |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | Where <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life |  | $u(t)=\left(1+e^{x}\right)\left(\mathrm{s} \cdot \ln \left[e^{1 / \mathrm{s}}+e^{\mu / s}\right]-\mathrm{t}\right)$ |  |
| Hazard Rate |  | $h(t)=\frac{1}{\mathrm{~s}\left(1+\mathrm{e}^{-z}\right)}=\frac{F(t)}{s}$ <br> $=\frac{1}{\mathrm{~s}+\mathrm{s} \exp \left\{\frac{\mu-t}{s}\right\}}$ |  |
| Cumulative Hazard Rate |  | $H(t)=\ln \left[1+\exp \left\{\frac{t-\mu}{s}\right\}\right]$ |  || Properties and Moments |  |
| :--: | :--: |
| Median | $\mu$ |
| Mode | $\mu$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\mu$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{\pi^{2}}{3} \mathrm{~s}^{2}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | 0 |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $\frac{6}{5}$ |
| Characteristic Function | $e^{i \mu t} B(1-i s t, 1+i s t)$ for $|s t|<1$ |
| $100 \gamma \%$ Percentile Function | $t_{\gamma}=\mu+s \ln \left(\frac{\gamma}{1-\gamma}\right)$ |
| Parameter Estimation |  |
| Plotting Method |  |
| Least Mean <br> Square $y=m x+c$ | X-Axis $\quad$ Y-Axis $\quad \hat{s}=\frac{1}{\mathrm{~m}}$ <br> $\mathrm{t}_{\mathrm{i}} \quad \ln [\mathrm{F}]-\ln [1-F]$ $\hat{\mu}=-c \hat{s}$ |
| Maximum Likelihood Function |  |
| Likelihood <br> Function | For complete data: $\quad L(\mu, s \mid E)=\underbrace{\prod_{i=1}^{n_{F}} \frac{\exp \left\{\frac{t_{i}-\mu}{-s}\right\}}{\mathrm{s}\left(1+\exp \left\{\frac{t_{i}-\mu}{-s}\right\}\right)}}_{\text {failures }}$ |
| Log-Likelihood Function | $\Lambda(\mu, s \mid E)=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln \mathrm{s}+\sum_{i=1}^{n_{F}}\left\{\frac{t_{i}-\mu}{-s}\right\}-2 \sum_{i=1}^{n_{F}} \ln \left(1+\exp \left\{\frac{t_{i}-\mu}{-s}\right\}\right)}_{\text {failures }}$ |
| $\frac{\partial \Lambda}{\partial \mu}=0$ | $\frac{\partial \Lambda}{\partial \mu}=\underbrace{\frac{\mathrm{n}_{\mathrm{F}}}{\mathrm{s}}-\frac{2}{s} \sum_{i=1}^{n_{F}}\left(1+\exp \left\{\frac{t_{i}-\mu}{s}\right\}\right)}_{\text {failures }}=0$ |
| $\frac{\partial \Lambda}{\partial \mathrm{~s}}=0$ | $\frac{\partial \Lambda}{\partial \mathrm{~s}}=\underbrace{-\frac{\mathrm{n}_{\mathrm{F}}}{\mathrm{s}}-\frac{1}{s} \sum_{i=1}^{n_{F}}\left(\frac{t_{i}-\mu}{s}\right)\left[1-\exp \left\{\frac{t_{i}-\mu}{s}\right\}\right]}_{\text {failures }}=0$ || MLE Point Estimates | The MLE estimates for $\hat{\mu}$ and $\hat{s}$ are found by solving the following equations: $\begin{gathered} \frac{1}{2}-\frac{1}{n_{F}} \sum_{i=1}^{n_{F}}\left[1+\exp \left\{\frac{t_{i}-\mu}{s}\right\}\right]^{-1}=0 \\ 1+\frac{1}{n_{F}} \sum_{i=1}^{n_{F}}\left(\frac{t_{i}-\mu}{s}\right) \frac{1-\exp \left\{\frac{t_{i}-\mu}{s}\right\}}{1+\exp \left\{\frac{t_{i}-\mu}{s}\right\}}=0 \end{gathered}$ <br> These estimates are biased. (Balakrishnan 1991) provides tables derived from Monte Carlo simulation to correct the bias. |
| :--: | :--: |
| Fisher Information | $I(\mu, s)=\left[\begin{array}{cc}\frac{1}{3 s^{2}} & 0 \\ 0 & \frac{\pi^{2}+3}{9 s^{2}}\end{array}\right]$ |
| (Antle et al. 1970) |  |
| $100 \gamma \%$ <br> Confidence Intervals | Confidence intervals are most often obtained from tables derived from Monte Carlo simulation. Corrections from using the Fisher Information matrix method are given in (Antle et al. 1970). |
| Bayesian |  |
| Non-informative Priors $\pi_{0}(\boldsymbol{\mu}, \boldsymbol{s})$ |  |
| Type | Prior |
| Jeffery Prior | $\frac{1}{s}$ |
| Description, Limitations and Uses |  |
| Example | The accuracy of a cutting machine used in manufacturing is desired to be measured. 5 cuts at the required length are made and measured as: $\begin{gathered} 7.436,10.270,10.466,11.039,11.854 \mathrm{~mm} \end{gathered}$ <br> Numerically solving MLE equations gives: $\begin{gathered} \hat{\mu}=10.446 \\ \hat{s}=0.815 \end{gathered}$ <br> This gives a mean of 10.446 and a variance of 2.183 . Compared to the same data used in the Normal distribution section it can be seen that this estimate is very similar to a normal distribution. <br> $90 \%$ confidence interval for $\mu$ : $\left[\begin{array}{cc}\hat{\mu}-\Phi^{-1}(0.95) & \frac{3 \hat{s}^{2}}{n_{F}}, \quad \hat{\mu}+\Phi^{-1}(0.95) & \frac{3 \hat{s}^{2}}{n_{F}} \\ {[9.408,11.4844]} \end{array}\right]$ ||  | $90 \%$ confidence interval for $s$ : $\begin{aligned} & {\left[\delta \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{\frac{9 \delta^{2}}{n_{F}\left(3+\pi^{2}\right)}}}{-\delta}\right)\right.} \\ & {[0.441,1.501]} \end{aligned}$ |
| :--: | :--: |
|  | Note that this confidence interval uses the assumption of the parameters being normally distributed which is only true for large sample sizes. Therefore these confidence intervals may be inaccurate. <br> Bayesian methods must be calculated using numerical methods. |
| Characteristics | The logistic distribution is most often used to model growth rates (and has been used extensively in biology and chemical applications). In reliability engineering it is most often used as a life distribution. <br> Shape. There is no shape parameter and so the logistic distribution is always a bell shaped curve. Increasing $\mu$ shifts the curve to the right, increasing $s$ increases the spread of the curve. <br> Normal Distribution. The shape of the logistic distribution is very similar to that of a normal distribution with the logistic distribution having slightly 'longer tails'. It would take a large number of samples to distinguish between the distributions. The main difference is that the hazard rate approaches $1 / s$ for large $t$. The logistic function has historically been preferred over the normal distribution because of its simplified form. (Meeker \& Escobar 1998, p.89) <br> Alternative Parameterization. It is equally as popular to present the logistic distribution using the true standard deviation $\sigma=\pi s / \sqrt{3}$. This form is used in reference book, Balakrishnan 1991, and gives the following cdf: $F(t)=\frac{1}{1+\exp \left(\frac{-\pi}{\sqrt{3}}\left(\frac{t-\mu}{\sigma}\right)\right)}$ <br> Standard Logistic Distribution. The standard logistic distribution has $\mu=0, s=1$. The standard logistic distribution random variable, $Z$, is related to the logistic distribution: $Z=\frac{X-\mu}{s}$ ||  | Let: $\quad T \sim \operatorname{Logistic}(t ; \mu, s)$ <br> Scaling property (Leemis \& McQueston 2008) $a T \sim \operatorname{Logistic}(t ; \mu, a s)$ <br> Rate Relationships. The distribution has the following rate relationships which make it suitable for modeling growth (Hastings et al. 2000, p.127): $\begin{gathered} h(t)=\frac{\mathrm{f}(\mathrm{t})}{\mathrm{R}(\mathrm{t})}=\frac{F(t)}{s} \\ z=\ln \left[\frac{F(t)}{R(t)}\right]=\ln [F(t)]-\ln [1-F(t)] \end{gathered}$ <br> where $\quad z=\frac{t-\mu}{s}$ <br> when $\mu=0$ and $s=1$ : $\quad f(t)=\frac{d F(t)}{d t}=F(t) R(t)$ |
| :--: | :--: |
| Applications | Growth Model. The logistic distribution most common use is a growth model. <br> Life Distribution. In reliability applications it is used as a life distribution. It is similar in shape to a normal distribution and so is often used instead of a normal distribution due to its simplified form. (Meeker \& Escobar 1998, p.89) <br> Logistic Regression. Logistic regression is a generalized linear regression model used predict binary outcomes. (Agresti 2002) |
| Resources | Online: <br> http://mathworld.wolfram.com/LogisticDistribution.html <br> http://en.wikipedia.org/wiki/Logistic_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> http://www.weibull.com/LifeDataWeb/the_logistic_distribution.htm <br> Books: <br> Balakrishnan, 1991. Handbook of the Logistic Distribution 1st ed., CRC. <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1995. Continuous Univariate Distributions, Vol. 2 2nd ed., Wiley-Interscience. || Relationship to Other Distributions |  |
| :--: | :--: |
| Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let $\quad X \sim \operatorname{Exp}(\lambda=1) \quad$ and $\quad Y=\ln \left(\frac{e^{-X}}{1+e^{-X}}\right)$ <br> Then $\quad Y \sim \operatorname{Logistic}(0,1)$ <br> (Hastings et al. 2000, p.127) |
| Pareto <br> Distribution <br> Pareto $(\theta, \alpha)$ | Let $\quad X \sim \operatorname{Pareto}(\theta, \alpha) \quad$ and $\quad Y=-\ln \left\{\left(\frac{\mathrm{X}}{\theta}\right)^{\alpha}-1\right\}$ <br> Then $\quad Y \sim \operatorname{Logistic}(0,1)$ <br> (Hastings et al. 2000, p.127) |
| Gumbel Distribution Gumbel $(\alpha, \beta)$ | Let $\quad X_{i} \sim \operatorname{Gumbel}(\alpha, \beta) \quad$ and $\quad Y=\mathrm{X}_{1}-\mathrm{X}_{2}$ <br> Then $\quad Y \sim \operatorname{Logistic}(0, \beta)$ <br> (Hastings et al. 2000, p.127) |# 4.5. Normal (Gaussian) Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - F(t)


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\mu$ | $-\infty<\mu<\infty$ | Location parameter: The mean of the distribution. |
|  | $\sigma^{2}$ | $\sigma^{2}>0$ | Scale parameter: The standard deviation of the distribution. |
| Limits | $-\infty<\mathrm{t}<\infty$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(\frac{\mathrm{t}-\mu}{\sigma}\right)^{2}\right]$ <br> $=\frac{1}{\sigma} \phi\left[\frac{t-\mu}{\sigma}\right]$ <br> where $\phi$ is the standard normal pdf with $\mu=0$ and $\sigma^{2}=1$. |  |  |
| CDF | $F(t)=\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{t} \exp \left[-\frac{1}{2}\left(\frac{\theta-\mu}{\sigma}\right)^{2}\right] d \theta$ <br> $=\frac{1}{2}+\frac{1}{2} \operatorname{erf}\left(\frac{t-\mu}{\sigma \sqrt{2}}\right)$ <br> $=\Phi\left(\frac{\mathrm{t}-\mu}{\sigma}\right)$ <br> where $\Phi$ is the standard normal cdf with $\mu=0$ and $\sigma^{2}=1$. |  |  |
| Reliability | $R(t)=1-\Phi\left(\frac{t-\mu}{\sigma}\right)$ <br> $=\Phi\left(\frac{\mu-t}{\sigma}\right)$ |  |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=\frac{\Phi\left(\frac{\mu-x-t}{\sigma}\right)}{\Phi\left(\frac{\mu-t}{\sigma}\right)}$ <br> Where <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life | $u(t)=\frac{\int_{t}^{\infty} R(x) d x}{R(t)}=\frac{\int_{t}^{\infty} R(x) d x}{R(t)}$ |  |  |
| Hazard Rate | $h(t)=\frac{\phi\left[\frac{\mathrm{t}-\mu}{\sigma}\right]}{\sigma\left(\Phi\left[\frac{\mu-\mathrm{t}}{\sigma}\right]\right)}$ |  |  |
| Cumulative Hazard Rate | $H(t)=-\ln \left[\Phi\left(\frac{\mu-t}{\sigma}\right)\right]$ |  |  || Properties and Moments |  |
| :--: | :--: |
| Median | $\mu$ |
| Mode | $\mu$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\mu$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\sigma^{2}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | 0 |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | 0 |
| Characteristic Function | $\exp \left(i \mu t-\frac{1}{2} \sigma^{2} t^{2}\right)$ |
| $100 \alpha \%$ Percentile Function | $\begin{aligned} t_{\alpha} & =\mu+\sigma \Phi^{-1}(\alpha) \\ & =\mu+\sigma \sqrt{2} \operatorname{erf}^{-1}(2 \alpha-1) \end{aligned}$ |
| Parameter Estimation |  |
| Plotting Method |  |
| Least Mean <br> Square $y=m x+c$ | X-Axis $\quad$ Y-Axis $\quad \tilde{\mu}=-\frac{c}{m}$ <br> $t_{i} \quad \operatorname{invNorm}\left[F\left(t_{i}\right)\right]$ |
| Maximum Likelihood Function |  |
| Likelihood Function | For complete data: $\quad L(\mu, \sigma \mid E)=\underbrace{\frac{1}{(\sigma \sqrt{2 \pi})} n_{F}} \prod_{i=1}^{n_{F}} \exp \left(-\frac{1}{2}\left[\frac{t_{i}-\mu}{\sigma}\right]^{2}\right)$ <br> $=\underbrace{\frac{1}{(\sigma \sqrt{2 \pi})} n_{F}} \exp \left(-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2}\right)$ |
| Log-Likelihood Function | $\Lambda(\mu, \sigma \mid E)=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln (\sigma \sqrt{2 \pi})}_{f a i l u r e s}-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2}$ |
| $\frac{\partial \Lambda}{\partial \mu}=0$ | solve for $\mu$ to get MLE $\tilde{\mu}$ : $\quad \frac{\partial \Lambda}{\partial \mu}=\underbrace{\frac{\mu n_{F}}{\sigma^{2}}-\frac{1}{\sigma^{2}} \sum_{i=1}^{n_{F}} t_{i}}_{\text {failures }}=0$ |
| $\frac{\partial \Lambda}{\partial \sigma}=0$ | solve for $\sigma$ to get $\tilde{\sigma}$ : $\quad \frac{\partial \Lambda}{\partial \sigma}=\underbrace{-\frac{\mathrm{n}_{\mathrm{F}}}{\sigma}+\frac{1}{\sigma^{3}} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2}}_{\text {failures }}=0$ || MLE Point Estimates | When there is only complete failure data the point estimates can be given as:

$$
\hat{\mu}=\frac{1}{n_{F}} \sum_{i=1}^{n_{F}} t_{i} \quad \widehat{\sigma^{2}}=\frac{1}{n_{F}} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2}
$$

In most cases the unbiased estimators are used:

$$
\hat{\mu}=\frac{1}{n_{F}} \sum_{i=1}^{n_{F}} t_{i} \quad \widehat{\sigma^{2}}=\frac{1}{n_{F}-1} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2}
$$

| Fisher <br> Information | $l\left(\mu, \sigma^{2}\right)=\left[\begin{array}{cc}1 / \sigma^{2} & 0 \\ 0 & -1 / 2 \sigma^{4}\end{array}\right]$ |  |  |
| :--: | :--: | :--: | :--: |
| $\begin{aligned} & 100 y \% \\ & \text { Confidence } \\ & \text { Intervals } \end{aligned}$ <br> (for complete data) | $\mu$ <br> $\sigma^{2} \quad \widehat{\sigma^{2}} \frac{(n-1)}{\overline{\chi_{0}^{2}(n-1)}} \quad \widehat{\sigma^{2}} \frac{(n-1)}{\overline{\chi_{[1+i]}^{2}(n-1)}} \quad \widehat{\sigma^{2}} \frac{(n-1)}{\overline{\chi_{[1+i]}^{2}(n-1)}} \quad \widehat{\sigma^{2}} \frac{\overline{\chi_{[1+i]}^{2}(n-1)}}{\overline{\chi_{[1-i]}^{2}(n-1)}} \hline \end{aligned}$ | 2 Sided - Lower <br> $\hat{\mu}-\frac{\hat{\sigma}}{\sqrt{n}} t_{[1+\gamma]}(n-1)$ <br> $\hat{\sigma}^{2} \frac{(n-1)}{\hat{\sigma}^{2}} \frac{(n-1)}{(n-1)}$ <br> $\hat{\sigma}^{2} \frac{(n-1)}{\chi_{[1-\gamma]}^{2}(n-1)} \quad \widehat{\sigma^{2}} \frac{\chi_{[1-\gamma]}^{2}}{2}$ | 2 Sided - Upper <br> $\hat{\mu}+\frac{\hat{\sigma}}{\sqrt{n}} t_{[1+\gamma]}(n-1)$ |
| (Nelson 1982, pp.218-220) Where $t_{y}(n-1)$ is the $100 y^{\text {th }}$ percentile of the $t$-distribution with $n-1$ degrees of freedom and $\chi_{p}^{2}(n-1)$ is the $100 y^{\text {th }}$ percentile of the $\chi^{2}$-distribution with $n-1$ degrees of freedom. |  |  |  |
| Bayesian |  |  |  |
| Non-informative Priors when $\sigma^{2}$ is known, $\pi_{0}(\mu)$ (Yang and Berger 1998, p.22) |  |  |  |
| Type | Prior | Posterior |  |
| Uniform Proper <br> Prior with limits $\mu \in[a, b]$ | $\frac{1}{b-a}$ | Truncated Normal Distribution <br> For $a \leq \mu \leq b$ <br> $c \cdot \operatorname{Norm}\left(\mu ; \frac{\sum_{i=1}^{n_{F}} t_{i}^{F}}{n_{F}}, \frac{\sigma^{2}}{n_{F}}\right)$ <br> Otherwise $\pi(\mu)=0$ |  |
| All | 1 | $\begin{gathered} \text { Norm }\left(\mu ; \frac{\sum_{i=1}^{n_{F}} t_{i}^{F}}{n_{F}}, \frac{\sigma^{2}}{n_{F}}\right) \\ \text { when } \mu \in(\infty, \infty) \end{gathered}$ |  |
| Non-informative Priors when $\mu$ is known, $\pi_{\sigma}\left(\sigma^{2}\right)$ (Yang and Berger 1998, p.23) |  |  |  |
| Type | Prior | Posterior |  |
| Uniform Proper <br> Prior with limits $\sigma^{2} \in[a, b]$ | $\frac{1}{b-a}$ | Truncated Inverse Gamma Distribution For $a \leq \sigma^{2} \leq b$ |  ||  |  | $\begin{gathered} c . I G\left(\sigma^{2} ; \frac{\left(n_{F}-2\right)}{2}, \frac{S^{2}}{2}\right) \\ \text { Otherwise } \pi\left(\sigma^{2}\right)=0 \end{gathered}$ |
| :--: | :--: | :--: |
| Uniform <br> Improper <br> with limits $\sigma^{2} \in(0, \infty)$ | 1 | $\begin{gathered} I G\left(\sigma^{2} ; \frac{\left(n_{F}-2\right)}{2}, \frac{S^{2}}{2}\right) \\ \text { See section 1.7.1 } \end{gathered}$ |
| Jeffery's, <br> Reference, MDIP <br> Prior | $\frac{1}{\sigma^{2}}$ | $\begin{gathered} I G\left(\sigma^{2} ; \frac{n_{F}}{2}, \frac{S^{2}}{2}\right) \\ \text { with limits } \sigma^{2} \in(0, \infty) \\ \text { See section 1.7.1 } \end{gathered}$ |
| Non-informative Priors when $\mu$ and $\sigma^{2}$ are unknown, $\pi_{a}\left(\mu, \sigma^{2}\right)$ (Yang and Berger 1998, p.23) |  |  |
| Type | Prior | Posterior |
| Improper <br> Uniform with limits: $\begin{aligned} & \mu \in(\infty, \infty) \\ & \sigma^{2} \in(0, \infty) \end{aligned}$ | 1 | $\begin{gathered} \pi(\mu \mid E) \sim T\left(\mu ; \mathrm{n}_{\mathrm{F}}-3, \tilde{\imath}, \frac{\mathrm{~S}^{2}}{\mathrm{n}_{\mathrm{F}}\left(\mathrm{n}_{\mathrm{F}}-3\right)}\right) \\ \text { See section 1.7.2 } \\ \pi\left(\sigma^{2} \mid E\right) \sim I G\left(\sigma^{2} ; \frac{\left(n_{F}-3\right)}{2}, \frac{S^{2}}{2}\right) \\ \text { See section 1.7.1 } \end{gathered}$ |
| Jeffery's Prior | $\frac{1}{\sigma^{4}}$ | $\begin{gathered} \pi(\mu \mid E) \sim T\left(\mu ; \mathrm{n}_{\mathrm{F}}+1, \tilde{\imath}, \frac{\mathrm{~S}^{2}}{\mathrm{n}_{\mathrm{F}}\left(\mathrm{n}_{\mathrm{F}}+1\right)}\right) \\ \text { when } \mu \in(\infty, \infty) \\ \text { See section 1.7.2 } \\ \pi\left(\sigma^{2} \mid E\right) \sim I G\left(\sigma^{2} ; \frac{\left(n_{F}+1\right)}{2}, \frac{S^{2}}{2}\right) \\ \text { when } \sigma^{2} \in(0, \infty) \\ \text { See section 1.7.1 } \end{gathered}$ |
| Reference Prior ordering $\{\phi, \sigma\}$ | $\begin{gathered} \pi_{a}\left(\phi, \sigma^{2}\right) \\ \propto \frac{1}{\sigma \sqrt{2+\phi^{2}}} \\ \text { where } \\ \phi=\mu / \sigma \end{gathered}$ | No Closed Form |
| Reference where $\mu$ and $\sigma^{2}$ are separate groups. <br> MDIP Prior | $\frac{1}{\sigma^{2}}$ | $\begin{gathered} \pi(\mu \mid E) \sim T\left(\mu ; \mathrm{n}_{\mathrm{F}}-1, \tilde{\imath}, \frac{\mathrm{~S}^{2}}{\mathrm{n}_{\mathrm{F}}\left(\mathrm{n}_{\mathrm{F}}-1\right)}\right) \\ \text { when } \mu \in(\infty, \infty) \\ \text { See section 1.7.2 } \\ \pi\left(\sigma^{2} \mid E\right) \sim I G\left(\sigma^{2} ; \frac{\left(n_{F}-1\right)}{2}, \frac{S^{2}}{2}\right) \\ \text { when } \sigma^{2} \in(0, \infty) \\ \text { See section 1.7.1 } \end{gathered}$ |where

$$
S^{2}=\sum_{i=1}^{n_{F}}\left(t_{i}-\bar{t}\right)^{2} \quad \text { and } \quad \bar{t}=\frac{1}{n_{F}} \sum_{i=1}^{n_{F}} t_{i}
$$

| Conjugate Priors |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| UOI | Likelihood <br> Model | Evidence | Dist of UOI | Prior <br> Para | Posterior Parameters |
| $\begin{gathered} \mu \\ \text { from } \\ \operatorname{Norm}\left(t ; \mu, \sigma^{2}\right) \end{gathered}$ | Normal with known $\sigma^{2}$ | $n_{F}$ failures at times $t_{i}$ | Normal | $\mathrm{u}_{o}, v_{0}$ | $\begin{gathered} u_{0} \\ \frac{v_{0}}{} \end{gathered}$ <br> $v=\frac{1}{\frac{1}{v_{0}}+\frac{n_{F}}{\sigma^{2}}} \frac{\sum_{i=1}^{n_{F}} t_{i}^{F}}{\sigma^{2}} \frac{1}{v_{0}}+\frac{n_{F}}{\sigma^{2}} \quad v=\frac{1}{\frac{1}{v_{0}}+\frac{n_{F}}{\sigma^{2}}} \end{gathered}$ |
| $\begin{gathered} \sigma^{2} \\ \text { from } \\ \operatorname{Norm}\left(t ; \mu, \sigma^{2}\right) \end{gathered}$ | Normal with known $\mu$ | $n_{F}$ failures at times $t_{i}$ | Gamma | $k_{0}, \lambda_{0}$ | $\begin{gathered} k=k_{o}+n_{F} / 2 \\ \lambda=\lambda_{o}+\frac{1}{2} \sum_{i=1}^{n_{F}}\left(t_{i}-\mu\right)^{2} \end{gathered}$ |
| $\begin{gathered} \mu_{N} \\ \text { from } \\ \operatorname{LogN}\left(t ; \mu_{N}, \sigma_{N}^{2}\right) \end{gathered}$ | LogNormal with known $\sigma_{N}^{2}$ | $n_{F}$ failures at times $t_{i}$ | Normal | $u_{o}, v_{0}$ | $\begin{gathered} u_{0} \\ \frac{v_{0}}{} \end{gathered}$ <br> $v=\frac{1}{\frac{1}{v^{2}}+\frac{n_{F}}{\sigma_{N}^{2}}} \frac{\sum_{i}}{\frac{1}{v^{2}}+\frac{n_{F}}{\sigma_{N}^{2}}} \frac{1}{v_{0}} \quad v=\frac{1}{\frac{1}{v^{2}}+\frac{n_{F}}{\sigma_{N}^{2}}} \end{gathered}$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | The accuracy of a cutting machine used in manufacturing is desired to be measured. 5 cuts at the required length are made and measured as: $\square$ <br> MLE Estimates are: $\begin{gathered} \hat{\mu}=\frac{\sum t_{i}^{F}}{n_{F}}=10.213 \\ \widehat{\sigma^{2}}=\frac{\sum\left(t_{i}^{F}-\widehat{\mu_{t}}\right)^{2}}{n_{F}-1}=2.789 \end{gathered}$ <br> $90 \%$ confidence interval for $\mu$ : $\begin{gathered} \left[\hat{\mu}-\frac{\hat{\sigma}}{\sqrt{5}} t_{[0.95]}(4), \quad \hat{\mu}+\frac{\hat{\sigma}}{\sqrt{5}} t_{[0.95]}(4)\right] \\ {[10.163,10.262]} \end{gathered}$ |  |  |  |  |  |$90 \%$ confidence interval for $\sigma^{2}$ :

$$
\left[\frac{\sigma^{2}}{\sigma^{2}} \frac{4}{\chi_{(0.95)}^{2}(4)}, \quad \frac{\sigma^{2}}{\chi_{(0.95)}^{2}(4)}\right]
$$

A Bayesian point estimate using the Jeffery non-informative improper prior $1 / \sigma^{4}$ with posterior for $\mu \sim T(6,10.213,0.558)$ and $\sigma^{2} \sim I G(3,5.578)$ has a point estimates:

$$
\begin{gathered}
\hat{\mu}=\mathrm{E}[T(6,6.595,0.412)]=\mu=10.213 \\
\widehat{\sigma^{2}}=\mathrm{E}[I G(3,5.578)]=\frac{5.578}{2}=2.789
\end{gathered}
$$

With $90 \%$ confidence intervals:

$$
\begin{gathered}
\mu \\
\sigma^{2}
\end{gathered}
$$

$$
\begin{gathered}
{\left[F_{T}^{-1}(0.05)=8.761, \quad F_{T}^{-1}(0.95)=11.665\right]} \\
{\left[1 / F_{G}^{-1}(0.95)=0.886, \quad 1 / F_{G}^{-1}(0.05)=6.822\right]}
\end{gathered}
$$

Characteristics
Also known as a Gaussian distribution or bell curve.
Unit Normal Distribution. Also known as the standard normal distribution is when $\mu=0$ and $\sigma=1$ with pdf $\phi(z)$ and cdf $\Phi(z)$. If $X$ is normally distributed with mean $\mu$ and standard deviation $\sigma$ then the following transformation is used:

$$
z=\frac{x-\mu}{\sigma}
$$

Central Limit Theorem. Let $X_{1}, X_{2}, \ldots, X_{n}$ be a sequence of $n$ independent and identically distributed (i.i.d) random variables each having a mean of $\mu$ and a variance of $\sigma^{2}$. As the sample size increases, the distribution of the sample average of these random variables approaches the normal distribution with mean $\mu$ and variance $\sigma^{2} / n$ irrespective of the shape of the original distribution. Formally:

$$
S_{n}=X_{1}+\cdots+X_{n}
$$

If we define a new random variables:

$$
Z_{n}=\frac{S_{n}-n \mu}{\sigma \sqrt{n}}, \text { and } \quad Y=\frac{S_{n}}{n}
$$

The distribution of $Z_{n}$ converges to the standard normal distribution. The distribution of $S_{n}$ converges to a normal distribution with mean $\mu$ and standard deviation of $\sigma / \sqrt{n}$.

Sigma Intervals. Often intervals of the normal distribution are expressed in terms of distance away from the mean in units ofsigma. The following is approximate values for each sigma:

| Interval | $\boldsymbol{\Phi}(\boldsymbol{\mu}+\boldsymbol{n} \boldsymbol{\sigma})-\boldsymbol{\Phi}(\boldsymbol{\mu}-\boldsymbol{n} \boldsymbol{\sigma})$ |
| :--: | :--: |
| $\mu \pm \sigma$ | $68.2689492137 \%$ |
| $\mu \pm 2 \sigma$ | $95.4499736104 \%$ |
| $\mu \pm 3 \sigma$ | $99.7300203937 \%$ |
| $\mu \pm 4 \sigma$ | $99.9936657516 \%$ |
| $\mu \pm 5 \sigma$ | $99.9999426697 \%$ |
| $\mu \pm 6 \sigma$ | $99.9999998027 \%$ |

Truncated Normal. Often in reliability engineering a truncated normal distribution may be used due to the limitation that $t \geq 0$. See Truncated Normal Continuous Distribution.

# Inflection Points: 

Inflection points occur one standard deviation away from the mean $(\mu \pm \sigma)$.

## Mean / Median / Mode:

The mean, median and mode are always equal to $\mu$.
Hazard Rate. The hazard rate is increasing for all $t$. The Standard Normal Distribution's hazard rate approaches $h(t)=t$ as $t$ becomes large.

Let:

$$
\mathrm{X} \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)
$$

## Convolution Property

$$
\sum_{i=1}^{n} X_{i} \sim \operatorname{Norm}\left(\sum \mu_{i}, \sum \sigma_{i}^{2}\right)
$$

## Scaling Property

$$
a X+b \sim \operatorname{Norm}\left(a \mu+b, a^{2} \sigma^{2}\right)
$$

## Linear Combination Property:

$$
\sum_{i=1}^{n} a_{i} X_{i}+b_{i} \sim \operatorname{Norm}\left(\sum\left\{a_{i} \mu_{i}+b_{i}\right\}, \sum\left\{a_{i}^{2} \sigma_{i}^{2}\right\}\right)
$$

Applications Approximations to Other Distributions. The origin of the Normal Distribution was from an approximation of the Binomial distribution. Due to the Central Limit Theory the Normal distribution can be used to approximate many distributions as detailed under 'Related Distributions'.

Strength Stress Interference. When the strength of a component follows a distribution and the stress that component is subjected to follows a distribution there exists a probability that the stress will be greater than the strength. When both distributions are a normal distribution, there is a closed for solution to the interference|  | probability. <br> Life Distribution. When used as a life distribution a truncated Normal Distribution may be used due to the constraint $t \geq 0$. However it is often found that the difference in results is negligible. (Rausand \& Høyland 2004) <br> Time Distributions. The normal distribution may be used to model simple repair or inspection tasks that have a typical duration with variation which is symmetrical about the mean. This is typical for inspection and preventative maintenance times. <br> Analysis of Variance (ANOVA). A test used to analyze variance and dependence of variables. A popular model used to conduct ANOVA assumes the data comes from a normal population. <br> Six Sigma Quality Management. Six sigma is a business management strategy which aims to reduce costs in manufacturing processes by removing variance in quality (defects). Current manufacturing standards aim for an expected 3.4 defects out of one million parts: $2 \Phi(-6)$. (Six Sigma Academy 2009) |
| :--: | :--: |
| Resources | Online: <br> http://www.weibull.com/LifeDataWeb/the_normal_distribution.htm http://mathworld.wolfram.com/NormalDistribution.html http://en.wikipedia.org/wiki/Normal_distribution http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> Books: <br> Patel, J.K. \& Read, C.B., 1996. Handbook of the Normal Distribution 2nd ed., CRC. <br> Simon, M.K., 2006. Probability Distributions Involving Gaussian Random Variables: A Handbook for Engineers and Scientists, Springer. |
| Relationship to Other Distributions |  |
| Truncated Normal Distribution $\begin{aligned} & \operatorname{TNorm}\left(x ; \mu, \sigma, a_{L}, b_{U}\right) \\ & \text { LogNormal } \\ & \text { Distribution } \\ & \log N\left(t ; \mu_{N}, \sigma_{N}^{2}\right) \end{aligned}$ | Let: $\begin{gathered} X \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right) \\ X \in(\infty, \infty) \\ Y \sim \mathrm{~T} \operatorname{Norm}\left(\mu, \sigma^{2}, a_{L}, b_{U}\right) \\ Y \in\left[a_{L}, b_{U}\right] \end{gathered}$ |
|  | $X \sim \log N\left(\mu_{N}, \sigma_{N}^{2}\right)$ $Y=\ln (X)$ <br> $Y \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)$ ||  |  | $\mu_{N}=\ln \left(\frac{\mu^{2}}{\sqrt{\sigma^{2}+\mu^{2}}}\right), \quad \sigma_{N}=\sqrt{\ln \left(\frac{\sigma^{2}+\mu^{2}}{\mu^{2}}\right)}$ |
| :--: | :--: | :--: |
| Rayleigh <br> Distribution <br> Rayleigh $(t ; \sigma)$ | Let <br> Then | $X_{1}, X_{2} \sim \operatorname{Norm}(0, \sigma) \quad$ and $\quad Y=\sqrt{X_{1}^{2}+X_{2}^{2}}$ <br> $\mathrm{Y} \sim \operatorname{Rayleigh}(\sigma)$ |
| Chi-square <br> Distribution $\chi^{2}(t ; v)$ | Let <br> Then | $X_{\mathrm{i}} \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right) \quad$ and $\quad \mathrm{Y}=\sum_{\mathrm{k}=1}^{\mathrm{v}}\left(\frac{\mathrm{X}_{\mathrm{k}}-\mu}{\sigma}\right)^{2}$ <br> $\mathrm{Y} \sim \chi^{2}(t ; v)$ |
| Binomial <br> Distribution <br> $\operatorname{Binom}(k ; n, p)$ | Limiting Case for constant $p$ : <br> $\lim _{\substack{p \rightarrow \infty \\ p=p}} \operatorname{Binom}(k ; n, p)=\operatorname{Norm}\left(\mathrm{k} ; \mu=\mathrm{n} p, \sigma^{2}=n p(1-p)\right)$ <br> The Normal distribution can be used as an approximation of the Binomial distribution when $n p \geq 10$ and $n p(1-p) \geq 10$. <br> $\operatorname{Binom}(k ; p, n) \approx \operatorname{Norm}\left(t=k+0.5 ; \mu=n p, \sigma^{2}=n p(1-p)\right)$ |  |
| Poisson <br> Distribution <br> $\operatorname{Pois}(\mathrm{k} ; \mu)$ |  | $\lim _{\mu \rightarrow \infty} F_{\text {Pois }}(k ; \mu)=F_{\text {Norm }}\left(k ; \mu^{\prime}=\mu, \sigma=\sqrt{\mu}\right)$ <br> This is a good approximation when $\mu>1000$. When $\mu>10$ the same approximation can be made with a correction: $\begin{aligned} & \lim _{\mu \rightarrow \infty} F_{\text {Pois }}(k ; \mu)=F_{\text {Norm }}\left(k ; \mu^{\prime}=\mu-0.5, \sigma=\sqrt{\mu}\right) \\ & \end{aligned}$ |
| Beta Distribution <br> $\operatorname{Beta}(t ; \alpha, \beta)$ | For large $\alpha$ and $\beta$ with fixed $\alpha / \beta$ : <br> $\operatorname{Beta}(\alpha, \beta) \approx \operatorname{Norm}\left(\mu=\frac{\alpha}{\alpha+\beta}, \sigma=\sqrt{\frac{\alpha \beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}}\right)$ <br> As $\alpha$ and $\beta$ increase the mean remains constant and the variance is reduced. |  |
| Gamma <br> Distribution <br> $\operatorname{Gamma}(k, \lambda)$ | Special Case for large k: $\begin{aligned} & \lim _{k \rightarrow \infty} \operatorname{Gamma}(k, \lambda)=\operatorname{Norm}\left(\mu=\frac{k}{\lambda}, \sigma=\sqrt{\frac{k}{\lambda^{2}}}\right) \end{aligned}$ |  |# 4.6. Pareto Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |
| :--: | :--: | :--: |
| Parameters | $\theta$ | $\theta>0$ <br> Location parameter. $\theta$ is the lower limit of $t$. Sometimes refered to as $t$ minimum. |
|  | $\alpha$ | $\alpha>0$ <br> Shape parameter. Sometimes called the Pareto index. |
| Limits | $\theta \leq \mathrm{t}<\infty$ |  |
| Distribution | Formulas |  |
| PDF | $f(t)=\frac{\alpha \theta^{\alpha}}{\mathrm{t}^{\alpha+1}}$ |  |
| CDF | $F(t)=1-\left(\frac{\theta}{\mathrm{t}}\right)^{\alpha}$ |  |
| Reliability | $R(t)=\left(\frac{\theta}{\mathrm{t}}\right)^{\alpha}$ |  |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}=\frac{(t)^{\alpha}}{(t+x)^{\alpha}}$ <br> $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |
| Mean Residual Life | $u(t)=\frac{\int_{t}^{\infty} R(x) d x}{R(t)}$ |  |
| Hazard Rate | $h(t)=\frac{\alpha}{\mathrm{t}}$ |  |
| Cumulative <br> Hazard Rate | $H(t)=\alpha \ln \left(\frac{t}{\theta}\right)$ |  |
| Properties and Moments |  |  |
| Median | $\theta 2^{1 / \alpha}$ |  |
| Mode | $\theta$ |  |
| Mean - $1^{\text {st }}$ Raw Moment | $\frac{\alpha \theta}{\alpha-1}$, for $\alpha>1$ |  |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{\alpha \theta^{2}}{(\alpha-1)^{2}(\alpha-2)}$, for $\alpha>2$ |  |
| Skewness - $3^{\text {rd }}$ Central Moment | $\frac{2(1+\alpha)}{(\alpha-3)} \sqrt{\frac{\alpha-2}{\alpha}}$, for $\alpha>3$ |  || Excess kurtosis - $4^{\text {th }}$ Central Moment |  | $\frac{6\left(\alpha^{2}+\alpha^{2}-6 \alpha-2\right)}{\alpha(\alpha-3)(\alpha-4)}$, for $\alpha>4$ |  |
| :--: | :--: | :--: | :--: |
| Characteristic Function |  | $\alpha(-i \theta t)^{\alpha} \Gamma(-\alpha,-i \theta t)$ |  |
| 100y \% Percentile Function |  | $t_{\gamma}=\theta(1-\gamma)^{-1 / \alpha}$ |  |
| Parameter Estimation |  |  |  |
| Plotting Method |  |  |  |
| Least Mean <br> Square $y=m x+c$ | X-Axis | Y-Axis | $\begin{gathered} \bar{a}=-m \\ \bar{\theta}=\exp \left(\frac{c}{\bar{\alpha}}\right) \end{gathered}$ |
|  | $\ln \left(t_{i}\right)$ | $\ln [1-F]$ |  |
| Maximum Likelihood Function |  |  |  |
| Likelihood Function | For complete data: $L(\theta, \alpha \mid E)=\underbrace{\alpha^{\mathrm{n}_{\mathrm{F}}} \theta^{\alpha \mathrm{n}_{\mathrm{F}}}}_{\text {failures }} \prod_{\substack{1=1 \\ \text { failures }}}^{\mathrm{n}_{\mathrm{F}}} \frac{1}{\theta}$ |  |  |
| Log-Likelihood Function | $\Lambda(\theta, \alpha \mid E)=\underbrace{\mathrm{n}_{\mathrm{F}} \ln (\alpha)+\mathrm{n}_{\mathrm{F}} \alpha \ln (\theta)-(\alpha+1)}_{\text {failures }} \sum_{\substack{i=1}}^{\mathrm{n}_{\mathrm{F}}} \ln t_{i}$ |  |  |
| $\frac{\partial \Lambda}{\partial \alpha}=0$ | solve for $\alpha$ to get $\bar{a}$ : $\frac{\partial \Lambda}{\partial \alpha}=\underbrace{-\frac{\mathrm{n}_{\mathrm{F}}}{\alpha}+\mathrm{n}_{\mathrm{F}} \ln \theta-\sum_{\substack{i=1 \\ \text { failures }}}^{n_{F}} \ln t_{i}}_{\text {failures }}=0$ |  |  |
| MLE Point Estimates | The likelihood function increases as $\theta$ increases. Therefore the MLE point estimate is the largest $\theta$ which satisfies $\theta \leq t_{i}<\infty$ :

$$
\bar{\theta}=\min \left\{\mathrm{t}_{1}, \ldots, \mathrm{t}_{\mathrm{n}_{\mathrm{F}}}\right\}
$$

Substituting $\bar{\theta}$ gives the MLE for $\bar{a}$ :

$$
\bar{a}=\frac{n_{F}}{\sum_{i=1}^{n_{F}}\left(\ln t_{i}-\ln \bar{\theta}\right)}
$$

| Fisher <br> Information | $l(\theta, \alpha)=\left[\begin{array}{cc}-1 / \alpha^{2} & 0 \\ 0 & 1 / \theta^{2}\end{array}\right]$ |  |  |
| :--: | :--: | :--: | :--: |
| $100 \gamma \%$ <br> Confidence <br> Intervals |  | 1 Sided - Lower | 2 Sided - Lower | 2 Sided - Upper |
|  | $\frac{\bar{a}}{2 \theta \text { is }}$ <br> unknown | $\frac{\bar{a}}{2 \mathrm{n}_{\mathrm{F}}} \chi_{(1-\gamma)}(2 \mathrm{n}-2)$ | $\frac{\bar{a}}{2 \mathrm{n}_{\mathrm{F}}} \chi^{2}\left(\frac{1-\gamma}{2}\right)(2 \mathrm{n}-2)$ | $\frac{\bar{a}}{2 \mathrm{n}_{\mathrm{F}}} \chi^{2}\left(\frac{1+\gamma}{2}\right)(2 \mathrm{n}-2)$ || (for complete data) | $\begin{gathered} \bar{a} \\ \text { e is } \\ \text { known } \end{gathered}$ | $\frac{\bar{\sigma}}{2 \mathrm{n}_{F}} \chi_{(1-\gamma)(2 \mathrm{n})}^{2}$ | $\frac{\bar{\sigma}}{2 \mathrm{n}_{F}} \chi_{(1-\gamma)(2 \mathrm{n})}^{2}(2 \mathrm{n})$ | $\frac{\bar{\sigma}}{2 \mathrm{n}_{F}} \chi_{(1+\gamma)(2 \mathrm{n}-2)}^{2}(2 \mathrm{n}-2)$ |
| :--: | :--: | :--: | :--: | :--: |
|  | (Johnson et al. 1994, p.583) Where $\chi_{F}^{2}(n)$ is the $100 y^{\text {th }}$ percentile of the $\chi^{2}$-distribution with $n$ degrees of freedom. |  |  |  |
| Bayesian |  |  |  |  |
| Non-informative Priors when $\boldsymbol{\theta}$ is known, $\pi_{\theta}(\boldsymbol{\alpha})$ (Yang and Berger 1998, p.22) |  |  |  |  |
| Type |  | Prior |  |  |
| Jeffery and Reference |  | $\frac{1}{\alpha}$ |  |  |
| Conjugate Priors |  |  |  |  |
| UOI |  | Likelihood Model | Evidence | Dist of UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} b \\ \text { from } \\ \text { Unif }(t ; \mathrm{a}, b) \end{gathered}$ |  | Uniform with known a | $n_{F}$ failures at times $t_{i}$ | Pareto | $\theta_{o}, \alpha_{0}$ | $\begin{gathered} \theta=\max \left\{t_{1}, \ldots, t_{n_{F}}\right\} \\ \alpha=\alpha_{0}+n_{F} \end{gathered}$ |
| $\begin{gathered} \theta \\ \text { from } \\ \text { Pareto }(t ; \theta, \alpha) \end{gathered}$ |  | Pareto with known $\alpha$ | $n_{F}$ failures at times $t_{i}$ | Pareto | $\mathrm{a}_{0}, \theta_{0}$ | $\begin{gathered} \mathrm{a}=\mathrm{a}_{o}-\alpha n_{F} \\ \text { where } \mathrm{a}_{0}>\alpha n_{F} \\ \theta=\theta_{0} \end{gathered}$ |
| $\begin{gathered} \alpha \\ \text { from } \\ \text { Pareto }(t ; \theta, \alpha) \end{gathered}$ |  | Pareto with known $\theta$ | $n_{F}$ failures at times $t_{i}$ | Gamma | $\mathrm{k}_{0}, \lambda_{0}$ | $\begin{gathered} \mathrm{k}=\mathrm{k}_{o}+n_{F} \\ \lambda=\lambda_{o}+\sum_{i=1}^{n_{F}} \ln \left(\frac{x_{i}}{\theta}\right) \end{gathered}$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example |  | 5 components are put on a test with the following failure times: $108,125,458,893,13437$ hours <br> MLE Estimates are: $\bar{\theta}=108$ <br> Substituting $\bar{\theta}$ gives the MLE for $\bar{a}$ : $\bar{a}=\frac{5}{\sum_{i=1}^{n_{F}}\left(\ln t_{i}-\ln (108)\right)}=0.8029$ <br> $90 \%$ confidence interval for $\bar{a}$ : |  |  |  ||  | $\left[\frac{\bar{a}}{10} x^{2}{ }_{[0.05]}(\theta), \quad \frac{\bar{a}}{10} x^{2}{ }_{[0.95]}(\theta)\right]$ |
| :-- | :-- |
| Characteristics | $80 / 20$ Rule. Most commonly described as the basis for the "80/20 <br> rule" (In a quality context, for example, 80\% of manufacturing <br> defects will be a result from 20\% of the causes). <br> Conditional Distribution. The conditional probability distribution <br> given that the event is greater than or equal to a value $\theta_{1}$ exceeding <br> $\theta$ is a Pareto distribution with the same index $\alpha$ but with a minimum <br> $\theta_{1}$ instead of $\theta$. <br> Types. This distribution is known as a Pareto distribution of the first <br> kind. The Pareto distribution of the second kind (not detailed here) <br> is also known as the Lomax distribution. Pareto also proposed a <br> third distribution now known as a Pareto distribution of the third <br> kind. <br> Pareto and the Lognormal Distribution. The Lognormal <br> distribution models similar physical phenomena as the Pareto <br> distribution. The two distributions have different weights at the <br> extremities. <br> Let: <br> $$
X_{i} \sim \operatorname{Pareto}\left(\theta, \alpha_{i}\right)
$$ <br> Minimum property <br> $$
\min \left\{X, X_{2}, \ldots, X_{n}\right\} \sim \operatorname{Pareto}\left(\theta, \sum_{i=1}^{n} \alpha_{i}\right)
$$ <br> For constant $\theta$. |
| :--: | :--: |
| Applications | Rare Events. The survival function 'slowly' decreases compared to <br> most life distributions which makes it suitable for modeling rare <br> events which have large outcomes. Examples include natural <br> events such as the distribution of the daily rain fall, or the size of <br> manufacturing defects. |
| Resources | Online: <br> http://mathworld.wolfram.com/ParetoDistribution.html <br> http://en.wikipedia.org/wiki/Pareto_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> Books: <br> Arnold, B., 1983. Pareto distributions, Fairland, MD: International <br> Co-operative Pub. House. <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1994. Continuous <br> Univariate Distributions, Vol. 1 2nd ed., Wiley-Interscience. || Relationship to Other Distributions |  |  |
| :--: | :--: | :--: |
| Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let <br> Then $\begin{gathered} Y \sim \operatorname{Pareto}(\theta, \alpha) \quad \text { and } \quad X=\ln (Y / \theta) \\ X \sim \operatorname{Exp}(\lambda=\alpha) \end{gathered}$ |  |
| Chi-Squared Distribution $\chi^{2}(x ; v)$ | Let <br> Then $\begin{gathered} Y \sim \operatorname{Pareto}(\theta, \alpha) \quad \text { and } \quad X=2 \alpha \ln (Y / \theta) \\ X \sim \chi^{2}(v=2) \end{gathered}$ <br> (Johnson et al. 1994, p.526) | $X=2 \alpha \ln (Y / \theta)$ |
| Logistic <br> Distribution $\operatorname{Logistic}(\mu, s)$ | Let <br> Then $\begin{gathered} X \sim \operatorname{Pareto}(\theta, \alpha) \quad \text { and } \quad Y=-\ln \left\{\left(\frac{x}{\theta}\right)^{a}-1\right\} \\ Y \sim \operatorname{Logistic}(0,1) \end{gathered}$ <br> (Hastings et al. 2000, p.127) | $Y=-\ln \left\{\left(\frac{x}{\theta}\right)^{a}-1\right\}$ |# 4.7. Triangle Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $a$ | $-\infty \leq a<b$ | Minimum Value. $a$ is the lower bound |
|  | $b$ | $a<b<\infty$ | Maximum Value. $b$ is the upper bound. |
|  | c | $a \leq c \leq b$ | Mode Value. $c$ is the mode of the distribution (top of the triangle). |
| Random Variable | $a \leq t \leq b$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(t)= \begin{cases}\frac{2(\mathrm{t}-\mathrm{a})}{(\mathrm{b}-\mathrm{a})(\mathrm{c}-\mathrm{a})} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{c} \\ \frac{2(\mathrm{~b}-\mathrm{t})}{(\mathrm{b}-\mathrm{a})(\mathrm{b}-\mathrm{c})} & \text { for } \mathrm{c} \leq \mathrm{t} \leq \mathrm{b}\end{cases}$ |  |  |
| CDF | $F(t)= \begin{cases}\frac{(\mathrm{t}-\mathrm{a})^{2}}{(\mathrm{~b}-\mathrm{a})(\mathrm{c}-\mathrm{a})} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{c} \\ 1-\frac{(\mathrm{b}-\mathrm{t})^{2}}{(\mathrm{~b}-\mathrm{a})(\mathrm{b}-\mathrm{c})} & \text { for } \mathrm{c} \leq \mathrm{t} \leq \mathrm{b}\end{cases}$ |  |  |
| Reliability | $R(t)= \begin{cases}1-\frac{(\mathrm{t}-\mathrm{a})^{2}}{(\mathrm{~b}-\mathrm{a})(\mathrm{c}-\mathrm{a})} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{c} \\ \frac{(\mathrm{b}-\mathrm{t})^{2}}{(\mathrm{~b}-\mathrm{a})(\mathrm{b}-\mathrm{c})} & \text { for } \mathrm{c} \leq \mathrm{t} \leq \mathrm{b}\end{cases}$ |  |  |
| Properties and Moments |  |  |  |
| Median | $a+\sqrt{\frac{1}{2}(b-a)(c-a)}$ for $c \geq \frac{b-a}{2}$ $b-\sqrt{\frac{1}{2}(b-a)(b-c)}$ for $c<\frac{b-a}{2}$ |  |  |
| Mode | c |  |  |
| Mean - $1^{\text {st }}$ Raw Moment | $\frac{a+b+c}{3}$ |  |  |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{a^{2}+b^{2}+c^{2}-a b-a c-b c}{18}$ |  |  |
| Skewness - $3^{\text {rd }}$ Central Moment | $\frac{\sqrt{2}(a+b-2 c)(2 a-b-c)(a-2 b+c)}{5\left(a^{2}+b^{2}+c^{2}-a b-a c-b c\right)^{3 / 2}}$ |  |  |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $\frac{-3}{5}$ |  |  || Characteristic Function | $-2 \frac{(\mathrm{~b}-\mathrm{c}) \mathrm{e}^{\mathrm{ita}}-(\mathrm{b}-\mathrm{a}) \mathrm{e}^{\mathrm{itc}}+(\mathrm{c}-\mathrm{a}) \mathrm{e}^{\mathrm{itb}}}{(\mathrm{b}-\mathrm{a})(\mathrm{c}-\mathrm{a})(\mathrm{b}-\mathrm{c}) \mathrm{t}^{2}}$ |
| :--: | :--: |
| $100 \gamma \%$ Percentile Function | $t_{\gamma}=\mathrm{a}+\sqrt{\gamma(\mathrm{b}-\mathrm{a})(\mathrm{c}-\mathrm{a})}$ for $\gamma<F(c)$ <br> $t_{\gamma}=\mathrm{b}-\sqrt{(1-\gamma)(\mathrm{b}-\mathrm{a})(\mathrm{b}-\mathrm{c})}$ for $\gamma \geq F(c)$ |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| Likelihood <br> Functions | $L(a, b, c \mid E)=\prod_{i=1}^{r} \frac{2\left(\mathrm{t}_{\mathrm{i}}-\mathrm{a}\right)}{(\mathrm{b}-\mathrm{a})(\mathrm{c}-\mathrm{a})} \prod_{i=r+1}^{\mathrm{n}_{\mathrm{F}}} \frac{2\left(\mathrm{~b}-\mathrm{t}_{\mathrm{i}}\right)}{(\mathrm{b}-\mathrm{a})(\mathrm{b}-\mathrm{c})}$ <br> $=\left(\frac{2}{\mathrm{~b}-\mathrm{a}}\right)^{n_{F}} \prod_{i=1}^{r} \frac{\mathrm{t}_{\mathrm{i}}-\mathrm{a}}{(\mathrm{c}-\mathrm{a})} \prod_{i=r+1}^{\mathrm{n}_{\mathrm{F}}} \frac{\mathrm{b}-\mathrm{t}_{\mathrm{i}}}{(\mathrm{b}-\mathrm{c})}$ <br> Where failure times are ordered: $T_{1} \leq T_{2} \leq \cdots \leq T_{r} \leq \cdots \leq T_{n_{F}}$ <br> and $r$ is the number of failure times less than $c$ and $s$ is the number of failure times greater than $c$. Therefore $n_{F}=r+s$. |
| Point <br> Estimates | The MLE estimates $\tilde{a}, \tilde{b}$, and $\tilde{c}$ are obtained by numerically calculating the likelihood function for different $r$ and selecting the maximum where $\tilde{\mathrm{c}}=\mathrm{X}_{\mathrm{F}}$. $\max _{a \leq c \leq b} L(a, b, c \mid E)=\left(\frac{2}{\mathrm{~b}-\mathrm{a}}\right)^{n_{F}}\{M(a, b, \tilde{r}(a, b)\}$ <br> where $\begin{gathered} M(a, b, r)=\prod_{i=1}^{r-1} \frac{\mathrm{t}_{\mathrm{i}}-\mathrm{a}}{\left(\mathrm{t}_{\mathrm{r}}-\mathrm{a}\right)} \prod_{i=r+1}^{\mathrm{n}_{\mathrm{F}}} \frac{\mathrm{b}-\mathrm{t}_{\mathrm{i}}}{\left(\mathrm{b}-\mathrm{t}_{\mathrm{r}}\right)} \\ r(a, b)=\underset{r \in\left\{1, \ldots, n_{F}\right\}}{\arg \max } M(a, b, r) \end{gathered}$ <br> Note that the MLE estimates for a and $b$ are not the same as the uniform distribution: $\begin{aligned} & \tilde{a} \neq \min \left(t_{1}^{F}, t_{2}^{F} \ldots\right) \\ & \tilde{b} \neq \max \left(t_{1}^{F}, t_{2}^{F} \ldots\right) \end{aligned}$ <br> (Kotz \& Dorp 2004) |
| Description, Limitations and Uses |  |
| Example | When eliciting an opinion from an expert on the possible value of a quantity, $x$, the expert may give : <br> - Lowest possible value $=0$ <br> - Highest possible value $=1$ <br> - Estimate of most likely value (mode) $=0.7$ <br> The corresponding distribution for $x$ may be a triangle distribution with parameters: $a=0, \quad b=1, \quad c=0.7$ ||  |  |
| :-- | :-- |
| Characteristics | Standard Triangle Distribution. The standard triangle distribution <br> has $a=0, b=1$. This distribution has a mean at $\sqrt{c / 2}$ and median <br> at $1-\sqrt{(1-c) / 2}$. <br> Symmetrical Triangle Distribution. The symmetrical triangle <br> distribution occurs when $c=(b-a) / 2$. The symmetrical triangle <br> distribution is formed from the average of two uniform random <br> variables (see related distributions). |
| Applications | Subjective Representation. The triangle distribution is often used <br> to model subjective evidence where $a$ and $b$ are the bounds of the <br> estimation and $c$ is an estimation of the mode. <br> Substitution to the Beta Distribution. Due to the triangle <br> distribution having bounded support it may be used in place of the <br> beta distribution. <br> Monte Carlo Simulation. Used to approximate distributions of <br> variables when the underlying distribution is unknown. A <br> distribution of interest is obtained by conducting Monte Carlo <br> simulation of a model using the triangle distributions as inputs. |
| Resources | Online: <br> http://mathworld.wolfram.com/TriangularDistribution.html <br> http://en.wikipedia.org/wiki/Triangular_distribution <br> Books: <br> Kotz, S. & Dorp, J.R.V., 2004. Beyond Beta: Other Continuous <br> Families Of Distributions With Bounded Support And Applications, <br> World Scientific Publishing Company. |
| Relationship to Other Distributions |  |
| Uniform <br> Distribution <br> Unif(t; a, b) | Let |
| Then | $\mathrm{X}_{1} \sim \operatorname{Unif}(a, b) \quad$ and $\quad \mathrm{Y}=\frac{\mathrm{X}_{1}+\mathrm{X}_{2}}{2}$ <br> Y Triangle $\left(\mathrm{a}, \frac{\mathrm{b}-\mathrm{a}}{2}, \mathrm{~b}\right)$ |
| Beta Distribution <br> Beta(t; a, $\beta$ ) | Special Cases: |
| Beta(1,2 ) = Triangle(0,0,1) <br> Beta(2,1 ) = Triangle(0,1,1) |  |# 4.8. Truncated Normal Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\mu$ | $-\infty<\mu<\infty$ | Location parameter: The mean of the distribution. |
|  | $\sigma^{2}$ | $\sigma^{2}>0$ | Scale parameter: The standard deviation of the distribution. |
|  | $a_{L}$ | $-\infty<a_{L}<b_{U}$ | Lower Bound: $a_{L}$ is the lower bound. The standard normal transform of $a_{L}$ is $z_{a}=\frac{a_{L}-\mu}{\sigma}$. |
|  | $b_{U}$ | $a_{L}<b_{U}<\infty$ | Upper Bound: $b_{U}$ is the upper bound. The standard normal transform of $b_{U}$ is $z_{b}=\frac{a_{U}-\mu}{\sigma}$. |
| Limits | $a_{L}<x \leq b_{U}$ |  |  |
| Distribution | Left Truncated Normal $x \in[0, \infty)$ |  | General Truncated Normal $x \in\left[a_{L}, b_{U}\right]$ |
| PDF | for $0 \leq x \leq \infty$ <br> $f(x)=\frac{\phi\left(\mathrm{z}_{\mathrm{x}}\right)}{\sigma \Phi\left(-\mathrm{z}_{0}\right)}$ <br> otherwise $f(x)=0$ |  | for $a_{L} \leq x \leq b_{U}$ <br> $f(x)=\frac{1}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}$ <br> otherwise $f(x)=0$ |
|  | where <br> $\phi$ is the standard normal pdf with $\mu=0$ and $\sigma^{2}=1$ <br> $\Phi$ is the standard normal cdf with $\mu=0$ and $\sigma^{2}=1$ $z_{i}=\left(\frac{i-\mu}{\sigma}\right)$ |  |  |
| CDF | for $x<0$ <br> $F(x)=0$ <br> for $0 \leq x<\infty$ <br> $F(x)=\frac{\Phi\left(\mathrm{z}_{\mathrm{x}}\right)-\Phi\left(\mathrm{z}_{0}\right)}{\Phi\left(-\mathrm{z}_{0}\right)}$ | for $x<\mathrm{a}_{\mathrm{L}}$ <br> $F(x)=0$ <br> for $a_{L} \leq x \leq b_{U}$ <br> $F(x)=\frac{\Phi\left(\mathrm{z}_{\mathrm{x}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}$ <br> for $x>\mathrm{b}_{\mathrm{U}}$ $F(x)=1$ |  |
| Reliability | for $x<0$ <br> $R(x)=1$ <br> for $0 \leq x<\infty$ <br> $R(x)=\frac{\Phi\left(\mathrm{z}_{0}\right)-\Phi\left(\mathrm{z}_{\mathrm{x}}\right)}{\Phi\left(-\mathrm{z}_{0}\right)}$ | for $x<\mathrm{a}_{\mathrm{L}}$ <br> $R(x)=1$ <br> for $a_{L} \leq x \leq b_{U}$ <br> $R(x)=\frac{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{x}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}$ <br> for $x>\mathrm{b}_{\mathrm{U}}$ $R(x)=0$ |  || Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | for $t<0$ <br> $m(x)=R(t+x)$ <br> for $0 \leq t<\infty$ <br> $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}$ <br> $=\frac{1-\Phi\left(\mathrm{z}_{\mathrm{t}+\mathrm{x}}\right)}{1-\Phi\left(\mathrm{z}_{\mathrm{t}}\right)}$ <br> $=\frac{\Phi\left(\frac{\mu-\mathrm{x}-\mathrm{t}}{\sigma}\right)}{\Phi\left(\frac{\mu-\mathrm{t}}{\sigma}\right)}$ | for $t<\mathrm{a}_{\mathrm{L}}$ <br> $m(x)=R(t+x)$ <br> for $a_{L} \leq t \leq b_{U}$ <br> $m(x)=R(x \mid t)=\frac{R(t+x)}{R(t)}$ <br> $=\frac{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{t}+\mathrm{x}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{t}}\right)}$ <br> for $t>\mathrm{b}_{\mathrm{U}}$ <br> $m(x)=0$ |
| :--: | :--: | :--: |
|  | $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. <br> Note: $x=0$ at $t$. This operation is the equivalent of $t$ replacing the lower bound. |  |
| Mean Residual Life | $u(t)=\frac{\int_{0}^{\infty} R(x) d x}{R(t)}=\frac{\int_{0}^{\infty} R(x) d x}{R(t)}$ |  |
| Hazard Rate | for $x<0$ <br> $h(x)=0$ <br> for $0 \leq x<\infty$ <br> $h(x)=\frac{\frac{1}{\sigma} \phi\left(\mathrm{z}_{\mathrm{a}}\right)\left[1-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)\right]}{\left[1-\Phi\left(\mathrm{z}_{0}\right)\right]^{2}}$ | for $x<\mathrm{a}_{\mathrm{L}}$ <br> $h(x)=0$ <br> for $a_{L} \leq x \leq b_{U}$ <br> $h(x)=\frac{\frac{1}{\sigma} \phi\left(\mathrm{z}_{\mathrm{x}}\right)\left[\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{x}}\right)\right]}{\left[\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)\right]^{2}}$ <br> for $x>\mathrm{b}_{\mathrm{U}}$ <br> $h(x)=0$ |
| Cumulative Hazard <br> Rate | $H(t)=-\ln [R(t)]$ | $H(t)=-\ln [R(t)]$ |
| Properties and <br> Moments | Left Truncated Normal $x \in[0, \infty)$ | General Truncated Normal $x \in\left[a_{L}, b_{U}\right]$ |
| Median | No closed form | No closed form |
| Mode | $\begin{gathered} \mu \text { where } \mu \geq 0 \\ 0 \text { where } \mu<0 \end{gathered}$ | $\begin{gathered} \mu \text { where } \mu \in\left[a_{L}, b_{U}\right] \\ a_{L} \text { where } \mu<a_{L} \\ b_{U} \text { where } \mu>b_{U} \end{gathered}$ |
| Mean <br> $1^{\text {st }}$ Raw Moment | $\begin{gathered} \mu+\frac{\sigma \phi\left(\mathrm{z}_{0}\right)}{\Phi\left(-\mathrm{z}_{0}\right)} \\ \text { where } \end{gathered}$ | $\begin{gathered} \mu+\sigma \frac{\phi\left(\mathrm{z}_{\mathrm{a}}\right)-\phi\left(\mathrm{z}_{\mathrm{b}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)} \\ \text { where } \end{gathered}$ |
|  | $z_{0}=\frac{-\mu}{\sigma}$ | $z_{a}=\frac{a_{L}-\mu}{\sigma}, \quad z_{b}=\frac{b_{U}-\mu}{\sigma}$ |
| Variance <br> $2^{\text {nd }}$ Central Moment | $\sigma^{2}\left[1-\left\{-\Delta_{0}\right\}^{2}-\Delta_{1}\right]$ <br> where | $\sigma^{2}\left[1-\left\{-\Delta_{0}\right\}^{2}-\Delta_{1}\right]$ ||  | $\Delta_{k}=\frac{z_{0}^{k} \phi\left(z_{0}\right)}{\Phi\left(z_{0}\right)-1}$ | $\Delta_{k}=\frac{z_{b}^{k} \phi\left(z_{b}\right)-z_{a}^{k} \phi\left(z_{a}\right)}{\Phi\left(z_{b}\right)-\Phi\left(z_{a}\right)}$ |
| :--: | :--: | :--: |
| Skewness $3^{\text {rd }}$ Central Moment | $\begin{gathered} \frac{-1}{V^{2}}[2 \Delta_{0}^{3}+\left(3 \Delta_{1}-1\right) \Delta_{0}+\Delta_{2}] \\ V=1-\Delta_{1}-\Delta_{0}^{2} \end{gathered}$ |  |
| Excess kurtosis <br> $4^{\text {th }}$ Central Moment | $\frac{1}{V^{2}}\left[-3 \Delta_{0}^{4}-6 \Delta_{1} \Delta_{0}^{2}-2 \Delta_{0}^{2}-4 \Delta_{2} \Delta_{0}-3 \Delta_{1}-\Delta_{3}+3\right]$ |  |
| Characteristic <br> Function | See (Abadir \& Magdalinos 2002, pp.1276-1287) |  |
| $100 \alpha \%$ Percentile <br> Function | $\begin{aligned} & t_{\alpha}= \\ & \mu+\sigma \Phi^{-1}\left\{\alpha+\Phi\left(\mathrm{z}_{0}\right)[1-\alpha]\right\} \end{aligned}$ | $\begin{aligned} & t_{\alpha}= \\ & \mu+\sigma \Phi^{-1}\left\{\alpha \Phi\left(\mathrm{z}_{\mathrm{b}}\right)+\Phi\left(\mathrm{z}_{\mathrm{a}}\right)[1-\alpha]\right\} \end{aligned}$ |
| Parameter Estimation |  |  |
| Maximum Likelihood Function |  |  |
| Likelihood Function | For limits $\left[a_{L}, b_{U}\right]$ : $L\left(\mu, \sigma, a_{L}, b_{U}\right)=\underbrace{\frac{1}{\left(\sigma \sqrt{2 \pi}\left\{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)\right\}\right)^{\mathrm{n}_{\mathrm{F}}}} \prod_{\text {failures }}^{\mathrm{n}_{\mathrm{F}}} \exp \left(-\frac{1}{2}\left[\frac{x_{i}-\mu}{\sigma}\right]^{2}\right)}_{\text {failures }}$ $=\underbrace{\frac{1}{\left(\sigma \sqrt{2 \pi}\left\{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)\right\}\right)^{\mathrm{n}_{\mathrm{F}}}} \exp \left(-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{\mathrm{n}_{\mathrm{F}}}\left(x_{i}-\mu\right)^{2}\right)}_{\text {failures }}$ <br> For limits $\{0, \infty)$ $\begin{aligned} L(\mu, \sigma) & =\underbrace{\frac{1}{\left(\Phi\left\{-z_{0}\right\} \sigma \sqrt{2 \pi}\right)^{\mathrm{n}_{\mathrm{F}}}} \prod_{i=1}^{\mathrm{n}_{\mathrm{F}}} \exp \left(-\frac{1}{2}\left[\frac{x_{i}-\mu}{\sigma}\right]^{2}\right)}_{\text {failures }} \\ & =\underbrace{\frac{1}{\left(\Phi\left\{-z_{0}\right\} \sigma \sqrt{2 \pi}\right)^{\mathrm{n}_{\mathrm{F}}}} \exp \left(-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{\mathrm{n}_{\mathrm{F}}}\left(x_{i}-\mu\right)^{2}\right)}_{\text {failures }}\end{aligned}$ |  |
| Log-Likelihood Function | For limits $\left[a_{L}, b_{U}\right]$ : $\Lambda\left(\mu, \sigma, a_{L}, b_{U} \mid E\right)$ <br> $=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln \left[\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)\right]-\mathrm{n}_{\mathrm{F}} \ln (\sigma \sqrt{2 \pi})-\frac{1}{2 \sigma^{2}} \sum_{\mathrm{i}=1}^{\mathrm{n}_{\mathrm{F}}}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^{2}}_{\text {failures }}$ |  |
|  | For limits $\{0, \infty)$ |  ||  | $\Lambda(\mu, \sigma \mid E)=\underbrace{-n_{F} \ln \left(\Phi\left\{-z_{0}\right\}\right)-n_{F} \ln (\sigma \sqrt{2 \pi})}_{\text {failures }}-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n_{F}}\left(x_{i}-\mu\right)^{2}$ |
| :--: | :--: |
| $\frac{\partial \Lambda}{\partial \mu}=0$ | $\frac{\partial \Lambda}{\partial \mu}=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln \left[\frac{\phi\left(\mathrm{z}_{\mathrm{a}}\right)-\phi\left(\mathrm{z}_{\mathrm{b}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}\right]+\frac{1}{\sigma^{2}} \sum_{i=1}^{n_{F}}\left(x_{i}-\mu\right)}_{\text {failures }}=0$ |
| $\frac{\partial \Lambda}{\partial \sigma}=0$ | $\frac{\partial \Lambda}{\partial \sigma}=\underbrace{-\mathrm{n}_{\mathrm{F}} \ln \left[\frac{\mathrm{z}_{\mathrm{a}} \phi\left(\mathrm{z}_{\mathrm{a}}\right)-\mathrm{z}_{\mathrm{b}} \phi\left(\mathrm{z}_{\mathrm{b}}\right)}{\Phi\left(\mathrm{z}_{\mathrm{b}}\right)-\Phi\left(\mathrm{z}_{\mathrm{a}}\right)}\right]-\frac{\mathrm{n}_{\mathrm{F}}}{\sigma}+\frac{1}{\sigma^{3}} \sum_{i=1}^{n_{F}}\left(x_{i}-\mu\right)^{2}}_{\text {failures }}=0$ |
| MLE Point Estimates | First Estimate the values for $z_{a}$ and $z_{b}$ by solving the simultaneous equations numerically (Cohen 1991, p.33): $\begin{gathered} H_{1}\left(z_{a}, z_{b}\right)=\frac{Q_{a}-Q_{b}-z_{a}}{z_{b}-z_{a}}=\frac{\bar{x}-a_{L}}{b_{U}-a_{L}} \\ H_{2}\left(z_{a}, z_{b}\right)=\frac{1+z_{a} Q_{a}-z_{b} Q_{b}-\left(Q_{a}-Q_{b}\right)^{2}}{\left(z_{b}-z_{a}\right)^{2}}=\frac{s^{2}}{\left(b_{U}-a_{L}\right)^{2}} \end{gathered}$ <br> Where: $\begin{gathered} Q_{a}=\frac{\phi\left(z_{a}\right)}{\Phi\left(z_{b}\right)-\Phi\left(z_{a}\right)}, Q_{b}=\frac{\phi\left(z_{b}\right)}{\Phi\left(z_{b}\right)-\Phi\left(z_{a}\right)} \\ z_{a}=\frac{a_{L}-\mu}{\sigma}, \quad z_{b}=\frac{b_{U}-\mu}{\sigma} \\ \bar{x}=\frac{1}{n^{F}} \sum_{0}^{n_{F}} x_{i}, \quad s^{2}=\frac{1}{n_{F}-1} \sum_{0}^{n_{F}}\left(x_{i}-\bar{x}\right)^{2} \end{gathered}$ <br> The distribution parameters can then be estimated using: $\begin{gathered} \hat{\sigma}=\frac{b_{U}-a_{L}}{\hat{z}_{b}-\hat{z}_{a}}, \quad \hat{\mu}=a_{L}-\hat{\sigma} \widehat{z_{a}} \\ \text { (Cohen 1991, p.44) provides a graphical procedure to estimate } \end{gathered}$ parameters to use as the starting point for numerical solvers. For the case where the limits are $[0, \infty)$ first numerically solve for $z_{0}$ : where $\begin{gathered} \frac{1-\mathrm{Q}_{0}\left(\mathrm{Q}_{0}-z_{0}\right)}{\left(\mathrm{Q}_{0}-z_{0}\right)^{2}}=\frac{s^{2}}{\bar{x}} \\ Q_{0}=\frac{\phi\left(z_{0}\right)}{1-\Phi\left(z_{0}\right)} \end{gathered}$ <br> The distribution parameters can be estimated using:$$
\tilde{\sigma}=\frac{\tilde{x}}{Q_{U}-\tilde{z}_{0}}, \quad \tilde{\mu}=-\tilde{\sigma} \tilde{z}_{0}
$$

When the limits $a_{L}$ and $b_{U}$ are unknown, the likelihood function is maximized when the difference, $\Phi\left(z_{b}\right)-\Phi\left(z_{a}\right)$, is at its minimum. This occurs when the difference between $b_{U}-a_{L}$ is at its minimum. Therefore the MLE estimates for $a_{L}$ and $b_{U}$ are:

$$
\begin{aligned}
& \widetilde{a_{L}}=\min \left(\mathrm{t}_{1}^{\mathrm{F}}, \mathrm{t}_{2}^{\mathrm{F}} \ldots\right) \\
& \mathrm{b}_{\mathrm{U}}=\max \left(\mathrm{t}_{1}^{\mathrm{F}}, \mathrm{t}_{2}^{\mathrm{F}} \ldots\right)
\end{aligned}
$$

| Fisher Information (Cohen 1991, p.40) | $\begin{gathered} l\left(\mu, \sigma^{2}\right)=\left[\begin{array}{ccc} \frac{1}{\sigma^{2}}\left[1-Q_{a}^{\prime}+Q_{b}^{\prime}\right] & \frac{1}{\sigma^{2}}\left[\frac{2(\tilde{x}-\mu)}{\sigma}-\lambda_{a}+\lambda_{b}\right] \\ \frac{1}{\sigma^{2}}\left[\frac{2(\tilde{x}-\mu)}{\sigma}-\lambda_{a}+\lambda_{b}\right] & \frac{1}{\sigma^{2}}\left[\frac{3\left[s^{2}+(\tilde{x}-\mu)^{2}\right]}{\sigma^{2}}-1-\eta_{a}+\eta_{b}\right] \end{array}$ |
| :--: | :--: |
|  | Where $\begin{gathered} Q_{a}^{\prime}=Q_{a}\left(Q_{a}-z_{a}\right), \quad Q_{b}^{\prime}=-Q_{b}\left(Q_{b}+z_{b}\right) \\ \lambda_{a}=a_{L} Q^{\prime}{ }_{a}+Q_{a}, \quad \lambda_{b}=b_{U} Q^{\prime}{ }_{b}+Q_{b} \\ \eta_{a}=a_{L}\left(\lambda_{a}+Q_{a}\right), \quad \eta_{b}=b_{U}\left(\lambda_{b}+Q_{b}\right) \end{gathered}$ |
| 100y\% Confidence Intervals | Calculated from the Fisher information matrix. See section 1.4.7. For further detail and examples see (Cohen 1991, p.41) |
| Bayesian |  |
| No closed form solutions to priors exist. |  |
| Description, Limitations and Uses |  |
| Example 1 | The size of washers delivered from a manufacturer is desired to be modeled. The manufacture has already removed all washers below 15.95 mm and washers above 16.05 mm . The washers received have the following diameters: $\begin{aligned} & \text { 15.976, 15.970, 15.955, 16.007, 15.966, 15.952, } 15.955 \mathrm{~mm} \\ & \text { From data: } \end{aligned}$ $\begin{gathered} \tilde{x}=15.973, \quad s^{2}=4.3950 E-4 \\ \text { Using numerical solver MLE Estimates for } z_{a} \text { and } z_{b} \text { are: } \end{gathered}$ $\begin{gathered} \widetilde{z_{a}}=0, \quad \widetilde{z_{b}}=3.3351 \\ \text { Therefore } \end{gathered}$ $\begin{gathered} \tilde{\sigma}=\frac{b_{U}-a_{L}}{\widetilde{z_{b}}-\widetilde{z_{a}}}=0.029984 \\ \tilde{\mu}=a_{L}-\tilde{\sigma} \widetilde{z_{a}}=15.95 \end{gathered}$ <br> To calculate confidence intervals, first calculate: |$$
\begin{array}{rlrl}
Q_{a}^{\prime} & =0.63771, & Q_{b}^{\prime} & =-0.010246 \\
\lambda_{a} & =10.970, & \lambda_{b} & =-0.16138 \\
\eta_{a} & =187.71, & \eta_{b} & =-2.54087
\end{array}
$$

90\% confidence intervals:

$$
I(\mu, \sigma)=\left[\begin{array}{cc}
391.57 & -10699 \\
-10699 & -209183
\end{array}\right]
$$

$$
\left[J_{n}(\hat{\mu}, \hat{\sigma})\right]^{-1}=\left[n_{F} I(\hat{\mu}, \hat{\sigma})\right]^{-1}=\left[\begin{array}{cc}
1.1835 E-4 & -6.0535 E-6 \\
-6.0535 E-6 & -2.2154 E-7
\end{array}\right]
$$

90\% confidence interval for $\mu$ :

$$
\left[\hat{\mu}-\Phi^{-1}(0.95) \sqrt{1.1835 E-4}, \quad \hat{\mu}+\Phi^{-1}(0.95) \sqrt{1.1835 E-4}\right]
$$

$[15.932,15.968]$
90\% confidence interval for $\sigma$ :
$\left[\hat{\sigma} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{2.2154 E-7}}{-\hat{\sigma}}\right), \quad \hat{\sigma} \cdot \exp \left(\frac{\Phi^{-1}(0.95) \sqrt{2.2154 E-7}}{\hat{\sigma}}\right)\right]$
$[2.922 E-2, \quad 3.0769 E-2]$
An estimate can be made on how many washers the manufacturer discards:

The distribution of washer sizes is a Normal Distribution with estimated parameters $\hat{\mu}=15.95, \hat{\sigma}=0.029984$. The percentage of washers wish pass quality control is:

$$
F(16.05)-F(15.95)=49.96 \%
$$

It is likely that there is too much variance in the manufacturing process for this system to be efficient.

| Example 2 | The following example adjusts the calculations used in the Normal Distribution to account for the fact that the limit on distance is $[0, \infty)$. <br> The accuracy of a cutting machine used in manufacturing is desired to be measured. 5 cuts at the required length are made and measured as: <br> $7.436,10.270,10.466,11.039,11.854 \mathrm{~mm}$ |
| :--: | :--: |
| From data: | $\bar{x}=10.213, \quad s^{2}=2.789$ |
| Using numerical solver MLE Estimates for $z_{0}$ is: |  |
|  | $\bar{z}_{0}=-4.5062$ |
| Therefore | $\hat{\sigma}=\frac{\bar{x}}{Q_{0}-\bar{z}_{0}}=2.26643$ |$$
\hat{\mu}=-\hat{\sigma} \overrightarrow{x_{a}}=10.213
$$

To calculate confidence intervals, first calculate:

$$
Q_{0}^{*}=7.0042 E-5, \quad \lambda_{0}=1.5543 E-5, \quad \lambda_{b}=-0.16138
$$

90\% confidence intervals:

$$
\begin{gathered}
I(\mu, \sigma)=\left[\begin{array}{cc}
0.19466 & -2.9453 E-6 \\
-2.9453 E-6 & 0.12237
\end{array}\right] \\
{\left[J_{n}(\hat{\mu}, \hat{\sigma})\right]^{-1}=\left[n_{F} I(\hat{\mu}, \hat{\sigma})\right]^{-1}=\left[\begin{array}{cc}
1.0274 & 2.4728 E-5 \\
2.4728 E-5 & 1.6343
\end{array}\right]}
\end{gathered}
$$

90\% confidence interval for $\mu$ :

$$
\left[\hat{\mu}-\Phi^{-1}(0.95) \sqrt{1.0274}, \quad \hat{\mu}+\Phi^{-1}(0.95) \sqrt{1.0274}\right]
$$

$[8.546,11.88]$
90\% confidence interval for $\sigma$ :

$$
\left[\hat{\sigma} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{1.6343}}{-\hat{\sigma}}\right\}, \hat{\sigma} \cdot \exp \left\{\frac{\Phi^{-1}(0.95) \sqrt{1.6343}}{\hat{\sigma}}\right\}\right]
$$

To compare these results to a non-truncated normal distribution:

|  | $90 \%$ Lower CI | Point Est | $90 \%$ Upper CI |
| :-- | :-- | :-- | :-- |
| Norm $-\mu$ <br> Classical | 10.163 | 10.213 | 10.262 |
| Norm $-\sigma^{2}$ <br> Classical | 1.176 | 2.789 | 15.697 |
| Norm $-\mu$ <br> Bayesian | 8.761 | 10.213 | 11.665 |
| Norm $-\sigma^{2}$ <br> Bayesian | 0.886 | 2.789 | 6.822 |
| TNorm $-\mu$ | 8.546 | 10.213 | 11.88 |
| TNorm $-\sigma^{2}$ | 0.80317 | 5.1367 | 32.856 |

*Note: The TNorm $\sigma$ estimate and interval are squared.
The truncated normal produced results which had a wider confidence in the parameter estimates, however the point estimates were within each others confidence intervals. In this case the truncation correction might be ignored for ease of calculation.

Characteristics
For large $\mu / \sigma$ truncation may have negligible affect. In this case the use the Normal Continuous Distribution as an approximation.

Let:

$$
\mathrm{X} \sim T \operatorname{Norm}\left(\mu, \sigma^{2}\right) \text { where } X \in[a, b]
$$

Convolution Property. The sum of truncated normal distribution random variables is not a truncated normal distribution. When truncation is symmetrical about the mean the sum of truncated|  | normal distribution random variables is well approximated using: $Y=\sum_{i=1}^{n} X_{i}$ where $\frac{b_{i}-a_{i}}{2}=\mu_{i}$ <br> $Y \approx T \operatorname{Norm}\left(\sum \mu_{i}, \sum \operatorname{Var}\left(X_{i}\right)\right) \quad$ where $Y \in\left[\sum a_{i}, \sum b_{i}\right]$ <br> Linear Transformation Property (Cozman \& Krotkov 1997) $Y=c X+d$ <br> $Y \sim T \operatorname{Norm}\left(c \mu+d, d^{2} \sigma^{2}\right)$ where $Y \in[c a+d, c b+d]$ |
| :--: | :--: |
| Applications | Life Distribution. When used as a life distribution a truncated Normal Distribution may be used due to the constraint t≥0. However it is often found that the difference in results is negligible. (Rausand \& Høyland 2004) <br> Repair Time Distributions. The truncated normal distribution may be used to model simple repair or inspection tasks that have a typical duration with little variation using the limits $[0, \infty)$ <br> Failures After Pre-test Screening. When a customer receives a product from a vendor, the product may have already been subject to burn-in testing. The customer will not know the number of failures which occurred during the burn-in, but may know the duration. As such the failure distribution is left truncated. (Meeker \& Escobar 1998, p.269) <br> Flaws under the inspection threshold. When a flaw is not detected due to the flaw's amplitude being less than the inspection threshold the distribution is left truncated. (Meeker \& Escobar 1998, p.266) <br> Worst Case Measurements. Sometimes only the worst performers from a population are monitored and have data collected. Therefore the threshold which determined that the item be monitored is the truncation limit. (Meeker \& Escobar 1998, p.267) <br> Screening Out Units With Large Defects. In quality control processes it may be common to remove defects which exceed a limit. The remaining population of defects delivered to the customer has a right truncated distribution. (Meeker \& Escobar 1998, p.270) |
| Resources | Online: <br> http://en.wikipedia.org/wiki/Truncated_normal_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> http://www.ntrand.com/truncated-normal-distribution/ ||  | Books: <br> Cohen, 1991. Truncated and Censored Samples 1st ed., CRC <br> Press. <br> Patel, J.K. \& Read, C.B., 1996. Handbook of the Normal <br> Distribution 2nd ed., CRC. <br> Schneider, H., 1986. Truncated and censored samples from normal <br> populations, M. Dekker. |
| :-- | :-- |

# Relationship to Other Distributions 

| Normal <br> Distribution <br> Norm $\left(x ; \mu, \sigma^{2}\right)$ | Let: <br> Then: | $X \sim \operatorname{Norm}\left(\mu, \sigma^{2}\right)$ <br> $X \in(\infty, \infty)$ <br> $Y \sim \uparrow \operatorname{Norm}\left(\mu, \sigma^{2}, a_{L}, b_{U}\right)$ <br> $Y \in\left[a_{L}, b_{U}\right]$ |
| :--: | :--: | :--: |

For further relationships see Normal Continuous Distribution# 4.9. Uniform Continuous Distribution 

Probability Density Function - $f(t)$


Cumulative Density Function - $F(t)$


Hazard Rate - $h(t)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $a$ | $0 \leq a<b$ | Minimum Value. $a$ is the lower bound of the uniform distribution. |
|  | $b$ | $a<b<\infty$ | Maximum Value. $b$ is the upper bound of the uniform distribution. |
| Random Variable | $a \leq t \leq b$ |  |  |
| Distribution | Time Domain |  | Laplace |
| PDF | $\begin{aligned} f(t) & =\left\{\begin{array}{ll}\frac{1}{\mathrm{~b}-\mathrm{a}} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{b} \\ 0 & \text { otherwise }\end{array}\right. \\ & =\frac{1}{\mathrm{~b}-\mathrm{a}}\{u(t-a)-u(t-b)\} \end{aligned}$ <br> Where $u(t-a)$ is the Heaviside step function. |  | $f(s)=\frac{e^{-a s}-e^{-b s}}{s(b-a)}$ |
| CDF | $\begin{aligned} F(t) & =\left\{\begin{array}{ll}0 & \text { for } t<a \\ \frac{1}{\mathrm{~b}-\mathrm{a}} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{b} \\ 1 & \text { for } \mathrm{t}>b\end{array}\right. \\ & =\frac{\mathrm{t}-\mathrm{a}}{\mathrm{~b}-\mathrm{a}}\{u(t-a)-u(t-b)\} \\ & +u(t-b) \end{aligned}$ |  | $F(s)=\frac{e^{-a s}-e^{-b s}}{s^{2}(b-a)}$ |
| Reliability | $R(t)=\left\{\begin{array}{ll}1 & \text { for } t<a \\ \frac{\mathrm{b}-\mathrm{t}}{\mathrm{~b}-\mathrm{a}} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{b} \\ 0 & \text { for } \mathrm{t}>b\end{array}\right.$ |  | $R(s)=\frac{e^{-b s}-e^{-a s}}{s^{2}(b-a)}+\frac{1}{s}$ |
| Conditional <br> Survivor Function $P(T>x+t \mid T>t)$ | For $t<a$ : $\begin{aligned} & m(x)=\frac{R(t+x)}{R(t)}= \\ & m(x)=\frac{R(t+x)}{R(t)}= \end{aligned}$ <br> For $t>b$ : | $\begin{aligned} & 1 \\ & \frac{\mathrm{~b}-(\mathrm{t}+\mathrm{x})}{0} \end{aligned}$ | $\begin{aligned} & \text { for } \mathrm{t}+\mathrm{x}<a \\ & \text { for } \mathrm{a} \leq \mathrm{t}+\mathrm{x} \leq \mathrm{b} \\ & \text { for } \mathrm{t}+\mathrm{x}>b \end{aligned}$ |
|  | Where $t$ is the given time we know the component has survived to. $x$ is a random variable defined as the time after $t$. Note: $x=0$ at $t$. |  |  |
| Mean Residual Life | For $t<a$ : <br> For $a \leq t \leq b$ : | $\begin{gathered} u(t)=\frac{1}{2}(a+b)-t \\ u(t)=a-t-\frac{(a-b)^{2}}{2(t-b)} \end{gathered}$ |  ||  | For $t>b$ : $u(t)=0$ |
| :--: | :--: |
| Hazard Rate | $h(t)=\left\{\begin{array}{ll}\frac{1}{\mathrm{~b}-\mathrm{t}} & \text { for } \mathrm{a} \leq \mathrm{t} \leq \mathrm{b} \\ 0 & \text { otherwise }\end{array}\right.$ |
| Cumulative <br> Hazard Rate | $H(t)=\left\{\begin{array}{ll}0 & \text { for } t<a \\ -\ln \left(\frac{b-t}{b-a}\right) & \text { for } a \leq t \leq b \\ \infty & \text { for } t>b\end{array}\right.$ |
| Properties and Moments |  |
| Median | $\frac{1}{2}(a+b)$ |
| Mode | Any value between $a$ and $b$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\frac{1}{2}(a+b)$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\frac{1}{12}(b-a)^{2}$ |
| Skewness - $3^{\text {rd }}$ Central Moment | 0 |
| Excess kurtosis - $4^{\text {th }}$ Central Moment | $-\frac{b}{5}$ |
| Characteristic Function | $\frac{\mathrm{e}^{\mathrm{itb}}-\mathrm{e}^{\mathrm{ita}}}{\mathrm{it}(\mathrm{b}-\mathrm{a})}$ |
| 100a\% Percentile Function | $t_{\alpha}=\alpha(\mathrm{b}-\mathrm{a})+\mathrm{a}$ |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| Likelihood <br> Functions | $L(a, b \mid E)=\underbrace{\left(\frac{1}{b-a}\right)^{n_{p}}}_{\text {failures }} \cdot \underbrace{\prod_{i=1}^{n_{5}}\left(\frac{b-t_{i}^{a}}{b-a}\right)}_{\text {survivors }} \cdot \underbrace{\prod_{i=1}^{n_{i}}\left(1+\frac{t_{i}^{\mathrm{RI}}-t_{i}^{\mathrm{LI}}}{b-a}\right)}_{\text {interval failures }}$ <br> This assumes that all times are within the bound a, b. <br> When there is only complete failure data: $\begin{aligned} L(a, b \mid E) & =\left(\frac{1}{b-a}\right)^{n_{p}} \\ a & \leq t_{i} \leq b \end{aligned}$ |
| Point <br> Estimates | The likelihood function is maximized when a is large, b is small with the restriction that all times are between a and b. Thus: $\begin{aligned} & \hat{a}=\min \left(t_{1}^{p}, t_{2}^{p} \ldots\right) \\ & \hat{b}=\max \left(t_{1}^{p}, t_{2}^{p} \ldots\right) \end{aligned}$ ||  | When $a=0$ and $b$ is estimated with complete data the following estimates may be used where $t_{\max }=\max \left(\mathrm{t}_{1}^{\mathrm{F}}, \mathrm{t}_{2}^{\mathrm{F}} \ldots \mathrm{t}_{n}^{\mathrm{F}}\right)$. (Johnson et al. 1995, p.286) <br> 1. MLE. $\quad \hat{\mathrm{b}}=\frac{t_{\max }}{n}$ <br> 2. Min Mean Square Error. $\quad \hat{\mathrm{b}}=\frac{\mathrm{n}+1}{\mathrm{n}+1} \mathrm{t}_{\max }$ <br> 3. Unbiased Estimator. $\quad \hat{\mathrm{b}}=\frac{\mathrm{n}+1}{\mathrm{n}} t_{\max }$ <br> 4. Closest Estimator. $\quad \hat{\mathrm{b}}=2^{1 / n} t_{\max }$ <br> Procedures for parameter estimating when there is censored data is detailed in (Johnson et al. 1995, p.286) |
| :--: | :--: |
| Fisher <br> Information | $I(a, b)=\left[\frac{-1}{(a-b)^{2}} \frac{1}{(a-b)^{2}}\right]$ <br> $\left[\frac{1}{(a-b)^{2}} \frac{-1}{(a-b)^{2}}\right]$ |
| Bayesian |  |

The Uniform distribution is widely used in Bayesian methods as a non-informative prior or to model evidence which only suggests bounds on the parameter.

Non-informative Prior. The Uniform distribution can be used as a non-informative prior. As can be seen below, the only affect the uniform prior has on Bayes equation is to limit the range of the parameter for which the denominator integrates over.

$$
\pi(\theta \mid E)=\frac{L(E \mid \theta)\left(\frac{1}{b-a}\right)}{\int_{a}^{b} L(E \mid \theta)\left(\frac{1}{b-a}\right) d \theta}=\frac{L(E \mid \theta)}{\int_{a}^{b} L(E \mid \theta) d \theta}
$$

Parameter Bounds. This type of distribution allows an easy method to mathematically model soft data where only the parameter bounds can be estimated. An example is where uniform distribution can model a person's opinion on the value $\theta$ where they know that it could not be lower than $a$ or greater than $b$, but is unsure of any particular value $\theta$ could take.

| Non-informative Priors |  |
| :-- | :-- |
| Jeffrey's Prior | $\frac{1}{a-b}$ |
| Description, Limitations and Uses |  |
| Example | For an example of the uniform distribution being used in Bayesian <br> updating as a prior, Beta(1,1) see the binomial distribution. <br> Given the following data calculate the MLE parameter estimates: <br> $240,585,223,751,255$ <br> $\tilde{a}=223$ ||  | $\hat{b}=751$ |
| :--: | :--: |
| Characteristics | The Uniform distribution is a special case of the Beta distribution when $\alpha=\beta=1$. <br> The uniform distribution has an increasing failure rate with $\lim _{t \rightarrow b} h(t)=\infty$. <br> The Standard Uniform Distribution has parameters $a=0$ and $b=1$. This results in $f(t)=1$ for $a \leq t \leq b$ and 0 otherwise. $T \sim \operatorname{Unif}(a, b)$ <br> Uniformity Property <br> If $t>a$ and $t+\Delta<b$ then: $P(t \rightarrow t+\Delta)=\int_{t}^{t+\Delta} \frac{1}{b-a} d x=\frac{\Delta}{b-a}$ <br> The probability that a random variable falls within any interval of fixed length is independent of the location, $t$, and is only dependent on the interval size, $\Delta$. <br> Variate Generation Property $F^{-1}(u)=u(b-a)+a$ <br> Residual Property <br> If k is a real constant where $a<k<b$ then: $\operatorname{Pr}(T \mid T>k) \sim \operatorname{Unif}(a=k, b)$ |
| Applications | Random Number Generator. The uniform distribution is widely used as the basis for the generation of random numbers for other statistical distributions. The random uniform values are mapped to the desired distribution by solving the inverse cdf. <br> Bayesian Inference. The uniform distribution can be used ss a non-informative prior and to model soft evidence. <br> Special Case of Beta Distribution. In applications like Bayesian statistics the uniform distribution is used as an uninformative prior by using a beta distribution of $\alpha=\beta=1$. |
| Resources | Online: <br> http://mathworld.wolfram.com/UniformDistribution.html <br> http://en.wikipedia.org/wiki/Uniform_distribution_(continuous) <br> http://socr.ucla.edu/htm/s/SOCR_Distributions.html (web calc) <br> Books: <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1995. Continuous Univariate Distributions, Vol. 2 2nd ed., Wiley-Interscience. |
| Relationship to Other Distributions |  |
| Beta Distribution | Let || $\operatorname{Beta}(t ; a, \beta, a, b)$ | $\mathrm{X}_{1} \sim \operatorname{Unif}(0,1) \quad$ and $\quad \mathrm{X}_{1} \leq \mathrm{X}_{2} \leq \cdots \leq \mathrm{X}_{\mathrm{n}}$ <br> Then <br> Where $n$ and $k$ are integers. <br> Special Case: $\quad$ Beta $(t ; a, b \mid \alpha=1, \beta=1)=\operatorname{Unif}(t ; a, b)$ |
| :--: | :--: |
| Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let $\quad X \sim \operatorname{Exp}(\lambda) \quad$ and $\quad \mathrm{Y}=\exp (-\lambda X)$ <br> Then $\quad Y \sim \operatorname{Unif}(0,1)$ |# 5. Univariate Discrete Distributions# 5.1. Bernoulli Discrete Distribution 

| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $p$ | $0 \leq p \leq 1$ | Bernoulli probability parameter. <br> Probability of success. |
| Random Variable | $k \in\{0,1\}$ |  |  |
| Question | The probability of getting exactly $k$ ( 0 or 1 ) successes in 1 trial with probability p. |  |  |
| Distribution | Formulas |  |  |
| PDF | $\begin{aligned} f(k) & =\mathrm{p}^{\mathrm{k}}(1-\mathrm{p})^{1-\mathrm{k}} \\ & = \begin{cases}1-\mathrm{p} & \text { for } \mathrm{k}=0 \\ \mathrm{p} & \text { for } \mathrm{k}=1\end{cases} \end{aligned}$ |  |  |
| CDF | $\begin{aligned} F(k) & =(1-\mathrm{p})^{1-\mathrm{k}} \\ & = \begin{cases}1-\mathrm{p} & \text { for } \mathrm{k}=0 \\ 1 & \text { for } \mathrm{k}=1\end{cases} \end{aligned}$ |  |  |
| Reliability | $\begin{aligned} F(k) & =1-(1-\mathrm{p})^{1-\mathrm{k}} \\ & = \begin{cases}\mathrm{p} & \text { for } \mathrm{k}=0 \\ 0 & \text { for } \mathrm{k}=1\end{cases} \end{aligned}$ |  |  |
| Hazard Rate | $h(k)= \begin{cases}1-\mathrm{p} & \text { for } \mathrm{k}=0 \\ 1 & \text { for } \mathrm{k}=1\end{cases}$ |  |  |
| Properties and Moments |  |  |  |
| Mode |  | $\begin{gathered} k_{0.5}=\|p\| \text { when } p \neq 0.5 \\ k_{0.5}=\{0,1\} \text { when } p=0.5 \end{gathered}$ |  |  |
| Mean - $1^{\text {st }}$ Raw Moment |  | $p$ |  |
| Variance - $2^{\text {nd }}$ Central Moment |  | $p(1-p)$ |  |
| Skewness - $3^{\text {rd }}$ Central Moment |  | $\frac{q-p}{\sqrt{p q}}$ where $q=(1-p)$ |  |
| Excess kurtosis - $4^{\text {th }}$ Central Moment |  | $\frac{6 p^{2}-6 p+1}{p(1-p)}$ |  |
| Characteristic Function |  | $(1-\mathrm{p})+\mathrm{pe}^{\text {it }}$ |  |
| Parameter Estimation |  |  |  |
| Maximum Likelihood Function |  |  |  |
| Likelihood <br> Function | $L(p \mid E)=p^{\sum k_{i}}(1-p)^{n-\sum k_{i}}$ <br> where $n$ is the number of Bernoulli trials $k_{i} \in\{0,1\}$, and $\sum k_{i}=\sum_{i=1}^{n} k_{i}$ |  |  || $\frac{d \mathrm{~L}}{d \mathrm{p}}=0$ | solve for $p$ <br> $\frac{d \mathrm{~L}}{d \mathrm{p}}=\sum \mathrm{k} \cdot \mathrm{p}^{\sum\left(\mathrm{k}_{\mathrm{i}}\right)-1}(1-\mathrm{p})^{\mathrm{n}-\sum \mathrm{k}_{\mathrm{i}}}-(\mathrm{n}-\sum \mathrm{k}) \mathrm{p}^{\sum \mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{\mathrm{n}-1-\sum \mathrm{k}_{\mathrm{i}}}=0$ <br> $\sum \mathrm{k} \cdot \mathrm{p}^{\sum\left(\mathrm{k}_{\mathrm{i}}\right)-1}(1-\mathrm{p})^{\mathrm{n}-\sum \mathrm{k}_{\mathrm{i}}}=\left(\mathrm{n}-\sum \mathrm{k}_{\mathrm{i}}\right) \mathrm{p}^{\sum \mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{\mathrm{n}-1-\sum \mathrm{k}_{\mathrm{i}}}$ <br> $\sum \mathrm{k}_{\mathrm{i}} \cdot \mathrm{p}^{-1}=\left(\mathrm{n}-\sum \mathrm{k}_{\mathrm{i}}\right)(1-\mathrm{p})^{-1}$ <br> $\frac{(1-\mathrm{p})}{\mathrm{p}}=\frac{\mathrm{n}-\sum \mathrm{k}_{\mathrm{i}}}{\sum \mathrm{k}_{\mathrm{i}}}$ <br> $\mathrm{p}=\frac{\sum \mathrm{k}_{\mathrm{i}}}{\mathrm{n}}$ |
| :--: | :--: |
| Fisher Information | $I(p)=\frac{1}{p(1-p)}$ |
| MLE Point Estimates | The MLE point estimate for p : $\hat{\mathrm{p}}=\frac{\sum \mathrm{k}}{\mathrm{n}}$ |
| Fisher Information | $I(p)=\frac{1}{p(1-p)}$ |
| Confidence Intervals | See discussion in binomial distribution. |
| Bayesian |  |
| Non-informative Priors for $\mathbf{p}, \boldsymbol{\pi}(\boldsymbol{p})$ <br> (Yang and Berger 1998, p.6) |  |
| Type | Prior | Posterior |
| Uniform Proper <br> Prior with limits $p \in[a, b]$ | $\frac{1}{b-a}$ | Truncated Beta Distribution <br> For $\mathrm{a} \leq p \leq \mathrm{b}$ <br> $c . B e t a(p ; 1+k, 2-k)$ <br> Otherwise $\pi(p)=0$ |
| Uniform Improper <br> Proir with limits $p \in[0,1]$ | $1=\operatorname{Beta}(p ; 1,1)$ | $\operatorname{Beta}(p ; 1+k, 2-k)$ |
| Jeffrey's Prior <br> Reference Prior | $\frac{1}{\sqrt{p(1-p)}}=\operatorname{Beta}\left(p ; \frac{1}{2} \cdot \frac{1}{2}\right)$ | $\begin{gathered} \operatorname{Beta}\left(p ; \frac{1}{2}+k, 1.5-k\right) \\ \text { when } p \in[0,1] \end{gathered}$ |
| MDIP | $1.6186 p^{p}(1-p)^{1-p}$ | Proper - No Closed Form |
| Novick and Hall | $p^{-1}(1-p)^{-1}=\operatorname{Beta}(0,0)$ | $\begin{gathered} \operatorname{Beta}(p ; k, 1-k) \\ \text { when } p \in[0,1] \end{gathered}$ || Conjugate Priors |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| UOI | Likelihood <br> Model | Evidence | Dist of UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} p \\ \text { from } \\ \text { Bernoulli }(k ; p) \end{gathered}$ | Bernoulli | $k$ failures in 1 trail | Beta | $\alpha_{0}, \beta_{0}$ | $\alpha=\alpha_{o}+k$ <br> $\beta=\beta_{o}+1-k$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | When a demand is placed on a machine it undergoes a Bernoulli trial with success defined as a successful start. It is known the probability of a successful start, $p$, equals 0.8 . Therefore the probability the machine does not start. $f(0)=0.2$. <br> For an example with multiple Bernoulli trials see the binomial distribution. |  |  |  |  |
| Characteristics | A Bernoulli process is a probabilistic experiment that can have one of two outcomes, success $(k=1)$ with the probability of success is $p$, and failure $(k=0)$ with the probability of failure is $q \equiv 1-p$. <br> Single Trial. It's important to emphasis that the Bernoulli distribution is for a single trial or event. The case of multiple Bernoulli trials with replacement is the binomial distribution. The case of multiple Bernoulli trials without replacement is the hypergeometric distribution. <br> Maximum Property $\max \left\{K_{1}, K_{2}, \ldots, K_{n}\right\} \sim \operatorname{Bernoulli}\left(k ; p=1-\Pi\left[1-p_{i}\right]\right)$ <br> Minimum property $\min \left\{K_{1}, K_{2}, \ldots, K_{n}\right\} \sim \operatorname{Bernoulli}\left(k ; p=\Pi p_{i}\right)$ <br> Product Property $\prod_{i=1}^{n} \mathrm{~K}_{\mathrm{i}} \sim \operatorname{Bernoulli}\left(\Pi k ; p=\Pi p_{i}\right)$ |  |  |  |  |
| Applications | Used to model a single event which have only two outcomes. In reliability engineering it is most often used to model demands or shocks to a component where the component will fail with probability $p$. <br> In practice it is rare for only a single event to be considered and so a binomial distribution is most often used (with the assumption of replacement). The conditions and assumptions of a Bernoulli trial however are used as the basis for each trial in a binomial distribution. See 'Related Distributions' and binomial distribution for more details. |  |  |  |  || Resources | Online: <br> http://mathworld.wolfram.com/BernoulliDistribution.html <br> http://en.wikipedia.org/wiki/Bernoulli_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) |
| :-- | :-- |
| Books: |  |
| Collani, E.V. \& Dräger, K., 2001. Binomial distribution handbook for <br> scientists and engineers, Birkhäuser. |  |
| Johnson, N.L., Kemp, A.W. \& Kotz, S., 2005. Univariate Discrete <br> Distributions 3rd ed., Wiley-Interscience. |  |

# Relationship to Other Distributions 

The Binomial distribution counts the number of successes in $n$ independent observations of a Bernoulli process.

Let

$$
K_{i} \sim \operatorname{Bernoulli}\left(\mathrm{k}_{\mathrm{i}} ; \mathrm{p}\right) \quad \text { and } \quad Y=\sum_{i=1}^{n} K_{i}
$$

Then

$$
\mathrm{Y} \sim \operatorname{Binom}\left(\mathrm{k}^{\prime}=\sum_{\mathrm{k}_{\mathrm{i}}} \mid \mathrm{n}, \mathrm{p}\right) \quad \text { where } k^{\prime} \in\{1,2, \ldots, n\}
$$

Special Case:

$$
\operatorname{Bernoulli}(\mathrm{k} ; \mathrm{p})=\operatorname{Binom}(\mathrm{k} ; \mathrm{p} \mid \mathrm{n}=1)
$$# 5.2. Binomial Discrete Distribution 

Probability Density Function - $f(k)$


Cumulative Density Function - $F(k)$


Hazard Rate - $h(k)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | n | $n \in\{1,2 \ldots, \infty\}$ | Number of Trials. |
|  | $p$ | $0 \leq p \leq 1$ | Bernoulli probability parameter. <br> Probability of success in a single <br> trial. |
| Random Variable | $k \in\{0,1,2 \ldots, n\}$ |  |  |
| Question | The probability of getting exactly $k$ successes in $n$ trials. |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(k)=\binom{n}{k} p^{k}(1-p)^{n-k}$ <br> where k combinations from n : $\left.\binom{n}{k}_{n}={ }_{n} C_{k}=C_{k}^{n}=\frac{n!}{k!(n-k)!}=\frac{n}{k} C_{k-1}^{n-1}\right.$ |  |  |
| CDF | $F(k)$ <br> $F(k)$ <br> $=l_{1-p}(n-k, k+1)$ <br> where $I_{p}(a, b)$ is the Regularized Incomplete Beta function. See <br> section 1.6.3. <br> When $n \geq 20$ and $p \leq 0.05$, or if $n \geq 100$ and $n p \leq 10$, this can <br> be approximated by a Poisson distribution with $\mu=n p$ : <br> When $n p \geq 10$ and $n p(1-p) \geq 10$ then the cdf can be <br> approximated using a normal distribution: $F(k) \cong \Phi\left(\frac{k+0.5-n p}{\sqrt{n p(1-p)}}\right)$ |  |  |
| Reliability | $R(k)$ <br> $=\sum_{j=0}^{k} \frac{n!}{j!(n-j)!} p^{j}(1-p)^{n-j}$ <br> $=\sum_{j=k+1}^{n} \frac{n!}{j!(n-j)!} p^{j}(1-p)^{n-j}$ <br> $=I_{p}(k+1, n-k)$ <br> where $I_{p}(a, b)$ is the Regularized Incomplete Beta function. See <br> section 1.6.3. |  |  || Hazard Rate |  |  |
| :--: | :--: | :--: |
| Properties and Moments |  |  |
| Median |  | $k_{\theta, \mathrm{S}}$ is either $\{[n p],\lceil n p\rceil\}$ |
| Mode |  | $[(n+1) p]$ |
| Mean - $1^{\text {st }}$ Raw Moment |  | $n p$ |
| Variance - $2^{\text {nd }}$ Central Moment |  | $n p(1-p)$ |
| Skewness - $3^{\text {rd }}$ Central Moment |  | $\frac{1-2 \mathrm{p}}{\sqrt{n \mathrm{p}(1-\mathrm{p})}}$ |
| Excess kurtosis - $4^{\text {th }}$ Central Moment |  | $\frac{6 \mathrm{p}^{2}-6 \mathrm{p}+1}{\mathrm{np}(1-\mathrm{p})}$ |
| Characteristic Function |  | $\left(1-\mathrm{p}+\mathrm{pe}^{\mathrm{it}}\right)^{\mathrm{n}}$ |
| 100a\% Percentile Function |  | Numerically solve for $k$ (which is not arduous for $n \leq 10$ ):

$k_{\alpha}=F^{-1}(n, p)$
For $n p \geq 10$ and $n p(1-p) \geq 10$ the normal approximation may be used:

$$
\mathrm{k}_{\alpha} \cong\left[\Phi^{-1}(\alpha) \sqrt{n p(1-p)}+n p-0.5\right]
$$

# Parameter Estimation 

Maximum Likelihood Function

| Likelihood <br> Function | For complete data only: $L(p \mid E)=\prod_{\substack{i=1 \\ i=1}}^{\mathrm{n}_{\mathrm{B}}}\left(\mathrm{~n}_{\mathrm{i}}\right) \mathrm{p}^{\mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{\mathrm{n}_{\mathrm{i}}-\mathrm{k}_{\mathrm{i}}}$ <br> $=\mathrm{p}^{\sum \mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}}$ |
| :--: | :--: | :--: |
|  | Where $n_{B}$ is the number of Binomial processes, $\sum k_{i}=\sum_{i=1}^{n_{B}} k_{i}$, $\sum n_{i}=\sum_{i=1}^{n_{B}} n_{i}$ and the combinatory term is ignored (see section 1.1.6 for discussion). |  || $\frac{d \mathrm{~L}}{d \mathrm{p}}=0$ | solve for $p$ <br> $\frac{d \mathrm{~L}}{d \mathrm{p}}=\sum \mathrm{k}_{\mathrm{i}} \cdot \mathrm{p}^{\sum\left(\mathrm{k}_{\mathrm{i}}\right)-1}(1-\mathrm{p})^{\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}}-\left(\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}\right) \mathrm{p}^{\sum \mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{\sum \mathrm{n}_{\mathrm{i}}-1-\sum \mathrm{k}_{\mathrm{i}}}$ <br> $\sum \mathrm{k}_{\mathrm{i}} \cdot \mathrm{p}^{\sum\left(\mathrm{k}_{\mathrm{i}}\right)-1}(1-\mathrm{p})^{\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}}=\left(\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}\right) \mathrm{p}^{\sum \mathrm{k}_{\mathrm{i}}}(1-\mathrm{p})^{-1+\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}}$ <br> $\sum \mathrm{k}_{\mathrm{i}} \cdot \mathrm{p}^{-1}=\left(\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}\right)(1-\mathrm{p})^{-1}$ <br> $\frac{(1-\mathrm{p})}{\mathrm{p}}=\frac{\sum \mathrm{n}_{\mathrm{i}}-\sum \mathrm{k}_{\mathrm{i}}}{\sum \mathrm{k}_{\mathrm{i}}}$ <br> $\mathrm{p}=\frac{\sum \mathrm{k}_{\mathrm{i}}}{\sum \mathrm{n}_{\mathrm{i}}}$ |
| :--: | :--: |
| MLE Point Estimates | The MLE point estimate for p : $\hat{\mathrm{p}}=\frac{\sum \mathrm{k}_{\mathrm{i}}}{\sum \mathrm{n}_{\mathrm{i}}}$ |
| Fisher Information | $l(p)=\frac{1}{p(1-p)}$ |
| Confidence Intervals | The confidence intervals for the binomial distribution parameter $p$ is a controversial subject which is still debated. The Wilson interval is recommended for small and large $n$. (Brown et al. 2001) where $\begin{gathered} \bar{p}=\frac{n \hat{p}+\kappa^{2} / 2}{n+\kappa^{2}}+\frac{\kappa \sqrt{\kappa^{2}+4 n \hat{p}(1-\hat{p})}}{2\left(n+\kappa^{2}\right)} \\ \frac{p}{n}=\frac{n \hat{p}+\kappa^{2} / 2}{n+\kappa^{2}}-\frac{\kappa \sqrt{\kappa^{2}+4 n \hat{p}(1-\hat{p})}}{2\left(n+\kappa^{2}\right)} \\ \kappa=\Phi^{-1}\left(\frac{r+1}{2}\right) \end{gathered}$ <br> It should be noted that most textbooks use the Wald interval (normal approximation) given below, however many articles have shown these estimates to be erratic and cannot be trusted. (Brown et al. 2001) $\begin{aligned} & \bar{p}=\hat{p}+\kappa \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \\ & \frac{p}{n}=\hat{p}-\kappa \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \end{aligned}$ <br> For a comparison of binomial confidence interval estimates the reader is referred to (Brown et al. 2001). The following webpage has links to online calculators which use many different methods. <br> http://en.wikipedia.org/wiki/Binomial proportion confidence interval| Bayesian |  |  |
| :--: | :--: | :--: |
| Non-informative Priors for p given $\mathbf{n}, \pi(p \mid n)$ (Yang and Berger 1998, p.6) |  |  |
| Type | Prior | Posterior |
| Uniform Proper <br> Prior with limits $p \in[a, b]$ | $\frac{1}{b-a}$ | Truncated Beta Distribution <br> For $a \leq p \leq b$ <br> c. Beta $(p ; 1+k, 1+n-k)$ <br> Otherwise $\pi(p)=0$ |
| Uniform Improper <br> Proir with limits $p \in[0,1]$ | $1=\operatorname{Beta}(p ; 1,1)$ | $\operatorname{Beta}(p ; 1+k, 1+n-k)$ |
| Jeffrey's Prior <br> Reference Prior | $\frac{1}{\sqrt{p(1-p)}}=\operatorname{Beta}\left(p ; \frac{1}{2}, \frac{1}{2}\right)$ | $\begin{gathered} \operatorname{Beta}\left(p ; \frac{1}{2}+k, \frac{1}{2}+n-k\right) \\ \text { when } p \in[0,1] \end{gathered}$ |
| MDIP | $1.6186 p^{p}(1-p)^{1-p}$ | Proper - No Closed Form |
| Novick and Hall | $p^{-1}(1-p)^{-1}=\operatorname{Beta}(0,0)$ | $\operatorname{Beta}(p ; k, n-k)$ <br> when $p \in[0,1]$ |
| Conjugate Priors |  |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior Parameters |
| $\begin{gathered} p \\ \text { from } \\ \operatorname{Binom}(k ; p, n) \end{gathered}$ | Binomial | $k$ failures in $n$ trial | Beta | $\alpha_{o}, \beta_{o}$ | $\alpha=\alpha_{o}+k$ <br> $\beta=\beta_{o}+n-k$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | Five machines are measured for performance on demand. The machines can either fail or succeed in their application. The machines are tested for 10 demands with the following data for each machine: |  |  |  |  |
| Machine/Trail | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 1 |  | F $=3$ |  |  | S $=7$ |  |  |  |  |  |
| 2 |  | F $=6$ |  |  | S $=8$ |  |  |  |  |  |
| 3 |  | F $=8$ |  |  | S $=8$ |  |  |  |  |  |
| 4 |  | F $=3$ |  |  | S $=7$ |  |  |  |  |  |
| 5 |  | F $=8$ |  |  | S $=8$ |  |  |  |  |  |
| $\mu_{i}$ |  | $n \hat{p}$ |  |  | $n(1-\hat{p})$ |  |  |  |  |  |
| Assuming machines are homogeneous estimate the parameter $p$ : <br> Using MLE: $\quad \hat{p}=\frac{\sum k_{i}}{\sum n_{i}}=\frac{12}{50}=0.24$ |  |  |  |  |  |  |  |  |  |  ||  | $90 \%$ confidence intervals for $p$ : $\begin{gathered} \kappa=\Phi^{-1}(0.95)=1.64485 \\ p_{\text {lower }}=\frac{n \hat{p}+\kappa^{2} / 2}{n+\kappa^{2}}-\frac{\kappa \sqrt{\kappa^{2}+4 n \hat{p}(1-\hat{p})}}{2\left(n+\kappa^{2}\right)}=0.1557 \\ p_{\text {upper }}=\frac{n \hat{p}+\kappa^{2} / 2}{n+\kappa^{2}}+\frac{\kappa \sqrt{\kappa^{2}+4 n \hat{p}(1-\hat{p})}}{2\left(n+\kappa^{2}\right)}=0.351 \end{gathered}$ <br> A Bayesian point estimate using a uniform prior distribution $\operatorname{Beta}(1,1)$, with posterior $\operatorname{Beta}(p ; 13,39)$ has a point estimate: $\begin{gathered} \hat{p}=\mathrm{E}[\operatorname{Beta}(p ; 13,39)]=\frac{13}{52}=0.25 \end{gathered}$ <br> With $90 \%$ confidence interval using inverse Beta cdf: $\begin{gathered} {\left[F_{\text {Beta }}^{-1}(0.05)=0.1579, \quad F_{\text {Beta }}^{-1}(0.95)=0.3532\right]} \end{gathered}$ <br> The probability of observing no failures in the next 10 trials with replacement is: $\begin{gathered} f(0 ; 10,0.25)=0.0563 \end{gathered}$ <br> The probability of observing less than 5 failures in the next 10 trials with replacement is: $\begin{gathered} f(0 ; 10,0.25)=0.9803 \end{gathered}$ |  |
| :--: | :--: | :--: |
| Characteristics | CDF Approximations. The Binomial distribution is one of the most widely used distributions throughout history. Although simple, the CDF function was tedious to calculate prior to the use of computers. As a result approximations using the Poisson and Normal distribution have been used. For details see 'Related Distributions'. <br> With Replacement. The Binomial distribution models probability of $k$ successes in $n$ Bernoulli trials. However, the $k$ successes can occur anywhere among the $n$ trials with ${ }_{n} C_{k}$ different combinations. Therefore the Binomial distribution assumes replacement. The equivalent distribution which assumes without replacement is the hypergeometric distribution. <br> Symmetrical. The distribution is symmetrical when $p=0.5$. <br> Compliment. $f(k ; n, p)=f(n-k ; n, 1-p)$. Tables usually only provide values up to $n / 2$ allowing the reader to calculate to $n$ using the compliment formula. <br> Assumptions. The binomial distribution describes the behavior of |  ||  | a count variable K if the following conditions apply: <br> 1. The number of observations $n$ is fixed. <br> 2. Each observation is independent. <br> 3. Each observation represents one of two outcomes ("success" or "failure"). <br> 4. The probability of "success" is the same for each outcome. <br> Convolution Property $\sum_{i} K_{i} \sim \operatorname{Binom}\left(\sum n_{i}, p\right)$ <br> When $p$ is fixed. |
| :--: | :--: |
| Applications | Used to model independent repeated trials which have two outcomes. Examples used in Reliability Engineering are: <br> - Number of independent components which fail, $k$, from a population, $n$ after receiving a shock. <br> - Number of failures to start, $k$, from $n$ demands on a component. <br> - Number of independent items defective, $k$, from a population of $n$ items. |
| Resources | Online: <br> http://mathworld.wolfram.com/BinomialDistribution.html <br> http://en.wikipedia.org/wiki/Binomial_distribution <br> http://socr.ucla.edu/htmls/SOCR_Distributions.html (web calc) <br> Books: <br> Collani, E.V. \& Dräger, K., 2001. Binomial distribution handbook for scientists and engineers, Birkhäuser. <br> Johnson, N.L., Kemp, A.W. \& Kotz, S., 2005. Univariate Discrete Distributions 3rd ed., Wiley-Interscience. |
| Relationship to Other Distributions |  |
| Bernoulli <br> Distribution <br> Bernoulli $\left(\mathrm{k}^{\prime} ; \mathrm{p}\right)$ | The Binomial distribution counts the number of successes $k$ in $n$ independent observations of a Bernoulli process. <br> Let <br> $K_{i} \sim \operatorname{Bernoulli}\left(\mathrm{k}_{i}^{\prime} ; p\right) \quad$ and $\quad Y=\sum_{i=1}^{n} K_{i}$ <br> Then <br> $\mathrm{Y} \sim \operatorname{Binom}\left(\sum \mathrm{k}_{i}^{\prime} ; n, p\right)$ where $k \in\{1,2, \ldots, n\}$ <br> Special Case: $\operatorname{Bernoulli}(k ; p)=\operatorname{Binom}(k ; p \mid n=1)$ || Hypergeometric Distribution <br> HyperGeom $(k ; n, m, N)$ | The hypergeometric distribution models probability of $k$ successes in $n$ Bernoulli trials from a population $N$, with $m$ successors without replacement. $f(k ; n, m, N)$ <br> Limiting Case for $n \gg k$ and $p$ not near 0 or 1 : $\lim _{N \rightarrow \infty} \operatorname{Binom}\left(k ; n, p=\frac{m}{N}\right)=\operatorname{HyperGeom}(k ; n, m, N)$ |
| :--: | :--: |
| Normal Distribution $\operatorname{Norm}\left(t ; \mu, \sigma^{2}\right)$ | Limiting Case for constant $p$ : $\begin{aligned} & \lim _{p \rightarrow p} \operatorname{Binom}(k \mid n, p)=\operatorname{Norm}\left(\mathrm{k} \mid \mu=n p, \sigma^{2}=n p(1-p)\right) \\ & p=p \end{aligned}$ <br> The Normal distribution can be used as an approximation of the Binomial distribution when $n p \geq 10$ and $n p(1-p) \geq 10$. $\operatorname{Binom}(k \mid p, n) \approx \operatorname{Norm}\left(k+0.5 \mid \mu=n p, \sigma^{2}=n p(1-p)\right)$ |
| Poisson Distribution $\operatorname{Pois}(k ; \mu)$ | Limiting Case for constant $n p$ : $\begin{aligned} & \lim _{n p \rightarrow \mu} \operatorname{Binom}(k ; n, p)=\operatorname{Pois}(\mathrm{k} ; \mu=n p) \\ & \text { The Poisson distribution is the limiting case of the Binomial } \\ & \text { distribution when } n \text { is large but the ratio of } n p \text { remains constant. } \\ & \text { Hence the Poisson distribution models rare events. } \end{aligned}$ <br> The Poisson distribution can be used as an approximation to the Binomial distribution when $n \geq 20$ and $p \leq 0.05$, or if $n \geq 100$ and $n p \leq 10$. <br> The Binomial is expressed in terms of the total number of a probability of success, $p$, and trials, $N$. Where a Poisson distribution is expressed in terms of a success rate and does not need to know the total number of trials. <br> The derivation of the Poisson distribution from the binomial can be found at http://mathworld.wolfram.com/PoissonDistribution.html. <br> This interpretation can also be used to understand the conditional distribution of a Poisson random variable: <br> Let $\begin{aligned} & K_{1}, K_{2} \sim \operatorname{Pois}(\mu) \\ & \text { Given } \\ & n=K_{1}+K_{2}=\text { number of events } \\ & \text { Then } \end{aligned}$ $\left.K_{1} \mid \mathrm{n} \sim \operatorname{Binom}\left(\mathrm{k} ; \mathrm{n}, \mathrm{p}=\frac{\mu_{1}}{\mu_{1}+\mu_{2}}\right)\right)$ |
| Multinomial Distribution $\operatorname{MNom}_{d}(\mathbf{k} \mid \mathrm{n}, \mathbf{p})$ | Special Case: $\operatorname{MNom}_{d=2}(\mathbf{k} \mid \mathrm{n}, \mathbf{p})=\operatorname{Binom}(k \mid n, p)$ |# 5.3. Poisson Discrete Distribution 

Probability Density Function - $f(k)$


Cumulative Density Function - $F(k)$


Hazard Rate - $h(k)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\mu$ | $\mu>0$ | Shape Parameter: The value of $\mu$ is the expected number of events per time period or other physical dimensions. If the Poisson distribution is modeling failure events, then $\mu=\lambda t$ is the average number of failures that would occur in the space $t$. In this case $t$ is fixed and $\lambda$ becomes the distribution parameter. Some texts use the symbol $\rho$. |
| Random Variable | $k$ is an integer, $k \geq 0$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(k)$ | $\frac{\mu^{k}}{k!} e^{-\mu}=\frac{(\lambda t)^{k}}{k!} e^{-\lambda t}$ |  |
| CDF | $F(k)$ | $\begin{aligned} e^{-\mu} & \sum_{j=0}^{k} \frac{\mu^{j}}{j!}=\frac{\Gamma(k+1, \mu)}{k!} \\ & =F_{\chi^{2}}(2 \mu, 2 k+2) \end{aligned}$ <br> Where $F_{\chi^{2}}(x \mid v)$ is the Chi-square CDF. <br> When $\mu>10$ the $F(k)$ can be approximated by a normal distribution: $F(k) \cong \Phi\left(\frac{k+0.5-\mu}{\sqrt{\mu}}\right)$ |  |
| Reliability | $\mathrm{R}(\mathrm{k})=1-\mathrm{F}(\mathrm{k})$ |  |  |
| Hazard Rate | $\begin{gathered} h(k)=\left[1+\frac{k!}{\mu}\left(\mathrm{e}^{\mu}-1-\sum_{j=1}^{k} \frac{\mu^{j}}{j!}\right)\right]^{-1} \\ \text { (Gupta et al. 1997) } \end{gathered}$ |  |  |
| Properties and Moments |  |  |  |
| Median |  | See 100a\% Percentile Function when $\alpha=0.5$. |  |
| Mode |  | $\|\mu\|$ <br> where \| \| is the floor function ${ }^{2}$ |  |
| Mean - $1^{\text {st }}$ Raw Moment |  | $\mu$ |  |

[^0]
[^0]:    ${ }^{2}|\mu|=$ is the floor function (largest integer not greater than $\mu$ )| Variance - $2^{\text {nd }}$ Central Moment | $\mu$ |
| :--: | :--: |
| Skewness $-3^{\text {rd }}$ Central Moment | $1 / \sqrt{\mu}$ |
| Excess kurtosis $-4^{\text {th }}$ Central Moment | $1 / \mu$ |
| Characteristic Function | $\exp \left\{\mu\left(e^{i k}-1\right)\right\}$ |
| 100a\% Percentile Function | Numerically solve for $k$ (which is not arduous for $\mu \leq 10)$ : <br> $k_{\alpha}=F^{-1}(\alpha)$ <br> For $k>10$ the normal approximation may be used: $\begin{aligned} & \mathrm{k}_{\alpha} \cong\left\lfloor\sqrt{\mu} \Phi^{-1}(\alpha)+\mu-0.5\right\rfloor \end{aligned}$ |
| Parameter Estimation |  |
| Maximum Likelihood Estimates |  |
| Likelihood <br> Functions | For complete data: $\quad L(\mu \mid E)=\underbrace{\prod_{\mathrm{i}=1}^{\mathrm{n}} \frac{\mu^{\mathrm{k} \mathrm{i}^{\mathrm{r}}}}{\mathrm{k}_{\mathrm{i}}^{\mathrm{r}}!}}_{\text {known } \mathrm{k}}$ <br> where $n$ is the number of poisson processes. |
| Log-Likelihood Function | $\Lambda=\underbrace{-\mathrm{n} \mu+\sum_{\mathrm{i}=1}^{\mathrm{n}}\left\{k_{i} \ln (\mu)-\ln \left(k_{i}!\right)\right\}}_{\text {known } \mathrm{k}}$ |
| $\frac{\partial \Lambda}{\partial \mu}=0$ | $\frac{\partial \Lambda}{\partial \mu}=-\mathrm{n}+\frac{1}{\mu} \sum_{\mathrm{i}=1}^{\mathrm{n}} k_{i}=0$ |
| MLE Point Estimates | For complete data solving $\frac{\partial \Lambda}{\partial \mu}=0$ gives: $\begin{aligned} & \widehat{\mu}=\frac{1}{n} \sum_{\mathrm{i}=1}^{\mathrm{n}} k_{i} \text { or } \widehat{\lambda}=\frac{1}{t n} \sum_{\mathrm{i}=1}^{\mathrm{n}} k_{i} \\ & \text { Note that in this context: } \\ & \mathrm{t}=\text { the unit of time for which the rate, } \lambda \text { is being measured. } \\ & n=\text { the number of Poisson processes for which the exact number of } \\ & \text { failures, k, was known. } \\ & k_{i}=\text { the number of failures that occurred within the } \mathrm{i}^{\text {th }} \text { Poisson } \\ & \text { process. } \\ & \text { When there is only one Poisson process this reduces to: } \\ & \widehat{\mu}=k \text { or } \widehat{\lambda}=\frac{k}{t} \\ & \text { For censored data numerical methods are needed to maximize the }\end{aligned}$ ||  | log-likelihood function. |  |  |
| :--: | :--: | :--: | :--: |
| Fisher Information | $I(\lambda)=\frac{1}{\lambda}$ |  |  |
| $100 \gamma \%$ <br> Confidence <br> Interval <br> (complete data only) |  | $\lambda_{\text {lower }}-$ <br> 2 Sided | $\lambda_{\text {upper }}-$ <br> 2 Sided |
|  | Conservative two sided confidence intervals. | $\frac{\chi_{[1-\gamma]}^{2}\left(2 \sum k_{i}\right)}{2 t n}$ | $\frac{\chi_{[1+\gamma]}^{2}\left(2 \sum k_{i}+2\right)}{2 t n}$ |
|  | When $k$ is large $(k>10)$ two sided intervals | $\hat{\lambda}-\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\frac{\hat{\lambda}}{t n}}$ | $\hat{\lambda}+\Phi^{-1}\left(\frac{1+\gamma}{2}\right) \sqrt{\frac{\hat{\lambda}}{t n}}$ |
|  | (Nelson 1982, p.201) Note: The first confidence intervals are conservative in that at least $100 \gamma \%$. Exact confidence intervals cannot be easily achieved for discrete distributions. |  |  |
| Bayesian |  |  |  |
| Non-informative Priors $\pi(\lambda)$ in known time interval $t$ |  |  |  |
| Type | Prior |  | Posterior |
| Uniform Proper <br> Prior with limits $\lambda \in[a, b]$ | $\frac{1}{b-a}$ |  | Truncated Gamma Distribution <br> For $a \leq \lambda \leq b$ <br> c. Gamma $(\lambda ; 1+\mathrm{k}, \mathrm{t})$ <br> Otherwise $\pi(\lambda)=0$ |
| Uniform Improper <br> Prior with limits $\lambda \in[0, \infty)$ | $1 \propto \operatorname{Gamma}(1,0)$ |  | $\operatorname{Gamma}(\lambda ; 1+\mathrm{k}, \mathrm{t})$ |
| Jeffrey's Prior | $\frac{1}{\sqrt{\lambda}} \propto \operatorname{Gamma}\left(\frac{1}{\lambda}, 0\right)$ |  | $\operatorname{Gamma}\left(\lambda ; \frac{1}{\lambda}+\mathrm{k}, \mathrm{t}\right)$ <br> when $\lambda \in[0, \infty)$ |
| Novick and Hall | $\frac{1}{\lambda} \propto \operatorname{Gamma}(0,0)$ |  | $\operatorname{Gamma}(\lambda ; \mathrm{k}, \mathrm{t})$ <br> when $\lambda \in[0, \infty)$ |
| Conjugate Priors |  |  |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior Parameters |
| $\begin{gathered} \lambda \\ \text { from } \\ \operatorname{Pois}(k ; \mu) \end{gathered}$ | Exponential | $n_{F}$ failures in $t_{T}$ unit of time | Gamma | $k_{0}, \Lambda_{0}$ | $\begin{aligned} & k=k_{o}+n_{F} \\ & \Lambda=\Lambda_{o}+t_{T} \end{aligned}$ |
| Description, Limitations and Uses |  |  |  |  |
| Example |  | Three vehicle tires were run on a test area for 1000km have punctures at the following distances: <br> Tire 1: No punctures <br> Tire 2: $400 \mathrm{~km}, 900 \mathrm{~km}$ |  |  ||  | Tire 3: 200km <br> Punctures can be modeled as a renewal process with perfect repair and an inter-arrival time modeled by an exponential distribution. Due to the Poisson distribution being homogeneous in time, the test from multiple tires can be combined and considered a test of one tire with multiple renewals. See example in section 1.1.6. <br> Total time on test is $3 \times 1000=3000 \mathrm{~km}$. Total number of failures is 3. Therefore using MLE the estimate of $\lambda$ : $\begin{gathered} \hat{\lambda}=\frac{\mathrm{k}}{t_{T}}=\frac{3}{3000}=1 \mathrm{E}-3 \end{gathered}$ <br> With $90 \%$ confidence interval (conservative): $\begin{gathered} {\left[\frac{\chi_{(0.05)}^{2}(6)}{6000}=0.272 E-3, \quad \frac{\chi_{(0.95)}^{2}(8)}{6000}=2.584 E-3\right]} \end{gathered}$ <br> A Bayesian point estimate using the Jeffery non-informative improper prior $\operatorname{Gamma}\left(\frac{1}{\sigma} 0\right)$, with posterior $\operatorname{Gamma}(\lambda ; 3.5,3000)$ has a point estimate: $\begin{gathered} \hat{\lambda}=\mathrm{E}[\operatorname{Gamma}(\lambda ; 3.5,3000)]=\frac{3.5}{3000}=1.1 \hat{\mathrm{e}} \mathrm{E}-3 \end{gathered}$ <br> With $90 \%$ confidence interval using inverse Gamma cdf: $\begin{gathered} {\left[F_{G}^{-1}(0.05)=0.361 E-3, \quad F_{G}^{-1}(0.95)=2.344 E-3\right]} \end{gathered}$ |
| :--: | :--: |
| Characteristics | The Poisson distribution is also known as the Rare Event distribution. <br> If the following assumptions are met than the process follows a Poisson distribution: <br> - The chance of two simultaneous events is negligible or impossible (such as renewal of a single component); <br> - The expected value of the random number of events in a region is proportional to the size of the region. <br> - The random number of events in non-overlapping regions are independent. <br> $\boldsymbol{\mu}$ characteristics: <br> - $\quad \mu$ is the expected number of events for the unit of time being measured. <br> - When the unit of time varies $\mu$ can be transformed into a rate and time measure, $\lambda t$. <br> - For $\mu \leq 10$ the distribution is skewed to the right. <br> - For $\mu \geq 10$ the distribution approaches a normal distribution with a $\mu=\mu$ and $\sigma=\sqrt{\mu}$. $\begin{gathered} K \sim \operatorname{Pois}(\mu) \end{gathered}$ ||  | Convolution property $K_{1}+K_{2}+\ldots+K_{n} \sim \operatorname{Pois}\left(k ; \sum \mu_{i}\right)$ |
| :--: | :--: |
| Applications | Homogeneous Poisson Process (HPP). The Poisson distribution gives the distribution of exactly k failures occurring in a HPP. See relation to exponential and gamma distributions. <br> Renewal Theory. Used in renewal theory as the counting function and may model non-homogeneous (aging) components by using a time dependent failure rate, $\lambda(t)$. <br> Binomial Approximation. Used to model the Binomial distribution when the number of trials is large and $\mu$ remains moderate. This can greatly simplify Binomial distribution calculations. <br> Rare Event. Used to model rare events when the number of trials is large compared to the rate at which events occur. |
| Resources | Online: <br> http://mathworld.wolfram.com/PoissonDistribution.html <br> http://en.wikipedia.org/wiki/Poisson_distribution <br> http://socr.ucla.edu/htm/s/SOCR_Distributions.html (interactive web calculator) <br> Books: <br> Haight, F.A., 1967. Handbook of the Poisson distribution [by] Frank <br> A. Haight, New York,: Wiley. <br> Nelson, W.B., 1982. Applied Life Data Analysis, WileyInterscience. <br> Johnson, N.L., Kemp, A.W. \& Kotz, S., 2005. Univariate Discrete Distributions 3rd ed., Wiley-Interscience. |
| Relationship to Other Distributions |  |
| Exponential Distribution $\operatorname{Exp}(t ; \lambda)$ | Let $\quad K \sim \operatorname{Pois}(\mathrm{k} ; \mu=\lambda t)$ <br> Given <br> Then <br> The time between each arrival of T is exponentially distributed. <br> Special Cases: $\quad \operatorname{Pois}(\mathrm{k} ; \lambda t \mid k=1)=\operatorname{Exp}(t ; \lambda)$ |
| Gamma <br> Distribution <br> $\operatorname{Gamma}(k \mid \lambda)$ | Let $\quad T_{1} \ldots T_{k} \sim \operatorname{Exp}(\lambda) \quad$ and $\quad T_{t}=T_{1}+T_{2}+\cdots+T_{k}$ <br> Then $\quad T_{t} \sim \operatorname{Gamma}(k, \lambda)$ ||  | The Poisson distribution is the probability that exactly $k$ failures have been observed in time $t$. This is the probability that $t$ is between $T_{k}$ and $T_{k+1}$. <br> $$
f_{\text {Poisson }}(k ; \lambda t)=\int_{k}^{k+1} f_{\text {Gamma }}(t ; x, \lambda) d x=F_{\text {Gamma }}(t ; k+1, \lambda)-F_{\text {Gamma }}(t ; k, \lambda) $$ <br> where $k$ is an integer. |
| :--: | :--: |
| Binomial Distribution $\operatorname{Binom}(k \mid p, N)$ | Limiting Case for constant $n p$ : <br> The Poisson distribution is the limiting case of the Binomial distribution when $n$ is large but the ratio of $n p$ remains constant. Hence the Poisson distribution models rare events. <br> The Poisson distribution can be used as an approximation to the Binomial distribution when $n \geq 20$ and $p \leq 0.05$, or if $n \geq 100$ and $n p \leq 10$. <br> The Binomial is expressed in terms of the total number of a probability of success, $p$, and trials, $N$. Where a Poisson distribution is expressed in terms of a success rate and does not need to know the total number of trials. <br> The derivation of the Poisson distribution from the binomial can be found at http://mathworld.wolfram.com/PoissonDistribution.html. <br> This interpretation can also be used to understand the conditional distribution of a Poisson random variable: <br> Let <br> Given <br> $K_{1}, K_{2} \sim \operatorname{Pois}(\mu)$ <br> Then $\quad n=K_{1}+K_{2}=$ number of events <br> $K_{1}|\mathrm{n} \sim \operatorname{Binom}\left(\mathrm{k} ; \mathrm{n} \mid \mathrm{p}=\frac{\mu_{1}}{\mu_{1}+\mu_{2}}\right)$ |
| Normal Distribution $\operatorname{Norm}\left(k \mid \mu^{\prime}, \sigma\right)$ | $\lim _{\mu \rightarrow \infty} F_{\text {Poisson }}(k ; \mu)=F_{\text {Normal }}\left(k ; \mu^{\prime}=\mu, \sigma^{2}=\mu\right)$ <br> This is a good approximation when $\mu>1000$. When $\mu>10$ the same approximation can be made with a correction: $\lim _{\mu \rightarrow \infty} F_{\text {Poisson }}(k ; \mu)=F_{\text {Normal }}\left(k ; \mu^{\prime}=\mu-0.5, \sigma^{2}=\mu\right)$ |
| Chi-square Distribution $\chi^{2}(t \mid v)$ | $\operatorname{Pois}(k \mid \mu)=\chi^{2}(x=2 \mu, v=2 k+2)$ |# 6. Bivariate and Multivariate Distributions# 6.1. Bivariate Normal Continuous Distribution 

Probability Density Function - $f(x, y)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
|  | $\mu_{x}, \mu_{y}$ | $\begin{gathered} -\infty<\mu_{i}<\infty \\ j \in\{x, y\} \end{gathered}$ | Location parameter: The mean of each random variable. |
|  | $\sigma_{x}, \sigma_{y}$ | $\begin{gathered} \sigma_{j}>0 \\ j \in\{x, y\} \end{gathered}$ | Scale parameter: The standard deviation of each random variable. |
| Parameters | $\rho$ | $-1 \leq \rho \leq 1$ | Correlation Coefficient: <br> The correlation between the two random variables. $\rho=\operatorname{corr}(X, Y)=\frac{\operatorname{cov}[X Y]}{\sigma_{x} \sigma_{y}}$ $=\frac{E\left[\left(X-\mu_{x}\right)\left(Y-\mu_{y}\right)\right]}{\sigma_{x} \sigma_{y}}$ |
| Limits | $-\infty<x<\infty$ and $-\infty<y<\infty$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $\begin{gathered} f(x, y)=\frac{1}{2 \pi \sigma_{x} \sigma_{y} \sqrt{1-\rho^{2}}} \exp \left[\frac{z_{x}^{2}+z_{y}^{2}-2 \rho z_{x} z_{y}}{-2\left(1-\rho^{2}\right)}\right] \\ =\phi(x) \phi(y \mid x) \\ =\phi(x) \phi\left(\frac{y-\rho x}{\sqrt{1-\rho^{2}}}\right)=\phi(y) \phi\left(\frac{x-\rho y}{\sqrt{1-\rho^{2}}}\right) \end{gathered}$ <br> Where $\phi$ is the standard normal distribution and: $z_{i}=\frac{x-\mu_{i}}{\sigma_{i}} \quad j \in\{x, y\}$ |  |  |
| Marginal PDF | $\begin{aligned} f(x) & =\int_{-\infty}^{\infty} f(x, y) d y \\ & =\frac{1}{\sigma_{x} \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(z_{x}\right)^{2}\right] \\ & =\operatorname{Norm}\left(\mu_{x}, \sigma_{x}\right) \end{aligned}$ | $\begin{aligned} f(y) & =\int_{-\infty}^{\infty} f(x, y) d x \\ & =\frac{1}{\sigma_{y} \sqrt{2 \pi}} \exp \left[-\frac{1}{2}\left(z_{y}\right)^{2}\right] \\ & =\operatorname{Norm}\left(\mu_{y}, \sigma_{y}\right) \end{aligned}$ |  |
| Conditional PDF | $\begin{aligned} & f(x \mid y)=\operatorname{Norm}\left(\mu_{x \mid y}=\mu_{x}+\rho\left(\frac{\sigma_{y}}{\sigma_{y}}\right)\left(y-\mu_{y}\right), \sigma_{x \mid y}^{2}=\sigma_{x}^{2}\left(1-\rho^{2}\right)\right) \\ & f(y \mid x)=\operatorname{Norm}\left(\mu_{y \mid x}=\mu_{y}+\rho\left(\frac{\sigma_{y}}{\sigma_{x}}\right)\left(y-\mu_{x}\right), \sigma_{y \mid x}^{2}=\sigma_{y}^{2}\left(1-\rho^{2}\right)\right) \end{aligned}$ |  |  |
| CDF | $F(\mathrm{x}, \mathrm{y})=\frac{1}{2 \pi \sigma_{\mathrm{x}} \sigma_{\mathrm{y}} \sqrt{1-\rho^{2}}} \int_{-\infty}^{\mathrm{x}} \int_{-\infty}^{\mathrm{y}} \exp \left[\frac{\mathrm{z}_{0}^{2}+\mathrm{z}_{x}^{2}-2 \rho \mathrm{z}_{\mathrm{u}} \mathrm{z}_{\mathrm{y}}}{-2\left(1-\rho^{2}\right)}\right] \mathrm{du} \mathrm{dv}$ |  |  ||  | where $\mathrm{z}_{\mathrm{j}}=\frac{\mathrm{x}-\mu_{\mathrm{j}}}{\sigma_{\mathrm{j}}}$ |
| :--: | :--: |
| Reliability | $\begin{gathered} R(\mathrm{x}, \mathrm{y})=\frac{1}{2 \pi \sigma_{\mathrm{x}} \sigma_{\mathrm{y}} \sqrt{1-\rho^{2}}} \int_{\mathrm{x}}^{\infty} \int_{\mathrm{y}}^{\infty} \exp \left[\frac{\mathrm{z}_{\mathrm{u}}^{2}+\mathrm{z}_{\mathrm{v}}^{2}-2 \rho \mathrm{z}_{\mathrm{u}} \mathrm{z}_{\mathrm{v}}}{2\left(1-\rho^{2}\right)}\right] \mathrm{du} \mathrm{dv} \\ \mathrm{z}_{\mathrm{j}}=\frac{\mathrm{x}-\mu_{\mathrm{j}}}{\sigma_{\mathrm{j}}} \end{gathered}$ |
| Properties and Moments |  |
| Median | $\left[\begin{array}{l}\mu_{x} \\ \mu_{y}\end{array}\right]$ |
| Mode | $\left[\begin{array}{l}\mu_{x} \\ \mu_{y}\end{array}\right]$ |
| Mean - $1^{\text {st }}$ Raw Moment | $\begin{aligned} & E\left[\begin{array}{l}X \\ Y\end{array}\right]=\left[\begin{array}{l} \mu_{x} \\ \mu_{y} \end{array}\right] \end{aligned}$ <br> The mean of the marginal distributions is: $\begin{aligned} & E[X]=\mu_{x} \\ & E[Y]=\mu_{y} \end{aligned}$ <br> The mean of the conditional distributions gives the following lines (also called the regression lines): $\begin{aligned} & \mathrm{E}(\mathrm{X} \mid \mathrm{Y}=\mathrm{y})=\mu_{\mathrm{x}}+\rho \frac{\sigma_{\mathrm{x}}}{\sigma_{\mathrm{y}}}\left(\mathrm{y}-\mu_{\mathrm{y}}\right) \\ & \mathrm{E}(\mathrm{Y} \mid \mathrm{X}=\mathrm{x})=\mu_{\mathrm{y}}+\rho \frac{\sigma_{\mathrm{y}}}{\sigma_{\mathrm{x}}}\left(\mathrm{y}-\mu_{\mathrm{x}}\right) \end{aligned}$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\begin{gathered} \operatorname{Cov}\left[\begin{array}{l}X \\ Y\end{array}\right]=\left[\begin{array}{cc} \sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\ \rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2} \end{array}\right] \end{gathered}$ <br> Variance of marginal distributions: $\begin{aligned} & \operatorname{Var}(\mathrm{X})=\sigma_{\mathrm{X}}^{2} \\ & \operatorname{Var}(\mathrm{Y})=\sigma_{\mathrm{Y}}^{2} \end{aligned}$ <br> Variance of conditional distributions: $\begin{aligned} & \operatorname{Var}(\mathrm{X} \mid \mathrm{Y}=\mathrm{y})=\sigma_{\mathrm{X}}^{2}\left(1-\rho^{2}\right) \\ & \operatorname{Var}(Y \mid X=x)=\sigma_{\mathrm{Y}}^{2}\left(1-\rho^{2}\right) \end{aligned}$ |
| 100a\% Percentile Function | An ellipse containing 100a \% of the distribution is (Kotz et al. 2000, p.254): $\begin{aligned} & \frac{\left(\mathrm{z}_{\mathrm{x}}^{2}+\mathrm{z}_{\mathrm{y}}^{2}-2 \rho \mathrm{z}_{\mathrm{x}} \mathrm{z}_{\mathrm{y}}\right)}{-2\left(1-\rho^{2}\right)}=\ln (1-\alpha) \end{aligned}$ || where |  |
| :--: | :--: |
| For the standard bivariate normal: |  |
|  | $\frac{x^{2}+y^{2}-2 p x y}{-2\left(1-\rho^{2}\right)}=\ln (1-\alpha)$ |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| MLE Point Estimates | When there is only complete failure data the MLE estimates can be given as (Kotz et al. 2000, p.294): $\begin{aligned} \widehat{\mu_{x}} & =\frac{1}{n_{F}} \sum_{i=1}^{n_{F}} x_{i} \quad \widehat{\sigma_{x}^{2}}=\frac{1}{n_{F}} \sum_{i=1}^{n_{F}}\left(x_{i}-\widehat{\mu_{x}}\right)^{2} \\ \widehat{\mu_{y}} & =\frac{1}{n_{F}} \sum_{i=1} y_{i} \quad \widehat{\sigma_{y}^{2}}=\frac{1}{n_{F}} \sum_{i=1}\left(y_{i}-\widehat{\mu_{y}}\right)^{2} \\ \hat{\rho} & =\frac{1}{\widehat{\sigma_{x}} \widehat{\sigma_{y}} n_{F}} \sum_{i=1}^{n_{F}}\left(x_{i}-\mu_{x}\right)\left(y_{i}-\mu_{y}\right) \end{aligned}$ <br> If one or more of the variables are known, different estimators are given in (Kotz et al. 2000, pp.294-305). <br> A correction factor of -1 can be introduced to the $\widehat{\sigma^{2}}$ to give the unbiased estimators: $\widehat{\sigma_{x}^{2}}=\frac{1}{n_{F}-1} \sum_{i=1}^{n_{F}}\left(x_{i}-\widehat{\mu_{x}}\right)^{2} \quad \widehat{\sigma_{y}^{2}}=\frac{1}{n_{F}-1} \sum_{i=1}^{n_{F}}\left(y_{i}-\widehat{\mu_{y}}\right)^{2}$ |
| Bayesian |  |
| Non-informative Priors: A complete coverage of numerous reference prior distributions with different parameter ordering is contained in (Berger \& Sun 2008). <br> For a summary of the general Bayesian priors and conjugates see the multivariate normal distribution. |  |
| Description, Limitations and Uses |  |
| Example | The accuracy of a cutting machine used in manufacturing is desired to be measured. 5 cuts at the required length are made. The lengths and room temperature were measured as: $\begin{aligned} & 7.436,10.270,10.466,11.039,11.854 \mathrm{~mm} \\ & 19.51,21.23,21.41,22.78,26.78^{\circ} \mathrm{C}\end{aligned}$ |MLE estimates are:

$$
\begin{gathered}
\widehat{\mu_{x}}=\frac{\sum \mathrm{x}_{\mathrm{i}}}{\frac{\mathrm{n}}{\mathrm{n}}}=10.213 \\
\widehat{\mu_{T}}=\frac{\sum \mathrm{t}_{\mathrm{i}}}{\mathrm{n}}=22.342 \\
\widehat{\sigma_{x}^{2}}=\frac{\sum\left(\mathrm{x}_{\mathrm{i}}-\widehat{\mu_{L}}\right)^{2}}{\frac{\mathrm{n}-1}{\mathrm{n}}=}=2.7885 \\
\widehat{\sigma_{T}^{2}}=\frac{\sum\left(\mathrm{t}_{\mathrm{i}}-\widehat{\mu_{T}}\right)^{2}}{\mathrm{n}-1}=7.5033 \\
\widehat{\rho}=\frac{1}{\widehat{\sigma_{x} \sigma_{T} \mathrm{n}_{Y}}} \sum_{i=1}^{n_{F}}\left(x_{i}-\mu_{x}\right)\left(t_{i}-\mu_{T}\right)=0.1454
\end{gathered}
$$

If you know the temperature is $24^{\circ} \mathrm{C}$ what is the likely cutting distance distribution?
$f(x \mid t=24)=\operatorname{Norm}\left(\mu_{x \mid t}=\mu_{x}+\rho\left(\frac{\sigma_{x}}{\sigma_{t}}\right)\left(t-\mu_{T}\right), \sigma_{x \mid t}^{2}=\sigma_{x}^{2}\left(1-\rho^{2}\right)\right)$
$f(x \mid t=24)=\operatorname{Norm}(10.303,2.730)$

Characteristic
Also known as Binormal Distribution.
Let U, V and W be three independent normally distributed random variables. Then let:

$$
\begin{aligned}
& X=U+V \\
& Y=V+W
\end{aligned}
$$

Then $(X, Y)$ has a bivariate normal distribution. (Balakrishnan \& Lai 2009, p.483)

Independence. If $X$ and $Y$ are jointly normal random variables, then they are independent when $\rho=0$. This gives a contour plot of $f(x, y)$ with concentric circles around the origin. When given a value on the $y$ axis it does not assist in estimating the value on the $x$ axis and therefore are independent. When $X$ and $Y$ are independent, the pdf reduces to:

$$
f(\mathrm{x}, \mathrm{y})=\frac{1}{2 \pi \sigma_{\mathrm{x}} \sigma_{\mathrm{y}}} \exp \left[-\frac{\mathrm{z}_{\mathrm{x}}^{2}+\mathrm{z}_{\mathrm{y}}^{2}}{2}\right]
$$

Correlation Coefficient $\rho$. (Yang et al. 2004, p.49)

- $\boldsymbol{\rho}>0$. When $X$ increases then $Y$ also tends to increase. When $\rho=1 \mathrm{X}$ and Y have a perfect positive linear relationship such that $Y=c+m X$ where $m$ is positive.
- $\quad \boldsymbol{\rho}<0$. When $X$ increases then $Y$ also tends to decrease. When $\rho=-1 \mathrm{X}$ and Y have a perfect negative linear relationship such that $Y=c+m X$ where $m$ is negative.- $\boldsymbol{\rho}=\mathbf{0}$. Increases or decreases in $X$ have no affect on Y. X and $Y$ are independent.

Ellipse Axis. (Kotz et al. 2000, p.254) The slope of the main axis from the $x$-axis is given as:

$$
\theta=\frac{1}{2} \tan ^{-1}\left[\frac{2 \rho \sigma_{x} \sigma_{y}}{\sigma_{x}^{2}-\sigma_{y}^{2}}\right]
$$

If $\sigma_{x}=\sigma_{y}$ for positive $\rho$ the main axis of the ellipse is $45^{\circ}$ from the $x$ axis. For negative $\rho$ the main axis of the ellipse is $-45^{\circ}$ from the $x$-axis.

Circular Normal Density Function. (Kotz et al. 2000, p.255) When $\sigma_{x}=\sigma_{y}$ and $\rho=0$ the bivariate distribution is known as a circular normal density function.

Elliptical Normal Distribution (Kotz et al. 2000, p.255). If $\rho=0$ and $\sigma_{x} \neq \sigma_{y}$ then the distribution may be known as an elliptical normal distribution.

Standard Bivariate Normal Distribution. Occurs when $\mu=0$ and $\sigma=1$. For positive $p$ the main axis of the ellipse is $45^{\circ}$ from the $x$-axis. For negative $p$ the main axis of the ellipse is $-45^{\circ}$ from the $x$-axis.

$$
f(\mathrm{x}, \mathrm{y})=\frac{1}{2 \pi \sqrt{1-\rho^{2}}} \exp \left[-\frac{\mathrm{x}^{2}+\mathrm{y}^{2}-2 \rho \mathrm{xy}}{2\left(1-\rho^{2}\right)}\right]
$$

# Mean / Median / Mode: 

As per the univariate distributions the mean, median and mode are equal.

Matrix Form. The bivariate distribution may be written in matrix form as:

$$
\boldsymbol{X}=\left(\begin{array}{l}
X_{1} \\
X_{2}
\end{array}\right) \quad \boldsymbol{\mu}=\binom{\mu_{1}}{\mu_{2}} \quad \boldsymbol{\Sigma}=\left[\begin{array}{cc}
\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\
\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right]
$$

when $\boldsymbol{X} \sim \operatorname{Norm}_{2}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$

$$
f(\mathbf{x})=\frac{1}{2 \pi \sqrt{|\boldsymbol{\Sigma}|}} \exp \left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\mathrm{T}} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right]
$$

Where $|\boldsymbol{\Sigma}|$ is the determinant of $\boldsymbol{\Sigma}$. This is the form used in multivariate normal distribution.

The following properties are given in matrix form:

## Convolution Property

Let

$$
\boldsymbol{X} \sim \operatorname{Norm}\left(\boldsymbol{\mu}_{\mathbf{x}}, \boldsymbol{\Sigma}_{\mathbf{x}}\right) \quad \boldsymbol{Y} \sim \operatorname{Norm}\left(\boldsymbol{\mu}_{\boldsymbol{y}}, \boldsymbol{\Sigma}_{\boldsymbol{y}}\right)
$$

Where $\quad \boldsymbol{X} \perp \boldsymbol{Y}$ (independent)Then

$$
X+Y \sim \operatorname{Norm}\left(\mu_{x}+\mu_{y}, \Sigma_{x}+\Sigma_{y}\right)
$$

Note if $\mathbf{X}$ and $\mathbf{Y}$ are dependent then $\boldsymbol{X}+\boldsymbol{Y}$ may not be even be normally distributed.(Novosyolov 2006)

# Scaling Property 

Let

$$
Y=A X+b
$$

$Y$ is a $p$
$x 1$ matrix
Then

$$
Y \sim \operatorname{Norm}\left(A \mu+b, A \Sigma A^{T}\right)
$$

b is a $p \times 1$ matrix
$x 2$ matrix
Marginalize Property:
Let

$$
\left[\begin{array}{l}
X_{1} \\
X_{2}
\end{array}\right] \sim \operatorname{Norm}\left(\left[\begin{array}{l}
\mu_{1} \\
\mu_{2}
\end{array}\right],\left[\begin{array}{rr}
\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\
\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right]\right)
$$

Then

$$
X_{1} \sim \operatorname{Norm}\left(\mu_{1}, \sigma_{1}\right)
$$

## Conditional Property:

Let

$$
\left[\begin{array}{l}
X_{1} \\
X_{2}
\end{array}\right] \sim \operatorname{Norm}\left(\left[\begin{array}{l}
\mu_{1} \\
\mu_{2}
\end{array}\right],\left[\begin{array}{rr}
\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\
\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right]\right)
$$

Then

$$
f\left(x_{1} \mid x_{2}\right)=\operatorname{Norm}\left(\mu_{1 \mid 2}, \sigma_{1 \mid 2}\right)
$$

Where

$$
\begin{aligned}
& \mu_{1 \mid 2}=\mu_{1}+\rho\left(\frac{\sigma_{1}}{\sigma_{2}}\right)\left(x_{2}-\mu_{2}\right) \\
& \sigma_{1 \mid 2}=\sigma_{1} \sqrt{1-\rho^{2}}
\end{aligned}
$$

It should be noted that the standard deviation of the marginal distribution does not depend on the given value.

| Applications | The bivariate distribution is used in many more applications which are <br> common to the multivariate normal distribution. Please refer to <br> multivariate normal distribution for a more complete coverage. |
| :-- | :-- |

Graphical Representation of Multivariate Normal. As with all
bivariate distributions having only two dependent variables allows it to
be easily graphed (in a three dimensional graph) and visualized. As
such the bivariate normal is popular in introducing higher dimensional
cases.

## Resources

Online:
http://mathworld.wolfram.com/BivariateNormalDistribution.html http://en.wikipedia.org/wiki/Multivariate_normal_distribution http://www.aiaccess.net/English/Glossaries/GlosMod/e_gm_binormal_ distri.htm (interactive visual representation)

Books:
Balakrishnan, N. \& Lai, C., 2009. Continuous Bivariate Distributions|  | 2nd ed., Springer. |
| :-- | :-- |
|  | Yang, K. et al., 2004. Multivariate Statistical Methods in Quality <br> Management 1st ed., McGraw-Hill Professional. |
|  | Patel, J.K, Read, C.B, 1996. Handbook of the Normal Distribution, $2^{\text {nd }}$ <br> Edition, CRC |
|  | Tong, Y.L., 1990. The Multivariate Normal Distribution, Springer. |# 6.2. Dirichlet Continuous Distribution 

Probability Density Function - $f(x)$
| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
|  | $\alpha=\left[\alpha_{1}, \alpha_{2}, \ldots, \alpha_{d}, \alpha_{0}\right]^{T}$ | $\alpha_{i}>0$ | Shape <br> Matrix. Note that the matrix $\boldsymbol{\alpha}$ is $d+1 \quad$ in length. |
|  | $d$ | $d \geq 1$ <br> (integer) | Dimensions. <br> The number of random variables being modeled. |
| Limits | $0 \leq \mathrm{x}_{\mathrm{i}} \leq 1$ <br> $\sum_{i=1}^{d} x_{i} \leq 1$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(\mathbf{x})=\frac{1}{\mathrm{~B}(\boldsymbol{\alpha})}\left(1-\sum_{i=1}^{d} x_{i}\right)^{\alpha_{0}-1} \prod_{i=1}^{\mathrm{d}} \mathrm{x}_{\mathrm{i}}^{\alpha_{i}-1}$ <br> where $\mathrm{B}(\boldsymbol{\alpha})$ is the multinomial beta function: $\begin{gathered} \mathrm{B}(\boldsymbol{\alpha})=\frac{\prod_{i=0}^{\mathrm{d}} \Gamma\left(\alpha_{\mathrm{i}}\right)}{\Gamma\left(\sum_{i=0}^{\mathrm{d}} \alpha_{\mathrm{i}}\right)} \\ \text { The special case of the Dirichlet distribution is the beta } \end{gathered}$ <br> distribution when $d=1$. |  |  |
| Marginal PDF | Let $\boldsymbol{X}=\left[\begin{array}{l}\boldsymbol{U} \\ \boldsymbol{V}\end{array}\right] \sim \operatorname{Dir}_{d}(\alpha)$ <br> Where $\quad \boldsymbol{X}=\left[X_{1}, \ldots, X_{s}, X_{s+1}, \ldots, X_{d}\right]^{T}$ <br> $\boldsymbol{U}=\left[X_{1}, \ldots, X_{s}\right]^{T}$ <br> $\boldsymbol{V}=\left[X_{s+1}, \ldots, X_{d}\right]^{T}$ <br> Let $\alpha_{\Sigma}=\sum_{j=0}^{d} \alpha_{j}=$ sum of $\boldsymbol{\alpha}$ matrix elements. |  |  |
|  | $\boldsymbol{U} \sim \operatorname{Dir}_{s}\left(\boldsymbol{\alpha}_{\mathbf{u}}\right)$ where $\boldsymbol{\alpha}_{\mathbf{u}}=\left[\alpha_{1}, \alpha_{2}, \ldots, \alpha_{s}, \alpha_{\Sigma}-\sum_{j=1}^{s} \alpha_{j}\right]^{T}$ |  |  |
|  | $f(\mathbf{u})=\frac{\Gamma\left(\alpha_{\Sigma}\right)}{\Gamma\left(\alpha_{\Sigma}-\sum_{j=1}^{s} \alpha_{j}\right) \prod_{i=1}^{s} \Gamma\left(\alpha_{i}\right)}\left(1-\sum_{i=1}^{s} x_{i}\right)^{\alpha_{\Sigma}-1-\sum_{j=i}^{s} \alpha_{j}} \prod_{i=1}^{s} x_{i}^{\alpha_{i}-1}$ |  |  ||  | When marginalized to one variable: $X_{i} \sim \operatorname{Beta}\left(\alpha_{i}, \alpha_{\Sigma}-\alpha_{i}\right)$ $f\left(x_{i}\right)=\frac{\Gamma\left(\alpha_{i}\right)}{\Gamma\left(\alpha_{i}-\alpha_{i}\right) \Gamma\left(\alpha_{i}\right)}\left(1-x_{i}\right)^{\alpha_{\Sigma}-\alpha_{i}-1} \mathrm{x}_{i}^{\alpha_{i}-1}$ |
| :--: | :--: |
| Conditional PDF | $\boldsymbol{U} \mid \boldsymbol{V}=\boldsymbol{v} \sim \operatorname{Dir}_{\mathrm{d} \rightarrow \mathrm{s}}\left(\boldsymbol{\alpha}_{\mathrm{u} \mid \boldsymbol{v}}\right)$ where $\boldsymbol{\alpha}_{\mathbf{u} \mid \boldsymbol{v}}=\left[\alpha_{S+1}, \alpha_{s+2}, \ldots, \alpha_{m}, \alpha_{0}\right]^{T}$ (Kotz et al. 2000, p.488) $f(\mathbf{u} \mid \mathbf{v})=\frac{r\left(\sum_{i=0}^{s} \alpha_{i}\right)}{\prod_{i=0}^{s} \Gamma\left(\alpha_{i}\right)}\left(1-\sum_{i=1}^{s} x_{i}\right)^{\alpha_{0}-1} \prod_{i=1}^{s} x_{i}^{\alpha_{i}-1}$ |
| CDF | $\begin{aligned} F(\mathbf{x}) & =\mathrm{P}\left(\mathrm{X}_{1} \leq \mathrm{x}_{1}, \mathrm{X}_{2} \leq \mathrm{x}_{2}, \ldots, \mathrm{X}_{\mathrm{d}} \leq \mathrm{x}_{\mathrm{d}}\right) \\ & =\int_{0}^{x_{1}} \int_{0}^{x_{2}} \ldots \int_{0}^{x_{d}}\left(1-\sum_{i=1}^{d} x_{i}\right)^{\alpha_{0}-1} \prod_{i=1}^{\mathrm{d}} \mathrm{x}_{i}^{\alpha_{i}-1} \mathrm{~d} d, \ldots, d x_{2}, d x_{1} \end{aligned}$ <br> Numerical methods have been explored to evaluate this integral, see (Kotz et al. 2000, pp.497-500) |
| Reliability | $\begin{aligned} R(\mathbf{x}) & =\mathrm{P}\left(\mathrm{X}_{1}>\mathrm{x}_{1}, \mathrm{X}_{2}>\mathrm{x}_{2}, \ldots, \mathrm{X}_{\mathrm{d}}>\mathrm{x}_{\mathrm{d}}\right) \\ & =\int_{x_{1}}^{\infty} \int_{x_{2}}^{\infty} \ldots \int_{x_{d}}^{\infty}\left(1-\sum_{i=1}^{d} x_{i}\right)^{\alpha_{0}-1} \prod_{i=1}^{\mathrm{d}} \mathrm{x}_{i}^{\alpha_{i}-1} \mathrm{~d} d, \ldots, d x_{2}, d x_{1} \end{aligned}$ |
| Properties and Moments |  |
| Median | Solve numerically using $F(\boldsymbol{x})=0.5$ |
| Mode | $x_{i}=\frac{\alpha_{i}-1}{\alpha_{\Sigma}-d}$ for $\alpha_{i}>0$ otherwise no mode |
| Mean - $1^{\text {st }}$ Raw Moment | Let $\alpha_{\Sigma}=\sum_{i=0}^{d} \alpha_{i}$ : $E[\boldsymbol{X}]=\boldsymbol{\mu}=\frac{\boldsymbol{\alpha}}{\alpha_{\Sigma}}$ <br> Mean of the marginal distribution: $E[\boldsymbol{U}]=\boldsymbol{\mu}_{\mathbf{u}}=\frac{\boldsymbol{\alpha}_{\mathbf{u}}}{\alpha_{\Sigma}}$ $E\left[X_{i}\right]=\mu_{i}=\frac{\alpha_{i}}{\alpha_{\Sigma}}$ <br> where $\boldsymbol{\alpha}_{\mathbf{u}}=\left[\alpha_{1}, \alpha_{2}, \ldots, \alpha_{s}, \alpha_{\Sigma} \sim \sum_{j=1}^{s} \alpha_{j}\right]^{T}$ <br> Mean of the conditional distribution: $E[\boldsymbol{U} \mid \boldsymbol{V}=\boldsymbol{v}]=\boldsymbol{\mu}_{\mathbf{u} \mid \boldsymbol{v}}=\frac{\boldsymbol{\alpha}_{\mathbf{u} \mid \boldsymbol{v}}}{\alpha_{\Sigma}}$ ||  | where <br> $\alpha_{u \mid v}=\left[\alpha_{5+1}, \alpha_{c+2}, \ldots, \alpha_{m}, \alpha_{0}\right]^{T}$ |
| :-- | :-- |

# Parameter Estimation 

Maximum Likelihood Function
MLE Point The MLE estimates of $\widehat{\alpha}_{i}$ can be obtained from n observations of $\boldsymbol{x}_{\boldsymbol{i}}$ by Estimates numerically maximizing the log-likelihood function: (Kotz et al. 2000, p.505)

$$
\Lambda(\boldsymbol{\alpha} \mid \mathrm{E})=n\left\{\ln \Gamma\left(\alpha_{\Sigma}\right)-\sum_{j=0}^{d} \ln \Gamma\left(\alpha_{j}\right)\right\}+n \sum_{j=0}^{d}\left\{\frac{1}{n}\left(\alpha_{j}-1\right) \sum_{i=1}^{n} \ln \left(x_{i j}\right)\right\}
$$

The method of moments are used to provide initial guesses of $\alpha_{i}$ for the numerical methods.

| Fisher <br> Information <br> Matrix | $l_{i j}=-n \psi^{\prime}\left(\alpha_{\Sigma}\right), \quad i \neq j$ <br> $l_{i i}=n \psi^{\prime}\left(\alpha_{i}\right)-n \psi^{\prime}\left(\alpha_{\Sigma}\right)$ |
| :-- | :-- |

Where $\psi^{\prime}(x)=\frac{\alpha^{2}}{2 x^{2}} \ln \Gamma(x)$ is the trigamma function. See section 1.6.8. (Kotz et al. 2000, p.506)
$100 y \% \quad$ The confidence intervals can be obtained from the fisher information Confidence Intervals matrix.

| Bayesian |  |
| :--: | :--: |
| Non-informative Priors |  |
| Jeffery's Prior | $\sqrt{\operatorname{det}(I(\boldsymbol{\alpha}))}$ <br> where $I(\boldsymbol{\alpha})$ is given above. |
| Conjugate Priors |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \boldsymbol{p} \\ \text { from } \\ M N o m_{\mathrm{d}}\left(\boldsymbol{k} ; n_{\mathrm{f}}, \boldsymbol{p}\right) \end{gathered}$ | Multinomial $_{d}$ | $k_{i, j}$ failures in $n$ trials with $d$ possible states. | Dirichlet ${ }_{\mathrm{d}+1}$ | $\boldsymbol{\alpha}_{\boldsymbol{o}}$ | $\boldsymbol{\alpha}=\boldsymbol{\alpha}_{\boldsymbol{o}}+\boldsymbol{k}$ || Description, Limitations and Uses |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Example | Five machines are measured for performance on demand. The machines can either fail, partially fail or success in their application. The machines are tested for 10 demands with the following data for each machine: |  |  |  |  |  |  |  |  |  |
| Machine/Trail | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 1 |  | $P=2$ |  | $P=2$ |  |  | $S=5$ |  |  |  |
| 2 |  | $P=2$ |  | $P=2$ |  |  | $S=6$ |  |  |  |
| 3 |  | $P=2$ |  | $P=3$ |  |  |  | $S=5$ |  |  |
| 4 |  | $P=3$ |  |  | $P=3$ |  |  | $S=4$ |  |  |
| 5 |  | $P=2$ |  | $P=3$ |  |  |  | $S=5$ |  |  |
| $\mu_{i}$ |  | $n \bar{p}_{F}$ |  | $n \bar{p}_{F}$ |  |  |  | $n \bar{p}_{F}$ |  |  |

Estimate the multinomial distribution parameter $\boldsymbol{p}=\left[p_{F}, p_{P}, p_{S}\right]$ :
Using a non-informative improper prior $\operatorname{Dir}_{3}(0,0,0)$ after updating:

$$
\boldsymbol{x}=\left[\begin{array}{l}
p_{F} \\
p_{P} \\
p_{S}
\end{array}\right] \quad \boldsymbol{\alpha}=\left[\begin{array}{l}
12 \\
13 \\
25
\end{array}\right] \quad E[\boldsymbol{x}]=\left[\begin{array}{l}
\bar{p}_{F}=\frac{12}{58} \\
\bar{p}_{F}=\frac{13}{58} \\
\bar{p}_{S}=\frac{25}{58}
\end{array}\right] \quad \operatorname{Var}[\boldsymbol{x}]=\left[\begin{array}{l}
7.15 E-5 \\
7.54 E-5 \\
9.80 E-5
\end{array}\right]
$$

Confidence intervals for the parameters $\boldsymbol{p}=\left[p_{F}, p_{P}, p_{S}\right]$ can also be calculated using the cdf of the marginal distribution $F\left(x_{i}\right)$.

Characteristic Beta Generalization. The Dirichlet distribution is a generalization of the beta distribution. The beta distribution is seen when $d=1$.
$\boldsymbol{\alpha}$ Interpretation. The higher $\alpha_{i}$ the sharper and more certain the distribution is. This follows from its use in Bayesian statistics to model the multinomial distribution parameter $p$. As more evidence is used, the $\alpha_{i}$ values get higher which reduces uncertainty. The values of $\alpha_{i}$ can also be interpreted as a count for each state of the multinomial distribution.

Alternative Formulation. The most common formulation of the Dirichlet distribution is as follows:

$$
\begin{aligned}
& \boldsymbol{\alpha}=\left[\alpha_{1}, \alpha_{2}, \ldots, \alpha_{m}\right]^{T} \text { where } \alpha_{i}>0 \\
& \mathbf{x}=\left[x_{1}, x_{2}, \ldots, x_{m}\right]^{T} \text { where } 0 \leq \mathrm{x}_{\mathrm{i}} \leq 1, \quad \sum_{i=1}^{m} x_{i}=1 \\
& f(\mathbf{x})=\frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^{m} x_{i}^{\alpha_{i}-1}
\end{aligned}
$$

This formulation is popular because it is a more simple presentation where the matrix of $\boldsymbol{\alpha}$ and $\boldsymbol{x}$ are the same size. However it should be noted that last term of the vector $\boldsymbol{x}$ is dependent on $\left\{x_{1} \ldots x_{m-1}\right\}$ through the relationship $x_{m}=1-\sum_{i=1}^{m-1} x_{i}$.

Neutrality. (Kotz et al. 2000, p.500) If $X_{1}$ and $X_{2}$ are non negative|  | random variables such that $X_{1}+X_{2} \leq 1$ then $X_{i}$ is called neutral if the following are independent: <br> If $\boldsymbol{X} \sim \operatorname{Dir}_{d}(\boldsymbol{\alpha})$ then $\boldsymbol{X}$ is a neutral vector with each $\mathrm{X}_{\mathrm{i}}$ being neutral under all permutations of the above definition. This property is unique to the Dirichlet distribution. |
| :--: | :--: |
| Applications | Bayesian Statistics. The Dirichlet distribution is often used as a conjugate prior to the multinomial likelihood function. |
| Resources | Online: <br> http://en.wikipedia.org/wiki/Dirichlet distribution <br> http://www.cis.hut.fi/ahonkela/dippa/node95.html <br> Books: <br> Kotz, S., Balakrishnan, N. \& Johnson, N.L., 2000. Continuous Multivariate Distributions, Volume 1, Models and Applications, 2nd Edition 2nd ed., Wiley-Interscience. <br> Congdon, P., 2007. Bayesian Statistical Modelling 2nd ed., Wiley. <br> MacKay, D.J. \& Petoy, L.C., 1995. A hierarchical Dirichlet language model. Natural language engineering. |
| Relationship to Other Distributions |  |
| Beta <br> Distribution <br> $\operatorname{Beta}(x ; \alpha, \beta)$ | Special Case: $\operatorname{Dir}_{d=1}\left(\mathrm{x} ;\left[\alpha_{1}, \alpha_{0}\right]\right)=\operatorname{Beta}\left(k=x ; \alpha=\alpha_{1}, \beta=\alpha_{0}\right)$ |
| Gamma Distribution <br> $\operatorname{Gamma}(x ; \lambda, k)$ | Let: $\begin{aligned} & Y_{i} \sim \operatorname{Gamma}\left(\lambda, k_{i}\right) \text { i.i.d and } \quad V=\sum_{i=1}^{d} Y_{i} \\ & \text { Then: } \quad V \sim \operatorname{Gamma}\left(\lambda, \sum k_{i}\right) \end{aligned}$ <br> Let: $\begin{aligned} & \mathbf{Z}=\left[\frac{Y_{1}}{V}, \frac{Y_{2}}{V}, \ldots, \frac{Y_{d}}{V}\right] \\ & \mathbf{Z} \sim \operatorname{Dir}_{d}\left(\alpha_{1}, \ldots, \alpha_{k}\right) \end{aligned}$ |
|  | Then: $\quad \mathbf{Z} \sim \operatorname{Dir}_{d}\left(\alpha_{1}, \ldots, \alpha_{k}\right)$ <br> *i.i.d: independent and identically distributed |# 6.3. Multivariate Normal Continuous Distribution 

*Note for a graphical representation see bivariate normal distribution

| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $\boldsymbol{\mu}=\left[\begin{array}{lll}\mu_{1}, \mu_{2}, \ldots, \mu_{d}\end{array}\right]^{T}$ | $-\infty<\mu_{i}<\infty$ | Location Vector: A ddimensional vector giving the mean of each random variable. |
|  | $\sum=\left[\begin{array}{llll}\sigma_{11} & \cdots & \sigma_{1 d} \\ \vdots & \ddots & \vdots \\ \sigma_{d 1} & \cdots & \sigma_{d d}\end{array}\right]$ | $\sigma_{i i}>0$ <br> $\sigma_{i j} \geq 0$ | Covariance Matrix: A $d \times d$ matrix which quantifies the random variable variance and dependence. This matrix determines the shape of the distribution. $\Sigma$ is symmetric positive definite matrix. |
|  | $d$ | $\begin{gathered} d \geq 2 \\ \text { (integer) } \end{gathered}$ | Dimensions. The number of dependent variables. |
| Limits | $-\infty<\mathrm{x}_{\mathrm{i}}<\infty$ |  |  |
| Distribution | Formulas |  |  |
| PDF | $f(\mathbf{x})=\frac{1}{(2 \pi)^{d / 2} \sqrt{|\boldsymbol{\Sigma}|}} \exp \left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\mathrm{T}} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right]$ <br> Where $|\boldsymbol{\Sigma}|$ is the determinant of $\boldsymbol{\Sigma}$. |  |  |
| Marginal PDF | Let $\quad \boldsymbol{X}=\left[\begin{array}{l}\boldsymbol{U} \\ \boldsymbol{V}\end{array}\right] \sim \operatorname{Norm}_{d}\left(\left[\begin{array}{l}\boldsymbol{\mu}_{u} \\ \boldsymbol{\mu}_{v}\end{array}\right],\left[\begin{array}{ll}\boldsymbol{\Sigma}_{u u} & \boldsymbol{\Sigma}_{u v} \\ \boldsymbol{\Sigma}_{u v}^{\prime} & \boldsymbol{\Sigma}_{v v}\end{array}\right]\right)$ <br> $\boldsymbol{X}=\left[X_{1}, \ldots, X_{p}, X_{p+1}, \ldots, X_{d}\right]^{T}$ <br> $\boldsymbol{U}=\left[X_{1}, \ldots, X_{p}\right]^{T}$ <br> $\boldsymbol{V}=\left[X_{p+1}, \ldots, X_{d}\right]^{T}$ |  |  |
|  | $\boldsymbol{U} \sim \operatorname{Norm}_{p}\left(\boldsymbol{\mu}_{\mathbf{u}}, \boldsymbol{\Sigma}_{\mathbf{u u}}\right)$ $f(\mathbf{u})=\int_{-\infty}^{\infty} f(\boldsymbol{x}) d \boldsymbol{v}$ <br> $=\frac{1}{(2 \pi)^{p / 2} \sqrt{\left|\boldsymbol{\Sigma}_{\mathbf{u u}}\right|}} \exp \left[-\frac{1}{2}\left(\mathbf{u}-\boldsymbol{\mu}_{\mathbf{u}}\right)^{\mathrm{T}} \boldsymbol{\Sigma}_{\mathrm{uu}}^{-1}\left(\mathbf{u}-\boldsymbol{\mu}_{\mathbf{u}}\right)\right]$ |  |  |
| Conditional PDF | $\boldsymbol{U} \mid \boldsymbol{V}=\boldsymbol{v} \sim \operatorname{Norm}_{p}\left(\boldsymbol{\mu}_{u \mid v}, \boldsymbol{\Sigma}_{u \mid v}\right)$ |  |  ||  | Where $\quad \boldsymbol{\mu}_{u \mid v}=\boldsymbol{\mu}_{u}+\boldsymbol{\Sigma}_{u v}^{T} \boldsymbol{\Sigma}_{v v}^{-1}\left(\boldsymbol{v}-\boldsymbol{\mu}_{v}\right)$ <br> $\boldsymbol{\Sigma}_{u \mid v}=\boldsymbol{\Sigma}_{u u}-\boldsymbol{\Sigma}_{u v}^{T} \boldsymbol{\Sigma}_{v v}^{-1} \boldsymbol{\Sigma}_{u v}$ |
| :-- | :--: |
| CDF | $F(\mathbf{x})=\frac{1}{(2 \pi)^{d / 2} \sqrt{|\boldsymbol{\Sigma}|}} \int_{-\infty}^{\mathbf{x}} \exp \left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\mathrm{T}} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right] \mathrm{d} \boldsymbol{x}$ |
| Reliability | $R(\mathbf{x})=\frac{1}{(2 \pi)^{d / 2} \sqrt{|\boldsymbol{\Sigma}|}} \int_{\mathbf{x}}^{\infty} \exp \left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\mathrm{T}} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right] \mathrm{d} \boldsymbol{x}$ |
| Properties and Moments |  |
| Median | $\boldsymbol{\mu}$ |
| Mode | $\boldsymbol{\mu}$ |
| Mean - $1^{\text {st }}$ Raw Moment | $E[\boldsymbol{X}]=\boldsymbol{\mu}$ <br> Mean of the marginal distribution: $\begin{aligned} & E[\boldsymbol{U}]=\boldsymbol{\mu}_{u} \\ & E[\boldsymbol{V}]=\boldsymbol{\mu}_{v} \end{aligned}$ <br> Mean of the conditional distribution: $\begin{aligned} & \boldsymbol{\mu}_{u \mid v}=\boldsymbol{\mu}_{u}+\boldsymbol{\Sigma}_{u v}^{T} \boldsymbol{\Sigma}_{v v}^{-1}\left(\boldsymbol{v}-\boldsymbol{\mu}_{v}\right) \end{aligned}$ |
| Variance - $2^{\text {nd }}$ Central Moment | $\operatorname{Cov}[\boldsymbol{X}]=\boldsymbol{\Sigma}$ <br> Covariance of marginal distributions: $\operatorname{Cov}(\mathbf{U})=\boldsymbol{\Sigma}_{\mathbf{u u}}$ <br> Covariance of conditional distributions: $\operatorname{Cov}(\mathbf{U} \mid \mathbf{V})=\boldsymbol{\Sigma}_{u u}-\boldsymbol{\Sigma}_{u v}^{T} \boldsymbol{\Sigma}_{v v}^{-1} \boldsymbol{\Sigma}_{u v}$ |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| MLE Point <br> Estimates | When given complete data of $n_{F}$ samples: $\boldsymbol{x}_{\boldsymbol{t}}=\left[\boldsymbol{x}_{1, t}, \boldsymbol{x}_{2, t}, \ldots, \boldsymbol{x}_{d, t}\right]^{\boldsymbol{T}}$ where $t=\left(1,2, \ldots, n_{F}\right)$ <br> The following MLE estimates are given: (Kotz et al. 2000, p.161) $\begin{gathered} \widehat{\boldsymbol{\mu}}=\frac{1}{n_{F}} \sum_{t=1}^{n_{F}} \boldsymbol{x}_{t} \\ \widehat{\Sigma}_{i j}=\frac{1}{n_{F}} \sum_{t=1}^{n_{F}}\left(x_{i, t}-\widehat{\mu}_{i}\right)\left(x_{j, t}-\widehat{\mu}_{j}\right) \end{gathered}$ <br> A review of different estimators is given in (Kotz et al. 2000). When estimates are from a low number of samples $\left(n_{F}<30\right)$ a correction ||  | factor of -1 can be introduced to give the unbiased estimators (Tong 1990, p.53): $\begin{aligned} & \hat{\Sigma}_{i j}=\frac{1}{n_{F}-1} \sum_{t=1}^{n_{F}}\left(x_{i, t}-\widehat{\mu}_{i}\right)\left(x_{j, t}-\widehat{\mu}_{j}\right) \\ & \hline \end{aligned}$ |
| :--: | :--: |
| Fisher <br> Information <br> Matrix | $I_{i, j}=\frac{\partial \mu^{T}}{\partial \theta_{i}} \Sigma^{-1} \frac{\partial \mu}{\partial \theta_{j}}$ |
| Bayesian |  |
| Non-informative Priors when $\boldsymbol{\Sigma}$ is known, $\pi_{0}(\boldsymbol{\mu})$ (Yang and Berger 1998, p.22) |  |
| Type | Prior | Posterior |
| Uniform <br> Improper, Jeffrey, <br> Reference Prior | 1 | $\begin{aligned} & \pi(\boldsymbol{\mu} \mid \boldsymbol{E}) \sim \operatorname{Norm}_{d}\left(\mu ; \frac{1}{n_{F}} \sum_{t=1}^{n_{F}} \boldsymbol{x}_{t}, \frac{\boldsymbol{\Sigma}}{n_{F}}\right) \\ & \text { when } \boldsymbol{\mu} \in(\infty, \infty) \end{aligned}$ |
| Shrinkage | $\left(\boldsymbol{\mu}^{T} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}^{T}\right)^{-(d-2)}$ | No Closed Form |
| Non-informative Priors when $\boldsymbol{\mu}$ is known, $\pi_{o}(\boldsymbol{\Sigma})$ (Yang \& Berger 1994) |  |  |
| Type | Prior | Posterior |
| Uniform Improper Prior with limits $\boldsymbol{\Sigma} \in(0, \infty)$ | 1 | $\begin{gathered} \pi\left(\boldsymbol{\Sigma}^{-1} \mid \boldsymbol{E}\right) \sim \\ \text { Wishart }_{d}\left(\boldsymbol{\Sigma}^{-1} ; n_{F}-d-1, \frac{\boldsymbol{\Sigma}^{-1}}{n_{F}}\right) \end{gathered}$ |
| Jeffery's Prior | $\frac{1}{|\boldsymbol{\Sigma}|^{\frac{d+1}{2}}}$ | $\begin{gathered} \pi\left(\boldsymbol{\Sigma}^{-1} \mid \boldsymbol{E}\right) \sim \\ \text { Wishart }_{d}\left(\boldsymbol{\Sigma}^{-1} ; n_{F}, \frac{\boldsymbol{\Sigma}^{-1}}{n_{F}}\right) \\ \text { with limits } \boldsymbol{\Sigma} \in(0, \infty) \end{gathered}$ |
| Reference Prior <br> Ordered $\left\{\lambda_{i}, \lambda_{j}, \ldots, \lambda_{d}\right\}$ | $\frac{1}{|\boldsymbol{\Sigma}| \prod_{i<j}\left(\lambda_{i}-\lambda_{j}\right)}$ | Proper - No Closed Form |
| Reference Prior <br> Ordered $\left\{\lambda_{1}, \lambda_{d}, \lambda_{i}, \ldots, \lambda_{d-1}\right\}$ | $\frac{1}{|\boldsymbol{\Sigma}|\left(\log \lambda_{1}-\log \lambda_{d}\right)^{d-2} \prod_{i<j}\left(\lambda_{i}-\lambda_{j}\right)}$ | Proper - No Closed Form |
| MDIP | $\frac{1}{|\boldsymbol{\Sigma}|}$ | No Closed Form |
| Non-informative Priors when $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are unknown for bivariate normal, $\pi_{o}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. A complete coverage of numerous reference prior distributions with different parameter ordering is contained in (Berger \& Sun 2008) |  |  || Type | Prior | Posterior |
| :--: | :--: | :--: |
| Uniform Improper <br> Prior | 1 | No Closed Form |
| Jeffery's Prior | $\frac{1}{|\Sigma|^{\frac{d+1}{2}}}$ | No Closed Form |
| Reference Prior <br> Ordered $\left\{\lambda_{i}, \lambda_{j}, \ldots, \lambda_{d}\right\}$ | $\frac{1}{|\Sigma|\prod_{i<j}\left(\lambda_{i}-\lambda_{j}\right)}$ | No Closed Form |
| Reference Prior <br> Ordered <br> $\left\{\lambda_{1}, \lambda_{d}, \lambda_{i}, \ldots, \lambda_{d-1}\right\}$ | $\frac{1}{|\Sigma|\left(\log \lambda_{1}-\log \lambda_{d}\right)^{d-2} \prod_{i<j}\left(\lambda_{i}-\lambda_{j}\right)}$ | No Closed Form |
| MDIP | $\frac{1}{|\Sigma|}$ | No Closed Form |

where $\lambda_{i}$ is the $i^{\text {th }}$ eigenvalue of $\Sigma$, and $\bar{R}$ and $R$ are population and sample multiple correlation coefficients where:

$$
S_{i j}=\frac{1}{n_{F}-1} \sum_{t=1}^{n_{F}}\left(x_{i, t}-\bar{\mu}_{i}\right)\left(x_{j, t}-\bar{\mu}_{j}\right) \quad \text { and } \quad \bar{x}=\frac{1}{n_{F}} \sum_{t=1}^{n_{F}} x_{t}
$$

| Conjugate Priors |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| UOI | Likelihood <br> Model | Evidenc <br> e | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \boldsymbol{\mu} \\ \text { from } \\ \operatorname{Norm}_{d}(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \end{gathered}$ | Multi-variate Normal with known $\boldsymbol{\Sigma}$ | $n_{F}$ events at $\boldsymbol{x}$ points | Multi- <br> variate <br> Normal | $\boldsymbol{U}_{0}, \mathbf{V}_{0}$ | $\boldsymbol{U}=\frac{\mathbf{V}_{0}^{-1} \mathbf{U}_{\mathbf{e}}+\mathrm{n}_{\mathrm{F}} \mathbf{V}^{-1} \overline{\mathbf{x}}}{\mathbf{V}_{0}^{-1}+\mathrm{n}_{\mathrm{F}} \Sigma^{-1}}$ <br> $\mathbf{V}=\frac{1}{\mathbf{V}_{0}^{-1}+\mathrm{n}_{\mathrm{F}} \Sigma^{-1}}$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | See bivariate normal distribution. |  |  |  |  |
| Characteristic | Standard Spherical Normal Distribution. When $\boldsymbol{\mu}=0, \boldsymbol{\Sigma}=I$ we obtain the standard spherical normal distribution: $f(\mathbf{x})=\frac{1}{(2 \pi)^{d / 2}} \exp \left[-\frac{1}{2} \mathbf{x}^{T} \mathbf{x}\right]$ <br> Covariance Matrix. (Yang et al. 2004, p.49) <br> - Diagonal Elements. The diagonal elements of $\Sigma$ is the variance of each random variable. $\sigma_{i j}=\operatorname{Var}\left(X_{i}\right)$ <br> - Non Diagonal Elements. Non diagonal elements give the covariance $\sigma_{i j}=\operatorname{Cov}\left(X_{i}, X_{j}\right)=\sigma_{j i}$. Hence the matrix is symmetric. <br> - Independent Variables. If $\operatorname{Cov}\left(X_{i}, X_{j}\right)=\sigma_{i j}=0$ then $X_{i}$ and |  |  |  |  |  |$X_{j}$ and independent.

- $\quad \sigma_{i j}>0$. When $X_{i}$ increases then $X_{j}$ and tends to increase.
- $\quad \sigma_{i j}<0$. When $X_{i}$ increases then $X_{j}$ and tends to decrease.

Ellipsoid Axis. The ellipsoids has axes pointing in the direction of the eigenvectors of $\Sigma$. The magnitude of these axes are given by the corresponding eigenvalues.

# Mean / Median / Mode: 

As per the univariate distributions the mean, median and mode are equal.

## Convolution Property

Let

$$
X \sim \operatorname{Norm}_{d}\left(\mu_{x}, \Sigma_{x}\right) \quad Y \sim \operatorname{Norm}_{d}\left(\mu_{y}, \Sigma_{y}\right)
$$

Where

$$
X \perp Y \text { (independent) }
$$

Then

$$
X+Y \sim \operatorname{Norm}_{d}\left(\mu_{x}+\mu_{y}, \Sigma_{x}+\Sigma_{y}\right)
$$

Note if $\mathbf{X}$ and $\mathbf{Y}$ are dependent then $\mathbf{X}+\mathbf{Y}$ may not be normally distributed. (Novosyolov 2006)

## Scaling Property

Let

$$
Y=A X+b \quad \begin{aligned}
& \text { Y is a p } \times 1 \text { matrix } \\
& \text { b is a p } \times 1 \text { matrix }
\end{aligned}
$$

Then

$$
Y \sim \operatorname{Norm}_{d}\left(A \mu+b, A \Sigma A^{T}\right) \quad \text { A is a p } \times \text { d matrix }
$$

## Marginalize Property:

Let

$$
X=\left[\begin{array}{l}
U \\
V
\end{array}\right] \sim \operatorname{Norm}_{d}\left(\left[\begin{array}{l}
\mu_{u} \\
\mu_{v}
\end{array}\right],\left[\begin{array}{ll}
\Sigma_{u u} & \Sigma_{u v} \\
\Sigma_{u v}^{T} & \Sigma_{v v}
\end{array}\right]\right)
$$

Then

$$
U \sim \operatorname{Norm}_{p}\left(\mu_{u}, \Sigma_{u u}\right) \quad U \text { is a p } \times 1 \text { matrix }
$$

## Conditional Property:

Let

$$
X=\left[\begin{array}{l}
U \\
V
\end{array}\right] \sim \operatorname{Norm}_{d}\left(\left[\begin{array}{l}
\mu_{u} \\
\mu_{v}
\end{array}\right],\left[\begin{array}{ll}
\Sigma_{u u} & \Sigma_{u v} \\
\Sigma_{u v}^{T} & \Sigma_{v v}
\end{array}\right]\right)
$$

Then

$$
U \mid V=v \sim \operatorname{Norm}_{p}\left(\mu_{u \mid v}, \Sigma_{u \mid v}\right) \quad U \text { is a p } \times 1 \text { matrix }
$$

Where

$$
\begin{aligned}
& \mu_{u \mid v}=\mu_{u}+\Sigma_{u v}^{T} \Sigma_{v v}^{-1}\left(V-\mu_{v}\right) \\
& \Sigma_{u \mid v}=\Sigma_{u u}-\Sigma_{u v}^{T} \Sigma_{v v}^{-1} \Sigma_{u v}
\end{aligned}
$$

It should be noted that the standard deviation of the marginal distribution does not depend on the given values in $\mathbf{V}$.

| Applications | Convenient Properties. (Balakrishnan \& Lai 2009, p.477) Popularity <br> of the multivariate normal distribution over other multivariate <br> distributions is due to the convenience of the conditional and marginal <br> distribution properties which both produce univariate normal <br> distributions. |
| :-- | :-- |Kalman Filter. The Kalman filter estimates the current state of a system in the presence of noisy measurements. This process uses multivariate normal distributions to model the noise.

Multivariate Analysis of Variance (MANOVA). A test used to analyze variance and dependence of variables. A popular model used to conduct MANOVA assumes the data comes from a multivariate normal population.

Multi-Linear Regression. Multi-linear regression attempts to model the relationship between parameters and variables by fitting a linear equation. One model to do such a task (MLE) fits a distribution to the observed variance where a multivariate normal distribution is often assumed.

Gaussian Bayesian Belief Networks (BBN). BBNs graphical represent the dependence between variables in a probability distribution. When using continuous random variables BBNs quickly become tremendously complicated. However due to the multivariate normal distribution's conditional and marginal properties this task is simplified and popular.

| Resources | Online: |
| :-- | :-- |
|  | http://mathworld.wolfram.com/BivariateNormalDistribution.html |
|  | http://www.aiaccess.net/English/Glossaries/GlosMod/e_gm_binormal |
|  | _distri.htm (interactive visual representation) |
|  | Books: |
|  | Patel, J.K, Read, C.B, 1996. Handbook of the Normal Distribution, $2^{\text {nd }}$ |
|  | Edition, CRC |
|  | Tong, Y.L., 1990. The Multivariate Normal Distribution, Springer. |
|  | Yang, K. et al., 2004. Multivariate Statistical Methods in Quality |
|  | Management 1st ed., McGraw-Hill Professional. |
|  | Bertsekas, D.P. \& Tsitsiklis, J.N., 2008. Introduction to Probability, |
|  | 2nd Edition, Athena Scientific. |# 6.4. Multinomial Discrete Distribution 

Probability Density Function - $f(\mathbf{k})$


Trinomial Distribution, $f\left(\left[k_{1}, k_{2}, k_{3}\right]^{T}\right)$ where $n=8, \mathbf{p}=\left[\frac{1}{3}, \frac{1}{4}, \frac{1}{12}\right]^{T}$. Note $k_{3}$ is not shown because it is determined using $k_{3}=n-k_{1}-k_{2}$


Trinomial Distribution, $f\left(\left[k_{1}, k_{2}, k_{3}\right]^{T}\right)$ where $n=20, \mathbf{p}=\left[\frac{1}{3}, \frac{1}{2}, \frac{1}{6}\right]^{T}$. Note $k_{3}$ is not shown because it is determined as $k_{3}=n-k_{1}-k_{2}$| Parameters \& Description |  |  |  |
| :--: | :--: | :--: | :--: |
| Parameters | $n$ | $\begin{gathered} \mathrm{n}>0 \\ \text { (integer) } \end{gathered}$ | Number of Trials. This is sometimes called the index. (Johnson et al. 1997, p.31) |
|  | $\mathbf{p}=\left[p_{1}, p_{2}, \ldots, p_{d}\right]^{T}$ | $\begin{gathered} 0 \leq \mathrm{p}_{\mathrm{i}} \leq 1 \\ \sum_{i=1}^{d} p_{i}=1 \end{gathered}$ | Event Probability Matrix: The probability of event $i$ occurring. $p_{i}$ is often called cell probabilities. (Johnson et al. 1997, p.31) |
|  | $d$ | $\begin{gathered} d \geq 2 \\ \text { (integer) } \end{gathered}$ | Dimensions. The number of mutually exclusive states of the system. |
| Limits | $\mathrm{k}_{\mathrm{i}} \in\{0, \ldots, n\}$ <br> $\sum_{i=1}^{d} k_{i}=n$ |  |  |
| Distribution | Formulas |  |  |
| PDF | where $\begin{gathered} f(\mathbf{k})=\left(\begin{array}{c}\mathrm{n} \\ \left.\mathrm{k}_{1}, \mathrm{k}_{2}, \ldots, \mathrm{k}_{\mathrm{d}}\right) \prod_{\mathrm{i}=1}^{\mathrm{d}} \mathrm{p}_{\mathrm{i}}^{\mathrm{k}_{\mathrm{i}}} \\ \left.\mathrm{k}_{1}, \mathrm{k}_{2}, \ldots, \mathrm{k}_{\mathrm{n}}\right)=\frac{\mathrm{n}!}{\mathrm{k}_{1}!\mathrm{k}_{2}!\ldots \mathrm{k}_{\mathrm{d}!}}=\frac{\mathrm{n}!}{\prod_{\mathrm{i}=1}^{\mathrm{d}} \mathrm{k}_{\mathrm{i}!}}=\frac{\Gamma(\mathrm{n}+1)}{\prod_{\mathrm{i}=1}^{\mathrm{d}} \Gamma\left(\mathrm{k}_{\mathrm{i}}+1\right)} \end{gathered}$ <br> Note that in $p$ there is only $d-1$ 'free' variables as the last $p_{d}=1-\sum_{i=1}^{d-1} p_{i}$ giving the distribution: $\begin{gathered} f(\mathbf{k})=\left(\begin{array}{c}\mathrm{n} \\ \left.\mathrm{k}_{1}, \mathrm{k}_{2}, \ldots, \mathrm{k}_{\mathrm{n}}\right) \prod_{\mathrm{i}=1}^{\mathrm{d}-1} \mathrm{p}_{\mathrm{i}}^{\mathrm{k}_{\mathrm{i}}} \cdot\left(1-\sum_{\mathrm{i}=1}^{\mathrm{s}} \mathrm{p}_{\mathrm{i}}\right)^{\mathrm{n}-\sum_{i=1}^{\mathrm{d}-1} \mathrm{k}_{\mathrm{i}}} \\ \text { Now the special case of binomial distribution when } d=2 \text { can be } \\ \text { seen. } \end{gathered}$ |  |  |
| Marginal PDF | Let <br> Where | $\begin{aligned} & \boldsymbol{K}=\left[\begin{array}{l} \boldsymbol{U} \\ \boldsymbol{V} \end{array}\right] \sim M N o m_{d}\left(n,\left[\begin{array}{l} \boldsymbol{p}_{\boldsymbol{u}} \\ \boldsymbol{p}_{\boldsymbol{v}} \end{array}\right]\right) \\ & \boldsymbol{K}=\left[K_{1}, \ldots, K_{s}, K_{s+1}, \ldots, K_{d}\right]^{T} \\ & \boldsymbol{U}=\left[K_{1}, \ldots, K_{s}\right]^{T} \\ & \boldsymbol{V}=\left[K_{s+1}, \ldots, K_{d}\right]^{T} \end{aligned}$ |  |
|  | where | $\boldsymbol{p}_{\boldsymbol{u}}=\left[p_{1}, p_{2}, \ldots, p_{s-1},\left(1-\sum_{i=1}^{s-1} p_{i}\right)\right]^{T}$ |  ||  | $f(\boldsymbol{u})=\left(\begin{array}{c}\mathrm{n} \\ \mathrm{k}_{1}, \mathrm{k}_{2}, \ldots, \mathrm{k}_{\mathrm{s}}\end{array}\right) \prod_{\mathrm{i}=1}^{3} \mathrm{p}_{\mathrm{i}}^{\mathrm{k}_{\mathrm{i}}}$ <br> When only two states $\boldsymbol{p}=[p,(1-p)]^{T}:$ <br> $f\left(k_{i}\right)=\left(\begin{array}{l}\mathrm{n} \\ \mathrm{k}_{\mathrm{i}}\end{array}\right) \mathrm{p}_{\mathrm{i}}^{\mathrm{k}_{\mathrm{i}}}\left(1-p_{i}\right)^{n-k_{i}}$ |
| :--: | :--: | :--: |
| Conditional PDF | $\boldsymbol{U} \mid \boldsymbol{V}=\boldsymbol{v} \sim M N o m_{x}\left(n_{u \mid v}, \boldsymbol{p}_{u \mid v}\right)$ <br> where $\quad n_{u \mid v}=n-n_{v}=n-\sum_{i=s+1}^{d} k_{i}$ <br> $\boldsymbol{p}_{u \mid v}=\frac{1}{\sum_{i=1}^{3} p_{i}}\left[p_{1}, p_{2}, \ldots, p_{s}\right]^{T}$ |
| CDF | $\begin{aligned} F(\mathbf{k}) & =\mathrm{P}\left(\mathrm{~K}_{1} \leq \mathrm{k}_{1}, \mathrm{~K}_{2} \leq \mathrm{k}_{2}, \ldots, \mathrm{~K}_{\mathrm{d}} \leq \mathrm{k}_{\mathrm{d}}\right) \\ & =\sum_{\mathrm{j}_{1}=0}^{\mathrm{k}_{1}} \sum_{\mathrm{j}_{2}=0}^{\mathrm{k}_{2}} \ldots \sum_{\mathrm{j}_{d}=0}^{\mathrm{k}_{\mathrm{d}}}\left(\mathrm{j}_{1}, \mathrm{j}_{2}, \ldots, \mathrm{j}_{\mathrm{d}}\right) \prod_{\mathrm{i}=1}^{\mathrm{d}} \mathrm{p}_{\mathrm{i}}^{\mathrm{j}_{\mathrm{i}}} \end{aligned}$ |
| Reliability | $\begin{aligned} R(\mathbf{k}) & =\mathrm{P}\left(\mathrm{~K}_{1}>\mathrm{k}_{1}, \mathrm{~K}_{2}>\mathrm{k}_{2}, \ldots, \mathrm{~K}_{\mathrm{d}}>\mathrm{k}_{\mathrm{d}}\right) \\ & =\sum_{\mathrm{j}_{1}=\mathrm{k}_{1}+1}^{\mathrm{n}} \sum_{\mathrm{j}_{2}=\mathrm{k}_{2}+1}^{\mathrm{n}} \ldots \sum_{\mathrm{j}_{\mathrm{d}}=\mathrm{k}_{\mathrm{d}}+1}^{\mathrm{n}}\left(\mathrm{j}_{1}, \mathrm{j}_{2}, \ldots, \mathrm{j}_{\mathrm{d}}\right) \prod_{\mathrm{i}=1}^{\mathrm{d}} \mathrm{p}_{\mathrm{i}}^{\mathrm{j}_{\mathrm{i}}} \end{aligned}$ |
| Properties and Moments |  |
| Median $^{3}$ | $\operatorname{Median}\left(k_{i}\right)$ is either $\left\{\left[n p_{i}\right],\left[n p_{i}\right]\right\}$ |
| Mode | $\operatorname{Mode}\left(k_{i}\right)=\left\{(n+1) p_{i}\right\}$ |
| Mean - $1^{\text {st }}$ Raw Moment | $E[\boldsymbol{K}]=\boldsymbol{\mu}=n \boldsymbol{p}$ <br> Mean of the marginal distribution: $\begin{aligned} & E[\boldsymbol{U}]=\boldsymbol{\mu}_{\boldsymbol{u}}=n \boldsymbol{p}_{\boldsymbol{u}} \\ & E\left[K_{i}\right]=\mu_{k_{i}}=n p_{i} \end{aligned}$ <br> Mean of the conditional distribution: $\begin{aligned} & E[\boldsymbol{U} \mid \boldsymbol{V}=\boldsymbol{v}]=\boldsymbol{\mu}_{u \mid v}=n_{u \mid v} \boldsymbol{p}_{u \mid v} \\ & \text { where } \end{aligned}$ $\begin{aligned} & n_{u \mid v}=n-n_{v}=n-\sum_{i=s+1}^{d} k_{i} \\ & \boldsymbol{p}_{u \mid v}=\frac{1}{\sum_{i=1}^{3} p_{i}}\left[p_{1}, p_{2}, \ldots, p_{s}\right]^{T} \end{aligned}$ |

[^0]
[^0]:    ${ }^{3}[x]=$ is the floor function (largest integer not greater than $x$ ) $[x]=$ is the ceiling function (smallest integer not less than $x$ )| Variance $\cdot 2^{\text {nd }}$ Central Moment | $\begin{gathered} \operatorname{Var}\left[K_{i}\right]=n p_{i}\left(1-p_{i}\right) \\ \operatorname{Cov}\left[K_{i}, K_{j}\right]=-n p_{i} p_{j} \end{gathered}$ <br> Covariance of marginal distributions: $\operatorname{Var}\left[K_{i}\right]=n p_{i}\left(1-p_{i}\right)$ <br> Covariance of conditional distributions: $\operatorname{Var}\left[K_{U \mid V, i}\right]=n_{u \mid v} p_{u \mid v, i}\left(1-p_{u \mid v, i}\right)$ $\operatorname{Cov}\left[K_{U \mid V, i}, K_{U \mid V, j}\right]=-n_{u \mid v} p_{u \mid v, i} p_{u \mid v, j}$ <br> where $\begin{aligned} & n_{u \mid v}=n-n_{v}=n-\sum_{i=z+1}^{d} k_{i} \\ & \boldsymbol{p}_{u \mid v}=\frac{1}{\sum_{i=1}^{z} p_{i}}\left[p_{1}, p_{2}, \ldots, p_{z}\right]^{T} \end{aligned}$ |
| :--: | :--: |
| Parameter Estimation |  |
| Maximum Likelihood Function |  |
| MLE Point Estimates | As with the binomial distribution the MLE estimates, given the vector k (and therefore n ), is:(Johnson et al. 1997, p.51) $\overline{\mathbf{p}}=\frac{\mathbf{k}}{\mathrm{n}}$ <br> Where there are $T$ observations of $\boldsymbol{k}_{t}$ each containing $n_{t}$ trails: $\overline{\mathbf{p}}=\frac{1}{\sum_{l=1}^{d} n_{l}} \sum_{t=1}^{T} \boldsymbol{k}_{t}$ |
| $100 \gamma \%$ <br> Confidence <br> Intervals <br> (Complete <br> Data) | An approximation of the joint interval confidence limits for $100 \gamma \%$ given by Goodman in 1965 is:(Johnson et al. 1997, p.51) <br> $p_{i}$ lower confidence limit: $\begin{aligned} & \frac{1}{2(n+A)}\left[A+2 k_{i}-A \sqrt{A+\frac{4}{n} k_{i}\left(n-k_{i}\right)}\right] \\ & p_{i} \text { upper confidence limit: } \end{aligned}$ $\frac{1}{2(n+A)}\left[A+2 k_{i}+A \sqrt{A+\frac{4}{n} k_{i}\left(n-k_{i}\right)}\right]$ <br> where $\Phi$ is the standard normal CDF and: $\begin{gathered} A=\underline{Z_{\frac{d-1+\gamma}{d}}}=\Phi^{-1}\left(\frac{d-1+\gamma}{d}\right) \end{gathered}$ ||  | A complete coverage of estimation techniques and confidence intervals is contained in (Johnson et al. 1997, pp.51-65). A more accurate method which requires numerical methods is given in (Sison \& Glaz 1995) |
| :--: | :--: |
| Bayesian |  |
| Non-informative Priors, $\pi(p)$ <br> (Yang and Berger 1998, p.6) |  |
| Type | Prior Posterior |
| Uniform Prior | $1=\operatorname{Dir}_{d+1}\left(\alpha_{i}=1\right)$ <br> $\operatorname{Dir}_{d+1}(\mathbf{p} \mid 1+\mathbf{k})$ |
| Jeffreys Prior <br> One Group - <br> Reference Prior | $\frac{C}{\sqrt{\prod_{i=1}^{d} p_{i}}}=\operatorname{Dir}_{d+1}\left(\alpha_{i}=\frac{1}{2}\right)$ <br> Dir $d+1\left(\mathbf{p} \left\lvert\, \frac{1}{2}+\mathbf{k}\right.\right.$ ) <br> where $C$ is a constant |
|  | In terms of the reference prior, this approach considers all parameters are of equal importance.(Berger \& Bernardo 1992) |
| d-group <br> Reference Prior | $\frac{C}{\sqrt{\prod_{i=1}^{d-1}\left[p_{i}\left(1-\sum_{j=1}^{i} p_{i}\right)\right]}}$ <br> Proper. See m-group posterior <br> when $m=1$. <br> where $C$ is a constant |
|  | This approach considers each parameter to be of different importance (group length 1) and so the parameters must be ordered by importance. (Berger \& Bernardo 1992) |
| m-group <br> Reference Prior | $\pi_{a}(\boldsymbol{p})=\frac{C}{\sqrt{\left(1-\sum_{j=1}^{N_{m}} p_{j}\right) \prod_{i=1}^{d-1} p_{i} \prod_{i=1}^{m-1}\left(1-\sum_{j=1}^{N_{i}} p_{j}\right)^{\frac{N_{i+1}}{N_{i+1}}}}}$ <br> where groups are given by: $\begin{gathered} \mathbf{p}_{1}=\left[p_{1}, \ldots p_{n_{1}}\right]^{T}, \quad \mathbf{p}_{2}=\left[p_{n_{1}+1}, \ldots, p_{n_{1}+n_{2}}\right]^{T} \\ N_{j}=n_{1}+\cdots+n_{j} \text { for } j=1, \ldots, m \\ \mathbf{p}_{\mathbf{i}}=\left[p_{N_{j-1}+1}, \ldots, p_{N_{j}}\right]^{T} \\ C \text { is a constant } \end{gathered}$ <br> Posterior: $\pi(\boldsymbol{p} \mid \boldsymbol{k}) \propto \frac{\left(1-\sum_{j=1}^{N_{m}} p_{i}\right)^{k_{d}-\frac{1}{2}}}{\sqrt{\prod_{i=1}^{d-1} p_{i} \prod_{i=1}^{m-1}\left(1-\sum_{j=1}^{N_{i}} p_{j}\right)^{\frac{N_{i+1}}{N_{i+1}}}}} \end{gathered}$ <br> This approach splits the parameters into $m$ different groups of importance. Within the group order is not important, but the groups need to be ordered by importance. It is common to have $m=2$ and split the parameters into importance and nuisance parameters. (Berger \& Bernardo 1992) || MDIP | $\prod_{i=1}^{d} p_{i}^{p_{i}}=D i r_{d+1}\left(\alpha_{i}=p_{i}+1\right)$ |  |  | $D i r_{d+1}\left(\mathbf{p}^{\prime} \mid p_{i}+1+\mathrm{k}_{\mathrm{i}}\right)$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Novick and Hall's <br> Prior (improper) | $\prod_{i=1}^{d} p_{i}^{-1}=D i r_{d+1}\left(\alpha_{i}=0\right)$ |  |  | $D i r_{d+1}(\mathbf{p} \mid \mathbf{k})$ |  |
| Conjugate Priors (Fink 1997) |  |  |  |  |  |
| UOI | Likelihood <br> Model | Evidence | Dist of <br> UOI | Prior <br> Para | Posterior <br> Parameters |
| $\begin{gathered} \boldsymbol{p} \\ \text { from } \\ M N o m_{d}\left(\boldsymbol{k} ; n_{t}, \boldsymbol{p}\right) \end{gathered}$ | Multinomial $_{d}$ | $k_{i, j}$ failures in $n$ trials with $d$ possible states. | Dirichlet $_{d+1}$ | $\boldsymbol{\alpha}_{\boldsymbol{o}}$ | $\boldsymbol{\alpha}=\boldsymbol{\alpha}_{\boldsymbol{o}}+\boldsymbol{k}$ |
| Description, Limitations and Uses |  |  |  |  |  |
| Example | A six sided dice being thrown 60 times produces the following multinomial distribution: |  |  |  |  |
|  | Face <br> Number | Times <br> Observed | $\boldsymbol{k}=\left[\begin{array}{c}12 \\ 6 \\ 12 \\ 10 \\ 8 \\ 12\end{array}\right]$ | $\boldsymbol{p}=\left[\begin{array}{c}0.2 \\ 0.1 \\ 0.2 \\ 0.16 \\ 0.13 \\ 0.2\end{array}\right]$ | $n=60$ |
| Characteristic | Binomial Generalization. The multinomial distribution is a generalization of the binomial distribution where more than two states of the system are allowed. The binomial distribution is a special case where $d=2$. <br> Covariance. All covariance's are negative. This is because the increase in one parameter $p_{i}$ must result in the decrease of $p_{j}$ to satisfy $\Sigma p_{i}=1$. <br> With Replacement. The multinomial distribution assumes replacement. The equivalent distribution which assumes without replacement is the multivariate hypergeometric distribution. <br> Convolution Property <br> Let <br> Then $\quad \boldsymbol{K}_{\boldsymbol{t}} \sim M N o m_{d}\left(\boldsymbol{k} ; n_{t}, \mathbf{p}\right)$ <br> This does not hold when the $\mathbf{p}$ parameter differs. |  |  |  |  || Applications | Partial Failures. When the states of a system under demands cannot be modeled with two states (success or failure) the multinomial distribution may be used. Examples of this include when modeling discrete states of component degradation. |
| :--: | :--: |
| Resources | Online: <br> http://en.wikipedia.org/wiki/Multinomial_distribution <br> http://mathworld.wolfram.com/MultinomialDistribution.html <br> http://www.math.uah.edu/stat/bernoulli/Multinomial.xhtml <br> Books: <br> Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1997. Discrete Multivariate Distributions 1st ed., Wiley-Interscience. |
| Relationship to Other Distributions |  |
| Binominal Distribution <br> $\operatorname{Binom}(k \mid n, p)$ | Special Case: $\quad M N o m_{d=2}(\mathbf{k} \mid n, \mathbf{p})=\operatorname{Binom}(k \mid n, p)$ |# 7. References 

Abadir, K. \& Magdalinos, T., 2002. The Characteristic Function from a Family of Truncated Normal Distributions. Econometric Theory, 18(5), p.1276-1287.

Agresti, A., 2002. Categorical data analysis, John Wiley and Sons.
Aitchison, J.J. \& Brown, J.A.C., 1957. The Lognormal Distribution, New York: Cambridge University Press.

Andersen, P.K. et al., 1996. Statistical Models Based on Counting Processes Corrected., Springer.

Angus, J.E., 1994. Bootstrap one-sided confidence intervals for the lognormal mean. Journal of the Royal Statistical Society. Series D (The Statistician), 43(3), p.395-401.

Anon, Six Sigma | Process Management | Strategic Process Management | Welcome to SSA \& Company.

Antle, C., Klimko, L. \& Harkness, W., 1970. Confidence Intervals for the Parameters of the Logistic Distribution. Biometrika, 57(2), p.397-402.

Aoshima, M. \& Govindarajulu, Z., 2002. Fixed-width confidence interval for a lognormal mean. International Journal of Mathematics and Mathematical Sciences, 29(3), p.143-153.

Arnold, B.C., 1983. Pareto distributions, Fairland, MD: International Co-operative Pub. House.

Artin, E., 1964. The Gamma Function, New York: Holt, Rinehart \& Winston.

Balakrishnan, 1991. Handbook of the Logistic Distribution 1st ed., CRC.
Balakrishnan, N. \& Basu, A.P., 1996. Exponential Distribution: Theory, Methods and Applications 1st ed., CRC.Balakrishnan, N. \& Lai, C.-D., 2009. Continuous Bivariate Distributions 2nd ed., Springer.

Balakrishnan, N. \& Rao, C.R., 2001. Handbook of Statistics 20: Advances in Reliability 1st ed., Elsevier Science \& Technology.

Berger, J.O., 1993. Statistical Decision Theory and Bayesian Analysis 2nd ed., Springer.

Berger, J.O. \& Bernardo, J.M., 1992. Ordered Group Reference Priors with Application to the Multinomial Problem. Biometrika, 79(1), p.25-37.

Berger, J.O. \& Sellke, T., 1987. Testing a Point Null Hypothesis: The Irreconcilability of P Values and Evidence. Journal of the American Statistical Association, 82(397), p.112-122.

Berger, J.O. \& Sun, D., 2008. Objective priors for the bivariate normal model. The Annals of Statistics, 36(2), p.963-982.

Bernardo, J.M. et al., 1992. On the development of reference priors. Bayesian statistics, 4, p.35-60.

Berry, D.A., Chaloner, K.M. \& Geweke, J.K., 1995. Bayesian Analysis in Statistics and Econometrics: Essays in Honor of Arnold Zellner 1st ed., Wiley-Interscience.

Bertsekas, D.P. \& Tsitsiklis, J.N., 2008. Introduction to Probability 2nd ed., Athena Scientific.

Billingsley, P., 1995. Probability and Measure, 3rd Edition 3rd ed., Wiley-Interscience.

Birnbaum, Z.W. \& Saunders, S.C., 1969. A New Family of Life Distributions. Journal of Applied Probability, 6(2), p.319-327.

Björck, A., 1996. Numerical Methods for Least Squares Problems 1st ed., SIAM: Society for Industrial and Applied Mathematics.Bowman, K.O. \& Shenton, L.R., 1988. Properties of estimators for the gamma distribution, CRC Press.

Brown, L.D., Cai, T.T. \& DasGupta, A., 2001. Interval estimation for a binomial proportion. Statistical Science, p.101-117.

Christensen, R. \& Huffman, M.D., 1985. Bayesian Point Estimation Using the Predictive Distribution. The American Statistician, 39(4), p.319-321.

Cohen, 1991. Truncated and Censored Samples 1st ed., CRC Press.
Collani, E.V. \& Dräger, K., 2001. Binomial distribution handbook for scientists and engineers, Birkhäuser.

Congdon, P., 2007. Bayesian Statistical Modelling 2nd ed., Wiley.
Cozman, F. \& Krotkov, E., 1997. Truncated Gaussians as Tolerance Sets.

Crow, E.L. \& Shimizu, K., 1988. Lognormal distributions, CRC Press.
Dekking, F.M. et al., 2007. A Modern Introduction to Probability and Statistics: Understanding Why and How, Springer.

Fink, D., 1997. A compendium of conjugate priors. See http://www. people. cornell. edu/pages/df36/CONJINTRnew\% 20TEX. pdf, p. 46 .

Georges, P. et al., 2001. Multivariate Survival Modelling: A Unified Approach with Copulas. SSRN eLibrary.

Gupta and Nadarajah, 2004. Handbook of beta distribution and its applications, CRC Press.

Gupta, P.L., Gupta, R.C. \& Tripathi, R.C., 1997. On the monotonic properties of discrete failure rates. Journal of Statistical Planning and Inference, 65(2), p.255-268.Haight, F.A., 1967. Handbook of the Poisson distribution, New York,: Wiley.

Hastings, N.A.J., Peacock, B. \& Evans, M., 2000. Statistical Distributions, 3rd Edition 3rd ed., John Wiley \& Sons Inc.

Jiang, R. \& Murthy, D.N.P., 1996. A mixture model involving three Weibull distributions. In Proceedings of the Second AustraliaJapan Workshop on Stochastic Models in Engineering, Technology and Management. Gold Coast, Australia, pp. 260270 .

Jiang, R. \& Murthy, D.N.P., 1998. Mixture of Weibull distributions parametric characterization of failure rate function. Applied Stochastic Models and Data Analysis, (14), p.47-65.

Jiang, R. \& Murthy, D.N.P., 1995. Modeling Failure-Data by Mixture of2 Weibull Distributions : A Graphical Approach. IEEE Transactions on Reliability, 44, p.477-488.

Jiang, R. \& Murthy, D.N.P., 1999. The exponentiated Weibull family: a graphical approach. Reliability, IEEE Transactions on, 48(1), p.68-72.

Johnson, N.L., Kemp, A.W. \& Kotz, S., 2005. Univariate Discrete Distributions 3rd ed., Wiley-Interscience.

Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1994. Continuous Univariate Distributions, Vol. 1 2nd ed., Wiley-Interscience.

Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1995. Continuous Univariate Distributions, Vol. 2 2nd ed., Wiley-Interscience.

Johnson, N.L., Kotz, S. \& Balakrishnan, N., 1997. Discrete Multivariate Distributions 1st ed., Wiley-Interscience.

Kimball, B.F., 1960. On the Choice of Plotting Positions on Probability Paper. Journal of the American Statistical Association, 55(291), p.546-560.Kleiber, C. \& Kotz, S., 2003. Statistical Size Distributions in Economics and Actuarial Sciences 1st ed., Wiley-Interscience.

Klein, J.P. \& Moeschberger, M.L., 2003. Survival analysis: techniques for censored and truncated data, Springer.

Kotz, S., Balakrishnan, N. \& Johnson, N.L., 2000. Continuous Multivariate Distributions, Volume 1, Models and Applications, 2nd Edition 2nd ed., Wiley-Interscience.

Kotz, S. \& Dorp, J.R. van, 2004. Beyond Beta: Other Continuous Families Of Distributions With Bounded Support And Applications, World Scientific Publishing Company.

Kundu, D., Kannan, N. \& Balakrishnan, N., 2008. On the hazard function of Birnbaum-Saunders distribution and associated inference. Comput. Stat. Data Anal., 52(5), p.2692-2702.

Lai, C.D., Xie, M. \& Murthy, D.N.P., 2003. A modified Weibull distribution. IEEE Transactions on Reliability, 52(1), p.33-37.

Lai, C.-D. \& Xie, M., 2006. Stochastic Ageing and Dependence for Reliability 1st ed., Springer.

Lawless, J.F., 2002. Statistical Models and Methods for Lifetime Data 2nd ed., Wiley-Interscience.

Leemis, L.M. \& McQueston, J.T., 2008. Univariate distribution relationships. The American Statistician, 62(1), p.45-53.

Leipnik, R.B., 1991. On Lognormal Random Variables: I-the Characteristic Function. The ANZIAM Journal, 32(03), p.327347 .

Lemonte, A.J., Cribari-Neto, F. \& Vasconcellos, K.L.P., 2007. Improved statistical inference for the two-parameter Birnbaum-Saunders distribution. Computational Statistics \& Data Analysis, 51(9), p.4656-4681.Limpert, E., Stahel, W. \& Abbt, M., 2001. Log-normal Distributions across the Sciences: Keys and Clues. BioScience, 51(5), p.352, 341 .

MacKay, D.J.C. \& Petoy, L.C.B., 1995. A hierarchical Dirichlet language model. Natural language engineering.

Manzini, R. et al., 2009. Maintenance for Industrial Systems 1st ed., Springer.

Martz, H.F. \& Waller, R., 1982. Bayesian reliability analysis, JOHN WILEY \& SONS, INC, 605 THIRD AVE, NEW YORK, NY 10158 .

Meeker, W.Q. \& Escobar, L.A., 1998. Statistical Methods for Reliability Data 1st ed., Wiley-Interscience.

Modarres, M., Kaminskiy, M. \& Krivtsov, V., 1999. Reliability engineering and risk analysis, CRC Press.

Murthy, D.N.P., Xie, M. \& Jiang, R., 2003. Weibull Models 1st ed., Wiley-Interscience.

Nelson, W.B., 1990. Accelerated Testing: Statistical Models, Test Plans, and Data Analysis, Wiley-Interscience.

Nelson, W.B., 1982. Applied Life Data Analysis, Wiley-Interscience.
Novosyolov, A., 2006. The sum of dependent normal variables may be not normal. http://risktheory.ru/papers/sumOfDep.pdf.

Patel, J.K. \& Read, C.B., 1996. Handbook of the Normal Distribution 2nd ed., CRC.

Pham, H., 2006. Springer Handbook of Engineering Statistics 1st ed., Springer.

Provan, J.W., 1987. Probabilistic approaches to the material-related reliability of fracture-sensitive structures. Probabilistic fracturemechanics and reliability(A 87-35286 15-38). Dordrecht, Martinus Nijhoff Publishers, 1987,, p.1-45.

Rao, C.R. \& Toutenburg, H., 1999. Linear Models: Least Squares and Alternatives 2nd ed., Springer.

Rausand, M. \& Høyland, A., 2004. System reliability theory, WileyIEEE.

Rencher, A.C., 1997. Multivariate Statistical Inference and Applications, Volume 2, Methods of Multivariate Analysis Har/Dis., WileyInterscience.

Rinne, H., 2008. The Weibull Distribution: A Handbook 1st ed., Chapman \& Hall/CRC.

Schneider, H., 1986. Truncated and censored samples from normal populations, M. Dekker.

Simon, M.K., 2006. Probability Distributions Involving Gaussian Random Variables: A Handbook for Engineers and Scientists, Springer.

Singpurwalla, N.D., 2006. Reliability and Risk: A Bayesian Perspective 1st ed., Wiley.

Sison, C.P. \& Glaz, J., 1995. Simultaneous Confidence Intervals and Sample Size Determination for Multinomial Proportions. Journal of the American Statistical Association, 90(429).

Tong, Y.L., 1990. The Multivariate Normal Distribution, Springer.
Xie, M., Gaudoin, O. \& Bracquemond, C., 2002. Redefining Failure Rate Function for Discrete Distributions. International Journal of Reliability, Quality \& Safety Engineering, 9(3), p. 275.

Xie, M., Goh, T.N. \& Tang, Y., 2004. On changing points of mean residual life and failure rate function for some generalized Weibull distributions. Reliability Engineering and System Safety, 84(3), p.293-299.Xie, M., Tang, Y. \& Goh, T.N., 2002. A modified Weibull extension with bathtub-shaped failure rate function. Reliability Engineering and System Safety, 76(3), p.279-285.

Yang and Berger, 1998. A Catalog of Noninformative Priors (DRAFT).
Yang, K. et al., 2004. Multivariate Statistical Methods in Quality Management 1st ed., McGraw-Hill Professional.

Yang, R. \& Berger, J.O., 1994. Estimation of a Covariance Matrix Using the Reference Prior. The Annals of Statistics, 22(3), p.1195-1211.

Zhou, X.H. \& Gao, S., 1997. Confidence intervals for the log-normal mean. Statistics in medicine, 16(7), p.783-790.