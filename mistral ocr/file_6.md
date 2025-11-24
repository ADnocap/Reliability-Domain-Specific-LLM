# J. W. McPherson 

## Reliability Physics and Engineering

Time-To-Failure Modeling
Third EditionReliability Physics and EngineeringJ. W. McPherson

# Reliability Physics and Engineering 

Time-To-Failure Modeling

Third Edition

SpringerJ. W. McPherson<br>McPherson Reliability Consulting, LLC<br>Plano, TX, USA

ISBN 978-3-319-93682-6
ISBN 978-3-319-93683-3 (eBook)
https://doi.org/10.1007/978-3-319-93683-3
Library of Congress Control Number: 2018955282
(C) Springer Nature Switzerland AG 2013, 2019

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.
The publisher, the authors, and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, express or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Switzerland AG
The registered company address is: Gewerbestrasse 11, 6330 Cham, SwitzerlandThe best idea that I have ever had -marrying my wife Victoria# Preface 

All engineers could benefit from at least one course in Reliability Physics \& Engineering. It is very likely that, starting with your very first engineering position, you will be asked-how long is your newly developed device expected to last? This textbook was designed to help answer this fundamentally important question. All materials and devices are expected to degrade with time, so it is very natural to askhow long will the device last?

The evidence for material/device degradation is apparently everywhere in nature. A fresh coating of paint on a house will eventually crack and peel. Doors in a house can become stuck due to the shifting of the foundation. The new finish on an automobile will oxidize with time. The tight tolerances associated with finely meshed gears will deteriorate with time. Critical parameters that are associated with precision semiconductor devices (threshold voltages, drive currents, interconnect resistances, capacitor leakages, etc.) will degrade with time. In order to understand the lifetime of the material/device, it is important to understand the reliability physics (kinetics) for each of the potential failure mechanisms and then be able to develop the required reliability engineering methods that can be used to prevent, or at least minimize the occurrence of, device failure.

Reliability engineering is a fundamental part of all good electrical, mechanical, and civil engineering designs. Since proper materials selection can also be a critically important reliability factor, reliability engineering is also very important to materials scientists. Reliability is distinguished from quality in that quality usually refers to time-zero compliance or conformance issues for the material/device. Reliability refers to the time dependence of material/device degradation. All devices (electrical and/or mechanical) are known to degrade with time. Measuring and modeling the degradation rate, the time to failure, and the failure rate are the subjects of reliability engineering.

Many electrical and mechanical devices, perhaps due to performance and/or cost reasons, push their standard operating conditions (use conditions) very close to the intrinsic strength of the materials used in the design. Thus, it is not a question of whether the device will fail, but when. Reliability engineering methods permit theelectrical engineer, armed with accelerated testing data, to claim with confidence that a newly designed integrated circuit will last at least 10 years under specified voltage and temperature operating conditions. Reliability engineering methods permit the mechanical engineer to claim that the newly designed engine will last for 180,000 miles at 3000 rpm with an oil change required every 6000 miles. Reliability engineering methods permit the civil engineer to claim that a newly designed bridge should last at least 75 years under specified environmental and use conditions. Reliability engineering methods enable the materials scientist to select a costeffective material which can safely withstand a specified set of high-temperature and high-stress use conditions for more than 10 years.

This textbook provides the basics of reliability physics and engineering that are needed by electrical engineers, mechanical engineers, civil engineers, biomedical engineers, materials scientists, and applied physicists to help them to build better devices/products. The information contained within should help all fields of engineering to develop better methodologies for more reliable product designs, reliable materials selections, and reliable manufacturing processes-all of which should help to improve product reliability. A mathematics level through differential equations is needed. Also, a familiarity with the use of Excel spreadsheets is assumed. Any needed statistical training and tools are contained within the text. While device failure is a statistical process (thus making statistics important), the emphasis of this book is clearly on the physics of failure and developing the reliability engineering tools required for product improvements during device-design and device-fabrication phases.

Plano, TX, USA
J. W. McPherson# Acknowledgments 

I would like to thank the many excellent engineers and scientists that I had the pleasure of working with and learning from during my three-decade career with Texas Instruments. Also, I am very appreciative of the ideas developed during stimulating discussions with many colleagues in reliability physics and engineering within industry, universities, and national laboratories. I will be forever grateful to Physics Professors E. Garness Purdom (Guilford College), Yung-Li Wang (Florida State University), and Edward Desloge (Florida State University) being outstanding role models during my earliest physics education. I benefited greatly from interactions with two Nobel Prize Winners in physics: Paul Dirac (Florida State University) and Jack Kilby (Texas Instruments).# Contents 

1 Introduction ..... 1
2 Physics of Degradation ..... 5
1 Degradation ..... 5
2 Rise of Entropy ..... 6
3 Metastable States ..... 8
4 Gibbs Potential/Free-Energy (A Brief Review) ..... 10
5 Relationship Between Increased Gibbs Potential and Decreased Stability ..... 14
6 Dissipative Work ..... 22
7 Reaching Lower Gibbs Potential ..... 23
8 Imperfect Materials/Devices ..... 25
9 Nuclide Degradation ..... 28
Bibliography ..... 31
3 Time-Dependence of Materials and Device Degradation ..... 33
1 Materials/Device Degradation ..... 33
2 Material/Device-Parameter Degradation Modeling ..... 34
2.1 Material/Device-Parameter Decreases with Time ..... 36
2.2 Material/Device-Parameter Increases with Time ..... 39
3 General Time-Dependent Degradation Models ..... 42
4 Degradation Rate Modeling ..... 42
5 Delays in the Start of Degradation ..... 45
6 Competing Degradation Mechanisms ..... 50
Problems ..... 52
4 From Material/Device Degradation to Time-to-Failure ..... 59
1 Time-to-Failure (TF) ..... 59
2 Time-to-Failure Kinetics ..... 62
Problems ..... 635 Time-to-Failure Modeling ..... 67
1 Flux-Divergence Impact on Time-to-Failure ..... 67
2 Stress Dependence and Activation Energy ..... 71
3 Conservative Time-to-Failure Models ..... 75
4 Time-to-Failure Modeling Under High-Stress ..... 77
Problems ..... 78
Bibliography ..... 80
6 Gaussian Statistics: An Overview ..... 81
1 Normal Distribution ..... 81
2 Probability Density Function ..... 86
3 Statistical Process Control ..... 87
Problems ..... 90
Bibliography ..... 91
7 Time-to-Failure Statistics ..... 93
1 Lognormal Probability Density Function ..... 93
2 Weibull Probability Density Function ..... 97
3 Multimodal Distributions ..... 100
3.1 Multimodal Distribution (Separated in Time) ..... 100
3.2 Mixed Multiple Failure Mechanisms ..... 103
Problems ..... 105
Bibliography ..... 107
8 Failure Rate Modeling ..... 109
1 Device Failure Rate ..... 109
2 Average Failure Rate ..... 110
2.1 Lognormal Average Failure Rate ..... 111
2.2 Weibull Average Failure Rate ..... 112
3 Instantaneous Failure Rate ..... 113
3.1 Lognormal Instantaneous Failure Rate ..... 113
3.2 Weibull Instantaneous Failure Rate ..... 114
4 Bathtub Curve ..... 114
5 Failure Rate for Electronic Devices ..... 116
Problems ..... 121
Bibliography ..... 124
9 Accelerated Degradation ..... 125
1 Impact of Temperature on Degradation Rate ..... 125
2 Impact of Stress and Temperature on Degradation Rate ..... 127
3 Accelerated Degradation Rates ..... 130
4 Free Energy of Activation ..... 132
5 Real Versus Virtual Stresses ..... 133
Problems ..... 134
Bibliography ..... 13610 Acceleration Factor Modeling ..... 137
1 Acceleration Factor ..... 137
2 Power-Law Versus Exponential Acceleration ..... 140
3 Cautions Associated with Accelerated Testing ..... 142
4 Conservative Acceleration Factors ..... 142
Problems ..... 145
Bibliography ..... 147
11 Ramp-to-Failure Testing ..... 149
1 Ramp-to-Failure Testing ..... 149
2 Linear Ramp Rate ..... 150
2.1 Linear Ramp with Exponential Acceleration ..... 150
2.2 Linear Ramp with Power-Law Acceleration ..... 152
3 Breakdown/Rupture Distributions ..... 154
4 Cautions for Ramp-to-Failure Testing ..... 156
5 Transforming Breakdown/Rupture Distributions into Constant-Stress Time-to-Failure Distributions ..... 157
5.1 Transforming Breakdown/Rupture Distribution to Time-to-Failure Distribution Using Exponential Acceleration ..... 157
5.2 Transforming Breakdown/Rupture Distribution to Time-to-Failure Distribution Using Power-Law Acceleration ..... 158
6 Constant-Stress Lognormal Time-to-Failure Distributions from Ramp Breakdown/Rupture Data ..... 158
6.1 Exponential Acceleration ..... 158
6.2 Power-Law Acceleration ..... 159
7 Constant-Stress Weibull Time-to-Failure Distributions from Ramp Breakdown/Rupture Data ..... 160
7.1 Exponential Acceleration ..... 160
7.2 Power-Law Acceleration ..... 160
Problems ..... 162
Bibliography ..... 164
12 Time-to-Failure Models for Selected Failure Mechanisms in Integrated Circuits ..... 165
1 Electromigration ..... 165
2 Stress Migration ..... 175
2.1 SM in Aluminum Interconnects ..... 176
2.2 SM in Cu Interconnects ..... 178
3 Corrosion ..... 183
3.1 Exponential Reciprocal-Humidity Model ..... 187
3.2 Power-Law Humidity Model ..... 187
3.3 Exponential Humidity Model ..... 188
4 Thermal-Cycling/Fatigue Issues ..... 189
5 Time-Dependent Dielectric Breakdown ..... 1945.1 Exponential E-Model ..... 195
5.2 Exponential 1/E-Model ..... 197
5.3 Power-Law Voltage V-Model ..... 198
5.4 Exponential $\sqrt{E}$-Model ..... 198
5.5 Which TDDB Model to Use? ..... 198
5.6 Complementary Electric Field and Current-Based Models ..... 201
6 Mobile-Ions/Surface-Inversion ..... 205
7 Hot-Carrier Injection ..... 207
8 Negative-Bias Temperature Instability ..... 212
Problems ..... 217
Bibliography ..... 220
13 Time-to-Failure Models for Selected Failure Mechanisms in Mechanical Engineering ..... 227
1 Molecular Bonding in Materials ..... 227
2 Origin of Mechanical Stresses in Materials ..... 231
3 Elastic Behavior of Materials ..... 233
4 Inelastic/Plastic Behavior of Materials ..... 237
5 Important Defects Influencing Material Properties ..... 239
5.1 Vacancies ..... 240
5.2 Dislocations ..... 241
5.3 Grain Boundaries ..... 244
6 Fracture Strength of Materials ..... 246
7 Stress Relief in Materials ..... 248
8 Creep-Induced Failures ..... 249
8.1 Creep Under Constant Load/Stress Conditions ..... 249
8.2 Creep Under Constant Strain Conditions ..... 258
9 Crack-Induced Failures ..... 263
9.1 Stress Raisers/Risers at Crack Tips ..... 264
9.2 Strain-Energy Release Rate ..... 266
9.3 Fast Fracture/Rupture ..... 268
10 Fatigue-Induced Failures ..... 269
10.1 Fatigue for Materials (No Pre-existing Cracks) ..... 271
10.2 Low-Cycle Fatigue ..... 272
10.3 High-Cycle Fatigue ..... 272
10.4 Fatigue for Materials (With Pre-existing Cracks) ..... 275
11 Adhesion Failures ..... 277
12 Thermal-Expansion-Induced Failures ..... 278
12.1 Thermal Expansion ..... 278
12.2 Constrained Thermal-Expansion ..... 280
12.3 Thermal-Expansion Mismatch ..... 281
12.4 Thin Films on Thick Substrates ..... 28313 Corrosion-Induced Failures ..... 285
13.1 Dry Oxidation ..... 285
13.2 Wet Corrosion ..... 292
13.3 Humidity-Induced Oxidation/Reduction ..... 294
13.4 Impact of Stress on Corrosion Rates ..... 296
Problems ..... 298
Bibliography ..... 302
14 Conversion of Dynamical Stresses into Effective Static Values ..... 305
1 Effective Static-Stress Equivalent Values ..... 305
2 Effective Static-Stress Equivalent Values When Using Power-Law TF Models ..... 307
3 Effective Static-Stress Equivalent Values When Using Exponential TF Models ..... 309
4 Conversion of a Dynamical Stress Pulse into a Rectangular Pulse Stress Equivalent ..... 310
4.1 Effective Rectangular Pulse Stress-Equivalent Values for Power-Law TF Models ..... 311
4.2 Effective Rectangular Pulse Stress-Equivalent Values for Exponential TF Models ..... 311
4.3 Numerical Integration ..... 312
5 Effective Static Temperature Equivalents ..... 316
6 Mission Profiles ..... 319
7 Avoidance of Resonant Frequencies ..... 324
Problems ..... 325
15 Resonance and Resonance-Induced Degradation ..... 331
1 Natural/Resonant Frequency ..... 331
2 Pulsing at Strong Resonance ..... 337
3 Pulsing at Strong Resonance with Dissipation ..... 340
4 Pulsing at Weak Resonance with Dissipation ..... 345
5 Onset of Yielding/Irreversible-Damage due to Pulsing ..... 347
Problems ..... 350
Bibliography ..... 352
16 Increasing the Reliability of Device/Product Designs ..... 353
1 Reliability Enhancement Factor ..... 354
2 Electromigration Design Considerations ..... 354
3 TDDB Design Considerations ..... 355
4 Negative-Bias Temperature Instability Design Considerations ..... 356
5 HCI Design Considerations ..... 356
6 Surface Inversion Design Considerations ..... 357
7 Creep Design Considerations ..... 358
7.1 Creep in Rotors ..... 359
7.2 Creep in Pressurized Vessels ..... 359
7.3 Creep in a Leaf Spring ..... 360
7.4 Stress Relaxation in Clamps/Fasteners ..... 3618 Fatigue Design Considerations ..... 361
8.1 Fatigue in Storage Vessels ..... 362
8.2 Fatigue in Integrated Circuits (ICs) ..... 362
Problems ..... 363
17 Screening ..... 365
1 Breakdown/Strength Distribution for Materials and Devices ..... 365
2 Impact of Screening Stress on Breakdown Strength ..... 366
2.1 Screening Using Exponential TF Model ..... 367
2.2 Screening Using Power-Law TF Model ..... 369
3 Screening Effectiveness ..... 372
3.1 Screening Effectiveness Using Exponential TF Model ..... 373
3.2 Screening Effectiveness Using Power-Law TF Model ..... 373
Problems ..... 378
18 Heat Generation and Dissipation ..... 381
1 Device Self-Heating and Heat Transfer ..... 381
1.1 Energy Conservation ..... 382
1.2 General Heat Flow Equation ..... 384
2 Steady-State Heat Dissipation ..... 387
3 Effective Thermal Resistance ..... 390
4 General Transient Heating and Heat Dissipation ..... 394
4.1 Effective Thermal Resistance Revisited ..... 395
4.2 Heat Capacity ..... 396
5 Modeling Dynamical Heat Generation and Dissipation ..... 396
5.1 Thermal Relaxation ..... 398
5.2 Thermal Rise with Constant Input Power ..... 401
5.3 Thermal Rise and Relaxation with Single Power Pulse ..... 402
5.4 Thermal Rises and Relaxations with Periodic Power Pulses ..... 403
6 Convection Heat Transfer ..... 407
7 Radiation Heat Transfer ..... 410
8 Entropy Changes Associated with Heat Transfer ..... 411
Problems ..... 414
Bibliography ..... 417
19 Sampling Plans and Confidence Intervals ..... 419
1 Poisson Distribution ..... 419
1.1 Poisson Probability for Finding Defective Devices ..... 420
1.2 Poisson Sample Size Requirements ..... 422
2 Binomial Distribution ..... 424
2.1 Binomial Probability for Finding Defective Devices ..... 424
2.2 Binomial Sample Size Requirements ..... 425
3 Chi Square Distribution ..... 427
3.1 Chi Square Confidence Intervals ..... 427
3.2 Chi Square Distribution for Defect Sampling ..... 4294 Confidence Intervals for Characteristic Time-to-Failure and Dispersion Parameters ..... 431
4.1 Normal Distribution Confidence Intervals ..... 431
4.2 Lognormal Distribution Confidence Intervals ..... 433
4.3 Weibull Distribution Confidence Intervals ..... 435
4.4 Chi Square Distribution Confidence Intervals for Average Failure Rates ..... 437
Problems ..... 439
Bibliography ..... 441
Appendices ..... 443
Index ..... 455# Chapter 1 <br> Introduction 

It is very frustrating (and often very expensive) to buy a device only to have it to fail with time. However, all devices (from integrated circuits to automobile tires) are fabricated from materials that will tend to degrade with time. The materials degradation will continue until some critical device parameter can no longer meet the required specification for proper device functionality. At this point, one usually says-the device has failed. The failure could be due to an increase in capacitor leakage (in the case of the integrated circuits) or the inability of an automobile tire to hold proper pressure (blowout). Materials degradation and eventual device failure are the subjects of Reliability Physics and Engineering. Reliability physics is normally associated with understanding the kinetics (temperature and stress dependence) of failure mechanisms. Reliability engineering is usually associated with establishing: proper design rules, robust materials selection criteria, and good manufacturing guidelines for reliable device fabrication and use.

Device failure, be it either electrical or mechanical, can usually be attributed to the degradation of a given material under stress. The term stress, as used in this text, is very general and not restricted just to the more common meaning: mechanical stress. Capacitors can fail because of dielectric breakdown due to electric-field stress. Interconnects can fail because of resistance rises due to electromigrationinduced voiding as a result of a high current-density stress. Metal-oxide-silicon fieldeffect transistors (MOSFETs) can fail due to interface-state generation during a voltage/field stress. Mechanical components can fail because of creep due to a high tensile stress. Metal corrosion can occur because of high humidity stress. Mechanical components can fail due to fatigue which can result from cyclical mechanical stress. Surfaces can wear due to a shearing frictional stress. Components can rupture because of crack propagation due to thermomechanical stress during temperature cycling.

Stress, as used in this text, will refer to any external agent which is capable of causing degradation to occur in the material properties such that the device can no longer function properly in its intended application. In the case of dielectrics, this could be the dielectric breakdown which occurs when an electric-field stress exceedsthe dielectric strength of the material (e.g., for $\mathrm{SiO}_{2}$ this is $>10 \mathrm{MV} / \mathrm{cm}$ ). Or, in the case of metals, this might be the rupture which occurs when a mechanical stress is applied which exceeds the rupture strength of the metal (e.g., for aluminum interconnects this is $>600 \mathrm{MPa}$ ). However, even when a material is stored at a fixed level of stress less than the material's strength, the material will still degrade with time and device failure is eventually expected.

The observed time-to-failure (TF) will depend on the temperature and the magnitude of the applied stress relative to the breakdown strength of the material. The breakdown strength is usually defined as the level of stress at which the material is expected to fail instantaneously. [By instantaneous, it is meant that the time-tofailure is extremely short (few seconds) versus the time-to-failure (many years) when the material is stressed at $50 \%$ of its breakdown/rupture strength.] To ensure that time-dependent failures are minimized during the expected lifetime of the product, historically, a good engineering design will comprehend the distribution of material strengths that is likely to result from normal processing/fabrication, and then keep the design stress-level well below these strength values. This is usually referred to as the safety factor approach for increased reliability margin.

The safety factor approach is, however, only qualitative (relative to time-tofailure modeling) and is becoming increasingly difficult to use for aggressive designs. For example, integrated circuits where device feature sizes continue to be aggressively scaled according to Moore's Law (a $0.7 \times$ reduction in feature size per technology node), the scaling has generally caused device current densities and electric fields to increase, forcing the normal use-conditions to be ever closer to the breakdown strength of the materials. In addition, the temperature cycling of assembled silicon chips generally leads to large thermomechanical stresses due to the thermal-expansion mismatch of the dissimilar materials used in chip fabrication and in the assembly process.

Mechanical devices also tend to be designed aggressively because of higher performance and/or materials cost-reduction demands. This serves to push the normal operational conditions much closer to the breakdown strength of the materials. How close can the application stress be to the material's strength (commonly referred to as the reliability margin or design rule), in order to achieve many years of reliable device operation, depends on the degradation rate for the material/device. The stress and temperature dependence of this degradation rate is the subject of reliability physics and is normally studied through the use of accelerated testing.

Chapter 2 will focus on the physics of degradation and why all fabricated materials are fundamentally unstable. Chapters 3, 4, and 5 will concentrate on material/device degradation models and the development of the critically important time-to-failure models. Since time-to-failure is statistical in nature, an overview of the needed statistical tools is presented in Chaps. 6 and 7. Failure-rate modeling is presented in Chap. 8. The use of accelerated testing methods and the modeling of the acceleration factors are presented in Chaps. 9 and 10, respectively. Important ramp-to-failure testing methods are introduced in Chap. 11. In Chap. 12, time-to-failure models are presented for selected failure mechanisms in electrical engineering applications. Likewise, in Chap. 13, time-to-failure models are presented forselected failure mechanisms in mechanical engineering applications. Chapter 14 describes how dynamical (time-dependent) stresses can be converted into staticvalue equivalents for easy use with all the models developed. Chapter 15 looks at the reliability impact of resonance and resonance avoidance methods. Chapter 16 focuses on the practical use of reliability enhancement factors, during initial product design and development, in order to increase the expected product lifetime and to reduce the expected device failure rate during customer use. Chapter 17 discusses the use of short-duration elevated stresses to screen out defective devices/materials. The critical importance of heat generation and dissipation for device/materials reliability is discussed in Chap. 18. The book is concluded with Chap. 19 which discusses sampling statistics and confidence intervals for defect level determination and for time-to-failure determination.# Chapter 2 <br> Physics of Degradation 

Regardless how carefully crafted, devices are made of materials that generally exist in metastable states. A state is referred to as being metastable if it is only apparently stable and susceptible to change/degradation. The driving force for materials degradation is a lower Gibbs Potential. When we apply a generalized stress $\xi$ to a material, it tends to increase (not lower) the Gibbs Potential. Therefore, a stressed material is even more unstable and even more susceptible to degradation. Since devices are fabricated from materials (and materials degrade with time), then devices will degrade with time. Engineers are confronted with the very difficult situation-they must manage the degradation rate in order to prevent failure.

The focus of this chapter is understanding the physics of degradation. This includes a better understanding of the driving force for degradation and the roles that a generalized stress $\xi$ and temperature $T$ play in the degradation process. Material defects can often play important roles in the degradation process. For this reason, it can be important to start (at time zero) with materials that are relatively defect free. This, however, raises an important question that must be addressed-is it possible to build a defect-free material?

## 1 Degradation

We are all confronted with this truism-regardless of how carefully crafted a device is at time zero, the materials in the device will degrade with time. Evidence of material degradation (deterioration of a material's properties with time) seemingly exists everywhere. Several illustrations of common material degradation mechanisms are shown in Fig. 2.1. Cracks tend to develop in a brick wall due to foundation/soil erosion. Regardless of the quality of paint, paint will degrade under environmental conditions and eventually crack and peel. A metal roof, once bright and shiny, will oxidize/corrode with time. Finally, in Fig. 2.1d, one can easily see that you and I are not immune to degradation-the teeth shown have developed

Fig. 2.1 (a) Cracks tend to develop in brick walls as the foundation degrades. (b) Paint will eventually crack and peel. (c) Bright shiny metal roofs will oxidize/corrode. (d) Human beings are not immune to degradation-note the tooth decay, fillings, and cracking
decay and the decay has led to needed fillings and cracks in the teeth. Thus, we have to accept the fact that materials will degrade with time. Since devices are made of materials, device degradation will occur as a result of materials degradation.

# 2 Rise of Entropy 

Most of us are familiar with, and know the importance of, the First Law of Thermodynamics. The First Law tells us that energy is conserved. Energy can be transformed, but it is always conserved. For example, suppose that a ball is dropped from the roof of a building at a height $h_{0}$. The initial potential energy of the ball is $m g h_{0}$, where $m$ is the mass of the ball and $g$ is the acceleration of gravity. As the ball drops, the potential energy of the ball is transformed to kinetic energy. When the ball bounces from the sidewalk below, we note that it returns to a height $h_{1}$, where $h_{1}<h_{0}$. It seems that some of the initial energy of the ball was lost. But no, when the potential energy of the ball at its new maximum height $h_{1}$ is added to the thermal energy produced (as the ball falls through the frictional forces of the air) plus the thermal energy produced when the ball slams into the concrete sidewalk below, then the total energy perfectly matches the initial potential energy of the ball. Thus, some of the initial potential energy was transformed to heat, but the total energy was conserved!Fig. 2.2 Examples of increased entropy. (a) Egg tends to split when cracked. (b) Object breaks into many pieces when dropped


The Second Law of Thermodynamics is probably lesser known but, arguably, it is just as important as the First Law. The Second Law tells us that for an isolated system of particles (atoms, molecules, gases, liquids, solids), the entropy (chaos) of the system will tend to increase spontaneously with time. This means that for an isolated system (a system for which no energy or mass can be transferred), order tends to degrade with time. As for its impact on reliability, the Second Law means that even the most carefully prepared material/device will tend to degrade with time.

A couple of examples of increasing entropy/chaos are illustrated in Fig. 2.2. Once an egg is cracked (Fig. 2.2a) it tends to remain broken. A dropped object (Fig. 2.2b) seemly breaks into a million pieces. In these examples, an external force acted on the system to produce the degradation. Such processes or actions tend to increase the entropy $S$ of the system. If the system is isolated after breakage, then these changes are irreversible.

Shown in Fig. 2.3a is another example of increasing entropy. During a blizzard, chaotic conditions tend to develop. These chaotic conditions can produce: randomness in the flying snowflakes, downed trees, and broken power lines. In fact, even more entropy/chaos can be generated if we simply allow the temperature to rise (addition of heat) and the snowflake crystals begin to melt. This is what happens to isolated systems (or systems with external dissipative forces acting)-the entropy tends to increase with time.

If the system is, however, not totally isolated (thus permitting energy flow), then Fig. 2.3b shows that some degree of order can be reestablished if we are willing to input energy into the system. In this case, the energy input is in the form of work. Work against frictional forces was required to roll the snow into snowballs. Work against gravity was required to stack the snowballs vertically thereby creating the snowmen family shown. Thus, work (done by an external force) was required to

Fig. 2.3 (a) Chaos develops during a blizzard. (b) Work can seemly convert chaos into order
bring the system's chaos back into some semblance of order. We also know this from common experience-a child's room, left unattended, generally becomes more chaotic with time. Only occasional work by the parent can restore the room back to its original order. Apparently work can serve to decrease the entropy of the child's room and might seem to violate the Second Law. However, in order for humans to do work, enormous amounts of food must be consumed. During digestion of such food, orderly plant and animal cell structures are broken down resulting in a large rise in entropy. Thus, the decrease in room entropy is more than offset by the rise in entropy elsewhere.

Before we leave this section, it should be noted that the snowmen in Fig. 2.3 are not very stable-a little wind or slight increase in temperature and the snowmen will begin to degrade. Due to the lack of stability in these work-created snowmen, their precarious state can be described as metastable.

# 3 Metastable States 

Materials/devices/systems often appear to be in very stable states. However, they are simply captured in momentary metastable states. Metastable means that the existing state/configuration is only apparently stable in that it can undergo transformation, with time, to a more stable state (state with lower potential energy). ${ }^{1}$ For example, a pebble on the edge of a cliff appears to be very stable until a slight push is given to the pebble. Note, however, that an input of energy was required to activate a change in the metastable state for the pebble.

Perhaps it is instructive to work through a simple example-one that is familiar to all of our experiences. This simple example should help us to better understand the

[^0]
[^0]:    ${ }^{1}$ Actually, a state with lower Gibbs Potential (as discussed in Sect. 4).

Fig. 2.4 Rectangular block is momentarily captured in the vertical position with potential energy $\mathrm{U}_{1}$. This vertical position is a metastable state for the block center of mass (CM) because a lower potential-energy state $\left(\mathrm{U}_{2}\right)$ is available for the center of mass. The driving force for a change of state is that $\mathrm{U}_{2}$ must be of lower potential energy than $\mathrm{U}_{1}$. However, an input of work energy (by an amount of $\Delta U^{*}$ ) is required to activate the change of state
strong driving force for all materials/devices to reach the lowest potential energy state available. Shown in Fig. 2.4 is a rectangular block that is momentarily captured in a metastable vertical state with potential energy $U_{J}$. However, a horizontal state is also available to the block and at a lower potential energy $U_{2}$. Since $U_{2}-U_{J}$ is negative, and if an energy input of $\Delta \mathrm{U}^{*}$ is supplied (for example, by simply shaking or bumping the supporting table), then a potential-energy reduction (driving-force) exists for the block center of mass (CM) to go from vertical state (with potential energy $\mathrm{U}_{1}$ ) to horizontal state (with lower potential energy $\mathrm{U}_{2}$ ).

The driving force $(\Delta U)$ for block transformation, from vertical to horizontal position, is driven by a potential energy reduction:

$$
\Delta U=U_{2}-U_{1}=-\frac{M g}{2}(L-W)
$$

where M is the mass of the block, g is the acceleration of gravity, W is the width of the block, and L is its height. The input energy $\Delta U^{*}$ required to activate the block transformation process is given by:

$$
\Delta U^{*}=\frac{M g}{2}\left(\sqrt{L^{2}+W^{2}}-L\right)
$$

From the above equations it can be seen that when the height of the block L increases relative to the width W , the block becomes less stable in the vertical state ( $\Delta U$ becomes more negative). Also, it is noted that the input energy $\Delta U^{*}$ required to activate the block transformation (from vertical to horizontal state) also reduces. In fact, the activation energy $\Delta U^{*}$ goes to zero when $\mathrm{L}>>\mathrm{W}$. This simple example ofblock instability serves to illustrate something that is very important and fundamental to reliability physics: materials put in higher potential energy states are fundamentally more unstable.

In the simple example shown in Fig. 2.4, only gravitational potential energy was considered to be important. The required energy input needed to produce a block transformation (from vertical to horizontal state) was in the form of work (something must push on the block or shake/bump the supporting table). However, we will discuss below thermodynamic systems where the required energy input for transformation can be in the form of work and/or heat. Reduction in the Gibbs Potential $\Delta G$ will serve as the driving force (as opposed to simply the gravitation potential energy used for the block transformation analysis above).

# 4 Gibbs Potential/Free-Energy (A Brief Review) 

Let us first start with a system of particles (gas, liquid, or solid) and use the First Law of thermodynamics (conservation of energy). We will let $U$ represent the internal energy of the system (sum of kinetic plus the potential energy of all particles). Any infinitesimal change in the internal energy $d U$ of the system must be equal to any infinitesimal heat additions $\delta q$ to the system plus any infinitesimal work $\delta w$ done on the system: $d U=\delta q+\delta w .{ }^{2}$ If the heat is added in a quasistatic/reversible manner, then $\delta q=T d S$, where $T$ is the temperature (Kelvin) and $S$ is the entropy. The infinitesimal work $\delta w$ done on the system is given by $\delta w=\xi d \varepsilon$, where $\xi$ is a generalized stress (external agent) that produces a generalized strain $\varepsilon$ (system response). Several examples of generalized stresses and generalized system responses (strains) are shown in Table 2.1.

The infinitesimal changes in internal energy $d U$ of the system (due to quasistatic heat additions to the system and any work done on the system) can be expressed as:

$$
\begin{aligned}
d U & =\delta(\text { Heat })+\delta(\text { Work }) \\
& =T d \mathcal{S}+\delta(\text { Work }) \\
& =T d \mathcal{S}-p d V+\sigma d \varepsilon+E d P+H d M+\text { etc. } \\
& =T d \mathcal{S}-p d V+\sum_{i} \xi_{i} d \varepsilon_{i}
\end{aligned}
$$

where $p$ is the pressure acting on system of volume $V, T$ is the temperature (Kelvin), and $S$ is the entropy. $\xi_{i}$ represents an external generalized stress (mechanical, electrical, magnetic, chemical, etc.) acting on the system to produce a generalized system response $\varepsilon_{i}$ (strain, polarization, magnetization, mole number, etc.). Rearrangement of Eq. (2.3) gives,

[^0]
[^0]:    ${ }^{2}$ The symbol $\delta$ is used (versus $d$ ) to indicate that the quantity may not be an exact differential (see Appendix F).Table 2.1 Methods for doing differential work on materials/devices

| Materials/ <br> devices | Type of work | Intensive and extensive variables | Differential work $\delta$ w done <br> on material/device |
| :-- | :--: | :--: | :--: |
| Fluids | Mechanical | Pressure $p$ and volume $V$ | $-p \mathrm{~d} V$ |
| Elastic <br> filaments | Mechanical | Force $F$ and length $L$ | $F \mathrm{~d} L$ |
| Solids | Mechanical | Mechanical stress $\sigma$ and volume <br> $V$ | $\sigma \mathrm{d} V$ |
| Dielectrics | Electrical | Electric field $E$ and polarization $P$ | $E \mathrm{~d} P$ |
| Magnetics | Electrical | Magnetic field intensity $H$ and <br> magnetization $M$ | $H d M$ |
| Batteries | Electrochemical | Voltage $V$ and charge stored $Q$ | $V \mathrm{~d} Q$ |
| Fuel cells | Chemical | Chemical potential $\mu$ and mole <br> number N | $\mu \mathrm{d} N$ |

$$
d U+p d V-T d \mathcal{S}=\sum_{i} \xi_{i} d \varepsilon_{i}
$$

The differential Gibbs ${ }^{3}$ Potential $d G$ is a defined potential and is given by

$$
d G=d U+p d V-T d \mathcal{S}=d H-T d \mathcal{S}=\sum_{i} \xi_{i} d \varepsilon_{i}
$$

where $d H=d U+p d V$ is the differential enthalpy. If there are no changes in system volume, then, changes in enthalpy and internal energy are the same: $d H=d U$. For materials/device degradation, we are generally interested in spontaneous changes in the Gibbs Potential at constant pressure $p$, constant temperature $T$, and constant generalized stress $\xi_{i}$. Under these conditions, the change in Gibbs Potential can be found by integrating Eq. (2.5) and we obtain either:

$$
\Delta G=\Delta H-T \Delta \mathcal{S}
$$

or

$$
\Delta G=\sum_{i} \xi_{i} \Delta \varepsilon_{i}
$$

Let us first concentrate on $\Delta \mathrm{G}$ using Eq. (2.6). There are two primary ways that a system can spontaneously lower its Gibbs Potential: by a decrease in enthalpy $(\Delta \mathrm{H})$ or by an increase in entropy $(\Delta \mathrm{S})$. These two methods, for Gibbs Potential $\Delta \mathrm{G}$

[^0]
[^0]:    ${ }^{3}$ Willard Gibbs was an American physicist/physical-chemist/mathematician (1839-1903). As a physicist/physical-chemist, he was the first to combine the First and Second Laws of Thermodynamics into a single equation (Eq. (2.3)). As a mathematician, he invented vector calculus. Albert Einstein once described Gibbs as "the greatest mind in American history."Fig. 2.5 Gibbs Potential reduction can occur due to: (a) reduction in enthalpy due to dominance of cohesive binding-forces or (b) increase in entropy due to dominance of dispersive forces

reduction, are illustrated in Fig. 2.5. In one case (oil in water) the cohesive bindingforces dominate, while in the other case (alcohol in water), the dispersive (diffusional) forces dominate. While these two examples of spontaneous change seem to be contradictory, they both reach the same objective-a lower Gibbs Potential.

Shown in Fig. 2.5a is the situation where cohesive binding-forces dominate. When very small individual droplets of oil are added to water at time zero, at some later time the individual droplets will spontaneously start to coalesce into a localized oil-rich region. In this case the cohesive forces attracting the oil molecules are so great that a reduction in Gibbs Potential $\Delta \mathrm{G}$ occurs through a reduction in enthalpy $\Delta \mathrm{H}$. However, the apparently opposite situation is shown in Fig. 2.5b. When alcohol is placed in a very localized region of the water at time zero, the alcohol spontaneously starts to disperse. Here, since the binding energy among the alcohol molecules in water is relatively weak, the dispersive forces are great (driven by an entropy increase $\Delta \mathrm{S}$ ). In summary, a lower Gibbs Potential can be produced either by strong molecular bonding or by strong entropy increases.

Let us now concentrate on the change in Gibbs Potential $\Delta \mathrm{G}$ expressed by Eq. (2.7). Because of the way that Gibbs Potential is defined, if the external forces acting on the system are against resistive conservative system forces, then the work performed by the external forces (Eq. (2.5)) serves to increase the Gibbs Potential for the system. This increase in stored potential energy is, of course, free to do work at some later time. For this reason, the Gibbs Potential is also referred to as Gibbs Free Energy. In this textbook, the two terms (Gibbs Potential and Gibbs Free Energy) will

Fig. 2.6 (a) Gibbs Potential/Free-Energy increase to due field-induced polarization $P$ in dielectric when a voltage drop of $\Delta \mathrm{V}$ occurs. (b) Gibbs Potential/Free-Energy reduction occurs (due to polarization collapse) when the dielectric breaks down thereby causing a short that permits current flow
be used interchangeably. An important feature of the Gibbs Potential is the fact that it has been defined in such a way that any spontaneous changes in the Gibbs Potential $\Delta \mathrm{G}$ can occur only if the change leads to a reduction in Gibbs Potential. Thus, according to Eq. (2.7), for a stressed system (under constant generalized stress $\xi$ ), the only allowed spontaneous changes for the stressed system are those changes that lead to a relaxation/degradation of the generalized strain $\Delta \varepsilon$.

An example of generalized strain $\Delta \varepsilon$ relaxation/degradation is illustrated in Fig. 2.6. We show a capacitor dielectric under a constant electric field $\xi$ stress in Fig. 2.6a. The electric field $\xi$ has done work on the dielectric to create the polarization $P$ (an ordering of the dipoles). Thus, the work against the conservative resistive forces of the polarization $P$ has increased the potential energy of the stressed dielectric and this serves to increase the Gibbs Potential. However, as illustrated in Fig. 2.6b, the Gibbs Potential $G$ can be reduced if the dielectric spontaneously degrades (causing a polarization $\Delta \mathrm{P}$ relaxation/reduction). An even greater reduction in $\Delta G$ occurs if dielectric eventually breaks down thereby causing the polarization P to collapse and a conductive filament (short) to form.

Before we leave this very important section for reliability physics, let us briefly summarize. Work done on a system/material, against conservative resistive system forces, tends to increase the potential energy of the system/material; therefore, work can increase the Gibbs Potential $G$. However, the increase in Gibbs Potential makes a system/material more unstable because the Gibbs Potential prefers a decrease in potential (not an increase). Thus, for a material in a stressed state, spontaneous-change/degradation in the stressed material is expected since the degradation leads to a reduction in Gibbs Potential/Free-Energy.Fig. 2.7 When work is done against gravity, the block is put into the vertical metastable state. The work against gravity serves to increase the potential energy of the block (in vertical position); but the increase in potential energy for the center of mass (CM) of block comes at the expense of decreased block stability


# 5 Relationship Between Increased Gibbs Potential and Decreased Stability 

Let us look more closely at how the metastable state shown in Fig. 2.4 was created. To create this metastable state, an external force has to do work against the force of gravity (as shown in Fig. 2.7).

As we slowly (quasi-statically) move the block, from horizontal to vertical position, work must be done against gravity. The external force $F_{\text {ext }}$ must be in the positive y direction (since the force of gravity is in the negative y direction). This gives the work against gravity:

$$
W_{\text {Against Gravity }}=\int_{Y_{1}}^{Y_{2}} \vec{F}_{\text {ext }} \cdot d \vec{y}=M g \int_{Y_{1}}^{Y_{2}} d y=M g\left(Y_{2}-Y_{1}\right)=\Delta U
$$

where $\Delta \mathrm{U}$ is the increase in potential energy of block. While this example deals only with gravity, this simple example serves to establish a general trend-work done against conservative resistive forces ${ }^{4}$ tends to increase the potential energy of the body/system. The generalized stresses shown in the Table 2.1 are derived from conservative forces. Thus, the work done against these conservative forces will serve to increase the potential energy of the material/device.

The increase in potential energy for the center of mass (CM) of block comes at the expense of decreased block stability because the Gibbs Potential increases $(\Delta \mathrm{G}=\Delta \mathrm{U})$. Recall that the Gibbs Potential wants to decrease, not increase. We will now demonstrate, through several examples which follow, that this is a general feature of degradation-external forces, acting against conservative resistive forces

[^0]
[^0]:    ${ }^{4} \mathrm{~A}$ force is said to be conservative if the work done by the force around any closed path is zero. This is discussed in some detail in Appendix F.of a system, will increase the potential energy of the system and this will increase the Gibbs Potential of the system. However, the increase in Gibbs Potential for the system comes only at the expense of less stability for the system.

An illustration of a hydroelectric power generation station is shown in Fig. 2.8. A dam is constructed in a river that flows down from the mountains. As the gravitational potential energy of the water at the dam increases (with lake depth $h$ ), this serves to increase the resistive stresses of the dam. The greatest pressure on the dam occurs at the base of the dam where the generator is placed for maximum power generation. The mechanical stresses on the dam will tend to put the dam into a metastable state and degradation is expected.

The mechanical stress $\sigma$ on the dam at position x below the surface of the water is given by:

$$
\sigma(x)=\rho g x
$$

where $\rho$ is the density of water and g is the acceleration of gravity. Because the dam must resist the pressure of the water (Newton's third law), the increase in potential energy density $w$ in dam (as the depth of the water increases to h) is given by:

$$
\begin{aligned}
w & =\int_{0}^{\varepsilon_{\max }} \sigma(x) d \varepsilon=\frac{1}{E} \int_{0}^{\sigma_{\max }} \sigma(x) d \sigma \\
& =\frac{(\rho g)^{2}}{E} \int_{0}^{h} x d x=\frac{(\rho g h)^{2}}{2 E}
\end{aligned}
$$

where $E$ is the effective modulus for the composite materials used during dam construction. The increase in potential energy density for the dam is thus given by,

$$
\Delta u=w=\frac{(\rho g h)^{2}}{2 E}
$$

Thus, as the depth $h$ of water increases, the dam becomes less stable due to the rise in the Gibbs Potential energy density $(\Delta g=\Delta u)$. If the stresses on the dam reach the fundamental strength of the dam, then nearly instantaneous failure will occur. If the stresses on the dam are less than its strength, degradation will still occur but, of course, the degradation rate will be relatively slow. Figure 2.9 shows a dam that has degraded over time and that has eventually failed catastrophically.

Shown in Fig. 2.10 is a cylinder of confined gas with a movable piston. The piston can be used to compress the gas (can do work against the resistive force of the gas) and thereby increases its pressure (internal energy).

Fig. 2.8 Dam shown is built for hydroelectric power generation. As the depth of water $h$ increases, the gravitational potential energy stored in the water increases. This creates resistive stresses in the dam with the greatest pressure/stress occurring at the bottom of the dam where the generator is placed


Fig. 2.9 Degradation of dam (due to pressure of water) and eventual failure

Work done by the external force in compressing the gas is given by:

$$
\begin{aligned}
W_{\text {against gas }} & =\int_{x_{0}}^{x} \vec{F}_{\text {External }} \cdot d \vec{x}=\int_{x_{0}}^{x} \frac{\bar{x}\left(-F_{\text {External }}\right)}{A_{0}} \cdot A_{0} \vec{x}(d x) \\
& =-\int_{V_{0}}^{V} p d V
\end{aligned}
$$

where $p$ (=Force/Area) is the pressure. For an ideal gas, the pressure can be expressed by Boyle's Law:$$
p=\frac{N R T}{V}
$$

where N is the number of moles of gas, R is the ideal gas constant, T is the Kelvin temperature, and V is the volume. Thus, the rise in potential energy of the confined gas in the cylinder becomes

$$
\Delta U=W_{\text {against gas }}=-\int_{V_{0}}^{V} p d V=-\int_{V_{0}}^{V} \frac{N R T}{V} d V=\mathrm{NRT} \ln \left(\frac{V_{0}}{V}\right)
$$

Note that as the volume of gas decreases, the pressure rises (Eq. (2.13)) and the potential energy of the confined gas in the cylinder increases (Eq. (2.14)). This serves to decrease the stability of the metal gas-cylinder because the Gibbs Potential increases $(\Delta \mathrm{G}=\Delta \mathrm{U})$. If the gas pressure increases to the rupture strength of the metal cylinder, nearly instantaneous cylinder failure will occur. However, at lower gas pressures (less than the rupture strength) cylinder degradation will still occur but at a much slower rate. Shown in Fig. 2.11 is a storage tank that has undergone degradation with time and that has finally ruptured catastrophically.

Shown in Fig. 2.12 is a solid material put under compressive mechanical stress due to an external force. The mechanical stress $\sigma$ (=Force/Area) deforms the solid, thereby increasing the potential energy $\Delta \mathrm{U}$ of the solid,

$$
\begin{aligned}
\Delta U & =W_{\text {resistive forces }}=A_{0} \int_{L_{0}}^{L} \sigma d L=A_{0} \int_{L_{0}}^{L} E\left(\frac{L-L_{0}}{L_{0}}\right) d L= \\
& =\frac{1}{2} E L_{0} A_{0}\left(\frac{L-L_{0}}{L_{0}}\right)^{2}=\frac{1}{2} E V_{0} \varepsilon^{2}=\frac{1}{2}\left(\frac{V_{0}}{E}\right) \sigma^{2}
\end{aligned}
$$

where $\varepsilon$ is the material strain, $E$ is Young's modulus for material, and $\mathrm{V}_{0}$ is the unstressed volume of the solid. This mechanical stress action on the solid serves to increase its potential energy. The solid material becomes more unstable because of the rise in Gibbs Potential $(\Delta \mathrm{G}=\Delta \mathrm{U})$. If the mechanical stress $\sigma$ is above the fracture strength of the material, then nearly instantaneous failure will occur. At lower stress levels, but above the yield stress, ${ }^{5}$ the material will degrade with time but at a much slower rate. Shown in Fig. 2.13 are the threads of a bolt that have degraded and the bolt finally failed catastrophically due to mechanical stress.

Shown in Fig. 2.14 is a capacitor dielectric under an electric field stress due to a voltage drop $\Delta \mathrm{V}$ across the dielectric. The electric field $\xi$ in the dielectric serves to do work against the resistive nature of the polarization P . The work done per unit

[^0]
[^0]:    ${ }^{5}$ Yield stress is the value of stress at which some level of permanent/plastic deformation occurs in the material.Fig. 2.10 The external force (as it compresses the gas) does work against the resistive force of the gas. Compression of the gas causes a pressure rise and an increase in its potential energy


Fig. 2.11 Storage tank degradation (due to fluid pressure) and eventual rupture

volume $w$ by the electric field on the dielectric increases its potential energy per unit volume by $\Delta \mathrm{u}$ :

$$
\begin{aligned}
\Delta u=w & =\int_{0}^{x} \vec{F}_{\text {External }} \cdot d \vec{x}=\int_{0}^{P}(\vec{\xi}) \cdot d \vec{P}=\int_{0}^{P}\left(\frac{P}{\varepsilon_{d i e l}}\right) d P \\
& =\frac{1}{2}\left(\frac{P^{2}}{\varepsilon_{d i e l}}\right)=\frac{1}{2}\left(\frac{\left(\varepsilon_{d i e l} \xi\right)^{2}}{\varepsilon_{d i e l}}\right)=\frac{1}{2} \varepsilon_{d i e l} \xi^{2}
\end{aligned}
$$

where $\varepsilon_{d i e l}$ is the dielectric constant. Thus, the total potential energy of the dielectric increases by $\Delta U$ :

$$
\Delta U=V_{0}(\Delta u)=\frac{V_{0}}{2} \varepsilon_{d i e l} \xi^{2}=\frac{t_{d i e l} \cdot A_{0}}{2} \varepsilon_{d i e l} \xi^{2}
$$Fig. 2.12 Solid material is compressed by an external force


Fig. 2.13 Threads on a bolt have degraded (due to mechanical tensile stress) and the bolt eventually failed

where $t_{\text {diel }}$ is the dielectric thickness and $\mathrm{A}_{0}$ is the area of the dielectric. With the dielectric in a state of higher potential energy due to the electric field, dielectric degradation is expected because of a higher Gibbs Potential $(\Delta \mathrm{G}=\Delta \mathrm{U})$. If the electric field exceeds the dielectric breakdown strength, nearly instantaneous failure will occur. When the electric field is less than the dielectric breakdown strength, degradation will still occur, but at a much slower rate. A catastrophic capacitor failure is shown in Fig. 2.15. Also, it is interesting to note that Eq. (2.17) indicates that, for the same level of electric field stress, thicker dielectrics are more unstable than thinner; larger area capacitors are more unstable than smaller area capacitors. Indeed, we find that thicker dielectrics and larger area capacitors tend to have lower breakdown strength.

Finally, we consider the charging of a lithium-ion battery as illustrated in Fig. 2.16. During charging we are increasing the potential energy $\Delta \mathrm{U}$ stored in the battery by an amount:

$$
\begin{aligned}
\Delta U & =Q \cdot V \\
& =[\text { Battery Rating (in Amp-hr) }] \cdot[\text { Battery Voltage }]
\end{aligned}
$$

This increase in potential energy of the battery makes the battery less stable because of the increase in Gibbs Potential $(\Delta G=\Delta U)$. In fact, if one overcharges the battery, it will degrade even more rapidly. The instantaneous power dissipation during rapid discharge of a fully charged battery can be huge:Fig. 2.14 A capacitor under electric field $\xi$ stress. The field does work on the dielectric and this is reflected as an increase in polarization $P$


Fig. 2.15 Capacitor degradation (under electric field stress) and eventual failure. Due to the large amount of stored charge, rapid capacitor discharge can produce an explosivelike failure mode when a fully charged capacitor undergoes time-dependent dielectric breakdown
Fig. 2.16 Charging of a lithium-ion battery. During normal battery operation, the anode is positive and the cathode is negative. However, their roles are reversed during charging so as to recover the depleted lithium from the anode side


Fig. 2.17 An alleged automobile fire developed (due to cell phone overheating) when cell phone battery underwent rapid discharge

$$
\text { Power }=\frac{\mathrm{dU}}{\mathrm{dt}}=\frac{\mathrm{d}}{\mathrm{dt}}(\mathrm{QV}) \approx\left(\frac{\mathrm{dQ}}{\mathrm{dt}}\right) \cdot \mathrm{V}_{\text {Battery }}=\mathrm{I}_{\text {Discharge }} \cdot \mathrm{V}_{\text {Battery }}
$$

Thus, rapid battery discharge (of a fully charged battery) can produce so much heat that often a fire can develop in the surrounding materials. Shown in Fig. 2.17 is an automobile fire that was alleged to have occurred when a cell phone underwent rapid battery discharge.# 6 Dissipative Work 

There are other forms of work that can be done against nonconservative forces. Generally these forces generate dissipative work because the net effect is not to increase the potential energy, but to increase the thermal energy (TE) of the material. Shown in Fig. 2.18 is a form of dissipative work done on a solid.

Assuming negligible energy transfer to the table (and from block to air), conservation of energy implies that the change in internal energy $\Delta \mathrm{U}$ of the block must be equal to the dissipative work done on the block,

$$
\Delta U=\int_{x_{1}}^{x_{2}} \vec{F}_{e x t} \cdot d \vec{x}=\mu(m g) \Delta x
$$

where $\mu$ is the coefficient of sliding friction, $m$ is the mass of the block, and $g$ is the acceleration of gravity. Since this is dissipative work, the work serves only to increase the thermal energy (TE) of the block,

$$
\Delta(T E)=c_{H} m \Delta T
$$

where $\Delta T$ is the temperature rise and $\mathrm{c}_{H}$ is the specific heat of the block material. ${ }^{6}$ Equating the last two equations, one obtains the average temperature rise of the block:

$$
\Delta T=\left(\frac{\mu g}{c_{H}}\right) \Delta x
$$

Dissipative work effectively adds heat to the material and this serves to increase the thermal energy of the system. This increase in thermal energy (TE) is reflected as a temperature rise for the system. Higher temperatures make the material less stable


Fig. 2.18 Example of dissipative work. Sliding a block across a rough-surface table that is thermally insulated. The work against the sliding friction serves to increase the thermal energy of the block

[^0]
[^0]:    ${ }^{6}$ Refer to Chap. 18 for more details.and thus more prone to degradation. The impact of elevated temperature on material degradation rate is discussed in detail in Chap. 9.

Before we leave these two very important Sects. 5 and 6, let us again emphasize that by doing work on a system, against conservative resistive forces, the work tends to increase the potential energy of the system. The rise in system potential energy makes the system less stable because of the higher Gibbs Potential $(\Delta \mathrm{G})$. Dissipative work done against nonconservative forces tends to increase the thermal energy of the system (recorded as a temperature rise) and this can also make the system less stable and more prone to degradation.

# 7 Reaching Lower Gibbs Potential 

Now that we understand-the only spontaneous changes that can occur in stressed material are those changes that lead to a lower Gibbs Potential, we want to better understand the forces that drive these spontaneous changes. While it is correct to say that electrons/atoms/molecules respond to a gradient in Gibbs Potential, we want to better understand the exact nature of the forces that drive a material's spontaneous change to a lower Gibbs Potential. To do this, we will focus on the gradients of several specific potentials of interest.

Electrons/atoms/molecules respond to gradients, as illustrated in Fig. 2.19, with each of these gradients leading to a lower Gibbs Potential. Large masses respond to gradients in gravitational potential. Electrons respond to gradients in electrostatic potential. Atoms/molecules respond to gradients in chemical potential, concentration/density, mechanical stress, pressure, and temperature. As shown in Appendix

Forces on Electrons/Atoms are Derived from Gradients
$\square$ Gradient in Gravitational Potential
$\square$ Gradient in Electrostatic Potential
$\square$ Gradient in Chemical Potential
$\square$ Gradient in Concentration/Density
$\square$ Gradient in Mechanical Stress
$\square$ Gradient in Pressure
$\square$ Gradient in Temperature

Response To Gradients


Fig. 2.19 Electrons/atoms/molecules respond to potential gradients. Several common potential gradients are illustrated that ultimately lead to a lower Gibbs Potential

Fig. 2.20 Illustrations of how fast electron/atoms/molecules can respond to potential gradients (fields)

3, for a conservative force, the force (or force field) is given by the gradient in potential. This is expressed by the equation, ${ }^{7}$

$$
\text { Force }=-\vec{\nabla}[\text { Potential }(x, y, z)]
$$

The negative sign in Eq. (2.23) ensures that the force (acting on the electrons/ atoms/molecules) is always in a direction of lower potential.

Since degradation rate is ultimately related to how fast electrons/atoms/molecules can respond to potential gradients, in Fig. 2.20, we show some rough rules of thumb for how fast electrons/atoms/molecules can respond to potential gradients (fields). For example, electron clouds about the nucleus of an atom can shift on the order of femtoseconds when exposed to electrostatic gradients (electric fields). Bond stretching occurs on the order of picoseconds when exposed to pressure/stress gradients. Polar molecules (in gaseous form) can respond to electric fields with rotations in nanoseconds. The question of how fast can atoms/ions can diffuse in solids depends strongly on the concentration gradient, material lattice, and temperature. It generally takes very fast diffusers at room temperature (e.g., hydrogen and lithium)—microsecond to diffuse/drift a distance of a single lattice constant. Obviously, for very slow diffusers (large radius atoms in very dense solids) it could take years.

[^0]
[^0]:    ${ }^{7}$ The gradient operator is given by: $\vec{\nabla}=\hat{x} \frac{\partial}{\partial x}+\hat{y} \frac{\partial}{\partial y}+\hat{z} \frac{\partial}{\partial z}$.# 8 Imperfect Materials/Devices 

Before we leave this chapter, we want to address an important question for reliability: since energy transfer to a system (such as work done on the system) can produce more order, is it possible to create perfect order in a material? To answer this question, we need to discuss the idea of lowest energy state versus lowest freeenergy state.

As illustrated in Fig. 2.21, with a negative bonding energy of $\left(-E_{\text {bond }}\right)$, a lower internal energy state $U$ is created when: (a) an electron binds with a proton, (b) two hydrogen atoms bond to form a $\mathrm{H}_{2}$ molecule, or (c) many atoms bond to form a crystalline solid (Fig. 2.20c). Thus, lower and lower internal energy $U$ is achieved with more and more bonding. The very lowest internal energy $U$ configuration would be achieved with a perfect crystalline formation, as illustrated in Fig. 2.21c. However, this perfect crystal, while it may be the lowest internal energy state $U$, may not be the lowest free-energy state $G$.

In Fig. 2.22a we show a perfect lattice, while in Fig. 2.22b we show the same lattice but with a single missing atom (called a vacancy). Is it possible that the lattice with a defect could actually have a lower free energy?

Let us first consider Fig. 2.22a and assume that each bond leads to a lower energy by an amount of $\left(-E_{\text {bond }}\right)$. Thus, the internal energy of the perfect crystal can be written as,


Fig. 2.21 System internal energy $U$ can be lowered through: (a) binding energy of atoms, (b) bond energy of molecules, (c) bonding energy of solids

Fig. 2.22 (a) Perfect crystal and (b) crystal with missing atom. Defect shown is usually referred to as a vacancy

$$
U=N_{\text {bonds }} \times\left(-E_{\text {bond }}\right)
$$

Let us now consider Fig. 2.22b. With the introduction of a missing atom (single vacancy), bonds must be broken and thus the internal energy will increase by an amount $\Delta \mathrm{E}$ with the introduction of each vacancy. The increase in internal energy of the solid due to the introduction of a number of vacancies $n$ can be written as:

$$
\Delta U=n \cdot \Delta E
$$

From Eq. (2.6), the change Gibbs free energy is given by,

$$
\Delta G=\Delta U-T \Delta \mathcal{S}=n \cdot \Delta E-T \Delta \mathcal{S}
$$

The change in entropy $\Delta \mathrm{S}$ for the material, with the introduction of the $n$ vacancies into a material with N lattice sites, can be described by the Boltzmann relation,

$$
\Delta \mathcal{S}=K_{B} \ln (\mathcal{W})
$$where W represents to the number of possible distinguishable vacancy locations in the lattice and $\mathrm{K}_{\mathrm{B}}$ is Boltzmann's constant ( $8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}$ ). As can be verified by inspection, W is given by

$$
\mathcal{W}=\frac{N!}{n!(N-n)!}
$$

Using Stirling's approximation, ${ }^{8}$ one obtains:

$$
\begin{aligned}
\Delta G & =n \cdot \Delta E-K_{B} T \ln |\mathcal{W}| \\
& =n \cdot \Delta E-K_{B} T[N \ln (N)-n \ln (n)-(N-n) \ln (N-n)]
\end{aligned}
$$

Finding the number of vacancies that will minimize the free energy, we obtain:

$$
\frac{\partial(\Delta G)}{\partial n}=0 \Rightarrow \frac{n}{N-n}=\exp \left(-\frac{\Delta E}{K_{B} T}\right)
$$

Since we expect that $\mathrm{N} \gg \mathrm{n}$, then

$$
\frac{n}{N} \approx \exp \left(-\frac{\Delta E}{K_{B} T}\right)
$$

Therefore, when the material is in equilibrium, the lowest free energy state for the material occurs when some vacancies/defects exist in the material. If the increase in energy $\Delta \mathrm{E}$ (needed to introduce a single vacancy/defect into the lattice) is relatively small, then the number of vacancies/defects can be significant. Also, as the temperature increases, the number of vacancies/defects in equilibrium will increase. Thus, we must conclude that while it is theoretically possible to fabricate a perfect material, it is extremely improbable. The inevitable presence of defects in a material can often impact/dominate a material's electrical, mechanical, chemical, and electrochemical properties. Thus, pre-existing defects in a material can impact the material's degradation rate and thus device reliability. This is discussed in much more detail in Chap. 13.

Before leaving this section (on the number of defects needed in a lattice for equilibrium) it is very important to recognize that a fundamental degradation mechanism is at play. If we put a lattice (with an initial equilibrium number of lattice defects) under stress (mechanical and/or electrical), then the number of defects needed for the new equilibrium state will increase. This is because the stress tends to increase the potential energy of the lattice thus making the lattice more unstable. The increase in lattice potential energy serves to lower the activation energy $\Delta \mathrm{E}$ needed for defect formation; and, according to Eq. (2.31), the number of defects in the new equilibrium state will increase. Therefore, in an effort to relieve lattice stress,

[^0]
[^0]:    ${ }^{8}$ Stirling's approximation: $\ln (\mathrm{m}!) \approx \min (\mathrm{m})-\mathrm{m}$, where $\mathrm{m} \gg 1$.

Fig. 2.23 Stable elements are shown with solid curve. Shaded areas indicate nuclide instability regions. Note that stability for the lighter elements occurs when the number of protons and neutrons are equal. For heavier elements, stability occurs when the number of neutrons exceeds the number of protons. However, too many neutrons can also produce nuclide instability
more lattice defects will be generated spontaneously in order to bring the stressed lattice into the new equilibrium state (the state with lowest Gibbs Free Energy). Stress-induced lattice defect generation is an important degradation mechanism for the lattice.

# 9 Nuclide Degradation 

In this chapter, the fundamental instability of materials fabricated into metastable states has been discussed. Before leaving this chapter, the author would be remiss if another fundamental instability was not discussed-metastable states for nuclides. Astrophysics tells us that all the elements on earth (both light and heavy elements) are the result of exploding stars. Since the earth is roughly 4 billion years old, the very unstable isotopes have long since decayed leaving mostly stable elements (lucky for us). The stability curve for the elements is shown in Fig. 2.23.

We should recall that attractive forces tend to decrease the potential energy of a system of particles; repulsive forces tend to increase the potential energy. Since protons are positively charged, the Coulomb repulsion increases the potential energy for a collection of protons. However, at very short distances ( femtometer) strong nuclear attractive forces tend to dominate and this lowers the potential energy thus making binding of the nucleons possible. The stability of the nucleus is further enhanced by adding neutrons (neutral charge) to the nucleus. The neutrons tend to modulate the repulsive Coulomb forces of the protons. The ratio of protons toneutrons needed to produce stability in the nucleus tends to reduce from 1 (for the lightest elements) to $<1$ for heavy elements (as shown in Fig. 2.23). However, it is very important to note that too many neutrons can also produce instability issues for the nuclides as is shown in the shaded regions for the stability curve.

The above paragraph tends to explain why certain nuclides are stable, so what produces nuclide instability? First, since protons have like charge, and the repulsive Coulomb forces are conservative, the potential energy must increase for a collection protons in nucleus. Second, since the nucleons (protons and neutrons) have a spin of $1 / 2$ then they are Fermions and the Pauli Exclusion Principle forbids two Fermions from having the same set of quantum numbers. Thus, the Pauli Exclusion Principle effectively creates strong repulsion among the nucleons and this serves to raise their potential energy. Therefore, due to Coulomb interactions and due to the Pauli Exclusion Principle, added nucleons to the nucleus must go into higher and higher energy states (states with higher potential energy). Like all metastable states, a rise in potential energy can make a nucleus less stable.

The shell model of the nucleus (with spin-orbit interaction) is similar to the shell model of the atom; the ground state of the nucleus (first shell) can contain 2 protons, 2nd shell can contain 6 protons, 3rd shell can contain 12 protons, 4th shell can contain 8 protons, 5th shell can contain 22 protons, 6th shell can contain 32 protons, 7th shell contains 44, 8th shell contains 58, etc. Similar to atoms, completed shells tend to be more stable. Therefore, the magic proton numbers for greatest nuclide stability are: $2,8,20,28,50,82,126,184$, etc., with the appropriate number of neutrons implied. These magic numbers for protons in the nucleus produce the most tightly bound nucleus. Thus, these nuclides will have the greatest binding energy (lowest potential energy) and are therefore very stable.

The binding energy per nucleon is shown in Fig. 2.24. We see that the binding energy per nucleon tends to reduce for very heavy elements. Another way of viewing this-the potential energy for the nucleus is increasing due to Coulomb repulsion and Pauli repulsion, thus making the nucleus less stable.

Finally, let us now explore a fundamental nuclide instability; one that is very important for nuclear engineering. Consider the reaction whereby an alpha particle (helium nucleus) slams into a thorium isotope (in an accelerator or within a star),

$$
{ }_{90}^{231} \operatorname{Th}+{ }_{2}^{4} \mathrm{He} \rightarrow{ }_{92}^{235} U
$$

As shown in Fig. 2.25, as the alpha particle $\left(Z_{1}=+2\right)$ approaches the thorium nucleus $\left(Z_{2}=+90\right)$, the work against the Coulomb repulsive conservative force increases the potential energy of uranium nucleus by,

$$
V(r)=Z_{1} Z_{2}\left(\frac{1}{4 \pi \varepsilon_{0}} \frac{q^{2}}{R}\right)
$$

where q is a positive electronic charge and $\varepsilon_{0}$ is the permittivity of free space. The nuclear radius R can be approximated by the equation,

Fig. 2.24 The nuclear binding energy per nucleon in the nucleus. Note that for very heavy elements (number of nucleons $>60$ ), the binding energy per nucleon decreases. An equivalent way of looking at this-the potential energy per nucleon is increasing as more nucleons are added to higher and higher energy states


Fig. 2.25 High energy alpha particle (He nucleus) approaches a relatively heavy nucleus. If the alpha particle has sufficient energy to overcome the Coulomb barrier, then strong nuclear attractive forces take over at short distances ( $\mathrm{r} \leq \mathrm{R}$ ), thus binding the alpha particle to the nucleus. Due to the Pauli Exclusion Principle, the added alpha particle must reside in unoccupied higher energy binding states for the protons and neutrons. In fact, if the alpha particle in the nucleus is able to reach an energy level E, it can possibly tunnel back out of the nucleus$$
R=(1.1 \mathrm{fm})(Z+N)^{1 / 3}
$$

With a thorium nuclear radius of $\mathrm{R}=6.75 \mathrm{fm}$, the impact of the alpha particle raises the potential energy of the uranium nucleus by at least +43 MeV while the binding energy (due to nuclear strong forces) is lowered by 4 nuclides $\times$ $(-7.5 \mathrm{MeV} /$ nuclide $)=-30 \mathrm{MeV}$. The increase in potential energy has apparently made the uranium isotope ${ }^{235} \mathrm{U}$ less stable. Furthermore, when a neutron is added to the ${ }^{235} \mathrm{U}$, the excess number of neutrons in the nucleus now makes the nucleus very unstable and it splits. The splitting of the ${ }^{235} \mathrm{U}$ nucleus serves to release an enormous amount of energy plus additional neutrons. The released neutrons can potentially be used for a chain nuclear reaction if other ${ }^{235} \mathrm{U}$ nuclei are nearby.

# Bibliography 

Atkins P., The Second Law, Scientific American Books, (W.H. Freeman and Co.), (1984).
Bernstein, J. et. al., Modern Physics, Prentice Hall, (2000).
Desloge, E.: Thermal Physics, Holt, Riehart and Winston, (1968).
Griffiths, D.: Introduction to Quantum Mechanics, Prentice Hall, (1995).
Matare, H.: Defect Electronics in Semiconductors, Wiley-Interscience, (1971).
McPherson, J., Underlying physics of the thermochemical E model in describing low-field timedependent dielectric breakdown in $\mathrm{SiO}_{2}$ thin films, J. Appl. Physics, 84, 1513, (1998).
Resnick, R., Halliday, D. and Krane, K., Physics, Vol.1, $4^{\text {th }}$ Ed., John Wiley and Sons, 1992.
Sears, F. and Salinger, G.: Thermodynamics, Kinetic Theory, and Statistical Thermodynamics, $3^{\text {rd }}$ Ed., Addison-Wesley Publishing, (1975).
Tipler, P. and Llewellyn, R.: Modern Physics, $4^{\text {th }}$ Ed., W.H. Freeman and Company, (2002).# Chapter 3 <br> Time-Dependence of Materials and Device Degradation 

Degradation is seemingly fundamental to all things in nature. Often this is described as one of the consequences of the Second Law of Thermodynamics-entropy (disorder) of isolated systems will tend to increase with time. The evidence for degradation is apparently everywhere in nature. A fresh coating of paint on a house will eventually crack and peel. The finish on a new automobile will oxidize with time. The tight tolerances associated with finely meshed gears will deteriorate with time. The critical parameters associated with precision semiconductor devices (threshold voltages, drive currents, interconnect resistances, capacitor leakage, etc.) will degrade with time. In order to understand the useful lifetime of the device, it is important to be able to model how critically important materials/deviceparameters degrade with time.

## 1 Materials/Device Degradation

We are confronted with the apparent truism-regardless of how carefully crafted a device is at time zero, the materials in the device will degrade with time. The materials degradation will cause some critically important device parameter $S$ to shift/degrade with time as illustrated in Fig. 3.1.

As also illustrated in Fig. 3.1, the critical device parameter can be either increasing or decreasing. The device will of course fail when the level of parameter $S$ degradation becomes too great for the device to properly function. Thus, we have to accept degradation as an axiom: materials will degrade with time and the materials degradation will cause important device parameters to shift/degrade. By carefully recording and modeling the time-dependence of this degradation, a useful device lifetime can be inferred. Thus, while we cannot stop device degradation, we can model the degradation to better understand the degradation rate and its impact on device failure.

Fig. 3.1 Materials degradation in a device can cause a critically important device parameter $S$ to degrade with time. The parameter $S$ can be increasing or decreasing

# 2 Material/Device-Parameter Degradation Modeling 

Reliability concerns arise when some critically important material/device-parameter (e.g., mechanical strength, capacitor leakage, transistor threshold voltage, brakelining thickness, etc.) degrades with time. Let $S$ represent a critically important material/device-parameter. ${ }^{1}$ Let us assume that $S$ changes relatively slowly over the lifetime of the material/device. A Taylor expansion about $t=0$ produces the Maclaurin series:

$$
S(t)=S_{t=0}+\left(\frac{\partial S}{\partial t}\right)_{t=0} t+\frac{1}{2}\left(\frac{\partial^{2} S}{\partial t^{2}}\right)_{t=0} t^{2}+\ldots
$$

It will be assumed that the higher order terms in the expansion can be approximated by simply introducing a power-law exponent $m$ and writing the above expansion in a shortened form:

$$
S=S_{o}\left[1 \pm A_{o}(t)^{m}\right]
$$

[^0]
[^0]:    ${ }^{1} S$, as used in this chapter, is a material/device parameter and should not be confused with $S$ used for entropy in Chap. 2.

Fig. 3.2 Strictly monotonic time-dependence behavior of the power-law model for degradation
where $A_{o}$ is a materials/device-dependent coefficient ${ }^{2}$ and $m$ is the power-law exponent. ${ }^{3}$ Both $A_{o}$ and $m$ are adjustable parameters that can be extracted from observed parameter-degradation data. For $+A_{o}$, the observed parameter $S$ increases strictly monotonically with time. Whereas, for $-A_{o}$, it decreases strictly monotonically with time.

Either an increase in a critical device-parameter $S$ (increase in threshold voltage of a semiconductor device, increase in leakage of a capacitor, increase in resistance of a conductor, etc.) or a decrease in critical-parameter $S$ value (decrease of pressure in a vessel, decrease of spacing between mechanical components, decrease in lubricating properties of a fluid, etc.) can eventually lead to device failure. Since device-failure can result from either increase or decrease of some critically-important materials/ device-parameter $S$, both cases are discussed.

The power-law degradation equation (Eq. (3.2)) describes strictly monotonic parameter-degradation. However, as Fig. 3.2 illustrates, the power-law adjustable parameter " $m$ " in the power-law model permits the model to fit much more complicated degradation.

[^0]
[^0]:    ${ }^{2}$ Note that $\mathrm{A}_{\mathrm{o}}$ is positive and must have the units of reciprocal-time to the mth power.
    ${ }^{3}$ Equation (3.2) was developed as a series expansion. To be more precise, Eq. (3.2) is an exact solution to the Euler differential equation: $d(\Delta S) / d t=m(\Delta S / t)$.

Fig. 3.3 Critical material/device-parameter $S$ is observed to reduce with time

# 2.1 Material/Device-Parameter Decreases with Time 

Shown in Fig. 3.3 is the observed time-dependence of the degradation for a critical device-parameter $S$ for three devices. ${ }^{4}$

Reduction in critically important parameter $S$ can be described by:

$$
S=S_{o}\left[1-A_{o}(t)^{m}\right]
$$

Rearranging terms in Eq. (3.3) and taking the logarithm of both sides of the resulting equation yield,

$$
\ln \left(1-\frac{S}{S_{0}}\right)=m \ln (t)+\ln \left(A_{o}\right)
$$

Using Eq. (3.4), a logarithmic plot for the three devices, shown in Fig. 3.3, is now re-plotted in Fig. 3.4. Note that the unknown parameters in Eq. (3.3) can now be easily extracted from such Ln-Ln plots.

[^0]
[^0]:    ${ }^{4}$ The term device is very general: any apparatus that serves some useful purpose.

Fig. 3.4 Logarithmic plots reveal straight lines with equal slopes $m$ (for the three devices) but each device has a different pre-factor $A_{o}\left(A_{o}\right.$ is said to be materials/device dependent. $A_{o}$ variation will result in a distribution of degradations for the devices, as will be discussed in Chap. 7)

# Example Problem: 1 

The threshold voltage $V_{t h}$, for a semiconductor device, was found to degrade with time $t$ (due to surface inversion) as indicated by the data in the table below.

| Time: $t(h)$ | $\mathrm{V}_{\mathrm{th}}(\mathrm{V})$ |
| :-- | :-- |
| 0 | 0.750 |
| 1 | 0.728 |
| 2 | 0.723 |
| 10 | 0.710 |

(a) Find the power-law exponent $m$ which best describes the degradation of the threshold voltage $\mathrm{V}_{\mathrm{th}}$ data versus time.
(b) Find the complete power-law equation that describes the shift in threshold voltage $\mathrm{V}_{\mathrm{th}}$.
(c) Estimate the value expected for the threshold-voltage after 100 h .

## Solution

(a) Inspecting the data, one can see that the device parameter $\mathrm{V}_{\mathrm{th}}$ is decreasing with time. Thus, power-law model, Eq. (3.3), is used:

$$
V_{t h}=\left(V_{t h}\right)_{o}\left[1-A_{o}(t)^{m}\right]
$$

Rearranging, one obtains:

$$
\frac{\left(V_{t h}\right)_{o}-V_{t h}}{\left(V_{t h}\right)_{o}}=A_{o}(t)^{m}
$$Taking the logarithm of both sides of the above equation, one obtains:

$$
\ln \left[\frac{\left(V_{t h}\right)_{o}-V_{t h}}{\left(V_{t h}\right)_{o}}\right]=m \ln (t)+\ln \left(A_{o}\right)
$$

Using the data in the above table, one can add useful columns to the table as is shown below:

| Time: $t(h)$ | $\mathrm{V}_{\mathrm{th}}(\mathrm{V})$ | $\frac{\left(V_{t h}\right)_{o}-V_{t h}}{\left(V_{t h}\right)_{o}}$ | $\ln (\mathrm{t})$ | $\ln \left[\frac{\left(V_{t h}\right)_{o}-V_{t h}}{\left(V_{t h}\right)_{o}}\right]$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 0.75 | 0.000 |  |  |
| 1 | 0.7275 | 0.030 | 0 | -3.51 |
| 2 | 0.72324284 | 0.036 | 0.693147 | -3.33 |
| 10 | 0.70998871 | 0.053 | 2.302585 | -2.93 |

Thus, plotting the values in the last two columns on the right side of this table, one obtains:

(a) From the above plot, one can see that the slope (power-law exponent $m$ ) is given by: $m=0.25$.
(b) Using Eq. (3.3), the threshold voltage $\mathrm{V}_{\mathrm{th}}$ shift/degradation equation is given by:

$$
V_{t h}=\left(V_{t h}\right)_{0}\left(1-A_{0} t^{m}\right)=(0.75 V)\left[1-\frac{0.03}{(h r)^{0.25}}(t)^{0.25}\right]
$$

(c) The value of the threshold voltage $\mathrm{V}_{\mathrm{th}}$, after $\mathrm{t}=100 \mathrm{~h}$, is expected to be:

$$
V_{t h}=(0.75 V)\left[1-\frac{0.03}{(h r)^{0.25}}(100 h r)^{0.25}\right]=0.68 \mathrm{~V}
$$# 2.2 Material/Device-Parameter Increases with Time 

As previously mentioned, degradation is not always associated with a decrease in a critical parameter $S$.

Device failure can result from an increase in a critically important material/ device-parameter with the increase assumed to be described by:

$$
S=S_{o}\left[1+A_{o}(t)^{m}\right]
$$

where $A_{o}$ is again a materials/device-dependent coefficient and $m$ is the timedependence exponent. Shown in Fig. 3.5 is the time-dependence for the degradation of three devices due to the increase in magnitude of the critical parameter $S$.

Rearranging Eq. (3.5) and taking the natural logarithm of both sides of resulting equation yield,

$$
\ln \left(\frac{S}{S_{0}}-1\right)=m \ln (t)+\ln \left(A_{o}\right)
$$

Using Eq. (3.6), the logarithmic plots for the three devices, with increasing critical parameter $S$ as was shown in Fig. 3.5, are now re-plotted in Fig. 3.6. Note that the unknown parameters in Eq. (3.5) can be easily extracted from such Ln-Ln plots.

Parameter S Increasing With Time


Fig. 3.5 Critical materials/device parameter $S$ is observed to increase with time

Fig. 3.6 Ln-Ln plots reveal straight lines with equal slopes $m$ for the three devices, but each device has a different pre-factor $\mathrm{A}_{\mathrm{o}}$

# Example Problem 2 

During a fatigue study, crack propagation occurred in a metal component. The crack-size was observed to increase with the number of cyclical stress-cycles $\mathrm{N}_{\text {cyc }}$. The crack-propagation data is shown below in the table.

| \# Cycles: $\mathrm{N}_{\text {cyc }}$ | Crack-Size: CS $(\mu \mathrm{m})$ |
| :-- | :-- |
| 0 | 1 |
| 100 | 2 |
| 200 | 9 |
| 300 | 28 |

(a) Find the power-law exponent $m$ which best describes the crack-size CS growth versus number of cycles $\mathrm{N}_{\text {cyc }}$.
(b) Find the complete power-law equation which describes the crack-size CS versus $\mathrm{N}_{\text {cyc }}$.
(c) What is the expected crack-size CS after 500 cycles?

## Solution

(a) Inspecting the data, one can see that the crack-size (CS) is increasing with time. Thus, power-law Eq. (3.5) is used:

$$
C S=(C S)_{o}\left[1+A_{o}\left(N_{c y c}\right)^{m}\right]
$$Rearranging, one obtains:

$$
\frac{C S-(C S)_{0}}{(C S)_{0}}=A_{o}\left(N_{c y c}\right)^{m}
$$

Taking the logarithm of both sides of the above equation, one obtains:

$$
\ln \left[\frac{C S-(C S)_{0}}{(C S)_{0}}\right]=m \ln \left(N_{c y c}\right)+\ln \left(A_{o}\right)
$$

Using the data in the above table, one can add useful columns to the table as is shown in the table below.

|  |  | $\frac{C S-(C S)_{o}}{(C S)_{o}}$ | $\ln \left(\mathrm{N}_{\mathrm{cyc}}\right)$ | $\ln \left[\frac{C S-(C S)_{o}}{(C S)_{o}}\right]$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 1 | 0 |  |  |
| 100 | 2 | 1 | 4.605 | 0.000 |
| 200 | 9 | 8 | 5.298 | 2.079 |
| 300 | 28 | 27 | 5.704 | 3.296 |

Plotting the values in the last two columns, on the right side, of the above table, one obtains:

(a) From the above plot, one can see that the slope (power-law exponent $m$ ) is given by: $m=3$.(b) The crack-size CS increase, Eq. (3.5), is given by:

$$
C S=(C S)_{0}\left[1+A_{0}\left(N_{c y c}\right)^{m}\right)=(1 \mu m)\left[1+\frac{1 x 10^{-6}}{(\text { cycle })^{3}}\left(N_{c y c}\right)^{3}\right]
$$

(c) The value of the crack-size CS, after 500 cycles, is expected to be:

$$
C S=(1 \mu m)\left[1+\frac{1 x 10^{-6}}{(\text { cycle })^{3}}(500 \text { cycles })^{3}\right]=126 \mu m
$$

# 3 General Time-Dependent Degradation Models 

There are many time-dependent forms for degradation. However, generally, one of the following three forms is used: power-law, exponential, or logarithmic. These three forms were selected because they tend to occur rather frequently in nature. The power-law is clearly the more frequently used. If, however, a power-law model gives a rather poor fit to the degradation data, then perhaps the other two models should be investigated. The three degradation models are shown in Table 3.1, as well as how the model parameters can be easily extracted from the observed degradation data.

## 4 Degradation Rate Modeling

The power-law model is one of the most widely used forms for time-dependent degradation. For this reason, special attention is given to this model. For convenience of illustration, let us assume that the critical parameter $S$ is decreasing with time and that $A_{o}=1$. Then Eq. (3.3) reduces to:

$$
S^{*}=1-\frac{S}{S_{o}}=(t)^{m}
$$

In Fig. 3.7 one can see the usefulness and flexibility of the power-law timedependent model. Note that for $\mathrm{m}=1$, one will see the expected linear degradation relationship. For $\mathrm{m}<1$, one can see the tendency for the degradation to saturate for long times. However, for $\mathrm{m}>1$, the degradation increases strongly with time and with no evidence of saturation effects.

The degradation rate is better emphasized when the actual degradation rate R equation is used:

$$
R=\frac{d S^{*}}{d t}=m(t)^{m-1}
$$Table 3.1 Selected time-dependent degradation models


Fig. 3.7 Power-law time-dependent degradation model: (a) for $\mathrm{m}=1$, (b) $\mathrm{m}<1$, and for $\mathrm{m}>1$
The degradation rate, for several values of $m$, is shown in Fig. 3.8. Note that when $\mathrm{m}=1$, a constant degradation rate is expected. For $\mathrm{m}<1$, a decreasing degradation rate is expected. For $\mathrm{m}>1$, an increasing degradation rate is expected. For a decreasing degradation rate, there is at least some hope that the degradation may saturate before causing material/device-failure. For a constant degradation rate, the time-to-failure is easily predicted. For an increasing degradation rate, the degradation is ever increasing, eventually leading to a catastrophic condition. Thus, of the three degradation rate conditions (decreasing, constant, increasing), each of which can produce failure, the increasing degradation rate is clearly the most worrisome.

Fig. 3.8 Degradation rate as predicted by the power-law model: (a) $\mathrm{m}=1$, (b) $\mathrm{m}<1$, and (c) $\mathrm{m}>1$. One can see that $\mathrm{m}=1$ produces a constant degradation rate. $\mathrm{m}<1$ produces a decreasing degradation rate. Whereas, $\mathrm{m}>1$ produces an increasing degradation rate

# Example Problem 3 

(a) In Example Problem 1, it was determined that the threshold-voltage parameter for a semiconductor device was degrading (decreasing) with time. Is the degradation rate, for the threshold-voltage parameter $\mathrm{V}_{\mathrm{th}}$, increasing or decreasing with time?
(b) In Example Problem 2, it was determined that the crack-size parameter for a metal component was degrading (increasing) with the number of cyclical stress-cycles. Is the degradation rate, for the crack-size CS parameter, increasing or decreasing with the number of cycles.

## Solution

(a) It was determined, in Example Problem 1, that the threshold voltage $\mathrm{V}_{\mathrm{th}}$ parameter was decreasing with time according to the equation:

$$
V_{t h}=\left(V_{t h}\right)_{0}\left(1-A_{0} t^{m}\right)=(0.75 V)\left[1-\frac{0.03}{(h r)^{0.25}}(t)^{0.25}\right]
$$

Since the exponent for the degradation is $\mathrm{m}=0.25$ (less than 1 ), then, according to Eq. (3.8), or Fig. 3.8, the degradation-rate for the thresholdvoltage parameter is decreasing with time.(b) It was determined, in Example Problem 2, that the crack-size parameter was increasing with time according to the equation:

$$
C S=(C S)_{0}\left[1+A_{0}\left(N_{c y c}\right)^{m}\right)=(1 \mu m)\left[1+\frac{1 \times 10^{-6}}{(\text { cycle })^{3}}\left(N_{c y c}\right)^{3}\right]
$$

Since the exponent for the degradation is $\mathrm{m}=3$ (greater than 1 ), then, according to Eq. (3.8), or Fig. 3.8, the degradation-rate (crack growth-rate) is increasing (in fact, strongly increasing) with time.

# 5 Delays in the Start of Degradation 

Sometimes materials/devices will be remarkably stable for a period of time $t_{0}$ and then show relatively rapid degradation with time. Examples of this include: a tire that holds stable pressure until a nail punctures the tire, the resistance of a metal conductor is stable until a void starts to forms, the fuel efficiency of an engine until the fuel injector starts to clog, an air-conditioner compressor that works fine until a leak in the coolant system develops, etc. Sometimes, it can be extremely important to be able to identify precisely when the degradation started. ${ }^{5}$

If a time-delay $t_{0}$ exists, before the start of degradation for the important material/ device parameter $S$, then one can write the degradation equation as:

$$
\begin{array}{ll}
S=S_{0} & \text { (for } t \leq t_{0} \\
S=S_{o}\left[1 \pm A_{0}\left(t-t_{0}\right)^{m}\right] & \text { (for } t \geq t_{0} \text { ). }
\end{array}
$$

In the above equation, the + sign is used when S increases with time whereas the sign is used when S decreases with time. Equation (3.8) is very useful in determining the precise time that the instability started. The degradation rate R equation can be used to help pin-point $t_{0}$, the time at which degradation actually started. Taking the derivative of Eq. (3.9) one obtains:

$$
\begin{array}{ll}
R_{1}=\frac{d S}{d t}=0 & \text { (for } t \leq t_{0} \\
R_{2}=\frac{d S}{d t}=( \pm) m S_{o} A_{0}\left(t-t_{0}\right)^{m-1} & \text { (for } t \geq t_{0} \text { ). }
\end{array}
$$

[^0]
[^0]:    ${ }^{5}$ If significant degradation (but not failure) started in the warrantee period, does one have a claim? Sometimes, it can be very important to be able to identify the onset of degradation.Table 3.2 Delayed start $\left(\mathrm{t}_{\mathrm{o}}\right)$ degradation models


Note that:
(a) if $m>1$, then $R_{2}$ goes to zero at $t=t_{0}$;
(b) if $m=1$, then $R_{2}$ is a constant; and
(c) if $m<1$, then $R_{2}$ goes to infinity at $t=t_{0}$.

One can see from the above equations that the rate/slope $R$ of the degradation can be used to find the time-delay $t_{0}$. If one plots the observed degradation rate $R$ versus time $t$, then the time at which the rate $R$ goes to zero, or $R$ goes to infinity, is $t=t_{0}$. If $R$ goes to zero, or infinity, at $t=0$, then $t_{0}=0$ and a time-delay is not needed in the degradation equation. The power-law model with a time-delay $t_{0}$, as well as other models, are shown in Table 3.2.

# Example Problem 4 

The fuel efficiency for a new auto remained very stable during the first 12 months of use. However, after about 1 year of use, a measureable degradation occurred in the efficiency (Eff) as is shown in the below table.

| Time (mo) | Efficiency (MPG) | Time (mo) | $\mathrm{R}=\mathrm{d}(\mathrm{Eff}) / \mathrm{dt}(\mathrm{MPG} / \mathrm{Mo})$ |
| :--: | :--: | :--: | :--: |
| 0 | 22.00 |  |  |
| 2 | 22.00 |  |  |
| 4 | 22.00 |  |  |
| 6 | 22.00 |  |  || 8 | 22.00 |  |  |
| :--: | :--: | :--: | :--: |
| 10 | 22.00 |  |  |
| 12 | 22.00 |  |  |
| 14 | 21.75 | 13 | -0.1264 |
| 16 | 21.42 | 15 | -0.1639 |
| 18 | 21.06 | 17 | -0.1819 |
| 20 | 20.67 | 19 | -0.1947 |
| 22 | 20.26 | 21 | -0.2048 |
| 24 | 19.83 | 23 | -0.2132 |

(a) Pinpoint the time $t_{0}$ that the degradation actually started.
(b) Determine the power-law equation which best-fits the efficiency versus time for the full 24 months of use.

# Solution 

The observed degradation rate R is shown in the below graph.

(a) One can see from the above plot, of degradation rate R versus time, that degradation rate R goes to zero at $\mathrm{t}=\mathrm{t}_{0}=10.5$ months. ${ }^{6}$
(b) Now that the value of the time-delay $t_{0}=10.5$ months has been determined, then one can proceed with finding the best fit parameters $\left(\mathrm{m}, \mathrm{A}_{0}\right)$ as follows:

$$
\text { Eff }=(E f f)_{o}\left[1-A_{0}(t-10.5 M o)^{m}\right] \quad(\text { for } t \geq 10.5 M o)
$$

(continued)

[^0]
[^0]:    ${ }^{6}$ Note that even though the degradation started at 10.5 months, the degradation at 12 months is so small that it went undetected by the measuring instrument.Rearranging and taking the logarithm of both sides, one obtains:

$$
\ln \left[\frac{(E f f)_{0}-E f f}{(E f f)_{0}}\right]=m \ln (t-10.5 M o)+\ln \left(A_{0}\right)
$$

The plot of the data is shown in the graph below.


Therefore, the power-law equation, with time-delay, that best-fits the fuel efficiency data is:

$$
\begin{array}{ll}
E f f=22.0 & (\text { for } t \leq 10.5 M o) \\
E f f=(22.0)\left[1-\frac{1.68 \times 10^{-3}}{(M o)^{1.58}}(t-10.5 M o)^{1.58}\right] & (\text { for } t \geq 10.5 M o)
\end{array}
$$

The plot of the data, and the modeled fit to the data, are shown in the graph below.
# Example Problem 5 

In semiconductor processing, yield (number of electrically good chips on a Si -wafer divided by the total number of chips on a wafer) is a key manufacturing parameter. The yield data is shown below for several weeks. Using the yield-degradation rate, pinpoint when the yield degradation started.

| Time (week) | Yield (\%) |
| :--: | :--: |
| 1 | 68.2 |
| 2 | 67.2 |
| 3 | 68.2 |
| 4 | 67.2 |
| 5 | 68.2 |
| 6 | 67.1 |
| 7 | 65.0 |
| 8 | 64.0 |
| 9 | 60.0 |
| 10 | 55.5 |
| 11 | 53.0 |
| 12 | 48.5 |

## Solution

To find the rate of yield degradation, additional columns are added to the table as is shown below.

| Time (week) | Yield (\%) | Time (week) | $\mathrm{R}=\mathrm{d}($ Yield $) / \mathrm{dt}(\% / \mathrm{Wk})$ |
| :--: | :--: | :--: | :--: |
| 1 | 68.2 |  |  |
| 2 | 67.2 | 1.5 | -1.00 |
| 3 | 68.2 | 2.5 | 1.00 |
| 4 | 67.2 | 3.5 | -1.00 |
| 5 | 68.2 | 4.5 | 1.00 |
| 6 | 67.1 | 5.5 | -1.10 |
| 7 | 65.0 | 6.5 | -2.10 |
| 8 | 64.0 | 7.5 | -1.00 |
| 9 | 60.0 | 8.5 | -4.00 |
| 10 | 55.5 | 9.5 | -4.50 |
| 11 | 53.0 | 10.5 | -2.50 |
| 12 | 48.5 | 11.5 | -4.50 |The plot of the yield-degradation rate is shown below.


One can see that while the degradation rate shows fluctuation from week to week, the average degradation rate was nearly constant through the first five weeks. Between weeks 5 and 7, the average degradation rate changed with time. This helps to pinpoint the time that some process step(s) started to go out of control.

# 6 Competing Degradation Mechanisms 

Competing mechanisms (one mechanism is driving an increase in the critical parameter $S$ while the other mechanism is driving a reduction in $S$ ) can also occur. This can be described in by the equation:

$$
S=S_{o}\left[1+A_{o}(t)^{m_{1}}\right]\left[1-B_{o}(t)^{m_{2}}\right]
$$

where the first term on the right of the above equation is tending to increase the parameter $S$ while the second term on the right is trying to decrease the parameter S. These mechanisms are competing and can produce either a maximum or minimum in the degradation, as is illustrated in Fig. 3.9.

In Fig. 3.9, a maximum occurs in the critical parameter $S / S_{o}$ because of the dominance of the increasing mechanism initially, then the dominance of decreasing mechanism during the later stages. ${ }^{7}$ If the roles are reversed, the decreasing term

[^0]
[^0]:    ${ }^{7}$ An example of competing mechanism comes from the joining/bonding of dissimilar materials. During the bonding of dissimilar metals at high temperatures, inter-diffusion of the two materials is usually required in order to establish good bonding. Initially, this inter-diffusion of materials will cause an increase in bonding strength. However, often during the later stages of inter-diffusion, the bond strength can start to weaken due to Kirkendall voiding.

Fig. 3.9 Maximum or minimum in the degradation parameter $\mathrm{S} / \mathrm{S}_{\mathrm{o}}$ is generally indicative of competing mechanisms: one mechanism driving an increase in $S$ and the other driving a decrease in $S$

Table 3.3 Model parameter extraction method (competing mechanisms)

2. During Later Stages:

$$
\begin{aligned}
& S \cong S_{o}^{\prime}\left[1-B_{o}(t)^{m_{2}}\right] \\
& \text { where : } S_{o}^{\prime}=S_{o}\left[1+A_{o}\left(t_{1}\right)^{m_{1}}\right] \\
& \Rightarrow \ln \left(1-\frac{S}{S_{o}^{\prime}}\right)=\ln \left(B_{o}\right)+m_{2} \ln (t)
\end{aligned}
$$


dominates initially, then the increasing term dominates during the later stages of parameter degradation, and then a minimum will be observed.

Table 3.3 indicates a method that is sometimes useful in separating the problem into early stages of degradation versus the later stages of degradation. If the strengthening term dominates the early stages while the later stages are dominated by the weakening term, then the model parameters can easily be extracted.# Problems 

1. The threshold voltage $\mathrm{V}_{\mathrm{th}}$ for a semiconductor device was observed to degrade with time. The degradation data is shown in the table.

| Time (h) | Vth (V) |
| :--: | :--: |
| 0 | 0.40 |
| 1 | 0.42 |
| 10 | 0.44 |
| 100 | 0.48 |

(a) Find the power-law equation which best-fits the threshold voltage $\mathrm{V}_{\mathrm{th}}$ versus time data.
(b) What is the expected value of the threshold voltage $\mathrm{V}_{t h}$ after 1000 h ?
(c) Is the degradation rate increasing or decreasing with time?

## Answers:

(a) $V_{t h}=0.40 \mathrm{~V}\left[1+\frac{0.05}{(h r)^{0.3}}(t)^{0.3}\right]$
(b) $V_{t h}(t=1000 h r)=0.56 \mathrm{~V}$
(c) Since $m=0.3(<1)$, then degradation rate is decreasing with time.
2. The pressure P of a tire is found to degrade with time according to the table shown.

| Time (day) | $\mathrm{P}\left(\mathrm{lb} / \mathrm{in}^{2}\right)$ |
| :--: | :--: |
| 0 | 32.00 |
| 1 | 30.72 |
| 2 | 30.06 |
| 3 | 29.53 |

(a) Find the power-law equation which best-fits the Pressure $P$ versus time data.
(b) What is the expected value of the Pressure $P$ after 10 days?
(c) Is the degradation rate for the Pressure $P$ increasing or decreasing with time?

## Answers:

(a) $P=32\left(\mathrm{lb} / \mathrm{in}^{2}\right)\left[1-\frac{0.04}{(\text { day })^{0.6}}(t)^{0.6}\right]$
(b) $P(t=10$ day $)=26.9 \mathrm{lb} / \mathrm{in}^{2}$
(c) Since $\mathrm{m}=0.6(<1)$, then degradation rate is decreasing with time.3. A current flows through a precision resistor and it is noted that the value of resistance R for the resistor degrades with time according to the data in the table.

| Time (h) | $\mathrm{R}(\Omega)$ |
| :--: | :-- |
| 0 | 10.00 |
| 1 | 10.02 |
| 5 | 10.22 |
| 10 | 10.63 |

(a) Find the power-law equation which best-fits the resistance R versus time.
(b) What is the expected value of the resistance R after 100 h ?
(c) Is the degradation rate for the resistance R increasing or decreasing with time?

# Answers: 

(a) $R=10.00($ ohm $)\left[1+\frac{0.002}{(h r)^{1.5}}(t)^{1.5}\right]$
(b) $R(t=100 h r)=30.00$ ohm
(c) Since $m=1.5(>1)$, then degradation rate is increasing with time.
4. A metal component is corroding/oxidizing with time. The metal-oxide thickness with time is shown in the table.

| Time (year) | Oxide thickness $\mathrm{T}_{\mathrm{ox}}(\mu \mathrm{m})$ |
| :--: | :--: |
| 0 | 1.00 |
| 1 | 1.90 |
| 2 | 2.27 |
| 3 | 2.56 |

(a) Find the power-law equation which best-fits the oxide-thickness $\mathrm{T}_{\mathrm{ox}}$ versus time.
(b) What is the expected value of the oxide-thickness $\mathrm{T}_{\mathrm{ox}}$ after 10 years?
(c) Is the degradation rate for the oxide-thickness $\mathrm{T}_{\mathrm{ox}}$ increasing or decreasing with time?

## Answers:

(a) $T_{o x}=1.00(\mu m)\left[1+\frac{0.9}{(y r)^{0.5}}(t)^{0.5}\right]$
(b) $T_{o x}(t=10 y r)=3.85 \mu m$
(c) Since $m=0.5(<1)$, then degradation rate is decreasing with time.5. The prostate-specific antigen (PSA) test is routinely used to detect the possibility of prostate cancer. The absolute level of the PSA is expected to be $<4.0 \mathrm{ngm} / \mathrm{ml}$, but the rate of change is also important. Below are the hypothetical PSA levels for a patient over a three-year period. The absolute PSA level is less than $4.0 \mathrm{ngm} / \mathrm{ml}$, but is the rate a concern?
(a) Find the power-law model which best-fits the increase in PSA versus time data.
(b) Is the increase in PSA occurring at an increasing or decreasing rate?

| Time (year) | PSA (ngm/ml) |
| :--: | :--: |
| 0 | 1 |
| 1 | 1.1 |
| 2 | 1.4 |
| 3 | 1.9 |

# Answers: 

(a) $P S A=(P S A)_{0}\left[1+A_{0}(t)^{m}\right]=(1.0 \mathrm{ngm} / \mathrm{ml})\left[1+\frac{0.1}{(y r)^{2}}(t)^{2}\right]$
(b) Since $\mathrm{m}=2(>1)$, the rate of increase for the PSA is very strong and should be noted to the physician.
6. For our nervous system to work properly, the nerve cell must be able to generate a potential difference of about 50 mV . This is done through the differential diffusion rates of sodium (Na-ions) and potassium (K-ions). The ratio of the Na to K in our body is typically $(\mathrm{Na} / \mathrm{K})=31.93$. If this ratio drops to 25.47 , then heart issues (e.g., atrial fibrillation) can sometimes occur.

| Time (year) | $(\mathrm{Na} / \mathrm{K})$ ratio |
| :--: | :--: |
| 0 | 31.97 |
| 1 | 31.61 |
| 2 | 31.56 |
| 3 | 31.43 |

(a) Find the power-law model which best-fits the reduction in ( $\mathrm{Na} / \mathrm{K})$ ratio versus time data.
(b) Is the decrease of the $(\mathrm{Na} / \mathrm{K})$ ratio occurring at an increasing or decreasing rate?

## Answers:

(a) $\left(\frac{N a}{K}\right)=(N a / K)_{0}\left(1-A_{0} t^{m}\right)=(31.97 \mathrm{ngm} / \mathrm{ml})\left[1-\frac{0.01}{(y r)^{0.4}}(t)^{0.4}\right]$
(b) Since $\mathrm{m}=0.4(<1)$, the rate of reduction is decreasing with time.7. The size of an inoperable brain tumor was monitored for 3 months preceding the use of an experimental drug and for 3 months post drug use. The data is shown below.
(a) What is the power-law equation that describes tumor growth prior to experimental drug use?
(b) What is the power-law equation that describes tumor growth versus time after experimental drug use.
(c) Take the ratio of the two growth rates to see if the experimental drug was effective at reducing the tumor growth rate.

| Time (mo) | Tumor size: S (cm) |
| :--: | :--: |
| 0 | 1.00 |
| 1 | 1.10 |
| 2 | 1.20 |
| 3 | 1.30 |
| Drug introduction |  |
| 3 | 1.30 |
| 4 | 1.43 |
| 5 | 1.48 |
| 6 | 1.52 |

# Answers: 

(a) $S_{\text {before drug }}=(1.00 \mathrm{~cm})\left[1+\frac{0.1}{(M o)^{t}}\right]$
(b) $S_{\text {after drug }}=(1.30 \mathrm{~cm})\left[1+\frac{0.1}{(M o)^{0.5}}(t-3 M o)^{0.5}\right] \quad(t \geq 3 M o)$
(c) $\frac{R_{\text {after }}}{R_{\text {before }}}=\frac{d S_{\text {after }} / d t}{d S_{\text {before }} / d t}=\frac{0.65(M o)^{0.5}}{(t-3 M o)^{0.5}} \quad(t \geq 3 M o)$

Note that in the 4th month, after the drug was introduced, the tumor growth rate was $65 \%$ of what it would have been without the drug. In the 5th month, the tumor growth rate is $46 \%$ of what it would have been if no drug was introduced.
8. The pressure P of a toxic gas, in a very large storage vessel, was monitored every month during its 12 month storage and the results are shown below.
(a) Pinpoint the month that a leak started to occur, causing a gradual release of the gas.
(b) What is the power-law equation that best-fits the degradation data?
(c) Children, in a nearby school, had a mysterious illness in month 3. Could this have been due to the gas leak?| Time (mo) | Pressure: P (atm) |
| :--: | :--: |
| 0 | 5.0 |
| 1 | 5.0 |
| 2 | 5.0 |
| 3 | 5.0 |
| 4 | 5.0 |
| 5 | 5.0 |
| 6 | 5.0 |
| 7 | 5.0 |
| 8 | 4.9 |
| 9 | 4.7 |
| 10 | 4.4 |
| 11 | 4.0 |
| 12 | 3.5 |

# Answers: 

(a) $t_{0}=6.6$ months.
(b) $P=5.0 \mathrm{~atm} \quad(t \leq 6.6$ Months $)$
$P=5.0 \mathrm{~atm}\left[1-\frac{1.03 \times 10^{-2}}{(M o)^{2.0}}(t-6.6 M o)^{2.0}\right](t \geq 6.6$ Months $)$
(c) The gas leak did not start until month 6.6. The illness of the children at the local school occurred in month 3.
9. Nuclear decay from a radioactive material exhibits the decay characteristics:

$$
\frac{N}{N_{0}}=\exp \left[-\left(\frac{6.93 \times 10^{-3}}{h r}\right) t\right]
$$

(a) Plot the exponential decay function through the first 100 h .
(b) Find the best-fit power-law model to this exponential function through the first 100 h .
(c) Plot both the exponential and the best-fit power-law model and compare the plots through 100 h .

## Answer:

(b) $\frac{N}{N_{0}}=1-\frac{0.00941}{(h r)^{0.871}}(t)^{0.871}$10. In semiconductor processing, yield (number of electrically good chips on a wafer divided by the total number of chips on a wafer) is a key manufacturing parameter. The yield data is shown below for several weeks. Using the yielddegradation rate, when did the yield start to degrade?

| Time (week) | Yield (\%) |
| :--: | :--: |
| 1 | 52.1 |
| 2 | 52.6 |
| 3 | 52.1 |
| 4 | 51.6 |
| 5 | 52.2 |
| 6 | 51.7 |
| 7 | 52.2 |
| 8 | 51.9 |
| 9 | 51.3 |
| 10 | 50.4 |
| 11 | 49.2 |
| 12 | 47.7 |

Answer: Yield started to degrade between weeks 6 and 8.
11. Thermo-sonic Au ball-bonding to aluminum pads is a common attachment process for silicon chips. If these bonds are stored at high temperatures ( $>150{ }^{\circ} \mathrm{C}$ ), one can observe competing mechanisms: inter-diffusion of the two elements tending to strengthening the bonds initially but Kirkendall voiding tends to weaken the bonds during longer storage times. The bond-strength $S$ data is shown versus the storage time at high temperature in the below table.

Determine the degradation equation for the ball bonds shown.

| Time (s) | Bond strength: S (gm-f) |
| :-- | :--: |
| $0.00 \times 10$ | 20.00 |
| $1.00 \times 10$ | 20.01 |
| $1.00 \times 10^{1}$ | 20.03 |
| $1.00 \times 10^{2}$ | 20.10 |
| $1.00 \times 10^{3}$ | 20.31 |
| $1.00 \times 10^{4}$ | 20.90 |
| $1.00 \times 10^{5}$ | 22.16 |
| $2.00 \times 10^{5}$ | 22.47 |
| $4.00 \times 10^{5}$ | 22.32 |
| $6.00 \times 10^{5}$ | 21.75 |
| $8.00 \times 10^{5}$ | 20.94 |
| $1.00 \times 10^{6}$ | 20.00 |
| $2.00 \times 10^{6}$ | 14.14 |
| $2.20 \times 10^{6}$ | 12.83 |
| $2.30 \times 10^{6}$ | 12.17 || Time (s) | Bond strength: S (gm-f) |
| :-- | :--: |
| $2.40 \times 10^{6}$ | 11.49 |
| $2.50 \times 10^{6}$ | 10.81 |
| $2.60 \times 10^{6}$ | 10.12 |
| $2.70 \times 10^{6}$ | 9.43 |
| $2.80 \times 10^{6}$ | 8.73 |
| $3.00 \times 10^{6}$ | 7.32 |
| $4.00 \times 10^{6}$ | 0.00 |

# Answer: 

$$
S=(22.00 \mathrm{gm} \cdot f)\left[1+\frac{1 \times 10^{-3}}{(\sec )^{0.5}}(t)^{0.5}\right]\left[\left(1-\frac{5 \times 10^{-4}}{(\sec )^{0.5}}(t)^{0.5}\right)\right]
$$

12. A metal-oxide thickness Tox was found to take a logarithmic growth functional form:

$$
\frac{T_{o x}}{\left(T_{o x}\right)_{0}}=1+\ln \left[\left(\frac{1 \times 10^{-2}}{h r}\right) t+1\right]
$$

(a) Plot the logarithmic growth function through the first 100 h .
(b) Find the best-fit power-law model to this logarithmic growth function through the first 100 h .
(c) Plot both the logarithmic and the best-fit power-law model and compare the fits through the first 100 h .

## Answer:

(b) $\frac{T_{o x}}{\left(T_{o x}\right)_{0}}=1+\frac{0.0138}{(h r)^{0.858}} t^{0.858}$# Chapter 4 <br> From Material/Device Degradation to Time-to-Failure 

In Chap. 3, it was suggested that material/device degradation will occur with time and that this continuing degradation will eventually cause device failure. Methods were presented in Chap. 3 which can be used for modeling the time-dependence of degradation. The question that we would like to address in this chapter is-how does one go from the time-dependence of degradation to the time-to-failure for the device? The time-to-failure (TF) equations are critically important, for device failure mechanisms, and will be the focus of the remaining chapters in this book.

## 1 Time-to-Failure (TF)

TF occurs when an important material/device parameter degrades to a point that the device can no longer function properly in its intended application. For an electronic device, this could be the time associated with a $10 \%$ reduction in circuit speed, relative to its initial (time-zero) value. For an automobile tire, this could be the time required for the tire tread to reach $10 \%$ of its original (time-zero) value.

In Chap. 3 it was learned that the degradation of an important material/device parameter $S$ could be modeled with a power-law equation:

$$
S=S_{o}\left[1 \pm A_{o}(t)^{m}\right]
$$

Plus sign $(+)$ is used when the parameter $S$ increases with time while the minus sign $(-)$ is used when the parameter $S$ decreases with time. Solving for time, one obtains:

$$
t=\left[\frac{1}{ \pm A_{o}}\left(\frac{S-S_{o}}{S_{o}}\right)\right]^{1 / m}
$$

Fig. 4.1 Time-to-failure depends on the amount of degradation that can be tolerated in some critically important material/device parameter $S$. Note that for a $20 \%$ decrease in the critically important material/device parameter $S,\left(S / S_{0}=0.8\right)$, the time-to-failure will be different for the three devices versus what it would be for $60 \%$ decrease

Time-to-failure $(t=\mathrm{TF})$ occurs when the material/device parameter shifts by some critical amount such that the device no longer functions properly:

$$
\mathrm{TF}=\left[\frac{1}{\pm A_{0}}\left(\frac{S-S_{0}}{S_{0}}\right)_{\text {crit }}\right]^{1 / m}
$$

One can see, from Eq. (4.3), that the TF increases as the critical amount of allowed parameter degradation increases. Also, TF increases as the exponent $m$ decreases. Note that TF goes to infinity as $m$ goes to zero. Recall that $m=$ 0 means that no degradation is occurring with time, thus TF goes to infinity.

Shown in Fig. 4.1 is a parameter $S$ that is decreasing with time. TF occurs when parameter reaches some critical level.

# Example Problem 1 

In Example Problem 1 in Chap. 3, the important threshold $\mathrm{V}_{\text {th }}$ parameter for a semiconductor device was found to decrease/shift according to the power-law equation:

$$
V_{\mathrm{th}}=\left(V_{\mathrm{th}}\right)_{0}\left(1-A_{0} t^{m}\right)=(0.75 \mathrm{~V})\left[1-\frac{0.03}{(\mathrm{~h})^{0.25}}(t)^{0.25}\right]
$$

Assuming that the maximum threshold voltage $\mathrm{V}_{\mathrm{th}}$ shift that one can tolerate is $20 \%$, before device failure occurs, then what is the TF?# Solution 

Since the threshold voltage $\mathrm{V}_{\mathrm{th}}$ is an important decreasing device parameter, then Eq. (4.3) gives the TF:

$$
\mathrm{TF}=\left[\frac{1}{A_{0}}\left(\frac{\left(V_{\mathrm{th}}\right)_{0}-V_{\mathrm{th}}}{\left(V_{\mathrm{th}}\right)_{0}}\right)_{\mathrm{crit}}\right]^{1 / m}
$$

This equation becomes:

$$
\begin{aligned}
\mathrm{TF} & =\left[\frac{1}{0.03 /(\mathrm{h})^{0.25}}\left(\frac{\left(V_{\mathrm{th}}\right)_{0}-0.8\left(V_{\mathrm{th}}\right)_{0}}{\left(V_{\mathrm{th}}\right)_{0}}\right)_{\mathrm{crit}}\right]^{1 / 0.25} \\
& =\left[\frac{0.2}{0.03 /(\mathrm{h})^{0.25}}\right]^{4} \\
& =1,975.3 \mathrm{~h}
\end{aligned}
$$

In summary, it will take approximately $1,975 \mathrm{~h}$ for this device parameter $\mathrm{V}_{\mathrm{th}}$ to decrease/shift by $20 \%$ and to cause device failure.

Shown in Fig. 4.2 is an important material/device parameter $S$ that is increasing with time. TF occurs when the degradation reaches a critical level.

Parameter S Increasing with Time


Fig. 4.2 Time-To-Failure depends on the amount of degradation that can be tolerated in some critically important material/device parameter $S$. Note that for a $100 \%$ increase in the critically important parameter $S\left(S / S_{0}=2\right)$ the time-to-failure will be different for the three devices versus what it would be for $50 \%$ increase in $S,\left(S / S_{0}=1.5\right)$# Example Problem 2 

In Example Problem 2 in Chap. 3, the important reliability parameter was crack-size (CS) and the crack-size was found to increase with the number of cyclical-stressing cycles $\mathrm{N}_{\text {cyc }}$ according to the power-law equation:

$$
\mathrm{CS}=(\mathrm{CS})_{0}\left[1+A_{0}\left(N_{\mathrm{cyc}}\right)^{m}\right]=(1 \mu m)\left[1+\frac{1 \times 10^{-6}}{(\mathrm{cyc} 1 \mathrm{e})^{3}}\left(N_{\mathrm{cyc}}\right)^{3}\right]
$$

Assuming that the maximum CS can increase by 500 times its original value before the device fails, what is the expected number of cycles-to-failure?

## Solution

Since the CS was found to increase with the number of cyclical-stress cycles, then Eq. (4.3) gives the cycle-to-failure CTF:

$$
\mathrm{CTF}=\left[\frac{1}{A_{0}}\left(\frac{\mathrm{CS}-(\mathrm{CS})_{0}}{(\mathrm{CS})_{0}}\right)_{\mathrm{cnt}}\right]^{1 / m}
$$

This equation becomes:

$$
\begin{aligned}
\mathrm{CTF} & =\left[\frac{1}{1 \times 10^{-6} /(\mathrm{cyc})^{3}}\left(\frac{500(\mathrm{CS})_{0}-(\mathrm{CS})_{0}}{(\mathrm{CS})_{0}}\right)_{\mathrm{cnt}}\right]^{1 / 3} \\
& =\left[\frac{499}{1 \times 10^{-6} /(\mathrm{cyc})^{3}}\right]^{1 / 3} \\
& =793.2 \text { cycles. }
\end{aligned}
$$

In summary, it will take approximately 793 cycles of cyclical stress for the initial CS $(1 \mu \mathrm{~m})$ to propagate to a CS of $500 \mu \mathrm{~m}$ and to cause failure.

## 2 Time-to-Failure Kinetics

In Chap. 3, we discussed the fact that the above degradation parameter $A_{0}$ is, in general, material/microstructure dependent and this can lead to TF values which are device-dependent (as illustrated in Figs. 4.1 and 4.2). However, there are also other very important properties of $A_{0}$ (such as its stress and temperature dependence) that we have not yet discussed. ${ }^{1}$

It is common experience that electrical devices tend to degrade faster as the voltage $V$ and/or temperature $T$ increases. In this case, the degradation parameter

[^0]
[^0]:    ${ }^{1} \mathrm{~A}$ more detailed discussion of degradation kinetics is found in Chap. 9.$A_{0}$ is not only a function of material variations but also a function of the applied voltage and the use temperature: $A_{0}=A_{0}(V, T)$. It is also common experience that mechanical devices tend to degrade faster as the mechanical stress $\sigma$ and the temperature $T$ increases. In this case, $A_{0}$ is not only a function of materials variations but also the applied mechanical stress $\sigma$ and the use temperature $T: A_{0}=A_{0}(\sigma, T)$.

Seldom are devices purely electrical or purely mechanical; they can be more accurately described as electro-mechanical devices. Therefore, for electromechanical devices, the relationship between TF and parameter $S$ degradation is given by:

$$
\mathrm{TF}=\left[\frac{1}{ \pm A_{0}(V, \sigma, T)}\left(\frac{S-S_{0}}{S_{0}}\right)_{\text {crit }}\right]^{1 / m}
$$

Plus sign (+) is used for an increasing parameter $S$ and minus sign (-) is used for a decreasing parameter $S$. One can see, from Eq. (4.4), that TF kinetics (voltage, stress, and temperature dependence) may not have a simple inverse relation with degradation kinetics contained in the degradation parameter $\mathrm{A}_{0}(V, \sigma, T)$. In fact, only for the special case of $m=1$ (constant degradation rate), will TF have a simple inverse relationship with the degradation parameter $A_{0}(V, \sigma, T)$. Therefore, while a critical amount of degradation $\left(\Delta S / S_{0}\right)_{\text {crit }}$ is necessary to produce device failure, one should not expect the TF equation $\operatorname{TF}(V, \sigma, T)$ to necessarily have a simple inverse relation with the degradation kinetics contained in $A_{0}(V, \sigma, T)$.

# Problems 

1. The threshold voltage $V_{\text {th }}$ for a semiconductor device was found to degrade according to the power-law equation:

$$
V_{\mathrm{th}}=0.40 \mathrm{~V}\left[1-\frac{0.05}{(\mathrm{~h})^{0.3}}(t)^{0.3}\right]
$$

Find the time required for threshold voltage to increase by $10 \%$.
Answer: Time required $=10.1 \mathrm{~h}$.
2. The pressure $P$ in a tire was found to degrade according to the power-law equation:

$$
P=32\left(1 \mathrm{~b} / \mathrm{in}^{2}\right)\left[1-\frac{0.04}{(\mathrm{day})^{0.6}}(t)^{0.6}\right]
$$

Find the time required for the pressure $P$ to degrade to $16 \mathrm{lb} / \mathrm{in}^{2}$.
Answer: Time required $=67.3$ days.3. A current flowing through a precision resistor causes the resistance $R$ to rise according to the power-law equation:

$$
R=10.00(\Omega)\left[1+\frac{0.002}{(\mathrm{~h})^{1.5}}(t)^{1.5}\right]
$$

Find the time required for the resistance to increase by $10 \%$.
Answer: Time required $=13.6 \mathrm{~h}$.
4. A metal component was corroding/oxidizing according to the power-law degradation:

$$
T_{\mathrm{ox}}=1.00(\mu m)\left[1+\frac{0.9}{(\text { year })^{0.5}}(t)^{0.5}\right]
$$

Find the time required for the oxide-thickness to increase to 3 times its original thickness.

Answer: Time required $=4.9$ years.
5. The prostate-specific antigen (PSA) values for a certain patient were found to increase according to:

$$
\mathrm{PSA}=(1.0 \mathrm{ngm} / \mathrm{ml})\left[1+\frac{0.1}{(\text { year })^{2}}(t)^{2}\right]
$$

Find the time required for the PSA level to reach $4.0 \mathrm{ngm} / \mathrm{ml}$.
Answer: Time required $=5.5$ years.
6. The ratio of the Na to K in a certain patient's blood was described by:

$$
\left(\frac{\mathrm{Na}}{\mathrm{~K}}\right)=\left(\frac{\mathrm{Na}}{\mathrm{~K}}\right)_{0}\left(1-A_{0} t^{m}\right)=(31.93)\left[1-\frac{0.01}{(\text { year })^{0.4}}(t)^{0.4}\right]
$$

Find the time required for the ratio to degrade to 30.00 .
Answer: Time required $=90$ years.
7. The size of an inoperable brain tumor was found to increase, according to the power-law equation:

$$
S=(1.30 \mathrm{~cm})\left[1+\frac{0.1}{\left(M_{0}\right)^{0.5}}(t)^{0.5}\right]
$$

Find the time required for the tumor to grow in size to 1.6 cm .
Answer: Time required $=5.3$ months.8. The pressure $P$ of a gas in a vessel was found to degrade according to the powerlaw model:

$$
\begin{aligned}
& P=5.0 \mathrm{~atm} \\
& \text { ( } t \leq 6.6 \text { months) } \\
& P=5.0 \mathrm{~atm}\left[1-\frac{1.03 \times 10^{-2}}{(M o)^{2.0}}(t-6.6 M o)^{2.0}\right] \quad(t \geq 6.6 \text { months }) .
\end{aligned}
$$

Find the time required for the pressure to reduce by $5 \%$ of its original value.
Answer: Time required $=8.8$ months.
9. Bond strengths of thermo-sonic bonded Au balls to aluminum pads were found to degrade according to the equation:

$$
S=(20.00 \mathrm{~g}-f)\left[1+\frac{1 \times 10^{-3}}{(\mathrm{~s})^{0.5}}(t)^{0.5}\right]\left[\left(1-\frac{5 \times 10^{-4}}{(\mathrm{~s})^{0.5}}(t)^{0.5}\right)\right]
$$

Find the time required for the bond-strength to reduce to $50 \%$ of its original value.

Answer: Time required $=2.6 \times 10^{6} \mathrm{~s}$.
10. Nuclear decay from a radioactive material exhibited the decay characteristics: (a)

$$
\frac{N}{N_{0}}=\exp \left[-\left(\frac{6.93 \times 10^{-3}}{\mathrm{~h}}\right) t\right]
$$

The nuclear decay can be approximated by the power-law: (b)

$$
\frac{N}{N_{0}}=1-\frac{0.00941}{(\mathrm{~h})^{0.871}}(t)^{0.871}
$$

Using models (a) and (b), find the time required for the material to reduce to $50 \%$ of its original value.

# Answers: 

(a) Exponential Model: Time required $=100 \mathrm{~h}$.
(b) Power-Law Model: Time required $=96 \mathrm{~h}$.
11. A metal-oxide thickness $T_{\mathrm{ox}}$ was found to increase in a logarithmic manner according to:
(a) $\frac{T_{\mathrm{ox}}}{\left(T_{\mathrm{ox}}\right)_{0}}=1+\ln \left[\left(\frac{1 \times 10^{-2}}{\mathrm{~h}}\right) t+1\right]$.

The growth can also be approximated by the power-law:
(b) $\frac{T_{\mathrm{ox}}}{\left(T_{\mathrm{ox}}\right)_{0}}=1+\frac{0.0138}{(\mathrm{~h})^{0.858}} t^{0.858}$.Find the time required, using both models, for the oxide thickness to increase to 2 times its original value.

# Answers: 

(a) Logarithmic Model: Time required $=172 \mathrm{~h}$.
(b) Power-Law Model: Time required $=147 \mathrm{~h}$.# Chapter 5 <br> Time-to-Failure Modeling 

All materials tend to degrade, and will eventually fail, with time. For example, metals tend to creep and fatigue; dielectrics tend to trap charge and breakdown; paint tends to crack and peel; polymers tend to lose their elasticity and become more brittle, teeth tend to decay and fracture; etc. All devices (electrical, mechanical, electromechanical, biomechanical, bioelectrical, etc.) will tend to degrade with time and eventually fail. The rate of degradation and eventual time-to-failure (TF) will depend on the electrical, thermal, mechanical, and chemical environments to which the device is exposed.

## 1 Flux-Divergence Impact on Time-to-Failure

In the case of metals, due to the extended nature of the valence-electron wave functions forming metallic bonds, the bonding of the atoms is relatively independent of the exact location of individual metal ions. This is the reason that metals tend to have ductile and malleable properties. Therefore, it is relatively easy for the metal ions to flow under the presence of an external force. While metal ion movement is necessary for failure, it is not sufficient. For a material to degrade, and eventually fail, a flux divergence in the particle transport is required as illustrated in Fig. 5.1.

By flux divergence, we mean that the flux of particles (number of particles per unit area per unit time) flowing into a region must be greater than or less than the flux of particles leaving the region. A region of voiding or accumulation is depicted in Fig. 5.1 and occurs because of a flux divergence in the particle transport process. This depiction could represent electromigration (EM)-induced voiding leading to an open circuit failure, a buildup of chlorine ions on a bond pad leading to corrosion failure, or the trapping of electrons or holes in a dielectric leading to dielectric breakdown. The flux divergence can be described by Fick's Second Law (which is a statement of the conservation of mass),

Fig. 5.1 Material degradation (voiding or accumulation of material is shown in darker region of volume $V$ of interest) occurs due to a flux divergence. $J_{\text {in }}$ represents the flux of particles into the volume $V$ of interest and $J_{\text {out }}$ represents the flux of particles out. The volume $V$ of interest is bounded by a surface of area $A$. Flux divergence occurs if $J_{\text {in }} \neq J_{\text {out }}$

$$
\vec{\nabla} \cdot \vec{J}(x, t)=-\frac{\partial \rho(x, t)}{\partial t}
$$

where $J(x, t)$ represents the particle flux at the specified coordinates $x\left(=x_{1}, x_{2}, x_{3}\right)$ and time $t$, and $\rho(x, t)$ represents the density of such particles. Integrating both sides over the observation volume $V$ and then using the divergence theorem, ${ }^{1}$ one can express Eq. (5.1) in integral form,

$$
\int \vec{J} \cdot \mathrm{~d} \vec{A}=-\frac{\mathrm{d} N(t)}{\mathrm{d} t}
$$

where $N$ represents the total number of particles contained in the volume $V$ of interest which is bounded by a closed surface of area $A$.

In analogy with reaction-rate theory, it is convenient to think of the voiding (or accumulation) in terms of a reaction-rate equation,

$$
\frac{\mathrm{d} N(t)}{\mathrm{d} t}=-k(t) N(t)
$$

where $k(t)$ is the reaction-rate constant for failure. Comparing Eqs. (5.2) and (5.3), one obtains a relationship between the reaction-rate constant and the flux divergence,

$$
k(t)=\frac{\int \vec{J}(x, t) \cdot \mathrm{d} \vec{A}}{N(t)}
$$

In this text, the reaction-rate constant, ${ }^{2}$ given by Eq. (5.4), will be referred to as a degradation-rate constant. One can see clearly that the degradation-rate constant is

[^0]
[^0]:    ${ }^{1}$ The divergence theorem states that: $\int_{V} \vec{\nabla} \cdot \vec{J} \mathrm{~d} V=\int_{A} \vec{J} \cdot \mathrm{~d} \vec{A}$, where $V$ is the volume of interest which is bounded by a surface of area $A$.
    ${ }^{2}$ The reaction-rate constant, in many cases, may not really be constant. It may, in general, be a function of time.directly proportional to the net flux of particles crossing the boundary area $A$ enclosing the volume $V$ of interest. Thus, a flux divergence is needed to produce material degradation (and material degradation is needed to eventually cause device failure). Also, $k$ can be either positive or negative depending on the details of the flux divergence; thus, Eq. (5.3) can be used to describe either accumulation or depletion of particles. The general solution to Eq. (5.3) can be found by separating the variables and integrating,

$$
\int_{N(0)}^{N(t)} \frac{\mathrm{d} N}{N}=-\int_{0}^{t} k(t) \mathrm{d} t
$$

giving:

$$
\frac{N(t)}{N(0)}=\exp \left[-\int_{0}^{t} k(t) \mathrm{d} t\right]
$$

Failure is expected at time $t=\mathrm{TF}$, when the ratio $N(t=\mathrm{TF}) / N(0)$ reaches some critical fraction $f_{\text {crit }}$. This gives:

$$
f_{\text {crit }}=\frac{N(\mathrm{TF})}{N(0)}=\exp \left[-\frac{\int_{0}^{\mathrm{TF}} k(t) \mathrm{d} t}{\int_{0}^{\mathrm{TF}} \mathrm{~d} t} \mathrm{TF}\right]
$$

One will note that, in Eq. (5.7), ${ }^{3}$ the time-averaged value of the degradation-rate constant $\langle k\rangle$ appears where:

$$
\langle k\rangle=\frac{\int_{0}^{\mathrm{TF}} k(t) \mathrm{d} t}{\int_{0}^{\mathrm{TF}} \mathrm{~d} t}
$$

Using Eqs. (5.4) and (5.8), and solving Eq. (5.7) for TF, one obtains the TF equation:

$$
\mathrm{TF}=\frac{\ln \left(1 / f_{\text {crit }}\right)}{\left\langle\frac{\int J(x, t) \cdot \mathrm{d} A}{N(t)}\right\rangle}
$$

Remember that the brackets $\rangle$, in the above equation, represent the timeaveraged value of the quantities enclosed. The above equation shows explicitly

[^0]
[^0]:    ${ }^{3}$ We have inserted the identity: $\mathrm{TF}=\int_{0}^{\mathrm{TF}} \mathrm{d} t$.that a flux divergence in the particle transport is required to produce failure. The equation also shows that the impact of the flux divergence is somewhat mitigated by the number of atoms in failing volume. For example, with voiding-induced failure, if the amount of flux divergence (net number of particles per second leaving the volume) is constant, then one would expect that the time required for $10 \%$ of the atoms to leave the volume of interest would depend on the number of atoms in the volume. This is evident by the fact that a wider metal conductor tends to fail more slowly than a narrow one at the same stress level. ${ }^{4}$ This is indeed the case for crack propagation. If the crack growth rate is constant (flux divergence is constant), then the time required for the crack to propagate through the material increases with its thickness.

For many failure mechanisms, the transport of material can be described as Fickian-like. Fickian transport considers both the drift and diffusion components for the atoms in the transport process:

$$
J(x, t)=\mu \rho(x, t) F-D \frac{\partial \rho(x, t)}{\partial x}
$$

where $\mu$ is the particle mobility, $\rho$ is the particle density, $F$ is the driving force, and $D$ is the diffusivity for the moving particles. The first term on the right-hand side of Eq. (5.10) is referred to as the drift component while the second term is referred to as the diffusion component. The mobility $\mu$ is given by the Einstein relation:

$$
\mu=\frac{D}{K_{B} T}=\frac{D_{0} \exp \left(-\frac{Q_{\text {diffusion }}}{K_{B} T}\right)}{K_{B} T}
$$

where $Q_{\text {diffusion }}$ is the activation energy for diffusion, $T$ is the Kelvin temperature, and $K_{B}$ is Boltzmann's constant ( $8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}$ ). $D_{0}$ is the diffusion coefficient and, for a solid material, can be approximated by,

$$
D_{0}=\frac{v_{0}}{6}\left(r_{0}\right)^{2}
$$

where $v_{0}$ is the vibration/interaction frequency $\left(\sim 10^{13} / \mathrm{s}\right)$ and $r_{0}$ is the mean atom spacing $(\sim 2 \AA$ ) in the material. Equations (5.9), (5.10), and (5.11) suggest that the TF should depend (exponentially) on temperature $T$ and on the driving force $F$.

[^0]
[^0]:    ${ }^{4}$ This is generally true for EM-induced failure in conductors. Wider metal leads, at the same current density stress, tend to last longer. An apparent exception seems to exist in aluminum where very narrow metal leads can last longer than wider metal leads during EM testing. With aluminum, a bamboo-like grain-boundary microstructure can develop when the metal width and thickness are comparable to the Al grain size. Here, however, the amount of flux divergence is no longer constant, but is reduced by the bamboo grain structure thus causing the narrow metal leads to last longer than the wider leads.The force $F$ acting on an atom is, of course, derived from gradients: gradient in electrical potential, gradient in mechanical stress, gradient in chemical potential, etc.

# 2 Stress Dependence and Activation Energy 

It must be emphasized that even if we know the physics behind the driving force $F$, and the activation energy $Q$ for the diffusion process, which should permit accurate modeling of the flux given by Eq. (5.10), seldom do we know the exact details of the flux divergence. The exact details of the flux divergence are often imbedded in the details of the materials microstructure. Thus, Eq. (5.9) is difficult to use when constructing a TF equation. For this reason, it is usually assumed that the flux divergence is related to the applied stress $\xi$ through either a power-law or exponential dependence. Thus, the TF equation Eq. (5.9) is normally assumed to reduce to one of the two following forms:

$$
\mathrm{TF}=A_{0}(\xi)^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$

or

$$
\mathrm{TF}=B_{0} \exp (-\gamma \cdot \xi) \exp \left(\frac{Q}{K_{B} T}\right)
$$

In the above equations, $\xi$ is the generalized stress (the agent which produces material degradation and eventual device TF), $n$ is the power-law exponent, $\gamma$ is the exponential stress parameter, $Q$ is the activation energy, and $A_{0}$ and $B_{0}$ are material/ device-dependent prefactors. The key reliability physics parameters are the TF kinetic values $(n, \gamma, Q)$ and these are determined from actual TF data using the following equations:

$$
n=-\left[\frac{\partial \ln \mathrm{TF}}{\partial \ln \xi}\right]_{T}
$$

or

$$
\gamma=-\left[\frac{\partial \ln \mathrm{TF}}{\partial \xi}\right]_{T}
$$

and $^{5}$

[^0]
[^0]:    ${ }^{5}$ To properly use this equation, the temperature $T$ must be expressed in Kelvin.

Fig. 5.2 Method is illustrated for determination of the power-law exponent $n$ from time-to-failure data. $n$ is dimensionless

$$
Q=k_{B}\left[\frac{\partial \ln \mathrm{TF}}{\partial(1 / T)}\right]_{\xi}
$$

From the above equations, the power-law exponent $n$ is determined from the partial derivative of the logarithm of time-to-failure $\ln (\mathrm{TF})$ with respect to the logarithm of the stress $\ln (\xi)$ while holding the temperature $T$ constant. Thus, to determine $n$, one usually does a $\log -\log$ plot of TF versus the stress variable $\xi$. The slope of the best fitting straight line is $n$. This is illustrated in Fig. 5.2. $n$ is simply a power-law exponent and, as such, $n$ is dimensionless.

The exponential model parameter $\gamma$, according to Eq. (5.14b), is determined from the partial derivative of the $\ln (\mathrm{TF})$ with respect to the stress $\xi$ while holding the temperature $T$ constant. Thus, to determine $\gamma$, one usually does a semi-log plot of TF versus the stress variable $\xi$ : The slope of this best fitting straight line is $\gamma$. The units for $\gamma$ must be in reciprocal stress units so that the product $\gamma \xi$ remains dimensionless. This is illustrated in Fig. 5.3.

The activation energy $Q$ is determined from the partial derivative of the $\ln$ (TF) with respect to the inverse temperature $(1 / T)$ while holding the stress $\xi$ constant. The temperature $T$ must be expressed in Kelvin. Thus, to determine the activation energy $Q$, one usually does a semi-log plot of TF versus the inverse temperature $(1 / T)$. Boltzmann's constant $\left(8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}\right)$ times the slope of this best fitting straight line is $Q$. In this text, the units for $Q$ are normally expressed in electron volts (eV) (see Fig. 5.4).

In Figs. 5.2, 5.3, and 5.4, we have illustrated how the TF kinetics is obtained directly from observed TF data. For these illustrations, the stress dependence for the TF could be described by a power-law model with exponent $n=2$ or with an exponential model with $\gamma=6.1 \times 10^{-3}$ (in units of reciprocal stress). The temperature dependence was described as being Arrhenius-like with an activation energy of $Q=0.52$ (in units of eV ). It should be emphasized that when determining the stress dependence $n$ (or $\gamma$ ), using Eq. (5.14a) and (5.14b), the temperature must be held constant (either physically or mathematically). This can become an important issue ifFig. 5.3 Method is illustrated for determination of the exponential parameter $\gamma$ from time-to-failure data. $\gamma$ must be expressed in the units of reciprocal stress such that the product $\gamma \xi$ is dimensionless


Fig. 5.4 Method is illustrated for determination of the activation energy $Q$, from time-to-failure data. In this text, $Q$ will normally be expressed in the units of electron volts (eV). The temperature must be expressed in Kelvin

the applied stress (such as current density) actually heats the sample. ${ }^{6}$ Therefore, one may wish to determine the activation energy first, using Eq. (5.15), with the stress level held fixed, and then use the activation energy $Q$ to extrapolate to some fixed temperature condition as the stress is changed.

# Example Problem 1 

Metal rods were tested at a constant tensile stress level, and elevated temperature, until the metal rod failed due to creep. The tensile stress levels (in MegaPascals) and the temperatures (in ${ }^{\circ} \mathrm{C}$ ) for the test conditions are shown in the table below, as well as the TF data.

[^0]
[^0]:    ${ }^{6}$ This can be a very important issue if the stress also tends to serve as a significant source of selfheating, e.g., Joule heating can raise the temperature of the conductor when the current density stress is increased in a metal stripe during EM testing. This temperature rise (with the level of current-density stress) must be taken into account when determining the failure kinetics.|  | Mechanical tensile-stress: $\sigma$ |  |  |
| :-- | :-- | :-- | :-- |
| TEMP | 600 MPa | 700 MPa | 800 MPa |
| $500^{\circ} \mathrm{C}$ | - | 29.9 h | - |
| $550^{\circ} \mathrm{C}$ | 18.5 h | 10.0 h | 5.8 h |
| $600^{\circ} \mathrm{C}$ | - | 3.8 h | - |

(a) Assuming a power-law TF model, what is the power-law exponent for the stress $\sigma$ ?
(b) What is the activation energy $Q$ determined from this test?

# Solution 

(a) The stress dependence for the power-law TF model is given by Eq. (5.14a):

$$
n=-\left[\frac{\partial \ln \mathrm{TF}}{\partial \ln \sigma}\right]_{T}
$$

Thus, one needs to perform a $\ln (\mathrm{TF})$ versus $\ln (\sigma)$ plot (while holding the temperature $T$ constant). As an equivalent approach, one can perform a TF versus $\sigma$ plot, using a logarithmic scaling of both axes. This latter approach was chosen and the plot is shown below.


One can see from the above plot that the stress exponent for the power-law is $\mathrm{n}=4$.
(b) After converting the temperature from centigrade to Kelvin, the activation energy $Q$ determination is shown in the plot below. ${ }^{7}$
(continued)

[^0]
[^0]:    ${ }^{7}$ Remember that one must convert the temperature from Centigrade to Kelvin. The conversion equation is $\mathrm{T}(\mathrm{K})=\mathrm{T}\left({ }^{\circ} \mathrm{C}\right)+273$.

# 3 Conservative Time-to-Failure Models 

Since the TF models have adjustable parameters, it is likely that each of the TF models will fit, quite nicely, the accelerated TF data over a limited accelerated stress range. The stress-test range, however, is usually limited because of the time required to take TF data. At the lower stress levels, the test time could easily be years! Therefore, one usually has to model limited TF data, taken under higher stress conditions, and then hope that the model is still valid for extrapolations to much lower stress use conditions. Unless some overriding physics supports one model over the other, then one might want to select the more conservative model (the model which predicts the shortest time to failure). But which model is more conservative?

Shown in Table 5.1 is a set of accelerated stress data (in arbitrary units) with the corresponding TF (also in arbitrary units). We want to obtain the best fitting for each model to the accelerated data and then see which model is more conservative (which model produces the shortest TF when the models are used to predict TF at much lower levels of stress).

The TF data is plotted in Fig. 5.5. Both the exponential and power-law models tend to fit the actual accelerated data extremely well. However, even though both models tend to fit the accelerated data points extremely well, the two models give very different predictions for the TF (when the models are used to extrapolate to much lower values of stress). One can see easily that the exponential model gives a lower estimate of TF (at lower values of stress $\xi$ versus the power-law model. For this reason, we say that the exponential model gives a more conservative estimate of time-to-failure versus the power-law model. One should always remember that the exponential model is more conservative. This may be very important to remember inTable 5.1 Arbitrary accelerated data

| Stress: $\xi$ (arbitrary units) | TF (arbitrary units) |
| :-- | :-- |
| 100 | 1.00 |
| 90 | 1.52 |
| 80 | 2.44 |
| 70 | 4.17 |



Fig. 5.5 The two time-to-failure TF models (exponential and power-law) were used to fit the accelerated stress data shown in Table 5.1. Note that the two models fit the accelerated TF data extremely well at the higher values of stress. At the lower stress levels, the two models generate dramatically different predictions. Note that the exponential model is more conservative (shorter time-to-failure prediction) at lower stress levels
the case of very high-reliability applications, if there is little understanding of the exact physics of failure. An understanding of failure mechanisms, and their physics of failure, can often be very helpful in helping one to decide on which model to use.

In summary, model selection would seem to be easy-just use the more conservative model, right? Well maybe, maybe not. There is the apparent reliability truism: the customer never gets mad if the device lasts longer than you predict. However, the customer may get upset if you were too conservative, during device design and development phases, and your new device does not meet either the cost or performance expectations. Therefore, there should always be an emphasis on understanding the physics of failure so that you can possibly use a more physics-based model selection. Many physics-based models are presented, in Chaps. 11 and 12, to aid you in your model selection. This will give you some degree of confidence in your model selection-knowing that a certain TF model is widely used for the failure mechanism of interest, and under what conditions the model is generally accepted to be valid.# 4 Time-to-Failure Modeling Under High-Stress 

The breakdown strength $\xi_{\mathrm{BD}}$ of a material is defined as the level of stress at which the material is expected to fail instantaneously. Since the material breakdown generally involves atom movement, and atoms cannot move faster than the speed of light, instantaneous behavior is not really possible. By instantaneous, we will mean that the time-to-failure $t_{0}$ at a stress level of $\xi_{\mathrm{BD}}$ is extremely short versus the TF at $50 \%$ of $\xi_{\mathrm{BD}}$. For example, a device/material might be able to operate safely for years at $50 \%$ of $\xi_{\mathrm{BD}}$, but could fail in milliseconds at $\xi_{\mathrm{BD}}$. Usually $\xi_{\mathrm{BD}}$ is determined experimentally by ramping up the level of the stress $\xi$ until $\xi_{\mathrm{BD}}$ is recorded. Ramp-to-failure testing and $t_{0}$ determination is discussed in Chap. 10.

Since stressing close to $\xi_{\mathrm{BD}}$ is obviously in a very high-stress region, a special form of Eq. (5.13b) is sometimes used. One can write Eq. (5.13b) as:

$$
\mathrm{TF}=B_{0}(T) \exp (-\gamma \xi)
$$

By inserting an identity ${ }^{8}$ and rewriting one obtains:

$$
\mathrm{TF}=t_{0}(T) \exp \left[\gamma\left(\xi_{\mathrm{BD}}-\xi\right]\right.
$$

where,

$$
t_{0}(T)=B_{0}(T) \exp \left(-\gamma \xi_{\mathrm{BD}}\right)=B_{0} \exp \left(-\gamma \xi_{\mathrm{BD}}\right) \exp \left(\frac{Q_{0}}{K_{B} T}\right)
$$

One will note that Eq. (5.17) is self-consistent in that: when $\xi=\xi_{\mathrm{BD}}$ then $\mathrm{TF}=t_{0}$, where $t_{0}$ is the TF at breakdown. This will be very useful for interpreting ramp-tofailure test results (Chap. 10). It is also important to note that, experimentally, one finds that $\gamma$ can be temperature dependent, and this temperature dependence has been expressed historically as: ${ }^{9}$

$$
\gamma(T)=\gamma_{0}+\frac{\gamma_{1}}{K_{B} T}
$$

Thus, if $\gamma$ has the expected temperature dependence, as described by Eq. (5.19), then Eq. (5.13b) can be written as

[^0]
[^0]:    ${ }^{8}$ Identity is used: $\exp \left(-\gamma \xi_{\mathrm{BD}}\right) \exp \left(\gamma \xi_{\mathrm{BD}}\right)=1$.
    ${ }^{9}$ In Problem 7, at the end of this chapter, it is shown that a stress-dependent activation energy also develops if a Maclaurin Series expansion is used: $\gamma(T)=a_{0}+\left(a_{1} K_{B}\right) T$.$$
\mathrm{TF}=t_{0} \exp \left[\gamma_{0}\left(\xi_{\mathrm{BD}}-\xi\right)\right] \exp \left(\frac{Q-\gamma_{1} \xi}{K_{B} T}\right)
$$

where $Q=Q_{0}+\gamma_{1} \xi_{\mathrm{BD}}$. Note that Eq. (5.20) suggests that, under very high stress conditions (very close to the breakdown strength of the material), the effective activation energy $Q_{\text {eff }}=Q-\gamma_{1} \xi$ may show a reduction with stress if $\gamma_{1}$ not equal to $0 .{ }^{10}$ A stress-dependent activation energy is widely reported for time-dependent dielectric breakdown TDDB (under high electric-field stress conditions) and for creep-rate studies for metals (under high mechanical stress conditions at high temperatures). Thus, one should consider the possibility of a stress-dependent activation energy when doing extremely high-stress TF testing. The physics behind this stress-dependent activation energy is discussed in detail in Chap. 8.

# Problems 

1. If a constant flux divergence exists, and is given by:

$$
\int \vec{J} \cdot \mathrm{~d} \vec{A}=R=\frac{100,000 \text { Billion atoms }}{\mathrm{s}}
$$

find the time required for $50 \%$ of the atoms to flow out of $1 \mathrm{~cm}^{3}$ of aluminum. Hint:

$$
\begin{aligned}
N_{\text {atoms }} & =\frac{(\text { density })_{\mathrm{A} 1}(\text { Volume })_{\mathrm{A} 1}}{(\text { atomic weight })_{\mathrm{A} 1}}=\frac{\left(2.7 \mathrm{~g} / \mathrm{cm}^{3}\right)\left(1 \mathrm{~cm}^{3}\right)}{(27.0 \mathrm{~g}) /\left(6.02 \times 10^{23} \text { atoms }\right)} \\
& =6.0 \times 10^{22} \text { atoms }
\end{aligned}
$$

Answer: 9.5 years
2. If the reaction-rate constant $k$ shows a monotonic time dependence, then Chap. 2 suggests that one can approximate the time dependence with:

$$
k(t)=k_{0}\left[1 \pm a_{0} t^{m}\right]
$$

where the plus (+) sign is used for an increasing reaction rate constant and a minus (-) sign for a decreasing reaction rate constant. Using Eq. (5.3), show that the TF is given by the transcendental equation:

[^0]
[^0]:    ${ }^{10}$ The occurrence of a stress-dependent activation energy (for high level of stress) is discussed in detail in Chap. 8.$$
\mathrm{TF}=\frac{\ln \left[N_{0} / N(t=\mathrm{TF})\right]}{k_{0}\left[1 \pm a_{0} \frac{(\mathrm{TF})^{m}}{m+1}\right]}
$$

1. EM testing of Cu produced the following table of TF results:

| Electromigration time-to-failure data |  |  |  |
| :-- | :-- | :-- | :-- |
|  | $1 \times 10^{6}\left(\mathrm{~A} / \mathrm{cm}^{2}\right)$ | $2 \times 10^{6}\left(\mathrm{~A} / \mathrm{cm}^{2}\right)$ | $3 \times 10^{6}\left(\mathrm{~A} / \mathrm{cm}^{2}\right)$ |
| $280^{\circ} \mathrm{C}$ | - | 20.3 h | - |
| $300^{\circ} \mathrm{C}$ | 20 h | 10 h | 6.7 h |
| $320^{\circ} \mathrm{C}$ | - | 5 h | - |

(a) Find the power-law exponent $n$ for the current density.
(b) Find the activation energy $Q$ for this failure mechanism.

Answers: (a) $n=1$ (b) $Q=1.0 \mathrm{eV}$
4. Corrosion testing of a metal produced the following table of TF results:

Corrosion time-to-failure data

| Corrosion time-to-failure data |  |  |  |
| :-- | :-- | :-- | :-- |
|  | $60 \% \mathrm{RH}$ | $70 \% \mathrm{RH}$ | $80 \% \mathrm{RH}$ |
| $25^{\circ} \mathrm{C}$ | - | 824 h | - |
| $50^{\circ} \mathrm{C}$ | 332 h | 100 h | 30 h |
| $75^{\circ} \mathrm{C}$ | - | 16.4 h | - |

(a) Find the exponential-dependence parameter $\gamma$ for the humidity.
(b) Find the activation energy for this failure mechanism.

Answers: (a) $\gamma=0.12(\% \mathrm{RH})^{-1}$ (b) $Q=0.7 \mathrm{eV}$
5. Testing for surface-inversion/mobile-ions in ICs produced the following TF results:

| Mobile-Ions time-to-failure data |  |  |  |
| :-- | :-- | :-- | :-- |
|  | 3 V | 6 V | 9 V |
| $60^{\circ} \mathrm{C}$ | - | 67.70 h | - |
| $70^{\circ} \mathrm{C}$ | 40 h | 20 h | 13.30 h |
| $80^{\circ} \mathrm{C}$ | - | 6.33 h | - |

(a) Find the power-law exponent $n$ which describes the voltage dependence.
(b) Find the activation energy $Q$ for this failure mechanism.

Answers: (a) $n=1$ (b) $Q=1.2 \mathrm{eV}$6. Testing for channel hot-carriers in n-type MOSFETs produced the following TF results.

| Hot-Carrier injection time-to-failure data |  |  |  |
| :-- | :-- | :-- | :-- |
|  | $5 \mu \mathrm{~A} / \mu \mathrm{m}$ | $15 \mu \mathrm{~A} / \mu \mathrm{m}$ | $25 \mu \mathrm{~A} / \mu \mathrm{m}$ |
| $25^{\circ} \mathrm{C}$ | - | 5.65 h | - |
| $50^{\circ} \mathrm{C}$ | 324 h | 12 h | 2.60 h |
| $75^{\circ} \mathrm{C}$ | - | 22.90 h | - |

(a) Find the power-law exponent $n$ which describes the substrate current dependence.
(b) Find the activation energy $Q$ for this failure mechanism.

Answers: (a) $n=3$ (b) $Q=-0.25 \mathrm{eV}$
7. Using Eq. (5.13b) for TF, and assuming that the temperature dependence of $\gamma$ can be expressed by the Maclaurin Series:

$$
\gamma(T) \cong a_{0}+\left(a_{1} K_{B}\right) T
$$

show that a stress-dependent activation energy develops of the form:

$$
Q_{\mathrm{eff}}=Q-a_{1}\left(K_{B} T\right)^{2} \xi
$$

# Bibliography 

McPherson, J.: Stress Dependent Activation Energy, IEEE International Reliability Physics Symposium Proceedings, 12(1986).
McPherson, J. and E. Ogawa: Reliability physics and engineering. In: Handbook of Semiconductor Manufacturing Technology, $2^{\text {nd }}$ Edition, CRC Press, (2008).# Chapter 6 <br> Gaussian Statistics: An Overview 

The Gaussian distribution (normal or bell-shaped distribution) is a widely used statistical distribution and it is generally used as the foundation for statistical quality control. Simply measuring the time-zero values of a parameter (resistor values, mechanical tolerances, children heights, class grades on a test, etc.) can result in a distribution of values which can be described by a normal distribution.

## 1 Normal Distribution

The normal distribution $f(x)$ shown in Fig. 6.1 is defined by the equation:

$$
f(x)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left\{-\left[\frac{x-x_{50}}{\sigma \sqrt{2}}\right]^{2}\right\}
$$

For the normal distribution (since it is symmetrical), $x_{50}$ represents the mean $=$ mode $=$ median. In order to be consistent with later chapters in this book, $x_{50}{ }^{1}$ will be referred to as the median ( $50 \%$ of the values are below the median value and $50 \%$ are above). $\sigma$ is the standard deviation ${ }^{2}$ (represents the spread in the data) and can be approximated by $\sigma=x_{50}-x_{16}$, where $x_{16}$ represents the value and where $16 \%^{3}$ of the observations are below this value. Once $x_{50}$ and $\sigma$ are determined from the data, then the full distribution is described by Eq. (6.1).

[^0]
[^0]:    ${ }^{1}$ Mean can be estimated: $x_{50}=\sum_{i=1}^{N} x_{i} / N$, when N is the sample size.
    ${ }^{2}$ Standard deviation can be estimated: $\sigma=\left[\sum_{i=1}^{N}\left(x_{i}-x_{50}\right)^{2} /(N-1)\right]^{1 / 2}$.
    ${ }^{3} \mathrm{~A}$ more precise value is $15.87 \%$.Fig. 6.1 Gaussian (or normal) distribution is illustrated. $x_{50}$ is the mean $=$ mode $=$ median. $68.3 \%$ of observations are between $( \pm) \sigma, 95.5 \%$ of observations are between $( \pm) 2 \sigma$ and $99.7 \%$ of observations are between $( \pm) 3 \sigma$

$x_{50}$ and $\sigma$ can be determined from a plot of the cumulative fraction $F(x)$ :

$$
F(x)=\int_{0}^{x} f(x) \mathrm{d} x
$$

The cumulative (cum) fraction $F$ integral in Eq. (6.2) must be numerically evaluated and is given by:

$$
F(x)=\frac{1}{2} \operatorname{erfc}\left(\frac{x_{50}-x}{\sigma \sqrt{2}}\right) \quad\left(\text { for } x \leq x_{50}\right)
$$

and

$$
F(x)=1-\frac{1}{2} \operatorname{erfc}\left(\frac{x-x_{50}}{\sigma \sqrt{2}}\right) \quad\left(\text { for } x \geq x_{50}\right)
$$

where the erfc stands for the error function complement. Some often used values for the erfc are shown in Table 6.1. In the past, such tables were widely used by engineers. Now, however, ERFC is a standard Excel Function so any arbitrary value is readily available to the engineer.

Table 6.2 is an example of a suggested method for data collection that can be used for relatively easy statistical analysis. In this example, 25 measurements were taken on the shear strength (in units of $\mathrm{gm}-\mathrm{f})^{4}$ of Au ball bonds to aluminum pads on semiconductor chips. These 25 observed measurements (data points) were then

[^0]
[^0]:    ${ }^{4}$ One gm-f equals $9.8 \times 10^{-3} \mathrm{~N}$.Table 6.1 Error function complement (erfc)

| y | erfc(y) | y | erfc(y) |
| :-- | :-- | :-- | :-- |
| 0 | 1.0000 | 1 | 0.1573 |
| 0.1 | 0.8875 | 1.1 | 0.1198 |
| 0.2 | 0.7773 | 1.2 | 0.0897 |
| 0.3 | 0.6714 | 1.3 | 0.0660 |
| 0.4 | 0.5716 | 1.4 | 0.0477 |
| 0.5 | 0.4795 | 1.5 | 0.0339 |
| 0.6 | 0.3961 | 1.6 | 0.0237 |
| 0.7 | 0.3222 | 1.7 | 0.0162 |
| 0.8 | 0.2579 | 1.8 | 0.0109 |
| 0.9 | 0.2031 | 1.9 | 0.0072 |
| 1 | 0.1573 | 2.0 | 0.0047 |

Table 6.2 Statistical data for bond shear strengths

| 25 |  | Shear strength (gm-f) | F | Z-Value |
| :--: | :--: | :--: | :--: | --: |
|  | 1 | 17.07 | 0.028 | $-1.918$ |
|  | 2 | 17.11 | 0.067 | $-1.499$ |
|  | 3 | 18.02 | 0.106 | $-1.246$ |
|  | 4 | 18.20 | 0.146 | $-1.055$ |
|  | 5 | 18.50 | 0.185 | $-0.896$ |
|  | 6 | 18.61 | 0.224 | $-0.757$ |
|  | 7 | 18.70 | 0.264 | $-0.632$ |
|  | 8 | 18.72 | 0.303 | $-0.515$ |
|  | 9 | 18.79 | 0.343 | $-0.406$ |
|  | 10 | 18.96 | 0.382 | $-0.301$ |
|  | 11 | 19.20 | 0.421 | $-0.199$ |
|  | 12 | 19.34 | 0.461 | $-0.099$ |
|  | 13 | 19.42 | 0.500 | 0.000 |
|  | 14 | 19.44 | 0.539 | 0.099 |
|  | 15 | 19.46 | 0.579 | 0.199 |
|  | 16 | 19.55 | 0.618 | 0.301 |
|  | 17 | 19.61 | 0.657 | 0.406 |
|  | 18 | 19.75 | 0.697 | 0.515 |
|  | 19 | 19.81 | 0.736 | 0.632 |
|  | 20 | 19.88 | 0.776 | 0.757 |
|  | 21 | 19.96 | 0.815 | 0.896 |
|  | 22 | 19.98 | 0.854 | 1.055 |
|  | 23 | 20.03 | 0.894 | 1.246 |
|  | 24 | 20.25 | 0.933 | 1.499 |
|  | 25 | 20.26 | 0.972 | 1.918 |

${ }^{a}$ Unbiased estimate: $F=$ (Observation \# - 0.3)/(Sample Size + 0.4)

Fig. 6.2 Normal distribution plotting for data found in Table 6.2
ranked from smallest to largest value. In order to insure that all 25 data points can be used when plotting the data, an unbiased estimate is used for the cumulative fraction failed $F .{ }^{5}$ An unbiased estimate used for $F$ in this text is:

$$
F=\frac{\text { Observation } \#-0.3}{\text { Sample Size }+0.4}
$$

where observation \# is the cumulative number of observations.
The cum fraction $F$ is very useful in that it permits relatively easy plotting of the statistical data and relatively easy parameter $\left(\mathrm{x}_{50}, \sigma\right)$ extraction from the data. The plot of the data (from Table 6.2) is shown in Fig. 6.2, as well as the extracted best fitting normal distribution parameters $\left(x_{50}, \sigma\right)$. Using these best fitting normal distribution parameters $\left(x_{50}, \sigma\right)$, shown in Fig. 6.2, the resulting normal distribution is shown in Fig. 6.3.

In Table 6.3, the $Z$-value is the number of standard deviations associated with a given cum fraction $F$ and can be found from standard lookup tables such as the ones below, or can be easily generated with an EXCEL spreadsheet: to go from $Z$ to $F$, use the EXCEL function $F=$ NORMSDIST $(Z)$; to go from $F$ to $Z$, use the EXCEL function: $Z=\operatorname{NORMSINV}(F)$.

[^0]
[^0]:    ${ }^{5} \mathrm{~A}$ cumulative probability of exactly $F=1$ cannot be plotted. Therefore, in order to ensure that all 25 data points can be plotted, then an unbiased estimate of the cum $F$ is needed. In reliability physics and engineering, Eq. (6.4) is generally used.

Fig. 6.3 Shear strengths (from Table 6.2) presented as a normal distribution

Table 6.3 Conversion tables for $F$ to $Z$ and $Z$ to $F$

| From Cum $F$ to $Z$-values |  | From $Z$-values to Cum $F$ |  |
| :-- | :-- | :-- | :-- |
|  | Standard deviations (Z-values) <br> NORMSINV(F) | Standard deviations <br> Z-value | Cum <br> $F$ NORMSDIST(Z) |
| 0.001 | -3.090232306 | -3.0 | 0.0013 |
| 0.01 | -2.326347874 | -2.5 | 0.0062 |
| 0.1 | -1.281551566 | -2.0 | 0.0228 |
| 0.2 | -0.841621234 | -1.5 | 0.0668 |
| 0.3 | -0.524400513 | -1.0 | 0.1587 |
| 0.4 | -0.253347103 | -0.5 | 0.3085 |
| 0.5 | -1.39214E-16 | 0.0 | 0.5000 |
| 0.6 | 0.253347103 | 0.5 | 0.6915 |
| 0.7 | 0.524400513 | 1.0 | 0.8413 |
| 0.8 | 0.841621234 | 1.5 | 0.9332 |
| 0.9 | 1.281551566 | 2.0 | 0.9772 |
| 0.95 | 1.644853627 | 2.5 | 0.9938 |
| 0.99 | 2.326347874 | 3.0 | 0.9987 |
| 0.999 | 3.090232306 |  |  |
|  |  |  |  |In general, once the normal distribution parameters $\left(x_{50}, \sigma\right)$ are determined, then any other fraction $F$ can be found using the equation:

$$
x_{F}=x_{50}-z_{F} \sigma
$$

The following relations are so frequently used that they are highlighted here:

$$
x_{16 \%}=x_{50}-1 \sigma ; x_{1 \%}=x_{50}-2.33 \sigma ; x_{0.13 \%}=x_{50}-3 \sigma
$$

# 2 Probability Density Function 

The normal distribution, as defined by Eq. (6.1), is a normalized distribution (which means that the total area under the curve is equal to unity). Thus, $f(x)$ can be thought of as a probability density function such that $f(x) \mathrm{d} x$ is the probability of finding a value between $x$ and $x+\mathrm{d} x$, as illustrated in Fig. 6.4. The probability of finding a value in the range, between $x_{1}$ and $x_{2}$, is then given by

$$
P\left(x_{1} \text { to } x_{2}\right)=\int_{x_{1}}^{x_{2}} f(x) d x=F\left(x_{2}\right)-F\left(x_{1}\right)
$$



Fig. 6.4 $f(x) \mathrm{d} x$ represents the probability of observing a value of shear strength between $x$ and $x+\mathrm{d} x$# Example Problem 1 

From Fig. 6.3, normal distribution characteristic parameters that describe the ball bond shear strengths are:

$$
\begin{aligned}
& \mathrm{x}_{50}=19.15 \mathrm{gm}-\mathrm{f} \\
& \text { and } \\
& \sigma=0.96 \mathrm{gm}-\mathrm{f}
\end{aligned}
$$

Find the probability that if one does a single measurement of the shear strength of the ball bonds, a value between 18.0 and $19.0 \mathrm{gm}-\mathrm{f}$ will be obtained.

## Solution

$$
P(18.0 \text { to } 19.0)=\int_{18.0}^{19.0} f(x) \mathrm{d} x=F(19.0)-F(18.0)
$$

The cum fail fractions are given by:

$$
\begin{aligned}
& F(19.0)=\frac{1}{2} \operatorname{erfc}\left(\frac{19.15-19.0}{0.96 \sqrt{2}}\right)=0.438 \\
& \text { and } \\
& F(18.0)=\frac{1}{2} \operatorname{erfc}\left(\frac{19.15-18.0}{0.96 \sqrt{2}}\right)=0.115
\end{aligned}
$$

This gives:

$$
P(18.0 \text { to } 19.0)=F(19.0)-F(18.0)=0.438-0.115=0.323
$$

Therefore, the probability of a single bond-shear measurement producing a value between 18.0 and $19.0 \mathrm{gm}-\mathrm{f}$ is 0.323 (or $32.3 \%$ ).

## 3 Statistical Process Control

Suppose that one knows (maybe from previous experience) that the lower reliable bond strength is $15.5 \mathrm{gm}-\mathrm{f}$ (an under-bonding condition). Likewise, when the timezero bond strength exceeds $24.5 \mathrm{gm}-\mathrm{f}$ (an over-bonding condition), the bond is also unreliable. A very natural question to ask is-how does one statistically characterize the bonding process and is this process under control for reliable use? To answer the above questions, capability parameters $C p$ and $C p k$ are used.$C p$ and $C p k$ are defined quantities:

$$
C p=\frac{(\text { Upper Spec Limit })-(\text { Lower Spec Limit })}{6 \sigma}
$$

and

$$
C p k=C p l=\frac{\left(x_{50}\right)-(\text { Lower Spec })}{3 \sigma}
$$

or

$$
C p k=C p u=\frac{(\text { Upper Spec })-\left(x_{50}\right)}{3 \sigma}
$$

The value of $C p k$ is stated based on whether Eqs. (6.9a) or (6.9b) produces a smaller value. For a perfectly centered process, note that $\mathrm{Cpk}=\mathrm{Cpl}=\mathrm{Cpu}=\mathrm{Cp}$.

# Example Problem 2 

For the ball bonding process illustrated in Fig. 6.3, with ( $\mathrm{x}_{50}=19.15 \mathrm{gm}-\mathrm{f}$, $\sigma=0.96$ ), what is the capability $(C p)$ for this process and how well is it centered $(C p k)$ ? Assume that the lower permitted level is $15.5 \mathrm{gm}-\mathrm{f}$ and the upper permitted level is $24.5 \mathrm{gm}-\mathrm{f}$.

## Solution

The process capability is given by:

$$
C p=\frac{(24.5-15.5) \mathrm{gm}-\mathrm{f}}{6(0.96) \mathrm{gm}-\mathrm{f}}=1.56
$$

The centering for the process is given by:

$$
\begin{aligned}
& C p k=C u p=\frac{(24.5-19.15) \mathrm{gm}-\mathrm{f}}{3(0.96) \mathrm{gm}-\mathrm{f}} \\
& C p k=C p l=\frac{(19.15-15.5) \mathrm{gm}-\mathrm{f}}{3(0.96) \mathrm{gm}-\mathrm{f}}=1.27
\end{aligned}
$$

Therefore, $C p k$ is 1.27 (note that the smaller of the two $C p k$ values is used). $C p k$ is non-symmetrical (since $C p l$ is not equal to $C p u$ ), and is dominated by the lower-end specification.# Example Problem 3 

From the previous example problem, it was determined that $C p k=1.27$ and was dominated by the lower-end of the distribution relative to the specification (spec). (a) What fraction of the bonds has the potential for reliability problems occurring at the lower-end of the spec? (b) Fraction of bonds above the upperend spec?

## Solution

(a) One will need to find the number of standard deviations ( $Z$-value) that corresponds to the lower-end spec. From Fig. 6.2 one obtains:

$$
Z=\left(\frac{1.043}{\mathrm{gm}-\mathrm{f}}\right) x-19.969
$$

With the lower-end spec at $\mathrm{x}=15.5 \mathrm{gm}-\mathrm{f}$, this gives: $Z=-3.803$.
Using the EXCEL NORMSDIST function, one obtains:

$$
F=\operatorname{NORMSDIST}(-3.803)=7.15 \times 10^{-5}
$$

Therefore, the fraction of bonds at reliability risk due to the lower-end spec is 71.5 ppm (parts per million) or $0.00715 \%$ of the bonds.
(b) One needs to find the number of standard deviations ( $Z$-value) at the upper-end specification. Again, using:

$$
Z=\left(\frac{1.043}{\mathrm{gm}-\mathrm{f}}\right) x-19.969
$$

with the upper-end spec of $\mathrm{x}=24.5 \mathrm{gm}-\mathrm{f}$, one obtains: $Z=5.585$.
Using the EXCEL NORMSDIST function, one obtains:

$$
\mathrm{F}=\mathrm{NORMDIST}(5.585)=0.9999999883
$$

Therefore, the fraction of the bonds at reliability risk due to the upper-end spec is $1-F$ where:
$1-F=1-0.9999999883=11.7 \times 10^{-9}$ or 11.7 parts per billion(ppb):# Problems 

1. O-rings (from a manufacturing line) were randomly selected for diameter measurements. The 25 measurements are shown in the below table (all measurements are in mm ). Find the Normal Distribution parameters: median diameter size $\left(x_{50}\right)$ and the standard deviation $\sigma$.

| 181.4 | 173.0 | 172.2 | 173.5 | 180.5 |
| :-- | :-- | :-- | :-- | :-- |
| 187.8 | 178.6 | 170.7 | 179.5 | 186.5 |
| 171.1 | 180.0 | 183.4 | 177.3 | 187.0 |
| 176.7 | 186.1 | 182.5 | 174.2 | 188.7 |
| 184.0 | 185.6 | 190.0 | 175.4 | 189.5 |

Answers: $\mathrm{x}_{50}=180.7 \mathrm{~mm} \sigma=6.6 \mathrm{~mm}$
2. For the O-ring manufacturing process in Problem $1\left(x_{50}=180.7 \mathrm{~mm}, \sigma=6.6\right.$ mm ), find the capability parameters: $C p$ and $C p k$. Assume that the upper spec limit is 215 mm and the lower spec limit is 155 mm .

Answers: $C p=1.52 C p k=1.30$
3. The breakdown-strength distribution for capacitor dielectrics had a median value of $\left(E_{\mathrm{bd}}\right)_{50}=10.50 \mathrm{MV} / \mathrm{cm}$ and a $\sigma=1.8 \mathrm{MV} / \mathrm{cm}$.
(a) Find the fraction of caps with a breakdown $\leq 8 \mathrm{MV} / \mathrm{cm}$.
(b) Find the fraction of caps with a breakdown $\geq 12 \mathrm{MV} / \mathrm{cm}$.

Answers: (a) 0.082 (b) 0.202
4. The rupture strength distribution of water pipes had a median value of (RuptureStress) $)_{50}=900 \mathrm{MPa}$ and a $\sigma=120 \mathrm{MPa}$.
(a) Find the fraction of pipes with a rupture stress of $\leq 600 \mathrm{MPa}$.
(b) Find the fraction of pipes with a rupture stress of $\geq 1,300 \mathrm{MPa}$.

Answers: (a) $6.21 \times 10^{-3}=6,210 \mathrm{ppm}$ (b) $4.29 \times 10^{-4}=429 \mathrm{ppm}$
5. Resistors have a resistance value distribution with a median value of $(R)_{50}=$ $189 \Omega$ and a $\sigma=3.5 \Omega$.
(a) Find the fraction of resistors with a resistance value of $\leq 160 \Omega$.
(b) Find the fraction of resistors with a resistance value of $\geq 200 \Omega$.

Answers: (a) $5.55 \times 10^{-17}=0.555 \times 10^{-10} \mathrm{ppm}$ (b) $8.37 \times 10^{-4}=837 \mathrm{ppm}$
6. A group of patients had a heart rate distribution with a median value $(\mathrm{HR})_{50}=$ 60 beats $/ \mathrm{min}$ and a $\sigma=2$ beats $/ \mathrm{min}$.
(a) Find the fraction of patients with a heart rate of $\leq 50$ beats $/ \mathrm{min}$.
(b) Find the fraction of patients with a heart rate of $\geq 70$ beats $/ \mathrm{min}$.

Answers: (a) $2.87 \times 10^{-7}=0.287 \mathrm{ppm}$ (b) $2.87 \times 10^{-7}=0.287 \mathrm{ppm}$7. Using the breakdown-strength distribution, defined in Problem 3, what are the process capability parameters: $C p$ and $C p k$ ? Assume an upper-level limit of $12 \mathrm{MV} / \mathrm{cm}$ and a lower-level limit of $8 \mathrm{MV} / \mathrm{cm}$.

Answers: $C p=0.37 C p k=0.28$
8. For the rupture strength distribution, defined in Problem 4, what are the process capability parameters: $C p$ and $C p k$ ? Assume an upper-level limit of $1,300 \mathrm{MPa}$ and a lower-level limit of 600 MPa .

Answers: $C p=0.97 C p k=0.83$
9. For the resistor distribution, defined in Problem 5, what are the process capability parameters: $C p$ and $C p k$ ? Assume an upper-level limit of $200 \Omega$ and a lower-level limit of $160 \Omega$.

Answers: $C p=1.90 C p k=1.05$
10. For the heart rate distribution, defined in Problem 6, what are the capability parameters: $C p$ and $C p k$ for this group of patients? Assume an upper-level limit of 70 beats/min and a lower-level limit of 50 beats/min.

Answers: $C p=1.67 C p k=1.67$

# Bibliography 

Ash, C.: The Probability Tutoring Book, IEEE Press, (1993).
Bowker, A. and G. Lieberman: Engineering Statistics, Prentice-Hall Publishing, (1972). Dixon, W. and F. Massey: Introduction to Statistical Analysis, McGraw-Hill Book Co., (1957). Fowler, J., L. Cohen and P. Jarvis: Practical Statistics for Field Biology, John Wiley \& Sons, (1998).

Larsen, R.: Engineering with EXCEL, 2nd Ed., Pearson/Prentice Hall Publishing, (2005). Miller, I. and J. Freund: Probability and Statistics for Engineers, Prentice Hall Publishing, (1977).# Chapter 7 <br> Time-to-Failure Statistics 

When nearly identically processed materials/devices are placed under the same set of stress conditions, they will not fail exactly at the same time. An explanation for this occurrence is that slight differences can exist in the materials' microstructure, even for materials/devices processed nearly identically. This means that not only are we interested in time-to-failure but, more precisely, we are interested in the distribution of times-to-failure. Once the distribution of times-to-failure is established, then one can construct a probability density function $f(t)$ which will permit one to calculate the probability of observing a failure in any arbitrary time interval between $t$ and $t+\mathrm{d} t$, as illustrated in Fig. 7.1.

Historically, two probability density functions have been widely used to describe material/device failures: lognormal and Weibull distributions. Due to their importance in reliability physics and engineering, each distribution will be discussed in some detail. The possibility of having to use multimodal distributions or mixed multiple failure distributions to describe your time-to-failure data is also presented.

## 1 Lognormal Probability Density Function

The lognormal distribution is based on the normal distribution, except that failures are assumed to be logarithmically distributed in time, rather than linearly distributed in time. The use of the lognormal distribution has been very popular for describing time-to-failure for devices where the degradation mechanism is fairly general/extensive in nature and not restricted to simply a very localized/microscopic region of the material. Examples of failure mechanisms where the use of the lognormal distribution has gained popularity include: electromigration-induced failure, corrosioninduced failure, wear-induced failure, creep-induced failure, and fatigue-induced failure. These are discussed in Chaps. 12 and 13.

Fig. 7.1 Probability density function $f(t)$ for failure. $f(t) \mathrm{d} t$ represents the probability of finding a device failure between $t$ and $t+\mathrm{d} t$

The lognormal probability density function is defined by:

$$
f(t)=\frac{1}{\sigma t \sqrt{2 \pi}} \exp \left\{-\left[\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right]^{2}\right\}
$$

where $t_{50}$ is the median time-to-failure and $\sigma$ is the logarithmic standard deviation. ${ }^{1} \sigma$ is usually approximated by $\sigma=\ln \left(t_{50}\right)-\ln \left(t_{16}\right)=\ln \left(t_{50} / t_{16}\right)$ where $t_{16}$ represents the time-to-failure for $16 \%$ of the units. The cumulative failure probability $F$ for the lognormal distribution is given by:

$$
\begin{aligned}
& F(t)=\frac{1}{2} \operatorname{erfc}\left(\frac{\ln \left(t_{50}\right)-\ln (t)}{\sigma \sqrt{2}}\right) \quad\left(\text { for } t \leq t_{50}\right) \\
& F(t)=1-\frac{1}{2} \operatorname{erfc}\left(\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right) \quad\left(\text { for } t \geq t_{50}\right)
\end{aligned}
$$

A systematic approach to collecting cumulative fraction F failure data for statistical analysis is shown in Table 7.1.

The cumulative time-to-failure data (from Table 7.1) is shown in Fig. 7.2 with lognormal probability scaling. One can see from Fig. 7.2 that if normal probability scaling versus $\ln (t)$ is used, a best fitting straight line develops whereby both $t_{50}$ and $t_{16}$ can be read directly from the plot. However, this requires a special scaling, as illustrated in Fig. 7.2, for the cumulative fraction of devices failed. As discussed in

[^0]
[^0]:    ${ }^{1}$ Note that the lognormal distribution has the same general form as does the normal distribution in Chap. 5. The major differences are: (1) the natural logarithm of time $\ln (t)$ is used rather simply the time $t$; and (2) $\sigma$ now represents the logarithmic standard deviation $\sigma=\ln \left(t_{50} / t_{16}\right)$. Also, the $(1 / t)$ in the prefactor of the lognormal distribution is needed to ensure that $f(t) \mathrm{dt}$ will continue to represent the probability of failure. This is due to the fact that $\mathrm{d} \ln (t)=(1 / t) \mathrm{dt}$.Table 7.1 Method for collection of cumulative fraction failure data

| Sample size $=132$ |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
| Time (h) | Number of new failures recorded <br> at each time interval | Cum \# <br> failures | Raw cum <br> fraction | Unbiased $^{\mathrm{a}}$ cum <br> fraction $F$ |
| 500 | 3 | 3 | 0.02 | 0.02 |
| 1,000 | 27 | 30 | 0.23 | 0.22 |
| 1,500 | 37 | 67 | 0.51 | 0.50 |
| 2,000 | 29 | 96 | 0.73 | 0.72 |

${ }^{a}$ Unbiased estimate of $F=($ Cum \# failures - 0.3)/(Sample size +0.4 )


Fig. 7.2 Lognormal plotting of cumulative data from Table 7.1

Chap. 5 for the normal distribution, an alternative method to this type of representation of the lognormal distribution is to simply use the number of logarithmic standard deviations represented by the $Z$-values. Recall that $Z=1$ represents one logarithmic standard deviation $\sigma=\ln \left(t_{50} / t_{16}\right), Z=2$ represents two logarithmic standard deviations, etc. Also recall from Chap. 5, the conversion of cumulative fraction failed $F$ to a $Z$-value, and vice versa, can be easily done using

EXCEL functions: $Z=\operatorname{NORMSINV}(F)$ and $F=\operatorname{NORMSDIST}(Z)$, respectively. Conversions, from $F$ to $Z$ and from $Z$ to $F$, are shown in Table 7.2

The $Z$-values in the table above represent logarithmic standard deviations. Thus, using $Z$ values, the data is replotted in Fig. 7.3.

In general, once the lognormal parameters $\left(t_{50}, \sigma\right)$ are determined, then any other cum fraction F can be obtained using the equation:

$$
t_{F \%}=t_{50} \exp \left[Z_{F} \cdot \sigma\right]
$$

$\sigma$ is calculated using $\sigma=\ln \left(t_{50} / t_{16}\right)$Table 7.2 Lognormal conversion Tables for $F$ to $Z$ and $Z$ to $F$

| $F$ | $Z$-Value | $Z$-Value | $F$ |
| :-- | :-- | :-- | :-- |
| 0.001 | -3.0902 | -3.50 | 0.00023 |
| 0.010 | -2.3263 | -3.00 | 0.00135 |
| 0.100 | -1.2816 | -2.50 | 0.00621 |
| 0.150 | -1.0364 | -2.00 | 0.02275 |
| 0.200 | -0.8416 | -1.50 | 0.06681 |
| 0.250 | -0.6745 | -1.25 | 0.10565 |
| 0.300 | -0.5244 | -1.00 | 0.15866 |
| 0.350 | -0.3853 | -0.75 | 0.22663 |
| 0.400 | -0.2533 | -0.50 | 0.30854 |
| 0.450 | -0.1257 | -0.25 | 0.40129 |
| 0.500 | 0.0000 | 0.00 | 0.50000 |
| 0.550 | 0.1257 | 0.25 | 0.59871 |
| 0.600 | 0.2533 | 0.50 | 0.69146 |
| 0.650 | 0.3853 | 0.75 | 0.77337 |
| 0.700 | 0.5244 | 1.00 | 0.84134 |
| 0.750 | 0.6745 | 1.25 | 0.89435 |
| 0.800 | 0.8416 | 1.50 | 0.93319 |
| 0.850 | 1.0364 | 2.00 | 0.97725 |
| 0.900 | 1.2816 | 2.50 | 0.99379 |
| 0.950 | 1.6449 | 3.00 | 0.99865 |
| 0.990 | 2.3263 | 3.50 | 0.99977 |
| 0.999 | 3.0902 |  |  |



Fig. 7.3 Alternative method for performing a lognormal plot of the time-to-failure data found in Table 7.1. Note that the figure here differs from the normal distribution in that a logarithmic scaling is used for the time axis. $t_{50}$ is extracted from the best fitting linear equation by setting the $Z$-value $=$ $0 . t_{16}$ is obtained by setting the $Z$-value $=-1$.The following relations are so frequently used for the lognormal distribution that they are highlighted here:

$$
t_{16 \%}=\frac{t_{50}}{\exp (1 \sigma)} ; \quad t_{1 \%}=\frac{t_{50}}{\exp (2.33 \sigma)} ; \quad t_{0.13 \%}=\frac{t_{50}}{\exp (3 \sigma)}
$$

# 2 Weibull Probability Density Function 

The Weibull distribution is a weakest-link type distribution. By using the term weakest link, one means that the failure of the whole (for example a chain) is dominated by the degradation rate for the weakest element (one of the links). The Weibull distribution is very popular when plotting semiconductor failure mechanisms such as time-dependent dielectric breakdown (TDDB) where the entire capacitor fails when a very localized region of the capacitor fails. The Weibull distribution tends to fit TDDB data extremely well because one small localized region (usually called a percolation region/path) of the dielectric will tend to degrade more rapidly than the other regions of the dielectric. Thus, the failure of the whole (capacitor) tends to be dominated by the degradation of this weakest link (very localized/ microscopic region within the dielectric). The Weibull distribution is also very useful for system reliability where the entire system fails when one of the constituent components fails.

The Weibull probability density function is defined by

$$
f(t)=\left(\frac{\beta}{\alpha}\right)\left(\frac{t}{\alpha}\right)^{\beta-1} \exp \left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]
$$

where $\alpha$ is referred to as the characteristic time-to-failure and $\beta$ is referred to as the shape (or dispersion or Weibull slope) parameter.

Unlike the lognormal distribution (where the cumulative failure probability $F(t)$ must be obtained by numerical methods represented by the error function), an analytical expression can be found for the cumulative Weibull failure probability function,

$$
F(t)=\int_{0}^{t} f(t) \mathrm{dt}=1-\exp \left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]
$$

Rearranging Eq. (7.6) and taking the appropriate logarithms, one obtains:

$$
\ln [-\ln (1-F)]=\beta[\ln (t / \alpha)]
$$

Fig. 7.4 Weibull probability plotting is shown for data in Table 7.1

One can see that when $F=0.63212$, the left-hand side of Eq. (7.7) goes to zero. It tells us that the characteristic time $\alpha$ is the time for $63.212 \%$ of the devices to fail.

Generally, one simply approximates this and writes the Weibull characteristic time as: $\alpha=t_{63}$. Solving for the Weibull slope $\beta$ in Eq. (7.7), one obtains: ${ }^{2}$

$$
\beta=\frac{\ln [-\ln (1-F)]}{\ln \left(t / t_{63}\right)}
$$

Using the time-to-failure data shown in Table 7.1, a Weibull plot of the data is shown in Fig. 7.4 using a special Weibull probability scaling. The determination of the characteristic time $t_{63}$ and Weibull slope $\beta$, which give the best fitting to the time-to-failure data, are shown. One can see that the Weibull distribution gives a reasonably good fitting to the data. The Weibull parameters that give the best fitting to the data are: a characteristic time of $t_{63}=1,738 \mathrm{~h}$ and a slope of $\beta=3.02$.

An alternative method for performing the Weibull plotting is through the use of Weibits. The conversion of cumulative fraction failed F into Weibits is given by: Weibit $=\ln [-\ln (1-F)]$. Table 7.3 shows a few selected conversions.

The new Weibull plot of the time-to-failure data, found in Table 7.1, is shown in Fig. 7.5.

One should always keep in mind, when working with such Weibull plots, that a Weibit $=0$ (using the best fitting line) corresponds to $t_{63}$. The slope of this best

[^0]
[^0]:    ${ }^{2}$ Note that any cumulative fraction $F$, and its corresponding failure time, may be used in Eq. (7.8) to determine the Weibull slope. The author's preference is to use $F=0.1$ and $t_{10}$. However, this is only a preference, not a requirement.Table 7.3 Conversions from $F$ to Weibits and Weibits to $F$

| Cum $F$ | Weibits $\ln [-\ln (1-F)]$ | Weibits $\ln [-\ln (1-F)]$ | Cum $F$ |
| :-- | :-- | :-- | :-- |
| 0.001 | -6.90725507 | -3.0 | 0.048568007 |
| 0.01 | -4.60014923 | -2.5 | 0.078806345 |
| 0.1 | -2.25036733 | -2.0 | 0.126576982 |
| 0.2 | -1.49993999 | -1.5 | 0.199989287 |
| 0.3 | -1.03093043 | -1.0 | 0.307799372 |
| 0.4 | -0.67172699 | -0.5 | 0.454760788 |
| 0.5 | -0.36651292 | 0.0 | 0.632120559 |
| 0.6 | -0.08742157 | 0.5 | 0.807704354 |
| 0.7 | 0.185626759 | 1.0 | 0.934011964 |
| 0.8 | 0.475884995 | 1.5 | 0.988685714 |
| 0.9 | 0.834032445 | 2.0 | 0.999382021 |
| 0.95 | 1.0971887 | 2.5 | 0.999994881 |
| 0.99 | 1.527179626 | 3.0 | 0.999999998 |
| 0.999 | 1.932644734 |  |  |



Fig. 7.5 Weibull distribution plotting in terms of Weibits (Weibit $=\ln [-\ln (1-F)]$ ). Note that a Weibit $=0$, produces $t_{63}$. The slope of the best linear fitting is $\beta$
fitting line is the Weibull slope $\beta$. Once the Weibull distribution parameters $\left(t_{63}, \beta\right)$ are established, then any other cum fraction can be found using:

$$
t_{F \%}=t_{63} \exp \left\{\frac{1}{\beta} \ln [-\ln (1-F)]\right\}
$$

Some often used values for the Weibull distribution are highlighted here:

$$
t_{10 \%}=\frac{t_{63}}{\exp \left[\frac{2.25}{\beta}\right]} ; \quad t_{1 \%}=\frac{t_{63}}{\exp \left[\frac{4.60}{\beta}\right]} ; \quad t_{0.1 \%}=\frac{t_{63}}{\exp \left[\frac{6.91}{\beta}\right]}
$$# 3 Multimodal Distributions 

Generally, a multimodal failure distribution has more than one failure mechanism present in the single set of time-to-failure data. Sometimes this can be easily detected in the time-to-failure data because the failure mechanisms are slightly separated in time. Often, however, the mechanisms are mixed (occurring during the same time intervals).

### 3.1 Multimodal Distribution (Separated in Time)

When taking time-to-failure data sometimes more than one failure mechanism/ mode can be active during a single reliability test. In semiconductor devices, one might have electromigration, TDDB, and hot-carrier injection (HCI) failures occurring during the same high-temperature operating life test. In mechanical systems, one might have wear, fatigue and corrosion-induced failures occurring during the same test. Multimodal time-to-failure data is shown in Table 7.4.

Evidence for more than one failure mechanism being active during a single reliability test can sometimes be detected as points of inflection in the lognormal and/or Weibull plots. In Table 7.4, time-to-failure data is shown. When this time-tofailure data is plotted in a single lognormal plot ${ }^{3}$ (as shown in Fig. 7.6), at least three failure mechanisms/modes (A, B, and C) are indicated in Fig. 7.6 by the two indicated points of inflection.

As one can see from Fig. 7.6, Mechanism A is responsible for about $22 \%$ of the total failures. Mechanism B is responsible for about $40 \%$ of the total failures and Mechanism C represents about $38 \%$ of the total number of failures. Many times we would like to estimate what distribution A (alone) would look like, or B (alone) or C (alone).

[^0]
[^0]:    ${ }^{3} \mathrm{~A}$ lognormal distribution was used here but a Weibull distribution could have been used and would show similar results.Table 7.4 Multimodal time-to-failure data

| Rank $F$ | Time-to-failure (h) | Normal distribution <br> Z-value NORMSINV( $F$ ) |
| :-- | :--: | :-- |
| 0.01 | 7 | -2.326 |
| 0.05 | 12 | -1.645 |
| 0.10 | 15 | -1.282 |
| 0.15 | 20 | -1.036 |
| 0.20 | 23 | -0.842 |
| 0.25 | 100 | -0.674 |
| 0.30 | 105 | -0.524 |
| 0.35 | 110 | -0.385 |
| 0.40 | 120 | -0.253 |
| 0.45 | 130 | -0.126 |
| 0.50 | 140 | 0.000 |
| 0.55 | 150 | 0.126 |
| 0.60 | 160 | 0.253 |
| 0.65 | 500 | 0.385 |
| 0.70 | 520 | 0.524 |
| 0.75 | 530 | 0.674 |
| 0.80 | 550 | 0.842 |
| 0.85 | 570 | 1.036 |
| 0.90 | 590 | 1.282 |
| 0.95 | 610 | 1.645 |



Fig. 7.6 Two inflection points are evident in this single lognormal plot. The two inflection points suggest the possibility of three failure mechanisms (A, B, C) existing in this single set of time-tofailure dataTable 7.5 Separation of mechanisms for distribution plotting

| Rank <br> $F$ | Adjusted by point of Inflection $\mathrm{F}_{\mathrm{A}}=$ [Rank F]/0.22 | Adjusted by points of Inflection $\mathrm{F}_{\mathrm{B}}=$ [Rank F - 0.22]/ $(0.62-0.22)$ | Adjusted by point of Inflection $\mathrm{F}_{\mathrm{C}}=$ [Rank F - 0.62]/ $(1-0.62)$ | Time- <br> to- <br> failure <br> (h) | Normal distribution Z-value NORMSINV $(F)$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0.01 | 0.05 |  |  | 7 | $-1.691$ |
| 0.05 | 0.23 |  |  | 12 | $-0.748$ |
| 0.1 | 0.45 |  |  | 15 | $-0.114$ |
| 0.15 | 0.68 |  |  | 20 | 0.473 |
| 0.2 | 0.91 |  |  | 23 | 1.335 |
| 0.25 |  | 0.08 |  | 100 | $-1.440$ |
| 0.3 |  | 0.20 |  | 105 | 0.842 |
| 0.35 |  | 0.33 |  | 110 | $-0.454$ |
| 0.4 |  | 0.45 |  | 120 | $-0.126$ |
| 0.45 |  | 0.58 |  | 130 | 0.189 |
| 0.5 |  | 0.70 |  | 140 | 0.524 |
| 0.55 |  | 0.83 |  | 150 | 0.935 |
| 0.6 |  | 0.95 |  | 160 | 1.645 |
| 0.65 |  |  | 0.08 | 500 | $-1.412$ |
| 0.7 |  |  | 0.21 | 520 | $-0.805$ |
| 0.75 |  |  | 0.34 | 530 | $-0.407$ |
| 0.8 |  |  | 0.47 | 550 | $-0.066$ |
| 0.85 |  |  | 0.61 | 570 | 0.267 |
| 0.9 |  |  | 0.74 | 590 | 0.634 |
| 0.95 |  |  | 0.87 | 610 | 1.119 |

The estimated contribution of each of the mechanisms is given by:
Mechanism A

$$
F_{A}=\frac{\operatorname{Rank}(F)}{0.22}
$$

Mechanism B

$$
F_{B}=\frac{\operatorname{Rank}(F)-0.22}{0.62-0.22}
$$

Mechanism C

$$
F_{C}=\frac{\operatorname{Rank}(F)-0.62}{1-0.62}
$$

In Table 7.5, the three separate mechanisms are now shown. Shown in Fig. 7.7 are the individual distributions $\left(t_{50}, \sigma\right)$ for each mechanism.

Fig. 7.7 The three mechanisms, shown in Fig. 7.6, are now separated with the individual $t_{50}$ and $\sigma$ values determined for each

Table 7.6 Mixed multiple failure mechanisms

| Sample size $(\mathrm{SS})=100$ |  |  |  |
| :-- | :-- | :-- | :-- |
| Read points $(\mathrm{h})$ | Cum F | Mechanism A (Cum \# fails) | Mechanism B (Cum \# fails) |
| 0 | 0 | 0 | 0 |
| 500 | 0.02 | 0 | 2 |
| 1,000 | 0.22 | 5 | 17 |
| 1,500 | 0.50 | 12 | 38 |
| 2,000 | 0.72 | 20 | 52 |

# 3.2 Mixed Multiple Failure Mechanisms 

Sometimes multiple failure mechanisms are occurring in a single set of time-tofailure data but with no obvious points of inflection to help separate the mechanisms. In this case, a Kaplan-Meiers type of decoupling method is useful for separating the mechanisms. The method is illustrated below.

Time-to-failure data is shown in Table 7.6. Suppose that, through electrical or physical failure analysis, one can identify that the failures are a mixture of two failure mechanisms: type A and type B. The questions that we would like to answer are: (1) what would the failure distribution look like if only mechanism A was active; and (2) what would the failure distribution look like if only mechanism B was active?

The cum fraction $F_{\mathrm{A}}$ calculation for A-type failures alone is complicated by the fact that the B-type failures are occurring during the same time intervals, and vice versa. For this reason, one will find it more useful to work with the survivor probability $\left(1-F_{\mathrm{A}}\right)$ rather than the cum failure probability $F_{\mathrm{A}}$. One must takeTable 7.7 Decoupling of mixed multiple failure mechanisms

| Sample size $(\mathrm{SS})=100$ |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Read points $(\mathrm{h})$ | Cum F | Mechanism A <br> (Cum \# fails) | Mechanism B <br> (Cum \# fails) | $1-\mathrm{F}_{\mathrm{A}}$ | $1-\mathrm{F}_{\mathrm{B}}$ | $\mathrm{F}_{\mathrm{A}}$ | $\mathrm{F}_{\mathrm{B}}$ |
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| 500 | 0.02 | 0 | 2 | 1.00 | 0.98 | 0 | 0.02 |
| 1,000 | 0.22 | 5 | 17 | 0.94 | 0.80 | 0.06 | 0.20 |
| 1,500 | 0.50 | 12 | 38 | 0.76 | 0.46 | 0.24 | 0.54 |
| 2,000 | 0.72 | 20 | 52 | 0.44 | 0.16 | 0.56 | 0.84 |

into account that both failure mechanisms are occurring during the same intervals and when B-failures occur they are taking away from the effective sample size for $A$, and vice versa.

One can take advantage of the fact that the probability $(1-F)_{i+1}$ of surviving the $i$ th +1 time interval must be equal to the probability $(1-F)_{i}$ of surviving the previous $i$ th time interval times the probability of surviving the present time interval. For example:

$$
\left(1-F_{A}\right)_{i+1}=\left(1-F_{A}\right)_{i}\left(\frac{\mathrm{SS}-(\text { Cum\#for } \mathrm{A})_{i+1}-(\text { Cum\#for } \mathrm{B})_{i+1}}{\mathrm{SS}-(\text { Cum\#for } \mathrm{B})_{i+1}}\right)
$$

and

$$
\left(1-F_{B}\right)_{i+1}=\left(1-F_{B}\right)_{i}\left(\left(\frac{\mathrm{SS}-(\text { Cum\#for } \mathrm{A})_{i+1}-(\text { Cum\#for } \mathrm{B})_{i+1}}{\mathrm{SS}-(\text { Cum\#for } \mathrm{A})_{i+1}}\right)\right.
$$

In the above equations, SS is the beginning sample size (at time zero) and Cum \# represents the cumulative number of failures for each mechanism (A or B) at the indicated time interval. Shown in Table 7.7 is an example of how to use the above equations to generate the individual cumulative failure distributions for mechanisms A and B separately. Figure 7.8 shows the individual Weibull plots ${ }^{4}$ of the failure mechanisms for A and B , along with their characteristic Weibull parameters $\left(t_{63}, \beta\right)$.

Shown in Fig. 7.8 are the Weibull plots of $\mathrm{F}_{\mathrm{A}}$ and $\mathrm{F}_{\mathrm{B}}$ for the separated mechanisms A and B, respectively, for the data taken from Table 7.7. From Fig. 7.8, one can see that the characteristic times $\left(t_{63}\right)$ are different for the two failure mechanisms as well as their Weibull slopes $(\beta)$.

[^0]
[^0]:    ${ }^{4} \mathrm{~A}$ lognormal distribution could also have been used and would produce similar results.

Fig. 7.8 Separation of mixed multiple failure mechanisms is illustrated. The characteristic Weibull parameters are given for each mechanism

# Problems 

1. Time-to-rupture data (from a creep study) are shown for steel rods that were held at a fixed level of stress at very high temperatures until rupture occurred. The time-to-failure data are shown in hours. Find the lognormal $t_{50}$ and $\sigma$ that describes the data.

| 44.0 | 43.3 | 49.0 | 36.0 | 70.8 |
| :-- | :-- | :-- | :-- | :-- |
| 50.3 | 45.2 | 47.4 | 36.3 | 68.3 |
| 65.6 | 51.4 | 43.2 | 39.4 | 70.7 |
| 54.5 | 58.3 | 42.5 | 52.2 | 56.5 |
| 41.1 | 60.2 | 42.7 | 63.6 | 40.0 |

Answers: $t_{50}=49.8 \mathrm{~h}, \sigma=\ln \left(t_{50} / t_{16}\right)=0.22$
2. Given the lognormal distribution $\left(t_{50}=49.8 \mathrm{~h}, \sigma=0.22\right)$ from Problem 1,
(a) What is the expected time for $0.1 \%$ of the steel rods to rupture?
(b) What is the expected time for $99.9 \%$ of the steel rods to rupture?

Answers: (a) $t_{0.1 \%}=25.2 \mathrm{~h}$, (b) $t_{99.9 \%}=98.3 \mathrm{~h}$
3. Given the lognormal distribution $\left(t_{50}=49.8 \mathrm{~h}, \sigma=0.22\right)$ from Problem 1, what fraction of failures occur between 35 and 55 h ?

Answer: 0.6204. Using the time-to-rupture data in problem 1, find the Weibull distribution that gives the best fitting to the data. What are the values for $t_{63}$ and the Weibull slope $\beta$ ?
Answer: $t_{63}=55.2 \mathrm{~h}, \beta=5.4$
5. Given the Weibull distribution $\left(t_{63}=55.2 \mathrm{~h}, \beta=5.4\right)$ from Problem 4,
(a) What is the expected time for $0.1 \%$ of the steel rods to rupture?
(b) What is the expected time for $99.9 \%$ of the steel rods to rupture?

Answers: (a) $t_{0.1} \%=15.4 \mathrm{~h}$, (b) $t_{99.9} \%=79.0 \mathrm{~h}$
6. Given the Weibull distribution $\left(t_{63}=55.2 \mathrm{~h}, \beta=5.4\right)$ from Problem 4, what fraction of the failures occurred between 35 and 55 h ?
Answer: 0.543
7. Using the normal distribution in Chap. 5, fit the data shown in Table 7.1.
(a) What are the values of $t_{50}$ and sigma for the normal distribution?
(b) Compare your normal fit to the lognormal-fit shown in Fig. 7.3. Which distribution gives the better fitting, normal or lognormal?

# Answers: 

(a) $t_{50}=1,573 \mathrm{~h}, \sigma=576 \mathrm{~h}$,
(b) Lognormal distribution gives a better fitting to this data set.
8. The following time-to failure data was collected and found to have two failure mechanisms in the time-to-failure data.

| Cum fraction <br> F | Time-to-failure <br> (h) |
| :-- | :-- |
| 0.05 | 16 |
| 0.09 | 20 |
| 0.15 | 25 |
| 0.22 | 30 |
| 0.3 | 35 |
| 0.38 | 42 |
| 0.45 | 104 |
| 0.51 | 110 |
| 0.63 | 118 |
| 0.68 | 127 |
| 0.75 | 135 |
| 0.82 | 143 |
| 0.87 | 150 |
| 0.9 | 155 |

(a) Perform a lognormal plot of the above data.
(b) Find the point of inflection which separates the two mechanisms.(c) Replot the data for the two mechanisms.
(d) What are the $\left(t_{50}, \sigma\right)$ values for the two mechanisms?

# Answers: 

(b) Point of inflection: $\mathrm{F}=0.42$,
(d) Mechanism A: $t_{50}=27.3 \mathrm{~h}, \sigma=0.4$,

Mechanism B: $t_{50}=131.1 \mathrm{~h}, \sigma=0.17$.
9. Using the time-to failure data (shown in the table in Problem 8):
(a) Perform a Weibull plot of the above data.
(b) Find the point of inflection which separates the two mechanisms.
(c) Replot the data for the two mechanisms.
(d) What are the $\left(t_{63}, \beta\right)$ values for the two mechanisms?

## Answers:

(b) Point of inflection: $F=0.42$,
(d) Mechanism A: $t_{63}=32.3 \mathrm{~h}, \beta=2.99$ Mechanism B: $t_{63}=139.6 \mathrm{~h}, \beta=6.29$.

## Bibliography

Dhillon, B. and C. Singh: Engineering Reliability, John Wiley \& Sons, (1981).
McPherson, J.: Reliability Physics. In: Handbook of Semiconductor Manufacturing Technology, Marcel Dekker, 959 (2000).
Miller, I. and J. Freund: Probability and Statistics for Engineers 2nd Ed., Prentice Hall, (1977). Nelson, W.: Accelerated Testing, John Wiley and Sons, (1990).# Chapter 8 <br> Failure Rate Modeling 

For a collection of devices, it is critically important to be able to understand the expected failure rate for the devices. For the supplier of such devices, the expected failure rate will be an important indicator of future warranty liability. For the customer, the expected failure rate will be an important indicator of future satisfaction. For mission-critical ${ }^{1}$ applications, it is of paramount importance for one to know that the expected failure rate will be extremely low.

## 1 Device Failure Rate

The survivor failure rate for a collection of devices is of great reliability importance. The failure rate equation, by which the devices are expected to fail, is given by:

$$
\frac{\mathrm{d} M}{\mathrm{~d} t}=-\lambda(t) M(t)
$$

$M(t)$ represents the number of survivors at any time $t$, and $\lambda(t)$ represents the instantaneous survivor failure rate. One can write

$$
M(t)=M(0)[1-F(t)]
$$

[^0]
[^0]:    ${ }^{1}$ The use of the expression mission critical came into vogue for space applications. In space applications, device repair or replacement is very difficult, if not impossible. Therefore, it is imperative that such devices have extremely low failure rates. However, today, life-support implantable devices are widely used. If one of these devices is part of your life-support system, there is little doubt that you would describe this as a mission-critical application.where $M(0)$ is the number of devices at time zero and $F(t)$ is the cumulative failure probability as previously discussed in Chap. 7. Using the equations above, the instantaneous survivor failure rate $\lambda(t)$ is given by:

$$
\begin{aligned}
\lambda(t) & =-\frac{1}{M(t)} \frac{\mathrm{d} M}{\mathrm{~d} t}=-\frac{1}{M(0)[1-F(t)]}\left[-M(0) \frac{\mathrm{d} F}{\mathrm{~d} t}\right] \\
& =\frac{f(t)}{1-F(t)}
\end{aligned}
$$

where $f(t)$ is the probability density function (from Chap. 7).

# 2 Average Failure Rate 

Separating the variables and integrating, the solution to Eq. (8.1) can be written as ${ }^{2}$ :

$$
\int_{0}^{t} \frac{\mathrm{~d} M}{M(t)}=-\int_{0}^{t} \lambda(t) \mathrm{d} t=-t\left(\frac{\int_{0}^{t} \lambda(t) \mathrm{d} t}{\int_{0}^{t} \mathrm{~d} t}\right)=-\langle\lambda\rangle t
$$

where $\langle\lambda\rangle$ is the time-averaged failure rate. The solution to Eq. (8.4) becomes:

$$
M(t)=M(0) \exp [-<\lambda>t]
$$

Although the failure rate $\lambda(t)$ is, in general, a function of time, the average failure rate $\langle\lambda\rangle$ over some interval $0-t$ can often be useful and requires closer attention:

$$
\begin{aligned}
<\lambda> & =\frac{\int_{0}^{t} \lambda(t) \mathrm{d} t}{\int_{0}^{t} \mathrm{~d} t}=\frac{1}{t} \int_{0}^{t} \frac{f(t)}{1-F(t)} \mathrm{d} t \\
& =\frac{1}{t} \int_{0}^{t} \frac{\mathrm{~d} F(t) / \mathrm{d} t}{1-F(t)} \mathrm{d} t=\frac{1}{t} \int_{0}^{t} \frac{\mathrm{~d} F}{1-F(t)} \\
& =\frac{1}{t} \ln \left[\frac{1}{1-F(t)}\right]
\end{aligned}
$$

[^0]
[^0]:    ${ }^{2}$ The identity $1=t / \int_{0}^{t} \mathrm{~d} t$ is used in Eq. (8.4).Equation (8.6) can be approximated for small cum fraction $F$ by,

$$
\langle\lambda\rangle \cong \frac{F(t)}{t}
$$

Remember that $\ll \lambda>$ represents the average failure rate over the interval $0-t$. Therefore, during reliability testing, the average failure rate is usually estimated by:

$$
\langle\lambda\rangle=\frac{\text { Cum \# Failures }}{\text { Total \# Device } \cdot \mathrm{h}}=\frac{F \cdot \mathrm{SS}}{\mathrm{SS} \cdot(\# \text { Test } \mathrm{h})}=\frac{F}{\# \text { Test } \mathrm{h}}
$$

In the equation above, SS is the sample size. The unit of failure rate is the failure in time (FIT) and represents 1 failure per billion device-hours ( 1 FIT $=1$ failure $/ 10^{9}$ $\operatorname{dev} \bullet \mathrm{h}=10^{-9}$ fails $/ \operatorname{dev} \bullet \mathrm{h}=10^{-9} / \mathrm{h}$ ). ${ }^{3}$ While the instantaneous failure rate is obviously more precise, the average failure rate can often be useful, especially for very complex/multi-component systems and when estimating cum fraction $F$.

# 2.1 Lognormal Average Failure Rate 

The average failure rate, using the lognormal cumulative failure distribution $F(t)$ from Chap. 7, becomes:

$$
\begin{aligned}
\langle\lambda\rangle_{\text {log normal }} & =\frac{1}{t} \ln \left[\frac{1}{1-F(t)}\right] \\
& =\frac{1}{t} \ln \left[\frac{1}{1-\frac{1}{2} \operatorname{erfc}\left(\frac{\ln \left(t_{50}\right)-\ln (t)}{\sigma \sqrt{2}}\right)}\right]\left(\text { for } t \leq t_{50}\right) \\
& =\frac{1}{t} \ln \left[\frac{1}{\frac{1}{2} \operatorname{erfc}\left(\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right)}\right]\left(\text { for } t \geq t_{50}\right)
\end{aligned}
$$

[^0]
[^0]:    ${ }^{3}$ In order to be consistent with Eq. (8.1), the true unit of failure rate $\lambda$ must be in reciprocal time. Often the pseudo units (failures and devices) are introduced for emphasis and to facilitate a little bookkeeping. However, the true units of the FIT are: 1 FIT $=10^{-9} / \mathrm{h}$.# 2.2 Weibull Average Failure Rate 

The average failure rate, using the Weibull cumulative failure distribution $F(t)$ from Chap. 7, is given by:

$$
\begin{aligned}
\langle\lambda\rangle_{\text {Weibull }} & =\frac{1}{t} \ln \left[\frac{1}{1-F(t)}\right]=\frac{1}{t} \ln \left[\frac{1}{\exp \left[-\left(\frac{t}{t_{63}}\right)^{\beta}\right]}\right] \\
& =\frac{1}{t}\left(\frac{t}{t_{63}}\right)^{\beta}
\end{aligned}
$$

## Example Problem 1

The observed average failure rate for a collection of devices was found to be: $\langle\lambda\rangle=\lambda_{0}=1,000$ FITs. If one starts with 50,000 devices at time zero, how many devices are expected to fail after 1 year? [Note: 1 year $=8,760 \mathrm{~h}$ ]

## Solution

$$
\begin{aligned}
& M(t)=M_{0} \exp \left(-\lambda_{0} t\right) \\
& \Rightarrow \\
M(t=8,760 \mathrm{~h}) & =(50,000 \text { devices }) \exp \left[-(1,000 \mathrm{FITs})\left(\frac{10^{-9} / \mathrm{h}}{1 \mathrm{FIT}}\right)(8,760 \mathrm{~h})\right] \\
& =4,9564 \\
\# \text { Failures } & =M_{0}-M(t=8,760 \mathrm{~h})=50,000-49,564=436
\end{aligned}
$$

## Example Problem 2

Suppose that one has a system which is made up of 1,000 components, with the components having an average failure rate of 100 FITs. What would be the mean (average) time between failures for such a system?

## Solution

$$
\begin{aligned}
\text { Average System Failure Rate } & =(1,000 \text { devices }) \cdot(100 \text { FITs }) \\
& =(1,000 \text { devices }) \cdot\left(\frac{100 \text { failures }}{109 \text { device } \cdot \mathrm{h}}\right) \\
& =\frac{1 \text { failure }}{10^{4} \mathrm{~h}}
\end{aligned}
$$Since $10^{4} \mathrm{~h}=1.14$ years, then one would expect this system to fail (on average) once every 1.14 year. This represents the mean-time-betweenfailures (MTBF $=1 /<\lambda>$ ) and is a very important reliability parameter. MTBF describes, on average, the level of reliability problems that can be expected for such a system.

# 3 Instantaneous Failure Rate 

The instantaneous survivor failure rate is generally of greater value to the reliability engineer than simply the average failure rate. ${ }^{4}$ Both the lognormal and Weibull instantaneous failure rates are discussed in detail.

### 3.1 Lognormal Instantaneous Failure Rate

Using Eq. (8.3), with $f(t)$ and $F(t)$ found in Chap. 7 Eqs. (8.1) and (8.2), respectively, then the lognormal instantaneous failure rate becomes:

$$
\lambda(t)=\frac{\frac{1}{\sigma t \sqrt{2 \pi}} \exp \left\{\left\{-\left[\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right]^{2}\right\}\right.}{1-\frac{1}{2} \operatorname{erfc}\left(\frac{\ln \left(t_{50}\right)-\ln (t)}{\sigma \sqrt{2}}\right)} \quad\left(\text { for } t \leq t_{50}\right)
$$

and

$$
\lambda(t)=\frac{\frac{1}{\sigma t \sqrt{2 \pi}} \exp \left\{-\left[\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right]^{2}\right\}}{\frac{1}{2} \operatorname{erfc}\left(\frac{\ln (t)-\ln \left(t_{50}\right)}{\sigma \sqrt{2}}\right)}\left(\text { for } t \geq t_{50}\right)
$$

[^0]
[^0]:    ${ }^{4} \mathrm{~A}$ common-experience analogy is perhaps useful-the instantaneous speed that you drive is usually far more important than your average speed. Speeding tickets are normally issued based on instantaneous speed, not average speed!# 3.2 Weibull Instantaneous Failure Rate 

Using Eq. (8.3), and $f(t)$ and $F(t)$ found in Eqs. (8.5) and (8.6), respectively, then the Weibull instantaneous failure rate takes on a relatively simple form:

$$
\lambda(t)=\left(\frac{\beta}{t_{63}}\right)\left(\frac{t}{t_{63}}\right)^{\beta-1}
$$

The Weibull failure rate is widely used because it describes weakest link type failure mechanisms very well. Also, another reason for its popularity is that its form is relatively simple, versus the lognormal failure rate, Eq. (8.11). Note that for $\beta=$ 1 , the failure rate is a constant (independent of time). It will be shown, in example problem 3 , that the Weibull failure rate decreases when $\beta<1$, increases when $\beta>$ 1 , and is constant for $\beta=1$.

## Example Problem 3

In a reliability test, it was found that the characteristic Weibull lifetime was $t_{63}=87,600 \mathrm{~h}$. Determine the Weibull instantaneous failure rate curve for: $\beta=0.5, \beta=1.0$, and $\beta=1.5$.

## Solution

Shown in Fig. 8.1 is the failure rate $\lambda(t)$ in FITs, given by Eq. (8.12). In Fig. 8.1a, the failure rate is shown with a linear scaling of the time. In Fig. 8.1b, the failure rate is shown with a logarithmic scaling of the time. These figures indicate that for $\beta=0.5$, the failure rate decreases with time. For $\beta=1.0$, the failure rate is constant. For $\beta=1.5$, the failure rate increases with time.

## 4 Bathtub Curve

The failure rate curve for devices (either electrical or mechanical) generally takes the form shown in Fig. 8.2. From its obvious shape, this reliability curve is commonly referred to as the bathtub curve for reliability. There are three distinct reliability regions associated with this curve and these are highlighted in (Fig. 8.2). First, during the early stages of device use, the failure rate is relatively high and this region is referred to as the early failure rate (EFR) region. The failures occurring in the EFR region are generally due to rather gross defects. Second, after the initial high EFR portion of the curve, a much lower and stable failure rate region occurs and this region is referred to as the intrinsic failure rate (IFR) region. The IFR fails can be due to very small defects in the materials. After the IFR region, one usually has a region of rapid turn-up in the failure rate which is referred to as the Wear-out region. The Wear-out region is driven by normal material/device degradation, as discussed in

Fig. 8.1 (a) Failure rate is observed to decrease with time for $\beta<1$, failure rate is constant for $\beta=$ 1 , and failure rate is observed to increase for $\beta>1$. Linear time-scaling is shown. (b) Failure rate is observed to decrease with time for $\beta<1$, failure rate is constant for $\beta=1$, and failure rate is observed to increase for $\beta>1$. Logarithmic time-scaling is shown

Chap. 3. This Wear-out region is strongly dependent of the level of stress and temperature, as discussed in Chap. 5.

The old reliability joke among air travelers-if you are either scheduled for the maiden flight on a new airliner or scheduled for a trip on an airliner that has been in service for more than 25 years, then you may want to reconsider your travel plans! In the former case, one worries about EFR and in the later case one worries about Wear-out. If you are told that the plane is about 10 years old, with outstandingFig. 8.2 Bathtub reliability curve is used to describe device failure rate characteristics for nearly all devices

reliability and service record, then you should be at the bottom of the bathtub curve (lowest failure rate)—so sit back and enjoy the flight!

Depressing as the subject may be, the bathtub curve also describes the mortality rate for humans. The death rate for newborns is relatively high during the first few hours of life because of birth defects in critically important organs (heart, lungs, kidneys, brain, etc.). This is the EFR portion of the curve for humans ${ }^{5}$ and helps to explain why doctors and parents generally have more apprehension/anxiety during the first 24 h of a newborn's life. After this initial period, the level of concern tends to reduce with time and drops rather sharply after 1 day, 1 week, 1 month, etc. After a year or so, the mortality rate tends to flatten (bottom of bathtub curve) and the mortality rate is at its lowest value (sweet part of the reliability curve). Unfortunately, however, after about 70+ years of use, your components (organs) start wearing out and the system (your body) starts to fail.

# 5 Failure Rate for Electronic Devices 

The EFR portion of the reliability curve for electronic devices can be very similar to that shown in Fig. 8.2. This EFR region, for integrated circuits, is dominated by manufacturing defects (materials with extremely low breakdown strengths) and shows a rather sharp reduction in failure rate with time. This EFR region (higher failure-rate region) can last for a year or more at normal operating voltage and temperature conditions: $\left(V_{\mathrm{op}}, T_{\mathrm{op}}\right)$. This can be a reliability headache (very expensive) for the supplier because the warranty period is generally 1 year. To avoid the supplier headaches, from irate customers having initially very high failure rates, the supplier may sometimes choose to exercise the devices for a period of time (to eliminate the defective devices) before sending the product to their customers.

[^0]
[^0]:    ${ }^{5}$ This is why the EFR region is also referred to as infant mortality.Table 8.1 Observed failure data for 5,000 devices

| Sample size $=5,000$ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Time (year) | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Number of fails | 15 | 1 | 0 | 0 | 0 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 15 | 25 |

This period of time, in which the devices are exercised to eliminate the defective devices, is often called burn-in.

The IFR region still contains some relatively small defects (which tend to reduce the breakdown strength of the materials). The failure rate that is observed at the bottom of the bathtub curve is nearly constant and is due primarily to those intrinsic weaknesses (intermediate breakdown strengths) found in a population of otherwise good devices. This portion of the curve is referred to as the intrinsic failure-rate (IFR) region.

Finally, if the devices are operated long enough, they will eventually start to fail even though the material strengths may be excellent; this region is referred to as the Wear-out region. The Wear-out region is correlated with the materials-type selection, design rules used, and the use conditions.

In order to reduce the high failure rate during the EFR period, burn-in is sometimes needed; but, 1 year of burn-in at nominal operating conditions ( $V_{\text {op }}$, $T_{\text {op }}$ ) is not practical. If, however, one increases the normal operating conditions to ( $V_{\text {stress }}, T_{\text {stress }}$ ), then one can accelerate the time-to-failure process for these defective devices. Hopefully, under the accelerated conditions, the defective devices will fail much more rapidly (hours, minutes, or even seconds) versus the 1 year period of normal conditions. This all depends on the acceleration factor (subject of Chaps. 9 and 10).

One also has to be careful that the accelerated burn-in process does not significantly weaken the good devices. It is assumed that the design and materials used in the good devices are such that these devices have many years of reliable operation; therefore, losing 1 year of lifetime is rather insignificant. Again, all this depends on the acceleration factor used for the burn-in process.

# Example Problem 4 

The reliability of 5,000 devices was monitored during a 10-year period. The failures are shown in Table 8.1.
(a) Construct the failure rate curve (bathtub curve).
(b) How long should the devices have been burned-in so that the shipped product had a failure rate of $<100$ fits?
(c) If wear out is defined as the time for the failure rate to exceed 100 fits, when did this product start to wear out?# Solution 

(a) The failure data, provided in this problem, is first reorganized in Table 8.2 below for relatively easy data analysis. Shown in Fig. 8.3 is the cumulative fraction failed F for the complete data set. The EFR, IFR, and Wear-out regions are also indicated. The EFR region is treated as an independent failure rate contributor with the cum fraction FEFR calculated using the entire sample size of 5,000 (see Table 8.2). The IFR region is also treated as an independent failure rate contributor but uses a reduced sample size of 4,984. The wear-out region is also treated as an independent failure rate contributor, but with a further reduced sample size of 4,971 . The total failure rate will be a sum of these independent contributors to the failure rate.

The characteristic Weibull parameters $\left(t_{63}, \beta\right)$, which best describe each of the independent regions (EFR, IFR, Wear-out), are shown in Fig. 8.4. From these characteristic values, and using the Weibull failure rate Eq. (8.12), the constructed bathtub curve is shown in Fig. 8.5
(b) Using the above bathtub curve (Fig. 8.5) one can see that the device/ product should be burned-in for at least 0.5 years, if the goal is to ship product with a failure rate of $<100$ FITs.
(c) One can see, from Fig. 8.5, that the failure rate again exceeds 100 FITs after 6.9 years of use and thus defines the start of wear out.

It must be noted that it is probably unrealistic to burn-in devices for 0.5 years ( 6 months) before being shipped; thus, accelerated methods have to be developed which will accelerate this burn-in time. Normally this acceleration is achieved through the use of elevated voltages, elevated mechanical stresses, and/or elevated temperature. This will be discussed in more detail in Chaps. 9 and 10.Table 8.2 Failure data reorganized (from Table 8.1). Sample Size $=\mathrm{SS}=5000$.

| Time
(year) | \# <br> FAILS | F | $\begin{aligned} & \hline \ln [-\ln \\ & (1-F)] \end{aligned}$ | $\begin{aligned} & \hline \text { (SS) } \mathrm{EFR}=\mathrm{SS} \\ & F_{\mathrm{EFR}} \end{aligned}$ | $\begin{aligned} & \text { EFR: } \ln [-\ln \\ & \left(1-F_{\mathrm{EFR}}\right)] \end{aligned}$ | $\begin{aligned} & (\mathrm{SS})_{\mathrm{EFR}}=\mathrm{SS} \\ & -16 \end{aligned}$ | IFR: $\ln [-\ln$ $\left.\left(1-F_{\mathrm{IFR}}\right)\right]$ | $\begin{aligned} & (\mathrm{SS})_{\text {Wear-out }}=\mathrm{SS}-29 \end{aligned}$ | Wear-out: $\ln [-\ln (1-$ <br> $F_{\text {wear-out }}$ ) $]$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 0.1 | 15 | 0.0030 | $-5.8076$ | 0.0030 | $-5.8076$ |  |  |  |  |
| 0.2 | 1 | 0.0032 | $-5.7430$ | 0.0032 | $-5.7430$ |  |  |  |  |
| 0.3 | 0 | 0.0032 | $-5.7430$ |  |  |  |  |  |  |
| 0.4 | 0 | 0.0032 | $-5.7430$ |  |  |  |  |  |  |
| 0.5 | 0 | 0.0032 | $-5.7430$ |  |  |  |  |  |  |
| 1 | 1 | 0.0034 | $-5.6823$ |  |  | 0.0002 | $-8.5139$ |  |  |
| 2 | 2 | 0.0038 | $-5.5709$ |  |  | 0.0006 | $-7.4151$ |  |  |
| 3 | 2 | 0.0042 | $-5.4706$ |  |  | 0.0010 | $-6.9040$ |  |  |
| 4 | 2 | 0.0046 | $-5.3794$ |  |  | 0.0014 | $-6.5674$ |  |  |
| 5 | 2 | 0.0050 | $-5.2958$ |  |  | 0.0018 | $-6.3159$ |  |  |
| 6 | 2 | 0.0054 | $-5.2187$ |  |  | 0.0022 | $-6.1150$ |  |  |
| 7 | 2 | 0.0058 | $-5.1470$ |  |  | 0.0026 | $-5.9477$ |  |  |
| 8 | 5 | 0.0068 | $-4.9874$ |  |  |  |  | 0.0010 | $-6.9014$ |
| 9 | 15 | 0.0098 | $-4.6205$ |  |  |  |  | 0.0040 | $-5.5136$ |
| 10 | 25 | 0.0148 | $-4.2057$ |  |  |  |  | 0.0091 | $-4.7002$ |Fig. 8.3 Weibull plot of cum fraction failed $F$ versus time for failure data shown in Table 8.2. The EFR, IFR, and Wear-out regions are indicated


Fig. 8.4 Individual weibull plots for the independent failure rate contributors: EFR, IFR, and wearout regions. Characteristic weibull parameters $\left(t_{63}, \beta\right)$ for each independent region are shown

Fig. 8.5 Bathtub reliability curve is created when the independent failure rate contributors are added: EFR + IFR + Wear-Out

# Problems 

1. For certain implantable medical devices, the median time-to-failure is $t_{50}=$ $87,600 \mathrm{~h}$ (10 years) and a logarithmic standard deviation of $\sigma=0.7$. Assuming a lognormal distribution:
(a) What is the instantaneous failure rate at 8 years?
(b) What is the average failure rate after 8 years?
(c) What fraction of the devices is expected to fail after 8 years?

## Answers:

(a) $\lambda @ t=70,080 \mathrm{~h}=1.24 \times 10^{-5} / \mathrm{h}$
(b) $<\lambda>$ after $780,080 \mathrm{~h}=6.71 \times 10^{-6} / \mathrm{h}$
(c) $F=0.375$
2. A certain collection of capacitors has a Weibull time-to-failure distribution with a characteristic time-to-failure of $t_{63}=100,000 \mathrm{~h}$ and a Weibull slope of $\beta=$ 1.2 .
(a) What is the instantaneous failure rate at 9 years?
(b) What is the average failure rate after 9 years?
(c) What fraction of the capacitors is expected to fail after 9 years?

## Answers:

(a) $\lambda @ t=78,840 \mathrm{~h}=1.14 \times 10^{-5} / \mathrm{h}$
(b) $<\lambda>$ after $78,840 \mathrm{~h}=9.54 \times 10^{-6} / \mathrm{h}$
(c) $F=0.528$3. For a mechanical component, fatigue data indicates that the median cycle-tofailure is $(\mathrm{CTF})_{50}=26,000$ cycles and a logarithmic standard deviation of $\sigma=$ 1.2. Assuming a lognormal distribution:
(a) What is the instantaneous failure rate at 18,000 cycles?
(b) What is the average failure rate after 18,000 cycles?
(c) What fraction of the components is expected to fail after 18,000 cycles?

# Answers: 

(a) $\lambda @ 18,000$ cycles $=2.84 \times 10^{-5} /$ cycle
(b) $<\lambda>$ after 18,000 cycles $=2.65 \times 10^{-5} /$ cycle
(c) $F=0.380$
4. Certain mechanical components are found to corrode and can be described by a lognormal time-to-failure distribution with a characteristic time-to-failure of $t_{50}=50,500 \mathrm{~h}$ and a $\sigma=1.2$.
(a) What is the instantaneous failure rate at $40,000 \mathrm{~h}$ ?
(b) What is the average failure rate after $40,000 \mathrm{~h}$ ?
(c) What fraction of the components is expected to fail after $40,000 \mathrm{~h}$ ?

## Answers:

(a) $\lambda @ t=40,000 \mathrm{~h}=1.41 \times 10^{-5} / \mathrm{h}$
(b) $<\lambda>$ after $40,000 \mathrm{~h}=1.37 \times 10^{-5} / \mathrm{h}$
(c) $F=0.423$
5. Certain integrated circuits are found to fail, due to channel hot-carrier injection, and can be described by Weibull time-to-failure distribution with a characteristic time-to-failure of $t_{63}=75,000 \mathrm{~h}$ and a Weibull slope of $\beta=2.0$.
(a) What is the instantaneous failure rate at $60,000 \mathrm{~h}$ ?
(b) What is the average failure rate after $60,000 \mathrm{~h}$ ?
(c) What fraction of the circuits is expected to fail after $60,000 \mathrm{~h}$ ?

## Answers:

(a) $\lambda @ t=60,000 \mathrm{~h}=2.13 \times 10^{-5} / \mathrm{h}$
(b) $<\lambda>$ after $60,000 \mathrm{~h}=1.07 \times 10^{-5} / \mathrm{h}$
(c) $F=0.473$
6. Certain automobile tires are found to wear out according to a lognormal wearout distribution with characteristic parameters: (wear out) $)_{50}=38,000$ miles with a $\sigma=0.6$.
(a) What is the instantaneous wear-out rate at 32,000 miles?
(b) What is the average wear-out rate after 32,000 miles?
(c) What fraction of the tires is expected to wear out after 32,000 miles?# Answers: 

(a) $\lambda @ 32,000$ miles $=3.25 \times 10^{-5} /$ mile
(b) $<\lambda>$ after 32,000 miles $=1.53 \times 10^{-5} /$ mile
(c) $F=0.388$
7. Certain hinges on doors are found to fail according to a Weibull distribution with the parameters: (number of closures) ${ }_{63}=25,000$ with a Weibull slope of $\beta=0.5$.
(a) What is the instantaneous failure rate at 18,000 closures?
(b) What is the average failure rate after 18,000 closures?
(c) What fraction of hinges is expected to fail after 18,000 closures?

## Answers:

(a) $\lambda @ 18,000$ closures $=2.36 \times 10^{-5} /$ closure
(b) $<\lambda>$ after 18,000 closures $=4.71 \times 10^{-5} /$ closure
(c) $F=0.572$
8. Crowns, from a certain dental supply company, are found to fail according to a Weibull distribution with the parameters: $t_{63}=15.0$ years and a Weibull slope of $\beta=1.0$.
(a) What is the instantaneous failure rate at 12 years?
(b) What is the average failure rate after 12 years?
(c) What fraction of crowns is expected to fail after 12 years?

## Answers:

(a) $\lambda @ t=12$ years $=6.67 \times 10^{-2} /$ year
(b) $<\lambda>$ after 12 years $=6.67 \times 10^{-2} /$ year
(c) $F=0.551$
9. Certain cell phones can start to fail after a number of drops. (Note: dropped phones not dropped calls.) The failures in a certain test are found to be described well by a Weibull distribution with the parameters: (number of drops) ${ }_{63}=$ 88 drops and Weibull slope of $\beta=0.6$.
(a) What is the instantaneous failure rate at 50 drops?
(b) What is the average failure rate after 50 drops?
(c) What fraction of phones is expected to fail after 50 drops?

## Answers:

(a) $\lambda @ 50$ drops $=8.55 \times 10^{-3} /$ drop
(b) $<\lambda>$ after 50 drops $=1.42 \times 10^{-2} /$ drop
(c) $F=0.510$
10. Temperature-cycling of bi-metallic layers was found to produce delamination type failures conforming to a lognormal distribution with parameters: median cycle-to-failure of (cycles-to-failure) ${ }_{50}=1,600$ cycles and $\sigma=0.9$.(a) What is the instantaneous failure rate at 1,300 cycles?
(b) What is the average failure rate after 1,300 cycles?
(c) What fraction of components is expected to fail after 1,300 cycles?

# Answers: 

(a) $\lambda @ 1,300$ cycles $=5.62 \times 10^{-4} /$ cycle
(b) $<\lambda>$ after 1,300 cycles $=4.04 \times 10^{-4} /$ cycle
(c) $F=0.409$

## Bibliography

McPherson, J: Accelerated Testing. In: Electronic Materials Handbook, Vol. 1 Packaging, ASM International, 887 (1989).
Miller, I. and J. Freund: Probability and Statistics for Engineers, 2nd. Ed. Prentice-Hall, (1977). Thomas, T. and P. Lawler: Statistical Methods for Reliability Prediction. In: Electronic Materials Handbook, Vol. 1 Packaging, ASM International, 895 (1989).# Chapter 9 <br> Accelerated Degradation 

In Chap. 2 we learned that a stressed material was at a higher Gibbs Potential and therefore more unstable. The stressed material will spontaneously degrade, but at what rate? We might suspect, and rightfully so, that higher stress levels will make a material even more unstable and therefore accelerate the degradation rate; also, our intuition might suggest that the degradation rate for a material is temperature dependent. This chapter will develop the needed equations that show that this is indeed the case.

By accelerating the degradation rate, one means: accelerating the normal degradation process through the use of elevated stress and/or temperature. Accelerated testing is intended to shorten the normal time-to-failure process (which could take years), without changing the physics of failure. The objective of accelerated testing is to understand the stress and temperature dependence (kinetics) of failure mechanisms so that reliability estimations and reliability improvements can be made through: better design rules, better materials selection criteria, and/or better process/manufacturing control. Also, reliability improvements can be made through: defect reduction, burn-in, intrinsic failure-rate reduction, and wear-out prevention.

## 1 Impact of Temperature on Degradation Rate

In Chap. 2 we discussed how a generalized stress acting on a material increases its Gibbs Potential and thus makes the material less stable and more prone to degradation. It is a common experience that devices (automobile tires, valve springs, shock absorbers, computers, TVs, cell phones, iPads, etc.) generally degrade faster at higher stress levels and at higher temperatures. Therefore, we need a Gibbs Potential description for material degradation that incorporates the fact that either increased stress $\xi$ or increased temperature T will cause a material to degrade at a faster rate.

Shown in Fig. 9.1 is a Gibbs Potential/Free-Energy description of the material degradation reaction. Initially (at time-zero), as we can see from Fig. 9.1, theFig. 9.1 Free energy description of material/ device degradation is illustrated. The initial state is metastable because the degraded state has a lower free energy. The relative stability of the initial metastable state is impacted by the activation energy $\Delta G^{*}$ needed to go from the initial metastable state to the degraded state. The degradation rate is generally controlled by the Boltzmann probability

material/device is in a metastable state with a Gibbs-Potential/Free-Energy of $\mathrm{G}_{1}$. However, one knows from experience that the material will degrade with time thus moving towards the lower Gibbs Potential/Free-Energy degraded state $\mathrm{G}_{2}$. The driving force for this material degradation is a difference in the Gibbs-Potential/ Free-Energy $\Delta G$. This implies that $\mathrm{G}_{2}-\mathrm{G}_{1}$ must be negative for the degradation process to proceed. To avoid any ambiguities with sign convention (in all of the degradation reaction-rate equations that follow in this chapter) we have used the absolute value: $\Delta G=\left|G_{2}-G_{1}\right|$ in the rate equations. It will be understood that the free energy of the degraded state $\mathrm{G}_{2}$ must be lower than the initial state $\mathrm{G}_{1}$ for the degradation reaction to proceed. Therefore, the larger $\Delta G$ the stronger is the driving force for degradation.

While the driving force for degradation is a free energy difference $\Delta G$ between the initial state and the degraded state, the rate of the degradation reaction is limited by the activation energy $\Delta G^{*}$. Generally heat and/or work is required to overcome this activation energy barrier. In analogy with chemical reaction rates, one can think of the degradation rate in terms of a degradation rate constant $k$. The forward (or degradation) reaction rate $k_{\text {forward }}$ (Fig. 9.1) is given by:

$$
k_{\text {forward }}=k_{0} \exp \left[-\frac{\Delta G^{*}}{K_{B} T}\right]
$$

where $k_{0}$ is an interaction frequency (taken to be a constant), $K_{B}$ is Boltzmann's constant, and $T$ is the temperature (Kelvin). ${ }^{1}$ The reverse (or recovery) reaction rate is controlled by:

[^0]
[^0]:    ${ }^{1}$ Equation (9.1) represents the Boltzmann probability that atoms in the initial state will obtain the necessary energy to go over the barrier to the degraded state. It is possible that the atoms can tunnel through the barrier, but the tunneling probability is very small except for the very lightest of elements such as hydrogen. For nearly all other elements, the Boltzmann probability is usually much greater than the tunneling probability. Boltzmann's constant is $8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}$.$$
k_{\text {reverse }}=k_{0} \exp \left[-\frac{\left(\Delta G+\Delta G^{*}\right)}{K_{B} T}\right]
$$

Thus, the net degradation reaction rate for material/device is given by $k_{\text {net }}=k_{\text {forward }}-k_{\text {reverse }}:$

$$
k_{\text {net }}=k_{0} \exp \left[-\frac{\Delta G^{*}}{K_{B} T}\right]\left\{1-\exp \left[-\frac{\Delta G}{K_{B} T}\right]\right\}
$$

One can see that the driving force for the net degradation rate is $\Delta G$. If $\Delta G=0$, then the net degradation reaction rate is zero, regardless of the activation energy $\Delta G^{*}$. When the degraded state has a lower free energy than the initial state $(\Delta G \neq 0)$, then the activation energy $\Delta G^{*}$ becomes critically important in retarding the degradation reaction. In fact, when $\Delta G \gg K_{B} T$, then the reverse reaction rate becomes negligible and Eq. (9.3) reduces simply to:

$$
k_{\text {net }}=k_{0} \exp \left[-\frac{\Delta G^{*}}{K_{B} T}\right]
$$

From Eq. (9.4), one can see that the activation energy can be extracted from the observed degradation rate using:

$$
\Delta G^{*}=-K_{B}\left[\frac{\partial \ln \left(k_{\text {net }}\right)}{\partial(1 / T)}\right]
$$

# 2 Impact of Stress and Temperature on Degradation Rate 

Let us now consider the impact of applying a stress $\xi$ to a material and investigate its impact on the degradation rate. Remember that the stress $\xi$ can be general in nature (mechanical stress, electrical stress, chemical stress, etc.) and represents any external agent which can enhance/accelerate the degradation rate. The expected impact of stress $\xi$ on the Gibbs Potential/Free-Energy is illustrated in Fig. 9.2. The generalized stress $\xi$ tends to elevate the initial Gibbs Potential making $\Delta \mathrm{G}$ larger and the activation energy $\Delta \mathrm{G}^{*}$ lower.

We expect that a generalized stress $\xi$ acting on a material will increase the material degradation rate by increasing the free energy difference $\Delta G$ between the initial state (when the stress is initially applied) and the degraded state (which occurs sometime later). Since $\Delta G$ is a function of the generalized stress $\xi$, then we can use a Maclaurin Series to expand:

Fig. 9.2 Free energy impact when a stress $\xi$ is applied to a material/device. The stress $\xi$ can have at least two impacts on the free energy: (1) the stress can make the initial metastable state even more unstable by increasing the free energy difference $\Delta \mathrm{G}$ between the initial and degraded states and (2) the stress can lower the activation energy $\Delta \mathrm{G}^{*}$ and this can accelerate the degradation rate

$$
\begin{aligned}
\Delta G & =(\Delta G)_{\xi=0}+\left[\frac{\partial(\Delta G)}{\partial \xi}\right]_{\xi=0} \xi+\cdots \\
& \cong \Delta G_{0}+c \xi
\end{aligned}
$$

We have chosen to use a positive sign in front of " $c$ " in the last equation because we have found (in Chap. 2) that the generalized stress $\xi$ tends to increase $\Delta G$. In fact, we should note that in Chap. 2 we found that, for many cases, $\Delta G$ actually increases quadratically with stress $\xi$. For this reason, we choose to write Eq. (9.6) in a more general form:

$$
\Delta G \cong \Delta G_{0}+b \xi^{n}
$$

where $n \geq 1$ and n is generally determined experimentally.
Likewise, we will assume that a similar Maclaurin series expansion approach can be taken for the free energy of activation $\Delta G^{*}$ :

$$
\begin{aligned}
\Delta G^{*} & =\left(\Delta G^{*}\right)_{\xi=0}+\left[\frac{\partial\left(\Delta G^{*}\right)}{\partial \xi}\right]_{\xi=0} \xi+\cdots \\
& \cong \Delta G_{0}^{*}-a \xi
\end{aligned}
$$

We have chosen to use a negative sign in front of " $a$ " in the last equation because we anticipate (from Fig. 9.2) that the stress $\xi$ will tend to decrease $\Delta G^{*}$.

Using Eq. (9.3), along with Eqs. (9.7) and (9.8), the net reaction rate for material/ device degradation becomes:$$
k_{\text {net }}=k_{0} \exp \left[-\frac{\left(\Delta G_{0}^{*}-a \xi\right)}{K_{B} T}\right]\left\{1-\exp \left[-\frac{\left(\Delta G_{0}+b \xi^{n}\right.}{K_{B} T}\right]\right\}
$$

Let us now consider a special case of Eq. (9.9). Suppose that $\Delta \mathrm{G}_{0}$ is relatively small (without stress, the free energy difference between the initial unstressed state and the degraded state is relatively small). Equation (9.9) now becomes:

$$
\begin{aligned}
k_{\text {net }} & =k_{0} \exp \left[-\frac{\left(\Delta G_{0}^{*}-a \xi\right)}{K_{B} T}\right]\left\{1-\exp \left[-\frac{b \xi^{n}}{K_{B} T}\right]\right\} \\
& =k_{0} \exp \left[-\frac{\left(\Delta G_{0}^{*}-a \xi\right)}{K_{B} T}\right] 2 \exp \left[-\frac{b \xi^{n}}{K_{B} T}\right] \sinh \left[\frac{b \xi^{n}}{K_{B} T}\right] \\
& =2 k_{0} \sinh \left[\frac{b \xi^{n}}{2 K_{B} T}\right] \exp \left\{-\frac{\left[\Delta G_{0}^{*}-a \xi+\frac{b \xi^{n}}{2^{2}}\right]}{K_{B} T}\right\}
\end{aligned}
$$

Assuming that $b \xi^{n}>>2 K_{B} T$ and that $\Delta G_{0}^{*}>>-a \xi+b \xi^{n}$, then due to the properties of the hyperbolic $\sinh (x)$ function ${ }^{2}$ one obtains for materials under moderate stress conditions:

$$
k_{\text {net }}=\left(\frac{k_{0} b}{K_{B} T}\right) \xi^{n} \exp \left\{-\frac{\Delta G_{0}^{*}}{K_{B} T}\right\}(\text { moderate stress })
$$

For materials under very high stress conditions, one obtains

$$
k_{\text {net }}=k_{0} \exp \left\{-\frac{\left[\Delta G_{0}^{*}-a \xi\right]}{K_{B} T}\right\}(\text { very high stress })
$$

One can see from the net degradation reaction-rate equation (in the moderatestress region) that the stress $\xi$ has little/no impact on reducing the activation energy $\Delta G_{0}^{*}$. The degradation reaction-rate is driven purely by increasing the free energy separation $\Delta G$ of the degraded state from the initial metastable state. Thus, $\Delta G$ is impacted by the stress $\xi$ but the activation energy $\Delta G^{*}$ is not. ${ }^{3}$

The stress dependence exponent $n$ is determined from the slope of an $\ln -\ln$ plot of Eq. (9.11), while holding the temperature $T$ constant:

[^0]
[^0]:    ${ }^{2} \sinh (x) \sim x$ for small $x$ and $\sinh (x) \sim \exp (x) / 2$ for large $x$.
    ${ }^{3}$ Note that since it was assumed that the free energy difference between the initial state and the degraded state was zero, when $\xi=0$ then the net degradation rate at low stress levels goes to zero when $b$ is zero.$$
n=\left[\frac{\partial \ln \left(k_{\text {net }}\right)}{\partial \ln (\xi)}\right]_{T=\text { constan } t}
$$

The activation energy $\Delta G_{0}^{*}$ is determined from the slope of an Arrhenius plot of Eq. (9.11), while holding the stress $\xi$ constant:

$$
\Delta G^{*}=-K_{B}\left[\frac{\partial \ln \left(k_{n e t}\right)}{\partial(1 / T)}\right]_{\xi=\text { constan } t}
$$

Finally, before we end this section, let us take a closer look at the net degradation rate constant under very high stress, Eq. (9.12). If the free-energy difference $\Delta \mathrm{G}$ (for the unstressed initial metastable state and the degrade state) is not large, then under high stress conditions what drives the net reaction rate is simply a reduction in free energy of activation $\Delta G_{0}^{*}$. Also, if $a$ is temperature dependent and has a simple temperature-dependence of the form: ${ }^{4}$

$$
a=a_{o}+\left(a_{1} K_{B}\right) T
$$

then the net degradation rate-constant under very high stress becomes:

$$
k_{\text {net }}=k_{0} \exp \left[a_{1} \xi\right] \exp \left\{-\frac{\left(\Delta G_{0}^{*}-a_{0} \xi\right)}{K_{B} T}\right\}(\text { for high stress }) .
$$

One can see that under very high stress, the degradation rate-constant is exponentially dependent on the stress $\xi$. Also, one can see that (under very high stress conditions) the effective activation energy for the degradation rate-constant can be stress dependent.

# 3 Accelerated Degradation Rates 

Acceleration of the degradation rate occurs when we increase the stress variable $\xi$ and/or the temperature $T$. One can compare the degradation rate under a set of operating conditions ( $\xi_{o p} T_{o p}$ ) versus another set of stress conditions ( $\xi_{\text {stress. }} T_{\text {stress }}$ ) by using the acceleration factor $A F$ for degradation. $A F$ for degradation rate is defined as:

$$
A F=\frac{k_{\text {net }}\left(\xi_{\text {stress }}, T_{\text {stress }}\right)}{k_{\text {net }}\left(\xi_{o p}, T_{o p}\right)}
$$

[^0]
[^0]:    ${ }^{4}$ A Maclaurin series expansion is carried out (keeping only the first term).Using Eq. (9.17), in conjunction with Eqs. (9.11) and (9.16), one obtains for moderately stressed materials:

$$
A F=\left(\frac{T_{o p}}{T_{\text {stress }}}\right)\left(\frac{\xi_{\text {stress }}}{\xi_{o p}}\right)^{n} \exp \left[-\left(\frac{\Delta G^{*}}{K_{B}}\right)\left(\frac{1}{T_{\text {stress }}}-\frac{1}{T_{o p}}\right)\right]
$$

or for very high stressed materials,

$$
A F=\exp \left[a_{1}\left(\xi_{\text {stress }}-\xi_{o p}\right)\right] \exp \left\{\frac{\Delta G_{0}^{*}-a_{o} \xi_{o p}}{K_{B} T_{o p}}-\frac{\left(\Delta G_{0}^{*}-a_{o} \xi_{\text {stress }}\right)}{K_{B} T_{\text {stress }}}\right\}
$$

Since $T$ must be expressed in Kelvin, the $\left(T_{o p} / T_{\text {stress }}\right)$ term in Eq. (9.18) is usually relatively small compared to the temperature dependence in the exponential term. Often any temperature dependence in the pre-factor is simply ignored when determining the acceleration factor. Note that the activation energy in Eq. (9.19), since it depends on stress, is no longer of the simple Arrhenius type.

# Example Problem 1 

Suppose that under constant stress the critical parameter for a certain device is observed to degrade two times faster when the temperature is simply elevated from $25^{\circ} \mathrm{C}$ to $35^{\circ} \mathrm{C}$. What is the effective activation energy associated with this degradation process?

## Solution

Must first convert ${ }^{\circ} \mathrm{C}$ to Kelvin:

$$
\begin{aligned}
& 25^{\circ} \mathrm{C}=(25+273) \mathrm{K}=298 \mathrm{~K} \\
& 35^{\circ} \mathrm{C}=(35+273) \mathrm{K}=308 \mathrm{~K}
\end{aligned}
$$

Using Eq. (9.18):

$$
\begin{aligned}
A F=2 & =\exp \left[-\left(\frac{\Delta G^{*}}{K_{B}}\right)\left(\frac{1}{T_{\text {stress }}}-\frac{1}{T_{o p}}\right)\right] \\
\Rightarrow \Delta G^{*} & =K_{B} \frac{\ln (2)}{\left(\frac{1}{T_{o p}}-\frac{1}{T_{\text {stress }}}\right)} \\
& =\left(8.62 \times 10^{-5} \mathrm{eV} / K\right) \frac{\ln (2)}{\left(\frac{1}{298 K}-\frac{1}{308 K}\right)} \\
& =0.55 \mathrm{eV}
\end{aligned}
$$# Example Problem 2 

During a constant temperature accelerated test, it was noted that a critical device parameter degradation rate increased by six times as the electric field was doubled. Using the power-law model, what is the effective fielddependence exponent $n$ for the observed degradation?

## Solution

Using Eq. (9.18):

$$
\begin{aligned}
A F & =6=\left(\frac{E_{\text {stress }}}{E_{o p}}\right)^{n} \\
& \Rightarrow n=\frac{\ln (6)}{\ln \left(\frac{V_{\text {stress }}}{V_{o p}}\right)} \\
& =\ln (6) / \ln (2) \\
& =2.58
\end{aligned}
$$

## 4 Free Energy of Activation

Reaction rates are often expressed in terms of a free energy difference $(\Delta G)$ and free energy of activation $\left(\Delta G^{*}\right)$; or, enthalpy difference $(\Delta H)$ and enthalpy of activation $\left(\Delta H^{*}\right)$; or, internal energy difference $(\Delta U)$ and internal energy of activation $\left(\Delta U^{*}\right)$. This usage can sometimes be confusing-which of these thermodynamic descriptions should be used? This book has chosen to use the Gibbs free energy approach because it emphasizes the work done on the system. The conditions for which it is acceptable to use the enthalpy approach, or the internal energy approach, are now discussed.

Changes in Gibbs free energy $\Delta \mathrm{G}$ can be written as:

$$
\Delta G=\Delta H-T \Delta \mathcal{S}
$$

where $G$ is the Gibbs free energy, $\Delta H(=\Delta U+p \Delta V)$ is the enthalpy, $T$ is the temperature $(K)$, and $S$ is the entropy. Similarly, the free energy of activation can be written as:

$$
\Delta G^{*}=\Delta H^{*}-T \Delta \mathcal{S}^{*}
$$

Referring to Fig. 9.1 and Eq. (9.3), the net reaction rate ( $k_{\text {net }}=k_{\text {forward }}-k_{\text {reverse }}$ ) can be written as:$$
\begin{aligned}
k_{\text {net }} & =k_{0} \exp \left[-\frac{\Delta G^{*}}{K_{B} T}\right]\left\{1-\exp \left[-\frac{\Delta G}{K_{B} T}\right]\right\} \\
& =k_{0} \exp \left[\frac{\Delta \mathcal{S}^{*}}{K_{B}}\right] \exp \left[-\frac{\Delta H^{*}}{K_{B} T}\right]\left\{1-\exp \left[-\frac{\Delta G}{K_{B} T}\right]\right\} \\
& =k_{1} \exp \left[-\frac{\Delta H^{*}}{K_{B} T}\right]\left\{1-\exp \left[-\frac{\Delta G}{K_{B} T}\right]\right\}
\end{aligned}
$$

Thus, for degradation reactions strongly favored in the forward direction $\left(\Delta \mathrm{G} \gg \mathrm{K}_{\mathrm{B}} \mathrm{T}\right)$, the net reaction rate constant becomes:

$$
k_{\text {net }}=k_{1} \exp \left[-\frac{\Delta H^{*}}{K_{B} T}\right]
$$

One can see that the only significant difference between Eqs. (9.4) and (9.23) is in the pre-factor. Thus, for reactions that are strongly favored in the forward direction, one can safely use either the free energy of activation $\Delta G^{*}$ or the enthalpy of activation $\Delta H^{*}$.

Also, since

$$
\Delta H=\Delta U+p \Delta V
$$

then if little/no change occurs in the solid's volume during the degradation, the $p \Delta V$ term is often ignored and one uses the approximation for solids: $\Delta H \cong \Delta U$ and $\Delta H^{*}$ $\cong \Delta U^{*}$.

# 5 Real Versus Virtual Stresses 

If one applies a stress to a material and it produces a time-to-failure distribution which is strongly dependent on the material dimensions, then the stress will be referred to as a virtual stress. If one applies a stress to a material and it produces a time-to-failure that is approximately independent of the material dimensions, then it will be referred to as a real stress. A few examples of real versus virtual stresses are given below.

Current $I$ flowing through a conductor may eventually cause electromigrationinduced failure, but the observed time-to-failure (TF) is strongly dependent on the cross-sectional area $A$ of the conductor. However, if one uses current density $J(=I /$ Area $)$ instead of current $I$, then the TF depends only on the magnitude of $J$ and is approximately independent of the cross-sectional area of the conductor. In this case, one would describe $J$ as a real stress and $I$ as a virtual stress.In dielectrics, if one ramps the voltage to breakdown, and records the breakdown voltage $V_{b d}$, one finds that $\mathrm{V}_{\mathrm{bd}}$ is strongly dependent on the dielectric thickness $t_{\text {dielectric }}$. However, if electric field $E\left(=V / t_{\text {dielectric }}\right)$ is used instead of voltage $V$, then one finds that the breakdown field $\mathrm{E}_{\mathrm{bd}}$ is approximately independent of dielectric thickness. In this case, one would describe $E$ as a real stress and $V$ as a virtual stress.

In mechanical devices, if one applies a large tensile force $F$ to a member, the member may eventually fail with time due to creep; but, the time-to-failure is strongly dependent on the cross-sectional area $A$ of the member. However, if tensile stress $\sigma(=F / A)$ is used instead of force $F$, then the time-to-failure $T F$ depends only on the magnitude of the stress $\sigma$ and $T F$ is approximately independent of the material dimensions. Thus, $\sigma$ will be referred to as a real stress and the force $F$ as a virtual stress.

Real stresses are generally preferred, when reporting time-to-failure data, because it is much more likely that someone else will be able to reproduce your time-tofailure results. Time-to-failure results using virtual stresses are very difficult to reproduce unless someone uses exactly the same material dimensions. As an additional reminder, generally, if it is a real stress, tables can be found listing a breakdown strength for the material (the stress level at which nearly instantaneous time-to-failure can be expected). For example, the rupture strength for steel occurs at a mechanical stress level of $\sigma_{\text {rupture }} \approx 2 \mathrm{GPa}$; the dielectric breakdown strength of $\mathrm{SiO}_{2}$ dielectric occurs at an electric field of $E_{B D} \approx 10 \mathrm{MV} / \mathrm{cm}$; or the fusing current density of aluminum occurs at a level of $J_{\text {Fuse }} \approx 20 \mathrm{MA} / \mathrm{cm}^{2}$. Tables listing virtual stresses [breakdown force for mechanical systems, or breakdown voltage for dielectrics, or breakdown current for conductors] are of relatively little value (because the value changes with material dimensions) and therefore generally cannot be found in tables. In this text, when we refer to stress, it is implied that it is a real stress, unless otherwise stated.

# Problems 

1. The corrosion-rate for a metal component doubles from 75 to $85^{\circ} \mathrm{C}$. What is the effective activation energy $Q$ associated with this corrosion rate?

Answer: $Q=0.74 \mathrm{eV}$
2. The threshold voltage $\mathrm{V}_{\mathrm{th}}$ degradation rate for a MOSFET device actually decreases by $40 \%$ from 25 to $50^{\circ} \mathrm{C}$. What is the effective activation energy $Q$ associated with this degradation rate?

Answer: $Q=-0.17 \mathrm{eV}$
3. The wear-rate for an automobile tire is found to occur $50 \%$ faster during the summer months $\left(35^{\circ} \mathrm{C}\right)$ than during the winter months than during the winter $\left(15^{\circ} \mathrm{C}\right)$. What is the effective activation energy $Q$ for this wear-rate increase during the summer months?Answer: $Q=0.16 \mathrm{eV}$
4. The creep rate for a metal was found to double when the temperature was elevated from 500 to $525^{\circ} \mathrm{C}$. What is the effective activation energy $Q$ ?

Answer: $Q=1.47 \mathrm{eV}$
5. The resistance degradation rate for a metal resistor, with current flowing, quadruples when the temperature increases from 250 to $300^{\circ} \mathrm{C}$. What is the effective activation energy $Q$ ?

Answers: $Q=0.72 \mathrm{eV}$
6. The tires, on a certain trailer, were found to wear-out $89 \%$ faster when carrying a weight of 3 W versus when the trailer was empty (weight of 1 W ). Find the effective power-law exponent $n$ that describes the wear rate for the tires versus the weight carried.

Answer: $n=0.58$
7. The creep rate for a metal was found to increase by 15 times when the tensilestress increased by a factor of 2 . Find the effective power-law exponent $n$ that describes creep-rate dependence on tensile stress.

Answer: $n=3.91$
8. Paint on a house was found to degrade 4 times faster (on the south side of the house which gets 3 x more sun than does the west side of the house). Find the effective power-law exponent $n$ that describes the degradation rate with sun exposure.

Answer: $n=1.26$
9. The operational frequency, of a semiconductor device, was found to degrade at a rate 4 times faster when the operational voltage was increased $10 \%$. Find the effective power-law exponent $n$ that describes the degradation rate versus voltage.

Answer: $n=14.5$
10. The degradation rate, for the resistance of a conductor, increases by 4 x when the current is doubled. Find the effective power-law exponent $n$ that describes the degradation rate versus current density.

Answer: $n=2$.# Bibliography 

Schrodinger, E.: Statistical Thermodynamics, Dover Publications, (1952).
Desloge, E.: Thermal Physics, Holt, Rinehart and Winston, Inc., (1968).
Haase, R.: Thermodynamics of Irreversible Processes, Dover Publications, (1969).
Barret, C., et al.: The Principles of Engineering Materials, Prentice Hall, (1973).
Sears, F. and Salinger, G: Thermodynamics, Kinetic Theory, and Statistical Thermodynamics, $3^{\text {rd }}$ Ed. , Addison-Wesley Publishing, (1975).
Kittel, C. and H. Kroemer: Thermal Physics, $2^{\text {nd }}$ Edition, W.H. Freeman and Co., (1980).
McPherson, J.: Stress Dependent Activation Energy, IEEE International Reliability Physics Symposium Proceedings, 12 (1986).
McPherson, J., Accelerated Testing. In: Electronic Materials Handbook, Vol. 1 Packaging, ASM International, 887 (1989a).
McPherson, J.: Accelerated Testing and VLSI Failure Mechanisms, Tutorial, IEEE International Symposium on Physical and Failure Analysis of Integrated Circuits, (1989b).# Chapter 10 <br> Acceleration Factor Modeling 

In reliability physics and engineering, the development and use of the acceleration factor (AF) is fundamentally important to the theory of accelerated testing. The AF permits one to take time-to-failure (TF) data very rapidly under accelerated stress conditions, and then to be able to extrapolate the accelerated TF results (into the future) for a given set of operational conditions. ${ }^{1}$ Since experimental determination of the AF could actually take many years, the AF must be modeled using the TF models introduced in Chap. 5. Since the AF must be modeled, it brings up another important question-how does one build some conservatism into the models without being too conservative?

## 1 Acceleration Factor

The AF is defined as the ratio of the expected TF under normal operating conditions to the TF under some set of accelerated stress conditions,

$$
\mathrm{AF}=\frac{(\mathrm{TF})_{\text {operation }}}{(\mathrm{TF})_{\text {stress }}}
$$

Since the TF under normal operation may take many years to occur, then experimental determination of the AF (from stress conditions to normal operating conditions) is usually impractical. However, if one has proper TF models (developed under accelerated conditions) then one can use these TF-models to model the AF.

Two important TF models were presented in Chap. 5, the power-law and exponential models, and are reproduced here:

[^0]
[^0]:    ${ }^{1}$ Note: for the reliability engineer, this is very exciting because the acceleration factor permits one to effectively take a crystal-ball look into the future as to what will happen!.# Power-Law TF Model 

$$
\mathrm{TF}=A_{o}(\xi)^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$

and

## Exponential TF Model

$$
\mathrm{TF}=B_{o} \exp (-\gamma \cdot \xi) \exp \left(\frac{Q}{K_{B} T}\right)
$$

In the above TF equations, the prefactor coefficients $\left(A_{o}, B_{o}\right)$ will vary from device-to-device because these parameters are strongly fabrication/process dependent. ${ }^{2}$ This is the reason why the TF will actually be a distribution of times-to-failure. The Weibull and lognormal TF distributions were discussed in Chap. 7.

Using the TF models (Eq. 10.2a) along with Eq. (10.1), one obtains for the powerlaw AF,

$$
\mathrm{AF}=\left(\frac{\xi_{\text {stress }}}{\xi_{\mathrm{op}}}\right)^{n} \cdot \exp \left[\frac{Q}{K_{\mathrm{B}}}\left(\frac{1}{T_{\mathrm{op}}}-\frac{1}{T_{\text {stress }}}\right)\right]
$$

Likewise, for the exponential model one obtains:

$$
\mathrm{AF}=\exp \left[\gamma\left(\xi_{\text {stress }}-\xi_{\mathrm{op}}\right)\right] \cdot \exp \left[\frac{Q}{K_{\mathrm{B}}}\left(\frac{1}{T_{\mathrm{op}}}-\frac{1}{T_{\text {stress }}}\right)\right]
$$

It is very important to note that the AF is very special, in that the AF is independent of the materials/process-dependent coefficients $\left(A_{o}, B_{o}\right)$. This means that even though the TF must be expressed as a distribution of times-to-failure (because of device-to-device variation), the AF is unique. AF depends only on the physics-of-failure kinetics $(n, \gamma, Q)$ and not on device-to-device variation $\left(A_{o}, B_{o}\right)$.

As discussed in Chap. 5, the kinetic values $(n, \gamma, Q)$ are determined through accelerated testing and are given by the equations:

$$
n=-\left[\frac{\partial \ln \mathrm{TF}}{\partial \ln \xi}\right]_{T}
$$

[^0]
[^0]:    ${ }^{2}$ Time-to-failure for materials/devices is strongly process dependent. Small micro-structural differences in the material can lead to device-to-device variations producing different times-to-failure.$$
\gamma=-\left[\frac{\partial \ln \mathrm{TF}}{\partial \xi}\right]_{T}
$$

and

$$
Q=K_{\mathrm{B}}\left[\frac{\partial \ln \mathrm{TF}}{\partial(1 / T)}\right]_{\xi}
$$

Given the kinetic values $(n, \gamma, Q)$ from accelerated data, ${ }^{3}$ one can then easily model the AF without having to wait the many years which would otherwise be required to actually measure the AF.

It cannot be emphasized too strongly: it is extremely important that the devicedependent/materials-dependent/process-dependent prefactors, $A_{o}$ and $B_{o}$, which appear so prominently in the TF equations, do not appear in the equations for the AF. This means that the AF depends only on the physics-of-failure (kinetics) and not on device-to-device variation. ${ }^{4}$ Thus, for a single failure mechanism, all parts of the TF distribution should be accelerated by the same amount.

The modeled AF, Eq. (10.3a) and (10.3b), permits one to go from a TF distribution taken under accelerated test conditions to a projected TF distribution under normal operating conditions. The transformations from stress conditions to operating conditions, for the lognormal and Weibull distributions, are given by:

# Lognormal 

$$
\left(t_{50}\right)_{\mathrm{op}}=\mathrm{AF} \cdot\left(t_{50}\right)_{\text {stress }}
$$

and

$$
(\sigma)_{\mathrm{op}}=(\sigma)_{\text {stress }}
$$

## Weibull

$$
\left(t_{63}\right)_{\mathrm{op}}=\mathrm{AF} \cdot\left(t_{63}\right)_{\text {stress }}
$$

and

[^0]
[^0]:    ${ }^{3}$ Kinetic values are given in Chaps. 12 and 13 for various failure mechanisms. Also, kinetic values $(n, \gamma, Q)$ for various failure mechanisms can be found in reference materials, e.g., the IEEE International Reliability Physics Symposium Proceedings.
    ${ }^{4}$ The fact that the AF depends only on the kinetics of failure $(n, \gamma, Q)$ and not on device-to-device variation (due to slight materials/process differences) is very important. This means that, for a single failure mechanism, all devices of the time-to-failure distribution should be accelerated by the same amount.$$
(\beta)_{\mathrm{op}}=(\beta)_{\text {stresss }}
$$

Note that while the characteristic TF for each distribution has been transformed using the AF, it has been assumed that the dispersion parameter $(\sigma, \beta)$ for each distribution does not change with stress. The requirement that the dispersion parameter does not change with stress will serve as the definition for uniform acceleration: uniform acceleration tends to accelerate the entire TF distribution uniformly such that the dispersion/slope-parameters $(\sigma, \beta)$ for the distributions do not change with the level of stress. One should always take enough accelerated data to establish the set of stress conditions under which the acceleration is uniform. A change in slope of the TF distribution, with stress level, may indicate a change in physics could be occurring. ${ }^{5}$ The goal of accelerated testing is to accelerate the physics without changing the physics-of-failure!

Accelerated testing is fundamental to integrated circuit reliability improvements because: (1) the defects (materials with low breakdown strengths) in a population of otherwise good devices can be eliminated with a short duration accelerated stress (burn-in); (2) the intrinsic failures can be accelerated with stress/ temperature (on a sampling basis) so that the intrinsic failure rate for a population of good devices can be determined; and, (3) the time for Wear-out (TF for the main distribution of devices) can be projected from stress conditions to a specified set of operating conditions.

# 2 Power-Law Versus Exponential Acceleration 

It is prudent to ask the question: for the same set of TF data which can be fitted nearly equally well by either the power-law or the exponential TF model, which model gives a more conservative (smaller) TF value? Also, which model gives a more conservative (smaller) AF? Generally, unless one is aware of some over-riding physics to support one model over the other, then it may be advisable to use the model with the more conservative AF. Example Problem 1 will be used to illustrate that when the same TF data set is used, the exponential model (versus the power-law model) produces a smaller TF and a smaller AF when the data is extrapolated from stress conditions to use conditions. For this reason, the exponential model is usually referred to as a more conservative model. This can be very important when one is unsure which model is more valid.

[^0]
[^0]:    ${ }^{5}$ An example of the physics-of-failure changing can be easily found from electromigration-induced failure in aluminum metallizations (discussed in Chap. 12). At relatively low temperatures, the Al-ion transport is dominated by grain-boundary diffusion with activation energy $Q_{\mathrm{gb}}$. At much higher temperatures, the transport is dominated by bulk (within-grain or lattice) diffusion with activation energy $Q_{\text {bulk }}$, where: $Q_{\text {bulk }}>Q_{\mathrm{gb}}$.

Fig. 10.1 Accelerated TF data is shown fitted using both a power-law model and an exponential model. Either model can fit the accelerated data quite well, but the two models give quite different predictions as to the TF when the results are extrapolated to much lower values of the stress. The TF and stress $\xi$ are in arbitrary units (a.u.)

# Example Problem 1 

During constant temperature accelerated testing, TF data were collected and the data are shown in Fig. 10.1. The units of the stress are in arbitrary units (a.u.). The TF data could be fit rather nicely by a power-law model $\xi^{-n}$ (with an exponent of $n=4$ ) or with an exponential model $\exp (-\gamma \xi)$ (with $\gamma=$ 0.0475 in units reciprocal stress). However, one can see that the extrapolated TF results from stress conditions ( $\xi=100$ a.u.) to use conditions ( $\xi=10$ a.u.) are quite different for the two models. The exponential model predicts a much shorter TF for use conditions ( $\xi=10$ a.u.).

Determine:
(a) Using the power-law model, what is the AF for a stress condition of $\xi_{\text {stress }}=100$ a.u. to a use condition of $\xi_{\text {use }}=10$ a.u.
(b) Using the exponential model, what is the AF for a stress condition of $\xi_{\text {stress }}$ $=100$ a.u. to a use condition of $\xi_{\text {use }}=10$ a.u.
(c) Which is the more conservative model, the exponential $\xi$-model or the power-law model?

## Solution

(a) Power-Law Model:

$$
\mathrm{AF}=\left(\frac{\xi_{\text {stress }}}{\xi_{\mathrm{op}}}\right)^{n}=\left(\frac{100}{10}\right)^{4}=10,000
$$(b) Exponential Model

$$
\mathrm{AF}=\exp \left[\gamma\left(\xi_{\text {stress }}-\xi_{\mathrm{op}}\right)\right]=\exp [(0.0475)(100-10)]=71.9
$$

(c) For the same TF data set, the exponential model is more conservative than the power-law model. By conservative, one means that the exponential model produces a smaller TF and a smaller AF when we extrapolate from accelerated conditions to use conditions.

# 3 Cautions Associated with Accelerated Testing 

There are at least two very important cautions associated with accelerated testing. First, the acceleration should only accelerate the failure physics-it should not change the failure physics. A simple story will perhaps serve as a reminder of this important caution. If one goes to a local farm and gathers some fresh fertilized chicken eggs, places them in an oven at $40^{\circ} \mathrm{C}$ and waits approximately 21 days, then one will likely obtain some very lively baby chicks. A highly accelerated testing approach would be to place the eggs in boiling water $\left(100{ }^{\circ} \mathrm{C}\right)$ and wait for only 7 min . However, this particular accelerated approach produces hard-boiled eggsnot the intended lively chicks. It is painfully obvious that we did more than simply accelerate the physics, the acceleration was too great and we changed the physics!

Second, the acceleration must be uniform-the acceleration must accelerate all parts of the Weibull (or lognormal) distribution the same. In Fig. 10.2, an example of uniform acceleration is shown. In Fig. 10.3, an example of nonuniform acceleration is shown (Weibull slopes are very different).

Note that for non-uniform acceleration, as illustrated in Fig. 10.3, there is no unique AF for the testing because the Weibull slopes $\beta$ are very different.

## 4 Conservative Acceleration Factors

Often, one is required to construct/model an AF which is well outside the region where actual stress data is available. Under these conditions, one might want to use a more conservative approach to AF construction. In this more conservative AF modeling approach, one can use the experimentally determined kinetics $(n, Q)$ over the region where stress data is actually available, and then use more conservative kinetics $\left(n_{c}, Q_{c}\right)$ outside the region where data are not available.

Fig. 10.2 Example is shown of uniform acceleration. Note that the Weibull slopes $\beta$ are the same


Fig. 10.3 Example is shown of non-uniform acceleration. Note that the Weibull slopes $\beta$ are significantly different

For a power-law TF model, the conservative AF becomes:

$$
\begin{aligned}
& \mathrm{AF}=\left(\frac{\xi_{\text {stress }}}{\xi_{c}}\right)^{n} \cdot\left(\frac{\xi_{c}}{\xi_{\text {op }}}\right)^{n_{c}} \\
& \cdot \exp \left[\frac{Q}{K_{\mathrm{B}}}\left(\frac{1}{T_{c}}-\frac{1}{T_{\text {stress }}}\right)\right] \cdot \exp \left[\frac{Q_{C}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\text {op }}}-\frac{1}{T_{c}}\right)\right]
\end{aligned}
$$

In the equation above, $\left(\xi_{c}, T_{c}\right)$ are the conservative limits on the stress and temperature. For values above $\left(n_{c}, T_{c}\right)$, data are available showing that the kinetics $(n, Q)$ are valid. Below $\left(\xi_{c}, T_{c}\right)$, where little/no data are available, it may be advisable to use more conservative values for the kinetics $\left(n_{c}, Q_{c}\right)$. Generally, the more conservative values are: $n_{c}<n$ and $Q_{c}<Q$.Also, one can easily develop a similar conservative AF for the exponential TF model:

$$
\begin{aligned}
& \mathrm{AF}=\exp \left[\gamma\left(\xi_{\text {stress }}-\xi_{c}\right)\right] \cdot \exp \left[\gamma_{c}\left(\xi_{c}-\xi_{\mathrm{op}}\right)\right] \\
& \cdot \exp \left[\frac{Q}{K_{\mathrm{B}}}\left(\frac{1}{T_{c}}-\frac{1}{T_{\text {stress }}}\right)\right] \cdot \exp \left[\frac{Q_{C}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\mathrm{op}}}-\frac{1}{T_{c}}\right)\right]
\end{aligned}
$$

Generally, the more conservative values are: $\gamma_{c}<\gamma$ and $Q_{c}<Q$.
The reason that a conservative value for the AF is sometimes used-a customer never gets mad if the device lasts longer than you predict! However, a TF prediction that is too conservative generally results in over-design or performance limitations, both of which impact the cost/sale of the designed device.

# Example Problem 2 

In a constant temperature accelerated test, accelerated TF data was taken under highly accelerated conditions where the accelerated stress conditions ranged from $\xi=1,000$ to 100 arbitrary units (a.u.). A power-law fit with $n=2$ served to describe very well the TF data over this accelerated stress range.

Determine the AF over the entire stress range from $\xi=1,000$ to 10 a.u.:
(a) when using no conservatism and
(b) when using conservatism.

## Solution

(a) Using no conservatism means that one would assume a power-law dependence $n=2$ (observed during accelerated testing over the stress range of 1,000 to 100 a.u.) and assume that the power-law exponent $n=2$ continues to hold from 100 to 10 a.u. (clearly outside the range were one has accelerated data). Under these assumptions, Eq. (10.3a) gives:

$$
\mathrm{AF}=\left(\frac{\xi_{\text {stress }}}{\xi_{\mathrm{op}}}\right)^{n}=\left(\frac{1000}{10}\right)^{2}=10,000
$$

(b) A more conservative approach would be to assume that $n=2$ holds over the accelerated data range ( 1,000 to 100 a.u.) and then perhaps assume something more conservative (e.g., $n=1$ ) from 100 to 10 a.u. (which is outside the range where one actually has accelerated data). Equation (10.9) gives:

$$
\mathrm{AF}=\left(\frac{\xi_{\text {stress }}}{\xi_{c}}\right)^{n} \cdot\left(\frac{\xi_{c}}{\xi_{\mathrm{op}}}\right)^{n_{c}}=\left(\frac{1.000}{100}\right)^{2} \cdot\left(\frac{100}{10}\right)^{1}=1,000
$$# Problems 

1. During accelerated electromigration (EM) TF testing of an aluminum-alloy at current density of $J=2 \times 910^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and a temperature of $150^{\circ} \mathrm{C}$, a lognormal distribution was obtained with the parameters: $t_{50}=400 \mathrm{~h}$ and a $\sigma=0.5$. Assuming a current density power-law exponent of $n=2$ and an activation energy of $Q=0.75 \mathrm{eV}$ (and negligible Joule/self-heating):
(a) What is the AF from stress conditions to use conditions ( $J_{\text {use }}=0.5 \times 10^{6}$ $\left.\mathrm{A} / \mathrm{cm}^{2}, T_{\text {use }}=105^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=185$, (b) $\operatorname{TF}(1 \%)=2.6$ years
2. During accelerated creep TF testing of a metal-alloy at tensile stress level of $\sigma=$ 800 MPa and a temperature of $800^{\circ} \mathrm{C}$, a lognormal distribution was obtained with the parameters: $\mathrm{t}_{50}=250 \mathrm{~h}$ and a $\sigma=0.8$. Assuming a creep power-law exponent of $\mathrm{n}=4$ and activation energy of $\mathrm{Q}=1.3 \mathrm{eV}$ :
(a) What is the AF from stress conditions to use conditions ( $\sigma_{\text {use }}=500 \mathrm{MPa}, T_{\text {use }}$ $\left.=500^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=1,532$, (b) $\mathrm{TF}(1 \%)=6.8$ years
3. During accelerated fatigue cycle-to-failure testing of a metal-alloy with a stress range of $\Delta \sigma=400 \mathrm{MPa}$ and a temperature of $25^{\circ} \mathrm{C}$, a lognormal distribution was obtained with the parameters: $(\mathrm{CTF})_{50}=2,500$ cycles and a $\sigma=0.7$. Assuming a fatigue power-law exponent of $\mathrm{n}=4$ :
(a) What is the AF from stress conditions to use conditions ( $\Delta \sigma_{\text {use }}=200 \mathrm{MPa}$, $\left.T_{\text {use }}=25^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected cycles-to-failure for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=16$ (b) $\mathrm{TF}(1 \%)=7,829$ cycles
4. During accelerated time-dependent dielectric breakdown (TDDB) testing of a silica-based dielectric, at an electric field of $\mathrm{E}=10 \mathrm{MV} / \mathrm{cm}$ and a temperature of $105^{\circ} \mathrm{C}$, a Weibull distribution was obtained with the parameters: $\mathrm{t}_{63}=1.5 \mathrm{~h}$ and a $\beta=1.4$. Assuming an exponential model with a field acceleration of $\gamma=4.0$ $\mathrm{cm} / \mathrm{MV}$ :
(a) What is the AF from stress conditions to use conditions ( $E_{\text {use }}=5 \mathrm{MV} / \mathrm{cm}$, $\left.T_{\text {use }}=105^{\circ} \mathrm{C}\right)$
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=4.850 \times 10^{8}$ (b) $\mathrm{TF}=3,107$ years5. During accelerated corrosion TF testing at $90 \%$ relative humidity (RH) and temperature of $121^{\circ} \mathrm{C}$, a lognormal distribution was obtained with the parameters: $\mathrm{t}_{50}=1,500 \mathrm{~h}$ and a $\sigma=0.7$. Assuming an exponential TF model with a humidity acceleration parameter of $\gamma=[0.12] / \% \mathrm{RH}$ and activation energy of 0.75 eV :
(a) What is the AF from stress conditions to use conditions $(\% \mathrm{RH})_{\text {use }}=65 \%$, $\left.T_{\text {use }}=85^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=185$ (b) $\mathrm{TF}=6.2$ years
6. During mobile-ions TF testing of MOSFET isolation devices at 7.5 V and $150^{\circ} \mathrm{C}$, a Weibull distribution was obtained with the parameters: $\mathrm{t}_{63}=1,200 \mathrm{~h}$ and a $\beta=$ 1.6. Assuming a power-law TF model with $\mathrm{n}=1$ and activation energy of 1.0 eV :
(a) What is the AF from stress conditions to use conditions ( $V_{\text {use }}=5.0 \mathrm{~V}, T_{\text {use }}=$ $\left.85^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=218$, (b) $\operatorname{TF}(1 \%)=1.7$ years
7. For the accelerated EM data given in Problem 1, perform a more conservative TF analysis by using $\mathrm{n}=2$ from $\mathrm{J}=2.0 \times 106$ to $1.0 \times 106 \mathrm{~A} / \mathrm{cm} 2$ and $\mathrm{n}=1.5$ below $1.0 \times 106 \mathrm{~A} / \mathrm{cm} 2$.
(a) What is the AF from stress conditions to use conditions ( $J_{\text {use }}=0.5 \times 10^{6}$ $\left.\mathrm{A} / \mathrm{cm}^{2}, T_{\text {use }}=105^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=131$, (b) $\operatorname{TF}(1 \%)=1.9$ years
8. For the accelerated creep data given in Problem 2, perform a more conservative TF analysis by using $\mathrm{n}=4$ from $\sigma=800$ to 600 MPa and $\mathrm{n}=3$ below 600 MPa
(a) What is the AF from stress conditions to use conditions ( $\sigma=500 \mathrm{MPa}$, $\left.T_{\text {use }}=500^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=1,279$, (b) $\operatorname{TF}(1 \%)=5.7$ years
9. For the accelerated fatigue data given in Problem 3, perform a more conservative TF analysis by using $\mathrm{n}=4$ from $\Delta \sigma=400$ to 300 MPa and $\mathrm{n}=3$ below $\Delta \sigma=$ 300 MPa .
(a) What is the AF from stress conditions to use conditions ( $\Delta \sigma=200 \mathrm{MPa}, T_{\text {use }}$ $\left.=25^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected cycles-to-failure for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=10.7$, (b) $\operatorname{TF}(1 \%)=5,226$ cycles10. For the accelerated TDDB data given in Problem 4, perform a more conservative TF analysis by using $\gamma=4 \mathrm{~cm} / \mathrm{MV}$ from $\mathrm{E}=10$ to $7 \mathrm{MV} / \mathrm{cm}$ and $\gamma=3.5$ $\mathrm{cm} / \mathrm{MV}$ below $7 \mathrm{MV} / \mathrm{cm}$.
(a) What is the AF from stress conditions to use conditions ( $E_{\text {use }}=5 \mathrm{MV} / \mathrm{cm}$, $\left.T_{\text {use }}=105^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=1.79 \times 10^{8}$, (b) $\operatorname{TF}(1 \%)=1,142$ years
11. For the accelerated corrosion data given in Problem 5, perform a more conservative TF analysis by using $\gamma=[0.12] / \% \mathrm{RH}$ from 90 to $80 \% \mathrm{RH}$ and $\gamma=[0.1] /$ $\% \mathrm{RH}$ below $80 \% \mathrm{RH}$.
(a) What is the AF from stress conditions to use conditions $(\% \mathrm{RH})_{\text {use }}=65 \%$, $T_{\text {use }}=85^{\circ} \mathrm{C}$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=137$, (b) $\mathrm{TF}=4.6$ years
12. For the mobile-ions TF data given in Problem 6, perform a more conservative TF analysis by using $\mathrm{Q}=1.0 \mathrm{eV}$ from $\mathrm{T}=150$ to $100^{\circ} \mathrm{C}$ and $\mathrm{Q}=0.75 \mathrm{eV}$ below $100^{\circ} \mathrm{C}$.
(a) What is the AF from stress conditions to use conditions ( $V_{\text {use }}=5.0 \mathrm{~V}$, $\left.T_{\text {use }}=85^{\circ} \mathrm{C}\right)$ ?
(b) What is the expected TF for $1 \%$ of the devices during use conditions?

Answers: (a) $\mathrm{AF}=158$, (b) $\mathrm{TF}=1.22$ years

# Bibliography 

McPherson, J.: Accelerated Testing. In: Electronic Materials Handbook, Vol. 1 Packaging, ASM International, 887 (1989).
McPherson, J.: Reliability Physics. In: Handbook of Semiconductor Manufacturing Technology, 2nd Ed., Marcel Dekker, 959 (2000).
McPherson, J.: Reliability Physics and Engineering. In: Handbook of Semiconductor Manufacturing Technology, 2 CRC Press, 30-1 (2008).# Chapter 11 <br> Ramp-to-Failure Testing 

Engineers are constantly confronted with time issues. Applying a constant stress and waiting for failure can be very time-consuming. Thus, it is only natural to ask the question-does a rapid time-zero test exist that can be used on a routine sampling basis to monitor the reliability of the materials/devices? The answer to this question is often yes and it is called the ramp-to-failure test. While the test is destructive in nature (one has to sacrifice materials/devices), it is generally much more rapid than conventional constant-stress time-to-failure tests. The relative quickness of the test also enables the gathering of more data and thus the gathering of better statistics.

## 1 Ramp-to-Failure Testing

Let us suppose that rather than applying a constant stress $\xi$ and waiting for failure, we induce failure simply by ramping up the stress level $\xi(t)$ with time until the device fails. During the ramp testing, one carefully records the level of stress at failure/ breakdown $\xi_{\mathrm{bd}}$ and the total time from start of stress to breakdown $t_{\mathrm{bd}}$. An example of linear ramp-to-failure/breakdown test is shown in Fig. 11.1.

From this ramp-to-breakdown test, it can be easily seen that $t_{\mathrm{bd}}$ is not the length of time that the material actually experiences the stress level of $\xi_{\mathrm{bd}}$. The time $t_{\mathrm{bd}}$ is the total observation time, and as such, comprehends the time that the material/ device spent at the lower stress levels of the ramp as well as at time spent at $\xi_{\mathrm{bd}}$. Therefore, the effective time $t_{\text {eff }}$ actually spent at the breakdown strength $\xi_{\mathrm{bd}}$ will be lower than $t_{\mathrm{bd}}$. One can use the acceleration factor to equate a differential element of effective stress time $\mathrm{d} t_{\text {eff }}$ with a differential element of observed time $\mathrm{d} t$ :

$$
\mathrm{d} t_{\text {eff }}=F_{\xi(t), \xi_{\mathrm{bd}}} \mathrm{~d} t
$$Fig. 11.1 Stress $\xi(t)$ is ramped with time in a linear manner until the material/ device fails. The level of stress at failure/ breakdown is recorded to be $\xi_{\mathrm{bd}}$. The total time of the ramp to breakdown is $t_{\mathrm{bd}} . R(=\mathrm{d} \xi / \mathrm{d} t)$ is a constant ramp rate


Integrating both sides of the above equation to determine the effective time spent at $\xi_{\mathrm{bd}}$ for the entire ramp-to-breakdown test, one obtains:

$$
t_{\mathrm{eff}}=\int_{0}^{t_{\mathrm{bd}}} A F_{\xi(t), \xi_{\mathrm{bd}}} \mathrm{~d} t
$$

# 2 Linear Ramp Rate 

Let us determine the effective time $t_{\text {eff }}$ spent at $\xi_{\mathrm{bd}}$ during the linear ramp of $\xi(\mathrm{t})$, as illustrated in Fig. 11.1, where:

$$
\xi(t)=R t
$$

Ramping the stress with a constant ramp rate $R(=\mathrm{d} \xi / \mathrm{d} t)$ means that $t_{\mathrm{bd}}=\xi_{\mathrm{bd}} / R$.

### 2.1 Linear Ramp with Exponential Acceleration

Let us suppose that the acceleration factor in Eq. (11.2) is in the form of an exponential acceleration factor. From Chap. 10, one obtains:

$$
\mathrm{AF}_{\xi(t), \xi_{\mathrm{bd}}}=\exp \left\{\gamma\left[\xi(t)-\xi_{\mathrm{bd}}\right]\right\}
$$Equation (11.2) now becomes:

$$
\begin{aligned}
t_{\mathrm{eff}} & =\int_{0}^{\xi_{\mathrm{bd}} / R} \exp \left[\gamma\left(R t-\xi_{\mathrm{bd}}\right)\right] \mathrm{d} t \\
& =\exp \left[-\gamma \xi_{\mathrm{bd}}\right] \int_{0}^{\xi_{\mathrm{bd}} / R} \exp [\gamma R t] \mathrm{d} t \\
& =\exp \left[-\gamma \xi_{\mathrm{bd}}\right]\left[\frac{1}{\gamma R}\right]\left[\exp \left(\gamma \xi_{\mathrm{bd}}\right)-1\right] \\
& =\left[\frac{1}{\gamma R}\right]\left[1-\exp \left(-\gamma \xi_{\mathrm{bd}}\right)\right]
\end{aligned}
$$

Therefore, for an exponential acceleration factor, the linear ramp produces an effective time $t_{\text {eff }}$ spent at the breakdown strength $\xi_{\text {bd }}$ :

$$
t_{\mathrm{eff}}=\left[\frac{1}{\gamma R}\right]\left[1-\exp \left(-\gamma \xi_{\mathrm{bd}}\right)\right] \cong \frac{1}{\gamma R}
$$

where it is assumed in Eq. (11.6) that $\gamma \xi_{\mathrm{bd}}$ is large enough that the exponential term is much smaller than 1 . The fact that one has an expression for the effective time $t_{\text {eff }}$ spent at the breakdown level $\xi_{\mathrm{bd}}$ is very important. Coupled with the appropriate acceleration factor, $t_{\text {eff }}$ permits us to extrapolate from a breakdown value $\xi_{\mathrm{bd}}$ to a time-to-failure. The usefulness of $t_{\text {eff }}$ is illustrated in the next example problem.

# Example Problem 1 

To make sure that capacitors will last an expected lifetime (10 years at $105^{\circ} \mathrm{C}$ ), capacitors were randomly selected and then ramp-to-failure tested using a ramp rate of $R=\mathrm{d} E / \mathrm{d} t=1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$ at $105^{\circ} \mathrm{C}$. During ramp testing, it was determined that the weakest device had a breakdown strength of $E_{\mathrm{bd}}=10.5 \mathrm{MV} / \mathrm{cm}$. Assuming an exponential acceleration factor with $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$, determine the expected time-to-failure at an operational field of $5 \mathrm{MV} / \mathrm{cm}$.

## Solution

Since $\gamma E_{\mathrm{bd}}$ is large, then $\exp \left[-\gamma E_{\mathrm{bd}}\right] \ll 1$ and the effective time-to-failure at $E_{\mathrm{bd}}$ is given by:$$
t_{\mathrm{eff}} \cong \frac{1}{\gamma R}=\frac{1}{(4.0 \mathrm{~cm} / \mathrm{MV})(1 \mathrm{MV} / \mathrm{cm} / \mathrm{s})}=0.25 \mathrm{~s}
$$

Therefore, if the capacitors last 0.25 s at $E_{\mathrm{bd}}=10.5 \mathrm{MV} / \mathrm{cm}$ (and at $105^{\circ} \mathrm{C}$ ), then at a constant stress of $E=5.0 \mathrm{MV} / \mathrm{cm}$ (and at $105^{\circ} \mathrm{C}$ ) they would be expected to last:

$$
\begin{aligned}
T F_{E=5 \mathrm{MV} / \mathrm{cm}} & =A F_{E_{\mathrm{bd}}=10.5 \mathrm{MV} / \mathrm{cm}, E=5 \mathrm{MV} / \mathrm{cm}} \cdot(0.25 \mathrm{~s}) \\
& =\exp [(4.0 \mathrm{~cm} / \mathrm{MV})(10.5-5) \mathrm{MV} / \mathrm{cm}] \cdot(0.25 \mathrm{~s}) \\
& =8.96 \times 10^{8} \mathrm{~s}\left(\frac{1 \mathrm{~h}}{3,600 \mathrm{~s}}\right)\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right) \\
& =28 \text { years }
\end{aligned}
$$

Therefore, based on the sampling results using the linear-ramp breakdown test, the capacitors should safely meet the 10-year lifetime requirement.

# 2.2 Linear Ramp with Power-Law Acceleration 

Let us suppose that the acceleration factor in Eq. (11.2) is in the form of a power-law acceleration factor:

$$
\mathrm{AF}_{\xi(t), \xi_{\mathrm{bd}}}=\left\{\begin{array}{ll}
0 & {\left[\text { for } \xi(t) \leq \xi_{\text {yield }}\right]} \\
{\left[\frac{\xi(t)-\xi_{\text {yield }}}{\xi_{b d}-\xi_{\text {yield }}}\right]^{n}} & {\left[\text { for } \xi(t) \geq \xi_{\text {yield }}\right]}
\end{array}\right\}
$$

For reasons which will be established in Chap. 13, where mechanical stress is discussed in detail, an additional term has been inserted in Eq. (11.7) called the yield stress $\xi_{\text {yield }}$. Below $\xi_{\text {yield }}$, the stress $\xi(\mathrm{t})$ is expected to produce no damage to the material/device and thus the acceleration factor, as expressed by Eq. (11.7), is assumed equal to zero when the stress $\xi(\mathrm{t})$ is below $\xi_{\text {yield }}{ }^{1}$ Since a given material may or may not have a yield stress, then one must always question its existence. Using Eq. (11.7), Eq. (11.2) now becomes:

[^0]
[^0]:    ${ }^{1}$ One should always question the existence of a yield stress $\xi_{\text {yield }}$. Some materials have a yield stress, some do not. Even if a material has a reported yield point, a slight crack/defect existing in the material may have an adverse impact on the yield point. The stress riser at the crack-tip/defect may produce a local stress in the material well above the yield stress. Degradation would now be expected even though the average stress may be below $\xi_{\text {yield }}$.$$
\begin{aligned}
t_{\mathrm{eff}} & =\int_{0}^{\xi_{\mathrm{bd}} / R} \mathrm{AF}_{\xi(t), \xi_{\mathrm{bd}}} \mathrm{~d} t \\
& =\int_{\xi_{\text {yield }} / R}^{\xi_{\mathrm{bd}} / R}\left[\frac{\xi(t)-\xi_{\text {yield }}}{\xi_{\mathrm{bd}}-\xi_{\text {yield }}}\right]^{n} \mathrm{~d} t \\
& =\left[\frac{1}{\left(\xi_{\mathrm{bd}}-\xi_{\text {yield }}\right)}\right]^{n} \int_{\xi_{\text {yield }} / R}^{\xi_{\mathrm{bd}} / R}\left[R t-\xi_{\text {yield }}\right]^{n} \mathrm{~d} t \\
& =\left[\frac{1}{\xi_{\mathrm{bd}}-\xi_{\text {yield }}}\right]^{n}\left[\frac{\left(\xi_{\mathrm{bd}}-\xi_{\text {yield }}\right)^{n+1}}{R(n+1)}\right] \\
& =\frac{1}{n+1}\left[\frac{\xi_{\mathrm{bd}}-\xi_{\text {yield }}}{R}\right]
\end{aligned}
$$

Therefore, for a power-law acceleration factor, the linear-ramp test produces an effective time $t_{\text {eff }}$ at the breakdown strength $\xi_{\text {bd }}$ of:

$$
t_{\mathrm{eff}}=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{bd}}-\xi_{\text {yield }}}{R}\right]
$$

# Example Problem 2 

During the inspection of turbine blades, it was noted that small cracks existed at the base of the turbine blades. A potential reliability issue can develop if the cracks propagate during use and produce failure under the normal tensilestress conditions of rotation. A random selection of these turbine blades was tested using a linear ramp-to-failure test. The linear ramp rate used for the tensile stress was $\mathrm{R}=\mathrm{d} \sigma / \mathrm{d} t=10 \mathrm{MPa} / \mathrm{min}$ and the testing was done at the expected use temperature of $850^{\circ} \mathrm{C}$. The weakest turbine blade found during the ramp testing was $\sigma_{\text {rupture }}=200 \mathrm{MPa}$. Assuming that the use-condition tensile stress is 10 MPa , find the expected time-to-failure. Assume that a power-law model is appropriate with a stress dependence exponent of $n=$ 4 and, because of stress risers (discussed in Chap. 13) at the crack tips, $\sigma_{\text {yield }}$ is negligibly small.

## Solution

For the weakest turbine blade ( $\sigma_{\text {rupture }}=200 \mathrm{MPa}$ ) found during the linear ramp stress testing, the time-to-failure under this ramp testing was:

$$
\mathrm{TF}_{\oplus 200 \mathrm{MPa}}=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{bd}}}{R}\right]=\frac{1}{4+1}\left[\frac{200 \mathrm{MPa}}{10 \mathrm{MPa} / \mathrm{min}}\right]=4 \mathrm{~min}
$$The expected time-to-failure at the use condition of 10 MPa would be:

$$
\begin{aligned}
\mathrm{TF}_{\Theta \sigma=10 \mathrm{MPa}} & =\mathrm{AF}_{\sigma \text {-rupture }=200 \mathrm{MPa}, \sigma=10 \mathrm{MPa}} \cdot(4 \mathrm{~min}) \\
& =\left[\frac{200 \mathrm{MPa}}{10 \mathrm{MPa}}\right]^{4}(4 \mathrm{~min}) \\
& =6.40 \times 10^{5} \mathrm{~min} \\
& =6.40 \times 10^{5} \min \left(\frac{1 \mathrm{~h}}{60 \mathrm{~min}}\right)\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right) \\
& =1.2 \text { years. }
\end{aligned}
$$

# 3 Breakdown/Rupture Distributions 

The breakdowns/ruptures that are determined using the ramp-to-breakdown method may not be described well by the normal distribution (which is a symmetrical distribution). This occurs because the breakdowns/ruptures at the high end of the distribution are generally relatively tightly grouped. This is because the breakdowns/ ruptures are limited, on the high end of the distribution, by the fundamental strength of the material. However, at the lower end of the distribution, the breakdowns/ ruptures are generally more widely spread due to defects existing in the materials. For this reason, the Weibull distribution is often used to describe the inherent non-symmetrical breakdown/rupture data. This is illustrated in Fig. 11.2.

The Weibull probability density function $\mathrm{f}\left(\xi_{\mathrm{bd}}\right)$ for the breakdown/rupture values is given by:

$$
f\left(\xi_{\mathrm{bd}}\right)=\left[\frac{\beta}{\left(\xi_{\mathrm{bd}}\right)_{63}}\right]\left[\frac{\xi_{\mathrm{bd}}}{\left(\xi_{\mathrm{bd}}\right)_{63}}\right]^{\beta-1} \exp \left[-\left(\frac{\xi_{\mathrm{bd}}}{\left(\xi_{\mathrm{bd}}\right)_{63}}\right)^{\beta}\right]
$$



Fig. 11.2 The breakdown/rupture values, obtained from ramped-to-breakdown testing, can often be described by a Weibull distribution. Note that the Weibull distribution can be nonsymmetrical, favoring the lower breakdown values. This tends to more accurately reflect actual breakdown/ rupture data. The actual shape is a sensitive function of the Weibull slope $\beta$where $\left(\xi_{\mathrm{bd}}\right)_{63}$ is the characteristic Weibull value and $\beta$ is the Weibull slope, with the method for determination given in Chap. 7. The cumulative Weibull probability function is given by:

$$
F\left(\xi_{\mathrm{bd}}\right)=\int_{0}^{\xi_{\mathrm{bd}}} f\left(\xi_{\mathrm{bd}}\right) \mathrm{d} \xi_{\mathrm{bd}}=1-\exp \left[-\left(\frac{\xi_{\mathrm{bd}}}{\left(\xi_{\mathrm{bd}}\right)_{63}}\right)^{\beta}\right]
$$

# Example Problem 3 

During ramp-to-rupture testing of metal rods, the following rupture values were obtained:

| 637 MPa | 573 MPa | 712 MPa | 614 Mpa | 552 Mpa |
| :-- | :-- | :-- | :-- | :-- |
| 527 MPa | 593 Mpa | 666 Mpa | 497 Mpa | 453 Mpa |

(a) Find the Weibull parameters that give the best fitting to the rupture data.
(b) Plot the Weibull probability density function.

## Solution

(a) The Weibull best fitting parameters are given by:

## Weibull Distribution



The Weibull parameters that produce the best fitting to the rupture data are: (Rupture) $)_{63}=616 \mathrm{MPa}$ and $\beta=8.1$.
(b) The Weibull probability density function is shown below. Note that the distribution is asymmetrical and tends to favor the lower part of the rupture distribution. The lower value ruptures tend to occur more frequently because of defects in the materials.

# 4 Cautions for Ramp-to-Failure Testing 

One should note that the ramp-to-failure testing method can potentially be very fast. However, always remember the story of the lively chicks versus the hardboiled eggs in Sect. 4 in Chap. 10. One should confirm that the linear ramp test is only accelerating the physics of failure, not changing the physics of failure. To help insure that you are accelerating the right activation energy mechanism, always try to do the ramp test at the expected material/device operating temperature $T_{\text {op }}$. Also, make the ramp rate as slow ${ }^{2}$ as test time will permit. One should always take some constant-stress time-to-failure data, just to confirm that the time-to-failure projections from the ramp stress test are correct. Finally, some stresses, such as a current density stress in a conductor, can produce severe Joule/self-heating as the current-density stress is ramped. Thus, in a ramp test using current density, one might be investigating fusing physics as opposed to the intended electromigration physics. However, many of the stresses of interest (mechanical stress, electric-field stress, electrochemical stress, etc.) may not produce significant self-heating. As you build your confidence in the ramp-to-failure test method (assuming that the results from the ramp test closely match those of a constant-stress time-to-failure test), then the majority of your future testing may be the ramp-to-failure method of testing.

[^0]
[^0]:    ${ }^{2}$ Generally, the slower the ramp rate, the closer the ramp test results will match actual constantstress time-to-failure results.Fig. 11.3 Distribution $f$ $\left(\xi_{\mathrm{bd}}\right)$ of breakdown/rupture strengths as determined from a linear ramp-to-failure test. $\xi_{\mathrm{bd}}(F \%)$ represents the breakdown strength for a cumulative fraction $F$ of the devices. $\xi_{\text {op }}$ represents the expected constant-stress operational value


# 5 Transforming Breakdown/Rupture Distributions into Constant-Stress Time-to-Failure Distributions 

Shown in Fig. 11.3 is the breakdown/rupture $\xi_{\mathrm{bd}}$ distribution that was obtained from a linear ramp-to-failure test. The question is, how does one transform these breakdown/rupture values into an expected constant-stress $\xi_{\text {op }}$ time-to-failure distribution?

The time-to-failure for a cumulative fraction $F$ of the breakdown strengths is given by:

$$
\operatorname{TF}(F \%)=\mathrm{AF}_{\xi_{\mathrm{bd}}(F \%), \xi_{\mathrm{op}}} \cdot t_{\mathrm{eff}}
$$

where $t_{\text {eff }}$ is the effective time-to-failure at $\xi_{\mathrm{bd}}$ during the ramp testing.

### 5.1 Transforming Breakdown/Rupture Distribution to Time-to-Failure Distribution Using Exponential Acceleration

One would like to find the transformation equation for converting a breakdown/ rupture distribution into a time-to-failure distribution when one has exponential acceleration. Using Eqs. (11.6) and (11.12) with the exponential acceleration factor,

$$
\mathrm{AF}_{\xi_{\mathrm{bd}(F \%), \xi_{\mathrm{op}}}}=\exp \left\{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{op}}\right]\right\}
$$

gives:

$$
\operatorname{TF}(F \%)=\left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{op}}\right]\right\}
$$

In Eq. (11.14), $\gamma$ is the exponential acceleration parameter, $R(=\mathrm{d} \xi / \mathrm{d} t)$ is the linear ramp rate, $F \%$ is the percentage of devices that have a breakdown/rupture strength $\leq$ $\xi_{\mathrm{bd}}(\mathrm{F} \%)$, and $\xi_{\mathrm{op}}$ is the expected constant-stress operational value.# 5.2 Transforming Breakdown/Rupture Distribution to Time-to-Failure Distribution Using Power-Law Acceleration 

One would like to find the transformation equation for converting a breakdown/ rupture distribution into a time-to-failure distribution when one has power-law acceleration. Using Eqs. (11.9) and (11.12), with the power-law acceleration factor,

$$
\mathrm{AF}_{\xi_{\mathrm{bd}}(F \%), \xi_{\mathrm{op}}}=\left[\frac{\xi_{\mathrm{bd}}(F \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yie1d }}}\right]^{n}
$$

gives:

$$
\operatorname{TF}(F \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}-\xi_{\text {yield }}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(F \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yie1d }}}\right]^{n+1}
$$

In Eq. (11.16), $n$ is the power-law exponent for the acceleration, $R(=\mathrm{d} \xi / \mathrm{d} t)$ is the linear ramp rate, $F \%$ is the percentage of devices that have a breakdown/rupture strength $\leq \xi_{\mathrm{bd}}(F \%)$, and $\xi_{\mathrm{op}}$ is the expected constant-stress operational value. If the material exhibits a yield stress, $\xi_{\text {yield }}$, it is also included in Eq. (11.16).

## 6 Constant-Stress Lognormal Time-to-Failure Distributions from Ramp Breakdown/Rupture Data

As discussed in Chap. 7, the lognormal time-to-failure distribution is fully defined when the characteristic parameters $\left(t_{50}, r\right)$ are determined.

### 6.1 Exponential Acceleration

Given that the time-to-failure for exponential acceleration can be expressed by

$$
\operatorname{TF}(F \%)=\left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{op}}\right]\right\}
$$

the characteristic parameters for the lognormal distribution are given by:

$$
\operatorname{TF}(50 \%)=\left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(50 \%)-\xi_{\mathrm{op}}\right]\right\}
$$and

$$
\sigma_{\log \text { normal }}=\ln \left[\frac{\mathrm{TF}(50 \%)}{\mathrm{TF}(16 \%)}\right]=\gamma\left[\xi_{\mathrm{bd}}(50 \%)-\xi_{\mathrm{bd}}(16 \%)\right]
$$

# Example Problem 4 

Assuming exponential acceleration with acceleration parameter $\gamma$, show that if the breakdown/rupture strengths are normally distributed then the expected time-to-failure results will be lognormally distributed.

## Solution

From Eq. (11.19) one obtains:

$$
\begin{aligned}
\sigma_{\text {log normal }} & =\ln \left[\frac{\mathrm{TF}(50 \%)}{\mathrm{TF}(16 \%)}\right]=\gamma\left[\xi_{\mathrm{bd}}(50 \%)-\xi_{\mathrm{bd}}(16 \%)\right] \\
& =\gamma \sigma_{\text {normal }}
\end{aligned}
$$

Therefore, assuming exponential acceleration with acceleration parameter $\gamma$, if the breakdown strengths are normally distributed with standard deviation of $\sigma_{\text {normal }}$, the time-to-failure will be lognormally distributed with logarithmic standard deviation $\sigma_{\text {lognormal }}=\gamma \sigma_{\text {normal }}$.

### 6.2 Power-Law Acceleration

Given that the time-to-failure for power-law acceleration is given by

$$
\operatorname{TF}(F \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}-\xi_{\text {yield }}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(F \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yield }}}\right]^{n+1}
$$

the characteristic parameters for the lognormal distribution are given by:

$$
\begin{aligned}
& \operatorname{TF}(50 \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}-\xi_{\text {yield }}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(50 \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yield }}}\right]^{n+1} \\
& \sigma=\ln \left(\frac{\mathrm{TF}(50 \%)}{\mathrm{TF}(16 \%)}\right)=(n+1) \ln \left[\frac{\xi_{\mathrm{bd}}(50 \%)-\xi_{\text {yield }}}{\xi_{\mathrm{bd}}(16 \%)-\xi_{\text {yield }}}\right]
\end{aligned}
$$# 7 Constant-Stress Weibull Time-to-Failure Distributions from Ramp Breakdown/Rupture Data 

As discussed in Chap. 7, the Weibull time-to-failure distribution is fully defined when the characteristic parameters $\left(t_{63}, \beta\right)$ are determined.

### 7.1 Exponential Acceleration

Given that the time-to-failure for exponential acceleration is given by

$$
\operatorname{TF}(F \%)=\left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{op}}\right]\right\}
$$

the characteristic Weibull distribution parameters $\left(t_{63}, \beta\right)$ are given by:

$$
\operatorname{TF}(63 \%)=\left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(63 \%)-\xi_{\mathrm{op}}\right]\right\}
$$

and $^{3}$

$$
\beta=\frac{\ln [-\ln (1-F)]}{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{bd}}(63 \%)\right]}
$$

### 7.2 Power-Law Acceleration

Given that the time-to-failure for power-law acceleration is given by

$$
\operatorname{TF}(F \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}-\xi_{\text {yield }}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(F \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yie1d }}}\right]^{n+1}
$$

the characteristic parameters of the Weibull distribution are obtained by:

[^0]
[^0]:    ${ }^{3}$ Reminder-any cum fraction $F$ can be used to determine $\beta$ provided that the corresponding $\xi_{\mathrm{bd}}(F \%)$ is also used. If one chooses to use $F=0.1$, then $\beta=2.25 /\left\{\gamma\left[\xi_{\mathrm{bd}}(63 \%)-\xi_{\mathrm{bd}}(10 \%)\right]\right\}$.$$
\operatorname{TF}(63 \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}-\xi_{\text {yield }}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(63 \%)-\xi_{\text {yield }}}{\xi_{\mathrm{op}}-\xi_{\text {yield }}}\right]^{n+1}
$$

and $^{4}$

$$
\beta=\frac{\ln [-\ln (1-F)]}{(n+1) \ln \left[\frac{\xi_{\mathrm{bd}}(F \%)-\xi_{\text {yield }}}{\xi(63 \%)-\xi_{\text {yield }}}\right]}
$$

where $n$ is the power-law exponent and $R(=\mathrm{d} \xi / \mathrm{d} t)$ is the constant ramp rate used to determine the breakdown strength $\xi_{\mathrm{bd}}$.

# Example Problem 5 

During the ramp-breakdown testing of capacitors (caps) at $105^{\circ} \mathrm{C}$ with a ramp rate of $\mathrm{R}=1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$, it was determined that $10 \%$ of the caps break down at a field of $\leq 10.5 \mathrm{MV} / \mathrm{cm}$ and $63 \%$ of the caps at $\leq 11 \mathrm{MV} / \mathrm{cm}$. If the devices are operated at a constant stress of $5 \mathrm{MV} / \mathrm{cm}$, what are the expected Weibull time-to-failure distribution parameters $t_{63}$ and $\beta$ ?

1. Assume an exponential acceleration, with $\gamma=4 \mathrm{~cm} / \mathrm{MV}$.
2. Assume a power-law acceleration, with $n=42$ and $\xi_{\text {yield }}=0$

## Solution

1. For exponential acceleration, at $105^{\circ} \mathrm{C}$, Eq. (11.23) gives:

$$
\begin{aligned}
\operatorname{TF}(63 \%)= & \left(\frac{1}{\gamma R}\right) \exp \left\{\gamma\left[\xi_{\mathrm{bd}}(63 \%)-\xi_{\mathrm{op}}\right]\right\} \\
= & \left(\frac{1}{(4.0 \mathrm{~cm} / \mathrm{MV})(1 \mathrm{MV} / \mathrm{cm} / \mathrm{s})}\right) \\
& \cdot \exp \{(4.0 \mathrm{~cm} / \mathrm{MV})(11 \mathrm{MV} / \mathrm{cm}-5 \mathrm{MV} / \mathrm{cm})\} \\
= & 6.62 \times 10^{9} \mathrm{~s}\left(\frac{1 \mathrm{~h}}{3,600 \mathrm{~s}}\right)\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right) \\
= & 210 \text { years. }
\end{aligned}
$$

The expected Weibull slope $\beta$ from Eq. (11.25) is:
(continued)

[^0]
[^0]:    ${ }^{4}$ If one uses $F=0.1$ then $\beta=2.25 /\left\{(n+1) \ln \left[\xi_{\mathrm{bd}}(63 \%) / \xi_{\mathrm{bd}}(10 \%)\right]\right\}$.$$
\begin{aligned}
\beta & =\frac{\ln [-\ln (1-F)]}{\gamma\left[\xi_{\mathrm{bd}}(F \%)-\xi_{\mathrm{bd}}(63 \%)\right]} \\
& =\frac{\ln [-\ln (1-0.1)]}{(4.0 \mathrm{~cm} / \mathrm{MV})[10 \mathrm{MV} / \mathrm{cm}-10.5 \mathrm{MV} / \mathrm{cm}]} \\
& =1.13
\end{aligned}
$$

2. For power-law acceleration at $105^{\circ} \mathrm{C}$ and no yield point, Eq. (11.26) gives:

$$
\begin{aligned}
\operatorname{TF}(63 \%) & =\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}[63 \%]}{\xi_{\mathrm{op}}}\right]^{n+1} \\
& =\frac{1}{43}\left[\frac{5 \mathrm{MV} / \mathrm{cm}}{1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}}\right]\left[\frac{11 \mathrm{MV} / \mathrm{cm}}{5 \mathrm{MV} / \mathrm{cm}}\right]^{43} \\
& =6.16 \times 10^{13} \mathrm{~s}\left[\frac{1 \mathrm{~h}}{3,600 \mathrm{~s}}\right]\left[\frac{1 \text { year }}{8,760 \mathrm{~h}}\right] \\
& =1.95 \times 10^{6} \text { years. }
\end{aligned}
$$

The expected Weibull slope $\beta$ is given by Eq. (11.28):

$$
\begin{aligned}
\beta & =\frac{\ln [-\ln (1-F)]}{(n+1) \ln \left[\frac{\xi_{\mathrm{bd}}(F \%)}{\xi_{\mathrm{bd}}(63 \%)}\right]} \\
& =\frac{\ln [-\ln (1-0.1)]}{(42+1) \ln \left[\frac{10.5 \mathrm{MV} / \mathrm{cm}}{11 \mathrm{MV} / \mathrm{cm}}\right]} \\
& =1.12
\end{aligned}
$$

# Problems 

1. Capacitor dielectrics were randomly selected and ramp-to-breakdown tested at $105^{\circ} \mathrm{C}$, using a linear ramp rate of $R=\mathrm{d} E / \mathrm{d} t=0.5 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$. During ramp-tobreakdown testing, it was determined that the breakdown distribution could be approximated by a normal distribution with: $\left(E_{\mathrm{bd}}\right)_{50}=12 \mathrm{MV} / \mathrm{cm}$ and $\sigma=1.0$ $\mathrm{MV} / \mathrm{cm}$. Determine the expected time-to-failure for $1 \%$ of the capacitors at an operational field of $5 \mathrm{MV} / \mathrm{cm}$ at $105^{\circ} \mathrm{C}$. Assume an exponential acceleration factor with $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$.

Answer: $\operatorname{TF}(1 \%)=2.1$ years2. Turbine blades were randomly selected and ramped-to-rupture at $700^{\circ} \mathrm{C}$ using a tensile stress with a linear ramp rate of $R=\mathrm{d} \sigma_{\text {stress }} / \mathrm{d} t=5 \mathrm{MPa} / \mathrm{min}$. During ramp-to-rupture testing, it was determined that the rupture distribution could be approximated by a normal distribution with: $\left(\sigma_{\text {rupture }}\right)_{50}=250 \mathrm{MPa}$ with a standard deviation of $\sigma=25 \mathrm{MPa}$. Determine the expected time-to-failure for $1 \%$ of the turbine blades at an operational tensile stress of 15 MPa at $700{ }^{\circ} \mathrm{C}$. Assume a power-law acceleration factor with $n=4.0$ and (because of small cracks) no yield point.

Answer: $\operatorname{TF}(1 \%)=0.4$ years
3. Analyze Problem 1 except this time, assume a power-law acceleration with $n=40$.

Answer: $\operatorname{TF}(1 \%)=4,297$ years
4. Analyze Problem 2, except this time assume an exponential acceleration with $\gamma=0.06 / \mathrm{MPa}$.

Answer: $\operatorname{TF}(1 \%)=0.3$ years
5. Steel pipes were randomly selected for pressurizing-to-rupture testing. Using a linear ramp rate of $R=\mathrm{d} P / \mathrm{d} t=5 \mathrm{kpsi} / \mathrm{min}$, the rupture data tended to obey a Weibull distribution with $\left(P_{\text {rupture }}\right)_{63}=200 \mathrm{kpsi}$ and a Weibull slope of $\beta=10$. Determine the expected time-to-failure for $1 \%$ of the pipes at an operational pressure of 5 kpsi . Assume that the stress in the cylindrical pipes is directly proportional to the pressure and assume a power-law acceleration factor with an exponent of $n=4$ and (because of small cracks) no yield point.

Answer: $\operatorname{TF}(1 \%)=3.9$ years
6. Suspension cables were randomly selected for tensile stressing-to-rupture testing. Using a linear ramp rate of $R=\mathrm{d} \sigma_{\text {Tensile }} / \mathrm{d} t=4 \mathrm{kpsi} / \mathrm{min}$, the rupture data tended to obey a Weibull distribution with $\left(\sigma_{\text {rupture }}\right)_{63}=250 \mathrm{kpsi}$ and a Weibull slope of $\beta=12$. Determine the expected time-to-failure for $1 \%$ of the cables at an operational pressure of 2 kpsi . Assume a power-law acceleration factor with an exponent of $n=4$ and (because of small defects) no yield point.

Answer: $\operatorname{TF}(1 \%)=854$ years
7. With no yield point, Eq. (11.16) reduces to:

$$
\operatorname{TF}(F \%)=\frac{1}{n+1}\left[\frac{\xi_{\mathrm{op}}}{R}\right]\left[\frac{\xi_{\mathrm{bd}}(F \%)}{\xi_{\mathrm{op}}}\right]^{n+1}
$$

which is valid when the stress $\xi$ is linearly ramped at a constant rate $R(R=\mathrm{d} \xi / \mathrm{d} t$ $=$ constant) until failure occurs. Show that, if the stress is proportional to the power-law of some other parameter $S$,$$
\xi=C_{o} S^{m}
$$

then the time-to-failure equation becomes:

$$
\operatorname{TF}(F \%)=\frac{1}{n+1}\left[\frac{S_{\mathrm{op}}^{m}}{R_{1}}\right]\left[\frac{S_{\mathrm{bd}}(F \%)}{S_{\mathrm{op}}}\right]^{m(n+1)}
$$

where the ramp rate $R_{1}$ is given by:

$$
R_{1}=m S^{m-1}\left(\frac{\mathrm{~d} S}{\mathrm{~d} t}\right)=\text { constant }
$$

8. Using the results from Problem 7, metal storm shutters with small cracks were randomly selected for storm testing. The shutters were tested in a wind tunnel by ramping the wind speed $S$ until the shutters failed. The stress $\sigma$ in the shutters, due to the wind, is proportional to the square of the wind speed: $\sigma=C_{o} S^{2}$. Using a constant ramp rate of $R_{1}=2 S(\mathrm{~d} S / \mathrm{d} t)=10(\mathrm{mph})^{2} / \mathrm{min}$, the failure data tended to obey a Weibull distribution with $(S)_{63}=100 \mathrm{mph}$ and a Weibull slope of $\beta=10$. Determine the expected time-to-failure for $1 \%$ of the shutters with a nominal constant wind speed of 25 mph . Assume a power-law acceleration factor of at least $n=6$, and because of the small cracks, no yield point.

Answer: $\operatorname{TF}(1 \%)=7.2$ years

# Bibliography 

Anolick, E. and G. Nelson: Low-Field Time-Dependent Dielectric Breakdown, IEEE International Reliability Symposium Proceedings, 8 (1979).
Berman, A.: Time-Zero Dielectric Breakdown by a Ramp Method, IEEE International Reliability Symposium Proceedings, 204 (1981).
McPherson, J.: Stress-Dependent Activation Energy, IEEE International Reliability Symposium Proceedings, 12 (1986).# Chapter 12 <br> Time-to-Failure Models for Selected Failure Mechanisms in Integrated Circuits 

Advanced integrated circuits (ICs) are very complex, both in terms of their design and in their usage of many dissimilar materials (semiconductors, insulators, metals, plastic molding compounds, etc.). For cost reductions per device and improved performance, scaling of device geometries has played a critically important role in the success of semiconductors. This scaling-where device geometries are generally reduced by $0.7 \times$ for each new technology node and tend to conform to Moore's Law ${ }^{1}$ —has caused the electric fields in the materials to rise (bringing the materials ever closer to their breakdown strength) and current densities in the metallization to rise causing electromigration (EM) concerns. The higher electric fields can accelerate reliability issues such as: time-dependent dielectric breakdown (TDDB), hot-carrier injection (HCI), and bias temperature instability (BTI). In addition, the use of dissimilar materials in a chip and in the assembly process produces a number of thermal expansion mismatches which can drive large thermomechanical stresses. These thermomechanical stresses can result in failure mechanisms such as stress migration (SM), creep, fatigue, cracking, delaminating interfaces, etc.

## 1 Electromigration

EM has historically been a significant reliability concern for both Al-based and Cu-based metallizations. As illustrated in Fig. 12.1, due to the momentum exchange between the current carrying electrons and the host metal lattice, metal ions can drift

[^0]
[^0]:    ${ }^{1}$ Moore's Law, attributed to Gordon Moore, states that the transistor density on ICs tends to double every $18-24$ months.

Fig. 12.1 For high-electron current densities $J^{(e)}$, the electron wind (collisions of the electrons with the metal ions in the lattice) serves to exert a force $F$ on the metal ion which is large enough to cause the metal ion $M^{*}$ to drift from the cathode toward the anode. Generally, this metal-ion movement is along grain boundaries in Al-alloys and along interfaces with copper


Fig. 12.2 Electromigration-induced transport (and eventual flux divergence) has produced severe voiding in the Al metal lead shown. The voiding will cause a resistance rise in the metal line/ stripe/ lead, eventually impacting device functionality. In the case shown here, the metal-ion flux is $J_{\text {out }}>$ $J_{\text {in }}$, thus voiding occurs
under the influence of the electron wind. The force $F$ exerted on a metal ion due to the electron wind is directly proportional to the electron current density $J^{(e)}$,

$$
F=\rho_{0} z^{*} e J^{(e)}
$$

where $\rho_{0}$ is the resistivity of the metal, and $z^{*} e$ is the effective metal-ion charge.
Eventually, due to a flux divergence ${ }^{2}$ (caused by gradients in microstructure, temperature, stress, impurities, etc.), vacancies ${ }^{3}$ will start to cluster; the cluster can grow into a void; and finally the void growth will continue until the conductor reaches a resistive or open-circuit condition. This can be an important failure mechanism for ICs where the current densities in the metal stripes/leads can easily approach and even exceed a mega-amp per square centimeter $\left(\mathrm{MA} / \mathrm{cm}^{2}\right)$. Shown in Fig. 12.2 is a metal conductor which was stressed at $2 \mathrm{MA} / \mathrm{cm}^{2}$ and at $150^{\circ} \mathrm{C}$ for a few 100 h . Note the severe EM-induced voiding which has occurred in this test line/ lead/stripe.

[^0]
[^0]:    ${ }^{2}$ Recall from Chap. 5 that a flux divergence represents the net flow of material into or out of a region of interest. A flux divergence can result in the accumulation or depletion of metal ions in the region of interest. Microstructure differences, such as grain size differences, can result in flux divergences. ${ }^{3}$ Vacancy is simply a vacant lattice site. A vacancy represents free space (a missing atom) and, as such, a clustering of vacancies can result in void formation. A discussion of vacancies can be found in Chap. 13.

Fig. 12.3 Electromigration-induced transport is primarily along grain boundaries in polycrystalline Al-alloy conductors. (a) Two regions of uniform grain structure are illustrated. (b) Electron flow $J^{(e)}$ from left to right can serve to produce a void in the metal due to the flux divergence at the microstructure gradient. (c) Electron flow from right to left can produce an accumulation of metal due to the flux divergence at the microstructure gradient. The dominant electromigration-transport mechanism for Cu can be along the $\mathrm{Cu} /$ barrier interfaces

For Al-alloys, the metal-ion transport is primarily along grain boundaries (for temperatures $T<T_{\text {melt }} / 2$ ). ${ }^{4}$ Two idealized regular/uniform grain structures are illustrated in Fig. 12.3. ${ }^{5}$ The transport of metal ions due to the electron wind, coupled with a flux divergence due to a microstructure gradient, as illustrated in Fig. 12.3, can cause either voiding or accumulations to occur. The void nucleation phase generally has little/no impact on the electrical resistance rise in the metal stripe. The void growth-phase, however, can cause local current crowding and a rise in resistance for the metal stripe.

If the metallization is actually an Al-alloy/barrier-metal laminate, then the resistance rise may show a time delay $t_{0}$ and then a gradual rise as illustrated in Fig. 12.4. This gradual rise in resistance, of course, assumes that the barrier metal is electromigration resistant. Some commonly used electromigration-resistant barriers in integrated circuit applications include: TiW, TiN, and TaN. Without a barrier layer

[^0]
[^0]:    ${ }^{4}$ Grain boundary (or interface) transport generally dominates for $T<0.5 T_{\text {melt }}$, where $T_{\text {melt }}$ is the melting temperature of the metal (expressed in Kelvin). Bulk (within grain or lattice) transport can dominate for $T>0.5 T_{\text {melt }}$. The activation energy for grain-boundary transport $Q_{\mathrm{gb}}$ is roughly half that of bulk transport $Q_{\text {bulk }}$.
    ${ }^{5}$ Grain sizes are not really as regular/uniform as illustrated in Fig. 12.3. Grain sizes are generally lognormally distributed.Fig. 12.4 Electromigrationinduced resistance rise in layered metal stripes (e.g., $\mathrm{Al}-\mathrm{Cu} / \mathrm{TiN}$ ) shows little/no resistance rise initially for a time $t_{0}$ and then a gradual rise in resistance. The TiN layer serves as an electromigration-resistant shunting layer to prevent catastrophic resistance rises (open-circuit conditions)


Fig. 12.5 (a) Al-alloy interconnect system for ICs. Grain-boundary (GB) transport in Al-alloy usually dominates EM performance. Flux-divergence/voiding is often associated with the W-plug via. (b) Copper interconnect system for ICs. Interfacial transport associated with the $\mathrm{Cu} /$ barrier interfaces usually dominates the EM performance. Flux-divergence/voiding is often associated with the via
present to participate in shunting the current, the rise in resistance for the Al-alloy can be very abrupt for EM-induced damage. The use of barriers is illustrated in Fig. 12.5.

For pure copper metallization, the dominant diffusion path during EM testing is generally along interfaces, rather than along grain boundaries as in Al-alloys. Unlike aluminum, which forms a strongly bonded Al -oxide layer $\left(\mathrm{Al}_{2} \mathrm{O}_{3}\right)$ on its surface, Cu -oxide is relatively poorly bonded to the Cu surface. This can provide a high mobility interface for the Cu -ion transport. In order to reduce Cu -ion mobility along such interfaces, the Cu should be tightly bounded by well-adhering barrier layers.

Fig. 12.6 Shown is a pictorial (on the left) of where EM-induced damage might be expected in Cu interconnects. Shown on right is the actual EM-induced voiding

Normally, the bottom and sidewalls of the Cu lead are bounded by a TiN or TaN barrier, while the top of the Cu lead has a dielectric barrier such as $\mathrm{SiN}, \mathrm{SiCOH}$, or SiCON. During EM transport, the Cu -ions will select one or more of the weak interfaces. (See Fig. 12.6 for typical failing locations.)

While differences in the materials properties between Cu and Al can dominate the mass transport mechanism, Cu metallization is also distinguished from Al because it is fabricated differently using the so-called damascene or dual-damascene process flow (refer to Fig. 12.5b). Damascene processes are used, rather than the physical/ sputter-deposition and subtractive-etch processes used to make Al-alloy interconnects, because of better filling characteristics and because of difficulties with developing plasma etches for the Cu metallization.

In the damascene process flow, trenches are first etched into a dielectric layer (where the metallization will eventually go) and then the trenches are lined with a metal barrier material (such as Ta-based metallization) and a thin, physically vapordeposited Cu seed-layer. This trench feature is then filled with Cu metallization using an electroplating process $(E P)$. This is followed by chemical mechanical polishing (CMP) and subsequent cleans to define the interconnect geometry. Next, the Cu is capped by a sealing barrier layer, usually a dielectric barrier material.

In the dual-damascene process, the via openings are also formed in addition to the trench such that via and trench are not separated by a metal barrier as would be the case for single damascene interconnects. In dual-damascene Cu , a flux barrier (due to the use of a barrier) is present at the bottom of via. ${ }^{6}$ This somewhat complicated interconnect architecture, utilizing dielectric and metal barriers with different interface properties, exhibits a number of flux divergence locations not seen in Al metallization. For electron flow up into a via (up-direction EM), a flux divergence is located at the top corner of the trench. For down-direction EM, the flux divergence location is along the top surface of the lower metal trench where the metal barrier of

[^0]
[^0]:    ${ }^{6}$ Via is the term used to describe the physical/electrical connection of an upper level of metal to a lower level of metal through a dielectric layer.the via and the dielectric cap (on the lower metal trench) meet. The voiding volumes necessary to cause severe resistance rises are also somewhat different for the two cases, leading to the general observation that down-direction EM failures occur somewhat faster than up-direction EM. ${ }^{7}$ Additionally, defects present within a via may lead to premature EM failure (early or weak-mode failure) for an up-direction interconnect.

The presence of weak interfaces in Cu metallization, due to the fact that Cu does not form a strongly adhering native oxide, means that optimization of interfacial adhesion strength between Cu and the capping layer is critically important. Studies have shown that improvements in interfacial adhesion strength will improve EM performance. Also, when the interfacial adhesion is extremely good, as the case with Co-cladding of the Cu , the EM performance improves dramatically and the Cu EM performance can then be primarily limited by bulk diffusion, with a corresponding increase in activation energy $Q$.

Since electromigration transport is a mass conserving process then, in addition to the voiding problems, accumulations of the transported metal ions will also occur thus increasing the mechanical stress in the metallization and surrounding dielectrics. This localized buildup of stress in the metallization will serve to generate a backflow of metal ions (the Blech effect). For shorter leads (generally a few tens of microns), the Blech effect can be so strong that the backflow of metal ions will cancel the drift component ${ }^{8}$ and electromigration-induced failure can be retarded. However, the buildup of mechanical stress in the metal lead is also accompanied by a buildup of opposing mechanical stress in the surrounding dielectrics which can cause potential fracturing of the surrounding dielectrics. Fracture of the surrounding dielectrics can facilitate the shorting of the test lead to the adjacent metal leads. For advanced Cu metallizations, which require low-k dielectrics that are relatively mechanically weak, this potential shorting failure mechanism may need to be considered.

The model generally used to describe EM time-to-failure takes the form

$$
\mathrm{TF}=A_{0}\left(J^{(e)}-J_{\mathrm{crit}}^{(e)}\right)^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
$$

where:
$A_{0}$ is a process/material-dependent coefficient. This coefficient can vary from device-to-device and is the reason that the time-to-failure TF is actually a distribution of times-to-failure. The device-to-device variation ( $A_{0}$ variation) can be as subtle as slight microstructure differences in the metallization. A lognormal TF distribution is generally used for EM failure mechanisms.

[^0]
[^0]:    ${ }^{7} U p$ (into via) or down (into via) refers to the electron-flow direction.
    ${ }^{8}$ Drift and diffusion (backflow) mechanisms were discussed in Chap. 7. If the backflow pressure (created by the accumulation of material) starts to cancel the drift-induced pressure, then net material flow ceases.$J^{(e)}$ is the electron current density. $J^{(e)}$ must be greater than $J_{\text {crit }}^{(e)}$ to produce failure. $J_{\text {crit }}^{(e)}$ is a critical (threshold) current density which must be exceeded before significant EM damage is expected. $J_{\text {crit }}^{(e)}$ can be determined from the Blech length equation: $\left(J^{(e)} \cdot L\right)_{\text {crit }}=A_{\text {Blech }}$. For aluminum alloys, $A_{\text {Blech }} \cong 6,000 \mathrm{~A} / \mathrm{cm}$. For $\mathrm{Cu}, A_{\text {Blech }}=1,000$ to $4,000 \mathrm{~A} / \mathrm{cm}$, depending on the mechanical strength of the surrounding dielectrics and barrier materials. If the test stripe length is $>250 \mu \mathrm{~m}$, then $J_{\text {crit }}^{(e)}$ is typically small compared to the normal EM stressing current density of $>1 \mathrm{MA} / \mathrm{cm}^{2}$. For this reason, $J_{\text {crit }}^{(e)}$ is often ignored. However, the Blech effect may be an important design consideration for very short conductor lengths.
$n$ is the current density exponent. $n=2$ is normally used for aluminum-alloys and $n=1$ for Cu .
$Q$ is the activation energy. $Q=0.5-0.6 \mathrm{eV}$ is generally used for Al and $\mathrm{Al}-\mathrm{Si}$, $Q=0.7-0.9 \mathrm{eV}$ is used for $\mathrm{Al}-\mathrm{Cu}$ alloys, and $Q=1.0 \mathrm{eV}$ for pure Cu .

For Al-alloys, time-to-failure will generally show a metal-width dependence, with the worst case (smallest time-to-failure) occurring for metal widths approximately 2 times the mean grain size. ${ }^{9}$ As for copper, the worst-case EM performance generally occurs with the most narrow metal widths.

# Example Problem 1 

Find the Blech length when a current density of $\mathrm{J}^{(\mathrm{e})}=1 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ is flowing through an aluminum alloy conductor.

## Solution

For aluminum alloys, the Blech relation becomes:

$$
\begin{aligned}
& \left(J^{(e)} \cdot L\right)_{\text {crit }} \leq 6,000 \mathrm{~A} / \mathrm{cm} \\
& \Rightarrow L_{\text {crit }} \leq \frac{6,000 \mathrm{~A} / \mathrm{cm}}{1 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}}=6.0 \times 10^{-3} \mathrm{~cm}=60 \mu \mathrm{~m}
\end{aligned}
$$

In summary, for a current density of $1 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ flowing through an aluminum-alloy conductor, the electromigration-induced damage should be relatively small for conductors of length less than $60 \mu \mathrm{~m}$. This assumes, of course, that the conductor is adequately constrained by the covering dielectric layer(s) so that the backflow stresses can develop fully and thus retard the void growth. If the voiding is in the form of a very thin slit-like void, the backflow stress may not be strong enough to prevent EM failure. For this reason, the most conservative design approach is to assume that $J_{\text {crit }}=0$.

[^0]
[^0]:    ${ }^{9}$ For Al-alloys, stripe widths of approximately $3 \mu \mathrm{~m}$ are typically used for EM testing.# Example Problem 2 

Under typical Al-alloy electromigration testing conditions, the stress current densities are $J_{\text {stress }}^{(e)} \sim 1 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and the length of test structures is $L \sim$ $1,000 \mu \mathrm{~m}$. Under these stress conditions, show that $J_{\text {crit }}^{(e)}$ is much smaller than $J_{\text {stress }}^{(e)}$ and can therefore be safely neglected during electromigration testing.

## Solution

The Blech relation gives for Al-alloys:

$$
\begin{aligned}
& \left(J^{(e)} \cdot L\right)_{\text {crit }} \leq 6,000 \mathrm{~A} / \mathrm{cm} \\
& \Rightarrow J_{\text {crit }}^{(e)} \leq \frac{6,000 \mathrm{~A} / \mathrm{cm}}{1,000 \mu \mathrm{~m}} \cdot\left(\frac{1 \mu \mathrm{~m}}{10^{-4} \mathrm{~cm}}\right)=6.0 \times 10^{4} \mathrm{~A} / \mathrm{cm}^{2}
\end{aligned}
$$

Therefore, typically during electromigration testing, $J_{\text {crit }}^{(e)} \ll J_{\text {stress }}^{(e)} \sim 10^{6}$ $\mathrm{A} / \mathrm{cm}^{2}$ and can usually be safely neglected. Since the Blech constant $A_{\text {Blech }}$ for $\mathrm{Cu}(1,000-4,000 \mathrm{~A} / \mathrm{cm})$ is typically smaller than for Al-alloys, then $J_{\text {crit }}^{(e)}$ is usually smaller for Cu versus Al-alloys.

## Example Problem 3

Under accelerated electromigration testing of an Al-alloy, at a current density of $J_{\text {stress }}=2 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and at a metal temperature of $T_{\text {stress }}=200^{\circ} \mathrm{C}$, the EM data was found to be fitted well by a lognormal distribution with median time-to-failure of $t_{50}=200 \mathrm{~h}$ and a logarithmic standard deviation of $\sigma=0.5$. Assuming an activation energy of $Q=0.8 \mathrm{eV}$ and a current density exponent of $n=2$, what is the maximum design current density $J_{\text {design }}$ to produce fewer than $0.13 \%$ failures in 10 years at $105^{\circ} \mathrm{C}$ ?

## Solution

Recall from Chap. 10 that:

$$
\mathrm{AF}=\frac{(\mathrm{TF})_{\text {operation }}}{(\mathrm{TF})_{\text {stress }}}=\left[\frac{J_{\text {stress }}}{J_{\text {design }}}\right]^{2} \exp \left\{\frac{Q}{K_{B}}\left(\frac{1}{T_{\text {design }}}-\frac{1}{T_{\text {stress }}}\right)\right\}
$$

During stress, the time-to-fail for $0.13 \%$ of the devices (lognormal distribution from Chap. 7) is:

$$
\left(\mathrm{TF}_{0.13 \%}\right)_{\text {stress }}=\frac{t_{50}}{\exp (3 \sigma)}=\frac{200 \mathrm{~h}}{\exp [(3)(0.5)]}=44.63 \mathrm{~h}
$$To last 10 years at $105^{\circ} \mathrm{C}$, one will need an acceleration factor of:

$$
\mathrm{AF}=\frac{10 \text { years }}{44.63 \mathrm{~h}}=\frac{87,600 \mathrm{~h}}{44.63 \mathrm{~h}}=1962.8
$$

Solving the first equation above for $J_{\text {design }}$, one obtains:

$$
\begin{aligned}
J_{\text {design }} & =J_{\text {stress }} \sqrt{\frac{\exp \left\{\frac{Q}{K_{B}}\left(\frac{1}{T_{\text {design }}}-\frac{1}{T_{\text {stress }}}\right)\right\}}{A F}} \\
& =2 \times 10^{6} \frac{\mathrm{~A}}{\mathrm{~cm}^{2}} \sqrt{\frac{\exp \left\{\frac{0.8 \mathrm{eV}}{8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}}\left(\frac{1}{(105+273) \mathrm{K}}-\frac{1}{(200+273) \mathrm{K}}\right)\right\}}{1962.8}} \\
& =5.3 \times 10^{5} \frac{\mathrm{~A}}{\mathrm{~cm}^{2}}
\end{aligned}
$$

In summary, based on the stated EM data and the planned use conditions for this metallization, the design current density should be limited to approximately $J_{\text {design }}=5.3 \times 10^{5} \mathrm{~A} / \mathrm{cm}^{2}$.

EM data is normally collected under DC conditions whereas the circuit operation is AC. This means that a method is needed to transform AC current densities into DC EM equivalents for design rule checking. For unipolar-current waveforms, $J^{(e)}$ can be taken as the average current density $\left\langle J^{(e)}\right\rangle$. For bipolar current waveforms, a sweepback recovery action can take place and the effective current density $J^{(e)}$ has been described by $J^{(e)}=\left\langle J_{+}^{(e)}\right\rangle-r\left\langle J_{-}^{(e)}\right\rangle$, where $\left\langle J_{+}^{(e)}\right\rangle$ is the average of the positive polarity pulses and $\left\langle J_{-}^{(e)}\right\rangle$ is the average of the negative polarity pulses. ${ }^{10}$ The recovery coefficient $r$ has a reported value of at least 0.7 . While bipolar waveforms permit much more allowed current density to flow for EM reasons, one needs to be careful with Joule heating and limit $J_{\mathrm{rms}}$.

Electromigration associated with vias must be investigated separately because they show characteristics which are different from single leads fed by bonding pads. For example, vias can show different degradation rates depending on electron current flow direction [upper level of metal (M2) to lower level of metal (M1) may

[^0]
[^0]:    ${ }^{10}$ It is assumed here that the average of the positive pulses is greater than the average of the negative pulses.be quite different versus M1 to M2]. Also, the degradation rate is strongly dependent on via structure (barrier layer, capping layer, and via etching), via number, layout, and a reservoir effect ${ }^{11}$ can be present.

For Al alloy stripes, terminated by bonding pads and having no barrier metallization, the total time-to-failure is dominated by nucleation and $n$ is observed to be equal to 2 (which is commonly referred to as the Black equation). ${ }^{12}$ However, for Al-alloy stripes with barrier metal and terminated by tungsten plugs, one may see both an incubation (nucleation) period dominated by $n=2$ and a resistance rise (drift period) dominated by $n=1$ (as illustrated in Fig. 12.4). Also, under high current density test conditions, unaccounted for Joule heating can produce apparent current density exponents much greater than $n=2$. Similar observations hold for Cu metallization, where a mixture of void nucleation and void growth contributions is often simultaneously present; however, the trend appears to be weighted more toward growth-controlled EM and $n=1$ is generally used for Cu . In summary, one may need to be a little cautious (as described in Chap. 10) when extrapolating highly accelerated data to the expected operating conditions.

IC metallization must be used to make contact to shallow ( $<0.25 \mu \mathrm{~m}$ ) $\mathrm{n}^{+}$and $\mathrm{p}^{+}$ junctions in CMOS technologies. Being able to build stable/reliable contacts necessitates that a barrier metal be used between the interconnect metal and the shallow junction. Some common barrier metals often used are TiW, TiN, and TaN. During contact electromigration transport, the dominant diffusing species which causes contact failure is reported to be silicon from the contact region. In addition to the barrier type being important, silicided junctions can also be important relative to retarding the transport process.

Equation (12.2) can also be used to describe IC contacts (metal to silicon or silicide) failure due to electromigration. Here, however, the diffusing species which leads to failure is generally the silicon. Contact electromigration failure occurs when a buildup of silicon occurs in the contact window (assuming that silicon is in the aluminum-alloy metallization initially) leading to resistive contact formation; or, an erosion of silicon from the contact window can lead to junction leakage and failure. Since the current crowding can be severe in a shallow contact, the actual current density is non-uniform over the contact window and may be very difficult to specify. For this reason, normally the contact area is incorporated into the process-dependent prefactor $A_{0}$ and the time-to-failure equation is usually written as:

$$
\mathrm{TF}=A_{0} I^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
$$

[^0]
[^0]:    ${ }^{11}$ Tabs (extra metal extensions) at the cathode-end connection (acting as a reservoir/source of additional metal ions) can slow down the voiding rate and thus can improve the time-to-failure.
    ${ }^{12} \mathrm{Jim}$ Black was the first to propose a current density exponent of $n=2$ for electromigration in Al-alloys, without barrier layers, where the void nucleation phase tends to dominate the time-tofailure. However, $n=2$ is not valid for all metal systems, e.g., $n=1$ is used for Cu metallization.where $I$ is the current flowing into or out of the contact window during EM testing. ${ }^{13}$ For aluminum-alloy to silicon contacts, the reported values of activation energy are generally in the range $0.8-0.9 \mathrm{eV}$. For silicided $\left(\mathrm{TiSi}_{2}, \mathrm{TaSi}_{2}\right)$ contacts the values are higher $1.1-1.5 \mathrm{eV}$. Due to the extreme localized nature of the self-heating during contact stressing, the values for $n$ have been reported to be as low as 1 and as high as $11 .{ }^{14}$

# 2 Stress Migration 

Mechanical stress-related failures are very important for IC devices. When a metal is placed under a mechanical stress which exceeds its yield point, the metal will undergo plastic deformation with time. ${ }^{15}$ This time-dependent phenomenon is described by metallurgists as creep. The creep will continue until the stress level is brought below the yield point or until the metal fails. This metal failure mechanism is especially important for ICs where one is confronted with: on-chip aluminum-alloy or copper metallization, gold ball-bonds and wires, iron-alloy or copper lead-frames, solder joints, etc.

Stress migration in ICs is the term used to describe the flow of metal atoms under the influence of mechanical stress. Generally, this failure mechanism is driven by creep (under a fixed-strain condition) and, as such, it is a stress-relief mechanism for the metallization on the chip. ${ }^{16}$ This stress-relief mechanism (resulting in void formation in the IC metallization) will generally continue until the mechanical stress in the metallization is relieved below its yield point (as discussed in Chap. 13).

[^0]
[^0]:    ${ }^{13}$ The current $I$, as used here, is a virtual stress (discussed in Chap. 9 (Sec. 4)) because TF depends strongly on the dimensions of the contact. The use of a real stress, such as current density $J(=I /$ Area), would normally be preferred. However, due to current crowding effects in the small contact window, the current density is very non-uniform and difficult to describe. For this reason, the virtual stress current $I$ is used.
    ${ }^{14}$ Joule(or self) heating can be an important issue for contacts. Even though the ambient temperature may be held constant, the actual contact temperature can vary greatly with the current level applied. If the self heating is not properly accounted for, then very high apparent n values are obtained.
    ${ }^{15}$ This is normally referred to as plastic (versus elastic) deformation. Elastic deformations tend to produce no damage to the material while plastic deformations tend to cause some amount of permanent change to the material.
    ${ }^{16}$ Generally, metals will tend to flow in order to relieve the stress in the material. Unfortunately, such mass flow can result in notching/voiding in the metal.

Fig. 12.7 Mechanical stress gradients can cause metal atoms to flow (creep) in an effort to relieve the stress energy. The small grain $C$, with high specific-energy grain boundaries as illustrated in (a), may be absorbed by grains $A$ and $B$ to facilitate the stress relaxation shown in (b). As for Cu , the dominant diffusion paths may be along $\mathrm{Cu} /$ barrier interfaces

Fig. 12.8 Stress migration has served to produce notching/ voiding in the Al-alloy metal lead shown


# 2.1 SM in Aluminum Interconnects 

Actually, mass flow occurs due to stress gradients in the material, not simply due to the applied stress in the material. Usually, the stress gradients are assumed to be proportional to the applied mechanical stress $\sigma$. The source of this stress $\sigma$ can be intrinsic and/or thermomechanical stress.

Relatively little permanent atom movement occurs until the stress $\sigma$ exceeds the yield point of the metallization. The flux of the moving metal atoms is primarily along grain boundaries as illustrated in Fig. 12.7, but may also occur within a grain if the metal lead is very narrow and the grain structure can be considered bamboo-like. ${ }^{17}$

The inevitable flux divergence associated with the metal movement can cause notching and voiding to occur in IC metal leads/stripes (see Fig. 12.8). ${ }^{18}$ The resistance rise associated with the void formation can cause electrical failures. The time-to-failure (TF) due to creep is described by

[^0]
[^0]:    ${ }^{17}$ Grain boundaries which are nearly perpendicular to the metal stripe length.
    ${ }^{18}$ As discussed in Chap. 13, the strain energy reduction/release is greater than the energy increase associated with the creation of new surfaces.$$
\mathrm{TF}=A_{0} \sigma^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
$$

where:
$\sigma$ is the tensile stress in the metal for a constant strain ${ }^{19}$;
$n$ is the stress migration exponent. $n=2-4$ for soft metals such as aluminum and copper, $n=4-6$ for mild steels, and $n=6-9$ for very strong/hardened metals; and $Q$ is the activation energy. $Q \approx 0.6-0.8 \mathrm{eV}$ for grain-boundary diffusion in aluminum, $Q \approx 1 \mathrm{eV}$ for within-grain (bamboo-like) diffusion in aluminum.

For on-chip metallization, the dominant mechanical stress is generated by thermal expansion mismatch of the metal and the constraining surrounding materials. For this reason, the stress is referred to as thermomechanical stress and $\sigma$ is proportional to the change in temperature, i.e.,

$$
\sigma \propto \Delta T
$$

Therefore, if the metal creep is caused by thermomechanical stress, then the time-to-failure, Eq. (12.4), can be expressed by ${ }^{20}$ :

$$
\mathrm{TF}=A_{0}\left(T_{0}-T\right)^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:
$T_{0}$ is defined as the stress-free temperature for the metal. ${ }^{21}$
The role of stress and stress relaxation is very important in the nucleation and growth of voids in aluminum-alloy interconnects. Cu doping in the aluminum is somewhat effective in suppressing grain-boundary diffusion, but is much less effective if the grain size is large compared to line width. In these bamboo-like leads, one observes slit-like void formation due to intra-grain diffusion.

To test for SM, typically long ( $>1,000 \mu \mathrm{~m}$ ) and narrow stripes ( $<2 \mu \mathrm{~m}$ width) are stored at temperatures in the range $150-200^{\circ} \mathrm{C}$ for $1-2 \mathrm{kh}$ and then electrically tested for resistance increases (or reduction in breakdown currents). ${ }^{22}$ The SM baking temperature should be carefully selected because, as predicted from Eq. (12.6), there is a maximum in the creep rate (as illustrated in Fig. 12.9). This generally

[^0]
[^0]:    ${ }^{19}$ The metallization on a chip is constrained (fixed strain) due to the hard dielectrics surrounding the metallization. The creep, in this case, is a stress-relaxation mechanism under fixed strain which can lead to void formation.
    ${ }^{20}$ This equation is usually referred to as the McPherson and Dunn Model for stress migration in interconnects.
    ${ }^{21}$ The prefactor $\left(T_{0}-T\right)$, in Eq. (12.6), can be expressed in ${ }^{\circ} \mathrm{C}$ or K , since this is a difference of two temperatures. However, the temperature in the exponential term must be expressed in K .
    ${ }^{22}$ The breakdown current is determined by ramping the current to breakdown. If the metal stripe has a notch/void in it, then the breakdown current should be lower.

Fig. 12.9 Stress migration-induced creep/voiding rate has a maximum at a critical temperature (which is generally in the $150-200^{\circ} \mathrm{C}$ range for Al -alloys). This maximum in the creep/voiding rate occurs because of the low mobility (but high stress) at lower temperatures and low stress (but high mobility) at elevated temperatures
occurs in the $150-200^{\circ} \mathrm{C}$ range and serves to drive a minimum in the time-to-failure Eq. (12.6). This maximum in the creep rate occurs (because of competing mechanisms as discussed in Chap. 3) due to the high stress (but low mobility) at lower temperatures, and low stress (but high mobility) at high temperatures. Because the mechanical stress is temperature dependent, a straightforward determination of the diffusion activation energy is somewhat difficult to obtain. Generally, $Q \sim$ $0.5-0.6 \mathrm{eV}$ is used for grain-boundary diffusion and $\sim 1 \mathrm{eV}$ for single-grain/bulkdiffusion.

The use of refractory metal barriers or layered metallization has tended to greatly reduce the impact of the damage caused by slit-like void formation in bamboo leads. This is because the refractory metal layer tends to serve as a redundant conductor, shunting the current and reducing the electrical resistance rise when a SM-induced void forms.

# 2.2 SM in Cu Interconnects 

Stress migration in Cu metallization (see Fig. 12.10) is also a concern, despite an expectation that Cu's generally superior EM capabilities would translate to significantly improved stress migration performance.

Similar to a comparison between Al and Cu EM, as it pertains to its use in advanced IC technology, the contrasting fabrication methods used for Cu vs. Al generate pronounced differences in the type of stress migration issues that are found in the different metallizations. A basic difference between Cu and Al lies with their different melting points: $1,083{ }^{\circ} \mathrm{C}$ vs. $660^{\circ} \mathrm{C}$, respectively. Normal interconnect processing temperatures during integrated circuit fabrication can be as high asFig. 12.10 Stress-induced voiding under a single via in a copper interconnect system. Wide Cu lines are servicing the via

$400^{\circ} \mathrm{C}$, which is a substantial fraction of the melting temperature of Al but to a lesser degree for Cu . Hence, the processing of Al metallization can lead to grains that are large and well-formed within interconnect wiring (so-called bamboo structure for narrow metal leads) - but similar processing temperatures do not greatly alter the microstructure of Cu after it has reached a certain level of stability. Therefore, the grain structure within Cu interconnect wiring is much more varied, both grain sizewise and texture-wise. Electroplated Cu also greatly impacts the evolved microstructure such that narrow lines remain small grained, whereas wider lines develop larger grains.

Like Al stripes, Cu stripes can show evidence of SM-induced voiding; however, because of the presence of a somewhat redundant metal barrier and the lack of sufficient bamboo character to the Cu grains, its general impact on reliability may not be quite as strong. However, when a void forms under or within vias, ${ }^{23}$ as shown in Fig. 12.10 and illustrated in Fig. 12.11, the reliability impact can be substantial, especially when the via is an electrically weak link along the interconnect path. This via-voiding impact is felt most severely when wide leads are placed over and/or under single vias. ${ }^{24}$ As indicated by the voiding illustrated in Fig. 12.11, once a void is nucleated, an ample supply of vacancies can be provided within wide Cu leads to enlarge the void, within the via or under a via, and enable very resistive or opencircuit formation.

[^0]
[^0]:    ${ }^{23}$ On a chip, there can be several levels of metallization, stacked on top of one another with a layer of dielectric in between metal levels. The via is an electrical connection, through the dielectric layer (s), from an upper metal level to a lower metal level.
    ${ }^{24}$ The voiding is a stress-relief mechanism as discussed in Chap. 13. Void growth occurs because of vacancy flow due to stress gradients. More vacancies are available in wide Cu-leads versus narrow ones.

Fig. 12.11 Due to the fact that at least some of the plated Cu annealing during processing is done while the Cu is fully constrained by the barrier layers and dielectric layers, the Cu metallization becomes super-saturated with vacancies along grain boundaries and interfaces. These vacancies can move under presence of stress gradients and generally flow from tensile regions to compressive regions. Voiding under/within via is a stress-relief mechanism


Fig. 12.12 Baking/annealing data is shown for single-via to wide Cu-lead test structures. These stress migration results show that a maximum occurs in voiding rate (creep rate) at a critical temperature in the range between 150 and $200^{\circ} \mathrm{C}$. This critical temperature is independent of the resistance rise failure criteria used

Void growth continues until the local stress is relaxed below its yield point. Baking (or annealing) data is shown in Fig. 12.12 for single vias to wide Cu-lead test structures. The Cu-via baking data, similar to aluminum metallization previouslyFig. 12.13 Fitting of the relative creep-rate data (extracted from Fig. 12.12) produces the kinetic parameters: stress dependence exponent of $n=$ 3.2 , an activation energy of $Q=0.74 \mathrm{eV}$, and a stressfree temperature of $290^{\circ} \mathrm{C}$. The maximum in the creep/ voiding rate occurs at: $T_{\text {crit }}$ $=190^{\circ} \mathrm{C}$

discussed (refer to Fig. 12.9), show that a maximum occurs in via failure rate (creep rate). The critical temperature $\left(150-200{ }^{\circ} \mathrm{C}\right)$ at which the maximum occurs is roughly independent of the resistance rise used to define TF.

The resistance-rise data in Fig. 12.12 is indicative of the voiding/creep rate. Thus, fitting the stress-migration data in Fig. 12.12, using the McPherson and Dunn creep/ voiding rate model, one obtains:

$$
\operatorname{Creep}(\text { Voiding }) \text { Rate }=B_{0}\left(T_{0}-T\right)^{n} \exp \left[-\frac{Q}{K_{B} T}\right]
$$

where: stress exponent $n=3.2$, an activation energy of $Q=0.74 \mathrm{eV}$, and a stress free temperature for the Cu of $T_{0}=270^{\circ} \mathrm{C}$. The maximum in the creep/voiding rate occurs at a temperature close to $T_{\text {crit }}=190^{\circ} \mathrm{C}$. The fitting is shown in Fig. 12.13.

# Example Problem 4 

Show that if the creep rate [Eq. (12.7)] has a maximum in it, then the three kinetic parameters $\left(n, Q, T_{0}\right)$ are not independent and must obey the equation:

$$
Q=n K_{B}\left(\frac{T_{\mathrm{crit}}^{2}}{T_{0}-T_{\mathrm{crit}}}\right)
$$

Also show that the best fitting parameters (shown in Fig. 12.13) do indeed satisfy this equation.

## Solution

One can easily show that if $\mathrm{R}(\mathrm{T})$ has a maximum at $T=T_{\text {crit }}$, then $\ln [\mathrm{R}(\mathrm{T})]$ also has a maximum at $T=T_{\text {crit }}$.# Proof 

For a maximum to exist in $\mathrm{R}(\mathrm{T})$ then it is necessary that:

$$
\left(\frac{\mathrm{d} R}{\mathrm{~d} T}\right)_{T=T_{\text {crit }}}=0
$$

If we investigate $\ln [\mathrm{R}(\mathrm{T})]$, one obtains:

$$
\left(\frac{\mathrm{d} \ln [R(T)]}{\mathrm{d} T}\right)_{T=T_{\text {crit }}}=\left[\frac{1}{R}\left(\frac{\mathrm{~d} R}{\mathrm{~d} T}\right)\right]_{T=T_{\text {crit }}}=\frac{1}{R\left(T_{\text {crit }}\right)}\left(\frac{\mathrm{d} R}{\mathrm{~d} T}\right)_{T=T_{\text {crit }}}=0 . \text { Therefore, if } \mathrm{R}(\mathrm{~T}) \text { has a maximum in the function at } T=T_{\text {crit }}, \text { then } \ln [\mathrm{R}(\mathrm{T})] \text { will also }
$$

have a maximum at $T=T_{\text {crit }}$. Taking the natural logarithm of both sides of the Eq. (12.7), one obtains:

$$
\ln [R]=\ln \left(B_{0}\right)+n \ln \left(T_{0}-T\right)-\frac{Q}{K T}
$$

Taking the derivative, and evaluating at $T=T_{\text {crit }}$, one obtains:

$$
\left(\frac{\mathrm{d} \ln [R(T)]}{\mathrm{d} T}\right)_{T=T_{\text {crit }}}=0=-\frac{n}{T_{0}-T_{\text {crit }}}+\frac{Q}{K_{B} T_{\text {crit }}^{2}}
$$

giving

$$
Q=n K_{B}\left(\frac{T_{\text {crit }}^{2}}{T_{0}-T_{\text {crit }}}\right)
$$

Finally, we check to see if the best fitting parameters, shown in Fig. 12.13, actually satisfy this equation:

$$
\begin{aligned}
Q= & n K_{B}\left(\frac{T_{\text {crit }}^{2}}{T_{0}-T_{\text {crit }}}\right)=3.2\left(8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}\right) \times \\
& \left(\frac{[(190+273) \mathrm{K}]^{2}}{(270+273) \mathrm{K}-(190+273) \mathrm{K}}\right)=0.74 \mathrm{eV}
\end{aligned}
$$

This activation energy agrees well with the best fitting activation energy $Q=0.74 \mathrm{eV}$ shown in Fig. 12.13.Fig. 12.14 (a) Corrosion of aluminum bonding pads can occur if chlorides and moisture are present. Grounded $\left(V_{\mathrm{sa}}\right)$ pads are especially sensitive to corrosion. (b) Exposed Cu stripes can corrode during processing in the time window between post-CMP Cu-clean and cap-layer dielectric deposition. The volume of the corrosion product, usually $\mathrm{Cu}(\mathrm{OH})_{2}$, can be much larger than the volume of Cu consumed


# 3 Corrosion 

Corrosion failures can occur when ICs are exposed to moisture and contaminants. IC corrosion failures are usually classified as one of two broad groups: bonding-pad corrosion or internal-chip corrosion. The bonding pad is a rather large piece of on-chip metallization on the order of $50 \times 50 \mu \mathrm{~m}$. These bonding pads, historically, have provided the metallization contact surface for eventual Au or Cu -wire ball bonding (refer to Figs. 12.14, 12.20 and 12.21). This wire bonding permits electrical connection of the chip to the outside world. Bonding-pad corrosion can occur during die processing and/or post assembly. ${ }^{25}$ Bonding pads that are connected/grounded to the silicon substrate (see Fig. 12.14a) are especially sensitive to corrosion. Bondingpad corrosion is usually more common (than internal-chip corrosion) simply because the die-level passivation (often either silicon nitride or oxynitride) does not cover the bonding-pad metallization. Furthermore, any residual chlorides from aluminum and/or protective overcoat etching, plus moisture, can cause Al corrosion. ${ }^{26}$

[^0]
[^0]:    ${ }^{25}$ Assembly describes the process used to encapsulate a silicon chip into plastic packaging with electrical connections to the outside world. This process includes: silicon chips are first separated from the wafer (usually by sawing), chips are then attached to a lead frame, the lead frame is then molded in plastic, and finally the leads are trimmed and formed.
    ${ }^{26}$ If Al corrosion occurs in a liquid state, the corrosion may have the appearance of simply missing aluminum. If Al corrosion occurs in humidity/moisture, the corrosion product (usually aluminum hydroxide) can be expansive in size and will appear to be black, under an optical microscope, due to its very rough/cracked texture. The volume of the corrosion product, usually $\mathrm{Al}(\mathrm{OH})_{3}$, can be much larger than the volume of Al consumed.Fig. 12.15 Wet corrosion generally occurs with low activation energy because of the very high mobility of the diffusing ions in water. The ions must be able to diffuse away from the anode/ cathode region for the corrosion cell to continue to work. In water, this diffusion process is relatively easy


Internal corrosion (internal to the chip, away from the bonding pads) can also occur if some weakness or damage exists in the die passivation layer which could permit moisture and contaminants (e.g., chlorides) to reach the exposed metallization. The internal corrosion can cause electrical discontinuities at localized regions of die.

Corrosion can be generally described in terms of a corrosion cell. ${ }^{27}$ The corrosion cell must have four key components in order for corrosion to occur: an anode (a region for the oxidation reaction to occur), a cathode (a region for the reduction reaction to occur), an electrolyte (through which the ions can diffuse), and a conductor to provide a pathway for the electron flow from the oxidation region to the reduction region. An example of wet corrosion is shown in Fig. 12.15. Metal corrosion (oxidation) can occur if there is an imperfection in the native oxide covering the metallization.

Generally, Al forms a good self-passivating oxide and it is much less corrosive than Cu , even though the Galvanic Series ${ }^{28}$ would suggest just the opposite. However, if chlorides and moisture are present, then the $\mathrm{Al}_{2} \mathrm{O}_{3}$ native oxide protecting the Al can be quickly reduced. Once the native oxide is reduced, exposing a highly reactive virgin metal surface, the corrosion can proceed rapidly.

In order for the corrosion to continue at a rapid rate, the ions must be able to diffuse rapidly to and from the regions of oxidation/reduction. ${ }^{29}$ This can occur most easily in liquids because the activation energy for diffusion in a liquid is generally very low $\sim 0.3 \mathrm{eV}$. However, for dry or ambient corrosion (see Fig. 12.16), the activation energy for diffusion is generally higher and the corrosion rate is very dependent on the percentage relative humidity $(\% \mathrm{RH})$. In fact, the surface mobility on oxide has been found to be exponentially dependent on $\% \mathrm{RH}$ over a rather wide range of $\% \mathrm{RH}$. With the surface mobility limited by the $\% \mathrm{RH}$, as illustrated in

[^0]
[^0]:    ${ }^{27}$ The corrosion cell is discussed in more detail in Chap. 13.
    ${ }^{28}$ The Galvanic Series is discussed in Chap. 13.
    ${ }^{29}$ If the ions cannot diffuse away from the region of oxidation/reduction, then a rise in electrical potential will retard the corrosion potential.

Fig. 12.16 Ambient corrosion has a very strong humidity dependence and an expansive corrosion product $\mathrm{M}(\mathrm{OH})_{\mathrm{n}}$ can develop. The percentage relative humidity $(\% \mathrm{RH})$ has a great impact on surface/interface mobility. The ions have to be able to diffuse from the anode/cathode regions for the corrosion cell to work. Otherwise, the buildup of localized ions will create an electrical potential that will tend to offset the chemical corrosion potential


Fig. 12.17 Generally, immediately after chemical-mechanical polishing (CMP) of the plated Cu on a wafer, the exposed Cu is susceptible to oxidation. The oxidation of the Cu (in other parts of the circuit not shown) serves to free Cu -ions which can then diffuse across the dielectric surface. (a) If a grounded node (such as the Cu -via to an N -well connection shown above) can be found, then a reduction/re-plating of the Cu -ions can occur resulting in the unwanted Cu -nodules, as are shown in early stages in (a). The later stages are shown in (b)

Fig. 12.16, then the time-to-failure is expected to be limited by the humidity. Also, an expansive corrosion product $\mathrm{M}(\mathrm{OH})_{\mathrm{n}}$ can develop.

During IC wafer processing, Cu -ions (which are produced during oxidation at some location in the circuit) can diffuse away from this region of oxidation and then may plate out again at other locations in the circuit. In Fig. 12.17, we show a Cu-via (Cu-via contacted to a W-plug) to n-well. Since this is, in effect, a grounded Cu-via, any free Cu -ions on the surface of the dielectric can diffuse and plate out by reduction at these grounded locations: $\mathrm{Cu}^{2+}+2 \mathrm{e} \rightarrow \mathrm{Cu}$. One can see in Fig. 12.17a the Cu -plated nodules at the perimeter of the grounded Cu -via and how this region will continue to grow with time as shown in Fig. 12.17b. This is quite interesting. It should be emphasized that the Cu , which was originally electrochemically plated and chemically-mechanically polished, is now being replated by a secondary oxidation and reduction reaction.

Fig. 12.18 Corrosion activity is shown as a function of applied voltage. The corrosion activity of the Cu is much higher than Al . The corrosion activity of the Cu can be reduced by adding thin protective layers such as BTA during processing

The relative corrosion activities for Copper and Aluminum are shown in Fig. 12.18 as a function of applied voltage. The strong native oxide $\left(\mathrm{Al}_{2} \mathrm{O}_{3}\right)$ on aluminum serves as a self-passivation layer and the corrosion activity for Al is relatively low and is nearly independent of the applied voltage (from 0 to 0.8 V ). However, the native oxide $\left(\mathrm{Cu}_{\mathrm{x}} \mathrm{O}_{\mathrm{x}}\right)$ on copper is of relatively poor quality and does not protect the exposed copper-and a higher corrosion activity ${ }^{30}$ is observed. In order to reduce the corrosion activity of the exposed Cu , corrosion inhibitors are generally used. BTA (benzotriazole: $\mathrm{C}_{6} \mathrm{H}_{5} \mathrm{~N}_{3}$ ) is a commonly used corrosion inhibitor which is added during CMP of the Cu to reduce post-CMP corrosion. The BTA serves to reduce the corrosion activity of the Cu to manageable levels during processing. However, even with the use of corrosion inhibitors, it is good practice to establish a tight processing time window between CMP processing of the Cu and dielectric barrier deposition in order to minimize corrosion.

To monitor the corrosion susceptibility of packaged chips, the industry generally uses one or more of three standard corrosion tests. These three tests have been widely used to accelerate potential IC corrosion failure mechanisms: biased $85^{\circ} \mathrm{C}$ and $85 \%$ RH, autoclave ( $121^{\circ} \mathrm{C}$ and $100 \% \mathrm{RH}$ ), and highly accelerated stress test (HAST) conditions (typically biased, $130^{\circ} \mathrm{C}$ and $85 \% \mathrm{RH}$ ). To extrapolate packaged-chips corrosion results, under highly accelerated conditions to use conditions, at least three models have been used.

[^0]
[^0]:    ${ }^{30}$ Corrosion activity was measured by monitoring the resistance rise vs. time, for a metal stripe when the test structure was stored in an ammonium-chloride solution.# 3.1 Exponential Reciprocal-Humidity Model 

The time-to-failure equation for IC failure due to corrosion is

$$
\mathrm{TF}=A_{0} \exp \left(\frac{b}{\mathrm{RH}}\right) \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:
$A_{0}$ is a process/material-dependent parameter and serves to produce a distribution of times-to-failure (Weibull or lognormal distributions),
$b$ is the reciprocal humidity dependence parameter (approximately equal to $\sim 300 \%$ ),
RH is the relative humidity expressed as a $\%,{ }^{31}$ and $Q$ is the activation energy (approximately equal to 0.3 eV for phosphoric acid-induced corrosion of aluminum and generally consistent with wet corrosion. ${ }^{32}$

This model was developed when phosphosilicate glass (PSG) was used for interconnect dielectric and/or passivation. ${ }^{33}$ Too much phosphorus ( $>8 \%$ ) in the glass and the phosphorus would precipitate onto the glass surface and along its interfaces. With the addition of moisture, this would cause phosphoric acid to form which would attack the metallization.

### 3.2 Power-Law Humidity Model

The time-to-failure equation for IC failure due to corrosion is

$$
\mathrm{TF}=A_{0}(\mathrm{RH})^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:
$n$ is the power-law exponent and equal to 2.7 ,
$R H \%$ relative humidity, and
$Q$ is the activation energy and equal to $0.7-0.8 \mathrm{eV}$ for chloride-induced corrosion of aluminum.

[^0]
[^0]:    ${ }^{31} 100 \%$ relative humidity represents saturated water vapor.
    ${ }^{32}$ This low value of activation energy $(0.3 \mathrm{eV})$ is typical for wet corrosion mechanisms where the mobility of the diffusing ions is good. Due to a very high concentration of phosphorus in the PSG, liquid droplets of phosphoric acid can develop under humid conditions.
    ${ }^{33}$ The phosphorus in the glass is very useful in gettering unwanted sodium ions. The Na ions, if present, can induce a surface-inversion failure mechanism. The surface-inversion failure mechanism is discussed in Sect. 6.This model was developed for chloride-induced corrosion in plastic-packaged chips. Chlorine-based dry etches are generally used for the aluminum-alloy metallizations. If excessive amounts of chlorides are left on the die after post-etch cleanups, corrosion can occur with the addition of moisture.

# 3.3 Exponential Humidity Model 

The time-to-failure equation for integrated circuit failure due to corrosion is

$$
\mathrm{TF}=A_{0} \exp (-a \cdot \mathrm{RH}) \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:
$a$ is the humidity acceleration parameter and is equal to $0.10-0.15(\% \mathrm{RH})^{-1}, \mathrm{RH}$ is the $\%$ relative humidity, and
$Q$ is the activation energy and is equal to $0.7-0.8 \mathrm{eV}$ for chloride-induced corrosion of aluminum in plastic packages.

This corrosion model was developed when it was shown that, over a wide range of humidity ( $20-80 \%$ ), the surface conductivity is exponentially dependent on the humidity, as shown in Fig. 12.19.

There seems to be reasonably good consensus that the proper activation energy for chloride-induced aluminum corrosion is in the $0.7-0.8 \mathrm{eV}$ range. There is not a consensus for the humidity dependence. A comparison of the three models for the same data set tended to show some preference for the exponential model with a $\sim 0.10-0.15(\% \mathrm{RH})^{-1}$. However, the power-law model is a widely used corrosion model in the IC industry for plastic-package chips.


Fig. 12.19 The surface conductivity for $\mathrm{SiO}_{2}$ over a wide range of humidity was observed to be exponentially dependent on the $\%$ relative humidity. An exponential acceleration parameter of $a=$ $0.12(\% \mathrm{RH})^{-1}$ was observed# Example Problem 5 

For an ambient relative humidity of $40 \%$ in a wafer fab, it was established that the longest corrosion-free time (time window) that a Cu metallization could be exposed to the ambient conditions was 4 h . If the humidity due to a clogged filter increases the relative humidity from 40 to $50 \% \mathrm{RH}$, what would the new time window be?

## Solution

$$
\mathrm{AF}=\frac{(\mathrm{TF})_{40 \% \mathrm{RH}}}{(\mathrm{TF})_{50 \% \mathrm{RH}}}=\exp [a \cdot(50 \% \mathrm{RH}-40 \% \mathrm{RH})]
$$

Assuming that $a=0.12(\% \mathrm{RH})^{-1}$, then

$$
\begin{gathered}
\mathrm{AF}=\exp \left[0.12(\% \mathrm{RH})^{-1}(50 \% \mathrm{RH}-40 \% \mathrm{RH})\right] \\
=3.32
\end{gathered}
$$

Therefore, the time window becomes:

$$
(\mathrm{TF})_{50 \% \mathrm{RH}}=\frac{(\mathrm{TF})_{40 \% \mathrm{RH}}}{\mathrm{AF}}=\frac{4 \mathrm{~h}}{3.32}=1.2 \mathrm{~h}
$$

In summary, by the humidity going from 40 to $50 \% \mathrm{RH}$, the safe (corrosion free) processing time window for the metallization is reduced from 4 to 1.2 h .

## 4 Thermal-Cycling/Fatigue Issues

Each time the assembled Si-chips are powered up and down, the assembled chips undergo a thermal cycle. Thermal cycling can induce important fatigue ${ }^{34}$ failure mechanism for fully assembled chips. As shown in Fig. 12.20, the thermal expansion mismatch of the diverse materials used on the chip and during assembly can result in significant thermomechanical stresses. These thermomechanical stresses, and the cyclical nature of the power up and power down of the devices, can generate fatigue failures. For example, the lifted bonding ball shown in Fig. 12.21 resulted from thermomechanical stress during temperature cycling. The thermomechanical stress (generated by the thermal expansion coefficient mismatch of the: plastic molding compound, gold bonding ball, $\mathrm{Au}-\mathrm{Al}$ intermetallics, Al pad, and silicon chip) served to weaken the bond during thermal cycling and eventually led to failure of the ballbond attachment.

[^0]
[^0]:    ${ }^{34}$ Fatigue failure can result from cyclical stresses as discussed in Chap. 13.Fig. 12.20 Shown is a multiple-die stack with the on-die bonding pads, ballbonds to these pads and the ball wires. The individual die/chips are separated by adhesives. This ensemble of stacked-die will be eventually encapsulated in plastic for handling. Thus, the thermal expansion mismatch of dissimilar materials is ever-present during temperature cycling of the assembled die


Fig. 12.21 Au ball-bond, originally bonded to an aluminum bonding pad on the die, has become detached during temperature cycling. The facture under the ball-bond is clearly evident in the micrograph


Thermal cycling of a device will naturally occur each time the assembled chips undergo a normal power-up and power-down cycle. Such thermal cycles can induce a cyclical thermomechanical stress that tends to degrade the materials, and may cause a host of potential failure modes: dielectric/thin-film cracking, lifted ballbonds, fractured/broken bond wires, solder fatigue, cracked die, etc.

The thermomechanical stresses during thermal cycling can be very large due to the large thermal expansion mismatch that exists between the silicon, on-chip dielectrics and metallization, lead frame, and the plastic molding compound used for chip encapsulation. Thus, to accelerate thermal-cycling failure mechanisms, the assembled chip(s) may be accelerated by using temperature cycling ranges outside the normal range of operation and then recording the number of cycles-to-failure. Some commonly used accelerated temperature cycling ranges for ICs include: -65 ${ }^{\circ} \mathrm{C} / 150^{\circ} \mathrm{C},-40^{\circ} \mathrm{C} / 140^{\circ} \mathrm{C}$, and $0^{\circ} \mathrm{C} / 125^{\circ} \mathrm{C}$.

Fig. 12.22 Thermomechanical stresses during temperature cycling can cause plastic deformation and fatigue damage to on-chip metallization and their interfaces. Temperature cycling can also accelerate crack propagation in more brittle dielectric materials. The aluminum (in top layer metal) has shifted from left to right during temperature cycling. The accumulation of Al became so great that the surrounding dielectric cracked, thus permitting an Al extrusion to occur

As for modeling, one can assume that each thermal cycle generates plastic deformation which serves to damage the materials, as illustrated in Fig. 12.22. For ductile materials, low-cycle fatigue data is described rather well by the CoffinManson model ${ }^{35}$ :

$$
\mathrm{CTF}=A_{0}\left(\Delta \varepsilon_{p}\right)^{-s}
$$

where:
$C T F$ is the number of cycles-to-failure,
$\Delta \varepsilon_{p}$ is the plastic strain range, ${ }^{36}$ and
$s$ is an empirically determined exponent.
Low-cycle fatigue usually refers to stress conditions that only require a few hundred (or few thousand) cycles to produce failure. High-cycle fatigue usually refers to stress conditions which may require hundreds of thousands of cycles to produce failure.

During a temperature cycle, not all of the entire temperature range $\Delta T$ may be inducing plastic deformation. If a portion of this range $\Delta T_{0}$ is actually in the elastic range, then this should be subtracted and one can write a modified Coffin-Manson equation as:

[^0]
[^0]:    ${ }^{35}$ Coffin-Manson model is discussed in more detail in Chap. 13.
    ${ }^{36}$ The plastic strain range is outside the normal elastic region. Damage is occurring to the material in the plastic range.

Fig. 12.23 Thermomechanical stress, during temperature cycling, can cause crack propagation (fatigue damage) for brittle materials and their interfaces

$$
\Delta \varepsilon_{p} \propto\left(\Delta T-\Delta T_{0}\right)^{\beta}
$$

Thus, for temperature cycling, the Coffin-Manson equation becomes:

$$
\mathrm{CTF}=A_{0}\left(\Delta T-\Delta T_{0}\right)^{-q}
$$

where $q$ is an empirically determined exponent. This equation is commonly referred to as the Dunn and McPherson equation. If the elastic range $\left(\Delta T_{0}\right)$ is much smaller than the entire temperature cycle range $(\Delta T)$, then it may be dropped without significant error being introduced. However, one should always question the assumption as to whether $\left(\Delta T_{0}\right)$ is an insignificant part of total thermomechanical stress range $(\Delta T)$.

As illustrated in Fig. 12.23, fatigue can also occur in brittle materials due to crack propagation. Normally, there are three distinct phases to brittle material failure: a crack initiation phase (which usually exists at time zero), a crack growth phase (which tends to dominate the number of cycles-to-failure), and a catastrophic failure phase which is typically of relatively short duration. ${ }^{37}$ Since the crack growth phase is of greatest duration (dominates the number of cycles-to-failure), the modeling effort is usually focussed on this phase. Experimentally, one finds that the crack growth rate (increase in crack length per cycle) is dependent on the length of the existing crack and on the applied cyclical stress so, one can write:

$$
\frac{\mathrm{d} L}{\mathrm{~d} N}=C\left(\sigma_{a}\right)^{m} L^{n}
$$

where $L$ is the crack length, $N$ is the number of cycles, $\sigma_{a}$ is the applied cyclical stress, $m$ and $n$ are empirically determined exponents. Separating the variables and integrating gives:

$$
\mathrm{CTF}=\left[\frac{1}{C}\right]\left[\int_{L_{0}}^{L_{f}} \frac{\mathrm{~d} L}{L^{n}}\right]\left(\sigma_{a}\right)^{-m}=B_{0}\left(\sigma_{a}\right)^{-m}
$$

[^0]
[^0]:    ${ }^{37}$ Additional information on crack propagation can be found in Chap. 13.Table 12.1 Temperaturecycling exponents

| Material | Temp-cycle exponent |
| :-- | :-- |
| Soft metals (Solder, Aluminum, etc.) | $q=1-3$ |
| Hard metals/Intermetallics | $q=3-6$ |
| Brittle materials (Dielectrics) | $q=6-9$ |

In the previous equation, it is clear that $B_{0}$ is a function of crack size (the initial crack size $L_{0}$ and how large a crack is needed to produce failure $L_{f}$ ). Since $B_{0}$ will vary from device-to-device, $B_{0}$ causes CTF to actually become a cycles-to-failure distribution with either the lognormal or Weibull distribution preferred to describe the statistical data.

Since the cyclical stress is assumed to be thermomechanical, $\sigma_{\mathrm{a}}$ is proportional to $\Delta \mathrm{T}$, then cycles-to-failure becomes:

$$
\mathrm{CTF}=\mathrm{A}_{0}(\Delta T)^{-q}
$$

which is very similar to Eq. (12.13) for ductile materials. Thus, while the CoffinManson model was originally developed for ductile materials (metals), it has also been successfully applied to brittle materials with the appropriate selection of exponents as summarized in Table 12.1.

In summary, temperature cycling failures for integrated circuits can be described reasonably well by the modified Coffin-Manson equation. The equation works rather well even for brittle materials, where failure is dominated by crack growth rather than simple plastic deformation (which was assumed in the development of the original Coffin-Manson equation).

# Example Problem 6 

During a temperature cycling stress test of packaged die/chips, it was determined that the units were able to pass 500 cycles of temperature cycling from -65 to $150^{\circ} \mathrm{C}$ but started to fail at 600 cycles. Failure analysis indicated that the failure mechanism was lifted ball-bonds due to fractured intermetallics (intermetallic region between the Au-ball and the Aluminum bonding pad). Assuming that the full thermomechanical stress range of -65 to $150^{\circ} \mathrm{C}$ is in the plastic-deformation region for the intermetallic, and a cycling exponent of $n=4$, estimate how long the parts should survive for use conditions of 0 to $85^{\circ} \mathrm{C}$.

## Solution

Assuming that the entire thermomechanical stress range is in the plasticdeformation region for the intermetallic layer and that the temperature cycling exponent is $q=4$ for intermetallics, then the acceleration factor becomes:

$$
\begin{aligned}
\mathrm{AF} & =\frac{(\mathrm{CTF})_{0 \text { to } 85^{\circ} \mathrm{C}}}{(\mathrm{CTF})_{-65 \text { to } 150^{\circ} \mathrm{C}}}=\left[\frac{(\Delta T)_{-65 \text { to } 150^{\circ} \mathrm{C}}}{(\Delta T)_{0 \text { to } 85^{\circ} \mathrm{C}}}\right]^{4}=\left[\frac{150^{\circ} \mathrm{C}-\left(-65^{\circ} \mathrm{C}\right)}{85^{\circ} \mathrm{C}-0^{\circ} \mathrm{C}}\right]^{4} \\
& =40.9
\end{aligned}
$$Therefore, the cycles-to-failure CTF, for 0 to $85^{\circ} \mathrm{C}$, becomes:
$(\mathrm{CTF})_{0 \text { to } 85^{\circ} \mathrm{C}}=\mathrm{AF} .(\mathrm{CTF})_{-65 \text { to } 150^{\circ} \mathrm{C}}=(40.9) \cdot(500 \mathrm{cyc})=20,450 \mathrm{cyc}$
Assuming that the device is temperature cycled from 0 to $85^{\circ} \mathrm{C}$, on average 4 times a day, then the time-to-failure TF becomes:

$$
\mathrm{TF}=\frac{20,450 \mathrm{cyc}}{4 \mathrm{cyc} / \text { day }} \cdot\left(\frac{24 \mathrm{~h}}{1 \text { day }}\right)\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right)=14 \text { years }
$$

# 5 Time-Dependent Dielectric Breakdown 

Due to the very high operating electric fields in the gate dielectric of MOSFET devices, time-dependent dielectric breakdown (TDDB) can be an important IC failure mechanism. Usually after a relatively long period of degradation (bondbreakage/trap-creation) as illustrated in Fig. 12.24a, the dielectric eventually undergoes breakdown (a catastrophic thermal runaway condition due to severe


Fig. 12.24 (a) Dielectric degradation occurs due to broken bonds/trap-creation in the dielectric material and at the $\mathrm{SiO}_{2} / \mathrm{Si}$ interface. (b) The trapping of the holes initially and then followed by electron trapping continues up to the point of catastrophic breakdown whereby the localized Joule heating produces a melt-filament shorting the poly-gate and silicon substrate. In very thin dielectrics $(<10 \mathrm{~nm})$, the pre-breakdown leakage may show a stress-induced leakage current increase prior to breakdown of the dielectric. Also, hyper-thin dielectrics ( $<4 \mathrm{~nm}$ ) can show soft breakdown characteristicscurrent flow). This localized current density and associated severe Joule heating can result in a conductive filament forming in the dielectric shorting the poly ${ }^{38}$ gate to the substrate (thus shorting anode and cathode) in the MOSFET device (see Fig. 12.24b). Historically, there are two TDDB models which have been widely used to describe the time-dependent dielectric breakdown failure mechanism in oxides. One model is field-driven (E-Model) while the other is current-driven (1/E—Model).

# 5.1 Exponential E-Model 

In the thermochemical E-Model, ${ }^{39}$ the cause of low-field ( $<10 \mathrm{MV} / \mathrm{cm}$ ) and hightemperature TDDB is due to field-enhanced thermal bond-breakage. In this model, the field serves to stretch polar molecular bonds thus making them weaker and more susceptible to breakage by standard Boltzmann (thermal) processes. Since the field reduces the activation energy required to break a bond, then the degradation rate is expected to increase exponentially with field.

Time-to-failure occurs when a localized density of broken bonds (or percolation sites) becomes sufficiently high to cause a conductive path to form from anode to cathode.

The time-to-failure equation, which is the inverse of degradation rate, decreases exponentially with field,

$$
\mathrm{TF}=A_{0} \exp \left(-\gamma E_{\mathrm{ox}}\right) \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:
$\gamma$ is the field acceleration parameter,
$E_{\text {ox }}$ is the electric field in the oxide and is given by the voltage dropped $V_{\text {ox }}{ }^{40}$ across the dielectric divided by the oxide thickness $t_{\mathrm{ox}}$,
$Q$ is the activation energy (enthalpy of activation), and
$A_{0}$ is a process/material-dependent coefficient that varies from device-to-device and causes TF to actually become a times-to-failure distribution, usually a Weibull distribution.

[^0]
[^0]:    ${ }^{38}$ Poly is short for polycrystalline silicon. Doped-poly has been a common electrode material for MOSFETs for many years. Advanced ICs may use metal gate electrodes.
    ${ }^{39}$ The E-Model was originally introduced as an empirical model and was later given a theoretical thermochemical foundation by McPherson.
    ${ }^{40}$ For MOS-type capacitors on silicon, when stressing in accumulation: $V_{\text {ox }} \cong V_{\text {applied }}-1 \mathrm{~V}$. Whereas, when stressing in inversion: $V_{\text {ox }} \cong V_{\text {applied }}$.Many investigations have shown that $\gamma$ is temperature dependent and that it can be described rather well by a simple $1 / T$ dependence:

$$
\gamma(T)=-\left[\frac{\partial \ln (\mathrm{TF})}{\partial E}\right]_{T}=\frac{p_{\mathrm{eff}}}{K_{B} T}
$$

The effective dipole moment $p_{\text {eff }}$ is related to the amount of polar bonding in the molecule and is given by:

$$
p_{\mathrm{eff}}(m, n)=\left(z^{*} e\right) r_{0} \eta(m, n)^{-1}\left(\frac{2+k}{3}\right)
$$

where: $z^{*}$ is the effective charge transferred from the silicon-ion to its four oxygenion bonding neighbors $\left[z^{*}=4(0.6)=2.4\right], r_{\mathrm{o}}$ is the equilibrium bonding distance ( $r_{0}$ $=1.7 \AA$ ), $\eta$ is related purely to the bonding parameters in the Mie-Gruneisen bonding potential $\left[\eta(9,1)^{-1}=1.67\right],{ }^{41}$ and the dielectric constant for $\mathrm{SiO}_{2}$ is 3.9 [giving $(2+k) / 3=1.97]$. Thus, for the $(9,1)$ bonding potential one obtains a value of $p_{\text {eff }}=13.4 \mathrm{e} \AA$. If the bonding is less ionic and more covalent, then $\eta(9,2)^{-1}=0.93$ and produces a $p_{\text {eff }}=7.5 \mathrm{e} \AA$.
$p_{\text {eff }}$ is generally found to be from TDDB data in the range of $7-14 \mathrm{e} \AA^{42}$ for $\mathrm{SiO}_{2}$, but can be much larger for higher dielectric constant $k$ materials (as indicated by Eq. (12.19). The $1 / T$ dependence for $\gamma$, as given by Eq. (12.18), serves to drive an observed/effective activation energy that is field dependent. Using Eqs. 5.15, 12.17 and 12.18 , one obtains an effective activation energy which reduces linearly with the electric field,

$$
Q_{\mathrm{eff}}=Q-p_{\mathrm{eff}} E_{\mathrm{ox}}
$$

where:
$Q_{\text {eff }}$ is the effective activation energy $(\mathrm{eV})$ and $Q$ is the activation energy for $\mathrm{Si}-\mathrm{O}$ bond breakage in absence of external electric field.

The observed value of $\gamma$ may not necessarily be temperature dependent if several types of disturbed bonding states are present and participating in the dielectric degradation process under high-field and/or high-temperature TDDB testing. Generally, however, for silica-based dielectrics with thicknesses $>40 \AA$ and tested at $105^{\circ} \mathrm{C}$, one generally finds that $\gamma \sim 4.0 \mathrm{~cm} / \mathrm{MV}$ and $Q \sim 1.8 \mathrm{eV}$ are observed during TDDB testing. Thus, if TDDB testing is done at $10 \mathrm{MV} / \mathrm{cm}$ or greater, then according to Eq. (12.20) the expected activation energy is: $Q_{\text {eff }} \leq 1.8 \mathrm{eV}-$ $(13 \mathrm{e} \AA)(10 \mathrm{MV} / \mathrm{cm})=0.5 \mathrm{eV}$. Thus, when TDDB testing is done at fields above

[^0]
[^0]:    ${ }^{41}$ The values for $\eta(m, n)$ can be found in Chap. 13.
    ${ }^{42}$ This range is consistent with effective dipole moments: $p_{\text {eff }}(9,2)$ to $p_{\text {eff }}(9,1)$.$10 \mathrm{MV} / \mathrm{cm}$, the observed activation energy will generally be $\leq 0.5 \mathrm{eV}$. When TDDB testing is done at fields lower than $10 \mathrm{MV} / \mathrm{cm}$, the observed activation energy is generally greater $\geq 0.5 \mathrm{eV}$.

# 5.2 Exponential 1/E-Model 

In the $1 / E$-Model for TDDB (even at low fields) damage is assumed to be due to current flow through the dielectric due to Fowler-Nordheim ( $\mathrm{F}-\mathrm{N}$ ) conduction. Electrons, which are $\mathrm{F}-\mathrm{N}$ injected from the cathode into the conduction band of $\mathrm{SiO}_{2}$, are accelerated toward the anode. As the electrons are accelerated through the dielectric, because of impact ionization, some damage to the dielectric might be expected. Also, when these accelerated electrons finally reach the anode, hot holes can be produced which may tunnel back into the dielectric causing damage (hot-hole anode-injection model). Since both the electrons (from the cathode) and the hot holes (from the anode) are the result of $\mathrm{F}-\mathrm{N}$ conduction, then the time-to-failure is expected to show an exponential dependence on the reciprocal of the electric field, $1 / E$,

$$
\mathrm{TF}=\tau_{0}(T) \exp \left[\frac{G(T)}{E_{\mathrm{ox}}}\right]
$$

where:
$\tau_{0}(T)$ a temperature-dependent prefactor, and $G(T)$ is a temperature-dependent field acceleration parameter for the $1 / E$-Model.

The temperature dependence of $G$ has been expressed as a $1 / T$ power-series expansion given by,

$$
G=\left[\frac{\partial \ln (\mathrm{TF})}{\partial(1 / E)}\right]_{T}=G_{0}\left[1+\left(\frac{\delta}{K_{B}}\right)\left(\frac{1}{T}-\frac{1}{300 \mathrm{~K}}\right)\right]
$$

where:

$$
\delta=\left(\frac{K_{B}}{G_{0}}\right)\left[\frac{\mathrm{d} G}{\mathrm{~d}(1 / T)}\right]_{300 \mathrm{~K}}
$$

and where the derivative is evaluated at 300 K . At room temperature, $G_{0} \sim$ $350 \mathrm{MV} / \mathrm{cm}$ and $\delta \sim 0.017 \mathrm{eV} . \tau_{0}(T)$ is usually also represented as $1 / T$ expansion,

$$
\tau_{0}(T)=\tau_{0} \exp \left[\left(\frac{-Q}{K_{B}}\right)\left(\frac{1}{T}-\frac{1}{300 \mathrm{~K}}\right)\right]
$$

where: $\tau_{0} \sim 1 \times 10^{-11} \mathrm{~s}$ and $Q \sim 0.3 \mathrm{eV}$.# 5.3 Power-Law Voltage V-Model 

For $\mathrm{SiO}_{2}$ dielectrics which are hyper-thin ( $<40 \AA$ ), a power-law voltage model has been proposed for TDDB of the form:

$$
\mathrm{TF}=B_{0}(T)[V]^{-n}
$$

As we have discussed before, normally one prefers to use a real stress such as electric field $E$ (where time-to-failure TF, for a fixed field $E$, is approximately independent of the thickness of the dielectric). But, $V$ as used here is a virtual stress (since time-to-failure TF at a fixed voltage $V$ depends strongly on dielectric thickness). However, the argument has been made that for ballistic transport (no scattering or energy loss in these hyper-thin dielectric films) the amount of energy which is actually delivered to the anode is simply (e) $\times(\mathrm{V})$. For hyper-thin oxide films, the observed exponent is generally in the range: $n=40-48$. However, the value of $n$ is observed to be thickness dependent and can be much lower for thick oxides.

### 5.4 Exponential $\sqrt{E}$-Model

Current-induced dielectric degradation and TF models assume that the degradation is due to current flow through the dielectric. For high quality $\mathrm{SiO}_{2}$, the dominant current flow is nearly always Fowler-Nordheim conduction and thus the damage is assumed to follow a 1/E-Model. However, for other dielectrics, or even poor quality $\mathrm{SiO}_{2}$ dielectrics (such as low-k interconnect dielectrics), the conduction mechanism may be Poole-Frenkel or Schottky conduction. Thus, based on current-induced degradation, one might expect a TF model of the form,

$$
\mathrm{TF}=C_{0}(T) \exp [-\alpha \sqrt{E}]
$$

where the root-field acceleration parameter $\alpha$ is given by:

$$
\alpha=-\left[\frac{\partial \ln (\mathrm{TF})}{\partial \sqrt{E}}\right]_{T}
$$

### 5.5 Which TDDB Model to Use?

Since the physics of each of the TDDB models seems to be quite different, then it is only natural to ask the question-which model should one use? That is probably too difficult of a question to try to answer in this text, because there seems to be no

Fig. 12.25 Shown are the four models best fittings to the same set of accelerated TDDB data. All the models tend to give a very good fitting to the four accelerated TDDB data points. However, their extrapolated results to lower electric fields are quite different. The E-Model gives the shortest time-to-failure when the results are extrapolated to lower electric fields. The 1/E-Model gives the longest time-to-failure at lower electric fields. One could describe the E-Model as being the most conservative and the $1 / \mathrm{E}$-Model as being the most optimistic in their projections
universal agreement (the physical arguments for each model seem to be reasonable). However, one can certainly ask the question-what is the relative ranking of the models in terms of their conservatism? This question does have an answer and it is illustrated in Fig. 12.25. When the models are used to fit the same set of accelerated TDDB data, the E-Model gives a shorter time-to-failure TF, as one extrapolates from high-field accelerated TDDB conditions to lower-field use conditions. This makes the E-Model the more conservative model. In terms of relative rank of conservatism: E-Model is the most conservative, followed by $\sqrt{E}$-Model, then the V-Model, and finally the $1 /$ E-Model.

It should be noted that the $E$-Model TF, unlike $1 / \mathrm{E}$ and V-Models, does not go to infinity as the field $E$ (or voltage) goes to zero. This is because the poly/oxide/ silicon capacitor has been fabricated into a very highly-ordered structure which is metastable, as discussed in Chap. 9. Thus, we expect this metastable state will degrade with time, even when the electric field (or voltage) is zero. Therefore, the electric field simply serves to accelerate this natural degradation process. When the electric field goes to zero, the natural degradation/diffusional-processes still exist which will degrade the dielectric quality and will eventually cause failure, even though it may take hundreds or thousands of years in the absence of electric field.# Example Problem 7 

In a high-reliability application, capacitors were made of a silica-based dielectric of thickness $90 \AA$. During accelerated testing at 9 V , the dielectrics started to fail in 5 s at $105^{\circ} \mathrm{C}$. How long would the capacitors be expected to last at 5 V ?

## Solution

Since this is a high-reliability application, we will use a conservative TDDB model like the E-Model. In the E-Model, the field acceleration parameter $\gamma$ is given by:

$$
\begin{aligned}
& \gamma(T)=\frac{p_{\text {eff }}}{K_{\mathrm{B}} T} \cong \frac{13 \mathrm{e} \AA}{\left(8.62 \times 10^{-5} \mathrm{eV} / K\right)(105+273) \mathrm{K}} \cdot\left(\frac{10^{-8} \mathrm{~cm}}{1 \AA}\right) \\
& =4.0 \times 10^{-6} \mathrm{~cm} / \mathrm{V}=4.0 \mathrm{~cm} / \mathrm{MV}
\end{aligned}
$$

The acceleration factor for TDDB (using E-Model) becomes:

$$
\begin{aligned}
& \mathrm{AF}=\frac{(\mathrm{TF})_{5-\text { volts }}}{(\mathrm{TF})_{9-\text { volts }}}=\exp \left[\gamma \cdot\left(\frac{9 \mathrm{~V}}{t_{\mathrm{ox}}}-\frac{5 \mathrm{~V}}{t_{\mathrm{ox}}}\right)\right] \\
& =\exp \left[\left(4 \times 10^{-6} \mathrm{~cm} / \mathrm{V}\right) \cdot\left(\frac{9 \mathrm{~V}}{90 \times 10^{-8} \mathrm{~cm}}-\frac{5 \mathrm{~V}}{90 \times 10^{-8} \mathrm{~cm}}\right)\right] \\
& =5.26 \times 10^{7}
\end{aligned}
$$

Therefore, one would expect that the capacitors would last at $105^{\circ} \mathrm{C}$ for:

$$
\begin{aligned}
& (\mathrm{TF})_{5-\text { volts }}=\mathrm{AF} \cdot(\mathrm{TF})_{9-\text { volts }}=\left(5.26 \times 10^{7}\right) \cdot(5 \mathrm{~s})=2.63 \times 10^{8} \mathrm{~s} \\
& =\left(2.63 \times 10^{8} \mathrm{~s}\right) \cdot\left(\frac{1 \mathrm{~h}}{3,600 \mathrm{~s}}\right)\left(\frac{1}{8,760 \mathrm{~h}}\right) \\
& =8.3 \text { years. }
\end{aligned}
$$

## Example Problem 8

For the capacitors in Example Problem 7, what is the maximum design voltage which should be used for these capacitors, if one wants them to last at least 15 years at $105^{\circ} \mathrm{C}$ ?

## Solution

The caps lasted 5 s at 9 V , but we need them to last a minimum of 15 yrs. Thus, we need an acceleration factor of at least:$$
(\mathrm{AF})_{\text {needed }}=\left(\frac{15 \text { years }}{5 \mathrm{~s}}\right)\left(\frac{3,600 \mathrm{~s}}{1 \mathrm{~h}}\right)\left(\frac{8,760 \mathrm{~h}}{1 \text { year }}\right)=9.46 \times 10^{7}
$$

However, the acceleration factor is also given by:

$$
(\mathrm{AF})=\left(\frac{(\mathrm{TF})_{V-\text { design }}}{(\mathrm{TF})_{9-\text { volts }}}\right)=\exp \left[\gamma \cdot\left(\frac{9 \mathrm{~V}}{t_{\mathrm{ox}}}-\frac{V_{\text {design }}}{t_{\mathrm{ox}}}\right)\right]
$$

Solving for $V_{\text {design }}$ one obtains:

$$
\begin{aligned}
V_{\text {design }} & =9 \mathrm{~V}-\frac{t_{\mathrm{ox}}}{\gamma} \ln (\mathrm{AF}) \\
& =9 \mathrm{~V}-\frac{90 \times 10^{-8} \mathrm{~cm}}{4 \times 10^{-6} \mathrm{~cm} / \mathrm{V}} \ln \left(9.46 \times 10^{7}\right) \\
& =4.87 \mathrm{~V}
\end{aligned}
$$

Therefore, to last at least 15 years at $105^{\circ} \mathrm{C}$, the maximum design voltage for this $90 \AA$ silica-based dielectric is $\leq 4.87 \mathrm{~V}$.

# 5.6 Complementary Electric Field and Current-Based Models 

There have been several attempts to include both field-induced degradation and current-induced degradation into a single TDDB model with some degree of success. These modeling efforts permit both field-induced and current-induced dielectric degradation mechanisms to occur simultaneously, in parallel fashion, during the TDDB testing. If it is assumed that the root cause of TDDB is bond-breakage/trapcreation, then let us look at the bond-breakage rate equation,

$$
\frac{\mathrm{d} N}{\mathrm{~d} T}=-k N(t)
$$

where $N$ is the number of $\mathrm{Si}-\mathrm{O}$ bonds in the region of interest and k is the bondbreakage rate constant. Separating variables in the above equation and integrating, one obtains:

$$
\int_{N_{0}}^{N_{\mathrm{on}}} \frac{\mathrm{~d} N}{N}=-k \int_{0}^{\mathrm{TF}} \mathrm{~d} t
$$giving,

$$
\mathrm{TF}=\frac{\ln \left(1 / f_{\text {crit }}\right)}{k}
$$

where $f_{\text {crit }}=\left(N / N_{0}\right)_{\text {crit }}$ is the critical fraction of bonds that must be broken to produce failure. It is believed that only a relatively few of the total number of bonds must be broken to cause TDDB, thus $\mathrm{f}_{\text {crit }}$ is expected to be only slightly less than one.

Now let us assume that the total reaction rate constant k is the sum of two independent bond-breakage mechanisms: $k=k_{1}+k_{2}$. The total reaction rate becomes:

$$
\begin{aligned}
k=k_{1} & +k_{2}=\ln \left(1 / f_{\text {crit }}\right)\left[\frac{1}{(\mathrm{TF})_{1}}+\frac{1}{(\mathrm{TF})_{2}}\right] \\
& =\ln \left(1 / f_{\text {crit }}\right)\left[\frac{(\mathrm{TF})_{1}+(\mathrm{TF})_{2}}{(\mathrm{TF})_{1}(\mathrm{TF})_{1}}\right]
\end{aligned}
$$

Combining Eqs. (12.30) and (12.31), one obtains:

$$
\mathrm{TF}=\frac{(\mathrm{TF})_{1}(\mathrm{TF})_{2}}{(\mathrm{TF})_{1}+(\mathrm{TF})_{2}}
$$

The above TF equation is valid for degradation mechanisms that are acting independently, but acting concurrently. One can see that if $(\mathrm{TF})_{1}$ is much greater than $(\mathrm{TF})_{2}$, then the time-to-failure TF is completely dominated by $(\mathrm{TF})_{2}$, and vice versa.

As for TDDB, let us assume that above $E=10 \mathrm{MV} / \mathrm{cm}$ the current-based 1/EModel physics (hole-catalyzed bond-breakage mechanism) could be dominating the TDDB physics. Below $E=10 \mathrm{MV} / \mathrm{cm}$, where anode hole-injection is relatively small, the field-based E-Model physics (thermal breakage of field-stretched bonds) could be dominating. Thus, a single time-to-failure equation (combining the physics of both the E-Model and 1/E-Model) would take the form:

$$
\mathrm{TF}=\frac{(\mathrm{TF})_{\mathrm{E}-\text { Model }}(\mathrm{TF})_{1 / \mathrm{E}-\text { Model }}}{(\mathrm{TF})_{\mathrm{E}-\text { Model }}+(\mathrm{TF})_{1 / \mathrm{E}-\text { Model }}}
$$

Shown in Fig. 12.26 is a single time-to-failure TF model, when both the fieldbased E-Model and the current-based 1/E-Model are combined into a single model.

Current-induced hole capture could serve to catalyze the bond-breakage process, ${ }^{43}$ thus playing an important role in TDDB. Hole capture can lead to a very strong $\mathrm{Si}-\mathrm{O}$ bond suddenly becoming a much weaker bond. This weakened bond is now amenable to field-enhanced thermal breakage. Also, a hydrogen-release model has been

[^0]
[^0]:    ${ }^{43}$ Remember that a hole is simply a missing bonding electron. Hole capture thus eliminates one of the two electrons in the S-O bond. Therefore, hole capture serves to weaken the bond. Furthermore, the hole (if hot) can also bring energy to the bond to help in the bond-breakage process.

Fig. 12.26 E and 1/E-Models are combined into a single time-to-failure model. It is believed that current-induced degradation may dominate at very high fields $(E>10 \mathrm{MV} / \mathrm{cm})$, while field-induced degradation may dominate at lower fields $(E<10 \mathrm{MV} / \mathrm{cm})$
proposed to better explain the power-law V-Model (with an exponent of $n \sim 40$ ) used for time-to-failure. Both the hole-injection and the hydrogen-release models are expected to show a polarity dependence which is widely reported for hyper-thin $(\leq 4.0 \mathrm{~nm})$ gate oxides. Also, the adverse effects of hydrogen on TDDB have been studied.

In summary, there has been great disagreement in the technical community as to the dominant degradation mechanism for low-field TDDB in $\mathrm{SiO}_{2}$ thin films, i.e., is the major degradation mechanism related to current or field? Certainly hole capture and hydrogen release are relevant mechanisms and must be folded into any TDDB discussion. While the E-Model has been widely used and has been quite successful in describing low-field TDDB data for thick films $>4.0 \mathrm{~nm}$; however, for very thin oxides $(<4.0 \mathrm{~nm})$, the direct-tunneling current (ballistic transport) can be very high in these films and could mean that the degradation mechanism in hyper-thin oxide films is more controlled by current than field. In any case, as illustrated in Fig. 12.25, the E-Model is generally accepted as being the most conservative of the TDDB Models. The next most conservative model would be a complementary combination of the TDDB models, using the approach that was described by Eqs. (12.32) and (12.33) and as illustrated in Fig. 12.26.

Also, TDDB should not be considered just a MOSFET gate oxide or capacitoroxide issue. The issue of TDDB has also been raised for interconnects (metallization plus surrounding/supporting dielectrics) with the introduction of low-k dielectrics. TDDB data for interconnect dielectrics is normally taken using comb-comb or comb-serpent type test structures as illustrated in Fig. 12.27. While silica-based low-k dielectric materials enable significant performance gains at the interconnect level in terms of circuit delay reduction, they also possess substantially inferior electrical properties relative to gate oxide dielectric quality in terms of leakage and breakdown strength.Fig. 12.27 Typical interconnect-dielectric test structure is illustrated. Shown is a comb-serpent type test structure with minimum pitch (minimum line-width plus minimum space). A simple breakdown strength measurement, or TDDB data, can be an indication of interconnect dielectric goodness


Fig. 12.28 TDDB data for various silica-based dielectrics at $105^{\circ} \mathrm{C}$. The lower-k materials MSQ $(k=$ 2.3), OSG [ $\operatorname{SiCOH}(k=$ 2.9)], and FSG [ $\operatorname{SiOF}(k=$ 3.5)] generally have lower breakdown strength and time to failure. However, all of these silica-based materials have a very similar E-Model field acceleration parameter of $\gamma \approx 4 \mathrm{~cm} / \mathrm{MV}$ (or a $p_{\text {eff }} \approx 13 \mathrm{e} \AA$ )


Presently, minimum intra-metal spacing between adjacent interconnect stripes is approaching the physical dimensions of gate oxides ( $<100 \mathrm{~nm}$ ) used a couple of decades ago. Hence, a discussion of which TDDB model to use is also pertinent to low-k dielectrics as well. Oxide-based low-k dielectrics have been shown to have inferior breakdown strength and significantly wider failure distributions under constant voltage stress. This is attributed to the presence of pre-existing defects in the low-k dielectrics that scale roughly with the degree of porosity present within the low-k. Yet, as illustrated in Fig. 12.28, these low-k TDDB results indicate that the field acceleration parameter $\gamma$ is similar for all of these silica-based materials: a field acceleration parameter of $\gamma \sim 4 \mathrm{~cm} / \mathrm{MV}$ at $105^{\circ} \mathrm{C}$ (giving an effective dipole moment $p_{\text {eff }} \sim 13 \mathrm{e} \AA$ ).

A pore in the context of low-k porosity is defined as a localized region in the dielectric of low-polarizability. In this pore region weak bonds can exist and thesecan serve as charge traps. Percolation theory, along with the assumption of preexisting electrically active defects that scale with the degree of porosity, has been used to explain both the degraded breakdown strength and wider failure distributions with low-k dielectrics. Thus, the TDDB of the low-k materials should be assessed when using these low-k materials in an advanced integration scheme. Also, the contact to gate edge spacing is presently only a few hundred Angstroms, similar to gate oxide thickness just a couple of decades ago. Thus, gate-to-contact TDDB should be considered.

# 6 Mobile-Ions/Surface-Inversion 

Alkaline-metal elements such as $\mathrm{Li}, \mathrm{Na}$, and K can sometimes be found in the semiconductor processing materials. In $\mathrm{SiO}_{2}$, these ions are very mobile under the presence of modest electric fields $(\sim 0.5 \mathrm{MV} / \mathrm{cm})$ and temperatures $\left(100{ }^{\circ} \mathrm{C}\right)$. An accumulation of the drifted ions at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface (see Fig. 12.29) can cause surface inversion and can lead to increased leakage for isolation-type devices in silicon and eventual device failure.

Sodium and potassium (and perhaps lithium) are the usual mobile-ion suspects, simply because of their high mobility and their relative abundance in some materials. Under bias, they can drift from the poly (anode) to the silicon substrate (cathode). A buildup of positive ions at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface can invert the surface and severely degrade the oxide isolation. Ionic drift in $\mathrm{SiO}_{2}$ gate dielectric can also cause premature TDDB. In the case of EPROMs ${ }^{44} /$ EEPROMs ${ }^{45} /$ Flash-Memories, ${ }^{46}$


Fig. 12.29 If any mobile ions are in the dielectric, they can drift in the oxide isolation due to the presence of an electric field. Such mobile-ion drift can cause surface inversion in the P-well region. Surface inversion can result in a leakage-path creation from N -well to the adjacent $\mathrm{n}^{+}$moat

[^0]
[^0]:    ${ }^{44}$ EPROM is an erasable programmable read-only memory.
    ${ }^{45}$ EEPROM is an electrically erasable programmable read-only memory.
    ${ }^{46}$ Flash Memories are block-erasable EEPROMs.mobile-ion accumulation around the negatively charged floating poly-gate can lead to data-retention fails.

Devices showing inversion-induced leakage failures can often recover during an unbiased high-temperature bake. The bake causes a redistribution of the mobile ions from the accumulated $\mathrm{Si} / \mathrm{SiO}_{2}$ interface (or away from the floating poly in the case of an EPROM-like devices) and can bring about device recovery.

Since the mobile-ion flux is impacted by both electric field and temperature, the TF is usually described by

$$
\mathrm{TF}=A_{0} J_{\mathrm{ion}}^{-1} \exp \left(\frac{Q}{K_{B} T}\right)
$$

where:

$$
J_{\text {ion }}=\left\langle\left(\frac{D_{0}}{K_{B} T}\right) \rho[e E(t)]-D_{0} \frac{\partial \rho(x, t)}{\partial x}\right\rangle
$$

and where $J_{\text {ion }}$ is the time-averaged flux of mobile ions. The first term on the righthand side of Eq. (12.35) is the drift component, with $E$ the externally applied electric field, $D_{0}=$ diffusion coefficient and $\rho=$ density of mobile ions. The second term is the back-diffusion component, and the brackets $\rangle$ represent the time-averaged value of the time-dependent quantities enclosed. Note that if the field is turned off and the device is baked (an unbiased bake), the mobile ions will diffuse away from the interface and the device can recover. This is generally referred to as a bake-recovery failure mechanism. The activation energy $Q$ depends upon the IC medium through which the ions must diffuse. For Na diffusion through silica-based dielectrics, device-failures tend to have an activation energy range from 0.75 to 1.8 eV , with 1.0 eV being typically used in modeling.

It is interesting to note that Cu -ions can be mobile in silica-based dielectrics, thus free Cu -ions under electrical bias are also a concern for interconnects. The loss of barrier integrity or the presence of Cu -related corrosion defects will lead to substantially degraded back-end dielectric reliability performance. Since many interfaces exist with Cu interconnect technology, relatively fast diffusion pathways always seemed to be available for any free Cu -ions. Since such defects are difficult to observe under use conditions, their statistical presence must be determined using accelerated test conditions and rapid tests such as ramped-breakdown testing. ${ }^{47}$ Usually, Cu-ion drift under an electric field is more of an interconnect TDDB issue than a surface-inversion issue.

In summary, the activation energy for ion diffusion depends on: the diffusing species, medium through which the mobile ions diffuse, and the concentration of the

[^0]
[^0]:    ${ }^{47}$ Ramped-to-breakdown testing was extensively discussed in Chap. 11. The ramp-to-breakdown test can be a very important test for interconnect dielectric reliability. Both intrinsic issues (low-k integrity) and extrinsic issues (metal/dielectric defects) can be found in a ramp-to-breakdown test at elevated temperature.ions. If the mobile-ion concentration is relatively low, and if deep interfacial traps exist, then one may see interfacial deep-traps that dominate with higher activation energy $(\sim 1.8 \mathrm{eV})$ for $\mathrm{Na}^{+}$diffusion noted. However, if the concentration of $\mathrm{Na}^{+}$is relatively high, such that all deep interfacial traps are filled, leaving residual mobile $\mathrm{Na}+$ ions to freely diffuse, then one may see lower activation energy $(Q \sim 0.75 \mathrm{eV})$.

# 7 Hot-Carrier Injection 

Channel HCI describes the phenomena by which electrons (or holes) can gain sufficient kinetic energy, as they are accelerated along the channel of a MOSFET (see Fig. 12.30), such that they can be injected over either the 3.1 eV barrier (for electrons) or 4.7 eV barrier (for holes) that exists at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface. The channel electrons, as they are accelerated from source to drain can acquire the needed energy for injection into the $\mathrm{SiO}_{2}$, especially those lucky electrons ${ }^{48}$ located near the tail of the Boltzmann distribution. These lucky electrons (or hot carriers) ${ }^{49}$ are redirected toward the gate oxide as a result of impact ionization near the drain end of the MOSFET device where the channel electric field is the greatest. HCI serves to produce damage at the interface (interface-state generation).

Interface-state generation and charge trapping by this HCI mechanism can result in transistor parameter degradation. This is an important degradation mechanism,


Fig. 12.30 Carriers traveling along N-MOSFET channel are accelerated from source to drain. These accelerated electrons reach kinetic energies well above their normal thermal energy [(3/2) $K_{B} T$ ] and, as such, are referred to as hot carriers. Hot carriers can produce impact ionization near the drain end (where the electric field along the channel is greatest) causing some of the carriers to be redirected toward the gate oxide. These redirected (and energetic) electrons can interact with the normal bonding at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface and produce damage (create new interface states or fill existing ones). Interface-state generation usually results in device degradation (changes in critically important device parameters, e.g., $V_{t}, \mathrm{gm}, I_{\text {drive }}$, etc.)

[^0]
[^0]:    ${ }^{48}$ Lucky electron means that it obtains the maximum possible kinetic energy.
    ${ }^{49}$ These energetic electrons are referred to as hot, because their kinetic energy is greater than the average thermal energy $(3 / 2) K_{B} T$.

Fig. 12.31 Interface between the silicon substrate and the $\mathrm{SiO}_{2}$ gate dielectric is illustrated. Silicon atoms in the silicon substrate are four-fold bonded in a crystalline lattice. The $\mathrm{SiO}_{2}$ layer is amorphous with the silicon four-fold bonded to neighboring oxygen (in a tetrahedral arrangement). The oxygen at the corners of each tetrahedron are two-fold bonded to neighboring silicon. Due to lattice mismatch at the interface, not all silicon bonds will be satisfied (creating dangling silicon bonds). Hydrogen is usually introduced during MOSFET fabrication, to chemically tie-up/terminate these dangling bonds and prevent them from being electrically active
especially for advanced technologies where the channel electric fields (which accelerate the carriers) have increased faster than the reductions in operating voltage. Thus, HCI can be an important MOSFET degradation mechanism. Since the MOSFET is a field-effect device, the interface between the silicon substrate and the $\mathrm{SiO}_{2}$ gate dielectric is critically important. Usually, device instabilities come about due to degradation (bond-breakage) at this interface. For this reason, a closer look at this interface is illustrated in Fig. 12.31.

Silicon atoms in the silicon substrate are four-fold bonded in a crystalline lattice. The $\mathrm{SiO}_{2}$ layer is amorphous with the silicon four-fold bonded to the neighboring oxygen (in a tetrahedral arrangement). The oxygen at the corners of each tetrahedron is two-fold bonded to neighboring silicon atoms. Due to the mismatch in lattice structure at the interface, not all silicon bonds will be satisfied (creating a silicon dangling bond). Hydrogen is usually introduced during MOSFET fabrication, in order to chemically tie-up/terminate these dangling bonds and to prevent them from being electrically active. The impact of $\mathrm{Si}-\mathrm{O}$ and $\mathrm{Si}-\mathrm{H}$ bond breakage, and its impact on TDDB was discussed in Section 5. In this section and the next, we will focus on the impact that bond breakage at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface can have on MOSFET device stability.

Initially, after $\mathrm{SiO}_{2}$ growth, there are likely to be at least some broken bonds, or at least some very weak $\mathrm{Si}-\mathrm{O}$ bonds, in the bulk of the $\mathrm{SiO}_{2}$ and at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface. Depending on the location of the Fermi Level (Chemical Potential), these dangling bonds ${ }^{50}$ can serve as electron traps, hole traps, or remain neutral. If

[^0]
[^0]:    ${ }^{50}$ Normally, each $\mathrm{Si}-\mathrm{O}$ bond has two electrons in it which are being shared. If the bond is broken (thus forming a dangling bond), depending on the chemical potential (Fermi-level), a dangling bond can be neutral (retains a single electron), can become negative with the trapping of a second electron, or can give up its single electron (hole trap) and become positively charged.

Fig. 12.32 As electrons are accelerated from source to drain, impact ionization at the drain end of the MOSFET can produce electron-hole pairs. Some of these energetic electrons will be redirected toward the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface. These energetic electrons are capable of producing interface damage in a localized region near the drain end. The holes (since they are majority carriers) are easily collected as substrate current. The substrate current is an indirect indicator of the HCI-induced damage
these dangling bonds charge during operation, then the MOSFET operational parameters can degrade. Interface stability can be extremely important for reliable MOSFET operation. If device operation serves to break the $\mathrm{Si}-\mathrm{H}$ bonds at the interface, then the exposed Si-dangling bond may charge and degrade MOSFET operational parameters. Thus, the interface must remain relatively stable for the MOSFET device to be stable.

As discussed in Chap. 3 (Sec. 2), device-parameter degradation (induced by HCI) can be described by

$$
\Delta P=B_{0} t^{m}
$$

where:
$P$ is the parameter of interest $\left(V_{t}, g m, I_{\text {dsat }}, \mathrm{etc.}\right)$,
$t$ is the time,
$B_{0}$ is a material/device-dependent parameter, and $m(\simeq 0.5)$ is the power-law exponent for the HCI time dependence.

As illustrated in Fig. 12.32 for N-channel MOSFETs, when the hot electron undergoes impact ionization near the drain end of the device, holes are produced during the impact collision event which can be collected as substrate current $I_{\text {sub }}$. While it is gate current that produces the transistor damage, the substrate current measurement is generally easier. Therefore, even though the substrate current is a pseudo stress, it is a good proxy for the actual stress (gate current).

The peak $I_{\text {sub }}$ current thus becomes an easy-to-measure indicator of the material/ device stress that will be occurring during the channel hot-carrier testing. The time-to-failure expression that is generally used for N -channel transistors is

$$
\mathrm{TF}=A_{0}\left(\frac{I_{\mathrm{sub}}}{w}\right)^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$where:
$I_{\text {sub }}$ is the peak substrate current ${ }^{51}$ during stressing,
$w$ is the width of the transistor,
$n$ is the power-law exponent, approximately equal to 3 , and
$Q$ is the activation energy and is approximately -0.25 to +0.25 eV depending on channel length.
$A_{0}$ is a device-dependent parameter, which will vary from device to device and will produce a distribution of times-to-failure.

The peak substrate current $I_{\text {sub }}$ has been divided by the transistor width w in an effort to make $I_{\text {sub }} / \mathrm{w}$ a true stress (a stress that is roughly independent of the device width, as discussed in Chap. 9, Sec. 4). The activation energy for HCI is small, and can be positive or negative depending on channel length. The positive values for activation energy are generally observed only for gate lengths $<0.25 \mu \mathrm{~m}$.

# Example Problem 9 

To better understand the hot-carrier injection lifetime of an n-type MOSFET, a device was stressed for 1 h at 7.5 V and a $10 \%$ reduction in drive current was recorded. It was also recorded that the peak substrate current was 30 times higher at 7.5 V vs. the expected 5.0 V operation. How long would it take to see a $10 \%$ reduction in drive current at the expected operation of 5.0 V ?

## Solution

Using Eq. (12.37), the acceleration factor becomes:

$$
\mathrm{AF}=\left[\frac{\left(I_{\text {sub }} @ 7.5 \mathrm{~V}\right)}{I_{\text {sub }} @ 5.0 \mathrm{~V}}\right]^{3}=\left[\frac{30}{1}\right]^{3}=2.7 \times 10^{4}
$$

Therefore, the time-to-fail at 5.0 V vs. 7.5 V becomes:

$$
\begin{aligned}
\mathrm{TF}_{\oplus 50 \mathrm{~V}}= & \mathrm{AF} \cdot \mathrm{TF}_{\oplus 75 \mathrm{~V}} \\
& \left(2.7 \times 10^{4}\right) \cdot 1 \mathrm{~h} \\
& =2.7 \times 10^{4} \mathrm{~h}\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right) \\
& =3.1 \text { years. }
\end{aligned}
$$

[^0]
[^0]:    ${ }^{51}$ The gate voltage $\left(V_{\mathrm{gs}}\right)$ conditions must be determined that produce the maximum substrate current, for a fixed drain-to-source voltage $V_{\mathrm{ds}}$. For an n-type MOSFET, this could be $V_{\mathrm{gs}}=(1 / 2)$ $V_{\mathrm{ds}}$ for n-type MOSFETs with longer channel lengths ( $>0.25 \mu \mathrm{~m}$ ) but could be $V_{\mathrm{gs}}=V_{\mathrm{ds}}$ for devices with shorter channel lengths. In any case, the voltage conditions which produce the maximum substrate current must be established for the full range of expected device operation.Historically, HCI for P-channel devices has been of lesser concern. This is generally true because of lower hole-mobility and the increase in barrier height for hole-injection. For P-channel devices, sometimes the gate current $I_{\text {gate }}$ is the better indicator of the actual stress on the device. Thus, for P-channel devices the time-tofailure equation for HCI is usually written

$$
\mathrm{TF}=A_{0}\left(\frac{I_{\text {gate }}}{w}\right)^{-n} \operatorname{Exp}\left(\frac{Q}{K_{B} T}\right)
$$

where:
$I_{\text {gate }}$ is the peak gate current during stressing,
$w$ is the width of the transistor,
$n$ is the power-law exponent and is generally from 2 to 4 , and
$Q$ is the activation energy, generally from -0.25 eV to +0.25 eV .

In summary, HCI-induced transistor degradation seems to be satisfactorily modeled by using peak substrate current $I_{\text {sub }}$ for the N -channels and peak gate current $I_{\text {gate }}$ for the P -channels, at least for transistors at $>0.25 \mu \mathrm{~m}$. The drive current for the N -channel device tends to reduce after HCI stressing (i.e., HCI stressing tends to produce charge trapping such that it serves to increase the effective channel length for the N-channel device). The P-channel drive current tends to increase after HCI stress (i.e., HCI stressing tends to produce charge trapping such that the degradation serves to effectively shorten the channel length for the P-channel devices) and the off-state leakage can increase significantly.

While HCI-induced transistor degradation measurements and modeling seem to be quite accurate, the extrapolation from transistor degradation to circuit-level degradation is often difficult and makes IC time-to-failure predictions difficult. First, one must consider the actual fraction-of-time (duty cycle) that a transistor in an IC actually experiences the maximum/peak substrate current (or maximum gate current) conditions. For fast switching transistors, this can be less than $10 \%$ of the time. Second, how much transistor degradation (5, 10, $20 \%$, or ?) can the circuit tolerate before some critical circuit parameter (speed, power, leakage, etc.) starts to shift?

For the reasons listed above, sometimes it is easier and more precise to simply take an empirical approach to establishing the HCI impact at the circuit level. In this empirical approach, one takes a sampling of the ICs and puts the sample on operational life test at an elevated voltage level (higher than expected operating voltage). The circuit-level degradation can then be recorded as a function of stress time. Using the acceleration factor, which is easily extracted from the above models, one can then find out how the circuit will be expected to degrade during normal operation.# 8 Negative-Bias Temperature Instability 

For a MOSFET device, as illustrated in Fig. 12.30, the stability of the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface is of great importance. If the $\mathrm{Si}-\mathrm{H}$ bonds at this interface become broken during device operation, as shown in Fig. 12.33, then the device properties will degrade and device failure can eventually occur.

In Fig. 12.33, the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface is illustrated between the silicon substrate and the gate dielectric. Since the P-type MOSFET operates with a negative gate voltage, the electric field in the $\mathrm{SiO}_{2}$ layer is directed away from the interface. If a $\mathrm{Si}-\mathrm{H}$ bond is broken during device operation thus freeing an $\mathrm{H}+$ ion, the drift direction is away from the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface. This illustrates why negative-bias temperature instability for P-channel MOSFET is usually more of an issue than the sister problem of positive-bias temperature instability (PBTI) associated with an N-type MOSFET. However, PBTI can still be an issue when the dielectric is something other than $\mathrm{SiO}_{2}$, e.g., high-k gate dielectrics.

The bond-breakage mechanism is thought to be a result of hole capture by the $\mathrm{Si}-\mathrm{H}$ bond during device operation. A possible degradation reaction is given by:

$$
\mathrm{Si}-\mathrm{H}+(\text { hole })^{+} \rightarrow \mathrm{Si}-+\mathrm{H}^{+}
$$

where $\mathrm{Si}-\mathrm{H}$ represents a normal silicon-hydrogen bond, Si -represents a silicon dangling bond, and $\mathrm{H}^{+}$represents a freed hydrogen ion (proton). Due to the electric field which is present, refer to Fig. 12.33, any hydrogen ions $\mathrm{H}^{+}$generated (due to the above reaction) will tend to drift away from the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface and into the bulk of the $\mathrm{SiO}_{2}$. Recall from Chap. 5, once the $\mathrm{H}^{+}$ions are generated, one would expect the ions to drift away from the interface governed by the transport equation:

$$
J(x, t)=\mu \rho(x, t)(q E)-D \frac{\partial \rho(x, t)}{\partial x}
$$



Fig. 12.33 Interface $\left(\mathrm{Si} / \mathrm{SiO}_{2}\right)$ for a P-type MOSFET is illustrated. Since the P-type MOSFET operates with a negative gate voltage, the electric field in the $\mathrm{SiO}_{2}$ layer is directed away from the interface. If a $\mathrm{Si}-\mathrm{H}$ bond is broken during device operation, thus freeing an $\mathrm{H}^{+}$ion, the drift direction is away from the $\mathrm{Si} / \mathrm{SiO}_{2}$ interfacewhere $\rho(\mathrm{x}, \mathrm{t})$ is the density of $\mathrm{H}^{+}$ions at a distance x from the interface at any time $t$, le! $E$ is the force action on the $\mathrm{H}^{+}$ion, $D$ is the diffusivity of the $\mathrm{H}^{+}$ion, and $\mu$ is the mobility of the $\mathrm{H}^{+}$ion and is related to the diffusivity through the Einstein relation:

$$
\mu=\frac{D}{K_{B} T}=\frac{D_{0} \exp \left(-\frac{Q}{K_{B} T}\right)}{K_{B} T}
$$

One can see from Eq. (12.40), as the $H^{+}$ions tend to drift away from the interface due to the presence of the electric field $E$, the concentration of $\mathrm{H}^{+}$ions in the $\mathrm{SiO}_{2}$ starts to increase. As the concentration of $\mathrm{H}^{+}$ions grows in the $\mathrm{SiO}_{2}$ dielectric, a backflow of $\mathrm{H}^{+}$ions (toward the interface) can be expected to develop. In fact, if the stress stops (electric field goes to zero), then the backflow of $\mathrm{H}^{+}$ions is expected to occur causing some device recovery to take place. Complete recovery does not generally take place because some of the $\mathrm{H}^{+}$ions may undergo a reduction reaction while in the $\mathrm{SiO}_{2}$ gate dielectric. ${ }^{52}$ Several reduction reactions are possible:

$$
\mathrm{H}^{+}+\mathrm{e} \rightarrow \mathrm{H}
$$

or

$$
\mathrm{H}^{+}+\mathrm{H}+\mathrm{e} \rightarrow \mathrm{H}_{2}
$$

or

$$
\mathrm{H}^{+}+\mathrm{H}^{+}+2 \mathrm{e} \rightarrow \mathrm{H}_{2}
$$

The electrical impact of NBTI on p-MOSFET device characteristics is substantial: a shift can occur in the threshold voltage of the device and a decrease in hole mobility in the inversion channel. Both the $V_{t}$ shift and mobility degradation lead to reduced current in the channel ( $I_{\text {drive }}$ ) of the device and, as a consequence, degraded device performance. The threshold voltage $V_{t}$ shift with time is observed to take the form:

$$
\frac{\Delta V_{t}}{\left(V_{t}\right)_{0}}=B_{0}(E, T)(t)^{m}
$$

where $B_{0}(E, T)$ is a prefactor that is electric field $E$ and temperature $T$ dependent. $m$ is the power-law exponent for the time $t$. Generally, $m=0.15-0.35$, with $m=0.25$ often observed.

[^0]
[^0]:    ${ }^{52}$ It is also possible that some of the $\mathrm{H}^{+}$ions may be reduced and dispersed within the poly-gate electrode and/or diffuse laterally from the gate region.Since the time-dependence exponent $m$ is less than 1, then we know from Chap. 3 that the degradation with time will tend to saturate. Such degradation saturation is fully expected from the reaction-diffusion model illustrated in Fig. 12.33. Since the number of $\mathrm{S}-\mathrm{H}$ bonds is finite, then the degradation rate due to $\mathrm{Si}-\mathrm{H}$ bond breakage must reduce as the number of unbroken $\mathrm{Si}-\mathrm{H}$ bonds dwindles with time.

# Example Problem 10 

During a NBTI stress test of a P-channel MOSFET, it was determined that the $V_{t}$ shifted by $10 \%$ in 100 h . How long would it take the $V_{t}$ to shift by $20 \%$ ? Assume a time-dependence exponent of $\mathrm{m}=0.25$.

## Solution

Given the $10 \%$ degradation in 100 h , one can determine $B_{0}$ for the set of stress conditions using Eq. (12.43):

$$
0.1=B_{0}(100 \mathrm{~h})^{0.25}
$$

giving: $B_{0}=0.0316 /(\mathrm{h})^{1 / 4}$. Solving Eq. (12.43) for time $t$, one obtains:

$$
t=\left[\frac{1}{B_{0}}\left(\frac{\Delta V_{t}}{\left(V_{t}\right)_{0}}\right)\right]^{1 / m}
$$

giving

$$
t=\left[\frac{1}{0.0316 /(\mathrm{h})^{1 / 4}}(0.2)\right]^{4}=1,605 \mathrm{~h}
$$

Note that, because NBTI is a saturating degradation mechanism, it took only 100 h to reach a $10 \%$ degradation level for the device, but it took more than $1,600 \mathrm{~h}$ to reach a $20 \%$ degradation level. The full plot is shown (Fig. 12.34).

The field $E$ and temperature $T$ dependence of the prefactor $B_{0}(E, T)$ takes the familiar form:

$$
B_{0}(E, T)=C_{0} \exp \left[\gamma_{\text {degradation }} \cdot E\right] \exp \left[-\frac{Q_{\text {degradation }}}{K_{B} T}\right]
$$

where $C_{0}$ is proportional to the concentration of $\mathrm{Si}-\mathrm{H}$ bonds at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface.

Time-to-failure TF for the device will occur at a time when the parameter degradation reaches some critical amount $\left[\left(\Delta V_{t}\right) /\left(V_{t}\right)_{0}\right]_{\text {crit }}$. Solving Eq. (12.43) for $t=\mathrm{TF}$, one obtainsFig. 12.34 NBTI
degradation shows saturation effects for longer times. Time-to-degrade to $10 \%$ was 100 h while the time- to-degrade to $20 \%$ was over $1,600 \mathrm{~h}$


$$
\mathrm{TF}=\left[\frac{1}{B_{0}}\left(\frac{\Delta V_{t}}{\left(V_{t}\right)_{0}}\right)_{\text {crit }}\right]^{1 / m}
$$

Using Eqs. (12.44) and (12.45), one obtains

$$
\mathrm{TF}=A_{0} \exp \left[-\gamma_{\mathrm{NBTI}} \cdot E\right] \exp \left[\frac{Q_{\mathrm{NBTI}}}{K_{B} T}\right]
$$

where:

$$
\begin{gathered}
A_{0}=\left[\frac{1}{C_{0}}\left(\frac{\Delta V_{t}}{\left(V_{t}\right)_{0}}\right)_{\text {crit }}\right]^{1 / m} \\
\gamma_{\mathrm{NBTI}}=\frac{\gamma_{\text {degradation }}}{m}
\end{gathered}
$$

and

$$
Q_{\mathrm{NBTI}}=\frac{Q_{\text {degradation }}}{m}
$$

One can see from Eq. (12.46) and Eq. (12.47) that the time-to-failure prefactor $A_{0}$ is dependent on the amount of parameter degradation that can be tolerated and inversely dependent on the concentration $C_{0}$ of $\mathrm{Si}-\mathrm{H}$ bonds at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface. It is not surprising that as $C_{0}$ goes to zero, the time-to-failure for the NBTI failure mechanism goes to infinity. One should also note that, just as Chap. 4 (Sect. 3.2)discussed, the time-to-failure kinetics $\left(\gamma_{\mathrm{NBTI}}, Q_{\mathrm{NBTI}}\right)$ are not the same as the degradation kinetics $\left(\gamma_{\text {degradation }}, Q_{\text {degradation }}\right) .{ }^{53}$ Accelerated NBTI degradation data suggests that the time exponent for degradation is $m=0.25$ and the degradation kinetics are given by: $\left(\gamma_{\text {degradation }}=0.8 \mathrm{~cm} / \mathrm{MV}, Q_{\text {degradation }}=0.15 \mathrm{eV}\right)$. Thus, the time-tofailure kinetics, as given by Eqs. (12.48) and (12.49), are expected to be four times greater or: $\left(\gamma_{\mathrm{NBTI}}=3.2 \mathrm{~cm} / \mathrm{MV}, Q_{\mathrm{NBTI}}=0.6 \mathrm{eV}\right)$.

# Example Problem 11 

NBTI accelerated data was taken on a P-channel MOSFET device with a gate oxide thickness of $t_{\mathrm{ox}}=35 \AA$. At 3.0 V and $150^{\circ} \mathrm{C}$, the time-to-failure (based on a $10 \% V_{t}$ shift) was recorded to be 1 h . How long would a similar device be expected to last at the operating conditions of 1.8 V and $105^{\circ} \mathrm{C}$ ? Assume an exponential field acceleration parameter: $\gamma_{\mathrm{NBTI}}=3.2 \mathrm{~cm} / \mathrm{MV}$.

## Solution

Acceleration factor due to voltage:

$$
\begin{aligned}
\mathrm{AF}_{\text {voltage }} & =\exp \left[\gamma_{\mathrm{NBTI}} \cdot\left(\frac{V_{\text {stress }}-V_{\mathrm{op}}}{t_{\mathrm{ox}}}\right)\right] \\
& =\exp \left[\left(3.2 \times 10^{-6} \mathrm{~cm} / \mathrm{V}\right) \cdot\left(\frac{3.0 \mathrm{~V}-1.8 \mathrm{~V}}{35.0 \times 10^{-8} \mathrm{~cm}}\right)\right] \\
& =5.82 \times 10^{4}
\end{aligned}
$$

Acceleration factor due to temperature:

$$
\begin{aligned}
\mathrm{AF}_{\text {temp }} & =\exp \left[\left(\frac{Q_{\mathrm{NBTI}}}{K_{B}}\right)\left(\frac{1}{T_{\mathrm{op}}}-\frac{1}{T_{\text {stress }}}\right)\right] \\
& =\exp \left[\left(\frac{0.6 \mathrm{eV}}{8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}}\right)\left(\frac{1}{(105+273) \mathrm{K}}-\frac{1}{(150+273) \mathrm{K}}\right)\right] \\
& =7.10
\end{aligned}
$$

Total acceleration factor:

$$
\mathrm{AF}=\mathrm{AF}_{\text {voltage }} \cdot \mathrm{AF}_{\text {temp }}=\left(5.82 \times 10^{4}\right) \cdot(7.10)=4.13 \times 10^{5}
$$

(continued)

[^0]
[^0]:    ${ }^{53}$ Note that for the case $m=0.25$, the time-to-failure kinetics are four times greater than the degradation kinetics!Therefore, the expected time-to-failure at use conditions is:

$$
\begin{aligned}
\operatorname{TF}\left(1.8 \mathrm{~V}, 105^{\circ} \mathrm{C}\right) & =\mathrm{AF} \cdot \mathrm{TF}\left(3.0 \mathrm{~V}, 105^{\circ} \mathrm{C}\right) \\
& =\left(4.13 \times 10^{5}\right) \cdot(1 \mathrm{~h}) \\
& =4.13 \times 10^{5} \mathrm{~h}\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right) \\
& =47 \text { years. }
\end{aligned}
$$

# Problems 

1. Electromigration data was taken, for an $\mathrm{Al}-\mathrm{Cu}$ alloy, using metal stripes much greater than the Blech length and with a width $\sim 2 \times$ the average metal grain size. At a current density of $J=2.5 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and temperature $T=175^{\circ} \mathrm{C}$, the median time-to-failure was $t_{50}=320 \mathrm{~h}$ with a logarithmic standard deviation of $\sigma=0.5$. Assuming an activation energy of $Q=0.8 \mathrm{eV}$ and a current density exponent of $n=2$, find the maximum design current density that can be used to have no more than $0.13 \%$ cumulative failures in 10 years at a metal temperature of $105^{\circ} \mathrm{C}$.

Answer: $J_{\text {design }}=4.9 \times 10^{5} \mathrm{~A} / \mathrm{cm}^{2}$
2. Electromigration data was taken, for dual-damascene Cu leads, using a via-fed Cu -stripe of minimum width and a length much longer than the Blech length. At a current density of $1.0 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and temperature $T=275^{\circ} \mathrm{C}$, the median time-to-failure was $t_{50}=31 \mathrm{~h}$ and with a logarithmic standard deviation of $\sigma=$ 0.4 . Assuming an activation energy of $Q=1.0 \mathrm{eV}$ and a current density exponent of $n=1$, find the maximum design current density that can be used in order to have no more than $0.13 \%$ cumulative failures in 10 years at $105^{\circ} \mathrm{C}$ metal temp.
Answer: $J_{\text {design }}=1.5 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$
3. In electromigration testing of an aluminum-alloy at $2 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$, it was found that the time-to-failure was 2 times longer for $66 \mu \mathrm{~m}$-long metal leads vs. $132 \mu \mathrm{~m}$-long metal leads. Determine the critical Blech constant $A_{\text {Blech }}$ $=(J \cdot L)_{\text {crit }}$ for this Al-alloy metal system.

Answer: $A_{\text {Blech }}=6,000 \mathrm{~A} / \mathrm{cm}$
4. In electromigration testing of copper at $1 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ it was found that the time-to-failure was 2 times longer for $30 \mu \mathrm{~m}$-long metal leads vs. $60 \mu \mathrm{~m}$-long metal leads. Determine the critical Blech constant $A_{\text {Blech }}=(J \cdot L)_{\text {crit }}$ for this Cu-metal system.

Answer: $A_{\text {Blech }}=2,000 \mathrm{~A} / \mathrm{cm}$5. During stress migration testing of Cu interconnects, it was found that a certain via would fail in 450 h when a chip was baked at $190^{\circ} \mathrm{C}$. Assuming a power-law stress-migration exponent of $n=3$, activation energy for diffusion of $Q=0.75$ eV , and a stress-free temperature of $T_{o}=270^{\circ} \mathrm{C}$ :
(a) Find the time-to-failure at $105^{\circ} \mathrm{C}$.
(b) What is the effective activation energy for the stress migration from $190^{\circ} \mathrm{C}$ vs. $105^{\circ} \mathrm{C}$ ?

Answers: a) $\mathrm{TF}_{\@_{0}=105 \mathrm{c}}=3,600 \mathrm{~h}$ b) $Q_{\text {eff }}=0.37 \mathrm{eV}$
6. During $85 \% \mathrm{RH}$ and $85^{\circ} \mathrm{C}$ testing of plastic-packaged silicon chips, aluminum metallization failures due to corrosion started to occur at 750 h of testing. Assuming an exponential humidity dependence of $a=0.12 \% \mathrm{RH}$ and activation energy of 0.75 eV , find the expected time-to-failure at $40 \% \mathrm{RH}$ and $50^{\circ} \mathrm{C}$.

Answer: $\mathrm{TF}=264$ years
7. The corrosion-free time window, for post chemical-mechanical polishing of Cu , was determined to be 3 h when the wafers are stored in $40 \% \mathrm{RH}$ ambient at room temp. How long would the corrosion-free window be if the humidity is lowered to $30 \% \mathrm{RH}$ ? Assume an exponential humidity dependence with $a=$ $0.12 \% \mathrm{RH}$.

# Answer: 10 h 

8. Thermal cycling of plastic-packaged silicon chips produced solder-ball failures after 500 cycles of $-65^{\circ} \mathrm{C} / 150^{\circ} \mathrm{C}$. Assuming that the elastic range is negligibly small and that the temperature cycling exponent for the soft-solder metal is $q=3$, estimate the number of cycles-to-failure for temperature cycling from 0 to $85^{\circ} \mathrm{C}$.

Answer: 8,100 cycles
9. Thermal cycling of plastic-packaged silicon chips produced crack propagation in the silicon substrate and caused a fractured-die failure mechanism after 500 cycles of $-65^{\circ} \mathrm{C} / 150^{\circ} \mathrm{C}$. Assuming that time-zero cracks exist and that the temperature cycling exponent for hard/brittle silicon substrate is $q=6$, estimate the number of cycles-to-failure for temperature cycling from 0 to $85^{\circ} \mathrm{C}$.

Answer: $1.31 \times 10^{5}$ cycles
10. TDDB data was taken for capacitors at $E=10 \mathrm{MV} / \mathrm{cm}$ and a temperature of $105^{\circ} \mathrm{C}$. The following Weibull results were obtained: $t_{63}=200 \mathrm{~s}$ and $\beta=1.4$. Using an E-Model with $\gamma_{@ 105 \mathrm{C}}=4.0 \mathrm{~cm} / \mathrm{MV}$ :
(a) What is the expected time-to-failure, at $10 \mathrm{MV} / \mathrm{cm}$ and $105^{\circ} \mathrm{C}$, for $0.1 \%$ of the capacitors?
(b) What acceleration factor is needed to insure that no more than $0.1 \%$ of the capacitor will fail during 10 years of use at $105^{\circ} \mathrm{C}$ ?(c) What is the maximum allowed operational electric field $E_{\text {op }}$ to ensure that no more than $0.1 \%$ of the capacitors are expected to fail in 10 years of service at $105^{\circ} \mathrm{C}$ ?

Answers: a) $t_{0.1 \%}=1.44 \mathrm{~s}$ b) $\mathrm{AF}=2.19 \times 10^{8} \mathrm{c}$ ) $E_{\mathrm{op}}=5.2 \mathrm{MV} / \mathrm{cm}$
11. TDDB data was taken for capacitors at $E=10 \mathrm{MV} / \mathrm{cm}$ and a temperature of $105^{\circ} \mathrm{C}$. The following Weibull results were obtained: $t_{63}=200 \mathrm{~s}$ and $\beta=1.4$. Using a 1/E-Model with $G_{\text {@105C }}=303 \mathrm{MV} / \mathrm{cm}$ :
(a) What is the expected time-to-failure, at $10 \mathrm{MV} / \mathrm{cm}$ and $105^{\circ} \mathrm{C}$, for $0.1 \%$ of the capacitors?
(b) What acceleration factor is needed to insure that no more than $0.1 \%$ of the capacitor will fail during 10 years of use at $105^{\circ} \mathrm{C}$ ?
(c) What is the maximum allowed operational electric field $E_{\text {op }}$ to ensure that no more than $0.1 \%$ cap-fails will occur during 10 years at $105^{\circ} \mathrm{C}$ ?

Answers: a) $\mathrm{t}_{0.1 \%}=1.44 \mathrm{~s}$ b) $\mathrm{AF}=2.19 \times 10^{8} \mathrm{c}$ ) $E_{\mathrm{op}}=6.12 \mathrm{MV} / \mathrm{cm}$
12. Linear ramp-to-breakdown testing at $105^{\circ} \mathrm{C}$ of a random collection of capacitors with a ramp rate of $1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$ produced a breakdown distribution which could be described by a Weibull distribution with $\left(E_{\mathrm{bd}}\right)_{63}=12 \mathrm{MV} / \mathrm{cm}$ and a Weibull slope of $\beta=15.0$. Using an E-Model, with $\gamma_{\text {@105C }}=4.0 \mathrm{~cm} / \mathrm{MV}$, what is the expected fraction of capacitors that will fail in 10 years at $4 \mathrm{MV} / \mathrm{cm}$ at $105^{\circ} \mathrm{C}$.

Answer: $1.8 \%$
13. Na ions are present in a group of MOSFET devices. If the devices start to fail in 400 h at $125^{\circ} \mathrm{C}$ and 5.0 V , what is the expected time-to-failure at $85^{\circ} \mathrm{C}$ and 3.3 V? Assume activation energy of 1.0 eV .

# Answer: 1.8 years 

14. Minimum channel length MOSFETS were HCI tested. The maximum substrate current was found to approximately double for each 0.5 V increase in operational voltage. If the time-to-failure was 1 h at 6.5 V , what is the expected time-to-failure at 4.0 V ? Assume a time-to-failure power-law exponent of $n=3$ for the substrate current.

Answer: 3.7 years
15. MOSFETS were randomly selected and NBTI stress tested. The electric field in the gate oxide during stress was $E_{\text {stress }}=8 \mathrm{MV} / \mathrm{cm}$ and the stress temperature was $T_{\text {stress }}=150^{\circ} \mathrm{C}$. If the devices started to fail in 1 h under NBTI stress, what would the time-to-failure be at $E_{\mathrm{op}}=5 \mathrm{MV} / \mathrm{cm}$ and $T_{\mathrm{op}}=105^{\circ} \mathrm{C}$ ? Assume an exponential model with $c_{\mathrm{NBTI}}=3.2 \mathrm{~cm} / \mathrm{MV}$ and activation energy $Q_{\mathrm{NBTI}}=$ 0.6 eV .

Answer: 12 years# Bibliography 

## Corrosion

Dunn, C. and J. McPherson: Recent Observations on VLSI Bond Pad Corrosion Kinetics, J. Electrochem. Soc., 661 (1988).

Flood, J.: Reliability Aspects of Plastic Encapsulated Integrated Circuits, IEEE International Reliability Physics Symposium Proceedings, 95 (1972).
Gunn, J., R. Camenga and S. Malik: Rapid Assessment of the Humidity Dependence of IC Failure Modes by Use of Hast, IEEE International Reliability Physics Symposium Proceedings, 66 (1983).
Koelmans, H.: Metallization Corrosion in Silicon Devices by Moisture-Induced Electrolysis, IEEE International Reliability Physics Symposium Proceedings, 168 (1974).
Lawrence, D.. and J. McPherson: Corrosion Susceptibility of Al-Cu and Al-Cu-Si Films, J. Electrochem. Soc., Vol. 137, 3879 (1990).

McPherson, J.: VLSI Corrosion Models: A Comparison of Acceleration Factors, Proceedings of Third Intern. Symp. on Corrosion and Reliability of Electronic Materials and Devices, Electrochem. Soc., Vol. 94-29, 270 (1994).
Paulson, W. and R. Kirk: The Effects of Phosphorus-Doped Passivation Glass on the Corrosion of Aluminum, IEEE International Reliability Physics Symposium Proceedings, 172 (1972).
Peck, D.: The Design and Evaluation of Reliable Plastic-Encapsulated Semiconductor Devices, IEEE International Reliability Physics Symposium Proceedings, 81 (1970).
Peck, D.: A Comprehensive Model for Humidity Testing Correlation, IEEE International Reliability Physics Symposium Proceedings, 44 (1986).
Schnable, A. and R. Keen: Failure Mechanisms in Large-Scale Integrated Circuits, IEEE International Reliability Physics Symposium Proceedings, 170 (1969).

## Electromigration (EM)

Black, J.: A Brief Survey of Some Recent Electromigration Results, IEEE Trans. Electron Dev., ED-16, 338 (1969).
Blech, I. and H. Sello: The Failure of Thin Aluminum Current-Carrying Strips on Oxidized Silicon, Physics of Failures in Electronics Vol. 5, USAF-RADC Series, 496 (1966).
d'Heurle, F. and P. Ho, Electromigration in Thin Films. In: Thin Films: Interdiffusion and Reactions, John Wiley \& Sons, 243 (1978).
Filippi, R., G. Biery and R. Wachnik: The Electromigration Short-Length Effect in Ti-AlCu-Ti Metallization with Tungsten Plugs, J. Appl. Phys., Vol. 78, 3756 (1995).
Graas, C., H. Le, J. McPherson and R. Havemann, Electromigration Reliability Improvements of W-Plug vias by Titanium Layering, IEEE International Reliability Physics Symposium Proceedings, 173 (1994).
Hau-Riege, S.: Probabilistic Immortality of Cu Damascene Interconnects, Journal of Applied Physics, 91(4), 2014 (2002).
Hau-Riege, C. A. P. Marathe, and V. Pham: The Effect of Low-k ILD on the Electromigration Reliability of Cu Interconnects with Different Line Lengths, 41st Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 173 (2003).
Hu, C. et al.: Scaling Effect on Electromigration in On-Chip Cu Wiring, IEEE International Interconnect Conference, 267 (1999).
Hu, C., et al.: Effects of Overlayers on Electromigration Reliability Improvement for Cu/Low K Interconnects, 42th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 222 (2004).Huntington, H. and A. Grone: Current Induced Marker Motion in Gold Wires, J. Phys. Chem. Solids, VOL. 20, 76 (1961).
Hussein, M. and J. He: Materials Impact on Interconnect Process Technology and Reliability, IEEE Transactions on Semiconductor Manufacturing, 18(01), 69 (2005).
Lane, M., E. Liniger, and J. R. Lloyd: Relationship between interfacial adhesion and electromigration in Cu metallization, J. Appl. Phys., 93(3), 1417 (2003).
Lee, K., X. Lu, E. T. Ogawa, H. Matsuhashi, and P. S. Ho: Electromigration Study of Cu/low $k$ Dual-damascene Interconnects, 40th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 322 (2002).
Lloyd, J.: Electromigration in Thin Film Conductors, Semicond. Sci. Technol. 12, 1177 (1997). Maiz, J.: Characterization of Electromigration under Bidirectional and Pulsed Unidirectional Currents, IEEE International Reliability Physics Symposium Proceedings, 220 (1989).
Martin, C. and J. McPherson: Via Electromigration Performance of Ti/W/Al-Cu(2\%) Multilayered Metallization, VLSI Multilevel Interconnect Conference Proceedings, 168 (1989).
McPherson, J., H. Le and C. Graas: Reliability Challenges for Deep Submicron Interconnects, Microelectronics Reliability, Vol. 37, 1469 (1997).
Michael, N., C. Kim, P. Gillespie, and R. Augur: Mechanism of Reliability Failure in Cu Interconnects with Ultra-Low Materials, Applied Physics Letters, 83(10), 1959 (2003).
Oates, A.: Electromigration Failure Distribution of Contacts and Vias as a Function of Stress Conditions in Submicron IC Metallizations, IEEE International Reliability Physics Symposium Proceedings, 164 (1996).
Ogawa, E., et al.: Statistics of Electromigration Early Failures in Cu/Oxide Dual-Damascene Interconnects, 39th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 341(2001).
Ogawa, E., K.-D. Lee, V. A. Blaschke, and P. S. Ho: Electromigration Reliability Issues in DualDamascene Cu Interconnections, IEEE Transactions on Reliability, 51(4), 403 (2002a).
Ondrusek, J., C. Dunn and J. McPherson: Kinetics of Contact Wearout for Silicided(TiSi2) and Nonsilicided Contacts, IEEE International Reliability Physics Symposium Proceedings, 154 (1987).
Park, Y. Park, K.-D. Lee and W. R. Hunter, 43th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 18 (2005).
Shatzkes, M. and J. R. Lloyd: A Model for Conductor Failure Considering Concurrently with Electromigration Resulting in a Current Exponent of 2, J. Appl. Physics, Vol. 59, 3890 (1986).
Steenwyk, S. and E. Kankowski: Electromigration in Aluminum to Ta-Silicide Contacts, IEEE International Reliability Physics Symposium Proceedings, 30 (1986).
Ting, L., J. May, W. Hunter and J. McPherson: AC Electromigration Characterization and Modeling of Multilayered Interconnects, IEEE International Reliability Physics Symposium Proceedings, 311 (1993).
Vaidya, S. et al.: Electromigration Induced Shallow Junction Leakage with Al/Poly-Si Metallization, J. Electrochem. Soc., Vol. 130, 496 (1983).
Vaidya, S., et al.: Shallow Junction Cobalt Silicide Contacts with Enhanced Electromigration Resistance, J. Appl. Phys. Vol. 55, 3514 (1984).

# Hot Carrier Injection (HCI) 

Aur, S., A. Chatterjee and T. Polgreen: Hot Electron Reliability and ESD Latent Damage, IEEE International Reliability Physics Symposium Proceedings, 15 (1988).
Fang, P., J.T. Yue, and D. Wollesen: A Method to Project Hot-Carrier Induced Punch Through Voltage Reduction for Deep Submicron LDD PMOS FETs at Room and Elevated Temperatures, IEEE International Reliability Physics Symposium Proceedings, 131 (1982).LaRosa, G., et al.: NBTI Channel Hot Carrier Efffects in PMOSFETS in Advanced CMOS Technologies, IEEE International Reliability Physics Symposium Proceedings, 282 (1997a).
Liu, Z., et al.: Design Tools for Reliability Analysis, IEEE Design Tools for Reliability Analysis, IEEE Design Automation Conference, pp. 182-185, (2006).
Lu, M., et al.: Hot Carrier Degradation in Novel Strained Si n-MOSFETs, IEEE International Reliability Physics Symposium Proceedings, pp. 18-21, (2004).
Ong, T., P. Ko and C. Hu: Hot-Carrier Current Modeling and Device Degradation in Surface Channel PMOSFET, IEEE Trans. on Electron Devices, ED-37, 1658 (1990).
Snyder, E., D. Cambell, S. Swanson and D. Pierce: Novel Self-Stressing Test Structures for Realistic High-Frequency Reliability Characterization, IEEE International Reliability Physics Symposium Proceedings, 57 (1993).
Takeda, E., R. Izawa, K. Umeda and R. Nagai: AC Hot-Carrier Effects in Scaled MOS Devices, IEEE International Reliability Physics Symposium Proceedings, 118 (1991).
Wang, W., et al.: An Integrated Modeling Paradigm of Circuit Reliability for 65 nm CMOS Technology, IEEE Custom Integrated Circuits Conference, pp. 511-514 (2007).
Wang-Ratkovic, J. et al.: New Understanding of LDD CMOS Hot-Carrier Degradation and Device Lifetime at Cryogenic Temperatures, IEEE International Reliability Physics Symposium Proceedings, 312 (1997).
Yue J.: Reliability. In: ULSI Technology, McGraw-Hill, 657 (1996a).

# Mobile-Ions/Surface-Inversion 

Hefley, P. and J. McPherson: The Impact of an External Sodium diffusion Source on the Reliability of MOS Circuitry, IEEE International Reliability Physics Symposium Proceedings, 167 (1988).
Schnable, A.: Failure Mechanisms in Microelectronic Devices, Microelectronics and Reliability, (1988).

Snow, E., A.S. Grove, B.E. Deal, and C.T. Sah: Ion Transport Phenomenon in Insulating Films, J. Appl. Phys. Vol 36, 1664 (1965).

Snow, E. and B.E. Deal: Polarization Phenomena and Other Properties of Phosphosilicate Glass Films on Silicon, J. Electrochem. Soc., Vol 113, 263 (1966).
Stuart, D.: Calculations of Activation Energy of Ionic Conductivity in Silica Glass by Classical Methods, Journal of the American Ceramic Society, 573 (1954).

## Negative-Bias Temperature Instability (NBTI)

Abadeer, W. and W. Ells: Behavior of NBTI Under AC Dynamical Circuit Conditions, IEEE International Reliability Physics Symp., pp. 17-22, (2003).
Alam, A., et al.: A Comprehensive Model of PMOS Negative Bias Temperature Degradation, Microelectronics Reliability, pp. 71-81 (2005).
Chakravarthi, S. et al.: A Comprehensive Framework for Predictive Modeling of Negative Bias Temperature Instability, IEEE International Reliability Physics Symp. pp. 273-282, (2004).
Chen, G., et al.: Dynamic NBTI of PMOS Transistors and Its Impact on Device Lifetime, IEEE International Reliability Physics Symp. pp. 196-202, (2003).
Huard V. and M. Denais: Hole Trapping Effect on Methodology for DC and AC Negative Bias Temperature Instability Measurements in pMOS transistors, IEEE International Reliability Physics Symp. pp. 40-45 (2003).Kimizuka, N., et al.,: The Impact of Bias Temperature Instability for Direct-Tunneling in Ultrathin Gate Oxide on MOSFET Scaling, VLSI Symp. On Tech., pp. 73-74, (1999).
Krishnan, A., et al.: NBTI Impact on Transistor and Circuit: Models, Mechanisms and Scaling Effects, IEEE-IEDM, pp. 349-352, (2003).
Larosa, G., et al.,: NBTI-Channel Hot Carrier Effects in Advanced Sub-Micron PFET Technologies, IEEE Interational Reliability Physics Symp. Proceedings, pp. 282-286 (1997b).
Mahaptra, S., et al.: Negative bias Temperature Instability in CMOS Devices, Microelectronics Reliability, pp. 114-121 (2005).
Ogawa, S. and N. Shiono: Generalized Diffusion-reaction Model for the Low-Field Chaarge Buildup Instability at the Si-SiO2 Interface, Physical Rev. B, p. 4218 (1995).
Rangan, S., et al.: Universal Recovery Behavior of Negative Bias Temperature Instability, IEEEIEDM, pp. 341-344.(2003).
Reddy, V., et al.: Impact of Negative Bias Temperature Instability on Digital Circuit Reliability, pp. 248-254, (2002).
Schlunder, C. et al.: Evaluation of MOSFET Reliability in Analog Applications, IEEE, International Reliability Physics Symposium, pp. 5-10, (2003).
Stathis, J. and S. Zafar: The Negative Bias Temperature Instability of MOS Devices: A Review, Microelectronics Reliability, pp. 270-286 (2006).

# Stress Migration/Stress-Induced Voiding 

Edelstein, D., et al.: Full Copper Wiring in a Sub-0.25 $\mu \mathrm{m}$ CMOS ULSI Technology, IEEE International Electron Devices Meeting Technical Digest, 773 (1997).
Groothuis, S. and W. Schroen: Stress Related Failures Causing Open Metallization, IEEE International Reliability Physics Symposium Proceedings, 1 (1987).
Harper, J., et al.: Mechanisms for Microstructure Evolution in Electroplated Copper Thin Films Near Room Temperature, Journal of Applied Physics, 86(5), 2516 (1999).
Klema, J., R. Pyle and E. Domangue: Reliability Implications of Nitrogen Contaminated during Deposition of Sputtered Aluminum/Silicon Metal Films, IEEE International Reliability Physics Symposium Proceedings, 1 (1984).
McPherson, J. and C. Dunn: A Model for Stress-Induced Metal Notching and Voiding in VLSI Al-Si Metallization, J. Vac. Sci. Technology B, 1321 (1987).
McPherson, J.: Accelerated Testing. In: Electronic Materials Handbook, Volume 1 Packaging, ASM International Publishing, 887 (1989).
Ogawa, E., J. W. McPherson, J. A. Rosal, K. J. Dickerson, T.-C. Chiu, L. Y. Tsung, M. K. Jain, T. D. Bonifield, J. C. Ondrusek, and W. R. McKee: Stress-Induced Voiding Under Vias Connected To Wide Cu Metal Leads, 40th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 312 (2002b).
Paik, J., J.-K. Jung and Y.-C. Joo: The Dielectric Material Dependence of Stress and Stress Relaxation on the Mechanism of Stress-Voiding of Cu Interconnects, 43th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 195 (2005).
Von Glasow, A., A. H. Fischer, M. Hierlemann, S. Penka, and F. Ungar: Geometrical Aspects of Stress-Induced Voiding in Copper Interconnects, Advanced Metallization Conference Proceedings (AMC), 161 (2002).
Yoshida, K., T. Fujimaki, K. Miyamoto, T. Honma, H. Kaneko, H. Nakazawa, and M. Morita: Stress-Induced Voiding Phenomena for an actual CMOS LSI Interconnects, IEEE International Electron Devices Meeting Technical Digest, 753 (2002).
Yue, J., W. Fusten and R. Taylor: Stress Induced Voids in Aluminum Interconnects During IC Processing, IEEE International Reliability Physics Symposium Proceedings, 126 (1985).
Yue, J.: Reliability. In: ULSI Technology, McGraw-Hill, 674 (1996b).# Temperature-Cycling/Fatigue 

Blish, R.: Temperature Cycling and Thermal Shock Failure Rate Modeling, IEEE International Reliability Physics Symposium Proceedings, 110 (1997).
Caruso, H. and A. Dasgupta: A Fundamental Overview of Accelerated-Testing Analytical Models, Proceedings of Annual Rel. and Maintainability Symposium, 389 (1998).
Coffin, L., Met. Eng. Q., Vol 3, 15 (1963).
Dieter, G.: Mechanical Metallurgy, McGraw-Hill, 467 (1976).
Dunn, C. and J. McPherson: Temperature Cycling Acceleration Factors in VLSI Applications, IEEE International Reliability Physics Symposium Proceedings, 252 (1990).
Manson, S.: Thermal Stress and Low-Cycle Fatigue, McGraw-Hill Book Co., New York, (1966).

## Time-Dependent Dielectric Breakdown (TDDB)

Anolick, E. and G. Nelson: Low-Field Time-Dependent Dielectric Integrity, IEEE International Reliability Physics Symposium Proceedings, 8 (1979).
Berman, A.: Time Zero Dielectric Reliability Test by a Ramp Method, IEEE International Reliability Physics Symposium Proceedings, 204 (1981).
Boyko, K. and D. Gerlach: Time Dependent Dielectric Breakdown of 210A Oxides, IEEE International Reliability Physics Symposium Proceedings, 1 (1989).
Charparala, P., et al.: Electric Field Dependent Dielectric Breakdown of Intrinsic SiO2 Films Under Dynamic Stress, IEEE International Reliability Physics Symposium Proceedings, 61 (1996).
Chen, I., S. Holland and C. Hu: A Quantitative Physical Model for Time-dependent Breakdown, IEEE International Reliability Physics Symposium Proceedings, 24 (1985).
Cheung, K.: A Physics-Based, Unified Gate-Oxide Breakdown Model, Technical Digest of Papers International Electron Devices Meeting, 719 (1999).
Crook, D.: Method of Determining Reliability Screens for Time-Dependent Dielectric Breakdown, IEEE International Reliability Physics Symposium Proceedings, 1 (1979).
Degraeve, R., et al.: New Insights in the Relation Between Electron Trap Generation and the Statistical Properties of Oxide Breakdown, IEEE Trans. Electron Devices 45, 904 (1998).
DiMaria, D. and J. Stasiak: Trap Creation in Silicon Dioxide Produced by hot electrons, J. Appl. Physics, Vol 65, 2342 (1989).
DiMaria, D., E. Cartier and D. Arnold: Impact ionization, trap creation, degradation, and breakdown in silicon dioxide films on silicon, J. Appl. Physics, Vol 73, 3367 (1993).
Eissa, M., D. A. Ramappa, E. Ogawa, N. Doke, E. M. Zielinski, C. L. Borst, G. Shinn, and A. J. McKerrow: Post-Copper CMP Cleans Challenges for 90 nm Technology, Advanced Metallization Conference Proceedings (AMC), 559 (2004).
Hu, C. and Q. Lu: A Unified Gate Oxide Reliability Model, IEEE International Reliability Physics Symposium Proceedings, 47 (1999).
Haase, G., E. T. Ogawa and J. W. McPherson: Breakdown Characteristics of Interconnect Dielectrics, 43th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 466 (2005).
Kimura, M.: Oxide Breakdown Mechanism and Quantum Physical Chemistry for Time-Dependent Dielectric Breakdown, IEEE International Reliability Physics Symposium Proceedings, 190 (1997).
Lee, J., I. Chen and C. Hu: Statistical Modeling of Silicon Dioxide Reliability, IEEE International Reliability Physics Symposium Proceedings, 131 (1988).
McPherson, J. and D. Baglee: Acceleration factors for Thin Gate Oxide Stressing, IEEE International Reliability Physics Symposium Proceedings, 1 (1985).McPherson, J. and H. Mogul: Underlying Physics of the Thermochemical E-Model in Describing Low-Field Time-Dependent Dielectric Breakdown in SiO2 Thin Films, J. Appl. Phys., Vol. 84, 1513 (1998).
McPherson, J., R. Khamankar and A. Shanware: Complementary Model for Intrinsic TimeDependent Dielectric Breakdown in SiO2 Dielectrics, J. Appl. Physics, Vol. 88, 5351 (2000).
McPherson, J.: Trends in the Ultimate Breakdown Strength of High Dielectric-Constant Materials, IEEE Trans. On Elect. Devs., Vol. 50, 1771 (2003).
McPherson, J.: Determination of the Nature of Molecular bonding in Silica from Time-Dependent Dielectric Breakdown Data, J. Appl. Physics, Vol. 95, 8101 (2004).
Moazzami, R., J. Lee and C. Hu: Temperature Acceleration of Time-Dependent Dielectric Breakdown, IEEE Trans. Elect. Devices, Vol. 36, 2462 (1989).
Nicollian, P.: Experimental Evidence for Voltage Driven Breakdown Models in Ultra-Thin Gate Oxides, IEEE International Reliability Physics Symposium, 47 (1999).
Noguchi, J., N. Miura, M. Kubo, T. Tamaru, H. Yamaguchi, N. Hamada, K. Makabe, R. Tsuneda and K. Takeda: Cu-Ion-Migration Phenomena and its Influence on TDDB Lifetime in Cu Metallization, 41st Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 287 (2003).
Ogawa, E., J. Kim and J. McPherson: Leakage, Breakdown, and TDDB Characteristics of Porous Low-k Silica-Based Interconnect Dielectrics, IEEE-IRPS Proceedings, 166 (2003a).
Ogawa, E., J. Kim, G. S. Haase, H. C. Mogul, and J. W. McPherson: Leakage, Breakdown, and TDDB Characteristics of Porous Low-K Silica-Based Interconnect Dielectrics, 41st Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 166 (2003b).
Pompl, T., et al.: Change in Acceleration Behavior of Time-Dependent Dielectric Breakdown by the BEOL Process: Indications for Hydrogen Induced Transition in Dominant Degradation Mechanism, IEEE International Reliability Physics Symposium, 388 (2005).
Schuegraph, K. and C. Hu: Hole Injection Oxide Breakdown Model for Very Low Voltage Lifetime Extrapolations, IEEE International Reliability Physics Symposium Proceedings, 7 (1993).
Suehle, J., et al.: Field and Temperature Acceleration of Time-Dependent Dielectric Breakdown in Intrinsic Thin SiO2, IEEE International Reliability Physics Symposium Proceedings, 120 (1994).
Suehle, J. and P. Chaparala: Low Electric Field Breakdown of Thin SiO2 Films Under Static and Dynamic Stress, IEEE Trans. Elect. Devices, 801 (1997).
Sune, J., D. Jimenez, and E. Miranda: Breakdown Modes and Breakdown Statistics of Ultrathin SiO2 Gate Oxides, J. High Speed Electronics and Systems, 11, 789 (2001).
Stathis, J and D. DiMaria: Reliability Projection for Ultra-Thin Oxides at Low Voltage, Technical Digest of Papers International Electron Devices Meeting, 167 (1998).
Swartz, G.: Gate Oxide Integrity of NMOS Transistor Arrays, IEEE Trans. on Electron Devices, Vol. ED-33, 1826 (1986).
Tsu, R., J. W. McPherson, and W. R. McKee: Leakage and Breakdown Reliability Issues Associated with Low-k Dielectrics in a Dual-Damascene Cu Process, 38th Annual IEEE International Reliability Physics Symposium Proceedings (IRPS), 348 (2000).
Wu, E. et al.: Experimental Evidence of TBD Power-Law for Voltage Dependence of Oxide Breakdown in Ultrathin Gate Oxides, IEEE Trans. On Electron Devices, Vol. 49, 2244 (2002a).
Wu, E., et al.: Polarity-Dependent Oxide Breakdown of NFET Devices for Ultra-Thin Gate Oxide, IEEE International Reliability Physics Symposium, 60 (2002b).# Chapter 13 <br> Time-to-Failure Models for Selected Failure Mechanisms in Mechanical Engineering 

The mechanical properties of materials are related to the fundamental bonding strengths of the constituent atoms in the solid and any bonding defects which might form. A molecular model is presented so that primary bond formation mechanisms (ionic, covalent, and metallic) can be better understood. How these bonds form and respond to mechanical stress/loading is very important for engineering applications. A discussion of elasticity, plasticity and bond breakage is presented. The theoretical strengths of most molecular bonds in a crystal are seldom realized because of crystalline defects limiting the ultimate strength of the materials. Important crystalline defects such as vacancies, dislocations, and grain boundaries are discussed. These crystalline defects can play critically important roles as time-tofailure models are developed for: creep, fatigue, crack propagation, thermal expansion mismatch, corrosion and stress-corrosion cracking.

## 1 Molecular Bonding in Materials

As emphasized in earlier chapters, mechanical device failures result from: materials degradation (generally causing a shift in some critical device parameter) and eventual device failure. Since the material's properties are ultimately related to the molecular bonding in the material and any bonding defects which might form, it is important to have a fundamental understanding of this bonding.

Figure 13.1 illustrates the bonding of two atoms. As the atoms are brought closer together (from a great distance away), an attractive potential develops tending to pull the atoms closer together. This attractive potential develops because of the transfer or sharing of the valence electrons of the interacting atoms. At very small distances $\left(r<r_{0}\right)$, a strong repulsive potential develops between the two atoms

Fig. 13.1 Molecular bonding equilibrium develops due to the competition of the attractive and repulsive potential terms. Equilibrium bonding distance is $r=r_{0}$. The bonding energy is $-\phi_{\mathrm{BE}}$
because of atom-1 core electrons interacting with atom-2 core electrons due to the Pauli Exclusion Principle. ${ }^{1}$

The bonding potential in Fig. 13.1 is often approximated by using a Mie (or MieGrüneisen) Potential $\phi(\mathrm{r})$ :

$$
\phi(r)=\frac{A}{r^{m}}-\frac{B}{r^{n}}(m>n)
$$

The parameters $A$ and $B$ can be determined from equilibrium conditions at $\mathrm{r}=\mathrm{r}_{0}$ where the bonding energy is $-\phi_{\mathrm{BE}}$ and the slope of the potential is zero:

$$
\phi\left(r=r_{0}\right)=-\phi_{\mathrm{BE}}
$$

and

$$
\left(\frac{\partial \phi}{\partial r}\right)_{r=r_{0}}=0
$$

Thus, Eq. (13.1) becomes:

$$
\phi(r)=\phi_{\mathrm{BE}}\left(\frac{\mathrm{mn}}{m-n}\right)\left[\frac{1}{m}\left(\frac{r_{0}}{r}\right)^{m}-\frac{1}{n}\left(\frac{r_{0}}{r}\right)^{n}\right]
$$

[^0]
[^0]:    ${ }^{1}$ Classical description is-two bodies cannot occupy the same space.

Fig. 13.2 Ionic character of bonds is shown using Pauling electronegativity. Bonds with $\mathrm{f}^{*}$ values of greater than 0.5 are considered to be strongly polar

The repulsive exponent $m$ is normally obtained from compressibility studies and is found to be generally in the range $m=8-12$. Some often used forms of this potential are: the Born-Landé potential $(m=9, n=1)$ used for ionic bonding (transferring of valence electrons); the Harrison potential $(m=9, n=2)$ used for covalent bonding (sharing of valence electrons); and the Lenard-Jones potential ( $m=12, n=6$ ) used for dipolar bonding. Even for metallic bonding (sea of conduction electrons minimizing the repulsive nature of the host metal ions), the potential shown in Fig. 13.1 can still be useful. The Pauling classification of ionic character of bonds is shown in Fig. 13.2.

Normally, any bond with an ionic character of $f^{*}=0.6 \pm 0.1$ is considered to be strongly ionic/polar. Ionic bonds are of relatively longer range and are non-directional (no preferred direction). The valence electrons are transferred from an atom of low electronegativity to another atom of higher electronegativity. The atoms in a strongly ionic solid generally take a close-pack arrangement depending on the ionic radii of the bonding elements involved. Since ionic bonding is of longer range, the total bonding potential is due to nearest neighbors and beyond. The impact of the extended ionic bonding potential is often accounted for by the use of the Madelung constant ${ }^{2}$ which comes from the summation of the contributions to the potential from both near and far neighbors.

Covalent bonds are generally highly directional because of quantum mechanical restrictions on the bonding to only along preferred directions. Covalent bonds are typically of shorter range (more localized). Shown in Fig. 13.3 is the longer-range

[^0]
[^0]:    ${ }^{2}$ In order that ionic contributions are comprehended from both near and far, the potential for anionpair is often written as: $\varphi(r)=-\alpha e^{2} / r$, where $\alpha$ is the Madelung constant. In cubic crystalline structures, $\alpha=1$ to 2 .

Fig. 13.3 The bonding potential $(9, n)$ tends to show a more localized bonding nature when the value of $n$ increases. Generally, $n=1$ is used for ionic bonds, $n=2$ (or greater) for covalent bonds and $n=6$ is used for dipolar bonding
nature of the ionic bond $[(9,1)$ potential $]$ versus the more covalent-type bonds $[(9,2)$ and $(9,3)$ type bonds]. Covalent bonding generally leads to very hard and non-ductile materials such as diamond. Also, important semiconductors (silicon and germanium) are due to covalent bonds. Normally, these materials have higher modulus $E$ and tend to be hard and can be brittle.

Metallic bonds (due to the relatively free-moving conduction electrons in a host metal-ion matrix) are less dependent on the exact positions of the host lattice metal ions. This type of bonding produces the ductile and malleable properties of metals. Large material deformation (yielding) is possible before material cracking or rupture occurs.

Secondary bonds (dipolar and hydrogen bonds) are generally much weaker than the primary bonds (ionic, covalent, and metallic). Since the secondary bonds are relatively weak, solid materials formed using these secondary bonds exclusively are characterized by relatively low melting points and relatively poor mechanical properties.

The bond energy $-\phi_{\mathrm{BE}}$ is a critically important parameter because it represents the strength/stability of the bond. Very strong bonds can have values of bond energy of the order of several electron volts ( eV ) while very weak bonds generally have bonding energies of less than 1 eV . Shown in Table 13.1 are the single-bond energies for a few selected molecules. In this table, $U^{(e)}$ represents the electronic/ covalent component to the bonding energy, $U^{(i)}$ represents the ionic component, and $U^{(t)}$ represents the total bonding energy. In general, the stronger bonds have more ionic character and the bond energy can be several eV . The covalent bond energy isTable 13.1 Selected single-bond energies (Pauling approach)

| Bond | Electronegativities <br> $\left(X_{A}-X_{B}\right)$ | $U^{(e)}(\mathrm{eV})$ | $U^{(i)}(\mathrm{eV})$ | $U^{(i)}(\mathrm{eV})$ | Ionic \% of total bond <br> energy (\%) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| O-O | $3.5-3.5$ | 1.4 | 0.0 | 1.4 | 0 |
| F-F | $4.0-4.0$ | 1.6 | 0.0 | 1.6 | 0 |
| N-N | $3.0-3.0$ | 1.7 | 0.0 | 1.7 | 0 |
| Cl-Cl | $3.0-3.0$ | 2.5 | 0.0 | 2.5 | 0 |
| H-H | $2.1-2.1$ | 4.5 | 0.0 | 4.5 | 0 |
| Si-Si | $1.8-1.8$ | 1.8 | 0.0 | 1.8 | 0 |
| H-Si | $2.1-1.8$ | 2.9 | 0.1 | 3.0 | 3 |
| N-Si | $3.0-1.8$ | 1.8 | 1.9 | 3.7 | 51 |
| Cl-Si | $3.0-1.8$ | 2.1 | 1.9 | 4.0 | 48 |
| O-H | $3.5-2.1$ | 2.5 | 2.6 | 5.1 | 51 |
| O-Si | $3.5-1.8$ | 1.6 | 3.8 | 5.4 | 70 |
| F-Si | $4.0-1.8$ | 1.7 | 6.3 | 8.0 | 79 |

somewhat less, usually around a few eV . Dipolar and hydrogen bonding can result in relatively weaker bond energies (generally less than 1 eV ). These bonds are relatively weak and that is the reason why water (dependent on secondary bonding) is a solid only below $0^{\circ} \mathrm{C}$ and vaporizes easily at $100^{\circ} \mathrm{C}$.

# 2 Origin of Mechanical Stresses in Materials 

Let us now consider what happens when one applies an external force to the bond (load the bond), as shown in Fig. 13.4. One can see that the bond resists the external force by trying to create an equal, but opposite, internal force.

In static equilibrium, the external forces must be equal and opposite to the internal forces and one can write:

$$
F_{\mathrm{ext}}=-F_{\mathrm{int}}(r)=\left(\frac{\partial \phi}{\partial r}\right)
$$

giving

$$
F_{\mathrm{ext}}=\phi_{\mathrm{BE}}\left(\frac{\mathrm{mn}}{m-n}\right)\left[-\frac{1}{r_{0}}\left(\frac{r_{0}}{r}\right)^{m+1}+\frac{1}{r_{0}}\left(\frac{r_{0}}{r}\right)^{n+1}\right]
$$

The general shape of the curve, for the external force $F_{\text {ext }}$ versus atom separation $r$, is shown in Fig. 13.5.

The curve in Fig. 13.5 is very important because $\mathrm{d} W=F_{\text {ext }} \mathrm{d} r$ represents the incremental amount of work that is done by the external force on the bond (either stretching or compressing the bond). This incremental work serves to increase theFig. 13.4 Bonds are shown in states of compression and tension. External forces $F_{\text {ext }}$ are shown as well as the internal resistive forces $F_{\text {int }}$


Fig. 13.5 External force $F_{\text {ext }}$ versus bonding distance $r$
energy of the bond (making the bond energy more positive) thus making the bond less stable and more susceptible to breakage. From Fig. 13.5, one can see what happens when we stretch or compress the bond beyond its elastic limit. The elastic region (Hooke's Law region) is a region where, once the external force is removed, the material returns back to its original unstressed position (thus no permanent changes to the bonding or to the materials).Fig. 13.6 In the region of Hooke's Law validity (elastic behavior), the force acting on the interacting atoms is directly proportional to the displacement of the atoms from their equilibrium positions. Hooke's law leads to a simple harmonic potential energy of the form: $\phi(x)=(1 / 2) \kappa x^{2}$, where $x=r-r_{0}$


# 3 Elastic Behavior of Materials 

The elastic region for the bond can be characterized by a spring with spring constant (or stiffness constant) $\kappa$, as shown in Fig. 13.6. The value of $\kappa$ can be determined from the molecular potential:

$$
\kappa=\left(\frac{\partial^{2} \phi}{\partial r^{2}}\right)_{r=r_{0}}=\phi_{\mathrm{BE}}\left(\frac{\mathrm{mn}}{r_{0}^{2}}\right)
$$

The elastic behavior leads to a quadratic/harmonic potential energy of the form:

$$
\phi(x)=-\int_{0}^{x} \vec{F} \cdot \mathrm{~d} \vec{x}=\kappa \int_{0}^{x} x \mathrm{~d} x=\frac{1}{2} \kappa x^{2}
$$

Note that the elastic energy goes as the square of the displacement (for small displacement) of the atoms from their equilibrium positions. Since this is a harmonic potential, once the atoms are displaced from their equilibrium positions and suddenly released, the atoms are expected to oscillate about their equilibrium positions until the elastic energy is dissipated. ${ }^{3}$

Let us now go from the microscopic level (atom level) to the macroscopic level (solid level) as shown in Fig. 13.7. From Fig. 13.7, one can see that if the number of such bonds per unit area is $\eta$ then the stress needed to elastically displace the atoms from their equilibrium position is given by:

[^0]
[^0]:    ${ }^{3}$ The classical oscillator will oscillate until all its energy is finally dissipated. The quantum oscillator, however, will dissipate its energy in quantum amounts $(n+1 / 2) \hbar \omega$ until it finally reaches its ground state. In the ground state $(n=0)$, the quantum oscillator will still have zero-point energy oscillation: $(1 / 2) \hbar \omega$.Fig. 13.7 Planar crosssection illustrates the bonding/ springs between nearest neighboring atoms along the length of the solid. Plane-to-plane bonding/ springs are compressed by the applied stress. With $N$ cross-sectional units along the length of the solid, the length $L$ of the solid is simply $L=$ Nr. Only bonding/springs between planes are shown


$$
\sigma=\frac{F_{\text {Total }}}{A}=\frac{\eta \cdot A \cdot\left[\kappa\left(r-r_{0}\right)\right]}{A}=\eta \kappa\left(r-r_{0}\right)
$$

But, since $\eta=1$ bond $/ r_{0}^{2}$, then

$$
\sigma=\frac{\kappa}{r_{0}}\left(\frac{r-r_{0}}{r_{0}}\right)=E \varepsilon
$$

where the modulus $E$ is given by:

$$
E=\frac{\kappa}{r_{0}}=\frac{(m \cdot n) \phi_{\mathrm{BE}}}{r_{0}^{3}}
$$

# Example Problem 1 

Typical primary molecular single-bond energies are $\sim 2 \mathrm{eV}$ and typical equilibrium bond lengths are $\sim 2 \AA$. Estimate Young's modulus for: (a) $(m=9$, $n=1$ ) bonding potential, (b) $(m=9, n=2)$ bonding potential and (c) $(m=$ $9, n=3$ ) bonding potential.

## Solution

Equation (13.11) gives:

$$
E=\frac{(m \cdot n) \phi_{\mathrm{BE}}}{r_{0}^{3}}
$$(a) For $(9,1)$ bonding one obtains:

$$
\begin{aligned}
E=\frac{(9 \cdot 1) 2 \mathrm{eV}}{(2 \AA)^{3}}= & 2.25 \frac{\mathrm{eV}}{(\AA)^{3}} \cdot\left(\frac{1.6 \times 10^{-19} \mathrm{~J}}{1 \mathrm{eV}}\right) \cdot\left(\frac{1 \AA}{10^{-10} \mathrm{~m}}\right)^{3} \\
& \cdot\left(\frac{1 \mathrm{Nm}}{1 \mathrm{~J}}\right) \cdot\left(\frac{1 \mathrm{GPa}}{10^{9} \mathrm{~N} / \mathrm{m}^{2}}\right) \\
= & 360 \mathrm{GPa}
\end{aligned}
$$

This value of modulus is similar to modulus values reported for medium strength steels, silicon nitride, titanium carbide, and tantalum carbide.
(b) For $(9,2)$ bonding one obtains:

$$
E=\frac{(9 \cdot 2) 2 \mathrm{eV}}{(2 \AA)^{3}}=720 \mathrm{GPa}
$$

This value of modulus is similar to very hard materials such as tungsten carbide.
(c) For $(9,3)$ bonding one obtains:

$$
E=\frac{(9 \cdot 3) 2 \mathrm{eV}}{(2 \AA)^{3}}=1,080 \mathrm{GPa}
$$

This is similar to an extremely hard material such as diamond.

The elastic energy density in a macroscopic material can also be determined from the microscopic bonding. The elastic energy density (elastic energy per unit volume) is given by $u_{\text {elastic }}$ :

$$
\begin{aligned}
u_{\text {elastic }} & =\frac{\text { Total Elastic Energy }}{\text { (Volume) }_{0}}=\frac{\eta \cdot A \cdot\left[\frac{1}{2} \kappa\left(r-r_{0}\right)^{2}\right] \cdot N}{\left(N r_{0}\right) \cdot A} \\
& =\frac{1}{2}\left(\kappa \eta r_{0}\right)\left[\frac{N\left(r-r_{0}\right)}{N r_{0}}\right]^{2}=\frac{1}{2}\left(\frac{\kappa}{r_{0}}\right)\left[\frac{\Delta L}{L_{0}}\right]^{2}
\end{aligned}
$$

Therefore, the elastic energy density in a solid material is given by:

$$
u_{\text {elastic }}=\frac{1}{2} E e^{2}
$$# Example Problem 2 

For many materials, the elastic region is fairly small (elastic behavior occurs for strains of about $1 \%$ or less) and the average bond distance is about $2 \stackrel{\circ}{\mathrm{~A}}$. If the material's modulus is 350 GPa :
(a) Find the elastic energy density for a $1 \%$ strain.
(b) Find the elastic energy per atom for a $1 \%$ strain.

## Solution

The elastic energy density is given by:

$$
u_{\text {elastic }}=\frac{1}{2} E \varepsilon^{2}
$$

(a) The elastic energy density becomes:

$$
\begin{aligned}
u_{\text {elastic }} & =\frac{1}{2}(350 \mathrm{GPa})(0.01)^{2}=1.75 \times 10^{-2} \mathrm{GPa}=1.75 \times 10^{7} \frac{\mathrm{~N}}{\mathrm{~m}^{2}} \\
& =1.75 \times 10^{7} \frac{\mathrm{Nm}}{\mathrm{~m}^{3}} \cdot\left(\frac{1 \mathrm{~J}}{1 \mathrm{Nm}}\right)\left(\frac{1 \mathrm{eV}}{1.6 \times 10^{-19} \mathrm{~J}}\right)\left(\frac{1 \mathrm{~m}}{100 \mathrm{~cm}}\right)^{3} \\
& =1.09 \times 10^{20} \frac{\mathrm{eV}}{\mathrm{~cm}^{3}}
\end{aligned}
$$

(b) Since the average bonding distance is $2 \stackrel{\circ}{\mathrm{~A}}$, the atom density becomes:

$$
\frac{1 \mathrm{atom}}{\left(2 \stackrel{\circ}{\mathrm{~A}}\right)^{3}} \cdot\left(\frac{1 \stackrel{\circ}{\mathrm{~A}}}{10^{-8} \mathrm{~cm}}\right)^{3}=1.25 \times 10^{23} \frac{\text { atoms }}{\mathrm{cm}^{3}}
$$

Thus, the elastic energy per atom is:

$$
\begin{aligned}
\frac{\text { elastic energy }}{\text { atom }} & =\frac{u_{\text {elastic }}}{\text { \#atoms/volume }}=\frac{1.09 \times 10^{20} \mathrm{eV} / \mathrm{cm}^{3}}{1.25 \times 10^{23} \mathrm{atom} / \mathrm{cm}^{3}} \\
& =8.72 \times 10^{-4} \mathrm{eV} / \mathrm{atom} \cong 1 \times 10^{-3} \frac{\mathrm{eV}}{\mathrm{atom}}
\end{aligned}
$$

One should note that the elastic energy per atom is much, much smaller than the average single-bond strength ( 2 eV ) per atom.# 4 Inelastic/Plastic Behavior of Materials 

When the bond is placed under the tensile load of an external force $F_{\text {ext }}$, one can see from Fig. 13.5 that the response of the bond to this load is linear only for very small displacements about $r_{0}$. When the displacement $r$ is significantly greater than $r_{0}$, then the bond weakens, as indicated by the reduction in force $F_{\text {ext }}$ needed to produce the next incremental displacement $\mathrm{d} r$. Finally, as $r$ is increased beyond $r_{1}$, the bond can no longer support the large fixed load $F_{\text {ext }}$ and the bond will fail.

The value of $r=r_{1}$, which is an important bond parameter, can be found by using the fact that the external force $F_{\text {ext }}$ is a maximum at $r=r_{1}$.

$$
\left(\frac{\partial F}{\partial r}\right)_{r=r_{1}}=\left(\frac{\partial^{2} \phi}{\partial r^{2}}\right)_{r=r_{1}}=0
$$

This gives

$$
r_{1}=\left(\frac{m+1}{n+1}\right)^{\frac{1}{m-n}} r_{0}
$$

With $r_{1}$ now determined, one can estimate the maximum tensile force that a bond can support.

$$
\left(F_{\text {ext }}\right)_{\max }=-\left(F_{\text {int }}\right)_{r=r_{1}}=\left(\frac{\partial \phi}{\partial r}\right)_{r=r_{1}}
$$

giving,

$$
\left(F_{\text {ext }}\right)_{\max }=\left(\frac{\phi_{\mathrm{BE}}}{r_{0}}\right) \eta(m, n)
$$

where,

$$
\eta(m, n)=\left(\frac{\mathrm{mn}}{m-n}\right)\left[\left(\frac{m+1}{n+1}\right)^{\frac{n+1}{n-m}}-\left(\frac{m+1}{n+1}\right)^{\frac{m+1}{n-m}}\right]
$$

In Table 13.2 are shown two key bonding coefficients/parameters for the Mie-Grüneisen potential. Because of their general usefulness and importance, the $(m=9, n=1)$ and $(m=9, n=2)$ potentials are emphasized. Note that the maximum strain $\left(r_{1}-r_{0}\right) / r_{0}$ that the atoms can support before bond breakage occurs is generally $<30 \%$.Table 13.2 Important bond-modeling parameters (Mie-Grüneisen potential)

| $\eta(\mathrm{m}, \mathrm{n})$ | $m=12$ | $m=11$ | $m=10$ | $m=9$ | $m=8$ | $m=7$ | $m=6$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $n=1$ | 0.66 | 0.64 | 0.62 | 0.60 | 0.58 | 0.55 | 0.52 |
| $n=2$ | 1.19 | 1.15 | 1.12 | 1.07 | 1.03 | 0.97 | 0.91 |
| $n=3$ | 1.64 | 1.59 | 1.53 | 1.47 | 1.39 | 1.31 | 1.22 |
| $n=4$ | 2.03 | 1.96 | 1.89 | 1.80 | 1.71 | 1.60 | 1.48 |
| $n=5$ | 2.38 | 2.29 | 2.20 | 2.09 | 1.98 | 1.85 | 1.70 |
| $n=6$ | 2.69 | 2.59 | 2.47 | 2.35 | 2.21 | 2.06 | - |
| $\mathrm{r}_{1} / \mathrm{r}_{0}$ | $m=12$ | $m=11$ | $m=10$ | $m=9$ | $m=8$ | $m=7$ | $m=6$ |
| $n=1$ | 1.19 | 1.20 | 1.21 | 1.22 | 1.24 | 1.26 | 1.28 |
| $n=2$ | 1.16 | 1.17 | 1.18 | 1.19 | 1.20 | 1.22 | 1.24 |
| $n=3$ | 1.14 | 1.15 | 1.16 | 1.16 | 1.18 | 1.19 | 1.21 |
| $n=4$ | 1.13 | 1.13 | 1.14 | 1.15 | 1.16 | 1.17 | 1.18 |
| $n=5$ | 1.12 | 1.12 | 1.13 | 1.14 | 1.14 | 1.15 | 1.17 |
| $n=6$ | 1.11 | 1.11 | 1.12 | 1.13 | 1.13 | 1.14 | - |

# Example Problem 3 

The bond energy for two elements was determined to be 2.5 eV with an equilibrium bond distance of $1.5 \AA$. Assuming that the bond can be described by a $(m=9, n=1)$ bonding potential,
(a) What is the maximum tensile force that the bond can support?
(b) What is the maximum bond displacement from equilibrium before the bond fails?
(c) If there are approximately $10^{15}$ such bonds per $\mathrm{cm}^{2}$ in a cross-sectional area of the solid, then estimate the maximum tensile stress, in Giga-Pascals (GPa), that this material can withstand before it ruptures.

## Solution

(a) Using Eq. (13.17) and Table 13.2, one obtains:

$$
\left(F_{\mathrm{ext}}\right)_{\max }=\left(\frac{\phi_{\mathrm{BE}}}{r_{0}}\right) \eta(9,1)=\left(\frac{2.5 \mathrm{eV}}{1.5 \AA}\right)(0.60)=1 \mathrm{eV} / \AA
$$

Conversion factors used:

$$
\begin{aligned}
& 1(\mathrm{eV} / \AA)\left(\frac{1.602 \times 10^{-12} \mathrm{erg}}{\mathrm{eV}}\right)\left(\frac{1 \AA}{10^{-8} \mathrm{~cm}}\right)\left(\frac{1 \text { dyne }-\mathrm{cm}}{\mathrm{erg}}\right) \\
& \quad=1.602 \times 10^{-4} \text { dynes. }
\end{aligned}
$$(b) Table 13.2 tells us that the maximum displacement, before bond rupture occurs, is:

$$
\frac{r_{1}}{r_{0}}=1.22 \Rightarrow r_{1}-r_{0}=0.22 r_{0}=0.22\left(1.5 \AA^{0}\right)=0.33 \AA^{0}
$$

Note that this represents a strain of:

$$
\frac{r_{1}-r_{0}}{r_{0}}=22 \%
$$

(c) Since it takes a force of $1.6 \times 10^{-4}$ dynes to rupture a single bond and there are approximately $10^{15}$ such bonds per $\mathrm{cm}^{2}$-then it represents a stress of:

$$
\begin{aligned}
(\text { stress })_{\max } & =\frac{\left(F_{\text {ext }}\right)_{\max }}{b o n d}\left(\frac{10^{15} \text { bonds }}{\mathrm{cm}^{2}}\right)=\left(\frac{1.6 \times 10^{-4} \text { dynes }}{\text { bond }}\right)\left(\frac{10^{15} \text { bonds }}{\mathrm{cm}^{2}}\right) \\
& =1.6 \times 10^{11} \frac{\text { dynes }}{\mathrm{cm}^{2}}
\end{aligned}
$$

Conversion to GPa becomes:

$$
1.6 \times 10^{11} \frac{\text { dynes }}{\mathrm{cm}^{2}}\left(\frac{0.1 \mathrm{~N} / \mathrm{m}^{2}}{1 \text { dyne } / \mathrm{cm}^{2}}\right)\left(\frac{1 \mathrm{~Pa}}{1 \mathrm{~N} / \mathrm{m}^{2}}\right)=1.6 \times 10^{10} \mathrm{~Pa}=16 \mathrm{GPa}
$$

A tensile strength $\sigma_{\mathrm{TS}}=16 \mathrm{GPa}$, calculated using our atomistic model, is significantly higher than the typical $\sigma_{\mathrm{TS}}=1-2 \mathrm{GPa}$ observed during testing of high strength steels. This is because, in real/macroscopic materials, crystalline defects (e.g., vacancies, dislocations, grain boundaries, etc.) exist in polycrystalline materials; these naturally occurring defects can dominate the onset of yielding and the ultimate tensile strength of the material. Dislocations can reduce the ultimate tensile strength of a material by at least one order of magnitude.

# 5 Important Defects Influencing Material Properties 

There are three important metal defects that we will discuss: vacancies, dislocations, and grain boundaries. These defects can dominate the electrical, mechanical, and electrochemical properties of the material. Understanding their roles in the materials can have important reliability implications.Fig. 13.8 A vacancy (vacant lattice site) is shown in an otherwise normal lattice. The vacancy represents a point defect in the lattice and it has an amount of free space $\Omega$ associated with it. Movement of such vacancies, due to stress gradients, and eventual flux divergencies can lead to vacancy-clustering (void growth) and a weakening/ degradation of the material


# 5.1 Vacancies 

A vacancy is illustrated in Fig. 13.8. The vacancy is simply a vacant lattice site in an otherwise normal matrix. As such, it is usually referred to as a point defect. Note that the vacancy might be thought of as a fundamental unit of free space in the normal lattice with a volume size of $\Omega$. As discussed in Chap. 11 (see stress migration), the vacancy can move under the presence of stress gradients. ${ }^{4}$ The force acting on a vacancy can be written as

$$
\vec{F}=-\Omega \vec{\nabla} \sigma
$$

where $\vec{\nabla} \sigma$ is the stress gradient and it is a vector quantity. The negative sign in the previous equation is needed because vacancies tend to move from regions of relative tensile stress to regions of relative compressive stress. By relative, it is meant that vacancies may also move from regions of higher tensile stress to regions of lower tensile stress. Vacancy movement from regions of lower compressive stress to regions of higher compressive stress can also occur. ${ }^{5}$

A divergence in vacancy movement can lead to voiding. The reliability impact of vacancy movement was discussed under stress migration in Chap. 11. One should always keep in mind that atom flow is opposite to the direction of vacancy flow and can be an important stress-relief mechanism.

[^0]
[^0]:    ${ }^{4}$ The stress gradient is given by: $\vec{\nabla} \sigma=\left[\hat{x} \frac{\partial}{\partial x}+\hat{y} \frac{\partial}{\partial y}+\hat{z} \frac{\partial}{\partial z}\right] \sigma(x, y, z)$.
    ${ }^{5}$ Atom movement is opposite to vacancy movement. Atoms tend to move from relative compressive regions to relative tensile regions. Such atom movement tends to reduce both the relative compressive stress and the relative tensile stress. Atom (or vacancy) movement due to stress gradients is a stress-relief mechanism.# Example Problem 4 

Assuming the formation/creation energy for a vacancy is $\left(\Delta H_{0}\right)_{\text {formation }}=1.0$ eV , estimate the vacancy density in a single-crystal piece of Cu at $500^{\circ} \mathrm{C}$.

## Solution

The density of Cu atoms $\rho_{\text {atoms }}$ is given by:

$$
\begin{aligned}
\rho_{\text {atoms }} & =\frac{N_{A} \rho_{\mathrm{Cu}}}{(\text { Atom Mass })_{\mathrm{Cu}}} \\
& =\frac{\left(6.02 \times 10^{23} \text { atoms } / \mathrm{mole}\right)\left(8.6 \mathrm{~g} / \mathrm{cm}^{3}\right)}{63.5 \mathrm{~g} / \mathrm{mo1e}} \\
& =8.2 \times 10^{22} \text { atoms } / \mathrm{cm}^{3}
\end{aligned}
$$

The Boltzmann probability for vacancy formation gives:

$$
\rho_{\text {vacancies }}=\rho_{\text {atoms }} \exp \left[-\frac{\left(\Delta H_{0}\right)_{\text {formation }}}{K_{\mathrm{B}} T}\right]
$$

With $\left(\Delta H_{0}\right)_{\text {formation }}=1.0 \mathrm{eV}$ and $T=500^{\circ} \mathrm{C}=773 \mathrm{~K}$, the vacancy density becomes:

$$
\rho_{\text {vacancies }}=2.5 \times 10^{16} / \mathrm{cm}^{3}
$$

### 5.2 Dislocations

An edge dislocation is illustrated in Fig. 13.9 and it is usually referred to as a linear defect (extending into and out of the plane of atoms shown). The edge dislocation is created when an extra partial plane of atoms is introduced into an otherwise normal lattice. These dislocations can move under shear stress. As the dislocations move under shear stress, they carry mass with them since the dislocation represents an extra partial plane of atoms. Thus, dislocation movement permits mass flow (creep) to occur at much lower values of stress than would be predicted for a defect-free lattice.

For the edge dislocation to move (and thus to carry mass with it), a shearing stress must be developed along a slip plane direction. Slip planes are high specific density ${ }^{6}$ planes such as (111) planes in a face-centered cubic lattice. Dislocations tend to move with relative ease along these slip planes under a shearing-type stress. Even though a tensile stress may be applied to a material, a shearing stress can also develop as illustrated in Fig. 13.10.

The external force shown in Fig. 13.10 serves to put the material in a tensile-stress condition given by: $\sigma=F / A$. However, the external force also serves to produce a

[^0]
[^0]:    ${ }^{6}$ Specific density represents the number of atoms per unit area.Fig. 13.9 Edge dislocation is illustrated. Note that the edge dislocation represents an extra partial plane of atoms (extending into and out of the plane shown) that has been introduced into an otherwise normal lattice


Fig. 13.10 The external force shown produces a tensile stress $\sigma$ in the material but it also produces a shearing stress $\tau$ along the elevated plane as illustrated. The maximum value of the shearing stress occurs for $\theta$ $=45^{\circ}$, giving a maximum shear stress of $\tau_{\max }=\sigma / 2$

shearing force of: $F \sin \theta$ acting over the heavily shaded area $A / \cos \theta$. Thus, the shearing stress $\tau$ becomes:

$$
\tau=\frac{F \sin (\theta)}{A / \cos (\theta)}=\sigma \sin (\theta) \cos (\theta)
$$

It can be easily shown that the maximum shear stress $\tau_{\max }$ occurs for $\theta=45^{\circ}$, thus giving $\tau_{\max }=\sigma / 2$. As the edge dislocation moves along slip planes (illustrated in Fig. 13.11) under a shear stress, it carries this extra partial plane of atoms with it. Thus, dislocation movement under mechanical shear stress can serve as an important mass-flow mechanism-and important mechanism for creep. This leads to creep occurring at much lower values of mechanical stress than would be expected from a perfect lattice. ${ }^{7}$ Dislocations can thus be thought of as carriers of mass, permitting material flow from one region to another and bringing about plastic

[^0]
[^0]:    ${ }^{7}$ Other dislocation types can exist, such as screws dislocations (not discussed here). These can also be important in the mass-flow/creep process.Fig. 13.11 Under tensile loading, the maximum shear stress will develop along planes at $45^{\circ}$ to the tensile stress. Dislocations on a slip plane close to this direction can propagate due to the shearing stress. Dislocation movement results in a mass transfer bringing about plastic deformation within the material (creep)

deformation in the material. Strengthening mechanisms in metals, such as steel, are normally associated with reducing the relative ease of dislocation movement. For example, the addition of relatively small amounts of carbon to iron can serve to pin the dislocation movement and convert relatively weak iron into strong steel.

Thus far, our analysis has been primarily confined to bond stability under tensile stress. What happens to the bond under compression? One can see from Fig. 13.5 that, under compression, the external force required to produce an incremental change in $\mathrm{d} r$ increases dramatically (below $r_{0}$ ) with no apparent bond breakage/ rupture indicated in the figure. While it is generally true that solids are stronger under compressive stress, compressive materials will fail (via cracking, buckling, delamination, blistering, etc.). By putting the polycrystalline material under compression, dislocation movement is again possible, leading to a mass transfer (plastic deformation). One must remember-what gives the bond stability is its negative bond energy $\left(-\phi_{\mathrm{BE}}\right)$. The bond is no longer stable when the work $\Delta W$ done by the external force is greater than $\phi_{\mathrm{BE}}$. Therefore, all bond stability is lost when:

$$
\Delta W=\int_{r_{0}}^{r_{\text {fracture }}} F_{e x t} \mathrm{~d} r \geq \phi_{\mathrm{BE}}
$$

Similar to our use of tensile strength $\sigma_{\mathrm{TS}}$, a crushing strength $\sigma_{\mathrm{CS}}$ can also be determined by loading the material under compression. For metals (or any material which can show plastic deformation) the tensile strength and crushing strength are roughly the same. However, for brittle materials such as ceramics, the crushing strength may be as much as $15 \times$ greater than the tensile strength. This is because the failure mechanism is quite different in ceramic materials under tension versus compression. Whereas a single crack can dominate the failure mechanism (rapid crack propagation) under tension, numerous cracks tend to develop under compression and seem to mitigate the erratic/rapid propagation with a single crack. Whereas cracks tend to propagate perpendicular to the tensile stress axis, cracks tend to propagate parallel to the compressive-stress axis. Even if the time-zero crackformation is not parallel to the compressive-stress axis, it is likely to twist out of its initial orientation to an orientation parallel to the compressive stress axis. The fact that many cracks tend to form in brittle materials under compressive stress can be used to make fine powders from a much larger piece of the brittle material.

# 5.3 Grain Boundaries 

Grain boundaries can often play extremely important roles in the reliability of a material. Many materials (especially metals/conductors) are polycrystalline. Polycrystalline is a term used in materials science to describe solid materials which consist of many tiny single-crystals, called grains, coexisting in the solid material. At the region between grains, the grain boundary, the two grains may be poorly matched in specific density (often referred to as lattice mismatch) and this can sometimes lead to weaker-bonded interfaces.

Figure 13.12 illustrates the specific density of atoms for two crystalline planes, (100) and (110), for the face-centered cubic crystalline structure. The number of enclosed atoms for both cases is the same: $1+4(1 / 4)=2$ atoms for the (100) plane and $2(1 / 2)+4(1 / 4)=2$ atoms for the (110) plane. However, the areas are different. This causes the specific density for the (100) plane to be higher than the (110) plane. Thus, if these two planes were brought together to form a grain boundary, then there would be mismatch in specific densities of atoms (lattice mismatch).

Figure 13.13 illustrates the mismatch that can happen when two grains of different orientations and different specific densities are brought together for joining/ bonding. For large specific-density differences at the g-b interface between the two


Fig. 13.12 Specific density of atoms is illustrated for (100) and (110) planes in the face-centered cubic crystalline structure. One can see that the specific density of atoms in the (100) plane is greater than in the (110) plane. Thus, if two such interfaces formed the bonding interface, a mismatch in specific density of atoms would occur. This mismatch can lead to dangling and/or severely bent bonds

Fig. 13.13 When the two grains $A$ and $B$ are joined along the grain boundary (g-b) interface, a mismatch in specific density of atoms at the interface can result in a large number of dangling and/or stretched bonds along this g-b interface. This causes the g-b free energy to increase above the normal-bonding value and thus causes the g-b to become less stable. This means that g-bs can be prime locations for: enhanced crack propagation, higher corrosion activity, higher impurity precipitation, higher diffusion rates, etc.
grains, the two grains will be poorly matched resulting in a g-b interface with a relatively high density of dangling and/or stretched bonds. This causes the g-b free energy to increase, relative to the normal-bonding state, and this causes the g-b to become generally weaker and less stable than the grains. The g-bs with large mismatch introduce considerable free space into an otherwise normal lattice and can thus serve as a site for impurity precipitation. Also, the g-bs can serve as prime locations for: crack formation, crack propagation, higher corrosion activity, and higher diffusion rates.

Since poorly matched grain boundaries have much higher free energy versus the better matched ones, then, during high temperature annealing, the grains with preferred orientations will tend to grow at the expense of some of the other grains. This grain growth, in order to minimize the number of high free-energy grain boundaries, will tend to minimize the total number of grain boundaries, i.e., the average grain size increases during annealing. Of course, the grain growth during high temperature annealing will also be subject to any mechanical stresses that might be present (or generated) in the material during the annealing process.# 6 Fracture Strength of Materials 

The facture strength (or toughness) of a material is generally found by recording the strain as the stress is increased (ramped) to failure. The ramp-stress-to-failure/ rupture test ${ }^{8}$ is an important mechanical test for several reasons: (1) it is a timezero test of relatively short duration, (2) it is a relatively easy test to perform, and (3) it can be a strong indicator of the reliability of such materials/devices. ${ }^{9}$ A major downside with ramp-stress-to-failure testing is that it is a destructive test. Thus, ramp-stress-to-failure testing can only be used on a sampling basis (for a few materials/devices that were randomly selected for the test). The reliability of the remaining population must be statistically inferred, as discussed in Chap. 17.

A ramp-stress-to-failure/rupture test is normally used to gather the indicated data that is illustrated in Fig. 13.14. As the stress increases from the zero-strain state, the stress depends linearly on the strain and this continues up to the yield point
$\sigma_{Y}=E \varepsilon_{Y}$. Above the yield point, the stress depends on the strain in a more complicated fashion (a power-law):

$$
\sigma=E \varepsilon \quad\left(\varepsilon<\varepsilon_{Y}\right)
$$

and

$$
\sigma=B_{0} \varepsilon^{n} \quad\left(\varepsilon>\varepsilon_{Y}\right)
$$

Fig. 13.14 The fracture/ rupture strength is determined by ramping up the stress (at some specified rate) and monitoring the strain until fracture/rupture occurs. The toughness is the area under the curve


[^0]
[^0]:    ${ }^{8}$ The ramp-to-failure/rupture test is described in detail in Chap. 11.
    ${ }^{9}$ The usefulness of ramp-voltage-to-breakdown test for capacitor dielectrics is highlighted in Chap. 12 .By matching the two equations at $\varepsilon_{Y}$, one obtains:

$$
\sigma=E \varepsilon \quad\left(\varepsilon \leq \varepsilon_{Y}\right)
$$

and

$$
\sigma=E \varepsilon_{Y}\left(\frac{\varepsilon}{\varepsilon_{Y}}\right)^{n} \quad\left(\varepsilon \geq \varepsilon_{Y}\right)
$$

Generally, $n=0.1-0.5$ is observed for many materials.
The material toughness is given by the area under the stress-stain $(\sigma-\varepsilon)$ curve:

$$
\text { Toughness }=\int_{0}^{\varepsilon_{\text {fracture }}} \sigma \mathrm{d} \varepsilon=E \int_{0}^{\varepsilon_{Y}} \varepsilon d \varepsilon+E \varepsilon_{Y} \int_{\varepsilon_{Y}}^{\varepsilon_{\text {fracture }}}\left(\frac{\varepsilon}{\varepsilon_{Y}}\right)^{n} \mathrm{~d} \varepsilon
$$

# Example Problem 5 

The stress-strain curve for a material with modulus of $E=600 \mathrm{GPa}$ is very similar to that shown in Fig. 13.14. If the elastic-strain region extends to a level of $1.5 \%$ and the fracture strain is $30 \%$, then calculate the toughness for this material. Assume that the power-law model, which describes the stress versus strain relation in the plastic region, is given by $n=0.25$.

## Solution

$$
\begin{aligned}
\text { Toughness } & =\int_{0}^{\varepsilon_{\text {fracture }}} \sigma \mathrm{d} \varepsilon=E \int_{0}^{\varepsilon_{Y}} \varepsilon \mathrm{~d} \varepsilon+E \varepsilon_{Y} \int_{\varepsilon_{Y}}^{\varepsilon_{\text {fracture }}}\left(\frac{\varepsilon}{\varepsilon_{Y}}\right)^{n} \mathrm{~d} \varepsilon \\
& =E\left[\frac{\varepsilon_{x}^{2}}{2}\right]+E\left(\varepsilon_{y}\right)^{1-n} \int_{\varepsilon_{Y}}^{\varepsilon_{\text {fracture }}} \varepsilon^{n} \mathrm{~d} \varepsilon \\
& =E\left\{\left[\frac{\varepsilon_{x}^{2}}{2}\right]+\left(\varepsilon_{y}\right)^{1-n}\left[\frac{\left(\varepsilon_{\text {fracture }}\right)^{n+1}-\left(\varepsilon_{y}\right)^{n+1}}{n+1}\right]\right\} \\
& =600 \mathrm{GPa}\left\{\frac{(0.015)^{2}}{2}+(0.015)^{0.75}\left[\frac{(0.30)^{125}-(0.015)^{125}}{1.25}\right]\right\}=4.5 \mathrm{GPa} \\
& =4.5 \mathrm{GPa}\left(\frac{10^{9} \mathrm{~N} / \mathrm{m}^{2}}{1 \mathrm{GPa}}\right)\left(\frac{1 \mathrm{~J}}{1 \mathrm{Nm}}\right)\left(\frac{1 \mathrm{eV}}{1.6 \times 10^{-19} \mathrm{~J}}\right)\left(\frac{1 \mathrm{~m}}{100 \mathrm{~cm}}\right)^{3} \\
& =2.8 \times 10^{22} \mathrm{eV} / \mathrm{cm}^{3}
\end{aligned}
$$In Problem 1 of Chap. 4, it was shown that $\sim 10^{23}$ atoms $/ \mathrm{cm}^{3}$ exist in most dense solids. Therefore, the toughness represents only a few tenths of eV/atom, significantly lower than the bond energy per atom. This is because of intrinsic lattice defects (vacancies, dislocations, grain boundaries, etc.) existing in the materials.

# 7 Stress Relief in Materials 

From the discussions in this chapter, one should now clearly understand that the bonding energy of a solid material is negative and reaches its lowest value when the bonded atoms are in their equilibrium state (non-stretched or non-compressed state). Mechanically stressing the material, either by stretching or compressing the bonds, serves to raise the total energy of the material, making the material less stable and more prone to degradation and eventual failure. Therefore, materials will tend to look for ways of relaxing the mechanical stress $\sigma$ (e.g., vacancy movement, dislocation movement, cracking, buckling, delamination, etc.). These are all important stress-relief mechanisms.

The time dependence of the stress relief, as illustrated in Fig. 13.15, generally takes the form:

$$
\frac{\mathrm{d} \sigma}{\mathrm{~d} t}=-k\left(\sigma-\sigma_{\text {Yield }}\right)
$$

where $k$ is a stress-relaxation rate constant and $\sigma_{\text {yield }}$ is the yield stress. Below the yield stress, it is assumed that little/no relaxation is possible and the material will show elastic behavior (no further degradation with time). Separation of variables and integration of Eq. (13.25),

$$
\int_{\sigma_{\text {Max }}}^{\sigma} \frac{\mathrm{d} \sigma}{\left(\sigma-\sigma_{\text {Yield }}\right)}=-k \int_{0}^{t} \mathrm{~d} t
$$

Fig. 13.15 General stressrelaxation curve is illustrated. Stress relaxation may take many forms: vacancy movement, dislocation movement, voiding, cracking, buckling, delamination, etc.
gives:

$$
\sigma(t)=\sigma_{\text {Yield }}+\left(\sigma_{\text {Max }}-\sigma_{\text {Yield }}\right) \exp (-\mathrm{kt})
$$

Solving Eq. (13.27) for the time-to-relax ( $t=t_{\text {Relax }}$ ), one obtains:

$$
t_{\text {Relax }}=-\left(\frac{1}{k}\right) \ln \left[\frac{\sigma\left(t=t_{\text {Relax }}\right)-\sigma_{\text {Yield }}}{\sigma_{\text {max }}-\sigma_{\text {yield }}}\right]
$$

The time for the stress $\left[\sigma\left(t=t_{\text {Relax }}\right)-\sigma_{\text {yield }}\right]$ to relax, to one-half of its original value $\left[\sigma_{\max }-\sigma_{\text {yield }}\right]$, is given by ${ }^{10}$ :

$$
t_{\text {Relax }}=\left(\frac{\ln (2)}{k}\right)
$$

Stress relaxation can take on several materials-degradation forms: creep, voiding, cracking, delamination, blistering, buckling, etc. The stress relaxation process will continue until the mechanical stress level (originally above the yield strength of the material) relaxes to the yield strength of the material. The yield stress may be quite high and rather precisely defined for some materials (steel) but low and poorly defined for others (aluminum). For brittle materials, such as ceramics, crack formation and propagation may be the only effective stress-relief mechanism available.

# 8 Creep-Induced Failures 

One of the more important failure mechanisms for mechanical systems is creepinduced failure. Creep can refer to an increase in strain with time for a fixed load (constant stress). ${ }^{11}$ However, creep can also refer to stress relaxation for a fixed strain. Either type of creep can produce material degradation as illustrated in Fig. 13.16 and eventual device failure in certain applications.

### 8.1 Creep Under Constant Load/Stress Conditions

Creep under a constant load (constant stress) is shown in Fig. 13.17. When the material is exposed to an applied stress $\sigma$, the time-zero strain that occurs is:

[^0]
[^0]:    ${ }^{10}$ Recall from Chap. 9, one expects the relaxation-rate constant to be thermally activated: $k=k_{0} \exp \left[-Q /\left(K_{B} T\right)\right]$.
    ${ }^{11}$ The load/force is constant. The average stress is only approximately constant during testing due to some expected cross-sectional area changes.Fig. 13.16 When a mechanical stress is applied to a material, the material can become metastable with a driving force $(\Delta G)$ favoring the degraded state. However, the rate of the degradation (creep) is limited by the activation energy $\left(\Delta \mathrm{G}^{*}\right)$ which is generally associated with dislocation movement along the slip planes


Fig. 13.17 Creep behavior under a fixed load (constant stress). (a) At time zero, the length of the material is $L_{0}$. (b) Immediately after a stress $\sigma$ is applied, the strain is: $\varepsilon=\left(L-L_{0}\right) / L_{0}$. (c) If the applied stress $\sigma$ (assumed to be above the materials yield-point) is held constant, then the strain $\varepsilon(t)$ $=\left[L(t)-L_{0}\right] / L_{o}$ ] will increase with time. Creep, under constant load, is usually referred to as an increase in strain with time for a fixed stress
$\varepsilon=\left(L-L_{0}\right) / L_{0}$. If the applied stress (which is assumed to be beyond the material's elastic-region/yield-point) is held constant, then strain will increase with time: $\varepsilon(t)=$ $\left[L(t)-L_{0}\right] / L_{0}$.

A typical creep curve is shown in Fig. 13.18. After an initial period of nonlinear creep, the creep shows an extended period of linear behavior and then, eventually, a shorter period of rapid turn-up and material rupture. Also, one can see in Fig. 13.19 the creep rate depends on the stress level in the material and the temperature (creep is thermally activated). Generally, creep can be an issue for metals when the use temperature is above $40 \%$ of the melting temperature: $T_{\text {creep }}>0.4 T_{\text {melt }}$, where temperatures must be expressed in Kelvin. For example, aluminum melts at $660^{\circ} \mathrm{C}$ ( 933 K ). Therefore, creep in Al could become an issue forFig. 13.18 Typical creep behavior for ductile materials is illustrated


Fig. 13.19 Creep rate $\mathrm{d} \varepsilon / \mathrm{d} t$ increases with stress. Creep rate is also thermally activated

$T_{\text {creep }}>0.4(933 \mathrm{~K})=373 \mathrm{~K}=100^{\circ} \mathrm{C} .^{12}$
In the linear creep region (steady-state creep region), the creep as a function of time is given by:

$$
\varepsilon(t)=\varepsilon_{0}+\left(\frac{\mathrm{d} \varepsilon}{\mathrm{~d} t}\right) t
$$

From the previous equation, one can see that the creep rate $(\mathrm{d} \varepsilon / \mathrm{d} t)$ is of primary/ fundamental importance and becomes the focus of our attention. The creep can continue until a time-to-failure is reached. Time-to-failure (TF) will occur when the

[^0]
[^0]:    ${ }^{12}$ Recall, from Chap. 11, that the stress-migration/creep bakes for aluminum were generally done at temperatures above $100^{\circ} \mathrm{C}$.total creep becomes too large for specified tolerances (or the material fractures/ ruptures) at $t=\mathrm{TF}$, giving:

$$
\mathrm{TF}=\left[\frac{\varepsilon(t=\mathrm{TF})-\varepsilon_{0}}{(\mathrm{~d} \varepsilon / \mathrm{d} t)}\right]
$$

One can see from the previous equation that the time-to-failure is directly proportional to the amount of creep that can be tolerated and with a simple inverse-dependence on creep rate (since the creep rate is constant in the linear creep region).

For the information shown in Fig. 13.19, one can see that the creep rate ( $\mathrm{d} \varepsilon / \mathrm{d} t$ ) depends on both the level of stress and the temperature (thermally activated). Thus, the creep rate can be written as

$$
\frac{\mathrm{d} \varepsilon}{\mathrm{~d} t}=B_{0}\left(\sigma-\sigma_{\text {yield }}\right)^{n} \exp \left(-\frac{Q}{K_{B} T}\right)
$$

Since the creep rate (degradation rate) for constant stress $\sigma$ takes the above form, then the time-to-failure equation can be easily extracted:

$$
\int_{0}^{\varepsilon_{\text {crit }}} \mathrm{d} \varepsilon=\left[B_{0}\left(\sigma-\sigma_{\text {yield }}\right)^{n} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)\right] \int_{0}^{\mathrm{TF}} \mathrm{~d} t
$$

giving,

$$
\mathrm{TF}=A_{0}\left(\sigma-\sigma_{\text {yield }}\right)^{-n} \exp \left(\frac{Q}{K_{B} T}\right)
$$

Note that the kinetics $(n, Q)$ for creep rate $\mathrm{d} \varepsilon / \mathrm{d} t$ and time-to-failure TF are the same, except for a change of sign. This is because the creep is assumed to increase linearly with time (creep rate is constant). As before, $A_{0}$ is a material/process-dependent coefficient that depends on the total amount of creep that can be tolerated. $A_{0}$ can vary from device to device and generally results in a lognormal or Weibull distribution of times-to-failure. Often, the time-to-failure stress dependence is described by $n=1-3$ for relative soft/weak materials (e.g., Pb -alloy solders and viscous glasses), $n=3-6$ for strong metals (e.g., mild steels and many inter-metallic formations) and $n=6-9$ for very strong/brittle materials (e.g., hardened steels and ceramics).

One should be cautioned against taking creep-rate data under very high-stress/ high-temperature test conditions and then extrapolating to very low-stress/lowtemperature operational conditions using the same kinetic values $(n, Q)$. Generally, when creep testing above $T>0.5 T_{\text {melt }}$ one my observe different values for n and activation energy $Q$ than when creep testing at temperatures $T<0.5 T_{\text {melt }}$. One needsTable 13.3 Creep-rate (de/dt) data for a metal alloy

| Temperature |  |  |  |
| :-- | :-- | :-- | :-- |
| Stress (Mpa) | $400^{\circ} \mathrm{C}$ | $450^{\circ} \mathrm{C}$ | $500^{\circ} \mathrm{C}$ |
| 1.0 | $0.001 / \mathrm{h}$ | $0.01 / \mathrm{h}$ | $0.1 / \mathrm{h}$ |
| 1.5 | - | $0.05 / \mathrm{h}$ | - |
| 2.0 | - | $0.16 / \mathrm{h}$ | - |

to ensure that the extrapolations from stress to use conditions are not too optimistic. This caution is emphasized in Example Problem 6.

# Example Problem 6 

Creep-rate ( $\mathrm{d} \varepsilon / \mathrm{d} t$ ) data was collected for a given metal alloy. The tensile stress and temperature conditions during testing are indicated in the Table 13.3. For this particular metal alloy, the yield strength is very low (relative to the stress conditions used) and therefore can be neglected.
(a) Determine the activation energy $Q$ and the stress dependence exponent $n$ that produce the best fitting for the accelerated data for this metal alloy.
(b) Construct the time-to-failure equation for this metal alloy.
(c) Construct the acceleration factor equation for this metal alloy.
(d) If a mechanical component (made of this metal alloy) fails in 2 h at a tensile stress level of 1.9 MPa and a temperature of $380^{\circ} \mathrm{C}$, how long would the component be expected to last at 1.25 MPa and a temperature of $310^{\circ} \mathrm{C}$ ?
(e) How long would the component be expected to last at a tensile stress level of 0.5 MPa and a temperature of $250^{\circ} \mathrm{C}$ ?

## Solution

The creep rate equation is given by:

$$
\frac{\mathrm{d} \varepsilon}{\mathrm{~d} r}=B_{0}(\sigma)^{n} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)
$$

Taking the natural logarithm of both sides of the equation yields:

$$
\operatorname{Ln}(\mathrm{d} \varepsilon / \mathrm{d} t)=\operatorname{Ln}\left(B_{0}\right)+n \operatorname{Ln}(\sigma)-\frac{Q}{K_{\mathrm{B}} T}
$$

Thus, the activation energy for the creep is given by,

$$
Q=-K_{B}\left(\frac{\partial \operatorname{Ln}(\mathrm{~d} \varepsilon / \mathrm{d} t)}{\partial(1 / T)}\right)_{\sigma=\text { constant }}
$$

and the creep exponent n is given by:$$
n=\left(\frac{\partial \operatorname{Ln}(\mathrm{~d} \varepsilon / \mathrm{d} t)}{\partial \operatorname{Ln}(\sigma)}\right)_{T=\text { constant }}=\left(\frac{\partial \log (\mathrm{d} \varepsilon / \mathrm{d} t)}{\partial \log (\sigma)}\right)_{T=\text { constant }}
$$

(a) The plot of $\operatorname{Ln}(d \varepsilon / d t)$ versus $(1 / T)$ is shown in Fig. 13.20 for the constant stress condition of 1 MPa . [Reminder: one must always convert the temperature from degrees centigrade $\left({ }^{\circ} \mathrm{C}\right)$ to Kelvin (K).]

From the slope of the previous plot, one obtains:

$$
Q=-K_{B}\left(\frac{\partial \operatorname{Ln}(\mathrm{~d} \varepsilon / \mathrm{d} t)}{\partial(1 / T)}\right)_{\sigma=\text { constant }}=2.06 \mathrm{eV}
$$

The $\log -\log$ plot of creep rate $(\mathrm{d} \varepsilon / \mathrm{d} t)$ versus stress $(\sigma)$ is shown in Fig. 13.21 for the constant temperature condition of $450^{\circ} \mathrm{C}=723 \mathrm{~K}$.From the previous plot one obtains the creep power-law exponent $n$ :

$$
n=\left(\frac{\partial \operatorname{Ln}(\mathrm{~d} \varepsilon / \mathrm{d} t)}{\partial \operatorname{Ln}(\sigma)}\right)_{T=\text { constant }}=\left(\frac{\partial \log (\mathrm{d} \varepsilon / \mathrm{d} t)}{\partial \log (\sigma)}\right)_{T=\text { constant }} \cong 4.0
$$

(b) The time-to-failure equation for this metal alloy is given by:

$$
\mathrm{TF}=A_{0}(\sigma)^{-4} \exp \left(\frac{2.06 \mathrm{eV}}{K_{\mathrm{B}} T}\right)
$$

(c) The acceleration factor for this metal alloy use conditions is:

$$
\mathrm{AF}=\frac{(\mathrm{TF})_{1}}{(\mathrm{TF})_{2}}=\left(\frac{\sigma_{2}}{\sigma_{1}}\right)^{4} \exp \left[\frac{2.06 \mathrm{eV}}{K_{\mathrm{B}}}\left(\frac{1}{T_{1}}-\frac{1}{T_{2}}\right)\right]
$$

(d) The acceleration factor becomes:

$$
\begin{aligned}
\mathrm{AF} & =\left(\frac{1.9 \mathrm{MPa}}{1.25 \mathrm{MPa}}\right)^{4} \exp \left[\frac{2.06 \mathrm{eV}}{8.62 \times 10^{-5} \frac{\mathrm{eV}}{\mathrm{~K}}}\left(\frac{1}{(310+273) \mathrm{K}}-\frac{1}{(380+273) \mathrm{K}}\right)\right] \\
& =(5.34)(81.0)=432.5
\end{aligned}
$$

The time to failure becomes:

$$
\mathrm{TF}_{1.25 \mathrm{MPa}, 310^{\circ} \mathrm{C}}=\mathrm{AF} \cdot \mathrm{TF}_{19 \mathrm{MPa}, 380^{\circ} \mathrm{C}}=(432.5) \cdot(2 \mathrm{~h})=865 \mathrm{~h}
$$(e) Note that the proposed use conditions $\left(0.5 \mathrm{MPa}, 250^{\circ} \mathrm{C}\right)$ are well below the regions where accelerated data was actually taken (see the previous table).

Optimistic approach: assume that the kinetics $\left(n=4, Q_{\text {creep }}=2.06 \mathrm{eV}\right)$ are valid throughout the full range of stresses and temperatures, giving:

$$
\begin{aligned}
\mathrm{AF} & =\left(\frac{1.9 \mathrm{MPa}}{0.5 \mathrm{MPa}}\right)^{4} \exp \left[\frac{2.06 \mathrm{eV}}{8.62 \times 10^{-5} \frac{\mathrm{eV}}{\mathrm{~K}}}\left(\frac{1}{(250+273) \mathrm{K}}-\frac{1}{(380+273 \mathrm{~K})}\right)\right] \\
& =(208.5)(8926.6)=1.86 \times 10^{6}
\end{aligned}
$$

The time-to-failure becomes:

$$
\begin{aligned}
& \mathrm{TF}_{0.1 \mathrm{MPa}, 200^{\circ} \mathrm{C}}=\mathrm{AF} \cdot \mathrm{TF}_{1.9 \mathrm{MPa}, 380^{\circ} \mathrm{C}}=\left(1.86 \times 10^{6}\right) \cdot(2 \mathrm{~h})=3.72 \times 10^{6} \mathrm{~h} \\
& =3.72 \times 10^{6} \mathrm{~h}\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right)=425 \text { years. }
\end{aligned}
$$

Conservative approach: assume that the kinetics $\left(n=4, Q_{\text {creep }}=2.06 \mathrm{eV}\right)$ are valid over the region where actual data is available and then use more conservative kinetic values ( $n=2$ and $Q_{\text {creep }}=1.0 \mathrm{eV}$ ) below this region.

$$
\begin{aligned}
\mathrm{AF}= & \left(\frac{1.9 \mathrm{MPa}}{1.0 \mathrm{MPa}}\right)^{4} \cdot\left(\frac{1.0 \mathrm{MPa}}{0.5 \mathrm{MPa}}\right)^{2} \\
& \cdot \exp \left[\frac{2.06 \mathrm{eV}}{8.62 \times 10^{-5} \frac{\mathrm{eV}}{\mathrm{~K}}}\left(\frac{1}{(300+273) \mathrm{K}}-\frac{1}{(380+273) \mathrm{K}}\right)\right] \\
& \cdot \exp \left[\frac{1.0 \mathrm{eV}}{8.62 \times 10^{-5} \frac{\mathrm{eV}}{\mathrm{~K}}}\left(\frac{1}{(250+273) \mathrm{K}}-\frac{1}{(300+273) \mathrm{K}}\right)\right] \\
= & (13.03) \cdot(4) \cdot(165.6) \cdot(6.93)=5.98 \times 10^{4}
\end{aligned}
$$

Using this more conservative approach, the time-to-failure becomes:

$$
\begin{aligned}
\mathrm{TF}_{0.5 \mathrm{MPa}, 250^{\circ} \mathrm{C}} & =\mathrm{AF} \cdot \mathrm{TF}_{19 \mathrm{MPa}, 380^{\circ} \mathrm{C}}=\left(5.98 \times 10^{4}\right) \cdot(2 \mathrm{~h})=1.20 \times 10^{5} \mathrm{~h} \\
& =1.2 \times 10^{5} \mathrm{~h}\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right)=13.7 \text { years. }
\end{aligned}
$$

Fig. 13.20 Semi-log plot of creep rate $(\mathrm{d} e / \mathrm{d} t)$ versus $1 / T$ is shown


Fig. 13.21 Log-Log plot of creep rate $(\mathrm{d} e / \mathrm{d} t)$ versus stress $(\sigma)$ is shown

# Example Problem 7 

Shown in Fig. 13.22 is a mechanical rotor that must rotate continuously at 2,500 revolutions per minute (rpm). A heavy mass $(0.5 \mathrm{~kg})$ is attached to the end of an aluminum connecting rod ( 10 cm long, cross sectional-area $1 \mathrm{~cm}^{2}$ ). The mass of the connecting rod is negligible compared to the heavy mass on the end. The designer is worried that the tensile stress in the small diameter connecting rod (during 2,500 rpm operation) may be excessive and creep will eventually cause the large mass to come into contact with the cylindrical walls causing the component to freeze up (fail). To test his hypothesis, the engineer decided to use accelerated testing and subjected the component to acceleratedoperation at $8,000 \mathrm{rpm}$ for an extended period of time. The component failed in 18 h , because of creep, i.e., the large revolving mass started to rub the cylindrical wall $(\Delta r=\Delta x)$ after 18 h under these accelerated conditions. Assuming the following material properties for the aluminum-alloy connecting rod: tensile strength $\sigma_{\mathrm{TS}}=0.6 \mathrm{GPa}$, modulus $E=75 \mathrm{GPa}$, a negligible yield point, and a stress dependence power-law exponent of $n=4$.
(a) Find the stress in the aluminum component during $8,000 \mathrm{rpm}$ accelerated operation.
(b) Find the stress in the aluminum component for the expected normal $2,500 \mathrm{rpm}$ operation.
(c) Given that the aluminum component lasted 18 h at $8,000 \mathrm{rpm}$, how long would the component last during normal operation at $2,500 \mathrm{rpm}$ ?

# Solution 

(a) Due to circular motion, tensile stress in constant in the aluminum-alloy rod and is given by:

$$
\begin{aligned}
\sigma_{T, 8,000 \mathrm{rpm}} & =\frac{F_{r}}{\mathrm{~A}}=\frac{\mathrm{M} \mathrm{\tau} \omega^{2}}{1 \mathrm{~cm}^{2}} \\
& =\frac{(0.5 \mathrm{~kg})(0.1 \mathrm{~m})[2 \pi(8,000 \mathrm{rpm})(1 \mathrm{~min} / 60 \mathrm{~s})]^{2}}{1 \mathrm{~cm}^{2}}\left(\frac{100 \mathrm{~cm}}{1 \mathrm{~m}}\right)^{2} \\
& =0.351 \times 10^{9} \mathrm{~N} / \mathrm{m}^{2}=0.351 \mathrm{GPa}
\end{aligned}
$$

With no yield point, creep is expected at $8,000 \mathrm{rpm}$.
(b) At $2,500 \mathrm{rpm}$, the tensile stress would be:

$$
\begin{aligned}
\sigma_{T, 2,500 \mathrm{rpm}} & =\left(\frac{\omega_{\text {use }}}{\omega_{\text {accelerated }}}\right)^{2} \sigma_{T, 8,000 \mathrm{rpm}}=\left(\frac{2.500}{8.000}\right)^{2}(0.351 \mathrm{GPa}) \\
& =0.034 \mathrm{Gpa}
\end{aligned}
$$

(c) The acceleration factor is:

$$
\begin{aligned}
\mathrm{AF} & =\frac{\mathrm{TF}_{\oplus 2,500 \mathrm{rpm}}}{\mathrm{TF}_{\oplus 8,000 \mathrm{rpm}}}=\left(\frac{\sigma_{T, 8,000 \mathrm{rpm}}}{\sigma_{T, 2,500 \mathrm{rpm}}}\right)^{4}=\left(\frac{\omega_{\oplus 8,000 \mathrm{rpm}}^{2}}{\omega_{\oplus 2,500 \mathrm{rpm}}^{2}}\right)^{4} \\
& =\left(\frac{8000}{2500}\right)^{8}=1.1 \times 10^{4}
\end{aligned}
$$Therefore, for $2,500 \mathrm{rpm}$ operation, then one would expect the component to last:

$$
\begin{aligned}
\mathrm{TF}_{\oplus 2,500 \mathrm{rpm}} & \geq \mathrm{AF} \cdot \mathrm{TF}_{\oplus 8,000 \mathrm{rpm}}=\left(1.1 \times 10^{4}\right)(18 \mathrm{~h})=198,000 \mathrm{~h} \\
& =198,000 \mathrm{~h}\left(\frac{1 \text { year }}{8,760 \mathrm{~h}}\right)=22.6 \text { years. }
\end{aligned}
$$

Note that the AF depends on the 8th power of the angular speed. Hopefully, one can start to better understand why mechanical components in an engine tend to fail much faster under engine race conditions ( $8,000+\mathrm{rpm}$ ) versus normal auto driving conditions ( $2,500 \mathrm{rpm}$ ).

Fig. 13.22 Mechanical rotor is designed to rotate at an angular speed of $\omega$. The rotor consists of a heavy mass $M$ that is constrained to rotate by a light Al-alloy connecting rod. The tolerance $\Delta x$ is the free space between the mass and the cylinder walls. If significant creep with time occurs in the aluminum rod, the mass will make contact with the cylinder walls and the rotor will fail (freeze up)


# 8.2 Creep Under Constant Strain Conditions 

Creep under a constant strain is shown in Fig. 13.23. When the material is exposed to an applied stress $\sigma$ (assumed to be above the material's yield point), the time-zero strain that occurs is: $\varepsilon=\left(L-L_{0}\right) / L_{0}$.

If the strain is held constant and the stress is monitored with time, then the stress $\sigma(t)$ will relax with time-the force per unit area needed to hold the fixed strain in the material will reduce with time. General features of stress relaxation were discussed earlier, see Fig. 13.15, but we would like to take a closer look at stress relaxation under the condition of constant strain.

The total strain can be written in terms of the elastic (recoverable) part plus the plastic (permanent deformation) part:

$$
\varepsilon_{\text {total }}=\varepsilon_{\text {elastic }}+\varepsilon_{\text {plastic }}
$$Fig. 13.23 Illustration of creep under a fixed strain. (a) At time zero, the length of the material is $L_{0}$. (b) Immediately after a stress $\sigma$ is applied, the strain is: $\varepsilon=$ $\left(L-L_{0}\right) / L_{0}$. (c) If the strain is held constant, then the stress $\sigma(t)$ will be a function of time. Creep at constant strain is referred to as stress relaxation. The time dependence of the stress relaxation is expected to be similar to that shown in Fig. 13.15


For stress relaxation, where the total strain remains constant, then

$$
\frac{\mathrm{d} \varepsilon_{\text {total }}}{\mathrm{d} t}=0 \Rightarrow \frac{\mathrm{~d} \varepsilon_{\text {plastic }}}{\mathrm{d} t}=-\frac{\mathrm{d} \varepsilon_{\text {elastic }}}{\mathrm{d} t}=-\frac{1}{E} \frac{\mathrm{~d} \sigma}{\mathrm{~d} t}
$$

Creep occurs because of plastic deformation, therefore:

$$
\frac{\mathrm{d} \varepsilon_{\text {plastic }}}{\mathrm{d} t}=A_{0}\left(\sigma-\sigma_{\text {yield }}\right)^{n} \exp \left(\frac{-Q}{K_{B} T}\right)
$$

For constant strain, one can use Eq. (13.35) to write:

$$
\frac{\mathrm{d} \varepsilon_{\text {plastic }}}{\mathrm{d} t}=-\frac{\mathrm{d} \varepsilon_{\text {elastic }}}{\mathrm{d} t}=-\frac{1}{E} \frac{\mathrm{~d} \sigma}{\mathrm{~d} t}=B_{0}\left(\sigma-\sigma_{\text {yield }}\right)^{n}
$$

Separating variables in Eq. (13.38) and integrating, one obtains:

$$
\int_{\sigma_{\max }}^{\sigma} \frac{\mathrm{d} \sigma}{\left(\sigma-\sigma_{\text {yield }}\right)^{n}}=-B_{0} E \int_{0}^{t} \mathrm{~d} t
$$

For $n=1$, the previous equation reduces to Eq. (13.27):

$$
\sigma(t)-\sigma_{\text {yield }}=\left(\sigma_{\max }-\sigma_{\text {yield }}\right) \exp [-k t]
$$

where $k$ is the relaxation rate constant, $k=B_{0} E$. If we define TF as the stress level at which $\left[\sigma(t=\mathrm{TF})-\sigma_{\text {yield }}\right]$ becomes some fraction f of $\left[\sigma_{\max }-\sigma_{\text {yield }}\right]$, then:$$
\begin{aligned}
\mathrm{TF} & =-\frac{1}{k} \ln (f) \\
& =-\frac{\ln (f)}{k_{0}} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
\end{aligned}
$$

where we have used the expectation from Chap. 8 that the relaxation rate constant will be thermally activated and given by,

$$
k=k_{0} \exp \left[-\frac{Q}{K_{B} T}\right]
$$

For values of $n \neq 1$, one obtains from Eq. (13.39):

$$
\frac{1}{\left[\sigma(t)-\sigma_{\text {yield }}\right]^{n-1}}-\frac{1}{\left[\sigma_{\max }-\sigma_{\text {yield }}\right]^{n-1}}=(n-1) \mathrm{kt}
$$

Again, if one defines TF as $\left[\sigma(t=\mathrm{TF})-\sigma_{\text {yield }}\right]=f\left[\sigma_{\max }-\sigma_{\text {yield }}\right]$, then:

$$
\begin{aligned}
\mathrm{TF} & =\frac{1}{k(n-1)\left[\sigma_{\max }-\sigma_{\text {yield }}\right]^{n-1}}\left[\frac{1-f^{n-1}}{f^{n-1}}\right] \\
& =\frac{1}{k_{0}(n-1)\left[\sigma_{\max }-\sigma_{\text {yield }}\right]^{n-1}}\left[\frac{1-f^{n-1}}{f^{n-1}}\right] \exp \left(\frac{Q}{K_{B} T}\right) \\
& =A_{0}\left(\sigma_{\max }-\sigma_{\text {yield }}\right)^{-(n-1)} \exp \left(\frac{Q}{K_{B} T}\right)
\end{aligned}
$$

At first glance, stress relaxation might be thought to be a good thing-lower stress is good, right? No, not always. Many fasteners (e.g., nuts and bolts) may rely on very high stress levels to properly clamp things into place. This is why one generally wants to snug up a nut on a bolt during the assembly of mechanical components so that the nut and bolt will serve as an adequate clamp for the components (so that they will be held tightly in place). In a critically important clamping application, one does not want the stress in the materials to relax. This is illustrated in Example Problem 8.

# Example Problem 8 

Three mechanical components are fastened/clamped using a nut and bolt as illustrated in Fig. 13.24. During the initial stage of tightening of the nut, free space is simply being eliminated between the nut and the various members as shown. Once the free space is eliminated, then the tensile stress rises rapidly in the bolt shaft with each turn of the nut. Due to the pitch of the threads on the bolt, during each turn of the nut (after free space elimination), the length of unstressed bolt region (above the nut) increases by $0.4 \%$ for each completeturn of the nut. The properties of the mild steel used in bolt and nut fabrication are: modulus $E=200 \mathrm{GPa}$, tensile yield strength $\sigma_{Y}=0.2 \mathrm{GPa}$, tensile strength $\sigma_{\mathrm{TS}}=0.5 \mathrm{GPa}$, and a power-law creep exponent of $n=4$. To make sure that the members are properly clamped, the nut is tightened to a tensile level of 0.4 GPa in the bolt and the level of stress must stay above 0.25 GPa for adequate clamping.
(a) Immediately after the free space elimination between nut and members, estimate the tensile stress in the bolt with each additional $3 / 4$ turn of the nut.
(b) If we assume that most of the stress relaxation occurs within the shaft of the bolt, as opposed to the other materials, then if the stress in the bolt relaxes from 0.4 to 0.35 GPa in 1 year, how long will it take for the stress to relax to 0.25 GPa ?

# Solution 

(a) Assume that the bolt is initially in the elastic region. Since a single turn of the nut produces a strain of 0.004 in the bolt, then the $5 / 4$ turn will produce a strain of 0.001 . The tensile stress $\sigma$ in the bolt associated with this level of strain $(\varepsilon=0.001)$ is:

$$
\sigma=\mathrm{E} \varepsilon=(200 \mathrm{GPa})(0.001)=0.2 \mathrm{GPa}
$$

(b) First we must determine the relaxation rate constant $k$. Assuming a creep power-law exponent of $n=4$, one obtains:

$$
\begin{aligned}
k & =\frac{1}{3 t}\left[\frac{1}{\sigma(t)^{3}}-\frac{1}{\sigma_{\max }^{3}}\right] \\
& =\frac{1}{3(1 \text { year })}\left[\frac{1}{(0.35 \mathrm{GPa})^{3}}-\frac{1}{(0.4 \mathrm{GPa})^{3}}\right] \\
& =\frac{2.57}{(\mathrm{GPa})^{3} \text { year }}
\end{aligned}
$$

Thus, the time-to-relax to a value of 0.25 GPa becomes:

$$
\begin{aligned}
t & =\frac{1}{3 \mathrm{k}}\left[\frac{1}{\sigma(t)^{3}}-\frac{1}{\sigma_{\max }^{3}}\right] \\
& =\frac{1}{3\left(\frac{2.57}{(\mathrm{GPa})^{3} \text { year }}\right)}\left[\frac{1}{(0.25 \mathrm{GPa})^{3}}-\frac{1}{(0.4 \mathrm{GPa})^{3}}\right] \\
& =6.3 \text { years. }
\end{aligned}
$$Fig. 13.24 Nut and bolt are used to clamp three members of a multicomponent system. As the nut is tightened (to create an effective clamp) the bolt shaft comes under a state of tension while members $A, B$, and $C$ are compressed


Let us now turn our attention to what is happening to the metal inside the shaft of the bolt. As the tensile stress in the shaft of the bolt relaxes, the bolt loses some of its clamping effectiveness. This stress relaxation necessitates a continual tightening of the nut to maintain proper clamping. Let us suppose that every six months the nut must be turned one-quarter of a turn in order to return the shaft of the bolt back to its original tensile stress level (which restores its original clamping effectiveness). With each complete turn, the nut (due to the pitch of the threads on the bolt/nut) results in $0.4 \%$ of the mass (originally in the shaft) now being above the top of the nut. Since the mass of the bolt above the top of the nut is virtually in a stress-free state then, effectively, $0.4 \%$ of the metal in the shaft of the bolt will transfer/flow from the high stress shaft region of the bolt to a lower stress region above the nut every two years. Since this is a mass-conserving process, then the density of the metal in the shaft must be reducing with time (due to the flux divergence effect discussed in Chap. 4). This reduction in density of the metal in the shaft with time normally results in void formations along grain boundaries which are roughly perpendicular to the axis of the shaft, as illustrated in Fig. 13.25.

The previous example (voiding in the shaft of a bolt under tension) serves to illustrate a very important point: atoms will flow from regions of higher stress to regions of lower stress so as to reduce the stress-level in the material. However, this material flow, and resulting flux divergences (as discussed in Chap. 4), can produce void formations in the material. The mass flow and voiding at temperatures well below the melting temperature, tend to occur along grain boundaries finally resulting in failure with time.Fig. 13.25 For confined metals under tension, stress relaxation can result in void formations along grain boundaries


# 9 Crack-Induced Failures 

Crack-induced failures can be particularly important because it is difficult to fabricate mechanical devices without at least some micro-cracks developing during fabrication. Once a crack has developed, the crack may tend to propagate under loading with crack propagation eventually leading to device failure.

At first thought, the introduction of a small crack would seem to be insignificant. For example, suppose that one introduces a small thin crack of radius $a$ in a cylindrical rod of radius $R$. Further assume that the crack is perpendicular to the length of the rod which is the tensile-stress axis. Thus, the impact on the average tensile stress would be:

$$
\sigma_{T}=\frac{F}{\pi R^{2}-\pi a^{2}}=\frac{\left(\sigma_{T}\right)_{0}}{1-\left(\frac{a}{R}\right)^{2}}
$$

Thus, the impact of a small crack on the average tensile stress would seem to be very small if $a \ll R$. However, Eq. (13.45) is not valid for reliability assessments of materials with cracks. To emphasize this, suppose that the initial tensile $\left(\sigma_{T}\right)_{0}$ is well below the yield strength of the material. With the introduction of a small crack, it is unlikely that the small crack $(\mathrm{a} \ll \mathrm{R})$ introduction will cause the average tensile stress $\sigma_{T}$ to increase above the yield strength of the material. Thus, one might come to the erroneous conclusion that the small crack should have little/ no impact on the reliability of the cylindrical rod. Our initial reliability assessment of the reliability impact of the crack is flawed (pardon the pun) because it ignores the stress raisers/ risers at crack tips.# 9.1 Stress Raisers/Risers at Crack Tips 

Equation (13.45) is not the proper reliability analysis for a crack. While it does comprehend a small rise in average tensile stress in the rod with crack introduction, this equation does not comprehend the large stress raiser/riser ${ }^{13}$ that can occur at the tips of the crack. This is illustrated in Fig. 13.26, where we look more closely at what happens to the lines of force when a crack is introduced.

The lines of force before and after a horizontal crack introduction are shown in Fig. 13.26. Before the introduction of the crack, the lines of force are parallel and uniform, producing a uniform tensile stress $\sigma(=F /$ Area $)$ as illustrated in Fig. 13.26a. However, after crack introduction, the lines of force are no longer uniform and parallel as illustrated in Fig. 13.26b.

The higher density of lines of force at the tips of the crack produces a stress raiser (increase in stress) at the crack tips and a non-uniform stress in the material. At some distance away from the crack, the lines of force again will become uniform and parallel. The stress raiser, however, serves to bring the tip of the crack to a stress level which may exceed the yield stress of the material and thus produces continued plastic deformation/damage in the material.

Fig. 13.26 (a) Lines of force are uniform and parallel initially, producing a uniform stress of $\sigma=$ Force/Area. (b) The introduction of the crack causes the lines of force to become non-uniform and non-parallel (producing a crowding of force lines at the crack tip). The higher density of force lines at the crack tip produces a stress riser (much higher stress level than the uniform stress level $\sigma$ ) and this may induce additional crack growth



[^0]
[^0]:    ${ }^{13}$ Historically, these localized stresses at crack tips have been referred to as either stress raisers or stress risers. The terms will be used interchangeably.Fig. 13.27 Molecular bonds are shown broken for the elliptical crack of major diameter 2a and minor diameter 2b. The strain energy, above and below the crack, has been partially relieved. Bonds near the crack tip are severely strained (plastic region). Regions well beyond the crack tip are in the normal tensile-stressed state


Figure 13.27 illustrates a more microscopic (molecular level) view of things. One can see that the bonds are broken at the site of the crack which tends to increase the bonding energy. Above the crack, however, the bonds are more relaxed (reducing the strain energy). Near the crack tip, the bonds are severely strained (raising the bond energy). This region is often referred to as the plastic region.

Griffith has shown that for brittle materials with an elliptical crack of length 2a (major diameter) and width 2b (minor diameter) as shown in Fig. 13.27, the stress raiser $\sigma_{\text {raiser }}$ at the tip of the crack is given by:

$$
\sigma_{\text {raiser }}=\sigma_{o}\left[1+2\left(\frac{a}{b}\right)\right]
$$

where $\sigma_{0}$ is the uniform stress before crack introduction. A useful term is the stress concentration factor $K$ given by:

$$
K=\frac{\sigma_{\text {raiser }}}{\sigma_{0}}=1+2\left(\frac{a}{b}\right)
$$

# Example Problem 9 

A cylindrical rod has yield strength of 600 MPa and it is tensile loaded with an average stress of 400 MPa . If an elliptical crack is introduced with major axis $2 a$ and minor axis $2 b$, such that the ratio is given by $a / b=4$, estimate the stress raiser at the tip of the crack and comment on its reliability impact.# Solution 

$$
\begin{aligned}
\sigma_{\text {raiser }} & =\sigma_{o}\left[1+2\left(\frac{a}{b}\right)\right] \\
& =400 \mathrm{MPa}[1+2(4)] \\
& =3.6 \mathrm{GPa}
\end{aligned}
$$

Note that the stress at the crack tip ( 3.6 GPa ) is well above the yield strength $(0.6 \mathrm{GPa})$ of the material and plastic-deformation/damage is expected at the crack tip; thus, crack propagation is likely. Even for the most forgiving crack (a spherically shaped crack with $a=\mathrm{b}$ ), the stress-riser is still three times the nominal/average-stress.

### 9.2 Strain-Energy Release Rate

Figure 13.28 illustrates a material which is uniformly tensile stressed by the fixed external force. If a thin horizontal crack develops, as illustrated in Fig. 13.28, then some of the tensile strain energy stored in the material will be reduced/released, both above and below the crack. If the horizontal crack propagates further, then even more strain energy stored in the material will be released. The fundamental question is, of course, will the strain energy released with crack growth be more than offset by the rise in potential energy due to the bond breakage which occurs as the crack propagates? If the answer is yes, then crack propagation is expected to continue and will eventually lead to device failure.

While the analysis presented here may be oversimplified, it is instructive to consider how much strain energy would be released when the thin circular crack shown in Fig. 13.28 grows in size. We first consider brittle materials (where the strain energy stored is in terms of elastic energy) and then generalize the results to comprehend plastic materials.

Fig. 13.28 The external force is acting to put the material in a uniform tensile state. The strain energy stored in this film can be released/reduced by crack formation and growth
The impact on the molecular bonding due to crack formation/growth is illustrated in Fig. 13.27. Note that the crack (of length $2 a$ ) allows the material above and below the crack to relax to a more unstressed state, thus reducing the strain energy in the material. However, the bonds in the material region near the cracked tip are highly strained. Well beyond the crack tip, the material is in the normal tensile-stress state.

The strain energy density (energy per unit volume) stored in a brittle crack-free material of modulus $E$ is given by:

$$
u_{\text {elastic }}=\frac{1}{2} E e^{2}=\frac{1}{2}\left(\frac{\sigma^{2}}{E}\right)
$$

While an oversimplification, let us assume that a thin crack develops ( $b \simeq 0$ in Fig. 13.27) and propagates horizontally in a circular pattern (of radius $a$ ), as indicated in Fig. 13.28. To further simplify the analysis presented, let us assume that the strain energy immediately above and below the crack area is released/relaxed for some effective thickness $t_{\text {eff }}$. Therefore, the strain energy that is released when a thin circular crack develops in a brittle material and propagates horizontally is:

$$
U_{\text {released }}=u_{\text {elastic }} \cdot(\text { Volume })=\frac{1}{2}\left(\frac{\sigma^{2}}{E}\right)\left(\pi a^{2} t_{\text {eff }}\right)
$$

In analyzing crack growth problems, the strain-energy release rate $G$ is of great importance. ${ }^{14} G$ represents the energy released (when a crack of radius $a$ increases to $a+\mathrm{d} a$ ). For a circular crack growing horizontally, as illustrated in Fig. 13.28, $G$ can be determined from Eq. (13.49) and is given by:

$$
G=\frac{1}{t_{\text {eff }}}\left(\frac{\mathrm{d} U_{\text {released }}}{\mathrm{d} a}\right)=\pi a\left(\frac{\sigma^{2}}{E}\right)
$$

While Eq. (13.50) for $G$ was produced here, under some oversimplified assumptions, Griffith has shown that this equation for $G$ is generally valid for brittle materials. It is interesting to note that $G$, as normally defined by Eq. (13.50), represents a rate only in the sense that $\mathrm{d} U_{\text {released }} / \mathrm{d} a$ represents the strain energy released for an incremental change in crack size da. Given the previous energy balance discussion - the strain energy released must be greater than or equal to the bonding energy increase associated with the crack size growth-then this energy requirement can be restated, for the crack size to grow at a rapid rate:

$$
G \geq G_{\text {critical }}
$$

[^0]
[^0]:    ${ }^{14}$ The elastic energy $U_{\text {elastic }}$ of the material reduces with crack propagation, thus we have defined $\Delta U_{\text {released }}$ such that it is always positive, i.e., $\Delta U_{\text {released }}=-\Delta U_{\text {elastic }}$.# 9.3 Fast Fracture/Rupture 

$G_{\text {crit }}$ has been measured for many materials by introducing a crack (actually a halfcrack) in the side of the material to a known depth $a$ and then recording the level of average stress in the material which causes rapid/catastrophic fracture. $G_{\text {crit }}$ is determined by combining Eqs. (13.50) and (13.51), giving:

$$
\sigma_{\text {fracture }} \sqrt{\pi a}=\sqrt{\mathrm{EG}_{\text {crit }}}
$$

Typical measured values of $G_{\text {crit }}$ for several material types are shown in Table 13.4.

Let us make sure that we clearly understand the implications of Eq. (13.52). The right-hand side of this equation is in terms of measured material parameters only and is a constant. The left-hand side is a product of the average stress $\sigma$ in the material and the root of $\pi$ times the half-crack size $a$; if this product is equal to or greater than the right side of the equation, then rapid/catastrophic fracture is expected.

Also shown in Table 13.4 are the related stress concentration factors $K_{\text {crit }}$ (also called fracture toughness), where $K_{\text {crit }}$ is given by:

$$
K_{\text {crit }}=\sigma_{\text {fracture }} \sqrt{\pi a}=\sqrt{\mathrm{EG}_{\text {crit }}}
$$

One should note that since the units of $G$ are in energy/area, then the energy release rate $G$ can be thought of as the energy required for the creation of two new surfaces $2 \Gamma$, where $\Gamma$ is the specific energy (surface energy per unit area). Thus, with $G=2 \Gamma$, Eq. (13.50) can be rewritten as:

$$
\sigma_{\text {fracture }}=\sqrt{\frac{\mathrm{E} 2 \Gamma}{\pi a}}
$$

While the previous equations were developed under the brittle material assumption (no plastic deformation), in most ductile materials crack propagation involves more energy considerations than simply new surfaces creation-around each crack an extensive plastic region exists, as illustrated in Fig. 13.27. Yielding in metals

Table 13.4 Representative values for $G_{\text {crit }}$ and $K_{\text {crit }}$

| Material | $G_{\text {crit }}\left(\mathrm{kJ} / \mathrm{m}^{2}\right)$ | $K_{\text {crit }}\left(\mathrm{MN} / \mathrm{m}^{3 / 2}\right)$ |
| :-- | :-- | :-- |
| Dutile Metals: $\mathrm{Cu}, \mathrm{Ni}, \mathrm{Al}, \mathrm{Ag}$ | $100-1,000$ | $100-350$ |
| Steel | $10-100$ | $50-150$ |
| Al-Alloys | $10-30$ | $20-50$ |
| Strong Polymers, Cast Iron | $1-10$ | $1-15$ |
| Granite, Silicon Nitride | $0.1-1.0$ | $2-5$ |
| Beryllium, Silicon Carbide, Alumina, Glass | $0.01-0.1$ | $1-3$ |
| Ice | 0.003 | 0.2 |occurs at the ends of the crack thus increasing the toughness of the material, as indicated in Table 13.4. Generally, ductile metals show much greater toughness (higher $G_{\text {crit }}$ and $K_{\text {crit }}$ ). Brittle materials such as glass show little toughness.

Irwin has shown that the plastic region associated with the crack simply serves to increase the specific surface energy and thus produces an effective specific surface energy $\Gamma_{\text {eff }}$ which can be written as:

$$
\Gamma_{\text {eff }}=\Gamma_{\text {surface }}+\Gamma_{\text {plastic }}
$$

Thus, the Griffith criterion can still be used even for ductile materials:

$$
G_{\text {crit }}=\pi a\left(\frac{\sigma_{\text {rupture }}^{2}}{E}\right)
$$

The rupture stress $\sigma_{\text {rupture }}$ is used here for ductile materials since fracture stress $\sigma_{\text {fracture }}$ is usually reserved for brittle materials. Therefore, one can write for both brittle and ductile materials:

$$
\sigma_{\text {rupture }}=\sqrt{\frac{\mathrm{EG}_{\text {crit }}}{\pi a}}=\sqrt{\frac{2 E \Gamma_{\text {eff }}}{\pi a}}=\frac{K_{\text {crit }}}{\sqrt{\pi a}}
$$

Again, we remind ourselves-when the right-hand side of Eq. (13.57) is equal to the nominal/average stress in the material, then we expect rapid crack propagation and catastrophic rupture. ${ }^{15}$ The nominal/average stress level in the material at which this occurs is referred to as the rupture stress $\sigma_{\text {rupture }}$. One can see that the larger the crack size $a$, the lower the average stress level in the material needed to produce rapid rupture. Also, perhaps it is helpful to remember a common-experience example. When striking a piece of wood parallel to the wood fibers with an axe, the piece of wood will show fast rupture/splitting when a combination of stress level and indentation/crack-size produced by the axe reaches a critical level.

# 10 Fatigue-Induced Failures 

During the discussion of crack propagation, it was emphasized that rapid crack propagation resulting in rapid/catastrophic failure was expected when:

[^0]
[^0]:    ${ }^{15}$ Note that when the crack size $a$ goes to zero, the apparent rupture stress goes to infinity. However, in these situations, where the right-hand side of the equation becomes extremely large, the rupture stress will be limited by the normal crack-free rupture mechanisms and $\sigma_{\text {rupture }}$ will assume the crack-free rupture strength.Fig. 13.29 Cracks can develop just above the welded connection of a sign/ light pole to its base plate. Gusting-wind conditions and/ or changes in wind direction can result in a cyclical stress in the metal. Cyclical stress can cause the cracks to grow, eventually leading to failure. Also note that the cracks tend to form in the heat affected region (the region in the pole just above the welded region)


$$
K=K_{\text {crit }}=\sigma_{\text {rupture }} \sqrt{\pi a}=\sqrt{\mathrm{EG}_{\text {crit }}}
$$

This does not mean, however, that the material will not fail with time when $K<$ $K_{\text {crit }}$. The material will fail with time, and the time-to-failure will depend on the level of stress.

One mechanism that can produce time-dependent failure is fatigue. For example, crack formation often occurs in a metal sign/light pole at its welded connection to its supporting base plate as illustrated in Fig. 13.29. As the pole sways, in a gusting wind, one side of the metal pole at its supporting base-plate connection will come under tension while the opposite side will come under compression. The stress state and the magnitude of these stresses will continually change with a changing wind. Also, the tensile and compressive states in the pole will be reversed with a reversal of wind direction.

Fatigue failure can result in cycles-to-failure problems. The subject of fatigue can be so important that it is discussed separately in this text. Fatigue can arise when a material is continually put under cyclical stress conditions as illustrated in Fig. 13.30.

Useful stress parameters for describing cyclical stress are:

$$
\Delta \sigma=\sigma_{\max }-\sigma_{\min }, \sigma_{\text {mean }}=\frac{\sigma_{\max }+\sigma_{\min }}{2}, \sigma_{a}=\frac{\sigma_{\max }-\sigma_{\min }}{2}
$$

where $\Delta \sigma$ is the stress range, $\sigma_{\text {mean }}$ is the mean stress, and $\sigma_{a}$ is the amplitude of stress relative to the mean.

We will first consider cyclical stressing where one has alternating equal amounts of tensile and compressive stress, i.e., $\sigma_{\text {mean }}=0$, and then generalize to $\sigma_{\text {mean }} \neq$ 0 conditions. Also, rather than discussing TF, it is more useful to discuss cycles-tofailure (CTF) for fatigue-related failures.

Fig. 13.30 Cyclical stress is shown. Key parameters for the cyclical stress are: maximum stress level $\left(\sigma_{\max }\right)$ and minimum stress level $\left(\sigma_{\min }\right)$ that define the stress range $(\Delta \sigma)$, mean stress level $\left(\sigma_{\text {mean }}\right)$, and stress amplitude $\left(\sigma_{a}\right)$

Fig. 13.31 Stress $(\sigma)$-Strain $(\varepsilon)$ curve for one cycle of cyclical stress with $\sigma_{\text {mean }}=$ 0 . Material damage/ degradation can be expected during plastic deformation. The amount of strain in the plastic region is represented by $\Delta \varepsilon_{\mathrm{pl}}$


# 10.1 Fatigue for Materials (No Pre-existing Cracks) 

Shown in Fig. 13.31 is a typical stress-strain $(\sigma-\varepsilon)$ curve for a material. In the elastic region, it is assumed that no damage is occurring during cycling. In the plastic region, each stress cycle will induce a certain amount of plastic deformation (damage/degradation) to the material. The degradation will continue with each cycle until the material fails.Fig. 13.32 Stress( $\sigma$ )-Strain ( $\varepsilon$ ) curves. Solid curve represents a cycle with $\sigma_{\text {mean }}$ $=0$. Dashed curve represents a cycle with $\sigma_{\text {mean }}$ $>0$. For a constant $\Delta \sigma$ range, greater material damage/degradation can be expected with $\sigma_{\text {mean }}>$ 0 during plastic deformation due to the fact that $\left(\Delta \varepsilon_{\mathrm{pl}}\right)_{1}>$ $\left(\Delta \varepsilon_{\mathrm{pl}}\right)_{0}$


# 10.2 Low-Cycle Fatigue 

Since the damage to the material during each cycle depends on the amount of plastic deformation $\Delta \varepsilon_{\mathrm{pl}}$, then a power-law model for the CTF would seem to be reasonable:

$$
\mathrm{CTF}=B_{0}\left(\Delta \varepsilon_{\mathrm{pl}}\right)^{-n}(\text { low-cycle fatigue })
$$

The previous equation is referred to as the Coffin-Manson Model and it is generally valid for low-cycle fatigue (where CTF is generally $<10^{4}$ cycles) due to large plastic strain $\Delta \varepsilon_{\mathrm{pl}}$ during the cycling. The values of $n$ generally range from $n=$ 1 to 3 for ductile metals, 3-6 for hard materials, and 6-9 for brittle materials. One can see in Fig. 13.32, with a mean stress offset ( $\sigma_{\text {mean }}>0$ ), that even greater plastic strain $\left(\Delta \varepsilon_{\mathrm{pl}}\right)_{1}$ occurs during each cycle thus shorter CTF can be expected:

$$
\mathrm{CTF}=B_{0}\left(\Delta \varepsilon_{p l}\right)_{1}^{-n}(\text { low-cycle fatigue })
$$

The stress offset serves to increase the amount of plastic deformation $\left[\left(\Delta \varepsilon_{\mathrm{pl}}\right)_{1}\right.$ greater than $\left(\Delta \varepsilon_{\mathrm{pl}}\right)_{0}$ ] during each cycle thus reducing the number of cycles-to-failure.

### 10.3 High-Cycle Fatigue

An alternative equation (power-law expression using the stress range $\Delta \sigma$ rather than the plastic strain) is generally used for high-cycle ( $>10^{4}$ cycles) fatigue:

$$
\mathrm{CTF}=B_{0}\left(\Delta \sigma-\Delta \sigma_{\text {elastic }}\right)^{-m}(\text { high-cycle fatigue })
$$where the total stress range is $\Delta \sigma$ and $\Delta \sigma_{\text {elastic }}$ is the portion of the total stress range that is in the elastic region (thus producing no damage). The previous equation is generally referred to as Basquin's Law. This equation is used for cyclic stresses, where the stress range is given by $\Delta \sigma$ and zero mean stress $\left(\sigma_{\text {mean }}=0\right)$. If, however, $\sigma_{\text {mean }} \neq 0$ (e.g., offset in the tensile-stress direction), then a Goodman-like relation can be developed for the effective stress range $(\Delta \sigma)_{\text {eff }}$ :

$$
(\Delta \sigma)_{\mathrm{eff}}=\frac{\Delta \sigma}{1-\left(\sigma_{\text {mean }} / \sigma_{\mathrm{TS}}\right)}
$$

Note that with a mean stress offset of $\sigma_{\text {mean }}$ (if it is a significant fraction of the tensile strength $\sigma_{\mathrm{TS}}$ ) it serves to increase the effective cyclical stress range $\Delta \sigma_{\text {eff }}$. An increase in the effective stress range, according to Eq. 13.62, reduces the number of cycles-to-failure CTF.

An example of a mean stress offset is illustrated in Fig. 13.33. In Fig. 13.33a, a metal pole is shown supporting a sign. During gusting-wind conditions, a cyclical stress will be generated in the pole, with the maximum bending moment occurring where the metal pole is welded to its base plate. Shown in Fig. 13.33b is a similar situation of a pole supporting a sign; except in this case, a cantilever attachment of a stoplight to the pole also exists. This cantilevered attachment of the stoplight to the pole will serve to put the left side of the pole, at its base plate connection, in a state of


Fig. 13.33 Shown in (a) is metal pole supporting a sign. Also shown are the bolts used to clamp the base plate to the fixed support. Shown in (b) is a similar configuration except that a cantilevered beam is also attached to the pole behind the sign. On the cantilevered beam hangs a stoplight which serves to produce an added moment (additional mean stress) at the base platemean tension and the opposite side in a state of mean compression. Now, with gusting wind conditions, the left side of the pole will have cyclical stress about a mean tensile stress. With a mean tensile stress in the pole, the effective stress range $(\Delta \sigma)_{\text {eff }}$ given by Eq. 13.63 will now be larger than the actual stress range $(\Delta \sigma)$ and each cycle will now produce more damage.

One can see from Eq. (13.63) that as the mean stress $\sigma_{\text {mean }}$ increases (relative to the tensile strength $\sigma_{\mathrm{TS}}$ of the material), then the effective stress range $(\Delta \sigma)_{\text {eff }}$ increases and a shorter number of CTF is expected, given by:

$$
\mathrm{CTF}=B_{0}\left[\frac{\Delta \sigma}{1-\left(\sigma_{\text {mean }} / \sigma_{\mathrm{TS}}\right)}-\Delta \sigma_{\text {elastic }}\right]^{-m}
$$

# Example Problem 10 

A metal pole experiences a cyclic stress at the base-plate connection due to the swaying of the pole. During a half cycle, one side of the metal pole at the base plate will come under tension while the opposite side comes under compression, then the roles of tension/compression are reversed during the next half cycle. In addition, if the pole also supports an overhanging structure such as the stoplight shown in Fig. 13.33, then an additional mean stress offset of $\sigma_{\text {mean }}=190 \mathrm{MPa}$ will occur. To make sure that the pole will last the required time, accelerated data was taken on poles (without an overhanging structure) where a cyclical stress was applied to the poles whereby the metal at the base plate came under a continuous cyclical stress range of -600 MPa to +600 MPa with a mean tensile stress of zero. The poles failed at the base plate connection after 10,000 cycles. Assuming a power-law exponent of $n=4$ for the cycling, a metal tensile strength of 800 MPa and no defined elastic range (due to cracks or other issues):
(a) Estimate the number of cycles-to-failure CTF that would be expected if the normal-use stress range is between -200 MPa to +200 MPa and there is no overhanging structure.
(b) Estimate the number of cycles-to-failure CTF that would be expected if the normal-use stress range is between -200 MPa and +200 MPa but there is an overhanging structure that produces mean tensile offset of $\sigma_{\text {mean }}=$ 190 MPa .

## Solution

(a) Expected acceleration factor for the cycling:

$$
\mathrm{AF}=\left[\frac{(\Delta \sigma)_{\text {stress }}}{(\Delta \sigma)_{\text {operation }}}\right]^{n}=\left[\frac{600-(-600) \mathrm{MPa}}{200-(-200) \mathrm{MPa}}\right]^{4}=[3]^{4}=81
$$Therefore:
$(\mathrm{CTF})_{\text {operation }}=\mathrm{AF} \cdot(\mathrm{CTF})_{\text {stress }}=81(10,000$ cycles $)=810,000$ cycles.
(b) The overhang which serves to produce a mean stress in the pole also serves to increase the effective stress range under use conditions:

$$
(\Delta \sigma)_{\mathrm{eff}}=\frac{\Delta \sigma}{1-\frac{\sigma_{\text {mean }}}{\sigma_{\mathrm{TS}}}}=\frac{[200-(-200)] \mathrm{MPa}}{1-\frac{190 \mathrm{MPa}}{800 \mathrm{MPa}}}=525 \mathrm{MPa}
$$

The acceleration factor now becomes:

$$
\mathrm{AF}=\left[\frac{(\Delta \sigma)_{\text {stress }}}{(\Delta \sigma)_{\text {operation }}}\right]^{n}=\left[\frac{600-(-600) \mathrm{MPa}}{525 \mathrm{MPa}}\right]^{4}=[2.286]^{4}=27
$$

Therefore:

$$
(\mathrm{CTF})_{\mathrm{op}}=\mathrm{AF} \cdot(\mathrm{CTF})_{\text {stress }}=27(10,000 \text { cycles })=270,000 \text { cycles. }
$$

# 10.4 Fatigue for Materials (With Pre-existing Cracks) 

A material with a pre-existing crack is stressed with a sinusoidal stress as shown in Fig. 13.34. The stress concentration factor $K$ for a crack was previously defined for a constant tensile stress load $\sigma . \Delta K$ values are useful for cyclical stress:

$$
\Delta K=K_{\text {high }}-K_{\text {low }}=\left(\sigma_{\text {high }}-\sigma_{\text {low }}\right) \sqrt{\pi a}=\Delta \sigma \sqrt{\pi a}
$$

Fig. 13.34 Sinusoidal stress is applied to a material with a pre-existing crack
The crack growth $\mathrm{d} a$ per cycle $\mathrm{d} N$ can be written:

$$
\frac{\mathrm{d} a}{\mathrm{~d} N}=C_{0}(\Delta K)^{m}=F_{0}(\Delta \sigma)^{m}(a)^{m / 2}
$$

Separating variables and integrating, gives:

$$
\int_{0}^{\mathrm{CTF}} \mathrm{~d} N=\left[\frac{1}{F_{0}} \int_{a_{0}}^{a_{\text {fall }}} \frac{\mathrm{d} a}{a^{m / 2}}\right](\Delta \sigma)^{-m}
$$

The above equation reduces simply to a power-law dependence:

$$
\mathrm{CTF}=A_{0}[\Delta \sigma]^{-m}
$$

No elastic range $\Delta \sigma_{\text {elastic }}$ appears in Eq. (13.68) because it assumes that the stress riser at crack tips reduces the elastic range to zero. As previously discussed, for cyclical stressing when $\sigma_{\text {mean }} \neq 0$, then

$$
\mathrm{CTF}=A_{0}\left[\frac{\Delta \sigma}{1-\left(\sigma_{\text {mean }} / \sigma_{\mathrm{TS}}\right)}\right]^{-m}
$$

One can see that the functional form for CTF in Eq. (13.64) [for materials without cracks] is very similar in form to that for materials with cracks, Eq. (13.69). However, there is no assumed elastic range $\Delta \sigma_{\text {elastic }}$ when the crack is present and the prefactors ( $A_{0}$ and $B_{o}$ ) are quite different. In general, for materials with cracks, $A_{0}$ is much less than $B_{0}$. Also, the cracks (which may vary greatly in number and size from device to device) generally drive a wider spread in the CTF data. This serves to produce a larger logarithmic standard deviation (in the case of the log-normal distribution) or a smaller Weibull slope (in the case of the Weibull distribution).

# Example Problem 11 

Suppose that a certain batch of poles (described in Example Problem 10) has cracks (at time-zero) just above the welded region at the base plate. Rather than failing at 10,000 cycles under accelerated cyclical stress, they now fail in 1,000 cycles.
(a) Estimate the number of cycles-to-failure CTF that would be expected if the normal-use stress range is between -200 MPa to +200 MPa (without an overhanging structure).
(b) Estimate the number of cycles-to-failure CTF that would be expected if the normal-use stress range is between -200 MPa and +200 MPa and with anoverhanging structure that produces mean tensile stress offset of $\sigma_{\text {mean }}=$ 190 MPa .

# Solution 

One would expect that the cracks will impact the prefactor in the CTF Eq. (13.69) but the acceleration factors are expected to be similar. Thus,
(a) $(\mathrm{CTF})_{\text {operation }}=\mathrm{AF} \cdot(\mathrm{CTF})_{\text {stress }}=81(1,000$ cycles $)=81,000$ cycles.
(b) $(\mathrm{CTF})_{\mathrm{op}}=\mathrm{AF} \cdot(\mathrm{CTF})_{\text {stress }}=27(1,000$ cycles $)=27,000$ cycles.

## 11 Adhesion Failures

Adhesion failures are associated with the debonding of materials. Similar to all the other failure mechanisms discussed, adhesion failures are driven by a free energy difference between the bonded and debonded materials.

Consider two materials that are bonded at an interface, as shown in Fig. 13.35. Let us compare the stress energy in the films (which is positive) to the interfacial bonding energy (which is negative). The stress energy would be lower if the two materials would delaminate but the interfacial energy would be higher due to the broken bonds. These are the two competing energy mechanisms that serve to hold the two materials together.

The elastic stress-energy density $u$ in the two materials can be written as:

$$
u_{\text {elastic }}=u_{A}+u_{B}=\frac{1}{2}\left(\frac{1}{E_{A}}\right) \sigma_{A}^{2}+\frac{1}{2}\left(\frac{1}{E_{B}}\right) \sigma_{B}^{2}
$$

If the two materials $A$ and $B$ delaminate, two new surfaces will be created, one with a specific energy density ${ }^{16} \Gamma_{A}$ and the other $\Gamma_{B}$. Thus, the total specific energy density associated with the formation of the two new surfaces is given by: $\Gamma_{\text {total }}=\Gamma_{A}$ $+\Gamma_{B}$.


Fig. 13.35 Two materials, $A$ and $B$, are bonded together. If there are stresses in the two materials (due to Material $A$ interacting with Material B, and vice versa) then there will be a driving force for the two materials to delaminate. A driving force for delamination, over some interfacial area da, will exist if the stress-energy reduction in $A$ and $B$ is greater than the increase in bonding energy associated with the formation of the delaminated region $d a$

[^0]
[^0]:    ${ }^{16}$ Recall that specific energy density is the energy per unit area.Therefore, the free energy driving force for the materials to delaminate is: the stress energy reduction in some differential area $\mathrm{d} a$ must be greater than the increase in bonding energy associated with the creation of the two new surfaces at the interface:

$$
\left[\frac{1}{2}\left(\frac{1}{E_{A}}\right) \sigma_{A}^{2}\right]\left(t_{A} \mathrm{~d} a\right)+\left[\frac{1}{2}\left(\frac{1}{E_{B}}\right) \sigma_{B}^{2}\right]\left(t_{B} \mathrm{~d} a\right) \geq\left[\Gamma_{A}+\Gamma_{B}\right] \mathrm{d} a
$$

This reduces simply to:

$$
\frac{1}{2}\left(\frac{t_{A}}{E_{A}}\right) \sigma_{A}^{2}+\frac{1}{2}\left(\frac{t_{B}}{E_{B}}\right) \sigma_{B}^{2} \geq \Gamma_{A}+\Gamma_{B}
$$

While the focus of this section is on adhesion, there is a similarity with crack propagation previously discussed. For a crack to propagate, the strain energy released within the materials or along their interfaces must be greater than the increase in specific energy density associated with the newly created surfaces/ interfaces during the crack growth. ${ }^{17}$ For delamination to continue, the strain energy release rate by delamination must be greater than the specific energy increase associated with the two new surfaces.

# 12 Thermal-Expansion-Induced Failures 

Solid materials tend to expand when heated. The reason for this is the asymmetrical bonding potential between the atoms forming the solid (as illustrated in Fig. 13.1). The thermal expansion of materials, in itself, is not a reliability issue. The thermal expansion simply redefines a new equilibrium position. However, if the material is constrained in any way, while it is trying to expand thermally, then large thermomechanical stresses can develop in the materials. It is these large thermomechanical stresses that can cause material degradation and eventual failure of the device.

### 12.1 Thermal Expansion

The molecular bonding model shown in Fig. 13.1 permits one to discuss what happens to the equilibrium bonding positions as the temperature is increased. The

[^0]
[^0]:    ${ }^{17}$ Historically, this has been referred to as Griffith's equation which was developed for brittle materials. More recently, Irwin is usually credited for developing the failure in terms of a strain energy release rate $G$ [(Eq. (13.56)], which incorporates both elastic and plastic deformations when new surfaces or interfaces are formed.

Fig. 13.36 Increase in temperature serves to increase the probability that higher vibrational quantum states will be occupied. Due to the asymmetrical bonding potential, the higher quantum states will have an increase in mean bond length
asymmetrical potential associated with molecular bonding is illustrated in Fig. 13.36.

Quantum mechanics permits only certain allowed vibrational states to exist. Increasing the temperature (thermal energy) serves to make the population of the higher vibrational states more probable. However, the mean position for the vibrating atom tends to increase with higher vibrational-state population. Therefore, the mean bond length tends to increase with temperature.

Since the change in bond length $\Delta r$ with temperature is generally small compared with the original bond length $r_{0}$, a Taylor expansion normally suffices:

$$
r(T) \cong r\left(T_{0}\right)+\left(\frac{\partial r}{\partial T}\right)_{T=T_{0}}\left(T-T_{0}\right)
$$

Equation (13.73) can be rewritten simply as:

$$
\frac{\Delta r}{r_{0}}=\alpha \Delta T
$$

where $\alpha$ is the linear thermal expansion coefficient defined as ${ }^{18}$ :

$$
\alpha=\frac{1}{r_{0}}\left(\frac{\partial r}{\partial T}\right)_{T=T_{0}}
$$

[^0]
[^0]:    ${ }^{18}$ Linear coefficients of thermal expansion are listed for several material types (in units of $10^{-6} /{ }^{\circ} \mathrm{C}$ ): $\alpha_{\text {polymers }} \cong 50, \alpha_{\text {metals }} \cong 10, \alpha_{\text {ceramics }} \cong 2, \alpha_{\text {glass }} \cong 0.5$.The translation from microscopic (molecular) dimensions $r$ to macroscopic length $L$ (solid) dimensions is straightforward. If the length of the solid material is $L$, then $L$ must be given by the number of elemental units $N$ times the elemental distance r , then one can write:

$$
\frac{\Delta L}{L_{0}}=\frac{L(T)-L\left(T_{0}\right)}{L\left(T_{0}\right)}=\frac{N\left[r_{0}+\Delta r\right]-\mathrm{Nr}_{0}}{\mathrm{Nr}_{0}}=\frac{\Delta r}{r_{0}}
$$

Therefore:

$$
\alpha=\frac{1}{r_{0}}\left(\frac{\partial r}{\partial T}\right)_{T=T_{0}}=\frac{1}{L_{0}}\left(\frac{\partial L}{\partial T}\right)_{T=T_{0}}
$$

Since the linear strain $\varepsilon$ is given by $\Delta L / L_{0}$ (or equivalently $\Delta r / r_{0}$ ), then the thermal expansion strain, from Eq. (13.74), is given by:

$$
\varepsilon=\alpha \Delta T
$$

# 12.2 Constrained Thermal-Expansion 

If a material is constrained such that it cannot move during temperature changes, then a thermomechanical stress $\sigma$ develops in the material given by:

$$
\sigma=E \varepsilon=\alpha E \Delta T
$$

where $E$ is Young's modulus. Using Eq. (13a) from Chap. 4, then time-to-failure due to a constrained thermomechanical stress is expected to take the form:

$$
\mathrm{TF}=A_{0}(\sigma)^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)=B_{0}\left(T-T_{0}\right)^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right) \quad\left(\text { for } T>T_{0}\right)
$$

Or

$$
\mathrm{TF}=A_{0}(\sigma)^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)=B_{0}\left(T_{0}-T\right)^{-n} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right) \quad\left(\text { for } T<T_{0}\right)
$$

In the previous equation, $T_{0}$ is assumed to be the temperature at which zero stress exists in the material. As one goes to a temperature above or below $T_{0}$, a thermomechanical stress develops in the material. The thermomechanical stress can bring about material degradation and possible failure due to creep, especially at elevated temperatures. The impact of this thermomechanical stress on the time-to-failure is expected to be thermally activated (activation energy $=Q$ ). However, the effective/observed activation energy will be complicated by the fact that the prefactor in the above equation is also temperature dependent. This was discussed in detail for stress migration in Chap. 11.

# 12.3 Thermal-Expansion Mismatch 

Seldom is there only a single material used in a device. Different materials are often joined/bonded together to form the device. If these materials have significantly different thermal expansion coefficients, then large thermal-expansion mismatch stresses can be generated during thermal cycling. These thermomechanical stresses can induce failures because of: creep, fatigue, cracking, buckling and/or delamination.

Shown in Fig. 13.37 are two materials, $A$ and $B$, which are constrained to move together during thermal expansion due to the adhesion forces existing at the interface of materials $A$ and $B$. If the two materials were joined at temperature $T_{0}$, and if material $A$ is assumed to have a greater thermal expansion coefficient than $B$, then an increase in temperature above $T_{0}$ will result in A being under a state of compression and $B$ under tension.

The strain in material $A$ is given by:

$$
\varepsilon_{A}=\frac{\Delta L}{L_{0}}-\alpha_{A} \Delta T
$$

and, likewise, the strain in $B$ is given by:

$$
\varepsilon_{B}=\frac{\Delta L}{L_{0}}-\alpha_{B} \Delta T
$$



Fig. 13.37 Two materials are constrained by interfacial adhesion to move together during thermal expansion from $T_{0}$ to $T$. If the thermal expansion coefficient for $A$ is greater than $B$, then constrained thermal expansion above $T_{0}$ results in $A$ being in compression and $B$ in tensionSince the two materials are constrained to move together during the thermal expansion, then Newton's third law tells us that the force of Material $A$ acting on $B$ must be equal and opposite to $B$ acting on $A$ :

$$
\begin{gathered}
F_{A}=-F_{B} \\
\Rightarrow \sigma_{A}\left(t_{A} \cdot \text { Width }\right)=-\sigma_{B}\left(t_{B} \cdot \text { Width }\right) \\
\Rightarrow\left(E_{A} \varepsilon_{A}\right) t_{A}=-\left(E_{B} \varepsilon_{B}\right) t_{B} \\
\Rightarrow \varepsilon_{A}=-\left(\frac{E_{B}}{E_{A}}\right)\left(\frac{t_{B}}{t_{A}}\right) \varepsilon_{B}
\end{gathered}
$$

where $E$ is the modulus for each material and $t$ is the thickness of each material. Solving Eqs. (13.81), (13.82) and (13.83) for $\sigma_{A}$ and $\sigma_{B}$, one obtains:

$$
\sigma_{A}=E_{A} \varepsilon_{A}=\frac{E_{A}\left(\alpha_{B}-\alpha_{A}\right) \Delta T}{1+\left(\frac{E_{A}}{E_{B}}\right)\left(\frac{t_{A}}{t_{B}}\right)}
$$

and

$$
\sigma_{B}=E_{B} \varepsilon_{B}=\frac{E_{B}\left(\alpha_{A}-\alpha_{B}\right) \Delta T}{1+\left(\frac{E_{B}}{E_{A}}\right)\left(\frac{t_{B}}{t_{A}}\right)}
$$

Note that when $\alpha_{A}>\alpha_{B}$, material $A$ will be under compression and material $B$ will be under tension.

It is instructive to look at the strain ratio $\left(\varepsilon_{A} / \varepsilon_{B}\right)$, stress ratio $\left(\sigma_{A} / \sigma_{B}\right)$ and the stress energy density ratio $\left(u_{A} / u_{B}\right)$ for thermal expansion mismatch:

Strain Ratio

$$
\frac{\varepsilon_{A}}{\varepsilon_{B}}=-\left(\frac{E_{B}}{E_{A}}\right)\left(\frac{t_{B}}{t_{A}}\right)
$$

Stress Ratio:

$$
\frac{\sigma_{A}}{\sigma_{B}}=-\left(\frac{t_{B}}{t_{A}}\right)
$$

Energy Density Ratio:

$$
\frac{u_{A}}{u_{B}}=\frac{\frac{1}{2} E_{A} \varepsilon_{A}^{2}}{\frac{1}{2} E_{B} \varepsilon_{B}^{2}}=\frac{E_{B}}{E_{A}}\left(\frac{t_{B}}{t_{A}}\right)^{2}
$$Note that if the material thicknesses are equal, $t_{A}=t_{B}$, then Eq. (13.86) shows that most of the strain will be in the lower modulus material. Furthermore, Eq. (13.88) indicates that most of the energy density will be in the lower modulus material.

# 12.4 Thin Films on Thick Substrates 

It is well known that thin layers (thin films) on thick materials (thick substrates) are prone to delamination, cracking, buckling, or blistering. Eqs. (13.86), (13.87) and (13.88) can be used to understand why this is the case. Assuming that the modulus for $A$ is similar to that for $B$; when the substrate (material $B$ ) is very thick compared to material $A$, then most of the strain, stress, and energy density is in thin film $A$. If the adhesion strength of materials $A$ and $B$ is relatively good, then tensile-stressed films can crack (Fig. 13.38) to relieve the strain energy. Compressive films can buckle (Fig. 13.39) in order to release the strain energy-this is why a thermal expansion gap in concrete is often used. If the adhesion strength of $A$ and $B$ is relatively poor, then delamination/blistering can occur (Fig. 13.40) in order to release the strain energy.

In addition to thermomechanical stress in thin films, intrinsic stresses can also be very important. Intrinsic stresses can develop during fabrication of the material and these stresses are not related to thermal-expansion mismatch. An example of

Fig. 13.38 Cracking can occur when material $A$ is under tensile stress. Cohesive cracking is a stress/strain-energy release mechanism when the adhesion of $A$ and $B$ is strong. Delamination of layer $A$ from layer $B$ can occur if the adhesion of $A$ to $B$ is relatively weak


Fig. 13.39 Shown is the buckling which can occur when material $A$ is under compressive stress. Buckling can be a compressive stress-relief/ strain-energy release mechanism when the adhesion of layer $A$ to layer $B$ is strong
Fig. 13.40 Shown is the blistering which can occur when material $A$ is under compressive stress.
Blistering is a compressive stress-relief/ strain-energy release mechanism when the adhesion of layers $A$ and $B$ is relatively weak

intrinsic stress is the stress which can develop in thin metal-oxide layers which are thermally grown at a fixed temperature on relatively thick metal substrates. If the volume of the metal oxide is much larger than the volume of the metal consumed, then a large compressive stress will develop in the metal-oxide layer during growth. Likewise, if the volume of the metal oxide is much less than the volume of the metal consumed, then a large tensile stress will develop in the metal-oxide layer during growth. These intrinsic stresses are developed during thin-film fabrication (metaloxide growth) and, as such, are built into the film during fabrication. As these metaloxide films are then lowered from their fabrication/growth temperature, then the thermal expansion mismatch can add to or reduce the mechanical stress in these thin films.

# Example Problem 12 

A metal component in a certain application will be thermal cycled from room temperature to an oxidizing ambient of $250^{\circ} \mathrm{C}$. To prevent oxidation of the metal at the high temperatures, a thin ceramic coating is used on the metal component. The concern is that cracks will develop in the ceramic layer during thermal cycling thus exposing the metal to oxidation. To accelerate the cracking, the components were thermal cycled from room temperature to $700^{\circ} \mathrm{C}$. If cracks start to develop in the ceramic layer after 100 thermal cycles from room temperature to $700^{\circ} \mathrm{C}$, how many crack-free cycles would be expected from room temperature to $250^{\circ} \mathrm{C}$ ? Assume that the ceramic material is hard/brittle with a temperature exponent of at least $n=7$.

## Solution

$$
\mathrm{AF} \geq\left[\frac{(\Delta T)_{\text {stress }}}{(\Delta T)_{\text {operation }}}\right]^{n}=\left[\frac{(700-25)^{\circ} \mathrm{C}}{(250-25)^{\circ} \mathrm{C}}\right]=(3)^{7}=2,187
$$

Therefore:
$(\mathrm{CTF})_{\text {operation }} \geq \mathrm{AF} \cdot(\mathrm{CTF})_{\text {stress }}=2,187(100$ cycles $)=218,700$ cycles.

Fig. 13.41 Strong driving force (large $\Delta G$ ) exists for metal oxidation. The activation energy $\left(\Delta G^{*}\right)$ tends to limit the corrosion rate

# 13 Corrosion-Induced Failures 

There is a strong driving force (large free energy difference) for metals to oxidize/ corrode as illustrated in Fig. 13.41. This is why, in nature, one can easily find metal oxides (ores) but it is very difficult to find the element in its pure-metallic form. The only exception to this is gold (which generally does not oxidize) and it can found in nature in the metallic state. However, generally, metals are found in nature as metal oxides.

In order to obtain metal in a pure metallic form, a significant energy input is required to separate the metal from its oxide/ore. Once in the metallic form, tremendous amounts of money (tens of \$billions each year) are spent for corrosion prevention and replacement of corroded parts.

An example of corrosion failure is shown Fig. 13.42 where a U-type support clamp has totally corroded away at the point of maximum bending.

### 13.1 Dry Oxidation

Table 13.5 shows the very strong driving force $\left(\Delta G_{\text {Formation }}\right)$ for a metal atom to combine with $\mathrm{O}_{2}$ to form a metal oxide. The more negative the formation energy, the stronger the driving force for the metal atom to oxidize. However, the activation energy which limits the oxidation rate depends on the ability of the metal ions and/orFig. 13.42 Corrosion failure of a U-type metal support clamp. The metal at the bottom of the support clamp has corroded away. One should note that the corrosion rate was greatest in the regions where the metal was severely bent


Table 13.5 Free energy for Metal-Oxide (MxOy) formation

| Metal | Oxidation state | $\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ | $\Delta G\left[\mathrm{~kJ} /\left(\right.\right.$ Mole of $\left.\mathrm{O}_{2}\right)$ ] | $\Delta G\left[\mathrm{eV} /\left(\mathrm{O}_{2}\right.\right.$ molecule)] |
| :--: | :--: | :--: | :--: | :--: |
| Be | $\mathrm{Be} \rightarrow \mathrm{Be}^{2+}+2 \mathrm{e}$ | BeO | $-1,182$ | $-12.27$ |
| Al | $\mathrm{Al} \rightarrow \mathrm{Al}^{3+}+3 \mathrm{e}$ | $\mathrm{Al}_{2} \mathrm{O}_{3}$ | $-1,045$ | $-10.85$ |
| Ti | $\mathrm{Ti} \rightarrow \mathrm{Ti}_{2+}+2 \mathrm{e}$ | TiO | $-1,000$ | $-10.38$ |
| Si | $\mathrm{Si} \rightarrow \mathrm{Si}^{4+}+4 \mathrm{e}$ | $\mathrm{SiO}_{2}$ | $-848$ | $-8.80$ |
| Ta | $\mathrm{Ta} \rightarrow \mathrm{Ta}^{5+}+5 \mathrm{e}$ | $\mathrm{Ta}_{2} \mathrm{O}_{5}$ | $-764$ | $-7.93$ |
| Cr | $\mathrm{Cr} \rightarrow \mathrm{Cr}^{3+}+3 \mathrm{e}$ | $\mathrm{Cr}_{2} \mathrm{O}_{3}$ | $-757$ | $-7.86$ |
| Zn | $\mathrm{Zn} \rightarrow \mathrm{Zn}^{2+}+2 \mathrm{e}$ | ZnO | $-636$ | $-6.60$ |
| W | $\mathrm{W} \rightarrow \mathrm{W}^{6+}+6 \mathrm{e}$ | $\mathrm{WO}_{3}$ | $-510$ | $-5.29$ |
| Fe | $\mathrm{Fe} \rightarrow \mathrm{Fe}^{2+}+2 \mathrm{e}$ | FeO | $-508$ | $-5.27$ |
| Sn | $\mathrm{Sn} \rightarrow \mathrm{Sn}^{2+}+2 \mathrm{e}$ | SnO | $-500$ | $-5.19$ |
| Ni | $\mathrm{Ni} \rightarrow \mathrm{Ni}^{2+}+2 \mathrm{e}$ | NiO | $-439$ | $-4.56$ |
| Cu | $\mathrm{Cu} \rightarrow \mathrm{Cu}^{2+}+2 \mathrm{e}$ | CuO | $-254$ | $-2.64$ |
| Pt | $\mathrm{Pt} \rightarrow \mathrm{Pt}^{4+}+4 \mathrm{e}$ | $\mathrm{PtO}_{2}$ | $-160$ | $-1.66$ |
| Ag | $\mathrm{Ag} \rightarrow \mathrm{Ag}^{+}+\mathrm{e}$ | $\mathrm{Ag}_{2} \mathrm{O}$ | $-5$ | $-0.05$ |
| Au | $\mathrm{Au} \rightarrow \mathrm{Au}^{3+}+3 \mathrm{e}$ | $\mathrm{Au}_{2} \mathrm{O}_{3}$ | 80 | 0.83 |

oxygen ions to diffuse through $\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ oxide layer formed, as well as the ability of the electrons to conduct through this oxide layer. Key features of the oxidation process are shown in Fig. 13.43.

The process of oxidation generally converts metals into insulators. Normally this is thought to have negative consequences; but, in at least one very important case (oxidation of silicon), this oxide formation permits one to build metal/oxide/ silicon field-effect transistors (MOSFETs) which were instrumental in driving the $>\$ 250$ B/year semiconductor industry in 2008. It is very difficult to imagine life without computers, laptops, smart phones, iPods, iPads, implantable medical devices, etc. In addition, copper oxide tends to be superconducting at low temperatures.

Fig. 13.43 Dry metal corrosion (oxidation in an $\mathrm{O}_{2}$ containing gas ambient at high temperatures) results in an metal-oxide $\left(\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}\right)$ formation on the surface of the metal. The quality of this oxide layer generally controls the oxidation reaction rate by limiting M-ion and/or O-ion diffusion. Also shown are the freed electrons (from the metal ion) that must be able to conduct through this oxide layer in order for the oxidation process to continue

There are at least three oxidation models often used to describe the rate of oxidation: linear growth rate, parabolic growth rate, and logarithmic growth rate. Often, the initial growth rate for a period of time $t_{0}$ will be erratic until some minimum oxide thickness $x_{0}$ (at least a few monolayers) is reached. Then above the initial thickness and time conditions $\left(x_{0}, t_{0}\right)$, the growth rate is relatively well behaved and generally described by one of the three models given below.

# 13.1.1 Linear Oxide-Growth Region 

In the linear growth region, one assumes that the oxide thickness $x$ grows at a constant rate $k_{1}$ which is temperature dependent:

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=k_{1}
$$

where,

$$
k_{1}=k_{10} \exp \left(-\frac{Q}{K_{B} T}\right)
$$

Separating the variables, in Eq. (13.89), and integrating from the initial conditions $\left(x_{0}, t_{\mathrm{o}}\right)$ to the conditions $(x, t)$, one obtains:

$$
x=x_{0}+k_{1}\left(t-t_{0}\right)
$$Assuming that time-to-failure $(t=\mathrm{TF})$ for a device occurs when the oxide thickness increases to some critical level $(\Delta x)_{\text {crit }}=\left(x_{\text {crit }}-x_{0}\right)$, then TF is given by:

$$
T F=t_{0}+\frac{(\Delta x)_{\text {crit }}}{k_{10}} \exp \left(\frac{Q}{K_{B} T}\right)=t_{0}+A_{10} \exp \left(\frac{Q}{K_{B} T}\right)
$$

Normally, $\mathrm{TF} \gg t_{0}$ and $t_{0}$ is often ignored.
Some metals such as iron tend to show poor resistance to oxidation because the oxide layer cracks and/or delaminates during oxidation. Oxide damage will tend to occur when the volume of the metal oxide $\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ is much different from the volume of the consumed metal $M$. If the metal oxide $\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ volume is less than the volume of the metal M consumed, then the oxide layer will be in a severe state of tension and a strong driving force for oxide cracking will exist. If the metal oxide $\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ volume is much greater than the metal $M$ consumed, then the oxide layer will be under severe state of compression and oxide layer delamination (blistering or buckling) can be anticipated. Shown in Fig. 13.44 is a pure piece of Cu after it has been exposed to dry oxidation at $250^{\circ} \mathrm{C}$. Note that the damage that occurs in the $\mathrm{Cu}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ layer is because of intrinsic stresses developed during oxide growth.


Fig. 13.44 Dry oxidation of pure copper. (a) Copper at time-zero. (b) After $250^{\circ} \mathrm{C}$ storage in an oxygen-containing ambient. $\mathrm{Cu}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}$ layer shows evidence of cracking and delamination# 13.1.2 Parabolic Oxide-Growth Region 

In the parabolic oxide-growth region, one assumes that the growth rate is inversely proportional to the oxide thickness and directly proportional to the reaction rate constant $k_{2}$ which is temperature dependent:

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{k_{2}}{x}
$$

where

$$
k_{2}=k_{20} \exp \left(-\frac{Q}{K_{B} T}\right)
$$

Separating variables, in Eq. (13.93), and integrating

$$
\int_{x_{0}}^{x} x \mathrm{~d} x=k_{2} \int_{t_{0}}^{t} \mathrm{~d} t
$$

then one obtains

$$
x^{2}=x_{0}^{2}+2 k_{2}\left(t-t_{0}\right)
$$

Note that for $t \gg t_{0}$ and $x \gg x_{0}$, then one obtains the standard diffusion relation:

$$
x=\sqrt{\mathrm{Dt}}
$$

where,

$$
D(T)=2 k_{2}(T)=2 k_{20} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)=D_{0} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)
$$

Assuming that $t=\mathrm{TF}$, when the oxide thickness reaches some critical value $x_{\text {crit }}$, then

$$
\mathrm{TF}=t_{0}+\left(\frac{x_{\text {crit }}^{2}-x_{0}^{2}}{2 k_{20}}\right) \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)=t_{0}+A_{20} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
$$

Often, $T F \gg \mathrm{t}_{0}$ and $t_{0}$ is ignored.# Example Problem 13 

The critically important integrated circuit (IC) industry is based on the ability to grow a self-passivating oxide layer on silicon. During parabolic oxide growth at high temperatures, it was found that $\mathrm{SiO}_{2}$ grew to an oxide thickness of 100 $\stackrel{\circ}{\mathrm{A}}$ in one hour. How long would it take for $\mathrm{SiO}_{2}$ oxide to grow to $200 \AA$ ?

## Solution

For a parabolic growth rate, and assuming that the time-zero oxide thickness on the silicon is negligible, one obtains:

$$
\begin{aligned}
x^{2} & =\mathrm{kt} \\
& \Rightarrow k=\frac{x^{2}}{t}=\frac{\left(100 \stackrel{\circ}{\mathrm{~A}}\right)^{2}}{1 h r}=\frac{1,000 \AA^{2}}{1 h r}=1 \times 10^{4} \frac{\AA^{2}}{\mathrm{~h}}
\end{aligned}
$$

Therefore, the total time required to grow the oxide layer to $200 \AA$ is:

$$
t=\frac{x^{2}}{k}=\frac{\left(200 \stackrel{\circ}{\mathrm{~A}}\right)^{2}}{1 \times 10^{4} \frac{\AA^{2}}{\mathrm{hr}}}=4 \mathrm{hrs}
$$

## Example Problem 14

In the previous example problem, it took 4 h to grow $200 \AA$ of $\mathrm{SiO}_{2}$ on silicon at $950^{\circ} \mathrm{C}$. How long would it take to grow the $200 \stackrel{\circ}{\mathrm{~A}}$ of $\mathrm{SiO}_{2}$ at $1,000^{\circ} \mathrm{C}$ ? Assume the activation energy for the growth rate is $Q=2.0 \mathrm{eV}$.

## Solution

The reaction rate constant $k$ at $1,000^{\circ} \mathrm{C}$ is expected to take the form:

$$
\begin{aligned}
k(T)= & k_{0}\left[-\frac{Q}{K_{B}}\left(\frac{1}{T}-\frac{1}{T_{0}}\right)\right]=1.0 \\
& \times 10^{4} \frac{\AA^{2}}{\mathrm{~h}} \exp \left[-\frac{2.0 \mathrm{eV}}{8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}}\left(\frac{1}{(1,000+273) \mathrm{K}}-\frac{1}{(950+273 \mathrm{~K})}\right)\right] \\
= & 2.1 \times 10^{4} \frac{\AA^{2}}{\mathrm{~h}}
\end{aligned}
$$

Therefore, the time at $1,000{ }^{\circ} \mathrm{C}$ to grow $200 \stackrel{\circ}{\mathrm{~A}}$ of $\mathrm{SiO}_{2}$ would be:

$$
t=\frac{x^{2}}{t}=\frac{\left(200 \stackrel{\circ}{\mathrm{~A}}\right)^{2}}{2.1 \times 10^{4} \frac{\AA^{2}}{\mathrm{~h}}}=1.9 \mathrm{~h}
$$# 13.1.3 Logarithmic Oxide-Growth Region 

In the logarithmic oxide-growth region, one assumes that the growth rate saturates with time. Thus, the growth rate is assumed to be inversely proportional to the growth time $t$ and directly proportional to the reaction rate constant $k_{3}$, which is temperature dependent:

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{k_{3}}{t+t_{0}}
$$

where

$$
k_{3}=k_{30} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)
$$

Separating variables in Eq. (13.95) and integrating, one obtains:

$$
\int_{t_{0}}^{x} \mathrm{~d} x=k_{3} \int_{t_{0}}^{t} \frac{\mathrm{~d} t}{t+t_{0}}
$$

giving,

$$
x=x_{0}+k_{3} \ln \left(\frac{t+t_{0}}{2 t_{0}}\right)
$$

where,

$$
k_{3}=k_{30} \exp \left(-\frac{Q}{K_{\mathrm{B}} T}\right)
$$

Setting $t=\mathrm{TF}$, when $x=x_{\text {crit }}$, then the time-to-failure equation becomes:

$$
\mathrm{TF}=t_{0}\left\{2 \exp \left[A_{30} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)\right]-1\right\}
$$

where,

$$
A_{30}=\frac{x_{\text {crit }}-x_{0}}{k_{30}}
$$

Another way of writing Eq. (13.105), for easier parameter extraction/determination, is$$
\ln \left[\frac{T F+t_{0}}{2 t_{0}}\right]=A_{30} \exp \left(\frac{Q}{K_{\mathrm{B}} T}\right)
$$

where it is assumed $t_{0}$ is not equal to zero.

# 13.2 Wet Corrosion 

Wet corrosion (or electrolytic corrosion) is significantly different from dry corrosion in that metal hydroxides $\mathrm{M}(\mathrm{OH})_{\mathrm{n}}$ tend to form during wet oxidation (in aerated water) at relatively low temperatures, whereas metal oxides $\left(\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}\right)$ tend to form during dry oxidation at relatively high temperatures.

The formation of metal hydroxides during wet corrosion is a critically important difference-whereas metal oxides generally do not dissolve easily in water, metal hydroxides can dissolve relatively easily in water and thereby constantly exposing fresh metal for continued oxidation. While metal dry oxidation is normally an issue only at elevated temperatures, wet corrosion may occur easily at room temperature.

The critical features of wet corrosion are illustrated in Fig. 13.45. For wet corrosion to occur, one needs the four key elements of an electrolytic cell to exist:


Fig. 13.45 Metal wet-corrosion (corrosion in aerated water) results in an metal-hydroxide $\left[\mathrm{M}_{\mathrm{x}}(\mathrm{OH})_{\mathrm{y}}\right]$ formation on the surface of the metal. Metal hydroxides can dissolve in water, thus exposing fresh metal for continued corrosion. Certain regions in the metal can become anodic, relative to other locations, depending on mechanical stress differences, grain size differences, impurity concentration differences, impressed potentials, etc.an anode (where oxidation can occur), a cathode (where reduction can occur), a conductor (for electrons to flow) and an electrolyte (for the ions to flow).

With no protective oxide formation, which could serve to limit the corrosion rate, the corrosion rate is generally expressed as a linear corrosion rate with:

$$
\mathrm{TF}=A_{0} \exp \left(\frac{Q}{K_{B} T}\right)
$$

The prefactor $A_{0}$ can be a strong function of the concentration of any corrosive contaminants (e.g., chlorine or fluorine) in the water and a function of the acidity ( pH level) of the water.

# 13.2.1 Galvanic Series 

When dissimilar metals are connected electrically, three elements of the corrosion cell are assured: anode, cathode and conductor. Usually impure water (e.g., sea water) or water vapor, with chloride or fluoride contaminants, can provide the fourth key element (electrolyte) for the corrosion cell to work. The connection of two dissimilar materials can be described as a Galvanic couple. The corrosion potential of the couple is described by the potential difference between the two elements forming the couple. The standard electrode potentials (relative to the hydrogen electrode) of several elements are shown in Table 13.6.

Table 13.6 Standard electrode potentials

| Metal | Oxidation state | Standard electrode potential: $\mathrm{V}_{0}$ (Volts) |  |
| :--: | :--: | :--: | :--: |
| Mg | $\mathrm{Mg}^{2+}+2 \mathrm{e}$ | $-2.36$ | More Anodic |
| Al | $\mathrm{Al}^{3+}+3 \mathrm{e}$ | $-1.66$ |  |
| Zn | $\mathrm{Zn}^{2+}+2 \mathrm{e}$ | $-0.76$ |  |
| Cr | $\mathrm{Cr}^{3+}+3 \mathrm{e}$ | $-0.74$ |  |
| Fe | $\mathrm{Fe}^{2+}+2 \mathrm{e}$ | $-0.44$ |  |
| Cd | $\mathrm{Cd}^{2+}+2 \mathrm{e}$ | $-0.40$ |  |
| Co | $\mathrm{Co}^{2+}+2 \mathrm{e}$ | $-0.28$ |  |
| Ni | $\mathrm{Ni}^{2+}+2 \mathrm{e}$ | $-0.25$ |  |
| Sn | $\mathrm{Sn}^{2+}+2 \mathrm{e}$ | $-0.14$ |  |
| Pb | $\mathrm{Pb}^{2+}+2 \mathrm{e}$ | $-0.13$ | $\uparrow$ |
| $\mathrm{H}_{2}$ | $2 \mathrm{H}^{+}+2 \mathrm{e}$ | 0.00 | Reference Electrode |
| Cu | $\mathrm{Cu}^{2+}+2 \mathrm{e}$ | 0.34 | $\downarrow$ |
| Ag | $\mathrm{Ag}^{+}+\mathrm{e}$ | 0.80 |  |
| Pd | $\mathrm{Pd}^{2+}+2 \mathrm{e}$ | 0.99 |  |
| Pt | $\mathrm{Pt}^{2+}+2 \mathrm{e}$ | 1.20 |  |
| Au | $\mathrm{Au}^{3+}+3 \mathrm{e}$ | 1.50 | More Cathodic |For a Galvanic couple, under standard conditions (1-atmosphere, 1-molar solution, $25^{\circ} \mathrm{C}$ ) the driving force is the free energy difference per ion $\Delta G$, given by:

$$
\Delta G=(z e) \Delta V_{0}
$$

where $\Delta V_{0}$ is the difference in standard electrode potentials, $z$ is the ionic charge state and $e$ is the electron charge. A Galvanic couple composed of Fe and Cu can potentially produce a large free energy reduction per oxidized Fe-ion:

$$
\Delta G=(2 e)[-0.44-(+0.34)]=-1.56 \mathrm{eV}
$$

This is a very strong driving potential for corrosion to occur. The corrosion rate (thickness $x$ of Fe impacted per unit time $t$ ) is given by:

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{(\text { Mole })_{\mathrm{wt}}}{\rho}\left(\frac{\mathfrak{I}}{z F}\right)
$$

where (Mole) $)_{\text {wt }}$ is the molecular weight of $\mathrm{Fe}, \rho$ is the density of iron, $z(=2)$ is the charge transferred during Fe oxidation, $F$ is Faraday's constant ( $96,500 \mathrm{C} / \mathrm{mol}$ ), and $\mathfrak{I}$ is the current density (current per unit corroded area). In general, one can write the previous equation as:

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=A_{0} \Im(t)
$$

One can see that the corrosion rate (metal thickness corroded per unit time) is dependent on the corrosion current density $\mathfrak{I}$. For a constant corrosion current, the corrosion rate may be much faster in a small area and thus can form a corrosion pit. Also, time-to-failure equations can be extracted, as done in Sects. 13.1.1, 13.1.2 and 13.1.3), when the current density $\Im(t)$ is specified as a function of time:

$$
\int_{0}^{x} \mathrm{~d} x=A_{0} \int_{0}^{\mathrm{TF}} \Im(t) \mathrm{d} t
$$

# 13.3 Humidity-Induced Oxidation/Reduction 

Many examples of corrosion cannot be described simply as either dry oxidation or wet oxidation. For many cases of corrosion, the process can be described more accurately as humidity-induced oxidation/reduction. When a metal atom oxidizes,

Fig. 13.46 Under light exposure, a photovoltaic-induced voltage of $\sim 0.7 \mathrm{~V}$ is created because of a $\mathrm{p} / \mathrm{n}$ junction in the silicon (to which the metal is connected). Due to this impressed potential, and with the presence of humidity, the Cu will oxidize in the anode contact region $\left(\mathrm{Cu} \rightarrow \mathrm{Cu}^{2+}+2 e\right)$ and then the Cu ions will migrate to the cathode contact region for reduction and redeposition $\left(\mathrm{Cu}^{2+}\right.$ $+2 e \rightarrow \mathrm{Cu}$ ). The Cu -ion mobility along the oxide free surface (and thus the Cu oxidation/ reduction rate) is very sensitive to the $\%$ relative humidity $(\% \mathrm{RH})$
gives up its conduction electrons at the anode region of the metal, the metal ion must be able to diffuse away from the corroded region for the corrosion process to continue; otherwise, the local electric potential will increase thus offsetting the chemical potential for oxidation. An example of humidity-induced oxidation/ reduction is shown in Fig. 13.46 for an IC during chip fabrication.

As discussed in Chap. 11 (corrosion of integrated circuits), the mobility on an oxide surface increases exponentially with humidity (from 20 to $80 \%$ ) and exponentially with temperature. Thus the time-to-failure equation for metal corrosion under humid conditions can be written as:

$$
\mathrm{TF}=A_{0} \exp \left[-a \cdot(\% \mathrm{RH})+\frac{Q}{K_{\mathrm{B}} T}\right]
$$

where $a$ and $Q$ are the corrosion time-to-failure kinetics.
The coefficient $A_{0}$ in Eq. (13.114) can be a strong function of any corrosive contamination (e.g., chlorides or fluorides) present on the surface of the metal. Chlorides and fluorides are particularly important because they tend to reduce the metal-oxide layer which is trying to serve as a self-protection layer.# Example Problem 15 

During IC processing, Cu oxidation of the type shown in Fig. 13.46 can occur while exposed Cu surface is waiting for dielectric-barrier/passivation deposition. To minimize such occurrences of exposed-Cu oxidation, the processing time window is normally kept short. If the normal/safe processing window is 4 h at $45 \%$ relative humidity, how much longer would the processing window be at $35 \% \mathrm{RH}$ ? Assume an exponential humidity dependence with parameter $a=0.12 / \% \mathrm{RH}$.

## Solution

The acceleration factor becomes:

$$
\begin{aligned}
\mathrm{AF} & =\exp \left[a\left(\% \mathrm{RH}_{1}-\% \mathrm{RH}_{2}\right)\right] \\
& =\exp \left[\frac{0.12}{\% \mathrm{RH}}(45 \% \mathrm{RH}-35 \% \mathrm{RH})\right] \\
& =3.32
\end{aligned}
$$

Therefore, the time window at $35 \% \mathrm{RH}$ becomes:

$$
\begin{aligned}
\text { Time }_{@ 35 \% \mathrm{RH}} & =\mathrm{AF} \cdot \text { Time }_{@ 45 \% \mathrm{RH}} \\
& =3.32(4 \mathrm{~h}) \\
& =13.3 \mathrm{~h}
\end{aligned}
$$

### 13.4 Impact of Stress on Corrosion Rates

Mechanical stress can have a strong impact on the rate of corrosion. Regions of relatively-high tensile stress will generally corrode more rapidly. This is illustrated in Fig. 13.47. The upper convex curvature of a bent piece of metal is under tension


Fig. 13.47 Simple bending, as shown, produces a top surface under tension and a bottom surface under compression. The neutral stress region is also shown. The corrosion rate will be the greatest on the top surface where the tensile stress is the greatest. This is because the tensile stress serves to stretch the bonds, making the existing bonds less stable and more prone to oxidationwhile the lower surface is under compression. This mechanical stress reduces the normal bonding energy of the atoms thus making oxidation/corrosion of the atoms more likely to occur.

For humidity-driven corrosion of metals, regions of higher stress generally have higher corrosion rates. As we have done many times in Chap. 11, let us try to describe the corrosion rate constant (dependence on mechanical stress $\sigma$ in the metal) as a power-law:

$$
k(\sigma, \% \mathrm{RH}, T)=k_{0}\left(\% \mathrm{RH}, T\right)\left(1+b \sigma^{m}\right)
$$

One will note in Eq. (13.115) that, even when the mechanical stress $\sigma$ in the material goes to zero, the metal-oxidation rate constant simply reverts to its $k_{0}$ value. This is because metals are expected to oxidize even in a stress-free state. However, with the addition of mechanical stress in the metal, the corrosion rate constant is expected to increase. From the corrosion rate constant, Eq. (13.115), one can now extract the time-to-failure equation:

$$
\operatorname{TF}(\sigma, \% \mathrm{RH}, T)=A_{0}\left(1+a_{0} \sigma^{m}\right)^{-1} \exp \left[(-a \cdot(\% \mathrm{RH})+\frac{Q}{K_{\mathrm{B}} T}\right]
$$

If the piece of metal in Fig. 13.47 is plastically deformed, such that a bend is still evident after the stress is removed, then the bent region will corrode faster. This is illustrated in Fig. 13.48 where a chain-link fence is shown. Note that the highest corrosion rate occurs at the bends where the plastic deformation is the greatest. This is the region where the bonds have been stretched the greatest making them less stable and more prone to oxidation.

Fig. 13.48 Higher stress regions (and more plastic deformation) occur at the crossover bending points of this chain-link fence. Note the enhanced corrosion rates at these crossover/bent-wire locations. Also note that for each bend, the top surface (in tension) generally shows more corrosion than does the underneath surface (in compression)


Fig. 13.49 Corrosion tends to occur along existing grain boundaries and/or cracks, especially in tensile stress regions. If the oxide volume is larger than the metal consumed, then the metal-oxide formation can act like a wedge thus causing the crack tip to come under additional stress and thus accelerating the crack propagation. Assuming that the metal oxide formed is rather porous, then the growth of the metal-oxide along the crack will continue and this will continue to exacerbate the normal crack growth rate process. Similar oxidation processes can also accelerate fatigue

For permanent bends (as shown in the chain-link fence in Fig. 13.48) the amount of plastic deformation in the metal will be assumed to be proportional to the radius of curvature $R$ for the bend, producing a time-to-failure equation which can be written as:

$$
\operatorname{TF}(\sigma, R, T)=A_{0}\left[1+c_{0}\left(\frac{1}{R}\right)^{m}\right]^{-1} \exp \left[-a \cdot(\% \mathrm{RH})+\frac{Q}{K_{\mathrm{B}} T}\right]
$$

Corrosion can also enhance the crack growth rate in stressed materials. As noted earlier, the volume of the oxide can be much greater than the metal consumed thus creating additional stress at the site of the crack. If a porous oxide formation is assumed, such that the corrosion can continue, then the oxide formed will increase the mechanical stress at the crack tip and will tend to accelerate crack growth. This is illustrated in Fig. 13.49.

# Problems 

1. Two atoms are bonded and the bonding potential can be described by the $(9,1)$ bonding potential, with an equilibrium bond energy 3.0 eV and equilibrium bonding distance of $2.0 \AA$. Calculate the value of the spring/stiffness constant for small relative displacements of the two atoms.
Answer: $6.75 \mathrm{eV} /(\AA)^{2}=108 \mathrm{~N} / \mathrm{m}$2. The bond energy for two atoms is 2.2 eV and the equilibrium bond distance is $1.9 \AA$. Assuming that the bond can be described by a $(9,2)$ bonding potential:
(a) What is the maximum tensile force that the bond can support?
(b) What is the maximum bond extension, from equilibrium bonding distance, before the bond fails?
Answers: a) $1.24 \mathrm{eV} / \AA=1.98 \times 10^{-4}$ dynes b) $0.36 \AA$
3. If the Young's modulus for a solid material is $E=500 \mathrm{GPa}$, what is the estimated single-bond energy for two atoms in the solid? Assume that the bonding can be described by the $(9,2)$ potential with an equilibrium bonding distance for the two atoms of $2 \AA$.
Answer: $222 \mathrm{GPa}\left(\AA^{3}\right)^{3}=1.4 \mathrm{eV}$
4. If the Young's modulus of a solid material is $E=250 \mathrm{GPa}$, estimate the elastic energy density in the material when the material is tensile strained by $1 \%(\varepsilon=$ $\Delta L / L_{0}=0.01)$.
Answer: $1.25 \times 10^{-2} \mathrm{GPa}=7.81 \times 10^{19} \mathrm{eV} / \mathrm{cm}^{3}$
5. The stress-strain curve for a material with modulus of $E=400 \mathrm{GPa}$ is very similar to that shown in Fig. 13.14. If the elastic region extends to $1 \%$ strain and the fracture strain is $22 \%$, then calculate the toughness of this material. Assume that the power-law model, which describes the stress versus strain relation in the plastic region, is given by $n=0.3$.
Answer: $1.7 \mathrm{GPa}=1.1 \times 10^{22} \mathrm{eV} / \mathrm{cm}^{3}$
6. Using the vacancy density results from Example Problem 4, show that the flux $J$ of vacancies, described by Eq. (4.10), has an activation energy of $Q=$ $(Q)_{\text {formation }}+(Q)_{\text {diffusion }}$.
7. Creep can occur in metals due to dislocation movement along slip planes due to shear stress. If a pure tensile stress $\sigma_{T}$ is applied, as illustrated in Fig. 13.10, then a shearing stress $\tau$ is generated: $\tau=\sigma \sin (\theta) \cos (\theta)$. Show that the maximum shear stress occurs at $\theta=45^{\circ}$.
8. Creep, under constant tensile-stress conditions, can be an important failure mechanism for gas turbines due to high angular speeds and high temperatures during operation. To make sure that the turbine blades can withstand the expected creep, a random selection of turbines was stressed to failure by using an angular speed of $2 \times$ the expected operation conditions and at a temperature of $800^{\circ} \mathrm{C}$ versus the expected operating temperature of $600^{\circ} \mathrm{C}$. The turbines started to fail after one week under these accelerated conditions. How long would the turbine blades be expected to last (due to creep) at the expected operational conditions? Assume a creep exponent of at least $n=4$, an activation energy of at least 1.2 eV , and all stresses are well above the yield strength of the material.

Answer: 96 years9. Creep, under constant strain, can be an important failure mechanism for clamps/ fasteners. To make sure that a clamp is reliable at $200^{\circ} \mathrm{C}$, accelerated data was taken for clamps tightened to 2 X their normal stress level while stored at $300^{\circ} \mathrm{C}$. The clamps lose their effectiveness after one week under these accelerated conditions. Find the time-to-failure for the clamps under the operational conditions at $200^{\circ} \mathrm{C}$. Assume a creep exponent of at least $n=4$, an activation energy of at least 1.2 eV and that all stresses are well above the yield point of the material.

Answer: 26 years
10. Time-zero cracks are found on the outside of a stainless steel storage vessel. If the depth of the cracks is 20 mm , determine if fast facture is expected as the vessel is pressurized to a level such that 400 MPa of tensile stress exists in the metal. Assume that the stress concentration factor for the stainless steel is $K_{\text {crit }}=$ $75\left(\mathrm{MN} / \mathrm{m}^{3 / 2}\right)$.

Answer: Yes, since $400 \mathrm{MPa}>\sigma_{\text {rupture }}=299 \mathrm{MPa}$, fast rupture is expected as the vessel is being pressurized.
11. Aluminum-alloy rods were randomly selected and ramped-to-rupture at the intended use temperature with a linear ramp rate of tensile stress of $50 \mathrm{MPa} /$ day. The breakdown distribution was described by a Weibull distribution with $\left(\sigma_{\text {rupture }}\right)_{63}=600 \mathrm{MPa}$ and a Weibull slope of $\beta=6$. Assuming that the tensile stress during normal operation is $\sigma_{\mathrm{op}}=100 \mathrm{MPa}$, a time-to-failure power-law with a stress exponent of $n=6$, and that the aluminum-alloy has no well defined yield point:
(a) What fraction of the Al-alloy rods will fail immediately ( $<0.3$ day) when loaded with a tensile stress of 100 MPa ?
(b) What fraction of the Al-alloy rods will fail after 10 years with a 100 MPa loading?

Answers: a) $0.0021 \%$ b) $7 \%$
12. In a certain batch of the aluminum-alloy rods, described in problem 11, some of the rods were found to have small cracks. While the characteristic rupture strength $\left(\sigma_{\text {rupture }}\right)_{63}=600 \mathrm{MPa}$ showed little/no change, the Weibull slope $\beta$ degraded to 4 . Assuming that the tensile stress during normal operation is $\sigma_{\text {op }}=$ 100 MPa and a time-to-failure power-law with a stress exponent of $n=6$ for the aluminum-alloy:
(a) What fraction of the metal rods will fail immediately ( $<0.3$ day) when loaded with a tensile stress of 100 MPa ?
(b) What fraction of the metal rods will fail after 10 years with a 100 MPa loading?

Answers: a) $0.08 \%$ b) $16 \%$13. Steel rods were selected for a high-temperature and high tensile-stress application. During a ramp-testing determination of the rupture strength of steel, at the intended application temperature of $600{ }^{\circ} \mathrm{C}$ and with a ramp rate of $200 \mathrm{MPa} /$ day, the following data was obtained: $\left(\sigma_{\text {rupture }}\right)_{63}=1,600 \mathrm{MPa}$ and $\beta_{\text {rupture }}=10$. The yield strength of the steel is 600 MPa and the intended application is 700 MPa . Assuming a time-to-failure power-law with a stress exponent of $n=6$ :
(a) What fraction of the metal rods will fail immediately ( $<0.07$ day) when loaded with a tensile stress of 700 MPa ?
(b) What fraction of the metal rods will fail after 10 years with a 700 MPa loading?

Answers: a) $0.03 \%$ b) $0.8 \%$
14. On a certain batch of steel rods described in Problem 13, small cracks were discovered on some of the rods. While the characteristic Weibull strength $\left(\sigma_{\text {rupture }}\right)_{63}=1,600 \mathrm{MPa}$ was virtually unchanged, the Weibull slope degraded to $\beta=6$. The yield strength of the steel is 600 MPa and the intended application is 700 MPa . Assuming a time-to-failure power-law with a stress exponent of $n=6$ :
(a) What fraction of the metal rods will fail immediately ( $<0.07$ day) when loaded with a tensile stress of 700 MPa ?
(b) What fraction of the metal rods will fail after 10 years with a 700 MPa loading?

Answers: a) $0.7 \%$ b) $5.3 \%$
15. Metal poles, that are intended to support signs, undergo continual cyclical stressing at the base plate due to changing wind conditions. To better understand their reliability, such poles were randomly selected for cyclical stress testing. Under an accelerating cyclical stress of $\Delta \sigma=800 \mathrm{MPa}$, the poles started to crack at the base plate after 5,000 cycles. How many cycles are the poles expected to last at the effective operating condition of $\Delta \sigma=200 \mathrm{MPa}$ ? Assume $m=4$.

Answer: $1.28 \times 10^{6}$ cycles.
16. The poles described in Problem 15 will be used to support an extended sign which puts a mean stress tensile stress of 200 MPa in addition to cyclical stress of $\Delta \sigma=200 \mathrm{MPa}$. Assuming that the tensile strength in these poles is $\sigma_{\mathrm{TS}}=$ 800 MPa , calculate the expected number of cycles to failure.

Assume $m=4$.
Answer: $4.0 \times 10^{5}$ cycles
17. A metal rod has a thermal expansion coefficient of $\alpha=24 \times 10^{-6} /{ }^{\circ} \mathrm{C}$ and a modulus of $\mathrm{E}=70 \mathrm{GPa}$.
(a) If the metal rod is free to expand from $25^{\circ} \mathrm{C}$ to $300^{\circ} \mathrm{C}$, what fractional change in rod length would be expected?(b) If the rod is fully constrained (cannot move), how much thermal stress would be generated in the rod?

Answers: a) $0.66 \%$ b) 462 MPa
18. A metal component, in a certain application, will be thermal cycled from room temp to an oxidizing ambient of $300^{\circ} \mathrm{C}$. To prevent oxidation of the metal at the high temperatures, a thin ceramic coating is used on the metal component. The concern is that cracks will develop in the ceramic layer during thermal cycling thus exposing the metal to oxidation. To accelerate the cracking, the components were thermal cycled from room temperature to $600^{\circ} \mathrm{C}$. If cracks start to develop in the ceramic layer after 500 thermal cycles, how many crack-free cycles would one expect from room temp to $300^{\circ} \mathrm{C}$ ? Assume that the ceramic material is hard/ brittle with a temperature-cycling power-law exponent of $m=9$.

Answer: 382,000 cycles
19. If left unprotected, how much faster will a scratch in the paint of your new car oxidize at 80 vs. $40 \%$ relative humidity. Assume an exponential model with parameter: $a=0.12 \% \mathrm{RH}$.

Answer: 122 times faster

# Bibliography 

## Materials Science

Ashby, M. and D. Jones: Engineering Materials, 2nd Edition, Butterworth/Heinemann Publishers, (1980).

Ashby, M. and D. Jones: Engineering Materials 1, Elsevier Publishing, (2005).
Askeland, D.: The Science and Engineering of Materials, 3rd Edition, PWS Publishing Company, (1994).

Barrett, C., W. Nix and A. Tetelman: The Principles of Engineering Materials, Prentice Hall, (1973).

Callister, W.: Materials Science and Engineering an Introduction, John Wiley and Sons, (2003). Jastrzebski Z.: The Nature and Properties of Engineering Materials, 2nd Edition, John Wiley and Sons, (1976).
Keyser, C.: Materials Science in Engineering, 3rd Edition, Charles E. Merril Publishing, (1980). Ralls, K., T. Courtney, and J. Wulff: Introduction to Materials Science and Engineering, John Wiley and Sons, (1976).
Ruoff, A.: Introduction to Materials Science, Prentice-Hall, (1972).
Tu, K., J. Mayer, and L. Feldman: Electronic Thin Film Science For Electrical Engineers and Materials Science, Macmillan Publishing Company, (1992).# Mechanics of Materials 

Bedford, A. and K. Liechti: Mechanics of Materials, Prentice Hall, (2000).
Eisenberg, M.: Introduction to the Mechanics of Solids, Addison-Wesley Publishing, (1980).
Gere, J.: Mechanics of Materials, 5th Edition, Brooks/Cole Publishing, (2001).

## Fracture Mechanics

Anderson, T.: Fracture Mechanics, 2nd Edition, CRC Press, (1995).
Dunn, C. and J. McPherson: Temperature Cycling Acceleration Factors for Aluminum Metallization Failure in VLSI Applications, IEEE International Reliability Physics Symposium, 252 (1990).
Griffith, A.: The Phenomena of Rupture and Flow in Solids, Philosophical Transactions, Series A, Vol. 221, pp. 163-198, (1920).
Hertzberg, R.: Fracture Mechanics and Engineering Materials, John Wiley and Sons, (1996).
Irwin, G.: Fracture Dynamics, Fracturing of Metals, American Society for Metals, Cleveland, pp. 147-166, (1948).
Stokes, R. and D. Evans: Fundamentals of Interfacial Engineering, Wiley-VCH, (1997).

## Physical Chemistry

Atkins, P.: Physical Chemistry, 5th Edition, W.H Freeman and Company, New York, (1994).
Engel, T. and P. Reid: Physical Chemistry, Pearson \& Benjamin Cummings, (2006).
McPherson, J.: Determination of the Nature of Molecular Bonding in Silica from Time-Dependent Dielectric Breakdown Data, J. Appl. Physics, 95, 8101 (2004).
Pauling, L.: The Nature of the Chemical Bond, 3rd Edition, Cornel University Press, (1960).
Silbey, R. and R. Alberty: Physical Chemistry, 3rd Edition, John Wiley and Sons (2001).

## Solid State Physics

Ashcroft, N. and David Mermin: Solid State Physics, Harcourt Brace College Publishers, (1976). Blakemore, J.: Solid State Physics, 2nd Edition, Cambridge University Press, (1985).
Kittel, C.: Introduction to Solid State Physics, 7th Edition, John Wiley and Sons, (1996).
McPherson, J.: Underlying Physics of the Thermochemical E-Model in Describing Low-Field
Time-Dependent Dielectric Breakdown in SiO2 Thin Films, J. Appl. Physics, 84, 1513 (1998).
Turton, R.: The Physics of Solids, Oxford University Press, (2000).

## Quantum Mechanics

Atkins, P. and R. Friedman: Molecular Quantum Mechanics, 3rd Edition, Oxford University Press, (1997).Dirac, P.: The Principles of Quantum Mechanics, 4th Edition, Oxford Science Publications, (1958). Griffiths, D.: Introduction to Quantum Mechanics, Prentice Hall, (1995).
Harrison, W.: Applied Quantum Mechanics, World Scientific Publishing, (2000).
McPherson, J.: Quantum Mechanical Treatment of Si-O Bond Breakage in Silica Under TimeDependent Dielectric Breakdown, IEEE International Reliability Physics Symposium, 209 (2007).
Robinett, R.: Quantum Mechanics, 2nd Edition, Oxford University Press, (2006).
Shift, L.: Quantum Mechanics, McGraw-Hill Book Company, (1949).

# Semiconductors and Dielectrics 

Dumin, D.: Oxide Reliability, A Summary of Silicon Oxide Wearout, Breakdown, and Reliability, World Scientific, (2002).
Grove, A.: Physics and Technology of Semiconductor Devices, John Wiley and Sons, (1967).
Matare, H.: Defect Electronics in Semiconductors, Wiley-Interscience, (1971).
Streetman, B. and S. Banerjee: Solid State Electronic Devices, 5th Edition, Prentice Hall, (2000).
Sze, S.: Physics of Semiconductor Devices, 2nd Edition, John Wiley and Sons, (1981).
Sze, S.: Semiconductor Devices: Physics and Technology, 2nd Edition, John Wiley and Sons, (2002).

## Thermodynamics and Statistical Mechanics

Desloge, E.: Statistical Physics, Holt, Riehart and Winston, (1966).
Haase, R.: Thermodynamics of Irreversible Processes, Dover Publications, (1969).
Kittel, C. and H. Kroemer: Thermal Physics, 2nd Edition, W.H. Freeman and Co., (1980).
Schrodinger, E.: Statistical Thermodynamics, Dover Publications, (1952).# Chapter 14 <br> Conversion of Dynamical Stresses into Effective Static Values 

The time-to-failure models which were developed in the previous chapters assume that the stress remains constant with time until the material fails. Even when we discussed fatigue (a failure mechanism caused by a cyclical stress), it was assumed that the stress range $\Delta \sigma$ remained constant with time. However, seldom is the applied stress constant with time, as illustrated in Fig. 14.1. In integrated circuits, the currents and fields are continually changing during operation and generally depend on the frequency of operation. In mechanical devices, the mechanical stress usually varies with time (the mechanical stress in a metal light pole changes with wind direction and with wind speed while the mechanical stress in the shaft of a rotor changes with the number of rpm ). Therefore, a question naturally arises: how does one convert dynamical stresses (time-dependent stresses) $\xi(t)$ into an effective static form $\xi_{\text {effective }}$ so that all of the previously developed time-to-failure models can be used? This chapter presents a methodology for that conversion.

## 1 Effective Static-Stress Equivalent Values

Figure 14.2 illustrates a dynamical (time-dependent) stress $\xi(t)$ : Also shown is an effective static-stress equivalent $\xi_{\text {effective }}$. We want to determine $\xi_{\text {effective }}$ such that it will produce an equivalent amount of material/device degradation and thus the same time-to-failure as the dynamical stress $\xi(t)$ :

One would expect that when $\xi(t)>\xi_{\text {effective }}$; then the actual degradation rate for the material/device during this time interval will be accelerated relative to degradation rate at $\xi_{\text {effective }}$ : However, when $\xi(t)<\xi_{\text {effective }}$ the actual degradation rate for the material/device during this time interval will be decelerated relative to degradation rate at $\xi_{\text {effective }}$.

The time is either accelerated or decelerated, depending on whether the actual stress level $\xi(t)$ is above or below the constant $\xi_{\text {effective }}$ value. If one compares an increment of time $\mathrm{d} t^{\prime}$ under constant stress $\xi_{\text {effective }}$ with an increment of time

Fig. 14.1 Example of a dynamical (time-dependent) stress is illustrated. It will be assumed that the stress amplitudes are sufficiently low that they only accelerate the normal physics-of-failure - they do not change the normal physics-of-failure


Fig. 14.2 Dynamical (time-dependent) stress $\xi(t)$ is shown. $\xi_{\text {effective }}$ represents the effective staticstress level that would produce the same amount of material/device degradation and same time-tofailure as would the dynamical stress $\xi(t)$ : If the dynamical stress is also periodic, as shown, then only the first period is needed in the $\xi_{\text {effective }}$ determination
$\mathrm{d} t$ under actual accelerated/decelerated conditions, then the following equation must hold:

$$
\mathrm{d} t^{\prime}=\mathrm{AF}_{\xi(t), \xi_{\text {effective }}} \mathrm{d} t
$$If one integrates both sides of the above equation from $t=0$ to $t=\mathrm{TF}$, then one obtains:

$$
\mathrm{TF}=\int_{0}^{\mathrm{TF}} \mathrm{AF}_{\xi(t), \xi_{\text {effective }}} \mathrm{d} t
$$

Thus, the compliance equation for dynamical stresses that ensures the material/ device degradation caused by the effective static-stress $\xi_{\text {effective }}$ is identical to the degradation caused by the time-varying stress $\xi(t)$ is given by:

$$
\frac{1}{\mathrm{TF}} \int_{0}^{\mathrm{TF}} \mathrm{AF}_{\xi(t), \xi_{\text {effective }}} \mathrm{d} t=1
$$

If the dynamical stress is periodic, with a period $P$ (as indicated in Fig. 14.2), then we only need to determine $\xi_{\text {effective }}$ over one period (since it will be the same for all other periods). The compliance equation for periodic dynamical stresses becomes:

$$
\frac{1}{P} \int_{0}^{P} \mathrm{AF}_{\xi(t), \xi_{\text {effective }}} \mathrm{d} t=1
$$

As we will see in the remaining sections of this chapter, the compliance equations permit us to determine $\xi_{\text {effective }}$ for arbitrary dynamical conditions.

# 2 Effective Static-Stress Equivalent Values When Using Power-Law TF Models 

The acceleration factor for the power-law TF model is given by:

$$
\mathrm{AF}_{\xi(t), \xi_{\text {effective }}}=\left(\frac{\xi(t)-\xi_{\text {yield }}}{\xi_{\text {effective }}-\xi_{\text {yield }}}\right)^{n}
$$

Substituting the above equation into Eq. (14.4) and solving for $\xi_{\text {effective }}$; one obtains $\xi_{\text {effective }}$ when using the power-law TF model:

$$
\xi_{\text {effective }}-\xi_{\text {yield }}=\left[\frac{1}{P} \int_{0}^{P}\left[\xi(t)-\xi_{\text {yield }}\right]^{n} \mathrm{~d} t\right]^{1 / n}
$$In Eq. (14.6) it will be understood that only when $\xi(t)>\xi_{\text {yield }}$ does damage occur, thus only the values of $\xi(t)>\xi_{\text {yield }}$ should be included in the integral. ${ }^{1}$

# Example Problem 1 

Assuming a power-law time-to-failure model with $n=4$ and a negligibly small yield stress, find the static effective stress $\xi_{\text {effective }}$ for the dynamic stress $\xi(t)$ shown in Fig. 14.2.

## Solution

If the exact functional form of the stress $\xi(t)$ is known, then $n_{\text {effective }}$ can be determined from:

$$
\xi_{\text {effective }}=\left[\frac{1}{P} \int_{0}^{P} \xi^{4}(t) \mathrm{d} t\right]^{1 / 4}
$$

Usually the exact functional form of the stress $\xi(t)$ is not known (as the case here) and has to be approximated. One can use numerical integration to find the area under the curve. However, a much simpler and often-used approach is to simply approximate the area under each lobe of the curve using the peak/ maximum value for height and for the width: use the full-width-at halfmaximum (fwhm). This is the conservative approach that we have used here and is shown in Fig. 14.3.


Fig. 14.3 For dynamical stresses which are roughly Gaussian in shape, the full width at half maximum (fwhm) approach is often used to approximate the area under each lobe (If the pulse is purely Gaussian, with standard deviation $\sigma$, then fwhm $=2.355 \sigma$ )
(continued)

[^0]
[^0]:    ${ }^{1}$ Recall from Chap. 13, if a yield stress truly exists, then when the applied stress is below the yield stress no material degradation is expected.With $n=4$ and the yield stress equal to zero, one obtains:

$$
\begin{aligned}
\xi_{\text {effective }} & =\left[\frac{1}{P} \int_{0}^{P} \xi^{4}(t) \mathrm{d} t\right]^{1 / 4} \\
& \cong\left\{\frac{1}{P}\left[\sum_{i}\left(\xi_{\text {peak }}^{4}\right)_{i}(\Delta t)_{i}\right]\right\}^{1 / 4} \\
& =\left\{\frac{1}{10}\left[(7.5)^{4}(1.5)+(3.2)^{4}(1.5)\right]\right\}^{1 / 4} \\
& =4.7(\text { arbitrary units })
\end{aligned}
$$

In summary, with a power-law exponent of $n=4$, one would expect a constant stress of $\xi_{\text {effective }}=4.7$ (arbitrary units) to produce the same amount of degradation to the material/device as would the dynamical stress $\xi(t)$ and, therefore, produce an equivalent time-to-failure. Usually, the fwhm method is a conservative approach to handling the reliability impact of pulses.

# 3 Effective Static-Stress Equivalent Values When Using Exponential TF Models 

The acceleration factor for the exponential TF model is given by:

$$
\mathrm{AF}_{\xi(t), \xi_{\text {effective }}}=\exp \left\{\gamma\left[\xi(t)-\xi_{\text {effective }}\right]\right\}
$$

Substituting the above equation into Eq. (14.4) and solving for $\xi_{\text {effective }}$; one obtains $\xi_{\text {effective }}$ for the exponential TF model:

$$
\xi_{\text {effective }}=\frac{1}{\gamma} \ln \left\{\frac{1}{P} \int_{0}^{P} \exp [\gamma \xi(t)] \mathrm{d} t\right\}
$$

## Example Problem 2

Assuming an exponential time-to-failure model with $\gamma=2$ (in units of reciprocal stress), find the effective static stress $\xi_{\text {effective }}$ for the dynamic stress $\xi(t)$ shown in Fig. 14.3.# Solution 

Using an exponential time-to-failure model with $\gamma=2$ (in units of reciprocal stress), along with Eq. (14.8) and Fig. 14.3, one can write:

$$
\begin{aligned}
\xi_{\text {effective }} & =\frac{1}{\gamma} \ln \left\{\frac{1}{P} \int_{0}^{P} \exp [\gamma \xi(t)] \mathrm{d} t\right\} \\
& \cong \frac{1}{\gamma} \ln \left\{\frac{1}{P} \sum_{i}(\Delta t)_{i} \exp \left[\gamma\left(\xi_{\text {peak }}\right)_{i}\right]\right\} \\
& =\frac{1}{2} \ln \left\{\frac{1}{10}[(1.5) \exp [2(7.5)]+(1.5) \exp [2(3.2)]\right\} \\
& =6.6
\end{aligned}
$$

In summary, with an exponential time-to-failure model and with $\gamma=2$ (in units of reciprocal stress), we would expect a constant stress of $\xi_{\text {effective }}=6.6$ (arbitrary units) to produce the same amount of material/device degradation and time-to-failure as would the dynamic stress $\xi(t)$ :

## 4 Conversion of a Dynamical Stress Pulse into a Rectangular Pulse Stress Equivalent

It would be very useful if one could somehow convert a rather complicated dynamical stress pulse, over some time interval $t_{a}-t_{b}$, into a rectangular pulse effective stress which would produce an equivalent amount of material/device degradation over this same time interval $t_{a}-t_{\mathrm{b}}$. This is illustrated in Fig. 14.4.

The compliance equation for dynamical stresses can again aid us in developing the effective rectangular pulse stress equivalent of a single dynamical pulse. Since the amount of degradation to the material/device must be equivalent over the region

Fig. 14.4 A single dynamical stress pulse $\xi(t)$ is shown over the time interval $t_{a}-t_{b} . \xi_{\text {effective }}$ represents the effective rectangular pulse, over the same time interval, and is expected to produce an equivalent amount of degradation to the material/ device
$a-b$, then we can restate the compliance equation for the conversion of a dynamic pulse into the rectangular pulse stress equivalent

$$
\frac{1}{\left(t_{b}-t_{a}\right)} \int_{t_{a}}^{t_{b}} \mathrm{AF}_{\xi(t), \xi_{\text {effective }}} \mathrm{d} t=1
$$

# 4.1 Effective Rectangular Pulse Stress-Equivalent Values for Power-Law TF Models 

Since the acceleration factor for the power-law TF model is given by:

$$
\mathrm{AF}_{\xi(t), \xi_{\text {effective }}}=\left(\frac{\xi(t)-\xi_{\text {yield }}}{\xi_{\text {effective }}-\xi_{\text {yield }}}\right)^{n}
$$

the compliance equation yields the effective rectangular pulse stress-equivalent value $\xi_{\text {effective }}$ for the power-law exponential model:

$$
\xi_{\text {effective }}-\xi_{\text {yield }}=\left[\frac{1}{\left(t_{b}-t_{a}\right)} \int_{t_{a}}^{t_{b}}\left[\xi(t)-\xi_{\text {yield }}\right]^{n} \mathrm{~d} t\right]^{1 / n}
$$

In Eq. (14.11) it will be understood that damage only occurs when $\xi(t)>\xi_{\text {yield }}$. Thus, only the values of $\xi(t)>\xi_{\text {yield }}$ should be included in the integral.

### 4.2 Effective Rectangular Pulse Stress-Equivalent Values for Exponential TF Models

Since the acceleration factor for the exponential TF model is given by:

$$
\mathrm{AF}_{\xi(t), \xi_{\text {effective }}}=\exp \left\{\gamma\left[\xi(t)-\xi_{\text {effective }}\right]\right\}
$$

the compliance equation yields the effective rectangular pulse stress-equivalent value $\xi_{\text {effective }}$ for the exponential TF model

$$
\xi_{\text {effective }}=\frac{1}{\gamma} \ln \left\{\frac{1}{t_{b}-t_{a}} \int_{t_{a}}^{t_{b}} \exp [\gamma \xi(t)] \mathrm{d} t\right\}
$$# 4.3 Numerical Integration 

Since the determination of the rectangular pulse stress equivalents of dynamical pulses [Eqs. (14.11) and (14.13)] generally requires the integration of rather complicated functions, a numerical method of integration is suggested.

The Composite Trapezoidal and Simpson's Rule numerical method of integration is illustrated in Fig. 14.5. The method begins by segmenting the total area into $m$ subintervals (of equal spacing) $\Delta t$. The height of each rectangular area is given by $\left[f\left(t_{i}\right)+f\left(t_{i-1}\right)\right] / 2$. Summing the areas of $m$ such rectangles gives:

$$
\int_{a}^{b} f(t) \mathrm{d} t \cong \Delta t \sum_{i=1}^{m}\left[\frac{f\left(t_{i}\right)+f\left(t_{i}-1\right)}{2}\right]=\Delta t \sum_{i=1}^{m} f_{i}
$$

where

$$
\Delta t=\frac{t_{b}-t_{a}}{m} \text { and } f_{i}=\left[\frac{f\left(t_{i}\right)+f\left(t_{i-1}\right)}{2}\right]
$$

This method of numerical integration is illustrated in Fig. 14.5.
Thus, $\xi_{\text {effective }}$ for a rectangular pulse equivalent of a dynamical pulse, using the power-law TF model, becomes:

$$
\begin{aligned}
\xi_{\text {effective }}-\xi_{\text {yield }} & =\left[\frac{1}{\left(t_{b}-t_{a}\right)} \int_{t_{a}}^{t_{b}}\left[\xi(t)-\xi_{\text {yield }}\right]^{n} \mathrm{~d} t\right]^{1 / n} \\
& \cong\left[\frac{\Delta t}{t_{b}-t_{a}} \sum_{i=1}^{m}\left(\xi^{n}\right)_{i}\right]^{1 / n}
\end{aligned}
$$

Fig. 14.5 Numerical integration method is illustrated using the Composite Trapezoidal and Simpson's Rule
where

$$
\left(\xi^{n}\right)_{i}=\frac{\left[\xi\left(t_{i}\right)-\xi_{\text {yield }}\right]^{n}+\left[\xi\left(t_{i-1}\right)-\xi_{\text {yield }}\right]^{n}}{2}
$$

It is understood that damage only occurs when the stress level $\xi(t)$ is greater than $\xi_{\text {yield }}$. Therefore, only values $\xi(t)>\xi_{\text {yield }}$ should be included in the integral/ summations.
$\xi_{\text {effective }}$ for a rectangular pulse stress equivalent of a dynamical pulse, using the exponential model becomes:

$$
\begin{aligned}
\xi_{\text {effective }} & =\frac{1}{\gamma} \ln \left\{\frac{1}{t_{b}-t_{a}} \int_{t_{a}}^{t_{b}} \exp [\gamma \xi(t)] \mathrm{d} t\right\} \\
& \cong \frac{1}{\gamma} \ln \left\{\frac{\Delta t}{t_{b}-t_{a}} \sum_{i=1}^{m}[\exp (\gamma \xi)]_{i}\right\}
\end{aligned}
$$

where

$$
[\exp (\gamma \xi)]_{i}=\frac{\exp \left[\gamma \xi\left(t_{i}\right)\right]+\exp \left[\gamma \xi\left(t_{i-1}\right)\right]}{2}
$$

# Example Problem 3 

Shown in Fig. 14.6 is a dynamic stress pulse given by:

$$
\xi(t)=6 \sin [\pi(t / 5)] \text { (arbitrary units) }
$$

Using numerical integration, divide the pulse area into $m=20$ area segments of equal width $\Delta t=0.25$ and determine the effective rectangular pulse equivalent $\xi_{\text {effective }}$ for the dynamical pulse assuming:
(a) power-law model with $n=4$ and negligibly small yield stress, and
(b) exponential model with $\gamma=2$ (in units of reciprocal stress).

## Solution

(a) For the power-law model (with $n=4$ and $\xi_{\text {yield }}=0$ ) we have:

$$
\begin{aligned}
\xi_{\text {effective }} & =\left[\frac{1}{t_{b}-t_{a}} \int_{t_{a}}^{t_{b}} \xi^{n}(t) \mathrm{d} t\right]^{1 / n} \\
& \cong\left[\frac{\Delta t}{t_{b}-t_{a}} \sum_{i=1}^{m}\left(\xi^{n}\right)_{i}\right]^{1 / n}=\left[\frac{0.25}{5-0} \sum_{i=1}^{20}\left(\xi^{4}\right)_{i}\right]^{1 / 4}
\end{aligned}
$$

(continued)

Fig. 14.6 A single pulse of waveform $\xi(t)=6 \sin [\pi(t / 5)]$ is shown. $\xi_{\text {effective }}$ is an effective rectangular pulse for this dynamical pulse

The details of the numerical integration are shown in the following spreadsheet. In summary, using a power-law TF model with $n=4$, we obtain an effective rectangular pulse value of $\xi_{\text {effective }}=4.70$ (arbitrary units).

$$
\begin{aligned}
\xi(t) & =6 \sin [\pi(t / 5)] \\
t_{b}-t_{a} & =5 \\
m & =20 \\
\Delta t & =\left(\mathrm{t}_{b}-t_{a}\right) / m=0.25 \\
n & =4
\end{aligned}
$$

| $t$ | $\xi(t)$ | $\xi(t)^{4}$ | $\frac{\Delta t}{t_{b}-t_{a}}\left[\frac{\xi^{n}\left(t_{i}\right)+\xi^{n}\left(t_{i-1}\right)}{2}\right]$ |
| :-- | :-- | :-- | :-- |
| 0.00 | 0.00 | 0.00 |  |
| 0.25 | 0.94 | 0.78 | 0.02 |
| 0.50 | 1.85 | 11.82 | 0.31 |
| 0.75 | 2.72 | 55.05 | 1.67 |
| 1.00 | 3.53 | 154.70 | 5.24 |
| 1.25 | 4.24 | 324.00 | 11.97 |
| 1.50 | 4.85 | 555.19 | 21.98 |
| 1.75 | 5.35 | 816.83 | 34.30 |
| 2.00 | 5.71 | $1,060.31$ | 46.93 |
| 2.25 | 5.93 | $1,233.35$ | 57.34 |
| 2.50 | 6.00 | $1,296.00$ | 63.23 || 2.75 | 5.93 | $1,233.34$ | 63.23 |
| :-- | :-- | :-- | :-- |
| 3.00 | 5.71 | $1,060.30$ | 57.34 |
| 3.25 | 5.35 | 816.82 | 46.93 |
| 3.50 | 4.85 | 555.17 | 34.30 |
| 3.75 | 4.24 | 323.99 | 21.98 |
| 4.00 | 3.53 | 154.69 | 11.97 |
| 4.25 | 2.72 | 55.05 | 5.24 |
| 4.50 | 1.85 | 11.82 | 1.67 |
| 4.75 | 0.94 | 0.78 | 0.31 |
| 5.00 | 0.00 | 0.00 | 0.02 |
|  |  |  | Sum $=486.00$ |

$\xi_{\text {effective }}=(\text { Sum })^{(1 / 4)}=4.70$
(b) For the exponential model with $\gamma=2$ (reciprocal stress units):

$$
\begin{aligned}
\xi_{\text {effective }} & =\frac{1}{\gamma} \ln \left\{\frac{1}{t_{b}-t_{a}} \int_{t_{a}}^{t_{b}} \exp [\gamma \xi(t)] \mathrm{d} t\right\} \\
& \cong \frac{1}{\gamma} \ln \left\{\frac{\Delta t}{t_{b}-t_{a}} \sum_{i=1}^{m}[\exp (\gamma \xi)]_{i}\right\} \\
& =\frac{1}{2} \ln \left\{\frac{0.25}{5-0} \sum_{i=1}^{20}[\exp (\gamma \xi)]_{i}\right\}
\end{aligned}
$$

The numerical integration is shown in the spreadsheet below.

$$
\begin{aligned}
\xi(t) & =6 \sin [\pi(t / 5)] \\
t_{b}-t_{a} & =5 \\
m & =20 \\
\Delta t & =\left(t_{b}-t_{a}\right) / m=0.25 \\
\gamma & =2
\end{aligned}
$$

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| $t$ | $\xi(t)$ | $\operatorname{Exp}[\gamma \xi(t)]$ | $\frac{\Delta t}{t_{b}-t_{a}}\left[\frac{\exp \left[\gamma \xi\left(t_{i}\right)\right]+\exp \left[\gamma \xi\left(t_{i-1}\right)\right]}{2}\right]$ |
| 0.00 | 0.00 | 1.00 |  |
| 0.25 | 0.94 | 6.54 | 0.19 |
| 0.50 | 1.85 | 40.78 | 1.18 |
| 0.75 | 2.72 | 232.27 | 6.83 || 1.00 | 3.53 | $1,156.83$ | 34.73 |
| :-- | :-- | :-- | :-- |
| 1.25 | 4.24 | $4,843.04$ | 150.00 |
| 1.50 | 4.85 | $16,452.28$ | 532.38 |
| 1.75 | 5.35 | $44,006.49$ | $1,511.47$ |
| 2.00 | 5.71 | $90,462.36$ | $3,361.72$ |
| 2.25 | 5.93 | $140,402.18$ | $5,771.61$ |
| 2.50 | 6.00 | $162,754.79$ | $7,578.92$ |
| 2.75 | 5.93 | $140,400.24$ | $7,578.88$ |
| 3.00 | 5.71 | $90,459.89$ | $5,771.50$ |
| 3.25 | 5.35 | $44,004.72$ | $3,361.62$ |
| 3.50 | 4.85 | $16,451.43$ | $1,511.40$ |
| 3.75 | 4.24 | $4,842.73$ | 532.35 |
| 4.00 | 3.53 | $1,156.75$ | 149.99 |
| 4.25 | 2.72 | 232.25 | 34.72 |
| 4.50 | 1.85 | 40.78 | 6.83 |
| 4.75 | 0.94 | 6.53 | 1.18 |
| 5.00 | 0.00 | 1.00 | 0.19 |
|  |  |  | Sum $=37,897.69$ |

$\xi_{\text {effective }}=(1 / \gamma) \ln (\mathrm{Sum})=5.27$
In summary, for the exponential model with $\gamma=2$ (reciprocal stress units), $\xi_{\text {effective }}=5.27$ (arbitrary units).

# 5 Effective Static Temperature Equivalents 

Similar to stress, the temperature $T$ of the material/device is not usually constant during device operation. For example, a computer generally runs hotter (higher power dissipation) during heavy number crunching (many computations per sec) versus the sleep mode (a period of relative inactivity). An electrical power transformer (from your local utility company) generally runs hotter in the summer months versus the winter months since the transformer is continuously exposed to the ambient weather conditions. Engine components are obviously much hotter when the engine is running.

Thus, for reliability estimations, it would be very useful to have an effective static temperature $T_{\text {effective }}$ (as illustrated in Fig. 14.7) which produces an equivalent amount of material/device degradation [versus the dynamical temperature $T(t)$ ].

One can use the compliance equation to determine $T_{\text {effective }}$ over any interval $t_{a}-t_{b}:$

$$
\frac{1}{\left(t_{b}-t_{a}\right)} \int_{t_{a}}^{t_{b}} \mathrm{AF}_{T(t), T_{\text {effective }}} \mathrm{d} t=1
$$

Fig. 14.7 The temperature of a device is seldom constant. The effective static temperature $T_{\text {effective }}$ is of great reliability importance
where

$$
\mathrm{AF}_{T(t), T_{\text {effective }}}=\exp \left[\frac{Q}{K_{B}}\left(\frac{1}{T_{\text {effective }}}-\frac{1}{T(t)}\right)\right]
$$

Using Eq. (14.21) and solving Eq. (14.20) for $T_{\text {effective }}$, one obtains:

$$
\begin{aligned}
T_{\text {effective }} & =\frac{-\left(Q / K_{B}\right)}{\ln \left\{\frac{1}{t_{b}-t_{a}} \sum_{t_{a}}^{t_{b}}\left[\exp \left[-\frac{Q}{K_{B} T(t)}\right] \mathrm{d} t\right\}\right.} \\
& \cong \frac{-\left(Q / K_{B}\right)}{\ln \left\{\frac{\Delta t}{t_{b}-t_{a}} \sum_{i=1}^{m}\left[\exp \left(-\frac{Q}{K_{B} T}\right)\right]_{i}\right\}}
\end{aligned}
$$

where

$$
\left[\exp \left(-\frac{Q}{K_{B} T}\right)\right]_{i}=\frac{\exp \left(-\frac{Q}{K_{B} T_{i}}\right)+\exp \left(-\frac{Q}{K_{B} T_{i-1}}\right)}{2}
$$# Example Problem 4 

The time dependence of the temperature shown in Fig. 14.7 is given by:

$$
T(t)=300 \mathrm{~K}+100 \mathrm{~K} \sin \left(\frac{\pi}{5} t\right)
$$

Assuming an activation energy of $\mathrm{Q}=1.0 \mathrm{eV}$, determine the effective static temperature over the time interval from 0 to 5 .

## Solution

Using,

$$
\begin{aligned}
T(t) & =300+100 \sin [\pi(t / 5)] \\
t_{b}-t_{a} & =5 \\
m & =20 \\
\Delta t & =\left(t_{b}-t_{a}\right) / m=0.25 \\
Q & =1 \mathrm{ev} \\
K_{B} & =8.625 \times 10^{-5} \mathrm{eV} / \mathrm{K}
\end{aligned}
$$

the numerical integration is shown in the following spreadsheet.

$$
\begin{aligned}
T(t) & =300+100 \sin [\pi(t / 5)] \\
t_{b}-t_{a} & =5 \\
m & =20 \\
\Delta t & =\left(t_{b}-t_{a}\right) / m=0.25 \\
Q & =1 \mathrm{ev} \\
K_{B} & =8.625 \times 10^{-5} \mathrm{eV} / \mathrm{K}
\end{aligned}
$$

| $t$ | $T(t)$ | $\exp \left[-\frac{Q}{K_{B} T}\right]$ | $\frac{\Delta t}{t_{b}-t_{a}}\left[\frac{\exp \left[\frac{Q}{K_{B} T_{i}}\right]+\exp \left[-\frac{Q}{K_{B} T_{i-1}}\right]}{2}\right]$ |
| :-- | :-- | :-- | :-- |
| 3.75 | 370.71 | $2.61 \mathrm{E}-14$ | $2.16 \mathrm{E}-15$ |
| 4.00 | 358.78 | $9.23 \mathrm{E}-15$ | $8.84 \mathrm{E}-16$ |
| 4.25 | 345.40 | $2.64 \mathrm{E}-15$ | $2.97 \mathrm{E}-16$ |
| 4.50 | 330.90 | $6.07 \mathrm{E}-16$ | $8.12 \mathrm{E}-17$ |
| 4.75 | 315.64 | $1.12 \mathrm{E}-16$ | $1.80 \mathrm{E}-17$ |
| 5.00 | 300.00 | $1.64 \mathrm{E}-17$ | $3.20 \mathrm{E}-18$ |
|  |  |  | $\operatorname{Sum}=7.59 \mathrm{E}-14$ |

$T_{\text {effective }}=-\left(Q / K_{B}\right) / \ln (\mathrm{Sum})=384$
In summary, the effective static temperature is $T_{\text {effective }}=384 \mathrm{~K}=111^{\circ} \mathrm{C}$.# 6 Mission Profiles 

A mission (or use) profile is a succinct description of the intended use conditions for the device throughout its lifetime. It is very important, especially during the design and materials selection phase of a new device, that the mission profile is fully comprehended. Now that we have learned how to convert dynamic stresses into effective static stress equivalents, these can be used for a succinct description of the mission profile expected for the device.

The mission profile describes the expected use conditions for the device during its entire lifetime. An example of a mission profile is shown in Table 14.1. The expected lifetime for the device is 10 years ( 120 months).

If a power-law time-to-failure model is used, then the effective constant-stress value $\xi_{\text {effective }}$ for the entire mission profile becomes:

$$
\begin{aligned}
(\xi)_{\text {effective }}-\xi_{\text {yield }} & =\left[\frac{1}{T F} \int_{0}^{T F}\left[\xi(t)-\xi_{\text {yield }}\right]^{n} \mathrm{~d} t\right]^{1 / n} \\
& \cong\left[\frac{1}{T F} \sum_{i}(\Delta t)_{i}\left[\xi_{(i)}-\xi_{\text {yield }}\right]^{n}\right]^{1 / n} \\
& =\left[\sum_{i}(\mathrm{dyc})_{i}\left[\xi_{(i)}-\xi_{\text {yield }}\right]^{n}\right]^{1 / n}
\end{aligned}
$$

where the duty cycle (dyc) is given by:

$$
(\mathrm{dyc})_{i}=\frac{(\Delta t)_{i}}{\mathrm{TF}}
$$

The duty cycle is simply the fraction of time that the stated stress is active during the expected 10 years ( 120 months) of use. It is understood in Eq. (14.24) that damage only occurs when the stress level $\xi(t)$ is greater than $\xi_{\text {yield }}$. Thus, only values $\xi(t)>\xi_{\text {yield }}$ should be included in the integral/summations.

If an exponential TF model is used, then the effective constant-stress value $\xi_{\text {effective }}$ for the entire mission becomes:

Table 14.1 Stress Mission profile for a device

| Stress: $\xi$ (arbitrary units) | Time (months) | Duty cycle |
| :-- | :-- | :-- |
| $\xi 1$ | 1 | 0.008 |
| $\xi 2$ | 7 | 0.058 |
| $\xi 3$ | 12 | 0.100 |
| $\xi 4$ | 70 | 0.583 |
| $\xi 5$ | 24 | 0.200 |
| $\xi 6$ | 6 | 0.050 |
|  | Sum $=120$ | 1.000 |Table 14.2 Thermal Mission profile for device

| Temp ( C) | Time (months) | Duty cycle |
| :-- | :-- | :-- |
| 180 | 1 | 0.008 |
| 150 | 7 | 0.058 |
| 125 | 12 | 0.100 |
| 95 | 70 | 0.583 |
| 75 | 24 | 0.200 |
| 25 | 6 | 0.050 |
|  | Sum $=120$ | 1.000 |

$$
\begin{aligned}
\xi_{\text {effective }} & =\frac{1}{\gamma} \ln \left\{\frac{1}{\mathrm{TF}} \int_{0}^{\mathrm{TF}} \exp [\gamma \xi(t)] \mathrm{d} t\right\} \\
& \cong \frac{1}{\gamma} \ln \left\{\sum_{i}(\mathrm{dyc})_{i} \exp \left[\gamma \xi_{i}\right]\right\}
\end{aligned}
$$

Similarly, a mission profile can be described for the expected use temperature and is shown in Table 14.2. The expected lifetime for the device is 10 years.

The effective constant-temperature equivalent $T_{\text {eff }}$ for the full 10 years ( 120 months) of device use can be easily determined in terms of the temperature $T_{i}$ for each time interval and its duty cycle (dyc):

$$
\begin{aligned}
T_{\text {effective }} & =\frac{-\left(Q / K_{B}\right)}{\ln \left\{\frac{1}{T F} \int_{t_{a}}^{t_{b}} \exp \left[-\frac{Q}{K_{B} T(t)}\right] \mathrm{d} t\right\}} \\
& \cong \frac{-\left(Q / K_{B}\right)}{\ln \left\{\sum_{i=1}^{m}(\mathrm{dyc})_{i} \exp \left(-\frac{Q}{K_{B} T_{i}}\right)\right\}}
\end{aligned}
$$

# Example Problem 5 

For the mission profile shown in Table 14.2, find the effective static temperature equivalent for the expected 10 years of use. Assume an activation energy of 1 eV .

## Solution

$$
T_{\text {effective }}=\frac{-\left(Q / K_{B}\right)}{\ln \left\{\sum_{i=1}^{m}(\mathrm{dyc})_{i} \exp \left(-\frac{Q}{K_{B} T_{i}}\right)\right\}}
$$

The following spreadsheet was used to determine $T_{\text {effective }}$.| $Q=1 \mathrm{eV}$ |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
| $K_{B}=8.62 \mathrm{E}-5 \mathrm{eV} / \mathrm{K}$ |  |  |  |  |
| Temp $\left({ }^{\circ} \mathrm{C}\right)$ | Temp (K) | Time (months) | Duty cycle (dyc) | $(\mathrm{dyc})_{i}\left[\exp \left(-\frac{Q}{K_{B} T_{i}}\right)\right]$ |
| 180 | 453 | 1 | 0.00833 | $6.29394 \mathrm{E}-14$ |
| 150 | 423 | 7 | 0.05833 | $7.16528 \mathrm{E}-14$ |
| 125 | 398 | 12 | 0.10000 | $2.1936 \mathrm{E}-14$ |
| 95 | 368 | 70 | 0.58333 | $1.18879 \mathrm{E}-14$ |
| 75 | 348 | 24 | 0.20000 | $6.65869 \mathrm{E}-16$ |
| 25 | 298 | 6 | 0.05000 | $6.19719 \mathrm{E}-19$ |
|  |  | 120 | 1.00000 | Sum $=1.69083 \mathrm{E}-13$ |

$$
\text { Teff }=-\left(Q / K_{\mathrm{B}}\right) / \mathrm{Ln}(\text { Sum })=394.2 \mathrm{~K}=121.2^{\circ} \mathrm{C}
$$

With an activation energy of $Q=1 \mathrm{eV}$, the effective static temperature $T_{\text {eff }}$ for this mission profile is $T_{\text {eff }}=121^{\circ} \mathrm{C}$

# Example Problem 6 

The voltage dropped across a $70 \AA$ thick $\mathrm{SiO}_{2}$ capacitor dielectric is shown below for one period. Assuming that the operating temperature is $105^{\circ} \mathrm{C}$ and that the field acceleration can be estimated by:

$$
\begin{aligned}
\gamma & =\frac{p_{\mathrm{eff}}}{K_{B} T} \cong \frac{13 \mathrm{e} \AA}{K_{B} T}=\frac{13 \times 10^{-8} \mathrm{e}(\mathrm{~cm})}{\left(8.625 \times 10^{-5} \mathrm{eV} / \mathrm{K}\right)(105+273) \mathrm{K}} \\
& =4.0 \mathrm{~cm} / \mathrm{MV}=4.0 \times 10^{-6} \mathrm{~cm} / \mathrm{V}
\end{aligned}
$$

find the effective voltage $V_{\text {eff }}$ for the time-dependent dielectric breakdown (TDDB) failure mechanism.

(continued)# Solution 

The stress $\xi$ in this example problem, which produces TDDB, is electric field E. From Eq. (14.26) one can write:

$$
E_{\text {effective }} \cong \frac{1}{\gamma} \ln \left\{\sum_{i}(\mathrm{dyc})_{i} \exp \left[\gamma E_{i}\right]\right\}
$$

Since $E=V / t_{\mathrm{ox}}$, where $t_{\mathrm{ox}}$ is the thickness of the dielectric, then one can write the effective voltage for TDDB as:

$$
V_{\text {effective }} \cong \frac{t_{\mathrm{ox}}}{\gamma} \ln \left\{\sum_{i}(\mathrm{dyc})_{i} \exp \left[\left(\gamma / t_{\mathrm{ox}}\right) V_{i}\right]\right\}
$$

| $t_{\mathrm{ox}}=7.00 \mathrm{E}-07 \mathrm{~cm}$ |  |  |
| :-- | :-- | :-- |
| $\gamma=4.00 \mathrm{E}-06 \mathrm{~cm} / \mathrm{V}$ | Duty cycle | $(\mathrm{dyc})_{\mathrm{i}} \exp \left[\left(\gamma / t_{\mathrm{ox}}\right) \mathrm{V}_{i}\right]$ |
| Voltage $(\mathrm{V})$ | $3.00 \mathrm{e}-01$ | $4.64 \mathrm{E}+07$ |
| 3.3 | $1.50 \mathrm{E}-01$ | $1.29 \mathrm{E}+08$ |
| 3.6 | $1.00 \mathrm{E}-01$ | $4.77 \mathrm{E}+08$ |
| 3.9 | $4.00 \mathrm{E}-02$ | $5.98 \mathrm{E}+08$ |
| 4.1 | $2.00 \mathrm{E}-01$ | $3.20 \mathrm{E}+05$ |
| 2.5 | $1.00 \mathrm{E}-02$ | $8.17 \mathrm{E}+09$ |
| 3.6 |  | $\operatorname{Sum}=9.59 \mathrm{E}+09$ |
| 4.8 |  |  |

$V_{\text {effective }}=\left(t_{\mathrm{ox}} / \gamma\right) \ln (\mathrm{Sum})=4.02$ volts
$V_{\text {effective }}$ determination is shown in the following spreadsheet. In summary, the mission profile for this dielectric is equivalent to an effective constant voltage of $V_{\text {effective }}=4.02 \mathrm{~V}$ for TDDB.

## Example Problem 7

The mission profile is shown in Fig. 14.8 for a conductor.
Because the current density is rather high, one would like to find the effective current density for electromigration (EM)-induced failure. Since EM-induced failure is impacted by the average current density, find the average current density $\mathrm{J}_{\text {ave }}$ for the EM mission profile shown Fig. 14.8.

Fig. 14.8 Mission profile for current densities in a conductor over one period $P$

# Solution 

The average current density can be easily determined using Eq. (14.24) with $n=1$ :

$$
J_{\text {effective }}-J_{\text {crit }}=\sum_{i}(\text { dyc })_{i}\left[J_{i}-J_{\text {crit }}\right]
$$

Assuming that $J_{\text {crit }}$ is negligibly small for the conductor length, the following spreadsheet was used to calculate $J_{\text {effective }}=J_{\text {ave }}$.

| Current density $\left(\mathrm{A} / \mathrm{cm}^{2}\right)$ | $(\text { Duty cycle })_{\mathrm{i}}$ | $(\mathrm{dyc})_{\mathrm{i}}\left[J\right]_{\mathrm{i}}$ |
| :-- | :-- | :-- |
| $5.00 \mathrm{E}+05$ | $3.75 \mathrm{E}-01$ | $1.88 \mathrm{E}+05$ |
| $7.00 \mathrm{E}+05$ | $2.25 \mathrm{E}-01$ | $1.58 \mathrm{E}+05$ |
| $5.80 \mathrm{E}+05$ | $2.50 \mathrm{E}-01$ | $1.45 \mathrm{E}+05$ |
| $0.00 \mathrm{E}+00$ | $5.00 \mathrm{E}-02$ | $0.00 \mathrm{E}+00$ |
| $4.70 \mathrm{E}+05$ | $1.00 \mathrm{E}-01$ | $4.70 \mathrm{E}+04$ |
|  |  | $\operatorname{Sum}=5.37 \mathrm{E}+05$ |

$J_{\text {effective }}=J_{\text {ave }}=\operatorname{Sum}=5.37 \mathrm{E}+05 \mathrm{~A} / \mathrm{cm}^{2}$
In summary, for EM-induced failures, the effective current density $J_{\text {effective }}$ is simply the average current density $J_{\text {ave }}$. However, the assumption here isthe constituent current densities, in the mission profile, are each of sufficiently low value that significant Joule heating (self heating) is not an issue for the conductor, i.e., the conductor temperature remains constant. If this is not the case, then the conductor temperature will have to be taken into account and the effective temperature $T_{\text {eff }}$ will have to be calculated, as in example problem 5. When $J_{\text {effective }}=J_{\text {ave }}$ is obtained, the time-to-failure TF goes as $\mathrm{TF} \sim\left(J_{\text {ave }}\right)^{-2}$ for aluminum-alloys and as $\mathrm{TF} \sim\left(J_{\text {ave }}\right)^{-1}$ for copper.# Example Problem 8 

The mission profile, for fatigue considerations, is shown below. Find the effective stress range $(\Delta \sigma)_{\text {effective }}$ for the mission profile. Assume a stress range exponent of $n=4$ and $(\Delta \sigma)_{\text {yield }}=400 \mathrm{MPa}$.

| Stress range: $\Delta \sigma(\mathrm{MPa})$ | (Duty cycle) |
| :-- | :-- |
| 200 | 0.10 |
| 400 | 0.25 |
| 700 | 0.36 |
| 900 | 0.23 |
| 1,200 | 0.05 |
| 1,400 | 0.01 |

## Solution

The effective stress range $(\Delta \sigma)_{\text {effective }}$ can be determined from Eq. (14.24) with $n=4$ and $(\Delta \sigma)_{\text {yield }}=400 \mathrm{MPa}$ :

$$
(\Delta \sigma)_{\text {effective }}-(\Delta \sigma)_{\text {yield }} \cong\left[\sum_{i}(\text { dyc })_{i}\left[(\Delta \sigma)_{i}-(\Delta \sigma)_{\text {yield }}\right]^{4}\right]^{1 / 4}
$$

Recall that no damage is occurring when the stress range is less than $(\Delta \sigma)_{\text {yield }}$; thus, only the stress range above $(\Delta \sigma)_{\text {yield }}$ is used in the following spreadsheet for the effective stress range $(\Delta \sigma)_{\text {eff }}$ calculation.

| Stress range: <br> $\Delta \sigma(\mathrm{MPa})$ | Stress range above yield: <br> $(\Delta \sigma)_{i}-(\Delta \sigma)_{\text {yield }}(\mathrm{MPa})$ | (Duty <br> cycle) | $(\mathrm{dyc})_{i}\left[(\Delta \sigma)_{i}-(\Delta \sigma)_{\text {yield }}\right]^{n}$ |
| :-- | :-- | :-- | :-- |
| 200 | 0.00 | 0.10 | 0 |
| 400 | 0.00 | 0.25 | 0 |
| 700 | 300.00 | 0.36 | $2.92 \mathrm{E}+09$ |
| 900 | 500.00 | 0.23 | $1.44 \mathrm{E}+10$ |
| 1,200 | 800.00 | 0.05 | $2.05 \mathrm{E}+10$ |
| 1,400 | $1,000.00$ | 0.01 | $1.00 \mathrm{E}+10$ |
|  |  |  | $\mathrm{Sum}=4.78 \mathrm{E}+10$ |

$(\Delta \sigma)_{\text {effective }}-(\Delta \sigma)_{\text {yield }}=[\mathrm{Sum}]^{1 / 4}=468 \mathrm{MPa}$.
In summary, for the mission profile shown, the effective stress range is $(\Delta \sigma)_{\text {effective }}-(\Delta \sigma)_{\text {yield }}=468 \mathrm{MPa}$ or $(\Delta \sigma)_{\text {effective }}=868 \mathrm{MPa}$.

## 7 Avoidance of Resonant Frequencies

There is a strong caution that we must discuss before this chapter ends. Nearly every component/system has certain natural or resonant frequencies that must be avoided. If the applied time-dependent stress $\xi(t)$ is periodic, with a frequency close to asystem's natural/resonant frequency, then unexpectedly large amplitude oscillations can occur. This is true for both mechanical systems and circuits. If the applied stress is near a natural resonance for the system, then what might have been initially thought to be a rather benign stress level, may actually cause severe damage to the system. This is discussed in great detail in the next chapter (Chap. 15).

One has probably heard stories about the large amplitude oscillations that can occur when a dog simply trots across a suspension bridge. Certainly, most of us have experienced something similar when a dog simply trots across a wooden floor in our house. The entire room may tend to shake as the dog trots across the floor. Even though the energy input per step associated with the dog's movement is rather small, an oscillator (close to its natural frequency) is very effective in absorbing the input energy. Thus, the amplitude of the oscillation tends to grow rapidly as the dog trots.

The equations developed in this chapter assume that the applied dynamical stress $\xi(t)$ is not close to a natural frequency for the device/system. Remember- because of resonance, a soprano can shatter a wine glass with simply the voice!

# Problems 

1. The electric field $E$ in a capacitor dielectric is expected to operate at $4 \mathrm{MV} / \mathrm{cm}$ during a period of 16 ns . However, during this period, a sharp rise/pulse in the electric field (rising from 4 to $8 \mathrm{MV} / \mathrm{cm}$ ) occurs between 4 and 7 ns . Using the full-width-at-half-maximum approach for the pulse, calculate the effective constant electric field for the 16 ns period shown. Assume an exponential field acceleration parameter of $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$.


Answer: $E_{\text {effective }}=7.48 \mathrm{MV} / \mathrm{cm}$2. A mechanical component experiences a time-dependent tensile-stress waveform given by:

$$
\sigma(t)=\frac{1.863 \times 10^{-5} \mathrm{MPa}}{(\mathrm{~h})^{9}}(t)^{9} \exp \left[-\left(\frac{t}{8}\right)^{10}\right]
$$

The shape of the waveform is shown below.


Assuming a creep power-law exponent of $n=4$ :
(a) Find the effective rectangular pulse over the time interval from 4 h to 10 h .
(b) Assuming the period is 24 h , what is the effective constant value of the stress over this period?

Answer: (a) 599 MPa (b) 424 MPa
3. For wind turbine use, the energy contained in the wind is a critically important parameter. The energy contained in the wind is proportional to the square of the wind speed. For Dallas, Texas, the following mean wind speeds were reported by month:
(a) Find the mean value for the wind speed $S$ for the entire year.

| Month | \# Days | Wind speed: S (mph) | (Duty cycle) $)_{i}$ |
| :-- | :-- | :-- | :-- |
| January | 31 | 11.0 | 0.085 |
| February | 28 | 11.7 | 0.077 |
| March | 31 | 12.6 | 0.085 |
| April | 30 | 12.4 | 0.082 |
| May | 31 | 11.1 | 0.085 |
| June | 30 | 10.6 | 0.082 |
| July | 31 | 9.8 | 0.085 || Month | \# Days | Wind speed: S (mph) | (Duty cycle) |
| :-- | :-- | :-- | :-- |
| August | 31 | 8.9 | 0.085 |
| September | 30 | 9.3 | 0.082 |
| October | 31 | 9.7 | 0.085 |
| November | 30 | 10.7 | 0.082 |
| December | 31 | 10.8 | 0.085 |

(b) Given the energy in the wind goes as the square of the wind speed, find the constant effective wind speed $(S)_{\text {effective }}$ for turbine use during the entire year.

# Answers: 

(a) Mean Speed $=10.7 \mathrm{mph}$
(b) $(S)_{\text {effective }}=10.8 \mathrm{mph}$
4. The mission profile is shown below for a mechanical component. Assuming that the mechanical component is a metal that has no yield point and a power-law of $n=4$ for creep, find the effective constant stress $\sigma_{\text {effective }}$ for the full 10 years (120 Months) of service.

| Stress level: $\sigma$ (MPa) | Time (months) | (Duty cycle) |
| :-- | :-- | :-- |
| 0 | 1 | 0.008 |
| 100 | 2 | 0.017 |
| 200 | 4 | 0.033 |
| 300 | 6 | 0.050 |
| 400 | 18 | 0.150 |
| 500 | 35 | 0.292 |
| 600 | 25 | 0.208 |
| 700 | 15 | 0.125 |
| 800 | 9 | 0.075 |
| 900 | 4 | 0.033 |
| 1,000 | 1 | 0.008 |
|  | Total $=120$ | 1.000 |

Answer: $\sigma_{\text {effective }}=612 \mathrm{MPa}$
5. Using the mission profile for the metal component in Problem 4, what would be the effective constant-stress value $\sigma_{\text {effective }}$ for the full 10 years ( 120 months) of service if the metal component has a power-law stress exponent of $n=4$ for creep and has a yield strength of 400 MPa ?

Answer: $\sigma_{\text {effective }}-\sigma_{\text {yield }}=283 \mathrm{MPa}$ or $\sigma_{\text {effective }}=683 \mathrm{MPa}$
6. Using the mission profile for the metal component in Problem 4, what would be the effective constant-stress value $\sigma_{\text {ffective }}$ for the full 10 years ( 120 months) of service if a power-law exponent of $n=6$ for creep is assumed and no defined yield strength?Answer: $\sigma_{\text {effective }}=650 \mathrm{MPa}$
7. Using the mission profile for the metal component in Problem 4, what would be the effective constant-stress value $\sigma_{\text {effective }}$ for the full 10 years ( 120 months) of service if a power-law exponent of $n=6$ for creep is assumed and a yield strength of 400 MPa ?

Answer: $\sigma_{\text {effective }}-\sigma_{\text {yield }}=331 \mathrm{MPa}$ or $\sigma_{\text {effective }}=731 \mathrm{MPa}$
8. EM is a concern for a certain conductor. The current densities in the conductor are shown below. What is the average current density?

| Current density: $J\left(\mathrm{~A} / \mathrm{cm}^{2}\right)$ | (Duty cycle) $)_{1}$ |
| :-- | :-- |
| $5.00 \mathrm{E}+05$ | 0.4 |
| $7.00 \mathrm{E}+05$ | 0.3 |
| $9.00 \mathrm{E}+05$ | 0.2 |
| $1.20 \mathrm{E}+06$ | 0.1 |

Answer: $(J)_{\text {average }}=7.1 \times 10^{5} \mathrm{~A} / \mathrm{cm}^{2}$
9. The mission profile for a component, with fatigue concerns, is shown below. Assuming a power-law exponent of $n=4$ and no elastic range, find the effective constant value for the stress range $(\Delta \sigma)_{\text {effective }}$.

| Stress range: $\Delta \sigma(\mathrm{MPa})$ | (Duty cycle) $)_{1}$ |
| :-- | :-- |
| 300 | 0.10 |
| 400 | 0.25 |
| 500 | 0.36 |
| 600 | 0.23 |
| 700 | 0.05 |
| 800 | 0.01 |

Answer: $(\Delta \sigma)_{\text {effective }}=524 \mathrm{MPa}$
10. A silica-based capacitor dielectric of thickness $45 \AA$ will see the following voltages during operation. What is the effective constant voltage $V_{\text {eff }}$ for TDDB? Assume an exponential field acceleration parameter of $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$.

| Voltage $(\mathrm{V})$ | (Duty cycle) $)_{1}$ |
| :-- | :-- |
| 2.5 | $3.00 \mathrm{E}-01$ |
| 2.8 | $1.50 \mathrm{E}-01$ |
| 3.1 | $1.00 \mathrm{E}-01$ |
| 3.4 | $4.00 \mathrm{E}-02$ |
| 3.7 | $2.00 \mathrm{E}-01$ |
| 4.0 | $2.00 \mathrm{E}-01$ |
| 4.3 | $1.00 \mathrm{E}-02$ |

Answer: $V_{\text {effective }}=3.9 \mathrm{~V}$11. The thermal profile for a device is shown below. Assuming an activation energy of 0.7 eV , what is the effective constant-temperature $T_{\text {effective }}$ ?

| Temp $\left({ }^{\circ} \mathrm{C}\right)$ | Temp $(\mathrm{K})$ | Time (months) | Duty cycle (dyc) |
| :-- | :-- | :-- | :-- |
| 180 | 453 | 1 | 0.00833 |
| 150 | 423 | 7 | 0.05833 |
| 125 | 398 | 12 | 0.10000 |
| 95 | 368 | 70 | 0.58333 |
| 75 | 348 | 24 | 0.20000 |
| 25 | 298 | 6 | 0.05 |

Answer: $T_{\text {effective }}=112^{\circ} \mathrm{C}$# Chapter 15 <br> Resonance and Resonance-Induced Degradation 

The time-to-failure models (developed in Chap. 14) for periodic stresses assumed that the periodic stresses were not associated with any resonant frequencies for the component/system. However, nearly every component/system has certain natural (or resonant) frequencies that must be avoided. If the applied time-dependent stress $\xi(\mathrm{t})$ is periodic, with a frequency close to a system's natural frequency $v$, then this condition is referred to as resonance. Resonance can produce unexpectedly largeamplitude oscillations. This is true for both mechanical systems and electrical systems. Because of resonance, what might have been thought initially to be a rather benign stress condition can actually be a severe stress condition.

## 1 Natural/Resonant Frequency

You have probably heard of and/or seen stories about the large amplitude oscillations that can occur when a dog simply trots across a suspension bridge. Or, you may have seen pictures of the Tacoma bridge failure during pulsating wind conditions. ${ }^{1}$ As previously mentioned at the end of the last chapter, because of resonance, many of the objects in the room may vibrate rather strongly as the dog trots across a wooden floor. Even though the energy-input per-step associated with the dog's movement is relatively small, an oscillator (that is acted on by a periodic stress

[^0]
[^0]:    ${ }^{1}$ For many years, the Tacoma bridge failure was attributed simply to resonance due to pulsating wind conditions. More recently this has been questioned.Fig. 15.1 Block is captured in a metastable vertical state. The center of mass (CM) is trapped in a potential well which gives the vertical state some degree stability. The frictional forces at the base of the block are sufficient to keep the block from sliding

$\xi(\mathrm{t})$ close to the oscillator's natural/resonant frequency $v$ ) can be very effective in absorbing the input energy. Thus, the amplitude of the oscillations may grow rapidly as the dog trots across the wooden floor.

Every system has certain natural frequencies $v$ that make it unstable when a periodic stress $\xi(\mathrm{t})$ of frequency $f$ is applied that is very close to the system's natural frequency $v$. Shown in Fig. 15.1 is a very simple system (a block) that is captured in a vertical metastable state. We will assume that the frictional forces at the base of the block are sufficient to keep the block from sliding when pushed on by the external force. We want to see if a certain constant external force $\mathrm{F}_{\text {ext }}$ can tip/activate the block from the vertical to the horizontal position.

The amount of constant-force $\mathrm{F}_{\text {ext }}$ work required to tip/activate the block from the vertical to the horizontal position is $\mathrm{F}_{\text {ext }} \Delta \mathrm{x} \geq \mathrm{Q}$, where Q is the needed activation energy to tip the block. Thus, it would seem to be impossible that a small constant external force can tip/activate the block if $\mathrm{F}_{\text {ext }}<\mathrm{Q} / \Delta \mathrm{x}$. However, if the small force is not constant, but is actually periodic (with a frequency $f$ close to the natural/resonant frequency $v$ for the block), then amazing things can happen.

# Example Problem 1 

A block is resting on a rough surface (with a high coefficient of sliding friction) that prevents block sliding. Using the principle of virtual work and conservation of energy, show that it requires only half the force to tip the block when the force is applied at the top of the block versus the middle.

Infinitesimal virtual work $\delta \mathrm{w}$ done by an external force is defined as,

$$
\delta w=\vec{F}_{\text {ext }} \cdot d \vec{x}
$$

Using conservation of energy, the work done by $\left(\mathrm{F}_{\text {ext }}\right)_{1}$ to tip the block must be the same amount of work as done by $\left(\mathrm{F}_{\text {ext }}\right)_{2}$. Therefore, we have

$$
\left(F_{\text {ext }}\right)_{2} x_{2}=\left(F_{\text {ext }}\right)_{1} x_{1} \Rightarrow\left(F_{\text {ext }}\right)_{2}=\left(\frac{x_{1}}{x_{2}}\right)\left(F_{\text {ext }}\right)_{1}
$$

The angle at which the block is tipped is $\theta_{\text {crit }}$. Thus, we have the relationship:

$$
\frac{x_{1}}{x_{2}}=\frac{(L / 2) \tan \left(\theta_{\text {crit }}\right)}{L \tan \left(\theta_{\text {crit }}\right)}=\frac{1}{2}
$$

Therefore,Fig. 15.2 Parabolic potential $\mathrm{V}(\mathrm{x})$ is a reasonably good approximation for the center of mass (CM) trapped in the metastable vertical state. The block's tipping point occurs at $x_{\text {crit }}$ and the energy needed to tip/activate the block is Q


$$
\left(F_{e x t}\right)_{2}=\frac{1}{2}\left(F_{e x t}\right)_{1}
$$

We want to finish this simple example problem with noting that, by using the principle of virtual work and conservation of energy, we achieved the same result that would have been obtained if we had used torque analysis. Taking the moments about a fixed point at the base (e.g., point B in Fig. 15.1), one obtains:

$$
\begin{gathered}
\left(F_{e x t}\right)_{2}(L)=\left(F_{e x t}\right)_{1}(L / 2) \\
\therefore\left(F_{e x t}\right)_{2}=\frac{1}{2}\left(F_{e x t}\right)_{1}
\end{gathered}
$$

At first glance, it is hard to imagine how a rigid solid block can behave like an oscillator. However, as we can see from Fig. 15.2, the center of mass (CM) is momentarily trapped in a potential well. Furthermore, as illustrated in Fig. 15.2, we see that we can approximate this potential well with a parabolic potential $\mathrm{V}(\mathrm{x})$ [which is the potential for a simple harmonic oscillator].

The parabolic potential $\mathrm{V}(\mathrm{x})$ is given by:

$$
V(x)=\frac{1}{2} k_{s}(x)^{2}
$$

where $x$ is the displacement from equilibrium and $k_{s}$ is the effective spring constant for this harmonic oscillator. For this parabolic potential, the restoring force $F$ is given by:

$$
F=-\frac{d V(x)}{d x}=-k_{s} x
$$

The natural/resonant frequency $v$ for this oscillator is given by ${ }^{2}$ :

[^0]
[^0]:    ${ }^{2}$ Refer to Resnick, Halliday, and Krane in Bibliography.$$
v=\frac{1}{2 \pi} \sqrt{\frac{k_{s}}{M}}
$$

where $M$ is the mass of the block. Conservation of energy at the tipping point can be used to find an effective value for the spring constant $k_{s}$ :

$$
V\left(x_{\text {crit }}\right)=\frac{1}{2} k_{s}\left(x_{\text {crit }}\right)^{2}=Q
$$

where Q is the activation energy.
In Chap. 2 we showed that for a block of mass M, width W, and height L, the activation energy for tipping was given by:

$$
Q=\frac{M g}{2}\left(\sqrt{L^{2}-W^{2}}-L\right)
$$

where g is the acceleration of gravity. Using Eqs. (15.4) and (15.5), an equation is obtained that gives an effective value for the spring constant $k_{s}$ for describing the block oscillations:

$$
k_{s}=\frac{M g\left(\sqrt{L^{2}-W^{2}}-L\right)}{\left(x_{\text {crit }}\right)^{2}}
$$

Thus, using Eqs. (15.3) and (15.6), the natural/resonant frequency for the block becomes

$$
v=\frac{1}{2 \pi} \sqrt{\frac{g\left(\sqrt{L^{2}-W^{2}}-L\right)}{x_{\text {crit }}^{2}}}
$$

If we now apply a relatively small periodic stress $F(t)$ with a frequency $f$ equal to the block's natural/resonant frequency $v$, and assuming no energy loss, then with time the block can be tipped/activated from the vertical to the horizontal position. This is illustrated in Fig. 15.3 where we show amplitude growth with each forcepulse.

One can see from Fig. 15.3 that large amplitudes/displacements can occur rather quickly when the applied external force is periodic with a frequency $f$ very close to the block's natural/resonant frequency $v$. It should be noted, from Fig. 15.3, that the amplitude can potentially grow if pulsed at any of these frequencies: $v, v / 2, v / 3, v / 4$, $\bullet \bullet \bullet v / \mathrm{N}$. However, the amplitude will grow at a much slower rate for each of the successive decreases in frequency. Also, if there is damping/energy-loss present (as discussed in detail in later sections), then this will greatly diminish the effectiveness of the lower frequency resonant modes. Thus, in this book, a strong resonance

Fig. 15.3 External periodic force is applied at a system's natural/resonant frequency $v$. Due to resonance, and assuming little/no energy loss, relatively large amplitudes/displacements can occur

Fig. 15.4 Amplitude/ displacement grows with periodic pulsing at the system's natural frequency. The periodic force produces a rocking of the block back and forth. Assuming little/ no energy loss per cycle, a slightly higher oscillator energy-level/amplitude is reached with each new pulse

condition will be said to occur when the pulsing frequency $f$ matches the natural frequency $v$ of the oscillator: $f=v$. Lower frequency weaker resonance conditions will be said to occur when $f=v / N$, where $N$ is an integer $(N>1)$.

As illustrated in Fig. 15.4, periodic pulsing at strong resonance causes the amplitude/displacement to grow with each pulse. Eventually, the amplitude/displacement of the center of mass reaches $\mathrm{x}=\mathrm{x}_{\text {crit }}$ and a tipping of the block occurs. Thus, because of resonance, what seemed to be an impossible task (tipping of large block with a small external force) tended to occur relatively easily.

Please note (see Fig. 15.4) that the periodic force is doing work on the oscillator. Assuming no energy loss per cycle, then with each pulse the potential energy of the oscillator is increasing. Therefore, from Chap. 2, we know that the Gibbs Potential for the oscillator is increasing with each new pulse. This makes the oscillator more unstable with each new pulse. One can think of the increase in Gibbs Potential for the oscillator as equivalent to exciting the oscillator. An excited oscillator is fundamentally more unstable and a driving force exists for Gibbs Potential reduction. This isFig. 15.5 Light pole failed (at its baseplate) due to pulsating wind conditions at resonance


Fig. 15.6 Shown are the rear wheels of an truck that are trapped in a deep pothole that can be approximated by a parabolic potential energy $\mathrm{V}(\mathrm{x})$. Since only the rear wheels of truck are trapped, the amount of mass trapped in the pothole is M (where the total mass of the truck is 2 M ). The pothole has a depth $h$ and width $2 x_{\text {crit }}$
especially true for excited atomic oscillators (lowering its Gibbs Potential can occur via photon emissions) and excited nuclear oscillators (lowering its Gibbs Potential can occur via photon and/or particle emissions).

Shown in Fig. 15.5 is a light pole that has failed at its baseplate (due to resonance produced by pulsating wind conditions). The maximum wind speed was thought to be rather benign relative to the strength of the baseplate/pole system. However, the frequency $f$ of the pulsating wind conditions tended to match the natural/resonant oscillation frequency $o$ for the light pole. Because of resonance, the light pole failed catastrophically at its baseplate.

# 2 Pulsing at Strong Resonance 

Consider the rear wheels of a truck that are captured in a pothole that can be approximated by a parabolic potential as shown in Fig. 15.6.For the mass M to escape the parabolic pothole, the energy $V_{\text {crit }}$ for the oscillator at $x_{\text {crit }}$ must be at least equal to the potential energy of the trapped mass, giving:

$$
V_{\text {crit }}=\frac{1}{2} k_{s} x_{\text {crit }}^{2}=M g h
$$

Therefore, using Eq. (15.8), the effective spring constant $k_{s}$ for the trapped mass $M$ (in the parabolic-shaped pothole) can be expressed by:

$$
k_{s}=\frac{2 M g h}{x_{\text {crit }}^{2}}
$$

The resonant frequency $v$ for this system can be expressed as,

$$
v=\frac{1}{2 \pi} \sqrt{\frac{k_{s}}{M}}=\frac{1}{2 \pi} \sqrt{\frac{2 g h}{x_{\text {crit }}^{2}}}
$$

Periodic pulsing/pushing at the truck's natural frequency $v$, with an input energy of $\mathrm{V}_{0}$ per pulse/push, the number $n$ of pulses required to free the truck (assuming no energy dissipation) can be determined from the conservation of energy:

$$
n V_{0} \geq V_{\text {crit }}=\frac{1}{2} k_{s} x_{\text {crit }}^{2}=M g h
$$

# Example Problem 2 

The rear wheels of a truck are trapped in a pothole that is 50 cm deep and 150 cm wide (as illustrated in Fig. 15.6). Assume that the trapped mass $M$ in the pothole can be approximated by a parabolic potential. With a single push, we find that the rear wheels are displaced by 10 cm in the horizon direction. If we now push periodically (with the same amount input energy each cycle) and at the same frequency as the natural/resonant frequency for the system, how many pushes are required to free the truck from the pothole. Assume that the truck weighs 2000 lbs and that no energy is dissipated during pulsing.

## Solution

Since only the rear wheels of truck are confined to the pothole, the confined mass $M$ is:$$
M=\left(\frac{2000 l b}{2}\right) \cdot\left(\frac{1 k g}{2.205 l b}\right)=453.5 \mathrm{~kg}
$$

Using Eq. (15.9), the effective spring constant $k_{s}$ for the rear wheels that are stuck in the parabolic potential is:

$$
\begin{aligned}
k_{s}=\frac{2 M g h}{x_{c r i t}^{2}}= & \frac{(2)(453.5 \mathrm{~kg})\left(9.81 \frac{\mathrm{~m}}{\mathrm{~s}^{2}}\right)(0.5 \mathrm{~m})}{(0.75 \mathrm{~m})^{2}} \\
& =7.91 \times 10^{3} \frac{\mathrm{~kg}}{2^{2}}
\end{aligned}
$$

Since the single push produced a displacement in the x -direction of $\mathrm{x}_{0}=10 \mathrm{~cm}$, this corresponds to a pushing force of $\mathrm{F}=\mathrm{k}_{\mathrm{s}} \mathrm{x}_{0}=791 \mathrm{~N}=178 \mathrm{lb}$. Thus, we will assume that each push increases the potential energy of the oscillator by an amount $\mathrm{V}_{0}$, where:

$$
\begin{aligned}
V_{0}=\frac{1}{2} k_{s}\left(x_{0}\right)^{2} & =\left(\frac{1}{2}\right)\left(7.91 \times 10^{3} \frac{k g}{s^{2}}\right)(0.1 \mathrm{~m})^{2} \\
& =39.6 \frac{\mathrm{~kg} \cdot \mathrm{~m}^{2}}{\mathrm{~s}^{2}}
\end{aligned}
$$

Using conservation of energy (with no energy dissipation), the number $n$ of periodic pushes (with an input of energy of $\mathrm{V}_{0}$ per push) required to free the rear wheels of the truck from the parabolic pothole is:

$$
n V_{0} \geq V_{\text {crit }}=M g h
$$

Solving for $n$ we have:

$$
n \geq \frac{M g h}{V_{0}}=\frac{(453.5 \mathrm{~kg})\left(9.81 \frac{\mathrm{~m}}{\mathrm{~s}}\right)(0.5 \mathrm{~m})}{39.6 \frac{\mathrm{~kg} \cdot \mathrm{~m}^{2}}{\mathrm{~s}^{2}}}=56
$$

In summary, with a periodic pushing input energy of $\mathrm{V}_{0}$ per pulse, and assuming no energy loss, it will require at least $n=56$ pushes to free the 2000 lb . truck from the parabolic pothole.# 3 Pulsing at Strong Resonance with Dissipation 

Thus far, we have only considered resonance without regards to energy-dissipation/ damping. However, often there are dissipative forces (e.g., frictional forces) existing that prevent the oscillator from absorbing all of the work-energy generated by the periodic external force $\mathrm{F}_{\text {ext }}$.

Suppose we push on an oscillator of mass $M$, displace the mass $M$ by amount $x_{0}$, and then release it. At the end of the first cycle, the mass returns back to a position $x_{1}$ (where $\mathrm{x}_{1}=\mathrm{x}_{0}$ ). For this situation, there was no energy loss in the oscillator and we say that no dissipative forces are acting. A system with no dissipative forces is an artificial situation because dissipative forces always seem to exist.

In Fig. 15.7 we again show the rear wheels of a truck that are trapped in a pothole, but this time loose sand is added to the pothole. When we push on the truck and displace it horizontally by the amount $x_{0}$ and release, the truck does not return to the position $x_{0}$ but to $x_{1}$ (where $x_{1}<x_{0}$ ). Some of the oscillator energy has dissipated.

The fractional energy reduction per cycle $\alpha$ for the oscillator is given by,

$$
\alpha=\frac{(1 / 2) k_{s} x_{1}^{2}}{(1 / 2) k_{s} x_{0}^{2}}=\left(\frac{x_{1}}{x_{0}}\right)^{2}
$$

It should be noted here that the energy loss per cycle (dissipation factor $L$ ) is given simply by $L=1-\alpha$.

Using Eq. (15.12), we want to see how the amplitude of the oscillations will degrade after a single-push (single input of energy) is initially given to the oscillator. The amplitude degrades from the initial value of $x_{0}$ as follows. Initially, the amplitude is $\mathrm{x}_{0}$. After one cycle of oscillation, the amplitude degrades to $\mathrm{x}_{1}=\alpha^{(1 / 2)} \bullet \mathrm{x}_{0}$. After two cycles of oscillation, the amplitude degrades to $\mathrm{x}_{2}=\alpha^{(1 / 2)} \bullet \mathrm{x}_{1}=\left(\alpha^{(1 / 2)}\right)^{2} \bullet \mathrm{x}_{0}$. If we generalize, then after the $\mathrm{n}^{\text {th }}$ oscillation, the relative amplitude of the oscillation is given by


Fig. 15.7 Shown are the rear wheels of a truck that are trapped in a pothole. The pothole potential well has been approximated by a parabolic potential energy $\mathrm{V}(\mathrm{x})$. The pothole is filled with sand which serves to generate resistivefrictional forces. Since only the rear wheels of truck are trapped, the amount of mass trapped in the pothole is M where the total mass of the truck is 2 MFig. 15.8 Relative amplitude degradation, with number of cycles and degradation factors $L$. A single input energy of $\mathrm{V}_{0}$ was given to the oscillator initially. For example, if the oscillations die-off after $\sim 15$ cycles, then the loss factor is $L=0.5$


$$
\frac{x_{n}}{x_{0}}=(\alpha)^{n / 2}=(1-L)^{n / 2}
$$

For a single push (single energy-input), Fig. 15.8 illustrates how the amplitude of the oscillations degrades as a function of the number of cycles and as a function of the loss factor $L$.

# Example Problem 3 

With a single push, the mass of an oscillator is displaced by $\mathrm{x}_{0}$. After 5 oscillations, the displacement has degraded by $90 \%$. What is the loss factor L for this oscillator.

## Solution

Since the amplitude of the oscillations has degraded by $90 \%$ after 5 oscillations, using Eq. (15.13) we obtain:

$$
\begin{gathered}
\frac{0.1 x_{0}}{x_{0}}=(1-L)^{5 / 2} \\
\Rightarrow(0.1)^{2 / 5}=\left[(1-L)^{5 / 2}\right]^{2 / 5} \\
\Rightarrow L=1-(0.1)^{2 / 5}=0.602
\end{gathered}
$$

Therefore, after a single push, if the amplitude of the oscillations degrades by $90 \%$ after 5 cycles, then the loss factor is $\mathrm{L}=0.602$.

Now, rather than a single input of energy into the oscillator initially, let us assume that at the start of each cycle a constant amount of energy $V_{0}$ is input to the oscillator. With dissipation, the oscillator energy at the end of the first cycle is $\mathrm{V}_{1}=\alpha \mathrm{V}_{0}$. The oscillator energy at the end of the second cycle is: $V_{2}=\alpha\left[V_{0}+\alpha V_{0}\right]=\alpha$Fig. 15.9 Relative oscillator energy absorption, with number of cycles and with loss factors $L$. An input energy of Vo is given to the oscillator at the start of each cycle. Note that all curves tend to saturate when the input energy rate matches the energy loss rate

$V_{0}[1+\alpha]$. The energy at the end of the third cycle is $V_{3}=\alpha\left[V_{0}+V_{0}\left(\alpha+\alpha^{2}\right)\right]=\alpha$ $V_{0}\left[1+\alpha+\alpha^{2}\right]$. If we generalize, the energy $V_{n}$ at the end of the $n^{t h}$ cycle is given by:

$$
V_{n}=V_{0} \alpha \sum_{m=0}^{n-1} \alpha^{m}
$$

For dissipative forces (with $\alpha<1$ ), the above summation is simply a geometric series and the summation for a geometric series is given by:

$$
\sum_{m=0}^{n-1} \alpha^{m}=\left[\frac{1-\alpha^{n}}{1-\alpha}\right]
$$

Thus, using Eqs. (15.14) and (15.15). the relative energy of the oscillator at the end of the $n^{\text {th }}$ cycle is given by,

$$
\frac{V_{n}}{V_{0}}=\alpha\left[\frac{1-\alpha^{n}}{1-\alpha}\right]
$$

Shown in Fig. 15.9 is the relative energy of the dissipative oscillator at the end of $n$ oscillations, with a fixed input of energy $V_{0}$ at the start of each cycle and with a dissipation factor of $L=1-\alpha$. One can see that the relative oscillator energy increases initially but then tends to saturate at longer cycles.

With a dissipation factor of $L=0.5$, the relative oscillator absorption $\left(\mathrm{V}_{\mathrm{n}} / \mathrm{V}_{0}\right)$ saturates at approximately 1 ; this means that even though the total energy input into the oscillator is $n V_{0}$, the oscillator can only absorb $V_{0}$ of this energy. With a dissipation factor of $L=0.3$, the relative oscillator energy absorption saturates atapproximately 2 ; this means that even though the total energy input into the oscillator is $n V_{0}$, the oscillator can only absorb $2 V_{0}$ of this energy. With a dissipation factor of $L=0.2$, the relative oscillator energy absorption saturates at approximately 4 ; this means that even though the total energy input into the oscillator is $n V_{0}$, the oscillator can only absorb $4 V_{0}$ of this energy. With a dissipation factor of $L=0.1$, the relative oscillator energy absorption saturates at approximately 8 ; this means that even though the total energy input into the oscillator is $n V_{0}$, the oscillator can only absorb $8 V_{0}$ of this energy. Finally, with a dissipation factor of $L=0.01$, the relative oscillator absorption saturates at $\mathrm{n} \gg 10$; this means that the total energy input into the oscillator is $n V_{0}$ and the oscillator eventually absorbs much of the input energy. But, only when the loss factor is $L=0$ can the oscillator absorb all the input energy $\mathrm{nV}_{0}$.

# Example Problem 4 

Show that in the limit $\mathrm{L} \rightarrow 0$ (no energy loss), Eq. (15.16) reduces to: $\mathrm{V}_{\mathrm{n}}=\mathrm{nV}_{0}$.

## Solution

Since $\mathrm{L}=1-\alpha$, in the limit $L \rightarrow 0$ is equivalent to limit $\alpha \rightarrow 1$. Working with Eq. (15.16) we obtain:

$$
\begin{aligned}
& \operatorname{Limit}_{\alpha \rightarrow 1}\left\{V_{0} \alpha\left[\frac{1-\alpha^{n}}{1-\alpha}\right]\right\}=\operatorname{Limit}_{\alpha \rightarrow 1}\left\{V_{0}\left[\frac{\alpha-\alpha^{n+1}}{1-\alpha}\right]\right\} \\
& =\operatorname{Limit}_{\alpha \rightarrow 1}\left\{V_{0}\left[\frac{\frac{d}{d \alpha}\left(\alpha-\alpha^{n+1}\right)}{d \alpha(1-\alpha)}\right]\right\} \\
& =\operatorname{Limit}_{\alpha \rightarrow 1}\left\{V_{0}\left[\frac{\left(1-(n+1) \alpha^{n}\right)}{-1}\right]\right\} \\
& =n V_{0} \text {. }
\end{aligned}
$$

Therefore, in the limit $\mathrm{L} \rightarrow 0$ (no energy loss), Eq. (15.16) reduces to the expected result $\mathrm{V}_{\mathrm{n}}=\mathrm{nV}_{0}$ and the oscillator absorbs all of the input energy. We should note that L'Hospital's Rule for limits has been used in this solution.

Let us now return to the truck in the pothole shown in Fig. 15.7. In order for the truck to escape the pothole, the energy $V_{n}$ (at the end of the $\mathrm{n}^{\text {th }}$ cycle of pulsing) must be $V_{n} \geq V_{\text {crit }}$. Therefore, we obtain

$$
V_{0} \alpha\left[\frac{1-\alpha^{n}}{1-\alpha}\right] \geq V_{\text {crit }}=M g h=\frac{1}{2} k_{s} x_{\text {crit }}^{2}
$$

Solving Eq. (15.17) for the number of pulses required to escape ( $n=n_{\text {escape }}$ ) the parabolic potential, we have$$
n_{\text {escape }}=\frac{\ln \left[1-\left(\frac{1-\alpha}{\alpha}\right)\left(\frac{V_{\text {crit }}}{V_{0}}\right)\right]}{\ln (\alpha)}
$$

Remember that $n_{\text {escape }}[$ in Eq. (15.18)] represents the number of pulses required to escape the parabolic potential well when pulsing at resonance $(f=v)$ with an input energy per pulse of $V_{0}$ but with a fractional energy reduction per pulse of $\alpha$. It is noted, from Eq. (15.18), that a solution exists for $n_{\text {escape }}$ only if,

$$
\left(\frac{1-\alpha}{\alpha}\right)\left(\frac{V_{\text {crit }}}{V_{0}}\right)<1
$$

Thus, when pulsing at resonance $(f=v)$, with an input of energy $V_{0}$ per cycle, the necessary condition for escape is that the fractional energy reduction per cycle $\alpha$ must satisfy the condition:

$$
\alpha>\frac{V_{\text {crit }}}{V_{0}+V_{\text {crit }}}
$$

Or, equivalently, the loss factor $L=1-\alpha$ must satisfy:

$$
L<\frac{V_{0}}{V_{0}+V_{\text {crit }}}
$$

# Example Problem 5 

For the truck shown in Fig. 15.7, assume a dissipation factor of $L=1-\alpha=0.1$.
(a) Find the constant input energy $\mathrm{V}_{0}$ needed per cycle to free the trapped rear wheels of the truck after 10 cycles.
(b) Find the amount of the total input energy that is lost due to energy dissipation.

## Solution

(a) The rear wheels of the truck can be freed only when the oscillator energy at the end of the $\mathrm{n}^{\text {th }}$ oscillation is equivalent to or greater than Mgh . The energy at the end of the $\mathrm{n}^{\text {th }}$ oscillation is given by Eq. (15.16),

$$
V_{0} \alpha\left[\frac{1-\alpha^{n}}{1-\alpha}\right] \geq V_{\text {crit }}=M g h
$$

Solving for $\mathrm{V}_{0}$, we obtain:$$
V_{0} \geq\left[\frac{1-\alpha}{\alpha\left(1-\alpha^{n}\right)}\right] M g h
$$

where: $\mathrm{V}_{0}$ is the fixed input energy per cycle, $M$ is the amount of mass trapped in the pothole, $h$ is the depth of the pothole, and $\alpha$ is the fractional reduction in energy per cycle. With a loss factor of $L=0.1$ for each cycle, then $\alpha=1$ $L=0.9$ and we obtain,

$$
V_{0} \geq\left[\frac{1-0.9}{0.9\left(1-0.9^{10}\right)}\right] M g h=0.17 M g h
$$

(b) In order to free the truck in 10 pushing cycles (when pushing with a constant input-energy of $\mathrm{V}_{0}$ per-cycle and with a loss factor of $L=0.1$ per cycle) $\mathrm{V}_{0}$ needs to be at least $17 \%$ of the energy $V_{\text {crit }}=M g h$ needed to need to lift the truck vertically. However, during pulsing, total energy input over the 10 cycles was $10 \cdot(17 \%$ of Vcrit $)=170 \%$ Mgh. Therefore, because of the loose sand in the pothole, about $70 \%$ of the total input energy was dissipated/lost during pushing.

# 4 Pulsing at Weak Resonance with Dissipation 

We would now like to consider a commonly occurring condition where pulsing is done at a frequency $f$ that is at a weak resonant condition ( $f=w / N$, where N is an integer). Let us assume that at the start of each cycle, we input a constant amount of energy $\mathrm{V}_{0}$ into the oscillator. The oscillator energy at the end of the first pulsing cycle is $\mathrm{V}_{1}=\alpha^{\mathrm{N}} \mathrm{V}_{0}$. The oscillator energy at the end of the second cycle is $\mathrm{V}_{2}=\alpha^{\mathrm{N}}$ $\left[\mathrm{V}_{0}+\alpha^{\mathrm{N}} \mathrm{V}_{0}\right]=\alpha^{\mathrm{N}} \mathrm{V}_{0}\left[1+\alpha^{\mathrm{N}}\right]$. The energy at the end of the third cycle is $\mathrm{U}_{3}=\alpha^{\mathrm{N}}$ $\left[\mathrm{V}_{0}+\mathrm{V}_{0}\left(\alpha^{\mathrm{N}}+\alpha^{2 \mathrm{~N}}\right)\right]=\alpha^{\mathrm{N}} \mathrm{V}_{0}\left[1+\alpha^{\mathrm{N}}+\left(\alpha^{\mathrm{N}}\right)^{2}\right]$. If we generalize, the energy at the end of the $\mathrm{n}^{\text {th }}$ pulsing cycle is

$$
V_{n}=V_{0} \alpha^{N} \sum_{m=0}^{n-1}\left(\alpha^{\mathrm{V}}\right)^{m}=V_{0} \alpha^{N}\left[\frac{1-\left(\alpha^{N}\right)^{n}}{1-\alpha^{N}}\right]
$$

To escape the parabolic potential, the energy $V_{n}$ at the end of the $n^{\text {th }}$ pulse must be greater than or equal to $V_{\text {crit }}$. Solving for the number of pulses $n=n_{\text {escape }}$ required to escape the parabolic potential (when pulsing at a weak resonance condition $\mathrm{f}=w / \mathrm{N}$ ), we have$$
n_{\text {escape }}=\frac{\ln \left[1-\left(\frac{1-\alpha^{N}}{\alpha^{N}}\right)\left(\frac{V_{\text {crit }}}{V_{0}}\right)\right]}{\ln \left(\alpha^{N}\right)}
$$

For a solution to exist for $n_{\text {escape }}$, then

$$
\left(\frac{1-\alpha^{N}}{\alpha^{N}}\right)\left(\frac{V_{\text {crit }}}{V_{0}}\right)<1
$$

Solving for $\alpha=\alpha_{\text {escape }}$, we obtain the necessary condition for escaping the parabolic potential,

$$
\alpha_{\text {escape }}>\left[\frac{V_{\text {crit }}}{V_{0}+V_{\text {crit }}}\right]^{1 / N}
$$

Equation (15.25) can, of course, be used to determine the necessary condition on the loss factor per cycle for escaping ( $L_{\text {escape }}=1-\alpha_{\text {escape }}$ ):

$$
L<1-\left[\frac{V_{\text {crit }}}{V_{0}+V_{\text {crit }}}\right]^{1 / N}
$$

# Example Problem 6 

In Example Problem 4, the truck trapped in the parabolic pothole was freed with ten pulses when pulsing was conducted at strong resonance $(f=v)$. The loss factor was $L=0.1$ and the input energy per pulse was $V_{0}=17 \%$ of $V_{\text {crit }}$. If we had pulsed at a weaker resonance $(f=v / 3)$, would it have been possible to free the truck?

## Solution

Since the loss factor is $L=0.1, \alpha=1-L=0.9$. To be able to free the truck, $\alpha=\alpha_{\text {escape }}$ must be:

$$
\begin{aligned}
\alpha_{\text {escape }} & >\left[\frac{V_{\text {crit }}}{V_{0}+V_{\text {crit }}}\right]^{1 / N} \\
& >\left[\frac{V_{\text {crit }}}{0.17 V_{\text {crit }}+V_{\text {crit }}}\right]^{1 / 3} \\
& >0.95
\end{aligned}
$$

Therefore, since it was stated in this problem that $\alpha=0.9$, but $\alpha_{\text {escape }} \geq 0.95$, then it is impossible to free the truck with an input energy of $V_{o}=0.17 V_{\text {crit }}$ per pulse at the weaker resonance condition $(f=v / 3)$ and with a loss factor per cycle of $L=0.1$.Fig. 15.10 Cantilevered beam acted on by an external force. Beam deflection $\Delta \mathrm{x}$ (from the horizontal position) will occur when an external force $\mathrm{F}_{\text {ext }}$ is applied. Permanent bending/deformation of the beam will occur when the external force $\mathrm{F}_{\text {ext }}$ is greater than the yield force $\left(\mathrm{F}_{\text {ext }}\right)_{\text {yield }}$ for the beam


# 5 Onset of Yielding/Irreversible-Damage due to Pulsing 

If resonance cannot be totally avoided, then it is very important to understand how many resonant pulses can be tolerated before permanent damage is done to the component/system. Again, let us consider a relatively simple system, the cantilevered beam shown in Fig. 15.10.

As illustrated in Fig. 15.10, when a constant external force $F_{\text {ext }}$ is applied as shown, the beam will be deflected from the horizontal position by an amount $(\Delta \mathrm{x})_{0}$. When the external force is removed, the beam returns back to its normal horizontal position at $\Delta \mathrm{x}=0$. Thus, the beam is showing elastic behavior that can be approximated by a spring of constant $\mathrm{k}_{\mathrm{s}}$ given by:

$$
k_{s}=\frac{F_{e x t}}{(\Delta x)_{0}}
$$

During previous reliability testing of such cantilevered beams, it was determined that beam yielding occurs for a displacement $(\Delta \mathrm{x})_{\text {yield }}$ when an external force of $\left(\mathrm{F}_{\text {ext }}\right)_{\text {yield }}$ is applied. By yielding, we mean that the beam becomes permanently deformed/bent and cannot return back to its original position when the external force is removed. Since the beam acts elastically up to the point of yielding, then the amount of energy $V_{\text {yield }}$ required to produce yielding/permanent-damage to the beam is:

$$
V_{\text {yield }} \geq\left(F_{\text {ext }}\right)_{\text {yield }}(\Delta x)_{\text {yield }}=\frac{1}{2} k_{s}(\Delta x)_{\text {yield }}^{2}
$$

If the energy required to produce yielding $\left(V_{\text {yield }}\right)$ is in the form of strong resonant $(f=v)$ pulsing, with each pulse having a constant energy input of $\mathrm{V}_{\mathrm{o}}$ (and with no energy dissipation), then the number of pulses $n=n_{\text {damage }}$ required to produce permanent damage/deformation in the beam is given by,$$
n_{\text {damage }} \geq \frac{V_{\text {yield }}}{V_{0}}
$$

Let us now consider a much more general and realistic situation. Suppose that the energy required to produce yielding ( $V_{\text {yield }}$ ) can be in the form of either strong resonant pulsing $(f=v)$ or weak resonant pulsing $(f=v / N)$. Let us further suppose that each pulse has a constant input energy of $\mathrm{V}_{\mathrm{o}}$ but also with a dissipation factor of $L=1-\alpha$ per pulse. Using Eq. (15.23), the number of pulses $n=n_{\text {damage }}$ required to produce permanent damage/deformation of the beam can be written as,

$$
n_{\text {damage }}=\frac{\ln \left[1-\left(\frac{1-\alpha^{N}}{\alpha^{N}}\right)\left(\frac{V_{\text {yield }}}{V_{0}}\right)\right]}{\ln \left(\alpha^{N}\right)}
$$

In Eq. (15.30), as we have discussed, the resonant pulsing can be either strong resonance $(\mathrm{N}=1)$ or weaker resonance $(\mathrm{N}>1)$. The energy reduction fraction per cycle $\alpha$ is related to the loss factor per cycle $L$ by a simple relation $L=1-\alpha$.

It can be seen from Eq. (15.30) that no solution exists for $n_{\text {damage }}$ unless

$$
\left(\frac{1-\alpha^{N}}{\alpha^{N}}\right)\left(\frac{V_{\text {yield }}}{V_{0}}\right)<1
$$

Equation (15.31) can be used to determine the necessary condition for the energy reduction fraction $\alpha$ that leads to yielding/irreversible-damage:

$$
\alpha_{\text {damage }}>\left[\frac{V_{\text {yield }}}{V_{0}+V_{\text {yield }}}\right]^{1 / N}
$$

Equation (15.32) can, of course, be used to determine the necessary condition for the loss factor per cycle $L$ to produce damage ( $L_{\text {damage }}=1-\alpha_{\text {damage }}$ ):

$$
L_{\text {damage }}<1-\left[\frac{V_{\text {yield }}}{V_{0}+V_{\text {yield }}}\right]^{1 / N}
$$

# Example Problem 7 

A diver weighing 200 lb . steps to the end of a diving board. The end of the board is deflected from the horizontal position by 0.5 ft . Assume that diving board deformation is elastic, but yielding (permanent board deformation/ bending) occurs when the end of the board is displaced by 4 ft .
(a) What is the effective spring constant for the diving board?(b) What is the natural frequency for the diving board?
(c) Assuming that the diver starts bouncing (at the end of the diving board) and at the diving board's natural frequency, how many bounces (with a input energy from the diver's legs of $25 \mathrm{ft} \cdot \mathrm{lb}$ per bounce) are required to produce irreversible damage to the diving board?
(d) Reconsider question (c) except this time with a loss factor per cycle of $L=0.1$.

# Solution 

(a) Using Eq. (15.26), we obtain the effective spring constant $k_{s}$ :

$$
k_{s}=\frac{\text { Force }}{(\Delta x)_{0}}=\frac{200 l b}{0.5 f t}=100 \frac{l b}{f t}
$$

(b) Using Eq. (15.10), we obtain the natural frequency $\nu$ :

$$
\begin{aligned}
v & =\frac{1}{2 \pi} \sqrt{\frac{k_{s}}{M}}=\frac{1}{2 \pi} \sqrt{\frac{k_{s} g}{M g}}=\frac{1}{2 \pi} \sqrt{\frac{k_{s} g}{F_{e x t}}} \\
& =\frac{1}{2 \pi} \sqrt{\frac{100 \frac{l b}{f t}\left(32.2 \frac{f t}{s^{2}}\right)}{200 l b}}=0.64 \text { cycles } / \mathrm{sec} \\
& =1 \text { bounce every } 1.56 \mathrm{~s}
\end{aligned}
$$

(c) Using Eq. (15.28), we obtain the number $n_{\text {damage }}$ of cycles that will produce yielding/permanent-damage to diving board:

$$
\begin{aligned}
n_{\text {damage }} V_{0} & =V_{\text {yield }}=\frac{1}{2} k_{s}(\Delta x)_{y i e l d}^{2} \\
& \Rightarrow n_{\text {damage }}(25 f t \bullet l b)=\frac{1}{2}\left(100 \frac{l b}{f t}\right)(4 f t)^{2} \\
& \Rightarrow n_{\text {damage }}=32
\end{aligned}
$$

(d) With a loss factor of $L=0.1, \alpha=1-L=0.9$. The necessary condition for damage to the diving board,$$
\alpha_{\text {damage }}>\left[\frac{V_{\text {yield }}}{V_{0}+V_{\text {yield }}}\right]^{1 / N}
$$

If pulsing is done at strong resonance $(\mathrm{N}=1)$, then the necessary condition for $\alpha_{\text {damage }}$ is,

$$
\alpha_{\text {damage }}>\left[\frac{800 \mathrm{ft} \cdot \mathrm{lb}}{25 \mathrm{ft} \cdot \mathrm{lb}+800 \mathrm{ft} \cdot \mathrm{lb}}\right]^{1 / 1}=0.97
$$

Therefore, since $\alpha$ (determined from loss factor) is 0.9 , but the requirement for damage is $\alpha_{\text {damage }}>0.97$, then no damage to the diving board is expected when the loss factor is $L=0.1$.

# Problems 

1. An 18 -wheel truck (+ load) can weigh as much as $80,000 \mathrm{lb}$. As the truck crosses a 100 ft long bridge, the center of mass (CM) of the bridge undergoes vertical displacement of 0.2 ft . After the truck passes, the bridge eventually returns backs to its normal horizontal position.
(a) Find the effective spring constant for this bridge.
(b) Find the effective natural/resonant frequency $v$ for the bridge.
(c) What is the period for the bridge oscillations?

## Answers:

(a) $4.0 \times 10^{5} \mathrm{lb} / \mathrm{ft}$
(b) $2.02 \mathrm{Cyc} / \mathrm{s}$
(c) 0.5 s
2. For the bridge described in Problem 1, assume that the 18-wheelers are entering/ leaving the bridge at a rate of $45 \mathrm{Mi} / \mathrm{h}$.
(a) What is the truck transit time across the bridge?
(b) Is strong resonance for the bridge possible due sequential truck passage?
(c) Is it possible that a weaker resonant mode for the bridge can be activated by sequential truck passage?

## Answers:

(a) Transit time $=1.52 \mathrm{~s}$
(b) Strong resonance condition is unlikely since the transit time for truck of 1.52 s is greater than the minimum period for the bridge of 0.5 s .(c) Weaker resonance condition: Period for Bridge $=3 / v=1.5 \mathrm{~s}$. Since this is approximately equal to the transit time, weak resonance is possible.
3. For the bridge described in Problems 1 and 2, it is known that the bridge will start to yield for a vertical displacement of 1 ft . How many truck pulses (at the weaker resonant condition of $v / 3$ ) is needed to cause yielding/irreversible-damage to the bridge. (Assume no energy loss.)
(a) What is the energy input to the bridge per truck passage?
(b) What is the total energy that must go into the bridge to produce yielding (permanent damage to the bridge)?
(c) How many trucks must pass sequentially before permanent damage is done to the bridge.

# Answers: 

(a) $8000 \mathrm{ft}-\mathrm{lb}$
(b) $200,000 \mathrm{ft}-\mathrm{lb}$
(c) 25
4. Reconsider Problem 3, except this time find the dissipation factor for which damage will not occur to the bridge.

Answer: $L>0.0057 \%$
5. The center of mass (CM) of a tall flag pole is displaced (in the horizontal direction) by a distance of 0.5 ft . when acted upon by a constant horizontal wind of $20 \mathrm{mi} / \mathrm{h}$. When released, the CM of the flag pole returns to its normal position. Given that the force on the flag pole increases as the square of the wind speed, and assuming elastic behavior, find the horizontal displacement for the CM at a wind speed of $60 \mathrm{mi} / \mathrm{h}$.

Answer: 4.5 ft
6. For the tall flag pole described in Problem 5, suppose that the flag pole starts to show plastic behavior when the center of mass CM is displaced by 6 ft . At what wind speed does plastic-behavior/permanent-damage start to occur for the flag pole.

Answer: $69.3 \mathrm{mi} / \mathrm{h}$.
7. A tall flag pole weighs 600 lb . A horizontal steady wind speed of $20 \mathrm{mi} / \mathrm{h}$ displaces the center of mass of the pole by 0.5 ft . When the wind suddenly stops, the CM oscillates at 3 cycles/s. Given that the force on the pole increases as the square of the wind speed:
(a) find the effective external force acting on the CM to displace it 0.5 ft and
(b) what is the total input energy into the flag pole from the wind?

## Answers:

(a) 3312 lb
(b) $1656 \mathrm{ft}-\mathrm{lb}$8. Assuming that the flag pole (described in Problems 6 and 7) has no energy loss,
(a) how many $20 \mathrm{mi} / \mathrm{h}$ wind pulses (pulsing at flag pole resonance) are need to cause permanent damage to the flag pole?
(b) Assuming an energy loss factor of $L=0.1$, is it possible that a pulsating $20 \mathrm{mi} / \mathrm{h}$ wind (pulsing at resonance for the flag pole) can produce damage?

# Answers: 

(a) Assuming no energy loss factor, it will take 12 pulses from the wind to produce damage to the flag pole.
(b) For damage to occur, the loss factor $L$ must be: $L<0.077$. Since the stated loss factor is $L=0.1$, damage is impossible.

## Bibliography

Askeland, D. The Science and Engineering of Materials, $3^{\text {rd }}$ Ed., PWS Publishing, 1994. Bedford, A. and Liechti, K., Mechanics of Materials, Prentice Hall Publishing, 2000. Gere, J., Mechanics of Materials, $5^{\text {th }}$ Ed., Brooks/Cole Publishing, 2001.
Resnick, R., Halliday, D. and Krane, K., Physics, Vol.1, $4^{\text {th }}$ Ed., John Wiley and Sons, 1992.
Riley, K., Hobson, M. and Bence, S., Mathematical Methods for Physics and Engineering, Cambridge University Press, 1998.# Chapter 16 <br> Increasing the Reliability of Device/Product Designs 

Design engineers are continually asked reliability questions such as: (1) how long is your newly designed device/product expected to last and (2) how can you make costeffective design changes to improve the reliability robustness of the device? Often the designer will attempt to answer these questions by stating a safety factor $v$ which was used for a design:

$$
\xi_{\text {design }}=\xi_{\text {strength }} / \chi
$$

The safety factor, however, is only a qualitative indicator of the reliability margin of the designed device. It states that the designer tried to stay below the expected material's strength distribution by some safety factor $\chi$. For example, the designer may have used a safety factor of $\chi=2$. While this tends to give some degree of reliability assurance, the fundamental reliability question still remains: how long is the device/product expected to last, i.e., is the safety factor large enough or is it too large? If the safety factor $\chi$ is too small, then a reliability problem may occur with time (a very costly mistake). If the safety factor is too large, then the device/product may be over-designed (a very costly mistake). The previous chapters of this book emphasized that with accelerated testing data (this data may already exist in the literature) and using the modeled acceleration factors (which have been presented in this text for many of the potential failure mechanisms), one can answer the question: how long is your newly designed device/ product expected to last?

As one can surely appreciate, the design engineer is always working in a tight space where device reliability is one constraint and cost of the device is another, the proverbial rock and a hard place for the designer. Because of higher materials costs and/or higher device-performance demands, the designer is usually forced to design more aggressively (less conservative with respect to reliability) and must be able to answer the question: how long is the newly designed device/product expected to last? If the time-to-failure answer is millions of years, then it is likely a costly overdesign issue. If the time-to-failure answer is only one year, it could be a costlyreliability issue. In this chapter, design areas are emphasized where a relatively small design improvement could have a large impact on device reliability.

# 1 Reliability Enhancement Factor 

Many time-to-failure models have been presented in this text and these can be used to define a very useful expression, the reliability enhancement factor (REF):

$$
\mathrm{REF}=\frac{\mathrm{TF}_{\text {improved-design }}}{\mathrm{TF}_{\text {design }}}
$$

The REF should be $>1$ for an improvement in reliability. ${ }^{1}$ If REF $<1$, the improved design actually has reduced reliability (perhaps the changes were made for improved performance reasons, not for improved reliability reasons) and it tells the designer how much reduction in reliability/lifetime can be expected.

Several examples are shown in this chapter for improving the reliability of designs from both electrical and mechanical considerations. Since many device designs (electromechanical devices) have both electrical and mechanical aspects to the product reliability, inclusion of design examples from both electrical and mechanical engineering into this single chapter may be of significant value for all engineers. One will find that Eq. (16.2) is very helpful when one looks for design areas where a small design change can have a large impact on device reliability. The REF can be used to quickly estimate the impact on device reliability/lifetime when changes are made to the design.

## 2 Electromigration Design Considerations

Electromigration (EM)-induced voiding in conductors (electron wind forcing the metal ions to drift) generally occurs under high current densities $J$ and at elevated temperatures $T$. The design reliability enhancement factor REF for EM can be written as

[^0]
[^0]:    ${ }^{1} \mathrm{A} \mathrm{REF}=2$ means that the improved design should last 2 times longer than the original design, a $\mathrm{REF}=3$ means the improved design should last 3 times longer than the original design, etc.$$
\begin{aligned}
\operatorname{REF} & =\left(\frac{J_{\text {design }}-J_{\text {Crit }}}{J_{\text {improved-design }}-J_{\text {Crit }}}\right)^{n_{\mathrm{EM}}} \exp \left[\frac{Q_{E \mathrm{M}}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right] \\
& =\left[\frac{\left(\frac{l}{w t}\right)_{\text {design }}-J_{\text {crit }}}{\left(\frac{l}{w t}\right)_{\text {improved-design }}-J_{\text {crit }}} 1\right]^{n_{\mathrm{EM}}} \exp \left[\frac{Q_{E \mathrm{M}}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
\end{aligned}
$$

where $n_{\mathrm{EM}}=2$ and $Q_{\mathrm{EM}}=0.75 \mathrm{eV}$ are often used for aluminum-alloys, $n_{\mathrm{EM}}=1$ and $Q_{\mathrm{EM}}=1.0 \mathrm{eV}$ are often used for copper, and I is the current in the conductor of width $w$ and thickness t. $J_{\text {crit }}$ is usually negligible except for very short leads ( $<100 \mu \mathrm{~m}$ ). Changes in these design parameters can have a significant impact on REF. The REF value tells the designer how much longer the device/product will last if one uses the improved design parameters. One can see that, for long leads with Al-alloy metallization, reducing the design current density by $50 \%$ can produce a REF $=4$. This means that the expected lifetime increases by a factor of 4 (or a $300 \%$ improvement in lifetime).

The improved design temperature $T_{\text {improved design }}$ is usually achieved through lowering the device operating temperature. This is normally achieved by designing for lower device operating-power (reduced self-heating effects) and/or by improved heat dissipation. The improved heat dissipation can be achieved through the design use of more thermally conductive materials (e.g., $\mathrm{Cu}, \mathrm{SiC}, \mathrm{Si}$, diamond, etc.), heatsinks, air foils to improve convection heat losses, fans to improve air flow for better convection heat losses, or circulating fluids to improve heat losses (similar to circulating coolants in combustion engines). Assuming an activation energy of $Q$ $\sim 1 \mathrm{eV}$, a rough rule of thumb is: for each $10{ }^{\circ} \mathrm{C}$ drop in device operating temperature, the device will last $\sim 2$ times longer.

# 3 TDDB Design Considerations 

Time-dependent dielectric breakdown (TDDB) occurs when a dielectric is operated at elevated electric-fields $E$ and at elevated temperatures $T$. If one uses a conservative TDDB model, such as the E-Model, the REF for TDDB can be written as

$$
\begin{aligned}
\operatorname{REF} & =\exp \left[\gamma_{\mathrm{TDDB}} \cdot\left(E_{\text {design }}-E_{\text {improved-design }}\right)\right] \exp \left[\frac{Q_{\mathrm{TDDB}}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right] \\
& =\exp \left[\gamma_{\mathrm{TDDB}} \cdot\left(\frac{V_{\text {design }}-V_{\text {improved-design }}}{t_{\mathrm{ox}}}\right)\right] \exp \left[\frac{Q_{\mathrm{TDDB}}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
\end{aligned}
$$

The value of $\gamma_{\text {TDDB }}$ is temperature and dielectric-type dependent. For silica-based dielectrics (which are critically important for ICs), $\gamma$ is often approximated by: $\gamma_{\text {TDDB }}(T)=p_{\text {eff }} /\left(K_{B} T\right)$, where $p_{\text {eff }}=13 \mathrm{e} \AA$. Thus, at $105{ }^{\circ} \mathrm{C}(378 \mathrm{~K}), \gamma_{\text {TDDB }}=$ $4.0 \times 10^{-6} \mathrm{~cm} / \mathrm{V}$. The electric-field $E$ (which is the voltage $V$ drop in the dielectricdivided by the dielectric thickness $t_{\mathrm{ox}}$ ) generally plays a greater role in TDDB than does temperature. One can see that for a $1 \mathrm{MV} / \mathrm{cm}$ reduction in electric-field $E$, at a temperature of $105^{\circ} \mathrm{C}$, the dielectric lifetime due to TDDB will increase by at least 55 times. One can also see that even small changes in voltages are important when the gate oxide thickness $t_{\mathrm{ox}}$ is very thin. More optimistic models such as the 1/EModel or V-Model (for hyper-thin gate dielectrics $t_{\mathrm{ox}}<40 \AA$ ) have also been used. While the activation energy for TDDB is usually complicated by the fact that it is field dependent, an effective activation energy of $Q_{\mathrm{TDDB}}=0.3-0.6 \mathrm{eV}$ is often used for silica-based dielectrics.

# 4 Negative-Bias Temperature Instability Design Considerations 

Negative-bias temperature instability (NBTI) is a threshold voltage instability which occurs in p-channel MOSFET devices in CMOS IC technologies. Under device operation (presence of electric-field $E$ in the gate oxide) and at elevated temperatures $T$, the metastable $\mathrm{Si}-\mathrm{H}$ bonds (at the gate oxide/silicon interface) can start to break with the H -ions drifting away from this interface. This bondbreakage mechanism results in an increase in threshold voltage for the $p$-channel device and results in a corresponding reduction in p-channel drive-current. NBTI can result in failure for some CMOS circuits. The REF for NBTI can be written as

$$
\begin{aligned}
\mathrm{REF} & =\exp \left[\gamma_{\mathrm{NBTI}} \cdot\left(E_{\text {design }}-E_{\text {improved-design }}\right)\right] \exp \left[\frac{Q_{\mathrm{NBTI}}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\text {improved-design }}} \frac{1}{T_{\text {design }}}\right)\right] \\
& =\exp \left[\gamma_{\mathrm{NBTI}} \cdot\left(\frac{V_{\text {design }}-V_{\text {improved-design }}}{t_{\mathrm{ox}}}\right)\right] \exp \left[\frac{Q_{\mathrm{NBTI}}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\text {improved-design }}} \frac{1}{T_{\text {design }}}\right)\right]
\end{aligned}
$$

where $t_{\mathrm{ox}}$ is the gate oxide thickness. It is normally best practice to use your own empirically determined values for $\gamma$ and $Q$. However, if you do not have access to such accelerated data, sometimes the following values are used: $\gamma_{\mathrm{NBTI}}=3.2 \mathrm{~cm} / \mathrm{MV}$ and $Q_{\mathrm{NBTI}}=0.6 \mathrm{eV}$. Remember, one can always use more conservative values (lower values for $\gamma$ and $Q$ ). Note that for a $40 \AA$ gate dielectric, a reduction in gate voltage of only 0.1 V will produce an $\mathrm{REF}=2.23$ (a $2.23 \times$ improvement in NBTI lifetime).

## 5 HCI Design Considerations

Hot carrier injection (HCI) is generally an instability issue for n-channel devices in CMOS IC technologies. Due to electrons being accelerated laterally from source to drain in n-channel MOSFET devices, scattering will cause some of these hotelectrons to be redirected vertically into the gate oxide, thereby causing damage generally at the gate oxide/silicon interface. This interface damage tends to produce an increase in threshold voltage with a corresponding reduction in the drive current for n-channel devices. This type of device degradation may eventually result in circuit failure. The REF for the HCI-induced failure mechanism can be written as

$$
\begin{aligned}
\mathrm{REF} & =\exp \left[\alpha_{\mathrm{HCI}} \cdot\left(\frac{1}{V_{\text {improved-design }}}-\frac{1}{V_{\text {design }}}\right)\right] \exp \left[\frac{Q_{\mathrm{HCI}}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right] \\
& =\exp \left[\beta_{\mathrm{HCI}} \cdot\left(1-\frac{V_{\text {improved-design }}}{V_{\text {design }}}\right)\right] \exp \left[\frac{Q_{\mathrm{HCI}}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
\end{aligned}
$$

It is normally best practice to use empirically determined values for $\beta_{\mathrm{HCI}}$ and $Q_{\mathrm{HCI}}$ for your own devices. However, if you do not have access to such accelerated data, sometimes the following values are useful: $\beta_{\mathrm{HCL}}=30$ and $Q_{\mathrm{HCI}}$ is very small (sometimes positive, sometimes negative) but generally the activation energy is in the range: $-0.30 \mathrm{eV}<Q_{\mathrm{HCI}}<0.30 \mathrm{eV}$ ). Remember, one can always use more conservative values (lower values for $\beta_{\mathrm{HCI}}$ and $\mathrm{Q}_{\mathrm{HCI}}$ ). The voltage $V$ in Eq. (16.6) is the voltage drop from source gate edge to drain gate edge because this is the voltage drop that is accelerating the electrons. This may be a consideration for drain and/or source extended devices. Note that a $10 \%$ reduction in voltage may produce a REF $=20$ (a $20 \times$ improvement in HCI lifetime).

# 6 Surface Inversion Design Considerations 

MOSFET devices (especially threshold-dependent oxide-isolation devices) can suffer from surface inversion if mobile ions, such as $\mathrm{Li}^{+}, \mathrm{Na}^{+}$, and $\mathrm{K}^{+}$are accidentally incorporated in the silica-based dielectrics. The ions may drift under normal device operation. Accumulation of these drifted mobile ions at the silica/ silicon interface can cause Si surface inversion resulting in an unwanted leakage increase for oxideisolation devices. The REF for surface inversion due to mobile ions can be written as

$$
\begin{aligned}
R E F & =\left(\frac{E_{\text {design }}}{E_{\text {improved-design }}}\right) \exp \left[\frac{Q_{\text {Mobile-Ions }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right] \\
& =\left[\left(\frac{\left(V / t_{\mathrm{ox}}\right)_{\text {design }}}{\left(V / t_{\mathrm{ox}}\right)_{\text {improved-design }}}\right)\right] \exp \left[\frac{Q_{\text {Mobile-Ions }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
\end{aligned}
$$

For mobile ion-induced surface inversion, voltage is of relatively weak importance because it is a drift mechanism. Therefore, the burden of preventing mobile-ionreliability issues usually falls on manufacturing. The mobile-ion issues are usually resolved by material purity improvements and/or the use of layers which getter the mobile ions or serve as diffusion barriers. The activation energy for mobile ion-induced failures is generally high, with $Q_{\text {Mobile-Ions }}=1.0 \mathrm{eV}$ often used.

# 7 Creep Design Considerations 

Creep-induced failures can be very important in mechanical components. The REF for creep can be written as

$$
\mathrm{REF}=\left(\frac{\sigma_{\text {design }}-\sigma_{\text {yield }}}{\sigma_{\text {improved-design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }}} \exp \left[\frac{Q_{\text {creep }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
$$

where $\sigma$ is the mechanical stress in the material. ${ }^{2}$ Note that if the improved design stress $\sigma_{\text {improved design }}$ can be brought very close to the yield strength, then the REF goes to infinity. This means that, in theory, an infinite improvement in lifetime can be achieved and the device should never fail! However, as we have cautioned several times in this text, if even small cracks exist in the material, stress risers can develop at crack tips. These stress risers can serve to increase the local stress levels at crack tips (originally below the yield point without crack) to levels that easily exceed the yield point and degradation may occur. Thus, one should always question: does a yield stress really exist in the materials being used?

If the designer does not have creep data for the component materials being used in the design, then the following values can sometimes be useful: for soft metals (such as solder), $n_{\text {creep }}=3$ is often used; for strong metals, such as mild steels, $n_{\text {creep }}=5$ is often used; ${ }^{3}$ and, for very strong metals, $n_{\text {creep }}=7$ is sometimes used.

Since creep is usually a more severe problem at temperatures $>0.5 T_{\text {melt }}$, then the creep activation energy $Q_{\text {creep }}$ is usually close to the lattice-diffusion/bulk activation energy $Q_{\text {lattice-diffusion }}(1-4 \mathrm{eV})$.

The REF, Eq. (16.8), can be very helpful because the designer only needs to know the equations for the maximum stress in the material for a given loading. Fortunately, these equations may already exist and are often found in Strength of Materials, Solid Mechanics, Fracture Mechanics, and Materials Science textbooks. Several examples of creep will follow.

[^0]
[^0]:    ${ }^{2}$ Recall that the stress-level $\sigma_{\text {design }}$ must be greater than the yield-strength $\sigma_{\text {yield }}$ for creep to occur. ${ }^{3}$ The value of $n_{\text {creep }}=5$ is used so often in creep analysis that it is generally referred to as the literature as the five-power-law for creep behavior.# 7.1 Creep in Rotors 

Creep can be very important for mechanical components (rotors) that have to rotate with high angular speed $\omega$. The REF equation for a simple rotor (rotating mass attached to a light connecting rod) becomes:
$\operatorname{REF}=\left(\frac{\left(\frac{M r \omega^{2}}{A}\right)_{\text {design }}-\sigma_{\text {yield }}}{\left(\frac{M r \omega^{2}}{A}\right)_{\text {improved-design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }}} \exp \left[\frac{Q_{\text {creep }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]$.

Creep exponent data can usually be found in the literature for a given material. If such empirical data is unavailable to you, for strong metal-alloys, the kinetic values are sometimes used: $n_{\text {creep }}=4$ (likely a conservative value) and $Q_{\text {creep }}=1 \mathrm{eV}$ (likely a conservative value). One can see that for mechanical designs where creep in rotors can be an issue, the designer can dramatically improve reliability robustness by: reducing the angular velocity $\omega$ of the rotor, reducing the effective radius $r$ of the rotor, reducing the mass $M$ at the end of the rotor, and by increasing the crosssectional area $A$ of the connecting rod. Assuming that the yield stress is negligibly small and a creep exponent of $n_{\text {creep }}=4$, the REF goes as the 8 th power of angular speed $x$ and as the 4th power for the connecting arm length $r$, mass $M$ of rotor, and cross-sectional area $A$ of the connecting rod. Note that a $20 \%$ reduction in angular speed can produce a $\mathrm{REF}=6$, or a $500 \%$ increase in lifetime.

### 7.2 Creep in Pressurized Vessels

Creep can be a very important degradation mechanism for thin-walled vessels that are continually pressurized and then evacuated. The REF for creep can be written for a spherical thin-walled vessel as
$\operatorname{REF}=\left(\frac{\left(\frac{P r}{2 t}\right)_{\text {design }}-\sigma_{\text {yield }}}{\left(\frac{P r}{2 t}\right)_{\text {improved-design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }}} \exp \left[\frac{Q_{\text {creep }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]$.
$P$ is the pressure difference of the gas inside versus outside of the vessel, $r$ is the radius of the spherical vessel, $t$ is the thickness of the vessel wall, and it is assumed that $t \ll r$. Assuming that the yield stress is negligibly small and has a creep exponent of $n_{\text {creep }}=4$ (likely a conservative value), then the REF goes as the 4thpower of the gas pressure $P$, vessel radius $r$, and vessel thickness $t$. Note that a $20 \%$ increase in the thickness of the vessel can increase the REF to 2 , or a $100 \%$ increase in the expected lifetime. Also, as a caution, this analysis assumes that the gas in the vessel does not chemically react with or diffuse into the vessel material, thus possibly changing the material properties during the lifetime of the product. Finally, creep is strongly temperature dependent. A conservative value for the activation energy is $Q_{\text {creep }}=1.0 \mathrm{eV}$.

# 7.3 Creep in a Leaf Spring 

Creep can be a very important degradation mechanism in leaf springs when the beam is loaded. A simple leaf spring (illustrated in Fig. 16.1) is a rectangular beam of length $L$, width $b$ and thickness $t$. The leaf spring is supported at both ends and must carry a weight $W$.

One can write the REF for creep in a leaf spring as

$$
\operatorname{REF}=\left(\frac{\left(\frac{3 W L}{2 b t^{2}}\right)_{\text {design }}-\sigma_{\text {yield }}}{\left(\frac{3 W L}{2 b t^{2}}\right)_{\text {improved-design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }}} \exp \left[\frac{Q_{\text {creep }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]
$$

Assuming that the yield stress is negligible and the beam is made of a material that is hard/strong with a creep exponent of $n_{\text {creep }}=4$ (likely conservative), then the REF for this simple leaf spring goes as at least the 8th power of the thickness of the beam while the other beam design dimensions go as the 4th power. Therefore, if the designer goes with an improved design and increases the beam thickness by $20 \%$, then REF $=4.3$, or a $330 \%$ increase in lifetime. Also, creep is thermally activated with $Q_{\text {creep }}=1.0 \mathrm{eV}$ (likely conservative value).

Fig. 16.1 Leaf spring (bending beam) is shown
# 7.4 Stress Relaxation in Clamps/Fasteners 

Stress relaxation can induce failures for critically important clamping applications. The REF equation, for the stress relaxation (due to creep with an exponent of $n$ ) in a clamp/fastener, can be written as
$R E F=\left(\frac{\left(\sigma_{\max }\right)_{\text {design }}-\sigma_{\text {yield }}}{\left(\sigma_{\max }\right)_{\text {improved-design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }-1}} \exp \left[\frac{Q_{\text {creep }}}{K_{\mathrm{B}}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]$.

Assuming that a minimum clamping force $F$ must be maintained for adequate bolt and nut type clamping and that all stress relief occurs in the shaft of the bolt, then the REF for stress relaxation that is occurring in the shaft of the bolt of radius $r$ is given by
$\operatorname{REF}=\left(\frac{\left(\frac{F}{\pi r^{2}}\right)_{\text {design }}-\sigma_{\text {yield }}}{\left(\frac{F}{\pi r^{2}}\right)_{\text {improved }- \text { design }}-\sigma_{\text {yield }}}\right)^{n_{\text {creep }-1}} \exp \left[\frac{Q_{\text {creep }}}{K_{B}}\left(\frac{1}{T_{\text {improved-design }}}-\frac{1}{T_{\text {design }}}\right)\right]$.

Assuming negligible yield strength and that the shaft of the bolt is made of material that is reasonably hard/strong with a creep exponent of $n_{\text {creep }}=4$ (likely conservative), then one can see that the REF for stress relief goes as the 6th power of the radius of the shaft of the bolt. Note that a $20 \%$ increase in the bolt-shaft radius can result in an REF $=3$, or a $200 \%$ increase in lifetime. Also, creep is strongly temperature dependent with $Q_{\text {creep }}=1.0 \mathrm{eV}$ (likely a conservative value).

## 8 Fatigue Design Considerations

Fatigue can be a very important reliability issue for devices which undergo a cyclical stress. This can be an important failure mechanism for storage vessels that are continually pressurized and then evacuated; it can be an important failure mechanism for ICs that undergo continual power-up and power-down cycles; it can be an important failure mechanism for turbine blades that experience continual starting and stopping; it can be an important failure mechanism for light poles that must respond to continual changes in the wind speed and direction; etc. The REF equation due to cyclical stress can be written as$$
\operatorname{REF}=\left[\frac{(\Delta \sigma)_{\text {design }}-(\Delta \sigma)_{\text {elastic }}}{(\Delta \sigma)_{\text {improved-design }}-(\Delta \sigma)_{\text {elastic }}}\right]^{n_{\text {fatigue }}}
$$

where $\Delta \sigma$ is the total stress range and $(\Delta \sigma)_{\text {elastic }}$ is the part of the total stress range that is considered to be in the elastic region (where no degradation is expected). Note that the stress range $(\Delta \sigma)_{\text {elastic }}$ is analogous to the yield stress.

# 8.1 Fatigue in Storage Vessels 

Fatigue can be an important failure mechanism for a vessel that is continually pressured with a gas and then evacuated. The REF equation due to fatigue can be written as

$$
\begin{aligned}
\operatorname{REF} & =\left[\frac{(\Delta \sigma)_{\text {design }}-(\Delta \sigma)_{\text {elastic }}}{(\Delta \sigma)_{\text {improved-design }}-(\Delta \sigma)_{\text {elastic }}}\right]^{n_{\text {fatigue }}} \\
& =\left[\frac{\left(\frac{\Delta \sigma}{1-\left(\sigma_{\text {mean }} / \sigma_{\mathrm{TS}}\right)}\right)_{\text {design }}-(\Delta \sigma)_{\text {eleastic }}}{\left(\frac{\Delta \sigma}{1-\left(\sigma_{\text {mean }} / \sigma_{\mathrm{TS}}\right)}\right)_{\text {improved-design }}-(\Delta \sigma)_{\text {elastic }}}\right]^{n_{\text {fatigue }}}
\end{aligned}
$$

For a spherical vessel, of radius $r$ and metal thickness $t$, that is continually pressured to $P_{\max }$ then evacuated to $P_{\min }$, the stress range is given by:

$$
\Delta \sigma=\frac{\left(P_{\max }-P_{\min }\right) r}{2 t} \text { and } \sigma_{\text {mean }}=\frac{\left(P_{\max }-P_{\min }\right) r}{4 t}
$$

$\sigma_{\mathrm{TS}}$ is the tensile stress of the material used to make the spherical vessel. Assuming that the yield stress is negligible (because of cracks or other issues) and that the vessel is made of hard/strong metals, then $n_{\text {fatigue }}=4$ (likely conservative) can be used. From a design standpoint, one can see that fatigue can be minimized by keeping the pressure difference ( $P_{\max }-P_{\min }$ ) as small as possible, keeping the radius $r$ of the spherical vessel as small as possible, and selecting materials with high tensile strength $\sigma_{\mathrm{TS}}$.

### 8.2 Fatigue in Integrated Circuits (ICs)

Each time that an IC is powered up and then down, the device undergoes cyclical stress due to the thermal expansion mismatch in the materials used for IC fabrication. Since these are thermomechanical stresses, the REF equation for thermal cycling is often written as$$
\mathrm{REF}=\left[\frac{a_{\mathrm{ij}}\left[(\Delta T)-(\Delta T)_{\text {elastic }}\right]_{\text {design }}}{\alpha_{\mathrm{ij}}^{\prime}\left[(\Delta T)-(\Delta T)_{\text {elastic }}\right]_{\text {improved-design }}}\right]^{n_{\text {fatigue }}}
$$

where $\Delta T$ is the full thermal-cycling range and $a_{\mathrm{ij}}$ represents the thermal expansion mismatches for the materials of interest. $(\Delta T)_{\text {elastic }}$ represents the part of the total temperature range that is expected to be in the elastic range. Anything that can be done to minimize the thermal expansion mismatch of the materials and/or the temperature cycling range will improve $R E F$. An exponent of $\mathrm{n}_{\text {fatigue }}=4$ is often used for fatigue in ICs. If solder is the material failing, then perhaps $n_{\text {fatigue }}=2$ is more appropriate.

# Problems 

1. An IC designer worried about electromigration decides to increase the metal width of an aluminum-alloy conductor by $20 \%$. Assuming $\mathrm{J}_{\text {crit }}$ is negligibly small, how much of an increase in lifetime can the designer expect?

Answer: REF $=1.44$ (or a $44 \%$ increase in lifetime)
2. If the conductor in Problem 1 is copper, how much lifetime improvement can be expected with an increase in conductor width by $20 \%$ ?

Answer: REF $=1.2$ (or a $20 \%$ increase in lifetime)
3. If the temperature of the Al-alloy conductor in Problem 1 could be reduced from 105 to $95^{\circ} \mathrm{C}$ by using a heat sink, how much longer would the conductor be expected to last?

Answer: REF $=1.87$ (or a $87 \%$ increase in lifetime)
4. If the temperature of the copper conductor in Problem 2 could be reduced from 105 to $95^{\circ} \mathrm{C}$ by using a heat sink, how much longer would the conductor be expected to last?

Answer: REF $=2.30$ (or a $130 \%$ increase in lifetime)
5. A $45 \AA$ gate oxide MOSFET operates in inversion with a gate voltage of 2.7 V. How much would the TDDB lifetime increase if gate voltage is reduced to 2.5 V?

Answer: REF $=5.92$ (or a $492 \%$ increase in lifetime)
6. If the transistor described in Problem 5 is a p-channel MOSFET, how much would the NBTI lifetime increase if the gate voltage is reduced from 2.7 to 2.5 V ?

Answer: REF $=4.15$ (or a $315 \%$ increase in lifetime)7. If the transistor described in Problem 5 is a n-channel MOSFET, how much would the HCI lifetime increase if the device operating voltage is reduced from 2.7 to 2.5 V ?

Answer: $\mathrm{REF}=9.23$ (or a $823 \%$ increase in lifetime)
8. Assuming that a rotor's arm is made of a strong metal and that the operational stress in the rotor's arm is much greater than the materials yield point, what is the expected increase in creep lifetime if the length of the rotor's arm $r$ is reduced by $20 \%$ ?

Answer: $\mathrm{REF}=2.44$ (or $144 \%$ increase in lifetime)
9. Assuming that a thin-walled spherical storage vessel is made of a strong metal and that the operational stress is much greater than the materials yield point, what is the expected increase in creep lifetime if the thickness of the wall is increased by $30 \%$ ?

Answer: $\mathrm{REF}=2.86$ (or $186 \%$ increase in lifetime)
10. Assuming that a leaf spring is made of a strong metal and that the operational stress is much greater than the materials yield point, what is the expected increase in creep lifetime if the thickness of the spring is increased by $30 \%$ ?

Answer: $\mathrm{REF}=8.16$ (or $716 \%$ increase in lifetime)
11. Assuming that a nut and bolt type clamp is made of a strong metal and that the operational stress in the shaft of the bolt is much greater than the materials yield point, what is the expected increase in stress-relaxation lifetime if the radius of shaft is increased by $30 \%$ ?

Answer: $\mathrm{REF}=4.83$ (or $383 \%$ increase in lifetime)
12. Assuming that a thin-walled spherical storage vessel is made of a strong metal and that the operational stress is much greater than the materials yield point, what is the expected increase in fatigue lifetime if the allowed pressure range is decreased by $20 \%$ ?

Answer: $\mathrm{REF}=2.44$ (or $144 \%$ increase in lifetime)
13. Assuming that the elastic range is negligibly small and that a fatigue exponent of $n=4$ can be used for a plastic molded integrated circuit, what is the expected increase in IC thermal-cycling lifetime if the operational thermal range is decreased by $20 \%$ ?

Answer: $\mathrm{REF}=2.44$ (or $144 \%$ increase in lifetime)# Chapter 17 <br> Screening 

It would be a great accomplishment if we could simply design and build devices without defects. That should always be our goal-but, obtaining perfection is indeed a difficult/impossible challenge. Given that all devices will likely have a small fraction of the population which is defective, the question that we want to address in this chapter is: can a relatively short-duration stress be used to eliminate the defective/weak devices without causing significant degradation to the good/ strong devices? The use of a short-duration stress to eliminate weak devices is generally referred to as screening. We will find that screening can sometimes be very effective, but not always. Screening effectiveness depends on the exact details of the strength distribution for the devices plus the magnitude and duration of the screening stress.

## 1 Breakdown/Strength Distribution for Materials and Devices

In Chap. 10 we discussed ramp-to-failure/ramp-to-breakdown/ramp-to-rupture testing. In that chapter, a sample of the population of such devices/materials was randomly selected and the stress level $\xi$ was ramped (often in a linear fashion) until device/material failure was recorded. This ramp-to-breakdown sampling approach typically produces a breakdown distribution for $\xi_{\mathrm{BD}}$ similar to that illustrated in Fig. 17.1. A region $A$ of very low breakdown strengths can exist where these devices/materials will fail almost immediately after the normal operational stress $\xi_{\text {op }}$ is applied. A region $B$ of defective devices/materials can also exist where these devices/materials are strong enough to survive $\xi_{\text {op }}$ for a short period of time, but where they are too weak to survive for an extended period of time (a reliability problem). Region $B$ can be impacted by using a short screening stress $\xi_{\text {Screen }}$ to eliminate these weak devices/materials. However, while the application of $\xi_{\text {Screen }}$ tends to eliminate the devices/materials to the left of the screen, screening also

Fig. 17.1 Arbitrary device/material breakdown distribution is illustrated. Region $A$ is often referred to as a yield (or manufacturing) issue because these devices/materials will fail almost immediately after the normal operational stress $\xi_{\text {op }}$ is applied. Region $B$ devices will fail relatively shortly after the screening stress $\xi_{\text {Screen }}$ is applied. Region $C$ devices/materials can be severely weakened by the screen and some of these devices/materials may actually fail during the screen. The extent of Region $C$ depends on the magnitude and the length of time that the screening stress $\xi_{\text {Screen }}$ is used and how far removed the screening stress $\xi_{\text {Screen }}$ is from the strength $\xi_{\mathrm{BD}}$
weakens some of the devices/materials to the right of the screen. If more devices/ materials are eliminated to the left of the screen $\xi_{\text {Screen }}$ (in region $B$ ) than those that are severely weakened to the right of the screen (in region $C$ ) then the screen can have an overall positive impact on the reliability of the post-screened devices/ materials. However, if the screen severely weakens more devices/materials to the right of the screen (in region $C$ ) than it eliminates to the left of the screen (in region $B$ ), then the screen can have an overall adverse impact on the reliability of the postscreened devices/materials.

# 2 Impact of Screening Stress on Breakdown Strength 

The impact of a screening stress $\xi_{\text {Screen }}$ (and screening time $t_{\text {Screen }}$ ) on the devices/ materials to the left of the screening value is very simple. If $t_{\text {Screen }}>t_{0}$ (the time-tofail at breakdown), then all the devices/materials to the left of the screen will fail during the screen. However, the impact of screening on devices to the right of the screen is also an important reliability concern. In fact, this is the crucial reliability concern/question for screening and the answer will determine whether the overall reliability impact of the screen will have a positive or a negative impact on the postscreened devices.# 2.1 Screening Using Exponential TF Model 

From the exponential time-to-failure (TF) model presented in Chap. 11 one obtains:

$$
\mathbf{T F}_{\xi_{\mathrm{op}}}=t_{0} \exp \left[\gamma\left(\xi_{\mathbf{B D}}-\xi_{\mathbf{o p}}\right)\right]
$$

where: $t_{0}=1 /(\gamma R), R=\mathrm{d} \xi / \mathrm{d} t$, and $\gamma$ is the exponential stress parameter. Recall that $t_{0}$ is the time-to-failure when a stress level of $\xi=\xi_{\mathrm{BD}}$ is applied to the device/ material. $R$ is the ramp-rate (often linear) that is associated with increasing the stress during the ramp.

After the screening stress $\xi_{\text {Screen }}$ is applied for a time $t_{\text {Screen }}$, the screen will reduce time-to-failure for a device to the right of the screen (illustrated in Fig. 17.1) and this reduction in TF is given by:

$$
\mathrm{TF}_{\text {§op, Post Screen }}=t_{0} \exp \left[\gamma\left(\xi_{\mathrm{BD}}-\xi_{\mathrm{op}}\right)\right]-t_{\text {Screen }} \exp \left[\gamma\left(\xi_{\text {Screen }}-\xi_{\mathrm{op}}\right)\right]
$$

The reduction in TF can be expressed alternatively as a reduction in the original/ pre-screen breakdown strength $\xi_{\mathrm{BD}}$ :

$$
\begin{aligned}
\mathrm{TF}_{\text {§op, Post Screen }} & =t_{0} \exp \left\{\gamma\left[\left(\xi_{\mathrm{BD}}-\Delta \xi_{\mathrm{BD}}\right)-\xi_{\mathrm{op}}\right]\right\} \\
& =\exp \left[-\gamma \Delta \xi_{\mathrm{BD}}\right] \cdot \mathrm{TF}_{\text {§op }}
\end{aligned}
$$

where:

$$
\Delta \xi_{\mathrm{BD}}=\xi_{\mathrm{BD}, \text { Pre Screen }}-\xi_{\mathrm{BD}, \text { Post Screen }}
$$

Equating Eqs. (17.2) and (17.3), one obtains:

$$
\Delta \xi_{\mathrm{BD}}=\frac{1}{\gamma} \ln \left\{\frac{1}{1-\left(\frac{t_{\text {Screen }}}{t_{0}}\right) \exp \left[-\gamma\left(\xi_{\mathrm{BD}}-\xi_{\text {Screen }}\right)\right]}\right\}
$$

where: $\xi_{\mathrm{BD}}=\xi_{\mathrm{BD}, \text { Pre }}$ Screen and $t_{0}=1 /(\gamma R)$. Equation (17.5) describes the expected screening-induced degradation in breakdown strength $\Delta \xi_{\mathrm{BD}}$ (for devices to the right of the screening value in Fig. 17.1) when using an exponential TF model. Remember-for $t_{\text {Screen }}>t_{0}$, all of the devices to the left of the screening value $\xi_{\text {Screen }}$ are expected to fail during the screen.

The use of Eq. (17.5) is illustrated in Fig. 17.2. For the devices to the right of the screening value $\xi_{\text {Screen }}$, assuming that $t_{\text {Screen }}>t_{0}$, a region (1) develops in which the devices are expected to fail during $\mathrm{t}_{\text {Screen }}$. Adjacent to this is a region (2) in which the devices/materials do not fail during the screen but these devices/ materials are severely degraded by the screen. Past this severely degraded region is a region (3) of devices/materials where the degradation impact of the screen is rather small

Fig. 17.2 Screening-induced degradation $\Delta \xi_{\mathrm{BD}}$ for devices/materials to the right of the screening stress $\xi_{\text {Screen }}$ (region $C$ in Fig. 17.1). The screening-induced degradation can be large for a long screening time $t_{\text {Screen }}$ and/or when screening stress $\xi_{\text {Screen }}$ is close to the device/material breakdown strength $\xi_{\mathrm{BD}}$. Region (1) depicts devices that are expected to fail during the screen. Region (2) represents devices/materials that do not fail during the screen but that are severely degraded by the screen. Region (3) depicts devices where the screening-induced degradation is very small
and reduces sharply with screening stress when $\xi_{\text {Screen }}$ is much less than the pre-screen breakdown value $\xi_{\mathrm{BD}}$.

# Example Problem 1 

A sample of capacitors (with $\mathrm{SiO}_{2}$ dielectric) was randomly selected from a population of such capacitors. The electric field for each capacitor in the sample was ramped to failure at the expected operating temperature of $105^{\circ} \mathrm{C}$ with a linear ramp rate of $R=1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$. A median breakdown strength of $E_{\mathrm{BD}}=10.0 \mathrm{MV} / \mathrm{cm}$ was recorded. Assuming an exponential field acceleration parameter of $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$, the time-to-failure at $E=E_{\mathrm{BD}}$ was calculated to be $t_{0}=1 /(\gamma R)=0.25 \mathrm{~s}$. In order to weed out some of the low breakdowns in the population, a screening stress of $E_{\text {Screen }}=6.0 \mathrm{MV} / \mathrm{cm}$ was applied for 3 s . How much screening-induced degradation will occur for the median breakdown strength?

## Solution

Using Eq. (17.5), one obtains for the exponential TF model:$$
\begin{aligned}
\Delta E_{\mathrm{BD}} & =\frac{1}{\gamma} \ln \left\{\frac{1}{1-\left(\frac{t_{\text {Screen }}}{t_{0}}\right) \exp \left[-\gamma\left(E_{\mathrm{BD}}-E_{\text {Screen }}\right)\right]}\right\} \\
& =\frac{1}{4.0 \mathrm{~cm} / \mathrm{MV}} \ln \left\{\frac{1}{1-\left(\frac{3 \mathrm{~S}}{0.25 \mathrm{~S}}\right) \exp [-(4.0 \mathrm{~cm} / \mathrm{MV})(10-6) \mathrm{MV} / \mathrm{cm}]}\right\} \\
& =3.38 \times 10^{-7} \mathrm{MV} / \mathrm{cm} \\
& \cong 0 \mathrm{MV} / \mathrm{cm}
\end{aligned}
$$

Therefore, when using an exponential TF model for dielectric breakdown, one finds that a short 3 s capacitor stress at $6.0 \mathrm{MV} / \mathrm{cm}$ has virtually no impact on the median breakdown strength of $10.0 \mathrm{MV} / \mathrm{cm}$ (a reduction in breakdown strength of only $\left[\Delta E_{\mathrm{BD}} /(10 \mathrm{MV} / \mathrm{cm})\right] * 100 \%=0.00000338 \%$ ).

# 2.2 Screening Using Power-Law TF Model 

From the power-law time-to-failure (TF) model presented in Chap. 11, one obtains ${ }^{1}$ :

$$
\mathrm{TF}_{\xi_{\mathrm{op}}}=t_{0}^{*}\left(\frac{\xi_{\mathrm{BD}}}{\xi_{\mathrm{op}}}\right)^{n}
$$

where, $t_{0}^{*}=\xi_{B D} /[(n+1) R]$ and $R=d \xi / d t . t_{0}^{*}$ is the power-law model time-tofailure when a stress level of $\xi=\xi_{\mathrm{BD}}$ is applied to the device/material; $R$ is the ramprate (often linear) that is associated with increasing the stress with time during the ramp; and $n$ is the power-law exponent. One should note that (for a constant ramp rate $R$ ) $t_{0}$ is approximately constant for the exponential TF model but $t_{0}^{*}$ depends on $\xi_{\mathrm{BD}}$ when using the power-law model.

After the screening stress $\xi_{\text {Screen }}$ is applied for a time $t_{\text {Screen }}$, the screen will reduce the time-to-failure for a device to the right of the screening value $\xi_{\text {Screen }}$ (illustrated in Fig. 17.1) and is given by:

[^0]
[^0]:    ${ }^{1} \mathrm{~A}$ yield strength $\xi_{\text {Yield }}$ (see Chap. 13) has not been included in this power-law model. Since we are screening for defects, the assumption is made here that the defective units are unlikely to have a yield point.$$
\begin{aligned}
& \mathrm{TF}_{\xi \mathrm{op}, \text { Post Screen }}=t_{0}^{*}\left(\frac{\xi_{\mathrm{BD}}}{\xi_{\mathrm{op}}}\right)^{n}-t_{\text {Screen }}\left(\frac{\xi_{\text {Screen }}}{\xi_{\mathrm{op}}}\right)^{n} \\
& \quad=\frac{\xi_{\mathrm{BD}}}{(n+1) R}\left(\frac{\xi_{\mathrm{BD}}}{\xi_{\mathrm{op}}}\right)^{n}-t_{\text {Screen }}\left(\frac{\xi_{\text {Screen }}}{\xi_{\mathrm{op}}}\right)^{n}
\end{aligned}
$$

The reduction in TF can be expressed alternatively as a reduction in the original pre-screen breakdown strength $\xi_{\mathrm{BD}}$ :

$$
\mathrm{TF}_{\xi \mathrm{op}, \text { Post Screen }}=\frac{\xi_{\mathrm{BD}}-\Delta \xi_{\mathrm{BD}}}{(n+1) R}\left(\frac{\xi_{\mathrm{BD}}-\Delta \xi_{\mathrm{BD}}}{\xi_{\mathrm{op}}}\right)^{n}
$$

where:

$$
\Delta \xi_{\mathrm{BD}}=\xi_{\mathrm{BD}, \text { Pre Screen }}-\xi_{\mathrm{BD}, \text { Post Screen }}
$$

Equating Eqs. (17.7) and (17.8), one obtains:

$$
\Delta \xi_{\mathrm{BD}}=\xi_{\mathrm{BD}}\left\{1-\left[1-\frac{t_{\text {Screen }}}{t_{0}^{*}}\left(\frac{\xi_{\text {Screen }}}{\xi_{\mathrm{BD}}}\right)^{n}\right]^{1 /(n+1)}\right\}
$$

where: $\xi_{\mathrm{BD}}=\xi_{\mathrm{BD}, \text { Pre Screen }}$ and $t_{0}^{*}=\xi_{B D}[(n+1) R]$. Equation (17.10) describes the expected screening-induced degradation $\Delta \xi_{\mathrm{BD}}$, for devices to the right of the screening value in Fig. 17.1, when using a power-law TF model. Remember-for $t_{\text {screen }}>$ $t_{0}^{*}$, all the devices to the left of the screening value $\xi_{\text {screen }}$ are expected to fail during the screen.

In Fig. 17.3 we illustrate the impact of applying a screening stress $\xi_{\text {Screen }}$ for a time $t_{\text {screen }}>2 t_{0}^{*}$, using a power-law TF model with exponent $n$.

When screening devices/materials with the power-law TF model and with a low value exponent $n(\sim 2)$, a short duration screening stress $\xi_{\text {Screen }}$ can serve to weed out the very weak devices. But, the screening stress $\xi_{\text {Screen }}$ can also produce significant degradation $\Delta \xi_{\mathrm{BD}}$ to the good/strong devices/materials that were initially well above the screening value $\xi_{\text {Screen }}$. However, for high values of $n(>10)$ the degradation $\Delta \xi_{\mathrm{BD}}$ for the good/strong devices is relatively small except when $\xi_{\text {screen }}$ is very close to the initial $\xi_{\mathrm{BD}}$. Therefore, one would expect that screening might be more safely/ effectively implemented for hard metals (with $n \geq 5$ ) versus very soft metals such as solder $(n \sim 2)$. We should note that for time dependent dielectric breakdown (Chap. 12), a power-law model is sometimes used for very thin dielectrics ( $<5 \mathrm{~nm}$ ) and with a very high power-law exponent $n(\sim 40-48)$. Thus, screening dielectrics using a power-law TF model can potentially be very effective.

Fig. 17.3 Screening-induced degradation $\Delta \xi_{\mathrm{BD}}$ for good/strong devices when a screening stress $\xi_{\text {Stress }}$ is applied for a time of $t_{\text {Screen }}=2 t_{0}^{*}$. For power-law TF model, the screening-induced degradation for the good/strong devices is more significant when the power law exponent is low. For high values of $n(>10)$, the degradation for the good/strong devices is significant only when the screening stress is very close to the initial (pre-screen) breakdown strength of these devices/ materials

# Example Problem 2 

Reconsider Example Problem 1, except this time use a power-law TF model with $n=44$.

## Solution:

For the power-law model, the time-to-fail at breakdown is given by:

$$
t_{0}^{*}=E_{\mathrm{BD}} /[(n+1) R]=(10 \mathrm{MV} / \mathrm{cm}) /[(45)(1 \mathrm{MV} / \mathrm{cm} / \mathrm{s})]=0.22 \mathrm{~s}
$$

Using Eq. (17.10), one obtains:

$$
\begin{aligned}
\Delta E_{\mathrm{BD}} & =E_{\mathrm{BD}}\left\{1-\left[1-\frac{t_{\mathrm{Screen}}}{t_{0^{*}}}\left(\frac{E_{\mathrm{Screen}}}{E_{\mathrm{BD}}}\right)^{n}\right]^{1 /(n+1)}\right\} \\
& =(10 \mathrm{MV} / \mathrm{cm})\left\{1-\left[1-\frac{3 \mathrm{~s}}{0.22 \mathrm{~s}}\left(\frac{6.0 \mathrm{MV} / \mathrm{cm}}{10.0 \mathrm{MV} / \mathrm{cm}}\right)^{44}\right]^{1 /(45)}\right\} \\
& =(10 \mathrm{MV} / \mathrm{cm})\left\{5.25 \times 10^{-11}\right\} \\
& =5.25 \times 10^{-10} \mathrm{MV} / \mathrm{cm} \\
& \cong 0 \mathrm{MV} / \mathrm{cm}
\end{aligned}
$$

Therefore, when using a power-law TF model for dielectric breakdown, we see that a short 3 s capacitor stress at $6.0 \mathrm{MV} / \mathrm{cm}$ serves to produce virtually no

Fig. 17.4 Voltage breakdown distribution for 28 silica-based capacitors with dielectric thickness $200 \AA$. Normal operation for these capacitors is at 5 V . Region $A$ represents very weak capacitors that will result in a yield loss at 5 V . Region $B$ represents weak capacitors that will become a longer term reliability issue during 5 V operation. Region $C$ represents a region which is free of weak devices
degradation to the pre-screen median breakdown strength of $10.0 \mathrm{MV} / \mathrm{cm}$ (a reduction in breakdown strength of only $\left[\Delta E_{\mathrm{BD}} /(10 \mathrm{MV} / \mathrm{cm})\right] * 100 \%=$ $0.00000000525 \%)$.

# 3 Screening Effectiveness 

For a screen to be effective (an overall positive impact on post-screen device/ materials reliability), one must look closely at the details of the breakdown distribution plus the magnitude and duration of the screening stress. We will consider cases where the screen is effective (increases the reliability of the post-screen devices) as well as cases where the screen is not effective.

In Fig. 17.4 we show a normal-distribution plotting ${ }^{2}$ of the ramp-to-breakdown values for 28 randomly selected capacitors with a $\mathrm{SiO}_{2}$ dielectric thickness of $200 \AA$. The breakdown values were obtained by ramping the electric field to breakdown using a ramp rate of $R=1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$. One can see that region $A$ consists of 4 capacitors ( $\sim 14 \%$ of capacitors) that have a breakdown less than 5 V . Region $B$ has three weak capacitors ( $\sim 11 \%$ of capacitors) with breakdowns between 5 and 12 V . Region $C$ represents the separation between the weak devices in region $B$ and the strong part (majority) of the distribution.

[^0]
[^0]:    ${ }^{2}$ Recall from Chap. 6-to convert the standard deviation Z-value to cumulative fraction $F$ of devices, use the Excel Function: $F=$ NORMSDIST(Z).# 3.1 Screening Effectiveness Using Exponential TF Model 

We want to investigate the potential reliability impact of applying a voltage screen $V_{\text {Screen }}$ for a time $t_{\text {Screen }}$ to the devices/capacitors shown in Fig. 17.4. Recall that this distribution was obtained by ramping the electric field with a linear ramp rate of $R=$ $1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$ at the expected operational temperature of $105^{\circ} \mathrm{C}$. At $105^{\circ} \mathrm{C}$, the field acceleration parameter is given by $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$. This gives a time-to-failure at breakdown of $t_{0}=1 /[\gamma R]=0.25 \mathrm{~s}$.

Table 17.1 shows the impact of screening on the breakdown distribution ( $V_{\mathrm{BD}}$ $\Delta V_{\mathrm{BD}}$ ) when a screening stress $V_{\text {Screen }}$ is applied for a time of $t_{\text {Screen }}=2.5 \mathrm{~s} . \Delta V_{\mathrm{BD}}$ in this table is determined using Eq. (17.5) for the exponential model. In Table 17.1 we can see the pre-screen breakdown distribution, as well as the expected post-screen breakdown distributions after 7,8 or 9 V screening. The dashed table entries ( - ) mean that the degradation was severe enough to cause these devices to fail during the screen.

As for screening effectiveness, the 7 V screen in Table 17.1 was ineffective because it only eliminates the very low breakdowns in region $A$ (see Fig. 17.4). However, these devices would have normally been eliminated anyway with a simple 5 V operational test. Also, the 7 V screen tended to weaken the region $B$ devices thus making them even more likely to become a post-screen reliability problem during normal 5 V operation. The 8 V screen in Table 17.1 was only partially effective-it did eliminate one of the three weak devices in region $B$ but the remaining two devices in region $B$ were significantly weakened by the 8 V screen, thus making them even more likely to become a post-screen reliability problem during normal 5 V operation. The 9 V screen in Table 17.1 worked extremely well- all three weak devices in region $B$ were eliminated without having a significant adverse impact on the breakdown of post-screened good/strong devices.

### 3.2 Screening Effectiveness Using Power-Law TF Model

We now want to investigate the reliability impact of applying a voltage screen $V_{\text {Screen }}$, to the devices/capacitors shown in Fig. 17.4, except this time we want to use a power-law model (with $n=44$, from Chap. 12). Recall that for the power-law TF model, the time-to-failure at breakdown is given by $t_{0}{ }^{*}=E_{B D} /[(n+1) R]$. The degradation caused by the screen on the breakdown strength $\Delta V_{\mathrm{BD}}$ is given by Eq. (17.10) for the power-law model.

Table 17.2 shows the impact of screening on the breakdown distribution ( $V_{\mathrm{BD}}$ $\Delta V_{\mathrm{BD}}$ ) when a screening stress $V_{\text {Screen }}$ is applied for a time $t_{\text {Screen }}=2.5 \mathrm{~s}$. In Table 17.2 one can see the pre-screen breakdown distribution as well as the predicted post-screen breakdown distributions after $7,8,9$, or 10 V screening. The dashed table entries ( - ) means that the degradation was severe enough to eliminate these weak devices during the screen. The 7 V screen was ineffective because it onlyTable 17.1 Impact of voltage screening on capacitor breakdown distribution (using exponential TF model)

| $t_{\text {ox }}=2.00 \mathrm{E}-06 \mathrm{~cm}$ <br> $\gamma=4.0 \mathrm{E}-06 \mathrm{~cm} / \mathrm{V}$ <br> $R=\mathrm{d} E / \mathrm{d} t=1.0 \mathrm{E}+06 \mathrm{~V} / \mathrm{cm} / \mathrm{s}$ <br> $t_{0}=1 /(\gamma R)=0.25 \mathrm{~s}$ <br> $V_{\text {Screen }}=7,8$, or 9 V <br> $t_{\text {screen }}=2.5 \mathrm{~s}$ |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | Exponential TF model |  |
| Cap | $V_{\text {BD }}$ (volts) <br> (pre-screen) | F | Z | Post <br> 7 V screen <br> $\left(V_{\mathrm{BD}}-\Delta V_{\mathrm{BD}}\right)$ | Post <br> 8 V screen <br> $\left(V_{\mathrm{BD}}-\Delta V_{\mathrm{BD}}\right)$ |
| 1 | 1.00 | 0.025 | $-1.966$ | — | — |
| 2 | 2.00 | 0.060 | $-1.556$ | — | — |
| 3 | 2.50 | 0.095 | $-1.310$ | — | — |
| 4 | 3.50 | 0.130 | $-1.125$ | — | — |
| 5 | 9.00 | 0.165 | $-0.972$ | 8.90 | — |
| 6 | 9.50 | 0.201 | $-0.839$ | 9.47 | 9.16 |
| 7 | 10.00 | 0.236 | $-0.720$ | 9.99 | 9.90 |
| 8 | 25.00 | 0.271 | $-0.609$ | 25.00 | 25.00 |
| 9 | 25.25 | 0.306 | $-0.506$ | 25.25 | 25.25 |
| 10 | 25.50 | 0.342 | $-0.408$ | 25.50 | 25.50 |
| 11 | 25.75 | 0.377 | $-0.314$ | 25.75 | 25.75 |
| 12 | 26.00 | 0.412 | $-0.222$ | 26.00 | 26.00 |
| 13 | 26.25 | 0.447 | $-0.133$ | 26.25 | 26.25 |
| 14 | 26.50 | 0.482 | $-0.044$ | 26.50 | 26.50 |
| 15 | 26.75 | 0.518 | 0.044 | 26.75 | 26.75 |
| 16 | 27.00 | 0.553 | 0.133 | 27.00 | 27.00 |
| 17 | 27.25 | 0.588 | 0.222 | 27.25 | 27.25 |
| 18 | 27.50 | 0.623 | 0.314 | 27.50 | 27.50 |
| 19 | 27.75 | 0.658 | 0.408 | 27.75 | 27.75 |
| 20 | 28.00 | 0.694 | 0.506 | 28.00 | 28.00 |
| 21 | 28.25 | 0.729 | 0.609 | 28.25 | 28.25 |
| 22 | 28.50 | 0.764 | 0.720 | 28.50 | 28.50 |
| 23 | 28.75 | 0.799 | 0.839 | 28.75 | 28.75 |
| 24 | 29.00 | 0.835 | 0.972 | 29.00 | 29.00 |
| 25 | 29.25 | 0.870 | 1.125 | 29.25 | 29.25 |
| 26 | 29.50 | 0.905 | 1.310 | 29.50 | 29.50 |
| 27 | 29.75 | 0.940 | 1.556 | 29.75 | 29.75 |
| 28 | 30.00 | 0.975 | 1.966 | 30.00 | 30.00 |

eliminated the very low breakdowns in region $A$ (refer to Fig. 17.4). The 7 V screen in Table 17.2 had virtually no impact on region $B$ devices. As one can see, the 8 V screen also had little impact on the region $B$ devices. The 9 V screen in Table 17.2 was only partially effective-it did eliminate two of the three weak devices in region $B$, but the 9 V screen also served to weaken the remaining post-screen device inTable 17.2 Impact of voltage screening on capacitor breakdown distribution (using power-law TF model)

| $t_{\text {ox }}=2.00 \mathrm{E}-06 \mathrm{~cm}$ <br> $n=44$ <br> $R=\mathrm{d} E / \mathrm{d} t=1.00 \mathrm{E}+06 \mathrm{~V} / \mathrm{cm} / \mathrm{s}$ <br> $V_{\text {Screen }}=7,8,9$, or 10 V <br> $t_{\text {screen }}=2.5 \mathrm{~s}$ <br> $t_{o^{*}}=E_{\mathrm{BD}} /[(n+1) R]$ |  |  |  | Power-law TF model |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Cap\# | $V_{\text {BD }}$ (volts) <br> (pre-screen) | F | Z | Post 7 V screen $\left(V_{\mathrm{BD}}-\right.$ $\left.\Delta V_{\mathrm{BD}}\right)$ | Post 8 V screen $\left(V_{\mathrm{BD}}-\right.$ $\left.\Delta V_{\mathrm{BD}}\right)$ | Post 9 V screen $\left(V_{\mathrm{BD}}-\right.$ $\Delta V_{\mathrm{BD}}$ ) | Post 10 V screen $\left(V_{\mathrm{BD}}-\right.$ $\Delta V_{\mathrm{BD}}$ ) |
| 1 | 1.00 | 0.025 | $-1.966$ | - | - | - | - |
| 2 | 2.00 | 0.060 | $-1.556$ | - | - | - | - |
| 3 | 2.50 | 0.095 | $-1.310$ | - | - | - | - |
| 4 | 3.50 | 0.130 | $-1.125$ | - | - | - | - |
| 5 | 9.00 | 0.165 | $-0.972$ | 9.00 | 8.97 | - | - |
| 6 | 9.50 | 0.201 | $-0.839$ | 9.50 | 9.50 | - | - |
| 7 | 10.00 | 0.236 | $-0.720$ | 10.00 | 10.00 | 9.95 | - |
| 8 | 25.00 | 0.271 | $-0.609$ | 25.00 | 25.00 | 25.00 | 25.00 |
| 9 | 25.25 | 0.306 | $-0.506$ | 25.25 | 25.25 | 25.25 | 25.25 |
| 10 | 25.50 | 0.342 | $-0.408$ | 25.50 | 25.50 | 25.50 | 25.50 |
| 11 | 25.75 | 0.377 | $-0.314$ | 25.75 | 25.75 | 25.75 | 25.75 |
| 12 | 26.00 | 0.412 | $-0.222$ | 26.00 | 26.00 | 26.00 | 26.00 |
| 13 | 26.25 | 0.447 | $-0.133$ | 26.25 | 26.25 | 26.25 | 26.25 |
| 14 | 26.50 | 0.482 | $-0.044$ | 26.50 | 26.50 | 26.50 | 26.50 |
| 15 | 26.75 | 0.518 | 0.044 | 26.75 | 26.75 | 26.75 | 26.75 |
| 16 | 27.00 | 0.553 | 0.133 | 27.00 | 27.00 | 27.00 | 27.00 |
| 17 | 27.25 | 0.588 | 0.222 | 27.25 | 27.25 | 27.25 | 27.25 |
| 18 | 27.50 | 0.623 | 0.314 | 27.50 | 27.50 | 27.50 | 27.50 |
| 19 | 27.75 | 0.658 | 0.408 | 27.75 | 27.75 | 27.75 | 27.75 |
| 20 | 28.00 | 0.694 | 0.506 | 28.00 | 28.00 | 28.00 | 28.00 |
| 21 | 28.25 | 0.729 | 0.609 | 28.25 | 28.25 | 28.25 | 28.25 |
| 22 | 28.50 | 0.764 | 0.720 | 28.50 | 28.50 | 28.50 | 28.50 |
| 23 | 28.75 | 0.799 | 0.839 | 28.75 | 28.75 | 28.75 | 28.75 |
| 24 | 29.00 | 0.835 | 0.972 | 29.00 | 29.00 | 29.00 | 29.00 |
| 25 | 29.25 | 0.870 | 1.125 | 29.25 | 29.25 | 29.25 | 29.25 |
| 26 | 29.50 | 0.905 | 1.310 | 29.50 | 29.50 | 29.50 | 29.50 |
| 27 | 29.75 | 0.940 | 1.556 | 29.75 | 29.75 | 29.75 | 29.75 |
| 28 | 30.00 | 0.975 | 1.966 | 30.00 | 30.00 | 30.00 | 30.00 |

region $B$, thus making this device more prone to failure during normal operation. The 10 V screen in Table 17.2 was very effective-it eliminated all three weak devices in region $B$ without producing significant degradation to the main group of good/strong devices.When comparing Tables 17.1 and 17.2, we see that for either the power-law model (with $n=44$ ) or for the exponential model (with $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$ ), the models tend to give similar screening results. However, in order to achieve nearly identical screening results, a somewhat higher voltage was required when using the powerlaw model. However, the higher voltage screen ( 10 V ), needed by the power-law model to eliminate all the bad/weak devices in region $B$, did not seem to harm the good/strong devices (devices above region $C$ ).

# Example Problem 3 

A metal component must operate safely under a normal tensile stress of 5 kpsi . Ultimate tensile strength $\sigma_{\mathrm{TS}}$ data was collected for a random sample of 28 such components using a linear ramp rate of $R=\mathrm{d} \sigma / \mathrm{d} t=2 \mathrm{kpsi} / \mathrm{min}$ at the expected component operating temperature. The $\sigma_{\mathrm{TS}}$ data is shown in the figure below using a power-law model with $n=5$. Evaluate the overall reliability impact if these devices were screened with $\sigma_{\text {Screen }}=7,8,9$, or 10 kpsi for a screening duration of $t_{\text {Screen }}=10 \mathrm{~min}$. Which of these screens would be the preferred screening approach? (Assume that the preferred screening approach is the one that eliminates more bad/weak components but creates the least amount of degradation to the good/strong components.)


## Solution:

The time-to-failure at breakdown using the power-law model is given by: $t_{0}{ }^{*}$ $=\sigma_{T S} /[(n+1) R]$. Using the power-law TF model with $n=5$, the degradation $\Delta \sigma_{\mathrm{TS}}$ to the pre-screen ultimate tensile strength $\sigma_{\mathrm{TS}}$ due to a screening stress $\sigma_{\text {Screen }}$ acting for a duration of $t_{\text {Screen }}=10 \mathrm{~min}$ is given by Eq. (17.10):

$$
\Delta \sigma_{\mathrm{TS}}=\sigma_{\mathrm{TS}}\left\{1-\left[1-\frac{t_{\mathrm{Screen}}}{t_{0}^{*}}\left(\frac{\sigma_{\mathrm{Screen}}}{\sigma_{\mathrm{TS}}}\right)^{n}\right]^{1 /(n+1)}\right\}
$$

The equation above is used to calculate the degradation $\Delta \sigma_{\mathrm{TS}}$ for each of the pre-screen ultimate tensile strengths and this is shown in the table below.The dashed table entries ( - ) mean that the degradation was severe enough to eliminate these defective/weak devices during the screen.

Note that the 7 kpsi screen in the table above has optimal screening effectiveness. It screens out all of the weak devices (ultimate tensile strengths of $\sigma_{\mathrm{TS}} \leq 10 \mathrm{kpsi}$ ) and it also produces the least amount of degradation to the strong devices ( $\sigma_{\mathrm{TS}} \geq 25 \mathrm{kpsi}$ ). Also, note that when the power-law exponent $n$ is low (less than 10), as this example problem with $n=5$, at least some amount of screening-induced degradation $\Delta \sigma_{\mathrm{TS}}$ extends even into the very strongest devices in the distribution.

| $n=5$ <br> $R=\mathrm{d} \sigma / \mathrm{d} t=2 \mathrm{kpsi} / \mathrm{min}$ <br> $\sigma_{\text {Screen }}=7,8,9$ or 10 kpsi <br> $t_{\text {Screen }}=10 \mathrm{~min}$ <br> $t_{0}{ }^{*}=\sigma_{\mathrm{TS}} /[(n+1) R]$ |  |  |  | Power-law model |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Component <br> \# | $\begin{gathered} \sigma_{\text {TS }} \\ \text { (kpsi) } \\ \text { (pre-screen) } \end{gathered}$ | F | Z | Post <br> 7 kpsi screen $\left(\sigma_{\mathrm{TS}}-\right.$ $\left.\Delta \sigma_{\mathrm{TS}}\right)$ | Post <br> 8 kpsi screen $\left(\sigma_{\mathrm{TS}}-\right.$ $\left.\Delta \sigma_{\mathrm{TS}}\right)$ | Post <br> 9 kpsi screen $\left(\sigma_{\mathrm{TS}}-\right.$ $\left.\Delta \sigma_{\mathrm{TS}}\right)$ | Post <br> 10 kpsi screen $\left(\sigma_{\mathrm{TS}}-\right.$ $\Delta \sigma_{\mathrm{TS}}$ ) |
| 1 | 1.00 | 0.025 | $-1.966$ | - | — | — | — |
| 2 | 2.00 | 0.060 | $-1.556$ | - | — | — | — |
| 3 | 2.50 | 0.095 | $-1.310$ | - | — | — | — |
| 4 | 3.50 | 0.130 | $-1.125$ | - | — | — | — |
| 5 | 9.00 | 0.165 | $-0.972$ | - | — | — | — |
| 6 | 9.50 | 0.201 | $-0.839$ | - | — | — | — |
| 7 | 10.00 | 0.236 | $-0.720$ | - | — | — | — |
| 8 | 25.00 | 0.271 | $-0.609$ | 24.97 | 24.93 | 24.88 | 24.79 |
| 9 | 25.25 | 0.306 | $-0.506$ | 25.22 | 25.19 | 25.13 | 25.05 |
| 10 | 25.50 | 0.342 | $-0.408$ | 25.47 | 25.44 | 25.39 | 25.31 |
| 11 | 25.75 | 0.377 | $-0.314$ | 25.72 | 25.69 | 25.64 | 25.57 |
| 12 | 26.00 | 0.412 | $-0.222$ | 25.97 | 25.94 | 25.90 | 25.83 |
| 13 | 26.25 | 0.447 | $-0.133$ | 26.22 | 26.20 | 26.15 | 26.09 |
| 14 | 26.50 | 0.482 | $-0.044$ | 26.47 | 26.45 | 26.41 | 26.34 |
| 15 | 26.75 | 0.518 | 0.044 | 26.73 | 26.70 | 26.66 | 26.60 |
| 16 | 27.00 | 0.553 | 0.133 | 26.98 | 26.95 | 26.92 | 26.86 |
| 17 | 27.25 | 0.588 | 0.222 | 27.23 | 27.21 | 27.17 | 27.12 |
| 18 | 27.50 | 0.623 | 0.314 | 27.48 | 27.46 | 27.42 | 27.37 |
| 19 | 27.75 | 0.658 | 0.408 | 27.73 | 27.71 | 27.68 | 27.63 |
| 20 | 28.00 | 0.694 | 0.506 | 27.98 | 27.96 | 27.93 | 27.88 |
| 21 | 28.25 | 0.729 | 0.609 | 28.23 | 28.21 | 28.18 | 28.14 |
| 22 | 28.50 | 0.764 | 0.720 | 28.48 | 28.47 | 28.44 | 28.39 |
| 23 | 28.75 | 0.799 | 0.839 | 28.73 | 28.72 | 28.69 | 28.65 || 24 | 29.00 | 0.835 | 0.972 | 28.98 | 28.97 | 28.94 | 28.90 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 25 | 29.25 | 0.870 | 1.125 | 29.23 | 29.22 | 29.19 | 29.16 |
| 26 | 29.50 | 0.905 | 1.310 | 29.48 | 29.47 | 29.45 | 29.41 |
| 27 | 29.75 | 0.940 | 1.556 | 29.74 | 29.72 | 29.70 | 29.66 |
| 28 | 30.00 | 0.975 | 1.966 | 29.99 | 29.97 | 29.95 | 29.92 |

# Problems 

1. A randomly selected sample of capacitors was ramped-to-failure using a ramp rate of $R=1 \mathrm{MV} / \mathrm{cm} / \mathrm{s}$ at $105^{\circ} \mathrm{C}$. What is the time-to-failure $t_{0}$ at the breakdown field of $10 \mathrm{MV} / \mathrm{cm}$ and at $105^{\circ} \mathrm{C}$ ? Assume an exponential TF model with a field acceleration parameter of $\gamma=4.0 \mathrm{~cm} / \mathrm{MV}$.

Answer: $t_{0}=0.25 \mathrm{~s}$
2. A randomly selected sample of capacitors was ramped-to-failure using a ramp rate of $R=1 \mathrm{MV} / \mathrm{cm} / \mathrm{sec}$ at $105^{\circ} \mathrm{C}$. What is the time-to-failure $t_{0}^{*}$ at the breakdown field of $10 \mathrm{MV} / \mathrm{cm}$ and at $105^{\circ} \mathrm{C}$ ? Assume a power-law TF model with an exponent of $n=44$.

Answer: $t_{0}^{*}=0.22 \mathrm{~s}$
3. For the capacitors described in Problem 1 above, calculate the screening-induced degradation $\Delta E_{\mathrm{BD}}$ for a capacitor with a pre-screen breakdown strength of $10 \mathrm{MV} / \mathrm{cm}$. Assume that the screen is conducted with stressing field of 9 MV for 5 s .

Answer: $\Delta E_{\mathrm{BD}}=0.11 \mathrm{MV} / \mathrm{cm}$
4. For the capacitors described in Problem 2 above, calculate the screening-induced degradation $\Delta E_{\mathrm{BD}}$ for a capacitor with a pre-screen breakdown strength of $10 \mathrm{MV} / \mathrm{cm}$. Assume that the screen is conducted with stressing field of 9 MV for 5 s .

Answer: $\Delta E_{\mathrm{BD}}=0.055 \mathrm{MV} / \mathrm{cm}$
5. Toxic gas lines/pipes are expected to operate at a normal pressure of 4 kpsi . To insure that the metal pipes can reliably withstand the normal operating pressure, a random selection of such pipes was taken and the pressure was ramped-to-rupture with a ramp rate of $1 \mathrm{kpsi} / \mathrm{min}$ at the expected operating temperature. The median pre-screen rupture strength was determined to be 12 kpsi . Calculate the expectedscreening-induced degradation to the median pre-screen rupture strength if a screening stress of 6 kpsi is applied for 1 min .
(a) Assume a power-law exponent of $n=4$.
(b) Assume a power-law exponent of $n=7$.

Answers: (a) $\Delta P_{\mathrm{BD}}=0.063 \mathrm{kpsi}$ and (b) $\Delta P_{\mathrm{BD}}=0.0078 \mathrm{kpsi}$
6. Using the information found in Table 17.1, determine the screening effectiveness of using a 23 V screen and the degradation impact to the good/strong devices.

Answer: Comparing the 9 and 23 V screens, with the exponential TF model, the 23 V screen is excessive-it does not eliminate anymore defects than does the 9 V screen; in addition, the 23 V screen produces more degradation $\left(\Delta \mathrm{V}_{\mathrm{BD}}\right)$ for the good/strong devices.
7. Using the details found in Table 17.2, describe the screening effectiveness of using a 23 V screen and the degradation impact to the good/strong devices.

Answer: Comparing the 10 and 23 V screens, with the power-law TF model, the 23 V is excessive-it does not eliminate anymore weak devices than does the 10 V screen; in addition, the 23 V screen produces more degradation $\left(\Delta V_{\mathrm{BD}}\right)$ for the good/strong devices.
8. Using the details found in Example Problem 3, describe the screening effectiveness of using a 14 psi stress and the degradation impact to the good/strong devices.

Answer: Comparing the 7 kpsi and 14 kpsi screens, we see that the 14 kpsi screen is excessive-it does not eliminate anymore defects than does the 7 kpsi screen; in addition, the 14 kpsi screen causes more degradation $\left(\Delta \sigma_{\mathrm{TS}}\right)$ to the good/strong components.
9. A randomly selected group of 28 gas cylinders was ramped-to-rupture (using a ramp rate of $0.50 \mathrm{kpsi} / \mathrm{min}$ at the expected operational temperature) and the following rupture values (in units of kpsi ) were obtained: $26.50,1.00,26.25$, $2.00,26.00,2.50,25.75,3.50,25.25,9.00,25.00,9.50,25.50,10.00,26.75$, $28.00,30.00,27.00,27.25,29.75,29.50,29.25,29.00,28.75,28.50,28.25$, 27.75 , and 27.50 . Assuming an operational pressure of 2 kpsi and a power-law. TF model with an exponent of $n=5$, evaluate the screening impact/effectiveness of applying a screening pressure of $1,2,3$, or 4 kpsi for 1 min .
(a) Plot the rupture data as a normal distribution (Z-plot from Chap. 5).
(b) Identify the gas cylinder rupture values that represent a yield loss.
(c) Identify the gas cylinder rupture values that represent a reliability risk.
(d) What is the screening effectiveness when using a $1,2,3$, or 4 kpsi screen for 1 min ? Which is the optimal screen for this group of cylinders?# Answers: 

(b) Five rupture values less $\leq 2 \mathrm{kpsi}$ represent a yield loss.
(c) Three rupture values between 2 and 6 kpsi represent a reliability risk.
(d) A screen of at least 4 kpsi for 1 min is needed to eliminate all weak components without producing significant degradation to the good/strong components. This represents the optimal screen for the four screening conditions presented.# Chapter 18 <br> Heat Generation and Dissipation 

The adverse impact of temperature on device/material reliability has been emphasized often in this book. The degradation rate for most devices/materials tends to accelerate exponentially with increasing temperature. ${ }^{1}$ Therefore, for reliability reasons, lower temperature device operation is usually preferred. However, many devices (both electrical and mechanical) can generate significant amounts of heat as they are being operated. Once device operation begins, the rate of increase in temperature of the device/material will depend upon on the heat generation within the device, the heat capacity of the materials, and the heat dissipation from the device to the heat sink (which is often the ambient). Elevated device temperature during operation (versus the ambient temperature) creates a thermal gradient which serves to drive heat flow from the device. In thermal equilibrium the heat dissipation from the device will just match the heat generation within the device. Managing device heat dissipation may require a significant engineering effort-but the improvements in reliability can be worth the effort.

## 1 Device Self-Heating and Heat Transfer

Many devices generate heat during operation. Examples of heat generation during device operation are abundant: combustion engines, furnaces, rockets, resistors, transistors, transformers, our bodies, etc. We refer to such devices (which generate heat during normal operation) as self-heating devices because no external heating source is necessarily needed to elevate device temperature during operation.

Combustion engines, furnaces and rockets generate self heat through the burning of fuels (exothermic chemical reactions). Electric motors, generators, transformers,

[^0]
[^0]:    ${ }^{1}$ In Chap. 12 (Sec. 7) a failure mechanism (Hot Carrier Injection) was discussed that can be contrary to this general statement.

Fig. 18.1 Device operation often produces heat generation $G$ (depicted here by the conventional symbol for an electrical resistor which generates heat when a current flows through it). The heat generation will cause the temperature of the volume to increase. Heat flux $J_{H}$ from the volume will occur in a direction from higher temperature to lower. Thermal equilibrium will occur when the heat flow from the generation volume just matches the heat generation within the volume
relays, resistors, and transistors generate self heat through Joule heating processes. Our bodies generate heat through metabolic processes (burning of food) and through frictional processes (muscle to muscle interactions, tendons to muscle interactions, ligament to bone interactions, etc.). The heat generation in all devices must be eventually dissipated or a catastrophic rise in device temperature can occur. Figure 18.1 illustrates the heat dissipation/flow/transfer needed to prevent overheating.

In Fig. 18.1 we illustrate the dissipation/flow/transfer/flux of heat which is needed to prevent the generation volume from overheating (excessive temperature rise during device operation). As heat is generated within the volume, the temperature within this region will increase relative to its surroundings. The thermal gradient created will thus serve to drive heat flow from the higher temperature generation volume to the lower temperature surroundings/ambient. The rate at which the temperature will increase within the generation volume will be determined by the input power, the heat capacity of the materials within the volume, and the heat dissipation rate. Thermal equilibrium will be established when the heat dissipation rate from the volume just matches the heat generation rate within the volume.

# 1.1 Energy Conservation 

We need to develop a dynamical equation that can be used to describe heat generation, temperature rise and heat dissipation. We first start with a statement of energy conservation (First Law of Thermodynamics):

Heat Generated $=$ Heat Absorbed + Heat Transferred.If no heat is being generated then we simply have:

$$
\text { Heat Absorbed }=-\text { Heat Transferred. }
$$

Equation (18.2) states that: under the conditions of no heat generation, the heat absorbed must be equal but opposite to the heat transferred. Heat absorption (or loss) by a material will raise (or lower) the internal energy $U$. The internal energy of a system is the sum of the kinetic and potential energy of the atoms in the system. ${ }^{2}$ If the specific heat $c^{3}$ and mass $M$ of the material are known, then a change in internal energy $\Delta U$ due to heat flow can be determined ${ }^{4}$ :

$$
\Delta U=M \int_{T_{1}}^{T_{2}} c(T) \mathrm{d} T
$$

For cases where the specific heat $c$ is approximately constant over the temperature range of interest, Eq. (18.3a) simply reduces to:

$$
\Delta U=M c\left(T_{2}-T_{1}\right)=M c \Delta T
$$

The specific heat, thermal conductivity and density of selected materials are shown in Table 18.1. Note that water is an excellent cooling agent-not only because of its relative abundance but also due to the fact that its specific heat is relatively high. ${ }^{5}$

The heat/thermal capacity $C_{\mathrm{Th}}$ of a constant volume $V$ of material is given by:

$$
C_{\mathrm{Th}}=\int c(\boldsymbol{x}) \rho(\boldsymbol{x}) \mathrm{d} V
$$

where $c(\boldsymbol{x})$ is the specific heat at constant volume and $\rho(\boldsymbol{x})$ is the density of the material at the location $\boldsymbol{x}=\left(x_{1}, x_{2}, x_{3}\right)$ within the volume $V$. One should remember

[^0]
[^0]:    ${ }^{2}$ The term external energy is usually reserved for any relative motion of the macroscopic system and/or any system energy associated with external fields.
    ${ }^{3}$ Often the specific heat is subscripted as $c_{v}$ (specific heat at constant volume) or $c_{p}$ (specific heat at constant pressure). This textbook will use $c=c_{v}$.
    ${ }^{4}$ In general, the internal energy of a system can be changed by the flow of Heat (into or out of system) and/or by Work (done on or by system). The conservation of energy statement ( $\mathrm{d} U=\delta$ Heat $+\delta$ Work) is often referred to as the First Law of Thermodynamics. $\delta$ Heat and $\delta$ Work imply that these are not exact differentials. Thus, before we can integrate, we must know details of the processes by which the heat is changed and/or how the work is performed.
    ${ }^{5}$ Using Eq. (18.3b) and solving for $\Delta T$, you can see that water (due to its relatively large specific heat) is capable of absorbing significant amounts of heat with only relatively small changes in its temperature. Now you can perhaps better understand why water is an excellent cooling agent and widely used-from nuclear reactors and combustion engines to fire fighting.Table 18.1 Specific heat, density and thermal conductivity for selected materials at $25^{\circ} \mathrm{C}$

| Material | Density $\left[10^{3} \mathrm{~kg} / \mathrm{m}^{3}\right]$ | Specific heat <br> $[\mathrm{kJ} /(\mathrm{kg} \mathrm{K})]$ | Thermal conductivity <br> $[\mathrm{kW} /(\mathrm{m} \mathrm{K})]$ |
| :-- | :-- | :-- | :-- |
| Silicon | 2.33 | 0.69 | 0.084 |
| Aluminum | 2.69 | 0.90 | 0.250 |
| Copper | 8.96 | 0.39 | 0.400 |
| Lead | 11.36 | 0.13 | 0.030 |
| Gold | 19.32 | 0.13 | 0.310 |
| Granite | 2.70 | 0.79 | 0.002 |
| Silicon nitride | 3.20 | 0.63 | 0.033 |
| Silicon dioxide | 2.60 | 0.84 | 0.001 |
| Water | 1.00 | 4.19 | 0.0006 |

Note that the units of specific heat $c$, as shown in table, are in units utilizing the temperature in Kelvin. Often you will see the specific heat $c$ also expressed in units of ${ }^{\circ} \mathrm{C}$. This is acceptable if you are only using it to calculate a temperature difference because $\Delta T(\mathrm{~K})=\Delta T\left({ }^{\circ} \mathrm{C}\right)$.
The specific heat of a material is approximately independent of temperature above its Debye temperature, which can be $25^{\circ} \mathrm{C}$ or less for many materials
that thermal capacity $C_{\mathrm{Th}}$ is the ability to store heat for an incremental increase in temperature. It is analogous to electrical capacitance which is the ability to store charge for an incremental increase in voltage. Also, remember the analogy- current flows due to a potential difference and heat flows due to a thermal difference. Similarly, electrical resistances impede current flow and thermal resistances impede heat flow. Thus, similar to electrical resistances, one can think of thermal resistances as being in either series or in parallel (as illustrated in Problems 1, 2 and 3 at the end of this chapter).

# 1.2 General Heat Flow Equation 

Let us now reconsider Eq. (18.1) in its general form (when we have heat generation, absorption and dissipation) and let us suppose that the heat generation region (shown in Fig. 18.1) is an infinitesimal unit volume such that Eq. (18.1) can be written as:

$$
g(\boldsymbol{x}, t)=\rho(\boldsymbol{x}) c(\boldsymbol{x}) \frac{\partial[T(\boldsymbol{x}, t)]}{\partial t}+\vec{\nabla} \cdot \vec{J}_{H}(\boldsymbol{x}, t)
$$

Here, $g(\boldsymbol{x}, t)$ is the heat generation per unit time, per unit volume (power density); $\boldsymbol{x}=\left(x_{1}, x_{2}, x_{3}\right)$ represents the position coordinates; $t$ is the time; $\rho(\boldsymbol{x})$ is the density of the material within the unit volume; $c(\boldsymbol{x})$ is the specific heat of the material within the unit volume; $T(\boldsymbol{x}, t)$ is the temperature within the unit volume; and $J_{H}(\boldsymbol{x}, t)$ is the heat flux from the unit volume. The heat flux $J_{H}$ from the generation region is driven by a temperature gradient and is described by Fourier's Law:$$
\tilde{J}_{H}(\boldsymbol{x}, t)=-\bar{\kappa} \cdot \vec{\nabla} T(\boldsymbol{x}, t)
$$

where the temperature $T(\boldsymbol{x}, t)$ is a function of the position coordinates $\boldsymbol{x}$ and time $t$. The thermal conductivity $\kappa$ is, in general, a tensor (direction dependent). The negative sign in Fourier's law is needed to ensure that heat will always flow in a direction from higher temperature to lower temperature. If the material in volume $V$ (through which the heat flows) is homogeneous and isotropic, then $\kappa$ is simply a scalar. Fourier's Law is very important because it tells us that heat will spontaneously flow as long as a temperature difference/gradient exists. This is illustrated in Example Problem 1.

# Example Problem 1 

An aluminum block of 1 kg mass at $25^{\circ} \mathrm{C}$ and with a specific heat of $c_{\mathrm{Al}}=$ $0.90 \mathrm{~kJ} /(\mathrm{kg} \mathrm{K})$ is brought into thermal contact with a copper block of 1 kg mass at $500^{\circ} \mathrm{C}$ and with a specific heat of $c_{\mathrm{Cu}}=0.39 \mathrm{~kJ} /(\mathrm{kg} \mathrm{K})$. Assuming that the blocks are perfectly thermally insulated on all sides, except for their thermal contact interface, find the equilibrium temperature for the two blocks after they are brought into thermal contact as illustrated below. Assume that no heat generation exists in this example problem, only heat conduction.


## Solution

Let us start with the conservation of energy and write:

$$
U_{\mathrm{Al}}+U_{\mathrm{Cu}}=\text { constant }
$$

Thus, conservation of energy implies:

$$
\Delta U_{\mathrm{Al}}=-\Delta U_{\mathrm{Cu}}
$$

This means that the heat/energy gained by the Al block must be equal to the heat/energy lost by the Cu block. Thus, using the previous equation plus Eq. (18.3b) one can write:$$
\begin{aligned}
& M_{\mathrm{Al}} c_{\mathrm{Al}} \Delta T_{\mathrm{Al}}=-M_{\mathrm{Cu}} c_{\mathrm{Cu}} \Delta T_{\mathrm{Cu}} \\
& \Rightarrow M_{\mathrm{Al} C_{\mathrm{Al}}}\left(T_{\text {final }}-T_{\text {initial }}\right)_{\mathrm{Al}}=-M_{\mathrm{Cu}} c_{\mathrm{Cu}}\left(T_{\text {final }}-T_{\text {initial }}\right)_{\mathrm{Cu}}
\end{aligned}
$$

According to Fourier's Law, heat will continue to flow until $\left(T_{\text {final }}\right)_{\mathrm{Al}}=$ $\left(T_{\text {final }}\right)_{\mathrm{Cu}}=T_{\text {equilibrium }}$, therefore:

$$
M_{\mathrm{Al} C_{\mathrm{Al}}}\left(T_{\text {equilibrium }}-T_{0, \mathrm{Al}}\right)=M_{\mathrm{Cu}} c_{\mathrm{Cu}}\left(T_{0, \mathrm{Cu}}-T_{\text {equilibrium }}\right)
$$

Solving for the equilibrium temperature, one obtains:

$$
\begin{aligned}
T_{\text {equilibrium }} & =\frac{M_{\mathrm{Al}} c_{\mathrm{Al}} T_{0, \mathrm{Al}}+M_{\mathrm{Cu}} c_{\mathrm{Cu}} T_{0, \mathrm{Cu}}}{M_{\mathrm{Al}} c_{\mathrm{Al}}+M_{\mathrm{Cu}} c_{\mathrm{Cu}}} \\
& =\frac{1 \mathrm{~kg}\left(0.90 \frac{\mathrm{~kJ}}{\mathrm{~kgK}}\right)(298 \mathrm{~K})+1 \mathrm{~kg}\left(0.39 \frac{\mathrm{~kJ}}{\mathrm{~kgK}}\right)(773 \mathrm{~K})}{1 \mathrm{~kg}\left(0.90 \frac{\mathrm{~kJ}}{\mathrm{~kgK}}\right)+1 \mathrm{~kg}\left(0.39 \frac{\mathrm{~kJ}}{\mathrm{~kgK}}\right)} \\
& =441.6 \mathrm{~K}=168.6^{\circ} \mathrm{C}
\end{aligned}
$$

Therefore, when the blocks come into thermal equilibrium, in a perfectly insulated container, each block should be at a temperature of approximately $169^{\circ} \mathrm{C}$.

If we now return to Eq. (18.5) and integrate over the entire volume $V$ of interest (which contains the generation region plus all the material(s) between the generation region and heat sink) then we obtain:

$$
\int_{V} g(x, t) \mathrm{d} V=\int_{V} \rho(x) c(x) \frac{\partial[T(x, t)]}{\partial t} \mathrm{~d} V+\int_{V} \vec{\nabla} \cdot \vec{J}_{H}(x, t) \mathrm{d} V
$$

Assuming that the heat generation is uniform within the generation region $V_{\text {Gen }}$ (and zero elsewhere) and using the divergence theorem, ${ }^{6}$ we can write:

[^0]
[^0]:    ${ }^{6}$ Recall that the divergence theorem states:
    $\int_{V} \vec{\nabla} \cdot \vec{J} \mathrm{~d} V=\int_{A} \vec{J} \cdot \mathrm{~d} \vec{A}$, where $V$ is the volume of interest which is bounded by a surface of area $A$.$$
G(t)=\int_{V} \rho(x) c(x) \frac{\partial[T(x, t)]}{\partial t} \mathrm{~d} V+\int_{A} \vec{J}_{H}(x, t) \cdot \mathrm{d} \vec{A}
$$

where $G(t)=g(t) V_{\text {Gen }}$ is the input power (heat generation per unit time) in the generation volume $V_{\text {Gen }}$ and where $A$ is the area of the surface which bounds the volume $V$ of interest.

# 2 Steady-State Heat Dissipation 

Let us now consider cases where the heat generation in $V_{\text {Gen }}$ is independent of time [ $G(t)=G_{0}=$ constant] and let us further assume that the entire volume $V$ of interest is in thermal equilibrium, i.e.,

$$
\frac{\partial[T(x, t)]}{\partial t}=0
$$

Thus, under the conditions of thermal equilibrium, the heat capacities of the materials play no role and Eq. (18.8) reduces to:

$$
G_{0}=\int_{A} \vec{J}_{H}(x) \cdot \mathrm{d} \vec{A}
$$

Equation (18.10) simply states that in thermal equilibrium, the heat generation rate within the volume of interest must be equal to the heat dissipation rate (the heat per unit time which crosses the surface of area $A$ enclosing the volume $V$ of interest).

In Fig. 18.2 we show a rectangular metal plate which is embedded in a material of volume $V$ with uniform thermal conductivity $\boldsymbol{\kappa}$. The embedded plate is then placed in thermal contact with a heat sink at constant temperature of $T_{\text {Sink. }}{ }^{7}$ The rectangular plate is heated at a constant generation rate of $G_{0}$. The question that we would like to address is-for a constant input power of $G_{0}$ into the metal plate, what is the highest temperature that $T_{\text {Gen }}$ will reach before the metal plate will come into thermal equilibrium with its surroundings?

If, in Fig. 18.2, the material thickness $S_{0}$ is much less than the other material dimensions $\left(S_{i \neq 0}\right)$, then the lowest thermal resistance path is from the bottom of the metal plate to the heat sink; and, this will be the dominant heat flow path. Under these conditions, and using Eq. (18.6), then Eq. (18.10) simply reduces to:

[^0]
[^0]:    ${ }^{7}$ In heat flow analysis, the heat sink fixes the temperature at specified locations and plays a role similar to the use of ground in electrical circuits.

Fig. 18.2 Rectangular metal plate is embedded in a material of volume $V$ with uniform thermal conductivity $\boldsymbol{\kappa}$. The embedded plate is in thermal contact with a heat sink. $S_{0}$ is the thickness of the material between the plate and heat sink. The thickness $S_{0}$ will be assumed to be much less than the other material dimensions $\left(S_{i \neq 0}\right)$. The volume $V$ of interest contains the materials in the generation region (the metal plate) plus all the materials between the heat generation region and the heat sink. The top/bottom surface of this thin metal plate has an area of $A_{0}$

$$
\begin{gathered}
G_{0}=\int_{A} \vec{J}_{H}(x) \cdot \mathrm{d} \vec{A} \\
\cong J_{H} A_{0}=-\kappa\left(\frac{\Delta T}{\Delta x}\right) A_{0}=\kappa\left(\frac{T_{\mathrm{Gen}}-T_{\mathrm{Sink}}}{S_{0}}\right) A_{0}
\end{gathered}
$$

where $A_{0}$ is the heat dissipation area. ${ }^{8}$ Therefore, the equilibrium temperature of the rectangular metal plate becomes:

$$
T_{\mathrm{Gen}}=T_{\mathrm{Sink}}+G_{0}\left(\frac{S_{0}}{\kappa A_{0}}\right)
$$

where $S_{0}$ is the thickness of the material between $T_{\text {Gen }}$ and $T_{\text {Sink }}, \kappa$ is the thermal conductivity of the material between $T_{\text {Gen }}$ and $T_{\text {Sink }}$, and $A_{0}$ is the heat dissipation area.

Often Eq. (18.12) is simply expressed as a maximum temperature increase/rise $\Delta T_{\max }$ :

[^0]
[^0]:    ${ }^{8}$ Actually, not all of the heat flow (from metal plate bottom surface area $A_{0}$ ) is vertically downward. Part of the heat flow will be from the metal plate spreading laterally. Thus, the true heat flow across the surface area $A$, which bounds the volume $V$ of interest, will be through an effective area $A_{\text {eff }}$ such that $A_{\text {eff }}>A_{0}$. However, if $S_{0}$ is much less than the metal plate dimensions (length and width), then $A_{\text {eff }} \approx A_{0}$.$$
\Delta T_{\max }=T_{\mathrm{Gen}}-T_{\mathrm{Sink}}=\left(\frac{S_{0}}{\kappa A_{0}}\right) G_{0}=\theta \cdot \text { Power }
$$

where $\theta$ will be referred to as the thermal resistance and is given by:

$$
\theta=\left(\frac{S_{0}}{\kappa A_{0}}\right)
$$

Since the input power $G_{0}$ is often expressed in the units Watts (W), then the thermal resistance $\theta$ (in this textbook) will be expressed in units $\left({ }^{\circ} \mathrm{C} / \mathrm{W}\right)$.

# Example Problem 2 

Assume that the embedded metal plate shown in Fig. 18.2 is being heated electrically (either by resistive or inductive methods) with a constant input power of 10 W . Find the maximum temperature rise for the embedded metal plate assuming that: the metal plate bottom surface area is $5 \mathrm{~cm}^{2}$, the plate is embedded in a material with thermal conductivity $\kappa=12 \mathrm{~mW} /{ }^{\circ} \mathrm{C} \mathrm{cm}$ and the thickness of the material between the metal plate and the heat sink is $S_{0}=1.0$ cm . Furthermore, assume that $S_{0}$ is much smaller than all the other material dimensions $\left(S_{i \neq 0}\right)$.

## Solution

The thermal resistance $\theta$ can be modeled/estimated using Eq. (18.14):

$$
\theta=\left(\frac{S_{0}}{\kappa A_{0}}\right)=\frac{1.0 \mathrm{~cm}}{\left(12 \mathrm{~mW} /{ }^{\circ} \mathrm{C}-\mathrm{cm}\right)\left(5 \mathrm{~cm}^{2}\right)}=16.7^{\circ} \mathrm{C}
$$

The maximum temperature rise $\Delta T_{\max }$ of the metal plate relative to the heat sink is given by Eq. (18.13):

$$
\begin{aligned}
\Delta T_{\max }=T_{\mathrm{Gen}}-T_{\mathrm{Sink}}= & \theta \cdot \text { Power }=(16.7^{\circ} \mathrm{C} / \mathrm{W})(10 \mathrm{~W}) \\
& =167^{\circ} \mathrm{C}
\end{aligned}
$$

Therefore, for the embedded metal plate described, which is dissipating a power of 10 W , the metal plate temperature will rise to a maximum of $167^{\circ} \mathrm{C}$ above heat sink temperature. At this elevated temperature, the heat dissipation rate from the metal plate will just match the heat generation rate within the plate and the system will come into thermal equilibrium. In thermal equilibrium, the elevated temperature of the plate will remain at a constant level as long as the input power level remains constant.# 3 Effective Thermal Resistance 

The thermal resistance from $T_{\text {Gen }}$ to $T_{\text {Sink }}$ (for the metal plate shown in Fig. 18.2) was easy to model/estimate, as described in Example Problem 2. However, there will often be heat flow problems when a theoretical modeling of the thermal resistance is quite difficult and/or time-consuming. Such an example is illustrated in Fig. 18.3.

In Fig. 18.3 we see that the heat generation region is non-symmetrical which makes heat dissipation modeling difficult. Second, this heat generation region is surrounded (non-symmetrically) by several materials with different thermal conductivities that also add to the modeling complexity. Under such complex modeling conditions, it is often easier to simply measure the effective thermal resistance (from the generation region temperature $T_{\text {Gen }}$ to the ambient region at temperature $T_{\text {Amb }}$ ) than it is to try to model the thermal resistance. The effective thermal resistance is given by:

$$
\theta_{\mathrm{eff}}=\frac{\Delta T}{\text { Power }}=\frac{T_{\mathrm{Gen}}-T_{\mathrm{Amb}}}{\text { Power }}
$$

A common experimental approach is to simply dissipate a known amount of fixed power in the generation region and then measure the equilibrium temperature rise of the generation region versus the ambient temperature (with a thermal sensor placed very close to or within the generation region).


Fig. 18.3 An arbitrary heat generation region is illustrated which is quite complicated (has little/no symmetry) and it is surrounded by a non-symmetrical arrangement of various material types with different thermal conductivities. When analyzing heat flow problems such as this, which possess little/no symmetry, it is often easier to simply measure the effective thermal resistance $\theta_{\text {eff }}$ (between the generation region and heat sink/ambient) rather than trying to model the thermal resistance. Here, the volume $V$ of interest contains the material in the heat generation region plus all the materials between the heat generation region and heat sink (which is the ambient in this illustration). The heat dissipation area $A$ is the area of the surface which bounds the volume $V$# Example Problem 3 

In the assembly process for ICs, a silicon chip is often attached to a metal-pad/ lead-frame and then the chip and lead-frame assembly is molded in plastic. The plastic is then cured and then the assembly goes through trim and formwhich creates the pins which protrude from the package. Finally, the pins are soldered to a circuit board. This assembly/arrangement is illustrated below.


For normal IC operation, the heat generation region within the chip is located near the top of the silicon chip where the diffusions/junctions reside. For this reason, usually one speaks in terms of chip junction-temperature as being the critical reliability care-about. Once the packaged IC is soldered onto a circuit board and the device is operated, as illustrated above, the rise in the device temperature will generally produce some natural convection air flow. The thermal resistance $\theta_{\mathrm{JC}}$ (from chip junction to plastic-case surface) is often measured rather than modeled. The thermal resistance $\theta_{\mathrm{CA}}$ (from case surface to ambient) can likewise be measured.

In this example problem, let us assume that the chip dissipates a constant power of $1 \mathrm{~W} .{ }^{9} \mathrm{~A}$ metal sensor on the chip records a steady-state chip junctiontemperature of $60^{\circ} \mathrm{C}$. A thermocouple was used to measure the steady-state plastic-case surface temperature (above the chip) and it was found to be $35^{\circ} \mathrm{C}$. A steady-state ambient air temperature of $25^{\circ} \mathrm{C}$ was recorded using a thermometer located a relatively great distance from the device.
(a) What is the effective thermal resistance $\theta_{\mathrm{JC}}$ that exists between the chip junction and the plastic-case surface?
(b) What is the effective thermal resistance $\theta_{\mathrm{CA}}$ that exists between the plasticcase surface and the ambient air?

[^0]
[^0]:    ${ }^{9}$ Remember, the chip power $P$ is given simply by: $P=($ Current $) \times($ Voltage $)$.(c) What is the expected silicon chip steady-state junction temperature when the IC dissipates a constant power of 3.2 W ?

# Solution: 

(a) The effective thermal resistance between chip junction and plastic-case surface is given by:

$$
\begin{aligned}
\left(\theta_{\mathrm{JC}}\right)_{\mathrm{eff}} & =\frac{\Delta T}{\text { Power }}=\frac{T_{\mathrm{Gen}}-T_{\mathrm{Case}}}{\text { Power }} \\
& =\frac{(60-35)^{\circ} \mathrm{C}}{1 \mathrm{~W}} \\
& =25^{\circ} \mathrm{C} / \mathrm{W}
\end{aligned}
$$

(b) The effective thermal resistance between plastic-case surface and ambient is given by:

$$
\begin{aligned}
\left(\theta_{\mathrm{CA}}\right)_{\mathrm{eff}} & =\frac{\Delta T}{\text { Power }}=\frac{T_{\mathrm{Case}}-T_{\mathrm{Amb}}}{\text { Power }} \\
& =\frac{(35-25)^{\circ} \mathrm{C}}{1 \mathrm{~W}} \\
& =10^{\circ} \mathrm{C} / \mathrm{W}
\end{aligned}
$$

(c) The effective thermal resistance between the chip junction and the ambient is given by:

$$
\begin{aligned}
\left(\theta_{\mathrm{JA}}\right)_{\mathrm{eff}} & =\left(\theta_{\mathrm{JC}}\right)_{\mathrm{eff}}+\left(\theta_{\mathrm{CA}}\right)_{\mathrm{eff}}=(25+10)^{\circ} \mathrm{C} / \mathrm{W} \\
& =35^{\circ} \mathrm{C} / \mathrm{W}
\end{aligned}
$$

The maximum chip junction-temperature rise during constant 3.2 W operation becomes:

$$
\begin{aligned}
\Delta T_{\max } & =T_{\text {Junction }}-T_{\mathrm{Amb}}=\left(\theta_{\mathrm{JA}}\right)_{\text {eff }} \cdot \text { Power } \\
& =\left(35^{\circ} \mathrm{C} / \mathrm{W}\right)(3.2 \mathrm{~W}) \\
& =112^{\circ} \mathrm{C}
\end{aligned}
$$

Thus, the chip junction-temperature becomes:

$$
\begin{aligned}
T_{\text {Junction }} & =T_{\text {Amb }}+\Delta T_{\max } \\
& =25^{\circ} C+112^{\circ} C \\
& =137^{\circ} C
\end{aligned}
$$# Example Problem 4 

Using the information described in Example Problem 3, it was determined that when the chip dissipates a power of 3.2 W , the chip junction-temperature will rise to a steady-state temperature of $137^{\circ} \mathrm{C}$. Let us suppose that the chip was designed to operate reliably at a maximum junction temperature of $110^{\circ} \mathrm{C}$. In an effort to lower the chip junction-temperature from $137^{\circ} \mathrm{C}$, a heat sink is added to the chip plastic-package surface and a fan is also added to create a forced air flow condition (as illustrated below).


A heat sink is normally a metal structure which is attached to the plasticpackage surface with a thermally conductive adhesive. The metal heat sink with fins serves to increase the effective heat dissipation area of the plasticpackage surface thus reducing the effective thermal resistance $\left(\theta_{\mathrm{CA}}\right)_{\text {eff }}$ from plastic case surface to ambient. If the combination of heat sink plus increased air flow reduces the effective thermal resistance $\left(\theta_{\mathrm{CA}}\right)_{\text {eff }}$ from 10 to $1^{\circ} \mathrm{C} / \mathrm{W}$, then what impact will it have on device junction-temperature during 3.2 W operation?

## Solution

Without heat sink, the steady-state chip junction-temperature was determined to be $137^{\circ} \mathrm{C}$ with 3.2 W operation (as described in Example Problem 3). With heat sink plus increased air flow,

$$
\left(\theta_{\mathrm{CA}}\right)_{\mathrm{eff}}=10^{\circ} \mathrm{C} / \mathrm{W} \rightarrow 1^{\circ} \mathrm{C} / \mathrm{W}
$$

Therefore,

$$
\begin{aligned}
\left(\theta_{\mathrm{JA}}\right)_{\mathrm{eff}} & =\left(\theta_{\mathrm{JC}}\right)_{\mathrm{eff}}+\left(\theta_{\mathrm{CA}}\right)_{\mathrm{eff}}=(25+1)^{\circ} \mathrm{C} / \mathrm{W} \\
& =26^{\circ} \mathrm{C} / \mathrm{W}
\end{aligned}
$$The chip junction-temperature rise during 3.2 W chip operation (with heat sink plus increased air flow) becomes:

$$
\begin{aligned}
\Delta T & =T_{\text {Junction }}-T_{\mathrm{Amb}}=\left(\theta_{\mathrm{JA}}\right)_{\text {eff }} \cdot \text { Power } \\
& =\left(26^{\circ} \mathrm{C} / \mathrm{W}\right)(3.2 \mathrm{~W}) \\
& =83.2^{\circ} \mathrm{C}
\end{aligned}
$$

This leads to a chip junction-temperature of:

$$
\begin{aligned}
T_{\text {Junction }} & =T_{\mathrm{Amb}}+\Delta T \\
& =25^{\circ} \mathrm{C}+83.2^{\circ} \mathrm{C} \\
& =108.2^{\circ} \mathrm{C}
\end{aligned}
$$

Therefore, with the addition of a heat sink plus increased air flow, the device junction-temperature can be kept below the design requirement of $\leq 110^{\circ} \mathrm{C}$.

# 4 General Transient Heating and Heat Dissipation 

The general equation for transient heating, heat absorption and dissipation of the generated heat is given by Eq. (18.8) and is reproduced here ${ }^{10}$ :

$$
G(t)=\int_{V} \rho(x) c(x) \frac{\partial[T(x, t)]}{\partial t} \mathrm{~d} V+\int_{A} \vec{J}_{H}(x, t) \cdot \mathrm{d} \vec{A}
$$

This equation simply states that the heat generation rate $G(t)$ must be equal to the heat absorption rate plus the heat transfer rate. Eq. (18.16) thus permits one to determine the rate at which the temperature will rise in the volume $V$ (which contains the material in the generation region plus all the materials between the generation region and the heat sink).

[^0]
[^0]:    ${ }^{10}$ Recall that the volume $V$ of interest contains all of the materials in the generation region plus all the materials between the generation region and the heat sink/ambient. $A$ is the area of the surface that bounds the volume $V$ of interest.# 4.1 Effective Thermal Resistance Revisited 

Let us reconsider the heat-flux/transfer term on the far right of Eq. (18.16) and use an identity ${ }^{11}$ to rewrite the heat flux term as:

$$
\begin{aligned}
\int_{A} \vec{J}_{H}(x, t) \cdot \mathrm{d} \vec{A} & =A\left[\frac{\int_{0}^{A} \vec{J}_{H}(x, t) \cdot \mathrm{d} \vec{A}}{\int_{0}^{A} \mathrm{~d} A}\right] \\
& =A\left\langle J_{H}\right\rangle
\end{aligned}
$$

where $\left\langle J_{H}\right\rangle$ represents the average flux of heat across the surface of area $A$ which bounds the volume $V$ of interest. However, the average heat flux across this surface area $A$ can be expressed as:

$$
\left\langle J_{H}\right\rangle=\left\langle-\kappa \frac{\Delta T}{\Delta x}\right\rangle=\left\langle\frac{\kappa}{\Delta x}\right\rangle\left[T_{\mathrm{Gen}}(t)-T_{\mathrm{Amb}}\right]
$$

where $\Delta x$ is the thickness of the material(s) from the generation region to the ambient/heat-sink and $\kappa$ is the thermal conductivity(ies) of the material(s). The heat flux can now be written as:

$$
\begin{aligned}
\int_{A} \vec{J}_{H}(x, t) \cdot \mathrm{d} \vec{A} & =A\left\langle J_{H}\right\rangle \\
& =A\left\langle\frac{\kappa}{\Delta x}\right\rangle\left[T_{\mathrm{Gen}}(t)-T_{\mathrm{Amb}}\right] \\
& =\left(\frac{1}{\theta_{\mathrm{eff}}}\right)\left[T_{\mathrm{Gen}}(t)-T_{\mathrm{Amb}}\right]
\end{aligned}
$$

where $\theta_{\text {eff }}$ is the effective thermal resistance given by:

$$
\theta_{\mathrm{eff}}=\frac{1}{A}\left\langle\frac{\Delta x}{\kappa}\right\rangle
$$

[^0]
[^0]:    ${ }^{11}$ Identity used: $A=\int_{0}^{A} \mathrm{~d} A$.# 4.2 Heat Capacity 

Let us now reconsider the heat absorption rate term in Eq. (18.16). Assuming that the density(ies) $\rho$, specific heat(s) $c$ and coordinates $\mathrm{x}=\left(\mathrm{x}_{1}, \mathrm{x}_{2}, \mathrm{x}_{3}\right)$ are independent of time, then the limits of integration are independent of time and we can change the order in which we perform the integration and differentiation and write ${ }^{12}$ :

$$
\begin{aligned}
\int_{V} \rho(x) c(x) \frac{\partial T(x, t)}{\partial t} \mathrm{~d} V & =\int_{V} \rho(x) c(x) \frac{\partial\left[T(x, t)-T_{\text {Sink }}\right]}{\partial t} \mathrm{~d} V \\
& =\frac{\mathrm{d}}{\mathrm{~d} t} \int_{V} \rho(x) c(x)\left[T(x, t)-T_{\text {Sink }}\right] \mathrm{d} V
\end{aligned}
$$

Furthermore, if we are only interested in the temperature difference between the generation region $T_{\text {Gen }}$ and the fixed heat sink $T_{\text {Sink }}$ [plus assuming that the temperature within the generation region is uniform $T(x, t)=T_{\text {Gen }}(t)$, then we can write:

$$
\begin{aligned}
& \frac{\mathrm{d}}{\mathrm{~d} t} \int_{V} \rho(x) c(x)\left[T_{\text {Gen }}(t)-T_{\text {Sink }}\right] \mathrm{d} V \\
& =\frac{\mathrm{d}}{\mathrm{~d} t}\left[T_{\text {Gen }}(t)-T_{\text {Sink }}\right] \int_{V}[\rho(x) c(x)] \mathrm{d} V \\
& =C_{\mathrm{Th}} \frac{\mathrm{~d}}{\mathrm{~d} t}\left[T_{\text {Gen }}(t)-T_{\text {Sink }}\right]
\end{aligned}
$$

where $C_{\mathrm{Th}}$ is the thermal capacity of the materials in the volume $V$ of interest [refer to Eq. (18.4)].

## 5 Modeling Dynamical Heat Generation and Dissipation

Using Eqs. (18.19) and (18.21b), the dynamical heat generation and dissipation equation [Eq. (18.16)] becomes:

$$
G(t)=C_{\mathrm{Th}} \frac{\mathrm{~d}}{\mathrm{~d} t}\left[T_{\mathrm{Gen}}(t)-T_{\mathrm{Amb}}\right]+\frac{T_{\mathrm{Gen}}(t)-T_{\mathrm{Amb}}}{\theta_{\mathrm{eff}}}
$$

Rearranging Eq. (18.22a), one obtains the Euler differential equation:

[^0]
[^0]:    ${ }^{12}$ Since $T_{\text {sink }}$ is assumed to be a fixed temperature, then we have used: $\frac{\partial\left[T(x, t)-T_{\text {Sink }}\right]}{\partial t}=\frac{\partial\left[T(x, t)\right]}{\partial t}$.Table 18.2 Equivalent circuits

|  | Current Generation |
| :-- | :-- |
|  | $\mathrm{V}_{\text {Gen }}$ |
|  | $\mathrm{R} \stackrel{\Delta}{=} \xrightarrow{\Delta} \mathrm{C}$ |
| Conservation of Current |  |
| $I(t)=I_{1}(t)+I_{2}(t)$ |  |
| $\Rightarrow I(t)=\frac{\Delta V(t)}{R}+C \frac{d[\Delta V(t)]}{d t}$ |  |
| $\Rightarrow \frac{d[\Delta V(t)]}{d t}+\frac{1}{R C} \Delta V(t)=\frac{1}{C} I(t)$ |  |

## 

## Conservation of Energy

$G(t)=G_{1}(t)+G_{2}(t)$
$\Rightarrow G(t)=\frac{\Delta T(t)}{\theta_{\text {eff }}}+C_{T h} \frac{d[\Delta T(t)]}{d t}$
$\Rightarrow \frac{d[\Delta T(t)]}{d t}+\frac{1}{\theta_{\text {eff }} C_{T h}} \Delta T(t)=\frac{1}{C_{T h}} G(t)$

$$
\frac{\mathrm{d}}{\mathrm{~d} t}(\Delta T)+\frac{\Delta T}{\tau}=f(t)
$$

where $\Delta T=T_{\text {Gen }}(t)-T_{\text {Amb }}, f(t)$ is the time-dependent heat-generation rate function given by $f(t)=G(t) / C_{\mathrm{Th}}$, and $\tau$ is the thermal time-constant given by $\tau=$ $C_{\text {Th }} \theta_{\text {eff. }}$

In Table 18.2, we compare heat generation and dissipation with current generation and flow. When a voltage $V_{\text {Gen }}$ is generated above $V_{o}$ (at $t=0$ for circuit on the left), a parallel current flow path is created where $I_{l}(t)$ is the current flow through the resistor $R$ and $I_{2}(t)$ is the current flow to the capacitor $C$. This parallel-path conduction will continue until the capacitor is fully charged at which time all the steadystate current must now flow through the resistor.

The heat-flow circuit (on the right in Table 18.2) is analogous to the current-flow circuit on the left. The heat generation (starting at $t=0$ for the circuit on the right) will cause the temperature of the generation region $T_{\text {Gen }}$ to rise above $T_{\text {Sink }}$ and the generated heat to start flowing (in parallel). Some of the generated heat $G_{1}(t)$ flows through the effective thermal resistance $\theta_{\text {eff }}$ to the heat sink at $T_{\text {Sink }}$ and some of the generated heat $G_{2}(t)$ goes into charging the thermal capacitance $C_{\mathrm{Th}}$ (heating the surrounding materials). This heating of the surrounding materials will continue until the thermal capacitance is fully charged. At this time the steady-state thermal gradients created throughout the materials are sufficient to drive a heat flow to sink which just matches the heat generation. Note that by using current conservation (for current flow) and energy conservation (for heat flow), the same type of Euler differential equation is developed for each (as shown in Table 18.2).

As one can verify by inspection, the solution to the Euler differential equation, Eq. (18.22b), is given by:$$
\Delta T(t)=\Delta T_{0} \exp \left(-\frac{t}{\tau}\right)+\exp \left(-\frac{t}{\tau}\right) \int_{0}^{t} f(t) \exp \left(\frac{t}{\tau}\right) \mathrm{d} t
$$

where $\Delta T_{0}=T_{\text {Gen }}(t=0)-T_{\text {Amb/Sink. }}$

# 5.1 Thermal Relaxation 

Let us suppose that the input power to the generation region $V_{\text {Gen }}$ just matches the heat dissipation rate from the volume $V$ of interest. Under these thermal equilibrium conditions, the generation region $V_{\text {Gen }}$ will have a constant temperature rise of $\Delta T_{\mathrm{o}}$. Let us further suppose that the input power is suddenly stopped at some time $t=$ 0 . The thermal relaxation rate for the generation region can be determined using Eq. (18.23) by setting the generation rate term to zero $[f(t)=0]$. This gives:

$$
\Delta T(t)=\Delta T_{0} \exp \left(-\frac{t}{\tau}\right)
$$

where the thermal time-constant $\tau$ is given by $\tau=C_{\mathrm{Th}} \theta_{\text {eff. }} C_{\mathrm{Th}}$ is the thermal capacity and $\theta_{\text {eff }}$ is the effective thermal resistance. Therefore, the thermal capacity $C_{\mathrm{Th}}$ of the materials (in volume $V$ of interest which also contains the generation region) plus the effective thermal resistance $\theta_{\text {eff }}$ of these materials dictate the thermal relaxation time $\tau$. Figure 18.4 shows the thermal relaxation with time. Note that the temperature rise $\Delta T(t)$ will be $99.3 \%$ relaxed after five time-constants $(t=5 \tau) .{ }^{13}$

Fig. 18.4 Thermal relaxation for heat generation region after the input power is suddenly stopped at $t=0$. The temperature of the generation region will be $99.3 \%$ relaxed after five thermal time-constants $\tau$


[^0]
[^0]:    ${ }^{13}$ Thermal relaxation after a time $t=5 \tau$ is given by: $\frac{\Delta T_{0}-\Delta T\left(t=5 \tau\right)}{\Delta T_{0}}=1-\exp \left(\frac{5 \tau}{\tau}\right)=0.993=99.3 \%$. After $t=10 \tau$, the thermal relaxation is $99.995 \%$ complete.# Example Problem 5 

Assume that a metal plate is embedded in plastic, similar to that shown in Example Problem 2. Also, assume that the effective thermal resistance for the metal plate embedded in the plastic is $\theta_{\text {eff }}=16.7^{\circ} \mathrm{C} / \mathrm{W}$ and that the effective heat capacity of the metal plate and plastic is $C_{\mathrm{Th}}=24.2 \mathrm{~W} \mathrm{sec} /{ }^{\circ} \mathrm{C}$.
(a) For a constant input power level of 5 W to the metal plate, what is the expected steady-state temperature rise of the metal plate?
(b) What is the effective thermal time-constant for this system?
(c) If the constant input power is on long enough for all temperatures to reach steady state, but then the power is suddenly stopped at $t=0$, how long will it take the metal plate to relax to $1 / 2$ of its original steady-state temperature rise?

## Solution

(a) The steady-state temperature rise for the metal plate is given by:

$$
(\Delta T)_{\mathrm{Max}}=\theta_{\mathrm{eff}} \cdot \text { Power }=\left(16.7 \frac{\mathrm{C}}{\mathrm{~W}}\right) \cdot(5 \mathrm{~W})=83.5^{\circ} \mathrm{C}
$$

(b) The thermal time-constant $\tau$ for this metal plate and plastic is given by:

$$
\begin{aligned}
\tau=C_{\mathrm{Th}} \theta_{\mathrm{eff}} & =\left(24.2 \frac{\mathrm{Ws}}{\mathrm{C}}\right)\left(16.7 \frac{\mathrm{C}}{\mathrm{~W}}\right) \\
& =404 \mathrm{~s}
\end{aligned}
$$

(c) When input power to the metal plate is suddenly stopped, the fall in temperature of the metal plate is given by:

$$
\begin{aligned}
\Delta T(t) & =\Delta T_{\mathrm{Max}} \exp \left(-\frac{t}{\tau}\right) \\
& \Rightarrow \frac{\Delta T(t)}{\Delta T_{\mathrm{Max}}}=\frac{\Delta T_{\mathrm{Max}} / 2}{\Delta T_{\mathrm{Max}}}=\exp \left(-\frac{t_{1 / 2}}{\tau}\right) \\
& \Rightarrow t_{1 / 2}=\tau \ln (2)=(404 \mathrm{~s}) \ln (2)=280 \mathrm{~s}
\end{aligned}
$$

In summary, $t_{1 / 2}=280 \mathrm{~s}$ is the time required for the initial temperature rise $\Delta T_{\text {Max }}$ of the metal plate to relax to $50 \%$ of its original value.# Example Problem 6 

On a very cold winter day ( $T_{\text {amb/outside }}=-10^{\circ} \mathrm{C}$ ), the heating power is suddenly lost in a home. In one of the empty rooms in the house (with an exterior wall containing a glass window) the average temperature of the air in the room was observed to drop from 23 to $8^{\circ} \mathrm{C}$ in 2 h . Assuming that the empty room is 14 ft by 14 ft by 8 ft , that the room is relatively air tight, and that the specific heat of air at constant volume is $c_{V}=21.0 \mathrm{~J} / \mathrm{mol}{ }^{\circ} \mathrm{C}$, what is the effective thermal resistance of the external wall? For this problem, ignore the thermal capacity contribution from the room walls and assume that the house is located at sea level so that the air pressure can be assumed to be $1 \mathrm{~atm}=$ $1.013 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}$.

## Solution

The thermal time-constant can be determined by:

$$
\begin{aligned}
\Delta T(t) & =\Delta T_{0} \exp \left(-\frac{t}{\tau}\right) \\
& \Rightarrow \frac{23^{\circ} \mathrm{C}-8^{\circ} \mathrm{C}}{23^{\circ} \mathrm{C}-\left(-10^{\circ} \mathrm{C}\right)}=\exp \left(-\frac{2 \mathrm{~h}}{\tau}\right) \\
& \Rightarrow \tau=-\frac{2 \mathrm{~h}}{\ln (15 / 33)}=2.54 \mathrm{~h}
\end{aligned}
$$

The constant volume V of air in the room is given by:

$$
V=(14 \cdot 14 \cdot 8) \mathrm{ft}^{3}\left(\frac{1 \mathrm{~m}}{3.281 \mathrm{ft}}\right)^{3}=44.4 \mathrm{~m}^{3}
$$

The heat capacity $C_{\mathrm{Th}}$ of the constant volume $V$ of air can be written as:

$$
C_{\mathrm{Th}}=\mathrm{nc}_{V}
$$

where $n$ is the number of moles of air molecules and $c_{V}$ is the specific heat per mole at constant volume. $n$ can be determined using the ideal gas law approximation:

$$
n=\frac{\mathrm{PV}}{\mathrm{RT}}=\frac{\left(1.013 \times 10^{5} \frac{\mathrm{~N}}{\mathrm{~m}^{2}}\right)\left(44.4 \mathrm{~m}^{3}\right)}{\left(8.31 \frac{\mathrm{~J}}{\mathrm{~mol} \times \mathrm{K}}\right)(23+273) \mathrm{K}}=1.83 \times 10^{3} \mathrm{~mol}
$$

The heat capacity $C_{\mathrm{Th}}$ of the constant volume $V$ air in the room is:$$
C_{\mathrm{Th}}=\mathrm{nc}_{V}=\left(1.83 \times 10^{3} \mathrm{mo} 1\right)\left(21.0 \frac{\mathrm{~J}}{\mathrm{~mol}^{1} \mathrm{C}}\right)=3.84 \times 10^{4} \frac{\mathrm{~J}}{\mathrm{C}}
$$

The effective thermal resistance $\theta_{\text {eff }}$ can be determined from the thermal time-constant $\tau$ and it is given by:

$$
\begin{aligned}
\tau & =C_{\mathrm{Th}} \theta_{\mathrm{eff}} \\
& \Rightarrow \theta_{\mathrm{eff}}=\frac{\tau}{C_{\mathrm{Th}}}=\frac{(2.54 \mathrm{~h})\left(\frac{3600 \mathrm{~S}}{1 \mathrm{~h}}\right)}{3.84 \times 10^{4} \frac{\mathrm{~J}}{\mathrm{C}}}=0.24 \frac{\mathrm{C}}{\mathrm{~W}}
\end{aligned}
$$

For the room described in this example problem, please note that if we added furniture, a granite-top table, and a large aquarium (filled with water) to the room-this will add heat capacity to the room and this will increase the thermal time-constant for the room. Thus, the room will cool off much more slowly when the heating power is lost to the room. This is why "passive solar homes" make extensive use of materials with large heat capacities in the rooms. Thus, when the sun goes down on a cold winter evening (the solar heating power is lost to home), the temperature inside the house drops relatively slowly during the night.

# 5.2 Thermal Rise with Constant Input Power 

Let us now consider the situation where the generation region is at the same temperature as the ambient $\left(\Delta T_{0}=0\right)$ and we introduce power into the generation region at $t=0$ and the input power remains constant, $G(t)=G_{0}=$ constant. Under these conditions, Eq. (18.23) reduces to:

$$
\begin{aligned}
\Delta T(t) & =\exp \left(-\frac{t}{\tau}\right) \int_{0}^{t} \frac{G_{0}}{C_{\mathrm{Th}}} \exp \left(\frac{t}{\tau}\right) \mathrm{d} t \\
& =\frac{G_{0}}{C_{\mathrm{Th}}} \exp \left(-\frac{t}{\tau}\right)\left[\tau \exp \left(\frac{t}{\tau}\right)\right]_{0}^{t} \\
& =\frac{\tau G_{0}}{C_{\mathrm{Th}}}\left[1-\exp \left(-\frac{t}{\tau}\right)\right] \\
& =\theta_{\mathrm{eff}} G_{0}\left[1-\exp \left(-\frac{t}{\tau}\right)\right] \\
& =(\Delta T)_{\max }\left[1-\exp \left(-\frac{t}{\tau}\right)\right]
\end{aligned}
$$

Fig. 18.5 Temperature rise $\Delta T$ for generation region versus time with constant power input $G_{0}$. The maximum temperature rise is $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$. The temperature rise tends to saturate ( $99.3 \%$ ) for 5 time-constants $(t=5 \tau)$. The insert shows a constant input power level $G_{0}$ versus time

One will note that $(\Delta T)_{\max }=\theta_{\text {eff }} G_{0}$ is the maximum temperature rise when the generation region comes into thermal equilibrium for a constant input power.

Let us assume that the temperature of the generation region is equal to $T_{\text {Sink }}$ at time zero when the constant power $G_{o}$ is applied. We will further assume that the volume $V$ of interest contains materials with a heat capacity of $C_{\mathrm{Th}}$ and that they have an effective thermal resistance of $\theta_{\text {eff }}$. In Fig. 18.5 we show the temperature rise $\Delta T(t)$ of the generation region when a constant power input is suddenly given to the generation region. We can see that the temperature rise tends to saturate for times $t>5 \tau$, where $\tau=C_{\mathrm{Th}} \theta_{\text {eff }}$ and the saturation temperature level is given by $\Delta T \max =\theta_{\text {eff }} G_{0}$.

# 5.3 Thermal Rise and Relaxation with Single Power Pulse 

Let us consider the case of a simple rectangular shaped power pulse as illustrated in the insert of Fig. 18.6. ${ }^{14}$ We will assume that the temperature of the generation region is equal to $T_{\text {Sink }}$ at time zero. If the power is assumed to be on for at least ten thermal time-constants $\tau$ and then off for another ten thermal time-constants, then the temperature (rise and fall) is shown in Fig. 18.6.

Under the conditions of a single power pulse, which is on for at least 10 thermal time-constants $\tau$, the temperature rise $\Delta T(t)$ will tend to saturate ( $99.995 \%$ ) at a

[^0]
[^0]:    ${ }^{14}$ The actual power pulse could be more complicated than a simple rectangular shape; however, in Chap. 14 we learned how to convert complicated waveforms into rectangular equivalents.

Fig. 18.6 Temperature rise and fall for heat generation volume versus input power time. Input power $G(t)$ is shown in insert with the duration of input power equal to ten thermal time-constants $(t=10 \tau)$. The maximum temperature rise is $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$. The temperature rise and relaxation times tend to saturate ( $>99.3 \%$ ) for times $(t>5 \tau)$. The insert indicates input power level versus time
maximum of $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$. Also, nearly full thermal relaxation occurs within another 10 thermal time-constants. The thermal time-constant is given by $\tau=$ $C_{\mathrm{Th}} \theta_{\text {eff }}$.

# 5.4 Thermal Rises and Relaxations with Periodic Power Pulses 

Let us now consider what would happen if we have periodic power generation in the volume as illustrated in Fig. 18.7.

During each period, there will be a temperature-rise portion of the period due to the input power being on and a temperature-fall portion of the period due to the input power being off. For example, during the first period, we have a temperature rise and fall portion of the period given by:

$$
\Delta T_{\text {rise }}\left[0 \leq t \leq t_{\text {on }}\right]=\Delta T[t=0]+\theta_{\text {eff }} G_{0}\left[1-\exp \left(-\frac{t}{\tau}\right)\right]
$$

and

$$
\Delta T_{\text {fall }}\left[t_{\text {on }} \leq t \leq t_{p}\right]=\Delta T\left[t=t_{\text {on }}\right] \cdot \exp \left(-\frac{t-t_{\text {on }}}{\tau}\right)
$$Fig. 18.7 Periodic power generation $G(t)$. Duty cycle is defined as the fraction of time that the power pulse is on: $t_{\text {on }} / t_{p}$


The thermal rise and fall for each period can be generalized easily. The temperature rise and fall during the $N$ th period is given by:

$$
\begin{gathered}
\Delta T_{\text {rise }}\left[(N-1) t_{p} \leq t \leq(N-1) t_{p}+t_{\text {on }}\right]=\Delta T\left[t=(N-1) t_{p}\right] \\
+\theta_{\text {eff }} G_{0}\left[1-\exp \left(-\frac{t-(N-1) t_{p}}{\tau}\right)\right]
\end{gathered}
$$

and

$$
\begin{gathered}
\Delta T_{\text {fall }}\left[(N-1) t_{p}+t_{\text {on }} \leq t \leq N t_{p}\right]=\Delta T\left[t=(N-1) t_{p}+t_{\text {on }}\right] \\
\cdot \exp \left(-\frac{t-(N-1) t_{p}-t_{\text {on }}}{\tau}\right)
\end{gathered}
$$

In Fig. 18.8 we show the temperature rises and falls for the first five power pulses [with $50 \%$ duty cycle pulses $\left(t_{\text {on }}=t_{\text {off }}\right)$ ]. In Fig. 18.8a we see that when $t_{\text {on }} \gg \tau$, then $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$ is reached during the on-portion of each pulse; $\Delta T_{\max }$ will relax fully during the off-portion of the period. In Fig. 18.8b, we see that when $t_{\text {on }} \approx \tau$, then $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$ is not reached during the on-portion of the first pulse and neither does full thermal relaxation occur during the off-portion of the first pulse. However, with each successive pulse, the temperature rise increases incrementally finally reaching a value of $\Delta T_{\max }=\theta_{\text {eff }} G_{0}$ when the number of pulses is much greater than 5. In Fig. 18.8c, we see that when $t_{\text {on }} \ll \tau$, then the thermal time-constant $\tau$ for the system prevents a rapid rise of the temperature during each pulse. ${ }^{15}$

[^0]
[^0]:    ${ }^{15}$ Systems with large thermal time-constants are often referred to as systems with large thermal inertia. Such systems, with large thermal inertia, have great difficulty responding quickly to shortduration power pulses. This can be good or bad depending on the details of device application.
b

c


Fig. 18.8 Thermal rises and falls for power pulsing with $50 \%$ duty cycle $\left(t_{\text {out }} / t_{p}=0.5\right)$. First five pulses are shown. (a) Periodic power pulses with $t_{P}=10 \tau$ where $\tau$ is the thermal time-constant. (b) Periodic power pulses with $t_{P}=\tau$. (c) Periodic power pulses with $t_{P}=0.1 \tau$# Example Problem 7 

Using the information found in Example Problem 6, assume that when the room air temperature reaches $8^{\circ} \mathrm{C}$, an electric heater (power $=\mathrm{G} 0=0.5 \mathrm{~kW}$ ) is brought into the room and turned on. How long will it take for the temperature of the air in the room to recover from $8^{\circ} \mathrm{C}$ to the normal level of $23^{\circ} \mathrm{C}$ ?

## Solution

From Example Problem 5 we have:

$$
\theta_{\mathrm{eff}}=0.24^{\circ} \mathrm{C} / \mathrm{W} \text { and } \tau=2.54 \mathrm{~h}
$$

As soon as the electric heater is switched on $\left(G_{0}=0.5 \mathrm{~kW}\right)$, the average temperature of the air in the room will start to climb as given by:

$$
\begin{aligned}
\Delta T_{\text {rise }} & =\Delta T[t=0]+\theta_{\mathrm{eff}} G_{0}\left[1-\exp \left(-\frac{t}{\tau}\right)\right] \\
& \Rightarrow t=-\tau \ln \left[1-\left(\frac{\Delta T_{\text {rise }}-\Delta T_{0}}{\theta_{\mathrm{eff}} G}\right)\right] \\
& =-2.54 \mathrm{~h} \ln \left[1-\left(\frac{15^{\circ} \mathrm{C}}{\left(0.24^{\circ} \mathrm{C} / \mathrm{W}\right)\left(0.5 \times 10^{3} \mathrm{~W}\right)}\right)\right] \\
& =0.34 \mathrm{~h}=20.4 \mathrm{~min}
\end{aligned}
$$

Therefore, it will take approximately 20 min (after the 0.5 KW electric heater is switched on) before the average temperature of the room increases from 8 to $23^{\circ} \mathrm{C}$.

## Example Problem 8

A silicon power ( 50 W ) transistor is used in a certain device application. Assuming that the effective thermal resistance for the power transistor is $\theta_{\text {eff }}$ $=10^{\circ} \mathrm{C} / \mathrm{W}$ and that the thermal time-constant is $\tau=100 \mu \mathrm{~s}$, determine the temperature rise for the power transistor when it delivers a power of 50 W for:
(a) $1 \mu \mathrm{~s}$,
(b) $10 \mu \mathrm{~s}$,
(c) $100 \mu \mathrm{~s}$,
(d) $1,000 \mu \mathrm{~s}$.

## Solution

The temperature rise for the power transistor is given by:$$
\begin{aligned}
\Delta T_{\text {nse }} & =\Delta T[t=0]+\theta_{\text {eff }} G_{0}\left[1-\exp \left(-\frac{t}{r}\right)\right] \\
& =0+\left(10^{\circ} \mathrm{C} / \mathrm{W}\right)(50 \mathrm{~W})\left[1-\exp \left(-\frac{t}{100 \mu \mathrm{~s}}\right)\right] \\
& =500^{\circ} \mathrm{C}\left[1-\exp \left(-\frac{t}{100 \mu \mathrm{~s}}\right)\right]
\end{aligned}
$$

(a)

$$
\Delta T_{\text {rise }}=500^{\circ} \mathrm{C}\left[1-\exp \left(-\frac{1 \mu \mathrm{~s}}{100 \mu \mathrm{~s}}\right)\right]=5^{\circ} \mathrm{C}
$$

(b)

$$
\Delta T_{\text {rise }}=500^{\circ} \mathrm{C}\left[1-\exp \left(-\frac{10 \mu \mathrm{~s}}{100 \mu \mathrm{~s}}\right)\right]=48^{\circ} \mathrm{C}
$$

(c)

$$
\Delta T_{\text {rise }}=500^{\circ} \mathrm{C}\left[1-\exp \left(-\frac{100 \mu \mathrm{~s}}{100 \mu \mathrm{~s}}\right)\right]=316^{\circ} \mathrm{C}
$$

(d)

$$
\Delta T_{\text {nse }}=500^{\circ} \mathrm{C}\left(1-\exp \left(-\frac{1,000 \mu \mathrm{~s}}{100 \mu \mathrm{~s}}\right)\right)=499.98^{\circ} \mathrm{C}
$$

# 6 Convection Heat Transfer 

Thus far in this chapter, the primary heat transfer mechanism discussed has been conduction (solid to solid) heat transfer. The importance of convection (solid to fluid) heat transfer was alluded to in Example Problem 4 when we noted that the thermal resistance (from package surface to the ambient air) could be reduced by air flow. Now we would like to make the convection heat transfer process a little more quantitative.

Shown in Fig. 18.9 is an example of convection heat transfer process using forced fluid (air or liquid) flow over the surface of the device. As the molecules in the fluid come in contact with the surface of the device, heat transfer will occur. If the molecules in the fluid leave the surface of the device with a higher mean speed, then energy is being transferred from the surface of the device to the fluid. In thermal equilibrium, the constant heat generation rate $G_{0}$ must be equal to the heat loss rate from the device's surface.

Fig. 18.9 Convection heat transfer is enhanced by forced fluid (air or liquid) flow. The fluid, as it flows over the surface of the hot device, will absorb heat (assuming that $T_{\text {Surface }}[\mathrm{T}$ ). Since the local temperature of the fluid close to the surface of the hot device will rise, $T$, represents the steady-state temperature of the fluid some relatively large distance away from the surface of the hot device

Let us represent the heat transfer rate at a unit area of the surface using a transfer coefficient $h$. In terms of the heat transfer coefficient $h$, we will write an integral form of Newton's law for cooling rate ${ }^{16}$ :

$$
\begin{aligned}
G_{0} & =\int \vec{J}_{H}(x) \cdot \mathrm{d} \vec{A}_{\text {Surface }}=\int h(x)\left[T(x)_{\text {Surface }}-T_{\infty}\right] \mathrm{d} A_{\text {Surface }} \\
& =A_{\text {Surface }} \frac{\int h(x)\left[T(x)_{\text {Surface }}-T_{\infty}\right] \mathrm{d} A_{\text {Surface }}}{\int \mathrm{d} A_{\text {Surface }}} \\
& =A_{\text {Surface }}\left\langle h(x)\left[T(x)_{\text {Surface }}-T_{\infty}\right\rangle\right.
\end{aligned}
$$

If the temperature of the device's surface is approximately uniform/constant, then Eq. (18.28) reduces to:

$$
\begin{aligned}
G_{0} & =A_{\text {Surface }}\left\langle h(x)\left[T(x)_{\text {Surface }}-T_{\infty}\right]\right\rangle \\
& =A_{\text {Surface }}\langle h(x)\rangle\left[T_{\text {Surface }}-T_{\infty}\right] \\
& =A_{\text {Surface }} h_{\text {eff }}\left[T_{\text {Surface }}-T_{\infty}\right] \\
& =\frac{1}{\theta_{\text {eff }}}\left[T_{\text {Surface }}-T_{\infty}\right]
\end{aligned}
$$

Therefore, we see from Eq. (18.29) that the effective thermal resistance from
device surface to fluid can be written as:

[^0]
[^0]:    ${ }^{16}$ Newton's law for cooling states that the rate of heat loss from a body is proportional to the temperature difference between the body and its surroundings:
    $\frac{\mathrm{d}\left(\text { Heat }_{\text {Loc. } \text { Iron Body }}\right)}{\mathrm{d} t} \propto\left[T_{\text {Body }}-T_{\text {Ambient }}\right]$. However, for convection cooling in general, deviations from this simple linear dependence can be observed.$$
\left(\theta_{\mathrm{eff}}\right)_{\text {Surface-to-Fluid }}=\frac{1}{\left(h_{\mathrm{eff}}\right)_{\text {Surface-to-Fluid }} \cdot A_{\text {Surface }}}
$$

# Example Problem 9 

A metal plate of surface area $10 \mathrm{~cm}^{2}$ is being heated by resistive or inductive methods. It is dissipating a constant 40 W of power to the ambient air.
(a) If the steady-state surface temperature rise of the metal plate is $250^{\circ} \mathrm{C}$, what is the average/effective heat transfer coefficient for metal surface to the ambient air?
(b) Assuming that a forced air flow increases the heat transfer coefficient by a factor of 5 , what would be the new steady-state metal surface temperature rise?

## Solution

(a) Equation (18.29) gives:

$$
\begin{aligned}
G_{0} & =A_{\text {Surface }} \langle h(x)\rangle\left[T_{\text {Surface }}-T_{\infty}\right] \\
& =A_{\text {Surface }} h_{\text {eff }}\left[T_{\text {Surface }}-T_{\infty}\right] \\
& =40 \mathrm{~W}
\end{aligned}
$$

Therefore:

$$
\begin{aligned}
h_{\mathrm{eff}}=\langle h\rangle & =\frac{40 \mathrm{~W}}{A_{\text {Surface }}\left[T_{\text {Surface }}-T_{\infty}\right]} \\
& =\frac{40 \mathrm{~W}}{100 \mathrm{~cm}^{2}\left[250^{\circ} \mathrm{C}\right]}=0.0016 \frac{\mathrm{~W}}{\mathrm{C} \mathrm{~cm}^{2}}
\end{aligned}
$$

(b) With forced air flow the new heat transfer coefficient $\left(h_{\text {eff }}\right)_{\text {new }}$ increases by a factor of 5 . This will reduce the metal plate temperature rise to:

$$
\begin{aligned}
{\left[T_{\text {Surface }}-T_{\infty}\right] } & =\frac{40 \mathrm{~W}}{A_{\text {Surface }} \cdot\left(h_{\text {eff }}\right)_{\text {New }}} \\
& =\frac{40 \mathrm{~W}}{100 \mathrm{~cm}^{2}\left[5 \cdot(0.0016) \frac{\mathrm{W}}{\mathrm{C}-\mathrm{cm}^{2}}\right]} \\
& =50^{\circ} \mathrm{C}
\end{aligned}
$$Table 18.3 Material surface emissivity

| Material | Emissivity: $e_{\text {mis }}$ |
| :-- | :-- |
| Polished metals | $0.01-0.10$ |
| Oxidized metals | $0.10-0.20$ |
| Heavily oxidized metals | $0.20-0.50$ |
| Water | $0.60-0.70$ |
| Silica | $0.80-0.90$ |
| Paint: flat black | $0.85-0.90$ |
| Dark red brick | $0.90-0.95$ |
| Coal | $0.95-0.99$ |

# 7 Radiation Heat Transfer 

Heat transfer can be achieved through conduction (solid to solid heat transfer as illustrated in Example Problems 2 and 3) or by convection (solid to fluid heat transfer as illustrated in Example Problems 4 and 9). There is, however, another method of heat transfer that should be discussed-radiation (solid to ambient heat transfer via electromagnetic radiation).

A body at temperature $T$ will emit electromagnetic radiation, and the power $P$ of the emission (energy radiated per unit time) is given by the Stefan-Boltzmann Law:

$$
P_{\text {radiation }}=e_{\text {mis }} \sigma_{\text {Stef }} \mathrm{AT}^{4}
$$

where $e_{\text {mis }}$ is the emissivity for the surface of area $A$ which bounds the volume of material at temperature $T$ (in Kelvin). $\sigma_{\text {Step }}$ is Stefan's constant and has a value of $5.67 \times 10^{-8} \mathrm{~W} /\left(\mathrm{m}^{2} \mathrm{~K}^{4}\right)$. We will show in Example Problem 10 that (except for very high temperatures) the radiation heat losses are often small compared to conduction/ convection heat transfer. The emissivity of several material surfaces is given in Table 18.3.

## Example Problem 10

Reconsider Example Problem 2-except this time, consider both the conductive heat transfer and the radiation heat transfer from the metal plate. Assume that the metal plate is initially at $25^{\circ} \mathrm{C}$ before input power is applied to the metal plate.

## Solution

In Example Problem 2, the steady-state conduction power from the metal plate was given by:

$$
P_{\text {conduction }}=\frac{\Delta T}{\theta}=\left(\frac{\kappa A_{0}}{S_{o}}\right) \Delta T
$$

Thus, the conduction power per unit area becomes:$$
\begin{aligned}
\frac{P_{\text {conduction }}}{A_{0}}=\left(\frac{\kappa}{S_{o}}\right) \Delta T & =\left(\frac{12 \frac{\mathrm{~mW}}{\mathrm{C}-\mathrm{cm}}}{1 \mathrm{~cm}}\right)(167-25)^{\circ} \mathrm{C} \\
& =1.7 \frac{\mathrm{~W}}{\mathrm{~cm}^{2}}
\end{aligned}
$$

Assume that the total surface area $A$ of this thin plate is $A \approx 2 A_{o}$ and that its emissivity is $e_{\text {mis }}=0.1$, then Eq. (18.31) gives:

$$
\begin{aligned}
\frac{P_{\text {radiation }}}{A_{o}} & =2 e_{\text {mis }} \sigma_{\text {Stef }} T^{4} \\
& =2(0.1)\left(5.67 \times 10^{-8} \frac{\mathrm{~W}}{\mathrm{~m}^{2} \mathrm{~K}^{4}}\right)\left(\frac{1 \mathrm{~m}}{100 \mathrm{~cm}}\right)^{2}[(25+167+273) \mathrm{K}]^{4} \\
& =0.053 \frac{\mathrm{~W}}{\mathrm{~cm}^{2}}
\end{aligned}
$$

Note that the radiation heat transfer (per unit area) from the metal plate is small compared to the conduction heat transfer (per unit area) from the metal plate for this problem. Note also that the effective thermal resistance $\theta_{\text {eff }}$ (described in Sect. 18.3) was experimentally determined by measuring the temperature rise for a fixed power dissipation-therefore $\theta_{\text {eff }}$ (since it is a measured quantity) comprehends the impact of all three heat transfer mechanisms: conduction, convection, and radiation.

# 8 Entropy Changes Associated with Heat Transfer 

Before leaving this chapter we must, at the very least, mention entropy changes associated with heat transfer. Even though we have not used entropy changes explicitly, they are implicit in everything that we have done. Recall from Chap. 3 the stated Second Law of Thermodynamics: entropy (disorder) of isolated systems will tend to increase with time-thus entropy tends to act like a clock which distinguishes past, present and future. The change in entropy $\Delta S$ of a system is given by:

$$
\Delta S=\int_{T_{1}}^{T_{2}} \frac{\delta(\text { Heat })}{T}
$$

where the temperature $T$ must be expressed in Kelvin. $\delta$ (Heat) is not an exact differential which means that before one can integrate-details must be given concerning the heat transfer process.In Example Problem 1, when we brought the blocks of aluminum and copper into thermal contact at time $t=0$, the block of copper immediately/spontaneously started to transfer heat from the hotter copper block to the cooler aluminum block. What was the driving force for this heat flow/transfer to occur? The First Law of Thermodynamics (conservation of energy) cannot be the driving force for the energy transfer because the total energy of the system remains constant throughout the transfer of energy from the copper block to the aluminum block. We said that the transfer of energy/heat was due to Fourier's Law (heat flow due to a thermal gradient) which is correct, but Fourier's Law seems to be only a consequence of something more fundamental-an alternative statement of the Second Law of Thermodynamics: spontaneous changes will occur within an isolated system with time in a direction that tends to increase/maximize entropy. The Second Law can be considered the driving force that caused the heat to spontaneously start flowing from the hot block of copper to the cooler block of aluminum when the two materials were brought into thermal contact. In Example Problem 11 we will show that the entropy of the system increases when heat flows from the hotter Cu block to the cooler Al block; and, this is the ultimate driving force for spontaneous heat flow. The maximum entropy increase for this system (final state of system) will occur when the temperature of the two blocks of metal reach the same equilibrium temperature.

# Example Problem 11 

Determine the change in entropy, for the process described in Example Problem 1, where the block of aluminum (initially at $25^{\circ} \mathrm{C}$ ) and the block of copper (initially at $500^{\circ} \mathrm{C}$ ) were brought together and reached their final state of thermal equilibrium at $168.6^{\circ} \mathrm{C}$.

## Solution

The change in the entropy for the block of aluminum (from initial state to final equilibrium state) is given by:

$$
\Delta S_{\mathrm{Al}}=\int_{298 \mathrm{~K}}^{\mathrm{Teq}} \frac{c_{\mathrm{Al}} M_{\mathrm{Al}} \mathrm{~d} T}{T}=c_{\mathrm{Al}} M_{\mathrm{Al}} \ln \left(\frac{T_{\mathrm{eq}}}{298 \mathrm{~K}}\right)
$$

and for the block of copper,

$$
\Delta S_{\mathrm{Cu}}=\int_{773 \mathrm{~K}}^{\mathrm{Teq}} \frac{c_{\mathrm{Cu}} M_{\mathrm{Cu}} \mathrm{~d} T}{T}=c_{\mathrm{Cu}} M_{\mathrm{Cu}} \ln \left(\frac{T_{\mathrm{eq}}}{773 \mathrm{~K}}\right)
$$Since the equilibrium temperature was determined in Example Problem 1 to be $T_{\text {eq }}=168.6^{\circ} \mathrm{C}=441.6 \mathrm{~K}$, then the entropy change for the aluminum block is:

$$
\begin{aligned}
\Delta S_{\mathrm{Al}} & =c_{\mathrm{Al}} M_{\mathrm{Al}} \ln \left(\frac{T_{\mathrm{eq}}}{298 \mathrm{~K}}\right) \\
& =\left[0.9 \times 10^{3} \mathrm{~J} /(\mathrm{kgK})\right][1 \mathrm{~kg}] \ln \left(\frac{441.6 \mathrm{~K}}{298 \mathrm{~K}}\right) \\
& =354 \mathrm{~J} / \mathrm{K}
\end{aligned}
$$

The entropy change for the copper block is:

$$
\begin{aligned}
\Delta S_{\mathrm{Cu}} & =c_{\mathrm{Cu}} M_{\mathrm{Cu}} \ln \left(\frac{441.6 \mathrm{~K}}{298 \mathrm{~K}}\right) \\
& =\left[0.39 \times 10^{3} \mathrm{~J} /(\mathrm{kgK})\right][1 \mathrm{~kg}] \ln \left(\frac{441.6 \mathrm{~K}}{773 \mathrm{~K}}\right) \\
& =-219 \mathrm{~J} / \mathrm{K}
\end{aligned}
$$

The net entropy change for the system is given by:

$$
\begin{aligned}
\Delta S & =\Delta S_{\mathrm{Al}}+\Delta S_{\mathrm{Cu}} \\
& =+354 \mathrm{~J} / \mathrm{K}+(-219 \mathrm{~J} / \mathrm{K}) \\
& =+135 \mathrm{~J} / \mathrm{K}
\end{aligned}
$$

Therefore, we conclude that the driving force for spontaneous heat flow (from the hot copper block to the cooler aluminum block) was due to the increase in entropy $(+135 \mathrm{~J} / \mathrm{K})$ for the system.

We should note that the Second Law prohibits heat from spontaneously flowing from a cooler block of aluminum to the hotter block of Cu (see Problem 9 at the end of this chapter) because this would represent a decrease in entropy for the system. The Second Law prevents spontaneous changes which would lead to a decrease in entropy of the universe. Since entropy (disorder) of the universe must always increase-then how can we explain the creation of highly-ordered/highly-structured devices? How can these devices be built without violating the Second Law?

We know that with the addition of work, local order can be easily achieved. With work, impressive highly-ordered structures/devices can be created: cars, buildings, cities, ICs, computers, etc. Creation of local order is possible (reduction in local entropy) as long as the net entropy of the universe increases. For example, a common way of bringing about an increase in local order (decrease in local entropy) is simply to build a device/structure. This building effort, however, requires work. In theprocess of doing work, food must be consumed and burned by our bodies. If we use machines to build the devices/structures, then fuels must be consumed and burned by the machines. Since the energy content in food/fuel is normally highly concentrated, food and fuel represent states with relatively low entropy. However, as the food/fuel is burned, an enormous increase in entropy (increase in chaos) occurs. Thus, a local decrease in entropy is possible (evidenced by the building of highly-ordered devices/ structures). This is permitted by the Second Law as long as there is a net increase in entropy somewhere else in the universe. Also, as we recall from Chap. 8, once these highly-ordered devices/ structures are built, they are generally metastable and will start to degrade with time-also because of the Second Law.

In summary, building highly-ordered/highly-structured devices represents a decrease in local entropy. Such highly-ordered structures can be accomplished with work and/or with heat transfer. However, the entropy of the universe must increase somewhere else when we create such devices. As we discussed in Chap. 8, these newly created highly-ordered/highly-structured devices tend to be metastable and will generally degrade with time-also as a consequence of the Second Law.

# Problems 

1. For the horizontal heat flow configuration shown, where $k_{i}$ is the thermal conductivity and $S_{\mathrm{i}}$ is the thickness for each material with cross-sectional area $A$,

show that the thermal resistance $h$ for the three materials is given by:

$$
\theta=\frac{1}{A} \sum_{i=1}^{3} \frac{S_{i}}{k_{i}}
$$

2. For the horizontal heat flow configuration shown, where $k_{i}$ is the thermal conductivity and $A_{i}$ is the cross-sectional area for each material with thickness $S$,
show that the thermal resistance $\theta$ for the three materials is given by:

$$
\theta=\frac{S}{\sum_{i=1}^{3} k_{i} A_{i}}
$$

3. For the embedded metal plate shown, 10 W of power is being generated in the metal plate and dissipated in equilibrium through the thermal resistances shown with values: $\theta_{1}=\theta_{2}=5^{\circ} \mathrm{C} / \mathrm{W}$ and $\theta_{3}=\theta_{4}=\theta_{5}=\theta_{6}=40^{\circ} \mathrm{C} / \mathrm{W}$.
(a) What is the total effective thermal resistance for all of these thermal resistors in parallel?
(b) In steady state, what is the temperature rise for the metal plate above the ambient temperature?
(c) Of the total power ( 10 W ) being dissipated by the metal plate, how much of the power dissipation is going out the top and bottom of the metal plate? How much of the power dissipation is going out the sides of the metal plate?


Answers: (a) $2.0^{\circ} \mathrm{C} / \mathrm{W}$ (b) $20^{\circ} \mathrm{C}$ (c) Top plus Bottom: 8.0 W , Sides: 2.0 W
4. The thermal resistance (from silicon-chip junction to ambient air) for an IC package is $\theta_{\mathrm{JA}}=33^{\circ} \mathrm{C} / \mathrm{W}$ in still air. In moving air (air flow of $1 \mathrm{~m} / \mathrm{s}$ ) the thermal resistance reduces to $27^{\circ} \mathrm{C} / \mathrm{W}$. Suppose that a silicon chip is placed in this IC package and that the chip dissipates a constant power of 2 W .(a) Calculate the equilibrium chip junction-temperature when the packaged chip is placed in still air at $25^{\circ} \mathrm{C}$.
(b) Calculate the equilibrium chip junction-temperature when the packaged chip is placed in moving air $(1 \mathrm{~m} / \mathrm{s})$ at $25^{\circ} \mathrm{C}$.

Answers: (a) $91^{\circ} \mathrm{C}$ (b) $79^{\circ} \mathrm{C}$
5. On a very cold winter day (outside air temperature of $-10^{\circ} \mathrm{C}$ ), a constant input power of 1 kW is required from an electric heater to keep the room temperature at $23^{\circ} \mathrm{C}$. Assuming that the exterior wall has a large plate glass window such that most of the heat in the room is lost through this exterior wall: (a) what is the effective thermal resistance of the exterior wall; and, (b) if the cost of the electric power is $\$ 0.1 /(\mathrm{kW} \mathrm{h})$, what is the cost to heat such a room for 1 month ( 30 days) under this extreme condition?

Answers: (a) $0.033^{\circ} \mathrm{C} / \mathrm{W}$ (b) $\$ 72$
6. For the silicon chip described in Problem 5 (in still air), what is the effective heat capacity of the chip and package if the chip comes into thermal equilibrium approximately 60 s after a constant power is applied? (Assume that thermal equilibrium occurs after approximately 5 thermal time-constants.)

Answer: $0.36(\mathrm{~W} \mathrm{~s}) /{ }^{\circ} \mathrm{C}$
7. If the electric power is suddenly lost to the room described in Problem 5, how long would it take for the room temperature to drop from 23 to $0^{\circ} \mathrm{C}$ ? Assume that the room $(8 \mathrm{~m} \times 8 \mathrm{~m} \times 3 \mathrm{~m})$ is relatively air tight with a heat capacity of $3.84 \times 10^{4}(\mathrm{~W} \mathrm{~s}) /{ }^{\circ} \mathrm{C}$ and that the room is located at sea level.

Answer: $t=0.42 \mathrm{~h}$
8. Quench hardening is a metallurgical process whereby a piece of metal is raised to a high temperature and then suddenly quenched-rapidly lowering the temperature of the piece of metal. Suppose that a 10 kg piece of steel at $900^{\circ} \mathrm{C}$ is suddenly dropped in a thermally insulated vat with 100 kg of water at $25^{\circ} \mathrm{C}$. What will be the equilibrium temperature of the steel and water? Assume that the specific heat for the steel is $0.49 \mathrm{~kJ} /\left({ }^{\circ} \mathrm{C} \mathrm{kg}\right)$ and for the water is $4.19 \mathrm{~kJ} /\left({ }^{\circ} \mathrm{C} \mathrm{kg}\right)$.

Answer: $35^{\circ} \mathrm{C}$
9. Using the First and Second Laws of Thermodynamics, show that heat cannot spontaneously flow from a cooler object to a hotter object. [Hint bring together two identical blocks (but at different temperatures) and calculate the entropy change that would occur if heat flows from the cooler to the hotter block. Is the entropy change positive or negative?]
10. Show that when you bring together two identical blocks, except one has an initial temperature of $T_{1}$ and the other has an initial temperature of $T_{2}$, the finalequilibrium temperature will be $T_{\text {equilibrium }}=\left(T_{1}+T_{2}\right) / 2$. [Hint show that this equilibrium temperature produces the maximum entropy change for the system.]
11. The solar constant $S=1.4 \mathrm{~kW} / \mathrm{m}^{2}$ represents the average specific power density delivered to the earth ${ }^{17}$ by the sun. Assuming that the distance from the earth to the sun is $1.5 \times 10^{11} \mathrm{~m}$, the radius of the sun is $6.96 \times 10^{8} \mathrm{~m}$, and the emissivity of the sun is $\mathrm{e}_{\text {mis }}=1$, use the Stefan-Boltzmann equation to calculate the average temperature of the sun.

Answer: $\mathrm{T}_{\text {Sun }}=5,820 \mathrm{~K}$ (or approximately $6,000 \mathrm{~K}$ )

# Bibliography 

Arpacz, V., Conduction Heat Transfer, Addison-Wesley Publishing, 1966.
Carslaw, H. and J. Jaeger, Conduction of Heat in Solids, 2nd Ed., Oxford Press, 1959.
Kittel, C. and H. Kroemer, Thermal Physics, 2nd Ed., W.H. Freeman and Co., 1980.
Sears, F and G. Salinger, Thermodynamics, Kinetic Theory, and Statistical Thermodynamics, 3rd Ed., 1975.
Thomas, L., Fundamentals of Heat Transfer, Prentice-Hall Inc., 1980.

[^0]
[^0]:    ${ }^{17}$ Note that the solar specific power density delivered to earth is equivalent to fourteen one-hundred watt light bulbs per square meter of the earth's surface and represents a lot of power!# Chapter 19 <br> Sampling Plans and Confidence Intervals 

Before purchasing a large number of devices, a customer will likely ask the supplier about the defect level for the product being offered. The customer's reliability inquiry is often expressed as: what is the defect level for the population of such devices in terms of number of defective devices per hundred, number of defective devices per thousand, number of defective devices per million (dpm), etc.? To determine the fraction defective, a sample of the devices is randomly selected from the population and this sample is tested/stressed to determine the fraction defective. After the fraction defective is determined for the sample, then it is only natural to ask: based on the sample size used, what is the confidence interval for the population fraction defective? To answer this critically important question, we must understand the basics of sampling theory.

## 1 Poisson Distribution

The statistical distributions discussed in Chaps. 6 and 7 (normal, lognormal, Weibull) are continuous distributions and are well suited for time-to-failure statistics. This is because time-to-failure will take on a continuous spectrum of time- to-failure values. However, in sampling a population, in order to determine the number of defective devices $x$, one will obtain discrete values for $x$ (such as 0 , or 1 , or 2 , etc.). This is because we will view defects as digital-a device is either defective or it is not (it either passes or fails, it is either good or bad, etc.). There will be no consideration given here as to labeling a device as being partially defective. The Poisson distribution is a discrete distribution that is often used in physics, engineering, and manufacturing. It is used to describe the probability of occurrence for discrete random events/processes. Random processes refer to physical events which are controlled purely by chance. Examples of discrete random events include: the number of disintegrations observed in given time intervals for a radioactive material; the number visible stars observed in a small area of the sky as one pans thesky; the number of telephone calls received in given time intervals; the number of defects observed on a silicon wafer (in the field of view of a microscope) as the stage moves; and the number of manufacturing defects observed to come off the assembly line in given time intervals. More reading on the subject of Poisson processes can be found in the bibliography. In this textbook, we only state the needed results a priori. Our attention will be focused on how to use discrete distributions for defect-level determination and how to calculate the appropriate sample size and the confidence levels/intervals associated with the sampling measurement.

# 1.1 Poisson Probability for Finding Defective Devices 

If one draws a random sample of size SS from a large population of devices that has a fraction defective $F$, then the probability of finding $x$ defective devices in the sample is given by the Poisson probability $p(x ; S S, F)$ :

$$
p(x ; S S, F)=\frac{(\mathrm{SS} \cdot F)^{x} \exp [-\mathrm{SS} \cdot F]}{x!}
$$

The probability of getting zero defective devices in the sample size SS is given by,

$$
\begin{aligned}
p(x=0 ; S S, F) & =\frac{(\mathrm{SS} \cdot F)^{0} \exp [-\mathrm{SS} \cdot F]}{0!} \\
& =\exp [-\mathrm{SS} \cdot F]
\end{aligned}
$$

If $p(x=0 ; \mathrm{SS}, F)$ is the Poisson probability of getting zero defective units in SS, then the probability $P$ of getting something other than zero defects in SS is $p(x \neq 0$; $\mathrm{SS}, F)$ :

$$
\begin{aligned}
P=p(x \neq 0 ; \mathrm{SS}, F) & =1-p(x=0 ; \mathrm{SS}, F) \\
& =1-\exp [-\mathrm{SS} \cdot F]
\end{aligned}
$$

$P$ is usually expressed as a fraction/decimal; but, when expressed as a percentage, it is often referred to as a confidence level.

## Example Problem 1

In the integrated circuit (IC) industry, yield (fraction of good electrical chips on a wafer) is a very important manufacturing parameter. Defects introduced during manufacturing can have an adverse impact on yield as illustrated in this figure.
$N=$ Number of Chips on Wafer
$n=$ Number of Randomly Distributed Defects
$N=$ Number of Chips on Wafer
$n=$ Number of Randomly Distributed Defects
Yield is simply the probability of testing a single chip ( $\mathrm{SS}=1$ ) on a wafer (having a total of $N$ such chips and with $n$ randomly distributed defects) and finding that the chip has zero defects $(x=0)$.

Using Eq. (19.2),

1. find an expression for chip yield in terms of $n$ and $N$, and
2. find an alternative expression for yield in terms of defect density dd and the area of a single chip $A_{\text {chip. }}$.

# Solution 

1. If we assume that the wafer contains a total of $n$ randomly distributed defects across the top surface of wafer, then from Eq. (19.2) we obtain:

$$
\begin{aligned}
\text { yield }=p( & \left.x=0 ; \mathrm{SS}=1, F \cong \frac{n}{N}\right) \\
& =\exp \left(-\frac{n}{N}\right)
\end{aligned}
$$

2. IC fabrication centers (Fabs) like to express the yield in terms of a defect density dd over the top surface area of the wafer:

$$
\mathrm{dd}=\frac{n}{\text { Area of Wafer }} \cong \frac{n}{N \cdot A_{\text {chip }}}
$$

Therefore, we can write:$$
\begin{aligned}
\text { yield } & =\exp \left(-\frac{n}{N}\right) \\
& =\exp \left(-\mathrm{dd} \cdot A_{\text {chip }}\right)
\end{aligned}
$$

We should emphasize that the previous equation for yield assumes that the defects are randomly located across the surface of the wafer. If the defects tend to cluster into certain regions of the wafer (e.g., an unusually high number of the defects can sometimes occur near the edge of the wafer) then this yield equation can be too pessimistic in its prediction.

# 1.2 Poisson Sample Size Requirements 

Let us suppose that we test/stress a sample size SS of units, randomly drawn from a large population of such units, to determine the fraction of defective units $F$ in the population. During the testing/stressing of SS we find zero defects. The question that we want to address here is: how large should SS be to ensure that the fraction defective $F$ for the population is less than or equal to some value and at what confidence level? Using Eq. (19.3) we obtain

$$
\mathrm{SS}=\frac{1}{F} \ln \left(\frac{1}{1-P}\right)
$$

Thus, if our hypothesis is that the fraction defective for a group of devices/units is $F$, then at the $P$ confidence level Eq. (19.4) gives the required sample size SS to test the hypothesis. We can use Eq. (19.4) for the sample size SS determination, only if we get zero failures during the testing/stressing of SS.

## Example Problem 2

Assuming that the defects can be described by a Poisson distribution, what should be the minimum sample size SS (with accepting the hypothesis for $F$ only if zero defects are found in the sample) to ensure that the population fraction defective is $F \leq 0.05$ at the $95 \%$ confidence level $(P=0.95)$ ?

## Solution

Using Eq. (19.4) we obtain,$$
\begin{aligned}
\mathrm{SS} & =\frac{1}{F} \ln \left(\frac{1}{1-P}\right) \\
& =\frac{1}{0.05} \ln \left(\frac{1}{1-0.95}\right) \\
& =59.9
\end{aligned}
$$

Therefore, if we select a random sample size of $\mathrm{SS}=60$ units, and test/ stress them and find zero defects, then we can state (at the $95 \%$ confidence level CL using the Poisson distribution) that the fraction defective for the population of such devices is $F \leq 0.05$.

Suppose that we would like to have the flexibility of accepting the hypothesis for $F$ based on something other than finding zero defective units. Suppose that we would like to draw a larger sample size SS but accept the hypothesis for $F$ based on either 0 or 1 . The probability of getting something other than 0 or 1 is given by,

$$
\begin{aligned}
& P=1-p(x=0 ; \mathrm{SS}, F)-p(x=1 ; \mathrm{SS}, F) \\
& =1-\exp [-\mathrm{SS} \cdot F]-(\mathrm{SS} \cdot F) \exp [-\mathrm{SS} \cdot F]
\end{aligned}
$$

Equation (19.5) can be used to solve for SS and we obtain,

$$
\mathrm{SS}=\left(\frac{1}{F}\right) \ln \left[\frac{1+\mathrm{SS} \cdot F}{1-P}\right]
$$

Equation (19.6) can be used to determine the required sample size SS for testing the hypothesis for $F$, at the $P$ confidence level, only if we accept on observations of 0 or 1 defective devices when testing/stressing the sample size SS. Equation (19.6)which is a transcendental equation-can be solved self-consistently as illustrated in Table 19.1.

To find the self-consistent solution to the equation shown at the top of Table 19.1, the left-hand column is iterated while the right-hand column is calculated. One simply finds the iteration at which the left-hand columnar value is approximately equal to the right-hand columnar value. In this example, the self-consistent solution for SS is between 95 and 96 . If a more precise value is required, the interval between 95 and 96 can be subdivided. This process of subdivision can be continued until any desired level of accuracy is achieved by the self-consistent method of solution. However, in sample size SS determination, the SS value is nearly always rounded up; thus, a high accuracy self-consistent solution is usually not required.

In summary, if we select a random sample of size $\mathrm{SS}=96$ and accept only on finding either 0 or 1 defective units, then we can be $95 \%$ confident that the defective fraction for the population of such devices is $F \leq 0.05$. By extending the approach used in Eq. (19.5) to develop Eq. (19.6), the SS requirement for accepting on values other than 0 or 1 can also be computed.Table 19.1 Self-consistent solution for poisson sampling (accepting on either 0 or 1 )

| $\mathrm{SS}=\left(\frac{1}{F}\right) \ln \left[\frac{1+\mathrm{SS} \cdot F}{1-P}\right]$ |  |
| :-- | :-- |
| SS | $\left(\frac{1}{F}\right) \ln \left[\frac{1+\mathrm{SS} \cdot F}{1-P}\right]$ |
| 0 | 59.9 |
| 1 | 60.9 |
| 2 | 61.8 |
| 3 | 62.7 |
| 4 | 63.6 |
| 5 | 64.4 |
| $\cdot$ | $\cdot$ |
| $\cdot$ | $\cdot$ |
| $\cdot$ | $\cdot$ |
| 90 | 94.0 |
| 91 | 94.2 |
| 92 | 94.4 |
| 93 | 94.5 |
| 94 | 94.7 |
| 95 | 94.9 |
| 96 | 95.1 |
| 97 | 95.2 |
| 98 | 95.4 |
| 99 | 95.6 |
| 100 | 95.7 |

# 2 Binomial Distribution 

The binomial distribution is also a discrete distribution and it is a frequently used statistical distribution in manufacturing and engineering. It is a well-suited distribution for defect statistics because it assumes that the outcome of a trial/measurement can have only one of the two outcomes: a device is either defective or it is not. It further assumes that the probability $p$ of finding a defective device is the same for each trial such that the probability of not finding a defect is simply $1-p$.

### 2.1 Binomial Probability for Finding Defective Devices

If one draws a sample size SS of devices/units from a population that has a fraction defective $F$, then the probability of finding $x$ defective devices in the sample is given by the binomial probability $b(x ; \mathrm{SS}, F)$ :

$$
b(x ; S S, F)=\frac{\mathrm{SS}!}{x!(S S-x)!}(F)^{x}(1-F)^{\mathrm{SS}-x}
$$

The probability of getting zero defects in the sample size SS becomes:$$
\begin{aligned}
b(0 ; S S, F) & =\frac{\mathrm{SS}!}{0!(\mathrm{SS}-0)!}(F)^{0}(1-F)^{\mathrm{SS}-0} \\
& =(1-F)^{\mathrm{SS}}
\end{aligned}
$$

If $b(x=0 ; \mathrm{SS}, F)$ is the binomial probability of getting zero defects in SS, then the probability $P$ of getting something other than zero defects in SS is $b(x \neq 0 ; \mathrm{SS}, F)$ :

$$
\begin{gathered}
P=b(x \neq 0 ; S S, F)=1-b(x=0 ; S S, F) \\
=1-(1-F)^{\mathrm{SS}}
\end{gathered}
$$

# 2.2 Binomial Sample Size Requirements 

Let us suppose that we test/stress a sample size SS (of units randomly drawn from the population of such units) to determine the fraction $F$ of defective units in the population. During the testing/stressing of SS we find zero defects. The question that we want to address is: how large should SS be to ensure that the fraction $F$ defective for the population is less than or equal to a certain value and at what confidence level?

Using Eq. (19.6) we obtain,

$$
\mathrm{SS}=\frac{\ln (1-P)}{\ln (1-F)}
$$

Thus, if our hypothesis is that the defective fraction for the population of devices/ units is $F$, then at the $P$ confidence level, Eq. (19.10) gives the required sample size SS to test the hypothesis. We can use Eq. (19.10) for the SS determination to test our hypothesis concerning $F$, only if we get zero failures during the testing/ stressing of SS.

## Example Problem 3

Let us reconsider Example Problem 2-except this time we will use the binomial distribution rather than the Poisson distribution.

## Solution

Using Eq. (19.10) one obtains,$$
\begin{aligned}
\mathrm{SS} & =\frac{\ln (1-P)}{\ln (1-F)} \\
& =\frac{\ln (1-0.95)}{\ln (1-0.05)} \\
& =58.4
\end{aligned}
$$

Therefore, if we select a random sample size $\mathrm{SS}=59$ units $^{1}$ and test/stress them and find zero defects, then we can state (at the $95 \%$ confidence level CL using the binomial distribution) that the population fraction defective is $F \leq$ 0.05 . Note that when we compare the results in Example Problems 2 and 3, we see that the Poisson and binomial distributions give very similar results (sample size of 60 vs. 59 , respectively).

Suppose that we would like to have the flexibility of accepting the hypothesis for $F$ based on something other than finding 0 defective units. Accepting on something other than 0 will require us to draw a larger sample size SS. The probability of finding something other than 0 or 1 is given by,

$$
\begin{aligned}
P & =1-b(x=0 ; \mathrm{SS}, F)-b(x=1 ; \mathrm{SS}, F) \\
& =1-(1-F)^{\mathrm{SS}}-(\mathrm{SS} \cdot F)(1-F)^{\mathrm{SS}-1}
\end{aligned}
$$

Equation (19.11) can be used to solve for SS and we obtain:

$$
\mathrm{SS}=\frac{\ln (1-P)-\ln \left[\frac{1+(\mathrm{SS}-1) F}{1-F}\right]}{\ln (1-F)}
$$

Equation (19.12) can be used to determine the required sample size SS for testing the hypothesis for $F$, at the $P$-confidence level, only if we accept on observations of 0 or 1 defective units when testing/stressing the sample size SS. At the $95 \% \mathrm{CL}(P=$ $0.95)$ and with the hypothesis of $F \leq 0.05$, the self-consistent solution of Eq. (19.12) is shown in Table 19.2 and it gives a sample size $\mathrm{SS}=93$. [Note that this binomial distribution value $\mathrm{SS}=93$ is very close, but slightly lower, than the value $\mathrm{SS}=$ 96 found using the Poisson distribution.]

[^0]
[^0]:    ${ }^{1}$ Generally, in sampling theory, we round up the sample size requirement.Table 19.2 Self-consistent solution for binomial sampling (accepting on either 0 or 1 )

| $\mathrm{SS}=\frac{\ln (1-P)-\ln \left[\frac{1+(\mathrm{SS}-1) F}{1-F}\right]}{\ln (1-F)}$ |  |
| :--: | :--: |
| SS | $\frac{\ln (1-P)-\ln \left[\frac{1+(\mathrm{SS}-1) F}{1-F}\right]}{\ln (1-F)}$ |
| 0 | 58.4 |
| 1 | 59.4 |
| 2 | 60.4 |
| 3 | 61.3 |
| 4 | 62.1 |
| 5 | 63.0 |
| . | . |
| . | . |
| 90 | 92.5 |
| 91 | 92.6 |
| 92 | 92.8 |
| 93 | 93.0 |
| 94 | 93.2 |
| 95 | 93.3 |

# 3 Chi Square Distribution 

Drawing a random sample of size SS from a population containing a fraction $F$ defective will not always produce the expected number of fails SS $\cdot F$. In fact, if we do a series of $k$ trials and keep track of the observed value $O_{i}$ versus the expected value $E_{i}$, and compute the statistic $\chi^{2}$ (read Chi square):

$$
\chi^{2}=\sum_{i=1}^{k} \frac{\left(O_{i}-E_{i}\right)^{2}}{E_{i}}
$$

then this sampling distribution for the statistic $\chi^{2}$ will follow a Chi square distribution.

### 3.1 Chi Square Confidence Intervals

Using the Chi square distribution, we can define a confidence interval for the statistic $\chi^{2}$ as:$$
\chi^{2}(1-P, v) \leq \chi^{2} \leq \chi^{2}(P, v)
$$

where $v(=k-1)$ represents the number of degrees of freedom (the number of times that the population parameters must be estimated to carry out the calculation) and $P$ is a confidence level. In statistics, the right-hand side of Eq. (19.14) is generally referred to as the upper end of the specified range while the left-hand side is generally referred to as the lower end. The values for $\chi^{2}(P, v)$ and $\chi^{2}(1-P, v)$ can be found in standard statistical textbooks or simply can be determined using standard Excel functions. In Excel, $\chi^{2}(P, v)=\operatorname{CHIINV}(1-P, v)$ and $\chi^{2}(1-P, v)=\operatorname{CHIINV}(P, v)$. The $\chi^{2}(P, v)$ values are also shown in Appendix H.

Let us now consider the case where we draw a single sample size SS from a large population of devices with a defective fraction $F$. We would expect to get SS $\cdot F$ defects but we observe SS $\cdot F_{s}$ from the sampling. Thus, using Eq. (19.13) and (19.14), from this single sample we have:

$$
\chi^{2}(1-P, v) \leq \frac{\left(\mathrm{SS} \cdot F_{s}-\mathrm{SS} \cdot F\right)^{2}}{\mathrm{SS} \cdot F} \leq \chi^{2}(P, v)
$$

Equation (19.11) can be rewritten as,

$$
\frac{\chi^{2}(1-P, v)}{[(x / \mathrm{SS})-F]^{2} / F} \leq \mathrm{SS} \leq \frac{\chi^{2}(P, v)}{[(x / \mathrm{SS})-F]^{2} / F}
$$

where we have used the fact that $F_{s}=x / \mathrm{SS}$ and where $x$ is the number of defective devices observed in the sample size SS. For dichotomous data (devices are either defective or non-defective), then the appropriate number of degrees of freedom is $v=k-1=2-1=1$. Thus, using the upper end of the specified range in the last equation to determine the sample size SS, which should be randomly drawn from the population, to be $P$ confident that the fraction defective in population is less than or equal to F :

$$
\mathrm{SS}=\frac{\chi^{2}(P, v=1)}{[(x / \mathrm{SS})-F]^{2} / F}
$$

# Example Problem 4 

Let us reconsider Example Problem 2-except this time we will use the Chi square distribution rather than the Poisson distribution.

## Solution

Using Eq. (19.17) (along with Appendix H) and accepting on finding $x=$ 0 failures in the sample, the needed sample size SS is:$$
\begin{aligned}
\mathrm{SS} & =\frac{\chi^{2}(P, v=1)}{[(x / \mathrm{SS})-F]^{2} / F} \\
& =\frac{\chi^{2}(0.95, v=1)}{F} \\
& =\frac{3.84}{0.05}=77
\end{aligned}
$$

Therefore, using this particular Chi square distribution approach, if we select a random sample size of $\mathrm{SS}=77$ units and test/stress them and find zero defects, then we can state at the $95 \%$ confidence level CL (using the Chi square distribution) that the fraction defective is $F \leq 0.05$. [Note that the Poisson and binomial distributions, Example Problems 2 and 3, gave somewhat smaller sample requirements ( $\mathrm{SS}=60$ and 59 , respectively).]

# 3.2 Chi Square Distribution for Defect Sampling 

In order to get better agreement (in the required sample size) between the Chi square distribution and the other two distributions (Poisson and binomial), and in order to avoid the necessity of having to do the self-consistent solution for SS, a variation of Eq. (19.16) is preferred:

$$
\frac{\left[\chi^{2}(1-P, v=2 x)\right] / 2}{F} \leq \mathrm{SS} \leq \frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{F}
$$

where $x$ is the number of defective units found in the random sample size SS. Using the upper end of the specified range, the sample size SS requirement (at the $P$ confidence level) becomes:

$$
\mathrm{SS}=\frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{F}
$$

By rearranging terms, another useful equation follows from Eq. (19.18):

$$
\frac{\left[\chi^{2}(1-P, v=2 x)\right] / 2}{\mathrm{SS}} \leq F \leq \frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{\mathrm{SS}}
$$

Equation (19.20) can be used to determine, at the $P$ confidence level, the appropriate confidence interval for the population fraction defective $F$ when a sample size of SS is randomly drawn from a large population and tested/stressed. When using Eq. (19.20), a special case arises when we draw a sample and get zerodefects. The left-hand side of Eq. (19.20) is not defined when $x=0$, because $\chi^{2}(1-P$, $v=0$ ) is not defined. In this case the left-hand side of Eq. (19.20) is set to zero. Setting to zero is consistent with our observation-zero defects were found in the sample size SS which means that it is at least possible that zero defects may actually exist in the population. However, the possibility of the population having zero defects is eliminated as soon as we obtain at least one defect in our sample size SS-thus $\chi^{2}(1-P, v=2)$ is defined.

# Example Problem 5 

Using the Chi square distribution [Eq. (19.19)], find the required sample size SS at the $95 \% \mathrm{CL}(P=0.95)$ which should be tested/stressed, to detect a population defective fraction of $F=0.05$ ? Assume two conditions for acceptance:
(a) accept only on finding zero defective units, and
(b) accept only on finding 1 (or zero) defective units.

## Solution

(a) Using Eq. (19.19), along with Appendix H, one obtains for $x=0$ :

$$
\begin{aligned}
\mathrm{SS} & =\frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{F} \\
& =\frac{\left[\chi^{2}(0.95,2)\right] / 2}{0.05} . \\
& =\frac{5.99 / 2}{0.05}=60
\end{aligned}
$$

(b) Using Eq. (19.19), along with Appendix H, one obtains for $x=1$ :

$$
\begin{aligned}
\mathrm{SS} & =\frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{F} \\
& =\frac{\left[\chi^{2}(0.95,4)\right] / 2}{0.05} . \\
& =\frac{9.49 / 2}{0.05}=95
\end{aligned}
$$

From Example Problems 2, 3, and 5, we can see that Eq. (19.19) gives good agreement with the Poisson and binomial distributions and requires no self- consistent type solutions for sample size determination. Therefore, Eqs. (19.19) and (19.20) will become the preferred equations to use for sampling in this textbook.# Example Problem 6 

A random sample of 100 devices was drawn from a large population of such devices and tested/stressed. It was found that $x=2$ of the devices were defective (or $2 \%$ defective). What is the $90 \%$ confidence-level interval for the fraction $F$ defective of the population?

## Solution

Equation (19.20), along with Appendix H, gives the $P$ confidence-level interval for $F$ :

$$
\begin{aligned}
& \frac{\left[\chi^{2}(1-P, v=2 x)\right] / 2}{\mathrm{SS}} \leq F \leq \frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{\mathrm{SS}} \\
& \Rightarrow \frac{\left[\chi^{2}(0.1,4)\right] / 2}{100} \leq F \leq \frac{\left[\chi^{2}(0.9,6)\right] / 2}{100} \\
& \Rightarrow 0.0053 \leq F \leq 0.053
\end{aligned}
$$

Although our sample size $\mathrm{SS}=100$ units indicated a percentage defective of $2 \%$, the $90 \%$ confidence interval for the population defective is between 0.53 and $5.3 \%$.

## 4 Confidence Intervals for Characteristic Time-to-Failure and Dispersion Parameters

In Chap. 7 we discussed continuous distributions (lognormal and Weibull) that could be used to describe time-to-failure when a random sample was drawn from the population of such devices and stressed to failure. However, there was no discussion on the confidence intervals for such sampling. We will first discuss the confidence intervals for the normal distribution because it will serve as a good introduction to the confidence intervals associated with the lognormal and Weibull distributions.

### 4.1 Normal Distribution Confidence Intervals

Let us suppose that a single sample size SS is drawn randomly from a large population of devices and that a device parameter is measured and recorded for each device. From this single sample, the parameter is found to be normally distributed (approximately) with a median value of $\left(x_{50}\right)_{s}$ and standard deviation $(\sigma)_{s}$. The question that we want to address here is-what are the confidence intervals for the population parameters $x_{50}$ and $r$ based on this single sample? The confidence interval for $x_{50}$ can be described using a Student's $t$-distribtution:$$
x_{50}=\left(x_{50}\right)_{s} \pm t(1-\alpha / 2, \quad \text { SS }-1) \cdot \frac{\sigma_{s}}{\sqrt{\mathrm{SS}-1}}
$$

where $\left(x_{50}\right)_{s}$ and $\sigma_{s}$ are the sample median and standard deviation values; $\alpha$ is the level of significance $\left(0.1,0.05,0.01\right.$, etc. $)^{2} ; P$ is the confidence level $(P=1-\alpha)$; SS is the sample size; $\sigma_{s}=\left(x_{50}\right)_{s}-\left(x_{16}\right)_{s}$; and $t$ stands for the student's $t$-distribution. In Excel, $t(1-\alpha / 2$, SS - 1$)=\operatorname{TINV}(\alpha$, SS - 1$)$ and values are also shown in Appendix G. The $P$ confidence interval for the population standard deviation is given by:

$$
\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \leq \sigma \leq\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s}
$$

where: $\sigma_{s}$ is the sample standard deviation; $\sigma$ is the population standard deviation; SS is the sample size; $P$ is the confidence level; and $\chi^{2}$ represents the Chi square distribution. In Excel, $\chi^{2}(P, \mathrm{SS}-1)=\mathrm{CHIINV}(1-P, \mathrm{SS}-1)$ and $\chi^{2}(1-P, \mathrm{SS}-1)$ $=\mathrm{CHIINV}(P, \mathrm{SS}-1)$. The $t$-distribution and the Chi square distributions are used because they may be used for both small and large sample sizes.

# Example Problem 7 

A sample size $\mathrm{SS}=30$ was randomly drawn from a large population of resistors. The sampling results for the resistors were: $\left(x_{50}\right)_{s}=14.00 \Omega$ with a standard deviation of $\sigma_{s}=0.80 \Omega$. Determine the $90 \%$ confidence intervals for the population median and standard deviation.

## Solution

$90 \% \mathrm{CL} \Rightarrow P=1-\alpha=0.9 \Rightarrow \alpha=0.1$. Equation (19.21), along with Appendix G, gives:

$$
\begin{aligned}
x_{50} & =\left(x_{50}\right)_{s} \pm t(1-\alpha / 2, \mathrm{SS}-1) \cdot \frac{\sigma_{s}}{\sqrt{\mathrm{SS}-1}} \\
& =\left(14.00 \pm t(0.95,29) \cdot \frac{0.80}{\sqrt{30-1}}\right) \Omega \\
& =\left(14.00 \pm 1.70 \cdot \frac{0.80}{\sqrt{29}}\right) \Omega \\
& =(14.00 \pm 0.25) \Omega
\end{aligned}
$$

Therefore, the $90 \%$ confidence interval for the mean/median $x_{50}$ of the population is from 13.75 to $14.25 \Omega$.
(continued)

[^0]
[^0]:    ${ }^{2}$ The level of significance $a$ is the probability that population $x_{50}$ could be outside the range given by Eq. (19.21). The confidence level $P$ is the probability that the population $x_{50}$ will be within the range described by Eq. (19.21). Thus, $P$ is the complement of $a$ such that $P+\alpha=1$.Equation (19.22), along with Appendix H, gives:

$$
\begin{aligned}
& \left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \leq \sigma \leq\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \\
& \Rightarrow\left(\sqrt{\frac{30}{\chi^{2}(0.9,29)}}\right) \cdot 0.80 \Omega \leq \sigma \leq\left(\sqrt{\frac{30}{\chi^{2}(0.1,29)}}\right) \cdot 0.80 \Omega \\
& \Rightarrow\left(\sqrt{\frac{30}{391}}\right) \cdot 0.80 \Omega \leq \sigma \leq\left(\sqrt{\frac{30}{198}}\right) \cdot 0.80 \Omega \\
& \Rightarrow 0.70 \Omega \leq \sigma \leq 0.98 \Omega
\end{aligned}
$$

Therefore, the $90 \%$ confidence interval for the standard deviation $\sigma$ of the population is from 0.70 to $0.98 \Omega$.

# 4.2 Lognormal Distribution Confidence Intervals 

Remembering that the normal distribution becomes a lognormal distribution if the logarithm of the values is used, then Eq. (19.17) can be used to write:

$$
\ln \left[\mathrm{TF}_{50}\right]=\ln \left[\left(\mathrm{TF}_{50}\right)_{s}\right] \pm t(1-\alpha / 2, \mathrm{SS}-1) \cdot \frac{\sigma_{s}}{\sqrt{\mathrm{SS}-1}}
$$

Equation (19.23) can be rewritten as:

$$
\mathrm{TF}_{50}=\left(\mathrm{TF}_{50}\right)_{s} \exp \left[ \pm t(1-\alpha / 2, \mathrm{SS}-1) \cdot \frac{\sigma_{s}}{\sqrt{\mathrm{SS}-1}}\right]
$$

The confidence interval for the logarithmic standard deviation $r$ takes the same form as Eq. (19.22),

$$
\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \leq \sigma \leq\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s}
$$

## Example Problem 8

A sample size of $\mathrm{SS}=25$ devices was randomly drawn from a large population of such devices and the sample was stressed at a constant level until thetime-to-failure was recorded for each device. The time-to-failure results were described well by a lognormal distribution with a median time-to- failure of $\left(t_{50}\right)_{s}=42 \mathrm{~h}$ with a logarithmic standard deviation of $r_{s}=0.50$. Determine the $90 \%$ confidence intervals for the population median time-to- failure $t_{50}$ and the population logarithmic standard deviation $r$.

# Solution 

$90 \% C L \Rightarrow P=1-\alpha=0.9 \Rightarrow \alpha=0.1$. Using Eq. (19.24), along with Appendix G, for the population $\mathrm{TF}_{50}$, one obtains:

$$
\begin{aligned}
& \mathrm{TF}_{50}=\left(\mathrm{TF}_{50}\right)_{s} \exp \left[ \pm t(1-\alpha / 2, \mathrm{SS}-1) \cdot \frac{\sigma_{s}}{\sqrt{\mathrm{SS}-1}}\right] \\
& =(42 \mathrm{~h}) \exp \left[ \pm t(0.95,24) \cdot \frac{0.50}{\sqrt{24}}\right] \\
& =(42 \mathrm{~h}) \exp \left[ \pm 1.71 \cdot \frac{0.50}{\sqrt{24}}\right] \\
& \Rightarrow 35.3 \mathrm{~h} \leq \mathrm{TF}_{50} \leq 50.0 \mathrm{~h} .
\end{aligned}
$$

Therefore, the $90 \%$ confidence interval for the population $\mathrm{TF}_{50}$ is between 35.3 and 50.0 h . Using Eq. (19.25), along with Appendix H, for the population $\sigma$, we obtain:

$$
\begin{aligned}
& \left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \leq \sigma \leq\left(\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}\right) \cdot \sigma_{s} \\
& \Rightarrow\left(\sqrt{\frac{25}{\chi^{2}(0.9,24)}}\right) \cdot 0.50 \leq \sigma \leq\left(\sqrt{\frac{25}{\chi^{2}(0.1,24)}}\right) \cdot 0.50 \\
& \Rightarrow\left(\sqrt{\frac{25}{332}}\right) \cdot 0.50 \leq \sigma \leq\left(\sqrt{\frac{25}{157}}\right) \cdot 0.50 \\
& \Rightarrow 0.43 \leq \sigma \leq 0.63
\end{aligned}
$$

Therefore, the $90 \%$ confidence interval for the population $\sigma$ is between 0.43 and 0.63 .# 4.3 Weibull Distribution Confidence Intervals 

Starting with Eq. (19.20) and using characteristics of the Weibull distribution [ $\mathrm{TF}_{50}$ $=\mathrm{TF}_{63} / \exp (0.367 / \beta)]$ plus the approximate relation between the lognormal and Weibull dispersion parameters $[r=1.38 / b]$, one can write:

$$
\mathrm{TF}_{63}=\frac{\left(\mathrm{TF}_{63}\right)_{s}}{\exp \left[\frac{0367}{\beta_{s}}\left(1-\frac{\beta_{s}}{\beta}\right)\right]} \exp \left[ \pm t(1-\alpha / 2, \quad \mathrm{SS}-1) \cdot \frac{1.38}{\beta_{s} \sqrt{\mathrm{SS}-1}}\right]
$$

From sampling theory we will use the relation:

$$
\frac{\beta_{s}}{\beta}=\frac{\sigma}{\sigma_{s}}=\sqrt{\frac{\mathrm{SS}}{\mathrm{SS}-1}}
$$

Using Eqs. (19.26) and (19.27) can now be rewritten as:

$$
\mathrm{TF}_{63}=\left(\mathrm{TF}_{63}\right)_{s} \exp \left[\frac{0.367}{\beta_{s}}\left(\sqrt{\frac{\mathrm{SS}}{\mathrm{SS}-1}}-1\right)\right] \exp \left[ \pm t(1-\alpha / 2, \quad \mathrm{SS}-1) \cdot \frac{1.38}{\beta_{s} \sqrt{\mathrm{SS}-1}}\right]
$$

The first exponential term in Eq. (19.28) is normally small for $\beta_{s}>1$ and for sample sizes SS of 20 or more. Thus, it is often ignored and we approximate the confidence intervals for the Weibull distribution as:

$$
\mathrm{TF}_{63} \cong\left(\mathrm{TF}_{63}\right)_{s} \exp \left[ \pm t(1-\alpha / 2, \quad \mathrm{SS}-1) \cdot \frac{1.38}{\beta_{s} \sqrt{\mathrm{SS}-1}}\right]
$$

and

$$
\frac{\beta_{s}}{\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}}} \geq \beta \geq \frac{\beta_{s}}{\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}}
$$

## Example Problem 9

A device sample size $\mathrm{SS}=25$ was randomly drawn from a large population of such devices and the sample was stressed at a constant level until the time-tofailure was recorded for each device. The time-to-failure results for the sample were well described by a Weibull distribution with a characteristic time-tofailure of $\left(t_{63}\right)_{s}=48 \mathrm{~h}$ with a Weibull slope of $\beta_{s}=2.76$. Determine the $90 \%$confidence interval for the population characteristic time-to-failure $t_{63}$ and the population Weibull slope $\beta$.

# Solution 

$90 \% C L \Rightarrow P=1-\alpha=0.9 \Rightarrow \alpha=0.1$. Equation (19.29), along with Appendix G, gives:

$$
\begin{gathered}
\mathrm{TF}_{63} \cong\left(\mathrm{TF}_{63}\right)_{s} \exp \left[ \pm t(1-\alpha / 2, \quad \mathrm{SS}-1) \cdot \frac{1.38}{\beta_{s} \sqrt{\mathrm{SS}-1}}\right] \\
=(48 \mathrm{~h}) \exp \left[ \pm t(0.95,24) \cdot \frac{1.38}{2.76 \sqrt{24}}\right] \\
=(48 \mathrm{~h}) \exp \left[ \pm 1.71 \cdot \frac{1.38}{2.76 \sqrt{24}}\right] \\
\Rightarrow 40.3 \mathrm{~h} \leq \mathrm{TF}_{63} \leq 57.2 \mathrm{~h}
\end{gathered}
$$

Equation (19.30), along with Appendix H, gives:

$$
\begin{aligned}
& \frac{\beta_{s}}{\sqrt{\frac{\mathrm{SS}}{\chi^{2}(P, \mathrm{SS}-1)}} \geq \beta \geq \frac{\beta_{s}}{\sqrt{\frac{\mathrm{SS}}{\chi^{2}(1-P, \mathrm{SS}-1)}}}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \frac{2.76}{\sqrt{\frac{25}{\chi^{2}(0.9,24)}} \geq \beta \geq \frac{2.76}{\sqrt{\frac{25}{\chi^{2}(0.1,24)}}}} \\
& \Rightarrow \frac{2.76}{\sqrt{\frac{25}{33.2}} \geq \beta \geq \frac{2.76}{\sqrt{\frac{25}{15.7}}}} \\
& \Rightarrow 3.18 \geq \beta \geq 2.19
\end{aligned}
$$

Therefore, the $90 \%$ confidence interval for the population characteristic time-to-failure $\mathrm{TF}_{63}$ is between 40.3 and 57.2 h ; the $90 \%$ confidence interval for the population Weibull slope $\beta$ is between 2.19 and 3.18.# 4.4 Chi Square Distribution Confidence Intervals for Average Failure Rates 

In Chap. 8, Sec. 2, we found that, for small cumulative determines fraction $F$, the average failure rate $\langle\lambda\rangle$ for a population of devices could be estimated by:

$$
\langle\lambda\rangle \cong \frac{F(t)}{t}=\frac{(\mathrm{SS}) \cdot F(t)}{(\mathrm{SS}) \cdot t}=\frac{\# \text { failures }}{(\mathrm{SS}) \cdot t}
$$

where $F(t)$ is the cumulative fraction of failures observed during the time interval $t$; SS is the sample size drawn from the population of such devices; and \#failures represents the cumulative number of failures observed during the time interval $t$. Since most devices will be required to last 10 years or more, it is impractical to wait the needed 10+ years to measure the actual average failure rate. Therefore, we have to accelerate the observation time $t$.

In Chap. 10 we found that, by increasing the stress $n$ (electric field, mechanical stress, humidity, etc.) and/or increasing the temperature of operation, the stressing time $t_{\text {Stress }}$ could be accelerated:

$$
t=(\mathrm{AF}) \cdot t_{\text {Stress }}
$$

Combining Eqs. (19.31) and (19.32) we obtain ${ }^{3}$ :

$$
\langle\lambda\rangle \cong \frac{\# \text { failures }}{\text { (SS) } \cdot\left(\mathrm{AF} \cdot t_{\text {Stress }}\right)}
$$

It is only natural to ask: how confident are we that Eq. (19.33) represents a good estimate of the average failure rate for the entire population of such devices? For example, several samplings using identical size SS might produce different results: a first sampling might produce two failures; a second sampling might produce four failures; and a third sampling might produce zero failures. Thus, if we are only drawing a single sample size SS from the population, how confident are we that we are capturing the true average failure rate for the entire population? Using Eq. (19.20), plus the fact that \#failures $=\mathrm{SS} \cdot F(t)$, we see that the number of observed failures (at the $P$ confidence level) can be expressed as:

$$
\left[\chi^{2}(1-P, \quad v=2 x)\right] / 2 \leq\left(\text { \#failures) }_{P-\mathrm{CL}} \leq\left[\chi^{2}(P, \quad v=2 x+2)\right] / 2\right.
$$

[^0]
[^0]:    ${ }^{3}$ Note that this equation gives only single point estimation for the average failure rate over the interval $t$. It does not tell us whether the failure rate is increasing, decreasing, or remains constant. To determine this, several sequential periods of time would have to be studied.where $x$ represents the number of failures actually observed in the sample size SS. Therefore, the average failure rate $\langle\lambda\rangle$ (at the $P$ confidence level) for a population of such devices, based on a single sample size SS, is given by:

$$
\frac{\left[\chi^{2}(1-P, v=2 x)\right] / 2}{(\mathrm{SS}) \cdot\left(\mathrm{AF} \cdot t_{\text {Stress }}\right)} \leq\langle\lambda\rangle_{@ P-\mathrm{CL}} \leq \frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{(\mathrm{SS}) \cdot\left(\mathrm{AF} \cdot t_{\text {Stress }}\right)}
$$

In summary, the usual practice for determining the average failure rate for a large population of devices (operating under normal use conditions) is to draw a single random sample (of size SS) and then place the sample under accelerated testing conditions-being careful to record the number of failures $x$ that actually occur during the stressing time interval $t_{\text {Stress }}$. Then, using Eq. (19.35), one can determine the upper end [right side of Eq. (19.35)] and the lower end [left side of Eq. (19.35)] of the expected average failure rate for the entire population of such devices (operating under normal use conditions and over the effective time interval $t=\mathrm{AF} \cdot t_{\text {Stress }}$ ).

# Example Problem 10 

In the qualification of ICs, it is often required to take a random sample of at least 231 chips (from a large population of such chips) and then stress the chips under high temperature operating lifetest (HTOL) conditions for $1,000 \mathrm{~h}$, sometimes at elevated voltages. Suppose that we obtain zero failures from this HTOL testing. Assuming that the combined temperature and voltage acceleration factor during HTOL was $\mathrm{AF}=100$, there are several questions that we would like to address.

1. The accelerated stress time was $1,000 \mathrm{~h}$, but what would be the equivalent/ effective observation time under normal use conditions?
2. What would be the upper end estimate for the average failure rate (at the $90 \%$ confidence level) for the entire population of such chips when they are operated under normal use conditions?
3. At the $90 \%$ confidence level, what is the upper end for the faction of the chips that would be expected to fail after 10 years of normal service?
4. If chip reliability $R(t)$ is defined as $R(t)=1-F(t)$, then what is the expected chip reliability (at the $90 \%$ confidence level) after 10 years of normal use?

## Solution

1. Effective observation time for the sample of chips is:

$$
t=(\mathrm{AF}) \cdot t_{\text {Stress }}=100 \cdot 1,000 \mathrm{~h}=100,000 \mathrm{~h}=11.4 \text { years }
$$

(continued)2. The upper end of average failure rate estimation (at $90 \%$ confidence level) is given by Eq. (19.35). Using Appendix H for the Chi square distribution value, we obtain:

$$
\begin{aligned}
& \langle\lambda\rangle_{\Theta P-\mathrm{CL}} \leq \frac{\left[\chi^{2}(P, v=2 x+2)\right] / 2}{(\mathrm{SS}) \cdot\left(\mathrm{AF} \cdot t_{\text {Stress }}\right)}=\frac{\left[\chi^{2}(0.9, v=2)\right] / 2}{(231) \cdot(100 \cdot 1,000 \mathrm{~h})} \\
& =\frac{4.61 / 2}{2.31 \times 10^{7} \mathrm{~h}}=1.0 \times 10^{-7} / \mathrm{hr}=100 \mathrm{Fit} \\
& \therefore\langle\lambda\rangle_{\Theta 90 \%-\mathrm{CL}} \leq 100 \text { Fit }
\end{aligned}
$$

3. For an average failure rate of $\langle\lambda\rangle=1$ Fit $=10^{-9} / \mathrm{h}$ over 11.4 years of normal use conditions, then the fraction of failures (after 10 years of normal use conditions) becomes [see Eq. (5) in Chap. 7)]:

$$
\begin{gathered}
F(t=10 \text { years })=1-\frac{M(t=10 \text { years })}{M(t=0)}=1-\exp [-\langle\lambda\rangle t] \\
=1-\exp \left[-\left(10^{-7} / \mathrm{hr}\right) \cdot 87,600 \mathrm{hr}\right] \\
=8.8 \times 10^{-3}
\end{gathered}
$$

4. For 10 years of service (under normal use conditions), this chip has a reliability $R$ of (at the $90 \%$ confidence level):
$R=1-F(t=10$ years $)=0.9912$
or
$R=99.12 \%$ reliable at the $90 \%$ Confidence Level

# Problems 

1. To find the fraction of defective medical devices, from a large population of such devices, a sample size of 100 devices was randomly selected from the population and tested. One defective device was found. Using the Chi square distribution, what is the $90 \%$ confidence interval for the fraction defective of the population of such devices?

Answer: $0.00105 \leq F \leq 0.0389$
2. To find the fraction defective of a large population of stainless steel pipes, a sample size of 50 pipes was randomly selected from the population of such pipes and the sample was pressurized to 1,000 psi. Zero defects were found. Using theChi square distribution, what is the $90 \%$ confidence interval for the fraction defective of the population of such pipes?

Answer: $0 \leq F \leq 0.0461$
3. An electronics store is worried about the defect level for a large population of TVs being sold. Using the Chi square distribution, what sample size should be randomly selected from the population, turned on and tested, to ensure (at $90 \%$ confidence level) that the fraction defective is $\leq 0.5 \%$ ? Assume that we accept only on finding zero defects in the sample.

Answer: $\mathrm{SS}=47$
4. Valves, going into the cooling system of a nuclear reactor, must have a very low level fraction defective $\leq 0.1 \%$. Using the Chi square distribution, at the $90 \%$ confidence level, what sample size should be randomly drawn from a large population of such valves and then tested/stressed with accepting only on zero defective valves being found in the sample?

Answer: $\mathrm{SS}=2,303$
5. Balloons are being tested for defectivity. Using the Chi square distribution, at the $90 \%$ confidence level, how many balloons should be randomly drawn from a large population of such balloons and pressurized/tested to claim that the fraction of defective balloons in the population is $\leq 1 \%$ ?
(a) Assume that you accept only when finding zero defects in the sample of size SS.
(b) Assume that you accept only when finding one or fewer defects in the sample of size SS.
(c) Assume that you accept only when finding two or fewer defects in the sample of size SS.

Answers: (a) $\mathrm{SS}=231$, (b) $\mathrm{SS}=389$, (c) $\mathrm{SS}=533$
6. A sample size of 25 O -rings was randomly selected from a large population of such O-rings and the results for the sample followed closely a normal distribution with a mean/median value of $\left(x_{50}\right)_{s}=181.6 \mathrm{~mm}$ and with a standard deviation of $\sigma_{\mathrm{s}}=3.2 \mathrm{~mm}$. What are the $90 \%$ confidence intervals for the population $x_{50}$ and the population $\sigma$ ?

Answers: ( $180.5 \mathrm{~mm} \leq x_{50} \leq 182.7 \mathrm{~mm}$ ) and ( $2.8 \mathrm{~mm} \leq \sigma \leq 4.0 \mathrm{~mm}$ )
7. In an electromigration test, 30 metal conductors were randomly selected from a large population of such conductors and stressed at a constant current density until the time-to-failure for each conductor was recorded. The time-to-failure data for the sample was described well by a lognormal distribution with a median time-to-failure of $\left(t_{50}\right)_{s}=412 \mathrm{~h}$ and with a logarithmic standard deviation of $\sigma_{s}=$ 0.52 . What are the $90 \%$ confidence intervals for the population $t_{50}$ and $\sigma$ ?

Answers: ( $350 \mathrm{~h} \leq \mathrm{TF}_{50} \leq 485 \mathrm{~h}$ ) and ( $0.46 \leq \sigma \leq 0.64$ )8. In a corrosion test, 26 devices were randomly selected from a large population of such devices and stressed at a constant humidity and temperature until the time- to-failure for each device was recorded. The time-to-failure data for the sample was described well by a lognormal distribution with a median time-tofailure of $\left(t_{50}\right)_{s}=212 \mathrm{~h}$ and with a logarithmic standard deviation of $\sigma_{s}=0.42$. What are the $90 \%$ confidence intervals for the population $t_{50}$ and $\sigma$ ?
Answers: $\left(184 \mathrm{~h} \leq T F_{50} \leq 245 \mathrm{~h}\right)$ and $(0.37 \leq \sigma \leq 0.53)$
9. In a thermal cycling fatigue test, a sample of 29 devices was randomly selected from a large population of such devices and the sample was cycled from -65 to $+150{ }^{\circ} \mathrm{C}$ until failure occurred. The cycles-to-failure data for the sample was described well by a lognormal distribution with a median cycle- to-failure of $\left(\mathrm{CTF}_{50}\right)_{s}=812$ cycles and a logarithmic standard deviation of $\sigma_{s}=0.64$. What are the $90 \%$ confidence intervals for the population $\mathrm{CTF}_{50}$ and $\sigma$ ?
Answers: $\left(661 \mathrm{cyc} \leq \mathrm{CTF}_{50} \leq 997 \mathrm{cyc}\right)$ and $(0.56 \leq \sigma \leq 0.79)$
10. In a time-dependent dielectric breakdown (TDDB) test, a sample of 25 capacitors was randomly selected from a large population of such capacitors and the sample was TDDB stressed at a constant voltage and temperature until the time-to-failure for each device was recorded. The time-to-failure data for the sample was described well by a Weibull distribution with a characteristic time-to-failure of $\left(t_{63}\right)_{s}=505 \mathrm{~h}$ and a Weibull slope of $\beta_{s}=1.82$. What are the $90 \%$ confidence intervals for the population $t_{63}$ and $\beta$ ?
Answers: $\left(388 \mathrm{~h} \leq \mathrm{TF}_{63} \leq 658 \mathrm{~h}\right)$ and $(2.10 \geq \beta \geq 1.47)$

# Bibliography 

Ash, C.: The Probability Tutoring Book, IEEE Press, (1993).
Bowker, A. and G. Lieberman: Engineering Statistics, Prentice-Hall Publishing, (1972).
Devore, J: Probability and Statistics for Engineers and Scientists, 6th Ed., Thomson/Brooks/ Cole Publishing, 2004.
Fowler, J., L. Cohen and P. Jarvis: Practical Statistics for Field Biology, John Wiley \& Sons, (1998).

Larsen, R.: Engineering with EXCEL, 2nd Ed., Pearson/Prentice Hall Publishing, (2005).
Miller, I. and J. Freund: Probability and Statistics for Engineers, Prentice Hall Publishing, (1977).# AppendicesAppendix A: Useful Conversion Factors

| Length | $1 \mathrm{~m}=10^{2} \mathrm{~cm}$ | $10^{10} \AA$ | $10^{6} \mu \mathrm{~m}$ | $10^{9} \mathrm{~nm}$ | $3.937 \times 10^{1} \mathrm{in}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Area | $1 \mathrm{~m}^{2}=10^{4} \mathrm{~cm}^{2}$ | $10^{20} \AA^{2}$ | $10^{-6} \mathrm{~km}^{2}$ | $10^{18} \mathrm{~nm}^{2}$ | $1.550 \times 10^{3} \mathrm{in}^{2}$ |
| Volume | $1 \mathrm{~m}^{3}=10^{6} \mathrm{~cm}^{3}$ | $10^{30} \AA^{3}$ | $10^{-9} \mathrm{~km}^{3}$ | $10^{27} \mathrm{~nm}^{3}$ | $10^{3} \mathrm{~L}$ |
| Mass | $1 \mathrm{~kg}=10^{3} \mathrm{~g}$ | $6.852 \times 10^{-2}$ slug | $3.527 \times 10^{1} \mathrm{oz}$ | 2.205 lb | $1.102 \times 10^{-3}$ ton |
| Density | $1 \mathrm{~kg} / \mathrm{m}^{3}=1 \times 10^{-3} \mathrm{~g} / \mathrm{cm}^{3}$ | $1.940 \times 10^{-3}$ slug/ $\mathrm{ft}^{3}$ | $6.243 \times 10^{-2} \mathrm{lb} / \mathrm{ft}^{3}$ | $3.613 \times 10^{-5} \mathrm{lb} / \mathrm{in}^{3}$ | $1.686 \mathrm{lb} / \mathrm{yd}^{3}$ |
| Time | $1 \mathrm{~s}=1.667 \times 10^{-2} \mathrm{~min}$ | $2.778 \times 10^{-4} \mathrm{~h}$ | $1.157 \times 10^{-5}$ day | $3.803 \times 10^{-7}$ months | $3.169 \times 10^{-8}$ year |
| Speed | $1 \mathrm{~m} / \mathrm{s}=100 \mathrm{~cm} / \mathrm{s}$ | $3.600 \mathrm{~km} / \mathrm{h}$ | $3.281 \mathrm{ft} / \mathrm{s}$ | $2.237 \mathrm{mi} / \mathrm{h}$ | $1.967 \times 10^{2} \mathrm{ft} / \mathrm{min}$ |
| Force | $1 \mathrm{~N}=10^{5}$ dyne | $2.248 \times 10^{-1} \mathrm{lb}$ | 7.233 pdl | $1.020 \times 10^{2} \mathrm{gf}$ | $1.020 \times 10^{-1} \mathrm{kgf}$ |
| Stress | $1 \mathrm{~Pa}=1 \mathrm{~N} / \mathrm{m}$ | 10 dyne/cm | $9.869 \times 10^{-6} \mathrm{~atm}$ | $10^{-2}$ millibar | $7.501 \times 10^{-4} \mathrm{~cm} \mathrm{Hg}$ |
| Energy | $1 \mathrm{~J}=10^{7}$ erg | $7.376 \times 10^{-1} \mathrm{ft} \cdot \mathrm{lb}$ | $9.481 \times 10^{-4} \mathrm{Btu}$ | $2.389 \times 10^{-1} \mathrm{cal}$ | $6.242 \times 10^{18} \mathrm{eV}$ |
| Power | $1 \mathrm{~W}=1 \mathrm{~J} / \mathrm{s}$ | $7.376 \times 10^{-1}(\mathrm{ft} \cdot \mathrm{lb}) / \mathrm{s}$ | $9.481 \times 10^{-4} \mathrm{Btu} / \mathrm{s}$ | $2.389 \times 10^{-1} \mathrm{cal} / \mathrm{s}$ | $2.778 \times 10^{-7}(\mathrm{~kW} \mathrm{~h}) / \mathrm{s}$ |
| Temp | $\mathrm{T}(\mathrm{K})=\mathrm{T}\left({ }^{\circ} \mathrm{C}\right)+273.15$ | $(5 / 9) \mathrm{T}\left({ }^{\circ} \mathrm{F}\right)+255.37$ |  |  |  |# Appendix B: Useful Physical Constants 

| Physical constant | Value | Units |
| :-- | :-- | :-- |
| Avagadro's number | $N_{0}=6.02 \times 10^{23}$ | Particles/mole |
| Electronic charge | $e=1.60 \times 10^{-19}$ | C |
| Electronic mass | $m_{e}=9.11 \times 10^{-31}$ | kg |
| Planck's constant | $h=4.14 \times 10^{-15}$ | eV.s |
| Speed of light | $c=3.00 \times 10^{8}$ | $\mathrm{~m} / \mathrm{s}$ |
| Boltzmann's constant | $K_{B}=8.62 \times 10^{-5}$ | $\mathrm{eV} / \mathrm{K}$ |
| Gas constant | $R=8.31$ | $\mathrm{~J} /(\mathrm{mole}-\mathrm{K})$ |
| Permittivity of free space | $\varepsilon_{0}=8.85 \times 10^{-12}$ | $\mathrm{C}^{2} /\left(\mathrm{N}-\mathrm{m}^{2}\right)$ |
| Permeability of free space | $\mu_{0}=4 \pi \times 10^{-7}$ | $\mathrm{~N} / \mathrm{A}^{2}$ |
| Stefan's constant | $\sigma=5.67 \times 10^{-8}$ | $\mathrm{~W} /\left(\mathrm{m}^{2} \mathrm{~K}^{4}\right)$ |
| Faraday's constant | $F=9.65 \times 10^{4}$ | $\mathrm{C} / \mathrm{mole}$ |
| Bohr's radius | $\mathrm{a}_{0}=0.53$ | $\AA$ |

## Appendix C: Useful Rules-of-Thumb

Molecular bonding distance $\approx 1-2 \AA$
Molecular strong single-bond energy $\approx$ few eV
Molecular vibration frequency $\approx 10^{13} / \mathrm{s}$
Ultimate tensile strength of strong materials $\approx \mathrm{GPa}$
Metals compressive strength $\approx$ tensile strength
Brittle materials compressive strength $\approx 15 \times$ tensile strength
Degradation activation energy $\approx 1 \mathrm{eV}$
Degradation rate $\approx 2 \times$ increase for each $10^{\circ} \mathrm{C}$ rise
Self-diffusion temperature in solids $T(K) \geq T(K)_{\text {melt }} / 2$
Electromigation-concern current density $(\mathrm{Al}, \mathrm{Cu}) \approx \mathrm{MA} / \mathrm{cm}^{2}$
Fusing-concern current density $(\mathrm{Al}, \mathrm{Cu}) \approx 20 \mathrm{MA} / \mathrm{cm}^{2}$
Silica dielectric breakdown strength $\approx 10 \mathrm{MV} / \mathrm{cm}$
Particle mean thermal-energy $(3 / 2)\left(\mathrm{K}_{\mathrm{n}} T\right)_{\oplus 300 \mathrm{~K}} \approx 0.04 \mathrm{eV}$
Phonon energy (near ground state) $\mathrm{h} v \approx 0.04 \mathrm{eV}$
Photon energy $(\mathrm{hc}) / \lambda \approx 1.24 \mathrm{eV}_{\oplus \lambda=1 \mu \mathrm{~m}}$
Rules-of-Thumb means that the value listed is only approximately correct and should be used only for rough-estimate type of calculations. The value listed is generally the correct order of magnitude# Appendix D: Useful Mathematical Expressions 

Some useful relations
$x^{a} x^{b}=x^{a+b}$
$\left(x^{a}\right)^{b}=x^{a b}$
$\exp (x) \exp (y)=\exp (x+y)$
$\ln (x y)=\ln (x)+\ln (y)$
$\ln (x / y)=\ln (x)-\ln (y)$
$\ln (x)=\ln (10) \log _{10}(x)$

$$
=2.3 \log _{10}(x)
$$

$\ln [\exp (x)]=x$
$\exp [\ln (x)]=x$
$\exp (0)=1$
$\exp (1)=2.71828$
$\exp (x)=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots$
$\ln (1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\cdots$
$(|x|<1)$

## Gradient

$\vec{\nabla} f=\widehat{i}\left(\frac{\partial f}{\partial x}\right)+\widehat{j}\left(\frac{\partial f}{\partial y}\right)+\widehat{k}\left(\frac{\partial f}{\partial z}\right)$

## Divergence theorem

$\int_{\text {volume } \mathrm{v}}(\vec{\nabla} \cdot \vec{A}) \mathrm{d} v=\int_{\text {area } \mathrm{a}} \vec{A} \cdot \mathrm{~d} \vec{a}$

## Stokes' theorem

$\int_{\text {area } \mathrm{a}}(\vec{\nabla} \times \vec{A}) \cdot \mathrm{d} \vec{a}=\int_{\text {line } 1} \vec{A} \cdot \mathrm{~d} \vec{l}$

Vectors
$\vec{A}=\hat{\vec{i}} A_{x}+\hat{\vec{j}} A_{y}+\hat{k} A_{z}$
$\vec{A} \cdot \vec{B}=A_{x} B_{x}+A_{y} B_{y}+A_{z} B_{z}$
$\vec{A} x \vec{B}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & \hat{k} \\ A_{x} & A_{y} & A_{z} \\ B_{x} & B_{y} & B_{z}\end{array}\right|$
$=\hat{i}\left[A_{x} B_{z}-A_{z} B_{x}\right]$
$+\hat{j}\left[A_{y} B_{x}-A_{x} B_{z}\right]$
$+\hat{k}\left[A_{x} B_{y}-A_{y} B_{x}\right]$
Divergence
$\vec{\nabla} \cdot \vec{A}=\frac{\partial A_{x}}{\partial x}+\frac{\partial A_{y}}{\partial y}+\frac{\partial A_{z}}{\partial z}$
Curl
$\vec{\nabla} \times \vec{A}=\left|\begin{array}{ccc}\hat{i} & \hat{j} & k \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_{x} & A_{y} & A_{z}\end{array}\right|$
$=\hat{i}\left[\frac{\partial A_{z}}{\partial y}-\frac{\partial A_{y}}{\partial z}\right]$
$+\hat{j}\left[\frac{\partial A_{x}}{\partial z}-\frac{\partial A_{z}}{\partial x}\right]$
$+\hat{k}\left[\frac{\partial A_{y}}{\partial x}-\frac{\partial A_{x}}{\partial y}\right]$# Appendix E: Useful Differentials and Definite Integrals 

Often used differentials
$\frac{\mathrm{d}}{\mathrm{d} x} x=1$
$\frac{\mathrm{d}}{\mathrm{d} x} c f(x)=c \frac{\mathrm{~d}}{\mathrm{~d} x} f(x)$
( $c$ is a constant)
$\frac{\mathrm{d}}{\mathrm{d} x} x^{m}=m x^{m-1}$
$\frac{\mathrm{d}}{\mathrm{d} x} \exp (x)=\exp (x)$
$\frac{\mathrm{d}}{\mathrm{d} x} \ln (x)=\frac{1}{x}$
$\frac{\mathrm{d}}{\mathrm{d} x} \ln (1+x)=\frac{1}{1+x}$
$\frac{\mathrm{d}}{\mathrm{d} x} \ln (1-x)=-\frac{1}{1-x}$
$\frac{\mathrm{d}}{\mathrm{d} x} \sin (x)=\cos (x)$
$\frac{\mathrm{d}}{\mathrm{d} x} \cos (x)=-\sin (x)$
$\frac{\mathrm{d}}{\mathrm{d} x}(f g)=g \frac{\mathrm{~d} f}{\mathrm{~d} x}+f \frac{\mathrm{~d} g}{\mathrm{~d} x}$

Often used definite integrals
$\int_{x 1}^{x 2} \mathrm{~d} x=x_{2}-x_{1}$
$\int_{x 2}^{x 1} c f(x) \mathrm{d} x=c \int_{x 1}^{x 2} f(x) \mathrm{d} x$
$\int_{x 1}^{x 2} x^{m} \mathrm{~d} x=\frac{1}{m+1}\left[x_{2}^{m+1}-x_{1}^{m+1}\right]$
(note: $m \neq-1$ )
$\int_{x 1}^{x 2} \exp (x) \mathrm{d} x=\exp \left(x_{2}\right)-\exp \left(x_{1}\right)$
$\int_{x 1}^{x 2} \frac{\mathrm{~d} x}{x}=\ln \left(x_{2}\right)-\ln \left(x_{1}\right)=\ln \left(x_{2} / x_{1}\right)$
$\int_{x 1}^{x 2} \frac{\mathrm{~d} x}{1+x}=\ln \left(\frac{1+x_{2}}{1+x_{1}}\right)$
$\int_{x 1}^{x 2} \frac{\mathrm{~d} x}{1-x}=\ln \left(\frac{1-x_{1}}{1-x_{2}}\right)$
$\int_{x 1}^{x 2} \sin (x) \mathrm{d} x=\cos \left(x_{1}\right)-\cos \left(x_{2}\right)$
$\int_{x 1}^{x 2} \cos (x) \mathrm{d} x=\sin \left(x_{2}\right)-\sin \left(x_{1}\right)$
$\int_{x 1}^{x 1} f(x) \mathrm{d} g(x)=f\left(x_{2}\right) g\left(x_{2}\right)$
$-f\left(x_{1}\right) g\left(x_{1}\right)$
$-\int_{x 1}^{x 2} g(x) \mathrm{d} f(x)$# Appendix F: Free-Energy 

## Potential Energy $\varphi$ Associated with Conservative Forces

If a potential energy $\varphi(x, y, z)$ is derived from a conservative force $f$, then $\mathrm{d} \varphi(x, y, z)$ is an exact differential:

$$
\begin{aligned}
\mathrm{d} \varphi(x, y, z) & =\left(\frac{\partial \varphi}{\partial x}\right)_{y, z} \mathrm{~d} x+\left(\frac{\partial \varphi}{\partial y}\right)_{x, z} \mathrm{~d} y+\left(\frac{\partial \varphi}{\partial x}\right)_{x, y} \mathrm{~d} z \\
& =-f_{x} \mathrm{~d} x-f_{y} \mathrm{~d} y-f_{z} \mathrm{~d} z \\
& =-\vec{f} \cdot \mathrm{~d} \vec{x}
\end{aligned}
$$

Note that in the equation above:

$$
f_{x}=-\left(\frac{\partial \varphi}{\partial x}\right)_{y, z} ; \quad f_{y}=-\left(\frac{\partial \varphi}{\partial y}\right)_{x, z} ; \quad f_{z}=-\left(\frac{\partial \varphi}{\partial z}\right)_{x, y}
$$

For conservative forces, the potential difference $\Delta \varphi$ in Eq. (F.1) depends only on the end points for the integration, not on the path selected between the end points. Thus, for conservative forces the closed-path integral must be equal to zero regardless of the path selected:

$$
\oint \mathrm{d} \varphi(x, y, x)=-\oint \vec{f} \cdot \mathrm{~d} \vec{x}=0
$$

## Internal Energy U of a Thermodynamic System

The internal energy $U$ of a system of particles is the sum of the potential and kinetic energies of all the particles in the system. The First Law of Thermodynamics tells us that the internal energy $U$ can be transformed/changed by heat flow and/or work, but the total energy must be conserved:

$$
\mathrm{d} U=\delta(\text { Heat })+\delta(\text { Work })
$$

The use of the symbol $\delta$ in Eq. (F.4) means that the quantities enclosed may not be exact differentials. ${ }^{1}$ Equation (F.4) states that the internal energy $U$ of a system of particles can be changed by: heat flowing into the system $(+)$ or out of the system $(-)$; and/or by doing work on the system $(+)$ or the system doing work $(-)$. Equation (F.4) can also be expressed as:

[^0]
[^0]:    ${ }^{1}$ Before Eq. (F.4) can be integrated, details of the heat-transfer process and details of how the work is to be performed must be given.$$
\begin{aligned}
\mathrm{d} U & =T \mathrm{~d} S+\sum_{i} F_{i} \mathrm{~d} x_{i} \\
& =T \mathrm{~d} S-p \mathrm{~d} V+\mu \mathrm{d} N+E \mathrm{~d} P+H \mathrm{~d} M+F \mathrm{~d} l+\mathrm{etc}
\end{aligned}
$$

Thus, we will postulate that the internal energy $U$ of a system of particles can be described by a set of thermodynamic extensive parameters ${ }^{2}$ : entropy $S$; volume $V$; mole number $N$, plus any system changes $\varepsilon$ (polarization $P$, magnetization $M$, elongation $l$, etc.) due to a external agent $\xi$ acting on the system. Because the external agent $\xi$ does work on the system, it can bring more local order to the system (increase in polarization, magnetization, elongation, etc.). However, the work done by $\xi$ on the system also increases the potential energy of the system. As discussed in Chap. 2, higher energy states are generally less stable and the system will look for ways of degrading to lower energy states.

Since energy must be conserved, then $U(S, V, N, \varepsilon)$ is expected to be an exact differential and we can express it as:

$$
\begin{aligned}
\mathrm{d} U(S, V, N, \varepsilon)= & \left(\frac{\partial U}{\partial S}\right)_{V, N, \varepsilon} \mathrm{~d} S+\left(\frac{\partial U}{\partial V}\right)_{S, N, \varepsilon} \mathrm{~d} V+\left(\frac{\partial U}{\partial N}\right)_{S, V, \varepsilon} \mathrm{~d} N \\
& +\left(\frac{\partial U}{\partial \varepsilon}\right)_{S, V, N} \mathrm{~d} \varepsilon \\
= & T \mathrm{~d} S-p \mathrm{~d} V+\mu \mathrm{d} N+\xi \mathrm{d} \varepsilon
\end{aligned}
$$

where

$$
T=\left(\frac{\partial U}{\partial S}\right)_{V, N, \varepsilon} ; \quad p=-\left(\frac{\partial U}{\partial V}\right)_{S, N, \varepsilon} ; \quad \mu=\left(\frac{\partial U}{\partial N}\right)_{S, V, \varepsilon} ; \quad \xi=\left(\frac{\partial U}{\partial \varepsilon}\right)_{S, V, N}
$$

# Helmholtz Potential (Free-Energy F) 

The Helmholtz Potential (Free-Energy $F$ ) is a defined thermodynamic potential:

$$
F=U-T S
$$

Differentiating, one obtains:

$$
\mathrm{d} F=\mathrm{d} U-T \mathrm{~d} S-S \mathrm{~d} T
$$

[^0]
[^0]:    ${ }^{2} \mathrm{~A}$ system parameter that depends on system size (for example mass) is referred to as extensive parameter. A system parameter that does not depend on system size (for example mass-density) is referred to as an intensive parameter.Substituting for $\mathrm{d} U$ [substituting Eq. (F.6) into Eq. (F.9)], gives:

$$
\mathrm{d} F(T, V, N, \varepsilon)=-S \mathrm{~d} T-p \mathrm{~d} V+\mu \mathrm{d} N+\xi \mathrm{d} \varepsilon
$$

Integrating Eq. (F.10), one obtains the change in Helmholtz Free Energy DF:

$$
\begin{aligned}
\Delta F & =F\left(T_{2}, V_{2}, N_{2}, \varepsilon_{2}\right)-F\left(T_{1}, V_{1}, N_{1}, \varepsilon_{1}\right) \\
& =-\int_{T_{1}}^{T_{2}} S \mathrm{~d} T-\int_{V_{1}}^{V_{2}} p \mathrm{~d} V+\int_{N_{1}}^{N_{2}} \mu \mathrm{~d} N+\int_{\varepsilon_{1}}^{\varepsilon_{2}} \xi \mathrm{~d} \varepsilon
\end{aligned}
$$

If the generalized external force $\xi$ acting on the system is a conservative force, then $F(T, V, N, \varepsilon)$ is an exact differential and can also be expressed as:

$$
\begin{aligned}
\mathrm{d} F(T, V, N, \varepsilon)= & \left(\frac{\partial F}{\partial T}\right)_{V, N, \varepsilon} \mathrm{~d} T+\left(\frac{\partial F}{\partial V}\right)_{T, N, \varepsilon} \mathrm{~d} V+\left(\frac{\partial F}{\partial N}\right)_{T, V, \varepsilon} \mathrm{~d} N \\
& +\left(\frac{\partial F}{\partial \varepsilon}\right)_{T, V, N} \mathrm{~d} \varepsilon
\end{aligned}
$$

Comparing Eq. (F.10) with Eq. (F.12), one obtains:

$$
S=-\left(\frac{\partial F}{\partial T}\right)_{V, N, \varepsilon} ; \quad p=-\left(\frac{\partial F}{\partial V}\right)_{T, N, \varepsilon} ; \quad \mu=\left(\frac{\partial F}{\partial N}\right)_{T, V, \varepsilon} ; \quad \xi=\left(\frac{\partial F}{\partial \varepsilon}\right)_{T, V, N}
$$

# Gibbs Potential (Free-Energy G) 

The Gibbs Potential (Free-Energy $G$ ) is a defined thermodynamic potential:

$$
G=U-T S+p V
$$

Differentiating, one obtains:

$$
\mathrm{d} G=\mathrm{d} U-T \mathrm{~d} S-S \mathrm{~d} T+p \mathrm{~d} V+V \mathrm{~d} p
$$

Substituting for $\mathrm{d} U$ [substituting Eq. (F.6) into Eq. (F.15)], gives:

$$
\mathrm{d} G(T, p, N, \varepsilon)=-S \mathrm{~d} T+V \mathrm{~d} p+\mu \mathrm{d} N+\xi \mathrm{d} \varepsilon
$$

Integrating Eq. (F.16), one obtains the change in Gibbs Free Energy $\Delta G$ :

$$
\begin{aligned}
\Delta G & =G\left(T_{2}, p_{2}, N_{2}, \varepsilon_{2}\right)-G\left(T_{1}, p_{1}, N_{1}, \varepsilon_{1}\right) \\
& =-\int_{T_{1}}^{T_{2}} S \mathrm{~d} T+\int_{p_{1}}^{p_{2}} V \mathrm{~d} p+\int_{N_{1}}^{N_{2}} \mu \mathrm{~d} N+\int_{\varepsilon_{1}}^{\varepsilon_{2}} \xi \mathrm{~d} \varepsilon
\end{aligned}
$$If the generalized external force $\xi$ acting on the system is a conservative force, then $G(T, p, N, \varepsilon)$ is an exact differential and can also be expressed as:

$$
\begin{aligned}
\mathrm{d} G(T, p, N, \varepsilon)= & \left(\frac{\partial G}{\partial T}\right)_{p, N, \varepsilon} \mathrm{~d} T+\left(\frac{\partial G}{\partial p}\right)_{T, N, \varepsilon} \mathrm{~d} p+\left(\frac{\partial G}{\partial N}\right)_{T, p, \varepsilon} \mathrm{~d} N \\
& +\left(\frac{\partial G}{\partial \varepsilon}\right)_{T, p, N} \mathrm{~d} \varepsilon
\end{aligned}
$$

Comparing Eq. (F.16) with Eq. (F.18), one obtains:

$$
S=-\left(\frac{\partial G}{\partial T}\right)_{p, N, \varepsilon} ; \quad V=\left(\frac{\partial G}{\partial p}\right)_{T, N, \varepsilon} ; \quad \mu=\left(\frac{\partial G}{\partial N}\right)_{T, p, \varepsilon} ; \quad \xi=\left(\frac{\partial G}{\partial \varepsilon}\right)_{T, p, N}
$$

Note that for constant pressure and constant volume system changes $\Delta F=\Delta G$.

# Properties of Thermodynamic Potentials 

Any one of the thermodynamic potentials $U(S, V, N, \varepsilon), F(T, V, N, \varepsilon)$ or $G(T, p, N, \varepsilon)$, when expressed in terms of their characteristic variables, provides a complete thermodynamic description of the system. These thermodynamic potentials, in addition to being exact differentials, are also homogeneous functions of degree one. As such, (using the Euler Theorem for homogeneous functions of degree one) these thermodynamic potentials can be written as:

$$
\begin{aligned}
U(S, V, N, \varepsilon) & =\left(\frac{\partial U}{\partial S}\right)_{V, N, \varepsilon} S+\left(\frac{\partial U}{\partial V}\right)_{S, N, \varepsilon} V+\left(\frac{\partial U}{\partial N}\right)_{S, V, \varepsilon} N+\left(\frac{\partial U}{\partial \varepsilon}\right)_{S, V, N} \varepsilon \\
& =T S-p V+\mu N+\xi \varepsilon
\end{aligned}
$$

Using Eq. (F.20), along with Eqs. (F.8) and (F.14), gives:

$$
F=U-T S=-p V+\mu N+\xi \varepsilon
$$

and

$$
G=U-T S+p V=\mu N+\xi \varepsilon
$$# Appendix G: $t(1-\alpha / 2, v)$ Distribution Values 

| Degrees of freedom $v$ | $\alpha$ (significance level) |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 0.01 | 0.02 | 0.05 | 0.1 | 0.2 | 0.4 | 0.6 | 0.8 | 1 |
|  | $1-\alpha / 2$ |  |  |  |  |  |  |  |  |
|  | 0.995 | 0.99 | 0.975 | 0.95 | 0.9 | 0.8 | 0.7 | 0.6 | 0.5 |
| 1 | 63.6567 | 31.8205 | 12.7062 | 6.3138 | 3.0777 | 1.3764 | 0.7265 | 0.3249 | 0.0000 |
| 2 | 9.9248 | 6.9646 | 4.3027 | 2.9200 | 1.8856 | 1.0607 | 0.6172 | 0.2887 | 0.0000 |
| 3 | 5.8409 | 4.5407 | 3.1824 | 2.3534 | 1.6377 | 0.9785 | 0.5844 | 0.2767 | 0.0000 |
| 4 | 4.6041 | 3.7469 | 2.7764 | 2.1318 | 1.5332 | 0.9410 | 0.5686 | 0.2707 | 0.0000 |
| 5 | 4.0321 | 3.3649 | 2.5706 | 2.0150 | 1.4759 | 0.9195 | 0.5594 | 0.2672 | 0.0000 |
| 6 | 3.7074 | 3.1427 | 2.4469 | 1.9432 | 1.4398 | 0.9057 | 0.5534 | 0.2648 | 0.0000 |
| 7 | 3.4995 | 2.9980 | 2.3646 | 1.8946 | 1.4149 | 0.8960 | 0.5491 | 0.2632 | 0.0000 |
| 8 | 3.3554 | 2.8965 | 2.3060 | 1.8595 | 1.3968 | 0.8889 | 0.5459 | 0.2619 | 0.0000 |
| 9 | 3.2498 | 2.8214 | 2.2622 | 1.8331 | 1.3830 | 0.8834 | 0.5435 | 0.2610 | 0.0000 |
| 10 | 3.1693 | 2.7638 | 2.2281 | 1.8125 | 1.3722 | 0.8791 | 0.5415 | 0.2602 | 0.0000 |
| 11 | 3.1058 | 2.7181 | 2.2010 | 1.7959 | 1.3634 | 0.8755 | 0.5399 | 0.2596 | 0.0000 |
| 12 | 3.0545 | 2.6810 | 2.1788 | 1.7823 | 1.3562 | 0.8726 | 0.5386 | 0.2590 | 0.0000 |
| 13 | 3.0123 | 2.6503 | 2.1604 | 1.7709 | 1.3502 | 0.8702 | 0.5375 | 0.2586 | 0.0000 |
| 14 | 2.9768 | 2.6245 | 2.1448 | 1.7613 | 1.3450 | 0.8681 | 0.5366 | 0.2582 | 0.0000 |
| 15 | 2.9467 | 2.6025 | 2.1314 | 1.7531 | 1.3406 | 0.8662 | 0.5357 | 0.2579 | 0.0000 |
| 16 | 2.9208 | 2.5835 | 2.1199 | 1.7459 | 1.3368 | 0.8647 | 0.5350 | 0.2576 | 0.0000 |
| 17 | 2.8982 | 2.5669 | 2.1098 | 1.7396 | 1.3334 | 0.8633 | 0.5344 | 0.2573 | 0.0000 |
| 18 | 2.8784 | 2.5524 | 2.1009 | 1.7341 | 1.3304 | 0.8620 | 0.5338 | 0.2571 | 0.0000 |
| 19 | 2.8609 | 2.5395 | 2.0930 | 1.7291 | 1.3277 | 0.8610 | 0.5333 | 0.2569 | 0.0000 |
| 20 | 2.8453 | 2.5280 | 2.0860 | 1.7247 | 1.3253 | 0.8600 | 0.5329 | 0.2567 | 0.0000 |
| 21 | 2.8314 | 2.5176 | 2.0796 | 1.7207 | 1.3232 | 0.8591 | 0.5325 | 0.2566 | 0.0000 |
| 22 | 2.8188 | 2.5083 | 2.0739 | 1.7171 | 1.3212 | 0.8583 | 0.5321 | 0.2564 | 0.0000 |
| 23 | 2.8073 | 2.4999 | 2.0687 | 1.7139 | 1.3195 | 0.8575 | 0.5317 | 0.2563 | 0.0000 |
| 24 | 2.7969 | 2.4922 | 2.0639 | 1.7109 | 1.3178 | 0.8569 | 0.5314 | 0.2562 | 0.0000 |
| 25 | 2.7874 | 2.4851 | 2.0595 | 1.7081 | 1.3163 | 0.8562 | 0.5312 | 0.2561 | 0.0000 |
| 26 | 2.7787 | 2.4786 | 2.0555 | 1.7056 | 1.3150 | 0.8557 | 0.5309 | 0.2560 | 0.0000 |
| 27 | 2.7707 | 2.4727 | 2.0518 | 1.7033 | 1.3137 | 0.8551 | 0.5306 | 0.2559 | 0.0000 |
| 28 | 2.7633 | 2.4671 | 2.0484 | 1.7011 | 1.3125 | 0.8546 | 0.5304 | 0.2558 | 0.0000 |
| 29 | 2.7564 | 2.4620 | 2.0452 | 1.6991 | 1.3114 | 0.8542 | 0.5302 | 0.2557 | 0.0000 |
| 30 | 2.7500 | 2.4573 | 2.0423 | 1.6973 | 1.3104 | 0.8538 | 0.5300 | 0.2556 | 0.0000 |
| 40 | 2.7045 | 2.4233 | 2.0211 | 1.6839 | 1.3031 | 0.8507 | 0.5286 | 0.2550 | 0.0000 |
| 50 | 2.6778 | 2.4033 | 2.0086 | 1.6759 | 1.2987 | 0.8489 | 0.5278 | 0.2547 | 0.0000 |
| 60 | 2.6603 | 2.3901 | 2.0003 | 1.6706 | 1.2958 | 0.8477 | 0.5272 | 0.2545 | 0.0000 |
| 70 | 2.6479 | 2.3808 | 1.9944 | 1.6669 | 1.2938 | 0.8468 | 0.5268 | 0.2543 | 0.0000 |
| 80 | 2.6387 | 2.3739 | 1.9901 | 1.6641 | 1.2922 | 0.8461 | 0.5265 | 0.2542 | 0.0000 |
| 90 | 2.6316 | 2.3685 | 1.9867 | 1.6620 | 1.2910 | 0.8456 | 0.5263 | 0.2541 | 0.0000 |
| 100 | 2.6259 | 2.3642 | 1.9840 | 1.6602 | 1.2901 | 0.8452 | 0.5261 | 0.2540 | 0.0000 |

In Excel: $t(1-\alpha / 2, v)=\operatorname{TINV}(\alpha, v)$Appendix H: Chi-Square $\chi^{2}(P, v)$ Distribution Values

| Degrees of freedom $v$ | $P$ (confidence level) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 0.995 | 0.99 | 0.975 | 0.95 | 0.9 | 0.8 | 0.6 | 0.4 | 0.2 | 0.1 | 0.05 | 0.025 | 0.010 | 0.005 |
| 1 | 7.88 | 6.63 | 5.02 | 3.84 | 2.71 | 1.64 | 0.71 | 0.27 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 10.60 | 9.21 | 7.38 | 5.99 | 4.61 | 3.22 | 1.83 | 1.02 | 0.45 | 0.21 | 0.10 | 0.05 | 0.02 | 0.01 |
| 3 | 12.84 | 11.34 | 9.35 | 7.81 | 6.25 | 4.64 | 2.95 | 1.87 | 1.01 | 0.58 | 0.35 | 0.22 | 0.11 | 0.07 |
| 4 | 14.86 | 13.28 | 11.14 | 9.49 | 7.78 | 5.99 | 4.04 | 2.75 | 1.65 | 1.06 | 0.71 | 0.48 | 0.30 | 0.21 |
| 5 | 16.75 | 15.09 | 12.83 | 11.07 | 9.24 | 7.29 | 5.13 | 3.66 | 2.34 | 1.61 | 1.15 | 0.83 | 0.55 | 0.41 |
| 6 | 18.55 | 16.81 | 14.45 | 12.59 | 10.64 | 8.56 | 6.21 | 4.57 | 3.07 | 2.20 | 1.64 | 1.21 | 0.87 | 0.68 |
| 7 | 20.28 | 18.48 | 16.01 | 14.07 | 12.02 | 9.80 | 7.28 | 5.49 | 3.82 | 2.83 | 2.17 | 1.69 | 1.24 | 0.99 |
| 8 | 21.95 | 20.09 | 17.53 | 15.51 | 13.36 | 11.03 | 8.35 | 6.42 | 4.59 | 3.49 | 2.73 | 2.18 | 1.65 | 1.34 |
| 9 | 23.59 | 21.67 | 19.02 | 16.92 | 14.68 | 12.24 | 9.41 | 7.36 | 5.38 | 4.17 | 3.33 | 2.70 | 2.09 | 1.73 |
| 10 | 25.19 | 23.21 | 20.48 | 18.31 | 15.99 | 13.44 | 10.47 | 8.30 | 6.18 | 4.87 | 3.94 | 3.25 | 2.56 | 2.16 |
| 11 | 26.76 | 24.72 | 21.92 | 19.68 | 17.28 | 14.63 | 11.53 | 9.24 | 6.99 | 5.58 | 4.57 | 3.82 | 3.05 | 2.60 |
| 12 | 28.30 | 26.22 | 23.34 | 21.03 | 18.55 | 15.81 | 12.58 | 10.18 | 7.81 | 6.30 | 5.23 | 4.40 | 3.57 | 3.07 |
| 13 | 29.82 | 27.69 | 24.74 | 22.36 | 19.81 | 16.98 | 13.64 | 11.13 | 8.63 | 7.04 | 5.89 | 5.01 | 4.11 | 3.57 |
| 14 | 31.32 | 29.14 | 26.12 | 23.68 | 21.06 | 18.15 | 14.69 | 12.08 | 9.47 | 7.79 | 6.57 | 5.63 | 4.66 | 4.07 |
| 15 | 32.80 | 30.58 | 27.49 | 25.00 | 22.31 | 19.31 | 15.73 | 13.03 | 10.31 | 8.55 | 7.26 | 6.26 | 5.23 | 4.60 |
| 16 | 34.27 | 32.00 | 28.85 | 26.30 | 23.54 | 20.47 | 16.78 | 13.98 | 11.15 | 9.31 | 7.96 | 6.91 | 5.81 | 5.14 |
| 17 | 35.72 | 33.41 | 30.19 | 27.59 | 24.77 | 21.61 | 17.82 | 14.94 | 12.00 | 10.09 | 8.67 | 7.56 | 6.41 | 5.70 |
| 18 | 37.16 | 34.81 | 31.53 | 28.87 | 25.99 | 22.76 | 18.87 | 15.89 | 12.86 | 10.86 | 9.39 | 8.23 | 7.01 | 6.26 |
| 19 | 38.58 | 36.19 | 32.85 | 30.14 | 27.20 | 23.90 | 19.91 | 16.85 | 13.72 | 11.65 | 10.12 | 8.91 | 7.63 | 6.84 |
| 20 | 40.00 | 37.57 | 34.17 | 31.41 | 28.41 | 25.04 | 20.95 | 17.81 | 14.58 | 12.44 | 10.85 | 9.59 | 8.26 | 7.43 |
| 21 | 41.40 | 38.93 | 35.48 | 32.67 | 29.62 | 26.17 | 21.99 | 18.77 | 15.44 | 13.24 | 11.59 | 10.28 | 8.90 | 8.03 ||  Degrees of freedom $v$ | $P$ (confidence level) |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | 0.995 | 0.99 | 0.975 | 0.95 | 0.9 | 0.8 | 0.6 | 0.4 | 0.2 | 0.1 | 0.05 | 0.025 | 0.010 | 0.005  |
|  22 | 42.80 | 40.29 | 36.78 | 33.92 | 30.81 | 27.30 | 23.03 | 19.73 | 16.31 | 14.04 | 12.34 | 10.98 | 9.54 | 8.64  |
|  23 | 44.18 | 41.64 | 38.08 | 35.17 | 32.01 | 28.43 | 24.07 | 20.69 | 17.19 | 14.85 | 13.09 | 11.69 | 10.20 | 9.26  |
|  24 | 45.56 | 42.98 | 39.36 | 36.42 | 33.20 | 29.55 | 25.11 | 21.65 | 18.06 | 15.66 | 13.85 | 12.40 | 10.86 | 9.89  |
|  25 | 46.93 | 44.31 | 40.65 | 37.65 | 34.38 | 30.68 | 26.14 | 22.62 | 18.94 | 16.47 | 14.61 | 13.12 | 11.52 | 10.52  |
|  26 | 48.29 | 45.64 | 41.92 | 38.89 | 35.56 | 31.79 | 27.18 | 23.58 | 19.82 | 17.29 | 15.38 | 13.84 | 12.20 | 11.16  |
|  27 | 49.64 | 46.96 | 43.19 | 40.11 | 36.74 | 32.91 | 28.21 | 24.54 | 20.70 | 18.11 | 16.15 | 14.57 | 12.88 | 11.81  |
|  28 | 50.99 | 48.28 | 44.46 | 41.34 | 37.92 | 34.03 | 29.25 | 25.51 | 21.59 | 18.94 | 16.93 | 15.31 | 13.56 | 12.46  |
|  29 | 52.34 | 49.59 | 45.72 | 42.56 | 39.09 | 35.14 | 30.28 | 26.48 | 22.48 | 19.77 | 17.71 | 16.05 | 14.26 | 13.12  |
|  30 | 53.67 | 50.89 | 46.98 | 43.77 | 40.26 | 36.25 | 31.32 | 27.44 | 23.36 | 20.60 | 18.49 | 16.79 | 14.95 | 13.79  |
|  40 | 66.77 | 63.69 | 59.34 | 55.76 | 51.81 | 47.27 | 41.62 | 37.13 | 32.34 | 29.05 | 26.51 | 24.43 | 22.16 | 20.71  |
|  50 | 79.49 | 76.15 | 71.42 | 67.50 | 63.17 | 58.16 | 51.89 | 46.86 | 41.45 | 37.69 | 34.76 | 32.36 | 29.71 | 27.99  |
|  60 | 91.95 | 88.38 | 83.30 | 79.08 | 74.40 | 68.97 | 62.13 | 56.62 | 50.64 | 46.46 | 43.19 | 40.48 | 37.48 | 35.53  |
|  70 | 104.21 | 100.43 | 95.02 | 90.53 | 85.53 | 79.71 | 72.36 | 66.40 | 59.90 | 55.33 | 51.74 | 48.76 | 45.44 | 43.28  |
|  80 | 116.32 | 112.33 | 106.63 | 101.88 | 96.58 | 90.41 | 82.57 | 76.19 | 69.21 | 64.28 | 60.39 | 57.15 | 53.54 | 51.17  |
|  90 | 128.30 | 124.12 | 118.14 | 113.15 | 107.57 | 101.05 | 92.76 | 85.99 | 78.56 | 73.29 | 69.13 | 65.65 | 61.75 | 59.20  |
|  100 | 140.17 | 135.81 | 129.56 | 124.34 | 118.50 | 111.67 | 102.95 | 95.81 | 87.95 | 82.36 | 77.93 | 74.22 | 70.06 | 67.33  |

In Excel: $\chi^{2}(P, v)=$ CHINV $(1-P, v)$# Index 

## A

Accelerated testing, 2, 125, 137, 138, 140-142, 144, 200, 256, 353, 438
uniform acceleration, 140, 142, 143
Acceleration factor, 2, 117, 130, 131, 137-147, 149-153, 157, 158, 162-164, 173, 193, 200, 201, 210, 211, 216, 218, 253, 254, 257, 274, 275, 277, 296, 307, 309, 311, 353, 438
Activation energy
enthalpy of activation, 132, 133, 195
free-energy of activation, 126, 128, $132-133$
internal energy of activation, 132
$\mathrm{Q}_{\text {bulk }}, 108,134,140,167$
$\mathrm{Q}_{\text {creep }}, 255,358-361$
$\mathrm{Q}_{\text {diffusion }}, 70$
$\mathrm{Q}_{\mathrm{EM}}, 355$
$\mathrm{Q}_{\mathrm{gb}}, 140,167$
$\mathrm{Q}_{\mathrm{HCI}}, 357$
$\mathrm{Q}_{\text {lattice-diffusion }}, 358$
$\mathrm{Q}_{\text {Mobile-ions }}, 358$
$\mathrm{Q}_{\mathrm{NBTI}}, 215,216$
$\mathrm{Q}_{\mathrm{SM}}, 251,281$
$\mathrm{Q}_{\text {TDDB }}, 355,356$
Adhesion failure, see Delamination
blistering (see Delamination)
buckling (see Delamination)
cracking (see Crack)
Al-alloy, 166-169, 171, 172, 174, 176, 178, $217,268,300,355,363$
Alkaline metal-ions, see Mobile-ions
Al-oxide, see Corrosion
Alpha particle, 29-31

Ambient, 175, 184, 185, 189, 218, 284, 287, 288, 302, 316, 381, 382, 390-395, $401,407-410,415$
Ambient corrosion, see Corrosion
Anode injection, see Time-dependent dielectric breakdown
Anode oxidation, see Corrosion
Asymmetrical potential, see Bonding potential
Attractive potential, see Bonding potential
Au ball-bond, 57, 82, 190
Average failure rate, see Failure rate

## B

Bamboo grain structure, see Electromigration
Barrier metal, see Electromigration
Basquin's Law, see Fatigue
Bathtub curve, see Failure rate
Bell-shaped curve, see Gaussian distribution
Binomial distribution, 424-427
probability, 424-425
sample size, 425-427
Bipolar current waveforms, see Electromigration
Black equation, see Electromigration
Blech effect, see Electromigration
Blistering, see Delamination
Bolt, 17, 19, 260-262, 273, 361, 364
Boltzmann, 26, 27, 70, 72, 126, 195, 207, 241
Bonding defects, 227
dangling bonds, 244, 245
dislocations, 241-244, 248
grain boundaries, 244-245, 248
point defect, 240
vacancies, 240-241, 248Bonding pad corrosion, see Corrosion
Bonding potential
asymmetrical potential, 278, 279
attractive potential, 227
bond breakage, 227, 237
bond energy, 230-232, 238
Born-Landé potential, 229
close-pack arrangement, 229
covalent, 196, 227, 229, 230
equilibrium position, 278
harmonic potential, 233
Harrison potential, 229
ionic bonding, 229
Lenard-Jones potential, 229
Mie-Grüneisen potential, 237, 238
quantum mechanics, 229, 279
repulsive potential, 227, 228
secondary bonds, 230, 231
single-bond energies, 230, 231, 234
strength/stability of bond, 230
Born-Landé potential, see Bonding potential
Breakdown distributions, 365-366, 372-375
Breakdown/rupture, 2, 154-162
Brittle materials, 192, 193, 243, 244, 249, 252, 265-269, 272, 278
Buckling, see Delamination
Bulk/lattice diffusion, see Diffusion
Burnin, see Failure rate

## C

Capability, see Gaussian distribution
Capacitor, 1, 13, 17, 19, 20, 33-35, 90, 97, $121,151,152,161,162,195,199$, 200, 218, 219, 246, 321, 325, 328, $368,369,371-375,378,397,441$
Cathode reduction, see Corrosion
Cathode voiding, see Electromigration
Cell phone, 21, 123, 125
Ceramics, 243, 249, 252
Charasteristic time $\mathrm{t}_{63}$, see Weibull distribution
Chemical mechanical polishing (CMP), 169, 185
Chemical potential, 11, 23, 71, 208, 295
Chi-square distribution
$\chi^{2}(\mathrm{P}, \nu)$ distribution values, 453-454
failure rates, 437-439
Chlorides and fluorides, see Corrosion
Circuit board, 391
Close-pack arrangement, see Bonding potential
CMP, see Chemical mechanical polishing (CMP)
Coffin-Manson Model, see Fatigue
Competing mechanisms, 50-51, 57, 178
Complementary model, 201-205

Compliance equation, 307, 310, 311, 316
Composite trapezoidal and Simpson's rule, see Numerical integration
Conduction, 197, 198, 229, 230, 295, 385, $407,410,411$
Confidence interval, 3, 419-441
Confined gas, 15, 17
Conservation of energy, 10, 332-335, 338, $339,382-385,397,412$
Conservative force, 14, 24, 29
Conservative TF model, 75-76
Constant load
creep rate, 250, 252-254
five-power-law, 358
fixed strain, 175, 177, 249, 258, 259
steady-state creep, 251
stress relaxation, 176, 177, 248, 249, 258-263, 361
Constant ramp rate, 150, 161, 164, 369
Constrained thermal expansion, see Thermo-mechanical stress
Convection, 355, 391, 407-411
Conversion, 74, 85, 95, 96, 98, 99, 238, 239, 305-329
Conversion factors, 238
Cooling agent, 383
Corrosion
Al-oxide, 168
ambient corrosion, 184, 185
anode, 184, 185, 195, 197, 198, 202, 205, 293, 295
bonding-pad corrosion, 183
cathode, 174, 184, 185, 195, 293, 295
cell, 184, 185, 293
chlorides, 183, 184, 187, 188, 293, 295
corrosion activity, 186, 245
corrosion failure, 183, 186, 285, 286
corrosion inhibitor, 186
corrosion product, 183, 185, 295
Cu-oxide, 168
dry oxidation, 285-292, 294
electrolyte, 184, 293
enhanced crack growth, 245, 266, 298
fluorides, 293, 295
humidity-induced oxidation, 294-296
internal-chip corrosion, 183
linear growth region, 287-288
logarithmic oxide-growth, 291-292
metal hydroxides, 292
oxidation reaction, 184, 287
oxide thickness, 53, 57, 64, 66, 195, 205, 287, 289, 290, 356
reduction reaction, 185, 213
residual chlorides, 183
standard electrode potentials, 293, 294time window, 183, 186, 189, 213, 296
wet corrosion, 184, 187, 292-294
Cost, 76, 144, 165, 353, 416
Covalent, see Bonding potential
$\mathrm{C}_{\mathrm{p}}$, see Gaussian distribution
$\mathrm{C}_{\mathrm{pk}}$, see Gaussian distribution
Crack
Gcrit, 268, 269
Griffith, 265, 269, 278
initiation, 192
pre-existing crack, 275-277
propagation, 1, 40, 70, 191, 192, 218, 227, 243-245, 249, 263, 266-269, 278, 298
stress concentration factor, 265, 268, 275, 300
stress raisers, 263-266
stress risers, 152, 153, 263-266, 358
tips, 152, 153, 263-267, 276, 298, 358
Creep, 1, 67, 73, 105, 133-135, 145, 146, 165, 175-178, 180, 181, 227, 241-243, 249-263, 280, 281, 299, 300, 326-328, $358-361,364$
Crushing strength, 243
Cumulative fraction, 82, 84, 94, 95, 98, 157, 372, 437
Current density, 1, 2, 70, 73, 79, 133, 135, 145, 156, 165, 166, 171-175, 195, 217, 294, $322,323,328,354,355,440$
Cycles-to-failure, see Fatigue
Cyclical stress, see Fatigue

## D

Damascene, 169
Dual, 169, 217
Dangling bonds, see Bonding defects
DC EM equivalents, see Electromigration
Debonding, see Delamination
Defect-free material, 5
Defective devices/materials, 3, 116, 117, 365, $419-425,439$
Defectivity, 428, 429, 440
Defect level, 3, 419, 420, 440
Degradation, 1, 2, 5-31, 33-69, 71, 93, 97, 114, 125-135, 152, 194, 196, 198, 199, 201-203, 207-209, 211-215, 227, 240, 248-250, 252, 271, 272, 278, 280, 305-310, 316, 331-352, 357-360, 362, $365,367,368,370-373,375-379,381$
Degradation rate, 2, 5, 15, 23, 24, 34, 42-47, 49, $50,53,56,63,68,69,97,125-132,134$, $135,173,174,195,214,252,305,381$
rate constant, $68,69,126,130$

Delamination
adhesion failure, 277-278
blistering, 243, 249, 283, 284, 288
buckling, 243, 248, 249, 281, 283, 288
cracking (see Crack)
de-bonding, 277
Device failure, 1-3, 34, 35, 39, 43, 59, 61, 63, $93,94,109-110,116,205,206,212$, 227, 249, 263, 266
Device-to-device variation, 138, 139, 170, 193, 195
Dielectric barrier, see Electroplating
Dielectric breakdown, 1, 134, 369, 371
Differentials and definite integrals, 446-447
Diffusion
activation energy for, $70,184,206,217,358$
bulk, 170
diffusion component, 70, 206
diffusivity, 70, 213
lattice (see Diffusion (bulk))
vibration/interaction frequency, 70
Diffusions/junctions, 391
Discrete distribution, 419, 420, 424
Dislocations, see Bonding defects
Dispersion parameter, see Gaussian distribution (standard deviation)
Dissimilar materials, 2, 50, 165, 190, 293
Dissipation, 19, 316, 338-348, 351, 355, $381-417$
Dissipative work, 22-23
Divergence theorem, 68, 386
Down-direction EM, see Electromigration
dpm, 419
Drift, 24, 70, 165-166, 170, 174, 205, 206, $212,213,354,357$
Driving force, 5, 9, 10, 70, 71, 126, 127, 250, 277, 278, 285, 288, 294, 336, 412, 413
Ductile materials, 191, 193, 251, 268, 269
Dynamical stresses
conversion of, 305-329
duty cycle, 319-324, 326-329
pulse, 308-318

## E

Early failure rate (EFR), see Failure rate
Edge dislocation, see Bonding defects
Effective thermal resistance, 390-395, 397-402, 406, 409, 411, 415, 416
Effective values
activation energy, 9, 27, 70-75, 77-80, 126-131, 134, 140, 145, 146, 156, 167, 170-172, 175, 177, 178, 181, 182, 184, 187, 188, 195-197, 206, 207, 210, 211,217, 219, 222, 250, 252, 253, 281, 285, 290, 299, 300, 318, 320, 321, 329, 332, $335,355,356,358$
dipole moment, 196, 204
static temperature, 316-318, 320, 321
$\mathrm{T}_{\text {effective }}, 316-318,320,329$
$\xi_{\text {effective }}, 305-316,319$
Einstein relation, 70, 213
Elastic behavior
elasticity, 67, 227
energy density, 235, 236
Hooke's Law, 232, 233
strain ratio, 282
stress ratio, 282
Electric fields, 1, 2, 11, 13, 18-20, 24, 78, 132-134, 145, 156, 165, 194-199, 201-208, 212, 213, 218, 219, 325, $355,356,368,372,373,437$
Electrolyte, see Corrosion (cell)
Electrolytic cell, see Corrosion
Electro-mechanical, 63
Electromigration
bamboo grain-structure, 70
barrier metal, 167, 174
bipolar current waveforms, 173
Black equation, 174
Blech effect, 170, 171
Blech length, 171, 217
cathode, 21, 166, 184, 185, 195, 197, 205, 293, 295
DC EM equivalents, 173
down-direction, 169, 170
electron wind, 166, 167, 354
reservoir effect, 174
shunting, 168, 178
sweep-back, 173
up-direction, 169, 170
via, 169
void-growth phase, 167
voiding, $1,50,57,67,68,166-171$, 174-176, 179-181, 223, 240, 248, 249, 262, 354
void-nucleation phase, 167, 174
W-plug via, 168
Electronegativity, see Pauling
Electroplating, 169
dielectric barrier, 169, 186, 296
EM, see Electromigration
E-Model, see Time-dependent dielectric breakdown
Energy conservation, 382-384, 397
Enthalpy, 11, 12, 132
Enthalpy of activation, see Activation energy

Entropy, 6-8, 10, 12, 26, 33, 34, 132, $411-414,416$
Entropy changes, 411-414, 416
Equilibrium position, see Bonding potential
Error function complement, 82, 83
Euler differential equation, 35, 396, 397
EXCEL, 84, 89, 95
Exclusion principle, see Pauli
Exothermic reactions, 381
Exponential model, 65, 72, 75, 76, 138, 140-142, 145, 188, 219, 302, 311, $313,315,316,373,376$
Extensive parameter, see Gibbs free energy
External energy, 383

## F

Failure mechanisms, 1-3, 70, 76, 79, 80, $93,100,103-105,114,139,165-219$, 227-302, 305, 321, 353, 357, 361, 362, 381
Failure models
integrated circuits, 1, 2, 116, 122, 140, 165-219, 290, 295, 362-364, 420
mechanical components, 1, 35, 121, 253, $258,260,325,327,358,359$
Failure probability, 97, 100
Failure rate
average failure rate, 110-113, 121-123, $437-439$
bathtub curve, 114-118, 120
burnin, 381, 382
EFR, 114-120
FIT, 111, 112, 114, 118
IFR, 114, 117-120
wear-out, 114, 115, 117-120, 122, 125, 134,140
Fatigue
Basquin's Law, 273
Coffin-Manson, 191-193, 272
CTF, 62, 121, 145, 191-194, 270, 272-274, 276, 277
cycles to failure, 62, 123, 145, 146, 190-194, 218, 270, 272-274, 276, 301, 440
cyclical stress, 62, 189, 192, 193, 270, 271, 273-276, 301, 305, 361
high-cycle fatigue, 191, 272-275
low-cycle fatigue, 191, 272
mean stress offset, 272-274
Fermi-level, 208
Fickian transport, 70
Fins, 393First Law of Thermodynamics, 382, 383
FIT, see Failure rate
Five-power law, see Creep
Flux divergence
accumulation, 67-69, 166, 167, 170, 191, 195, 205, 206, 357
voiding, 67, 68, 70, 166-168, 176, 262
Fourier's Law, 384-386, 412
Fowler-Nordheim, 197, 198
Fraction of defective, 422, 439
Free energy, 25, 27, 126-130, 132-133, 245, 277, 278, 285, 286, 294
Free-energy of activation, see Activation energy
Frenkel-Poole, see Poole-Frenkel
Frictional processes, 382
Full-width at half-maximum, 325

## G

Galvanic, 293
couple, 293, 294
Gaussian distribution
bell-shaped, 81
capability $\mathrm{C}_{\mathrm{p}}, 87,88$
capability index $\mathrm{C}_{\mathrm{pk}}, 87,88$
mean, 81
median, 81,82
normal distribution, 81-86
process control, 87-89
standard deviation, 81, 90
Z-value, 83-85, 89
Gcrit, see Crack
Generalized stress, 10, 11, 13, 14, 71, 125, 127, 128
Generation volume, 382, 387, 403
Geometric series, 342
Gibbs free energy
extensive parameter, 11
intensive parameter, 11
internal energy, 10, 11
Gibbs potential, 8, 10-26, 125-128, 336, 337
Gradients, 23, 24, 71, 166, 167, 175, 176, 179, 180, 240, 381, 382, 384, 385, 397, 412
Grain boundaries, see Bonding defects
Griffith, see Crack

## H

$\mathrm{H}^{+}$ions, 212, 213
Hard/brittle, 218, 284
Harmonic potential, see Bonding potential
Harrison potential, see Bonding potential

HCI, see Hot carrier injection
Heat
capacity, 382, 396, 399-402, 416
dissipation, 355, 382, 387-390, 393-396, 398
flow, 382-388, 390, 397, 412-414, 416
flux, 382, 384, 395
generation, 381-417
generation volume, 403
sink, 386-390, 393-397
transfer, 381-387, 394, 407-414
Helmholtz Free Energy, 449-450
Hooke's Law, see Elastic behavior
Hot carrier injection (HCI)
gate current, 209, 211
HCI, 207-211
substrate current, 209-211

## I

IC contacts, 174
Inelastic, see Plastic deformation
Infant mortality, 116
Injection, see Hot carrier injection
Instability, 10, 28, 29, 45, 212-216, 356
Instantaneous, 2, 15, 17, 19, 77, 109-111, $113-114,121-123,134$
Insulators, 165, 286
Integrated circuits (ICs), 1, 2, 116, 122, 140, 165-219, 290, 295, 296, 305, 356, 362-364, 391, 392, 415, 420, 421
Intensive parameter, see Gibbs free energy
Interconnect dielectrics, 178, 187, 198, 203, 204, 206
Interfaces, 165-170, 176, 180, 185, 187, 191, 192, 194, 205-209, 212-215, 244, 245, 277, 278, 281, 356, 357, 385
Interface-state generation, 1, 207
Intergrals and differentials, 383
Internal chip corrosion, see Corrosion
Internal energy, 10, 11, 15, 22, 25, 26, 132, 383
Internal energy of activation, see Activation energy
Intrinsic failure rate (IFR), see Failure rate
Ionic bonding, see Bonding potential
Ionic character, see Pauling

## J

Joule heating, 73, 145, 156, 173-175, 194, 195, 323, 382
Junction temperature, 391-394, 416## K

Kaplan-Meiers method, see Mixed multiple failure mechanisms
Kelvin temperature, 10, 70, 126
Kinetics, 1, 6, 10, 62-63, 72, 73, 125, 138, 139, 142, 143, 181, 207, 215, 216, 252, 255, 295, 383
Kinetic values, 71, 138, 139, 252, 255, 359
Kirkendall voiding, 50, 57

## $\mathbf{L}$

Large amplitude oscillations, 325, 331
Lattice, 24-28, 140, 165-167, 208, 230, 240-242, 244, 245, 248
Lattice/bulk diffusion, see Diffusion
Left of the screen, see Screening
Lenard-Jones potential, see Bonding potential
Life-support system, see Mission critical
Linear oxide growth rate, see Corrosion
Lithium-ion battery, 19, 21
Logarithmic oxide growth, see Corrosion
Lognormal distribution, 93-95, 97, 100, 104-106, 121, 123, 139, 142, 145, 146, 158, 159, 172, 187, 193, 252, 419, 431, 433-434, 440
logarithmic standard deviation $\sigma$ (see Lognormal distribution)
median time-to-failure $\mathrm{t}_{50}$ (see Lognormal distribution)
Lucky electron, see Hot carrier injection (HCI)

## $\mathbf{M}$

Maclaurin series, 34, 77, 80, 127, 128, 130
Madelung constant, 229
Materials/device degradation, see Degradation
Materials microstructure, 62, 71, 93
Materials strength, see Strength
Mathematical expressions, 446
Mean, see Gaussian distribution
Mean stress offset, see Fatigue
Mean-time between failures (MBTF), see Failure rate
Median, see Gaussian distribution
Metabolic processes, 382
Metal hydroxides, see Corrosion
Metal-ions, 67, 166, 167, 230, 287, 295
Metal-oxide $\left(\mathrm{M}_{\mathrm{x}} \mathrm{O}_{\mathrm{y}}\right)$ formation, see Corrosion
Metal-oxide-silicon field-effect transistors (MOSFETs), 1, 80, 134, 146, 194, 195, 203, 207-210, 212, 214, 216, 219, 286, $356,357,363,364$

Metal-pad/lead-frame, 391
Metals, 1, 2, 5, 6, 17, 40, 44, 45, 50, 53, 64, 67, $70,73,78,79,134,135,155,164-172$, 174-179, 184, 186, 191, 193, 195, 206, 217, 218, 229, 230, 239, 243, 244, 250, 252-254, 262, 263, 268-270, 272-274, 284-288, 292-302, 305, 327, 328, 354, 358, 362-364, 370, 376, 378, 387-391, 393, 399, 409-412, 415, 416, 440
Metastable, 5, 8, 9, 126, 250, 332, 334, 356, 414
Metastable states, 5, 8-10, 14, 15, 28, 29, 126, 128-130, 199, 332
Mie-Grüneisen potential, see Bonding potential
Mismatch in specific densities, 245
Mission critical, 109
Mission profile, 319-324, 327, 328
Mixed multiple failure distributions, 93, $103-105$
points of inflection, 103
Mobile-ions, 79, 146, 147, 205-207, 357, 358
Mobility, 70, 168, 178, 184, 185, 187, 205, 213, 295
Mode, see Gaussian distribution
Modulus, 15, 17, 230, 234-236, 247, 257, 261, 267, 280, 282, 283, 299, 301
spring constant, 233
stiffness constant, 233, 298
Moments, 196, 204, 273, 334
Momentum exchange, 165
Moore's law, 2, 165
Multimodal distributions, 93, 100-105

## $\mathbf{N}$

Native oxide, 170, 184, 186
Natural convection, 391
Natural/resonant frequency, 325, 331-338, 349, 350
NBTI, see Negative bias temperature instability (NBTI)
Negative-bias temperature instability (NBTI), 165, 212-216, 219, 356, 363
Normal distribution, see Gaussian distribution
Normal operating conditions, 117, 137, 139
Nuclear reaction, 31
Nuclide, 28-31
Numerical integration, 308, 312-316, 318

## 0

Oscillator, 325, 331, 332, 334, 336, 338-345
classical oscillator, 233
quantum oscillator, 233vibrational states, 279
zero-point energy, 233
Over-design, 144, 353
Oxidation reaction, see Corrosion
Oxide thickness, see Corrosion

## $\mathbf{P}$

Packaged IC, 391
Parabolic oxide-growth, 289-290
Parabolic potential, 334, 337-340, 343-346
Pauli, 29, 30, 228
exclusion principle, 29, 30, 228
Pauling, 229, 231
electronegativity (see Pauling)
ionic character (see Pauling)
PBTI, 212
postivite-bias temperature instability (see PBTI)
Peak gate current, see HCI
Periodic force, 336, 340
Periodic power, 403-407
Photovoltaic-induced voltage, 295
Physical constants, 445
Physics of failure, 76, 138-140, 156, 306
Pins, 391
Planck's constant, 445
Plastic deformation, 17, 175, 191, 193, 243, 259, 264, 266, 268, 271, 272, 297, 298
Plasticity, 227
Plastic molding compounds, 190
Plastic strain $\Delta \varepsilon_{\mathrm{pl}}, 272$
Point defect, see Bonding defects
Points of inflection, see Mixed multiple failure distribution
Poisson distribution
probability, 420-422
sample-size requirements, 422-425
Polarization, 10, 11, 13, 17, 20
Poole-Frenkel, 198
Post-screen, 372-374
Power-law models, 75
TF model, 74, 138, 143, 146, 307, 311, $312,314,369-378$
Pre-existing crack, see Crack
Probability, 84, 86, 87, 94, 97, 103, 104, 110, 126, 279, 419-421, 423-426, 432
Probability density function, 86-87, 94, 110

## Q

Q, see Activation energy
Qbulk, see Activation energy

Qcreep, see Activation energy
Qdiffusion, see Activation energy
QEM, see Activation energy
Qgb, see Activation energy
QHCI, see Activation energy
Qlattice-diffusion, see Activation energy
QMobile-Ions, see Activation energy
QNBTI, see Activation energy
QSM, see Activation energy
QTDDB, see Activation energy
Quantum mechanics, see Bonding potential
Quasi-static, 10, 14
Quench hardening, 416

## $\mathbf{R}$

Radiation, 410, 411
Ramp-rate, 150, 151, 156, 161, 164, 219, $301,367,368,378,379$
Ramp-to-breakdown, 149, 150, 154, 162, 206, 365, 372
Random events/processes, 419
Rapid/catastrophic failure, 269
Reaction rate, 68, 78, 126-130, 132, 133, 202, 287, 289-291
rate constant, 68, 78, 133, 202, 290, 291
Real stress, 133, 134, 175, 198
Rectangular stress-pulse equivalent, 312, 313
Relative humidity, 146, 184, 185, 187-189, 295, 296, 302
Reliability enhancement factor, 354
REF, 354-361
Reliability physics, 1, 2, 10, 13, 71, 84, 139
Reliability robustness, 353, 359
Repulsive potential, see Bonding potential
Resonance, 3, 325, 331-352
Resonance-induced degradation, 331-352
Resonant frequencies, 324-325
large amplitude oscillations, 325
Right of the screen, see Screening
Rules-of-thumb, 24
Rupture/fracture strength, see Strength

## $\mathbf{S}$

Safety factor, 2, 353
Sample size, 81, 83, 95, 103, 104, 111, $117,119,420,422-426,428-433$, $435,437-440$
Sampling plan, see Sampling theory
Sampling theory, 419, 426, 435
Screening
effectiveness, 372-379Screening (cont.)
left of the screen, 365-367, 370
nScreen, 365-370
right of the screen, 366-370
Using Exponential TF model, 309-310, 367-369, 373, 374
Using Power-Law TF model, 369-378
Secondary bonds, see Bonding potential
Second Law of Thermodynamics, 7, 11, 411, 412, 416
Self-consistent solution, 423, 424, 426, 427, 429
Self-heating, 73, 156, 175, 323, 355, 381-387
Semiconductors, 35, 37, 44, 49, 52, 56, 60, 63, $82,97,100,135,205,230,286$
Shear stress, 241-243, 299
Shell model, 29
Shunting current, see Barrier metal
Si-H bond, 208, 209, 212, 214, 215, 356
Silicon chips, 2, 57, 183, 218, 392, 421
Simple harmonic oscillator, 334
Simpson's rule, see Numerical integration
Single-bond energies, see Bonding potential
Sliding friction, 22, 332
SM, see Stress migration
Solar constant, 417
Specific density, 241, 244, 245
Specific heat, 22, 383-385, 396, 400, 416
Spring constant, see Modulus
Stability, 8, 10, 14-22, 28, 29, 126, 179, 208, 209, 212, 230, 243, 332
Standard deiviation, see Statistics
Standard electrode potential, see Corrosion
Statistical process control, see Gaussian statistics
Statistics, 3, 424, 428
Steady state creep, see Creep
Stefan's constant, 410
Stiffness constant, see Modulus
Stirling's approximation, 27
Storage tank, 17, 18
Strain-energy release rate, 266-267
Strain ratio, see Elastic behavior
Strength, 2, 16, 17, 19, 34, 50, 51, 57, 65, $77,78,87,90,116,117,134,140$, 149, 151, 153, 154, 157-159, 161, 170, 171, 203-205, 230, 235, 236, 239, 243, 246-249, 253, 257, 261, 269, 273, 274, 283, 300, 301, 337, $353,358,362,365-373,376-378$
Stress
real stress, 133, 134, 175, 198, 358
virtual stress, 133-135, 175, 198
Stress concentration factor, see Crack

Stress conditions, 75, 78, 129, 130, 137, 139-141, 144-147, 153, 172, 191, 214, 249-258, 270, 299
Stress-dependent activation energy, 77, 78, 80
Stress energy density ratio, see Elastic behavior
Stress-free temperature, 177, 181, 217
Stress gradients, 71, 175, 176, 179, 180, 240
Stress migration (SM), 175-183, 217, 240, 251, 281
Stress raiser/risers, see Crack
Stress range, 75, 144, 192, 193, 270-276, 324, 328, 362
Stress ratio, see Elastic behavior
Stress relaxation, 176, 177, 248, 249, 258-263, 361, 364
Stress relief, 175, 179, 180, 240, 248-249, 283, 284, 361
Student's t-distribtution, 431
$\mathrm{t}(1-\mathrm{a} / 2, \mathrm{~m})$ distribution values, 426
Substrate current, see HCI
Surface inversion, see Mobile ions
Surface mobility, 184
Surroundings/ambient, 382
Sweep-back, see Electromigration

## T

Taylor expansion, 34, 279
TDDB, see Time-dependent dielectric breakdown
t distribution values, 426
Temperature-fall portion, 403
Temperature rise, 22, 23, 73, 382, 389, 390, 394, 398, 399, 402-404, 406, 409, 411,415
Temperature-rise portion, 403
Tensile strength, 239, 243, 257, 273, 274, 301
Tensile stress, 1, 73, 74, 135, 145, 153, 163, 177, 178, 238, 240-243, 253, 256, 257, 260-267, 273-275, 277, 283, 284, 296, 298-301, 325, 362, 376
Thermal conductivity, 383-385, 387-389, 395
Thermal cycling, 189-194, 218, 281, 284, 302, 362-364, 440
Thermal equilibrium, 381, 382, 386, 387, 389, 398, 402, 407, 412, 416
Thermal expansion, 278-281, 283, 301, 362, 363
mismatch, 2, 190, 281-283, 362, 363
Thermal gradient, 381, 382, 412
Thermally conductive adhesive, 393
Thermal processes, see Boltzmann
Thermal relaxation, 398-401, 403, 404Thermal resistance, 384, 387, 389, 390, 407, $409,414-416$
$\theta_{\text {eff }}, 390,397,398,401,411$
Thermal rise, 401-407
Thermal time-constant, 397-406, 416
Thermo-mechanical stress, 1, 2, 176, 177, 189-193, 280, 281, 283, 362
Threshold voltage, 33-35, 37, 38, 44, 52, $61,63,134,213,356,357$
Time-averaged value, 69, 206
Time-dependent dielectric breakdown anode-injection, 197
complementary, 203
E-Model, 195-197, 199, 200, 202, 203
$\sqrt{2}$-model, 198, 199
1/E-model, 197-199, 202
Fowler-Nordheim conduction, 197, 198
$\mathrm{H}^{+}, 212,213$
power-law V-model, 203
trap-creation, 194
Time-dependent stresses, 3, 305
Time-to-failure, 2, 3, 43, 59-80, 93-107, 117, $121,122,125,133,134,138,139,141$, 151, 153, 154, 156-219, 227-302, 305, $306,308-310,319,323,353,354$, $367-369,373,376,378,419,431-441$
Time window, see Corrosion
Torque analysis, 334
Toughness, 246-248, 268, 269, 299
Trap creation, 194
Trapezoidal rule, see Numerical integration
Trim and form, 391

## $\mathbf{U}$

Uniform acceleration, see Accelerated testing
Units, 35, 72, 73, 75, 111, 141, 193, 234, 268, $279,280,309,310,313,369,379,384$, $389,420,422-426,429-431$
Uranium, 29, 31

## V

Vacancies, see Bonding defects
Vacancy, 25-27, 166, 179, 240-241, 248, 299
Vectors, 11, 240
Very high stress, 77, 78, 129-131, 252, 260
Vibrational/interaction frequency, see Diffusion
Virtual work, 332-334

## W

Warranty liability, 109
Weakest link, see Weibull distribution
Weak interfaces, see Delamination
Wear-out, see Failure rate
Weibits, 98, 99
Weibull distribution
characteristic time, 98, 104
weakest-link, 97, 114
Weibull slope, 97-99, 104, 105, 121-123, $142,143,154,155,161-164,219$, $276,300,301,435,436,441$
Work, 7-14, 16, 18, 20, 22, 23, 25, 29, 45, 54, $103,126,132,184,185,193,231,243$, $293,332,333,336,383,413,414$

## $\mathbf{Y}$

Yield, 36, 39, 49, 56, 152, 162-164, 175, 176, 180, 246, 249, 253, 257, 258, 261, 263-266, 299-301, 327, 351, 358-362, $364,366,369,372,379,420-422$
Yielding, 230, 239, 268, 347-351
Yield stress, 17, 152, 158, 248, 249, 264, 308, $309,358-360,362$
Young's modulus, see Modulus

## $\mathbf{Z}$

Zero-point energy, see Oscillator
Z-value, see Gaussian distribution