# Problem Set

*30 problems*

## Table of Contents

1. [A software development team is tracking defects in two...](#a-software-development-team-is-tracking-defects-in-two)
2. [A manufacturer is conducting accelerated life testing on a...](#a-manufacturer-is-conducting-accelerated-life-testing-on-a)
3. [A radar system consists of a critical power amplifier...](#a-radar-system-consists-of-a-critical-power-amplifier)
4. [A parallel redundant system consists of 3 independent...](#a-parallel-redundant-system-consists-of-3-independent)
5. [A data center has 5 independent cooling units arranged in a...](#a-data-center-has-5-independent-cooling-units-arranged-in-a)
6. [A quality control inspector is examining a batch of...](#a-quality-control-inspector-is-examining-a-batch-of)
7. [A critical aerospace component follows a Weibull...](#a-critical-aerospace-component-follows-a-weibull)
8. [A parallel redundant system consists of 3 independent...](#a-parallel-redundant-system-consists-of-3-independent)
9. [Derive the hazard rate function h(t) for a system whose...](#derive-the-hazard-rate-function-ht-for-a-system-whose)
10. [A system has a linearly increasing hazard rate given by...](#a-system-has-a-linearly-increasing-hazard-rate-given-by)
11. [A manufacturer monitors the defect rate in production...](#a-manufacturer-monitors-the-defect-rate-in-production)
12. [A reliability engineer is comparing two suppliers for a...](#a-reliability-engineer-is-comparing-two-suppliers-for-a)
13. [A semiconductor device has a lifetime that follows a...](#a-semiconductor-device-has-a-lifetime-that-follows-a)
14. [A reliability test is conducted on 8 identical components...](#a-reliability-test-is-conducted-on-8-identical-components)
15. [A manufacturer conducts a reliability study on electronic...](#a-manufacturer-conducts-a-reliability-study-on-electronic)
16. [A power supply unit has a constant failure rate of λ =...](#a-power-supply-unit-has-a-constant-failure-rate-of)
17. [A manufacturer conducts an accelerated life test on 300 LED...](#a-manufacturer-conducts-an-accelerated-life-test-on-300-led)
18. [A quality control inspector has a box containing 20...](#a-quality-control-inspector-has-a-box-containing-20)
19. [A reliability engineer is testing power supply units that...](#a-reliability-engineer-is-testing-power-supply-units-that)
20. [A communication system component has a reliability function...](#a-communication-system-component-has-a-reliability-function)
21. [A quality control system uses two independent inspection...](#a-quality-control-system-uses-two-independent-inspection)
22. [Electronic control units in automotive applications are...](#electronic-control-units-in-automotive-applications-are)
23. [A data center has backup generators that activate...](#a-data-center-has-backup-generators-that-activate)
24. [A manufacturing system consists of 5 independent subsystems...](#a-manufacturing-system-consists-of-5-independent-subsystems)
25. [A reliability test is conducted on 50 identical electronic...](#a-reliability-test-is-conducted-on-50-identical-electronic)
26. [A semiconductor device has a lognormal failure distribution...](#a-semiconductor-device-has-a-lognormal-failure-distribution)
27. [A sensor system processes incoming signals where the output...](#a-sensor-system-processes-incoming-signals-where-the-output)
28. [A component follows a lognormal distribution for its...](#a-component-follows-a-lognormal-distribution-for-its)
29. [A reliability test plan requires testing n units to failure...](#a-reliability-test-plan-requires-testing-n-units-to-failure)
30. [A satellite system consists of 3 redundant power modules...](#a-satellite-system-consists-of-3-redundant-power-modules)

---

## 1. A software development team is tracking defects in two...

### Question

A software development team is tracking defects in two different modules of their application. Module A has 50,000 lines of code and Module B has 75,000 lines of code. After deployment, Module A experiences 18 defects in the first month, while Module B experiences 35 defects in the same period. Assume defects follow a Poisson distribution.

(a) Estimate the defect density (defects per KLOC) for each module.
(b) Construct 90% confidence intervals for the true defect density of each module.
(c) Using the Likelihood Ratio Test at α = 0.05, determine whether there is sufficient evidence to conclude that the two modules have different defect densities.

### Reasoning

###### Problem Setup

**Given Information:**
- Module A: 50,000 LOC = 50 KLOC, 18 defects observed
- Module B: 75,000 LOC = 75 KLOC, 35 defects observed
- Distribution: Poisson
- Time period: 1 month (same for both)

---

##### Part (a): Point Estimates of Defect Density

For Poisson distribution, the MLE of the rate parameter is:
$$\hat{\lambda} = \frac{\text{observed defects}}{\text{exposure (KLOC)}}$$

###### Module A:
$$\hat{\lambda}_A = \frac{18}{50} = 0.36 \text{ defects/KLOC}$$

###### Module B:
$$\hat{\lambda}_B = \frac{35}{75} = 0.4667 \text{ defects/KLOC}$$

###### Answer (a):
**Module A: λ̂ₐ = 0.36 defects/KLOC**
**Module B: λ̂ᵦ = 0.467 defects/KLOC**

---

##### Part (b): 90% Confidence Intervals

###### Formula for Poisson Rate CI

For observed count X and exposure n (in KLOC):
$$\left[ \frac{\chi^2_{2X, \alpha/2}}{2n}, \frac{\chi^2_{2X+2, 1-\alpha/2}}{2n} \right]$$

Where α = 0.10 for 90% CI, so α/2 = 0.05

###### Module A (X = 18, n = 50):

**Chi-square values needed:**
- $\chi^2_{36, 0.05} = 23.269$
- $\chi^2_{38, 0.95} = 53.384$

**Lower Limit:**
$$L_A = \frac{23.269}{2(50)} = \frac{23.269}{100} = 0.233$$

**Upper Limit:**
$$U_A = \frac{53.384}{2(50)} = \frac{53.384}{100} = 0.534$$

**90% CI for Module A: (0.233, 0.534) defects/KLOC**

###### Module B (X = 35, n = 75):

**Chi-square values needed:**
- $\chi^2_{70, 0.05} = 51.739$
- $\chi^2_{72, 0.95} = 90.531$

**Lower Limit:**
$$L_B = \frac{51.739}{2(75)} = \frac{51.739}{150} = 0.345$$

**Upper Limit:**
$$U_B = \frac{90.531}{2(75)} = \frac{90.531}{150} = 0.604$$

**90% CI for Module B: (0.345, 0.604) defects/KLOC**

###### Answer (b):
**Module A: (0.233, 0.534) defects/KLOC**
**Module B: (0.345, 0.604) defects/KLOC**

---

##### Part (c): Likelihood Ratio Test

###### Hypotheses:
- H₀: λₐ = λᵦ = λ (equal defect densities)
- H₁: λₐ ≠ λᵦ (different defect densities)

###### Step 1: Calculate MLEs

**Under H₁ (separate estimates):**
- Already calculated: $\hat{\lambda}_A = 0.36$, $\hat{\lambda}_B = 0.4667$

**Under H₀ (pooled estimate):**
$$\hat{\lambda}_0 = \frac{X_A + X_B}{n_A + n_B} = \frac{18 + 35}{50 + 75} = \frac{53}{125} = 0.424$$

###### Step 2: Calculate Log-Likelihoods

For Poisson distribution with rate λ and exposure n, observing X events:
$$\ln L = X \ln(\lambda n) - \lambda n - \ln(X!)$$

Since we're comparing likelihoods, the factorial terms cancel.

**Under H₁:**
$$\ln L_1 = X_A \ln(\hat{\lambda}_A n_A) - \hat{\lambda}_A n_A + X_B \ln(\hat{\lambda}_B n_B) - \hat{\lambda}_B n_B$$

Note that $\hat{\lambda}_A n_A = X_A = 18$ and $\hat{\lambda}_B n_B = X_B = 35$:
$$\ln L_1 = 18 \ln(18) - 18 + 35 \ln(35) - 35$$
$$= 18(2.8904) - 18 + 35(3.5553) - 35$$
$$= 52.027 - 18 + 124.436 - 35$$
$$= 123.463$$

**Under H₀:**
$$\ln L_0 = X_A \ln(\hat{\lambda}_0 n_A) - \hat{\lambda}_0 n_A + X_B \ln(\hat{\lambda}_0 n_B) - \hat{\lambda}_0 n_B$$

Calculate:
- $\hat{\lambda}_0 n_A = 0.424(50) = 21.2$
- $\hat{\lambda}_0 n_B = 0.424(75) = 31.8$

$$\ln L_0 = 18 \ln(21.2) - 21.2 + 35 \ln(31.8) - 31.8$$
$$= 18(3.0540) - 21.2 + 35(3.4595) - 31.8$$
$$= 54.972 - 21.2 + 121.083 - 31.8$$
$$= 123.055$$

###### Step 3: Calculate LRT Statistic

$$-2 \ln \Lambda = 2(\ln L_1 - \ln L_0) = 2(123.463 - 123.055) = 2(0.408) = 0.816$$

###### Step 4: Determine Critical Value

Under H₀, the test statistic follows χ² distribution with df = 1

**Critical value at α = 0.05:**
$$\chi^2_{0.05, 1} = 3.841$$

**P-value:**
$$P(\chi^2_1 > 0.816) \approx 0.366$$

###### Step 5: Conclusion

**Test Statistic:** -2 ln Λ = 0.816
**Critical Value:** χ²₀.₀₅,₁ = 3.841

Since 0.816 < 3.841, we **fail to reject H₀**.

###### Answer (c):
**At α = 0.05, there is insufficient evidence to conclude that the two modules have different defect densities. The LRT statistic is 0.816 (p-value ≈ 0.366), which does not exceed the critical value of 3.841.**

---

##### Summary of Final Answers

| Part | Module A | Module B |
|------|----------|----------|
| **(a)** Defect Density | 0.36 defects/KLOC | 0.467 defects/KLOC |
| **(b)** 90% CI | (0.233, 0.534) | (0.345, 0.604) |

**(c)** The modules do not have significantly different defect densities (LRT = 0.816, p = 0.366)

### Answer

**(a) Module A: 0.36 defects/KLOC, Module B: 0.467 defects/KLOC
(b) Module A: (0.233, 0.534), Module B: (0.345, 0.604)
(c) Fail to reject H₀; no significant difference (LRT = 0.816, p-value = 0.366)**

---

## 2. A manufacturer is conducting accelerated life testing on a...

### Question

A manufacturer is conducting accelerated life testing on a new power supply design. They test 80 units at an elevated stress level for 500 hours. Assuming exponentially distributed failure times, failures are observed at the following times (in hours): 45, 112, 156, 203, 267, 318, 395, and 441. 

(a) Calculate the maximum likelihood estimate of the MTTF at this stress level.
(b) Construct a 95% two-sided confidence interval for the true MTTF.
(c) If the company wants to demonstrate an MTTF of at least 5,000 hours with 80% confidence using a 500-hour test with zero failures allowed, how many units would need to be tested?

### Reasoning

###### Problem Setup

**Given Information:**
- n = 80 units tested
- Test duration: T = 500 hours
- Number of failures: r = 8
- Failure times: 45, 112, 156, 203, 267, 318, 395, 441 hours
- Assumption: Exponential distribution

---

##### Part (a): MLE of MTTF

###### Step 1: Calculate Total Time on Test (TTT)

For Type I censoring with exponential distribution:
$$TTT = \sum_{i=1}^{r} t_i + (n-r) \cdot T$$

**Sum of failure times:**
$$\sum t_i = 45 + 112 + 156 + 203 + 267 + 318 + 395 + 441 = 1,937 \text{ hours}$$

**Number of survivors:**
$$n - r = 80 - 8 = 72 \text{ units}$$

**Total Time on Test:**
$$TTT = 1,937 + (72)(500) = 1,937 + 36,000 = 37,937 \text{ hours}$$

###### Step 2: Calculate MLE

For exponential distribution, the MLE of MTTF is:
$$\hat{\theta} = \frac{TTT}{r} = \frac{37,937}{8} = 4,742.125 \text{ hours}$$

###### Answer (a):
**The MLE of MTTF is θ̂ = 4,742.1 hours**

---

##### Part (b): 95% Confidence Interval for MTTF

###### Theoretical Background

For exponential distribution with r failures and total time on test TTT, the confidence interval for MTTF θ is based on the chi-square distribution:

$$\left[ \frac{2 \cdot TTT}{\chi^2_{2r, \alpha/2}}, \frac{2 \cdot TTT}{\chi^2_{2r, 1-\alpha/2}} \right]$$

Where:
- α = 0.05 (for 95% CI)
- Degrees of freedom: 2r = 2(8) = 16

###### Step 1: Find Chi-Square Values

From chi-square tables:
- $\chi^2_{16, 0.025} = 6.908$ (lower tail)
- $\chi^2_{16, 0.975} = 28.845$ (upper tail)

###### Step 2: Calculate Confidence Limits

**Lower Limit:**
$$L = \frac{2 \cdot TTT}{\chi^2_{16, 0.975}} = \frac{2(37,937)}{28.845} = \frac{75,874}{28.845} = 2,630.5 \text{ hours}$$

**Upper Limit:**
$$U = \frac{2 \cdot TTT}{\chi^2_{16, 0.025}} = \frac{2(37,937)}{6.908} = \frac{75,874}{6.908} = 10,983.0 \text{ hours}$$

###### Answer (b):
**The 95% confidence interval for MTTF is (2,630.5, 10,983.0) hours**

---

##### Part (c): Sample Size for Reliability Demonstration

###### Given Requirements:
- Target MTTF: θ₀ = 5,000 hours
- Confidence level: 1 - α = 0.80, so α = 0.20
- Test duration: t = 500 hours
- Allowed failures: r = 0

###### Formula

$$n = \frac{\chi^2_{1-\alpha, 2(r+1)}}{2 \cdot t \cdot \lambda_0}$$

Where λ₀ = 1/θ₀ = 1/5,000 = 0.0002 failures/hour

###### Step 1: Find Chi-Square Value

For r = 0:
- Degrees of freedom: 2(r + 1) = 2(1) = 2
- $\chi^2_{0.20, 2} = 3.219$

###### Step 2: Calculate Sample Size

$$n = \frac{\chi^2_{0.20, 2}}{2 \cdot t \cdot \lambda_0} = \frac{3.219}{2(500)(0.0002)} = \frac{3.219}{0.2} = 16.095$$

**Round up: n = 17 units**

###### Answer (c):
**17 units must be tested to demonstrate MTTF ≥ 5,000 hours with 80% confidence**

---

##### Summary of Final Answers

| Part | Answer |
|------|--------|
| **(a)** MLE of MTTF | **4,742.1 hours** |
| **(b)** 95% CI for MTTF | **(2,630.5, 10,983.0) hours** |
| **(c)** Required sample size | **17 units** |

### Answer

**(a) 4,742.1 hours, (b) (2,630.5, 10,983.0) hours, (c) 17 units**

---

## 3. A radar system consists of a critical power amplifier...

### Question

A radar system consists of a critical power amplifier component that fails according to a Weibull distribution with shape parameter β = 1.5 and characteristic life η = 8,000 hours. The system operates continuously and failed components are immediately replaced (renewal process). For a 12,000-hour mission, how many spare amplifiers should be stocked to ensure that the probability of running out of spares is less than 10%?

### Reasoning

#### Spare Parts Calculation for Weibull Renewal Process

##### Problem Understanding

I need to determine the number of spare power amplifiers required for a 12,000-hour mission where:
- Component failures follow a Weibull distribution
- Shape parameter β = 1.5
- Characteristic life η = 8,000 hours
- Required probability of shortage < 10% (i.e., probability of having enough spares ≥ 90%)

##### Step 1: Calculate the Mean Time to Failure (MTTF)

For a Weibull distribution, the MTTF is:
$$MTTF = \eta \cdot \Gamma\left(1 + \frac{1}{\beta}\right)$$

where Γ is the gamma function.

For β = 1.5:
$$MTTF = 8,000 \cdot \Gamma\left(1 + \frac{1}{1.5}\right) = 8,000 \cdot \Gamma(1.667)$$

$$\Gamma(1.667) \approx 0.9027$$

$$MTTF = 8,000 \times 0.9027 = 7,221.6 \text{ hours}$$

##### Step 2: Calculate Expected Number of Failures

For a renewal process over time T = 12,000 hours, we can approximate the expected number of renewals using:
$$\mu = \frac{T}{MTTF} = \frac{12,000}{7,221.6} = 1.661$$

For renewal processes, when the number of renewals is not too large, we can approximate the distribution of the number of failures as Poisson with parameter μ = 1.661.

##### Step 3: Apply Poisson Distribution

The number of failures N(T) approximately follows a Poisson distribution with mean μ = 1.661.

The probability of exactly k failures is:
$$P(N = k) = \frac{\mu^k e^{-\mu}}{k!} = \frac{(1.661)^k e^{-1.661}}{k!}$$

First, calculate: $e^{-1.661} = 0.1899$

##### Step 4: Determine Required Number of Spares

We need to find the minimum number of spares **n** such that:
$$P(N \leq n) \geq 0.90$$

**For n = 0:**
$$P(N = 0) = e^{-1.661} = 0.1899$$
$$P(N \leq 0) = 0.1899 < 0.90$$ ❌

**For n = 1:**
$$P(N = 1) = \frac{1.661 \times 0.1899}{1} = 0.3154$$
$$P(N \leq 1) = 0.1899 + 0.3154 = 0.5053 < 0.90$$ ❌

**For n = 2:**
$$P(N = 2) = \frac{(1.661)^2 \times 0.1899}{2} = \frac{2.759 \times 0.1899}{2} = 0.2620$$
$$P(N \leq 2) = 0.5053 + 0.2620 = 0.7673 < 0.90$$ ❌

**For n = 3:**
$$P(N = 3) = \frac{(1.661)^3 \times 0.1899}{6} = \frac{4.583 \times 0.1899}{6} = 0.1451$$
$$P(N \leq 3) = 0.7673 + 0.1451 = 0.9124 \geq 0.90$$ ✓

**For n = 4 (verification):**
$$P(N = 4) = \frac{(1.661)^4 \times 0.1899}{24} = \frac{7.613 \times 0.1899}{24} = 0.0602$$
$$P(N \leq 4) = 0.9124 + 0.0602 = 0.9726$$

##### Step 5: Verification

Since P(N ≤ 3) = 0.9124 > 0.90, having 3 spares is sufficient.

The probability of shortage = 1 - 0.9124 = 0.0876 = 8.76% < 10% ✓

---

##### **Final Answer**

$$\boxed{n = 3 \text{ spare amplifiers}}$$

Three spare amplifiers should be stocked to ensure that the probability of running out of spares is less than 10% (actual probability of shortage = 8.76%).

### Answer

**3 spare amplifiers.**

---

## 4. A parallel redundant system consists of 3 independent...

### Question

A parallel redundant system consists of 3 independent components, each with a Weibull-distributed lifetime with shape parameter β = 2 and characteristic life η = 500 hours. For a parallel system, the system fails only when all components have failed. Calculate:
1. The reliability of the system at t = 300 hours
2. The probability that the system fails before t = 400 hours

### Reasoning

#### Solution: Parallel System with Weibull Components

##### Problem Setup

We have a parallel system with 3 independent components, each following a Weibull distribution with:
- **Shape parameter β = 2**
- **Characteristic life η = 500 hours**

For a parallel system, **at least one component must survive** for the system to survive.

---

##### Step 1: Weibull Distribution Reliability Function

For a Weibull distribution, the reliability function is:

$$R(t) = e^{-\left(\frac{t}{\eta}\right)^\beta}$$

For each component with β = 2 and η = 500:

$$R_{\text{component}}(t) = e^{-\left(\frac{t}{500}\right)^2}$$

---

##### Step 2: Reliability of a Single Component at t = 300 hours

$$R_{\text{component}}(300) = e^{-\left(\frac{300}{500}\right)^2} = e^{-(0.6)^2} = e^{-0.36}$$

$$R_{\text{component}}(300) = 0.6977$$

---

##### Step 3: System Reliability for Parallel Configuration

For a parallel system, the system fails only when **all components fail**. Therefore:

$$F_{\text{system}}(t) = \prod_{i=1}^{n} F_i(t)$$

where F(t) = 1 - R(t) is the failure probability.

The system reliability is:

$$R_{\text{system}}(t) = 1 - \prod_{i=1}^{n} [1 - R_i(t)]$$

For 3 identical components:

$$R_{\text{system}}(t) = 1 - [1 - R_{\text{component}}(t)]^3$$

---

##### Step 4: System Reliability at t = 300 hours

$$R_{\text{system}}(300) = 1 - [1 - 0.6977]^3$$

$$R_{\text{system}}(300) = 1 - [0.3023]^3$$

$$R_{\text{system}}(300) = 1 - 0.02758$$

$$\boxed{R_{\text{system}}(300) = 0.9724 \text{ or } 97.24\%}$$

---

##### Step 5: Component Reliability at t = 400 hours

$$R_{\text{component}}(400) = e^{-\left(\frac{400}{500}\right)^2} = e^{-(0.8)^2} = e^{-0.64}$$

$$R_{\text{component}}(400) = 0.5273$$

---

##### Step 6: System Reliability at t = 400 hours

$$R_{\text{system}}(400) = 1 - [1 - 0.5273]^3$$

$$R_{\text{system}}(400) = 1 - [0.4727]^3$$

$$R_{\text{system}}(400) = 1 - 0.1056$$

$$R_{\text{system}}(400) = 0.8944$$

---

##### Step 7: Probability of System Failure Before t = 400 hours

$$F_{\text{system}}(400) = 1 - R_{\text{system}}(400)$$

$$F_{\text{system}}(400) = 1 - 0.8944$$

$$\boxed{F_{\text{system}}(400) = 0.1056 \text{ or } 10.56\%}$$

---

##### Final Answers

| Question | Answer |
|----------|--------|
| **System reliability at t = 300 hours** | **0.9724 (97.24%)** |
| **Probability of system failure before t = 400 hours** | **0.1056 (10.56%)** |

---

### Answer

**1. System reliability at 300 hours: 0.972
2. Probability of failure before 400 hours: 0.106**

---

## 5. A data center has 5 independent cooling units arranged in a...

### Question

A data center has 5 independent cooling units arranged in a k-out-of-n configuration where at least 3 units must be operational for the system to function (3-out-of-5 system). Each cooling unit has a constant failure rate and follows an exponential distribution with MTTF = 2000 hours. What is the reliability of the cooling system at t = 500 hours? (Note: For a k-out-of-n system, the system survives if at least k out of n components survive.)

### Reasoning

#### Solution: k-out-of-n System Reliability

##### Problem Setup

We have a **3-out-of-5 system** (k = 3, n = 5) where:
- The system functions if **at least 3 out of 5** cooling units are operational
- Each unit has exponential lifetime with **MTTF = 2000 hours**
- Components are independent
- We need reliability at **t = 500 hours**

---

##### Step 1: Individual Component Reliability

For an exponential distribution:

$$\lambda = \frac{1}{\text{MTTF}} = \frac{1}{2000} \text{ per hour}$$

The reliability function for each component:

$$R_{\text{component}}(t) = e^{-\lambda t} = e^{-t/2000}$$

At t = 500 hours:

$$R(500) = e^{-500/2000} = e^{-0.25} = 0.7788$$

The failure probability for each component:

$$F(500) = 1 - R(500) = 1 - 0.7788 = 0.2212$$

---

##### Step 2: k-out-of-n System Reliability Formula

For a k-out-of-n system with identical independent components, the system reliability is given by the **binomial distribution**:

$$R_{\text{system}}(t) = \sum_{i=k}^{n} \binom{n}{i} [R(t)]^i [1-R(t)]^{n-i}$$

This represents the probability that **at least k components survive**.

For our 3-out-of-5 system:

$$R_{\text{system}}(500) = \sum_{i=3}^{5} \binom{5}{i} [R(500)]^i [F(500)]^{5-i}$$

---

##### Step 3: Calculate Each Term

Let p = R(500) = 0.7788 and q = F(500) = 0.2212

**Exactly 3 components survive:**

$$\binom{5}{3} p^3 q^2 = 10 \times (0.7788)^3 \times (0.2212)^2$$

$$= 10 \times 0.4720 \times 0.0489 = 0.2308$$

**Exactly 4 components survive:**

$$\binom{5}{4} p^4 q^1 = 5 \times (0.7788)^4 \times (0.2212)^1$$

$$= 5 \times 0.3676 \times 0.2212 = 0.4066$$

**All 5 components survive:**

$$\binom{5}{5} p^5 q^0 = 1 \times (0.7788)^5 \times 1$$

$$= 0.2862$$

---

##### Step 4: Sum All Probabilities

$$R_{\text{system}}(500) = 0.2308 + 0.4066 + 0.2862$$

$$\boxed{R_{\text{system}}(500) = 0.9236 \text{ or } 92.36\%}$$

---

##### Step 5: Verification

Total probability check:
- P(0 survive) + P(1 survive) + P(2 survive) + P(3 survive) + P(4 survive) + P(5 survive) = 1 ✓

System fails when 0, 1, or 2 components survive:

$$F_{\text{system}}(500) = 1 - 0.9236 = 0.0764 \text{ or } 7.64\%$$

---

##### Final Answer

**System reliability at t = 500 hours: 0.9236 (92.36%)**

This demonstrates that the 3-out-of-5 redundant configuration provides significantly higher reliability (92.36%) compared to what a single component would provide (77.88%) or what a series system of 5 components would provide (≈26%).

---

### Answer

**0.924 (or 92.4%)**

---

## 6. A quality control inspector is examining a batch of...

### Question

A quality control inspector is examining a batch of electronic components. The batch contains 15 components: 9 are from Supplier A and 6 are from Supplier B. Historical data shows that components from Supplier A have a 5% defect rate, while components from Supplier B have a 10% defect rate. The inspector randomly selects one component and tests it. 

(a) What is the probability that the selected component is defective?
(b) If the selected component is found to be defective, what is the probability it came from Supplier A?

### Reasoning

#### Quality Control Probability Problem

##### Given Information
- Total components: 15
- Supplier A components: 9
- Supplier B components: 6
- Defect rate for Supplier A: P(D|A) = 0.05
- Defect rate for Supplier B: P(D|B) = 0.10

##### Part (a): Probability of Selecting a Defective Component

We need to find P(D), the total probability of selecting a defective component.

###### Step 1: Find the probability of selecting from each supplier

$$P(A) = \frac{9}{15} = \frac{3}{5} = 0.60$$

$$P(B) = \frac{6}{15} = \frac{2}{5} = 0.40$$

###### Step 2: Apply the Law of Total Probability

$$P(D) = P(D|A) \cdot P(A) + P(D|B) \cdot P(B)$$

$$P(D) = (0.05)(0.60) + (0.10)(0.40)$$

$$P(D) = 0.030 + 0.040 = 0.070$$

$$\boxed{P(\text{Defective}) = 0.070 = 7.0\%}$$

##### Part (b): Probability Component Came from Supplier A Given It's Defective

We need to find P(A|D) using Bayes' Theorem.

###### Step 3: Apply Bayes' Theorem

$$P(A|D) = \frac{P(D|A) \cdot P(A)}{P(D)}$$

###### Step 4: Substitute values

$$P(A|D) = \frac{(0.05)(0.60)}{0.070}$$

$$P(A|D) = \frac{0.030}{0.070} = \frac{30}{70} = \frac{3}{7}$$

$$P(A|D) = 0.4286$$

$$\boxed{P(\text{Supplier A}|\text{Defective}) = \frac{3}{7} \approx 0.4286 = 42.86\%}$$

##### Verification

Let's verify using P(B|D):

$$P(B|D) = \frac{P(D|B) \cdot P(B)}{P(D)} = \frac{(0.10)(0.40)}{0.070} = \frac{0.040}{0.070} = \frac{4}{7} \approx 0.5714$$

Check: $P(A|D) + P(B|D) = \frac{3}{7} + \frac{4}{7} = 1$ ✓

##### Interpretation

Even though Supplier A has a lower defect rate (5% vs 10%), when we find a defective component, there's only a 42.86% chance it came from Supplier A. This is because:
- Supplier A contributes more components (60% of batch)
- But Supplier B has a higher defect rate
- The combination results in Supplier B being slightly more likely to be the source of a defective component (57.14% vs 42.86%)

---

##### Summary of Final Answers

| Question | Answer | Decimal | Percentage |
|----------|--------|---------|------------|
| (a) P(Defective) | 7/100 | 0.070 | 7.0% |
| (b) P(Supplier A\|Defective) | 3/7 | 0.4286 | 42.86% |

### Answer

**(a) 7.0% or 0.070
(b) 3/7 or approximately 42.86%**

---

## 7. A critical aerospace component follows a Weibull...

### Question

A critical aerospace component follows a Weibull distribution for its failure time. The characteristic life (scale parameter) η is 50,000 flight hours, and the shape parameter β is 2.5. 

(a) Calculate the reliability of the component at 10,000 flight hours.
(b) Find the hazard rate (instantaneous failure rate) at 10,000 flight hours.
(c) What does the shape parameter β = 2.5 tell us about the aging behavior of this component?

### Reasoning

#### Weibull Distribution Reliability Analysis

##### Given Information
- Characteristic life (scale parameter): η = 50,000 hours
- Shape parameter: β = 2.5
- Time of interest: t = 10,000 hours

##### Weibull Distribution Background

For a Weibull distribution:

**Reliability Function:**
$$R(t) = e^{-(t/\eta)^\beta}$$

**Cumulative Distribution Function:**
$$F(t) = 1 - e^{-(t/\eta)^\beta}$$

**Hazard Rate Function:**
$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

##### Part (a): Calculate Reliability at 10,000 Hours

###### Step 1: Apply the Weibull reliability formula

$$R(10,000) = e^{-(10,000/50,000)^{2.5}}$$

###### Step 2: Calculate the ratio

$$\frac{t}{\eta} = \frac{10,000}{50,000} = 0.2$$

###### Step 3: Raise to the power of β

$$(0.2)^{2.5} = (0.2)^{2.5}$$

Using logarithms:
$$\ln(0.2^{2.5}) = 2.5 \times \ln(0.2) = 2.5 \times (-1.6094) = -4.0236$$

$$(0.2)^{2.5} = e^{-4.0236} = 0.01789$$

###### Step 4: Calculate reliability

$$R(10,000) = e^{-0.01789} = 0.9823$$

$$\boxed{R(10,000) = 0.9823 = 98.23\%}$$

##### Part (b): Find the Hazard Rate at 10,000 Hours

###### Step 1: Apply the Weibull hazard rate formula

$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

###### Step 2: Substitute values

$$h(10,000) = \frac{2.5}{50,000}\left(\frac{10,000}{50,000}\right)^{2.5-1}$$

$$h(10,000) = \frac{2.5}{50,000}(0.2)^{1.5}$$

###### Step 3: Calculate (0.2)^1.5

$$(0.2)^{1.5} = (0.2)^{3/2} = \sqrt{(0.2)^3} = \sqrt{0.008} = 0.08944$$

###### Step 4: Complete the calculation

$$h(10,000) = \frac{2.5}{50,000} \times 0.08944$$

$$h(10,000) = 0.00005 \times 0.08944 = 4.472 \times 10^{-6} \text{ failures/hour}$$

Converting to failures per 1,000 hours:
$$h(10,000) = 4.472 \times 10^{-3} \text{ failures per 1,000 hours}$$

$$\boxed{h(10,000) = 4.47 \times 10^{-6} \text{ failures/hour} = 0.00447 \text{ failures per 1,000 hours}}$$

##### Part (c): Interpretation of Shape Parameter β = 2.5

###### Analysis of β Value

The shape parameter β determines the aging characteristic:

**Three regions:**
- β < 1: Decreasing failure rate (infant mortality)
- β = 1: Constant failure rate (random failures, exponential distribution)
- β > 1: Increasing failure rate (wear-out)

###### For β = 2.5:

Since **β = 2.5 > 1**, this indicates:

1. **Wear-out Region**: The component exhibits wear-out behavior with an increasing failure rate over time.

2. **Aging Effect**: Unlike the exponential distribution, this component DOES age. The longer it operates, the higher its instantaneous failure rate becomes.

3. **Rate of Increase**: The hazard function increases according to:
   $$h(t) \propto t^{1.5}$$
   
   This means the failure rate increases faster than linearly with time.

4. **Preventive Maintenance**: This aging behavior suggests that preventive replacement before reaching high operating hours would be beneficial.

5. **Physical Mechanisms**: This is consistent with failure mechanisms like fatigue, corrosion, or mechanical wear that accumulate over time.

$$\boxed{\text{β = 2.5 indicates wear-out with increasing failure rate; component ages and degrades over time}}$$

##### Summary

The Weibull distribution with β = 2.5 models a component that:
- Has high initial reliability (98.23% at 10,000 hours)
- Experiences wear-out (increasing hazard rate)
- Requires age-based maintenance strategies
- Is typical of mechanical/structural components subject to fatigue or wear

---

##### Final Answers Summary

| Question | Answer |
|----------|--------|
| (a) Reliability at 10,000 hours | 98.23% or 0.9823 |
| (b) Hazard rate at 10,000 hours | 4.47 × 10⁻⁶ failures/hour |
| (c) Aging behavior | Wear-out with increasing failure rate |

### Answer

**(a) 98.23%
(b) 4.47 × 10⁻⁶ failures per hour (or 0.00447 failures per 1,000 hours)
(c) β = 2.5 > 1 indicates the component exhibits wear-out behavior with an increasing failure rate over time, meaning the component does age and degrades with use.**

---

## 8. A parallel redundant system consists of 3 independent...

### Question

A parallel redundant system consists of 3 independent components, each with a reliability described by the Weibull distribution with shape parameter β = 1.5 and characteristic life η = 800 hours. What is the reliability of the system at t = 200 hours? (Note: In a parallel system, the system functions if at least one component is working.)

### Reasoning

#### Solution: Parallel System Reliability with Weibull Components

##### Problem Setup

I need to find the reliability of a parallel system with 3 independent components at t = 200 hours, where each component follows a Weibull distribution with β = 1.5 and η = 800 hours.

##### Step 1: Understand the Weibull Reliability Function

For a Weibull distribution, the reliability function is:
$$R(t) = e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$

where:
- β = 1.5 (shape parameter)
- η = 800 hours (characteristic life)
- t = 200 hours (time of interest)

##### Step 2: Calculate Individual Component Reliability

For one component at t = 200 hours:
$$R_{\text{component}}(200) = e^{-\left(\frac{200}{800}\right)^{1.5}}$$

$$R_{\text{component}}(200) = e^{-\left(\frac{1}{4}\right)^{1.5}}$$

$$R_{\text{component}}(200) = e^{-(0.25)^{1.5}}$$

Calculate (0.25)^1.5:
$$(0.25)^{1.5} = (0.25)^{3/2} = \sqrt{(0.25)^3} = \sqrt{0.015625} = 0.125$$

Therefore:
$$R_{\text{component}}(200) = e^{-0.125} = 0.8825$$

##### Step 3: Calculate Component Failure Probability

$$F_{\text{component}}(200) = 1 - R_{\text{component}}(200) = 1 - 0.8825 = 0.1175$$

##### Step 4: Apply Parallel System Logic

For a parallel system, the system **fails only if all components fail**. Since components are independent:

$$F_{\text{system}}(t) = \prod_{i=1}^{n} F_i(t)$$

With 3 identical components:
$$F_{\text{system}}(200) = \left[F_{\text{component}}(200)\right]^{3}$$

$$F_{\text{system}}(200) = (0.1175)^{3} = 0.001623$$

##### Step 5: Calculate System Reliability

$$R_{\text{system}}(200) = 1 - F_{\text{system}}(200)$$

$$R_{\text{system}}(200) = 1 - 0.001623 = 0.9984$$

##### Verification

Check that our logic is correct:
- Individual component reliability: 88.25%
- With 3 parallel components, system reliability should be much higher ✓
- System reliability: 99.84% ✓

This makes physical sense: even though each component has about an 11.75% chance of failing, the probability that all three fail simultaneously is very small (0.16%).

---

##### **Final Answer**

$$\boxed{R_{\text{system}}(200) = 0.9984 \text{ or } 99.84\%}$$

### Answer

**0.998**

---

## 9. Derive the hazard rate function h(t) for a system whose...

### Question

Derive the hazard rate function h(t) for a system whose lifetime follows a Weibull distribution with probability density function f(t) = (β/η)(t/η)^(β-1) exp[-(t/η)^β] for t ≥ 0, where β > 0 is the shape parameter and η > 0 is the characteristic life. Show how the hazard rate behavior changes depending on the value of β.

### Reasoning

#### Deriving the Hazard Rate for Weibull Distribution

##### Problem Statement

Derive the hazard rate function h(t) for a Weibull distribution and analyze how it depends on the shape parameter β.

##### Step 1: Recall the Definition of Hazard Rate

The hazard rate (failure rate) is defined as:
$$h(t) = \frac{f(t)}{R(t)}$$

where:
- f(t) is the probability density function
- R(t) is the reliability function

##### Step 2: Identify the Given PDF

The Weibull PDF is:
$$f(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$

##### Step 3: Derive the Reliability Function

The reliability function is related to the CDF by R(t) = 1 - F(t).

For the Weibull distribution, we can derive R(t) by integrating f(t) from t to ∞, or use the known form:

$$R(t) = e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$

We can verify this is correct since:
$$f(t) = -\frac{dR(t)}{dt} = -\frac{d}{dt}\left[e^{-\left(\frac{t}{\eta}\right)^{\beta}}\right]$$

Using the chain rule:
$$f(t) = -e^{-\left(\frac{t}{\eta}\right)^{\beta}} \cdot \left(-\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}\right) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$ ✓

##### Step 4: Calculate the Hazard Rate

$$h(t) = \frac{f(t)}{R(t)} = \frac{\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}}{e^{-\left(\frac{t}{\eta}\right)^{\beta}}}$$

The exponential terms cancel:
$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

This can be rewritten as:
$$h(t) = \frac{\beta}{\eta^{\beta}} t^{\beta-1}$$

Or more compactly:
$$\boxed{h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}}$$

##### Step 5: Analyze Behavior Based on β

The hazard rate behavior depends critically on the shape parameter β:

**Case 1: β < 1 (Decreasing Hazard Rate)**
- h(t) decreases with time
- Represents "infant mortality" or early failures
- Example: β = 0.5 gives h(t) ∝ t^(-0.5), which decreases

**Case 2: β = 1 (Constant Hazard Rate)**
- h(t) = 1/η (constant)
- This is the exponential distribution
- Represents random failures (memoryless property)

**Case 3: β > 1 (Increasing Hazard Rate)**
- h(t) increases with time
- Represents wear-out failures
- Example: β = 2 gives h(t) ∝ t, which increases linearly
- Example: β = 3.5 gives h(t) ∝ t^(2.5), which increases rapidly

##### Step 6: Verification

For β = 1:
$$h(t) = \frac{1}{\eta}\left(\frac{t}{\eta}\right)^{0} = \frac{1}{\eta} = \lambda$$

This matches the exponential distribution with MTTF = η ✓

---

##### **Final Answer**

$$\boxed{h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} = \frac{\beta}{\eta^{\beta}} t^{\beta-1}}$$

**Behavior:**
- **β < 1**: Decreasing failure rate (early failures/infant mortality)
- **β = 1**: Constant failure rate (random failures/exponential distribution)
- **β > 1**: Increasing failure rate (wear-out failures)

### Answer

**h(t) = (β/η)(t/η)^(β-1)

The hazard rate is decreasing for β < 1, constant for β = 1, and increasing for β > 1.**

---

## 10. A system has a linearly increasing hazard rate given by...

### Question

A system has a linearly increasing hazard rate given by h(t) = αt, where α is a positive constant and t ≥ 0. 

(a) Derive the cumulative distribution function F(t) for this system.
(b) Find the probability density function f(t).
(c) Calculate the reliability function R(t) at time t = 10 hours if α = 0.02 per hour².

### Reasoning

#### Deriving Distribution Functions from a Linear Hazard Rate

##### Problem Setup
Given: h(t) = αt for t ≥ 0, where α > 0

We need to find F(t), f(t), and evaluate R(10) when α = 0.02.

---

##### Part (a): Derive F(t)

###### Step 1: Recall the fundamental relationship
The cumulative hazard function H(t) is:
$$H(t) = \int_0^t h(u) \, du$$

And the reliability function is:
$$R(t) = e^{-H(t)}$$

###### Step 2: Calculate the cumulative hazard
$$H(t) = \int_0^t \alpha u \, du = \alpha \left[\frac{u^2}{2}\right]_0^t = \frac{\alpha t^2}{2}$$

###### Step 3: Find R(t)
$$R(t) = e^{-\alpha t^2/2}$$

###### Step 4: Convert to F(t)
Since F(t) = 1 - R(t):
$$\boxed{F(t) = 1 - e^{-\alpha t^2/2}, \quad t \geq 0}$$

This is the **Rayleigh distribution** with scale parameter related to α.

---

##### Part (b): Find f(t)

###### Step 1: Take the derivative of F(t)
$$f(t) = \frac{dF(t)}{dt} = \frac{d}{dt}\left(1 - e^{-\alpha t^2/2}\right)$$

###### Step 2: Apply the chain rule
$$f(t) = -e^{-\alpha t^2/2} \cdot \frac{d}{dt}\left(-\frac{\alpha t^2}{2}\right)$$

$$f(t) = e^{-\alpha t^2/2} \cdot \alpha t$$

$$\boxed{f(t) = \alpha t \, e^{-\alpha t^2/2}, \quad t \geq 0}$$

###### Step 3: Verification
We can verify using h(t) = f(t)/R(t):
$$h(t) = \frac{\alpha t \, e^{-\alpha t^2/2}}{e^{-\alpha t^2/2}} = \alpha t \quad \checkmark$$

---

##### Part (c): Calculate R(10) when α = 0.02

###### Step 1: Substitute values into R(t)
$$R(10) = e^{-\alpha (10)^2/2} = e^{-(0.02)(100)/2}$$

$$R(10) = e^{-2/2} = e^{-1}$$

###### Step 2: Calculate numerical value
$$R(10) = e^{-1} = 0.3679$$

$$\boxed{R(10) = 0.368 \text{ or } 36.8\%}$$

This means the system has a 36.8% probability of surviving to 10 hours.

---

##### Summary

The linearly increasing hazard rate h(t) = αt represents a system experiencing "wear-out" where the failure rate increases proportionally with time. This is characteristic of mechanical systems subject to aging or fatigue.

**Key Results:**
- **F(t) = 1 - e^(-αt²/2)** (Rayleigh CDF)
- **f(t) = αt e^(-αt²/2)** (Rayleigh PDF)
- **R(10) = 0.368** when α = 0.02 hr⁻²

### Answer

**(a) F(t) = 1 - e^(-αt²/2)

(b) f(t) = αt e^(-αt²/2)

(c) R(10) = e^(-1) ≈ 0.368 or 36.8%**

---

## 11. A manufacturer monitors the defect rate in production...

### Question

A manufacturer monitors the defect rate in production batches. Historical data from 20 batches (each containing 100 items) showed a total of 45 defective items. A new production method is implemented, and the first batch under the new method has 100 items with 1 defective item.

Using beta-binomial Bayesian methodology:
(a) Starting with a non-informative prior (Beta(1,1)), calculate the posterior distribution parameters using the historical data.
(b) Using the posterior from part (a) as the prior, calculate the new posterior distribution after observing the first batch from the new method.
(c) Compute the Bayesian point estimate for the defect rate under the new method and compare it to the classical MLE estimate using only the new batch data.
(d) Calculate a 95% Bayesian credibility interval for the new defect rate.

### Reasoning

#### Bayesian Analysis of Defect Rates with Process Change

##### Problem Setup

- **Historical data**: 20 batches × 100 items = 2000 items, 45 defective
- **New method data**: 1 batch × 100 items = 100 items, 1 defective
- **Prior**: Start with Beta(1,1)

---

##### Part (a): Posterior from Historical Data

###### Step 1: Initial prior
Non-informative uniform prior:
$$\text{Beta}(\alpha_0 = 1, \beta_0 = 1)$$

###### Step 2: Historical data summary
- Total items tested: n = 2000
- Total defectives (failures): x = 45
- Total non-defectives (successes): 2000 - 45 = 1955

###### Step 3: Update using Beta-Binomial conjugacy
For Beta(α, β) prior with x defectives in n trials:
$$\text{Posterior} = \text{Beta}(\alpha + x, \beta + (n-x))$$

$$\alpha_1 = 1 + 45 = 46$$
$$\beta_1 = 1 + 1955 = 1956$$

$$\boxed{\text{Posterior from historical data: Beta}(46, 1956)}$$

The historical defect rate estimate: 46/2002 ≈ 0.023 or 2.3%

---

##### Part (b): Posterior After New Method Batch

###### Step 1: Prior for new analysis
Use the historical posterior as the new prior:
$$\text{Beta}(46, 1956)$$

###### Step 2: New batch data
- Items tested: n = 100
- Defectives: x = 1
- Non-defectives: 100 - 1 = 99

###### Step 3: Calculate new posterior
$$\alpha_{new} = 46 + 1 = 47$$
$$\beta_{new} = 1956 + 99 = 2055$$

$$\boxed{\text{New posterior: Beta}(47, 2055)}$$

---

##### Part (c): Bayesian vs Classical Point Estimates

###### Bayesian Point Estimate (Posterior Mean)
$$\hat{p}_{Bayes} = \frac{\alpha_{new}}{\alpha_{new} + \beta_{new}} = \frac{47}{47 + 2055} = \frac{47}{2102}$$

$$\boxed{\hat{p}_{Bayes} = 0.0224 \text{ or } 2.24\%}$$

###### Classical MLE (Using Only New Batch)
$$\hat{p}_{MLE} = \frac{x}{n} = \frac{1}{100} = 0.01 \text{ or } 1.0\%$$

$$\boxed{\hat{p}_{MLE} = 0.01 \text{ or } 1.0\%}$$

###### Comparison
The Bayesian estimate (2.24%) is pulled toward the historical rate (2.3%), while the classical estimate (1.0%) is based solely on the limited new data. The Bayesian estimate is more conservative and less influenced by the small sample from the new method.

---

##### Part (d): 95% Bayesian Credibility Interval

###### Step 1: Parameters for interval calculation
We need the 2.5th and 97.5th percentiles of Beta(47, 2055).

###### Step 2: Calculate interval bounds
Using the Beta distribution quantile function:

**Lower bound (2.5th percentile):**
$$p_{0.025} = \text{BETAINV}(0.025, 47, 2055) \approx 0.0157$$

**Upper bound (97.5th percentile):**
$$p_{0.975} = \text{BETAINV}(0.975, 47, 2055) \approx 0.0305$$

###### Step 3: Final credibility interval
$$\boxed{\text{95% Bayesian Credibility Interval: }(0.0157, 0.0305)}$$

Or expressed as percentages: **(1.57%, 3.05%)**

###### Step 4: Interpretation
We are 95% confident that the true defect rate under the new method lies between 1.57% and 3.05%. The interval is relatively narrow due to the large amount of historical data incorporated.

---

##### Summary and Insights

| Metric | Bayesian | Classical |
|--------|----------|-----------|
| **Point Estimate** | 2.24% | 1.00% |
| **Data Used** | 2100 items | 100 items |
| **95% Interval** | (1.57%, 3.05%) | Would be wider |

**Key Observations:**
1. The new batch shows improvement (1% vs historical 2.3%)
2. The Bayesian estimate moderates this optimism by incorporating historical knowledge
3. More data from the new method would be needed to definitively conclude improvement
4. The credibility interval doesn't include zero, confirming some defect rate exists

### Answer

**(a) Posterior from historical data: Beta(46, 1956)

(b) Posterior after new batch: Beta(47, 2055)

(c) Bayesian estimate: p̂ = 47/2102 = 0.0224 (2.24%); Classical MLE: p̂ = 1/100 = 0.01 (1.0%)

(d) 95% Bayesian credibility interval: (0.0157, 0.0305) or (1.57%, 3.05%)**

---

## 12. A reliability engineer is comparing two suppliers for a...

### Question

A reliability engineer is comparing two suppliers for a critical electronic component. A sample of 25 components from Supplier A was tested for 1,000 hours each, resulting in 3 failures. A sample of 30 components from Supplier B was tested for 1,000 hours each, resulting in 8 failures. Both suppliers claim their components follow an exponential failure distribution.

(a) Calculate the estimated MTTF for each supplier's components.
(b) Using a chi-square test at the 90% confidence level, determine if Supplier A's MTTF is statistically better than 8,000 hours (their specification claim).
(c) What is the probability that a component from Supplier B will survive at least 500 hours?

Note: For chi-square distribution, χ²₀.₀₅,₆ = 12.59 and χ²₀.₉₅,₆ = 1.64; χ²₀.₀₅,₁₆ = 26.30 and χ²₀.₉₅,₁₆ = 7.96.

### Reasoning

#### Comparison of Two Suppliers Using Exponential Distribution Analysis

##### Given Information
- **Supplier A**: 25 components, 1,000 hours each, 3 failures
- **Supplier B**: 30 components, 1,000 hours each, 8 failures
- **Distribution**: Exponential (constant failure rate)
- **Supplier A's claim**: MTTF ≥ 8,000 hours
- **Confidence level for testing**: 90%

---

##### Part (a): Estimate MTTF for Each Supplier

###### Step 1: Calculate total test time for each supplier

**Supplier A:**
$$T_A = 25 \text{ components} \times 1,000 \text{ hours} = 25,000 \text{ unit-hours}$$

**Supplier B:**
$$T_B = 30 \text{ components} \times 1,000 \text{ hours} = 30,000 \text{ unit-hours}$$

###### Step 2: Apply the MTTF estimator for exponential distribution

For an exponential distribution with r failures observed:
$$\hat{\text{MTTF}} = \frac{\text{Total test time}}{\text{Number of failures}} = \frac{T}{r}$$

**Supplier A:**
$$\hat{\text{MTTF}}_A = \frac{25,000}{3} = 8,333.3 \text{ hours}$$

$$\boxed{\hat{\text{MTTF}}_A = 8,333 \text{ hours}}$$

**Supplier B:**
$$\hat{\text{MTTF}}_B = \frac{30,000}{8} = 3,750 \text{ hours}$$

$$\boxed{\hat{\text{MTTF}}_B = 3,750 \text{ hours}}$$

---

##### Part (b): Chi-Square Test for Supplier A's MTTF Claim

###### Step 1: State the hypotheses

- **H₀**: MTTF ≥ 8,000 hours (Supplier A meets specification)
- **H₁**: MTTF < 8,000 hours (Supplier A fails to meet specification)
- **Significance level**: α = 0.10 (for 90% confidence)
- **Test type**: One-tailed (lower tail)

###### Step 2: Understand the chi-square relationship

For exponential distribution testing, the test statistic is:
$$\chi^2 = \frac{2T}{\text{MTTF}_0}$$

where T is the total test time and MTTF₀ is the claimed value.

This statistic follows a chi-square distribution with degrees of freedom:
$$\text{df} = 2r$$

where r is the number of failures.

###### Step 3: Calculate the test statistic

For Supplier A:
- Total test time: T = 25,000 hours
- Claimed MTTF₀ = 8,000 hours
- Number of failures: r = 3
- Degrees of freedom: df = 2 × 3 = 6

$$\chi^2 = \frac{2 \times 25,000}{8,000} = \frac{50,000}{8,000} = 6.25$$

###### Step 4: Determine the critical value

For a one-tailed test (lower tail) at α = 0.10 with df = 6:
$$\chi^2_{0.10, 6} = \chi^2_{0.90, 6} = 1.64$$

(We use the 90th percentile because we're testing the lower tail)

###### Step 5: Make the decision

**Decision rule**: Reject H₀ if χ² < χ²₀.₉₀,₆

$$\chi^2_{calculated} = 6.25 > 1.64 = \chi^2_{critical}$$

**Conclusion**: We **fail to reject H₀**. There is insufficient evidence at the 90% confidence level to conclude that Supplier A's MTTF is less than 8,000 hours.

$$\boxed{\text{Supplier A's claim is statistically supported at 90\% confidence}}$$

###### Alternative interpretation using confidence bounds:

The lower 90% confidence bound for MTTF is:
$$\text{MTTF}_{lower} = \frac{2T}{\chi^2_{0.10, 6}} = \frac{50,000}{12.59} = 3,971 \text{ hours}$$

The upper 90% confidence bound is:
$$\text{MTTF}_{upper} = \frac{2T}{\chi^2_{0.90, 6}} = \frac{50,000}{1.64} = 30,488 \text{ hours}$$

Since the 90% confidence interval [3,971, 30,488] includes 8,000 hours, the claim is supported.

---

##### Part (c): Probability of Survival for Supplier B at t = 500 hours

###### Step 1: Determine the failure rate for Supplier B

$$\lambda_B = \frac{1}{\hat{\text{MTTF}}_B} = \frac{1}{3,750} = 2.667 \times 10^{-4} \text{ failures/hour}$$

###### Step 2: Apply the exponential reliability function

For an exponential distribution:
$$R(t) = e^{-\lambda t}$$

###### Step 3: Calculate reliability at t = 500 hours

$$R(500) = e^{-\lambda_B \times 500}$$

$$R(500) = e^{-(2.667 \times 10^{-4}) \times 500}$$

$$R(500) = e^{-0.1333}$$

$$R(500) = 0.8752$$

$$\boxed{R(500) = 0.875 \text{ or } 87.5\%}$$

**Interpretation**: A component from Supplier B has an 87.5% probability of surviving at least 500 hours.

---

##### Summary of Final Answers

| Question | Answer |
|----------|--------|
| **(a) Supplier A MTTF** | **8,333 hours** |
| **(a) Supplier B MTTF** | **3,750 hours** |
| **(b) Statistical test** | **Claim supported (χ² = 6.25 > 1.64)** |
| **(c) P(Survival > 500 hrs)** | **87.5%** |

###### Additional Insight:
Supplier A shows significantly better reliability than Supplier B (8,333 hours vs 3,750 hours MTTF). Supplier A's claim of MTTF ≥ 8,000 hours is statistically supported by the test data.

### Answer

**(a) Supplier A: MTTF = 8,333 hours; Supplier B: MTTF = 3,750 hours; (b) Supplier A's claim is statistically supported (χ² = 6.25 > χ²_crit = 1.64); (c) P(survival ≥ 500 hours) = 87.5%**

---

## 13. A semiconductor device has a lifetime that follows a...

### Question

A semiconductor device has a lifetime that follows a lognormal distribution with a shape parameter σ = 3.5. The manufacturer guarantees that 95% of devices will survive beyond 10,000 hours of operation. Calculate: (a) the median lifetime T₅₀ that satisfies this guarantee, and (b) the expected cumulative percent fallout at 5,000 hours under this design.

### Reasoning

###### Problem Analysis

Given:
- Lognormal distribution with shape parameter σ = 3.5
- Guarantee: 95% survival at t = 10,000 hours (i.e., 5% failure at 10,000 hours)
- Need to find: (a) median life T₅₀, (b) cumulative percent fallout at 5,000 hours

###### Part (a): Finding Median Lifetime T₅₀

For a lognormal distribution, the CDF is:
$$F(t) = \Phi\left(\frac{\ln(t/T_{50})}{\sigma}\right)$$

where Φ is the standard normal CDF.

**Given condition:** F(10,000) = 0.05

$$0.05 = \Phi\left(\frac{\ln(10,000/T_{50})}{3.5}\right)$$

###### Step 1: Find the z-value for 5th percentile

From standard normal tables:
$$\Phi(z) = 0.05 \implies z = -1.645$$

###### Step 2: Solve for T₅₀

$$\frac{\ln(10,000/T_{50})}{3.5} = -1.645$$

$$\ln(10,000/T_{50}) = -1.645 \times 3.5 = -5.758$$

$$\frac{10,000}{T_{50}} = e^{-5.758} = 0.003156$$

$$T_{50} = \frac{10,000}{0.003156} = 3,168,900 \text{ hours}$$

###### Step 3: Verify the result

Check: At t = 10,000 with T₅₀ = 3,168,900:
$$z = \frac{\ln(10,000/3,168,900)}{3.5} = \frac{\ln(0.003156)}{3.5} = \frac{-5.758}{3.5} = -1.645$$

$$F(10,000) = \Phi(-1.645) = 0.05$$ ✓

###### Part (b): Cumulative Percent Fallout at 5,000 Hours

Now find F(5,000) with T₅₀ = 3,168,900 hours and σ = 3.5

###### Step 4: Calculate z-value for t = 5,000

$$z = \frac{\ln(5,000/3,168,900)}{3.5}$$

$$\frac{5,000}{3,168,900} = 0.001578$$

$$\ln(0.001578) = -6.452$$

$$z = \frac{-6.452}{3.5} = -1.843$$

###### Step 5: Find cumulative probability

From standard normal tables:
- Φ(1.84) = 0.9671
- Φ(1.85) = 0.9678

Interpolating for z = 1.843:
$$\Phi(1.843) = 0.9671 + 0.3(0.9678 - 0.9671) = 0.9671 + 0.0002 = 0.9673$$

Therefore:
$$\Phi(-1.843) = 1 - 0.9673 = 0.0327$$

###### Step 6: Convert to percentage

$$\text{Cumulative Percent Fallout at 5,000 hours} = 0.0327 \times 100\% = 3.27\%$$

###### Verification

This makes physical sense:
- At 5,000 hours (half of the guaranteed 10,000 hours), we expect fewer failures
- 3.27% < 5%, which is consistent
- The median life (3.17 million hours) is much greater than both test times

---

### Answer

****(a) Median lifetime T₅₀ = 3,169,000 hours (approximately 3.17 million hours)**

**(b) Expected cumulative percent fallout at 5,000 hours = 3.3%****

---

## 14. A reliability test is conducted on 8 identical components...

### Question

A reliability test is conducted on 8 identical components under accelerated stress conditions. At the end of the test, exactly 3 components have failed and 5 have survived. 

(a) How many different failure patterns are possible?

(b) If we label the components as A, B, C, D, E, F, G, H, and we know that component A survived, how many different failure patterns are now possible?

(c) What is the probability that components A and B both survive, assuming all failure patterns are equally likely?

### Reasoning

#### Solution: Counting Failure Patterns in Reliability Testing

##### Part (a): Total Number of Failure Patterns

###### Problem Understanding
I need to find how many different arrangements are possible when:
- There are 8 components total
- 3 components fail (F)
- 5 components survive (S)

###### Solution Approach
This is a combinations problem. I need to count how many ways I can choose which 3 positions (out of 8) will have failures.

###### Formula Used
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

###### Calculation
$$\binom{8}{3} = \frac{8!}{3!(8-3)!} = \frac{8!}{3! \cdot 5!}$$

Calculating:
$$\binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = \frac{336}{6} = 56$$

**Answer for part (a): 56 different failure patterns**

---

##### Part (b): Failure Patterns Given Component A Survived

###### Problem Understanding
Now we have a constraint: Component A must survive.

This means:
- Component A is fixed as a survivor
- We need to choose 3 failures from the remaining 7 components (B through H)
- Equivalently, we need 5 survivors total, but A is already one of them, so we choose 4 more survivors from 7 components

###### Solution Approach
Since A must survive, we only need to determine which 3 of the remaining 7 components fail.

###### Calculation
$$\binom{7}{3} = \frac{7!}{3! \cdot 4!} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = \frac{210}{6} = 35$$

**Answer for part (b): 35 different failure patterns**

---

##### Part (c): Probability Both A and B Survive

###### Problem Understanding
We want to find the probability that both A and B are among the 5 survivors, assuming all failure patterns from part (a) are equally likely.

###### Solution Approach
- Total possible patterns = 56 (from part a)
- Favorable patterns = patterns where both A and B survive
- If A and B both survive, we need 3 failures from the remaining 6 components (C through H)

###### Calculation of Favorable Outcomes
$$\binom{6}{3} = \frac{6!}{3! \cdot 3!} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = \frac{120}{6} = 20$$

###### Probability Calculation
$$P(\text{A and B both survive}) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}} = \frac{20}{56} = \frac{5}{14}$$

Converting to decimal:
$$\frac{5}{14} = 0.357143$$

Converting to percentage:
$$0.357143 \times 100\% = 35.71\%$$

**Answer for part (c): 5/14 or approximately 35.71%**

---

##### Verification for Part (c)

Alternative approach using conditional probability:
- P(A survives) = 5/8 (5 survivors out of 8 components)
- P(B survives | A survives) = 4/7 (4 remaining survivor spots out of 7 remaining components)
- P(both survive) = (5/8) × (4/7) = 20/56 = 5/14 ✓

This confirms our answer.

### Answer

**(a) **56 different failure patterns**

(b) **35 different failure patterns**

(c) **5/14 or 35.71%****

---

## 15. A manufacturer conducts a reliability study on electronic...

### Question

A manufacturer conducts a reliability study on electronic modules using a defect model approach. A sample of n = 200 modules is tested with inspections at 500 hours, 1,000 hours, and 2,000 hours (end of test). The failure data collected shows:
- 12 failures discovered at T₁ = 500 hours
- 8 failures discovered at T₂ = 1,000 hours  
- 5 failures discovered at T₃ = 2,000 hours
- 175 modules survived to the end of test

Assume the defective subpopulation follows an exponential distribution with failure rate λ, and let p represent the fraction of defective modules in the population.

(a) Write the specific likelihood function for this data.

(b) Derive the maximum likelihood estimate (MLE) for the fraction defective, p.

(c) If the estimated failure rate is λ̂ = 0.0015 per hour, calculate the numerical MLE for p.

### Reasoning

#### Solution: Defect Model Likelihood for Electronic Modules

##### Part (a): Likelihood Function for This Data

###### Given Information
- n = 200 modules
- T₁ = 500 hours, r₁ = 12 failures
- T₂ = 1,000 hours, r₂ = 8 failures
- T₃ = 2,000 hours, r₃ = 5 failures
- Survivors: n - r = 200 - 25 = 175 modules
- Total failures: r = 12 + 8 + 5 = 25

###### Defect Model with Exponential Distribution

For exponential distribution with failure rate λ:
$$F(t) = 1 - e^{-\lambda t}$$

###### Interval Failure Probabilities

**Interval 1: (0, 500]**
$$\pi_1 = p \cdot F(500) = p(1 - e^{-500\lambda})$$

**Interval 2: (500, 1000]**
$$\pi_2 = p[F(1000) - F(500)] = p[e^{-500\lambda} - e^{-1000\lambda}]$$

**Interval 3: (1000, 2000]**
$$\pi_3 = p[F(2000) - F(1000)] = p[e^{-1000\lambda} - e^{-2000\lambda}]$$

**Survival beyond 2000 hours:**
$$\pi_4 = 1 - p \cdot F(2000) = 1 - p(1 - e^{-2000\lambda})$$

###### Complete Likelihood Function

$$\boxed{L(p, \lambda) = \frac{200!}{12! \cdot 8! \cdot 5! \cdot 175!} \cdot [p(1-e^{-500\lambda})]^{12} \cdot [p(e^{-500\lambda}-e^{-1000\lambda})]^{8}}$$
$$\boxed{\cdot [p(e^{-1000\lambda}-e^{-2000\lambda})]^{5} \cdot [1-p(1-e^{-2000\lambda})]^{175}}$$

Simplifying by extracting p:

$$\boxed{L(p, \lambda) = C \cdot p^{25} \cdot (1-e^{-500\lambda})^{12} \cdot (e^{-500\lambda}-e^{-1000\lambda})^{8}}$$
$$\boxed{\cdot (e^{-1000\lambda}-e^{-2000\lambda})^{5} \cdot [1-p(1-e^{-2000\lambda})]^{175}}$$

where C is the multinomial coefficient.

---

##### Part (b): Maximum Likelihood Estimate for p

###### Log-Likelihood Function

Taking the natural logarithm (ignoring constants):

$$\ln L = 25\ln p + 12\ln(1-e^{-500\lambda}) + 8\ln(e^{-500\lambda}-e^{-1000\lambda})$$
$$+ 5\ln(e^{-1000\lambda}-e^{-2000\lambda}) + 175\ln[1-p(1-e^{-2000\lambda})]$$

###### Taking Derivative with Respect to p

$$\frac{\partial \ln L}{\partial p} = \frac{25}{p} + 175 \cdot \frac{-(1-e^{-2000\lambda})}{1-p(1-e^{-2000\lambda})}$$

###### Setting Equal to Zero

$$\frac{25}{p} = \frac{175(1-e^{-2000\lambda})}{1-p(1-e^{-2000\lambda})}$$

Let $q = 1 - e^{-2000\lambda}$ (the probability a defective unit fails by time 2000)

$$\frac{25}{p} = \frac{175q}{1-pq}$$

$$25(1-pq) = 175pq$$

$$25 = 25pq + 175pq$$

$$25 = 200pq$$

$$\boxed{\hat{p} = \frac{25}{200q} = \frac{25}{200(1-e^{-2000\lambda})} = \frac{r}{n(1-e^{-2000\lambda})}}$$

More generally:

$$\boxed{\hat{p}_{MLE} = \frac{r}{n \cdot F(T_k; \hat{\lambda})}}$$

where r is total failures, n is sample size, and $T_k$ is the final inspection time.

---

##### Part (c): Numerical MLE for p

###### Given Information
- λ̂ = 0.0015 per hour
- r = 25 failures
- n = 200 modules
- T₃ = 2,000 hours

###### Calculate F(2000)

$$F(2000) = 1 - e^{-\lambda \cdot t} = 1 - e^{-0.0015 \times 2000}$$

$$= 1 - e^{-3.0}$$

$$= 1 - 0.049787$$

$$= 0.950213$$

###### Calculate p̂

$$\hat{p} = \frac{25}{200 \times 0.950213} = \frac{25}{190.043} = 0.1315$$

Converting to percentage:

$$\hat{p} = 13.15\%$$

###### Interpretation

This means approximately **13.15%** of the modules in the population are estimated to be defective (susceptible to failure). The remaining 86.85% are estimated to be non-defective and will not fail during the operational lifetime.

###### Verification

Expected failures if p = 0.1315:
$$E[\text{failures}] = n \cdot p \cdot F(2000) = 200 \times 0.1315 \times 0.950213 = 25$$ ✓

This matches our observed 25 failures, confirming our calculation.

### Answer

**(a) **Likelihood function:**
$$L(p, \lambda) = C \cdot p^{25} \cdot (1-e^{-500\lambda})^{12} \cdot (e^{-500\lambda}-e^{-1000\lambda})^{8} \cdot (e^{-1000\lambda}-e^{-2000\lambda})^{5} \cdot [1-p(1-e^{-2000\lambda})]^{175}$$

(b) **MLE for fraction defective:**
$$\hat{p} = \frac{r}{n \cdot F(T_k; \hat{\lambda})} = \frac{25}{200(1-e^{-2000\lambda})}$$

(c) **Numerical MLE:** 
$$\hat{p} = 0.1315 \text{ or } 13.15\%$$**

---

## 16. A power supply unit has a constant failure rate of λ =...

### Question

A power supply unit has a constant failure rate of λ = 0.004 failures per 1000 hours. The unit operates continuously and is replaced upon failure (renewal process). For a mission duration of 50,000 hours:

(a) What is the probability that exactly 3 failures will occur during the mission?
(b) What is the minimum number of spare power supplies needed to ensure at least 99% confidence that spares will not be exhausted during the mission?
(c) If the system has already operated for 20,000 hours with 1 failure, what is the probability of having 2 or more additional failures in the remaining 30,000 hours?

### Reasoning

###### Problem Setup

Given:
- Constant failure rate: λ = 0.004 per 1000 hours = 0.000004 per hour
- Mission duration: T = 50,000 hours
- This is a renewal process, so failures follow a Poisson distribution

---

###### Part (a): Probability of Exactly 3 Failures

**Step 1: Calculate expected number of failures**

For a Poisson process, the mean number of failures over time T is:
$$\mu = \lambda T = 0.004 \times \frac{50,000}{1,000} = 0.004 \times 50 = 0.2$$

**Step 2: Apply Poisson probability formula**

The probability of exactly k failures is:
$$P(N = k) = \frac{\mu^k e^{-\mu}}{k!}$$

For k = 3:
$$P(N = 3) = \frac{(0.2)^3 e^{-0.2}}{3!} = \frac{0.008 \times e^{-0.2}}{6}$$

$$e^{-0.2} = 0.8187$$

$$P(N = 3) = \frac{0.008 \times 0.8187}{6} = \frac{0.006550}{6} = 0.001092$$

$$\boxed{P(N = 3) = 0.00109 \text{ or } 0.109\%}$$

---

###### Part (b): Number of Spares for 99% Confidence

We need to find minimum n such that:
$$P(N \leq n) \geq 0.99$$

**Calculate cumulative probabilities:**

$$P(N = 0) = e^{-0.2} = 0.8187$$
$$P(N \leq 0) = 0.8187 < 0.99$$ ❌

$$P(N = 1) = \frac{0.2^1 \times 0.8187}{1!} = 0.1637$$
$$P(N \leq 1) = 0.8187 + 0.1637 = 0.9824 < 0.99$$ ❌

$$P(N = 2) = \frac{0.2^2 \times 0.8187}{2!} = \frac{0.04 \times 0.8187}{2} = 0.01637$$
$$P(N \leq 2) = 0.9824 + 0.01637 = 0.9988 \geq 0.99$$ ✓

$$\boxed{\text{Minimum spares needed: } n = 2}$$

With 2 spares, the probability of not exhausting spares = 99.88%

---

###### Part (c): Conditional Probability of Additional Failures

Given: 1 failure already occurred in first 20,000 hours
Find: P(2 or more additional failures in remaining 30,000 hours)

**Step 1: Calculate expected failures in remaining time**

For the remaining 30,000 hours:
$$\mu_{remaining} = 0.004 \times \frac{30,000}{1,000} = 0.004 \times 30 = 0.12$$

**Step 2: Calculate probability of 2 or more failures**

Due to the memoryless property and independent increments of the Poisson process, failures in the remaining time are independent of past failures.

$$P(N \geq 2) = 1 - P(N \leq 1) = 1 - [P(N = 0) + P(N = 1)]$$

$$P(N = 0) = e^{-0.12} = 0.8869$$

$$P(N = 1) = 0.12 \times e^{-0.12} = 0.12 \times 0.8869 = 0.1064$$

$$P(N \geq 2) = 1 - (0.8869 + 0.1064) = 1 - 0.9933 = 0.0067$$

$$\boxed{P(\text{2 or more additional failures}) = 0.0067 \text{ or } 0.67\%}$$

---

### Answer

**(a) 0.00109 or 0.109%
(b) 2 spare units
(c) 0.0067 or 0.67%**

---

## 17. A manufacturer conducts an accelerated life test on 300 LED...

### Question

A manufacturer conducts an accelerated life test on 300 LED light bulbs for 2500 hours. Assuming exponentially distributed failure times, failures are observed at the following times (in hours): 145, 389, 672, 891, 1205, 1456, 1823, and 2187. Using the chi-squared distribution method, calculate the 90% two-sided confidence interval for the Mean Time To Failure (MTTF). Also calculate the point estimate of the MTTF and interpret all results.

### Reasoning

#### Confidence Interval for MTTF Problem

##### Problem Setup

**Given Information:**
- n = 300 LED bulbs tested
- Test duration: T = 2500 hours
- Number of failures: r = 8
- Failure times: 145, 389, 672, 891, 1205, 1456, 1823, 2187 hours
- Assumption: Exponentially distributed failure times
- Required: 90% two-sided confidence interval for MTTF

##### Step 1: Calculate Total Time on Test (TTT)

For Type I censoring with exponential distribution:
$$TTT = \sum_{i=1}^{r} t_i + (n-r) \cdot T$$

**Sum of failure times:**
$$\sum t_i = 145 + 389 + 672 + 891 + 1205 + 1456 + 1823 + 2187 = 8,768 \text{ hours}$$

**Number of survivors:**
$$n - r = 300 - 8 = 292 \text{ bulbs survived to 2500 hours}$$

**Total Time on Test:**
$$TTT = 8,768 + (292)(2500) = 8,768 + 730,000 = 738,768 \text{ hours}$$

##### Step 2: Calculate Point Estimate (MLE) of MTTF

For exponential distribution, the Maximum Likelihood Estimate of MTTF is:
$$\hat{\theta} = \frac{TTT}{r} = \frac{738,768}{8} = 92,346 \text{ hours}$$

$$\boxed{\text{Point Estimate: } \hat{\theta} = 92,346 \text{ hours}}$$

##### Step 3: Construct 90% Two-Sided Confidence Interval

For exponential distribution, the confidence interval for MTTF θ is based on the fact that:
$$\frac{2 \cdot TTT}{\theta} \sim \chi^2_{2r}$$

This gives us the confidence interval:
$$\frac{2 \cdot TTT}{\chi^2_{\alpha/2, 2r}} \leq \theta \leq \frac{2 \cdot TTT}{\chi^2_{1-\alpha/2, 2r}}$$

For 90% confidence interval, α = 0.10, so:
- Lower critical value: χ²₀.₉₅,₁₆ (upper 5%)
- Upper critical value: χ²₀.₀₅,₁₆ (lower 5%)
- Degrees of freedom: 2r = 2(8) = 16

##### Step 4: Find Chi-Squared Critical Values

From chi-squared tables with df = 16:
- χ²₀.₀₅,₁₆ = 26.296 (lower tail)
- χ²₀.₉₅,₁₆ = 7.962 (upper tail)

##### Step 5: Calculate Confidence Bounds

**Calculate 2·TTT:**
$$2 \cdot TTT = 2 \times 738,768 = 1,477,536$$

**Lower confidence bound:**
$$\theta_L = \frac{1,477,536}{26.296} = 56,184.6 \text{ hours}$$

**Upper confidence bound:**
$$\theta_U = \frac{1,477,536}{7.962} = 185,589.5 \text{ hours}$$

##### Step 6: Final Results

$$\boxed{\text{90\% Confidence Interval: } (56,185 \text{ hours}, 185,590 \text{ hours})}$$

---

##### Interpretation

###### Point Estimate (92,346 hours):
- This is our **best single estimate** of the true MTTF based on the observed data
- It represents the average lifetime we expect for the LED bulbs
- Approximately **10.5 years** of continuous operation

###### 90% Confidence Interval (56,185 to 185,590 hours):
- We are **90% confident** that the true MTTF lies within this range
- The interval is **quite wide** (ratio of upper to lower bound ≈ 3.3), reflecting the uncertainty due to the small number of failures (only 8 out of 300 units)
- **Lower bound (56,185 hours):** Conservative estimate - approximately 6.4 years
- **Upper bound (185,590 hours):** Optimistic estimate - approximately 21.2 years

###### Practical Implications:
- With only 8 failures observed, there is substantial uncertainty in the MTTF estimate
- The manufacturer can claim with 90% confidence that the average bulb life is at least 56,185 hours
- More failures (longer test or more units) would narrow this confidence interval
- The wide interval suggests the product is highly reliable, but more testing may be needed for precise MTTF determination

---

##### Summary Table

| Statistic | Value (hours) | Approximate Years |
|-----------|---------------|-------------------|
| Point Estimate (MTTF) | 92,346 | 10.5 |
| 90% CI Lower Bound | 56,185 | 6.4 |
| 90% CI Upper Bound | 185,590 | 21.2 |

### Answer

****Point Estimate of MTTF: 92,346 hours**

**90% Confidence Interval for MTTF: (56,185 hours, 185,590 hours)****

---

## 18. A quality control inspector has a box containing 20...

### Question

A quality control inspector has a box containing 20 electronic components: 5 are defective and 15 are functional. Due to a labeling error, the components are not marked. The inspector randomly selects 3 components for installation in a critical system. What is the probability that exactly 2 of the selected components are functional? What is the probability that at least 2 of the selected components are functional?

### Reasoning

#### Electronic Components Selection Problem

##### Given Information
- Total components: 20
- Defective components: 5
- Functional components: 15
- Selection: 3 components randomly selected (without replacement)

##### Part 1: Probability of Exactly 2 Functional Components

###### Method: Using Combinations

To get exactly 2 functional components, we need 2 functional AND 1 defective.

**Formula:**
$$P(\text{exactly 2 functional}) = \frac{\binom{15}{2} \times \binom{5}{1}}{\binom{20}{3}}$$

**Calculations:**

Number of ways to choose 2 functional from 15:
$$\binom{15}{2} = \frac{15!}{2!(15-2)!} = \frac{15 \times 14}{2 \times 1} = \frac{210}{2} = 105$$

Number of ways to choose 1 defective from 5:
$$\binom{5}{1} = \frac{5!}{1!(5-1)!} = 5$$

Total number of ways to choose 3 components from 20:
$$\binom{20}{3} = \frac{20!}{3!(20-3)!} = \frac{20 \times 19 \times 18}{3 \times 2 \times 1} = \frac{6840}{6} = 1140$$

**Probability of exactly 2 functional:**
$$P(\text{exactly 2 functional}) = \frac{105 \times 5}{1140} = \frac{525}{1140} = \frac{105}{228} = \frac{35}{76}$$

$$\boxed{P(\text{exactly 2 functional}) = \frac{35}{76} \approx 0.4605 \text{ or } 46.05\%}$$

---

##### Part 2: Probability of At Least 2 Functional Components

"At least 2 functional" means either exactly 2 functional OR all 3 functional.

**Formula:**
$$P(\text{at least 2 functional}) = P(\text{exactly 2 functional}) + P(\text{all 3 functional})$$

**Calculate P(all 3 functional):**

Number of ways to choose 3 functional from 15:
$$\binom{15}{3} = \frac{15!}{3!(15-3)!} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = \frac{2730}{6} = 455$$

$$P(\text{all 3 functional}) = \frac{455}{1140} = \frac{91}{228}$$

**Total probability of at least 2 functional:**
$$P(\text{at least 2 functional}) = \frac{525}{1140} + \frac{455}{1140} = \frac{980}{1140} = \frac{245}{285} = \frac{49}{57}$$

$$\boxed{P(\text{at least 2 functional}) = \frac{49}{57} \approx 0.8596 \text{ or } 85.96\%}$$

---

##### Summary of Final Answers

| Event | Probability | Decimal | Percentage |
|-------|-------------|---------|------------|
| Exactly 2 functional | 35/76 | 0.4605 | 46.05% |
| At least 2 functional | 49/57 | 0.8596 | 85.96% |

### Answer

**Probability of exactly 2 functional: **35/76 ≈ 0.4605**

Probability of at least 2 functional: **49/57 ≈ 0.8596****

---

## 19. A reliability engineer is testing power supply units that...

### Question

A reliability engineer is testing power supply units that follow a Weibull distribution with a shape parameter β = 1.5. The specification requires that the average failure rate over the first 5,000 hours of operation must not exceed 200 FITs. What is the minimum characteristic life (η) required to meet this specification? Additionally, what would be the instantaneous failure rate at exactly t = 5,000 hours for this minimum characteristic life?

### Reasoning

#### Finding Minimum Characteristic Life for Weibull Distribution with Average Failure Rate Constraint

##### Problem Statement

Find the minimum characteristic life (η) for a Weibull distribution with β = 1.5 such that the average failure rate over [0, 5000] hours does not exceed 200 FITs. Then calculate the instantaneous failure rate at t = 5,000 hours.

##### Step 1: Understanding the Key Concepts

**FIT (Failure In Time)**: 1 FIT = 1 failure per 10⁹ device-hours

**Weibull Distribution**:
- CDF: $F(t) = 1 - e^{-(t/\eta)^\beta}$
- Reliability: $R(t) = e^{-(t/\eta)^\beta}$
- Instantaneous failure rate: $h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$

**Average Failure Rate** over [0, t]:
$$\bar{\lambda}(t) = \frac{F(t)}{t}$$

##### Step 2: Set Up the Constraint Equation

Given:
- Maximum average failure rate: 200 FITs = 200 × 10⁻⁹ failures/hour
- Time period: t = 5,000 hours
- Shape parameter: β = 1.5

The constraint:
$$\bar{\lambda}(5000) \leq 200 \times 10^{-9}$$

$$\frac{F(5000)}{5000} \leq 200 \times 10^{-9}$$

$$F(5000) \leq 200 \times 10^{-9} \times 5000 = 1.0 \times 10^{-3}$$

For the minimum η, we use equality:
$$F(5000) = 0.001$$

##### Step 3: Apply the Weibull CDF

$$F(t) = 1 - e^{-(t/\eta)^\beta}$$

Setting F(5000) = 0.001:
$$1 - e^{-(5000/\eta)^{1.5}} = 0.001$$

$$e^{-(5000/\eta)^{1.5}} = 0.999$$

Taking natural logarithm:
$$-(5000/\eta)^{1.5} = \ln(0.999)$$

$$-(5000/\eta)^{1.5} = -0.001000500$$

$$(5000/\eta)^{1.5} = 0.001000500$$

##### Step 4: Solve for η

$$\frac{5000}{\eta} = (0.001000500)^{1/1.5}$$

$$\frac{5000}{\eta} = (0.001000500)^{2/3}$$

$$\frac{5000}{\eta} = 0.01000333$$

$$\eta = \frac{5000}{0.01000333} = 499,834 \text{ hours}$$

$$\eta \approx 5.0 \times 10^{5} \text{ hours}$$

##### Step 5: Verification

Let's verify with η = 499,834 hours:

$$F(5000) = 1 - e^{-(5000/499834)^{1.5}}$$

$$= 1 - e^{-(0.01000333)^{1.5}}$$

$$= 1 - e^{-0.001000500}$$

$$= 1 - 0.999000 = 0.001$$ ✓

$$\bar{\lambda} = \frac{0.001}{5000} = 2 \times 10^{-7} = 200 \times 10^{-9} = 200 \text{ FITs}$$ ✓

##### Step 6: Calculate Instantaneous Failure Rate at t = 5,000 hours

The Weibull instantaneous failure rate (hazard function):
$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

With β = 1.5, η = 499,834 hours, t = 5,000 hours:

$$h(5000) = \frac{1.5}{499834}\left(\frac{5000}{499834}\right)^{0.5}$$

$$= \frac{1.5}{499834} \times (0.01000333)^{0.5}$$

$$= \frac{1.5}{499834} \times 0.1000166$$

$$= 3.001 \times 10^{-6} \times 0.1000166$$

$$= 3.001 \times 10^{-7} \text{ failures/hour}$$

$$= 300.1 \text{ FITs}$$

##### Step 7: Interpretation

Note that the instantaneous failure rate (300.1 FITs) at t = 5,000 hours is **higher** than the average failure rate (200 FITs) over [0, 5000] hours. This makes sense because:
- β = 1.5 > 1 indicates an increasing failure rate (wear-out pattern)
- The average is pulled down by the lower failure rates early in life
- At exactly 5,000 hours, the system is experiencing higher instantaneous risk

---

##### Final Answers

**Minimum characteristic life:** η ≈ **5.0 × 10⁵ hours** (or 499,834 hours)

**Instantaneous failure rate at t = 5,000 hours:** h(5000) ≈ **300 FITs**

The power supply units must have a characteristic life of at least 500,000 hours to meet the specification of 200 FITs average failure rate over the first 5,000 hours of operation.

### Answer

**Minimum characteristic life: η = 5.0 × 10⁵ hours (500,000 hours)

Instantaneous failure rate at t = 5,000 hours: h(5000) = 300 FITs**

---

## 20. A communication system component has a reliability function...

### Question

A communication system component has a reliability function (survival function) given by $R(t) = e^{-0.5t}$ for $t \geq 0$, where $t$ is measured in years. Find:
1. The cumulative distribution function (CDF) F(t)
2. The probability density function (PDF) f(t)
3. The hazard rate function h(t)
4. The mean time to failure (MTTF)
5. The design life $T_{90}$ (time by which 10% of units will have failed)

### Reasoning

#### Solution: Analyzing an Exponential Reliability Function

##### Given Information
- Reliability function: $R(t) = e^{-0.5t}$ for $t \geq 0$

Let me verify this is a valid reliability function:
- $R(0) = e^{0} = 1$ ✓
- $R(\infty) = e^{-\infty} = 0$ ✓
- R(t) is decreasing ✓

---

##### Part 1: Finding the CDF

The CDF is related to the reliability function by:
$$F(t) = 1 - R(t)$$

**Calculation:**
$$\boxed{F(t) = 1 - e^{-0.5t}, \quad t \geq 0}$$

---

##### Part 2: Finding the PDF

The PDF can be found either by differentiating F(t) or by using $f(t) = -\frac{dR(t)}{dt}$:

**Using the CDF:**
$$f(t) = \frac{dF(t)}{dt} = \frac{d}{dt}(1 - e^{-0.5t})$$

$$f(t) = 0 - e^{-0.5t} \cdot (-0.5)$$

$$\boxed{f(t) = 0.5e^{-0.5t}, \quad t \geq 0}$$

**Verification:** This is the exponential distribution with λ = 0.5.

---

##### Part 3: Finding the Hazard Rate Function

The hazard rate (failure rate) is:
$$h(t) = \frac{f(t)}{R(t)}$$

**Calculation:**
$$h(t) = \frac{0.5e^{-0.5t}}{e^{-0.5t}}$$

$$\boxed{h(t) = 0.5 \text{ failures/year (constant)}}$$

**Note:** This confirms the exponential distribution has a constant hazard rate.

---

##### Part 4: Finding the MTTF (Mean Time To Failure)

For non-negative random variables:
$$MTTF = E[T] = \int_0^{\infty} R(t) \, dt$$

**Calculation:**
$$MTTF = \int_0^{\infty} e^{-0.5t} dt$$

$$MTTF = \left[-\frac{1}{0.5}e^{-0.5t}\right]_0^{\infty}$$

$$MTTF = \left[-2e^{-0.5t}\right]_0^{\infty}$$

$$MTTF = 0 - (-2) = 2$$

$$\boxed{MTTF = 2 \text{ years}}$$

**Alternative:** For exponential distribution, $MTTF = \frac{1}{\lambda} = \frac{1}{0.5} = 2$ years.

---

##### Part 5: Finding T₉₀ (Design Life)

T₉₀ is the time at which F(t) = 0.10 (10% have failed), or equivalently R(t) = 0.90:

$$R(T_{90}) = 0.90$$

$$e^{-0.5T_{90}} = 0.90$$

**Solving for T₉₀:**
$$-0.5T_{90} = \ln(0.90)$$

$$T_{90} = \frac{\ln(0.90)}{-0.5}$$

$$T_{90} = \frac{-0.10536}{-0.5}$$

$$\boxed{T_{90} = 0.211 \text{ years} \approx 2.53 \text{ months}}$$

---

##### Final Answers Summary

| Quantity | Result |
|----------|--------|
| **CDF** | $F(t) = 1 - e^{-0.5t}$ |
| **PDF** | $f(t) = 0.5e^{-0.5t}$ |
| **Hazard Rate** | $h(t) = 0.5$ failures/year (constant) |
| **MTTF** | $2$ years |
| **T₉₀** | $0.211$ years ≈ 2.53 months |

### Answer

**F(t) = 1 - e^(-0.5t), f(t) = 0.5e^(-0.5t), h(t) = 0.5 (constant hazard rate), MTTF = 2 years, and T₉₀ = 0.211 years.**

---

## 21. A quality control system uses two independent inspection...

### Question

A quality control system uses two independent inspection methods to detect faulty products. Method 1 (visual inspection) has a probability of 0.85 of detecting a fault when one exists. Method 2 (automated testing) has a probability of 0.75 of detecting a fault when one exists. A product with a fault goes through both inspections independently.

1. What is the probability that at least one method detects the fault?
2. What is the probability that both methods detect the fault?
3. Given that at least one method detected a fault, what is the probability that both methods detected it?
4. Are the events "Method 1 detects the fault" and "Method 2 detects the fault" independent? Prove your answer.

### Reasoning

#### Solution: Probability Analysis of Dual Inspection System

##### Problem Setup

For a faulty product:
- **Event M₁**: Method 1 detects the fault, P(M₁) = 0.85
- **Event M₂**: Method 2 detects the fault, P(M₂) = 0.75
- The two inspection methods operate **independently**

---

##### Part 1: Probability That At Least One Method Detects the Fault

**Approach 1 - Using Complement:**

"At least one detects" is the complement of "neither detects."

$$P(\text{at least one}) = 1 - P(\text{neither detects})$$

$$P(\text{neither}) = P(M_1^c \cap M_2^c)$$

Since the methods are independent:
$$P(M_1^c \cap M_2^c) = P(M_1^c) \times P(M_2^c)$$

$$P(M_1^c) = 1 - 0.85 = 0.15$$
$$P(M_2^c) = 1 - 0.75 = 0.25$$

$$P(\text{neither}) = 0.15 \times 0.25 = 0.0375$$

$$P(\text{at least one}) = 1 - 0.0375 = 0.9625$$

**Approach 2 - Using Inclusion-Exclusion (verification):**

$$P(M_1 \cup M_2) = P(M_1) + P(M_2) - P(M_1 \cap M_2)$$

$$P(M_1 \cap M_2) = P(M_1) \times P(M_2) = 0.85 \times 0.75 = 0.6375$$

$$P(M_1 \cup M_2) = 0.85 + 0.75 - 0.6375 = 0.9625 \checkmark$$

$$\boxed{P(\text{at least one detects}) = 0.9625 = 96.25\%}$$

---

##### Part 2: Probability That Both Methods Detect the Fault

Since the methods are independent:

$$P(M_1 \cap M_2) = P(M_1) \times P(M_2)$$

$$P(M_1 \cap M_2) = 0.85 \times 0.75$$

$$\boxed{P(\text{both detect}) = 0.6375 = 63.75\%}$$

---

##### Part 3: Conditional Probability - Both Detect Given At Least One Detects

We need: $P(\text{both} | \text{at least one})$

Using conditional probability:
$$P(M_1 \cap M_2 | M_1 \cup M_2) = \frac{P[(M_1 \cap M_2) \cap (M_1 \cup M_2)]}{P(M_1 \cup M_2)}$$

**Key insight:** If both methods detect, then at least one detects, so:
$$(M_1 \cap M_2) \cap (M_1 \cup M_2) = M_1 \cap M_2$$

Therefore:
$$P(M_1 \cap M_2 | M_1 \cup M_2) = \frac{P(M_1 \cap M_2)}{P(M_1 \cup M_2)}$$

$$P(M_1 \cap M_2 | M_1 \cup M_2) = \frac{0.6375}{0.9625}$$

$$\boxed{P(\text{both} | \text{at least one}) = 0.6623 = 66.23\%}$$

---

##### Part 4: Proving Independence of M₁ and M₂

**Definition of Independence:**
Events M₁ and M₂ are independent if and only if:
$$P(M_1 \cap M_2) = P(M_1) \times P(M_2)$$

**Verification:**

From the problem statement, we're told the inspections operate independently.

Let's verify mathematically:
- $P(M_1) \times P(M_2) = 0.85 \times 0.75 = 0.6375$
- $P(M_1 \cap M_2) = 0.6375$ (calculated in Part 2)

**Since:**
$$P(M_1 \cap M_2) = 0.6375 = P(M_1) \times P(M_2)$$

$$\boxed{\text{YES, events M₁ and M₂ are independent}}$$

**Alternative verification using conditional probability:**
$$P(M_2|M_1) = \frac{P(M_1 \cap M_2)}{P(M_1)} = \frac{0.6375}{0.85} = 0.75 = P(M_2) \checkmark$$

This confirms that knowing Method 1 detected the fault doesn't change the probability that Method 2 detects it.

---

##### Final Answers Summary

| Question | Result |
|----------|--------|
| **1. P(at least one detects)** | **0.9625 or 96.25%** |
| **2. P(both detect)** | **0.6375 or 63.75%** |
| **3. P(both \| at least one)** | **0.6623 or 66.23%** |
| **4. Independence** | **YES - events are independent** because P(M₁∩M₂) = P(M₁)×P(M₂) |

### Answer

**1. P(at least one detects) = 0.9625 or 96.25%
2. P(both detect) = 0.6375 or 63.75%
3. P(both | at least one) = 0.6623 or 66.23%
4. Yes, the events are independent because P(M₁∩M₂) = 0.6375 = P(M₁)×P(M₂) = 0.85 × 0.75.**

---

## 22. Electronic control units in automotive applications are...

### Question

Electronic control units in automotive applications are found to have lifetimes that follow a Weibull distribution with a shape parameter (β) of 2.5 and a characteristic life (η) of 150,000 hours. 

(a) Calculate the expected cumulative percent failure at 50,000 hours of operation.

(b) If a manufacturer wants to offer a warranty period during which no more than 1% of units are expected to fail, what should be the maximum warranty period in hours?

### Reasoning

#### Solution: Weibull Distribution Analysis for Electronic Control Units

##### Given Information
- Shape parameter: β = 2.5
- Characteristic life: η = 150,000 hours

---

##### Part (a): Cumulative Percent Failure at 50,000 Hours

###### Step 1: Apply Weibull CDF Formula

The cumulative distribution function for Weibull:
$$F(t) = 1 - e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$

###### Step 2: Calculate t/η Ratio
$$\frac{t}{\eta} = \frac{50,000}{150,000} = \frac{1}{3} = 0.3333$$

###### Step 3: Raise to Power β
$$\left(\frac{t}{\eta}\right)^{\beta} = (0.3333)^{2.5}$$

$$= (0.3333)^{2.5} = (0.3333)^2 \times (0.3333)^{0.5}$$

$$= 0.1111 \times 0.5774 = 0.06415$$

###### Step 4: Calculate Exponential Term
$$e^{-0.06415} = 0.93788$$

###### Step 5: Calculate F(t)
$$F(50,000) = 1 - 0.93788 = 0.06212$$

###### Step 6: Convert to Percentage
$$\text{Cumulative Percent Failure} = 0.06212 \times 100\% = 6.21\%$$

**Answer for Part (a)**: At 50,000 hours, approximately **6.21%** of units are expected to have failed.

---

##### Part (b): Warranty Period for 1% Failure Rate

###### Step 1: Set Up Equation

We want to find time $t_w$ such that $F(t_w) = 0.01$

$$0.01 = 1 - e^{-\left(\frac{t_w}{\eta}\right)^{\beta}}$$

###### Step 2: Solve for the Exponential Term
$$e^{-\left(\frac{t_w}{\eta}\right)^{\beta}} = 1 - 0.01 = 0.99$$

###### Step 3: Take Natural Logarithm
$$-\left(\frac{t_w}{\eta}\right)^{\beta} = \ln(0.99)$$

$$-\left(\frac{t_w}{\eta}\right)^{\beta} = -0.010050$$

$$\left(\frac{t_w}{\eta}\right)^{\beta} = 0.010050$$

###### Step 4: Solve for t_w/η
$$\frac{t_w}{\eta} = (0.010050)^{1/\beta}$$

$$\frac{t_w}{\eta} = (0.010050)^{1/2.5}$$

$$\frac{t_w}{\eta} = (0.010050)^{0.4}$$

To calculate $(0.010050)^{0.4}$:
$$\ln(0.010050) = -4.6007$$
$$0.4 \times (-4.6007) = -1.8403$$
$$e^{-1.8403} = 0.1586$$

###### Step 5: Calculate Warranty Time
$$t_w = \eta \times 0.1586$$

$$t_w = 150,000 \times 0.1586$$

$$t_w = 23,790 \text{ hours}$$

###### Step 6: Verification
Let's verify: $F(23,790) = 1 - e^{-(23,790/150,000)^{2.5}}$

$$\frac{23,790}{150,000} = 0.1586$$

$$(0.1586)^{2.5} = 0.010050$$ ✓

$$F(23,790) = 1 - e^{-0.010050} = 1 - 0.99 = 0.01$$ ✓

**Answer for Part (b)**: The maximum warranty period should be approximately **23,790 hours** (or about 24,000 hours when rounded).

---

##### Notes on the Shape Parameter

With β = 2.5 (greater than 1), this indicates an **increasing failure rate**, characteristic of wear-out failures. This is typical for electronic components that degrade over time. The failure rate accelerates as components age, which is why the 1% failure threshold occurs relatively early compared to the characteristic life.

### Answer

**(a) Expected cumulative percent failure at 50,000 hours: **6.21%**

(b) Maximum warranty period for 1% failure rate: **23,790 hours** (approximately 24,000 hours)**

---

## 23. A data center has backup generators that activate...

### Question

A data center has backup generators that activate automatically when power failures occur. Power failures follow a Poisson process with a rate of 0.5 failures per month. Each generator activation lasts for 15 minutes on average. 

(a) What is the probability that exactly 2 power failures occur in a 3-month period?

(b) What is the variance of the number of power failures in a 6-month period?

(c) Given that no power failures have occurred in the first month, what is the probability that the first failure occurs after month 2 (i.e., more than 2 months from the start)?

### Reasoning

#### Solution: Poisson Process for Data Center Power Failures

##### Given Information
- Power failures follow a Poisson process
- Rate λ = 0.5 failures per month
- Each activation lasts 15 minutes (contextual information)

---

##### Part (a): Probability of Exactly 2 Failures in 3 Months

###### Formula
For a Poisson process with rate λ, the number of events N(t) in time interval t follows a Poisson distribution:
$$P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$$

###### Calculation
- Time interval: t = 3 months
- Rate: λ = 0.5 per month
- Expected number of events: λt = 0.5 × 3 = 1.5
- We want: k = 2

$$P(N(3) = 2) = \frac{(1.5)^2 e^{-1.5}}{2!}$$

$$P(N(3) = 2) = \frac{2.25 \times e^{-1.5}}{2}$$

$$P(N(3) = 2) = \frac{2.25 \times 0.2231}{2}$$

$$P(N(3) = 2) = \frac{0.5020}{2} = 0.2510$$

###### Answer for Part (a)
$$\boxed{P(\text{exactly 2 failures in 3 months}) \approx 0.251 \text{ or } 25.1\%}$$

---

##### Part (b): Variance of Number of Failures in 6 Months

###### Formula
For a Poisson distribution, a key property is that the variance equals the mean:
$$\text{Var}[N(t)] = E[N(t)] = \lambda t$$

###### Calculation
- Time interval: t = 6 months
- Rate: λ = 0.5 per month

$$\text{Var}[N(6)] = \lambda t = 0.5 \times 6 = 3$$

###### Answer for Part (b)
$$\boxed{\text{Variance} = 3 \text{ failures}^2}$$

---

##### Part (c): Probability First Failure Occurs After Month 2, Given No Failures in Month 1

###### Key Concept: Memoryless Property
The Poisson process has the memoryless property. Given that no failures have occurred in the first month, the process "restarts" - the time until the first failure from that point is still exponentially distributed with rate λ.

###### Approach
Given no failures in month 1, we need the probability that the first failure occurs more than 1 additional month later (which would be after month 2 total).

The time T until the first event in a Poisson process follows an exponential distribution with rate λ:
$$P(T > t) = e^{-\lambda t}$$

By the memoryless property, given survival past month 1:
$$P(T > 2 \mid T > 1) = P(T > 1) = e^{-\lambda \times 1}$$

###### Calculation
- λ = 0.5 per month
- t = 1 month (additional time from end of month 1 to end of month 2)

$$P(\text{first failure after month 2} \mid \text{no failures in month 1}) = e^{-0.5 \times 1}$$

$$P = e^{-0.5} \approx 0.6065$$

###### Answer for Part (c)
$$\boxed{P(\text{first failure after month 2} \mid \text{no failures in month 1}) = e^{-0.5} \approx 0.607 \text{ or } 60.7\%}$$

---

##### Summary of Final Answers

| Question | Answer |
|----------|--------|
| P(exactly 2 failures in 3 months) | **0.251** |
| Variance in 6 months | **3 failures²** |
| P(first failure after month 2 \| none in month 1) | **e⁻⁰·⁵ ≈ 0.607** |

### Answer

**(a) 0.251, (b) 3, (c) 0.607**

---

## 24. A manufacturing system consists of 5 independent subsystems...

### Question

A manufacturing system consists of 5 independent subsystems connected in series. Each subsystem contains 3 identical components in parallel (so each subsystem is a parallel configuration, and the 5 subsystems are in series). Each individual component has a reliability described by the exponential distribution with MTTF = 2000 hours.

(a) What is the reliability of a single subsystem at t = 500 hours?

(b) What is the reliability of the entire manufacturing system at t = 500 hours?

(c) What is the MTTF of a single subsystem?

### Reasoning

#### Solution: Series-Parallel System Reliability Problem

##### Problem Setup

The system has a series-parallel configuration:
- 5 subsystems in series
- Each subsystem has 3 identical components in parallel
- Each component: exponential distribution with MTTF = 2000 hours

---

##### Step 1: Determine Component Parameters

For an exponential distribution:
$$\text{MTTF} = \frac{1}{\lambda}$$

**For each component:**
$$\lambda = \frac{1}{2000} \text{ per hour}$$

**Component reliability function:**
$$R_{\text{component}}(t) = e^{-\lambda t} = e^{-t/2000}$$

---

##### Part (a): Reliability of a Single Subsystem at t = 500 hours

###### Step 2: Calculate Component Reliability at t = 500

$$R_{\text{component}}(500) = e^{-500/2000} = e^{-1/4} = e^{-0.25}$$

$$R_{\text{component}}(500) = 0.7788$$

###### Step 3: Calculate Subsystem Reliability (Parallel Configuration)

For a parallel system of n identical components, the system fails only if **all components fail**.

The unreliability (probability of failure) of the parallel subsystem:
$$F_{\text{subsystem}}(t) = \prod_{i=1}^{n} F_{\text{component}}(t) = [F_{\text{component}}(t)]^n$$

Where $F_{\text{component}}(t) = 1 - R_{\text{component}}(t)$

**Component unreliability at t = 500:**
$$F_{\text{component}}(500) = 1 - 0.7788 = 0.2212$$

**Subsystem unreliability (3 components in parallel):**
$$F_{\text{subsystem}}(500) = (0.2212)^3 = 0.01082$$

**Subsystem reliability:**
$$R_{\text{subsystem}}(500) = 1 - F_{\text{subsystem}}(500) = 1 - 0.01082 = 0.9892$$

###### Answer for Part (a)
$$\boxed{R_{\text{subsystem}}(500) = 1 - (1-e^{-0.25})^3 \approx 0.989}$$

---

##### Part (b): Reliability of the Entire System at t = 500 hours

###### Step 4: Calculate System Reliability (Series Configuration)

For a series system of 5 identical subsystems, **all subsystems must survive** for the system to survive.

$$R_{\text{system}}(t) = [R_{\text{subsystem}}(t)]^5$$

**At t = 500 hours:**
$$R_{\text{system}}(500) = (0.9892)^5$$

$$R_{\text{system}}(500) = 0.9473$$

###### Answer for Part (b)
$$\boxed{R_{\text{system}}(500) \approx 0.947 \text{ or } 94.7\%}$$

---

##### Part (c): MTTF of a Single Subsystem

###### Step 5: Calculate Subsystem MTTF

For a parallel system of n components with exponential distributions (same λ), the MTTF is:

$$\text{MTTF}_{\text{subsystem}} = \frac{1}{\lambda} \sum_{i=1}^{n} \frac{1}{i}$$

This comes from integrating the reliability function of the parallel system.

**For our subsystem (n = 3, λ = 1/2000):**

$$\text{MTTF}_{\text{subsystem}} = \frac{1}{1/2000} \times \left(\frac{1}{1} + \frac{1}{2} + \frac{1}{3}\right)$$

$$\text{MTTF}_{\text{subsystem}} = 2000 \times \left(1 + 0.5 + 0.3333\right)$$

$$\text{MTTF}_{\text{subsystem}} = 2000 \times 1.8333$$

$$\text{MTTF}_{\text{subsystem}} = 3666.7 \text{ hours}$$

###### Answer for Part (c)
$$\boxed{\text{MTTF}_{\text{subsystem}} = 2000 \times \frac{11}{6} \approx 3667 \text{ hours}}$$

---

##### Summary of Final Answers

| Question | Answer |
|----------|--------|
| (a) Subsystem reliability at 500 hrs | **0.989** |
| (b) System reliability at 500 hrs | **0.947** |
| (c) Subsystem MTTF | **3667 hours** |

### Answer

**(a) 0.989, (b) 0.947, (c) 3667 hours**

---

## 25. A reliability test is conducted on 50 identical electronic...

### Question

A reliability test is conducted on 50 identical electronic modules. The modules are tested until 8 failures occur. The failure times (in hours) of the 8 failed units are: 1240, 1580, 2130, 2890, 3420, 4180, 5240, and 6870 hours. Assuming an exponential failure distribution, estimate the Mean Time Between Failures (MTBF) for this population. What is the reliability at 3000 hours?

### Reasoning

#### Estimating MTBF from Censored Exponential Data

##### Problem Understanding

This is a **time-censored** or **failure-censored** test where:
- 50 modules were tested
- Testing stopped after 8 failures
- The remaining 42 modules had not failed (right-censored data)
- We assume exponential distribution
- We need to find MTBF (θ = 1/λ) and R(3000)

##### Step 1: Calculate Total Test Time

For censored data, the total test time includes:
- Time accumulated by failed units (up to their failure times)
- Time accumulated by surviving units (up to the censoring time)

The censoring time is the last observed failure: t_c = 6870 hours

**Total test time (T_total):**
- 8 failed units contributed: 1240 + 1580 + 2130 + 2890 + 3420 + 4180 + 5240 + 6870 = 27,550 hours
- 42 surviving units each contributed 6870 hours: 42 × 6870 = 288,540 hours

$$T_{total} = 27,550 + 288,540 = 316,090 \text{ hours}$$

##### Step 2: Calculate the Failure Rate (MLE for Exponential)

For exponential distribution with censored data, the Maximum Likelihood Estimator for the failure rate is:

$$\hat{\lambda} = \frac{r}{T_{total}}$$

where r = number of failures = 8

$$\hat{\lambda} = \frac{8}{316,090} = 2.531 \times 10^{-5} \text{ failures per hour}$$

##### Step 3: Calculate MTBF

The Mean Time Between Failures (MTBF) is:

$$\text{MTBF} = \theta = \frac{1}{\lambda}$$

$$\text{MTBF} = \frac{1}{2.531 \times 10^{-5}} = 39,511 \text{ hours}$$

##### Step 4: Calculate Reliability at 3000 Hours

For an exponential distribution, the reliability function is:

$$R(t) = e^{-\lambda t}$$

At t = 3000 hours:

$$R(3000) = e^{-\lambda \times 3000}$$

$$R(3000) = e^{-(2.531 \times 10^{-5}) \times 3000}$$

$$R(3000) = e^{-0.07593}$$

$$R(3000) = 0.9269$$

##### Step 5: Interpretation

- The estimated MTBF is 39,511 hours (about 4.51 years)
- At 3000 hours of operation, approximately 92.69% of modules are expected to still be functioning
- The unreliability at 3000 hours is F(3000) = 1 - 0.9269 = 0.0731 (7.31% failure probability)

##### Final Answer

$$\boxed{\text{MTBF} = 39,511 \text{ hours}}$$

$$\boxed{R(3000) = 0.927 \text{ or } 92.7\%}$$

The estimated Mean Time Between Failures is **39,511 hours**, and the reliability at 3000 hours is **92.7%**.

### Answer

**MTBF = 39,511 hours; R(3000) = 0.927 (or 92.7%)**

---

## 26. A semiconductor device has a lognormal failure distribution...

### Question

A semiconductor device has a lognormal failure distribution with a median life (t₅₀) of 85,000 hours and a shape parameter σ = 0.45. A manufacturer wants to offer a warranty period such that no more than 2% of devices fail during the warranty period. What should be the maximum warranty period in hours?

### Reasoning

#### Finding Warranty Period for Lognormal Distribution

##### Problem Understanding

We need to find the warranty time t_w such that:
- The failure distribution is lognormal with median t₅₀ = 85,000 hours
- Shape parameter σ = 0.45
- Maximum 2% of devices fail during warranty (F(t_w) = 0.02)

##### Step 1: Review Lognormal Distribution Properties

For a lognormal distribution:
- The median life t₅₀ corresponds to the 50th percentile
- The CDF at any time t is related to the standard normal distribution
- The relationship is: $$F(t) = \Phi\left(\frac{\ln(t) - \ln(t_{50})}{\sigma}\right)$$

where Φ is the standard normal cumulative distribution function.

##### Step 2: Set Up the Equation

We want F(t_w) = 0.02, so:

$$0.02 = \Phi\left(\frac{\ln(t_w) - \ln(85000)}{\sigma}\right)$$

##### Step 3: Find the Z-Score for CDF = 0.02

From standard normal tables, the z-value corresponding to a cumulative probability of 0.02 is:

$$z_{0.02} = -2.0537$$

(This is the 2nd percentile of the standard normal distribution)

##### Step 4: Solve for the Warranty Period

Using the relationship:
$$\frac{\ln(t_w) - \ln(85000)}{0.45} = -2.0537$$

Multiply both sides by 0.45:
$$\ln(t_w) - \ln(85000) = -2.0537 \times 0.45$$

$$\ln(t_w) - \ln(85000) = -0.9242$$

$$\ln(t_w) = \ln(85000) - 0.9242$$

$$\ln(t_w) = 11.3509 - 0.9242 = 10.4267$$

##### Step 5: Calculate t_w

$$t_w = e^{10.4267}$$

$$t_w = 33,658 \text{ hours}$$

##### Step 6: Verification

Let's verify:
$$F(33658) = \Phi\left(\frac{\ln(33658) - \ln(85000)}{0.45}\right)$$

$$F(33658) = \Phi\left(\frac{10.4247 - 11.3509}{0.45}\right)$$

$$F(33658) = \Phi\left(\frac{-0.9262}{0.45}\right) = \Phi(-2.058) \approx 0.02$$ ✓

##### Final Answer

$$\boxed{t_w \approx 33,700 \text{ hours}}$$

The maximum warranty period should be approximately **33,700 hours** (or about 3.85 years) to ensure that no more than 2% of devices fail during the warranty period.

### Answer

**33,700 hours (or 3.85 years)**

---

## 27. A sensor system processes incoming signals where the output...

### Question

A sensor system processes incoming signals where the output voltage Y (in volts) is related to the input current X (in milliamps) by the transformation Y = -0.5X + 15. The input current X follows a normal distribution with mean 12 mA and standard deviation 3 mA.

(a) Determine the mean and standard deviation of the output voltage Y.
(b) Calculate the probability that the output voltage falls below 7 volts.
(c) Quality control requires that the output voltage be between 8 and 10 volts. What is the probability that a randomly selected signal meets this specification?
(d) If 5 independent signals are processed, what is the probability that their average output voltage is less than 8.5 volts?

### Reasoning

#### Solution: Linear Transformation of Normal Random Variables for Sensor System

##### Given Information
- Input current X ~ N(μ_X = 12, σ_X = 3) in milliamps
- Output voltage transformation: Y = -0.5X + 15 in volts

##### Part (a): Mean and Standard Deviation of Y

###### Step 1: Calculate the Mean of Y

For a linear transformation Y = aX + b:
$$E[Y] = aE[X] + b$$

Applying this:
$$\mu_Y = E[Y] = -0.5(12) + 15 = -6 + 15 = 9$$

$$\boxed{\mu_Y = 9 \text{ volts}}$$

###### Step 2: Calculate the Standard Deviation of Y

For variance under linear transformation:
$$Var(Y) = a^2 \cdot Var(X)$$

Note: The sign of 'a' doesn't affect variance.

$$\sigma_Y^2 = (-0.5)^2 \cdot (3)^2 = 0.25 \cdot 9 = 2.25$$

$$\sigma_Y = \sqrt{2.25} = 1.5$$

$$\boxed{\sigma_Y = 1.5 \text{ volts}}$$

**Summary:** Y ~ N(μ_Y = 9, σ_Y = 1.5)

##### Part (b): Probability that Y < 7

###### Standardize using Z-transformation

$$Z = \frac{Y - \mu_Y}{\sigma_Y}$$

For Y = 7:
$$Z = \frac{7 - 9}{1.5} = \frac{-2}{1.5} = -1.333$$

###### Calculate probability

$$P(Y < 7) = P(Z < -1.333) = \Phi(-1.333)$$

Using standard normal tables:
$$\Phi(-1.333) = 1 - \Phi(1.333) = 1 - 0.9088 = 0.0912$$

$$\boxed{P(Y < 7) = 0.0912 \text{ or } 9.12\%}$$

##### Part (c): Probability that 8 < Y < 10

###### Standardize both bounds

**For Y = 8:**
$$Z_1 = \frac{8 - 9}{1.5} = \frac{-1}{1.5} = -0.667$$

**For Y = 10:**
$$Z_2 = \frac{10 - 9}{1.5} = \frac{1}{1.5} = 0.667$$

###### Calculate probability

$$P(8 < Y < 10) = P(-0.667 < Z < 0.667)$$

$$= \Phi(0.667) - \Phi(-0.667)$$

$$= \Phi(0.667) - [1 - \Phi(0.667)]$$

$$= 2\Phi(0.667) - 1$$

Using standard normal tables:
$$\Phi(0.667) \approx 0.7475$$

$$P(8 < Y < 10) = 2(0.7475) - 1 = 1.4950 - 1 = 0.4950$$

$$\boxed{P(8 < Y < 10) = 0.4950 \text{ or } 49.50\%}$$

##### Part (d): Probability that Average of 5 Signals < 8.5 volts

###### Step 1: Distribution of Sample Mean

For n = 5 independent observations, the sample mean follows:
$$\bar{Y} \sim N\left(\mu_{\bar{Y}} = \mu_Y, \sigma_{\bar{Y}} = \frac{\sigma_Y}{\sqrt{n}}\right)$$

###### Step 2: Calculate Standard Error

$$\sigma_{\bar{Y}} = \frac{1.5}{\sqrt{5}} = \frac{1.5}{2.236} = 0.6708$$

###### Step 3: Standardize

$$Z = \frac{8.5 - 9}{1.5/\sqrt{5}} = \frac{-0.5}{0.6708} = -0.7454$$

###### Step 4: Calculate Probability

$$P(\bar{Y} < 8.5) = P(Z < -0.7454) = \Phi(-0.7454)$$

$$= 1 - \Phi(0.7454) = 1 - 0.7720 = 0.2280$$

$$\boxed{P(\bar{Y}_5 < 8.5) = 0.2280 \text{ or } 22.80\%}$$

---

##### Final Summary

| Question | Answer |
|----------|--------|
| **(a) Mean of Y** | **9 volts** |
| **(a) Std Dev of Y** | **1.5 volts** |
| **(b) P(Y < 7)** | **0.0912 (9.12%)** |
| **(c) P(8 < Y < 10)** | **0.4950 (49.50%)** |
| **(d) P(Ȳ₅ < 8.5)** | **0.2280 (22.80%)** |

### Answer

**(a) Mean of Y: **9 volts**; Standard deviation of Y: **1.5 volts**

(b) P(Y < 7) = **0.0912 or 9.12%**

(c) P(8 < Y < 10) = **0.4950 or 49.50%**

(d) P(Ȳ₅ < 8.5) = **0.2280 or 22.80%****

---

## 28. A component follows a lognormal distribution for its...

### Question

A component follows a lognormal distribution for its time-to-failure. Reliability testing shows that 10% of components fail by 500 hours and 30% fail by 1,200 hours. Determine the parameters μ and σ of the underlying normal distribution, and calculate the B₁₀ life (time by which 10% fail) to verify your results.

### Reasoning

#### Lognormal Distribution: Finding Parameters from Failure Data

##### Problem Understanding

For a lognormal distribution, if T is the time-to-failure, then ln(T) follows a normal distribution with parameters μ and σ.

The CDF of the lognormal distribution is:
$$F(t) = \Phi\left(\frac{\ln(t) - \mu}{\sigma}\right)$$

where Φ is the standard normal CDF.

**Given information:**
- F(500) = 0.10 (10% fail by 500 hours)
- F(1200) = 0.30 (30% fail by 1200 hours)
- Need to find: μ and σ

##### Step 1: Set Up Equations

For t₁ = 500 hours:
$$\Phi\left(\frac{\ln(500) - \mu}{\sigma}\right) = 0.10$$

For t₂ = 1200 hours:
$$\Phi\left(\frac{\ln(1200) - \mu}{\sigma}\right) = 0.30$$

##### Step 2: Use Standard Normal Inverse

From standard normal tables:
- Φ⁻¹(0.10) = -1.282 (10th percentile)
- Φ⁻¹(0.30) = -0.524 (30th percentile)

This gives us:
$$\frac{\ln(500) - \mu}{\sigma} = -1.282 \quad \text{...(1)}$$

$$\frac{\ln(1200) - \mu}{\sigma} = -0.524 \quad \text{...(2)}$$

##### Step 3: Calculate Natural Logarithms

$$\ln(500) = 6.2146$$
$$\ln(1200) = 7.0901$$

Substituting:
$$\frac{6.2146 - \mu}{\sigma} = -1.282 \quad \text{...(1)}$$

$$\frac{7.0901 - \mu}{\sigma} = -0.524 \quad \text{...(2)}$$

##### Step 4: Solve the System of Equations

From equation (1):
$$6.2146 - \mu = -1.282\sigma$$
$$\mu = 6.2146 + 1.282\sigma \quad \text{...(3)}$$

Substitute (3) into equation (2):
$$\frac{7.0901 - (6.2146 + 1.282\sigma)}{\sigma} = -0.524$$

$$\frac{0.8755 - 1.282\sigma}{\sigma} = -0.524$$

$$0.8755 - 1.282\sigma = -0.524\sigma$$

$$0.8755 = 1.282\sigma - 0.524\sigma$$

$$0.8755 = 0.758\sigma$$

$$\sigma = \frac{0.8755}{0.758} = 1.155$$

##### Step 5: Calculate μ

From equation (3):
$$\mu = 6.2146 + 1.282 \times 1.155$$

$$\mu = 6.2146 + 1.481$$

$$\mu = 7.696$$

##### Step 6: Verification - Calculate B₁₀

The B₁₀ life is the time at which F(t) = 0.10, which should equal 500 hours.

$$t_{B10} = e^{\mu + \sigma \cdot \Phi^{-1}(0.10)}$$

$$t_{B10} = e^{7.696 + 1.155 \times (-1.282)}$$

$$t_{B10} = e^{7.696 - 1.481}$$

$$t_{B10} = e^{6.215}$$

$$t_{B10} = 499.8 \approx 500 \text{ hours} \checkmark$$

##### Step 7: Additional Verification at 30% failure

$$t_{30\%} = e^{\mu + \sigma \cdot \Phi^{-1}(0.30)}$$

$$t_{30\%} = e^{7.696 + 1.155 \times (-0.524)}$$

$$t_{30\%} = e^{7.696 - 0.605}$$

$$t_{30\%} = e^{7.091}$$

$$t_{30\%} = 1199.5 \approx 1200 \text{ hours} \checkmark$$

---

##### Final Answer

$$\boxed{\mu = 7.70, \quad \sigma = 1.16}$$

**Verification:** B₁₀ = 500 hours ✓

**Interpretation:** The underlying normal distribution of ln(T) has a mean of 7.70 and standard deviation of 1.16. The relatively large σ value indicates high variability in component lifetimes.

### Answer

**μ = 7.70, σ = 1.16, B₁₀ = 500 hours**

---

## 29. A reliability test plan requires testing n units to failure...

### Question

A reliability test plan requires testing n units to failure with zero failures allowed (c = 0 acceptance number) to demonstrate a reliability of R = 0.95 at 1,000 hours with 90% confidence. Assuming an exponential failure distribution:
(a) Determine the minimum sample size n required.
(b) If the test is conducted and all n units survive 1,000 hours, what is the demonstrated MTTF (Mean Time To Failure) at 90% confidence?
(c) What would be the demonstrated reliability at 500 hours with the same confidence level?

### Reasoning

#### Zero-Failure Reliability Demonstration Test

##### Problem Understanding

**Given:**
- Acceptance number: c = 0 (zero failures allowed)
- Required reliability: R = 0.95 at t = 1,000 hours
- Confidence level: CL = 90% (or 0.90)
- Distribution: Exponential

**Need to find:**
(a) Minimum sample size n
(b) Demonstrated MTTF at 90% confidence
(c) Demonstrated reliability at 500 hours

##### Theoretical Framework

For an exponential distribution:
$$R(t) = e^{-\lambda t} = e^{-t/\theta}$$

where θ = MTTF (Mean Time To Failure) and λ = 1/θ (failure rate)

For a zero-failure test, the confidence level that the true reliability is at least R₀ is:
$$CL = 1 - [R_0]^n$$

##### Part (a): Finding Minimum Sample Size

**Step 1: Set up the equation**

We need:
$$0.90 = 1 - (0.95)^n$$

**Step 2: Solve for n**

$$(0.95)^n = 1 - 0.90 = 0.10$$

Taking natural logarithm:
$$n \cdot \ln(0.95) = \ln(0.10)$$

$$n = \frac{\ln(0.10)}{\ln(0.95)}$$

**Step 3: Calculate**

$$\ln(0.10) = -2.3026$$
$$\ln(0.95) = -0.05129$$

$$n = \frac{-2.3026}{-0.05129} = 44.89$$

Since n must be an integer:
$$\boxed{n = 45 \text{ units}}$$

**Verification:**
$$(0.95)^{45} = 0.0994 \approx 0.10$$
$$CL = 1 - 0.0994 = 0.9006 \approx 90\% \checkmark$$

##### Part (b): Demonstrated MTTF

**Step 1: Relationship between R and MTTF**

At t = 1,000 hours with R = 0.95:
$$0.95 = e^{-1000/\theta}$$

**Step 2: Solve for θ**

Taking natural logarithm:
$$\ln(0.95) = -\frac{1000}{\theta}$$

$$-0.05129 = -\frac{1000}{\theta}$$

$$\theta = \frac{1000}{0.05129}$$

$$\theta = 19,497 \text{ hours}$$

**Step 3: Apply confidence adjustment**

For zero-failure testing with exponential distribution, the lower confidence bound on MTTF is:
$$\theta_{lower} = \frac{2T}{\chi^2_{2r+2, 1-CL}}$$

where T = total test time = n × t = 45 × 1,000 = 45,000 hours
and r = number of failures = 0

For 90% confidence (α = 0.10):
$$\chi^2_{2, 0.10} = 4.605$$

$$\theta_{demonstrated} = \frac{2 \times 45,000}{4.605} = \frac{90,000}{4.605}$$

$$\boxed{\theta_{demonstrated} = 19,544 \text{ hours}}$$

Note: This is consistent with our required reliability demonstration.

##### Part (c): Demonstrated Reliability at 500 hours

**Step 1: Use the demonstrated MTTF**

$$R(500) = e^{-500/\theta_{demonstrated}}$$

$$R(500) = e^{-500/19,544}$$

$$R(500) = e^{-0.02558}$$

$$R(500) = 0.9748$$

**Alternative approach using the scaling property:**

Since reliability follows:
$$R(t) = e^{-t/\theta}$$

And we know R(1000) = 0.95, we can use:
$$R(500) = e^{-500/\theta} = [e^{-1000/\theta}]^{0.5} = [R(1000)]^{0.5}$$

$$R(500) = (0.95)^{0.5} = 0.9747$$

$$\boxed{R(500) = 0.975 \text{ or } 97.5\%}$$

---

##### Final Answers

| Part | Quantity | Value |
|------|----------|-------|
| **(a)** | **Minimum sample size** | **n = 45 units** |
| **(b)** | **Demonstrated MTTF** | **θ = 19,544 hours** |
| **(c)** | **Reliability at 500 hours** | **R(500) = 97.5%** |

**Interpretation:** To demonstrate 95% reliability at 1,000 hours with 90% confidence using a zero-failure test, we need 45 units. If all survive, this demonstrates an MTTF of approximately 19,544 hours, which yields 97.5% reliability at the shorter mission time of 500 hours.

### Answer

**(a) n = 45 units; (b) MTTF = 19,544 hours; (c) R(500 hours) = 97.5%**

---

## 30. A satellite system consists of 3 redundant power modules...

### Question

A satellite system consists of 3 redundant power modules configured in a 2-out-of-3 system (the system works if at least 2 out of 3 modules are functioning). Each power module has an identical reliability of R = 0.92 for a 5-year mission. 
(a) What is the overall system reliability for the 5-year mission?
(b) If the design is changed to require all 3 modules working (series configuration), what would each module's reliability need to be to achieve the same system reliability as in part (a)?

### Reasoning

#### Reliability Analysis for k-out-of-n System

##### Problem Understanding

We have a 2-out-of-3 system where success requires at least 2 of 3 modules working.
- Individual module reliability: R = 0.92
- Mission duration: 5 years
- Configuration: 2-out-of-3 (k-out-of-n where k=2, n=3)

---

##### Part (a): System Reliability for 2-out-of-3 Configuration

###### Step 1: Identify Success Scenarios

The system succeeds if:
- Exactly 2 modules work (and 1 fails), OR
- All 3 modules work

###### Step 2: Apply Binomial Probability Formula

For a k-out-of-n system with identical component reliability R:

$$R_{system} = \sum_{i=k}^{n} \binom{n}{i} R^i (1-R)^{n-i}$$

For our 2-out-of-3 system:

$$R_{system} = \binom{3}{2} R^2 (1-R)^1 + \binom{3}{3} R^3 (1-R)^0$$

###### Step 3: Calculate Binomial Coefficients

$$\binom{3}{2} = \frac{3!}{2!1!} = 3$$

$$\binom{3}{3} = \frac{3!}{3!0!} = 1$$

###### Step 4: Substitute Values

With R = 0.92 and (1-R) = 0.08:

$$R_{system} = 3 \times (0.92)^2 \times (0.08) + 1 \times (0.92)^3 \times 1$$

###### Step 5: Calculate Each Term

**Term 1 (exactly 2 work):**
$$3 \times 0.8464 \times 0.08 = 3 \times 0.067712 = 0.203136$$

**Term 2 (all 3 work):**
$$1 \times 0.778688 \times 1 = 0.778688$$

###### Step 6: Sum the Terms

$$R_{system} = 0.203136 + 0.778688 = 0.981824$$

###### Answer (a):
**The system reliability for the 2-out-of-3 configuration is R_system = 0.9818 or 98.18%**

---

##### Part (b): Required Module Reliability for Series System

###### Step 1: Set Up Series System Equation

For a series system with 3 identical components:

$$R_{system} = R_{module}^3$$

We want this to equal the reliability from part (a):

$$R_{module}^3 = 0.981824$$

###### Step 2: Solve for R_module

Taking the cube root:

$$R_{module} = (0.981824)^{1/3}$$

###### Step 3: Calculate Using Logarithms

$$\ln(R_{module}) = \frac{\ln(0.981824)}{3}$$

$$\ln(0.981824) = -0.018355$$

$$\ln(R_{module}) = \frac{-0.018355}{3} = -0.006118$$

$$R_{module} = e^{-0.006118} = 0.99390$$

###### Step 4: Verification

Check: $(0.99390)^3 = ?$

$$3 \times \ln(0.99390) = 3 \times (-0.006118) = -0.018355$$

$$e^{-0.018355} = 0.98182$$ ✓

###### Answer (b):
**Each module would need a reliability of R = 0.9939 or 99.39% to achieve the same system reliability in a series configuration**

---

##### Summary of Final Answers

| Part | Configuration | Answer |
|------|---------------|--------|
| **(a)** | 2-out-of-3 system with R=0.92 | **R_system = 0.9818 (98.18%)** |
| **(b)** | Series (3-out-of-3) equivalent | **R_module = 0.9939 (99.39%)** |

###### Interpretation

This demonstrates the **benefit of redundancy**: 
- With 2-out-of-3 redundancy, modules with 92% reliability achieve 98.18% system reliability
- To achieve the same system reliability with no redundancy (series), each module would need to be 99.39% reliable
- The redundancy allows use of less reliable (and potentially less expensive) components while achieving high system reliability

### Answer

**(a) 0.9818 or 98.18%
(b) 0.9939 or 99.39%**
