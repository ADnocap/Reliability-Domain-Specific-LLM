# Springer Series in Reliability Engineering 

## Hoang Pham

## System Software ReliabilitySpringer Series in Reliability Engineering# Series Editor 

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
Reliability and Optimal Maintenance
Hongzhou Wang and Hoang Pham# Hoang Pham 

## System Software Reliability

With 63 Figures# Hoang Pham, PhD <br> Department of Industrial Engineering <br> Rutgers, The State University of New Jersey <br> 96 Freylinghuysen Road <br> Piscataway, New Jersey 08854-8018 <br> USA 

British Library Cataloguing in Publication Data
Pham, Hoang
System software reliability. - (Springer series in
reliability engineering)
1.Systems software 2.Computer software - Reliability
I.Title
$005.4^{\prime} 3$
ISBN-10: 1852339500
Library of Congress Control Number: 2006924634
Springer Series in Reliability Engineering series ISSN 1614-7839
ISBN-10: 1-85233-950-0 e-ISBN 1-84628-295-0 Printed on acid-free paper
ISBN-13: 978-1-85233-950-0
© Springer-Verlag London Limited 2006
Apart from any fair dealing for the purposes of research or private study, or criticism or review, as permitted under the Copyright, Designs and Patents Act 1988, this publication may only be reproduced, stored or transmitted, in any form or by any means, with the prior permission in writing of the publishers, or in the case of reprographic reproduction in accordance with the terms of licences issued by the Copyright Licensing Agency. Enquiries concerning reproduction outside those terms should be sent to the publishers.

The use of registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant laws and regulations and therefore free for general use.

The publisher makes no representation, express or implied, with regard to the accuracy of the information contained in this book and cannot accept any legal responsibility or liability for any errors or omissions that may be made.

987654321
Springer Science+Business Media
springer.comTo my parents
Phong Pham and Tam Huynh, for many reasons.# Preface 

In today's technological world nearly everyone depends upon the continued functioning of a wide array of complex machinery and equipment for our everyday safety, security, mobility and economic welfare. We expect our electric appliances, hospital monitoring control, next-generation aircraft, data exchange systems, and aerospace applications to function wherever and whenever we need them. When they fail, the results can be catastrophic. As our society grows in complexity, so do the critical challenges in the area of system and software reliability engineering.

In general, system software reliability is the probability that the system will not fail for a specified period of time under specified conditions. The greatest problem facing the industry today is how to assess quantitatively system reliability characteristics.

The author published the book Software Reliability in 2000. Due to the critical challenges and complexity of modern embedded-software systems developed over the last five years, there has arisen an ever increasing attention of both public and professional communities to look for products with high reliability at reasonable costs. At the same time, the techniques, tools and models available in the last five years to system designers, engineers, and practitioners have continued to be developed by scientists and researchers at the same rate.

This book aims to present the state-of-the-art of system software reliability in theory and practice and recent research on this subject over the last five years. It is a textbook based mainly on the author's recent research and publications as well as experience of 20 years in this field. The topics covered are organized as follows.

Chapter 1 gives a brief introduction to system software reliability and basic terminologies used throughout the book. This chapter also identifies the literature available in the area of software reliability engineering. Chapter 2 discusses the concepts of system reliability engineering, systemability, various reliability aspects of systems with multiple failure modes, and the stochastic processes including the Markov process, renewal process, quasi-renewal process, and nonhomogeneous Poisson process.

Chapter 3 describes the theory of estimation, common estimation techniques and confidence interval estimates. Chapter 4 presents the basic concepts of software engineering assessment including software lifecycle, software developmentprocess and its applications, software testing concepts, and data analysis. Chapter 5 discusses various groups of traditional software reliability models and methods for evaluating software reliability and other performance measures, such as software complexity and the number of remaining errors.

Chapter 6 comprehensively covers software reliability models for the failure phenomenon based on the nonhomogeneous Poisson process (NHPP). The generalized NHPP model, model selection and the software mean time between failures are also discussed. Chapter 7 discusses various software reliability models addressing testing coverage and fault removal.

Chapter 8 describes some recent studies on environmental factors and the impact of these factors on software reliability assessment. Several software reliability models that incorporate environmental factors are also discussed. Chapter 9 discusses calibrating software reliability modelling research on how to quantify the mismatch between the system test environment and the field environment.

Chapter 10 discusses some software cost models based on the NHPP addressing warranty issues and risk costs due to software failures. This chapter also discusses a generalized gain model under random field environments. Various optimal release policies of the software systems, that is when to conclude testing and release the software, are also presented.

Chapter 11 is devoted to the basic concepts of fault-tolerant software system modeling and other advanced techniques including self-checking schemes. The reliability analysis of fault-tolerant software schemes such as recover block, N -version programming, and hybrid fault-tolerant systems are presented. This chapter also discusses a triple-version programming reliability model with common failures. A brief mathematical reliability analysis of complex systems considering hardware and software interaction failures is also discussed.

A list of references for further reading and problems are included at the end of each chapter. Solutions to selected problems are provided towards the end of the book. Appendix 1 contains various distribution tables. Appendix 2 contains some useful Laplace transform functions. Appendix 3 provides a survey form which software engineers may adopt in order to obtain a better understanding of the software development activities and priorities.

The text is suitable for a one-semester graduate course on software reliability in Industrial Engineering, Systems Engineering, Operations Research, Computer Science and Engineering, Mathematics, Statistics, and Business Management. The book will also be a valuable reference tool for practitioners and managers in reliability engineering, software engineering, statistics, safety engineering, and for researchers in the field. It is also intended that the individual, after having utilized this book, will be thoroughly prepared to pursue advanced studies in software reliability engineering and research in this field.

I have used the first seven chapters as supplementary reading for a three-day industrial seminar on system software reliability and, in addition, have included the material from Chapter 8 through 10 for a five-day seminar. These short sessions, three-day and five-day, serve as both an introduction and an account of advances in software reliability discipline, and can be easily tailored by the instructors to be specific for an industry or organization. Similarly, one can use the firstthree chapters, together with Chapter 6 and Chapter 11, for a two-day seminar on system reliability engineering.

I am grateful to the students of the Department of Industrial and Systems Engineering at Rutgers University who have used preliminary versions of this book during the past two years and have provided numerous comments and suggestions. Thanks also go to many colleagues from universities and industry for their useful suggestions.

Anthony Doyle, Senior Editor, and Kate Brown at Springer-Verlag deserve significant praise for their patience and understanding when deadlines were missed and for their assistance in finalizing the camera-ready version.

Finally and most importantly, I want to thank my other-half, Michelle, and my sons, Hoang Jr. and David, for their love, patience, understanding, and support. It is to them that this book is dedicated.

Hoang Pham
Rutgers University, New Jersey, USA
December 2005# Contents 

1 Introduction ..... 1
1.1 The Need for System Software Reliability ..... 1
1.2 Software-related Problems ..... 3
1.3 Software Reliability Engineering ..... 5
1.4 Future Problems in the Twenty-first Century ..... 5
1.5 Further Reading ..... 6
1.6 Problems ..... 7
2 System Reliability Concepts. ..... 9
2.1 Reliability Measures ..... 10
2.2 Common Distribution Functions ..... 16
2.3 A Generalized Systemability Function ..... 32
2.3.1 Systemability Definition. ..... 33
2.3.2 Systemability Calculations ..... 33
2.4 System Reliability with Multiple Failure Modes ..... 41
2.4.1 Reliability Calculations ..... 42
2.4.2 An Application of Systems with Multiple Failure Modes ..... 48
2.5 Markov Processes ..... 50
2.6 Counting Processes ..... 62
2.6.1 Poisson Processes ..... 63
2.6.2 Renewal Processes ..... 64
2.6.3 Quasi-renewal Processes ..... 66
2.6.4 Non-homogeneous Poisson Processes ..... 69
2.7 Further Reading ..... 71
2.8 Problems ..... 71
3 Theory of Estimation ..... 77
3.1 Point Estimation ..... 77
3.2 Maximum Likelihood Estimation Method ..... 79
3.3 Maximum Likelihood Estimation with Censored Data ..... 86
3.3.1 Parameter Estimate with Multiple-censored Data ..... 863.3.2 Confidence Intervals of Estimates ..... 88
3.3.3 Applications ..... 89
3.4 Statistical Change-point Estimation Methods ..... 91
3.4.1 Application: A Software Model with a Change Point ..... 95
3.5 Goodness of Fit Techniques ..... 96
3.5.1 Chi-squared Test ..... 96
3.5.2 Kolmogorov-Smirnov $d$ Test ..... 98
3.6 Least Squared Estimation ..... 98
3.7 Interval Estimation ..... 100
3.7.1 Confidence Intervals for the Normal Parameters ..... 100
3.7.2 Confidence Intervals for the Exponential Parameters ..... 102
3.7.3 Confidence Intervals for the Binomial Parameters ..... 104
3.7.4 Confidence Intervals for the Poisson Parameters ..... 106
3.8 Non-parametric Tolerance Limits ..... 106
3.9 Sequential Sampling ..... 107
3.10 Bayesian Methods ..... 113
3.11 Further Reading ..... 118
3.12 Problems ..... 119
4 Software Development Lifecycle and Data Analysis ..... 121
4.1 Introduction ..... 121
4.2 Software vs Hardware Reliability ..... 122
4.3 Software Reliability and Testing Concepts ..... 124
4.4 Software Lifecycle ..... 127
4.5 Software Development Process and its Applications ..... 132
4.5.1 Analytic Hierarchy Process ..... 133
4.5.2 Evaluation of Software Development Process ..... 133
4.6 Software Verification and Validation ..... 134
4.7 Data Analysis ..... 135
4.8 Failure Data Sets ..... 136
4.9 Further Reading ..... 150
4.10 Problems ..... 150
5 Software Reliability Modeling ..... 153
5.1 Introduction ..... 153
5.2 Halstead's Software Metric ..... 154
5.3 McCabe's Cyclomatic Complexity Metric ..... 157
5.4 Error Seeding Models ..... 159
5.5 Failure Rate Models ..... 164
5.6 Curve Fitting Models ..... 169
5.7 Reliability Growth Models ..... 171
5.8 Markov Structure Models ..... 172
5.9 Time Series Models ..... 174
5.10 Non-homogeneous Poisson Process Models ..... 175
5.11 Further Reading ..... 176
5.12 Problems ..... 1766 Imperfect-debugging Models ..... 179
6.1 Introduction ..... 179
6.2 Parameter Estimation ..... 180
6.3 Model Selection ..... 181
6.4 NHPP Exponential Models ..... 183
6.5 NHPP S-shaped Models ..... 188
6.6 NHPP Imperfect Debugging Models ..... 192
6.7 NHPP Imperfect Debugging S-shaped Models ..... 194
6.7.1 A Generalized Imperfect-debugging Fault-detection Model ..... 195
6.8 Applications ..... 203
6.9 Imperfect Debugging vs Perfect Debugging ..... 211
6.10 Mean Time Between Failures for NHPP ..... 213
6.11 Further Reading ..... 216
6.12 Problems ..... 216
7 Testing Coverage and Removal Models ..... 219
7.1 Introduction ..... 219
7.2 Testing Coverage Models ..... 219
7.3 Testing Coverage and Imperfect Debugging ..... 222
7.4 Fault Removal Efficiency Model ..... 224
7.5 Model Implementations ..... 231
7.6 Imperfect Debugging Model with Multiple Failure Types ..... 247
7.6.1 A Constant Fault Detection Rate ..... 248
7.6.2 Fault Detection Time-dependent Rate ..... 251
7.7 Further Reading ..... 255
7.8 Problems ..... 256
8 Software Reliability Models with Environmental Factors ..... 257
8.1 Introduction ..... 257
8.2 Data Analysis ..... 257
8.2.1 Survey Analysis ..... 258
8.2.2 Statistical Methods ..... 261
8.3 Exploratory Analysis of Environmental Factors ..... 263
8.4 Further Exploratory Analysis ..... 266
8.5 A Generalized Model with Environmental Factors ..... 272
8.6 Environmental Parameter Estimation ..... 275
8.7 Enhanced Proportional Hazard Jelinski-Moranda (EPJM) Model ..... 276
8.8 Applications ..... 279
8.9 Further Reading ..... 292
8.10 Problems ..... 292
9 Calibrating Software Reliability Models ..... 293
9.1 Introduction ..... 293
9.2 Calibration Factor Approach ..... 294
9.3 Model Application ..... 295
9.4 Calibrating Models with Random Field Environments ..... 296
9.4.1 A Generalized Random Field Environmental Model ..... 2989.4.2 RFE Reliability Models ..... 301
9.4.3 Applications ..... 303
9.5 Further Reading ..... 313
9.6 Problems ..... 313
10 Optimal Release Policies ..... 315
10.1 Introduction ..... 315
10.2 A Software Cost Model with Risk Factor ..... 316
10.3 Cost Model with Testing Coverage ..... 319
10.4 A Generalized Software Cost Model ..... 323
10.5 Cost Model with Multiple Failure Errors ..... 326
10.6 Gain Model with Random Field Environments ..... 332
10.6.1 Model Formulation ..... 334
10.6.2 Applications ..... 338
10.7 Other Cost Models ..... 342
10.8 Further Reading ..... 343
10.9 Problems ..... 343
11 Complex Fault-tolerant System Reliability Modeling ..... 347
11.1 Introduction ..... 347
11.2 Basic Fault-tolerant Software Techniques ..... 348
11.2.1 Recovery Block Scheme ..... 349
11.2.2 N-version Programming ..... 350
11.3 Other Advanced Techniques ..... 352
11.3.1 Self-checking Duplex Scheme ..... 352
11.3.2 Hybrid Fault-tolerant Scheme ..... 353
11.3.3 Reduction of Common-cause Failures ..... 355
11.4 Triple-version Programming Model with Common Failures ..... 357
11.4.1 Modeling Assumptions ..... 360
11.4.2 TVP Reliability Function ..... 364
11.4.3 Numerical Example ..... 366
11.5 Complex-system Reliability Modeling ..... 375
11.5.1 System Considerations ..... 375
11.5.2 Reliability Modeling ..... 377
11.6 Application Example ..... 383
11.7 Further Reading ..... 385
11.8 Problems ..... 386
Appendix 1: Distribution Tables ..... 389
Appendix 2: Laplace Transform ..... 395
Appendix 3: Survey of Factors that Affect Software Reliability ..... 399
References ..... 407
Glossary ..... 423
Solutions to Selected Problems ..... 429
Index ..... 437# Introduction 

### 1.1 The Need for System Software Reliability

Today, almost everyone in the world is directly or indirectly affected by computer systems. Computers are used in diverse areas for various applications including air traffic control, nuclear reactors, aircraft, real-time sensor networks, industrial process control, automotive mechanical and safety control, and hospital health care, affecting many millions of people.

An application of computer systems to the hospital health care is the monitoring of heart patients. In hospitals so equipped, sensors that detect electrical signals associated with heart activity are attached to the patient's heart area. The signals from these sensors are transmitted along wires to a computer programmed to analyze such data. If the incoming data indicate that the patient is doing well, the computer generated no output. If the data indicate the onset of serious conditions, the computer signals an alarm at the nursing station indicating which patient needs human care and the kind of help most apt to be useful.

As the functionality of computer operations becomes more essential and yet more complicated and critical applications increase in size and complexity, there is a great need for looking at ways to quantify and predict the reliability of computer systems in various complex operating environments (Pham 2005c). Faults, especially with logic, in software design thus become more subtle. Usually logic errors in the software are not hard to fix but diagnosing logic bugs is the most challenging for many reasons. The fault again is usually subtle.

Let us look at an example. A man wants to withdraw $\$ 50$ at an automatic transfer machine (ATM) from a checking account held jointly with his wife. Almost simultaneously, at another machine, his wife also begins the deposit of $\$ 500$. Both the husband's and the wife's ATM read the account balance of $\$ 100$ from the memory at the bank's central computer. While the first ATM (husband's machine) subtracts the withdrawal, the second ATM adds the deposit. Because withdrawals often take slightly longer to process than deposits, the wife's ATM records a new balance of $\$ 600$ before her husband's transaction is complete. His ATM, obviously not knowing that the old balance has been changed and in factincreased, records a wrong balance of $\$ 50$, instead of the new balance which should be $\$ 550$ !

Let us define the terms such as "software error", "fault" and "failure" (IEEE Std. 610.12,1990). An error is a mental mistake made by the programmer or designer. A fault is the manifestation of that error in the code. A software failure is defined as the occurrence of an incorrect output as a result of an input value that is received with respect to the specification. Figure 1.1 demonstrates how a software fault triggered by a specific input leads to software failure.


Figure 1.1. Relationship between software fault and software failure
A computer system consists of two major components: hardware and software. Although extensive research has been carried out on hardware reliability, the growing importance of recent software in complex applications dictates that the major focus has shifted to system software reliability and cost analysis. Software reliability is different from hardware reliability in the sense that software does not wear out or burn out. The software itself does not fail unless flaws within the software result in a failure in its dependent system.

In recent years, the cost of developing software and the penalty cost of software failure have become a major expense in the whole system (Pham 1992a). Failure of the software may result in an unintended system state or course of action. A loss event could ensue in which property is damaged or destroyed, people are injured or killed, and/or monetary costs are incurred. A quantitative measure of loss is called the risk cost of failure (Pham 1996). In other words, risk cost is a quantitative measure of the severity of loss resulting from a software failure. A research study has shown that professional programmers average six software defects for every 1000 lines of code (LOC) written. At that rate, a typical commercial software application of 350000 LOCs may contain over 2000 programming errors including memory-related errors, memory leaks, languagespecific errors, errors calling third-party libraries, extra compilation errors, standard library errors, etc.

As software projects become larger, the rate of software defects increases geometrically (see Figure 1.2). Table 1.1 shows the defect rates of several software applications per 100 LOC. Locating software faults is extremely difficult and costly. A study conducted by Microsoft showed that it takes about 12 programming hours to locate and correct a software defect. At this rate, it can take more than 24000 hours (or 11.4 man-years) to debug a program of 350000 LOC at a cost of over US $\$ 1$ million.

Figure 1.2. The rate of software defect changes

Table 1.1. Defect rates of several software applications

| Application | Number of systems | Fault density <br> (per 100 LOC) |
| :-- | :--: | :--: |
| Airborne | 8 | 1.28 |
| Strategic | 18 | 0.66 |
| Tactical | 6 | 1.00 |
| Process control | 2 | 0.18 |
| Production | 9 | 1.30 |
| Developmental | 2 | 0.40 |

# 1.2 Software-related Problems 

Software errors have caused spectacular failures, some with dire consequences, such as the following examples. On 31 March 1986, a Mexicana Airlines Boeing 727 airliner crashed into a mountain because the software system did not correctly negotiate the mountain position. Between March and June 1986, the massive Therac-25 radiation therapy machines in Marietta, Georgia; Boston, Massachusetts; and Tyler, Texas overdosed cancer patients due to flaws in the computer program controlling the highly automated devices. On 26 June 1988, Air France's new A320 model, just delivered two days before, crashed into the trees at an air show near Mulhouse in France due to computer software failure while performing a low-level pass. Three passengers were killed.

During the period 2-4 November 1988, a computer virus infected software at universities and defense research centers in the United States causing system failures. On 10 December 1990, Space Shuttle Columbia was forced to land early due to computer software problems. On 17 September 1991, a power outage at the AT\&T switching facility in New York City interrupted service to 10 million telephone users for 9 hours. The problem was due to the deletion of three bits ofcode in a software upgrade and failure to test the software before its installation in the public network.

The Patriot missile systems were built to intercept the Scud missiles but a bug in the Patriot software processing their clock times caused them to fail to intercept the target. The clocks were originally supposed to be reset frequently but as they were in one place for more than 100 hours the software failed, causing the missiles to miss their Scud targets. During the 1991 Gulf War this software problem resulted in the failure of the Patriot missile system to track an Iraqi Scud missile causing the deaths of 28 American soldiers. On 14 August 2003, a blackout that crippled most of the Northeast corridor of the United State and parts of Canada resulted from a software failure at FirstEnergy Corporation which may have contributed significantly to the outage.

In 1992, the London Ambulance service switched to a voice and computer control system which logged all its activities. However, when the traffic to the computer increased the software could not cope and slowed down; as a consequence it lost track of the ambulances. On 26 October 1992, the computer-aided dispatch system of the Ambulance Service in London, which handles more than 5000 requests daily in the transportation of patients in critical condition, failed after installation. This led to serious consequences for many critical patients.

A recent inquiry revealed that a software design error and insufficient software testing caused an explosion that ended the maiden flight of the European Space Agency's (ESA) Ariane 5 rocket, less than 40 seconds after lift-off on 4 June 1996. The problems occurred in the flight control system and were caused by a few lines of Ada code containing three unprotected variables. One of these variables pertained to the rocket launcher's horizontal velocity A problem occurred when the ESA used the software for the inertial-reference flight-control system in the Ariane 5, similar to the one used in the Ariane 4. The Ariane 5 has a high initial acceleration and a trajectory that leads to a horizontal velocity acceleration rate five times greater than that found in Ariane 4. Upon lift-off, the Ariane 5's horizontal velocity exceeded a limit that was set by the old software in the backup inertial-reference system's computer. This stopped the primary and backup inertial-reference system's computers, causing the rocket to veer off course and explode. The ESA report revealed that officials did not conduct a pre-flight test of the Ariane 5's inertial-reference system, which would have located the fault. The companies involved in this project had assumed that the same inertial-reference-system software would work in both Ariane 4 and Ariane 5. The ESA estimates that corrective measures will amount to US $\$ 362$ million (Pham 2000a).

Generally, software faults are more insidious and much more difficult to handle than physical defects. In theory, software can be error-free, and unlike hardware, does not degrade or wear out but it does deteriorate. The deterioration here, however, is not a function of time. Rather, it is a function of the results of changes made to the software during maintenance, through correcting latent defects, modifying the code to changing requirements and specifications, environments and applications, or improving software performance. All design faults are present from the time the software is installed in the computer. In principle, these faults could be removed completely, but in reality the goal ofperfect software remains elusive (Friedman and Voas 1995). Computer programs, which vary for fairly critical applications between hundreds and millions of lines of code, can make the wrong decision because the particular inputs that triggered the problem were not tested and corrected during the testing phase. Such inputs may even have been misunderstood or unanticipated by the designer who either correctly programmed the wrong interpretation or failed to identify the problem. These situations and other such events have made it apparent that we must determine the reliability of the software systems before putting them into operation.

# 1.3 Software Reliability Engineering 

Research on software reliability engineering has been conducted during the past three decades and numerous statistical models have been proposed for estimating software reliability (Pham 1999a, 2000a). Most existing models for pre- dicting software reliability are based purely on the observation of software product failures where they require a considerable amount of failure data to obtain an accurate reliability prediction. Some other research efforts recently have developed reliability models addressing fault coverage, testing coverage, and imperfect debugging processes.

In contrast, not many software practitioners, developers, or users utilize these models to evaluate software system reliability as they do not know how to select and apply them. A survey conducted in the late 1990s by the American Society for Quality reported that only $4 \%$ of the participants responded positively when asked if they could use a software reliability model.

Many researchers are currently pursuing the development of statistical models, based on nonhomogeneous Poisson process, semi quasi renewal, time series, that can be used to evaluate the reliability of real-world software systems. To develop an application-practice software reliability model and be able to make sound judgments when using the model, one needs to understand how software is produced and tested, the types of errors, and how errors are introduced. Environmental factors can help us justify the usefulness of the model and its applicability in a user environment. In other words, these models would be valuable if practitioners, software developers and users could use the information about the software development process, incorporating the environmental factors, thus giving greater confidence in estimates based on small numbers of failure data.

### 1.4 Future Problems in the Twenty-first Century

In the early 1970s, when computers were first used in the business world, storage space was at a premium and the use of a two-digit convention to represent the year seemed appropriate. For example, a date such as 20 April 1997 is typically represented in software as YY/MM/DD, or 97/04/20, and 1 January 2000 will look like 00/01/01 on our computers, but at that time, the year 2000 was a long way off.However, the time arrived, causing the year 2000 to be a major software concern of the twenty-first century. It was called the Year 2000 Problem, Y2K Problem or the Millennium Bug. The Year 2000 problem involved either or all of the following: (i) the year 2000 represented as a two-digit number causes failures in arithmetic, comparisons, and input/output to databases or files when manipulating date data, (ii) using an incorrect algorithm to recognize leap years for years divisible by 400, and (iii) system date data types that may roll over and fail due to the storage register becoming full.

Incorrect software programs will assume that the maximum value of a year field is "99" and will roll systems over to the year 1900 instead of 2000, resulting in negative date calculations and the creation of many overnight centenarians. Incorrect leap year calculations will therefore incorrectly assume that the year 2000 has only 365 days instead of 366 . The Year 2000 Problem was widespread several years ago. It indeed affected hardware, embedded firmware, languages and compilers, operating systems, nuclear power plants, air-traffic control, security services, database-management systems, communications systems, transaction processing systems, banking systems and medical services.

In 1997, United States federal officials estimated the cost of analysis and modification of the Year 2000 Problem to be US\$2 per line. As an estimated 15 billion lines of code have to be changed to cope with the problem, the work may cost up to US $\$ 30$ billion and the worldwide cost may be US $\$ 600$ billion. This estimate, however, reflects only conversion costs and may not include the cost of replacing hardware, testing and upgrading the systems.

The year 2000 was, however, not the only date dangerous to software applications. Over the next 50 years, at least 100 million applications around the world will need modification because of formatting problems with dates or related data. The total cost of the remedies in the United States could exceed US\$5 trillion. These problems include: the "nine" end-of-file, the global positioning system's date roll over; the social insecurity identity numbers, the date on which Unix and C libraries rollover and some date-like patterns used for data purposes. In the early twenty-first century, the nine digits assigned to the United States social security numbers and the ten digits allotted to long-distance telephone numbers will no longer suffice for American citizens and required phone lines, respectively. Changes to these numbering systems will also affect software. There is a solution to such problems but it will need a global agreement. A good starting point would be to examine all known date and data-like problems, and how computers and application software basically handle dates.

# 1.5 Further Reading 

There are numerous papers published on this subject - System Software Reliability - in the last three decades. This section only provides a brief list of recent papers, books, and reviewed papers published in the last 10 years. Interested readers are referred to recent reviewed articles by Pham (1999a, 2003b).

The book Software Reliability by Hoang Pham (Springer, 2000), Software-Reliability-Engineered Testing Practice by J. D. Musa (McGraw-Hill,New York, 1997), Software Assessment: Reliability, Safety, Testability by M.A. Friedman and J.M. Voas (Wiley, New York, 1995), are recent good textbooks for readers including students, practitioners and researchers.

The Handbook of Reliability Engineering edited by Hoang Pham (Springer, 2003), Handbook of Software Reliability Engineering edited by M. R. Lyu (IEEE Computer Society Press, Los Angeles, 1996), and Software Reliability and Testing by H. Pham (IEEE Computer Society Press, Los Angeles, 1995) are edited books containing many interesting results in which the readers may find useful.

Many research and tutorial papers on software reliability have been published in the IEEE Transactions on Software Engineering, IEEE Transactions on Reliability, and IEEE Software Magazine. Several special issues on software reliability are of practical interest:

Special issues of the International Journal of Reliability, Quality and Safety Engineering on Software Reliability, vol. 4(3), September 1997; on Software Reliability Model and Applications, vol. 6(l), March 1999; Special issue of the IEEE Computer on System Testing and Reliability, November, 1996

Several other journals occasionally publish papers on the subject:
Journal of Systems and Software
International Journal of Reliability, Quality and Safety Engineering
Reliability Engineering and System Safety Journal
Microelectronics and Reliability - An International Journal
IIE Transactions on Quality and Reliability Engineering.
There are also a great number of proceedings of international conferences where many interesting papers on software reliability and testing can be found, for example:

IEEE Annual Reliability and Maintainability Symposium
ISSAT International Conference on Reliability and Quality in Design
IEEE International Computer Software and Applications Conference
IEEE International Conference on Software Engineering
IEEE International Symposium on Software Reliability Engineering
This list is by no means exhaustive, but it will provide readers with a basic knowledge of software reliability.

# 1.6 Problems 

1. What is the difference between reliability and availability?
2. List the differences between hardware failures and software failures.
3. Provide examples of software failures, software defects and software faults.# System Reliability Concepts 

The analysis of the reliability of a system must be based on precisely defined concepts. Since it is readily accepted that a population of supposedly identical systems, operating under similar conditions, fall at different points in time, then a failure phenomenon can only be described in probabilistic terms. Thus, the fundamental definitions of reliability must depend on concepts from probability theory. This chapter describes the concepts of system reliability engineering. These concepts provide the basis for quantifying the reliability of a system. They allow precise comparisons between systems or provide a logical basis for improvement in a failure rate. Various examples reinforce the definitions as presented in Section 2.1. Section 2.2 examines common distribution functions useful in reliability engineering. Several distribution models are discussed and the resulting hazard functions are derived. Section 2.3 describes a new concept of systemability. Several systemability functions of various system configurations such as series, parallel, and k-out-of-n, are presented. Section 2.4 discusses various reliability aspects of systems with multiple failure modes. Stochastic processes including Markov process, Poisson process, renewal process, quasi-renewal process, and nonhomogeneous Poisson process are discussed in Sections 2.5 and 2.6.

In general, a system may be required to perform various functions, each of which may have a different reliability. In addition, at different times, the system may have a different probability of successfully performing the required function under stated conditions. The term failure means that the system is not capable of performing a function when required. The term capable used here is to define if the system is capable of performing the required function. However, the term capable is unclear and only various degrees of capability can be defined.# 2.1 Reliability Measures 

The reliability definitions given in the literature vary between different practitioners as well as researchers. The generally accepted definition is as follows.

Definition 2.1: Reliability is the probability of success or the probability that the system will perform its intended function under specified design limits.

More specific, reliability is the probability that a product or part will operate properly for a specified period of time (design life) under the design operating conditions (such as temperature, volt, etc.) without failure. In other words, reliability may be used as a measure of the system's success in providing its function properly. Reliability is one of the quality characteristics that consumers require from the manufacturer of products.

Mathematically, reliability $R(t)$ is the probability that a system will be successful in the interval from time 0 to time $t$ :

$$
R(t)=P(T>t) \quad t \geq 0
$$

where $T$ is a random variable denoting the time-to-failure or failure time.
Unreliability $F(t)$, a measure of failure, is defined as the probability that the system will fail by time $t$ :

$$
F(t)=P(T \leq t) \quad \text { for } t \geq 0
$$

In other words, $F(t)$ is the failure distribution function. If the time-to-failure random variable T has a density function $f(t)$, then

$$
R(t)=\int_{t}^{\infty} f(s) d s
$$

or, equivalently,

$$
f(t)=-\frac{d}{d t}[R(t)]
$$

The density function can be mathematically described in terms of $T$ :

$$
\lim _{\Delta t \rightarrow 0} P(t<T \leq t+\Delta t)
$$

This can be interpreted as the probability that the failure time $T$ will occur between the operating time $t$ and the next interval of operation, $t+\Delta t$.

Consider a new and successfully tested system that operates well when put into service at time $t=0$. The system becomes less likely to remain successful as the time interval increases. The probability of success for an infinite time interval, of course, is zero.

Thus, the system functions at a probability of one and eventually decreases to a probability of zero. Clearly, reliability is a function of mission time. For example, one can say that the reliability of the system is 0.995 for a mission time of 24 hours. However, a statement such as the reliability of the system is 0.995 is meaningless because the time interval is unknown.Example 2.1: A computer system has an exponential failure time density function

$$
f(t)=\frac{1}{9,000} e^{-\frac{t}{9,000}} \quad t \geq 0
$$

What is the probability that the system will fail after the warranty (six months or 4380 hours) and before the end of the first year (one year or 8760 hours)?

Solution: From equation (2.1) we obtain

$$
\begin{aligned}
P(4380<T \leq 8760)= & \int_{4380}^{8760} \frac{1}{9000} e^{-\frac{t}{9000}} d t \\
& =0.237
\end{aligned}
$$

This indicates that the probability of failure during the interval from six months to one year is $23.7 \%$.

If the time to failure is described by an exponential failure time density function, then

$$
f(t)=\frac{1}{\theta} e^{-\frac{t}{\theta}} \quad t \geq 0, \theta>0
$$

and this will lead to the reliability function

$$
R(t)=\int_{t}^{\infty} \frac{1}{\theta} e^{-\frac{x}{\theta}} d s=e^{-\frac{t}{\theta}} \quad t \geq 0
$$

Consider the Weibull distribution where the failure time density function is given by

$$
f(t)=\frac{\beta t^{\beta-1}}{\theta^{\beta}} e^{-\left(\frac{t}{\theta}\right)^{\beta}} \quad t \geq 0, \theta>0, \beta>0
$$

Then the reliability function is

$$
R(t)=e^{-\left(\frac{t}{\theta}\right)^{\theta}} \quad t \geq 0
$$

Thus, given a particular failure time density function or failure time distribution function, the reliability function can be obtained directly. Section 2.2 provides further insight for specific distributions.

# System Mean Time to Failure 

Suppose that the reliability function for a system is given by $R(t)$. The expected failure time during which a component is expected to perform successfully, or the system mean time to failure (MTTF), is given by

$$
M T T F=\int_{0}^{\infty} t f(t) d t
$$

Substituting

$$
f(t)=-\frac{d}{d t}[R(t)]
$$

into equation (2.4) and performing integration by parts, we obtain$$
\begin{aligned}
M T T F & =-\int_{0}^{\infty} t d[R(t)] \\
& =[-t R(t)] \stackrel{\infty}{ }_{0}+\int_{0}^{\infty} R(t) d t
\end{aligned}
$$

The first term on the right-hand side of equation (2.5) equals zero at both limits, since the system must fail after a finite amount of operating time. Therefore, we must have $t R(t) \rightarrow 0$ as $t \rightarrow \infty$. This leaves the second term, which equals

$$
M T T F=\int_{0}^{\infty} R(t) d t
$$

Thus, MTTF is the definite integral evaluation of the reliability function. In general, if $\lambda(t)$ is defined as the failure rate function, then, by definition, MTTF is not equal to $1 / \lambda(t)$.

The MTTF should be used when the failure time distribution function is specified because the reliability level implied by the MTTF depends on the underlying failure time distribution. Although the MTTF measure is one of the most widely used reliability calculations, it is also one of the most misused calculations. It has been misinterpreted as "guaranteed minimum lifetime". Consider the results as given in Table 2.1 for a twelve-component life duration test.

Table 2.1. Results of a twelve-component life duration test

| Component | Time to failure <br> (hours) |
| :--: | :--: |
| 1 | 4510 |
| 2 | 3690 |
| 3 | 3550 |
| 4 | 5280 |
| 5 | 2595 |
| 6 | 3690 |
| 7 | 920 |
| 8 | 3890 |
| 9 | 4320 |
| 10 | 4770 |
| 11 | 3955 |
| 12 | 2750 |

Using a basic averaging technique, the component MTTF of 3660 hours was estimated. However, one of the components failed after 920 hours. Therefore, it is important to note that the system MTTF denotes the average time to failure. It is neither the failure time that could be expected $50 \%$ of the time, nor is it the guaranteed minimum time of system failure.

A careful examination of equation (2.6) will show that two failure distributions can have the same MTTF and yet produce different reliability levels. This is illustrated in a case where the MTTFs are equal, but with normal and exponentialfailure distributions. The normal failure distribution is symmetrical about its mean, thus

$$
R(M T T F)=P(Z \geq 0)=0.5
$$

where Z is a standard normal random variable. When we compute for the exponential failure distribution using equation (2.3), recognizing that $\theta=$ MTTF, the reliability at the MTTF is

$$
R(M T T F)=e^{-\frac{M T T F}{M T T F}}=0.368
$$

Clearly, the reliability in the case of the exponential distribution is about $74 \%$ of that for the normal failure distribution with the same MTTF.

# Failure Rate Function 

The probability of a system failure in a given time interval $\left[t_{1}, t_{2}\right]$ can be expressed in terms of the reliability function as

$$
\begin{aligned}
\int_{t_{1}}^{t_{2}} f(t) d t & =\int_{t_{1}}^{\infty} f(t) d t-\int_{t_{2}}^{\infty} f(t) d t \\
& =R\left(t_{1}\right)-R\left(t_{2}\right)
\end{aligned}
$$

or in terms of the failure distribution function (or the unreliability function) as

$$
\begin{aligned}
\int_{t_{1}}^{t_{2}} f(t) d t & =\int_{-\infty}^{t_{2}} f(t) d t-\int_{-\infty}^{t_{1}} f(t) d t \\
& =F\left(t_{2}\right)-F\left(t_{1}\right)
\end{aligned}
$$

The rate at which failures occur in a certain time interval $\left[t_{1}, t_{2}\right]$ is called the failure rate. It is defined as the probability that a failure per unit time occurs in the interval, given that a failure has not occurred prior to $t_{1}$, the beginning of the interval. Thus, the failure rate is

$$
\frac{R\left(t_{1}\right)-R\left(t_{2}\right)}{\left(t_{2}-t_{1}\right) R\left(t_{1}\right)}
$$

Note that the failure rate is a function of time. If we redefine the interval as $[t, t+\Delta t]$, the above expression becomes

$$
\frac{R(t)-R(t+\Delta t)}{\Delta t R(t)}
$$

The rate in the above definitions is expressed as failures per unit time, when in reality, the time units might be in terms of miles, hours, etc. The hazard function is defined as the limit of the failure rate as the interval approaches zero. Thus, the hazard function $h(t)$ is the instantaneous failure rate, and is defined by

$$
\begin{aligned}
h(t) & =\lim _{\Delta t \rightarrow 0} \frac{R(t)-R(t+\Delta t)}{\Delta t R(t)} \\
& =\frac{1}{R(t)}\left[-\frac{d}{d t} R(t)\right] \\
& =\frac{f(t)}{R(t)}
\end{aligned}
$$The quantity $h(t) d t$ represents the probability that a device of age $t$ will fail in the small interval of time $t$ to $(t+d t)$. The importance of the hazard function is that it indicates the change in the failure rate over the life of a population of components by plotting their hazard functions on a single axis. For example, two designs may provide the same reliability at a specific point in time, but the failure rates up to this point in time can differ.

The death rate, in statistical theory, is analogous to the failure rate as the force of mortality is analogous to the hazard function. Therefore, the hazard function or hazard rate or failure rate function is the ratio of the probability density function (pdf) to the reliability function.

# Maintainability 

When a system fails to perform satisfactorily, repair is normally carried out to locate and correct the fault. The system is restored to operational effectiveness by making an adjustment or by replacing a component.

Maintainability is defined as the probability that a failed system will be restored to specified conditions within a given period of time when maintenance is performed according to prescribed procedures and resources. In other words, maintainability is the probability of isolating and repairing a fault in a system within a given time. Maintainability engineers must work with system designers to ensure that the system product can be maintained by the customer efficiently and cost effectively. This function requires the analysis of part removal, replacement, tear-down, and build-up of the product in order to determine the required time to carry out the operation, the necessary skill, the type of support equipment and the documentation.

Let $T$ denote the random variable of the time to repair or the total downtime. If the repair time $T$ has a repair time density function $g(t)$, then the maintainability, $V(t)$, is defined as the probability that the failed system will be back in service by time $t$, i.e.,

$$
V(t)=P(T \leq t)=\int_{0}^{t} g(s) d s
$$

For example, if $g(t)=\mu e^{-\mu t}$ where $\mu>0$ is a constant repair rate, then

$$
V(t)=1-e^{-\mu t}
$$

which represents the exponential form of the maintainability function.
An important measure often used in maintenance studies is the mean time to repair (MTTR) or the mean downtime. MTTR is the expected value of the random variable repair time, not failure time, and is given by

$$
M T T R=\int_{0}^{\infty} t g(t) d t
$$

When the distribution has a repair time density given by $g(t)=\mu e^{-\mu t}$, then, from the above equation, MTTR $=1 / \mu$. When the repair time $T$ has the log normal density function $g(t)$, and the density function is given by$$
g(t)=\frac{1}{\sqrt{2 \pi} \sigma t} e^{-\frac{(\ln t-\mu)^{2}}{2 \sigma^{2}}} \quad t>0
$$

then it can be shown that

$$
M T T R=m e^{\frac{\sigma^{2}}{2}}
$$

where $m$ denotes the median of the log normal distribution.
In order to design and manufacture a maintainable system, it is necessary to predict the MTTR for various fault conditions that could occur in the system. This is generally based on past experiences of designers and the expertise available to handle repair work.

The system repair time consists of two separate intervals: passive repair time and active repair time. Passive repair time is mainly determined by the time taken by service engineers to travel to the customer site. In many cases, the cost of travel time exceeds the cost of the actual repair. Active repair time is directly affected by the system design and is listed as follows:

1. The time between the occurrence of a failure and the system user becoming aware that it has occurred.
2. The time needed to detect a fault and isolate the replaceable component(s).
3. The time needed to replace the faulty component(s).
4. The time needed to verify that the fault has been corrected and the system is fully operational.
The active repair time can be improved significantly by designing the system in such a way that faults may be quickly detected and isolated. As more complex systems are designed, it becomes more difficult to isolate the faults.

# Availability 

Reliability is a measure that requires system success for an entire mission time. No failures or repairs are allowed. Space missions and aircraft flights are examples of systems where failures or repairs are not allowed. Availability is a measure that allows for a system to repair when failure occurs.

The availability of a system is defined as the probability that the system is successful at time $t$. Mathematically,

$$
\begin{aligned}
\text { Availability } & =\frac{\text { System up time }}{\text { System up time }+ \text { System down time }} \\
& =\frac{\text { MTTF }}{\text { MTTF }+ \text { MTTR }}
\end{aligned}
$$

Availability is a measure of success used primarily for repairable systems. For non-repairable systems, availability, $A(t)$, equals reliability, $R(t)$. In repairable systems, $A(t)$ will be equal to or greater than $R(t)$.

The mean time between failures (MTBF) is an important measure in repairable systems. This implies that the system has failed and has been repaired. Like MTTFand MTTR, MTBF is an expected value of the random variable time between failures. Mathematically,

$$
\mathrm{MTBF}=\mathrm{MTTF}+\mathrm{MTTR}
$$

The term MTBF has been widely misused. In practice, MTTR is much smaller than MTTF, which is approximately equal to MTBF. MTBF is often incorrectly substituted for MTTF, which applies to both repairable systems and non-repairable systems. If the MTTR can be reduced, availability will increase, and the system will be more economical.

A system where faults are rapidly diagnosed is more desirable than a system that has a lower failure rate but where the cause of a failure takes longer to detect, resulting in a lengthy system downtime. When the system being tested is renewed through maintenance and repairs, $E(T)$ is also known as MTBF.

# 2.2 Common Distribution Functions 

This section presents some of the common distribution functions and several hazard models that have applications in reliability engineering (Pham 2000a).

## Binomial Distribution

The binomial distribution is one of the most widely used discrete random variable distributions in reliability and quality inspection. It has applications in reliability engineering, e.g., when one is dealing with a situation in which an event is either a success or a failure.

The pdf of the distribution is given by

$$
\begin{gathered}
P(X=x)=\binom{n}{x} p^{x}(1-p)^{n-x} \quad x=0,1,2, \ldots, n \\
\binom{n}{x}=\frac{n!}{x!(n-x)!}
\end{gathered}
$$

where $n=$ number of trials; $x=$ number of successes; $p=$ single trial probability of success.

The reliability function, $R(k)$, (i.e., at least $k$ out of $n$ items are good) is given by

$$
R(k)=\sum_{x=k}^{n}\binom{n}{x} p^{x}(1-p)^{n-x}
$$

Example 2.2: Suppose in the production of lightbulbs, $90 \%$ are good. In a random sample of 20 lightbulbs, what is the probability of obtaining at least 18 good lightbulbs?

Solution: The probability of obtaining 18 or more good lightbulbs in the sample of 20 is$$
\begin{aligned}
R(18) & =\sum_{x=18}^{20}\binom{20}{18}(0.9)^{x}(0.1)^{20-x} \\
& =0.667
\end{aligned}
$$

# Poisson Distribution 

Although the Poisson distribution can be used in a manner similar to the binomial distribution, it is used to deal with events in which the sample size is unknown. This is also a discrete random variable distribution whose pdf is given by

$$
P(X=x)=\frac{(\lambda t)^{x} e^{-\lambda t}}{x!} \text { for } x=0,1,2, \ldots
$$

where $\lambda=$ constant failure rate, $x=$ is the number of events. In other words, $P(X=x)$ is the probability of exactly x failures occurring in time $t$. Therefore, the reliability Poisson distribution, $R(k)$ (the probability of k or fewer failures) is given by

$$
R(k)=\sum_{x=0}^{\lambda} \frac{(\lambda t)^{x} e^{-\lambda t}}{x!}
$$

This distribution can be used to determine the number of spares required for the reliability of standby redundant systems during a given mission.

## Exponential Distribution

Exponential distribution plays an essential role in reliability engineering because it has a constant failure rate. This distribution has been used to model the lifetime of electronic and electrical components and systems. This distribution is appropriate when a used component that has not failed is as good as a new component - a rather restrictive assumption. Therefore, it must be used diplomatically since numerous applications exist where the restriction of the memoryless property may not apply. For this distribution, we have reproduced equations (2.2) and (2.3), respectively:

$$
\begin{aligned}
& f(t)=\frac{1}{\theta} e^{-\frac{t}{\theta}}=\lambda e^{-\lambda t}, \quad t \geq 0 \\
& R(t)=e^{-\frac{t}{\theta}}=e^{-\lambda t}, \quad t \geq 0
\end{aligned}
$$

where $\theta=1 / \lambda>0$ is an MTTF's parameter and $\lambda \geq 0$ is a constant failure rate.
The hazard function or failure rate for the exponential density function is constant, i.e.,

$$
h(t)=\frac{f(t)}{R(t)}=\frac{\frac{1}{\theta} e^{-\frac{1}{\theta}}}{e^{-\frac{1}{\theta}}}=\frac{1}{\theta}=\lambda
$$

The failure rate for this distribution is $\lambda$, a constant, which is the main reason for this widely used distribution. Because of its constant failure rate property, the exponential is an excellent model for the long flat "intrinsic failure" portion of thebathtub curve. Since most parts and systems spend most of their lifetimes in this portion of the bathtub curve, this justifies frequent use of the exponential (when early failures or wear out is not a concern). The exponential model works well for inter-arrival times. When these events trigger failures, the exponential lifetime model can be used.

We will now discuss some properties of the exponential distribution that are useful in understanding its characteristics, when and where it can be applied.

Property 2.1: (Memoryless property) The exponential distribution is the only continuous distribution satisfying

$$
P\{T \geq t\}=P\{T \geq t+s \mid T \geq s\} \quad \text { for } t>0, s>0
$$

This result indicates that the conditional reliability function for the lifetime of a component that has survived to time $s$ is identical to that of a new component. This term is the so-called "used-as-good-as-new" assumption.

The lifetime of a fuse in an electrical distribution system may be assumed to have an exponential distribution. It will fail when there is a power surge causing the fuse to burn out. Assuming that the fuse does not undergo any degradation over time and that power surges that cause failure are likely to occur equally over time, then use of the exponential lifetime distribution is appropriate, and a used fuse that has not failed is as good as new.

Property 2.2: If $T_{1}, T_{2}, \ldots, T_{n}$, are independently and identically distributed exponential random variables (RVs) with a constant failure rate $\lambda$, then

$$
2 \lambda \sum_{i=1}^{n} T_{i} \sim \chi^{2}(2 n)
$$

where $\chi^{2}(2 n)$ is a chi-squared distribution with degrees of freedom $2 n$. This result is useful for establishing a confidence interval for $\lambda$.

Example 2.3: A manufacturer performs an operational life test on ceramic capacitors and finds they exhibit constant failure rate with a value of $3 \times 10^{-8}$ failure per hour. What is the reliability of a capacitor at $10^{4}$ hours?

Solution: The reliability of a capacitor at $10^{4}$ hour is

$$
R(t)=e^{-\lambda t}=e^{-3 \times 10^{-8} t}=e^{-3 \times 10^{-4}}=0.9997
$$

The resulting reliability plot is shown in Figure 2.1.

# Normal Distribution 

Normal distribution plays an important role in classical statistics owing to the Central Limit Theorem. In reliability engineering, the normal distribution primarily applies to measurements of product susceptibility and external stress. This twoparameter distribution is used to describe systems in which a failure results due to some wearout effect for many mechanical systems.

Figure 2.1. Reliability function vs time
The normal distribution takes the well-known bell shape. This distribution is symmetrical about the mean and the spread is measured by variance. The larger the value, the flatter the distribution. The pdf is given by

$$
f(t)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^{2}} \quad-\infty<t<\infty
$$

where $\mu$ is the mean value and $\sigma$ is the standard deviation. The cumulative distribution function (cdf) is

$$
F(t)=\int_{-\infty}^{t} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} d s
$$

The reliability function is

$$
R(t)=\int_{t}^{\infty} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} d s
$$

There is no closed form solution for the above equation. However, tables for the standard normal density function are readily available (see Table A1.1 in Appendix 1) and can be used to find probabilities for any normal distribution. If

$$
Z=\frac{T-\mu}{\sigma}
$$

is substituted into the normal pdf, we obtain

$$
f(z)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{z^{2}}{2}} \quad-\infty<Z<\infty
$$

This is a so-called standard normal pdf, with a mean value of 0 and a standard deviation of 1 . The standardized cdf is given by

$$
\Phi(t)=\int_{-\infty}^{t} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} s^{2}} d s
$$where $\Phi$ is a standard normal distribution function. Thus, for a normal random variable $T$, with mean $\mu$ and standard deviation $\sigma$,

$$
P(T \leq t)=P\left(Z \leq \frac{t-\mu}{\sigma}\right)=\Phi\left(\frac{t-\mu}{\sigma}\right)
$$

where $\Phi$ yields the relationship necessary if standard normal tables are to be used. The hazard function for a normal distribution is a monotonically increasing function of $t$. This can be easily shown by proving that $h^{\prime}(t) \geq 0$ for all $t$. Since

$$
h(t)=\frac{f(t)}{R(t)}
$$

then (see Problem 15)

$$
h^{\prime}(t)=\frac{R(t) f^{\prime}(t)+f^{2}(t)}{R^{2}(t)} \geq 0
$$

One can try this proof by employing the basic definition of a normal density function $f$.

Example 2.4: A component has a normal distribution of failure times with $\mu=$ 2000 hours and $\sigma=100$ hours. Find the reliability of the component and the hazard function at 1900 hours.

Solution: The reliability function is related to the standard normal deviate z by

$$
R(t)=P\left(Z>\frac{t-\mu}{\sigma}\right)
$$

where the distribution function for Z is given by equation (2.9). For this particular application,

$$
\begin{aligned}
R(1900) & =P\left(Z>\frac{1900-2000}{100}\right) \\
& =P(z>-1)
\end{aligned}
$$

From the standard normal table in Table A1.1 in Appendix 1, we obtain

$$
R(1900)=1-\Phi(-1)=0.8413
$$

The value of the hazard function is found from the relationship

$$
h(t)=\frac{f(t)}{R(t)}=\frac{\Phi\left(z=\frac{t-\mu}{\sigma}\right)}{\sigma R(t)}
$$

where $\phi$ is a pdf of standard normal density. Here

$$
\begin{aligned}
h(1900) & =\frac{\Phi(-1.0)}{\sigma R(t)}=\frac{0.1587}{100(0.8413)} \\
& =0.0019 \text { failures/cycle }
\end{aligned}
$$

Example 2.5: A part has a normal distribution of failure times with $\mu=40000$ cycles and $\sigma=2000$ cycles. Find the reliability of the part at 38000 cycles.Solution: The reliability at 38000 cycles

$$
\begin{aligned}
R(38000) & =P\left(z>\frac{38000-40000}{2000}\right) \\
& =P(z>-1.0) \\
& =\Phi(1.0)=0.8413
\end{aligned}
$$

The resulting reliability plot is shown in Figure 2.2.
The normal distribution is flexible enough to make it a very useful empirical model. It can be theoretically derived under assumptions matching many failure mechanisms. Some of these are corrosion, migration, crack growth, and in general, failures resulting from chemical reactions or processes. That does not mean that the normal is always the correct model for these mechanisms, but it does perhaps explain why it has been empirically successful in so many of these cases.

# Log Normal Distribution 

The log normal lifetime distribution is a very flexible model that can empirically fit many types of failure data. This distribution, with its applications in maintainability engineering, is able to model failure probabilities of repairable systems and to model the uncertainty in failure rate information. The log normal density function is given by

$$
f(t)=\frac{1}{\sigma t \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{\ln t-\mu}{\sigma}\right)^{2}} \quad t \geq 0
$$

where $\mu$ and $\sigma$ are parameters such that $-\infty<\mu<\infty$, and $\sigma>0$. Note that $\mu$ and $\sigma$ are not the mean and standard deviations of the distribution.

Reliability Curve


Figure 2.2. Normal reliability plot $v s$ timeThe relationship to the normal (just take natural logarithms of all the data and time points and you have "normal" data) makes it easy to work with many good software analysis programs available to treat normal data.

Mathematically, if a random variable $X$ is defined as $X=\ln T$, then X is normally distributed with a mean of $\mu$ and a variance of $\sigma^{2}$. That is,

$$
E(X)=E(\ln T)=\mu
$$

and

$$
V(X)=V(\ln T)=\sigma^{2}
$$

Since $T=e^{X}$, the mean of the log normal distribution can be found by using the normal distribution. Consider that

$$
E(T)=E\left(e^{X}\right)=\int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2 \pi}} e^{\int_{x-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} d x}
$$

and by rearrangement of the exponent, this integral becomes

$$
E(T)=e^{\mu+\frac{\sigma^{2}}{2}} \int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2 \sigma^{2}}\left[x-\left(\mu+\sigma^{2}\right)\right]^{2}} d x
$$

Thus, the mean of the log normal distribution is

$$
E(T)=e^{\mu+\frac{\sigma^{2}}{2}}
$$

Proceeding in a similar manner,

$$
E\left(T^{2}\right)=E\left(e^{2 X}\right)=e^{2\left(\mu+\sigma^{2}\right)}
$$

thus, the variance for the log normal is

$$
V(T)=e^{2 \mu+\sigma^{2}}\left(e^{\sigma^{2}}-1\right)
$$

The cumulative distribution function for the log normal is

$$
F(t)=\int_{0}^{t} \frac{1}{\sigma s \sqrt{2 \pi}} e^{-\frac{1}{2} \frac{\ln s-\mu}{\sigma} t^{2}} d s
$$

and this can be related to the standard normal deviate Z by

$$
\begin{aligned}
F(t)=P[T \leq t] & =P(\ln T \leq \ln t) \\
& =P\left[Z \leq \frac{\ln t-\mu}{\sigma}\right]
\end{aligned}
$$

Therefore, the reliability function is given by

$$
R(t)=P\left[Z>\frac{\ln t-\mu}{\sigma}\right]
$$

and the hazard function would be

$$
h(t)=\frac{f(t)}{R(t)}=\frac{\Phi\left(\frac{\ln t-\mu}{\sigma}\right)}{\sigma t R(t)}
$$

where $\Phi$ is a cdf of standard normal density.Example 2.6: The failure time of a certain component is log normal distributed with $\mu=5$ and $\sigma=1$. Find the reliability of the component and the hazard rate for a life of 50 time units.

Solution: Substituting the numerical values of $\mu, \sigma$, and $t$ into equation (2.12), we compute

$$
\begin{aligned}
R(50) & =P\left[Z>\frac{\ln 50-5}{1}\right]=P[Z>-1.09] \\
& =0.8621
\end{aligned}
$$

Similarly, the hazard function is given by

$$
h(50)=\frac{\Phi\left(\frac{\ln 50-5}{1}\right)}{50(1)(0.8621)}=0.032 \text { failures/unit. }
$$

Thus, values for the log normal distribution are easily computed by using the standard normal tables.

Example 2.7: The failure time of a part is log normal distributed with $\mu=6$ and $\sigma=$ 2. Find the part reliability for a life of 200 time units.

Solution: The reliability for the part of 200 time units is

$$
\begin{aligned}
R(200) & =P\left(Z>\frac{\ln 200-6}{2}\right)=P(Z>-0.35) \\
& =0.6368
\end{aligned}
$$

Reliability Curve


Figure 2.3. Log normal reliability plot $v s$ time

The log normal lifetime model, like the normal, is flexible enough to make it a very useful empirical model. Figure 2.3 shows the reliability of the log normal vs time. It can be theoretically derived under assumptions matching many failuremechanisms. Some of these are: corrosion and crack growth, and in general, failures resulting from chemical reactions or processes.

# Weibull Distribution 

The exponential distribution is often limited in applicability owing to the memoryless property. The Weibull distribution (Weibull 1951) is a generalization of the exponential distribution and is commonly used to represent fatigue life, ball bearing life, and vacuum tube life. The Weibull distribution is extremely flexible and appropriate for modeling component lifetimes with fluctuating hazard rate functions and for representing various types of engineering applications. The three-parameters probability density function is

$$
f(t)=\frac{\beta(t-\gamma)^{\beta-1}}{\theta^{\beta}} e^{-\left(\frac{t-\gamma}{\theta}\right)^{\beta}} \quad t \geq \gamma \geq 0
$$

where $\theta$ and $\beta$ are known as the scale and shape parameters, respectively, and $\gamma$ is known as the location parameter. These parameters are always positive. By using different parameters, this distribution can follow the exponential distribution, the normal distribution, etc. It is clear that, for $t \geq \gamma$, the reliability function $R(t)$ is

$$
R(t)=e^{-\left(\frac{t-\gamma}{\theta}\right)^{\beta}} \quad \text { for } t>\gamma>0, \beta>0, \theta>0
$$

hence,

$$
h(t)=\frac{\beta(t-\gamma)^{\beta-1}}{\theta^{\beta}} \quad t>\gamma>0, \beta>0, \theta>0
$$

It can be shown that the hazard function is decreasing for $\beta<1$, increasing for $\beta>1$, and constant when $\beta=1$.

Example 2.8: The failure time of a certain component has a Weibull distribution with $\beta=4, \theta=2000$, and $\gamma=1000$. Find the reliability of the component and the hazard rate for an operating time of 1500 hours.

Solution: A direct substitution into equation (2.13) yields

$$
R(1500)=e^{-\left(\frac{1500-1000}{2000}\right)^{4}}=0.996
$$

Using equation (2.14), the desired hazard function is given by

$$
\begin{aligned}
h(1500) & =\frac{4(1500-1000)^{4-1}}{(2000)^{4}} \\
& =3.13 \times 10^{-5} \text { failures/hour }
\end{aligned}
$$

Note that the Rayleigh and exponential distributions are special cases of the Weibull distribution at $\beta=2, \gamma=0$, and $\beta=1, \gamma=0$, respectively. For example, when $\beta=1$ and $\gamma=0$, the reliability of the Weibull distribution function in equation (2.13) reduces to

$$
R(t)=e^{-\frac{t}{\theta}}
$$and the hazard function given in equation (2.14) reduces to $1 / \theta$, a constant. Thus, the exponential is a special case of the Weibull distribution. Similarly, when $\gamma=0$ and $\beta=2$, the Weibull probability density function becomes the Rayleigh density function. That is

$$
f(t)=\frac{2}{\theta} t e^{-\frac{t^{2}}{\theta}} \quad \text { for } \theta>0, t \geq 0
$$

# Other Forms of Weibull Distributions 

The Weibull distribution again is widely used in engineering applications. It was originally proposed for representing the distribution of the breaking strength of materials. The Weibull model is very flexible and also has theoretical justification in many applications as a purely empirical model. Another form of Weibull probability density function is, for example,

$$
f(x)=\lambda \gamma x^{\gamma-1} e^{-\lambda t^{\gamma}}
$$

When $\gamma=2$, the density function becomes a Rayleigh distribution.
It can easily be shown that the mean, variance and reliability of the above Weibull distribution are, respectively, as follows:

$$
\begin{array}{ll}
\text { Mean } & =\lambda^{\frac{1}{\gamma}} \Gamma\left(1+\frac{1}{\gamma}\right) \\
\text { Variance } & =\lambda^{\frac{2}{\gamma}}\left(\Gamma\left(1+\frac{2}{\gamma}\right)-\left(\Gamma\left(1+\frac{1}{\gamma}\right)\right)^{2}\right) \\
\text { Reliability } & =e^{-\lambda t^{\gamma}}
\end{array}
$$

Example 2.9: The time to failure of a part has a Weibull distribution with $\frac{1}{\lambda}=250$ (measured in $10^{5}$ cycles ) and $\gamma=2$. Find the part reliability at $10^{6}$ cycles.

Solution: The part reliability at $10^{6}$ cycles is

$$
R\left(10^{6}\right)=e^{-(10)^{2} / 250}=0.6703
$$

The resulting reliability function is shown in Figure 2.4.

Figure 2.4. Weibull reliability function $v s$ time

# Gamma Distribution 

Gamma distribution can be used as a failure probability function for components whose distribution is skewed. The failure density function for a gamma distribution is

$$
f(t)=\frac{t^{\alpha-1}}{\beta^{\alpha} \Gamma(\alpha)} e^{-\frac{t}{\beta}} \quad t \geq 0, \alpha, \beta>0
$$

where $\alpha$ is the shape parameter and $\beta$ is the scale parameter. Hence,

$$
R(t)=\int_{t}^{\infty} \frac{1}{\beta^{\alpha}} \frac{1}{\Gamma(\alpha)} s^{\alpha-1} e^{-\frac{s}{\beta}} d s
$$

If $\alpha$ is an integer, it can be shown by successive integration by parts that

$$
R(t)=e^{-\frac{t}{\beta}} \sum_{i=0}^{\alpha-1} \frac{\left(\frac{t}{\beta}\right)^{i}}{i!}
$$

and

$$
h(t)=\frac{f(t)}{R(t)}=\frac{\frac{1}{\beta^{\alpha}} \frac{1}{\Gamma(\alpha)} t^{\alpha-1} e^{-\frac{t}{\beta}}}{e^{-\frac{t}{\beta}} \sum_{i=0}^{\alpha-1} \frac{\left(\frac{t}{\beta}\right)^{i}}{i!}}
$$

The gamma density function has shapes that are very similar to the Weibull distribution. At $\alpha=1$, the gamma distribution becomes the exponential distribution with the constant failure rate $1 / \beta$. The gamma distribution can also be used to model the time to the $n^{\text {th }}$ failure of a system if the underlying failure distribution is exponential. Thus, if $X_{i}$ is exponentially distributed with parameter $\theta=1 / \beta$, then $T=X_{1}+X_{2}+\ldots+X_{n}$, is gamma distributed with parameters $\beta$ and $n$.Example 2.10: The time to failure of a component has a gamma distribution with $\alpha$ $=3$ and $\beta=5$. Determine the reliability of the component and the hazard rate at 10 time-units.

Solution: Using equation (2.18), we compute

$$
R(10)=e^{-\frac{10}{5}} \sum_{i=0}^{2} \frac{\left(\frac{10}{5}\right)^{i}}{i!}=0.6767
$$

From equation (2.17), we obtain

$$
h(10)=\frac{f(10)}{R(10)}=\frac{0.054}{0.6767}=0.798 \text { failures/unit time }
$$

The other form of the gamma probability density function can be written as follows:

$$
f(x)=\frac{\beta^{\alpha} t^{\alpha-1}}{\Gamma(\alpha)} e^{-t \beta} \quad \text { for } t>0
$$

This pdf is characterized by two parameters: shape parameter $\alpha$ and scale parameter $\beta$. When $0<\alpha<1$, the failure rate monotonically decreases; when $\alpha>1$, the failure rate monotonically increase; when $\alpha=1$ the failure rate is constant.

The mean, variance and reliability of the density function in equation (2.19) are, respectively,

$$
\begin{array}{ll}
\text { Mean }(\text { MTTF }) & =\frac{\alpha}{\beta} \\
\text { Variance } & =\frac{\alpha}{\beta^{2}} \\
\text { Reliability } & =\int_{t}^{\infty} \frac{\beta^{\alpha} x^{\alpha-1}}{\Gamma(\alpha)} e^{-x \beta} d x
\end{array}
$$

Example 2.11: A mechanical system time to failure is gamma distribution with $\alpha=3$ and $1 / \beta=120$. Find the system reliability at 280 hours.

Solution: The system reliability at 280 hours is given by

$$
R(280)=e^{-\frac{280}{120}} \sum_{k=0}^{2} \frac{\left(\frac{280}{120}\right)^{2}}{k!}=0.85119
$$

and the resulting reliability plot is shown in Figure 2.5.
The gamma model is a flexible lifetime model that may offer a good fit to some sets of failure data. It is not, however, widely used as a lifetime distribution model for common failure mechanisms. A common use of the gamma lifetime model occurs in Bayesian reliability applications.

Figure 2.5. Gamma reliability function $v s$ time

# Beta Distribution 

The two-parameter Beta density function, $f(t)$, is given by

$$
f(t)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} t^{\alpha}(1-t)^{\beta} \quad 0<t<1, \alpha>0, \beta>0
$$

where $\alpha$ and $\beta$ are the distribution parameters. This two-parameter distribution is commonly used in many reliability engineering applications.

## Pareto Distribution

The Pareto distribution was originally developed to model income in a population. Phenomena such as city population size, stock price fluctuations, and personal incomes have distributions with very long right tails. The probability density function of the Pareto distribution is given by

$$
f(t)=\frac{\alpha k^{\alpha}}{t^{\alpha+1}} \quad k \leq t \leq \infty
$$

The mean, variance and reliability of the Pareto distribution are, respectively,

$$
\begin{array}{ll}
\text { Mean } & =k /(\alpha-1) \text { for } \alpha>1 \\
\text { Variance } & =\frac{\alpha K^{2}}{(\alpha-1)^{2}(\alpha-2)} \quad \text { for } \alpha>2 \\
\text { Reliability } & =\left(\frac{k}{t}\right)^{\alpha}
\end{array}
$$

The Pareto and log normal distributions have been commonly used to model the population size and economical incomes. The Pareto is used to fit the tail of the distribution, and the log normal is used to fit the rest of the distribution.# Rayleigh Distribution 

The Rayleigh function is a flexible lifetime distribution that can apply to many degra- dation process failure modes. The Rayleigh probability density function is

$$
f(t)=\frac{t}{\sigma^{2}} e^{\left(\frac{-t^{2}}{2 \sigma^{2}}\right)}
$$

The mean, variance, and reliability of Rayleigh function are, respectively,

$$
\begin{array}{ll}
\text { Mean } & =\sigma\left(\frac{\pi}{2}\right)^{\frac{1}{2}} \\
\text { Variance } & =\left(2-\frac{\pi}{2}\right) \sigma^{2} \\
\text { Reliability } & =e^{\frac{-\sigma t^{2}}{2}}
\end{array}
$$

Example 2.12: Rolling resistance is a measure of the energy lost by a tire under load when it resists the force opposing its direction of travel. In a typical car, traveling at 60 miles per hour, about $20 \%$ of the engine power is used to overcome the rolling resistance of the tires.

A tire manufacturer introduces a new material that, when added to the tire rubber compound, significantly improves the tire rolling resistance but increases the wear rate of the tire tread. Analysis of a laboratory test of 150 tires shows that the failure rate of the new tire linearly increases with time (hours). It is expressed as

$$
h(t)=0.5 \times 10^{-8} t
$$

Find the reliability of the tire at one year.
Solution: The reliability of the tire after one year ( 8760 hours) of use is

$$
R(1_{\text {year }})=e^{-\frac{0.5}{2} \times 10^{-8} \times(8760)^{2}}=0.8254
$$

Figure 2.6 shows the resulting reliability function.

Figure 2.6. Rayleigh reliability function $v s$ time

# Vtub-shaped Hazard Rate Distribution 

Pham (2002a) recently developed a two-parameter lifetime distribution with a Vtub-shaped hazard rate, called Pham distribution - also known as Loglog distribution.

Note that the loglog distribution with Vtub-shaped and Weibull distribution with bathtub-shaped failure rates are not the same. As for the bathtub-shaped, after the infant mortality period, the useful life of the system begins. During its useful life, the system fails as a constant rate. This period is then followed by a wear out period during which the system starts slowly and increases with the onset of wear out. For the Vtub-shaped, after the infant mortality period, the system starts to experience at a relatively low increasing rate, but this is not constant, and then increases with failures due to aging.

The Pham probability density function is given as follows (Pham 2002a):

$$
f(t)=\alpha \ln a t^{\alpha-1} a^{t^{\alpha}} e^{1-a^{t^{\alpha}}} \quad \text { for } t>0, a>0, \alpha>0
$$

The Pham distribution and reliability functions are

$$
F(t)=\int_{0}^{t} f(x) d x=1-e^{1-a^{t^{\alpha}}}
$$

and

$$
R(t)=e^{1-a^{t^{\alpha}}}
$$

respectively. The corresponding failure rate of the Pham distribution is given by

$$
h(t)=\alpha \ln (a) t^{\alpha-1} a^{t^{\alpha}}
$$

Figures 2.7 and 2.8 describe the density function and failure rate function for various values of $a$ and $\alpha$.

Figure 2.7. Probability density function for various values $\alpha$ with $\mathrm{a}=2$


Figure 2.8. Probability density function for various values a with $\alpha=1.5$

# Two-Parameter Hazard Rate Function 

This is a two-parameter function that can have increasing and decreasing hazard rates. The hazard rate, $h(t)$, the reliability function, $R(t)$, and the pdf are, respectively, given as follows

$$
\begin{gathered}
h(t)=\frac{n \lambda t^{n-1}}{\lambda t^{n}+1} \quad \text { for } n \geq 1, \lambda>0, t \geq 0 \\
R(t)=e^{-\ln \left(\lambda t^{N}+1\right)}
\end{gathered}
$$

and$$
f(t)=\frac{n \lambda t^{n-1}}{\lambda t^{n}+1} e^{-\ln \left(\lambda t^{n}+1\right)} \quad n \geq 1, \lambda>0, t \geq 0
$$

where $n=$ shape parameter; $\lambda=$ scale parameter

# Three-Parameter Hazard Rate Function 

This is a three-parameter distribution that can have increasing and decreasing hazard rates. The hazard rate, $h(t)$, is given as

$$
h(t)=\frac{\lambda(b+1)[\ln (\lambda t+\alpha)]^{b}}{(\lambda t+\alpha)} \quad b \geq 0, \lambda>0, \alpha \geq 0, t \geq 0
$$

The reliability function $R(t)$ for $\alpha=1$ is

$$
R(t)=e^{-\{\ln (\lambda t+\alpha)\}^{b+1}}
$$

The probability density function $f(t)$ is

$$
f(t)=e^{-\{\ln (\lambda t+\alpha)\}^{b+1}} \frac{\lambda(b+1)[\ln (\lambda t+\alpha)]^{b}}{(\lambda t+\alpha)}
$$

where $b=$ shape parameter, $\lambda=$ scale parameter, and $\alpha=$ location parameter.

### 2.3 A Generalized Systemability Function

The traditional reliability definitions and its calculations have commonly been carried out through the failure rate function within a controlled laboratory-test environment. In other words, such reliability functions are applied to the failure testing data and then utilized to make predictions on the reliability of the system used in the field. The underlying assumption for such calculation is that the field environments and the testing environments are the same.

By defintion, a mathematical reliability function is the probability that a system will be successful in the interval from time 0 to time $t$, given by

$$
R(t)=\int_{t}^{\infty} f(s) d s=e^{-\int_{0}^{t} h(s) d s}
$$

where $f(s)$ and $h(s)$ are, respectively, the failure time density and failure rate function.

The operating environments are, however, often unknown and yet different due to the uncertainties of environments in the field (Pham and Xie 2003). A new look at how reliability researchers can take account of the randomness of the field environments into mathematical reliability modeling covering system failure in the field is great interest.

Pham (2005a) recently developed a new mathematical function called systemability, considering the uncertainty of the operational environments in the function for predicting the reliability of systems.Notation
$h_{i}(t) \quad i^{\text {th }}$ component hazard rate function
$R_{i}(t) \quad i^{\text {th }}$ component reliability function
$\lambda_{i} \quad$ Intensity parameter of Weibull distribution for $i^{\text {th }}$ component
$\underline{\lambda} \quad \underline{\lambda}=\left(\lambda_{1}, \lambda_{2}, \lambda_{3} \ldots, \lambda_{n}\right)$.
$\gamma_{i} \quad$ Shape parameter of Weibull distribution for $i^{\text {th }}$ component
$\underline{\gamma} \quad \underline{\gamma}=\left(\gamma_{1}, \gamma_{2}, \gamma_{3} \ldots, \gamma_{n}\right)$.
$\eta \quad$ A common environment factor
$G(\eta) \quad$ Cumulative distribution function of $\eta$
$\alpha \quad$ Shape parameter of Gamma distribution
$\beta \quad$ Scale parameter of Gamma distribution

# 2.3.1 Systemability Definition 

This section discusses a definition of systemability function.
Definition 2.2 (Pham 2005a): Systemability is defined as the probability that the system will perform its intended function for a specified mission time under the random operational environments.

In a mathematical form, the systemabililty function is given by

$$
R_{s}(t)=\int_{\eta} e^{-\eta \int_{0}^{h(s) d s} d G(\eta)}
$$

where $\eta$ is a random variable that represents the system operational environments with a distribution function $G$.

This new function captures the uncertainty of complex operational environments of systems in terms of the system failure rate. It also would reflect the reliability estimation of the system in the field.

If we assume that $\eta$ has a gamma distribution with parameters $\alpha$ and $\beta$, i.e., $\eta \sim \operatorname{gamma}(\alpha, \beta)$ where the pdf of $\eta$ is given by

$$
f_{\eta}(x)=\frac{\beta^{\alpha} x^{\alpha-1} e^{-\beta x}}{\Gamma(\alpha)} \quad \text { for } \alpha, \beta>0 ; x \geq 0
$$

then the systemability function of the system in equation (2.30), using the Laplace transform (see Appendix 2), is given by

$$
R_{s}(t)=\left[\frac{\beta}{\beta+\int_{0}^{t} h(s) d s}\right]^{\alpha}
$$# 2.3.2 Systemability Calculations 

This subsection presents several systemability results and variances of some system configurations such as series, parallel, and $k$-out-of- $n$ systems (Pham 2005a). Consider the following assumptions:

1. A system consists of $n$ independent components where the system is subject to a random operational environment $\eta$.
2. $i^{\text {th }}$ component lifetime is assumed to follow the Weibull density function, i.e.

$$
\begin{aligned}
& \text { Component hazard rate } h_{i}(t)=\lambda_{i} \gamma_{i} t^{\gamma_{i}-1} \\
& \text { Component reliability } R_{i}(t)=e^{-\lambda_{i} t^{\gamma_{i}}} \quad \mathrm{t}>0
\end{aligned}
$$

Given common environment factor $\eta \sim \operatorname{gamma}(\alpha, \beta)$, the systemability functions for different system structures can be obtained as follows.

## Series System Configuration

In a series system, all components must operate successfully if the system is to function. The conditional reliability function of series systems subject to an actual operational random environment $\eta$ is given by

$$
R_{\text {Series }}(t \mid \eta, \underline{\lambda}, \gamma)=e^{\left(-\eta \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}\right)}
$$

The series systemability is given as follows

$$
R_{\text {Series }}(t \mid \underline{\lambda}, \gamma)=\int_{\eta} \exp \left(-\eta \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}\right) d G(\eta)=\left[\frac{\beta}{\beta+\sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}}\right]^{\alpha}
$$

The variance of a general function $R(t)$ is given by

$$
\operatorname{Var}[R(t)]=E\left[R^{2}(t)\right]-(E[R(t)])^{2}
$$

Given $\eta \sim \operatorname{gamma}(\alpha, \beta)$, the variance of systemability for any system structure can be easily obtained. Therefore, the variance of series systemability is given by

$$
\begin{aligned}
\operatorname{Var}\left[R_{\text {Series }}(t \mid \underline{\lambda}, \gamma)\right]= & \int_{\eta} \exp \left(-\eta\left(2 \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}\right)\right) d G(\eta)- \\
& \left(\int_{\eta} \exp \left(-\eta \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}\right) d G(\eta)\right)^{2}
\end{aligned}
$$

or

$$
\operatorname{Var}\left[R_{\text {Series }}(t \mid \underline{\lambda}, \gamma)\right]=\left[\frac{\beta}{\beta+2 \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}}\right]^{\alpha}-\left[\frac{\beta}{\beta+\sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}}\right]^{2 \alpha}
$$# Parallel System Configuration 

A parallel system is a system that is not considered to have failed unless all components have failed. The conditional reliability function of parallel systems subject to the uncertainty operational environment $\eta$ is given by

$$
\begin{aligned}
& R_{\text {Parallel }}(t \mid \eta, \underline{\lambda}, \underline{\gamma})=\exp \left(-\eta \lambda_{i} t^{\gamma_{i}}\right)-\sum_{\substack{i_{1}, i_{2}=1 \\
i_{1} \neq i_{2}}}^{n} \exp \left(-\eta\left(\lambda_{i_{1}} t^{\gamma_{i_{1}}}+\lambda_{i_{2}} t^{\gamma_{i_{2}}}\right)\right)+ \\
& \sum_{\substack{i_{1}, i_{2}, i_{1}=1 \\
i_{1} \neq i_{2} \neq i_{2}}}^{n} \exp \left(-\eta\left(\lambda_{i_{1}} t^{\gamma_{i_{1}}}+\lambda_{i_{2}} t^{\gamma_{i_{2}}}+\lambda_{i_{1}} t^{\gamma_{i_{1}}}\right)\right)- \\
& \ldots \\
& +(-1)^{n-1} \exp \left(-\eta \sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}\right)
\end{aligned}
$$

Hence, the parallel systemability is given by

$$
\begin{aligned}
& R_{\text {parallel }}(t \mid \underline{\lambda}, \underline{\gamma})=\sum_{i=1}^{n}\left[\frac{\beta}{\beta+\lambda_{i} t^{\gamma_{i}}}\right]^{\alpha}-\sum_{\substack{i_{1}, i_{2}=1 \\
i_{1} \neq i_{2}}}^{n}\left[\frac{\beta}{\beta+\lambda_{i_{1}} t^{\gamma_{i_{1}}}+\lambda_{i_{2}} t^{\gamma_{i_{2}}}}\right]^{\alpha}+ \\
& \sum_{\substack{i_{1}, i_{2}, i_{2}=1 \\
i_{1} \neq i_{2} \neq i_{2}}}^{n}\left[\frac{\beta}{\beta+\lambda_{i_{1}} t^{\gamma_{i_{1}}}+\lambda_{i_{2}} t^{\gamma_{i_{2}}}+\lambda_{i_{1}} t^{\gamma_{i_{1}}}}\right]^{\alpha}- \\
& \ldots \\
& +(-1)^{n-1}\left[\frac{\beta}{\beta+\sum_{i=1}^{n} \lambda_{i} t^{\gamma_{i}}}\right]^{\alpha}
\end{aligned}
$$

or

$$
\mathrm{R}_{\text {parallel }}(t \mid \underline{\lambda}, \underline{\gamma})=\sum_{k=1}^{n}(-1)^{k-1} \sum_{\substack{i_{1}, i_{2} \ldots, i_{k}=1 \\
i_{1} \neq i_{2} \ldots \neq i_{k}}}^{n}\left[\frac{\beta}{\beta+\sum_{j=i_{1} \ldots i_{k}} \lambda_{j} t^{\gamma_{j}}}\right]^{\alpha}
$$

To simplify the calculation of a general n-component parallel system, we only consider here a parallel system consisting of two components. It is easy to see that the second-order moments of the systemability function can be written as

$$
\begin{aligned}
& E\left[\mathrm{R}_{\text {Parallel }}^{2}(t \mid \underline{\lambda}, \underline{\gamma})\right]=\int_{\eta}\left(e^{-2 \eta \lambda_{1} t^{\gamma_{1}}}+e^{-2 \eta \lambda_{2} t^{\gamma_{2}}}+\mathrm{e}^{-2 \eta\left(\lambda_{1} t^{\gamma_{1}}+\lambda_{2} t^{\gamma_{2}}\right)}\right. \\
& \left.\quad+\mathrm{e}^{-\eta\left(\lambda_{1} t^{\gamma_{1}}+\lambda_{2} t^{\gamma_{2}}\right)}-e^{-\eta\left(2 \lambda_{1} t^{\gamma_{1}}+\lambda_{2} t^{\gamma_{2}}\right)}-\mathrm{e}^{-\eta\left(\lambda_{1} t^{\gamma_{1}}+2 \lambda_{2} t^{\gamma_{2}}\right)}\right) d G(\eta)
\end{aligned}
$$The variance of series systemability of a two-component parallel system is given by

$$
\begin{aligned}
& \operatorname{Var}\left[R_{\text {Parallel }}(t \mid \underline{\lambda}, \underline{\gamma})\right]=\left[\frac{\beta}{\beta+2 \lambda_{1} t^{T_{1}}}\right]^{\alpha}+\left[\frac{\beta}{\beta+2 \lambda_{2} t^{T_{2}}}\right]^{\alpha}+ \\
& {\left[\frac{\beta}{\beta+2 \lambda_{1} t^{T_{1}}+2 \lambda_{2} t^{T_{2}}}\right]^{\alpha}+\left[\frac{\beta}{\beta+\lambda_{1} t^{T_{1}}+\lambda_{2} t^{T_{2}}}\right]^{\alpha}-} \\
& {\left[\frac{\beta}{\beta+2 \lambda_{1} t^{T_{1}}+\lambda_{2} t^{T_{2}}}\right]^{\alpha}-\left[\frac{\beta}{\beta+\lambda_{1} t^{T_{1}}+2 \lambda_{2} t^{T_{2}}}\right]^{\alpha}-} \\
& {\left[\left[\frac{\beta}{\beta+\lambda_{1} t^{T_{1}}}\right]^{\alpha}+\left[\frac{\beta}{\beta+\lambda_{2} t^{T_{2}}}\right]^{\alpha}-\left[\frac{\beta}{\beta+\lambda_{1} t^{T_{1}}+\lambda_{2} t^{T_{2}}}\right]^{\alpha}\right]^{2}}
\end{aligned}
$$

# $\boldsymbol{k}$-out-of- $\boldsymbol{n}$ System Configuration 

In a $k$-out-of- $n$ configuration, the system will operate if at least k out of n components are operating. To simplify the complexity of the systemability function, we assume that all the components in the $k$-out-of- $n$ systems are identical. Therefore, for a given common environment $\eta$, the conditional reliability function of a component is given by

$$
R(t \mid \eta, \lambda, \gamma)=e^{-\eta \lambda t^{T}}
$$

The conditional reliability function of $k$-out-of- $n$ systems subject to the uncertainty operational environment $\eta$ can be obtained as follows:

$$
R_{k-\text { out-of }-n}(t \mid \eta, \lambda, \gamma)=\sum_{j=k}^{n}\binom{n}{j} e^{-\eta j \lambda t^{T}}\left(1-e^{-\eta \lambda t^{T}}\right)^{(n-j)}
$$

Note that

$$
\left(1-e^{-\eta \lambda t^{T}}\right)^{(n-j)}=\sum_{l=0}^{n-j}\binom{n-j}{l}\left(-e^{-\eta \lambda t^{T}}\right)^{l}
$$

The conditional reliability function of $k$-out-of- $n$ systems, from equation (2.45), can be rewritten as

$$
R_{k-\text { out-of }-n}(t \mid \eta, \lambda, \gamma)=\sum_{j=k}^{n}\binom{n}{j} \sum_{l=0}^{n-j}\binom{n-j}{l}(-1)^{l} e^{-\eta(j+l) \lambda t^{T}}
$$

Then if $\eta \sim \operatorname{gamma}(\alpha, \beta)$ then the $k$-out-of- $n$ systemability is given by

$$
R_{\left(T_{t}, \ldots, T_{n}\right)}(t \mid \lambda, \gamma)=\sum_{j=k}^{n}\binom{n}{j} \sum_{l=0}^{n-j}\binom{n-j}{l}(-1)^{l}\left[\frac{\beta}{\beta+\lambda(j+l) t^{T}}\right]^{\alpha}
$$

It can be easily shown that

$$
R_{k-\text { out-of }-n}^{2}(t \mid \eta, \lambda, \gamma)=\sum_{i=k}^{n}\binom{n}{i} \sum_{j=k}^{n}\binom{n}{j} e^{-\eta(i+j) \lambda t^{T}}\left(1-e^{-\eta \lambda t^{T}}\right)^{(2 n-i-j)}
$$Since

$$
\left(1-e^{-\eta \lambda t^{T}}\right)^{(2 n-i-j)}=\sum_{l=0}^{2 n-i-j}\binom{2 n-i-j}{l}\left(-e^{-\eta \lambda t^{T}}\right)^{i}
$$

we can rewrite equation (2.48), after several simplifications, as follows

$$
R_{k \text {-out-of }-n}^{2}(t \mid \eta, \lambda, \gamma)=\sum_{i=k}^{n}\binom{n}{i} \sum_{j=k}^{n}\binom{n}{j}(-1)^{i} \sum_{l=0}^{2 n-i-j}\binom{2 n-i-j}{l} e^{-\eta(i+j+l) \lambda t^{T}}
$$

Therefore, the variance of $k$-out-of-n system systemability function is given by

$$
\begin{aligned}
& \operatorname{Var}\left(R_{k / n}(t \mid \lambda, \gamma)=\int_{\eta} R_{k / n}^{2}(t \mid \eta, \lambda, \gamma) d G(\eta)-\left[\int_{\eta} R_{k / n}(t \mid \eta, \lambda, \gamma) d G(\eta)\right]^{2}\right. \\
& =\sum_{i=k}^{n}\binom{n}{i} \sum_{j=k}^{n}\binom{n}{j} \sum_{l=0}^{2 n-i-j}\binom{2 n-i-j}{l}(-1)^{i}\left(\frac{\beta}{\beta+(i+j+l) \lambda t^{T}}\right)^{2} \\
& -\left(\sum_{j=k}^{n}\binom{n}{j} \sum_{l=0}^{n-j}\binom{n-j}{l}(-1)^{l}\left(\frac{\beta}{\beta+(j+l) \lambda t^{T}}\right)^{2}\right)^{2}
\end{aligned}
$$

Example 2.13: Consider a k-out-of-n system where $\lambda=0.0001, \gamma=1.5, n=5$, and $\eta \sim \operatorname{gamma}(\alpha, \beta)$. Calculate the systemability of various $k$-out-of- $n$ system configurations.

Solution: The systemability of generalized $k$-out-of-5 system configurations is given as follows:

$$
R_{k-\text { out-of }-n}(t \mid \lambda, \gamma)=\sum_{j=k}^{5}\binom{5}{j} \sum_{l=0}^{2-i}\binom{5-j}{l}(-1)^{l}\left[\frac{\beta}{\beta+\lambda(j+l) t^{T}}\right]^{\alpha}
$$

Figures 2.9 and 2.10 show the reliability function (conventional reliability function) and systemability function (equation 2.52 ) of a series system (here $k=5$ ) for $\alpha=2, \beta=3$ and for $\alpha=2, \beta=1$, respectively.

Figures 2.11 and 2.12 show the reliability and systemability functions of a parallel system (here $k=1$ ) for $\alpha=2, \beta=3$ and for $\alpha=2, \beta=1$, respectively. Similarly, Figures 2.13 and 2.14 show the reliability and systemability functions of a 3 -out-of- 5 system for $\alpha=2, \beta=3$ and for $\alpha=2, \beta=1$, respectively.

Figure 2.9. Comparisons of series system reliability vs systemability functions for $\alpha=2$ and $\beta=3$


Figure 2.10. Comparisons of series system reliability vs. systemability functions for $\alpha=2$ and $\beta=1$

Figure 2.11. Comparisons of parallel system reliability $v s$ systemability function for $\alpha=2$ and $\beta=3$


Figure 2.12. Comparisons of parallel system reliability $v s$ Systemability functions for $\alpha=2$ and $\beta=1$

Figure 2.13. Comparisons of k -out-of- $n$ system reliability vs. systemability functions for $\alpha=2$ and $\beta=3$


Figure 2.14. Comparisons of k -out-of- $n$ system reliability vs. systemability functions for $\alpha=2$ and $\beta=1$

# Variance of Systemability Calculations 

Assume $\lambda=0.00001, \gamma_{c}=1.5, \mathrm{n}=3, k=2$, and $\eta \sim \operatorname{gamma}(\alpha, \beta)$, Figures 2.15 and 2.16 shows the systemability and its confidence intervals of a 2 -out-of-3 system (Pham 1993) for $\alpha=2, \beta=1$ and $\alpha=2, \beta=2$, respectively.

Figure 2.15. A 2-out-of-3 systemability and its $95 \%$ confidence interval where $\alpha=2, \beta=1$


Figure 2.16. A 2-out-of-3 systemability and its $95 \%$ confidence interval $(\alpha=2, \beta=2)$

# 2.4 System Reliability with Multiple Failure Modes 

This section discusses various reliability and optimization aspects of systems subject to multiple types of failure. It is assumed that the system component states are statistically independent and identically distributed. Networks of relays, diode circuits, fluid flow valves, etc. are a few examples of systems having components subject to failure in either open or closed modes.

The designations "closed mode" and "short mode" both appear in this section, and we will use the two terms interchangeably. Redundancy can be used to enhance the reliability of a system without any change in the reliability of theindividual components that form the system. However, in a two-failure mode problem, redundancy may either increase or decrease the system's reliability. Therefore, adding components to the system may not increase the system reliability.

The reliability of a system subject to two kinds of failure is calculated as follows (Malon 1989):

$$
\begin{aligned}
\text { System reliability } & =\operatorname{Pr}\{\text { system works in both modes }\} \\
& =\operatorname{Pr}\{\text { system works in open mode }\}-\operatorname{Pr}\{\text { system fails in } \\
& \text { closed mode }\}+\operatorname{Pr}\{\text { system fails in both modes })
\end{aligned}
$$

When the open- and closed-mode failure structures are dual of one another, i.e. $\operatorname{Pr}\{$ system fails in both modes $\}=0$, then the system reliability given by equation (2.53) becomes

System reliability $=1-\operatorname{Pr}\{$ system fails in open mode $\}$

- $\operatorname{Pr}\{$ system fails in closed mode $\}$

Notation

| $q_{0}$ | The open-mode failure probability of each component $\left(p_{0}=1-q_{0}\right)$ |
| :-- | :-- |
| $q_{\mathrm{s}}$ | The short-mode failure probability of each component $\left(p_{\mathrm{s}}=1-q_{\mathrm{s}}\right)$ |
| $\lfloor x\rfloor$ | The largest integer not exceeding $x$ |
| $*$ | Implies an optimal value |

# 2.4.1 Reliability Calculations 

## The Series System

Consider a series system consisting of $n$ components. In this series system, any one component failing in an open mode causes system failure in open mode whereas all components of the system must malfunction in short mode for the system to fail in closed mode.

The probabilities of system fails in open mode and fails in short mode are

$$
F_{0}(n)=1-\left(1-q_{0}\right)^{n}
$$

and

$$
F_{s}(n)=q_{s}^{n}
$$

respectively. From equation (2.54), the system reliability is

$$
R_{s}(n)=\left(1-q_{0}\right)^{n}-q_{s}^{n}
$$

where $n$ is the number of identical and independent components. In a series arrangement, reliability with respect to closed system failure increases with the number of components, whereas reliability with respect to open system failure decreases.Theorem 2.1: Let $\mathrm{q}_{0}$ and $\mathrm{q}_{\mathrm{s}}$ be fixed. There exists an optimum number of components, say $n^{*}$, that maximizes the system reliability. If we define

$$
n_{0}=\frac{\log \left(\frac{q_{0}}{1-q_{s}}\right)}{\log \left(\frac{q_{s}}{1-q_{0}}\right)}
$$

then the system reliability, $\mathrm{R}_{\mathrm{s}}\left(n^{*}\right)$, is maximum for

$$
n^{*}= \begin{cases}\left\lfloor n_{0}\right\rfloor+1 & \text { if } n_{0} \text { is not an integer } \\ n_{0} \text { or } n_{0}+1 & \text { if } n_{0} \text { is an integer }\end{cases}
$$

Proof: The proof is left as an exercise for the reader (see Problem 2.17).
Example 2.14: A switch has two failure modes: fail-open and fail-short. The probability of switch open-circuit failure and short-circuit failure are 0.1 and 0.2 respectively. A system consists of $n$ switches wired in series. That is, given $q_{0}=$ 0.1 and $q_{\mathrm{s}}=0.2$. Then

$$
n_{0}=\frac{\log \left(\frac{0.1}{1-0.2}\right)}{\log \left(\frac{0.2}{1-0.1}\right)}=1.4
$$

Thus, $n^{*}=\lfloor 1.4\rfloor+1=2$. Therefore, when $n^{*}=2$ the system reliability $R_{\mathrm{s}}(n)=$ 0.77 is maximized.

# The Parallel System 

Consider a parallel system consisting of $n$ components. For a parallel configuration, all the components must fail in open mode or at least one component must malfunction in short mode to cause the system to fail completely. The system reliability is given by

$$
R_{p}(n)=\left(1-q_{s}\right)^{n}-q_{0}^{n}
$$

where $n$ is the number of components connected in parallel. In this case, $\left(1-q_{s}\right)^{n}$ represents the probability that no components fail in short mode, and $q_{0}{ }^{n}$ represents the probability that all components fail in open mode.

Theorem 2.2: If we define

$$
n_{0}=\frac{\log \left(\frac{q_{s}}{1-q_{0}}\right)}{\log \left(\frac{q_{0}}{1-q_{s}}\right)}
$$then the system reliability $\mathrm{R}_{\mathrm{p}}\left(n^{*}\right)$ is maximum for

$$
n^{*}= \begin{cases}\left\lfloor n_{0}\right\rfloor+1 & \text { if } n_{0} \text { is not an integer } \\ n_{0} \text { or } n_{0}+1 & \text { if } n_{0} \text { is an integer. }\end{cases}
$$

Proof: The proof is left as an exercise for the reader (see Problem 2.18).
It is observed that, for any range of $q_{0}$ and $q_{s}$, the optimal number of parallel components that maximizes the system reliability is one, if $q_{s}>q_{0}$ (see Problem 2.19). For most other practical values of $q_{0}$ and $q_{s}$ the optimal number turns out to be two. In general, the optimal value of parallel components can be easily obtained using equation (2.58).

# The Parallel-Series System 

Consider a system of components arranged so that there are $m$ subsystems operating in parallel, each subsystem consisting of $n$ identical components in series. Such an arrangement is called a parallel-series arrangement. The components are subject to two types of failure: failure in open mode and failure in short mode.

The systems are characterized by the following properties:

1. The system consists of $m$ subsystems, each subsystem containing $n$ i.i.d. components.
2. A component is either good, failed open, or failed short. Failed components can never become good, and there are no transitions between the open and short failure modes.
3. The system can be (a) good, (b) failed open (at least one component in each subsystem fails open), or (c) failed short (all the components in any subsystem fail short).
4.The unconditional probabilities of component failure in open and short modes are known and are constrained: $q_{0}, q_{s}>0 ; q_{0}+q_{s}<1$.

The probabilities of a system failing in open mode and failing in short mode are given by
and

$$
F_{0}(m)=\left[1-\left(1-q_{0}\right)^{n}\right]^{m}
$$

respectively. The system reliability is

$$
R_{p s}(n, m)=\left(1-q_{s}^{n}\right)^{m}-\left[1-\left(1-q_{0}\right)^{n}\right]^{m}
$$

An interesting example in Barlow and Proschan (1965) shows that there exists no pair $n, m$ maximizing system reliability, since $\mathrm{R}_{\mathrm{ps}}$ is made arbitrarily close to one by appropriate choice of $m$ and $n$. To see this, let

$$
a=\frac{\log q_{s}-\log \left(1-q_{0}\right)}{\log q_{s}+\log \left(1-q_{0}\right)} \quad M_{n}=q_{s}^{-n /(1+a)} \quad m_{n}=\left\lfloor M_{n}\right\rfloor
$$For given $n$, take $m=m_{n}$; then one can rewrite equation (2.62) as:

$$
R_{p s}\left(n, m_{n}\right)=\left(1-q_{s}^{n}\right)^{m_{n}}-\left[1-\left(1-q_{0}\right)^{n}\right]^{m_{n}}
$$

A straightforward computation yields

$$
\lim _{n \rightarrow \infty} R_{p s}\left(n, m_{n}\right)=\lim _{n \rightarrow \infty}\left\{\left(1-q_{s}^{n}\right)^{m_{n}}-\left[1-\left(1-q_{0}\right)^{n}\right]^{m_{n}}\right\}=1
$$

For fixed $n, q_{0}$, and $q_{s}$, one can determine the value of $m$ that maximizes $R_{\mathrm{ps}}$.
Theorem 2.3 (Barlow and Proschan 1965): Let $n, q_{0}$, and $q_{s}$ be fixed. The maximum value of $\mathrm{R}_{\mathrm{ps}}(\mathrm{m})$ is attained at $m^{*}=\left\lfloor m_{0}\right\rfloor+1$, where

$$
m_{0}=\frac{n\left(\log p_{0}-\log q_{s}\right)}{\log \left(1-q_{s}^{n}+\log \left(1-p_{0}^{n}\right)\right.}
$$

If $m_{\mathrm{o}}$ is an integer, then $m_{\mathrm{o}}$ and $m_{\mathrm{o}}+1$ both maximize $\mathrm{R}_{\mathrm{ps}}(m)$.
Proof: The proof is left as an exercise for the reader (see Problem 20).

# The Series-Parallel System 

The series-parallel structure is the dual of the parallel-series structure. We consider a system of components arranged so that there are $m$ subsystems operating in series, each subsystem consisting of $n$ identical components in parallel. Such an arrangement is called a series-parallel arrangement.

Failure in open mode of all the components in any subsystem makes the system unresponsive. Failure in closed (short) mode of a single component in each subsystem also makes the system unresponsive. The probabilities of system failure in open and short mode are given by

$$
F_{0}(m)=1-\left(1-q_{0}^{n}\right)^{m}
$$

and

$$
F_{s}(m)=\left[1-\left(1-q_{s}\right)^{n}\right]^{m}
$$

respectively. The system reliability is

$$
R(m)=\left(1-q_{0}^{n}\right)^{m}-\left[1-\left(1-q_{s}\right)^{n}\right]^{m}
$$

where $m$ is the number of identical subsystems in series and $n$ is the number of identical components in each parallel subsystem.

Barlow and Proschan (1965) show that there exists no pair $(m, n)$ maximizing system reliability. For fixed $m, q_{0}$, and $q_{s}$ however, one can determine the value of $n$ that maximizes the system reliability.

Theorem 2.4 (Barlow and Proschan 1965): Let $n, q_{0}$, and $q_{s}$ be fixed. The maximum value of $R(m)$ is attained at $m^{*}=\left\lfloor m_{0}\right\rfloor+1$, where

$$
m_{0}=\frac{n\left(\log p_{s}-\log q_{0}\right)}{\log \left(1-q_{0}^{n}\right)-\log \left(1-p_{s}^{n}\right)}
$$

If $m_{o}$ is an integer, then $m_{o}$ and $m_{o}+1$ both maximize $R(m)$.Proof: (see Problem 21).

# The $\boldsymbol{k}$-out-of- $\boldsymbol{n}$ Systems 

Consider a $k$-out-of- $n$ system consisting of $n$ identical and independent components that can be either good or failed. The components are subject to two types of failure: failure in open mode and failure in closed mode. The k out of n system can fail when $k$ or more components fail in closed mode or when $(n-k+1)$ or more components fail in open mode.

Applications of $k$-out-of- $n$ systems can be found in the areas of target detection, communication, and safety monitoring systems, and, particularly, in the area of human organizations. The following is an example in the area of human organizations (Nordmann and Pham 1999).

Consider a committee with $n$ members who must decide to accept or reject innovation-oriented projects. The projects are of two types: "good" and "bad". It is assumed that the communication among the members is limited, and each member will make a yes-no decision on each project. A committee member can make two types of error: the error of accepting a bad project and the error of rejecting a good project. The committee will accept a project when $k$ or more members accept it, and will reject a project when $(n-k+1)$ or more members reject it.

Thus, the two types of potential error of the committee are: (1) the acceptance of a bad project (which occurs when $k$ or more members make the error of accepting a bad project); (2) the rejection of a good project (which occurs when ( $n$ $-k+1)$ or more members make the error of rejecting a good project).

This section determines the optimal $k$ or n that maximizes the system reliability. We also study the effect of the system's parameters on the optimal $k$ or $n$. The system fails in closed mode if and only if at least $k$ of its $n$ components fail in closed mode, and we obtain

$$
F_{s}(k, n)=\sum_{i=k}^{n}\binom{n}{i} q_{s}^{i} p_{s}^{n-i}=1-\sum_{i=0}^{k-1}\binom{n}{i} q_{s}^{i} p_{s}^{n-i}
$$

The system fails in open mode if and only if at least $(n-k+1)$ of its $n$ components fail in open mode, that is:

$$
F_{0}(k, n)=\sum_{i=n-k+1}^{n}\binom{n}{i} q_{0}^{i} p_{0}^{n-i}=\sum_{i=0}^{k-1}\binom{n}{i} p_{0}^{i} q_{0}^{n-i}
$$

The system reliability is given by

$$
R(k, n)=1-F_{0}(k, n)-F_{s}(k, n)=\sum_{i=0}^{k-1}\binom{n}{i} q_{s}^{i} p_{s}^{n-i}-\sum_{i=0}^{k-1}\binom{n}{i} p_{0}^{i} q_{0}^{n-i}
$$

For a given $k$, we can find the optimum value of $n$, say $n^{*}$, that maximizes the system reliability.

Theorem 2.5 (Pham 1989a): For fixed $\mathrm{k}, q_{0}$, and $q_{s}$, the maximum value of $\mathrm{R}(k$, $n)$ is attained at $n^{*}=\left\lfloor n_{0}\right\rfloor$ where$$
n_{0}=k\left[\frac{\log \left(\frac{1-q_{0}}{q_{s}}\right)}{\log \left(\frac{1-q_{s}}{q_{0}}\right)}\right]
$$

If $n_{0}$ is an integer, both $n_{0}$ and $n_{0}+1$ maximize $R(k, n)$.
Proof: The proof is left as an exercise for the reader (see Problem 22).
This result shows that when $n_{0}$ is an integer, both $n^{*}-1$ and $n^{*}$ maximize the system reliability $R(k, n)$. In such cases, the lower value will provide the more economical optimal configuration for the system. If $q_{0}=q_{s}$ the system reliability $R(k, n)$ is maximized when $n=2 k$ or $2 k-1$. In this case, the optimum value of $n$ does not depend on the value of $q_{0}$ and $q_{s}$ and the best choice for a decision voter is a majority voter; this system is also called a majority system (Pham,1989a).

From Theorem 2.5, we understand that the optimal system size $\mathrm{n}^{*}$ depends on the various parameters $q_{0}$ and $\mathrm{q}_{\mathrm{s}}$. It can be shown the optimal value $\mathrm{n}^{*}$ is an increasing function of $\mathrm{q}_{0}$ and a decreasing function of $q_{\mathrm{s}}$ (see Problem 23). Intuitively, these results state that when $q_{\mathrm{s}}$ increases it is desirable to reduce the number of components in the system as close to the value of threshold level $k$ as possible. On the other hand, when $q_{0}$ increases, the system reliability will be improved if the number of components increases.

Theorem 2.6 (Ben-Dov 1980): For fixed $n, q_{0}$, and $q_{s}$, it is straightforward to see that the maximum value of $\mathrm{R}(k, n)$ is attained at $k^{*}=\left\lfloor k_{0}\right\rfloor+1$, where

$$
k_{0}=n \frac{\log \left(\frac{q_{0}}{p_{s}}\right)}{\log \left(\frac{q_{s} q_{0}}{p_{s} p_{0}}\right)}
$$

If $k_{0}$ is an integer, both $k_{0}$ and $k_{0}+1$ maximize $\mathrm{R}(k, n)$.
Proof: The proof is left as an exercise for the reader (see Problem 24).
We now discuss how these two values, $k^{*}$ and $n^{*}$, are related to one another. Define $\alpha$ by

$$
\alpha=\frac{\log \left(\frac{q_{0}}{p_{s}}\right)}{\log \left(\frac{q_{s} q_{0}}{p_{s} p_{0}}\right)}
$$

then, for a given $n$, the optimal threshold $k$ is given by $k^{*}=\lceil n \alpha\rceil$ and for a given k the optimal $n$ is $n^{*}=\lfloor k / \alpha\rfloor$. For any given $q_{0}$ and $q_{s}$, we can easily show that (see Problem 25)$$
q_{s}<\alpha<p_{0}
$$

Therefore, we can obtain the following bounds for the optimal value of the threshold $k$ :

$$
n q_{s}<k^{*}<n p_{0}
$$

This result shows that for given values of $q_{0}$ and $q_{s}$, an upper bound for the optimal threshold $k^{*}$ is the expected number of components working in open mode, and a lower bound for the optimal threshold $k^{*}$ is the expected number of components failing in closed mode.

# 2.4.2 An Application of Systems with Multiple Failure Modes 

In many critical applications of digital systems, fault tolerance has been an essential architectural attribute for achieving high reliability. Several techniques can achieve fault tolerance using redundant hardware (Mathur and De Sousa 1975) or software (Pham 1985).

Typical forms of redundant hardware structures for fault-tolerant systems are of two types: fault masking and standby. Masking redundancy is achieved by implementing the functions so that they are inherently error correcting, e.g. triple-modular redundancy (TMR), N-modular redundancy (NMR), and selfpurging redundancy. In standby redundancy, spare units are switched into the system when working units break down. Mathur and De Sousa (1975) have analyzed, in detail, hardware redundancy in the design of fault-tolerant digital systems. Redundant software structures for fault-tolerant systems based on the acceptance tests have been proposed by Homing et al. (1974).

This section presents a fault-tolerant architecture to increase the reliability of a special class of digital systems in communication (Pham and Upadhyaya 1989b). In this system, a monitor and a switch are associated with each redundant unit. The switches and monitors can fail. The monitors have two failure modes: failure to accept a correct result, and failure to reject an incorrect result. The scheme can be used in communication systems to improve their reliability.

Consider a digital circuit module designed to process the incoming messages in a communication system. This module consists of two units: a converter to process the messages, and a monitor to analyze the messages for their accuracy. For example, the converter could be decoding or unpacking circuitry, whereas the monitor could be checker circuitry (Lala 1985).

To guarantee a high reliability of operation at the receiver end, $n$ converters are arranged in "parallel". All, except converter $n$, have a monitor to determine if the output of the converter is correct. If the output of a converter is not correct, the output is cancelled and a switch is changed so that the original input message is sent to the next converter. The architecture of such a system has been proposed by Pham and Upadhyaya (1989b). Systems of this kind have useful applications in communication and network control systems and in the analysis of fault-tolerant software systems.

We assume that a switch is never connected to the next converter without a signal from the monitor, and the probability that it is connected when a signal arrives is $p_{s}$. We next present a general expression for the reliability of the systemconsisting of $n$ non-identical converters arranged in "parallel". Let us define the following notation, events, and assumptions.

Notation

$$
\begin{array}{ll}
p_{i}^{c} & \operatorname{Pr}\{\text { converter } i \text { works }\} \\
p_{i}^{s} & \operatorname{Pr}\{\text { switch } i \text { is connected to converter }(i+1) \text { when a signal arrives }\} \\
p_{i}^{m 1} & \operatorname{Pr}\{\text { monitor } i \text { works when converter } i \text { works }\}=\operatorname{Pr}\{\text { not sending a signal to } \\
& \text { the switch when converter } i \text { works }\} \\
p_{i}^{m 2} & \operatorname{Pr}\{i \text { monitor works when converter } i \text { has failed }\}=\operatorname{Pr}\{\text { sending a signal to } \\
& \text { the switch when converter } i \text { has failed }\} \\
R_{n-k}^{k} & \text { Reliability of the remaining system of size }(n-k) \text { given that the first } k \text { switch } \\
& \text { ches work } \\
R_{n} & \text { Reliability of the system consisting of } n \text { converters }
\end{array}
$$

The events are:

| $C_{i}^{w}, C_{i}^{f}$ | Converter $i$ works, fails |
| :-- | :-- |
| $M_{i}^{w}, M_{i}^{f}$ | Monitor $i$ works, fails |
| $S_{i}^{w}, S_{i}^{f}$ | Switch $i$ works, fails |
| $W$ | System works |

The assumptions are:

1. The system, the switches, and the converters are two-state: good or failed.
2. The module (converter, monitor, or switch) states are mutually statistically independent.
3. The monitors have three states: good, failed in mode 1 , failed in mode 2 .
4. The modules are not identical.

The reliability of the system is defined as the probability of obtaining the correctly processed message at the output. To derive a general expression for the reliability of the system, we use an adapted form of the total probability theorem as translated into the language of reliability.

Let $A$ denote the event that a system performs as desired. Let $X_{i}$ and $X_{j}$ be the event that a component $X$ (e.g. converter, monitor, or switch) is good or failed respectively. Then
$\operatorname{Pr}\{$ system works $\}=\operatorname{Pr}\{$ system works when unit $X$ is good $\} \times \operatorname{Pr}\{$ unit $X$ is good\}

$$
+\operatorname{Pr}\{\text { system works when unit } X \text { fails }\} \times \operatorname{Pr}\{\text { unit } X \text { is failed }\}
$$

The above equation provides a convenient way of calculating the reliability of complex systems. Notice that $R_{1}=p_{i}^{c}$ and for $n \geq 2$, the reliability of the system can be calculated as follows:

$$
\begin{aligned}
R_{n}= & \operatorname{Pr}\left\{W \mid C_{1}^{w} \text { and } M_{1}^{w}\right\} \operatorname{Pr}\left\{C_{1}^{w} \text { and } M_{1}^{w}\right\}+\operatorname{Pr}\left\{W \mid C_{1}^{w} \text { and } M_{1}^{f}\right\} \\
& \operatorname{Pr}\left\{C_{1}^{w} \text { and } M_{1}^{f}\right\}+\operatorname{Pr}\left\{W \mid C_{1}^{f} \text { and } M_{1}^{w}\right\} \operatorname{Pr}\left\{C_{1}^{f} \text { and } M_{1}^{w}\right\}
\end{aligned}
$$$$
+\operatorname{Pr}\left\{W \mid C_{1}^{f} \text { and } M_{1}^{f}\right\} \operatorname{Pr}\left\{C_{1}^{f} \text { and } M_{1}^{f}\right\}
$$

In order for the system to operate when the first converter works and the first monitor fails, the first switch must work and the remaining system of size $n-1$ must work:

$$
\operatorname{Pr}\left\{W \mid C_{1}^{w} \text { and } M_{1}^{f}\right\}=p_{1}^{s} R_{n-1}^{1}
$$

Similarly,

$$
\operatorname{Pr}\left\{W \mid C_{1}^{f} \text { and } M_{1}^{w}\right\}=p_{1}^{s} R_{n-1}^{1}
$$

then

$$
R_{n}=p_{1}^{c} p_{1}^{m_{1}}+\left[p_{1}^{c}\left(1-p_{1}^{m_{1}}\right)+\left(1-p_{1}^{c}\right) p_{1}^{m_{1}}\right] p_{1}^{s} R_{n-1}^{1}
$$

The reliability of the system consisting of $n$ non-identical converters can be rewritten as:

$$
R_{n}=\sum_{i=1}^{n-1} p_{i}^{c} p_{i}^{m 1} \pi_{i-1}+\pi_{n-1} p_{n}^{c} \quad \text { for } n>1
$$

and $R_{1}=p_{1}^{c}$ where

$$
\begin{array}{ll}
\pi_{k}^{j}=\prod_{i<j}^{k} A_{i} & \text { for } k \geq 1 \\
\pi_{k} \equiv \pi_{k}^{1} & \text { for all } k \text { and } \pi_{0}=1
\end{array}
$$

and

$$
A_{i} \equiv\left[p_{i}^{c}\left(1-p_{i}^{m 1}\right)+\left(1-p_{i}^{c}\right) p_{i}^{m 2}\right] \text { for all } i=1,2, \ldots, n
$$

Assume that all the converters, monitors, and switches have the same reliability, that is

$$
p_{i}^{c}=p^{c}, \quad p_{i}^{m 1}=p^{m 1}, \quad p_{i}^{m 2}=p^{m 2}, \quad p_{i}^{s}=p^{s} \quad \text { for all } i
$$

then we obtain a closed form expression for the reliability of system as follows:

$$
R_{n}=\frac{p^{c} p^{m 1}}{1-A}\left(1-A^{n-1}\right)+p^{c} A^{n-1}
$$

where

$$
A=\left[p^{c}\left(1-p^{m 1}\right)+\left(1-p^{c}\right) p^{m 2}\right] p^{s}
$$

# 2.5 Markov Processes 

Stochastic processes are used for the description of a systems operation over time. There are two main types of stochastic processes: continuous and discrete. The complex continuous process is a process describing a system transition from state to state. The simplest process that will be discussed here is a Markov process. Given the current state of the process, its future behavior does not depend on the past. In Section 2.6 we will discuss the discrete stochastic process. As an introduction to the Markov process, let us examine the following example.Example 2.15: Consider a parallel system consisting of two components. From a reliability point of view, the states of the system can be described by

State 1: Full operation (both components operating)
State 2: One component operating - one component failed
State 3: Both components failed
Define

$$
P_{i}(t)=P[X(t)=i]=P[\text { system is in state } i \text { at time } t]
$$

and

$$
P_{i}(t+d t)=P[X(t+d t)=i]=P[\text { system is in state } i \text { at time } t+d t]
$$

Define a random variable $X(t)$ which can assume the values 1,2 , or 3 corresponding to the above-mentioned states. Since $X(t)$ is a random variable, one can discuss $P[X(t)=1], P[X(t)=2]$ or conditional probability, $P\left[X\left(t_{1}\right)=2 \mid X\left(t_{0}\right)=\right.$ 1]. Again, $X(t)$ is defined as a function of time $t$, the last stated conditional probability, $P\left[X\left(t_{1}\right)=2 \mid X\left(t_{0}\right)=1\right]$, can be interpreted as the probability of being in state 2 at time $t_{1}$, given that the system was in state 1 at time $t_{0}$. In this example, the "stage space" is discrete, i.e., $1,2,3$, etc., and the parameter space (time) is continuous. The simple process described above is called a stochastic process, i.e., a process which develops in time (or space) in accordance with some probabilistic (stochastic) laws. There are many types of stochastic processes. In this section, the emphasis will be on Markov processes which are a special type of stochastic process.

Definition 2.3: Let $t_{0}<t_{1}<\ldots<t_{n}$. If

$$
\begin{aligned}
P\left[X\left(t_{n}\right)\right. & \left.=A_{n} \mid X\left(t_{n-1}\right)=A_{n-1}, X\left(t_{n-2}\right)=A_{n-2}, \ldots ., X\left(t_{0}\right)=A_{0}\right] \\
& =P\left[X\left(t_{n}\right)=A_{n} \mid X\left(t_{n-1}\right)=A_{n-1}\right]
\end{aligned}
$$

then the process is called a Markov process.
Given the present state of the process, its future behavior does not depend on past information of the process.

The essential characteristic of a Markov process is that it is a process that has no memory; its future is determined by the present and not the past. If, in addition to having no memory, the process is such that it depends only on the difference $(t+d t)-t=d t$ and not the value of $t$, i.e., $P[X(t+d t)=j \mid X(t)=i]$ is independent of $t$, then the process is Markov with stationary transition probabilities or homogeneous in time. This is the same property noted in exponential event times, and referring back to the graphical representation of $X(t)$, the times between state changes would in fact be exponential if the process has stationary transition probabilities.

Thus, a Markov process which is time homogeneous can be described as a process where events have exponential occurrence times. The random variable of the process is $X(t)$, the state variable rather than the time to failure as in the exponential failure density. To see the types of processes that can be described, a review of the exponential distribution and its properties will be made. Recall that, if $X_{1}, X_{2}, \ldots, X_{\mathrm{n}}$, are independent random variables, each with exponential densityand a mean equal to $1 / \lambda_{i}$ then $\min \left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ has an exponential density with $\operatorname{mean}\left(\sum \lambda_{i}\right)^{-1}$.

The significance of the property is as follows:

1. The failure behavior of the simultaneous operation of components can be characterized by an exponential density with a mean equal to the reciprocal of the sum of the failure rates.
2. The joint failure/repair behavior of a system where components are operating and/or undergoing repair can be characterized by an exponential density with a mean equal to the reciprocal of the sum of the failure and repair rates.
3. The failure/repair behavior of a system such as 2 above, but further complicated by active and dormant operating states and sensing and switching, can be characterized by an exponential density.

The above property means that almost all reliability and availability models can be characterized by a time homogeneous Markov process if the various failure times and repair times are exponential. The notation for the Markov process is $\{X(t)$, $t>0\}$, where $X(t)$ is discrete (state space) and $t$ is continuous (parameter space). By convention, this type of Markov process is called a continuous parameter Markov chain.
From a reliability/availability viewpoint, there are two types of Markov processes. These are defined as follows:

1. Absorbing Process: Contains what is called an "absorbing state" which is a state from which the system can never leave once it has entered, e.g., a failure which aborts a flight or a mission.
2. Ergodic Process Contains no absorbing states such that $X(t)$ can move around indefinitely, e.g., the operation of a ground power plant where failure only temporarily disrupts the operation.
Pham (2000a) page 265, presents a summary of the processes to be considered broken down by absorbing and ergodic categories. Both reliability and availability can be described in terms of the probability of the process or system being in defined "up" states, e.g., states 1 and 2 in the initial example. Likewise, the mean time between failures (MTBF) can be described as the total time in the "up" states before proceeding to the absorbing state or failure state.

Define the incremental transition probability as

$$
P_{i j}(d t)=P[X(t+d t)=j \mid X(t)=i]
$$

This is the probability that the process (random variable $X(t)$ ) will go to state $i$ during the increment $t$ to $(t+d t)$, given that it was in state $i$ at time $t$. Since we are dealing with time homogeneous Markov processes, i.e., exponential failure and repair times, the incremental transition probabilities can be derived from an analysis of the exponential hazard function. In Section 2.1, it was shown that the hazard function for the exponential with mean $1 / \lambda$ was just $\lambda$. This means that the limiting (as $d t \rightarrow 0$ ) conditional probability of an event occurrence between $t$ and $t+d t$, given that an event had not occurred at time $t$, is just $\lambda$, i.e.,$$
h(t)=\lim _{d t \rightarrow 0} \frac{P[t<X<t+d t \mid X>t]}{d t}=\lambda
$$

The equivalent statement for the random variable $X(t)$ is

$$
h(t) d t=P[X(t+d t)=j \mid X(t)=i]=\lambda d t
$$

Now, $h(t) d t$ is in fact the incremental transition probability, thus the $P_{i j}(d t)$ can be stated in terms of the basic failure and/or repair rates.

Returning to Example 2.15, a state transition can be easily constructed showing the incremental transition probabilities for process between all possible states (see Figure.B.4, Pham 2000a)

State 1: Both components operating
State 2: One component up - one component down
State 3: Both components down (absorbing state)
The loops indicate the probability of remaining in the present state during the $d t$ increment

$$
\begin{array}{lll}
P_{11}(d t)=1-2 \lambda d t & P_{12}(d t)=2 \lambda d t & P_{13}(d t)=0 \\
P_{21}(d t)=0 & P_{22}(d t)=1-\lambda d t & P_{23}(d t)=\lambda d t \\
P_{31}(d t)=0 & P_{32}(d t)=0 & P_{33}(d t)=1
\end{array}
$$

The zeros on $P_{i j}, i>j$, denote that the process cannot go backwards, i.e., this is not a repair process. The zero on $P_{13}$ denotes that in a process of this type, the probability of more than one event (e.g., failure, repair, etc.) in the incremental time period $d t$ approaches zero as $d t$ approaches zero.

Except for the initial conditions of the process, i.e., the state in which the process starts, the process is completely specified by the incremental transition probabilities. The reason for the latter is that the assumption of exponential event (failure or repair) times allows the process to be characterized at any time $t$ since it depends only on what happens between $t$ and $(t+d t)$. The incremental transition probabilities can be arranged into a matrix in a way which depicts all possible statewide movements. Thus, for the parallel configurations,

$$
\left[p_{i j}(d t)\right]=\left[\begin{array}{ccc}
1 & 2 & 3 \\
1-2 \lambda d t & 2 \lambda d t & 0 \\
0 & 1-\lambda d t & \lambda d t \\
0 & 0 & 1
\end{array}\right]
$$

for $i, j=1,2$, or 3 . The matrix $\left[P_{i j}(d t)\right]$ is called the incremental, one-step transition matrix. It is a stochastic matrix, i.e., the rows sum to 1.0. As mentioned earlier, this matrix along with the initial conditions completely describes the process.

Now, $\left[P_{i j}(d t)\right]$ gives the probabilities for either remaining or moving to all the various states during the interval $t$ to $t+d t$, hence,

$$
\begin{aligned}
& P_{1}(t+d t)=(1-2 \lambda d t) P_{1}(t) \\
& P_{2}(t+d t)=2 \lambda d t P_{1}(t)(1-\lambda d t) P_{2}(t) \\
& P_{3}(t+d t)=\lambda d t P_{2}(t)+P_{3}(t)
\end{aligned}
$$

By algebraic manipulation, we have$$
\begin{aligned}
& \frac{\left[P_{1}(t+d t)-P_{1}(t)\right]}{d t}=-2 \lambda P_{1}(t) \\
& \frac{\left[P_{2}(t+d t)-P_{2}(t)\right]}{d t}=2 \lambda P_{1}(t)-\lambda P_{2}(t) \\
& \frac{\left[P_{3}(t+d t)-P_{3}(t)\right]}{d t}=\lambda P_{2}(t)
\end{aligned}
$$

Taking limits of both sides as $d t \rightarrow 0$, we obtain

$$
\begin{aligned}
& P_{1}{ }^{\prime}(t)=-2 \lambda P_{1}(t) \\
& P_{2}{ }^{\prime}(t)=2 \lambda P_{1}(t)-2 \lambda P_{2}(t) \\
& P_{3}{ }^{\prime}(t)=\lambda P_{2}(t)
\end{aligned}
$$

The above system of linear first-order differential equations can be easily solved for $P_{1}(t)$ and $P_{2}(t)$, and therefore, the reliability of the configuration can be obtained:

$$
R(t)=\sum_{i=1}^{2} P_{i}(t)
$$

Actually, there is no need to solve all three equations, but only the first two as $P_{3}(t)$ does not appear and also $P_{3}(t)=1-P_{1}(t)-P_{2}(t)$. The system of linear, first-order differential equations can be solved by various means including both manual and machine methods. For purposes here, the manual methods employing the Laplace transform (see Appendix 2) will be used.

$$
\begin{gathered}
L\left[P_{i}(t)\right]=\int_{0}^{\infty} e^{-s t} P_{i}(t) d t=f_{i}(s) \\
L\left[P_{i}^{\prime}(t)\right]=\int_{0}^{\infty} e^{-s t} P_{i}^{\prime}(t) d t=s f_{i}(s)-P_{i}(0)
\end{gathered}
$$

The use of the Laplace transform will allow transformation of the system of linear, first-order differential equations into a system of linear algebraic equations which can easily be solved, and by means of the inverse transforms, solutions of $P_{i}(t)$ can be determined.

Returning to the example, the initial condition of the parallel configuration is assumed to be "full-up" such that

$$
P_{1}(t=0)=1, P_{2}(t=0)=0, P_{3}(t=0)=0
$$

transforming the equations for $P^{\prime}{ }_{1}(t)$ and $P^{\prime}{ }_{2}(t)$ gives

$$
\begin{aligned}
& \left.s f_{1}(s)-P_{1}(t)\right|_{t=0}=-2 \lambda f_{1}(s) \\
& \left.s f_{2}(s)-P_{2}(t)\right|_{t=0}=2 \lambda f_{1}(s)-\lambda f_{2}(s)
\end{aligned}
$$

Evaluating $P_{1}(t)$ and $P_{2}(t)$ at $t=0$ gives

$$
\begin{aligned}
& s f_{1}(s)-1=-2 \lambda f_{1}(s) \\
& s f_{2}(s)-0=2 \lambda f_{1}(s)-\lambda f_{2}(s)
\end{aligned}
$$

from which we obtain

$$
\begin{aligned}
& (s+2 \lambda) f_{1}(s)=1 \\
& -2 \lambda f_{1}(s)+(s+\lambda) f_{2}(s)=0
\end{aligned}
$$Solving the above equations for $f_{1}(s)$ and $f_{2}(s)$, we have

$$
\begin{aligned}
& f_{1}(s)=\frac{1}{(s+2 \lambda)} \\
& f_{2}(s)=\frac{2 \lambda}{[(s+2 \lambda)(s+\lambda)]}
\end{aligned}
$$

From Appendix 2 of the inverse Laplace transforms,

$$
\begin{aligned}
& P_{1}(t)=e^{-2 \lambda t} \\
& P_{2}(t)=2 e^{-\lambda t}-2 e^{-2 \lambda t} \\
& R(t)=P_{1}(t)+P_{2}(t)=2 e^{-\lambda t}-e^{-2 \lambda t}
\end{aligned}
$$

The example given above is that of a simple absorbing process where we are concerned about reliability If repair capability in the form of a repair rate $\mu$ were added to the model, the methodology would remain the same with only the final result changing. With a repair rate $\mu$ added to the parallel configuration, the incremental transition matrix would be

$$
\left[P_{i j}(d t)\right]=\left[\begin{array}{ccc}
1-2 \lambda d t & 2 \lambda d t & 0 \\
\mu d t & 1-(\lambda+\mu) d t & \lambda d t \\
0 & 0 & 1
\end{array}\right]
$$

The differential equations would become

$$
\begin{aligned}
& P_{1}{ }^{*}(t)=-2 \lambda P_{1}(t)+\mu P_{2}(t) \\
& P_{2}{ }^{*}(t)=2 \lambda P_{1}(t)-(\lambda+\mu) P_{2}(t)
\end{aligned}
$$

and the transformed equations would become

$$
\begin{aligned}
& (s+2 \lambda) f_{1}(s)-\mu f_{2}(s)=1 \\
& -2 \lambda f_{1}(s)+(s+\lambda+\mu) f_{2}(s)=0
\end{aligned}
$$

Hence, we obtain

$$
\begin{aligned}
& f_{1}(s)=\frac{(s+\lambda+\mu)}{\left(s-s_{1}\right)\left(s-s_{2}\right)} \\
& f_{2}(s)=\frac{2 \lambda}{\left(s-s_{1}\right)\left(s-s_{2}\right)}
\end{aligned}
$$

where

$$
\begin{aligned}
& s_{1}=\frac{-(3 \lambda+\mu)+\sqrt{(3 \lambda+\mu) 2-8 \lambda^{2}}}{2} \\
& s_{2}=\frac{-(3 \lambda+\mu)-\sqrt{(3 \lambda+\mu) 2-8 \lambda^{2}}}{2}
\end{aligned}
$$

From Appendix 2, we obtain$$
\begin{aligned}
& P_{1}(t)=\frac{\left(s_{1}+\lambda+\mu\right) e^{-s_{1} t}}{\left(s_{1}-s_{2}\right)}+\frac{\left(s_{2}+\lambda+\mu\right) e^{-s_{2} t}}{\left(s_{2}-s_{1}\right)} \\
& P_{2}(t)=\frac{2 \lambda e^{-s_{1} t}}{\left(s_{1}-s_{2}\right)}+\frac{2 \lambda e^{-s_{2} t}}{\left(s_{2}-s_{1}\right)}
\end{aligned}
$$

Thus, the reliability of two-component in a parallel system is given by

$$
\begin{aligned}
R(t) & =P_{1}(t)+P_{2}(t) \\
& =\frac{\left(s_{1}+3 \lambda+\mu\right) e^{-s_{1} t}-\left(s_{2}+3 \lambda+\mu\right) e^{-s_{2} t}}{\left(s_{1}-s_{2}\right)}
\end{aligned}
$$

# System Mean Time Between Failures 

Another parameter of interest in absorbing Markov processes is the mean time between failures (MTBF). Recalling the previous example of a parallel configuration with repair, the differential equations $P_{1}{ }^{\prime}(t)$ and $P_{2}{ }^{\prime}(t)$ describing the process were

$$
\begin{aligned}
& P_{1}{ }^{\prime}(t)=-2 \lambda P_{1}(t)+\mu P_{2}(t) \\
& P_{2}{ }^{\prime}(t)=2 \lambda P_{1}(t)-(\lambda+\mu) P_{2}(t)
\end{aligned}
$$

Integrating both sides of the above equations yields

$$
\begin{gathered}
\int_{0}^{\infty} P_{1}^{\prime}(t) d t=-2 \lambda \int_{0}^{\infty} P_{1}(t) d t+\mu \int_{0}^{\infty} P_{2}(t) d t \\
\int_{0}^{\infty} P_{2}(t) d t=2 \lambda \int_{0}^{\infty} P_{1}(t) d t-(\lambda+\mu) \int_{0}^{\infty} P_{2}(t) d t
\end{gathered}
$$

From Section 2.1,

$$
\int_{0}^{\infty} R(t) d t=M T B F
$$

Similarly,

$$
\begin{aligned}
& \int_{0}^{\infty} P_{1}(t) d t=\text { mean time spent in state } 1, \text { and } \\
& \int_{0}^{\infty} P_{2}(t) d t=\text { mean time spent in state } 2
\end{aligned}
$$

Designating these mean times as $T_{1}$ and $T_{2}$, respectively, we have

$$
\begin{aligned}
& \left.P_{1}(t) d t\right|_{0} ^{\infty}=-2 \lambda T_{1}+\mu T_{2} \\
& \left.P_{2}(t) d t\right|_{0} ^{\infty}=2 \lambda T_{1}-(\lambda+\mu) T_{2}
\end{aligned}
$$

But $P_{1}(t)=0$ as $t \rightarrow \infty$ and $P_{1}(t)=1$ for $t=0$. Likewise, $P_{2}(t)=0$ as $t \rightarrow \infty$ and $P_{2}(t)=0$ for $t=0$. Thus,$$
\begin{aligned}
-1 & =-2 \lambda T_{1}+\mu T_{2} \\
0 & =2 \lambda T_{1}-(\lambda+\mu) T_{2}
\end{aligned}
$$

or, equivalently,

$$
\left[\begin{array}{c}
-1 \\
0
\end{array}\right]=\left[\begin{array}{cc}
-2 \lambda & \mu \\
2 \lambda & -(\lambda+\mu)
\end{array}\right]\left[\begin{array}{l}
T_{1} \\
T_{2}
\end{array}\right]
$$

Therefore,

$$
\begin{gathered}
T_{1}=\frac{(\lambda+\mu)}{2 \lambda^{2}} \quad T_{2}=\frac{1}{\lambda} \\
M T B F=T_{1}+T_{2}=\frac{(\lambda+\mu)}{2 \lambda^{2}}+\frac{1}{\lambda}=\frac{(3 \lambda+\mu)}{2 \lambda^{2}}
\end{gathered}
$$

The MTBF for non-maintenance processes is developed exactly the same way as just shown. What remains under absorbing processes is the case for availability for maintained systems. The difference between reliability and availability for absorbing processes is somewhat subtle. A good example is that of a communication system where, if such a system failed temporarily, the mission would continue, but, if it failed permanently, the mission would be aborted. Consider the following cold-standby configuration consisting of two units: one main unit and one spare unit (Pham 2000a):

State 1: Main unit operating - spare OK
State 2: Main unit out - restoration underway
State 3: Spare unit installed and operating
State 4: Permanent failure (no spare available)
The incremental transition matrix is given by (see Figure B. 8 in Pham 2000a, for a detailed state transition diagram)

$$
\left[P_{i j}(d t)\right]=\left[\begin{array}{cccc}
1-\lambda d t & \lambda d t & 0 & 0 \\
0 & 1-\mu d t & \mu d t & 0 \\
0 & 0 & 1-\lambda d t & \lambda d t \\
0 & 0 & 0 & 1
\end{array}\right]
$$

We obtain

$$
\begin{aligned}
P_{1}^{\prime}(t) & =-\lambda P_{1}(t) \\
P_{2}^{\prime}(t) & =\lambda P_{1}(t)-\mu P_{2}(t) \\
P_{3}^{\prime}(t) & =\mu P_{2}(t)-\lambda P_{3}(t)
\end{aligned}
$$

Using the Laplace transform, we obtain

$$
\begin{aligned}
s f_{1}(s)-1 & =-\lambda f_{1}(s) \\
s f_{2}(s) & =\lambda f_{1}(s)-\mu f_{2}(s) \\
s f_{3}(s) & =\mu f_{2}(s)-\lambda f_{3}(s)
\end{aligned}
$$

After simplifications,$$
\begin{aligned}
& f_{1}(s)=\frac{1}{(s+\lambda)} \\
& f_{2}(s)=\frac{\lambda}{[(s+\lambda)(s+\mu)]} \\
& f_{3}(s)=\frac{\lambda \mu}{\left[(s+\lambda)^{2}(s+\mu)\right]}
\end{aligned}
$$

Therefore, the probability of full-up performance, $P_{1}(t)$, is given by

$$
P_{1}(t)=e^{-\lambda t}
$$

Similarly, the probability of the system being down and under repair, $P_{2}(t)$, is

$$
P_{2}(t)=\left[\frac{\lambda}{(\lambda-\mu)}\right]\left(e^{-\mu t}-e^{-\lambda t}\right)
$$

and the probability of the system being full-up but no spare available, $P_{3}(t)$, is

$$
P_{3}(t)=\left[\frac{\lambda \mu}{(\lambda-\mu)^{2}}\right]\left[e^{-\mu t}-e^{-\lambda t}-(\lambda-\mu) t e^{-\lambda t}\right]
$$

Hence, the point availability, $A(t)$, is given by

$$
A(t)=P_{1}(t)+P_{3}(t)
$$

If average or interval availability is required, this is achieved by

$$
\left(\frac{1}{t}\right) \int_{0}^{T} A(t) d t=\left(\frac{1}{t}\right) \int_{0}^{T}\left[P_{1}(t)+P_{3}(t)\right] d t
$$

where $T$ is the interval of concern.
With the above example, cases of the absorbing process (both maintained and non-maintained) have been covered insofar as "manual" methods are concerned. In general, the methodology for treatment of absorbing Markov processes can be "packaged" in a fairly simplified form by utilizing matrix notation. Thus, for example, if the incremental transition matrix is defined as follows:

$$
\left[P_{i j}(d t)\right]=\left[\begin{array}{ccc}
1-2 \lambda d t & 2 \lambda d t & 0 \\
\mu d t & 1-(\lambda+\mu) d t & \lambda d t \\
0 & 0 & 1
\end{array}\right]
$$

then if the $d t$ s are dropped and the last row and the last column are deleted, the remainder is designated as the matrix $T$ :

$$
[T]=\left[\begin{array}{cc}
1-2 \lambda & 2 \lambda \\
\mu & 1-(\lambda+\mu)
\end{array}\right]
$$

Define $[Q]=[T]^{\prime}-[I]$, where $[T]^{\prime}$ is the transposition of $[T]$ and $[I]$ is the unity matrix:$$
\begin{aligned}
{[Q] } & =\left[\begin{array}{cc}
1-2 \lambda & \mu \\
2 \lambda & 1-(\lambda+\mu)
\end{array}\right]-\left[\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right] \\
& =\left[\begin{array}{cc}
-2 \lambda & \mu \\
2 \lambda & -(\lambda+\mu)
\end{array}\right]
\end{aligned}
$$

Further define $[P(t)]$ and $\left[P^{\prime}(t)\right]$ as column vectors such that

$$
\left[P_{1}(t)\right]=\left[\begin{array}{l}
P_{1}(t) \\
P_{2}(t)
\end{array}\right], \quad\left[P^{\prime}(t)\right]=\left[\begin{array}{l}
P_{1}^{\prime}(t) \\
P_{2}^{\prime}(t)
\end{array}\right]
$$

then

$$
\left[P^{\prime}(t)\right]=[Q][P(t)]
$$

At the above point, solution of the system of differential equations will produce solutions to $P_{1}(t)$ and $P_{2}(t)$. If the MTBF is desired, integration of both sides of the system produces

$$
\begin{aligned}
& {\left[\begin{array}{c}
-1 \\
0
\end{array}\right]=\left[Q \mid\left[\begin{array}{l}
T_{1} \\
T_{2}
\end{array}\right]\right.} \\
& {\left[\begin{array}{c}
-1 \\
0
\end{array}\right]=\left[\begin{array}{cc}
-2 \lambda & \mu \\
2 \lambda & -(\lambda+\mu)
\end{array}\right]\left[\begin{array}{l}
T_{1} \\
T_{2}
\end{array}\right] \text { or } } \\
& {[Q]^{-1}\left[\begin{array}{l}
1 \\
0
\end{array}\right]=\left[\begin{array}{l}
T_{1} \\
T_{2}
\end{array}\right]}
\end{aligned}
$$

where $[Q]^{-1}$ is the inverse of $[Q]$ and the MTBF is given by

$$
\mathrm{MTBF}=T_{1}+T_{2}=\frac{3 \lambda+\mu}{(2 \lambda)^{2}}
$$

In the more general MTBF case,

$$
[Q]^{-1}\left[\begin{array}{c}
-1 \\
0 \\
\cdot \\
\cdot \\
\cdot \\
0
\end{array}\right]=\left[\begin{array}{c}
T_{1} \\
T_{2} \\
\cdot \\
\cdot \\
\cdot \\
T_{n-1}
\end{array}\right] \text { where } \sum_{i=1}^{n-1} T_{i}=\mathrm{MTBF}
$$

and $(n-1)$ is the number of non-absorbing states.
For the reliability/availability case, utilizing the Laplace transform, the system of linear, first-order differential equations is transformed to$$
\begin{aligned}
s\left[\begin{array}{c}
f_{1}(s) \\
f_{2}(s)
\end{array}\right]-\left[\begin{array}{l}
1 \\
0
\end{array}\right] & =\left[\begin{array}{l}
Q
\end{array}\right]\left[\begin{array}{c}
f_{1}(s) \\
f_{2}(s)
\end{array}\right] \\
{[s I-Q]\left[\begin{array}{l}
f_{1}(s) \\
f_{2}(s)
\end{array}\right] } & =\left[\begin{array}{l}
1 \\
0
\end{array}\right] \\
{\left[\begin{array}{c}
f_{1}(s) \\
f_{2}(s)
\end{array}\right] } & =\left[\begin{array}{l}
s I-Q
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
0
\end{array}\right] \\
L^{-1}\left[\begin{array}{c}
f_{1}(s) \\
f_{2}(s)
\end{array}\right] & =L^{-1}\left\{\left[\begin{array}{l}
s I-Q
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
0
\end{array}\right]\right\} \\
{\left[\begin{array}{c}
p_{1}(s) \\
p_{2}(s)
\end{array}\right] } & =L^{-1}\left\{\left[\begin{array}{l}
s I-Q
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
0
\end{array}\right]\right\}
\end{aligned}
$$

Generalization of the latter to the case of $(n-1)$ non-absorbing states is straightforward.

Ergodic processes, as opposed to absorbing processes, do not have any absorbing states, and hence, movement between states can go on indefinitely For the latter reason, availability (point, steady-state, or interval) is the only meaningful measure. As an example for ergodic processes, a ground-based power unit configured in parallel will be selected.

The parallel units are identical, each with exponential failure and repair times with means $1 / \lambda$ and $1 / \mu$, respectively (Pham 2000a). Assume a two-repairmen capability if required (both units down), then

State 1: Full-up (both units operating)
State 2: One unit down and under repair (other unit up)
State 3: Both units down and under repair
It should be noted that, as in the case of failure events, two or more repairs cannot be made in the $d t$ interval.

$$
\left[P_{i j}(d t)\right]=\left[\begin{array}{ccc}
1-2 \lambda d t & 2 \lambda d t & 0 \\
\mu d t & 1-(\lambda+\mu) d t & \lambda d t \\
0 & 2 \mu d t & 1-2 \mu d t
\end{array}\right]
$$

Case I: Point Availability - Ergodic Process. For an ergodic process, as $t \rightarrow \infty$ the availability settles down to a constant level. Point availability gives a measure of things before the "settling down" and reflects the initial conditions on the process. Solution of the point availability is similar to the case for absorbing processes except that the last row and column of the transition matrix must be retained and entered into the system of equations. For example, the system of differential equations becomes$$
\left[\begin{array}{c}
P_{1}^{\prime}(t) \\
P_{2}^{\prime}(t) \\
P_{3}^{\prime}(t)
\end{array}\right]=\left[\begin{array}{ccc}
-2 \lambda & \mu & 0 \\
2 \lambda & -(\lambda+\mu) & 2 \mu \\
0 & \lambda & -2 \mu
\end{array}\right]\left[\begin{array}{c}
P_{1}(t) \\
P_{2}(t) \\
P_{3}(t)
\end{array}\right]
$$

Similar to the absorbing case, the method of the Laplace transform can be used to solve for $P_{1}(t), P_{2}(t)$, and $P_{3}(t)$, with the point availability, $A(t)$, given by

$$
A(t)=P_{1}(t)+P_{2}(t)
$$

Case II: Interval Availability - Ergodic Process. This is the same as the absorbing case with integration over time period $T$ of interest. The interval availability, $A(T)$, is

$$
A(T)=\frac{1}{T} \int_{0}^{T} A(t) d t
$$

Case III: Steady State Availability - Ergodic Process. Here the process is examined as $t \rightarrow \infty$ with complete "washout" of the initial conditions. Letting $t \rightarrow \infty$ the system of differential equations can be transformed to linear algebraic equations. Thus,

$$
\lim _{t \rightarrow \infty}\left[\begin{array}{c}
P_{1}^{\prime}(t) \\
P_{2}^{\prime}(t) \\
P_{3}^{\prime}(t)
\end{array}\right]=\lim _{t \rightarrow \infty}\left[\begin{array}{ccc}
-2 \lambda & \mu & 0 \\
2 \lambda & -(\lambda+\mu) & 2 \mu \\
0 & \lambda & -2 \mu
\end{array}\right]\left[\begin{array}{c}
P_{1}(t) \\
P_{2}(t) \\
P_{3}(t)
\end{array}\right]
$$

As $t \rightarrow \infty, P_{i}(t) \rightarrow$ constant and $P_{i}{ }^{\prime}(t) \rightarrow 0$. This leads to an unsolvable sys-tem, namely

$$
\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]=\left[\begin{array}{ccc}
-2 \lambda & \mu & 0 \\
2 \lambda & -(\lambda+\mu) & 2 \mu \\
0 & \lambda & -2 \mu
\end{array}\right]\left[\begin{array}{c}
P_{1}(t) \\
P_{2}(t) \\
P_{3}(t)
\end{array}\right]
$$

To avoid the above difficulty, an additional equation is introduced:

$$
\sum_{i=1}^{3} P_{i}(t)=1
$$

With the introduction of the new equation, one of the original equations is deleted and a new system is formed:

$$
\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right]=\left[\begin{array}{ccc}
1 & 1 & 1 \\
-2 \lambda & \mu & 0 \\
2 \lambda & -(\lambda+\mu) & 2 \mu
\end{array}\right]\left[\begin{array}{c}
P_{1}(t) \\
P_{2}(t) \\
P_{3}(t)
\end{array}\right]
$$

or, equivalently,

$$
\left[\begin{array}{l}
P_{1}(t) \\
P_{2}(t) \\
P_{3}(t)
\end{array}\right]=\left[\begin{array}{ccc}
1 & 1 & 1 \\
-2 \lambda & \mu & 0 \\
2 \lambda & -(\lambda+\mu) & 2 \mu
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right]
$$We now obtain the following results:

$$
\begin{aligned}
& P_{1}(t)=\frac{\mu^{2}}{(\mu+\lambda)^{2}} \\
& P_{2}(t)=\frac{2 \lambda \mu}{(\mu+\lambda)^{2}}
\end{aligned}
$$

and

$$
\begin{aligned}
P_{3}(t) & =1-P_{1}(t)-P_{2}(t) \\
& =\frac{\lambda^{2}}{(\mu+\lambda)^{2}}
\end{aligned}
$$

Therefore, the steady state availability, $A(\infty)$, is given by

$$
\begin{aligned}
A_{3}(\infty) & =P_{1}(t)+P_{2}(t) \\
& =\frac{\mu(\mu+2 \lambda)}{(\mu+\lambda)^{2}}
\end{aligned}
$$

Note that Markov methods can also be employed where failure or repair times are not exponential, but can be represented as the sum of exponential times with identical means (Erlang distribution or Gamma distribution with integer valued shape parameters). Basically, the method involves the introduction of "dummy" states which are of no particular interest in themselves, but serve the purpose of changing the hazard function from constant to increasing.

# 2.6 Counting Processes 

Among discrete stochastic processes, counting processes in reliability engineering are widely used to describe the appearance of events in time, e.g., failures, number of perfect repairs, etc. The simplest counting process is a Poisson process. The Poisson process plays a special role to many applications in reliability (Pham 2000a). A classic example of such an application is the decay of uranium. Radioactive particles from nuclear material strike a certain target in accordance with a Poisson process of some fixed intensity. A well-known counting process is the so-called renewal process. This process is described as a sequence of events, the intervals between which are independent and identically distributed random variables. In reliability theory, this type of mathematical model is used to describe the number of occurrences of an event in the time interval. In this section we also discuss the quasi-renewal process and the non-homogeneous Poisson process.

A non-negative, integer-valued stochastic process, $N(t)$, is called a counting process if $N(t)$ represents the total number of occurrences of the event in the time interval $[0, \mathrm{t}]$ and satisfies these two properties:

1. If $t_{1}<t_{2}$, then $N\left(t_{1}\right) \leq N\left(t_{2}\right)$
2. If $t_{1}<t_{2}$, then $N\left(t_{2}\right)-N\left(t_{1}\right)$ is the number of occurrences of the event in the interval $\left[t_{1}, t_{2}\right]$For example, if $N(t)$ equals the number of persons who have entered a restaurant at or prior to time $t$, then $N(t)$ is a counting process in which an event occurs whenever a person enters the restaurant.

# 2.6.1 Poisson Processes 

One of the most important counting processes is the Poisson process.
Definition 2.4: A counting process, $N(t)$, is said to be a Poisson process with intensity $\lambda$ if

1. The failure process, $N(t)$, has stationary independent increments
2. The number of failures in any time interval of length $s$ has a Poisson distribution with mean $\lambda s$, that is,

$$
P\{N(t+s)-N(t)=n\}=\frac{e^{-\lambda s}(\lambda s)^{n}}{n!} \quad n=0,1,2, \ldots
$$

3. The initial condition is $N(0)=0$

This model is also called a homogeneous Poisson process indicating that the failure rate $\lambda$ does not depend on time $t$. In other words, the number of failures occurring during the time interval $(t, t+s]$ does not depend on the current time $t$ but only the length of time interval $s$. A counting process is said to possess independent increments if the number of events in disjoint time intervals are independent.

For a stochastic process with independent increments, the auto-covariance function is

$$
\operatorname{Cov}\left[X\left(t_{1}\right), X\left(t_{2}\right)\right]= \begin{cases}\operatorname{Var}\left[N\left(t_{1}+s\right)-N\left(t_{2}\right)\right] & \text { for } 0<t_{2}-t_{1}<s \\ 0 & \text { otherwise }\end{cases}
$$

where

$$
X(t)=N(t+s)-N(t)
$$

If $X(t)$ is Poisson distributed, then the variance of the Poisson distribution is

$$
\operatorname{Cov}\left[X\left(t_{1}\right), X\left(t_{2}\right)\right]= \begin{cases}\lambda\left[s-\left(t_{2}-t_{1}\right)\right] & \text { for } 0<t_{2}-t_{1}<s \\ 0 & \text { otherwise }\end{cases}
$$

This result shows that the Poisson increment process is covariance stationary. We now present several properties of the Poisson process.

Property 2.3: The sum of independent Poisson processes, $N_{1}(t), N_{2}(t), \ldots, N_{\mathrm{k}}(t)$, with mean values $\lambda_{1} t, \lambda_{2} t, \ldots, \lambda_{\mathrm{k}} t$ respectively, is also a Poisson process with mean $\left(\sum_{i=1}^{k} \lambda_{i}\right) t$. In other words, the sum of the independent Poisson processes is also a Poisson process with a mean that is equal to the sum of the individual Poisson process' mean.

Proof: The proof is left as an exercise for the reader (see Problem 26).Property 2.4: The difference of two independent Poisson processes, $N_{1}(t)$, and $N_{2}(t)$, with mean $\lambda_{1} t$ and $\lambda_{2} t$, respectively, is not a Poisson process. Instead, it has the probability mass function

$$
P\left[N_{1}(t)-N_{2}(t)=k\right]=e^{-\left(\lambda_{1}+\lambda_{2}\right) t}\left(\frac{\lambda_{1}}{\lambda_{2}}\right)^{\frac{k}{2}} I_{k}\left(2 \sqrt{\lambda_{1} \lambda_{2}} t\right)
$$

where $I_{k}($.$) is a modified Bessel function of order k (Handbook 1980)$.
Proof: The proof is left as an exercise for the reader (see Problem 27).
Property 2.5: If the Poisson process, $N(t)$, with mean $\lambda t$, is filtered such that every occurrence of the event is not completely counted, then the process has a constant probability $p$ of being counted. The result of this process is a Poisson process with mean $\lambda p t[]$.

Property 2.6: Let $N(t)$ be a Poisson process and $Y_{n}$ a family of independent and identically distributed random variables which are also independent of $N(t)$. A stochastic process $X(t)$ is said to be a compound Poisson process if it can be represented as

$$
X(t)=\sum_{i=1}^{N(t)} Y_{i}
$$

# 2.6.2 Renewal Processes 

A renewal process is a more general case of the Poisson process in which the inter-arrival times of the process or the time between failures do not necessarily follow the exponential distribution. For convenience, we will call the occurrence of an event a renewal, the inter-arrival time the renewal period, and the waiting time the renewal time.

Definition 2.5: A counting process $N(t)$ that represents the total number of occurrences of an event in the time interval $(0, t]$ is called a renewal process, if the time between failures are independent and identically distributed random variables.

The probability that there are exactly $n$ failures occurring by time $t$ can be written as

$$
P\{N(t)=n\}=P\{N(t) \geq n\}-P\{N(t)>n\}
$$

Note that the times between the failures are $T_{1}, T_{2}, \ldots, T_{n}$ so the failures occurring at time $W_{k}$ are

$$
W_{k}=\sum_{i=1}^{k} T_{i}
$$

and

$$
T_{k}=W_{k}-W_{k-1}
$$Thus,

$$
\begin{aligned}
P\{N(t)=n\} & =P\{N(t) \geq n\}-P\{N(t)>n\} \\
& =P\left\{W_{n} \leq t\right\}-P\left\{W_{n+1} \leq t\right\} \\
& =F_{n}(t)-F_{n+1}(t)
\end{aligned}
$$

where $F_{n}(t)$ is the cumulative distribution function for the time of the $n$th failure and $n=0,1,2, \ldots$.

Example 2.16: Consider a software testing model for which the time to find an error during the testing phase has an exponential distribution with a failure rate of $X$. It can be shown that the time of the $n$th failure follows the gamma distribution with parameters $k$ and $n$ with probability density function. From equation (2.83) we obtain

$$
\begin{aligned}
P\{N(t)=n\} & =P\{N(t) \leq n\}-P\{N(t) \leq n-1\} \\
& =\sum_{k=0}^{\infty} \frac{(\lambda t)^{k}}{k!} e^{-\lambda t}-\sum_{k=0}^{n-1} \frac{(\lambda t)^{k}}{k!} e^{-\lambda t} \\
& =\frac{(\lambda t)^{n}}{n!} e^{-\lambda t} \quad \text { for } \quad n=0,1,2, \ldots
\end{aligned}
$$

Several important properties of the renewal function are given below.
Property 2.7: The mean value function of the renewal process, denoted by $m(t)$, is equal to the sum of the distribution function of all renewal times, that is,

$$
\begin{aligned}
m(t) & =E[N(t)] \\
& =\sum_{n=1}^{\infty} F_{n}(t)
\end{aligned}
$$

Proof: The renewal function can be obtained as

$$
\begin{aligned}
m(t) & =E[N(t)] \\
& =\sum_{n=1}^{\infty} n P\{N(t)=n\} \\
& =\sum_{n=1}^{\infty} n\left[F_{n}(t)-F_{n+1}(t)\right] \\
& =\sum_{n=1}^{\infty} F_{n}(t)
\end{aligned}
$$

The mean value function of the renewal process is also called the renewal function.
Property 2.8: The renewal function, $m(t)$, satisfies the following equation:$$
m(t)=F_{a}(t)+\int_{0}^{t} m(t-s) d F_{a}(s)
$$

where $F_{a}(t)$ is the distribution function of the inter-arrival time or the renewal period. The proof is left as an exercise for the reader (see Problem 28).

In general, let $y(t)$ be an unknown function to be evaluated and $x(t)$ be any non-negative and integrable function associated with the renewal process. Assume that $F_{a}(t)$ is the distribution function of the renewal period. We can then obtain the following result.

Property 2.9: Let the renewal equation be

$$
y(t)=x(t)+\int_{0}^{t} y(t-s) d F_{a}(s)
$$

then its solution is given by

$$
y(t)=x(t)+\int_{0}^{t} x(t-s) d m(s)
$$

where $m(t)$ is the mean value function of the renewal process.
The proof of the above property can be easily derived using the Laplace transform. It is also noted that the integral equation given in Property 2.8 is a special case of Property 2.9.

Example 2.17: Let $x(t)=a$. Thus, in Property 2.9, the solution $y(t)$ is given by

$$
\begin{aligned}
y(t) & =x(t)+\int_{0}^{t} x(t-s) d m(s) \\
& =a+\int_{0}^{t} a d m(s) \\
& =a(1+E[N(t)])
\end{aligned}
$$

# 2.6.3 Quasi-renewal Processes 

In this section, a general renewal process, namely, the quasi-renewal process, is discussed. Let $\{N(t), t>0\}$ be a counting process and let $X_{\mathrm{n}}$ be the time between the $(n-1)^{\text {th }}$ and the $n^{\text {th }}$ event of this process, $\mathrm{n} \geq 1$.

Definition 2.6 (Wang and Pham 1996a): If the sequence of non-negative random variables $\left\{X_{1}, X_{2}, \ldots\right\}$ is independent and

$$
X_{i}=a X_{i-1}
$$

for $i \geq 2$ where $\alpha>0$ is a constant, then the counting process $\{N(t), t \geq 0\}$ is said to be a quasi-renewal process with parameter and the first inter-arrival time $X_{1}$.When $\alpha=1$, this process becomes the ordinary renewal process as discussed in Section 2.6.2. This quasi-renewal process can be used to model reliability growth processes in software testing phases and hardware burn-in stages for $\alpha>1$, and in hardware maintenance processes when $\alpha \leq 1$.

Assume that the probability density function, cumulative distribution function, survival function, and failure rate of random variable $X_{1}$ are $f_{1}(x), F_{1}(x), s_{1}(x)$, and $r_{l}(x)$, respectively. Then the pfd, cdf, survival function, failure rate of $X_{\mathrm{n}}$ for $n=1$, $2,3, \ldots$ is respectively given below (Wang and Pham 1996a):

$$
\begin{aligned}
& f_{n}(x)=\frac{1}{\alpha^{n-1}} f_{1}\left(\frac{1}{\alpha^{n-1}} x\right) \\
& F_{n}(x)=F_{1}\left(\frac{1}{\alpha^{n-1}} x\right) \\
& s_{n}(x)=s_{1}\left(\frac{1}{\alpha^{n-1}} x\right) \\
& f_{n}(x)=\frac{1}{\alpha^{n-1}} r_{1}\left(\frac{1}{\alpha^{n-1}} x\right)
\end{aligned}
$$

Similarly, the mean and variance of $X_{\mathrm{n}}$ is given as

$$
\begin{aligned}
& E\left(X_{\mathrm{n}}\right)=\alpha^{n-1} E\left(X_{1}\right) \\
& \operatorname{Var}\left(X_{\mathrm{n}}\right)=\alpha^{2 n-2} \operatorname{Var}\left(X_{1}\right)
\end{aligned}
$$

Because of the non-negativity of $X_{1}$ and the fact that $X_{1}$ is not identically 0 , we obtain

$$
E\left(X_{1}\right)=\mu_{1} \neq 0
$$

Proposition 2.1 (Wang and Pham 1996a): The shape parameters of $X_{\mathrm{n}}$ are the same for $n=1,2,3, \ldots$ for a quasi-renewal process if $X_{1}$ follows the gamma, Weibull, or log normal distribution.

This means that after "renewal", the shape parameters of the inter-arrival time will not change. In software reliability, the assumption that the software debugging process does not change the error-free distribution type seems reasonable. Thus, the error-free times of software during the debugging phase modeled by a quasi-renewal process will have the same shape parameters. In this sense, a quasi-renewal process is suitable to model the software reliability growth. It is worthwhile to note that

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \frac{E\left(X_{1}+X_{2}+\ldots+X_{n}\right)}{n} & =\lim _{n \rightarrow \infty} \frac{\mu_{1}\left(1-\alpha^{n}\right)}{(1-\alpha) n} \\
& =0 \quad \text { if } \alpha<1 \\
& =\infty \quad \text { if } \alpha>1
\end{aligned}
$$Therefore, if the inter-arrival time represents the error-free time of a software system, then the average error-free time approaches infinity when its debugging process is occurring for a long debugging time.

# Distribution of $N(t)$ 

Consider a quasi-renewal process with parameter $\alpha$ and the first inter-arrival time $X_{1}$. Clearly, the total number of renewals, $N(t)$, that has occurred up to time $t$ and the arrival time of the $n$th renewal, $S S_{n}$, has the following relationship:

$$
N(t) \geq n \text { if and only if } S S_{n} \leq t
$$

that is, $N(t)$ is at least $n$ if and only if the nth renewal occurs prior to time $t$. It is easily seen that

$$
S S_{n}=\sum_{i=1}^{n} X_{i}=\sum_{i=1}^{n} \alpha^{i-1} X_{1} \quad \text { for } \quad n \geq 1
$$

Here, $S S_{0}=0$. Thus, we have

$$
\begin{aligned}
P\{N(t)=n\} & =P\{N(t)=n\}-P\{N(t) \geq n+1\} \\
& =P\left\{S S_{n} \leq t\right\}-P\left\{S S_{n+1} \leq t\right\} \\
& =G_{n}(t)-G_{n+1}(t)
\end{aligned}
$$

where $G_{n}(t)$ is the convolution of the inter-arrival times $F_{1}, F_{2}, F_{3}, \ldots, F_{n}$. In other words,

$$
G_{n}(t)=P\left\{F_{1}+F_{2}+\ldots .+F_{n} \leq t\right\}
$$

If the mean value of $N(t)$ is defined as the renewal function $m(t)$, then,

$$
\begin{aligned}
m(t) & =E[N(t)] \\
& =\sum_{n=1}^{\infty} P\{N(t) \geq n\} \\
& =\sum_{n=1}^{\infty} P\left\{S S_{n} \leq t\right\} \\
& =\sum_{n=1}^{\infty} G_{n}(t)
\end{aligned}
$$

The derivative of $m(t)$ is known as the renewal density

$$
\lambda(t)=m^{\prime}(t)
$$

In renewal theory, random variables representing the inter-arrival distributions only assume non-negative values, and the Laplace transform of its distribution $F_{1}(t)$ is defined by

$$
\mathfrak{L}\left\{F_{1}(s)\right\}=\int_{0}^{\infty} e^{-s s} d F_{1}(x)
$$

Therefore,

$$
\mathfrak{L} F_{n}(s)=\int_{0}^{\infty} e^{-s^{n-1} s t} d F_{1}(t)=\mathfrak{L} F_{1}\left(\alpha^{n-1} s\right)
$$and

$$
\begin{aligned}
\mathfrak{L} m_{n}(s) & =\sum_{n=1}^{\infty} \mathfrak{L} G_{n}(s) \\
& =\sum_{n=1}^{\infty} \mathfrak{L} F_{1}(s) \mathfrak{L} F_{1}(\alpha s) \cdots \mathfrak{L} F_{1}\left(\alpha^{n-1} s\right)
\end{aligned}
$$

Since there is a one-to-one correspondence between distribution functions and its Laplace transform, it follows that

Proposition 2.2 (Wang and Pham 1996a): The first inter-arrival distribution of a quasi-renewal process uniquely determines its renewal function.

If the inter-arrival time represents the error-free time (time to first failure), a quasi-renewal process can be used to model reliability growth for both software and hardware.

Suppose that all faults of software have the same chance of being detected. If the inter-arrival time of a quasi-renewal process represents the error-free time of a software system, then the expected number of software faults in the time interval $[0, t]$ can be defined by the renewal function, $m(t)$, with parameter $\alpha>1$. Denoted by $m_{r}(t)$, the number of remaining software faults at time $t$, it follows that

$$
m_{r}(t)=m\left(T_{c}\right)-m(t)
$$

where $m\left(T_{c}\right)$ is the number of faults that will eventually be detected through a software lifecycle $T_{c}$.

# 2.6.4 Non-homogeneous Poisson Processes 

The non-homogeneous Poisson process model (NHPP) that represents the number of failures experienced up to time $t$ is a non-homogeneous Poisson process $\{N(t), t$ $\geq 0\}$. The main issue in the NHPP model is to determine an appropriate mean value function to denote the expected number of failures experienced up to a certain time.

With different assumptions, the model will end up with different functional forms of the mean value function. Note that in a renewal process, the exponential assumption for the inter-arrival time between failures is relaxed, and in the NHPP, the stationary assumption is relaxed.

The NHPP model is based on the following assumptions:

- The failure process has an independent increment, i.e., the number of failures during the time interval $(t, t+s)$ depends on the current time $t$ and the length of time interval $s$, and does not depend on the past history of the process.
- The failure rate of the process is given by

$$
\begin{gathered}
P\{\text { exactly one failure in }(t, t+\Delta t)\}=P\{N(t+\Delta t)-N(t)=1\} \\
=\lambda(t) \Delta t+o(\Delta t)
\end{gathered}
$$

where $\lambda(t)$ is the intensity function.

- During a small interval $\Delta t$, the probability of more than one failure is negligible, that is,$P\{$ two or more failure in $(t, t+\Delta t)\}=o(\Delta t)$

- $\quad$ The initial condition is $N(0)=0$.

On the basis of these assumptions, the probability of exactly $n$ failures occurring during the time interval $(0, t)$ for the NHPP is given by

$$
\operatorname{Pr}\{N(t)=n\}=\frac{[m(t)]^{n}}{n!} e^{-m(t)} \quad n=0,1,2, \ldots
$$

where $m(t)=E[N(t)]=\int_{0}^{t} \lambda(s) d s$ and $\lambda(t)$ is the intensity function. It can be easily shown that the mean value function $m(t)$ is non-decreasing.

# Reliability Function 

The reliability $R(t)$, defined as the probability that there are no failures in the time interval $(0, t)$, is given by

$$
\begin{aligned}
R(t) & =P\{N(t)=0\} \\
& =e^{-m(t)}
\end{aligned}
$$

In general, the reliability $R(x \mid t)$, the probability that there are no failures in the interval $(t, t+x)$, is given by

$$
\begin{aligned}
R(x \mid t) & =P\{N(t+x)-N(t)=0\} \\
& =e^{-[m(t+x)-m(t)]}
\end{aligned}
$$

and its density is given by

$$
f(x)=\lambda(t+x) e^{-[m(t+x)-m(t)]}
$$

where

$$
\lambda(x)=\frac{\partial}{\partial x}[m(x)]
$$

The variance of the NHPP can be obtained as follows:

$$
\operatorname{Var}[N(t)]=\int_{0}^{t} \lambda(s) d s
$$

and the auto-correlation function is given by

$$
\begin{aligned}
\operatorname{Cor}[s] & =E[N(t)] E[N(t+s)-N(t)]+E\left[N^{2}(t)\right] \\
& =\int_{0}^{t} \lambda(s) d s \int_{0}^{t+s} \lambda(s) d s+\int_{0}^{t} \lambda(s) d s \\
& =\int_{0}^{t} \lambda(s) d s\left[1+\int_{0}^{t+s} \lambda(s) d s\right]
\end{aligned}
$$Example 2.18: Assume that the intensity $\lambda$ is a random variable with the pdf $f(\lambda)$. Then the probability of exactly $n$ failures occurring during the time interval $(0, t)$ is given by

$$
P\{N(t)=n\}=\int_{0}^{\infty} e^{-\lambda t} \frac{(\lambda t)^{n}}{n!} f(\lambda) d \lambda
$$

It can be shown that if the pdf $f(\lambda)$ is given as the following gamma density function with parameters $k$ and $m$,

$$
f(\lambda)=\frac{1}{\Gamma(m)} k^{m} \lambda^{m-1} e^{-k \lambda} \quad \text { for } \lambda \geq 0
$$

then

$$
P\{N(t)=n\}=\binom{n+m-1}{n} p^{m} q^{n} \quad n=0,1,2, \ldots
$$

is also called a negative binomial density function, where

$$
p=\frac{k}{t+k} \quad \text { and } \quad q=\frac{t}{t+k}=1-p
$$

# 2.7 Further Reading 

The reader interested in a deeper understanding of advanced probability theory and stochastic processes should note the following highly recommended books:

Devore, J.L., Probability and Statistics for Engineering and the Sciences, 3rd edition, Brooks/Cole Pub. Co., Pacific Grove, 1991.
Gnedenko, BV and I.A. Ushakov, Probabilistic Reliability Engineering, Wiley, New York, 1995.
Feller, W., An Introduction to Probability Theory and Its Applications, 3rd edition, Wiley, New York, 1994.

### 2.8 Problems

1. Assume that the hazard rate, $h(t)$, has a positive derivative. Show that the hazard distribution

$$
H(t)=\int_{0}^{t} h(x) d x
$$

is strictly convex.
2. An operating unit is supported by $(n-1)$ identical units on cold standby. When it fails, a unit from standby takes its place. The system fails if all $n$ units fail.Assume that units on standby cannot fail and the lifetime of each unit follows the exponential distribution with failure rate $\lambda$.
(a) What is the distribution of the system lifetime?
(b) Determine the reliability of the standby system for a mission of 100 hours when $\lambda=0.0001$ per hour and $n=5$.
3. Assume that there is some latent deterioration process occurring in the system. During the interval $[0, a-h]$ the deterioration is comparatively small so that the shocks do not cause system failure. During a relatively short time interval $[a-h, a]$, the deterioration progresses rapidly and makes the system susceptible to shocks. Assume that the appearance of each shock follows the exponential distribution with failure rate $\lambda$. What is the distribution of the system lifetime?
4. Consider a series system of $n$ Weibull components. The corresponding lifetimes $T_{1}, T_{2}, \ldots, T_{n}$ are assumed to be independent with pdf

$$
f(t)= \begin{cases}\lambda_{i}^{\beta} \beta t^{\beta-1} e^{-\left(\lambda_{i} t\right)^{\beta}} & \text { for } t \geq 0 \\ 0 & \text { otherwise }\end{cases}
$$

where $\lambda>0$ and $\beta>0$ are the scale and shape parameters, respectively.
(a) Show that the lifetime of a series system has the Weibull distribution with pdf

$$
f_{s}(t)=\left\{\begin{array}{ll}
\left(\sum_{i=1}^{n} \lambda_{i}^{\beta}\right) \beta t^{\beta-1} e^{-\left(\sum_{i=1}^{n} \lambda_{i}^{\beta}\right) t^{\beta}} & \text { for } t \geq 0 \\
0 & \text { otherwise }
\end{array}\right.
$$

(b) Find the reliability of this series system.
5. Consider the pdf of a random variable that is equally likely to take on any value only in the interval from $a$ to $b$.
(a) Show that this pdf is given by

$$
f(t)= \begin{cases}\frac{1}{b-a} & \text { for } a<t<0 \\ 0 & \text { otherwise }\end{cases}
$$

(b) Derive the corresponding reliability function $R(t)$ and failure rate $h(t)$.
(c) Think of an example where such a distribution function would be of interest in reliability application.
6. The failure rate function, denoted by $h(t)$, is defined as

$$
h(t)=-\frac{d}{d t} \ln [R(t)]
$$Show that the constant failure rate function implies an exponential distribution.
7. One thousand new streetlights are installed in Saigon city. Assume that the lifetimes of these streetlights follow the normal distribution. The average life of these lamps is estimated at 980 burning-hours with a standard deviation of 100 hours.
(a) What is the expected number of lights that will fail during the first 800 burning-hours?
(b) What is the expected number of lights that will fail between 900 and 1100 burning-hours?
(c) After how many burning-hours would $10 \%$ of the lamps be expected to fail?
8. A fax machine with constant failure rate $\lambda$ will survive for a period of 720 hours without failure, with probability 0.80 .
(a) Determine the failure rate $\lambda$.
(b) Determine the probability that the machine, which is functioning after 600 hours, will still function after 800 hours.
(c) Find the probability that the machine will fail within 900 hours, given that the machine was functioning at 720 hours.
9. The time to failure T of a unit is assumed to have a log normal distribution with pdf

$$
f(t)=\frac{1}{\sqrt{2 \pi}} \frac{1}{\sigma t} e^{-\frac{(\ln t-\mu)^{2}}{2 \sigma^{2}}} \quad t>0
$$

Show that the failure rate function is unimodal.
10. A diode may fail due to either open or short failure modes. Assume that the time to failure $T_{0}$ caused by open mode is exponentially distributed with pdf

$$
f_{0}(t)=\lambda_{0} e^{-\lambda_{0} t} \quad t \geq 0
$$

and the time to failure $T_{1}$ caused by short mode has the pdf

$$
f_{s}(t)=\lambda_{s} e^{-\lambda_{s} t} \quad t \geq 0
$$

The pdf for the time to failure $T$ of the diode is given by

$$
f(t)=p f_{0}(t)+(1-p) f_{s}(t) \quad t \geq 0
$$

(a) Explain the meaning of $p$ in the above pdf function.
(b) Derive the reliability function $R(t)$ and failure rate function $h(t)$ for the time to failure $T$ of the diode.
(c) Show that the diode with pdf $f(t)$ has a decreasing failure rate (DFR).
11. A diesel is known to have an operating life (in hours) that fits the following pdf:$$
f(t)=\frac{2 a}{(t+b)^{2}} \quad t \geq 0
$$

The average operating life of the diesel has been estimated to be 8760 hours.
(a) Determine $a$ and $b$.
(b) Determine the probability that the diesel will not fail during the first 6000 operating-hours.
(c) If the manufacturer wants no more than $10 \%$ of the diesels returned for warranty service, how long should the warranty be?
12. The failure rate for a hydraulic component

$$
h(t)=\frac{t}{t+1} \quad t>0
$$

where $t$ is in years.
(a) Determine the reliability function $R(t)$.
(b) Determine the MTTF of the component.
13. A 18 -month guarantee is given based on the assumption that no more than $5 \%$ of new cars will be returned.
(a) The time to failure $T$ of a car has a constant failure rate. What is the maximum failure rate that can be tolerated?
(b) Determine the probability that a new car will fail within three years assuming that the car was functioning at 18 months.
14. Show that if

$$
R_{1}(t) \geq R_{2}(t) \quad \text { for all } t
$$

where $R_{i}(t)$ is the system reliability of the structure $i$, then MTTF of the system structure 1 is always $\geq$ MTTF of the system structure 2 .
15. Prove equation (2.10)
16. Show that the reliability function of Pham distribution (see equation 2.21) is given as in equation (2.22).
17. Prove Theorem 2.1.
18. Prove Theorem 2.2.
19. Show that for any range of $q_{0}$ and $q_{s}$, if $q_{s}>q_{0}$, the optimal number of parallel components that maximizes the system reliability is one.
20. Prove Theorem 2.3.
21. Prove Theorem 2.4.
22. Prove Theorem 2.5.23. Show that the optimal value $n^{*}$ in Theorem 2.5 is an increasing function of $q_{0}$ and a decreasing function of $q_{s}$.
24. Prove Theorem 2.6.
25. For any given $q_{0}$ and $q_{s}$, show that $q_{s}<\alpha<p_{0}$ where $\alpha$ is given in equation (2.73).
26. Prove Property 2.3.
27. Prove Property 2.4.
28. Prove Property 2.8 .
29. Events occur according to an NHPP in which the mean value function is

$$
m(t)=t^{3}+3 t^{2}+6 t \quad t>0
$$

What is the probability that $n$ events occur between times $t=10$ and $t=15$ ?# Theory of Estimation 

### 3.1 Point Estimation

The problem of point estimation is that of estimating the parameters of a population, e.g., $\lambda$ or $\theta$ from an exponential, $\mu$ and $\sigma^{2}$ from a normal, etc. It is assumed that the population distribution by type is known, but the distribution parameters are unknown and they have to be estimated by using collected failure data. This chapter is devoted to the theory of estimation and discusses several common estimation techniques such as maximum likelihood, least squared, and Bayesian methods. We also discuss the confidence interval estimates and tolerance limit estimates. For example, assume n independent samples from the exponential density $f(x ; \lambda)=\lambda e^{-\lambda x}$ for $x>0$ and $\lambda>0$, then the joint probability density function (pdf) or sample density (for short) is given by

$$
f\left(x_{1}, \lambda\right) \cdot f\left(x_{1}, \lambda\right) \cdots \cdot f\left(x_{1}, \lambda\right)=\lambda^{n} e^{-\lambda \sum_{i=1}^{N_{n}} x_{i}}
$$

The problem here is to find a "good" point estimate of $\lambda$ which is denoted by $\hat{\lambda}$. In other words, we shall find a function $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ such that, if $x_{1}, x_{2}, \ldots$, $x_{n}$ are the observed experimental values of $X_{1}, X_{2}, \ldots ., X_{n}$, then the value $h\left(x_{1}, x_{2}\right.$, $\left.\ldots ., x_{n}\right)$ will be a good point estimate of $\lambda$. By "good' we mean the following properties shall be implied:

- Unbiasedness
- Consistency
- Efficiency (i.e., minimum variance)
- Sufficiency

In other words, if $\hat{\lambda}$ is a good point estimate of $\lambda$, then one can select the function $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ such that $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is not only an unbiased estimator of $\lambda$ butalso the variance of $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is a minimum. We will now present the following definitions.

Definition 3.1: For a given positive integer $n$, the statistic $Y=h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is called an unbiased estimator of the parameter $\theta$ if the expectation of $Y$ is equal to a parameter $\theta$, that is,

$$
E(Y)=\theta
$$

Definition 3.2: The statistic $Y$ is called a consistent estimator of the parameter $\theta$ if $Y$ converges stochastically to a parameter $\theta$ as $n$ approaches infinity. If $\in$ is an arbitrarily small positive number when $Y$ is consistent, then

$$
\lim _{n \rightarrow \infty} P(|Y-\theta| \leq \in)=1
$$

Definition 3.3: The statistic $Y$ will be called the minimum variance unbiased estimator of the parameter $\theta$ if $Y$ is unbiased and the variance of $Y$ is less than or equal to the variance of every other unbiased estimator of $\theta$. An estimator that has the property of minimum variance in large samples is said to be efficient.

Definition 3.4: The statistic $Y$ is said to be sufficient for $\theta$ if the conditional distribution of $X$, given $Y=y$, is independent of $\theta$.

Definition 3.3 is useful in finding a lower bound on the variance of all unbiased estimators. We now establish a lower bound inequality known as the Cramér-Rao inequality.

Theorem 3.1 (Cramér-Rao inequality): Let $X_{1}, X_{2}, \ldots, X_{n}$ denote a random sample from a distribution with pdf $f(x ; \theta)$ for $\theta_{1}<\theta<\theta_{2}$, where $\theta_{1}$ and $\theta_{2}$ are known. Let $Y=\mathrm{h}\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ be an unbiased estimator of $\theta$. The lower bound inequality on the variance of $Y, \operatorname{Var}(Y)$, is given by

$$
\operatorname{Var}(Y) \geq \frac{1}{n E\left\{\left[\frac{\partial \ln f(x ; \theta)}{\partial \theta}\right]^{2}\right\}}
$$

Theorem 3.2: An estimator $\hat{\theta}$ is said to be asymptotically efficient if $\sqrt{n} \hat{\theta}$ has a variance that approaches the Cramér-Rao lower bound for large $n$, that is,

$$
\lim _{n \rightarrow \infty} \operatorname{Var}(\sqrt{n} \hat{\theta})=\frac{1}{n E\left\{\left[\frac{\partial \ln f(x ; \theta)}{\partial \theta}\right]^{2}\right\}}
$$

We now discuss some basic methods of parameter estimation.# 3.2 Maximum Likelihood Estimation Method 

The method of maximum likelihood estimation (MLE) is one of the most useful techniques for deriving point estimators. As a lead-in to this method, a simple example will be considered. The assumption that the sample is representative of the population will be exercised both in the example and later discussions.

Example 3.1: Consider a sequence of 25 Bernoulli trials (binomial situation) where each trial results in either success or failure. From the 25 trials, 6 failures and 19 successes result. Let $p$ be the probability of success, and $1-p$ the probability of failure. Find the estimator of $p, \hat{p}$, which maximizes that particular outcome.

The sample density function can be written as

$$
g(19)=\binom{25}{19} p^{19}(1-p)^{6}
$$

The maximum of $g(19)$ occurs when

$$
p=\hat{p}=\frac{19}{25}
$$

so that

$$
g\left(19 \mid p=\frac{19}{25}\right) \geq g\left(19 \mid p \neq \frac{19}{25}\right)
$$

Now $\mathrm{g}(19)$ is the probability or "likelihood" of 6 failures in a sequence of 25 trials. Select $p=\hat{p}=\frac{19}{25}$ as the probability or likelihood maximum value and, hence, $\hat{p}$ is referred to as the maximum likelihood estimate. The reason for maximizing $g(19)$ is that the sample contained six failures, and hence, if it is representative of the population, it is desired to find an estimate which maximizes this sample result. Just as $g(19)$ was a particular sample estimate, in general, one deals with a sample density:

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=f\left(x_{1} ; \theta\right) f\left(x_{2} ; \theta\right) \ldots . f\left(x_{n} ; \theta\right)
$$

where $x_{1}, x_{2}, \ldots, x_{n}$ are random, independent observation from a population with density function $f(x)$. For the general case, it is desired to find an estimate or estimates, $\hat{\theta}_{1}, \hat{\theta}_{2}, \ldots, \hat{\theta}_{m}$ (if such exist) where

$$
f\left(x_{1}, x_{2}, \ldots, x_{n} ; \theta_{1}, \theta_{2}, \ldots, \theta_{m}\right)>f\left(x_{1}, x_{2}, \ldots, x_{n} ; \theta_{1}^{\prime}, \theta_{2}^{\prime}, \ldots, \theta_{m}^{\prime}\right)
$$

Notation $\theta_{1}^{\prime}, \theta_{2}^{\prime}, \ldots, \theta_{n}^{\prime}$ refers to any other estimates different than $\hat{\theta}_{1}, \hat{\theta}_{2}, \ldots, \hat{\theta}_{m}$.

Let us now discuss the method of MLE. Consider a random sample $X_{1}, X_{2}, \ldots$, $X_{n}$ from a distribution having pdf $f(x ; \theta)$. This distribution has a vector $\theta=\left(\theta_{1}, \theta_{2}\right.$, $\ldots, \theta_{\mathrm{m}}$ )'of unknown parameters associated with it, where $m$ is the number of unknown parameters. Assuming that the random variables are independent, thenthe likelihood function, $\mathrm{L}(X ; \theta)$, is the product of the probability density function evaluated at each sample point:

$$
L(X, \theta)=\prod_{i=1}^{n} f\left(X_{i} ; \theta\right)
$$

where $\boldsymbol{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. The maximum likelihood estimator $\hat{\theta}$ is found by maximizing $L(\boldsymbol{X} ; \theta)$ with respect to $\theta$. In practice, it is often easier to maximize $\ln [L(\boldsymbol{X} ; \theta)]$ to find the vector of MLEs, which is valid because the logarithm function is monotonic. The log likelihood function is given by

$$
\ln L(X, \theta)=\sum_{i=1}^{n} \ln f\left(X_{i} ; \theta\right)
$$

and is asymptotically normally distributed since it consists of the sum of $n$ independent variables and the implication of the central limit theorem. Since $L(\mathrm{X}$; $\theta$ ) is a joint probability density function for $X_{1}, X_{2}, \ldots, X_{n}$, it must integrate equal to 1 , that is,

$$
\iint_{0}^{\infty} \int_{0}^{\infty} \cdots \int_{0}^{\infty} L(X ; \theta) d X=1
$$

Assuming that the likelihood is continuous, the partial derivative of the left-hand side with respect to one of the parameters, $\theta_{i}$, yields

$$
\begin{aligned}
\frac{\partial}{\partial \theta_{i}} \int_{0}^{\infty} \int_{0}^{\infty} \cdots \int_{0}^{\infty} L(X ; \theta) d X & =\int_{0}^{\infty} \int_{0}^{\infty} \cdots \int_{0}^{\infty} \frac{\partial}{\partial \theta_{i}} L(X ; \theta) d X \\
& =\int_{0}^{\infty} \int_{0}^{\infty} \cdots \int_{0}^{\infty} \frac{\partial \log L(X ; \theta)}{\partial \theta_{i}} L(X ; \theta) d X \\
& =E\left[\frac{\partial \log L(X ; \theta)}{\partial \theta_{i}}\right] \\
& =E\left[U_{i}(\theta)\right] \quad \text { for } i=1,2, \ldots, m
\end{aligned}
$$

where $\boldsymbol{U}(\theta)=\left(U_{1}(\theta), U_{2}(\theta), \ldots U_{n}(\theta)\right)^{\prime}$ is often called the score vector and the vector $\boldsymbol{U}(\theta)$ has components

$$
U_{i}(\theta)=\frac{\partial[\log L(X ; \theta)]}{\partial \theta_{i}} \quad \text { for } \quad i=1,2, \ldots, m
$$

which, when equated to zero and solved, yields the MLE vector $\theta$.
Suppose that we can obtain a non-trivial function of $X_{1}, X_{2}, \ldots, X_{n}$, say $h\left(X_{1}, X_{2}\right.$, $\left.\ldots, X_{n}\right)$, such that, when $\theta$ is replaced by $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$, the likelihood function $L$ will achieve a maximum. In other words,

$$
L(X, h(X)) \geq L(X, \theta)
$$for every $\theta$. The statistic $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is called a maximum likelihood estimator of $\theta$ and will be denoted as

$$
\hat{\theta}=h\left(x_{1}, x_{2}, \ldots, x_{n}\right)
$$

The observed value of $\hat{\theta}$ is called the MLE of $\theta$. In general, the mechanics for obtaining the MLE can be obtained as follows:

Step 1. Find the joint density function $L(X, \theta)$
Step 2. Take the natural $\log$ of the density In $L$
Step 3. Take the partial derivatives of In $L$ with respect to each parameter
Step 4. Set partial derivatives to "zero"
Step 5. Solve for parameter(s)
Example 3.2: Let $X_{1}, X_{2}, \ldots, X_{n}$ be a random sample from the exponential distribution with pdf

$$
f(x ; \lambda)=\lambda e^{-\lambda x} \quad x>0, \lambda>0
$$

The joint pdf of $X_{1}, X_{2}, \ldots, X_{n}$, is given by

$$
L(X, \lambda)=\lambda^{n} e^{-\lambda \sum_{i=1}^{n} x_{i}}
$$

and

$$
\ln L(X, \lambda)=n \ln \lambda-\lambda \sum_{i=1}^{n} x_{i}
$$

The function $\ln L$ can be maximized by setting the first derivative of $\ln L$, with respect to $\lambda$, equal to zero and solving the resulting equation for $\lambda$. Therefore,

$$
\frac{\partial \ln L}{\partial \lambda}=\frac{n}{\lambda}-\sum_{i=1}^{n} x_{i}=0
$$

This implies that

$$
\hat{\lambda}=\frac{n}{\sum_{i=1}^{n} x_{i}}
$$

The observed value of $\hat{\lambda}$ is the maximum likelihood estimate of $\lambda$.
Example 3.3: In an exponential censored case, the non-conditional joint pdf that $r$ items have failed is given by

$$
f\left(x_{1}, x_{2}, \ldots, x_{r}\right)=\lambda^{r} e^{-\lambda \sum_{i=1}^{r} x_{i}} \quad(r \text { failed items })
$$

and the probability distribution that $(n-r)$ items will survive is

$$
P\left(X_{r+1}>t_{1}, X_{r+2}>t_{2}, \ldots, X_{n}>t_{n-r}\right)=e^{-\lambda \sum_{i=1}^{n} t_{i}}
$$Thus, the joint density function is

$$
\begin{aligned}
L(X, \lambda) & =f\left(x_{1}, x_{2}, \ldots, x_{r}\right) P\left(X_{r+1}>t_{1}, \ldots, X_{n}>t_{n-r}\right) \\
& =\frac{n!}{(n-r)!} \lambda^{r} e^{-\lambda\left(\sum_{i=1}^{n} x_{i}+\sum_{j=1}^{n} t_{j}\right)}
\end{aligned}
$$

Let

$$
T=\sum_{i=1}^{r} x_{i}+\sum_{j=1}^{n-r} t_{j}
$$

then

$$
\ln L=\ln \left(\frac{n!}{(n-r)!}\right)+r \ln \lambda-\lambda T
$$

and

$$
\frac{\partial \ln L}{\partial \lambda}=\frac{r}{\lambda}-T=0
$$

Hence,

$$
\hat{\lambda}=\frac{r}{T}
$$

Note that with the exponential, regardless of the censoring type or lack of censoring, the MLE of $\lambda$ is the number of failures divided by the total operating time.

Example 3.4: Let $X_{1}, X_{2}, \ldots, X_{n}$ represent a random sample from the distribution with pdf

$$
f(x ; \theta)=e^{-(x-\theta)} \quad \text { for } \theta \leq x \leq \infty \quad \text { and }-\infty<\theta<\infty
$$

The likelihood function is given by

$$
\begin{aligned}
L(\theta ; X) & =\prod_{i=1}^{n} f\left(x_{i} ; \theta\right) \quad \text { for } \theta \leq x_{i} \leq \infty \text { all } i \\
& =\prod_{i=1}^{n} e^{-\left(x_{i}-\theta\right)}=e^{-\sum_{i=1}^{n} x_{i}+n \theta}
\end{aligned}
$$

For fixed values of $x_{1}, x_{2}, \ldots, x_{n}$, we wish to find that value of $\theta$ which maximizes $L(\theta, X)$. Here we cannot use the techniques of calculus to maximize $L(\theta, X)$. Note that $L(\theta, X)$ is largest when $\theta$ is as large as possible. However, the largest value of $\theta$ is equal to the smallest value of $X_{i}$ in the sample. Thus,

$$
\hat{\theta}=\min \left\{X_{i}\right\} \quad 1 \leq i \leq n
$$

Example 3.5: Let $X_{1}, X_{2}, \ldots, X_{n}$, denote a random sample from the normal distribution $N\left(\mu, \sigma^{2}\right)$. Then the likelihood function is given by$$
L\left(X, \mu, \sigma^{2}\right)=\left(\frac{1}{2 \pi}\right)^{\frac{n}{2}} \frac{1}{\sigma^{n}} e^{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}}
$$

and

$$
\ln L=-\frac{n}{2} \log (2 \pi)-\frac{n}{2} \log \sigma^{2}-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}
$$

Thus we have

$$
\begin{aligned}
& \frac{\partial \ln L}{\partial \mu}=\frac{1}{\sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)=0 \\
& \frac{\partial \ln L}{\partial \sigma^{2}}=-\frac{n}{2 \sigma^{2}}-\frac{1}{2 \sigma^{4}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}=0
\end{aligned}
$$

Solving the two equations simultaneously, we obtain

$$
\begin{aligned}
& \hat{\mu}=\frac{\sum_{i=1}^{n} x_{i}}{n} \\
& \hat{\sigma^{2}}=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}
\end{aligned}
$$

Note that the MLEs, if they exist, are both sufficient and efficient estimates. They also have an additional property called invariance, i.e., for an MLE of $\theta$, then $\mu(\theta)$ is the MLE of $\mu(\theta)$. However, they are not necessarily unbiased, i.e., $E(\hat{\theta})=$ $\theta$. The point in fact is $\sigma^{2}$ :

$$
E\left(\hat{\sigma}^{2}\right)=\left(\frac{n-1}{n}\right) \sigma^{2} \neq \sigma^{2}
$$

Therefore, for small $n, \sigma^{2}$ is usually adjusted for its bias and the best estimate of $\sigma^{2}$ is

$$
\hat{\sigma^{2}}=\left(\frac{1}{n-1}\right) \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}
$$

Sometimes it is difficult, if not impossible, to obtain maximum likelihood estimators in a closed form, and therefore numerical methods must be used to maximize the likelihood function. For illustration see the following example.

Example 3.6: Suppose that $X_{1}, X_{2}, \ldots, X_{n}$ is a random sample from the Weibull distribution with pdf

$$
f(x, \alpha, \lambda)=\alpha \lambda x^{\alpha-1} e^{-\lambda x^{\alpha}}
$$

The likelihood function is$$
L(X, \alpha, \lambda)=\alpha^{n} \lambda^{n} \prod_{i=1}^{n} x_{i}^{\alpha-1} e^{-\lambda \sum_{i=1}^{n} x_{i}^{\alpha}}
$$

Then

$$
\begin{aligned}
& \ln L=n \log \alpha+n \log \lambda+(\alpha-1) \sum_{i=1}^{n} \log x_{i}-\lambda \sum_{i=1}^{n} x_{i}^{\alpha} \\
& \frac{\partial \ln L}{\partial \alpha}=\frac{n}{\alpha}+\sum_{i=1}^{n} \log x_{i}-\lambda \sum_{i=1}^{n} x_{i}^{\alpha} \log x_{i}=0 \\
& \frac{\partial \ln L}{\partial \lambda}=\frac{n}{\lambda}-\sum_{i=1}^{n} x_{i}^{\alpha}=0
\end{aligned}
$$

As noted, solutions of the above two equations for $\alpha$ and $\lambda$ are extremely difficult and require either graphical or numerical methods.

Example 3.7: Let $X_{1}, X_{2}, \ldots, X_{n}$ be a random sample from the gamma distribution with pdf

$$
f(x, \lambda, \alpha)=\frac{\lambda^{(\alpha+1)} x^{\alpha} e^{-\lambda x}}{(\alpha!)^{n}}
$$

then the likelihood function and $\log$ of the likelihood function, respectively, are

$$
\begin{aligned}
& L(X, \lambda, \alpha)=\frac{\lambda^{n(\alpha+1)} \prod_{i=1}^{n} x_{i}^{\alpha} e^{-\lambda \sum_{i=1}^{n} x_{i}}}{(\alpha!)^{n}} \\
& \ln L=n(\alpha+1) \log \lambda+\alpha \sum_{i=1}^{n} \log x_{i}-\lambda \sum_{i=1}^{n} x_{i}-n \log (\alpha!)
\end{aligned}
$$

Taking the partial derivatives, we obtain

$$
\begin{aligned}
& \frac{\partial \ln L}{\partial \alpha}=n \log \lambda+\sum_{i=1}^{n} \log x_{i}-n \frac{\partial}{\partial \alpha}[\log \alpha!]=0 \\
& \frac{\partial \ln L}{\partial \lambda}=\frac{n(\alpha+1)}{\lambda}-\sum_{i=1}^{n} x_{i}=0
\end{aligned}
$$

The solutions of the two equations at equation (3.21) for $\alpha$ and $\lambda$ are extremely difficult and require either graphical or numerical methods.

Example 3.8: Let $t_{1}, t_{2}, \ldots, t_{n}$ be failure times of a random variable having the Pham distribution, also known as loglog distribution (Pham 2002a), with two parameters $a$ and $\alpha$ as follows (see also equation (2.21), Chapter 2):

$$
f(t)=\alpha \cdot \ln a \cdot t^{\alpha-1} \cdot a^{t^{\alpha}} \cdot e^{1-a^{t^{\alpha}}} \quad \text { for } t>0, \alpha>0, a>1
$$

From Chapter 2, equation (2.22), the Pham cumulative distribution function is given as follows:$$
F(t)=1-e^{1-a^{t^{\alpha}}}
$$

We now estimate the values of $a$ and $\alpha$ using the MLE method. From equation (3.22), the likelihood function is

$$
\begin{aligned}
L(a, \alpha) & =\prod_{i=1}^{n} \alpha \ln a \cdot t_{i}^{\alpha-1} e^{1-a^{t^{\alpha}}} a^{t^{\alpha}} \\
& =\alpha^{n}(\ln a)^{n}\left(\prod_{i=1}^{n} t_{i}\right)^{\alpha-1} a^{\sum_{i=1}^{n} t_{i}^{\alpha}} e^{n \cdot \sum_{i=1}^{n} a^{t^{\alpha}}}
\end{aligned}
$$

The $\log$ likelihood function is

$$
\begin{aligned}
\log L(a, \alpha)=n \log & \alpha+n \ln (\ln a)+(\alpha-1)\left(\sum_{i=1}^{n} \ln t_{i}\right) \\
& +\ln a \cdot \sum_{i=1}^{n} t_{i}^{\alpha}+n-\sum_{i=1}^{n} a^{t^{\alpha}}
\end{aligned}
$$

The first derivatives of the $\log$ likelihood function with respect to a and $\alpha$ are, respectively,

$$
\frac{\partial}{\partial a} \log L(a, \alpha)=\frac{n}{a \ln a}+\frac{1}{a} \cdot \sum_{i=1}^{n} t_{i}^{\alpha}-\sum_{i=1}^{n} t_{i}^{\alpha} a^{t^{\alpha}-1}
$$

and

$$
\begin{aligned}
\frac{\partial}{\partial \alpha} \log L(a, \alpha)= & \frac{n}{\alpha}+\sum_{i=1}^{n} \ln t_{i}+\ln a \cdot \sum_{i=1}^{n} \ln t_{i} \cdot t_{i}^{\alpha} \\
& -\sum_{i=1}^{n} t_{i}^{\alpha} \cdot a^{t^{\alpha}} \cdot \ln a \cdot \ln t_{i}
\end{aligned}
$$

Setting equations (3.25) and (3.26) equal to zero, we can obtain the MLE of $a$ and $\alpha$ by solving the following simultaneous equations:

$$
\begin{gathered}
\frac{n}{\ln a}+\sum_{i=1}^{n} t_{i}^{\alpha}-\sum_{i=1}^{n} t_{i}^{\alpha} a^{t^{\alpha}}=0 \\
\frac{n}{\alpha}+\sum_{i=1}^{n} \ln t_{i}+\ln a \cdot \sum_{i=1}^{n} \ln t_{i} \cdot t_{i}^{\alpha}\left(1-a^{t^{\alpha}}\right)=0
\end{gathered}
$$

After rearrangements, we obtain

$$
\begin{gathered}
\ln a \sum_{i=1}^{n} t_{i}^{\alpha}\left(a^{t^{\alpha}}-1\right)=n \\
\ln a \cdot \sum_{i=1}^{n} \ln t_{i} \cdot t_{i}^{\alpha} \cdot\left(a^{t^{\alpha}}-1\right)-\frac{n}{\alpha}=\sum_{i=1}^{n} \ln t_{i}
\end{gathered}
$$# 3.3 Maximum Likelihood Estimation with Censored Data 

Censored data arises when an individual's life length is known to occur only in a certain period of time. In other words, a censored observation contains only partial information about the random variable of interest. In this section, we consider two types of censoring. The first type is called Type-I censoring where the event is observed only if it occurs prior to some pre-specified time. The second type is Type-II censoring in which the study continues until the failure of the first $r$ units (or components), where $r$ is some predetermined integer $(r<n)$.

Examples of Type-II censoring are often used in testing of equipment life. Here items are put on test at the same time, and the test is terminated when $r$ of the $n$ items have failed. Such an experiment may, however, save time and resources because it could take a very long time for all items to fail. Both Type-I and Type-II censoring arise in many reliability applications.

For example, there is a batch of transistors or tubes; we put them all on test at $t=0$, and record their times to failure. Some transistors may take a long time to burn out, and we will not want to wait that long to end the experiment. Therefore, we might stop the experiment at a pre-specified time $t_{\mathrm{c}}$, in which case we have Type-I censoring, or we might not know beforehand what value of the fixed censoring time is good so we decide to wait until a pre-specified number of units have failed, $r$, of all the transistors has burned out, in which case we have Type-II censoring.

Censoring times may vary from individual to individual or from application to application. We now discuss a generalized censoring times case, call a multiplecensored data.

### 3.3.1 Parameter Estimate with Multiple-censored Data

The likelihood function for the multiple-censored data is given by

$$
L=f\left(t_{1, f}, \ldots, t_{r, f}, t_{1, s}, \ldots, t_{m, s}\right)=C \prod_{i=1}^{r} f\left(t_{i, f}\right) \prod_{j=1}^{m}\left[1-F\left(t_{j, s}\right)\right]
$$

where $C$ is a constant, $f($.$) is the density function and F($.$) is the distribution$ function. There are $r$ failure at times $t_{1, f}, \ldots, t_{r, f}$ and $m$ units with censoring times $t_{1, s}, \ldots, t_{m, s}$.

Note that this includes Type-I censoring by simply setting $t_{1, f}=t_{1, n}$ and $t_{1, s}=t_{0}$ in the likelihood function in equation (3.27). Also, the likelihood function for Type-II censoring is similar to Type-I censoring except $t_{1, s}=t_{\mathrm{r}}$ in equation (3.27). In other words, the likelihood function for the first $r$ observations from a sample size $n$ drawn from the model in both Type-I and Type-II censoring is given by

$$
L=f\left(t_{1, n}, \ldots, t_{r, n}\right)=C \prod_{i=1}^{r} f\left(t_{i, n}\right)\left[1-F\left(t_{*}\right)\right]^{n-r}
$$

where $t_{*}=t_{0}$, the time of cessation of the test for Type-I censoring and $t_{*}=t_{r}$, the time of the $r^{\text {th }}$ failure for Type-II censoring.Example 3.9: Consider a two-parameter probability density distribution with multiple-censored data and distribution function with failure rate bathtub shape, as given by (Chen 2000):

$$
f(t)=\lambda \beta t^{\beta-1} \exp \left[t^{\beta}+\lambda\left(1-e^{t^{\beta}}\right)\right] \quad t, \lambda, \beta>0
$$

and

$$
F(t)=1-\exp \left[\lambda\left(1-e^{t^{\beta}}\right)\right] \quad t, \lambda, \beta>0
$$

respectively.
Substituting the functions $f(t)$ and $F(t)$ in equations (3.29) and (3.30) into equation (3.28), we obtain the logarithm of the likelihood function:

$$
\begin{aligned}
\ln L= & \ln C+r \ln \lambda+r \ln \beta+\sum_{i=1}^{r}(\beta-1) \ln t_{i} \\
& +(m+r) \lambda+\sum_{i=1}^{r} t_{i}^{\beta}-\left[\sum_{i=1}^{r} \lambda e^{t_{i}^{\beta}}+\sum_{j=1}^{m} \lambda e^{t_{j}^{\beta}}\right]
\end{aligned}
$$

The function $\ln L$ can be maximized by setting the partial derivative of $\ln L$ with respect to $\lambda$ and $\beta$, equal to zero and solving the resulting equations simultaneously for $\lambda$ and $\beta$. Therefore, we obtain

$$
\begin{aligned}
\frac{\partial \ln L}{\partial \lambda}= & \frac{r}{\lambda}+(m+r)-\sum_{i=1}^{r} e^{t_{i}^{\beta}}-\sum_{j=1}^{m} e^{t_{j}^{\beta}} \equiv 0 \\
\frac{\partial \ln L}{\partial \beta}= & \frac{r}{\beta}+\sum_{i=1}^{r} \ln t_{i}+\sum_{i=1}^{r} t_{i}^{\beta} \ln t_{i} \\
& -\lambda\left[\sum_{i=1}^{r} e^{t_{i}^{\beta}} t_{i}^{\beta} \ln t_{i}+\sum_{j=1}^{m} e^{t_{j}^{\beta}} t_{j}^{\beta} \ln t_{j}\right] \equiv 0
\end{aligned}
$$

This implies that

$$
\hat{\lambda}=\frac{r}{\left(\sum_{i=1}^{r} e^{t_{i}^{\beta}}+\sum_{j=1}^{m} e^{t_{j}^{\beta}}\right)-m-r}
$$

and $\hat{\beta}$ is the solution of

$$
\begin{aligned}
& \frac{r}{\hat{\beta}}+\sum_{i=1}^{r} \ln t_{i}+\sum_{i=1}^{r} t_{i}^{\hat{\beta}} \ln t_{i}= \\
& \frac{r}{\left(\sum_{i=1}^{r} e^{t_{i}^{\beta}}+\sum_{j=1}^{m} e^{t_{j}^{\beta}}\right)-m-r}\left[\sum_{i=1}^{r} e^{t_{i}^{\beta}} t_{i}^{\hat{\beta}} \ln t_{i}+\sum_{j=1}^{m} e^{t_{j}^{\beta}} t_{j}^{\hat{\beta}} \ln t_{j}\right]
\end{aligned}
$$

We now discuss two special cases as follows.Case I: Type-I or Type-II Censoring Data.
From equation (3.28), the likelihood function for the first $r$ observations from a sample size $n$ drawn from the model in both Type-I and Type-II censoring is

$$
L=f\left(t_{1, n}, \ldots, t_{r, n}\right)=C \prod_{i=1}^{r} f\left(t_{i, n}\right)\left[1-F\left(t_{*}\right)\right]^{n-r}
$$

where $t_{*}=t_{0}$, the time of cessation of the test for Type-I censoring and $t_{*}=t_{e}$, the time of the $r^{\text {th }}$ failure for Type-II censoring equation (3.33) and (3.34) become

$$
\begin{gathered}
\hat{\lambda}=\frac{r}{\sum_{i=1}^{r} e^{t_{i}^{\hat{\beta}}}+(n-r) e^{t_{i}^{\hat{\beta}}}-n} \\
\frac{r}{\hat{\beta}}+\sum_{i=1}^{r} \ln t_{i}+\sum_{i=1}^{r} t_{i}^{\hat{\beta}} \ln t_{i}= \\
\frac{r}{\sum_{i=1}^{r} e^{t_{i}^{\hat{\beta}}}+(n-r) e^{t_{i}^{\hat{\beta}}}-n}\left[\sum_{i=1}^{r} e^{t_{i}^{\hat{\beta}}} t_{i}^{\hat{\beta}} \ln t_{i}+\sum_{j=1}^{m} e^{t_{i}^{\hat{\beta}}} t_{j}^{\hat{\beta}} \ln t_{j}\right]
\end{gathered}
$$

Case II: Complete Censored Data.
Simply replace $r$ with $n$ in equations (3.33) and (3.34) and ignore the $t_{j}$ portions. The maximum likelihood equations for the $\lambda$ and $\beta$ are given by

$$
\begin{gathered}
\hat{\lambda}=\frac{n}{\sum_{i=1}^{n} e^{t_{i}^{\hat{\beta}}}-n} \\
\frac{n}{\hat{\beta}}+\sum_{i=1}^{n} \ln t_{i}+\sum_{i=1}^{n} t_{i}^{\hat{\beta}} \ln t_{i}=\frac{n}{\sum_{i=1}^{n} e^{t_{i}^{\hat{\beta}}}-n} \times \sum_{i=1}^{n} e^{t_{i}^{\hat{\beta}}} t_{i}^{\hat{\beta}} \ln t_{i}
\end{gathered}
$$

# 3.3.2 Confidence Intervals of Estimates 

The asymptotic variance-covariance matrix of the parameters $(\lambda$ and $\beta$ ) is obtained by inverting the Fisher information matrix

$$
I_{i j}=E\left[-\frac{\partial^{2} L}{\partial \theta_{i} \partial \theta_{j}}\right], \quad i, j=1,2
$$

where $\theta_{1}, \theta_{2}=\lambda$ or $\beta$ (Nelson 1990). This leads to$$
\left[\begin{array}{cc}
\operatorname{Var}(\hat{\lambda}) & \operatorname{Cov}(\hat{\lambda}, \hat{\beta}) \\
\operatorname{Cov}(\hat{\lambda}, \hat{\beta}) & \operatorname{Var}(\hat{\beta})
\end{array}\right]=\left[\begin{array}{cc}
E\left(-\left.\frac{\partial^{2} \ln L}{\partial^{2} \lambda}\right|_{\hat{\lambda}, \hat{\beta}}\right) & E\left(-\left.\frac{\partial^{2} \ln L}{\partial \lambda \partial \beta}\right|_{\hat{\lambda}, \hat{\beta}}\right) \\
E\left(-\left.\frac{\partial^{2} \ln L}{\partial \beta \partial \lambda}\right|_{\hat{\lambda}, \hat{\beta}}\right) & E\left(-\left.\frac{\partial^{2} \ln L}{\partial^{2} \beta}\right|_{\hat{\lambda}, \hat{\beta}}\right)
\end{array}\right]
$$

We can obtain an approximate $(1-\alpha) 100 \%$ confidence intervals on parameter $\lambda$ and $\beta$ based on the asymptotic normality of the MLEs (Nelson 1990) as follows:

$$
\hat{\lambda} \pm Z_{\alpha / 2} \sqrt{\operatorname{Var}(\hat{\lambda})} \text { and } \hat{\beta} \pm Z_{\alpha / 2} \sqrt{\operatorname{Var}(\hat{\beta})}
$$

where $Z_{\alpha / 2}$ is upper percentile of standard normal distribution.

# 3.3.3 Applications 

Consider a helicopter main rotor blade part code xxx-015-001-107 based on the system database collected from October 1995 to September 1999 (Pham 2002a). The data set is shown in Table 3.1. In this application, we consider several distribution functions including Weibull, lognormal, normal, and loglog distribution functions.

From Example 3.8, the $\operatorname{loglog} \operatorname{pdf}$ (see equation 3.22) with parameters $a$ and $\alpha$ is

$$
f(t)=\alpha \cdot \ln a \cdot t^{\alpha-1} \cdot a^{t^{\alpha}} \cdot e^{1-a^{t^{\alpha}}} \quad \text { for } t>0, \alpha>0, a>1
$$

and its corresponding log likelihood function (see equation 3.24) is

$$
\begin{aligned}
\log L(a, \alpha)= & n \log \alpha+n \ln (\ln a)+(\alpha-1)\left(\sum_{i=1}^{n} \ln t_{i}\right) \\
& +\ln a \cdot \sum_{i=1}^{n} t_{i}^{\alpha}+n-\sum_{i=1}^{n} a^{t_{i}^{\alpha}}
\end{aligned}
$$

We next determine the confidence intervals for parameter estimates $a$ and $\alpha$. For the log-likelihood function given in equation (3.24), we can obtain the Fisher information matrix $H$ as $H=\left[\begin{array}{ll}h_{11} & h_{12} \\ h_{21} & h_{22}\end{array}\right] \quad$ where $h_{11}=E\left[-\frac{\partial^{2} \log L}{\partial a^{2}}\right]$

$$
\begin{gathered}
h_{12}=h_{21}=E\left[-\frac{\partial^{2} \log L}{\partial a \partial \alpha}\right] \\
h_{22}=E\left[-\frac{\partial^{2} \log L}{\partial \alpha^{2}}\right]
\end{gathered}
$$The variance matrix, $V$, can be obtained as follows:

$$
V=[H]^{-1}=\left[\begin{array}{ll}
v_{11} & v_{12} \\
v_{21} & v_{22}
\end{array}\right]
$$

The variances of $a$ and $\alpha$ are

$$
\operatorname{Var}(a)=v_{11} \quad \operatorname{Var}(\alpha)=v_{22}
$$

One can approximately obtain the $100(1-\beta) \%$ confidence intervals for $a$ and $\alpha$ based on the normal distribution as $\left[\hat{a}-z_{\frac{\beta}{2}} \sqrt{v_{11}}, \hat{a}+z_{\frac{\beta}{2}} \sqrt{v_{11}}\right]$ and $\left[\hat{\alpha}-z_{\frac{\beta}{2}} \sqrt{v_{22}}\right.$, $\left.\hat{\alpha}+z_{\frac{\beta}{2}} \sqrt{v_{22}}\right]$, respectively, where $v_{i j}$ is given in equation (3.42) and $\mathrm{z}_{\beta}$ is (1$\beta / 2) 100 \%$ of the standard normal distribution. After we obtain $\hat{a}$ and $\hat{\alpha}$, the MLE of reliability function can be computed as

$$
\hat{R}(t)=e^{1-\hat{a}^{2}}
$$

Let us define a partial derivative vector for reliability $R(t)$ as

$$
v[R(t)]=\left[\frac{\partial R(t)}{\partial a} \frac{\partial R(t)}{\partial \alpha}\right]
$$

then the variance of $R(t)$ can be obtained as follows:

$$
\operatorname{Var}[R(t)]=v[R(t)] \cdot V \cdot(v[R(t)])^{T}
$$

where V is given in equation (3.42).
One can approximately obtain the $(1-\beta) 100 \%$ confidence interval for $R(t)$ as

$$
\left[\hat{R}(t)-z \beta \sqrt{\operatorname{Var}[R(t)]}, \hat{R}(t)+z \beta \sqrt{\operatorname{Var}[R(t)]}\right]
$$

The MLE parameter estimations of Pham distribution using the data set in Table 3.1 are given as follows:

$$
\begin{array}{ll}
\hat{\alpha}=1.1075 & \operatorname{Var}[\hat{\alpha}]=0.0162 \\
95 \% \text { CI for } \hat{\alpha}: & {[0.8577,1.3573] } \\
\hat{a}=1.0002 & \operatorname{Var}[\hat{a}]=2.782 e^{-8} \\
95 \% \text { CI for a: } & {[0.9998,1.0005] }
\end{array}
$$

MTTF $=1608.324$
$\operatorname{MRL}(\mathrm{t}=\mathrm{MTTF})=950.475$
Substituting $a=1.0002$ and $\alpha=1.1075$ into the equation for $\mathrm{R}(\mathrm{t})$ yields the results in Table 3.2. Figure 3.1 shows the reliability comparisons between the normalmodel, the lognormal model, the Weibull model and the loglog model for the main rotor blade data set.

Table 3.1. Main rotor blade data (hour)

| 1634.3 | 2094.3 | 3318.2 |
| --: | --: | --: |
| 1100.5 | 2166.2 | 2317.3 |
| 1100.5 | 2956.2 | 1081.3 |
| 819.9 | 795.5 | 1953.5 |
| 1398.3 | 795.5 | 2418.5 |
| 1181 | 204.5 | 1485.1 |
| 128.7 | 204.5 | 2663.7 |
| 1193.6 | 1723.2 | 1778.3 |
| 254.1 | 403.2 | 1778.3 |
| 3078.5 | 2898.5 | 2943.6 |
| 3078.5 | 2869.1 | 2260 |
| 3078.5 | 26.5 | 2299.2 |
| 26.5 | 26.5 | 1655 |
| 26.5 | 3180.6 | 1683.1 |
| 3265.9 | 644.1 | 1683.1 |
| 254.1 | 1898.5 | 2751.4 |
| 2888.3 | 3318.2 |  |
| 2080.2 | 1940.1 |  |

# 3.4 Statistical Change-point Estimation Methods 

The change-point problem has been widely studied in reliability applications such as biological sciences, survival analysis, and environmental statistics.

Assume there is a sequence of random variables $X_{1}, X_{2}, \ldots, X_{n}$, that represent the inter-failure times and exists an index change-point $\tau$, such that $X_{1}, X_{2}, \ldots, X_{\tau}$ have a common distribution $F$ with density function $f(t)$ and $X_{\tau+1}, X_{\tau+2}, \ldots, X_{n}$ have the distribution G with density function $g(t)$, where $F \neq G$. Consider the following assumptions:

1. There is a finite unknown number of units, $N$, to put under the test.
2. At the beginning, all of the units have the same lifetime distribution $F$. After $\tau$ failures are observed, the remaining $(N-\tau)$ items have the distribution $G$. The change-point $\tau$ is assumed unknown.3. The sequence $\left\{X_{1}, X_{2}, \ldots, X_{r}\right\}$ is statistically independent of the sequence $\left\{X_{r+1}, X_{r+2}, \ldots, X_{n}\right\}$.
4. The lifetime test is performed according to the Type-II censoring plan in which the number of failures, $n$, is pre-determined.

Table 3.2. Reliability of a main rotor blade for various mission time $t$ (hour)

| Time | Reliability | Time | Reliability |
| :--: | :--: | :--: | :--: |
| 10 | 0.9974 | 450 | 0.8274 |
| 20 | 0.9945 | 500 | 0.8063 |
| 30 | 0.9914 | 600 | 0.7637 |
| 40 | 0.9881 | 700 | 0.7209 |
| 50 | 0.9848 | 800 | 0.6781 |
| 100 | 0.9672 | 900 | 0.6354 |
| 150 | 0.9486 | 1000 | 0.5931 |
| 200 | 0.9294 | 1500 | 0.3939 |
| 250 | 0.9096 | 2000 | 0.2292 |
| 300 | 0.8895 | 2500 | 0.1122 |
| 350 | 0.8690 | 3000 | 0.0436 |
| 400 | 0.8483 | 3500 | 0.0125 |



Figure 3.1. Reliability comparisons for a main rotor blade data set

Note that in hardware reliability testing, the total number of units to put on the test $N$ can be determined in advance. But in software, the parameter $N$ can be defined as the initial number of faults, and therefore it makes more sense for it to be an unknown parameter. Let $T_{1}, T_{2}, \ldots, T_{n}$ be the arrival times of sequential failures.Then

$$
\begin{aligned}
T_{1} & =X_{1} \\
T_{2} & =X_{1}+X_{2} \\
& \vdots \\
T_{n} & =X_{1}+X_{2}+\ldots X_{n}
\end{aligned}
$$

The failure times $T_{1}, T_{2}, \ldots, T_{r}$ are the first $\tau$ order statistics of a sample of size $N$ from the distribution $F$. The failure times $T_{\tau+1}, T_{\tau+2}, \ldots, T_{n}$ are the first $(n-\tau)$ order statistics of a sample of size $(N-\tau)$ from the distribution $G$.

Example 3.10: The Weibull change-point model of given life time distributions $F$ and $G$ with parameters $\left(\lambda_{1}, \beta_{1}\right)$ and $\left(\lambda_{2}, \beta_{2}\right)$, respectively, can be expressed as follows:

$$
\begin{gathered}
F(t)=1-\exp \left(-\lambda_{1} t^{\beta_{1}}\right) \\
G(t)=1-\exp \left(-\lambda_{2} t^{\beta_{2}}\right)
\end{gathered}
$$

Assume that the distributions belong to parametric families $\left\{F\left(t \mid \theta_{1}\right), \theta_{1} \in \Theta_{1}\right\}$ and $\left\{G\left(t \mid \theta_{2}\right), \theta_{2} \in \Theta_{2}\right\}$. Assume $T_{1}, T_{2}, \ldots, T_{r}$ are the first $\tau$ order statistics of a sample with size $N$ from the distribution $\left\{F\left(t \mid \theta_{1}\right), \theta_{1} \in \Theta_{1}\right\}$ and $T_{\tau+1}, T_{\tau+2}, \ldots, T_{n}$ are the first $(n-\tau)$ order statistics of a sample of size $(N-\tau)$ from the distribution $\left\{G\left(t \mid \theta_{2}\right), \theta_{2} \in \Theta_{2}\right\}$ where $N$ is unknown. The log likeli-hood function can be expressed as follows (Zhao 2003):

$$
\begin{aligned}
L\left(\tau, N, \theta_{1}, \theta_{2} \mid T_{1}, T_{2}, \ldots, T_{n}\right)= & \sum_{i=1}^{n}(N-i+1)+\sum_{i=1}^{\tau} f\left(T_{i} \mid \theta_{1}\right) \\
& +\sum_{i=\tau+1}^{n} g\left(T_{i} \mid \theta_{2}\right)+(N-\tau) \log \left(1-F\left(T_{\tau} \mid \theta_{1}\right)\right) \\
& +(N-n) \log \left(1-G\left(T_{n} \mid \theta_{2}\right)\right)
\end{aligned}
$$

If the parameter $N$ is known where hardware reliability is commonly considered, then the likelihood function is given by

$$
\begin{aligned}
L\left(\tau, \theta_{1}, \theta_{2} \mid T_{1}, T_{2}, \ldots, T_{n}\right)= & \sum_{i=1}^{\tau} f\left(T_{i} \mid \theta_{1}\right)+\sum_{i=\tau+1}^{n} g\left(T_{i} \mid \theta_{2}\right) \\
& +(N-\tau) \log \left(1-F\left(T_{\tau} \mid \theta_{1}\right)\right)+(N-n) \log \left(1-G\left(T_{n} \mid \theta_{2}\right)\right)
\end{aligned}
$$

The maximum likelihood estimator (MLE) of the change-point value $\hat{\tau}$ and $\left(\hat{N}, \hat{\theta}_{1}, \hat{\theta}_{2}\right)$ can be obtained by taking partial derivatives of the $\log$ likelihoodfunction in equation (3.47) with respect to the unknown parameters that maximizes the function. It should be noted that there is no closed form for $\hat{\tau}$ but it can be obtained by calculating the log likelihood for each possible value of $\tau$, $1 \leq \tau \leq(n-1)$, and selecting as $\hat{\tau}$ the value that maximizes the log-likelihood function.

# 3.4.1 Application: A Software Model with a Change Point 

In this application we examine the case where the sample size $N$ is unknown. Consider a software reliability model developed by Jelinski and Moranda (1972), often called the Jelinski-Moranda model. The assumptions of the model are as follows:

1. There are $N$ initial faults in the program.
2. A detected fault is removed instantaneously and no new fault is introduced.
3. Each failure caused by a fault occurs independently and randomly in time according to an exponential distribution.
4. The functions $F$ and $G$ are exponential distributions with failure rate parameters $\lambda_{1}$ and $\lambda_{2}$, respectively.

Based on the assumptions, the inter-failure times $X_{1}, X_{2}, \ldots, X_{n}$ are independently exponentially distributed. Specifically, $X_{i}=T_{i}-T_{i-1}, i=1,2, \ldots \tau$, are exponentially distributed with parameter $\lambda_{1}(N-i+1)$ where $\lambda_{1}$ is the initial fault detection rate of the first $\tau$ failures and $X_{j}=T_{j}-T_{j-1}, j=\tau+1, \tau+2, \ldots n$, are exponentially distributed with parameter $\lambda_{2}(N-\tau-j+1)$ where $\lambda_{2}$ is the fault detection rate of the first $n-\tau$ failures. If $\lambda_{1}=\lambda_{2}$ it means that each fault removal is the same and the change-point model becomes the Jelinski-Moranda software reliability model (Jelinski and Moranda 1972).

The MLEs of the parameters $\left(\tau, N, \lambda_{1}, \lambda_{2}\right)$ can be obtained by solving the following equations simultaneously:

$$
\begin{gathered}
\hat{\lambda}_{1}=\frac{\tau}{\sum_{i=1}^{\tau}(\hat{N}-i+1) x_{i}} \\
\hat{\lambda}_{2}=\frac{(n-\tau)}{\sum_{i=\tau+1}^{n}(\hat{N}-i+1) x_{i}} \\
\sum_{i=1}^{n} \frac{1}{(\hat{N}-i+1)}=\hat{\lambda}_{1} \sum_{i=1}^{\tau} x_{i}+\hat{\lambda}_{2} \sum_{i=\tau+1}^{n} x_{i}
\end{gathered}
$$To illustrate the model, we use the data set as in Table 3.3 to obtain the unknown parameters $\left(\tau, N, \lambda_{1}, \lambda_{2}\right)$ using equations (3.48)-(3.50). The data in Table 3.3 (Musa et al.1987) shows the successive inter-failure times for a real-time command and control system.

The table reads from left to right in rows, and the recorded times are execution times, in seconds. There are 136 failures in total. Figure 3.2 plots the log-likelihood function vs number of failures. The MLEs of the parameters $\left(\tau, N, \lambda_{1}, \lambda_{2}\right)$ with one change-point are given by

$$
\hat{\tau}=16, \hat{N}=145, \hat{\lambda}_{1}=1.1 \times 10^{-4}, \hat{\lambda}_{2}=0.31 \times 10^{-4}
$$

If we do not consider a change-point in the model, the MLEs of the parameters $N$ and $\lambda$ can be given as

$$
\hat{N}=142, \hat{\lambda}=0.35 \times 10^{-4}
$$

From Figure 3.2, we can observe that it is worth considering the change-points in the reliability functions.

Table 3.3. Successive inter-failure times (in seconds) for a real-time command system

| 3 | 30 | 113 | 81 | 115 | 9 | 2 | 91 | 112 | 15 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 13850 | 77 | 24 | 108 | 88 | 670 | 120 | 26 | 114 |  |
| 32555 | 242 | 68 | 422 | 180 | 10 | 1146 | 600 | 15 |  |
| 36 | 4 | 0 | 8 | 227 | 65 | 176 | 58 | 457 | 300 |
| 97 | 263 | 452 | 255 | 197 | 193 | 6 | 79 | 816 | 1351 |
| 14821 | 233 | 134 | 357 | 193 | 236 | 31 | 369 | 748 |  |
| 0 | 232 | 330 | 365 | 1222 | 543 | 10 | 16 | 529 | 379 |
| 44 | 129 | 810 | 290 | 300 | 529 | 281 | 160 | 828 | 1011 |
| 445296 | 1755 | 1064 | 1783 | 860 | 983 | 707 | 33 | 868 |  |
| 7242323 | 2930 | 1461 | 843 | 12 | 261 | 1800 | 865 | 1435 |  |
| 30 | 143 | 108 | 0 | 3110 | 1247 | 943 | 700 | 875 | 245 |
| 7291897 | 447 | 386 | 446 | 122 | 990 | 948 | 1082 | 22 |  |
| 75 | 482 | 5509 | 100 | 10 | 1071 | 371 | 790 | 6150 | 3321 |
| 1045 | 648 | 5485 | 1160 | 1864 | 4116 |  |  |  |  |

Figure 3.2. The log-likelihood function versus the number of failures

# 3.5 Goodness of Fit Techniques 

The problem at hand is to compare some observed sample distribution with a theoretical distribution. Two common techniques that will be discussed are the $\chi^{2}$ goodness-of-fit test and the Kolmogorov-Smirnov " $d$ " test.

### 3.5.1 Chi-squared Test

The following statistic

$$
\chi^{2}=\sum_{i=1}^{k}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{2}
$$

has a chi-squared $\left(\chi^{2}\right)$ distribution with $k$ degrees of freedom. The steps of chisquared test are as follows:

1. Divide the sample data into the mutually exclusive cells (normally 8-12) such that the range of the random variable is covered.
2. Determine the frequency, $f_{i}$, of sample observations in each cell.
3. Determine the theoretical frequency, $F_{i}$, for each cell (area under density function between cell boundaries $X_{n}$ - total sample size). Note that the theoretical frequency for each cell should be greater than 1 . To carry out this step, it normally requires estimates of the population parameters which can be obtained from the sample data.4. Form the statistic

$$
S=\sum_{i=1}^{k} \frac{\left(f_{i}-F_{i}\right)^{2}}{F_{i}}
$$

5. From the $\chi^{2}$ tables, choose a value of $\chi^{2}$ with the desired significance level and with degrees of freedom $(=k-1-r)$, where $r$ is the number of population parameters estimated.
6. Reject the hypothesis that the sample distribution is the same as theoretical distribution if

$$
S>\chi_{1-\alpha, k-1-r}^{2}
$$

where $\alpha$ is called the significance level.
Example 3.11: Given the data in Table 3.4, can the data be represented by the exponential distribution with a significance level of $\alpha$ ?
From the above calculation, $\hat{\lambda}=0.00263, R_{i}=e^{-\lambda t_{i}}$ and $Q_{i}=1-R_{i}$. Given that a value of significance level $\alpha$ is 0.1 , from equation (3.52) we obtain

$$
S=\sum_{i=1}^{11} \frac{\left(f_{i}-F_{i}\right)^{2}}{F_{i}}=6.165
$$

From Table A1.3 in Appendix 1, the value of $\chi^{2}$ with nine degrees of freedom is 14.68 , that is,

$$
\chi_{9 d f}^{2}(.90)=14.68
$$

Table 3.4. Sample observations in each cell boundary

| Cell boundaries | $f_{1}$ | $Q_{1}=(1-\mathrm{Ri}) 60$ | $F_{1}=Q_{1}-Q_{1-1}$ |
| :--: | :--: | :--: | :--: |
| $0-100$ | 10 | 13.86 | 13.86 |
| $100-200$ | 9 | 24.52 | 10.66 |
| $200-300$ | 8 | 32.71 | 8.19 |
| $300-400$ | 8 | 39.01 | 6.30 |
| $400-500$ | 7 | 43.86 | 4.85 |
| $500-600$ | 6 | 47.59 | 3.73 |
| $600-700$ | 4 | 50.45 | 2.86 |
| $700-800$ | 4 | 52.66 | 2.21 |
| $800-900$ | 2 | 54.35 | 1.69 |
| $900-1,000$ | 1 | 55.66 | 1.31 |
| $>1,000$ | 1 | 58.83 | 2.17 |

Since $S=6.165<14.68$, we would not reject the hypothesis of exponential with $\lambda=0.00263$. If in the following statistic

$$
S=\sum_{i=1}^{k}\left(\frac{f_{i}-F_{i}}{\sqrt{F_{i}}}\right)^{2}, \quad\left(\frac{f_{i}-F_{i}}{\sqrt{F_{i}}}\right)
$$

is approximately normal for large samples, then $S$ also has a $\chi^{2}$ distribution. This is the basis for the goodness of fit test.# 3.5.2 Kolmogorov-Smirnov $d$ Test 

Both the $\chi^{2}$ and " $d$ " tests are non-parameters. However, the $\chi^{2}$ assumes large sample normality of the observed frequency about its mean while the " $d$ " only assumes a continuous distribution. Let $X_{1} \leq X_{2} \leq X_{3} \leq \ldots \leq X_{n}$ denote the ordered sample values. Define the observed distribution function, $F_{n}(x)$, as follows:

$$
F_{n}(X)= \begin{cases}0 & \text { for } x \leq x_{1} \\ \frac{i}{n} & \text { for } x_{i}<x \leq x_{i+1} \\ 1 & \text { for } x>x_{n}\end{cases}
$$

Assume the testing hypothesis

$$
H_{0}: F(x)=F_{0}(x)
$$

where $F_{0}(x)$ is a given continuous distribution and $F(x)$ is an unknown distribution. Let

$$
d_{n}=\sup _{-\infty<x<\infty}\left|F_{n}(x)-F_{0}(x)\right|
$$

Since $F_{0}(x)$ is a continuous increasing function, we can evaluate $\left|F_{n}(x)-F_{0}(x)\right|$ for each $n$. If $d_{n} \leq d_{n+\alpha}$ then we would not reject the hypothesis $\mathrm{H}_{0}$; otherwise, we would reject it when $d_{n}>d_{n+\alpha}$. The value $d_{n+\alpha}$ can be found in Table A1.4 in Appendix 1, where $n$ is the sample size and $a$ is the level of significance.

### 3.6 Least Squared Estimation

A problem of curve fitting, which is unrelated to normal regression theory and MLE estimates of coefficients but uses identical formulas, is called the method of least squares. This method is based on minimizing the sum of the squared distance from the best fit line and the actual data points. It just so happens that finding the MLEs for the coefficients of the regression line also involves these sums of squared distances.

## Normal Linear Regression

Regression considers the distributions of one variable when another is held fixed at each of several levels. In the bivariate normal case, consider the distribution of $X$ as a function of given values of $Z$ where $X=\alpha+\beta Z$. Consider a sample of $n$ observations $\left(x_{i}, z_{i}\right)$, we can obtain the likelihood and its natural log for the normal distribution as follows:

$$
\begin{aligned}
& f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\frac{1}{2 \pi^{5}}\left(\frac{1}{\sigma^{2}}\right)^{\frac{n}{2}} e^{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\alpha-\beta z_{i}\right)^{2}} \\
& \ln L=-\frac{n}{2} \log 2 \pi-\frac{n}{2} \log \sigma^{2}-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\alpha-\beta z_{i}\right)^{2}
\end{aligned}
$$Taking the partial derivatives of $\ln L$ with respect to $\alpha$ and $\beta$, we have

$$
\begin{aligned}
& \frac{\partial \ln L}{\partial \alpha}=\sum_{i=1}^{n}\left(x_{i}-\alpha-\beta z_{i}\right)^{2}=0 \\
& \frac{\partial \ln L}{\partial \beta}=\sum_{i=1}^{n} z_{i}\left(x_{i}-\alpha-\beta z_{i}\right)=0
\end{aligned}
$$

The solution of the simultaneous equations is

$$
\begin{aligned}
& \hat{\alpha}=\bar{X}-\beta \bar{Z} \\
& \hat{\beta}=\frac{\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)\left(Z_{i}-\bar{Z}\right)}{\sum_{i=1}^{n}\left(Z_{i}-\bar{Z}\right)^{2}}
\end{aligned}
$$

# Least Squared Straight Line Fit 

Assume there is a linear relationship between $X$ and $E(Y \mid x)$, that is, $E(Y \mid x)=a+b x$. Given a set of data, we want to estimate the coefficients $a$ and $b$ that minimize the sum of the squares. Suppose the desired polynomial, $p(x)$, is written as

$$
\sum_{i=0}^{m} a_{i} x^{i}
$$

where $a_{0}, a_{1}, \ldots, a_{m}$ are to be determined. The method of least squares chooses as "solutions" those coefficients minimizing the sum of the squares of the vertical distances from the data points to the presumed polynomial. This means that the polynomial termed "best" is the one whose coefficients minimize the function $L$, where

$$
L=\sum_{i=1}^{n}\left[y_{i}-p\left(x_{i}\right)\right]^{2}
$$

Here, we will treat only the linear case, where $X=\alpha+\beta Z$. The procedure for higher-order polynomials is identical, although the computations become much more tedious. Assume a straight line of the form $X=\alpha+\beta Z$. For each observation $\left(x_{i}, z_{i}\right): X_{i}=\alpha+\beta Z_{i}$, let

$$
Q=\sum_{i=1}^{n}\left(x_{i}-\alpha-\beta z_{i}\right)^{2}
$$

We wish to find $\alpha$ and $\beta$ estimates such as to minimize $Q$. Taking the partial differentials, we obtain

$$
\begin{aligned}
& \frac{\partial Q}{\partial \alpha}=-2 \sum_{i=1}^{n}\left(x_{i}-\alpha-\beta z_{i}\right)=0 \\
& \frac{\partial Q}{\partial \beta}=-2 \sum_{i=1}^{n} z_{i}\left(x_{i}-\alpha-\beta z_{i}\right)=0
\end{aligned}
$$

Note that the above are the same as the MLE equations for normal linear regression. Therefore, we obtain the following results:$$
\begin{aligned}
& \hat{\alpha}=\bar{x}-\beta \bar{z} \\
& \hat{\beta}=\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(z_{i}-\bar{z}\right)}{\sum_{i=1}^{n}\left(z_{i}-\bar{z}\right)^{2}}
\end{aligned}
$$

The above gives an example of least squares applied to a linear case. It follows the same pattern for higher-order curves with solutions of 3,4, and so on, from the linear systems of equations.

# 3.7 Interval Estimation 

A point estimate is sometimes inadequate in providing an estimate of an unknown parameter since it rarely coincides with the true value of the parameter. An alternative way is to obtain a confidence interval estimation of the form $\left[\theta_{L}, \theta_{U}\right]$ where $\theta_{L}$ is the lower bound and $\theta_{U}$ is the upper bound.

Point estimates can become more useful if some measure of their error can be developed, i.e., some sort of tolerance on their high and low values could be developed. Thus, if an interval estimator is $\left[\theta_{L}, \theta_{U}\right]$ with a given probability (1- $\alpha$ ), then $\theta_{L}$ and $\theta_{U}$ will be called $100(1-\alpha) \%$ confidence limits for the given parameter $\theta$ and the interval between them is a $100(1-\alpha) \%$ confidence interval and $(1-\alpha)$ is also called the confidence coefficient.

### 3.7.1 Confidence Intervals for the Normal Parameters

The one-dimensional normal distribution has two parameters: mean $\mu$ and variance $\sigma^{2}$. The simultaneous employment of both parameters in a confidence statement concerning percentages of the population will be discussed in the next section on tolerance limits. Hence, individual confidence statements about $\mu$ and $\sigma^{2}$ will be discussed here.

## Confidence Limits for the Mean $\mu$ with Known $\sigma^{2}$

It is easy to show that the statistic

$$
Z=\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}
$$

is a standard normal distribution where

$$
\bar{X}=\frac{1}{n} \sum_{i=1}^{n} X_{i}
$$

Hence, a $100(1-\alpha) \%$ confidence interval for the mean $\mu$ is given by$$
P\left[\bar{X}-Z_{\frac{\sigma}{\sqrt{n}}}<\mu<\bar{X}+Z_{\frac{\sigma}{\sqrt{n}}}\right]=1-\alpha
$$

In other words,

$$
\mu_{L}=\bar{X}-Z_{\frac{\sigma}{\sqrt{n}}} \quad \text { and } \quad \mu_{U}=\bar{X}+Z_{\frac{\sigma}{\sqrt{n}}}
$$

Example 3.12: Draw a sample of size 4 from a normal distribution with known variance $=9$, say $x_{1}=2, x_{2}=3, x_{3}=5, x_{4}=2$. Determine the location of the true mean $(\mu)$. The sample mean can be calculated as

$$
\bar{x}=\frac{\sum_{i=1}^{n} x_{i}}{n}=\frac{2+3+5+2}{4}=3
$$

Assuming that $\alpha=0.05$ and from the standard normal distribution (Table A1.1 in Appendix 1), we obtain

$$
\begin{aligned}
P\left[3-1.96 \frac{3}{\sqrt{4}}<\mu<3+1.96 \frac{3}{\sqrt{4}}\right] & =0.95 \\
P[0.06<\mu<5.94] & =0.95
\end{aligned}
$$

This example shows that there is a $95 \%$ probability that the true mean is somewhere between 0.06 and 5.94 . Now, $\mu$ is a fixed parameter and does not vary, so how do we interpret the probability? If the samples of size 4 are repeatedly drawn, a different set of limits would be constructed each time. With this as the case, the interval becomes the random variable and the interpretation is that, for $95 \%$ of the time, the interval so constructed will contain the true (fixed) parameter.

# Confidence Limits for the Mean $\mu$ with Unknown $\sigma^{2}$ 

Let

$$
S=\sqrt{\frac{1}{n-1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}}
$$

It can be shown that the statistic

$$
T=\frac{\bar{X}-\mu}{\frac{S}{\sqrt{n}}}
$$

has a $t$ distribution with ( $n-1$ ) degrees of freedom (see Table A1.2 in Appendix 1). Thus, for a given sample mean and sample standard deviation, we obtain

$$
P\left[|T|<t_{\frac{\sigma}{\sqrt{n}}, n-1}\right]=1-\alpha
$$

Hence, a $100(1-\alpha) \%$ confidence interval for the mean $\mu$ is given by

$$
P\left[\bar{X}-t_{\frac{\sigma}{\sqrt{n}}, n-1} \frac{S}{\sqrt{n}}<\mu<\bar{X}+t_{\frac{\sigma}{\sqrt{n}}, n-1} \frac{S}{\sqrt{n}}\right]=1-\alpha
$$Example 3.13: A problem on the variability of a new product was encountered. An experiment was run using a sample of size $n=25$; the sample mean was found to be $\bar{X}=50$ and the variance $\sigma^{2}=16$. From Table A1.2 in Appendix 1, $t_{\frac{\alpha}{2}, n-1}=t_{975,24}$ $=2.064$. A $95 \%$ confidence limit for $\mu$ is given by

$$
\begin{aligned}
P\left[50-2.064 \sqrt{\frac{16}{25}}<\mu<50+2.064 \sqrt{\frac{16}{25}}\right] & =0.95 \\
P[48.349<\mu<51.651] & =0.95
\end{aligned}
$$

Note that, for one-sided limits, choose $t_{\sigma}$, or $t_{1-\alpha}$.

# Confidence Limits on $\sigma^{2}$ 

Note that $n \frac{\bar{\sigma}^{2}}{\sigma^{2}}$ has a $\chi^{2}$ distribution with $(n-1)$ degrees of freedom. Correcting for the bias in $\hat{\sigma^{2}}$, then $(n-1) \sigma^{\hat{2}} / \sigma^{2}$ has this same distribution. Hence,

$$
P\left[\chi_{\frac{\alpha}{2}, n-1}^{2}<\frac{(n-1) S^{2}}{\sigma^{2}}<\chi_{1-\frac{\alpha}{2}, n-1}^{2}\right]=1-\alpha
$$

or

$$
P\left[\frac{\sum\left(x_{i}-\bar{x}\right)^{2}}{\chi_{1-\frac{\alpha}{2}, n-1}^{2}}<\sigma^{2}<\frac{\sum\left(x_{i}-\bar{x}\right)^{2}}{\chi_{\frac{\alpha}{2}, n-1}^{2}}\right]=1-\alpha
$$

Similarly, for one-sided limits, choose $\chi^{2}(\alpha)$ or $\chi^{2}(1-\alpha)$.

### 3.7.2 Confidence Intervals for the Exponential Parameters

The pdf and cdf of the exponential distribution are given as

$$
f(x)=\lambda e^{-\lambda x} \quad x>0, \lambda>0
$$

and

$$
F(x)=1-e^{-\lambda x}
$$

respectively. From equation (3.16), it was shown that the distribution of a function of the estimate

$$
\hat{\lambda}=\frac{r}{\sum_{i=1}^{n} x_{i}+(n-r) x_{r}}
$$

derived from a test of $n$ identical components with common exponential failure density (failure rate $\lambda$ ), whose testing was stopped after the $r$ th failure, was chi-squared $\left(\chi^{2}\right)$, i.e.,

$$
2 r \frac{\lambda}{\hat{\lambda}}=2 \lambda T \quad\left(\chi^{2} \text { distribution with } 2 r \text { degrees of freedom }\right)
$$where $T$ is the total accrued time on all units. Knowing the distribution of $2 \lambda T$ allows us to obtain the confidence limits on the parameter as follows:

$$
P\left[\chi_{1-\frac{\alpha}{2}, 2 r}^{2}<2 \lambda T<\chi_{2,2 r}^{2}\right]=1-\alpha
$$

or, equivalently, that

$$
P\left[\frac{\chi_{1-\frac{\alpha}{2}, 2 r}^{2}}{2 T}<\lambda<\frac{\chi_{2,2 r}^{2}}{2 T}\right]=1-\alpha
$$

This means that in $(1-\alpha) \%$ of samples with a given size $n$, the random interval

$$
\left(\frac{\chi_{1-\frac{\alpha}{2}, 2 r}^{2}}{2 T}, \frac{\chi_{2,2 r}^{2}}{2 T}\right)
$$

will contain the population of constant failure rate. In terms of $\theta=1 / \lambda$ or the mean time between failure (MTBF), the above confidence limits change to

$$
P\left[\frac{2 T}{\chi_{2,2 r}^{2}}<\theta<\frac{2 T}{\chi_{1-\frac{\alpha}{2}, 2 r}^{2}}\right]=1-\alpha
$$

If testing is stopped at a fixed time rather than a fixed number of failures, the number of degrees of freedom in the lower limit increases by two. Table 3.5 shows the confidence limits for $\theta$, the mean of an exponential density.

Example 3.14 (two-sided): From the goodness of fit example, $T=22,850$, testing stopped after $r=60$ failures. We can obtain $\hat{\lambda}=0.00263$ and $\hat{\theta}=380.833$. Assuming that $\alpha=0.1$, then, from the above formula, we obtain

$$
\begin{gathered}
P\left[\frac{2 T}{\chi_{0.05,120}^{2}}<\theta<\frac{2 T}{\chi_{0.95,120}^{2}}\right]=0.9 \\
P\left[\frac{45,700}{146.568}<\theta<\frac{45,700}{95.703}\right]=0.9 \\
P[311.80<\theta<477.52]=0.9
\end{gathered}
$$

Example 3.15 (one-sided lower): Assuming that testing stopped after 1,000 hours with four failures, then

$$
\begin{aligned}
P\left[\frac{2 T}{\chi_{0.10,10}^{2}}<\theta\right] & =0.9 \\
P\left[\frac{2,000}{15.987}<\theta\right] & =0.9 \\
P[125.1<\theta] & =0.9
\end{aligned}
$$Table 3.5. Confidence limits for $\theta$

| Confidence limits | Fixed number of failures | Fixed time |
| :-- | :--: | :--: |
| One-sided lower <br> limit | $\frac{2 T}{\chi_{\alpha, 2 r}^{2}}$ | $\frac{2 T}{\chi_{\alpha, 2 r+2}^{2}}$ |
| One-sided upper <br> limit | $\frac{2 T}{\chi_{1-\alpha, 2 r}^{2}}$ | $\frac{2 T}{\chi_{1-\alpha, 2 r}^{2}}$ |
| Two-sided limits | $\frac{2 T}{\chi_{\alpha / 2,2 r}^{2}}, \frac{2 T}{\chi_{1-\alpha / 2,2 r}^{2}}$ | $\frac{2 T}{\chi_{\alpha / 2,2 r+2}^{2}}, \frac{2 T}{\chi_{1-\alpha / 2,2 r}^{2}}$ |

# 3.7.3 Confidence Intervals for the Binomial Parameters 

Consider a sequence of $n$ Bernoulli trials with $k$ successes and $(n-k)$ failures. We now determine one-sided upper and lower and two-sided limits on the parameter $p$, the probability of success. For the lower limit, the binomial sum is set up such that the chance probability of $k$ or more successes with a true $p$ as low as $p_{L}$ is only $\alpha / 2$. This means the probability of $k$ or more successes with a true $p$ higher than $p_{L}$ is $\left(1-\frac{\alpha}{2}\right):$

$$
\sum_{i=k}^{n}\binom{n}{i} p_{L}^{i}\left(1-p_{L}\right)^{n-i}=\frac{\alpha}{2}
$$

Similarly, the binomial sum for the upper limit is

$$
\sum_{i=k}^{n}\binom{n}{i} p_{U}^{i}\left(1-p_{U}\right)^{n-i}=1-\frac{\alpha}{2}
$$

or, equivalently, that

$$
\sum_{i=0}^{k-1}\binom{n}{i} p_{U}^{i}\left(1-p_{U}\right)^{n-i}=\frac{\alpha}{2}
$$

Solving for $p_{L}$ and $p_{U}$ in the above equations,

$$
P\left[p_{L}<p<p_{U}\right]=1-\alpha
$$

For the case of one-sided limits, merely change $\alpha / 2$ to $\alpha$.
Example 3.16: Given $n=100$ with 25 successes, and 75 failures, an $80 \%$ two-sided confidence limits on $p$ can be obtained as follows:

$$
\begin{aligned}
& \sum_{i=25}^{100}\binom{100}{i} p_{L}^{i}\left(1-p_{L}\right)^{100-i}=0.10 \\
& \sum_{i=0}^{24}\binom{100}{i} p_{U}^{i}\left(1-p_{U}\right)^{100-i}=0.10
\end{aligned}
$$

Solving the above two equations simultaneously, we obtain

$$
\begin{aligned}
& p_{L} \approx 0.194 \text { and } p_{U} \approx 0.313 \\
& P[0.194<p<0.313]=0.80
\end{aligned}
$$Example 3.17: Continuing with Example 3.16, find an $80 \%$ one-sided confidence limit on $p$.

We now can set the top equation to 0.20 and solve for $p_{L}$. It is easy to obtain $p_{L}=$ 0.211 and $P[p>0.211]=0.80$. Let us define $\bar{p}=k / n$, the number of successes divided by the number of trials. For large values of $n$ and if $n p>5$ and $n(1-p)>5$, and from the central limit theorem (Feller 1957), the statistic

$$
Z=\frac{(\bar{p}-p)}{\sqrt{\frac{\bar{p}(1-\bar{p})}{n}}}
$$

approximates to the standard normal distribution. Hence,

$$
P\left[-z_{\frac{\alpha}{2}}<Z<z_{\frac{\alpha}{2}}\right]=1-\alpha
$$

Then

$$
P\left[\bar{p}-z_{\frac{\alpha}{2}} \sqrt{\frac{\bar{p}(1-\bar{p})}{n}}<p<\bar{p}+z_{\frac{\alpha}{2}} \sqrt{\frac{\bar{p}(1-\bar{p})}{n}}\right]=1-\alpha
$$

Example 3.18: Given $n=900, k=180$, and $\alpha=0.05$. Then we obtain $p=180 / 900=$ 0.2 and

$$
\begin{aligned}
P\left[0.2-1.96 \sqrt{\frac{0.2(0.8)}{900}}<p<0.2+1.96 \sqrt{\frac{0.2(0.8)}{900}}\right] & =0.95 \\
P[.174<p<.226] & =0.95
\end{aligned}
$$

# 3.7.4 Confidence Intervals for the Poisson Parameters 

Limits for the Poisson parameters are completely analogous to the binomial except that the sample space is infinite instead of finite. The lower and upper limits can be solved simultaneously in the following equations:

$$
\begin{aligned}
& \sum_{i=k}^{\infty} \frac{\lambda_{L}^{i} e^{-\lambda_{L}}}{i!}=\frac{\alpha}{2} \\
& \sum_{i=k}^{\infty} \frac{\lambda_{U}^{i} e^{-\lambda_{U}}}{i!}=1-\frac{\alpha}{2}
\end{aligned}
$$

or, equivalently

$$
\begin{aligned}
& \sum_{i=k}^{\infty} \frac{\lambda_{L}^{i} e^{-\lambda_{L}}}{i!}=\frac{\alpha}{2} \\
& \sum_{i=0}^{k-1} \frac{\lambda_{U}^{i} e^{-\lambda_{U}}}{i!}=\frac{\alpha}{2}
\end{aligned}
$$Example 3.19: One thousand article lots are inspected resulting in an average of 10 defects per lot. Find $90 \%$ limits on the average number of defects per 1000 article lots. Assume $\alpha=0.1$,

$$
\begin{aligned}
& \sum_{i=10}^{\infty} \frac{\lambda_{L}^{i} e^{-\lambda_{L}}}{i!}=0.05 \\
& \sum_{i=0}^{0} \frac{\lambda_{U}^{i} e^{-\lambda_{U}}}{i!}=0.05
\end{aligned}
$$

Solving the above two equations simultaneously for $\lambda_{L}$ and $\lambda_{U}$, we obtain

$$
P[5.45<\lambda<16.95]=0.90
$$

The one-sided limits are constructed similarly to the case for binomial limits.

# 3.8 Non-parametric Tolerance Limits 

Non-parametric tolerance limits are based on the smallest and largest observation in the sample, designated as $X_{S}$ and $X_{L}$, respectively. Due to their non-parametric nature, these limits are quite insensitive and to gain precision proportional to the parametric methods requires much larger samples. An interesting question here is to determine the sample size required to include at least $100(1-\alpha) \%$ of the population between $X_{S}$ and $X_{L}$ with given probability $y$.

For two-sided tolerance limits, if (1- $\alpha$ ) is the minimum proportion of the population contained between the largest observation $X_{L}$ and smallest observation $X_{S}$ with confidence $(1-\gamma)$, then it can be shown that

$$
n(1-\alpha)^{n-1}-(n-1)(1-\alpha)^{n}=\gamma
$$

Therefore, the number of observations required is given by

$$
n=\left\lfloor\frac{(2-\alpha)}{4 \alpha} \chi_{1-\gamma, 4}^{2}+\frac{1}{2}\right\rfloor+1
$$

where a value of $\chi_{1-\gamma, A}^{2}$ is given in Table A1.3 of Appendix 1.
Example 3.20: Determine the tolerance limits which include at least $90 \%$ of the population with probability 0.95 . Here,

$$
\alpha=0.1, \gamma=0.95 \text { and } \chi_{0.05, A}^{2}=9.488
$$

and therefore, a sample of size

$$
n=\left\lfloor\frac{(2-0.1)}{4(0.1)}(9.488)+\frac{1}{2}\right\rfloor+1=46
$$

is required. For a one-sided tolerance limit, the number of observations required is given by

$$
n=\left\lfloor\frac{\log (1-\gamma)}{\log (1-\alpha)}\right\rfloor+1
$$Example 3.21: As in Example 3.20, we wish to find a lower tolerance limit, that is, the number of observations required so that the probability is 0.95 that at least $90 \%$ of the population will exceed $\mathrm{X}_{S}$ is given by

$$
n=\left|\frac{\log (1-0.95)}{\log (1-0.1)}\right|+1=30
$$

One can easily generate a table containing the sample size required to include a given percentage of the population between $X_{S}$ and $X_{L}$ with given confidence, or sample size required to include a given percentage of the population above or below $X_{S}$ or $X_{L}$, respectively.

# 3.9 Sequential Sampling 

A sequential sampling scheme is one in which items are drawn one at a time and the results at any stage determine if sampling or testing should stop. Thus, any sampling procedure for which the number of observations is a random variable can be regarded as sequential sampling. Sequential tests derive their name from the fact that the sample size is not determined in advance, but allowed to "float" with a decision (accept, reject, or continue test) after each trial or data point.

In general, let us consider the hypothesis

$$
H_{0}: f(x)=f_{0}(x) \quad \text { vs } \quad H_{1}: f(x)=f_{1}(x)
$$

For an observation test, say $X_{1}$, if $X_{1} \leq A$, then we will accept the testing hypothesis $\left(H_{0}: f(x)=f_{0}(x)\right)$; if $X_{1} \geq A$, then we will reject $H_{0}$ and accept $H_{I}: f(x)=$ $f_{1}(x)$. Otherwise, we will continue to perform at least one more test. The interval $X_{1}$ $\leq A$ is called the acceptance region. The interval $X_{1} \geq \mathrm{A}$ is called the rejection or critical region (see Figure A.2, Pham 2000a).

A "good" test is one that makes the $\alpha$ and $\beta$ errors as small as possible. However, there is not much freedom to do this without increasing the sample size. The common procedure is to fix the $\beta$ error and then choose a critical region to minimize the error or maximize the "power" (power $=1-\beta$ ) of the test, or to choose the critical region so as to equalize the $\alpha$ and $\beta$ errors to reasonable levels.

A criterion, similar to the MLE, for constructing tests is called the "probability ratio", which is the ratio of the sample densities under $H_{1}$ over $H_{0}$. Consider the ratio of probabilities

$$
\lambda_{m}=\frac{\prod_{i=1}^{n} f_{1}\left(x_{i}\right)}{\prod_{i=1}^{n} f_{0}\left(x_{i}\right)}>k
$$

Here, $x_{1}, x_{2}, \ldots, x_{n}$ are $n$ independent random observations and $k$ is chosen to give the desired error.

Recall from the MLE discussion in Section 3.2 that $f_{1}\left(x_{1}\right), f_{1}\left(x_{2}\right), \ldots, f_{1}\left(x_{n}\right)$ are maximized under $H_{1}$ when the parameter(s), e.g., $\theta=\theta_{1}$ and, similarly, $f_{0}\left(x_{1}\right), f_{0}\left(x_{2}\right)$,. . . , $f_{0}\left(x_{n}\right)$ are maximized when $\theta=\theta_{0}$. Thus, the ratio will become large if the sample favors $H_{1}$ and will become small if the sample favors $H_{0}$. Therefore, the test will be called a sequential probability ratio test if we

1. Stop sampling and reject $H_{0}$ as soon as $\lambda_{m} \geq A$
2. Stop sampling and accept $H_{0}$ as soon as $\lambda_{m} \leq B$
3. Continue sampling as long as $B<\lambda_{m}<A$, where $A>B$.

The choice of $A$ and $B$ with the above test, suggested by Wald (1947), can be determined as follows:

$$
B=\frac{\beta}{1-\alpha} \quad \text { and } \quad A=\frac{1-\beta}{\alpha}
$$

The basis for $\alpha$ and $\beta$ are therefore

$$
\begin{aligned}
& P\left[\lambda_{m}>A \mid H_{0}\right]=\alpha \\
& P\left[\lambda_{m}<A \mid H_{1}\right]=\beta
\end{aligned}
$$

# Exponential Case 

Let

$$
V(t)=\sum_{i=1}^{r} X_{i}+\sum_{j=1}^{n-r} t_{j}
$$

where $X_{i}$ are the times to failure and $t_{j}$ are the times to test termination without failure. Thus, $V(t)$ is merely the total operating time accrued on both successful and unsuccessful units where the total number of units is $n$. The hypothesis to be tested is

$$
H_{0}: \theta=\theta_{0} \quad \text { vs } H_{I}: \theta=\theta_{I}
$$

For the failed items,

$$
g\left(x_{1}, x_{2}, \ldots, x_{r}\right)=\left(\frac{1}{\theta}\right)^{r} e^{-\sum_{i=1}^{r} x_{i}}
$$

For the non-failed items,

$$
P\left(X_{r+1}>t_{1}, X_{r+2}>t_{2}, \ldots, X_{n}>t_{n-r},\right)=e^{-\sum_{i=1}^{n-r} t_{j}}
$$

The joint density for the first $r$ failures among $n$ items is$$
\begin{aligned}
f\left(x_{1}, x_{2}, \ldots, x_{r}, t_{r+1}, \ldots, t_{n}\right) & =\left(\frac{1}{\theta}\right)^{r} e^{-\frac{r}{V \alpha} \frac{x_{r}}{\theta}} \sum_{i=1}^{V \alpha} \frac{t_{i}}{\theta} \\
& =\left(\frac{1}{\theta}\right)^{r} e^{-\frac{V(t)}{t}}
\end{aligned}
$$

and

$$
\begin{aligned}
\lambda_{i n} & =\frac{\left(\frac{1}{\theta_{1}}\right)^{r} e^{-\frac{V(t)}{\theta_{1}}}}{\left(\frac{1}{\theta_{0}}\right)^{r} e^{-\frac{V(t)}{\theta_{0}}}} \\
& =\left(\frac{\theta_{0}}{\theta_{1}}\right)^{r} e^{-V(t)\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}
\end{aligned}
$$

Now, it has been shown that for sequential tests, the reject and accept limits, $A$ and $B$, can be equated to simple functions of $\alpha$ and $\beta$. Thus, we obtain the following test procedures:

$$
\begin{array}{ll}
\text { Continue test: } & \frac{\beta}{1-\alpha} \equiv B<\lambda_{i n}<A \equiv \frac{1-\beta}{\alpha} \\
\text { Reject } H_{0}: & \lambda_{i n}>A \equiv \frac{1-\beta}{\alpha} \\
\text { Accept } H_{0}: & \lambda_{i n}<B \equiv \frac{\beta}{1-\alpha}
\end{array}
$$

Working with the continue test inequality, we now have

$$
\frac{\beta}{1-\alpha}<\left(\frac{\theta_{0}}{\theta_{1}}\right)^{r} e^{-V(t)\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}<\frac{1-\beta}{\alpha}
$$

Taking natural logs of the above inequality, we obtain

$$
\ln \left(\frac{\beta}{1-\alpha}\right)<r \ln \left(\frac{\theta_{0}}{\theta_{1}}\right)-V(t)\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]<\ln \left(\frac{1-\beta}{\alpha}\right)
$$

The above inequality is linear in $V(t)$ and $r$, and therefore the rejection line $V(t)$ can be obtained by setting

$$
r \ln \left(\frac{\theta_{0}}{\theta_{1}}\right)-V(t)\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]=\ln \left(\frac{1-\beta}{\alpha}\right)
$$

or, equivalently,$$
V(t)=\frac{r \ln \left(\frac{\theta_{0}}{\theta_{1}}\right)}{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}-\frac{\ln \left(\frac{1-\beta}{\alpha}\right)}{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}
$$

Similarly, the acceptance line $V(t)$ can be obtained by setting

$$
r \log \left(\frac{\theta_{0}}{\theta_{1}}\right)-V(t)\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]=\log \left(\frac{\beta}{1-\alpha}\right)
$$

This implies that

$$
V(t)=\frac{r \ln \left(\frac{\theta_{0}}{\theta_{1}}\right)}{{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}-\frac{\ln \left(\frac{\beta}{1-\alpha}\right)}{{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]}}
$$

Example 3.22: Given that $H_{0}: \theta=500$ vs $H_{1}: \theta=250$ and $\alpha=\beta=0.1$. The acceptance and rejection lines are given by

$$
V(t)=346.6 r+1098.6
$$

and

$$
V(t)=346.6 r-1098.6
$$

respectively. Both are linear functions in terms of $r$, the number of first $r$ failures in the test.

For an exponential distribution

$$
\begin{array}{ll}
\theta & P(A) \\
0 & 0 \\
\theta_{1} & \beta \\
\frac{\log \left(\frac{\theta_{0}}{\theta_{1}}\right)}{{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]} & \frac{\log \left(\frac{1-\beta}{\alpha}\right)}{\log \left(\frac{1-\beta}{\alpha}\right)-\log \left(\frac{\beta}{1-\alpha}\right)} \\
\theta_{1} & 1-\alpha \\
\infty & 1
\end{array}
$$

From the information given in the above example, we can obtain| $\theta$ | $P(A)$ |
| :-- | :-- |
| 0 | 0 |
| 250 | 0.10 |
| 346.5 | 0.5 |
| 500 | 0.90 |
| $\infty$ | 1.0 |

Since there is no pre-assigned termination to a regular sequential test, it is customary to draw a curve called the "average sample number" (ASN). This curve shows the expected sample size as a function of the true parameter value. It is known that the test will be terminated with a finite observation. It should be noted that "on average", the sequential tests utilizes significantly smaller samples than fixed sample plans:

$$
\begin{array}{ll}
\theta & E(r)=A S N \\
0 & 0 \\
\theta_{1} & \frac{\theta_{0} \beta \log \left(\frac{\beta}{1-\alpha}\right)+(1-\beta) \log \left(\frac{1-\beta}{\alpha}\right)}{\left[\log \left(\frac{\theta_{0}}{\theta_{1}}\right)-\left(\frac{\theta_{0}-\theta_{1}}{\theta_{1}}\right)\right] \theta_{1}} \\
\frac{\log \left(\frac{\theta_{0}}{\theta_{1}}\right)}{\left[\frac{1}{\theta_{1}}-\frac{1}{\theta_{0}}\right]} & \frac{\log \left(\frac{1-\beta}{\alpha}\right) \log \left(\frac{\beta}{1-\alpha}\right)}{\left[\log \left(\frac{\theta_{0}}{\theta_{1}}\right)\right]^{2}} \\
& \frac{\left[(1-\alpha) \log \left(\frac{\beta}{1-\alpha}\right)+\alpha \log \left(\frac{1-\beta}{\alpha}\right)\right] \theta_{1}}{\left[\log \left(\frac{\theta_{0}}{\theta_{1}}\right)-\left(\frac{\theta_{0}-\theta_{1}}{\theta_{1}}\right)\right] \theta_{0}} \\
\infty & 0
\end{array}
$$

An approximate formula for $E(t)$, the expected time to reach decision, is

$$
E(t) \equiv \theta \log \left(\frac{n}{n-E(r)}\right)
$$

where $n$ is the total number of units on test (assuming no replacement of failed units). If replacements are made, then

$$
E(t)=\frac{\theta}{n} E(r)
$$

Occasionally, it is desired to "truncate" a sequential plan such that, if no decision is made before a certain point, testing is stopped and a decision is made on the basis of data acquired up to that point (Pham 2000a, page 251). There are a number ofrules and theories on optimum truncation. In the reliability community, a $V(t)$ truncation point at $10 \theta_{0}$ is often used to determine the $V(t)$ and $r$ lines for truncation and the corresponding exact $\alpha=\beta$ errors (these will in general be larger for truncated tests than for the non-truncated). An approximate method draws the $V(t)$ truncation line to the center of the continue test band and constructs the $r$ truncation line perpendicular to that point (see Figure A.7, Pham 2000a, page 252).

# Bernoulli Case 

$$
H_{0}: p=p_{0} \text { vs } H_{1}: p=p_{1}
$$

and $\alpha=\beta$ are pre-assigned. Then we obtain

$$
\begin{aligned}
\lambda_{m} & =\frac{\prod_{i=1}^{n} p_{1}^{x_{i}}\left(1-p_{1}\right)^{1-x_{i}}}{\prod_{i=1}^{n} p_{0}^{x_{i}}\left(1-p_{0}\right)^{1-x_{i}}} \\
& =\frac{p_{1}^{\sum_{i=1}^{n} x_{i}}\left(1-p_{1}\right)^{n-\sum_{i=1}^{n} x_{i}}}{p_{0}^{\sum_{i=1}^{n} x_{i}}\left(1-p_{0}\right)^{n-\sum_{i=1}^{n} x_{i}}} \\
& =\left(\frac{p_{1}}{p_{0}}\right)^{\sum_{i=1}^{n} x_{i}}\left(\frac{1-p_{1}}{1-p_{0}}\right)^{n-\sum_{i=1}^{n} x_{i}}
\end{aligned}
$$

The following inequality will be determined to continue the test region:

$$
\frac{\beta}{1-\alpha}<\left(\frac{p_{1}}{p_{0}}\right)^{\sum_{i=1}^{n} x_{i}}\left(\frac{1-p_{1}}{1-p_{0}}\right)^{n-\sum_{i=1}^{n} x_{i}}<\frac{1-\beta}{\alpha}
$$

Taking logs through the above inequality produces linear relationships in $\sum x_{i}$ (e.g., number of failures or defects) and $n$, the total number of units or trials, that is,

$$
\begin{aligned}
& \log \left(\frac{\beta}{1-\alpha}\right) \\
& <\sum_{i=1}^{n} x_{i} \log \left(\frac{p_{1}}{p_{0}}\right)+\left(n-\sum_{i=1}^{n} x_{i}\right) \log \left(\frac{1-p_{1}}{1-p_{0}}\right)<\log \left(\frac{1-\beta}{\alpha}\right)
\end{aligned}
$$

Similar tests can be constructed for other distribution parameters following the same general scheme.

### 3.10 Bayesian Methods

The Bayesian approach to statistical inference is based on a theorem first presented by the Reverend Thomas Bayes. To demonstrate the approach, let $X$ have a pdf $f(x)$, which is dependent on $\theta$. In the traditional statistical inference approach, $\theta$ isan unknown parameter, and hence, is a constant. We now describe our prior belief in the value of $\theta$ by a pdf $h(\theta)$. This amounts to quantitatively assessing subjective judgment and should not be confused with the so-called objective probability assessment derived from the long-term frequency approach. Thus, $\theta$ will now essentially be treated as a random variable $\theta$ with pdf $h(\theta)$.

Consider a random sample $X_{1}, X_{2}, \ldots, X_{\mathrm{n}}$ from $f(x)$ and define a statistic Y as a function of this random sample. Then there exists a conditional pdf $g(y \mid \theta)$ of $Y$ for a given $\theta$. The joint pdf for $y$ and $\theta$ is

$$
f(\theta, y)=h(\theta) g(y \mid \theta)
$$

If $\theta$ is continuous, then

$$
f_{1}(y)=\int_{\theta} h(\theta) g(y \mid \theta) d \theta
$$

is the marginal pdf for the statistic $y$. Given the information $y$, the conditional pdf for $\theta$ is

$$
\begin{aligned}
k(\theta \mid y) & =\frac{h(\theta) g(y \mid \theta)}{f_{1}(y)} \quad \text { for } f_{1}(y)>0 \\
& =\frac{h(\theta) g(y \mid \theta)}{\int_{\theta} h(\theta) g(y \mid \theta) d \theta}
\end{aligned}
$$

If $\theta$ is discrete, then

$$
f_{1}(y)=\sum_{k} P\left(\theta_{k}\right) P\left(y \mid \theta_{k}\right)
$$

and

$$
P\left(\theta_{i} \mid y_{i}\right)=\frac{P\left(\theta_{k}\right) P\left(y_{i} \mid \theta_{i}\right)}{\sum_{k} P\left(\theta_{k}\right) P\left(y_{j} \mid \theta_{k}\right)}
$$

where $P\left(\theta_{j}\right)$ is a prior probability of event $\theta_{i}$ and $P\left(\theta_{j} \mid y_{j}\right)$ is a posterior probability of event $y_{j}$ given $\theta_{i}$. This is simply a form of Bayes' theorem. Here, $h(\theta)$ is the prior pdf that expresses our belief in the value of $\theta$ before the data $(Y=y)$ became available. Then $k(\theta \mid y)$ is the posterior pdf of given the data $(Y=y)$.

Note that the change in the shape of the prior pdf $h(\theta)$ to the posterior pdf $k(\theta \mid$ $y)$ due to the information is a result of the product of $g(y \mid \theta)$ and $h(\theta)$ because $f_{1}(y)$ is simply a normalization constant for a fixed $y$ The idea in reliability is to take "prior" data and combine it with current data to gain a better estimate or confidence interval or test than would be possible with either singularly. As more current data is acquired, the prior data is "washed out" (Pham 2000a).
Case 1: Binomial Confidence Limits - Uniform Prior. Results from ten missile tests are used to form a one-sided binomial confidence interval of the form

$$
P\left[R \geq R_{L}\right]=1-\alpha
$$

From Subsection 3.7.3, we have$$
\sum_{i=k}^{10}\binom{10}{i} R_{L}^{i}\left(1-R_{L}\right)^{10-i}=\alpha
$$

Choosing $\alpha=0.1$, lower limits as a function of the number of missile test successes are shown in Table 3.6. Assume from previous experience that it is known that the true reliability of the missile is somewhere between 0.8 and 1.0 and furthermore that the distribution through this range is uniform. The prior density on $R$ is then

$$
g(R)=5 \quad 0.8<R<1.0
$$

Table 3.6. Lower limits as a function of the number of missile test successes

| $k$ | $R_{L}$ | Exact level |
| :--: | :--: | :-- |
| 10 | 0.79 | 0.905 |
| 9 | 0.66 | 0.904 |
| 8 | 0.55 | 0.900 |
| 7 | 0.45 | 0.898 |
| 6 | 0.35 | 0.905 |

From the current tests, results are $k$ successes out of ten missile tests, so for the event $A$ that contained $k$ successes:

$$
P(A \mid R)=\binom{10}{k} R^{k}(1-R)^{10-k}
$$

Applying Bayes' theorem, we obtain

$$
\begin{aligned}
g(R \mid A) & =\frac{g(R) P(A \mid R)}{\int_{R} g(R) P(A \mid R) d R} \\
& =\frac{5\binom{10}{k} R^{k}(1-R)^{10-k}}{\int_{0.8}^{1.0} 5\binom{10}{k} R^{k}(1-R)^{10-k} d R}
\end{aligned}
$$

For the case of $k=10$,

$$
\begin{aligned}
g(R \mid A) & =\frac{R^{10}}{\int_{0.8}^{1.0} R^{10} d R} \\
& =\frac{11 R^{10}}{0.914}=12.035 R^{10}
\end{aligned}
$$

To obtain confidence limits incorporating the "new" or current data,$$
\begin{gathered}
\int_{R_{L}}^{1.0} g(A \mid R) d R=0.9 \\
\int_{R_{L}}^{1.0} 12.035 R^{10} d R=0.9
\end{gathered}
$$

After simplifications, we have

$$
\begin{aligned}
& R_{L}^{11}=0.177 \\
& R_{L}=0.855
\end{aligned}
$$

Limits for the 10/10, 9/10, 8/10, 7/10, and 6/10 cases employing the Bayesian method are given in Table 3.7 along with a comparison with the previously calculated limits not employing the prior assumption. Note that the lower limit of 0.8 on the prior cannot be washed out.

Table 3.7. Comparison between limits applying the Bayesian method and those that do not

| k | $R_{L}$ (uniform $[0.8,1]$ prior) | $R_{L}$ (no prior) | Exact level |
| :--: | :--: | :--: | :--: |
| 10 | 0.855 | 0.79 | 0.905 |
| 9 | 0.822 | 0.66 | 0.904 |
| 8 | 0.812 | 0.55 | 0.900 |
| 7 | 0.807 | 0.45 | 0.898 |
| 6 | 0.805 | 0.35 | 0.905 |

Case 2: Binomial Confidence Limits - Beta Prior. The prior density of the beta function is

$$
g(R)=\frac{(\alpha+\beta+1)!}{\alpha!\beta!} R^{\alpha}(1-R)^{\beta}
$$

The conditional binomial density function is

$$
P(A \mid R)=\binom{10}{i} R^{i}(1-R)^{10-i}
$$

Then we have

$$
g(R \mid A)=\frac{\frac{(\alpha+\beta+1)!}{\alpha!\beta!} R^{\alpha}(1-R)^{\beta}\binom{10}{k} R^{k}(1-R)^{10-k}}{\frac{(\alpha+\beta+1)!}{\alpha!\beta!} \int_{0}^{1} R^{\alpha}(1-R)^{\beta}\binom{10}{k} R^{k}(1-R)^{10-k} d R}
$$

After simplifications, we obtain

$$
g(R \mid A)=\frac{R^{\alpha+k}(1-R)^{\beta+10-k}}{\int_{0}^{1} R^{\alpha+k}(1-R)^{\beta+10-k} d R}
$$

Multiplying and dividing by$$
\frac{(\alpha+\beta+11)!}{(\alpha+\beta)!(\beta+10-k)!}
$$

puts the denominator in the form of a beta function with integration over the entire range, and hence, equal to 1 . Thus,

$$
g(R \mid A)=\binom{\alpha+\beta+10}{\alpha+k} R^{\alpha+k}(1-R)^{\beta+10-k}
$$

which again is a beta density function with parameters

$$
(\alpha+k)=\alpha^{\prime} \quad \text { and } \quad(\beta+10-k)=\beta^{\prime}
$$

Integration over $g(R \mid A)$ from $R_{L}$ to 1.0 with an integral set to $1-\alpha$ and a solution of $R_{L}$ will produce $100(1-\alpha) \%$ lower confidence bounds on $R$, that is,

$$
\int_{R_{L}}^{1.0} g(R \mid A) d R=1-\alpha
$$

Case 3: Exponential Confidence Limits - Gamma Prior. For this situation, assume interest is in an upper limit on the exponential parameter $X$. The desired statement is of the form

$$
p\left[\lambda<\lambda_{U}\right]=1-\alpha
$$

If 1000 hours of test time was accrued with one failure, a $90 \%$ upper confidence limit on $\lambda$ would be

$$
p[\lambda<0.0039]=0.9
$$

From a study of prior data on the device, assume that $\lambda$ has a gamma prior density of the form

$$
g(\lambda)=\frac{\lambda^{n-1} e^{-\frac{\lambda}{\beta}}}{(n-1)! \beta^{n}}
$$

With an exponential failure time assumption, the current data in terms of hours of test and failures can be expressed as a Poisson, thus,

$$
p(A \mid \lambda)=\frac{(\lambda T)^{n} e^{-\lambda T}}{r!}
$$

where $\mathrm{n}=$ number of failures
$T=$ test time, and
$A=$ event which is $r$ failures in $T$ hours of test.
Applying Bayes' results, we have$$
\begin{aligned}
g(\lambda \mid A)= & \frac{\frac{\lambda^{n-1} e^{-\frac{\lambda}{\beta}}}{(n-1)!} \frac{(\lambda T)^{r} e^{-\lambda T}}{r!}}{\int_{\lambda=0}^{\infty} \frac{\lambda^{n-1} e^{-\frac{\lambda}{\beta}}}{(n-1)!} \frac{(\lambda T)^{r} e^{-\lambda T}}{r!} d \lambda} \\
& =\frac{\lambda^{n+r-1} e^{-\lambda\left(\frac{1}{\beta}+T\right)}}{\int_{0}^{\infty} \lambda^{n+r-1} e^{-\lambda\left(\frac{1}{\beta}+T\right)} d \lambda}
\end{aligned}
$$

Note that

$$
\int_{0}^{\infty} \lambda^{n+r-1} e^{-\lambda\left(\frac{1}{\beta}+T\right)} d \lambda=\frac{(n+r-1)!}{\left(\frac{1}{\beta}+T\right)^{n+r}}
$$

Hence,

$$
g(\lambda \mid A)=\frac{\lambda^{n+r-1} e^{-\lambda\left(\frac{1}{\beta}+T\right)}\left(\frac{1}{\beta}+T\right)^{n+r}}{(n+r-1)!}
$$

Thus, $g(\lambda \mid A)$ is also a gamma density with parameters $(n+r-1)$ and $\frac{1}{\left(\frac{1}{\beta}+T\right)}$. This density can be transformed to the $\chi^{2}$ density with $2(n+r)$ degree of freedom by the following change of variable. Let

$$
\lambda^{\prime}=2 \lambda\left(\frac{1}{\beta}+T\right)
$$

then

$$
d \lambda=\frac{1}{2}\left(\frac{1}{\frac{1}{\beta}+T}\right) d \lambda^{\prime}
$$

We have

$$
h\left(\lambda^{\prime} \mid A\right)=\frac{\left(\lambda^{\prime}\right)^{\frac{2(n+r)}{2}-1} e^{-\frac{\lambda^{\prime}}{2}}}{\left[\frac{2(n+r)}{2}-1\right]!2^{\frac{2(n+r)}{2}}}
$$To obtain a $100(1-\alpha) \%$ upper confidence limit on $\lambda$, solve for $\lambda^{\prime}$ in the integral

$$
\int_{0}^{\lambda^{\prime}} h(s \mid A) d s=1-\alpha
$$

and convert $\lambda^{\prime}$ to $\lambda$ via the above transformation.
Example 3.23: Given a gamma prior with $n=2$ and $\beta=0.0001$ and current data as before (i.e., 1000 hours of test with one failure), the posterior density becomes

$$
g(\lambda \mid A)=\frac{\lambda^{2} e^{-\lambda(11,000)}(11,000)^{2}}{2}
$$

converting to $\chi^{2}$ via the transformation $\lambda^{\prime}=2 \lambda(11000)$ and

$$
h\left(\lambda^{\prime} \mid A\right)=\frac{\left(\lambda^{\prime}\right)^{\frac{6}{2}-1} e^{-\frac{\lambda^{\prime}}{2}}}{\left[\frac{6}{2}-1\right]!2^{\frac{6}{2}}}
$$

which is $\chi^{2}$ with six degrees of freedom. Choosing $\alpha=0.1$ then

$$
\chi_{6,1-\alpha}^{2}=\chi_{6,0.9}^{2}=10.6
$$

and

$$
p\left[\lambda^{\prime}<10.6\right]=0.9
$$

But $\lambda^{\prime}=2 \lambda(11,000)$, hence,

$$
p\left[\lambda^{\prime}=2 \lambda(11,000)<10.6\right]=0.9
$$

or

$$
p[\lambda<0.0005]=0.9
$$

The latter limit conforms to 0.0039 derived without the use of a prior density, i.e., an approximate eight fold improvement. The examples above involved the development of tighter confidence limits where a prior density of the parameter could be utilized.

In general, for legitimate applications and where prior data are available, employment of Bayesian methods can reduce cost or give results with less risk for the same dollar value (Pham 2000a).

# 3.11 Further Reading 

The reader interested in a deeper understanding of advanced statistical inference and theory should note the following highly recommended books:Introduction to Statistics:
P.S. Mann, Introductory Statistics, Wiley, 2004
J.L. Devore, Probability and Statistics for Engineering and the Sciences, 3rd edition, Brooks/Cole Pub. Co., Pacific Grove, 1991

Life Data Analysis:
W.B. Nelson, Applied Life Data Analysis, Wiley, 2004

For Censored data:
R.J.A. Little and D.B. Rubin, Statistical Analysis with Missing Data, Wiley, 2002

For Bayesian:
J. M. Bernardo and A.F. M. Smith, Bayesian Theory, Wiley, 2000
W. M. Bolstad, Introduction to Bayesian Statistics, Wiley, 2004

# 3.12 Problems 

1. Let $X_{1}, X_{2}, \ldots, X_{n}$ represent a random sample from the Poisson distribution having pdf

$$
f(x ; \lambda)=\frac{e^{-\lambda} \lambda^{x}}{x!} \quad \text { for } \mathrm{x}=0,1,2, \ldots \text { and } \lambda \geq 0
$$

Find the maximum likelihood estimator $\hat{\lambda}$ of $\lambda$.
2. Let $X_{1}, X_{2}, \ldots, X_{n}$ be a random sample from the distribution with a discrete pdf

$$
P(x)=p^{x}(1-p)^{1-x} \quad x=0,1 \quad \text { and } 0<p<1
$$

Find the maximum likelihood estimator $\hat{p}$ of $p$.
3. Assume that $X_{1}, X_{2}, \ldots, X_{n}$ represent a random sample from the Pareto distribution, that is,

$$
F(x ; \lambda, \theta)=1-\left(\frac{\lambda}{x}\right)^{\theta} \quad \text { for } \quad x \geq \lambda, \quad \lambda>0, \quad \theta>0
$$

This distribution is commonly used as a model to study incomes. Find the maximum likelihood estimators of $\lambda$ and $\theta$.
4. Let $Y_{1}<Y_{2}<\ldots<Y_{\mathrm{n}}$ be the order statistics of a random sample $X_{1}, X_{2}, \ldots, X_{n}$ from the distribution with pdf

$$
f(x ; \theta)=1 \quad \text { if } \quad \theta-\frac{1}{2} \leq x \leq \theta+\frac{1}{2}, \quad-\infty<\theta<\infty
$$

Show that any statistic $h\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ such that$$
Y_{n}-\frac{1}{2} \leq h\left(X_{1}, X_{2}, \ldots, X_{n}\right) \leq Y_{1}+\frac{1}{2}
$$

is a maximum likelihood estimator of $\theta$. What can you say about the following functions?
(a) $\frac{\left(4 Y_{1}+2 Y_{n}+1\right)}{6}$
(b) $\frac{\left(Y_{1}+Y_{n}\right)}{2}$
(c) $\frac{\left(2 Y_{1}+4 Y_{n}-1\right)}{6}$
5. The lifetime of transistors is assumed to have an exponential distribution with pdf

$$
f(t ; \theta)=\frac{1}{\theta} e^{-\frac{t}{\theta}} \text { for } \mathrm{t} \geq 0, \quad \theta>0
$$

A random sample of size $n$ is observed. Determine the following:
(a) The maximum likelihood estimator of $\theta$.
(b) The MLE of the transistor reliability function, $\hat{R}(t)$, of

$$
R(t)=e^{-\frac{t}{\theta}}
$$# Software Development Lifecycle and Data Analysis 

### 4.1 Introduction

As software becomes increasingly important in systems that perform complex and critical functions, e.g., military defense, nuclear reactors, so too have the risks and impacts of software-caused failures. There is now general agreement on the need to increase software reliability and quality by eliminating errors created during software development. Industry and academic institutions have responded to this need by improving developmental methods in the technology known as software engineering and by employing systematic checks to detect software errors during and in parallel with the developmental process.

Many organizations make the reduction of defects their first quality goal. The consumer electronics business, however, pursues a different goal: maintaining the number of defects in the field at zero. When electronic products leave the showroom, their destination is unknown. Therefore, detecting and correcting a serious software defect would entail recalling hundreds of thousands of products.

In the past 35 years, hundreds of research papers have been published in the areas of software quality, software engineering development process, software reliability modeling, software independent verification and validation (IV\&V) and software fault tolerance. Software engineering is evolving from an art to a practical engineering discipline (Lyu 1996).

A large number of analytical models have been proposed and studied over the last two decades for assessing the quality of a software system. Each model must make some assumptions about the development process and test environment. The environment can change depending on the software application, the lifecycle development process as well as the capabilities of the engineering design team (Malaiya 1990). Therefore, it is important for software users and practitioners to be familiar with all the relevant models in order to make informed decisions about the quality of any software product.

This chapter provides the basic concepts of software engineering assessment including software lifecycle, software development process and its applications, software verification and validation, and data collection and analysis.# 4.2 Software vs Hardware Reliability 

The development of hardware reliability theory has a long history and was established to improve hardware reliability greatly while the size and complexity of software applications have increased (Xie 1991). Hardware reliability encompasses a wide spectrum of analyses that strive systematically to reduce or eliminate system failures which adversely affect product performance. Reliability also provides the basic approach for assessing safety and risk analysis.

Software reliability strives systematically to reduce or eliminate system failures which adversely affect performance of a software program. Software systems do not degrade over time unless modified. There are many differences between the reliability and testing concepts and techniques of hardware and software. Therefore, a comparison of software and hardware reliability would be useful in developing software reliability modeling.

Table 4.1 shows the differences and similarities between the two. Pham (2000a, Figure 3.1) shows in more detail the sequence of failure either by the hardware or software. The result is that software quality and reliability must be built into software during the developmental process.

Example 4.1: Chilled Water System (Pham 2000a). The chilled water system acts as a heat sink for an air-conditioning system and the electronics cooling system. It provides a supply of chilled water to the individual air-handling units (AHUs) and to the suction of the electronics cooling water system pumps. More details about the system configuration and description can be obtained in Pham (2000a). A simplified diagram of the system and its corresponding reliability block diagram can be obtained in Pham (2000a, Figures 3.2(a) and 3.2(b), respectively).

The chilled water system consists of two chillers and two chilled water pumps that are used to circulate chilled water to the various chilled water loads. The system success criteria are based on supplying chilled water to the operations building AHUs. There are five AHUs in the operations building: two main units supply cool air to the entire building and three critical units supply cooling to three cooling zones in the critical operations area.

Successful operation was designed as follows: one of the two chillers operating, and one of the two chilled water pumps running, supplying chilled water to the operations building (Pham 2000a). Additionally, one of the two main operations building AHUs must be operating along with two of the three critical area AHUs. Its success criteria are based on the successful operation of one of the chillers and one of the chilled water pumps. It is also assumed that success requires one of the main operations building AHUs and two of the three critical area AHUs.Table 4.1. Software reliability vs hardware reliability

| Software reliability | Hardware reliability |
| :-- | :-- |
| Without considering program evolution, <br> failure rate is statistically non-increasing | Failure rate has a bathtub curve. <br> The burn-in state is similar to the <br> software debugging state |
| Failures never occur if the software is <br> not used | Material deterioration can cause <br> failures even though the system is <br> not used |
| Most models are analytically derived <br> from assumptions. Emphasis is on <br> developing the model, the interpretation <br> of the model assumptions, and the <br> physical meaning of the parameters | Failure data are fitted to some <br> distributions. The selection of the <br> underlying distribution is based on <br> the analysis of failure data and <br> experiences. Emphasis is placed on <br> analyzing failure data |
| Failures are caused by incorrect logic, <br> incorrect statements, or incorrect input <br> data. This is similar to design errors of a <br> complex hardware system | Failures are caused by material <br> deterioration, random failures, de- <br> sign errors, misuse, and environ- <br> ment |
| Software reliability can be improved by <br> increasing the testing effort and by <br> correc-ting detected faults. Reliability <br> tends to change continuously during <br> testing due to the addition of problems in <br> new code or to the removal of problems <br> by debugging errors | Hardware reliability can be impro- <br> ved by better design, better mate- <br> rial, applying redundancy and <br> accelerated life testing |
| Software repairs establish a new piece of <br> software | Hardware repairs restore the origi- <br> nal condition |
| Software failures are rarely preceded by <br> warnings | Hardware failures are usually pre- <br> ceded by warnings |
| Software components have rarely been <br> stan-dardized | Hardware components can be stan- <br> dardized |
| Software essentially requires infinite <br> testing | Hardware can usually be tested <br> exhaustively |

All the water pumps, the chillers, and AHUs can be represented by exponential distributions with failure rates $\lambda_{p}, \lambda_{c}$, and $\lambda_{a}$, respectively. Assume that$$
\begin{aligned}
& \lambda p=0.001 / \text { hour } \\
& \lambda c=0.0005 / \text { hour } \\
& \lambda a=0.0001 / \text { hour }
\end{aligned}
$$

Assume a mission of $t=72$ hours, then

1. The reliability of the water pumps subsystem is

$$
\begin{aligned}
R_{p} & =1-\left(1-e^{-(0.001)(72)}\right)^{2} \\
& =0.99517
\end{aligned}
$$

2. The reliability of the chillers' subsystem is

$$
\begin{aligned}
R_{c} & =1-\left(1-e^{-(0.0005)(72)}\right)^{2} \\
& =0.99875
\end{aligned}
$$

3. The reliability of the AHU subsystem I is

$$
\begin{aligned}
R_{I a} & =1-\left(1-e^{-(0.0001)(72)}\right)^{2} \\
& =0.99995
\end{aligned}
$$

4. The reliability of the AHU subsystem II is

$$
\begin{aligned}
R_{I I a} & =\sum_{i=2}^{3}\binom{3}{i}\left(e^{-(0.0001)(72)}\right)^{i}\left(1-e^{-(0.0001)(72)}\right)^{3-i} \\
& =0.99985
\end{aligned}
$$

Assuming all the software systems do not fail, the overall chilled water system reliability is

$$
\begin{aligned}
R_{s} & =R_{s} \times R_{s} \times R_{s} \times R_{s} \\
& =0.99373
\end{aligned}
$$

The software, however, does fail. The water pumps, chillers, and AHU software each contain approximately 250,000 lines of source code in ground control and processing to operate innumerable hardware units. One observes that the software reliabilities of the water pumps, chillers, and AHUs for a 72-hour mission are

$$
P_{p}=0.97, P_{c}=0.99, \text { and } P_{a}=0.995
$$

respectively. Therefore, the reliability of the overall chilled water hardware software system becomes

$$
\begin{aligned}
R_{s}= & \left(1-\left[1-\left(0.97\right) e^{-(0.001)(72)}\right]^{2}\right) \\
& \left(1-\left[1-(0.99) e^{-(0.0005)(72)}\right]^{2}\right)(0.995) R_{I a} \cdot R_{I I a} \\
= & 0.983354
\end{aligned}
$$

which is far less than the reliability result in equation (4.1).

# 4.3 Software Reliability and Testing Concepts 

Software is essentially an instrument for transforming a discrete set of inputs into a discrete set of outputs. It comprises a set of coded statements or instructions whose functions may be to evaluate an expression and store the result in a temporary orpermanent location, to decide which statement to execute, or to perform input/ output operations (Goel 1985). Hence, software can be regarded as a function $f$, mapping the input space to the output space ( $f$. input $\rightarrow$ output), where the input space is the set of all input states and the output space is the set of all output states (see Pham 2000a, Figure 3.3).

Software reliability is the probability that given software functions without failure in a given environmental condition during a specified time. Another deterministic model defines software reliability as the probability of successful execution(s) of an input state randomly selected from the input space under specified operating conditions. Another definition is the probability of failure-free execution of the software for a specified time in a specified environment. For example, an operating system with a reliability of $95 \%$ for 8 hours for an average user should work 95 out of 100 periods of 8 hours without any problems. Software failure means the inability to perform an intended task specified by a requirement. A software fault (or bug) is an error in the program source-text, which causes software failure when the program is executed under certain conditions. Hence, a software fault is generated when a mistake is made.

In vehicular applications, for instance, errors can be divided into four categories: critical, high, moderate and low:
Critical: It may affect a federally mandated item. (A change is required immediately, i.e., brake system.)
High: It may affect a necessary function of vehicle operation or subsystem, i.e., inoperative engine, air-conditioning, locks, etc. (Potential customer satisfaction item, a change is required immediately.)
Moderate: It may affect a convenience feature i.e., chimes, cruise control, compass, mini-trip computer, head lamp delay, etc. (Change at the next opportunity.)
Low: It is unreasonable to expect that the minor nature of this item would have any real effect on the vehicle or system performance. (No change required at this time.)
In general, the definition of what constitutes a software failure is an area open for debate since it depends on the application. When a program crashes, it has obviously failed due to an error in design, specifications, coding, or testing. One can define a failure as not meeting the user's requirements or expectations of the software operation. This can be due to a number of criteria which are not always well-defined. An example is that the speed of execution, accuracy of the computations, etc., can be the criteria for failure of the software.

Software testing is the process of executing a program to locate an error. A good test case is one that has a high probability of finding undiscovered error(s). It is impossible to continue testing the software until all faults are detected and removed as testing of all possible inputs would require millions of years! Therefore, failure probabilities must be inferred from testing a sample of all possible input states called the input space. In other words, input space is the set of all possible input states. Similarly, output space is the set of all possible output states for a given software and input space.

It is generally very difficult to test exhaustively a large computer program because of problems with dimensionality. If the input space consists of a singleunbounded variable, then an infinite number of input cases will be needed to provide an exhaustive test of the program. If the input space is bounded, but contains a large number of independent variables, then the number of input cases needed for an exhaustive test will tend to be impossibly large, even if one accepts the use of discretization for each input variable.

Similarly, it will probably be an impossible task to test each pathway through the program because of the very large number of paths involved. For instance, the flow graph of a very small program (see Pham 2000a, Figure 3.4) shows the schematics of a fairly small program, with a number of DO loops and IF branches, with 1018 unique paths through it. Even though exhaustive software testing may not be feasible for a very large software system, it makes sense to carry out a series of tests on each functional area. In the context of the user relationship, the user should obviously stipulate the tests to be carried out and be actively involved in their execution (Churchley 1991).

As we know, different inputs have different chances of being selected, and we can never be sure which inputs are selected in the operational phase of real world applications. During the operational phase, some input states are executed more frequently than others and a probability can be assigned to each input state to form the operational profile of the program. This operational profile can be used to construct the software reliability model. This type of model is also called an input-domain model. The interesting questions here are: (1) Is it possible to determine the sizes and locations of the fault regions in the input space? (2) How do we determine the reliability that a program will execute correctly for a particular length of time?

To select a good software model in order to make an accurate reliability prediction, the testing strategy should be incorporated into the software reliability model. It should be noted that the best models may vary from time to time and differ from application to application.

The evaluation of software reliability cannot be performed without software failure data. Therefore, the establishment of a software failure database is useful to both practitioners and researchers for predicting and estimating software reliability and to determine the total testing time needed to reach a desired reliability goal. Collected data are grouped into four categories: component data, management data, dynamic failure data, and fault removal data, each with a unique set of information.

The information in the component data category contains the number of executable source lines of code, the total number of comments and instructions, and the source language used for each system component. The information in the management data category is the starting and ending date for each lifecycle phase (analysis, design, code, test, and operation), the definitions and requirements of each lifecycle phase, and the models used for estimating software reliability.

The information in the dynamic failure data category is the number of CPU hours since the last failure, the number of test cases executed since the last failure, the severity of the failure, the method of failure detection, and the unit complexity and size where the fault was detected. The information in the fault removal data category is the date and time of fixing an error, the CPU hours required to fix an error, and the labor hours required to fix an error for each failure corrected. The data collection addresses these questions:1. Are the defects discovered as a result of simply testing artifacts of prior modifications or are they previously undetected defects?
2. What taxonomic categories are required for defense, aerospace, military, and commercial systems, and what defect percentages reside in each category?

# 4.4 Software Lifecycle 

A software lifecycle provides a systematic approach to developing, using, operating, and maintaining a software system. The standard IEEE computer dictionary has defined the software lifecycle as: "That period of time in which the software is conceived, developed and used". There are many different definitions of software lifecycle (Boehm 1981; Pressman 1983).

A software lifecycle consists of the following five successive phases (also see Figure 3.5 in Pham 2000a for details):

1. Analysis (requirements and functional specifications)
2. Design
3. Coding
4. Testing
5. Operation

The detailed activities of each phase are given in Pham (2000a) (see Figures 3.5-3.11). Table 4.2 shows the errors introduced and errors detected in the software lifecycle of a commercial application. In the early phases of the software lifecycle, a predictive software model is needed because no failure data are available. This type of model predicts the number of initial faults in the software before testing. In the testing phase, the software reliability can be used to improve through perfect debugging.

Table 4.2. Software error introduction and discovery

| Lifecycle phase | Errors introduced <br> $(\%)$ | Errors detected <br> $(\%)$ |
| :-- | :--: | :--: |
| Analysis | 55 | 18 |
| Design | 30 | 10 |
| Coding and testing | 10 | 50 |
| Operations | 5 | 22 |

By assuming perfect debugging, i.e., a fault is removed with certainty whenever a failure occurs, the number of remaining faults is a decreasing function of debug-ging time. With an imperfect debugging assumption, i.e., faults may or may not be removed, introduced, or changed at each debugging, the number of remaining faults may increase or decrease.

A reliability growth model is needed to estimate the current reliability level and the time and resources required to achieve the desired reliability goal. During this phase, reliability estimation is based on the analysis of failure data. After the release of a software program, the addition of new modules, removal of old ones, removal of detected errors, mixing of newly and previously written code, change ofuser environment, and change of hardware and management involvement have to be considered in the evaluation of software reliability. An evolution model is thus needed.

# Analysis Phase 

The analysis phase is the first step in the software development process and also the most important phase in the whole process and the foundation of building a successful software product (Pham 2000a). A survey at the North Jersey Software Process Improvement Network workshop in August 1995 showed that about 35\% of the effort in software development projects should be concentrated in the analysis phase (Pham 1999a).

The purpose of the analysis phase (Figure 3.6 in Pham 2000a) is to define the requirements and provide specifications for the subsequent phases and activities. The analysis phase is composed of three major activities: problem definition, requirements, and specifications. Problem definition develops the problem statement and the scope of the project. It is important to understand what the user's problem is and why the user needs a software product to solve the problem. This is determined by the frequent interactions with customers. A well-defined problem and its scope can help focus further development activities.

The requirement activity consists of collecting and analyzing requirements. Requirement collection includes product capabilities and constraints. Product capabilities qualitatively describe how well the system will perform. To obtain the qualitative requirements, we need to collect information on product functionality, usability, intended use, and future expectations. Usability refers to system reliability, performance, security, and human factors. Intended use describes the generality of a solution and how and where the system will be operated and who will use it. Future expectation describes the ease of adapting the product for new uses and how easy it is to keep the software in operation when there is a need to modify the code. Constraints are another important part of requirements collection. Schedule and resources are the two major constraints in requirements. There is a user schedule requirement. Resources refer to the limitations on the user side during development and operation of the software. These limitations can be computer and peripheral equipment, staff availability to operate and maintain the software, management support, and the cost for development and operation.

Requirement analysis includes a feasibility study and documentation. Based on the collected user requirements, further analysis is needed to determine if the requirements are feasible. A feasibility study includes cost estimation, benefit estimation, schedule and risk analysis. The documentation for requirements is the project plan, which is the foundation document of the entire project. It contains a proposal for the product itself, a description of the environment in which it is to be used, and development plans. These plans indicate the schedule, budget, and procedures of the project.

The next activity in the analysis phase is specifications, which is transforming the user-oriented requirements into a precise form oriented to the needs of software engineers. There are three major activities in the specification process: detailed aspects, documentation, and validation. The focus points of the detailed aspects are functionality, technical feasibility, and quality.Functionality refers to how to process the input information into expected results, and how the software interacts with other systems in the user environment. Technical feasibility is to examine the possibility of implementing the given functionalities, and the need of technical support, e.g., equipment and people. Quality measurement is needed to achieve the quality standard required by users. To check the quality standard, we need to focus on reliability, performance, security, and human factors.

Based on the project plan, the specification document provides technical details. It is written for the software team in a technical language. It is necessary to let the user review the specifications to ensure the proposed product is what the user wants. Prototyping can also be used for validation of the specifications. This allows the user and the software team to see the software in action and to find aspects that do not meet the requirements.

The importance of the analysis phase has been strongly reinforced in recent software development. A well-developed specification can reduce the incidence of faults in the software and minimize rework. Research indicates that increased effort and care during specification will generate significant rewards in terms of dependability, maintainability, productivity, and general software quality.

# Design Phase 

The design phase is concerned with building the system to perform as required. There are two stages of design: system architecture design and detailed design (see Figure 3.7 in Pham 2000a). The system architecture design includes system structure and the system architecture document. System structure design is the process of partitioning a software system into smaller parts. Before subdividing the system, we need to do further specification analysis, examine the details of performance requirements, security requirements, assumptions and constraints, and the need for hardware and software.

System decomposition includes subsystem process control and interface relationship. Besides determining how to control the process of each subsystem by identifying major modules, the internal and external interfaces need to be defined. Internal interface refers to how the subsystems interact with each other. External interface defines how the software interacts with its environment, e.g., user, operation, other software and hardware. The last activity in system architecture design is to initiate a system architecture document, which is part of the design document in the design phase. The system architecture document describes system components, subsystems and their interfaces.

Detailed design is about designing the program and algorithmic details. The activities within detailed design are program structure, program language and tools, validation and verification, test planning, and design documentation. Program structure optimizes the design of selecting data structures and algorithms to achieve the goal of the project. Structure quality measurement checks if the selected program structure meets the quality requirements.

The four major measurements are functionality, usability, intended use, and future expectations. To comply with the functionality requirements means that the designed algorithm should implement the functional characteristics of the proposedsystem. Usability consists of reliability, performance, security, and human factors requirements.

There are two important parts to provide reliability: fault detection and fault isolation. The design has to consider both aspects. Since performance requirements influence the selection of data structures and algorithms, it is important to check performance factors at the design phase. To estimate the performance of the design, the information on usage pattern, design structure, and installation characteristics are needed. The specifications describe the level and what security looks like while design considers its implementation.

Different types of systems may have their own particular security needs. There is a series of issues that need to be evaluated for system security: information must be kept confidential, unauthorized modification of information must be prohibited, and unauthorized withholding of information must be avoided. To check if human factors meet the requirements, the designed user interfaces and support tools are two issues to be considered. Intended use is to measure if the designed algorithms meet the stated requirements. Future expectations focus on adaptability and maintainability of the designed system. During detailed design, the selected data structures and algorithms are implemented in a particular programming language on a particular machine. Thus, choosing the appropriate program language and tools is essential.

Test plans should be initiated at design phase. These include identifying items to be tested, creating test case specifications, and generalizing the test approach. A design document is the deliverable of the design phase. It describes system architecture, module design, data object design, how quality expectations will be achieved, and the test plan.

# Coding Phase 

Coding involves translating the design into the code of a programming language, beginning when the design document is baselined. Coding comprises of the following activities: identifying reusable modules, code editing, code inspection, and final test planning (see Figure 3.8 in Pham 2000a). Identifying reusable modules is an effective way to save time and effort. Before writing the code, there may be existing code for modules of other systems or projects which is similar to the current system. These models can be reused with modification. When writing the code, developers should adopt good program styles.

A good program style is characterized by simplicity, readability, good documentation, changeability, and module independence. Generally, programming standards should be followed to ensure that the written programs are easily understood by all project team members. Writing structured code also helps to make the program easy to read and maintain. When modifying reusable code, the impact of reusable modules and the interfaces with other modules need to be considered.

Code inspection includes code reviews, quality, and maintainability. Code reviews is to check program logic and readability. This is normally conducted by other developers on the same project team and not the author of the program. Quality verification ensures that all the modules perform the functionality as described in the detailed design. Quality check focuses on reliability, performance,and security Maintainability is also checked to ensure the programs are easy to maintain. The final test plan should be ready at the coding phase. Based on the test plan initiated at the design phase, with the feedback of coding activities, the final test plan should provide details of what is to be tested, testing strategies and methods, testing schedules, and all necessary resources.

# Testing Phase 

Testing is the verification and validation activity for the software product. The goals of the testing phase are (1) to affirm the quality of the product by finding and eliminating faults in the program, (2) to demonstrate the presence of all specified functionality in the product, and (3) to estimate the operational reliability of the software. During the testing phase, program components are combined into the overall software code and testing is performed according to a developed test (Software Verification and Validation) plan.

System integration of the software components and system acceptance tests are performed against the requirements. In other words, testing during this phase determines whether all requirements have been satisfied and is performed in accordance with the reviewed software verification and validation plan. Test results are evaluated and test and verification reports are prepared to describe the outcome of the process. The testing phase (Figure 3.9 in Pham 2000a) consists of a unit test, integration test, and acceptance test.

The unit test is the process of taking a program module and running it in isolation from the rest of the software product by using prepared inputs and comparing the actual results with the results predicted by the specifications and design of the module. The unit test is the responsibility of programmers while the later stages of testing may be done by an independent testing group.

The integration test includes subsystem and system tests. The subsystem test focuses on testing the interfaces and interdependencies of subsystems or modules. The system test examines all the subsystems as a whole to determine whether specified functionality is performed correctly as the results of the software. The integration test also includes the system integration testing process which brings together all system components, hardware and software, and humanware. This testing is conducted to ensure that system requirements in real or simulated system environments are satisfied.

The acceptance test acts as a validation of the testing phase, consisting of an internal test and field test. The internal test includes a capability test and guest test, both performed in-house. The capability test examines the system in an environment configured similar to the customer environment. The guest test is conducted by the users in their software organization sites.

The field test is to install the product in a user environment and allows the user to test the product where customers often lead the test and define and develop the test cases. The field test is also called the "beta test" The acceptance test is defined as formal testing conducted to determine whether a software system satisfies its acceptance criteria and to enable the customer to determine whether the system is acceptable.When the developer's testing and system installation have been completed, acceptance testing that leads to ultimate certification begins. It is recommended that acceptance testing be performed by an independent group to ensure that the software meets all requirements. Testing by an independent group (without the developers' preconceptions about the functioning of the system) provides assurance that the system satisfies the intent of the original requirements. The acceptance test group usually consists of analysts who will use the system and members of the requirements definition group. Concurrent with all of the previous phases is the preparation of the user and maintenance manuals. The probability of fixing a known error incorrectly also increases rapidly during the latter stages. This phenomenon is of interest because an incorrect fix to a problem often causes more harm than the original problem. This may lead to an important question: Is there a good reason not to correct a software error deliberately?

# Operating Phase 

The final phase in the software lifecycle is operation. The operating phase (see Figure 3.11 in Pham 2000a) usually incorporates activities such as installation, training, support, and maintenance. After completion of the testing phase, the turnover of the software product plays a very small but important role of the life cycle. It transfers responsibility for software maintenance from the developer to the user by installing the software product.

The user is then responsible for establishing a program to control and manage the software. Installation may include system installation and providing the installation manual to the users. The training includes user training and operating staff training. User training is based primarily on major system functions and the user's need for access to them so that they understand what the functions are and how to perform them. Documentation support provides the customer with the user, reference, and system manuals. The software product is thus accepted for operational use.

Maintenance is defined as any change made to the software, either to correct a deficiency in performance (as required by the original software requirements specification), to compensate for environmental changes, or to enhance its operation. Maintenance activities include system improvement and replacement strategies. There are four types of activities in system improvement: correction of errors, adaptation to other changes, perfection of acceptable functions, and prevention of future errors. System improvement activities are similar to those of previous phases of development: analysis, design, coding, and testing.

### 4.5 Software Development Process and Its Applications

In this section, we will discuss the details of applying the generalized analytic hierarchy process (AHP) (Lee 1999) to the software development process.# 4.5.1 Analytic Hierarchy Process 

The AHP is a comprehensive mathematical framework for priority setting in a complex system. The AHP has been applied in a variety of areas since it was first developed by Saaty (1980) in the 1970s. According to Saaty, a complex system is decomposed into subsystems and represented in the hierarchical form. The element at the highest level is called the goal.

The elements at each level are the criteria of the elements at the level below. The elements at the bottom level are called the alternatives. In this way, the AHP organizes the basic rationality of the priority setting process by breaking down a multi-element complex system into its smaller constituent parts called components (or levels). The process setting can be divided into three phases: system structuring, pairwise comparison and priorities synthesis. The generalization of the AHP to systems with feedback, i.e., system with both inter-and intra-component dependence, is given in (Lee 1999).

### 4.5.2 Evaluation of Software Development Process

Software has a lifecycle, which goes through the periods of initiation, growth, maturity, and phase-out. The development of software goes through a number of phases or stages. There are several ways to structure software lifecycle into phases according to different activities during software development. After analyzing the software development process, we construct the software lifecycle into five phases: analysis, design, coding, testing, and operations.

The development phases overlap and feed information to each other. Each phase can be decomposed further to show the detailed activities under that phase (see Section 4.4). The results of a recent study on software development and its environmental factors show that analysis, design, coding, and testing take about 25 , 18,36 , and $21 \%$ of the whole software development efforts, respectively. In this application, the hierarchy structure for the design phase is discussed in this section. The same procedure can be applied to analyze the impacts among the activities to decompose the system into components and to construct the weight diagrams.

Pham (2000a) (Figures 3.12 and 3.13) shows details of the hierarchy structure of the design phase and the impact diagram of the elements in the design phase using the techniques developed by Lee (1999).

The overall priorities of the activities in the design phase are summarized in Pham (2000a, Figure 3.14). At the top-most level, we see that the weight of detailed design is approximately two to three times that of system architecture design. This is consistent with our intuition because there are more activities under detailed design and more resources are needed for these activities. Here we want to emphasize that the generalized AHP (Lee 1999) not only provides qualitative information consistent with intuition, but also quantitative information which is very instrumental in resource allocation. In the next level we see that the results obtained are consistent with the intuition. In system architecture design the resource allocated to system structure is about four times that of system architecture document. This should be evident from the amount of activities involved in system structure.Similarly, in detailed design, almost half of the resources should be allocated to program structure since it is the major activity at this level. To improve the design progress, we need to focus more on detailed design, especially on program structure. Other activities are also important, and resources allocated to these activities should also be proportional to their final weights.

Based on the results of this application using the generalized AHP, software developers can plan their schedules according to the relative weights within the design time frame. The weight diagram is useful in identifying the most important activities while conducting multiple tasks. For instance, sufficient time and effort should be spent on specification analysis before conducting system decomposition. Since the relative weight of system decomposition is about $37 \%$ and that of specification analysis is about $63 \%$, software developers should spend roughly twice as much time and effort on the latter. If the right amount of time and effort is spent on each of the activities, the development process can be made smoother, more efficient, and a better outcome can be achieved. This application presents a methodology which provides an effective way in quantifying resource allocation to enhance the software development process.

# 4.6 Software Verification and Validation 

Verification and validation (V\&V) are two ways to check whether the design satisfies the user's requirements. According to the IEEE Standard Glossary of Software Engineering Terminology:

Software verification is the process of evaluating a system or component to determine whether the products of a given development phase satisfy the conditions imposed at the start of that phase.
Software validation is the process of evaluating a system or component during or at the end of the development process to determine whether it satisfies specified requirements.
In short, Boehem (1981) expressed the difference between software verifycation and software validation as follows:

Verification: "Are we building the product right?"
Validation:'Are we building the right product?"
In other words, verification checks whether the product under construction meets the requirements definition. Validation checks whether the product's functions are in accordance to the customer's needs. Recently, an "eagle-eyed math lover" high school student, Colin Rizzio, who took the Scholastic Assessment Tests (SAT) with about 350,000 high school students on 12 October 1996, recognized the flaw in the multiple-choice answers for a question dealing with an algebraic equation.

The problem was that the question-writer had used a letter, in this case a, to represent any number, a standard practice in an algebra equation. The original "correct" answer assumed that ' V ' was positive and did not account for the possibility that it was a negative number such as -4 . Students who assumed the number could be negative had a different answer. It was the aim of the SAT to "check your work," which apparently, the testers did not (The Home News \&Tribune, 1997). As a result, the scores of up to 45,000 high-school students, who took the SAT last fall, were boosted by as much as 30 points. The math portion of the SAT test was worth 800 points.

Often, programming is done primarily by scientists or engineers who have little training in software development or programming. They are, however, highly motivated to get a program running in the shortest time possible. The consequence of expedited results is that the users find bugs in the software program after the software product is put into operation.

Although it costs the developer very little to fix faults during the development phase, i.e., the testing phase, it would definitely cost orders of magnitude more to fix faults during the operating and maintenance phases. The cost of fixing an error increases dramatically as the software lifecycle progresses (Pham 2000a).

Verification should be integrated not only in the testing phase but in all phases of the software development lifecycle. It should be noted that testing is one aspect of verification but it cannot replace the task of the verification process. In fact, verification is most effective and efficient when applied from the beginning of the development process.

Verification should be performed independently by a group other than the software developer whose interests lie in showing that the software program works and not in finding bugs or faults in the software. Therefore, an independent group of the development process is more likely to do a thorough testing and execute the software verification, coming up with a series of complex tests that may create blind spots in the evaluation process.

A good independent verification and validation (IV\&V) should: (1) have significant experience, (2) have a base of personnel skilled in IV\&V, (3) hold transferable tools with knowledable, (4) be a development team participant, and (5) be adaptable to any project.

In general, validation determines end product accuracy, e.g., code, with respect to the software requirements. It determines if the output conforms with what was required? Verification is performed at each phase and between each phase of the development lifecycle. It determines that each phase and subphase product is correct, complete, and consistent with itself and with its predecessor product.

# 4.7 Data Analysis 

Traditionally, there are two common types of failure data: time-domain data and interval-domain data. These data are usually used by practitioners when analyzing and predicting reliability applications. Some software reliability models can handle both types of data. The time-domain approach involves recording the individual times at which failure occurred, as illustrated in Table 4.3. The first failure occurred 25 min into the test, the second at 55 , the third at 70 , the fourth at 95 , the fifth at 112 , the sixth at 119 , the seventh at 143 , and the eighth failure at 187 min . Some models may require the time between failures in lieu of the actual failure time. In this example, the values $25,30,15,15,17,7,26$, and 44 should be used as the time-domain data set.The interval-domain approach is characterized by counting the number of failures occurring during a fixed period (e.g., test session, hour, week, day). Using this method, the collected data are a count of the number of failures in the interval. This approach is illustrated in Table 4.4. Using the same failures as in the timedomain example, we would record two failures in the first 1-hour interval, four failures in the second interval, one failure in the third, and one in the fourth. Intervals, however, do not need to be equally spaced for data collection. For example, if the interval for data collection is a test session, one session may last 4 hours and the next may last 8 hours. Models with assumptions that handle this situation should be considered for higher fidelity forecasts for systems with interval-domain data.

Table 4.3. Data recording for the time-domain approach

| Failure <br> records | Actual failure time <br> $(\mathrm{min})$ | Time between failures <br> $(\mathrm{min})$ |
| :--: | :--: | :--: |
| 1 | 25 | 25 |
| 2 | 55 | 30 |
| 3 | 70 | 15 |
| 4 | 95 | 15 |
| 5 | 112 | 17 |
| 6 | 119 | 7 |
| 7 | 143 | 26 |
| 8 | 187 | 44 |

The time-domain approach always provides higher accuracy in the parameter estimates with current tools but involves more data collection efforts than the interval-domain approach. The practitioners must trade off the cost of data collection with the accuracy reliability level required by the model predictions.

Table 4.4. Data recording for the interval-domain approach

| Time <br> (hours) | Observed number <br> of failures |
| :--: | :--: |
| 1 | 2 |
| 2 | 4 |
| 3 | 1 |
| 4 | 1 |

# 4.8 Failure Data Sets 

This section lists several application data sets that, throughout the book, can be used to implement and illustrate the software reliability modeling.Data Set \#1: On-line Data Entry Software Package Test Data
The small on-line data entry software package test data, available since 1980 in Japan (Ohba 1984a), is shown in Table 4.5 (Data set \#1). The size of the software has approximately 40,000 LOC. The testing time was measured on the basis of the number of shifts spent running test cases and analyzing the results. The pairs of the observation time and the cumulative number of faults detected are presented in Table 4.5.

Table 4.5. On-line IBM entry software package (data set \#1)

| Testing time <br> (day) | Failures | Cumulative <br> failures |
| :--: | :--: | :--: |
| 1 | 2 | 2 |
| 2 | 1 | 3 |
| 3 | 1 | 4 |
| 4 | 1 | 5 |
| 5 | 2 | 7 |
| 6 | 2 | 9 |
| 7 | 2 | 11 |
| 8 | 1 | 12 |
| 9 | 7 | 19 |
| 10 | 3 | 21 |
| 11 | 1 | 22 |
| 12 | 2 | 24 |
| 13 | 2 | 26 |
| 14 | 4 | 30 |
| 15 | 1 | 31 |
| 16 | 6 | 37 |
| 17 | 1 | 38 |
| 18 | 3 | 41 |
| 19 | 1 | 42 |
| 20 | 3 | 45 |
| 21 | 1 | 46 |

Data Set \#2: On-line Communication System (OCS)
The On-line Communication System (OCS) project at ABC Software Company was completed in 2000 (Pham 2003a). The project consisted of one unit-manager, one user interface software engineer, and ten software engineers/testers. The overall effort for each of the four phases in the software development process of the project can be described as follows:

| Phase | Weeks |
| :-- | :--: |
| Analysis | 7 |
| Design | 8 |
| Coding | 13 |
| Testing | 12 |The data was collected over a period of 12 weeks during which time the testing started and stopped many times. Errors detection is broken down into subcategories to help the development and testing team to sort and solve the most critical Modification Requests (MRs) first. These sub-categories are referred to as the severity level depending on the nature of the problem with 1 being the most severe problem, with 2 being the major problem and 3 being a minor problem. The data set \#2, maps into week, consists of three types of errors: severe 1, severe 2, and severe 3. The observation time (week) and the number of errors detected per week are presented in Table 4.6.

Table 4.6. OCS Failure Data (Data Set \#2)

| Week | Severe 1 | Severe 2 | Severe 3 |
| :--: | :--: | :--: | :--: |
| 1 | 4 | 7 | 10 |
| 2 | 1 | 5 | 2 |
| 3 | 0 | 0 | 4 |
| 4 | 1 | 4 | 6 |
| 5 | 1 | 4 | 6 |
| 6 | 10 | 15 | 8 |
| 7 | 4 | 6 | 4 |
| 8 | 1 | 5 | 3 |
| 9 | 1 | 1 | 1 |
| 10 | 3 | 7 | 6 |
| 11 | 0 | 0 | 1 |
| 12 | 0 | 1 | 4 |

Date Set \#3: Failure Data from Misra (1983)
A set of failure data taken from Misra (1983), given in Table 4.7, consists of three types of errors: critical, major, and minor. The observation time (week) and the number of failure detected per week are shown in Table 4.7.Table 4.7. Software failure data (data set \#3)

| Week | Hours | Cumulative <br> days | Critical <br> errors | Major <br> errors | Minor <br> errors |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 62.5 | 2.6 | 0 | 6 | 9 |
| 2 | 44 | 4.4 | 0 | 2 | 4 |
| 3 | 40 | 6.1 | 0 | 1 | 7 |
| 4 | 68 | 8.9 | 1 | 1 | 6 |
| 5 | 62 | 11.5 | 0 | 3 | 5 |
| 6 | 66 | 14.2 | 0 | 1 | 3 |
| 7 | 73 | 17.3 | 0 | 2 | 2 |
| 8 | 73.5 | 20.3 | 0 | 3 | 5 |
| 9 | 92 | 24.2 | 0 | 2 | 4 |
| 10 | 71.4 | 27.1 | 0 | 0 | 2 |
| 11 | 64.5 | 29.8 | 0 | 3 | 4 |
| 12 | 64.7 | 32.5 | 0 | 1 | 7 |
| 13 | 36 | 34 | 0 | 3 | 0 |
| 14 | 54 | 36.3 | 0 | 0 | 5 |
| 15 | 39.5 | 37.9 | 0 | 2 | 3 |
| 16 | 68 | 40.7 | 0 | 5 | 3 |
| 17 | 61 | 43.3 | 0 | 5 | 3 |
| 18 | 62.6 | 45.9 | 0 | 2 | 4 |
| 19 | 98.7 | 50 | 0 | 2 | 10 |Table 4.7. (continued)

| Week | Hours | Cumulative <br> days | Critical <br> errors | Major <br> errors | Minor <br> errors |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 20 | 25 | 51.1 | 0 | 2 | 3 |
| 21 | 12 | 51.6 | 0 | 1 | 1 |
| 22 | 55 | 53.8 | 0 | 3 | 2 |
| 23 | 49 | 55.9 | 0 | 2 | 4 |
| 24 | 64 | 58.6 | 0 | 4 | 5 |
| 25 | 26 | 59.6 | 0 | 1 | 0 |
| 26 | 66 | 62.4 | 0 | 2 | 2 |
| 27 | 49 | 64.4 | 0 | 2 | 0 |
| 28 | 52 | 66.6 | 0 | 2 | 2 |
| 29 | 70 | 69.5 | 0 | 1 | 3 |
| 30 | 84.5 | 73 | 1 | 2 | 6 |
| 31 | 83 | 76.5 | 1 | 2 | 3 |
| 32 | 60 | 79 | 0 | 0 | 1 |
| 33 | 72.5 | 82 | 0 | 2 | 1 |
| 34 | 90 | 85.8 | 0 | 2 | 4 |
| 35 | 58 | 88.2 | 0 | 3 | 3 |
| 36 | 60 | 90.7 | 0 | 1 | 2 |
| 37 | 168 | 97.7 | 1 | 2 | 11 |
| 38 | 111.5 | 102.3 | 0 | 1 | 9 |Data Set \#4: US Naval Tactical Data Systems (NTDS)
The software data set, listed in Table 4.8, was extracted from information about failures in the development of software for the real-time multi-computer complex of the US Naval Fleet Computer Programming Center of the US Naval Tactical Data Systems (NTDS) (Goel 1979a). The software consists of 38 different project modules. The time horizon is divided into four phases: production phase, test phase, user phase, and subsequent test phase. The 26 software failures were found during the production phase, five during the test phase and; the last failure was found on 4 January 1971. One failure was observed during the user phase, in September 1971, and two failures during the test phase in 1971.

Data Set \#5: Tandem Computers Software Data Project
This set of Release \#1 failure data, given in Table 4.9, is from one of four major releases of software products at Tandem Computers (Wood 1996).

Data Set \#6: On-Line Data Entry IBM Software Package
The data reported by Ohba (1984a) are recorded from testing an on-line data entry software package developed at IBM. Table 4.10 shows the pair of the observation time (days) and the cumulative number of errors that were detected.

Data Set \#7: AT\&T System T Project
The AT\&T's System $T$ is a network-management system developed by AT\&T that receives data from telemetry events, such as alarms, facility-performance information, and diagnostic messages, and forwards them to operators for further action. The system has been tested and failure data has been collected (Ehrlich, 1993). Table 4.11 shows the failures and the inter-failure as well as cumulative failure times (in CPU units).

Data Set \#8: Real-Time Control Systems (Hou et al., 1997)
The software for monitor and real-time control systems (Tohma 1991) consists of about 200 modules and each module has, on average, 1000 lines of a high-level language like FORTRAN. Table 4.12 records the software failures detected during the 111-day testing period. This actual data is concave overall with several up and downs reflecting different clusters of detected faults.

Data Set \#9: The Real-time Control System Data
The data is documented in Lyu (1996). There are in total 136 faults reported and the time-between failures (TBF) in second are listed in Table 4.13.

Data Set \#10: Real-Time Command and Control System
The data set in Table 4.14 was reported by Musa (1987) based on failure data from a real-time command and control system, which represents the failures observed during system testing for 25 hours of CPU time. The delivered number of object instructions for this system was 21700 and was developed by Bell Laboratories.Table 4.8. Naval Tactical Data System (NTDS) software error (data set \#4)

| Error no. <br> n | Time between errors <br> $\mathrm{x}_{\mathrm{k}}$ (days) | Cumulative time <br> $S_{n}:=\sum x_{k}$ (days) |
| :-- | :--: | :--: |
| Production (checkout) phase |  |  |
| 1 | 9 | 9 |
| 2 | 12 | 21 |
| 3 | 11 | 32 |
| 4 | 4 | 36 |
| 5 | 7 | 43 |
| 6 | 2 | 45 |
| 7 | 5 | 50 |
| 8 | 8 | 58 |
| 9 | 5 | 63 |
| 10 | 7 | 70 |
| 11 | 1 | 71 |
| 12 | 6 | 77 |
| 13 | 1 | 78 |
| 14 | 9 | 87 |
| 15 | 4 | 91 |
| 16 | 1 | 92 |
| 17 | 3 | 95 |
| 18 | 3 | 98 |
| 19 | 6 | 104 |
| 20 | 1 | 105 |
| 21 | 11 | 116 |
| 22 | 33 | 149 |
| 23 | 7 | 156 |
| 24 | 91 | 247 |
| 25 | 2 | 249 |
| 26 | 1 | 250 |
| Test phase |  |  |
| 27 | 87 | 337 |
| 28 | 47 | 384 |
| 29 | 12 | 396 |
| 30 | 9 | 405 |
| 31 | 135 | 540 |
| User phase |  |  |
| 32 | 258 | 798 |
| Test phase |  |  |
| 33 | 16 | 814 |
| 34 | 35 | 849 |Table 4.9. Tandem Computers software failure (CPU execution time)

| Testing time <br> (weeks) | CPU hours | Defects <br> found |
| :--: | :--: | :--: |
| 1 | 519 | 16 |
| 2 | 968 | 24 |
| 3 | 1,430 | 27 |
| 4 | 1,893 | 33 |
| 5 | 2,490 | 41 |
| 6 | 3,058 | 49 |
| 7 | 3,625 | 54 |
| 8 | 4,422 | 58 |
| 9 | 5,218 | 69 |
| 10 | 5,823 | 75 |
| 11 | 6,539 | 81 |
| 12 | 7,083 | 86 |
| 13 | 7,487 | 90 |
| 14 | 7,846 | 93 |
| 15 | 8,205 | 96 |
| 16 | 8,564 | 98 |
| 17 | 8,923 | 99 |
| 18 | 9,282 | 100 |
| 19 | 9,641 | 100 |
| 20 | 10,000 | 100 |

Table 4.10. IBM on-line data entry software testing

| No. of error | Inter-failure time | Cum. failure time |
| :--: | :--: | :--: |
| 1 | 10 | 10 |
| 2 | 9 | 19 |
| 3 | 13 | 32 |
| 4 | 11 | 43 |
| 5 | 15 | 58 |
| 6 | 12 | 70 |
| 7 | 18 | 88 |
| 8 | 15 | 103 |
| 9 | 22 | 125 |
| 10 | 25 | 150 |
| 11 | 19 | 169 |
| 12 | 30 | 199 |
| 13 | 32 | 231 |
| 14 | 25 | 256 |
| 15 | 40 | 296 |Table 4.11. Failure data from AT \& T Network-Management System (data set \#7)

| Failure index | Failure time | Interfailure time |
| :--: | :--: | :--: |
| 1 | 5.50 | 5.50 |
| 2 | 7.33 | 1.83 |
| 3 | 10.08 | 2.75 |
| 4 | 80.97 | 70.89 |
| 5 | 84.91 | 3.94 |
| 6 | 99.89 | 14.98 |
| 7 | 103.36 | 3.47 |
| 8 | 113.32 | 9.96 |
| 9 | 124.71 | 11.39 |
| 10 | 144.59 | 19.88 |
| 11 | 152.40 | 7.81 |
| 12 | 166.99 | 14.60 |
| 13 | 178.41 | 11.41 |
| 14 | 197.35 | 18.94 |
| 15 | 262.65 | 65.30 |
| 16 | 262.69 | 0.04 |
| 17 | 388.36 | 125.67 |
| 18 | 471.05 | 82.69 |
| 19 | 471.50 | 0.46 |
| 20 | 503.11 | 31.61 |
| 21 | 632.42 | 129.31 |
| 22 | 680.02 | 47.60 |

Table 4.12. Failure per day and cumulative failure (*: Interpolated data)

| Days | Faults | Cumulative <br> faults | Days | Faults | Cumulative <br> faults |
| :--: | :-- | :-- | :--: | :--: | :--: |
| 1 | $5^{*}$ | $5^{*}$ | 16 | 12 | 183 |
| 2 | $5^{*}$ | $10^{*}$ | 17 | 8 | 191 |
| 3 | $5^{*}$ | $15^{*}$ | 18 | 9 | 200 |
| 4 | $5^{*}$ | $20^{*}$ | 19 | 4 | 204 |
| 5 | $6^{*}$ | $26^{*}$ | 20 | 7 | 211 |
| 6 | 8 | 34 | 21 | 6 | 217 |
| 7 | 2 | 36 | 22 | 9 | 226 |
| 8 | 7 | 43 | 23 | 4 | 230 |
| 9 | 4 | 47 | 24 | 4 | 234 |
| 10 | 2 | 49 | 25 | 2 | 236 |
| 11 | 31 | 80 | 26 | 4 | 240 |
| 12 | 4 | 84 | 27 | 3 | 243 |
| 13 | 24 | 108 | 28 | 9 | 252 |
| 14 | 49 | 157 | 29 | 2 | 254 |
| 15 | 14 | 171 | 30 | 5 | 259 |Table 4.12. (continued)

| Days | Faults | Cumulative <br> faults | Days | Faults | Cumulative <br> faults |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 31 | 4 | 263 | 72 | 1 | 468 |
| 32 | 1 | 264 | 73 | 1 | 469 |
| 33 | 4 | 268 | 74 | 0 | 469 |
| 34 | 3 | 271 | 75 | 0 | 469 |
| 35 | 6 | 277 | 76 | 0 | 469 |
| 36 | 13 | 293 | 77 | 1 | 470 |
| 37 | 19 | 309 | 78 | 2 | 472 |
| 38 | 15 | 324 | 79 | 0 | 472 |
| 39 | 7 | 331 | 80 | 1 | 473 |
| 40 | 15 | 346 | 81 | 0 | 473 |
| 41 | 21 | 367 | 82 | 0 | 473 |
| 42 | 8 | 375 | 83 | 0 | 473 |
| 43 | 6 | 381 | 84 | 0 | 473 |
| 44 | 20 | 401 | 85 | 0 | 473 |
| 45 | 10 | 411 | 86 | 0 | 473 |
| 46 | 3 | 414 | 87 | 2 | 475 |
| 47 | 3 | 417 | 88 | 0 | 475 |
| 48 | 8 | 425 | 89 | 0 | 475 |
| 49 | 5 | 430 | 90 | 0 | 475 |
| 50 | 1 | 431 | 91 | 0 | 475 |
| 51 | 2 | 433 | 92 | 0 | 475 |
| 52 | 2 | 435 | 93 | 0 | 475 |
| 53 | 2 | 437 | 94 | 0 | 475 |
| 54 | 7 | 444 | 95 | 0 | 475 |
| 55 | 2 | 446 | 96 | 1 | 476 |
| 56 | 0 | 446 | 97 | 0 | 476 |
| 57 | 2 | 448 | 98 | 0 | 476 |
| 58 | 3 | 451 | 99 | 0 | 476 |
| 59 | 2 | 453 | 100 | 1 | 477 |
| 60 | 7 | 460 | 101 | 0 | 477 |
| 61 | 3 | 463 | 102 | 0 | 477 |
| 62 | 0 | 463 | 103 | 1 | 478 |
| 63 | 1 | 464 | 104 | 0 | 478 |
| 64 | 0 | 464 | 105 | 0 | 478 |
| 65 | 1 | 465 | 106 | 1 | 479 |
| 66 | 0 | 465 | 107 | 0 | 479 |
| 67 | 0 | 465 | 108 | 0 | 479 |
| 68 | 1 | 466 | 109 | 1 | 480 |
| 69 | 1 | 467 | 110 | 0 | 480 |
| 70 | 0 | 467 | 111 | 1 | 481 |
| 71 | 0 | 467 |  |  |  |Data Set \#11: Telecommunication System Data
The data set \#11 was reported by Zhang (2002) based on system test data for a telecommunication system. System test data consisting of two releases (Phases 1 and 2) are shown in Tables 4.15 and 4.16. In both tests, automated test and humaninvolved tests are executed on multiple test beds.

Table 4.13. The real-time control system data

| Fault | TBF | Cum. TBF | Fault | TBF | Cum. TBF |
| :--: | --: | --: | --: | --: | --: |
| 1 | 3 | 3 | 35 | 227 | 5324 |
| 2 | 30 | 33 | 36 | 65 | 5389 |
| 3 | 113 | 146 | 37 | 176 | 5565 |
| 4 | 81 | 227 | 38 | 58 | 5623 |
| 5 | 115 | 342 | 39 | 457 | 6080 |
| 6 | 9 | 351 | 40 | 300 | 6380 |
| 7 | 2 | 353 | 41 | 97 | 6477 |
| 8 | 91 | 444 | 42 | 263 | 6740 |
| 9 | 112 | 556 | 43 | 452 | 7192 |
| 10 | 15 | 571 | 44 | 255 | 7447 |
| 11 | 138 | 709 | 45 | 197 | 7644 |
| 12 | 50 | 759 | 46 | 193 | 7837 |
| 13 | 77 | 836 | 47 | 6 | 7843 |
| 14 | 24 | 860 | 48 | 79 | 7922 |
| 15 | 108 | 968 | 49 | 816 | 8738 |
| 16 | 88 | 1056 | 50 | 1351 | 10089 |
| 17 | 670 | 1726 | 51 | 148 | 10237 |
| 18 | 120 | 1846 | 52 | 21 | 10258 |
| 19 | 26 | 1872 | 53 | 233 | 10491 |
| 20 | 114 | 1986 | 54 | 134 | 10625 |
| 21 | 325 | 2311 | 55 | 357 | 10982 |
| 22 | 55 | 2366 | 56 | 193 | 11175 |
| 23 | 242 | 2608 | 57 | 236 | 11411 |
| 24 | 68 | 2676 | 58 | 31 | 11442 |
| 25 | 422 | 3098 | 59 | 369 | 11811 |
| 26 | 180 | 3278 | 60 | 748 | 12559 |
| 27 | 10 | 3288 | 61 | 0 | 12559 |
| 28 | 1146 | 4434 | 62 | 232 | 12791 |
| 29 | 600 | 5034 | 63 | 330 | 13121 |
| 30 | 15 | 5049 | 64 | 365 | 13486 |
| 31 | 36 | 5085 | 65 | 1222 | 14708 |
| 32 | 4 | 5089 | 66 | 543 | 15251 |
| 33 | 0 | 5089 | 67 | 10 | 15261 |
| 34 | 8 | 5097 | 68 | 16 | 15277 |Table 4.13. (continued)

| Fault | TBF | Cum. TBF | Fault | TBF | Cum. TBF |
| :--: | --: | --: | --: | --: | --: |
| 69 | 529 | 15806 | 103 | 108 | 42296 |
| 70 | 379 | 16185 | 104 | 0 | 42296 |
| 71 | 44 | 16229 | 105 | 3110 | 45406 |
| 72 | 129 | 16358 | 106 | 1247 | 46653 |
| 73 | 810 | 17168 | 107 | 943 | 47596 |
| 74 | 290 | 17458 | 108 | 700 | 48296 |
| 75 | 300 | 17758 | 109 | 875 | 49171 |
| 76 | 529 | 18287 | 110 | 245 | 49416 |
| 77 | 281 | 18568 | 111 | 729 | 50145 |
| 78 | 160 | 18728 | 112 | 1897 | 52042 |
| 79 | 828 | 19556 | 113 | 447 | 52489 |
| 80 | 1011 | 20567 | 114 | 386 | 52875 |
| 81 | 445 | 21012 | 115 | 446 | 53321 |
| 82 | 296 | 21308 | 116 | 122 | 53443 |
| 83 | 1755 | 23063 | 117 | 990 | 54433 |
| 84 | 1064 | 24127 | 118 | 948 | 55381 |
| 85 | 1783 | 25910 | 119 | 1082 | 56463 |
| 86 | 860 | 26770 | 120 | 22 | 56485 |
| 87 | 983 | 27753 | 121 | 75 | 56560 |
| 88 | 707 | 28460 | 122 | 482 | 57042 |
| 89 | 33 | 28493 | 123 | 5509 | 62551 |
| 90 | 868 | 29361 | 124 | 100 | 62651 |
| 91 | 724 | 30085 | 125 | 10 | 62661 |
| 92 | 2323 | 32408 | 126 | 1071 | 63732 |
| 93 | 2930 | 35338 | 127 | 371 | 64103 |
| 94 | 1461 | 36799 | 128 | 790 | 64893 |
| 95 | 843 | 37642 | 129 | 6150 | 71043 |
| 96 | 12 | 37654 | 130 | 3321 | 74364 |
| 97 | 261 | 37915 | 131 | 1045 | 75409 |
| 98 | 1800 | 39715 | 132 | 648 | 76057 |
| 99 | 865 | 40580 | 133 | 5485 | 81542 |
| 100 | 1435 | 42015 | 134 | 1160 | 82702 |
| 101 | 30 | 42045 | 135 | 1864 | 84566 |
| 102 | 143 | 42188 | 136 | 4116 | 88682 |Table 4.14. Real-time Command and Control Data (in a one-hour interval)

| Hour | Number of <br> failures | Cum. <br> Failures |
| :--: | :--: | :--: |
| 1 | 27 | 27 |
| 2 | 16 | 43 |
| 3 | 11 | 54 |
| 4 | 10 | 64 |
| 5 | 11 | 75 |
| 6 | 7 | 83 |
| 7 | 2 | 84 |
| 8 | 5 | 89 |
| 9 | 3 | 92 |
| 10 | 1 | 93 |
| 11 | 4 | 97 |
| 12 | 7 | 104 |
| 13 | 2 | 106 |
| 14 | 5 | 111 |
| 15 | 5 | 116 |
| 16 | 6 | 122 |
| 17 | 0 | 122 |
| 18 | 5 | 127 |
| 19 | 1 | 128 |
| 20 | 1 | 129 |
| 21 | 2 | 131 |
| 22 | 1 | 132 |
| 23 | 2 | 134 |
| 24 | 1 | 135 |
| 25 | 1 | 136 |

Table 4.15. Phase 1 system test data

| Week index | Exposure time <br> (cum. system test <br> hours) | Fault | Cum. fault |
| :--: | :--: | :--: | :--: |
| 1 | 356 | 1 | 1 |
| 2 | 712 | 0 | 1 |
| 3 | 1068 | 1 | 2 |
| 4 | 1424 | 1 | 3 |
| 5 | 1780 | 2 | 5 |
| 6 | 2136 | 0 | 5 |
| 7 | 2492 | 0 | 5 |
| 8 | 2848 | 3 | 8 |Table 4.15. (continued)

| Week index | Exposure time <br> (cum. system test <br> hours) | Fault | Cum. fault |
| :--: | :--: | :--: | :--: |
| 9 | 3204 | 1 | 9 |
| 10 | 3560 | 2 | 11 |
| 11 | 3916 | 2 | 13 |
| 12 | 4272 | 2 | 15 |
| 13 | 4628 | 4 | 19 |
| 14 | 4984 | 0 | 19 |
| 15 | 5340 | 3 | 22 |
| 16 | 5696 | 0 | 22 |
| 17 | 6052 | 1 | 23 |
| 18 | 6408 | 1 | 24 |
| 19 | 6764 | 0 | 24 |
| 20 | 7120 | 0 | 24 |
| 21 | 7476 | 2 | 26 |

Table 4.16. Phase 2 system test data

| Week index | Exposure time <br> (Cum. system <br> test hours) | Fault | Cum. fault |
| :--: | :--: | :--: | :--: |
| 1 | 416 | 3 | 3 |
| 2 | 832 | 1 | 4 |
| 3 | 1248 | 0 | 4 |
| 4 | 1664 | 3 | 7 |
| 5 | 2080 | 2 | 9 |
| 6 | 2496 | 0 | 9 |
| 7 | 2912 | 1 | 10 |
| 8 | 3328 | 3 | 13 |
| 9 | 3744 | 4 | 17 |
| 10 | 4160 | 2 | 19 |
| 11 | 4576 | 4 | 23 |
| 12 | 4992 | 2 | 25 |
| 13 | 5408 | 5 | 30 |
| 14 | 5824 | 2 | 32 |
| 15 | 6240 | 4 | 36 |
| 16 | 6656 | 1 | 37 |
| 17 | 7072 | 2 | 39 |
| 18 | 7488 | 0 | 39 |
| 19 | 7904 | 0 | 39 |
| 20 | 8320 | 3 | 42 |
| 21 | 8736 | 1 | 43 |# 4.9 Further Reading 

Some interesting research papers on software engineering and books are:
Frankl, P. G. and E. J. Weyuker, "Testing Software to Detect and Reduce Risk," Journal of Systems and Software, 2000, vol. 53, p. 275-286
Tahvildari, L. and A. Singh, "Software Bugs," in Wiley Encyclopedia of Electrical and Electronics Engineering, J.G. Webster (ed.), vol 19, Wiley, 1999, p. 445455
Schneidewind, N.F., "Software Maintenance," in Wiley Encyclopedia of Electrical and Electronics Engineering, J.G. Webster (ed.), vol 19, Wiley, 1999, p. 483492
Pfleeger, S. L., Software Engineering: Theory and Practice, Prentice Hall, New Jersey, 1998
Anderson, T, Software Requirements Specification and Testing, Blackwell Scientific Publications, London, 1995
Smith, D.J., Achieving Quality Software, 3rd edition, Chapman \& Hall, NewYork, 1995

### 4.10 Problems

1. List several practical system failures (since 1995) caused by software.
2. What are the differences between verification and validation? Provide several real world applications and examples.
3. Identify from articles and books at least two methodologies and/or models to support software V\&V processes. Prepare a summary of these methodologies and/or models.
4. Read three papers on software lifecycle published in the IEEE Transactions on Software Engineering. Summarize the material and relate it to the software development process.
5. Why it is important to integrate analysis, design, coding and testing in the software development process? Who should be involved in this integration and which techniques and/or methodologies are available to support this integrated approach?
6. What are the main difficulties involved in the data collection of time-domain approach and interval-domain approach?
7. Using the generalized AHP in Section 4.5, analyze the impacts among the activities and construct the weight diagrams for the analysis phase (see Section 4.4) in the development process.8. Using the generalized AHP in Section 4.5, analyze the impacts among the activities and construct the weight diagrams for the analysis phase (see Section 4.4) in the development process.
9. Using the generalized AHP in Section 4.5, analyze the impacts among the activities and construct the weight diagrams for the design phase (see Section 4.4) in the development process.
10. Using the generalized AHP in Section 4.5, analyze the impacts among the activities and construct the weight diagrams for the testing phase (see Section 4.4) in the development process.
11. Using the generalized AHP in Section 4.5, analyze the impacts among the activities and construct the weight diagrams for the operating phase (see Section 4.4) in the development process.# Software Reliability Modeling 

### 5.1 Introduction

For software qualification, it is highly desirable to have an estimate of the remaining errors in a software system. It is difficult to determine such an important finding without knowing what the initial errors are. Research activities in software reliability engineering have been studied over the past 30 years and many statistical models and various techniques have been developed for estimating and predicting reliability of software and numbers of residual errors in software. From historical data on programming errors, there are likely to be about 8 errors per 1000 program statements after the unit test. This, of course, is just an average and does not take into account any tests on the program.

There are two main types of software reliability models: the deterministic and the probabilistic. The deterministic model is used to study the number of distinct operators and operands in a program as well as the number of errors and the number of machine instructions in the program. Performance measures of the deterministic type are obtained by analyzing the program texture and do not involve any random event. Two well-known models are: Halstead's software metric and McCabe's cyclomatic complexity metric. Halstead's software metric is used to estimate the number of errors in the program, whereas McCabe's cyclomatic complexity metric (McCabe 1976) is used to determine an upper bound on the model for estimating the number of remaining software defects. In general, these models represent a growing quantitative approach to the measurement of computer software.

The probabilistic model represents the failure occurrences and the fault removals as probabilistic events. The probabilistic software reliability models can be classified into different groups (Pham 2000a):

- Error seeding
- Failure rate
- Curve fitting
- Reliability growth- Markov structure
- Time-series
- Nonhomogeneous Poisson process.

In this chapter, we discuss various types of software reliability models and methods for estimating software reliability and other performance measures such as software complexity, software safety, and the number of remaining errors.

# 5.2 Halstead's Software Metric 

Halstead's theory of software metric is probably the best-known technique to measure the complexity in a software program and the amount of difficulty involved in testing and debugging the software. Halstead (1977) uses the number of distinct operators and the number of distinct operands in a program to develop expressions for the overall program length, volume and the number of remaining defects in a program. The following notations are used:

$$
\begin{array}{ll}
n_{1} & =\text { number of unique or distinct operators appearing in a program } \\
n_{2} & =\text { number of unique or distinct operands appearing in a program } \\
N_{1} & =\text { total number of operators occurring in a program } \\
N_{2} & =\text { total number of operands occurring in a program } \\
N & =\text { length of the program } \\
V & =\text { volume of the program } \\
E & =\text { number of errors in the program } \\
I & =\text { number of machine instructions }
\end{array}
$$

The length and the volume measure of the program can be obtained by, respectively, (Halstead 1977):

$$
N=N_{1}+N_{2}
$$

and

$$
V=N \log _{2}\left(n_{1}+n_{2}\right)
$$

where

$$
\begin{aligned}
& N_{1}=n_{1} \log _{2} n_{1} \\
& N_{2}=n_{2} \log _{2} n_{2}
\end{aligned}
$$

Halstead also proposed two empirical formulae to estimate the number of remaining defects in the program, $E$, from program volume. The two formulae, namely, Halstead empirical model 1 and Halstead empirical model 2, respectively, are

$$
\hat{E}=\frac{V}{3000}
$$

and

$$
\hat{E}=\frac{A}{3000}
$$

where$$
A=\left(\frac{V}{\frac{2 n_{1}}{n_{1} N_{2}}}\right)^{\frac{3}{2}}
$$

To examine whether Halstead's software science can offer reasonable estimates for the number of remaining defects, we will discuss the following two examples.

Example 5.1: Consider the Interchange Sort Program (Fitzsimmons 1978) for the Fortran version in Table 5.1. From Table 5.1, the length and the volume for this program can be calculated as follows:

$$
N=N_{1}+N_{2}=50
$$

and

$$
\begin{aligned}
V & =N \log _{2}\left(n_{1}+n_{2}\right) \\
& =50 \log _{2}(10+7) \\
& =204
\end{aligned}
$$

From Halstead's empirical model 1, the number of remaining defects in this program can be expected to be

$$
\hat{E}=\frac{204}{3000}=0.068
$$

It should be noted that the volume for this program under the assembly language version would be 328 since it needs more effort to specify a program in assembly programming language.

Example 5.2: Let us consider Akiyama's software data (Halstead 1977) in Table 5.2, which will be used to validate Halstead's empirical model 2. The software system consists of nine modules and is written in assembly language.

Assuming that each of the S machine language steps include one operator and one operand, we obtain

$$
N_{1}=S, N_{2}=S \text {, and } N=2 S
$$

Halstead assumed that the number of distinct operators appearing in a program, $n_{1}$, was equal to the sum of the number of machine language instruction types, program calls, and unique program decisions. He further assumed that there were 64 types of machine language instructions and that only one-third of the decisions were unique. Therefore, Halstead proposed $n_{1}$ as follows:

$$
n_{1}=\frac{D}{3}+J+64
$$

Now we use the following formula:

$$
N=n_{1} \log _{2} n_{1}+n_{2} \log _{2} n_{2}
$$

to obtain $n_{2}$ when $n_{1}$ and $N$ are known. Thus, A can be also obtained. The computational results are shown in Table 5.3. From the results in Table 5.3, Halstead's empirical model 2 is close to the number of observed defects than empirical model 1.Table 5.1. Operators and operands for an interchange sort program

```
Interchange sort program
SUBROUTINE SORT (X,N)
DIMENSION X(N)
IF (N.LT.2) RETURN
DO 201 = 2,N
    DO 10 J = 1,1
    IF (X(1).GE.X(J)) GO TO 10
        SAVE = X(1)
        X(I) = X(J)
        X(J) = SAVE
10 CONTINUE
20 CONTINUE
    RETURN
    END
```

| Operators of the interchange sort program |  |
| :-- | :--: |
| Operator | Count |
| 1 End of statement | 7 |
| 2 Array subscript | 6 |
| $3=$ | 5 |
| 4 IF | 2 |
| 5 DO | 2 |
| 6 , | 2 |
| 7 End of program | 1 |
| 8.LT. | 1 |
| 9.GE. | 1 |
| $n_{1}=10$ GO TO 10 | 1 |


|  | $N_{1}=28$ |
| :-- | :--: |


| Operands of the interchange sort program |  |
| :-- | :--: |
| Operand | Count |
| 1 X | 6 |
| 2 I | 5 |
| 3 J | 4 |
| 4 N | 2 |
| 52 | 2 |
| 6 SAVE | 2 |
| $n_{2}=71$ | 1 |
|  | $N_{2}=22$ |Table 5.2. Akiyama's published data

| Program <br> module | Program <br> $(S)$ | Decisions <br> $(D)$ | Subroutine calls $(J)$ | Number of defects <br> observed $(O)$ |
| :--: | :--: | :--: | :--: | :--: |
| MA | 4032 | 372 | 283 | 102 |
| MB | 1329 | 215 | 49 | 18 |
| MC | 5453 | 552 | 362 | 146 |
| MD | 1674 | 111 | 130 | 26 |
| ME | 2051 | 315 | 197 | 71 |
| MF | 2513 | 217 | 186 | 37 |
| MG | 699 | 104 | 32 | 16 |
| MH | 3792 | 233 | 110 | 50 |
| MX | 3412 | 416 | 230 | 80 |

Table 5.3. Computational results of Akiyama's software data

| Program <br> module | $N$ | $n_{1}$ | $n_{2}$ | $A^{1.5}$ <br> $\times 10^{6}$ ) | $E$ | $V / 3000$ | Number of <br> defects <br> observed $(O)$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| MA | 8064 | 471 | 442 | 170.3 | 102 | 26.4 | 102 |
| MB | 2658 | 180 | 176 | 15.3 | 21 | 7.5 | 18 |
| MC | 10906 | 610 | 574 | 322.6 | 157 | 37.1 | 146 |
| MD | 3348 | 231 | 201 | 28.2 | 31 | 9.7 | 26 |
| ME | 4102 | 336 | 138 | 100.2 | 72 | 12.3 | 71 |
| MF | 5026 | 322 | 287 | 65.5 | 54 | 15.5 | 37 |
| MG | 1398 | 131 | 76 | 6.5 | 12 | 3.6 | 16 |
| MH | 7584 | 252 | 603 | 58.5 | 50 | 24.6 | 50 |
| MX | 6824 | 433 | 357 | 135.9 | 88 | 21.9 | 80 |

# 5.3 McCabe's Cyclomatic Complexity Metric 

A cyclomatic complexity metric measure of software proposed by McCabe (1976) is a complexity measure of the digraph based on the control flow representation of a program.

Cyclomatic complexity is a software metric that provides a quantitative measure of the logical complexity of a program by counting the decision points. For example, one should start with 1 for the straight path through the module or subroutine (McConnel 1993). Then 1 should be added each time one of the following keywords appear: IF, REPEAT, WHILE, FOR, OR, AND. Also, 1 should be added for each case in a case statement and also if the case statement lacks a default case. If the total score is less than 10 , then by using the McCabe's measure, the code is considered to be of high quality software. McCabe has suggested that a program with a high level of the metric is very difficult to produce and maintain. He recommended a total score of 10 as an upper limit for the Fortran environment (Rook 1990).In a strongly connected graph (with a path joining any pair of nodes), the cyclomatic number is equal to the maximum number of linearly independent circuits. The linearly independent circuits form a basis for the set of all circuits in $G$, and any path passing through $G$ can be expressed as a linear combination of the circuits.

The cyclomatic number $V(G)$ of a graph $G$ can be determined from the following formula:

$$
V(G)=e-n+2 p
$$

where
$e=$ number of edges in the control graph in which an edge is equivalent to a branching point in the program
$n=$ number of vertices in the control graph and a vertex is equivalent to a sequential block of code in the program
$p=$ number of connected elements (usually 1 )
The cyclomatic number of a graph with multiple connected components is equal to the sum of the cyclomatic numbers of the connected components. In any program that can be represented by a state diagram, the McCabe cyclomatic complexity metric can also be used to calculate the number of control flow paths $(F P)$, i.e.,

$$
F P=e-n+2
$$

where $e$ is the number of edges and $n$ is the number of nodes. Here, edges are represented on the diagram by arrows and nodes are shown on the diagram with circles.

Example 5.3: A control flow path is a path that considers only a single loop iteration. The program state diagram, shown in Pham (2000a) (Figure 4.1), measures the time between two switch inputs. It calculates the speed of a mini-van in which the number of edges equals 8 and the number of nodes equals 7 . Therefore, the number of control flow paths is

$$
F P=8-7+2=3
$$

The program in Figure 5.1 has three control flow paths which are: 1234567, 121234567, 123454567.

Another simple way of computing the cyclomatic number is as follows:

$$
V(G)=\pi+1
$$

where $\pi$ is the number of predicate nodes (decisions or branches) in the program. In other words, the cyclomatic number is a measure of the number of branches in a program. A branch occurs in IF, WHILE, REPEAT, and CASE statements (a GO TO statement is normally excluded from the structured program). The cyclomatic number has been widely used in predicting the number of errors and in measuring software quality.

McCabe (1976) notes that, when used in the context of the basis path testing method, the cyclomatic complexity, $V(G)$, provides an upper bound for the number of independent paths in the basis set of a program. It also provides an upper bound on the number of tests that must be conducted to ensure that all program statements have been executed at least once.It should be noted that the cyclomatic complexity is an interesting measure of whether the software designer has followed good structured programming and software standard practices. The cyclomatic complexity also estimates how difficult it will be to test all the paths in the program and thus, provide useful information of how difficult it will be to satisfy the software specifications and requirements (Basili 1984). Also, McCabe's measure will be less useful if the software developers and testing debuggers are interested in detecting all the faults (Friedman 1995).

# 5.4 Error Seeding Models 

The error seeding group models estimate the number of errors in a program by using the multistage sampling technique. Errors are divided into indigenous errors and induced errors (seeded errors). The unknown number of indigenous errors is estimated from the number of induced errors and the ratio of the two types of errors obtained from the debugging data. Models included in this group are:

- Mills' error seeding model (Mills, 1970)
- Cai's model (Cai, 1998)
- Hypergeometric distribution model (Tohma, 1991).


## Mills' Error Seeding Model

Mills'error seeding model (Mills 1970) proposed an error seeding method to estimate the number of errors in a program by introducing seeded errors into the program. From the debugging data, which consist of inherent errors and induced errors, the unknown number of inherent errors could be estimated. If both inherent errors and induced errors are equally likely to be detected, then the probability of $k$ induced errors in $r$ removed errors follows a hypergeometric distribution which is given by

$$
P\left(k ; N, n_{1}, r\right)=\frac{\binom{n_{1}}{k}\binom{N}{r-k}}{\binom{N+n_{1}}{r}}, \quad k=1,2, \ldots ., r
$$

where
$N \quad=$ total number of inherent errors
$n_{1} \quad=$ total number of induced errors
$r \quad=$ total number of errors removed during debugging
$k \quad=$ total number of induced errors in $r$ removed errors
$r-k=$ total number of inherent errors in $r$ removed errors
Since $n_{1}, r$, and $k$ are known, the MLE of $N$ can be shown to be (Huang 1984)

$$
\hat{N}=\left\lfloor N_{0}\right\rfloor+1
$$where

$$
N_{0}=\frac{n_{1}(r-k)}{k}-1
$$

If $N_{0}$ is an integer, then $N_{0}$ and $N_{0}+I$ are both the MLEs of $N$.
Example 5.4: Assume $n_{1}=10, r=15$, and $k=6$. The number of inherent errors can be estimated using equation (5.11), i.e.,

$$
\begin{aligned}
N_{0} & =\frac{n_{1}(r-k)}{k}-1 \\
& =\frac{10(15-6)}{6}-1 \\
& =14
\end{aligned}
$$

$N_{0}=14$ is an integer, therefore, both values of 14 and 15 are the MLEs of the total number of inherent errors.

However, there are some drawbacks with this model. It is expensive to conduct testing of the software and at the same time it increases the testing effort. This method was also criticized for its inability to determine the type, location, and difficulty level of the induced errors such that they would be detected equally likely as the inherent errors.

Another realistic method for estimating the residual errors in a program is based on two independent groups of programmers testing the program for errors using independent sets of test cases. Suppose that out of a total number of $N$ initial errors, the first programmer detects $n_{1}$ errors (and does not remove them at all) and the second independently detects $r$ errors from the same program.

Assume that $k$ common errors are found by both programmers (Pham 2000a, Figure 4.2). If all errors have an equal chance of being detected, then the fraction detected by the first programmer $(k)$ of a randomly selected subset of errors (e.g., $r$ ) should equal the fraction that the first programmer detects $\left(n_{1}\right)$ of the total number of initial errors $N$. In other words,

$$
\frac{k}{r}=\frac{n_{1}}{N}
$$

so that an estimate of the total number of initial errors, $N$, is

$$
\hat{N}=\frac{n_{1} r}{k}
$$

The probability of exactly $N$ initial errors with $k$ common errors in $r$ detected errors by the second programmer can be obtained using a hypergeometric distribution as follows:

$$
P\left(k ; N, n_{1}, r\right)=\frac{\binom{n_{1}}{k}\binom{N-n_{1}}{r-k}}{\binom{N}{r}}
$$and the MLE of $N$ is

$$
\hat{N}=\frac{n_{1} r}{k}
$$

which is the same as the above.
Example 5.5: Given $n_{1}=10, r=15$, and $k=6$, the number of initial errors (or inherent errors) is given by

$$
\hat{N}=\frac{n_{1} r}{k}=\frac{10(15)}{6}=25
$$

# Cai's Model 

Cai (1998) recently modified Mills' model by dividing the software into two parts: Part 0 and Part 1. This model is used to estimate the number of defects remaining in the software. The following assumptions are applied to this model:

1. There are $N$ defects remaining in the software where Part 0 contains $N_{0}$ and Part 1 contains $N_{1}$ remaining defects, i.e, $N=N_{0}+N_{1}$.
2. Each of the remaining defects has the same probability of being detected.
3. The defect is removed when detected.
4. Only one remaining defect is removed each time and no new defects are introduced.
5. There are $n$ remaining defects removed.

Let $t_{i}$ represent the time instant of the $\mathrm{i}^{\text {th }}$ remaining defect being removed, and let $Y_{i}$ be a random variable such that

$$
Y_{i}=\left\{\begin{array}{l}
0 \text { if the } \mathrm{i}^{\text {th }} \text { detected defect is contained in Part } 0 \\
1 \text { if the } \mathrm{i}^{\text {th }} \text { detected defect is contained in Part } 1
\end{array}\right.
$$

Define $N_{j}(i)$ be the number of defects remaining in Part $j$ in the time interval $\left(t_{i}, t_{i+1}\right]$ for $i=0,1,2, \ldots, n$ and $j=0$ or 1 . Assume $y_{i}$ are the observed values of $Y_{i}$ and $y_{0}=0$. Therefore,

$$
\begin{aligned}
& N_{0}(i)=N_{0}-i+\sum_{j=0}^{i} y_{j} \\
& N_{1}(i)=N_{1}-\sum_{j=0}^{i} y_{j}
\end{aligned}
$$

Let $p_{\mathrm{j}}(\mathrm{i})$ be the probability of having a defect remaining in Part $j$ detected during the time interval $\left(t_{\mathrm{i}}, t_{\mathrm{i}+1}\right]$ where $\mathrm{i}=0,1,2, \ldots, n$ and $j=0$ or 1 . Then we obtain

$$
\begin{aligned}
p_{0}(i) & =\frac{N_{0}(i)}{N_{0}(i)+N_{1}(i)} \\
& =\frac{N_{0}-i+\sum_{j=0}^{i} y_{j}}{N_{0}+N_{1}-i}
\end{aligned}
$$and

$$
\begin{aligned}
p_{1}(i) & =\frac{N_{1}(i)}{N_{0}(i)+N_{1}(i)} \\
& =\frac{N_{1}-\sum_{j=0}^{i} y_{j}}{N_{0}+N_{1}-i}
\end{aligned}
$$

Now we wish to estimate $N_{0}$ and $N_{1}$ using the MLE method. The likelihood function can be determined as follows (Cai 1998):

$$
\begin{aligned}
L\left(y_{1}, \ldots, y_{n}\right) & =P\left\{Y_{1}=y_{1}, \ldots, Y_{n}=y_{n}\right\} \\
& =\prod_{i=1}^{n} P\left\{Y_{i}=y_{i} \mid Y_{1}=y_{1}, \ldots, Y_{i-1}=y_{i-1}\right\}
\end{aligned}
$$

Note that

$$
P\left\{Y_{i}=y_{i} \mid Y_{1}=y_{1}, \ldots, Y_{i-1}=y_{i-1}\right\}=\left\{\begin{array}{ll}
p_{0}(i-1) & \text { if } y_{i}=0 \\
p_{1}(i-1) & \text { if } y_{i}=1
\end{array}\right.
$$

or, equivalently, that

$$
P\left\{Y_{i}=y_{i} \mid Y_{1}=y_{1}, \ldots, Y_{i-1}=y_{i-1}\right\}=\left[p_{0}(i-1)\right]^{1-y_{i}}\left[p_{1}(i-1)\right]^{y_{i}}
$$

where $p_{0}(i)$ and $p_{1}(i)$ are given in equations (5.15) and (5.16), respectively. Thus,

$$
L\left(y_{1}, \ldots, y_{n}\right)=\prod_{i=1}^{n}\left[p_{0}(i-1)\right]^{1-y_{i}}\left[p_{1}(i-1)\right]^{y_{i}}
$$

Taking the $\ln$ of the likelihood function, we obtain

$$
\ln L\left(y_{1}, \ldots, y_{n}\right)=\sum_{i=1}^{n}\left(1-y_{i}\right) \ln \left[p_{0}(i-1)\right]+\sum_{i=1}^{n} y_{i}\left[p_{1}(i-1)\right]
$$

Substituting $p_{0}(i)$ and $p_{1}(i)$ of equations. (5.15) and (5.16), respectively, into the above equation and taking the first derivatives with respect to $N_{0}$ and $N_{1}$, the estimates of $N_{0}$ and $N_{1}$, are determined by the following equations:

$$
\sum_{i=1}^{n} \frac{1-y_{i}}{N_{0}-i+1+\sum_{j=0}^{i-1} y_{j}}=\frac{1}{N_{0}+N_{1}-i+1}
$$

and

$$
\sum_{i=1}^{n} \frac{y_{i}}{N_{1}-\sum_{j=0}^{i-1} y_{j}}=\frac{1}{N_{0}+N_{1}-i+1}
$$# Hypergeometric Distribution Model 

Tohma et al. (1991) proposed a model for estimating the number of faults initially resident in a program at the beginning of the test or debugging process based on the hypergeometric distribution. Let $C_{i-1}$ be the cumulative number of errors already detected so far by $t_{1}, t_{2}, \ldots, t_{i-1}$, and let $N_{i}$ be the number of newly detected errors by time $t_{i}$. Assume:

1. A program initially contains $m$ faults when the test phase starts.
2. A test is defined as a number of test instances which are couples of input data and output data. In other words, the collection of test operations performed in a day or a week is called a test instance. The test instances are denoted by $t_{i}$ for $i=1,2, \ldots, n$.
3. Detected faults are not removed between test instances.

Therefore, from the latter assumption, same faults can be experienced at several test instances. Let $W_{i}$ be the number of faults experienced by test instance $t_{i}$. It should be noted that some of the $W_{i}$ faults may be those that are already counted in $C_{i-1}$, and the remaining $W_{i}$ faults account for the newly detected faults.

If $n_{i}$ is an observed instance of $N_{i}$, then we can see that $n_{i} \leq W_{i}$. Each fault can be classified into one of two categories:

- Newly discovered faults
- Rediscovered faults

If we assume that the number of newly detected faults $N_{i}$ follows a hypergeometric distribution, then the probability of obtaining exactly $n_{i}$ newly detected faults among $W_{i}$ faults is (Tohma 1991)

$$
P\left(N_{i}=n_{i}\right)=\frac{\left(\frac{m-C_{i-1}}{n_{i}}\right)\left(\frac{C_{i-1}}{W_{i}-n_{i}}\right)}{\left(\frac{m}{W_{i}}\right)}
$$

where

$$
C_{i-1}=\sum_{k=1}^{i-1} n_{k}, \quad C_{0}=0, \quad n_{0}=0
$$

and

$$
\max \left\{0, W_{i}-C_{i-1}\right\} \leq n_{i} \leq \max \left\{W_{i}, m-C_{i-1}\right\}
$$

for all $i$. Since $N_{i}$ is assumed to be hypergeometrically distributed, the expected number of newly detected faults during the interval $\left[t_{i-1}, t_{i}\right]$ is

$$
E\left(N_{i}\right)=\frac{\left(m-C_{i-1}\right) W_{i}}{m}
$$

and the expected value of $C_{i}$ is given by

$$
E\left(C_{i}\right)=m\left[1-\prod_{j=1}^{i}\left(1-p_{i}\right)\right]
$$

where

$$
p_{i}=\frac{W_{i}}{m} \quad i=1,2, \ldots
$$# 5.5 Failure Rate Models 

The failure rate group of models is used to study the program failure rate per fault at the failure intervals. Models included in this group are:

- Jelinski and Moranda (Jelinski 1972)
- Schick and Wolverton (Schick 1978)
- Jelinski-Moranda geometric (Moranda 1979)
- Moranda geometric Poisson (Littlewood 1979)
- Negative-binomial Poisson
- Modified Schick and Wolverton (Sukert 1977)
- Goel and Okumoto imperfect debugging (Goel 1979a).

This group of models studies how failure rates change at the failure time during the failure intervals. As the number of remaining faults changes, the failure rate of the program changes accordingly. Since the number of faults in the program is a discrete function, the failure rate of the program is also a discrete function with discontinuities at the failure times.

## Jelinski-Moranda Model

The Jelinski-Moranda (J-M) model (Jelsinki 1972) is one of the earliest software reliability models. Many existing software reliability models are variants or extensions of this basic model. The assumptions in this model include the following:

- The program contains N initial faults which is an unknown but fixed constant.
- Each fault in the program is independent and equally likely to cause a failure during a test.
- Time intervals between occurrences of failure are independent of each other.
- Whenever a failure occurs, a corresponding fault is removed with certainty.
- The fault that causes a failure is assumed to be instantaneously removed, and no new faults are inserted during the removal of the detected fault.
- The software failure rate during a failure interval is constant and is proportional to the number of faults remaining in the program.
The program failure rate at the ith failure interval is given by

$$
\lambda\left(t_{i}\right)=\phi[N-(i-1)], \quad i=1,2, \ldots ., N
$$

where
$\phi=$ a proportional constant, the contribution any one fault makes to the overall program
$N=$ the number of initial faults in the program
$t_{i}=$ the time between the $(\mathrm{i}-1)^{t h}$ and the $\mathrm{i}^{t h}$ failures.
For example, the initial failure intensity is

$$
\lambda\left(t_{i}\right)=\phi N
$$and after the first failure, the failure intensity decreases to

$$
\lambda\left(t_{i}\right)=\phi(N-1)
$$

and so on. The pdf and cdf of $t_{i}$ are

$$
\begin{aligned}
f\left(t_{i}\right) & =\lambda\left(t_{i}\right) e^{-\int_{0}^{t_{i}} \lambda\left(x_{i}\right) d x_{i}} \\
& =\phi[N-(i-1)] e^{-\int_{0}^{t_{i}} \lambda\left(x_{i}\right) d x_{i}} \\
& =\phi[N-(i-1)] e^{-\phi(N-(i-1)) t_{i}}
\end{aligned}
$$

and

$$
\begin{aligned}
F\left(t_{i}\right) & =\int_{0}^{t_{i}} f\left(x_{i}\right) d x_{i} \\
& =\int_{0}^{t_{i}} \phi[N-(i-1)] e^{-\phi[N-(i-1)] x_{i}} d x_{i} \\
& =1-e^{-\phi[N-i+1)] t_{i}}
\end{aligned}
$$

respectively. The software reliability function is, therefore,

$$
R\left(t_{i}\right)=e^{-\phi(N-i+1) t_{i}}
$$

The property of this model is that the failure rate is constant and the software during the testing stage is unchanged or frozen.

Suppose that the failure data set $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ is given and assume that $\phi$ is known. Using the MLE method, we obtain the likelihood function as follows:

$$
\begin{aligned}
L(N) & =\prod_{i=1}^{n} f\left(t_{i}\right) \\
& =\prod_{i=1}^{n}\left[\phi(N-(i-1)) e^{-\phi(N-(i-1)) t_{i}}\right] \\
& =\phi^{n} \prod_{i=1}^{n}[N-(i-1)] e^{-\phi \sum_{i=1}^{n}[N-(i-1)] t_{i}}
\end{aligned}
$$

and the $\log$ of the likelihood function is

$$
\ln L(N)=n \ln \phi+\sum_{i=1}^{n} \ln [N-(i-1)]-\phi \sum_{i=1}^{n}[N-(i-1)] t_{i}
$$

Taking the first partial derivative of the above function with respect to N , we obtain

$$
\frac{\partial}{\partial N} \ln L=\sum_{i=1}^{n} \frac{1}{N-(i-1)}-\phi \sum_{i=1}^{n} t_{i}
$$Set

$$
\frac{\partial}{\partial N} \ln L(N)=0
$$

then

$$
\sum_{i=1}^{n} \frac{1}{N-(i-1)}=\phi \sum_{i=1}^{n} t_{i}
$$

Thus, the MLE of $N$ can be obtained by solving the following equation:

$$
j
$$

In many applications, the parameter $\phi$ is also not known. In this case, we wish to estimate both the parameters $N$ and $\phi$ which are unknown. Again, the log likelihood function is

$$
L(N, \phi)=n \ln \phi+\sum_{i=1}^{n} \ln [N-(i-1)]-\phi \sum_{i=1}^{n}[N-(i-1)] t_{i}
$$

Taking the derivatives of $\ln L(N, \phi)$ with respect to $N$ and $\phi$, we obtain

$$
\frac{\partial}{\partial N}[\ln L(N, \phi)]=\sum_{i=1}^{n} \frac{1}{N-(i-1)}-\phi \sum_{i=1}^{n} t_{i} \equiv 0
$$

and

$$
\frac{\partial}{\partial \phi}[\ln L(N, \phi)]=\frac{n}{\phi}-\sum_{i=1}^{n}[N-(i-1)] t_{i} \equiv 0
$$

From the two equations above, we obtain

$$
\phi=\frac{\sum_{i=1}^{n} \frac{1}{N-(i-1)}}{\sum_{i=1}^{n} t_{i}}
$$

and

$$
n \sum_{i=1}^{n} t_{i}=\left[\sum_{i=1}^{n}[N-(i-1)] t_{i}\right]\left[\sum_{i=1}^{n} \frac{1}{N-(i-1)}\right]
$$

# Schick-Wolverton Model 

The Schick-Wolverton (S-W) model (Schick 1978) is a modification to the J-M model. It is similar to the J-M model except that it further assumes that the failure rate at the $\mathrm{i}^{\text {th }}$ time interval in creases with time $t_{i}$ since the last debugging. In the model, the program failure rate function between the $(\mathrm{i}-1)^{\text {th }}$ and the $\mathrm{i}^{\text {th }}$ failure can be expressed as

$$
\lambda\left(t_{i}\right)=\phi[N-(i-1)] t_{i}
$$

where $\phi$ and $N$ are the same as that defined in the J-M model and $t_{i}$ is the test time since the $(i-1)^{\text {th }}$ failure.The pdf of $t_{i}$ can be obtained as follows:

$$
f\left(t_{i}\right)=\phi[N-(i-1)] t_{i} e^{\frac{[N-(i-1) t_{i}^{2}}{2}} \quad \text { for } i=1,2, \ldots ., N
$$

Hence, the software reliability function is

$$
\begin{aligned}
R\left(t_{i}\right) & =e^{-\int_{0}^{t_{i}} l\left(t_{i}\right) d t_{i}} \\
& =e^{-\frac{\phi[N-i+1] t_{i}^{2}}{2}}
\end{aligned}
$$

We now wish to estimate $N$ assuming that $\phi$ is given. Using the MLE method, the $\log$ likelihood function is given by

$$
\begin{aligned}
\ln L(N) & =\ln \left\{\prod_{i=1}^{n} f\left(t_{i}\right)\right\} \\
& =\ln \left\{\prod_{i=1}^{n}\left(\phi[N-(i-1)] t_{i} e^{-\frac{\phi[N-(i-1)] t_{i}^{2}}{2}}\right)\right\} \\
& =n \ln \phi+\sum_{i=1}^{n} \ln [N-(i-1)]+\sum_{i=1}^{n} \ln t_{i}-\sum_{i=1}^{n} \phi[N-(i-1)] \frac{t_{i}^{2}}{2}
\end{aligned}
$$

Taking the first derivative with respect to $N$, we have

$$
\frac{\partial}{\partial N}[\ln L(N)]=\sum_{i=1}^{n} \frac{1}{N-(i-1)}-\phi \sum_{i=1}^{n} \frac{t_{i}^{2}}{2} \equiv 0
$$

Therefore, the MLE of $N$ can be obtained by solving the following equation:

$$
\sum_{i=1}^{n} \frac{1}{N-(i-1)}=\phi \sum_{i=1}^{n} \frac{t_{i}^{2}}{2}
$$

Next, we assume that both $N$ and $\phi$ are unknown. From equation (32), we obtain

$$
\frac{\partial}{\partial N}[\ln L(N, \phi)]=\sum_{i=1}^{n} \frac{1}{N-(i-1)}-\phi \sum_{i=1}^{n} \frac{t_{i}^{2}}{2} \equiv 0
$$

and

$$
\frac{\partial}{\partial \phi}[\ln L(N, \phi)]=\frac{n}{\phi}-\sum_{i=1}^{n}[N-(i-1)] \frac{t_{i}^{2}}{2} \equiv 0
$$

Therefore, the MLEs of $N$ and $\phi$ can be found by solving the two equations simultaneously as follows:

$$
\begin{aligned}
& \phi=2 \sum_{i=1}^{n} \frac{1}{[N-(i-1)] T} \\
& N=\frac{2 n}{\phi T}+\frac{\sum_{i=1}^{n}(i-1) t_{i}^{2}}{T}
\end{aligned}
$$where

$$
T=\sum_{i=1}^{n} t_{i}^{2}
$$

# Jelinski-Moranda Geometric Model 

The J-M geometric model (Moranda 1979) assumes that the program failure rate function is initially a constant $D$ and decreases geometrically at failure times. The program failure rate and reliability function of time-between-failures at the $\mathrm{i}^{t h}$ failure interval can be expressed, respectively, as

$$
\lambda\left(t_{i}\right)=D k^{i-1}
$$

and

$$
\begin{aligned}
R\left(t_{i}\right) & =e^{-\int_{0}^{\infty} \lambda\left(t_{i}\right) d t_{i}} \\
& =e^{-D k^{i-1} t_{i}}
\end{aligned}
$$

where
$D=$ initial program failure rate;
$k=$ parameter of geometric function $(0<k<1)$
If we allow multiple error removal in a time interval, then the failure rate function becomes

$$
\lambda\left(t_{i}\right)=D k^{n_{i-1}}
$$

where $n_{i-1}$ is the cumulative number of errors found up to the $(i-1)^{t h}$ time interval. The software reliability function can be written as

$$
R\left(t_{i}\right)=e^{-D k^{n_{i-1}} t_{i}}
$$

## Moranda Geometric Poisson Model

The Moranda geometric Poisson model (Moranda 1975) assumes fixed times $T, 2 T$, of equal length intervals, and that the number of failures occurring at interval $i, N_{i}$, follows a Poisson distribution with intensity rate $D k^{i-1}$. The probability of getting m failures at the $\mathrm{i}^{t h}$ interval is

$$
\operatorname{Pr}\left\{N_{i}=m\right\}=\frac{e^{-D k^{i-1}}\left(D k^{i-1}\right)^{m}}{m!}
$$

The reliability and other performance measures can be easily derived in the same manner as in the J-M model.

## Negative-binomial Poisson Model

Assume that the intensity $\lambda$ is a random variable with the gamma density function having parameters $k$ and $m$, that is,

$$
f(\lambda)=\frac{1}{\Gamma(m)} k^{m} \lambda^{m-1} e^{-k \lambda} \quad \lambda \geq 0
$$then the probability that there are exactly $n$ software failures occurring during the time interval $(0, t)$ is given by

$$
P\{N(t)=n\}=\binom{n+m-1}{n} p^{m} q^{n} \quad n=0,1,2, \ldots
$$

where

$$
p=\frac{k}{t+k} \quad \text { and } \quad q=\frac{t}{t+k}=1-p
$$

This probability is also called a negative binomial density function.

# Modified Schick-Wolverton Model 

Sukert (1977) modifies the S-W model to allow more than one failure at each time interval. The software failure rate function is given by

$$
\lambda\left(t_{i}\right)=\phi\left[N-n_{i-1}\right] t_{i}
$$

where $n_{(i-1)}$ is the cumulative number of failures at the (i-1) ${ }^{\text {th }}$ failure interval. Thus, the software reliability function is

$$
R\left(t_{i}\right)=e^{-\phi\left[N-n_{i-1}\right] \frac{t_{i}^{2}}{2}}
$$

## Goel-Okumoto Imperfect Debugging Model

Goel and Okumoto (1979b) extend the J-M model by assuming that a fault is removed with probability $p$ whenever a failure occurs. The failure rate function of the J-M model with imperfect debugging at the $\mathrm{i}^{\text {th }}$ failure interval becomes

$$
\lambda\left(t_{i}\right)=\phi[N-p(i-1)]
$$

The reliability function is

$$
R\left(t_{i}\right)=e^{-\phi[N-p(i-1)] t_{i}}
$$

It should be noted that

$$
\begin{aligned}
\lambda\left(t_{i}\right) & =\phi[N-p(i-1)] \\
& =p \phi\left[\frac{N}{p}-\left(i_{-1}\right)\right] \\
& =\phi^{\prime}\left[N^{\prime}-(i-1)\right]
\end{aligned}
$$

is the same as in the J-M model where

$$
\phi^{\prime}=p \phi \quad \text { and } \quad N^{\prime}=\frac{N}{p}
$$

### 5.6 Curve Fitting Models

The curve fitting group models uses statistical regression analysis to study the relationship between software complexity and the number of faults in a program, the number of changes, or failure rate. This group of models finds a functional relationship between dependent and independent variables by using the methods oflinear regression, nonlinear regression, or time series analysis. The dependent variables, for example, are the number of errors in a program. The independent variables are the number of modules changed in the maintenance phase, time between failures, programmers' skill, program size, etc. Models included in this group are

- Estimation of errors
- Estimation of complexity
- Estimation of failure rate


# Estimation of Errors Model 

The number of errors in a program can be estimated by using a linear or nonlinear regression model. A simple nonlinear regression model to estimate the total number of initial errors in the program, $N$, can be presented as follows:

$$
N=\sum_{i} a_{i} X_{i}+\sum_{i} b_{i} X_{i}^{2}+\sum_{i} c_{i} X_{i}^{3}+\varepsilon
$$

where $X_{i}$ is the $\mathrm{i}^{\text {th }}$ error factor; $a_{i}, b_{i}, c_{i}$ are the coefficients of the model, and $\varepsilon$ is an error term.

Typical error factors are software complexity metrics and environmental factors. Most curve fitting models involve only one error factor. Several reliability models with environmental factors will be further discussed in Chapter 8.

## Estimation of Complexity Model

Belady and Lehman (1976) proposed a model to estimate the software complexity, $C_{R}$, using the time series approach. The software complexity model is summarized as follows:

$$
C_{R}=a_{0}+a_{1} R+a_{2} E_{R}+a_{3} M_{R}+a_{4} I_{R}+a_{5} D+\varepsilon
$$

where
$R \quad=$ release sequence number
$E_{R} \quad=$ environmental factor(s) at release $R$
$M_{R} \quad=$ number of modules at release $R$
$I_{R} \quad=$ inter-release interval $R$
$D \quad=$ number of days since first release error
$\varepsilon \quad=$ error
This model is applicable for software having multiple release versions and evolving over a long period of time.

## Estimation of Failure Rate Model

Miller (1985) proposed a model to estimate the failure rate of software. Given failure times $t_{1}, t_{2}, \ldots, t_{n}$, a rough estimate of the failure rate at the $\mathrm{i}^{\text {th }}$ failure interval is

$$
\hat{\lambda}_{i}=\frac{1}{t_{i-1}-t_{i}}
$$Assuming that the failure rate is monotonically non-increasing, an estimate of this function $\lambda_{i}^{*}, i=1,2, \ldots, n$ can be obtained by using the least squared method (see Miller 1985).

# 5.7 Reliability Growth Models 

The reliability growth group of models measures and predicts the improvement of reliability programs through the testing process. The growth model represents the reliability or failure rate of a system as a function of time or the number of test cases. Models included in this group are

- Coutinho model (Coutinho 1973)
- Wall and Ferguson model (Wall 1977).


## Coutinho Model

Coutinho (1973) adapted the Duane growth model to represent the software testing process. Coutinho plotted the cumulative number of deficiencies discovered and the number of correction actions made vs the cumulative testing weeks on log-log paper. Let $N(t)$ denote the cumulative number of failures and let $t$ be the total testing time. The failure rate, $\lambda(t)$, model can be expressed as

$$
\begin{aligned}
\lambda(t) & =\frac{N(t)}{t} \\
& =\beta_{0} t^{-\beta_{1}}
\end{aligned}
$$

where $\beta_{0}$ and $\beta_{1}$ are the model parameters. The least squares method can be used to estimate the parameters of this model.

## Wall and Ferguson Model

Wall and Ferguson (1977) proposed a model similar to the Weibull growth model for predicting the failure rate of software during testing. The cumulative number of failures at time $t, m(t)$, can be expressed as

$$
m(t)=a_{0}[b(t)]^{\beta}
$$

where $\alpha_{0}$ and $\beta$ are the unknown parameters. The function $b(t)$ can be obtained as the number of test cases or total testing time. Similarly, the failure rate function at time $t$ is given by

$$
\lambda(t)=m^{\prime}(t)=a_{0} \beta b^{\prime}(t)[b(t)]^{\beta-1}
$$

Wall and Ferguson (1977) tested this model using several software failure data and observed that failure data correlate well with the model.# 5.8 Markov Structure Models 

A Markov process has the property that the future behavior of the process depends only on the current state and is independent of its past history (see Chapter 2). The Markov structure group of models is a general way of representing the failure process of software. This group of models can also be used to study the reliability and interrelationship of the modules. It is assumed that failures of the modules are independent of each other. This assumption seems reasonable at the module level since they can be designed, coded and tested independently, but may not be true at the system level. Models included in this group are:

- Markov model with imperfect debugging (Goel 1979b)
- Littlewood Markov (Littlewood 1979)
- Software safety (Tokuno 1997; Yamada 1998)


## Markov Model with Imperfect Debugging

Goel and Okumoto (1979b) proposed a linear Markov model with imperfect debugging and the transition probabilities of the model can be expressed as

$$
p_{i j}= \begin{cases}p & \text { for } j=i-1 \\ q & \text { for } j=i \\ 1 & \text { for } j=i=0 \\ 0 & \text { otherwise }\end{cases}
$$

where $p$ is the probability of successful debugging and $q=1-p$ for $i, j=0,1, \ldots, N$. In other word, $q$ is the probability of unsuccessfully debugging the fault whenever a failure occurs. The reliability function of the $\mathrm{k}^{\text {th }}$ failure interval is given by Goel (1979):

$$
R_{k}(t)=\sum_{j=0}^{k-1}\binom{k-1}{j} p^{k-j-1} q^{j} e^{-[N-(k-j-1)] t}
$$

## Littlewood Markov Model

Littlewoods model (Littlewood 1979) represents the transitions between program modules during execution as the Markov process. Two types of failures are considered in the model. The first type of failure comes from a Poisson failure process at each module. It is recognized that new errors will be introduced as modules are integrated. The second type of failure is the interface between modules. Let
$n=$ number of modules
$a_{\mathrm{ij}}=$ transition process from module $i$ to module $j$
$\lambda_{\mathrm{i}}=$ Poisson failure rate of module $i$
$q_{i j}=$ probability that transition from module $i$ to module $j$ fails
$\pi_{\mathrm{i}}=$ limiting distribution of the process
Assuming that failures at modules and interfaces are independent of each other, Littlewood (1979) has shown that the program failure process is asymptotically a Poisson process with failure rate$$
\sum_{i=1}^{n} \pi_{i}\left(\lambda_{i}+\sum_{i \neq j} a_{i j} q_{i j}\right)
$$

as $\lambda_{\mathrm{i}}$ and $q_{i j}$ approach zero.

# Software Safety Model 

Yamada et al. (1998) proposed a software safety model to describe the time-dependent behavior of the software using Markov processes. The assumptions in this safety model include:

- When the software system is operating, the holding times of the safety and the unsafe state follow exponential distributions with means $1 / \theta$ and $1 / \eta$, respectively.
- A debugging activity is performed when a software failure occurs. Debugging activities are perfect with probability $a$, while they are imperfect with probability $b$.
- Software reliability growth occurs in cases of perfect debugging. The time interval between software failure occurrences follows an exponential distribution with mean $1 / \lambda_{\mathrm{n}}$ where $\mathrm{n}=0,1,2, \ldots$ denotes the cumulative number of corrected faults.
- The probability that two or more software failures occur simultaneously is negligible.
Consider a stochastic process $\{X(t), t \geq 0\}$ representing the state of the software system at time $t$. The state space of $\{X(t), t \geq 0\}$ is defined as
$W_{n}=$ the system is operating safety
$U_{n}=$ the system falls into the unsafe state.
Yamada et al. (1998) use Moranda's model to describe the software reliability growth process. When $n$ faults have been corrected, the failure intensity for the next software failure occurrence $\lambda_{n}$ is

$$
\lambda_{n}=D k^{n}
$$

where $D>0$ and $0<k<1$ are the initial failure rate and the decreasing ratio of the failure rate, respectively.

Software safety is defined as the probability that the system does not fall into any unsafe states at time point $t$ and is given as follows (Yamada 1998):

$$
S(t)=\sum_{n=0}^{\infty} p_{n}(t)
$$

where

$$
\begin{aligned}
P_{n}(t) & =P\left\{X(t)=W_{n}\right\} \\
& =A_{n} e^{-\left(\lambda_{n}+\theta+\eta\right) t}+\sum_{i=0}^{n} B_{n i} e^{-a \lambda_{i} t}
\end{aligned}
$$

and the constant coefficients $A_{n}$ and $B_{n i}$ are given by$$
\begin{aligned}
& A_{n}=\frac{-\theta \prod_{j=0}^{n-1} a \lambda_{j}}{\prod_{j=0}^{n}\left(a \lambda_{j}-\lambda_{n}-\theta-\eta\right)} \\
& B_{n i}=\frac{\left(\lambda_{n}+\eta-a \lambda_{i}\right) \prod_{j=0}^{n-1} \lambda_{j}}{\left(\lambda_{n}+\theta+\eta-a \lambda_{i}\right) \prod_{j=0 \neq j \neq i}^{n}\left(\lambda_{j}-\lambda_{i}\right)}
\end{aligned}
$$

# 5.9 Time Series Models 

In this section, we discuss a general time series model, called Autoregressive Integrated Moving Average (ARIMA), that was studied by Box and Jenkins (Box et al. 1994).

The ARIMA models of order $(p, d, q)$ can be expressed as follows:

$$
\begin{aligned}
z_{t}= & \delta+\phi_{1} z_{t-1}+\phi_{2} z_{t-2}+\ldots+\phi_{p} z_{t-p} \\
& +a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-1}-\ldots-\theta_{q} a_{t-q}
\end{aligned}
$$

where
$\delta=$ mean of $z_{t}, t=0,1,2, \ldots$
$z_{t}=$ observed value at time $t$
$\hat{z}_{t}=$ the expected value of $z_{t}$
$a_{t}=z_{t}-\hat{z}_{t}$
$=$ white noise at the $\mathrm{t}^{\text {th }}$ time period; its value follows the normal distribution with mean 0
$p=$ the order number of autoregression (AR)
$d=$ the value of difference order of original data
$\mathrm{q}=$ the order number of moving average (MA)
Assume $y_{1}, y_{2}, \ldots, y_{n}$ denote the number of cumulative failure of software during testing in unit time $1,2, \ldots, n$. If the $n$ values do not fluctuate around a constant mean or do not fluctuate with constant variance, then this process is called a non-stationary time series process. In other words, a time series is stationary if the statistical properties of the time series are essentially constant through time.

In the non-stationary case, one can take the first or second difference of the values and examine if the transformed series is a stationary case.Let $z_{t}$ be the number of failures in the $\mathrm{t}^{\text {th }}$ testing period, then $z_{t}$ can be written as

$$
z_{t}=y_{t}-y_{t-1} \text { where } t=2, \ldots, n
$$

and $w$ is the first difference of z (or the second difference of $y_{1}, y_{2}, \ldots, y_{n}$ ), then we obtain as follows:

$$
\begin{aligned}
w_{t} & =z_{t}-z_{t-1}=\left(y_{t}-y_{t-1}\right)-\left(y_{t-1}-y_{t-2}\right) \\
& =y_{t}-2 y_{t-1}+y_{t-2} \quad \text { where } t=3,4, \ldots, n
\end{aligned}
$$

From equation (5.52), we can easily obtain the ARIMA function in term of $y_{1}, y_{2}, \ldots, y_{n}$ using equation (5.53). For example, consider $p=0, d=2$ and $q=3$. Then the ARIMA for $y$, the values of cumulative failure number can be calculated as follows.

It can be expressed that

$$
w_{t}=\delta+a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\theta_{3} a_{t-3}
$$

and, therefore, we obtain

$$
y_{t}-2 y_{t-1}+y_{t-2}=\delta+a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\theta_{3} a_{t-3}
$$

Equation (5.55) indicates that the second differences $\left\{w_{t}\right\}$ constitute a series of moving linear combinations of $\left\{a_{t-3}, a_{t-2}, a_{t-1}, a_{t}\right\}$ weighted by the weight function $\left\{-\theta_{3},-\theta_{2},-\theta_{1}, 1\right\}$ and can be used to estimate as well as predict the reliabi- lity of the software.

# 5.10 Non-homogeneous Poisson Process Models 

The non-homogeneous Poisson Process (NHPP) group of models provides an analytical framework for describing the software failure phenomenon during testing. The main issue in the NHPP model is to estimate the mean value function of the cumulative number of failures experienced up to a certain point in time. Models included in this group are

- Musa exponential (Musa 1987)
- Goel and Okumoto NHPP (Goel 1979a)
- S-shaped growth (Ohba, 1984b; Yamada 1983,1984)
- Hyperexponential growth (Huang 1984; Ohba 1984a)
- Discrete reliability growth (Yamada 1985)
- Testing-effort dependent reliability growth (Yamada 1986, 1993)
- Generalized NHPP (Pham 1997a, 1999b, 2000a, 2003a)

In Chapter 2, the NHPP represents the number of failures experienced up to time $t$ as an NHPP, $\{N(t), t \geq 0\}$. The main issue in the NHPP model is to determine an appropriate mean value function to denote the expected number of failuresexperienced up to a certain point in time. With different assumptions, the model will result with different functional forms of the mean value function.

Based on the NHPP assumptions in Chapter 2, it can be shown that $N(t)$ has a Poisson distribution with mean $m(t)$, i.e.,

$$
\operatorname{Pr}\{N(t)=k\}=\frac{[m(t)]^{k}}{k!} e^{-m(t)} \quad k=0,1,2, \ldots
$$

By definition, the mean value function of the cumulative number of failures, $m(t)$, can be expressed in terms of the failure intensity function of the software, i.e.,

$$
m(t)=\int_{0}^{t} \lambda(s) d s
$$

The reliability function of the software is

$$
R(t)=e^{-m(t)}=e^{-\int_{0}^{t} \lambda(s) d s}
$$

Goel and Okumoto's NHPP model (Goel 1979a, 1980) belongs to this class. Other types of mean value functions suggested by Ohba (1984a), Yamada and Osaki (1985), Pham and Zhang (1997a), and Pham (1999b, 2000a) are the delayed S-shaped growth model, inflection S-shaped growth model, and hyperexponential growth model. We will further discuss NHPP models in Chapter 6.

# 5.11 Further Reading 

Some interesting papers related to the subject discussed in this chapter are:
Cai K-Y, (1998) "On estimating the number of defects remaining in software," Journal of Systems and Software, vol. 40(l)

Boehm BW, (1981) Software Engineering Economics, Prentice-Hall, Englewood Cliffs

Malaiya YK, Karunanithi N, Verma P, (1992) "Predictability of softwarereliability models," IEEE Transactions on Reliability. vol. 41 no. 4, pp 539-546

Pham H, (1999a) "Software Reliability," a chapter in Wiley Encyclopedia of Electrical and Electronic Engineering, Editor: John Webster, Wiley: pp 565-578

### 5.12 Problems

1. Figure P.4.1 (in Pham 2000a, page 101) illustrates a program used in a toaster. The program scans the lever switch until a user pushes down the bread to be toasted. The heater is energized. The heat time is determined from the lightdark switch on the side of the toaster. After the time is input in Step5 , it is checked against valid times. If the number is less than 1 or greater than 10 , the heat is turned off and the toast pops up because the input is incorrect. This time number should be an integer between one and ten. A value of one dictates a short heating time of 10 seconds, resulting in light toast. Higher values dictate longer heating times. The program decreases the time number until the remaining time equals zero. The heater is then turned off and the toast pops up. The number of program control flow paths equals three. Determine the number of control flow paths in the program shown in Figure P.4.1 (Pham 2000a).
2. Suppose that the failure data $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ is given. Find the maximum likelihood estimates for the parameters $N$ and $\phi$ of the modified Schick Wolverton model.
3. Show that the mean time to the next failure of the $\mathrm{S}-\mathrm{W}$ model is given by

$$
M T T F_{i}=\sqrt{\frac{\pi}{2 \phi(N-i+1)}}
$$

4. Derive equations (5.21) and (5.22).
5. Assume that a new fault is introduced during the removal of a detected fault with a probability $q$. Determine the probability function of removing $k$ induced errors and $r-k$ indigenous errors in $m$ tests.
6. Using the Naval Tactical Data Systems (NTDS) failure data (data set \#4 in Chapter 4):
(a) Calculate the maximum likelihood estimates for the parameters of the Jelinski-Moranda (J-M) model based on all available NTDS data.
(b) Choose another software reliability model, other than NHPP models, and repeat question (a). Is the new model better or worse? Explain and justify your results.# Imperfect-debugging Models 

### 6.1 Introduction

Since computers are being used increasingly to monitor and control both safetycritical and civilian systems, there is a great demand for high-quality software products. Reliability is a primary concern for both software developers and software users.

Research activities in software reliability engineering have been conducted and a number of NHPP software reliability growth models have been proposed to assess the reliability of software. In fact, software reliability models based on the NHPP have been quite successful tools in practical software reliability engineering. These models consider the debugging process as a counting process characterized by its mean value function. Software reliability can be estimated once the mean value function is determined. Model parameters are usually estimated using either the maximum likelihood method or regression. Different models have been built upon different assumptions.

Software reliability assessment is increasingly important in developing and testing new software products. Before newly developed software is released to the user, it is extensively tested for errors that may have been introduced during development. Although detected errors are removed immediately, new errors may be introduced during debugging. Software that contains errors and is released to the market incurs high failure costs. Debugging and testing, on the other hand, reduces the error content but increases development costs. Thus, there is a need to determine the optimal time to stop software testing. During system testing, reliability measure is an important criterion in deciding when to release the software. Several other criteria, such as the number of remaining errors, failure rate, reliability requirements, or total system cost, may be used to determine optimal testing time.

This chapter discusses stochastic reliability models for the software failure phenomenon based on a non-homogeneous Poisson process (NHPP). Allowing both the error content function and the error detection rate to be time-dependent, a generalized software reliability model and an analytical expression for the mean value function are presented. Numerous existing models based on NHPP are also summarized. Several applications and numerical examples are included to illustratethe results. A general function for calculating the mean time between failures (MTBF) of software systems based on the NHPP is also presented. An NHPP is a realistic model for predicting software reliability and has a very interesting and useful interpretation in debugging and testing the software.

Notation

| $m(t)$ | Expected number of errors detected by time $t$ ("mean value function") |
| :-- | :-- |
| $a(t)$ | Error content function, i.e., total number of errors in the software |
|  | including the initial and introduced errors at time $t$ |
| $b(t)$ | Error detection rate per error at time $t$ |
| $N(t)$ | Random variable representing the cumulative number of software errors |
|  | detected by time $t$ |
| $y(t)$ | Actual values of $N(t)\left(y_{i}:=y\left(t_{i}\right)\right)$ |
| $S_{j}$ | Actual time at which the $j$ th error is detected |
| $R(s l t)$ | Reliability during $(t, t+s)$ given that the last error occurred at time $t$ |

# 6.2 Parameter Estimation 

Parameter estimation is of primary importance in software reliability prediction. Once the analytical solution for $m(t)$ is known for a given model, the parameters in the solution need to be determined. Parameter estimation is achieved by applying a technique of MLE, the most important and widely used estimation technique. In many cases, the maximum likelihood estimators are consistent and asymptotically normally distributed as the sample size increases (Zhao 1996). In this chapter, we only discuss the MLE technique to estimate the unknown parameters for the software reliability models. Depending on the format in which test data are available, two different approaches are frequently used. A set of failure data is usually collected in one of two common ways (see Chapter 4) and is discussed next.

## Type 1 Data: Interval Domain Data

Assuming that the data are given for the cumulative number of detected errors $y_{i}$ in a given time-interval $\left(0, t_{i}\right)$ where $i=1,2, \ldots, n$ and $0<t_{1}<t_{2}<\ldots<t_{n}$, then the $\log$ likelihood function (LLF) takes on the following form:

$$
L L F=\sum_{i=1}^{n}\left(y_{i}-y_{i-1}\right) \cdot \log \left[m\left(t_{i}\right)-m\left(t_{i-1}\right)\right]-m\left(t_{n}\right)
$$

Thus the maximum of the LLF is determined by the following system of equations:

$$
0=\sum_{i=1}^{n} \frac{\frac{\partial}{\partial \theta} m\left(t_{i}\right)-\frac{\partial}{\partial \theta} m\left(t_{i-1}\right)}{m\left(t_{i}\right)-m\left(t_{i-1}\right)}\left(y_{i}-y_{i-1}\right)-\frac{\partial}{\partial \theta} m\left(t_{n}\right)
$$

where for $\theta$ each of the unknown parameters is to be substituted. Using the observed failure data $\left(t_{i}, y_{i}\right)$ for $i=1,2, \ldots, n$, we can use the mean value function $m\left(t_{i}\right)$ to determine the expected number of errors to be detected by time $t_{i}$ for $i=n$ $+1, n+2$, etc.Type 2 Data: Time Domain Data
Assuming that the data are given for the occurrence times of the failures or the times of successive failures, i.e., the realization of random variables $S_{j}$ for $j=1,2$, $n$. Given that the data provide $n$ successive times of observed failures $s_{\mathrm{j}}$ for $0 s_{1} \leq s_{2}$ $\leq \ldots s_{n}$, we can convert these data into the time between failures $x_{i}$ where $x_{i}=s_{i}-\mathrm{s}_{i-1}$ for $i=1,2, \ldots, n$. Given the recorded data on the time of failures, the log likelihood function takes on the following form:

$$
L L F=\sum \log \left[\lambda\left(s_{i}\right)\right]-m\left(s_{n}\right)
$$

The MLE of unknown parameters $\theta=\left(\theta_{1}, \theta_{2}, \ldots ., \theta_{6}\right)$ can be obtained by solving the following equations:

$$
0=\sum_{i=1}^{n} \frac{\frac{\partial}{\partial \theta} \lambda\left(S_{i}\right)}{\lambda\left(S_{i}\right)}-\frac{\partial}{\partial \theta} m\left(S_{n}\right)
$$

where

$$
\lambda(t)=\frac{\partial}{\partial t} m(t)
$$

and for $\theta$ each of the unknown parameters is to be substituted.
In general, the equations to be solved for the MLE of the system parameters are nonlinear. One can easily obtain the MLE of unknown parameters for an arbitrary mean value function of a given set of test data by using the iterative Newton method. One can also use Microsoft Excel to obtain the MLE unknown parameters by directly maximizing the likelihood function from either equation (6.1) or equation (6.3).

# 6.3 Model Selection 

Once the analytical expression for the mean value function $m(t)$ is derived, the parameters of the mean value function need to be estimated, which is usually carried out by using the MLE method discussed in Section 6.2.

There are four common criteria, such as the sum of squared errors (SSE), mean squared errors (MSE), the Akaike's information criterion (AIC), and predictiveratio risk (PRR), that are commonly used for the model comparison of goodness-of-fit (descriptive power) and predictive power and we will use them for model illustrations.

SSE criteria: SSE can be calculated as follows:

$$
S S E=\sum_{j=1}^{k} \sum_{i=1}^{n}\left[y_{i j}-\hat{m}_{j}\left(t_{i}\right)\right]^{2}
$$

where $y_{\mathrm{ij}}$ is total number of type $j$ failures observed at time $t_{\mathrm{i}}$ according to the actual data and $m_{j}\left(t_{i}\right)$ is the estimated cumulative number of type $j$ failures at time $t_{i}$ for $i=1,2, \ldots, n$ and $j=1,2, \ldots, k$.MSE criteria: MSE is calculated as follows:

$$
\mathrm{MSE}=\frac{\sum_{j=1}^{k} \sum_{i=1}^{n}\left(m_{j}\left(t_{i}\right)-y_{i j}\right)^{2}}{k \cdot n-N}
$$

The MSE measures the distance of a model estimate from the actual data with the consideration of the number of observations and the number of parameters $(N)$ in the model.

AIC criteria (Akai 1974): AIC is calculated as follows:

$$
A I C=-2 \cdot \log (\text { likelihood function at its maximum value })+2 N
$$

where $N$ represents the number of parameters in the model. The AIC measures the ability of a model to maximize the likelihood function that is directly related to the degrees of freedom during fitting, increasing the number of parameters will usually result in a better fit. AIC criterion takes the degree of freedom into consideration by assigning a model with more parameters a larger penalty.

PRR criteria (Pham 2003a): The predictive-ratio risk (PRR) is defined as follows:

$$
\mathrm{PRR}=\sum_{j=1}^{k} \sum_{i=1}^{n}\left(\frac{m_{j}\left(\hat{t}_{i}\right)-y_{i j}}{m_{j}\left(\hat{t}_{i}\right)}\right)^{2}
$$

where $y_{i j}$ is total number of type $j$ failures observed at time $t_{\mathrm{i}}$ according to the actual data and $m_{j}\left(t_{i}\right)$ is the estimated cumulative number of type $j$ failures at time $t_{\mathrm{i}}$ for $i=1,2, \ldots, n$ and $j=1,2, \ldots, k$.

It is worth noting that the PRR criterion uses the risk-of-underestimation by assigning a larger penalty to a model that has underestimated the cumulative number of failures. PRR measures the distance of model estimates from the actual data against with the model estimate.

For all these four criteria - PRR, MSE, SSE, and AIC - the smaller the value, the better the model fits, relative to other models run on the same data set.# 6.4 NHPP Exponential Models 

In this section we will describe various types of NHPP SRGM models.

## Goel-Okumoto Model

The Goel-Okumoto model (also called as exponential NHPP model) is based on the following assumptions:

1. All faults in a program are mutually independent from the failure detection point of view.
2. The number of failures detected at any time is proportional to the current number of faults in a program. This means that the probability of the failures for faults actually occurring, i.e., detected, is constant.
3. The isolated faults are removed prior to future test occasions.
4. Each time a software failure occurs, the software error which caused it is immediately removed, and no new errors are introduced.

This is shown in the following differential equation:

$$
\frac{\partial m(t)}{\partial t}=b[a-m(t)]
$$

where $a$ is the expected total number of faults that exist in the software before testing and $b$ is the failure detection rate or the failure intensity of a fault.

Theorem 6.1 (Goel 1979a): The mean value function solution of the differential equation (6.9) is given by

$$
m(t)=a\left(1-e^{-b t}\right)
$$

This model is known as the Goel-Okumoto model (Goel 1979a).
For Type-I data, the estimate of parameters $a$ and $b$ of the Goel-Okumoto model using the MLE method discussed in Section 6.2, can be obtained by solving the following equations simultaneously:

$$
\begin{gathered}
a=\frac{y_{n}}{\left(1-e^{-b t_{n}}\right)} \\
\frac{y_{n} t_{n} e^{-b t_{n}}}{1-e^{-b t_{n}}}=\sum_{k=1}^{n} \frac{\left(y_{k}-y_{k-1}\right)\left(t_{k} e^{-b t_{k}}-t_{k-1} e^{-b t_{k-1}}\right)}{\left(e^{-b t_{k-1}}-e^{-b t_{k}}\right)}
\end{gathered}
$$

Similarly, for Type-II data, the estimate of parameters $a$ and $b$ using the MLE method can be obtained by solving the following equations:

$$
\begin{aligned}
& a=\frac{n}{\left(1-e^{-b S_{n}}\right)} \\
& \frac{n}{b}=\sum_{i=1}^{n} s_{i}+\frac{n s_{n} e^{-b S_{n}}}{1-e^{-b S_{n}}}
\end{aligned}
$$Let $\hat{a}$ and $\hat{b}$ be the MLE of parameters $a$ and $b$, respectively. We can then obtain the MLE of the mean value function (MVF) and the reliability function as follows:

$$
\begin{aligned}
\hat{m}(t) & =\hat{a}\left[1-e^{-\hat{b} t}\right] \\
\hat{R}(x \mid t) & =e^{-\hat{a}\left[e^{-\hat{m}}-e^{-\hat{b}(t+\alpha)}\right]}
\end{aligned}
$$

It is of interest to determine the variability of the number of failures at time $t, N(t)$. One can approximately obtain the confidence intervals for $N(t)$ based on the Poisson distribution as

$$
\hat{m}-z_{\alpha} \sqrt{\hat{m}(t)} \leq N(t) \leq \hat{m}(t)+z_{\alpha} \sqrt{\hat{m}(t)}
$$

where $\mathrm{z}_{\alpha}$ is $100(1+\alpha) / 2$ percentile of the standard normal distribution, i.e., $N(0,1)$.
Example 6.1: The data set \#10 (in Table 4.14, Chapter 4) was reported by Musa (1987) based on failure data from a real-time command and control system, which represents the failures observed during system testing for 25 hours of CPU time. The delivered number of object instructions for this system was 21700 and was developed by Bell Laboratories.

It should be noted that this data set belongs to a concave class, therefore, it seems reasonable to use the Goel-Okumoto NHPP model to describe the failure process of the software system. From the failure data, the two unknown parameters, $a$ and $b$, can be obtained using equation (6.12) and the estimated values for the two parameters are

$$
\hat{a}=142.3153 \quad \hat{b}=0.1246
$$

Recall that $\hat{a}$ is an estimate of the expected total number of failures to be eventually detected and $\hat{b}$ represents the number of faults detected per fault per unit time (hour). The estimated mean value function and software reliability function, respectively, are

$$
\hat{m}(t)=142.3153\left(1-e^{-0.1246 t}\right)
$$

and

$$
\hat{R}(x \mid t)=e^{-(142.3153)\left[e^{(0.124 t t}-e^{-(0.124 t)(t+t)}\right]}
$$

The above two functions can be used to determine when to release the software system or the additional testing effort required when the system is ready for release. Let us assume that failure data from only 16 hours of testing are available and from the data set \#10 (Table 4.14, Chapter 4), a total of 122 failures have been observed. Based on these data and using the MLE method, the estimated values for the two parameters are

$$
\hat{a}=138.3779 \text { and } \hat{b}=0.1334
$$

and the estimated mean value function becomes

$$
\hat{m}(t)=138.3779\left(1-e^{-0.1334 t}\right)
$$The reliability of the software system is

$$
\hat{R}(x \mid t)=e^{-(138.3779)\left[e^{(0.1334) t}-e^{-(0.1334)(t+x)}\right]}
$$

An estimate number of remaining errors after 16 hours of testing is 16.38 with a $90 \%$ confidence interval of $(4.64,28.11)$. Similarly, the estimated current software reliability for the next hour is 0.129 and the corresponding $90 \%$ confidence interval is $(0.019,0.31)$.

Next, suppose the problem of interest is to know how much additional testing is needed in order to achieve an acceptable number of remaining errors so that the software can be released for operational use. For example, we would want to release the software if the expected number of remaining errors is less than or equal to 10 . In the above analysis, we learned that the best estimate of the remaining errors in the software after 16 hours of testing is about 17 . Therefore, testing has to continue in the hope that additional faults can be detected. If we were to carry on a similar task after each additional hour of testing, we can expect to obtain another seven additional errors during the next 4 hours (see Table 6.1). In other words, the expected number of remaining errors after 20 hours would be 9.8 so that the above objective would be met.

Table 6.1. Software reliability performance measures

| Testing <br> time T | a | b | Remaining <br> errors | Reliability <br> $R(0.1 / T)$ |
| :--: | :--: | :--: | :--: | :--: |
| 16 | 138.3779 | 0.1333 | 16.4 | 0.8049 |
| 17 | 133.7050 | 0.1432 | 11.7 | 0.8466 |
| 18 | 141.2543 | 0.1274 | 14.3 | 0.8349 |
| 19 | 139.7190 | 0.1304 | 11.7 | 0.8591 |
| 20 | 138.8495 | 0.1323 | 9.8 | 0.8786 |
| 21 | 140.3408 | 0.1290 | 9.3 | 0.8871 |
| 22 | 140.1002 | 0.1296 | 8.1 | 0.9010 |
| 23 | 141.9104 | 0.1255 | 7.9 | 0.9060 |
| 24 | 142.0264 | 0.1252 | 7.0 | 0.9162 |
| 25 | 142.3153 | 0.1246 | 6.3 | 0.9248 |

# Musa Exponential Model 

Musa (1985) proposed a similar model to the Goel-Okumoto model by considering the relationship between execution time and calendar time. Let $m(t)$ be the number of failures discovered as a result of test case runs up to the time of observation. Musa obtained the differential equation as follows:

$$
\frac{\partial m(t)}{\partial t}=\frac{c}{n T}[a-m(t)]
$$

where
$a=$ number of failures in the program
$c=$ the testing compression factor
$T=$ mean time to failure at the beginning of the test
$n=$ total number of failures possible during the maintained life of the program$t=$ execution time or the total CPU time utilized to complete the test case runs up to a time of observation.

Theorem 6.2 (Musa 1985): The mean value function of the differential equation (6.14) can be easily solved as follows:

$$
m(t)=a\left(1-e^{-\frac{c t}{n T}}\right)
$$

This model is often called the Musa exponential model.
The failure intensity function is

$$
\lambda(t)=\frac{c}{n T}(a-m(t))
$$

The reliability function and pdf, respectively, are

$$
R(t)=e^{-a\left(1-e^{-\frac{c}{n T} t}\right)}
$$

and

$$
f(t)=\frac{c}{n T} a e^{-\frac{c}{n T} t} e^{-a\left(1-e^{-\frac{c}{n T} t}\right)}
$$

Suppose we have observed k failures of the software and suppose that the failure data set $\left\{t_{1}, t_{2}, \ldots t_{k}\right\}$ is given where $t_{i}$ is the observed time between the $(i-1)^{\text {th }}$ and the $i^{\text {th }}$ failure. Here we want to estimate the unknown parameters $a$ and $c$. Using the MLE method, the likelihood function is obtained as

$$
\begin{aligned}
L(a, c) & =\prod_{i=1}^{k} f\left(t_{i}\right) \\
& =\left(\frac{a c}{n T}\right)^{\mathrm{k}}\left(e^{-\frac{c}{n T} \sum_{i=1}^{k} t_{i}}\right) \mathrm{e}^{-a \sum_{i=1}^{k}\left(1-e^{-\frac{c}{n T} t_{i}}\right)}
\end{aligned}
$$

The log likelihood function is given by

$$
\ln L=k \ln \left(\frac{a c}{n T}\right)-\frac{c}{n T} \sum_{i=1}^{k} t_{i}-a \sum_{i=1}^{k}\left[1-e^{-\frac{c}{n T} t_{i}}\right]
$$

The first derivative of the log likelihood function with respect to the unknown parameters $c$ and $a$ are

$$
\frac{\partial}{\partial c} \ln L=k c \frac{1}{n T} \sum_{i=1}^{k} t_{i}-\frac{a}{n T} \sum_{i=1}^{k} t_{i} e^{-\frac{c}{n T} t_{i}} \equiv 0
$$

and

$$
\frac{\partial}{\partial a} \ln L=\frac{k}{a}-\sum_{i=1}^{k}\left(1-e^{-\frac{c}{n T} t_{i}}\right) \equiv 0
$$

Thus, $a$ and $c$ can be obtained by solving the following two equations simultaneously:$$
c=\frac{1}{k n T} \sum_{i=1}^{k} t_{i}+\frac{a}{k n T} \sum_{i=1}^{k} t_{i} e^{-\frac{c}{n t_{i}}}
$$

and

$$
a=\frac{k}{\sum_{i=1}^{k}\left(1-e^{-\frac{c}{n t_{i}} t_{i}}\right)}
$$

# Hyperexponential Growth Model 

The hyperexponential growth model (Ohba 1984a) is based on the assumption that a program has a number of clusters of modules, each having a different initial number of errors and a different failure rate. Examples are new modules vs reused modules, simple modules vs complex modules, and modules which interact with hardware vs modules which do not. It should be noted that the sum of exponential distributions becomes a hyperexponential distribution.

Theorem 6.3 (Ohba 1984a): Assume that a program has a number of clusters of modules and each having a different initial number of errors and a different failure intensity function. The mean value function of the hyperexponential class NHPP model is

$$
m(t)=\sum_{i=1}^{n} a_{i}\left[1-e^{-b_{i} t}\right]
$$

where
$n=$ number of clusters of modules
$a_{i} \quad=$ number of initial faults in cluster $i$
$b_{i}=$ failure rate of each fault in cluster $i$
The failure intensity function is given by

$$
\lambda(t)=\sum_{i=1}^{n} a_{i} b_{i} e^{-b_{i} t}
$$

## Yamada-Osaki Exponential Growth Model

A similar extension of the exponential growth model has been suggested by Yamada and Osaki (1985) by dividing the software into $k$ modules.

Theorem 6.4 (Yamada 1985): The failure intensity of faults within different modules are assumed to be different while the failure intensity of faults within the same module are assumed to be the same. Assume that the expected number of faults detected for each module are exponential. The expected number of faults detected for the entire software can be obtained as

$$
m(t)=a \sum_{i=1}^{k} p_{i}\left[1-e^{-b_{i} t}\right]
$$where
$k=$ number of modules in the software
$b_{i}=$ error detection rate of one fault within the $\mathrm{i}^{\text {th }}$ module
$p_{i}=$ probability of faults for the $\mathrm{i}^{\text {th }}$ module
$a=$ expected number of software errors to be eventually detected or total number of faults existing in the software before testing.
This model is called the Yamada-Osaki exponential growth model.
For Type-I data, the MLEs of the parameters $a$ and $b_{i}$ for $1=1,2, \ldots k$ can be obtained by solving the following equations simultaneously:

$$
\begin{gathered}
a=\frac{y_{n}}{\sum_{i=1}^{k} p_{i}\left(1-e^{-b t_{n}}\right)} \\
\frac{y_{n} t_{n} e^{-b_{i} t_{n}}}{\sum_{i=1}^{k} p_{i}\left(1-e^{-b t_{n}}\right)}=\sum_{i=1}^{n} \frac{\left(y_{i}-y_{i-1}\right)\left(t_{i} e^{-b t_{i}}-t_{i-1} e^{-b t_{i-1}}\right)}{\sum_{i=1}^{k} p_{i}\left(e^{-b t_{i-1}}-e^{-b t_{i}}\right)}
\end{gathered}
$$

Similarly, for Type-II data, the MLEs of the parameters $a$ and $b_{i}$ for $i=1,2$, $\ldots, k$ can be obtained by solving simultaneously the following two equations:

$$
\begin{gathered}
a=\frac{n}{\sum_{i=1}^{k} p_{i}\left(1-e^{-b_{i} s_{n}}\right)} \\
\frac{n s_{n} e^{-b_{i} s_{n}}}{\sum_{i=1}^{k} p_{i}\left(1-e^{-b_{i} s_{n}}\right)}=\sum_{j=1}^{n} \frac{\left(e^{-b_{i} s_{j}}-b_{i} s_{j} e^{-b_{i} s_{j}}\right)}{\sum_{i=1}^{k} p_{i} b_{i} e^{-b_{i} s_{j}}}
\end{gathered}
$$

# 6.5 NHPP S-shaped Model 

In the NHPP S-shaped model, the software reliability growth curve is an S-shaped curve which means that the curve crosses the exponential curve from below and the crossing occurs once and only once. The detection rate of faults, where the error detection rate changes with time, become the greatest at a certain time after testing begins, after which it decreases exponentially. In other words, some faults are covered by other faults at the beginning of the testing phase, and before these faults are actually removed, the covered faults remain undetected. Yamada (1984) also determined that the software testing process usually involves a learning process where testers become familiar with the software products, environments, and software specifications. Several S-shaped models (Yamada 1984; Pham 1997a) such as delayed S-shaped, inflection S-shaped, etc., will also be discussed in this section.The NHPP S-shaped model is based on the following assumptions:

1. The error detection rate differs among faults.
2. Each time a software failure occurs, the software error which caused it is immediately removed, and no new errors are introduced.

Theorem 6.5 (Ohba 1984b): The mean value function solution of the following differential equation:

$$
\frac{\partial m(t)}{\partial t}=b(t)[a-m(t)]
$$

is given by

$$
m(t)=a\left[1-e^{-\int_{0}^{t} b(u) d u}\right]
$$

where
$a=$ expected total number of faults that exist in the before testing
$b(t)=$ failure detection rate per fault
$m(t)=$ expected number of failures detected at time $t$

# Inflection S-shaped Model 

The inflection S-shaped model (Ohba 1984) is based on the dependency of faults by postulating the following assumptions:

1. Some of the faults are not detectable before some other faults are removed.
2. The probability of failure detection at any time is proportional to the current number of detectable faults in the software.
3. Failure rate of each detectable fault is constant and identical.
4. The isolated faults can be entirely removed.

Theorem 6.6 (Ohba 1984b): Assume

$$
b(t)=\frac{b}{1+\beta e^{-b t}}
$$

where the parameters $b$ and $\beta$ represent the failure-detection rate and the inflection factor, respectively. The mean value function is given by

$$
m(t)=\frac{a}{1+\beta e^{-b t}}\left(1-e^{-b t}\right)
$$

This model is called the inflection S-shaped model (Ohba 1984b).
The function $m(\mathrm{t})$ can be easily obtained by substituting $b(t)$ from equation. (6.31) into equation (6.30). The failure intensity function of the inflection S-shaped model is given by

$$
\lambda(t)=\frac{a b(1+\beta) e^{-b t}}{\left(1+\beta e^{-b t}\right)^{2}}
$$The expected number of remaining errors at time $t$ is given by

$$
m(\infty)-m(t)=\frac{a(1+\beta) e^{-b t}}{\left(1+\beta e^{-b t}\right)}
$$

For Type-I data, the estimate of parameters $a$ and $b$ for specified $\beta$ using the MLE method can be obtained by solving the following equations simultaneously:

$$
a=\frac{y_{n}\left(1+\beta e^{-b t_{n}}\right)}{\left(1-e^{-b t_{n}}\right)}
$$

and

$$
\begin{gathered}
\sum_{i=1}^{n}\left(y_{i}-y_{i-1}\right)\left(\frac{\left(t_{i} e^{-b t_{i}}-t_{i-1} e^{-b t_{i-1}}\right)}{\left(e^{-b t_{i-1}}-e^{-b t_{i}}\right)}+\frac{\beta t_{i} e^{-b t_{i}}}{\left(1+\beta e^{-b t_{i}}\right)}+\frac{\beta t_{i-1} e^{-b t_{i-1}}}{\left(1+\beta e^{-b t_{i-1}}\right)}\right) \\
=\frac{y_{n} t_{n} e^{-b t_{n}}\left(1-\beta+2 \beta e^{-b t_{n}}\right)}{\left(1-e^{-b t_{n}}\right)\left(1+\beta e^{-b t_{n}}\right)}
\end{gathered}
$$

Similarly, for Type-II data, the estimate of parameters $a$ and $b$ for specified $\beta$ using the MLE method can be obtained by solving the following two equations:

$$
a=\frac{n\left(1+\beta e^{-b s_{n}}\right)}{\left(1-e^{-b s_{n}}\right)}
$$

and

$$
\frac{n s_{a} e^{-b s_{n}}(1+\beta)}{\left(1-e^{-b s_{n}}\right)\left(1+\beta e^{-b s_{n}}\right)}=\frac{n}{\beta}-\sum_{i=1}^{n} s_{i}+2 \sum_{i=1}^{n} \frac{\beta s_{i} e^{-b s_{i}}}{\left(1+\beta e^{-b s_{i}}\right)}
$$

# NHPP Delayed S-shaped Model 

We now discuss a stochastic model for a software error detection process based on NHPP in which the growth curve of the number of detected software errors for the observed failure data is S-shaped, called delayed S-shaped NHPP model (Yamada 1984). The software error detection process described by an S-shaped curve can be characterized as a learning process in which test-team members become familiar with the test environment, testing tools, or project requirements, i.e., their test skills gradually improve. The delayed S-shaped model is based on the following assumptions:

1. All faults in a program are mutually independent from the failure detection point of view.
2. The probability of failure detection at any time is proportional to the current number of faults in a software.
3. The proportionality of failure detection is constant.
4. The initial error content of the software is a random variable.
5. A software system is subject to failures at random times caused by errors present in the system.6. The time between $(i-1)^{\text {th }}$ and $i^{\text {th }}$ failures depends on the time to the $(i-1)^{\text {th }}$ failure.
7. Each time a failure occurs, the error which caused it is immediately removed and no other errors are introduced.

Theorem 6.7 (Yamada 1984): Assume

$$
b(t)=\frac{b^{2} t}{b t+1}
$$

where b is the error detection rate per error in the steady-state. The mean value function is given by

$$
m(t)=a\left[1-(1+b t) e^{-b t}\right]
$$

which shows an S-shaped curve.
This model is called the delayed S-shaped NHPP model for such an error detection process, in which the observed growth curve of the cumulative number of detected errors is S-shaped (Yamada 1984). The corresponding failure intensity function is

$$
\lambda(t)=a b^{2} t e^{-b t}
$$

The reliability of the software system is

$$
\begin{aligned}
R(s \mid t) & =e^{-[m(t+s)-m(t)]} \\
& =e^{-a\left[(1+b t) e^{-b t}-(1+b(t+s)) e^{-b(t+s)}\right]}
\end{aligned}
$$

The expected number of errors remaining in the system at time $t, n(t)$, is given by

$$
\begin{aligned}
n(t) & =m(\infty)-m(t) \\
& =a(1+b t) e^{-b t}
\end{aligned}
$$

For Type-I data, the estimate of parameters $a$ and $b$ using the MLE method can be obtained by solving the following equations simultaneously:

$$
a=\frac{y_{n}}{\left[1-\left(1+b t_{n} e^{-b t_{n}}\right)\right]}
$$

and

$$
\frac{y_{n} t_{n}^{2} e^{-b t_{n}}}{\left[1-\left(1+b t_{n} e^{-b t_{n}}\right)\right]}=\sum_{i=1}^{n} \frac{\left(y_{i}-y_{i-1}\right)\left(t_{i}^{2} e^{-b t_{i}}-t_{i-1}^{2} e^{-b t_{i-1}}\right)}{\left[\left(1+b t_{i-1}\right) e^{-b t_{i-1}}-\left(1+b t_{i}\right) e^{-b t_{i}}\right]}
$$

Similarly, for Type-II data, the estimate of parameters $a$ and $b$ using the MLE method can be obtained by solving the following equations:

$$
a=\frac{n}{\left[1-\left(1+b s_{n} e^{-b s_{n}}\right)\right]}
$$and

$$
\frac{2 n}{b}=\sum_{i=1}^{n} s_{i}+\frac{n b s_{i i}^{2} e^{-b s_{i i}}}{\left[1-\left(1+b s_{i i} e^{-b s_{i i}}\right)\right]}
$$

Example 6.2: The small on-line data entry software package test, data set \#1 available since 1980 in Japan (Ohba 1984a), is shown in Table 4.5. The size of the software has approximately 40000 LOC. The testing time was measured on the basis of the number of shifts spent running test cases and analyzing the results. The pairs of the observation time and the cumulative number of faults detected are presented in Table 4.5.

One can easily obtain the unknown parameters $a$ and $b$ for the delayed S-shaped NHPP model using the MLE as follows

$$
\mathrm{a}=71.725 \quad \mathrm{~b}=0.104
$$

The estimated mean value function $m(t)$ is

$$
m(t)=(71.725)\left[1-(1+0.104 t) e^{-0.104 t}\right]
$$

It seems that the delayed S-shaped NHPP model fits the observed failure data well in this data set.

# Connective NHPP Model 

Nakagawa (1994) proposed a model, called the connective NHPP model, where the basic shape of the growth curve is exponential and that an S-curve forms due to the test. In the connective NHPP model, a group of modules called "main route modules" are tested first, followed by the rest of the modules. Even if the failure intensity of the faults in the main route module and the other modules are similar, the growth curve becomes an S-curve since the search for their detection starts at different points in time.

Theorem 6.8 (Nakagawa 1994): The expected number of faults detected for the software as a whole can be expressed as follows:

$$
m(t)=a_{1}\left(1-e^{-b l_{(0, t(t)}(t)}\right)+a_{2}\left(1-e^{-b l_{(t 0, t(t)}(t)}\right)
$$

where $a_{2}>a_{1}>0$, and
$a_{1}=$ number of faults that are expected to be detected in the main route modules
$a_{2}=$ number of faults that are expected to be detected in modules other than the main route modules
$b=$ failure intensity
$t_{0}=$ starting time for testing modules other than the main route modules
$\mathrm{I}_{\mathrm{L} 1}=$ indicator function.

### 6.6 NHPP Imperfect Debugging Models

Many existing models describe perfect debugging in section 6.5 , that is, $a(t)=a$ and where the error detection rate $b(t)$ function is time-dependent. In this section,we discuss several software reliability models with imperfect debugging processes and a constant error detection rate $b(t)=b$, studied by Yamada (Yamada 1984). The NHPP imperfect debugging model is based on the following assumptions:

1. When detected errors are removed, it is possible to introduce new errors.
2. The probability of finding an error in a program is proportional to the number of remaining errors in the program.

Theorem 6.9 (Yamada 1984): The mean value function solution of the following differential equation:

$$
\frac{\partial m(t)}{\partial t}=b[a(t)-m(t)]
$$

with the initial condition $m(0)=0$, and $a(t)$ is defined as the error content function of time $t$ during software testing, is given by

$$
m(t)=b e^{-b t} \int_{0}^{t} a(s) e^{b s} d s
$$

Theorem 6.10 (Yamada 1984): Assume the error content function is

$$
a(t)=a e^{\alpha t}
$$

then the mean value function in equation (6.47) is given by

$$
m(t)=\frac{a b}{b+\alpha}\left(e^{\alpha t}-e^{-b t}\right)
$$

This model has been studied by Yamada (1984) and is called the Yamada imperfect debugging model 1. It is straightforward to obtain the function $m(t)$ in equation (6.49) by substituting a(t) in equation (6.48) into equation (6.47).

We next show how to estimate the parameters of $a, b$, and $\alpha$. Using the MLE method, the log of the likelihood function is

$$
\begin{aligned}
L L F & =\sum_{i=1}^{n}\left[\left(y_{i}-y_{i-1}\right) \ln \left[m\left(t_{i}\right)-m\left(t_{i-1}\right)\right]-\left[m\left(t_{i}\right)-m\left(t_{i-1}\right)\right]\right. \\
& \left.-\ln \left[\left(y_{i}-y_{i-1}\right)!\right]\right]
\end{aligned}
$$

where

$$
m\left(t_{i}\right)-m\left(t_{i-1}\right)=\frac{a b}{b+\alpha}\left[\left(e^{\alpha t_{i}}-e^{-\alpha t_{i-1}}\right)-\left(e^{b t_{i}}-e^{-b t_{i-1}}\right)\right]
$$

Taking the partial derivatives of the above function with respect to the unknown parameters $a, b$, and, $\alpha$, set

$$
\begin{aligned}
& \frac{\partial}{\partial a} \ln L=0 \\
& \frac{\partial}{\partial b} \ln L=0 \\
& \frac{\partial}{\partial \alpha} \ln L=0
\end{aligned}
$$then we obtain the results by solving the following equations simultaneously:

$$
\begin{gathered}
a=\frac{b+\alpha}{b} \frac{y_{n}}{\left(e^{\alpha t_{n}}-e^{-b t_{n}}\right)} \\
\sum_{i=1}^{n}\left[\left(y_{i}-y_{i-1}\right) \frac{a}{B}\left(\frac{\alpha A}{(b+\alpha)^{2}}+\frac{b C}{b+\alpha}\right)-a\left(\frac{\alpha A}{(b+\alpha)^{2}}+\frac{b C}{b+\alpha}\right)\right]=0
\end{gathered}
$$

and

$$
\sum_{i=1}^{n}\left[\left(y_{i}-y_{i-1}\right) \frac{a}{B}\left(\frac{-b A}{(b+\alpha)^{2}}+\frac{b C}{b+\alpha}\right)-a\left(\frac{-b A}{(b+\alpha)^{2}}+\frac{b C}{b+\alpha}\right)\right]=0
$$

where

$$
\begin{aligned}
& A=\left(e^{\alpha t_{1}}-e^{-\alpha t_{i-1}}\right)-\left(e^{b t_{1}}-e^{-b t_{i-1}}\right) \\
& B=\frac{a b A}{b+\alpha}
\end{aligned}
$$

and

$$
C=t_{1} e^{\alpha t_{1}}-t_{i-1} e^{-\alpha t_{i-1}}
$$

Theorem 6.11 (Yamada 1984): Assume the error content function is

$$
a(t)=a(1+\alpha t)
$$

then the mean value function in equation (6.47) is given by

$$
m(t)=a\left(1-e^{-b t}\right)\left(1-\frac{\alpha}{\beta}\right)+a \alpha t
$$

This model has been studied by Yamada (1984) and is called the Yamada imperfect debugging model 2. It is straightforward to obtain the function $m(t)$ in equation (6.51) by substituting $a(t)$ in equation (6.50) into equation (6.47).

# 6.7 NHPP Imperfect Debugging S-shaped Models 

A general software reliability model based on NHPP is used to derive a model that integrates imperfect debugging with the "learning" phenomenon. "Learning" is said to occur if testing appears to improve dynamically in efficiency as one progresses through a testing phase. "Learning" usually manifests as a changing fault detection rate.

Published models, and empirical data, suggest that efficiency growth due to "learning" may follow any number of growth curves from linear to that described by the logistic function. On the other hand, some recent work indicates that, in a real industrial resource-constrained environment, very little actual "learning" may take place since non-operational profiles used to generate test and business models may prevent that. When that happens, the testing efficiency may still change when an explicit change in testing strategy takes place, or it may change as a result of thestructural profile of the code under test and test-case ordering. Either way, software reliability engineering researchers agree that changes in the fault-detection rate are common during the testing process (Pham 1999b). Furthermore, in most realistic situations, fault repair has associated with it a fault re-introduction rate due to imperfect debugging phenomenon.

# Notation 

$a(t) \quad$ Time dependent fault content function, i.e., total number of faults in the software including the initial and introduced faults
$b(t) \quad$ Time dependent fault detection rate function, faults per unit of time
$\lambda(t) \quad$ Failure intensity function, faults per unit of time
$m(t) \quad$ The mean value function, i.e., the expected number of faults detected by time $t$
$R(x / t)$ Software reliability function, i.e., the conditional probability of no failure occurring during $(t, t+x)$ given that the last failure occurred at time $t$
$\wedge \quad$ Estimates using maximum likelihood estimation method
SSE Sum of the squared errors of a model when fitting the actual data
$y_{k} \quad$ The number of actual failures observed at time $t_{k}$
$\hat{m}\left(t_{k}\right)$ Estimated cumulative number of failures at time $t_{k}$ obtained from the fitted mean value functions, $k=1,2, \ldots, n$

### 6.7.1 A Generalized Imperfect-debugging Fault-detection Model

The derivation of software reliability models is usually divided into three processes. The counting process $\{N(t), t \geq 0\}$ that represents the cumulative number of software errors detected by time $t$ is a stochastic process. Thus, in the first step, this counting process must be described by statistical means. Basic assumptions about this process lead to the commonly accepted conclusion that, for any fixed $t \geq 0, N(t)$ is Poisson-distributed with a time-dependent Poissonparameter $m(t)$, the so-called mean value function (MVF).

The MVF represents the expected number of software errors that have accumulated up to time $t$. In a second step, this MVF must be defined analytically This is usually done by expressing the MVF as a function of two other functions: the error content function $a(t)$ and the error detection rate $b(t)$. By making assumptions about the analytical behavior of these two functions, $a(t)$ and $b(t)$ are then defined as functions of time with one or more free parameters.

Some of these parameters might be determined through mathematical or physical inferences. In most cases, however, these parameters need to be inferred statistically. Therefore, in a third step, actual test data are analyzed, using the statistical model defined in the first step with the class of MVFs defined in the second step.

The derivation of the generalized mean value function is discussed next. Most of the existing models (Yamada 1992; Goel 1980; Pham 2000a; Ohba 1984a) for an MVF build upon the assumption that the error detection rate is proportional tothe residual error content. Pham and Nordmann (1997b) formulate a generalized NHPP software reliability model and provide an analytical expression for the MVF.

The generalized NHPP imperfect-debugging fault-detection rate model (Pham 1997b) is formulated based on the following assumptions:

1. The error detection rate differs among faults.
2. Each time a software failure occurs, the software error which caused it is immediately removed, and new faults can be introduced.

Theorem 6.12 (Pham 1997b): The generalized mean value function solution of the following differential equations:

$$
\frac{\partial m(t)}{\partial t}=b(t)[a(t)-m(t)]
$$

with the initial condition $m\left(t_{0}\right)=m_{0}$, is given by (Pham 1997b):

$$
m(t)=e^{-B(t)}\left[m_{0}+\int_{t_{0}}^{t} a(\tau) b(\tau) e^{B(\tau)} d \tau\right]
$$

where

$$
B(t)=\int_{t_{0}}^{t} b(\tau) d \tau
$$

and $t_{0}$ is the time to begin the debugging process and $m\left(t_{0}\right)=m_{0}$.
Proof (Pham 2000a): Let us rewrite equation (6.52) as follows:

$$
\frac{\partial}{\partial t} m(t)+b(t) m(t)=S(t)
$$

where $S(t)=a(t) b(t)$. Note that

$$
\frac{\partial}{\partial t}\left[m(t) e^{-\int_{t_{0}}^{t} b(\tau) d \tau}\right]=\left[\frac{\partial}{\partial t} m(t)+b(t) m(t)\right] e^{-\int_{t_{0}}^{t} b(\tau) d \tau}
$$

Multiplying both sides of equation (6.55) by the integrating factor

$$
e^{-\int_{t_{0}}^{t} b(\tau) d \tau}
$$

we have

$$
\frac{\partial}{\partial t}\left[m(t) e^{-\int_{t_{0}}^{t} b(\tau) d \tau}\right]=S(t) e^{-\int_{t_{0}}^{t} b(\tau) d \tau}
$$Integrating between $\mathrm{t}_{0}$ and $t$, we obtain

$$
m(t)=m\left(t_{0}\right) e^{-\int_{t_{0}}^{t} b(\tau) d \tau}+\int_{t_{0}}^{t} S(\tau) e^{-\int_{t_{0}}^{t} b(\tau) d \tau} d \tau
$$

Note that

$$
e^{-\int_{0}^{t} b(y) d y}=e^{-\left[\int_{t_{0}}^{t} b(y) d y-\int_{t_{0}}^{t} b(y) d y\right]}
$$

Therefore,

$$
m(t)=m\left(t_{0}\right) e^{-\int_{t_{0}}^{t} b(\tau) d \tau}+\int_{t_{0}}^{t} S(\tau) e^{-\left[\int_{t_{0}}^{t} b(y) d y-\int_{t_{0}}^{t} b(y) d y\right]} d \tau
$$

Substituting

$$
\begin{aligned}
& B(t)=\int_{t_{0}}^{t} b(\tau) d \tau \\
& S(t)=a(t) b(t) \text { and } m\left(t_{0}\right)=m_{0}
\end{aligned}
$$

into equation (6.56) and after simplifications, we obtain

$$
m(t)=e^{-B(t)}\left[m_{0}+\int_{t_{0}}^{t} a(\tau) b(\tau) e^{B(t)} d \tau\right]
$$

This yields the same result as in equation (6.53).
Q.E.D.

In the simplest model, the function $a(t)$ and $b(t)$ are both constants. A constant $a(t)$ stands for the assumption that no new errors are introduced during the debugging process (perfect debugging). A constant $b(t)$ implies that the proportional factor relating the error detection rate $\lambda(t)$ to the total number of remaining errors is constant. This model is known as the Goel-Okumoto NHPP model. Many existing models describe perfect debugging, i.e., $a(t)=a$, with a time-dependent error detection rate $b(t)$ (see Section 6.5). Other studies deal with an imperfect debugging process and a constant error detection rate $b(t)=b$ (Section 6.5)

In a general model, the functions $a(t)$ and $b(t)$ are both functions of time and, for practical purposes, both are increasing with time. An increasing $a(t)$ shows that the total number of errors (including those already detected) increases with time because new errors are introduced during the debugging process. An increasing proportional factor $b(t)$ indicates that the error detection rate usually increases as debuggers establish greater familiarity with the software.

Although the relationship above does not yield immediate conclusions about $m(t)$, it relates $m(t)$ to two other functions that, by their definition, possess actual physical meanings. The function $a(t)$ represents the total error content at time $t$, and $b(t)$ represents the error detection rate. In this way, by introducing functionalassumptions about $a(t)$ and $b(t)$, which are more tangible, an analytical expression for $m(t)$ can be derived.

Many existing NHPP models can be considered as a special case of the generalized model as in equation (6.53). An increasing $a(t)$ function implies an increasing total number of faults (note that this includes those already detected and removed and those inserted during the debugging process) and reflects imperfect debugging.

An increasing $b(t)$ implies an increasing fault detection rate, which could be either attributed to a learning curve phenomenon (Ohba 1984a; Yamada 1992), or to software process fluctuations (Zhang 1998), or a combination of both .

# Pham-Nordmann-Zhang Model (PNZ model) 

This model assumes that:

1. The introduction rate is a linear function time-dependent overall fault content function.
2. The fault detection rate function is non-decreasing time-dependent with an inflection S-shaped model.

Theorem 6.13 (Pham 1999b): Assume that the time-dependent fault content function and error detection rate are, respectively,

$$
\begin{aligned}
& a(t)=a(1+\alpha t) \\
& b(t)=\frac{b}{1+\beta e^{-b t}}
\end{aligned}
$$

where $a=\mathrm{a}(0)$ is the parameter for the total number of initial faults that exist in the software before testing, and $\frac{b}{1+\beta}$ is the initial per fault visibility or failure intensity. The mean value function of the equation (6.52) is given by

$$
m(t)=\frac{a}{1+\beta e^{-b t}}\left(\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{\beta}\right]+\alpha t\right)
$$

This model is known as the PNZ model (Pham 1999b). The result can be obtained by substituting both the functions $a(t)$ and $b(t)$ into equation (6.53) where the initial condition $\mathrm{m}(0)=0$. In other words, the PNZ model incorporates the imperfect debugging phenomenon by assuming that faults can be introduced during the debugging phase at a constant rate of $\alpha$ fault per detected fault.

Therefore, the fault content rate function, $a(t)$, is a linear function of the testing time. The model also assumes that the fault detection rate function, $b(t)$, is a nondecreasing S-shaped curve (Ohba 1984a), which may capture the "learning" process of the software testers.# Pham Exponential Imperfect Debugging Model 

This model assumes that:

1. The introduction rate is an exponential function of testing time.
2. The error detection rate function is non-decreasing with an inflection S-shaped model.

Theorem 6.14 (Pham 2000a): Assume the time-dependent fault content function and error detection rate are, respectively,

$$
\begin{aligned}
& a(t)=\alpha e^{\beta t} \\
& b(t)=\frac{b}{1+c e^{-b t}}
\end{aligned}
$$

then the mean value function is given by

$$
m(t)=\frac{\alpha b}{b+\beta}\left(\frac{e^{(\beta+b) t}-1}{e^{b t}+c}\right)
$$

This model is called as the Pham Exponential Imperfect Debugging model. The result can be obtained by substituting both the functions $a(t)$ and $b(t)$ into Eq. (6.53) where $\mathrm{m}(0)=0$.

We are interested in estimating the parameters $\alpha, \beta, b$, and $c$ of function $m(t)$ in equation (6.60). If data are given on the cumulative number of errors at discrete times $\left(y_{i}:=y(t i)\right.$ for $\left.i=1,2, \ldots, n\right)$, then we need to obtain the first partial derivative of $m(t)$ with respect to $\alpha, \beta, b$, and $c$, respectively.

$$
\begin{gathered}
\frac{\partial}{\partial \alpha} m(t)=\frac{1}{\alpha} m(t) \\
\frac{\partial}{\partial \beta} m(t)=\left[\frac{-1}{(b+\beta)}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}\right] m(t) \\
\frac{\partial}{\partial b} m(t)=\left[\frac{\beta}{(b+\beta) b}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}+\frac{-t e^{b t}}{e^{b t}+c}\right] m(t) \\
\frac{\partial}{\partial c} m(t)=\frac{1}{e^{b t}+c} m(t)
\end{gathered}
$$

The second derivative of $m(t)$ with respect to $\alpha, \beta, b$, and $c$ is

$$
\begin{gathered}
\frac{\partial^{2}}{\partial \alpha^{2}}[m(t)]=0 \\
\frac{\partial^{2}}{\partial \alpha \partial \beta} m(t)=\frac{1}{\alpha} \frac{\partial}{\partial \beta} m(t) \\
\frac{\partial^{2}}{\partial \alpha \partial b} m(t)=\frac{1}{\alpha} \frac{\partial}{\partial b} m(t)
\end{gathered}
$$$$
\begin{aligned}
& \frac{\partial^{2}}{\partial \alpha \partial c} m(t)=\frac{1}{\alpha} \frac{\partial}{\partial c} m(t) \\
& \frac{\partial^{2}}{\partial \beta^{2}} m(t)=\left[\left(\frac{-1}{(b+\beta)}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}\right)^{2}\right. \\
& \left.+\left(\frac{-1}{(b+\beta)^{2}}-\frac{t^{2} e^{(b+\beta) t}}{\left(e^{(b+\beta) t}-1\right)^{2}}\right)^{2}\right] m(t) \\
& \frac{\partial^{2}}{\partial \beta \partial b} m(t)=\left[\left(\frac{-1}{(b+\beta)}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}\right)\right. \\
& \left(\frac{\beta}{(b+\beta) b}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}-\frac{t e^{b t}}{e^{b t}+c}\right) \\
& \left.+\left(\frac{1}{(b+\beta)^{2}}-\frac{t^{2} e^{(b+\beta) t}}{\left(e^{(b+\beta) t}-1\right)^{2}}\right)^{2}\right] m(t) \\
& \frac{\partial^{2}}{\partial \beta \partial c} m(t)=-\left(\frac{1}{\left(e^{b t}+c\right)}\right) \frac{\partial}{\partial \beta} m(t) \\
& \frac{\partial^{2}}{\partial b \partial b} m(t)=m(t)\left(\frac{\beta}{(b+\beta) b}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}-\frac{t e^{b t}}{e^{b t}+c}\right)^{2} \\
& +\left(\frac{\beta(2 b+\beta)}{(b+\beta)^{2} b^{2}}+\frac{t^{2} e^{(b+\beta) t}}{\left(e^{(b+\beta) t}-1\right)^{2}}-\frac{c t^{2} e^{b t}}{\left(e^{b t}+c\right)^{2}}\right) m(t) \\
& \frac{\partial^{2}}{\partial b \partial c} m(t)=-\left(\frac{1}{e^{b t}+c}\right) \frac{\partial}{\partial b} m(t)+\frac{t e^{b t}}{\left(e^{b t}+c\right)^{2}} m(t) \\
& \frac{\partial^{2}}{\partial c^{2}} m(t)=\frac{2}{\left(e^{b t}+c\right)^{2}} m(t) \\
& \frac{\partial^{2}}{\partial \beta \partial \alpha} m(t)=\frac{\partial^{2}}{\partial \alpha \partial \beta} m(t) \\
& \frac{\partial^{2}}{\partial b \partial \alpha} m(t)=\frac{\partial^{2}}{\partial \alpha \partial b} m(t)
\end{aligned}
$$

Note that

$$
\begin{gathered}
\lim _{t \rightarrow 0} \frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}=\frac{1}{b+\beta} \\
\lim _{t \rightarrow 0} \frac{t^{2} e^{(b+\beta) t}}{\left(e^{(b+\beta) t}-1\right)^{2}}=\frac{1}{(b+\beta)^{2}}
\end{gathered}
$$and $m(0)=0$. Consequently,

$$
\lim _{t \rightarrow 0} \frac{\partial^{2}}{\partial x \partial y} m(t)=\lim _{t \rightarrow 0} \frac{\partial}{\partial x} m(t)=m(0)=0
$$

Therefore, one can obtain the model parameters $\alpha, \beta, b$, and $c$ by solving the following system of equations simultaneously:

$$
\begin{array}{r}
m(t)=0 \\
{\left[\frac{-1}{(b+\beta) b}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}\right] m(t)=0} \\
{\left[\frac{\beta}{(b+\beta) b}+\frac{t e^{(b+\beta) t}}{e^{(b+\beta) t}-1}+\frac{-t e^{b t}}{e^{b t}+c}\right] m(t)=0}
\end{array}
$$

If the given data represent the occurrence times of the errors ( $S_{j}$ for $j=1,2, \ldots$ n), then we need to obtain the first partial derivative of $\lambda(t)$ with respect to $\alpha, \beta, b$, and $c$, where

$$
\begin{aligned}
\lambda(t) & =\frac{\partial}{\partial t} m(t) \\
& =\frac{\alpha b}{b+\beta}\left[\frac{(b+\beta) e^{(b+\beta) t}}{e^{b t}+c}-\frac{e^{(b+\beta) t}-1}{\left(e^{b t}+c\right)^{2}} b e^{b t}\right]
\end{aligned}
$$

Using equation (6.61), we can easily obtain the estimate of $\alpha, \beta, b$, and $c$.

# Pham-Zhang NHPP Model 

The model (Pham 1997a) assumes that:

1. The error introduction rate is an exponential function of the testing time. In other words, the number of errors increases quicker at the beginning of the testing process than at the end. This reflects the fact that more errors are introduced into the software at the beginning, while at the end, testers possess more knowledge and therefore introduce fewer errors into the program.
2. The error detection rate function is non-decreasing with an inflexion S-shaped model.

Theorem 6.15 (Pham 1997a): Assume the time-dependent fault content function and error detection rate are, respectively,

$$
\begin{aligned}
& a(t)=c+a\left(1-e^{-\alpha t}\right) \\
& b(t)=\frac{b}{1+\beta e^{-b t}}
\end{aligned}
$$then the mean value function is given by

$$
m(t)=\frac{1}{\left(1+\beta e^{-b t}\right)}\left((c+a)\left(1-e^{-b t}\right)-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right)
$$

This model is known as the Pham-Zhang model. The result can be obtained by substituting both the functions $a(t)$ and $b(t)$ into equation (6.53) where $m(0)=0$.

In general, NHPP software reliability models can be used to estimate the expected number of errors. Obviously, different models use different assumptions and therefore provide different mathematical forms for the mean value function $m(t)$.

Table 6.2 shows a summary of many existing NHPP software reliability models appearing in the software reliability engineering literature (Pham 2003a, b).

Table 6.2. Summary of NHPP software reliability models

| Model | MVF ( m(t) ) |
| :--: | :--: |
| Goel-Okumoto (G-O) | $\begin{aligned} & m(t)=a\left(1-e^{-b t}\right) \\ & a(t)=a \\ & b(t)=b \end{aligned}$ |
| DelayedS-shaped | $\begin{aligned} & m(t)=a\left(1-(1+b t) e^{-b t}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t} \end{aligned}$ |
| Inflection S- <br> shaped | $\begin{aligned} & m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}} \\ & a(t)=a \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ |
| HD/G-O model | $m(t)=\log \left\{\left[e^{a}-c\right] /\left[e^{a e^{-b t}}-c\right]\right\}$ |
| Yamada exponential | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-\beta t)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta e^{-\beta t} \end{aligned}$ |Table 6.2. (continued)

| Yamada <br> Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-p t^{2} / 2)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta t e^{-\beta t^{2} / 2} \end{aligned}$ |
| :--: | :--: |
| Yamada imperfect debugging model (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ |
| Yamada imperfect debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \quad b(t)=b \end{aligned}$ |
| Pham exponential imperfect model | $\begin{aligned} & m(t)=\frac{\alpha b}{b+\beta}\left(\frac{e^{(\beta+b) t}-1}{e^{b t}+c}\right) \\ & a(t)=\alpha e^{\beta t} \\ & b(t)=\frac{b}{1+c e^{-b t}} \end{aligned}$ |
| PNZ model | $\begin{aligned} & m(t)=\frac{a}{1+\beta \mathrm{e}^{b t}}\left\{\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t\right\} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ |
| Pham-Zhang model | $\begin{aligned} & m(t)=\frac{1}{1+\beta e^{-b t}}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ |

# 6.8 Applications 

This section applies the models discussed in this chapter using several failure data sets (discussed in Chapter 4) collected from real software development projects.The data sets derive from different time-periods and are illustrative of industrial software processes prevalent in that period. The procedure is as follows.

First, we fit each model to the data, estimate the model parameters, and obtain the mean value functions. Second, all models are compared with each other within a data set using the SSE, MSE, and AIC metrics (see Section 6.3).

In these applications, we use most of the data points to fit the models and estimate the parameters. We also use several remaining points to illustrate the short-term predictive power of the model that incorporates both imperfect debugging and variable fault-detection rate.

Application 6.1 (The NTDS data): The software data set \#4 given in Table 4.8 (Chapter 4) was extracted from information about failures in the development of software for the real-time, multi-computer complex of the US Naval Fleet Computer Programming Center of the US Naval Tactical Data Systems (NTDS).

The software consists of 38 different project modules. The time horizon is divided into four phases: production phase, test phase, user phase, and subsequent test phase. The 26 software failures were found during the production phase, 5 during the test phase and; the last failure was found on 4 January 1971. One failure was observed during the user phase, in September 1971, and two failures during the test phase in 1971.

The fact that the last 3 of the first 26 errors in Table 4.8 (see Chapter 4) occur almost in a cluster, while there is a relatively long interval between errors before and after that cluster, leads to the conclusion that error number 26 is an unfortunate cut-off point if one wishes to fit a software reliability model. Instead, it seems more reasonable to use either the first 25 or the first 27 error data to fit models.

Let us choose the second alternative and fit some 5 selected models below to the first 27 error data. Although not presented here, we also fit the models to the first 25 error data, which results in only slight deviations with the same overall conclusions (see Problem 6.5). For the ease of discussion, let us name the following five selected models to be analyzed in this example.

Model 1 (Goel-Okumoto):

$$
m(t)=a\left(1-e^{-b t}\right)
$$

Model 2 (Inflection S-shaped):

$$
m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}
$$

Model 3 (Yamada imperfect debugging 1):

$$
m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right)
$$Model 4 (Yamada imperfect debugging 2):

$$
m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t
$$

Model 5 (Pham-Nordmann-Zhang):

$$
m(t)=\frac{a}{1+\beta e^{-b t}}\left[\left(1-e^{-b t}\right)\left(1-\frac{\alpha}{b}\right)+\alpha a t\right]
$$

and the corresponding reliability of model $i$ is $R_{i}$.
It is worthwhile to note that parameter estimates derived from a set of test data are representative and meaningful only for working conditions similar to those under which the test data were obtained. In the NTDS data in Table 4.8 (in Chapter 4), for example, the production and test phases can be considered similar, while the user phase is very different from the former two in two ways. First, during the user phase, no new errors due to testing and debugging are introduced.

Second, during the user phase, the software is not subject to such "hard" and extensive testing as it is during the production and testing phase. Both differences contribute towards the same effect - a reduced error occurrence rate. This can be verified by looking at the test data, which indicates a considerably longer time span between errors during the user phase. In general, changes in the working environment go along with shifts in model parameters, and consequently, parameter estimates relating to the production and first test phases are only applicable during the first two phases and meaningless beyond that point.

The MLEs of the parameters for several software reliability models based on the first 27 error data of the NTDS (data set \#4 in Chapter 4) are obtained as follows (Pham 2000a):

Model 1: $a=29.42827, b=0.007402$
Model 2: $a=27.44246, b=0.015517$
$\beta=2.042596$
Model 3: $a=29.42827, b=0.015517$
$\alpha=0$
Model 4: $a=29.42827, b=0.007402$
$\alpha=0$
Model 5: $a=19.32872, b=0.047526$
$\alpha=0.001256, \beta=24.33569$

It is worth noting that models 1,3 , and 4 yield exactly the same mean value functions after the MLE. Despite allowing for an imperfect debugging model, the perfect debugging model remains the one that provides the best fit to the NTDS data. The additional freedom introduced in models 3 and 4 through an additional parameter has no effect on the fitted mean value function, since the MLE of that additional parameter is found to be $\mathrm{a}=0$, transforming models 3 and 4 into Model 1. Model 2 allows for an inflection S-shaped mean value function. However, the fitted mean value function is only vaguely S -shaped if at all.

On the upper end of the time horizon, the mean value function underestimates the actual failure numbers. For example, at mission time $s=20$, model 5 estimates a reliability of $\mathrm{R}_{5}=0.615$, whereas models 1,3 , and 4 estimate a reliability of $\mathrm{R}_{1}=0.716$ and model 2 estimates a reliability of $\mathrm{R}_{2}=0.889$.The mean value function of Model 5 provides a good fit to the S-shape of the actual NTDS data. It overestimates the actual failure numbers at the upper end of the time horizon. However, it provides an excellent fit to the 27 test data points it is fitted to, and a good overall fit to all data points of the production and first test phases, reducing fitting and forecast errors of models 1-4. Further studies show that the parameter in model 5 appears especially sensitive to data at further progressed times, indicating an increasingly better fit with a widening time span of the test data (Pham 2000a).

Application 6.2 (The NTDS data, continued): In this section, we continue to use the NTDS data set to evaluate and compare the descriptive and the predictive power of several existing models. Detailed description of NTDS data can be found in Table 4.8.

There were 26 software failures during the production phase, 5 during the test phase (the last failure was found on 1971 January 4); 1 failure was observed during the user phase in 1971 September, and 2 failures were observed during the test phase in 1971. Since the first two phases, production and testing, can be considered similar, while the user phase is very different, we have decided to combine the first two. We now use the first 27 data points to fit several existing models, and the last four data points to evaluate the predictions (Pham 1999b). Table 6.3 summarizes the SSE and AIC values for some existing NHPP models.

Table 6.3. Comparison of goodness-of-fit and predictive power using NTDS data

| Model | SSE (fit) <br> $\sum_{k=1}^{27}\left[y_{k}-\hat{m}\left(t_{k}\right)\right]^{2}$ | SSE (prediction) <br> $\sum_{k=28}^{31}\left[y_{k}-\hat{m}\left(t_{k}\right)\right]^{2}$ | AIC |
| :-- | :--: | :--: | :--: |
| G-O model | 136.58 | 71.96 | 88.98 |
| Delayed S-shaped | 47.276 | 126.98 | 85.86 |
| Inflexion S-shaped | 57.496 | 129.88 | 88.44 |
| HD/G-O | 122.83 | 114.24 | 91.92 |
| Yamada exponential | 136.83 | 71.63 | 91.00 |
| Yamada Rayleigh | 39.78 | 134.59 | 89.66 |
| Yamada imperfect (1) | 111.50 | 922.34 | 90.36 |
| Yamada imperfect (2) | 109.59 | 2215.11 | 90.36 |
| PNZ model | 13.60 | 57.67 | 81.82 |

From Table 6.3, we can see that SSE (fit) value for the PNZ model is 13.60, which is significantly smaller than the value for other models. The SSE value for the prediction is 57.67 , which is again the smallest among all models. Comparing all models using the AIC criterion we find that the new model has the smallest AIC value. This may indicate that the complexity of the model that comes from theincreased number of parameters may be more than compensated by the ability of the model to describe better the debugging process.

Application 6.3 (The real-time control system data): The software for monitoring a real-time control system consists of about 200 modules having, on average, 1000 lines of a high-level language such as Fortran (Tohma 1991). Since the test data, data set \#8, (see Table 4.12, Chapter 4) are recorded daily, the test operations performed in a day are regarded to be a test instance.

In Table 4.12, data marked with an asterisk (*) are interpolated data. Let us look at the goodness of fit test to most NHPP software models based on the data set \#8 given in Table 4.12. The results of the estimated parameters of the models and their SSEs are given in Table 6.4. It is observed that the Pham-Zhang model, having an SSE equal to 59,549 , fits better than the other NHPP models for this failure data set. It is worthwhile to note that the inflection S-shaped model also performs well in this case.

Application 6.4 (The Tandem Computers data): The data used in this section derive from one of four major releases of software products at Tandem Computers are documented by Wood (1996).

In this application, two NHPP models will be analyzed: the Pham-NordmannZhang (PNZ) and the Goel-Okumoto (G-O) models (Pham 1999b). Table 6.5 presents the prediction results from week 10 to week 20 for the PNZ and G-O models based on the Release \#1 failure data set \#5, Table 4.9 in Chapter 4..

From Table 6.5, the SSE value as well as AIC of the PNZ model is smaller than that of G-O model. Table 6.6 also summarizes the results of several existing NHPP models for Release 1 software data (data set \#5, Table 4.9).

Commonly, a more sophisticated model, for example, the one that incorporates both imperfect debugging and a changing fault detection rate, is probably worth the effort because it models a more realistic set of actual effects, and also provides short-term predictive power which is at least as good or better than that of more 'traditional' models (as measured by SSE statistic).

Obviously, further work in broader validation of this conclusion is needed using other data sets and other quality metrics including AIC and PRR for descriptive and predictive software reliability modeling (Pham 1999b).Table 6.4. The MLEs and SSEs for some NHPP models for data set \#8

| Model name | MVF $(m(t))$ | MLEs | SSE |
| :--: | :--: | :--: | :--: |
| Goel-Okumoto (G-O) | $\begin{aligned} & m(t)=a\left(1-e^{-b t}\right) \\ & a(t)=a \\ & b(t)=b \end{aligned}$ | $\hat{a}=497.282$ <br> $\hat{b}=0.0308$ | 216872 |
| Delayed S- <br> shaped | $\begin{aligned} & m(t)=a\left(1-(1+b t) e^{-b t}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t} \end{aligned}$ | $\begin{aligned} & \hat{a}=483.039 \\ & \hat{b}=0.06866 \end{aligned}$ | 71247 |
| Infection S- <br> shaped | $\begin{aligned} & m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}} \\ & a(t)=a \\ & b(t)=\frac{b}{\left(1+\beta e^{-b t}\right)} \end{aligned}$ | $\begin{aligned} & \hat{a}=482.017 \\ & \hat{b}=0.07025 \\ & \hat{\beta}=4.15218 \end{aligned}$ | 60031 |
| Yamada exponential | $\begin{aligned} & m(t)=a\left(1-e^{\gamma \alpha\left(1-e^{(-\beta t)}\right)}\right) \\ & a(t)=a \\ & b(t)=\gamma \alpha \beta e^{(-\beta t)} \end{aligned}$ | $\begin{aligned} & \hat{a}=67958.8 \\ & \hat{\alpha}=0.00732 \\ & \hat{\beta}=0.03072 \end{aligned}$ | 220702 |
| Yamada <br> Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{\gamma \alpha\left(1-e^{(-\beta t^{2} / 2)}\right)}\right. \\ & a(t)=a \\ & b(t)=\gamma \alpha \beta e^{-\beta t^{2} / 2} \end{aligned}$ | $\begin{aligned} & \hat{a}=500.146 \\ & \hat{\alpha}=3.31944 \\ & \hat{\beta}=0.00066 \end{aligned}$ | 87251 |
| Yamada imperfect <br> debugging model (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ | $\begin{aligned} & \hat{a}=654.963 \\ & \hat{b}=0.02056 \\ & \hat{\alpha}=-0.0027 \end{aligned}$ | 155011 |
| Yamada imperfect <br> debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \\ & b(t)=b \end{aligned}$ | $\begin{aligned} & \hat{a}=591.804 \\ & \hat{b}=0.02423 \\ & \hat{\alpha}=-0.0019 \end{aligned}$ | 183157 |
| PNZ | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta e^{-b t}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=470.759 \\ & \hat{b}=0.07497 \\ & \hat{\alpha}=0.00024 \\ & \hat{\beta}=4.69321 \end{aligned}$ | 63189 |Table 6.4. (continued)

| Pham-Zhang | $m(t)=\frac{1}{1+\beta e^{-b t}}\left[(c+a)\left(1-e^{-b t}\right)\right.$ | $\hat{a}=0.46685$ | 59549 |
| :--: | :--: | :--: | :--: |
|  | $-\frac{a}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)$ | $\hat{b}=0.07025$ |  |
|  | $a(t)=c+a\left(1-e^{-\alpha t}\right)$ | $\hat{\alpha}=1.4 \times 10^{-5}$ |  |
|  | $b(t)=\frac{b}{1+\beta e^{-b t}}$ | $\hat{\beta}=4.15213$ |  |

Table 6.5. G-O and PNZ models using release \#1 software data set \#5

| Testing time <br> (weeks) | CPU hours | Defects <br> found | Predicted total <br> defects by G-O | Predicted total <br> defects by PNZ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 519 | 16 | - | - |
| 2 | 968 | 24 | - | - |
| 3 | 1,430 | 27 | - | - |
| 4 | 1,893 | 33 | - | - |
| 5 | 2,490 | 41 | - | - |
| 6 | 3,058 | 49 | - | - |
| 7 | 3,625 | 54 | - | - |
| 8 | 4,422 | 58 | - | - |
| 9 | 5,218 | 69 | - | - |
| 10 | 5,823 | 75 | 98 | 74.7 |
| 11 | 6,539 | 81 | 107 | 80.1 |
| 12 | 7,083 | 86 | 116 | 85.2 |
| 13 | 7,487 | 90 | 123 | 90.1 |
| 14 | 7,846 | 93 | 129 | 94.6 |
| 15 | 8,205 | 96 | 129 | 98.9 |
| 16 | 8,564 | 98 | 134 | 102.9 |
| 17 | 8,923 | 99 | 139 | 106.8 |
| 18 | 9,282 | 100 | 138 | 110.4 |
| 19 | 9,641 | 100 | 135 | 111.9 |
| 20 | 10,000 | 100 | 133 | 112.2 |
|  |  |  |  |  |
| SSE |  |  | 12233 | 495.98 |
| AIC |  |  | 149.60 | 138.56 |

Application 6.5 (NTDS data): Assume the time-dependent fault content function and fault detection rate function are, respectively,

$$
\begin{aligned}
& a(t)=c+a\left(1-e^{-\alpha t}\right) \\
& b(t)=\frac{b}{1+\beta e^{-b t}}
\end{aligned}
$$with the initial condition $m\left(t_{0}\right)=m_{0}$. From equation (6.53), the mean value function is given as follows:

$$
\begin{aligned}
m(t) & =\frac{e^{b t_{0}}+\beta}{e^{b t}+\beta} m_{0} \\
& +\frac{1}{1+\beta e^{-b t}}\left[(c+a)\left(1-e^{-b\left(t_{0}-t\right)}\right)-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-\left[\left(b-\alpha\right) t_{0}-b t\right]}\right)\right]
\end{aligned}
$$

This is called an Extended Pham-Zhang model and when $m_{0}=0$ and $t_{0}=0$ it yields the Pham-Zhang model

Assume we use the NTDS (data set \#4, Table 4.8) data and also assume that $t_{0}$ $=149$ and $m(149)=22$. Detailed description of NTDS data can be found in Table 4.8, Chapter 4. Then we obtain the following estimates:

$$
\begin{array}{ll}
a=0.22311 & \alpha=0.00677 \\
b=0.00442 & \beta=0.00607 \\
c=46.6092 &
\end{array}
$$

which were calculated by using the MLE. From this result, we can obtain a simple approach to determine when the next failure will occur. In other words, after substituting all the estimate parameters into the above mean value function $m(t)$, given $m(149)=22$, we can then determine the time to the next failure, $t_{23}$, by solving the following equation:

$$
\hat{m}(t)=23
$$

and therefore, we obtain

$$
t_{23}=158.356
$$

Table 6.6. Prediction comparison of release \#1 software failure data set \#5

|  | Total defects predicted several weeks (wks) after <br> the Start of system test |  |  |  |  |
| :-- | --: | --: | --: | --: | --: |
| Model | 10 wks | 12 wks | 14 wks | 17 wks | 20wks |
| Goel-Okumoto | 98 | 116 | 129 | 139 | 133 |
| (G-O) | 71 | 82 | 91 | 99 | 102 |
| Delayed S-shaped | 98 | 116 | 129 | 139 | 133 |
| Hossain Dahiya/G-O | 96 | 110 | 107 | 114 | 112 |
| Gompertz | 757 | 833 | 735 | 631 | 462 |
| Pareto (Pham 1999) | 98 | 116 | 129 | 139 | 133 |
| Weibull | 152 | 181 | 204 | 220 | 213 |
| Yamada exponential | 77 | 89 | 98 | 107 | 111 |
| Yamada Raleigh | 74.6 | 85.3 | 91.4 | 99.4 | 106.7 |
| Pham-Zhang (P-Z) | 74.7 | 85.2 | 94.6 | 106.8 | 112.2 |
|  |  |  |  |  |  |
| Actual data | 75 | 86 | 93 | 99 | 100 |

Application 6.6 (AT\&T Network-Management System): We evaluate models using the System $T$ data set (data set \#7, see Table 4.11) at AT\&T. This example uses the first 19 data points to fit the models, estimate the parameters in the models, andto predict the "future". Table 6.7 summarizes the results of several NHPP SRGMs. The PNZ and Yamada Imperfect (2) appear to be the best descriptive and predictive models. It is interesting to note that the delayed S -shaped model also fits the data well The SSE is slightly higher than that of the PNZ model, but it gives a poorer prediction with a SSE of 9.55 . Comparing all models using the AIC criterion, we observe that the PNZ model has the smallest AIC value.

Table 6.7. Comparison of goodness-of-fit and predictive power of SRGMs

| Model | SSE (fit) <br> $\sum_{k=1}^{19}\left[y_{k}-\hat{m}\left(t_{k}\right)\right]^{2}$ | SSE (prediction) <br> $\sum_{k=20}^{22}\left[y_{k}-\hat{m}\left(t_{k}\right)\right]^{2}$ | AIC |
| :-- | :--: | :--: | :--: |
| G-O model | 26.70 | 2.27 | 78.48 |
| Delayed S- <br> shaped | 21.95 | 9.55 | 86.70 |
| Inflexion S- <br> shaped | 26.70 | 2.27 | 80.05 |
| HD/G-O | 32.52 | 2.55 | 80.05 |
| Yamada <br> exponential | 26.75 | 2.27 | 80.08 |
| Yamada <br> Rayleigh | 30.06 | 11.21 | 91.90 |
| Yamada <br> imperfect (1) | 30.92 | 0.43 | 79.84 |
| Yamada <br> imperfect (2) | 30.34 | 0.37 | 79.86 |
| PNZ model | 21.93 | 0.36 | 75.86 |

# 6.9 Imperfect Debugging vs Perfect Debugging 

It is worthwhile to note that a study by Ohba and Chou (1989) shows that, for an arbitrary $b(t)$, a model with $a(t)=a$ and a model with $a(t)=a+\alpha m(t)$ are isomorphic. In other words, both models yield, after maximum likelihood estimation, the same mean value functions.

This explains why in many cases, imperfect debugging models do not significantly improve perfect debugging models (Pham 2000a). Consider the following two models.

Model P: The Perfect Debugging Model
Assume that

$$
\begin{aligned}
& a(t)=a \\
& b(t)=\text { arbitrary }
\end{aligned}
$$

then, from equation (6.30), we obtain$$
m(t)=a\left(1-e^{-B(t)}\right)
$$

where

$$
B(t)=\int_{0}^{t} b(s) d s
$$

Model IP: The Imperfect Debugging Model
Assume that

$$
\begin{aligned}
& a(t)=\alpha m(t)+a \\
& b(t)=\text { arbitrary }
\end{aligned}
$$

and from equation (6.53) we obtain

$$
m(t)=\frac{a}{1-\alpha}\left(1-e^{-B(t)(1-\alpha)}\right)
$$

Let the error detection rates $b_{i}(t)$ be functions of type

$$
b_{i}(t)=b_{i} f\left(\beta_{1}^{(1)}, \beta_{1}^{(1)}, \ldots ., \beta_{1}^{(n)}, t\right)
$$

where $b_{i}$ are positive constants and $f(., t)$ an arbitrary positive function. Furthermore, let

$$
v_{1}:=\left(a_{1}, b_{1}, \beta_{1}^{(1)}, \beta_{1}^{(1)}, \ldots ., \beta_{1}^{(n)}\right)
$$

be a vector of valid values for the free parameters in Model P. Then Model P is uniquely defined through the vector $v_{1}$. Analogously, Model IP is uniquely defined through another vector:

$$
v_{2}:=\left(a_{2}, b_{2}, \beta_{2}^{(1)}, \beta_{2}^{(1)}, \ldots, \beta_{2}^{(n)}\right)
$$

By letting $m_{l}\left(v_{1}, t\right)$ denote the mean value function for Model P , and $m_{2}\left(v_{2}, t\right)$ denote the mean value function for Model IP, we find

Lemma 6.1: Let $x$ be a number such that $0<\mathrm{x}<1$. Then the function

$$
\phi_{x}\left(a_{1}, b, \beta_{1}^{(1)}, \ldots ., \beta_{1}^{(n)}\right):=\left(a_{1}(1-x), \frac{b}{(1-x)}, x, \beta_{1}^{(1)}, \ldots ., \beta_{1}^{(n)}\right)
$$

defines a one-to-one mapping from Model P parameters to Model IP parameters with $\alpha_{2}=x$ such that

$$
m_{1}\left(v_{1}, t\right)=m_{2}\left(\phi_{x}\left(v_{1}\right), t\right)
$$

The proof of this lemma is straightforward.
This result shows that the mean value function of the imperfect debugging model equals that of (the) perfect debugging model with an error detection rate of the same type. This observation immediately implies the suspicion that, after substitution of the MLE for the parameters in each of the models, we will have the same mean value function, regardless of which model we begin with. The following results prove this relationship to be true under general conditions in equation (6.67).# Lemma 6.2 (Pham 2000a): 

(1) If

$$
v_{1}^{*}:=\left(a_{1}^{*}, b_{1}^{*}, \beta_{1}^{(1) *}, \beta_{1}^{(2) *,}, \ldots, \beta_{1}^{(n) *}\right)
$$

are MLEs for parameters in Model P, then for every $\alpha_{2} *\left(0<\alpha_{2}^{*}<1\right)$,

$$
\phi_{\alpha_{2} *}\left(v_{1}^{*}\right)
$$

are MLEs for parameters in Model IP.
(2) If

$$
v_{2}^{*}:=\left(a_{2}^{*}, b_{2}^{*}, \beta_{2}^{(1) *}, \beta_{2}^{(2) *,}, \ldots, \beta_{2}^{(n) *}\right)
$$

are MLEs for parameters in Model IP, then

$$
\phi_{\alpha_{2} *}^{-1}\left(v_{2}^{*}\right)
$$

are MLEs for parameters in Model P
Proof: Let $M L F_{1}\left(v_{1}\right)$ denote Model P's maximum likelihood function (MLF) as a function of the free parameters, $M L F_{2}\left(v_{2}\right)$ the MLF for Model IP. Let $v_{1}{ }^{*}$ and $v_{2}{ }^{*}$ denote the arbitrary MLE of parameters for Model P and Model IP, respectively. From Pham (2000a):

$$
\begin{aligned}
M L F_{1}\left(v_{1}^{*}\right) & =M L F_{2}\left(\phi_{\alpha_{2} *}\left(v_{1}^{*}\right)\right) \leq M L F_{2}\left(v_{2}^{*}\right)=M L F_{1}\left(\phi_{\alpha_{2} *}{ }^{-1}\left(v_{2}^{*}\right)\right) \\
& =M L F_{1}\left(v_{1}^{*}\right)
\end{aligned}
$$

The two " $\leq$ " relations hold due to Lemma 6.1. The two"="signs hold because $v_{1}{ }^{*}$ is an MLE for Model P and $v_{2}{ }^{*}$ is an MLE for Model IP. Since the left term in the above series equals the right, we conclude that all " $\leq$ " must be "=" signs, and consequently,

$$
M L F_{2}\left(\phi_{\alpha_{2} *}\left(v_{1}^{*}\right)\right)=M L F_{2}\left(v_{2}^{*}\right)
$$

and

$$
M L F_{1}\left(\phi_{\alpha_{2} *}{ }^{-1}\left(v_{2}^{*}\right)\right)=M L F_{1}\left(v_{1}^{*}\right)
$$

Theorem 6.16 (Pham 2000a): For every $x, 0<x<1$, the function $\theta_{x}\left(v_{1}\right)$ is a one-to-one mapping of the MLE of Model P parameters to Model IP parameters with $\alpha_{2}=x$.

Proof: From Lemma 6.2, the result follows.

### 6.10 Mean Time Between Failures for NHPP

Let $N(t)$ be an NHPP with the mean value function $\mathrm{m}(\mathrm{t})$ where $N(\mathrm{t})$ denotes the random variable of the total number of the events during $[0, t]$. Let $T_{k}$ denote the random variable of the occurring time for the $k$ th event, and let $X_{k}$ be the time interval between the $(k-1)$ th and $k$ th event. Then$$
X_{k}=T_{k}-T_{k-1}
$$

where $k=1,2, \ldots$ and $T_{0}=0$.
The probability density function of $T_{k}$ (Nakagawa 1983) is given by

$$
f_{T_{k}}(t)=\frac{\lambda(t) e^{-m(t)}[m(t)]^{k-1}}{(k-1)!}
$$

where

$$
\lambda(t)=\frac{\partial}{\partial t} m(t)
$$

is the intensity function for the NHPP. In software reliability, we commonly assume that the mean value function is bounded, which means $m(t)$ is always finite as $t$ approaches infinity. In this section, we assume that:

1. $m(t)$ is a strictly increasing function and uniformly continuous on any closed interval.
2. $m(0)=0, m(t)$ is a positive, finite, and differentiable function.

Let

$$
E^{*}\left[T_{k}\right]=E\left[T_{k} \mid T_{k}<\infty\right]
$$

be the conditional expectation. Then (Koshimae et al. 1994)

$$
E^{*}\left[T_{k}\right]=\frac{\int_{0}^{a} m^{-1}(z) z^{k-1} e^{-z} d z}{\int_{0}^{a} z^{k-1} e^{-z} d z}
$$

where $m(\infty)=a$.
If the expectation of $T_{k}$ is given, the mean time between failures (MTBFs) are given by

$$
E^{*}\left[T_{k}\right]=E\left[T_{k}\right]-E^{*}\left[T_{k-1}\right]
$$

where $E^{*}\left[X_{k}\right]$ is given in equation (6.75).
Example 6.3: Consider the mean value function

$$
m(t)=a\left[1-(1+b t) e^{-b t}\right]
$$

where parameters $a$ and $b$ denote the expected total number of initial errors and the detection rate per error, respectively. The intensity function is given by

$$
\lambda(t)=a b^{2} t e^{-b t}
$$

It is difficult to derive the inverse value function analytically in most mean value functions, for example, in equation (6.77). Let us denote

$$
u=m^{-1}(z)
$$then we can rewrite equation (6.75) as follows:

$$
E^{*}\left[T_{k}\right]=\frac{\int_{0}^{\infty} u \lambda(u)[m(u)]^{k-1} e^{-m(u)} d u}{\int_{0}^{a} z^{k-1} e^{-z} d z}
$$

It should be noted that one can solve the inverse function of $m(t)$ numerically using the Newton method or other mathematical software programs. Given the NTDS software failure data (data set \#4, see Table 4.8) and the total number of observed errors as $k=26$, we obtain the following estimates:

$$
a=27.50 \quad b=0.0186
$$

which was calculated by the MLE method. Table 6.8 shows numerical examples of the MTBFs using equations (6.76) and (6.78).

Table 6.8. Mean time between failures (MTBFs) for $m(t)$ as given in equation (6.77)

| Failure no. n | Time between failure <br> $\mathrm{x}_{\mathrm{k}}$ (days) | MTBF <br> $E^{*}\left[X_{\mathrm{k}}\right]$ |
| :-- | :--: | :--: |
| Production (checkout) phase |  |  |
| 1 | 9 | 14.4 |
| 2 | 12 | 8.2 |
| 3 | 11 | 6.7 |
| 4 | 4 | 6.1 |
| 5 | 7 | 5.8 |
| 6 | 2 | 5.6 |
| 7 | 5 | 5.5 |
| 8 | 8 | 5.5 |
| 9 | 5 | 5.6 |
| 10 | 7 | 5.7 |
| 11 | 1 | 5.9 |
| 12 | 6 | 6.2 |
| 13 | 1 | 6.5 |
| 14 | 9 | 6.8 |
| 15 | 4 | 7.2 |
| 16 | 1 | 7.6 |
| 17 | 3 | 8.0 |
| 18 | 3 | 8.4 |
| 19 | 6 | 8.7 |
| 20 | 1 | 9.0 |
| 21 | 11 | 9.1 |
| 22 | 33 | 9.1 |
| 23 | 7 | 8.9 |
| 24 | 91 | 8.7 |
| 25 | 2 | 8.5 |
| 26 | 1 | 8.1 |# 6.11 Further Reading 

The reader interested in a deeper understanding of NHPP software reliability modeling should note the following highly recommended articles:

Hoang Pham, "Recent Studies in Software Reliability Engineering", a chapter in the Handbook of Reliability Engineering, Editor: Hoang Pham, Springer, 2003, p. 285-302

Hoang Pham, "Software Reliability and Cost Models: Perspectives, Comparison and Practice", European Journal of Operational Research, vol. 149, 2003a, p. 475489

Hoang Pham, "Software Reliability", a chapter in Wiley Encyclopedia of Electrical and Electronic Engineering, Editor: John Webster, Wiley, 1999a, p.565-578

### 6.12 Problems

1. Assume the total error content function and error detection rate function are

$$
\begin{aligned}
& a(t)=\alpha_{2}(1+\gamma t) \\
& b(t)=\frac{b^{2} t}{b t+1}
\end{aligned}
$$

respectively. From equation (6.53), show that the mean value function is given as follows:

$$
\begin{aligned}
m(t) & =\alpha_{2}(1+\gamma t)-\frac{b t+1}{e^{b t}} \\
& -\frac{(1+b t) \alpha_{2} \gamma}{b e^{b t+1}}\left[\ln (b t+1)+\sum_{i=0}^{\infty} \frac{(b t+1)^{i+1}-1}{(i+1)!(i+1)}\right]
\end{aligned}
$$

2. Assume the total error content function and error detection rate function are

$$
\begin{aligned}
& a(t)=\alpha(1+\gamma t)^{2} \\
& b(t)=\frac{\gamma^{2} t}{\gamma t+1}
\end{aligned}
$$

respectively. Using equation (6.53), show that the mean value function is given as follows:

$$
m(t)=\alpha\left(\frac{1+\gamma t}{\gamma t}\right)\left(\gamma t e^{\gamma t}+1-e^{\gamma t}\right)
$$

3. Using a real-time command and control software system data given in Table 6.9 below:
(a) Calculate the maximum likelihood estimates for the parameters a and b of the Goel-Okumoto (G-0) NHPP model based on all available data.
(b) Obtain the mean value function $\mathrm{m}(\mathrm{t})$ and the reliability function.(c) What is the probability that a software failure does not occur in the time (hours) interval $[10,12]$ ?
(d) Choose another NHPP software reliability model and repeat items (a)-(c).
Is this model better than the G-O model? Explain why and justify your results.

Table 6.9. Failure in 1 hour (execution time) intervals

| Hour | Number of failures | Cumulative failures |
| :--: | :--: | :--: |
| 1 | 27 | 27 |
| 2 | 16 | 43 |
| 3 | 11 | 54 |
| 4 | 10 | 64 |
| 5 | 11 | 75 |
| 6 | 7 | 82 |
| 7 | 2 | 84 |
| 8 | 5 | 89 |
| 9 | 3 | 92 |
| 10 | 1 | 93 |

4. The data set \#9 which is given in Table 4.13 was reported in 1970 by Musa (1987). It shows the successive inter-failure times for a real-time command and control system. The recorded times in Table 4.13 are execution times, in seconds, between successive failures. Musa reports that fixes were introduced whenever a failure occurred and execution did not begin again until the identified failure source had been removed. Therefore, we can assume that there are no repeat occurrences of individual faults, although it is possible that an attempt to fix one fault may introduce new ones. Note that there are several zeros in the table, which are apparently accounted for by rounding up the raw times.
(a) Calculate the maximum likelihood estimates for the unknown parameters of the Musa exponential NHPP model based on all available data.
(b) Obtain the mean value function $m(t)$ and the reliability function.
(c) Choose three other NHPP S-shaped models in Sections 6.5-6.7 and repeat items (a) and (b). Draw your own conclusions and findings among the four models. Explain why and justify your results.
5. Based on the first 25 errors in Table 4.8 (data set \#4):
(a) Calculate the MLE for unknown parameters of five models discussed in Application 6.1 of Section 6.8.
(b) Obtain the mean value function and reliability function of all five models.
(c) Analyze and compare the results of all the models based on MSE and PRR criteria.6. Based on the phase 2 telecommunication system data set \#11 shown in Table 4.15(b):
(a) Calculate the MLE for unknown parameters of any five NHPP S-shaped models discussed in this chapter.
(b) Obtain the mean value function and reliability function of all five models.
(c) Analyze and compare the results of all the models.# Testing Coverage and Removal Models 

### 7.1 Introduction

Software reliability models based on an NHPP have been used to estimate and predict the quality of software products such as reliability, number of remaining errors, and failure intensity. Imperfect debugging, learning phenomenon of software developers, and other realistic issues have been studied during the last three decades (see Chapter 6). However, software development is a very complex process and there are important issues that have not been addressed. Testing coverage is one of these issues. Testing coverage is important information for both software developers and customers of software products. This chapter discusses various software reliability models incorporating testing coverage and fault removal.

### 7.2 Testing Coverage Models

Among all SRGMs, a large family of stochastic reliability models based on a nonhomogeneous Poisson process, which are known as NHPP reliability models, has been widely used to track reliability improvement during software testing. These models enable software developers to evaluate software reliability in a quantitative manner. They have also been successfully used to provide guidance in making decisions such as when to terminate testing the software or how to allocate available resources. However, software development is a very complex process and there are still issues that have not yet been addressed. Testing coverage is one of these issues. Testing coverage information is an important measure for both software developers and customers of software products.

Testing coverage (Pham 2003d) is a measure that enables software developers to evaluate the quality of the tested software and determine how much additional effort is needed to improve the reliability of the software. Testing coverage, on the other hand, can provide customers with a quantitative confidence criterion when they plan to buy or use the software products. To our knowledge, testing coveragehas not been addressed in the existing software reliability models. Testing coverage is an important measure for both software developers and users.

In this section, we discuss models incorporating testing coverage in the software development process and relate it to the error detection rate function. We examine the goodness-of-fit of the testing coverage model and other existing NHPP models based on several sets of software testing data.

# Notation 

$a(t) \quad$ Total errors content at time $t$
$b(t) \quad$ Error detection rate at time $t$
$c(t) \quad$ Testing coverage as a function of time $t$
$\lambda(t) \quad$ Intensity function or fault detection rate per unit time
$m(t) \quad$ Mean value function or the expected number of errors detected by time $t$
$R(x / t)$ Reliability function of software by time $t$ for a mission time $x$
$N(t) \quad$ Counting process representing the cumulative number of failures at time $t$
$\sum_{k} \quad$ Sum over $k$ from 1 to $n$
SSE Sum of squared errors of a model fitting the actual data
AIC Akaike's Information Criterion
PRR Predictive-risk ratio

## A Generalized Testing Coverage Model

Pham and Zhang (2003d) introduce a generalized model which incorporates testing coverage measure into software reliability assessment. Let $c(t)$ denote the percentage of the code coverage as a time dependent function which has been examined during software testing. Obviously, $1-c(t)$ is the percentage of the software code which has not yet been covered by test cases by time $t$. The derivative of the testing coverage function, $c^{\prime}(t)$, represents the coverage rate. Therefore, the error detection rate function can be expressed as $\frac{c^{\prime}(t)}{1-c(t)}$.
Theorem 7.1 (Pham and Zhang 2003d): The generalized NHPP model incorporating testing coverage can be formulated as follows:

$$
\frac{d m(t)}{d t}=\frac{c^{\prime}(t)}{1-c(t)}[(a(t)-m(t)]
$$

where $a(t)$ is the total fault content function. The explicit solution of the mean value function is given by:

$$
m(t)=e^{-B(t)}\left(m_{0}+\int_{t_{0}}^{t} a(\tau) e^{B(\tau)} \frac{c^{\prime}(\tau)}{1-c(\tau)} d \tau\right)
$$

where $B(t)=\int_{t_{0}}^{t} \frac{c^{\prime}(\tau)}{1-c(\tau)} d \tau$ and $m\left(t_{0}\right)=m_{0}$ is the marginal condition of equation (7.2) with $t_{0}$ representing the starting time of the debugging process.

This model indicates that the failure intensity depends on both the rate at which the remaining faults are covered and the number of remaining faults at current time $t$ divided by the current fractional population of uncovered faults.Once the total fault content function, $a(t)$, and testing coverage function, $c(t)$, are determined, the explicit solution of the mean value function $\mathrm{m}(\mathrm{t})$ of equation (7.1) can be obtained. From equation (7.2), the reliability function (see equation 5.3) can be obtained.

# A Testing Coverage Function 

Assuming that the testing coverage function $c(t)$ is a non-negative and concave function of time $t$ (see Figure 7.1), then the error detection rate is an S-shaped curve (see Figure 7.2).

Theorem 7.2 (Pham and Zhang 2003d): Assume the testing coverage function

$$
c(t)=1-(1+b t) e^{-b t}
$$

and the error content rate function

$$
a(t)=a(1+\alpha t)
$$

and with $m(0)=0$, the mean value function is given as follows:

$$
\begin{aligned}
m(t)= & a\left(1+\alpha t-\frac{b t+1}{e^{b t}}\right) \\
& -\frac{a \alpha(1+b t)}{b e^{b t+1}}\left(\ln (b t+1)+\sum_{i=0}^{\infty} \frac{(1+b t)^{i+1}-1}{(i+1)!(i+1)}\right)
\end{aligned}
$$

This model is knowned as the PZ-Coverage model. The proof is straightforward as from equation (7.2).


Figure 7.1. Testing coverage function $c(t)$We assume that errors can be introduced during the debugging phase with a constant error introduction rate $\alpha$. Therefore, the error content rate function, $a(t)$, is a linear function of the testing time. The NHPP software reliability models can be used to predict the expected number of errors. Different models use different assumptions and therefore provide different mathematical forms for the mean value function.


Figure 7.2. The error detection rate function $v s$ time

# 7.3 Testing Coverage and Imperfect Debugging 

In existing software reliability models, imperfect debugging of the software testing process is usually studied by assuming that new errors can be introduced into the software during debugging and therefore the fault content function is a time dependent function of testing time. This leads to the fact that certain assumptions about fault content rate need to be made when selecting a software reliability model. In this section, we discuss a software reliability growth model which incorporates fault introduction phenomenon and testing coverage information into error detection (Pham 2005b). This model, however, does not require any specific assumptions for the fault content function. The number of faults in the software estimated by this model is consistent; in other words, this estimate does not change significantly with time.

## Notation

a Number of initial software faults
$d(t) \quad$ Imperfect debugging intensity rate# Assumptions 

The general NHPP software reliability growth model is formulated based on the following assumptions:

1. The occurrence of software failures follows an NHPP.
2. The software failure intensity rate at any time is proportional to the number of remaining faults in the software at that time.
3. When a software failure occurs, a debugging effort takes place immediately. This debugging is s-independent at each location of the software failures.
4. During the debugging process, the effort to remove each fault may not be perfect and therefore new faults may be introduced into the software system with the imperfect debugging intensity rate $d(t)$.
5. The imperfect debugging rate is assumed to decrease as testing progresses and becomes negligible towards the end of the testing phase because the experience and knowledge of the testing team increases with the progress of the learning process.
Under assumptions 4 and 5, a general NHPP model incorporating testing coverage and imperfect debugging can be formulated as follows:

$$
\frac{d m(t)}{d t}=\frac{c^{\prime}(t)}{1-c(t)}[a-m(t)]-d(t)[a-m(t)]
$$

where $a$ is the number of initial faults in the software code and $d(t)$ denotes the fault introduction rate which is a decreasing function of time. The function $c(t)$ represents the testing coverage function, which measure the percentage of the software code covered by testing cases up to any time $t$. Then, $1-c(t)$ is the percentage of the software code which has not yet been covered by test cases by time $t$. The derivative of the testing coverage function, $c^{\prime}(t)$, represents the coverage rate. Therefore, the fault detection rate function can be expressed as $\frac{c^{\prime}(t)}{1-c(t)}$ (see Figure 7.2).
Theorem 7.3 (Pham and Zhang 2005b): Let

$$
g(t)=\frac{c^{\prime}(t)}{1-c(t)}-d(t)
$$

be denoted as the imperfect fault detection rate. Then equation (7.6) can be rewritten as:

$$
\frac{d m(t)}{d t}=g(t)[a-m(t)]
$$

The mean value function is, therefore, given by:

$$
m(t)=e^{-B(t)}\left[m_{0}+\int_{0} a e^{B(\tau)} g(\tau) d \tau\right]
$$where $B(t)=\int_{t_{0}} g(\tau) d \tau$ and $m\left(t_{0}\right)=m_{0}$ is the marginal condition with $t_{0}$ representing the starting time of the debugging process.

The proof is straightforward and left to readers (see Problem 7.1). Software reliability $R(x / t)$ is defined as the probability that a software failure does not occur in $(t, t+x)$, given that the last failure occurred at testing time $t(t \geq 0, x>0)$. Therefore, the software reliability function is given by

$$
R(x / t)=e^{-[m(t+x)-m(t)]}
$$

where $m(t)$ is given in equation (7.8).
Theorem 7.4 (Pham and Zhang 2004): Consider the testing coverage function

$$
c(t)=1-(1+b t) e^{-b t}
$$

and the fault introduction rate, $d(t)$, as a decreasing function of testing time $t$ (see Figure 7.3), as follows:

$$
d(t)=\frac{d}{1+d t}
$$

From equation (7.8) with the initial condition $m(0)=0$, the mean value function is given by

$$
m(t)=a-a e^{-b t}\left[1+(b+d) t+b d t^{2}\right]
$$

This model is known as Pham-Zhang imperfect fault detection (Pham-Zhang IFD).
Proof: See Problem 7.2.
From equation (7.9),

$$
c(t)=1-(1+b t) e^{-b t}
$$

the fault detect rate function can be expressed as:

$$
\frac{c^{\prime}(t)}{1-c(t)}=\frac{b^{2} t}{1+b t}
$$

Given $d(t)=\frac{d}{1+d t}$ then the imperfect fault detection rate function can be expressed as

$$
g(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t}
$$

where the first term is the fault detection rate function and the second term is the imperfect fault detection rate.

# 7.4 Fault Removal Efficiency Model 

Although some software reliability studies addressed the imperfect debugging phenomenon, most of them only considered possibilities of adding new faultswhile removing the existing ones. However, imperfect debugging also means that detected faults are removed with an imperfect removal efficiency rate other than $100 \%$. Jones (1996) pointed out that the defect removal efficiency is an important factor for software quality and process management. It can provide software developers with the estimation of testing effectiveness and the prediction of additional effort. Moreover, fault removal efficiency is usually way below $100 \%$ (e.g., it ranges from $15 \%$ to $50 \%$ for unit test, $25 \%$ to $40 \%$ for integration test, and $25 \%$ to $55 \%$ for system test.


Figure 7.3. Imperfect fault detection rate function $d(t)$ vs testing time

Goel and Okumoto (1979b) also considered a similar conception in their Markov model. They assumed that after a failure the residual faults remained the same with probability $q$ and it reduces to one less than current value with probability $p$. In other words, fault removal is not always $100 \%$. Pham (2005c) recently applied a birth-death process to software reliability modeling, considering both imperfect fault removal probability (death-process) and fault introduction (birth process). In practice, software fault detection is a very complex process. Usually when testers detected a deviation from the requirement, they create a modification request. Then a review board member will assign this request to a particular developer. After the developer studies the software fault, he/she will submit a code change to fix it. Thus, a software fault has to go through a fairly long life cycle which consists of various sequential states. It is not unusual for the software development team to find that a software fault has been reported many times before they are finally removed.This section discusses a software reliability growth model, studied by Zhang, Teng and Pham (Zhang 2003), addressing fault removal efficiency and fault introduction rate.

Fault removal efficiency is a practical and useful measure in real software development processes since it helps developers to evaluate the debugging effectiveness and estimate the future workload. Imperfect debugging is also considered regarding new faults being introduced into the software during debugging and the detected faults not being removed completely. As a result, this model can provide, in addition to traditional reliability measures, some useful reliability metrics to help the development team make better decisions.

# Notation 

$p \quad$ Fault removal efficiency, i.e., percentage of faults eliminated by reviews, inspections and tests
$\beta(t) \quad$ Fault introducing rate at time $t$

## Assumption

The following are the assumptions for this model:

1. The occurrence of software failures follows an NHPP.
2. The software fault detection rate at any time is proportional to the number of remaining faults in the software at that time.
3. When a software failure occurs, a debugging effort takes place immediately. This debugging is $s$-independent at each location of the software failures.
4. For each debugging effort, whether the fault is successfully removed or not, some new faults may be introduced into the software system with probability $\beta(t)$.

## A Generalized Model with Fault Removal Efficiency

Fault removal efficiency is defined as the percentage of bugs eliminated by reviews, inspections, and tests. This is a very important and convenient metric in software development practice. Incorporating this metrics into software reliability analysis will not only improve the software reliability assessment but also change quality from an amorphous term to a tangible factor.

This section also presents an explicit solution to the differential equation of the proposed model. The mean value function that incorporate both fault removal efficiency and fault introduction phenomena can be obtained by solving the system of differential equations as follows:

$$
\begin{gathered}
\frac{d m(t)}{d t}=b(t)[a(t)-p m(t)] \\
\frac{d a(t)}{d t}=\beta(t) \frac{d m(t)}{d t}
\end{gathered}
$$

where $p$ represents the fault removal efficiency, which means $\mathrm{p} \%$ of detected faults can be eliminated completely during the development process. The function $m(t)$ in equation (7.13) represents the expected number of faults detected by time $t$, and $p m(t)$ thenrepresents the expected number of faults that can be successfully removed. Existing models usually assume that $p$ is $100 \%$. The marginal conditions for the differential equations (7.13) and (7.14) are as follows:

$$
m(0)=0 \text { and } a(0)=a
$$

where a is the number of initial faults in the software system before testing starts. Equation (7.13) can be deduced directly from assumption 2 and 3. Software system failure rate is proportional to the expected number of remaining faults in the software at time $t$. The expected number of residual faults is given by

$$
x(t)=a(t)-p m(t)
$$

Notice that when $p=1$, the proposed model can be reduced to an existing NHPP model. Equation (7.14) can also be directly deduced from assumption 3 and 4. The fault content rate $a^{\prime}(t)$ in the software at time $t$ is proportional to the rate of debugging efforts to the system, which equals to $m^{\prime}(t)$ because of assumption 3. Equation (7.15) can be used to derive explicit solutions of equations (7.13) and (7.14). By taking derivatives on both sides of equation (7.15), we obtain

$$
\frac{d x(t)}{d t}=\frac{d a(t)}{d t}-p \frac{d m(t)}{d t}=(\beta(t)-p) \frac{d m(t)}{d t}
$$

or

$$
\frac{d x(t)}{d t}=(\beta(t)-p) b(t) x(t)
$$

with marginal condition

$$
x(0)=a(0)-m(0)=a
$$

Hence, the expected number of residual faults given by equation (7.16) is

$$
x(t)=a e^{-\int_{a}^{t}(p-\beta(\tau)) b(\tau) d \tau}
$$

From equation (7.13), the failure intensity function can be expressed as follows:

$$
\lambda(t)=m^{\prime}(t)=b(t)(a(t)-p m(t))=b(t) x(t)
$$

Theorem 7.5 (Zhang et al. 2003): The explicit mean value function and fault content rate function can respectively be obtained as follows:

$$
m(t)=\int_{0}^{t} x(u) b(u) d u=a \int_{0}^{t} b(u) e^{-\int_{a}^{t}(p-\beta(\tau)) b(\tau) d \tau} d u
$$

and

$$
a(t)=a\left(1+\int_{0}^{t} \beta(u) b(u) e^{-\int_{a}^{t}(p-\beta(\tau)) b(\tau) d \tau} d u\right)
$$

Proof: Using the result in equation (7.18), one can easily also obtain the solution for the fault content rate function by taking the integral of equation (7.14).In this section, we present a model studied by Zhang et al. (2003), called the Zhang-Teng-Pham model, from the general class of model presented in the previous section. The fault detection rate function in this model, $b(t)$, is a nondecreasing function with inflexion S-shaped curve, which captures the learning process of the software developers. In the existing models, however, the upper bound of fault detection rate is assumed to be the same as the learning curve increasing rate.

In this chapter, we relax this assumption and use a different parameter for the upper bound of fault detection rate (see equation 7.20). The model also addresses imperfect debugging by assuming faults can be introduced during debugging with a constant fault introduction rate, $\beta$.

Theorem 7.6 (Zhang et al. (2003): Assume

$$
\begin{aligned}
& b(t)=\frac{c}{1+\alpha e^{-b t}} \\
& \beta(t)=\beta
\end{aligned}
$$

The mean value function for the Zhang-Teng-Pham model is as follows:

$$
m(t)=\frac{a}{p-\beta}\left[\left(1-\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{\frac{c}{(p-\beta)}}\right]
$$

Proof: Substituting equation (7.20) into Eq. (7.19), we can easily obtain the result. Note that as $t$ approaches $\infty, m(t)$ converges to its upper bound $\frac{a}{p-\beta}$. The expected number of residual faults $X(t)$ is given by:

$$
X(t)=a\left[\left(\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{\frac{c}{(p-\beta)}}\right]
$$

and the software failure rate is:

$$
\lambda(t)=\frac{a c}{1+\alpha e^{-b t}}\left[\left(\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{\frac{c}{(p-\beta)}}\right]
$$

Table 7.1 summarizes many existing NHPP models mentioned in this chapter where the function $a(t)$ is defined as the fault content function, $b(t)$ is the fault detection function, and $g(t)$ is the imperfect fault detection rate, together with most of the recent models presented in current software reliability literature.Table 7.1. Summary of the software reliability models

| Model | $\operatorname{MVF}(m(t))$ | Comments |
| :--: | :--: | :--: |
| Goel- <br> Okumoto <br> (G-O) | $\begin{aligned} & m(t)=a\left(1-e^{-b t}\right) \\ & a(t)=a \\ & b(t)=b \end{aligned}$ | Also called exponential model |
| Delayed Sshaped | $m(t)=a\left(1-[1+b t] e^{-b t}\right)$ | Modification of G-O model |
| Inflection S-shaped | $\begin{aligned} & m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}} \\ & a(t)=a \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | Becomes the same as G-O if $\beta=0$ |
| Yamada Exponential | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-b t)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta e^{-\beta t} \end{aligned}$ | Attempt to account for testing-effort |
| Yamada <br> Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-b t^{2} / 2)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta t e^{-\beta t^{2} / 2} \end{aligned}$ | Attempt to account for testing-effort |
| Yamada. imperfect debugging (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha \mathrm{t}}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ | Assume exponential fault content function and constant fault detection rate |
| Yamada. imperfect debugging (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \\ & b(t)=b \end{aligned}$ | Assume constant introduction rate $\alpha$ and the fault detection rate |Table 7.1. (continued)

| PNZ model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\mathrm{bt}}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | Assume introduction rate is a linear function of testing time, and the fault detection rate function is nondecreasing inflexion S-shaped model |
| :--: | :--: | :--: |
| Pham-Zhang model | $\begin{aligned} m(t)= & \frac{1}{\left(1+\beta e^{-b t}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ a(t)= & c+a\left(1-e^{-\alpha t}\right) \\ b(t)= & \frac{b}{1+\beta e^{-b t}} \end{aligned}$ | Assume introduction rate is exponential function of the testing time, and the fault detection rate is nondecreasing with an inflexion S-shaped model |
| PZ-coverage | $\begin{aligned} & m(t)=a\left(1+\alpha t-\frac{b t+1}{e^{b t}}\right)-\frac{a \alpha(1+b t)}{b e^{b t+1}} \times \\ & \quad\left[\ln (b t+1)+\sum_{i=0}^{\infty} \frac{(1+b t)^{i+1}-1}{(i+1)!(i+1)}\right] \\ & a(t)=a(1+\alpha t) \\ & c(t)=1-(1+b t) e^{-b t} \end{aligned}$ | Assume introduction rate is a linear function of time and incorporates the testing coverage function into reliability model |
| PhamZhang IFD | $\begin{aligned} & m(t)=a-a e^{-b t}\left(1+(b+d) t+b d t^{2}\right) \\ & a(t)=a \\ & g(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t} \end{aligned}$ | Assume a constant initial fault content function, and the imperfect fault detection rate combining the fault introduction phenomenon |
| Zhang-TengPham model | $\begin{aligned} & m(t)=\frac{a}{p-\beta}\left[1-\left(\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{c(p-\beta)}\right] \\ & a^{\prime}(t)=\beta(t) m^{\prime}(t) \\ & b(t)=\frac{c}{1+\alpha e^{-b t}} \\ & \beta(t)=\beta \end{aligned}$ | Assume constant fault introduction rate, and the fault detection rate function is nondecreasing with an infle- xion Sshaped model |# 7.5 Model Implementations 

In this section, two sets of data will be used to analyze the PZ-coverage model and compare it to the existing NHPP software reliability models. These two sets of data are from IBM and AT\&T applications. First, the parameters of each model are estimated and the mean value functions are determined. Second, all the models are compared and the results are presented in Tables 7.2 and 7.3. We examine the goodness-of-fit and predictive power of the models based on the six software application data sets.

Application 7.1. IBM On-line Data Entry (data set \#6, Table 4.10, Chapter 4) Implementation of PZ-coverage Model: Consider the data set \#6 (listed in Table 4.10, Chapter 4) reported by Ohba (1984) are recorded from testing an on-line data entry software package developed at IBM. Table 4.10 of data set \#6 shows the pair of the observation time (days) and the cumulative number of errors that were detected. Here we fit all the given models in Table 7.1 to IBM data set. The estimators, the SSEs, and the AICs for each model are presented in Table 7.2.

Table 7.2. Model comparison: IBM data

| Model <br> name | MVF (m(t) ) and MLEs | N | SSE | AIC |
| :-- | :-- | :--: | :--: | :--: |
| Goel- <br> Okumoto <br> (G-O) | $m(t)=a\left(1-e^{-b t}\right)$ <br> $\hat{a}=19.54, \hat{b}=0.0049$ | 2 | 76.38 | 34.38 |
| Delayed S- <br> shaped <br> SRGM | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ <br> $\hat{a}=15.85, \hat{b}=0.0157$ | 2 | 231.78 | 38.06 |
| Inflection <br> S-shaped <br> SRGM | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ <br> $\hat{a}=28.58, \hat{b}=0.00013, \hat{\beta}=0.965$ | 3 | 74.51 | 34.34 |
| Yamada <br> Exponential | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t / t}\right)}\right)$ <br> $\hat{a}=368.22, \hat{\alpha}=0.055, \hat{\beta}=0.0048$ | 4 | 76.55 | 38.38 |
| Yamada <br> Rayleigh | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t / t / 2)}\right)}\right.$ <br> $\hat{a}=17.62, \hat{\alpha}=2.1073, \hat{\beta}=5.38 \times 10^{-5}$ | 4 | 329.30 | 44.82 |
| Yamada <br> Imperfect <br> Debugging <br> model (1) | $m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha \cdot 1}-e^{-b t}\right)$ <br> $\hat{a}=12.66, \hat{b}=0.0084, \hat{\alpha}=0.001237$ | 3 | 70.89 | 36.33 |Table 7.2. (continued)

| Yamada Imperfect Debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & \hat{a}=11.40, \hat{b}=0.0094, \hat{\alpha}=0.001925 \end{aligned}$ | 3 | 71.88 | 36.38 |
| :--: | :--: | :--: | :--: | :--: |
| PNZ model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\alpha}} \\ & \hat{a}=27.1363, \hat{b}=0.000144, \\ & \hat{\alpha}=0.000146, \hat{\beta}=0.9629 \end{aligned}$ | 4 | 74.22 | 38.33 |
| Pham- <br> Zhang <br> model | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\alpha}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-a t}-e^{-b t}\right)\right] \\ & \hat{a}=23.97, \hat{b}=8.8 \times 10^{-5}, \hat{\alpha}=3.5 \times 10^{-4} \\ & \hat{\beta}=0.9785, \hat{a}=25.9 \end{aligned}$ | 5 | 70.81 | 40.33 |
| PZ- <br> coverage | $\begin{aligned} & m(t)=a\left(1+\alpha t-\frac{b t+1}{e^{b t}}\right)-\frac{a \alpha(1+b t)}{b e^{b t+1}} \times \\ & \quad\left[\ln (b t+1)+\sum_{i=0}^{\infty} \frac{(1+b t)^{i+1}-1}{(i+1)!(i+1)}\right] \\ & \hat{a}=7.0, \hat{b}=0.0301, \hat{\alpha}=0.0045 \end{aligned}$ | 3 | 50.75 | 37.09 |

From Table 7.2, the PZ-coverage model performs significantly better than the others when applied to this data set. The SSE value of PZ-coverage model, which is 50.75 , is much lower than those of other models. The second criterion, AIC, of the PZ-coverage model is also reasonably low. The testing coverage function, $c(t)$, as a function of time $t$ is presented in Figure 7.4. Definitely more application is needed to validate fully this finding.

Application 7.2. AT\&T System T Project (data Set \#7, Table 4.11) - Implementation of PZ-coverage Model: The AT\&T's System $T$ is a network-management system developed by AT\&T that receives data from telemetry events, such as alarms, facility-performance information, and diagnostic messages, and forwards them to operators for further action. The system has been tested and failure data has been collected (Ehrlich 1993). Table 4.11 shows the failures and the interfailure as well as cumulative failure times (in CPU units). We fit all of the models listed in Table 7.1 based on the AT\&T data set. Table 7.3 summarizes the SSE and AIC scores for all of these models.

Figure 7.4. Testing coverage of IBM data

Table 7.3. Model comparison (data set \#7)

| Model name | MVF (m(t) ) | N | SSE | MLEs |
| :--: | :--: | :--: | :--: | :--: |
| Goel-Okumoto (G-O) | $m(t)=a\left(1-e^{-b t}\right)$ | 2 | 281.33 | $\begin{aligned} & \hat{a}=24.3 \\ & \hat{b}=0.00347 \end{aligned}$ |
| Delayed Sshaped SRGM | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ | 2 | 624.33 | $\begin{aligned} & \hat{a}=22.40 \\ & \hat{b}=0.00878 \end{aligned}$ |
| Inflection Sshaped SRGM | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ | 3 | 281.38 | $\begin{aligned} & \hat{a}=24.30 \\ & \hat{b}=0.0035 \\ & \hat{\beta}=0.001 \end{aligned}$ |
| Yamada exponential | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t \beta / t)}\right)}\right)$ | 4 | 283.40 | $\begin{aligned} & \hat{a}=1373.79 \\ & \hat{\alpha}=0.0179 \\ & \hat{\beta}=0.0034 \end{aligned}$ |
| Yamada <br> Rayleigh | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t \beta / 2 / 2)}\right)}\right)$ | 4 | 421.97 | $\begin{aligned} & \hat{a}=20.50 \\ & \hat{\alpha}=2.839 \\ & \hat{\beta}=2.29 \times 10^{-5} \end{aligned}$ |
| Yamada imperfect debugging model (1) | $m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right)$ | 3 | 223.94 | $\begin{aligned} & \hat{a}=16.67 \\ & \hat{b}=0.00623 \\ & \hat{\alpha}=0.000546 \end{aligned}$ |Table 7.3. (continued)

| Yamada imperfect debugging model (2) | $m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t$ | 3 | 254.42 | $\hat{a}=16.13$ <br> $\hat{b}=0.0064$ <br> $\hat{\alpha}=0.00716$ |
| :--: | :--: | :--: | :--: | :--: |
| P-N-Z model | $m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{4 \mathrm{a}}}$ | 4 | 254.38 | $\hat{a}=16.1214$ <br> $\hat{b}=0.00643$ <br> $\hat{\alpha}=0.000717$ <br> $\hat{\beta}=0.001$ |
| Pham-Zhang | $m(t)=\frac{(c+a)\left(1-e^{-b t}\right)}{\left(1+\beta \mathrm{e}^{4 \mathrm{a}}\right)}$ <br> $-\frac{a b\left(e^{-\alpha t}-e^{-b t}\right)}{(b-\alpha)\left(1+\beta \mathrm{e}^{4 \mathrm{a}}\right)}$ | 5 | 222.76 | $\hat{a}=211.449$ <br> $\hat{b}=0.01449$ <br> $\hat{\alpha}=6.75 \times 10^{-5}$ <br> $\hat{\beta}=1.9815$ <br> $\hat{d}=13.455$ |
| PZ-coverage | $m(t)=a\left(1+\alpha t-\frac{b t+1}{e^{b t}}\right)$ <br> $-\frac{a \alpha(1+b t)}{b e^{b t+1}} \times$ <br> $\left[\ln (b t+1)+\sum_{i=0}^{\infty} \frac{(1+b t)^{i+1}-1}{(i+1)!(i+1)}\right]$ | 3 | 180.34 | $\hat{a}=15.0$ <br> $\hat{b}=0.013$ <br> $\hat{\alpha}=0.0007$ |

From Table 7.3, we find that the testing PZ-coverage model performs significantly better than the others when applied to the AT\&T data set based on the SSE criterion. The testing coverage function, $c(t)$, as a function of time $t$ is presented in Figure 7.5.

Application 7.3. Data from IBM Entry Software Package - Implementation of Pham-Zhang IFD Model: This section examines both the goodness-of-fit of the Pham-Zhang IFD model and the existing ones using the software failure data collected from testing an On-line data entry software package at IBM (Ohba 1984a) (see data set 1, Table 4.5). The failures are recorded in days.

Figure 7.5. Testing coverage of AT\&T System T (data set \#7)

We use subset of the above data to fit the models and estimate the parameters. Then we use the remaining ones to compare the predictive power of these existing models. For illustration purpose, we assume that the software has been tested for 17 days and the software failures during these 17 days are recorded.

We estimate the parameters and determine the software reliability models using the first 17 data points, given in Table 7.4. Second, we utilized all the 21day's data to estimate the model parameters, and the last column of Table 7.4 lists the estimation using the 21-day's data.

From Table 7.4, we find that the Pham-Zhang IFD model provides consistent estimates for the number of initial faults $(\hat{a})$. That is, $\hat{a}$ estimated using 17 data points is very close to the one estimated using 21 data points. This consistency will provide software developers with the precise information of how many initial faults are in the software and how many faults remain in the code at any time in the testing process.

Table 7.5 summarizes the MSE value for model comparison where MSE is calculated based on 21-day failure data. From the results, we can draw a conclusion that the new model provides the best fit.Table 7.4. MLEs of model parameters (IBM data)

| Model name | $\operatorname{MVF}(m(t))$ | MLEs <br> (17 data <br> points) | MLEs <br> (21 data points) |
| :-- | :-- | :-- | :-- |
| Goel- <br> Okumoto <br> (G-O) | $m(t)=a\left(1-e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=b$ | $\hat{a}=37435.36$ <br> $\hat{b}=5.9710^{-5}$ | $\hat{a}=56051$ <br> $\hat{b}=3.9 \times 10^{-5}$ |
| Delayed S- <br> shaped | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=\frac{b^{2} t}{1+b t}$ | $\hat{a}=75.36$ <br> $\hat{b}=0.1995$ | $\hat{a}=71.73$ <br> $\hat{b}=0.10397$ |
| Inflexion S- <br> shaped | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ <br> $a(t)=a$ <br> $b(t)=\frac{b}{1+\beta e^{-b t}}$ | $\hat{a}=63.25$ <br> $\hat{b}=0.1558$ <br> $\hat{\beta}=7.743$ | $\hat{a}=57.37$ <br> $\hat{b}=0.175$ <br> $\hat{\beta}=8.5136$ |
| Yamada <br> exponential | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t / t}\right)}}\right)$ <br> $a(t)=a$ <br> $b(t)=r \alpha \beta e^{-\beta t}$ | $\hat{a}=17081$ <br> $\hat{\alpha}=0.725$ <br> $\hat{\beta}=0.00018$ | $\hat{a}=17264.83$ <br> $\hat{\alpha}=0.734$ <br> $\hat{\beta}=0.000173$ |
| Yamada <br> Rayleigh | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t / t / 2)}\right)}\right)$ <br> $a(t)=a$ <br> $b(t)=r \alpha \beta t e^{-\beta t^{2} / 2}$ | $\hat{a}=645.57$ <br> $\hat{\alpha}=0.0837$ <br> $\hat{\beta}=0.0089$ | $\hat{a}=664.19$ <br> $\hat{\alpha}=0.086$ <br> $\hat{\beta}=0.0083$ |
| Yamada <br> imperfect <br> debugging <br> model (1) | $m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha 1}-e^{-b t}\right)$ <br> $a(t)=a e^{\alpha t}$ <br> $b(t)=b$ | $\hat{a}=91920.94$ <br> $\hat{\alpha}=0.0454$ <br> $\hat{b}=1.6110^{-5}$ | $\hat{a}=39252.6$ <br> $\hat{\alpha}=0.0185$ <br> $\hat{b}=4.57 \times 10^{-5}$ |
| Yamada <br> imperfect <br> debugging <br> model (2) | $m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t$ <br> $a(t)=a(1+\alpha t)$ <br> $b(t)=b$ | $\hat{a}=1787056$ <br> $\hat{\alpha}=0.08104$ <br> $\hat{b}=7.4110^{-6}$ | $\hat{a}=1671644$ <br> $\hat{\alpha}=0.02932$ <br> $\hat{b}=1.0 \times 10^{-6}$ |Table 7.4. (continued)

| PNZ Model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\mathrm{bt}}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=63.19 \\ & \hat{b}=0.1559 \\ & \hat{\alpha}=4.9810^{-5} \\ & \hat{\beta}=7.735 \end{aligned}$ | $\begin{aligned} & \hat{a}=57.30 \\ & \hat{b}=0.175 \\ & \hat{\alpha}=4.96 \times 10^{-5} \\ & \hat{\beta}=8.506 \end{aligned}$ |
| :--: | :--: | :--: | :--: |
| Pham-Zhang model | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{bt}}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=303.71 \\ & \hat{b}=0.01125 \\ & \hat{\alpha}=0.0625 \\ & \hat{\beta}=0.03105 \\ & \hat{c}=104.0103 \end{aligned}$ | $\begin{aligned} & \hat{a}=167.9 \\ & \hat{b}=0.0112 \\ & \hat{\alpha}=0.1592 \\ & \hat{\beta}=0.01785 \\ & \hat{c}=100.615 \end{aligned}$ |
| Pham-Zhang IFD | $\begin{aligned} & m(t)=a-a e^{-b t}\left(1+(b+d) t+b d t^{2}\right) \\ & a(t)=a \\ & g(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t} \end{aligned}$ | $\begin{aligned} & \hat{a}=60.32 \\ & \hat{b}=0.138 \\ & \hat{d}=0.011 \end{aligned}$ | $\begin{aligned} & \hat{a}=60 \\ & \hat{b}=0.137 \\ & \hat{d}=0.013 \end{aligned}$ |

Table 7.5. Model comparison (IBM data)

| Model name | $\operatorname{MVF}(m(t))$ | MSE (fit) |
| :-- | :-- | :--: |
| Goel-Okumoto <br> (G-O) | $m(t)=a\left(1-e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=b$ | 117.24 |
| Delayed S-shaped | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=\frac{b^{2} t}{1+b t}$ | 38.0 |
| Inflexion S- <br> shaped | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ <br> $a(t)=a$ <br> $b(t)=\frac{b}{1+\beta e^{-b t}}$ | 52.01 |Table 7.5. (continued)

| Yamada exponential | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{t-\beta t}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta e^{-\beta t} \end{aligned}$ | 124.81 |
| :--: | :--: | :--: |
| Yamada Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{t-\beta t^{2} / 2)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta t e^{-\beta t^{2} / 2} \end{aligned}$ | 36.89 |
| Yamada imperfect <br> debugging model <br> (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ | 53.09 |
| Yamada imperfect debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \\ & b(t)=b \end{aligned}$ | 43.87 |
| PNZ model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\mathrm{bt}}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 34.05 |
| Pham-Zhang model | $\begin{aligned} m(t)= & \frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{bt}}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ a(t)= & c+a\left(1-e^{-\alpha t}\right) \\ b(t)= & \frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 37.13 |
| Pham-Zhang IFD | $\begin{aligned} & m(t)=a-a e^{-b t}\left(1+(b+d) t+b d t^{2}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t} \end{aligned}$ | 32.20 |Application 7.4. Real Time Control Systems (data set 8, Table 4.12) Implementation of Pham-Zhang IFD Model: We examine the models using a data set collected from testing a program for monitor and real-time control systems. The software consists of about 200 modules and each module has, on average, 1000 lines of a high-level language like FORTRAN.

Table 4.12 records the software failures detected during the 111-day testing period. This actual data is concave overall with several ups and downs reflecting different clusters of detected faults.

Since the software turns stable after 61 days of testing, we will estimated the model parameters using the first 61 data points and compare them with parameter estimates using all the 111 data points. The results are summarized in Table 7.6.

There are totally 481 faults detected by the end of 111-day of testing period. From Table 7.6, the number of initial faults, $a$, estimated by the PNZ and PhamZhang IFD models using the first 61 data points are 470.8 and 482.5 , respectively, whereas when using all the 111 data are 470.8 and 482 respectively.

We can draw the following conclusions: (1) both estimates are very close to the actual number of total faults; (2) the estimation is stable and consistent. This indicates that the new model can provide developers with precise information about the total number of initial faults and number of remaining faults at any time during testing phase.

Table 7.7 summarizes the MSE values of model prediction. From Table 7.7, Pham-Zhang IFD model seems likely to fit and predict better than other existing models on these data sets.Table 7.6. MLEs of model parameters (data set \#8)

| Model name | $\operatorname{MVF}(m(t))$ | MLEs <br> (61 data pts) | MLEs <br> (111 data pts) |
| :--: | :--: | :--: | :--: |
| Goel- <br> Okumoto <br> (G-O) | $\begin{aligned} & m(t)=a\left(1-e^{-b t}\right) \\ & a(t)=a \\ & b(t)=b \end{aligned}$ | $\hat{a}=852.97$ <br> $\hat{b}=0.01283$ | $\hat{a}=497.282$ <br> $\hat{b}=0.0308$ |
| Delayed S- <br> shaped | $\begin{aligned} & m(t)=a\left(1-(1+b t) e^{-b t}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t} \end{aligned}$ | $\hat{a}=522.49$ <br> $\hat{b}=0.06108$ | $\hat{a}=483.039$ <br> $\hat{b}=0.06866$ |
| Inflexion S- <br> shaped | $\begin{aligned} & m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}} \\ & a(t)=a \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=852.45 \\ & \hat{b}=0.01285 \\ & \hat{\beta}=0.001 \end{aligned}$ | $\begin{aligned} & \hat{a}=482.017 \\ & \hat{b}=0.07025 \\ & \hat{\beta}=4.15218 \end{aligned}$ |
| Yamada exponential | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-f t) t}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta e^{-\beta t} \end{aligned}$ | $\begin{aligned} & \hat{a}=9219.7 \\ & \hat{\alpha}=0.09995 \\ & \hat{\beta}=0.01187 \end{aligned}$ | $\begin{aligned} & \hat{a}=67958.8 \\ & \hat{\alpha}=0.00732 \\ & \hat{\beta}=0.03072 \end{aligned}$ |
| Yamada <br> Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-f t t^{2} / 2)}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta t e^{-\beta t^{2} / 2} \end{aligned}$ | $\begin{aligned} & \hat{a}=611.70 \\ & \hat{\alpha}=1.637 \\ & \hat{\beta}=0.00107 \end{aligned}$ | $\begin{aligned} & \hat{a}=500.146 \\ & \hat{\alpha}=3.31944 \\ & \hat{\beta}=0.00066 \end{aligned}$ |
| Yamada imperfect <br> debugging model (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ | $\begin{aligned} & \hat{a}=1795.7 \\ & \hat{b}=0.00614 \\ & \hat{\alpha}=0.002 \end{aligned}$ | $\begin{aligned} & \hat{a}=654.963 \\ & \hat{b}=0.02059 \\ & \hat{\alpha}=0.0027 \end{aligned}$ |
| Yamada imperfect <br> debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \\ & b(t)=b \end{aligned}$ | $\begin{aligned} & \hat{a}=16307 \\ & \hat{b}=0.0068 \\ & \hat{\alpha}=0.009817 \end{aligned}$ | $\begin{aligned} & \hat{a}=591.804 \\ & \hat{b}=0.02423 \\ & \hat{\alpha}=0.0019 \end{aligned}$ |Table 7.6. (continued)

| PNZ Model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\mathrm{bt}}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=470.759 \\ & \hat{b}=0.07497 \\ & \hat{\alpha}=0.00024 \\ & \hat{\beta}=4.69321 \end{aligned}$ | $\begin{aligned} & \hat{a}=470.759 \\ & \hat{b}=0.07497 \\ & \hat{\alpha}=0.00024 \\ & \hat{\beta}=4.69321 \end{aligned}$ |
| :--: | :--: | :--: | :--: |
| $\begin{aligned} & \text { Pham- } \\ & \text { Zhang } \\ & \text { model } \end{aligned}$ | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{bt}}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | $\begin{aligned} & \hat{a}=0.920318 \\ & \hat{b}=0.0579 \\ & \hat{\alpha}=2.76 \times 10^{-5} \\ & \hat{\beta}=3.152 \\ & \hat{c}=520.784 \end{aligned}$ | $\begin{aligned} & \hat{a}=0.46685 \\ & \hat{b}=0.07025 \\ & \hat{\alpha}=1.4 \times 10^{-5} \\ & \hat{\beta}=4.15213 \\ & \hat{c}=482.016 \end{aligned}$ |
| $\begin{aligned} & \text { Pham- } \\ & \text { Zhang IFD } \end{aligned}$ | $\begin{aligned} & m(t)=a-a e^{-b t}\left(1+(b+d) t+b d t^{2}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t} \end{aligned}$ | $\begin{aligned} & \hat{a}=482.5 \\ & \hat{b}=0.0751 \\ & \hat{d}=0.006 \end{aligned}$ | $\begin{aligned} & \hat{a}=482 \\ & \hat{b}=0.081 \\ & \hat{d}=0.007 \end{aligned}$ |

Table 7.7. Model Comparison (data set \#8)

| Model name | $\operatorname{MVF}(m(t))$ | MSE <br> (prediction) |
| :-- | :-- | :-- |
| Goel-Okumoto <br> (G-O) | $m(t)=a\left(1-e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=b$ | 11611.42 |
| Delayed S-shaped | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=\frac{b^{2} t}{1+b t}$ | 935.88 |
| Inflexion S-shaped | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ <br> $a(t)=a$ <br> $b(t)=\frac{b}{1+\beta e^{-b t}}$ | 590.38 |Table 7.7. (continued)

| Yamada exponential | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-p t t}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta e^{-\beta t} \end{aligned}$ | 12228.25 |
| :--: | :--: | :--: |
| Yamada Rayleigh | $\begin{aligned} & m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-p t t t}\right)}\right) \\ & a(t)=a \\ & b(t)=r \alpha \beta t e^{-\beta t^{2} / 2} \end{aligned}$ | 187.57 |
| Yamada imperfect <br> debugging model (1) | $\begin{aligned} & m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right) \\ & a(t)=a e^{\alpha t} \\ & b(t)=b \end{aligned}$ | 8950.54 |
| Yamada imperfect <br> debugging model (2) | $\begin{aligned} & m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t \\ & a(t)=a(1+\alpha t) \\ & b(t)=b \end{aligned}$ | 2752.83 |
| PNZ Model | $\begin{aligned} & m(t)=\frac{a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t}{1+\beta \mathrm{e}^{-\mathrm{bt}}} \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 2480.7 |
| Pham-Zhang model | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{bt}}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 102.66 |
| Pham-Zhang IFD | $\begin{aligned} & m(t)=a-a e^{-b t}\left(1+(b+d) t+b d t^{2}\right) \\ & a(t)=a \\ & b(t)=\frac{b^{2} t}{1+b t}-\frac{d}{1+d t} \end{aligned}$ | 9.37 |Application 7.5. Real Time Control System (data set \#9, Table 4.13) Implementation of Zhang-Teng-Pham Model: The data is documented in Lyu (1996). There are in total 136 faults reported and the time-between failures (TBF) in seconds are listed in Table 4.13. We tested the goodness of fit using the first 122 data points and the remaining data are used for the predictive power test. The SSE values for fit and prediction are listed in Table 7.8.

Basically, we perform the reliability estimation and prediction at any point in time. The reason for using the first 122 data points is that we observe an extremely long TBF from fault 122 to fault 123 and the TBFs after fault 123 increase tremendously which implies the reliability growth and system stability.

From Table 7.8, we observe that the Zhang-Teng-Pham model provides the best fit and prediction for this data set (both the SSE and the AIC values are the lowest among all models). Furthermore, some instrumental information can be obtained from the parameter estimation provided by the new model. For example, the fault removal efficiency $(\hat{p})$ is $90 \%$, which is relatively high according to (Zhang 2003). The number of initial faults $(\hat{a})$ is estimated to be 135 , together with $90 \%$ fault removal efficiency; the expected number of total detected faults is then 152. Therefore, at the assumed stopping point of 57042 seconds, there are about 30 $(152-122=30)$ faults remaining in the software.

The fault introduction rate $(\hat{\beta})$ is 0.012 , that is, on average, one fault will be introduced when 100 faults are removed. Some of the existing models (G-O, Yamada Exponential and Yamada Rayleigh) underestimate the expected number of total faults $(\hat{a}<136)$.

Software failure rate can be predicted after the parameters are estimated. Figure 7.6 shows the trend of failure rate for test and post-test period. Figure 7.7 illustrates the difference between the post-test failure rates predicted by several existing models listed in Table 7.8 and the proposed model.

For instance, the failure rate given by the G-O model is on the optimistic side. This is due to the following two reasons: (1) the G-O model underestimates the expected number of total faults ( 125 instead of 136) and (2) unlike the proposed model, the G-O model does not consider the fault removal efficiency. Thus, we can see that the new model has promising technical merit in the sense that it provides the development teams with both traditional reliability measures and in-process metrics.Table 7.8. Parameter estimation and model comparison

| Model name | SSE (fit) | SSE(Predict) | AIC | MLEs |
| :--: | :--: | :--: | :--: | :--: |
| G -O Model | 7615.1 | 704.82 | 426.05 | $\begin{aligned} & \hat{a}=125 \\ & \hat{b}=0.00006 \end{aligned}$ |
| Delayed S-shaped | 51729.23 | 257.67 | 546 | $\begin{aligned} & \hat{a}=140 \\ & \hat{b}=0.00007 \end{aligned}$ |
| Inflexion S-shaped | 15878.6 | 203.23 | 436.8 | $\begin{aligned} & \hat{a}=135.5 \\ & \hat{b}=0.00007 \\ & \hat{\beta}=1.2 \end{aligned}$ |
| Yamada exponential | 6571.55 | 332.99 | 421.18 | $\begin{aligned} & \hat{a}=130 \\ & \hat{\alpha}=10.5 \\ & \hat{\beta}=5.4 \times 10^{-6} \end{aligned}$ |
| Yamada Rayleigh | 51759.23 | 258.45 | 548 | $\begin{aligned} & \hat{a}=130 \\ & \hat{\alpha}=5 \times 10^{-10} \\ & \hat{\beta}=6.035 \end{aligned}$ |
| Yamada imperfect debugging model (1) | 5719.2 | 327.99 | 450 | $\begin{aligned} & \hat{a}=120 \\ & \hat{b}=0.00006 \\ & \hat{\alpha}=1 \times 10^{-5} \end{aligned}$ |
| Yamada imperfect debugging model (2) | 6819.83 | 482.7 | 416 | $\begin{aligned} & \hat{a}=120.3 \\ & \hat{b}=0.00005 \\ & \hat{\alpha}=3 \times 10^{-5} \end{aligned}$ |
| PNZ model | 5755.93 | 106.81 | 415 | $\begin{aligned} & \hat{a}=121 \\ & \hat{b}=0.00005 \\ & \hat{\alpha}=2.5 \times 10^{-6} \\ & \hat{\beta}=0.002 \end{aligned}$ |
| Pham-Zhang model | 14233.88 | 85.36 | 416 | $\begin{aligned} & \hat{a}=20 \\ & \hat{b}=0.00007 \\ & \hat{\alpha}=1.0 \times 10^{-5} \\ & \hat{\beta}=1.922 \\ & \hat{c}=125 \end{aligned}$ |
| Zhang-Teng-Pham model | 4783.12 | 32.06 | 411.36 | $\begin{aligned} & \hat{a}=135 \\ & \hat{b}=0.001 \\ & \hat{\alpha}=0.01 \\ & \hat{\beta}=0.012 \\ & \hat{c}=3.5 \times 10^{-5} \end{aligned}$ |

Figure 7.6. The trend of failure rate for test and post-test period (data set \#9)

# Failure Rate 



Figure 7.7. The difference between the post-test failure rates predicted

Application 7.6. Tandem Computers Data (Data set \#5, Table 4.9) Implementation of Zhang-Teng-Pham Model: In this example, we look at the predictive power of the Zhang-Teng-Pham model and G-O model using software (Release 1) failure data set \#5 listed in Table 4.9 (Wood 1996). Table 7.9 showsthe results predicted using the CPU execution hours as the time frame. From Table 7.9, we observe that Z-T-P FRE model predicts significantly better than the G-O model based on the SSE and AIC values.

The estimates of the parameters and their implications can be summarized as follows: fault removal efficiency $\hat{p}=0.63$, which is below average. Jones (1996) mentioned that the fault removal efficiency ranges from 45 to $99 \%$ with the average $72 \%$. Thus more resources need to be allocated to improve the fault removal efficiency. The result also shows that the initial number of faults is $\hat{a}=$ 103.36, which is greater than the actual total detected faults by the end of the testing phase (100) and the estimated total number of faults by the end of testing phase is about 117. This implies that there are still a number of remaining faults in the software at the end of the testing phase. This agrees with the fact that about 20 faults were detected during user operational phase (Wood 1996). The MLEs of the other model parameters are $\hat{b}=0.095, \hat{\alpha}=0.00039$, and $\hat{\beta}=0.00054$.

Table 7.9. Comparison of G-O and Zhang-Teng-Pham using data set \#5 (Table 4.9)

| Release 1 |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| Testing time <br> (weeks) | CPU hours | Defects <br> found | Predicted total <br> defects by G-O <br> model | Predicted total <br> defects by Z-T- <br> P FRE model |
| 1 | 519 | 16 | - | - |
| 2 | 968 | 24 | - | - |
| 3 | 1,430 | 27 | - | - |
| 4 | 1,893 | 33 | - | - |
| 5 | 2,490 | 41 | - | - |
| 6 | 3,058 | 49 | - | - |
| 7 | 3,625 | 54 | - | - |
| 8 | 4,422 | 58 | - | - |
| 9 | 5,218 | 69 | - | - |
| 10 | 5,823 | 75 | 98 | 74.7 |
| 11 | 6,539 | 81 | 107 | 80.1 |
| 12 | 7,083 | 86 | 116 | 85.2 |
| 13 | 7,487 | 90 | 123 | 90.0 |
| 14 | 7,846 | 93 | 129 | 94.6 |
| 15 | 8,205 | 96 | 129 | 98.9 |
| 16 | 8,564 | 98 | 134 | 102.9 |
| 17 | 8,923 | 99 | 139 | 106.7 |
| 18 | 9,282 | 100 | 138 | 110.4 |
| 19 | 9,641 | 100 | 135 | 113.8 |
| 20 | 10,000 | 100 | 133 | 117.1 |
| SSE |  |  | 12233 | 495.98 |
| AIC |  |  | 149.60 | 138.56 |# 7.6 Imperfect Debugging Model with Multiple Failure Types 

In this section, the development of a software reliability model (Pham 1996a) that addresses the problems of multiple failure types and imperfect debugging based on an NHPP, where the fault detection rate is constant, for predicting software performance measures is discussed. The first model considers the fault detection rate is constant, where the second model considers the fault-detection timedependent. The model allows for three different error types, categorized by the severity levels or the difficult of detection. Critical errors (Type 1) are very difficult to detect and remove; major errors (Type 2) are difficult to detect and remove; and minor errors (Type 3) are easy to detect and remove. An example of a critical error would be adding two numbers when they should be subtracted. Major errors are easier to detect than critical errors, but are still hard to detect. An example of a major error is going through a loop one too few, or one too many, times. Minor errors are easy to detect. An example of a minor error is forgetting a comma or semicolon where one is needed.

Notation (used throughout this section)
$a \quad$ Expected number of software errors to be eventually detected
$b_{i} \quad$ Error detection rate per type $i$ error, $i=1,2,3 ; 0<b_{1}<b_{2}<b_{3}<1$
$p_{i} \quad$ Content proportion of type $i$ errors
$\lambda(t) \quad$ Intensity function or error detection rate
$N_{i}(t) \quad$ Cumulative number of type $i$ errors
$n(t) \quad$ Number of errors to be eventually detected plus the number of errors introduced to the program by time $t$
$\beta i \quad$ Type $i$ error introduction rate that satisfies $0 \leq \beta_{i} \leq 1$
$m_{i}(t) \quad$ Expected number of software type $i$ detected errors by time $t$
M Number of parameters in the model
$\wedge \quad$ Maximum likelihood estimate
$\mathrm{m}(\mathrm{t}) \quad$ Expected number of software failures detected by time t
$R(s / t) \quad$ Software reliability function, i.e., the conditional probability of no failure occurring during $(t, t+s)$ given that the last failure occurred at time $t$
$y_{i j} \quad$ Cumulative number of actual type $j$ failures observed at time $t_{i}$
$\hat{m}_{j}\left(t_{i}\right)$ Estimated cumulative number of type $j$ failures at time $t_{i}$ obtained from the fitted mean value function, $i=1,2, \ldots, n$.

The NHPP imperfect debugging model is based on the following assumptions (Pham 1996):

1. When detected errors are removed, it is possible to introduce new errors.
2. The probability of finding an error in a program is proportional to the number of errors remaining in the program.
3. The probability of introducing a new error is constant.
4. Three types of errors exist:

Type I errors (critical): very difficult to detect.
Type 2 errors (major): difficult to detect.
Type 3 errors (minor): easy to detect.5. The parameters $a$ and $b_{i}$ for $i=1,2,3$ are unknown constants.
6. The error detection phenomenon in the software is modeled by an NHPP

# 7.6.1 A Constant Fault Detection Rate 

Assume the error detection rate per type $i$ error $b_{i}$ is constant where $i=1,2,3$; $0<b_{1}<b_{2}<b_{3}<1$.

Theorem 7.7 (Pham 1996a): The mean value function $m(t)$ of the generalized model incorporating imperfect debugging with multiple failure types by solving the following differential equations:

$$
\begin{gathered}
\frac{\partial}{\partial t}\left[m_{i}(t)\right]=b_{i}\left[n_{i}(t)-m_{i}(t)\right] \\
\frac{\partial}{\partial t}\left[n_{i}(t)\right]=\beta_{i} \frac{\partial}{\partial t}\left[m_{i}(t)\right] \\
m(t)=\sum_{i=1}^{3} m_{i}(t) \\
n_{i}(0)=a p_{i} \\
m_{i}(0)=0
\end{gathered}
$$

is given by

$$
m_{i}(t)=\frac{a p_{i}}{\left(1-\beta_{i}\right)}\left[1-e^{-\left(1-\beta_{i}\right) b_{i} t}\right]
$$

The fault detection rate per unit time and the error content function up to time $t$ are, respectively,

$$
\lambda_{i}(t)=a p_{i} b_{i} e^{-\left(1-\beta_{i}\right) b_{i} t}
$$

and

$$
n_{i}(t)=\frac{a p_{i}}{1-\beta_{i}}\left[1-e^{-\left(1-\beta_{i}\right) b_{i} t}\right]
$$

The software reliability function $R(x \mid t)$ is given by

$$
R(x \mid t)=e^{-\left[\sum_{i=1}^{3} \frac{a p_{i}}{\left(1-\beta_{i}\right)}\left(1-e^{-\left(1-\beta_{i}\right) b_{i} t}\right)\left(1-e^{-\left(1-\beta_{i}\right) b_{i} t}\right)\right]}
$$

## Parameter Estimation

The model parameters $a, b_{1}, b_{2}$, and $b_{3}$ are estimated using the MLE method. For Type 1 data (the data on the cumulative number of detected errors), suppose that the data are available in the form of $\left(t_{i}, y_{i j}\right)$, where $y_{i j}$ are the cumulative number of failures type $j$ detected up to time $t_{i}$ for $i=1,2, \ldots, n$, and $j=1,2,3$. Assuming the fault detection process is NHPP, the likelihood function $L\left(a, b_{1}, b_{2}, b_{3}\right)$ for given data $\left(t_{i} y_{i j}\right), i=1,2, \ldots, n$, and $j=1,2,3$ is as follows:$$
\begin{aligned}
L\left(a, b_{1}, b_{2}, b_{3}\right) & =\operatorname{Pr}\left\{\prod_{j=1}^{3}\left(m_{j}(0)=0, m_{j}\left(t_{1}\right)=y_{1, j}, m_{j}\left(t_{2}\right)\right.\right. \\
& \left.\left.=y_{2, j}, \ldots ., m_{j}\left(t_{n}\right)=y_{n, j}\right)\right\} \\
& =\prod_{j=1}^{3} \prod_{i=1}^{n} \frac{\left[m_{j}\left(t_{i}\right)-m_{j}\left(t_{i-1}\right)\right]^{y_{i, j}-y_{i-1, j}}}{\left(y_{i, j}-y_{i-1, j}\right)!} e^{-\left[m_{j}\left(t_{i}\right)-m_{j}\left(t_{i-1}\right)\right]}
\end{aligned}
$$

where

$$
m_{j}\left(t_{i}\right)=\frac{a p_{j}}{\left(1-\beta_{j}\right)}\left[1-e^{-\left(1-\beta_{j}\right) b_{j} t_{i}}\right]
$$

Taking the log likelihood function, we obtain

$$
\begin{aligned}
\ln \left[L\left(a, b_{1}, b_{2}, b_{3}\right)\right] & =\sum_{j=1}^{3} \sum_{i=1}^{n}\left[\left(y_{i, j}-y_{i-1, j}\right) \ln \left[m_{j}\left(t_{i}\right)-m_{j}\left(t_{i-1}\right)\right]\right. \\
& \left.-\ln \left[\left(y_{i, j}-y_{i-1, j}\right)!\right]-\left[m_{j}\left(t_{i}\right)-m_{j}\left(t_{i-1}\right)\right]\right.
\end{aligned}
$$

Taking the partial derivatives of the log likelihood function, $\ln \left[L\left(a, b_{1}, b_{2}, b_{3}\right)\right]$ with respect to the unknown parameters, $a, b_{l}, b_{2}$, and $b_{3}$, and setting them equal to zero, we obtain the following system of equations:

$$
\begin{gathered}
a=\frac{\sum_{j=1}^{3} y_{n j}}{\sum_{j=1}^{3} \frac{p_{j}}{\left(1-\beta_{j}\right)}\left[1-e^{-\left(1-\beta_{j}\right) b_{j} t_{n}}\right]} \\
\sum_{i=1}^{n}\left(y_{i, j}-y_{i-1, j}\right) \frac{(1-\beta)\left[\left(t_{i} e^{-\left(1-\beta_{j}\right) b_{j} t_{i}}-t_{i-1} e^{-\left(1-\beta_{j}\right) b_{j} t_{i-1}}\right)\right.}{\left[e^{-\left(1-\beta_{j}\right) b_{j} t_{i-1}}-e^{-\left(1-\beta_{j}\right) b_{j} t_{i}}\right]} \\
=a p_{j} t_{n} e^{-\left(1-\beta_{j}\right) b_{j} t_{n}}
\end{gathered}
$$

for $j=1,2$, and 3 . Solving the above system of equations (7.28)-(7.29) simultaneously gives the MLE of parameters $a, b_{l}, b_{2}$, and $b_{3}$.

For Type 2 data (the data on failure occurrence times), assume that the data set is available in the form of $n_{1}$ Type 1 errors, $n_{2}$ Type 2 errors, and $\mathrm{n}_{3}$ Type 3 errors, and $S_{1,1} \leq S_{1,2} \leq \ldots \leq S_{1, \mathrm{n} 1}, S_{2,1} \leq \ldots \leq S_{2, \mathrm{n} 2}$, and $S_{3,1} \leq S_{3,2} \leq \ldots \leq S_{3, \mathrm{n} 3}$, where $S_{\mathrm{i}, \mathrm{j}}$ is the actual time that the $j^{\text {th }}$ failure of Type $i$ error occurs. Again, using the MLE method, the likelihood function for the NHPP model in a given data set is as follows:

$$
L\left(a, b_{1}, b_{2}, b_{3}\right)=\prod_{j=1}^{3} \prod_{i=1}^{n} e^{-m_{j}\left(S_{i}\right)} \lambda_{j}\left(S_{j, i}\right)
$$where

$$
S_{r}=\max \left\{S_{1, n 1}, S_{2, n 2}, S_{3, n 3}\right\}
$$

Taking the partial derivatives with respect to the unknown parameters and setting them equal to zero, we obtain the following results:

$$
\begin{gathered}
\sum_{i=1}^{n_{j}} S_{j, i}=\frac{n_{j}-a p_{j} b_{j} S_{r} e^{-\left(1-\beta_{j}\right) b_{j} S_{r}}}{b_{j}\left(1-\beta_{j}\right)} \\
a=\frac{\sum_{j=1}^{3} n_{j}}{\sum_{j=1}^{3} \frac{p_{j}}{\left(1-\beta_{j}\right)}\left[1-e^{-\left(1-\beta_{j}\right) b_{j} S_{r}}\right]}
\end{gathered}
$$

for $j=1,2$, and 3 . Solving equations (7.31) and (7.32) simultaneously gives the MLE of parameters $a, b_{1}, b_{2}$, and $b_{3}$.

Application 7.7: The failure data set \#3 (see Table 4.7) (Misra 1983) consists of three types of errors: critical, major, and minor. The observation time (week, hour) and the number of failures detected per week are presented in Table 4.7 (in Chapter 4). Given

$$
\begin{aligned}
& p_{1}=0.0173 ; p_{2}=0.3420 ; p_{3}=0.6407 \\
& \beta_{1}=0.5 ; \beta_{2}=0.2 ; \beta_{3}=0.05
\end{aligned}
$$

Using the MLE method, the parameters for the reliability model are obtained as follows:

$$
\begin{gathered}
a=428 \\
b_{1}=0.00024275 \\
b_{2}=0.00029322 \\
b_{3}=0.00030495
\end{gathered}
$$

Substituting the known and estimated parameters into the reliability equation, we obtain

$$
R(x \mid t)=e^{-A}
$$

where

$$
\begin{aligned}
A= & 14.81\left(e^{-0.00012138 t}\right)\left(1-e^{-0.00012138 x}\right) \\
& +182.97\left(e^{-0.00023458 t}\right)\left(1-e^{-0.00023458 x}\right) \\
& +288.65\left(e^{-0.0002897 t}\right)\left(1-e^{-0.0002897 x}\right)
\end{aligned}
$$

Other reliability performance measures are given by

$$
\begin{aligned}
& m_{1}(T)=14.81\left(1-e^{-0.00012138 T}\right), \quad n_{1}(T)=14.81\left(1-0.5 e^{-0.00012138 T}\right) \\
& m_{2}(T)=182.97\left(1-e^{-0.00023458 T}\right), \quad n_{2}(T)=182.97\left(1-0.2 e^{-0.00023458 T}\right) \\
& m_{3}(T)=288.65\left(1-e^{-0.0002897 T}\right), \quad n_{3}(T)=288.65\left(1-0.05 e^{-0.0002897 T}\right)
\end{aligned}
$$# 7.6.2 Fault Detection Time-dependent Rate 

Pham and Deng (2003a) extended the imperfect debugging model in Theorem 7.7 by considering the time-dependent fault detection rate function, instead of a constant rate.

Let $\mathrm{b}_{\mathrm{i}}(t)$ be the time-dependent Type i fault detection rate per unit time, $\mathrm{i}=1,2,3$; $0<\mathrm{b}_{\mathrm{i}}<1$. Assume the function $\mathrm{b}_{\mathrm{i}}(t)$ is a non-decreasing S -shape curve which can capture the learning process of the software testers corresponding to Type $i$ faults, which is given as follows:

$$
b_{i}(t)=\frac{b_{i}}{1+\theta_{i} e^{-b_{i} t}}
$$

Assume the error detection rate per type $i$ error $b_{i}$ is constant where $i=1,2,3 ; 0<$ $b_{1}<b_{2}<b_{3}<1$.

Theorem 7.8 (Pham and Chao 2003a): The mean value function $m(t)$ of the generalized model incorporating imperfect debugging and time-dependent fault detection rate with multiple failure types by solving the differential equations:

$$
\begin{gathered}
\frac{\partial}{\partial t}\left[m_{i}(t)\right]=b_{i}(t)\left[n_{i}(t)-m_{i}(t)\right] \\
\frac{\partial}{\partial t}\left[n_{i}(t)\right]=\beta_{i} \frac{\partial}{\partial t}\left[m_{i}(t)\right] \\
m(t)=\sum_{i=1}^{3} m_{i}(t) \\
n_{i}(0)=a p_{i} \\
m_{i}(0)=0
\end{gathered}
$$

where

$$
b_{i}(t)=\frac{b_{i}}{1+\theta_{i} e^{-b_{i} t}}
$$

is given by:

$$
m_{i}(t)=\left(\frac{a p_{i}}{1-\beta_{i}}\right)\left[1-\left(\frac{1+\theta_{i}}{\theta_{i}+e^{b_{i} t}}\right)^{1-\beta_{i}}\right]
$$

The proof can be obtained in Pham and Chao (2003a).
The software reliability function is given by

$$
R(s / t)=e^{-\sum_{i=1}^{3}\left(\frac{a p_{i}}{1-\beta_{i}}\right)\left[\left(\frac{1+\theta_{i}}{\theta_{i}+e^{b_{i} t}}\right)^{1-\beta_{i}}-\left(\frac{1+\theta_{i}}{\theta_{i}+e^{\beta_{i}(t+\tau)}}\right)^{1-\beta_{i}}\right]}
$$When $\theta_{i}=0$ from equation (7.36), the mean value function becomes

$$
m(t)=\sum_{i=1}^{3}\left(\frac{a p_{i}}{1-\beta_{i}}\right)\left[1-\left(e^{-b_{i} t\left(1-\beta_{i}\right)}\right)\right]
$$

which is the same as equation (7.25).

# Parameter Estimation 

The model parameters $a, b_{\mathrm{i}}, \beta_{i}$, and $\theta_{i}$ are estimated using the MLE method. The form of the likelihood function depends on the form of the data being used to estimate the parameters. The first data set type gives the cumulative number of failures up to a given time. The second data set type gives the actual time that each failure occurs. In this section, we only discuss the first type of data set. The discussion of the second type of data set can be obtained in Section 7.6.1.

Assume that the data are available in the form of $\left(t_{\mathrm{i}}, y_{\mathrm{ij}}\right)$, where $y_{\mathrm{ij}}$ are the cumulative number of Type $j$ errors detected up to time $t_{\mathrm{i}}$ for $i=1,2, \ldots, \mathrm{n}$ and $j=$ $1,2, \ldots, k$. The likelihood function for estimating the model parameters can be expressed as follows:

$$
\begin{aligned}
L(\Omega, t)= & P\left\{\prod_{j=1}^{k}\left[m_{l}(0)=0, m_{l}\left(t_{1}\right)=y_{1, j}, m_{l}\left(t_{2}\right)=y_{2, j}, \ldots, m_{l}\left(t_{n}\right)=y_{n, j}\right]\right\} \\
& =\prod_{j=1}^{k} \prod_{i=1}^{n} \frac{\left[m_{l}\left(t_{i}\right)-m_{l}\left(t_{i-1}\right)\right]^{\left(y_{i, j}-y_{i-1, j}\right)}}{\left(y_{i, j}-y_{i-1, j}\right)!} e^{-\left[m j\left(t_{i}\right)-m j\left(t_{i-1}\right)\right]}
\end{aligned}
$$

where $\Omega$ is a vector of unknown parameters $\left(a, b_{\mathrm{i}}, \beta_{i}, \theta_{\mathrm{i}}\right)$ and $m_{\mathrm{j}}(\mathrm{t})$ is given in equation (7.36) for $j=1,2, \ldots, k$.

The logarithm of the likelihood function is given by

$$
\begin{aligned}
\ln [L(\Omega, t)]=\sum_{j=1}^{k} & \sum_{i=1}^{n}\left\{\left(y_{i, j}-y_{i-1, j}\right) \ln \left[m_{l}\left(t_{i, j}\right)-m_{l}\left(t_{i-1}\right)\right]-\right. \\
& \left.\ln \left[\left(y_{i, j}-y_{i-1, j}\right)!\right]-\left[m_{l}\left(t_{i}\right)-m_{l}\left(t_{i-1}\right)\right]\right\}
\end{aligned}
$$

A system of differential equations can be constructed by taking the derivatives of the log likelihood function (see equation 7.38) with respect to each unknown parameter and setting them equal to zero. The estimated parameters $a, b_{\mathrm{i}}, \beta_{i}$, and $\theta_{i}$ can be obtained by solving such equations.

We now implement the model in this Section that incorporates the time-dependent fault detection rate with multiple failure types and also with the model in Section 7.6.1, on two data-sets (Applications 7.8 and 7.9 below) collected from real software development projects. The procedure is:

1. Fit each model to the data; estimate the model parameters and obtain the mean value functions and the reliability functions.
2. Compare the models with each other within a data set using the PRR, MSE, and AIC criteria.3. All of the data points are used to fit the models and estimate the parameters.

Application 7.8. On-line Communication System (OCS): The On-line Communication System (OCS) project at ABC Software Company was completed in 2000. The data (data set \#2 in Chapter 4) was collected over a period of 12 weeks during which time the testing started and stopped many times and is given in Table 4.6. Errors detection is broken down into sub-categories to help the development and testing team to sort and solve the most critical Modification Requests (MRs) first. These sub-categories are referred to as the severity level depending on the nature of the problem with 1 being the most severe problem, with 2 being the major problem and 3 being a minor problem.

The data set, maps into week, consists of three types of errors: severe 1, severe 2 , and severe 3 . The observation time (week) and the number of errors detected per week are presented in Table 4.6. The cumulative number of errors observed at time t (in week) is shown in Figure 7.8.

Given the values of content proportion of errors type: $p_{1}=0.18, p_{2}=0.40$, and $p_{3}=0.42$. The maximum likelihood estimates of the NHPP model in equation (7.25) (see Pham 1996a), called Model 1, and the imperfect debugging NHPP model in equation (7.36) (also Pham 2003a), called Model 2, are given in Table 7.10 .

Table 7.11 summarizes the PRR, MSE, and AIC values for Model 1 and Model 2. Table 7.11 shows that for Model 2:

MSE $=7.78$, which is much smaller than for Model 1
AIC $=194.4$ which is smaller than Model 1
PRR $=0.86$, which is appreciably smaller than Model 1
From the results, the NHPP imperfect debugging model (Model 2) indicates that the complexity of the model by incorporating the time-dependent fault detection rate with the learning phenomenon is worth the effort since it models a more realistic set of actual effects. However, further work in broader validation of this remark is needed using other data sets.

Figure 7.8. Mean value function of model and actual error data

Table 7.10. Parameter estimation

| Mod | $a$ | $b_{1}$ | $b_{2}$ | $b_{3}$ | $\beta_{1}$ | $\beta_{2}$ | $\beta_{3}$ | $\theta_{1}$ | $\theta_{2}$ | $\theta_{3}$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 157 | 0.083 | 0.089 | 0.076 | 0.5 | 0.3 | 0.00005 |  |  |  |
| 2 | 144 | 0.289 | 0.321 | 0.33 | 0.1 | 0.1 | 0.056 | 0.257 | 0.23 | 0.01 |

Table 7.11. Comparison of models for OCS data set

| Model | PRR | MSE | AIC |
| :--: | :--: | :--: | :--: |
| Model 1 | 1.57 | 34.64 | 209.36 |
| Model 2 | 0.86 | 7.78 | 194.40 |

Application 7.9. Software Failure Data: In this section the failure data set \#3 (see Table 4.7) (Misra, 1983) are used to illustrate further the new NHPP imperfect debugging and time-dependent fault detection rate model. The data sets consist of three types of errors: critical, major, and minor. Given the values of content proportion of errors type: $p_{1}=0.02, p_{2}=0.34$, and $p_{3}=0.64$. The maximum likelihood estimates of the NHPP model in equation (7.25) and the imperfect debugging model in equation (7.36) are given in Table 7.12. Table 7.13 summarizes the PRR, MSE, and AIC values for Model 1 and Model 2. It shows that for Model 2:MSE $=9.34$, which is much smaller than for Model 1
AIC $=331.3$ which is smaller than Model 1
PRR $=1.42$, which is appreciably smaller than Model 1
The NHPP imperfect debugging model (Model 2) again indicates that the complexity of the model by incorporating the time-dependent fault detection rate is worth the effort to study. Further work in broader validation of this conclusion is needed using other application data sets.

Table 7.12. Results of parameter estimation

| Mo | $a$ | $b_{1}$ | $b_{2}$ | $b_{3}$ | $\beta_{1}$ | $\beta_{2}$ | $\beta_{3}$ | $\theta_{1}$ | $\theta_{2}$ | $\theta_{3}$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 240 | 0.015 | 0.026 | 0.032 | 0.8 | 0.6 | 0.75 |  |  |  |
| 2 | 239 | 0.02 | 0.032 | 0.013 | 0.9 | $10^{-4}$ | 0.546 | 0.43 | 0.273 | $10^{-6}$ |

Table 7.13. Comparison of models

| Model | PRR | MSE | AIC |
| :-- | :--: | :--: | :--: |
| Model 1 | 1.91 | 16.34 | 352.6 |
| Model 2 | 1.42 | 9.34 | 331.3 |

# 7.7 Further Reading 

Some interesting research papers on testing coverage and removal are:
X. Zhang, X. Teng and H. Pham, "Considering Fault Removal Efficiency in Software Reliability Assessment", IEEE Trans. on Systems, Man, and Cybernetics - Part A, vol. 33, no.1, 2003, p. 114-120
H. Pham and X. Zhang, "NHPP Software Reliability and Cost Models with Testing Coverage", European Journal of Operational Research, vol. 145, 2003, p. 443-454

### 7.8 Problems

1. Show that the solution of equation (7.7) in Theorem 7.3 is given by

$$
m(t)=e^{-B(t)}\left[m_{0}+\int_{t_{0}}^{t} a e^{B(\tau)} g(\tau) d \tau\right]
$$where $B(t)=\int_{t_{0}}^{t} g(\tau) d \tau$ and $m\left(t_{0}\right)=m_{0}$
2. Show that, if the functions $c(\mathrm{t})$ and $d(\mathrm{t})$ are given in equations (7.9) and (7.10), then the function $m(\mathrm{t})$ is given by

$$
m(t)=a-a e^{-b t}\left[1+(b+d) t+b d t^{2}\right]
$$# Software Reliability Models with Environmental Factors 

### 8.1 Introduction

Modern society relies heavily on the correct operation of software in various forms. From the users' point of view, software plays an important role in systems of both safety-critical and civil applications. High-quality software of such systems is desirable and even critical. From the developers' point of view, the pressure of delivering high-quality software on time and within budget requires further research on software reliability assessment. Many software reliability models studied in the last three decades often excluded information on the software development process. In other words, the software reliability is assessed based on the software failure data without taking the software development environment into consideration. This chapter discusses the environmental factors involved in the whole software development process and the impacts of these factors on software reliability assessment. We also discuss several software reliability models that incorporate environmental factors.

### 8.2 Data Analysis

This section presents a recent survey on software environmental factors consisting of 32 factors based on the studies by Pham and Zhang (1998a) and Zhang and Pham (2000a), and Zhang et al. (2001a). The information about the background of survey participants are considered. The survey form with a brief definition of each of the 32 factors is included in Appendix 3. The basic question Pham and Xuemei (1998a) wanted to study was to determine the factors that profile the software development processes and have significant impact on software reliability?

Analyses of the survey information of the software development process are discussed. Also described is the identification of key factors for software development teams to consider in their software development practice as well as theunderstanding of the elements in software development process that may affect software reliability.

# 8.2.1 Survey Analysis 

The survey has two complementary sections (see Appendix 3). Section A data were collected using a formal survey questionnaire given directly by the software developers or managers in 13 organizations. The general information of the survey participants is shown in Table 8.1. The data were collected from March to May 1998. Demographic data on the participants is summarized in Table 8.2. Thirteen companies were chosen to maximize sample breadth for a mostly exploratory study, yet they have sufficient technical and managerial depth to provide reliable data. All organizations had software development projects either for safety-critical, commercial, or inside-user orientated applications. They had a relatively good mixture of software development experience, were diverse in size, program categories, and represented a good mixture of software development firms.

Section A of the survey used a Likert scale to identify the degree to which an increase of significance in each environmental factor (the independent variables) which typically makes software reliability assessment more accurate. In the survey form, 1 indicated "not significant" and 7 "most significant". If these factors are irrelevant, scores of (or close to) 1 would be expected; if they do have a significant effect on software reliability assessment, mean scores would be statistically different from 1 (not significant). Similarly, factors with high scores could be deemed as having a greater impact than those with lower scores for comparative purposes. Finally, all the factors will be listed in order with the most significant at the top.

Section B in Appendix 3 sought personal and organizational professional data to explore possible relationships with the ranking of environmental factors. Some background data of the survey participants and the categories of the software application were collected. Information of software development effort allocation was also obtained. See Zhang and Pham (2000a) for detailed information.

Based on the survey information, the analysis, design, coding, and testing phases take, respectively, about $25,18,36$, and $21 \%$ of the development efforts. Analysis and design testing phases together take about $64 \%$ of the total development time. People in different positions are found to have different opinions (Table 8.3). The significance of incorporating the factors into software reliability studies averages at $75 \%$, ranging from $80 \%$ of the programmers, testers, and managers to $63 \%$ by other people. The distribution of the survey participants is also shown. For example, 9 out of 22 people are programmers, 4 are system engineers and so on.Table 8.1. General information of survey participants

| Company name | Number of participants |
| :-- | :-- |
| MCI International Inc. | 1 |
| Lucent Technologies | 2 |
| General Electronics Capital | 1 |
| Peracom | 1 |
| IBM | 1 |
| Bellcore | 6 |
| AT \&T | 1 |
| NEC | 1 |
| Chrysler | 5 |
| Hughes Network System Inc. | 1 |
| Level 1 | 1 |
| BOC Gas | 1 |
| Texas Instruments | 1 |
| Total | 23 |

Table 8.2. Demographic data of survey participants

| Personal/demographic factor | Mean score | Sample <br> size |
| :-- | :-- | :-- |
| 1. Current job position | Manager: $9.09 \%$ |  |
|  | System engineer: $18.2 \%$ |  |
|  | Programmer: $40.9 \%$ |  |
|  | Tester: $4.55 \%$ |  |
|  | Other: $27.27 \%$ |  |
| 2. Experience (years) | 7.79 | 22 |
| 3. Significance of improvement | $72.17 \%$ | 23 |
| 4. Percentage of reused code | $36.38 \%$ | 18 |
| 5. Percentage of time spend in analysis | $25.28 \%$ | 18 |
| 6. Percentage of time spend in design | $18.06 \%$ | 18 |
| 7. Percentage of time spend in coding | $35.83 \%$ | 18 |
| 8. Percentage of time spend in testing | $20.83 \%$ | 18 |Table 8.3. Summary by position

| $\operatorname{manager}(2 / 22)$ |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| analysis | 30 | 25 |  |  |  |  |  |  |  |  |
| design | 20 | 5 |  |  |  |  |  |  |  |  |
| coding | 30 | 45 |  |  |  |  |  |  |  |  |
| testing | 20 | 25 |  |  |  |  |  |  |  |  |
| reused | 10 | 20 |  |  |  |  |  |  |  |  |
| sig | 80 | 80 |  |  |  |  |  |  |  |  |
| programmer(9/22) |  |  |  |  |  |  |  |  |  |  |
| analysis | 10 | 10 | 25 | 30 | 40 | 20 | 50 | 30 | 0 |  |
| design | 10 | 30 | 25 | 20 | 10 | 30 | 10 | 20 | 0 |  |
| coding | 50 | 30 | 25 | 30 | 30 | 20 | 30 | 20 | 0 |  |
| testing | 30 | 30 | 25 | 20 | 20 | 30 | 10 | 30 | 0 |  |
| reused | 60 | 50 | 40 | 40 | 5 | 0 | 0 | 30 | 80 |  |
| sig | 80 | 60 | 80 | 60 | 60 | 80 | 80 | 60 | 100 |  |

system engineer(4/22)

| analysis | 25 | 20 | 10 | 75 |
| :-- | :-- | :-- | :-- | :-- |
| design | 30 | 20 | 20 | 5 |
| coding | 35 | 40 | 60 | 10 |
| testing | 10 | 20 | 10 | 10 |
| reused | 35 | 50 | 60 | 20 |
| sig | 60 | 80 | 60 | 80 |

tester(1/22)

| analysis | 25 |
| :-- | :-- |
| design | 20 |
| coding | 30 |
| testing | 25 |
| reused | 5 |
| sig | 80 |

other(6/22)

| analysis | 20 | 5 | 0 | 5 |
| :-- | :-- | :-- | :-- | :-- |
| design | 20 | 10 | 0 | 20 |
| coding | 30 | 70 | 0 | 60 |
| testing | 30 | 15 | 0 | 15 |
| reused | 20 | 40 | 30 | 60 |
| sig | 80 | 100 | 40 | 60 |



Note: legend 1:analysis, 2:design, 3:coding, 4:testing# 8.2.2 Statistical Methods 

## Relative Weight Method

This is simply ranking and determining the relative weights of factors based solely on the participants' opinions as reflected in Section A of the survey forms. Under this methodology, every participant is treated equally without considering his/her background information.

Let $r_{i j}$ be the original ranking of the $i$ th factor on the $j$ th survey and $w_{i j}$ the corresponding normalized score as follows:

$$
w_{i j}=\frac{r_{i j}}{\sum_{i=1}^{n} r_{i j}}
$$

where $n$ is the number of factors on the $j$ th survey. Therefore $\sum_{i=1}^{n} w_{i j}=1$ for all $j$.
Different people may give different original ranking and some of them may give higher scores for all factors. Therefore, the summation of all the scores from $f 1$ to $f 32$ ranges from 117 to 200 . By normalizing the original ranking scores using equation (8.1), the final weight for the $i$ th factor can be written as

$$
w_{i}^{*}=\frac{\sum_{j=1}^{l} w_{i j}}{l}
$$

where $l$ is the number of surveys used in this method.

## Analysis of Variance Method

Analysis of variance (ANOVA) model is a very versatile statistical tool for studying the relationship between a dependent variable and one or more independent variables. The response in the model is named dependent variable because its value depends on other variables, and explanatory variables are named independent variables since their values are not influenced by anything else.

A factor in ANOVA is an independent variable to be studied in the model. A level is a factor is a particular form or value of that factor. The primary purpose of ANOVA is to determine the effects of factors on the response and to single out the most significant factors.

## One-way ANOVA Model

$$
r_{i j}=\mu_{0}+\alpha_{i}+\varepsilon_{i j}
$$

where
$\mathrm{r}_{\mathrm{ij}} \quad$ is the original or observed response value
$\mu_{0}$ is a constant or intercept term in the model, the mean of all the cells
$\alpha_{i}$ is the main effect for a factor, say A , at the $i$ th level
$\varepsilon_{\text {ij }}$ is the random error term, which follows normal distribution with mean 0Using one-way ANOVA, we can perform the hypothesis tests to classify all factors into different groups according to the significance of their impact on the software reliability analysis.

# Two-way ANOVA Model 

$$
r_{i j k}=\mu_{0}+\alpha_{i}+\beta_{j}+\left(\alpha^{*} \beta\right)_{i j}+\varepsilon_{i j k}
$$

where
$\mathrm{r}_{\mathrm{i}} \quad$ is the original or observed response value
$\mu_{0} \quad$ is a constant or intercept term in the model, the mean of all the cells
$\alpha_{\mathrm{i}} \quad$ is the main effect for a factor, say A , at the $i$ th level
$\beta_{j} \quad$ is the main effect for a factor, say B , at the $j$ th level
$\left(\alpha^{*} \beta\right)_{i j}$ is the interaction term of A and B at the $i j$ th level
$\varepsilon_{\text {ij }} \quad$ is the random error term
One-way ANOVA can be used to rank the weights of the factors and select the most important ones. Like relative weight method, one-way ANOVA treats the original ranking from the survey equally. Therefore, these two methods may have some bias in the analysis. The two-way ANOVA can be used to overcome this weakness.

Two-way ANOVA can be used to get rid of survey bias and adjust the mean ranking score of significance for each environmental factor. People who have different experience of software development may not have same opinions on the significance of the environmental factors. The background factors then can be the title, the experience and so on. These can be the factors of two-way ANOVA analysis, and each can have several levels. Also interaction between these influence factors can also be tested. After these analyses, the information can be used to adjust the mean ranking score for each environmental factor. Based on this information, further analyses can be conducted on the treatments of the survey data. The disadvantage of this model is its complexity. The model validations such as normality and independence can be obtained in Zhang and Pham (2000a).

Based on the information obtained from the survey data, Zhang and Pham (2000a) studied a number of hypotheses as follows:
Hypothesis 1: The significance of the impacts of the 32 factors on software reliability assessment is of the same level. Intuitively, the impacts of the 32 factors may not be the same. Some may have more significant impacts than others; then the ranking of these factors in terms of their impacts on software reliability assessment will be desirable.
Hypothesis 2: People playing different roles in software development have the same opinion on the significance of the 32 factors. Managers, system engineers, programmers, and testers may not have the same opinion on the significance of all these factors. This hypothesis will find out whether their opinion can be considered as "the same".Hypothesis 3: People developing software for different applications have the same opinion on the importance of the 32 factors. Safety-critical, commercial and insideused systems are considered here.

# 8.3 Exploratory Analysis of Environmental Factors 

## Relative Weight Method

Table 8.4 shows the results by the relative weight method. The ten most important environmental factors are classified as factors in the analysis phase (three factors), coding (one factor), testing (four factors), and general (two factors). The column "Normalized priorities" gives the contribution of each environmental factor. For example, program complexity factor contributes approximately $3.7 \%$ (its relative weight $=0.03768$ ). A higher priority value indicates a higher ranking. The application of this finding in Table 8.4 is not to discard the environmental factors belonging to lower ranking classes, but hopefully, to help software developers or managers prioritize their tasks.

## ANOVA

ANOVA method was performed on each quantitative survey variable including all environmental factors and mean and variance of these factors are calculated. The final ranking based on this information listed in Table 8.5. It seems that the final ranking of the environmental factors is consistent with the one we got from relative weight method. For example, the top 10 factors remain the same except that factor \# 8 (frequency of specification change) ranks two positions down.

ANOVA method also classified the factors into several groups in terms of their importance. The first five factors are the first class, which is the most important factors, the next five factors belong to the second group and so on. This finding can be used to help software developers to determine which are the most important groups of environmental factors subject to the available resources.

## Correlation Analysis

Correlation analysis is also studied based on the survey information. The purpose is to find out the correlation of environmental factors and determine if they are independent or not. (If not, then which factors are related to each other?) Table 8.6 shows the correlation of the environmental factors. Correlation analysis aims at finding out the correlation among the factors. In other words, to find out whether the factors are independent or not. If not, which factors are related to each other? In this section, we present the result obtained from a correlation test of the factors.

For example, Factor 1 (program complexity) is statistical significantly correlated with Factor 17 (development team size). For those correlated factors, we may not want to include all of them in the software reliability models provided that one has been considered. This is because by considering one of these related factors we already take the contributions of these factors into consideration. Including the correlated ones will not make much additional contribution but just increase the complexity of the model.Table 8.4. Results ranking based on relative weight method

| Rank | Rank <br> factors | Factor name | Normalized <br> priorities |
| :--: | :--: | :-- | :--: |
| 1 | f1 | Program complexity | 0.03768 |
| 2 | f15 | Programmer skills | 0.03693 |
| 3 | f25 | Testing coverage | 0.03675 |
| 4 | f22 | Testing effort | 0.03650 |
| 5 | f21 | Testing environment | 0.03533 |
| 6 | f8 | Frequency of specification change | 0.03483 |
| 7 | f24 | Testing methodologies | 0.03433 |
| 8 | f11 | Requirements analysis | 0.03417 |
| 9 | f6 | Percentage of reused code | 0.03369 |
| 10 | f12 | Relationship of detailed design, requirement | 0.03330 |
| 11 | f5 | Level of programming technologies | 0.03315 |
| 12 | f27 | Documentation | 0.03281 |
| 13 | f18 | Program workload | 0.03275 |
| 14 | f26 | Testing tools | 0.03227 |
| 15 | f16 | Programmer organization | 0.03210 |
| 16 | f19 | Domain knowledge | 0.03180 |
| 17 | f3 | Difficulty of programming | 0.03171 |
| 18 | f10 | Design methodologies | 0.03171 |
| 19 | f20 | Human nature (mistake and omission) | 0.03169 |
| 20 | f14 | Development management | 0.03166 |
| 21 | f23 | Testing resource allocation | 0.03096 |
| 22 | f4 | Amount of programming effort | 0.03072 |
| 23 | f2 | Program categories | 0.03058 |
| 24 | f13 | Work standards | 0.02985 |
| 25 | f32 | System software | 0.02839 |
| 26 | f9 | Volume of program design documents | 0.02750 |
| 27 | f17 | Development team size | 0.02738 |
| 28 | f7 | Programming language | 0.02711 |
| 29 | f28 | Processor | 0.02414 |
| 30 | f31 | Telecommunication device | 0.02404 |
| 31 | f30 | Input/output device | 0.02291 |
| 32 | f29 | Storage device | 0.02127 |Table 8.5. Final ranking based on ANOVA method

| SNK grouping |  |  | Mean | N | Factor <br> no. | Factor name | Final <br> grouping |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | A |  | 6.0435 | 23 | f1 | Program complexity | 1 |
|  | A |  | 6.0000 | 23 | f15 | Programmer skills | 1 |
|  | A |  | 5.9565 | 23 | f25 | Testing coverage | 1 |
|  | A |  | 5.9565 | 23 | f22 | Testing effort | 1 |
|  | A |  | 5.7826 | 23 | f21 | Testing environment | 1 |
| B | A |  | 5.6087 | 23 | f24 | Testing methodologies | 2 |
| B | A |  | 5.6087 | 23 | f11 | Requirements analysis | 2 |
| B | A |  | 5.6087 | 23 | f8 | Frequency of spec change | 2 |
| B | A |  | 5.5652 | 23 | f6 | Percentage of reused code | 2 |
| B | A |  | 5.5000 | 22 | f18 | Program work load | 2 |
| B | A | C | 5.4762 | 23 | f12 | Relationship of detailed <br> design and requirement | 3 |
| B | A | C | 5.4348 | 23 | f5 | Level of programming <br> technologies | 3 |
| B | A | C | 5.3913 | 23 | f27 | Documentation | 3 |
| B | A | C | 5.3636 | 22 | f26 | Testing tools | 3 |
| B | A | C | 5.2727 | 22 | f19 | Domain knowledge | 3 |
| B | A | C | 5.2174 | 23 | f23 | Difficulty of programming | 3 |
| B | A | C | 5.1905 | 21 | f23 | Testing resource allocation | 3 |
| B | A | C | 5.1739 | 23 | f10 | Design methodologies | 3 |
| B | A | C | 5.1739 | 23 | f16 | Programmer organization | 3 |
| B | A | C | 5.1364 | 22 | f14 | Development management | 3 |
| B | A | C | 5.1304 | 23 | f20 | Human nature (mistake and <br> omission | 3 |
| B | A | C | 5.0909 | 22 | f4 | Amount of programming <br> effort | 3 |
| B | A | C | 5.0000 | 23 | f2 | Program categories | 3 |
| B | A | C | 5.0000 | 20 | f13 | Work ttandards | 3 |
| B | A | C | 4.7727 | 22 | f32 | System software | 4 |
| B | A | C | 4.4783 | 23 | f7 | Programming language | 4 |
| B | A | C | 4.4348 | 23 | f17 | Development team size | 4 |
| B | A | C | 4.4286 | 21 | f9 | Volume of program design <br> documents | 4 |
| B | C |  | 4.0909 | 22 | f28 | Processor | 5 |
| B | C | C | 4.0455 | 22 | f31 | Telecommunication device | 5 |
|  |  | C | 3.90916 | 22 | f30 | Input / output device | 6 |
|  |  |  | 3.5455 | 22 | f29 | Storage device | 7 |# 8.4 Further Exploratory Analysis 

This section considers those 11 top factors in Table 8.4 by looking at ways how to combine those related factors so that the dimension of the factor can be reduced without losing much information (Zhang et al. 2001a). Table 8.7 presents a list of the top 11 ranking environmental factors.

A factor analysis method is used to find the explanation of relationships among the EFs to derive a small number of linear combinations of EFs that retain as much of the information in the original EFs as possible. This linear combination of EFs will be called 'common factor' to avoid confusion with environmental factors and it will be used in place of the original EFs for regression analysis later. Suppose the environmental factors can be grouped by their correlation; then the factors that belong to the same group are highly correlated among themselves but have relatively small correlation with factors in a different group.

## Factor Analysis

The factor analysis based on those 11 EFs is discussed. The eigenvalues of the correlation, the proportion of variation represented, and the cumulative proportions of variation are summarized in Table 8.8. It shows that the common factors (denoted by $\mathrm{C}_{\mathrm{i}} \mathrm{s}$ ) and the first four factors, $\mathrm{C}_{1}$ through $\mathrm{C}_{4}$, have eigenvalues greater than 1 and a drop below $10 \%$ of the variance explained after the $\mathrm{C}_{4}$. Therefore, four common factors are retained.

To figure out the characteristic of the common factors we chose the EFs with factor loading greater than 0.6 in absolute value and listed them in Table 8.9. Factor loadings describe the correlation between the common factors emerging from a factor analysis and the original EFs used in the construction of the factors. The higher the factor loading for a given EF, the more that the EF contributes to the factor score. Note that the first common factor, $\mathrm{C}_{1}$, has high loadings which exceed 0.6 for f5, f12, f21 and f22. Since it is difficult to pin a specific label on the first common factor we call it the 'Overall' factor. In many cases, the first common factor represents an overall measure of the information contained in all the variables. The first common factor explains $32.58 \%$ (Table 8.8) of the total variation. f6, f24, and f25 have large loadings on the second common factor, $\mathrm{C}_{2}$. These EFs related to the index of testing efficiency. Therefore, the second common factor is called the 'Testing Efficiency' factor. Similarly, we call the third and fourth common factors the 'Requirement and Specification' factor and 'Program and Skill' factor, respectively.Table 8.6. Correlation of environmental factors

| Factor no. | Name of factor | Correlated factors |
| :--: | :--: | :--: |
| f1 | Program complexity | f 17 Development team size |
| f15 | Programmer skills | f 3 Difficulty of programming f 18 Program workload |
| f25 | Testing coverage | f 2 Program categories f 24 Testing methodologies |
| f22 | Testing effort | f 5 Level of programming technologies f 13 Work standards f 14 Development management f 21 Testing environment |
| f21 | Testing environment | f 5 Level of programming technologies f 12 Relationship of detailed design and requirement f 13 Work standards f 22 Testing effort |
| f8 | Frequency of specification change |  |
| f24 | Testing methodologies | f 25 Testing coverage f 26 Testing tools |
| f11 | Requirements analysis | f 12 Relationship of detailed design and requirement f 30 Input/output device f 32 System software |
| f6 | Percentage of reused code | f 7 Programming language f 9 Volume of program design documents f 14 Development management f 18 Program workload f 23 Testing resource allocation f 24 Testing methodologies f 26 Testing tools f 27 Documentation |
| f12 | Relationship of detailed design and requirement | f 11 Requirements analysis f 21 Testing environment |
| f5 | Level of programming technologies | f 21 Testing environment f 22 Testing effort |
| f27 | Documentation | f 6 Percentage of reused code f 26 Testing tools f 31 Telecommunication device |
| f18 | Program workload | f 3 Difficulty of programming f 4 Amount of programming effort f 7 Programming language f 13 Work standards f 15 Programmer skills f 23 Testing resource allocation f 26 Testing tools f 30 Input/output device |Table 8.6. (continued)

| Factor no. | Name of factor | Correlated factors |
| :--: | :--: | :--: |
| f26 | Testing tools | f 6 Percentage of reused code <br> f 18 Program workload <br> f 27 Documentation |
| f16 | Programmer organization |  |
| f19 | Domain knowledge |  |
| f3 | Difficulty of programming | f 6 Percentage of reused code <br> f 15 Programmer skills <br> f 18 Program workload |
| f10 | Design methodologies | f 2 Program categories |
| f20 | Human nature (mistake and omission) |  |
| f14 | Development management | f 22 Testing effort |
| f23 | Testing resource allocation | f 6 Percentage of reused code <br> f 24 Testing methodologies |
| f4 | Amount of programming effort | f 6 Percentage of reused code <br> f 7 Programming language <br> f 18 Program workload |
| f2 | Program categories | f 10 Design methodologies <br> f 25 Testing coverage |
| f13 | Work standards | f 14 Development management <br> f 18 Program workload <br> f 21 Testing environment <br> f 22 Testing effort |
| f32 | System software | f 11 Requirements analysis <br> f 28 Processor <br> f 30 Input/output device <br> f31 Telecommunication device |
| f9 | Volume of program design documents | f 6 Percentage of reused code |
| f17 | Development team size | f 1 Program complexity <br> f 18 Program workload |
| f7 | Programming language | f 4 Amount of pro. effort <br> f 6 Percentage of reused code <br> f 18 Program workload |
| f28 | Processor | f 29 Storage device <br> f 31 Telecom. device |
| f31 | Telecommunication device | f 27 Documentation <br> f 28 Processor <br> f 32 System software |
| f30 | Input/output device | f 28 Processor |
| f29 | Storage device | f 30 Input/output device |Table 8.7. Top 11 ranking EFs based on relative weight method

| Rank | EF | Name |
| :--: | :--: | :-- |
| 1 | f 1 | Program complexity |
| 2 | f 15 | Programmer skills |
| 3 | f 25 | Testing coverage |
| 4 | f 22 | Testing effort |
| 5 | f 21 | Testing environment |
| 6 | f 8 | Frequency of specification change |
| 7 | f 24 | Testing methodologies |
| 8 | f 11 | Requirements analysis |
| 9 | f 6 | Percentage of reused code |
| 10 | f 12 | Relationship of detailed design and requirement |
| 11 | f 5 | Level of programming technologies |

Table 8.8. Eigenvalue of the correlation matrix

| Common <br> factor | Eigenvalue | Percentage | Cumulative <br> percentage |
| :--: | :--: | :--: | :--: |
| $\mathrm{C}_{1}$ | 3.5836 | 32.58 | 32.58 |
| $\mathrm{C}_{2}$ | 1.7940 | 16.31 | 48.89 |
| $\mathrm{C}_{3}$ | 1.5753 | 14.32 | 63.21 |
| $\mathrm{C}_{4}$ | 1.3039 | 11.85 | 75.06 |
| $\mathrm{C}_{5}$ | 0.8316 | 7.56 | 82.62 |
| $\mathrm{C}_{6}$ | 0.7020 | 6.38 | 89.00 |
| $\mathrm{C}_{7}$ | 0.4288 | 3.90 | 92.90 |
| $\mathrm{C}_{8}$ | 0.3616 | 3.29 | 96.19 |
| $\mathrm{C}_{9}$ | 0.2622 | 2.38 | 98.57 |
| $\mathrm{C}_{10}$ | 0.1120 | 1.02 | 99.59 |
| $\mathrm{C}_{11}$ | 0.0450 | 0.41 | 100.00 |

# Regression Analysis 

In this section, we examine the relationships between the four common factors and the software reliability assessment improvement based on multiple linear regression. The weighted linear combinations of Efs ( $\mathrm{X}_{i}: i=1, \ldots, 4$ ) for each index and the improvement of the accuracy of software reliability assessment (IASRA) (Section B of the survey form in Zhang and Pham 2000a) are considered as independent variables and dependent variable, respectively.

Let $k_{i j}$ be the $j$ th loading on the $i$ th index and $l_{i j}$ be the normalized loading using the following form:

$$
l_{i j}=\frac{k_{i j}}{\sum_{i j} k_{i j}}, \quad i=1, . ., 4
$$

The linear combination of EFs that will be used as independent variables is$$
X_{i}=\sum_{i} l_{i j} * E F_{i j}
$$

where $\mathrm{EF}_{\mathrm{ij}}$ denotes the $j$ th EF score in the $i$ th common factor $\mathrm{C}_{\mathrm{i}}$. Here $X_{1}$ and $X_{2}$ represent the weighted linear combinations of 'Overall' and 'Testing Efficiency' index scores, respectively. $X_{3}$ and $X_{4}$ represent the weighted linear combinations of 'Requirement and Specification' and 'Program and Skill Level' index score for each one.

Table 8.9. Identification of the common factors

| Common <br> factor | Index | EF | Name | Loading |
| :--: | :--: | :--: | :--: | :--: |
| $\mathrm{C}_{1}$ | Overall | F21 | Testing environment | 0.926 |
|  |  | F22 | Testing effort | 0.803 |
|  |  | F5 | Level of programming | 0.718 |
|  |  | F12 | Technologies relationship of detailed design and requirements | 0.696 |
| $\mathrm{C}_{2}$ | Testing efficiency | F24 | Testing methodologies | 0.844 |
|  |  | F25 | Testing coverage | 0.823 |
|  |  | F6 | Percentage of reused code | 0.714 |
| $\mathrm{C}_{3}$ | Requirements and specification | F11 | Requirements analysis | 0.826 |
|  |  | F8 | Frequency of specification change | 0.603 |
| $\mathrm{C}_{4}$ | Program and skill level | F15 | Programmer skills | 0.845 |
|  |  | F1 | Program complexity | 0.605 |

There are a total of 15 different linear regression models: 4 simple linear regression models with only 1 independent variable each: 6 linear regression models with 2 independent variables: 4 linear regression models with 3 independent variables: and one full linear regression with all 4 independent variables. Among the 15 linear regression models, six models turned out to be significant which include all simple regression models (Models I, II, III, and IV) and 2 models (Model V and VI) with 2 independent variables (Zhang et al. 2001a). The intercept is not statistical significant in any of these regression models. The results are summarized in Table 8.10.

From Table 8.10, for example, the regression model VI of the estimate of IASRA, $I A \hat{S} R A$, can be expressed as the linear equation of $X_{3}$ and $X_{4}$ such that

$$
I A \hat{S} R A=3.31^{*} X_{3}+2.76^{*} X_{4}
$$

This equation implies that the predicted score for the improvement of the accuracy of software reliability assessment increases as the 'Requirement and Specification' index and in the 'Program and Skill Level' index increases.Table 8.10. Parameter estimates based on the common factors

| Model | No. of <br> variables <br> in model | Variables | Parameter <br> estimate | P-value | $\mathrm{R}^{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| I | 1 | $X_{1}$ | 1.29 | 0.0001 | 0.9433 |
| II | 1 | $X_{2}$ | 2.20 | 0.0001 | 0.9332 |
| III | 1 | $X_{3}$ | 6.29 | 0.0001 | 0.9368 |
| IV | 1 | $X_{4}$ | 5.68 | 0.0001 | 0.9348 |
| V | 2 | $X_{2}$ | 1.08 | 0.0571 | 0.9464 |
| VI | 2 | $X_{3}$ | 2.97 | 0.0436 |  |
|  |  | $X_{4}$ | 3.31 | 0.0369 | 0.9485 |

# Testing Between - Phases Within the Development Process 

Thirty-two EFs are now divided into five categories: 'General', 'Analysis and Design', 'Coding', 'Testing' and 'Hardware systems'. In this analysis, we consider 'Analysis and Design', 'Coding' and 'Testing' as the software development process phase (Zhang et al. 2001a). The null hypothesis is that these phases are of the same significant level. The results of one-way ANOVA including the Student-NewmanKeuls (SNK) multiple comparison tests are summarized in Table 8.11.

Table 8.11. SNK test result

| SNK grouping | Phase | Mean |
| :--: | :--: | :--: |
| A | Testing | 5.43 |
| A | Coding | 5.35 |
| A | General | 5.24 |
| A | Analysis and design | 5.03 |

The results show that these phases have slightly different mean values, ranging from 5.43 for the 'Testing' phase to 5.03 for the 'Analysis and design' phase. The same letter in the SNK grouping shown in the first column of Table 8.11 indicates that the different among the mean values are not statistically significant. Zhang and Pham (2000a) studied the time allocation for each of the development phases and it was found that the requirement analysis, design, coding, and testing takes about 25, 18,36 , and $21 \%$ of the entire development time. However, this result indicates that each development phase is considered equally important in terms of their impact on software reliability assessment.# Identifying Significant Environmental Factors Within Each Phase 

This section discusses the most important subsets of environmental factors describing the relationship between software reliability assessment and environmental factors for each phase. We consider the improvement of IASRA as a dependent variable and the 32 environmental factors as independent variables. The significant factors and their parameter estimates based on a linear regression backward elimination method are presented in Table 8.12.

Table 8.12. Significant EFs for each phase

| Phase | Variables | Name | Parameter estimate | $\begin{aligned} & \text { P- } \\ & \text { value } \end{aligned}$ | $\mathrm{R}^{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| General | f1 | Program complexity | 9.17 | 0.0001 | 0.9697 |
|  | f6 | Percentage of reused modules | 3.17 | 0.0907 |  |
| Analysis and design | f8 | Frequency of program specification change | 3.37 | 0.0635 | 0.9801 |
|  | f10 | Design methodology | 4.90 | 0.0063 |  |
|  | f13 | Work standards | 6.42 | 0.0068 |  |
| Coding | f17 | Development team size | 8.88 | 0.0192 | 0.9551 |
|  | f19 | Domain knowledge | 6.46 | 0.0341 |  |
| Testing | f21 | Testing environment | 12.57 | 0.0001 | 0.9703 |

The hypothesis of zero intercept was not rejected for any phase regression model. Therefore, it may be appropriate to remove the constant term from the model. Note that the program complexity (f1) and percent of reused modules (f6) are significant for 'General' phase with p-value 0.0001 and 0.0907 , respectively. That means program complexity and percent of reused modules provides significant information for the prediction of software reliability assessment in 'General' phase. Similar interpretation can be represented in the different development phase. More findings can be obtained in Zhang et al. (2001a) and Zhang and Pham (2000a).

### 8.5 A Generalized Model with Environmental Factors

In this section, we discuss several newly developed software reliability models that consider environmental factors by combining the proportional hazard model (Cox 1975) and existing software reliability models (Pham 2000a). Such factors are, e.g., the complexity metrics of the software, the development and environmental conditions, the effect of mental stress and human nature, the level of the test-teammembers, and the facility level during testing. The proportional hazard model has been widely used in medical applications to estimate the survival rate of patients.

| Notation |  |
| :-- | :-- |
| $\tilde{z}$ | Vector of environmental factors |
| $\tilde{\beta}$ | Coefficient vector of environmental factors |
| $\Phi(\tilde{\beta} \tilde{z})$ | Function of environmental factors |
| $\lambda_{0}(t)$ | Failure intensity rate function without environmental factors |
| $\lambda(t, \tilde{z})$ | Failure intensity rate function with environmental factors |
| $m_{0}(t)$ | Baseline mean value function without environmental factors |
| $m(t, \tilde{z})$ | Mean value function with environmental factors |
| $R_{0}(x / t)$ | Baseline reliability function without environmental factors |
| $R(x / t, \tilde{z})$ | Reliability function with environmental factors |

Chapter 6 has discussed the fault intensity rate function $\lambda(t)$ and the mean value function $m(t)$ based on NHPP without environmental factors. In this section, a fault intensity rate function that integrates environmental factors based on a proportional hazard model can be constructed using the following assumptions:

1. The fault intensity rate function consists of two categories: the fault intensity rate functions without environmental factors, $\lambda_{0}(t)$, and the environmental factor function, $\Phi(\tilde{\beta} \tilde{z})$.
2. The fault intensity rate function $\lambda_{0}(t)$ and the function of the environmental factors are independent. The function $\lambda_{0}(t)$ is also called the baseline intensity function.

Based on the proportional hazard model (PHM), let us consider the failure intensity function of a software system as the product of an unspecified baseline failure intensity $\lambda_{0}(t)$, a function that only depends on time, and environmental factor function $\Phi(\tilde{\beta} \tilde{z})$ incorporating the effects of a number of environmental factors.

The fault intensity function with environmental factors, $\lambda(t, \tilde{z})$, can be expressed as:

$$
\lambda(t, \tilde{z})=\lambda_{0}(t) \cdot \Phi(\tilde{\beta} \tilde{z})
$$

The mean value function with environmental factors then can be obtained as follows:

$$
m(t, \tilde{z})=\int_{0}^{t} \lambda_{0}(s) \Phi(\tilde{\beta} \tilde{z}) d s=\Phi(\tilde{\beta} \tilde{z}) \int_{0}^{t} \lambda_{0}(s) d s=\Phi(\tilde{\beta} \tilde{z}) m_{0}(t)
$$

The reliability function with environmental factors can be expressed as follows:$$
\begin{aligned}
R(x / t, \bar{z}) & =e^{-(m(t+x, \bar{z})-m(t, \bar{z}))} \\
& =e^{-\left(\Phi(\bar{\beta} \bar{x}) m_{0}(t+x, \bar{z})-\Phi(\bar{\beta} \bar{x}) m_{0}(t, \bar{z})\right)} \\
& =\left[R_{0}(x / t)\right]^{\Phi(\bar{\beta} \bar{x})}
\end{aligned}
$$

The basic assumption for PHM is that the ratio of the failure intensity functions of any two errors observed at any time $t$ associated with any environmental factor sets $z_{i i}$ and $z_{2 i}$ is a constant with respect to time and they are proportional to each other. In other words, $\left(t_{i}, z_{1 i}\right)$ is directly proportional to $\left(t_{i}, z_{2 i}\right)$.

Assuming the exponential function of environmental form, then a failure intensity function of the software reliability model that considers environmental factors can be written as

$$
\lambda\left(t_{i} ; z_{i}\right)=\lambda_{0}\left(t_{i}\right) e^{\left(\sum_{j=1}^{n} \beta_{j} z_{j i}\right)}
$$

where

| $z_{i j}$ | environmental factor $j$ of the $i$ th error |
| :-- | :-- |
| $\beta_{j}$ | regression coefficient of the $j$ th factor |
| $t_{i}$ | failure time between the $(i-1)^{\text {th }}$ error and $i$ th error, $i=1,2, \ldots, n$ |
| $z_{i}$ | environmental factor of the $i$ th error |
| $m$ | number of environmental factors. |

It is easy to see that $\lambda_{0}(t)$ is a baseline failure intensity function that represents the failure intensity when all environmental factors variables are set to zero.

Let $Z$ be a column vector consisting of the environmental factors and $B$ represents a row vector consisting of the corresponding regression parameters. Then the above failure intensity model can be rewritten as

$$
\lambda(t ; Z)=\lambda_{0}(t) e^{(B Z)}
$$

Therefore, the reliability of the software systems can be written in a general form, as follows:

$$
\begin{aligned}
R(t ; Z) & =e^{-\int \lambda_{0}(x) e^{B Z} d x} \\
& =\left[e^{-\int \lambda_{0}(x) e^{B Z} d x}\right]^{\beta^{(B Z)}} \\
& =\left[R_{0}(t)\right]^{\beta^{B Z}}
\end{aligned}
$$

where $R_{0}(t)$ is the time-dependent software reliability. The pdf of the software system is given by

$$
\begin{aligned}
f(t ; Z) & =\lambda(t ; Z) \cdot R(t ; Z) \\
& =\lambda_{0}(t) e^{B Z}\left[R_{0}(t)\right]^{\beta^{B Z}}
\end{aligned}
$$The regression coefficient $B$ can be estimated, using either the MLE method or the maximum partial likelihood approach, which is discussed later, without assuming any specific distributions about the failure data and estimating the baseline failure intensity function. A direct generalization of the above model in equation (8.7) is that one may want to consider the environmental factor variables $Z_{j i}$ as a function of time. In this case, a mathematical generalized form of the failure intensity function is given by

$$
\lambda(t ; Z)=\lambda_{0}(t) e^{\left[\sum_{i=1}^{n} \beta_{j} z_{j i}(t)\right]}
$$

# 8.6 Environmental Parameter Estimation 

In this section, we will discuss how to estimate the parameters in the environmental factor model by using two widely used methods: the MLE method and the partial likelihood method. The advantage of the partial likelihood method is that it does not require as much data as the typical maximum likelihood method. Therefore, the data collection required by regression method can be simplified. Information of similar applications and settings of environmental factors that have been stored in databases can be utilized.

## Environmental Factors Estimation Using MLE

Assume that there are $p$ unknown parameters in the baseline failure intensity function $\lambda_{0}(t)$, say $\alpha_{1}, \alpha_{2}, \ldots, \alpha_{\mathrm{p}}$, and there are $m$ environmental factors $\beta_{1}, \beta_{2}, \ldots$, $\beta_{\mathrm{m}}$. Let $A=\left(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{\mathrm{p}}\right)$ be a set of unknown parameters $\alpha_{1}, \alpha_{2}, \ldots, \alpha_{\mathrm{p}}$, and $B$ be a set of $\beta_{1}, \beta_{2}, \ldots, \beta_{\mathrm{m}}$. Then the likelihood function is given by

$$
\begin{aligned}
L(A, B) & =\prod_{i=1}^{n} f\left(t_{i} ; z_{i}\right) \\
& =\prod_{i=1}^{n}\left(\lambda_{0}\left(t_{i}\right) e^{\left(\sum_{i=1}^{n} \beta_{j} z_{j i}\right)}\left[R_{0}\left(t_{i}\right)\right]^{\left(\sum_{i=1}^{n} \beta_{j} z_{j i}\right)}\right)
\end{aligned}
$$

The log likelihood function is given by

$$
\ln L(A, B)=\sum_{i=1}^{n} \ln \left[\lambda_{0}\left(t_{i}\right)\right]+\sum_{i=1}^{n} \sum_{j=1}^{m} \beta_{j} z_{j i}+\sum_{i=1}^{n} e^{\left(\sum_{i=1}^{n} \beta_{i} z_{i i}\right)}
$$

Taking the first partial derivatives of the log likelihood function with respect to ( $m$ $+p$ ) parameters, we obtain

$$
\frac{\partial}{\partial \alpha_{k}}[\ln L(A, B)]=\sum_{i=1}^{n} \frac{\frac{\partial}{\partial \alpha_{k}}\left[\lambda_{0}\left(t_{i}\right)\right]}{\lambda_{0}\left(t_{i}\right)}+\sum_{i=1}^{n} e^{\left(\sum_{i=1}^{n} \beta_{i} z_{i i}\right)} \frac{\frac{\partial}{\partial \alpha_{k}}\left[R_{0}\left(t_{i}\right)\right]}{R_{0}\left(t_{i}\right)}
$$$$
\frac{\partial}{\partial \beta_{s}}[\ln L(A, B)]=\sum_{i=1}^{n} z_{s i}+\sum_{i=1}^{n} z_{s i} e^{\left(\sum_{j=1}^{n} \beta_{j} z_{p}\right)} \ln \left[R_{0}\left(t_{i}\right)\right]
$$

where $k=1,2,--, p$ and $s=1,2, \ldots, m$.
Setting the previous equations equal to zero, we can obtain all the $(m+p)$ parameters by solving the following system of $(m+p)$ equations simultaneously:

$$
\begin{gathered}
\sum_{i=1}^{n}\left[\frac{\frac{\partial}{\partial \alpha_{k}}\left[\lambda_{0}\left(t_{i}\right)\right]}{\lambda_{0}\left(t_{i}\right)}+e^{\left(\sum_{j=1}^{m} \beta_{j} z_{p}\right)} \frac{\partial}{\partial \alpha_{k}}\left[R_{0}\left(t_{i}\right)\right]}{R_{0}\left(t_{i}\right)}\right]=0 \quad \text { for } k=1,2, \ldots, p \\
\sum_{i=1}^{n} z_{s i}\left[1+e^{\left(\sum_{j=1}^{m} \beta_{j} z_{p}\right)} \ln \left[R_{0}\left(t_{i}\right)\right]\right]=0 \quad \text { for } s=1,2, \ldots, m
\end{gathered}
$$

# Environmental Factors Estimation Using Maximum Partial Likelihood Approach 

According to the idea of Cox's proportional hazard model, we can use the maximum partial likelihood method to estimate environmental factors without assuming any specific distributions about the failure data and estimating the baseline failure intensity function. The only basic assumption of this model is that the ratio of the failure intensity functions of any two errors observed at any time $t$ associated with any environmental factor sets $z_{1 i}$ and $z_{2 i}$ is constant with respect to time and they are proportional to each other.

First we estimate the environmental factor parameters based on the partial likelihood function. The partial likelihood function of this model is given by

$$
L(B)=\prod_{i=1}^{n} \frac{e^{\left(\beta_{1} z_{1 i}+\beta_{2} z_{2 i}+\ldots \ldots+\beta_{m} z_{m i}\right)}}{\sum_{k \in R_{i}} e^{\left(\beta_{1} z_{1 k}+\beta_{2} z_{2 k}+\ldots \ldots+\beta_{i} z_{i k}\right)}}
$$

where $R_{i}$ is the risk set at $t_{i}$. Take the derivatives of the log partial likelihood function with respect to $\beta_{1}, \beta_{2}, \ldots, \beta_{m}$ and let them equal zero. Therefore, we can obtain all of the estimated $\beta_{s}$ by solving these equations simultaneously using numerical methods. After estimating the factor parameters $\beta_{1}, \beta_{2}, \ldots, \beta_{m}$, the remaining task is to estimate the unknown parameters of the baseline failure intensity function $\lambda_{0}(t)$.

### 8.7 Enhanced Proportional Hazard Jelinski-Moranda (EPJM) Model

Recall that the Jelinski-Moranda (JM) model is one of the earliest models developed for predicting software reliability (see Chapter 5). The failure intensity of the software at the $i$ th failure interval of this model is given by$$
\lambda\left(t_{i}\right)=\phi[N-(i-1)] \quad i=1,2, \ldots, N
$$

and the probability density function is given by

$$
f\left(t_{i}\right)=\phi[N-(i-1)] e^{-\phi[N-(i-1)] t_{i}}
$$

The enhanced proportional hazard JM model (Pham 2000a), called the EPJM model, which is based on the proportional hazard and J M model, is expressed as

$$
\lambda\left(t_{i} ; z_{i}\right)=\phi[N-(i-1)] e^{\left(\sum_{j=1}^{N} \beta_{j} z_{j i}\right)}
$$

and the pdf corresponding to $\left(t_{i}, z_{i}\right)$ is given by

$$
f\left(t_{i} ; z_{i}\right)=\phi[N-(i-1)] e^{\left(\sum_{j=1}^{N} \beta_{j} z_{j i}\right)} e^{\left[-\phi[N-(i-1)] t_{i} e^{\left(\sum_{j=1}^{N} \beta_{j} z_{j i}\right)}\right]}
$$

Now we wish to estimate the parameters of the EPJM model using the two methods discussed in Section 5, the maximum likelihood method and the maximum partial likelihood method. There are $(m+2)$ unknown parameters in this model.

# The Maximum Likelihood Method 

From equation (8.10), the likelihood function of the model is given by

$$
\begin{aligned}
L(B, N, \phi) & =\prod_{i=1}^{n} f\left(t_{i} ; z_{i}\right) \\
& =\prod_{i=1}^{n}\left(\phi[N-(i-1)] e^{\left(\sum_{j=1}^{N} \beta_{j} z_{j i}\right)} e^{\left[-\phi[N-(i-1)] t_{i} e^{\left(\sum_{j=1}^{N} \beta_{j} z_{j i}\right)}\right.}\right)
\end{aligned}
$$

The log likelihood function is given by

$$
\begin{aligned}
\ln L(B, N, \phi)= & n \ln \phi+\sum_{i=1}^{n} \ln [N-(i-1)]+\sum_{i=1}^{n}\left(\sum_{j=1}^{m} \beta_{j} z_{j i}\right) \\
& -\sum_{i=1}^{n} \phi[N-(i-1)] t_{i} e^{\sum_{j=1}^{m}\left(\beta_{j} z_{j i}\right)}
\end{aligned}
$$

Taking the first partial derivatives of the log likelihood function with respect to $(m+2)$ parameter: $\beta_{1}, \beta_{2}, \ldots, \beta_{\mathrm{m}}, N$, and $\Phi$, we obtain the following:

$$
\begin{gathered}
\frac{\partial \log L}{\partial \phi}=\frac{n}{\phi}-\sum_{i=1}^{n}[N-(i-1)] t_{i} e^{\sum_{j=1}^{m}\left(\beta_{j} z_{j i}\right)} \\
\frac{\partial \log L}{\partial N}=\sum_{i=1}^{n} \frac{1}{[N-(i-1)]}-\phi \sum_{i=1}^{n} t_{i} e^{\sum_{j=1}^{m}\left(\beta_{j} z_{j i}\right)}
\end{gathered}
$$

and$$
\frac{\partial \log L}{\partial \beta_{j}}=\sum_{i=1}^{n} z_{j i}-\sum_{i=1}^{n} \phi[N-(i-1)] t_{i} z_{j i} e^{\sum_{j=1}^{n}\left(\beta_{j} z_{j i}\right)}
$$

Setting all of these equations equal to zero, we can obtain the estimated $(m+2)$ parameters by solving the following system equations simultaneously using a numerical method:

$$
\begin{gathered}
\sum_{i=1}^{n}[N-(i-1)] t_{i} e^{\sum_{j=1}^{n}\left(\beta_{j} z_{j i}\right)}=\frac{n}{\phi} \\
\sum_{i=1}^{n} \frac{1}{[N-(i-1)]}=\phi \sum_{i=1}^{n} t_{i} e^{\sum_{j=1}^{n}\left(\beta_{j} z_{j i}\right)} \\
\sum_{i=1}^{n} \phi[N-(i-1)] t_{i} z_{j i} e^{\sum_{j=1}^{n}\left(\beta_{j} z_{j i}\right)}=\sum_{i=1}^{n} z_{j i} \quad \text { for } j=1,2, \ldots, m
\end{gathered}
$$

# The Maximum Partial Likelihood Method 

Assume that the baseline failure intensity has the form of the JM model. That means that the basic assumption of this model (see Section 4) is satisfied and that the ratio of the failure intensity functions of any two errors observed at any time $t$, associated with any environmental factor sets $z_{1 i}$ and $z_{2 i}$, is a constant with respect to time and they are proportional to each other.

Having estimated the factor parameters $\beta_{1}, \beta_{2}, \ldots, \beta_{m}$ the remaining task is to estimate the unknown parameters of the baseline failure intensity function. Note that the failure intensity function model has the form

$$
\begin{aligned}
\lambda\left(t_{i} ; z_{i}\right) & =\phi[N-(i-1)] e^{\left(\hat{\beta}_{1} z_{1 i}+\hat{\beta}_{2} z_{2 i}+\ldots . .+\hat{\beta}_{m} z_{m i}\right)} \\
& =\phi[N-(i-1)] E_{i}
\end{aligned}
$$

where

$$
E_{i}=e^{\left(\hat{\beta}_{1} z_{1 i}+\hat{\beta}_{2} z_{2 i}+\ldots . .+\hat{\beta}_{m} z_{m i}\right)}
$$

The pdf is given by

$$
f\left(t_{i} ; z_{i}\right)=\phi E_{i}[N-(i-1)] e^{-\left(\phi E_{i}[N-(i-1)] t_{i}\right)}
$$

The likelihood function is given by

$$
L(N, \phi)=\prod_{i=1}^{n}\left(\phi E_{i}[N-(i-1)] e^{-\left(\phi E_{i}[N-(i-1)] t_{i}\right)}\right)
$$

By taking the log of the likelihood function and its derivatives with respect to $N$ and $\phi$, and setting them equal to zero, we obtain the following equations:$$
\frac{\partial \ln L}{\partial N}=\sum_{i=1}^{n} \frac{1}{N-(i-1)}-\sum_{i=1}^{n} \phi E_{i} t_{i}=0
$$

and

$$
\frac{\partial \ln L}{\partial \phi}=\frac{n}{\phi}-\sum_{i=1}^{n} E_{i}[N-(i-1)] t_{i}=0
$$

The estimated $N$ and $\phi$ can be obtained as follows. First, the parameter $N$ can be obtained by solving the following equation:

$$
\left(\sum_{i=1}^{n} E_{i}[N-(i-1)] t_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{[N-(i-1)]}\right)=n \sum_{i=1}^{n} E_{i} t_{i}
$$

After finding $N$, the parameter can easily be obtained and is given by

$$
\phi=\frac{\sum_{i=1}^{n} \frac{1}{[N-(i-1)]}}{\sum_{i=1}^{n} E_{i} t_{i}}
$$

# 8.8 Applications 

Almost all software reliability engineering models need one of two basic types of input data: time-domain data and interval-domain data. One can possibly transform between the two types of data domains. The time-domain approach is characterized by recording the individual times at which the failure occurred. The intervaldomain approach is characterized by counting the number of failures that occurred over a given period.

Application 8.1: To illustrate the EPJM model, we use the software failure data reported by Musa (1975) and also refer to data set \#9 in Chapter 4. The data is related to a real-time command and control system. There is, however, no record of corresponding environmental factor measures in most, if not all, existing available data. To demonstrate the use of this model, we generate a failure-cluster factor and give its value which is logically realistic based on the failure data and consultation with several local software firms by the author.

One of the assumptions of the J-M model is that the time between failures is independent. As in many real testing environments, the failure times indeed occur in a cluster, i.e., the failure time within a cluster is relatively shorter than that between the clusters. Data set \#9 shows that it is reasonable in that particular application. This may indicate that the assumption of independent failure time is not correct. We can enhance the J-M model considering the failure-cluster factor by generating this factor based on the failure data.

We assume that if the present failure time, compared to the previous failure time, is relatively short, then some correlation may exist between them. Let us define a failure-cluster factor, such as$$
z_{i}= \begin{cases}1 & \text { when } \frac{t_{i-1}}{t_{i}} \geq 7 \text { or } \frac{t_{i-1}}{t_{i}} \geq 5 \\ 0 & \text { otherwise }\end{cases}
$$

The data used in this model include both the failure time data and the explanatory environmental factor data (see Table 8.13). The explanatory variable data is dynamic, that is, it changes depending on the failure time. For example, in Table 8.13 , the time between the fourth and fifth errors is 115 seconds; the time between the fifth and sixth errors is 9 seconds. Therefore, $z_{5}$ is assigned to 0 and $z_{6}$ is equal to 1 .

For the J-M model, using the MLE, we obtain the estimate of the two parameters, $N$ and $\phi$, as follows:

$$
\begin{aligned}
& \hat{N}=142 \\
& \hat{\phi}=(3.48893) \times 10^{-5}
\end{aligned}
$$

Therefore, the current reliability of the software system is given by

$$
R\left(t_{137}\right)=e^{-\hat{\phi}\left(\hat{N}-(137-1) t_{137}\right.}
$$

Now, we want to predict the future failure behavior using only data collected in the past after 136 errors have been found. For example, the reliability of the software for the next 100 seconds after 136 errors are detected is given by

$$
\begin{aligned}
R\left(t_{137}=100\right) & =e^{-\hat{\phi}\left(\hat{N}-(137-1) t_{137}\right.} \\
& =e^{-(3.4889310^{-5})(142-136)(100)} \\
& =0.979284
\end{aligned}
$$

Similarly, the reliability of the software for the next 1000 seconds is given by

$$
\begin{aligned}
R\left(t_{137}=1000\right) & =e^{-(0.0000348893[142-136](1,000)} \\
& =0.811123
\end{aligned}
$$

Assume that we use the partial likelihood approach to estimate the environmental factor parameter for the EPJM model. As there is only one factor in this example, we can easily obtain the estimated parameter using the statistical software package SAS:

$$
\hat{\beta}_{1}=1.767109
$$

with a significance level of 0.0001 . Then the estimates of $N$ and $\phi$ are given as follows:

$$
\begin{aligned}
& \hat{N}=141 \\
& \hat{\phi}=(3.28246) \times 10^{-5}
\end{aligned}
$$Table 8.13. Musa's failure time data with a generated covariate

| Fault | Time | z | Fault | Time | z |
| :--: | --: | :--: | --: | --: | --: |
| 1 | 3 | 0 | 35 | 227 | 0 |
| 2 | 30 | 0 | 36 | 65 | 0 |
| 3 | 113 | 0 | 37 | 176 | 0 |
| 4 | 81 | 0 | 38 | 58 | 0 |
| 5 | 115 | 0 | 39 | 457 | 0 |
| 6 | 9 | 1 | 40 | 300 | 0 |
| 7 | 2 | 1 | 41 | 97 | 0 |
| 8 | 91 | 0 | 42 | 263 | 0 |
| 9 | 112 | 0 | 43 | 452 | 0 |
| 10 | 15 | 1 | 44 | 255 | 0 |
| 11 | 138 | 0 | 45 | 197 | 0 |
| 12 | 50 | 0 | 46 | 193 | 0 |
| 13 | 77 | 0 | 47 | 6 | 1 |
| 14 | 24 | 0 | 48 | 79 | 0 |
| 15 | 108 | 0 | 49 | 816 | 0 |
| 16 | 88 | 0 | 50 | 1351 | 0 |
| 17 | 670 | 0 | 51 | 148 | 1 |
| 18 | 120 | 0 | 52 | 21 | 1 |
| 19 | 26 | 1 | 53 | 233 | 0 |
| 20 | 114 | 0 | 54 | 134 | 0 |
| 21 | 325 | 0 | 55 | 357 | 0 |
| 22 | 55 | 0 | 56 | 193 | 0 |
| 23 | 242 | 0 | 57 | 236 | 0 |
| 24 | 68 | 0 | 58 | 31 | 1 |
| 25 | 422 | 0 | 59 | 369 | 0 |
| 26 | 180 | 0 | 60 | 748 | 0 |
| 27 | 10 | 1 | 61 | 0 | 1 |
| 28 | 1146 | 0 | 62 | 232 | 0 |
| 29 | 600 | 0 | 63 | 330 | 0 |
| 30 | 15 | 1 | 64 | 365 | 0 |
| 31 | 36 | 1 | 65 | 1222 | 0 |
| 32 | 4 | 1 | 66 | 543 | 0 |
| 33 | 0 | 1 | 67 | 10 | 1 |
| 34 | 8 | 0 | 68 | 16 | 1 |Table 8.13. (continued)

| Fault | Time | z | Fault | Time | z |
| :--: | --: | --: | --: | --: | --: |
| 69 | 529 | 0 | 103 | 108 | 0 |
| 70 | 379 | 0 | 104 | 0 | 1 |
| 71 | 44 | 1 | 105 | 3110 | 0 |
| 72 | 129 | 0 | 106 | 1247 | 0 |
| 73 | 810 | 0 | 107 | 943 | 0 |
| 74 | 290 | 0 | 108 | 700 | 0 |
| 75 | 300 | 0 | 109 | 875 | 0 |
| 76 | 529 | 0 | 110 | 245 | 0 |
| 77 | 281 | 0 | 111 | 729 | 0 |
| 78 | 160 | 0 | 112 | 1897 | 0 |
| 79 | 828 | 0 | 113 | 447 | 0 |
| 80 | 1011 | 0 | 114 | 386 | 0 |
| 81 | 445 | 0 | 115 | 446 | 0 |
| 82 | 296 | 0 | 116 | 122 | 0 |
| 83 | 1755 | 0 | 117 | 990 | 0 |
| 84 | 1064 | 0 | 118 | 948 | 0 |
| 85 | 1783 | 0 | 119 | 1082 | 0 |
| 86 | 860 | 0 | 120 | 22 | 1 |
| 87 | 983 | 0 | 121 | 75 | 1 |
| 88 | 707 | 0 | 122 | 482 | 0 |
| 89 | 33 | 1 | 123 | 5509 | 0 |
| 90 | 868 | 0 | 124 | 100 | 1 |
| 91 | 724 | 0 | 125 | 10 | 1 |
| 92 | 2323 | 0 | 126 | 1071 | 0 |
| 93 | 2930 | 0 | 127 | 371 | 0 |
| 94 | 1461 | 0 | 128 | 790 | 0 |
| 95 | 843 | 0 | 129 | 6150 | 0 |
| 96 | 12 | 1 | 130 | 3321 | 0 |
| 97 | 261 | 0 | 131 | 1045 | 1 |
| 98 | 1800 | 0 | 132 | 648 | 1 |
| 99 | 865 | 0 | 133 | 5485 | 0 |
| 100 | 1435 | 0 | 134 | 1160 | 0 |
| 101 | 30 | 1 | 135 | 1864 | 0 |
| 102 | 143 | 1 | 136 | 4116 | 0 |

Therefore,

$$
E_{t}=e^{\rho_{t} z_{t_{1}}}=\left\{\begin{array}{ll}
5.853905 & \text { for } z=1 \\
1 & \text { for } z=0
\end{array}\right.
$$

The current reliability of the software system is given by$$
\begin{aligned}
R\left(t_{137}\right) & =e^{-\phi E_{137}\left(\hat{N}-(137-1)\right) t_{137}} \\
& = \begin{cases}e^{-9.607610^{-4} t_{137}} & \text { for } z=1 \\
e^{-1.6412310^{-4} t_{137}} & \text { for } z=0\end{cases}
\end{aligned}
$$

Assuming that

$$
\begin{aligned}
& P(Z=1)=\frac{28}{136}=0.20588 \\
& P(Z=0)=\frac{108}{136}=0.79412
\end{aligned}
$$

The reliability of the software for the next 100 seconds is given by

$$
\begin{aligned}
R\left(t_{137}=100\right)=0.90839 & \text { for } z=1 \text { with probability }=0.20588 \\
=0.98372 & \text { for } z=0 \text { with probability }=0.79412
\end{aligned}
$$

or, equivalently, that

$$
R\left(t_{137}=100\right)=0.95375
$$

Similarly, the reliability of the software for the next 1000 seconds is given by

$$
\mathrm{R}\left(\mathrm{t}_{137}=1000\right)= \begin{cases}0.3826 & \text { for } z=1 \text { with probability }=0.20588 \\ 0.84864 & \text { for } z=0 \text { with probability }=0.79412\end{cases}
$$

or

$$
R\left(t_{137}=1000\right)=0.74021
$$

In the next two applications, we use Pham-Zhang NHPP model given in equation (6.62) to illustrate the model with environmental factors. The corresponding Pham-Zhang NHPP model baseline intensity function can be expressed as follows:

$$
\begin{aligned}
\lambda_{0}(t) & =\frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{bt}}\right)}\left[(c+a)\left(1-e^{-b t}\right)-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\
& +\frac{-\beta b e^{-b t}}{\left(1+\beta e^{-b t}\right)^{2}}\left[(c+a)\left(1-e^{-b t}\right)-\frac{a b\left(e^{-\alpha t}-e^{-b t}\right)}{b-\alpha}\right]
\end{aligned}
$$

Any NHPP models can easily be integrated into a model with environmental factors using equation (8.5).

Application 8.2: The first set of software failure data is collected from testing a program for a monitor and real-time control systems (Tohma 1991) (also see data set \#8, Chapter 4). Table 8.14 records the software failures detected during a 111day testing period. The only environmental factor available for this application is the testing team size. Team size is one of the most useful measures in the software development process since it has a close relationship with the testing effort, testing efficiency and the development management issues.

From the correlation analysis of the 32 environmental factors, team size is the only environmental factor correlated to the program complexity, which is the number one significant factor according to our environmental factor study.Intuitively, the more complex the software, the larger the development team. Therefore, testing team size is an important factor to be incorporated into the software reliability analysis.

Table 8.14 combines the information of testing team size with the software failure data. It is interesting to note that there are two clusters where increasing number of faults are detected. Checking the testing team size, we find that the testing team size was enlarged for the periods associated with the two clusters where increasing number of failures were encountered (day 11 - day 17 and day 36 - day 42). This indicates that testing team is an important factor we need to consider at least for this data set.

Since the testing team size ranges from 1 to 8 , we first categorize the factor of team size into two levels. Let $z_{i}$ denote the factor of team size as follows:

$$
z_{i}= \begin{cases}0 & \text { team size ranges from } 1-4 \\ 1 & \text { team size ranges from 5-8 }\end{cases}
$$

After carefully examining the failure data, we find that after day 61, the software turns stable and the failures occur with a much slower frequency. Therefore, we use the first 61 data points for testing the goodness-of-fit and estimating the parameters. Then we use the calibrated model to predict the remaining 50 data points and compare the prediction to the 50 data points actually observed (from day 62 to day 111) for examining the predictive power of software reliability models.

From equation (8.16), the intensity function with environmental factor is given by:

$$
\begin{aligned}
& \lambda(t)=\lambda_{0}(t) \cdot e^{\beta_{1} z_{1}} \\
& =\left\{\begin{array}{l}
\frac{1}{\left(1+\beta \mathrm{e}^{\lambda \alpha}\right)}\left[(c+a)\left(1-e^{-b t}\right)-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\
+\frac{-\beta b e^{-b t}}{\left(1+\beta e^{-b t}\right)^{2}}\left[(c+a)\left(1-e^{-b t}\right)-\frac{a b\left(e^{-\alpha t}-e^{-b t}\right)}{b-\alpha}\right]
\end{array}\right\} e^{\beta_{1} z_{1}}
\end{aligned}
$$

First, the coefficient $\beta_{1}$ is estimated using partial likelihood estimate method. The partial likelihood method estimates the coefficients of covariates separately from the parameters in the baseline intensity function. From equation (8.11), the likelihood function of partial likelihood method is given by

$$
L(\beta)=\prod_{i}\left(\frac{\exp \left(\beta z_{i}\right)}{\left[\sum_{m \in R} \exp \left(\beta z_{m}\right)\right]^{d_{i}}}\right)
$$

where $d_{\mathrm{i}}$ represented the tie failure times. The estimate of $\beta_{1}$ for our example is $\hat{\beta}_{1}=0.0246$ with $p$-value 0.01 , which indicates that this factor is statistical significant to consider. We then substitute $\hat{\beta}_{1}$ into the failure intensity model in equation (8.17) and estimate the parameters in the baseline function.Table 8.14. Software testing data for application 1 (those marked with * are interpolated data)

| Days | Faults | Cum. <br> faults | Team size | Days | Faults | Cum. <br> faults | Team <br> size |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | $5^{*}$ | $5^{*}$ | 4 | 29 | 2 | 254 | 6 |
| 2 | $5^{*}$ | $10^{*}$ | 4 | 30 | 5 | 259 | 6 |
| 3 | $5^{*}$ | $15^{*}$ | 4 | 31 | 4 | 263 | 6 |
| 4 | $5^{*}$ | $20^{*}$ | 4 | 32 | 1 | 264 | 6 |
| 5 | $6^{*}$ | $26^{*}$ | 4 | 33 | 4 | 268 | 6 |
| 6 | 8 | 34 | 5 | 34 | 3 | 271 | 6 |
| 7 | 2 | 36 | 5 | 35 | 6 | 277 | 6 |
| 8 | 7 | 43 | 5 | 36 | 13 | 293 | 6 |
| 9 | 4 | 47 | 5 | 37 | 19 | 309 | 8 |
| 10 | 2 | 49 | 5 | 38 | 15 | 324 | 8 |
| 11 | 31 | 80 | 5 | 39 | 7 | 331 | 8 |
| 12 | 4 | 84 | 5 | 40 | 15 | 346 | 8 |
| 13 | 24 | 108 | 5 | 41 | 21 | 367 | 8 |
| 14 | 49 | 157 | 5 | 42 | 8 | 375 | 8 |
| 15 | 14 | 171 | 5 | 43 | 6 | 381 | 8 |
| 16 | 12 | 183 | 5 | 44 | 20 | 401 | 8 |
| 17 | 8 | 191 | 5 | 45 | 10 | 411 | 8 |
| 18 | 9 | 200 | 5 | 46 | 3 | 414 | 8 |
| 19 | 4 | 204 | 5 | 47 | 3 | 417 | 8 |
| 20 | 7 | 211 | 5 | 48 | 8 | 425 | 4 |
| 21 | 6 | 217 | 5 | 49 | 5 | 430 | 4 |
| 22 | 9 | 226 | 5 | 50 | 1 | 431 | 4 |
| 23 | 4 | 230 | 5 | 51 | 2 | 433 | 4 |
| 24 | 4 | 234 | 5 | 52 | 2 | 435 | 4 |
| 25 | 2 | 236 | 5 | 53 | 2 | 437 | 4 |
| 26 | 4 | 240 | 5 | 54 | 7 | 444 | 4 |
| 27 | 3 | 243 | 5 | 55 | 2 | 446 | 4 |
| 28 | 9 | 252 | 6 | 56 | 0 | 446 | 4 |Table 8.14 (continued)

| Days | Faults | Cumulative <br> Faults | Team <br> Size | Days | Faults | Cumulative <br> Faults | Team <br> Size |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 57 | 2 | 448 | $\mathbf{4}$ | 85 | 0 | 473 | $\mathbf{2}$ |
| 58 | 3 | 451 | $\mathbf{4}$ | 86 | 0 | 473 | $\mathbf{2}$ |
| 59 | 2 | 453 | $\mathbf{4}$ | 87 | 2 | 475 | $\mathbf{2}$ |
| 60 | 7 | 460 | $\mathbf{4}$ | 88 | 0 | 475 | $\mathbf{2}$ |
| 61 | 3 | 463 | $\mathbf{4}$ | 89 | 0 | 475 | $\mathbf{2}$ |
| 62 | 0 | 463 | $\mathbf{4}$ | 90 | 0 | 475 | $\mathbf{2}$ |
| 63 | 1 | 464 | $\mathbf{4}$ | 91 | 0 | 475 | $\mathbf{2}$ |
| 64 | 0 | 464 | $\mathbf{4}$ | 92 | 0 | 475 | $\mathbf{2}$ |
| 65 | 1 | 465 | $\mathbf{4}$ | 93 | 0 | 475 | $\mathbf{2}$ |
| 66 | 0 | 465 | $\mathbf{3}$ | 94 | 0 | 475 | $\mathbf{2}$ |
| 67 | 0 | 465 | $\mathbf{3}$ | 95 | 0 | 475 | $\mathbf{2}$ |
| 68 | 1 | 466 | $\mathbf{3}$ | 96 | 1 | 476 | $\mathbf{2}$ |
| 69 | 1 | 467 | $\mathbf{3}$ | 97 | 0 | 476 | $\mathbf{2}$ |
| 70 | 0 | 467 | $\mathbf{3}$ | 98 | 0 | 476 | $\mathbf{2}$ |
| 71 | 0 | 467 | $\mathbf{3}$ | 99 | 0 | 476 | $\mathbf{2}$ |
| 72 | 1 | 468 | $\mathbf{3}$ | 100 | 1 | 477 | $\mathbf{2}$ |
| 73 | 1 | 469 | $\mathbf{4}$ | 101 | 0 | 477 | $\mathbf{1}$ |
| 74 | 0 | 469 | $\mathbf{4}$ | 102 | 0 | 477 | $\mathbf{1}$ |
| 75 | 0 | 469 | $\mathbf{4}$ | 103 | 1 | 478 | $\mathbf{1}$ |
| 76 | 0 | 469 | $\mathbf{4}$ | 104 | 0 | 478 | $\mathbf{1}$ |
| 77 | 1 | 470 | $\mathbf{4}$ | 105 | 0 | 478 | $\mathbf{1}$ |
| 78 | 2 | 472 | $\mathbf{2}$ | 106 | 1 | 479 | $\mathbf{1}$ |
| 79 | 0 | 472 | $\mathbf{2}$ | 107 | 0 | 479 | $\mathbf{1}$ |
| 80 | 1 | 473 | $\mathbf{2}$ | 108 | 0 | 479 | $\mathbf{1}$ |
| 81 | 0 | 473 | $\mathbf{2}$ | 109 | 1 | 480 | $\mathbf{1}$ |
| 82 | 0 | 473 | $\mathbf{2}$ | 110 | 0 | 480 | $\mathbf{1}$ |
| 83 | 0 | 473 | $\mathbf{2}$ | 111 | 1 | 481 | $\mathbf{1}$ |
| 84 | 0 | 473 | $\mathbf{2}$ |  |  |  |  |

The estimates of parameters in the baseline failure intensity function are as follows:

$$
\hat{a}=40.0, \hat{b}=0.09, \hat{\beta}=8.0, \hat{\alpha}=0.015, \hat{c}=450
$$

After all the parameters are estimated, the mean value function and the software reliability model can be determined. It can then be used to predict quantitatively the software performance metrics such as software reliability, the number of remaining faults, and the failure intensity rate. Table 8.15 compares the SSE and AIC values for some existing NHPP models and the model with environmental factors. It seems that the environmental factor model in equation (8.17) provides a significantly improved predictive power according to the SSE and AIC criteria. This validates that (1) team size is a significant environmental factor for this data set and (2) incorporating this factor provide a better description of the fault detection process and thus enhances the predictive power of the software reliability model.Note that since the SSE value of the environmental factor model is significantly smaller, other comparison criteria that compensate the model complexity in terms of the number of parameters such as MSE is not necessary. Also, the model provides other useful information such as the number of initial faults is $\hat{c}=450$ and the number of introduced faults is $\hat{a}=40$. Therefore, the number of total faults in the software is about 490 . By the end of the software testing, 481 faults were detected, which implies that 9 faults still remain in the software.

Sensitivity analysis of the environmental factors categorization is desired to find out whether the categories of defining the environmental factors has significant influence on the final predictive results. Since in practice the typical testing team consists of two people, we re-define the level of team size and reexamine the prediction of the model. This time, we use three levels for the team size. In other words, $z_{1}^{\prime}$ is defined as follows:

$$
z_{1}^{\prime}= \begin{cases}0 & \text { team size ranges from 1-2 } \\ 1 & \text { team size ranges from 3-5 } \\ 2 & \text { team size } \geq 6\end{cases}
$$

The estimate of $\beta_{1}^{\prime}$ for this example is $\hat{\beta}_{1}^{\prime}=0.01129$ with $p$-value 0.04469 .
Similary, the estimates of parameters in equation (8.17) for the numerical example are as follows:

$$
\hat{a}=40.2, \hat{b}=0.088, \hat{\beta}=8.1, \hat{\alpha}=0.0175, \text { and } \hat{c}=451.2
$$

We now use this model to predict the detected errors from day 62 to day 111 and compare it with the existing reliability models without environmental factors and the Environmental Factor Model proposed in this paper. The SSE value for the model with three-category team size is 537.48 , which is even lower than the SSE of the model with two-category team size (see Table 8.2). Therefore, we can draw a conclusion that, for this example, reliability models incorporating team size provide significant enhancement in terms of predictive power.

Application 8.3: The second set of software failure data is collected from testing a large telecommunications software system, which consists of approximately 7000000 non-commentary source lines (NCSL). This release contained approximately 400000 new or changed NCSL for adding new features and fixing existing faults. Table 8.16 summarizes the staff time spent testing, the number of faults detected, and the additional line of code under test. Therefore, the line of code is considered as the environmental factor for this application. Changed code size is one of the most useful metrics of the software development process from which other metrics can be estimated.Table 8.15. Model comparison for application 2

| Model name | $\operatorname{MVF}(m(\mathrm{t}))$ | SSE <br> (prediction) | AIC |
| :-- | :-- | :-- | :--: |
| G-O model | $m(t)=a\left(1-e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=b$ | $1,052,528$ | 978.14 |
| Delayed S- <br> shaped | $m(t)=a\left(1-(1+b t) e^{-b t}\right)$ <br> $a(t)=a$ <br> $b(t)=\frac{b^{2} t}{1+b t}$ | $83,929.3$ | 983.90 |
| Inflexion S- <br> shaped | $m(t)=\frac{a\left(1-e^{-b t}\right)}{1+\beta e^{-b t}}$ <br> $a(t)=a$ <br> $b(t)=\frac{b}{1+\beta e^{-b t}}$ | $1,051,714.7$ | 980.14 |
| Yamada <br> exponential | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t t-1}\right)}\right)$ <br> $a(t)=a$ <br> $b(t)=r \alpha \beta e^{-\beta t}$ | $1,085,650.8$ | 979.88 |
| Yamada <br> Rayleigh | $m(t)=a\left(1-e^{-r \alpha\left(1-e^{(-t t-1}\right)}\right)$ <br> $a(t)=a$ <br> $b(t)=r \alpha \beta t e^{-\beta t^{2} / 2}$ | $86,472.3$ | 967.92 |
| Imperfect <br> debugging (1) | $m(t)=\frac{a b}{\alpha+b}\left(e^{\alpha t}-e^{-b t}\right)$ <br> $a(t)=a e^{\alpha t}$ <br> $b(t)=b$ | 791,941 | 981.44 |
| Imperfect <br> debugging (2) | $m(t)=a\left[1-e^{-b t}\right]\left[1-\frac{\alpha}{b}\right]+\alpha a t$ <br> $a(t)=a(1+\alpha t)$ <br> $b(t)=b$ | 238,324 | 984.62 |Table 8.15. (continued)

| PNZ Model | $\begin{aligned} & m(t)=\frac{a}{1+\beta e^{-b t}}\left[\left(1-e^{-b t}\right)\left(1-\frac{\alpha}{b}\right)+\alpha t\right] \\ & a(t)=a(1+\alpha t) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 94,112.2 | 965.37 |
| :--: | :--: | :--: | :--: |
| PZ model | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\theta t}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 86,180.8 | 960.68 |
| Environmental factor model | $\begin{aligned} & m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-b t}\right)}\left[(c+a)\left(1-e^{-b t}\right)\right. \\ & \left.\quad-\frac{a b}{b-\alpha}\left(e^{-\alpha t}-e^{-b t}\right)\right] e^{\beta / c_{1}} \\ & a(t)=c+a\left(1-e^{-\alpha t}\right) \\ & b(t)=\frac{b}{1+\beta e^{-b t}} \end{aligned}$ | 560.82 | 890.68 |

From Table 8.16, we can see that increases in faults are associated with increases in code size. This indicates that change of code size is an important factor to be considered. From Table 8.17 we can see that the environmental factor model seems to provide the best predictive power according to the SSE and AIC values. Other measures such as the testing effort and development cost are usually estimated based on code size. Therefore, code size is an important factor to be incorporated into the software reliability analysis.

Let $z_{c}$ denote the factor of changed code size as follows:

$$
z_{c}= \begin{cases}0 & \text { changed code } \leq 1,000 \mathrm{NLOC} \\ 1 & 1,000 \mathrm{NLOC}<\text { changed code } \leq 5,000 \mathrm{NLOC} \\ 2 & 5,000 \mathrm{NLOC}<\text { changed code } \leq 10,000 \mathrm{NLOC} \\ 3 & 10,000 \mathrm{NLOC}<\text { changed code }\end{cases}
$$

After carefully examining the failure data, we find that the failures occur with a much slower frequency after 1013.9 staff days of testing. Therefore, we use dataup to the 1013.9 staff-days to fit the models and estimate the parameters, and use calibrated model to predict the remaining data and compare the predictive power of software reliability models.

Similar to analysis of Application 2, the estimate of $\beta_{1}$ for our example is $\hat{\beta}_{1}=0.00567$ with $p$-value 0.048 , which indicates that this factor is significant to consider. The estimates of parameters in the baseline failure intensity function in equation (17) are as follows:

$$
\hat{a}=101.0, \hat{b}=0.004, \hat{\beta}=8.9, \hat{\alpha}=0.0148, \text { and } \hat{c}=803.5
$$

Table 8.17 lists the SSE and AIC values for the model comparison. From the results it is seen that the number of initial faults is $\hat{c}=804$ and the number of introduced faults is $\hat{a}=102$. Therefore, the number of total faults in the software is about 906. By the end of the software testing, 870 faults were detected, which implies that the number of residual faults is about 36 .

Table 8.16. Software testing data for application 3

| Staff <br> days | Faults | Code <br> size | $z$ | Staff <br> days | Faults | Code size | $z$ | Staff <br> days | Faults | Code size | $z$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | 0 | 0 | 0 | 207.2 | 97 | 213093 | 2 | 424.9 | 321 | 272457 | 1 |
| 4.8 | 0 | 16012 | 3 | 211.9 | 98 | 219248 | 2 | 434.2 | 326 | 273741 | 1 |
| 6 | 0 | 16012 | 3 | 217 | 105 | 221355 | 1 | 442.7 | 339 | 275025 | 1 |
| 14.3 | 7 | 32027 | 3 | 223.5 | 113 | 223462 | 1 | 451.4 | 346 | 276556 | 1 |
| 22.8 | 7 | 48042 | 3 | 227 | 113 | 225568 | 1 | 456.1 | 347 | 278087 | 1 |
| 32.1 | 7 | 58854 | 3 | 234.1 | 122 | 227675 | 1 | 460.8 | 351 | 279618 | 1 |
| 41.4 | 7 | 69669 | 3 | 241.6 | 129 | 229784 | 1 | 466 | 356 | 281149 | 1 |
| 51.2 | 11 | 80483 | 3 | 250.7 | 141 | 233557 | 1 | 472.3 | 359 | 283592 | 1 |
| 60.6 | 12 | 91295 | 3 | 259.8 | 155 | 237330 | 1 | 476.4 | 362 | 286036 | 1 |
| 70 | 13 | 102110 | 3 | 268.3 | 166 | 241103 | 1 | 480.9 | 367 | 288480 | 1 |
| 79.9 | 15 | 112925 | 3 | 277.2 | 178 | 244879 | 1 | 486.8 | 374 | 290923 | 1 |
| 91.3 | 20 | 120367 | 2 | 285.5 | 186 | 247946 | 1 | 495.8 | 376 | 293367 | 1 |
| 97 | 21 | 127812 | 2 | 294.2 | 190 | 251016 | 1 | 505.7 | 380 | 295811 | 1 |
| 107.7 | 22 | 135257 | 2 | 298 | 190 | 254086 | 1 | 516 | 392 | 298254 | 1 |
| 119.1 | 28 | 142702 | 2 | 305.2 | 195 | 257155 | 1 | 526.2 | 399 | 300698 | 1 |
| 127.6 | 40 | 150147 | 2 | 312.3 | 201 | 260225 | 1 | 527.3 | 401 | 300698 | 1 |
| 135.1 | 44 | 152806 | 1 | 318.2 | 209 | 260705 | 0 | 535.8 | 405 | 303142 | 1 |
| 142.8 | 46 | 155464 | 1 | 328.9 | 224 | 261188 | 0 | 546.3 | 415 | 304063 | 0 |
| 148.9 | 48 | 158123 | 1 | 334.8 | 231 | 261669 | 0 | 556.1 | 425 | 305009 | 0 |
| 156.6 | 52 | 160781 | 1 | 342.7 | 243 | 262889 | 0 | 568.1 | 440 | 305956 | 0 |
| 163.9 | 52 | 167704 | 2 | 350.5 | 252 | 263629 | 0 | 577.2 | 457 | 306902 | 0 |
| 169.7 | 59 | 174626 | 2 | 356.3 | 259 | 264367 | 0 | 578.3 | 457 | 306902 | 0 |
| 170.1 | 59 | 174626 | 2 | 360.6 | 271 | 265107 | 0 | 587.2 | 467 | 307849 | 0 |
| 174.7 | 63 | 181548 | 2 | 365.7 | 277 | 265845 | 0 | 595.5 | 473 | 308795 | 0 |
| 179.6 | 68 | 188473 | 2 | 386.5 | 290 | 267325 | 1 | 605.6 | 480 | 309742 | 0 |
| 185.5 | 71 | 194626 | 2 | 396.5 | 300 | 268607 | 1 | 613.9 | 491 | 310688 | 0 |
| 194 | 88 | 200782 | 2 | 408 | 310 | 269891 | 1 | 621.6 | 496 | 311635 | 0 |
| 200.3 | 93 | 206937 | 2 | 417.3 | 312 | 271175 | 1 | 623.4 | 496 | 311635 | 0 |Table 8.16. (continued)

| Staff <br> days | Faults | Code size | $z$ | Staff <br> days | Faults | Code size | $z$ | Staff <br> days | Faults | Code size | $z$ |
| :-- | :-- | :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 636.3 | 502 | 311750 | 0 | 938.3 | 710 | 330435 | 0 | 1231.6 | 842 | 333481 | 0 |
| 649.7 | 517 | 311866 | 0 | 952 | 720 | 330263 | 0 | 1240.9 | 844 | 333695 | 0 |
| 663.9 | 527 | 312467 | 0 | 965 | 729 | 330091 | 0 | 1249.5 | 845 | 333909 | 0 |
| 675.1 | 540 | 313069 | 0 | 967.7 | 729 | 330091 | 0 | 1262.2 | 849 | 335920 | 1 |
| 677.4 | 543 | 313069 | 0 | 968.6 | 731 | 330091 | 0 | 1271.3 | 851 | 337932 | 1 |
| 677.9 | 544 | 313069 | 0 | 981.3 | 740 | 329919 | 0 | 1279.8 | 854 | 339943 | 1 |
| 688.4 | 553 | 313671 | 0 | 997 | 749 | 329747 | 0 | 1281 | 854 | 339943 | 1 |
| 698.1 | 561 | 314273 | 0 | 1013.9 | 759 | 330036 | 0 | 1287.4 | 855 | 341955 | 1 |
| 710.5 | 573 | 314783 | 0 | 1030.1 | 776 | 330326 | 0 | 1295.1 | 859 | 341967 | 0 |
| 720.9 | 581 | 315294 | 0 | 1044 | 781 | 330616 | 0 | 1304.8 | 860 | 341979 | 0 |
| 731.6 | 584 | 315805 | 0 | 1047 | 782 | 330616 | 0 | 1305.8 | 865 | 342073 | 0 |
| 732.7 | 585 | 315805 | 0 | 1059.7 | 783 | 330906 | 0 | 1313.3 | 867 | 342168 | 0 |
| 733.6 | 585 | 315805 | 0 | 1072.6 | 787 | 331196 | 0 | 1314.4 | 867 | 342168 | 0 |
| 746.7 | 586 | 316316 | 0 | 1085.7 | 793 | 331486 | 0 | 1320 | 867 | 342262 | 0 |
| 761 | 598 | 316827 | 0 | 1098.4 | 796 | 331577 | 0 | 1325.3 | 867 | 342357 | 0 |
| 776.5 | 612 | 318476 | 1 | 1112.4 | 797 | 331669 | 0 | 1330.6 | 870 | 342357 | 0 |
| 793.5 | 621 | 320125 | 1 | 1113.5 | 798 | 331669 | 0 | 1334.2 | 870 | 342358 | 0 |
| 807.2 | 636 | 321774 | 1 | 1141.1 | 798 | 331669 | 0 | 1336.7 | 870 | 342358 | 0 |
| 811.8 | 639 | 321774 | 1 | 1128 | 802 | 331760 | 0 |  |  |  |  |
| 812.5 | 639 | 321774 | 1 | 1139.1 | 805 | 331852 | 0 |  |  |  |  |
| 829 | 648 | 323423 | 1 | 1151.4 | 811 | 331944 | 0 |  |  |  |  |
| 844.4 | 658 | 325072 | 1 | 1163.2 | 823 | 332167 | 0 |  |  |  |  |
| 860.5 | 666 | 326179 | 1 | 1174.3 | 827 | 332391 | 0 |  |  |  |  |
| 876.7 | 674 | 327286 | 1 | 1184.6 | 832 | 332615 | 0 |  |  |  |  |
| 892 | 679 | 328393 | 1 | 1198.3 | 834 | 332939 | 0 |  |  |  |  |
| 895.5 | 686 | 328393 | 1 | 1210.3 | 836 | 333053 | 0 |  |  |  |  |
| 910.8 | 690 | 329500 | 1 | 1221.1 | 839 | 333267 | 0 |  |  |  |  |
| 925.1 | 701 | 330608 | 1 | 1230.5 | 842 | 333481 | 0 |  |  |  |  |

Table 8.17. Model comparison

| Model name | SSE | AIC |
| :-- | --: | --: |
| G-O model | 240,773 | 1473.5 |
| Delayed S-shaped | 4,322 | 1422.6 |
| Inflexion S-shaped | 246,702 | 1481.5 |
| Yamada exponential | 230,955 | 1471.1 |
| Yamada Rayleigh | 8,824 | 1441.3 |
| Imperfect debugging (1) | 290,449 | 1491.7 |
| Imperfect debugging (2) | 364,398 | 1496.1 |
| PNZ model | 17,753 | 1441.7 |
| PZ model | 8,947 | 1436.5 |
| Environmental factor model | 1,182 | 1411.0 |# 8.9 Further Reading 

Some interesting research papers and book on this subject are, but not limited to:
Zhang X. and Pham, H., "An analysis of factors affecting software reliability," Journal of Systems and Software, 1999

Venkatesh, G. A. and Fischer, C. N., "SPARE: A development environment for program analysis algorithms, " IEEE Trans on Software Engineering, vol 18, no. 4, April 1992

Madhavji, N.H., "Environment Evolution: The Prism model of changes," IEEE Trans on Software Engineering, vol 18, no. 5, May 1992

### 8.10 Problems

1. Using the real-time control system as in Table 4.12 (data set \#8, Chapter 4), calculate the MLE for unknown parameters of the EPJM model discussed in Section 8.7.
2. Based on the first 60 days in Table 4.12 (data set \#8, Chapter 4), calculate the MLE for unknown parameters of the EPJM model.
3. Let us define a failure-cluster factor, such as

$$
z_{i}= \begin{cases}1 & \text { when } \frac{t_{i-1}}{t_{i}} \geq 10 \text { or } \frac{t_{i-1}}{t_{i}} \geq 12 \\ 0 & \text { otherwise }\end{cases}
$$

Using the software failure data set \#9 in Chapter 4, obtain the entire data set with the environmental factor variable $z_{i}$. Then estimate the two parameters, $N$ and $\phi$, of EPJM model.# Calibrating Software Reliability Models 

### 9.1 Introduction

Estimating software reliability measures that will be perceived by users is important in order to decide when to release software. Usually, software reliability models are applied to system test data with the hope of estimating the failure rate of the software in user environments. This chapter discusses recent methods and research on how to quantify the mismatch between the system test environment and the field environment based on recent studies (Zhang 2002; Teng 2001). The chapter also discusses a generalized random field environment (RFE) model incorporating both testing phase and operating phase in the software development cycle for estimating the reliability of software systems in the field. Examples are included to illustrate the calibrating software reliability model based on test data.

## Notation

$a(t) \quad$ Fault content function, i.e., total number of faults in the software including the initial and introduced faults
$b(t) \quad$ Fault detection rate function (faults per unit of time)
$b_{\text {test }} \quad$ Average per fault failure rate during system test interval
$b_{\text {field }} \quad$ Average per fault failure rate in the field
$\bar{b}_{\text {test }} \quad$ Long-term average per fault failure rate during system test interval
$\bar{b}_{\text {field }} \quad$ Long term average per fault failure rate in the field
$\lambda(t) \quad$ Failure intensity function (faults per unit of time)
$\bar{\lambda}(T) \quad$ Failure intensity representation based on system test data
K Calibration factor
$m(t) \quad$ Mean value function, i.e., the expected number of faults detected by time $t$
$N(t) \quad$ Number of detected faults by time $t$
$\bar{N}(t) \quad$ Number of residual faults by time $t$
$T \quad$ Duration of system test interval# 9.2 Calibration Factor Approach 

Let us assume that the system test ends at time $T$ and after that the software is delivered to the field. The expected number of faults detected and removed by time $T$ is $m(T)$. To account for the mismatch between the system test field environments, Zhang et al. (2002) recently proposed linking the error detection rate function $b(t)$ under the system test environment, say $b_{\text {test }}(t)$, to a different $b(t)$ under the field environment, say $b_{\text {field }}(t)$. Define

$$
\bar{b}_{\text {test }}=\lim _{T \rightarrow \infty} \frac{1}{T} \int_{0}^{T} b_{\text {test }}(t) d t
$$

Intuitively, $\bar{b}_{\text {test }}$ represents the long-term average per fault failure rate during system test. Using an analogous definition for $\bar{b}_{\text {field }}$, Zhang et al. (2002) defined the calibration factor as the ratio $K=\bar{b}_{\text {test }} / \bar{b}_{\text {field }}$. In the case where the system test and field environments are the same, $K$ will be unity.

Assuming that the fault detection rate, $b_{\text {test }}(t)$, for system test environments is given by

$$
b_{\text {test }}(t)=\frac{b_{\text {test }}}{1+\beta e^{-b_{\text {test }} t}}
$$

where $\beta$ represents a learning parameter and $b_{\text {test }}$ is the limiting value of the fault detection rate. Note that $\beta=0$ coincides with no learning, and the fault detection rate reduces to the constant value $b_{\text {test }}$.

## A General Approach (Zhang 2002)

Consider a context where only system test data is available for a release and it is desired to estimate the field failure rate of the software. Assume that system test and field data of the previous releases of the same product or similar product are also available from which a $K$ factor can be obtained. We suppose an NHPP SRGM model (see Chapter 6) has been fit to the system test data and the assumptions underlying GO model (i.e., no learning factor and no introduction of new faults) are adequately satisfied in the field environment. The software failure rate in the field can be estimated by the following steps:

1. Estimate the calibration factor $K$ from previous releases/projects.
2. Estimate the number of residual faults based on system test data, $\hat{\tilde{N}}(T)=\hat{a}(T)-$ $N(T)$, and the long-term average per fault failure rate $\bar{b}_{\text {test }}=\hat{b}_{\text {test }}$ from the system test data.
3. Calibrate the system test analysis to estimate the average per fault failure rate in the field using the calibration factor $K$. The average per fault failure rate in the field is estimated by $\hat{b}_{\text {field }}=\hat{b}_{\text {test }} / K$.4. Estimate the failure rate of the software in the field by incorporating the number of residual faults by the average per fault failure rate in the field. The field failure rate after $t$ system-hours of field exposure time is

$$
\hat{\lambda}_{\text {field }}(t)=\hat{\bar{N}}(T) \times \hat{b}_{\text {field }} \times e^{-\hat{b}_{\text {field } t}}=\hat{\bar{N}}(T) \times \frac{\hat{b}_{\text {test }}}{K} \times e^{-\frac{\hat{b}_{\text {test }}}{K} t}
$$

# 9.3 Model Application 

Consider two systems test data, shown in Table 9.1 and 9.2 where System 1 is a high-capacity data transmission system and System 2 is a flexible signal multiplexing and transmission system (Zhang 2002). The interesting question here is, by comparing the analyses of the system test and field data, how can one calculate the value of the calibration factor $K$ for each project. In other words, it is interesting to show, in general, how projects can calibrate their system test data analyses to make them applicable to field environments.

Assume the mean value function (Pham 1997a) is given by

$$
m(t)=\frac{1}{\left(1+\beta \mathrm{e}^{-\mathrm{b}_{\text {test } t}}\right)}\left[(c+a)\left(1-e^{-b_{\text {test } t}}\right)-\frac{a b_{\text {test }}}{b_{\text {test }}-\alpha}\left(e^{-\alpha t}-e^{-b_{\text {test } t}}\right)\right]
$$

The parameter $\alpha$ represents the fault introduction rate and $\beta$ is the learning parameter. Table 9.3 lists the estimates of these parameters for both System 1 and System 2. See Zhang (2002) for details. Note that the estimates of $c$ and $a$ are shown as normalized values, defined as the ratio between the parameter estimates and the actual number of total faults.

## Calculation of the Calibration Factor

The GO model was fit to the field data of both System 1 and System 2. Table 9.4 shows the estimates of the average per fault failure in the field, $b_{\text {field }}$, and the longterm average per fault failure rate in system test, $\bar{b}_{\text {test }}=b_{\text {test }}$, for each system. The analyses of the two data sets presented in this section provide a means to estimate the calibration factor $K$. According to Section 2, the ratio of $b_{\text {test }}$ to $b_{\text {field }}$ gives an empirical observation of $K$. The value of $K$ for System 1 and System 2 are 34.32 and 49.20 respectively.Table 9.1. System 1 normalized data

| Time | Cumulative <br> faults | Estimated <br> faults | Time | Cumulative <br> faults | Estimated <br> faults |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | 0 | 0 | 0.508197 | 0.863014 | 0.859464 |
| 0.016393 | 0.020548 | 0.019882 | 0.52459 | 0.881849 | 0.873735 |
| 0.032787 | 0.054795 | 0.041306 | 0.540984 | 0.900685 | 0.886763 |
| 0.04918 | 0.07363 | 0.064295 | 0.557377 | 0.913527 | 0.898626 |
| 0.065574 | 0.104452 | 0.088856 | 0.57377 | 0.922089 | 0.909404 |
| 0.081967 | 0.129281 | 0.114968 | 0.590164 | 0.928938 | 0.919174 |
| 0.098361 | 0.15839 | 0.142591 | 0.606557 | 0.934932 | 0.928016 |
| 0.114754 | 0.184075 | 0.171656 | 0.622951 | 0.941781 | 0.936002 |
| 0.131148 | 0.217466 | 0.202065 | 0.639344 | 0.943493 | 0.943205 |
| 0.147541 | 0.236301 | 0.233693 | 0.655738 | 0.951199 | 0.949693 |
| 0.163934 | 0.26113 | 0.266387 | 0.672131 | 0.961473 | 0.955529 |
| 0.180328 | 0.302226 | 0.299971 | 0.688525 | 0.97089 | 0.960772 |
| 0.196721 | 0.345034 | 0.334243 | 0.704918 | 0.973459 | 0.965479 |
| 0.213115 | 0.374144 | 0.368986 | 0.721311 | 0.976884 | 0.969699 |
| 0.229508 | 0.385274 | 0.40397 | 0.737705 | 0.980308 | 0.973481 |
| 0.245902 | 0.40411 | 0.438958 | 0.754098 | 0.983733 | 0.976867 |
| 0.262295 | 0.440925 | 0.473712 | 0.770492 | 0.983733 | 0.979897 |
| 0.278689 | 0.482877 | 0.508004 | 0.786885 | 0.983733 | 0.982607 |
| 0.295082 | 0.53339 | 0.541613 | 0.803279 | 0.987158 | 0.985029 |
| 0.311475 | 0.594178 | 0.57434 | 0.819672 | 0.988014 | 0.987192 |
| 0.327869 | 0.614726 | 0.606006 | 0.836066 | 0.98887 | 0.989125 |
| 0.344262 | 0.651541 | 0.636458 | 0.852459 | 0.98887 | 0.99085 |
| 0.360656 | 0.672089 | 0.665569 | 0.868852 | 0.990582 | 0.992389 |
| 0.377049 | 0.684075 | 0.693241 | 0.885246 | 0.994007 | 0.993763 |
| 0.393443 | 0.711473 | 0.719405 | 0.901639 | 0.994007 | 0.994987 |
| 0.409836 | 0.732021 | 0.744017 | 0.918033 | 0.994863 | 0.99608 |
| 0.42623 | 0.75 | 0.767059 | 0.934426 | 0.995719 | 0.997054 |
| 0.442623 | 0.77226 | 0.788535 | 0.95082 | 0.995719 | 0.997922 |
| 0.459016 | 0.789384 | 0.808468 | 0.967213 | 0.997432 | 0.998696 |
| 0.47541 | 0.809932 | 0.826897 | 0.983607 | 0.998288 | 0.999385 |
| 0.491803 | 0.84161 | 0.843875 | 1 | 1 | 1 |
|  |  |  |  |  |  |

# 9.4 Calibrating Models with Random Field Environments 

Many existing NHPP software reliability models have been carried out through the fault intensity rate function and the mean value functions $m(t)$ within a controlled operating environment. Generally, these models are applied to the software testing data and then used to make predictions on the software failures and reliability in the field. The operating environments in the field for the software are perhaps quite different. The randomness of the field environment will affect the software failure and software reliability in an unpredictable way.Table 9.2. System 2 normalized data

| Time | Cumulative <br> faults | Estimated <br> faults | Time | Cumulative <br> faults | Estimated <br> faults |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | 0 | 0 | 0.512821 | 0.639547 | 0.688351 |
| 0.025641 | 0.019567 | 0.023097 | 0.538462 | 0.677652 | 0.719633 |
| 0.051282 | 0.052523 | 0.0481 | 0.564103 | 0.720906 | 0.74906 |
| 0.076923 | 0.07415 | 0.07503 | 0.589744 | 0.742533 | 0.776578 |
| 0.102564 | 0.102987 | 0.103878 | 0.615385 | 0.764161 | 0.802168 |
| 0.128205 | 0.125644 | 0.134602 | 0.641026 | 0.786818 | 0.825843 |
| 0.153846 | 0.161689 | 0.167122 | 0.666667 | 0.797116 | 0.847641 |
| 0.179487 | 0.189495 | 0.201317 | 0.692308 | 0.814624 | 0.867624 |
| 0.205128 | 0.22863 | 0.237027 | 0.717949 | 0.830072 | 0.885868 |
| 0.230769 | 0.255407 | 0.274051 | 0.74359 | 0.840371 | 0.902465 |
| 0.25641 | 0.294542 | 0.312152 | 0.769231 | 0.851699 | 0.917511 |
| 0.282051 | 0.329557 | 0.351062 | 0.794872 | 0.863028 | 0.931111 |
| 0.307692 | 0.369722 | 0.390487 | 0.820513 | 0.865088 | 0.943369 |
| 0.333333 | 0.399588 | 0.430118 | 0.846154 | 0.888774 | 0.954391 |
| 0.358974 | 0.427394 | 0.469639 | 0.871795 | 0.898043 | 0.96428 |
| 0.384615 | 0.46344 | 0.508738 | 0.897436 | 0.935118 | 0.973134 |
| 0.410256 | 0.495366 | 0.547116 | 0.923077 | 0.950566 | 0.981047 |
| 0.435897 | 0.526262 | 0.584495 | 0.948718 | 0.966014 | 0.988108 |
| 0.461538 | 0.543769 | 0.620629 | 0.974359 | 0.971164 | 0.9944 |
| 0.487179 | 0.593203 | 0.655305 | 1 | 1 | 1 |

Table 9.3. Parameter estimation for Systems 1 and 2

| Parameter | System 1 | System 2 |
| :-- | :-- | :-- |
| (Normalized) initial faults $\hat{c}$ | 0.987 | 0.912 |
| (Normalized) introduced faults $\hat{a}$ | 0.015 | 0.093 |
| Average per fault failure rate $\hat{b}_{\text {test }}$ | 0.11667 | 0.12650 |
| Fault introduction parameter $\hat{\alpha}$ | $9.4 \times 10^{-5}$ | $9.82 \times 10^{-6}$ |
| Learning parameter $\hat{\beta}$ | 5.13 | 4.956 |

Table 9.4. The calibration factor for Systems 1 and 2

|  | System 1 |  | System 2 |  |
| :-- | :-- | :-- | :-- | :-- |
| Parameter | System <br> test | Field | System <br> test | Field |
| Average per fault <br> failure rate | 0.1167 | 0.0034 | 0.1265 | 0.00257 |
| Calibration factor, $K$ | 34.32 |  | 49.20 |  |

In previous sections, we discuss an NHPP software reliability calibration model by considering a calibration factor. This section discusses a model based onNHPP model framework for predicting software failures and evaluating the software reliability subject to the random field environments.

Notation

| $R(t)$ | Software reliability function |
| :--: | :--: |
| $\eta$ | Random environmental factor |
| $G(\eta)$ | Cumulative distribution function of $\eta$ |
| $\gamma$ | Shape parameter of Gamma distributions |
| $\theta$ | Scale parameter of Gamma distributions |
| $\alpha, \beta$ | Parameters of Beta distributions |
| $N(t)$ | Counting process which counts the number of software failures discovered by time $t$ |
| $m(t)$ | Expected number of software failures detected by time $t$ |
| $a(t)$ | Expected number of initial software faults plus introduced faults by time $t$ |
| $m_{1}(t)$ | Expected number of software failures in testing by time $t$ |
| $m_{2}(t)$ | Expected number of software failures in the field by time $t$ |
| $a_{1}(t)$ | Expected number of initial software faults plus introduced faults discovered in the testing by time $t$ |
| $a$ | Number of initial software faults at the beginning of testing phase, is a software parameter that is directly related to the software itself |
| $T$ | Time to stop testing and release the software for field operations |
| $a_{F}$ | number of initial software faults in the field (at time $T$ ) |
| $b(t)$ | Failure detection rate per fault at time $t$, is a process parameter that is directly related to testing and failure process |
| $p$ | Probability that a fault will be successfully removed from the software |
| $q$ | Error introduction rate at time $t$ in the testing phase |
| RFE-model | Software reliability model subject to a random field environment |
| $\gamma$-RFE | Software reliability model with a Gamma distributed field environment |
| $\beta$-RFE | Software reliability model with a Beta distributed field environment |

# 9.4.1 A Generalized Random Field Environmental Model 

A generalized NHPP model can be formulated as follows (Zhang 2003):

$$
\begin{aligned}
& m^{\prime}(t)=\eta \cdot b(t) \cdot(a(t)-p \cdot m(t)) \\
& a^{\prime}(t)=q \cdot m^{\prime}(t)
\end{aligned}
$$

where $m(t)$ is the expected number of software failures to be detected by time $t$. If the marginal conditions are given as $m(0)=0$ and $a(0)=a$, then for a specificenvironmental factor $\eta$, the solutions to equations (9.5) and (9.6) can be obtained as follows:

$$
\begin{gathered}
m_{\eta}(t)=a \int_{0}^{t} \eta b(u) e^{-\int_{0}^{u} \eta(p-q) b(\tau) d \tau} d u \\
a_{\eta}(t)=a\left(1+\int_{0}^{t} \eta q b(u) e^{-\int_{0}^{t} \eta(p-q) b(\tau) d \tau} d u\right)
\end{gathered}
$$

Figure 9.1 shows the last two phases of the software life cycle: in-house testing and field operation. If $T$ is the time to stop testing and release the software for field operations, then the time period $0 \leq t \leq T$ refers to the time period of Software Testing, while the time period $T \leq t$ refers to the post release period - Field Operation.


Figure 9.1. Testing $v s$ field environment where $T$ is the time to stop testing

The environmental factor $\eta$ is used to capture the uncertainty about the environment and its effects upon the software failure rate. In general, the software testing is carried out in a controlled environment with very small variations, which can be used as a referenced environment where $\eta$ is constant and equal to 1 . For the field operating environment, the environmental factor $\eta$ is assumed to be a nonnegative random variable with probability density function (pdf) $f(\eta)$, i.e.

$$
\eta= \begin{cases}1 & t \leq T \\ \text { r.v. with pdf } f(\eta) & t \geq T\end{cases}
$$

If the value of $\eta$ is less than 1 , it indicates that the condition is less favorable to fault detection than that of testing environment. Likewise, if the value of $\eta$ is greater than 1 , it indicates that the condition is more favorable to fault detection than that of testing environment.

From equations (9.7) and (9.9), the mean value function and the function $a_{1}(t)$ during testing can be obtained as

$$
\begin{aligned}
& m_{1}(t)=a \int_{0}^{t} b(u) e^{-\int_{0}^{u}(p-q) b(\tau) d \tau} d u \\
& t \leq T \\
& a_{1}(t)=a\left(1+\int_{0}^{t} q b(u) e^{-\int_{0}^{t}(p-q) b(\tau) d \tau} d u\right) \quad t \leq T
\end{aligned}
$$

For the field operation, where $t \geq T$, the mean value function can be represented as$$
\begin{aligned}
m_{2}(t) & =m_{1}(T)+\int_{0}^{\infty} m_{\eta}(t) f(\eta) d \eta \\
& =m_{1}(T)+\int_{0}^{\infty}\left(a_{F} \int_{T}^{t} \eta b(u) e^{-\int_{T}^{u} \eta(p-q) b(\tau) d \tau} d u\right) f(\eta) d \eta \\
& =m_{1}(T)+\int_{T}^{t} a_{F} b(u)\left(\int_{0}^{\infty} \eta e^{-\eta \int_{T}^{t}(p-q) b(\tau) d \tau} f(\eta) d \eta\right) d u
\end{aligned}
$$

where $a_{F}$ is number of faults in the software at time $T$. Using the Laplace transform formula, the mean value function can be rewritten as

$$
\begin{aligned}
m_{2}(t) & =m_{1}(T)+\left.\int_{T}^{t} a_{F} b(u)\left(-\frac{d F^{*}(s)}{d s}\right|_{\left.s=\int_{u}^{u}(p-q) b(\tau) d \tau\right)}\right) d u \\
& =m_{1}(T)+\frac{a_{F}}{(p-q)} \int_{T}^{t}\left(-d F^{*}\left((p-q) \int_{T}^{u} b(\tau) d \tau\right)\right)
\end{aligned}, t \geq T
$$

where $F^{*}(s)$ is the Laplace transform of the $\operatorname{pdf} f(x)$ and

$$
\int_{0}^{\infty} x \cdot e^{-x \cdot s} \cdot f(x) d x=-\frac{d F^{*}(s)}{d s}
$$

or, equivalently,

$$
\begin{aligned}
m_{2}(t) & =m_{1}(T)-\left.\frac{a_{F}}{p-q} F^{*}\left((p-q) \int_{T}^{u} b(\tau) d \tau\right)\right|_{T} ^{t} \\
& =m_{1}(T)+\frac{a_{F}}{p-q}\left(F^{*}(0)-F^{*}\left((p-q) \int_{T}^{t} b(\tau) d \tau\right)\right), \quad t \geq T
\end{aligned}
$$

Notice that $F^{*}(0)=\int_{0}^{\infty} e^{-0 x} f(x) d x=1$, then

$$
m_{2}(t)=m_{1}(T)+\frac{a_{F}}{p-q}\left(1-F^{*}\left((p-q) \int_{T}^{t} b(\tau) d \tau\right)\right) \quad t \geq T
$$

The expected number of faults in the software at time $T$ is given by

$$
\begin{aligned}
a_{F} & =a_{1}(T)-p m_{1}(T) \\
& =a\left(1-\int_{0}^{t}(p-q) b(u) e^{-\int_{0}^{t}(p-q) b(\tau) d \tau} d u\right) \\
& =a e^{-\int_{0}^{t}(p-q) \cdot b(\tau) d \tau}
\end{aligned}
$$

The generalized RFE model can be obtained as$$
m(t)=\left\{\begin{array}{lr}
\frac{a}{p-q}\left(1-e^{-(p-q) \int_{t_{0}}^{t} b(\tau) d \tau}\right) & t \leq T \\
\frac{a}{p-q}\left(1-e^{-(p-q) \int_{t_{0}}^{t} b(\tau) d \tau} F^{\mathbb{R}}\left((p-q) \int_{T}^{t} b(\tau) d \tau\right)\right) & t \geq T
\end{array}\right.
$$

This model in equation (9.12) is a generalized software reliability model subject to random field environments. The next section presents specific RFE models for the Gamma and beta distributions of the random field environmental factor $\eta$.

# 9.4.2 RFE Reliability Models 

This section discusses two specific models. The first model is a $\gamma$-RFE model based on Gamma distribution which can be used to evaluate and predict software reliability in the field environments where software failure detection rate can be either greater or less than the failure detection rate in the testing environment. The second model is a $\beta$-RFE model based on Beta distribution which can be used to predict software reliability in the field environments where the software failure detection rate can only be less than the failure detection rate in the testing environment.

## Gamma Model

In this model, we use the Gamma distribution to describe the random environmental factor $\eta$. This model is called $\gamma$-RFE model.

Assume $\eta$ follows a Gamma distribution with a probability density function as follows:

$$
f_{\gamma}(\eta)=\frac{\theta^{\gamma} \cdot \eta^{\gamma-1} \cdot e^{-\theta \cdot \eta}}{\Gamma(\gamma)}, \quad \gamma, \theta>0 ; \eta \geq 0
$$

Figure 9.2 shows an example of the Gamma density probability function. The Gamma function seems to be a reasonable to describe a software failure process in those field environments where the software failure detection rate can be either greater (i.e., $\eta>1$ ) or less than (i.e., $\eta<1$ ) the failure detection rate in the testing environment.


Figure 9.2. A Gamma density functionThe Laplace transform of the probability density function in equation (9.13) is

$$
F^{+}(s)=\left[\frac{\theta}{\theta+s}\right]^{r}
$$

Assume that the error detection rate function $b(t)$ is given by

$$
b(t)=\frac{b}{1+c \cdot e^{-b \cdot t}}
$$

where $b$ is the asymptotic unit software failure detection rate and $c$ is the parameter defining the shape of the learn curve, then from equation (9.12) the mean value function of $\gamma$-RFE model can be obtained as follows:

$$
m_{\gamma}(t)=\left\{\begin{array}{lr}
\frac{a}{(p-q)}\left(1-\left(\frac{1+c}{e^{b t}+c}\right)^{p-q}\right) & t \leq T \\
\frac{a}{p-q}\left(1-\left(\frac{1+c}{e^{b T}+c}\right)^{p-q}\left(\frac{\theta}{\theta+(p-q) \ln \left(\frac{c+e^{b t}}{c+e^{b T}}\right)}\right)^{r}\right) & t \geq T
\end{array}\right.
$$

# Beta Model 

Similary, we use the Beta distribution to describe the random environmental factor $\eta$, which is called $\beta$-RFE model. The Beta pdf is

$$
f_{\beta}(\eta)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} \eta^{\alpha-1}(1-\eta)^{\beta-1} \quad 0 \leq \eta \leq 1, \alpha>0, \beta>0
$$

Figure 9.3 shows an example of the Beta density function. It seems that the $\beta$-RFE model is a reasonable function to describe a software failure process in those field environments where the software failure detection rate can only be less than the failure detection rate in the testing environment. This is not uncommon in the software industry because, during the software testing, the engineers generally test the software intensely and conduct an "accelerated" test on the software in order to detect most of the software faults as early as possible.


Figure 9.3. A pdf curve of Beta distributionThe Laplace transform of the pdf in equation (9.17) is

$$
F_{\beta}^{*}(s)=e^{-s} \cdot H G([\beta],[\alpha+\beta], s)
$$

where $H G([\beta],[\alpha+\beta], s)$ is a generalized hypergeometric function such that

$$
H G\left(\left[a_{1}, a_{2}, \ldots, a_{m}\right],\left[b_{1}, b_{2}, \ldots, b_{n}\right], s\right)=\sum_{k=0}^{\infty}\left[\frac{s^{k} \prod_{i=1}^{m} \frac{\Gamma\left(a_{i}+k\right)}{\Gamma\left(a_{i}\right)}}{\prod_{i=1}^{n} \frac{\Gamma\left(b_{i}+k\right)}{\Gamma\left(b_{i}\right)} k!}\right]
$$

Therefore

$$
\begin{aligned}
F_{\beta}^{*}(s) & =e^{-s} \sum_{k=0}^{\infty}\left[\frac{\Gamma(\alpha+\beta) \Gamma(\beta+k) s^{k}}{\Gamma(\beta) \Gamma(\alpha+\beta+k) k!}\right] \\
& =\sum_{k=0}^{\infty}\left[\frac{\Gamma(\alpha+\beta) \Gamma(\beta+k)}{\Gamma(\beta) \Gamma(\alpha+\beta+k)} \cdot \frac{s^{k} e^{-s}}{k!}\right] \\
& =\sum_{k=0}^{\infty}\left[\frac{\Gamma(\alpha+\beta) \Gamma(\beta+k)}{\Gamma(\beta) \Gamma(\alpha+\beta+k)} \cdot P(k, s)\right]
\end{aligned}
$$

where $P(k, s)$ is a Poisson probability density function as follows:

$$
P(k, s)=\frac{s^{k} e^{-s}}{k!}
$$

Using the same error detection rate function as in equation (9.15) and replacing $F^{*}(s)$ by $F_{\beta}^{*}(s)$, the mean value function of the $\beta$-RFE model is

$$
m_{\beta}(t)=\left\{\begin{array}{lr}
\frac{a}{(p-q)}\left(1-\left(\frac{1+c}{e^{b t}+c}\right)^{p-q}\right) & t \leq T \\
\frac{a}{p-q}\left(1-\left(\frac{1+c}{e^{b T}+c}\right)^{p-q} \sum_{k=0}^{\infty}\left[\frac{\Gamma(\alpha+\beta) \Gamma(\beta+k) \mathrm{P}(k, s)}{\Gamma(\beta) \Gamma(\alpha+\beta+k)}\right]\right) t \geq T
\end{array}\right.
$$

where

$$
s=(p-q)\left(\ln \left(\frac{c+e^{b t}}{c+e^{b T}}\right)\right)
$$

# 9.4.3 Applications 

This section discusses the parameter estimation and illustrates the applications of the two random field environment software reliability models using a software failure data. In this analysis, the error removal efficiency $p$ is given. Each model has five unknown parameters. For example, in the $\gamma$-RFE model we need to estimate the following five unknown parameters: $a, b, q, \gamma$ and $\theta$. For the $\beta$-RFE model, we will estimate $a, b, q, \alpha$ and $\beta$.

Table 9.5 shows a set of failure data from a telecommunication software application during software testing. The column "Time" shows the normalizedcumulative time spent in software testing for this telecommunication application, and the column "Failures" shows the normalized cumulative number of failures occurred in the testing period up to the given time.

Table 9.5. Normalized cumulative failures and times during software testing

| Time | Failures | Time | Failures | Time | Failures |
| :-- | :--: | :--: | :--: | :--: | :--: |
| 0.0001 | 0.0249 | 0.0038 | 0.3483 | 0.0121 | 0.6766 |
| 0.0002 | 0.0299 | 0.0044 | 0.3532 | 0.0128 | 0.7015 |
| 0.0002 | 0.0647 | 0.0048 | 0.3682 | 0.0135 | 0.7363 |
| 0.0003 | 0.0647 | 0.0053 | 0.3881 | 0.0142 | 0.7761 |
| 0.0005 | 0.1095 | 0.0058 | 0.4478 | 0.0147 | 0.7761 |
| 0.0006 | 0.1194 | 0.0064 | 0.4876 | 0.0155 | 0.8159 |
| 0.0008 | 0.1443 | 0.0070 | 0.5224 | 0.0164 | 0.8259 |
| 0.0012 | 0.1692 | 0.0077 | 0.5473 | 0.0172 | 0.8408 |
| 0.0016 | 0.1990 | 0.0086 | 0.5821 | 0.0176 | 0.8458 |
| 0.0023 | 0.2289 | 0.0095 | 0.6119 | 0.0180 | 0.8756 |
| 0.0028 | 0.2637 | 0.0105 | 0.6368 | 0.0184 | 0.8955 |
| 0.0033 | 0.3134 | 0.0114 | 0.6468 | $\underline{0.0184}$ | 0.9005 |

The time to stop testing is at $T=0.0184$. After the time $T$, the software is released for field operations. Table 9.6 shows the field data for this software release. Similarly, the column "Time" shows the normalized cumulative time spent in the field for this software application, and the time in Table 9.6 is continued from the time to stop testing $T$. The column "Failures" shows the normalized cumulative number of failures found after releasing the software for field operations up to the given time. The cumulative number of failures is the total number of software failures since the beginning of software testing.

Let us assume that testing engineers have number of years experience in this particular product and software development skills and therefore conducted a perfect debugging during the test. In other words, $p=1$. We also assume that the constant value c in equation (9.11) is zero. The MLEs (see Chapter 6) of all the parameters in the $\gamma$-RFE model are obtained as shown in Table 9.7.

Similarly, set $p=1$, the MLE of all parameters in $\beta$-RFE model are obtained as shown in Table 9.8. For both RFE models, the MLE results can be used to obtain more insightful information about the software development process. In this example, at the time to stop testing the software $T=0.0184$, the estimated number of remaining faults in the system is $a_{F}=a-(p-q) \cdot m(T)=55$.

After we obtain the MLEs for all parameters, we can plot the mean value function fitting curves for both $\gamma$-RFE model and $\beta$-RFE model based on MLE parameters against the actual software application failures. Table 9.9 shows the mean value function fitting curves for both the models where the column $m_{p}(t)$ and $m_{\beta}(t)$ show the mean value function for $\gamma$-RFE model and $\beta$-RFE model, respectively.Table 9.6. Normalized cumulative failures and their times in operation

| Time | Failures | Time | Failures | Time | Failures |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0.0431 | 0.9055 | 0.3157 | 0.9751 | 0.7519 | 0.9900 |
| 0.0616 | 0.9104 | 0.3407 | 0.9751 | 0.7585 | 0.9900 |
| 0.0801 | 0.9204 | 0.3469 | 0.9751 | 0.7718 | 0.9900 |
| 0.0863 | 0.9254 | 0.3967 | 0.9751 | 0.7983 | 0.9900 |
| 0.1357 | 0.9303 | 0.4030 | 0.9801 | 0.8251 | 0.9900 |
| 0.1419 | 0.9353 | 0.4291 | 0.9851 | 0.8453 | 0.9900 |
| 0.1666 | 0.9453 | 0.4357 | 0.9851 | 0.8520 | 0.9900 |
| 0.2098 | 0.9453 | 0.4749 | 0.9851 | 0.9058 | 0.9900 |
| 0.2223 | 0.9502 | 0.5011 | 0.9851 | 0.9126 | 0.9900 |
| 0.2534 | 0.9502 | 0.5338 | 0.9851 | 0.9193 | 0.9900 |
| 0.2597 | 0.9502 | 0.5731 | 0.9851 | 0.9395 | 0.9950 |
| 0.2659 | 0.9502 | 0.6258 | 0.9900 | 0.9462 | 0.9950 |
| 0.2721 | 0.9552 | 0.6656 | 0.9900 | 0.9529 | 1.0000 |
| 0.2971 | 0.9602 | 0.6789 | 0.9900 | 0.9865 | 1.0000 |
| 0.3033 | 0.9701 | 0.7253 | 0.9900 | 1.0000 | 1.0000 |

The $\gamma$-RFE and $\beta$-RFE models yield very close fittings and predictions on software failures. Figure 9.4 shows the mean value function fitting curves of both the $\gamma$-RFE model and $\beta$-RFE model. Both models appear to be a good fit for a given data set. Figure 9.5 plots the detailed mean value fitting curves for both $\gamma$ RFE model and $\beta$-RFE model in the field operation.

For the overall fitting of the mean value function against the actual software failures, the MSE is 23.63 for $\gamma$-RFE model fitting, and is 23.69 for $\beta$-RFE model. Figure 9.6 shows the comparisons of mean value function fitting curves between the two RFE models and some existing NHPP software reliability models such as Goel-Okumoto and delayed S-shaped models (see Chapter 6). It appeared that those two models with considerations of the field environments on the software failure detection rate provide much better in term of predictions on the software failures in the field.

Table 9.7. MLE solutions for the $\gamma$-RFE model

| $\hat{a}$ | $\hat{b}$ | $\hat{q}$ | $\hat{\gamma}$ | $\hat{\theta}$ |
| :-- | :-- | :-- | :-- | :-- |
| 236.58 | 0.00144 | 0 | 0.2137 | 10.713 |Table 9.8. MLE solutions for the $\beta$-RFE model

| $\hat{a}$ | $\hat{b}$ | $\hat{q}$ | $\hat{\alpha}$ | $\hat{\beta}$ |
| :--: | :--: | :--: | :--: | :--: |
| 236.07 | 0.00145 | 0 | 0.1862 | 8.6922 |

Once MLEs of all parameters in equations (9.16) and (9.19) are obtained, the software reliability within $(T, T+x)$ can be determined as

$$
R(x \mid T)=e^{-(m(T+x)-m(T))}
$$

Let $\mathrm{T}=0.0184$, and change $x$ from 0 to 0.001 ; then we can examine reliability predictions between two RFE models and some other NHPP models which assume constant failure detection rate for both software testing and operation. The reliability prediction curves are shown in Figure 9.7.

# Confidence Interval 

Case 1: $\gamma$-RFE model. In this section we construct confidence intervals for the prediction on software reliability in the random field environments. From Tables 9.4 and 9.5 , if $p=1, c=0$ and $q=0$, then the model in equation (9.16) becomes

$$
m(t)= \begin{cases}a\left(1-e^{-b \cdot t}\right) & t \leq T \\ a\left(1-e^{-b \cdot T} \cdot\left(\frac{\theta}{\theta+b \cdot(t-T)}\right)^{\gamma}\right) & t \geq T\end{cases}
$$

To obtain the confidence interval for the reliability predictions for $\gamma$-RFE model, we can derive the variance-covariance matrix for all the MLEs. If we use $x_{i}, i=1,2,3$, and 4 to denote all parameters in the model,

$$
x_{1} \rightarrow a \quad x_{2} \rightarrow b \quad x_{3} \rightarrow \theta \quad x_{4} \rightarrow \gamma
$$Table 9.9. The mean value functions for both RFEs models

| Time | Failures | $m_{\mathrm{r}}(t)$ | $m_{\beta}(t)$ | Time | Failures | $m_{\mathrm{r}}(t)$ | $m_{\beta}(t)$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1357 | 0.9303 | 0.9340 | 0.9341 |
| 0.0001 | 0.0249 | 0.0085 | 0.0085 | 0.1419 | 0.9353 | 0.9352 | 0.9354 |
| 0.0002 | 0.0299 | 0.0152 | 0.0152 | 0.1666 | 0.9453 | 0.9398 | 0.9399 |
| 0.0002 | 0.0647 | 0.0219 | 0.0219 | 0.2098 | 0.9453 | 0.9469 | 0.9467 |
| 0.0003 | 0.0647 | 0.0302 | 0.0302 | 0.2223 | 0.9502 | 0.9487 | 0.9485 |
| 0.0005 | 0.1095 | 0.0466 | 0.0467 | 0.2534 | 0.9502 | 0.9530 | 0.9525 |
| 0.0006 | 0.1194 | 0.0547 | 0.0548 | 0.2597 | 0.9502 | 0.9538 | 0.9533 |
| 0.0008 | 0.1443 | 0.0708 | 0.0709 | 0.2659 | 0.9502 | 0.9545 | 0.9540 |
| 0.0012 | 0.1692 | 0.1023 | 0.1025 | 0.2721 | 0.9552 | 0.9553 | 0.9547 |
| 0.0016 | 0.1990 | 0.1404 | 0.1406 | 0.2971 | 0.9602 | 0.9582 | 0.9575 |
| 0.0023 | 0.2289 | 0.1915 | 0.1917 | 0.3033 | 0.9701 | 0.9589 | 0.9582 |
| 0.0028 | 0.2637 | 0.2332 | 0.2335 | 0.3157 | 0.9751 | 0.9603 | 0.9594 |
| 0.0033 | 0.3134 | 0.2667 | 0.2670 | 0.3407 | 0.9751 | 0.9628 | 0.9618 |
| 0.0038 | 0.3483 | 0.3053 | 0.3056 | 0.3469 | 0.9751 | 0.9635 | 0.9624 |
| 0.0044 | 0.3532 | 0.3422 | 0.3426 | 0.3967 | 0.9751 | 0.9681 | 0.9667 |
| 0.0048 | 0.3682 | 0.3718 | 0.3721 | 0.4030 | 0.9801 | 0.9686 | 0.9672 |
| 0.0053 | 0.3881 | 0.4003 | 0.4007 | 0.4291 | 0.9851 | 0.9708 | 0.9692 |
| 0.0058 | 0.4478 | 0.4332 | 0.4336 | 0.4357 | 0.9851 | 0.9713 | 0.9697 |
| 0.0064 | 0.4876 | 0.4648 | 0.4651 | 0.4749 | 0.9851 | 0.9743 | 0.9725 |
| 0.0070 | 0.5224 | 0.4998 | 0.5002 | 0.5011 | 0.9851 | 0.9761 | 0.9742 |
| 0.0077 | 0.5473 | 0.5332 | 0.5335 | 0.5338 | 0.9851 | 0.9783 | 0.9762 |
| 0.0086 | 0.5821 | 0.5772 | 0.5775 | 0.5731 | 0.9851 | 0.9808 | 0.9785 |
| 0.0095 | 0.6119 | 0.6205 | 0.6208 | 0.6258 | 0.9900 | 0.9839 | 0.9813 |
| 0.0105 | 0.6368 | 0.6600 | 0.6602 | 0.6656 | 0.9900 | 0.9860 | 0.9833 |
| 0.0114 | 0.6468 | 0.6953 | 0.6955 | 0.6789 | 0.9900 | 0.9867 | 0.9839 |
| 0.0121 | 0.6766 | 0.7210 | 0.7211 | 0.7253 | 0.9900 | 0.9890 | 0.9860 |
| 0.0128 | 0.7015 | 0.7479 | 0.7479 | 0.7519 | 0.9900 | 0.9902 | 0.9871 |
| 0.0135 | 0.7363 | 0.7684 | 0.7684 | 0.7585 | 0.9900 | 0.9905 | 0.9874 |
| 0.0142 | 0.7761 | 0.7924 | 0.7924 | 0.7718 | 0.9900 | 0.9911 | 0.9879 |
| 0.0147 | 0.7761 | 0.8050 | 0.8049 | 0.7983 | 0.9900 | 0.9923 | 0.9890 |
| 0.0155 | 0.8159 | 0.8294 | 0.8292 | 0.8251 | 0.9900 | 0.9934 | 0.9900 |
| 0.0164 | 0.8259 | 0.8522 | 0.8520 | 0.8453 | 0.9900 | 0.9943 | 0.9908 |
| 0.0172 | 0.8408 | 0.8713 | 0.8710 | 0.8520 | 0.9900 | 0.9945 | 0.9910 |
| 0.0176 | 0.8458 | 0.8804 | 0.8801 | 0.9058 | 0.9900 | 0.9966 | 0.9929 |
| 0.0180 | 0.8756 | 0.8897 | 0.8893 | 0.9126 | 0.9900 | 0.9969 | 0.9932 |
| 0.0184 | 0.8955 | 0.8987 | 0.8983 | 0.9193 | 0.9900 | 0.9971 | 0.9934 |
| 0.0184 | 0.9005 | 0.8995 | 0.8991 | 0.9395 | 0.9950 | 0.9979 | 0.9941 |
| 0.0431 | 0.9055 | 0.9092 | 0.9092 | 0.9462 | 0.9950 | 0.9981 | 0.9943 |
| 0.0616 | 0.9104 | 0.9153 | 0.9155 | 0.9529 | 1.0000 | 0.9983 | 0.9945 |
| 0.0801 | 0.9204 | 0.9208 | 0.9210 | 0.9865 | 1.0000 | 0.9995 | 0.9956 |
| 0.0863 | 0.9254 | 0.9224 | 0.9227 | 1.0000 | 1.0000 | 1.0000 | 0.9960 |

Figure 9.4. Mean value function fitting curves for both RFE models


Figure 9.5. Mean value function fitting comparisons

Figure 9.6. Model comparisons


Figure 9.7. Reliability prediction comparisonsThe Fisher information matrix $H$ can be obtained as

$$
H=\left[\begin{array}{llll}
h_{11} & h_{12} & h_{13} & h_{14} \\
h_{21} & h_{22} & h_{23} & h_{24} \\
h_{31} & h_{32} & h_{33} & h_{34} \\
h_{41} & h_{42} & h_{43} & h_{44}
\end{array}\right]
$$

where

$$
h_{i j}=E\left[-\frac{\partial^{2} L}{\partial x_{i} \partial x_{j}}\right] \quad i, j=1, \ldots, 6
$$

where $L$ is the log-likelihood function.
If we denote $z\left(t_{k}\right)=m\left(t_{k}\right)-m\left(t_{k-1}\right)$ and $\Delta y_{k}=y_{k}-y_{k-1}, k=1,2, \ldots, n$, then we have

$$
\frac{\partial^{2} L}{\partial x_{i} \partial x_{j}}=\sum_{k=1}^{n}\left(-\frac{\Delta y_{k}}{z\left(t_{k}\right)^{2}} \cdot \frac{\partial z\left(t_{k}\right)}{\partial x_{i}} \cdot \frac{\partial z\left(t_{k}\right)}{\partial x_{j}}+\left(\frac{\Delta y_{k}-z\left(t_{k}\right)}{z\left(t_{k}\right)} \cdot \frac{\partial^{2} z\left(t_{k}\right)}{\partial x_{i} \partial x_{j}}\right)\right)
$$

Then we can obtain the each element in Fisher information matrix $H$. For example,

$$
\begin{aligned}
h_{11} & =E\left[-\frac{\partial^{2} L}{\partial x_{1}^{2}}\right] \\
& =\sum_{k=1}^{n}\left(\sum_{\Delta y_{k}=0}^{\infty}\left(\frac{\Delta y_{k}}{z\left(t_{k}\right)^{2}} \cdot\left(\frac{\partial z\left(t_{k}\right)}{\partial a}\right)^{2}\right) \cdot \frac{\left(z\left(t_{k}\right)\right)^{\Delta y_{k}} \cdot e^{-z\left(t_{k}\right)}}{\left(\Delta y_{k}\right)!}\right) \\
& =\sum_{k=1}^{n}\left(\sum_{\Delta y_{k}=0}^{\infty}\left(\frac{\Delta y_{k}}{z\left(t_{k}\right)^{2}} \cdot\left(\frac{z\left(t_{k}\right)}{a}\right)^{2}\right) \cdot \frac{\left(z\left(t_{k}\right)\right)^{\Delta y_{k}} \cdot e^{-z\left(t_{k}\right)}}{\left(\Delta y_{k}\right)!}\right) \\
& =\sum_{k=1}^{n}\left(\frac{1}{a^{2}} \cdot \sum_{\Delta y_{k}=0}^{\infty} \Delta y_{k} \cdot \frac{\left(z\left(t_{k}\right)\right)^{\Delta y_{k}} \cdot e^{-z\left(t_{k}\right)}}{\left(\Delta y_{k}\right)!}\right) \\
& =\sum_{k=1}^{n}\left(\frac{1}{a^{2}} \cdot z\left(t_{k}\right)\right) \\
& =\frac{1}{a^{2}} \cdot m\left(t_{n}\right)
\end{aligned}
$$

The variance matrix, $V$, can also be obtained

$$
V=[H]^{-1}=\left[\begin{array}{llll}
v_{11} & v_{12} & v_{13} & v_{14} \\
v_{21} & v_{22} & v_{23} & v_{24} \\
v_{31} & v_{32} & v_{33} & v_{34} \\
v_{41} & v_{42} & v_{43} & v_{44}
\end{array}\right]
$$The variances of all the estimate parameters are given by

$$
\begin{aligned}
& \operatorname{Var}(\hat{a})=\operatorname{Var}\left(x_{1}\right)=v_{11} \\
& \operatorname{Var}(\hat{b})=\operatorname{Var}\left(x_{2}\right)=v_{22} \\
& \operatorname{Var}(\hat{\gamma})=\operatorname{Var}\left(x_{3}\right)=v_{33} \\
& \operatorname{Var}(\hat{\theta})=\operatorname{Var}\left(x_{4}\right)=v_{44}
\end{aligned}
$$

The actual numerical results for the $\gamma$-RFE model variance matrix is

$$
V_{\hat{\gamma}}=\left[\begin{array}{cccc}
703.8472 & -0.005387 & -88.6906 & -2.6861 \\
-0.005387 & 7.3655 \times 10^{-8} & 1.11 \times 10^{-3} & 3.097 \times 10^{-5} \\
-88.6906 & 1.11 \times 10^{-3} & 92.4287 & 1.1843 \\
-2.6861 & 3.097 \times 10^{-5} & 1.1843 & 0.0238
\end{array}\right]
$$

Case2: $\beta-R F E$ model. The mean value function in equation (9.19) can also be simplified, where the estimate of $q=0$ and set $c=0, p=1$, is as follows:

$$
m_{\beta}(t)=\left\{\begin{array}{lr}
a\left(1-e^{-b t}\right) & t \leq T \\
a\left(1-e^{-b T} \sum_{k=0}^{\infty}\left[\frac{\Gamma(\alpha+\beta) \Gamma(\beta+k) \mathrm{P}(k, b(t-T))}{\Gamma(\beta) \Gamma(\alpha+\beta+k)}\right]\right) & t \geq T
\end{array}\right.
$$

The above model leads to the same MLE results for parameter $a, b, \alpha$ and $\beta$, and also yields exactly the same mean value function fittings and predictions. To obtain the confidence interval for the reliability predictions for $\beta$-RFE model, we need to obtain the variance-covariance matrix for all maximum likelihood estiates.

If we use $x_{i}, i=1,2,3$, and 4 , to denote all parameters in the model, or

$$
x_{1} \rightarrow a \quad x_{2} \rightarrow b \quad x_{3} \rightarrow \alpha \quad x_{4} \rightarrow \beta
$$

Going through the similar steps as for $\gamma$-RFE model, the actual numerical results for the $\beta$-RFE model variance matrix can be obtained as

$$
V_{\beta}=\left[\begin{array}{cccc}
691.2 & -0.00536 & -2.728 & -66.2172 \\
-0.00536 & 7.4485 \times 10^{-8} & 2.671 \times 10^{-5} & 0.00085 \\
-2.7652 & 2.671 \times 10^{-5} & 0.01820 & 0.8295 \\
-66.2172 & 0.00085 & 0.8295 & 60.5985
\end{array}\right]
$$

# Confidence Interval of Reliability Predictions 

If we define a partial derivative vector for reliability $R(x \mid t)$ as

$$
v R(x \mid t)=\left[\frac{\partial R(x \mid t)}{\partial x_{1}}, \frac{\partial R(x \mid t)}{\partial x_{2}}, \frac{\partial R b(x \mid t)}{\partial x_{3}}, \frac{\partial R(x \mid t)}{\partial x_{4}}\right]
$$then the variance of $R(x \mid t)$ in equation (20) can be obtained as

$$
\operatorname{Var}[R(x \mid t)]=v R(x \mid t) \cdot V \cdot(v R(x \mid t))^{T}
$$

Assume the reliability estimation follows normal distribution, then the $95 \%$ confidence interval for reliability prediction $R(x \mid t)$ is

$$
[R(x \mid t)-1.96 \sqrt{\operatorname{Var}[R(x \mid t)]}, R(x \mid t)+1.96 \sqrt{\operatorname{Var}[R(x \mid t)]}]
$$

Figures 9.8 and 9.9 show the $95 \%$ confidence interval of the reliability predicted by $\gamma$-RFE and $\beta$-RFE models, respectively.



Figure 9.8. $\gamma$-RFE model reliability growth curve and its $95 \%$ confidence interval



Figure 9.9. $\beta$-RFE model reliability growth prediction and its $95 \%$ confidence intervalWe plot the reliability predictions and their $95 \%$ confidence interval by both $\gamma$ RFE model and $\beta$-RFE model in Figure 9.10. For this given application set of data, the reliability predictions by $\gamma$-RFE model and $\beta$-RFE model are very close to each other, so are their confidence intervals.


Figure 9.10. Reliability growth prediction curves and their $95 \%$ confidence intervals for $\gamma$-RFE model and $\beta$-RFE model

# 9.5 Further Reading 

H. Pham, "Recent studies in software reliability engineering," chapter 16 in the Handbook of Reliability Engineering, H. Pham (ed.), Springer, 2003
W. A. Arbaugh, W.L. Fithen and J. McHugh, "Windows of vulnerability: A case study analysis," IEEE Computer, December 2000
N.A. Streitz, C. Rocker, T. Prante, D. Alphen, R. Stenzel, and C. Magerkurth, "Designing smart artifacts for smart environments," IEEE Computer, March 2005
X. Teng and H. Pham, "A software cost model for quantifying the gain with considerations of random field environments," IEEE Trans on Computers, vol 53, no. 3, 2004

### 9.6 Problems

1. Derive the mean value function given in equation (9.16).
2. Derive the mean value function given in equation (9.19).# Optimal Release Policies 

### 10.1 Introduction

The quality of the software system usually depends on how much time testing takes and what testing methodologies are used. On the one hand, the more time people spend on testing, the more errors can be removed, which leads to more reliable software; however, the testing cost of the software will also increase. On the other hand, if the testing time is too short, the cost of the software could be reduced, but the customers may take a higher risk of buying unreliable software (Pham 1999a; Zhang 1998a). This will also increase the cost during the operational phase, since it is much more expensive to fix an error during the operational phase than during the testing phase. Therefore, it is important to determine when to stop testing, and release the software.

In defining important software cost factors, a cost model should help software developers and managers answer the following questions:

1. How should resources be scheduled to ensure the on-time and efficient delivery of a software product?
2. Is the software product sufficiently reliable for release (e.g., have we done enough testing?
3. What information does a manager or software developer need to determine the release of software from current software testing activities?

This chapter discusses several recent generalized cost models based on the NHPP software reliability functions. It aims to help answer these questions by determining the optimal testing release policies of the software systems. In addition to the costs of traditional cost models, the cost models to be discussed in this chapter consider other features such as the testing cost, debugging cost during testing phase, debugging cost during the warranty period, and risk cost due to software failure. These models can be used to estimate the realistic total software cost for applications such as telecommunications, customer service, and real-time embedded systems. The following notations and basic assumptions are used throughout this chapter.$m(T) \quad$ Expected number of errors to be detected by time $T$
$a \quad$ Total number of software errors to be eventually detected
$b \quad$ Exponential index
$x \quad$ Mission time
$R(x \mid T)$ Reliability function of software by time $T$ for a mission time $x$
$T \quad$ Software release time
$C_{1} \quad$ Software test cost per unit time
$C_{2} \quad$ Cost of removing each error per unit time during testing
$E(T) \quad$ Expected total cost of a software system by time T
$N(T) \quad$ Number of errors to be detected by time T
$Y \quad$ Time to remove an error during testing phase
$\mu \mathrm{y} \quad$ Expected time to remove an error during testing phase which is $E(Y)$

# General Assumptions 

(1) The cost to perform testing is proportional to the testing time.
(2) The cost to remove errors during the testing phase is proportional to the total time of removing all errors detected by the end of the testing phase.
(3) The time to remove each error during testing follows a truncated exponential distribution.
(4) There is a risk cost related to the reliability at each release time point.

Let $Y$ be a random variable of time to remove an error. Based on assumption (3), the probability density distribution of $Y$ is given by

$$
s(y)=\frac{\lambda e^{-\lambda y}}{\int_{0}^{T_{0}} \lambda e^{-\lambda z} d z} \quad \text { for } 0 \leq y \leq T_{0}
$$

where $T_{0}$ is the maximum time to remove an error. The expected time to remove each error is

$$
\begin{aligned}
\mu_{y}=E(Y) & =\int_{0}^{T_{0}} y s(y) d y \\
& =\int_{0}^{T_{0}} \frac{y \lambda e^{-\lambda y}}{\int_{0}^{T_{0}} \lambda e^{-\lambda z} d z} d y
\end{aligned}
$$

After simplifications, we obtain

$$
\mu_{y}=\frac{1-\left(\lambda T_{0}+1\right) e^{-\lambda T_{0}}}{\lambda\left(1-e^{-\lambda T_{0}}\right)}
$$

### 10.2 A Software Cost Model with Risk Factor

This section discusses a cost model addressing the risk level and the time to remove errors. The optimal release policies that minimize the expected totalsoftware cost are obtained. Without loss of generality, the Goel-Okumoto NHPP model will be used as a reliability function for this cost model. In other words, the Goel-Okumoto NHPP mean value function $m(T)$ is given by

$$
m(T)=a\left(1-e^{b T}\right)
$$

The error detection rate function is

$$
\lambda(T)=a b e^{-b T}
$$

and the reliability of the software is

$$
\begin{aligned}
R(x \mid T) & =e^{-[m(T+x)-m(T)]} \\
& =e^{-a\left[e^{-b T}-e^{-b(T+x)}\right]}
\end{aligned}
$$

The expected software system cost, $E(T)$, is defined as: (1) the cost to perform testing; (2) the cost incurred in removing errors during the testing phase; and (3) a risk cost due to software failure.

The cost to perform testing is given by

$$
E_{1}(T)=C_{1} T
$$

The expected total time to remove all $N(T)$ errors is

$$
E\left[\sum_{i=1}^{N(T)} Y_{i}\right]=E[N(T)] E\left[Y_{i}\right]=m(T) \mu_{y}
$$

where $\mu_{y}$ is given in equation (10.1). Hence, the expected cost to remove all errors detected by time $T$ can be expressed as

$$
E_{2}(T)=C_{2} E\left[\sum_{i=1}^{N(T)} Y_{i}\right]=C_{2} m(T) \mu_{y}
$$

The risk cost due to software failure after releasing the software is

$$
E_{3}(T)=C_{3}[1-R(x \mid T)]
$$

where $C_{3}$ is the cost due to software failure.
Therefore, the expected total software cost can be expressed (Zhang 1998) as

$$
E(T)=C_{1}(T)+C_{2} m(T) \mu_{y}+C_{3}[1-R(x \mid T)]
$$

Define

$$
\begin{gathered}
f(T)=\lambda(T)\left[C_{3}\left(1-e^{-b x}\right) R(x \mid T)-C_{2} \mu_{y}\right] \\
g(T)=C_{3}\left(1-e^{-b x}\right) R(x \mid T)\left[1-a e^{-b T}\left(1-e^{-b x}\right)\right]
\end{gathered}
$$

It should be noted that $g(T)$ is a strictly increasing function of $T$.
Theorem 10.1 (Zhang and Pham 1998): Given $C_{1}, C_{2}, C_{3}, x$, and $\mu_{y}$, the optimal value of $T$, say $T^{*}$, which minimizes the expected total cost of the software can be determined as follows:
(1) If $g(0)>C_{2} \mu_{y}$, then
(a) If $f(0) \leq C_{l}$, then $T^{*}=0$.(b) If $f(\infty)>C_{1}$, then $T^{*}=\infty$.
(c) If $f(0)>C_{1}, f(T) \geq C_{1}$, for any $T \in\left(0, T^{\prime}\right)$ and $f(T)<C_{1}$, for any $T \in\left(T^{\prime}, \infty^{\prime}\right)$, then $T^{*}=T^{\prime}$ where $T^{\prime} \inf \left\{T: f(T)<C_{1}\right\}$
(2) If $g(\infty)<C_{2} \mu_{y}$, then
(a) If $f(0) \geq C_{1}$, then $T^{*}=\infty$.
(b) If $f(\infty)<C_{1}$, then $T^{*}=0$.

If $f(0)<C_{1}, f(T) \leq C_{1}$ for any $T \in\left(0, T^{\prime}\right)$ and $f\left(T^{\prime}\right)>C_{1}$, for any $T \in\left(T^{\prime \prime} \infty\right)$, then

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0)<\mathrm{E}(\infty) \\
& T^{*}=\infty \text { if } E(0) \geq \mathrm{E}(\infty) \\
& \text { where } \mathrm{T}^{\prime \prime}=\inf \left\{T: f(T)>C_{1}\right\}
\end{aligned}
$$

(3) If $g(0)<C_{2} \mu_{y}, g(T) \leq C_{2} \mu_{y}$ for $T \in\left(0, T_{0}\right)$ and $g(T)>C_{2} \mu_{y}$, for $T \in\left(T_{0}, \infty\right)$, then

If $f(0)<C_{1}$, then

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0)<E\left(T_{b}\right) \\
& T^{*}=T_{b} \text { if } E(0) \geq E\left(T_{b}\right) \\
& \text { where } T_{b}=\inf \left\{T: f(T)<C_{1}, \mathrm{~T}>T_{a}\right\}
\end{aligned}
$$

If $f(0)>C_{1}$, then $T^{*}=T_{b}{ }^{\prime}$ where $T_{b}{ }^{\prime}=\inf \left\{T: f(T)<C_{1}\right\}$
Proof. See (Zhang 1998).
Example 10.1: Assuming a software failure data is given in Table 4.14 (data set \#10), the parameters of the Goel-Okumoto model using MLE is given by

$$
\hat{a}=142.32, \quad \hat{b}=0.1246
$$

The mean value function becomes

$$
\begin{aligned}
m(T) & =a\left(1-e^{-b T}\right) \\
& =142.32\left(1-e^{-0.1246 T}\right)
\end{aligned}
$$

Given $C_{1}=\$ 25, C_{2}=\$ 200, C_{3}=\$ 7,000, \mu_{y}=0.1$, and $x=0.05$, from Theorem 10.1, the results are shown in Table 10.1. The optimal release time in this case is $T^{*}=21.5$ hours and the corresponding expected total cost is $\$ 3,600.49$.

If we increase the value of $C_{3}$ from $\$ 7,000$ to $\$ 10,000$, we would expect to have a longer testing time. In this case ( $C_{1}=\$ 25, C_{2}=\$ 200, C_{3}=\$ 10,000, \mu_{y}=0.1$, and $x$ $=0.05$ ), the optimal release time is $T^{*}=27$ hours and the corresponding expected total cost is $\$ 3,723.95$.Table 10.1. Optimal release time

| Release time T* (hours) | Expected total cost E(T) |
| :--: | :--: |
| 19.5 | 3,607.34 |
| 20.0 | 3,604.47 |
| 20.5 | 3,602.39 |
| 21.0 | 3,601.07 |
| 21.5* | 3,600.49 |
| 22.0 | 3,600.60 |
| 22.5 | 3,601.39 |
| 23.0 | 3,602.81 |
| 23.5 | 3,604.83 |

# 10.3 Cost Model with Testing Coverage 

In this section, a software cost model incorporating testing coverage is discussed. Besides some traditional cost items such as testing cost and error removal cost, risk cost due to potential faults in the uncovered code is included associated with the number of demands from customers. The optimal release policies that minimize the expected total cost subject to the reliability requirement are described.

## Model Formulation

A software cost model is developed based on the following assumptions:
(1)-(3) These assumptions are same as (1)-(3) in the General Assumptions (in Section 10.1).
(4) The mean value function with consideration of testing coverage is given in Theorem 7.2. It is also called the PZ-coverage model
(5) There is a risk cost associated with the testing coverage. A software provider has to pay each customer a certain amount of money for potential faults in uncovered code.
(6) The reliability of the software at release time must satisfy the customers' requirement.

The expected software system cost $E(T)$ is defined as: (1) cost to do testing, $E_{1}(T)$; (2) cost incurred in removing errors during the testing phase, $E_{2}(T)$; and (3) risk cost due to potential faults remaining in the uncovered software code, $E_{3}(T)$.
The two functions $E_{1}(T)$ and $E_{2}(T)$ are the same as in equations (10.5) and (10.6), respectively. Let us assume there are $D$ customers. The provider has to pay each of them a certain amount of money, $C_{3}$, for potential risk due to faults remaining in the uncovered code. Without lack of generality, we assume the demand $D$ is a constant number. It is not difficult to relax this assumption by studying the distribution of demand and calculating the mean value. The total risk cost corresponding to testing coverage, $E_{3}(T)$, can be expressed as follows:

$$
E_{3}(T)=C_{3} D(1-c(T))
$$Therefore, the expected total software cost $E(T)$ can be expressed as following:

$$
E(T)=C_{1} T+C_{2} m(T) \mu_{y}+C_{3} D[1-c(T)]
$$

where $\mu_{y}$ is given in equation (10.1). From Theorem 7.2, the mean value function $m(T)$ and the testing coverage function $c(T)$ are, respectively,

$$
\begin{aligned}
m(T)= & a\left(1+\alpha T-\frac{b T+1}{e^{b T}}\right) \\
& -\frac{a \alpha(1+b T)}{b e^{b T+1}}\left(\ln (b T+1)+\sum_{i=0}^{\infty} \frac{(1+b T)^{i+1}-1}{(i+1)!(i+1)}\right)
\end{aligned}
$$

and

$$
c(T)=1-(1+b T) e^{-b T}
$$

# Optimal Software Release Policies 

We now determine the optimal software release time that minimizes the expected total software cost. In other words, we wish to find the value of T such that $E(T)$ is minimized. Software reliability $R(x / T)$ is another criterion that should be considered in the optimal release policies, especially for safety-critical applications.

Therefore, we determine the optimal release time that minimizes the expected software cost subject to attaining a desired reliability level, $R_{0}$. The optimization problem can be formulated as

Minimize E(T)
Subject to $R(x / T) \geq R_{0}$
where $E(T)$ is given in equation (10.11).
It can be shown that the software reliability function $R(x / T)$ increases as $T$ increases. Let $T_{R}$ be the solution of $R\left(x / T_{R}\right)=R_{0}$. That is, $T_{R}=\left\{T: R^{-1}(x / T)=R_{0}\right\}$. Define

$$
\begin{gathered}
h(T)=\ln (1+b T)+\sum_{i=0}^{\infty} \frac{(1+b T)^{i+1}-1}{(i+1)!(i+1)} \\
g(T)=A-C_{2} \mu_{y} a b \alpha h(T) \\
C=C_{2} \mu_{y} a \alpha, \mathrm{C}>0 \\
u(T)=T g(T)+C \\
v(T)=e^{-(1+b T)}, v(T)>0, \quad \forall T \\
f(T)=C_{1}-v(T) u(T) \\
A=\left(C_{3} D-C_{2} \mu_{y} a\right) e^{1} b^{2} \\
T_{g}=g^{-1}(0)
\end{gathered}
$$

It should be noted that $h(T)$ is a strictly increasing function of $T$ and $g(T)$ is a strictly decreasing function of $T$.Theorem 10.2 (Pham and Zhang 2003d): Given $C_{1}, C_{2}, C_{3}, x, \mu_{y}, D$, the opti-mal value of $T$, say $T^{*}$, which minimizes the expected total cost $E(T)$ subject to software reliability requirement $R_{0}$ is determined as follows:

Case 1. If $\mathrm{A} \geq 0$, then
(1) If $T_{g}>0$,
if $T_{f 2}>T_{R}$, then $T^{*}=T_{f 2}$ minimizes $E(T)$;
if $T_{f 2}<T_{R}, T^{*}=T_{R}$
where $T_{f 2}=\left\{T: T>T_{f 1}, T=f^{-1}(0)\right\}$ and $T_{f 1}=f^{-1}(0)$.
(2) If $T_{g} \leq 0$ then $g(T) \leq 0, \forall T$. The function $u(T)$ intersects with T-axis at only one point $T_{u}=u^{-1}(0)$. Since $u(T) \geq 0$ for $T \in\left[0, T_{u}\right]$ and $u(T)$ $<0$ for $T>T_{u}$, then this subcase becomes the same as subcase (1) for the following discussion

$$
\begin{aligned}
& \text { If } T_{f 2}>T_{R}, T^{*}=T_{f 2} \text { minimizes } E(T) \\
& \text { If } T_{f 2}<T_{R}, T^{*}=T_{R}
\end{aligned}
$$

Case 2. If $\mathrm{A}<0$, then $f(T)$ is a strictly increasing and positive function of $T$. The expected total cost function $E(T)$ will be a strictly increasing and convex function of $T$. Hence, $T^{*}=0$ minimizes $E(T)$.

# Proof: See Problem 4 

Application 10.1: In this example, we use AT\&T system T data to illustrate how we can determine the optimal release time using Theorem 2.

The cost coefficients in the cost model are usually determined by empirical data, previous experiences, or the nature of the applications. The following parameter values are specified in terms of staff recourse according to a project data collected by AT \& T researchers (Ehrlich 1993). The unit is staff-units.

The testing cost coefficient, $C_{1}$, can be estimated to be about 600-700 staffunits. It is estimated that there are 370 CPU test-execution unit during testing with 1.9 staff-units per CPU unit. The error removal cost coefficient during testing period, $C_{2}$, is about 60 staff-units per error.

The risk cost coefficient, $C_{3}$, is the cost due to potential faults in the uncovered code. The value of this cost depends upon the nature of the applications. The cost may include the loss of revenues, customers, and even human life. Let's assume the demand, $D$, is 100 . For commercial applications the demand is usually higher, while for safety-critical applications, the risk coefficient, $C_{3}$, itself is usually higher because of the safety requirement.

Based on the above information, let us consider the following coefficients in the cost model.

Example 10.2: Given $C_{1}=600, C_{2}=60, C_{3}=10,000, \mu_{y}=0.8, x=4.0, D=100$, and assume that the reliability requirement $R_{0}$ is 0.90 . After determining those coefficient values of parameters and from Theoerem 10.2, one can easily find theoptimal release time $T^{*}$ that minimizes the expected total cost $E(T)$. Figure 10.1 illustrates the cost function versus the testing time. The results are as follows:

$$
T^{*}=353.5 \text { days and } E(353.5)=269407.2
$$

The software reliability at time $T^{*}=353.5$ is

$$
R(353.5)=0.8868
$$

In this case, the reliability requirement is not satisfied yet the derised requirement. The testing coverage at this time is $c(353.5)=0.9435$ or $94 \%$. This indicates that one would need to continue testing the software until the software reliability exceeds 0.90 . From the reliability analysis, we can see that when $T=409.5$ days, the software reliability $R(409.5)=0.90006$. This implies that we need to test our software for additional 56 days and the testing coverage at day 409.5 is $c(409.5)=0.9692$ or $97 \%$.


Figure 10.1. The Expected total cost function vs time
Example 10.3: Given $C_{1}=650, C_{2}=65, C_{3}=20,000, \mu_{y}=0.8, x=2.0, D=100$ and assuming that the reliability requirement $R_{0}$ is 0.95 .

Using Theorem 10.2, we can easily obtain the optimal release time $T^{*}$ that minimizes the expected total cost $E(T)$. The result is given as follows:

$$
T^{*}=413 \text { days and } E(413)=328724.1 \text { dollars. }
$$

The corresponding software reliability is given by

$$
R(413)=0.94987
$$

Figure 10.2 illustrates the cost function versus the testing time. We should consider that the software reliability requirement is satisfied. The testing coverage at this time is $c(413)=0.970328$ or $97 \%$. This indicates that we can stop testing the software.# Expected total Cost E(T) 



Figure 10.2. The expected total cost function

### 10.4 A Generalized Software Cost Model

In addition to the cost factors presented in Section 10.2, this section describes a generalized cost model considering the cost of removing errors detected during the warranty period and the risk cost due to software failure. In this section, we use the following notations and assumptions.

## Notation

$C_{0} \quad$ Set-up cost for software testing
$C_{3} \quad$ Cost of removing an error per unit time during the operational phase
$C_{4} \quad$ Loss due to software failure
W Variable of time to remove an error during the warranty period in the operation phase
$\mu_{\mathrm{w}} \quad$ Expected time to remove an error during the warranty period in the operation phase, which is $E(W)$
$T_{w} \quad$ Period of warranty time
$\alpha \quad$ The discount rate of the testing cost

## Additional Assumptions

(1)-(4) Same as General Assumptions 1 - 4 in Section 10.2
(5) There is a set-up cost at the beginning of the software development process.
(6) The cost of testing is a power function of the testing time. This means that at the beginning of the testing, the cost increases with a higher gradient, slowing down later.
(7) The time to remove each error during the warranty period follows a truncated exponential distribution.
(8) The cost to remove errors during the warranty period is proportional to the total time of removing all errors detected during the interval of $\left(\mathrm{T}, T_{w}\right)$.Similarly, from assumption 7, the truncated exponential density function of error removal time during the warranty period is

$$
q(w)=\frac{\lambda_{w} e^{-\lambda_{w} w}}{\int_{0}^{T_{0}} \lambda_{w} e^{-\lambda_{w} x} d x} \text { for } 0 \leq w \leq T_{0}
$$

Therefore, the expected time to remove an error during the warranty period is

$$
\mu_{w}=\frac{1-\left(\lambda_{w} T_{0}+1\right) e^{-\lambda_{w} T_{0}}}{\lambda_{w}\left(1-e^{-\lambda_{w} T_{0}}\right)}
$$

The expected software system cost comprises of the set-up cost, the cost to do testing, the cost incurred in removing errors during the testing phase and during the warranty period, and the risk cost in releasing the software system by time $T$. Hence, the expected total software system cost $E(T)$ can be expressed as follows (Pham 1999c):

$$
\begin{aligned}
E(T)=C_{0} & +C_{1} T^{\alpha}+C_{2} m(T) \mu_{y}+C_{3} \mu_{w}\left[m\left(T+T_{w}\right)-m(T)\right] \\
& +C_{4}[1-R(x \mid T)]
\end{aligned}
$$

where $0 \leq \alpha \leq 1$. Define

$$
\begin{aligned}
y(T)= & \alpha C_{1} T^{(\alpha-1)}-\mu_{w} C_{3} a b e^{-b T}\left(1-e^{-b T_{w}}\right) \\
& -a b e^{-b T}\left[C_{4}\left(1-e^{-b x}\right) R(x \mid T)-C_{2} \mu_{y}\right] \\
u(T)= & a b^{2} C_{4}\left(1-e^{-b x}\right) R(x \mid T)\left[1-a e^{-b T}\left(1-e^{-b x}\right)\right] \\
& +\alpha(\alpha-1) C_{1} T^{(\alpha-2)} e^{b T} \\
C & =C_{2} \mu_{y} a b^{2}-\mu_{w} C_{3} a b^{2}\left(1-e^{-b T_{w}}\right)
\end{aligned}
$$

It can be shown that the function $u(T)$ is an increasing function of $T$ (see Problem 2). The optimal software release time, $T^{*}$, which minimizes the expected total system cost is given below.

Theorem 10.3 (Pham and Zhang, 1999c): Given $C_{O}, C_{1}, C_{2}, C_{3}, C_{4}, x, \mu_{y}, \mu_{w}, T_{w}$, the optimal value of $T$, say $T^{*}$, which minimizes the expected total cost of the software is as follows:
(1) If $u(0) \geq C$, and
(a) If $y(0) \geq 0$, then $T^{*}=0$;
(b) If $y(\infty)<0$, then $T^{*}=\infty$.
(c) If $y(0)<0, y(T)<0$, for $T \in\left(0, T^{\prime}\right)$ and $y(T)>0$, for $T \in\left(T^{\prime}, \infty\right)$, then $T^{*}$ $=T^{\prime}$ where $T^{\prime}=y^{-1}(0)$
(2) If $u(\infty)<C$ and
(a) If $y(0) \leq 0$, then $T^{*}=\infty$.
(b) If $y(\infty)>0$, then $T^{*}=0$.
(c) If $y(0)>0, y(T)>0$ for $T \in\left(0, T^{\prime \prime}\right)$ and $y(T)<0$ for $T \in\left(T^{\prime \prime}, \infty\right)$, then $T^{*}=0$ if $E(0) \leq E(\infty)$$$
T^{*}=\infty \text { if } E(0)>E(\infty)
$$

where $T^{\prime \prime}=y^{-1}(0)$
(3) If $u(0)<C, u(T) \leq C$ for $T \in\left(0, T_{0}\right)$ and $u(T)>C$ for $T \in\left(T_{0}, \infty\right)$, where $T_{0}=u^{-1}(C)$, then
(a) If $y(0) \geq 0$, then
$T^{*}=0$ if $E(0) \leq E\left(T_{b}\right)$
$T^{*}=T_{b}$ if $E(0)>E\left(T_{b}\right)$
where $T_{b}=\inf \left\{T>T_{a}: y(T)>0\right\}$
(b) If $y(0)<0$, then $T^{*}=T_{b}$ ' where $T_{b}{ }^{\prime}=y^{-1}(0)$

Proof: Taking the first derivative of $E(T)$, we obtain

$$
\begin{aligned}
\frac{\partial E(T)}{\partial T} & =\alpha C_{1} T^{(\alpha-1)}-\mu_{w} C_{3} a b e^{-b T}\left(1-e^{-b T_{o}}\right) \\
& -a b e^{-b T}\left[C_{4}\left(1-e^{-b x}\right) R(x \mid T)-C_{2} \mu_{y}\right] \\
& =y(T)
\end{aligned}
$$

The second derivative of $E(T)$,

$$
\frac{\partial^{2} E(T)}{\partial T^{2}}=e^{-b T}[u(T)-C]
$$

Case 1: If $u(0) \geq C$, then $u(T)>C$ for any $T$. In this case, $y(T)$ is a strictly increasing function of $T$ and

$$
\frac{\partial^{2} E(T)}{\partial T^{2}}>0
$$

There are three subcases:
(a) If $y(0)>0$, then $y(T)>0$ for all $T$ and $E(T)$ is strictly increasing in $T$ Hence, $T^{*}$ $=0$ minimizes $E(T)$.
(b) If $y(\infty)<0$, then $y(T)<0$ for all $T$ and $E(T)$ is decreasing in $T$. Hence, $T^{*}=\infty$ minimizes $E(T)$.
(c) If $y(0)<0, y(T)<0$ for any $T \in\left(0, T^{\prime}\right)$ and $y(T)>0$ for any $T \in\left(T^{\prime}, \infty\right)$, then $T^{*}$ $=T^{\prime}$ where $T^{\prime}=y^{-1}(0)$.

Case 2: If $u(\infty)<C$, then $u(T)<C$ for any $T$. In this case, $y(T)$ is a strictly decreasing function of $T$ and

$$
\frac{\partial^{2} E(T)}{\partial T^{2}}<0
$$

There are three subcases:
(a) If $y(0) \leq 0$, then $y(T) \leq 0$ for all $T$ and $E(T)$ is strictly decreasing in $T$. Hence, $T^{*}$ $=\infty$ minimizes $E(T)$.
(b) If $y(\infty)>0$, then $y(T)>0$ for all $T$ and $E(T)$ is increasing in $T$. Hence, $T^{*}=0$ minimizes $E(T)$.
(c) If $y(0)>0$, and $y(T)>0$ for any $T \in\left(0, T^{\prime \prime}\right]$ and $y(T)<0$ for any $T \in\left(T^{\prime \prime}, \infty\right)$, then $T^{*}=0$ if
$\mathrm{E}(0)<\mathrm{E}(\infty)$ and $\mathrm{T}^{*}=\infty$ if $E(0) \geq E(\infty)$, where $T^{\prime}=y^{-1}(0)$.Case 3: See Problem 3.
Example 10.4: Considering a set of testing data given in Table 4.14 (data set \#10), and Example 10.1, the mean value function is

$$
m(T)=142.32\left(1-e^{-0.1246 T}\right)
$$

Given $C_{1}=\$ 50, C_{2}=\$ 25, C_{3}=\$ 100, C_{4}=\$ 1000, \mu_{\mathrm{r}}=0.1, \mu_{\mathrm{w}}=0.5, x=0.05, \alpha=$ 0.05 , and $T_{\mathrm{w}}=20$. Based on Theorem 10.3, we obtain the results given in Table 10.2. The optimal release time is $T^{*}=24.5$ and the corresponding expected total cost is $\$ 1836.15$.

Table 10.2. Optimal release time for $C_{0}=\$ 100$

| $\mathrm{T}^{*}$ (hours) | $E(T)(\$)$ |
| :--: | :-- |
| 22.5 | $1,843.31$ |
| 23.0 | $1,843.31$ |
| 23.5 | $1,839.52$ |
| 24.0 | $1,837.17$ |
| $24.5^{*}$ | $1,836.15$ |
| 25.0 | $1,836.39$ |
| 25.5 | $1,837.82$ |
| 26.0 | $1,840.35$ |
| 26.5 | $1,843.93$ |

Example 10.5: Given $C_{1}=\$ 50, C_{2}=\$ 25, C_{3}=\$ 100, C_{4}=\$ 10,000, \mu_{\mathrm{r}}=0.1, \mu_{\mathrm{w}}=$ $0.5, x=0.05, \alpha=0.05$, and $T_{\mathrm{w}}=20$. Using Theorem 10.3, we obtain the results in Table 10.3. The optimal release time for this case is $T^{*}=30.5$ and the corresponding expected total cost is $\$ 3017.13$.

# 10.5 Cost Model with Multiple Failure Errors 

This section describes a software cost model under the following assumptions:
(1) The cost of debugging an error during the development phase is lower than in the operational phase.
(2) The cost of removing a particular type of error is constant during the debugging phase.
(3) The cost of removing a particular type of error is constant during the operational phase.
(4) The cost of removing critical errors is more expensive than major errors, and the cost of removing major errors is more expensive than minor errors.
(5) There is a continuous cost incurred during the entire time of the debugging period.Table 10.3. Optimal release time for $C_{0}=\$ 1000$

| T* (hours) | $E(T)(\$)$ |
| :-- | :-- |
| 28.5 | 3029.72 |
| 29.0 | 3024.41 |
| 29.5 | 3020.60 |
| 30.0 | 3018.20 |
| $30.5^{*}$ | 3017.13 |
| 31.0 | 3017.30 |
| 31.5 | 3018.64 |
| 32.0 | 3021.09 |
| 32.5 | 3024.57 |

# Notation 

$T \quad$ Software release time
$C_{i 1} \quad$ Cost of fixing a type $i$ error during the test phase $i=1,2,3$
$C_{i 2} \quad$ Cost of fixing a type $i$ error during the operation phase $\left(C_{i 2} \geq C_{i 1}, i=1,2,3\right)$
$C_{3} \quad$ Cost of testing per unit time
$E(T) \quad$ Expected cost of software
$R_{0} \quad$ Pre-specified software reliability
$T_{\mathrm{r}} \quad$ Debugging time required to attain minimum cost subject to a reliability constraint
$T_{\mathrm{e}} \quad$ Debugging time required to attain minimum cost subject to the number of remaining errors constraint
$T_{\text {rel }} \quad$ Debugging time required to attain maximum reliability subject to a cost constraint

Assume that the duration of the software lifecycle is random. Let $t$ be the random variable of the duration of the software lifecycle and $g(t)$ the probability density function of $t$. Assume that the cost of testing per unit time and the cost of fixing any type $i$ error during the test phase and the operation phase are given.

The expected software cost is defined as the cost incurred in removing and fixing errors in the software during the software lifecycle measured from the time the testing starts. Hence, the expected software cost $E(T)$ can be formulated as (Pham 1996a)

$$
\begin{aligned}
E(T)= & \int_{0}^{T}\left[C_{3} t+\sum_{i=1}^{3} C_{i 1} m_{i}(t)\right] g(t) d t \\
& +\int_{T}^{\infty}\left[C_{3} T+\sum_{i=1}^{3} C_{i 1} m_{i}(T)\right. \\
& \left.+\sum_{i=1}^{3} C_{i 2}\left(m_{i}(t)-m_{i}(T)\right)\right] g(t) d t
\end{aligned}
$$

where $m_{i}(t)$ is given (in Pham 1996a) as follows:

$$
m_{i}(t)=\frac{a p_{i}}{1-\beta_{i}}\left(1-e^{-\left(1-\beta_{i}\right) b_{i} t}\right)
$$The function $E(T)$ represents testing costs per unit time and of fixing errors during testing incurred if the determination of the software lifecycle is less than or equal to the software release time. On the other hand, if the determination of the software lifecycle is greater than the software release time, then an additional cost factor should be involved, i.e., the cost of fixing errors during the operation phase. We next determine the value of $T$ such that $E(T)$ is minimized. Define

$$
h(T)=\sum_{i=1}^{3}\left(c_{i 2}-c_{i 1}\right) \lambda_{i}(T)
$$

Theorem 10.4: Given $C_{3}, C_{\mathrm{il}}$, and $C_{\mathrm{i} 2}$ for $i=1,2,3$. There exists an optimal testing time, $T^{*}$, for $T$ that minimizes $E(T)$ :

$$
\begin{aligned}
& \text { If } h(0) \leq C_{3}, \text { THEN } T^{*}=0 \\
& \text { ELSE } T^{*}=h^{-1}\left(C_{3}\right) ; \text { ENDIF }
\end{aligned}
$$

Proof: See Problem 8.
Theorem 10.4 shows that if $h(0) \geq C_{3}$, then the testing time required to attain the minimum cost has already been achieved. Thus, the marginal cost for further testing is an increasing function, and as each additional test and debug increases the cost of the software, no further testing should be done, and the software package should be released for sale.

However, if the testing time required to attain the minimum cost has not been achieved, and the marginal cost for further debugging is a decreasing function for an interval of times, testing should be continued until time $T^{*}$, where $T^{*}$ satisfies $h\left(T^{*}\right)=C_{3}$.

Although the optimal policies in Theorem 4 are sound in theory, it seems reasonable in practice that simply minimizing cost should not be the only goal for some applications. In the following subsection, we discuss the optimum release policies that minimize the expected software system cost subject to various constraints.

# Cost Subject to Reliability Constraint 

Consider the expected software cost $E(T)$ and the software reliability $R(x / T)$ as the evaluation criteria. We determine the optimum release time that minimizes the expected software cost subject to attaining a desired reliability level, $R_{0}$. Then the optimization problem can be formulated as

$$
\begin{aligned}
& \text { Minimize } E(T) \\
& \text { Subject to } R(x / T) \geq R_{0}
\end{aligned}
$$

where $E(T)$ is given in equation (10.26). It can be proven that the software reliability $R(x / T)$ increases as $T$ increases. Let $T_{1}$ be the solution of $R\left(x / T_{1}\right)=R_{0}$.

Lemma 10.1: Given $C_{3}, R_{0}, C_{i 1}$, and $C_{i 2}$ for $i=1,2,3$. The optimal value of $T$, say $T_{\mathrm{r}}$, which minimizes $E(T)$ subject to software reliability not less than a specified value, $R_{0}$, is determined from$$
\begin{aligned}
& \text { IF } h(0) \leq C_{3} \text { THEN } \\
& \text { IF } R(x \mid 0) \geq R_{0} \text { THEN } T_{\mathrm{r}}=0 \\
& \text { ELSE } T_{\mathrm{r}}=T_{1} \\
& \text { ELSE IF } R\left(x \mid T^{*}\right) \geq R_{0} \text { THEN } T_{\mathrm{r}}=T^{*} \\
& \text { ELSE } T_{\mathrm{r}}=T_{1}
\end{aligned}
$$

The physical interpretation of the result of Lemma 10.1 is as follows. If $h(0) \leq$ $C_{3}$, then the current amount of debugging has already minimized the expected software system cost. Furthermore, if the current amount of debugging has met the reliability constraint, then no further debugging should be done, and the software should be released. Otherwise, the current amount of debugging does not meet the reliability constraint, and the debugging should be continued until time $T_{1}$, where $T_{1}$ satisfies $R\left(x \mid T_{1}\right)=R_{0}$. The interpretation of the case $h(0)>C_{3}$ is similar to the above.

# Cost Subject to the Number of Remaining Errors Constraint 

We now present a method that will allow for the constraining of a particular type of error. The importance of this is that, though a program may be able to tolerate a large number of minor errors, it cannot tolerate critical errors. In this case, a constraint can be put on the expected number of remaining critical errors in the system before its release. It is also possible to set up constraints for each of the different types of errors independent of the other types.

Consider both the expected total software system cost, $E(T)$, and the expected number of failure type $i$ errors remaining in the system, $\bar{m}_{i}(T)$, as the evaluation criteria. The optimal release problem can be formulated as

$$
\begin{array}{ll}
\text { Minimize } & E(T) \\
\text { Subject to } & \bar{m}_{i}(T) \leq d_{i} \quad i=1,2,3
\end{array}
$$

where

$$
\begin{aligned}
\bar{m}_{i}(T) & =m_{i}(\infty)-m_{i}(T) \\
& =\frac{a p_{i}}{1-\beta_{i}} e^{-\left(1-\beta_{i}\right) b_{i} T}
\end{aligned}
$$

and $d_{i}$ is the accepted number of remaining type $i$ errors. Define

$$
T_{m_{i}}=\frac{\ln \left(\frac{a p_{i}}{d_{i}\left(1-\beta_{i}\right)}\right)}{\left(1-\beta_{i}\right) b_{i}}
$$

The function $\bar{m}_{i}(T)$ is, of course, decreasing in $T$ for all $T$ Then $\bar{m}_{i}(T) \leq d_{i}$ if and only if $T \geq \mathrm{~T}_{m i}$.

Lemma 10.2: Given $C_{3}, d_{i}, C_{i 1}$, and $C_{i 2}$ for $i=1,2,3$, then the optimal value of $T$, say $T_{\mathrm{e}}$, that minimizes $E(T)$ subject to the number of remaining errors constraint is determined from$$
\begin{aligned}
& \text { IF } h(0) \leq C_{3} \text { THEN } T_{\mathrm{e}}=\max _{1 \leq i \leq 3}\left\{0, T_{m i}\right\} \\
& \text { ELSE } T_{\mathrm{e}}=\max _{1 \leq \mathrm{i} \leq 3}\left\{T^{*}, T_{m i}\right\} ; \text { ENDIF }
\end{aligned}
$$

Similarly, the physical interpretation of the results of Lemma 10.2 is that if $h(0) \leq C_{3}$, then the current debugging has already minimized cost, but not all of the expected error constraints have been met. In this situation, the software program should be debugged until all of the expected error constraints have been met. However, if $h(0)>C_{3}$, then the current amount of debugging has not achieved minimum cost. In this situation, debugging should continue until all constraints have been met and minimum cost has been achieved.

# Software Reliability Subject to Cost Constraint 

Consider both the software reliability $R(x \mid T)$ and the expected software cost $E(T)$ as the evaluation criteria. The optimal policies problem can be formulated as

$$
\left\{\begin{array}{l}
\text { Maximize } R(x \mid T) \\
\text { Subject to } E(T) \leq C_{R}
\end{array}\right.
$$

where $C_{\mathrm{R}}$ is the maximum amount allowable.
Lemma 10.3: Given $C_{3}, C_{R}, C_{i}$, and $C_{i 2}$ for $i=1,2,3$. The optimal value of $T$, say $T_{\text {rel }}$, that maximizes $R(x \mid T)$ subject to the cost constraint is determined from

$$
\begin{aligned}
& \text { IF } E\left(T^{*}\right)>C_{\mathrm{R}} \text { THEN there is NO solution } \\
& \text { ELSE } T_{\text {rel }}=\left\{T \geq T^{*}: T=E^{-1}\left(C_{\mathrm{R}}\right)\right\} ; \text { ENDIF }
\end{aligned}
$$

These results show that if $E\left(T^{*}\right)>C_{R}$, the minimum software system cost required to develop and debug the program exceeds the maximum amount allowable. Therefore, it is impossible to produce the software under these conditions. Similarly, if $E\left(T^{*}\right) \leq C_{R}$, and as the reliability of the software continually improves with testing and debugging time, then the program should be debugged until the cost constraint is binding, implying that additional debugging will violate the constraint.

## Applications

Using the data set \#3 given in Table 4.7 and given the following reliability and error introduction rate parameters values,

$$
\begin{array}{lll}
p_{1}=0.0173 & p_{2}=0.3420 & p_{3}=0.6407 \\
\beta_{1}=0.5 & \beta_{2}=0.2 & \beta_{3}=0.05
\end{array}
$$

Using the MLE, we obtain (Pham 1996a)

$$
\begin{array}{ll}
a=428 & b_{1}=0.00024275 \\
b_{2}=0.00029322 & b_{3}=0.00030495
\end{array}
$$

Given the following cost coefficients,

$$
\begin{array}{lll}
C_{1,1}=200 & C_{2,1}=80 & C_{3,1}=30 \\
C_{1,2}=1000 & C_{2,2}=350 & C_{3,2}=150 & C_{3}=10
\end{array}
$$Assume that the mean rate of the software lifecycle length is constant. Given that the mean rate $\mu=0.00005$, then

$$
g(T)=\mu e^{-\mu T} \quad \text { for } T>0
$$

From equation (10.26), the expected software system cost is given by

$$
\begin{aligned}
E(T)= & \int_{0}^{T}\left[10 t+200 m_{1}(t)+80 m_{2}(t)+30 m_{3}(t)\right] g(t) d t \\
& +\int_{T}^{\infty}\left[10 T+200 m_{1}(T)+80 m_{2}(T)+30 m_{3}(T)\right. \\
& +1,000\left(m_{1}(t)-m_{1}(T)\right)+350\left(m_{2}(t)-m_{2}(T)\right) \\
& \left.+150\left(m_{3}(t)-m_{3}(T)\right)\right] g(t) d t
\end{aligned}
$$

Substituting $m_{i}(t)$ in equation (10.26) for $i=1,2,3$ into the above equation, we obtain

$$
\begin{aligned}
E(T)= & \frac{1}{\mu}\left(1-e^{-\mu T}\right) C_{3} \\
& -\sum_{i=1}^{3}\left(C_{i 2}-C_{i 1}\right) A_{i}\left[\left(1-e^{-\left(1-\beta_{i}\right) b_{i} T}\right] e^{-\mu T}\right. \\
& \left.+\sum_{i=1}^{3} C_{i 1}\left\{A_{i}\left[\left(1-e^{-\mu T}\right)-\frac{\mu}{B_{i}}\left(1-e^{B_{i} T}\right)\right]\right\}\right. \\
& \left.+\sum_{i=1}^{3} C_{i 2}\left\{A_{i}\left[e^{-\mu T}-\frac{\mu}{B_{i}} e^{-\beta_{i} T}\right)\right]\right\}
\end{aligned}
$$

where

$$
A_{i}=\frac{a p_{i}}{1-\beta_{i}} \quad \text { and } \quad B_{i}=\left(1-\beta_{i}\right) b_{i}+\mu
$$

Substituting and simplifying the cost coefficient values to the above equation, we obtain$$
\begin{aligned}
E(T)= & 200,000\left(1-e^{-0.00005 T}\right)-11,848\left(1-e^{-0.0001214 T}\right) e^{-0.00005 T} \\
& -49,401.9\left(1-e^{-0.0002346 T}\right) e^{-0.00005 T} \\
& -34,638\left(1-e^{-0.0002897 T}\right) e^{-0.00005 T} \\
& +2,962\left[1-e^{-0.00005 T}-0.2917153\left(1-e^{-0.0001714 T}\right)\right] \\
& +14,637.6\left[1-e^{-0.00005 T}-0.1756852\left(1-e^{-0.0002846 T}\right)\right] \\
& +8,659.5\left[1-e^{-0.00005 T}-0.1471887\left(1-e^{-0.0003397 T}\right)\right] \\
& +14,810\left[e^{-0.00005 T}-0.2917153 e^{-0.0001714 T}\right] \\
& +64,039.5\left[e^{-0.00005 T}-0.1756852 e^{-0.0002846 T}\right] \\
& +43,297.5\left[e^{-0.00005 T}-0.1471887 e^{-0.0003397 T}\right]
\end{aligned}
$$

It is easy to obtain the optimum total testing time, $T^{*}$, that minimizes the expected total software system cost using Theorem 10.4. The results are given as below:

$$
T^{*}=3,366.8 \text { hours and } \mathrm{E}(3,366.8)=\$ 82,283.2
$$

If a desired level of reliability is 0.99 for a mission of 10 hours, then by using Lemma 10.1, the optimal software release time, $T_{r}$, that minimizes the expected total software system cost is easily obtained as $T_{r}=19,045$ hours.

If we assume that the remaining error constraints are
type 1 errors: $d_{1} \leq 5$
type 2 errors: $d_{2} \leq 5$
type 3 errors: $d_{3} \leq 5$
From Lemma 10.2, the optimal release time in this situation is given as follows:
$T_{m 1}=8,946$ hours
$T_{m 2}=13,912$ hours, and
$T_{m 3}=11,607$ hours.
Since $T_{m 2}$ is the maximum of the four values, $T_{m 1}, T_{m 2}, T_{m 3}$, and $T^{*}, T_{\mathrm{e}}=13,912$ hours.

# 10.6 Gain Model with Random Field Environments 

This section discusses the software gain model under random field environment with consideration of not only time to remove faults during in-house testing, cost of removing faults during beta testing, risk cost due to software failure, but also the benefits from reliable executions of the software during both beta testing and field operation.

Section 9.4 discusses a NHPP software reliability model with consideration of random field environments. This is a model which covers both beta testing and operation phases in the software systems. During beta testing, not only can software faults still be removed from the software after failures occur, but they arealso likely to be conducted in an environment that is the same as (or close to) the end-user environment.

The model in Theorem 10.3 considers both the warranty cost and the penalty cost after releasing the software, which are overlapped with each other. The model which will be discussed in this section is solely based on a recent study by Teng and Pham (2004). For the sake of simplicity, let us called it the T-P cost model. The T-P cost model is indeed slightly different to the model in Theorem 10.3. The T-P cost model does not consider a warranty cost, but instead considers a similar concept - the cost associated with the beta testing that is conducted in the field environment. The beta testing cost and the penalty cost after the software is released are not overlapped with each other.

Notation

| $R(x \mid T)$ | Software reliability function. It is defined as the probability that a <br> software failure does not occur in time interval $[t, t+x]$, where $t \geq$ <br> 0 , and $x>0$ |
| :-- | :-- |
| $G(\eta)$ | Cumulative distribution function of random environmental factor |
| $\gamma$ | Shape parameter of field environmental factor (Gamma distributed <br> variable) |
| $\theta$ | Scale parameter of field environmental factor (Gamma distributed <br> variable) |
| $N(T)$ | Counting process which counts the number of software failures <br> discovered by time $T$ |
| $m(T)$ | Expected number of software failures by time $T, m(T)=E[N(T)]$ |
| $m_{1}(T)$ | Expected number of software failures during in-house testing by <br> time $T$ |
| $m_{2}(T)$ | Expected number of software failures in beta testing and final field <br> operation by time $T$ |
| $m_{F}(t \mid \eta)$ | Expected number of software failures in field by time $t$ |
| $C_{0}$ | Set-up cost for software testing |
| $C_{1}$ | Software in-house testing per unit time |
| $C_{2}$ | Cost of removing a fault per unit time during in-house testing |
| $C_{3}$ | Cost of removing a fault per unit time during beta testing |
| $C_{4}$ | Penalty cost due to software failure |
| $C_{5}$ | Benefits if software does not fail during beta testing |
| $C_{6}$ | Benefits if software does not fail in field operation |
| $\mu_{y}$ | Expected time to remove a fault during in-house testing phase |
| $\mu_{w}$ | Expected time to remove a fault during beta testing phase |
| $a$ | Number of initial software faults at the beginning of testing |
| $a_{F}$ | Number of initial software faults at the beginning of the field <br> operations || $t_{0}$ | Time to stop testing and release the software for field operations. |
| :-- | :-- |
| $b$ | Fault detection rate per fault |
| $T_{w}$ | Time length of the beta testing |
| $x$ | Time length that the software is going to be used |
| $p$ | Probability that a fault is successfully removed from the software |
| $\beta$ | Probability that a fault is introduced into the software during <br> debugging, and $\beta<<p$ |

Assume that the error detection rate function $\mathrm{b}(\mathrm{t})$ is a constant and from equation (9.16), the mean value function of the software system with consideration of random field environments is given by

$$
m(t)= \begin{cases}\frac{a}{p-\beta}\left(1-e^{-b(p-\beta) t}\right) & \mathrm{t} \leq T \\ \frac{a}{p-\beta}\left(1-\left(e^{-b(p-\beta) T}\right)\left(\frac{\theta}{\theta+b(p-\beta)(t-T)}\right)^{T}\right) & \mathrm{t} \geq T\end{cases}
$$

Generally, the software reliability prediction is used after the software is released for field operations, i.e., $t \geq T$. Therefore, the reliability of the software in the field is

$$
R(x \mid t)=e^{a e^{-b(p-\beta) T} D}
$$

where

$$
D=\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot(t+x-T)}\right)^{T}-\left(\frac{\theta}{\theta+b(p-\beta)(t-T)}\right)^{T}
$$

We want to determine when to stop testing the software. In other words, we only need to know the software reliability immediately after the software is released. In this case, $t=T$, therefore

$$
R(x \mid T)=\exp \left(-a e^{-b(p-\beta) T}\left(1-\left(\frac{\theta}{\theta+b(p-\beta) x}\right)^{T}\right)\right)
$$

# 10.6.1 Model Formulation 

Figure 10.3 shows the software development process to be considered in the cost model: in-house testing, beta testing and operation, while beta testing and operation are conducted in the field environment, which is commonly quite different from the environment where the in-house testing is conducted.

Figure 10.3. Software gain model
Consider the following cost factors:

1. There is a constant set-up cost at the beginning of the in-house testing.
2. The cost of testing is a linear function of in-house testing time.
3. The cost to remove faults during the in-house testing period is proportional to the total time for removing all faults detected during this period.
4. The cost to remove faults during the beta testing period is proportional to the total time of removing all faults detected in $\left[T, T+T_{w}\right]$.
5. It takes time to remove faults and it is assumed that the time to remove each fault follows a truncated exponential distribution.
6. There is a penalty cost due to software failure after formal release of the software, i.e., after the beta testing.
7. Software companies receive the economic profits from reliable executions of their software during beta testing and use in field environments.

The expected time to remove each fault during in-house testing $\mu_{x}$ is given in equation (10.1). Similarly, the expected time to remove each fault $\mu_{w}$ during beta testing is given in equation (10.23).

The expected net gain of the software development process $E(T)$ is defined as the economical revenue in software reliability that exceeds the expected total cost of the software development (Teng and Pham 2004). In other words,
$E(T)=$ Expected Revenue Gain in Reliability - (Total Development Cost + Risk Cost)

Based on the above assumptions, the expected software system cost consists of:

# 1. Total development cost 

The total development cost, $E_{C}(T)$, including
a) A constant set-up $\operatorname{cost} C_{0}$
b) Cost to do in-house testing, $E_{1}(T)$. We assume it is a linear function of time to do in-house testing $T$, then $E_{1}(T)=C_{1} \cdot T$c) As in equation (10.24), the expected fault removal cost during in-house testing period, $E_{2}(T)$, is given by

$$
E_{2}(T)=C_{2} \cdot E\left[\sum_{i=1}^{N(T)} Y_{i}\right]=C_{2} \cdot m(T) \cdot \mu_{y}
$$

d) The fault removal cost during beta testing period, $E_{3}(T)$, can be easily obtained as follows:

$$
E_{3}(T)=C_{3} \cdot E\left[\sum_{i=N(T)}^{N\left(T+T_{w}\right)} W_{i}\right]=C_{3} \cdot \mu_{w} \cdot\left(m\left(T+T_{w}\right)-m(T)\right)
$$

Therefore, the total software development cost can be written as

$$
E_{C}(T)=C_{0}+E_{1}(T)+E_{2}(T)+E_{3}(T)
$$

# 2. Risk cost 

The risk cost due to software failures after releasing the software, $\mathrm{E}_{4}(T)$, is given by

$$
E_{4}(T)=C_{4} \cdot\left(1-R\left(x \mid T+T_{w}\right)\right)
$$

## 3. Expected Revenue Gain

The expected revenue gain, $E_{p}(T)$, including
a) Benefits gained during beta testing due to reliable execution of the software, $\mathrm{E}_{5}(T)$, is

$$
E_{5}(T)=C_{5} \cdot R\left(T_{w} \mid T\right)
$$

b) Benefits gained during field operation due to reliable execution of the software, $\mathrm{E}_{6}(T)$, is

$$
E_{6}(T)=C_{6} \cdot R\left(x \mid T+T_{w}\right)
$$

Therefore, the expected gain of the software development process, $E(T)$, can be expressed as

$$
\begin{aligned}
E(T)= & E_{p}(T)-\left(E_{C}(T)+E_{4}(T)\right) \\
= & \left(E_{5}(T)+E_{6}(T)\right)-\left(C_{0}+E_{1}(T)+E_{2}(T)+E_{3}(T)+E_{4}(T)\right) \\
= & C_{5} \cdot R\left(T_{w} \mid T\right)+C_{6} \cdot R\left(x \mid T+T_{w}\right)-C_{0}-C_{1} \cdot T-C_{2} \cdot \mu_{y} \cdot m(T) \\
& -C_{3} \cdot \mu_{w} \cdot\left(m\left(T+T_{w}\right)-m(T)\right)-C_{4} \cdot\left(1-R\left(x \mid T+T_{w}\right)\right)
\end{aligned}
$$

or, equivalently, as

$$
\begin{aligned}
E(T)= & C_{5} \cdot R\left(T_{w} \mid T\right)+\left(C_{4}+C_{6}\right) \cdot R\left(x \mid T+T_{w}\right)-\left(C_{0}+C_{4}\right) \\
& -C_{1} \cdot T-C_{2} \cdot m_{1}(T) \cdot \mu_{y}-C_{3} \cdot \mu_{w} \cdot\left(m_{2}\left(T+T_{w}\right)-m_{2}(T)\right)
\end{aligned}
$$

where

$$
m_{1}(t)=\frac{a}{p-\beta}\left(1-e^{-b(p-\beta) t}\right) \quad \mathrm{t} \leq \mathrm{T}
$$$$
m_{2}(t)=\frac{a}{p-\beta}\left(1-e^{-b(p-\beta) T}\left(\frac{\theta}{\theta+b(p-\beta)(t-T)}\right)^{T}\right) \quad \mathrm{t} \geq \mathrm{T}
$$

Next we will obtain the optimal software release time, $T^{*}$ which maximizes the expected net gain of software systems. Let

$$
\begin{aligned}
y(T)= & -C_{1}-C_{2} \cdot \mu_{y} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T}+ \\
& \mu_{w} \cdot C_{3} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T}\left(1-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}\right)+ \\
& C_{5} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T} \cdot R\left(T_{w} \mid T\right) \cdot\left(1-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}\right) \\
& +\left(C_{4}+C_{6}\right) \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T} \cdot R\left(x \mid T+T_{w}\right) \cdot \\
& \left(\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot\left(T_{w}+x\right)}\right)^{T}\right) \\
u(T)= & -\left(C_{4}+C_{6}\right)(p-\beta) a b^{2} R\left(x \mid T+T_{w}\right) \times \\
& \left(\left(\frac{\theta}{\theta+b(p-\beta) T_{w}}\right)^{T}-\left(\frac{\theta}{\theta+b(p-\beta)\left(T_{w}+x\right)}\right)^{T}\right) \times \\
& {\left[1-\frac{a}{(p-\beta)} e^{-b(p-\beta) T}\left(\left(\frac{\theta}{\theta+b(p-\beta) T_{w}}\right)^{T}-\left(\frac{\theta}{\theta+b(p-\beta)\left(T_{w}+x\right)}\right)^{T}\right)\right] } \\
& -C_{5}(p-\beta) a b^{2} R\left(T_{w} \mid T\right) \times\left(1-\left(\frac{\theta}{\theta+b(p-\beta) T_{w}}\right)^{T}\right) \times \\
& {\left[1-\frac{a}{(p-\beta)} e^{-b(p-\beta) T}\left(1-\left(\frac{\theta}{\theta+b(p-\beta) T_{w}}\right)^{T}\right)\right] } \\
C=\mu_{w} & C_{3}(p-\beta) a b^{2}\left(1-\left(\frac{\theta}{\theta+b(p-\beta) T_{w}}\right)^{T}\right) \\
& -C_{2} \mu_{y}(p-\beta) a b^{2}
\end{aligned}
$$

It can be shown that the function $u(T)$ decreases as $T$ increases.
Theorem 10.5 (Teng and Pham 2004): Given $C_{0}, C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}, x$, $\mu_{y}, \mu_{w}, T_{w}$, the optimal value of $T$, say $T^{*}$, which maximizes the expected net gain of the software development process $E(T)$, is as follows1. If $u(0) \leq C$ and
(a) If $y(0) \leq 0$, then $T^{*}=0$;
(b) If $y(\infty)>0$, then $T^{*}=\infty$;
(c) If $y(0)>0, y(\mathrm{~T}) \geq 0$ for $\mathrm{T} \in\left(0, T^{\prime}\right]$ and $y(T)<0$ for $T \in\left(T^{\prime}, \infty\right]$, then $T^{*}=T^{\prime}$ where $T^{\prime}=y^{-1}(0)$
2. If $u(\infty)>C$ and
(a) If $y(0) \geq 0$, then $T^{*}=\infty$;
(b) If $y(\infty)<0$, then $T^{*}=0$;
(c) If $y(0)<0, y(T) \leq 0$ for $T \in\left(0, T^{\prime \prime}\right]$ and $y(T)>0$ for $T \in\left(T^{\prime \prime}, \infty\right]$, then: $T^{*}=\infty$ if $E(0)<E(\infty)$
$T^{*}=0$ if $E(0) \geq E(\infty)$
where $T^{\prime \prime}=y^{-1}(0)$
3. If $u(0)>C, u(\mathrm{~T}) \geq C$ for $T \in\left(0, T^{0}\right]$ and $u(T)<C$ for $T \in\left(T^{0}, \infty\right]$ where $T^{0}=u^{-1}(C)$, then:
(a) If $y(0)<0$, then

If $y\left(T^{0}\right) \leq 0$, then $T^{*}=0$
If $y\left(T^{0}\right)>0$, then

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0) \geq E\left(T_{b}\right) \\
& T^{*}=T_{b} \text { if } E(0)<E\left(T_{b}\right) \\
& \text { where } T_{b}=y^{-1}(0) \text { and } T_{b} \geq T^{0}
\end{aligned}
$$

(b) If $y(0) \geq 0$, then $T^{*}=T_{c}$, where $T_{c}=y^{-1}(0)$

# Proof: Problem 9. 

### 10.6.2 Applications

The data in Tables 10.4 and 10.5 show, respectively, the normalized time and cumulative failures during in-house testing and field operation per system day of a software telecommunication product (Teng and Pham 2004).

In Table 10.4, the last normalized time point $t_{0}=0.0184$ is the actual stopping in-house testing time for this real application. After $t_{0}$, the software is released for the field operation. Table 10.5 shows the normalized field data for this software application.

The parameters of the NHPP model in equation (10.30) based on the MLE method with $p=1$ is given by

$$
\hat{a}=207.97, \hat{b}=0.00179, \hat{\gamma}=0.5194, \hat{\theta}=5.6244, \hat{\beta}=0
$$Table 10.4. Normalized cumulative failures during in-house testing period

| Time | Failures | Time | Failures |
| :--: | :--: | :--: | :--: |
| 0.00010 | 0.02488 | 0.00704 | 0.52239 |
| 0.00017 | 0.02985 | 0.00768 | 0.54726 |
| 0.00024 | 0.06468 | 0.00858 | 0.58209 |
| 0.00033 | 0.06468 | 0.00954 | 0.61194 |
| 0.00051 | 0.10945 | 0.01048 | 0.63682 |
| 0.00061 | 0.11940 | 0.01138 | 0.64677 |
| 0.00079 | 0.14428 | 0.01207 | 0.67662 |
| 0.00116 | 0.16915 | 0.01285 | 0.70149 |
| 0.00162 | 0.19900 | 0.01347 | 0.73632 |
| 0.00226 | 0.22886 | 0.01424 | 0.77612 |
| 0.00281 | 0.26368 | 0.01467 | 0.77612 |
| 0.00327 | 0.31343 | 0.01553 | 0.81592 |
| 0.00382 | 0.34826 | 0.01639 | 0.82587 |
| 0.00437 | 0.35323 | 0.01717 | 0.84079 |
| 0.00483 | 0.36816 | 0.01755 | 0.84577 |
| 0.00529 | 0.38806 | 0.01796 | 0.87562 |
| 0.00584 | 0.44776 | 0.01836 | 0.89552 |
| 0.00640 | 0.48756 | 0.01840 | 0.90050 |

Please note that the MLE results listed above are actual results, not the normalized results, since they can be more helpful to understand the software development process. Therefore, the mean value function becomes

$$
m(t)=\left\{\begin{array}{lr}
m_{1}(t)=207.97\left(1-e^{-0.00179 t}\right) & \mathrm{t} \leq T \\
m_{2}(t)=207.97\left(1-e^{-0.00179 T}\left(\frac{\theta}{\theta+0.00179 \cdot(t-T)}\right)^{T}\right) & t \geq T
\end{array}\right.
$$

Figure 10.4 shows the mean value function and normalized cumulative software failures fitting curve during in-house testing and field operation.

The cost coefficients can be commonly determined by empirical data or by previous experiences. In this example, we use the following cost coefficients and parameter values:
$C_{0}=50, \quad C_{1}=100, \quad C_{2}=60, \quad C_{3}=3600, \quad C_{4}=300000, \quad C_{5}=500000$, $C_{6}=100000, \mu_{y}=0.1, \mu_{w}=0.5, T_{w}=1000, x=4000$.

From Theorem 10.5, we can obtain the (normalized) optimum release time and the corresponding maximum expected net gain of the software development as follows:

$$
T^{*}=0.0663 \quad E\left(T^{*}\right)=179,012.2
$$Compared with the actual software stopping testing time $t_{0}=0.0184$ and based on the the optimal release time $T^{*}=0.066291$, this shows that one need to continue to do in-house testing after $t_{0}$ until $T^{*}$.

Table 10.5. Normalized cumulative failures and times during field operation

| Time | Failures | Time | Failures |
| :--: | :--: | :--: | :--: |
| 0.04310 | 0.90547 | 0.50111 | 0.98507 |
| 0.06162 | 0.91045 | 0.53383 | 0.98507 |
| 0.08015 | 0.92040 | 0.57309 | 0.98507 |
| 0.08632 | 0.92537 | 0.62580 | 0.99005 |
| 0.13573 | 0.93035 | 0.66560 | 0.99005 |
| 0.14190 | 0.93532 | 0.67887 | 0.99005 |
| 0.16660 | 0.94527 | 0.72531 | 0.99005 |
| 0.20983 | 0.94527 | 0.75185 | 0.99005 |
| 0.22229 | 0.95025 | 0.75849 | 0.99005 |
| 0.2534 | 0.95025 | 0.77176 | 0.99005 |
| 0.25967 | 0.95025 | 0.79829 | 0.99005 |
| 0.26590 | 0.95025 | 0.82511 | 0.99005 |
| 0.27213 | 0.95522 | 0.84529 | 0.99005 |
| 0.29705 | 0.96020 | 0.85201 | 0.99005 |
| 0.30328 | 0.97015 | 0.90583 | 0.99005 |
| 0.31575 | 0.97512 | 0.91255 | 0.99005 |
| 0.34067 | 0.97512 | 0.91928 | 0.99005 |
| 0.34690 | 0.97512 | 0.93946 | 0.99502 |
| 0.39674 | 0.97512 | 0.94619 | 0.99502 |
| 0.40297 | 0.98010 | 0.95291 | 1 |
| 0.42914 | 0.98507 | 0.98655 | 1 |
| 0.435684 | 0.98507 | 1 | 1 |
| 0.474941 | 0.98507 |  |  |

Figure 10.4 seems to indicate that this specific software application appears to be more reliable in field than in testing environments. Figure 10.5 shows the expected net gain function $E(T)$ curve. Figure 10.6 shows the software reliability growth curve $R\left(x \mid T+T_{w}\right)$ for various value of $T$ where $T_{w}$ and $x$ are fixed.

Figure 10.4. Failures and mean value function fitting curve


Figure 10.5. Expected net gain $E(T)$

Figure 10.6. Software reliability growth curve $R\left(x \mid T+T_{w}\right)$

# 10.7 Other Cost Models 

Pham and Wang (2001a) presented a software cost model based on the quasi renewal processes. If the inter-arrival time represents the error-free time (time between errors), a quasi renewal process can be used to model reliability growth for software. For example, suppose that all faults of the software have the same chance of being detected. If the inter-arrival times of a quasi renewal process represent the error-free times of the software, the expected cumulative number of software faults in $[0, t)$ can be described by the renewal function $M(t)$ with parameter . Let $\bar{M}(t)$ be the number of remaining software faults at time $t$. It follows that $\bar{M}(t)=M(\tau)-M(t)$ where $M(\tau)$ is the number of faults which can be detected through a long testing time $\tau$, relative to $t$.

## Notation

$c_{1} \quad$ The cost of fixing a fault during testing phase
$c_{2} \quad$ The cost of fixing a fault during operation phase
$c_{3} \quad$ The cost of testing per unit time
$T \quad$ The software release time
$T_{d} \quad$ The scheduled delivery time
$g(t) \quad$ The probability density function of the life-cycle length $(t>0)$
$c_{p}(t)$ A penalty cost for a delay of delivering software
$\mathrm{M}(\mathrm{t}) \quad$ Number of faults which can be detected through a period of testing time $t$.The expected total software life-cycle cost can be defined as follows:

$$
\begin{aligned}
C(T) & =c_{S} T+c_{t} M(T) \\
& +\int_{T}^{\infty} c_{S}[M(t)-M(T)] g(t) d t+I\left(T-T_{d}\right) c_{p}\left(T-T_{d}\right)
\end{aligned}
$$

where $I(t)$ is an indicator function, that is,

$$
I(t)= \begin{cases}1 & \text { if } t \geq 0 \\ 0 & \text { otherwise }\end{cases}
$$

$M(t)$ and $\operatorname{Var}[N(t)]$ contains some unknown parameters. Those unknown parameters can be obtained by using the MLE (discussed in Chapter 5) or least squares methods (in Chapter 2). Detailed optimal release policies and findings can be found in (Pham 2001a).

# 10.8 Further Reading 

Some interesting papers on cost models and books are:
H. Pham, "Software reliability and cost models: Perspectives, comparison and practices,"European Journal of Operational Research, vol 149, 2003
B.W. Boehm, C. Abts, A.W. Brown, S. Chulani, et al., Software Cost Estimation with COCOMO II, 2000, Prentice-Hall
H. Pham (Ed.), Handbook of Reliability Engineering, Springer 2003

### 10.9 Problems

1. Show that the function $g(T)$ in equation (10.9) is increasing in $T$.
2. Show that the function $u(T)$ in equation (10.25) is increasing in $T$.
3. Complete the proof of Case 3 in Theorem 10.3.
4. Prove Theorem 10.2 .
5. Assume that the risk cost due to software failure after releasing the software beyond the warranty period, $E_{4}(T)$, is given by

$$
E_{4}(T)=C_{4}\left[1-R\left(x \mid T+T_{w}\right)\right)]
$$From equation (10.24), the expected total software cost $E(T)$ can be modified as follows:

$$
\begin{aligned}
E(T)=C_{0} & +C_{1} T^{\alpha}+C_{2} m(T) \mu_{y} \\
& +C_{3} \mu_{w}\left[m\left(T+T_{w}\right)-m(T)\right] \\
& \left.+C_{4}\left[1-R\left(x \mid T+T_{w}\right)\right)\right]
\end{aligned}
$$

where

$$
R\left(x \mid\left(T+T_{w}\right)\right)=e^{-a e^{-b\left(T+T_{w}\right)}\left[1-e^{-b x}\right]}
$$

Given $C_{0}, C_{1}, C_{2}, C_{3}, C_{4}, x, \mu_{y}, \mu_{w}, T$, show that the optimal value of $T$, say $T^{*}$, which minimizes the expected total cost of the software, is given as below:

1. If $v(0) \geq C$, and
(a) If $y(0) \geq 0$, then $T^{*}=0$;
(b) If $y(\infty)<0$, then $T^{*}=\infty$;
(c) If $y(0)<0, y(T)<0$ for any $T \in\left(0, T^{\prime}\right)$ and $y(T)>0$ for any $T \in\left(T^{\prime}, \infty\right)$, then $T^{*}=T^{\prime}$, where $T^{\prime}=y^{-1}(0)$
2. If $v(\infty)<C$, and
(a) If $y(0) \leq 0$, then $T^{*}=\infty$;
(b) If $y(\infty)>0$, then $T^{*}=0$;
(c) If $y(0)>0, y(T)>0$ for any $T \in\left(0, T^{\prime \prime}\right)$ and $y(T)<0$ for any $T \in\left(T^{\prime \prime}, \infty\right)$, then

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0) \leq \mathrm{E}(\infty) \\
& T^{*}=\infty \text { if } E(0)>\mathrm{E}(\infty) \\
& \text { where } T^{\prime \prime}=\inf \{T: y(T)<0\}
\end{aligned}
$$

3. If $v(0)<C, v(T) \leq C$ for $T \in\left(0, T_{0}\right]$ and $v(T)>C$ for $T \in\left(T_{0}, \infty\right)$, where $T_{0}=\left\{T: T=v^{-1}(\mathrm{C})\right\}$ then
(a) If $y(0) \geq 0$, then

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0) \leq E\left(T_{b}\right) \\
& T^{*}=T_{b} \text { if } E(0)>E\left(T_{b}\right) \\
& \text { where } T_{b}=\inf \left\{T>T_{a}: T=y^{-1}(0)\right\}
\end{aligned}
$$

(b) If $y(0)<0$, then $T^{*}=T_{b}$ ' minimizes $E(T)$ where

$$
\begin{aligned}
& T_{b}^{\prime}=\inf \left\{T: T=y^{-1}(0)\right\} \\
& y(T)=\alpha C_{1} T^{(\alpha-1)}-\mu_{w} C_{3} a b e^{-b T}\left(1-e^{-b T}\right) \\
& \quad-a b e^{-b T}\left[C_{4}\left(1-e^{-b x}\right) e^{-b\left(T+T_{w}\right)} R\left(x \mid T+T_{w}\right)\right)-C_{2} \mu_{y} \\
& v(T)=a b^{2} C_{4}\left(1-e^{-b x}\right) e^{-b T_{w}} R\left(x \mid\left(T+T_{w}\right)\right)\left[1-a e^{-b T}\left(1-e^{-b x}\right)\right] \\
& +\alpha(\alpha-1) C_{1} T^{(\alpha-2)} e^{b T} \\
& C=C_{2} \mu_{y} a b^{2}-\mu_{w} C_{3} a b^{2}\left(1-e^{-b T_{w}}\right)
\end{aligned}
$$

6. Given $C_{0}=\$ 100, C_{1}=\$ 50, C_{2}=\$ 25, C_{3}=\$ 100, C_{4}=\$ 1,000, \mu_{\mathrm{y}}=0.1, \mu_{\mathrm{w}}=$ $0.5, x=0.05$, and $T_{\mathrm{w}}=20, \alpha=0.95$, using the results in Problem 5, show that therelease times and the corresponding expected total software cost are given in Table A below.

Table A. Optimal release time

| Release time $T^{*}$ <br> (hours) | Expected total cost $E(T)$ <br> $(\$)$ |
| :--: | :--: |
| 21.5 | 1,806.69 |
| 22.0 | 1,801.17 |
| 22.5 | 1,797.18 |
| 23.0 | 1,794.65 |
| $23.5^{*}$ | 1,793.47 |
| 24.0 | 1,793.56 |
| 24.5 | 1,794.85 |
| 25.0 | 1,797.27 |
| 25.5 | 1,800.74 |

7. Given $C_{0}=\$ 100, C_{1}=\$ 10, C_{2}=\$ 5, C_{3}=\$ 100, C_{4}=\$ 1,000, \mu_{\mathrm{r}}=0.1, \mu_{\mathrm{w}}=0.5$, $x=0.05$, and $T_{\mathrm{w}}=20, \alpha=0.95$, using the results in Problem 5, show that the optimal release time and the corresponding expected total software cost are 37 and $\$ 545.2$, respectively.
8. Prove Theorem 10.4
9. Prove Theorem 10.5# Complex Fault-tolerant System Reliability Modeling 

### 11.1 Introduction

Computer systems are now applied to many important areas such as defense, transportation, and air traffic control. Therefore, fault-tolerance has become one of the major concerns of computer designers. Fault-tolerant computer systems are defined as systems capable of recovery from hardware or software failure to provide uninterrupted real-time service.

It is important to provide very high reliability to critical applications such as aircraft controller and nuclear reactor controller software systems. No matter how thorough the testing, debugging, modularization, and verification of software are, design bugs still plague the software. After reaching a certain level of software refinement, any effort to increase the reliability, even by a small margin, will increase exponential cost. Consider, for example, fairly reliable software subjected to continuous testing and debugging, and guaranteed to have no more than 10 faults throughout the lifecycle. In order to improve the reliability such that, for example, only seven faults may be tolerated, the effort and cost to guarantee this may be enormous. A way of handling unpredictable software failure is through fault-tolerance. Over the last three decades, there has been considerable research in the area of fault-tolerant software.

Fault-tolerant software has been considered for use in a number of critical areas of application. For example, in traffic control systems, the Computer Aided Traffic Control System (COMTRAC) (Lala 1985) is a fault-tolerant computer system designed to control the Japanese railways. It consists of three symmetrically interconnected computers. Two computers are synchronized at the program task level while the third acts as an active-standby. Each computer can be in one of the following states: on-line control, standby, or offline. The COMTRAC software has a symmetric configuration. The configuration system contains the configuration control program and the dual monitor system contains the state control program. When one of the computers under dual operation has a fault, the state control program switches the system to single operation and reports the completion of the system switching to the configuration control program. The configuration control program commands the state control program to switchover to dual operation withthe standby computer. The latter program then executes the system switchover, transferring control to the configuration control program, which judges the accuracy of the report and indicates its own state to the other computers. The COMTRAC shows that it failed seven times during a three-year period - once due to hardware failure, five times due to software failure, and once for unknown causes.

Another example is the NASA space shuttle. The shuttle carries a configuration of four identical flight computers, each loaded with the same software, and a fifth computer developed by a different manufacturer and running dissimilar (but functionally equivalent) software. This software is executed only if the ones in the other four processors cannot reach consensus during critical phases of the flight (Spector 1984).

Software fault-tolerance is achieved through special programming techniques that enable the software to detect and recover from failure incidents. The method requires redundant software elements that provide alternative means of fulfilling the same specifications. The different versions must be such that they will not all fail in response to the same circumstances. Many researchers have investigated and suggested that diverse software versions developed using different specifications, designs, programming teams, programming languages, etc., might fail in a statistically independent manner. Empirical evidence questions that hypothesis (Leveson 1990). On the other hand, almost all software fault-tolerance experiments have reported some degree of reliability improvement (Avizienis 1988).

Software fault-tolerance is the reliance on design redundancy to mask residual design faults present in software programs (Pham 1992a). Fault-tolerance, however, incurs costs due to the redundancy in hardware and software resources required to provide backup for system components. We must weigh the cost of fault-tolerance against the cost of software failure. With the current growth of software system complexity, we cannot afford to postpone the implementation of fault-tolerance in critical areas of software application.

This chapter discusses a basic concept for fault-tolerant software techniques and some advanced techniques including self-checking systems. We then give the reliability analysis of fault-tolerant software schemes such as recovery block (RB), N -version programming (NVP), and hybrid fault-tolerant systems. Basically, in the last system, an RB can be embedded within an NVP by applying the RB approach to each version of the NVP. Similarly, an NVP can be nested within an RB.

This chapter describes a software reliability growth model for triple-version programming (TVP) systems based on the NHPP. This chapter also discusses a reliability study in modeling the interactions between the hardware and the software component.

# 11.2 Basic Fault-tolerant Software Techniques 

The study of software fault-tolerance is relatively new as compared with the study of fault-tolerant hardware. In general, fault-tolerant approaches can be classified into fault-removal and fault-masking approaches. Fault-removal techniques can be either forward error recovery or backward error recovery.Forward error recovery aims to identify the error and, based on this knowledge, correct the system state containing the error. Exception handling in high-level languages, such as Ada and $\mathrm{PL} / 1$, provides a system structure that supports forward recovery. Backward error recovery corrects the system state by restoring the system to a state which occurred prior to the manifestation of the fault. The recovery block scheme provides such a system structure. Another fault-tolerant software technique commonly used is error masking. The NVP scheme uses several independently developed versions of an algorithm. A final voting system is applied to the results of these N -versions and a correct result is generated.

A fundamental way of improving the reliability of software systems depends on the principle of design diversity where different versions of the functions are implemented. In order to prevent software failure caused by unpredicted conditions, different programs (alternative programs) are developed separately, preferably based on different programming logic, algorithm, computer language, etc. This diversity is normally applied under the form of recovery blocks or N -version programming.

Fault-tolerant software assures system reliability by using protective redundancy at the software level. There are two basic techniques for obtaining fault-tolerant software:

- RB scheme
- NVP

Both schemes are based on software redundancy assuming that the events of coincidental software failures are rare.

# 11.2.1 Recovery Block Scheme 

The recovery block scheme, proposed by Randell (1975), consists of three elements: primary module, acceptance tests, and alternate modules for a given task. The simplest scheme of the recovery block is as follows:

Ensure $T$
By P
Else by $Q_{1}$
Else by $Q_{2}$

Else by $Q_{\mathrm{n}-1}$
Else Error
where $T$ is an acceptance test condition that is expected to be met by successful execution of either the primary module $P$ or the alternate modules $Q_{1}, Q_{2}, \ldots, Q_{\mathrm{n}-1}$. The process begins when the output of the primary module is tested for acceptability. If the acceptance test determines that the output of the primary module is not acceptable, it recovers or rolls back the state of the system before the primary module is executed. It allows the second module $Q_{1}$, to execute. The acceptance test is repeated to check the successful execution of module $Q_{1}$. If it fails, then module $Q_{2}$ is executed, etc. The alternate modules are identified by the keywords "else by" When all alternate modules are exhausted, the recovery blockitself is considered to have failed and the final keywords "else error" declares the fact. In other words, when all modules execute and none produce acceptable outputs, then the system falls.

A reliability optimization model has been studied by Pham (1989b) to determine the optimal number of modules in a recovery block scheme that minimizes the total system cost given the reliability of the individual modules. Details of the model can be obtained in Pham (1989b).

In a recovery block, a programming function is realized by $n$ alternative programs, $P_{1}, P_{2}, \ldots, P_{n}$. The computational result generated by each alternative program is checked by an acceptance test, $T$. If the result is rejected, another alternative program is then executed. The program will be repeated until an acceptable result is generated by one of the $n$ alternatives or until all the alternative programs fail.

The probability of failure of the RB scheme, $P_{\mathrm{rb}}$, is as follows:

$$
P_{r b}=\prod_{i=1}^{n}\left(e_{i}+t_{2 i}\right)+\sum_{i=1}^{n} t_{1 i} \mathrm{e}_{1}\left(\prod_{j=1}^{i-1}\left(e_{j}+t_{2 j}\right)\right)
$$

where
$e_{i}=$ probability of failure for version $P_{i}$
$\mathrm{t}_{1 \mathrm{i}}=$ probability that acceptance test $i$ judges an incorrect result as correct
$t_{2 i}=$ probability that acceptance test $i$ judges a correct result as incorrect.
The first term of equation (11.1) corresponds to the case when all versions fall the acceptance test. The second term corresponds to the probability that acceptance test $i$ judges an incorrect result as correct at the $i$ th trial of the $n$ versions.

# 11.2.2 N-version Programming 

The NVP was proposed by Chen and Avizienis (1978) for providing fault-tolerance in software. In concept, the NVP scheme is similar to the N -modular redundancy scheme used to provide tolerance against hardware faults (Lala 1985).

The NVP is defined as the independent generation of $N \geq 2$ functionally equivalent programs, called versions, from the same initial specification. Independent generation of programs means that the programming efforts are carried out by $N$ individuals or groups that do not interact with respect to the programming process. Whenever possible, different algorithms, techniques, programming languages, environments, and tools are used in each effort. In this technique, $N$ program versions are executed in parallel on identical input and the results are obtained by voting on the outputs from the individual programs. The advantage of NVP is that when a version failure occurs, no additional time is required for reconfiguring the system and redoing the computation.

Consider an NVP scheme consists of $n$ programs and a voting mechanism, V. As opposed to the RB approach, all n alternative programs are usually executed simultaneously and their results are sent to a decision mechanism which selects the final result. The decision mechanism is normally a voter when there are more than two versions (or, more than $k$ versions, in general), and it is a comparator whenthere are only two versions ( $k$ versions). The syntactic structure of NVP is as follows:

$$
\begin{aligned}
& \text { seq } \\
& \text { par } \\
& P_{1} \text { (version 1) } \\
& P_{2} \text { (version 2) }
\end{aligned}
$$

$$
\begin{aligned}
& P_{n}(\text { version } n) \\
& \text { decision } V
\end{aligned}
$$

Assume that a correct result is expected where there are at least two correct results. The probability of failure of the NVP scheme, $P_{n}$, can be expressed as

$$
P_{n v}=\prod_{i=1}^{n} e_{i}+\prod_{i=1}^{n}\left(1-e_{i}\right) e_{i}^{-1} \prod_{j=1}^{n} e_{j}+d
$$

The first term of equation (11.2) is the probability that all versions fail. The second term is the probability that only one version is correct. The third term, $d$, is the probability that there are at least two correct results but the decision algorithm fails to deliver the correct result.

Eckhardt and Lee (1985) also developed a statistical model of NVP. In their model, "independently developed versions" are modeled as programs randomly selected from the input space of possible program versions that support problem-solving. Assume that the aggregate fails whenever at least $m$ versions fail. Let $q(x)$ be the proportion of versions failing when executing on input state $x$. Let $Q(A)$ be the usage distribution, the probability that the subset of input state $A$ is selected. Then the reliability of the NVP aggregate is given as

$$
R=1-\int \sum_{i=m}^{N}\binom{N}{i}[q(x)]^{i}[1-q(x)]^{N-i} d Q(A)
$$

where $m=\lfloor 1(\mathrm{~N}+1) / 2\rfloor$ a majority of the $N$ versions. Eckhardt and Lee also noted that independently developed versions do not necessarily fail independently.

It is worthwhile to note that the goal of the NVP approach is to ensure that multiple versions will be unlikely to fail on the same inputs. With each version independently developed by a different programming team, design approach, etc., the goal is that the versions will be different enough in order that they will not fail too often on the same inputs. However, multiversion programming is still a controversial topic.

The main difference between the recovery block scheme and the $N$-version programming is that the modules are executed sequentially in the former. The recovery block generally is not applicable to critical systems where real-time response is of great concern. The $N$-version programming and the recovery block techniques have been discussed in detail by Anderson and Lee (1980).# 11.3 Other Advanced Techniques 

$N$-version programming has been researched thoroughly during the past decade. Correlated errors form a main source of failure of the $N$-version programs (Nicola 1990) and can be minimized by design diversity. A design paradigm has been developed to assure design diversity in $N$-version software. Several experiments (see Lyu 1991; Leveson 1990) have been conducted to validate the assumption of error independence in multiple versions, to analyze the types of faults, to investigate the use of self-checks and voting in error detection, and to establish the need for a complete and unambiguous specification. There has been some effort on modeling the reliability of such fault-tolerant software approaches (Arlat 1990; Belli 1990; Tso 1986; Vouk 1990). Pham (1995) has given a cost model to obtain the optimal number of program versions that minimizes the expected cost of the NVP scheme.

However, in critical systems with real-time deadlines, voting at the end of the program, as in the basic $N$-version programming, may not be acceptable. Therefore, voting at intermediate points is called for. Such a scheme, where the comparison of results is done at intermediate points, is called the community error recovery (CER) scheme (Nicola 1990) and is shown to offer a higher degree of fault-tolerance compared to the basic $N$-version programming. This approach, however, requires the synchronization of the various versions of the software at the comparison points.

Another scheme which adopts intermediate voting is the $N$-program, selfchecking scheme (Yau 1975) where each version is subject to an acceptance test or checking by comparison. When $N=2$, it is a two-version, self-checking scheme or self-checking duplex scheme. Whenever a particular version raises an exception, the correct result is obtained from the remaining versions and execution is continued. This method is similar to the CER approach, with the only difference being the on-line detection in the former by an acceptance test rather than a comparison.

### 11.3.1 Self-checking Duplex Scheme

In this section we discuss an approach, called a self-checking duplex scheme, for the enhancement of software reliability. This scheme incorporates redundancy at two levels and can increase the reliability of software in critical systems significantly.

If individual versions are made highly reliable, an ultra-high reliability can be achieved merely by having two versions. These two versions should be made self-checking and work simultaneously as a duplex system as shown in Pham (2000a) (Figure 7.1). In Pham (2000a) (Figure 7.1) for example, if module $i$ raises an exception, correct results can be obtained from the other version. This approach is known as a self-checking duplex system, illustrating a simple architecture of the system scheme where both versions are represented by a sequence of $N$ modules.

Although $N$ self-checking versions can be used, Pham (1991a) reported a preliminary study that two versions are sufficient to raise the reliability to acceptable levels using our new approach. It is also more practical to have as fewself-checking versions as possible because of the high cost of developing $N$ different self-checking versions.

Self-checking software can be developed in various ways. Self-checking provides an on-line detection of errors and prevents the contamination of the software by not letting the errors manifest. Software integrity can be assured by testing for illegal branching, infinite loops, wrong branching, etc., and testing for functionality and validity of the results. It is easier to incorporate self-checking assertions into the software during the design stage since the team that develops the software is expected to have the best understanding of the problem. A good understanding of the application and the algorithms is deemed important for creating and placing meaningful assertions in the code. Both local and global selfchecking assertions need to be incorporated to guarantee a high reliability. Hua and Abraham (1986) provide a systematic method for developing the self-checking assertions. In the following paragraphs, we show how self-checking assertions can provide ultra-high reliability.

Let the executable assertions be inserted in a module both locally and globally. By inserting local and global assertions, it is possible to check not only the internal states of the modules, but also the input/output specifications. As the inputs to an intermediate module such as $i+1$ (see Figure 7.1 Pham 2000a) are reset to the correct value by the corresponding module of the other version if and only if an error is detected, any undetected error at module $i$ will propagate to the next module $i+1$. Let $p$ represent the probability of detecting an error in module $i$ of a self-checking version. Now, given that an error goes undetected at the ith, $(i+1)$ th, $\ldots,(\mathrm{i}+k-1)$ th module, the probability of this error being detected at the $i+1$ th module of the version is

$$
p_{k}=p \sum_{j=i}^{i+k}(1-p)^{j-i}
$$

Example 11.1: Suppose that the probability of detecting a design error at a particular module by self-checking is 0.9 . If an error is not detected at this module, the probability of this error being detected at the following module, using equation (11.1), is 0.99 and the probability of detecting it at the next module is 0.999 and so on. This establishes that self-checking assertions could be a very powerful tool in increasing software reliability.

# 11.3.2 Hybrid Fault-tolerant Scheme 

A hybrid fault-tolerant system is defined as a software system which combines the RB and NVP schemes in order to improve the reliability of software systems. For simplicity, we only discuss two level hybrid systems. We use the notation $\left(N V P_{n}\right.$, $\mathrm{RB}_{m}$ ) to represent an $n$-version NVP with each version being an $m$-version RB. Similarly, $\left(\mathrm{RB}_{n}, \mathrm{NVP}_{m}\right)$ represents an $n$-version RB with each version being an $m$-version NVR. For example, two of the possible combinations of recovery block and NVP using four versions $P_{1}, P_{2}, P_{3}$, and $P_{4}$, are shown in Figures 11.1 and 11.2.```
/* NVP */
seq
par
/* RB */
ensure T
by P P (version 1)
    else by P P (version 2)
        else error;
/* RB */
ensure T
by P P (version 3)
    else by P P (version 4)
else error;
```

Figure 11.1. $\left(\mathrm{NVP}_{2}, \mathrm{RB}_{2}\right)$ configuration.

```
/* RB */
ensure T
by /* NVP */
seq
    par
    P P (version 1);
    P P (version 2);
decision V
else by /* NVP */
seq
par
    P P (version 3);
    P P (version 4);
decision V
```

Figure 11.2. $\left(\mathrm{RB}_{2}, \mathrm{NVP}_{2}\right)$ configuration.
Without loss of generality, we discuss here the hybrid fault-tolerant schemes (see Figure 7.3 in Pham 2000a) with only two levels: RB embedded in NVP or NVP embedded in RB. Figure 7.3 in Pham (2000a) shows the basic structure of a two-level hybrid fault-tolerant scheme. The first level consists of $P_{i}$ basic program versions which form the second level composite program modules $M_{j}$ where $1 \leq i \leq$ $n$ and $1 \leq i \leq m$. If RB (or NVP) is used at the first level, NVP (or RB) is used at the second level. The composite version failure rates of the program version are $e_{i}$, acceptance test error probabilities are $t_{1}$, and $t_{2}$, and the decision error probability is $d$. The hybrid fault-tolerant scheme's reliability can be obtained by calculating the reliability of the lower level program versions or composite versions, and then using the lower level reliabilities as inputs to the higher level composite versions. This process is repeated until the total system reliability is obtained. Mathemati-cally, the probability of failure of the hybrid system, $P_{h}$, is calculated by using equations (11.1) and (11.2) where the program version's failure rates $e_{i}$ are substituted by $P_{r b}(i)$ or $P_{n v}(i)$. We now obtain

$$
P_{h}(r b)=\prod_{i=1}^{n}\left(P_{n v}(i)+t_{2 i}\right)+\sum_{i=1}^{n} t_{1 i} P_{n v}(i)\left(\prod_{j=1}^{i-1}\left(P_{n v}(j)+t_{2 j}\right)\right)
$$

for hybrid systems with a recovery block where each version is an NVP scheme and

$$
P_{h}(n v)=\prod_{i=1}^{n} P_{r b}(i)+\sum_{i=1}^{n} \frac{\left(1-P_{r b}(i)\right)}{P_{r b}(i)}\left(\prod_{j=1}^{n} P_{r b}(j)\right)+d
$$

for hybrid systems with an NVP where each version is a recovery block.

# 11.3.3 Reduction of Common-cause Failures 

Before the $N$-version programming schemes can be applied to enhance the reliability of critical software, such as the nuclear reactor controller system and the fly-by-wire aircraft, their feasibility should be determined. Both the nuclear reactor controller and fly-by-wire software require ultra-high reliability. The existing $N$-version schemes may be unable to offer the required reliability because of their vulnerability to failures due to identical causes. If the majority of the versions fail because of common design errors, then a wrong result may be given by voting on incorrect outputs. The likelihood of common-cause failures in nuclear controller software cannot be ruled out because of its complexity.

Methods to alleviate the common-cause failures include the development of diverse versions by independent teams so as to minimize the commonalities between the various versions. According to Knight and Leveson (1986), experiments have shown that the use of different languages and design philosophy has little effect on the reliability in $N$-version programming because people tend to make similar logical mistakes in a difficult-to-program part of the software. Thus, in the presence of a common-cause failure, all the different variations of the $N$-version programming prove to be equally useless. It seems beneficial to have a single version in order to minimize cost.

According to the latest research on software reliability, fault-tolerance is a highly recommended application for critical systems. However, a new approach that could alleviate the weakness of the existing fault-tolerant software reliability models is even more desirable. An empirical study by Leveson et al. (1990) suggests not to utilize the $N$-version if it is known that the probability of making common mistakes during programming is unavoidable. Furthermore, Pham et al. (1991a) recommend (1) developing fewer versions, (2) minimizing the errors in the individual versions, and (3) minimizing or eliminating the incidence of common-cause failures in these versions. The author suggests that either two or three versions is reasonably good for a fault tolerant system to achieve the desiredreliability goal given that each version is likely to be reliable based on a realistic reliability evaluation.

Clearly, complex software is developed in a modular fashion and not all the modules are equally complex and difficult to design. Therefore, it is accurate to conclude that the common-cause failures are confined to the "difficult to understand and design logically" part of the problem. The common-cause failures can be reduced if such critical parts are identified and certain design guidelines are followed.

Some suggestions of the design guidelines to reduce or eliminate the common-cause failures are as follows (Pham et al. 1991a):

- Techniques to identify critical parts in a program. Generally, the control flow complexity of an algorithm indicates the level of difficulty. We can therefore use the McCabe measure to identify the critical parts of a program.
- The manager of the project should identify the critical sections of the problem, meet the development teams, and steer them to different techniques for solving the critical parts. Suppose that the critical part involves sorting a file. Then one team should be asked to use Quicksort, the other teams should be asked not to use Quicksort but to use some other naïve scheme. In this way, the probability of committing identical logical mistakes can be reduced or eliminated.

Further research on the development of additional design guidelines to minimize the common-cause failures should also be studied.

The self-checking duplex scheme discussed in Section 11.3 incorporates fault-tolerance in two layers. The first layer of protection is provided by self-checking assertions. The second layer is duplication.

In the self-checking system, if one of the versions detects an error at the end of the current module, results are obtained from the other version. After exchanging the correct results, both versions will continue execution in a lock-step fashion. Finally, the output of the duplicated versions are compared for consistency before accepting the result as correct. By keeping the size of the modules sufficiently small, a larger number of errors can be masked by this approach. However, too small a size for the module will increase the overhead of implanting the self-checking assertions. The analysis of the reliability and the optimal module size selection requires further research.

Common-cause failure is still a problem in the self-checking duplex system. There is no known technique to address this in $N$-version programming. Therefore, it can only be attempted to reduce the common-cause failures by design diversity. A summary of references on fault-tolerant systems is given in Table 11.1.Table 11.1. Summary of references

| Group models | References |
| :-- | :-- |
| General fault <br> tolerant systems | Abbott (1990); Anderson (1980, 1985); Arlat (1990); Geist <br> (1990); Hecht (1979); Iyer (1985); Kanoun (1993); Kim <br> (1989); Laprie (1990); Leveson (1990); Pham. (1989, <br> 1992); Siewiorek (1990) |
| N -version <br> programming | Anderson (1980, 1985); Avizienis (1977, 1988); Chen <br> (1978); Gersting (1991); Kelly (1988); Knight (1986); <br> Pham (1995); Shimeall (1991); Tso (1987); Vouk (1990) |
| Recovery block | Kim (1988); Laprie (1990); Pham (1989); Randell (1975) |
| Other | Eckhardt (1985); Hua (1986); Kim (1989); Nicola (1990); |
| fault-tolerant | Pham (1991b, 1992a); Taylor (1980); Vouk (1990) |
| techniques |  |

# 11.4 Triple-version Programming Model with Common Failures 

This section discusses a recent software reliability growth model (SGRM) for a triple-version programming (TVP) system with common failures based on NHPP based solely on the papers recently published by Teng and Pham (2002, 2003).

Although diverse software versions are developed by using different specifications, designs, programming teams, programming languages, etc., many researchers have revealed that those independently developed software versions do not necessarily fail independently. In this section we refer to related faults as common faults for simplicity. Figure 11.3 illustrates the common faults and the independent faults in a two-version system.

Common Faults are those which are located in the functionally equivalent modules among two or more software versions because their programmers are prone to making the same or similar mistakes although they develop different versions independently. Those faults will be activated by the same input to cause those versions to fail simultaneously, and these failures by common faults are called Common Failures.

Independent Faults are usually located in different or functionally unequivalent modules between or among different software versions. Since they are independent of each other and are considered harmless to the fault-tolerant systems because their resulting failures are typically distinguishable to the decision mechanism.

However, there is still a probability, though very small compared with that of Common Failures, that an unforeseeable input activates two independent faults in different software versions that will lead those versions to fail at the same time. These failures by independent faults are called Concurrent Independent Failures.

Figure 11.3. Common faults and independent faults
Table 11.2 shows the differences between the common failures and the concurrent independent failures. This section considers that the software failures in TVP systems have two modes: a common failure mode and an s-independent failure mode. There are three independently developed software versions 1,2 , and 3 in the system, which uses majority voting. The reliability of the voter is assumed to be 1 .

Table 11.2. Common failures and concurrent independent failures

|  | Common failures | Concurrent independent <br> failures |
| :--: | :-- | :-- |
| Fault type | Common faults | Independent faults |
| Output | Usually the same | Usually different |
| Fault location <br> (logically) | Same | Different |
| Voting result <br> (majority voting) | Choose wrong <br> solution | Unable to choose correct <br> solution || Notation |  |
| :--: | :--: |
| A | Independent faults in version 1 |
| $B$ | Independent faults in version 2 |
| C | Independent faults in version 3 |
| $A B$ | Common faults between version 1 and version 2 |
| $A C$ | Common faults between version 1 and version 3 |
| $B C$ | Common faults between version 2 and version 3 |
| $A B C$ | Common faults among version 1, version 2 and version 3 |
| $N_{x}(t)$ | Counting process which counts the number of type $x$ faults discovered up to time $t, x=A, B, C, A B, A C, B C$ and $A B C$ |
| $N_{d}(t)$ | $\begin{gathered} N_{a}(t)=N_{A B}(t)+N_{A C}(t)+N_{B C}(t)+N_{A B C}(t) \\ \text { Counting process which counts common faults discovered in the } \\ \text { NVP system up to time } t \end{gathered}$ |
| $m_{x}(t)$ | Mean value function of counting process $N_{x}(t), m_{x}(t)=E\left[N_{x}(t)\right]$ $x=A, B, C, A B, A C, B C, A B C$ and $d$ |
| $a_{x}(t)$ | Total number of type $x$ faults in the system plus those type $x$ faults already removed from the system at time $t . a_{x}(t)$ is nondecreasing function, and $a_{x}(0)$ denotes the initial number of type $x$ fault in the system, $x=A, B, C, A B, A C, B C$ and $A B C$ |
| $b(t)$ | Failure detection rate per fault at time $t$ |
| $\beta_{1}, \beta_{2}, \beta_{3}$ | The probability that a new fault is introduced into version 1,2 and 3 during the debugging, respectively |
| $p_{1}, p_{2}, p_{3}$ | The probability that a new fault is successfully removed from version 1,2 and 3 during the debugging, respectively |
| $X_{A}(t), X_{B}(t)$, $X_{C}(t)$ | Number of type $\mathrm{A}, \mathrm{B}$ and C faults at time $t$ remaining in the system respectively |
| $R(x \mid t)$ | Software reliability function for given mission time $x$ and time to stop testing $t$ $R(x \mid t)=\operatorname{Pr}\{$ No failure occurs during $(t, t+x) \mid$ stop testing at $t\}$ |
| $R_{\text {NVP-SRGM }}(x \mid t)$ | NVP system reliability function for given mission time $x$ and time to stop testing $t$ with consideration of common failures in the NVP system |
| $R_{\text {Ind }}(x \mid t)$ | NVP system reliability function for given mission time $x$ and time to stop testing $t$, assuming no common failures in the NVP system, i.e., the versions are totally independent of each other. |
| $K_{A B}, K_{A C}, K_{B C}$ | Failure intensity per pair of faults for concurrent independent failures between version 1 and 2, between 1 and 3 and between 2 and 3 respectively |
| $N_{\overline{A B}}(t), N_{\overline{A C}}(t)$ | Counting processes that count the number of concurrent independent failures involving version 1 and 2 , version 1 and 3 , and version 2 and 3 up to time $t$ respectively |
| $N_{\overline{B C}}(t)$ | Counting process that counts the total number of concurrent independent failures up to time $t$, $N_{I}(t)=N_{\overline{A B}}(t)+N_{\overline{A C}}(t)+N_{\overline{B C}}(t)$ || $m_{\overline{A B}}(t), m_{\overline{A C}}(t)$ | Mean value functions of the corresponding counting processes. |
| :-- | :-- |
| $m_{\overline{B C}}(t), m_{l}(t)$ | For example, $m_{\overline{A B}}(t)=E\left[N_{\overline{A B}}(t)\right]$ |
| $h_{\overline{A B}}(t), h_{\overline{A C}}(t)$ | Failure intensity functions of concurrent independent failures |
| $h_{\overline{B C}}(t)$ | involving version 1 and 2, between 1 and 3, and between 2 and 3 |
|  | $h_{\overline{A B}}(t)=\frac{d}{d t} m_{\overline{A B}}(t)$ |
| $\operatorname{Pr}(\cdot \mid T)$ | Conditional probability given that testing and debugging are |
|  | stopped at time $T$ |

A concurrent independent failure occurs when two or more versions fail by independent faults at the same input, i.e., $A, B$ or $C$, not by $A B, A C$, etc. Different fault types and their relations are shown in Figure 11.4.


Figure 11.4. Different software faults in the 3 -version software system

# 11.4.1 Modeling Assumptions 

Consider the following assumptions:

1. Faster versions will have to wait for the slowest versions to finish (prior to voting).
2. Each software version can fail during execution, caused by faults in the software.
3. Two or more software versions may fail on the same input, which can be caused by either the common faults or the independent faults in different versions.
4. The occurrence of software failures caused by different faults (independent faults, 2-version common faults or 3-version common faults) follows an NHPP.5. The software-failure detection rate at any time is proportional to the number of faults remaining in the software at that time.
6. When a software failure occurs in any of the three versions, a debugging effort is executed immediately. That effort removes the faults immediately with probability $p_{i}, p_{i}>>1-p_{i}$ ( $i$ representing the version number 1,2 or 3 ).
7. For each debugging effort, whether the fault is successfully removed or not, some new independent faults may be introduced into the software system with probability $\beta_{i}, \beta_{i}<<p_{i}$ but no new common faults will be introduced into the system.
8. Some common faults may reduce to some low-level common faults or independent faults due to unsuccessful removal efforts.
9. The error detection rates per fault for all kinds of faults $A, B, C, A B, A C, B C$ and $A B C$ are the same and constant, i.e., $b(t)=b$.
10. The concurrent independent failures are caused by the activation of independent faults between different versions, and the probability that a concurrent independent failure involves three versions is zero. Those failures only involve two versions.
11. Any pair of remaining independent faults between versions has the same probability to be activated by some input.
12. The intensity for concurrent independent failures involving any two versions is proportional to the remaining pairs of independent faults in those two versions.

Figure 11.5 shows the pairs of independent faults between software version 1 and version 2. There are three independent faults (type A) in version 1, and there are two independent faults (type B) in version 2. There are six pairs of independent faults between version 1 and version 2. It is assumed that each of these six pairs has the same probability to be activated by some input.


Figure 11.5. Independent fault pairs between version 1 and version 2
Based on the above assumptions and the software reliability model studied by Zhang et al. ((2003) (Equations 1,2 and 9 therein), the following NHPP system of equations for different faults and software failures can be obtained:(1) Error type ABC

$$
m_{A B C}^{\prime}(t)=b \cdot\left(a_{A B C}-p_{1} \cdot p_{2} \cdot p_{3} \cdot m_{A B C}(t)\right)
$$

with marginal conditions $m_{A B C}(0)=0$ and $a_{A B C}(0)=a_{A B C}$. The solution to equation (11.6) is

$$
m_{A B C}(t)=\frac{a_{A B C}}{p_{1} \cdot p_{2} \cdot p_{3}} \cdot\left(1-e^{-b \cdot p_{1} \cdot p_{2} \cdot p_{3} \cdot t}\right)
$$

(2) Error type $A B$

$$
\begin{aligned}
& m_{A B}^{\prime}(t)=b \cdot\left(a_{A B}(t)-p_{1} \cdot p_{2} \cdot m_{A B}(t)\right) \\
& a_{A B}^{\prime}(t)=\left(1-p_{1}\right) \cdot\left(1-p_{2}\right) \cdot p_{3} \cdot m_{A B C}^{\prime}(t)
\end{aligned}
$$

Similarly, error type AC

$$
\begin{aligned}
& m_{A C}^{\prime}(t)=b \cdot\left(a_{A C}(t)-p_{1} \cdot p_{3} \cdot m_{A C}(t)\right) \\
& a_{A C}^{\prime}(t)=\left(1-p_{1}\right) \cdot\left(1-p_{3}\right) \cdot p_{2} \cdot m_{A B C}^{\prime}(t)
\end{aligned}
$$

Error type BC

$$
\begin{aligned}
& m_{B C}^{\prime}(t)=b \cdot\left(a_{B C}(t)-p_{2} \cdot p_{3} \cdot m_{B C}(t)\right) \\
& a_{B C}^{\prime}(t)=\left(1-p_{2}\right) \cdot\left(1-p_{3}\right) \cdot p_{1} \cdot m_{A B C}^{\prime}(t)
\end{aligned}
$$

with marginal conditions

$$
\begin{array}{ll}
m_{A B}(0)=0, & a_{A B}(0)=a_{A B} \\
m_{A C}(0)=0, & a_{A C}(0)=a_{A C} \\
m_{B C}(0)=0, & a_{B C}(0)=a_{B C}
\end{array}
$$

Substituting equation (11.7) into equations (11.8)-(11.9), we can obtain the mean value function for $\mathrm{AB}, \mathrm{AC}$ and BC :

$$
\begin{aligned}
& m_{A B}(t)=C_{A B 1}-C_{A B 2} \cdot e^{-b \cdot p_{1} \cdot p_{2} \cdot t}+C_{A B 3} \cdot e^{-b \cdot p_{1} \cdot p_{2} \cdot p_{3} \cdot t} \\
& m_{A C}(t)=C_{A C 1}-C_{A C 2} \cdot e^{-b \cdot p_{1} \cdot p_{2} \cdot t}+C_{A C 3} \cdot e^{-b \cdot p_{1} \cdot p_{2} \cdot p_{3} \cdot t} \\
& m_{B C}(t)=C_{B C 1}-C_{B C 2} \cdot e^{-b \cdot p_{2} \cdot p_{3} \cdot t}+C_{B C 3} \cdot e^{-b \cdot p_{1} \cdot p_{2} \cdot p_{3} \cdot t}
\end{aligned}
$$

where

$$
\begin{gathered}
C_{A B 1}=\frac{a_{A B}}{p_{1} \cdot p_{2}}+\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{2}\right)}{p_{1}^{2} \cdot p_{2}^{2}} \\
C_{A B 2}=\frac{a_{A B}}{p_{1} \cdot p_{2}}+\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{2}\right)}{p_{1}^{2} \cdot p_{2}^{2}}-\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{2}\right)}{p_{1}^{2} \cdot p_{2}^{2} \cdot\left(1-p_{3}\right)}
\end{gathered}
$$$$
\begin{gathered}
C_{A B 3}=-\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{2}\right)}{p_{1}^{2} \cdot p_{2}^{2} \cdot\left(1-p_{3}\right)} \\
C_{A C 1}=\frac{a_{A C}}{p_{1} \cdot p_{3}}+\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{3}\right)}{p_{1}^{2} \cdot p_{3}^{2}} \\
C_{A C 2}=\frac{a_{A C}}{p_{1} \cdot p_{3}}+\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{3}\right)}{p_{1}^{2} \cdot p_{3}^{2}}-\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{3}\right)}{p_{1}^{2} \cdot p_{3}^{2} \cdot\left(1-p_{2}\right)} \\
C_{A C 3}=-\frac{a_{A B C} \cdot\left(1-p_{1}\right) \cdot\left(1-p_{3}\right)}{p_{1}^{2} \cdot p_{3}^{2} \cdot\left(1-p_{3}\right)} \\
C_{B C 1}=\frac{a_{B C}}{p_{2} \cdot p_{3}}+\frac{a_{A B C} \cdot\left(1-p_{2}\right) \cdot\left(1-p_{3}\right)}{p_{2}^{2} \cdot p_{3}^{2}} \\
C_{B C 2}=\frac{a_{B C}}{p_{2} \cdot p_{3}}+\frac{a_{A B C} \cdot\left(1-p_{2}\right) \cdot\left(1-p_{3}\right)}{p_{2}^{2} \cdot p_{3}^{2}}-\frac{a_{A B C} \cdot\left(1-p_{2}\right) \cdot\left(1-p_{3}\right)}{p_{2}^{2} \cdot p_{3}^{2} \cdot\left(1-p_{1}\right)} \\
C_{B C 3}=-\frac{a_{A B C} \cdot\left(1-p_{2}\right) \cdot\left(1-p_{3}\right)}{p_{2}^{2} \cdot p_{3}^{2} \cdot\left(1-p_{1}\right)}
\end{gathered}
$$

(3) Error type A

$$
\begin{gathered}
m_{A}^{\prime}(t)=b \cdot\left(a_{A}(t)-p_{1} \cdot m_{A}(t)\right) \\
a_{A}^{\prime}(t)=\beta_{1} \cdot\left(m_{A}^{\prime}(t)+m_{A B}^{\prime}(t)+m_{A C}^{\prime}(t)+m_{A B C}^{\prime}(t)\right) \\
+\left(1-p_{1}\right) \cdot p_{2} \cdot m_{A B}^{\prime}(t)+\left(1-p_{1}\right) \cdot p_{3} \cdot m_{A C}^{\prime}(t) \\
+\left(1-p_{1}\right) \cdot p_{2} \cdot p_{3} \cdot m_{A B C}^{\prime}(t)
\end{gathered}
$$

Similarly, error type B

$$
\begin{gathered}
m_{B}^{\prime}(t)=b \cdot\left(a_{B}(t)-p_{2} \cdot m_{B}(t)\right) \\
a_{B}^{\prime}(t)=\beta_{2} \cdot\left(m_{B}^{\prime}(t)+m_{A B}^{\prime}(t)+m_{B C}^{\prime}(t)+m_{A B C}^{\prime}(t)\right) \\
+\left(1-p_{2}\right) \cdot p_{1} \cdot m_{A B}^{\prime}(t)+\left(1-p_{2}\right) \cdot p_{3} \cdot m_{B C}^{\prime}(t) \\
+\left(1-p_{2}\right) \cdot p_{1} \cdot p_{3} \cdot m_{A B C}^{\prime}(t)
\end{gathered}
$$

Error type C

$$
m_{C}^{\prime}(t)=b \cdot\left(a_{C}(t)-p_{3} \cdot m_{C}(t)\right)
$$$$
\begin{aligned}
a_{C}^{\prime}(t)= & \beta_{3} \cdot\left(m_{C}^{\prime}(t)+m_{A C}^{\prime}(t)+m_{B C}^{\prime}(t)+m_{A B C}^{\prime}(t)\right) \\
& +\left(1-p_{3}\right) \cdot p_{1} \cdot m_{A C}^{\prime}(t)+\left(1-p_{3}\right) \cdot p_{2} \cdot m_{B C}^{\prime}(t) \\
& +\left(1-p_{3}\right) \cdot p_{1} \cdot p_{2} \cdot m_{A B C}^{\prime}(t)
\end{aligned}
$$

with marginal conditions

$$
\begin{array}{ll}
m_{A}(0)=0, & a_{A}(0)=a_{A} \\
m_{B}(0)=0, & a_{B}(0)=a_{B} \\
m_{C}(0)=0, & a_{C}(0)=a_{C}
\end{array}
$$

The solutions to the above equations are lengthy, although they are straightforward to solve.

# 11.4.2 TVP Reliability Function 

An NVP system fails when more than half of its versions fail simultaneously at the same time. It is assumed that a voter or decision mechanism is a perfect one. As we mentioned before, we divide these failures into two categories: common failures and independent failures. The NVP system reliability can be obtained by combining these two failure modes together.

## Common Failure Mode

Let $N_{d}(t)$ be the total number of software system failures which are caused by common faults in the system. Then it is easily to see that

$$
N_{d}(t)=N_{A B}(t)+N_{A C}(t)+N_{B C}(t)+N_{A B C}(t)
$$

Therefore, the mean value function of $N_{d}(t)$ is as follows

$$
m_{d}(t)=m_{A B}(t)+m_{A C}(t)+m_{B C}(t)+m_{A B C}(t)
$$

The probability that the TVP software system will not fail during $(T, \mathrm{~T}+x)$ given that the latest failure occurred at time $T$ is

$$
\operatorname{Pr}\{\text { No common failure during } x \mid T\}=e^{-\left(m_{d}(T+x)-m_{d}(T)\right)}
$$

## Independent Failure

Commonly the TVP software system fails on common faults among versions; however, there is a small probability that two software versions fail on the same input because of independent faults.

From assumptions 12 and 13, the failure intensity $h_{\overline{A B}}(t)$ for the concurrent independent failures between version 1 and version 2 is given by

$$
h_{\overline{A B}}(t)=K_{A B} \cdot X_{A}(t) \cdot X_{B}(t)
$$

where the numbers of independent faults in version 1 and 2 are

$$
\begin{aligned}
& X_{A}(t)=a_{A}(t)-p_{1} \cdot m_{A}(t) \\
& X_{B}(t)=a_{B}(t)-p_{2} \cdot m_{B}(t)
\end{aligned}
$$Then the mean value function for concurrent independent failures $N_{\overline{A B}}(t)$ is given by

$$
m_{\overline{A B}}(t)=\int_{0}^{t} h_{\overline{A B}}(\tau) d \tau
$$

Given the release time $T$ and mission time $x$, we can obtain the probability that there is no concurrent independent failure $\overline{A B}$ during $x$

$$
\operatorname{Pr}\{\text { no } \overline{A B} \text { failure during } x \mid T\}=e^{-\left(m_{\overline{A B}}(T+x)-m_{\overline{A B}}(T)\right)}
$$

Similarly, the mean value functions for concurrent independent failures between version 1 and 3 and between version 2 and 3, respectively, are

$$
\begin{aligned}
& m_{\overline{A C}}(t)=\int_{0}^{t} h_{\overline{A C}}(\tau) d \tau \\
& m_{\overline{B C}}(t)=\int_{0}^{t} h_{\overline{B C}}(\tau) d \tau
\end{aligned}
$$

Given the release time $T$ and mission time $x$, we can obtain the probability that there is no concurrent independent failure $\overline{A C}$ and $\overline{B C}$ during $x$

$$
\begin{aligned}
& \operatorname{Pr}\{\text { no } \overline{A C} \text { failure during } x \mid T\}=e^{-\left(m_{\overline{A C}}(T+x)-m_{\overline{A C}}(T)\right)} \\
& \operatorname{Pr}\{\text { no } \overline{B C} \text { failure during } x \mid T\}=e^{-\left(m_{\overline{B C}}(T+x)-m_{\overline{B C}}(T)\right)}
\end{aligned}
$$

where

$$
\begin{aligned}
& h_{\overline{A C}}(t)=K_{A C} \cdot X_{A}(t) \cdot X_{C}(t) \\
& h_{\overline{B C}}(t)=K_{B C} \cdot X_{B}(t) \cdot X_{C}(t)
\end{aligned}
$$

If we define

$$
N_{I}(t)=N_{\overline{A B}}(t)+N_{\overline{A C}}(t)+N_{\overline{B C}}(t)
$$

with the mean value function

$$
m_{I}(t)=m_{\overline{A B}}(t)+m_{\overline{A C}}(t)+m_{\overline{B C}}(t)
$$

then the probability that there is no independent failure during mission $x$ for the NVP system is

$$
\begin{aligned}
& P\{\text { no concurrent independence failure during } x / T\} \\
& \quad=e^{-\left(m_{I}(T+x)-m_{I}(T)\right)}
\end{aligned}
$$

Because the common failures and concurrent independent failures are independent of each other, then

$$
\begin{aligned}
R_{T V P}(x \mid T)= & \operatorname{Pr}\{\text { no common failure during } x \mid T\} \times \\
& \operatorname{Pr}\{\text { no concurrent independent failure during } x \mid T\}
\end{aligned}
$$

From equations (11.19) and (11.27), the reliability of TVP system can be determined by

$$
R_{T V P}(x \mid T)=e^{-\left[m_{d}(T+x)+m_{I}(T+x)-m_{d}(T)-m_{I}(T)\right]}
$$One can estimate the parameters in the model by using the MLE method. See Teng and Pham (2002) for details.

# 11.4.3 Numerical Example 

Consider a simplify software control logic for a water reservoir control (WRC) system (Teng and Pham, 2002). Water is supplied via a source pipe controlled by a source valve and removed via a drain pipe controlled by a drain valve. There are two level sensors, positioned at the high and low limits; the high sensor does an output action above if the level is above it and the low sensor outputs below if the level is below it.

The control system should maintain the water level between these two limits, allowing for rainfall into and seepage from the reservoir. If, however, the water rises above the high level, an alarm should sound. The WRC system achieves fault tolerance and high reliability through the use of two-version programming (2VP) software control logic. The WRC software system with normalized data is listed in Table 11.3.

Table 11.3. Failure normalized-data of WRC 2VP system

| Fault <br> No. | Failure time (Version) |  | Fault <br> No. | Failure time <br> (Version) |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| K | Version <br> 1 | Version <br> 2 | K | Version <br> 1 | Version <br> 2 |
| 1 | 1.2 | 3.6 | 14 | 39.2 | 34.8 |
| 2 | 2.8 | 8.4 | 15 | 40 | 36.4 |
| 3 | 8.4 | 12.8 | 16 | 44 | 36.8 |
| 4 | 10 | 14.4 | 17 | 44.8 | 38 |
| 5 | 16.4 | 17.2 | 18 | 54 | 39.2 |
| 6 | 20 | 18 | 19 | 56 | 41.6 |
| 7 | 24.4 | 20 | 20 | 62.4 | 42 |
| 8 | 28 | 23.2 | 21 | 80 | 46.4 |
| 9 | 29.2 | 25.2 | 22 | 92 | 59.6 |
| 10 | 31.2 | 28 | 23 | 99.6 | 62.4 |
| 11 | 34 | 28.4 | 24 |  | 98.8 |
| 12 | 36 | 30.8 | 25 |  | 99.6 |
| 13 | 36.8 | 31.2 | 26 |  | 100 |

In this example, we assume that the reliability of the voter is equal to 1 and the voter can identify exactly which version(s) is failed whenever a failure occurred. Under these assumptions, the 2VP system fails only when both its components (software versions) fail at the same input data.

This example considers two cases - one is that two software versions are assumed to fail $s$-independent; the other is that both versions are not assumed to fail $s$-independently.
Case 1: Independent of TVP Software Versions. Assuming that those two software versions are $s$-independent of each other. We can apply the generalized softwarereliability model to each version separately, and estimate the reliability of each version $R_{1}(x \mid t)$ and $R_{2}(x \mid t)$, and further obtain the reliability for the entire system by using

$$
R_{\text {ind }}(x \mid t)=1-\left(1-R_{1}(x \mid t)\right) \cdot\left(1-R_{2}(x \mid t)\right)
$$

where $x$ is a mission time,

$$
R_{1}(x \mid t)=e^{-\left(m_{1}(t+x)-m_{2}(t)\right)}
$$

and

$$
R_{2}(x \mid t)=e^{-\left(m_{2}(t+x)-m_{3}(t)\right)}
$$

Figures 11.6 and 11.7 show the goodness of fit of mean value function $\mathrm{m}_{1}(t)$ (for version 1) and $\mathrm{m}_{2}(t)$ for (version 2), respectively. The reliability function $R_{\text {ind }}(x \mid t)$ is also illustrated in Figure 11.11.


Figure 11.6. Function $\mathrm{m}_{1}(t) v s$ cumulative number of failures in version 1

Case 2: Dependent of TVP Software Versions. From Table 11.4, we can observe that two versions fail simultaneously at some time, for example, at $t=8.4,20,28$, ..., 99.6. These failures are considered as coincident failures that are caused either by the common faults, or unrelated faults between two versions. Therefore, the assumption of independence is not valid for this normalized-data set.

Figure 11.7. Function $\mathrm{m}_{2}(t)$ vs vs. cumulative number of failures in version 2

In this example, we assume that all concurrent failures are common failures. Table 11.4 is generated directly from Table 11.3 and it shows the different fault types in this 2VP system. Similary from the TVP modeling formulation, we can easily obtain the mean value functions.

From Section 11.4.1, we can obtain the results as follows:
(1) Error type AB

$$
m_{A B}^{\prime}(t)=b \cdot\left(a_{A B}-p_{1} \cdot p_{2} \cdot m_{A B}(t)\right)
$$

with marginal condition $m_{A B}(0)=0$, and $a_{A B}(0)=a_{A B}$. The solution to equation (11.30) is

$$
m_{A B}(t)=\frac{a_{A B}}{p_{1} \cdot p_{2}}\left(1-e^{-b p_{1} p_{2} t}\right)
$$

(2) Fault type A

$$
\begin{gathered}
m_{A}^{\prime}(t)=b \cdot\left(a_{A}(t)-p_{1} \cdot m_{A}(t)\right) \\
a_{A}^{\prime}(t)=\left(1-p_{1}\right) \cdot p_{2} \cdot m_{A B}^{\prime}(t)+\beta_{1} \cdot\left(m_{A}^{\prime}(t)+m_{A B}^{\prime}(t)\right)
\end{gathered}
$$

with marginal condition $m_{A}(0)=0$, and $a_{A}(0)=a_{A}$. The solution to equation (11.32) is

$$
m_{A}(t)=C_{A 1}+C_{A 2} \cdot e^{-b p_{1} p_{2} t}+C_{A 3} \cdot e^{-b\left(p_{1}-\beta_{1}\right) t}
$$

where

$$
C_{A 1}=\frac{a_{A}}{p_{1}-\beta_{1}}+\frac{\left(\left(1-p_{1}\right) \cdot p_{2}+\beta_{1}\right) \cdot a_{A B}}{p_{1} \cdot p_{2} \cdot\left(p_{1}-\beta_{1}\right)}
$$$$
\begin{gathered}
C_{A 2}=-\frac{\left(\left(1-p_{1}\right) \cdot p_{2}+\beta_{1}\right) \cdot a_{A B}}{p_{1} \cdot p_{2} \cdot\left(p_{1} \cdot\left(1-p_{2}\right)-\beta_{1}\right)} \\
C_{A 3}=\frac{\left(\left(1-p_{1}\right) \cdot p_{2}+\beta_{1}\right) \cdot a_{A B}}{\left(p_{1}-\beta_{1}\right) \cdot\left(p_{1} \cdot\left(1-p_{2}\right)-\beta_{1}\right)}-\frac{a_{A}}{p_{1}-\beta_{1}}
\end{gathered}
$$

Table 11.4. Fault type table for 2VP system

| $F a$ <br> ult \# | Failure time (hour) |  |  |
| :--: | :--: | :--: | :--: |
|  | Fault A | Fault B | Fault AB |
| 1 | 1.2 | 3.6 | 8.4 |
| 2 | 2.8 | 12.8 | 20 |
| 3 | 10 | 14.4 | 28 |
| 4 | 16.4 | 17.2 | 31.2 |
| 5 | 24.4 | 18 | 36.8 |
| 6 | 29.2 | 23.2 | 39.2 |
| 7 | 34 | 25.2 | 62.4 |
| 8 | 36 | 28.4 | 99.6 |
| 9 | 40 | 30.8 |  |
| 10 | 44 | 34.8 |  |
| 11 | 44.8 | 36.4 |  |
| 12 | 54 | 38 |  |
| 13 | 56 | 41.6 |  |
| 14 | 80 | 42 |  |
| 15 | 92 | 46.4 |  |
| 16 |  | 59.6 |  |
| 17 |  | 98.8 |  |
| 18 |  | 100 |  |

(3) Fault type B

$$
\begin{gathered}
m_{B}^{\prime}(t)=b \cdot\left(a_{B}(t)-p_{2} \cdot m_{B}(t)\right) \\
a_{B}^{\prime}(t)=\left(1-p_{2}\right) \cdot p_{1} \cdot m_{A B}^{\prime}(t)+\beta_{2} \cdot\left(m_{B}^{\prime}(t)+m_{A B}^{\prime}(t)\right)
\end{gathered}
$$

with marginal condition $m_{B}(0)=0$, and $a_{B}(0)=a_{B}$. The solution to equation (11.34) is

$$
m_{B}(t)=C_{B 1}+C_{B 2} \cdot e^{-b p_{1} p_{2} t}+C_{B 3} \cdot e^{-b\left(p_{2}-\beta_{2}\right) t}
$$

where

$$
\begin{gathered}
C_{B 1}=\frac{a_{B}}{p_{2}-\beta_{2}}+\frac{a_{A B} \cdot\left(\left(1-p_{2}\right) \cdot p_{1}+\beta_{2}\right)}{p_{1} \cdot p_{2} \cdot\left(p_{2}-\beta_{2}\right)} \\
C_{B 2}=-\frac{\left(\left(1-p_{2}\right) \cdot p_{1}+\beta_{2}\right) \cdot a_{A B}}{p_{1} \cdot p_{2} \cdot\left(p_{2} \cdot\left(1-p_{1}\right)-\beta_{2}\right)} \\
C_{B 3}=\frac{\left(\left(1-p_{2}\right) \cdot p_{1}+\beta_{2}\right) \cdot a_{A B}}{\left(p_{2}-\beta_{2}\right) \cdot\left(p_{2} \cdot\left(1-p_{1}\right)-\beta_{2}\right)}-\frac{a_{B}}{p_{2}-\beta_{2}}
\end{gathered}
$$The likelihood function is given by

$$
L=L_{A} \cdot L_{B} \cdot L_{A B}
$$

where

$$
\begin{aligned}
& L_{A}=\prod_{i=1}^{n} \cdot\left\{\frac{\left[m_{A}\left(t_{i}\right)-m_{A}\left(t_{i-1}\right)\right]^{y_{A i}-y_{A(i-1)}}}{\left(y_{A i}-y_{A(i-1)}\right)!} \cdot e^{-\left[m_{A}\left(t_{i}\right)-m_{A}\left(t_{i-1}\right)\right]}\right\} \\
& L_{B}=\prod_{i=1}^{n_{A}}\left\{\frac{\left[m_{B}\left(t_{i}\right)-m_{B}\left(t_{i-1}\right)\right]^{y_{B i}-y_{B(i-1)}}}{\left(y_{B i}-y_{B(i-1)}\right)!} \cdot e^{-\left[m_{B}\left(t_{i}\right)-m_{B}\left(t_{i-1}\right)\right]}\right\} \\
& L_{A B}=\prod_{i=1}^{n_{A B}}\left\{\frac{\left[m_{A B}\left(t_{i}\right)-m_{A B}\left(t_{i-1}\right)\right]^{y_{A B i}-y_{A B(i-1)}}}{\left(y_{A B i}-y_{A B(i-1)}\right)!} \cdot e^{-\left[m_{A B}\left(t_{i}\right)-m_{A B}\left(t_{i-1}\right)\right]}\right\}
\end{aligned}
$$

Therefore, the log of likelihood function can be obtained:

$$
\begin{aligned}
\ln (L)= & \sum_{i=1}^{n_{A}}\left\{\left(y_{A i}-y_{A(i-1)}\right) \cdot \ln \left(m_{A}\left(t_{i}\right)-m_{A}\left(t_{i-1}\right)\right)\right. \\
& \left.\cdot-m_{A}\left(t_{i}\right)+m_{A}\left(t_{i-1}\right)-\ln \left(\left(y_{A i}-y_{A(i-1)}\right)!\right)\right\} \\
+ & \sum_{i=1}^{n_{B}}\left\{\left(y_{B i}-y_{B(i-1)}\right) \cdot \ln \left(m_{B}\left(t_{i}\right)-m_{B}\left(t_{i-1}\right)\right)\right. \\
+ & \left.\cdot-m_{B}\left(t_{i}\right)+m_{B}\left(t_{i-1}\right)-\ln \left(\left(y_{B i}-y_{B(i-1)}\right)!\right)\right\} \\
+ & \sum_{i=1}^{n_{A B}}\left\{\left(y_{A B i}-y_{A B(i-1)}\right) \cdot \ln \left(m_{A B}\left(t_{i}\right)-m_{A B}\left(t_{i-1}\right)\right)\right. \\
& \left.\cdot-m_{A B}\left(t_{i}\right)+m_{A B}\left(t_{i-1}\right)-\ln \left(\left(y_{A B i}-y_{A B(i-1)}\right)!\right)\right\}
\end{aligned}
$$

Taking a derivative with respect to each unknown parameters, setting it to zero, and solving the system of equations, we can finally obtain MLEs of all unknown parameters. The confidence interval for each parameter estimate can easily be obtained by constructing the Hessian matrix H. The Hessian matrix $H$ can be obtained as follows:

$$
H=\left[\begin{array}{llllll}
h_{11} & h_{12} & h_{13} & h_{14} & h_{15} & h_{16} \\
h_{21} & h_{22} & h_{23} & h_{24} & h_{25} & h_{26} \\
h_{31} & h_{32} & h_{33} & h_{34} & h_{35} & h_{36} \\
h_{41} & h_{42} & h_{43} & h_{44} & h_{45} & h_{46} \\
h_{51} & h_{52} & h_{53} & h_{54} & h_{55} & h_{56} \\
h_{61} & h_{62} & h_{63} & h_{64} & h_{65} & h_{66}
\end{array}\right]
$$

where

$$
h_{i j}=\frac{\partial^{2} L}{\partial x_{i} \partial x_{j}} \quad i, j=1, \ldots, 6
$$and the expression,

$$
\begin{array}{lll}
x_{1} \rightarrow a_{A} & x_{2} \rightarrow a_{B} & x_{3} \rightarrow a_{A B} \\
x_{4} \rightarrow \beta_{1} & x_{5} \rightarrow \beta_{2} & x_{6} \rightarrow b
\end{array}
$$

For example,

$$
\begin{aligned}
h_{11} & =\frac{\partial^{2} L}{\partial x_{1}^{2}}=\frac{\partial^{2} L}{\partial a_{A}^{2}} \\
& =\sum_{i=1}^{n} \frac{-\left(\frac{-e^{-b\left(p_{i}-\beta_{i}\right) t_{i}}+e^{-b\left(p_{i}-\beta_{i}\right) t_{i-1}}}{p_{1}-\beta_{1}}\right)^{2}}{\left(C_{A 2}\left(e^{-b p_{1} p_{1} t_{i}}-e^{-b p_{1} p_{1} t_{i-1}}\right)+C_{A 3}\left(e^{-b\left(p_{1}-\beta_{1}\right) t_{i}}-e^{-b\left(p_{1}-\beta_{1}\right) t_{i-1}}\right)\right)^{2}}
\end{aligned}
$$

where $C_{A 2}$ and $C_{A 3}$ are given in equation (11.33). The variance matrix, $V$, can be obtained as follows:

$$
V=[-H]^{-1}=\left[\begin{array}{cccccc}
v_{11} & v_{12} & v_{13} & v_{14} & v_{15} & v_{16} \\
v_{21} & v_{22} & v_{23} & v_{24} & v_{25} & v_{26} \\
v_{31} & v_{32} & v_{33} & v_{34} & v_{35} & v_{36} \\
v_{41} & v_{42} & v_{43} & v_{44} & v_{45} & v_{46} \\
v_{51} & v_{52} & v_{53} & v_{54} & v_{55} & v_{56} \\
v_{61} & v_{62} & v_{63} & v_{64} & v_{65} & v_{66}
\end{array}\right]
$$

where $v_{i j}$ is the covariance of $x_{i}$ and $x_{j}$ and

$$
\begin{aligned}
& v_{11}=\operatorname{Var}\left(x_{1}\right)=\operatorname{Var}\left(a_{A}\right) \\
& v_{22}=\operatorname{Var}\left(x_{2}\right)=\operatorname{Var}\left(a_{B}\right) \\
& v_{33}=\operatorname{Var}\left(x_{3}\right)=\operatorname{Var}\left(a_{A B}\right) \\
& v_{44}=\operatorname{Var}\left(x_{4}\right)=\operatorname{Var}\left(\beta_{1}\right) \\
& v_{55}=\operatorname{Var}\left(x_{5}\right)=\operatorname{Var}\left(\beta_{2}\right) \\
& v_{66}=\operatorname{Var}\left(x_{6}\right)=\operatorname{Var}(b)
\end{aligned}
$$

Since all coincident failures are common failures then $K_{\mathrm{AB}}=0$. Assume $p_{1}=p_{2}=0.9$, then the corresponding MLEs are given by

$$
\begin{array}{lll}
\hat{a}_{A}=15.47 & \hat{a}_{B}=18.15 & \hat{a}_{A B}=7.8 \\
\hat{\beta}_{1}=0 & \hat{\beta}_{2}=0.002324 & \hat{b}=0.009
\end{array}
$$The corresponding Hessian matrix and variance matrices are

$$
\begin{aligned}
& H=\left[\begin{array}{cccccc}
-0.0763 & 0 & -0.0042 & -1.028 & 0 & -39.48 \\
0 & 0.051 & -0.0037 & 0 & -1.043 & -36.55 \\
-0.0042 & -0.0037 & -0.132 & -0.0825 & -0.133 & -40.11 \\
-1.028 & 0 & -0.0825 & -31.68 & 0 & 37.38 \\
0 & -1.043 & -0.133 & 0 & -33.26 & 68.38 \\
-39.48 & -36.55 & -40.11 & 37.38 & 68.38 & -179746.12
\end{array}\right] \\
& V=[-H]^{-1}=\left[\begin{array}{cccccc}
41.473 & 40.4 & 5.625 & -1.384 & -1.33 & -0.0194 \\
40.4 & 143.61 & 13.28 & -1.397 & -4.645 & -0.0431 \\
5.625 & 13.28 & 9.511 & -0.215 & -0.467 & -0.0063 \\
-1.384 & -1.397 & -0.215 & 0.0778 & 0.046 & 0.00067 \\
-1.33 & -4.645 & -0.467 & 0.046 & 0.181 & 0.00142 \\
-0.0194 & -0.0431 & -0.0063 & 0.00067 & 0.00142 & 2.067 e-05
\end{array}\right]
\end{aligned}
$$

Then the variance of estimations are

$$
\begin{array}{ll}
\operatorname{Var}\left(\hat{a}_{A}\right)=41.473 & \operatorname{Var}\left(\hat{a}_{B}\right)=143.61 & \operatorname{Var}\left(\hat{a}_{A B}\right)=9.511 \\
\operatorname{Var}\left(\hat{\beta}_{1}\right)=0.0778 & \operatorname{Var}\left(\hat{\beta}_{2}\right)=0.181 & \operatorname{Var}(b)=2.067 \times 10^{-5}
\end{array}
$$

The NVP-SRGM software system reliability is given by

$$
R_{N V P-S R G M}(x \mid t)=e^{-\left(m_{S B}(t+x)-m_{S B}(t)\right)}
$$

Figures 11.8-11.9 show the mean value functions and their $95 \%$ confidence intervals as well as the number of cumulative failures. Figure 11.10 shows the 2VP system reliability and its $95 \%$ confidence interval for a mission time $x=10$ hours. The reliability $R_{N V P-S R G M}(x \mid t), R_{\text {ind }}(x \mid t)$ and component reliability $R_{1}(x \mid t)$ and $R_{2}(x \mid t)$ for the 2VP system are shown in Figure 11.11 with mission time $x=10$. Figure 11.11 shows that the 2VP scheme has a higher reliability than any single component, which means that the 2 VP scheme is able to provide higher system reliability. It seems that more application is needed to validate fully the NVPSRGM for quantify model discuss in the section (Teng 2002) in a general industrial setting.

Figure 11.8. $\mathrm{m}_{\mathrm{A}}(t) v s$ the number of cumulative type $A$ failures


Figure 11.9. $\mathrm{m}_{\mathrm{B}}(t) v s$ the number of cumulative type $B$ failures

Figure 11.10. 2VP system reliability and its $95 \%$ confidence interval


Figure 11.11. 2VP reliability comparisons (mission time $x=10$ )# 11.5 Complex-system Reliability Modeling 

This section discusses a reliability model considering system failures due to hardware failures, software failures or hardware-software interaction failures based on the work by Teng et al. (2001). A system reliability model is discussed based on Markov processes. Hardware-software interaction failures can be specified into two categories: transient and permanent hardware-related software failures.

### 11.5.1 System Considerations

Figure 11.12 shows the system failure categories. The overlap region between hardware failures and software failures represents hardware-software interaction (HW/SW) failures. Because of the associations with system hardware components, all HW/SW failures can be further divided into two categories: Transient and permanent hardware/software interaction failures. Figure 11.13 shows a presentation of the system reliability diagram.

Figure 11.13 divides hardware and software failures into four parts. They are H-2/S-2, which represents permanent HW/SW failures, and H-3/S-3, which represents temporary (transient) HW/SW failures.


Figure 11.12. System failure categories

Following are the explanations of all modules in Figure 11.13.

## Hardware Failures:

H - 1: Total hardware component failures - whenever there is an H-1 event, the whole system will fail. These kinds of failures are "pure hardware failures".H-2: Also known as hardware degradation. Only partial hardware fails (permanently), and the whole system does not fail necessarily but let the system work in the degraded state. It is related to S - 2, and possibly causes the software to fail in the state of "Hardware-related Software Failure".
H-3: Temporary (Transient) hardware component failures - these hardware failures are usually caused by the disturbances from the operation environment.


Figure 11.13. System reliability diagram

# Software Failures 

S-1: Pure software failures, they are caused by the faults in the software, which is not related to hardware system failures.
S-2: Permanent hardware-related software failures. When the hardware degrades (H-2), the system is liable to fail in S-2. These failures cannot be solved by simply redoing the computing tasks, and usually are related to hardware degradations. These failures are the major unknown failures in this paper. One can consider that the hardware-related software failures are caused by design faults that cannot deal with the potential partial hardware failures.
S-3: Transient hardware-related software failures. Although these failures are actually related to transient hardware failures, they can be avoided if the designer anticipates the hardware transients and designs fault-tolerance (such as Roll back scheme) into the software. Thus, hardware transients can be transferred into temporary hardware-related software failures.# 11.5.2 Reliability Modeling 

## Assumptions (Teng et al. 2001)

1. An entire system fails whenever a total hardware failure (pure hardware failure), or a pure software failure or a hardware-related software failure (HW/SW interaction failure) happens.
2. Pure hardware failures and pure software failures are independent of each other.
3. Pure hardware failures and HW/SW interaction failures are independent of each other.
4. Pure software failures and hardware-related software failures (HW/SW) are independent of each other.
5. Hardware-related software failures (HW/SW) can be put into two categories: permanent HW/SW and transient HW/SW. They are also independent of each other.
6. Hardware components go to degradation (partial failure) with failure rate $\lambda_{1}$.
7. The partial hardware failure can be immediately detected with a probability $p_{1}$. Once a partial hardware failure is detected, it can be recovered using a software tool with a probability $p_{2}$.
8. An undetected degradation may cause a hardware-related software failure (fail unsafe) with rate $\lambda_{3}$, and a detected degradation may cause an execution abortion (fail safe) with rate $\lambda_{4}$.
9. Once a partial hardware failure is detected, the failed hardware components can be fixed or replaced at rate $\mu_{1}$ (if recovered by software) and $\mu_{2}$ (if not recovered by software).
10. Partial hardware failure can go further to the total failure state with either $\lambda_{21}$, $\lambda_{22}$ or $\lambda_{23}$ (see Figure 11.14).
11. The transient hardware failure rate is $\lambda_{5}$.
12. Transient hardware failures are detected immediately with probability $p_{3}$. If detected, the transient failures are treated immediately by software methods, which recover the transient failures with probability $p_{4}$. If a transient failure is not successfully recovered, then the consequent new transient failure can still be detected since they are caused by the same kind of hardware transient problems.
13. If a transient hardware failure is not detected, the software will fail to give the correct result, and then the system will fail.
14. The maximum number of times that the software tries to recover a transient hardware failure is $H$. If $H$ is exceeded, the system is considered failed.

The reliability of the entire system is

$$
R_{\text {System }}(t)=R_{s}(t) R_{h}(t) R_{h s}(t)
$$

where
$\mathrm{R}_{\mathrm{s}}(\mathrm{t})=$ reliability of software subsystem
$\mathrm{R}_{\mathrm{h}}(\mathrm{t})=$ reliability of hardware subsystem
$\mathrm{R}_{\mathrm{hs}}(\mathrm{t})=$ reliability of hardware-software interaction# A. Hardware Subsystem 

If we assume that the hardware system has the following Weibull hazard function:

$$
h_{h}(t)=\frac{\gamma}{\theta} t^{\gamma-1}
$$

then the hardware reliability function of the Weibull distribution $R_{h}(t)$ is

$$
R_{h}(t)=e^{-\frac{t^{\gamma}}{\theta}}
$$

## B. Software Subsystem

From equation (9) in (Zhang et al. 2003) and if we assume that the error detection rate function $b(t)$ is a non-decreasing function with inflexion S -shaped curve as follows

$$
b(t)=\frac{c}{1+\alpha e^{-b t}}
$$

and the errors can be introduced during debugging, $\beta$ being a constant error introduction rate, as
$\beta(t)=\beta$
then the mean value function and reliability of software subsystem are as follows:

$$
m_{s}(t)=\frac{a}{p-\beta}\left(1-\left(\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{\frac{\gamma}{\theta}(p-\beta)}\right)
$$

and

$$
R_{s}(t)=e^{-m_{s}(t)}
$$

respectively.

## C. Hardware-Software Interaction Modeling

## Notation

$\lambda_{1} \quad$ Hazard rate for hardware subsystem to go to the degradation state.
$\mu \quad$ Repair rate after degradation is detected.
$\mu_{1}=$ repair rate at state $9 a$
$\mu_{2}=$ repair rate at state $9 b$
$\lambda_{2} \quad$ Hazard rate for degraded hardware subsystem to go to the total failure
$\lambda_{21}=$ hazard rate at state $9 a$
$\lambda_{22}=$ hazard rate at state $9 b$
$\lambda_{23}=$ hazard rate at state 10
$\lambda_{3} \quad$ Hazard rate from undetected hardware degradation to hardware-related software failure (fail unsafe)
$\lambda_{4} \quad$ Hazard rate from detected hardware degradation to abortion (fail safe)
$\lambda_{5} \quad$ Hazard rate for hardware transient failures| $\lambda_{6}$ | Hazard rate from hardware transient to aborting operation |
| :-- | :-- |
| $p_{1}$ | Probability that the hardware degradation is detected |
| $q_{1}$ | Probability that the hardware degradation is undetected, $q_{1}=1-p_{1}$ |
| $p_{2}$ | Probability that the degradation is recovered by software methods |
| $q_{2}$ | Probability that the degradation is not recovered by software, $q_{2}=1-p_{2}$ |
| $p_{3}$ | Probability that the transient is detected by some methods |
| $q_{3}$ | Probability that the transient is not detected by software, $q_{3}=1-p_{3}$ |
| $H$ | Maximal number of times that redo a task to fix a transient hardware |
|  | failure. |

Permanent Hardware/Software Interactions Case. If a hardware component goes to totally fail directly, then it is considered in the hardware reliability model; if a hardware component goes to partially fail first, then it is considered in this model.

# Notation 

$Q_{0}(t) \quad$ Probability to stay in state 0 (system operation)
$Q_{2}(t) \quad$ Probability to stay in state 2 (total hardware failure)
$Q_{9 a}(t) \quad$ Probability to stay in state 9a (hardware degradation-detected and software recovered)
$Q_{9 b}(t)$ Probability to stay in state 9 b (hardware degradation-detected and not software recovered)
$Q_{10}(t) \quad$ Probability to stay in state 10 (hardware degradation not detected)
$Q_{11}(t) \quad$ Probability to stay in state 11 (execution aborted)
$Q_{12}(t)$ Probability to stay in state 12 (permanent hardware-related software failure)

Figure 11.14 shows the system state transition diagram of the permanent HW/SW interactions based on assumptions 6-10. From the figure, we can easily obtain the following differential equations (Teng et al. 2001):

$$
\begin{aligned}
& Q_{0}^{\prime}(t)=-\lambda_{1} Q_{0}(t)+\mu_{1} Q_{9 a}(t)+\mu_{2} Q_{9 b}(t) \\
& Q_{2}^{\prime}(t)=\lambda_{22} Q_{9 a}(t)+\lambda_{21} Q_{9 b}(t)+\lambda_{23} Q_{10}(t) \\
& Q_{9 a}^{\prime}(t)=\lambda_{1} p_{1} p_{2} Q_{0}(t)-\left(\mu_{1}+\lambda_{22}\right) Q_{9 a}(t) \\
& Q_{9 b}^{\prime}(t)=\lambda_{1} p_{1} q_{2} Q_{0}(t)-\left(\mu_{2}+\lambda_{21}+\lambda_{4}\right) Q_{9 b}(t) \\
& Q_{10}^{\prime}(t)=\lambda_{1} q_{1} Q_{0}(t)-\left(\lambda_{23}+\lambda_{3}\right) Q_{10}(t) \\
& \mathrm{Q}_{11}^{\prime}(\mathrm{t})=\lambda_{4} \mathrm{Q}_{9 \mathrm{~b}}(\mathrm{t}) \\
& Q_{12}^{\prime}(t)=\lambda_{3} Q_{10}(t)
\end{aligned}
$$

Given the initial conditions

$$
\begin{array}{lll}
Q_{0}(0)=1 & Q_{2}(0)=0 & Q_{9 a}(0)=0 & Q_{9 b}(0)=0 \\
Q_{10}(0)=0 & Q_{11}(0)=0 & Q_{12}(0)=0 &
\end{array}
$$Work States for Permanent HW/SW Interactions


Figure 11.14. State Transition Diagram Permanent Hardware/Software Interactions
It should be noted that among all these system states, state 2,11 and 12 are failure states, while state $9 \mathrm{a}, 9 \mathrm{~b}$ and 10 are degraded working states, and state 0 is the normal working state. Using the Laplace transform, we can easily obtain the solutions as follows:

$$
\begin{aligned}
& Q_{0}(t)=\frac{\left(c_{1}+b_{1}\right)\left(c_{1}+b_{2}\right)}{\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)} e^{c_{1} t}+\frac{\left(c_{2}+b_{1}\right)\left(c_{2}+b_{2}\right)}{\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)} e^{c_{2} t}+\frac{\left(c_{3}+b_{1}\right)\left(c_{3}+b_{2}\right)}{\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)} e^{c_{3} t} \\
& Q_{9 \mathrm{a}}(t)=\lambda_{1} p_{1} p_{2}\left[\frac{\left(c_{1}+b_{2}\right) e^{c_{1} t}}{\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)}+\frac{\left(c_{2}+b_{2}\right) e^{c_{2} t}}{\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)}+\frac{\left(c_{3}+b_{2}\right) e^{c_{3} t}}{\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)}\right] \\
& Q_{9 \mathrm{~b}}(t)=\lambda_{1} p_{1} q_{2}\left[\frac{\left(c_{1}+b_{1}\right) e^{c_{1} t}}{\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)}+\frac{\left(c_{2}+b_{1}\right) e^{c_{2} t}}{\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)}+\frac{\left(c_{3}+b_{1}\right) e^{c_{3} t}}{\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)}\right]
\end{aligned}
$$$$
\begin{aligned}
& Q_{10}(t)=\lambda_{1} q_{1}\left(\begin{array}{l}
\frac{\left(c_{1}+b_{1}\right)\left(c_{1}+b_{2}\right) e^{c_{1} t}}{\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)\left(c_{1}-c_{4}\right)}+\frac{\left(c_{2}+b_{1}\right)\left(c_{2} b_{2}\right) e^{c_{2} t}}{\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)\left(c_{2}-c_{4}\right)} \\
+\frac{\left(c_{3}+b_{1}\right)\left(c_{3}+b_{2}\right) e^{c_{3} t}}{\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)\left(c_{3}-c_{4}\right)}+\frac{\left(c_{4}+b_{1}\right)\left(c_{4}+b_{3}\right) e^{c_{4} t}}{\left(c_{4}-c_{1}\right)\left(c_{4}-c_{2}\right)\left(c_{4}-c_{3}\right)}
\end{array}\right) \\
& Q_{11}(t)=\lambda_{1} \lambda_{4} p_{1} q_{2}\left(\begin{array}{l}
\frac{-b_{1}}{c_{1} c_{2} c_{3}}+\frac{\left(c_{1}+b_{1}\right) e^{c_{1} t}}{c_{1}\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)}+\frac{\left(c_{2}+b_{1}\right) e^{c_{2} t}}{c_{2}\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)} \\
+\frac{\left(c_{3}+b_{1}\right) e^{c_{3} t}}{c_{3}\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)}
\end{array}\right) \\
& Q_{12}(t)=\lambda_{1} \lambda_{3} q_{1}\left(\begin{array}{l}
\frac{b_{1} b_{2}}{c_{1} c_{2} c_{3} c_{4}}+\frac{\left(c_{1}+b_{1}\right)\left(c_{1}+b_{2}\right) e^{c_{1} t}}{c_{1}\left(c_{1}-c_{2}\right)\left(c_{1}-c_{3}\right)\left(c_{1}-c_{4}\right)}+\frac{\left(c_{2}+b_{1}\right)\left(c_{2}+b_{2}\right) e^{c_{2} t}}{c_{2}\left(c_{2}-c_{1}\right)\left(c_{2}-c_{3}\right)\left(c_{2}-c_{4}\right)} \\
+\frac{\left(c_{3}+b_{1}\right)\left(c_{3}+b_{2}\right) e^{-c_{3} t}}{c_{3}\left(c_{3}-c_{1}\right)\left(c_{3}-c_{2}\right)\left(c_{3}-c_{4}\right)}+\frac{\left(c_{4}+b_{1}\right)\left(c_{4}+b_{2}\right) e^{-c_{4} t}}{c_{4}\left(c_{4}-c_{1}\right)\left(c_{4}-c_{2}\right)\left(c_{4}-c_{3}\right)}
\end{array}\right) \\
& Q_{2}(t)=1-Q_{0}(t)-Q_{\theta a}(t)-Q_{\theta b}(t)-Q_{10}(t)-Q_{11}(t)-Q_{12}(t)
\end{aligned}
$$

where

$$
\begin{aligned}
& b_{1}=\mu_{1}+\lambda_{22} \\
& b_{2}=\mu_{2}+\lambda_{21}+\lambda_{4} \\
& c_{4}=-\left(\lambda_{23}+\lambda_{3}\right) \text { and } \\
& c_{1}, c_{2} \text { and } c_{3} \text { are the roots of the following equation } \\
& \left(x+\lambda_{1}\right)\left(x+b_{1}\right)\left(x+b_{2}\right)=\lambda_{1} p_{1}\left[\mu_{1} p_{2}\left(x+b_{2}\right)+\mu_{2} q_{2}\left(x+b_{1}\right)\right]
\end{aligned}
$$

The probability that the system will not fail in permanent mode due to hardware/software interactions is given by

$$
\begin{aligned}
P_{P H S}(\mathrm{t}) & =\operatorname{Pr}\{\text { No permanent HW/SW failures up to } t\} \\
& =Q_{0}(t)+Q_{\theta a}(t)+Q_{\theta b}(t)+Q_{10}(t)
\end{aligned}
$$

Furthermore, the probability that the system fails safely by permanent HW/SW interactions is

$$
P_{\text {safe }}(t)=Q_{11}(t)
$$

The probability that the system fails unsafely by permanent HW/SW interactions is

$$
P_{\text {unsafe }}(t)=Q_{2}(t)+Q_{12}(t)
$$

Transient Hardware/Software Interactions Case. Figure 11.15 shows the diagram of the transient HW/SW in systems based on the assumptions 11-14. At state 3a, the transient can be recovered by software methods with probability $p_{4}$, and if the transient can not be recovered, then it goes back to state 3a itself with probability $q_{4}=\left(1-p_{4}\right)$. If the number of failed recovery attempts gets to H , then the recoverysoftware will abort the task, therefore the state goes from $3 a$ to 4 . In Figure 11.15, states $3 b$ and 4 are the failure states, and state $0^{\prime}$ is a working state, and state $3 a$ is a transient state. Assume that failed and aborted states are independent of each other, then from Teng (2001)

$$
\begin{gathered}
Q_{0^{\prime}}^{\prime}(t)=-\lambda_{5} Q_{0^{\prime}}(t)+\lambda_{6}\left(1-q_{4}^{H}\right) Q_{3 a}(t) \\
Q_{3 a}^{\prime}(t)=\lambda_{5} p_{3} Q_{0^{\prime}}(t)-\lambda_{6} Q_{3 a}(t) \\
Q_{3 b}^{\prime}(t)=\lambda_{5} q_{3} Q_{0^{\prime}}(t) \\
Q_{4}^{\prime}(t)=\lambda_{6} q_{4}^{H} Q_{0^{\prime}}(t)
\end{gathered}
$$

The solution of the system of equations in equation (11.44) can be easily obtained. Therefore, the probability that the system will not fail due to transient $\mathrm{HW} / \mathrm{SW}$ failures is given by

$$
\begin{aligned}
P_{T H S}(\mathrm{t}) & =\operatorname{Pr}\{\text { No transient HW/SW Failures }\} \\
& =Q_{0^{\prime}}(\mathrm{t})+Q_{3 \mathrm{a}}(\mathrm{t})
\end{aligned}
$$

From equations (11.43) and (11.45), the reliability function for hardware and software interaction is as follows:

$$
\begin{aligned}
P_{h s}(t) & =\operatorname{Pr}\{\text { No HW/SW failures }\} \\
& =\operatorname{Pr}\{\text { No permanent failures }\} \times \operatorname{Pr}\{\text { No transient failures }\} \\
& =P_{P H S}(t) P_{T H S}(t)
\end{aligned}
$$

That is,

$$
P_{h s}(t)=\left[Q_{0}(t)+Q_{q_{a}}(t)+Q_{q b}(t)+Q_{10}(t)\right]\left(Q_{0^{\prime}}(t)+Q_{3 a}(t)\right)
$$



Figure 11.15. Transient failures transition diagramTherefore, the system reliability considering hardware, software and the interactions between them is as follows

$$
\begin{aligned}
& R_{\text {System }}(t)=R_{h}(t) R_{s}(t) P_{h s}(t) \\
& \quad=e^{-\frac{t^{2}}{2}} e^{-m(t)}\left[Q_{0}(t)+Q_{h s}(t)+Q_{h h}(t)+Q_{I 0}(t)\right]\left(\mathrm{Q}_{0}(\mathrm{t})+\mathrm{Q}_{3}(\mathrm{t})\right)
\end{aligned}
$$

# 11.6 Application Example 

This section illustrates the hardware and software modeling approach by applying it to a telecommunication application data. Table 11.5 shows exposure time and failure data collected from the field for a particular product that supports voice and data communication. Detail information can be obtained in Teng et al. (2001).

The hardware failures shown in Table 11.5 represent the frequency of server failures, irrespective of which particular component of the server failed. Table 11.5 does not explicitly show the HW/SW failures, but the assumption in Teng et al. (2001) that $15 \%$ of the reported HW failures were actually HW/SW failures. Table 11.6 represents a revised Table 11.5 with consideration of $15 \%$ of HW/SW failures.

Table 11.5. Failures in a telecommunication application

| Month | Software <br> exposure time <br> (system days) | Software <br> failures | Hardware exposure <br> time (system days) | Hardware <br> failures |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 961 | 4 | 9,843 | 23 |
| 2 | 4,170 | 1 | 10,290 | 32 |
| 3 | 8,789 | 5 | 11,254 | 32 |
| 4 | 11,858 | 4 | 12,385 | 21 |
| 5 | 13,110 | 3 | 13,155 | 44 |
| 6 | 14,198 | 1 | 14,198 | 55 |
| Total | 53,086 | 18 | 71,125 | 207 |

Table 11.6. HW/SW interaction failures data set

| Month | Software <br> exposure <br> time (system <br> days) | Software <br> failures | Hardware <br> exposure time <br> (system days) | Hardware <br> failures | HW/SW <br> failures |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 961 | 4 | 9,843 | 20 | 3 |
| 2 | 4,170 | 1 | 10,290 | 27 | 5 |
| 3 | 8,789 | 5 | 11,254 | 27 | 5 |
| 4 | 11,858 | 4 | 12,385 | 18 | 3 |
| 5 | 13,110 | 3 | 13,155 | 37 | 7 |
| 6 | 14,198 | 1 | 14,198 | 47 | 8 |
| Total | 53,086 | 18 | 71,125 | 176 | 31 |# Pure Software Failures 

Note that from equation (11.39), the mean value function is given by

$$
m(t)=\frac{a}{p-\beta}\left(1-\left(\frac{(1+\alpha) e^{-b t}}{1+\alpha e^{-b t}}\right)^{e_{(\beta-\beta)}} \right)
$$

where
$a$ is the expected number of initial faults in the software
$c$ is the average per fault failure rate
$\beta$ is the probability of faults being introduced during the debugging processes
$p$ is the probability of faults being successfully removed
$\alpha$ is a shape parameter that represents the learning curve in the debugging process
$b$ is the rate parameter for the learning curve.
Assuming the value $p=0.95$, the MLEs for all unknown parameters are $\hat{a}=$ $17.97, \hat{b}=0.000001, \hat{c}=0.000001, \hat{\alpha}=0, \hat{\beta}=0$. Since $\alpha$ and $\beta$ are zero, the resulting model becomes the Goel-Okumoto model with imperfect debugging. It seems that the Goel-Okumoto model fits the given data set well.

## Pure Hardware Failures

Assuming that $85 \%$ of the hardware failures reported in a given month are pure hardware. We use the Weibull model (Equation 11.38) for pure hardware failures. The data shown in Table 11.5 represents the data collected on release number two of the product. The MLE for $\theta$ and $\gamma$ in equation (11.38) are as follows:

$$
\hat{\gamma}=1.14 \quad \hat{\theta}=1949
$$

where the hardware reliability function is

$$
R_{h}(t)=e^{-\frac{t^{1.14}}{1949}}
$$

## HW/SW Interactions

To simplify the computation, Teng et al (2001) considers only permanent HW/SW failures and also assume that $p_{1}=0, \lambda_{23}=0, \lambda_{1}=0.1 \lambda_{3}$ and $\lambda_{3}=0.0048$ failures/ day. The probability that the system will not fail due to hardware and software interactions at time x is as follows:

$$
P_{h s}(x)=\frac{\lambda_{3} e^{-\lambda_{1} x}-\lambda_{1} e^{-\lambda_{3} x}}{\lambda_{3}-\lambda_{1}}
$$

Entire System ReliabilityFunction
Considering a new installation that will be delivered at time $t=53,086$ days, the entire system reliability, combining the HW, SW and HW/SW models together, between $t=53,086$ and $t=53,086+x$ (where $x$ is the mission time) is given by (Teng at el. 2001)$$
\begin{gathered}
R_{\text {system }}(x \mid t=53,086)=R_{b}(x) \cdot R_{c}(x \mid t=53,086) \cdot R_{h s}(x) \\
=e^{-\frac{x^{2}}{2}} \cdot e^{-\left[(m(53,086+x)-m(53,086)\right]} \cdot \frac{\lambda_{3} e^{-\lambda_{1} x}-\lambda_{1} e^{-\lambda_{3} x}}{\lambda_{3}-\lambda_{1}}
\end{gathered}
$$

The estimated conditional reliability function $R_{\text {system }}(x)$, and each of its three components are plotted in Figure 11.16. Figure 11.17 shows the comparison between two reliability function curves $R_{\text {ind }}(t)$ and $R_{\text {system }}(t)$, where $R_{\text {ind }}(t)$ is the reliability model which does not include effects of hardware/software interactions:

$$
R_{\text {ind }}(t)=R_{b}(t) R_{s}(t)=R_{\text {system }}(t) / R_{h s}(t)
$$



Figure 11.16. System reliability function

# 11.7 Further Reading 

Some interesting research papers and book on fault tolerant software systems are:
Y. Jiang, J. Li and Shoichi Nishimura, "A general stochastic model for dynamic locking in database systems," IEEE Trans on Computers, vol 53, no 3, 2004
T. Clouqueur, K.K. Saluja, and P. Ramanathan, "Fault tolerance in collaborative sensor networks for target detection," IEEE Trans on Computers, vol 53, no 3, 2004

Figure 11.17. System reliability comparisons

# 11.8 Problems 

1. The cost of the fault-tolerant software for a new product (XZY) includes development and design, testing, implementation, and operation costs. In general, the reliability of the system can be increased by adding more redundant programs or modules. However, the extra cost and complexity may not justify the small gains in reliability. Let us consider the following problem.

Suppose $P_{h}(s)$ is the probability of failure for the hybrid scheme based on configurations, then $\left[1-P_{h}(s)\right]$ is the reliability of the fault-tolerant software. Let
$C=$ the total amount of resources available
$C_{e i}=$ the amount of resources needed for program version $i$
$C_{v j}=$ the resources needed for voting version $j$
$C_{t k}=$ the amount of resources needed for testing version $k$.
(a) Show that the reliability optimization model, given all the information above, can be formulated as follows:

$$
\begin{aligned}
& \text { Objective } \operatorname{Max}_{s \in S}\left[1-P_{h}(s)\right] \\
& \text { Subject to } \frac{\sum_{i} C_{e i}+\sum_{j} C_{v j}+\sum_{k} C_{t k} \leq C}{C_{e i} \geq 0, C_{v j} \geq 0, C_{t k} \geq 0}
\end{aligned}
$$

where $S$ is a set of all the possible configurations of the hybrid scheme.(b) Develop a heuristic algorithm to determine the optimal solution of the above optimization problem.
2. Continuing with Problem 1, assume that all programs and their testing versions have the same reliability and costs. Given that

Cost of a program version $C_{e}=\$ 15,000$
Cost of test $C_{t}=85 \%$ of $C_{e}=\$ 12,750$
Cost of voter $C_{v}=10 \%$ of $C_{e}=\$ 1,500$
Total amount or resources available $C=\$ 120,000$
Probability of program version failure $e=0.05$
Probability of test failure $t=0.02$
Probability of voter failure $d=0.002$,
calculate the system reliability and cost of each of the following possible configurations:
(a) 7 RB
(b) 7 NVP
(c) 3 RB 2 NVP
(d) 2 NVP 3 RB
(e) 2 RB 3 NVP# Appendix 1 

## Distribution Tables

Table A1.1. Cumulative areas under the standard normal distribution

| Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| -3.0 | .0013 | .0010 | .0007 | .0005 | .0003 | .0002 | .0002 | .0001 | .0001 |
| -2.9 | .0019 | .0018 | .0017 | .0017 | .0016 | .0016 | .0015 | .0015 | .0014 |
| -2.8 | .0026 | .0025 | .0024 | .0023 | .0023 | .0022 | .0021 | .0021 | .0020 |
| -2.7 | .0035 | .0034 | .0033 | .0032 | .0031 | .0030 | .0029 | .0028 | .0027 |
| -2.6 | .0047 | .0045 | .0044 | .0043 | .0041 | .0040 | .0039 | .0038 | .0037 |
| -2.5 | .0062 | .0060 | .0059 | .0057 | .0055 | .0054 | .0052 | .0051 | .0049 |
| -2.4 | .0082 | .0080 | .0078 | .0075 | .0073 | .0071 | .0069 | .0068 | .0066 |
| -2.3 | .0107 | .0104 | .0102 | .0099 | .0096 | .0094 | .0091 | .0089 | .0087 |
| -2.2 | .0139 | .0136 | .0132 | .0129 | .0126 | .0122 | .0119 | .0116 | .0113 |
| -2.1 | .0179 | .0174 | .0170 | .0166 | .0162 | .0158 | .0154 | .0150 | .0146 |
| -2.0 | .0228 | .0222 | .0217 | .0212 | .0207 | .0202 | .0197 | .0192 | .0188 |
| -1.9 | .0287 | .0281 | .0274 | .0268 | .0262 | .0256 | .0250 | .0244 | .0238 |
| -1.8 | .0359 | .0352 | .0344 | .0336 | .0329 | .0322 | .0314 | .0307 | .0300 |
| -1.7 | .0446 | .0436 | .0427 | .0418 | .0409 | .0401 | .0392 | .0384 | .0375 |
| -1.6 | .0548 | .0537 | .0526 | .0516 | .0505 | .0495 | .0485 | .0475 | .0465 |
| -1.5 | .0668 | .0655 | .0643 | .0630 | .0618 | .0606 | .0594 | .0582 | .0570 |
| -1.4 | .0808 | .0793 | .0778 | .0764 | .0749 | .0735 | .0722 | .0708 | .0694 |
| -1.3 | .0968 | .0951 | .0934 | .0918 | .0901 | .0885 | .0869 | .0853 | .0838 |
| -1.2 | .1151 | .1131 | .1112 | .1093 | .1075 | .1056 | .1038 | .1020 | .1003 |
| -1.1 | .1357 | .1335 | .1314 | .1292 | .1271 | .1251 | .1230 | .1210 | .1190 |
| -1.0 | .1587 | .1562 | .1539 | .1515 | .1492 | .1469 | .1446 | .1423 | .1401 |
| -0.9 | .1841 | .1814 | .1788 | .1762 | .1736 | .1711 | .1685 | .1660 | .1635 |
| -0.8 | .2119 | .2090 | .2061 | .2033 | .2005 | .1977 | .1949 | .1922 | .1894 |
| -0.7 | .2420 | .2389 | .2358 | .2327 | .2297 | .2266 | .2236 | .2206 | .2177 |
| -0.6 | .2743 | .2709 | .2676 | .2643 | .2611 | .2578 | .2546 | .2514 | .2483 |
| -0.5 | .3085 | .3050 | .3015 | .2981 | .2946 | .2912 | .2877 | .2843 | .2810 |
| -0.4 | .3446 | .3409 | .3372 | .3336 | .3300 | .3264 | .3228 | .3192 | .3156 |
| -0.3 | .3821 | .3783 | .3745 | .3707 | .3669 | .3632 | .3594 | .3557 | .3520 |Table A1.1. (continued)

| Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| -0.2 | .4207 | .4168 | .4129 | .4090 | .4052 | .4013 | .3974 | .3936 | .3897 |
| -0.1 | .4602 | .4562 | .4522 | .4483 | .4443 | .4404 | .4364 | .4325 | .4286 |
| -0.0 | .5000 | .4960 | .4920 | .4880 | .4840 | .4801 | .4761 | .4721 | .4681 |
| 0.0 | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 |
| 0.1 | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 |
| 0.2 | .5793 | .5832 | .5871 | .5910 | .5948 | .5987 | .6026 | .6064 | .6103 |
| 0.3 | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 |
| 0.4 | .6554 | .6591 | .6628 | .6664 | .6700 | .6736 | .6772 | .6808 | .6844 |
| 0.5 | .6915 | .6950 | .6985 | .7019 | .7054 | .7088 | .7123 | .7157 | .7190 |
| 0.6 | .7257 | .7291 | .7324 | .7357 | .7389 | .7422 | .7454 | .7486 | .7517 |
| 0.7 | .7580 | .7611 | .7642 | .7673 | .7703 | .7734 | .7764 | .7794 | .7823 |
| 0.8 | .7881 | .7910 | .7939 | .7967 | .7995 | .8023 | .8051 | .8078 | .8106 |
| 0.9 | .8159 | .8186 | .8212 | .8238 | .8264 | .8289 | .8315 | .8340 | .8365 |
| 1.0 | .8413 | .8438 | .8461 | .8485 | .8508 | .8531 | .8554 | .8577 | .8599 |
| 1.1 | .8643 | .8665 | .8686 | .8708 | .8729 | .8749 | .8770 | .8790 | .8810 |
| 1.2 | .8849 | .8869 | .8888 | .8907 | .8925 | .8944 | .8962 | .8980 | .8997 |
| 1.3 | .9032 | .9049 | .9066 | .9082 | .9099 | .9115 | .9131 | .9147 | .9162 |
| 1.4 | .9192 | .9207 | .9222 | .9236 | .9251 | .9265 | .9278 | .9292 | .9306 |
| 1.5 | .9332 | .9345 | .9357 | .9370 | .9382 | .9394 | .9406 | .9418 | .9430 |
| 1.6 | .9452 | .9463 | .9474 | .9484 | .9495 | .9505 | .9515 | .9525 | .9535 |
| 1.7 | .9554 | .9564 | .9573 | .9582 | .9591 | .9599 | .9608 | .9616 | .9625 |
| 1.8 | .9641 | .9648 | .9656 | .9664 | .9671 | .9678 | .9686 | .9693 | .9700 |
| 1.9 | .9713 | .9719 | .9726 | .9732 | .9738 | .9744 | .9750 | .9756 | .9762 |
| 2.0 | .9772 | .9778 | .9783 | .9788 | .9793 | .9798 | .9803 | .9808 | .9812 |
| 2.1 | .9821 | .9826 | .9830 | .9834 | .9838 | .9842 | .9846 | .9850 | .9854 |
| 2.2 | .9861 | .9864 | .9868 | .9871 | .9874 | .9878 | .9881 | .9884 | .9887 |
| 2.3 | .9893 | .9896 | .9898 | .9901 | .9904 | .9906 | .9909 | .9911 | .9913 |
| 2.4 | .9918 | .9920 | .9922 | .9925 | .9927 | .9929 | .9931 | .9932 | .9934 |
| 2.5 | .9938 | .9940 | .9941 | .9943 | .9945 | .9946 | .9948 | .9949 | .9951 |
| 2.6 | .9953 | .9955 | .9956 | .9957 | .9959 | .9960 | .9961 | .9962 | .9963 |
| 2.7 | .9965 | .9966 | .9967 | .9968 | .9969 | .9970 | .9971 | .9972 | .9973 |
| 2.8 | .9974 | .9975 | .9976 | .9977 | .9977 | .9978 | .9979 | .9979 | .9980 |
| 2.9 | .9981 | .9982 | .9982 | .9983 | .9984 | .9984 | .9985 | .9985 | .9986 |
| 3.0 | .9987 | .9990 | .9993 | .9995 | .9997 | .9998 | .9998 | .9999 | .9999 |Table A1.2. Percentage points of the $t$-distribution

| $\boldsymbol{v} \backslash \boldsymbol{\alpha}$ | 0.100 | 0.050 | 0.025 | 0.01 | 0.005 | 0.001 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 3.078 | 6.314 | 12.706 | 31.821 | 63.657 | 318.310 |
| 2 | 1.886 | 2.920 | 4.303 | 6.965 | 9.925 | 23.326 |
| 3 | 1.638 | 2.353 | 3.182 | 4.541 | 5.841 | 10.213 |
| 4 | 1.533 | 2.132 | 2.776 | 3.747 | 4.604 | 7.173 |
| 5 | 1.476 | 2.015 | 2.571 | 3.365 | 4.032 | 5.893 |
| 6 | 1.440 | 1.943 | 2.447 | 3.143 | 3.707 | 5.208 |
| 7 | 1.415 | 1.895 | 2.365 | 2.998 | 3.499 | 4.785 |
| 8 | 1.397 | 1.860 | 2.306 | 2.896 | 3.355 | 4.501 |
| 9 | 1.383 | 1.833 | 2.262 | 2.821 | 3.250 | 4.297 |
| 10 | 1.372 | 1.812 | 2.228 | 2.764 | 3.169 | 4.144 |
| 11 | 1.363 | 1.796 | 2.201 | 2.718 | 3.106 | 4.025 |
| 12 | 1.356 | 1.782 | 2.179 | 2.681 | 3.055 | 3.930 |
| 13 | 1.350 | 1.771 | 2.160 | 2.650 | 3.012 | 3.852 |
| 14 | 1.345 | 1.761 | 2.145 | 2.624 | 2.977 | 3.787 |
| 15 | 1.341 | 1.753 | 2.131 | 2.602 | 2.947 | 3.733 |
| 16 | 1.337 | 1.746 | 2.120 | 2.583 | 2.921 | 3.686 |
| 17 | 1.333 | 1.740 | 2.110 | 2.567 | 2.898 | 3.646 |
| 18 | 1.330 | 1.734 | 2.101 | 2.552 | 2.878 | 3.610 |
| 19 | 1.328 | 1.729 | 2.093 | 2.539 | 2.861 | 3.579 |
| 20 | 1.325 | 1.725 | 2.086 | 2.528 | 2.845 | 3.552 |
| 21 | 1.323 | 1.721 | 2.080 | 2.518 | 2.831 | 3.527 |
| 22 | 1.321 | 1.717 | 2.074 | 2.508 | 2.819 | 3.505 |
| 23 | 1.319 | 1.714 | 2.069 | 2.500 | 2.807 | 3.485 |
| 24 | 1.318 | 1.711 | 2.064 | 2.492 | 2.797 | 3.467 |
| 25 | 1.316 | 1.708 | 2.060 | 2.485 | 2.787 | 3.450 |
| 26 | 1.315 | 1.706 | 2.056 | 2.479 | 2.779 | 3.435 |
| 27 | 1.314 | 1.703 | 2.052 | 2.473 | 2.771 | 3.421 |
| 28 | 1.313 | 1.701 | 2.048 | 2.467 | 2.763 | 3.408 |
| 29 | 1.311 | 1.699 | 2.045 | 2.462 | 2.756 | 3.396 |
| 30 | 1.310 | 1.697 | 2.042 | 2.457 | 2.750 | 3.385 |
| 40 | 1.303 | 1.684 | 2.021 | 2.423 | 2.704 | 3.307 |
| 60 | 1.296 | 1.671 | 2.000 | 2.390 | 2.660 | 3.232 |
| 120 | 1.289 | 1.658 | 1.980 | 2.358 | 2.617 | 3.160 |
| $\infty$ | 1.282 | 1.645 | 1.960 | 2.326 | 2.576 | 3.090 |Table A1.3. Percentage points of the chi-squared distribution

| $\nu \backslash \chi_{a}^{2}$ | $\chi_{99}^{2}$ | $\chi_{975}^{2}$ | $\chi_{95}^{2}$ | $\chi_{90}^{2}$ | $\chi_{10}^{2}$ | $\chi_{05}^{2}$ | $\chi_{025}^{2}$ | $\chi_{01}^{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0 | 0.00 | 0.00 | 0.02 | 2.71 | 3.84 | 5.02 | 6.64 |
| 2 | 0.02 | 0.05 | 0.10 | 0.21 | 4.61 | 5.99 | 7.38 | 9.21 |
| 3 | 0.12 | 0.22 | 0.35 | 0.58 | 6.25 | 7.82 | 9.35 | 11.35 |
| 4 | 0.30 | 0.48 | 0.71 | 1.06 | 7.78 | 9.49 | 11.14 | 13.28 |
| 5 | 0.55 | 0.83 | 1.15 | 1.61 | 9.24 | 11.07 | 12.83 | 15.09 |
| 6 | 0.87 | 1.24 | 1.64 | 2.20 | 10.65 | 12.59 | 14.45 | 16.81 |
| 7 | 1.24 | 1.69 | 2.17 | 2.83 | 12.02 | 14.07 | 16.01 | 18.48 |
| 8 | 1.65 | 2.18 | 2.73 | 3.49 | 13.36 | 15.51 | 17.54 | 20.09 |
| 9 | 2.09 | 2.70 | 3.33 | 4.17 | 14.68 | 16.92 | 19.02 | 21.67 |
| 10 | 2.56 | 3.25 | 3.94 | 4.87 | 15.99 | 18.31 | 20.48 | 23.21 |
| 11 | 3.05 | 3.82 | 4.58 | 5.58 | 17.28 | 19.68 | 21.92 | 24.73 |
| 12 | 3.57 | 4.40 | 5.23 | 6.30 | 18.55 | 21.92 | 23.34 | 26.22 |
| 13 | 4.11 | 5.01 | 5.89 | 7.04 | 19.81 | 22.36 | 24.74 | 27.69 |
| 14 | 4.66 | 5.63 | 6.57 | 7.79 | 21.06 | 23.69 | 26.12 | 29.14 |
| 15 | 5.23 | 6.26 | 7.26 | 8.57 | 22.31 | 25.00 | 27.49 | 30.58 |
| 16 | 5.81 | 6.91 | 7.96 | 9.31 | 23.54 | 26.30 | 28.85 | 32.00 |
| 17 | 6.41 | 7.56 | 8.67 | 10.09 | 24.77 | 27.59 | 30.19 | 33.41 |
| 18 | 7.02 | 8.23 | 9.39 | 10.87 | 25.99 | 28.87 | 31.53 | 34.81 |
| 19 | 7.63 | 8.91 | 10.12 | 11.65 | 27.20 | 30.14 | 32.85 | 36.19 |
| 20 | 8.26 | 9.59 | 10.85 | 12.44 | 28.41 | 31.41 | 34.17 | 37.57 |
| 21 | 8.90 | 10.28 | 11.59 | 13.24 | 29.62 | 32.67 | 35.48 | 38.93 |
| 22 | 9.54 | 10.98 | 12.34 | 14.04 | 30.81 | 33.92 | 36.78 | 40.29 |
| 23 | 10.20 | 11.69 | 13.09 | 14.85 | 32.01 | 35.17 | 38.08 | 41.64 |
| 24 | 10.86 | 12.40 | 13.85 | 15.66 | 33.20 | 36.42 | 39.36 | 42.98 |
| 25 | 11.52 | 13.12 | 14.61 | 16.47 | 34.38 | 37.65 | 40.65 | 44.31 |
| 26 | 12.20 | 13.84 | 15.38 | 17.29 | 35.56 | 38.89 | 41.92 | 45.64 |
| 27 | 12.88 | 14.57 | 16.15 | 18.11 | 36.74 | 40.11 | 43.19 | 46.96 |
| 28 | 13.57 | 15.31 | 16.93 | 18.94 | 37.92 | 41.34 | 44.46 | 48.28 |
| 29 | 14.26 | 16.05 | 17.71 | 19.77 | 39.09 | 42.56 | 45.72 | 49.59 |
| 30 | 14.95 | 16.79 | 18.49 | 20.60 | 40.26 | 43.77 | 46.98 | 50.89 |
| 35 | 18.48 | 20.56 | 22.46 | 24.81 | 46.03 | 49.80 | 53.21 | 57.36 |
| 40 | 22.14 | 24.42 | 26.51 | 29.07 | 51.78 | 55.76 | 59.35 | 63.71 |
| 50 | 29.69 | 32.35 | 34.76 | 37.71 | 63.14 | 67.50 | 71.42 | 76.17 |
| 60 | 37.47 | 40.47 | 43.19 | 46.48 | 74.37 | 79.08 | 83.30 | 88.39 |
| 70 | 45.43 | 48.75 | 51.74 | 55.35 | 85.50 | 90.53 | 95.03 | 100.44 |
| 80 | 53.53 | 57.15 | 60.39 | 64.30 | 96.55 | 101.88 | 106.63 | 112.34 |
| 90 | 61.74 | 65.64 | 69.12 | 73.31 | 107.54 | 113.15 | 118.14 | 124.13 |
| 100 | 70.05 | 74.22 | 77.93 | 82.38 | 118.47 | 124.34 | 129.57 | 135.81 |Table A1.4. Critical values $\mathrm{dn}, \alpha$ for the Kolmogorov-Smirnov test

| $n \backslash \alpha$ | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0.900 | 0.950 | 0.975 | 0.990 | 0.995 |
| 2 | 0.684 | 0.776 | 0.842 | 0.900 | 0.929 |
| 3 | 0.565 | 0.636 | 0.708 | 0.785 | 0.829 |
| 4 | 0.493 | 0.565 | 0.624 | 0.689 | 0.734 |
| 5 | 0.447 | 0.509 | 0.563 | 0.627 | 0.669 |
| 6 | 0.410 | 0.468 | 0.519 | 0.577 | 0.617 |
| 7 | 0.381 | 0.436 | 0.483 | 0.538 | 0.576 |
| 8 | 0.358 | 0.410 | 0.454 | 0.507 | 0.542 |
| 9 | 0.339 | 0.387 | 0.430 | 0.480 | 0.513 |
| 10 | 0.323 | 0.369 | 0.409 | 0.457 | 0.489 |
| 11 | 0.308 | 0.352 | 0.391 | 0.437 | 0.468 |
| 12 | 0.296 | 0.338 | 0.375 | 0.419 | 0.449 |
| 13 | 0.285 | 0.325 | 0.361 | 0.404 | 0.432 |
| 14 | 0.275 | 0.314 | 0.349 | 0.390 | 0.418 |
| 15 | 0.266 | 0.304 | 0.338 | 0.377 | 0.404 |
| 16 | 0.258 | 0.295 | 0.327 | 0.366 | 0.392 |
| 17 | 0.250 | 0.286 | 0.318 | 0.355 | 0.381 |
| 18 | 0.244 | 0.279 | 0.309 | 0.346 | 0.371 |
| 19 | 0.237 | 0.271 | 0.301 | 0.337 | 0.361 |
| 20 | 0.232 | 0.265 | 0.294 | 0.329 | 0.352 |
| 21 | 0.226 | 0.259 | 0.287 | 0.321 | 0.344 |
| 22 | 0.221 | 0.253 | 0.281 | 0.314 | 0.337 |
| 23 | 0.216 | 0.247 | 0.275 | 0.307 | 0.330 |
| 24 | 0.212 | 0.242 | 0.264 | 0.301 | 0.323 |
| 25 | 0.208 | 0.238 | 0.264 | 0.295 | 0.317 |
| 26 | 0.204 | 0.233 | 0.259 | 0.290 | 0.311 |
| 27 | 0.200 | 0.229 | 0.254 | 0.284 | 0.305 |
| 28 | 0.197 | 0.225 | 0.250 | 0.279 | 0.300 |
| 29 | 0.193 | 0.221 | 0.246 | 0.275 | 0.295 |
| 30 | 0.190 | 0.218 | 0.242 | 0.270 | 0.281 |# Appendix 2 

## Laplace Transform

If a function $h(x)$ can be obtained from some prescribed operation on a function $f(x)$, then $h(x)$ is often called a transform of $f(x)$. For example,

$$
\begin{aligned}
& h(x)=\sqrt{2+f(x)} \\
& h(x)=\frac{\partial}{\partial x} f(x)
\end{aligned}
$$

The Laplace transform of $f(t)$ is the function $f^{*}(s)$ where

$$
f^{*}(s)=\int_{0}^{\infty} e^{-s t} f(t) d t
$$

Often the Laplace transform is denoted as $f^{*}(s)$ or $\mathfrak{L}(f(t))$ or $\mathfrak{L}(f)$. The results of the Laplace transform for a few simple functions are presented below.

## Results

1. $\mathfrak{L}(1)=\int_{0}^{\infty} e^{-s t} d t=\frac{1}{s}$
2. $\mathfrak{L}\left(e^{-a t}\right)=\int_{0}^{\infty} e^{-s t} e^{-a t} d t=\int_{0}^{\infty} e^{-(s+a) t} d t$

$$
=\frac{1}{s+a}
$$3. If $f(t)=\frac{1}{a} e^{\frac{-t}{a}}$, then
$\mathfrak{L}(f(t))=\int_{0}^{\infty} e^{-s t} \frac{1}{a} e^{-\frac{t}{a}} d t=\frac{1}{1+s a}$
4. If $f(t)=t e^{a t}$, then
$\mathfrak{L}(f(t))=\int_{0}^{\infty} e^{-s t} t e^{a t} d t=\frac{1}{(s-a)^{2}}$
5. If $f(t)=\frac{1}{a}\left(e^{a t}-1\right)$, then
$\mathfrak{L}(f(t))=\int_{0}^{\infty} e^{-s t} \frac{1}{a}\left(e^{a t}-1\right) d t=\frac{1}{s(s-a)}$
6. If $f(t)=(1+a t) e^{a t}$, then
$\mathfrak{L}(f(t))=\int_{0}^{\infty} e^{-s t}(1+a t) e^{a t} d t=\frac{s}{(s-a)^{2}}$

Similarly, we can obtain the following results:
7. If $f(t)=\frac{a e^{a t}-b e^{b t}}{a-b}$, then
$\mathfrak{L}(f(t))=\frac{s}{(s-a)(s-b)} \quad$ for $a \neq b$
8. If $f(t)=\frac{\alpha^{k} t^{k-1} e^{-a t}}{\Gamma(k)}$ then
$\mathfrak{L}(f(t))=\left(\frac{\alpha}{\alpha+s}\right)^{k}$
9. If $f(t)=\frac{e^{a t}-e^{b t}}{a-b}$, for $a \neq b$, then
$\mathfrak{L}(f(t))=\frac{1}{(s-a)(s-b)}$10. If $f(t)=\lambda e^{-\lambda t}$, then

$$
\mathfrak{L}(f(t))=\frac{\lambda}{\lambda+s}
$$

11. $\mathfrak{L}\left(c_{1} f_{1}(t)+c_{2} f_{2}(t)\right)=\int_{0}^{\infty} e^{-s t}\left[c_{1} f_{1}(t)+c_{2} f_{2}(t)\right] \mathrm{d} t$

$$
=c_{1} \mathfrak{L}\left(f_{1}(t)\right)+c_{2} \mathfrak{L}\left(f_{2}(t)\right)
$$

12. If $f_{i}(t)=\lambda_{i} e^{-\lambda_{i} t}$, then

$$
\mathfrak{L}\left(\sum_{i=1}^{n} f_{i}(t)\right)=\sum_{i=1}^{n} \frac{\lambda_{i}}{\lambda_{i}+s}
$$

13. $\mathfrak{L}\left(\sum_{i=1}^{n} f_{i}(t)\right)=\sum_{i=1}^{n} \mathfrak{L}\left(f_{i}(t)\right)$
14. $\mathfrak{L}\left(f^{\prime}(t)\right)=\int_{0}^{\infty} e^{-s t} f^{\prime}(t) d t$

$$
\begin{aligned}
& =f(t) e^{-s t} \int_{0}^{\infty}+s \int_{0}^{\infty} f(t) e^{-s t} d t \\
& =-f\left(0^{+}\right)+s f^{+}(s) \\
& =-f\left(0^{+}\right)+s \mathfrak{L}(f(t))
\end{aligned}
$$# Appendix 3 

## Survey of Factors that Affect Software Reliability

## Name <br> Institution/company

This is a survey questionnaire concerning software reliability and environmental factors involved in the software development process. The environmental factors here include characteristics of the software itself (e.g., size), the development environment (e.g., people and tools), and all other factors during the whole software development process. The software reliability models that use testing time as the only influence factor may not be appropriate for the evaluation of the software reliability. In this study, we are interested in obtaining your opinion about the impact of environmental factors on software reliability, as well as some background information about you in order to keep your answer in perspective.

Please read the following paragraphs below and then answer all questions on the following pages. Section A is the survey deals with the issue of software reliability and environmental factors. The definitions of the factors are provided at the end of section A. Section B is some background information about you.

Please rank the following environmental factors in terms of identifying the significance of including them in the software reliability analysis. For example, if you think that "program complexity" is an extremely important factor, you should rank it at a level of " 7 ". In contrast, if you think it will not improve the assessment of software reliability at all, you may rank it at " 1 ". Each factor can take an integer value from " 0 " to " 7 ". Please do not omit any ranking. Thank you for your cooperation.

Please return this survey to: Software Engineer| Section A. Environmental Factors | Not <br> significant |  | Extremely <br> significant |  |  |  | No opinion |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| General |  |  |  |  |  |  |  |
| 1. Program complexity(e.g., size,) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2. Program categories (e.g., database, operating system, etc.) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 3. Difficulty of programming | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 4. Amount of programming effort | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 5. Level of programming technologies | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 6. Percentage of reused modules | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 7. Programming language | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Analysis and Design |  |  |  |  |  |  |  |
| 8. Frequency of program specification change | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 9. Volume of program design documents | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 10. Design methodology | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 11. Requirements analysis | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 12. Relationship of detailed design to requiremt | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 13. Work standards | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 14. Development management | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Coding |  |  |  |  |  |  |  |
| 15. Programmer skill | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 16. Programmer organization | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 17. Development team size | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 18. Program workload(stress) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 19. Domain knowledge | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 20. Human nature(mistake and work omission) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Testing |  |  |  |  |  |  |  |
| 21. Testing environment(duplication of product) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 22. Testing effort | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 23. Testing resource allocation | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 24. Testing methodologies | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 25. Testing coverage | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 26. Testing tools | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 27. Documentation | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Hardware systems |  |  |  |  |  |  |  |
| 28. Processors | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 29. Storage devices | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 30. Input/output devices | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 31. Telecommunication devices | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 32. System software | 1 | 2 | 3 | 4 | 5 | 6 | 7 |To what extent do you believe that the environmental factors will improve the accuracy of the software reliability assessment?

10\% 20\% 40\% 60\% 80\% 100\%

# Section B. Background Information 

B1. What kind of applications do you usually develop for?
__Safety-critical __ Commercial __ Inside users-oriented
B2. What type of software development experience do you have?
__Database__Operation system__Communicationcontrol__Language processor
B3. Number of years have you been working on software development $\qquad$
B4. Your title/position
_ Manager _ System engineer _ Programmer _ Tester _ Administrator _ Other
B5. Average percentage of the development time in your group spent on
Analysis phase: $\qquad$
Design phase: $\qquad$
Coding phase: $\qquad$
Testing phase: $\qquad$
Total: $\quad 100 \%$
B6. Average percentage of reusable code in your software applications:

Please complete all rankings and return to the researchers. Thank you!# Definitions of the Environmental Factors 

The environmental factors can be defined and measured as follows.

## Program Complexity

McCabe's V(G), Halstead's E and program size are well known complexity measures. There exists a significant relationship between each of these measures. However, it has been proved that none of these seemed significantly better than program size. For this reason, program size (Kiloline of code: KLOC) is used as a measure of program complexity. The level of this factor is "High", meaning the program size is greater than 50 KLOC , otherwise the level is "Low".

## Program Categories

The program categories indicate system complexity. There are four program categories: operating system, communication control program, data base management system, and languages processor

## Amount of Programming Effort

The deliberate programming effort may be regarded as effective for reducing the number of errors made. This is calculated in man years.

## Difficulty of Programming (PDIF)

Difficulty of programming is defined according to the Putnum as follows:

$$
\text { PDIF }=\frac{k}{t^{2}} \quad\left(\text { man years } / \text { years }^{2}\right)
$$

where
$k=$ the amount of programming effort
$t=$ the amount of programming time

## Level of Programming Technologies (TLVL)

The programming technologies are classified into four categories: design techniques, documentation techniques, programming techniques (including programming languages), and development computer access environment. Each of the categories had a rating scale (low, middle, and high) and the rating scores $\mathrm{T}=0.8,1$, 1.2 , respectively, are allocated. These rating scores were determined by referring to Boehm's cost driver productivity range. The final TLVL is computed as follows by using the rating scores:

$$
\mathrm{TLVL}=\sum_{i=1}^{4} T_{i}
$$

where $T_{i}=$ the rating score of category $i$.

## Percentage of Reused Code (PORC)

When people develop some new software products or when they update the old version of their software products, they usually keep some of the modules of thecode which can be reused, and add in some new ones. That is why it is important to include the measure:

$$
\mathrm{PORC}=\frac{S_{o}}{S_{N}+S_{o}}
$$

where
$S_{o}=$ kiloline of code for the existing modules
$S_{N}=$ kiloline of code for new modules

# Programming Languages 

Different programming languages have different complexity and structure; therefore there is the possibility for different languages to introduce errors are different.

## Frequency of Program Specification Change (SCHG)

SCHG is calcuated from the number of pages of problem reports generated to change the program design specifications during programming phase of development.

## Volume of Program Design Documents (DOCC)

Program design documents that lack sufficient contents for the program produce errors. DOCC is calculated from the number of pages of new and modified program design documents.

## Design Methodologies

Different design methodologies for the same software may have different impact on the quality of the final software products. There are two types of design methodologies: structured design and functional design.

## Requirements Analysis

Requirements are provided by customers. Based on the requirements, software developers generate specifications. Usually customers and developers meet to verify the requirements and achieve understanding of the problems. Requirement analysis is necessary following design and coding work.

## Relationship of Detailed Design to Requirements

At the end of the design phase, detailed design is compared with requirements. Inspections are performed to verify whether the functions designed meet the requirements. Modifications can be made to remove the misunderstanding between the customers and developers.

## Work Standard

Work standard is the norm the developing team needs to obey. This could be company standard or group standard. Work standard indicates products to be made at each phase, design document format, design document description level and content, and the items to be checked in verifying the design documents. Having this kind of norms or not has an impact on the quality of software products.# Development Management 

Development management includes all the organization and decision-making activities. From the specification phase to design, code, and testing and even operational phase, development managers schedule the meeting time, keep all participants in touch and keep track of the development progress and work standards, give instructions, make decisions.

## Programmer Skills (PSKL)

PSKL has direct impact on the reliability of software products. PSKL can be defined as the average number of years of programming experience of programmers:

$$
\operatorname{PSKL}=\frac{\sum_{i=}^{n} I_{i}}{n} \text { (years) }
$$

where
$I_{i}=$ number of years experience of programmer $I$
$n=$ the total number of programmers

## Programmer Organization (ICON)

ICON is defined as the percentage of high-quality programmers. ICON is computed as follows:

$$
\mathrm{ICON}=\frac{n_{h}}{n}
$$

where
$n_{h}=$ number of programmers whose programming experience is more than six years
$n=$ the total number of programmers.

## Development Team Size

Team size has impact on the quality of software products. Some believe that large team size will improve the quality of the software since there are more people involving on the development process. However, others claim that smaller but experienced development teams will be better.

## Program Work Contents (Stress)

During software development, stress factors in terms of "work contents" such as schedule pressure and too much work are the major factors. This includes developer's mental stress and physical stress. Stress can be classified into several degree groups.

## Domain Knowledge

Domain knowledge refers to the programmer's knowledge of the input space and output target. Insufficient knowledge may cause problems in coding and testing procedures.# Mental Stress and Human Nature 

This refer to the developers' characteristics, including the ability to avoid making working mistakes or careless work omission. Mental stress from deadlines or short development time causes imperfect survey, investigation, documentation, etc. Human nature causes developers to skip some part of the requirement procedures because of their experience. A study showing the ratios of stress factor effect to human nature factor effect for each error category are as follows:
(1) Imperfect investigation
6:1 (stress factors are dominant)
(2) Imperfect documentation
4:2 (stress factors are relatively effective)
(3) Imperfect survey
4:6 (stress factors are less effective)

## Testing Environment

In order to find out more errors during testing phase, testing environment should mimic the operational environment. This can be defined as the degree of compatibility of testing and operational environments.

## Testing Effort

Testing effort can be defined as the number of testing cases generated, testing expenditures, or human years that the testing takes.

## Testing Resource Allocation

Testing resource allocation refers to different schemes to allocate the testing resources, in terms of testers, facilities and schedules of the testing activities.

## Testing Methodologies

Different testing methodologies have different impact on the quality of software products. Good testing methodologies may test more paths and require less time.

## Testing Coverage

Test coverage is defined as the percentage of the source code which are covered by the test cases. It can be expressed as

$$
\mathrm{TCVG}=\frac{S_{c}}{S_{T}}
$$

where
$S_{c}=$ kiloline of code which is covered by testing
$S_{T}=$ total kiloline of code

## Testing Tools

There exist many different testing tools. These include the software packages testers utilize to carry out the testing tasks. Different tools also provide different quality and testing measures.

## Documentation

Documentation includes all paperwork from specification to design, coding and testing. This can serve as resources for developers to allocate changes andproblems, for programmers to review the codes, and for testers to examine the codes and detect bugs.

Factors 27-32 are the hardware systems used for software development. The definite is obvious.

Please complete all rankings and return to the researchers. Thank you!# References 

Agresti, A (1990) Categorical Data Analysis. Wiley, New York
ANSI/IEEE, (1991) "Standard Glossary of Software Engineering Terminology", STD-729 ANSI/IEEE

Akaike H (1974) "A new look at statistical model identification," IEEE Transactions on Automatic Control, 19:716-723

Anderson T, Lee P (1980) Fault Tolerance: Principles and Practices, Prentice-Hall, Englewood Cliffs

Anderson T, Barrett P, Halliwell D, Moulding M (1985) "Software fault tolerance: An evaluation," IEEE Transactions on Software Engineering, vol SE-11(12)

Arlat J, Kanoun K, Laprie J (1990) "Dependability modeling and evaluation of software fault tolerant systems," IEEE Transactions on Computers, vol. 39(4)

Ashrafi N, Berman O, Cutler M (1994) "Optimal design of large software-systems using N-version programming," IEEE Transactions on Reliability, v 43 n 2:344350

Avizienis A, Chen L (1977) "On the Implementation of N-Version Programming for Software Fault-Tolerance during Program Execution," Proceedings COMPASAC 77:149-155

Avizienis A, Lyu M, Schutz W (1988) "In search of effective diversity: A six language study of fault tolerant flight control software," in Digest of $18^{\text {th }}$ International Symposium on Fault Tolerant Computing, Tokyo, Japan

Bandinelli, S, et al. (1995) "Modeling and improving an industrial software process," IEEE Transactions on Software Engineering 21 (5): 440-453Barlow R, Proschan F, (1965) Mathematical Theory of Reliability, Wiley, New York

Barlow RE, Hunter LC, Proschan F (1963) "Optimum redundancy when components are subject to two kinds of failure,".J. Soc Ind Appl Math; 1 1(l):64-73

Basili VR, Perricone BT (1984) "Software errors and complexity: An empirical investigation," Communication ACM, vol 27, no. 1

Belady LA,Lehman MM (1976) "A model of large program development," IBM System Journal, vol 3

Belli F, Jedrzejowics P (1990) "Fault-tolerant programs and their reliability," IEEE Transactions on Reliability, v 39 n 2

Bendell T (1986) "The use of exploratory data analysis techniques for software reliability assessment and prediction," Software System Design Methods, Ed. J.K.SkSkwirynski, NATO ASI Series, Vol. F22, Springer-Verlag, Berlin:337-351

Ben-Dov Y (1980) "Optimal reliability design of $k$-out-of-n systems subject to two kinds of failure," J Opt Res Soc;31:743-748

Bertsbakh IB (2000) Statistical Reliability Theory, Marcel Dekker, New York
Blischke WR, Murthy DNP (2000) Reliability: Modeling, Prediction and Optimization, Wiley \& Sons:18

Boehm BW (1981) Software Engineering Economics, Prentice-Hall, Englewood Cliffs

Box J, Reinsel J (1994) Time-series Model, Wiley, New York
Cai K-Y (1998) "On estimating the number of defects remaining in software," Journal of Systems and Software,Vol. 40(l)

Chen L, Avizienis A (1978) "N-version programming: A fault tolerance approach to the reliable software," Proceedings of $8^{\text {th }}$ International Symposium FaultTolerant Computing, IEEE Computer Society Press

Chen M-H, Mathur AP, Rego VJ (1995) "Effect of testing techniques on software reliability estimates obtained using a time-domain model," IEEE Transactions on Reliability. v 44 n 1:97-103

Churchley, A (ed.), (1991) Microprocessor Based Protection Systems, Elsevier Applied Science, AmsterdamCoutinho JS (1973) "Software reliability growth," in Proceedings International Conference on Reliable Software, IEEE Computer Society Press, Los Angeles

Dalal SR, Mallows CL (1988) "When should one stop testing software," Journal of the American Statistical Association, vol. 83, No.403:872-879

Dalal SR, Mallows CL (1992) "Some graphical aids for deciding when to stop testing software," IEEE Journal on Selected Areas in Communication, Vol. 8, No. 2:169-175

Eckhardt DE, Lee LD (1985) "A theoretical basis for the analysis of multiversion software subject to coincident errors," IEEE Transactions on Software Engineering, vol SE-11(12)

Ehrlich W, Prasanna B, Stampfel J, Wu J (1993) "Determining the cost of a stoptesting decision," IEEE Software:33-42

Evanco WM, Lacovara R (1994) "A model-based framework for the integration of software metrics," Journal of Systems Software, vol 26:77-86

Fairley R (1985) Software Engineering Concepts, McGraw-Hill, N.Y
Feller W (1957) An Introduction to Probability Theory and its Applications, vol. 1, Wiley, New York

Fitzsimmons A, Love T (1978) "A review and evaluation of software science," ACM Computing Surveys, vol. 10(l)

Friedman MA, Voas JM (1995) Software Assessment - Reliability, Safety, Testability, John Wiley \& Sons, New York

Furuyama T, et al. (1994) "Fault generation model and mental stress effect analysis," Journal of Systems and Software 26:31-42

Furuyama T, Arai Y, Lio K (1997) "Analysis of fault generation caused by stress during software development," Journal of Systems and Software 38:13-25

Goel AL (1980) "A summary of the discussion on an analysis of computing software reliability models," IEEE Trans. Software Engineering, Vol. SE- 6(5)

Goel AL (1985) "Software reliability models: Assumptions, limitations, and applicability," IEEE Trans. Software Engineering, Vol. SE-2(12)

Goel AL,.Okumoto K (1979a) "Time-dependent error-detection rate model for software and other performance measures," IEEE Transaction on Reliability, 28:206-211Goel AL, Okumoto K (1979b) "A Markovian model for reliability and other performance measures of software systems," in Proc. COMPCON, IEEE Computer Society Press, Los Angeles

Goel AL, Okumoto K (1981) "When to stop testing and start using software?" ACM/Sigmetrics, 10:131-135

Gorsuch RL (1974) Factor Analysis. Philadelphia: W.B. Saunders Co.
Gray J (1990) "A census of Tandem system availability between 1985 and 1990", IEEE Transactions on Reliability, vol.39, no.4:409-418

Hakuta M, Ton F, Ohminami M (1997) "A software estimation model and its evaluation," Journal of Systems and Software 37:253-263

Halstead MH (1977) Elements of Software Science, Elsevier, New York
Handbook of Mathematical (1980), M. Fogiel (Ed.), Research and Education, New York

Home News \& Tribune (1997) "An eagle-eyed math lover:' 7 February 1997
Homing JJ, Lauer HC, Melliar-Smith PM, Randell B (1974) "A program structure for error detection and recovery," Lecture Notes in Computer Science, vol. 16. Springer:177-93

Hossain SA, Ram CD (1993) "Estimating the parameters of a non-homogeneous Poisson process model for software reliability," IEEE Transactions on Reliability, vol. 42, no 4:604-612

Hua KA, Abraham JA (1986) "Design of systems with concurrent error detection using software redundancy," in Joint Fault Tolerant Computer Conference, IEEE Computer Society Press

Huang XX (1984) "The hypergeometric distribution model for predicting the reliability of software," Microelectronics and Reliability, Vol. 24(l)

IEEE Standard Glossary of Software Engineering Terminology, (1990) IEEE Standard 610.12

Iyer RK, Velardi R (1985) "Hardware-related software errors: Measurement and analysis," IEEE Trans. Software Engineering, vol. SE-11(2)

Jambu M (1991) Exploratory and Multivariate Data Analysis, Academic PressJelinski Z, Moranda PB (1972) "Software reliability research," in Statistical Computer Performance Evaluation, W. Freiberger (ed), Academic Press, New York

Jenney BW, Sherwin DJ (1986) "Open and short circuit reliability of systems of identical items," IEEE Trans Reliability, R-35:532-538

Jones TC (1978) "Measuring programming quality and productivity," IBM Systems Journal, vol 17, no. 1

Kanoun K, Mohamed K, Beounes C, Laprie J-C, Arlat J (1993) "Reliability growth of fault-tolerant Software," IEEE Transactions on Reliability. v 42 n 2 Jun:205-218

Kapur PK, Bhalla VK (1992) "Optimal release policies for a flexible software reliability growth model", Reliability Engineering and System Safety, 35:45-54

Kareer N, Kapur PK, Grover PS (1990) "An S-shaped software reliability growth model with two types of errors", Microelectronics and Reliability--an International Journal, 30:1085-1090

Kim KH, Welch HO (1989) "Distributed execution of recover blocks: An approach for uniform treatment of hardware and software faults in real time applications," IEEE Transactions on Computers, vol.38, no. 5, May

Knight JC, Leveson NG (1986) "An experimental evaluation of the assumption of independence in multiversion programming," IEEE Transactions on Software Engineering, vol.12, no. 1

Koshimae H, Tanaka H, Osaki S (1994) "Some remarks on MTBF's for nonhomogeneous Poisson process," IEICE Trans. Fundamentals, vol E77-A(1), January

Lala RK (1985) Fault Tolerant \& Fault Testable Hardware Design, Prentice-Hall, London

Laprie JC, Arlat J, Beounes C, Kanoun K (1990) "Definition and analysis of hardware- and software-fault tolerant architectures," IEEE Computers, Vol. 23(7), July

Lee M, Pham H, Zhang X (1999) "A Methodology for Priority Setting With Application to Software Development Process," European Journal of Operational Research, vol. 118, no. 2, October:375-389

Leung YW (1992) "Optimal software release time with a given cost budget," Journal of Systems and Software, 17:233-242Leveson NG, Cha SS, Knight JC, Shimeall TJ (1990) "The use of self-checks and voting in software error detection: An empirical study," IEEE Transactions on Software Engineering, vol.16, no. 4

Lin H-H, Chen K-H (1993) "Nonhomogeneous Poisson process softwaredebugging models with linear dependence", IEEE Transactions on Reliability. v 42 n 4 Dec:613-617

Lindman HR (1992) Analysis of Variance in Experimental Design, SpringerVerlag

Lions JL (1996) Ariane 5 Flight 501 Failure: Report of the Inquiry Board, Paris, July 19

Littlewood B (1979) "Software reliability model for modular program structure," IEEE Trans. Reliability, Vol. R-28(3)

Littlewood B (1981) "Stochastic Reliability Growth: A Model for Fault Removal in Computer Programs and Hardware Design", IEEE Transactions on Reliability, (12): 313-320.

Littlewood B, Miller DR (1989) "Conceptual Modeling of Coincident Failures in Multiversion Software", IEEE Transactions on Software Engineering, vol.15, no. 12:1596-1614

Lyu MR (1993) "Improving the N-version programming process through the evolution of a design paradigm," IEEE Transactions on Reliability. v 42 n 2 Jun:179-189

Lyu MR (1996) Handbook of Software Reliability Engineering, McGraw-Hill, New York

Malaiya YK, Srimani PK (eds.), (1990) Software Reliability Models: Theoretical Developments, Evaluation and Applications, IEEE Computer Society Press, Los Angeles

Malaiya YK, Karunanithi N, Verma P (1992) "Predictability of software-reliability models," IEEE Transactions on Reliability. v 41 n 4, Dec:539-546

Malon DM (1989) "On a common error in open and short circuit reliability computation," IEEE Trans Reliab, 38:275-6

Mathur FP, De Sousa PT (1975) "Reliability modeling and analysis of general modular redundant systems," IEEE Trans Reliab;24:296-9McAllister DF, Sun CE, Vouk MA (1990) "Reliability of Voting in Fault-Tolerant Software Systems for Small Output Spaces," IEEE Transactions on Reliability, vol.39, no.5:524-534

McCabe TJ (1976) "A complexity measure," IEEE Trans. Software Engineering, Vol. SE-2(4)

McConnell, SC (1993) Code Complete, Microsoft Press, Richmond:395
Matsumoto K, Inoue K, Kikuno T, Torii K (1988) "Experimental evaluation of software reliability growth models,, Digest of Papers - FTCS (Fault-Tolerant Computing Symposium). n 88CH2543-7:148-153

May JHR, Lunn AD (1995) "Model of code sharing for estimating software failure on demand probabilities," IEEE Transactions on Software Engineering. v 21 n 9 Sept:747-753

Miller DR, Sofer A (1985) "Completely monotone regression estimation of software failure rate," Proc. International Conference on Software Engineering, IEEE Computer Society Press, Los Angeles

Mills HD (1970) "On the statistical validation of computer programs," IBM FSD, July (unpublished)

Misra PN (1983) "Software reliability analysis," IBM Systems Journal, 22:262-270
Moranda PB (1975) "A comparison of software error-rate models," Proc. Texas Conference on Computing Systems, IEEE Computer Society Press, Los Angeles

Moranda PB (1979) "An error detection model for application during software development," IEEE Trans. Reliability, Vol. R-28(5)

Musa JD (1975) "A theory of software reliability and its applications," IEEE Trans. on Software Engineering, vol. SE-1(3)

Musa JD, Okumoto K (1985)"Applications of basic and logarithmic Poisson execution model in software reliability measure," The Challenge of Advanced Computing Technology to System Design Methods, NATO Advanced Study Institute.

Musa JD, lannino A, Okumoto K (1987) Software Reliability: Measurement, Prediction, and Application, McGraw-Hill, NewYork.

Nakagawa Y (1994) "A connective exponential software reliability growth model based on analysis of software reliability growth curves," IEICE Trans., vol J77-DI(6), June:433-442Nicola VF, Goyal A (1990) "Modeling of correlated failures and community error recovery in multiversion software," IEEE Transactions on Software Engineering. v 16 n 3 Mar:350-359

Normann L, Pham H (1999) "Weighted voting systems," IEEE Transactions on Reliability, vol. 48, no. 1, March:42-49

Ohba M (1984) "Software reliability analysis models," IBM Journal of Research Development, 28:428-443

Ohba M (1984a) "Software reliability analysis models," IBM J Research Deuelopment, vol. 21(4)

Ohba M, Yamada S (1984b) "S-shaped software reliability growth models," Proc. 4th Int.Conf. Reliability and Maintainability:430-436

Ohba M, Chou XM (1989) "Does imperfect debugging affect software reliability growth?" Proc. 11th Int.Conf. on Software Engineering, IEEE Computer Society Press, Los Angeles

Ohtera H, Yamada S (1990) "Optimal allocation and control problems for software-testing resources," IEEE Transactions on Reliability, 39:171-176

Pham H (1989a), Optimal Designs of Systems With Competing Failure Modes, PhD Dissertation, State University of NewYork, Buffalo (unpublished).

Pham H, Upadhyaya SJ (1989b), "Reliability analysis of a class of fault tolerant systems," IEEE Transactions on Reliability, vol. 38, no. 3, August:333-337

Pham H, Pham M (1991a) Software reliability models for critical applications," Idaho National Engineering Laboratory, EG\&G2663, December

Pham H, Upadhyaya SJ (1991b) "Optimal design of fault tolerant distributed systems based on a recursive algorithm," IEEE Transactions on Reliability, vol. 40, no. 3, August:375-379

Pham H, Pham M (1991c) "Optimal designs of $(k, n-k+1)$ out-of-n: F systems (subject to 2 failure modes)," IEEE Trans Reliability; 40:559-562

Pham H (1992a) Fault-Tolerant Software Systems: Techniques and Applications, IEEE Computer Society Press

Pham H (1992b) "On the optimal design of k-out-of-n subsystems," IEEE Transactions on Reliability, vol. 41, no. 4, December:572-574

Pham H (1992c) "Optimal design of parallel-series systems with competing failure modes," IEEE Transactions on Reliability, vol. 41, no. 4, December:583-587Pham H (1992d) "Optimal system-profit design of series-parallel systems with multiple failure modes," Reliability Engineering and System Safety Journal, vol. 37, no. 2:151-155

Pham H (1993) Software reliability assessment: imperfect debugging and multiple failure types in software development.EG\&G-RAAM-10737; Idaho National Laboratory

Pham H (1994) "On the optimal design of N-version software systems subject to constraints", Journal of Systems \& Software. v 27 n 1 Oct:55-61

Pham H, Malon DM (1994) "Optimal design of systems with competing failure modes," IEEE Transactions on Reliability, vol. 43, no. 2, June: 251-254

Pham H (1995) Software Reliability and Testing, IEEE Computer Society Press
Pham H (1996a) "A software cost model with imperfect debugging, random life cycle and penalty cost," International Journal of Systems Science, vol. 27, no. 5:455-463

Pham H, Wang H (1996b) "Imperfect maintenance," European Journal of Operational Research, vol. 94:425-438

Pham H, Suprasad A, Misra RB (1996c) "Reliability and MTTF prediction of k-out-of-n complex systems with components subjected to multiple stages of degradation," International Journal of Systems Science, vol. 27, no. 10:995-1000

Pham H, Zhang X (1997a) "An NHPP software reliability model and its comparison," International Journal of Reliability, Quality and Safety Engineering, vol. 4, no. 3:269-282

Pham H, Normann L (1997b) "A generalized NHPP software reliability model," Proc. $3^{\text {rd }}$ ISSAT International Conf. on Reliability and Quality in Design, August, ISSAT Press, Anaheim

Pham H, Zhang X, Teng X, Pham L (1998a) Software reliability growth models and environmental factors study and its applications, Draft Report, prepared for the U.S. Federal Aviation Administration, September

Pham H, Zhang X (1999) "Software release policies with gain in reliability justifying the cost," Annals of Software Engineering, vol 8:147-166

Pham H (1999a) "Software Reliability," a chapter in Wiley Encyclopedia of Electrical and Electronic Engineering, Editor: John Webster, John Wiley and Sons:565-578Pham H, Nordmann L, Zhang X (1999b) "A general imperfect software debugging model with s-shaped fault detection rate," IEEE Transactions on Reliability, vol. 48, no. 2, June:169-175

Pham H, Zhang X (1999c) "A software cost model with warranty and risk costs," IEEE Trans on Computers, vol 48, no. 1:71-75

Pham H (1999d) "Reliability analysis for dynamic configurations of systems with three failure modes," Reliability Engineering and System Safety, vol. 63:13-23

Pham H, Wang H (2000) "Optimal (t,T) Opportunistic Maintenance of a k-out-of-n System with Imperfect PM and Partial Failure," Naval Research Logistics, vol. 47:223-239

Pham H (2000a) Software Reliability, Springer-Verlag
Pham H, Wang H (2001) "A Quasi Renewal Process for Software Reliability and Testing Costs", IEEE Transactions on Systems, Man, and Cybernetics - Part A, vol. 31, no. 6, November:623-631

Pham H (2002) "Hardware-software reliability perspectives", a chapter in the Engineering Reliability, Editors: Y. Hayakawa, A. Itory, and Min Xie, World Scientific:41-72

Pham H (2002a), "A Vtub-shaped hazard rate function with applications to system safety", International Journal of Reliability and Applications, vol. 3,no. 1:1-16

Pham H, Xie M (2002b) "A generalized surveillance model with applications to systems safety," IEEE Transactions on Systems, Man and Cybernetics - Part C, vol. 32:485-492

Pham H (2003) Handbook of Reliability Engineering, Springer
Pham H, Deng C (2003a) "Predictive-ratio risk criterion for selecting software reliability models," Proc. Ninth International Conf. On Reliability and Quality in Design, August

Pham H (2003b) "Software reliability and cost models: perspectives, comparison and practice," European Journal of Operational Research, vol. 149: 475-489

Pham H (2003c) "Recent studies in software reliability engineering," a chapter in the Handbook of Reliability Engineering, Editor: Hoang Pham, Springer:285-302

Pham H, Zhang X (2003d) "NHPP software reliability and cost models with testing coverage," European Journal of Operational Research, vol. 145:443-454Pham H (2003e) "Commentary: Steady-state series-system availability," IEEE Transactions on Reliability, vol. 52, no. 2, June:146-147

Pham H (2003f) "Reliability of systems with multiple failure modes," a chapter in the Handbook of Reliability Engineering, Editor: Hoang Pham, Springer:19-36

Pham H (2005c) "A new generalized systemability model," International Journal of Performability Engineering, vol 1, no. 2:145-155

Pham H, Zhang X (2005b), "A New Coverage Software Model," International Journal of Plant Engineering (to appear)

Pressman RS (1983) Software Engineering: A Practitioner's Approach, Addison Wesley

Randell B (1975) "System structure for software fault tolerance," IEEE Transactions on Software Engineering, vol. SE-1, no.2, June:220-232

Roberts Jr., TL et al. (1998) "Factors that impact implementing a system development methodology", IEEE Transactions on Software Engineering, 24 (8):640-648

Rook P (1990) Software Reliability Handbook, Elsevier Applied Science, Amsterdam

Saaty TL (1980) The Analytic Hierarchy Process, McGraw-Hill, New York
Sah RK, Stiglitz JE (1988) "Qualitative properties of profit making $k$-out-of-n systems subject to two kinds of failures, " IEEE Trans Reliab;37:515-520

Sawyer S, Guinan PJ (1998) "Software development: processes and performance," IBM System Journal 37(4)

Schick GJ, Wolverton RW (1978) "An analysis of competing software reliability Models," IEEE Trans. Software Engineering, vol. SE- 4(2)

Schneberger SL (1997), "Distributed computing environments: Effects on software maintenance difficulty", Journal of Systems Software, 37:101-116

Schneidewind NF (1993) "Software reliability model with optimal selection of failure data", IEEE Transactions on Software Engineering. v 19 n 11 Nov: 10951104

Schneidewind NF (1997) "Reliability modeling for safety-critical software," IEEE Transactions on Reliability, vol. 46, no. 1Scott RK, Gault JW, McAllister DF (1987) "Fault-tolerant reliability modeling," IEEE Transactions on Software Engineering, vol. SE-13, no. 5:582-592

Sinpurwalla ND (1991) "Determining an optimal time interval for testing and debugging software," IEEE Transaction on Software Engineering, vol.17:313-319

Singpurwalla ND (1995) "Failure rate of software: Does it exist?" IEEE Transactions on Reliability. v 44, Sept:463-469

Spector A, Grifford D (1984) "The space shuttle primary computer system, Communications of the ACM, vol. 27, no.8:874-900

Subramanian GH, Breslawski S (1995) "An empirical analysis of software effort estimate alternations," Journals of Systems Software 31:135-141

Sukert AN (1977) "An investigation of software reliability models," in Proc. Annual Reliability \& Maintainability Symposium, IEEE Reliability Society, Piscataway

Tai AT, Meyer JF, Aviziems A (1993) "Performability enhancement of faulttolerant software," IEEE Transactions on Reliability, vol. 42 no. 2:227-237

Teng X, Pham H (2002) "A software reliability growth model for N-version programming systems," IEEE Transactions on Reliability, vol. 51, no. 3:311-321

Teng X, Pham H (2003) "Software fault tolerance", a chapter in the Handbook of Reliability Engineering, Editor: Hoang Pham, Springer:585-611

Teng X, Pham H (2004) "A software cost model for quantifying the gain with considerations of random field environments", IEEE Transactions on Computers

Teng X, Pham H, Jeski D (2001) "A new methodology for predicting software reliability in the random field environments," submitted to the IEEE Transactions on Reliability

Tohma Y, Yamano H, Ohba M, Jacoby R (1991) "The estimation of parameters of the hypergeometric distribution and its application to the software reliability growth model," IEEE Trans. Software Engineering, vol. SE-17(5)

Tokuno K, Yamada S (1997) "Markovian availability measurement and assessment for hardware-software systems," Int. J Reliability, Quality and Safety Engineering, Vol. 4(3)

Voas JM, Miller KW (1995) "Software testability: The new verification," IEEE Software, vol.12:17-28Wald A (1947) Sequential Analysis, John Wiley \& Sons, New York
Wall JK, Ferguson PA (1977) "Pragmatic software reliability prediction," Proc. Annual Reliability \& Maintainability Symposium, IEEE Reliability Society, Piscataway

Walls LA, Bendell A (1986) "An exploratory approach to software reliability measurement," Software Reliability: State of the Art Report, Eds. A. Bendell and P. Mellor, Pengamon Infotech Ltd.:209-227

Wang H, Pham H (1996) "Optimal Age-Dependent Preventive Maintenance Policies With Imperfect Maintenance", International Journal of Reliability, Quality and Safety Engineering, vol. 3, no. 2:119-135

Wang H, Pham H (1996a),"A Quasi Renewal Process and Its Applications in Imperfect Maintenance", International Journal of Systems Science, vol. 27, no. 10:1055-1062

Wang H, Pham H (1996b) "Optimal Maintenance Policies for Several Imperfect Repair Models", International Journal of Systems Science, vol. 27, no. 6:543-549

Wang H, Pham H (1997) "Optimal opportunistic maintenance of a k-out-of-n:G system," International Journal of Reliability, Quality and Safety Engineering, vol. 4, No. 4:369-386

Weibull W (1951) "A statistical distribution function of wide applicability," $J$ Applied Mech., Vol. 18:293-297

Welke SR, Johnson BW, Aylor, JH (1995) "Reliability modeling of hardware/software systems", IEEE Transactions on Reliability. v 44 n 3 Sept:413418

Wightman D, Bendell T (1995) "Comparison of proportional hazards modeling, additive hazards modeling and proportional intensity modeling when applied to repairable system reliability," International Journal of Reliability, Quality and Safety Engineering: 23-34

Wood A (1996) "Predicting software reliability", IEEE Computer, 11:69-77
Xie M (1991) Software Reliability Modelling, World Scientific, Singapore
Yamada S, Ohba M, Osaki S (1983) "S-shaped reliability growth modeling for software error detection," IEEE Transactions on Reliability, 12:475-484

Yamada S, Ohba M, Osaki S (1984) "S-shaped software reliability growth models and their applications," IEEE Trans. Reliability, Vol. R-33, OctoberYamada S, Osaki S (1985) "Software reliability growth modeling: models and applications," IEEE Transactions on Software Engineering, 11:1431-1437

Yamada S, Ohtera H, Narihisa H (1986) "Software reliability growth models with testing-effort", IEEE Trans. Reliability, Vol. R- 35(l)

Yamada S, Osaki S (1987) "Optimal software release policies with simultaneous cost and reliability criteria", European J. of Operational Research, 31, 1:46-51

Yamada S (1991) "Software Quality/Reliability measurement and assessment: software reliability growth models and data analysis", Journal of Information Processing, vol. 14, no. 3:254- 266

Yamada S, Tokuno K, Osaki S (1992) "Imperfect debugging models with fault introduction rate for software reliability assessment", International Journal of Systems Science, vol. 23, num. 12

Yamada S, Hishitani J, Osaki S (1993a) "Software reliability growth models with a Weibull test-effort function," IEEE Trans. Reliability, Vol. R-42(l)

Yamada S, Tokuno K, Osaki S (1993b) "Software reliability measurement in imperfect debugging environment and its application," Reliability Engineering \& System Safety. v 40 n 2:139-147

Yamada S, Tokuno K, Kasano Y (1998) "Quantitative assessment models for software safety/reliability," Electronics and Communications in Japan, Part 2, vol 81, no. 5

Yang M, Chao A (1995) "Reliability-estimation \& stopping-rules for software testing, based on repeated appearances of bugs," IEEE Transactions on Reliability. v 44 n 2 Jun:315-321

Yau SS, Cheung RC (1975) "Design of self-checking software," in Reliable Software, IEEE Press, April

Yau SS, Tsai JJ (1986) "A survey of software design techniques", IEEE Transactions on Software Engineering 12 (6): 713-721

Zeephongsekul P, Xia G, Kumar S (1994) "Software-reliability growth model: Primary-failures generate secondary-faults under imperfect debugging," IEEE Transactions on Reliability. v 43 n 3 Sept:408-413

Zhang X, Pham H (1998) "A software cost model with warranty cost, error removal times and risk costs", IIE Transactions on Quality and Reliability Engineering, vol. 30, no. 12:1135-1142Zhang X, Pham H (1998a) "A software cost model with error removal times and risk costs," International Journal of Systems Science, vol 29, no 4: 435-442

Zhang X (1999) "Software Reliability and Cost Models with Environmental Factors", Ph. D. thesis, Rutgers University, New Jersey

Zhang X, Pham H (2000) "Comparisons of nonhomogeneous Poisson process software reliability models and its applications," International Journal of Systems Science, vol. 31, no. 9:1115-1123

Zhang X, Pham H (2000a) "An analysis of factors affecting software reliability," Journal of Systems and Software, vol. 50:43-56

Zhang X, Shin M-Y, Pham H (2001a) "Exploratory analysis of environmental factors for enhancing the software reliability assessment," Journal of Systems and Software, vol. 57:73-78

Zhang X, Jeske DR, Pham H (2002) "Calibrating software reliability models when the test environment does not match the user environment," Applied Stochastic Models in Business and Industry, vol. 18:87-99

Zhang X, Teng X, Pham H (2003) "Considering fault removal efficiency in software reliability assessment," IEEE Trans. on Systems, Man, and Cybernetics Part A, vol. 33, no.1:114-120

Zhao M (2003) "Statistical reliability change-point estimation models," in Handbook of Reliability Engineering, H. Pham (ed.), Springer:157-163

Zhao M, Xie M (1996) "On maximum likelihood estimation for a general nonhomogeneous Poisson process," Scandinavian J. Statistics, vol 23# Basic Glossary, Definitions and Terminologies 

Some basic glossary and useful definitions are referred to and are used throughout the book.

Accelerated test. A test in which the applied stress level is chosen to exceed that stated in the reference conditions in order to shorten the time required to observe the stress response of the equipment in a given time.
Algorithm. A prescribed set of instructions, rules or processes for solving a problem in a finite number of steps.
ANOVA (Analysis of Variance). A statistical technique that is used to compare the differences between two or more groups in order to decide whether or not there is a difference between the groups on the measured variable.
Artificial intelligence (AI). A system of algorithms that attempts to create programs capable of emulating human characteristics such as learning and reasoning.
Availability. The probability that the system is operating satisfactorily at any point in time when used under stated conditions.

Binary code. A system for representing information by combinations of two numbers such as ones and zeros.
Bug. An unintended property of computer software or hardware that causes a computer operation to malfunction or to function unexpectedly.
Burn-in. The operation of systems prior to their ultimate application intended to stabilize their characteristics and to identify early failures.

Chi-square. A statistical test to help one make a decision about whether the items being counted are proportionally distributed among the groups.
Clean test. A test with the primary purpose of validation, i.e., a test designed to demonstrate the software's correct working.
Central processing unit (CPU). The central part of the computer containing the arithmetic logic unit, control unit, and memory.
Code. Parts of computer programs.
Constant failure rate. That period during which failures of some units occur at an approximately uniform rate.Compatibility. The ability of two or more systems to exchange information. Component. One element of a system or a part of an application.
Corrective action. A documented design (development) process or materials changes implemented and validated to correct the cause of a failure.
Correlation. A statistical technique that determines the relationship between two variables.

Data. A representation of facts or instructions in a manner suitable for processing by computers or analyzing by human.
Debugging. The detection, location, and correction of errors or bugs in hardware or software systems.
Decision mapping. The process of identifying a need and deciding on the corresponding element of the framework.
Degradation. A gradual impairment in ability to perform the required function.
Dependent variable. A factor in an experimental setting that depends on the action of the independent variable.
Derating. The intentional reduction of stress and strength ratio in the application of an item, usually for the purposes of reducing the occurrence of stress-related failures.
Developer. An individual or team assigned a particular task.
Dirty test. A test with the primary purpose of falsification i.e., test designed to break the software.
End-user. Anyone who uses a computer system at an application level.
Failure density. At any point in the life of a system, the incremental change in the number of failures per associated incremental change in time.
Failure effect. The consequences a failure mode has on the operation or status of a system. Failure effects may be classified as minor effects, major effects, or critical effects.
Failure rate. At a particular time, the rate of change of the number of units that have failed divided by the number of units surviving.
FORTRAN (FORmula TRANslator). FORTRAN was the first high-level programming language. It was developed in 1954 by IBM and is used to perform scientific and engineering computations.
Fuzzy sets. Fuzzy sets refer to a classes of sets with a continuous grade of membership involving a gradual transition from membership to non-membership.

Hardware. The physical, tangible equipment that makes up a computer system.
High-level language. A programming language that approximates human language more closely than does machine code or assembly language, and in which one statement may invoke several machine-code or assembly-language instructions.
Heuristics. These pertain to exploratory methods of problem solving in which solutions are devised by evaluation of the progress made towards the final result.

Infant mortality. The initial phase in the lifetime of a population of a particular system when failures occur as results of latent defects, manufacturing errors, or design errors.Input. Information fed into a computer system.
Integration test. Test that explores the interaction and consistency of successfully tested units.
Interface. The connection and interrelationships among hardware, software and the users.

Machine code. A set of binary digits that can be directly understood by a computer without translation.
Maintainability. The probability that, when maintenance action is initiated under stated conditions, a failed system will be restored to operable condition within a specified total downtime.
Markov-Chain. When the behavior of a system is described by a certain state at a specified time, the probability of its future states of existence depends only upon the present state and not on how the system reached that state, the system state behavior can be described by a process called the Markov process. A Markov process whose state space is discrete is called a Markov chain.
Memory. The principal work space inside a computer in which data can be recorded or from which it is retrieved.
Mean time between failures (MTBF). The mean time between failures of a system computed from its design considerations and from the failure rates of its components under the intended conditions of use.
Module. A specific part of a hardware or software component.
Multiple regression. A statistical technique that allows predictions to be made about the performance of one variable based on performance of two or more other variables.
Multivariate analysis. Any statistical technique that looks at the relationship between three or more variables.
Multivariate correlation. A statistical technique that can be used to determine the relationship between two sets of variables.

Object. A generic term that includes data and software.
Operational profile. The set of operations that the software can execute, given the probability of their occurrence.
Operating system. A set of programs used to control, assist, or supervise all other programs that run on a computer system.
Output. The result of a computation, generated by a computer.
Principle component analysis. A multivariate statistical technique that analyzes the relationships among a large number of variables, allowing the users to describe these relationships in terms of a smaller set of constructed variables. If this is successful, the new "components" can be thought of as describing the structure of the original data set.
Process improvement. Act of monitoring development practices and actively seeking ways to increase value: reduce error, increase productivity, enhance the developer's environment.
Program. A sequence of instructions for performing some operation or solving some problem by computer.Regression coefficients. Numbers in a regression equation that represent the amount that one variable contributes to the prediction of another variable.
Reliability. The ability of a system to perform a required function under stated conditions for a stated period of time.
Reusability. The degree to which software modules can be used for multiple applications.
Risk. The combination of the frequency or probability, and the consequence of a specified hazardous event.

Safety-related system. Those systems that enable, independently of other systems, the tolerable risk level to be met.
Safety integrity. The likelihood of a safety-related system achieving its required functions under all stated conditions within a time period.
Safety validation. The process of determining the level of conformance of the final operating system to safety requirements specification.
Serviceability. The degree of ease or difficulty with which a system can be repaired or maintained.
Software. The programs that enable a computer system to run.
Software availability. The probability that a system has not failed due to a software fault.
Software defect. A generic term referring to a fault or a failure.
Software engineering. A systematic approach to the development and maintenance of software that begins with analysis of the software's goals of purposes.
Software error. An error made by a programmer or designer, e.g., a typographical error, an incorrect numerical value, an omission, etc.
Software fault. An error that leads to a software fault. Software faults can remain undetected until software failure results.
Software failure. A failure that occurs when the user perceives that the software has ceased to deliver the expected result with respect to the specification input values. The user may need to identify the severity of the levels of failures, e.g., catastrophic, critical, major or minor, depending on their impact on the systems. Severity levels may vary from one system to another, and from application to application. Typically, the severity of a software system effect is classified into four categories:

Category 1: Catastrophic. This category is for disastrous effects, e.g., loss of human life or permanent loss of property, the effect of an erroneous medication prescription or an air-traffic controller error.
Category 2: Critical. This category is for disastrous but restorable damage. It includes damage to equipment without lost of human life or where there is major but curable illness or injury.
Category 3: Major. This category is for serious failures of the software system where there is no physical injury to people or other systems. This may include erroneous purchase orders or the breakdown of a vehicle.
Category 4: Minor. This category is for faults that cause marginal inconveniences to a software system or its users. Examples might be a vending machine that momentarily cannot provide change or a bank's computer system that is not working when a consumer requests an account balance.Software debugging. Activity to isolate faults and eliminate underlying error.
Software MTTF. The expected time when the next failure is observed due to software faults.
Software maintainability. The probability that a program will be restored to working condition in a given period of time when it is being changed, modified, or enhanced.
Software MTTR. The expected time to restore a system to operation upon a failure due to software faults.
Software reliability. The probability that software will not fail for a specified period of time under specified conditions.
Software testing. A verification process for software quality evaluation and improvement.
Software validation. The process of ensuring that the software is executing the correct task.
Software verification. The process of ensuring that the software is executing the task correctly.
Source code. The lines of programming in a high-level language that are fed to a computer to be translated into machine code or assembly language.
Specifications. The stated requirements of a system under development.
Standard deviation. A statistical technique measuring the variability of a sample of scores from the mean of a sample.
System availability. The probability that a system is available when needed.
System effectiveness. The probability that the system can successfully meet an operational demand for a given time under specified conditions.
System testing. Testing that explores system behavior that cannot be done by unit, component, or integration testing. System testing presumes that all components have been previously and successfully integrated and is often performed by independent testers.
t-test. A common statistical test used to allow one to determine whether differences between two groups are reliable.
Test. A sequence of one or more subtests executed as a sequence because the result of one subtest is the input of the next.
Test design. The process of specifying the input and predicting the result for that input.
Test strategy. A systematic method used to select and/or generate tests to be included in a test suite.
Test suite. A set of one or more tests, usually aimed at a single input, with a common purpose and database, usually run as a set.
Type I error. An error made when one believes there are differences in an experimental group because of the independent variables, when in fact the differences were the results of chance.
Type II error. An error made when one believes there are no differences between experimental groups when in fact the independent variable did have an influence.

Useful life. The length of time a system operates with an acceptable failure rate.Acronyms

| AIC | Akaike's information criterion |
| :-- | :-- |
| ANOVA | Analysis of Variance |
| cdf | Cumulative distribution function |
| GO model | Goel and Okumoto model |
| JM model | Jelinski and Moranda model |
| LLF | Log likelihood function |
| ln | Natural logarithm |
| LOC | Lines of code |
| MLE | Maximum likelihood estimate |
| MSE | Mean squared errors |
| MTBF | Mean time between failure |
| MVF | Mean value function |
| NHPP | Non-homogeneous Poisson process |
| NVP | N-version programming |
| pdf | Probability density function |
| PNZ model | Pham, Nordmann and Zhang model |
| PRR | Predictive-ratio risk |
| SRGM | Software reliability growth model |
| SSE | Sum of squared errors |
| SW model | Schick and Wolverton model |
| WF model | Wall and Ferguson model |# Solutions to Selected Problems 

## Chapter 2

27. see (Pham 2000a, page 334)
28. see (Pham 2000a, page 334)

## Chapter 3

1. see (Pham 2000a, page 330)
2. see (Pham 2000a, page 331)
3. see (Pham 2000a, page 333)

## Chapter 5

2. The MLE of $N$ and $\phi$ can be obtained by solving the following two equations simultaneously:

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{1}{N-i+1} & =\phi \sum_{i=1}^{n} t_{i} \\
\sum_{i=1}^{n}(N-i+1) t_{i} & =\frac{n}{\phi}
\end{aligned}
$$

The above two equations can be solved and obtained as follows:

$$
\left(\sum_{i=1}^{n}(N-i+1) t_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{N-i+1}\right)=n \sum_{i=1}^{n} t_{i}
$$and

$$
\phi=\frac{n}{\sum_{i=1}^{n}(N-i+1) t_{i}}
$$

5. The probability of removing k induced errors and $(r-k)$ indigenous errors in $m$ tests is a combination of binomial and hypergeometric distributions and is given by

$$
\begin{aligned}
& P\left(k ; N+n_{1}, n_{1}, r, m\right)=\binom{m}{r}(1-q)^{r} q^{m-r} \frac{\binom{n_{1}}{k}\binom{N}{r-k}}{\binom{N+n_{1}}{r}} \\
& N \geq r-k \geq 0, \quad n_{\mathrm{i}} \geq k \geq 0, \text { and } m \geq r
\end{aligned}
$$

# Chapter 6 

3. (a) By Equation (6.10), the MLE of parameters $a$ and $b$ of the G-O model are given by

$$
a=99 \text { and } b=0.28
$$

(b) The mean value function and the reliability function are

$$
m(t)=99\left(1-e^{-0.28 t}\right)
$$

and

$$
R(x / t)=e^{-99\left[e^{-0.28(t+\varepsilon)}-e^{-0.28 t}\right]}
$$

respectively.
(c) Assume $x=2$ and $t=10$, then

$$
R(2 / 10)=e^{-99\left[e^{-0.28(12)}-e^{-0.28(10)}\right]}=0.077
$$

(d) Consider the logarithmic NHPP model, also known as Musa-Okumoto (M-O ) model where the mean value function, a logarithmic function of time, is given by

$$
m(t)=a \ln (1+b t)
$$

Using the MLE, the parameter estimate of $a$ and $b$ can be obtained as follows:

$$
a=94 \text { and } b=0.17
$$

The mean value function and the reliability function are

$$
\begin{aligned}
m(t) & =a \ln (1+b t) \\
& =94 \ln (1+0.17 t)
\end{aligned}
$$and

$$
R(x / t)=e^{-94\left\{\ln (1+0.17(t+x)-\ln (1+0.17 t)\right\}}
$$

respectively.
The probability that a software failure does not occur during the interval $[10,12]$ is

$$
\begin{aligned}
R(x=2 / t=10) & =e^{-94\left\{\ln (1+0.17(12)-\ln (1+0.17(10))\right\}} \\
& =1.44 \times 10^{-5}
\end{aligned}
$$

From the table below, we can observe that the G-O model fits the actual data better than the M-O model, and therefore, the G-O model is a better model for this application data set.

| Hour | G-O model <br> $m(\mathrm{t})$ | M-O model <br> $m(\mathrm{t})$ | Actual data |
| :--: | :--: | :--: | :--: |
| 1 | 24 | 15 | 27 |
| 2 | 42 | 28 | 43 |
| 3 | 56 | 39 | 54 |
| 4 | 67 | 49 | 64 |
| 5 | 75 | 59 | 75 |
| 6 | 81 | 66 | 82 |
| 7 | 85 | 74 | 84 |
| 8 | 88 | 81 | 89 |
| 9 | 91 | 87 | 92 |
| 10 | 93 | 93 | 93 |

# Chapter 10 

8. Proof of Theorem 10.2 (Chapter 10). From equation (10.11), the first derivative of $E(T)$ is:
$f(T)=\frac{d E(T)}{d T}$
$=C_{1}-e^{-(1+b T)}$
$\left\{T\left\{\left(C_{3} D-C_{2} \mu_{y} a\right) e b^{2}-C_{2} \mu_{y} a b \alpha\left\{\ln (1+b T)+\sum_{i=0}^{\infty} \frac{(1+b t)^{i+1}-1}{(i+1)!(i+1)}\right\}\right\}+C_{2} \mu_{y} a \alpha\right\}$

1. If $\mathrm{A} \geq 0$, then
(1) If $T_{g}>0$, then function $u(T)$ intersects with $T$-axis at two points, i.e., $T=0$ and $T_{u}=u^{-1}(0) . \quad u(T) \geq 0$ for $T \in\left[0, T_{u}\right]$ and $u(T)<0$ for $T>T_{u}$. Since $v(T)>0 \forall T, f(T)$ intersects with T-axis at two points (see Figure A), i.e.,$T_{f 1}=f^{-1}(0)$ and $T_{f 2}=\left\{T: T>T_{f 1}, T=f^{-1}(0)\right\}$. Then $f(T) \geq 0$ for $T \in\left[0, T_{f 1}\right]$, $f(T)<0$ for $T \in\left(T_{f 1}, T_{f 2}\right]$, and $f(T) \geq 0$ for $T \in\left[T_{f 2}, \infty\right)$. Therefore, $E(T)$ is an increasing function of T for $T \in\left[0, T_{f 1}\right]$, reaches its maximum at $T_{f 1}$ and a decreasing function of $T$ for $T \in\left(T_{f 1}, T_{f 2}\right]$, after reaching its minimum at $T_{f 2}$ becomes an increasing function of $T$ again (see Figure A). Under this circumstance:
a) if $T_{f 2}>T_{R}, T^{*}=T_{f 2}$ minimizes $E(T)$
b) if $T_{f 2}<T_{R}, T^{*}=T_{R}$
c) It is worthwhile to notice that $f(0)=0$ is a special case of the aforementioned subcase (1), where the excepted total cost function $E(T)$ is a monotone function of time $T$ and is minimized at an unique point $T_{f 2}$.
(a) if $T_{f 2}>T_{R}, T^{*}=T_{f 2}$ minimizes $E(T)$;
(b) if $T_{f 2}<T_{R}, T^{*}=T_{R}$.

Figure A below illustrates the relationships of functions $u(T), f(T)$, and $E(T)$.
(2) If $T_{g} \leq 0$, then $g(T) \leq=0 \forall T$. Function $u(T)$ intersects with the T-axis at only one point $T_{u}=u^{-1}(0)$. Function $u(T) \geq 0$ for $T \in\left[0, T_{u}\right]$ and $u(T)<0$ for $T>T_{u}$. Then this subcase becomes the same as subcase (1) for the following discussion.
2. If $A<0$, then $f(T)$ is a strictly increasing and positive function of $T$. The expected total cost function $E(T)$ will be a strictly increasing and convex function of $T$. Hence, $T^{*}=0$ minimizes $E(T)$.

Figure A. Functions $u(T), f(T)$, and $E(T)$9. Proof of Theorem 10.5

Taking the first derivative of $E(T)$ as given in equation (10.33), we obtain

$$
\begin{aligned}
\frac{d E(T)}{d T} & =-C_{1}-C_{2} \cdot \mu_{y} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T}+ \\
& \mu_{w} \cdot C_{3} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T}\left(1-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}\right)+ \\
& C_{5} \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T} \cdot R\left(T_{w} \mid T\right) \cdot\left(1-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}\right) \\
& +\left(C_{4}+C_{6}\right) \cdot a \cdot b \cdot e^{-b \cdot(p-\beta) \cdot T} \cdot R\left(x \mid T+T_{w}\right) \cdot \\
& \left(\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot T_{w}}\right)^{T}-\left(\frac{\theta}{\theta+b \cdot(p-\beta) \cdot\left(T_{w}+x\right)}\right)^{T}\right) \\
& =y(T)
\end{aligned}
$$

Taking the second derivative of $E(T)$, we have

$$
\frac{d^{2} E(T)}{d T^{2}}=e^{-b T}[u(T)-C]
$$

where $u(T)$ and $C$ are defined in equations (10.35) and (10.36), respectively.
Case 1. If $u(0) \leq C$, then $u(T) \leq C$ for any $T$. In this case $\frac{d^{2} E(T)}{d T}<0$ and $y(T)$ is an decreasing function of $T$. There are three subcases:

1. If $y(0) \leq 0$, then $y(T) \leq 0$ for all $T$ and $E(T)$ is strictly decreasing in $T$. Hence, $T^{*}=0$ maximizes $E(T)$
2. If $y(\infty)>0$, then $y(T) \geq 0$ for all $T$ and $E(T)$ is increasing in $T$. Hence, $T^{*}=$ $\infty$ maximizes $E(T)$
3. If $y(0)>0$, then there exists a $T^{\prime}$ such that $y(T)>0$ for any $T \in\left(0, T^{\prime}\right]$ and $y(T) \leq 0$ for any $T \in\left(T^{\prime}, \infty\right]$. Therefore, $T^{*}=T^{\prime}$ minimizes $E(T)$, where $T^{\prime}=y^{-1}(0)$.
Case 2. If $u(\infty) \geq C$, then $u(T) \geq C$ for any $T$. In this case $\frac{d^{2} E(T)}{d T}>0$ and $y(T)$ is a strictly increasing function of $T$. There are three subcases:
4. If $y(0) \geq 0$, then $y(T) \geq 0$ for all $T$ and $E(T)$ is strictly increasing in $T$. Hence, $T^{*}=\infty$ maximizes $E(T)$
5. If $y(\infty)<0$, then $y(T)<0$ for all $T$ and $E(T)$ is decreasing in $T$. Hence, $T^{*}$ $=0$ maximizes $E(T)$
6. If $y(0)<0, y(\infty)>0$, then there exists a $T^{\prime \prime}$ such that $y(T) \leq 0$ for any $T \in$ $\left(0, T^{\prime \prime}\right]$ and $y(T)>0$ for any $T \in\left(T^{\prime \prime}, \infty\right]$. Therefore, $T^{*}=T^{\prime \prime}$ minimizes $E(T)$, where $T^{\prime \prime}=y^{-1}(0)$. Therefore, $T^{*}=0$ if $E(0) \leq E(\infty)$ and $T^{*}=\infty$ if $E(0)>E(\infty)$.Case 3. If $u(0)>\mathrm{C}, u(\infty)<\mathrm{C}$, then there exists a $T^{0}$ such that $u(T) \geq \mathrm{C}$ for $T \in\left(0, T^{0}\right]$, and $u(T)<\mathrm{C}$ for $T \in\left(T^{0}, \infty\right]$, where $T^{0}=u^{-1}(C)$

1. If $y(0)<0$, then for $T \in\left(0, T^{0}\right], \frac{d^{2} E(T)}{d T} \geq 0, y(T)$ is an increasing function of $T$. Similarly, from case 2 , if $y\left(T^{0}\right) \leq 0$, then $T^{*}=0$. If $y\left(T^{0}\right)>0$, then

$$
T^{*}= \begin{cases}T^{0} & \text { if } \mathrm{E}\left(T^{0}\right)>\mathrm{E}(0) \\ 0 & \text { otherwise }\end{cases}
$$

If $y\left(T^{0}\right)>0$, for $T \in\left(T^{0}, \infty\right], \frac{d^{2} E(T)}{d T}<0, y(T)$ is an decreasing function of $T$. Notice $y(\infty)<0$, then from case $1, T^{*}=T_{b}$ maximizes $E(T)$, where $T_{b}=y^{-1}(0)$, $T_{b}>T^{0}$. Since $E\left(T_{b}\right) \geq E\left(T^{0}\right)$, then the optimal solution is

$$
\begin{aligned}
& T^{*}=0 \text { if } E(0) \geq E\left(T_{b}\right) \\
& T^{*}=T_{b} \text { if } E(0)<E\left(T_{b}\right)
\end{aligned}
$$

2. If $y(0)>0$, then for $T \in\left(0, T^{0}\right], \frac{d^{2} E(T)}{d T} \geq 0, y(T)$ is an increasing function of $T$. From case $2, E\left(T^{0}\right)>E(0)$. For $T \in\left(T^{0}, \infty\right]$, Notice $y(\infty)<0, y\left(T^{0}\right)>0$, and $\frac{d^{2} E(T)}{d T}<0, y(T)$ is an decreasing function of $T$, then from case $1, T^{*}=T_{c}$ maximizes $E(T)$, where $T_{c}=y^{-1}(0), T_{c}>T^{0}$, and $E\left(T_{c}\right)>E\left(T^{0}\right)>E(0)$.# Index 

## A

Absorbing Markov process 56
Absorbing process 52
AIC criteria 182
Akaike's information criterion 181
Akiyama's software data 157
Analysis phase 128
Analytic hierarchy process 133
ANOVA 262
Applications 48, 279, 303
Asymptotic normality 89
ATM 1
Automatic transfer machine 1
Availability 15

## B

Barlow and Proschan 45
Baseline failure intensity 280
Bathtub-shaped 30
Bayesian method 113
Ben-Dov 47
Bessel function 64
Best choice 47
Beta distribution 28
Beta model 302
Binomial distribution 16
Binomial parameters 104

## C

Cai's model 161
Calibrating factor 293

Calibrating model 293
Cdf 22
Censored data 86
Central limit theorem 18
Change-point estimation 91
Chao 251
Chi-squared test 96
Chilled water system 122
Coding phase 130
Common-cause failures 355
Complete censored data 88
Complex-system model 375
Compound Poisson process 64
Computer system 1
Conditional probability 52
Connective model 192
Counting process 62
Confidence intervals 88, 306
Confidence limits 101
Constant failure rate 18
Correlation analysis 263
Coutinho model 171
Covariance stationary 63
Cramer-Rao inequality 78
Curve fitting models 169

## D

Data analysis 135
Data sets 136
Definitions 389Delayed S-shaped 190
Design phase 129
Digital system 48
Distribution tables 395

## E

Environmental factors 258
Environmental estimation 275
EPJM model 276
Ergodic process 52
Error seeding model 159
European Space Agency 4
Expected revenue gain model 336
Exploreatory analysis 263
Exponential distribution 17
Exponential imperfect
debugging 198
Extended Pham-Zhang model 210

## F

Factor analysis 266
Failure data sets 136
Failure distribution 13
Failure rate 13, 18
Failure rate function 13
Failure rate models 164
Fault density 3
Fault detection timedependent rate 251
Fault detection rate 248
Fault tolerant system 48, 347
Fault tolerant techniques 348
Fault removal efficiency 224
Future problems in the $21^{\text {st }}$
Century 5

## G

Gain model 332
Gamma distribution 26, 33, 84
Gamma model 301
Goel-Okumoto model 183
Goodness of fit 96

## H

Halstead's software metric 154
Hardware reliability 122
Hardware $v s$ software 123

Hardware-software model 379
Hazard function 22
Homogeneous Poisson
process 63
Hybrid fault tolerant system 353
Hypergeometric distribution 162
HW/SW interactions 384

## I

IBM online data 231
Imperfect debugging 211
Imperfect debugging model 179, 194
Imperfect fault detection rate 225
Independent faults 357
Inflection S-shaped model 189
Intensity function 69
Interval availability 58
Interval estimation 100

## J

Jelinski-Geometric model 168
Jelinski-Moranda model 164

## K

k-out-of-n system 36, 46
Kolmogorov-Smirnov test 98

## $\mathbf{L}$

Laplace transforms 55, 66
Latent deterioration process 72
Least squared estimation 98
Lightbulb 16
Likelihood function 85
Littlewood Markov model 172
Loglog distribution 30
Lognormal distribution 21
London ambulance service 4

## $\mathbf{M}$

Maintainability 14
Markov process 50
Markov structure models 172
Maximum likelihood function 79
McMcbe's cyclomatic metric 157
Mean value function 65
Mean time between failures 213
Mean time to repair 14Memoryless property 18
Minimum variance 78
MLE with censored data 86
Model selection 181
MSE criteria 182
Multiple-censored data 86
Multiple failure types 247, 326
Musa 95
MTBF 15
MTTR 14
Multiple failure modes 41

## $\mathbf{N}$

N -version programming 350
Nakagawa 192
Naval tactical data 141
Negative-binomial Poisson model 168
NHPP models 175
Exponential models 182
G-O model 183
Musa model 185
S-shaped 188
Yamada models 187
Environmental factors 272
Random field model 298
Nonparametric 106
Normal distribution 18
Normal parameters 100
Nordmann 198
Nonhomogeneous Poisson
Process 69
Nonhomogeneous Poisson
Process models 175
NTDS data 204

## O

Ohba 187
Operating phase 132
Optimal release policies 315, 320

## $\mathbf{P}$

Parallel system 35, 43
Parallel-series system 44
Parameter estimation 86, 180, 252
Pareto distribution 28
Partial likelihood approach 276

Patriot missile systems 4
Perfect debugging 211
Pham 46, 196, 198, 213, 221,251, 317, 321
Pham distribution 30
Pham-Zhang NHPP 201
Point availability 60
Point estimation 77
Poisson distribution 17
Poisson process 63
Poisson parameters 106
Predictive ratio risk 182
Prior density 116
PRR criteria 182
PZN model 198

## Q

Quasi-renewal processes 66

## $\mathbf{R}$

Random field environments 296, 332
Rayleigh distribution 29
Real-time system data 95
Recovery block scheme 349
REF model 301
Regression analysis 269
Release policies 320
Reliability 10
Reliability calculations 42
Reliability function 70
Reliability growth model 171
Reliability measures 10
Reliability modeling 35, 377
Reliability prediction 311
Removal model 219
Renewal function 65
Renewal processes 64
Renewal theory 68
Risk factor 317
Risk cost model 317

## $\mathbf{S}$

Schick-Wolverton model 166, 169
Self-checking duplex system 352
Sequential sampling 107
Series system 34, 42
Series-parallel system 45Software vs hardware 123
Software cost model 316, 323
Software development process 121
Software lifecycle 127
Software module 2
Software-related problems 3
Software reliability 122
Software reliability modeling 153
Software safety model 173
Software testing 124
Software V\&V 134
Software verification 134
SSE criteria 181
Standard normal distribution 19
Steady state availability 61
Survey analysis 258
System mean time to failure 11
System reliability 41
System reliability concept 9
Systemability function 32

## T

Tables 395
Tandem computer data 207
Teng 337
Testing coverage 219, 319

Testing phase 131
Time series 174
Transition probability 51
Triple version programming 357
TVP reliability function 364

## $\mathbf{U}$

Unbiased estimator 78
Unreliability 10

## V

Variance of systemability 40
Vtub-shaped function 30

## W

Wall and Ferguson model 171
Wang 67, 69
Weibull distribution 24, 83

## Y

Yamada 187, 193
Y2K problems 6

## $\mathbf{Z}$

Zhang 198,220, 227, 294, 317, 321