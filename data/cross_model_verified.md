# Cross-Model Verified Problems

*7 problems*

## Table of Contents

1. [A software development team is tracking defects in two...](#a-software-development-team-is-tracking-defects-in-two)
2. [A manufacturer is conducting accelerated life testing on a...](#a-manufacturer-is-conducting-accelerated-life-testing-on-a)
3. [A radar system consists of a critical power amplifier...](#a-radar-system-consists-of-a-critical-power-amplifier)
4. [A parallel redundant system consists of 3 independent...](#a-parallel-redundant-system-consists-of-3-independent)
5. [A data center has 5 independent cooling units arranged in a...](#a-data-center-has-5-independent-cooling-units-arranged-in-a)
6. [A quality control inspector is examining a batch of...](#a-quality-control-inspector-is-examining-a-batch-of)
7. [A critical aerospace component follows a Weibull...](#a-critical-aerospace-component-follows-a-weibull)

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
