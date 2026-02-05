# Cross-Model Rejected Problems

*9 problems*

## Table of Contents

1. [A system consists of two parallel subsystems (A and B),...](#a-system-consists-of-two-parallel-subsystems-a-and-b)
2. [A Weibull distribution is used to model the lifetime of a...](#a-weibull-distribution-is-used-to-model-the-lifetime-of-a)
3. [A reliability test is conducted on electronic assemblies...](#a-reliability-test-is-conducted-on-electronic-assemblies)
4. [A component follows a Weibull distribution with a shape...](#a-component-follows-a-weibull-distribution-with-a-shape)
5. [A manufacturer of industrial sensors needs to demonstrate...](#a-manufacturer-of-industrial-sensors-needs-to-demonstrate)
6. [A Weibull distribution is used to model the lifetime of a...](#a-weibull-distribution-is-used-to-model-the-lifetime-of-a)
7. [A reliability test plan requires testing 200 components for...](#a-reliability-test-plan-requires-testing-200-components-for)
8. [A manufacturer of electronic components has determined that...](#a-manufacturer-of-electronic-components-has-determined-that)
9. [A quality control engineer is analyzing failure data from a...](#a-quality-control-engineer-is-analyzing-failure-data-from-a)

---

## 1. A system consists of two parallel subsystems (A and B),...

### Question

A system consists of two parallel subsystems (A and B), where each subsystem contains components in series. Subsystem A has 3 components, each with reliability 0.95, and Subsystem B has 5 components, each with reliability 0.98. The system succeeds if at least one subsystem operates successfully. Calculate:
1. The reliability of each subsystem
2. The overall system reliability
3. If we want to achieve an overall system reliability of at least 0.999, and we can only improve Subsystem A by replacing all its components with identical higher-reliability components, what minimum component reliability is needed for Subsystem A?

### Reasoning

#### Solution: Parallel-Series System Reliability Analysis

##### Problem Setup

- **Subsystem A**: 3 components in series, each R_A = 0.95
- **Subsystem B**: 5 components in series, each R_B = 0.98
- **System Configuration**: Subsystems A and B in parallel
- System succeeds if at least one subsystem works

---

##### Part 1: Calculate Reliability of Each Subsystem

###### Subsystem A (Series Configuration)

For series systems, all components must work:

$$R_A^{sys} = (R_A)^{n_A} = (0.95)^3$$

$$R_A^{sys} = 0.857375$$

$$\boxed{R_A^{sys} = 0.8574}$$

###### Subsystem B (Series Configuration)

$$R_B^{sys} = (R_B)^{n_B} = (0.98)^5$$

$$R_B^{sys} = 0.903921$$

$$\boxed{R_B^{sys} = 0.9039}$$

---

##### Part 2: Calculate Overall System Reliability

For parallel systems, at least one subsystem must work. Using the complement rule:

$$R_{system} = 1 - (1 - R_A^{sys})(1 - R_B^{sys})$$

$$R_{system} = 1 - (1 - 0.8574)(1 - 0.9039)$$

$$R_{system} = 1 - (0.1426)(0.0961)$$

$$R_{system} = 1 - 0.01370$$

$$R_{system} = 0.98630$$

$$\boxed{R_{system} = 0.9863}$$

---

##### Part 3: Required Component Reliability for Subsystem A

We need: $R_{system} \geq 0.999$

Let $R_A^{new}$ be the new component reliability for Subsystem A.

Subsystem B remains unchanged: $R_B^{sys} = 0.9039$

New Subsystem A reliability: $(R_A^{new})^3$

**System reliability equation:**

$$1 - (1 - (R_A^{new})^3)(1 - 0.9039) \geq 0.999$$

$$1 - (1 - (R_A^{new})^3)(0.0961) \geq 0.999$$

$$1 - 0.0961 + 0.0961(R_A^{new})^3 \geq 0.999$$

$$0.9039 + 0.0961(R_A^{new})^3 \geq 0.999$$

$$0.0961(R_A^{new})^3 \geq 0.0951$$

$$(R_A^{new})^3 \geq \frac{0.0951}{0.0961}$$

$$(R_A^{new})^3 \geq 0.9896$$

Taking the cube root:

$$R_A^{new} \geq (0.9896)^{1/3}$$

$$R_A^{new} \geq 0.9965$$

**Verification:**

If $R_A^{new} = 0.9965$:
- New $R_A^{sys} = (0.9965)^3 = 0.9896$
- System reliability = $1 - (1 - 0.9896)(1 - 0.9039) = 1 - (0.0104)(0.0961) = 1 - 0.001 = 0.999$ ✓

$$\boxed{R_A^{new} \geq 0.9965 \text{ (or 99.65%)}}$$

---

##### Summary of Results

| Parameter | Value |
|-----------|-------|
| **Subsystem A Reliability** | **0.8574** |
| **Subsystem B Reliability** | **0.9039** |
| **Overall System Reliability** | **0.9863** |
| **Required Component Reliability for Subsystem A** | **≥ 0.9965** |

This demonstrates how parallel redundancy significantly improves system reliability, and how even with one subsystem providing backup, achieving very high reliability (99.9%) requires excellent component-level performance.

### Answer

**1. Subsystem A reliability = 0.8574; Subsystem B reliability = 0.9039
2. Overall system reliability = 0.9863
3. Each component in Subsystem A must have reliability ≥ 0.9965 (99.65%)**

---

## 2. A Weibull distribution is used to model the lifetime of a...

### Question

A Weibull distribution is used to model the lifetime of a mechanical component with a characteristic life (η) of 25,000 hours and a shape parameter (β) of 2.5. Calculate:
1. The reliability at t = 15,000 hours
2. The mean time to failure (MTTF)
3. The hazard rate at t = 5,000, 15,000, and 25,000 hours
4. At what time will the reliability drop to 0.50?

Note: For Weibull distribution, MTTF = η·Γ(1 + 1/β), where Γ is the gamma function.

### Reasoning

#### Solution: Weibull Distribution Analysis

##### Given Information
- Characteristic life: η = 25,000 hours
- Shape parameter: β = 2.5

##### Key Weibull Formulas

**Reliability Function:**
$$R(t) = e^{-(t/\eta)^\beta}$$

**Probability Density Function:**
$$f(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-(t/\eta)^\beta}$$

**Hazard Rate:**
$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

---

##### Part 1: Reliability at t = 15,000 hours

$$R(15000) = e^{-(15000/25000)^{2.5}}$$

$$R(15000) = e^{-(0.6)^{2.5}}$$

$$R(15000) = e^{-0.4162}$$

$$R(15000) = 0.6596$$

$$\boxed{R(15000) = 0.660}$$

---

##### Part 2: Mean Time to Failure (MTTF)

**Formula:**
$$MTTF = \eta \cdot \Gamma\left(1 + \frac{1}{\beta}\right)$$

With β = 2.5:
$$MTTF = 25000 \cdot \Gamma\left(1 + \frac{1}{2.5}\right)$$

$$MTTF = 25000 \cdot \Gamma(1.4)$$

Using gamma function tables or calculation: Γ(1.4) ≈ 0.8873

$$MTTF = 25000 \times 0.8873$$

$$MTTF = 22,182.5 \text{ hours}$$

$$\boxed{MTTF = 22,183 \text{ hours}}$$

---

##### Part 3: Hazard Rate Calculations

**General formula:**
$$h(t) = \frac{2.5}{25000}\left(\frac{t}{25000}\right)^{1.5} = \frac{2.5}{25000} \times \frac{t^{1.5}}{25000^{1.5}}$$

Simplifying:
$$h(t) = \frac{2.5}{25000^{2.5}} \times t^{1.5}$$

$$h(t) = \frac{2.5}{25000^{2.5}} \times t^{1.5} = \frac{2.5}{3.90625 \times 10^{10}} \times t^{1.5}$$

$$h(t) = 6.4 \times 10^{-11} \times t^{1.5}$$

###### At t = 5,000 hours:

$$h(5000) = \frac{2.5}{25000}\left(\frac{5000}{25000}\right)^{1.5}$$

$$h(5000) = \frac{2.5}{25000}(0.2)^{1.5}$$

$$h(5000) = 0.0001 \times 0.08944$$

$$h(5000) = 8.944 \times 10^{-6} \text{ per hour}$$

$$\boxed{h(5000) = 8.94 \times 10^{-6} \text{ per hour}}$$

###### At t = 15,000 hours:

$$h(15000) = \frac{2.5}{25000}\left(\frac{15000}{25000}\right)^{1.5}$$

$$h(15000) = 0.0001 \times (0.6)^{1.5}$$

$$h(15000) = 0.0001 \times 0.4648$$

$$h(15000) = 4.648 \times 10^{-5} \text{ per hour}$$

$$\boxed{h(15000) = 4.65 \times 10^{-5} \text{ per hour}}$$

###### At t = 25,000 hours:

$$h(25000) = \frac{2.5}{25000}\left(\frac{25000}{25000}\right)^{1.5}$$

$$h(25000) = \frac{2.5}{25000} \times 1$$

$$h(25000) = 1.0 \times 10^{-4} \text{ per hour}$$

$$\boxed{h(25000) = 1.0 \times 10^{-4} \text{ per hour}}$$

---

##### Part 4: Time When Reliability = 0.50

We need to solve for t when R(t) = 0.50:

$$0.50 = e^{-(t/25000)^{2.5}}$$

Taking natural logarithm of both sides:

$$\ln(0.50) = -(t/25000)^{2.5}$$

$$-0.6931 = -(t/25000)^{2.5}$$

$$(t/25000)^{2.5} = 0.6931$$

Taking both sides to the power of (1/2.5):

$$\frac{t}{25000} = (0.6931)^{1/2.5}$$

$$\frac{t}{25000} = (0.6931)^{0.4}$$

$$\frac{t}{25000} = 0.8659$$

$$t = 25000 \times 0.8659$$

$$t = 21,647.5 \text{ hours}$$

$$\boxed{t_{50} = 21,648 \text{ hours}}$$

---

##### Summary of Results

| Parameter | Value |
|-----------|-------|
| **R(15,000 hrs)** | **0.660** |
| **MTTF** | **22,183 hours** |
| **h(5,000 hrs)** | **8.94 × 10⁻⁶ per hour** |
| **h(15,000 hrs)** | **4.65 × 10⁻⁵ per hour** |
| **h(25,000 hrs)** | **1.0 × 10⁻⁴ per hour** |
| **Time at R = 0.50** | **21,648 hours** |

**Note:** The increasing hazard rate (from 8.94×10⁻⁶ to 1.0×10⁻⁴) confirms that β = 2.5 > 1, indicating wear-out failure mode typical of mechanical components.

### Answer

**1. R(15,000) = 0.660
2. MTTF = 22,183 hours
3. h(5,000) = 8.94 × 10⁻⁶ per hour; h(15,000) = 4.65 × 10⁻⁵ per hour; h(25,000) = 1.0 × 10⁻⁴ per hour
4. Reliability drops to 0.50 at t = 21,648 hours**

---

## 3. A reliability test is conducted on electronic assemblies...

### Question

A reliability test is conducted on electronic assemblies with the following specifications:
- Target acceptable failure rate (AQL): λ₀ = 100 FITS at 10,000 operating hours
- Rejectable failure rate (LTPD): λ₁ = 500 FITS at 10,000 operating hours
- Failures follow an exponential distribution (constant failure rate)
- Test duration: t = 500 hours
- No acceleration is used (field conditions, A = 1)
- Producer's risk: α = 0.05
- Consumer's risk: β = 0.10

Determine the appropriate sampling plan (n, c) for this acceptance test.

### Reasoning

###### Problem Summary

- AQL failure rate: λ₀ = 100 FITS
- LTPD failure rate: λ₁ = 500 FITS
- Operating period: T = 10,000 hours
- Test duration: t = 500 hours
- Acceleration factor: A = 1 (no acceleration)
- Distribution: Exponential (constant failure rate)
- Producer's risk: α = 0.05 (P(reject | good) ≤ 0.05)
- Consumer's risk: β = 0.10 (P(accept | bad) ≤ 0.10)

###### Step 1: Convert FITS to Failure Rates

FITS = failures per 10⁹ hours

**AQL failure rate:**
$$\lambda_0 = 100 \times 10^{-9} = 1 \times 10^{-7} \text{ failures/hour}$$

**LTPD failure rate:**
$$\lambda_1 = 500 \times 10^{-9} = 5 \times 10^{-7} \text{ failures/hour}$$

###### Step 2: Calculate Expected Failures per Unit During Test

For an exponential distribution, the probability of failure during test time t is:

$$p = 1 - e^{-\lambda t}$$

For small λt (which applies here), we can approximate:
$$p \approx \lambda t$$

**For AQL:**
$$p_0 = \lambda_0 \times t = 1 \times 10^{-7} \times 500 = 5 \times 10^{-5}$$

**For LTPD:**
$$p_1 = \lambda_1 \times t = 5 \times 10^{-7} \times 500 = 2.5 \times 10^{-4}$$

###### Step 3: Calculate Expected Number of Failures in Sample of Size n

For a sample of size n:

**Under AQL:**
$$\mu_0 = n \times p_0 = n \times 5 \times 10^{-5}$$

**Under LTPD:**
$$\mu_1 = n \times p_1 = n \times 2.5 \times 10^{-4}$$

###### Step 4: Determine Discrimination Ratio

$$R = \frac{\mu_1}{\mu_0} = \frac{p_1}{p_0} = \frac{\lambda_1}{\lambda_0} = \frac{500}{100} = 5.0$$

###### Step 5: Find Sampling Plan Using Standard Tables

For a discrimination ratio R = 5.0 with α = 0.05 and β = 0.10:

From Poisson-based acceptance sampling tables:

For **c = 2**:
- nμ₀ ≈ 0.818 gives P(X ≤ 2) ≈ 0.95
- nμ₁ ≈ 6.296 gives P(X ≤ 2) ≈ 0.10
- Ratio: 6.296/0.818 ≈ 7.7 (too high)

For **c = 5**:
- nμ₀ ≈ 2.613 gives P(X ≤ 5) ≈ 0.95
- nμ₁ ≈ 10.513 gives P(X ≤ 5) ≈ 0.10
- Ratio: 10.513/2.613 ≈ 4.02 (too low)

For **c = 7**:
- nμ₀ ≈ 4.057 gives P(X ≤ 7) ≈ 0.95
- nμ₁ ≈ 13.35 gives P(X ≤ 7) ≈ 0.10
- Ratio: 13.35/4.057 ≈ 3.29 (too low)

For **c = 10**:
- nμ₀ ≈ 6.169 gives P(X ≤ 10) ≈ 0.95
- nμ₁ ≈ 17.82 gives P(X ≤ 10) ≈ 0.10
- Ratio: 17.82/6.169 ≈ 2.89 (too low)

The best match for R = 5.0 is **c = 5** (accepting the slight deviation).

###### Step 6: Calculate Sample Size

Using c = 5 and nμ₀ = 2.613:

$$n = \frac{2.613}{\mu_0/n} = \frac{2.613}{5 \times 10^{-5}} = 52,260$$

###### Step 7: Verify with LTPD

$$n\mu_1 = 52,260 \times 2.5 \times 10^{-4} = 13.065$$

From Poisson tables, P(X ≤ 5 | λ = 13.065) ≈ 0.08, which is close to β = 0.10. ✓

###### Alternative Approach: Use c = 6

For **c = 6**:
- nμ₀ ≈ 3.286 gives P(X ≤ 6) ≈ 0.95
- nμ₁ ≈ 11.84 gives P(X ≤ 6) ≈ 0.10
- Ratio: 11.84/3.286 ≈ 3.60

$$n = \frac{3.286}{5 \times 10^{-5}} = 65,720$$

Verification: n×μ₁ = 65,720 × 2.5 × 10⁻⁴ = 16.43

This gives P(X ≤ 6 | λ = 16.43) ≈ 0.02, which is too conservative.

### Answer

****Sampling Plan: n = 52,000 to 53,000 units, c = 5 failures**

**Recommended: n = 52,500, c = 5**

This means: Test 52,500 units for 500 hours each under field conditions. Accept the lot if 5 or fewer failures occur; reject if 6 or more failures occur.**

---

## 4. A component follows a Weibull distribution with a shape...

### Question

A component follows a Weibull distribution with a shape parameter β = 2.0 and a characteristic life η = 50,000 hours. Calculate:
(a) The reliability R(t) at t = 10,000 hours
(b) The hazard rate h(t) at t = 10,000 hours
(c) The mean time to failure (MTTF)

Note: For a Weibull distribution, MTTF = η·Γ(1 + 1/β), where Γ is the gamma function. For β = 2, Γ(1.5) = √π/2 ≈ 0.8862.

### Reasoning

###### Problem Analysis

This problem involves calculating key reliability metrics for a Weibull distribution with:
- Shape parameter: β = 2.0
- Characteristic life: η = 50,000 hours
- Analysis time: t = 10,000 hours

###### Part (a): Reliability R(t) at t = 10,000 hours

The reliability function for a Weibull distribution is:

$$R(t) = e^{-\left(\frac{t}{\eta}\right)^{\beta}}$$

**Step 1: Calculate the ratio t/η**

$$\frac{t}{\eta} = \frac{10,000}{50,000} = 0.2$$

**Step 2: Raise to the power β**

$$\left(\frac{t}{\eta}\right)^{\beta} = (0.2)^{2.0} = 0.04$$

**Step 3: Calculate R(t)**

$$R(t) = e^{-0.04} = 0.9608$$

**Answer (a):** R(10,000) = 0.9608 or **96.08%**

###### Part (b): Hazard Rate h(t) at t = 10,000 hours

For a Weibull distribution, the hazard rate is:

$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

**Step 1: Calculate (t/η)^(β-1)**

$$\left(\frac{t}{\eta}\right)^{\beta-1} = (0.2)^{2.0-1} = (0.2)^{1.0} = 0.2$$

**Step 2: Calculate h(t)**

$$h(t) = \frac{2.0}{50,000} \times 0.2$$

$$h(t) = \frac{0.4}{50,000} = 8 \times 10^{-6} \text{ failures/hour}$$

**Step 3: Convert to FITS (Failures in 10⁹ hours)**

$$h(t) = 8 \times 10^{-6} \times 10^{9} = 8,000 \text{ FITS}$$

**Answer (b):** h(10,000) = 8 × 10⁻⁶ failures/hour or **8,000 FITS**

###### Part (c): Mean Time to Failure (MTTF)

For a Weibull distribution:

$$\text{MTTF} = \eta \cdot \Gamma\left(1 + \frac{1}{\beta}\right)$$

**Step 1: Calculate the argument of the gamma function**

$$1 + \frac{1}{\beta} = 1 + \frac{1}{2.0} = 1.5$$

**Step 2: Use the given gamma function value**

$$\Gamma(1.5) = 0.8862$$

**Step 3: Calculate MTTF**

$$\text{MTTF} = 50,000 \times 0.8862 = 44,310 \text{ hours}$$

**Answer (c):** MTTF = **44,310 hours**

###### Verification and Interpretation

- **β = 2.0** indicates an increasing hazard rate (wear-out failures), typical of mechanical components
- The hazard rate increases linearly with time for β = 2 (Rayleigh distribution)
- At t = 10,000 hours, the component has 96.08% reliability, which is quite high
- The MTTF (44,310 hours) is less than the characteristic life (50,000 hours), which is expected for β > 1

### Answer

**(a) R(10,000) = 0.9608 or 96.08%
(b) h(10,000) = 8 × 10⁻⁶ failures/hour or 8,000 FITS
(c) MTTF = 44,310 hours**

---

## 5. A manufacturer of industrial sensors needs to demonstrate...

### Question

A manufacturer of industrial sensors needs to demonstrate that their new temperature sensor meets a reliability target of MTTF ≥ 1,500,000 hours. They plan to conduct an accelerated life test at elevated temperature for 5,000 hours per unit. If the test plan allows for up to 3 failures, what sample size is needed to demonstrate this requirement with 80% confidence? If budget constraints limit the sample to 2,000 units, how many failures can be allowed while maintaining 80% confidence?

### Reasoning

#### Reliability Demonstration Test Sample Size and Acceptance Criteria

##### Problem Setup

We have two related questions:
1. Given up to 3 allowed failures, find required sample size for 80% confidence
2. Given 2,000 units, find maximum allowed failures for 80% confidence

**Common parameters:**
- Target MTTF: θ₀ = 1,500,000 hours (equivalently, λ₀ = 1/1,500,000 = 6.667 × 10⁻⁷ failures/hour)
- Test duration per unit: t = 5,000 hours
- Confidence level: 1 - α = 0.80, so α = 0.20

##### Theoretical Foundation

For reliability demonstration testing with exponential distribution, the chi-square relationship is:

$$n = \frac{\chi^2_{1-\alpha, 2(r+1)}}{2 \cdot t \cdot \lambda_0}$$

Where:
- n = sample size (number of units on test)
- t = test time per unit
- λ₀ = target failure rate
- r = number of allowed failures
- χ²₁₋α, 2(r+1) = chi-square value with 2(r+1) degrees of freedom

##### Key Calculation Values

$$t \times \lambda_0 = 5,000 \times \frac{1}{1,500,000} = \frac{5,000}{1,500,000} = \frac{1}{300} = 0.003333$$

$$2 \times t \times \lambda_0 = 0.006667$$

---

##### Part 1: Sample Size for 3 Allowed Failures

**Parameters:**
- Confidence level: 80% (α = 0.20)
- Allowed failures: r = 3
- Degrees of freedom: 2(r + 1) = 2(4) = 8

**Chi-square value:**
χ²₀.₂₀, ₈ = 11.030

**Sample size calculation:**

$$n = \frac{\chi^2_{0.20, 8}}{2 \cdot t \cdot \lambda_0} = \frac{11.030}{0.006667} = 1,654.5$$

**Round up: n = 1,655 units**

---

##### Part 2: Maximum Allowed Failures for 2,000 Units

Given n = 2,000 units, we need to find the maximum r such that:

$$2,000 = \frac{\chi^2_{0.20, 2(r+1)}}{0.006667}$$

Rearranging:
$$\chi^2_{0.20, 2(r+1)} = 2,000 \times 0.006667 = 13.334$$

We need to find r such that χ²₀.₂₀, 2(r+1) ≤ 13.334

**Testing different values of r:**

**For r = 3:** df = 8
χ²₀.₂₀, ₈ = 11.030 < 13.334 ✓ (but we need to check if r = 4 works)

**For r = 4:** df = 10
χ²₀.₂₀, ₁₀ = 12.549 < 13.334 ✓

**For r = 5:** df = 12
χ²₀.₂₀, ₁₂ = 14.011 > 13.334 ❌

Therefore, the maximum allowed failures is r = 4.

**Verification:**
$$n = \frac{12.549}{0.006667} = 1,882.4 < 2,000$$ ✓

This means with 2,000 units and 4 allowed failures, we have:
$$\chi^2_{required} = 2,000 \times 0.006667 = 13.334$$

Since χ²₀.₂₀, ₁₀ = 12.549 < 13.334, the test plan with n = 2,000 and r = 4 provides more than 80% confidence.

---

##### Summary of Results

| Question | Allowed Failures | Chi-Square Value | Sample Size |
|----------|-----------------|------------------|-------------|
| Part 1 | 3 | 11.030 | **1,655** |
| Part 2 | 4 | 12.549 | 2,000 (given) |

---

##### Final Answers

1. **For 3 allowed failures with 80% confidence: n = 1,655 units**
2. **For 2,000 units with 80% confidence: maximum 4 failures allowed**

### Answer

**Part 1: 1,655 units
Part 2: 4 failures maximum**

---

## 6. A Weibull distribution is used to model the lifetime of a...

### Question

A Weibull distribution is used to model the lifetime of a mechanical component. The characteristic life (η) is 25,000 hours and the shape parameter (β) is 2.5. Calculate:
1. The reliability at t = 15,000 hours
2. The MTTF (Mean Time To Failure)
3. The hazard rate h(t) at t = 15,000 hours and t = 30,000 hours
4. Comment on whether this component exhibits infant mortality, random failures, or wear-out behavior.

### Reasoning

#### Weibull Distribution Analysis Solution

##### Given Information
- Characteristic life: η = 25,000 hours
- Shape parameter: β = 2.5

##### Part 1: Calculate Reliability at t = 15,000 hours

**Formula for Weibull Reliability:**
$$R(t) = e^{-(t/\eta)^\beta}$$

**Calculation:**
$$R(15,000) = e^{-(15,000/25,000)^{2.5}}$$

$$R(15,000) = e^{-(0.6)^{2.5}}$$

$$R(15,000) = e^{-0.4415}$$

$$\boxed{R(15,000) = 0.643 = 64.3\%}$$

##### Part 2: Calculate the MTTF

**Formula for Weibull MTTF:**
$$MTTF = \eta \cdot \Gamma\left(1 + \frac{1}{\beta}\right)$$

where Γ is the gamma function.

**Calculation:**
$$MTTF = 25,000 \times \Gamma\left(1 + \frac{1}{2.5}\right)$$

$$MTTF = 25,000 \times \Gamma(1.4)$$

From gamma function tables: Γ(1.4) ≈ 0.8873

$$MTTF = 25,000 \times 0.8873$$

$$\boxed{MTTF = 22,183 \text{ hours}}$$

##### Part 3: Calculate Hazard Rate h(t)

**Formula for Weibull Hazard Rate:**
$$h(t) = \frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}$$

###### At t = 15,000 hours:

$$h(15,000) = \frac{2.5}{25,000}\left(\frac{15,000}{25,000}\right)^{2.5-1}$$

$$h(15,000) = \frac{2.5}{25,000}(0.6)^{1.5}$$

$$h(15,000) = 0.0001 \times 0.4648$$

$$h(15,000) = 4.648 \times 10^{-5} \text{ per hour}$$

$$\boxed{h(15,000) = 46.48 \text{ FITs (failures per billion hours)}}$$

###### At t = 30,000 hours:

$$h(30,000) = \frac{2.5}{25,000}\left(\frac{30,000}{25,000}\right)^{1.5}$$

$$h(30,000) = 0.0001 \times (1.2)^{1.5}$$

$$h(30,000) = 0.0001 \times 1.3148$$

$$h(30,000) = 1.315 \times 10^{-4} \text{ per hour}$$

$$\boxed{h(30,000) = 131.5 \text{ FITs}}$$

##### Part 4: Interpretation of Failure Behavior

**Analysis of Shape Parameter:**

The shape parameter β = 2.5 indicates the failure behavior:
- β < 1: Infant mortality (decreasing failure rate)
- β = 1: Random failures (constant failure rate - exponential distribution)
- β > 1: Wear-out (increasing failure rate)

**Observations:**

1. **β = 2.5 > 1**: This component exhibits **wear-out behavior**

2. **Increasing Hazard Rate**: The hazard rate increases from 46.48 FITs at 15,000 hours to 131.5 FITs at 30,000 hours, confirming wear-out

3. **Hazard Rate Growth Factor**: 
   $$\frac{h(30,000)}{h(15,000)} = \frac{131.5}{46.48} = 2.83$$
   
   The hazard rate has nearly tripled, showing significant aging

4. **Physical Meaning**: This distribution is appropriate for mechanical components subject to fatigue, wear, or degradation mechanisms where failure probability increases with age

$$\boxed{\text{Conclusion: This component exhibits WEAR-OUT behavior with increasing failure rate}}$$

##### Summary of Results

| Parameter | Value |
|-----------|-------|
| **R(15,000 hrs)** | **64.3%** |
| **MTTF** | **22,183 hours** |
| **h(15,000 hrs)** | **4.648 × 10⁻⁵ per hour (46.48 FITs)** |
| **h(30,000 hrs)** | **1.315 × 10⁻⁴ per hour (131.5 FITs)** |
| **Failure Behavior** | **Wear-out (β = 2.5 > 1)** |

### Answer

**R(15,000) = 64.3%, MTTF = 22,183 hours, h(15,000) = 46.48 FITs, h(30,000) = 131.5 FITs. The component exhibits **wear-out behavior** because β = 2.5 > 1, resulting in an increasing hazard rate over time.**

---

## 7. A reliability test plan requires testing 200 components for...

### Question

A reliability test plan requires testing 200 components for 1000 hours each (total test time = 200,000 device-hours). The acceptance criterion is that no more than 3 failures are allowed during the test. Assume failures follow an exponential distribution with constant failure rate λ.

1. What is the maximum acceptable failure rate (in FITs) that would pass this test with 90% confidence (α = 0.10)?
2. If the true failure rate is 10 FITs, what is the probability of passing this test?
3. If exactly 3 failures occurred during the test, calculate the point estimate and the upper 90% confidence bound for the failure rate.

### Reasoning

#### Reliability Test Plan Analysis Solution

##### Given Information
- Number of components: n = 200
- Test duration per component: t = 1000 hours
- Total test time: T = 200,000 device-hours
- Maximum allowed failures: c = 3
- Exponential distribution (constant failure rate λ)

##### Part 1: Maximum Acceptable Failure Rate (90% Confidence)

We need to find the failure rate λ such that there's a 90% probability of observing ≤ 3 failures.

**For exponential distribution with total test time T:**
The expected number of failures: μ = λT

Using Poisson approximation (appropriate for rare events):
$$P(X \leq 3) = \sum_{x=0}^{3} \frac{e^{-\mu}\mu^x}{x!} = 0.90$$

$$P(X \leq 3) = e^{-\mu}\left(1 + \mu + \frac{\mu^2}{2} + \frac{\mu^3}{6}\right) = 0.90$$

**Finding μ using Poisson tables:**
- At μ = 6.0: P(X ≤ 3) = 0.1512
- At μ = 5.0: P(X ≤ 3) = 0.2650
- At μ = 4.0: P(X ≤ 3) = 0.4335
- At μ = 3.5: P(X ≤ 3) = 0.5366
- At μ = 2.5: P(X ≤ 3) = 0.7576
- At μ = 2.0: P(X ≤ 3) = 0.8571
- At μ = 1.8: P(X ≤ 3) = 0.8913
- At μ = 1.9: P(X ≤ 3) = 0.8747

By interpolation between μ = 1.8 and μ = 2.0:
$$\frac{0.90 - 0.8913}{0.8571 - 0.8913} = \frac{\mu - 1.8}{2.0 - 1.8}$$

$$\frac{-0.0087}{-0.0342} = \frac{\mu - 1.8}{0.2}$$

$$\mu \approx 1.85$$

**Calculate failure rate:**
$$\lambda = \frac{\mu}{T} = \frac{1.85}{200,000} = 9.25 \times 10^{-6} \text{ per hour}$$

**Convert to FITs (failures per 10⁹ hours):**
$$\lambda = 9.25 \times 10^{-6} \times 10^9 = 9,250 \text{ FITs}$$

$$\boxed{\text{Maximum acceptable failure rate} = 9,250 \text{ FITs}}$$

##### Part 2: Probability of Passing if True Failure Rate = 10 FITs

**Convert 10 FITs to failures per hour:**
$$\lambda = \frac{10}{10^9} = 10^{-8} \text{ per hour}$$

**Expected failures:**
$$\mu = \lambda T = 10^{-8} \times 200,000 = 2.0 \text{ failures}$$

**Probability of ≤ 3 failures:**
$$P(X \leq 3) = e^{-2.0}\left(1 + 2.0 + \frac{4.0}{2} + \frac{8.0}{6}\right)$$

$$P(X \leq 3) = e^{-2.0}(1 + 2.0 + 2.0 + 1.333)$$

$$P(X \leq 3) = 0.1353 \times 6.333$$

$$P(X \leq 3) = 0.8571$$

$$\boxed{\text{Probability of passing} = 85.71\%}$$

##### Part 3: Point Estimate and 90% Upper Confidence Bound

**Given:** Exactly r = 3 failures observed in T = 200,000 hours

###### Point Estimate:
$$\hat{\lambda} = \frac{r}{T} = \frac{3}{200,000} = 1.5 \times 10^{-5} \text{ per hour}$$

$$\hat{\lambda} = 15,000 \text{ FITs}$$

$$\boxed{\text{Point estimate} = 15,000 \text{ FITs}}$$

###### Upper 90% Confidence Bound:

For exponential distribution, the upper confidence bound uses the chi-square distribution:
$$\lambda_{upper} = \frac{\chi^2_{1-\alpha, 2(r+1)}}{2T}$$

For 90% confidence (α = 0.10) with r = 3 failures:
- Degrees of freedom: 2(r+1) = 2(4) = 8
- χ²₀.₉₀,₈ = 13.362 (from chi-square tables)

**Calculate upper bound:**
$$\lambda_{upper} = \frac{13.362}{2 \times 200,000} = \frac{13.362}{400,000}$$

$$\lambda_{upper} = 3.341 \times 10^{-5} \text{ per hour}$$

$$\lambda_{upper} = 33,410 \text{ FITs}$$

$$\boxed{\text{Upper 90% confidence bound} = 33,410 \text{ FITs}}$$

###### Confidence Statement:
We are 90% confident that the true failure rate is less than 33,410 FITs.

##### Summary of Results

| Parameter | Value |
|-----------|-------|
| **Maximum acceptable λ (90% pass)** | **9,250 FITs** |
| **P(pass) if λ = 10 FITs** | **85.71%** |
| **Point estimate (3 failures)** | **15,000 FITs** |
| **Upper 90% confidence bound** | **33,410 FITs** |

### Answer

**1. Maximum acceptable failure rate = 9,250 FITs (to pass with 90% confidence)
2. Probability of passing if true λ = 10 FITs is 85.71%
3. Point estimate = 15,000 FITs; Upper 90% confidence bound = 33,410 FITs**

---

## 8. A manufacturer of electronic components has determined that...

### Question

A manufacturer of electronic components has determined that the time-to-failure of their devices follows a Weibull distribution with a shape parameter (β) of 2.5. Reliability testing shows that 15% of the units fail by 500 hours. Calculate the characteristic life (η) of these components, and then determine what percentage of units would be expected to fail by 1000 hours.

### Reasoning

#### Finding Characteristic Life and Failure Probability for Weibull Distribution

##### Problem Setup

Given information:
- Shape parameter: β = 2.5
- F(500) = 0.15 (15% fail by 500 hours)
- Need to find: η (characteristic life) and F(1000)

##### Step 1: Recall the Weibull CDF

The cumulative distribution function for a Weibull distribution is:

$$F(t) = 1 - e^{-(t/η)^β}$$

where:
- η = characteristic life (scale parameter)
- β = shape parameter

##### Step 2: Set Up Equation Using Known Point

We know that F(500) = 0.15, so:

$$0.15 = 1 - e^{-(500/η)^{2.5}}$$

##### Step 3: Solve for η

Rearranging:
$$e^{-(500/η)^{2.5}} = 1 - 0.15 = 0.85$$

Taking natural logarithm of both sides:
$$-(500/η)^{2.5} = \ln(0.85)$$

$$-(500/η)^{2.5} = -0.1625$$

$$(500/η)^{2.5} = 0.1625$$

Taking both sides to the power of (1/2.5):
$$\frac{500}{η} = (0.1625)^{1/2.5}$$

$$\frac{500}{η} = (0.1625)^{0.4}$$

Calculate (0.1625)^0.4:
$$\frac{500}{η} = 0.4818$$

Therefore:
$$η = \frac{500}{0.4818} = 1037.8 \text{ hours}$$

##### Step 4: Calculate F(1000)

Now using η = 1037.8 hours, find the probability of failure by 1000 hours:

$$F(1000) = 1 - e^{-(1000/1037.8)^{2.5}}$$

Calculate the exponent:
$$\frac{1000}{1037.8} = 0.9636$$

$$(0.9636)^{2.5} = 0.9118$$

Therefore:
$$F(1000) = 1 - e^{-0.9118}$$

$$F(1000) = 1 - 0.4019$$

$$F(1000) = 0.5981$$

##### Step 5: Verification

Let's verify our η value with the original condition:
$$F(500) = 1 - e^{-(500/1037.8)^{2.5}} = 1 - e^{-(0.4818)^{2.5}}$$
$$= 1 - e^{-0.1625} = 1 - 0.85 = 0.15$$ ✓

##### Final Answer

**Characteristic life: η = 1037.8 hours ≈ 1038 hours**

**Percentage failing by 1000 hours: 59.81% ≈ 60%**

### Answer

**Characteristic life η = 1038 hours; approximately 60% of units would fail by 1000 hours.**

---

## 9. A quality control engineer is analyzing failure data from a...

### Question

A quality control engineer is analyzing failure data from a production line. Out of 80 components tested, only the first 25 failures could be analyzed before the test was terminated. When the times-to-failure for these 25 units are plotted on Weibull probability paper, the plot appears linear with an estimated shape parameter β = 1.8. The best-fit line passes through the point where the cumulative probability equals 20% at a time of 145 hours. Estimate the characteristic life (η) of the entire population. Additionally, what is the median time-to-failure (T₅₀) for this population?

### Reasoning

#### Estimating Weibull Parameters from Suspended Test Data

##### Problem Understanding

We have a **suspended (right-censored) test** where:
- 80 components were tested
- Only the first 25 failures were analyzed (test terminated after 25th failure)
- Shape parameter estimated: β = 1.8
- The fitted line passes through CDF = 20% at t = 145 hours
- Need to find: η (characteristic life) and T₅₀ (median life)

##### Step 1: Understand Weibull Distribution on Probability Paper

For a Weibull distribution, when plotted on Weibull probability paper, the linearized form is:

$$\ln[-\ln(1-F(t))] = β \ln(t) - β \ln(η)$$

Alternatively, we can work directly with the CDF:
$$F(t) = 1 - e^{-(t/η)^β}$$

##### Step 2: Use the Given Data Point

We know that at t = 145 hours, F(t) = 0.20, and β = 1.8.

Substituting into the Weibull CDF:
$$0.20 = 1 - e^{-(145/η)^{1.8}}$$

##### Step 3: Solve for η

Rearranging:
$$e^{-(145/η)^{1.8}} = 1 - 0.20 = 0.80$$

Taking natural logarithm:
$$-(145/η)^{1.8} = \ln(0.80)$$

$$-(145/η)^{1.8} = -0.2231$$

$$(145/η)^{1.8} = 0.2231$$

Taking both sides to the power of (1/1.8):
$$\frac{145}{η} = (0.2231)^{1/1.8}$$

$$\frac{145}{η} = (0.2231)^{0.5556}$$

Calculate (0.2231)^0.5556:
$$\frac{145}{η} = 0.4250$$

Therefore:
$$η = \frac{145}{0.4250} = 341.2 \text{ hours}$$

##### Step 4: Calculate the Median Life T₅₀

The median occurs when F(t) = 0.50:
$$0.50 = 1 - e^{-(T_{50}/η)^β}$$

$$e^{-(T_{50}/η)^β} = 0.50$$

$$-(T_{50}/η)^β = \ln(0.50)$$

$$(T_{50}/η)^β = -\ln(0.50) = \ln(2) = 0.6931$$

$$T_{50}/η = (0.6931)^{1/β}$$

With β = 1.8:
$$T_{50}/341.2 = (0.6931)^{1/1.8}$$

$$T_{50}/341.2 = (0.6931)^{0.5556}$$

$$T_{50}/341.2 = 0.8007$$

$$T_{50} = 0.8007 × 341.2 = 273.2 \text{ hours}$$

##### Step 5: Verification

Verify with the original data point:
$$F(145) = 1 - e^{-(145/341.2)^{1.8}}$$
$$= 1 - e^{-(0.4250)^{1.8}}$$
$$= 1 - e^{-0.2231}$$
$$= 1 - 0.80 = 0.20$$ ✓

Verify the median:
$$F(273.2) = 1 - e^{-(273.2/341.2)^{1.8}}$$
$$= 1 - e^{-(0.8007)^{1.8}}$$
$$= 1 - e^{-0.6931}$$
$$= 1 - 0.50 = 0.50$$ ✓

##### Final Answer

**Characteristic life: η = 341.2 hours ≈ 341 hours**

**Median time-to-failure: T₅₀ = 273.2 hours ≈ 273 hours**

### Answer

**Characteristic life η = 341 hours; Median life T₅₀ = 273 hours.**
