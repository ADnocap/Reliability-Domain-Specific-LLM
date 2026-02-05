# Springer Series in Reliability Engineering 

## Hongzhou Wang $\cdot$ Hoang Pham

## Reliability and Optimal MaintenanceSpringer Series in Reliability Engineering# Series Editor 

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
Toshio Nakagawa# Hongzhou Wang and Hoang Pham 

## Reliability and Optimal Maintenance

With 27 FiguresHongzhou Wang, PhD<br>Lucent Technologies<br>Whippany, New Jersey<br>USA

Hoang Pham, PhD<br>Department of Industrial Engineering<br>Rutgers<br>The State University of New Jersey<br>Piscataway, New Jersey<br>USA

British Library Cataloguing in Publication Data
A catalogue record for this book is available from the British Library
Library of Congress Control Number: 2006926891
Springer Series in Reliability Engineering series ISSN 1614-7839
ISBN-10: 1-84628-324-8 e-ISBN 1-84628-325-6 Printed on acid-free paper
ISBN-13: 978-1-84628-324-6
(c) Springer-Verlag London Limited 2006

Apart from any fair dealing for the purposes of research or private study, or criticism or review, as permitted under the Copyright, Designs and Patents Act 1988, this publication may only be reproduced, stored or transmitted, in any form or by any means, with the prior permission in writing of the publishers, or in the case of reprographic reproduction in accordance with the terms of licences issued by the Copyright Licensing Agency. Enquiries concerning reproduction outside those terms should be sent to the publishers.

The use of registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant laws and regulations and therefore free for general use.

The publisher makes no representation, express or implied, with regard to the accuracy of the information contained in this book and cannot accept any legal responsibility or liability for any errors or omissions that may be made.

Printed in Germany
987654321
Springer Science+Business Media
springer.comTo Connie and Grace.

- Hongzhou Wang

To Michelle, Hoang Jr., and David.

- Hoang Pham# Preface 

This book aims to present a state-of-the-art survey of theories and methods of reliability, maintenance, and warranty with emphasis on multi-unit systems, and to reflect current hot topics: imperfect maintenance, economic dependence, opportunistic maintenance, quasi-renewal processes, warranty with maintenance and economic dependency, and software testing and maintenance. This book is distinct from others because it consists mainly of research work published on technical journals and conferences in recent years by us and our co-authors.

Maintenance involves preventive and unplanned actions carried out to retain a system at or restore it to an acceptable operating condition. Optimal maintenance policies aim to provide optimum system reliability and safety performance at the lowest possible maintenance costs. Proper maintenance techniques have been emphasized in recent years due to increased safety and reliability requirements of systems, increased complexity, and rising costs of material and labor. For some systems, such as aircraft, submarines, and nuclear power stations, it is extremely important to avoid failure during actual operation because it is dangerous and disastrous.

Special features of our book include: (a) Imperfect maintenance. Imperfect maintenance has being receiving a great deal of attention in reliability and maintenance literature. In fact, its study indicates a significant breakthrough in reliability and maintenance theory; (b) Quasi-renewal processes. Quasi-renewal processes, including renewal processes as a special case, have been proven to be an effective tool to model hardware imperfect maintenance and software reliability growth; (c) Economic dependence and opportunistic maintenance. For maintenance of multi-component systems, economic dependency is one of the major concerns. Due to it, preventive maintenance (PM) on non-failed but deteriorated components may be carried out when corrective maintenance (CM) activities are performed since PM with CM can be executed without substantial additional expense. Accordingly, 'opportunistic' maintenance is resulted in; (d) Correlated failure and repair; (e) Emphasis on multicomponent systems; (f) Combined criteria on maintenance optimization. Usual criteria on maintenance optimization are based on maintenance cost measures only. In this book, optimization criteria are based on both cost and reliability indices; (g) Multipledegraded systems and inspection-maintenance; (h) Software reliability and maintenance models based on quasi-renewal processes; (i) Warranty cost models with imperfect maintenace, dependence, and emphasis on multi-component systems; (j) Monte Carlo reliability simulation techniques and issues.

This book is a valuable resource for understanding the latest developments in reliability, maintenance, inspection, warranty, software reliability models, and Monte Carlo reliability simulation. Postgraduates, researchers, and practitioners in reliability engineering, maintenance engineering, operations research, industrial engineering, systems engineering, management science, mechanical engineering, and statistics will find this book a state-of-the-art survey of the field. This book can serve as a textbook for graduate students, and a reference book for researchers and practioners.

Chapter 1 provides an introduction to recent hot topics in reliability and maintenance engineering, and sketch the framework of this book. Chapter 2 surveys imperfect repair and dependence research in detail to summarize significant approaches to model imperfect maintenance and dependence while Chapter 3 overviews various maintenance policies in the literature and practice, such as age-dependent PM policy, and repair limit policy.

In Chapter 4, we introduce a new modeling tool for imperfect maintenance: a quasi-renewal process which includes the ordinary renewal process as a special case and model imperfect maintenance of one-unit systems using the quasi-renewal process. Eleven imperfect maintenance models based on the quasi-renewal process are discussed in this chapter.

In practice, many systems are series systems or can be simplified into series systems. Chapter 5 investigates reliability and maintenance costs of a series system with $n$ components subject to imperfect repair, and correlated failure and repair, and looks into its optimal maintenance. Some important properties of reliability and maintenance cost of the series system are discussed. Imperfect repairs are modeled through increasing and decreasing quasi-renewal processes.

Opportunistic maintenance of a system with $(n+1)$ subsystems and economic dependence among them is discussed in Chapter 6, in which whenever a subsystem fails its repair is combined with PM of the functioning one having increasing failure rate if it reaches some age. Two different imperfect modeling methods are used in this chapter.

In Chapter 7 we look into preparedness maintenance policies for a system with $n+1$ subsystems, economic dependency and imperfect maintenance. In this preparedness maintenance policy, the system is placed in storage and is called on to perform a given task only if a specific but unpredictable emergency occurs. Some maintenance actions resulting in optimal system "preparedness for field use" may be taken while the system is in storage.

Chapter 8 presents three new opportunistic maintenance models for a $k$-out-of$n$ :G system with economic dependency and imperfect maintenance. The results, including at least 13 existing maintenance models as special cases, generalize and unify some previous work.

Chapter 9 studies multi-state degraded systems subject to multiple competing failure processes including two independent degradation processes and random shocks. We first model system reliability and then discuss optimal condition-basedinspection-maintenance. A quasi-renewal process is employed to establish the inter-inspection sequence.

In current highly competitive markets, warranty policies become more and more complex. Chapter 10 discusses warranty cost models of repairable complex systems from the manufacturers' point of view under three types of existing warranty policies: free repair warranty (FRPW), free replacement warranty (FRW), and pro-rata warranty (PRW), and two new warranty policies: renewable full service warranty (RFSW) and repair-limit risk-free warranty (RLRFW). Imperfect or minimal repair is considered. Monte Carlo simulation techniques and a new modeling tool - a truncated quasi-renewal process - will be used. The focus is on multi-component systems.

Chapter 11 models software reliability and testing costs using the quasi-renewal process, and discusses optimal software testing and release policies. Several software reliability and cost models are presented. Optimum testing policies incorporating both reliability and cost measures are investigated.

To obtain the optimal maintenance policy for a complex system, it is necessary to determine system availability or MTBF. However, there are some difficulties in evaluating complex large-scale system reliability and availability given confidence levels using classical statistics. In Chapter 12 Monte Carlo reliability, availability and MTBF simulation techniques will be examined together with variance reduction methods, simulation errors, etc.

We would like to express our appreciation to our wives, Xuehong Connie Wang and Michelle Pham, and to our families for their patience, understanding, and assistance during the preparation of this book. The constructive comments, encouragement, and support of our colleagues are very much appreciated. We are indebted to Kate Brown, Anthony Doyle and the Springer staff for their editorial work.

Hongzhou Wang
Bell Laboratories
Whippany, New Jersey
Hoang Pham
Rutgers University
Piscataway, New Jersey
November 2005# Contents 

1 Introduction ..... 1
1.1 Imperfect Maintenance ..... 2
1.2 Dependence. ..... 4
1.3 Warranty, Dependence, Imperfect Maintenance ..... 6
1.4 Criteria on Maintenance Optimization ..... 7
1.5 Scope of this Book ..... 7
1.5.1 General Methodologies ..... 7
1.5.2 Directions ..... 8
1.5.3 Framework ..... 11
2 Imperfect Maintenance and Dependence ..... 13
2.1 Imperfect Maintenance ..... 13
2.1.1 Modeling Methods for Imperfect Maintenance. ..... 14
2.1.2 Typical Imperfect Maintenance Models by Maintenance Policies ..... 23
2.2 Dependence. ..... 29
3 Maintenance Policies and Analysis ..... 31
3.1 Introduction ..... 31
3.2 Maintenance Policies for One-unit Systems ..... 32
3.2.1 Age-dependent PM Policy ..... 32
3.2.2 Periodic PM Policy ..... 35
3.2.3 Failure Limit Policy ..... 38
3.2.4 Sequential PM Policy ..... 39
3.2.5 Repair Limit Policy ..... 40
3.2.6 Repair Number Counting and Reference Time Policy ..... 42
3.2.7 On the Maintenance Policies for Single-unit Systems ..... 43
3.3 Maintenance Policies of Multi-unit Systems ..... 45
3.3.1 Group Maintenance Policy ..... 46
3.3.2 Opportunistic Maintenance Policies ..... 47
4 A Quasi-renewal Process and Its Applications ..... 51
4.1 A Quasi-renewal Process ..... 524.1.1 Definition ..... 52
4.1.2 Quasi-renewal Function ..... 55
4.1.3 Associated Statistical Testing Problems ..... 56
4.1.4 Truncated Quasi-renewal Processes ..... 59
4.2 Periodic PM with Imperfect Maintenance ..... 62
4.2.1 Model 1: Imperfect Repair and Perfect PM ..... 62
4.2.2 Model 2: Imperfect Repair and Imperfect PM ..... 63
4.2.3 Model 3: Imperfect Repair and Imperfect PM ..... 64
4.2.4 Model 4: Imperfect Repair and Imperfect PM ..... 68
4.2.5 Model 5: Imperfect Repair and Imperfect PM ..... 70
4.2.6 Model 6: Imperfect Repair and Imperfect PM ..... 72
4.3 Cost Limit Replacement Policy - Model 7 ..... 73
4.4 Age-dependent PM Policies with Imperfect Maintenance ..... 76
4.4.1 Model 8: Imperfect Repair ..... 76
4.4.2 Model 9: Imperfect CM and Imperfect PM ..... 80
4.4.3 Model 10: Two Imperfect Repairs ..... 82
4.4.4 Model 10a: Two Imperfect Repairs Considering Repair Time ..... 85
4.4.5 Model 11: Imperfect Repair and Perfect PM ..... 87
4.5 Concluding Discussions ..... 88
5 Reliability and Optimal Maintenance of Series Systems with Imperfect Repair and Dependence ..... 91
5.1 Introduction ..... 91
5.2 System Availability Indices Modeling ..... 94
5.3 Modeling of Maintenance Costs ..... 101
5.3.1 Cost Model 1 ..... 101
5.3.2 Cost Model 2 ..... 102
5.4 Optimal System Maintenance Policies ..... 103
5.4.1 Optimality of Availability and Maintenance Cost Rates ..... 103
5.4.2 Optimal Repair Policy ..... 108
5.5 Concluding Discussions ..... 110
6 Opportunistic Maintenance of Multi-unit Systems ..... 111
6.1 Optimal Maintenance Policies by the $(p, q)$ Rule ..... 114
6.1.1 Modeling of Availability and Cost Rate ..... 115
6.1.2 Other Operating Characteristics ..... 120
6.1.3 Optimization Models ..... 123
6.2 Optimal Maintenance Policies by the $(p(t), q(t))$ Rule ..... 124
6.2.1 Modeling of Availability and Cost Rate ..... 124
6.2.2 Other Performance Measures ..... 130
6.2.3 Optimal Maintenance Policy ..... 131
6.3 Concluding Remarks ..... 132
7 Optimal Preparedness Maintenance of Multi-unit Systems with Imperfect Maintenance and Economic Dependence ..... 135
7.1 Introduction ..... 135
7.2 System Maintenance Cost Rate and 'Availability' ..... 1407.3 Other Operating Characteristics ..... 146
7.4 Optimization Models ..... 149
7.5 Concluding Discussions ..... 150
8 Optimal Opportunistic Maintenance Policies of $\boldsymbol{k}$-out-of-n Systems ..... 151
8.1 Introduction ..... 151
8.2 Perfect PM ..... 155
8.3 Imperfect PM: Case 1 ..... 159
8.4 Imperfect PM: Case 2 ..... 161
8.5 Special Cases ..... 163
8.6 Optimization Problems ..... 166
8.7 Numerical Example ..... 167
8.8 Concluding Discussions ..... 169
9 Reliability and Optimal Inspection-maintenance Models
of Multi-degraded Systems ..... 171
9.1 Reliability Modeling ..... 174
9.1.1 System Description and Modeling Methodologies ..... 174
9.1.2 Reliability Modeling ..... 179
9.1.3 Numerical Examples ..... 180
9.2 Optimal Inspection-maintenance ..... 185
9.2.1 A General Inspection-maintenance Policy ..... 187
9.2.2 Average Long-run Maintenance Cost Analysis ..... 189
9.2.3 Algorithms for Optimal Inspection-maintenance Policy ..... 196
9.2.4 Numerical Example ..... 199
10 Warranty Cost Models with Dependence and Imperfect Repair ..... 203
10.1 RFSW Policies for Multi-component Systems ..... 207
10.1.1 Background ..... 207
10.1.2 Model Details ..... 208
10.1.3 RFSW for Series Systems ..... 210
10.1.4 RFSW for Parallel Systems ..... 215
10.1.5 RFSW for Series-parallel Systems ..... 216
10.1.6 RFSW for Parallel-series Systems ..... 218
10.1.7 A Numerical Example and Sensitivity Study ..... 222
10.2 DWC for Minimally Repaired Series Systems ..... 225
10.2.1 Preliminary Results ..... 227
10.2.2 DWC Under an FRW Policy ..... 228
10.2.3 DWC Under an PRW Policy ..... 231
10.2.4 Numerical Examples ..... 231
10.2.5 Future Research ..... 235
10.3 RLRFW Policies with Imperfect Repair ..... 236
10.3.1 Introduction ..... 236
10.3.2 Analysis of Repair-limit Risk-free Warranties ..... 237
10.3.3 Special Cases ..... 240
10.3.4 Numerical Examples and Sensitivity Analysis ..... 242
10.3.5 Concluding Remarks ..... 24410.4 Optimal RRLRFW Policies with Minimal Repair ..... 245
10.4.1 A General Optimization Model ..... 247
10.4.2 Cost Analysis of RRLRFW Policy ..... 249
10.4.3 Optimal RRLRFW Policy ..... 252
10.4.4 Remarks ..... 253
10.5 On Warranty Policies and their Comparison ..... 254
11 Software Reliability, Cost, and Optimization Models ..... 259
11.1 Introduction ..... 259
11.2 Use of Quasi-renewal Process in Software Reliability ..... 261
11.3 Software Reliability and Cost Modeling ..... 261
11.3.1 Model 1 ..... 262
11.3.2 Model 2 ..... 265
11.4 Optimization Models ..... 269
11.5 Concluding Discussions ..... 274
12 Monte Carlo Reliability Simulation of Complex Systems ..... 275
12.1 Introduction ..... 275
12.2 Typical Monte Carlo Algorithms for Reliability ..... 277
12.2.1 K-R Method ..... 277
12.2.2 R-M Method ..... 280
12.2.3 C-H Method ..... 282
12.2.4 L-D-L Method ..... 283
12.2.5 L-D Method ..... 284
12.2.6 Other Methods for Non-repairable Systems ..... 284
12.2.7 Monte Carlo Methods for Repairable Systems ..... 286
12.3 Variance Reduction and Random Number Generation ..... 288
12.4 On Monte Carlo Reliability Simulation ..... 290
12.5 Commercial Monte Carlo Reliability Simulation Tools ..... 292
12.6 A General Monte Carlo Reliability Procedure ..... 293
Appendix Elements of Reliability and Probability ..... 295
A. 1 Reliability Measures ..... 295
A. 2 Common Probability Distribution Functions ..... 296
A.2.1 Discrete Random Variable Distributions ..... 296
A.2.2 Continuous Random Variable Distributions ..... 298
A. 3 Stochastic Processes Concepts ..... 302
A.3.1 Markov Processes ..... 302
A.3.2 Counting Processes ..... 303
A.3.3 Poisson Processes ..... 303
A.3.4 Renewal Processes ..... 304
A.3.5 Non-homogeneous Poisson Processes ..... 305
References ..... 309
Index ..... 341# Introduction 

Maintenance involves preventive (planned) and unplanned actions carried out to retain a system at or restore it to an acceptable operating condition. Optimal maintenance policies aim to provide optimum system reliability and safety performance at the lowest possible maintenance costs. Proper maintenance techniques have been emphasized due to increased safety and reliability requirements of systems, increased complexity, and rising costs of material and labor (Sheriff and Smith 1981). For some systems, such as aircraft, submarines, military systems, aerospace systems, it is extremely important to avoid failure during actual operation because it is dangerous and disastrous. One important research area in reliability engineering is the study of various maintenance policies in order to improve system reliability, to prevent the occurrence of system failure, and to reduce maintenance costs (Pham and Wang 1996).

In the past several decades, maintenance, replacement and inspection problems have been extensively studied. The literature in this area is vast, making it impossible to give a short overview of the subject. There are to date many models for reliability, maintenance, replacement and inspection, and recent research has attempted to unify some of them. McCall (1963), Barlow and Proschan (1965), Pieskalla and Voelker (1976), Osaki and Nakagawa (1976), Sherif and Smith (1981), Jardine and Buzacott (1985), Valdez-Flores and Feldman (1989), Cho and Parlar (1991), Jensen (1995), Dekker (1996), Pham and Wang (1996), Dekker et al. (1997), and Wang (2002) survey and summarize the research and practice in this area in different ways. As modern systems grow in complexity, so do reliability and maintenance challenges. This book aims to present recent research on theories and methods in reliability and optimal maintenance in a realistic way, and the focus is on the emerging areas: imperfect maintenance, dependence, correlates failure and repair. A general introduction to each of them will be given in the following subsections.

Most equipment offers some level of warranty to gain some advantages in the highly competitive markets. The warranty assures the buyer that a faulty item will either be repaired or replaced at no cost or at reduced cost. Some buyers may infer that a product with a relatively long warranty period is a more reliable and longerlasting product than one with a shorter warranty period. Warranty cost could be asignificant percentage of overall product cost. So far, many warranty cost models and polices have been proposed and practiced as summarized in Brennan (1994), Blischke and Murthy (1994, 1996), Sahin and Polatogu (1998), and Bai and Pham (2006b). A simple but relatively complete taxonomy of warranty policies can be found in Blischke and Murthy (1993), and Bai and Pham (2006b). Today maintenance may be considered during warranty, and both consumers and manufacturers may benefit from proper maintenance during warranty. In addition, economic dependence may exist in some multi-component systems and maintenance may be imperfect. These issues in warranty research will be further stated in Section 1.3.

Many modern systems contain both hardware and software, and software problems may account for half of system failures for some systems such as telecommunication systems. Software reliability, testing and maintenance have received much attention in recent years, and some significant work is summarized in Musa et al. (1987), Lyu (1996), and Pham (2000). In addition to hardware reliability and maintenance, reliability and optimal testing and debugging for software will also be discussed in this book.

To obtain the optimal maintenance policy for a complex system, we may first need to determine system reliability, availability, or MTBF. However, there are some difficulties in evaluating complex large-scale system reliability and availability using classical statistics: for example, the system reliability structure may be complicated, or subsystems may follow different failure distributions. In this book, Monte Carlo reliability, availability and MTBF simulation algorithms will be discussed together with variance reduction methods, simulation errors, etc.

# 1.1 Imperfect Maintenance 

Maintenance can be classified by two major categories: corrective and preventive. Corrective maintenance (CM) is the maintenance that occurs when the system fails. Some researchers refer to CM as repair and we will use them alternatively throughout this study. According to MIL-STD-721B, CM means all actions performed as a result of failure, to restore an item to a specified condition. Obviously, CM is performed at unpredictable time points because an item's failure time is not known. CM is typically carried out in three steps: (1) Diagnosis of the problem, (2) Repair and/or replacement of faulty component(s), and (3) Verification of the repair action. Preventive maintenance (PM) is the maintenance that occurs when the system is operating. According to MIL-STD-721B, PM means all actions performed in an attempt to retain an item in specified condition by providing systematic inspection, detection, and prevention of incipient failures. Maintenance can also be classified according to the degree to which the operating condition of an item is restored by maintenance in the following way:
a) Perfect repair or perfect maintenance: maintenance actions which restore a system operating condition to 'as good as new'. That is, upon a perfect maintenance, a system has the same lifetime distribution and failure rate function as a new one. Complete overhaul of an engine with a broken connecting rod is anexample of perfect repair. Generally, replacement of a failed system by a new one is a perfect repair.
b) Minimal repair ${ }^{1}$ or minimal maintenance: maintenance actions which restore a system to the same failure rate as it had when it failed. Minimal repair was first studied by Barlow and Hunter (1960). The system operating state after the minimal repair is often called 'as bad as old' in the literature. Changing a flat tire on a car is an example of minimal repair because the overall failure rate of the car is essentially unchanged. The mathematical definition of minimal repair is given in the Appendix to Chapter 4.
c) Imperfect repair or imperfect maintenance: maintenance actions which make a system not 'as good as new' but younger. Usually, it is assumed that imperfect maintenance restores the system operating state to somewhere between 'as good as new' and 'as bad as old'. Clearly, imperfect repair (maintenance) is a general repair (maintenance) which can include two extreme cases: minimal and perfect repair (maintenance). Engine tune-up is an example of imperfect maintenance. Chapter 2 will discuss imperfect maintenance in detail.
d) Worse repair or worse maintenance: maintenance actions which undeliberately make the system failure rate or actual age increase but the system does not break down. Thus, upon worse repair a system's operating condition becomes worse than that just prior to its failure.
e) Worst repair or worst maintenance: maintenance actions which undeliberately make the system fail or break down.

According to the above classification, we can say that a PM is a minimal, perfect, imperfect, worst or worse one. Similarly, a CM could be a minimal, perfect, imperfect, worst or worse CM. We will refer to imperfect CM and PM as imperfect maintenance later. The type and degree of maintenance used in practice depend on types of systems, their costs as well as reliability and safety requirements.

In the previous literature, most studies assume that the system after CM or PM is 'as good as new' (perfect maintenance) or 'as bad as old' (minimal maintenance). In practice, the perfect maintenance assumption may be plausible for systems with one component which is structurally simple. On the other hand, the minimal repair assumption seems reasonable for failure behavior of systems when one of its many, non-dominating components is replaced by a new one (Kijima 1989). However, many maintenance activities may not result in these two extreme situations but in a complicated intermediate one. For example, an engine may not be 'as good as new' or 'as bad as old' after tune-up, a type of PM. It usually becomes "younger" than at the time just prior to PM and enters some state between 'as good as new' and 'as bad as old'. Therefore, perfect maintenance and minimal maintenance are not practical in many actual instances and realistic imperfect maintenance should be modeled. In recent years, imperfect CM and PM have received more attention in reliability and maintenance literature. In fact, we can say

[^0]
[^0]:    ${ }^{1}$ Here we refer to physical minimal repair instead of statistical (black box) minimal repair; see Natvig (1990).that imperfect maintenance study indicates a significant breakthrough in reliability and maintenance theory.

Helvik (1980) believes that imperfectness of maintenance is related to the skill of the maintenance personnel, the quality of the maintenance procedure, and the maintainability of the system. Obviously, maintenance expenditure and reliability requirements also have important effects on imperfectness of maintenance.

Brown and Proschan (1982) state some possible causes for imperfect, worse or worst maintenance due to the maintenance performer:

- Repairing the wrong part
- Only partially repairing the faulty part
- Repairing (partially or completely) the faulty part but damaging adjacent parts
- Incorrectly assessing the condition of the unit inspected
- Performing the maintenance action not when called for but at his / her convenience (the timing for maintenance is off the schedule)

Nakagawa (1987) suggests three reasons causing worse or worst maintenance:

- Hidden faults and failures which are not detected during maintenance
- Human errors such as wrong adjustments and further damage done during maintenance
- Replacement with faulty parts.

According to Brown and Proschan (1982), maintenance policies based on planned inspections are "periodic inspection", and "inspection interval dependent on age". By periodic inspections, a failed unit is identified (e.g., spare battery, a fire detection device, etc.), or it is determined whether the unit is functioning or not. With aging of the unit, the inspection interval may be shortened. These inspection methods are subject to imperfect maintenance caused by randomness in the actual time of inspection in spite of the schedule, imperfect inspection, and cost structure. Therefore, realistic and valid maintenance models must incorporate random features of the inspection policy.

So far, only a small portion of literature concerning the stochastic behavior of repairable systems and their maintenance has considered imperfect maintenance, and most work on imperfect maintenance has been limited to the one-unit system. Kay (1976), and Chan and Downs (1978) have studied the worst PM; Nakagawa (1987) has investigated worst and worse CM and PM. In this book, imperfect maintenance will be one of the major concerns, especially for multi-unit systems.

# 1.2 Dependence 

In recent years, there has existed an increasing interest in multicomponent maintenance models. Schouten (1996) states a good reason: the fact that the vast majority of the maintenance models were concerned with a single piece of equipment operating at a fixed environment was considered as an intrinsic barrier for applications.Maintenance of a multicomponent system differs from that of a single-unit system because there exists dependence in multicomponent systems. One kind of dependence is the economic dependence. For example, due to economic dependence, PM to non-failed subsystems can be performed at a reduced additional cost while failed subsystems are being repaired. Another kind of dependence is failure dependence, or correlated failures. For example, the failure of one subsystem may affect one or more of the other functioning subsystems, and times to failures of different units are then statistically dependent (Nakagawa and Murthy 1993).

Economic dependency is common in most continuous operating systems. Examples of such systems include aircraft, ship, power plants, telecommunication systems, chemical processing facilities, and mass production lines. For this type of system, the cost of system unavailability (one-time shut-down) may be much higher than component maintenance costs. Therefore, there is often great potential cost savings by implementing an opportunistic maintenance policy (Huang and Okogbaa 1996).

Obviously, the joint maintenance of two or more subsystems tends to spend less cost and less time (economic dependency), and the failures of different subsystems in multicomponent system may not be independent (failure dependency). Thus, each subsystem may not be considered as a single-unit system individually and to apply the existing optimum maintenance models of a single-unit system to each of such subsystems may not lead to a global optimal maintenance policy for the system as a whole.

Imperfect maintenance also exists in the repairable multicomponent system. For example, an aircraft consists of many subsystems which are repairable. If one of its subsystems fails, it can be repaired by replacing some of its parts. Clearly, reliability measures of the repaired subsystem are improved after repair but it might not be as good as new (imperfect CM), and consequently the entire system will no longer function as well as a new one. On the other hand, some subsystems in this example may become worse or break down after repair, and accordingly the whole aircraft system may work worse or break down, that results in worse or worst maintenance.

Realistic imperfect maintenance associated with individual subsystems and, accordingly, systems should be modeled. According to Valdez-Flores and Feldman (1989), "Systems used in the production of goods and delivery of services constitute the vast majority of most industry's capital. These systems are subject to deterioration with usage and age. System deterioration is often reflected in higher production costs and lower product quality. To keep production costs down while maintaining good quality, PM is often performed on such deteriorating systems". Obviously, this kind of system is often composed of many subsystems whose maintenance is often imperfect or sometimes even worse. It is necessary to point out that considering the entire system as a single unit and applying a minimal repair model to it may not be plausible for large-scale systems, such as the above two systems. Such maintenance modeling may also be too rough for complex systems since economic and failure dependencies may exist. Besides, individual maintenance procedures are often scheduled for individual subsystems.In practice, some subsystems are inspected and tested separately, and their reliability performances are also evaluated individually. Especially, lifetime distributions of all new subsystems may be known through reliability tests and statistical inference before they are put into field use for some systems. Thus, we can evaluate reliability measures and system maintenance costs for the whole system based on failure information, maintenance costs, and maintenance degrees of all subsystems. Therefore, we may say that a realistic method is to treat a system as one with many subsystems which are subject to imperfect maintenance respectively, economic dependence, and failure dependence; to model imperfect maintenance of the system through modeling imperfect maintenance of all subsystems and at the same time to model economic and failure dependence in the system in order to obtain global optimum maintenance policies for the system.

In summary, it would be realistic to consider both imperfect maintenance and dependence among subsystems when studying reliability measurements, maintenance costs and optimum PM policy of multicomponent systems. Economic dependence, in addition to imperfect maintenance, will be another major factor of interest in this book.

In the maintenance literature, a basic assumption tends to be the independence of the time to failure and time to repair. In practice, the repair time of a unit may depend on its time to failure, that is, time to failure and time to repair are not independent. Goel (1989) states that it is a common experience of system engineers that, in most systems, an early failure leads to a short repair time and vice versa. He uses the bivariate exponential distribution to model this class of dependencies. Later we will refer to this dependence as correlated failures and repairs, i.e., time to failure and time to repair are correlated.

This class of dependencies differs from the failure dependence mentioned in Section 1.2: correlated failures and repairs indicate the dependence between the time to failure and time to repair of a unit but the failure dependence or the correlated failures indicates the dependence between the time to failure of one subsystem and that of other subsystems. Correlated failure and repair may exist in either a single-unit system or a multicomponent system but failure dependence can only exist in a multicomponent system.

It is worthwhile to mention that "dependence" will be a general term in this book and can mean every kind of dependency: economic dependence, failure dependence, or dependence of failure and repair time, i.e., correlated failures and repairs.

# 1.3 Warranty, Dependence, Imperfect Maintenance 

A traditional way to model warranty cost of multi-component systems is the blackbox approach that does not utilize the information of system structure. In fact, system architecture information is very important in modeling warranty cost since economic dependence may be present. Chapter 10 will discuss the importance of system structure information for four types of systems: series, parallel, seriesparallel and parallel-series.The majority of warranty cost models for repairable products assume perfect repair or minimal repair. As pointed out in Section 1.1, imperfect repair is more realistic. Chapter 10 will discuss warranty cost modeling given repair is imperfect.

Maintenance may be incorporated in the warranty period. For example, if a warranted product failed, the failed component(s) or subsystem(s) that cause the system failure will be replaced; in addition, a PM action could be carried out to reduce the chance of future failure. Both consumers and manufacturers will benefit from this policy. Therefore, warranty policies with integrated PM actions may become more and more attractive. Note that PM could also be imperfect in practice if it is performed.

One of the primary questions to be answered in warranty analysis is how much a warranty program will cost. Due to the random nature of warranty cost, most warranty cost models would prefer to use the expected warranty cost (EWC) as the answer. In contrast to the EWC, the expected value of discounted warranty cost (DWC), which incorporates the value of time, may provide a better cost measure for warranties. This is because in general warranty cost can be treated as a random cash flow in the future. Warranty issuers do not have to spend all the money at the stage of the warranty planning. Instead, they can allocate it over the life cycle of warranted products. Another reason that one should consider the value of time is that for the purpose of determining warranty reserve, a fund can be set up specifically to meet future warranty claims. This book will mainly use DWC as warranty cost measures.

# 1.4 Criteria on Maintenance Optimization 

The usual criteria on optimization of maintenance policies are based on maintenance cost measures only: expected maintenance costs per unit of time, total discounted costs, gain, etc. Hence, the optimal maintenance policies are the ones that minimize (maximize) a given cost (gain) criterion (Jensen 1996). A small portion of maintenance models has used reliability measures: availability, average up time, or average down time in optimization criteria. This book will consider both system maintenance cost measures and reliability measures to obtain global optimal maintenance policies. Section 1.5 will further explain this while Chapter 5 will demonstrate the necessity of considering system maintenance cost measures and reliability measures together through numerical examples.

### 1.5 Scope of this Book

### 1.5.1 General Methodologies

Repairable systems whose subsystems are subject to imperfect maintenance, economic dependence, correlated failure and repair, and failure dependence may be realistic in many applications, according to the previous sections. Therefore, for such systems a study of system reliability measures: availability, mean time between system failures (MTBSF), mean time between system repairs (MTBSR),of system maintenance cost measures, and of optimum PM policies would be necessary. The objectives of the book are to study the stochastic behavior of repairable multicomponent systems whose components are subject to imperfect maintenance, economic dependence, correlated failure and repair, and failure dependence, and to investigate the optimal system maintenance policies. In this book, to study the stochastic behavior of systems means mainly to:
a) Formulate and derive the system reliability measures: availability, MTBSF and MTBSR, etc.
b) Model and derive system maintenance cost per unit time, or cost rate.
c) Model and derive system warranty costs and their variance (for some system structures).

The optimal system maintenance policies mentioned above may be those which:
a) Minimize system maintenance cost rate.
b) Optimize the system reliability measures.
c) Minimize system maintenance cost rate while the system reliability requirements are satisfied.
d) Optimize the system reliability measures when the requirements for the system maintenance cost are satisfied.

Similarly, for software systems, we will first formulate and model their reliability and testing cost, and then discuss the optimal software testing policy which may:
a) Minimize software testing cost.
b) Optimize the software reliability measures.
c) Minimize software testing cost while the software reliability requirements are satisfied.
d) Optimize the software reliability measures when the requirements for the software testing cost are satisfied.

# 1.5.2 Directions 

This book aims to discuss the stochastic behavior and optimal maintenance policies for typical reliability system architectures: single-unit systems, series systems, parallel systems, and $k$-out-of- $n$ systems.

There exist many maintenance policies for one-unit hardware systems. This book uses the following practical maintenance policies for each subsystem or the entire system when applicable:
a) Age-dependent PM policy. We consider the situation in which either CM or PM or both are imperfect.
b) Periodic PM policy. We consider the cases of imperfect or perfect PMs, and minimal or imperfect CM at failures between PMs.
c) $T-N$ policy. A subsystem is subject to (imperfect) PM $T$ where $T$ is a nonzero constant, or at the $N^{\text {th }}$ failure ( $N=1,2,3, \ldots$ ), whichever occursfirst, and undergoes (imperfect) repair at failures between PMs.
d) Repair limit policy.

Other maintenance policies will be formally described in related chapters, where their characteristics are also discussed.

For warranty policies, this book discusses three types of existing warranty policies: free repair warranty (FRPW), free replacement warranty (FRW), and prorata warranty (PRW), and two new warranty policies: renewable full service warranty (RFSW) and repair-limit risk-free warranty (RLRFW).

It is worthwhile to note that for a series system there exist various shut-off rules. For example, while a failed component in a series system is in repair, all other components remain in "suspended animation" (they do not age and do not fail). After the repair is completed, the system is returned to operation. At that instant, the components in "suspended animation" are as good as they were when the system stopped operating. This shut-off rule is used in Barlow and Proschan (1975). Obviously, it is practical and can be applicable in other system architectures. We will refer to it as shut-off rule 1 later. In shut-off rule 2, component $A$ upon failure shuts off component $B$ but not vice versa. The third shut-off rule is that components operate independently, and non-failed components continue to operate regardless of the failed components. Hudes (1979) and Khalil (1985) discuss various shut-off rules and system availability for the series system.


Figure 1.1. Maintenance policy and constituting factors
Figure 1.1 shows various factors which may affect an optimal maintenance policy of a system. An optimal maintenance policy should properly consider /incorporate various maintenance policies, system architectures, shut-off rules, maintenance restoration degrees, correlated failures and repairs, failure dependence, economic dependence, non-negligible maintenance time, etc. This book discusses optimal maintenance policies under various system architectures,maintenance policies, shut-off rules, imperfect maintenance, correlated failures and repairs, and economic dependence given that the planning horizon is infinite. Nonnegligible maintenance time is also considered for some models in this book. It is worthwhile to mention the following points:

1. Because a unit is a building brick for a multicomponent system it is necessary to establish effective and efficient methods for modeling reliability measures and cost rates, and determining optimal maintenance policies for a single-unit system considering proper impact factors. All these methods for a single-unit system will be the basis for the analysis of a multicomponent system. For example, there are various modeling methods for imperfect repair for a singleunit system, and they may also be used to model imperfect repair for a multicomponent systems.
2. Most work in the literature tends to determine optimal maintenance policies through minimizing the system maintenance cost rate. It is important to note that for multicomponent systems, minimizing the system maintenance cost rate may not result in optimal system reliability measures. Sometimes when the maintenance cost rate is minimized the system reliability measures are so low that they are not acceptable in practice. This is because various components in the system may have different maintenance costs and different reliability importance in the system. The details are demonstrated in Chapter 5 through numerical examples. Therefore, to achieve the best operating performance for multicomponent systems we need to consider both maintenance cost and reliability measures simultaneously.
3. The reliability architecture of the system must be considered to obtain optimal system reliability performance. For example, once a subsystem of a series system fails it is necessary to repair it at once. Otherwise, the system will have a longer downtime and worse reliability measures. However, when a subsystem of a parallel system fails, the system will still function even if this subsystem is repaired immediately. In fact, its repair can be delayed until it is time to do PM on the system, considering economic dependence; or repair can begin at a time such that only one subsystem operates and the other subsystems have failed and are awaiting repairs; or at the time that all subsystems fail and thus the system fails, if the system failure during actual operation is not very important.
4. In this book, maintenance cost measures, system reliability measures and optimal maintenance policies for imperfect maintenance will be compared with those for perfect maintenance because perfect maintenance may be a special case of imperfect maintenance, and the stochastic behavior and optimal maintenance policies for the perfect maintenance cases have been studied extensively. The comparisons will be helpful for verifying the results obtained under the imperfect maintenance cases.
5. Throughout this book, maintenance will be a general term and may represent PM or CM. Replacement is a perfect maintenance, preventive or corrective. Repair is an action made at component or system failure and has the same meaning as CM. CM and repair will be used alternatively when there can be no confusion.
6. Throughout this book, the planning horizon is assumed to be infinite.
7. In most existing literature, the maintenance time is assumed to be negligiblefor reliability and maintenance models. This assumption makes availability, MTBF and MTBR modeling impossible or unrealistic. This book will consider maintenance time to obtain realistic system reliability measures whenever possible.

# 1.5.3 Framework 

In this book, Chapter 2 will survey imperfect repair and dependence models in the literature and summarize approaches to model imperfect maintenance and dependence, while Chapter 3 will overview various maintenance policies in the literature and practice, such as age-dependent PM policy, repair limit policy.

Chapter 4 will introduce a new modeling tool for imperfect maintenance: a quasi-renewal process which includes ordinary renewal processes as a special case and discusses imperfect maintenance of one-unit systems by means of the quasi renewal process. Eleven imperfect maintenance models based on the quasi-renewal process are presented in this chapter.

In practice, many systems are series systems or can be simplified into series systems. Chapter 5 will investigate reliability and maintenance cost of a series system with $n$ components and correlated failure and repair, and discuss some related optimal maintenance polices. Some important properties of reliability and maintenance cost of series systems are presented. Imperfect repairs are modeled through increasing and decreasing quasi-renewal processes.

Chapter 6 will discuss the opportunistic maintenance of a system with $(n+1)$ subsystems and economic dependence among them, in which whenever a subsystem fails, its repair is combined with PM of the functioning one having increasing failure rate (IFR) if the former reaches some age. Imperfect repair is assumed and two different imperfect modeling methods are used in this chapter.

In Chapter 7 we will look into a preparedness maintenance policy for a system with $n+1$ subsystems, economic dependency and imperfect maintenance. In this preparedness maintenance policy, the system is placed in storage and is called on to perform a given task only if a specific but unpredictable emergency occurs. Some maintenance actions resulting in optimal system "preparedness for field use" may be taken while the system is in storage.

A $k$-out-of- $n$ system is one of the most important systems in reliability engineering and can include series and parallel systems as special cases. Chapter 8 will presents three new $(\tau, T)$ opportunistic maintenance models for a $k$-out-of$n$ :G system with economic dependency and imperfect maintenance. In these models, minimal repairs are performed on failed components before fixed time $\tau$ - a decision variable, and CM of all failed components is combined with PM of all functioning ones after $\tau$. At time $T$ - another decision variable, PM is performed if the system has not been subject to perfect maintenance before $T$. Applications to aircraft engine maintenance are also discussed in Chapter 8.

Chapter 9 will investigate multi-state degraded systems subject to multiple competing failure processes including two independent degradation processes and random shocks. We first discuss reliability model and then optimal condition-based inspection-maintenance for these systems. The system reliability model can be used not only to determine the reliability of the degraded systems but also to obtainthe states of the systems by calculating the system state probabilities. A quasirenewal process introduced in Chapter 4 is employed to establish the interinspection sequence. The PM thresholds for degradation processes and inspection sequence are the decision variables. An optimization algorithm to minimize the average long-run maintenance cost rate is discussed.

In current highly competitive markets, warranty policies become more and more complex. Chapter 10 will discuss warranty cost models of repairable complex systems from manufacturers' point of view by considering a comprehensive set of warranty cost impact factors, such as warranty policies, system structure, product failure mechanism, warranty service cost, impact of warranty service, value of time, warranty service time, and warranty claim related factors, under three types of existing warranty policies: free repair warranty (FRPW), free replacement warranty (FRW), and pro-rata warranty (PRW), and two new warranty policies: renewable full service warranty (RFSW) and repair-limit risk-free warranty (RLRFW). Imperfect or minimal repair is assumed. Monte Carlo simulation techniques and a new modeling tool: a truncated quasi-renewal process introduced in Chapter 4 will be used. The focus is on multi-component systems.

Chapter 11 will model software reliability and testing costs using the quasirenewal process introduced in Chapter 4, and discusses optimal software testing and release policies. Several software reliability and cost models are presented in which successive error-free times form an increasing quasi-renewal process. It is assumed that the cost of fixing a fault during the software testing phase consists of deterministic and incremental random parts, and increases as the number of faults removed rises. The maximum likelihood estimates of parameters associated with these models are provided. Based on the valuable properties of quasi-renewal processes, the expected software testing and debugging cost, number of remaining faults in the software, and mean error-free time after testing are obtained. Optimum testing policies incorporating both reliability and cost measures are investigated.

To obtain the optimal maintenance policy for a complex system, we may first need to determine system availability or MTBF. Generally there are four major difficulties in evaluating complex large-scale system reliability, availability, and MTBF and their confidence limits using classical statistics: the system reliability structure may be very complicated; subsystems may follow different failure distributions; subsystems may have arbitrary failure and repair distributions for maintained systems; failure data of subsystems are sometimes not sufficient, sample size of life test or field population tends to be small. Therefore, it is difficult and often impossible to obtain $s$-confidence limits of the reliability measurements by classical statistics. It has been proven that Monte Carlo technique combined with Bayes method is a powerful tool to deal with this kind of complex systems. In Chapter 12, some existing Monte Carlo reliability, availability and MTBF simulation algorithms will be analyzed. Variance reduction methods, random variate generation techniques, commercial Monte Carlo reliability softwares, etc., are addressed. The pros, cons, accuracy and computer execution time of Monte Carlo simulation in evaluating reliability, availability and MTBF of a complex network are discussed, and a general Monte Carlo reliability assessment method is presented.# Imperfect Maintenance and Dependence 

Imperfect maintenance and dependence are major concerns of this book, as stated in Chapter 1. This chapter will present a detailed introduction to imperfect maintenance and dependence, and survey typical modeling methods, their characteristics and uses. Imperfect maintenance section of this chapter updates Pham and Wang (1996). Some modeling methods on imperfect maintenance and dependence will be used in the subsequent chapters in this book.

### 2.1 Imperfect Maintenance

Perfect maintenance assumes that the system is "as good as new" following maintenance. However, this assumption may not be true in practice. A more realistic assumption is that, upon maintenance, the system lies in a state somewhere between 'as good as new' and its pre-maintenance condition, i.e., maintenance is imperfect, as mentioned in Chapter 1. Kay (1976), Ingle and Siewiorek (1977), Chaudhuri and Sahu (1977), and Chan and Downs (1978) are pioneers in imperfect maintenance study. Kay (1976) and Chan and Downs (1978) study the worst PM. Ingle and Siewiorek (1977) investigate imperfect maintenance. Chaudhuri and Sahu (1977) mention the concept of imperfect PM. An early work on imperfect repair can also be found in NAPS document No. 03476-A. In fact, NAPS document No. 03476-A plays a significant role in later imperfect maintenance research. Based on this work, other researchers have proposed some imperfect maintenance models.

In the existing imperfect maintenance literature, various methods for modeling imperfect maintenance have been used and most of them are on single-unit systems. It is necessary to summarize and compare these modeling methods because it will be helpful for later study in this area, especially for a multicomponent system which is the main concern in this book. It should be pointed out that although the existing literature is mainly on a single-unit system and the modeling methods will be summarized from it, they will also be useful for modeling a multi-component system. This is because individual subsystems can be regarded as single-unit systems, and thus the methods of treating imperfectmaintenance for single-unit systems may also be effective for modeling imperfect maintenance of individual subsystems, based on which imperfect maintenance of a system will be investigated, possibly together with dependence (Pham and Wang 1996).

Methods for modeling imperfect, worse and worst maintenance can be classified into seven categories. Pham and Wang (1996) summarize these methods from related papers and technical reports throughout the literature, and these seven methods and some important results for them are presented next.

# 2.1.1 Modeling Methods for Imperfect Maintenance 

### 2.1.1.1 Modeling Method 1 - $(p, q)$ Rule

Nakagawa (1979) models imperfect PM in this way: after PM a unit is returned to the 'as good as new' state (perfect PM) with probability $p$ and returned to the 'as bad as old' state (minimal PM) with probability $q=1-p$. Clearly, if $p=1$ the PM coincides with perfect one and if $p=0$ it corresponds to minimal PM. So in this sense, minimal and perfect maintenances are special cases of imperfect maintenance and imperfect maintenance is a general maintenance. Using such a study method for imperfect maintenance and assuming that PM is imperfect, Nakagawa $(1979,1980)$ succeeds in obtaining optimum PM policies minimizing the $s$-expected maintenance cost rate for one-unit system under age-dependent and periodic PM policies, respectively.

Similar to Nakagawa (1979a,b), Helvic (1980) states that, while the faulttolerant system is usually renewed after PM with probability $\theta_{2}$, its operating condition sometimes remains unchanged (as bad as old) with probability $\theta_{1}$ where $\theta_{1}+\theta_{2}=1$

Brown and Proschan (1983) study the following model of the imperfect repair process. A unit is repaired each time it fails. The executed repair is either a perfect one with probability $p$ or a minimal one with probability $1-p$. Assuming that all repair actions take negligible time, they establish ageing preservation properties of this imperfect repair model and monotonicity of various parameters and random variables associated with the failure process. They obtain an important, useful result: if the life distribution of a unit is $F$ and its failure rate is $r$, then the distribution function of the time between successive perfect repairs is $F_{p}=1-(1-F)^{p}$ and the corresponding failure rate $r_{p}=p r$. Using this result, Fontenot and Proschan (1984), and Wang and Pham (1996b) obtain optimal imperfect maintenance policies for one-component system.

Later on, we will refer to this method for modeling imperfect maintenance as the $(p, q)$ rule, that is, after maintenance (corrective or preventive) a system becomes "as good as new" with probability $p$ and "as bad as old" with probability $1-p$. In fact, this modeling method is getting popular: more and more imperfect maintenance models have used this rule in recent years.

Bhattacharjee (1987) obtains the same results as Brown and Proschan (1983), and some new results for Brown-Proschan model of imperfect repair via a shockmodel representation of the sojourn time.
Lim et al. (1998) extend the Brown and Proschan (1983) imperfect repair model, and propose a new Bayesian imperfect repair model where the probability of perfect repair, $P$, is considered to be a random variable. Assuming that $P$ has a prior distribution $\mathrm{II}(p)$, they obtain the distribution of waiting times between two successive perfect repairs and its corresponding failure rate. Lim et al. (1998) discuss the posterior distribution of $P$ and its estimators, and study some preservation properties for certain nonparametric classes of life distributions and the monotonicity properties for several parameters. Cha and Kim (2001) model Bayesian availability where $P$ is not fixed but a random variable with a prior distribution.

Li and Shaked (2003) equip the Brown and Proschan (1983) imperfect repair model with PM, and obtain stochastic maintenance comparisons for the numbers of failures under different policies via a point-process approach. They also obtain some results involving stochastic monotonicity properties of these models with respect to the unplanned complete repair probability.

# 2.1.1.2 Modeling Method $2-(p(t), q(t))$ Rule 

Block et al. (1985) extend the above Brown-Proschan imperfect repair model with the $(p, q)$ rule to the age-dependent imperfect repair for one-unit system: an item is repaired at failure (corrective maintenance). With probability $p(t)$, the repair is a perfect repair; with probability $q(t)=1-p(t)$, the repair is a minimal one, where $t$ is the age of the item in use (the time since the last perfect repair). Block et al. (1985) prove that if the item's life distribution $F$ is a continuous function and its failure rate is $r$, the successive perfect repair times form a renewal process with interarrival time distribution

$$
F_{p}=1-\exp \left\{\int_{0}^{t} p(x)[1-F(x)]^{-1} F(d x)\right\}
$$

and the corresponding failure rate $r_{p}(t)=p(t) r(t)$. In fact, similar results can be found in Beichelt and Fischer (1980), and NAPS Document No. 03476-A. Block et al. (1985) prove that the ageing preservation results of Brown and Proschan (1983) hold under suitable hypotheses on $p(t)$. Later on, we will call this imperfect maintenance modeling method as the $(p(t), q(t))$ rule.

Using this $(p(t), q(t))$ rule, Block et al. (1988) investigate a general agedependent PM policy, where an operating unit is replaced when it reaches age $T$; if it fails at age $y<T$, it is either replaced by a new unit with probability $p(t)$, or it undergoes minimal repair with probability $q(t)=1-p(t)$. The cost of the $i^{\text {th }}$ minimal repair is a function, $c_{i}(y)$, of age $y$ and number of repairs. After a perfect maintenance, planned or unplanned (preventive), the procedure is repeated.

Both Brown and Proschan (1983) model and Block et al. (1985) model assume that the repair time is negligible. It is worthwhile to mention that Iyer (1992) obtains availability results for imperfect repair using the $(p(t), q(t))$ rule given thatthe repair time is not negligible. His realistic treatment method will be helpful for later research.

Sumita and Shanthikumar (1988) propose and study an age-dependent counting process generated from a renewal process and apply that counting process to the age-dependent imperfect repair for the one-unit system.

Whitaker and Samaniego (1989) propose an estimator for the life distribution when the above model by Block et al. (1985) is observed until the time of the $m^{\text {th }}$ perfect repair. This estimator was motivated by a nonparametric maximum likelihood approach, and was shown to be a 'neighborhood MLE'. They derive large-sample results for this estimator. Hollander et al. (1992) take the more modern approach of using counting process and martingale theory to analyze these models. Their methods yield extensions of Whitaker and Samaniego's results to the whole line and provide a useful framework for further work on the minimal repair model.

The $(p, q)$ rule and $(p(t), q(t))$ rule for imperfect maintenance seem practical and realistic. It makes imperfect maintenance be somewhere between perfect and minimal ones. The degree to which the operating conditions of an item is restored by maintenance can be measured by $p$ or $p(t)$. Especially, in the $(p(t), q(t))$ rule, the degree to which the operating condition of an item is restored by maintenance is related to its age $t$. Thus, the $(p(t), q(t))$ rule seems more realistic but mathematical modeling of imperfect maintenance by using it will be more complicated. The two rules can be expected to be powerful in future imperfect maintenance modeling. In fact, both rules have received much attention and have been used in some imperfect repair models, as shown in the subsequent chapters.

Makis and Jardine (1992) consider a general treatment method for imperfect maintenance and model imperfect repair at failure in a way that repair returns a system to the "as good as new" state with probability $p(n, t)$ or to the "as bad as old" state with probability $q(n, t)$, or with probability $s(n, t)=1-p(n, t)-q(n, t)$ the repair is unsuccessful, the system is scrapped and replaced by a new one, where $t$ is the age of the system and $n$ is the number of failures since replacement. We will refer to this treatment method as $(p(n, t), q(n, t), s(n, t))$ rule later.

# 2.1.1.3 Modeling Method 3 - Improvement Factor Method 

Malik (1979) introduces the concept of improvement factor in the maintenance scheduling problem. He believes that maintenance changes the system time of the failure rate curve to some newer time but not all the way to zero (not new), as shown in Figure 2.1 This treatment method for imperfect maintenance also makes the failure rate after PM lie between 'as good as new' and 'as bad as old'. The degree of improvement in failure rate is called improvement factor. Malik (1979) assumes that since systems need more frequent maintenance with increased age the successive PM intervals are decreasing in order to keep the system failure rate at or below a stated level (sequential PM policy), and proposes an algorithm to determine these successive PM intervals. Lie and Chun (1986) present a general expression to determine these PM intervals. Malik (1979) relies on an expert judgment to estimate the improvement factor, while Lie and Chun (1986) give a set

Figure 2.1. Minimal, perfect, imperfect repair vs. failure rate changes
of curves as a function of maintenance cost and the age of the system for the improvement factor.

Using the improvement factor and assuming finite planning horizon, Jayabalan and Chaudhuri (1992b) introduce a branching algorithm to minimize the average total cost for a maintenance scheduling model with assured reliability and they (1992c) discuss optimal maintenance policy for a system with increased mean down time and assured failure rate. It is worthwhile to note that using fuzzy set theory and improvement factor, Suresh and Chaudhuri (1994) establish a PM scheduling procedure to assure an acceptable reliability level or tolerable failure rate assuming finite planning horizon. They regard the starting condition, ending condition, operating condition, and type of maintenance of a system as fuzzy sets. Improvement factor is used to find out the starting condition of the system after maintenance.

Chan and Shaw (1993) think that failure rate is reduced after each PM and this reduction of failure rate depends on the item age and the number of PMs. Chan and Shaw propose two types of failure-rate reduction: (1) failure-rate with fixed reduction. After each PM, the failure rate is reduced such that all jump-downs of the failure rate are the same; (2) failure rate with proportional reduction. After PM, the failure rate is reduced such that each jump-down is proportional to the current failure rate. They obtain cycle-availability for single unit system and discuss the design scheme to maximize the probability of achieving a specified stochasticcycle availability with respect to the duration of the operating interval between PMs .

In Doyen and Gaudoin (2004), the (conditional) failure intensity before the first repair is a continuous function of time. The repair effect is characterized by the change induced on the failure intensity before and after failure. Repair effect is expressed by a reduction of failure intensity. Several cases are studied, which take into account the possibility of a Markovian memory property.This kind of study method for imperfect maintenance is in terms of failure rate and seems useful and practical in engineering where it can be used as a general treatment method for imperfect maintenance or even worse maintenance. Later on we call this treatment method Improvement Factor Method.

Besides, Canfield (1986) assumes that PM at time $t$ restores the failure rate function to its shape at $t-\tau$, while the level remains unchanged where $\tau$ is less than or equal to the PM intervention interval.

# 2.1.1.4 Modeling Method 4 - Virtual Age Method 

Kijima et al. (1988) develop an imperfect repair model by using the idea of the virtual age process of a repairable system. If the system has the virtual age $V_{n-1}=y$ immediately after the $(n-1)^{\text {th }}$ repair, the $n^{\text {th }}$ failure-time $X_{n}$ is assumed to have the distribution function

$$
\operatorname{Pr}\left\{X_{n} \leq x \mid V_{n-1}=y\right\}=\frac{F(x+y)-F(y)}{1-F(y)}
$$

where $F(x)$ is the distribution function of the time to failure of a new system. Let $a$ be the degree of the $n^{\text {th }}$ repair where $0 \leq a \leq 1$. They construct such a repair model: the $n^{\text {th }}$ repair cannot remove the damage incurred before the $(n-1)^{\text {th }}$ repair. It reduces the additional age $X_{n}$ to $a X_{n}$. Accordingly, the virtual age after the $n^{\text {th }}$ repair becomes:

$$
V_{n}=V_{n-1}+a X_{n}
$$

Obviously, $a=0$ corresponds to a perfect repair while $a=1$ to a minimal repair. Later Kijima (1989) extends the above model to the case that $a$ is a random variable taking a value between 0 and 1 and proposes another imperfect repair model:

$$
V_{n}=A_{n}\left(V_{n-1}+X_{n}\right)
$$

where $A_{n}$ is a random variable taking a value between 0 and 1 for $n=1,2,3, \ldots$ For the extreme values 0 and $1, A_{n}=1$ means a minimal repair and $A_{n}=0$ a perfect repair. Comparing this treatment method with Brown and Proschan's, we can see that if $A_{n}$ is independently and identically distributed (i.i.d.) taking the two extreme values 0 and 1 they are the same. Therefore, the second treatment method by Kijima (1989) is general. He derives various monotonicity properties associated with the above two models.

In Doyen and Gaudoin (2004), repair effect is expressed by a reduction of the system virtual age. Several cases are studied, which take into account the possibility of a Markovian memory property.

This treatment method will be referred to as the Virtual Age Method later on.
It is worth mentioning that Uematsu and Nishida (1987) consider a more general model including the above two models by Kijima (1989) as special cases and obtain some elementary properties of the associated failure process. Let $T_{n}$denote the time interval between the $(n-1)^{\text {th }}$ failure and the $n^{\text {th }}$ one, and $X_{n}$ denote the degree of repair. After performing the $n^{\text {th }}$ repair, the age of the system becomes $q\left(t_{1}, \ldots, t_{n} ; x_{1}, \ldots x_{n}\right)$ given that $T_{i}=t_{i}$ and $X_{i}=x_{i} \quad(i=1,2, \ldots n)$ where $T_{i}$ and $X_{i}$ are random variables. On the other hand, $q\left(t_{1}, \ldots, t_{n} ; x_{1}, \ldots x_{n-1}\right)$ represents the age of the system as just before the $n^{\text {th }}$ failure. The starting epoch of an interval is subject to the influence of all previous failure history, i.e., the $n^{\text {th }}$ interval is statistically dependent on $T_{1}=t_{1}, \ldots, T_{n-1}=t_{n-1}, \quad X_{1}=x_{1}, \ldots, \quad T_{n-1}=t_{n-1}$. For example, if $q\left(t_{1}, \ldots, t_{n} ; x_{1}, \ldots x_{n}\right)=\sum_{j=1}^{n} \sum_{i=j}^{n} x_{i} t_{j}$, then $X_{i}=0\left(X_{i}=1\right)$ represents that perfect repair (minimal repair) performs at the $i^{\text {th }}$ failure.

# 2.1.1.5 Modeling Method 5 - Shock Model 

It is well-known that the time to failure of a unit can be represented as a first passage time to a threshold for an appropriate stochastic process that describes the levels of damage. Consider a unit which is subject to shocks occurring randomly in time. At time $t=0$, the damage level of the unit is assumed to be 0 . Upon occurrence of a shock, the unit suffers a non-negative random damage. Each damage, at the time of its occurrence, adds to the current damage level of the unit, and between shocks, the damage level stays constant. The unit fails when its accumulated damage first exceeds a specified level. To keep the unit in an acceptable operating condition, some PM is performed (Kijima and Nakagawa 1991).

Kijima and Nakagawa (1991) propose a cumulative damage shock model with imperfect periodic PM. The PM is imperfect in the sense that each PM reduces the damage level by $100(1-b) \%, 0 \leq b \leq 1$, of total damage. Note that if $b=1$ the PM is minimal and if $b=0$ the PM coincides with a perfect PM. This research approach is similar to the one in treatment method 1. They derive a sufficient condition for the time to failure to have an IFR distribution and discuss the problem of finding the number of PMs that minimizes the expected maintenance cost rate.

Kijima and Nakagawa (1992) establish a cumulative damage shock model with a sequential PM policy assuming that PM is imperfect. They model imperfect PM in a way that the amount of damage after the $k^{\text {th }} \mathrm{PM}$ becomes $b_{k} Y_{k}$ when it was $Y_{k}$ before PM, i.e., the $k^{\text {th }} \mathrm{PM}$ reduces the amount $Y_{k}$ of damage to $b_{k} Y_{k}$ where $b_{k}$ is called the improvement factor. They assume that a system is subject to shocks occurring according to a Poisson Process and, upon occurrence of shocks, it suffers a non-negative random damage which is additive. Each shock causes a system failure with probability $p(z)$ when the total damage is $z$ at the shock. In this model, PM is done at fixed intervals $x_{k}$ for $k=1,2,3, \ldots, N$ because more frequent maintenance is needed with age, and the $N^{\text {th }} \mathrm{PM}$ is perfect. If the system fails between PMs it undergoes only minimal repair. They derive the expected maintenance cost rate until replacement assuming that $p(z)$ is an exponential function and damage is independently and identically distributed and discuss the optimal replacement policies.Finkelstein (1997) investigates the performance of a repairable system subject to shocks: each shock with a probability that depends on a virtual age of the effected system causes a breakdown that ends the process of system functioning. In Finkelstein (1997), various models of repair, ranging from minimal till perfect repair are studied. It is assumed that shocks occur according to the nonhomogeneous Poisson process or a renewal process with identically distributed cycles. The probability of a system functioning without breakdowns for the mentioned models is derived.

This study approach for imperfect maintenance will be called Shock Model later in this book.

# 2.1.1.6 Modeling Method 6 - Quasi-renewal Process 

Wang and Pham (1996b) treat imperfect repair in a way that, upon each repair, the lifetime of a system will be reduced to a fraction $\alpha$ of its immediately previous one where $0<\alpha<1$ and all lifetimes are independent, i.e., the lifetime decreases with the number of repairs. In Wang and Pham (1996b), the successive lifetimes are defined to constitute a decreasing quasi-renewal process, whose details are given in Chapter 4. Assuming that the $p d f$ of the lifetime of a system which has been subject to $(n-1)$ repairs, $X_{n}$, is $f_{n}(x)$ for $n=1,2,3, \ldots$, Wang and Pham (1996b) study this quasi-renewal process and prove that:
a. If $f_{1}(x)$ belongs to IFR, DFR, IFRA, DFRA, and NBU (for definitions see Chapter 4 Appendix), then $f_{n}(x)$ is in the same category, $\forall n, n=2,3, \ldots$.
b. The shape parameter of $X_{n}$ are the same for $n=1,2,3, \ldots$ for a quasirenewal process if $X_{1}$ follows the Gamma, Weibull or Lognormal distribution.

The second result means that after "renewal" the shape parameters of the interarrival time will not change. In reliability theory, the shape parameters of a lifetime of an item tend to relate to its failure mechanism. Usually, if a product possesses the same failure mechanism then its lifetimes will have the same shape parameters at different application conditions. Because most maintenance does not change the failure mechanism we can expect that the lifetime of a system will have the same shape parameters. Thus, in this sense, the quasi-renewal process will be plausible to model the imperfect maintenance process.

Wang and Pham (1996c) further assume that repair time is non-negligible, not as in most imperfect maintenance models, and upon repair the next repair time becomes a multiple $\beta$ of its current one where $\beta>1$ and all repair times are independent, i.e., the time to repair increases with the number of repairs. In Wang and Pham (1996b), the successive repair times are defined to form an increasing quasi-renewal process. This method modeling imperfect maintenance will be referred to as the $(\alpha, \beta)$ rule or quasi-renewal process method. Yang and Lin (2005) apply the quasi-renewal process in age and block PM.

In investigating the optimal replacement problem, Lam (1988) uses the fixed life reduction idea after repair, referred to as the geometric process. Lam (1988, 1996) studies the geometric process by means of the ordinary renewal process. InChapter 4, the quasi-renewal process is introduced from defining the quasi-renewal function.

# 2.1.1.7 Modeling Method 7 - Multiple ( $p, q$ ) Rule 

Shaked and Shanthikumar (1986) introduce the multivariate imperfect repair concept. They consider a system whose components have dependent lifetimes and are subject to imperfect repairs respectively until they are replaced. For each component the repair is imperfect according to the $(p, q)$ rule, i.e., at failure the repair is perfect with probability $p$ and minimal with probability $q$. Assume that $n$ components of the system start to function at the same time 0 , and no more than one component can fail at a time. They establish the joint distribution of the times to next failure of the functioning devices after a minimal repair or perfect repair, and derive the joint density of the resulting lifetimes of the components and other probabilistic quantities of interest, from which the distribution of the lifetime of the system can be obtained. Sheu and Griffith (1992) further extend this work. Later we will call this treatment method the multiple $(p, q)$ rule.

### 2.1.1.8 Others

Nakagawa (1979b) models imperfect PM in a way that, in the steady-state, PM reduces the failure rate of an item to a fraction of its value just before PM and during operation of the item the failure rate climbs back up. He believes that the portion by which the failure rate is reduced is a function of some resource consumed in PM and a parameter. That is, after PM the failure rate of the unit becomes $\lambda(t)=g\left(c_{1}, \theta\right) \cdot \lambda(t+T)$ where the fraction reduction of failure rate $g\left(c_{1}, \theta\right)$ lies between 0 and $1, T$ is the time interval length between PMs, $c_{1}$ is the amount of resource consumed in PM, and $\theta$ is a parameter. This treatment method is different from the improvement factor method in that, for improvement factor method, maintenance makes the system younger in terms of its age, i.e., its age becomes younger after maintenance.

Nakagawa $(1986,1988)$ uses two other methods to deal with imperfect PM for two sequential PM policies: (1) The failure rate after PM $k$ becomes $a_{k} h(t)$ given that it was $h(t)$ in the previous period where $a_{k} \geq 1$. That is, the failure rate increases with the number of PMs; (2) The age, after PM $k$, reduces to $b_{k} t$ when it was $t$ before PM where $0 \leq b_{k}<1$. That is, PM reduces the age. Obviously, the second method is similar to the improvement factor method. Besides, in investigating periodic PM models, Nakagawa (1980) treats imperfect PM in that the age of the unit becomes $x$ units of time younger by each PM and further suggests that $x$ is in proportion to the PM cost where $x$ is less than or equal to the PM interval. We will call it the $x$ Rule later.

Nguyen and Murthy (1981) model imperfect PM in a way that, after PM, the unit has a different (worse) failure time distribution than after CM. Yak (1984) assumes that maintenance may result in its failure (the worst maintenance) in modeling the MTTF and the availability of a system.

Some typical work on imperfect maintenance are summarized in Table 2.1 by modeling methods. From this table we can see that the $(p, q)$ rule and $(p(t), q(t))$rule are popular in treating imperfect maintenance. This is partly because these two rules make imperfect maintenance modeling mathematically tractable, as demonstrated in Chapters $6-8$.

Table 2.1. Summary of treatment methods for imperfect maintenance

| Modeling method | References |
| :--: | :--: |
| $(p, q)$ Rule | Chan and Downs (78), Helvic (80), Nakagawa (79, 80, 87), Brown and Proschan (82, 83), Fontenot and Proschan (84), Lie and Chun (86), Yun and Bai (87), Bhattacharjee (87), Rangan and Grace (89), Sheu and Liou (92), Srivastava and Wu (93), Wang and Pham (96a,b,c, 97b), Lim et al. (98), Pham and Wang (00), Cha and Kim (01), Kvam et al. (02), Li and Shaked (03) |
| $(p(t), q(t))$ <br> Rule | Beichelt (80, 81), Block et al. (85, 88), Abdel-Hameed (87a), Whitaker and Samaniego (89), Sheu (91a, 92, 93), Makis and Jardine (91), Iyer (92), Hollander et al. (92), Sheu and Kuo (94), Sheu et al. (95), Wang et al. (01), Wang and Pham $(99,03)$ |
| Improvement factor | Malik (79), Canfield (86), Lie and Chun (86), Jayabalan and Chaudhuri (92a, b,c, 95), Chan and Shaw (93), Suresh and Chaudhuri (94), Doyen and Gaudoin (04) |
| Virtual age | Uematsu and Nishida (87), Kijima (88, 89), Makis and Jardine (93), Liu et al. (95), Gasmi et al. (03), Doyen and Gaudoin (04) |
| Shock model | Bhattacharjee (87), Kijima and Nakagawa (91,92), Sheu and Liou (92c), Finkelstein (97) |
| $(\alpha, \beta)$ Rule or quasi-renewal process | Lam (88, 96), Wang and Pham (96a,b,c, 97b, 99, 06), Pham and Wang (00, 01), Yang and Lin (05), Wu and Clements-Croome (05), Bai and Pham (06a) |
| Multiple $(p, q)$ <br> rule | Shaked and Shanthikumar (86), Sheu and Griffith (92) |
| Others | Nakagawa (79b, 80, 86, 88), Subramanian and Natarajan (80), Nguyen and Murthy (81), Yak (84), Yun and Bai (88), Dias (90), Subramanian and Natarajan (90), Zheng and Fard (91), Jack (91), Chun (92), Dagpunar and Jack (94) |

The following further work on imperfect maintenance is necessary:

- Study optimal maintenance policy for multicomponent systems because previous work on imperfect maintenance was focused on one-unit systems.
- Construct statistical estimation methods for parameters of various imperfect maintenance models.
- Develop more and better methods for treating imperfect maintenance.
- Study more realistic imperfect maintenance models, for example, including non-negligible repair time, finite horizon.
- Use the reliability measures as the optimality criteria for maintenance policies instead of cost rates, or combine both, as stated in Section 1.5.1.# 2.1.2 Typical Imperfect Maintenance Models by Maintenance Policies 

### 2.1.2.1 Age-dependent PM Policy

In the age-dependent PM model, a unit is preventively maintained at predetermined age $T$, or repaired at failure, whichever comes first. For this policy there are various imperfect maintenance models according to the conditions that either or both of PM and CM is imperfect. The research under the age-dependent PM policy and its extensions is summarized in Table 2.2.

Table 2.2. Imperfect maintenance study under age-dependent PM policy

| Study | PM | CM | Treatment <br> method | Optimality <br> criteria | Modeling tool | Planning <br> horizon |
| :-- | :-- | :-- | :--: | :--: | :--: | :--: |
| Chan and <br> Downs (1978) | Imperfect | Perfect | $(p, q)$ rule | Availability <br> cost rate | Semi-Markov | Infinite |
| Nakagawa <br> (1979a) | Imperfect | Perfect | $(p, q)$ rule | Cost rate | Renewal <br> theory | Infinite |
| Beichelt <br> (1980) | Perfect | Imperfect | $(p(t), q(t))$ <br> rule | Cost rate | Renewal <br> theory | Infinite |
| Fontenot and <br> Proschan <br> (1984) | Perfect | Imperfect | $(p, q)$ rule | Cost rate | Renewal <br> theory | Infinite |
| Block et al. <br> (1988) | Perfect | Imperfect | $(p(t), q(t))$ <br> rule | Cost rate <br> total cost | Renewal <br> theory | Infinite <br> finite |
| Rangan and <br> Grace (1989) | Perfect | Imperfect | $(p, q)$ rule | Total cost | Renewal <br> theory | Finite |
| Sheu (1991a) | Perfect | Imperfect | $(p(t), q(t))$ <br> rule | Cost rate <br> (random cost) | Renewal <br> theory | Infinite <br> finite |
| Sheu and Kuo <br> (1993) | Perfect | Imperfect | $(p(t), q(t))$ <br> rule | Cost rate <br> (random cost) | Renewal <br> theory | Infinite |
| Sheu et al. <br> (1995) | Perfect | Imperfect | $(p(t), q(t))$ <br> rule | Cost rate <br> (random cost) | Renewal <br> theory | Infinite |
| Wang and <br> Pham (1996a) | Imperfect | Imperfect | $(p, q)$ rule <br> $(\alpha, \beta)$ rule | Cost rate <br> Availability | Renewal <br> theory | Infinite |

One of the pioneer imperfect maintenance models for the age-dependent PM policy is due to Nakagawa (1979a) and NAPS Document No. 03476-A. Nakagawa (1979a) investigates three age-dependent PM models with imperfect PM and perfect or minimal repair at failure using the $(p, q)$ rule. He derives the expected maintenance cost rate and discusses the optimal maintenance policies in terms of PM time interval $T$.

Using the $(p(t), q(t))$ rule, Block et al. (1988) discuss an age-dependent PM policy where CM is imperfect and the cost of the $i^{\text {th }}$ minimal repair is a function, $c_{i}(y)$, of age and number of repairs. Sheu et al. (1993) generalized the agedependent PM policy where if a system fails at age $y<t$, it is subject to perfect repair with $p(y)$, or undergoes minimal repair with probability $q(y)=1-p(y)$.Otherwise, a system is replaced when the first failure after $t$ occurs or the total operating time reaches age $T(0 \leq t \leq T)$, whichever occurs first. They discussed the optimal policy $\left(t^{*}, T^{*}\right)$ to minimize the expected cost rate. This is a realistic PM model. Sheu et al. (1995) further extend this model. They assume that a system has two types of failures when it fails at age $z$ and is replaced at the $n^{\text {th }}$ type 1 failure or first type 2 failure or at age $T$, whichever occurs first. Type 1 failure occurs with probability $p(z)$ and is corrected by minimal repair. Type 2 failure occurs with probability $q(z)=1-p(z)$ and is corrected by perfect repair (replacement). Using the $(p(t), q(t))$ rule and random minimal repair costs, they derive the expected cost rate and a numerical example is presented.

Table 2.3. Imperfect maintenance study under periodic PM policy

| Study | PM | CM | Treatment <br> method | Optimality <br> criterion | Modeling <br> tool | Planning <br> horizon |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Nakagawa <br> (1979) | Imperfect | Minimal | $(p, q)$ rule | Cost rate | Renewal <br> theory | Infinite |
| Nakagawa <br> (1980) | Imperfect | Perfect <br> minimal | $(p, q)$ rule <br> $x$ rule | Cost rate | Renewal <br> theory | Infinite |
| Beichelt <br> (1981a, b) | Perfect | Imperfect | $p(t), q(t)$ | Cost rate | Renewal <br> theory | Infinite |
| Fontenot and <br> Proschan <br> (1984) | Perfect | Imperfect | $(p, q)$ rule | Cost rate | Renewal <br> theory | Infinite |
| Nakagawa <br> (1986) | Imperfect | Minimal | Different <br> failure rates | Cost rate | Renewal <br> theory | Infinite |
| Abdel- <br> Hameed <br> (1987a) | Perfect | Imperfect | $p(t), q(t)$ | Cost rate | Stochastic <br> process | Infinite |
| Nakagawa <br> and Yasui <br> (1987) | Imperfect | Perfect | $(p, q)$ rule | Availability | Renewal <br> theory | Infinite |
| Kijima et al. <br> (1988) | Perfect | Imperfect | Virtual age | Cost rate | Renewal <br> theory | Infinite |
| Kijima and <br> Nakagawa <br> (1991) | Imperfect | Perfect | Shock model | Cost rate | Renewal <br> theory | Infinite |
| Jack (1991) | Perfect | Imperfect | Others | Total cost | Renewal <br> theory | Finite |
| Chun (1992) | Imperfect | Minimal | $x$ rule | Total cost | Probability | Finite |
| Sheu (1992) | Perfect | Imperfect | $p(t), q(t)$ | Cost rate | Renewal <br> theory | Infinite |
| Liu et al. <br> (1995) | Imperfect | Minimal | Virtual age | Cost rate | Renewal <br> theory | Infinite |
| Wang and <br> Pham (1996c) | Imperfect | Imperfect | $(p, q)$ rule <br> $(\alpha, \beta)$ rule | Cost rate <br> Availability | Quasi- <br> renewal <br> theory | Infinite |
| Wang and <br> Pham (1999) | Imperfect | Imperfect | $p(t), q(t)$ | Cost rate <br> Availability | Renewal <br> theory | Infinite |# 2.1.2.2 Periodic PM Policy 

In the periodic PM policy, a unit is preventively maintained at fixed time intervals and repaired at intervening failures. Liu et al. (1995) investigate an extended periodical PM model using the notation of the virtual age. They assume that a unit receives (imperfect) PM every $T$ time unit, intervening failures are subject to minimal repairs and the unit is replaced every fixed number of PMs. Nakagawa (1986) studies a similar model but he assumes that PM is imperfect in the sense that after PM the failure rate will be changed. The research under the periodic PM policy and its extensions are summarized in Table 2.3.

Table 2.4. Imperfect maintenance study under failure limit policy

| Study | PM | CM | Measure <br> improved | Optimality <br> criterion | Modeling <br> tool | Planning <br> horizon |
| :-- | :-- | :--: | :--: | :--: | :--: | :--: |
| Malik (1979) | Imperfect | None | Reliability | Reliability | Probability | Infinite |
| Canfield <br> (1986) | Imperfect | None | Failure rate | Cost rate | Renewal <br> theory | Infinite |
| Lie and Chun <br> (1986) | Imperfect | Imperfect | Failure rate | Cost rate | Renewal <br> theory | Infinite |
| Jayabalan <br> (1992a) | Imperfect | Minimal | Failure rate | Total cost | Probability | Finite |
| Jayabalan and <br> Chaudhuri <br> (1992c) | Imperfect | Minimal | Age <br> Others | Cost rate | Probability | Infinite |
| Jayabalan and <br> Chaudhuri <br> (1992d) | Imperfect | None | Age | Total cost | Probability | Finite |
| Chan and <br> Shaw (1993) | Imperfect | Perfect | Failure rate | Availability | Probability | Infinite |
| Suresh and <br> Chaudhuri <br> (94) | Imperfect |  | Reliability and <br> failure rate | Total cost | Probability | Finite |
| Jayabalan and <br> Chaudhuri <br> (1995) | Imperfect | Minimal | Age | Total cost | Renewal <br> theory | Finite |
| Monga et al. <br> (1996) | Imperfect | Minimal | Reduction <br> (age and failure <br> rate) | Cost rate | Renewal <br> theory | Infinite |

### 2.1.2.3 Failure Limit Policy

This policy assumes that PM is performed only when the failure rate or reliability of a unit reaches a predetermined level. Malik (1979) derives the PM schedule points so that a unit works at or above the minimum acceptable level of reliability. Lie and Chun (1986) formulate a maintenance cost model where PM is performed whenever the unit reaches the predetermined maximum failure rate. Jayabalan and Chaudhuri (1992a) obtain the optimal maintenance policy for a specific period of time given that downtime for installation and for PM are negligible. In other work, Jayabalan and Chaudhuri (1992b) consider downtime for replacement as a nonzeroconstant. As a unit ages, the successive downtime for PM interventions is expected to consume more time. To incorporate this point, Jayabalan and Chaudhuri (1992b) assume that PM time follows exponential distribution and is increasing with age. Jayabalan and Chaudhuri (1995) present an algorithm to obtain optimal maintenance policies which require less computational time. The research under the failure limit policy and its extensions is summarized in Table 2.4.

# 2.1.2.4 Sequential PM Policy 

When a system is maintained at unequal intervals, the PM policy is known as Sequential PM policy. Nakagawa $(1986,1988)$ discusses a sequential PM policy where PM is done at fixed intervals $x_{k}$ where $x_{k} \leq x_{k-1}$ for $k=2,3 \ldots$ This policy is practical because most units need more frequent maintenance with increased age. This PM policy is different from the failure limit policy in that it controls $x_{k}$ lengths directly but the failure limit policy controls failure rate, age, reliability, etc., directly. In Wu and Clements-Croome (2005), the PM is sequentially executed with $\tau_{n}$ time units after the $(n-1)^{\text {th }} \mathrm{PM}$, where $n=1,2, \ldots$ Between two adjacent PMs, a CM is carried out immediately on failure. Both PM and CM are imperfect. $\tau_{n}$ is dependent on $n$ and determined through minimizing the maintenance cost rate. The research under the sequential PM policy and its extensions is summarized in Table 2.5.

Table 2.5. Sequential PM policy

| Study | PM | CM | Treatment | Optimality <br> criterion | Modeling <br> tool | Planning <br> horizon |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Nakagawa (1986) | Imperfect | Minimal | Different failure <br> rates | Cost rate | Renewal <br> theory | Infinite |
| Nakagawa (1987) | Imperfect | Minimal | Reduction <br> (age and failure <br> rate) | Cost rate | Renewal <br> theory | Infinite |
| Kijima and <br> Nakagawa (1992) | Imperfect | Minimal | Shock model | Cost rate | Renewal <br> theory | Infinite |
| Monga et al. <br> (1996) | Imperfect | Minimal | Reduction <br> (age and failure <br> rate) | Cost rate | Renewal <br> theory | Infinite |
| Wu and <br> Clements-Croome <br> (2005) | Imperfect | Imperfect | $(\alpha, \beta)$ rule | Cost rate | Renewal <br> theory | Infinite |

### 2.1.2.5 Repair Limit Policy

When a unit fails, the repair cost is estimated and repair is undertaken if the estimated cost is less than a predetermined limit; otherwise, the unit is replaced. This is called the Repair Cost Limit Policy in the literature. Yun and Bai (1987) study the optimal repair cost limit policies under an imperfect maintenance assumption.

The Repair Time Limit Policy is proposed by Nakagawa and Osaki (see Nguyen and Murthy 1981) in which a unit is repaired at failure: if the repair is notcompleted within a specified time $T$, it is replaced by a new one; otherwise the repaired unit is put into operation again where $T$ is called the repair limit time. Nguyen and Murthy (1981) study the repair time limit replacement policies with imperfect repair in which there are two types of repair - local and central repair. The local repair is imperfect while the central repair is perfect. The optimal policies are derived to minimize the expected cost rate for an infinite time span. The research under the repair limit policy and its extensions is summarized in Table 2.6.

Table 2.6. Imperfect maintenance study under repair limit policy

| Study | CM before <br> cost limit | CM after <br> cost limit | Treatment <br> method | Optimality <br> criterion | Modeling <br> tool | Planning <br> horizon |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Beichelt <br> $(1978$, <br> 1981b) | Minimal | Perfect | $(p(t), q(t))$ | Cost rate | Renewal <br> theory | Infinite |
| Nguyen and <br> Murthy <br> $(1981)$ | Imperfect | Perfect | Others | Cost rate | Renewal <br> theory | Infinite |
| Yun and <br> Bai (1987) | Imperfect | Perfect | $(p, q)$ rule | Cost rate | Renewal <br> theory | Infinite |
| Yun and <br> Bai (1988) | Minimal | Perfect | Others | Cost rate | Renewal <br> theory | Infinite |
| Wang and <br> Pham <br> $(1996 c)$ | Imperfect | Imperfect | $(p, q)$ rule/ <br> $(a, \beta)$ rule | Cost rate <br> Availability | Quasi- <br> renewal <br> theory | Infinite |

# 2.1.2.6 Multicomponent Systems 

Imperfect maintenance models for multi-unit systems are summarized in Table 2.7. For series system Zhao (1994) establishes a series system availability model in which either minimal repair or perfect repair of all components can be modeled based on Barlow and Proschan's work (1975). He assumes that the repaired component might not be as good as new and its lifetime may follow any distribution which can be different from that of old one after repair and obtain mean limiting availability and mean system down and up time. In this model of series system, repair time is not negligible and thus it is practical. This treatment method for imperfect repair is similar to the one by Subramanian and Natarajan (1980). Besides, Sheu et al. have done some work on this problem. The related research is summarized in Table 2.7.

### 2.1.2.7 Others

Jack (1991) investigates a maintenance policy involving imperfect repairs on failure with replacement upon the $N^{\text {th }}$ failure. Dagpunar and Jack (1994) determine the optimal number of imperfect PM during a finite horizon given that the minimal repairs are made at any failures between PMs and the $i^{\text {th }} \mathrm{PM}$ makes the age of a unit $x_{i}$ units of time younger ( $x$ rule). Chun (1992) studies determination of the optimal number of periodic PMs under a finite planning horizon using the $x$ rule.Makis and Jardine (1992) contemplate a replacement policy without PMs in which a unit can be replaced at any time at a cost $c_{0}$, and at the $n^{\text {th }}$ failure the unit is either replaced at the cost $c_{0}$ or undergoes an imperfect repair at a cost $c(n, t)$ where $t$ is the age of the unit. They use the $(p(n, t), q(n, t), s(n, t))$ rule to model imperfect repair. Makis and Jardine $(1991,1993)$ discuss the optimal replacement policy with imperfect repair at failure: a unit is replaced each time at the first failure after some fixed time using the $(p(t), q(t), s(t))$ rule and the virtual age method, respectively.

Table 2.7. Multicomponent systems subject to imperfect maintenance

| Study | PM | CM | Treatment | Optimality criterion | Modeling tool | Horizon / architecture / policy |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Shaked and <br> Shanthikumar <br> (1986) | None | Imperfect | Multiple $(p, q)$ rule | None | Renewal | Infinite / <br> Arbitrary/ |
| Subramanian and Natarajan (1990) | None | Imperfect | Other | Reliability <br> Availability | Stochastic process | Infinite / <br> Two-unit standby/ |
| Zheng and <br> Fard (1991) | Perfect | Imperfect | Other | Cost rate | Probability | Infinite / <br> Arbitrary / <br> Failure limit |
| Sheu and Griffith (1991b) | None | Imperfect | Multiple $(p(t), q(t))$ | None | Renewal theory | Infinite / <br> Arbitrary / <br> Age-dependent |
| Sheu and Liou (1992c) | Perfect | Imperfect | $\left(p_{1}(t), \ldots, p_{n}(t)\right)$ | Cost rate | NHPP | Infinite / <br> $k$-out-of- $n$ / <br> Age-dependent |
| Zhao (1994) | None | Imperfect | Other | Availability | Probability | Infinite/ <br> Series |
| Sheu and Kuo (1994) | Perfect | Imperfect | $(p(t), q(t))$ | Cost rate (random cost) | Renewal theory | Infinite / <br> $k$-out-of- $n$ / <br> Age-dependent |
| Wang and <br> Pham (2006) | None | Imperfect | $(\alpha, \beta)$ | Availability | Quasi- <br> renewal <br> theory | Infinite / <br> Series / |
| Wang (1997) | Perfect | Imperfect | $(p(t), q(t))$ | Availability Cost rate | Renewal theory | Infinite / <br> Arbitrary / <br> Age-dependent |
| Pham and <br> Wang (2000) | Imperfect | Imperfect | $(p, q)$ rule | Availability cost rate | Renewal theory | Infinite / <br> $k$-out-of- $n$ / <br> Periodic |
| Wang et al. <br> 2001) | Imperfect | Perfect | $(p(t), q(t))$ | Availability Cost rate | Renewal theory | Infinite / Arbitrary / <br> Age-dependent |

Block et al. (1992) introduce a generalized age replacement policy - repair replacement policy where units are preventively maintained when a certain time has elapsed since their last repair. If the last repair was a perfect repair, this policy is essentially the same as an age replacement policy.Srivastava and Wu (1993) present an imperfect-inspection model in which failures can only be detected with probability $p$, and they discuss the estimation of parameter $p$. Sheppard (1983) and Nicolescu (1985) study imperfect testing which may result in reduction of availability of a unit. Ebrahimi (1985) derives the mean time to keep a failure-free operation with imperfect repair which either restore a unit to "as good as new" or to "as bad as old". Guo and Love (1992), and Love and Guo (1993) contemplate the statistical analysis for imperfect repair models.

Fontenot and Proschan (1984) explore four imperfect maintenance models using the $(p, q)$ rule under various maintenance policies. Helvic (1980) investtigates maintenance of the fault-tolerant system using the $(p, q)$ rule. Besides, Abdel-Hameed (1987b, 1995), Makis and Jardine (1992), Murthy(1991), Nguyen and Murthy (1981), Natvig (1990), and Zheng and Fard (1991) also discuss the imperfect repair problem.

# 2.2 Dependence 

There are three kinds of dependencies: Economic Dependence, Correlated Failures and Repairs, and Failure Dependence, as stated in Chapter 1. McCall (1963), and Radner and Jorgenson (1963) address the economic dependence in a system with $n$ components. Ozekici (1988) studies the effects of failure and economic dependencies on periodic replacement policies and provide useful characterizations of the optimal replacement policy.

Goel et al. $(1992,1993,1996)$ investigate the correlated failure and repair for some repairable systems: a two-unit standby system, two unit priority redundant system, warm standby system, two-unit cold standby system, two server two unit cold standby system, etc. He uses a bivariate exponential distribution to model the joint distribution of failure and repair times of components. Gupta (1999) discusses profit analysis of a two non-identical unit cold standby system with correlated failure and repair and switchover.

Harris (1968) utilizes a bivariate exponential to describe correlated failures of two components and derives the mean time to system failure by using the supplementary variable technique for an arbitrary repair time distribution. Osaki (1970) extends this analysis to obtain the availability of the system by using a variant of a semi-Markov process with some non-regeneration points. Pijinenburg (1993) obtains reliability, mean time to system failure, pointwise and steady-state availability and joint availability and interval reliability using the imbedded renewal process. Shaked and Shanthikumar (1986), and Sheu and Griffith (1992) model failure dependence in a system with $n$ components using the joint distribution of the lifetimes of $n$ components.

Albin et al. (1992) investigates the PM policies for the series system with failure dependence and economic dependence using Markov chain and presents a brief summary of previous work on failure dependence. Nakagawa and Murthy (1993) consider a two-unit system with two kinds of failure dependence: when unit 1 fails, (1) unit 2 fails with probability $\alpha_{j}$ where $j$ represents the $j^{\text {th }}$ failure of unit 1and (2) unit 1 causes damage with distribution $G(z)$ to unit 2 , and the damage is cumulative and unit 2 fails once the total damage exceeds some specified level. Nakagawa and Murthy (1993) derive expected maintenance cost rates of the two models assuming that the system is replaced at failure of unit 2 or at the $n^{\text {th }}$ failure of unit 1 and discuss the optimum maintenance policies. Murthy and Wilson (1994) consider the parameter estimation problem for failure dependence models.

Pham (1992) studies a high voltage system reliability with dependent failures and treats the failure dependence in the way that the failure of one component causes the failure rate of the other working component to increase.# Maintenance Policies and Analysis 

In the past several decades, maintenance and replacement problems of deteriorating systems have been extensively studied in the literature. Hundreds of maintenance and replacement models have been created. However, all these models can fall into certain categories of maintenance policies: age replacement policy, random age replacement policy, block replacement policy, periodic PM policy, failure limit policy, sequential PM policy, repair cost limit policy, repair time limit policy, repair number counting policy, reference time policy, mixed age policy, preparedness maintenance policy, group maintenance policy, opportunistic maintenance policy, etc. Each kind of policy has different characteristics, advantages, disadvantages, and relationship with others. This chapter summarizes, classifies, and compares various existing maintenance policies in the maintenance literature and practice for both single unit and multi-unit systems, following Wang (2002). Relationships among different maintenance policies are also addressed.

### 3.1 Introduction

Systems used in the production of goods and delivery of services constitute the vast majority of most industry's capital. These systems are subject to deterioration with usage and age (Valdez-Flores and Feldman 1989). Most of them are maintained or repairable systems. Therefore, maintenance on them may be necessary since it can improve reliability. The growing importance of maintenance has generated an increasing interest in the development and implementation of optimal maintenance strategies for improving system reliability, preventing the occurrence of system failures, and reducing maintenance costs of deteriorating systems.

As mentioned earlier in this chapter, maintenance, inspection, and replacement problems have been extensively investigated in the past several decades. In this chapter, a classification scheme of maintenance models that is amenable to current theoretical development is presented. This classification is intended to serve as guidance to both practitioners and researchers. The idea is to classify maintenance models such that a decision maker can recognize those that best fit his maintenanceproblem. Although thousands of maintenance models have been published, there are a limited number of maintenance policies which all maintenance models can be based on. For example, hundreds of maintenance models fall into the age replacement policy, and many fall into the failure limit policy. Therefore, this chapter examines existing maintenance models in terms of maintenance policies that they belong to. It is organized into two sections reflecting the classification scheme: maintenance policies of single unit systems and multi-unit systems. Since maintenance polices for single-unit systems are more established, and are the basis for maintenance policies of multi-unit systems, this chapter discusses single-unit systems in larger space. Note that maintenance policies can also be classified into time-based and system condition-based. For example, periodic PM policy is timebased, and failure limit maintenance policy is condition-based.

# 3.2 Maintenance Policies for One-unit Systems 

As mentioned earlier, although thousands of maintenance models have been developed they can be classified into certain kinds of maintenance policies. This section summarizes, classifies, and compares maintenance policies of one-unit systems. The characteristics, advantages, and drawbacks for each kind of policy will be addressed. Maintenance models with different maintenance cost structures and/or different maintenance restoration degrees (minimal, imperfect, perfect) under the same maintenance policy will be classified into the same policy. The first five subsections of this section discuss maintenance policies with PMs and another subsection contemplates those without PMs. The last subsection provides a summary of them.

The basic assumption for single-unit systems under all PM polices is that the system lifetime has increasing failure rate (IFR).

### 3.2.1 Age-dependent PM Policy

The most common and popular maintenance policy might be the age-dependent PM policy. Studies on this type of policy went back to as early as Morse (1958). In some early work, the age replacement policy was extensively studied. Under this policy, a unit is always replaced at its age $T$ or failure, whichever occurs first, where $T$ is a constant (Barlow and Hunter 1960). Later, as concepts of minimal repair and especially imperfect maintenance (Pham and Wang 1996) became more and more established, various extensions and modifications of the age replacement policy have been proposed. This class of policies, i.e., the age replacement policy and its extensions, is referred to as the age-dependent PM policy in this chapter since their PM times are based on the age of the unit. Under this type of policy, a unit is preventively maintained at some predetermined age $T$, or repaired at failure, until a perfect maintenance, preventive or corrective, is received. Note that PM at $T$ and CM at failure might be either minimal, imperfect, or perfect. Thus, for this class of policies various maintenance models can be constructed according to different types of PMs (minimal, imperfect, perfect), CMs (minimal, imperfect, perfect), cost structures, etc. For example, PM at $T$ might be a replacement orimperfect, CM at failure might be minimal or imperfect, maintenance cost may be a constant or a function of unit age or number of repairs, etc. Details can be found in Pham and Wang (1996) and Valdez-Flores and Feldman (1989), and Chapter 2 of this book. If $T$ is a random variable, the policy is referred to as the random agedependent maintenance policy that is in force when it is impractical to maintain a unit in a strictly periodic fashion. For example, a given unit may have a variable work cycle so that maintenance in midcycle is impossible or impractical. In this eventuality, the maintenance policy would have to be a random one, taking advantage of any free time available to perform maintenance. In the age replacement policy, items are replaced if they reach a certain age. This age is measured from the time of the last replacement. If only minimal repair is undertaken upon failure, the age replacement policy amounts to the "Periodic replacement with minimal repair at failure" policy (see Section 3.2.2).

Some researchers have produced many interesting and significant results for variations of the age replacement model. Tahara and Nishida (1975) introduce the maintenance policy "Replace the unit when the first failure after $t_{0}$ hours of operation or when the total operating time reaches $T\left(0 \leq t_{0} \leq T\right)$, whichever occurs first; failures in $\left[0, t_{0}\right]$ are removed by minimal repair." Note that if $t_{0} \equiv 0$, it becomes the age replacement policy, and if $t_{0} \equiv T$ it reduces to the "Periodic replacement with minimal repair at failure" policy. Observe that $t_{0}$ is a reference time, and maintenance actions are not performed exactly at that moment $t_{0}$ (unlike PM time).

Nakagawa (1984) extends the age replacement policy to replacing a unit at time $T$ or at number $N$ of failures, whichever occurs first, and undergoes minimal repair at failure between replacements. The decision variables for this policy are $T$ and $N$. Note that this policy combines the fixed age and the repair number counting ideas. Clearly, if $N \equiv 1$, this policy reduces to the age replacement policy. Herein this policy is called $T-N$ policy. A more general policy is that a subsystem is subject to imperfect PM at $T$, or CM at the $N^{\text {th }}$ failure ( $N=1,2,3, \ldots$ ), whichever occurs first, and undergoes imperfect repair at failure between replacements.

Two other expansions of the age replacement policy are provided by Sheu et al. (1993, 1995). Sheu et al. (1993) examine a generalized age replacement policy by using the idea similar to Tahara and Nishida (1975). In this policy if a unit fails at age $y<t$, it is subject to a perfect repair with $p(y)$, or undergoes a minimal repair with probability $q(y)=1-p(y)$. Otherwise, the unit is replaced when the first failure after $t$ occurs or the total operating time reaches age $T(0 \leq t \leq T)$, whichever occurs first. The policy decision variables are $t$ and $T$. Obviously, if $t \equiv 0$ then this policy becomes the age replacement policy. If $t \equiv T$ and $q(y) \equiv 1$, it becomes the "Periodic replacement with minimal repair at failure" policy (see Section 3.2.2). Therefore, this policy is also general since it includes both age replacement policy and "Periodic replacement with minimal repair at failure", which are in two different categories of this chapter. Sheu et al. (1995) make another extension to the age replacement policy. They assume that a unit has two types of failures at age $z$, and is replaced at either the $n^{\text {th }}$ Type 1 failure or firstType 2 failure, or at age $T$, whichever occurs first. Type 1 failure occurs with probability $p(z)$ and is corrected by minimal repair. Type 2 failure occurs with probability $q(z)=1-p(z)$ and is corrected by perfect repair. Clearly, if $p(z)=0$ this policy becomes the age replacement policy. If $p(z) \equiv 1$ and $n \equiv \infty$, it becomes the "Periodic replacement with minimal repair at failure" policy (see Section 3.2.2). The policy decision variables are $n$ and $T$. Again, this policy is quite general since it includes both the age replacement policy and the "Periodic replacement with minimal repair at failure" policy.

Block et al. (1993) introduce another generalized age replacement policy, repair replacement policy, where units are preventively maintained when a certain time has elapsed since their last repair. That is, items are repaired if they fail and are replaced only if they survive beyond a certain fixed time from the last repair or replacement. Units are either minimally or perfectly repaired at failure or they are replaced if they survive a certain fixed time from the last repair without suffering a CM. If at failure only perfect repair is allowed, then the repair replacement policy reduces to the age replacement policy. Consequently, the concept of a repair replacement policy is a more general type of replacement policy than the age replacement policy. This policy seems convenient, since, at repair, a schedule to maintain the item is in place and so the bookkeeping to start the maintenance policy can also be undertaken at this time. Furthermore, it seems reasonable, especially for an item which is aging and has undergone minimal repairs, to have some replacement policy rather than to do nothing.

Wang and Pham (1999) make another extension of age replacement policy, called "Mixed age PM policy". In this policy, after the $n^{\text {th }}$ imperfect repair, there are two types of failures. A Type 1 failure might be total breakdowns, while a Type 2 failure can be interpreted as a slight and easily fixed problem. When a failure occurs, it is a Type 1 failure with probability $p(t)$ and a Type 2 failure with probability $q(t)=1-p(t)$. Type 1 failures are subject to perfect repairs and Type 2 failures are subject to minimal repairs. Therefore, each repair is a perfect repair with probability $p(t)$ and a minimal one with probability $q(t)=1-p(t)$. After the first $n$ imperfect repairs, the unit will be subject to a perfect maintenance at age $T$ or at the first Type 1 failure, whichever occurs first. This process continues along an infinite time horizon. The policy decision variables are $T$ and $n$. Obviously, if $p(t) \equiv 0$ and $n \equiv 0$, it becomes the "Periodic replacement with minimal repair at failures" policy. If $p(t) \equiv 1$ and $n \equiv 0$, it becomes the age replacement policy. Chapter 4 will further discuss this policy by investigating the maintenance cost rate, availability and optimal maintenance policy.

The age-dependent PM policy has probably received most of the attention in the literature. In the age-dependent PM policy, the failure rate is increasing with age. Various age-dependent PM policies, summarized from numerous existing maintenance models, are listed in Table 3.1. Table 3.1 shows that age replacement policy is the basic one and most extended policies are general and can include the age replacement policy and/or the "Periodic replacement with minimal repair at failure" policy as special cases. Note also that most of them are proposed based onTable 3.1. Summary of age-dependent PM policies

| Maintenance policy | Typical reference | PM time points | Decision variables | Special cases |
| :--: | :--: | :--: | :--: | :--: |
| Age <br> replacement | Barlow and <br> Hunter (1960) | Fixed age $T$ | $T$ |  |
| Repair <br> Replacement | Block et al. (1993) | Time since last maintenance | Fixed time | Age replacement |
| $T-N$ | Nakagawa (1984) | Fixed age $T$ or time | $T, N$ | Age replacement Periodic PM |
| $(T, t)$ | Sheu et al. (1993) | Fixed Age $T$ or time | $T, t$ | Age replacement Periodic PM |
| $\left(t_{0}, T\right)$ | Tahara and Nishida (1975) | Fixed age $T$ | $t_{0}, T$ | Age replacement Periodic PM |
| Mixed age | Wang and Pham (1999) | Fixed age $T$ or time | $k, T$ | Age replacement Periodic PM |
| $(T, n)$ | Sheu et al. (1995) | Fixed Age $T$ | $T, n$ | Age replacement Periodic PM |

imperfect maintenance concepts. Most extended policies have more than one decision variables.

# 3.2.2 Periodic PM Policy 

In the periodic PM policy, a unit is preventively maintained at fixed time intervals $k T(k=1,2, \ldots)$ independent of the failure history of the unit, and repaired at intervening failures where $T$ is a constant. In some early research, the block replacement policy was examined in which a unit is replaced at pre-arranged times $k T(k=1,2, \ldots)$ and at its failures. The block replacement policy derives its name from the commonly employed practice of replacing a block or group of units in a system at prescribed times $k T(k=1,2, \ldots)$ independent of the failure history of the system and is often used for multi-unit systems. Early research on the block replacement policy can be found in Welker (1959) and Drenick (1960) (see Barlow and Proschan 1965). Another basic periodic PM policy in this class is "Periodic replacement with minimal repair at failures" policy under which a unit is replaced at pre-determined times $k T(k=1,2, \ldots)$ and failures are removed by minimal repair (Barlow and Hunter 1960, Policy II). This policy is good for large systems where minimal repair are plausible at failures. The third basic periodic PM policy: no failure replacement, is that a unit is always replaced at times $k T(k=1,2, \ldots)$ but it is not replaced at failure.

As the concepts of minimal repair and especially imperfect maintenance (Pham and Wang 1996) became more and more established, various extensions and variations of these two policies were proposed. One expansion of the "Periodic replacement with minimal repair at failure" policy is the one where a unit receivesimperfect PM every $T$ time unit, intervening failures are subject to minimal repairs, and it is replaced after its age has reached $(O+1) T$ time units where $O$ is the number of imperfect PMs which have been done (Liu et al. 1995). $O=0$ is allowed in this policy, which means the unit will be replaced whenever it has operated for $T$ time units and there will be no imperfect PM for it. The policy decision variables are $O$ and $T$. Obviously, if $O=0$, this policy becomes the "Periodic replacement with minimal repair at failure" policy.

Cox (1962) extends the block replacement policy to one where if a failure occurs just before a preventive replacement at $T$, it will be left down until the following preventive replacement. In particular, if a failure occurs in an interval $(k T-\delta, k T), \forall k, k=0,1,2, \ldots$, the replacement will be made instantaneously but at $k T$. Obviously, if $\delta=0$, this policy reduces to the block replacement policy. if $\delta=T$, this policy reduces to the third basic periodic PM policy.

Berg and Epstein (1976) have modified the block replacement policy by setting an age limit. Under this modified policy, a failed unit is replaced by a new one; however, units whose ages are less than or equal to $t_{0}\left(0 \leq t_{0} \leq T\right)$ at the scheduled replacement times $k T(k=1,2, \ldots)$ are not replaced, but remain working until failure or the next scheduled replacement time point. Obviously, if $t_{0}=T$, it reduces to the block replacement policy. In Berg and Epstein (1976), this modified block replacement policy is shown to be superior to the block replacement policy in terms of the long-run maintenance cost rate.

Tango (1978) suggests that some failed units be replaced by used ones, which have been collected before the scheduled replacement times. Under this extended block replacement policy, units are replaced by new ones at periodic times $k T(k=1,2, \ldots)$. The failed units are, however, replaced by either new ones or used ones based on their individual ages at the times of failures. A time limit $r$ is set in this policy, similar to $t_{0}$ in Berg and Epstein (1976). Under this policy, if a failed unit' age is less than or equal to a predetermined time limit $r$, it is replaced by a new one; otherwise, it is replaced by a used one. This policy is different from Berg and Epstein's (1976) because it modifies the ordinary block replacement policy by considering rules on the failed units rather than on the working ones. Obviously, if $r=T$, this policy becomes the block replacement policy.

Nakagawa (1981a, b) presents three modifications to the "Periodic replacement with minimal repair at failure" policy. The modifications give alternatives that emphasize practical considerations. The three policies all establish a reference time $T_{0}$ and periodic time $T^{*}$. If failure occurs before $T_{0}$, then minimal repair occurs. If the unit is operating at time $T^{*}$, then replacement occurs at time $T^{*}$. If failure occurs between $T_{0}$ and $T^{*}$, then: (Policy I) the unit is not repaired and remains failed until $T^{*}$; (Policy II) the failed unit is replaced by a spare unit as many times as needed until $T^{*}$; (Policy III) the failed unit is replaced by a new one. In all these three policies, the policy decision variables are $T_{0}$ and $T^{*}$. Clearly, if $T_{0} \equiv T^{*}$, Policies I, II, and II all become the "Periodic replacement with minimalTable 3.2. Summary of periodic PM policies

| Maintenance policy | Typical reference | PM time points | Decision variables | Special cases |
| :--: | :--: | :--: | :--: | :--: |
| Block <br> replacement | Barlow and <br> Hunter (1960) | Periodic time | Periodic time |  |
| Periodic replacement with minimal repair | Barlow and <br> Hunter (1960) | Periodic time | Periodic time |  |
| Overhaul and Minimal repair | Liu et al. (1995) | Periodic time and its multiples | Fixed number of PMs / Periodic time | Periodic replacement with minimal repair |
| $\left(T_{0}, T^{*}\right)$ Policy <br> I | Nakagawa (1981) | Periodic time | Periodic time/ reference time | Periodic replacement with minimal repair |
| $\left(T_{0}, T^{*}\right)$ Policy <br> II | Nakagawa (1981) | Periodic time | Periodic time/ reference time | Periodic replacement with minimal repair |
| $\left(T_{0}, T^{*}\right)$ Policy <br> III | Nakagawa (1981) | Periodic time | Periodic time/ reference time | Periodic replacement with minimal repair/ Block replacement |
| $(n, T)$ | Nakagawa (1986) | Periodic time | Periodic time /number of failures | Periodic replacement with minimal repair |
| $(r, T)$ | Tango (1978) | Periodic time | Periodic time/ reference age | Block replacement |
| $(N, T)$ | Wang and Pham (1999) | Periodic time and its multiples | Periodic time /number of repairs | Block replacement/ <br> Periodic replacement with minimal repair |
| $(\delta, T)$ | Cox (1962) | Periodic time | Periodic time/ reference age | Block replacement/ No failure repair |
| $\left(t_{0}, T\right)$ | Berg and Epstein (1976) | Periodic time | Periodic time/ reference age | Block replacement |

repair at failure" policy. If $T_{0} \equiv 0$, Policy III becomes the block replacement policy.

Nakagawa (1980) also makes an expansion to the block replacement policy. In his policy, a unit is replaced at times $k T(k=1,2, \ldots)$ independent of the age of the unit. A failed unit remains failed until the next planned replacement. Another variant of the "Periodic replacement policy with minimal repair" policy is also due to Nakagawa (1986), in which the replacement is scheduled at periodic times $k T(k=1,2, \ldots)$ and failure is removed by minimal repair. If the total number of failures is equal to or greater than a specified number $n$, the replacement should be done at the next scheduled time; otherwise, no maintenance should be done. Thedecision variable is $n$ and $T$. In this policy, if $n=\infty$, this policy becomes the "Periodic replacement with minimal repair at failure" policy.

Chun (1992) studies determination of the optimal number of periodic PMs under a finite planning horizon. Dagpunar and Jack (1994) determine the optimal number of imperfect PMs for a finite horizon given that the minimal repair is made at any failure between PMs.

Wang and Pham (1999) extend the block replacement policy to a general case. In their policy, a unit is imperfectly repaired at failure if the number of repairs is less than $N$ (a positive integer). The repair is imperfect in the sense that the unit has shorter and shorter lifetime upon each repair. Upon the $N^{\text {th }}$ imperfect repair at failure, the unit is preventively maintained at $k T(k=1,2, \ldots)$ where the constant $T>0$. The PM is imperfect in the sense that after PM the unit is "as good as new" with probability $p$ and "as bad as old" with $(1-p)$. Upon a perfect PM, the maintenance process repeats. The decision variables are $N$ and $T$. The justification of this policy is that when a new unit is put into operation, the first $N$ repairs at failure will be performed at a low cost. This is because the unit is young at those times and these repairs turn out to be imperfect. Usually, these repairs are just minor repairs because it is in good operating condition. After the $N^{\text {th }}$ imperfect repair at failure, the unit may be in worse operating condition due to usage, aging and imperfectness of repairs, and then a major maintenance is necessary at a higher cost. If the repair at failure and PM are perfect and $N \equiv \infty$, this policy reduces to the block replacement policy. If the repair at failure is minimal and PM is perfect and $N \equiv \infty$, this policy amounts to the "Periodic replacement with minimal repair at failure" policy. Chapter 4 will further discuss this policy.

Maintenance schedules under the periodic PM policy, summarized from various existing maintenance models, are listed in Table 3.2, which shows that block replacement policy and periodic replacement with minimal repair are the basic ones with one decision variable. Other policies have more than one decision variables.

# 3.2.3 Failure Limit Policy 

Under the failure limit policy, PM is performed only when the failure rate or other reliability indices of a unit reach a predetermined level and intervening failures are corrected by repairs. This PM policy makes a unit work at or above the minimum acceptable level of reliability. For example, Lie and Chun (1986) formulate a maintenance cost policy where PM is performed whenever a unit reaches the predetermined maximum failure rate, and failures are corrected by minimal repair. Bergman (1978) investigates a failure limit policy in which replacements are based on measurements of some increasing state variable, e.g., wear, accumulated damage or accumulated stress, and the proneness to failure of an active unit is described by an increasing state-dependent failure rate function. The optimal replacement rule in terms of average long-run maintenance cost rate is shown to be a failure limit rule, i.e., it is optimal to replace either at failure or when the state variable has reached some threshold value, whichever occurs first. Bergman's model includes the age replacement policy as a special case.Other research on the failure limit policy can be found in Malik (1979), Canfield (1986), Jayabalan and Chaudhuri (1992a), Jayabalan and Chaudhuri (1992c), Jayabalan and Chaudhuri (1995), Chan and Shaw (1993), Suresh and Chaudhuri (1994), Monga et al. (1997), and Pham and Wang (1996). In addition, Love and Guo (1996) study failure limit policy for PM decisions under Weibull failure rates.

Generally, the problem for this class of policies is that it requires much computing effort to determine maintenance schedules and wasteful to implement.

The failure limit policy and its extensions are summarized in Table 3.3, that shows that most failure limits are measured by failure rates, and maintenance cost rate is most used to determine the optimal maintenance policies. Several policies consider finite planning horizon.

Table 3.3. Summary of failure limit policies

| Typical reference | Reliability index monitored | Optimality criterion | Planning horizon |
| :--: | :--: | :--: | :--: |
| Bergman (1978) | Failure rate through wear, accumulated damage or stress | Cost rate | Infinite |
| Malik (1979) | Reliability | Reliability | Infinite |
| Canfield (1986) | Failure rate | Cost rate | Infinite |
| Zheng and Fard (1991) | Failure rates | Cost rate | Infinite |
| Lie and Chun (1986) | Failure rate | Cost rate | Infinite |
| Jayabalan and <br> Chaudhuri (1992a) | Failure rate | Total cost | Finite |
| Jayabalan and <br> Chaudhuri (1992c) | Age <br> others | Cost rate | Infinite |
| Jayabalan and <br> Chaudhuri (1992d) | Age | Total cost | Finite |
| Chan and Shaw (1993) | Failure rate | Availability | Infinite |
| Suresh and Chaudhuri (1994) | Reliability and failure rate | Total cost | Finite |
| Jayabalan and <br> Chaudhuri (1995) | Age | Total cost | Finite |
| Monga et al. (1997) | Reduction <br> (age and failure rate) | Cost rate | Infinite |
| Love and Guo (1996) | Weibull failure rate | Cost rate | Infinite |

# 3.2.4 Sequential PM Policy 

Unlike the periodic PM policy, a unit is preventively maintained at unequal time intervals under the sequential PM policy. Usually, the time intervals become shorter and shorter as time passes, considering that most units need more frequent maintenance with increased ages. An early sequential PM policy is designed for a finite span (Barlow and Proschan 1962). Under this sequential policy, the age forwhich PM is scheduled is no longer the same following successive PMs, but depends on the time still remaining. Clearly the added flexibility permits the achievement of an optimum sequential PM policy having lower cost than that of the corresponding optimum age replacement policy. Under sequential PM policy, the next PM interval is selected to minimize the expected expenditure during the remaining time. Thus, this policy does not specify at the beginning of the original time span each future PM interval; rather, after each PM, it specifies only the next PM interval. This gain in flexibility leads to reduction in expected cost.

Nguyen and Murthy (1981b) introduce a sequential policy which calls for a PM if a failure has not occurred by some reference time $t_{i}$, where $t_{i}$ is the maximum time that a unit should be left without maintenance after the $(i-1)^{\text {th }}$ repair (time from the last repair or replacement). In this policy, a unit is replaced after $(k-1)$ repairs. It is repaired (or replaced at the $k^{\text {th }}$ repair) at the time of failure or at age $t_{i}$, whichever occurs first. The decision variables are $k$ and $t_{i}$ for $i=1, \ldots, k$, given that each PM increases the failure rate of the unit. If $k=1$, this sequential policy reduces to the age replacement policy.

Nakagawa $(1986,1988)$ discusses a sequential PM policy where PM is done at fixed intervals $x_{k}$ for $k=1,2, \ldots, N$. The unit is replaced at the $N^{\text {th }} \mathrm{PM}$ and failures between PMs are corrected by minimal repairs, given the unit has different failure distributions between PMs (the failure rate of the unit increases with the number of PMs, or its age is reduced (1988), i.e., the first $(N-1)$ PMs are imperfect). The policy decision variables are $N$ and $x_{k}(k=1,2, \ldots, N)$. Nakagawa $(1986,1988)$ also presents two numerical examples indicating that the optimal policy satisfies $x_{k} \leq x_{k-1}$ for $k=2, \ldots, N$. Nguyen and Murthy (1981b) study this policy (Policy II in their paper). If $N=1$, this sequential policy reduces to the "Periodic replacement with minimal repair at failure" policy.

These sequential policies are practical because most units need more frequent maintenance with increased age. They are different from the failure limit policy in that it controls $x_{k}$ lengths directly but the failure limit policy controls failure rate, reliability, etc., directly. Moreover, Kijima and Nakagawa (1992) develop a sequential PM policy using an accumulated damage concept.

In Wu and Clements-Croome (2005), both PM and CM are carried out. The PM is sequentially executed with $\tau_{n}$ time units after the $(n-1)^{\text {th }} \mathrm{PM}$, where $n=1,2, \ldots$ Between two adjacent PMs, a CM is carried out immediately on failure. $\tau_{n}$ is dependent on $n$ and determined through minimizing the maintenance cost rate. Obviously, if $\tau_{n}$ is independent on $n$, the sequential PM policy becomes a periodic PM policy.

# 3.2.5 Repair Limit Policy 

The repair limit policies and their extensions are summarized in Table 3.4. Note that in the existing literature, there are two types of repair limit policies: repair cost limit policy and repair time limit policy.When a unit fails, the repair cost is estimated and repair is undertaken if the estimated cost is less than a predetermined limit; otherwise, the unit is replaced. This is called repair cost limit policy in the literature, investigated by Gardent and Nonant (1963) and Drinkwater and Hastings (1967).

A drawback of the repair cost limit policy is that the replacement or repair decision depends only on the cost of a single repair. Long-lasting situations characterized by frequent repairs whose costs are below the corresponding limit do not directly influence the time of replacement, although the repair cost rate might justify a replacement. Thus, further financial savings seem possible if the replacement decision depends on the whole history of the repair process. Considering this drawback, Beichelt (1982) examines repair cost limit policy and uses the repair cost rate (repair cost per unit time) as a criterion of replacement or repair: a unit is replaced as soon as the repair cost rate reaches or exceeds a fixed level, otherwise, it is repaired. In this policy (Beichelt, 1982), the replacement intervals are independently and identically distributed random variables. Yun and Bai (1987) propose a repair cost limit policy in which when a unit fails, the repair cost is estimated and repair is undertaken if the estimated cost is less than a predetermined limit $L$, where the repair is imperfect. Otherwise, the unit is replaced. This policy by Yun and Bai (1987) is generalized from the one by Hastings (1967). In addition, Kapur et al. (1989) extend the repair cost limit policy to incorporate the number of repairs as a policy decision variable.

Table 3.4. Summary of repair limit policies

| Reference | CM before limit | CM after limit | Limit type | Optimality criterion | Planning horizon |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Hastings (1969) | Minimal | Perfect | Cost | Cost rate | Infinite |
| Kapur et al. (1989) | Minimal | Perfect | Cost | Cost rate | Infinite |
| Beichelt (1982) | Perfect | Perfect | Cost rate | Cost rate | Infinite |
| $\begin{gathered} \text { Beichelt } \\ (1978,1981 \mathrm{~b}) \end{gathered}$ | Minimal | Perfect | Cost rate | Cost rate | Infinite |
| Nguyen and <br> Murthy (1981) | Imperfect | Perfect | Time | Cost rate | Infinite |
| Yun and Bai (1988) | Minimal | Perfect | Cost | Cost rate | Infinite |
| $\begin{gathered} \text { Koshimae et al. } \\ \text { (1996) } \end{gathered}$ | Perfect | Perfect | Time | Cost rate | Infinite |
| Nguyen and <br> Murthy (1980) | Minimal | Perfect | Time | Cost rate | Infinite |
| $\begin{gathered} \text { Dohi et al. } \\ \text { (1997) } \end{gathered}$ | Minimal | Imperfect | Time | Cost rate | Infinite |
| Park (1983) | Minimal | Perfect | Cost | Cost rate | Infinite |
| Nakagawa and Osaki (1974) | Minimal | Perfect | Time | Cost rate | Infinite |
| $\begin{gathered} \text { Yun and Bai } \\ \text { (1987) } \end{gathered}$ | Imperfect | Perfect | Cost | Cost rate | Infinite |
| $\begin{gathered} \text { Wang and Pham } \\ \text { (1996c) } \end{gathered}$ | Imperfect | Imperfect | Cost | Availability/ <br> Cost rate | Infinite |The repair time limit policy is proposed by Nakagawa and Osaki (1974) in which a unit is repaired at failure: if the repair is not completed within a specified time $T$, it is replaced by a new one; otherwise the repaired unit is put into operation again, where $T$ is called repair time limit. Nguyen and Murthy (1980) study a repair time limit replacement policy with imperfect repair in which there are two types of repair - local and central repair. The local repair is imperfect while the central repair is perfect, which may take a longer time. Dohi et al. (1997) consider a generalized repair time limit replacement problem with lead time and imperfect repair, which is subject to a time constraint, and propose a nonparametric solution procedure to estimate the optimal repair time limit. Koshimae et al. (1996) consider another repair time limit policy. Under this policy, when the original unit fails, the repair is started immediately. If the repair is completed in a time limit $t_{0}$, then the repaired unit is installed as soon as the repair is finished. On the other hand, if the repair time is greater than the time limit $t_{0}$, the failed unit is scrapped and a spare is ordered immediately. It is delivered and installed after a lead time. The policy decision variable is the repair time limit $t_{0}$.

# 3.2.6 Repair Number Counting and Reference Time Policy 

Morimura and Makabe (1963a) introduce a policy where a unit is replaced at the $k^{\text {th }}$ failure. The first $(k-1)$ failures are removed by minimal repair. Upon replacement, the process repeats. This policy is called repair number counting policy in this chapter. The policy decision variable is $k$. Later, Morimura (1970) extends this policy by introducing another policy variable $T$ - critical reference time which is a positive number. Under this extended policy, all failures before the $k^{\text {th }}$ failure are corrected only with minimal repair. If the $k^{\text {th }}$ failure occurs before an accumulated operating time $T$, it is corrected by minimal repair and the next failure induces replacement. But if the $k^{\text {th }}$ failure occurs after $T$, it induces replacement of the unit. Obviously, this policy combines the ideas of counting the number of repairs and recording the elapsed time. The policy decision variables are $k$ and $T$. If the policy decision variable $T$ is zero, this policy reduces to the repair number counting policy. An imperfect repair version of the repair number counting policy is examined by Jack (1991): performing imperfect repair on failure, and replacement upon the $k^{\text {th }}$ failure. A policy similar to the repair number counting policy is also investigated by Park (1979) in which a unit is replaced at the $k^{\text {th }}$ failure and minimal repairs are performed for the first $(k-1)$ failures. Later, Lam (1988) and Stadje and Zuckerman (1990) investigate the repair number counting policy, given that the lengths of the operating intervals decrease whereas the durations of the repair increase in different ways.

Muth (1977) examines a replacement policy, similar to the reference time idea of the extended policy by Morimura and Makabe (1970), in which a unit is minimally repaired up to time $T$ and replaced at the first failure after $T$. This policy is referred to as the reference time policy later in this review. Note that in this policy the maintenance action is not undertaken exactly at the reference time point $T$ (unlike PM time). Makis and Jardine $(1991,1993)$ discuss an optimal replacement policy with imperfect repair at failure: a unit is replaced at the firstfailure after some fixed time. Makis and Jardine (1992) also introduce a general policy in which a unit can be replaced at any time and at the $n^{\text {th }}$ failure the unit can be either replaced or can undergo an imperfect repair. Under different conditions, this policy can reduce to the repair number counting policy, reference time policy, and "Periodic replacement with minimal repair at failure" policy, respectively. Therefore, it is a quite general policy.

In general, the repair number counting policy is effective when the total operating time of a unit is not recorded or it is time consuming and costly to replace a unit in operation. It has been proven (Muth 1977) that the reference time policy yields a lower long-run expected cost per unit time than the periodic PM policy given that the mean residual life function of the unit is strictly decreasing after some age $t_{0}$. With this condition, called positive aging, the unit deteriorates and eventually reaches a condition where it is no longer economically justifiable to perform minimal repair after repair. It is shown that the repair number counting policy yields lower asymptotic expected cost rate than the age replacement policy. Also the number of failures before replacement in the repair number counting policy is less than that in the age replacement policy. However, all these results are proven numerically for the Weibull distribution (i.e., for some specific Weibull distribution parameter values).

Phelps (1981) compares the "Periodic replacement with minimal repair at failure" policy (Barlow and Hunter 1960), the repair number counting policy (Morimura and Makabe 1963a,b; Park 1979), and the reference time policy (Muth 1977), given an increasing failure rate. Phelps (1981) shows that the reference time policy, replacing after the first failure that occurs after reference time $T$, is the optimal of the three policies in terms of the long-run cost rate; the repair number counting policy is more economical than the "Periodic replacement with minimal repair at failure" policy.

Note that generally there are no PMs scheduled for this type of policy. These policies are mainly based on counting the number of repairs and/or reference time, but the age-dependent PM policy and periodic PM policy rely on PM times, at which maintenance actions are performed. In the repair number counting and reference time policy, maintenance actions are not undertaken precisely at the reference time point $T$. In the repair number counting and reference time policy, number of repairs and/or reference time are policy decision variable(s). In the agedependent PM policy and periodic PM policy, PM time is one of the policy decision variables.

# 3.2.7 On the Maintenance Policies for Single-unit Systems 

The age-dependent PM policy and periodic PM policy have received much more attention in the literature. Hundreds of papers and models have been published under these two kinds of maintenance policies, as summarized in McCall (1963), Barlow and Proschan (1965, 1975), Pieskalla and Voelker (1976), Osaki and Nakagawa (1976), Sherif and Smith (1981), Jardine and Buzacott (1985), ValdezFlores and Feldman (1989), Pham and Wang (1996), and Wang (2002). Detailed mathematical comparisons on the age and block replacement policies can be found in Barlow and Proschan $(1965,1975)$ in which the general conclusion is that theage replacement policy is an economical way to the block replacement policy. They prove that more unfailed components under the block replacement policy are removed than under age replacement policy, and the total number of removals for both failed and unfailed components under the block replacement policy is larger. Berg and Epstein (1978) compare three types of replacement policies: age, block, failure replacement policies and provide a heuristic rule for choosing the best one. Berg (1976a) and Bergman (1980) prove that an age replacement policy is optimal among all reasonable maintenance policies. In Block et al. (1990), comparisons are made between the block replacement policy and "Periodic replacement with minimal repair at failure" policy. In Block et al. (1993), comparisons are made among the age replacement policy, block replacement policy, and repair replacement policy. The periodic PM policy is perhaps more practical than the agedependent PM policy since it does not require keeping records on unit usage. The block replacement policy is more wasteful than the age replacement policy since a unit of "young" age might be replaced at periodic times. Generally, the same argument may hold for the age-dependent PM and periodic PM policy.

The failure limit policy, repair limit policy, and sequential policy are more practical, but there has been much less research done on it. The failure limit policy is also directly consistent with the maintenance objectives: improving reliability and reducing failure frequency. One of the disadvantages of the failure limit policy and sequential policy is that their PM intervals are not equal and thus it is wasteful to implement them.

Note that maintenance policies have become more and more general because they include some previous policies as special cases. This is reflected in Tables 3.1 and 3.2, and described in Sections 3.2.1 - 3.2.6. In general, optimal maintenance plans obtained from these general policies may result in some cost savings since the optimal maintenance schedules under them might be "globally" optimal (optimal in a larger range). However, as they become more and more complicated, these general policies may also cause inconvenience in implementation in practice. Similarly, the maintenance cost is no longer a constant and becomes more and more general. For example, it may be a function of unit age and number of repairs already performed on the unit (Note that Frenk et al. (1997) establish a general method for modeling complicated maintenance costs, which is also convenient for this case).

Generally, each maintenance policy for one-unit systems either depends on counting/recording of the number of repairs, PM time, or reference time. In practice, counting number of repairs and recording PM time, and reference time are all possible ways. The current research seems to intend to use two or more of them as policy decision variables in a single policy.

Note that in some policies no PMs are involved. For example, in Gasmi et al. (2003), a system is observed to operate in alternative states. The most common mode is loaded (or regular) operation. Occasionally the system is placed in an unloaded state, while the system is mechanically still operating; it is assumed that the failure intensity is lower due to this reduction in operating intensity. They use a proportional hazard model to capture this reduction in failure intensity due to switching of operating modes. In either operating state, the system is occasionallyshut down for repair and upon failure, one of the three actions is taken: a) minimal repair, b) minor repair, or c) major repair.

# 3.3 Maintenance Policies of Multi-unit Systems 

The six types of maintenance policies in Section 3.2 are designed for a system composed of a single stochastically deteriorating subsystem. A natural generalization of these maintenance policies is to consider a system with a number of subsystems. Optimal maintenance policies for such systems reduce to those for systems with a single subsystem only if there exists neither economic dependence, failure dependence nor structural dependence. In this case, maintenance decisions are independent, and the "optimal" maintenance policy is to employ one of the six classes of maintenance policies described in Section 3.2 for each separate subsystem. However, if there exists dependence, for example, economic dependence, then the optimal maintenance policy is not one of considering each subsystem separately and maintenance decisions will not be independent. Obviously, the optimal maintenance action for a given subsystem at any time point depends on the states of all subsystems in the system: the failure of one subsystem results in the possible opportunity to undertake maintenance on other subsystems (opportunistic maintenance). In this chapter, economic dependence means that performing maintenance on several subsystems jointly costs less money and/or time than on each subsystem separately. Failure dependence means that failure distributions of several subsystems are stochastically dependent.

Economic dependency is common in most continuous operating systems. Examples of such systems include aircraft, ships, power plants, telecommunication systems, chemical processing facilities, and mass production lines. For this type of system, the cost of system unavailability (one-time shut-down) may be much higher than maintenance costs. Therefore, there is often a great potential for cost savings by implementing an opportunistic maintenance policy.

Currently, there is an increasing interest in multicomponent maintenance policies and models. As pointed out in van der Duyn Schouten (1995), one of the reasons that is often put forward to explain the lack of success in applications of maintenance and replacement models is the simplicity of the models compared to the complex environment where the applications occur. In particular, the fact that up to ten years ago the vast majority of the maintenance models were concerned with one single piece of equipment operating in a fixed environment was considered an intrinsic barrier for applications. Next we summarize maintenance policies for multi-unit systems. Cho and Parlar (1991) survey the multi-unit system maintenance models created before 1991, and Dekker et al.'s review (1997) is focused on economic dependence models published after 1991. This chapter emphasizes classifications and characteristics of maintenance policies though sometimes it cites the same existing maintenance models as the previous survey papers. The basic assumptions for multi-unit systems under all maintenance polices are that there are virtually infinitely many disposable identical units with i.i.d. lifetimes for all items; salvage values of all units are negligible.# 3.3.1 Group Maintenance Policy 

The problem of establishing group maintenance policies, which are best from the point of view of the system's reliability or operational cost, has received significant attention in the maintenance literature. One class of problem for group maintenance policies has been to establish categories of units that should be replaced when a failure occurs. This is particularly important when there are varying access costs associated with disassembly and reassembly, and simultaneous PM of categories of parts may be appropriate. A second class of group replacement studies has been concerned with reducing costs by including redundant parts into systems design. A third class of papers has been concerned with establishing group maintenance policies for systems of independently operating machines, all of which are subject to stochastic failures from the same distribution (Ritchken and Wilson 1990). For this class of problems, there are three existing group maintenance policies. The first policy, referred to as a $T$-age group replacement policy, calls for a group replacement when the system is of age $T$. A second policy, referred to as an $m$-failure group replacement policy, calls for a system inspection after $m$ failures have occurred. The third policy combines the advantages of the $m$-failure and $T$-age policies. This policy, referred to as an $(m, T)$ group replacement policy, calls for a group replacement when the system is of age $T$, or when $m$ failures have occurred, whichever comes first. The $(m, T)$ group replacement policy requires inspection at either the fixed age $T$ or the time when $m$ machines have failed, whichever comes first. At an inspection, all failed units are replaced with new ones and all functioning units are serviced so that they become as good as new. The policy decision variables are $m$ and $T$.

Gertsbakh (1984) introduces a policy in which a system has $n$ identical units with exponential lifetimes, and it is repaired when the number of failed units reaches some prescribed number $k$, the policy decision variable. Vergin and Scriabin (1977) propose an $(n, N)$ policy. Under this group maintenance policy, a unit undergoes preventive replacement if it has operated for $N$ periods, and undergoes a group replacement if it has operated $n$ periods and if either another unit fails or another unit reaches its preventive replacement age (where $n<N$ ). Love et al. (1982) establish another group replacement policy for a fleet of vehicles. Under this group maintenance policy a vehicle is replaced when repair cost for the vehicle exceeds a pre-set repair limit; otherwise, it is repaired. Sheu and Jhang (1997) propose a 2-phase group maintenance policy for a group of identical repairable items. The time interval $(0, T)$ is defined as the first phase, and the timer interval $(T, T+W)$ is defined as the second phase. As individual units fail, individual units have two types of failures. Type I failures are removed by minimal repairs, whereas Type II failures are removed by replacements or are left idle. A group of maintenance is conducted at time $T+W$ or upon the $k^{\text {th }}$ idle, whichever comes first. The policy decision variables are $T, W$, and $k$.

Wildeman et al. (1997) discuss a group maintenance policy considering that a maintenance activity carried out on a technical system involves a systemdependent set-up cost that is the same for all maintenance activities carried out on that system, and grouping activities thus saves costs since execution of a group of activities requires only one set-up. Under this policy, a rolling-horizon approach isproposed that takes a long-term tentative plan as a basis for a subsequent adaptation according to information that becomes available in the short term. This policy makes it easy to incorporate short-term circumstances such as opportunities or a varying use of components because these are either not known beforehand or make the problem intractable.

Assaf and Shanthikumar (1987) propose a group preparedness policy for a set of $N$ machines having exponential lifetimes with constant rate. A failed machine can be repaired at any time, and the repair is perfect. The number of failed machines in the system is unknown unless an inspection is carried out. Upon an inspection, a decision will be made on whether to repair the failed machines or not, based on the number of failed machines in the system, a policy decision variable.

# 3.3.2 Opportunistic Maintenance Policies 

As pointed out earlier, maintenance of a multicomponent system differs from that of a single-unit system because there exists dependence in multicomponent systems. One of the dependencies is economic dependence. For example, it is possible to do PM to non-failed subsystems at a reduced additional cost while failed subsystems are being repaired. Another dependence is failure dependence, or correlated failures. For example, the failure of one subsystem may affect one or more of the other functioning subsystems, and times to failures of different units are then statistically dependent (Nakagawa and Murthy 1993). Berg $(1976,1977)$ suggests a preventive replacement policy for a machine with two identical components which are subject to exponential failure. Under this policy, upon a component failure the other component as well as the failed one is also replaced by a new one if its age exceeds a pre-determined control limit L. Later, Berg (1978) extends it to such an policy: both units are replaced either when one of them fails and the age of the other unit exceeds the critical control limit $L$, or when any of them reaches a predetermined critical age $S$. A unit is replaced at age $T$ or at failure, whichever occurs first. Note that this policy will become two independent age replacement policies if $L \equiv \infty$.

Zheng and Fard (1991) examine an opportunistic maintenance policy based on failure rate tolerance for a system with $k$ different types of units. A unit is replaced (active replacement) either when the hazard rate reaches $L$ or at failure with the failure rate in a predetermined interval $(L-u, L)$. When a unit is replaced due to the hazard rate reaching $L$, all of the operating units with their hazard rate falling in the interval $(L-u, L)$ are replaced (passive replacement) at that time. A unit is subject to minimal repair at failure when the hazard rate is in interval $(0, L-u)$. The policy decision variables are $L$ and $u$.

Kulshrestha (1968) investigates an opportunistic maintenance policy in which there are two classes of units, 1 and 2 . Class 1 contains $M$ standby redundant units so that upon the failure of the currently operating Class-1 units, a standby takes over. When all the Class-1 standbys have failed, the system suffers catastrophic failure. The Class-2 units, on the other hand, form a series system; if one of them should fail, the system suffers a minor breakdown. When a minor breakdownoccurs, there is a possible chance for opportunistic repair of those Class-1 units which have failed.

Pham and Wang (2000) propose two new $(\tau, T)$ opportunistic maintenance policies for a $k$-out-of- $n$ system. In these two policies, minimal repairs are performed on failed components before time $\tau$ - a policy decision variable, and CM of all failed components is combined with PM of all functioning ones after $\tau$. At time $T$, another policy decision variable, PM is performed if the system has not been subject to a perfect maintenance before $T>\tau$. The policy decision variables are $\tau$ and $T$. Pham and Wang (2000) also extend these two policies to the one including the third decision variable - the number of failed components to start CM, considering the $k$-out-of- $n$ system may still operate even if some of its components have failed. Chapter 8 will further discuss this policy.

Dagpunar (1996) introduces a general maintenance policy where replacement of a component within a system is available at an opportunity. An opportunity arises if the failure of some other part of the system allows the component in question to be replaced. It is assumed that the opportunity process is Poisson, which is reasonable if the system consists of a large number of components which are regularly maintained. In this policy the component will be replaced if its age at an opportunity exceeds a specified control limit.

Radner and Jorgenson (1963) and Wang et al. (2001) investigate an opportunistic preparedness maintenance of multi-unit systems with $(n+1)$ subsystems. Wang et al. (2001) examine such a preparedness policy:
i) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $\left[0, t_{i}\right)$, replace subsystem $i$ alone at a cost of $C_{i}$ and at a time of $w_{i}$, $\forall i, i=1,2, \ldots, n$.
ii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $\left[t_{i}, T\right)$, replace subsystem $i$ and do perfect PM on subsystem 0 , $\forall i, i=1,2, \ldots, n$. The total maintenance cost is $C_{0 i}$ and total maintenance time is $w_{0 i}$.
iii) If subsystem 0 survives until its age $x=T$, perform PM on subsystem 0 alone at a cost of $C_{0}$ and at a maintenance time of $w_{0}$ at $x=T$. PM is imperfect.
iv) If subsystem 0 has not received a perfect PM at $T$, perform PM on it alone at time $j T(j=2,3, \ldots)$ until it gets a perfect PM; if subsystem 0 has not experienced a perfect maintenance and subsystem $i$ fails after some PM, replace subsystem $i$ and do perfect PM on subsystem $0, \forall i, i=1,2, \ldots, n$. The total maintenance cost is still $C_{0 i}$ and total maintenance time is $w_{0 i}$. This process continues until subsystem 0 gets a perfect maintenance.

Chapter 7 will further discuss the above preparedness maintenance policy by investigating its reliability and maintenance cost measures. Chapter 6 will discussthe following opportunistic maintenance policy for multi-unit systems with $(n+1)$ subsystems and arbitrary reliability architecture:
(i) If subsystem 0 fails at any time before $T$, perform imperfect repair on it at a cost $C_{00}$.
(ii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $0 \leq x<t_{i}$, replace subsystem $i$ alone at a cost $C_{i}$ and at a time $w_{i}$, $\forall i, i=1,2, \ldots, n$.
(iii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $t_{i} \leq x<T$, replace subsystem $i$ and do perfect PM on subsystem 0 , $\forall i, i=1,2, \ldots, n$. The total maintenance cost is $C_{0 i}$ and total maintenance time is $w_{0 i}$.
(iv) If subsystem 0 survives until $x=T$, perform PM on subsystem 0 at a cost $C_{0}$ and at a maintenance time $w_{0}$.# A Quasi-renewal Process and Its Applications 

Renewal theory had its origin in the study of strategies for replacement of technical components (Cox 1962). In a renewal process, the times between successive events are supposed to be independent and identically distributed (i.i.d). Most maintenance models using renewal theory were actually based on this assumption, i.e., "as good as new" after each maintenance. As pointed out in Chapters 1 and 2, "as good as new" represents one extreme type of maintenance results and usually a system may not be good as new but younger after maintenance, i.e., maintenance is imperfect. Therefore, it is useful to establish some directly effective theories which can be used to model imperfect maintenance.

In this chapter, a general renewal process, a quasi-renewal process, is introduced and its usefulness in treating imperfect maintenance of one-unit systems is demonstrated. Section 4.1.1 presents the definition of the quasi-renewal process and discusses its properties. The quasi-renewal function of the quasi-renewal process is derived in Section 4.1.2. The justification of the quasi-renewal process in modeling imperfect maintenance and the problems of statistical hypothesis testing are discussed in Section 4.1.3. Using the quasi-renewal theory, eleven imperfect maintenance models with periodic PM, age-dependent PM, and cost limit replacement policies for one-component systems are developed. For each of the 11 maintenance models, the expected maintenance cost rate and/or availability are derived, and optimum maintenance policies as well as related optimization problems are discussed. The developed models show that the quasi-renewal process and its basic idea are an effective tool to deal with imperfect maintenance problems. This chapter is based on Wang and Pham (1996a, b, c, 1999). In Chapter 5 , the quasi-renewal process will be used to study imperfect repair of the series system. Chapter 9 uses it to establish inspection time sequences and Chapter 10 uses the truncated quasi-renewal process to model warranty cost. Software reliability growth and testing cost by using quasi-renewal process is discussed in Chapter 11.

## NOTATION

$T \quad$ Fixed age at which a unit is subject to PM, $T>0$
$A \quad$ Asymptotic average availability$c_{p} \quad$ PM cost at fixed age $T$
$c_{f} \quad$ Fixed part of imperfect repair cost at failure for each of the first $(k-1)$ failures
$c_{v} \quad$ Incremental part of imperfect repair cost at failure for each of the first $(k-1)$ failures
$c_{f r} \quad$ Repair (perfect or imperfect ) cost at failure after the first $(k-1)$ imperfect repairs
$(k-1)$ Number of imperfect repairs in the sense of the fixed lifetime reduction rule
$L \quad$ Expected total maintenance cost per unit time or cost rate
$D \quad$ Expected renewal cycle length
$f_{1}(t), F_{1}(t) \quad$ Probability density function ( $p d f$ ) and cumulative distribution function ( $c d f$ ) of the failure time of a new unit
$r_{1}(t), R_{1}(t) \quad$ Failure rate and cumulative failure rate function of the failure time of a new unit
$s_{1}(t) \quad$ Survival function ( $s f$ ) or reliability function of a new unit, $s_{1}(t)=1-F_{1}(t)$
$p \quad$ Probability that maintenance is perfect
$q \quad$ Probability that maintenance is minimal where $q=1-p$
$\mu, \eta \quad$ Expected lifetime and expected repair time of a new unit
$\alpha \quad$ Lifetime reduction factor
$\beta \quad$ Incremental factor for repair time

# ACRONYMS 

NBU New better than used
NWU New worse than used
NBUE New better than used in expectation
NWUE New worse than used in expectation
IFRA Increasing failure rate in average
DFRA Decreasing failure rate in average
IFR Increasing failure rate
DFR Decreasing failure rate
i.i.d. Independently and identically distributed

### 4.1 A Quasi-renewal Process

The quasi-renewal process is defined and studied in Wang and Pham (1996b). In this section, we will introduce its definition, properties, quasi-renewal function, parameter estimation problems, and truncated quasi-renewal processes.

### 4.1.1 Definition

Let $\{N(t), t>0\}$ be a counting process, and $X_{n}$ denote the time between the $(n-$ 1) ${ }^{\text {th }}$ and the $n^{\text {th }}$ event of this process, $n \geq 1$.Definition 4.1 Observe the sequence of nonnegative random variables $\left\{X_{1}, X_{2}, X_{3}, \ldots\right\}$. The counting process $\{N(t), t \geq 0\}$ is said to be a quasi-renewal process with parameter $\alpha$ and the first interarrival time $X_{1}$, if $X_{1}=Z_{1}$, $X_{2}=\alpha Z_{2}, X_{3}=\alpha^{2} Z_{3}, \ldots$, where $Z_{i} \mathrm{~s}$ are i.i.d. and $\alpha>0$ is a constant.

When $\alpha=1$ this quasi-renewal process becomes the ordinary renewal process. We will see that this quasi-renewal process can be used to model hardware maintenance process when $0<\alpha \leq 1$. It can also be utilized to model software reliability growth process in testing or operation phase, hardware repair times, and hardware reliability growth in burn-in stage for $\alpha>1$. Later on, a quasi-renewal process with parameter $\alpha>1$ will be known as an increasing quasi-renewal process, and a quasi-renewal process with $0<\alpha<1$ as a decreasing quasi-renewal process.

Assuming that the probability density function ( $p d f$ ), cumulative density function ( $c d f$ ), survival function ( $s f$ ), and failure rate of random variable $X_{1}$ are $f_{1}(x), F_{1}(x), s_{1}(x)$ and $r_{1}(x)$ respectively. Wang and Pham (1996b) show that the $p d f, c d f, s f$, failure rate, mean and variance of random variable $X_{n}$ for $n=2,3,4, \ldots$ are given by Equation (4.1):

$$
\begin{cases}f_{n}(x)=\alpha^{1-n} f_{1}\left(\alpha^{1-n} x\right) & F_{n}(x)=F_{1}\left(\alpha^{1-n} x\right) \\ s_{n}(x)=s_{1}\left(\alpha^{1-n} x\right) & r_{n}(x)=\alpha^{1-n} r_{1}\left(\alpha^{1-n} x\right) \\ E\left(X_{n}\right)=\alpha^{n-1} E\left(X_{1}\right) & \operatorname{Var}\left(X_{n}\right)=\alpha^{2 n-2} \operatorname{Var}\left(X_{1}\right)\end{cases}
$$

Because the nonnegativity of $X_{1}$ and the fact that $X_{1}$ is not identically 0 , we conclude that $E\left(X_{1}\right)=\mu_{1} \neq 0$. Now we investigate some properties of the quasirenewal process.

Theorem 4.1 If $f_{1}(x)$ belongs to IFR, DFR, IFRA, DFRA, NBU, or NWU, then $f_{n}(x)$ is in the same category for $n=2,3, \ldots$

Proof. For mathematical definitions of the above terms: IFR, DFR, IFRA, DFRA, NBU, and NWU, see Appendix at the end of this chapter. Suppose that the failure rate of $X_{n}$ is differentiable with respect to time $x$. From Equation (4.1) the derivative of the failure rate of $X_{n}$ is given by

$$
r_{n}^{\prime}(x)=\frac{1}{\alpha^{2 n-2}} r_{1}^{\prime}\left(\frac{1}{\alpha^{n-1}} x\right)
$$

From the above equation we can see that if $r_{1}(x)$ is increasing (decreasing) then $r_{n}(x)$ is also increasing (decreasing). Therefore, for the first two categories: IFR or DFR, the conclusion follows.

Next assume that$$
s_{1}(x+y) \leq(\geq) s_{1}(x) s_{1}(y)
$$

Then it follows that

$$
\begin{aligned}
s_{n}(x+y) & =s_{1}\left(\frac{x+y}{\alpha^{n-1}}\right) \\
& \leq(\geq) s_{1}\left(\frac{x}{\alpha^{n-1}}\right) s_{1}\left(\frac{y}{\alpha^{n-1}}\right) \\
& =s_{n}(x) s_{n}(y)
\end{aligned}
$$

Therefore, if $s_{1}(x)$ is NBU (NWU) then $s_{n}(x)$ is also in the same category.
Finally, note that the derivatives with respect to $x$ :

$$
\begin{aligned}
{\left[s_{n}^{1 / x}(x)\right]_{x}^{\prime} } & =\left[\exp \left(\frac{1}{x} \ln s_{1}\left(\frac{x}{\alpha^{n-1}}\right)\right)\right]_{x}^{\prime} \\
& =-\frac{1}{\alpha^{2 n-2}} s_{1}^{1 / x}\left(\frac{x}{\alpha^{n-1}}\right)\left[\left(\frac{x}{\alpha^{n-1}}\right)^{-2} \ln s_{1}\left(\frac{x}{\alpha^{n-1}}\right)+\left(\frac{x}{\alpha^{n-1}}\right)^{-1} \frac{f_{1}\left(\alpha^{1-n} x\right)}{s_{1}\left(\alpha^{1-n} x\right)}\right]
\end{aligned}
$$

and

$$
\left[s_{1}^{1 / x}(x)\right]_{x}^{\prime}=-s_{1}^{1 / x}(x)\left[x^{-2} \ln s_{1}(x)+x^{-1} \frac{f_{1}(x)}{s_{1}(x)}\right]
$$

Note also that

$$
s_{1}^{1 / x}(x) \geq 0 \quad s_{1}^{1 / x}\left(\alpha^{1-n} x\right) \geq 0 \quad \text { for } x \geq 0
$$

From above it follows that, if $\left[s_{1}^{1 / x}(x)\right]_{x}^{\prime}$ is increasing or decreasing respectively, $\left[s_{n}^{1 / x}(x)\right]_{x}^{\prime}$ is also increasing or decreasing respectively. Thus, for the last two categories: NBU or NWU, the conclusion holds. This completes the proof of Theorem 4.1.

It is worthwhile to note that if $f_{1}(x)$ is NBUE or NWUE, then $f_{n}(x)$ may not be in the same category for $n=2,3, \ldots$

The following result is due to Wang and Pham (1996b):
Theorem 4.2 The shape parameter of random variable $X_{n}$ is the same, $\forall n, n=1,2,3, \ldots$ for a quasi-renewal process if $X_{1}$ follows the Gamma, Weibull or Lognormal distribution.

Remark. This means after "renewal" the shape parameters of the interarrival time will not be changed. In reliability theory, the shape parameters of a lifetime of a hardware product tend to relate to its failure mechanism and modes. Usually, if it possesses the same failure mechanism then a product will have the same shape parameters of its lifetimes at different environments. Therefore, the use of a quasi-renewal process is generally justified in the maintenance process of a hardware system and hardware burn-in stage.

It is worth noting that

$$
\lim _{n \rightarrow \infty} \frac{E\left(X_{1}+X_{2}+\cdots+X_{n}\right)}{n}=\lim _{n \rightarrow \infty} \frac{\mu_{1}\left(1-\alpha^{n}\right)}{(1-\alpha) n}= \begin{cases}0 & \text { when } \quad \alpha<1 \\ +\infty & \text { when } \quad \alpha>1\end{cases}
$$

Therefore, if the interarrival time represents the failure-free time of a hardware system with imperfect maintenance the average failure-free time goes to zero when the planning horizon is infinite. This is because the operating condition of the hardware system becomes generally worse and worse as time goes on if it is subject to imperfect maintenance. If the interarrival time represents the error-free time of a software system the average error-free time goes to infinity when its debugging process goes on for a very long time. This conclusion seems reasonable because the faults in the software become generally less and less when it is subject to testing and debugging. When the debugging time is infinite we can expect that there exist no faults with this software and thus average error-free time and the error-free time at the infinite time point is infinite.

# 4.1.2 Quasi-renewal Function 

Consider a quasi-renewal process with parameter $\alpha$ and the first interarrival time $X_{1}$. Clearly, the total number $N(t)$ of "renewals" that has occurred up to time $t$ and the arrival time of the $n^{\text {th }}$ renewal, $S S_{n}$, has the following relationship:

$$
N(t) \geq n \quad \Leftrightarrow \quad S S_{n} \leq t
$$

That is, $N(t)$ is at least $n$ if and only if the $n^{\text {th }}$ renewal occurs prior to or at time $t$. It is easily seen that

$$
S S_{n}=\sum_{i=1}^{n} X_{i}=\sum_{i=1}^{n} \alpha^{i-1} Z_{i} \quad n \geq 1
$$

Take

$$
S S_{0}=0
$$

Thus, we have

$$
\begin{aligned}
P\{N(t)=n\} & =P\{N(t) \geq n\}-P\{N(t) \geq n+1\} \\
& =P\left\{S S_{n} \leq t\right\}-P\left\{S S_{n+1} \leq t\right\} \\
& =G^{(n)}(t)-G^{(n+1)}(t)
\end{aligned}
$$

where $G^{(n)}(t)$ is the convolution of the interarrival times $F_{1}, F_{2}, \ldots, F_{n}$.
In Wang and Pham (1996b), the mean value of $N(t)$ is defined as the quasirenewal function $M(t)$. Therefore,$$
\begin{aligned}
M(t) & =E[N(t)] \\
& =\sum_{n=1}^{\infty} P\{N(t) \geq n\} \\
& =\sum_{n=1}^{\infty} P\left\{\mathrm{SS}_{n} \leq t\right\} \\
& =\sum_{n=1}^{\infty} G^{(n)}(t)
\end{aligned}
$$

The derivative of $M(t)$ is known as quasi-renewal density:

$$
m(t)=M^{\prime}(t)
$$

In renewal theory, random variables representing the interarrival distributions assume nonnegative values only, and the Laplace transform of distribution $F_{1}(t)$ is defined by

$$
\tilde{F}_{1}(s)=\int_{0}^{\infty} e^{-s s} d F_{1}(x)
$$

Thus,

$$
\begin{aligned}
\tilde{F}_{n}(s) & =\int_{0}^{\infty} e^{-\alpha^{n-1} s t} d F_{1}(t)=\widetilde{F}_{1}\left(\alpha^{n-1} s\right) \\
\tilde{M}(s) & =\sum_{n=1}^{\infty} \tilde{G}^{(n)}(s) \\
& =\sum_{n=1}^{\infty} \tilde{F}_{1}(s) \cdot \widetilde{F}_{1}(\alpha s) \cdots \widetilde{F}_{1}\left(\alpha^{n-1} s\right)
\end{aligned}
$$

Since there is a one-to-one correspondence between distribution functions and its Laplace transforms, it follows that:

THEOREM 4.3 The first interarrival distribution of a quasi-renewal process uniquely determines its quasi-renewal function.

In investigating optimal hardware replacement problem, Lam (1988) uses the fixed life reduction idea after repair, referred to as a geometric process. Lam (1988, 1996) studies the geometric process by means of the ordinary renewal process. As shown in this section, the quasi-renewal process is investigated from defining the quasi-renewal function, not from the ordinary renewal process.

# 4.1.3 Associated Statistical Testing Problems 

Ascher and Feingold (1984) observe that the interarrival times between successive failures of a deteriorating system tend to become smaller and smaller based on some actual examples. One of the actual examples is the average failure-free timelengths of some bus engines between successive failures: 9400, 7000, 5400, 4100, 3300 miles. In this example, there were 191 engines run to first failure and a sample size of approximately 100 was for each of the other four interarrival miles. Since the sample sizes are large there is overwhelming evidence that the miles between successive failures were decreasing (p.70, Ascher and Feingold 1984). Generally, whether decreases in failure-free times in maintenance processes have geometric reduction patterns needs statistical hypothesis testing. However, since there may not be many failure data available in practice, geometric decay of failure-free times implied by a quasi-renewal process is a good choice as it can, at least, approximate the failure process. Besides, the quasi-renewal process makes imperfect repair modeling mathematically tractable as it can be seen later in this chapter.

In the above example, the estimates of parameter $\alpha$ are respectively

$$
\begin{array}{ll}
\hat{\alpha}_{1}=7000 / 9400=.745 & \hat{\alpha}_{2}=5400 / 7000=.771 \\
\hat{\alpha}_{3}=4100 / 5400=.759 & \hat{\alpha}_{4}=3300 / 4100=.805
\end{array}
$$

which are very close to each other. Therefore, we have no strong evidence to reject the hypothesis

$$
\begin{aligned}
& H_{0}: \alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\alpha \\
& H_{a}: \alpha_{1}, \alpha_{2}, \alpha_{3} \text { and } \alpha_{4} \text { are not all equal }
\end{aligned}
$$

To discuss this problem further, assume that $n$ units operate at time zero independently with lifetimes $X_{1}^{1}, X_{1}^{2}, \ldots, X_{1}^{n}$, respectively. The times between failures for each of them are recorded as follows:

| To 1st failure | To 2nd failure |  | To $\left(m_{i}+1\right)^{\text {th }}$ failure |
| :--: | :--: | :--: | :--: |
| $x_{1}^{1}$ | $x_{2}^{1}$ | ... | $x_{m_{1}+1}^{1}$ |
| $x_{1}^{2}$ | $x_{2}^{2}$ | ... | $x_{m_{2}+1}^{2}$ |
| $\vdots$ | $\vdots$ |  | $\vdots$ |
| $x_{1}^{n}$ | $x_{2}^{n}$ | ... | $x_{m_{n}+1}^{n}$ |

where $x_{j}^{i}$ represents the lifetime of unit $i$ after the $(j-1)^{\text {th }}$ repair, and $i, j, n$ and $m_{i}$ are all integers.

From these data we can obtain the following estimates of parameter $\alpha$ :

$$
\begin{array}{llll}
\hat{\alpha}_{1}^{1} & \hat{\alpha}_{2}^{1} & \ldots & \hat{\alpha}_{m_{1}}^{1} \\
\hat{\alpha}_{1}^{2} & \hat{\alpha}_{2}^{2} & \ldots & \hat{\alpha}_{m_{2}}^{2} \\
& \vdots & & \\
\hat{\alpha}_{1}^{n} & \hat{\alpha}_{2}^{n} & \ldots & \hat{\alpha}_{m_{n}}^{n}
\end{array}
$$

where $\hat{\alpha}_{j}^{i}=x_{j+1}^{i} / x_{j}^{i}$.If $\alpha_{i}$ is the parameter related to the $(i-1)^{\text {th }}$ failure and the $i^{\text {th }}$ failure, the following hypothesis:

$$
\begin{aligned}
& H_{0}: \alpha_{1}=\alpha_{2}=\cdots=\alpha_{k}=\alpha \\
& H_{n}: \alpha_{1}, \alpha_{2}, \ldots, \text { and } \alpha_{k} \text { are not all equal }
\end{aligned}
$$

can be tested by Analysis of Variance (ANOVA) techniques with the normality assumption where $k=\max \left(m_{l} \mid l=1,2, \ldots, n\right)$. Note that this is generally an unbalanced experimental design. When $m_{1}=m_{2}=\cdots=m_{n}$ it becomes a balanced design. For pairwise comparisons, the pairwise $t$-test can be used. These techniques are available in standard textbooks on statistical design of experiments and so there will be no further discussion in this book. If we have no evidence to reject the null hypothesis then parameter $\alpha$ can be estimated by

$$
\hat{\alpha}=\frac{\sum_{j=1}^{m^{*}}\left(\sum_{i=1}^{n} \alpha_{j}^{i}\right) / n}{m^{*}}
$$

where $m^{*}=\min \left(m_{l} \mid l=1,2, \ldots, n\right)$
For other estimation methods of parameter $\alpha$, we refer to Wang and Pham (1996e) about acceleration factor estimation.

A quasi-renewal process may be characterized by several parameters, including $\alpha$. Their estimation can be carried out by using the maximum likelihood estimate (MLE). Assume that we observe one unit and its maintenance process follows a quasi-renewal process. Denote by $t_{i}$ the $i^{\text {th }}$ time to failure since the unit operate at time 0 . Assume that $0=t_{0}<t_{1} \cdots<t_{n}$. The likelihood function of this maintenance model is, noting Equation (4.1),

$$
\begin{aligned}
L\left(t_{1}, t_{2}, \ldots, t_{n}\right) & =\prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| f_{2}\left(t_{2}|\Theta| \cdots f_{n}\left(t_{n} \mid \Theta\right)\right.\right. \\
& =\prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| \alpha^{-1} f_{1}\left(\alpha^{-1} t_{2}|\Theta| \cdots \alpha^{1-n} f_{1}\left(\alpha^{1-n} t_{n} \mid \Theta\right)\right.\right. \\
& =\alpha^{-n(n-1) / 2} \prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| f_{1}\left(\alpha^{-1} t_{2}|\Theta| \cdots f_{1}\left(\alpha^{1-n} t_{n} \mid \Theta\right)\right.\right.
\end{aligned}
$$

where $\Theta$ represents the parameter family including parameter $\alpha$, specified by the parameter space $\Omega$.

From the above likelihood function, the parameters associated with the quasirenewal process can be estimated by the maximum likelihood method. For example, assume that the first failure time, $X_{1}$, of a new unit follows the normal distribution with mean $\mu$ and variance $\sigma^{2}$, that is

$$
f_{1}(x)=\sigma^{-1}(2 \pi)^{-\frac{1}{2}} e^{-(x-\mu)^{2} / 2 \sigma^{2}}
$$and that its maintenance process can be modeled by the quasi-renewal process. Given the observed failure times $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ we can estimate quasi-renewal process parameter $\alpha$ and normal distribution parameters $\mu$ and $\sigma$. The likelyhood function becomes

$$
\begin{aligned}
& L\left(t_{1}, t_{2}, \cdots, t_{n}\right)=\alpha^{-n(n-1) / 2} \frac{1}{(\sigma \sqrt{2 \pi})^{n}} \exp \left\{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(\alpha^{1-i} t_{i}-\mu\right)^{2}\right\} \quad \text { and } \\
& \ln L\left(t_{1}, t_{2}, \cdots, t_{n}\right)=-\frac{n(n-1)}{2} \ln \alpha-n \ln (\sigma \sqrt{2 \pi})-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(\alpha^{1-i} t_{i}-\mu\right)^{2}
\end{aligned}
$$

Taking derivatives of $\ln L$ with respect to $\alpha, \mu$ and $\sigma$ result in the MLE of parameters $\alpha, \mu$, and $\sigma$, which can be obtained by solving following simultaneous equations:

$$
\left\{\begin{aligned}
\tilde{\mu} & =\frac{1}{n} \sum_{i=1}^{n} \hat{\alpha}^{1-i} t_{i} \\
n & =\frac{1}{2 \hat{\sigma}^{2}} \sum_{i=1}^{n}\left(\hat{\alpha}^{1-i} t_{i}-\hat{\mu}\right)^{2} \\
\frac{n(n-1)}{2} & =\frac{1}{\hat{\sigma}^{2}} \sum_{i=1}^{n}\left(\hat{\alpha}^{1-i} t_{i}-\hat{\mu}\right) \frac{t_{i}}{\hat{\alpha}^{2 i-1}}
\end{aligned}\right.
$$

If failure times of many identical units are recorded, similar MLE procedure can be used to estimate the associated parameters.

It is noted that Whitaker and Samaniego (1989) discuss parameter estimation problems associated with the $(p, q)$ rule for the imperfect repair. It should be pointed out that statistical hypothesis testing and parameter estimation of maintenance models need more attention and study while most work on reliability and maintenance in the literature is focused on probabilistic modeling.

# 4.1.4 Truncated Quasi-renewal Processes 

Bai and Pham (2005) introduce the truncated quasi-renewal processes through omitting a range of possible values for the total number $N(t)$ of "renewals". As one can see in Section 10.3 of Chapter 10, truncated quasi-renewal processes arise naturally in warranty cost study for repairable products. There are also potential applications in reliability and maintenance modeling. Depending on the values omitted from a quasi-renewal process, there are three types of truncations: truncation above $m$, truncation below $m$, and double truncation, where $m$ is a fixed non-negative number. Here we focus on the discussion of truncation above $m$, which will be used in warranty cost models in Chapter 10.# Model I 

A quasi-renewal process truncated above $m$ means that for a given $t$, the total number of "renewals" $N(t)$ can only take values of $0,1, \cdots, m$. For such $N(t)$, let $P_{i}(t) \equiv P[N(t)=i]$. Assume that the probability law governing $P_{i}(t)$ does not change by the truncation, or in other words, all these probabilities $P_{i}(t)$ are standardized, then

$$
P_{i}(t)=\frac{G^{(i)}(t)-G^{(i+1)}(t)}{1-G^{(m+1)}(t)}, \quad \forall i, i=0,1, \cdots, m
$$

As a result, the first and second moments of $N(t)$ are given by

$$
\begin{aligned}
E[N(t)] & =\sum_{i=0}^{m} i\left[G^{(i)}(t)-G^{(i+1)}(t)\right] /\left[1-G^{(m+1)}(t)\right] \\
& =\frac{1}{1-G^{(m+1)}(t)}\left[\sum_{i=1}^{m} i G^{(i)}(t)-\sum_{j=2}^{m+1}(j-1) G^{(j)}(t)\right] \quad(\text { let } j=i+1) \\
& =\frac{1}{1-G^{(m+1)}(t)}\left[\sum_{i=1}^{m} i G^{(i)}(t)-\sum_{j=2}^{m+1} j G^{(j)}(t)+\sum_{j=2}^{m+1} G^{(j)}(t)\right] \\
& =\frac{\sum_{i=1}^{m+1} G^{(i)}(t)-(m+1) G^{(m+1)}(t)}{1-G^{(m+1)}(t)} \\
& =\frac{\sum_{i=1}^{m} G^{(i)}(t)-m G^{(m+1)}(t)}{1-G^{(m+1)}(t)}
\end{aligned}
$$

and

$$
\begin{aligned}
E\left[N^{2}(t)\right] & =\frac{1}{1-G^{(m+1)}(t)} \sum_{i=0}^{m} i^{2}\left[G^{(i)}(t)-G^{(i+1)}(t)\right] \\
& =\frac{1}{1-G^{(m+1)}(t)}\left[\sum_{i=1}^{m} i^{2} G^{(i)}(t)-\sum_{j=2}^{m+1}(j-1)^{2} G^{(j)}(t)\right] \quad(\text { let } j=i+1) \\
& =\frac{\sum_{i=1}^{m} i^{2} G^{(i)}(t)-\left(\sum_{j=2}^{m+1} j^{2} G^{(j)}(t)-\sum_{j=2}^{m+1} 2 j G^{(j)}(t)+\sum_{j=2}^{m+1} G^{(j)}(t)\right)}{1-G^{(m+1)}(t)} \\
& =\frac{\sum_{i=1}^{m+1}(2 i-1) G^{(i)}(t)-(m+1)^{2} G^{(m+1)}}{1-G^{(m+1)}(t)} \\
& =\frac{\sum_{i=1}^{m}(2 i-1) G^{(i)}(t)-m^{2} G^{(m+1)}(t)}{1-G^{(m+1)}(t)}
\end{aligned}
$$# Model II 

Sometimes truncation may change the relative magnitude of $P_{i}(t)$. In particular, let $N(t)$ be a quasi-renewal process truncated above $m$. Suppose that for $i \in\{0,1, \cdots, m-1\}, P_{i}(t)$ is the same for that without truncation, so for $i=m$, $P_{m}(t)=1-\sum_{j=0}^{m-1} P_{j}(t)$. That is:

$$
\begin{aligned}
& P_{i}(t)=G^{(i)}(t)-G^{(i+1)}(t), \quad \text { for } i=0,1, \cdots, m-1 \\
& P_{m}(t)=G^{(m)}(t)
\end{aligned}
$$

Consequently, the first and second moments of $N(t)$ are

$$
\begin{aligned}
E[N(t)] & =\sum_{i=0}^{m-1} i\left[G^{(i)}(t)-G^{(i+1)}(t)\right]+m G^{(m)}(t) \\
& =\sum_{i=1}^{m-1} i G^{(i)}(t)-\sum_{j=2}^{m}(j-1) G^{(j)}(t)+m G^{(m)}(t) \quad(\text { let } j=i+1) \\
& =\sum_{i=1}^{m} G^{(i)}(t)
\end{aligned}
$$

and

$$
\begin{aligned}
E\left[N^{2}(t)\right] & =\sum_{i=0}^{m-1} i^{2}\left[G^{(i)}(t)-G^{(i+1)}(t)\right]+m^{2} G^{(m)}(t) \\
& =\sum_{i=1}^{m-1} i^{2} G^{(i)}(t)-\sum_{j=2}^{m}(j-1)^{2} G^{(j)}(t)+m^{2} G^{(m)}(t) \quad(\text { let } j=i+1) \\
& =\sum_{i=1}^{m-1} i^{2} G^{(i)}(t)-\left(\sum_{j=2}^{m} j^{2} G^{(j)}(t)-\sum_{j=2}^{m} 2 j G^{(j)}(t)+\sum_{j=2}^{m} G^{(j)}(t)\right)+m^{2} G^{(m)}(t) \\
& =\sum_{i=1}^{m}(2 i-1) G^{(i)}(t)
\end{aligned}
$$

Chapter 10 will discuss modeling of warranty cost by using truncated quasirenewal processes.

The next three sections will model imperfect maintenance of a single-unit system by using the quasi-renewal process. The following three assumptions are made in this chapter:
i) A new unit begins to operate at time 0 .
ii) The failure rate $r_{1}(t)$ of the new unit is continuous and monotonously increasing and differentiable.
iii) $c d f F_{1}(t)$ of the unit is absolutely continuous and $F_{1}(0)=0$.# 4.2 Periodic PM with Imperfect Maintenance 

### 4.2.1 Model 1: Imperfect Repair and Perfect PM

Suppose that a unit is preventively maintained at times $T, 2 T, 3 T, \ldots$ at a cost $c_{p}$, independently of the unit's failure history where the constant $T>0$ and PM is perfect. The unit undergoes imperfect repair at failures between PMs at cost $c_{f}$ in the sense that upon each repair lifetime (random variable) will be reduced to a fraction $\alpha$ of its immediately previous one and all successive lifetimes are independent, i.e., the lifetimes follow a decreasing quasi-renewal process with parameter $\alpha$. Thus we can apply the quasi-renewal theory to model this maintenance process. We consider $T$ as a decision variable, $\alpha$ as a parameter in this section. The following result is from Wang and Pham (1996b):

Proposition 4.1 The long-run expected maintenance cost per unit time, or maintenance cost rate, is

$$
L(T ; \alpha)=\frac{c_{p}+c_{f} M(T)}{T}
$$

where $M(T)$ is the quasi-renewal function of a quasi-renewal process with parameter $\alpha$.

We can see the form of cost rate $L(T ; \alpha)$ is the same as the well-known result obtained from the ordinary renewal theory based on the perfect repair assumption (Barlow and Proschan, 1965). However, the renewal functions are different.

Proposition 4.2 There exists an optimum $T^{*}$ which minimizes $L(T ; \alpha)$ where $0<T^{*} \leq \infty$ and the resulting minimum value of $L(T ; \alpha)$ is $c_{f} m\left(T^{*}\right)$.

Proof. Note that $L(T ; \alpha)$ is continuous for $0<T<\infty$ because we assume that $F_{1}(t)$ is continuous. It is easy to see that $L(T, \alpha) \rightarrow \infty$ when $T \rightarrow 0$ from Equation (4.2). If we explain PM at interval $T=\infty$ as maintenance only at failure, i.e., no PM, it follows that $L(T ; \alpha)$ has a minimum for $0<T \leq \infty$. A necessary condition that a finite value $T^{*}$ minimizes $L(T ; \alpha)$ is that it must satisfy the following equation, obtained by differentiating $L(T ; \alpha)$ with respect to $T$ and setting the derivative equal to 0 :

$$
T^{*} m\left(T^{*}\right)-M\left(T^{*}\right)=c_{p} / c_{f}
$$

where $m(\cdot)$ is the renewal density. Substituting this equation into Equation (4.2) it follows that the minimum value of $L(T ; \alpha)$ is $c_{f} m\left(T^{*}\right)$.# 4.2.2 Model 2: Imperfect Repair and Imperfect PM 

This model is identical to Model 1 in Section 4.2.1 except that the unit is imperfectly preventively maintained at times $T, 2 T, 3 T, \ldots$ at a cost $c_{p}$ where the constant $T>0$. Imperfect PM is treated by the $(p, q)$ rule, that is, after PM the unit is 'as good as new' with probability $p$ and is restored to 'as bad as old' with probability $q=1-p$.

Proposition 4.3 The long-run expected maintenance cost per unit time, or cost rate, is

$$
L(T ; \alpha, p)=\frac{c_{p}+c_{f} p^{2}\left[M(T)+\sum_{i=2}^{\infty} q^{i-1} M(i T)\right]}{T}
$$

where $M(i T)$ is the quasi-renewal function of a quasi-renewal process with parameter $\alpha$.

Proof. For detailed proof, see Wang and Pham (1996b). The times between consecutive perfect PM constitute a renewal cycle. Note that the expected duration of a renewal cycle $D(T ; \alpha, p)$ is

$$
D(T ; \alpha, p)=\sum_{i=1}^{\infty} q^{i-1} p(i T)
$$

Equation (4.3) follows.
Note that if $p=1$ (corresponding to perfect PM), the above equation coincides with the result of Model 1. In this section $T$ is considered as a decision variable, $\alpha$ and $p$ are considered as parameters.

Proposition 4.4 There exists an optimum $T^{*}$ which minimizes $L(T ; \alpha, p)$ where $0<T^{*} \leq \infty$ and the resulting minimum value of expected cost rate $L(T ; \alpha, p)$ is $c_{f} p^{2} \sum_{i=1}^{n} q^{i-1}\left[i T^{*} m\left(i T^{*}\right)\right]$.

Proof. Note that $L(T ; \alpha, p)$ is continuous for $0<T<\infty$ because we assume that $F_{1}(t)$ is continuous and that $L(T ; \alpha, p) \rightarrow \infty$ as $T \rightarrow 0$ from Equation (4.3). If we explain PM at an interval $T=\infty$ as maintenance only at failure, that is, no PM, it follows that $L(T ; \alpha, p)$ has minimum for $0<T \leq \infty$.

A necessary condition that a finite value $T^{*}$ minimizes $L(T ; \alpha, p)$ is that it satisfies the following equation, from Wang and Pham (1996b):$$
\sum_{i=1}^{n} q^{i-1}\left[i T^{*} m\left(i T^{*}\right)-M\left(i T^{*}\right)\right]=c_{p} /\left(c_{f} p^{2}\right)
$$

From this it follows that the optimum maintenance cost rate $L(T ; \alpha, p)$ is $c_{f} p^{2} \sum_{i=1}^{n} q^{i-1}\left[i T^{*} m\left(i T^{*}\right)\right]$, where $m(\cdot)$ is the quasi-renewal density of the quasirenewal process.

# 4.2.3 Model 3: Imperfect Repair and Imperfect PM 

Assume that a unit start working at time 0 ; upon failure $i$ it is imperfectly repaired at a cost $c_{f}+(i-1) c_{v}$ if and only if $i \leq k-1$ where $i=1,2,3, \ldots, c_{f}$ and $c_{v}$ are fixed repair cost and incremental cost respectively. The repair is imperfect in the sense that upon each repair the time to failure will be reduced to a fraction $\alpha$ of its immediate predecessor and be independent of all previous ones; the repair time will increase to a multiple $\beta$ of its immediately previous one and be independent of all previous ones. In other words, the successive times to failure constitute a decreasing quasi-renewal process with parameter $\alpha$ and the successive repair times follow an increasing quasi-renewal process with parameter $\beta$. Notice that the repair cost increases by $c_{v}$ for each next imperfect repair. Boland and Proschan (1982) introduce this kind of increasing maintenance cost notation for minimal repair.

Given that the lifetime $X_{1}$ of the new unit and the first imperfect repair time $Y_{1}$ are independent random variables with means $\mu$ and $\eta$, respectively, and suppose that $Z_{i} \mathrm{~s}$ and $\zeta_{i} \mathrm{~s}$ are respectively i.i.d. random variable sequences. The lifetime of the unit upon the first imperfect repair and the second imperfect repair time will become respectively $\alpha Z_{1}$ with mean $\alpha \mu$ and $\beta \zeta_{1}$ with means $\beta \eta$, where the constant $\beta \geq 1$ means that the repair time is increasing as the number of imperfect repairs increases and $0<\alpha \leq 1$ means that the lifetime is decreased at each imperfect repair. Note that the lifetime of the unit upon the $(k-2)^{\text {th }}$ repair and the $(k-1)^{\text {th }}$ repair time are $\alpha^{k-2} Z_{k-1}$ and $\beta^{k-2} \zeta_{k-1}$ with means $\alpha^{k-2} \mu$ and $\beta^{k-2} \eta$ respectively.

After the $(k-1)^{\text {th }}$ imperfect repair at failure, the unit is imperfectly preventively maintained at times $T, 2 T, 3 T, \ldots$ at a cost $c_{p}$ (independently of the unit's failure history), and imperfect PM is treated by the $(p, q)$ rule. If there is a failure between PMs an imperfect repair is performed at a cost $c_{f r}$ with negligible repair time; and the repair is imperfect in the sense that upon each repair the lifetime of this unit will be reduced to a fraction $\lambda$ of its immediately previous one and the successive lifetimes are independent where $0<\lambda<1$, i.e., the lifetimes constitute a decreasing quasi-renewal process with parameter $\lambda$. This sectionconsiders the case that the PM time is a random variable $W$ with mean $w$. This maintenance process will repeat itself once a perfect PM is incurred.

One possible interpretation of this model is: when a new unit is put into operation, the first $(k-1)$ repairs at failures, because the unit is young at that time, will be performed at a low cost $c_{f}+(i-1) c_{v}$ for $i=1,2, \ldots k-1$, and the repairs turn out to be imperfect. Usually, these repairs are just minor repairs because the unit is in a good operating condition. For example, if a new car is put into use, it will be in a good operating state and should not need any major repairs for some short period, to say, in the first half year. After the $(k-1)^{\text {th }}$ imperfect (minor) repair at failure, this car will be in a bad condition and then a better or perfect (major) maintenance (preventive or unplanned, especially preventive) is necessary at a higher cost of $c_{p}$ or $c_{f r}$.

# 4.2.3.1 Maintenance Cost Rate and Availability 

The following result is due to Wang and Pham (1996b), and we provide it here without the proof.

Proposition 4.5 The long-run expected maintenance cost per unit time, or maintenance cost rate, is

$$
L(T, k ; \alpha, \beta, \lambda, p)=\frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} p^{-1}+p c_{f r} \sum_{i=1}^{\infty} q^{i-1} M(i T)}{%2C \frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w}
$$

and the asymptotic average availability is given by

$$
A(T, k ; \alpha, \beta, \lambda, p)=\frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{T}{p}}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w}
$$

where $M(t)$ is the quasi-renewal function of a quasi-renewal process with parameter $\lambda$ and the first interarrival time distribution $F_{1}\left(\alpha^{1-k} t\right)$.

In this section, $T$ and $k$ are decision variables; $\alpha, \beta, \lambda$ and $p$ are parameters. $C(T, k ; \alpha, \beta, \lambda, p)$ implies that the expected maintenance cost per renewal cycle $C$ is a function of variables $T$ and $k$ with parameters of $\alpha, \beta, \lambda$ and $p$. We will use similar notation throughout this book.

Wang and Pham (1996b) prove that a necessary condition that finite values $\left(T^{*}, k^{*}\right)$ minimize $L(T, k ; \alpha, \beta, p)$ is that they satisfy the following simultaneous equations:$$
\begin{aligned}
& {\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w\right] p c_{f r} \sum_{i=1}^{\infty} i q^{i-1} m(i T)-c_{f r} \sum_{i=1}^{\infty} q^{i-1} M(i T) } \\
& =(k-1) c_{f} p^{-1}+\frac{(k-1)(k-2)}{2} c_{v} p^{-1}+c_{p} p^{-2} \\
& {\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w\right]\left[c_{f}+\frac{(2 k-3)}{2} c_{v}\right]=\left[\frac{\mu \alpha^{k-1} \ln \alpha}{\alpha-1}-\frac{\eta \beta^{k-1} \ln \beta}{1-\beta}\right] } \\
& \times\left[(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} p^{-1}+p c_{f r} \sum_{i=1}^{\infty} q^{i-1} M(i T)\right]
\end{aligned}
$$

# 4.2.3.2 Optimization and Numerical Example 

Sometimes it may be required that while some reliability requirements are satisfied the optimum maintenance policy is obtained. For maintenance Model 3, noting the asymptotic average availability in Equation (4.5), the following optimization problem can be formulated in terms of decision variables $T$ and $k$ as well as parameters $\alpha, \beta$ and $p$ :

## Minimize

$$
L(T, k ; \alpha, \beta, p)=\frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} p^{-1}+p c_{f r} \sum_{i=1}^{\infty} q^{i-1} M(i T)}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w}
$$

## Subject to

$$
\left\{\begin{array}{l}
A(T, k ; \alpha, \beta, p)=\frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{T}{p}}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{T}{p}+w} \geq A_{0} \\
k=2,3, \ldots \\
T>0
\end{array}\right.
$$

where constant $A_{0}$ is the predetermined availability requirement.

Similarly, some other optimization models can be formulated and these models can be solved by using any nonlinear programming software. To illustrate the optimal maintenance model (4.6) we now present a numerical example. Note that the normal distribution is IFR. Assume that the lifetime, $X_{1}$, of a new unit follows the normal distribution with mean $\mu$ and variance $\sigma^{2}$. Then upon the $(k-1)^{\text {th }}$ imperfect repair at failure, the $p d f$ of the lifetime of this unit will become$f_{k}(x)=\alpha^{1-k} f_{1}\left(\alpha^{1-k} x\right)$. From Section 4.1.2, the quasi-renewal function of the quasi-renewal process with parameter $\lambda$ and the first interarrival time distribution $\alpha^{1-k} f_{1}\left(\alpha^{1-k} x\right)$ is

$$
M(t)=\sum_{n=1}^{\infty} G^{n}(t)
$$

It is easy to obtain that

$$
G^{(n)}(t)=P\left\{S S_{n} \leq t\right\}
$$

where random variable $S S_{n}$ follows the normal cumulative distribution function with mean $\mu \alpha^{k-1}\left(1-\lambda^{n}\right) /(1-\lambda)$ and variance $\sigma^{2} \alpha^{2 k-2}\left(1-\lambda^{2 n}\right) /\left(1-\lambda^{2}\right)$.
Therefore, the quasi-renewal function is given by

$$
M(t)=\sum_{n=1}^{\infty} P\left\{S S_{n} \leq t\right\}=\sum_{n=1}^{\infty} \Phi\left(\left[t-\frac{\mu \alpha^{k-1}\left(1-\lambda^{n}\right)}{1-\lambda}\right] / \sqrt{\frac{\sigma^{2} \alpha^{2 k-2}\left(1-\lambda^{2 n}\right)}{1-\lambda^{2}}}\right)
$$

where $\Phi(\cdot)$ is the standard normal $c d f$. Now assume that

$$
\begin{array}{rlrl}
\mu & =10 & \sigma=1 & \eta=0.9 \\
c_{f} & =\$ 1 & c_{p}=\$ 3 & c_{f r}=\$ 4 \\
\alpha & =.95 & \beta=1.05 & p=0.95 \\
w & =0.2 & \lambda=0.95 & A_{0}=0.94
\end{array}
$$

Substituting the above parameter values and the quasi-renewal function into the optimization model (4.6) yields:

# Minimize 

$$
\begin{aligned}
& L(T, k ; 0.95,1.05,0.95)= \\
& \frac{k+0.03(k-1)(k-2)+\frac{41}{19}+3.8 \sum_{i=1}^{n} 0.05^{i-1} \sum_{n=1}^{\infty} \Phi\left(\frac{i T-200 \times 0.95^{k-1}\left(1-0.95^{n}\right)}{\sqrt{\frac{0.95^{2 k-2}\left(1-0.95^{2 n}\right)}{0.0975}}}\right)}{200\left(1-0.95^{k-1}\right)+18\left(1.05^{k-1}-1\right)+\frac{T}{0.95}+0.2}
\end{aligned}
$$

## Subject to

$A(T, k ; 0.95,1.05,0.95)=\frac{200\left(1-0.95^{k-1}\right)+\frac{T}{0.95}}{200\left(1-0.95^{k-1}\right)+18\left(1.05^{k-1}-1\right)+\frac{T}{0.95}+0.2} \geq 0.94$
$k=2,3, \ldots$
$T>0$Various kinds of approximations for the standard normal $\Phi(\cdot)$ have been developed and a simple approximation with high accuracy is by Zelen and Severo (see Johnson and Kotz, 1970):

$$
\Phi(x) \approx 1-\left(0.4361836 t-0.1201676 t^{2}+0.9372980 t^{3}\right)(\sqrt{2 \pi})^{1} \exp \left(-\frac{1}{2} x^{2}\right)
$$

where $t=(1+0.33267 x)^{-1}$. The error in $\Phi(x)$, for $x \geq 0$, is less than $1 \times 10^{-5}$.
Note that $\Phi(x)=1-\Phi(-x)$. Thus, for $x<0$ we can use this relationship and Equation (4.7) to approximate $\Phi(x)$.

Using the above approximation and nonlinear integer programming software we can find the optimal solution $\left(T^{*}, k^{*}\right)$ that minimizes the maintenance cost rate given that the availability is at least 0.94 :

$$
T^{*}=7.6530 \quad k^{*}=3
$$

and the corresponding minimum cost rate and availability are respectively

$$
L\left(T^{*}, k^{*} ; 0.95,1.05,0.95\right)=\$ 0.2332 \quad A\left(T^{*}, k^{*} ; 0.95,1.05,0.95\right)=0.9426
$$

The results show that the optimal maintenance policy is to perform repair at the first two failures of the unit at a cost of $\$ 1$ and $\$ 1.06$ respectively, and then perform PM every 7.6530 time units at a cost of $\$ 3$ and repair the unit upon failure between PMs at a cost of $\$ 4$.

# 4.2.4 Model 4: Imperfect Repair and Imperfect PM 

In the periodic PM Model 3 in Section 4.2.3, if we further assume that after the first $(k-1)$ imperfect repairs the unit will be subject to imperfect PMs at times $T, 2 T, 3 T, \ldots$ and repairs at failure. The repair at failure is perfect and the corresponding repair time is a random variable $Q$ with mean $\eta_{2}$. The PM is imperfect in the sense that after PM the unit will be as good as new with probability $p_{1}$ and as bad as old with probability $p_{2}$ and will fail (worst repair) and need repair with probability $p_{3}$ where $p_{1}+p_{2}+p_{3}=1$. Let us further assume that the perfect and worst PM times have means $\eta_{4}$ and $\eta_{5}$ respectively and the repair time upon failure caused by PM is a random variable $V$ with mean $\eta_{3}$. The reason that PM may result in a unit failure is stated in Nakagawa (1987) and Chapter 1 of this book.

According to the ordinary renewal reward theory, the limiting average availability $A$ is

$$
A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)=\frac{U\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)}{U\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)+D\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)}
$$

where $U\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ and $D\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ are the accumulating failure-free time and repair time in one renewal cycle. It is easy to obtain$$
\begin{aligned}
U\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right) & = \\
& \frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\left[\int_{0}^{T} t d F_{1}\left(\alpha^{1-k} t\right)+p_{2} \int_{T}^{2 T} t d F_{1}\left(\alpha^{1-k} t\right)+p_{2}^{2} \int_{2 T}^{3 T} t d F_{1}\left(\alpha^{1-k} t\right)+\cdots\right] \\
& +\left(p_{1}+p_{3}\right)\left[T \cdot s\left(\alpha^{1-k} T\right)+2 T \cdot p_{2} \cdot s\left(2 \alpha^{1-k} T\right)+3 T \cdot p_{2} \cdot s\left(3 \alpha^{1-k} T\right)+\cdots\right] \\
& =\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t \\
D\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)= & \frac{\eta_{1}\left(1-\beta^{k-1}\right)}{1-\beta}+\left(\eta_{3}+\eta_{5}\right) p_{3} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right) \\
& +\eta_{2}\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} F_{1}\left(\alpha^{1-k} i T\right)+\eta_{4} p_{1} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)
\end{aligned}
$$

Now let

$$
\begin{aligned}
& C L\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)=U\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)+D\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right) \\
& =\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta_{1}\left(1-\beta^{k-1}\right)}{1-\beta}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t \\
& +\left(\eta_{3}+\eta_{5}\right) p_{3} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)+\eta_{2}\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} F_{1}\left(\alpha^{1-k} i T\right) \\
& +\eta_{4} p_{1} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)
\end{aligned}
$$

Proposition 4.6 The unit's asymptotic average availability is

$$
A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)=\frac{\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t}{C L\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)}
$$

In this section, $T$ and $k$ are decision variables; $\alpha, \beta, p_{1}, p_{2}$ and $p_{3}$ are parameters. From Equation (4.8) we can see that $A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ is uniquely determined by variables $T$ and $k$ as well as parameters $\alpha, \beta, p_{1}, p_{2}$ and $p_{3}$. The optimal $T$ and $k$ which maximizes $A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ satisfies the following simultaneous equations if they exist:

$$
\begin{aligned}
& {\left[\left(1-p_{2}\right) \sum_{i=1}^{\infty} i p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)\right] \times\left[\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta_{1}\left(1-\beta^{k-1}\right)}{1-\beta}\right.} \\
& +\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t+\left(\eta_{3}+\eta_{5}\right) p_{3} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right) \\
& \left.+\eta_{2}\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} F_{1}\left(\alpha^{1-k} i T\right)+\eta_{4} p_{1} \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)\right]
\end{aligned}
$$$$
\begin{gathered}
-\left[\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t\right] \times \\
\left\{\sum_{i=1}^{\infty} i p_{2}^{i-1}\left[\left(1-p_{2}\right) s_{1}\left(\alpha^{1-k} i T\right)+\alpha^{1-k} f_{1}\left(\alpha^{1-k} i T\right)\left(\eta_{2}\left(1-p_{2}\right)-\left(\eta_{3}+\eta_{5}\right) p_{3}-\eta_{4} p_{1}\right)\right]\right\}=0
\end{gathered}
$$

and

$$
\begin{aligned}
& {\left[-\frac{\mu_{1} \alpha^{k-1} \ln \alpha}{1-\alpha}-\left(1-p_{2}\right) \alpha^{1-k} \ln \alpha \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} t f_{1}\left(\alpha^{1-k} t\right) d t\right]} \\
& \times\left[\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta_{1}\left(1-\beta^{k-1}\right)}{1-\beta}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t\right. \\
& \left.+\left(\left(\eta_{3}+\eta_{5}\right) p_{3}+\eta_{4} p\right) \sum_{i=1}^{\infty} p_{2}^{i-1} s_{1}\left(\alpha^{1-k} i T\right)+\eta_{2}\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} F_{1}\left(\alpha^{1-k} i T\right)\right]- \\
& {\left[\frac{\mu_{1}\left(1-\alpha^{k-1}\right)}{1-\alpha}+\left(1-p_{2}\right) \sum_{i=1}^{\infty} p_{2}^{i-1} \int_{0}^{i T} s_{1}\left(\alpha^{1-k} t\right) d t\right] \times\left\{-\frac{\mu_{1} \alpha^{k-1} \ln \alpha}{1-\alpha}-\frac{\eta_{1} \beta^{k-1} \ln \beta}{1-\beta}+\right.} \\
& \left.\sum_{i=1}^{\infty}\left[\left(p_{2}-1\right) \int_{0}^{i T} t f_{1}\left(\alpha^{1-k} t\right) d t+i T \alpha^{1-k} f_{1}\left(\alpha^{1-k} i T\right)\left(\eta_{2}\left(1-p_{2}\right)-\left(\eta_{3}+\eta_{5}\right) p_{3}-\eta_{4} p_{1}\right)\right]\right\} \\
& \times p_{2}^{i-1} \alpha^{1-k} \ln \alpha=0
\end{aligned}
$$

The above two equations are obtained by differentiating asymptotic average availability $A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ with respect to $T$ and $k$ respectively, and setting the derivatives equal to 0 . Note that $k$ is an integer and is regarded as a real number temporarily when differentiating $A\left(T, k ; \alpha, \beta, p_{1}, p_{2}, p_{3}\right)$ with respect to $k$. Note also that $\alpha, \beta, p_{1}, p_{2}$ and $p_{3}$ are all parameters.

# 4.2.5 Model 5: Imperfect Repair and Imperfect PM 

This model is exactly like Model 3 in Section 4.2.3 except that the imperfect PM is treated by the $x$ rule, i.e., the age of the unit becomes $x$ units of time younger upon PM (see Chapter 2); that the unit undergoes minimal repair at failures between PMs at cost $c_{f m}$ instead of imperfect repairs in terms of parameter $\lambda$ in Model 3. Assume that the $N^{\text {th }} \mathrm{PM}$ since the last perfect PM is perfect, where $N$ is a positive integer. A cost $c_{N p}$ and an independent replacement time $V$ with mean $v$ is suffered for the perfect PM at time $N T$. Given that imperfect PM at other times takes $W$ time with mean $w$ and imperfect PM cost is $c_{p}$. Suppose that $c_{N p}>c_{p}, v \geq w$, and $W$ and $V$ are independent of the previous failure history of the unit.

Proposition 4.7 The long-run expected maintenance cost per unit time is$$
\begin{aligned}
& L(T, k, N ; \alpha, \beta, p)= \\
& \frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{N p}+c_{p}(N-1)+c_{\beta n} \sum_{i=0}^{N-1} \int_{i(T-x)}^{T+i(T-x)} r\left(\alpha^{1-k} t\right) d t}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+N T+v+(N-1) w}
\end{aligned}
$$

and the asymptotic average availability is

$$
A(T, k, N ; \alpha, \beta, p)=\frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+N T}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+N T+v+(N-1) w}
$$

Proof. The times between consecutive perfect maintenance constitute a renewal cycle. From the classical renewal reward theory we have:

$$
\begin{aligned}
& L(T, k, N ; \alpha, \beta, p)=\frac{C(T, k, N ; \alpha, \beta, p)}{D(T, k, N ; \alpha, \beta, p)} \\
& A(T, k, N ; \alpha, \beta, p)=\frac{U(T, k, N ; \alpha, \beta, p)}{D(T, k, N ; \alpha, \beta, p)}
\end{aligned}
$$

where $C(T, k, N ; \alpha, \beta, p)$ is the expected maintenance cost per renewal cycle, $U(T, k, N ; \alpha, \beta, p)$ is the accumulated operating time in a renewal cycle, and $D(T, k, N ; \alpha, \beta, p)$ is the expected duration of a renewal cycle. Following Wang and Pham (1996c),

$$
\begin{aligned}
C(T, k, N ; \alpha, \beta, p) & =c_{f}+\cdots+\left[c_{f}+(k-2) c_{v}\right]+c_{N p}+c_{p}(N-1) \\
& +c_{\beta n} \sum_{i=0}^{N-1} \int_{i(T-x)}^{T+i(T-x)} r\left(\alpha^{1-k} t\right) d t \\
& =(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{N p}+c_{p}(N-1) \\
& +c_{\beta n} \sum_{i=0}^{N-1} \int_{i(T-x)}^{T+i(T-x)} r\left(\alpha^{1-k} t\right) d t \\
D(T, k, N ; \alpha, \beta, p) & =E\left[\sum_{i=1}^{k-1}\left(\alpha^{i-1} X_{1}+\beta^{i-1} Y_{1}\right)\right]+[N T+v+(N-1) w] \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+N T+v+(N-1) w \\
U(T, k, N ; \alpha, \beta, p) & =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+N T
\end{aligned}
$$

Hence, Proposition 4.7 follows.In this section, $T, k$ and $N$ are decision variables; $\alpha, \beta$ and $p$ are parameters. From Equation (4.9) we can see that maintenance cost rate $L$ and availability $A$ are uniquely determined by variables $T, k$ and $N$ as well as parameters $\alpha, \beta$ and $p$. From Proposition 4.7, the optimum solution $\left(T^{*}, k^{*}, N^{*}\right)$ which minimizes $L(T, k, N ; \alpha, \beta, p)$ or maximizes $A(T, k, N ; \alpha, \beta, p)$ or optimizes both can be obtained by using a nonlinear integer programming software.

# 4.2.6 Model 6: Imperfect Repair and Imperfect PM 

Model 6 is identical to Model 3 in Section 4.2.3 except that upon the $(k-1)^{\text {th }}$ imperfect repair we assume that there are two types of failures (see Beichelt 1980, 1981), and that PMs at times $T, 2 T, 3 T, \ldots$ are perfect. Type 1 failure might be total breakdowns while Type 2 failure can be interpreted as a slight and easily fixed problem. Type 1 failures are subject to perfect repairs and Type 2 failures are subject to minimal repairs. When a failure occurs it is a Type 1 failure with probability $p(t)$ and a Type 2 failure with probability $q(t)=1-p(t)$ where $t$ is the age of the unit. Thus, the repair at failure can be modeled by the $(p(t), q(t))$ rule described in Chapter 2. Assume that the failure repair time is negligible, and PM time is a random variable $V$ with mean $v$.

Consider $T$ and $k$ as decision variables in this section. For this maintenance model, the times between consecutive perfect PMs constitute a renewal cycle. The long-run expected maintenance cost per system time, or cost rate, is

$$
L(T, k)=\frac{C(T, k)}{D(T, k)}
$$

where $C(T, k)$ is the expected maintenance cost per renewal cycle and $D(T, k)$ is the expected duration of a renewal cycle.

After the $(k-1)^{\text {th }}$ imperfect repair, let $Y_{p}$ denote the time until the first perfect repair without PM since last perfect repair, i.e., the time between successive perfect repairs. As mentioned in Chapter 2 the survival distribution of $Y_{p}$ is given by

$$
\begin{aligned}
\bar{S}(t) & =\exp \left\{-\int_{0}^{t} p(x) r_{k}(x) d x\right\} \\
& =\exp \left\{-\alpha^{1-k} \int_{0}^{t} p(x) r\left(\alpha^{1-k} x\right) d x\right\}
\end{aligned}
$$

which is proved in Block et al. (1985) and NAPS 03476-A, and utilized in Beichelt (1980, 1981a) and Sheu et al. (1995). Block et al. (1985) further prove that $\bar{S}(t)$ has IFR if $r(t)$ is IFR.

Assume that $Z_{t}$ represents the number of minimal repairs during the time interval $\left(0, \min \left\{t, Y_{p}\right\}\right)$ and $S(t)=1-\bar{S}(t)$. Using the results shown in NAPS 03476-A and used in Beichelt (1981a), we have that:$$
\begin{aligned}
E\left\{Z_{t} \mid Y_{p}<t\right\} & =\frac{1}{S(t)} \int_{0}^{t} \int_{0}^{y} q(x) \cdot r_{k}(x) \cdot d x \cdot d S(y) \\
& =\frac{\alpha^{1-k}}{S(t)} \int_{0}^{t} \int_{0}^{y} q(x) r_{1}\left(\alpha^{1-k} x\right) d x d S(y) \\
E\left\{Z_{t} \mid Y_{p} \geq t\right\} & =\int_{0}^{t} q(x) \cdot r_{k}(x) \cdot d x \\
& =\alpha^{1-k} \int_{0}^{t} q(x) r_{1}\left(\alpha^{1-k} x\right) d x
\end{aligned}
$$

Let $N_{1}(t)$ and $N_{2}(t)$ denote s-expected number of perfect repairs and minimal repairs in $(0, t)$ respectively; $c_{1}, c_{2}$, and $c_{p}$ denote costs of perfect repair, minimal repair, and PM, respectively. Wang and Pham (1999) obtain

$$
\begin{gathered}
D(T, k)=\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+T+v \\
C(T, k)=(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{1} N_{1}(T)+c_{2} N_{2}(T)+c_{p}
\end{gathered}
$$

Obviously, $N_{1}(t)$ is the renewal function for the renewal process with the interarrival time distribution $S(t)$ and can be determined by the solution method to the renewal function in renewal theory. According to Beichelt (1981a), we have for $t \leq T$,

$$
N_{2}(t)=E\left\{Z_{t} \mid Y_{p} \geq t\right\} \cdot \bar{S}(t)+\int_{0}^{t}\left\{E\left\{Z_{x} \mid Y_{p}=x\right\}+N_{2}(t-x)\right\} d S(x)
$$

Note that $E\left\{Z_{t} \mid Y_{p}<t\right\} \cdot S(t)=\int_{0}^{t} E\left\{Z_{x} \mid Y_{p}=x\right\} d S(x)$ and Equations (4.11) and (4.12). It follows that

$$
\begin{aligned}
N_{2}(t) & =E\left\{Z_{t} \mid Y_{p} \geq t\right\} \cdot \bar{S}(t)+E\left\{Z_{t} \mid Y_{p}<t\right\} S(t)+\int_{0}^{t} N_{2}(t-x) d S(t) \\
& =E\left(Z_{t}\right)+\int_{0}^{t} N_{2}(t-x) d S(t) \\
& =\alpha^{1-k} \int_{0}^{t} \bar{S}(t) r_{1}\left(\alpha^{1-k} x\right) d x-S(t)+\int_{0}^{t} N_{2}(t-x) d S(t)
\end{aligned}
$$

Therefore, $N_{2}(t)$ can be obtained by the Laplace transform or by solving the integral Equation (4.15) using numerical computation. Substituting Equations (4.13) and (4.14) into Equation (4.10), it follows that:

Proposition 4.8 The long-run expected maintenance cost rate is given by$$
L(T, k)=\frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{1} N_{1}(T)+c_{2} N_{2}(T)+c_{p}}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+T+v}
$$

Again, the optimal maintenance policy $\left(T^{*}, k^{*}\right)$ to minimize the expected cost rate can be obtained from Equation (4.16) in the same manner as in Section 4.2.3.

# 4.3 Cost Limit Replacement Policy - Model 7 

This model is the same as Model 3 in Section 4.2.3 except that at next failures after the $(k-1)^{\text {th }}$ imperfect repair since time zero, repair cost is estimated by perfect inspection to determine whether to replace or imperfectly repair it. Assume that the repair cost has a cumulative distribution function $C(x)$ which is independent of the age of the unit. If the estimated cost does not exceed a constant cost limit $Q$, then this unit is imperfectly repaired at an expected repair cost not exceeding $Q$. Otherwise, it is replaced by a new one at a higher fixed cost $c_{2}$ and the replacement time is $W$ with mean $w$. Imperfect repair is modeled by the $(p, q)$ rule. Given that the repair time is $V$ with mean $v$, and that $W$ and $V$ are independent of the previous failure history of the unit. Upon a perfect repair or replacement the process repeats.

This section considers $k$ and $Q$ as decision variables, and $\alpha, \beta$ and $p$ as parameters.

Proposition 4.9 The long-run expected maintenance cost per unit time is

$$
\begin{aligned}
& L(k, Q ; \alpha, \beta, p)= \\
& \qquad \begin{aligned}
(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+\frac{c_{2}[1-C(Q)]+\bar{c}_{1} C(Q)}{1-p C(Q)} \\
\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{[1-C(Q)] w+p C(Q) v}{1-q C(Q)}+\int_{0}^{\infty} \exp \left\{-H\left(\alpha^{1-k} t\right)[1-q C(Q)]\right\} d t
\end{aligned}
\end{aligned}
$$

and the asymptotic average availability is

$$
\begin{aligned}
& A(k, Q ; \alpha, \beta, p)= \\
& \frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\int_{0}^{\infty} \exp \left\{-H\left(\alpha^{1-k} t\right)[1-q C(Q)]\right\} d t}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{[1-C(Q)] w+p C(Q) v}{1-q C(Q)}+\int_{0}^{\infty} \exp \left\{-H\left(\alpha^{1-k} t\right)[1-q C(Q)]\right\} d t}
\end{aligned}
$$

where $H\left(\alpha^{1-k} t\right)=\int_{0}^{t} \alpha^{1-k} r_{1}\left(\alpha^{1-k} x\right) d x$ is the cumulative hazard of the unit right afterthe $(k-1)^{t h}$ imperfect repair and $\bar{c}_{1}=C^{-1}(Q) \int_{0}^{L} t d C(t)$ is the mean of repair costs less than $Q$.

Proof. The times between consecutive perfect maintenance, either replacement or perfect repair, constitute a renewal cycle. From the classical renewal reward theory we have

$$
\begin{aligned}
L(k, Q ; \alpha, \beta, p) & =\frac{C(k, Q ; \alpha, \beta, p)}{D(k, Q ; \alpha, \beta, p)} \\
A(k, L ; \alpha, \beta) & =\frac{U(k, Q ; \alpha, \beta, p)}{D(k, Q ; \alpha, \beta, p)}
\end{aligned}
$$

where $C(k, Q ; \alpha, \beta, p)$ is the expected maintenance cost per renewal cycle, $U(k, Q ; \alpha, \beta, p)$ is the accumulated operating time in a renewal cycle, and $D(k, Q ; \alpha, \beta, p)$ is the expected duration of a renewal cycle. Denote by $Z_{0}, Z_{1}, Z_{2}, \ldots$, the failure times of the unit before a replacement or a perfect repair where $Z_{0}=0$. Wang and Pham (1996c) show

$$
\begin{aligned}
C(k, Q ; \alpha, \beta, p) & =(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v} \\
& +\sum_{i=1}^{\infty}\left\{q^{i-1} p[C(Q)]^{i} i \bar{c}_{1}+[C(Q)]^{i-1}[1-C(Q)] q^{i-1}\left[(i-1) \bar{c}_{1}+c_{2}\right]\right\} \\
& =(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+\frac{c_{2}[1-C(Q)]+\bar{c}_{1} C(Q)}{1-p C(Q)} \\
D(k, Q ; \alpha, \beta, p)= & \frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta} \\
& +\sum_{i=1}^{\infty}[q C(Q)]^{i-1}\left\{[1-C(Q)]\left[E\left(Z_{i}+W\right)\right]+p C(Q)\left[E\left(Z_{i}+V\right)\right]\right\} \\
U(Q, k ; \alpha, \beta, p)= & \frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\sum_{i=1}^{\infty}[q C(Q)]^{i-1}[1-C(Q)+C(Q) p] E\left(Z_{i}\right)
\end{aligned}
$$

Noting the results of Nakagawa and Kowada (1983):

$$
E\left(Z_{i}\right)=\sum_{n=0}^{i-1} \int_{0}^{\infty} H\left(\alpha^{1-k} t\right)^{n} e^{-H\left(\alpha^{1-k} t\right)} / n!\quad \forall i, i=1,2,3, \ldots
$$

it follows that

$$
D(k, Q ; \alpha, \beta, p)=\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k}\right)}{1-\beta}+\frac{[1-C(Q)] w+p C(Q) v}{1-q C(Q)}
$$$$
\begin{aligned}
& +\sum_{i=1}^{\infty}[q C(Q)]^{i-1}[1-C(Q)+p C(Q)] E\left(Z_{i}\right) \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{[1-C(Q)] w+p C(Q) v}{1-q C(Q)} \\
& +[1-q C(Q)] \sum_{t=1}^{\infty}[q C(Q)]^{i-1} \sum_{n=0}^{i-1} \int_{0}^{\infty} H\left(\alpha^{1-k} t\right)^{n} e^{-H\left(\alpha^{1-k} t\right)} / n!d t \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\frac{[1-C(Q)] w+p C(Q) v}{1-q C(Q)} \\
& +\int_{0}^{\infty} \exp \left\{-H\left(\alpha^{1-k} t\right)[1-q C(Q)]\right\} d t \\
& U(k, Q ; \alpha, \beta, p)=\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\int_{0}^{\infty} \exp \left\{-H\left(\alpha^{1-k} t\right)[1-q C(Q)]\right\} d t
\end{aligned}
$$

Proposition 4.9 follows from the above equations.
The optimum maintenance policy $\left(k^{*}, Q^{*}\right)$ which minimizes $L(k, Q ; \alpha, \beta, p)$ or maximizes $A(k, Q ; \alpha, \beta, p)$ can be obtained using any nonlinear programming software.

# 4.4 Age-dependent PM Policies with Imperfect Maintenance 

### 4.4.1 Model 8: Imperfect Repair

The model in this section is identical to Model 3 in Section 4.2.3 except that after the $(k-1)^{\text {th }}$ repair at failure the unit will be either replaced at next failure at a cost of $c_{f r}$, or preventively replaced at age $T$ at a cost $c_{p}$, whichever occurs first. That is, after time zero a unit is imperfectly repaired at failure $i$ at a cost $c_{f}+(i-1) c_{v}$ for $i \leq k-1$ where $c_{f}$ and $c_{v}$ are constants. The repair is imperfect in the sense that upon each repair the lifetime will be reduced to a fraction $\alpha$ of the immediate previous lifetime, and the repair time will be increased to a multiple $\beta$ of the immediately previous one, and the successive lifetimes and repair times are independent. In other words, the successive times to failure constitute a decreasing quasi-renewal process with parameter $\alpha$ and the successive repair times form an increasing quasi-renewal process with parameter $\beta$. Note that the lifetime of the unit after the $(k-2)^{\text {th }}$ repair and the $(k-1)^{\text {th }}$ repair time are $\alpha^{k-2} Z_{k-1}$ and$\beta^{k-2} \zeta_{k-1}$ with means $\alpha^{k-2} \mu$ and $\beta^{k-2} \eta$ respectively, where $Z_{i} \mathrm{~s}$ and $\zeta_{i} \mathrm{~s}$ are i.i.d. random variable sequences respectively.

Similar to Model 3, one possible interpretation of this model is: when a new system is put into operation, the first $(k-1)$ repairs at failures, because the system is young at that time, will be performed at low cost $c_{f}+(i-1) c_{v}$, and the repairs turn out to be imperfect. Usually, these repairs are just minor repairs because the system is in a good operating state. After the first $(k-1)$ repairs at failures, the system will be in a worse operating condition and a perfect maintenance, especially a PM, is necessary at a higher cost.

We consider $T$ and $k$ as decision variables, $\alpha$ and $\beta$ as parameters.

# 4.4.1.1 Cost Rate 

Proposition 4.10 The long-run expected maintenance cost per unit time, or maintenance cost rate is

$$
L(T, k ; \alpha, \beta)=\frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot s_{1}\left(\alpha^{1-k} T\right)+c_{f r} \cdot F_{1}\left(\alpha^{1-k} T\right)}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\alpha^{1-k} x\right) d x}
$$

Proof. The times between consecutive perfect maintenances, preventive or unscheduled at failure, constitute a renewal cycle. From the ordinary renewal reward theory we have

$$
L(T, k ; \alpha, \beta)=\frac{C(T, k ; \alpha, \beta)}{D(T, k ; \alpha, \beta)}
$$

where $C(T, k ; \alpha, \beta)$ is the expected total maintenance cost per renewal cycle and $D(T, k ; \alpha, \beta)$ is the expected duration of a renewal cycle.

Wang and Pham (1996a) show

$$
\begin{aligned}
C(T, k ; \alpha, \beta) & =c_{f}+\left(c_{f}+c_{v}\right)+\cdots+\left[c_{f}+(k-2) c_{v}\right]+c_{p} \cdot s_{1}\left(\frac{1}{\alpha^{k-1}} T\right) \\
& +c_{f r} \cdot F_{1}\left(\frac{1}{\alpha^{k-1}} T\right) \\
& =(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot s_{1}\left(\frac{1}{\alpha^{k-1}} T\right)+c_{f r} \cdot F_{1}\left(\frac{1}{\alpha^{k-1}} T\right)
\end{aligned}
$$

and

$$
\begin{aligned}
D(T, k ; \alpha, \beta) & =E\left[\sum_{i=1}^{k-1}\left(\alpha^{i-1} X_{1}+\beta^{i-1} Y_{1}\right)\right]+T \cdot s_{1}\left(\frac{1}{\alpha^{k-1}} T\right)+\alpha^{1-k} \int_{0}^{T} f_{1}\left(\frac{1}{\alpha^{k-1}} x\right) d x \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\frac{1}{\alpha^{k-1}} x\right) d x
\end{aligned}
$$

From them Proposition 4.10 follows.Let

$$
M(T)=r_{1}\left(\alpha^{1-k} T\right) \alpha^{1-k}\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\alpha^{1-k} x\right) d x\right]-F_{1}\left(\alpha^{1-k} T\right)
$$

and

$$
E=\left[(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p}\right] /\left(c_{f r}-c_{p}\right)
$$

We now determine the optimum maintenance policies that minimize the expected maintenance cost rate. The result is summarized in Proposition 4.11.

Proposition 4.11 For a fixed value of $k$, an optimum value of PM time $T$, say $T^{*}$, to minimize the maintenance cost rate exists, and is perhaps infinite, if

$$
M(0) \leq E
$$

if $r_{1}(t)$ is continuous and strictly increasing to infinity and Inequality (4.19) is satisfied, the optimal solution $T^{*}$ is unique and finite, given by

$$
T^{*}=M^{-1}(E)
$$

where $M^{-1}(E)$ is the inverse function of $M(T)$; if $M(0)>E$ the optimal solution is $T^{*}=0^{+}$.

Proof. Following Wang and Pham (1996c), the derivative of $L(T, k ; \alpha, \beta)$ with respect to $T$ is given by

$$
\begin{aligned}
\frac{\partial L(T, k ; \alpha, \beta)}{\partial T}= & r_{1}\left(\alpha^{1-k} T\right) \alpha^{1-k}\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\alpha^{1-k} x\right) d x\right] \\
& -F_{1}\left(\alpha^{1-k} T\right)-\left[(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p}\right] /\left(c_{f r}-c_{p}\right) \\
= & M(T)-E
\end{aligned}
$$

where $r_{1}(t)$ represents the failure rate of a new component.
A necessary condition for $T^{*}$ to minimize $L(T, k ; \alpha, \beta)$ can be obtained by setting the derivative of $L(T, k ; \alpha, \beta)$ with respect to $T$ equal to zero:

$$
M(T)-E=0
$$

The derivative of $M(T)$ is

$$
\frac{d M(T)}{d T}=r_{1}^{\prime}\left(\alpha^{1-k} T\right) \alpha^{2-2 k}\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\alpha^{1-k} x\right) d x\right]
$$Since $r_{\mathrm{i}}(t)$ is continuous and increasing, $M(T)$ is also continuous and increasing in $T$. Note also that $M(0) \geq 0$. Thus, there exists a unique and finite solution for Equation (4.21) only if $r_{\mathrm{i}}(t)$ is strictly increasing to infinity and Inequality (4.19) is satisfied. If Inequality (4.19) is satisfied and $r_{\mathrm{i}}(t)$ is increasing, a solution to Equation (4.20) exists, and is perhaps infinite. If $M(0)>E$ there is a unique optimal solution:

$$
T^{*}=\lim _{\substack{T \rightarrow 0 \\ T>0}} T=0^{*}
$$

since we assume that $T>0$. Therefore, Proposition 4.11 follows.
When repair number $k$ and the PM interval $T$ are both decision variables, we can find the optimal values for $k$ and $T$ by solving the following simultaneous equations if they exist and $k$ is taken as a real number temporarily:

$$
\frac{\partial \mathcal{L}(T, k ; \alpha, \beta)}{\partial T}=0 \quad \frac{\partial \mathcal{L}(T, k ; \alpha, \beta)}{\partial k}=0
$$

That is,

$$
\begin{aligned}
& {\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} s_{1}\left(\frac{1}{\alpha^{k-1}} x\right) d x\right]} \\
& \quad \times\left[c_{f}+\left(k-\frac{3}{2}\right) c_{v}+\left(c_{p}-c_{f r}\right) T \alpha^{1-k} f_{1}\left(\alpha^{1-k} T\right) \ln \alpha\right] \\
& =\left[(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot s_{1}\left(\frac{1}{\alpha^{k-1}} T\right)+c_{f r} \cdot F_{1}\left(\frac{1}{\alpha^{k-1}} T\right)\right] \times \\
& \quad\left[-\frac{\mu \alpha^{k-1} \ln \alpha}{1-\alpha}-\frac{\eta \beta^{k-1} \ln \beta}{1-\beta}+\alpha^{1-k} \ln \alpha \int_{0}^{T} x f_{1}\left(\alpha^{1-k} x\right) d x\right]
\end{aligned}
$$

and Equation (4.21). One can determine the optimal values for $T$ and $k$ from Equations (4.21) and (4.22) by numerical computation methods. Note that $k$ is taken as a real number in Equation (4.21) but the final optimal $k$ value should be rounded to an integer.

# 4.4.1.2 Numerical Example 

This section illustrates the results from Section 4.4.1.1 by a numerical example. Given the lifetime of a unit follows the Weibull distribution with a scale parameter $\lambda=1$ and a shape parameter $\theta=2$, that is, $F_{1}(t)=1-e^{-(\lambda t)^{\beta}}=1-e^{-t^{2}}$. The other parameters are (Wang 1997)

$$
\begin{array}{rlrl}
c_{f} & =\$ 1 & c_{v}=\$ 0.06 & c_{p}=\$ 4 & c_{f r}=\$ 12 \\
\alpha & =0.95 & \beta=1.05 & \eta=0.03
\end{array}
$$

Then the mean life of this unit is$$
\mu=\frac{1}{\lambda} \Gamma\left(\frac{1}{\theta}+1\right)=\Gamma(1.5)=0.88623 \text { time unit }
$$

Substituting the above parameters into Equation (4.18) we obtain

$$
L(T, k ; \alpha, \beta)=\frac{(k-1)(\underline{k-2})}{2} \cdot 0.06-8 \cdot \exp \left[-\left(0.95^{1-k} T\right)^{2}\right]+12}{\frac{0.88623 \cdot\left(1-0.95^{k-1}\right)}{1-0.95}+\frac{0.03 \cdot\left(1.05^{k-1}-1\right)}{1.05-1}+\int_{0}^{T} \exp \left[-\left(0.95^{1-k} x\right)^{2}\right] d x}
$$

Using nonlinear integer programming software, an optimum maintenance policy to minimize the maintenance cost rate can be found to be

$$
k^{*}=9 \quad T^{*}=0.0599
$$

and the corresponding optimal maintenance cost rate is

$$
L(0.0599,9 ; 0.95,1.05)=\$ 2.178 \text { per unit time }
$$

This result indicates that the optimal maintenance policy for Model 8 is that the first eight failures of the unit will be imperfectly repaired at low costs, and after the eighth repair at failures the unit will be either preventively replaced at the age of 0.0599 time units at a cost of $\$ 4$ or replaced at next failure at a cost of $\$ 12$, whichever occurs first.

Table 4.1. Optimal maintenance policies for Model 8

| Parameter(s) Changed | $L\left(k^{*}, T^{*}\right)$ | $k^{*}$ | $T^{*}$ |  |
| :--: | :--: | :--: | :--: | :--: |
| $\beta=1.1$ | $c_{f r}=8$ | 2.148 | 9 | 0.1182 |
| $c_{V}=0.1$ | $c_{f r}=8$ | 2.311 | 7 | 0.1561 |
| $c_{p}=6$ | $c_{f r}=8$ | 2.450 | 10 | 0.2433 |
| $c_{p}=2$ | $c_{f r}=8$ | 1.801 | 6 | 0.0899 |

If $c_{p}$ is changed to $\$ 8$ from $\$ 4$ and the other parameters are kept unchanged, then the optimal solution is

$$
L\left(k^{*}, T^{*}\right)=2.742 \quad k^{*}=11 \quad T^{*}=0.1229
$$

Similarly, we can change other parameters and leave the remaining unchanged, and compute the corresponding optimal solutions as shown in Table 4.1. Note that the failure rate of the unit $r_{\mathrm{i}}(t)=\theta \lambda(\lambda t)^{\theta-1}=2 t$ is continuous and strictly increasing to infinity. From Table 4.1 we can see that for these situations the optimum solutions always exist and they are finite and unique.# 4.4.2 Model 9: Imperfect CM and Imperfect PM 

This model is exactly like Model 8 in Section 4.4.1 except that since the $(k-1)^{\text {th }}$ repair at failure the unit will be imperfectly maintained at age $T$ at a cost $c_{p}$ or perfectly repaired at next failure at a cost $c_{f r}$, whichever occurs first. The imperfect PM is treated by the $(p, q)$ rule. In practice, after the $(k-1)$ minor repairs, although a PM is expected to be perfect it turns out to be not perfect due to maintenance cost and maintenance performers, etc. Hence, PMs are imperfect generally. Note that perfect PM is an extreme type of imperfect PM as discussed in Chapter 2 .

Considering $T$ and $k$ as decision variables, $\alpha, \beta$ and $p$ as parameters in this section, we have the following proposition:

Proposition 4.12 The long-run expected maintenance cost per unit time is

$$
\begin{aligned}
& L(T, k ; \alpha, \beta, p)= \\
& \frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \sum_{i=1}^{\infty} q^{i-1} s_{1}\left(i \alpha^{1-k} T\right)+c_{f r}\left[1-p \sum_{j=1}^{\infty} q^{j-1} s_{1}\left(j \alpha^{1-k} T\right)\right]}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\sum_{i=1}^{\infty} q^{i-1} \int_{(i-1) T}^{i T} s_{1}\left(\alpha^{1-k} x\right) d x}
\end{aligned}
$$

Proof. See Wang and Pham (1996a) for proof. The key point of the proof is that $\sum_{i=1}^{\infty} q^{i-1} s_{1}\left(i \alpha^{1-k} T\right)$ and $\left[1-p \sum_{j=1}^{\infty} q^{j-1} s_{1}\left(j \alpha^{1-k} T\right)\right]$ are the probabilities that PM and CM (repair) occur, respectively, in a renewal cycle (note that a renewal cycle may end with a perfect PM or a CM). For example, $q \cdot s_{1}\left(2 \alpha^{1-k} T\right)$ represents the probability that the unit has never failed in the interval $(0,2 T)$ and the first PM turns out to be not perfect (with probability $q$ ).

When $p=1$, i.e., PM is perfect, Proposition 4.12 becomes identical to Proposition 4.10.

It is important to determine $k$ and $T$ which minimize the expected maintenance cost rate. The optimal values for $k$ and $T$ can be obtained by differentiating $L(T, k ; \alpha, \beta, p)$ with respect to $T$ and $k$ and setting them equal to zero respectively if they exist. Wang and Pham (1996a) prove that the optimum solution $(T, k)$ satisfies the following two simultaneous equations:

$$
\begin{aligned}
& \left\{\left(-c_{p}+p c_{f r}\right) \alpha^{1-k} \sum_{i=1}^{\infty} i q^{i-1} f_{1}\left(\frac{i}{\alpha^{k-1}} T\right)\right\} \\
& \times\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\sum_{i=1}^{\infty} q^{i-1} \int_{(i-1) T}^{i T} s_{1}\left(\frac{x}{\alpha^{k-1}}\right) d x\right] \\
& -\left\{(k-1)\left(c_{f}+\frac{(k-2)}{2} c_{v}\right)+c_{p} \sum_{i=1}^{\infty} q^{i-1} s_{1}\left(\frac{i T}{\alpha^{i-1}}\right)+c_{f r}\left[1-p \sum_{j=1}^{\infty} q^{j-1} s_{1}\left(\frac{j T}{\alpha^{i-1}}\right)\right]\right\}
\end{aligned}
$$$$
\times\left[\sum_{i=1}^{\infty} q^{i-1}\left[i \cdot s_{1}\left(\alpha^{1-k} i T\right)-(i-1) \cdot s_{1}\left(\frac{i-1}{\alpha^{i-1}} T\right)\right]\right]=0
$$

and

$$
\begin{aligned}
& {\left[c_{f}+\frac{2 k-3}{2} c_{v}+\left(c_{p}-p c_{f r}\right) \alpha^{1-k} T \ln \alpha \sum_{i=1}^{\infty} q^{i-1} f_{1}\left(\frac{i T}{\alpha^{i-1}}\right)\right] } \\
& \times\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\sum_{i=1}^{\infty} q^{i-1} \int_{(i-1) T}^{i T} s_{1}\left(\frac{1}{\alpha^{i-1}} x\right) d x\right]- \\
& \left\{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \sum_{i=1}^{\infty} q^{i-1} s_{1}\left(i \frac{1}{\alpha^{i-1}} T\right)+c_{f r}\left[1-p \sum_{i=1}^{\infty} q^{j-1} s_{1}\left(i \frac{1}{\alpha^{i-1}} T\right)\right]\right\} \\
& \times\left[-\frac{\mu \alpha^{k-1} \ln \alpha}{1-\alpha}-\frac{\eta \beta^{k-1} \ln \beta}{1-\beta}+\alpha^{1-k} \ln \alpha \sum_{i=1}^{\infty} q^{i-1} \int_{(i-1) T}^{i T} x f_{1}\left(\frac{1}{\alpha^{i-1}} x\right) d x\right]=0
\end{aligned}
$$

One can determine the optimal values for $T$ and $k$ from the above two equations by numerical computation methods and nonlinear programming software. Note that $k$ is taken as a real number in the above equations but the final optimal $k$ value should be rounded to an integer.

# 4.4.3 Model 10: Two Imperfect Repairs 

This model is the same as Model 8 in Section 4.4.1 except that since the $(k-1)^{\text {th }}$ repair at failure the unit will be perfectly maintained at age $T$ at a cost $c_{p}$, or imperfectly repaired at next failure at a cost $c_{f r}$, whichever occurs first. The imperfect repair is modeled by the $(p, q)$ rule. If the repair is perfect, the next PM with the same cost $c_{p}$ will be rescheduled at a time $T$ since this perfect repair. If the repair is minimal, the unit is put back into operation and continues to operate until receiving a perfect maintenance, corrective or preventive.

We consider $T$ and $k$ as decision variables, $\alpha, \beta$ and $p$ as parameters in this section.

Proposition 4.13 The long-run expected maintenance cost per unit time is

$$
\begin{aligned}
& L(T, k ; \alpha, \beta, p)= \\
& \frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+c_{f r} \cdot\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} / p}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t}
\end{aligned}
$$

Proof. From renewal reward theory,$$
L(T, k ; \alpha, \beta, p)=\frac{C(T, k ; \alpha, \beta, p)}{D(T, k ; \alpha, \beta, p)}
$$

where $C(T, k ; \alpha, \beta, p)$ is expected total maintenance cost per renewal cycle (until a perfect repair or perfect PM) and $D(T, k ; \alpha, \beta, p)$ is the mean length of a renewal cycle. As mentioned in Chapter 2, Brown and Proschan (1983) prove that without PM the survival function of the time between successive perfect repairs of a unit is

$$
\bar{F}_{p}(t)=\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p}
$$

if its $p d f$ is $F_{1}\left(\alpha^{1-k} t\right)$ and imperfect repair is modeled by the $(p, q)$ rule. Hence

$$
\begin{aligned}
D(T, k ; \alpha, \beta, p) & =\mu+\eta+\alpha \mu+\beta \eta+\cdots+\alpha^{k-2} \mu+\beta^{k-2} \eta+\int_{0}^{T} \bar{F}_{p}(t) d t \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t
\end{aligned}
$$

The expected cost per renewal cycle is

$$
C(T, k ; \alpha, \beta, p)=c_{f}+\left(c_{f}+c_{v}\right)+\cdots+\left[c_{f}+(k-2) c_{v}\right]+C_{1}
$$

Using Lemma 2.1 of Fontenot and Proschan (1984), it follows that

$$
C_{1}=c_{f r} \int_{0}^{T}[1+q R(t)] d F_{p}(t)+\left[c_{f r} q R(T)+c_{p}\right] \bar{F}_{p}(T)
$$

where $R(t)=\int_{0}^{t} \alpha^{1-k} r_{1}\left(\alpha^{1-k} x\right) d x=-\ln \bar{F}_{p}(t) / p$ and $\bar{F}_{p}(t)=1-F_{p}(t)$.
Substituting $C_{1}$ into the $C(T, k ; \alpha, \beta, p)$ expression it follows that

$$
\begin{aligned}
C(T, k ; \alpha, p) & =(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v} \\
& +c_{f r}^{T}\left[\left[1-q \ln \bar{F}_{p}(t) / p\right] d F_{p}(t)+\left[c_{f r} q R(T)+c_{p}\right] \bar{F}_{p}(T)\right. \\
& =\left.(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+c_{f r} \cdot\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} / p\right.
\end{aligned}
$$

From which we obtain the expression for $L(T, k ; \alpha, \beta, p)$.

Proposition 4.14 For a fixed $k$ value, the following conclusions hold regarding the optimum solution $T^{*}$, which minimizes the maintenance cost rate:
(a) The optimal age $T^{*}$ is infinite if $c_{f r}<p c_{p}$
(b) An optimal age $T^{*}$ exists if $c_{f r}>p c_{p}$ and$$
\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}\right]\left[r_{1}(0) \alpha^{1-k}\right]\left(c_{f r}-p c_{p}\right)<\left(c_{f r}+(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}\right)
$$

(c) The equation $\frac{\partial L(T, k ; \alpha, p)}{\partial T}=0$ has at most one solution. If a solution exists it must be an optimal solution.
(d) There is a finite unique optimal solution if $c_{f r}>p c_{p}$ and the condition (4.23) is satisfied as well as

$$
r_{1}(\infty)>\frac{c_{f r}+p(k-1) c_{f}+\frac{(k-1)(k-2)}{2} p c_{v}}{p\left(c_{f r}-p c_{p}\right) \alpha^{1-k}\left[\int_{0}^{\infty} s_{1}^{p}\left(\alpha^{1-k} t\right) d t+\frac{\mu\left(1-\alpha^{k-1}\right)}{(1-\alpha)}+\frac{\eta\left(1-\beta^{k-1}\right)}{(1-\beta)}\right]}
$$

Proof. Differentiating $L(T, k ; \alpha, \beta, p)$ with respect to $T$ yields

$$
\begin{aligned}
\frac{\partial L}{\partial T} & =\left(\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t\right)^{-2} \\
& \times\left\{\left\{\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left(s_{1}\left(\alpha^{1-k} t\right)\right)^{p} d t\right]\right.\right. \\
& \times\left[r_{1}\left(\alpha^{1-k} T\right) \alpha^{1-k}\right]+\frac{\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}}{p}\left\{\left(c_{f r}-p c_{p}\right)-\frac{c_{f r}}{p}-(k-1) c_{f}-\frac{(k-1)(k-2)}{2} c_{v}\right\} \\
& \times\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}
\end{aligned}
$$

from which using the methods similar to Fontenot and Proschan (1984) and Section 4.4.1 we can see that for fixed $k$ :
(a) If $c_{f r}<p c_{p}$ then $\frac{\partial L(T, k ; \alpha, \beta, p)}{\partial T}<0$, i.e., the maintenance cost rate function $L$ is decreasing. Hence, the optimal age $T^{*}=\infty$.
(b) Let

$$
\begin{aligned}
E=\left\{\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left(s_{1}\right.\right. & \left.\left(\alpha^{1-k} t\right)\right)^{p} d t\left]\left[r_{1}\left(\alpha^{1-k} T\right) \alpha^{1-k}\right]+\frac{\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}}{p}\right\} \\
& \times\left(c_{f r}-p c_{p}\right)-\frac{c_{f r}}{p}-(k-1) c_{f}-\frac{(k-1)(k-2)}{2} c_{v}
\end{aligned}
$$

It is easy to verify that:$\frac{d E}{d T}=\left(c_{f r}-p c_{p}\right)\left[r_{1}^{s}\left(\alpha^{1-k} T\right) \alpha^{2-2 k}\right]\left[\int_{0}^{T}\left(s_{1}\left(\alpha^{1-k} t\right)\right)^{p} d t+\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}\right]>0$
Note that $\frac{\partial L(0, k ; \alpha, \beta, p)}{\partial T}<0$ when the condition (4.23) is satisfied. Therefore, if $\frac{\partial L(T, k ; \alpha, p)}{\partial T}=0$ has a solution $T^{*}$ then $\frac{\partial L(T, k ; \alpha, p)}{\partial T}>0$ in the interval $\left(T^{*}, \infty\right)$ and there is an optimal age $T^{*}$. If $\frac{\partial L(T, k ; \alpha, p)}{\partial T}=0$ has no solution then $\frac{\partial L(T, k ; \alpha, p)}{\partial T}<0$ and the optimal age $T^{*}$ is $\infty$.
(c) From the proof of (b) it is easy to draw such a conclusion.
(d) Note that at this time there is a finite unique $T^{*}$, which makes

$$
\begin{array}{ll}
\frac{\partial L(T, k ; \alpha, p)}{\partial T}<0 & \text { when } 0<T<T^{*} \\
\frac{\partial L(T, k ; \alpha, p)}{\partial T}>0 & \text { when } T^{*}<T<\infty
\end{array}
$$

Then the conclusion follows.
If $k$ is also regarded as a decision variable, differentiating $L(T, k ; \alpha, p)$ with respect to $k$ results in

$$
\begin{aligned}
& \frac{\partial L}{\partial k}=\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t\right]^{-2}\left\{\left[c_{f}+\left(k-\frac{3}{2}\right) c_{v}+r_{1}\left(\alpha^{1-k} T\right)\right.\right. \\
& \cdot\left(p c_{p}-c_{f r}\right) T\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p} \frac{1}{\alpha^{k-1}} \ln \alpha\left[\left[\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t\right]\right. \\
& -\left\{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{f r} / p+\left(c_{p}-c_{f r} / p\right) \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} \\
& \left.\left.\times\left[\frac{-\mu \alpha^{k-1} \ln \alpha}{1-\alpha}+\frac{-\eta \beta^{k-1} \ln \beta}{1-\beta}+p \alpha^{1-k} \ln \alpha \int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p-1} f_{1}\left(\alpha^{1-k} t\right) t d t\right]\right\}
\end{aligned}
$$

The optimal solution in terms of $k$ and $T$ which minimizes $L(T, k ; \alpha, p)$ satisfies the following simultaneous equations if it exists:

$$
\frac{\partial L(T, k ; \alpha, p)}{\partial T}=0 \quad \text { and } \quad \frac{\partial L(T, k ; \alpha, p)}{\partial k}=0
$$

# 4.4.4 Model 10a: Two Imperfect Repairs Considering Repair Time 

Assume that in the maintenance Model 10 in Section 4.4.3 the PM time duration is a random variable $W$ with mean $w$, and the duration of perfect repair time at failureis a random variable $V$ with mean $v$. The duration of minimal repair time at failure is negligible because it is smaller than perfect repair duration generally.

# 4.4.4.1 Cost Rate and Availability 

Proposition 4.15 The maintenance cost rate is given by

$$
\begin{aligned}
& L(T, k ; \alpha, \beta, p)= \\
& \quad \frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+c_{f r} \cdot\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} / p}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t+(w-v)\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+v}
\end{aligned}
$$

and the asymptotic average availability is

$$
\begin{aligned}
& A(T, k ; \alpha, \beta, p)= \\
& \frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t+(w-v)\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+v}
\end{aligned}
$$

Proof. From renewal reward theory,

$$
\begin{aligned}
& L(T, k ; \alpha, \beta, p)=\frac{C(T, k ; \alpha, \beta, p)}{D(T, k ; \alpha, \beta, p)} \\
& A(T, k ; \alpha, \beta, p)=\frac{U(T, k ; \alpha, \beta, p)}{D(T, k ; \alpha, \beta, p)}
\end{aligned}
$$

It is easy to verify that

$$
\begin{aligned}
D(T, k ; \alpha, \beta, p)= & \mu+\eta+\alpha \mu+\beta \eta+\cdots+\alpha^{k-2} \mu+\beta \eta^{k-2} \\
& +\int_{0}^{T} \bar{F}_{p}(t) d t+w \bar{F}_{p}(T)+v\left[1-\bar{F}_{p}(T)\right] \\
= & \frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta} \\
& +\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t+w\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+v\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} \\
C(T, k ; \alpha, \beta, p)= & (k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p} \\
& +c_{f r} \cdot\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} / p
\end{aligned}
$$$$
\begin{aligned}
U(T, k ; \alpha, \beta, p) & =\mu+\alpha \mu+\cdots+\alpha^{k-2} \mu+\int_{0}^{T} \bar{F}_{p}(t) d t \\
& =\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t
\end{aligned}
$$

From them the expressions for cost rate and the availability follow.

# 4.4.4.2 Optimal Maintenance Policies 

As noted in Chapter 3, sometimes it may be required that when some availability requirements are satisfied the optimum maintenance policy is attained or when some maintenance cost requirements are satisfied the optimum reliability measures are attained. For the maintenance model in Section 4.4.4.1, the following optimization problem can be formulated:

## Minimize

$$
\begin{aligned}
& L(T, k ; \alpha, \beta, p)= \\
& \qquad \frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{p} \cdot\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+c_{f r} \cdot\left\{1-\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}\right\} / p}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t+(w-v)\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+v}
\end{aligned}
$$

## Subject to

$$
\begin{aligned}
& A(T, k ; \alpha, \beta, p)= \\
& \frac{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T}\left[s_{1}\left(\alpha^{1-k} t\right)\right]^{p} d t+(w-v)\left[s_{1}\left(\alpha^{1-k} T\right)\right]^{p}+v}
\end{aligned}
$$

where constant $A_{0}$ is the specified availability requirements, $T>0$, and $k=2,3, \ldots$

### 4.4.5 Model 11: Imperfect Repair and Perfect PM

For periodic maintenance Model 6 in Section 4.2.6 we now assume that after the first $(k-1)$ imperfect repairs the system will be subject to a perfect maintenance at age $T(T>0)$ or at the first Type 1 failure, whichever occurs first. This process continues in infinite time horizon. That is, after the $(k-1)^{\text {th }}$ imperfect repair the system is subject to a perfect PM whenever it reaches age $T$. Otherwise, there are no PMs and after Type 1 failure the system age is set to zero and is counted again. When a failure after the first $(k-1)$ imperfect repairs occurs it is a Type 1 failure with probability $p(t)$ and a Type 2 failure with probability $q(t)=1-p(t)$. Type 2 failure is subject to minimal repair. Suppose that the minimal repair time is negligible, perfect maintenance (corrective or preventive) time is a random variable $Q$ with mean $\tau$.We consider $T$ and $k$ as decision variables, $\alpha, \beta$ and $p$ as parameters in this section. For this maintenance model, the times between consecutive perfect maintenance, corrective or preventive, constitute a renewal cycle. The long-run expected maintenance cost per system time, or cost rate, is

$$
L(T, k)=\frac{C(T, k)}{D(T, k)}
$$

Wang and Pham (1999) obtain

$$
D(T, k)=\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{\tau} \bar{S}(t) d t+\tau
$$

Note the derivation of Equation.(4.15). It follows that

$$
\begin{aligned}
C(T, k)= & (k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v} \\
& +\left[c_{2} E\left(Z_{T} \mid Y_{p}<T\right)+c_{1}\right] S(T)+\left[c_{2} E\left(Z_{T} \mid Y_{p} \geq T\right)+c_{p}\right] \bar{S}(T) \\
= & (k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{1} S(T) \\
& +c_{2}\left[E\left(Z_{T} \mid Y_{p}<T\right) S(T)+E\left(Z_{T} \mid Y_{p} \geq T\right) \bar{S}(T)\right]+c_{p} \bar{S}(T) \\
= & (k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v} \\
& +c_{2}\left[\alpha^{1-k} \int_{0}^{T} \bar{S}(x) r\left(\alpha^{1-k} x\right) d x-S(T)\right]+c_{1} S(T)+c_{p} \bar{S}(T) \\
= & (k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v} \\
& +c_{2}\left[\alpha^{1-k} \int_{0}^{T} \bar{S}(x) r\left(\alpha^{1-k} x\right) d x\right]+\left(c_{1}-c_{2}\right) S(T)+c_{p} \bar{S}(T)
\end{aligned}
$$

Substituting Equations (4.27) and (4.28) into Equation (4.26), we have:
Proposition 4.16 The long-run expected maintenance cost rate is given by
$L(T, k)=$

$$
\frac{(k-1) c_{f}+\frac{(k-1)(k-2)}{2} c_{v}+c_{2}\left[\alpha^{1-k} \int_{0}^{T} \bar{S}(x) r\left(\alpha^{1-k} x\right) d x\right]+\left(c_{1}-c_{2}\right) S(T)+c_{p} \bar{S}(T)}{\frac{\mu\left(1-\alpha^{k-1}\right)}{1-\alpha}+\frac{\eta\left(1-\beta^{k-1}\right)}{1-\beta}+\int_{0}^{T} \bar{S}(t) d t+\tau}
$$

The optimal maintenance policy $\left(T^{*}, k^{*}\right)$ to minimize the expected cost rate can also be determined from Equation (4.29) using a nonlinear integer programming software.# 4.5 Concluding Discussions 

All imperfect maintenance models in this chapter are based on the quasi-renewal process: successive operating times of a system are independent and decreasing by a fraction $(1-\alpha)$, and successive maintenance times are independent and increasing by a fraction $(\beta-1)$, or alternatively, upon each repair the time to failure will be reduced to a fraction $\alpha$ of the immediately previous one and be independent of all previous ones and the repair time will be increased to a multiple $\beta$ of the immediately previous one and be independent of all the previous ones. In other words, the successive times to failure form a decreasing quasi-renewal process with parameter $\alpha$, and the successive maintenance times constitute an increasing quasi-renewal process with parameter $\beta$. One can see that most results obtained in this chapter are in closed forms. Based on these results the optimal maintenance policies can be easily obtained by using any nonlinear programming software. Therefore, the quasi-renewal process is effective to treat hardware imperfect maintenance.

For most technical systems, such as cars or refrigerators, when a new one is put into use, it will be in a good operating state and may not need major repairs at the beginning period. After a period of operating, to say, after a certain number of imperfect (usually minor) repairs at failure the system will be in a worse operating condition and then a better or perfect maintenance (preventive or unplanned, especially preventive) is necessary at a higher cost to bring the system to a better operating condition with higher reliability. Therefore, the imperfect maintenance models discussed in this chapter will be practical in reliability and maintenance practice.

## Appendix

Assume that a unit has a distribution function $F(t)$ and survival function $s(t)=1-F(t)$ with mean $\mu$. We have the following definitions (For details see Barlow and Proschan 1965):

- $\quad s$ is NBU if $s(x+y) \leq s(x) \cdot s(y)$ for all $x, y \geq 0$.
$s$ is NWU if $s(x+y) \geq s(x) \cdot s(y)$ for all $x, y \geq 0$.
- $\quad s$ is NBUE if $\int_{t}^{\infty} s(x) d x \leq \mu s(t)$ for all $t \geq 0$.
$s$ is NWUE if $\int_{t}^{\infty} s(x) d x \geq \mu s(t)$ for all $t \geq 0$.
- $\quad s$ is IFRA if $[s(x)]^{1 / x}$ is decreasing in $x$ for $x \geq 0$.
$s$ is DFRA if $[s(x)]^{1 / x}$ is increasing in $x$ for $x \geq 0$.- $s$ is IFR if and only if $[F(t+x)-F(t)] / s(t)$ is increasing in $t$ for $x \geq 0$.
$s$ is DFR if and only if $[F(t+x)-F(t)] / s(t)$ is decreasing in $t$ for $x \geq 0$.
- Minimal repair: restore the system to its condition just prior to failure, i.e., if a system fails at age $t$ and undergoes minimal repair, then the repaired system has survival function $s^{\prime}(x)=s(x+t) / s(t)$.# Reliability and Optimal Maintenance of Series Systems with Imperfect Repair and Dependence 

The series system is one of the most important and common systems in reliability theory and applications. This chapter discusses availability, maintenance cost, and optimal maintenance policies of the series system with $n$ constituting components under the general assumption that each component is subject to correlated failure and repair, imperfect repair, and arbitrary distributions of times to failure and to repair under shut-off rules. Imperfect repair is modeled through quasi-renewal processes: the successive times to failure form a decreasing quasi-renewal process and the successive repair times constitute an increasing quasi-renewal process. System availability, mean time between system failures, mean time between system repairs, asymptotic fractional down time of the system, etc., are derived, and a numerical example is presented to compare with the models by Barlow and Proschan (1975). Then two classes of maintenance cost models are proposed, and system maintenance cost rates are modeled. Finally, properties of system availability and maintenance cost rates are studied. Optimization models to optimize system availability and/or system maintenance costs are furnished, and optimum system maintenance policies are discussed through a numerical example.

### 5.1 Introduction

In reliability engineering the series system is an important system as most systems in practice can be regarded or simplified as series systems. Its reliability, availability and maintenance have been studied in the reliability literature. Barlow and Proschan (1975) study the availability of the series system assuming that the repair at failure is perfect. Zhao (1994) extends their availability results to a general repair case. Schneeweiss (2005) investigates the availability of series systems without aging during repairs, proving the steady-state availability of a series-system with no aging of components during the repair of another one can be interpreted as a conditional probability of the well-known $s$-independent case conditioned on allowing for at most one failed component at any time. Trivially,this conditional probability is larger than the standard probability, i.e., the product of all components' probabilities (Pham 2003a). Blumenthal et al. (1976) discuss the transient reliability behavior of series system. Khalil (1985) investigates some shut-off rules for the series system. Wang and Pham (2006) study availability measures, maintenance cost modeling and optimal maintenance policies of series systems whose components are subject to imperfect repair as well as correlated failure and repair. This chapter introduces their work in which imperfect CM is modeled in a way that after repair the lifetime of each component will decrease to a fraction of its preceding one, and the repair time will increase to a multiple of its preceding one, given all lifetimes are independent and so are all repair times. In other words, the successive times to failure constitute a decreasing quasi-renewal process with parameter $\alpha$ and the successive repair times form an increasing quasirenewal process with parameter $\beta$. The correlated failure and repair for each component are modeled by arbitrary bivariate distributions.

The rest of this chapter is organized as follows. Section 5.2 explores system reliability measures: asymptotic average system availability, mean time between system failures, mean time between system repairs, etc. Section 5.3 investigates system maintenance costs. Section 5.4 discusses the optimal system maintenance policies combining both system availability and maintenance cost rate. Several numerical examples are presented to demonstrate models derived.

The following notations will be used throughout this chapter:

# Notation 

POS Period of Service of a component. It begins when the component is new and ends when it is replaced by a new one (perfect repair)
$n \quad$ Number of components in the system
$i \quad$ Index of component position or component position identification, $\forall i, i=1,2, \ldots, n$
$k \quad$ Component identification number for each component position, or number of times which a new component has occupied this component position, $k=1,2, \ldots$.
$k_{i}-1 \quad$ Maximum number of (imperfect) repairs on any component at component position $i$ where $k_{i} \geq 1$
$j \quad$ Index : number of distinct contiguous periods the component has been operating in a single POS for any component position; $(j-1)$ is the number of failures/imperfect repairs; $\forall j, j=1,2, \ldots, k_{i}$ for component position $i$
$Z_{i k} \quad$ POS of component $k$ at component position $i$
$X_{i j k} \quad$ Time to failure of component $k$ in component position $i$ which has been repaired $(j-1)$ times.
$X_{i 1 k} \quad$ Time to the first failure of component $k$ in component position $i$
$Y_{i j k} \quad$ Time of the $j^{\text {th }}$ imperfect repair of the $k^{\text {th }}$ component in component position $i$ where $j=1,2, \ldots, k_{i}-1$| $Y_{i k j k}$ | Time of the perfect repair of the $k^{\text {th }}$ component in component position $i$ |
| :-- | :-- |
| $\mu_{i j}$ | The expected value of $X_{i j k}: E\left[X_{i j k}\right]$ |
| $\eta_{i j}$ | The expected value of $Y_{i j k}: E\left[Y_{i j k}\right]$ |
| $\mu_{i}$ | $\sum_{j=1}^{k_{i}} \mu_{i j}$, total operating time of a component in component position $i$ <br> in a POS |
| $\eta_{i}$ | $\sum_{j=1}^{k_{i}} \eta_{i j}$, total repair (perfect and imperfect) time of a component in <br> component position $i$ in a POS |
| $U(t)$ | System uptime accumulated during $[0, t]$ |
| $D(t)$ | System downtime accumulated during $[0, t]$ |
| $U_{i}(t)$ | Operating-time in component position $i$ during $[0, t)$ |
| $D_{i}(t)$ | Downtime in component position $i$ resulting from failures there in $[0, t]$ |
| $\widetilde{N}_{i}(t)$ | Number of failures in component position $i$ during $[0, t]$ |
| $\widetilde{N}(t)$ | Total number of system failures during $[0, t]$ |
| $\widetilde{N}_{i j}(t)$ | Number of failures of components at component position $i$ for which <br> each has been repaired $(j-1)$ times during $[0, t]$ |
| $U_{i j}(t)$ | Accumulated operating time of the component in position $i$ which has <br> been repaired $(j-1)$ times during $[0, t]$ |
| a.s. | Almost surely: a statement is true with probability one <br> Mean reduction factor of time to failure for components at component <br> position $i$ |
| $\beta_{i}$ | Mean repair time growth factor for components at component position $i$ |

States, time to failure, time to repair and their relationship of components at component position $i$ are shown in Figure 5.1 (Wang and Pham 2006). The vertical axis represents component state: up or down, and the horizontal axis is system operating time.


Figure 5.1. States of components in component position $i$This chapter assumes:
i) Each of the $n$ components in the series system is new and starts to operate at time 0 .
ii) The component in component position $i$ is repaired at the $j^{\text {th }}$ failure if and only if $j<k_{i}$. The repair is imperfect and modeled by the quasirenewal process.
iii) The component in component position $i$ is replaced at the $k_{i}{ }^{\text {th }}$ failure by a new one where $k_{i}$ is an integer. This is a perfect repair.
iv) The time to failure and corresponding time to repair of each component in the system are correlated.
v) The times to failure or times to repair of the components in the same component position between the POSs are stochastically independent and have the same distributions if the corresponding components have the same history of repair.
vi) The steady-state availability exists.
vii) Two or more components cannot fail at the same time.

In addition, we assume that the series system is subject to the same shut-off rule as the one described in Barlow and Proschan (1975), and studied in Khalil (1985): while a failed component is in repair, all other components remain in "suspended animation". After the repair is completed, the system is returned to operation. At that instant, the components in "suspended animation" are as good as they were when the system stopped operating. In other words, the failure of any one component shuts off all other components in this series system.

Generally, when a new component is put into operation, the first $(k-1)$ repairs at failures will be performed at a low cost. This is because the system is young at that time and these repairs turn out to be imperfect. Usually, these repairs may be minor repairs because the component is in good operating condition. After the $(k-1)^{\text {th }}$ imperfect repair, the component may eventually be in a deteriorating operating condition and then a perfect (major) repair may be necessary.

# 5.2 System Availability Indices Modeling 

Note that we consider the case that the time to failure of component $k$ at position $i$ which has been repaired for $(j-1)$ times is correlated with the $j^{\text {th }}$ repair time. The dependence of the time to failure $X_{i j k}$ and the time to repair $Y_{i j k}$ is modeled by the joint distribution density $f_{i j}(x, y)$ in this chapter. Assume that the marginal pdfs of $X_{i j k}$ and $Y_{i j k}$ are $f_{i j}(x)$ and $\mathrm{g}_{i j}(y)$, respectively, and

$$
E\left(X_{i j k}\right)=\int_{0}^{\infty} x f_{i j}(x) d x=\mu_{i j} \quad \text { and } \quad E\left(Y_{i j k}\right)=\int_{0}^{\infty} y g_{i j}(y) d y=\eta_{i j}
$$

Next we derive the asymptotic availability of the system. Note that $U_{i}(t)$ is the operating time in the component position $i$ and the component in componentposition $i$ will not operate during repair of components in other positions per the shut-off rule. Note also that a series system functions if and only if all its constituting components function. Therefore, $U(t)=U_{i}(t)$. Since $U(t)+D(t)=t$ and $U(t)=U_{i}(t)$ we have

$$
\begin{gathered}
\sum_{i=1}^{n} \sum_{j=1}^{k} \sum_{k=1}^{\tilde{N}_{i j}(t)-1} Y_{i j k} \leq D(t) \leq \sum_{i=1}^{n} \sum_{j=1}^{k} \sum_{k=1}^{\tilde{N}_{i}(t)} Y_{i j k} \\
\frac{U(t)}{t}=\left[1+\frac{D(t)}{U(t)}\right]^{-1} \geq\left[1+\sum_{i=1}^{n} \sum_{j=1}^{k} \frac{1}{\tilde{N}_{i j}(t)} \sum_{k=1}^{\tilde{N}_{i j}(t)} Y_{i j k} \frac{N_{i j}\left(U_{i j}(t)\right)}{U_{i j}(t)} \frac{U_{i j}(t)}{U_{i}(t)}\right]^{-1}
\end{gathered}
$$

where $N_{i j}\left(U_{i j}(t)\right)=\tilde{N}_{i j}(t)$ and $\left\{N_{i j}(t), t \geq 0\right\}$ is the renewal counting process associated with $\left\{X_{i j k}, k \geq 1\right\}$.

By the strong law of large numbers it follows that

$$
\lim _{t \rightarrow \infty} \frac{1}{\tilde{N}_{i j}(t)} \sum_{k=1}^{\tilde{N}_{i j}(t)} Y_{i j k} \stackrel{\text { a.s. }}{ } \eta_{i j}
$$

Next we first prove

$$
\lim _{t \rightarrow \infty} \frac{U_{i j}(t)}{U_{i}(t)} \stackrel{\text { a.s. }}{ } \frac{\mu_{i j}}{\mu_{i}}
$$

Let

$$
X_{i k}=\sum_{j=1}^{k} X_{i j k}
$$

Then

$$
\frac{\sum_{k=1}^{N_{i}(t)-1} X_{i j k}}{\sum_{k=1}^{N_{i}(t)+1} X_{i k}} \leq \frac{U_{i j}(t)}{U_{i}(t)} \leq \frac{\sum_{k=1}^{N_{i}(t)+1} X_{i j k}}{\sum_{k=1}^{N_{i}(t)-1} X_{i k}}
$$

where $\left\{N_{i}(t), t \geq 0\right\}$ is the renewal counting process associated with $\left\{X_{i k}, k \geq 1\right\}$.

Note that

$$
\frac{\sum_{k=1}^{N_{i}(t)+1} X_{i j k}}{\sum_{k=1}^{N_{i}(t)-1} X_{i k}}=\frac{\sum_{k=1}^{N_{i}(t)+1} X_{i j k}}{N_{i}(t)+1} \frac{N_{i}(t)-1}{\sum_{k=1}^{N_{i}(t)-1} X_{i k}} \frac{N_{i}(t)+1}{N_{i}(t)-1}
$$Because $N_{i}(t) \xrightarrow{\text { a.s. }} \infty$ as $t \rightarrow \infty$, we have by the strong law of large numbers,

$$
\lim _{t \rightarrow \infty} \frac{U_{i j}(t)}{U_{i}(t)} \leq \lim _{t \rightarrow \infty} \frac{E\left[X_{i j 1}\right]}{E\left[X_{i 1}\right]} \xrightarrow{\text { a.s. }} \frac{\mu_{i j}}{\mu_{i}}
$$

The reverse inequality can be shown similarly. Thus, the above Limit (5.1) holds.
From the elementary renewal theorem it follows that

$$
\begin{aligned}
& \lim _{t \rightarrow \infty} \frac{N_{i j}(t)}{t} \stackrel{\text { a.s. }}{=} \frac{1}{\mu_{i j}} \\
& \lim _{t \rightarrow \infty} \frac{N_{i j}\left(U_{i j}(t)\right)}{U_{i j}(t)}=\frac{1}{\mu_{i j}}
\end{aligned}
$$

Using this result and Equation (5.1) we have

$$
\lim _{t \rightarrow \infty} \frac{U(t)}{t} \gtrless\left[1+\sum_{i=1}^{n} \sum_{j=1}^{k_{i}} \eta_{i j} \cdot \frac{1}{\mu_{i j}} \cdot \frac{\mu_{i j}}{\mu_{i}}\right]^{-1}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i}}{\mu_{i}}\right]^{-1}
$$

The reverse inequality can be proved similarly. Therefore, we have

$$
\lim _{t \rightarrow \infty} \frac{U(t)}{t}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i}}{\mu_{i}}\right]^{-1}
$$

Since $0 \leq U(t) / t \leq 1$ for all $t>0$, and the above asymptotic expression exists (the steady-state availability exists as per the assumptions in Section 5.1), it follows from the Lebesgue dominated convergence theorem that

$$
A_{a v}=\lim _{t \rightarrow \infty} \frac{E[U(t)]}{t}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i}}{\mu_{i}}\right]^{-1}
$$

Now we derive the limiting MTBSF $\bar{\mu}$ and MTBSR $\bar{\eta}$. The average of system up times in $[0, t]$ will be approximately

$$
\frac{U(t)}{\bar{N}(t)}=\frac{U(t) / t}{\sum_{i=1}^{n} \bar{N}_{i}(t) / t}
$$

The difference between the above expression and the average of system up times is a term that converges to 0 with probability 1 as $t \rightarrow \infty$. Noting that the asymptotic number of failures in component position $i$ per unit of time is

$$
\bar{N}_{i}=\lim _{t \rightarrow \infty} \frac{\bar{N}_{i}(t)}{t}=\lim _{t \rightarrow \infty} \frac{N_{i}(U(t)) / U(t)}{t / U(t)}=\frac{k_{i}}{\mu_{i}} A_{a v}
$$and Equation (5.2), we have

$$
\bar{\mu}=\lim _{t \rightarrow \infty} \frac{U(t)}{\bar{N}(t)}=\frac{A_{a v}}{\sum_{i=1}^{n} \frac{k_{i}}{\mu_{i}} A_{a v}}=\left[\sum_{i=1}^{n} \frac{k_{i}}{\mu_{i}}\right]^{-1}
$$

The average system downtime, $\bar{\eta}$, during $[0, t]$ will be approximately

$$
\frac{1}{\bar{N}(t)} \sum_{i=1}^{n} \sum_{j=1}^{k_{i}} \sum_{k=1}^{\bar{N}_{p}(t)} Y_{i j k}
$$

The difference between the above expression and the average system downtime is a term that converges to 0 with probability 1 as $t \rightarrow \infty$. Wang and Pham (2006) prove the following results:

$$
\begin{gathered}
\bar{\eta}^{a . x .}=\bar{\mu} \sum_{i=1}^{n} \frac{\eta_{i}}{\mu_{i}} \\
D_{a v, t}=\lim _{t \rightarrow \infty} \frac{D_{i}(t)}{t} \stackrel{a . x .}{ }=\frac{\eta_{i}}{\mu_{i}} A_{a v} \\
D_{a v}=\lim _{t \rightarrow \infty} \frac{D(t)}{t} \stackrel{a . x .}{ } A_{a v} \sum_{i=1}^{n} \frac{\eta_{i}}{\mu_{i}}
\end{gathered}
$$

Note that in the above expressions, the dependence of the time to failure $X_{i j k}$ and the time to repair $Y_{i j k}$ is allowed.

Suppose that in this series system of $n$ components upon each repair the time to failure of component $i$ will decrease to a fraction $\alpha_{i}$ of its immediately previous one and the repair time will increase to a multiple $\beta_{i}$ of its immediately previous one where successive times to failure are independent and so are successive repair times, $\forall i, i=1,2, \ldots, n$. In other words, the successive times to failure compose a decreasing quasi-renewal process with parameter $\alpha_{i}$ and the successive repair times form an increasing quasi-renewal process with parameter $\beta_{i}$ for component $i$. Accordingly, upon each repair the expected time to failure of the component will decrease to a fraction $\alpha_{i}$ of its immediately previous value and the expected repair time will increase to a multiple $\beta_{i}$ of its previous value, i.e.,

$$
\mu_{i(j+1)}=\alpha_{i} \mu_{i j} \quad \eta_{i(j+1)}=\beta_{i} \eta_{i j}
$$

where $1 \leq j \leq k_{i}-1$ and $k_{i}-1 \geq 1$ for component position $i$. Note that $\left(k_{i}-1\right)$ is the maximum number of imperfect repairs at component position $i$ in a POS and that $k_{i}=1$ indicates perfect repairs only for component position $i$. Obviously, that $\alpha_{i} \equiv 1$ also corresponds to a perfect repair only for the component in component position $i$.Generally in practice $0<\alpha_{i} \leq 1$ and $1 \leq \beta_{i}$. However, this chapter considers imperfect repair and assumes that the factors $\alpha_{i}, \beta_{i} \neq 1$ for $1 \leq i \leq n$ later in this chapter.

From the above relationship (5.9), it follows that the average accumulating operating time in a POS for component position $i$ resulting from failure there is given by

$$
\mu_{i}=\sum_{j=1}^{k_{i}} \mu_{i j}=\mu_{i 1}+\alpha_{i} \mu_{i 1}+\alpha_{i}^{2} \mu_{i 1}+\alpha_{i}^{3} \mu_{i 1}+\cdots+\alpha_{i}^{k_{i}-1} \mu_{i 1}=\frac{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}{1-\alpha_{i}}
$$

Similarly, the average accumulating down time (including perfect repair time) in a POS for component position $i$ resulting from failure there is

$$
\eta_{i}=\sum_{j=1}^{k_{i}} \eta_{i j}=\eta_{i 1}+\beta_{i} \eta_{i 1}+\beta_{i}^{2} \eta_{i 1}+\beta_{i}^{3} \eta_{i 1}+\cdots+\beta_{i}^{k_{i}-1} \eta_{i 1}=\frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)}{1-\beta_{i}}
$$

Alternatively, assume that the perfect repair time is $\tau_{i}$, which is independent of other imperfect repair times. Then the average accumulating down time in a POS for component position $i$ resulting from failure there is

$$
\eta_{i}=\sum_{j=1}^{k_{i}} \eta_{i j}=\frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}-1}\right)}{1-\beta_{i}}+\tau_{i}
$$

where $k_{i} \geq 1$.
Upon substituting Equations (5.10) and (5.11) into Equations (5.1) - (5.3) and simplifying, the following proposition follows:

Proposition 5.1 The mean asymptotic availability of the series system defined in Section 5.1 is

$$
A_{a v}=\lim _{t \rightarrow \infty} \frac{E[U(t)]}{t}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}\right]^{-1}
$$

The limiting average functioning time between system failures (MTBSF) is

$$
\bar{\mu}=\lim _{t \rightarrow \infty} \frac{U(t)}{\bar{N}(t)} \stackrel{\text { a.s. }}{=}\left[\sum_{i=1}^{n} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right]^{-1}
$$

The limiting mean time between system repairs (MTBSR) is

$$
\bar{\eta}=\lim _{t \rightarrow \infty} \frac{D(t)}{\bar{N}(t)} \stackrel{\text { a.s. }}{=} \bar{\mu} \sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}
$$

The asymptotic fractional down time due to the failure from component position $i$ is$$
\begin{aligned}
D_{a v, i} & =\lim _{t \rightarrow \infty} \frac{D_{i}(t)}{t} \\
& \stackrel{\text { a.s. }}{=}\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}\right]^{-1} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}
\end{aligned}
$$

The asymptotic fractional down time of the system is

$$
D_{a v}=\lim _{t \rightarrow \infty} \frac{D(t)}{t} \stackrel{\text { a.s. }}{=}\left\{1+\left[\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}\right]^{-1}\right\}^{-1}
$$

The asymptotic number of failures in component position i per unit of time is

$$
\widetilde{N}_{i}=\lim _{t \rightarrow \infty} \frac{\widetilde{N}_{i}(t)}{t} \stackrel{\text { a.s. }}{=} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)} A_{a v}
$$

The asymptotic number of failures of the system per unit of time is

$$
\widetilde{N}=\lim _{t \rightarrow \infty} \frac{\widetilde{N}(t)}{t}=\lim _{t \rightarrow \infty} \frac{\sum_{i}^{n} \widetilde{N}_{i}(t)}{t} \stackrel{\text { a.s. }}{=} A_{a v}\left[\sum_{i=1}^{n} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right]
$$

We can see that the above results $(5.12 \mathrm{a}-\mathrm{g})$ depend only on the expected time to failure $\mu_{i 1}$ and the expected repair time $\eta_{i 1}$ of each new component (not yet repaired) in the system as well as the maximum number of imperfect repair $\left(k_{i}-1\right)$, factors $\alpha_{i}$ and $\beta_{i}$ but not on distributions of actual times to failure and repair of the components. Thus, these asymptotic results hold for arbitrary distributions of times to failure and repair, and are mathematically very simple in spite of the fact that the age distribution of components in the system quickly becomes stochastically very complicated.

It follows that that from Equations (5.10) and (5.11),

$$
\begin{aligned}
\lim _{\alpha_{i} \rightarrow 1} \mu_{i} & =k_{i} \mu_{i 1} \\
\lim _{\beta_{i} \rightarrow 1} \eta_{i} & =k_{i} \eta_{i 1}
\end{aligned}
$$

which are identical to total operating time and down time for component position $i$ in a POS for the perfect repair case respectively. Note $\alpha_{i}=1$ corresponds to a perfect repair for the component in component position $i$. Therefore, the limiting values from the above results $(5.12 \mathrm{a}-\mathrm{g})$ for the imperfect repair case when $\alpha_{i} \rightarrow 1$ and $\beta_{i} \rightarrow 1$ can be used for the perfect repair case.

Example 5.1. Barlow and Proschan (1975) study a system of four components in series with expected times to failure and repair given in Table 5.1. Given the timeto failure and the time to repair of each component are independent they compute the availability measures for the perfect repair case. For this example, Wang and Pham (2006) consider imperfect repair case as described in the assumptions in Section 5.1, and assume that each component can be imperfectly repaired at most $\left(k_{i}-1\right)$ times. When each component fails at failure $k_{i}$, it undergoes a perfect repair (note that perfect repair times at different repair stages with different deteriorating component conditions may be different in practice). Correlated failure and repair are allowed. $k_{i}, \alpha_{i}$ and $\beta_{i}$ values for each component are summarized in Table 5.1.

Table 5.1. System parameters

| Component <br> index | Component type | Mean time to <br> failure $\mu_{i 1}$ <br> (hours) | Mean repair <br> time $\eta_{i 1}$ <br> (hours) | $k_{i}$ | $\alpha_{i}$ | $\beta_{i}$ |
| :--: | :-- | :--: | :--: | :--: | :--: | :--: |
| 1 | Power supply | 50 | 0.1 | 6 | 0.90 | 1.05 |
| 2 | Analog equipment | 100 | 0.2 | 5 | 0.90 | 1.05 |
| 3 | Digital equipment | 1000 | 1.0 | 6 | 0.95 | 1.05 |
| 4 | Mechanical | 10000 | 20.0 | 7 | 0.92 | 1.05 |

Table 5.2. Comparison of numerical results

| Availability measures | Perfect repair <br> (Barlow-Proschan) | Imperfect repair <br> (Wang-Pham) |
| :-- | :--: | :--: |
| Limiting availability | 0.993 | 0.9903 |
| Limiting average of system up times (hrs) | 32.15 | 25.5890 |
| Limiting average of system down times (hrs) | 0.225 | 0.2516 |
| Limiting number of system failures per hour |  | 0.0387 |
| $D_{a r, 1}$ | 0.002 | 0.0029 |
| $D_{a r, 2}$ | 0.002 | 0.0027 |
| $D_{a r, 3}$ | 0.001 | 0.0013 |
| $D_{a r, 4}$ | 0.002 | 0.0029 |
| $\bar{N}_{1}$ | 0.020 | 0.0254 |
| $\bar{N}_{2}$ | 0.010 | 0.0121 |
| $\bar{N}_{3}$ | 0.001 | 0.0011 |
| $\bar{N}_{4}$ | 0.0001 | 0.0001 |Using the formulae derived in this section, Wang and Pham (2006) evaluate availability measures for this system. The obtained numerical results are shown in Table 5.2 in which the numerical availability indices for the perfect repair case by Barlow and Proschan (1975) are also listed. Comparing these results with those by Barlow and Proschan, we can see that:
(a) The system availability and the limiting average of system up times for the imperfect repair case are significantly smaller than for the perfect repair case.
(b) The long-run fraction of the time that the system is down due to the failure of each of the four component types, and the long-run average number of failures per hour of each of the component types are larger for imperfect repair case. Obviously this is because the repair is imperfect, i.e., repair doesn't make a component "good as new".
(c) If $k_{i}=1$ for all four components, these results and those by Barlow and Proschan will be the same. Alternatively, the limiting results for the imperfect repair case when $\alpha_{i} \rightarrow 1$ and $\beta_{i} \rightarrow 1$ for all four components can expect to be the same as those by Barlow and Proschan (1975). This is because imperfect repair can include perfect repair as special case.

# 5.3 Modeling of Maintenance Costs 

Section 5.2 has studied one system performance measure - system availability indices. For a repairable system the maintenance cost per unit of time, or maintenance cost rate is another interesting system performance measure. For example, a car owner may want to know how much to spend on his car maintenance every year. This section investigates the system maintenance cost rate. Two maintenance cost models will be presented, following Wang and Pham (2006). Note assumption (vii) in Section 5.1: no more than one failure occurs at the same time.

### 5.3.1 Cost Model 1

Assume that it costs $d_{i}$ dollars per unit of down time for component $i$ to perform repair. $d_{i}$ consists of two parts: $d_{0}$ and $d_{i m}$, where $d_{0}$ is the loss cost per unit of system down time because the system is not available (loss from service interruption) and the same for all component positions, and $d_{i m}$ is the repair cost per unit of time for the component in component position $i$ where $1 \leq i \leq n$. Obviously, $d_{i}=d_{0}+d_{i m}$. Repair cost rate $d_{i m}$ may include two parts: materials and labor costs, and can be estimated from historical repair data, material cost, labor rate, etc. It follows that the total cost of the series system maintenance and service interruption accrued during the time interval $[0, t]$ is$$
C_{1}(t)=\sum_{i=1}^{n} d_{i} D_{i}(t)
$$

The system maintenance cost per unit of time, or system maintenance cost rate is, in the limit,

$$
\bar{C}_{1}=\lim _{t \rightarrow \infty} \frac{C_{1}(t)}{t}=\lim _{t \rightarrow \infty} \sum_{i=1}^{n} d_{i} \frac{D_{i}(t)}{t}
$$

Per Section 5.2 and Zhao (1994),

$$
\lim _{t \rightarrow \infty} \frac{D_{i}(t)}{t}=D_{a v, i}
$$

Using the quasi-renewal process in Chapter 4, Wang and Pham (2006) show

$$
\begin{aligned}
& \bar{C}_{1}=\lim _{t \rightarrow \infty} \frac{C_{1}(t)}{t}=A_{a v}\left[\sum_{i=1}^{n} d_{i} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)}{1-\beta_{i}} \frac{1-\alpha_{i}}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right] \\
& \bar{C}_{1}=\frac{\sum_{i=1}^{n} d_{i} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}}{1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}}
\end{aligned}
$$

Next we consider another type of repair cost for each component in the system: repair cost is in a lump sum instead of cost per unit of time.

# 5.3.2 Cost Model 2 

Suppose that component position $i$ costs $d_{i 1}$ dollars to imperfect repair and service interruption each time it fails and $d_{i 2}$ dollars to perfect repair and service interruption every $k_{i}$ repairs, regardless of the time to complete repair. Assume further that $d_{i 1}<d_{i 2} . d_{i 1}$ and $d_{i 2}$ may include system loss cost, materials cost, and labor cost, and can be estimated from service importance, historical repair data, material cost, labor rate, etc. Note that service interruption cost may tend to be related to time to repair in many situations, as in Cost Model 1. Therefore, Cost Model 1 and Model 2 should be chosen per actual application. Note that a lot of research in the maintenance and reliability field considers repair/maintenance cost only and ignores system loss cost. Then the total cost of system maintenance and service interruption accrued during $[0, t]$ is

$$
C_{2}(t)=\sum_{i=1}^{n}\left\{d_{i 1}\left[\tilde{N}_{i}(t)-\left\lfloor\tilde{N}_{i}(t) / k_{i}\right\rfloor\right]+d_{i 2}\left\lfloor\tilde{N}_{i}(t) / k_{i}\right\rfloor\right\}
$$

where $\left\lfloor x\right\rfloor$ means the largest integer less than or equal to $x$.The limiting system maintenance cost per unit of time, or maintenance cost rate is

$$
\bar{C}_{2}=\lim _{t \rightarrow \infty} \frac{C_{2}(t)}{t}=\lim _{i \rightarrow \infty} \sum_{i=1}^{n}\left\{d_{i 1} \cdot \bar{N}_{i}(t) / t+\left(d_{i 2}-d_{i 1}\right)\left\lfloor\bar{N}_{i}(t) / k_{i}\right\rfloor / t\right\}
$$

Following Section 5.2, we have that

$$
\lim _{t \rightarrow \infty} \bar{N}_{i}(t) / t=\bar{N}_{i}=\lim _{t \rightarrow \infty}\left[\bar{N}_{i}(t)-k_{i}\right] / t
$$

and

$$
\left[\left(\bar{N}_{i}(t)-k_{i}\right) / k_{i}\right] / t \leq\left\lfloor\bar{N}_{i}(t) / k_{i}\right\rfloor / t \leq\left[\bar{N}_{i}(t) / k_{i}\right] / t
$$

Thus,

$$
\lim _{t \rightarrow \infty}\left\lfloor\bar{N}_{i}(t) / k_{i}\right\rfloor / t=\bar{N}_{i} / k_{i}
$$

and

$$
\bar{C}_{2}=\lim _{t \rightarrow \infty} \frac{C_{2}(t)}{t}=A_{a v} \sum_{i=1}^{n} \mu_{i}^{-1}\left[\left(k_{i}-1\right) d_{i 1}+d_{i 2}\right]
$$

Finally, we have

$$
\bar{C}_{2}=\lim _{t \rightarrow \infty} \frac{C_{2}(t)}{t}=A_{a v} \sum_{i=1}^{n}\left[\left(k_{i}-1\right) d_{i 1}+d_{i 2}\right] \frac{1-\alpha_{i}}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}
$$

$$
\text { or } \quad \bar{C}_{2}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}\right]^{-1} \sum_{i=1}^{n} \frac{\left(1-\alpha_{i}\right)\left[\left(k_{i}-1\right) d_{i 1}+d_{i 2}\right]}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}
$$

It is easy to verify that $\bar{C}_{1}=\bar{C}_{2}$ when $d_{i} \eta_{i}=\left[\left(k_{i}-1\right) d_{i 1}+d_{i 2}\right]$, i.e., when the total repair cost in a POS per Cost Model 1 is equal to the total repair cost in a POS per Cost Model 2.

# 5.4 Optimal System Maintenance Policies 

### 5.4.1 Optimality of Availability and Maintenance Cost Rates

In Sections 5.2 and 5.3 we have derived systems availability measures and maintenance cost measures respectively. Next, we discuss how to determine the optimal number of repairs for each component position in a POS that maximizes the limiting system availability and/or minimizes the limiting system maintenance cost rate. Note that the number of all repairs on a component in component position $i$ in a POS is $k_{i}$ where $k_{i} \geq 1$. We have the following propositions from Wang and Pham (2006):Proposition 5.2 The optimal value for the vector of repair numbers $\left(k_{1}, k_{2}, \ldots, k_{n}\right)$ in a POS is $(1,1, \ldots, 1)$, given any of the following criteria: maximization of the limiting system availability $A_{a v}$, or MTBSF, or minimization of MTBSR, or fractional system down time $D_{a v}$.

Proof. Consider $A_{a v}$ first. Let

$$
A_{a v}\left(k_{1}, k_{2}, \ldots, k_{n}\right)=A_{a v}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}\right]^{-1}
$$

Then

$$
\begin{aligned}
\Delta A_{a v}(j) & =A_{a v}\left(k_{1}, k_{2}, \ldots, k_{j}+1, \ldots, k_{n}\right)-A_{a v}\left(k_{1}, k_{2}, \ldots, k_{j}, \ldots, k_{n}\right) \\
& =\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}\right]^{-1} \\
& \times\left[1+\sum_{\substack{i=1 \\
i \neq j}}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}+\frac{\eta_{j 1}\left(1-\alpha_{j}\right)\left(1-\beta_{j}^{k_{j}+1}\right)}{\mu_{j 1}\left(1-\beta_{j}\right)\left(1-\alpha_{j}^{k_{j}+1}\right)}\right]^{-1} \\
& \times \frac{\eta_{j 1}\left(1-\alpha_{j}\right)}{\mu_{j 1}\left(\beta_{j}-1\right)}\left(\frac{\beta_{j}^{k_{j}}-1}{1-\alpha_{j}^{k_{j}}}-\frac{\beta_{j}^{k_{j}+1}-1}{1-\alpha_{j}^{k_{j}+1}}\right)
\end{aligned}
$$

Let $G(x)=\frac{\beta_{j}^{x}-1}{1-\alpha_{j}^{x}} \quad$ where $x$ is a real number.

Then

$$
\frac{d G(x)}{d x}=\frac{\beta_{j}^{x}\left(1-\alpha_{j}^{x}\right) \ln \beta_{j}+\alpha_{j}^{x}\left(\beta_{j}^{x}-1\right) \ln \alpha_{j}}{\left(1-\alpha_{j}^{x}\right)^{2}}
$$

Now let

$$
W(x)=\beta_{j}^{x}\left(1-\alpha_{j}^{x}\right) \ln \beta_{j}+\alpha_{j}^{x}\left(\beta_{j}^{x}-1\right) \ln \alpha_{j}
$$

Noting that $W(0)=0$, and

$$
\frac{d W(x)}{d x}=\beta_{j}^{x}\left(1-\alpha_{j}^{x}\right)\left(\ln \beta_{j}\right)^{2}+\alpha_{j}^{x}\left(\beta_{j}^{x}-1\right)\left(\ln \alpha_{j}\right)^{2}>0
$$

it follows that $W(x)>0$ for $x>0$ and then $G^{\prime}(x)>0$ for $x>0$.
Therefore, we have that$$
\frac{\beta_{j}^{k_{j}}-1}{1-\alpha_{j}^{k_{j}}}-\frac{\beta_{j}^{k_{j}+1}-1}{1-\alpha_{j}^{k_{j}+1}}<0 \quad \text { for } \quad j=1,2, \ldots, n
$$

It follows that $\Delta A_{a v}(j)<0$ for $j=1,2, \ldots, n$, and then the maximum system asymptotic availability is obtained when $k_{1}=k_{2}=\cdots=k_{n}=1$.

Next we consider the asymptotic mean functioning time between system failures $\bar{\mu}$. Let

$$
\bar{\mu}\left(k_{1}, k_{2}, \ldots, k_{n}\right)=\bar{\mu}=\left[\sum_{i=1}^{n} k_{i} \frac{1-\alpha_{i}}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right]^{-1}
$$

Then

$$
\begin{aligned}
\Delta \bar{\mu}_{j} & =\bar{\mu}\left(k_{1}, \ldots, k_{j}+1, \ldots, k_{n}\right)-\bar{\mu}\left(k_{1}, \ldots, k_{j}, \ldots, k_{n}\right) \\
& =\left[\sum_{i=1}^{n} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right]^{-1}\left[\sum_{\substack{i=1 \\
i \neq j}}^{n} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}+\frac{\left(k_{j}+1\right)\left(1-\alpha_{j}\right)}{\mu_{j 1}\left(1-\alpha_{j}^{k_{j}+1}\right)}\right]^{-1} \\
& \times \frac{1-\alpha_{j}}{\mu_{j 1}} \frac{-1+\alpha_{j}^{k_{j}}+\alpha_{j}^{k_{j}} k_{j}\left(1-\alpha_{j}\right)}{\left(1-\alpha_{j}^{k_{j}}\right)\left(1-\alpha_{j}^{k_{j}+1}\right)}
\end{aligned}
$$

Let

$$
G\left(k_{j}\right)=-1+\alpha_{j}^{k_{j}}+\alpha_{j}^{k_{j}} k_{j}\left(1-\alpha_{j}\right)
$$

Then

$$
\Delta G_{j}=G\left(k_{j}+1\right)-G\left(k_{j}\right)=-\alpha_{j}^{k_{j}}\left(k_{j}+1\right)\left(1-\alpha_{j}\right)^{2}<0
$$

Note that

$$
G(1)=-\left(1-\alpha_{j}\right)^{2}<0
$$

From them it follows that $G\left(k_{j}\right)<0$ and then $\Delta \mu_{j}<0$ for $j=1,2, \ldots, n$.
For $D_{a v}$, let

$$
D_{a v}\left(k_{1}, k_{2}, \ldots, k_{n}\right)=D_{a v}=\left\{1+\left[\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)}{1-\beta_{i}} / \frac{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}{1-\alpha_{i}}\right]^{-1}\right\}^{-1}
$$

It is easy to obtain that

$$
\Delta D_{a v}(j)=D_{a v}\left(k_{1}, k_{2}, \ldots, k_{j}+1, \ldots, k_{n}\right)-D_{a v}\left(k_{1}, k_{2}, \ldots, k_{j}, \ldots, k_{n}\right)
$$$$
\begin{aligned}
& =\left\{1+\left[\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}\right]\right\}^{-1} \\
& \times\left\{1+\left[\frac{\eta_{j 1}\left(1-\alpha_{j}\right)\left(1-\beta_{j}^{k_{j}}\right)}{\mu_{j 1}\left(1-\beta_{i j}\right)\left(1-\alpha_{j}^{k_{j}}\right)}+\sum_{\substack{i=1 \\
i \neq j}}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}\right]\right\}^{-1} \\
& \times \frac{\eta_{j 1}\left(1-\alpha_{j}\right)}{\mu_{j 1}\left(\beta_{j}-1\right)}\left(\frac{\beta_{j}^{k_{j}+1}-1}{1-\alpha_{j}^{k_{j}+1}}-\frac{\beta_{j}^{k_{j}}-1}{1-\alpha_{j}^{k_{j}}}\right)>0 \quad \text { for } j=1,2, \ldots, n
\end{aligned}
$$

From them Proposition 5.2 follows.
The above proposition is intuitively obvious. $k_{1}, k_{2}, k_{3}, k_{4} \geq 1$ and they are all integers. Note that $A_{a v}$ is limiting average availability over infinite POSs which may be insensitive to changes of $k_{i}$ values.

Proposition 5.3 The necessary condition for minimizing $\bar{C}_{1}$ is to do perfect repair only on the component in the component position which has the largest maintenance cost per unit of time.

Proof. See Wang and Pham (2006). An interpretation to this proposition is given after the following proposition.

Proposition 5.4 For the component position with the smallest maintenance cost per unit of down time, say, position $j$, there may exist a finite unique number of all repairs in a POS, say, $k_{j}^{*}$, for all components in this position if

$$
\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)<d_{j}
$$

and it is the optimal solution for component position $j$ to minimize $\bar{C}_{1}$. Otherwise, the minimum system maintenance cost is obtained when $k_{j} \rightarrow \infty$.

Proof. Following Wang and Pham (2006), let

$$
\Delta_{j}=d_{j}-\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}\left(d_{i}-d_{j}\right)
$$

and

$$
d_{j}=\min \left\{d_{1}, d_{2}, \ldots, d_{n}\right\}
$$If at least one $k_{i} \rightarrow \infty$ for $i=1,2, \ldots, j-1, j+1, \ldots, n$, then $\Delta_{j} \rightarrow-\infty<0$ and $\frac{\partial \bar{C}_{1}}{\partial k_{j}}<0$. Note that

$$
\frac{\eta_{i 1}\left(1-\alpha_{i}\right)\left(1-\beta_{i}^{k_{i}}\right)}{\mu_{i 1}\left(1-\beta_{i}\right)\left(1-\alpha_{i}^{k_{i}}\right)}
$$

is increasing in $k_{i}$ and its minimum value is obtained when $k_{i}=1$ for $i=1,2, \ldots, n$. When $k_{1}=k_{2}=\cdots=k_{j-1}=k_{j+1}=\cdots=k_{n}=1, \Delta_{j}$ has the maximum value

$$
\Delta_{j, \max }=d_{j}-\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)
$$

if $\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)<d_{j}$ then $\Delta_{j}>0$ and thus $\frac{\partial \bar{C}_{1}}{\partial k_{j}}>0$.
Therefore, there may exist an optimal $k_{j}$ which minimizes $\bar{C}_{1}$ when the above condition is satisfied.

On the other hand, if $\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)>d_{j}$, then $\Delta_{j} \leq 0$ and thus $\frac{\partial \bar{C}_{1}}{\partial k_{j}} \leq 0$ for any $k_{j} \geq 1$. Hence, the minimum $\bar{C}_{1}$ is obtained when $k_{j} \rightarrow \infty$.

Propositions 5.3 and 5.4 imply that each component may not be treated as a single-unit system individually and local optimal maintenance policies for individual components may not result in the global optimal maintenance policy for the whole system. Now let's see a numerical example. Assume that in Example 5.1 in Section 5.2, $d_{1}=20, d_{2}=80, d_{3}=18$, and $d_{4}=0.2$ dollars per hour. Note

$$
\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)=0.2170>d_{4}=0.2 \quad \text { at this time. }
$$

Using nonlinear integer programming software, and noting that $k_{1}, k_{2}, k_{3}, k_{4} \geq 1$ and they are all integers, we obtain that if there is no constraint on $k_{4}$, the minimum system maintenance cost per hour $\bar{C}_{1}$ is $\$ 0.2$ which is reached when $k_{2}=1$ together with, $k_{1}=1, \quad k_{3}=1$, and $k_{4} \rightarrow+\infty$. One explanation may be that it is most expensive to restore the component at component position 2 once it fails. Note that the minimum system maintenance cost per hour of $\$ 0.2$ is equal to $d_{4}$. This is because the component at component position 2 is always repaired if $k_{4} \rightarrow+\infty . d_{4}$ is so low as compared with repair cost $d_{1}, d_{2}$, and $d_{3}$ that to always repair the component at component position 4 is of low cost for the entire system. However, this special situation may rarely happen in practice since loss cost from service interruption needs to be very low at this time.

If $d_{4}=4.4$ then$$
\sum_{i=1}^{n} \frac{\eta_{i 1}}{\mu_{i 1}}\left(d_{i}-d_{j}\right)=0.1960<d_{4}=4.4 \quad \text { at this time }
$$

and the optimal system maintenance cost rate is attained when repair numbers $k_{1}=k_{2}=k_{3}=k_{4}=1$. Note this $k_{4}$ is finite. The corresponding $A_{o r}=0.993049$.

Propositions 5.3 and 5.4 can be explained as follows. When the component in component position $j$ with the smallest maintenance cost $d_{j}$ is in repair, the components in the other component positions which have larger maintenance costs per unit of time will be suspended (neither age nor experience repair) and thus result in no additional repair cost. If the component in position $j$ fails frequently, the other components with larger repair cost per unit time will be subject to less repair costs. Hence, there exists a trade-off between the increase of the maintenance cost resulting from frequent repair of the component in position $j$ and less maintenance costs resulting from the suspended animation of the other components during the repair of the component at position $j$.

Similarly, we can consider minimizing system maintenance cost rate $\bar{C}_{2}$. Existence of the optimal solution to minimize $\bar{C}_{2}$ can also be explained from the physical meaning. According to the meaning of $d_{i}$, when the number of imperfect repairs in a POS becomes larger the repair time and repair frequency will become larger and thus the maintenance cost per unit of time will increase. On the other hand, if only perfect repair is performed, the maintenance cost rate may be big because $d_{i 1}<d_{i 2}$. Hence there may exist a trade-off between them, and so an optimal solution.

Example 5.2. Suppose that in Example 5.1, repair costs for four components are $d_{11}=1, d_{21}=10, d_{31}=15, d_{41}=10, d_{12}=2 d_{22}=16, d_{32}=18, d_{42}=14$ in dollars. Determine the minimum system maintenance cost per hour using cost model 2 in Section 5.3.2.

Note that $k_{1}, k_{2}, k_{3}, k_{4} \geq 1$ and they are all integers. Using nonlinear integer programming software, Wang and Pham (2006) obtain the minimum system maintenance cost per hour:

$$
\bar{C}_{2 \min }=\$ 0.178596 \quad \text { when } k_{1}=4, k_{2}=3, k_{3}=2, k_{4}=5
$$

and the corresponding limiting system availability:

$$
A_{o r}=0.991594
$$

# 5.4.2 Optimal Repair Policy 

From Section 5.4.1, we can see that when the minimum system maintenance rate $\bar{C}_{1}$ is obtained, the corresponding system availability may be so low that it may not be acceptable in practice. Therefore, both the system availability andmaintenance cost rate must be considered together to obtain the optimal system maintenance policy. For example, in view of the maintenance cost constraints, one may determine the optimal number of repairs in a POS for all component positions to maximize the system availability. This class of problems can be formulated as:

# Optimization Problem 1 

Maximize $\quad A_{a v}=\left[1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)\left(1-\beta_{i}\right)}\right]^{-1}$

Subject to $\quad\left\{\begin{array}{l}\bar{C}_{2} \leq C_{20} \\ k_{1}, k_{2}, \ldots, k_{n} \geq 1 \\ k_{1}, k_{2}, \ldots, k_{n}=\text { integer }\end{array}\right.$
where constant $C_{20}$ is the predetermined requirement for system maintenance cost per unit of time.

## Optimization Problem 2

Minimize

$$
\bar{C}_{1}=\frac{\sum_{i=1}^{n} d_{i} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)}{1-\beta_{i}} \frac{1-\alpha_{i}}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}}{1+\sum_{i=1}^{n} \frac{\eta_{i 1}\left(1-\beta_{i}^{k_{i}}\right)}{1-\beta_{i}} \frac{1-\alpha_{i}}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}}
$$

Subject to

$$
\left\{\begin{array}{l}
\bar{N}=A_{a v}\left[\sum_{i=1}^{n} \frac{k_{i}\left(1-\alpha_{i}\right)}{\mu_{i 1}\left(1-\alpha_{i}^{k_{i}}\right)}\right] \leq N_{0} \\
k_{1}, k_{2}, \ldots, k_{n} \geq 1 \\
k_{i} \leq k_{i}^{0}, \quad \forall i=1, \ldots, n \\
k_{1}, k_{2}, \ldots, k_{n}=\text { integer }
\end{array}\right.
$$

where constant $N_{0}$ is the pre-specified requirement for the number of failures of the system per unit of time, and $k_{i}^{0}$ is the upper bound for the $k_{i}, i=1, \ldots, n$.

Note Proposition 5.4. Thus, a upper bound $k_{i}^{0}$ for the $k_{i}$ where $i=1, \ldots, n$ is set for Optimization Problem 2.

Similarly, according to different requirements and circumstances we can devise different optimization models based on the system availability and maintenance cost rates derived in Sections 5.2 and 5.3. These models can be solved using any nonlinear programming software. Now let's see an example.

Example 5.3 Assume that in Example 5.2, $C_{20}=\$ 0.18$ per hour of down time. Determine the maximum system availability subject to this cost constraint.Using optimization model 1, the optimal solution can be found to be

$$
A_{o v, \max }=0.992354 \quad \text { when } k_{1}=3 \quad k_{2}=3 \quad k_{3}=2 \quad k_{4}=1
$$

If $C_{20}=\$ 0.20$ per hour,

$$
A_{o v, \max }=0.992893 \quad \text { when } \quad k_{1}=1 \quad k_{2}=2 \quad k_{3}=1 \quad k_{4}=1
$$

If $C_{20}=\$ 5$ per hour,

$$
A_{o v, \max }=0.993049 \quad \text { when } k_{1}=1 \quad k_{2}=1 \quad k_{3}=1 \quad k_{4}=1
$$

At this point, the system availability is equal to the one for the case of perfect repair only given by Barlow and Proschan (1975) because the maintenance cost constraint is not tight.

# 5.5 Concluding Discussions 

This chapter models imperfect repair using the quasi-renewal process: upon repair the time to failure of a unit will decrease to some proportion of its immediately previous one and be independent of all previous ones, and the repair time will increase to a multiple of its immediately previous one and be independent of all previous ones, i.e., the successive times to failure follow a decreasing quasirenewal process and the successive repair times form an increasing quasi-renewal process. One can see that the quasi-renewal process makes availability and maintenance cost modeling of the series system mathematically tractable given repair is imperfect. Most results obtained in this chapter are in closed forms. The optimization problems proposed in this chapter and optimal maintenance policies can be easily solved using mathematical programming software.

Availability indices derived in this chapter are compared with the well-known results by Barlow and Proschan (1975) which assume perfect repair through an example of a four-components series system. The comparison reveals: (a) The system availability and the limiting average of system up times for the imperfect repair case are smaller than for the perfect repair case; (b) The long-run fraction of the time that the system is down due to the failure of each of the four components, and the long-run average number of failures per hour of each of the four components are larger for imperfect repair case. If $k_{i}=1$ for all four components, results in this chapter and those by Barlow and Proschan (1975) will be the same. Alternatively, the limiting results for the imperfect repair case when $\alpha_{i} \rightarrow 1$ and $\beta_{i} \rightarrow 1$ for all four components can expect to be the same as those by Barlow and Proschan.

Many systems are the series system in practice, and their maintenance and availability are subject to various shut-off rules (Khalil 1985). Further work on optimum maintenance and availability modeling of the series system can be performed for other shut-off rules.# Opportunistic Maintenance of Multi-unit Systems 

Block, age and sequential PM policies have been studied extensively in the literature, as shown in Chapter 3. However, these PM policies are designed for a system composed of a single stochastically deteriorating subsystem (McCall 1965). A natural generalization of the underlying maintenance model is to consider a system with multi-subsystems. Optimal maintenance policies for such systems reduce to those for systems with a single subsystem only if there exists no economic dependence, failure dependence and structural dependence. In this case, maintenance decisions are also independent and the optimal policy is to employ an optimal block, age, failure limit, or sequential PM policy for each separate subsystem. However, if there is economic dependence, then the optimal maintenance policy is not one of considering each subsystem separately and maintenance decisions will not be independent, as mentioned in Chapter 1. Obviously, the optimal maintenance action for a given subsystem at any point of time depends on the states of all subsystems, i.e., maintenance is opportunistic. Radner and Jorgenson (1963), Cho and Parlar (1991), Dekker and Smeitink (1991), Zheng (1995), Jesen (1996), Wang and Pham (1996), and Wang (2002) summarize existing work on multi-component systems and opportunistic maintenance.

Chapters 1 and 3 indicate that most existing maintenance models in the reliability and maintenance literature have been developed for one-unit systems, and maintenance models for multi-subsystem systems are only a small proportion. It should also be noted that economic dependence is ignored in some previous maintenance models of multi-unit systems. Some models consider economic dependence but they suppose that all maintenance is perfect. This chapter, based on Wang (1997), investigates the optimal PM policy for a system with economic dependence and imperfect repair.

We assume that this system consists of $n+1$ subsystems and all of them are monitored. We suppose also that in this system one subsystem has increasing failure rate and the remaining $n$ subsystems have constant failure rates. Next, the subsystem with increasing failure rate is denoted by subsystem 0 while the remaining subsystems are labeled by subsystem 1 , subsystem $2, \ldots$, subsystem $n$. The failure rate function for each subsystem is given by $\lambda_{i}(t), \forall i, i=0,1, \ldots, n$ where$$
\begin{aligned}
& \lambda_{i}(t)=\lambda_{i}, \quad \forall i, i=1, \ldots, n \quad \text { and } \\
& \lambda_{0}^{i}(t)>0
\end{aligned}
$$

Since subsystem 1, subsystem 2,..., and subsystem $n$ fail exponentially, they will never be replaced before failure, hence no PM will be performed on them.

The following notation will be used in this chapter:

# NOTATION 

$T \quad$ Critical age at which a PM is performed on subsystem 0
$t_{i} \quad$ Critical age of subsystem $i$ for $i=1,2, \ldots, n$
$\lambda_{i} \quad$ Failure rate of subsystem $i$ for $i=1,2, \ldots, n$
$n \quad$ Number of subsystems with constant failure rates
$C_{0}, C_{00} \quad$ PM cost of subsystem 0 at $T$ and repair cost at its failure
$w_{0}, w_{00} \quad$ PM time of subsystem 0 and perfect repair time at its failure
$C_{i}, w_{i} \quad$ Cost and time to replace subsystem $i$ for $i=1,2, \ldots, n$
$C_{0 i}, w_{0 i} \quad$ Cost and time to maintenance subsystem 0 and $i$ together, $\forall i, i=1,2, \ldots, n$
$p \quad$ Probability that repair is perfect in section 6.1
$q \quad$ Probability that repair is minimal, $p+q=1$ in Section 6.1
$p(t) \quad$ Probability that maintenance or repair is perfect in Section 6.2
$q(t) \quad$ Probability that maintenance or repair is minimal, $p(t)+q(t)=1$ in Section 6.2
$q_{0 i} \quad$ Probability that the renewal cycle ends with a replacement of subsystem $i$ and PM of subsystem 0 together
$q_{00} \quad$ Probability that the cycle ends with a perfect repair of subsystem 0
$d_{i} \quad$ Probability that the renewal cycle ends on the interval $\left[t_{i}, t_{i+1}\right]$
$L \quad$ Asymptotic system maintenance cost per unit of time
A Asymptotic average system availability
$B \quad$ Random variable: the renewal cycle duration
$D \quad$ Expected duration of a renewal cycle
C Expected system maintenance cost per renewal cycle
$U \quad$ Expected accumulating system failure-free time per renewal cycle
$S_{i} \quad$ Time spent on replacing subsystem $i$ alone, $\forall i, i=1,2, \ldots, n$
$S \quad \sum_{i=1}^{n} S_{i}$
$Y \quad$ Age of subsystem 0 when perfectly repaired or preventively maintained, whichever occurs first
$Z \quad$ Time spent on performing perfect repair or PM on subsystem 0 , possibly with other subsystems (at end of cycle). The minimal repair time is ignored
$V_{i} \quad$ Duration of the interval over which subsystem $i$ alone would be replaced
$R \quad$ Expected system maintenance (down) time per renewal cycle$\varphi(x) \quad$ Probability density function of $Y$
$\lambda_{0}(t), f_{0}(t) \quad$ Failure rate and probability density function of the life of subsystem 0
$F_{0}(t), \bar{F}_{0}(t) \quad$ Cumulative failure distribution and survival function of Subsystem 0

Since this chapter assumes that there exists economic dependence, it spends less cost and time to repair subsystem 0 and any other subsystem together than to repair each subsystem separately, and the optimal action for subsystem 0 depends on the state of the other (exponentially failing) subsystems. Throughout this chapter, we will make such an assumption, i.e.,

$$
C_{0}, C_{i}<C_{0 i}<C_{0}+C_{i} \text { and } w_{0}, w_{i}<w_{0 i}<w_{0}+w_{i}
$$

Radner and Jorgenson (1963) devise an opportunistic maintenance policy. Using a dynamic programming formulation, Radner and Jorgenson show that the optimum replacement policy is what they call a $\left(t_{i}, T\right)$ type of policy. Barlow and Proschan (1975), and Khalil (1985) propose and study such a shut-off rule for system maintenance, which is called shut-off rule 1 in Chapter 1:

While a failed subsystem is in replacement or maintenance, all other subsystems remain in "suspended animation (do not age or fail)". After the repair is completed, the system is returned to operation. At that instant the subsystems in "suspended animation" are as good as they were when the system stopped operating.

The maintenance policy by Radner and Jorgenson (1963) and the shut-off by Barlow and Proschan (1975) and Khalil (1985) are practical in many engineering applications. Let $x$ be the age of subsystem 0 since last replacement of subsystem 0 and $T$ be some fixed time - a decision variable. This chapter considers the following opportunistic maintenance policy, based on the maintenance policy by Radner and Jorgenson (1963), the above shut-off rule used by Barlow and Proschan (1975) and Khalil (1985), and the imperfect repair concepts discussed in Chapter 2:
(i) If subsystem 0 fails at any time before $T$, perform imperfect repair on it at a cost $C_{00}$.
(ii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $0 \leq x<t_{i}$, replace subsystem $i$ alone at a cost $C_{i}$ and at a time $w_{i}$, $\forall i, i=1,2, \ldots, n$.
(iii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $t_{i} \leq x<T$, replace subsystem $i$ and do perfect PM on subsystem 0 , $\forall i, i=1,2, \ldots, n$. The total maintenance cost is $C_{0 i}$ and total maintenance time is $w_{0 i}$.
(iv) If subsystem 0 survives until $x=T$, perform PM on subsystem 0 at a cost $C_{0}$ and at a maintenance time $w_{0}$.Note that in the above maintenance policy the repair before $T$ is imperfect, and PM at $T$, if any, is perfect. The reason for such a policy is that before $T$ the system is young and in a good operating condition and thus no major repair is needed. Therefore, after repair the subsystem is not as good as new. However, when subsystem 0 survives until $x=T$ it is in a bad operating condition and a perfect PM is necessary. The treatment methods for imperfect repair discussed in Chapter 2 will be used in this chapter.

The optimal maintenance policy for this opportunistic maintenance model of multi-component systems is characterized by $n+1$ decision variables, and is obtained by determining the optimal $\left(t_{1}, t_{2}, \ldots, t_{n}, T\right)$ to maximize the system availability or minimize the system maintenance cost rate or optimize one when the requirements for the other are satisfied. It is worth noting that to achieve good operating characteristics of systems, we might take into account system availability because while the system cost rate is minimized the system availability, however, may not achieve an acceptable level, as demonstrated in Chapter 5.

The above maintenance policy is plausible. Since we assume that it spends less cost and time to perform maintenance on subsystem 0 and any other subsystem together than on each subsystem separately, the optimal action for subsystem 0 will depend on the state of other subsystems. If an exponentially failing subsystem, say subsystem $i$, is good at some time, two actions are possible for subsystem 0 : perform maintenance on it or do nothing. If subsystem $i$ has failed, then there are again two possible actions: perform maintenance on the exponentially failing subsystem only or on both subsystems.

From Equation (6.1) we can see that for multi-component systems this opportunistic maintenance policy may result in higher system availability as compared with the case that each subsystem is separately maintained. This is because while any subsystem fails and is under maintenance the whole system is down, and it will save time to do PMs on unfailed subsystems during this down period and thus reduce the system downtime. Therefore, the optimal maintenance model in this chapter can be expected to be effective to approximate any type of multi-component systems.

# 6.1 Optimal Maintenance Policies by the $(p, q)$ Rule 

Suppose that the imperfect repair of subsystem 0 at failure is treated by the $(p, q)$ rule. Given that the perfect repair time is $w_{00}$, note that $C_{00}$ is the imperfect repair cost of subsystem 0 in this case. The PM time at $T$ and the perfect repair time at failure are assumed to be different. In this section, PM of subsystem 0 at $T$ or PM of subsystem 0 together with another subsystem before $T$ are assumed to be perfect. Next we will first derive the long-run system maintenance cost per unit of time, or system maintenance cost rate, and the asymptotic average system availability, and then investigate other system operating characteristics and optimization problems.# 6.1.1 Modeling of Availability and Cost Rate 

Given the above opportunistic PM policy, the times between consecutive perfect repairs or PMs of subsystem 0 constitute a renewal cycle. From the renewal reward theory we have

$$
\begin{gathered}
L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \\
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{gathered}
$$

Note that

$$
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)
$$

Next, without loss of the generality, we assume that $t_{1} \leq t_{2} \leq \cdots \leq t_{n}$. Let us first study the expected duration $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$. The renewal cycle duration $B$ is the sum of three random variables. The duration and expected duration are respectively

$$
\begin{gathered}
B=S+Y+Z \\
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=E(B)=E(S)+E(Y)+E(Z)
\end{gathered}
$$

We evaluate the probability density and mean of $Y$ first. Let $U_{i}$ be the time to failure of subsystem $i$ after $t_{i}$, given that subsystem $i$ is good at $t_{i}(i=1,2, \ldots, n)$, and $U_{0}$ is time to the first perfect repair of subsystem 0 since time 0 . Let $t_{0}=0$. Noting shut-off rule 1 , then,

$$
Y=\min \left(U_{0}+t_{0}, t_{1}+U_{1}, \ldots, t_{n}+U_{n}, T\right)
$$

The random variables $U_{i}(i=1,2, \ldots, n)$ are statistically independent. For $i \neq 0, U_{i}$ has an exponential distribution with failure rate $\lambda_{i}$. Let us denote the cumulative distribution of new subsystem 0 by $F_{0}$. Let $\bar{F}_{0}=1-F_{0}$. We assume that $F_{0}$ is absolutely continuous with density $f_{0}$ and that $F_{0}(0)=0$. The failure rate of subsystem 0 is supposed to be continuous and increasing. The distribution function and failure rate of the time between successive perfect repairs at failure, will be denoted by $H(t)$ and $r_{H}(t)$ respectively. We shall use the relationships, proven by Brown and Proschan (1983), that $\bar{H}(t)=\bar{F}_{0}^{p}(t)$ and $r_{H}(t)=p \lambda_{0}(t)$ where $\bar{H}(t)=1-H(t)$ if there is no PM (see Chapter 2). The density of $H(t)$ is herein denoted by $h(t)$. The cumulative distribution function of $Y$ for $Y<T$ is

$$
\begin{aligned}
1-\operatorname{Pr}(Y>y) & =1-\operatorname{Pr}\left(t_{i}+U_{i}>y, \forall i, i=0,1,2, \ldots, n\right) \\
& =1-\prod_{i=0}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right)
\end{aligned}
$$$$
\begin{aligned}
& =1-\operatorname{Pr}\left(U_{0}>y\right) \prod_{i=1}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& =1-\left[\left(1-F_{0}(y)\right)^{p}\right] \exp \left[-\sum_{\substack{i=1 \\
y-t_{i}>0}}^{n} \lambda_{i}\left(y-t_{i}\right)\right]
\end{aligned}
$$

and for $Y=T$

$$
\operatorname{Pr}(Y=T)=\left[\left(1-F_{0}(T)\right)^{p}\right] \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(T-t_{i}\right)\right]
$$

Next we investigate the probability density of $Y$. For $i=1,2, \ldots, n$, let

$$
\begin{aligned}
M_{i} & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \\
D_{i} & =\exp \left(\sum_{j=1}^{i} \lambda_{j} t_{j}\right) \\
f_{i}(y) & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \exp \left[-\sum_{j=1}^{i} \lambda_{j}\left(y-t_{j}\right)\right] \\
& =D_{i} M_{i} \exp \left(-M_{i} y\right)
\end{aligned}
$$

The distribution of $Y$ has probability density

$$
\varphi(y)=\left\{\begin{array}{cl}
g_{0}(y), & 0 \leq y<t_{1} \\
g_{i}(y), & t_{i} \leq y<t_{i+1} \\
g_{n}(y), & t_{n} \leq y<T
\end{array} \quad \forall i, i=1,2, \ldots, n-1\right.
$$

with probability mass at $Y=T$

$$
G_{0}(T)=\left[1-F_{0}(T)\right]^{p} \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(T-t_{j}\right)\right]=\overline{F_{0}}^{p}(T) D_{n} \exp \left(-M_{n} T\right)
$$

where

$$
g_{i}(y)= \begin{cases}h(y) & i=0 \\ \left(1-F_{0}(y)\right)^{p} f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right] & i=1 \\ \vdots & \\ \left(1-F_{0}(y)\right)^{p} f_{i}(y)+h(y) \exp \left[-\sum_{j=1}^{i} \lambda_{j}\left(y-t_{j}\right)\right] & i=2,3, \ldots, n-1 \\ \vdots & \\ \left(1-F_{0}(y)\right)^{p} f_{n}(y)+h(y) \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(y-t_{j}\right)\right] & i=n\end{cases}
$$

Therefore, the expected value of $Y$ is given by$$
E(Y)=\sum_{i=0}^{n} \int_{t_{i}}^{t_{i-1}} y g_{i}(y) \mathrm{d} y+T G_{0}(T)
$$

where $t_{n+1}=T$.
Second, we derive the expected value of $S$. According to the previous definition, $V_{i}$ is the duration of the interval over which subsystem $i$ alone would be replaced if it were to fail $(i=1,2, \ldots n)$. Then

$$
\begin{array}{ll}
V_{i}=\min \left(Y, t_{i}\right) & \forall i, i=1,2, \ldots n \\
E\left(S_{i}\right)=\lambda_{i} E\left(V_{i}\right) w_{i} & \forall i, i=1,2, \ldots n
\end{array}
$$

Note that $V_{i}$ has a probability density equal to that of $Y$ for $Y<t_{i}$, and probability mass $\operatorname{Pr}\left(Y=t_{i}\right)$ concentrated at $t_{i}$. Therefore,

$$
E\left(V_{i}\right)=\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j-1}} y g_{i}(y) d y+t_{i}\left[1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i-1}} g_{i}(y) d y\right]
$$

Recall that $S=\sum_{i=1}^{n} S_{i}$
Then

$$
\begin{aligned}
E(S) & =\sum_{i=1}^{n} E\left(S_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i} E\left(V_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i-1}} y g_{i}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i-1}} g_{i}(y) d y\right)\right]
\end{aligned}
$$

Finally, let us derive an expression for $E(Z)$. Denote by $d_{i}$ the probability that the renewal cycle ends on the interval $\left[t_{i}, t_{i+1}\right]$ :

$$
d_{i}=\operatorname{Pr}\left(t_{i} \leq Y \leq t_{i+1}\right), \quad \forall, i=0,1,2, \ldots, n, t_{0}=0, t_{n+1}=T
$$

Then

$$
\begin{aligned}
& d_{0}=\int_{0}^{t_{1}} g_{0}(y) d y \\
& d_{1}=\left(1-d_{0}\right) \int_{t_{1}}^{t_{2}}\left(1-F_{0}(y)\right)^{p} f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right] d y
\end{aligned}
$$$$
\begin{aligned}
& d_{2}=\left(1-d_{0}\right)\left(1-\alpha_{1}\right) \int_{t_{2}}^{t_{1}}\left[\left(1-F_{0}(y)\right)^{p} f_{2}(y)+h(y) \exp \left(-\sum_{j=1}^{2} \lambda_{j}\left(y-t_{j}\right)\right)\right] d y \\
& d_{i}=\prod_{j=0}^{i-1}\left(1-\alpha_{j}\right) \alpha_{j} \\
& d_{n+1}=G_{0}(T)
\end{aligned}
$$

where $\alpha_{0}=d_{0}$ and

$$
\alpha_{j}=\int_{t_{j}}^{t_{j+1}}\left[\left(1-F_{0}(y)\right)^{p} f_{j}(y)+h(y) \exp \left(-\sum_{i=1}^{j} \lambda_{i}\left(y-t_{i}\right)\right)\right] d y
$$

Let $q_{0 i}$ represents the probability that the renewal cycle ends with a replacement of subsystem $i$ and subsystem 0 together. Then

$$
q_{0 i}=\sum_{j=i}^{n}\left(1-d_{j-1}\right) \int_{t_{j}}^{t_{j+1}}\left(1-F_{0}(y)\right)^{p} f_{j}(y) d y \quad \forall i, i=1,2, \ldots, n
$$

and $q_{00}$, the probability that the cycle ends with a perfect repair of subsystem 0 , is

$$
q_{00}=d_{0}+\sum_{j=i}^{n}\left(1-d_{j-1}\right) \int_{t_{j}}^{t_{j+1}} h(y) \exp \left(-\sum_{i=1}^{j} \lambda_{i}\left(y-t_{i}\right)\right) d y
$$

It follows that the third term in Equation (6.4) is given by

$$
E(Z)=\sum_{j=i}^{n} q_{0 i} w_{0 i}+d_{n+1} w_{0}
$$

This completes the derivation of the expected duration $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ in Equation (6.4).

Next we derive the expected system maintenance cost rate. Noting that the expected number of replacements of subsystem $i$ alone is $\lambda_{i} E\left(V_{i}\right)$ we obtain the corresponding expected replacement cost for subsystem $i$ in one renewal cycle as $\lambda_{i} E\left(V_{i}\right) C_{i}$ where $i=1,2, \ldots, n$. The probability of a replacement of subsystem 0 and $i$ together multiplied by the corresponding cost is $q_{0 i} C_{0 i}, \forall i, i=1, \ldots, n$. Using Lemma 2.1 of Fontenot and Proschan (1984), the probability that subsystem 0 is subject to PM at $T$, multiplied by the sum of the costs of PM at $T$ and minimal repair of subsystem 0 during $[0, T]$, results in

$$
d_{n+1}\left[C_{0}+C_{00} q \int_{0}^{T} \lambda_{0}(t) d t\right] \quad \text { or } \quad G_{0}(T)\left[C_{0}+C_{00} q \int_{0}^{T} \lambda_{0}(t) d t\right]
$$The probability that subsystem 0 is subject to perfect repair at its failure in the time interval $[0, T)$, multiplied by the cost of repair at its failure is $q_{00} C_{00}$. Due to the same lemma of Fontenot and Proschan (1984), the expected minimal repair cost of subsystem 0 during a single renewal cycle, if the renewal cycle ends with a perfect repair of subsystem 0 , alone or together with another subsystem, is given by

$$
\begin{aligned}
\mathrm{C}_{\text {mini }}= & C_{00} \int_{0}^{T}\left[q \int_{0}^{y} \lambda_{0}(t) d t\right] \varphi(y) d y \\
= & C_{00} \int_{0}^{T}\left[\int_{0}^{y} q \lambda_{0}(t) d t\right] h(y) d y \\
& +C_{00} \int_{t_{n}}^{t_{1}}\left[\int_{0}^{y} q \lambda_{0}(t) d t\right]\left[\left(1-F_{0}(y)\right)^{p} f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right]\right] d y+\cdots \\
& +C_{00} \int_{t_{n}}^{T}\left[\int_{0}^{y} q \lambda_{0}(t) d t\right]\left[\left(1-F_{0}(y)\right)^{p} f_{n}(y)+h(y) \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(y-t_{j}\right)\right]\right] d y
\end{aligned}
$$

It follows that the expected system maintenance cost during one renewal cycle

$$
\begin{aligned}
& C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) \\
& =\sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i}+\sum_{i=0}^{n} q_{0 i} C_{0 i}+C_{00} \int_{0}^{T}\left[\int_{0}^{y} q \lambda_{0}(t) d t\right] \varphi(y) d y \\
& \quad+d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q \lambda_{0}(t) d t\right]
\end{aligned}
$$

Substituting the above results into Equations (6.2) and (6.3), and noting the relationships

$$
E(Y)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) \text { and } \mathrm{E}(\mathrm{~S}+\mathrm{Z})=R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)
$$

we have the following proposition:
Proposition 6.1 The long-run system maintenance cost per unit of time, or system maintenance cost rate, and the asymptotic average system availability are respectively:

$$
\begin{aligned}
& L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
& \frac{\sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i}+\sum_{i=0}^{n} q_{0 i} C_{0 i}+q C_{00} \int_{0}^{T}\left[\int_{0}^{y} \lambda_{0}(t) d t\right] \varphi(y) d y+d_{n+1}\left[C_{0}+q C_{00} \int_{0}^{T} \lambda_{0}(t) d t\right]}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \\
& A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{E(Y)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{aligned}
$$From Proposition 6.1, the optimal opportunistic PM policy $\left(T^{*}, t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}\right)$ that minimizes the system maintenance cost rate or that maximizes the system availability can be obtained by a nonlinear programming software. Obviously, it would be difficult to obtain the analytical optimal solution.

Next we discuss the other operating characteristics of this opportunistic PM model.

# 6.1.2 Other Operating Characteristics 

To evaluate the performance of the imperfect opportunistic PM policy in this chapter, and to predict supply and maintenance requirements, let us investigate its other operating characteristics besides system maintenance cost rate and availability. First, we note that for this imperfect maintenance model, four different maintenance actions are observed:
(i) Repair of a failed subsystem 0 .
(ii) Replacement of a failed part with a constant failure rate by itself.
(iii) The joint opportunistic maintenance of a failed subsystem with a constant failure rate and subsystem 0 unfailed.
(iv) Perfect maintenance of subsystem 0 unfailed at age $T$.

In addition to the system availability and maintenance cost rate derived in the last section, other important operating characteristics of this maintenance policy are the expected number of each of these maintenance actions per unit time, and expected maintenance cost of each of these maintenance actions per unit time. Another characteristic of interest is the probability of at least $m$ failures of one of the subsystems in the interval $(0, t)$ (see McCall 1963). In this section, the following operating characteristics will be investigated:
$r_{00} \quad$ Expected rate of perfect repair of subsystem 0
$r_{0 f} \quad$ Expected rate of failure of subsystem 0
$r_{i} \quad$ Expected rate of failure of subsystem $i, \forall i, i=1,2, \ldots, n$
$r_{0 i} \quad$ Expected rate of joint opportunistic replacement of failed subsystem $i$ and unfailed subsystem $0, \forall i, i=1,2, \ldots, n$
$r_{0} \quad$ Expected rate of PM of subsystem 0 at age $T$
$r_{0 p} \quad$ Expected rate of total perfect maintenance of subsystem 0
$c_{00} \quad$ Expected rate of expenditure on repair of failed subsystem 0
$c_{i} \quad$ Expected rate of expenditure on replacement of subsystem $i$
$c_{0 i} \quad$ Expected rate of expenditure on joint replacement of subsystems 0 and $i$
$c_{0} \quad$ Expected rate of expenditure on PM of subsystem 0 at age $T$
$P_{i}(m, t) \quad$ Probability of at least $m$ failures of subsystem $i$ in the interval $(0, t)$,

$$
\forall i, i=0,1, \ldots, n
$$Let us consider the subsystems with constant failure rates first. Clearly,

$$
r_{i}=\lambda_{i} \quad \forall i, i=1,2, \ldots, n
$$

or including $w_{i}$, the time to replace subsystem $i$,

$$
r_{i}=\frac{1 / \lambda_{i}}{1 / \lambda_{i}+w_{i}}=\frac{\lambda_{i}}{\lambda_{i} w_{i}+1} \quad \forall i, i=1,2, \ldots, n
$$

Therefore,

$$
c_{i}=r_{i} C_{i}=\frac{\lambda_{i} C_{i}}{\lambda_{i} w_{i}+1} \quad \forall i, i=1,2, \ldots, n
$$

Using the elementary renewal theorem we obtain that the rate of perfect maintenance of subsystem 0 , is asymptotically equal to the reciprocal of the expected value of $Y$, the time to the first perfect maintenance of subsystem 0 , that is,

$$
\lim _{t \rightarrow \infty} r_{0 p}(t)=[E(Y)]^{-1}
$$

Thus, for large value of $t$

$$
r_{0 p} \approx[E(Y)]^{-1}
$$

On the other hand, from the foregoing definitions for rates of maintenance,

$$
r_{0 p}=r_{0}+r_{00}+\sum_{i=1}^{n} r_{0 i}
$$

That is, this expected value, $r_{0 p}$, can be partitioned into three parts: the expected rate of PM at age $T$, the expected rate of repair of subsystem 0 at failure, the expected rate of joint opportunistic replacement with another subsystem. We can also see this relationship from the derivation of Equation (6.8). By the law of large numbers, the fraction of the total number of replacements of subsystem 0 that are preventive is equal to $p_{1}$, the probability that, starting with a new subsystem 0 , this subsystem will not be replaced in the interval $(0, t)$. From Equation (6.7) of Section 6.1.1, we have

$$
p_{1}=\left[1-F_{0}(T)\right]^{p} \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(T-t_{j}\right)\right]
$$

Hence, in the long run, the expected rate of PM of subsystem 0 is

$$
r_{0} \approx p_{1}[E(Y)]^{-1}
$$

or, including replacement and maintenance time,

$$
r_{0} \approx \frac{p_{1}[E(Y)]^{-1}}{p_{1}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{p_{1}}{p_{1}[E(Z)+E(S)]+E(Y)}
$$The expected expenditure on PM is given by

$$
c_{0}=r_{0} C_{0}=\frac{p_{1} C_{0}}{p_{1}[E(Z)+E(S)]+E(Y)}
$$

Hence, in the long run, $\sum_{0}^{n} r_{0 i}$, the expected rate of repair of subsystem 0 plus the expected rate of joint opportunistic replacement of subsystem 0 is given by

$$
r_{f j}=\sum_{0}^{n} r_{0 i}=\left(1-p_{1}\right)[E(Y)]^{-1}
$$

From Section 6.1.1,

$$
1-p_{1}=\sum_{0}^{n} q_{0 i}
$$

where $q_{o i} \mathrm{~s}$ are given by Equations (6.11) and (6.12).
Therefore,

$$
r_{f j}=[E(Y)]^{-1} \sum_{0}^{n} q_{0 i}
$$

Since the probability that subsystem 0 will be replaced jointly with subsystem $i$ is $q_{0 i}$, the asymptotic expected rate of opportunistic replacement of subsystem 0 and $i$ is given by

$$
r_{0 i}=q_{0 i}[E(Y)]^{-1} \quad \forall i, i=1,2, \ldots, n
$$

Noting that $q_{00}$ is the probability that subsystem 0 will be perfectly repaired at failure, we have

$$
r_{00}=q_{00}[E(Y)]^{-1}
$$

or including maintenance time,

$$
r_{0 i}=\frac{q_{0 i}[E(Y)]^{-1}}{q_{o i}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{q_{0 i}}{q_{o i}[E(Z)+E(S)]+E(Y)} \quad \forall i, i=1,2, \ldots, n
$$

and

$$
r_{00}=\frac{q_{00}[E(Y)]^{-1}}{q_{00}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{q_{00}}{q_{00}[E(Z)+E(S)]+E(Y)}
$$

Accordingly, the expected rate of expenditure on opportunistic replacements is

$$
c_{0 i}=r_{0 i} C_{0 i}=\frac{q_{0 i} C_{0 i}}{q_{o i}[E(Z)+E(S)]+E(Y)} \quad \forall i, i=1,2, \ldots, n
$$

Since the repair of subsystem 0 at failure is perfect with probability $p$, the rate of failure of subsystem 0 is given by$$
r_{0 f}=r_{00} / p=\frac{q_{00}}{q_{00}[E(Z)+E(S)]+E(Y)} \frac{1}{p}
$$

Accordingly, the expected rate of expenditure on repair of subsystem 0 at failure is

$$
c_{00}=r_{0 f} C_{00}=\frac{q_{00} C_{00}}{q_{00}[E(Z)+E(S)]+E(Y) \frac{1}{p}}
$$

Because the lifetime of subsystem $i$ follows the exponential distribution, the probability of at least $m$ replacements of subsystem $i$ in the interval $(0, t)$ is

$$
P_{i}(m, t)=\sum_{j=m}^{\infty} \exp \left(-\lambda_{i} t\right) \cdot \frac{\left(\lambda_{i} t\right)^{j}}{j!} \quad \forall i, i=1, \ldots, n
$$

# 6.1.3 Optimization Models 

So far we have derived the system reliability measures: system availability, expected rate of failure of subsystem 0 , expected rate of failure of subsystem $i$, etc., and system maintenance cost measures: system maintenance cost rate, expected rate of expenditure on repair of failed subsystem 0 , expected rate of expenditure on replacement of subsystem $i$, etc. To obtain the optimal system maintenance policies the system reliability measures and system maintenance cost measures must be both acceptable. For example, if it is required that while the expected rate of failure of subsystem 0 is less than $A_{0}$ the system maintenance cost rate is minimized. For such a problem, we can formulate the following optimization model from Equations (6.15) and (6.33):

## Minimize

$$
\begin{aligned}
& L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
& \frac{\sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i}+\sum_{i=0}^{n} q_{0 i} C_{0 i}+q C_{00} \int_{0}^{T}\left[\int_{0}^{y} \lambda_{0}(t) d t\right] \varphi(y) d y+d_{n+1}\left[C_{0}+C_{00} q \int_{0}^{T} \lambda_{0}(t) d t\right]}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{aligned}
$$

Subject to

$$
\left\{\begin{array}{l}
r_{0 f}=\frac{q_{00}}{q_{00}[E(Z)+E(S)]+E(Y)} \frac{1}{p} \leq r^{+} \\
t_{1}, t_{2}, \ldots, t_{n}, T \geq 0
\end{array}\right.
$$

where $r^{+}$is the predetermined requirement for expected rate of failure of subsystem 0 .This model can be solved by nonlinear programming software to obtain an optimal system maintenance policy $\left(t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}, T^{*}\right)$.

# 6.2 Optimal Maintenance Policies by the $(p(t), q(t))$ Rule 

Suppose that the imperfect repair of subsystem 0 at failure is treated by the $(p(t), q(t))$ rule introduced in Section 2.1.1. Note that $C_{00}$ is the imperfect repair cost of subsystem 0 in this case, and the PM time at $T$ and the perfect repair time at failure are assumed to be different. In this section, PM of subsystem 0 at $T$ or PM of subsystem 0 together with another subsystem before $T$ are assumed to be perfect. Next we will derive the long-run system maintenance cost per unit of time, or system maintenance cost rate, and the asymptotic average system availability.

### 6.2.1 Modeling of Availability and Cost Rate

Given that the above opportunistic PM policy, the times between consecutive perfect repairs or PMs of subsystem 0 constitute a renewal cycle. From the renewal reward theory,

$$
\begin{gathered}
L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \\
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{gathered}
$$

Note that

$$
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)
$$

Next without loss of the generality we assume that $t_{1} \leq t_{2} \leq \cdots \leq t_{n}$. Let us first investigate the expected duration $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$. The renewal cycle duration $B$ is the sum of three random variables. The duration and expected duration are respectively

$$
\begin{aligned}
B & =S+Y+Z \\
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) & =E(B) \\
& =E(S)+E(Y)+E(Z)
\end{aligned}
$$

For the three terms in Equation (6.38), we evaluate the probability density and mean of $Y$ first. Let $U_{i}$ be the time to failure of subsystem $i$ after $t_{i}$, given that subsystem $i$ is good at $t_{i}(i=1,2, \ldots, n)$, and $U_{0}$ is time to the first perfect repair of subsystem 0 since time 0 . Let $t_{0}=0$. Noting shut-off rule 1 , then$$
Y=\min \left(U_{0}+t_{0}, t_{1}+U_{1}, \ldots, t_{n}+U_{n}, T\right)
$$

The random variables $U_{i}(i=1,2, \ldots, n)$ are statistically independent. For $i \neq 0, U_{i}$ has an exponential distribution with constant failure rate $\lambda_{i}$. Denote the $c d f$ of new subsystem 0 by $F_{0}$. Let $\bar{F}_{0}=1-F_{0}$. We assume that $F_{0}$ is absolutely continuous with density $f_{0}$ and that $F_{0}(0)=0$. The failure rate, $\lambda_{0}(t)$, of subsystem 0 is supposed to be continuous and increasing. The $c d f$ and failure rate of the time between successive perfect repairs of subsystem 0 at failures will be denoted by $H(t)$ and $r_{H}(t)$ respectively. We shall use the facts, proven by Block et al. (1985), that

$$
\bar{H}(t)=\exp \left[-\int_{0}^{t} p(x) \lambda_{0}(x) d x\right] \text { and } r_{H}(t)=p(t) \lambda_{0}(t)
$$

where $\bar{H}(t)=1-H(t)$, given that there is no PM and $\int_{0}^{\infty} p(x) \bar{F}_{0}^{-1}(x) F_{0}(d x)=+\infty$ (see Chapter 2). The derivative of $H(t)$ is herein denoted by $h(t)$.

It is easy to verify that the cumulative distribution function of $Y$ for $Y<T$ is given by

$$
\begin{aligned}
1-\operatorname{Pr}(Y>y) & =1-\operatorname{Pr}\left(t_{i}+U_{i}>y, \forall i, i=0,1,2, \ldots, n\right) \\
& =1-\prod_{i=0}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& =1-\operatorname{Pr}\left(U_{0}>y\right) \prod_{i=1}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& =1-\exp \left[-\int_{0}^{x} p(x) \lambda_{0}(x) d x\right] \exp \left[-\sum_{\substack{i=1 \\
y \geq t_{i}}}^{n} \lambda_{i}\left(y-t_{i}\right)\right]
\end{aligned}
$$

and for $Y=T$

$$
\operatorname{Pr}(Y=T)=\exp \left[-\int_{0}^{T} p(x) \lambda_{0}(x) d x\right] \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(T-t_{i}\right)\right]
$$

Now we evaluate the probability density function of $Y$. For $i=1,2, \ldots, n$, let

$$
\begin{aligned}
M_{t} & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \\
D_{i} & =\exp \left(\sum_{j=1}^{i} \lambda_{j} t_{j}\right) \\
f_{i}(y) & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \exp \left[-\sum_{j=1}^{i} \lambda_{j}\left(y-t_{j}\right)\right] \\
& =D_{i} M_{t} \exp \left(-M_{t} y\right)
\end{aligned}
$$

Then the distribution of $Y$ has probability density$$
\varphi(y)=\left\{\begin{array}{l}
g_{0}(y), 0 \leq y<t_{1} \\
g_{i}(y), t_{i} \leq y<t_{i+1} \\
g_{n}(y), t_{n} \leq y<T
\end{array} \quad \forall i, i=1,2, \ldots, n-1\right.
$$

with probability mass at $Y=T$

$$
\begin{aligned}
G_{0}(T) & =\exp \left[-\int_{0}^{T} p(x) \lambda_{0}(x) d x\right] \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(T-t_{j}\right)\right] \\
& =\exp \left[-\int_{0}^{T} p(x) \lambda_{0}(x) d x\right] D_{n} \exp \left(-M_{n} T\right)
\end{aligned}
$$

where

$$
g_{i}(y)= \begin{cases}h(y) & i=0 \\ \exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right] & i=1 \\ \vdots & \\ \exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{i}(y)+h(y) \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(y-t_{j}\right)\right] & i=2,3, \ldots, n-1 \\ \vdots & \\ \exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{n}(y)+h(y) \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(y-t_{j}\right)\right] & i=n\end{cases}
$$

Therefore, the expected value of $Y$ is given by

$$
E(Y)=\sum_{i=0}^{n} \int_{t_{i}}^{t_{i+1}} y g_{i}(y) \mathrm{d} y+T G_{0}(T)
$$

where $t_{n+1}=T$.
Second, we explore the expected value of $S$. According to the previous definition, $V_{i}$ is the duration of the interval over which subsystem $i$ alone would be replaced if it were to fail $(i=1,2, \ldots n)$. Then

$$
\begin{array}{ll}
V_{i}=\min \left(Y, t_{i}\right) & \forall i, i=1,2, \ldots n \\
E\left(S_{i}\right)=\lambda_{i} E\left(V_{i}\right) w_{i} & \forall i, i=1,2, \ldots n
\end{array}
$$

Note that $V_{i}$ has a probability density equal to that of $Y$ for $Y<t_{i}$, and probability mass $\operatorname{Pr}\left(Y=t_{i}\right)$ concentrated at $t_{i}$. Therefore,

$$
E\left(V_{i}\right)=\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i+1}} y g_{i}(y) d y+t_{i}\left[1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i+1}} g_{i}(y) d y\right]
$$Recall that $S=\sum_{i=1}^{n} S_{i}$
Then

$$
\begin{aligned}
E(S) & =\sum_{i=1}^{n} E\left(S_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i} E\left(V_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} y g_{i}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} g_{i}(y) d y\right)\right]
\end{aligned}
$$

Finally, let us derive an expression for $E(Z)$. Denote by $d_{i}$ the probability that the renewal cycle ends on the interval $\left[t_{i}, t_{i+1}\right]$ :

$$
d_{i}=\operatorname{Pr}\left(t_{i} \leq Y \leq t_{i+1}\right), \quad \forall, i=0,1,2, \ldots, n, t_{0}=0, t_{n+1}=T
$$

Then

$$
\begin{aligned}
d_{0}= & \int_{0}^{t_{1}} g_{0}(y) d y \\
d_{1}= & \left(1-d_{0}\right) \int_{t_{1}}^{t_{2}}\left\{\exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right]\right\} d y \\
d_{2}= & \left(1-d_{0}\right)\left(1-\alpha_{1}\right) \\
& \times \int_{t_{2}}^{t_{2}}\left\{\exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{2}(y)+h(y) \exp \left(-\sum_{j=1}^{2} \lambda_{j}\left(y-t_{j}\right)\right)\right\} d y \\
& \vdots \\
d_{i}= & \prod_{j=0}^{i-1}\left(1-\alpha_{j}\right) \alpha_{j} \\
& \vdots \\
d_{n+1}= & G_{0}(T)
\end{aligned}
$$

where $\alpha_{0}=d_{0}$ and

$$
\alpha_{j}=\int_{t_{j}}^{t_{j+1}}\left\{\exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{j}(y)+h(y) \exp \left(-\sum_{i=1}^{j} \lambda_{i}\left(y-t_{i}\right)\right)\right\} d y
$$

Let $q_{0 i}$ represents the probability that the renewal cycle ends with a replacement of subsystem $i$ and subsystem 0 together. Then,$$
q_{0 i}=\sum_{j=i}^{n}\left(1-d_{j-1}\right) \int_{t_{j}}^{t_{j-1}} f_{j}(y) \exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] d y \quad \forall i, i=1,2, \ldots, n
$$

and $q_{00}$, the probability that the cycle ends with a perfect repair of subsystem 0 , is given by

$$
q_{00}=d_{0}+\sum_{j=i}^{n}\left(1-d_{j-1}\right) \int_{t_{j}}^{t_{j-1}} h(y) \exp \left(-\sum_{i=1}^{j} \lambda_{i}\left(y-t_{i}\right)\right) d y
$$

It follows that the third term in Equation (6.38) is given by

$$
E(Z)=\sum_{j=i}^{n} q_{0 i} w_{0 i}+d_{n+1} w_{0}
$$

This completes the derivation of the expected duration $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$.
Now we derive the expected system maintenance cost rate. Noting that the expected number of replacements of subsystem $i$ alone is $\lambda_{i} E\left(V_{i}\right)$, it follows that the corresponding expected replacement cost for subsystem $i$ in one renewal cycle is $\lambda_{i} E\left(V_{i}\right) C_{i}, i=1,2, \ldots, n$. The probability of a replacement of subsystem 0 and $i$ together multiplied by the corresponding cost is $q_{0 i} C_{0 i}, \forall i, i=1,2, \ldots, n$. The probability that subsystem 0 alone is subject to perfect repair at its failure in the time interval $(0, T)$, multiplied by the cost of repair at its failure is $q_{00} C_{00}$.

Next we investigate the expected imperfect repair cost of subsystem 0 during a single renewal cycle. Consider the non-homogeneous Poisson process $\{N(t), t>0\}$ with intensity function $\lambda_{0}(t)$ and successive arrival times $s_{1}, s_{2}, \ldots$ At time $s_{n}$ we flip a coin. Designate the outcome by $W_{n}$ which takes the value 1 (head) with probability $p\left(s_{n}\right)$ and the value 0 (tail) with probability $q\left(s_{n}\right)$. Let

$$
\begin{aligned}
I(t) & =\sum_{n=1}^{N(t)} W_{n} \\
M(t) & =N(t)-I(t)
\end{aligned}
$$

According to Savits (1988), the processes $\{I(t), t \geq 0\}$ and $\{M(t), t \geq 0\}$ are independent non-homogeneous Poisson processes with respective intensities $p(t) \lambda_{0}(t)$ and $q(t) \lambda_{0}(t)$. Hence, the conditional probability that $k$ minimal repairs occur given that no perfect repair in $[0, y]$ is given by

$$
\begin{aligned}
P\{M(y)=k \mid I(y)=0\} & =P\{M(y)=k\} \\
& =\frac{\exp \left[-\int_{0}^{y} q(t) \lambda_{0}(t) d t\right] \cdot\left[\int_{0}^{y} q(t) \lambda_{0}(t) d t\right]^{k}}{k!}
\end{aligned}
$$with mean of $\int_{0}^{t} q(t) \lambda_{0}(t) d t$.
Using the foregoing result of Savits (1988), the probability that subsystem 0 is subject to PM at $T$, multiplied by the sum of the costs of PM at $T$ and minimal repair of subsystem 0 during $[0, T]$, results in

$$
d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q(t) \lambda_{0}(t) d t\right]
$$

Using this result by Savits (1988) again, the expected minimal repair cost of subsystem 0 during a single renewal cycle, if the renewal cycle ends with a perfect repair of subsystem 0 , alone or together with another subsystem, is given by

$$
\begin{aligned}
C_{\text {mini }} & =C_{00} \int_{t_{1}}^{T}\left[\int_{0}^{y} q(t) \lambda_{0}(t) d t\right] \varphi(y) d y \\
& =C_{00} \int_{0}^{t_{2}} \Psi(y) \cdot h(y) d y \\
& \left.+C_{00} \int_{t_{1}}^{t_{2}} \Psi(y)\left\{\exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{1}(y)+h(y) \exp \left[-\lambda_{1}\left(y-t_{1}\right)\right]\right\} d y+\ldots \\
& +C_{00} \int_{t_{n}}^{T} \Psi(y)\left\{\exp \left[-\int_{0}^{y} p(x) \lambda_{0}(x) d x\right] f_{n}(y)+h(y) \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(y-t_{j}\right)\right]\right\} d y
\end{aligned}
$$

where

$$
\Psi(y)=\int_{0}^{y} q(t) \lambda_{0}(t) d t
$$

From the above analysis it follows that the expected system maintenance cost during one renewal cycle is given by

$$
\begin{aligned}
C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= & \sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i} \\
& \left.+\sum_{i=0}^{n} q_{0 i} C_{0 i}+C_{00} \int_{0}^{T}\left[\int_{0}^{y} q(t) \lambda_{0}(t) d t\right] \varphi(y) d y\right. \\
& +d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q(t) \lambda_{0}(t) d t\right] \\
= & \sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i} \\
& +\sum_{i=0}^{n} q_{0 i} C_{0 i}+C_{00} \int_{0}^{T} \Psi(y) \cdot \varphi(y) d y+d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q(t) \lambda_{0}(t) d t\right]
\end{aligned}
$$Substituting the above results into Equations (6.36) and (6.37), and noting that $E(Y)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ and $\mathrm{E}(\mathrm{S}+\mathrm{Z}) \equiv R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$, the following result follows:

Proposition 6.2 The long-run system maintenance cost per unit of time, or system maintenance cost rate, and the asymptotic average system availability are, respectively,

$$
\begin{aligned}
& L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
& \frac{\sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i}+\sum_{i=0}^{n} q_{0 i} C_{0 i}+C_{00} \int_{0}^{T} \Psi(y) \cdot \varphi(y) d y+d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q(t) \lambda_{0}(t) d t\right]}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{aligned}
$$

$$
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{E(Y)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
$$

From Proposition 6.2, the optimal opportunistic PM policy $\left(T^{*}, t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}\right)$ to minimize the system maintenance cost rate or to maximize the system availability can be obtained by a nonlinear programming software. Next we discuss the other operating characteristics of this opportunistic PM model.

# 6.2.2 Other Performance Measures 

As in Section 6.1.2, we can derive other important operating characteristics of this policy, such as the expected number of each of these maintenance actions per unit time, and expected maintenance cost of each of these maintenance actions per unit time, in addition to the system availability and maintenance cost rate derived in Section 6.2.1. For example, using the elementary renewal theorem, the rate of perfect maintenance of subsystem 0 , is asymptotically equal to the reciprocal of the expected value of $Y$, the time to the first perfect maintenance of subsystem 0 , i.e.,

$$
\lim _{t \rightarrow \infty} r_{0 p}(t)=[E(Y)]^{-1}
$$

Thus, for large value of $t$,

$$
r_{0 p} \approx[E(Y)]^{-1}
$$

On the other hand, from the definitions for rates of maintenance (replacement),

$$
r_{0 p}=r_{0}+r_{00}+\sum_{i}^{n} r_{0 i}
$$

That is, this expected value, $r_{0 p}$, can be partitioned into three parts: the expected rate of PM at age $T$, the expected rate of perfect repair of subsystem 0 at failure, and the expected rate of joint opportunistic replacement with anothersubsystem. We can also see this relationship from the derivation of Equation (6.41). By the law of large numbers, the fraction of the total number of perfect maintenance of subsystem 0 that is preventive equals $p_{1}$, the probability that, starting with a new subsystem 0 , this subsystem will not be perfectly maintained in the interval $(0, T)$. From Equation (6.40) of Section 6.2.1, we have

$$
p_{1}=\exp \left[-\int_{0}^{T} p(t) \lambda_{0}(t) d t\right] \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(T-t_{j}\right)\right]
$$

where $p(t)$ is the probability that a repair of subsystem 0 at failure is perfect. Hence, in the long run, the expected rate of PM of subsystem 0 is

$$
r_{0} \approx p_{1}[E(Y)]^{-1}
$$

or, including replacement and maintenance time,

$$
r_{0} \approx \frac{p_{1}[E(Y)]^{-1}}{p_{1}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{p_{1}}{p_{1}[E(Z)+E(S)]+E(Y)}
$$

Hence, in the long run, $\sum_{0}^{n} r_{0 i}$, the expected rate of perfect repair of subsystem 0 plus the expected rate of joint opportunistic replacement of subsystem 0 is:

$$
r_{f j}=\sum_{0}^{n} r_{0 i}=\left(1-p_{1}\right)[E(Y)]^{-1}
$$

From Section 6.2.1,

$$
1-p_{1}=\sum_{0}^{n} q_{0 i}
$$

where $q_{0 i} \mathrm{~s}$ are given by Equations (6.44) and (6.45).
Therefore,

$$
r_{f j}=[E(Y)]^{-1} \sum_{0}^{n} q_{0 i}
$$

Other operating characteristics can be derived in a way similar to Section 6.1.2. Results can be found in Wang (1997).

# 6.2.3 Optimal Maintenance Policy 

To obtain the optimal system maintenance policies, the system reliability measures and system maintenance cost measures must both be acceptable. Based on the obtained system reliability measures - system availability, expected rate of failure of subsystem 0 , expected rate of failure of subsystem $i$, etc., and system maintenance cost measures - system maintenance cost rate, expected rate of expenditure on repair of failed subsystem 0 , expected rate of expenditure on replacement of subsystem $i$, etc., we can formulate different optimization models. For example, based on Equations (6.49) and (6.50), we can have the following optimization model:# Maximize 

$$
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{E(Y)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
$$

## Subject to

$$
\left\{\begin{array}{l}
L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
\frac{\sum_{i=1}^{n} \lambda_{i} E\left(V_{i}\right) C_{i}+\sum_{i=0}^{n} q_{0 i} C_{0 i}+C_{00} \int_{0}^{T} \Psi(y) \varphi(y) d y+d_{n+1}\left[C_{0}+C_{00} \int_{0}^{T} q(t) \lambda_{0}(t) d t\right]}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \leq \varpi \\
t_{1}, t_{2}, \ldots, t_{n}, T \geq 0
\end{array}\right.
$$

where $\varpi$ is the predetermined requirement for the rate of perfect maintenance of subsystem 0 .

The above optimization model can be solved by nonlinear programming software to obtain the optimal system maintenance policy $\left(t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}, T^{*}\right)$.

### 6.3 Concluding Remarks

The optimal maintenance of a system with $n+1$ subsystems is studied in this chapter. We assume that in this system there is economic dependency, i.e., both maintenance costs and times are less for several subsystems simultaneously than for each subsystem taken separately. We also suppose that repair is imperfect and the imperfect repair is modeled by the $(p, q)$ rule and $(p(t), q(t))$ rule. The realistic shut-off rule is used in this chapter. The system availability, system maintenance cost rate, and other operating characteristics of this multi-unit system are derived and the optimum system maintenance policies to optimize the system operating characteristics are proposed.

For multi-component systems the opportunistic maintenance policy in this chapter may result in higher system availability as compared with the case that each subsystem is separately maintained. This is because while any subsystem fails and is under maintenance the whole system is down, and it will save time to do PMs on unfailed subsystems during this down period and thus reduce the system downtime.

Noting the relationship between the $(p, q)$ rule and $(p(t), q(t))$ rule, the results in Section 6.2 are general. Both the $(p, q)$ rule and $(p(t), q(t))$ rule are convenient to model imperfect maintenance of multi-component systems.

Different from single component systems, one of the key problems for multicomponent systems is economic dependence. Imperfectness of maintenance is another important factor. This chapter considers both factors which affect optimalmaintenance policies of multi-unit systems and produces some results on this aspect. The maintenance policies are realistic and the results obtained in this chapter can be expected to be useful in practice. Further work includes extending this work to multi-unit systems with two or more IFR subsystems which are subject to imperfect maintenance and economic dependence or considering other shut-off rules. Various shut-off rules for system maintenance can be found in Khalil (1985).# Optimal Preparedness Maintenance of Multi-unit Systems with Imperfect Maintenance and Economic Dependence 

A system is placed in storage and is called on to perform a given task only if a specific but unpredictable emergency occurs. Some maintenance actions may be taken while the system is in storage and the objective is to choose the sequence of maintenance actions resulting in the highest level of system "preparedness for field use". This maintenance policy is known as the preparedness maintenance policy (McCall 1963). In Menipaz (1978), various inspection and preparedness models are examined, which deal with stochastically failing systems, in which failure is detected by inspection only. He provides the analysis of various models and various objective functions, and the analysis of those models while the maintenance costs are changing over time. The preparedness maintenance of a multi-unit system with $n+1$ subsystems subject to imperfect maintenance and opportunistic maintenance is presented in this chapter, following Wang (1997) and Wang et al. (2001). It is assumed that in the system the total maintenance costs and times are less for several subsystems simultaneously than for each subsystem separately as they often do in practice, i.e., economic dependence exists. An opportunistic maintenance policy is incorporated in this model. It is also assumed that PM is imperfect since in practice most maintenance actions tend to make systems not "as good as new" but younger, as discussed in Chapter 1. The system storage 'availability', system maintenance cost rate, and other operating characteristics of this multi-unit system are discussed. The optimum opportunistic preparedness maintenance policies to optimize the system operating performance and to provide the best operational readiness are then investigated.

### 7.1 Introduction

This chapter discusses an optimal preparedness maintenance policy for a system with $n+1$ subsystems considering imperfect maintenance and economic dependency. Assume that the system is placed in storage and is called upon toperform a given task only if a specific but unpredictable emergency occurs. Some maintenance actions may be taken while the system is in storage or long-term cold standby and the objective is to choose the maintenance action sequence providing the best level of preparedness. McCall $(1963,1965)$ applies this preparedness maintenance policy to ballistic missile maintenance and obtains an optimal preparedness maintenance policy. The ballistic missile studied was composed of one uninspected subsystem: the rocket engines, as well as three subsystems which are continuously inspected - the nozzle control units, the guidance and control system, and the re-entry vehicle. Obviously, to keep ballistic missiles at the highest level of operational readiness and thus to prevent them from failure in use they should be subject to frequent inspection and maintenance when in storage.

The main difference between the preparedness maintenance model for missiles, rockets, etc. and the other maintenance models for automobiles, aircraft, etc. lies in the way in which failures are detected. With the automobiles, aircraft, etc., failure occurring while the system is not in operation will be detected whenever an attempt at operation is made. The state of the system is always known with certainty. In fact, continuous operation provides assurance that the state of the system is always known with certainty. However, in a missile system, such a failure will go undetected indefinitely; the state of the system (at least some of its subsystems) is not known with certainty unless some definite maintenance or inspection action is taken. The difference directly affects the design of optimal maintenance policies for each kind of system. Those for automobiles must be designed to overcome the effects of uncertainty about when failures will occur. The policies for missile systems must overcome the same uncertainty, plus another as well: uncertainty about the actual state of the system at any given time - that is, whether it is good or has failed (McCall 1965). If the actual state of the system is known with certainty, either through continuous inspection or continuous operation, the theory of maintenance for the preparedness model becomes the same as for the other maintenance models such as the age replacement policy and block replacement policy. In this sense, the theory of maintenance for the preparedness model is more general than the other maintenance models.

The preparedness model is characterized by three different uncertainties. First, it is impossible to predict the exact time of system failure. Second, the time of emergency use is also not susceptible to exact prediction. Finally, the state of the system is known only at the time of certain maintenance or inspection actions (Radner and Jorgenson 1963).

This chapter considers imperfectness of PM and economic dependence in this multi-unit system, i.e., maintenance costs and times are less for several subsystems simultaneously than for each subsystem taken separately. We suppose that the times to failure of the subsystems in this system are stochastically independent. We also assume that one subsystem in this system has an increasing failure rate while the remaining $n$ subsystems have constant failure rates. The subsystem with an increasing failure rate is a uninspected subsystem and the other $n$ subsystems are inspected ones. The optimal policy for these kinds of systems possesses an opportunistic characteristic. For example, the failure of one subsystem results in a possible opportunity to perform PM on other subsystems.# NOTATION 

$\lambda_{i} \quad$ Failure rate of subsystem $i, \forall i, i=1,2, \ldots, n$
$n \quad$ Number of subsystems with constant failure rates
$T \quad$ Time interval at the end of which a PM is performed on subsystem 0
$t_{i} \quad$ Critical age of subsystem $i, \forall i, i=1,2, \ldots, n$
$C_{0} \quad$ PM cost of subsystem 0 at $j T$
$w_{0} \quad$ PM time of subsystem 0
$C_{i}, w_{i} \quad$ Cost and time to replace subsystem $i, \forall i, i=1,2, \ldots, n$
$C_{0 i}, w_{0 i}$ Cost and time to maintenance subsystem 0 and $i$ together, $\forall i, i=1,2, \ldots, n$
$p \quad$ Probability that PM is perfect
$q \quad$ Probability that PM is minimal, $p+q=1$
$q_{0 i} \quad$ Probability that the renewal cycle ends with a replacement of subsystem $i$ and PM of subsystem 0 together
$d_{i} \quad$ Probability that the renewal cycle ends on the interval $\left\{t_{i}, t_{i+1}\right)$
$L \quad$ Asymptotic system maintenance cost per unit of time
A Asymptotic average system (storage) 'availability'
$D \quad$ Expected duration of a renewal cycle
C Expected system maintenance cost per renewal cycle
$U \quad$ Expected accumulating system failure-free time per renewal cycle
$R \quad$ Expected system maintenance (down) time per renewal cycle
$B \quad$ Random variable: the renewal cycle duration
$S_{i} \quad$ Random variable: time spent on replacing subsystem $i$ alone in one renewal cycle, $\forall i, i=1,2, \ldots, n$
$Y \quad$ Random variable: age of subsystem 0 when perfectly preventively maintained
$Z \quad$ Random variable: time spent on performing perfect repair or perfect PM on subsystem 0 , possibly with other subsystems (at end of renewal cycle)
$V_{i} \quad$ Random duration of the interval over which subsystem $i$ alone would be replaced
$\varphi(x) \quad$ Probability density function of $Y$
$\lambda_{0}(t), f_{0}(t) \quad$ Failure rate and probability density function of the life of subsystem 0
$F_{0}(t), \bar{F}_{0}(t) \quad$ Cumulative failure distribution and survival function of subsystem 0
The distinctive feature of preparedness models is that the state of the system is ascertained only at the time of inspection or maintenance. Next, the subsystem with increasing failure rate $\lambda_{0}(t)$ is denoted by subsystem 0 while the remaining subsystems are labeled by subsystem 1 , subsystem $2, \ldots$, and subsystem $n$. The failure rate function for each remaining subsystem is denoted by $\lambda_{i}(t)$, $\forall i, i=1, \ldots, n$ where

$$
\lambda_{i}(t)=\lambda_{i}, \quad \forall i, i=1, \ldots, n \quad \text { and }
$$$$
\lambda_{0}^{t}(t)>0
$$

Since subsystems $1,2, \ldots, n$ fail exponentially, they are never replaced before failure, that is, no PM will be performed on them.

As stated at the beginning of this chapter, we assume that it spends less cost and time to perform maintenance on subsystem 0 and any other subsystem together than to do maintenance on each subsystem separately, that is,

$$
C_{0}, C_{i}<C_{0 i}<C_{0}+C_{i} \quad \text { and } \quad w_{0}, w_{i}<w_{0 i}<w_{0}+w_{i}
$$

At any point in time the maintenance performer must choose among four alternatives: perform maintenance on the un-inspected subsystem; on an inspected subsystem; on the un-inspected subsystem and an inspected subsystem together; or do nothing (no maintenance). Using a dynamic programming formulation, Radner and Jorgenson (1963) show that the optimum maintenance policy is what they call a $\left(t_{i}, T\right)$ type of policy and proposed an opportunistic maintenance policy. Note that shut-off rule 1 for maintenance by Barlow and Proschan (1975) and Khalil (1985) is realistic:

While a failed subsystem is in repair or maintenance, all other subsystems remain in "suspended animation". After the repair or maintenance is completed, the system is returned to operation. At that instant the subsystems in "suspended animation" are as good as they were when the system stopped operating.

Let $x$ be the age of subsystem 0 since last replacement of subsystem 0 . This chapter investigates such an opportunistic preparedness maintenance policy, based on the preparedness maintenance model developed by Radner and Jorgenson (1963), the shut-off rule by Barlow and Proschan (1975) and Khalil (1985), as well as the method to model imperfect maintenance studied by Brown and Proschan (1983) and Fontenot and Proschan (1984):
(i) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $\left[0, t_{i}\right)$, replace subsystem $i$ alone at a cost of $C_{i}$ and at a time of $w_{i}$ $\forall i, i=1,2, \ldots, n$.
(ii) If subsystem $i$ fails when the age of subsystem 0 is in the time interval $\left[t_{i}, T\right)$, replace subsystem $i$ and do perfect PM on subsystem 0 $\forall i, i=1,2, \ldots, n$. The total maintenance cost is $C_{0 i}$ and total maintenance time is $w_{0 i}$.
(iii) If subsystem 0 survives until its age $x=T$, perform PM on subsystem 0 alone at a cost of $C_{0}$ and at a maintenance time of $w_{0}$ at $x=T$. PM is imperfect.
(iv) If subsystem 0 has not received a perfect PM, perform PM on it alone at time $j T(j=2,3, \ldots)$ until it receives a perfect PM. If subsystem 0 does not receive a perfect maintenance and subsystem $i$ fails after some PM,

Figure 7.1. Opportunistic maintenance policy
replace subsystem $i$ and do perfect PM on subsystem $0, \forall i, i=1,2, \ldots, n$, and the total maintenance cost is still $C_{0 i}$ and total maintenance time is $w_{0 i}$. This process continues until subsystem 0 receives a perfect maintenance.

The optimal maintenance policy for this opportunistic preparedness maintenance model of multi-component systems is characterized by $(n+1)$ decision variables $\left(t_{1}, t_{2}, \ldots, t_{n}, T\right)$, and is obtained by determining the optimal $\left(t_{1}, t_{2}, \ldots, t_{n}, T\right)$ that maximizes the system availability, or minimizes the system maintenance cost rate, or optimizes one when the predetermined requirements for the other are satisfied. It is worth noting that to achieve good operating characteristics of systems, we might take into account system availability because while the system cost rate is minimized the system availability may sometimes not be maximized and is even very low, as shown in Chapter 5.

From Equation (7.1) we can see that for multi-component systems this opportunistic maintenance policy may result in higher system availability as compared with the case that each subsystem is separately maintained. This is because while any subsystem fails and is under maintenance the entire system is down, and it will save time to do PM on unfailed subsystems during this down period and thus reduce the system downtime. Note that shut-off rule 1 is plausible for the series system. The optimal maintenance policy discussed in this chapter can be expected to approximate any type of multi-component systems since maintenance time is short relative to operating time.

In this chapter, we suppose that imperfect PM of subsystem 0 is modeled by the $(p, q)$ rule. Upon each PM there is a perfect inspection requiring negligible time and yielding perfect information as to whether PM is perfect or minimal. Assume further that PM of subsystem 0 together with another subsystem between $j T$ s are assumed to be perfect, $\forall j, j=1,2,3, \ldots$ Next we will first derive the long-run expected system maintenance cost per unit of time, or system maintenance cost rate, the asymptotic average system (storage) 'availability', and then evaluate other system operating performance characteristics and investigate the optimal maintenance polices.# 7.2 System Maintenance Cost Rate and 'Availability' 

Given the above opportunistic preparedness maintenance policy, the times between consecutive perfect maintenance of subsystem 0 constitute a renewal cycle. From the renewal reward theory, the system maintenance cost rate is

$$
L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
$$

Asymptotic average system storage 'availability' is defined as:

$$
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}{U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
$$

where $C\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ is the expected system maintenance cost per renewal cycle, $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ is the expected duration of a renewal cycle, and $U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ and $R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$ are, respectively, the accumulating system storage time and the maintenance time of this system in one renewal cycle. Obviously,

$$
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)+R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)
$$

Next, without loss of the generality, we assume that $t_{1} \leq t_{2} \leq \cdots \leq t_{n}$. Let us first evaluate the expected duration $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$. The renewal cycle duration $B$ is the sum of three random variables. The duration and expected duration are respectively

$$
\begin{gathered}
B=S+Y+Z \\
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=E(B)=E(S)+E(Y)+E(Z)
\end{gathered}
$$

First, we investigate the cumulative distribution function ( $c d f$ ), probability density function ( $p d f$ ) and mean of $Y$. Let $U_{i}$ be the time to failure of subsystem $i$ after $t_{i}$, given subsystem $i$ is good at $t_{i}(i=1,2, \ldots, n)$. Let $H$ denote the time until subsystem 0 alone is subject to a perfect PM. Noting shut-off rule 1 and the memoryless property (Ross 1983) of the exponential distribution, then the age of subsystem 0 is given by

$$
Y=\min \left(t_{1}+U_{1}, \ldots, t_{n}+U_{n}, H\right)
$$

Random variables $U_{i}(i=1,2, \ldots, n)$ are statistically independent and $U_{i}$ has an exponential distribution with failure rate $\lambda_{i}$. Let us denote the $c d f$ of new subsystem 0 by $F_{0}(t)$. Let $\bar{F}_{0}=1-F_{0}$. We assume that $F_{0}$ is absolutely continuous with density $f_{0}(t)$ and that $F_{0}(0)=0$. The failure rate of subsystem 0 is supposed to be increasing. It is easy to show that random variable $H$ has a discrete distribution given by$$
\operatorname{Pr}(H=j T)=q^{j-1} p \quad \forall j, j=1,2, \ldots
$$

and the $c d f$ of $Y$ for $y<T$ is as follows:

$$
\begin{aligned}
& \operatorname{Pr}(Y \leq y)=1-\operatorname{Pr}(Y>y) \\
& \quad=1-\operatorname{Pr}\left(t_{i}+U_{i}>y, \forall i, i=1,2, \ldots, n\right) \\
& \quad=1-\prod_{i=1}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& \quad=1-\exp \left[-\sum_{\substack{i=1 \\
y-t_{i} \geq 0}}^{n} \lambda_{i}\left(y-t_{i}\right)\right]
\end{aligned}
$$

and for $y=T$ we have

$$
\operatorname{Pr}(Y=T)=p \cdot \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(T-t_{i}\right)\right]
$$

The $c d f$ of $Y$ for $T<y<2 T$ is given by

$$
\begin{aligned}
& \operatorname{Pr}(Y \leq y)=1-\operatorname{Pr}(Y>y) \\
& \quad=1-\operatorname{Pr}\left(t_{i}+U_{i} \geq y, i=1,2, \ldots, n ; 1 \text { st PM = imperfect }\right) \\
& \quad=1-q \prod_{i=1}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& \quad=1-q \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(y-t_{i}\right)\right]
\end{aligned}
$$

and for $y=2 T$

$$
\operatorname{Pr}(Y=2 T)=q p \cdot \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(2 T-t_{i}\right)\right]
$$

Generally, for $(j-1) T<Y<j T$ where $j=1,2,3, \ldots$ we have

$$
\begin{aligned}
\operatorname{Pr}(Y \leq y) & =1-\operatorname{Pr}\left(t_{i}+U_{i} \geq y, \forall i, i=1,2, \ldots, n ; 1^{\text {st }} \text { perfect PM is the } j^{\text {th }} \mathrm{PM}\right) \\
& =1-q^{j-1} \prod_{i=1}^{n} \operatorname{Pr}\left(U_{i}>y-t_{i}\right) \\
& =1-q^{j-1} \exp \left[-\sum_{\substack{i=1 \\
y-t_{i} \geq 0}}^{n} \lambda_{i}\left(y-t_{i}\right)\right]
\end{aligned}
$$

and for $y=j T$

$$
\operatorname{Pr}(Y=j T)=q^{j-1} p \cdot \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(j T-t_{i}\right)\right]
$$Next we derive the $p d f$ of $Y$. For $i=1,2, \ldots, n$, let

$$
\left\{\begin{aligned}
M_{i} & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \\
D_{i} & =\exp \left(\sum_{j=1}^{i} \lambda_{j} t_{j}\right) \\
f_{i}(y) & =\left(\sum_{j=1}^{i} \lambda_{j}\right) \exp \left[-\sum_{j=1}^{i} \lambda_{j}\left(y-t_{j}\right)\right] \\
& =D_{i} M_{i} \exp \left(-M_{i} y\right)
\end{aligned}\right.
$$

Then $Y$ has probability density given by, for $y<T$

$$
\varphi(y)=\left\{\begin{array}{ll}
0, & 0 \leq y<t_{1} \\
f_{i}(y), & t_{i} \leq y<t_{i+1} \\
f_{n}(y), & t_{n} \leq y<T
\end{array} \quad \forall i, i=1,2, \ldots, n-1\right.
$$

with probability mass at $Y=T$

$$
\begin{aligned}
G_{0}(T) & =p \cdot \exp \left[-\sum_{j=1}^{n} \lambda_{j}\left(T-t_{j}\right)\right] \\
& =p \cdot D_{n} \exp \left(-M_{n} T\right)
\end{aligned}
$$

For $(j-1) T<Y<j T, \forall j, j=2,3, \ldots, Y$ has probability density as follows:

$$
\varphi(y)=q^{j-1} f_{n}(y)
$$

with probability mass at $Y=j T$

$$
\begin{aligned}
G_{0}(j T) & =\operatorname{Pr}(Y=j T) \\
& =q^{j-1} p \cdot \exp \left[-\sum_{i=1}^{n} \lambda_{i}\left(j T-t_{i}\right)\right] \\
& =q^{j-1} p D_{n} \exp \left[-j T M_{n}\right]
\end{aligned}
$$

It follows that the expected value of $Y$ is given by

$$
\begin{aligned}
E(Y) & =\sum_{i=1}^{n} \int_{t_{i}}^{t_{i+1}} y f_{i}(y) \mathrm{d} y+\sum_{j=1}^{\infty} \int_{j T}^{(j+1) T} q^{j-1} f_{n}(y) d y+\sum_{j=1}^{\infty} j T G_{0}(j T) \\
& =\sum_{i=1}^{n} \int_{t_{i}}^{t_{i+1}} y f_{i}(y) \mathrm{d} y+D_{n} M_{n} \sum_{j=1}^{\infty} q^{j-1} \int_{j T}^{(j+1) T} \exp \left(-M_{n} y\right) d y \\
& +\sum_{j=1}^{\infty} j T q^{j-1} p D_{n} \exp \left[-j T M_{n}\right]
\end{aligned}
$$$$
\begin{aligned}
= & \sum_{i=1}^{n} \int_{t_{i}}^{t_{i-1}} y f_{i}(y) d y+D_{n} \sum_{j=1}^{\infty} q^{j-1}\left\{\exp \left(-j M_{n} T\right)-\exp \left[-\left(j+1\right) M_{n} T\right]\right\} \\
& +D_{n} p T \sum_{j=1}^{\infty} j q^{j-1} \exp \left(-j T M_{n}\right)
\end{aligned}
$$

where $t_{n+1}=T$. For each of the integrals in the first sum we have (Radner and Jorgenson 1963; McCall 1965):

$$
\int_{t_{i}}^{t_{i-1}} y f_{i}(y) d y=D_{i}\left[\left(t_{i}+M_{i}^{-1}\right) \exp \left(-M_{i} t_{i}\right)-\left(t_{i+1}+M_{i}^{-1}\right) \exp \left(-M_{i} t_{i+1}\right)\right]
$$

Second, we derive the expected value of $S$. Recall that $V_{i}$ is the duration of the interval over which subsystem $i$ alone would be replaced if it were to fail, $\forall i, i=1,2, \ldots, n$. Then

$$
\begin{aligned}
V_{i}=\min \left(Y, t_{i}\right) & \forall i, i=1,2, \ldots n \\
E\left(S_{i}\right)=\lambda_{i} E\left(V_{i}\right) w_{i} & \forall i, i=1,2, \ldots n
\end{aligned}
$$

Note that $V_{i}$ has $p d f$ equal to that of $Y$ for $Y<t_{i}$, and probability mass $\operatorname{Pr}\left(Y \geq t_{i}\right)$ concentrated at $t_{i}$. Therefore,

$$
E\left(V_{i}\right)=\sum_{j=1}^{i-1} \int_{t_{j}}^{t_{i-1}} y f_{j}(y) d y+t_{i}\left[1-\sum_{j=1}^{i-1} \int_{t_{j}}^{t_{i-1}} f_{j}(y) d y\right]
$$

Recall that $S=\sum_{i=1}^{n} S_{i}$, then

$$
\begin{aligned}
E(S) & =\sum_{i=1}^{n} E\left(S_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i} E\left(V_{i}\right) \\
& =\sum_{i=1}^{n} \lambda_{i} w_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i+1}} y f_{j}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{i+1}} f_{j}(y) d y\right)\right]
\end{aligned}
$$

Finally, let us derive an expression for $E(Z)$. Denote by $d_{i}$ the probability that the renewal cycle ends on the interval $\left[t_{i}, t_{i+1}\right)$, i.e.,

$$
d_{i}=\operatorname{Pr}\left(t_{i} \leq Y<t_{i+1}\right), \quad \forall i, i=1,2, \ldots, n, \text { and } t_{n+1}=T
$$

Then$$
\left\{\begin{aligned}
d_{1} & =1-\exp \left[-M_{1}\left(t_{2}-t_{1}\right)\right] \\
d_{2} & =\left(1-\alpha_{1}\right)\left\{1-\exp \left[-M_{2}\left(t_{3}-t_{2}\right)\right]\right\} \\
& \quad \vdots \\
d_{i} & =\prod_{j=1}^{i-1}\left(1-\alpha_{j}\right) \alpha_{i} \\
& \quad \vdots \\
d_{n} & =\prod_{j=1}^{n-1}\left(1-\alpha_{j}\right) \alpha_{i} \\
d_{n+1} & =\prod_{j=1}^{n}\left(1-\alpha_{j}\right)=p \cdot D_{n} \exp \left[-M_{n} T\right]
\end{aligned}\right.
$$

where $\alpha_{j}=1-\exp \left[-M_{j}\left(t_{j+1}-t_{j}\right)\right]$ and $d_{n+1}$ is the probability that the renewal cycle ends at $T$.

It is easy to verify that the probability that the renewal cycle ends on the interval $\{(j-1) T, j T\}$ and at $j T, \forall j, j=2,3, \ldots$ respectively, from Equations (7.7a) and $(7.7 b)$ :

$$
\begin{aligned}
d_{1 j} & =\operatorname{Pr}\{(j-1) T<Y<j T\} \\
& =\int_{(j-1) T}^{j T} q^{j-1} f_{n}(y) d y \\
& =q^{j-1} \int_{(j-1) T}^{j T} f_{n}(y) d y \\
d_{2 j} & =\operatorname{Pr}(Y=j T) \\
& =q^{j-1} p D_{n} \exp \left[-j T M_{n}\right]
\end{aligned}
$$

Denote by $q_{0 i}$ the probability that the renewal cycle ends with a replacement of subsystem $i$ and subsystem 0 together. Noting that for two independent exponential random variables $Z_{1}$ and $Z_{2}$ with rate $\eta_{1}$ and $\eta_{2}$ respectively, there exists the following equation (Ross 1993):

$$
\operatorname{Pr}\left(Z_{1}<Z_{2}\right)=\frac{\eta_{1}}{\eta_{1}+\eta_{2}}
$$

Then, we have

$$
\begin{aligned}
q_{0 i} & =\sum_{j=i}^{n} d_{j} \frac{\lambda_{i}}{M_{j}}+\sum_{j=1}^{n} d_{1 j} \frac{\lambda_{i}}{M_{n}} \\
& =\lambda_{i} \sum_{j=i}^{n} \frac{d_{j}}{M_{j}}+\frac{\lambda_{i}}{M_{n}} \sum_{j=1}^{n} d_{1 j} \quad \forall i, i=1,2, \ldots, n
\end{aligned}
$$The probability that the renewal cycle ends with a replacement of subsystem 0 alone is given by

$$
d_{0 p}=d_{n+1}+\sum_{j=2}^{\infty} d_{2 j}=p D_{n} \sum_{j=1}^{\infty} q^{j-1} \exp \left[-j T M_{n}\right]
$$

Therefore, it follows that the third term in Equation (7.4) is given by

$$
E(Z)=\sum_{i=1}^{n} q_{0 i} w_{0 i}+d_{0 p} w_{0}
$$

Recall that

$$
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=E(B)=E(Y)+E(Z)
$$

Thus,

$$
\begin{aligned}
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) & =\sum_{i=1}^{n} \lambda_{i} w_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} y f_{j}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} f_{j}(y) d y\right)\right] \\
& +\sum_{i=1}^{n} \int_{t_{i}}^{t_{i+1}} y f_{i}(y) \mathrm{d} y+D_{n} \sum_{j=1}^{\infty} q^{j-1}\left\{\exp \left(-j M_{n} T\right)-\exp \left[-(j+1) M_{n} T\right]\right\} \\
& +D_{n} T \sum_{j=1}^{\infty} j q^{j-1} \exp \left[-j T M_{n}\right]+\sum_{i=1}^{n} q_{0 i} w_{0 i}+d_{0 p} w_{0}
\end{aligned}
$$

This completes the derivation of the expected duration of a renewal cycle $D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)$.

Wang et al. (2001) investigate the expected system maintenance cost over a single renewal cycle, and here we use their result without proof:

$$
\begin{aligned}
D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) & =\sum_{i=1}^{n} \lambda_{i} C_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} y f_{j}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j+1}} f_{j}(y) d y\right)\right] \\
& +\sum_{i=1}^{n} q_{0 i} C_{0 i}+d_{0 p} C_{0}
\end{aligned}
$$

Substituting the above results into Equations (7.2) and (7.3), and noting that

$$
\begin{aligned}
& E(Y)=U\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right) \text { and } \\
& \mathrm{E}(\mathrm{~S}+\mathrm{Z})=R\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)
\end{aligned}
$$

we obtain the following proposition:
Proposition 7.1 The long-run expected system maintenance cost rate, and the asymptotic average system (storage) 'availability' are respectively:$$
\begin{aligned}
& L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
& \frac{\sum_{i=1}^{n} \lambda_{i} C_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j-1}} y f_{j}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j-1}} f_{j}(y) d y\right)\right]+\sum_{i=1}^{n} q_{0 i} C_{0 i}+d_{0 p} C_{0}}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \\
& A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{E(Y)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
\end{aligned}
$$

From Proposition 7.1, the optimal opportunistic preparedness maintenance policy $\left(T^{*}, t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}\right)$ that minimizes the system maintenance cost rate or maximizes the asymptotic average system storage 'availability' can be obtained by using nonlinear programming software.

Next we discuss the other operating performance characteristics of this opportunistic preparedness maintenance model.

# 7.3 Other Operating Characteristics 

To learn more about this imperfect opportunistic preparedness maintenance and to predict supply and maintenance requirements, let us investigate its other operating characteristics. First, we note that for this imperfect preparedness maintenance model, three different maintenance actions are observed:
(i) Replacement (perfect repair) of a failed subsystem with a constant failure rate by itself.
(ii) Joint opportunistic maintenance of a failed subsystem with a constant failure rate and subsystem 0 unfailed.
(iii) PM of unfailed subsystem 0 at some time $j T$ where $j$ is a natural number.

Besides the system storage availability and maintenance cost rate derived in the last section, other important operating characteristics of this preparedness maintenance policy are the expected number of each of these maintenance actions per unit time, and expected maintenance cost of each of these maintenance actions per unit time. Another characteristic of interest is the probability of at least $m$ failures of one of the subsystems in the interval $(0, t)$ (McCall 1963, 1965; Radner and Jorgenson 1963). Overall, the following operating characteristics will be investigated in this section:
$r_{i} \quad$ Expected rate of replacement of subsystem $i, \forall i, i=1,2, \ldots, n$
$r_{0 i} \quad$ Expected rate of joint opportunistic replacement of failed subsystem $i$ and unfailed subsystem $0, \forall i, i=1,2, \ldots, n$
$r_{00} \quad$ Expected rate of planned maintenance of subsystem 0 at times $j T$
$r_{0 p} \quad$ Expected rate of total perfect maintenance (alone and joint) of subsystem 0$r_{f j} \quad$ Expected rate of joint opportunistic maintenance of subsystem 0 with another subsystem
$c_{00} \quad$ Expected rate of expenditure on PM of subsystem 0 at times $j T$
$c_{i} \quad$ Expected rate of expenditure on replacement of subsystem $i$
$c_{0 i} \quad$ Expected rate of expenditure on joint replacement of subsystem 0 and subsystem $i$
$P_{i}(m, t) \quad$ Probability of at least $m$ failures of subsystem $i$ in the interval $(0, t)$ where $t$ is constant and $\forall i, i=0,1, \ldots, n$

Let us consider the subsystems with constant failure rates first. The time to failure for each of the inspected subsystems is an exponential random variable with rate $\lambda_{i}$. Obviously,

$$
r_{i}=\lambda_{i} \quad \forall i, i=1,2, \ldots, n
$$

or including $w_{i}$, the time to replace subsystem $i$,

$$
r_{i}=\frac{1 / \lambda_{i}}{1 / \lambda_{i}+w_{i}}=\frac{\lambda_{i}}{\lambda_{i} w_{i}+1} \quad \forall i, i=1,2, \ldots, n
$$

Therefore,

$$
c_{i}=r_{i} C_{i}=\frac{\lambda_{i} C_{i}}{\lambda_{i} w_{i}+1} \quad \forall i, i=1,2, \ldots, n
$$

Using the elementary renewal theorem we know that the rate of perfect maintenance of subsystem 0 , is asymptotically equal to the reciprocal of the expected value of $Y$, the time to the first perfect maintenance of subsystem 0 , that is,

$$
\lim _{t \rightarrow \infty} r_{0 p}(t)=[E(Y)]^{-1}
$$

where $E(Y)$ is given in Equation (7.8). Thus, for large value of $t$,

$$
r_{0 p} \approx[E(Y)]^{-1}
$$

On the other hand, from the foregoing definitions for rates of maintenance we have

$$
r_{0 p}=r_{00}^{\prime}+\sum_{i}^{n} r_{0 i}
$$

That is, this expected rate, $r_{0 p}$, can be partitioned into two parts: the expected rate of perfect PM at some time $j T$ and the expected rate of joint opportunistic replacement with another subsystem. We can also see this relationship from the derivation of Equation (7.8). By the Law of Large Numbers, the fraction of the total number of perfect PM of subsystem 0 is equal to $d_{0 p}$ given in Equation(7.11a) for large $t$. Hence, in the long run, the expected rate of perfect PM of subsystem 0 is given by

$$
r_{00}^{t} \approx d_{0 p}[E(Y)]^{-1}
$$

or, including maintenance time,

$$
r_{00}^{t} \approx \frac{d_{0 p}[E(Y)]^{-1}}{d_{0 p}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{d_{0 p}}{d_{0 p}[E(Z)+E(S)]+E(Y)}
$$

It follows that the expected rate of PM of subsystem 0 is

$$
r_{00} \approx r_{00}^{t} / p=\frac{d_{0 p}}{d_{0 p}[E(Z)+E(S)] p+E(Y) p}
$$

The expected expenditure on planned maintenance is given by

$$
c_{00}=r_{00} C_{0}=\frac{d_{0 p} C_{0}}{d_{0 p}[E(Z)+E(S)] p+E(Y) p}
$$

It is easy to see that in the long run, $\sum_{1}^{n} r_{0 i}$, the expected rate of joint opportunistic maintenance of subsystem 0 is

$$
r_{f j}=\sum_{1}^{n} r_{0 i}=\left(1-d_{0 p}\right)[E(Y)]^{-1}
$$

From Section 7.2 ,

$$
1-d_{0 p}=\sum_{1}^{n} q_{0 i}
$$

where $q_{o i} \mathrm{~s}$ are given by Equation (7.11).
Therefore,

$$
r_{f j}=[E(Y)]^{-1} \sum_{1}^{n} q_{0 i}
$$

Since the probability that subsystem 0 will be replaced jointly with subsystem $i$ is $q_{0 i}$, the asymptotic expected rate of opportunistic replacement of subsystem 0 and $i$ is given by

$$
r_{0 i}=q_{0 i}[E(Y)]^{-1} \quad \forall i, i=1,2, \ldots, n
$$

or including maintenance time,

$$
r_{0 i}=\frac{q_{0 i}[E(Y)]^{-1}}{q_{o i}[E(Y)]^{-1}[E(Z)+E(S)]+1}=\frac{q_{0 i}}{q_{o i}[E(Z)+E(S)]+E(Y)} \quad \forall i, i=1,2, \ldots, n
$$

Accordingly, the expected rate of expenditure on opportunistic maintenance is$$
c_{0 i}=r_{0 i} C_{0 i}=\frac{q_{0 i} C_{0 i}}{q_{o i}[E(Z)+E(S)]+E(Y)} \quad \forall i, i=1,2, \ldots, n
$$

Because the lifetime of subsystem $i$ follows the exponential distribution, the probability of at least $m$ replacements of subsystem $i$ in the interval $(0, t)$ is given by

$$
P_{i}(m, t)=\sum_{j=m}^{\infty} \exp \left(-\lambda_{i} t\right) \cdot \frac{\left(\lambda_{i} t\right)^{j}}{j!} \quad \forall i, i=1, \ldots, n
$$

# 7.4 Optimization Models 

So far we have derived the system reliability measures - system storage availability, probability of at least $m$ failures of subsystem $i$ in the interval $(0, t)$, expected rate of failure of subsystem $i$, etc., and system maintenance cost measures - system maintenance cost rate, expected rate of expenditure on planned maintenance of subsystem 0 , expected rate of expenditure on replacement of subsystem $i$, etc. To obtain the optimal system maintenance policies the system reliability measures and system maintenance cost measures must both be acceptable. For example, it may be required that the system maintenance cost rate is minimized while the system availability is not less than some predetermined requirement $A_{0}$. For such a problem, we can formulate the following optimization model from Equations (7.15) and (7.16):

## Maximize

$$
A\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)=\frac{E(Y)}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)}
$$

## Subject to

$$
\left\{\begin{array}{l}
L\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)= \\
\quad \frac{\sum_{i=1}^{n} \lambda_{i} C_{i}\left[\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j-1}} y f_{j}(y) d y+t_{i}\left(1-\sum_{j=0}^{i-1} \int_{t_{j}}^{t_{j-1}} f_{j}(y) d y\right)\right]+\sum_{i=1}^{n} q_{0 i} C_{0 i}+d_{0 p} C_{0}}{D\left(T, t_{1}, t_{2}, \ldots, t_{n} ; p\right)} \leq L_{0} \\
t_{1}, t_{2}, \ldots, t_{n}, T \geq 0
\end{array}\right.
$$

where $L_{0}$ is the pre-determined requirement for system maintenance cost rate.

This model can be solved by nonlinear programming software to obtain an optimal system preparedness maintenance policy $\left(t_{1}^{*}, t_{2}^{*}, \ldots, t_{n}^{*}, T^{*}\right)$. Similarly, basedon other operating characteristics derived we can formulate other optimization models as needed.

# 7.5 Concluding Discussions 

Different from single component systems, one of the key problems for multicomponent systems in modern maintenance practice is economic dependence (Wang et al. 2001). Besides, maintenance is often imperfect. This chapter has considered these two factors which greatly impact on optimal maintenance policies in multi-unit systems and presents some results on this aspect. Moreover, maintenance time is not ignored in this work. Both system reliability and maintenance cost measures are incorporated in the optimal opportunistic maintenance models in this chapter so that the optimal maintenance policies obtained may be optimal not only in terms of maintenance costs but also in terms of reliability measures. Therefore, the opportunistic maintenance model of the multi-component system with $(n+1)$ decision variables $\left(t_{1}, t_{2}, \ldots, t_{n}, T\right)$ introduced in this study is more realistic and the results obtained in this chapter expect to be effective in practice.

If the actual state of the system is known with certainty, either through continuous inspection or continuous operation, the theory of maintenance for the preparedness model becomes the same as for the regular maintenance models. In this sense, the theory of maintenance for the preparedness model is more general than the regular maintenance models.

This chapter has discussed optimal preparedness maintenance policy of multiunit systems with one IFR subsystems given economic dependence and imperfectness of maintenance. It can be extended to multi-unit systems with two or more IFR subsystems which are subject to imperfect maintenance and economic dependence. Another extension is to use other shut-off rules.

Jia and Christer (2002) consider the periodic testing of a preparedness system where, in addition to working and failed state recognition, a working but defective state also exists, and demonstrate their availability models in the context of a missile buffer system. The possible extension is to consider a working but defective state for subsystem 0 .

The imperfect PM is modeled by the $(p, q)$ rule in this chapter. Similarly, one can consider other imperfect maintenance modeling methods discussed in Chapter 2 , for example, the $(p(t), q(t))$ rule.# Optimal Opportunistic Maintenance Policies of $\boldsymbol{k}$-out-of- $\boldsymbol{n}$ Systems 

A $k$-out-of- $n$ :G system is an important system in reliability engineering and could include series and parallel systems as special cases. This chapter introduces opportunistic maintenance of a $k$-out-of- $n$ :G system with imperfect PM and economic dependence, studied by Pham and Wang (2000). Two new $(\tau, T)$ opportunistic maintenance models with consideration of reliability requirements and allowing partial failure are presented. In these two models, only minimal repairs are performed on failed components before a fixed time $\tau$ and CM of all failed components are combined with PM of all functioning but deteriorated components after $\tau$ and number of failed components triggering maintenance can be specified in advance or considered as a decision variable; If the system survives to another fixed time $T$ without perfect maintenance it will be subject to PM at time T. $\tau$ and $T$ are decision variables. System cost rate and availability are investigated for nonegligible maintenance time. The results, including 13 maintenance models as special cases, generalize and unify some previous work in this area.

### 8.1 Introduction

In this chapter, a $k$-out-of- $n$ system is defined to be a complex coherent system with $n$ independent components such that the system operates if and only if at least $k$ of these components function successfully. For a complex and expensive system, it may not be advisable to replace the entire system just because of the failure of one component, especially for a $k$-out-of- $n$ system. In fact, the system comes back into operation on repair or replacement of the failed component by a new one or by a used but operative one. Such maintenance actions do not renew the system completely but enable the system to continue to operate (Kapur et al. 1989). However, the system is usually deteriorating with usage and time. At some point of time or usage it may be in a poor operating condition and a perfect maintenance is necessary. Based on this situation, we formulate the following maintenance policy for a $k$-out-of- $n$ system.The new system starts to operate at time 0 . Each failure of a component of this system during the time interval $(0, \tau)$ is immediately removed by a minimal repair. Components which fail in the time interval $(\tau, T)$ can be left idle. A CM on the failed components together with PM on all unfailed but deteriorating ones is performed at a cost of $c_{f}$ once exactly $m$ components are idle, or PM on the whole system is carried out at a cost of $c_{p}$ once the total operating time reaches $T$, whichever occurs first. That is, if $m$ components fail in the time interval $(\tau, T)$, CM combined with PM is performed; if less than $m$ components fail in the time interval $(\tau, T)$, then PM is carried out at time $T$. After a perfect maintenance, either a CM combined with PM or a PM at $T$, the process repeats.


Figure 8.1. The $(\tau, T)$ opportunistic maintenance policy of $k$-out-of- $n$ systems
This maintenance policy is shown in Figure 8.1. In this policy $\tau$ and $T$ are decision variables. We assume that $m$ is a pre-determined positive integer, $1 \leq m \leq n-k+1$, and $\tau<T$. According to different reliability and cost requirements, $m$ may take different values. Obviously, $m=1$ means that the system is subject to maintenance whenever one component fails after $\tau$. For a series system ( $n$-out-of- $n$ system) or a system with critical applications $m$ may basically be required to be 1 . If $m$ is chosen as $n-k+1$ then $k$-out-of- $n$ system is maintained once the system fails. In most cases, the whole system is subject to a perfect CM together with a PM upon a system failure $(m=n-k+1)$ or partial failure, that is, some components may fail but the system still functions. However, if inspection is not continuous and the system operating condition can be known only through inspection, $m$ can be a number greater than $(n-k+1)$. We assume that if CM together with PM is carried out both are perfect, and that CM combined with PM takes $w_{1}$ time units and PM at time $T$ takes $w_{2}$ time units.

The justification for this policy is that before $\tau$ every component in the system is young and no major repair is necessary and only minimal repairs, which may not take much time and cost, are performed. The component is deteriorating as time passes and after $\tau$ time has elapsed the component may be in a weak operating condition and has a larger failure rate, and consequently a major or perfect repair is needed. Because there is economic dependence and availability requirements (less frequent shut-offs for maintenance), however, we may not replace it immediately but start CM until the number of failed components reaches some pre-specified number $m$. In fact, when the number of failed components reaches $m$, the remaining $(n-m)$ operating components may degrade to a worse operating condi-tion and also need PM. Note that as long as $m$ is less than $(n-k+1)$ the system will not fail and will continue to operate.

As pointed in Chapter 1, economic dependence means that it takes less cost and time to perform maintenance on several components jointly than on each component separately. For a multi-component system, if there is strong economic dependency joint maintenance should be considered. The optimal maintenance policy for this kind of systems possesses an opportunistic characteristic, that is, the optimal maintenance actions for one component depends on the states of the other components (Zheng 1995). Obviously, the maintenance policy proposed above is an opportunistic one.

In this chapter, the following assumptions are made:
i) All failure events are $s$-independent.
ii) Each component has increasing failure rate (IFR).
iii) Minimal repair takes negligible time since minimal repair time is small relatively to perfect maintenance time.
iv) Minimal repair costs are random variables which depend on age and number of minimal repairs.
v) The planning horizon is infinite.
vi) $k$-out-of- $n$ system consists of $n$ i.i.d. components.

We assume that for each component in the system the cost of the $i^{\text {th }}$ minimal repair at age $t$ consists of two parts: the deterministic part $c_{1}(t, i)$ which depends on the age of this component and the number of minimal repairs $i$, and the agedependent random part $c_{2}(t)$. This general cost structure was used by Sheu (1991) in study of an age replacement model.

It is well-known that for a single-unit system PM is justified only if it has IFR. The above assumption that failure rate of each component has IFR is still necessary for the $k$-out-of- $n$ system. This is because the system may be subject to a PM at time $T$. This requires that the system is IFR after $\tau$. The following proposition states the relationship between component and system failure rates:

Proposition 8.1 If a $k$-out-of-n system is composed of independent, identical, IFR components, the system also has IFR.

Proof. Assume that reliability of each component at some time is $p$. The survival function of a $k$-out-of- $n$ system is given by

$$
r(p)=\sum_{i=k}^{n}\binom{n}{i} p^{i}(1-p)^{n-i}
$$

Using binomial theorem it follows that

$$
r(p)=\frac{n!}{(k-1)!(n-k)!} \int_{0}^{p} x^{k-1}(1-x)^{n-k} d x
$$It is easy to prove that

$$
\begin{aligned}
\frac{p r^{\prime}(p)}{r(p)} & =\left[\frac{r(p)}{p r^{\prime}(p)}\right]^{-1} \\
& =\left[\frac{1}{p} \int_{0}^{p}\left(\frac{x}{p}\right)^{k-1}\left(\frac{1-x}{1-p}\right)^{n-k} d x\right]^{-1} \\
& =\left[\int_{0}^{1} y^{k-1}\left(\frac{1-y p}{1-p}\right)^{n-k} d y\right]^{-1}
\end{aligned}
$$

where $y=x / p$.
Since $[(1-y p) /(1-p)]$ is increasing in $p$, it is easy to see that $p r^{\prime}(p) / r(p)$ is decreasing in $p$. Similar arguments are also found in Barlow and Proschan (1975), and Ross (1983). Note that the failure rate of a $k$-out-of- $n$ system is given by

$$
\begin{aligned}
h_{x}(t) & =\frac{-d r[\bar{F}(t), \ldots, \bar{F}(t)]}{d t} / r[\bar{F}(t), \ldots, \bar{F}(t)] \\
& =\frac{-d r[\bar{F}(t), \ldots, \bar{F}(t)]}{d \bar{F}} \frac{d \bar{F}}{d t} \frac{\bar{F}}{\bar{F}} / r[\bar{F}(t), \ldots, \bar{F}(t)] \\
& =q(t) \frac{p r^{\prime}(p)}{r(p)} \int_{p=\bar{F}(t)}
\end{aligned}
$$

where $r(p)=r(p, \ldots, p)$.
It follows from the above equation that $h_{x}(t)$ has IFR noting that $q(t)$ has IFR, $\bar{F}(t)$ is a decreasing function of $t$, and $p r^{\prime}(p) / r(p)$ is decreasing in $p$.

The following notation will be used throughout this chapter:

# Notation 

$c_{f} \quad$ Cost of CM together with PM of a system
$c_{p} \quad$ Cost of PM alone of a system
$g\left(c_{1}(t, i), c_{2}(t)\right)$ Cost of the $i^{\text {th }}$ minimal repair at age $t$, where $g$ is a positive, non-decreasing and continuous function
$c_{1}(t, i) \quad$ Deterministic part of cost of the $i^{\text {th }}$ minimal repair at age $t$, which depends on the age and the number of minimal repairs
$c_{2}(t) \quad$ Random part of cost of the $i^{\text {th }}$ minimal repair at age $t$
$V_{t}(x) \quad$ Cumulative distribution function of $c_{2}(t)$
$v_{t}(x) \quad$ Probability density function of $c_{2}(t)$
$\tau, T \quad$ Two decision variables constituting the $(\tau, T)$ policy,
$f(t) \quad$ Probability density function of a component
$F(t) \quad$ Cumulative density function of a component| $\bar{F}(t)$ | Survival function of a component, $\bar{F}(t)-1-F(t)$ |
| :-- | :-- |
| $\bar{G}(t)$ | Residual survival function of a component |
| $\bar{F}_{n-k+1}(y)$ | Survival function of the time to failure of a $k$-out-of- $n$ system |
| $q(t)$ | Failure rate of a component |
| $Q(t)$ | Cumulative failure rate of a component, $Q(t)=\int_{0}^{t} q(x) d x$ |
| $n$ | Number of components in a system |
| $k$ | Minimum number of operating components to make a system |
|  | function |
| $m$ | Minimum number of failed components needed to start |
|  | maintenance. |
| $w_{1}$ | Time to perform CM together with PM |
| $w_{2}$ | Time to perform PM alone |
| $p$ | Probability that PM is perfect |
| $q$ | $1-p$ in Section 8.3 |
| $N(t)$ | Number of minimal repairs during time interval $(0, t)$ |
| $M(t)$ | Expected number of minimal repairs during time interval $(0, t)$ |
| $L(\tau, T)$ | Long-run expected system maintenance cost per unit time, or cost |
|  | rate |

# 8.2 Perfect PM 

We shall now characterize the classes of possible maintenance actions. Note that at any instant of time, the following alternative maintenance actions for a $k$-out-of- $n$ system are to be performed, per the maintenance policies described in Section 8.1:
i) Keep the present system and no maintenance actions are given.
ii) Performed minimal repair on a component of the system (before time $\tau$ ).
iii) Performed perfect repair on all failed components together with PM on all unfailed but deteriorating components (after time $\tau$ ).
iv) Performed PM on the system at time $T$.

Assume that each component in the $k$-out-of- $n$ system has cumulative distribution function ( $c d f) F(x)$, and probability density function ( $p d f) f(x)$. Then their failure rates (or the hazard rates) are $q(x)=f(x) / \bar{F}(x)$ and cumulative failure rates are $Q(x)=\int_{0}^{x} q(t) d t$ which have a relationship with their survival functions $\bar{F}(x)=\exp \{-Q(x)\}$, where $\bar{F}(x)=1-F(x)$. It is further assumed that the failure rate is differentiable, monotonely increasing, and remains undisturbed by minimal repair.If there is no PM, the residual survival function of each component is given by

$$
\begin{aligned}
\bar{G}(y) & =P\{Y \geq \tau+y \mid Y>\tau\} \\
& =\int_{\tau+y}^{+\infty} f(t) d t / \int_{\tau}^{+\infty} f(t) d t \\
& =\bar{F}(\tau+y) / \bar{F}(\tau) \\
& =e^{-Q(\tau+y)+Q(\tau)}
\end{aligned}
$$

where $y \geq 0$
Let $Y_{1}, Y_{2}, \ldots Y_{n}$ be i.i.d. random variables with survival distribution $\bar{G}(y)$, and $Y_{(1)} \leq Y_{(2)} \leq \cdots \leq Y_{(n)}$ be the corresponding order statistics. Note that the order statistics may be interpreted as successive times of failures of components in the systems, and the $(n-k+1)^{\text {th }}$ order statistic is just the time to failure of the $k$-out-of- $n$ system. The order statistic $Y_{(j)}$ has survival distribution, $\forall j, j=1,2, \ldots, n$,

$$
\begin{aligned}
\bar{F}_{j}(y) & =\sum_{i=0}^{i-1}\binom{n}{i}[G(y)]^{i}[\bar{G}(y)]^{n-i} \\
& =\sum_{i=0}^{i-1}\binom{n}{i}\left[1-e^{-Q(\tau+y)+Q(\tau)}\right]^{i} e^{-(n-i) Q(\tau+y)+(n-i) Q(\tau)}
\end{aligned}
$$

In this section we assume that PM at time $T$ is perfect. According to renewal theory, the times between consecutive perfect maintenance, preventive or corrective, constitute a renewal cycle. From the classical renewal reward theory, the long-run expected system maintenance cost per unit time, or cost rate, is

$$
L(\tau, T)=\frac{C(\tau, T)}{D(\tau, T)}
$$

where $C(\tau, T)$ is the expected system maintenance cost per renewal cycle and $D(\tau, T)$ is the expected duration of a renewal cycle.

Let $Z_{1}, Z_{2}, \ldots$ be i.i.d. random variables with distribution function $F_{m}(y)$, and $Z_{i}^{*}=\min \left(Z_{i}, T\right), \forall i, i=1,2, \ldots$ Then a renewal cycle consists of maintenance time and $Z_{i}^{*}$ duration. It is easy to verify

$$
\begin{aligned}
D(\tau, T) & =E\left[Z_{i}^{*}\right]+I_{\left[Y_{m}<T-\tau\right]} w_{1}+I_{\left[Y_{m} \geq T-\tau\right]} w_{2} \\
& =\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+I_{\left[Y_{m}<T-\tau\right]} w_{1}+I_{\left[Y_{m} \geq T-\tau\right]} w_{2} \\
& =\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}
\end{aligned}
$$

Next we evaluate expected system maintenance cost per renewal cycle $C(\tau, T)$. Note that $C(\tau, T)$ consists of three parts: minimal repair cost, cost of CM combined with PM, and cost of PM at time $T$. For each component thefailures between $(0, \tau)$ occur in accordance with a non-homogeneous Poisson process of rate $q(t)$. The cost of the $i^{\text {th }}$ minimal repair at age $t$ is $g\left(c_{1}(t, i), c_{2}(t)\right)$, where $g$ is a positive, non-decreasing and continuous function of $t$, and is a positive, non-decreasing function of $i$. Suppose that the random part $c_{2}(t)$ at age $t$ has distribution function $V_{i}(x)$, density function $v_{i}(x)$ and finite mean $E\left[c_{2}(t)\right]$. The total minimal repair cost for a $k$-out-of- $n$ system in one cycle is given by

$$
C_{s m r}=n E\left[\sum_{i=1}^{N(\tau)} g\left(c_{1}\left(S_{i}, i\right), c_{2}\left(S_{i}\right)\right)\right]
$$

where $N(\tau)$ is number of minimal repairs during time interval $(0, \tau)$.
The further derivation of this cost expression needs a proposition from Sheu (1991) and we now state it without proof:

Proposition 8.2 Let $\{N(t), t \geq 0\}$ be a non-homogeneous Poisson process with intensity $q(t)$ and $M(t)=E[N(t)]=\int_{0}^{t} q(u) d u$. Denote the successive arrival times of this process by $S_{1}, S_{2}, \ldots$ Assume that at time $S_{i}$ a cost of $g\left(c_{1}\left(S_{i}, i\right), c_{2}\left(S_{i}\right)\right)$ is incurred. Suppose that $c_{2}(y)$ at age $y$ is a random variable with finite mean $E\left[c_{2}(t)\right]$ and $g$ is a positive, non-decreasing and continuous function. If $A(t)$ is the total cost incurred over $[0, t]$, then

$$
E[A(t)]=\int_{0}^{t} \mu(y) q(y) d y
$$

where $\mu(y)=E_{N(y)}\left[E_{C_{2}(y)}\left[g\left(c_{1}(y, N(y)+1), c_{2}(y)\right]\right]\right.$ which is the expectation with respect to random variables $N(y)$ and $c_{2}(y)$.

According to the above proposition the total minimal repair cost in one cycle is given by

$$
C_{s m r}=n \int_{0}^{\tau} \mu(y) q(y) d y
$$

The total cost of PM at time $T$ and CM combined with PM is given by

$$
\begin{aligned}
C_{p f} & =I_{\left[Y_{m}<T-\tau\right]} c_{f}+I_{\left[Y_{m} \geq T-\tau\right]} c_{p} \\
& =F_{m}(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
C(\tau, T) & =C_{s m r}+C_{p f} \\
& =n \int_{0}^{\tau} \mu(y) q(y) d y+F_{m}(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}
\end{aligned}
$$

From Equations (8.3) and (8.5) the following proposition follows:Proposition 8.3 If $P M$ is always perfect, then the long-run expected system maintenance cost per unit time, or cost rate, for a $k$-out-of-n system is given by

$$
L(\tau, T)=\frac{n \int_{0}^{\tau} \mu(y) q(y) d y+F_{m}(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}}
$$

and the limiting average system availability is

$$
A(\tau, T)=\frac{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}}
$$

In what follows, we shall attempt to minimize $L(\tau, T)$ with respect to $\tau$ and $T$. Differentiating $L(\tau, T)$ with respect to $T$ and $\tau$, respectively, we have

$$
\begin{aligned}
& \frac{\partial L(\tau, T)}{\partial T}=-\frac{\bar{F}_{m}(T-\tau)\left[n \int_{0}^{\tau} \mu(y) q(y) d y+\left(c_{f}-c_{p}\right) \cdot F_{m}(T-\tau)+c_{p}\right]}{\left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}\right]^{2}}+ \\
& {\left[\tau\left(c_{f}-c_{p}\right)+c_{f} w_{2}-c_{p} w_{1}+\left(c_{f}-c_{p}\right) \int_{0}^{T-\tau} \bar{F}_{m}(t) d t-n\left(w_{1}-w_{2}\right) \int_{0}^{\tau} \mu(y) q(y) d y\right]} \\
& \left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}\right]^{2} \\
& \times \frac{\partial F_{m}(T-\tau)}{\partial T} \\
& \frac{\partial L(\tau, T)}{\partial \tau}=\frac{\left[n \mu(\tau) q(\tau)+\frac{\partial F_{m}(T-\tau)}{\partial \tau}\left(c_{f}-c_{p}\right)\right]}{\left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}\right]^{2}} \times \\
& {\left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}\right]} \\
& -\frac{\left[n \int_{0}^{\tau} \mu(y) q(y) d y+F_{m}(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}\right]}{\left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}\right]^{2}} \times \\
& {\left[1+\int_{0}^{T-\tau} \frac{\partial F_{m}(t)}{\partial \tau} d t-\bar{F}_{m}(T-\tau)+\frac{\partial F_{m}(T-\tau)}{\partial \tau}\left(w_{1}-w_{2}\right)\right] }
\end{aligned}
$$

A necessary condition that a pair $\left(\tau^{*}, T^{*}\right)$ minimizes $L(\tau, T)$ is that it satisfies$$
\frac{\partial L(\tau, T)}{\partial \tau}=0 \quad \text { and } \quad \frac{\partial L(\tau, T)}{\partial T}=0
$$

The optimal $(\tau, T)$ maintenance policy is obtained by solving the above equations.

# 8.3 Imperfect PM: Case 1 

Section 8.2 assumes that PM is always perfect. In practice, however, this assumption may not be realistic in some cases. This section is different from Section 8.2 in that PM at time $T, 2 T, 3 T, \ldots$ is imperfect and after PM a $k$-out-of- $n$ system is good as new with probability $p$ (perfect PM) and is bad as old with probability $q=1-p$ (minimal PM). Other assumptions and notations are identical to those in Section 8.2.

According to renewal theory of stochastic processes, the times between consecutive perfect maintenance, preventive or corrective, constitute a renewal cycle. From the classical renewal reward theory, the long-run expected system maintenance cost per unit time, or cost rate with parameter $p$, is

$$
L(\tau, T \mid p)=\frac{C(\tau, T \mid p)}{D(\tau, T \mid p)}
$$

where $C(\tau, T \mid p)$ is the expected system maintenance cost per renewal cycle and $D(\tau, T \mid p)$ is the expected duration of a renewal cycle.

Let $Z_{1}, Z_{2}, \ldots$ be i.i.d. random variables with distribution function $F_{m}(y)$, and $Z_{i}^{*}=\min \left(Z_{i}, k T \mid k=\right.$ numberof PMuntilthefirstperfectone), $i=1,2, \ldots$ Note that a renewal cycle is completed either by any CM together with PM or by a perfect PM at time $k T$, and the probability that a PM alone is perfect is $p$. Then a renewal cycle consists of maintenance time and the $Z_{i}^{*}$ duration. It follows from above arguments that

$$
D(\tau, T \mid p)=E\left[Z_{i}^{*}\right]+\text { Expected maintenance time }
$$

Let $T_{p}$ be the first perfect PM-alone time point. Note that events $\left\{T_{p}=T\right\}$, $\left\{T_{p}=2 T\right\},\left\{T_{p}=3 T\right\}, \ldots$ are mutually disjoint events satisfying sample space $\Omega=\bigcup_{j=1}^{\infty}\left\{T_{p}=j T\right\}$. Note also that a renewal cycle is completed either by any CM combined with PM or by a perfect PM at time $k T$. Note also that the probability that a PM alone is perfect is $p$. Pham and Wang (2000) prove

$$
\begin{aligned}
E\left[Z_{i}^{*}\right] & =E\left[Z_{i}^{*} \mid T_{p}=T\right] \cdot I_{\{T\}}\left(T_{p}\right)+E\left[Z_{i}^{*} \mid T_{p}=2 T\right] \cdot I_{\{2 T\}}\left(T_{p}\right)+\cdots \\
& =p\left[\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t\right]+q p\left[\tau+\int_{0}^{2 T-\tau} \bar{F}_{m}(t) d t\right]+q^{2} p\left[\tau+\int_{0}^{3 T-\tau} \bar{F}_{m}(t) d t\right]+\cdots \\
& =\tau+p\left(1+q+q^{2}+\cdots\right) \int_{0}^{T-\tau}+p q\left(1+q+q^{2}+\cdots\right) \int_{T-\tau}^{2 T-\tau}+\cdots
\end{aligned}
$$$$
=\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{i j-1) T-\tau}^{j T-\tau} \bar{F}_{m}(t) d t
$$

Let CM be the event that CM together with PM is performed in a renewal cycle. Pham and Wang (2000) show that the probability that CM combined with PM is

$$
\begin{aligned}
P(\mathrm{CM}) & =P\left(\mathrm{CM} \mid T_{p}=T\right) \cdot I_{\{T\}}\left(T_{p}\right)+P\left(\mathrm{CM} \mid T_{p}=2 T\right) \cdot I_{\{2 T\}}\left(T_{p}\right)+\cdots \\
& =1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)
\end{aligned}
$$

and the probability that PM alone occurs is

$$
P(\mathrm{PM})=\sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)
$$

The above expression at Equation (8.7d) also has direct meaning. For example, term $q \cdot \bar{F}_{m}(2 T-\tau)$ represents the probability that less than $m$ components have failed in the interval $(\tau, 2 T)$ and the first PM turns out to be not perfect (with probability $q$ ). Obviously,

$$
\text { Expected Maintenance Time }=w_{1} \cdot P(\mathrm{CM})+w_{2} \cdot P(\mathrm{PM})
$$

It follows from Equations $(8.7 \mathrm{a}-\mathrm{e})$ that

$$
\begin{aligned}
& D(\tau, T \mid p)=E\left[Z_{t}^{*}\right]+\text { Expected maintenance time } \\
& \quad=\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{i j-1) T-\tau}^{j T-\tau} \bar{F}_{m}(t) d t \\
& \quad+w_{1}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]+w_{2}\left[\sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
\end{aligned}
$$

Next we determine expected system maintenance cost per renewal cycle $C(\tau, T \mid p)$, which consists of three parts: minimal repair cost, PM cost and cost of CM together with PM. The total minimal repair cost in one cycle is the same as the one in Equation (8.4). Again note that a renewal cycle is completed either by any CM together with PM or by a perfect PM, and that the probability that a PM alone is perfect is $p$. Similarly to the derivation of the expected maintenance time, it is easy to show that the total cost of PM alone and CM combined with PM is given by

$$
C_{p f}=c_{p} \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)+c_{f}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
$$

Thus,

$$
\begin{aligned}
& C(\tau, T \mid p)=C_{s m r}+C_{p f} \\
& \quad=n \int_{0}^{\tau} \mu(y) q(y) d y+c_{p} \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)+c_{f}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
\end{aligned}
$$

From Equations (8.7) and (8.8) the following proposition follows:Proposition 8.4 If the $P M$ is perfect with probability $p$ and minimal with probability $q=1-p$, then the long-run expected system maintenance cost per unit time, or cost rate, for a $k$-out-of-n system is given by

$$
\begin{aligned}
& L(\tau, T \mid p)= \\
& \frac{n \int_{0}^{\tau} \mu(y) q(y) d y+c_{p} \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)+c_{f}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{(j-1) T-\tau}^{j T-\tau} \bar{F}_{m}(t) d t+w_{2}\left[\sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]+} \\
& w_{1}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
\end{aligned}
$$

and the limiting average system availability is

$$
\begin{aligned}
& A(\tau, T \mid p)= \\
& \frac{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{(j-1) T-\tau}^{j T-\tau} \bar{F}_{m}(t) d t}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{(j-1) T-\tau}^{j T-\tau} \bar{F}_{m}(t) d t+w_{2}\left[\sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]+} \\
& w_{1}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
\end{aligned}
$$

Obviously, if we set $p=1$ in Equations (8.9) and (8.9a) then we obtain Equations (8.6) and (8.6a). The optimal $(\tau, T)$ maintenance policy with parameter $p$ can be obtained in the same method as in Section 8.2.

# 8.4 Imperfect PM: Case 2 

The model in this section is exactly like the model in Section 8.2 except that after PM with probability $p$ the system is good as new, and with probability $q_{i}$ exactly $i$ components become failed (all other components become good as new) and are subject to perfect CMs immediately where $i=1,2, \ldots, n$ and $\sum_{i=1}^{n} q_{i}=1-p$. Obviously, the latter case may happen in practice (Nakagawa 1987) and consequently a longer maintenance time and a larger maintenance cost are incurred since an additional CM on the failed component(s) due to PM is needed. It should be noted that only the components which have failed due to PM will be repaired immediately. Notice also that more than $m$ components may fail due to PM since PM may cause adjacent damage (Nakagawa 1987) and becomes a worst PM.

Now we discuss modeling of system maintenance cost rate and availability. According to renewal theory, the times between consecutive perfect maintenance, preventive or corrective, constitute a renewal cycle. The long-run expected systemmaintenance cost per unit time, or maintenance cost rate with parameters $p$ and $q_{i}$ for $i=1,2, \ldots, n$, is

$$
L\left(\tau, T \mid p, q_{i}\right)=\frac{C\left(\tau, T \mid p, q_{i}\right)}{D\left(\tau, T \mid p, q_{i}\right)}
$$

where $C\left(\tau, T \mid p, q_{i}\right)$ is the expected system maintenance cost per renewal cycle and $D\left(\tau, T \mid p, q_{i}\right)$ is the expected duration of a renewal cycle.

Let $Z_{1}, Z_{2}, \ldots$ be i.i.d. random variables with distribution function $F_{m}(y)$, and $Z_{i}^{*}=\min \left(Z_{i}, T\right), \forall i, i=1,2, \ldots$ Let $w_{1 i}$ represent their total CM time when exactly $i$ components failed after PM at time $T$. Note that the a renewal cycle is completed either by any CM together with PM, by CM alone right after $T$, or by a perfect PM; and that the probability that a PM alone is perfect is $p$. Thus, a renewal cycle consists of maintenance time and the $Z_{i}^{*}$ duration. It follows from the above arguments that

$$
\begin{aligned}
& D(\tau, T \mid p)=E\left[Z_{i}^{*}\right]+\text { maintenance time } \\
& \quad=\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+w_{1} F_{m}(T-\tau)+\sum_{i=1}^{n} q_{i} \cdot w_{1 i} \cdot \bar{F}_{m}(T-\tau)+w_{2} \bar{F}_{m}(T-\tau)
\end{aligned}
$$

Next we evaluate the expected system maintenance cost per renewal cycle $C\left(\tau, T \mid p, q_{i}\right)$, which consists of four parts: minimal repair cost, cost of PM alone, cost of CM alone right after $T$, and cost of CM together with PM. The total minimal repair cost in one cycle is the same as the one in Equation (8.4). Let $c_{f i}$ represent their total subsequent CM cost when exactly $i$ components have failed due to PM. It is noted that a renewal cycle is completed either by a CM combined with a PM, by a CM alone right after $T$, or by a perfect PM at time $T$, and that the probability that a PM is perfect is $p$. It follows that the total cost of PM and CM after $\tau$ is given by

$$
C_{p f}=c_{p} \bar{F}_{m}(T-\tau)+c_{f} F_{m}(T-\tau)+\sum_{i=1}^{n} c_{f i} \cdot q_{i} \cdot \bar{F}_{m}(T-\tau)
$$

Thus,

$$
\begin{aligned}
& C\left(\tau, T \mid p, q_{i}\right)=C_{s m r}+C_{p f} \\
& =n \int_{0}^{\tau} \mu(y) q(y) d y+c_{p} \bar{F}_{m}(T-\tau)+c_{f} F_{m}(T-\tau)+\sum_{i=1}^{n} c_{f i} \cdot q_{i} \cdot \bar{F}_{m}(T-\tau)
\end{aligned}
$$

We may assume that $c_{f i}$ above has such a cost structure:

$$
c_{f i}=c_{00}+i \cdot c_{s}
$$

where $c_{00}$ represents one-time shut-off cost and $c_{s}$ represents the cost of parts and labor and incremental system-unavailable-for-work cost. However, if $c_{f i}$ has othercost structures, the results in this section are still valid.
From Equations (8.10) and (8.11) the following proposition follows:
Proposition 8.5 If PM is perfect with probability $p$ and causes exactly $i$ components to fail where $\sum_{i=1}^{n} q_{i}-1=p$ and the failed components due to $P M$ are subject to perfect $C M$ immediately, then the long-run expected system maintenance cost rate for the system is given by

$$
\begin{aligned}
& L\left(\tau, T \mid p, q_{i}\right)= \\
& \qquad \begin{array}{l}
n \int_{0}^{\tau} \mu(y) q(y) d y+c_{p} \bar{F}_{m}(T-\tau)+c_{f} F_{m}(T-\tau)+\sum_{i=1}^{n} c_{f i} \cdot q_{i} \cdot \bar{F}_{m}(T-\tau) \\
\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+w_{1} F_{m}(T-\tau)+\sum_{i=1}^{n} q_{i} \cdot w_{1 i} \cdot \bar{F}_{m}(T-\tau)+w_{2} \bar{F}_{m}(T-\tau)
\end{array}
\end{aligned}
$$

and the limiting average system availability is

$$
\begin{aligned}
& A\left(\tau, T \mid p, q_{i}\right)= \\
& \qquad \begin{array}{c}
\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t \\
\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+w_{1} F_{m}(T-\tau)+\sum_{i=1}^{n} q_{i} \cdot w_{1 i} \cdot \bar{F}_{m}(T-\tau)+w_{2} \bar{F}_{m}(T-\tau)
\end{array}
\end{aligned}
$$

Obviously, if we set $p=1$ in Equations (8.12) and (8.12a) then we obtain Equations (8.6) and (8.6a). The optimal $(\tau, T)$ maintenance policy with parameters $p$ and $q_{i}$ can be obtained in the same way as in Section 8.2.

# 8.5 Special Cases 

The three models in Sections 8.2, 8.3 and 8.4 include some previous maintenance models as special cases. A summary is given below. Since Proposition 8.3 is a special case of Propositions 8.4 and 8.5 , the discussions in this section will be focused on Proposition 8.3. The following special cases are in terms of Equation (8.6) except case 10 and case 11 .

Case $1\left(n=k=m=1, w_{1}=w_{2}=0, \tau=0\right)$ : this is the classical age-replacement policy which was called policy I in Barlow and Hunter (1960). If we set parameters $n=k=m=1, w_{1}=w_{2}=0$, and $\tau=0$ in Equation (8.6), then we obtain the wellknown result by Barlow and Hunter (1960):

$$
L(0, T)=\frac{F(T) c_{f}+c_{p} \bar{F}(T)}{\int_{0}^{T} \bar{F}(t) d t}
$$Case $2\left(m=n-k+1, w_{1}=w_{2}=0, \tau=0, \bar{G}(y)=e^{-z y}\right)$ : Nakagawa (1985) investigates this case. If we set parameters $m=n-k+1, w_{1}=w_{2}=0, \tau=0$ and $\bar{G}(y)=e^{-z y}$ in Equation (8.6) then the cost rate becomes

$$
L(0, T)=\frac{c_{p}+\left(c_{f}-c_{p}\right) \sum_{i=0}^{k-1}\binom{n}{i} e^{-i \lambda T}\left[1-e^{-z T}\right]^{n-i}}{\int_{0}^{T} \sum_{i=k}^{n}\binom{n}{i} e^{-i \lambda t}\left[1-e^{-z t}\right]^{n-i} d t}
$$

which agrees with Equation (8) in Nakagawa (1985).
Case $3\left(n=k=m=1, w_{1}=w_{2}=0, \tau=T, g\left(c_{1}(t, i), c_{2}(t)\right)=c\right)$ : this is policy II discussed by Barlow and Hunter (1960), i.e., the classical periodic replacement with minimal repair at failures. If we set parameters $n=k=m=1, w_{1}=w_{2}=0$, $\tau=T$, and $g\left(c_{1}(t, i), c_{2}(t)\right)=c$ in Equation (8.6), the system maintenance cost rate becomes

$$
L(T, T)=\frac{c Q(T)+c_{p}}{T}
$$

which is the same as the well-know result by Barlow and Hunter (1960).
Case $4\left(n=k=m=1, w_{1}=w_{2}=0, \tau=T, g\left(c_{1}(t, i), c_{2}(t)\right)=c, c_{p}=c(T)\right)$ : This is the case treated by Tilquin and Cleroux (1975). If we set $n=k=m=1$, $w_{1}=w_{2}=0, \tau=T, g\left(c_{1}(t, i), c_{2}(t)\right)=c$ and $c_{p}=c_{0}+a(T)$ in Equation (8.6), then the system maintenance cost rate becomes

$$
L(T, T)=\frac{c Q(T)+c_{0}+a(T)}{T}
$$

which is the same as the cost rate in Tilquin and Cleroux (1975).
Case $5\left(n=k=m=1, w_{1}=w_{2}=0, \tau=T, g\left(c_{1}(t, i), c_{2}(t)\right)=c(y)\right)$ : this is the case investigated by Boland (1982).

Case $6\left(n=k=m=1, w_{1}=w_{2}=0, \tau=T, g\left(c_{1}(t, i), c_{2}(t)\right)=c_{i}\right)$ : Boland and Proschan (1982) study this case. In particular, they considered the cost structure $c_{i}=a+i c$ in which minimal repair cost is increasing with the number of minimal repairs.

Case $7\left(n=k=m=1, w_{1}=w_{2}=0, g\left(c_{1}(t, i), c_{2}(t)\right)=c\right)$ : this is the policy considered by Tahara and Nishida (1975). If we set $n=k=m=1, w_{1}=w_{2}=0$, and $g\left(c_{1}(t, i), c_{2}(t)\right)=c$ in Equation (8.6), then the expected systems maintenance costrate is

$$
L(\tau, T)=\frac{c Q(\tau)+G(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}}{\tau+\int_{0}^{T-\tau} \bar{G}(t) d t}
$$

which agree with Equation (23) in Tahara and Nishida (1975).
It is noted that Tahara and Nishida (1975) discuss the optimality of the $(\tau, T)$ policy for a one-unit system by means of dynamic programming techniques and showed that the $(\tau, T)$ maintenance policy is optimal.

Case $8\left(n=k=m=1, w_{1}=w_{2}=0, T=\infty, g\left(c_{1}(t, i), c_{2}(t)\right)=c\right)$ : Muth (1977) studies this case. If we set parameters $n=k=m=1, w_{1}=w_{2}=0, T=\infty$, and $g\left(c_{1}(t, i), c_{2}(t)\right)=c$ in Equation (8.6), we obtain the same result as in Muth (1977)

$$
L(\tau, T)=\frac{c Q(\tau)+c_{f}}{\tau+\int_{0}^{\infty} \bar{G}(t) d t}
$$

Case $9\left(n=k=m=1, w_{1}=w_{2}=0, T=\infty, g\left(c_{1}(t, i), c_{2}(t)\right)=c(t)\right)$ : Yun (1989) considers this case. If we set parameters $n=k=m=1, w_{1}=w_{2}=0, T=\infty$, and $g\left(c_{1}(t, i), c_{2}(t)\right)=c(t)$ in Equation (8.6), we obtain the same result as in Yun (1989):

$$
L(\tau, \infty)=\frac{\int_{0}^{\tau} c(t) q(y) d y+c_{f}}{\tau+\int_{0}^{\infty} e^{-Q(\tau+x)+Q(\tau)} d t}
$$

Case $10\left(n=k=m=1, w_{1}=w_{2}=0, \tau=0\right)$ for Equation (8.9): Nakagawa (1979) deals with this case. If we set $n=k=m=1, w_{1}=w_{2}=0$, and $\tau=0$ in Equation (8.9), then the cost rate becomes

$$
L(0, T \mid p)=\frac{c_{p} \sum_{j=1}^{\infty} q^{j-1} \bar{F}(j T)+c_{f}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}(j T)\right]}{\sum_{j=1}^{\infty} q^{j-1} \int_{(j-1) T}^{j T} \bar{F}(t) d t}
$$

which is the same as Equation (1) in Nakagawa (1979).
Case $11(n=k=m=1, \tau=0)$ for Equation (8.12a): Chan and Downs (1978) study this case. If we set $n=k=m=1, w_{11}=w_{1}, q_{1}=q$ and $\tau=0$ in Equation (8.12a), then the limiting system availability becomes$$
A\left(0, T \mid p, q_{i}\right)=\frac{\int_{0}^{T} \bar{F}(t) d t}{w_{1} F(T)+q w_{1} \bar{F}(T)+\int_{0}^{T} \bar{F}(t) d t+w_{2} \bar{F}(T)}
$$

which is the same as Equation (1) in Chan and Downs (1978).
Case $12(n=k)$ : this case corresponds to optimal $(\tau, T)$ maintenance policy of a series system. If we set $n=k$ and $m=1$ in Equation (8.6), it follows that the longrun expected system maintenance cost rate for a series system with $n$ component is

$$
L(\tau, T)=\frac{n \int_{0}^{\tau} \mu(y) q(y) d y+\left[1-\bar{F}^{n}(T) / \bar{F}^{-n}(\tau)\right]\left(c_{f}-c_{p}\right)+c_{p}}{\tau+[\bar{F}(\tau)]^{-n} \int_{0}^{T-\tau}[\bar{F}(\tau+t)]^{n} d t+\left[1-\bar{F}^{n}(T) / \bar{F}^{-n}(\tau)\right]\left(w_{1}-w_{2}\right)+w_{2}}
$$

Case $13(k=1, n>1)$ : in this case the $k$-out-of- $n$ system is reduced to a parallel system. If we let $k=1$ and $m=n$, it follows that the long-run expected system maintenance cost rate for a parallel system with $n$ components is

$$
\begin{aligned}
& L(\tau, T)= \\
& \frac{n \int_{0}^{\tau} \mu(y) q(y) d y+\left(c_{f}-c_{p}\right)[\bar{F}(\tau)-\bar{F}(T)]^{n} \bar{F}^{-n}(\tau)+c_{p}}{\tau+\int_{0}^{T-\tau}\left\{1-[\bar{F}(\tau)-\bar{F}(\tau+t)]^{n} \bar{F}^{-n}(\tau)\right\} d t+\left(w_{1}-w_{2}\right)[\bar{F}(\tau)-\bar{F}(T)]^{n} \bar{F}^{-n}(\tau)+w_{2}}
\end{aligned}
$$

If we further set $\tau=0$ and $w_{1}=w_{2}=0$, then the above equation becomes

$$
L(0, T)=\frac{\left(c_{f}-c_{p}\right) F^{n}(T)+c_{p}}{\int_{0}^{T}\left[1-F^{n}(t)\right] d t}
$$

which is the same as the result in Yasui et al. (1988).

# 8.6 Optimization Problems 

In Sections 8.2, 8.3 and 8.4 we investigate expected system maintenance cost rate and availability. In some cases, the optimal maintenance policies may be required that while some availability requirements are satisfied the maintenance cost rate is minimized, or while maintenance cost rate is less than some predetermined value the system availability is maximized. For example, for the maintenance model in Section 8.2 the following optimization problem can be formulated in terms of decision variables $T$ and $\tau$ :Maximize $\quad A(\tau, T)=\frac{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}}$
Subject to $\quad L(\tau, T)=\frac{n \int_{0}^{\tau} \mu(y) q(y) d y+F_{m}(T-\tau)\left(c_{f}-c_{p}\right)+c_{p}}{\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+F_{m}(T-\tau)\left(w_{1}-w_{2}\right)+w_{2}} \leq L_{0}$
where constant $L_{0}$ is the predetermined maintenance cost rate requirement.

For maintenance model in Section 8.3 the following optimization problem can be formulated in terms of decision variables $T$ and $\tau$ :

# Minimize 

$$
\begin{aligned}
& L(\tau, T \mid p)= \\
& \begin{array}{c}
n \int_{0}^{\tau} \mu(y) q(y) d y+c_{p} \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)+c_{f}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right] \\
\tau+\int_{0}^{T-\tau} \bar{F}_{m}(t) d t+\sum_{j=2}^{\infty} q^{j-1} \int_{(j-1) T-\tau}^{(T-\tau} \bar{F}_{m}(t) d t+w_{2}\left[\sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]+ \\
w_{1}\left[1-p \sum_{j=1}^{\infty} q^{j-1} \bar{F}_{m}(j T-\tau)\right]
\end{array}
\end{aligned}
$$

Subject to $\quad\left\{\begin{array}{c|c}A(\tau, T & p) \geq A_{0} \\ \tau \geq 0 \\ T>\tau\end{array}\right.$
where constant $A_{0}$ is the predetermined availability requirement.

The optimal maintenance policy $\left(T^{*}, \tau^{*}\right)$ can be determined from it by using nonlinear programming software. Similarly, other optimization models can be formulated.

### 8.7 Numerical Example

Consider a 2-out-of-3 system. Assume that the time to failure of each unit follow a Weibull distribution with shape parameter $\beta$ and scale parameter $\theta$ which has $p d f$ given by

$$
f(y)=\frac{\beta}{\theta}\left(\frac{y}{\theta}\right)^{\beta-1} \exp \left[-\left(\frac{y}{\theta}\right)^{\beta}\right] \quad y>0, \quad \beta, \theta>0
$$and has failure rate

$$
q(y)=\frac{\beta}{\theta}\left(\frac{y}{\theta}\right)^{\theta-1}
$$

Suppose that $\beta=2$ and $\theta=500$ (days) and $g\left(c_{1}(y, i), c_{2}(y)\right)=c_{1}(y)+c_{2}(y)$ in this example. Since $\beta=2>1$ the lifetime of each unit has IFR and by Proposition 8.1 life of this system has IFR. Assume that $c_{1}(y)=1+\sqrt{y}$ and $c_{2}(y)$ follow the normal distribution with mean 1 . Then

$$
\begin{aligned}
\mu(y) & =E_{N(y)}\left[E_{C_{2}(y)}\left[g\left(c_{1}(y, N(y)+1), c_{2}(y)\right)\right]\right. \\
& =E\left[c_{1}(y)+c_{2}(y)\right] \\
& =2+\sqrt{y}
\end{aligned}
$$

Since the aircraft unit system is considered to be critical and very important, $m$ is taken to be 1 . The following parameters are assumed:

$$
\begin{array}{llll}
w_{1}=5 \text { days } & w_{2}=2 \text { days } & c_{f}=59 \\
c_{p}=40 & p=1 & A_{0}=0.99
\end{array}
$$

Let

$$
\begin{aligned}
\zeta & =\tau+500 \times 6^{-\frac{3}{2}} \exp \left[3(0.002 \tau)^{2}\right] \int_{0.002 \tau \sqrt{6}}^{0.002 T \sqrt{6}} \exp \left[-\frac{1}{2} u^{2}\right] d u \\
& -\exp \left[-3(0.002 T)^{2}+3(0.002 \tau)^{2}\right]+5
\end{aligned}
$$

Substituting the above data and parameters into optimization model (8.14) in Section 8.6 results in:

# Minimize 

$$
L=\frac{6\left(\tau^{2}+\frac{2}{5} \tau^{5 / 2}\right) / 500^{2}-19 \cdot \exp \left[-3(0.002 T)^{2}+3(0.002 \tau)^{2}\right]+59}{\zeta}
$$

## Subject to

$$
\left\{\begin{array}{l}
A=\frac{\tau+500 \times 6^{-\frac{1}{2}} \exp \left[3(0.002 \tau)^{2}\right] \int_{0.002 \tau \sqrt{6}}^{0.002 T \sqrt{6}} \exp \left[-\frac{1}{2} u^{2}\right] d u}{\zeta} \geq 0.99 \\
\tau \geq 0 \\
T \geq \tau
\end{array}\right.
$$

Various kinds of approximations for the integral in the above optimization model have been developed and a simple approximation with high accuracy is by Zelen and Severo (1964):$$
\int_{-\infty}^{t} \exp \left(\frac{1}{2} u^{2}\right) d u \approx \sqrt{2 \pi}\left[1-\frac{1}{2}\left(1+.196854 t-.115194 t^{2}+.000344 t^{3}+0.019527 t^{4}\right)^{-4}\right]
$$

The error, for $t \geq 0$, is less than $2.5 \times 10^{-4}$ (see Johnson and Kotz 1970).
By nonlinear optimization software the optimal solution for the above optimization model is found to be

$$
\tau^{*}=320.24 \text { days } \quad T^{*}=410.86 \text { days }
$$

which results in the minimum system maintenance cost rate given by

$$
L\left(\tau^{*}, T^{*}\right)=0.182
$$

That is, the optimal maintenance policy from optimization model (8.13) is that before time $\tau^{*}=320.24$ (days) only minimal repairs are performed; after $\tau^{*}=320.24$ the failed unit will be subject to perfect repair and the two unfailed will undergo PM once any unit fails, or PM at $T^{*}=410.86$ (days), whichever comes first (i.e., CM combined with PM or PM only at $T$, whichever occurs first). Or, we can say that after $\tau^{*}=320.24$ : the failed unit will be subject to perfect repair together with PM on the remaining two once any unit fails; If no unit fails until time $T^{*}=410.86$ (days), PM is carried out at $T^{*}=410.86$.

Other numerical examples can be found in Pham and Wang (2000).

# 8.8 Concluding Discussions 

This chapter deals with the opportunistic maintenance of $k$-out-of- $n$ systems. In many applications, the optimal maintenance actions for one component often depend on the states of the other components and system reliability requirements. Three new $(\tau, T)$ opportunistic maintenance models with consideration of reliability requirements are investigated. In these models only minimal repairs are performed on failed components before time $\tau$ and CM of all failed components are combined with PM of all functioning but deteriorated components after $\tau$. If the system survives to time $T$ without a perfect maintenance it will be subject to PM at time $T$. Considering the maintenance time, system asymptotic cost rate and availability are derived and the results obtained generalize and unify some previous research in this area.

In all three maintenance models PM on non-failed but deteriorated components is also carried out at the moment when CM activities are called for after $\tau$. Such maintenance policies may reduce the number of unexpected CM activities at fairly low costs, since CM together with PM can be performed without substantial additional expenses. Besides, the following points should be noted:

1) Some group replacement policies (see Section 3.3.1) do not consider system reliability structure and reliability requirements. For a $k$-out-of- $n$ system, when oneof its components is down if we repair or replace it there will be a one-time shutoff during which system will not be available. In fact, even if we do not take any action on this component the system may still operate as long as the number of failed components does not exceed $n-k$. However, once the number of failed components surpasses $n-k$ the system fails. Thus, most maintenance actions may start earlier than that moment in practice.
2) Equations (8.6), (8.6a), (8.9), (8.9a), (8.12), and (8.12a) are still valid if CM and PM costs as well as maintenance time of a system are random variables. In this case, $c_{f}, c_{p}, w_{1}$ and $w_{2}$ represent expected costs of CM combined with PM and PM alone, expected maintenance time of CM combined with PM and PM alone, respectively in Equations (8.6), (8.6a), (8.9), (8.9a), (8.12) and (8.12a).
3) $m$ could be a decision variable according to different situations. Its optimal value, together with the optimal values of $\tau$ and $T$, can be found by minimizing the system maintenance cost rate in Equations (8.6), (8.6a), (8.9), (8.9a), (8.12) and (8.12a) in terms of decision variables $\tau, T$ and $m$.
4) $m$ could take a natural number greater than $(n-k+1)$ depending on different reliability and cost requirements.# Reliability and Optimal Inspection-maintenance Models of Multi-degraded Systems 

In practice, the failure rate of a system may depend not only on the time, but also upon the state of the system. The system may not fail fully, but can degrade. Its operating condition can be characterized by a finite number of states: states of degradation. The failure rate transition process from one degradation state to the next degradation state might take faster rate as system reaches the last stages of degradation. Therefore, the state-dependent transition rates for the degradation process should be considered. In some cases if the degradation level exceeds a particular limit the system may not operate successfully and fail. This chapter investigates multi-state degraded systems subject to multiple competing failure processes including two independent degradation processes and random shocks, following Li and Pham (2005a, 2005b). We first discuss system reliability models and then optimal inspection-maintenance. This chapter also presents a methodology to generate the system states when there exists multi-failure processes. The system reliability model can be used not only to determine the reliability of the degraded systems in the context of multi-state functions but also to obtain the states of the systems by calculating the system state probabilities. A generalized condition-based inspection-maintenance model, consisting of the time sequence for inspection and PM threshold levels, is presented. An average long-run maintenance cost rate function is derived based on expressions for degradation paths and cumulative shock damage. A quasi-renewal process introduced in Chapter 4 is employed to develop the inter-inspection sequence. The PM thresholds for degradation processes and inspection sequence are the decision variables of the proposed inspection-maintenance model. The optimum solution to minimize the average long-run maintenance cost rate is discussed. Numerical examples are given to illustrate these system reliability and inspection-maintenance models.

In recent years, increasing research on degraded systems and their reliability as well as inspection and maintenance has been conducted. Pham et al. (1996) present a model for predicting the reliability of a $k$-out-of- $n$ :G system in which components are subject to multi-stage degradation as well as catastrophic failures. Due to the aging effect, the failure rate of the component will increase. Pham et al. (1996)consider the state-dependent transition rates for the degradation process. Because of degradation, the catastrophic state-dependent failure rate may increase as time progress as well based on the Markov approach. Sim and Endrenyi (1993) propose a Markov model for a continuously operating device with deterioration and Poisson failures. In the Markov diagram, the distribution of the inter-arrival between successive degradation stages is assumed to be exponentially distributed with constant rates.

Lam and Yeh (1994b) study state-age-dependent replacement policies for a multi-state system subjected to both deterioration and random shocks. The deteriorating process of the system was modeled based on a semi-Markov process. They assumed that the inter-arrival time between two successive states follows a continuous distribution $F_{t}(t)$ with a finite mean.

Other reliability models considering the degradation and catastrophic failures are developed. Zuo et al. (1999) present a mixture model assuming that the whole population can be divided into two independent sub-populations where one subpopulation is subjected to degradation and the other is subjected to catastrophic failure. Hosseini et al. (2000) develop a condition-based maintenance model for a system subject to deterioration-failures and to Poisson-failures using the Generalized Stochastic Petri Nets. Xue and Yang (1995) model the lifetime distribution of the multi-state deterioration systems based on the continuous-time Markov process and semi-Markov process.

Pham et al. (1997) create models for predicting the availability and mean lifetime of multistage degraded systems with partial repairs. The transition (degradation, partial failure, and repair rates) rates are assumed constant. Klutke and Yang (2002) study the availability of maintained systems subject to both the effects of the degradation and random shocks. They assumed that shocks occur according to a Poisson process and the shock magnitudes are independent and identically distributed random variables. Recently, Pham and Xie (2002) investig ate a generalized surveillance model consisting of dual mutually dependent stochastic processes for surveillance systems. Their model can be used to understand better both the inspection process and the repair unit itself and to provide information that can be used to assist inspectors in scheduling and prioritizing their future inspections.

This chapter first discusses the reliability model and then optimal inspectionmaintenance model of a degraded system subject to multiple competing failure processes including two degradation processes and random shocks. We assume that these three processes are independent and any of them would cause the system to fail based on the threshold value of each process. Applications of such systems can be found in the space shuttle computer complex due to critical mission phases such as boost, reentry and landing and in the electric generator power systems. More applications related to this can be found in Pham (1991). The system can also fail catastrophically whether it is either in a good state or in any of the degraded states due to random shocks. It should be noted that each competing process can be considered as a component in a series system in which system failure occurs when any component fails. In other word, the system fails whichever cause occurs first. This chapter also models the performance of the systems from a perfect condition to degradation stages.The following notation and symbols will be used throughout this chapter:

# Notation 

$Y_{i}(t) \quad$ The $i^{\text {th }}$ degradation process, $\forall i, i=1,2$
$D(t) \quad$ Cumulative random shock damage by the time $t . D(t)=\sum_{i=1}^{N(t)} X_{i}$ where $X_{i} \mathrm{~s}$ are i.i.d. with $p d f f_{X}(x), c d f F_{X}(x)$ and the $k^{\text {th }}$ convolution $F_{X}^{(k)}(x)$
$S \quad$ Critical threshold value for the shock process. The system will fails due to random shocks when $D(t)>S$
$G_{i} \quad$ Critical value for degradation process $i$ for $i=1,2$ where the system will fail due to degradation when $Y_{i}(t)>G_{i}$
$\Omega_{U} \quad\{M, \ldots, 1,0, F\}$ a system state space
$M \quad$ Perfect (good) state
0 Degraded failure state
$M-1, \ldots, 1 \quad$ Intermediate degradation states
$F \quad$ Catastrophic failure state
$\Omega \quad\{M, \ldots, 1,0\}$ a system degradation state space without catastrophic failure
$\Omega_{i} \quad\left\{M_{i}, \ldots, 1_{i}, 0_{i}\right\}$ a state space corresponding to degradation process $i$
$0_{i} \quad$ Degraded failure state due to the $i^{\text {th }}$ degradation process
$M_{i} \quad$ Good state of degradation process $i, \forall i, i=1,2$
$R \quad \Omega_{1} \times \Omega_{2}$ Cartesian product of $\Omega_{1}$ and $\Omega_{2}$
$R_{i} \quad$ The $i^{\text {th }}$ equivalence class, $i=0,1 \ldots, M$
$R(t) \quad$ Reliability function
r.v. $\quad$ Random variable

C $C_{c} \quad$ Cost per CM action
$C_{p} \quad$ Cost per PM action
$C_{m} \quad$ Loss per unit idle time
$C_{i} \quad$ Cost per inspection
$L_{1} \quad$ PM critical threshold value for degradation process 1
$L_{2} \quad$ PM critical threshold value for degradation process 2
$C(t) \quad$ Cumulative maintenance cost up to time $t$
$E\left[C_{1}\right] \quad$ Average total maintenance cost during a cycle
$E\left[W_{1}\right] \quad$ Mean cycle length
$E\left[N_{I}\right] \quad$ Mean number of inspections during a cycle
$E[\xi] \quad$ Mean idle time during a cycle
$\left\{I_{i}\right\}_{i \in N} \quad$ Inspection sequence
$\left\{U_{i}\right\}_{i \in N} \quad$ Inter-inspection sequence
$\left\{W_{i}\right\}_{i \in N} \quad$ Renewal times
$T \quad$ Time to failure| $P_{i+1}$ | Probability that there are a total of $(i+1)$ inspections in a renewal <br> cycle |
| :-- | :-- |
| $P_{p}$ | Probability that a renewal cycle ends by a PM action |
| $P_{c}$ | Probability that a renewal cycle ends by a CM action |
| $E C\left(L_{1}, L_{2}, I_{1}\right)$ | Expected long-run cost rate function |

# 9.1 Reliability Modeling 

In this section, we discuss models for evaluating the reliability of multi-state degraded systems subject to multiple competing failure processes. Two of them are the continuous and increasing degradation processes (processes 1 and 2 ) and the third one is random shocks. The performance of the systems can vary from a perfect condition as good as new to degradation stages as time passes since the multi-state reliability model in this section, from the multi-state perspective, can be capable of handling a wide range of performance ( Li and Pham 2005b). The remaining of this section is organized as follows. Section 9.1.1 describes the multistate system description, modeling assumptions and methodologies. It also presents a method to determine the system state and to view degradation process in terms of multi-state. In Section 9.1.2, we present a model for evaluating the reliability of multi-state degraded systems with random shocks. Section 9.1.3 delivers numerical examples to illustrate the obtained results.

### 9.1.1 System Description and Modeling Methodologies

Assume a system is subject to a variety of three independent competing failure processes in which two of them are degradation processes: degradation process 1 measured by the function $Y_{1}(t)$ and degradation process 2 measured by $Y_{2}(t)$ ), and the third is a random shock process $D(t)$; whichever occurred first would cause the system to fail.

Initially, the system is considered to be in a good state (i.e., $M_{1}$ and $M_{2}$ ). As time passes, it can either go to the first degraded state (i.e., $(M-1)_{1}$ or $\left.(M-1)_{2}\right)$ upon degradation or can go to a catastrophic failed state (state $F$ ) subject to random shocks. When a system reaches the first degraded state, it can either stay in that state until the mission time, or it can go to the second degradation state (i.e., $(M-2)_{1}$ or $\left.(M-2)_{2}\right)$ upon degradation, or can go to a failed state ( $F$ state) upon random shocks.

The same process will be continued for all stages of degradation except the last degradation state (i.e., either stage $0_{1}$ or stage $0_{2}$ ). If the system reaches the last degradation state, it cannot perform its functions satisfactorily (it considers to reach an unacceptable limit) and be treated as a failure (state 0 ). Figure 9.1 shows the system state transition diagram of the multiple competing transition processes. In Figure 9.1, the top portion represents degradation process 1 ; the bottom represents degradation process $2 ; F$ represents a catastrophic failure state due to random shocks.

Figure 9.1. Flow diagram of the system subjected to multiple failure processes

In this section, we have the following assumptions:
i) The system consists of $(M+2)$ states where state 0 and state $F$ are both complete failure states, state $i$ is a degradation state, and $1<i<M$.
ii) No repair or maintenance is performed on the system.
iii) $Y_{i}(t), i=1,2$ is a non-negative non-decreasing function at time $t$, since degradation is an irreversible accumulation of damage.
iv) $Y_{i}(t), i=1,2$ and $D(t)$ are statistically independent. The independence assumption implies that the state of one process will have no effect on the state of the others.
v) At time $t=0$, the system is at state $M$.
vi) The system can fail either due to each degradation process when $Y_{i}(t)>G_{i}, i=1,2$ or due to random shocks (it goes to a catastrophic failure state $F$ ) when $D(t)=\left(\sum_{i=1}^{N(t)} X_{i}\right)>S$
vii) The critical threshold value $G_{i}$ depends upon the function of states of the degraded systems.

In this section, degradation paths are modeled by some continuous probabilistic functions. Note that the operating condition of the system is characterized by a finite number of states: system state space $\Omega_{U}$. Therefore, we need to discretize continuous processes. In Step 1 below, we discuss a procedure how to discretize the two degradation processes in order to obtain $\Omega_{1}$ and $\Omega_{2}$ which correspond to degradation process 1 and 2, respectively. After obtaining the degradation process space $\Omega_{1}$ and $\Omega_{2}$, Step 2 presents a methodology how to establish a relationship between the system state space $\Omega_{U}$, and the degradation and random shock state spaces $\left\{\Omega_{1}, \Omega_{2}, F\right\}$.# Step 1: Characterizing Degradation Processes into Discrete State Sets 

The two degradation processes cases are considered here. A general situation is to allow each degradation process to be discretized into a number of different states. The state space denoted by $\Omega_{1}=\left\{M_{1}, \ldots, 1_{1}, 0_{1}\right\}$ corresponds to degradation process 1 with $\left(M_{1}+1\right)$ states. Similarly, the state space denoted by $\Omega_{2}=\left\{M_{2}, \ldots, 1_{2}, 0_{2}\right\}$ associates with degradation process 2 having $\left(M_{2}+1\right)$ states. $M_{1}$ and $M_{2}$ may or may not be the same and, $M_{i}<\infty, i=1,2$.

We view the degradation process from the perspective of a finite number of states. For example, when the value $Y_{1}(t)$ of degradation process 1 falls into a predefined interval, then its corresponding state will be determined. Let us define as follows: $\left[0, W_{M}\right], \ldots,\left(W_{2}, W_{1}\right]$ are the intervals on the degradation 1 curve (see Figure 9.2a) corresponding to state $M_{1}, 0_{1}$, where $W_{M}<W_{M-1}<\cdots<W_{1}$ and $\left[0, A_{M}\right], \ldots,\left(A_{2}, A_{1}\right]$ are intervals associated with degradation process 2 curve (see Figure 9.2b) corresponding to state $M_{2}, 0_{2}$, where $A_{M}<A_{M-1}<\ldots<A_{1}$.


Figure 9.2. Degradation process function in terms of multi-state
Mathematically, the relationship between the degradation process states $\Omega_{1}=\left\{M_{1}, \ldots, 1_{1}, 0_{1}\right\}, \Omega_{2}=\left\{M_{2}, \ldots, 1_{2}, 0_{2}\right\}$ and their corresponding degradation intervals are given as follows:

Degradation Process 1
$0<Y_{1}(t) \leq W_{M} \quad \Rightarrow$ state $M_{1}$
$W_{M}<Y_{1}(t) \leq W_{M-1} \Rightarrow$ state $(M-1)_{1} \quad A_{M}<Y_{2}(t) \leq A_{M-1} \Rightarrow$ state $(M-1)_{2}$
$W_{2}<Y_{1}(t) \leq W_{1} \Rightarrow$ state $1_{1}$
$G_{1}=W_{1}<Y_{1}(t) \Rightarrow$ state $0_{1}$

Degradation Process 2
$0<Y_{2}(t) \leq A_{M} \Rightarrow$ state $M_{2}$
$A_{M}<Y_{2}(t) \leq A_{M-1} \Rightarrow$ state $(M-1)_{2}$
: $\quad:$
$A_{2}<Y_{2}(t) \leq A_{1} \Rightarrow$ state $1_{2}$
$G_{2}=A_{1}<Y_{2}(t) \Rightarrow$ state $0_{2}$# Step 2: Constructing System State Space based on Degradation States 

The system state space is defined as $\Omega_{U}=\{M, \ldots, 1,0, F\}$, consisting of $M+2$ states. This step will create a method to develop a function to generate a relationship between the system state space $\Omega_{U}$ and degradation state spaces $\left\{\Omega_{1}, \Omega_{2}, F\right\}$. For example, at a given time $t$, suppose that degradation process 1 is at state $i_{1} \in \Omega_{1}$, and degradation process 2 is at state $j_{2} \in \Omega_{2}$, what is the system state?

Assume that at the current time the system is not in a catastrophic failure state. So state $F$ can be ignored for the time being. So, we can simply look at ways to define a function that represents relationship between $\Omega_{U}$ and $\left\{\Omega_{1}, \Omega_{2}\right\}$ instead of $\Omega_{U}$ and $\left\{\Omega_{1}, \Omega_{2}, F\right\}$. The operation can be described by a mapping function $f: R=\Omega_{1} \times \Omega_{2} \rightarrow \Omega=\{M, . ., 1,0\}$ where $R=\Omega_{1} \times \Omega_{2}=\left\{\left(i_{1}, j_{2}\right) \mid i_{1} \in \Omega_{1}, j_{2} \in \Omega_{2}\right\}$ is a Cartesian product as the input space domain and shown in Figure 9.3.


Figure 9.3. A mapping function
The matrix $H_{c}$ given below is an output space consisting of $M+1$ elements corresponding each input space domain through the function $f$ :

$$
\begin{aligned}
& H_{c}=\begin{array}{ccccc}
0_{1} & 1_{1} & \cdots & M_{1} \\
0_{2} & \times & 0 & \cdots & 0 \\
1_{2} & 0 & \ddots & & \vdots \\
\vdots & \vdots & & \ddots & \vdots \\
M_{2} & 0 & \cdots & \cdots & M
\end{array}
$$

The top row of $H_{c}$ represents the state from degradation process 1 . The very left column represents the state from degradation process 2 . The elements of $H_{c}$ represent $f\left(i_{1}, j_{2}\right)=k$ where $i_{1} \in \Omega_{1}, j_{2} \in \Omega_{2}$ and $k \in \Omega$. Note that in matrix $H_{c}$, all the elements in the first row and first column are zeros except the one denoted by $\times$ (will explain this later) since the system will go to a degraded failure state (state 0 ) when either of degradations reaches state $0_{i}, i=1,2$. Besides, some elements in matrix $H_{c}$ are also zeros since we define when degradation 1 is in some low state $l_{1}\left(\left(0_{1}<l_{1}<M_{1}\right)\right.$ and degradation 2 is also in some low state $l_{2}$ $\left(0_{2}<l_{2}<M_{2}\right)$. Hence, we consider it as degradation failure. It is also observed that $f\left(M_{1}, M_{2}\right)=M$, since initially the system is in a brand new state (state $M$ ).

As mentioned above, the first element in $H_{c}$ is marked by $\times$ which means that it does not exist. The reason is as follows. Note that we define the time-to-failure as$$
T=\inf \left\{t: Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2} \text { or } D(t)>S\right\}
$$

It should be noted that all the three processes are competing with each other for the life of a system. However, there is only one of the three processes, whichever occur first, that when exceeding its corresponding critical threshold value, will cause the system to fail. Hence, the following events will not happen:

$$
\begin{aligned}
& P\left\{Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2}, D(t)>S\right\}=0 \\
& P\left\{Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2}, D(t)>S\right\}=0 \\
& P\left\{Y_{1}(t)>G_{1}, Y_{2}(t)<G_{2}, D(t)>S\right\}=0 \\
& P\left\{Y_{1}(t)<G_{1}, Y_{2}(t)>G_{2}, D(t)>S\right\}=0
\end{aligned}
$$

Since $f\left(0_{1}, 0_{2}\right)=P\left\{Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2}, D(t) \leq S\right\}$, the combination of $f\left(0_{1}, 0_{2}\right)$ does not exist. The function $f: R=\Omega_{1} \times \Omega_{2} \rightarrow \Omega=\{M, . ., 1,0\}$ is defined to satisfy following conditions:
i) $f\left(0_{1}, b\right)=f\left(a, 0_{2}\right)=0$ where $b \in \Omega_{2}, a \in \Omega_{1}, f\left(M_{1}, M_{2}\right)=M$
ii) $f$ is a monotonic non-decreasing in each variable. For instance,

$$
f\left(a_{1}, b_{2}\right) \geq f\left(l_{1}, b_{2}\right) \text { if } a_{1} \geq l_{1} \quad \text { and } f\left(a_{1}, b_{2}\right) \geq f\left(a_{1}, l_{2}\right) \text { if } b_{2} \geq l_{2}
$$

Figure 9.4 demonstrates the system state generating box. There are two inputs $i_{1}$ and $j_{2}$ and an output $k$. The inside mapping mechanism is performed by the function $f$. At time $t$, suppose that degradation 1 is at state $i_{1}$ and degradation 2 is at state $j_{2} ; i_{1}$ and $j_{2}$ are as inputs; via matrix $H_{c}$, system state $k$ is then generated as output.


Figure 9.4. A representation of system state generating box
It is observed that in matrix $H_{c}$ different state combination inputs can generate the same results of the system state. To explain this, we need the following definition on the equivalence class:

DEFINITION The $i^{\text {th }}$ equivalence class $R_{i}$ is defined as follows:

$$
R_{i}=\left\{\left(k_{1}, j_{2}\right) \text { where } k_{1} \in \Omega_{1}, j_{2} \in \Omega_{2} \mid f\left(k_{1}, j_{2}\right)=i\right\}, \mathrm{i}=0,1, \ldots, \mathrm{M}
$$

$R_{i}$ represents all possible state combinations which generate the system state $i$. $R_{0}, \ldots, R_{M}$ are disjointed sets which partition $R$ into $M+1$ equivalence classes, so that$$
R=\bigcup_{i=0}^{M} R_{i}
$$

Next we give an example to illustrate the concepts. Assume the state spaces for degradation process 1 and degradation process 2 are: $\Omega_{1}=\left\{4_{1}, 3_{1}, 2_{1}, 0_{1}\right\}$ and $\Omega_{2}=\left\{3_{2}, 2_{2}, 1_{2}, 0_{2}\right\}$ respectively. The system state space is: $\Omega_{U}=\{3,2,1,0, F\}$. The matrix $H_{c}$ is defined as follows:

$$
H_{c}=\begin{gathered}
0_{1} 1_{1} 2_{1} 3_{1} 4_{1} \\
0_{2}\left[\begin{array}{lllll}
\times & 0 & 0 & 0 & 0 \\
1_{2} & 0 & 0 & 1 & 2 & 2 \\
2_{2} & 0 & 1 & 2 & 2 & 2 \\
3_{2} & 0 & 2 & 2 & 2 & 3
\end{array}\right]
\end{gathered}
$$

$R$ is numerated as follows:

$$
\begin{aligned}
R= & \left\{\left(0_{1}, 1_{2}\right),\left(0_{1}, 2_{2}\right),\left(0_{1}, 3_{2}\right),\left(1_{1}, 0_{2}\right),\left(2_{1}, 0_{2}\right),\left(3_{1}, 0_{2}\right),\left(4_{1}, 0_{2}\right),\left(1_{1}, 1_{2}\right),\left(1_{1}, 2_{2}\right)\right. \\
& \left.\left(2_{1}, 1_{2}\right),\left(3_{1}, 1_{2}\right),\left(4_{1}, 1_{2}\right),\left(2_{1}, 2_{2}\right),\left(3_{1}, 2_{2}\right),\left(4_{1}, 2_{2}\right),\left(1_{1}, 3_{2}\right),\left(2_{1}, 3_{2}\right),\left(3_{1}, 3_{2}\right),\left(4_{1}, 3_{2}\right)\right\}
\end{aligned}
$$

According to the $H_{c}$, the equivalence classes can be obtained as follows:

$$
\begin{aligned}
& R_{0}=\left\{\left(0_{1}, 1_{2}\right),\left(0_{1}, 2_{2}\right),\left(0_{1}, 3_{2}\right),\left(1_{1}, 0_{2}\right),\left(2_{1}, 0_{2}\right),\left(3_{1}, 0_{2}\right),\left(4_{1}, 0_{2}\right),\left(1_{1}, 1_{2}\right)\right\} \\
& R_{1}=\left\{\left(1_{1}, 2_{2}\right),\left(2_{1}, 1_{2}\right)\right\} \\
& R_{2}=\left\{\left(3_{1}, 1_{2}\right),\left(4_{1}, 1_{2}\right),\left(2_{1}, 2_{2}\right),\left(3_{1}, 2_{2}\right),\left(4_{1}, 2_{2}\right),\left(1_{1}, 3_{2}\right),\left(2_{1}, 3_{2}\right),\left(3_{1}, 3_{2}\right)\right\} \\
& R_{3}=\left\{\left(4_{1}, 3_{2}\right)\right\} \\
& \text { and } R=\bigcup_{i=0}^{3} R_{i}
\end{aligned}
$$

# 9.1.2 Reliability Modeling 

Now we are ready to derive the $p d f$ and the system mean time to failure based on the state probabilities given in Section 9.1.1. First we derive the probability in each state. Initially, the system is in a brand-new state, i.e., in state $M=f\left(R_{M}\right)$. The probability for state $M$ is given by

$$
P_{i}(M)=P_{i}\left(f\left(R_{M}\right)\right)
$$

As defined in Section 9.1.1, $R_{i}$ represents all possible state combinations generating the system state $i$. The probability in state $i$ is the union of all the elements in $R_{i}$ :

$$
P_{i}(i)=P\left\{f\left(R_{i}\right)\right\}
$$

The probability for a catastrophic failure state $F$ is given by$$
P_{t}(F)=P\left\{Y_{1}(t) \leq G_{1}, Y_{2}(t) \leq G_{2}, D(t)>S\right\}
$$

The reliability $R(t)$ can be calculated as follows:

$$
\begin{aligned}
R(t) & =P\{\text { system state } \geq 1\} \\
& =\sum_{i=1}^{M} P_{i}(i)
\end{aligned}
$$

where $P_{i}(t)$ is the probability in state $i$.
The mean time to failure is expressed as

$$
E[T]=\int_{0}^{\infty} P\{T>t\} d t
$$

Li and Pham (2005a) prove that

$$
E[T]=\sum_{j=0}^{\infty} \frac{F_{X}^{(j)}(S)}{j!} \int_{0}^{\infty} P\left\{Y_{1}(t) \leq G_{1}\right\} P\left\{Y_{2}(t) \leq G_{2}\right\}\left(\lambda_{2} t\right)^{j} e^{-\lambda_{2} t} d t
$$

Equation (9.8) shows that the mean time to failure $E(T)$ would depend on the expression of $P\left\{Y_{1}(t) \leq G_{1}\right\} P\left\{Y_{2}(t) \leq G_{2}\right\}$. The $p d f$ of time to failure, $f_{T}(t)$ is, therefore, as follows:

$$
\begin{aligned}
f_{T}(t) & =-\frac{d}{d t}[P\{T>t\}] \\
& =-\frac{d}{d t}\left[P\left\{Y_{1}\left(t \leq G_{1}\right\} P\left\{Y_{2}(t) \leq G_{2}\right\} \sum_{j=0}^{\infty} \frac{\left(\lambda_{2} t\right)^{j} e^{-\lambda_{2} t}}{j!} F_{X}^{(j)}(S)\right]
\end{aligned}
$$

# 9.1.3 Numerical Examples 

Consider a system subjected to two degradation processes and random shocks. Assume that degradation process 1 is described as the function $Y_{1}(t)=A+B g(t)$ where the random variables $A$ and $B$ are independent and both follow the normal distributions with mean 90 and variance 2.5 , and mean 78 and variance 6 , respectively, i.e., $A \sim N(90,2.5), B \sim N(78,6)$. The degradation function is assumed as $g(t)=t^{3}$. Suppose that critical threshold values: $G_{1}=2500$ and $W_{3}=1500, W_{2}=2000, W_{1}=2500$.

Assume that degradation process 2 is described by $Y_{2}(t)=W \cdot e^{B B t} /\left(A A+e^{B B t}\right)$ where the random variables $A A$ and $B B$ are independent and follow the uniform distribution with interval $[0,100]$ and exponential distribution with parameter 0.1 respectively: $A A \sim U[0,100], B B \sim \operatorname{Exp}(0.01)$. Assume critical values $G_{2}=5000$, $A_{2}=2600, A_{1}=5000$, and $W=7000$.

Suppose that the random shock is represented by $D(t)=\sum_{i=0}^{N(t)} X_{i}$ with critical value $S=200$, where $X_{i} \sim \operatorname{Exp}(0.1)$ and $X_{i}$ s are i.i.d.Assume that the states associated with degradation process 1 and degradation 2 are, respectively, $\Omega_{1}=\left\{3_{1}, 2_{1}, 1_{1}, 0_{1}\right\}$ and $\Omega_{2}=\left\{2_{2}, 1_{2}, 0_{2}\right\}$. We define the system state space as $\Omega_{U}=\{3,2,1,0, F\}$ and the matrix $H_{c}$ is given as follows:

$$
\begin{gathered}
0_{1} \quad 1_{1} \quad 2_{1} \quad 3_{1} \\
0_{2}\left[\begin{array}{llll}
\times & 0 & 0 & 0
\end{array}\right] \\
H_{c}=1_{2}\left[\begin{array}{llll}
0 & 0 & 2 & 3
\end{array}\right. \\
2_{2}\left[\begin{array}{llll}
0 & 1 & 2 & 3
\end{array}\right]
\end{gathered}
$$

Then we obtain

$$
\begin{aligned}
R= & \left\{\left(0_{1}, 1_{2}\right),\left(0_{1}, 2_{2}\right),\left(1_{1}, 0_{2}\right),\left(2_{1}, 0_{2}\right),\left(3_{1}, 0_{2}\right),\left(1_{1}, 1_{2}\right),\left(2_{1}, 1_{2}\right),\left(3_{1}, 1_{2}\right)\right. \\
& \left.\left(1_{1}, 2_{2}\right),\left(2_{1}, 2_{2}\right),\left(3_{1}, 2_{2}\right)\right\}
\end{aligned}
$$

The equivalence classes can be listed as follows:

$$
\begin{aligned}
& R_{0}=\left\{\left(0_{1}, 1_{2}\right),\left(0_{1}, 2_{2}\right),\left(1_{1}, 0_{2}\right),\left(2_{1}, 0_{2}\right),\left(3_{1}, 0_{2}\right),\left(1_{1}, 1_{2}\right)\right\} \\
& R_{1}=\left\{\left(1_{1}, 2_{2}\right)\right\} \\
& R_{2}=\left\{\left(2_{1}, 1_{2}\right),\left(2_{1}, 2_{2}\right)\right\} \\
& R_{3}=\left\{\left(3_{1}, 1_{2}\right),\left(3_{1}, 2_{2}\right)\right\} \\
& R=\sum_{i=0}^{3} R_{i}
\end{aligned}
$$

According to the above $H_{c}$, the probability of the system in state 3 is the sum of the probability $f\left(3_{1}, 2_{2}\right)$ and of probability $f\left(3_{1}, 1_{2}\right)$ and is calculated as follow:

$$
\begin{aligned}
P_{t}(3)= & P_{t}\left(f\left(R_{3}\right)\right) \\
= & \Phi\left(\frac{1500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)\left\{1-\frac{1}{100}(0.4)^{\frac{0.01}{t}}\left(\frac{t}{t-0.01}\right)\left(0.01^{t-\frac{0.01}{t}}\right)\right\} \bullet \\
& e^{-\lambda_{j} t} \sum_{j=0}^{\infty}\left(\frac{\lambda_{j} t}{j!}\right) F_{X}^{(j)}(200)
\end{aligned}
$$

Figure 9.5 shows the probability for the system in state 3 as a function of time $t$ where the solid line represents the compound Poisson process $D(t)=\sum_{i=0}^{N(t)} X_{i}$ with rate $\lambda=.04$ and the dotted line represents the compound Poisson process with rate $\lambda=.8$. In Figure 9.5, we observe in this example that, as $t$ reaches to 50 the system probability in state 3 quickly approaches to zero when the rate is given as $\lambda=.8$. and as a stable condition with $\lambda=.04$.

Since $R_{2}=\left\{\left(2_{1}, 1_{2}\right),\left(2_{1}, 2_{2}\right)\right\}$, the probability in state 2 is given by$$
\begin{aligned}
P_{t}(2) & =P_{t}\left\{f\left(2_{1}, 1_{2}\right)\right\}+P_{t}\left\{f\left(2_{1}, 2_{2}\right)\right\} \\
& =(U V) e^{-\lambda_{2} t} \sum_{j=0}^{\infty}\left(\frac{\lambda_{2} t}{j!}\right) F_{X}^{(j)}(200)
\end{aligned}
$$

where $U=\Phi\left(\frac{2000-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)-\Phi\left(\frac{1500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)$,

$$
V=1-\frac{1}{100}\left(\frac{t}{t-0.01}\right)(0.4)^{\frac{0.01}{t}}\left(\frac{t}{t-0.01}\right)(0.01)^{1-\frac{0.01}{t}}
$$



Figure 9.5. Probability plot for state $3 v s$. time
Figure 9.6 shows the probability in state 2 as a function of time $t$ where the solid line represents the compound Poisson process $D(t)=\sum_{i=0}^{N(t)} X_{i}$ with rate $\lambda=.04$, and the dotted line represents the compound Poisson process with rate $\lambda=.8$.


Figure 9.6. Probability plot for state $2 v s$. timeFrom Figure 9.6 we observe that before the time $t$ progresses to 5 the probability in state 2 stays close to zero for both the rate $\lambda=.8$. and $\lambda=.04$. It should be noted that the two curves are almost the same for rate $\lambda=.8$ and $\lambda=.04$. Similar observations are true for the probability in state 1 except that the curve rising starting point is 15 not 5 . For details, see Li and Pham (2005b).

We can also easily obtain the probability in state 0 as follows:

$$
\begin{aligned}
P_{t}(0) & =P\left\{f\left(0_{1}, 1_{2}\right)+f\left(0_{1}, 2_{2}\right)+f\left(1_{1}, 0_{2}\right)+f\left(2_{1}, 0_{2}\right)+f\left(3_{1}, 0_{2}\right)+f\left(1_{1}, 1_{2}\right)\right\} \\
& =\left(X_{1} Y_{1}+X_{2} Y_{2}+X_{3} Y_{3}\right) e^{-\lambda_{2} t} \sum_{j=0}^{\infty}\left(\frac{\lambda_{2} t}{j!}\right) F_{X}^{(j)}(200)
\end{aligned}
$$

where

$$
\begin{aligned}
& X_{1}=1-\Phi\left(\frac{2500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right) \\
& X_{2}=\Phi\left(\frac{2500-(90+78 t)}{\sqrt{25+6 t^{2}}}\right) \\
& Y_{1}=1-\frac{1}{100}(0.4)^{\frac{0.01}{t}}\left(\frac{t}{t-0.01}\right)\left(0.01^{1-\frac{0.01}{t}}\right) \\
& Y_{2}=\frac{1}{100}(0.4)^{\frac{0.01}{t}}\left(\frac{t}{t-0.01}\right)\left(0.01^{1-\frac{0.01}{t}}\right) \\
& X_{3}=\Phi\left(\frac{2500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)-\Phi\left(\frac{2000-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right) \\
& Y_{3}=1-\frac{1}{100}\left(\left(\frac{22}{13}\right)^{\frac{0.01}{t}}+(0.4)^{\frac{0.01}{t}}\right)\left(\frac{t}{t-0.01}\right)\left(0.01^{1-\frac{0.01}{t}}\right)
\end{aligned}
$$

Figure 9.7 shows the probability in state $0 v s$. time $t$ where the solid line represents the compound Poisson process $D(t)=\sum_{i=0}^{N(t)} X_{i}$ with rate $\lambda=.04$, and the dotted line represents the compound Poisson process with rate $\lambda=.8$. From Figure 9.7, we observe that the probability in state 0 is almost close to zero as $t$ reaches 100 or higher for the rate $\lambda=.8$.

The probability in state $F$ is calculated as

$$
\begin{aligned}
P_{t}(F) & =P\left\{Y_{1}(t) \leq G_{1}, Y_{2}(t) \leq G_{2}, D(t)>S\right\} \\
& =K L\left\{1-e^{-\lambda_{2} t} \sum_{j=0}^{\infty}\left(\frac{\lambda_{2} t}{j!}\right) F_{X}^{(j)}(200)\right\}
\end{aligned}
$$

where $K=\Phi\left(\frac{2500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right), L=1-\frac{1}{100}(0.4)^{\frac{0.01}{t}}\left(\frac{t}{t-0.01}\right)\left(0.01^{1-\frac{0.01}{t}}\right)$

Figure 9.7. Probability plot for state 0
Figure 9.8 shows the probability in state $F$ as a function of time $t$ where the solid line represents the compound Poisson process $D(t)=\sum_{i=0}^{N(t)} X_{i}$ with rate $\lambda=.04$, and the dotted line represents the compound Poisson process with rate $\lambda=.8$. The two curves exhibit quite different shapes.


Figure 9.8. Probability plot for state $F$
Finally, the system reliability $R(t)$ is given by

$$
\begin{aligned}
R(t) & =P\{\text { system state } \geq 1\} \\
& =\sum_{i=1}^{3} P_{i}(i) \\
& =X_{3} Y_{3} e^{-\lambda_{3} t} \sum_{j=0}^{\infty}\left(\frac{\lambda_{3} t}{j!}\right) F_{X}^{(j)}(200)
\end{aligned}
$$

where$$
\begin{aligned}
& X_{3}=\Phi\left(\frac{2000-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)\left\{1-\frac{1}{100}\left[(0.4)^{\frac{0.01}{t}}+\left(\frac{22}{13}\right)^{\frac{0.01}{t}}\right]\left(\frac{t}{t-0.01}\right)\left(0.01^{1-\frac{0.01}{t}}\right)\right\}, \\
& Y_{3}=\left\{\Phi\left(\frac{2500-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)-\Phi\left(\frac{2000-(90+78 t)}{\sqrt{2.5+6 t^{6}}}\right)\right\} \\
& \times\left\{1-\frac{1}{100}\left(\frac{t}{t-0.01}\right)\left(\frac{22}{13}\right)^{\frac{0.01}{t}} 0.01^{1-\frac{0.01}{t}}\right\}
\end{aligned}
$$

Figure 9.9 shows the system reliability $v s$. time $t$ where the solid line represents the compound Poisson process with rate $\lambda=.04$, and the dotted line represents the compound Poisson process with rate $\lambda=.8$. As for the rate $\lambda=.8$. we can see that the system likely will fail after time $t$ equals to 50 .


Figure 9.9. Reliability function
This section discusses a generalized model for evaluating the reliability of multi-state degraded systems, without maintenance and repair, considering two degradation processes and random shocks. The model can be used not only to determine the reliability of the degraded systems in the context of muli-state functions but also to obtain the states of the systems by calculating the system state probabilities. Next section will incorporate maintenance and repair strategies into the developed model and investigate the trade-off between the maintenance cost and reliability.

# 9.2 Optimal Inspection-maintenance 

In this section, we will present a generalized condition-based maintenance model subject to multiple competing failure processes including two degradation processes and random shocks. An average long-run maintenance cost rate functionis derived based on the expressions for the degradation paths and cumulative shock damage, which are measurable. A quasi-renewal process is employed to develop the inter-inspection sequence. Upon inspection, a decision will be made as to whether one needs to perform maintenance, either preventive or corrective, or to do nothing. The PM thresholds for degradation processes and inspection sequence are decision variables. This section also discusses an algorithm based on the NelderMead downhill simplex method (Rardin 1998) to obtain the optimum solution minimizing the average long-run maintenance cost rate. Numerical examples are given to illustrate the results using the optimization algorithm.

In some production systems failures are not possible to detect but can only be determined by an inspection (Bris et al. 2003). Various inspection policies and models for systems with a degradation process have been proposed. Grall et al. (2002a) study a system subject to a random deterioration process. They develop a model based on a stationary process to determine both the PM threshold and inspection dates that minimized the average long-run cost rate.

Grall et al. (2002b) recently study the inspection-maintenance strategy for a single unit deteriorating system based on a Gamma process in which it has the stationary and independent increment property. They create the inspectionmaintenance strategy consisting of PM threshold and inspection schedule that minimized the maintenance cost function based on regenerative and semiregenerative properties.

Chelbi and Ait-Kadi (1999) address the optimal inspection strategies for deteriorating equipment subject to PM and CM. Klutke and Yang (2002) study the availability of maintained systems subject to both the effects of the degradation and random shocks. They considered the degradation process as a deterministic function of time $t$ and the shocks occur according to a Poisson process in which the shock magnitudes are independent and identically distributed random variables.

This section considers systems with inspection-based maintenance subject to three failure processes that are competing for the life of such systems. Same as in Section 9.1, two of them are degradation processes (degradation process $i$ measured by $Y_{i}(t)$ for $\left.i=1,2\right)$ and the third is a random shock process measured by the function $D(t)$. The three processes are independent and any of them would cause the system to fail. The failure of the system is defined as when $Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2}$ or $D(t)>S$ whichever occurs first. Note that the state of the systems can only be revealed through an inspection,

This section discusses optimal inspection-maintenance policies, consisting of the time sequence for inspection and PM threshold levels for both degradation processes, to determine trade-off between the failure frequency and system total cost.

The optimal inspection-maintenance policies in this section differ from others. First, a system with three competing processes instead of one is considered. Second, it is assumed that the degradation and shock damage are measurable. Otherwise there are some parameters associated with the processes that can be traced (such as vibration analysis for tool wear and failure). The maintenance decision is made based upon the threshold levels of the degradations and cumulative shock damage, not on the distribution parameters or transitionprobability as in other studies (Grall et al. 2002b; Chelbi and Ait-Kadi 1999). Third, the modeling method is other than Markov, semi-Markov and the stationary processes.

This section uses the two degradation path functions as follows:
i) Function $Y(t)=A+B g(t)$ : random-coefficient degradation path, where $A>0$ and $B>0$ are independent random variables and $g(t)$ is an increasing function of time $t$. The random variable $A$ represents a measure of the initial degradation value and $B$ represents the measure of the coefficient of the degradation.
ii) Function $Y(t)=W e^{B t} /\left(A+e^{B t}\right)$ : the randomized logistic degradation path function, where $A$ and $B$ are independent non-negative random variables, and $W$ is a constant. The random variable $A$ represents the initial threshold level of degradation and $B$ describes the rate at which degradation accumulates.

Note that logistic function $y(t)=e^{b t} /\left(a+e^{b t}\right)$ for $a>0$ and $b>0$, as an $S$ shaped curve, for example, describes well the degradation process and it matches the path of the cumulative degradation of many systems in practice. The $S$-shaped curve reflects an initial run-in period of low usage, following by a period of steady rate of the usage, and finally ending with an increasing rate of use due to the aging of the system. Unlike most other work, the degradation path in this section is a stochastic process associated with the two random variables, not a deterministic. This section assumes the shock process is modeled according to a compound Poisson process $D(t)=\sum_{i=0}^{N(t)} X_{i}$ where $X_{i}$ s are i.i.d. and $N(t)$ follows a Poisson distribution with parameter $\lambda_{1}: N(t) \sim \operatorname{Poisson}\left(\lambda_{1}\right)$.

Maintenance has evolved from simply the model which reacts to machine breakdowns, to the time-based model, and to today's condition-based model. This section considers condition-based maintenance where there are two possible maintenance actions: PM or CM. The need for PM or CM is determined upon each inspection and the inspection cycles is reduced according to a quasi-renewal process as the system ages. The system is inspected at times $I_{1}, \ldots, I_{n}$. Upon inspection, one of the following two choices has to be made:
i) Do nothing but determine the time for the next inspection.
ii) The system has failed and a maintenance (PM or CM) action is begun instantaneously.

Since the state of the system can only be determined through inspection, the determination of the inspection times $\left\{I_{1}, \ldots, I_{i}, \ldots\right\}$ and PM thresholds $\left(L_{1}, L_{2}\right)$ will certainly make a great influence on the maintenance cost rate as well as the total system cost. This section uses a condition-based maintenance model to determine the optimal inspection schedule and PM thresholds $\left(L_{1}, L_{2}\right)$ for complex repairable systems. Both the decision variables - inspection times and PM thresholds are important for trading off the cost between the maintenance (both PM and CM), inspection and the losses due to system idle.The rest of Section 9.2 is organized as follows. The inspection-maintenance policy is described in Section 9.2.1. A new mathematical cost rate model is derived in Section 9.2.2. An optimization algorithm based on Nelder-Mead downhill simplex method is presented in Section 9.2.3. Numerical examples are given in Section 9.2.4.

# 9.2.1 A General Inspection-maintenance Policy 

This section assumes:
i) The system failure is only detected by each inspection. Inspections are assumed to be instantaneous, perfect and non-destructive. Since the system is not continuously monitored, if the system fails it will remain failed until the next inspection, which causes a loss of $C_{m}$ per unit time. In that case, a maintenance action is begun instantaneously at the inspection's time.
ii) After a maintenance action, either PM or CM, the system state will become as good as new.
iii) A CM action will cost more than a PM action. Similarly, a PM action will cost much more than an inspection itself. This implies that $C_{c}>C_{p}>C_{i}$.
iv) The three processes: $Y_{1}(t), Y_{2}(t)$ and $D(t)$ are independent.
v) No continuous monitoring is performed on the system.
vi) CM or PM time is negligible.

Although continuous monitoring process to some systems is feasible, the cost to monitor the process and the labor extensive would not make it realistic in practices. Therefore the criteria we consider in this section is to improve the system performance by performing periodic inspections with a maintenance action if necessary as the same token by minimizing the total system maintenance cost. Since deterioration while running leads to system failure, it proves to be better to assume that, as we take into account in this section, the degradation paths are continuous and increasing functions.

The length of the inspection will be reduced as the system ages. In other words, the intervals between successive inspections become shorter as the system ages. A quasi-renewal process is applied in this section to develop the inter-inspection sequence. Inspection time is constructed as $I_{n}=\sum_{j=1}^{n} \alpha^{j-1} I_{1}$, where $0<\alpha \leq 1$ and $I_{1}$ is the first inspection time. We define $U_{n}=I_{n}-I_{n-1}=\alpha^{n-1} I_{1}$ as the interinspection interval and $\left\{U_{i}\right\}_{i \in N}$ are a decreasing geometric sequence. According to the state detected at the inspection $I_{n}, n=1, \ldots$, one of the following actions is taken:
i) If both degradation values are below their PM thresholds and the shock damage value is less than its threshold, in other words, if $\left\{Y_{1}\left(I_{n}\right) \leq L_{1}, Y_{2}\left(I_{n}\right) \leq L_{2}\right\} \cap\left\{D\left(I_{n}\right) \leq S\right\}$, then the system is still in a good condition. In this case, we do nothing but determine the nextinspection at $I_{n+1}=I_{n}+U_{n}$ where $U_{n}$ is the inter-inspection time between $n^{\text {th }}$ and $(n+1)^{\text {th }}$ inspection interval.
ii) If there is a degradation process that falls into the PM zone $\left(L_{i}<Y_{i}\left(I_{n}\right) \leq G_{i}, i=1,2\right)$ and the other two processes are less than their corresponding critical thresholds, then the system is called for a PM action and it is instantaneously performed accordingly.
iii) If any of the processes is exceeding its corresponding critical threshold value $\left(Y_{i}(t)>G_{i}, i=1,2\right.$, or $\left.D(t)>S\right)$, then the system is called for a CM action and it is instantaneously performed. In this case, the system has failed and a CM is performed on the system.


Figure 9.10. Evolution of the system condition
We assume that after a maintenance action, i.e., PM or CM, the system will again be as good as new. A new sequence of inspection begins which is defined in the same way and the system maintenance follows the same decision rules outlined above. Figure 9.10 shows the evolution of the system where $Y_{1}(t)$ and $Y_{2}(t)$represent the degradation process 1 and process 2 , respectively, and $D(t)$ represents a cumulative shock damage. $\left\{W_{i}\right\}_{i \in N}$ is a renewal sequence.

Figure 9.11 shows the maintenance zones on the $Y_{1}(t), Y_{2}(t)$ plane. $G_{i}$ and $L_{i}$ are the CM and PM critical thresholds for $Y_{i}(t)$, respectively, $i=1,2$.


Figure 9.11. Maintenance zone projected on $Y_{1}(t), Y_{2}(t)$

# 9.2.2 Average Long-run Maintenance Cost Analysis 

In this section we derive the average long-run maintenance cost per unit time, and next section will discuss minimizing the average long-run maintenance cost rate by determining the PM critical threshold values $\left(L_{1}, L_{2}\right)$ and inspection sequence.

### 9.2.2.1 Expected Maintenance Cost in a Cycle

Suppose that the time horizon is infinity. From the basic renewal theory, we have

$$
\lim _{t \rightarrow \infty} \frac{C(t)}{t}=\frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}
$$

The expected total maintenance cost per cycle, $E\left[C_{1}\right]$, is given as

$$
E\left[C_{1}\right]=C_{i} E\left[N_{I}\right]+C_{p} P_{p}+C_{c} P_{c}+C_{m} E[\zeta]
$$

where $C_{i}$ is the cost associated with each inspection, $C_{p}$ is the cost associated with a PM action, and $C_{c}$ is the CM action cost. Since failure is not self-announcing and it can be occurred at any given instant time $T$ within the inspection time interval $\left[I_{i}, I_{i+1}\right]$, the system will remain idle during the interval $\left[T, I_{i+1}\right]$. The cost coefficient $C_{m}$ is defined as the penalty cost per unit time associated with such an event.

1) Let $P\left\{N_{I}=i+1\right\}$ be the probability that there are a total of $(i+1)$ inspections in the cycle. The expected number of inspections during a cycle, $E\left[N_{I}\right]$, is given by$$
E\left[N_{I}\right]=\sum_{i=0}^{\infty}(i+1) P_{i+1}
$$

where $P_{i+1}=P\left\{N_{I}=i+1\right\}$.
It can be obtained that

$$
\begin{aligned}
P_{i+1} & =P\left\{N_{I}=i+1\right\} \\
& =\bigcup_{j=1}^{17} P\left\{E_{j}^{(i+1)}\right\}
\end{aligned}
$$

where $E_{j}^{(i+1)}(j=1, \ldots, 17)$ denotes the renewal cycle ending at the $j^{\text {th }}$ possibility at time $I_{i+1}$ :

$$
\begin{aligned}
E_{1}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}, L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{2}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}, Y_{2}\left(I_{i+1}\right) \leq L_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{3}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}, L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{4}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}, Y_{2}\left(I_{i+1}\right)>G_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{5}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}\right. \\
& \left.L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}, D\left(I_{i+1}\right)>S\right\} \\
E_{6}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}, Y_{2}\left(I_{i+1}\right)>G_{2}\right. \\
& D\left(I_{i+1}\right)>S\} \\
E_{7}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, L_{2}>Y_{2}\left(I_{i+1}\right)\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{8}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\} \\
E_{9}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, L_{2}>Y_{2}\left(I_{i+1}\right)\right. \\
& D\left(I_{i+1}\right)>S\} \\
E_{10}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right. \\
& D\left(I_{i+1}\right)>S\} \\
E_{11}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, Y_{2}\left(I_{i+1}\right)>G_{2}\right. \\
& D\left(I_{i+1}\right) \leq S\}
\end{aligned}
$$$$
\begin{aligned}
E_{12}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right)>G_{1}, Y_{2}\left(I_{i+1}\right)>G_{2}\right. \\
& \left.D\left(I_{i+1}\right)>S\right\} \\
E_{13}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}, L_{2}>Y_{2}\left(I_{i+1}\right)\right. \\
& \left.D\left(I_{i+1}\right)>S\right\} \\
E_{14}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}>Y_{1}\left(I_{i+1}\right), L_{2}>Y_{2}\left(I_{i+1}\right)\right. \\
& \left.D\left(I_{i+1}\right) \leq S\right\} \\
E_{15}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}>Y_{1}\left(I_{i+1}\right), L_{2}>Y_{2}\left(I_{i+1}\right)\right. \\
& \left.D\left(I_{i+1}\right)>S\right\} \\
E_{16}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}>Y_{1}\left(I_{i+1}\right), L_{2}<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right. \\
& \left.D\left(I_{i+1}\right)>S\right\} \\
E_{17}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{L_{1}>Y_{1}\left(I_{i+1}\right), Y_{2}\left(I_{i+1}\right)>G_{2}\right. \\
& \left.D\left(I_{i+1}\right) \leq S\right\} \\
E_{18}^{(i+1)}= & \left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\} \cap\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}, Y_{2}\left(I_{i+1}\right) \leq L_{2}\right. \\
& \left.D\left(I_{i+1}\right) \leq S\right\}
\end{aligned}
$$

Note that $E_{j}^{(i+1)} \mathrm{s}$ are mutually disjoined events for $j=1, \ldots, 17$.
There are a total of 18 system state combinations that can be revealed at any given interval $\left(I_{i}, I_{i+1}\right]$ where as there is only one state event $E_{18}^{(i+1)}$ representing the fact that the system is in a good condition and that no maintenance action will be required. Any other remaining state events will trigger either a PM or a CM action at time $I_{i+1}$.

After some simplifications, we have

$$
\begin{aligned}
P_{i+1}= & P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\}-P\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}, Y_{2}\left(I_{i+1}\right) \leq L_{2}\right. \\
& \left.D\left(I_{i+1}\right) \leq S\right\}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
E\left[N_{1}\right]= & \sum_{i=0}^{\infty}(i+1)\left\{P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{2}\left(I_{i}\right) \leq L_{2}, D\left(I_{i}\right) \leq S\right\}\right. \\
& \left.-P\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}, Y_{2}\left(I_{i+1}\right) \leq L_{2}, D\left(I_{i+1}\right) \leq S\right\}\right\}
\end{aligned}
$$

2) There will be either a PM or CM action ending a renewal cycle. It is obviously that the two events (PM and CM) are mutually exclusive at renewal time points, i.e., $P_{p}+P_{c}=1$. We now evaluate $P_{p}$ as follows:

$$
P_{p}=P\{\text { the cycle ends due to an PM action }\}
$$$$
=\sum_{i=0}^{\infty} \sum_{j=1}^{3} P\left\{E_{j}^{(i+1)}\right\}
$$

After some simplifications, we obtain

$$
\begin{aligned}
P_{p}= & \sum_{i=0}^{\infty}\left\{P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}\right\} P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}, Y_{2}\left(I_{i+1}\right) \leq G_{2}\right\} P\left\{D\left(I_{i+1}\right\}\right. \\
& \left.+P\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}\right\} P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}, L<Y_{2}\left(I_{i+1}\right) \leq G_{2}\right\} P\left\{D\left(I_{i+1}\right\}\right\}
\end{aligned}
$$

and $P_{c}=1-P_{p}$.
We can obtain the joint probability density function $f_{Y\left(I_{i}\right), Y\left(I_{i+1}\right)}\left(y_{1}, y_{2}\right)$ of $Y\left(I_{i}\right)$ and $Y\left(I_{i+1}\right)$ by computing probabilities $P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{1}\left(I_{i+1}\right) \leq G_{1}\right\}$ and $P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}, Y_{2}\left(I_{i+1}\right) \leq G_{2}\right\}$.

We consider two different degradation functions for $Y(t)$ as follows:

CASE 1: Assume $Y(t)=A+B g(t)$ where $A>0$ and $B>0$ are two independent random variables and its corresponding $p d f$ are $f_{A}(a)$ and $f_{B}(b)$, respectively, and $g(t)$ is an increasing function. Let

$$
\left\{\begin{array}{l}
y_{1}=a+b g\left(I_{i}\right) \\
y_{2}=a+b g\left(I_{i+1}\right)
\end{array}\right.
$$

After solving the above two equations in terms of $y_{1}$ and $y_{2}$, we have

$$
\begin{aligned}
& a=\frac{y_{1} g\left(I_{i+1}\right)-y_{2} g\left(I_{i}\right)}{g\left(I_{i+1}\right)-g\left(I_{i}\right)}=h_{1}\left(y_{1}, y_{2}\right) \\
& b=\frac{y_{2}-y_{1}}{g\left(I_{i+1}\right)-g\left(I_{i}\right)}=h_{2}\left(y_{1}, y_{2}\right)
\end{aligned}
$$

The Jacobian $J$ is given by

$$
J=\left|\begin{array}{ll}
\frac{\partial h_{1}}{\partial y_{1}} \frac{\partial h_{1}}{\partial y_{2}} \\
\frac{\partial h_{2}}{\partial y_{1}} \frac{\partial h_{2}}{\partial y_{2}}
\end{array}\right|=\left|\frac{1}{g\left(I_{i}\right)-g\left(I_{i+1)}\right)}\right|
$$

Therefore, the joint continuous $p d f$ of a random vector $\left(Y\left(I_{i}\right), Y\left(I_{i+1}\right)\right)$ can be calculated as follows:

$$
f_{Y\left(I_{i}\right), Y\left(I_{i+1}\right)}\left(y_{1}, y_{2}\right)=|J| f_{A}\left(h_{1}\left(y_{1}, y_{2}\right)\right) f_{B}\left(h_{2}\left(y_{1}, y_{2}\right)\right)
$$CASE 2: Suppose $Y(t)=W e^{A t} /\left(B+e^{A t}\right)$ where $A>0$ and $B>0$ are two independent $r . v . s$ and its corresponding $p d f$ are $f_{A}(a)$ and $f_{B}(b)$, respectively. Let

$$
\left\{\begin{array}{l}
y_{1}=\frac{W e^{a I_{i}}}{b+e^{a I_{i}}} \\
y_{2}=\frac{W e^{a I_{i+1}}}{b+e^{a I_{i+1}}}
\end{array}\right.
$$

The solutions for $a$ and $b$ can be easily solved from the above equations in terms of $y_{1}$ and $y_{2}$ as follows:

$$
\left\{\begin{array}{l}
a=\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right)}{I_{i+1}-I_{i}}=h_{1}\left(y_{1}, y_{2}\right), \text { where } y_{2} \neq W \\
b=-\frac{\left(y_{2}-W\right)}{y_{2}} \exp \left(\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right) I_{i+1}}{I_{i+1}-I_{i}}\right)=h_{2}\left(y_{1}, y_{2}\right), \text { where } y_{2} \neq W
\end{array}\right.
$$

Similarly, the joint continuous $p d f$ of random vector $\left(Y\left(I_{i}\right), Y\left(I_{i+1}\right)\right)$ can be obtained:

$$
f_{Y\left(I_{i}\right), Y\left(I_{i+1}\right)}\left(y_{1}, y_{2}\right)=|J| f_{A}\left(h_{1}\left(y_{1}, y_{2}\right)\right) f_{B}\left(h_{2}\left(y_{1}, y_{2}\right)\right)
$$

where $J$ is given by

$$
J=\frac{y_{1}\left(y_{2}-W\right)\left(\frac{y_{2}}{y_{1}\left(y_{2}-W\right)}-\frac{y_{2}\left(y_{1}-W\right)}{y_{1}^{2}\left(y_{2}-W\right)}\right)\left(-d\left(y_{1}, y_{2}\right)-d_{1}\left(y_{1}, y_{2}\right)+d_{2}\left(y_{1}, y_{2}\right)\right)}{y_{2}\left(y_{1}-W\right)\left(I_{i+1}-I_{i}\right)}+d_{3}\left(y_{1}, y_{2}\right)
$$

where

$$
d\left(y_{1}, y_{2}\right)=\frac{\left(\left(\frac{y_{1}-W}{y_{1}\left(y_{2}-W\right)}-\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)^{2}}\right) y_{1}\left(y_{2}-W\right)^{2} I_{i+1} e^{-\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right) I_{i+1}}{I_{i+1}-I_{i}}}\right)}{y_{2}^{2}\left(y_{1}-W\right)\left(I_{i+1}-I_{i}\right)}
$$

where $y_{1} \neq W, y_{2} \neq W$$$
\begin{aligned}
& d_{1}\left(y_{1}, y_{2}\right)=\frac{1}{y_{2}} \exp \left(\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right) I_{i+1}}{I_{i+1}-I_{i}}\right), \quad y_{2} \neq W \\
& d_{2}\left(y_{1}, y_{2}\right)=\frac{\left(y_{2}-W\right) \exp \left(\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right) I_{i+1}}{I_{i+1}-I_{i}}\right)}{y_{2}^{2}}, \quad y_{2} \neq W \\
& d_{3}\left(y_{1}, y_{2}\right)=\frac{d_{31}\left(y_{1}, y_{2}\right) d_{32}\left(y_{1}, y_{2}\right)}{y_{2}^{3}\left(y_{1}-W\right)^{2}\left(I_{i+1}-I_{i}\right)^{2}}, \quad y_{1} \neq W \\
& d_{31}\left(y_{1}, y_{2}\right)=\left(\frac{y_{1}-W}{y_{1}\left(y_{2}-W\right)}-\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)^{2}}\right) y_{1}^{2}\left(y_{2}-W\right)^{3}, \quad y_{2} \neq W \\
& d_{32}\left(y_{1}, y_{2}\right)=\left(\frac{y_{2}}{y_{1}\left(y_{2}-W\right)}-\frac{y_{2}\left(y_{1}-W\right)}{y_{1}^{2}\left(y_{2}-W\right)}\right) I_{i+1} \cdot \exp \left(\frac{\ln \left(\frac{y_{2}\left(y_{1}-W\right)}{y_{1}\left(y_{2}-W\right)}\right) I_{i+1}}{I_{i+1}-I_{i}}\right)
\end{aligned}
$$

where $y_{2} \neq W$
3) Let $T$ denote the time to system failure, i.e., mathematically, $T=\inf \left\{t: Y_{1}(t)>G_{1}, Y_{2}(t)>G_{2}\right.$ or $\left.D(t)>S\right\}$. If $I_{i}<T \leq I_{i+1}$, the unit will be idle during the interval $\left[T, I_{i+1}\right]$. Let $E[\zeta]$ denote the average idle time between the failure occurrence epoch and its inspection during the cycle. Li and Pham (2005a) obtain that

$$
\begin{aligned}
E[\xi] & =\sum_{i=0}^{\infty} E\left[\left(I_{i+1}-T\right) I_{I_{i}<T \leq I_{i+1}}\right] \\
& =\sum_{j=0}^{\infty} R_{j} \int_{I_{i}}^{I_{i+1}}\left(I_{i+1}-t\right) d F_{T}(t)
\end{aligned}
$$

where

$$
\begin{aligned}
R_{j}= & \left\{P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, L_{1}<Y_{1}\left(I_{i+1}\right) \leq G_{1}\right\} P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}, L_{1}<Y_{1}\left(I_{i+1}\right)\right\}\right. \\
& +P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}\right\} P\left\{Y_{1}\left(I_{i}\right) \leq L_{1}, Y_{1}\left(I_{i+1}\right)>G_{1}\right\}+P\left\{Y_{1}\left(I_{i+1}\right) \leq L_{1}\right\} \\
& \left.P\left\{Y_{2}\left(I_{i}\right) \leq L_{2}\right\}\right\} P\left\{D\left(I_{i}\right) \leq S\right\}
\end{aligned}
$$$$
\begin{aligned}
F(t)= & P\left\{Y_{1}(t)>G_{1}, Y_{2}(t) \leq G_{2}, D\left(I_{i}\right) \leq S\right\}+P\left\{Y_{1}(t) \leq G_{1}, Y_{2}(t)>G_{2}, D\left(I_{i}\right) \leq S\right\} \\
& +P\left\{Y_{1}(t) \leq G_{1}, Y_{2}(t) \leq G_{2}, D\left(I_{i}\right)>S\right\}
\end{aligned}
$$

and $I_{I_{i}<T \leq I_{i+1}}$ is an indicator function.

# 9.2.2.2 Expected Cycle Length 

The expected cycle length $E\left[W_{1}\right]$ is given as follows:

$$
\begin{aligned}
E\left[W_{1}\right] & =E\left[E\left[W_{1} \mid N_{I}\right]\right] \\
& =\sum_{i=0}^{n} E\left[W_{1} \mid N_{I}=i\right] P\left\{N_{i}=i\right\} \\
& =\sum_{i=0}^{n} I_{i+1} P_{i+1}
\end{aligned}
$$

where $P_{i+1}$ is given in Equation (9.18).
Therefore, the average long-run maintenance cost rate function $E C\left(L_{1}, L_{2}, I_{1}\right)$ :

$$
E C\left(L_{1}, L_{2}, I_{1}\right)=\frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}
$$

is a function of the inspection times $\left\{I_{1}, \ldots I_{i}, \ldots\right\}$ and the PM critical threshold values $\left(L_{1}, L_{2}\right)$ through functions $P_{p}, P_{c}, E\left[N_{I}\right], E[\zeta]$ and $E\left[W_{1}\right]$. It can be obtained by solving the two functions given in Equations (9.16) and (9.23).

### 9.2.3 Algorithms for Optimal Inspection-maintenance Policy

This section will discuss a step-by-step algorithm based on the Nelder-Mead downhill simplex method (Rardin 1998) to obtain the optimum decision variables $\left(I_{1}, L_{1}, L_{2}\right)$ such that the long-run average system maintenance cost rate $E C\left(L_{1}, L_{2}, I_{1}\right)$ is minimized. Note that the inspection sequence $\left\{I_{1}, \ldots I_{i}, \ldots\right\}$, where $I_{n}=\sum_{j=1}^{n} \alpha^{j-1} I_{1}$, depends on $I_{1}$ for given $\alpha$. Mathematically, the optimization problem for the maintenance cost rate can be formulated as follows:

## Optimization Problem:

Find $I_{1}, L_{1}$ and $L_{2}\left(0<L_{1} \leq G_{1}, 0<L_{2} \leq G_{2}\right)$ to minimize

$$
\begin{aligned}
E C\left(L_{1}, L_{2}, I_{1}\right)=\left\{C_{1} \sum_{i=0}^{\infty}(i+1\right. & {\left[P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, D\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq S\right\} } \\
& -P\left\{Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq L_{2}, D\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq S\right]
\end{aligned}
$$$$
\begin{aligned}
& +C_{p} \sum_{i=0}^{\infty}\left[P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq G_{2}\right\} \\
& \times P\left\{Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, Y_{2}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq G_{2}\right\} P\left\{D\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq S\right\} \\
& +C_{c}\left[1-\sum_{i=0}^{\infty}\left(P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq G_{2}\right\}\right.\right. \\
& \left.\left.\times P\left\{Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, Y_{2}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq G_{2}\right\} P\left\{D\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq S\right\}\right)\right] \\
& +C_{m} \sum_{i=0}^{\infty}\left(\left(R_{1 i}+R_{2 i}+R_{3 i}\right) P\left\{D\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq S\right\}\right)\left\{\sum_{i=1}^{i+\alpha^{j-1} I_{1}}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}-t\right) d F_{T}(t)\right\} \\
& \left.\left.\left.\left.\left.\left.\left.-\left(P\left\{Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right)\right(P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, D\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq S\right\}\right.\right.\right.\right. \\
& \left.\left.\left.\left.\left.\left.\left.\left.\left.-\left(P\left\{Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right)\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\left.\left.\left.2\left(L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, D\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq S\right\}\right]\right\}
\end{aligned}
$$

where

$$
\begin{aligned}
& R_{1 i}=P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, L_{1}<Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right) \leq G_{1}\right\} \\
& \times P\left\{Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}, L_{1}<Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right)\right\} \\
& R_{2 i}=P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}, G_{1}<Y_{1}\left(\sum_{j=1}^{i+1} \alpha^{j-1} I_{1}\right)\right\} P\left\{Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}\right\} \\
& R_{3 i}=P\left\{Y_{1}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{1}\right\} P\left\{Y_{2}\left(\sum_{j=1}^{i} \alpha^{j-1} I_{1}\right) \leq L_{2}\right\}
\end{aligned}
$$

The objective function above is a complex nonlinear function. Nelder-Mead downhill simplex method (Rardin 1998) is one of the most popular direct search methods for obtaining the optimum solution of unconstrained nonlinear function, which does not require the calculation of derivatives.

We use the Nelder-Mead method based on the comparison of the function values at the $(n+1)$ vertices for $n$-dimensional decision variables. Each iteration will generate a new vertex for the simplex. If this new point is better than at least one of the existing vertices, it replaces the worst vertex. The simplex vertices are changed through reflection, expansion and contraction operations in order to find an improving solution. The step-by-step algorithm based on Nelder-Mead downhill simplex method is given as follows:

Step 1: Choose $(n+1)$ distinct vertices as an initial set $\left\{Z^{(1)}, \ldots, Z^{(n+1)}\right\}$. Then calculate
function value $f(Z)$ for $i=1,2, \ldots,(n+1)$ where $f(Z)=E C\left(L_{1}, L_{2}, I_{1}\right)$. Puttingthe values $f(Z)$ in an increasing order where $f\left(Z^{(i)}\right)=\min \left\{E C\left(L_{1}, L_{2}, I_{1}\right)\right\}$ and $f\left(Z^{(n+1)}\right)=\max \left\{E C\left(L_{1}, L_{2}, I_{1}\right)\right\}$. Set $k=0$.

Step 2: Compute the best-n centroid $X^{(k)}=\frac{1}{n} \sum_{i=1}^{n} Z^{(i)}$.
Step 3: Use the centroid $X^{(k)}$ in Step 2 to compute away-from-worst move direction $\Delta X^{(k+1)}=X^{(k)}-Z^{(n+1)}$.

Step 4: Set $\lambda=1$ and compute $f\left(X^{(k)}+\lambda \Delta X^{(k+1)}\right)$.
If $f\left(X^{(k)}+\lambda \Delta X^{(k+1)}\right) \leq f\left(Z^{(1)}\right)$ then go to Step 5.
Otherwise, if $f\left(X^{(k)}+\lambda \Delta X^{(k+1)}\right) \geq f\left(Z^{(n)}\right)$ then go to Step 6.
Else, fix $\lambda=1$ and go to Step 8.
Step 5: Set $\lambda=2$ and compute $f\left(X^{(k)}+2 \Delta X^{(k+1)}\right)$.
If $f\left(X^{(k)}+2 \Delta X^{(k+1)}\right) \leq f\left(X^{(k)}+\Delta X^{(k+1)}\right)$ then set $\lambda=2$.
Otherwise set $\lambda=1$.
Then go to Step 8.
Step 6: If $f\left(X^{(k)}+\lambda \Delta X^{(k+1)}\right) \leq f\left(Z^{(n+1)}\right)$ then set $\lambda=1 / 2$. Compute $f\left(X^{(k)}+\frac{1}{2} \Delta X^{(k+1)}\right)$.
If $f\left(X^{(k)}+\frac{1}{2} \Delta X^{(k+1)}\right) \leq f\left(Z^{(n+1)}\right)$ then set $\lambda=1 / 2$ and go to Step 8.
Otherwise, set $\lambda=-1 / 2$ and if $f\left(X^{(k)}-\frac{1}{2} \Delta X^{(k+1)}\right) \leq f\left(Z^{(n+1)}\right)$ then set $\lambda=-1 / 2$ and go to Step 8. Otherwise, go to Step 7.

Step 7: Shrinking the current solution set toward best $Z^{(1)}$ by $Z^{(i)}=\frac{1}{2}\left(Z^{(1)}+Z^{(i)}\right), i=2, \ldots, n+1$. Compute the new $f\left(Z^{(2)}\right), \ldots, f\left(Z^{(n+1)}\right)$, let $k=k+1$, and return to Step 2.

Step 8: Replace the worst $Z^{(n+1)}$ by $X^{(k)}+\lambda \Delta X^{(k+1)}$. If $\sqrt{\frac{1}{n+1} \sum_{i=1}^{n+1}\left[f\left(Z^{(i)}-\bar{f}\right]^{2}\right.}<0.5$, where $\bar{f}$ is an average value, then STOP. Otherwise, let $k=k+1$ and return to Step 2.Note that the criterion in Step 8 is not unique but will depend on how you would like the algorithm to stop when the vertices function values are close. In this section, reference value is when the difference between the maximum and the minimum values of $f$ is less than 0.5 .

# 9.2.4 Numerical Example 

Assume degradation process 1 is described by function $Y_{1}(t)=W e^{B_{1} t} /\left(A_{1}+e^{B_{1} t}\right)$ where the random variables $A_{1}$ and $B_{1}$ are independent and follow the uniform distribution with parameter interval $[0,40]$ and exponential distribution with parameter 1, respectively, i.e., $A_{1} \sim U[0,40]$ and $B_{1} \sim \operatorname{Exp}(1)$ Degradation process 2 is modeled as $Y_{2}(t)=A_{2}+B_{2} g(t)$ where $A_{2} \sim U[0,2], B_{2} \sim \operatorname{Exp}(0.2)$ and $g(t)=\sqrt{t} e^{0.01 t}$. Suppose that the random shock is represented by the function $D(t)=\sum_{i=0}^{N_{1}(t)} X_{i}$, where $X_{i} \sim \operatorname{Exp}(.04)$ and $N(t) \sim \operatorname{Poisson}(.1)$. Critical threshold values are $G_{1}=300, G_{2}=70$ and $S=100$.

Suppose the cost parameters are given as follows: $C_{c}=560$ units $/ C M$, $C_{p}=400$ units $/ P M, C_{i}=100$ units $/$ inspection, $C_{m}=500$ units $/$ unit time, and $\alpha=0.97$.

The inspection sequence $\left\{I_{1}, \ldots, I_{n}, \ldots\right\}$ is per $I_{n}=\sum_{j=1}^{n} \alpha^{j-1} I_{1}$. The objective is to determine the values of $I_{1}, L_{1}$, and $L_{2}$ so that the average long-run maintenance cost rate per unit time is minimized.

Following are the computing details for this example using the optimization algorithm in Section 9.2.3:

Step 1: There are three decision variables: $L_{1}, L_{2}, I_{1}$, and so we need $(n+1)=4$ distinct vertices as an initial set of values which are
$Z^{(1)}=(270,56,76), Z^{(2)}=(280,60,72), Z^{(3)}=(290,52,66)$ and
$Z^{(4)}=(300,50,57)$. Set $k=0$.
Then calculate the function value $f(Z)$ corresponding to each vertices and put them in an increasing order of the objective value $E C\left(L_{1}, L_{2}, I_{1}\right)$ from smallest to highest.
Step 2: Compute the centroid: $X^{(0)}=\frac{1}{3}\left(Z^{(1)}+Z^{(2)}+Z^{(3)}\right)=(280,56,71.3)$.
Step 3: Search for away-from-worst direction: $\Delta X=X^{(0)}-Z^{(4)}=(-20,6,14.3)$.
Step 4: Set $\lambda=1$; it will generate a new minimal $E C(260,60,85.6)=291.9$ which leads to try an expansion with $\lambda=2$ that is $(240,60,99.9)$.
Step 5: Set $\lambda=2$. Similarly, compute $f(Z)$ that leads to 247.9 . Go to Step 8.This result turns out to be a better solution, hence $(300,50,57)$ is replaced by $(240,60,99.9)$. The iteration continues and stops at $k=4$ (see Table 9.1) since

$$
\sqrt{\frac{1}{4} \sum_{i=1}^{4}\left[E C\left(Z^{(i)}\right)-\overline{E C\left(L_{1}, L_{2}, I_{1}\right)}\right]^{2}}=0.449<0.5
$$

where $\overline{E C\left(L_{1}, L_{2}, I_{1}\right)}$ is the average value.
Table 9.1. Nelder-Mead algorithm results

| k | $Z^{(1)}=\left(L_{1}, L_{2}, I_{1}\right)$ | $Z^{(2)}$ | $Z^{(3)}$ | $Z^{(4)}$ | Search results |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | $\begin{aligned} & (270,56,76) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=300.7 \end{aligned}$ | $\begin{aligned} & (280,60,72) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=332.2 \end{aligned}$ | $\begin{aligned} & (290,52,66) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=360.4 \end{aligned}$ | $\begin{aligned} & (300,50,57) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=388.2 \end{aligned}$ | $\begin{aligned} & \lambda=2 \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=247.9 \end{aligned}$ |
| 1 | $\begin{aligned} & (240,60,99.9) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=247.9 \end{aligned}$ | $\begin{aligned} & (270,56,76) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=300.7 \end{aligned}$ | $\begin{aligned} & (280,60,72) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=332.2 \end{aligned}$ | $\begin{aligned} & (290,52,66) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=360.4 \end{aligned}$ | $\begin{aligned} & \lambda=1 \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=248.0 \end{aligned}$ |
| 2 | $\begin{aligned} & (236,60,99.2) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=247.9 \end{aligned}$ | $\begin{aligned} & (240,60,99.9) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=248.0 \end{aligned}$ | $\begin{aligned} & (270,56,76) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=300.7 \end{aligned}$ | $\begin{aligned} & (280,60,72) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=332.2 \end{aligned}$ | $\begin{aligned} & \lambda=2 \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=246.7 \end{aligned}$ |
| 3 | $\begin{aligned} & (187,56,131) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=246.7 \end{aligned}$ | $\begin{aligned} & (236,60,99.2) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=247.9 \end{aligned}$ | $\begin{aligned} & (240,60,99.9) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=248.0 \end{aligned}$ | $\begin{aligned} & (270,56,76) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=300.7 \end{aligned}$ | $\begin{aligned} & \lambda=1 \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=245.9 \end{aligned}$ |
| 4 | $\begin{aligned} & (172,60,144) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=245.9 \end{aligned}$ | $\begin{aligned} & (187,56,131) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=246.7 \end{aligned}$ | $\begin{aligned} & (236,60,99.2) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=247.9 \end{aligned}$ | $\begin{aligned} & (240,60,99.9) \\ & \frac{E\left[C_{1}\right]}{E\left[W_{1}\right]}=248.0 \end{aligned}$ | Stop |



Figure 9.12. $E C\left(L_{1}, L_{2}, I_{1}\right)$ vs. $I_{1}$Table 9.1 shows the optimal solution for $\left(L_{1}, L_{2}, I_{1}\right): L_{1}^{*}=172, L_{2}^{*}=60$, $I_{1}^{*}=144$ and the corresponding minimum average long-run maintenance cost rate is $E C\left(L_{1}^{*}, L_{2}^{*}, I_{1}^{*}\right)=245.9$. Figure 9.12 depicts the average long-run maintenance cost rate curve $E C\left(L_{1}, L_{2}, I_{1}\right)$ as a function of the inspection time interval $I_{1}$ given that $L_{1}=172$ and $L_{2}=60$.

Table 9.2 exhibits a sensitivity analysis in terms of the probability that the cycle will end due to a PM action, $P_{p}$, for various values of $\left(L_{1}, L_{2}\right)$ for given $\alpha=0.97$ and $I_{1}=144$. Table 9.2 shows that probability $P_{p}$ slightly increases as both $L_{1}$ and $L_{2}$ decrease. This suggests that one would perform more PMs than CMs when $L_{1}$ and $L_{2}$ are both getting smaller.

Table 9.2. The effect of $\left(L_{1}, L_{2}\right)$ on $P_{p}$ for a given inspection sequence

| $L_{1}$ | $L_{2}$ | $P_{p}$ |
| :--: | :--: | :--: |
| 200 | 60 | .5910 |
| 190 | 58 | .5928 |
| 180 | 56 | .5936 |
| 170 | 54 | .5948 |
| 160 | 52 | .5950 |
| 150 | 50 | .5968 |

Similarly, Table 9.3 shows the probability that the cycle will end due to a PM action, $P_{p}$, for various values of $I_{1}$ given $L_{1}=172, L_{2}=60$ and $\alpha=0.97$. From Table 9.3, we observe that the probability $P_{p}$ decreases as $I_{l}$ increases. In other words, the maintenance cycle likely will be ended due to a CM rather than a PM if one should delay the inspection. This result can help the maintenance managers or inspectors to allocate resources and time.

Table 9.3. The effect of inspection sequence on $P_{p}$ for fixed PM values

| $I_{1}$ | $P_{p}$ |
| :--: | :--: |
| 110 | .642 |
| 120 | .610 |
| 130 | .578 |
| 140 | .510 |
| 150 | .480 |
| 160 | .430 |

This section has presented a generalized inspection-maintenance model with multiple competing processes based on different degradation paths and cumulative shock damage. A step-by-step algorithm based on Nelder-Mead downhill simplex method is presented to obtain the optimum decision variables that minimize the long-run average maintenance system cost rate. The decision variables are the inspection sequences as well as the PM critical threshold values.The models in this section can be used to help the maintenance managers and inspectors in particular and marketing managers in general to allocate the resources as well as promotion strategies for the new products.# Warranty Cost Models with Dependence and Imperfect Repair 

Today most equipment offers some level of warranty, and warranty cost could be a significant portion of overall product cost (Wang et al. 2004). Warranty is an obligation attached to products that requires the warranty issuers (manufacturers or sellers) to provide compensation for consumers (buyers) according to the warranty terms when the warranted products fail to perform their pre-specified functions under normal usage within the warranty coverage period, per Blischke and Murthy (1996). It can be considered as a contractual agreement between buyer and seller which becomes effective upon the sale of the warranted products.

A warranty contract should contain at least three characteristics: the coverage period (fixed or random), the method of compensations, and the conditions under which such compensations would be offered. The last characteristic is closely related to warranty execution since it clarifies consumers' rights and protects warranty issuers from excessive false claims. From the cost perspective, the first two characteristics are more important to manufacturers because they determine the depth of the protection against premature failures and the direct cost related to those failures.

From the manufacturer's point of view, one of the main roles of warranty is protection (Blischke and Murthy 1996). Warranty terms may, and often do, specify the use and conditions of use for which the product is intended and provide for limited coverage or no coverage at all in the event of misuse of the product. A second important purpose of warranty for the manufacturer is promotion. Since buyers often infer a more reliable product when a longer warranty is offered, warranty has been used as an effective advertising tool. This is often particularly important when marketing new and innovative products, which may be viewed with a degree of uncertainty by many potential consumers. In addition, warranty has become an instrument, similar to product performance and price, used in competition with competitors.

From the consumers' point of view, warranty provides protection against lowquality products. It helps consumers minimize the financial risk of using warranted products under the normal usage conditions specified in warranty contracts. Also warranty is informative since it serves as a signal of product quality and reliability.However, the link between warranty and product quality may not always be strong since manufacturers sometimes use it so aggressively as a marketing tool such that even relative inferior products may carry a generous' warranty.

One of the basic characteristics of warranties is whether they are renewable or not. For a regular renewable policy with warranty period $w$, whenever a product fails within $w$, the buyer is compensated according to the terms of the warranty contract and the warranty policy is renewed for another period $w$. As a result, a warranty cycle $T$, starting from the date of sale, ending at the warranty expiration date, is a random variable whose value depends on $w$, the total number of failures under the warranty, and the actual failure inter-arrival times. Renewable warranties are often offered for inexpensive, non-repairable consumer electronic products such as a microwave, a coffee maker, and so forth, either implicitly or explicitly. One should note that theoretically the warranty cycle for a renewable policy could be arbitrarily large. This might be one of the reasons why such policies are not as popular as non-renewable ones for warranty issuers. The majority of warranties in the market are non-renewable for which the warranty cycle, which is the same as the warranty period, is not random, but pre-determined (fixed) since the warranty obligation will be terminated as soon as $w$ units of time passes after the sale. These types of policies are also known as fixed period warranties.

In this chapter, we discuss warranty cost models of repairable complex systems from manufacturers' point of view by considering a comprehensive set of warranty cost factors, such as warranty policies, system reliability structure, product failure mechanism, warranty service cost, impact of warranty service, value of time, warranty service time, and warranty claim related factors, under three types of existing warranty policies: free repair warranty (FRPW), free replacement warranty (FRW), and pro-rata warranty (PRW), and two new warranty policies: renewable full service warranty (RFSW) and repair-limit risk-free warranty (RLRFW), based on Bai and Pham (2004, 2005, 2006a).

A traditional way to model warranty cost for warranted multi-component systems is the black-box approach that does not utilize the information of system structure or architecture. By studying the RFSW policies with explicit consideration of four types of systems: series, parallel, series-parallel (s-p) and parallel-series ( $\mathrm{p}-\mathrm{s}$ ), this chapter demonstrates the importance of system reliability architecture information.

Previous research has studied the discounted warranty cost (DWC), a measure incorporating the value of time, for black-box systems under various warranty policies. This chapter presents models to extend the previous studies by deriving the moments of DWC for minimally repaired series systems with an FRPW or a PRW while considering both continuous and discrete time discounting. The optimal warranty reserve level and the optimal warranty duration are obtained for lot sales.

Most studies on warranties of repairable products assume perfect repair. This chapter models warranty cost for RLRFW policies given minimal repair or imperfect repair. The exact expressions of the expectation and variance of warranty cost are obtained based on truncated quasi-renewal processes and truncated nonhomogeneous Poisson processes.Due to the random nature of warranty cost factors such as product failure times, warranty cost is also a random variable whose statistical behavior can be determined by establishing mathematical links between warranty factors and warranty cost. There are many factors that may affect warranty cost, and this chapter considers the following factors:
i) Characteristics of warranty policies
ii) Warranty service cost per failure
iii) Product failure mechanism
iv) Impact of warranty service on product reliability
v) Warranty service time
vi) Warranty claim related factors

The following acronyms and notations will be used in the chapter:

| ACronyms |  |
| :-- | :-- |
| $c d f$ | Cumulative distribution function |
| CMW | Combination warranty |
| DWC | Discounted warranty cost |
| EWC | Expected warranty cost |
| FRPW | Free repair warranty |
| FRW | Free replacement warranty |
| FSW | Full service warranty |
| NHPP | Non-homogeneous Poisson process |
| $p d f$ | Probability density function |
| PM | Preventive maintenance |
| $p m f$ | Probability mass function |
| p-s | Parallel-series |
| PRW | Pro-rata warranty |
| PV | Present value |
| RCLW | Repair-cost-limit warranty |
| RFSW | Renewable full service warranty |
| RLRFW | Repair-limit risk-free warranty |
| RNLW | Repair-number-limit warranty |
| RRLRFW | Renewable repair-limit risk-free warranty |
| RTLW | Repair-time-limit warranty |
| $r . v$. | Random variables |
| s-p | Series-parallel |
| WPD | Warranty period determination |
| WRD | Warranty reserve determination |
|  |  |
| Notation |  |
| w | Length of a warranty period $(w>0)$ |
| m | Upper limit of the number of repairs under warranty |
| $N_{a}(w), N_{b}(w)$ | Number of free repairs and replacements within $w$ respectively |
| $c_{a}, c_{b}$ | unit repair and replacement cost respectively, both constant || $T_{p}, t_{p}$ | Pivot points. Capital letter indicates a r.v. |
| :--: | :--: |
| $X_{i}$ | Inter-occurrence times of a truncated quasi-renewal process |
| $F, f$ | $c d f$ and $p d f$ of the first failure time of a new product |
| $F_{i}, f_{i}$ | $c d f$ and $p d f$ of the $i^{\text {th }}$ failure time of a (truncated) quasi-renewal process |
| $\alpha$ | Parameter for a (truncated) quasi-renewal process |
| $G^{(n)}$ | $c d f$ of the $n^{\text {th }}$ occurrence time of a (truncated) quasi-renewal process |
| $C(w)$ | Warranty cost per product sold with warranty duration of $w$ |
| $M_{q}(\cdot), M_{q, 2}(\cdot)$ | First and second moments of a truncated quasi-renewal process |
| $M_{d}(\cdot), M_{d, 2}(\cdot)$ | First and second moments of a delayed renewal process |
| $N(w)$ | Number of system failures within $w$ |
| $N_{i}(w)$ | Number of failures of component $i$ within $w$ |
| $\lambda_{i}(\cdot), \Lambda_{i}(\cdot)$ | Failure intensity function and accumulative failure intensity Function of component $i$ |
| $H(\cdot)$ | Discounting function |
| $\delta$ | Discount rate |
| $C_{d_{1}}(w)$ | Discounted warranty costs per product sold under continuous discounting |
| $C_{d_{2}}(w)$ | Discounted warranty costs per product sold under discrete discounting |
| $q$ | Number of components in a system |
| $c_{i}$ | Repair cost per failure of component $i$ |
| $S_{i j}$ | $j^{\text {th }}$ failure time of component $i$ |
| L | Size of a single lot sale |
| $T C_{w r}$ | Required warranty reserve level for a single lot sale |
| $c_{0}$ | Warranty budget level, a predetermined constant |
| $\Theta$ | Set of warranty parameters, $\Theta=\left\{\theta_{i}, \theta 2, \cdots, \theta_{n}\right\}$ |
| $\Psi(\Theta)$ | A warranty policy with parameters in $\Theta$ |
| $B$ | Consumer base of a product with warranty |
| $D$ | Demand of the product sold with warranty |
| $T$ | Length of a warranty cycle |
| $\pi$ | Total profit of the producer |
| $U(\cdot)$ | Utility function of the producer |
| $\Delta P$ | Profit per product not accounting for the warranty cost |
| $p_{c}$ | Probability of accepting a product with warranty |
| $N_{a}$ | Number of renewals of an RRLRFW |
| $N_{b}$ | Number of minimal repairs under an RRLRFW || $N_{b}^{\prime}$ | Number of minimal repairs in the last warranty period of an RRLRFW |
| :--: | :--: |
| $c_{f}$ | Fixed warranty cost per warranty service, a constant |
| $\lambda(\cdot), \Lambda(\cdot)$ | Failure rate function and cumulative failure rate function in RRLRFW respectively |
| $S_{i}$ | Occurrence times of an NHPP or a truncated quasi-renewal process |
| $R_{0}$ | Warranty budget level |
| $\varepsilon$ | Acceptance level of a producer towards the risk that the total warranty cost is over the warranty budget level |
| $G_{i}, g_{i}$ | $c d f$ and $p d f$ of the $i^{\text {th }}$ occurrence time of an NHPP respectively |
| C | Warranty cost per product sold |
| TC | Total warranty cost of the producer |

# 10.1 RFSW Policies for Multi-component Systems 

In this section, we discuss a new warranty model, namely renewable full-service warranty (RFSW), for repairable multi-component systems, following Bai and Pham (2006a). Under the RFSW policy, if a warranted product fails, the failed component(s) or subsystem(s) that cause the system failure will be replaced; besides, a preventive maintenance (PM) action will be carried out to reduce the chance of future failure. Both consumers and manufacturers will benefit from the policy because consumers will receive better warranty service compared to the traditional free repair policy. As to manufacturers, it may boost sales as well as reduce the overall warranty cost as a result of better warranty service.

### 10.1.1 Background

Many researchers have incorporated PM actions in designing and analyzing product warranties. Among them, Chun (1992) considers periodic PM actions during the warranty period. Jack and Dagunar (1994) generalize Chun's idea by allowing unequal PM intervals. Yeh (2001) further extends the work by considering the degree of maintenance as a decision variable. The RFSW policy in this chapter is different from others in two aspects: (a) the PM action will only take place when a system failure happens within the warranty coverage while others consider the case that maintenance actions are not necessarily failure-dependent; (b) the warranty policy considered in this chapter is renewable.

Warranty service cost per product failure, which includes diagnosis cost, repair or replacement cost, labor cost, and possible PM cost, is often assumed to be constant. In particular, most warranty cost models in the literature use an aggregated cost parameter, which may be estimated from historical data, to approximate the true warranty service cost per failure. However, for a reparable multi-component product, the constant cost assumption may not hold since in general the system repair cost is random due to the randomness in the combination of failed components upon a system failure. To incorporate the randomness, thissection decomposes the warranty service cost into two parts: replacement/repair cost and system PM cost. System PM cost is assumed to be constant, which may be interpreted as the aggregated average cost per PM action. However, the replacement/repair cost per system failure is considered as a random variable, whose value depends on component level replacement cost and system failure mechanism.

A simple way to model system warranty cost of multi-component systems is the so-called black-box approach which ignores system reliability structure. As a result, warranty cost models for single-component products can be applied directly. The disadvantage of black-box approach lies in the fact that it does not utilize the information on system structure. Therefore, the resulting warranty cost models should be only used as an approximation.

Warranty analysis of complex systems is relatively new and there are few systematic and explicit analyses on warranty policies for complex systems. Ritchken (1986) models warranty of a two-component parallel system under a twodimensional warranty. Hussain and Murthy (1998) also discuss warranty cost estimation for parallel systems under the setting that uncertain quality of new products may be a concern for the design of warranty programs. Balachandran et al. (1981) use Markovian approach to model warranty cost for a three-component system. Chukova and Dimtrov (1996) provide several warranty cost models for simple series systems and parallel systems under a free replacement warranty based on renewal theory, but only the expected warranty cost is addressed there.

This section discusses the RFSW policy for complex systems: series, parallel, s-p, and p-s. Section 10.1.2 addresses model considerations and assumptions. Section 10.1.3 presents a warranty cost model for series systems. In Section 10.1.4 we analyze warranty cost per system sold for parallel systems. Sections 10.1.5 and 10.1.6 generalize the ideas for simple series and parallel systems and present warranty cost analysis for complex systems with p-s and s-p structure. A numerical example is given in Section 10.1.7.

# 10.1.2 Model Details 

This section provides model descriptions, assumptions, and some preliminary results.

### 10.1.2.1 RFSW Policy

The warranty policy under study is a RFSW with a pre-specified warranty period denoted by $w$. For systems under such a warranty, upon a system failure, manufacturers are responsible for replacing the failed component(s) or subsystem(s) that cause the failure. After the repair, a PM action will be performed to ensure that the system is in good working condition. Due to the renewable nature of the warranty, the restored system will automatically carry the same warranty as for the original one. For example, in Figure 10.1, $t_{1}$ is the first system failure time. Since $t_{1}<w$, the system will receive the warranty service free of charge to consumers, but it will cost the manufacturer $C_{1}$, a random variable in nature, which is composed of two parts: the replacement cost for the failed

Figure 10.1. Warranty service cost per failure and system failure times
component(s) or subsystem(s), and the system maintenance cost. Starting from $t_{1}$, the restored system will have the same warranty with duration $w$ again.

Let's define the warranty cycle $T$ as follows: $T$ is a time interval starting from the date of sale, ending at the warranty expiration date. It is obvious that for a nonrenewable warranty, a warranty cycle coincides with a warranty period $w$. However, for a renewable policy, $T$ is a random variable whose value depends on $w$, the total number of system failures under the warranty and the actual failure inter-arrival times. Denote $N_{s}(w)$ as the total number of system failures under the RFSW, and let $t_{1}, t_{2}, \ldots, t_{N_{s}(w)}$ be the corresponding inter-arrival failure times, then $T$ can be expressed as

$$
T=t_{1}+t_{2}+\ldots+t_{N_{s}(w)}
$$

For the example exhibited in Figure 10.1, $T=t_{1}+w$ since the inter-arrival time of the second system failure is $t_{2}-t_{1}$, which is longer than $w$, therefore, the warranty expires exactly at the time point $t_{1}+w$.

# 10.1.2.2 Assumptions 

In this section, we assume perfect PM such that after each warranty service, the restored system is as good as new. The corresponding maintenance cost, denoted by CM, is assumed to be constant, which may be interpreted as the aggregated average cost per PM action. Assume that the maintenance cost is a random variable. Note that this assumption may make the computation of higher moments of warranty cost analytically intractable unless other assumptions such as statistical independence, which is not realistic, are adopted. It is also assumed that all warranty claims are valid, all system failures under warranty are claimed, and any warranty service is instant.

As mentioned before, systems under consideration could be series, parallel, s-p, and p-s. For the p-s system, it is also assumed that no other working components in a failed subsystem (in series) can fail before a system failure. As to the s-p system, it is supposed that only the failed subsystem (in parallel) that causes a system failure is replaced, and thus they are as good as new upon replacement. For all the systems under study, we assume that their components are statistically independent.# 10.1.2.3 Distribution of $N_{x}$ 

For a system under the RFSW policy, to derive the statistical properties of warranty cost per cycle or per product sold, it is necessary to obtain the distribution of $N_{x}$, the number of system failures within $T$. The following lemma gives the probability mass function ( $p m f$ ) of $N_{x}$.

Lemma 10.1 Under the perfect PM assumption, for a system under the RFSW policy with parameter $w$, the pmf of $N_{x}$ is

$$
P\left[N_{x}=n_{x}\right]=\left[F_{x}(w)\right]^{n_{x}} R_{x}(w) \quad \forall n_{x}, n_{x}=0,1,2, \ldots
$$

where $F_{x}(\cdot)$ is the cumulative distribution function (cdf) of the system failure times under the warranty, which is assumed to be known, and $R_{x}(\cdot)$ is the system reliability function.

Proof. Let $t_{1}, t_{2}, \ldots$, be the subsequent system failure times within $T$, i.i.d., and follow the distribution $F_{x}$. It's easy to see that for $i \in\{1,2, \ldots\}$,

$$
N_{x}=\min \left\{i: t_{i}>w\right\}-1
$$

Therefore $\forall n_{x}, n_{x}=0,1,2, \ldots$,

$$
\begin{aligned}
& \mathrm{P}\left[N_{x} \geq n_{x}\right]=\mathrm{P}\left[\min \left\{i: t_{i}>w\right\} \geq n_{x}+1\right] \\
& =\mathrm{P}\left[\bigcup_{i \leq n_{x}} t_{i} \leq w\right)] \\
& =\prod_{i=1}^{n_{x}} P\left[t_{i} \leq w\right] \\
& =\left[F_{x}(w)\right]^{n_{x}}
\end{aligned}
$$

Hence

$$
\begin{aligned}
P\left[N_{x}=n_{x}\right] & =P\left[N_{x} \geq n_{x}\right]-P\left[N_{x} \geq n_{x}+1\right] \\
& =\left[F_{x}(w)\right]^{n_{x}}-\left[F_{x}(w)\right]^{n_{x}+1} \\
& =\left[F_{x}(w)\right]^{n_{x}} \cdot R_{x}(w)
\end{aligned}
$$

Note that although the result in Lemma 10.1 coincides with the well-known result for renewable free replacement warranty, it is necessary to provide a formal mathematical proof. Intuitively, for any systems under the RFSW, $N_{x}$ being geometrically distributed is simply because the warranty will not terminate until the original system or a restored system survive a period of $w$ for the first time and it is assumed that after each warranty service the system is as good as new.

### 10.1.3 RFSW for Series Systems

This section will discusses the distribution, the first and second centered moments of the warranty cost per cycle for series systems under the RFSW policy.

Figure 10.2. $q$-Component series system
Define $\Omega \equiv\{1,2, \ldots, q\}$, and let $F_{i}(\cdot)$ and $R_{i}(\cdot)$ be the $c d f$ and the reliability function of the failure times of component $i, i \in \Omega$, respectively, then for the series system shown in Figure 10.2, the system reliability function is given by

$$
F_{s}(w)=1-R_{s}(w)=1-\prod_{i=1}^{q}\left[1-F_{i}(w)\right]=1-\prod_{i=1}^{q} R_{i}(w)
$$

Denote $N_{i}$ be the number of failures within $T$ for component $i$ in the series system. Let $T C$ be the system warranty cost per cycle, then $T C$ can be formulated as

$$
T C=\sum_{i=1}^{q}\left(c_{i}+c_{m}\right) N_{i}
$$

Equation (10.2) shows that the distribution of $T C$ can be determined as long as one knows the joint distribution of $N_{1,} N_{2}, \ldots, N_{q}$. To derive the joint distribution, we first define two quantities and present some useful properties.

LEMMA 10.2. Define $p_{i}(w) \equiv \mathrm{P}\left[T_{i} \leq Y, T_{i} \leq w\right]$ and $\alpha_{i}(w) \equiv p_{i}(w) / F_{s}(w)$, where $T_{i}$ is a failure time of component $i, Y=\min \left(T_{j}, \forall j, j \in \Omega, j \neq i\right)$, then

$$
\begin{aligned}
p_{i}(w) & =\int_{0}^{w} \frac{h_{i}(t)}{h_{s}(t)} f_{s}(t) d t \\
\sum_{i=1}^{q} p_{i}(w) & =F_{s}(w) \\
\alpha_{i}(w) & =\frac{1}{F_{s}(w)} \int_{0}^{w} \frac{h_{i}(t)}{h_{s}(t)} f_{s}(t) d t \\
\sum_{i=1}^{q} \alpha_{i}(w) & =1
\end{aligned}
$$

where subscript $s$ represents the system, subscripts $i$ or $j$ represents a component in the system, while $h(\cdot)$ and $f(\cdot)$ are the hazard rate function and the probability density function (pdf) respectively.

Proof. From the definition of $p_{i}(w)$, we have

$$
p_{i}(w)=\int_{0}^{\infty} \mathrm{P}\left[T_{i} \leq Y, T_{i} \leq w \mid T_{i}=t\right] d F_{i}(t)
$$$$
\begin{aligned}
& =\int_{0}^{\infty} \mathrm{P}[Y \geq t] d F_{i}(t) \quad \text { (since } Y \text { and } T_{i} \text { are independent) } \\
& =\int_{0}^{\infty} \mathrm{P}\left[\min \left(T_{j}, \forall j, j \in \Omega, j \neq i\right) \geq i\right) \geq t] d F_{i}(t) \\
& =\int_{0}^{\infty} \prod_{j \in \Omega, j \neq i} \mathrm{P}\left[T_{j} \geq t\right] d F_{i}(t) \\
& =\int_{0}^{\infty} R_{s}(t) \frac{f_{i}(t)}{R_{i}(t)} d t \quad\left(\text { since } R_{s}(t)=\prod_{i=1}^{q} R_{i}(t) \quad \text { and } h(t)=\frac{f(t)}{R(t)}\right) \\
& =\int_{0}^{\infty} \frac{h_{i}(t)}{h_{s}(t)} f_{s}(t) d t
\end{aligned}
$$

To prove Equation (10.4), use $\sum_{j=1}^{q} h_{i}(t)=h_{s}(t)$, and then the result then follows. The proof of Equations (10.5) and (10.6) is straightforward.

Remarks. $p_{i}(w)$ can be interpreted as the probability that component $i$ in a series system causes a system failure before the end of a warranty period $w$. Similarly, $\alpha_{i}$ can be interpreted as the conditional probability that a failure of component $i$ is the cause of a series system failure given that the system fails within $w$. Interestingly, $p_{i}(w)$ is also the partial expectation up to time $w$ of $\zeta_{i}(t)$, denoted as $E_{T_{i}}\left[\zeta_{i}(t), w\right]$, with regard to the system failure time $T_{s}$, where $\zeta_{i}(t) \equiv h_{i}(t) / h_{s}(t)$. Depending on $\zeta_{i}(t)$ and $F_{s}(t), p_{i}(w)$ or $\alpha_{i}(w)$ may have to be obtained numerically. It should be noted that if the hazard rate functions of components in series are proportional (proportional-hazard-in-series), i.e., $h_{i}(t)=\lambda_{i} g(t), \forall i, i \in \Omega$, where $g(\cdot)$ is a positive function, then we have $\alpha_{i}(w)=\lambda_{i} / \sum_{j=1}^{q} \lambda_{j}$, a constant, not depending on $w$. As a result, probability $p_{i}(w)=F_{s}(w) \lambda_{i} / \sum_{j=1}^{q} \lambda_{j}$.

LEMMA 10.3 The conditional joint distribution of $N_{1}, N_{2}, \ldots, N_{q}$, given $N_{s}=n_{s}$, is

$$
P\left(N_{1}=n_{1}, N_{2}=n_{2}, \ldots, N_{q}=n_{q} \mid N_{s}=n_{s}\right)=\binom{n_{s}}{n_{1}, n_{2}, \ldots, n_{q}} \prod_{i=1}^{q}\left[\alpha_{i}(w)\right]^{n_{i}}
$$

The joint distribution of $N_{1}, N_{2}, \ldots, N_{q}$ is given by

$$
\mathrm{P}\left(N_{1}=n_{1}, N_{2}=n_{2}, \ldots, N_{q}=n_{q}\right)=R_{s}(w)\binom{n_{s}}{n_{1}, n_{2}, \ldots, n_{q}} \prod_{i=1}^{q}\left[p_{i}(w)\right]^{n_{i}}
$$

where $\sum_{i=1}^{q} n_{i}=n_{s}$ and $n_{i} \in\left\{0,1, \ldots, n_{s}\right\}, \forall i, i \in \Omega$.Proof. Given $N_{s}=n_{s}$, we know that there are exactly $n_{s}$ system failures (i.i.d..) before the end of $T$, which implies that the failure times of all such failures are within a period of length $w$. Hence for each of these system failures, the probability that it is caused by component $i$ is simply $\alpha_{i}(w)$ according to its definition. As a result, the conditional joint distribution of $N_{1}, N_{2}, \ldots, N_{q}$, given $N_{s}=n_{s}$, is multinomial with parameters $n_{s}, \alpha_{1}(w), \alpha_{2}(w), \ldots$, and $\alpha_{q-1}(w)$. Unconditioning on $N_{s}$ and using $N_{s} \sim$ geometric $\left[F_{s}(w)\right]$, we then have

$$
\begin{aligned}
P\left(N_{1}=n_{1}, N_{2}=n_{2}, \ldots, N_{q}=n_{q}\right) & =\left(F_{s}(w)\right)^{n_{i}} R_{s}(w)\left(\sum_{i=1}^{q} n_{i}\right) \prod_{i=1}^{q}\left(\frac{p_{i}(w)}{F_{s}(w)}\right)^{n_{i}} \\
& =\left(\sum_{i=1}^{q} n_{i}\right) \prod_{i=1}^{q}\left[p_{i}(w)\right]^{n_{i}} R_{s}(w)
\end{aligned}
$$

We are now ready to derive the distribution of $N_{i}$.

Proposition 10.1 $N_{i}$ follows a geometric distribution with parameter $R_{s}(w) /\left[R_{s}(w)+p_{i}(w)\right], \forall i, i \in \Omega$. . The corresponding pmf is

$$
P\left[N_{i}=n_{i}\right]=\left[\frac{p_{i}(w)}{R_{s}(w)+p_{i}(w)}\right]^{n_{i}} \frac{R_{s}(w)}{R_{s}(w)+p_{i}(w)}, n_{i}=0,1,2, \ldots
$$

The covariance, $\operatorname{COV}\left(N_{i}, N_{j}\right), i, j \in \Omega, i \neq j$, is given by

$$
\operatorname{COV}\left(N_{i}, N_{j}\right)=\frac{p_{i}(w) p_{j}(w)}{R_{s}^{2}(w)}
$$

Proof. First we prove Equation (10.7). From Lemma 10.3 and the properties of multinomial distribution, we have that $\forall i, i \in \Omega, N_{i} \mid N \sim \operatorname{Binomial}\left(N, \alpha_{i}(w)\right)$. So the moment generating function ( $m g f$ ) of $N_{i}$ is

$$
E\left[e^{i N_{i}}\right]=E\left[E\left[e^{i N_{i}} \mid N\right]\right]
$$

Bai and Pham (2006a) prove that

$$
E\left[e^{i N_{i}}\right]=\frac{\frac{R_{s}(w)}{R_{s}(w)+p_{i}(w)}}{1-\frac{p_{i}(w)}{R_{s}(w)+p_{i}(w)} e^{i}}
$$By realizing that the last expression is nothing but the $m g f$ of a geometric distribution with parameter $R_{s}(w) /\left[R_{s}(w)+p_{i}(w)\right]$, we complete the proof for Equation (10.7).

Now we prove (10.8). Since $\operatorname{COV}\left(N_{i}, N_{j}\right)=E\left(N_{i} N_{j}\right)-E\left(N_{i}\right) E\left(N_{j}\right)$, and by the properties of the geometric distribution, $E\left(N_{i}\right) E\left(N_{j}\right)=p_{i}(w) p_{j}(w) / R_{s}^{2}(w)$ it is sufficient to show that $E\left(N_{i} N_{j}\right)=2 p_{i}(w) p_{j}(w) / R_{s}^{2}(w)$. For $q \geq 3$, Define $N_{k}$ as the number of system failures within $T$ due to the components other than $i$ or $j$, then by the properties of multinomial distribution and from Lemma 10.3, for $N_{i}$ and $N_{j}$, denote $P\left[N_{i}=n_{i}, N_{j}=n_{j}\right]$ by $P\left[n_{i}, n_{j}\right]$, we obtain

$$
\begin{aligned}
p\left[n_{i}, n_{j}\right]= & \sum_{n_{k}=0}^{\infty} P\left(N_{i}=n_{i}, N_{j}=n_{j}, N_{k}=n_{k} \mid N_{s}=n_{i}+n_{j}+n_{k}\right) \\
& \cdot\left(F_{s}(w)\right)^{n_{i}+n_{j}+n_{k}} R_{s}(w) \\
= & \sum_{n_{k}=0}^{\infty}\binom{n_{i}+n_{j}+n_{k}}{n_{i}, n_{j}, n_{k}}\left[\alpha_{i}(w)\right]^{n_{i}}\left[\alpha_{j}(w)\right]^{n_{j}}\left[\alpha_{k}(w)\right]^{n_{k}}\left[F_{s}(w)\right]^{n_{i}+n_{j}+n_{k}} R_{s}(w) \\
= & \binom{n_{i}+n_{j}}{n_{i}}\left[\frac{p_{i}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)}\right]^{n_{i}}\left[\frac{p_{j}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)}\right]^{n_{j}} \\
& \cdot \frac{R_{s}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)}
\end{aligned}
$$

where the last step is due to

$$
\sum_{n_{k}=0}^{\infty}\binom{n_{i}+n_{j}+n_{k}}{n_{i}, n_{j}, n_{k}} x^{n_{k}}=\binom{n_{i}+n_{j}}{n_{i}}(1-x)^{-\left(n_{i}+n_{j}+1\right)}, \quad \forall x, x \in(0,1)
$$

and $1-p_{k}(w)=R_{s}(w)+p_{i}(w)+p_{j}(w)$.
Bai and Pham (2004) obtain that

$$
\begin{aligned}
& E\left(N_{i} N_{j}\right)=\sum_{n_{i}=0}^{\infty} \sum_{n_{j}=0}^{\infty}\binom{n_{i}+n_{j}}{n_{i}}\left[\frac{p_{i}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)}\right]^{n_{i}} \\
& \cdot\left[\frac{p_{j}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)}\right]^{n_{j}} \cdot \frac{R_{s}(w)}{R_{s}(w)+p_{i}(w)+p_{j}(w)} \\
& =\frac{2 p_{i}(w) p_{j}(w)}{\left(R_{s}(w)\right)^{2}}
\end{aligned}
$$

The proof of Equation (10.8) for $q=2$ is similar, and is omitted here.
Applying Proposition 10.1 to Equation (10.2), we can then conclude that for aseries system under the RFSW policy, the distribution of $T C$ is simply a mixture of dependent random variables each of which follows a geometric distribution. The pmf of $T C$ may be written as

$$
P[T C=x]=\left\{\begin{array}{l}
R_{s}(w) \sum_{\left[n, n_{2}, \ldots, n_{q}\right] \in \sum_{i=1}^{q}\left(c_{i}+c_{m}\right) n_{i}=x}\binom{\sum_{i=1}^{q} n_{i}}{n_{i} n_{2}, \ldots n_{q}} \prod_{i=1}^{q}\left(p_{i}(w)\right)^{n_{i}} \\
\text { if } x \in\left\{\sum_{i=1}^{q}\left(c_{i}+c_{m}\right) n_{i}\right\} \text {, and } n_{i} \in\{0,1, \ldots\}, \forall i, i \in \Omega \\
0 \quad \text { otherwise }
\end{array}\right.
$$

COROLLARY 10.1 The expected warranty cost per cycle for the q-component series system under the RFSW policy is given by

$$
E[T C]=\frac{1}{R_{s}(w)} \sum_{i=1}^{q}\left(c_{i}+c_{m}\right) p_{i}(w)
$$

The corresponding variance of TC is

$$
\begin{aligned}
\operatorname{Var}[T C] & =\frac{1}{\left[R_{s}(w)\right]^{2}}\left\{\sum_{i=1}^{q}\left(c_{i}+c_{m}\right)^{2} p_{i}(w)\left[p_{i}(w)+R_{s}(w)\right]\right. \\
& \left.+2 \sum_{i<j, i, j \in \Omega}\left(c_{i}+c_{m}\right)\left(c_{j}+c_{m}\right) p_{i}(w) p_{j}(w)\right\}
\end{aligned}
$$

where $c_{i}$ is the replacement cost of component $i$, and $c_{m}$ is the system PM cost.
Proof. From Equation (10.2), it follows that

$$
\begin{gathered}
E[T C]=\sum_{i=1}^{q}\left(c_{i}+c_{m}\right) E\left[N_{i}\right] \text { and } \\
\operatorname{Var}[T C]=\sum_{i=1}^{q}\left(c_{i}+c_{m}\right)^{2} \operatorname{Var}\left(N_{i}\right)+2 \sum_{i<j, i, j \in \Omega}\left(c_{i}+c_{m}\right)\left(c_{i}+c_{m}\right) \operatorname{cov}\left(N_{i}, N_{j}\right)
\end{gathered}
$$

By Proposition 10.1 and the properties of the geometric distribution, the results follow.

# 10.1.4 RFSW for Parallel Systems 

For a parallel system, it won't fail unless all the components in the system fail. As a result, under the RFSW policy, the warranty service cost per system failure for the system shown in Figure 10.3 is simply $C_{m}+\sum_{i=1}^{q} c_{i}$. Again let $N_{s}$ be the number of system failures within $T$, then the corresponding system warranty cost $T C$ per system sold is

$$
T C=N_{s}\left(c_{m}+\sum_{i=1}^{q} c_{i}\right)
$$

Figure 10.3. $q$-Component parallel system
Not surprisingly, $N_{s}$ again follows a geometric distribution, but $F_{s}(w)$ is the failure time $c d f$ of the parallel system evaluated at $w$, which is given by

$$
F_{s}(w)=\prod_{i=1}^{q} F_{i}(w)
$$

COROLLARY 10.2 Under the RFSW policy, the pmf of the system warranty cost per cycle is

$$
P[T C=x]= \begin{cases}F_{s}(w))^{n_{s}}\left(1-F_{s}(w)\right), & \text { if } x \in\left\{\left(c_{m}+\sum_{i=1}^{q} c_{i}\right) n_{s}\right\} ; n_{s} \in\{0,1, \ldots\} \\ 0, & \text { otherwise }\end{cases}
$$

The expected system warranty cost is

$$
E[T C]=\frac{F_{s}(w)}{R_{s}(w)}\left(c_{m}+\sum_{i=1}^{q} c_{i}\right)
$$

The corresponding warranty cost variance is

$$
\operatorname{Var}[T C]=\frac{F_{s}(w)}{R^{2}{ }_{s}(w)}\left(c_{m}+\sum_{i=1}^{q} c_{i}\right)^{2}
$$

# 10.1.5 RFSW for Series-parallel Systems 

This section discusses the RFSW policy for s-p systems. For the s-p system composed of $q$ subsystems in series drawn in Figure 10.4, denote the number of components in subsystem $i$ that are in parallel as $r_{i}$. Let $C_{i}$ be the warranty service cost for subsystem $i$, and let $c_{i j}$ be the replacement cost of component $j$ in subsystem $i$; then we have $C_{i}=c_{m}+\sum_{j=1}^{r_{i}} c_{i j}, \forall i, i \in \Omega$. .

For the s-p system, denote $N_{i}$ as the number of failures of subsystem $i$ within T. Similar to Equation (10.2), the total system warranty cost per cycle can be formulated as$$
T C=\sum_{i=1}^{q} N_{i}\left(c_{m}+\sum_{j=1}^{n} c_{i j}\right)
$$



Figure 10.4. s-p System with $q$ subsystems
The $c d f$ of failure times of the s-p system under the warranty is given by

$$
\begin{aligned}
F_{s}(w) & =1-\prod_{i=1}^{q} R_{i}(w) \\
& =1-\prod_{i=1}^{q}\left[1-\prod_{j=1}^{n_{i}} F_{i j}(w)\right]
\end{aligned}
$$

where $F_{i j}(\cdot)$ is the $c d f$ of the failure times of component $j$ in subsystem $i$.
Under the RFSW policy, we define $p_{i}(w)$ and $\alpha_{i}(w)$ the same way as that for simple series systems except that in this case, $i$ refers to a subsystem instead of a single component. It is obvious that all the properties of $p_{i}(w)$ and $\alpha_{i}(w)$ in Lemma 10.2 still hold.

Corollary 10.3 For the s-p system under the RFSW policy, the pmf of the warranty cost per cycle TC is

$$
P[T C=x]=\left\{\begin{array}{l}
R_{s}(w) \sum_{\left\{n, n_{2}, \ldots n_{q}\right\}_{i} \triangleq \sum_{i=1}^{q}\left(c_{m}+\sum_{j=1}^{n_{i}} c_{i j}\right) n_{i}=x}\binom{\sum_{i=1}^{q} n_{i}}{n, n_{2}, \ldots n_{q}} \prod_{i=1}^{q}\left[p_{i}(w)\right]^{n_{i}} \\
\text { if } x \in\left\{\sum_{i=1}^{q}\left(c_{m}+\sum_{j=1}^{n_{i}} c_{i j}\right) n_{i}\right\} \text { and } n_{i} \in\{0,1, \ldots\}, \forall i, i \in \Omega \\
0 \quad \text { otherwise }
\end{array}\right.
$$The first two centered moments of the warranty cost per cycle TC are as follows:

$$
\begin{aligned}
E[T C]= & \frac{1}{R_{s}(w)} \sum_{i=1}^{q}\left(c_{m}+\sum_{j=1}^{c} c_{i j}\right) p_{i}(w) \\
\operatorname{Var}[T C]= & \sum_{i=1}^{q}\left(c_{m}+\sum_{j=1}^{c} c_{i j}\right)^{2} \frac{p_{i}(w)\left[p_{i}(w)+R_{s}(w)\right]}{R_{s}^{2}(w)} \\
& +2 \sum_{i<\ell, t, \ell \in \Omega}\left(c_{m}+\sum_{j=1}^{c} c_{i j}\right)\left(c_{m}+\sum_{j=1}^{c} c_{\ell j}\right) \frac{p_{i}(w) p_{\ell}(w)}{R_{s}^{2}(w)}
\end{aligned}
$$

Proof. The proof is similar to that for Corollary 10.1.

# 10.1.6 RFSW for Parallel-series Systems 

Consider the system shown in Figure 10.5 with $q$ subsystems in parallel, each of which consists of one or more components in series.


Figure 10.5. p-s System with $q$ subsystems

In this section, we study the RFSW policies for p-s systems. The first twocentered warranty cost moments will be derived. Let $r_{i}$ be the number of components in the $i^{\text {th }}$ subsystem and let $N_{s}$ be the number of system failures within $T$. Under the perfect PM assumption, again we have that $N_{s} \sim$ geometric $\left(F_{s}(w)\right)$. It's not difficult to verify that for the p-s system,

$$
F_{s}(w)=\prod_{i=1}^{q}\left[1-\prod_{j=1}^{c}\left[1-F_{i j}(w)\right]\right]
$$Let $N_{i j}$ be the number of failures of the $j^{\text {th }}$ component in subsystem $i$ within $T$. Since each subsystem is in series, all subsystems are connected in parallel and it is assumed that no working components in a failed subsystem can fail before a system failure, we have that $\sum_{j=1}^{r_{i}} N_{i j}=N_{s}, \forall i, i=1,2, \ldots, q$. Denote $c_{i j}$ as the replacement cost for component $j$ in subsystem $i$, then the total system warranty cost per cycle, $T C$, can be written as

$$
T C=\sum_{i=1}^{q} \sum_{j=1}^{c_{i j}}\left(c_{i j}+\frac{c_{s s}}{q}\right) N_{i j}
$$

To derive the expectation and the variance of $T C$ for p-s systems, we need to obtain the distribution of $N_{i j}, \forall i, i \in \Omega, \forall j, j \in \Omega_{i}, \Omega_{i} \equiv\left\{1,2, \ldots, r_{i}\right\}$, as well as the covariance between $N_{i j}$ and $N_{i k}$ for $j \neq k$ (covariance within a subsystem), and the covariance between $N_{i j}$ and $N_{i^{\prime} k}$ for $i \neq i^{\prime}$ (covariance between subsystems). Similar to $p_{i}(w)$ and $\alpha_{i}(w)$ defined in Section 10.1.3, next we define $p_{i j}(w)$ and $\alpha_{i j}(w)$ and state the related properties in the following lemma.

LEMMA 10.4 For the p-s system under the RFSW policy, let $T_{i j}$ be the failure times of component $j$ in subsystem $i$, define $p_{i j}(w) \equiv P\left[T_{i j} \leq Y_{i}, T_{i j} \leq w, T_{s} \leq w\right]$ and $\alpha_{i j}(w) \equiv p_{i j}(w) / F_{s}(w)$, where $Y_{i}=\min \left(T_{i k}, \forall k, k \in \Omega_{i}, k \neq j\right)$, then

$$
\begin{aligned}
& p_{i j}(w)=F_{s}^{\bar{i}}(w) \int_{0}^{w} \frac{h_{i j}(t)}{h_{i}(t)} f_{i}(t) d t \\
& \sum_{j=1}^{s} p_{i j}(w)=F_{s}(w) \\
& \alpha_{i j}(w)=\frac{1}{F_{i}(w)} \int_{0}^{w} \frac{h_{i j}(t)}{h_{i}(t)} f_{i}(t) d t \\
& \sum_{j=1}^{s} \alpha_{i j}(w)=1
\end{aligned}
$$

where $\bar{i}$ represents the new p-s system comprising $(q-1)$ subsystems of the original system except the subsystem $i$.

Proof. From the definition of $p_{i j}(w)$, we obtain

$$
\begin{aligned}
p_{i j}(w) & =\mathrm{P}\left[Y_{i} \geq T_{i j}, T_{i j} \leq w, T_{s}^{\bar{i}} \leq w\right] \quad \text { (since all components are independent) } \\
& =\mathrm{P}\left[Y_{i} \geq T_{i j}, T_{i j} \leq w\right] F_{s}^{\bar{i}}(w) \\
& =F_{s}^{\bar{i}}(w) \int_{0}^{w} P\left[\min \left(T_{i k}, \forall k, k \in \Omega_{i}, k \neq j\right) \geq t\right] d F_{i j}(t)
\end{aligned}
$$$$
\begin{aligned}
& =F_{s}^{i}(w) \int_{0}^{w} \prod_{k \in \Omega_{i}, k \neq j} R_{i k}(t) d F_{i j}(t) \\
& =F_{s}^{i}(w) \int_{0}^{w} R_{i}(t) \frac{f_{i j}(t)}{R_{i j}(t)} d t \quad\left(\text { since } R_{i}(t)=\prod_{j=1}^{n} R_{i j}(t) \text { and } h(t)=\frac{f(t)}{R(t)}\right) \\
& =F_{s}^{i}(w) \int_{0}^{w} \frac{h_{i j}(t)}{h_{i}(t)} f_{i}(t) d t
\end{aligned}
$$

To prove Equation (10.23), use $F_{i}(t) F_{s}^{i}(t)=F_{s}(t)$ and $\sum_{j=1}^{r_{i}} h_{i j}=h_{i}$; the result then follows. The proof for Equations (10.24) and (10.25) is straightforward.

Again, as a special case, if the proportional-hazards-in-series assumption is adopted, implying that the hazard rate function of component $j$ in subsystem $i$ has the form $\lambda_{i j} g_{i}(t), \forall j, j \in \Omega_{i}$, where $g_{i}(t)$ is a positive function, then it is easy to verify that $\alpha_{i j}=\lambda_{i j} / \sum_{k=1}^{r_{i}} \lambda_{i k}$ and $p_{i j}=F_{s}(w) \lambda_{i j} / \sum_{k=1}^{r_{i}} \lambda_{i k}$

Next, we derive the distribution of $N_{i j}$ and some related properties.

Corollary 10.4 For the p-s system under the RFSW, the pmf of $N_{i j}, \forall i, i \in \Omega$, $\forall j, j \in \Omega_{i}$, is given by

$$
P\left[N_{i j}=n_{i j}\right]=\left[\frac{p_{i j}(w)}{R_{s}(w)+p_{i j}(w)}\right]^{n_{i j}} \frac{R_{s}(w)}{R_{s}(w)+p_{i j}(w)}, n_{i j}=0,1,2, \ldots
$$

The covariance between $N_{i j}, N_{i k}$ (within subsystem covariance) for $j \neq k, j, k \in \Omega_{i}$ is

$$
\operatorname{cov}\left(N_{i j}, N_{i k}\right)=\frac{p_{i j}(w) p_{i k}(w)}{R_{s}^{2}(w)}
$$

and the covariance between $N_{i j}, N_{i^{\prime} k}$ (between subsystem covariance) for $i \neq i^{\prime}, i, i^{\prime} \in \Omega$ is

$$
\operatorname{cov}\left(N_{i j}, N_{i^{\prime} k}\right)=\sum_{n_{i j}=0}^{w} \sum_{n_{i^{\prime} k}=0}^{w} n_{i j} n_{i^{\prime} k} p\left(n_{i j}, n_{i^{\prime} k}\right)-\frac{p_{i j}(w) p_{i^{\prime} k}(w)}{R_{s}(w)^{2}}
$$

where for $n_{i^{\prime} k} \geq n_{i j}$

$$
\begin{aligned}
p\left(n_{i j}, n_{i^{\prime} k}\right)= & R_{s}(w) \sum_{n_{i j} \geq n_{i^{\prime} k}-n_{i j}}^{w}\binom{n_{i j}+n_{i j}}{n_{i^{\prime} k}}\left[\alpha_{i^{\prime} k}(w)\right]^{n_{i^{\prime} k}}\left[1-\alpha_{i^{\prime} k}(w)\right]^{n_{i j}+n_{i j}-n_{i^{\prime} k}} \\
\cdot & \binom{n_{i j}+n_{i j}}{n_{i k}}\left[\alpha_{i j}(w)\right]^{n_{i j}}\left[1-\alpha_{i j}(w)\right]^{n_{i j}}\left[F_{s}(w)\right]^{n_{i j}+n_{i j}}
\end{aligned}
$$Proof. The proof for Equations (10.26) and (10.27) is similar to that for Proposition 10.1 as long as one realizes that the joint distribution of $N_{i 1}, N_{i 2}, \ldots, N_{i n}, \forall i, i \in \Omega$ is given by

$$
P\left[N_{i 1}=n_{i 1}, N_{i 2}=n_{i 2}, \ldots, N_{i n}=n_{i n}\right]=R_{s}(w)\binom{n_{i 1}+n_{i 2}+\ldots+n_{i n}}{n_{i 1}, n_{i 2}, \ldots, n_{i n}} \prod_{k=1}^{n_{i}}\left[p_{i k}(w)\right]^{n_{i k}}
$$

Next we prove (10.29). Without loss of generality, let $n_{i^{\prime} k} \geq n_{i j}$, and denote

$$
p\left(n_{i j}, n_{i j}, n_{i^{\prime} k}\right)=P\left[N_{i j}=n_{i j}, \sum_{j^{\prime} \neq j, j^{\prime}, j \in \Omega_{i}} N_{i j^{\prime}}=n_{i j}, N_{i^{\prime} k}=n_{i^{\prime} k}\right)
$$

then

$$
\begin{aligned}
p\left(n_{i j}, n_{i j}, n_{i^{\prime} k}\right) & =p\left[n_{i^{\prime} k} \mid n_{i j}, n_{i j}\right) p\left(n_{i j}, n_{i j}\right) \\
& =\binom{n_{i j}+n_{i j}}{n_{i^{\prime} k}}\left[\left(\alpha_{i^{\prime} k}(w)\right]^{n_{i^{\prime} k}}\left[1-\alpha_{i^{\prime} k}(w)\right]^{n_{i j}+n_{i j}-n_{i^{\prime} k}}\right. \\
& *\binom{n_{i j}+n_{i j}}{n_{i j}}\left(\left(\alpha_{i j}(w)\right)^{n_{i j}}\left(1-\alpha_{i j}(w)\right)^{n_{i j}}\left(F_{s}(w)\right)^{n_{i j}+n_{i j}} R_{s}(w)\right.
\end{aligned}
$$

Consequently,

$$
\begin{aligned}
p\left(n_{i j}, n_{i^{\prime} k}\right)= & \sum_{n_{i j} \geq n_{i^{\prime} k}-n_{i j}}^{\infty}\binom{n_{i j}+n_{i j}}{n_{i^{\prime} k}}\left(\alpha_{i^{\prime} k}(w)\right)^{n_{i^{\prime} k}}\left(1-\alpha_{i^{\prime} k}(w)\right)^{n_{i j}+n_{i j}-n_{i^{\prime} k}} \\
& \cdot\binom{n_{i j}+n_{i j}}{n_{i j}}\left[\left(\alpha_{i j}(w)\right]^{n_{i j}}\left[1-\alpha_{i j}(w)\right]^{n_{i j}}\left[F_{s}(w)\right]^{n_{i j}+n_{i j}} R_{s}(w)
\end{aligned}
$$

The proof of Equation (10.28) is straightforward by using Equations (10.26) and (10.29).

Corollary 10.5 For the p-s system under the RFSW policy, the expectation of the system warranty cost per cycle, TC, is given by

$$
E[T C]=\sum_{i=1}^{q} \sum_{j=1}^{c}\left(c_{i j}+\frac{c_{m}}{q}\right) \frac{p_{i j}(w)}{R_{s}(w)}
$$

and the corresponding cost variance is

$$
\begin{aligned}
\operatorname{Var}[T C] & =\sum_{i=1}^{q} \sum_{j=1}^{c}\left(c_{i j}+\frac{c_{m}}{q}\right)^{2} \frac{p_{i j}(w)\left[R_{s}(w)+p_{i j}(w)\right]}{\left(R_{s}(w)\right)^{2}} \\
& +2 \sum_{i=1}^{q} \sum_{j<k, j, k, \in \Omega_{i}}\left(c_{i j}+\frac{c_{m}}{q}\right)\left(c_{i k}+\frac{c_{m}}{q}\right) \frac{p_{i j}(w) p_{i k}(w)}{R_{s}^{2}(w)} \\
& +2 \sum_{i<i^{\prime}, i, i^{\prime} \in \Omega} \sum_{j=1}^{c} \sum_{k=1}^{c}\left(c_{i j}+\frac{c_{m}}{q}\right)\left(c_{i^{\prime} k}+\frac{c_{m}}{q}\right)\left(\sum_{n_{i j}=0}^{\infty} \sum_{n_{i^{\prime} k}=0}^{\infty} n_{i j} n_{i^{\prime} k} p\left(n_{i j}, n_{i^{\prime} k}\right)\right.
\end{aligned}
$$$$
-\frac{p_{i j}(w) p_{i^{\prime} k}(w)}{R_{s}^{2}(w)}
$$

Proof. The derivation of $\mathrm{E}[T C]$ is straightforward. To derive $\operatorname{Var}(T C)$, starting from Equation (10.21), we obtain that

$$
\begin{aligned}
\operatorname{Var}(T C) & =\sum_{i=1}^{q} \sum_{j=1}^{c}\left(c_{i j}+\frac{c_{m}}{q}\right)^{2} \operatorname{Var}\left(N_{i j}\right) \\
& +2 \sum_{i=1}^{q} \sum_{j<k}\left(c_{i j}+\frac{c_{m}}{q}\right)\left(c_{i k}+\frac{c_{m}}{q}\right) \operatorname{cov}\left(N_{i j}, N_{i k}\right) \\
& +2 \sum_{i<i^{\prime}} \sum_{j=1}^{c_{i}} \sum_{k=1}^{c_{i}}\left(c_{i j}+\frac{c_{m}}{q}\right)\left(c_{i^{\prime} k}+\frac{c_{m}}{q}\right) \operatorname{cov}\left(N_{i j}, N_{i^{\prime} k}\right)
\end{aligned}
$$

Using Corollary 10.4, the results follow.
Next let's see a numerical example, a detailed sensitivity study, and a few possible further studies for this RFPW.

# 10.1.7 A Numerical Example and Sensitivity Study 

Consider a three-component p-s system shown in Figure 10.6 under the RFSW policy. Suppose $w=3$ and $c_{m}=\$ 220$. All other parameters are given in Table 10.1. The parameters of components' failure times were chosen such that $R_{s}(t)>0.90$ for $t \leq 20$. Assume that the failure times of components 1 and 3 follow Weibull distributions, and the failure time of component 2 are exponentially distributed.


Figure 10.6. p-s System with three components

Table 10.1. Parameters for the three-component s-p system

| Component number | 1 | 2 | 3 |
| :--: | :--: | :--: | :--: |
| $c_{i}$ | $\$ 200$ | $\$ 250$ | $\$ 550$ |
| $R(t)$ | $\exp \left(-\frac{t^{0.59}}{28.33}\right)$ | $\exp \left(-\frac{1}{121.68}\right)$ | $\exp \left(-\frac{t^{0.37}}{9.16}\right)$ |From Equations (10.30) and (10.31), the expected system warranty cost E[TC ] per product sold is $\$ 13.26$, which only accounts for $1.33 \%$ of the total system production cost (the sum of all components' cost). The corresponding standard deviation $\operatorname{Std}(T C)$ is $\$ 114.99$, which is much higher than $\mathrm{E}[T C]$. However, this is what one should expect since the distribution of TC is a mixture of geometrically distributed random variables whose standard deviation is always larger than its expectation. It is worth noting that most warranty models in warranty literature rely solely on expected warranty cost for the purpose of warranty cost modeling and analysis. This example shows the necessity of obtaining higher moments of warranty cost to evaluate the risk embedded in certain warranty policies for manufacturers.


Figure 10.7. $\mathrm{E}[\mathrm{TC}]$ and $\operatorname{std}(\mathrm{TC})$


Figure 10.8. CV and system reliabilityIf one decomposes $\operatorname{Var}(T C)$ into three parts: the total variation due to each $N_{i j}$, the covariance within subsystems, and the covariance between subsystems, it seems that the first and the third parts are the dominant sources of $\operatorname{Var}(T C)$. In this example they accounts for $55.83 \%$ and $44.11 \%$ respectively.

To show how the moments of TC change while the warranty duration varies, we consider $w$ in the range of one to twenty. From Figure 10.7 one can see that both the expectation and the standard deviation of TC increase monotonically over $w$. Coefficient of Variation (CV) is a standardized measure for the variability of random variables. Figure 10.8 shows that CV declines monotonically over $w$. For $w=20, \mathrm{CV}=3.39$. We also plot the system reliability curve in Figure 10.8.

As indicated previously, expectation is probably the most commonly used measure for evaluating warranty programs. Nevertheless, expectation itself can reveal little information about the warranty cost risk for manufacturers. In contrast, prediction intervals or quantiles of TC may be a better measure to evaluate warranties. In theory, computing prediction intervals is equivalent as computing quantiles. Since usually warranty managers are more interested in controlling the upper limit of TC, the upper quantiles of TC for different $w, w \in[1,20]$ are computed at the $95 \%$ and $99 \%$ confidence level, denoted by $1-\alpha$. It is possible to obtain the exact prediction intervals directly from the pmf of TC. But working with pmf of TC involves enumeration of all possible combinations of components' cost, which could be complicated and time consuming especially for large systems. Alternatively, Monte Carlo simulation is used to obtain estimates of those quantiles. The simulation procedure is given below:
i) Generate $N_{s}$ from geometric $\left(F_{s}(w)\right)$.
ii) If $N(w)=n>0$, then for each $i$ where $i=1,2, \ldots, n$, generate uniform random variables from $p_{i j}(w)$ to determine the exact combination of failed components, else $T C=0$.
iii) Compute TC based on the combination of failed components, the corresponding component replacement cost and system maintenance cost.
iv) Repeat steps i) -iii) for each w for 40,000 runs.

The corresponding quantiles, or equivalently, the upper prediction confidence bounds are then computed from the generated data points. The results are reported in Table 10.2. Based on the results, for the manufacturers, the warranty cost per product sold would be no more than $\$ 1,020$ for $w \leq 20$, roughly the same as the production cost, with the confidence level at $99 \%$.

Section 10.1 has discussed a new warranty policy, the renewable full-service warranty, which offers extra incentive for consumers by including free PM into the traditional free repair service, for multi-component systems with series, parallel, sp and p-s structure. Due to the more than ever fierce competition in markets, manufacturers are constantly in search of innovations in marketing strategies to promote their products. We believe that the RFSW policy can be used for marketing purpose since it provides extra compensation to consumers.Table 10.2. Quantiles of TC for the p-s system

| $w$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $Q_{95}$ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $Q_{99}$ | 0 | 0 | 970 | 970 | 970 | 970 | 970 | 970 | 970 | 1020 |
| $w$ | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| $Q_{95}$ | 0 | 970 | 970 | 970 | 970 | 970 | 970 | 970 | 970 | 970 |
| $Q_{99}$ | 1020 | 1020 | 1020 | 1020 | 1020 | 1020 | 1020 | 1020 | 1020 | 1020 |

There may be several potential extensions to the study of RFSW policies on complex systems. First is to relax the perfect PM assumption. Although this assumption is used widely in practice as well as in warranty and maintenance literature, we believe that more research should be done for RFSW policies considering minimal maintenance or imperfect maintenance. Second is to consider random system maintenance cost to fully take into account of the probabilistic behavior at component level. As indicated before, such a change could bring in much more complexity and the higher moments of warranty cost in general are analytically intractable. For s-p systems, it is assumed that only the components in a failed subsystem will be replaced under the warranty, thus the analysis of warranty cost under an RFSW becomes similar to that for simple series systems. In practice, consumers would prefer to have all failed components replaced upon a warranty service.

# 10.2 DWC for Minimally Repaired Series Systems 

One of the primary questions to be answered in warranty analysis is how much a warranty program will cost. Due to the random nature of warranty cost, most warranty cost models would prefer to use the expected warranty cost (EWC) as the answer. Extensive research on modeling and estimating EWC has been done under various warranty policies, for example, in Blischke and Murthy $(1994,1996)$ and Singpurwalla and Wilson (1993).

In contrast to the EWC, the expected value of discounted warranty cost (DWC), which incorporates the value of time, may provide a better cost measure for warranties. This is because in general warranty cost can be treated as a random cash flow in the future. Warranty issuers do not have to spend all the money at the stage of warranty planning. Instead, they can allocate it over the life cycle of warranted products. Another reason that one should consider the value of time is for the purpose of determining warranty reserve. Warranty reserve is a fund set up specifically to meet future warranty claims. It is well-known that the present value (PV) of warranty liability or rebates to be paid in the future is less than the face value (Amato and Anderson 1976). Hence, for warranty issuers, it is desirable to determine the warranty reserve according to the PV of total warranty liability. DWC and warranty reserve related issues have been studied, from bothmanufacturers' and consumers' perspectives for single-component products, either repairable or non-repairable (Mamer 1969, 1987; Patankar and Mitra 1995; Thomas 1989).

In practice, most products are composed of several components. If warranties are offered for each component separately, then warranty models for singlecomponent items can be applied directly. However, sometimes warranty terms are defined upon the entire systems. For such warranties, it is necessary to consider the system architecture as well as the component level warranty service cost (Blischke and Murthy 1996, p.543). Warranty analysis for multi-component systems based on system structure has been addressed in a few papers. Ritchken (1986) studies two-component parallel system under a two-dimensional warranty. Hussain and Murthy (1998) also discuss warranty cost estimation for parallel systems under the setting that uncertain quality of new products may be a concern for the design of warranty programs. A Markovian approach to the analysis of warranty cost for a three-component system can be found in Balachandran (1981). Chukova and Dimtrov (1996) derive the expected warranty cost for two-component series systems and parallel systems under a free replacement warranty. Bai and Pham (2004) study DWC for series systems. Section 10.1 presents the first two centered moments of renewable full-service warranties for complex systems with series, parallel, series-parallel and parallel-series structure.

There are many ways of modeling the impact on system failure times from repair actions. The simplest way is by assuming the as-good-as-new repair for which a single failure time distribution is sufficient to describe subsequent failure times of a system, no matter new or repaired. The advantage of such an approach is that it simplifies warranty cost models as renewal theory can be applied readily. However, it might lead to underestimated expected warranty cost due to the fact that repaired systems are usually not as reliable as a new one. A slight modification from as-good-as-new repair is by assuming a failure time distribution for all repaired systems, different from the failure time distribution of a new one, for which a delayed renewal process can be employed to model the product failure process (Blischke and Murthy 1996). For complex product, repair is often assumed to be minimal (as-good-as-old), i.e., the failure rate of a repaired product is the same as that just before the most recent repair. Nguyen and Murthy (1984a) presents a general warranty cost model for single-component repairable items. Perfect repair, minimal repair and imperfect repair are covered, but the value of time is not addressed. Kulkarni et al. (2002) develop several warranty reserve models for single component products for non-stationary sales processes. Ja et al. (2001) present a warranty cost model on minimally repaired single-component systems with time dependent cost. One of the assumptions there is that repair costs at different times are statistically independent. Nevertheless, in the context of DWC, usually those time-dependent costs are not independent. For this reason, the assumption of independent repair costs is dropped in this section.

Another important issue in warranty analysis is the variability or the risk embedded in warranty cost for warranty issuers. It is often not sufficient for warranty managers to simply obtain the estimates of EWC or expected DWC. Additional information about higher warranty cost moments is essential for warranty risk management and decision making. Discussions on warranty costvariation for single-component or black-box systems can be seen in Ja et al. (2002), Blacer and Sahin (1986), and Patankar and Worm (1981). In this section, we will discuss the first two centered moments of DWC for minimally repaired series systems, following Bai and Pham (2004). This section assumes:
i) Components in a system are statistically independent.
ii) All repairs are instant within warranty.
iii) All components in a system are repairable and any failed components are minimally repaired upon a system failure under warranty.
iv) All warranty claims are executed and all claims are valid.

The rest of this section is organized as follows. Section 10.2.1 shows some preliminary results to be used in later sections. In Section 10.2.2, general expressions of expected DWC and its variance for a repairable series system under an FRW policy are discussed. Two special cases are also presented here. Section 10.2.3 discusses DWC of a PRW policy. Section 10.2.4 addresses two important warranty management problems.

# 10.2.1 Preliminary Results 

Let $\{N(t), t>0\}$ be a non-homogeneous Poisson process (NHPP) with intensity function $\lambda(t)$, the corresponding cumulative intensity function is $\Lambda(t)$, which is also referred as the mean value function, is given by $\Lambda(t)=\int_{s=0}^{t} \lambda(s) d s$. Let $S_{i}, i=1,2, \cdots$, be the $i^{\text {th }}$ arrival time of the NHPP. Define a random variable $Y(t)$ as follows:

$$
Y(t)= \begin{cases}\sum_{i=1}^{N(t)} H\left(S_{i}\right), & \text { if } N(t) \in\{1,2, \cdots\} \\ 0 & \text { if } N(t)=0\end{cases}
$$

where $H(\cdot)$ is a non-negative bounded continuous function, then we have the following results:

## Proposition 10.2

$$
\begin{aligned}
& E[Y(t)]=\Lambda(t) E[H(U)]=\int_{0}^{t} H(u) \lambda(u) d u \\
& V[Y(t)]=\Lambda(t) E\left[H^{2}(U)\right]=\int_{0}^{t} H^{2}(u) \lambda(u) d u
\end{aligned}
$$

where the pdf of $U$ is given by $f_{U}(u)=\frac{\lambda(u)}{\Lambda(t)}, 0 \leq u \leq t$.
Proof. Define $\vec{S} \equiv\left(S_{1}, S_{2}, \cdots, S_{n}\right)$. Let $\vec{U} \equiv\left(U_{(1)}, U_{(2)}, \cdots, U_{(n)}\right)$, where $U_{(i)}$ 's are the order statistics of $U_{1}, U_{2}, \cdots, U_{n}$, which are i.i.d.. samples of the randomvariable $U$. Conditioning on $N(t)=n$, we have that $\vec{S}$ is equal in distribution of $\vec{U}$ (Kulkarni 1995, p.228). Hence

$$
\begin{aligned}
E[Y(t)] & =E\left\{E\left[\sum_{i=1}^{N(t)} H\left(S_{i}\right) \mid N(t)=n\right]\right\} \\
& =E\left\{E\left[\sum_{i=1}^{n} H\left(U_{(i)}\right)\right]\right\} & & (\text { since distribution }(\vec{U})=\text { distribution }(\vec{S})) \\
& =E\left\{E\left[\sum_{i=1}^{n} H\left(U_{i}\right)\right]\right\} & & \left(\text { for } \sum_{i=1}^{n} H\left(U_{i}\right)=\sum_{i=1}^{n} H\left(U_{(i)}\right)\right) \\
& =E[n E[H(U)]\} & & \\
& =\Lambda(t) E[H(U)] . & & (\operatorname{since} E[N(t)]=\Lambda(t)) \\
& =\int_{0}^{t} H(u) \lambda(u) d u & & \left(\text { since } f_{U}(u)=\frac{\lambda(u)}{\Lambda(t)}, 0 \leq u \leq t\right)
\end{aligned}
$$

Bai and Pham (2004) show that:

$$
\begin{aligned}
V[Y(t)] & =E\left\{V\left[\sum_{i=1}^{N(t)} H\left(S_{i}\right) \mid N(t)=n\right]\right\}+V\left\{E\left[\sum_{i=1}^{N(t)} H\left(S_{i}\right) \mid N(t)=n\right]\right\} \\
& =\int_{0}^{t} H^{2}(u) \lambda(u) d u
\end{aligned}
$$

Proposition 10.2 can also be proven by conditioning on the first failure time. Note that Ja et al. (2002) obtain the same results as in Proposition 10.2 except that they consider the special case of $H(t)=e^{-\alpha t}$ through the first failure time approach.

# 10.2.2 DWC Under an FRW Policy 

In this section, we consider a series system with $q$ statistically independent repairable components under an FRW policy with a fixed period $w$. We derive the mathematical expressions for expected DWC and the cost variance.
It is obvious that a series system will fail if and only if any of its components fails. Since simultaneous failures of components are impossible, each time a warranted system fails before $w$, there must be one and only one failed component in the system. Under the FRW policy, the failed component will be identified and repaired free of charge to consumers. For simplicity, we assume that every repair is instantaneous.

Let $\lambda_{i}(t)$ be the failure intensity function of component $i$. Due to instant repair assumption and the structure of series systems, the failure process for each component follows an NHPP on regular time scale, uniquely determined by the intensity function $\lambda_{i}(t)$ (Nguyen and Murthy 1984b). All these $q$ NHPPs are statistically independent since all components in the system are independent.Let the total DWC per system sold be $C(w)$ and define $Y_{i}(w), \forall i, i \in\{1,2, \cdots, q\}$ as follows:

$$
Y_{i}(w)= \begin{cases}\sum_{j=1}^{N_{i}(w)} c_{i} H\left(S_{i j}\right) & \text { if } N_{i}(w) \in\{1,2, \cdots\} \\ 0 & \text { if } N_{i}(w)=0\end{cases}
$$

where $c_{i} H\left(S_{i j}\right)$ can be interpreted as the discounted repair cost upon a system failure due to the $j^{\text {th }}$ failure of component $i$ at the time $S_{i j}$. Obviously $c_{i} H\left(S_{i j}\right)$ depends on the repair cost related to the failed component, which is assumed to be deterministic, it also depends on the failure times of the component, which are random variables in nature and statistically dependent on each other. Since for a series system any component failure will cause a system failure and no simultaneous failures are allowed, we can write $C(w)$ in terms of $Y_{i}(w)$

$$
C(w)=\sum_{i=1}^{q} Y_{i}(w)
$$

From Equation (10.35), it is clear that the system DWC is simply a weighted superposition of $q$ independent random variables $Y_{i}(w), i=1,2, \cdots, q$, and each of them has exactly the same structure as of the $Y(w)$ defined in Section 10.2.1. Therefore, it is easy to verify that

$$
\begin{aligned}
& E[C(w)]=\sum_{i=1}^{q} c_{i} \Lambda_{i}(w) E\left[H\left(U_{i}\right)\right]=\sum_{i=1}^{q} c_{i} \int_{0}^{w} H(u) \lambda_{i}(u) d u \\
& V[C(w)]=\sum_{i=1}^{q} c_{i}^{2} \Lambda_{i}(w) E\left[H^{2}\left(U_{i}\right)\right]=\sum_{i=1}^{q} c_{i}^{2} \int_{0}^{w}(H(u))^{2} \lambda_{i}(u) d u
\end{aligned}
$$

where $f_{U_{i}}(u)=\frac{\lambda_{i}(u)}{\Lambda_{i}(w)}, \quad 0 \leq u \leq w, \forall i, i=1,2, \ldots, q$.
Now, let's determine the functional form of the discounting function $H(\cdot)$. There are two most popular ways of time discounting: the continuous discounting method and the discrete discounting method (Blischke and Murthy 1996, pp.282, 794). For the continuous time discounting, the discounting function is given by $H\left(S_{i j}\right)=e^{-i S_{i j}}$. Under the discrete time discounting, $H\left(S_{i j}\right)=(1+\delta)^{-S_{i j}}$.

Let $C_{d_{i}}(w)$ be the DWC under the continuous discounting, we then have

$$
\begin{aligned}
& E\left[C_{d_{i}}(w)\right]=\sum_{i=1}^{q} c_{i} \int_{0}^{w} e^{-\delta u} \lambda_{i}(u) d u \\
& V\left[C_{d_{i}}(w)\right]=\sum_{i=1}^{q} c_{i}^{2} \int_{0}^{w} e^{-2 \delta u} \lambda_{i}(u) d u
\end{aligned}
$$Similarly, under the discrete time discounting, for the DWC $C_{d_{2}}(w)$,

$$
\begin{aligned}
& E\left[C_{d_{2}}(w)\right]=\sum_{i=1}^{q} c_{i} \int_{0}^{w}(1+\delta)^{-u} \lambda_{i}(u) d u \\
& V\left[C_{d_{2}}(w)\right]=\sum_{i=1}^{q} c_{i}^{2} \int_{0}^{w}(1+\delta)^{-2 u} \lambda_{i}(u) d u
\end{aligned}
$$

Next we discuss three special cases based on the above results considering exponential and Weibull failure time distributions.

# Case I: Exponential distribution 

Suppose all components have constant failure rate, that is, $\lambda_{i}(t)=\lambda_{i}$, $\forall i, i=1,2, \cdots, q$. This implies that the components' failure processes are independent Poisson processes with $\Lambda_{i}(w)=\lambda_{i} w$. So, the $p d f$ of $U_{i}$ is simply $f_{U_{i}}(u)=\frac{1}{w}, 0 \leq u \leq w$. Under the continuous discounting, from Equations (10.38) and (10.39), we obtain

$$
\begin{aligned}
& E\left[C_{d_{1}}(w)\right]=\frac{\left(1-e^{-\delta w}\right)}{\delta} \sum_{i=1}^{q} c_{i} \lambda_{i} \\
& V\left[C_{d_{1}}(w)\right]=\frac{\left(1-e^{-2 \delta w}\right)}{2 \delta} \sum_{i=1}^{q} c_{i}^{2} \lambda_{i}
\end{aligned}
$$

It is worth noting that, for $q=1$, the expected DWC is exactly the same as that in Chun and Twang (1999), but our approach is simpler and more general. While they do not discuss the variance of DWC, we derive the explicit expression here, which is critical in evaluating warranty cost risk. Ja et al. (2002) obtain the noncentered first and second moments of the DWC of four types of warranty policies for one-component products. It turns out that for $q=1$ the result agrees with theirs. For the case of discrete discounting, using Equations (10.40) and (10.41), upon simplification, we have

$$
\begin{aligned}
& E\left[C_{d_{2}}(w)\right]=\frac{1-(1+\delta)^{-w}}{\ln (1+\delta)} \sum_{i=1}^{q} c_{i} \lambda_{i} \\
& V\left[C_{d_{2}}(w)\right]=\frac{1-(1+\delta)^{-2 w}}{2 \ln (1+\delta)} \sum_{i=1}^{q} c_{i}^{2} \lambda_{i}
\end{aligned}
$$

## Case II: Rayleigh distributions

Suppose that for component $i$, the failure time before any repairs follows a Rayleigh distribution, $\forall i, i=1,2, \cdots, q$. Therefore, $\lambda_{i}(t)=\lambda_{i} t, \Lambda_{i}(w)=\lambda_{i} w^{2} / 2$ and $f_{U_{i}}(u)=2 u / w^{2}, 0<u \leq w$. So, under the continuous discounting, we obtain

$$
E\left[C_{d_{1}}(w)\right]=\frac{1-e^{-w \delta}-\delta w e^{-w \delta}}{\delta^{2}} \sum_{i=1}^{q} c_{i} \lambda_{i}
$$$$
V\left[C_{d_{2}}(w)\right]=\frac{1-e^{-2 w \delta}-2 \delta w e^{-2 w \delta}}{4 \delta^{2}} \sum_{i=1}^{q} c_{i}^{2} \lambda_{i}
$$

Similarly, for the discrete discounting, the results are

$$
\begin{aligned}
& E\left[C_{d_{2}}(w)\right]=\frac{1-w(1+\delta)^{-w} \ln (1+\delta)-(1+\delta)^{-w}}{2 \ln (1+\delta)} \sum_{i=1}^{q} c_{i} \lambda_{i} \\
& V\left[C_{d_{2}}(w)\right]=\frac{1-2 w(1+\delta)^{-2 w} \ln (1+\delta)-(1+\delta)^{-2 w}}{8 \ln (1+\delta)} \sum_{i=1}^{q} c_{i}^{2} \lambda_{i}
\end{aligned}
$$

# Case III: Weibull distributions 

Now consider the case that all new components' failure times follow Weibull distribution. Or equivalently, $\lambda_{i}(t)=\frac{\alpha_{i}}{\beta_{i}} t^{\alpha_{i}-1}, \alpha_{i} \geq 1, \beta_{i}>0, \forall i, i=1,2, \cdots, q$. Hence $\Lambda_{i}(w)=w^{\alpha_{i}} / \beta_{i}$ and $f_{U_{i}}(u)=\alpha_{i} u^{\alpha_{i}-1} / w^{\alpha_{i}}, 0 \leq u \leq w$. If the continuous discounting is considered, then

$$
\begin{aligned}
& E\left[C_{d_{1}}(w)\right]=\sum_{i=1}^{q} c_{i} \int_{0}^{w} \frac{\alpha_{i}}{\beta_{i}} u^{\alpha_{i}-1} e^{-\delta u} d u \\
& V\left[C_{d_{1}}(w)\right]=\sum_{i=1}^{q} c_{i}^{2} \int_{0}^{w} \frac{\alpha_{i}}{\beta_{i}} u^{\alpha_{i}-1} e^{-2 \delta u} d u
\end{aligned}
$$

In general, it is necessary to evaluate $E\left[C_{d_{1}}(w)\right]$ and $V\left[C_{d_{1}}(w)\right]$ numerically. However, if $\alpha_{i} \mathrm{~s}$ are positive integers, close form expressions do exist. For example, let $\alpha_{i}=3, \forall i, i=1,2, \cdots, q$, simplifying (10.48) and (10.49), the results are

$$
\begin{aligned}
& E\left[C_{d_{1}}(w)\right]=\frac{3\left(2 e^{\delta w}-\delta^{2} w^{2}-2 \delta w-2\right)}{\delta^{3} e^{\delta w}} \sum_{i=1}^{q} \frac{c_{i}}{\beta_{i}} \\
& V\left[C_{d_{1}}(w)\right]=\frac{3\left(e^{2 \delta w}-2 \delta^{2} w^{2}-2 \delta w-1\right)}{4 \delta^{3} e^{2 \delta w}} \sum_{i=1}^{q} \frac{c_{i}^{2}}{\beta_{i}}
\end{aligned}
$$

If instead the discrete discounting is adopted, for $\alpha_{i}=3, \forall i, i=1,2, \cdots, q$, the expected DWC and the cost variance are:

$$
\begin{aligned}
& E\left[C_{d_{2}}(w)\right]=\frac{2\left((1+\delta)^{w}-w^{2} \ln (1+\delta)-w \ln (1+\delta)-1\right)}{(1+\delta)^{w} \ln (1+\delta)} \sum_{i=1}^{q} \frac{c_{i}}{\beta_{i}} \\
& V\left[C_{d_{2}}(w)\right]=\frac{(1+\delta)^{2 w}-4 w^{2} \ln (1+\delta)-2 w \ln (1+\delta)-1}{4(1+\delta)^{2 w} \ln (1+\delta)} \sum_{i=1}^{q} \frac{c_{i}^{2}}{\beta_{i}}
\end{aligned}
$$

### 10.2.3 DWC Under a PRW Policy

This section considers a PRW policy with period $w$ for the $q$-component series system, and will derive the mathematical expressions for expected DWC and thecost variance.
Suppose that the PRW policy specifies that a consumer will get the amount of refund depending on the cost of the failed component instead of the total purchase price, then mathematically we can define the refund function, $K(\cdot)$, as follows: let $S_{i j}, 0 \leq S_{i j} \leq w$, be a system failure time, or equivalently, the $j^{\text {th }}$ failure time of component $i$, the warranty refund amount due to this failure is given by

$$
K\left(S_{i j}\right)=c_{i}\left(1-\frac{S_{i j}}{w}\right)
$$

Let $K^{\prime}\left(S_{i j}\right)$ be the ratio of the refund and the original cost $c_{i}$, then

$$
K^{\prime}\left(S_{i j}\right)=\left(1-\frac{S_{i j}}{w}\right)
$$

Again, let $H(\cdot)$ be the discounting function and define $Y_{i}^{\prime}(w), \forall i, i \in\{1,2, \cdots, q\}$ as follows:

$$
Y_{i}^{\prime}(w)=\left\{\begin{array}{cl}
\sum_{j=1}^{N_{i}(w)} c_{i} K^{\prime}\left(S_{i j}\right) H\left(S_{i j}\right) & \text { if } N_{i}(w) \in\{1,2, \cdots\} \\
0 & \text { if } N_{i}(w)=0
\end{array}\right\}
$$

then the total discounted refund for a warranted series system can be written as

$$
C(w)=\sum_{i=1}^{q} Y_{i}^{\prime}(w)
$$

Not surprisingly, if we let $G\left(S_{i j}\right)=K^{\prime}\left(S_{i j}\right) H\left(S_{i j}\right)$, we can directly apply the results in Equations (10.36) and (10.37) after replacing the $H(\cdot)$ function by the $G(\cdot)$ function. Therefore, the case of determining the discounted value of the PRW policy is a special case of what we discussed in Section 10.2.2.

Equation (10.50) implicitly assumes that the refund function is linear in components' failure time (Blischke and Murthy 1994, p.295). However, our formulation does not necessarily require the linearity assumption. Actually it can be any continuous function. We also assume that each refund depends on component's cost instead of the system purchase price (or manufacturer's production cost), which is usually the refund base in practice. Nevertheless, theoretically speaking our formulation is more general and it can be modified easily when the purchase price is considered. In particular, for $q=1$, the choice of base price has virtually no impact to our model since one can always interpret c1 as the purchase price. It should be noted that PRW is often used for non-repairable products such as automobile batteries, television picture tubes, and so forth (Blischke and Murthy 1994, p.169). However, such a policy could still be used for repairable products because: (1) consumers might be willing to share the repair cost with manufacturers for the benefits they has received after the purchase; (2) warranty issuers have the choice of offering longer warranties, which may be more attractive to buyers, provided that some of the cost is shared by consumers.For illustration purposes, let us continue the Case III in Section 10.2.2 by considering the linear PRW policy with warranty period $w$. Since all new components' failure times are assumed to follow Weibull distributions, we have, $\forall i, i=1,2, \ldots, q$,

$$
\text { (a) } \lambda_{i}(t)=\frac{\alpha_{i}}{\beta_{i}} t^{\alpha_{i}-1},(\text { b) } \Lambda_{i}(w)=\frac{w_{i}^{\alpha}}{\beta_{i}},(\text { c) } f_{U_{i}}(u)=\frac{\alpha_{i} u^{\alpha_{i}-1}}{w^{\alpha_{i}}}, \quad 0 \leq u \leq w
$$

If the continuous discounting is considered, then $G\left(U_{i}\right)=\left(1-U_{i} / w\right) e^{-\delta U_{i}}$. For $\alpha_{i}=3, \forall i, i=1,2, \cdots, q$, using Equations (10.36) and (10.37) (replacing $H(\cdot)$ by $G(\cdot))$, upon simplification, we obtain the following:

$$
\begin{gathered}
E\left[C_{d_{i}}(w)\right]=\frac{3\left(6+4 w \delta+\delta^{2} w^{2}-6 e^{\delta w}+2 w \delta e^{\delta w}+2 w \delta^{4} w^{2 \delta w} \sum_{i=1}^{q} \frac{c_{i}}{\beta_{i}}\right. \\
V\left[C_{d_{i}}(w)\right]=\frac{-3\left(3+3 w \delta+\delta^{2} w^{2}-3 e^{2 \delta w}-\delta^{2} w^{2} e^{2 \delta w}+3 w \delta e^{2 \delta w} \sum_{i=1}^{q} \frac{c_{i}^{2}}{\beta_{i}}\right.
\end{gathered}
$$

# 10.2.4 Numerical Examples 

In the design phase of warranty programs, warranty program managers are often faced with the following two important questions:

## (I) Warranty period determination (WPD) problem

Suppose that the budget $c_{0}$ for a warranty policy (either a FRW or PRW) is given.
The warranty managers would like to determine the warranty period $w^{*}$, which is attractive to consumers, at the same time, the probability that the true warranty cost is over the budget is less or equal to $\alpha$. Clearly it is desirable for manufacturers to offer the best possible warranty policy provided that the budget is followed properly. Therefore, $w^{*}$, the optimal warranty period, can be formulated as

$$
w^{*}=\sup \left\{w: P\left[C(w)>c_{0}\right] \leq \alpha\right\}
$$

## (II) Warranty reserve determination (WRD) problem

If due to competition, $w$, the parameter of the warranty period, is pre-determined, but it is of interest to find the required warranty reserve level $c_{w r}^{*}$ such that the probability that the warranty reserve $c_{w r}$ will be depleted is controlled. The corresponding mathematical expression for $c_{w r}^{*}$ is

$$
c_{w r}^{*}=\inf \left\{c_{w r}: P\left[c_{w r}>C(w)\right] \geq 1-\alpha\right\}
$$

Mathematically, these two problems are like dual problems. The main difficulty lies in the complexity of the distribution of $C(w)$, which in general is unknownand difficult to obtain. However, with the information of the first and second centered moments of DWC per product, it is possible to utilize a normal approximation to solve them for the cases like single lot sales (Patankar and Worm 1981, p.142).

Let $L$ be the size of a single lot sale, which is a relatively large number. The warranty policies under consideration are FRW or PRW. The total DWC (or the present value (PV) of the refund) for the lot sale is simply

$$
T C=\sum_{i=1}^{L} C_{i}(w)
$$

where $C_{i}(w)$ is the PV or the DWC of product $i$. Obviously, $C_{i}(w) \mathrm{s}$ are i.i.d.. whose expectation $E[C(w)]$ and the variance $V[C(w)]$ are given in Section 10.2.2 and Section 10.2.3 for the FRW policy or the PRW policy respectively. By the central limit theory, as $L$ is relatively large, the distribution of TC is approximately normal regardless the distribution of $C_{i}(w)$. Furthermore, from Equation (10.53) it is easy to obtain:

$$
\begin{aligned}
& \mathrm{E}[T C]=L \cdot \mathrm{E}[C(w)] \\
& \mathrm{V}[T C]=L \cdot \mathrm{~V}[C(w)]
\end{aligned}
$$

Consequently, for the WRD problem of the lot sale, denote $T C_{w r}^{*}$ as the required warranty reserve level, then

$$
T C_{w r}^{*}=L \cdot \mathrm{E}[C(w)]+z_{1-\alpha} \sqrt{L \cdot \mathrm{~V}[C(w)]}
$$

If the warranty budget $c_{0}$ is given and it is desirable to determine the warranty period $w$, then this becomes the WPD problem. Again let $w^{*}$ be the required warranty duration, then $w^{*}$ is simply the solution for the following non-linear equation:

$$
\frac{c_{0}-L \cdot \mathrm{E}[C(w)]}{\sqrt{L \cdot \mathrm{~V}[C(w)]}}=z_{1-\alpha}
$$

where $z_{1-\alpha}$ is the $(1-\alpha)$ quantile of the standard normal distribution.
It is necessary to check the existence and the uniqueness of $w^{*}$. Let $\psi(w)=$ $z_{1-\alpha} \sqrt{L \cdot \mathrm{~V}[C(w)]}+L \cdot \mathrm{E}[C(w)]-c_{0}$; then it is sufficient to show that there exists a unique $w^{*}$ such that $\psi\left(w^{*}\right)=0$. Clearly $\psi(w)$ is continuous and monotonically increasing in $w$ if both $E[C(w)]$ and $V[C(w)]$ are continuous and increasing functions of $w$, which are true in general. As $w \rightarrow 0, \psi(w) \rightarrow-c_{0}$, which is negative provided that $c_{0}>0$. Also it is obvious that there exists a positive number $w^{+}$such that $\psi\left(w^{+}\right)>0$. Therefore, a unique $w^{*}$ exists in $(0, \infty)$ that can be expressed as$$
w^{*}=\psi^{-1}(0)
$$

where $\psi^{-1}(0)$ is the inverse function of $\psi(\cdot)$ evaluated at the point 0 . The existence of $\psi^{-1}(\cdot)$ is given by the fact that $\psi(\cdot)$ is a monotonically increasing function in $(0, \infty)$.

One can use Equation (10.58) directly for the purpose of determining $w^{*}$. In case the functional form of $\psi^{-1}(\cdot)$ is complicated and hard to obtain due to the complexity of $\psi(w)$, the Newton-Raphson method can be applied.

Consider a numerical example. Suppose the warranty policy under consideration is a FRPW with $w=1$ and $L=1000$. The product under warranty is a threecomponent series system for which all failures under warranty are minimally repaired. Other parameters are given in Table 10.3.

Table 10.3. Parameters for the 3-component minimally repaired series system

| Component No. | 1 | 2 | 3 |
| :--: | :--: | :--: | :--: |
| $c_{i}$ | $\$ 100$ | $\$ 150$ | $\$ 200$ |
| $\lambda_{i}(t)$ | 0.0611 | $0.0423 t$ | $0.0187 t^{2}$ |

If the continuous discounting method is used and the discounting rate $\delta$ is $5 \%$, then according to Equations (10.38) and (10.39) and using the intermediate results in Cases I through III in Section 10.2.2, we have that $\mathrm{E}\left[C_{d_{1}}(w)\right]=\$ 10.23$ and $\mathrm{V}\left[C_{d_{1}}(w)\right]=9.94$. Therefore, for the WRD problem, the required warranty reserve level $T C_{w r}^{*}$ is $\$ 10461.25$ for $\alpha=0.01$.

For the WPD problem, if we are given that $c_{0}=T C_{w r}^{*}$, then obviously the required warranty duration $w^{*}$ is 1 . However, in practice usually $c_{0}$ is different from $T C_{w r}^{*}$ due to various budget constraints faced by warranty managers. If it is known that $c_{0}=\$ 20,000$, by employing the Newton-Raphson method, we have that $w^{*}=1.5037$. One should note that in this example both explicit forms exist for $\mathrm{E}\left[C_{d_{1}}(w)\right]$ and $\mathrm{V}\left[C_{d_{1}}(w)\right]$, which makes the computation of $w^{*}$ relatively easy. However, even if no explicit form exists for either $\mathrm{E}\left[C_{d_{1}}(w)\right]$ and $\mathrm{V}\left[C_{d_{1}}(w)\right]$, Newton-Raphson method can still be applied to find $w^{*}$, for example, by considering polynomial approximations to $\mathrm{E}\left[C_{d_{1}}(w)\right]$ and $\mathrm{V}\left[C_{d_{1}}(w)\right]$ whenever necessary (Rustagi 1994, p.148).

# 10.2.5 Future Research 

Section 10.2 has covered modeling of DWC for series systems with minimally repaired components. Both the expected value and the variance of DWC for FRWpolicies and PRW policies are considered. As shown in the applications, the results in this section can be used to determine the warranty duration or the required level of warranty reserve, two primary questions to be answered by warranty planning managers.

There may be some potential extensions to the warranty cost analysis of repairable complex systems: First is to consider imperfect repair (Pham and Wang 1996, p.146) instead of minimal repair. Second, one may consider non-instant repair as against to instant repair. Although instant repair can be justified when repair time is relatively short compared to warranty period, it might raise some concerns for multi-component systems since as the size of the system increases, the total repair time might be long enough that it has to be considered explicitly. Besides, in the automobile industry, additional warranty cost, such as transportation expense, may occur if a warranted vehicle cannot be repaired within one working day. Third, one may take into account of different system structure on warranty cost analysis. As shown in Section 10.1, various system structures could result in different warranty cost models. In this section, only series systems are considered. It is desirable to model DWC for more complicated systems such as series-parallel systems, parallel-series systems and $k$-out-of- $n$ systems.

# 10.3 RLRFW Policies with Imperfect Repair 

Numerous warranties have been studied in the past several decades. In general, one can divide them into three categories: free repair/replacement warranty (FRW), pro-rata warranty (PRW) and combination warranty that contains features of both FRW and PRW. In this section we introduce a repair-limit risk-free warranty (RLRFW) of fixed period $w$, based on Bai and Pham (2005). Different from ordinary FRW policies, this policy has a pre-determined limit $m$ on the number of repairs. If there are more than $m$ system failures within $w$, the failed product will be replaced instead of being repaired again. Such a policy is desirable for both manufacturers and consumers. For consumers, surely they will prefer such a policy to a simple free repair policy since there are chances that they could own another new product for free. From manufacturers' point of view, first of all, such a policy offers extra incentive for consumers to purchase their products. Second, if a single product has failed $m$ times before $w$, this might have provided sufficient information that the particular product is indeed of low quality. So it could be economically sound for the manufacturer to simply provide replacements without wasting more time on repairs. In addition, such extra compensation for those unlucky consumers may effectively reduce the chance of high-cost lawsuits due to those products with 'proven' bad quality.

### 10.3.1 Introduction

As discussed in Chapter 3, many researchers have studied various repair limit problems, which can be categorized into three groups: repair-number limit problems, repair-time limit problems and repair-cost limit problems. Almost all researchers dealing with repair-limit problems assumed infinite horizon andperformed the analysis based on asymptotic cost measures such as long-run average cost. This section focuses on finite horizon for the proposed repair-number limit warranty policy.

The main analytical tool used in this section is the truncated quasi-renewal processes. The concept and some properties of truncated quasi-renewal processes can be found in Chapter 4.

Another important issue in warranty cost analysis is the variability of warranty cost. It is often not sufficient for warranty managers to simply obtain the estimate of expected warranty cost. Additional information about variability of warranty cost is essential to evaluate risks involved in warranty programs.

The rest of this section is organized as follows. Section 10.3.2 provides the detailed analysis of the repair-limit risk-free warranty policy. Several special cases are discussed in Section 10.3.3. Section 10.3.4 presents sensitivity analyses for various policy parameters based on numerical examples.

In this section, we assume:
i) All warranty service is instant.
ii) Repairs are imperfect and the failure process before the first replacement follows a truncated quasi-renewal process with parameters $\alpha(0<\alpha<1)$ and $F$.
iii) All warranty claims are executed and all claims are valid.
iv) Both repair cost $c_{a}$ and replacement cost $c_{b}$ are constant and $c_{a}<c_{b}$ to avoid triviality.

# 10.3.2 Analysis of Repair-limit Risk-free Warranties 

In this section we discuss the warranty model of the repair-limit risk-free policy with warranty period $w$ and repair limit $m$, based on Bai and Pham (2005). We assume that repairs are imperfect such that after each repair, the system is between the states "as good as new" and "as bad as old". Suppose that the failure process with the imperfect repair follows a quasi-renewal process with parameter $\alpha$ $(0<\alpha<1)$ and $F$ (see Chapter 4). Since any warranted products will be repaired no more than $m$ times according to this policy, the failure process before the first replacement is actually a quasi-renewal process truncated above $m$. As a reminder, by the definition of truncated quasi-renewal processes, the inter-failure times in the process are independent and have the distributions $F\left(\alpha^{1-n} x\right), n=0,1, \cdots, m$.

One should note that for a repair-limit risk-free warranty policy, only Model II of truncated quasi-renewal processes is appropriate since the repair limit $m$ has no impact on the probabilities of the number of repairs except when it is equal to $m$.

Let $N_{a}(w)$ and $N_{b}(w)$ be the number of repairs and the number of replacements within the warranty duration respectively. Since $w$ is predetermined, we will suppress it later on for simplicity. Denote $c_{a}$ as the repair cost per failure and $c_{b}$ the replacement cost per unit, then for the warranty cost per product sold $C$, we have

$$
\mathrm{E}[C]=c_{a} \mathrm{E}\left[N_{a}\right]+c_{b} \mathrm{E}\left[N_{b}\right]
$$and

$$
\mathrm{V}[C]=c_{a}^{2} \mathrm{~V}\left[N_{a}\right]+c_{b}^{2} \mathrm{~V}\left[N_{b}\right]+2 c_{a} c_{b} \operatorname{COV}\left(N_{a}, N_{b}\right)
$$

Note that $N_{a}$ and $N_{b}$ are correlated and $\operatorname{COV}\left(N_{a}, N_{b}\right) \neq 0$. The relationship between them can be summarized as followings:
i) $\quad N_{a}<m$ implies $N_{b}=0$
ii) $\quad N_{b}>0$ implies $N_{a}=m$
iii) $\quad N_{b}=0$ implies $N_{a} \leq m$
iv) $\quad N_{a}=m$ implies $N_{b} \geq 0$

# Moments of $N_{a}$ 

Since under the warranty replacement instead of repair will be performed if there are more than $m$ failures within $w$, it is obvious that $N_{a}$ is a realization of a quasirenewal process truncated above $m$. As mentioned at the beginning of Section 10.3.1, Model II of truncated quasi-renewal processes can be used in describing the behavior of $N_{a}$. Hence we have

$$
\begin{aligned}
& E\left[N_{a}\right]=\sum_{i=1}^{m} G^{(i)}(w) \\
& E\left[N_{a}^{2}\right]=\sum_{i=1}^{m}(2 i-1) G^{(i)}(w)
\end{aligned}
$$

## The Pivot Point $S_{m}$

A pivot point is the time epoch that indicates the change of the type of warranty service. For the repair-limit risk-free policy, obviously $S_{m}$ is the pivot point since after it any failed products will be replaced instead of being repaired again. Let $H\left(t_{p}\right)$ be the $c d f$ of $S_{m}$, then

$$
\begin{aligned}
H\left(t_{p}\right) & \equiv P\left[S_{m} \leq t_{p}\right] \\
& =G^{(m)}\left(t_{p}\right), \quad t_{p} \geq 0
\end{aligned}
$$

## Moments of $N_{b}$

Suppose $S_{m}=t_{p}, 0 \leq t_{p} \leq w$, then starting from $t_{p}$, the system failure process becomes a delayed renewal process with the first failure time having the distribution $F_{m+1}(x)$ where $F_{m+1}(x)=F\left(\alpha^{-m} x\right)$ and all the following failure times are i.i.d. with distribution $F$. Conditioning on $S_{m}=t_{p}, t_{p} \leq w$, from the renewal theory, $E\left[N_{b} \mid S_{m}=t_{p}, t_{p} \leq w\right]=M_{d}\left(w-t_{p}\right)$ where $M_{d}(\cdot)$, the renewal function for the delayed renewal process, is given by

$$
M_{d}(t)=\sum_{i=0}^{\infty} F_{m+1} * F^{(i)}(t)
$$where $F^{(i)}(\cdot)$ is the $i$-fold convolution of $F(\cdot)$ itself and $F^{0}(\cdot)=1$ and

$$
F_{m+1} * F^{(i)}(t)=\int_{0}^{i} F_{m+1}(t-x) d F^{(i)}(x), \quad i \geq 0
$$

is the convolution of $F_{m+1}$ and $F^{(i)}$. After un-conditioning on $S_{m}$,

$$
E\left[N_{b}\right]=\int_{0}^{w} M_{d}\left(w-t_{p}\right) d H\left(t_{p}\right)
$$

Similar technique can be used to obtain $E\left[N_{b}^{2}\right]$. Let $M_{d, 2}\left(w-t_{p}\right) \equiv$ $E\left[N_{b}^{2} \mid S_{m}=t_{p}, t_{p} \leq w\right]$ then

$$
E\left[N_{b}^{2}\right]=\int_{0}^{w} M_{d, 2}\left(w-t_{p}\right) d H\left(t_{p}\right)
$$

where $M_{d, 2}(\cdot)$ can obtained by

$$
M_{d, 2}(t)=\sum_{i=0}^{\infty}(2 i+1) F_{m+1} * F^{(i)}(t)
$$

# Covariance of $\left(N_{a}, N_{b}\right)$ 

Next we determine covariance $\operatorname{COV}\left(N_{a}, N_{b}\right)$. Since $\operatorname{COV}\left(N_{a}, N_{b}\right)=E\left[N_{a} N_{b}\right]$ $-E\left[N_{a}\right] E\left[N_{b}\right]$, it is sufficient to know $E\left[N_{a} N_{b}\right]$. Note

$$
\begin{aligned}
E\left[N_{a} N_{b}\right] & =\sum_{n_{b}=0}^{\infty} \sum_{n_{a}=0}^{\infty} n_{a} n_{b} P\left[N_{a}=n_{a}, N_{b}=n_{b}\right] \\
& =m \sum_{n_{b}=0}^{\infty} n_{b} p\left[m, n_{b}\right] \\
& =m \sum_{n_{b}=1}^{\infty} n_{b} \int_{0}^{w} P\left[n_{b} \mid S_{m}=t_{p}\right] d H\left(t_{p}\right)
\end{aligned}
$$

and for $t_{p} \leq w$,

$$
\begin{gathered}
P\left[N_{b}=0 \mid S_{m}=t_{p}\right]=1-F_{m+1}\left(w-t_{p}\right) \\
P\left[N_{b}=n_{b} \mid S_{m}=t_{p}\right]=F_{m+1} * G^{\left(n_{b}-1\right)}\left(w-t_{p}\right)-F_{m+1} * G^{\left(n_{b}\right)}\left(w-t_{p}\right), \quad n_{b} \geq 1
\end{gathered}
$$

we obtain

$$
E\left[N_{a} N_{b}\right]=m \sum_{n_{b}=1}^{\infty} n_{b} \int_{0}^{w}\left[F_{m+1} * G^{\left(n_{b}-1\right)}\left(w-t_{p}\right)-F_{m+1} * G^{\left(n_{b}\right)}\left(w-t_{p}\right)\right] d H\left(t_{p}\right)
$$

Consequently,$$
\begin{aligned}
\operatorname{COV}\left[N_{a}, N_{b}\right] & =m \sum_{n_{b}=1}^{n} n_{b} \int_{0}^{w}\left[F_{m+1} * G^{\left(n_{b}-1\right)}\left(w-t_{p}\right)-F_{m+1} * G^{\left(n_{b}\right)}\left(w-t_{p}\right)\right] d H\left(t_{p}\right) \\
& -\int_{0}^{w} M_{d}\left(w-t_{p}\right) d H\left(t_{p}\right) \sum_{i=1}^{m} G^{(i)}(w)
\end{aligned}
$$

# Main Results: First and Second Moments of $C(w)$ 

Substituting Equations (10.61) and (10.64) into (10.59), we finally have the expected warranty cost per unit sold:

$$
E[C]=c_{a} \sum_{i=1}^{m} G^{(i)}(w)+c_{b} \int_{0}^{w} M_{d}\left(w-t_{p}\right) d H\left(t_{p}\right)
$$

The variance of the warranty cost per unit sold can be obtained through Equations (10.62), (10.65) and (10.67):

$$
\begin{aligned}
V[C]= & c_{a}^{2}\left\{\sum_{i=1}^{m}(2 i-1) G^{(i)}(w)-\left[\sum_{i=1}^{m} G^{(i)}(w)\right]^{2}\right\} \\
& +c_{b}^{2}\left\{\int_{0}^{w} M_{d, 2}\left(w-t_{p}\right) d H\left(t_{p}\right)-\left[\int_{0}^{w} M_{d}\left(w-t_{p}\right) d H\left(t_{p}\right)\right]^{2}\right\} \\
& +2 c_{a} c_{b}\left\{m \sum_{n_{b}=1}^{w} n_{b} \int_{0}^{w}\left[F_{m+1} * G^{\left(n_{b}-1\right)}\left(w-t_{p}\right)-F_{m+1} * G^{\left(n_{b}\right)}\left(w-t_{p}\right)\right] d H\left(t_{p}\right)\right. \\
& \left.-\int_{0}^{w} M_{d}\left(w-t_{p}\right) d H\left(t_{p}\right) \sum_{i=1}^{m} G^{(i)}(w)\right\}
\end{aligned}
$$

### 10.3.3 Special Cases

We have derived $E(C)$ and $V(C)$, as shown in Equations (6.68) and (6.69). It is difficult to evaluate $E(C)$ and $V(C)$ analytically, and now we discuss some special cases.

Case I: Suppose for finite $w, m=0$. In this case, no repair is allowed so all failed products within $w$ will be replaced always. This implies that $F_{i} \sim F, \forall i, i \geq 1$. So our policy degenerates to the regular free replacement policy. As a result, Equation (10.68) becomes

$$
E[C]=c_{b} M(w)
$$

Equation (10.69) changes to

$$
V[C]=c_{b}^{2}\left\{M_{2}(w)-[M(w)]^{2}\right\}
$$

where $M(t)$ and $M_{2}(w)$ are the first and the second moments of the number of renewals in a renewal process associated with $F$.These are the well-known results for the FRW policy (see Blischke and Murthy 1994).

Case II: Consider $m=\infty$ and w is finite. Thus no change of warranty service will ever happen and all failed products within w will be repaired. Consequently, we have

$$
E[C]=c_{a} \sum_{i=1}^{\infty} G^{(i)}(w)
$$

and

$$
V[C]=c_{a}^{2}\left\{\sum_{i=1}^{\infty}(2 i-1) G^{(i)}(w)-\left[\sum_{i=1}^{\infty} G^{(i)}(w)\right]^{2}\right\}
$$

These results agree with the study in Wang and Pham (1996).
Case III: Suppose for finite positive integer valued $m, w$ is large such that it can be treated as infinity. In this case, $E[C] \rightarrow \infty$ since it is strictly increasing in $w$. One may be interested in determining warranty cost per unit time (long-run average cost), another cost measure that is commonly used in the warranty and maintenance literature. It is not difficult to see that the long-run average cost $E\left[C^{\prime}\right]$ is given by

$$
E\left[C^{\prime}\right]=\frac{c_{b}}{\int_{-\infty}^{+\infty} x d F(x)}
$$

It is worth noting that this measure is only an approximation for the true warranty cost per unit time, and its accuracy heavily depends on the magnitude of $w$ compared to the product life times.

Case IV: Assume $F$ is a normal distribution with mean $\mu$ and variance $\sigma^{2}$ for finite positive integer-valued $m$ and finite $w$, i.e., $F \sim N\left(\mu, \sigma^{2}\right)$. As a result, the interarrival failure times under the imperfect repairs are independent and also follow the normal distribution. In particular, it is easy to see that $F_{i} \sim$ $N\left(\alpha^{i-1} \mu, \alpha^{2(i-1)} \sigma^{2}\right)$. Thus $G^{(i)} \sim N\left(\frac{1-\alpha^{i}}{1-\alpha} \mu, \frac{1-\alpha^{2 i}}{1-\alpha} \sigma^{2}\right)$. The pivot point distribution $H\left(t_{p}\right)$ is given by

$$
H\left(t_{p}\right)=\psi\left(\left(t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu\right) /\left[\sigma \sqrt{\left.\left(1-\alpha^{2 m}\right) /\left(1-\alpha^{2}\right)\right]}\right)\right.
$$

where $\psi(\cdot)$ is the $c d f$ of the standard normal distribution.
To compute $M_{d}\left(w-t_{p}\right)$, we need to evaluate $F_{m+1} * F^{(i)}$, which obeys the distribution $N\left(\left(\alpha^{m}+i\right) \mu,\left(\alpha^{2 m}+i\right) \sigma^{2}\right)$. So$$
M_{d}\left(w-t_{p}\right)=\sum_{i=0}^{\infty} \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\alpha^{2 m}+i}}\right.
$$

Similarly,

$$
M_{d, 2}\left(w-t_{p}\right)=\sum_{i=0}^{\infty}(2 i+1) \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\alpha^{2 m}+i}}\right)
$$

It is also necessary to obtain $F_{m+1} * G^{n_{b}-1}$ and $F_{m+1} * G^{n_{b}}$. Clearly, they again follow the normal distribution with parameters

$$
\begin{aligned}
& \left(\left(\alpha^{m}+\frac{1-\alpha^{n_{b}-1}}{1-\alpha}\right) \mu_{r}\left(\alpha^{2 m}+\frac{1-\alpha^{2\left(n_{b}-1\right)}}{1-\alpha^{2}}\right) \sigma^{2}\right) \text { and } \\
& \left(\left(\alpha^{m}+\frac{1-\alpha^{n_{b}}}{1-\alpha}\right) \mu_{r}\left(\alpha^{2 m}+\frac{1-\alpha^{2 n_{b}}}{1-\alpha^{2}}\right) \sigma^{2}\right) \text { respectively. }
\end{aligned}
$$

To obtain the expected warranty cost, combining the previous results together, Equation (6.68) is simplified to

$$
\begin{aligned}
E[C]= & c_{a} \sum_{i=1}^{m} \psi\left(\frac{w-\mu\left(1-\alpha^{i}\right) /(1-\alpha)}{\sigma \sqrt{\left(1-\alpha^{2 i}\right) /\left(1-\alpha^{2}\right)}}\right) \\
& +c_{b} \int_{0}^{w} \sum_{i=0}^{\infty} \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\alpha^{2 m}+i}} d \psi\left(\frac{t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu}{\sigma \sqrt{\left(1-\sigma^{2 m}\right) /\left(1-\alpha^{2}\right)}}\right)\right.
\end{aligned}
$$

The variance can be simplified in a similar way:

$$
\begin{aligned}
V[C]= & c_{a}^{2}\left\{\sum_{i=1}^{m}(2 i-1) \psi\left(\frac{w-\frac{1-\alpha^{i}}{1-\alpha} \mu}{\sigma \sqrt{\frac{1-\alpha^{2 i}}{1-\alpha^{2}}}}\right)-\left[\sum_{i=1}^{m} \psi\left(\frac{w-\frac{1-\alpha^{i}}{1-\alpha} \mu}{\sigma \sqrt{\frac{1-\alpha^{2 i}}{1-\alpha^{2}}}}\right)\right]^{2}\right\} \\
& +c_{b}^{2}\left\{\int_{0}^{w} \sum_{i=0}^{\infty}(2 i+1) \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\left(\alpha^{2 m}+i\right)}}\right) d \psi\left(\frac{t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu}{\sigma \sqrt{\left(1-\alpha^{2 m}\right) /\left(1-\alpha^{2}\right)}}\right)\right. \\
& \left.-\left[\int_{0}^{w} \sum_{i=0}^{\infty} \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\alpha^{2 m}+i}}\right) d \psi\left(\frac{t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu}{\sigma \sqrt{\left(1-\alpha^{2 m}\right) /\left(1-\alpha^{2}\right)}}\right)\right]^{2}\right\} \\
& +2 c_{a} c_{b}\left\{m \sum_{n_{b}=1}^{\infty} n_{b} \int_{0}^{w}\left[\psi\left(\frac{w-t_{p}-\left(\alpha^{m}+\frac{1-\alpha^{n_{b}-1}}{1-\alpha}\right) \mu}{\sigma \sqrt{\alpha^{2 m}+\frac{1-\alpha^{2\left(n_{b}-1\right)}}{1-\alpha^{2}}}}\right)\right.\right.
\end{aligned}
$$$$
\begin{aligned}
& -\psi\left(\frac{w-t_{p}-\left(\alpha^{m}+\frac{1-\alpha^{n_{b}-1}}{1-\alpha}\right) \mu}{\sigma \sqrt{\alpha^{2 m}+\frac{1-\alpha^{2 n_{b}}}{1-\alpha^{2}} i}}\right) d \psi\left(\frac{t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu}{\sigma \sqrt{\left(1-\alpha^{2 m}\right) /\left(1-\alpha^{2}\right)}}\right) \\
& -\int_{0}^{\infty} \sum_{0}^{\infty} \psi\left(\frac{w-t_{p}-\left(\alpha^{m}+i\right) \mu}{\sigma \sqrt{\alpha^{2 m}+i}}\right) d \psi\left(\frac{t_{p}-\frac{1-\alpha^{m}}{1-\alpha} \mu}{\sigma \sqrt{\frac{\left(1-\alpha^{2 m}\right)}{\left(1-\alpha^{2}\right)}}}\right) \sum_{i=1}^{\infty} \psi\left(\frac{w-\frac{1-\alpha^{i}}{1-\alpha} \mu}{\sigma \sqrt{\frac{1-\alpha^{2 i}}{1-\alpha}}}\right)]
\end{aligned}
$$

# 10.3.4 Numerical Examples and Sensitivity Analysis 

Now, let us consider a numerical example. Suppose $F \sim N(4,1), m=1, w=2.5$, $\alpha=.70, c_{a}=\$ 100$, and $c_{b}=\$ 5000$. Using Equation (6.80), we obtain that $E(C)=$ $\$ 7.6726$, which only accounts for $0.15 \%$ of the unit production (replacement) cost. By looking into the components of the warranty cost, we find that the repair cost is the dominant source as it contributes $87.07 \%$ to $E(C)$. This is what one should expect since the probability of more than one failure within $w$ is very small $(0.02 \%)$, indicating that most of the time no replacement will ever happen under the warranty. The standard deviation (std) of the warranty cost is 75.9571 , which indicates moderate risk contained in this warranty policy. When decomposing $V(C)$, not surprisingly we find that the dominant source of the variation in the warranty cost is from the replacement cost. The contributions in the variation from repair, replacement and the interaction between them are $10.81 \%, 85.99 \%$ and $3.21 \%$, respectively.

Table 10.4. $E[C]$ and $\operatorname{std}(C)$ for $\alpha=0.7, c_{a}=\$ 100$ and $c_{b}=\$ 5000$

| $w$ | $E[C]$ |  |  |  | $\operatorname{std}(C)$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $m=1$ | $m=2$ | $m=3$ | $m=4$ | $m=1$ | $m=2$ | $m=3$ | $m=4$ |
| 1.0 | 0.1372 | 0.1351 | 0.1351 | 0.1351 | 4.9754 | 3.6785 | 3.6758 | 3.6757 |
| 1.5 | 0.6442 | 0.6217 | 0.6217 | 0.6217 | 13.5118 | 7.8895 | 7.8693 | 7.8691 |
| 2.0 | 2.4495 | 2.2799 | 2.2792 | 2.2792 | 33.6026 | 15.0592 | 14.9533 | 14.9525 |
| 2.5 | 7.6726 | 6.7069 | 6.7022 | 6.7022 | 75.9571 | 25.5623 | 25.0969 | 25.0921 |
| 3.0 | 20.3751 | 15.9878 | 15.9591 | 15.9587 | 156.9596 | 38.8223 | 36.9034 | 36.8782 |

It is of interest to know how the warranty cost measures $E(C)$ and $\operatorname{std}(C)$ change with regard to parameters $m, w, \alpha$, and the replacement-repair cost ratio $c_{b} / c_{a}$. First vary $m$ in $\{1,2,3,4\}$ and $w$ in $\{1.0,1.5,2.0,2.5,3.0\}$ while keeping other parameters unchanged. The corresponding reliability of a new warranted productevaluated at $w$ are within the range of $84.13 \%$ to $99.87 \%$.
From Table 10.4, it is clear that both $E(C)$ and $\operatorname{std}(C)$ are monotonically increasing in $w$. This is reasonable since the chance of failures happening increases as the warranty period becomes longer. As $m$, the repair limit increases from 1 to 4 , both $E(C)$ and $\operatorname{std}(C)$ decreases, but the magnitude of decreasing becomes much smaller after $m=2$. This suggests that $m=2$ could be a good policy choice since the warranty cost and the risk associated with it are relatively small, while at the same time, smaller $m$ tends to be more attractive to consumers.

To investigate how the effort of repair affects the warranty cost, we consider three different levels of $\alpha$ (higher $\alpha$ indicates better repair). All other parameters are kept the same and $m$ is chosen as 2 . As expected, as $\alpha$ goes up, both $E[C]$ and $\operatorname{std}(C)$ decrease, as indicated in Table 10.5. This implies that it is possible to reduce the warranty cost and the warranty cost risk by improving the quality of repair.

Table 10.5. $E[C]$ and $\operatorname{std}(C)$ under various levels of repair efforts

| $w$ | $E[C]$ |  |  | $\operatorname{std}(C)$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $a=0.5$ | $a=0.7$ | $a=0.9$ | $a=0.5$ | $a=0.7$ | $a=0.9$ |
| 1 | 0.1356 | 0.1351 | 0.135 | 3.8738 | 3.6785 | 3.6738 |
| 1.5 | 0.6276 | 0.6217 | 0.6213 | 9.1006 | 7.8895 | 7.8626 |
| 2 | 2.324 | 2.2799 | 2.2766 | 19.9599 | 15.0592 | 14.9325 |
| 2.5 | 6.982 | 6.7069 | 6.6885 | 42.4468 | 25.5623 | 25.0368 |
| 3 | 17.4309 | 15.9878 | 15.8984 | 88.7695 | 38.8223 | 36.7474 |

Replacement-repair cost ratio is another important factor in determining the warranty cost. In Table 10.6, we report the results for various cost ratios for $w=$ $2.5, \alpha=0.9$ and $m=1$ while $c_{a}$ is fixed at 100 . It turns out that the cost ratio is positively related to both $E[C]$ and $\operatorname{std}(C)$, indicating that as replacement becomes more expensive compared to repair, the repair-limit warranty policy tends to be more costly with higher warranty cost risk.

Table 10.6. $E(C)$ and $\operatorname{std}(C)$ VS replacement-repair cost ratio

| $\mathrm{C}_{\mathrm{b}} / \mathrm{C}_{\mathrm{a}}$ | 2 | 10 | 50 | 100 | 300 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $E[C]$ | 6.6944 | 6.7493 | 7.0235 | 7.3662 | 8.7373 |
| $\operatorname{std}[C]$ | 25.0200 | 26.2891 | 48.308 | 86.4494 | 249.6575 |

# 10.3.5 Concluding Remarks 

Section 10.3 has discussed repair-limit risk-free warranty policies and provided the first and second moments of the warranty cost per unit sold by means of truncatedquasi-renewal processes. Warranty designers such as manufacturers are constantly in search of novel ideas to promote their products due to the more than ever fierce competition. This repair-limit risk-free warranty could be a good candidate for marketing purpose since it provides extra compensation to consumers suffering from low quality products with a relatively low cost.

The numerical examples assume that the failure time of a new product follows a normal distribution in order to simplify the computational efforts. More numerical studies are needed to include the cases when the failure time is modeled by nonnegative distributions such as the Weibull distribution or Gamma distribution.

# 10.4 Optimal RRLRFW Policies with Minimal Repair 

To gain some advantages in the highly competitive markets, manufacturers have to improve product quality continuously or to upgrade their products creatively. However, such strategies may be time consuming and very expensive. In comparison, a simple yet efficient alternative for the marketing purpose is to offer an attractive and comprehensive warranty. This leads to the question of designing and determining the optimal warranty policy. To make this problem more specific, this section focuses on a renewable repair-limit risk-free warranty (RRLRFW) for deteriorating repairable complex products:

Let $S_{i}, \forall i, i=1,2, \cdots, m+1$ be the failure arrival times of a new product (or a replacement) under the warranty. For this product, any failure within warranty duration $w$ will be repaired up to $m$ times. If $S_{m+1} \leq w$, then a replacement will be provided. The warranty is then automatically renewed for another period of $w$. All the warranty service is free of charge to the consumer.

This RRLRFW is denoted as $\varphi(w, m)$, and studied by Bai (2004). This policy has several attractive features. First, it is a generalization of the ordinary renewable free repair/replacement warranty (Blischke and Murthy 1994, p.144), often offered for inexpensive products. Obviously, when $m=0$, it degenerates to the latter. Second, this type of policies (when $m>0$ ) provides consumers better warranty service than the conventional free repair policies because it offers a new replacement whenever more than $m$ failures happened within a period of $w$, which may be a good indication that this particular product is of low quality or it does not worth being repaired any more. As a result, this policy could be applied for a wide range of products including expensive deteriorating systems. Third, the limit on the number of repairs presents producers the flexibility to control the warranty cost by choosing appropriate $m$ in addition to the usual decision variable $w$.

To analyze the warranty cost of RRLRFW policies, it is necessary to model the repair impact on product reliability or the failure rate. Section 10.3 has presented a warranty cost model for non-renewable repair-limit risk-free policies based on an imperfect repair assumption. Although the imperfect repair model is flexible in a sense that the repair effort is represented by a parameter in $(0,1]$, it may not beeasy for implementation due to the difficulty in estimating the parameter accurately. In contrast, minimal repair models have been studied extensively. This section assumes that repairs are minimal.

To determine the optimal RRLRFW policy, one has to assess quantitatively the benefit that a manufacturer might generate from a specific warranty. Usually there are two channels that producers could benefit from issuing a warranty: warranty pricing, which is an integrated part of product pricing strategy, and increase in sales or demand. In this section, we focus on the second channel since one of the main reasons of the existence of warranty is to promote sales instead of making extra profit per unit sold from warranty directly. Besides, many producers, as the so-called price takers, do not have the pricing power. For example, they may have to set the price equal or very close to that of the products with similar functionality of the competitors. The majority of the warranty literature focuses on warranty cost modeling and analysis for producers or consumers, and only a few study the demand side of warranty. Menezes (1992) posits a general deterministic demand function depending on price, warranty length, quality and many other economic factors, based on which the optimal warranty length was derived for profitmaximizing producers. Chun and Tang (1995) model consumers' acceptance of warranty through a general probability distribution of consumers' perception on product quality, which was represented by an exponential distribution. A linear form and a quadratic form of $w$, the warranty period, are employed by Thomas $(1983,1989)$ to model the warranty benefit directly. Alternatively, we propose a logistic regression model to estimate the demand of products with warranty.

The rest of this section is organized as follows: Section 10.4.1 gives a general optimization model for producers to determine the optimal warranty policy. The consumers are assumed to be homogeneous, thus the probability of accepting a warranted product is invariant among all consumers. A logistic regression model is used to determine the probability. For producers without the pricing power, their objective is to maximize the expected utility of the profit, generated from the products sold with warranty, by selecting appropriate parameters of the warranty based on the forecast of customers' demand. Section 10.4.2 discusses the warranty cost analysis of RRLRFW policies from manufacturers' perspective and some useful properties of the warranty cost per unit sold. These results combined with the optimization model are then used in Section 10.4.3 to determine the optimal RRLRFW through a numerical example. Section 10.4.4 discusses the limitations of the model and some future research directions. Following are assumptions in this section:
i) Any warranty service is instantaneous.
ii) All warranty claims are valid.
iii) All failures covered by warranty are claimed.
iv) Consumers are homogeneous.
v) Replacement products follow the same failure time distribution as of a new product.
vi) Any repairs under warranty are minimal.# 10.4.1 A General Optimization Model 

In this section, we present a general decision model for manufacturers to determine the optimal warranty policy $\psi\left(\Theta^{*}\right)$, where $\Theta^{*}=\left\{\theta_{1}^{*}, \theta_{2}^{*}, \cdots, \theta_{n}^{*}\right\}$ is the optimal set of the parameters of $\psi$. One may use either $\psi^{*}$ or $\Theta^{*}$ to represent the optimal policy. Let us suppose that the manufacturer has a utility function $U(\cdot)$, therefore his or her objective is to maximize the expected monetary utility of the profit, $\pi$, by choosing appropriate parameters of $\psi(\Theta)$.

### 10.4.1.1 Profit Per Unit Sold

Let's consider the situation that a typical producer, $M$, faces the problem of determining optimal parameters of a certain warranty policy $\phi(\Theta)$ for a certain product $A$, for which the market base, or the number of potential customers is $B$. In a competitive market with sufficient number of producers, producer $M$, as one of many other manufacturers in the market, may not have the pricing power. So, assume $M$ is a price-taker, implying that the price of product $A$ is exogenous. Due to technology constraints or the time constraint, it is possible that $M$ cannot reduce the production cost in a short time, so it is reasonable to assume that the production cost is a constant. As a result, the profit margin per unit not accounting for the future warranty cost, denoted as $\Delta P$, is a constant, which is assumed to be known by $M$.

The warranty cost per unit sold of product $A$ under the $\psi(\Theta)$ can be represented by $C(\Theta)$, a r.v. depending on $\Theta$. It should be noted that the quality of the product, represented by a distribution function $F$, surely will affect the warranty cost. However, it is not necessary to include $F$ explicitly here as long as $M$ has the complete knowledge of the quality. As a result, the profit per unit sold of product $A$ is $\Delta P-C(\Theta)$, also a r.v., due to the randomness of $C(\Theta)$.

### 10.4.1.2 Consumer's Responses

For homogeneous consumers in the customer base $B$, it is assumed that the probability $p_{c}$ of purchasing product $A$ solely depends on $\Theta$, invariant among all the potential consumers. Therefore, $p_{c}$ could be obtained by solving equation $h\left(p_{c}\right)=k(\Theta)$, where $h(\cdot)$ is the so-called link function and $k(\Theta)$ may be assumed to be a linear function of the elements in $\Theta$, i.e.,

$$
k(\Theta)=\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}
$$

There are many choices for link function $h(\cdot)$. This section considers the commonly used logit link function $h\left(p_{c}\right)=\ln \left(p_{c} /\left(1-p_{c}\right)\right)$ (see Stokes 2000). Thus,

$$
\ln \left(\frac{p_{c}}{1-p_{c}}\right)=\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}
$$From Equation (10.80), it is easy to obtain that

$$
p_{c}=\frac{\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}{1+\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}
$$

Note that $\beta_{0}$ could be interpreted as the baseline logarithm of the odds: the ratio of $p_{c}$ to $\left(1-p_{c}\right)$, for the products without warranty. Similarly, $\beta_{i}, i=1,2, \cdots, n$ is the change in the logarithm of the odds due to the unit change of $\theta_{i}$.

Let $D$ be the demand of product $A$ covered by $\psi(\Theta)$. It's easy to see that $D$ follows a binomial distribution. The total units expected to sell under the $\psi(\Theta)$ is given by

$$
E[D]=B \frac{\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}{1+\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}
$$

and the variance of $D$ is

$$
V[D]=B \frac{\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}{\left[1+\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)\right]^{2}}
$$

If consumers are not homogeneous in a sense that they can be classified to several categories according to their personal profiles such as the risk attitude, the knowledge of the product, and the desire of the product, it is still possible to forecast the demand by fitting a logistic regression model for each category based on survey data or some historical data if available. However, such an extension is beyond the scope of this section.

# 10.4.1.3 A General Decision Model 

The producer's profit $\pi$ can be expressed as $\sum_{i=1}^{D}\left(\Delta P-C_{i}\right)$, where $C_{i}$ is the future warranty cost to the producer due to the $i^{\text {th }}$ sale. Under the $\psi(\Theta)$, $C_{i}, i=1,2, \cdots$, are i.i.d., following the same distribution as $C(\Theta)$. Assuming statistical independence between $D$ and $C_{i}$, we then have

$$
E[\pi]=B \frac{\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}{1+\exp \left(\beta_{0}+\beta_{1} \theta_{1}+\beta_{2} \theta_{2}+\cdots+\beta_{n} \theta_{n}\right)}(\Delta P-E[C(\Theta)])
$$

So the problem of determining the optimal warranty policy $\psi\left(\Theta^{*}\right)$ can be formulated as

$$
\begin{array}{ll}
\operatorname{Maximize}_{\theta_{i}, i=1,2, \cdots, n} & E[U(\pi)] \\
\text { Subject to } & \left\{\begin{array}{l}
P\left[\sum_{i=1}^{D} C_{i} \geq R_{0}\right] \leq \varepsilon \\
\theta_{i}^{l} \leq \theta_{i} \leq \theta_{i}^{u}, \quad i=1,2, \cdots, n
\end{array}\right.
\end{array}
$$The first constraint is about the warranty budget $R_{0}$. Warranty managers usually require that the probability of the total warranty cost over the budget is controlled within $\varepsilon$, a pre-determined risk acceptance level. The second set of constraints defines the acceptable ranges of $\theta_{i}, i=1,2, \cdots, n$, which are usually affected by the reliability (quality) requirements and the competitors' strategy. Other constraints may also be included depending on individual applications.

If $M$ is risk-neutral, implying that $U(\pi)$ is a linear function of $\pi, E[\pi]$ becomes the objective function, which is given in Equation (10.84). The constraints remain the same.

# 10.4.2 Cost Analysis of RRLRFW Policy 

From the general optimization model illustrated in Section 10.4.1, it is clear that one of the main sources of the randomness is from the warranty cost per unit sold $C(\Theta)$. This section focuses on the RRLRFW with two parameters $w$ and $m$ for which $\Theta=\{w, m\}$, and will derive some useful statistical properties of $C(w, m)$ given minimal repairs. Such a situation is not rare for complex systems that are aging over time. Besides, manufacturers usually will not take extra effort to make a repaired system better than old unless they are required to do so. It is also assumed replacement products have the same failure time distribution as that of the original product.

Let $T$ represent the warranty cycle of $\psi(w, m)$, starting from the date of a sale, ending at the warranty expiration date. Since $\psi(w, m)$ is renewable, $T$ is actually an r.v. Denote $N_{a}(w, m)$ as the total number of renewals of the warranty, and let $t_{1}, t_{2}, \cdots, t_{N_{a}(w, m)}$ be the corresponding inter-arrival renewal times, then $T$ can be expressed as

$$
T=\left\{\begin{array}{cl}
w, & \text { for } N_{a}(w, m)=0 \\
t_{1}+t_{2}+\cdots+t_{N_{a}(w, m)}+w, & \text { for } N_{a}(w, m)=1,2, \cdots
\end{array}\right\}
$$

The total warranty cost per item sold, or per cycle, $C(w, m)$, can be formulated as

$$
C(w, m)=\left(c_{a}+c_{f}\right) N_{a}(w, m)+\left(c_{b}+c_{f}\right) N_{b}(w, m)
$$

where $N_{b}(w, m)$ is the total number of minimal repairs within $T . c_{a}$ and $c_{b}$ are the replacement cost and repair cost per unit respectively. $c_{f}$ represents the fixed cost per warranty service, which may include warranty managerial cost, handling cost, disposal cost, advertising cost, and so forth. $c_{a}, c_{b}$ and $c_{f}$ are assumed to be constant.

Define $N_{b}^{\prime}(w, m)$ as the number of minimal repairs in the last warranty period $w$, then the relationship between $N_{a}(w, m)$ and $N_{b}(w, m)$ can be written as

$$
N_{b}(w, m)=m N_{a}(w, m)+N_{b}^{\prime}(w, m)
$$Using Equation (10.86), $C(w, m)$ can be re-written as

$$
C(w, m)=\left[c_{a}+m c_{b}+(m+1) c_{f}\right] N_{a}(w, m)+\left(c_{b}+c_{f}\right) N_{b}^{\prime}(w, m)
$$

To simplify the notion, we will suppress $w$ and $m$ later on whenever appropriate. The expectation of $C$, denoted as $\mu_{\psi}$, is given by

$$
\mu_{\psi}=\left[c_{a}+m c_{b}+(m+1) c_{f}\right] E\left[N_{a}\right]+\left(c_{b}+c_{f}\right) E\left[N_{b}^{\prime}\right]
$$

The variance of $C, \sigma_{\psi}^{2}$, is

$$
\sigma_{\psi}^{2}=\left[c_{a}+m c_{b}+(m+1) c_{f}\right]^{2} V\left[N_{a}\right]+\left(c_{b}+c_{f}\right)^{2} V\left[N_{b}^{\prime}\right]
$$

It should be noted that Equation (10.89) holds since $N_{b}^{\prime}$ is independent of $N_{a}$, which can easily be proved through a conditioning argument.

We need the following lemma from Baxter (1982):

LEMMA 10.5 Let $S_{m+1}$ be the $(m+1)^{\text {th }}$ arrival failure time of a new or replacement product under the warranty, which is also the $(m+1)^{\text {th }}$ arrival time of the underlying NHPP associated with $\Lambda$. Let $G_{m+1}$ and $g_{m+1}$ be the cdf and pdf of $S_{m+1}$ respectively. Then

$$
\begin{aligned}
& G_{m+1}(x)=1-e^{-\Lambda(x)} \sum_{i=0}^{m} \frac{[\Lambda(x)]^{i}}{i!} \\
& g_{m+1}(x)=\lambda(x) e^{-\Lambda(x)} \frac{[\Lambda(x)]^{m}}{m!}
\end{aligned}
$$

Next we derive some useful properties of $N_{a}$ and $N_{b}^{\prime}$. The following notation is used: $p_{i}^{N_{a}}=P\left[N_{a}=i\right] ; p_{i}^{N_{b}}=P\left[N_{b}^{\prime}=i\right] ; F$ is the $c d f$ of the first failure time of a new product or a replacement. Accordingly, the accumulative failure rate function, $\Lambda$, is $\Lambda=-\ln (1-F)$, and the failure rate function is $\lambda=d F /(1-F)$.

Proposition 10.3 The first two centered moments of $N_{a}$ are given by

$$
\begin{aligned}
& E\left[N_{a}\right]=\frac{G_{m+1}(w)}{1-G_{m+1}(w)} \\
& V\left[N_{a}\right]=\frac{G_{m+1}(w)}{\left[1-G_{m+1}(w)\right]^{2}}
\end{aligned}
$$

Proof. It is not difficult to see that under the $\psi(w, m)$, the warranty will not expire until the first time that $S_{m+1}>w$. Thus the total number of renewals, $N_{a}$, follows a geometric distribution of parameter $1-G_{m+1}(w)$. Based on the propertiesof geometric distribution, the result then follows.

Proposition 10.4 The probability mass function (pmf) of $N_{b}^{\prime}$ is given by

$$
\begin{aligned}
& p_{i}^{N_{b}^{\prime}}=e^{-\Lambda(w)} \frac{(\Lambda(x))^{i}}{i!}, \quad \forall i, i=0,1, \cdots, m-1 \\
& p_{m}^{N_{b}^{\prime}}=1-\sum_{i=0}^{m-1} e^{-\Lambda(w)} \frac{(\Lambda(x))^{i}}{i!}=G_{m}(w)
\end{aligned}
$$

The expectation of $N_{b}^{\prime}$ is

$$
E\left[N_{b}^{\prime}\right]=m-e^{-\Lambda(w)} \sum_{i=0}^{m-1}(m-i) \frac{(\Lambda(x))^{i}}{i!}
$$

and the variance of $N_{b}^{\prime}$ follows

$$
V\left[N_{b}^{\prime}\right]=m^{2}-e^{-\Lambda(w)} \sum_{i=0}^{m-1}\left(m^{2}-i^{2}\right) \frac{(\Lambda(w))^{i}}{i!}-\left(E\left[N_{b}^{\prime}\right]\right)^{2}
$$

Proof. Since any failed product under warranty will be minimally repaired up to $m$ times, the failure process $\left\{N_{a}(t), t<0\right\}$ forms an NHPP truncated above $m$ with the accumulative failure rate function $\Lambda$. By realizing that the truncation does not make any change to the pmf of the underlying ordinary Poisson random variable when it is less or equal to $m-1$, we obtain Equation (10.94). Equation (10.95) holds due to the relationship that $P\left[N_{b}^{\prime}=m\right]=P\left[S_{m} \leq w\right]$. Equations (10.96) and (10.97) can be verified easily using the $p m f$ of $N_{b}^{\prime}$.

Now it is ready to give the expressions of the first two centered moments of $C$.
Proposition 10.5 The first two moments of the warranty cost per unit sold are

$$
\begin{aligned}
\mu_{\psi}= & {\left[c_{a}+m c_{b}+(m+1) c_{f}\right] \frac{G_{m+1}(w)}{1-G_{m+1}(w)} } \\
& +\left(c_{b}+c_{f}\right)\left(m-e^{-\Lambda(w)} \sum_{i=0}^{m-1}(m-i) \frac{(\Lambda(w))^{i}}{i!}\right) \\
\sigma_{\psi}^{2}= & {\left[c_{a}+m c_{b}+(m+1) c_{f}\right]^{2} \frac{G_{m+1}(w)}{\left(1-G_{m+1}(w)\right)^{2}} } \\
& +\left(c_{b}+c_{f}\right)^{2}\left\{\left(m^{2}-e^{-\Lambda(w)} \sum_{i=0}^{m-1}\left(m^{2}-i^{2}\right) \frac{[\Lambda(w)]^{i}}{i!}\right.\right. \\
& \left.-\left[m-e^{-\Lambda(w)} \sum_{i=0}^{m-1}(m-i) \frac{[\Lambda(w)]^{i}}{i!}\right]^{2}\right\}
\end{aligned}
$$

Proof. The proof is straightforward, thus omitted here.# 10.4.3 Optimal RRLRFW Policy 

This sections uses the optimization model in Section 10.4.1 to determine the optimal RRLRFW policy. In particular, we assume that the seller is risk neutral; therefore, the optimal warranty policy is determined by maximizing the expected profit under some constraints. Using the results in Section 10.4.2, the model becomes

$$
\begin{aligned}
& \operatorname{Maximize}_{(w, m)} B \frac{\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}{\left[1+\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)\right.} \begin{array}{c}
\left[\Delta P-\left[c_{a}+m c_{b}+(m+1) c_{f}\right] \frac{G_{m+1}(w)}{1-G_{m+1}(w)}\right. \\
\left.+\left(c_{b}+c_{f}\right)\left(m-e^{-\Lambda(w)} \sum_{i=0}^{m-1}(m-i) \frac{[\Lambda(w)]^{i}}{i!}\right)\right] \\
& \text { Subject to } \quad\left\{\begin{array}{l}
P\left[\sum_{i=1}^{D} C_{i} \geq R_{0}\right] \leq \varepsilon \\
w^{l} \leq w \leq w^{n} \\
m \in\{1,2, \cdots\}
\end{array}\right.
\end{aligned}
$$

The above formulation is a non-linear optimization problem, which can be solved by non-linear optimization software, except that the first constraint requires the knowledge of the distribution of TC, defined as $T C=\sum_{i=1}^{D} C_{i}$. Next we simplify the constraint.

Since $D$ follows a binomial distribution, and $C_{i}, i=1,2, \cdots$, are i.i.d.., TC actually follows a compound binomial distribution, for which usually there is no close form expression and the computation is difficult in general. Several recursive algorithms exist to compute the exact distribution function (see Sundt 2002). This section considers a simple approximation of the compound binomial distribution by a normal distribution (Rolski et al. 1999) with parameters $\mu_{T C}$ and $\sigma_{T C}^{2}$, the mean and variance of TC respectively. It can easily be verified that

$$
\begin{aligned}
\mu_{T C}= & B \frac{\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}{1+\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}\left\{\left[c_{a}+m c_{b}+(m+1) c_{f}\right] \frac{G_{m+1}(w)}{1-G_{m+1}(w)}\right. \\
& \left.+\left(c_{b}+c_{f}\right)\left\{\left(m-e^{-\Lambda(w)} \sum_{i=0}^{m-1}(m-i) \frac{[\Lambda(w)]^{i}}{i!}\right)\right\}\right. \\
\sigma_{T C}^{2}= & B \frac{\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}{1+\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}\left\{\left[c_{a}+m c_{b}+(m+1) c_{f}\right]^{2} \frac{G_{m+1}(w)}{\left[1-G_{m+1}(w)\right]^{2}}\right. \\
& +\left(c_{b}+c_{f}\right)^{2}\left\{m^{2}-e^{-\Lambda(w)} \sum_{i=0}^{m-1}\left(m^{2}-i^{2}\right) \frac{[\Lambda(w)]^{i}}{i!}-\frac{1}{1+\exp \left(\beta_{0}+\beta_{1} w+\beta_{2} m\right)}\right.
\end{aligned}
$$$$
\begin{aligned}
& \left(\left(c_{a}+m c_{b}+(m+1) c_{f}\right) \frac{G_{m+1}(w)}{1-G_{m+1}(w)}+\left(c_{b}+c_{f}\right)\left(m-e^{-\Lambda(w)}\right.\right. \\
& \left.\left.\times \sum_{i=0}^{m-1}(m-i) \frac{[\Lambda(w)]^{i}}{i!}\right)\right)^{2}\right\}
\end{aligned}
$$

Using Equations (10.100) and (10.101), and the normal approximation, the first constraint can be rewritten as

$$
R_{0}-\mu_{T C}-z_{\alpha} \sigma_{T C} \geq 0
$$

where $z_{\alpha}$ is the $(1-\alpha)$ quantile of the standard normal distribution.

Now the optimization problem has been converted into a standard non-linear optimization problem. Let's see a numerical example.

Suppose a warranty manager, with a warranty budget $R_{0}=\$ 4000$ and $\alpha=10 \%$, has decided to offer an RRLRFW. He (she) would like to consider $w \in[1,20]$ and $m \in\{1,2,3,4,5\}$. The objective is to determine the optimal warranty parameters $w^{*}$ and $m^{*}$ such that the expected profit is maximized while the constraints are satisfied. The customer base is estimated to be 10,000 . Through the data from a market survey, he estimated that parameters $\beta_{0}, \beta_{1}$, and $\beta_{2}$ are $0.4217,0.0141$ and -0.2012 respectively. The profit margin per unit is known to be $\$ 500$. The reliability function of the product is given by $\exp \left(-t^{1.07} / 247.16\right)$. The fixed warranty service cost per service $c_{f}$ is $\$ 50$, the replacement cost $c_{a}$ and repair cost $c_{b}$ are $\$ 10,000$ and $\$ 150$ respectively.

The optimal RRLRF policy is found: $w^{*}=9.5$ and $m^{*}=2$, for which the expected total profit is $\$ 1605,624$, the expected warranty cost per unit sold is $\$ 19.5$, and the corresponding standard deviation is 330.61 . It should be noted that the standard deviation is much higher than the expectation since the policy under consideration is renewable.

If there is no warranty budget constraint, then the optimal policy is given by $w^{*}$ $=13.2$ and $m^{*}=2$. The corresponding expected profit is $\$ 1,613,313$.

# 10.4.4 Remarks 

Among many warranty management problems, how to determine the optimal warranty policy that may help manufacturers to gain some advantage in the competitive market is a fundamental one. This section has provided a general optimization model for this problem. However, it should be noted that there are some limitations on this model. First, this optimization model deals with the demand of a warranted product through a logistic link function which only depends on the warranty parameters. Empirical study such as consumer surveys is needed to estimate the proposed link function. Second, the optimization model only considers the homogeneous consumers. The case of non-homogeneous consumers needs tobe examined. Third, if the manufacturer is not a price taker, then the product price should be included as one of the decision variables. Fourth, only minimal repair is considered in this section. Other situations such as imperfect repair can be studied.

This section has presented some useful results that can be applied to determine the optimal RRLRFW policy. A numerical example is provided for illustration purposes. One natural extension is to apply this approach to other warranty policies such as a two-dimensional warranty or a combination warranty. Other generalizations of the RRLRFW policy may be considered. For example, Bai (2004) suggests use of the quasi renewal process to study the renewable repair-limit risk-free warranty.

Let $S_{i}, i=1,2, \cdots, m+1$ be the failure arrival times of a new product (or a replacement) under the warranty, which has been renewed for $j$ times, $j=1,2, \ldots$ For this product, any failure within a period of $w_{j}$ will be repaired up to $m$ times. If $S_{m+1} \leq w_{j}$, then a replacement will be provided. The warranty is then renewed for another period of $w_{j+1}$. The relationship between $w_{j}$ and $w_{j+1}$ is given by $w_{j+1}=\gamma w_{j}$, where $\gamma \in(0,1]$, and $w_{0}=w$. All the warranty service is free of consumers.

Compared to an RRLRFW policy, the above policy is more general since it degenerates to the former when parameter $\gamma=1$. It would be interesting to investigate the statistical properties of this warranty policy.

# 10.5 On Warranty Policies and their Comparison 

Warranty managers usually have several choices among various warranty policies. This requires some basic measures as the criteria to make the comparison among these policies. Bai and Pham (2006b) and Mi (1999) discuss comparison of different warranties and some criteria, and following them we will compare various warranty policies in this section.

For a warranty policy, there are several measures available including EWC, expected DWC, monetary utility function and weighted objective function. EWC and expected DWC are more popular than others since they are easy to understand and can be estimated relatively easily. The key difference between them is that the latter considers the value of time, an important factor for the determination of warranty reserve.

Monetary utility function, $U(x)$, is a better candidate for the purpose of comparing warranty policies. The functional form of $U(x)$ reflects seller's risk attitude. If a seller is risk-neutral, then $U(x)$ is linear in $x$. This implies that maximizing $\mathrm{E}[U(x)]$ is the same as maximizing $U(\mathrm{E}[x])$. However, manufacturers may be risk-averse if they are concerned about the variations in profit or in warranty cost. For example, a particular seller may prefer a warranty with less warranty cost variation than another with much larger variation in warranty cost while the difference between the EWCs is small. If this is the case, then it can be shown that that the corresponding utility function is concave (Kreps 1990). Themain difficulty of the utility theory approach is that utility functions are subjective.
Weighted objective functions could also be used in the comparison of warranties. One commonly used weighted objective function is $E[\pi(x)]-$ $\rho V[\pi(x)]$, where $\rho$ is a parameter representing the subjective relative importance of the risk (variation) against the expectation and $\pi(x)$ is the manufacturers' profit for a given warranty policy $x$. Interestingly, such an objective function coincides to a special case of the utility theory approach when the manufacturers' subjective utility function only depends on the first and the second moments of $\pi(x)$ (Markowitz 1959, p.126).

According to compensation methods specified in a warranty contract upon premature failures, there are three basic types of warranties: free replacement warranty (FRW), free repair warranty (FRPW), and pro-rata warranty (PRW). Combination warranty (CMW) contains both features of FRW/FRPW and PRW, which often has two warranty periods, a free repair/replacement period followed by a pro-rata period. Full-service warranty (FSW), also known as PM warranty, is a policy that may be offered for expensive deteriorating complex products such as automobiles. Under this type of policy, consumers not only receive free repairs upon premature failures, but also free (preventive) maintenance.

For non-repairable products, usually the failed products under warranty will be replaced free of charge to consumers. Such a policy is often referred as a free replacement warranty or a unlimited warranty. In practice, even if a product is technically repairable, sometimes it will be replaced upon failure since repair may not be economically sound. As a result, for inexpensive repairable products, warranty issuers could simply offer FRW policies. Consequently, those inexpensive repairable products can be treated as non-repairable. However, for repairable products, if the warranty terms specify that upon a valid warranty claim, the warranty issuer will repair the failed product to working condition free of charge to buyers, then such a policy is the so-called free repair warranty. In practice, it is not rare that a warranty contract specifies that the warranty issuer would repair or replace a defective product under certain conditions. This is the reason why most researchers do not treat FRW and FRPW separately. Nevertheless, it is necessary to differentiate these two types of policies based on the following reasoning: first, repair cost is usually much lower than replacement cost unless for inexpensive products; second, by clearly defining the compensation terms, warranty issuers may establish a better image among consumers, which can surely be helpful for the marketing purpose.

Under an FRW policy, since every failed product within $T$ is replaced by a new one, it is reasonable to model all the subsequent failure times by a single probability distribution. However, under an FRPW, it is necessary to model the repair impact on failure times of a warranted product. If it is assumed that any repair is as-good-as-new (perfect repair), then from the modeling perspective, there is little difference between FRW and FRPW. For deteriorating complex systems, minimal repair is a commonly used assumption, as discussed in Chapter 2. In warranty literature, the majority of researchers consider repairs as either perfect or minimal. Little has been done on warranty cost analysis considering imperfect repair.Both FRW and FRPW policies provide full coverage to consumers in case of product failures within $T$. In contrast, a PRW policy requires that buyers pay a proportion of the warranty service cost upon a failure within $T$ in exchange for the warranty service such as repair or replacement, cash rebate or discount on purchasing a new product. The amount that a buyer should pay is usually an increasing function of the product age (duration after the sale). PRW policies are usually renewable, and offered for relatively inexpensive products like tires, batteries, and so forth.

Generally speaking, FRW and FRPW policies are in favor of buyers since manufacturers take all the responsibility of providing products that function properly during the whole warranty cycle (Blischke and Murthy 1994, p.221). In other words, it is the manufacturers that bear all the warranty cost risk. In contrast, for PRW policies manufacturers have the relative advantage with regard to the warranty cost risk. Although they do have to offer cash rebate or discounts to consumers if failures happen during $T$, they are usually better off no matter what consumers choose to do. If a consumer decides not to file a warranty claim, then the manufacturer saves himself the cash rebate or other types of warranty service. If instead a warranty claim is filed, the manufacturer might enjoy the increase in sales or at least the warranty service cost is shared by the consumer.

CMW can be used to balance the benefits between buyers and sellers, and is a policy that usually includes two warranty periods: a free repair/replacement period $w_{1}$ followed by a pro-rata period $w_{2}$. This type of warranty is not rare today because it has significant promotional value to sellers while at the same time it provides adequate control over the costs for both buyers and sellers (Blischke and Murthy 1996, p.12).

For deteriorating complex products, it is essential to perform PM to achieve satisfactory reliability performance. The burden of maintenance is usually on the consumers' side. Section 10.1 has discussed a renewable full-service warranty for multi-component systems under which the failed component(s) or subsystem(s) will be replaced, in addition, a PM action will be performed to reduce the chance of future product failures, both free of charge to consumers. Such a policy may be desirable for both consumers and manufacturers since consumers receive better warranty service compared to the traditional FRPW policies, at the same time manufacturers may enjoy cost savings due to the improved product reliability by the maintenance actions.

In the maintenance literature, many researchers studied maintenance policies set up in such a way that different maintenance actions may take place depending on whether or not some pre-specified limits are met. Three types of limits are usually considered: repair-number-limit, repair-time-limit, and repair-cost-limit, and these maintenance policies are summarized in Chapter 3. Similarly, three types of repairlimit warranties may be considered by manufacturers: repair-number-limit warranty (RNLW), repair-time-limit warranty (RTLW), and repair-cost-limit warranty (RCLW). Under a RNLW, the manufacturer agrees to repair a warranted product up to $m$ times within a period of $w$. If there are more than $m$ failures within $w$, the failed product shall be replaced instead of being repaired again. Section 10.3 has discussed this kind of policy under the imperfect repair assumption.An RTLW policy specifies that within a warranty cycle $T$, any failures shall be repaired by the manufacturer, free of charge to consumers. If a warranty service cannot be completed within a certain time, then a penalty cost occurs to the manufacturer to compensate the inconvenience of the consumer. This policy was analyzed by Murthy and Asgharizadeh (1999) in the context of maintenance service operation.

An RCLW policy has a repair cost limit in addition to an ordinary FRPW policy, i.e., upon each failure within the warranty cycle $T$, if the estimated repair cost is greater than a fixed number, then replacement instead of repair shall be provided to the consumer; otherwise, normal repair will be performed. This policy has been studied by Nguyen and Murthy (1989) and others.

Possible new warranty policies are those that combine various repair limits as well as other warranty characteristics such as renewing to define a new complex warranty. For example, it is possible to have a renewable repair-time-limit warranty for complex systems. Such combinations define a large set of new warranty policies that may appear in the market in the future.

In addition, most warranties in practice are one-attribute for which the warranty terms are based on either product age or product usage, but not both. Compared to one-attribute warranties, two-attribute warranties are more complex since the warranty obligation depends on both product age and product usage as well as the potential interaction between them. Two-attribute warranties are often seen in the automobile industry. For example, one automobile company, is currently offering 10 years/100,000 miles limited FRPW on the power train for their new car models in North America. Comparison and analysis of two-attribute warranties can be found in Murthy et al. (1995) and Singpurwalla and Wilson (1993).# Software Reliability, Cost, and Optimization Models 

Practice over the years has shown that a software development process using software reliability models instead of traditional project management methods is efficient and effective to produce reliable software at low cost. This chapter models software reliability and debugging costs using the quasi-renewal process, and discusses optimal software testing and release policies, following Pham and Wang (2001). Several software reliability and cost models are presented in which successive error-free times are independent and increasing by a fraction, i.e., they form an increasing quasi-renewal process. It is assumed that the cost of fixing a fault consists of deterministic and incremental random parts, and is increasing with the number of faults removed. The maximum likelihood estimates of parameters associated with these models are provided. Based on the valuable properties of quasi-renewal processes, the expected software testing and debugging cost, number of residual faults in the software, and mean error-free time upon testing are obtained. A class of related optimization problems are then contemplated, and optimum testing policies incorporating both reliability and cost measures are discussed. Finally, numerical examples are presented through a set of real testing, showing satisfactory results. The models in this chapter can also apply to modeling field reliability growth and maintenance cost.

### 11.1 Introduction

Research activities in software reliability have been conducted for the past several decades, and are still going on today because critical software applications are increasing in size and complexity. Since software is an interdisciplinary science, software reliability and cost models are developed from different perspectives towards software and with various applications. So far many software reliability models have been developed respectively by using nonhomogeneous Poisson processes, Markov processes, binary Markov processes, Bayesian statistics, classical statistics, input-domain-based methods, etc., as shown in Musa et al. (1987), Xie (1991), Downs (1985), Goel (1985), Pham (2000), and Lyn (1996). However, there is still a great need to develop more practical and realistic modelsto estimate software reliability and testing costs, and to determine the desired reliability level before releasing it (Pham 2003b; Lyn 1996). The key modeling approaches and a critical analysis of underlying assumptions, limitations, and applicability of some previous software models during the software development cycle are discussed in Goel (1985). A quasi-renewal process is a new tool to facilitate modeling of both software reliability and testing costs (Pham and Wang 2001).

Software testing is an efficient and necessary way to remove faults in software products. However, exhaustive testing of all possible executable paths in a large program may be impractical. Debugging and testing reduce the error content but increase the development costs. In fact, after reaching a certain level of software refinement, further efforts to increase reliability will result in exponential increase in cost and debugging time (Pham 2000). Therefore, it is important to determine when to stop testing, or when to release the software to customers. One might consider what questions a software model should help answer for software developers and managers. The important questions are (Lyn 1996; Pham and Wang 2001):
i) What would the failure rate of the software be if released now?
ii) How many faults remain in the software? How many high severity faults? Fault location (subsystem)?
iii) How much more testing is needed to achieve software reliability targets? How should resources be scheduled to ensure the on-time and efficient delivery of a software product? Is the software product sufficiently reliable for release?

This chapter aims to present software reliability models which will help answer the above questions. Unlike most previous work, this chapter determines the optimal software release time based on two criteria: reliability of the released software and total software cost. In addition to the traditional software testing measures, software error-free time information upon testing is also provided in the models in this chapter. In fact, some unique properties of the quasi-renewal process ease modeling it. This chapter assumes the cost of fixing a fault during the software testing phase consists of deterministic and probabilistic parts, and grows as the number of faults removed increases. Obviously, this assumption is realistic because usually it may become difficult to fix a fault which is detected in the later testing phases. Besides, cost of testing per unit time is considered in this chapter, which is treated as a random variable. The second model in this chapter contemplates that in software there exist three types of faults which are classified in terms of failure effects and severities.

In Section 11.2, the quasi-renewal process is discussed with regard to its application in software reliability growth. Section 11.3 models software reliability and testing cost through the quasi-renewal process, and then investigates the optimal software testing policies by some numerical examples using a set of real testing data. Some concluding remarks are made in Section 11.4.# 11.2 Use of Quasi-renewal Process in Software Reliability 

In ordinary renewal process, the times between successive events are supposed to be independently and identically distributed (i.i.d.). As discussed in Chapter 4, a general renewal process, including ordinary renewal process as special case, is the quasi-renewal process. The quasi-renewal process is motivated by imperfect repair processes of hardware and in turn finds wide applications in modeling hardware maintenance as shown in Chapter 4. This chapter will use quasi-renewal process to model software reliability growth and testing costs.

Recall that Theorem 4.2 in Chapter 4 implies that after "renewal" the shape parameters of the inter-arrival times will not be changed. In reliability theory, shape parameters of lifetime of a hardware product tend to relate to its failure mechanism. Usually, a product will have the same shape parameters at different operating conditions if it possesses the same failure mechanism. Therefore, the use of a quasi-renewal process is generally justified in the maintenance process of a hardware system. The assumption that software debugging and testing or field use do not change the type of the error-free time distribution seems plausible. Note that the error-free times in the software during debugging phase or field use will have the same shape parameters, if modeled by a quasi-renewal process. In this sense a quasi-renewal process will be plausible to model the software reliability growth.

Recall from Section 4.1.1

$$
\lim _{n \rightarrow \infty} \frac{E\left(X_{1}+X_{2}+\cdots+X_{n}\right.}{n}=\lim _{n \rightarrow \infty} \frac{\mu_{1}\left(1-\alpha^{n}\right)}{(1-\alpha) n}= \begin{cases}0 & \text { when } \alpha<1 \\ +\infty & \text { when } \alpha>1\end{cases}
$$

Therefore, if the inter-arrival time represents the error-free time of a software system the average error-free time goes to infinite while its debugging process is going on forever. This conclusion seems reasonable because the faults in the software become generally less and less while it is subject to testing and debugging. When the debugging time is infinitely long, no faults in this software can be expected. Thus, the average error-free time and the error-free time is infinite as the debugging time goes to infinity. In practice, we can expect the error-free time of software upon testing is very large if the testing time is sufficiently long. In fact, Theorem 4.1 shows that if the first error-free time of software is DFR, then the successive error-free times are DFR. Therefore, in this case the failure rate of software can be expected to be smaller and smaller as faults in the software are being removed. The same arguments are true for software reliability growth during field use if faults found in field are also removed.

### 11.3 Software Reliability and Cost Modeling

If the inter-arrival time represents the error-free time (time between errors), a quasi-renewal process can be used to model reliability growth for software. Next we will utilize this quasi-renewal process to investigate software reliability and testing costs. Throughout this chapter we assume- All faults of software are independent.
- All detected faults are removed immediately and no new faults are introduced.


# 11.3.1 Model 1 

Suppose that all faults of software have the same chance of being detected. If the inter-arrival times of a quasi-renewal process represent the error-free times of software, the expected cumulative number of software faults in $[0, t)$ can be described by the quasi-renewal function $M(t)$ with parameter $\alpha>1$. Denote by $\bar{M}(t)$ the number of remaining software faults at time $t$. It follows that

$$
\bar{M}(t)=M(\tau)-M(t)
$$

where $M(\tau)$ is the number of faults which can be detected through a long testing time $\tau$, relative to $t$. We suggest taking $\tau \geq 6 t$ in practice. In fact, this choice is somewhat arbitrary and the actual selection can also be determined through experience. However, any choice should make the difference between $M(\tau)$ and $M(\tau+\Delta)$ to be insignificant for any small value of $\Delta$.

Assume that the cost of fixing software fault $i$ is a random variable and consists of two parts - deterministic part $c_{0}$ and incremental random part $(i-1) W$ :

$$
c_{i}=c_{0}+(i-1) W \quad \forall i, i=1,2,3, \ldots
$$

where $c_{0}$ is a constant and $W$ is a random variable with mean $c_{v}$.
Note that the cost of fixing a fault is increasing as the number of faults removed is increasing. This is reasonable because it may become difficult to identify and fix a fault which occurs in the later testing phases. Then the expected total debugging cost in $[0, t)$ is given by

$$
\begin{aligned}
C_{r}(t) & =E\left[\sum_{i=1}^{N(t)}\left[c_{0}+(i-1) W\right]\right] \\
& =\sum_{n=1}^{\infty} E\left[\sum_{i=1}^{N(t)}\left[c_{0}+(i-1) W\right] \mid N(t)=n\right] P(N(t)=n) \\
& =\sum_{n=1}^{\infty} E\left[\sum_{i=1}^{n}\left[c_{0}+(i-1) W\right] \mid N(t)=n\right] P(N(t)=n) \\
& =\sum_{n=1}^{\infty} \frac{n\left[2 c_{0}+(n-1) c_{v}\right]}{2} P(N(t)=n) \\
& =\frac{1}{2} \sum_{n=1}^{\infty} n\left[2 c_{0}-c_{v}+n c_{v}\right] P(N(t)=n) \\
& =\left(\frac{2 c_{0}-c_{v}}{2}\right) E[N(t)]+\frac{c_{v}}{2} \sum_{n=1}^{\infty} n^{2} P(N(t)=n)
\end{aligned}
$$$$
\begin{aligned}
& =\left(\frac{2 c_{0}-c_{v}}{2}\right) M(t)+\frac{c_{v}}{2} E\left[N^{2}(t)\right] \\
& =\left(\frac{2 c_{0}-c_{v}}{2}\right) M(t)+\frac{c_{v}}{2}\left[\operatorname{Var}[N(t)]+M^{2}(t)\right]
\end{aligned}
$$

If in the above cost model we also consider the cost of testing per unit time and assume that it is a random variable $V_{1}$ with mean $c_{3}$, then the total expected testing and debugging cost up to time $t$ is given by

$$
\begin{aligned}
C(t) & =E\left[t V_{1}\right]+\left(\frac{2 c_{0}-c_{v}}{2}\right) M(t)+\frac{c_{v}}{2}\left[\operatorname{Var}[N(t)]+M^{2}(t)\right] \\
& =t c_{3}+\left(\frac{2 c_{0}-c_{v}}{2}\right) M(t)+\frac{c_{v}}{2}\left[\operatorname{Var}[N(t)]+M^{2}(t)\right]
\end{aligned}
$$

Now we determine the variance of $N(t)$. Pham and Wang (2001) prove

$$
\begin{aligned}
E\left[N^{2}(t)\right] & =\sum_{n=0}^{\infty} n^{2} P\{N(t)=n\} \\
& =\sum_{n=0}^{\infty} n^{2}\left[G^{(n)}(t)-G^{(n+1)}(t)\right] \\
& =\sum_{n=1}^{\infty}(2 n-1) G^{(n)}(t)
\end{aligned}
$$

Therefore, the variance turns out to be

$$
\begin{aligned}
\operatorname{Var}[N(t)] & =E\left[N^{2}(t)\right]-E^{2}[N(t)] \\
& =E\left[N^{2}(t)\right]-M^{2}(t) \\
& =\sum_{n=1}^{\infty}(2 n-1) G^{(n)}(t)-M^{2}(t)
\end{aligned}
$$

where $G^{(n)}(t)$ is the convolution of the inter-arrival times $F_{1}, F_{2}, \ldots, F_{n}$, defined in Section 11.2.

The cost of the expected testing and debugging up to time $t$ is discussed above. Now we investigate the expected total software cost during its life cycle. Pham (1996) derives a software cost model with imperfect debugging, random life cycle and penalty cost using nonhomogeneous Poisson process. Similar to Pham (1996), we can derive the expected total software life-cycle cost. Let $c_{1}$ represent the cost of fixing a fault during testing phase, $c_{2}$ represent the cost of fixing a fault during operation phase, $c_{3}$ the cost of testing per unit time, $T$ the software release time, $T_{d}$ the scheduled delivery time, $g(t)$ the probability density function of the lifecycle length $(t>0)$. Then it is easy to verify that the expected total software life-cycle cost is given by

$$
C(T)=c_{3} T+c_{1} M(T)+\int_{T}^{\infty} c_{2}[M(t)-M(T)] g(t) d t+I\left(T-T_{d}\right) \cdot c_{p}\left(T-T_{d}\right)
$$

where $c_{p}(t)$ is a penalty cost for a delay of delivering software, and $I(t)$ is an indicator function, i.e.,

$$
I(t)=\left\{\begin{array}{l}
1 \text { if } t \geq 0 \\
0 \text { otherwise }
\end{array}\right.
$$

Usually, $M(t)$ and $\operatorname{Var}[N(t)]$ contains some unknown parameters. Their estimation can be carried out by using the maximum likelihood or least squares method.

Denote by $t_{i}$ the $i^{\text {th }}$ failure time since the software testing begins at time zero. Assume that $0=t_{0}<t_{1} \cdots<t_{n}$. The likelihood function of the above software reliability model is, noting that Equation (11.1) in Section 11.2,

$$
\begin{aligned}
L\left(t_{1}, t_{2}, \ldots, t_{n}\right) & =\prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| f_{2}\left(t_{2}|\Theta| \cdots f_{n}\left(t_{n} \mid \Theta\right)\right.\right. \\
& =\prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| \alpha^{-1} f_{1}\left(\alpha^{-1} t_{2}|\Theta| \cdots \alpha^{1-n} f_{1}\left(\alpha^{1-n} t_{n} \mid \Theta\right)\right.\right. \\
& =\alpha^{-n(n-1) / 2} \prod_{i=1}^{n} f_{1}\left(t_{1}|\Theta| f_{1}\left(\alpha^{-1} t_{2}|\Theta| \cdots f_{1}\left(\alpha^{1-n} t_{n} \mid \Theta\right)\right.\right.
\end{aligned}
$$

where $\Theta$ represents the parameter family including parameter $\alpha$.
From the above likelihood function the parameters in $M(t)$ and $\operatorname{Var}[N(t)]$ can be estimated by the maximum likelihood method. Let's take the normal distribution as an example.

Assume that the first failure time, $X_{1}$, of a new software system follows the normal distribution with mean $\mu$ and variance $\sigma^{2}$, that is,

$$
f_{1}(x)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-(x-\mu)^{2} / 2 \sigma^{2}}
$$

and that the testing process can be modeled by the quasi-renewal process. From testing data - failure times $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ we can easily estimate quasi-renewal process parameter $\alpha$ and normal distribution parameters $\mu$ and $\sigma$. Pham and Wang (2001) obtain the following MLEs of parameters $\alpha, \mu$, and $\sigma$, which can be obtained by solving following simultaneous equations:$$
\left\{\begin{aligned}
\hat{\mu} & =\frac{1}{n} \sum_{i=1}^{n} \hat{\alpha}^{1-i} t_{i} \\
n & =\frac{1}{2 \hat{\sigma}^{2}} \sum_{i=1}^{n}\left(\hat{\alpha}^{1-i} t_{i}-\hat{\mu}\right)^{2} \\
\frac{n(n-1)}{2} & =\frac{1}{\hat{\sigma}^{2}} \sum_{i=1}^{n}\left(\hat{\alpha}^{1-i} t_{i}-\hat{\mu}\right) \frac{t_{i}}{\hat{\alpha}^{2 i-1}}
\end{aligned}\right.
$$

Now it is easy to compute the renewal function for the normal distribution. From Section 11.2, the renewal function is

$$
M(t)=\sum_{n=1}^{\infty} G^{(n)}(t)
$$

and

$$
G^{(n)}(t)=P\left\{S S_{n} \leq t\right\}
$$

where random variable $S S_{n}$ follows the normal cumulative distribution function with mean $\mu\left(1-\alpha^{n}\right) /(1-\alpha)$ and variance $\sigma^{2}\left(1-\alpha^{2 n}\right) /(1-\alpha)$.

Therefore, the renewal function is given by

$$
M(t)=\sum_{n=1}^{\infty} P\left\{S S_{n} \leq t\right\}=\sum_{n=1}^{\infty} \Phi\left(\left[t-\frac{\mu\left(1-\alpha^{n}\right)}{1-\alpha}\right] / \sqrt{\frac{\sigma^{2}\left(1-\alpha^{2 n}\right)}{1-\alpha^{2}}}\right)
$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function. Various types of approximations for the standard normal $\Phi(\cdot)$ have been developed and a simple approximation with high accuracy is by Zelen and Severo (1964):

$$
\Phi(x) \approx 1-\left(0.4361836 t-0.1201676 t^{2}+0.9372980 t^{3}\right) \sqrt[3]{2 \pi)^{1}} \exp \left(-\frac{1}{2} x^{2}\right)
$$

where $t=(1+0.33267 x)^{-1}$. The error in $\Phi(x)$, for $x \geq 0$, is less than $1 \times 10^{-5}$.
Note that the relationship $\Phi(x)=1-\Phi(-x)$. Thus, we can use this relationship and Equation (11.7) to approximate $\Phi(x)$ for $x<0$.

# 11.3.2 Model 2 

A software failure is one that occurs when the user perceives that the software ceases to deliver the expected result with respect to the specification input values. The user may need to identify the severity of failures, such as critical, major, or minor, depending on their impacts on systems. Severity levels may vary from one system to another, and from application to application (Pham 2000). Typically, the severity of software failure effects is classified into three categories (see, for example, Telcordia GR-1339-CORE 1997):Type 1 fault (critical) - This category is for disastrous effects, such as loss of human life or permanent loss of property, for example, the effect of an erroneous medication prescription or an air-traffic controller error due to software failures. This type of fault may occur rarely in practice.
Type 2 fault (major) - This category is for serious failures of the software system where there is no physical injury to people or other systems. Included in this category might be erroneous purchase orders or the breakdown of a road vehicle. Usually, this type of fault occurs occasionally.
Type 3 fault (minor) - This category is reserved for those faults which lead to marginal inconveniences to a software system or its users. Examples might be a vending machine that momentarily cannot provide changes or a bank's computer system that is down when a consumer requests a balance (Pham 2000). Relatively, this may be a type of fault that occurs most in reality.

In Telcordia GR-1339-CORE 1997, the telecommunication system software reliability objectives for a given release are:

- The cumulative number of Critical software faults for each software release should be equal to 0 .
- The cumulative number of Major faults for each software release should be less than or equal to 4 .
- The cumulative number of Minor software faults for each software release should be less than or equal to 36 .

Suppose that when a fault is detected it is a critical one with probability $p_{1}$, a major one with probability $p_{2}$, and a minor one with probability $p_{3}$ where $p_{1}+p_{2}+p_{3}=1$. When a critical, major, or minor fault is removed, the fault-free time will be independent of the previous ones and increased to a multiple, $\alpha_{1}, \alpha_{2}$, or $\alpha_{3}$, of the immediate previous one, respectively, where parameters $\alpha_{1} \geq \alpha_{2} \geq \alpha_{3} \geq 1$, or more generally $\alpha_{1}, \alpha_{2}, \alpha_{3} \geq 1$. Thus, upon removal of the first fault, the $c d f$ of the fault-free time $X_{2}$ is given by

$$
\begin{aligned}
F_{2}(t) & =P\left\{X_{2} \leq t\right\} \\
& =\sum_{i=1}^{3} P\left\{X_{2} \leq t \mid \text { first fault is type } i\right\} P\{\text { first fault is type } i\} \\
& =\sum_{i=1}^{3} P\left\{\alpha_{i} Z_{2} \leq t \mid \text { first fault is type } i\right\} P\{\text { first fault is type } i\} \\
& =\sum_{i=1}^{3} F_{1}\left(\alpha_{i}^{-1} t\right) \cdot p_{i}
\end{aligned}
$$and the $p d f$ and mean of $X_{2}$ are respectively,

$$
\begin{aligned}
f_{2}(t) & =F_{2}^{\prime}(t) \\
& =\sum_{i=1}^{3} \alpha_{i}^{-1} f_{1}\left(\alpha_{i}^{-1} t\right) \cdot p_{i} \\
E\left(X_{2}\right) & =\sum_{i=1}^{3} E\left\{X_{2} \mid \text { first fault is type } i\right\} P\{\text { first fault is type } i\} \\
& =\sum_{i=1}^{3} \alpha_{i} \mu p_{i} \\
& =\mu \sum_{i=1}^{3} \alpha_{i} p_{i}
\end{aligned}
$$

Similarly, upon removal of the second fault, the $c d f, p d f$ and the expected faultfree time $X_{3}$ is given by

$$
\begin{aligned}
F_{3}(t) & =P\left\{X_{3} \leq t\right\} \\
& =\sum_{i=1}^{3} F_{2}\left(\alpha_{i}^{-1} t\right) p_{i} \\
& =\sum_{i=1}^{3} \sum_{j=1}^{3} F_{1}\left(\alpha_{i}^{-1} \alpha_{j}^{-1} t\right) p_{i} p_{j} \\
f_{3}(t) & =F_{3}^{\prime}(t) \\
& =\sum_{i=1}^{3} \alpha_{i}^{-1} f_{2}\left(\alpha_{i}^{-1} t\right) p_{i} \\
& =\sum_{i=1}^{3} \sum_{j=1}^{3} \alpha_{i}^{-1} \alpha_{j}^{-1} f_{1}\left(\alpha_{i}^{-1} \alpha_{j}^{-1} t\right) p_{i} p_{j} \\
E\left(X_{3}\right) & =\sum_{j=1}^{3} E\left\{X_{3} \mid 2 \mathrm{nd} \text { fault is type } j\right\} P\{2 \mathrm{nd} \text { fault is type } j\} \\
& =\sum_{j=1}^{3} \alpha_{j} \mu \sum_{i=1}^{3} \alpha_{i} p_{i} p_{j} \\
& =\mu \sum_{j=1}^{3} \sum_{i=1}^{3} \alpha_{i} \alpha_{j} p_{i} p_{j}
\end{aligned}
$$

By induction, we can obtain $c d f, p d f$, and the expected error-free time of the software upon removal of the $k^{\text {th }}$ fault:

$$
F_{k+1}(t)=\sum_{i_{1}=1}^{3} \sum_{i_{2}=1}^{2} \cdots \sum_{i_{k}=1}^{3} F_{1}\left(\alpha_{i_{1}}^{-1} \alpha_{i_{2}}^{-1} \cdots \alpha_{i_{k}}^{-1} t\right) p_{i_{1}} p_{i_{2}} \cdots p_{i_{k}}
$$$$
\begin{gathered}
f_{k+1}(t)=\sum_{i_{1}=1}^{3} \sum_{i_{2}=1}^{3} \cdots \sum_{i_{k}=1}^{3} \alpha_{i_{1}}^{-1} \alpha_{i_{2}}^{-1} \cdots \alpha_{i_{k}}^{-1} f_{1}\left(\alpha_{i_{1}}^{-1} \alpha_{i_{2}}^{-1} \cdots \alpha_{i_{k}}^{-1}\right) p_{i_{1}} p_{i_{2}} \cdots p_{i_{k}} \\
E\left(X_{k+1}\right)=\mu \sum_{i_{1}=1}^{3} \sum_{i_{2}=1}^{3} \cdots \sum_{i_{k}=1}^{3} \alpha_{i_{1}} \alpha_{i_{2}} \cdots \alpha_{i_{k}} p_{i_{1}} p_{i_{2}} \cdots p_{i_{k}}
\end{gathered}
$$

From these $p d f \mathrm{~s}$ and the failure times $\left\{t_{1}, t_{2}, \ldots, t_{k}\right\}$ we can estimate the parameters $\alpha_{1}, \alpha_{2}, \alpha_{3}, p_{1}, p_{2}, p_{3}$, and the error-free time distribution parameters by maximum likelihood method.

Suppose that the $i^{\text {th }}$ software fault may be of type $j$ for $j=1,2,3$ respectively. We assume that the cost of fixing this fault is a random variable $c_{i j}$ and consists of two parts - deterministic part $c_{0 j}$ and incremental random part $(i-1) W_{j}$ :

$$
c_{i j}=c_{0 j}+(i-1) W_{j} \quad \forall i, i=1,2,3, \ldots, \forall j, j=1,2,3
$$

where $c_{0 j}$ is a constant and $W_{j}$ is a random variable with mean $c_{v j}$.
Assume that the cost of testing per unit time is a random variable $V_{1}$ with mean $c_{3}$ and is independent of the error-free time. Then the expected total cost of fixing the first $k$ faults during software testing phase is given by

$$
C\left(t_{k}\right)=E \sum_{m=1}^{k} V_{1} X_{m}+\sum_{i=1}^{k} \sum_{j=1}^{3} E\left[c_{i j} \mid \text { the } i^{\text {th }} \text { fault is type } j\right] P\{\text { the } i^{\text {th }} \text { fault is type } j\}
$$

Pham and Wang (2001) show

$$
C\left(t_{k}\right)=c_{3} \sum_{m=1}^{k} E\left[X_{m}\right]+k \sum_{j=1}^{3}\left[c_{0 j}+\frac{(k-1)}{2} c_{v j}\right] p_{j}
$$

where $E\left(X_{m}\right)$ is given by Equation (11.8b).
Now we consider a numerical example. Assume

$$
\begin{array}{lll}
\alpha_{1}=1.6 & \alpha_{2}=1.4 & \alpha_{3}=1.2 \\
p_{1}=0.1 & p_{2}=0.3 & p_{2}=0.6 \\
c_{01}=30 & c_{02}=15 & c_{03}=5 \\
c_{v 1}=1.4 & c_{v 2}=1.2 & c_{v 3}=0.8 \\
c_{3}=0.5 & \mu=10 \mathrm{hrs} &
\end{array}
$$

The expected error-free time (execution time, hrs) in Equation (11.8b) and expected total cost in Equation (11.9) are computed and listed in Table 11.1. The above cost unit is staff-unit (Ehrlich et al. 1993). Table 11.1 shows that both the expected error-free time and the expected total cost are increasing as the number of faults removed is becoming large. However, increment of the expected total cost is faster in this example, and is not linearly proportional to that of the expected error-Table 11.1. Expected error-free time and expected total cost

| Number of errors <br> removed $k$ | Expected <br> error-free time <br> $E\left[X_{k+1}\right]$ | Expected <br> total cost <br> $C\left(t_{k}\right)$ |
| :--: | :--: | :--: |
| 1 | 13.0 | 15.5 |
| 2 | 16.9 | 33.5 |
| 3 | 22.0 | 54.4 |
| 4 | 28.6 | 78.8 |
| 5 | 37.1 | 107.5 |
| 6 | 48.3 | 141.5 |
| 7 | 62.7 | 182.0 |
| 8 | 81.6 | 230.7 |
| 9 | 106.0 | 289.9 |
| 10 | 137.9 | 362.2 |
| 11 | 179.2 | 451.4 |
| 12 | 233.0 | 562.3 |
| 13 | 302.9 | 701.1 |
| 14 | 393.7 | 875.7 |
| 15 | 511.9 | 1096.8 |
| 16 | 665.4 | 1378.0 |
| 17 | 865.0 | 1736.8 |
| 18 | 1124.6 | 2196.5 |
| 19 | 1461.9 | 2786.9 |
| 20 | 1900.5 | 3547.0 |

free time. Therefore, this example demonstrates the fact that it may usually become difficult and costly to fix a fault which is detected in the later testing phases.

# 11.4 Optimization Models 

In Sections 11.3.1 and 11.3.2 we have derived software reliability and testing cost measurements respectively. Now we discuss the optimal software testing policies. Usual criteria of optimization of software testing are based on testing cost indices only. However, to optimize cost measures alone is sometimes not sufficient; we may be required to consider both reliability measure and testing costs for optimization. In practice, two classes of optimal testing policies may be needed: optimal testing policies which minimize the testing cost while some reliability requirements are satisfied, or policies that maximize software reliability measure given testing cost is no more than some predetermined value. For example, from Equations (11.1) and (11.4) we can formulate the following optimization models in terms of the decision variable - software testing time $t$ :$$
\begin{array}{ll}
\text { Minimize } & C(t)=t c_{3}+\left(\frac{2 c_{0}-c_{v}}{2}\right) M(t)+\frac{c_{v}}{2}\left\{\operatorname{Var}[N(t)]+M^{2}(t)\right\} \\
\text { Subject to } & \left\{\begin{array}{l}
\bar{M}(t)=M(\tau)-M(t) \leq N_{r} \\
t \geq 0
\end{array}\right.
\end{array}
$$

where constant $N_{r}$ is the pre-determined requirement for number of the remaining faults in the software upon release. From the above model, the optimal testing time $t^{*}$ can be achieved, which minimizes the expected total cost of testing and debugging, given that the number of remaining faults in the software upon release is no more than a constant $N_{r}$.

From Equations (11.8b) and (11.9) we can also establish the following optimization models in terms of the decision variable of testing stop number $k$ :

$$
\begin{array}{ll}
\text { Maximize } & E\left(X_{k+1}\right)=\mu \sum_{i_{t}=1}^{3} \sum_{i_{2}=1}^{3} \cdots \sum_{i_{k}=1}^{3} \alpha_{i_{t}} \alpha_{i_{2}} \cdots \alpha_{i_{t}} p_{i_{t}} p_{i_{2}} \cdots p_{i_{k}} \\
\text { Subject to } & \left\{\begin{array}{l}
C\left(t_{k}\right)=c_{3} \sum_{m=1}^{k} E\left[X_{m}\right]+\sum_{j=1}^{3}\left[k c_{0 j}+\frac{k(k-1)}{2} c_{v j}\right] p_{j} \leq C_{r 0} \\
k \leq a_{0} \\
k=1,2,3, \ldots
\end{array}\right.
\end{array}
$$

where $C_{r 0}$ is the predetermined requirement for total testing-debugging cost, and $a_{0}$ is the initial number of errors in the software program and can be estimated by Halstead's software metric $\hat{B}=V / 3000$ where $V$ is defined in Pham (2000) or from the Goel-Okumoto model (Goel 1985).

From Equation (11.11), the optimal testing stop number $k^{*}$ can be found, which maximizes the expected software error-free time upon release, given that the expected total cost of testing and debugging is no more than a constant $C_{r 0}$.

The above two models can be solved by nonlinear programming software to obtain the optimal software release time or number.

Now a numerical example is used to illustrate the optimization model (11.11). A set of real testing data from Misra (1983) is shown in Table 11.2 and will be used in this example. We first estimate the number of initial errors in this software program. The Goel-Okumoto software model shows the following relationship between the expected number $m(t)$ of errors to be detected by time $t$ and total number $a_{0}$ of faults that exist in a software before testing:

$$
m(t)=a_{0}\left(1-e^{-b t}\right)
$$

where $b$ is a parameter representing the failure intensity of a fault.Table 11.2. Failures in 1 hour (execution time) interval

| Time (hours) | Number of <br> failures | Cumulative <br> failures |
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

Using the maximum likelihood estimate method, we can obtain from Table 11.2 for the Goel-Okumoto model:

$$
\hat{a}_{0}=143 \quad \hat{b}=0.1246
$$

The cost coefficients are usually determined by empirical data, previous experiences, and software characteristics. Ehrlich et al. (1993) at AT\&T studied some project data using the measure unit of staff-units and found that the ratio of the cost of removing an error during testing period and the testing cost per unit time is about $10 \sim 12$. It is estimated that there are 370 CPU test-execution units during testing with 1.9 staff-units per CPU unit. Based on the above information, we assume in optimization model (11.11):

$$
\begin{array}{lll}
\alpha_{1}=1.020 & \alpha_{2}=1.015 & \alpha_{3}=1.010 \\
p_{1}=0.1 & p_{2}=0.3 & p_{2}=0.6
\end{array}
$$$$
\begin{array}{rlrl}
c_{01} & =30 & c_{02}=15 & c_{03}=5 \\
c_{v 1} & =1.4 & c_{v 2}=1.2 & c_{v 3}=0.8 \\
c_{3} & =1.2 & \mu=0.1838 \mathrm{hrs} & a_{0}=143 \\
C_{r 0} & =11,400 &
\end{array}
$$

The cost unit above is staff-units, and the error-free time is in terms of execution time (hrs). By numerical method from optimization model (11.11), the optimal testing stop number $k^{*}$ can be found to be 139 , which results in the maximum expected software error-free time upon release of 1.46 hrs , given the expected total cost of testing and debugging is no more than 11400 staff-units. The corresponding total cost of testing and debugging is 11377.4 staff-units.

Next we see another example. Consider the software testing model in Section 11.3.1. Assume that the release time for the software is the time of detecting $k$ faults. Then upon release the expected error-free time is

$$
E\left(X_{k+1}\right)=\alpha^{k} E\left(Z_{k}\right)=\alpha^{k} \mu
$$

The expected total testing-debugging cost until release is

$$
\begin{aligned}
C & =E\left[\sum_{i=1}^{k}\left[c_{0}+(i-1) W\right]\right] \\
& =k c_{0}+\frac{k(k-1)}{2} c_{v}
\end{aligned}
$$

If the expected error-free time upon software release is required to be larger than a predetermined number $L$, then the following optimization model can be formulated:

$$
\begin{aligned}
& \text { Minimize } \quad C=k c_{0}+\frac{k(k-1)}{2} c_{v} \\
& \text { Subject to }\left\{\begin{array}{c}
\alpha^{k} \mu \geq L \\
k \leq a_{0} \\
k=1,2,3, \ldots
\end{array}\right.
\end{aligned}
$$

where $a_{0}$ can be similarly estimated by Halstead's software metric or from the Goel-Okumoto model.

Now we assume that, in terms of execution time and staff-units,

$$
\begin{array}{lll}
c_{0}=13.5 & c_{v}=1 & \alpha=1.015 \\
a_{0}=143 & L=1.4 \mathrm{hrs} & \mu=0.1838 \mathrm{hrs}
\end{array}
$$

The optimal solution to above model is

$$
k^{*}=137
$$and the corresponding expected total cost is

$$
C^{*}=11,165.5 \text { staff-units }
$$

Therefore, we will obtain the minimum cost of 11,165.5 staff-units if we stop testing once the $137^{\text {th }}$ fault is removed. The corresponding expected error-free time is 1.4 hrs . If the average error-free time requirement $L$ is changed to 1.50 hrs from 1.40 hrs , the optimal release number is

$$
k^{*}=141
$$

and the corresponding expected total cost and error-free time are respectively

$$
\begin{aligned}
& C^{*}=11,773.5 \text { staff-units } \\
& \mu^{*}=1.50 \mathrm{hrs}
\end{aligned}
$$

If we consider the cost of testing per unit time which is a random variable $V_{1}$ with mean $c_{3}$ and is independent of the error-free time, the optimization model (11.12) becomes

$$
\begin{array}{ll}
\text { Minimize } & C=\frac{\mu\left(\alpha^{k}-1\right)}{\alpha-1} c_{3}+k c_{0}+\frac{k(k-1)}{2} c_{v} \\
\text { Subject to } & \left\{\begin{array}{c}
\alpha^{k} \mu \geq L \\
k \leq B \\
k=1,2,3, \ldots
\end{array}\right.
\end{array}
$$

Assume that $c_{3}=1.2$ staff-units per hour and the average error-free time requirement $L$ is 1.40 hrs . The optimal release number, in terms of removed faults, is

$$
k^{*}=137
$$

and the corresponding expected total cost and error-free time are respectively

$$
C^{*}=11,263.8 \text { staff-units } \quad \mu^{*}=1.41 \mathrm{hrs}
$$

The above numerical results based on the set of real testing data show that the models developed in this chapter work well in practice. Note that results from the three optimization models (Equations 11.11 through 11.13) are quite close.

In many cases a software is large-scale and consists of many software modules performing different functions. We can apply software reliability growth models to the module level to estimate how many faults are remaining in each module at different stages of software testing process, and prioritize future testing efforts.# 11.5 Concluding Discussions 

This chapter has discussed software reliability and cost modeling via quasi-renewal processes. From this chapter we can see that the quasi-renewal process is an effective tool to model software reliability and costs since measures and indices can be derived conveniently. Especially, software error-free time information upon testing can be obtained by using this modeling tool. In this chapter, we assume the cost of fixing a fault during software testing phase consists of deterministic and probabilistic parts, and it becomes larger as the number of faults removed is increasing. This assumption is justified by the fact that it may usually become difficult to fix a fault which is detected in the later testing phases. Besides, three types of faults in software are considered for Model 2. Testing and debugging costs are considered separately in this work. Obviously, all these assumptions and considerations make the proposed software models more realistic.

In software reliability and cost models introduced in this chapter, we note that most results - expected software testing and debugging cost, number of remaining faults in the software, and mean error-free time after testing - are in closed forms. The parameters associated with these models can be easily estimated through the maximum likelihood method and the likelihood equations can be solved by standard numerical methods. Unlike most other software reliability models, we combine reliability measures and testing cost measures of software in optimization problems and the optimal solutions to the optimization problems lead to optimal software testing policies with regards to both reliability measures and testing cost measures.

Software reliability models in this chapter can be used to estimate the residual faults upon release to know if software reliability objectives are met, for example, if telecommunication software can meet Telcordia software reliability objectives for a given release.

Generally, software reliability also grows in field use since faults found in the field may be removed. The models introduced in this chapter can also apply to modeling field reliability growth and maintenance cost.# Monte Carlo Reliability Simulation of Complex Systems 

To obtain the optimal maintenance policy for a complex system, we may need to evaluate system availability or MTBF first, as discussed in Section 1.5. The previous chapters have modeled reliability measures for some standard reliability architectures. However, in practice, many systems are complex systems. Generally there are four major difficulties in evaluating complex large-scale system reliability, availability and MTBF (MTTF): the system reliability structure may be very complicated; subsystems may follow different failure distributions; subsystems may have arbitrary failure and repair distributions for maintained systems; failure data of subsystems are sometimes not sufficient, sample size of life test or field population tends to be small. Therefore, it may be difficult and often impossible to obtain $s$-confidence limits of the reliability indices by classical statistics. It has been proven that Monte Carlo technique combined with Bayes method is a powerful tool to deal with this kind of complex systems. In this chapter, the typical existing Monte Carlo reliability, availability, and MTBF simulation procedures are analyzed together with variance reduction techniques and random variate generation algorithms. The advantages, drawbacks, accuracy and computer execution time of Monte Carlo simulation in evaluating reliability, availability and MTBF of complex networks are discussed. Some conclusions are summarized, and a general Monte Carlo reliability and MTTF assessment procedure is presented.

### 12.1 Introduction

Monte Carlo simulation methods are numerical methods which allow the solution to mathematical and technical problems by means of system probabilistic models and simulation of random variables. It was originated in the 1940s by mathematicians Newman and Ulam at an early development stage of nuclear technology. Scientists at the Los Alamos National Laboratory used it to model the random diffusion of neutrons. They gave it the name "Monte Carlo" after the cityin Monaco and its many casinos. Today, its applications have been extended to many areas of science and technology. Monte Carlo simulation method is now recognized as playing an important role in system reliability, availability and MTTF (MTBF) assessment and optimal maintenance of large-scale complex networks. During the last 50 years a lot of efforts has been made in developing efficient Monte Carlo simulation methods and software programs for determining $s$-confidence bounds on system reliability, availability, and MTTF (MTBF). Using classical statistical methods, it is difficult and sometimes even impossible to obtain $s$-confidence intervals of system reliability, availability, and MTTF (MTBF) though it may be easy to find point estimates of complex system reliability. In fact, how to obtain $s$-confidence limits on them is not only a dilemma in engineering practice, but also one in statistical theory. By Monte Carlo simulation method, such analysis becomes relatively easy and at least possible, as fast computers are now readily available.

In the last several decades, a lot of Monte Carlo reliability, availability, and MTTF (MTBF) evaluation methods and software programs have been developed. Wang and Pham (1997) summarize the previous research in an overview paper. System reliability and MTTF estimation by Monte Carlo method began at least in 1960. Orkand (1960) presents his technical report on determining system reliability confidence limits from subsystem failure test data using Monte Carlo simulation method at the U.S. Picatinny Arsenal. Burnett and Wales (1961) discuss analytical and Monte Carlo techniques for obtaining confidence limits and the assumptions necessary for their use. They create the method for the case of components with exponentially distributed failures. Bernhoff (1963) in his thesis also studies the Monte Carlo reliability simulation at U.S. Air Force Institute of Technology. Moore (1965) develops a general Monte Carlo technique extending the Monte Carlo method to cases where the joint distribution of the estimators of the parameters of failure model is known. In fact, Moore and his graduate students Levy (1964, 1967), Lutton (1967), Lannon (1972), Snead (1978), Rice (1979), Putz (1979), Johnson (1980), MacDonald (1982), and others, have done much work in this field. Among them, Levy and Moore (1967) design a process to obtain system reliability $s$-confidence limits for a system composed of different subsystems whose failures follow the Normal, Lognormal, Gamma, or Weibull distributions and distribution parameters are supposed to be estimated by the maximum likelihood method based on life tests from a complete sample or from a censored sample where the distribution of the estimator is known.

Gilmore (1968) analyzes complex system MTBF using Monte Carlo simulation. Integrating Bayesian method with Monte Carlo simulation, Locks (1974a,b, 1978) proposes a Monte Carlo-Bayesian approach to determine reliability lower bounds and MTTFs of complex large-scale systems of any modular reliability structures. Massa develops a Monte Carlo reliability evaluation technique under binomial and exponential failure distributions. Rice and Moore (1983), Chao and Huwang (1987) investigate Monte Carlo reliability assessment for systems with binomial-failure subsystems. Kamat and Riley (1975) present a Monte Carlo system reliability estimation method in which its subsystems are allowed to conform to any different failure distributions. Later, Kamat and Franzmeier (1976) extend this procedure to determine reliability confidenceintervals on systems including $s$-dependent subsystems and/or allowing repair of failed subsystems. Kumamoto et al. (1977, 1987), Fishman (1986a,b, 1987a,b,c, 1989), and Baca (1993) have done much research on Monte Carlo network reliability assessment and sampling plan, and investigated technique of variance reduction, a major problem for large Monte Carlo simulation. Availability and MTBF evaluation for reparable systems have also received certain attention (Kamat and Frazmeier 1976; Kim and Lee 1992; Kumamoto et al. 1980a; Moore et al. 1985). Today, Monte Carlo simulation technique for reliability, availability and MTBF assessment has been widely used in electric power systems, civil engineering, nuclear engineering, building industry, and probabilistic mechanics.

Monte Carlo reliability simulation methods of complex systems have become relatively mature, especially for non-repairable systems. In addition, fast computers can be available everywhere and using them to perform Monte Carlo simulation is very convenient. Note also that Monte Carlo reliability simulation research in some engineering fields, such as electric power systems, civil engineering, nuclear engineering, building industry, and probabilistic mechanics, still receive some attention. However, the focus of this chapter is general methodologies of Monte Carlo reliability and availability simulation for various reliability structures following Wang and Pham (1997), while its applications in individual fields will not be addressed in details.

# 12.2 Typical Monte Carlo Algorithms for Reliability 

To study characteristics, accuracy and related problems of different Monte Carlo techniques, we have selected some typical ones, and next analyze and discuss them. First, we analyze a general approach by combining reliability flow graph representation, Boolean state representation and Monte Carlo simulation.

### 12.2.1 K-R Method

This Monte Carlo procedure, developed by Kamat and Riley (1975), is fairly general and can be applied to most systems with arbitrary system reliability structure and different subsystem failure distributions without modification. In this procedure, individual subsystems are assumed to be independent of each other and repair of failed subsystems are not allowed; the underlying life distribution is known for each subsystem and distribution parameters have been estimated. The key idea of this K-R method is:
(a) Find out all minimal tie-sets from system Reliability Block Diagram (RBD). Assume that we need to obtain system reliability interval estimates at some time point $t$.
(b) From the life distribution of each subsystem, a random failure time $t_{i}$ is generated where $i$ represents the $i^{\text {th }}$ subsystem, $0<i<n$.
(c) Compare $t_{i}$ with $t$ for all subsystems. If $t_{i}>t$, this indicates that at time $t$ subsystem $i$ functions properly; if $t_{i} \leq t$, then subsystem $i$ has failed.(d) Determine whether the whole system is functioning or down according to the states of its subsystems at $t$ from step (c). Check all subsystems in a minimal tie-set. If all of them are operational then the system operates properly at $t$. If one or more of them fail, then the tie-set is broken (failure) at $t$. Further, check next minimal tie-set until an unbroken one appears, which means that the system is operational at $t$. If all minimal tie-sets are broken then the system fails at $t$.
(e) Repeat steps (b), (c), (d) for, say, $n$ times. Count failure and success numbers of the system respectively: $n_{S}(t)$ and $n_{F}(t)$. Note that $n=n_{S}(t)+n_{F}(t)$
(f) The system reliability point estimate corresponding to $t$ is given by

$$
\hat{R}(t)=\frac{n_{S}(t)}{n_{S}(t)+n_{F}(t)}
$$

Note that the simulation results are of binomial type. Based on the Normal approximation to the Binomial distribution, the $100(1-\gamma) \%$ confidence intervals of system reliability at time $t$ are given by

$$
\left[R_{L}(t), R_{U}(t)\right]=\hat{R}(t) \pm z_{\gamma} \frac{\hat{R}(t)(1-\hat{R}(t))}{\left[n_{S}(t)+n_{F}(t)\right]^{1 / 2}}
$$

where $z_{\gamma}$ is the double-side $100 \gamma \%$ percentile of the standard Normal distribution with mean zero and variance 1 .

An application example is given by Kamat and Riley (1975). The system reliability structure diagram in this example is shown in Figure 12.1 and lifetimes of all nine subsystems: a, b, c, d, e, f, g, h, i are assumed to follow the twoparameter Weibull distribution with survival function

$$
\operatorname{sf}\left(t ; K_{i}, M_{i}\right)=\exp \left[-\frac{K_{i}}{M_{i}+1} t^{M_{i}+1}\right] \quad t, M_{i}>0, M_{i}>-1
$$

From Figure 12.1, we can see that it is difficult to determine the reliability interval estimates of this system by using classical statistics. Per system reliability


Figure 12.1. Reliability structure diagramtheory, the system's minimal tie-sets can be found to be
adg, bdg, adhi, bdhi, aefi, befi, cfi
The scale parameter $K_{i}$ and shape parameter $M_{i}$ values for all nine subsystems are listed in Table 12.1. Utilizing the K-R Monte Carlo algorithm, 1000 simulation replications are performed on the IBM360/65 computer by Kamat and Riley (1975). Table 12.2 summarizes the results of system reliability point estimates and $95 \%$ interval estimates at certain time points.

Since Kamat and Riley (1975) do not discuss the accuracy of their simulation results and we cannot derive exact $95 \%$ confidence intervals for this system by

Table 12.1. Weibull parameters for each component

| Component no. | Scale parameter $K$ | Shape parameter $M$ |
| :--: | :--: | :--: |
| a | 2.8 | 1.8 |
| b | 2.7 | 1.7 |
| c | 2.6 | 1.6 |
| d | 2.5 | 1.5 |
| e | 2.4 | 1.4 |
| f | 2.2 | 1.2 |
| g | 2.3 | 1.3 |
| h | 2.1 | 1.1 |
| i | 2 | 1 |

Table 12.2. Reliability simulation results - 95\% confidence intervals

| Time | Reliability point <br> estimate | Upper 2.5\% <br> limit | Lower 2.5\% <br> limit |
| :--: | :--: | :--: | :--: |
| 0 | 1 | 1 | 1 |
| 0.1 | 1 | 1 | 1 |
| 0.2 | 0.999 | 1 | 0.997 |
| 0.3 | 0.986 | 0.993 | 0.979 |
| 0.4 | 0.95 | 0.964 | 0.936 |
| 0.5 | 0.886 | 0.906 | 0.886 |
| 0.6 | 0.775 | 0.801 | 0.749 |
| 0.7 | 0.625 | 0.665 | 0.595 |
| 0.8 | 0.445 | 0.486 | 0.424 |classical statistical methods, we are not able to draw conclusions on its accuracy. Note that the K-R method using the normal approximation to the binomial distribution will result in some error. However, from Table 12.2 we can see that the confidence intervals are generally very narrow and the point estimates are at the middle of them. Therefore, this method can basically be accepted in some engineering applications. Note that the $s$-confidence intervals obtained by the K-R method can be narrowed by increasing simulation replication number.

The simulation procedure are programmed in FORTRAN IV G level code. For the system structure in Figure 12.1, 16 seconds for execution are spent.

# 12.2.2 R-M Method 

The drawback of the K-R approach is that all minimal tie-sets have to be determined in advance. Rice and Moore (1983) propose a special Monte Carlo method (R-M) dealing with the fail-pass failure. Using this technique, not only a lower confidence limit (LCL) but also the quantitative analysis of accuracy of LCLs can be determined. The R-M method can be applied to any complex system structure whose subsystem failures follow binomial distributions, especially to the systems with zero-failure subsystems. However, LCLs obtained by the R-M algorithm are somewhat larger than the exact LCLs.

The R-M simulation method is also based on the Normal approximation to the Binomial distribution: if the success probability of a binomial test is $p$, failure probability $q$, test number $n$, failure number $f$, then this binomial failure follows the Normal distribution with mean $p$ and variance $(p q / n)$. If a test has zero failure, that is, $f_{i}=0$, then $f_{i}$ can be replaced by the equivalent failure number $f_{i}^{\prime}$ given by Gatliffe (1976).

The key steps of the R-M process are
(a) Define the system and its reliability block diagram (RBD). Develop the algorithm to compute system reliability from its subsystems' reliabilities, i.e., system reliability structure function.
(b) For each subsystem, determine its failure number $f_{i}$ or equivalent failure number $f_{i}^{\prime}$. To simplify, they are both represented by $f_{i}^{*}$.
(c) Calculate estimates:

$$
p_{i}=1-\frac{f_{i}^{*}}{n_{i}} \quad q_{i}=1-p_{i} \quad \text { Asymptotic Variance }=\frac{p_{i} q_{i}}{n_{i}}
$$

(d) For each subsystem, generate a random variable from $N(0,1)$, where $N(0,1)$ is the Normal distribution with mean zero and variance 1.
(e) Find the second estimate $p_{i} \sim\left(p_{i}, \frac{p_{i} q_{i}}{n_{i}}\right)$ by drawing an $r . v$. from $N(0,1)$. Multiply by asymptotic standard variance and add it to $p_{i}$.(f) Calculate system reliability $R_{s}$ from subsystem reliabilities according to the algorithm created in step (a).
(g) Implement steps (d) - (f) many times for, say, 999 times.
(h) List these $R_{s}$ values in order of non-decreasing magnitude.
(i) Determine the $100(1-\gamma) \%$ percentile to obtain $100(1-\gamma) \%$ LCLs of $R_{s}$.

The reliability LCLs of the system which consists of two and three subsystems in series have been computed by this algorithm and are compared with those by other methods. Table 12.3 lists these LCLs, where the other approaches are:

AN/MC R-M algorithm (Rice and Moore 1983)
ML Maximum-likelihood
LR Likelihood ratio (Madansky 1965)
OPT Optimal method (exact limits)
AO Approximately optimum (Mann and Grubbs 1974)
MMLI Modified maximum-likelihood (Easterling)
Table 12.3. Comparison of lower $s$-confidence limits on reliability by using three different Monte Carlo techniques

| Num. <br> comp. | CL | n | $f_{1}$ | $f_{2}$ | $f_{3}$ | AN/MC | ML | LR | OPT | AO | MMLI |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 2 | $90 \%$ | 10 | 1 | 1 | 0.655 | 0.655 | 0.629 | 0.607 | 0.606 | 0.585 |  |
|  |  |  | 1 | 2 |  | 0.542 | 0.545 | 0.529 | 0.497 | 0.493 | 0.489 |
|  |  |  | 2 | 2 |  | 0.458 | 0.456 | 0.451 | 0.445 | 0.43 | 0.441 |
|  |  |  | 1 | 4 |  | 0.337 | 0.347 | 0.35 | 0.344 | 0.335 | 0.318 |
|  |  |  | 2 | 3 |  | 0.372 | 0.373 | 0.375 | 0.354 | 0.353 | 0.362 |
|  |  | 20 | 1 | 2 |  | 0.754 | 0.756 | 0.739 | 0.716 | 0.728 | 0.709 |
|  |  |  | 2 | 2 |  | 0.7 | 0.701 | 0.687 | 0.683 | 0.678 | 0.669 |
|  |  |  | 1 | 3 |  | 0.693 | 0.697 | 0.683 | 0.66 | 0.675 | 0.655 |
|  |  |  | 2 | 3 |  | 0.646 | 0.647 | 0.638 | 0.622 | 0.628 | 0.619 |
|  |  |  | 3 | 3 |  | 0.599 | 0.599 | 0.591 | 0.585 | 0.582 | 0.57 |
|  | $95 \%$ | 10 | 1 | 1 |  | 0.614 | 0.611 | 0.571 | 0.548 | 0.552 | 0.53 |
|  |  |  | 1 | 2 |  | 0.495 | 0.495 | 0.473 | 0.443 | 0.435 | 0.436 |
|  |  |  | 2 | 2 |  | 0.414 | 0.405 | 0.397 | 0.392 | 0.382 | 0.391 |
|  |  |  | 1 | 4 |  | 0.29 | 0.292 | 0.301 | 0.298 | 0.293 | 0.271 |
|  |  |  | 2 | 3 |  | 0.328 | 0.32 | 0.326 | 0.304 | 0.307 | 0.315 |
|  |  | 20 | 1 | 2 |  | 0.724 | 0.728 | 0.7 | 0.677 | 0.693 | 0.671 |
|  |  |  | 2 | 2 |  | 0.669 | 0.67 | 0.647 | 0.643 | 0.643 | 0.631 |
|  |  |  | 1 | 3 |  | 0.663 | 0.665 | 0.643 | 0.62 | 0.639 | 0.616 |
|  |  |  | 2 | 3 |  | 0.612 | 0.614 | 0.587 | 0.582 | 0.593 | 0.58 |
|  |  |  | 3 | 3 |  | 0.565 | 0.551 | 0.544 | 0.548 | 0.548 | 0.532 |Table 12.3. (continued)


For an eight-subsystem series system with subsystem reliabilities respectively

$$
0.95,0.95,0.90,0.95,0.85,0.75,0.95,0.95
$$

The $90 \%$ reliability LCL is 0.3665 using the R-M algorithm with Monte Carlo simulation replications of 1000 . Among these 1000 LCLs, there exist 913 LCLs for which intervals (LCL, 1) contain the true reliability .42059 which are obtained by multiplying all subsystem reliabilities. In engineering, this accuracy can be acceptable in some cases.

# 12.2.3 C-H Method 

Since a upper error exists for the R-M procedure, Chao and Huang (1987) have improved it. The numerical examples show that Chao and Huang's method (C-H) can reduce this error. The C-H algorithm is related to "bootstrap" method by Efron and replaces the (c) and (d) steps of the R-M process by the following ( $\mathrm{c}^{\prime}$ ) and ( $\mathrm{d}^{\prime}$ ):
(c') The success and failure probability estimates of subsystem $i$ are given by$$
p_{i}=1-\frac{f_{i}+a}{n_{i}+a+b} \quad q_{i}=1-p_{i} \quad \text { where } a=0.2 \text { and } b=0
$$

The above equations are derived according to Bayes theorem using the Beta prior distribution. This choice of $a$ and $b$ are studied carefully to make LCL values by Monte Carlo simulation procedure close to the exact LCLs. Obviously, the above equation for $p_{i}$ and $q_{i}$ can apply to zero failure case.
(d') Generate a random variable $f_{i}^{\bullet}$ from the Binomial distribution with parameters $n$ and $p$ in (c') and compute

$$
p_{i}^{\bullet}=1-\frac{f_{i}^{\bullet}+a}{n_{i}+a+b} \quad q_{i}^{\bullet}=1-p_{i}^{\bullet}
$$

The simulation results shows that the $\mathrm{C}-\mathrm{H}$ approach can result in more exact LCLs than the R-M procedure and the ML methods, and LCLs given by the C-H procedure are close to those by other methods and the OPT (exact limits). Therefore, for binomial failure, we suggest the C-H method be used.

# 12.2.4 L-D-L Method 

The L-D-L method was designed by Lin et al. (1988) and also used to analyze problems with binomial failure distribution. It increases failure information of subsystems using a priori failures from the Bayes method. The L-D-L method takes beta distribution $\operatorname{Beta}\left(d_{i}, b_{i}\right)$ as a priori distribution where $d_{i}$ values are determined in such a way that LCLs obtained can be made exact and $d_{i}$ is the same for all subsystems, and $b_{i}=1$ for all subsystems. Thus, the a priori distribution of each subsystem is $B(d, 1)$. According to the Bayes theorem, its posterior distribution is $\operatorname{Beta}\left(d+x_{i}, n_{i}+x_{i}+1\right)$ where $x_{i}$ and $n_{i}$ are respectively failure and test numbers of subsystem $i$. Based on these obtained posterior distributions, the L-D-L algorithm is outlined as follows:
(a) Generate $k$ random samples $r_{1}, r_{2}, \ldots r_{k}$ from $\operatorname{Beta}\left(d+x_{i}, n_{i}+x_{i}+1\right)$. Suppose that a system consists of $k$ subsystems regardless of system reliability architecture.
(b) Calculate point estimate of system reliability

$$
R_{j}=g\left(r_{1}, r_{2} \ldots r_{k}\right)
$$

where $g\left(r_{1}, r_{2} \ldots r_{k}\right)$ are the structure function of the system.
(c) Repeat steps (a), (b) 10,000 times.
(d) Rank these $R_{j}$ in ascending magnitude order.
(e) Find $100(1-\gamma) \%$ percentile $R_{1-\gamma}$ from step (d) and then $R_{1-\gamma}$ is the $100(1-\gamma) \%$ LCL which we need.

Consider a two-subsystem series system. The exact LCLs and LCLs by the L-D-LTable 12.4. Comparison of exact LCLs and the ones by L-D-L

| No. of subsystems |  | No. of failures |  | $90 \%$ LCL |  | $95 \%$ LCL |  | $\delta$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $n_{1}$ | $n_{2}$ | $f_{1}$ | $f_{2}$ | L-D-L | Exact | L-D-L | Exact |  |
| 10 | 10 | 1 | 1 | 0.62 | 0.607 | 0.568 | 0.548 | 4.46 |
| 10 | 10 | 1 | 2 | 0.529 | 0.497 | 0.484 | 0.443 | 3.494 |
| 10 | 10 | 2 | 2 | 0.449 | 0.445 | 0.403 | 0.392 | 2.647 |
| 10 | 10 | 1 | 4 | 0.343 | 0.334 | 0.301 | 0.298 | 1.588 |
| 10 | 10 | 2 | 3 | 0.362 | 0.354 | 0.318 | 0.304 | 1.8 |
| 20 | 20 | 1 | 2 | 0.72 | 0.716 | 0.684 | 0.677 | 4.923 |
| 20 | 20 | 2 | 2 | 0.67 | 0.683 | 0.637 | 0.643 | 4.446 |
| 20 | 20 | 1 | 3 | 0.67 | 0.66 | 0.634 | 0.62 | 4.42 |
| 20 | 20 | 2 | 3 | 0.626 | 0.662 | 0.592 | 0.582 | 3.97 |
| 20 | 20 | 3 | 3 | 0.581 | 0.585 | 0.544 | 0.544 | 3.52 |

are listed in Table 12.4. We can see that they are close to each other and approximately equal.

# 12.2.5 L-D Method 

Most Monte Carlo simulation procedures require their users to provide minimal tie-sets or cut-sets. Lin and Donaghey (1993) propose a new Monte Carlo procedure (L-D method) for system reliability. The advantages of this algorithm is that it first utilizes the Monte Carlo method to determine the minimal tie-sets by tracing through the system from the input components to the output components of a system modeled by the Reliability Block Diagram in a random manner, then uses the minimal tie-sets to simulate system failures, the minimal cut sets and system reliability at any time are determined again by the Monte Carlo approach. Therefore, it avoids providing minimal tie-sets prior to simulation. In addition, the system mean time to failure, system failure distribution and the cumulative failure rates can be obtained. The basic idea of this process is that using Monte Carlo simulation and the minimal tie-sets as the criteria for system failure, the system fails when all minimal tie-sets are broken. Components which have failed prior to the system failure constitute a cut set. The frequencies of the minimal cut sets are tallied during the simulation runs to show the distribution of the frequencies of the minimal cut sets (Lin and Donaghey 1993). For the single bridge system and a complex ten-subsystem network, the tie-sets given by this algorithm agree with the results generated by general reliability theory. The disadvantage of this method is that it does not give confidence interval estimates.

### 12.2.6 Other Methods for Non-repairable Systems

MacDonald (1982) creates a double Monte Carlo reliability evaluation procedure for a complex system which is composed of subsystems with Weibull failuredistribution of three parameters. Putz (1979) presents a univariate Monte Carlo technique to approximate reliability confidence limits of systems with components characterized by the Weibull distribution. Lutton (1967) and Lannon (1972) study bivariate asymptotic Monte Carlo method by using the asymptotic s-normality of maximum likelihood estimates. Moore et al. (1980) compare these three Monte Carlo simulation methods: Double Monte Carlo, Univariate and Bivariate asymptotic Monte Carlo. For 3-subsystem series, parallel and series-parallel systems, a 5 -subsystem complex system and a 25 -subsystem network whose subsystems' failures follow respectively Weibull, Logistic and Gamma distributions. Conclusions by Moore et al. (1980) are that confidence bounds obtained by the bivariate asymptotic method are less than those by the double Monte Carlo which are less than those by the univariate approach. The percentage of times the confidence intervals covered the true system reliability is also compared with the desired confidence level and their results are that the bivariate method is conservative but more accurate than the univariate method and less sensitive to degradation due to high system reliability. The bivariate method is fast and accurate in some cases. The CPU times on the CDC6600 for the three methods (1000 Monte Carlo replications; 25 -subsystem system) are respectively: Bivariate: 22 seconds; Double: 22 minutes; Univariate: 11 seconds. The double Monte Carlo uses much more computer time than the other two methods. Later, Depuy et al. (1982) modify the double Monte Carlo algorithm and compare it with the two asymptotic techniques. Chang et al. (2001) introduce VP (Variational Principle) technique over analog MC and use variationally processed Monte Carlo simulation for estimating system reliability.

Kumamoto et al. (1977) design a Monte Carlo method, KTI named after them, using variance-reducing technique which applies to fail-pass failure. Using their algorithm, an 18-subsystem complex network, as shown in Figure 12.2, is analyzed and network reliability upper and lower limits are determined. Later in 1987, using variance reduction technique, they propose another new Monte Carlo technique for evaluating the top-event probability of a coherent fault tree of complex systems which can have high reliability under the assumption that all the minimal cut sets are known. However, although the KTI algorithm with a smaller sample size and variance reduction is an improvement over direct Monte Carlo approach (Hammersley and Handscomb 1964, pp.51-52) and Mazumdar's importance sampling method (Mazumdar 1975), a general-purpose computer program is not available and some theoretical problems in statistics exist with this algorithm. Locks (1979) studies the KTI procedure and presents an alternative explanation of this procedure and discusses its usefulness compared to some alternative ones available.

Some other researchers, Su (1986), Fishman (1987, 1991), and Elperin et al. (1991), integrate the graph theory and network theory with Monte Carlo simulation to assess network reliability. Note that the research based on this idea will make Monte Carlo reliability simulation systematic and theoretical and thus is very useful.

In addition, Kim and Fard (1995) propose two types of discrete-event simulation models estimating reliability, mean time to failure and probability density function of time to failure for a complex system with general failure rates.One advantage of this method is that these two discrete-event reliability models only require descriptive knowledge of network architecture rather than analytical network characteristics, such as cut or tie sets. Another advantage is that reliability modeling technique applied through this discrete-event simulation is modular and then its adaptability to large-scale complex systems is increased. They are programmed using SIMAN codes for both reliability modeling and evaluation. Actually before them, Prisker et al. (1989) suggest a sample system reliability modeling method using another discrete-event simulation language, SLAM. We believe that the discrete-event simulation for reliability is promising and suggest using it later.


Figure 12.2. Reliability block diagram of a complex system
Worth mentioning is ESCAF - Electronic Simulator to Compute and Analyze Failure developed by Laviron et al. (1982) although it is a direct simulation method, not Monte Carlo. ESCAF can be employed to determine and list cut sets and minimal cut sets, or tie-sets and minimal tie-sets; to gauge the importance of each subsystem or event by constructing histograms; to compute system unreliability or unavailability for both $s$-coherent and non-coherent systems.

# 12.2.7 Monte Carlo Methods for Repairable Systems 

Availability, MTBF and unreliability evaluation for a complex maintained system could be very complicated, sometimes even impossible to handle by classical probability, statistics, or Markov techniques. Using Monte Carlo method it is possible and practical to deal with this kind of problems. In fact, Monte Carlo simulation is the only practical technique to find $s$-confidence bounds for systemswith general failure and repair distribution (Moore et al. 1985). In the past two decades, some researchers, for example, Kamat and Franzmeier (1976), Kumamto et al. (1980a,b), Moore et al. (1985), Kim et al. (1992), have succeeded in solving this class of problems by means of Monte Carlo techniques though less work has been done on reparable systems.

Moore (1985) designs a double Monte Carlo process (see also MacDonald, 1980) for determining confidence bounds on reliability and availability of a reparable system. The confidence limits obtained by this approach in two examples demonstrate a satisfactory accuracy for it. The key idea of this method is: the simulated component failure and repair times is used to estimate parameters of failure and repair distributions. Simulated values of parameters are obtained by generating sample failure and repair times of equal size to the original sample using as parameters the estimates from the simulated real data. The parameters are again estimated from the generated data using the same estimator to obtain simulated values. Then simulated values for reliability and availability can be obtained after inserting the simulated values in the equations for reliability and availability. The process is repeated for the desired number of Monte Carlo repetitions. These points are used to determine a cumulative distribution function of system reliability and availability estimates by plotting the order statistics at their median ranks. Then the $100(1-\gamma) \%$ lower confidence bounds for reliability and availability are found.

Kumamto et al. (1980b) propose a state-transition Monte Carlo unreliability estimate method for evaluating large repairable systems which can be modeled by a stationary Markov transition diagram. Kumamto et al. (1980a) also create a dagger-sampling Monte Carlo approach for unavailability evaluation of systems which can be represented by a coherent fault tree. Generally, there are two kinds of Monte Carlo methods: direct and indirect simulation. The direct Monte Carlo is flexible but very wasteful of computer time, per Kumamto et al. (1980b). The above two methods are indirect Monte Carlo and thus reduce computation time. Along with reducing computation time, the dagger-sampling Monte Carlo combines success and failure states, and generates negatively-correlated state vectors of basic events. This negative correlation at the top-event level for fault tree applies to the corresponding states of the top event since the system structure function is a monotonously increasing one. The Monte Carlo estimator has a smaller variance than the direct Monte Carlo method because probabilistic fluctuations are canceled out by the correlation. A numerical example shows that the dagger-sampling could generate 100 trials in the computation time for one direct Monte Carlo trial. The disadvantage of the dagger-sampling Monte Carlo is that it only gives point estimate of system unavailability.

Besides Monte Carlo availability assessment, an MTBF estimate algorithm for a binomial coherent system is also presented by Kim et al. (1992), which is based on the assumptions that failed components are replaced with new ones at system failure ("as good as new" or perfect repair); if a minimal tie set fails, components therein (not included in any other minimal tie sets) cease to operate until repair of the system; replace time for any component is negligible; states of all components are $s$-independent. Note that Kamat and Franzmeier (1976) propose a Monte Carlo reliability determination method for systems which contain s-dependent compo-nents. In this method, the MTBF uses the special definition $t / E[N(t)]$, where $N(t)$ is the number of system failures in $[0, t]$ and $E[N(t)]$ is the expected value of $N(t)$. All minimal tie-sets of the system and lifetime distributions of all components are required in advance. If the component lifetime distributions are unknown, then a lower bound of system MTBF can be estimated by using known failure rates for each component. Comparing the simulation results against the theoretical ones given by Kim et al. (1992) indicates that this algorithm is successful. However, confidence limits on MTBF cannot be determined by this approach.

Monte Carlo simulation for maintained systems are more complicated than non-repairable systems. So far, there are no satisfactory Monte Carlo algorithms for evaluating MTBF and availability of general complex reparable systems. Some techniques can only give point estimates and some require much computer time. Most of them require determining all minimal tie-sets or path sets of systems in advance. Because many technical systems are repairable this seems to be a fruitful area on which later efforts can be concentrated. As shown in Chapter 2, researchers have developed many imperfect maintenance models for repairable systems, and Monte Carlo simulation of imperfect maintenance of repairable systems would be more realistic.

# 12.3 Variance Reduction and Random Number Generation 

For a system with highly reliable components, the likelihood of observing a system failure during each Monte Carlo simulation is very low. In consequence there is a large variance in the estimation of the system reliability (Chang et al. 2001). Methods have been developed to reduce the variance associated with rare events. In fact, one of the difficulties in Monte Carlo simulation lies in the prohibitive computing time whenever a very rare event has to be shown. The time required for a single sample run could therefore be quite long. For most reliability problems, the computation time is a rapidly increasing function of the number of subsystems in the system and Monte Carlo simulation of reliability problems usually results in rare-event simulation. Hence, direct Monte Carlo methods are extremely wasteful of computer time. Variance Reducing Techniques (VRT) have a dual purpose: to reduce the length of a sample run and to increase accuracy using the same number of runs. The method of applying VRTs usually depends on the particular simulation model of interest. It is generally impossible to know beforehand how great a variance reduction might be realized or whether the variance will be reduced at all in comparison with straightforward simulation. However, preliminary runs could be made to compare the results of applying a VRT with those from straightforward simulation. It is worthwhile to note that some VRTs themselves will increase computing cost and this decrease in computational efficiency must be traded off against the potential gains in statistical efficiency, measured by the variances of the output random variables from a simulation.

There are several comprehensive surveys that provide useful ways of classifying VRTs and also contain extensive bibliographies, among which are Hammersley and Handscomb (1964), Wilson (1983) and Nelson (1987). Somecommonly-used VRTs are control variates, antithetic variables, conditioning, stratified sampling and importance sampling. The control variate method attempts to take advantage of correlation between certain random variables to obtain a variance reduction. In the method of antithetic variables, the negative correlation is sought to reduce the variance of the output variable. Importance sampling reduces the variance of the output variable by increasing the frequency of rare and importance events.

Easton (1980) introduces a sequential destruction method which reduces the variance of the system reliability substantially and the amount of computation required. In evaluating system-failure probability, Kumamoto et al. (1980) show how to exploit sampling plans that induce negative correlation between replications (dagger-sampling Monte Carlo), and Kumamoto et al. (1987) proposes a new coverage Monte Carlo estimator with a smaller variance. Zio et al. (2004) further discuss dagger-sampling variance reduction in Monte Carlo reliability analysis to deal with components which may fail in more than one mode. Fishman (1986) compares the methodological features of four Monte Carlo sampling plans for estimating system reliability with particular emphasis on their statistical accuracy and variance reduction. Based on less prior information, Baca (1993) constructs a Monte Carlo procedure which yields estimators with smaller variance. The first application derives a variant of the sequential destruction method and the second application obtains the traditional importance sampling Monte Carlo method for static reliability problems.

Campioni et al. (2005) believe that, since for Monte Carlo reliability simulation it often happens that one has to deal with rare events, the use of a variance reduction technique is almost mandatory in order to have Monte Carlo efficient applications. The main issue associated with variance reduction techniques is related to the choice of the value of the biasing parameter. Actually, this task is typically left to the experience of the Monte Carlo user, who has to make many attempts before achieving an advantageous biasing. Campioni et al. (2005) provide a practical rule addressed to establish an a priori guidance for the choice of the optimal value of the biasing parameter. This rule, which has been obtained for a single component system, has the notable property of being valid for any multicomponent system.

In addition, Chang et al. (2001) investigate use of VP (Variational Principle) for another variance reduction method.

Random sampling of operating or repair times is necessary for Monte Carlo simulation. There are many techniques for generating random numbers from continuous or discrete distribution. The commonly used techniques for simulating continuous random variables are the inverse transformation method, acceptancerejection method, hazard rate method, composition method, and convolution method. The common used techniques for simulating discrete random variables are the inverse alias method developed by Walker (1977), and discrete-inversetransformation method. The particular algorithms for generating random variates from several common occurring continuous distributions, e.g., the Uniform, Exponential, Gamma, Weibull, Lognormal, Normal, $m$-Erlang, for generating random variates from some discrete distributions, e.g., the Binomial, Geometric, Negative Binomial, Poisson, can be found in Law and Kelton (2000).# 12.4 On Monte Carlo Reliability Simulation 

Monte Carlo reliability simulation methods generate random failure times from each component's failure distribution. The overall system reliability is then obtained by simulating system operation and empirically calculating the reliability values for a series of time values. Through the use of computers, simulation has become a very popular analysis tool. Simulation is simple to apply and it can produce results that can be rather difficult to solve analytically. On the other hand, simulation methods also have certain drawbacks, not the least of which is that the results depend on the number of simulations, which results in a lack of repeatability.

Generally, there exist four major difficulties in evaluating complex large-scale system reliability, availability and MTBF:
(a) The system reliability structure may be very complex.
(b) Subsystems may follow different failure distributions.
(c) The failure data of subsystems are sometimes not sufficient. Test sample size or field population tends to be small.
(d) Subsystems may follow arbitrary failure and repair distribution for repairable systems.

Using Monte Carlo technique combined with Bayes method, these four major problems can be solved at the same time. Generally, Monte Carlo simulation methods have the following pros in evaluating system reliability and availability in summary:
(a) Monte Carlo simulation techniques can be used to analyze systems whose subsystems' lifetimes follow various distributions: Binomial, Exponential, Weibull, Lognormal, Gamma, Phase-type, etc. In fact, in engineering practice, all subsystems of a complex system may not follow a single failure distribution. Using classical statistics, it is difficult or impossible to determine the upper and lower bounds on various reliability measures for such systems. Therefore, Monte Carlo approach is a powerful tool to solve this kind of systems.
(b) Monte Carlo simulation methods can be applied to any network configuration and architecture: series, parallel, series-parallel, bridge, $k$ -out-of- $n$, fault-tolerant, etc., no matter how complex the network is, as long as we can determine the system reliability structure function in terms of subsystem reliabilities. For a system with several hundred or more subsystems in complex structures, it is difficult to obtain LCLs of its reliability measures by classical probability and statistics. However, at least in principle, Monte Carlo technique can be applied to evaluate system reliability measures and confidence limits for this kind of systems.
(c) Combining Bayes method, Monte Carlo procedure can easily integrate $a$ priori information into its simulation modules. In practice, some systems tend to possess high reliability and/or be subject to reliability tests withsmall sample sizes or have small field population. For reliability assessment from small testing sample sizes or field population, this Monte Carlo-Bayes method is relatively effective because Bayes method can enlarge failure information of subsystems by using expert experience on similar subsystems' failures (Martz and Waller 1982).
(d) Monte Carlo method can be used to evaluate availability and MTBF of a reparable system. It is noted that so far there are no effective probabilistic and statistical methods for repairable systems with arbitrary time to failure and arbitrary time to repair. Markov chains are usually applied to exponential failures. In addition, Monte Carlo method can simulate availability and MTBF of maintained systems with imperfect maintenance.
(e) After Monte Carlo approaches are programmed in some programming languages, users can easily obtain system reliability and availability interval estimates by inputting the related data into computers. It is not necessary for them to be familiar with Monte Carlo methods applied and the software programs they are using.
(f) Modern computers have made actual Monte Carlo simulation time on computers shorter and shorter for most applications, and it is also convenient to implement Monte Carlo simulation on personal computers which are available almost everywhere now.
(g) By using Monte Carlo simulation, it is easy to find the system reliability and availability confidence interval and point estimates as well as their distributions at any time point $t$.
(h) The accuracy of the results by some Monte Carlo methods can be estimated.
(i) Discrete-event reliability simulation is robust in the modeling of complex system reliability structure and subsystem failure/repair functions.

The drawbacks of Monte Carlo simulation for evaluating system reliability and availability are:
(a) To get Monte Carlo simulation results with high accuracy, the number of simulation operation may becomes very large and computer time will then be increased.
(b) Confidence bounds obtained by some Monte Carlo methods are not exact or narrow enough.
(c) The significant digit number of confidence limits by Monte Carlo is small.

Sreider (1960) states that the error $E$ from Monte Carlo methods is less than some value $d$ generally, where $d$ is approximately equal to $1 / \sqrt{n}$ :

$$
E=|S-A|<d=1 / \sqrt{n}
$$

where $S$ is a simulation result, $A$ is the true value, and $n$ the number of simulationreplications. According to this relationship, the error of Monte Carlo simulation technique decreases as the number of simulation replications increases. However, once $E$ is smaller than certain value, it will no longer decrease basically. That is, it is impossible that $E$ becomes zero. If special techniques for reducing $E$ from Monte Carlo method are not used, this error have a maximum of $0.001-0.1$ (Singh et al. 1993).

Simulation can be used for analyzing any system. However, the accuracy of the results depends on the number of iterations and the complexity of the system. To achieve the desired level of accuracy, the number of simulations can be determined. Analytical methods based on advanced algorithms are in general quicker and produce more accurate results than simulation. Therefore, whenever possible, it is better to use analytical methods. However, if analytical results are not possible or prone to round-off errors, then simulation should be used.

Most Monte Carlo availability assessment, and MTBF estimate algorithms assume that failed components are replaced with new ones at failures, i.e., repair is perfect. As pointed out in Chapter 1, imperfect repair is more general and realistic, so allowing imperfect repair would be future direction for Monte Carlo availability and MTBF simulation.

# 12.5 Commercial Monte Carlo Reliability Simulation Tools 

Worth mentioning is the simulation language. Some existing Monte Carlo programs have used the FORTRAN, BASIC, C, etc., which may limit the adaptability and the scope of analysis. Kim and Fard (1995) state that many existing Monte Carlo simulation programs use a high level language which require considerable programming and development effort. Consequently, the result is a customized application-specific program usually limited in modeling flexibility and capability.

An alternative approach to improve the efficiency and flexibility in reliability modeling and assessment is to use discrete-event simulation language, for example, SIMAN, SLAM, or GPSS.

The good news is that today quite a few commercial general-purpose Monte Carlo reliability and availability simulation programs have appeared, for example, by Relex, Isograph, SoHaR, ReliaSoft, etc. Details on those general-purpose programs can be found in respective internet websites. An example is AvSim+ developed by Isograph. AvSim+ is a Windows-based availability and reliability simulation program capable of analyzing complex and dependent systems. AvSim+ allows users to construct fault tree or network diagrams (reliability block diagrams) using drag and drop facilities. Historical data (times to failure and times to repair) is automatically analyzed using the built-in Weibull Analysis facility and connected directly through to component failure models. This allows users to update their historical data records and almost immediately see the effects on predicted system performance. The AvSim+ Monte Carlo simulator engine enables one to model complex redundancies, common failures and component dependencies which cannot be modeled using standard analytical techniques. Complex dependencies include spares requirements, labor availability, operational phases,and standby arrangements. AvSim+ can also model ageing and effectiveness of planned maintenance, and determine optimal maintenance intervals.

# 12.6 A General Monte Carlo Reliability Procedure 

In Section 12.4, we state the four key difficulties in determining complex system reliability and MTTF interval estimates. Although Monte Carlo-Bayes integrated method can solve these four problems at the same time, so far there are none to fulfill this goal satisfactorily among the existing Monte Carlo algorithms. Examining the typical existing Monte Carlo procedures we can see that the S-R procedure utilizes no a priori information and its accuracy cannot be determined. L-D-L, R-M, and C-H algorithms can only apply to binomial failure distribution. The double Monte Carlo technique (MacDonald 1982) can only deal with Weibull distribution and does not make use of a priori failure information in its simulation model.

Wang and Pham (1997) propose a general Monte Carlo reliability simulation procedure which can apply to any complex systems with arbitrary failure distributions of their subsystems and employs Bayes method to increase failure information.

Assume that subsystems of a system follow different failure distributions. For each kind of failure distribution, using Bayes theorem, we can derive its posterior distribution from its a priori distribution based on engineering experiences of experts and engineers and related testing or field reliability data. Methods for determining posterior distribution have been discussed extensively for various distributions and can been found in Martz and Waller (1982). Based on the posterior failure distributions of all subsystems which possess more failure information, we can use Monte Carlo technique to obtain system reliability and MTTF confidence bounds. Here we can utilize a special Monte Carlo method similar to the S-R algorithm.

Different from the S-R method, the proposed method generates a random sample $T_{i}$ from the posterior distribution of subsystem $i$ for all subsystems. The other steps are the same until we obtain system reliability interval estimates. Then it is easy to obtain system MTTF interval estimates. The procedure for obtaining MTTF intervals is to generate a random sample $T_{i}$ from the posterior distribution of subsystem $i$ for all subsystems first, and then to find the minimum $T_{i}$ from among the $T_{i}$ s generated that make tie-set $j$ unbroken (success) for all tie-sets. Take the maximum of all $T_{i} \mathrm{~s}$ as system MTTF $q_{k}$. Repeating these steps $m$ times, $m$ system MTTFs $q_{1}, q_{2}, \ldots, q_{n}$ are obtained. From them we can finally determine confidence bounds on system MTTF.

The minimal tie-sets can be obtained by using Monte Carlo technique in advance. In fact, we can employ the idea of an existing program "MINCUT" developed by Lin et al. (1993). For details see Lin et al. (1993).

Checking the frequency that the intervals (LCL, 1) cover the true reliability or MTTF we can determine the accuracy of this proposed method.Similar algorithms can be used for Monte Carlo availability and MTBF simulation of maintained systems with imperfect maintenance under different maintenance policies. Various imperfect maintenance situations and maintenance policies can be found in Chapters 1 and 3.# Elements of Reliability and Probability 

The fundamental definitions of statistical reliability must depend on concepts from probability theory. This appendix describes the concepts of system reliability, examines common distribution functions useful in reliability and maintenance engineering and stochastic processes including Markov process, Poisson process, renewal process, and nonhomogeneous Poisson process. In general, a system may be required to perform various functions, each of which may have a different reliability.

## A. 1 Reliability Measures

The reliability definitions given in the literature vary among different practitioners as well as researchers. The generally accepted definition is as follows.

Definition A. 1 Reliability is the probability of success or the probability that the system will perform its intended function under specified design limits.

More specific, reliability is the probability that a product or part will operate properly for a specified period of time (design life) under the design operating conditions (such as temperature, volt, etc.) without failure. Mathematically, reliability $R(t)$ is the probability that a system will be successful in the interval from time 0 to time $t$ :

$$
R(t)=P(T>t) \quad t \geq 0
$$

where $T$ is a random variable denoting the time-to-failure or failure time.
If the time-to-failure random variable $T$ has a density function $f(t)$, then

$$
R(t)=\int_{t}^{\infty} f(s) d s
$$# System Mean Time to Failure 

Suppose that the reliability function for a system is given by $R(t)$. The expected failure time during which a component is expected to perform successfully, or the system mean time to failure (MTTF), is given by

$$
M T T F=\int_{0}^{\infty} t f(t) d t
$$

or equivalently,

$$
M T T F=\int_{0}^{\infty} R(t) d t
$$

Thus, MTTF is the definite integral evaluation of the reliability function. In general, if $\lambda(t)$ is defined as the failure rate function, then, by definition, MTTF is not equal to $1 / \lambda(t)$.

## Failure Rate Function

The hazard function is defined as the limit of the failure rate as the interval approaches zero. Thus, the hazard function $h(t)$ is the instantaneous failure rate, and is defined by

$$
\begin{aligned}
h(t) & =\lim _{\Delta t \rightarrow 0} \frac{R(t)-R(t+\Delta t)}{\Delta t R(t)} \\
& =\frac{1}{R(t)}\left(-\frac{d}{d t} R(t)\right) \\
& =\frac{f(t)}{R(t)}
\end{aligned}
$$

The quantity $h(t) d t$ represents the probability that a device of age $t$ will fail in the small interval of time $t$ to $(t+d t)$. The importance of the hazard function is that it indicates the change in the failure rate over the life of a population of components by plotting their hazard functions on a single axis. For example, two designs may provide the same reliability at a specific point in time, but the failure rates up to this point in time can differ.

The hazard function or hazard rate or failure rate function is the ratio of the probability density function ( $p d f$ ) to the reliability function.

## A. 2 Common Probability Distribution Functions

This section presents some of the common distribution functions and several hazard models that have applications in reliability and maintenance. For each distribution, we will give its distribution form, reliability function, mean, variance, and other useful properties. This appendix is, by no means, comprehensive in its coverage of statistical distributions.# A.2.1 Discrete Random Variable Distributions 

## Binomial Distribution

The binomial distribution is one of the most widely used discrete random variable distributions in reliability and quality inspection. It has applications in reliability engineering, e.g., when one is dealing with a situation in which an event is either a success or a failure.

The binomial distribution can be used to model a random variable $X$ which represents the number of successes (or failures) in n independent trials (these are referred to as Bernoulli trials), with the probability of success (or failure) being $p$ in each trial. The pdf of the distribution is given by

$$
\begin{aligned}
P(X=x) & =\binom{n}{x} p^{x}(1-p)^{n-x} \quad x=0,1,2, \ldots, n \\
\binom{n}{x} & =\frac{n!}{x!(n-x)!}
\end{aligned}
$$

where $n=$ number of trials; $x=$ number of successes; $p=$ single trial probability of success.

## Poisson Distribution

Although the Poisson distribution can be used in a manner similar to the binomial distribution, it is used to deal with events in which the sample size is unknown. A Poisson random variable is a discrete random variable distribution with probability density function given by

$$
P(X=x)=\frac{\lambda^{x} e^{-\lambda}}{x!} \quad \text { for } x=0,1,2, \ldots
$$

where $\lambda=$ constant failure rate; $x=$ is the number of events. In other words, $P(X=$ $x$ ) is the probability of exactly $x$ failures occur.

## Geometric Distribution

Consider a sequence of independent trials, each having the same probability for success, say $p$. Let $N$ be a random variable that counts for the number of trials until the first success. This distribution is called the geometric distribution. It has a pdf given by

$$
P(N=n)=p(1-p)^{n-1} \quad n=1,2, \ldots
$$

The expected value and variance are, respectively

$$
E(N)=\frac{1}{p}
$$

and

$$
V(N)=\frac{1-p}{p^{2}}
$$# Hypergeometric Distribution 

A discrete distribution that arises in sampling, for example, is the hypergeometric distribution. It has a pdf given by

$$
f(x)=\frac{\binom{k}{x}\binom{N-k}{n-x}}{\binom{N}{n}} x=0,1,2, \ldots, n
$$

Typically, $N$ will be the number of units in a finite population; $n$ will be the number of samples drawn without replacement from $N ; k$ will be the number of failures in the population; and $x$ will be the number of failures in the sample.

## A.2.2 Continuous Random Variable Distributions

## Exponential Distribution

Exponential distribution plays an essential role in reliability engineering because it has a constant failure rate. This distribution has been used to model the lifetime of electronic and electrical components and systems. This distribution is appropriate when a used component that has not failed is as good as a new component - a rather restrictive assumption. The $p d f$ and reliability functions are given by, respectively,

$$
\begin{aligned}
& f(t)=\frac{1}{\theta} e^{-\frac{t}{\theta}}=\lambda e^{-\lambda t}, \quad t \geq 0 \\
& R(t)=e^{-\frac{t}{\theta}}=e^{-\lambda t}, \quad t \geq 0
\end{aligned}
$$

where $\theta=1 / \lambda>0$ is an MTTFs parameter and $\lambda \geq 0$ is a constant failure rate.
The hazard function or failure rate for the exponential density function is constant, i.e.,

$$
h(t)=\frac{f(t)}{R(t)}=\frac{1}{\theta}=\lambda
$$

It should be noted that the exponential distribution is the only continuous distribution satisfying

$$
P\{T \geq t\}=P\{T \geq t+s \mid T \geq s\} \quad \text { for } t>0, s>0
$$

## Uniform Distribution

Let us denote $X$ be a random variable having a uniform distribution on the interval $(a, b)$ where $a<b$. The $p d f$ is given by

$$
f(x)=\left\{\begin{array}{cc}
\frac{1}{b-a} & a \leq x \leq b \\
0 & \text { otherwise }
\end{array}\right\}
$$The expected value and variance are, respectively,

$$
E(X)=\frac{a+b}{2}
$$

and

$$
V(X)=\frac{(b-a)^{2}}{12}
$$

# Normal Distribution 

Normal distribution plays an important role in classical statistics owing to the Central Limit Theorem. In reliability engineering, the normal distribution primarily applies to measurements of product susceptibility and external stress. The $p d f$ of the normal random variable is given by

$$
f(t)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left(-\frac{(t-\mu)^{2}}{2 \sigma^{2}}\right) \quad-\infty<t<\infty
$$

where $\mu$ is the mean value and $\sigma$ is the standard deviation.

## Log Normal Distribution

The log normal lifetime distribution is a very flexible model that can empirically fit many types of failure data. The log normal density function is given by

$$
f(t)=\frac{1}{\sigma t \sqrt{2 \pi}} \exp \left(-\frac{(\ln t-\mu)^{2}}{2 \sigma^{2}}\right) \quad-\infty<t<\infty, \quad \sigma>0
$$

where $\mu$ and $\sigma$ are parameters such that $-\infty<\mu<\infty$, and $\sigma>0$. Note that $\mu$ and $\sigma$ are not the mean and standard deviations of the distribution.

Mathematically, if a random variable $X$ is defined as $X=\ln T$, then $X$ is normally distributed with a mean of $\mu$ and a variance of $\sigma^{2}$. That is,

$$
E(X)=E(\ln T)=\mu
$$

and

$$
V(X)=V(\ln T)=\sigma^{2}
$$

The cumulative distribution function for the log normal is

$$
F(t)=\int_{0}^{t} \frac{1}{\sigma s \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{\ln s-\mu}{\sigma}\right)^{2}} d s
$$

and this can be related to the standard normal deviate $Z$ by$$
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

where $\Phi$ is a $c d f$ of standard normal density.

# Weibull Distribution 

The exponential distribution is often limited in applicability owing to the memoryless property. The Weibull distribution (Weibull 1951) is a generalization of the exponential distribution and is commonly used to represent fatigue life, ball bearing life, and vacuum tube life. The three-parameters probability density function is

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

## Gamma Distribution

The gamma distribution can be used as a failure probability function for components whose distribution is skewed. The failure density function for a gamma distribution is$$
f(t)=\frac{t^{\alpha-1}}{\beta^{\alpha} \Gamma(\alpha)} e^{-\frac{t}{\beta}} \quad t \geq 0, \alpha, \beta>0
$$

where $\alpha$ is the shape parameter and $\beta$ is the scale parameter. In this expression, $\Gamma(\alpha)$ is the gamma function, which is defined as

$$
\Gamma(\alpha)=\int_{0}^{\infty} t^{\alpha-1} e^{-t} d t \quad \text { for } \alpha>0
$$

Hence, the gamma reliability function is given by

$$
R(t)=\int_{t}^{\infty} \frac{1}{\beta^{\alpha} \Gamma(\alpha)} s^{\alpha-1} e^{-\frac{s}{\beta}} d s
$$

If $\alpha$ is an integer, it can be shown by successive integration by parts that

$$
R(t)=e^{-\frac{t}{\beta}} \sum_{i=0}^{\alpha-1} \frac{\left(\frac{t}{\beta}\right)^{i}}{i!}
$$

A common use of the gamma lifetime model occurs in Bayesian reliability applications.

# Beta Distribution 

The two-parameter beta density function, $f(t)$, is given by

$$
f(t)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} t^{\alpha-1}(1-t)^{\beta-1} \quad 0<t<1, \alpha>0, \beta>0
$$

where $\alpha$ and $\beta$ are the distribution parameters. This two-parameter beta distribution has commonly used in many reliability engineering applications and also an important role in the theory of statistics. Note that the beta-distributed random variable takes on values in the interval $(0,1)$, so the beta distribution is a natural model when the random variable represents a probability. The mean and variance of the beta distribution are, respectively, given by

$$
E(T)=\frac{\alpha}{\alpha+\beta}
$$

and

$$
V(T)=\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha+\beta)^{2}}
$$

## Pareto Distribution

The Pareto distribution was originally developed to model income in a population. Phenomena such as city population size, stock price fluctuations, and personalincomes have distributions with very long right tails. The probability density function of the Pareto distribution is given by

$$
f(t)=\frac{\alpha k^{\alpha}}{t^{\alpha+1}} \quad k \leq t \leq \infty
$$

# Rayleigh Model 

The Rayleigh model is a flexible lifetime model that can apply to many degradation process failure modes. The Rayleigh probability density function is

$$
f(t)=\frac{t}{\sigma^{2}} \exp \left[\frac{-t^{2}}{2 \sigma^{2}}\right]
$$

## Vtub-shaped Hazard Rate Distribution

Pham (2002) recently developed a two-parameter lifetime distribution with a Vtubshaped hazard rate, also known as Loglog distribution or Pham distribution.

Note that the loglog distribution with Vtub-shaped and Weibull distribution with bathtub-shaped failure rates are not the same. As for the bathtub-shaped, after the infant mortality period, the useful life of the system begins. During its useful life, the system fails as a constant rate. This period is then followed by a wear out period during which the system starts slowly increases with the on set of wear out. For the Vtub-shaped, after the infant mortality period, the system starts to experience at a relatively low increasing rate, but not constant, and then increasingly more failures due to aging.
The probability density function of the distribution is (Pham 2002)

$$
f(t)=\alpha \ln a t^{\alpha-1} a^{t^{\alpha}} e^{1-a^{t^{\alpha}}} \quad \forall t>0, a>0, \alpha>0
$$

The loglog reliability function is given by

$$
R(t)=e^{1-a^{t^{\alpha}}}
$$

The corresponding failure rate of the loglog distribution is given by

$$
h(t)=\alpha \cdot \ln a \cdot t^{\alpha-1} \cdot a^{t^{\alpha}}
$$

## A. 3 Stochastic Processes Concepts

Stochastic processes are used for the description of a systems operation over time. There are two main types of stochastic processes: continuous and discrete. The complex continuous process is a process describing a system transition from state to state. The simplest process that is discussed here is a Markov process. Given the current state of the process, its future behavior does not depend on the past.# A.3.1 Markov Processes 

Definition A. 2 Let $t_{0}<t_{1}<\ldots<t_{n}$. If

$$
\begin{aligned}
P\left[X\left(t_{n}\right)\right. & \left.=A_{n} \mid X\left(t_{n-1}\right)=A_{n-1}, X\left(t_{n-2}\right)=A_{n-2}, \ldots ., X\left(t_{0}\right)=A_{0}\right] \\
& =P\left[X\left(t_{n}\right)=A_{n} \mid X\left(t_{n-1}\right)=A_{n-1}\right]
\end{aligned}
$$

then the process is called a Markov process.
Given the present state of the process, its future behavior does not depend on past information of the process.

The essential characteristic of a Markov process is that it is a process that has no memory; its future is determined by the present and not the past. If, in addition to having no memory, the process is such that it depends only on the difference $(t+d t)-t=d t$ and not the value of $t$, i.e., $P[X(t+d t)=j \mid X(t)=i]$ is independent of $t$, then the process is Markov with stationary transition probabilities or homogeneous in time. This is the same property noted in exponential event times, and referring back to the graphical representation of $X(t)$, the times between state changes would in fact be exponential if the process has stationary transition probabilities.

Thus, a Markov process which is time homogeneous can be described processes where events have exponential occurrence times. The random variable of the process is $X(t)$, the state variable rather than the time to failure as in the exponential failure density.

## A.3.2 Counting Processes

Among discrete stochastic processes, counting processes in reliability engineering are widely used to describe the appearance of events in time, e.g., failures, number of perfect repairs, etc. The simplest counting process is a Poisson process. The Poisson process plays a special role to many applications in reliability (Pham 2000). A well-known counting process is the so-called renewal process. This process is described as a sequence of events, the intervals between which are independent and identically distributed random variables. In reliability theory, this type of mathematical model is used to describe the number of occurrences of an event in the time interval. In this section, we also discuss the quasi-renewal process and the non-homogeneous Poisson process.

A non-negative, integer-valued stochastic process, $N(t)$, is called a counting process if $N(t)$ represents the total number of occurrences of the event in the time interval $[0, \mathrm{t}]$ and satisfies these two properties:
i) If $t_{1}<t_{2}$, then $N\left(t_{1}\right) \leq N\left(t_{2}\right)$
ii) If $t_{1}<t_{2}$, then $N\left(t_{2}\right)-N\left(t_{1}\right)$ is the number of occurrences of the event in the interval $\left[t_{1}, t_{2}\right]$

For example, if $N(t)$ equals the number of persons who have entered a restaurant at or prior to time $t$, then $N(t)$ is a counting process in which an event occurs whenever a person enters the restaurant.# A.3.3 Poisson Processes 

One of the most important counting processes is the Poisson process.
Definition A. 3 A counting process, $N(t)$, is said to be a Poisson process with intensity $\lambda$ if
i) The failure process, $N(t)$, has stationary independent increments
ii) The number of failures in any time interval of length $s$ has a Poisson distribution with mean $\lambda s$, that is,

$$
P\{N(t+s)-N(t)=n\}=\frac{\exp (-\lambda s) \cdot(\lambda s)^{n}}{n!} \quad n=1,2, \ldots
$$

iii) Tthe initial condition is $N(0)=0$

This model is also called a homogeneous Poisson process, indicating that the failure rate $\lambda$ does not depend on time $t$. In other words, the number of failures occurring during the time interval $(t, t+s]$ does not depend on the current time $t$ but only the length of time interval $s$. A counting process is said to possess independent increments if the number of events in disjoint time intervals are independent.

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

This result shows that the Poisson increment process is covariance stationary.

## A.3.4 Renewal Processes

A renewal process is a more general case of the Poisson process in which the inter-arrival times of the process or the time between failures do not necessarily follow the exponential distribution. For convenience, we will call the occurrence of an event a renewal, the inter-arrival time the renewal period, and the waiting time the renewal time.

Definition A. 4 A counting process $N(t)$ that represents the total number of occurrences of an event in the time interval $(0, t]$ is called a renewal process, if thetime between failures are independent and identically distributed random variables.

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
$$

Thus,

$$
\begin{aligned}
P\{N(t)=n\} & =P\{N(t) \geq n\}-P\{N(t)>n\} \\
& =P\left\{W_{n} \leq t\right\}-P\left\{W_{n+1} \leq t\right\} \\
& =F_{n}(t)-F_{n+1}(t)
\end{aligned}
$$

where $F_{n}(t)$ is the cumulative distribution function for the time of the $n^{\text {th }}$ failure and $n=0,1,2, \ldots$

Renewal reward theory is often used in maintenance modeling. Consider a renewal process $\{N(t), t \geq 0\}$ with interarrival times $D_{n}, \forall n, n \geq 1$. Suppose that each time a renewal occurs we receive a reward. Denote by $R_{n}$, the reward earned at the time of the $n^{\text {th }}$ renewal. Assume further that $R_{n}, \forall n, n \geq 1$ are independently and identically distributed, and they may (and usually will) depend on $D_{n}$, the duration of the $n^{\text {th }}$ renewal interval. If we let

$$
R(t)=\sum_{n=1}^{N(t)} R_{n}
$$

then $R(t)$ represents the total reward earned by time $t$. Let

$$
E(R)=E\left(R_{n}\right), \quad E(D)=E\left(D_{n}\right)
$$

Following Ross (1972), we have the following theorem:
Theorem A. 1 (renewal reward). If $E(R)<\infty$ and $E(D)<\infty$, then with probability 1 ,

$$
\frac{R(t)}{t} \rightarrow \frac{E(R)}{E(D)} \quad \text { as } t \rightarrow \infty
$$# A.3.5 Non-homogeneous Poisson Processes 

The non-homogeneous Poisson process model (NHPP) that represents the number of failures experienced up to time $t$ is a non-homogeneous Poisson process $\{N(t), t$ $\geq 0\}$. The main issue in the NHPP model is to determine an appropriate mean value function to denote the expected number of failures experienced up to a certain time.

Note that in a renewal process, the exponential assumption for the inter-arrival time between failures is relaxed, and in the NHPP, the stationary assumption is relaxed.
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

- During a small interval $\Delta t$, the probability of more than one failure is negligible, that is,

$$
P\{\text { two or more failure in }(t, t+\Delta t)\}=o(\Delta t)
$$

- The initial condition is $N(0)=0$.

On the basis of these assumptions, the probability that exactly $n$ failures occurring during the time interval $(0, t)$ for the NHPP is given by

$$
\operatorname{Pr}\{N(t)=n\}=\frac{[m(t)]^{n}}{n!} e^{-m(t)} \quad n=0,1,2, \ldots
$$

where $m(t)=E[N(t)]=\int_{0}^{t} \lambda(s) d s$ and $\lambda(t)$ is the intensity function. It can be easily shown that the mean value function $m(t)$ is non-decreasing.

## Reliability Function

The reliability $R(t)$, defined as the probability that there are no failures in the time interval $(0, t)$, is given by

$$
\begin{aligned}
R(t) & =P\{N(t)=0\} \\
& =e^{-m(t)}
\end{aligned}
$$

In general, the reliability $R(x \mid t)$, the probability that there are no failures in the interval $(t, t+x)$, is given by$$
\begin{aligned}
R(x \mid t) & =P\{N(t+x)-N(t)=0\} \\
& =e^{-\{m(t+x)-m(t)\}}
\end{aligned}
$$

and its density is given by

$$
f(x)=\lambda(t+x) e^{-\{m(t+x)-m(t)\}}
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
$$# References 

Abdel-Hameed M (1987a) An imperfect maintenance model with block replacements. Applied Stochastic Models and Data Analysis 3:63-72
Abdel-Hameed M (1987b) Inspection and Maintenance Policies of Devices subject to deterioration. Advance in Applied Probability 10:917-931
Abdel-Hameed M (1995) Correction to: "Inspection and maintenance policies of devices subject to deterioration. Advance in Applied Probability 27/2:584
Albin SL, Chao S (1992) Preventive replacement in systems with dependent components. IEEE Transactions on Reliability 41/2:230-238
Alexopoulos C, Fishman SG (1988) Stochastic flow networks: How component criticality changes with component reliability. Winter Simulation Conference Proceedings, San Diego, CA, USA, 12-14 Dec 1988
Allan RN, Bhuiyan MR (1994) Application of sequential simulation to the reliability assessment of bulk power systems. Proceedings of the 29th Universities Power Engineering Conference, Part 2 (of 2), Galway, Irel, 1994, pp 763-766
Altiok T (1996) Performance Analysis of Manufacturing Systems. Springer
Amato HN, Anderson EE (1976) Determination of warranty reserves: an extension. Management Science 22/12:854-862
Archibald TW, Dekker R(1996) Modified block-replacement for multiplecomponent systems. IEEE Transactions on Reliability 45/1, 75-83
Arjas E, Norros I (1989) Change of life distribution via a hazard transformation: an inequality with application to minimal repair. Mathematics of Operations Research 14/2:355-361
Arjas E, Norros I (1990) Should minimal repair depend on information? In: Block HW, Sampson AR, Savits TH (eds) Proceedings of the Symposium on Dependence in Probability and Statistics. (held in Somerset, Pennsylvania, August 1-5, 1987; IMS Lecture Notes Monograph Ser., 16) Inst. Math. Statist., Hayward, CA.Arsham H (1989) On the inverse problem in Monte Carlo experiments. Inverse Problems 5/6:927-934
Asher H, Feingold H (1984) Repairable Systems Reliability. Marcel Dekker, New York
Assaf D, Shanthikumar JG (1987) Optimal group maintenance policies with continuous and periodic inspections. Management Science 33:1440-1450
Aven T (1983) Optimal replacement under a minimal repair strategy - a general failure model. Advances in Applied Probability 15/1:198-211
Aven T (1985) Determination/estimation of an optimal replacement interval under minimal repair. Optimization: A Journal of Mathematical Programming and Operations Research 16/5:743-754
Aven T, Jensen U (1999) Stochastic Models in Reliability. Springer-Verlag, New York
Baca A (1993) Examples of Monte Carlo methods in reliability estimation 'based on reduction of prior information. IEEE Transactions on Reliability 42/4:645649
Bai J (2004) On the study of warranties for repairable complex systems. PhD Dissertation, Rutgers University, USA
Bae SI, Ichikawa M (1993) Attempt to unify reliability and confidence level in reliability-based design (The case of 2-parameter Weibull distribution). Nippon Kikai Gakkai Ronbunshu, A Hen/Transactions of the Japan Society of Mechanical Engineers, Part A, 59/558:478-482
Bai J, Pham H (2004) Discounted warranty cost for minimally repaired series systems. IEEE Transactions on Reliability 53/1:37-42
Bai J, Pham H (2005) Repair-limit risk-free warranty policies with imperfect repair. IEEE Trans. on Systems, Man, and Cybernetics (Part A) 35/6:765-772
Bai J, Pham H (2006a) Cost analysis on renewable full-service warranties for multi-component systems. European Journal of Operational Research 168/2: 492-508

Bai J, Pham H (2006b) Promotional warranty policies: analysis and perspectives. In Pham H (ed) Springer Handbook of Engineering Statistics. Springer, London.
Balaban HS, Singpurwalla ND (1984) Stochastic properties of a sequence of interfailure times under minimal repair and under revival. In: Abdel Hameed MS, Cinlar E, Quinn J (eds) Reliability Theory and Models. Academic Press, Orlando, Fla., pp 65-80
Balachandran KR, Maschmeyer RA, Livingstone JL (1981) Product warranty period: A Markovian approach to estimation and analysis of repair and replacement costs. The Accounting Review 1:115-124
Balasubramanya KS, Vasudevan S, Rao PK (1985) State transition Monte Carlo simulation of electronic systems. IREECON, International (Convention Digest) (Institution of Radio and Electronics Engineers Australia) 2:730-732Barlow RE, Hunter LC (1960) Optimum preventive maintenance policies. Operations Research 8:90-100
Barlow RE, Proshan F (1965) Mathematical Theory of Reliability. John Wiley \& Sons, New York
Barlow RE, Proshan F (1975) Statistical Theory of Reliability and Life Testing. Holt, Renehart \& Winston, New York
Baxter LA. (1982) Reliability applications of the relevation transform. Naval Research Logistics Quarterly 29:323-330
Beichelt F (1976) A general preventive maintenance policy. Mathematische Operationsforschung und Statistik Series, Statistics 7:927-932
Beichelt F (1978) A new approach to repair limit replacement policies. Transactions of the Eighth Prague Conference on Information Theory, Statistical Decision Functions, Random Processes, Prague, vol.C, pp 31-37
Beichelt F (1981a) A generalized block-replacement policy. IEEE Transactions on Reliability R-30/2:171-173
Beichelt F (1981b) Replacement policies based on system age and maintenance cost limits. Mathematische Operationsforschung und Statistik Series, Statistics 12/4:621-627
Beichelt F, Fischer K (1980) General failure model applied to preventive maintenance policies. IEEE Transactions on Reliability R-29/1:39-41
Bererhoff OA (1963) Confidence limits for system reliability based on component test data. AD-42845, available from National Technical Information Service (NTIS), Department of Commerce, Springfield, VA22161, USA
Berg M (1976a) A proof of optimality for age replacement policies. Journal of Applied Probability 13:751-759
Berg M (1976b) Optimal replacement policies for two-unit machines with increasing running costs - I. Stochastic Processes and Applications 5:89-106
Berg M (1978) General trigger-off replacement procedures for two-unit systems. Naval Research Logistics 25:15-29.
Berg M, Epstein B (1976) A modified block replacement policy. Naval research Logistics 23:15-24
Berg M, Epstein B (1978) Comparison of age, block, and failure replacement. IEEE Transactions on Reliability R-27/1:25-29
Bergman B (1978) Optimal replacement under a general failure model. Advances in Applied Probability 10/2:431-451
Bergman B (1980) On the optimality of stationary replacement strategies. Journal of Applied Probability 17:178-186
Bertoldi O, Rivoiro A, Salvadori L (1994) New trends in power system planning and related effect on the reliability evaluation. Reliability Engineering \& System Safety 46/1:49-61Bhat KS, Gururajan M (1993) A two-unit cold standing system with imperfect repair and excessive availability period. Microelectronics and Reliability 33/4:509-514

Bhattacharjee MC (1987) New results for the Brown-Proschan model of imperfect repair. Journal of Statistical Planning and Inference 16:305-316
Bianu A, Frant S, Gurevich V (1995) Generation system reliability model with Monte Carlo simulation. Proceedings of the 18th Convention of Electrical and Electronics Engineers in Israel, pp 3.1.4/1-5
Billinton R, Li W (1991a) Composite system reliability assessment using a Monte Carlo approach. Third International Conference on Probabilistic Methods Applied to Electric Power Systems, London, UK, 1991 Jul 3-5
Billinton R, Li W (1991b) Hybrid approach for reliability evaluation of composite generation and transmission systems using Monte-Carlo simulation and enumeration technique. IEE Proceedings, Part C: Generation, Transmission and Distribution 138/3:233-241
Billinton R, Li W (1992) A Monte Carlo method for multi-area generation system reliability assessment. IEEE Transactions on Power Systems 7/4:1487-1492
Billinton R, Lian G (1993) Monte Carlo approach to substation reliability evaluation. IEE Proceedings, Part C: Generation, Transmission and Distribution 140/2:147-152
Blacer Y, Sahin I (1986) Replacement costs under warranty: cost moments and time variability. Operations Research 34/4:554-559
Blischke WR (1990) Mathematical models for analysis of warranty policies. Math. Comput. Model 13:1-16
Blischke WR, Murthy DNP (1993) Product warranty management-I: A taxonomy for warranty policies. European Journal of Operational Research 62:127-148
Blischke WR, Murthy DNP (1994) Warranty Cost Analysis. Marcel Dekker
Blischke WR, Murthy DNP (eds) (1996) Product Warranty Handbook. Marcel Dekker

Blischke WR, Scheuer EM (1975) Calculating the cost of warranty policies as a function of estimated life distributions. Naval Research Logistics Quarterly 28:193-205
Bloch-Mercier S (2002) A preventive maintenance policy with sequential checking procedure for a Markov deteriorating system. European Journal of Operational Research 147:548-576
Block HW, Borges WS, Savits TH (1985) Age dependent minimal repair. Journal of Applied Probability 22:370-385
Block HW, Borges WS, Savits TH (1988) A general age replacement model with minimal repair. Naval Research Logistics, An International Journal 35/5:365372
Block HW, Langberg NA, Savits TH (1990) Comparisons for maintenance policies involving complete and minimal repair. In: Block HW, Sampson AR, SavitsTH (eds) Proceedings of the Symposium on Dependence in Probability and Statistics. (held in Somerset, Pennsylvania, August 1-5, 1987. IMS Lecture Notes Monograph Ser. 16 ) Inst. Math. Statist., Hayward, CA.
Block HW, Langberg NA, Savits TH (1993) Repair replacement policies. Journal of Applied Probability 30/1:194-206
Blumenthal S, Greenwood JA, Herbach LH (1976) A comparison of the bad as old and superimposed renewal models. Management Science 23/3:280-285
Boehm F, Hald UP, Lewis EE (1988) Parts renewal in continuous-time Monte Carlo reliability simulation. Proceedings of the Annual Reliability and Maintainability Symposium, pp 345-349
Boland PJ (1982) Periodic replacement when increasing minimal repair costs vary with time. Naval Research Logistics 29:541-546
Boland PJ, El-Neweihi E (1998) Statistical and information based (physical) minimal repair for $k$ out of $n$ systems. Journal of Applied Probability 35/3:731740
Boland PJ, Proschan F (1982) Periodic replacement with increasing minimal repair costs at failure. Operations Research 30:1183-1189
Boland PJ, El-Neweihi E, Proschan F (1991) Stochastic order for inspection and repair policies. The Annals of Applied Probability 1/2:207-218
Brennan JR (1994) Warranties: Planning, Analysis and Implementation. McGrawHill, New York
Bris R, Chatelet E, Yalaoui F (2003) New method to minimize the preventive maintenance cost of series-parallel systems. Reliability Engineering and System Safety 82:247-255
Brown M, Proschan F (1982) Imperfect maintenance. In: IMS Lecture NotesMonograph Ser. 2: Survival analysis. Inst. Math. Statist., Hayward, Calif., pp $179-188$

Brown M, Proschan F(1983) Imperfect repair. Journal of Applied Probability 20:851-859
Buehler RJ (1957) Confidence intervals for the product of two binomial parameters. J. American Statistical Assoc. 52:482-493
Bustamante AS (1988) Monte Carlo methods in Reliability Engineering. In: Amendola A, Bustamantre AS (eds) Proceedings of the ISPRA. Kluwer Academic Publishers
Campioni L, Scardovelli R, Vestrucci P (2005) Biased Monte Carlo optimization: the basic approach. Reliability Engineering \& System Safety 87/3: 387-94
Canfield RV (1986) Cost optimization of periodic preventive maintenance. IEEE Transactions on Reliability R-35/1:78-81
Carter LL, Miles TL, Binney SE (1993) Quantifying the reliability of uncertainty predictions in Monte Carlo fast reactor physics calculations. Nuclear Science and Engineering 113/4:324-338Cha JH, Kim JJ (2001) On availability of Bayesian imperfect repair model. Statistics \& Probability Letters 53/2:181-187
Chan PKW, Downs T (1978) Two criteria for preventive maintenance. IEEE Transactions on Reliability R-27:272-273
Chan JK, Shaw L (1993) Modeling repairable systems with failure rates that depend on age \& maintenance. IEEE Transactions on Reliability 42:566-570
Chang M, Parks GT, Lewins JD (2001) Estimation of system reliability by variationally processed Monte Carlo simulation. In: Pham H (ed) Recent Advances in Reliability and Quality Engineering. World Scientific, New Jersey, pp 93-122
Chao A, Huwang LC (1987) A modified Monte Carlo technique for confidence limits of system reliability using pass-fail data. IEEE Trans. reliability R-36:109-112
Chaudhuri D, Sahu KC (1977) Preventive maintenance intervals for optimal reliability of deteriorating system. IEEE Transactions on Reliability R-26:371372
Chelbi A, Ait-Kadi D (1999) An optimal inspection strategy for randomly failing equipment. Reliability Engineering and System Safety 63:127-131
Chen J, Yao DD, Zheng S (1988) Quality control for products supplied with warranty. Operations Research, 46/1:107-115
Chen M, Feldman RM (1997) Optimal replacement policies with minimal repair and age-dependent costs. European Journal of Operational Research 98/1:7584
Cho ID, Parlar M (1991) A survey of maintenance models for multi-unit systems. European Journal of Operational Research 51:1-23
Chukova S, Dimitrov B (1996) Warranty analysis for complex systems. In: Blischke WR, Murthy DNP (eds) Product Warranty Handbook, Chapter 22. Marcel Dekker, pp 543-584
Chun YH (1992) Optimal number of periodic preventive maintenance operations under warranty. Reliability Engineering \& System Safety 37/3:223-225
Chun YH (1992) Optimal number of periodic preventive maintenance operations under warranty. Reliability Engineering and System Safety 37:223-225
Chun YH, Tang K (1995) Determining the optimal warranty price based on the producer's and customers' risk preferences. European Journal of Operational Research 85:97-110
Chun YH, Tang K (1999) Cost analysis of two-attribute warranty policies based on the product usage rate. IEEE Transactions on Engineering Management 46/2:201-209
Cinlar E (1975) Introduction to Stochastic Processes. Prentice-Hall, Englewood Cliffs, NJ
Cox DR (1962) Renewal Theory. Methuen, LondonCox DR (1972) Regression models and life tables (with discussion). Royal Statistical Society B 34:187
Crawford RH, Rao SS (1987) Reliability analysis of function generating mechanisms through Monte Carlo simulation. Advances in Design Automation, Volume Two: Robotics, Mechanisms, and Machine Systems. Boston, MA, USA, 1987 Sep 27-30
Csenki A (1989) Improved Monte Carlo method in structural reliability. Reliability Engineering \& System Safety 24/3:275-292
Dagpunar JS (1996) Maintenance model with opportunities and interrupt replacement options. Journal of the Operational Research Society 47/11:14061409
Dagpunar JS (1999) New approach for solving repair limit problems. European Journal of Operational Research 113/1:137-146
Dagpunar JS, Jack N (1992) Optimal repair-cost limit for a consumer following expiry of a warranty. IMA Journal of Mathematics Applied in Business and Industry 4:155-161
Dagpunar JS, Jack N (1994) Preventative maintenance strategy for equipment under warranty. Microelectronics and Reliability 34/6:1089-1093
Davani D (1994) Parametric what-if analysis in MTTF: a single-run Monte-Carlobased approach. Microelectronics \& Reliability 34/2:275
DeCroix GA (1999) Optimal warranties, reliabilities and prices for durable goods in an oligopoly. European Journal of Operational Research 112:554-569
DeGroot MH (1984) Probability and Statistics, 2nd edn. Addison-Wesley
Dekker R (1996 ) Applications of maintenance optimization models: a review and analysis. Reliability Engineering \& System Safety 51/3:229-240
Dekker R, Roelvink IFK (1995) Marginal cost criteria for preventive replacement of a group of components. European Journal of Operational Research 84/2:467-480
Dekker R, Wilderman RE, van der Duyn Schouten FA (1997) A review of multicomponent maintenance models with economic dependence. Math. Methods Oper. Res. 45/3:411-435
Depuy M, Hobbs JR, Moore AH, Johnson JW (1982) Accuracy of univariate, bivariate, and a 'modified double Monte Carlo' technique for finding lower confidence limits of system reliability. IEEE Trans Reliability R31:474-477
Devooght J, Dubus A, Smidts C (1990) Suboptimal inspection policies for imperfectly observed realistic systems. European Journal of Operational Research 45/2-3:203-218
Dey DK, Lee TM (1992) Bayes computation for life testing and reliability estimation. IEEE Transactions on Reliability 41/4:621-626
Dias JR (1990) Some approximate inspection policies for a system with imperfect inspections. RAIRO Recherche Operationnelle 24/2:191-199Dieulle L, Berenguer C, Gralland A, Roussignol M (2003) Sequential conditionbased maintenance scheduling for a deteriorating system. European Journal of Operational Research150:451-461
Djamaludin I, Murthy DNP (1994) Quality control through lot sizing for items sold with warranty. International Journal of Production Economics 33:97-107
Djamaludin I, Murthy DNP (2001) Warranty and preventive maintenance. International Journal of Reliability, Quality and Safety Engineering 8:89-107
Dohi T, Matsushima N, Kaio N, Osaki S (1997) Nonparametric repair-limit replacement policies with imperfect repair. European Journal of Operational Research 96/2:260-273
Dohi T, Kaio N, Osaki S (1998) On the optimal ordering policies in maintenance theory - survey and applications. Appl. Stochastic Models Data Anal. 14/4:309321
Dohi T, Kaio N, Osaki S (2000) A graphical method to repair-cost limit replacement policies with imperfect repair. Mathematical and Computer Modelling 31:99-106
Doshay I (1971) System availability and service simulation; on-line program using Monte-Carlo model. IEEE Trans. on Reliability R20:142-147
Downs T (1985) An approach to the modeling of software testing with some applications. IEEE Trans. Software Engineering se-11/4:356-363
Doyen L, Gaudoin O (2004) Classes of imperfect repair models based on reduction of failure intensity or virtual age. Reliability Engineering and System Safety 84/1:45-56
Drinkwater RW, Hastings NVJ (1967) An economic replacement model. Oper. Res. Quart. 18:121-138
Dubi A, Gandini A, Goldfeld A, Righini R (1989) New multipurpose Monte-carlo code for reliability analysis of complex systems: Application to a FBR decay heat removal system. Reliability '89, Part 1, London, UK, 1989 Jun 14-16 (Publ by Inst of Quality Assurance, London), pp 2B/6/1-2B/614
Dubi A, Gandini A, Goldfeld A, Righini R, Simonot H (1991) Analysis of nonmarkovian systems by a Monte-Carlo method. Annals of Nuclear Energy 18/3:125-130
Easton MC, Wong CK (1980) Sequential destruction method for Monte Carlo evaluation of system reliability. IEEE Trans. Reliability R-29:27-32
Ebrahimi N (1986) Two new replacement policies. IEEE Transactions on Reliability 42/1:141-145
Efton B (1979) Bootstrap method: another look at the jackknife. Annals of Statistics 7:1-26
Ehrlich W, Prasanna B, Stampfel J, Wu J (1993) Determining the cost of a stoptesting decision. IEEE Trans. Software Engineering 19:33-42
Elperin T, Gertsbakh I, Lomonosov M (1991) Estimation of network reliability using graph evolution models. IEEE Transactions on Reliability 40/5:572-581Emons W (1988) Warranties, moral hazard, and the lemons problem. Journal of Economic Theory 46:16-33
Emons W (1989) On the limitation of warranty duration. Journal of Industrial Economics 37:287-301
Faddy MJ (1995) Phase-type distributions for failure times. Mathematical and Computer Modeling 22:63-70
Faddy MJ, Wilson RJ (2000) Compartmental modeling of equipment subject to partial repair. Mathematical and Computer Modeling 31:115-120
Feller W (1966) An Introduction to Probability Theory and Its Applications, vol.II. John Wiley and Sons, New York
Feller W (1968) An Introduction to Probability Theory and Its Applications, vol.I, 3rd ed. John Wiley and Sons, New York
Finkelstein MS (1992) Some notes on two types of minimal repair. Advances in Applied Probability 24/1:226--228
Finkelstein MS (1997) Imperfect repair models for systems subject to shocks. Applied Stochastic Models \& Data Analysis 13/3-4:385-390
Fishman GS (1986a) A comparison of four Monte Carlo methods for estimating the probability of $s-t$ connectedness. IEEE Trans. Reliability R-35:145-154
Fishman GS (1986b) A Monte Carlo sampling plan for estimating network reliability. Operations Research 34:581-592
Fishman GS (1987a) A Monte Carlo sampling plan for estimating reliability parameters and related functions. Networks 17:169-186
Fishman GS (1987b) Distribution of maximum flow with applications to multistate reliability systems. Operations Research 35/4:607-618
Fishman GS (1987c) Monte Carlo estimation of function variation. Winter Simulation Conference Proceedings 1987, Atlanta, GA, USA, 1987 Dec 14-16 ( Available from IEEE Service Cent (Cat n 87CH2512-2), Piscataway, NJ, USA), pp 347-350
Fishman GS (1989) Estimating the s-t reliability function using importance and stratified sampling. Operations Research 37/3:462-473
Flynn J (1988) Optimal replacement policies for a multicomponent reliability system. Operations Research Letters 7/4:167-172
Fontenot RA, Proschan F (1984) Some imperfect maintenance models. In: Abdel Hameed MS, Cinlar E, Quinn J (eds) Reliability Theory and Models. Academic press, Orlando, Fla.
Frees EW (1986) Warranty analysis and renewal function estimation. Naval Research Logistics Quarterly 33:361-372
Frees EW (1988) Estimating the cost of a warranty. Journal of Business and Economic Statistics 6/1:79-86Frenk H, Dekker R, Kleijn M (1997) A unified treatment of single component replacement models, Stochastic models of reliability. Mathematical Methods of Operations Research 45/3:437-454
Gasmi S, Love CE, Kahle W (2003) A General Repair, Proportional-Hazards, Framework to Model Complex Repairable Systems. IEEE Trans. on Reliability $52 / 1: 26-32$
Gatliffe TR (1976) Accuracy analysis for a lower confidence limit procedure for system reliability. AD-A 031817, available from US NTIS
Geist RM, Smotherman MK (1989) Ultrahigh reliability estimates through simulation. Annual Reliability and Maintainability Symposium - 1989 Proceedings, Atlanta, GA, USA, 1989 Jan 24-26. Available from IEEE Service Cent (cat n 89CH2580-9), Piscataway, NJ, USA., pp 350-355
Gertsbakh IB (1977) Models of Preventive Maintenance. North-Holland, Amsterdam
Gertsbakh IB (1989) Optimal dynamic opportunistic replacement with random resupply of spare parts. Communications in Statistics, Stochastic Models $5 / 2: 315-326$
Ghajar R, Billinton R (1988) Monte Carlo simulation model for the adequacy evaluation of generating systems. Reliability Engineering \& System Safety 20/3: 173-186
Glickman TS, Berger PD (1976) Optimal price and protection period decisions for a product under warranty. Management Science 22:1381-1390
Goel AL (1985) Software reliability models: assumptions, limitations, and applicability. IEEE Trans. Software Engineering se-11/12:1411-1423
Goel LR, Taiga VK (1993) A two unit series system with correlated failures and repairs. Microelectronics and Reliability 33/14:2165-9
Goel LR, Shrivastava P, Gupta R (1992) Two unit cold standby system with correlated failures and repairs. International Journal of Systems Science 23/3:379-391
Goel LR, Gupta R, Tyagi PK (1993) Cost benefit analysis of a complex system with correlated failures and repairs. Microelectronics and Reliability 33/15: 2281-4
Goel LR, Mumtaz SZ, Gupta R (1996) A 2-Unit Duplicating Standby System with Correlated Failure Repair Replacement Times. Microelectronics and Reliability 36/4:517-523
Grall A, Berenguer C, Dieulle L (2002a) A condition-based maintenance policy for stochastically deteriorating systems. Reliability Engineering and System Safety 76:167-180
Grall A, Dieulle L, Berenguer C, Roussignol M (2002b) Continuous-time predicttive-maintenance scheduling for a deteriorating system. IEEE Trans. on Reliability 51/2:141-150Gubbala N, Singh C (1995) Models and considerations for parallel implementation of Monte Carlo simulation methods for power system reliability evaluation. IEEE Transactions on Power Systems 10/2:779-787
Guo R, Love CE (1992) Statistical analysis of an age model for imperfectly repaired systems. Quality and Reliability Engineering International 8:133-146
Gupta R (1999) Profit analysis of a system with mutual changeover of units and correlated failures and repairs. Journal of Quality in Maintenance Engineering $5 / 2: 128-140$

Gupta RC, Kirmani SNUA (1988) Closure and momotonicity properties of nonhomogeneous Poisson processes and record values. Probability in the Engineering and Informational Science 2:475-484
Gupta RC, Kirmani SNUA (1989) On predicting repair times in a minimal repair process. Communications in Statistics, Simulation and Computation 18/4:13591368
Gupta S (1984) Replacement policies involving idle time and minimal repair under Markov renewal processes. Journal of the Indian Statistical Association 22:5362

Gupta YP, Chand S (1993) Strategies of replacement under Markov renewal process. International Journal of Information and Management Sciences $4 / 1: 41-50$

Gururajan M, Stanley ADJ (1988) A complex two unit system with priority and imperfect repair. IAPQR Transactions, Journal of the Indian Association for Productivity, Quality and Reliability 13/1:65-70
Gutjahr WJ (1995) Optimal test distributions for software failure cost estimation. IEEE Trans. Software Engineering 21/3:219-228
Hammersley JM, Handscomb DC (1964) Monte Carlo Method. Methuen and Co. Ltd, London
Haringa GE, Jordan GA, Garver LL (1991) Application of Monte Carlo simulation to multi-area reliability evaluations. IEEE Computer Applications in Power $4 / 1: 21-25$

Hegde GG, Kubat P (1989) Diagnosis design: A product support strategy. European Journal of Operational Research 38:35-43
Heidergott B (1999) Optimization of a single-component maintenance system: A smoothed perturbation analysis approach. European Journal of Operational Research 119:181-190
Helvic BE (1980) Periodic maintenance, on the effect of imperfectness. 10th Int. Symp. Fault-tolerant Computing, pp 204-206
Henley J, Kumamoto H (1981) Reliability Engineering and Risk Assessment. Prentice-Hall
Heyman D, Sobel MJ (1982) Stochastic Models in Operations Research (vol. I). McGraw-HillHeyman D, Sobel MJ (1984) Stochastic Models in Operations Research (vol. II). McGraw-Hill
Hill VL, Beall CW, Blischke WR (1998) A simulation model for warranty analysis. International Journal of Production Economics 16:463-491
Hollander M, Presnell B, Sethuraman J (1992) Nonparametric methods for imperfect repair models. The Annals of Statistics 20/2:879-887
Holmberg K, Folkeson A (eds) (1991) Operational Reliability and Systematic Maintenance. Elsevier Applied Science, London
Hopp WJ, Wu SC (1988) Multiaction maintenance under Markovian deterioration and incomplete state information. Naval Research Logistics, An International Journal 35/5:447-462
Hosseini MM, Kerr RM, Randall RB (2000) An inspection model with minimal and major maintenance for a system with deterioration and Poisson failures. IEEE Trans. Reliability 49/1:88-98
Huang JS, Okogbaa OG (1996) A heuristic replacement scheduling approach for multi-unit systems with economic dependency. International Journal of reliability, Quality, and safety Engineering 3/1:1-10
Hudes ES (1979) Availability theory for systems whose components are subjected to various shut-off rules. Ph.D. dissertation, Department of Statistics, University of California, Berkeley, USA
Hussain AZMO, Murthy DNP (1998) Warranty and redundancy design with uncertain quality. IIE Transactions 30:1191-1199
Ingle AD, Siewiorek DP (1977) Reliability models for multiprocessor systems with and without periodic maintenance. 7th Int. Symp. Fault-Tolerant Computing, pp 3-9
Isaacson D, Reid S, Brennan J (1991) Warranty cost-risk analysis. Proceedings of the Annual Reliability and Maintainability Symposium, pp 332-339
Iskandar BP, Sandoh H (1999) An opportunity-based age replacement policy considering warranty. International Journal of Reliability, Quality and Safety Engineering 6:229-236
Iyer S (1992) Availability results for imperfect repair. Sankhya: the Indian Journal of statistics 54/2:249-259.
Ja S, Kulkarni V, Mitra A, Partaker G (2001) A renewable minimal-repair warranty policy with time-dependent costs. IEEE Transactions on Reliability 50/4:346-352
Ja S, Kulkarni V, Mitra A, Partaker G (2002) Warranty reserves for non-stationary sales processes. Naval Research Logistics 49/5:499-513
Jack N (1991) Repair replacement modeling over finite time horizons. Journal of the Operational Research Society 42/9:759-766
Jack N, Dagpunar JS (1994) An optimal imperfect maintenance policy over a warranty period. Microelectronics and Reliability 34:529-534Jacobsen SE, Arunkumar S (1973) Investment in series and parallel systems to maximize expected life. Management Science 19:1023-1028
Jardine AKS, Buzacott JA (1985) Equipment reliability and maintenance. European Journal of Operational Research 19:285-296
Jayabalan V, Chaudhuri D (1992a) Optimal maintenance and replacement policy for a deteriorating system with increased mean downtime. Naval Research Logistics 39:67-78.
Jayabalan V, Chaudhuri D (1992b) Cost optimization of maintenance scheduling for a system with assured reliability. IEEE Transactions on Reliability R-41/1:21-26
Jayabalan V, Chaudhuri D (1992c) Sequential imperfect preventive maintenance policies: A case study. Microelectronics and Reliability 32/9:1223-1229
Jayabalan V, Chaudhuri D (1992d) Optimal maintenance - Replacement policy under imperfect maintenance. Reliability Engineering \& System Safety 36/2:165-169.
Jayabalan V, Chaudhuri D (1992e) Heuristic approach for finite time maintenance policy. International Journal of Production Economics 27/3:251-256
Jayabalan V, Chaudhuri D (1995) Replacement policies: a near optimal algorithm. IIE Transactions 27:784-788
Jensen U (1995) Stochastic models of reliability and maintenance: an overview. In: Ozekici S (ed) Reliability and maintenance of complex systems. (Proceedings of the NATO Advanced Study Institute on Current Issues and Challenges in the Reliability and Maintenance of Complex Systems, held in Kemer-Antalya, Turkey, 12- 22 June 1995) Springer-Verlag, Berlin., pp 3-36
Jia X, Christer AH (2002) A periodic testing model for a preparedness system with a defective state. IMA Journal of Management Mathematics 13/1:39-49
Jiang X, Cheng K, Makis V (1998) On the optimality of repair-cost-limit policies. Journal of Applied Probability 35/4:936-949
Jin G, Chen L, Dong J (1993) Monte Carlo finite element method of structure reliability analysis. Reliability Engineering \& System Safety 40/1:77-83
Johnson NI, Kotz S (1970) Distributions in Statistics: Continuous Univariate Distributions-1. Houghton Mifflin Co, Boston
Johnson R, Wichern D (2002) Applied Multivariate Statistical Analysis, $5^{\text {th }}$ edn. Prentice Hall
Jorion P (2000) Value-at-Risk: The New Benchmark for Managing Financial Risk. McGraw-Hill
Kaio N, Osaki S (1982) Optimum repair limit policies with time constraint. International Journal of Systems Science 13:1345-1982
Kalbfleisch JD, Lawless JF, Robinson JA.(1991) Methods for the analysis and prediction of warranty claims. Technometrics 33:273-285Kamat SJ, Riley MW (1975) Determination of reliability using event-based Monte Carlo simulation. IEEE Transactions on reliability R-24/1:73-75
Kamat SJ, Franzmeier WE (1976) Determination of reliability using event-based Monte Carlo simulation II. IEEE Transactions on reliability R-25/4:254-255
Kaminskiy M, Krivtsov V (2000) G-renewal process as a model for statistical warranty claim prediction. Proceedings Annual Reliability and Maintainability Symposium, pp 276-280
Kao EPC (1998) Computing the phase-type renewal and related functions. Technometrics 30/1:87-93
Kao EPC, Smith MS (1992) On excess, current and total life distributions of phasetype renewal processes. Naval Research Logistics 39:789-799
Kao EPC, Smith MS (1996) Computational approximations of renewal process relating to a warranty problem: the case of phase-type lifetimes. European Journal of Operational Research 90:156-170
Kapur PK, Garg RB, Butani NL (1989) Some replacement policies with minimal repairs and repair cost limit. International Journal of Systems Science 20/2:267279

Karpinski J (1986) Multistate system under an inspection and repair. IEEE Transactions on Reliability R-35/1:76-77
Kay E (1976) The effectiveness of preventive maintenance. Int. J. Prod. Res. 14:329-344
Kececioglu D, Jiang S (1990) Error band estimation on Monte Carlo simulations. Proceedings of the 36th Annual Technical Meeting of the Institute of Environmental Sciences, New Orleans, LA, USA, 1990 Apr 23-27
Keller AZ (1987) Monte Carlo simulation in reliability. In: Colombo AG, Keller AZ (eds) Proceedings of the ISPRA. D.Reidel Publishing Co.
Khalil ZS (1985) Availability of series systems with various shut-off rules. IEEE Transaction Reliability 34:187-189
Kijimma M (1989) Some results for repairable systems with general repair. Journal of Applied Probability 26:89-102
Kijima M (1992) Replacement policies of a shock model with imperfect preventive maintenance. European Journal of Operational Research 57:100-110
Kijima M, Nakagawa T (1991) Accumulative damage shock model with imperfect preventive maintenance. Naval research Logistics 38:145-156
Kijima M, Nakagawa T (1992) Replacement policies of a shock model with imperfect preventive maintenance. European Journal of Operations Research 57:100-110
Kijima M, Morimura H, Suzuki Y (1988) Periodical replacement problem without assuming minimal repair. European Journal of Operational Research 37/2:194203Kim J, Fard N (1995) Discrete-event simulation of network reliability and Markovian models. International Journal of Modeling and Simulation
Kim C, Lee HK (1992) A Monte Carlo simulation algorithm for finding MTBF. IEEE Transactions on Reliability 41/2:193-195
Kim HG, Rao BM (2000) Expected warranty cost of two-attribute freereplacement warranties based on a bivariate exponential distribution. Computers and Industrial Engineering 38:425-434
Kirmani SNUA, Gupta RC (1989) On repair age and residual repair life in the minimal repair process. Probability in the Engineering and Informational Science 3:381-391
Kirmani SNUA, Gupta RC (1992) Some moment inequalities for the minimal repair process. Probability in the Engineering and Informational Science 6:245-255
Klein JP, Moeschberger ML (1997) Survival Analysis: Techniques for Censored and Truncated Data. Springer
Klutke GA, Yang YJ (2002) The availability of inspected systems subjected to shocks and graceful degradation. IEEE Trans. on Reliability 44:371-374
Kochar SC (1996) Some results on interarrival times of nonhomogeneous Poisson processes. Probability in the Engineering and Informational Science 10:75-85
Koshimae H, Tanaka H, Osaki S (1994) Some remarks on MTBF's for nonhomogeneous Poisson processes. IEICE Trans. on Fundamentals of Electronics, Communications and Computer sciences E77-A/1:144-149
Koshimae H, Dohi T, Kaio N, Osaki S (1996) Graphical/statistical approach to repair limit replacement problem. Journal of the Operations Research Society of Japan 39:230-246
Kreps DM (1990) A Course in Microeconomic Theory. Princeton University Press, Princeton, NJ
Kulkarni VG (1995) Modeling and Analysis of Stochastic Systems. Chapman and Hall
Kumamoto H, Tanaka T, Inoue K (1977) Efficient evaluation of system reliability reliability by Monte Carlo method. IEEE Trans. Reliability R-26:311-315
Kumamoto H, Kazuo T, Koichi I, Henley EJ (1980a) State transition Monte Carlo for evaluating large, repairable systems. IEEE Trans. Reliability R-29:376-380
Kumamoto H, Tanaka T, Inoue K, Henley EJ (1980b) Dagger sampling Monte Carlo for system unavailability evaluation. IEEE Trans. Reliability R-29:122125
Kumamoto H, Tanaka T, Inoue K (1987) A new Monte Carlo methods for evaluating system-failure probability. IEEE Trans. Reliability R-36:63-69
Kvam PH, Singh H, Whitaker LR (2002) Estimating distributions with increasing failure rate in an imperfect repair model. Lifetime data analysis 8/1: 53-67Lam Y (1988) A note on the optimal replacement problem. Adv. Appl. Prob. 20:479-482
Lam Y (1996) Analysis of a two-component series system with a geometric process model. Naval Research Logistics 43:491-502
Lam Y, Lam PKW (2001) An extended warranty policy with options open to consumers. European Journal of Operational Research 131:514-529
Lam CT, Yeh RH (1994a) Optimal maintenance-policies for deteriorating systems under various maintenance strategies. IEEE Trans. on Reliability 43/3:423-430
Lam CT, Yeh RH (1994b) Optimal replacement policies for multistate deteriorating systems. Naval Research Logistics 41:303-315
Lannon RG (1972) A Monte Carlo technique for approximating system reliability confidence limits using the Weibull distribution. AD-743633, Available from US NTIS
Laprie JC, Costes A, Landrault C (1981) Parametric analysis of 2-unit redundant computer systems with corrective and preventive maintenance. IEEE Trans. Reliability R-30/2:139-144
Laviron A, Carnino A, Manaranche JC, (1982) ESCAF - a new and cheap system for complex reliability analysis and computation. IEEE Trans. Reliability R-3:339-341
Law AM, Kelton WD (2000) Simulation modeling and analysis. McGraw-Hill
Levy LL, Moore AH (1967) A Monte Carlo Technique for obtaining system reliability confidence limits from component test data. IEEE Transaction on reliability R-16:69-72
Lewis EE, Boehm F, Kirsch C, Kelkhoff BP (1989) Monte Carlo simulation of complex system mission reliability. 1989 Winter Simulation Conference Proceedings - WSC '89, Washington, DC, USA, 1989 Dec 4-6
Li HJ, Shaked M (2003) Imperfect repair models with preventive maintenance. Journal of Applied Probability 40/4:1043-1059
Li W, Pham H (2005a) An inspection-maintenance model for systems with multiple competing processes. IEEE Trans. on Reliability 54/2:318-327
Li W, Pham H (2005b) Reliability modeling of multi-state degraded systems with multiple multi-competing failures and random shocks. IEEE Trans. on Reliability 54/2:297-303
Lie CH, Chun YH (1986) An algorithm for preventive maintenance policy. IEEE Trans. Reliability R-35/1:71-75
Lie CH, Hwang CL, Tillman FA (1977) Availability of maintained systems, A state-of-the-art survey. AIIE Transactions 9:247-259
Lim JH, Lu KL, Park DH (1998) Bayesian imperfect repair model. Communications in Statistics-Theory and Methods 27/ 4:965-984Lin CT, Duran BS, Lewis TO (1988) Estimating lower confidence limits on system reliability using a Monte Carlo technique on binomial data. Microelectronics and Reliability 28/3:487-493
Lin JY, Donaghey CE (1993) Monte Carlo simulation to determine minimal cut sets and system reliability. Proceedings of the 1993 Annual Reliability and Maintainability Symposium, Atlanta, GA, USA.
Liu XG, MakisV, Jardine AKS (1995) A replacement model with overhauls and repairs. Naval Research Logistics 42:1063-1079
Locks MO (1974a) Monte Carlo Bayesian system reliability and MTBF confidence assessment. AD-A057068, Available from US NTIS
Locks MO (1974b) Monte Carlo Bayesian system reliability - and MTBF confidence assessment II. AD-A025820, Available from US NTIS
Locks MO (1979) Evaluating of the KTI Monte Carlo method for system reliability calculations. IEEE Trans. Reliability R-28:369-372
Love CE, Guo R (1993) An application of a bathtub failure model to imperfectly repaired systems data. Quality and Reliability Engineering International 9:127134
Love CE, Guo R (1996) Utilizing Weibull failure rates in repair limit analysis for equipment replacement/preventive maintenance decisions. Journal of the Operational Research Society 47/11:1366-1376
Love CE, Rodger A, Blazenko G (1982) Repair limit policies for vehicle replacement. INFOR 20:226-236
Luby MG (1983) Monte-Carlo methods for estimating system reliability. Ph.D. Dissertation in computer science, University of California, Berkeley, USA
Lutton SC (1967) A Monte Carlo technique for approximating system reliability confidence limits from component failure data. MS thesis (GRE/MA/67-9), Air Force Institute of Technology, Wright-Patterson AFB, Ohio, USA
Lutz MA, Padmanabhan V (1998) Warranties, extended warranties, and product quality. International Journal of Industrial Organization 16:463-493
Lyu M (ed) (1996) Handbook of software reliability engineering. McGraw-Hill.
MacDonald MR (1982) A Monte Carlo technique suitable for obtaining complex space system reliability confidence limits from component test data with three unknown parameters. MS thesis, Air force Institute of Technology, WrightPatterson AFB, Ohio, USA
Madansky A (1965) Approximate confidence limits for the reliability of series and parallel systems. Technometrics 7:495-506
Mahajan V, Muller E, Wind Y (2000) New product diffusion models. Kluwer Academic
Makis V, Jardine AKS (1991) Optimal replacement of a system with imperfect repair. Microelectronics and Reliability 31/2-3:381-388Makis V, Jardine AKS (1992) Optimal replacement policy for a general model with imperfect repair. Journal of the Operational Research Society 43/2:111120

Makis V, Jardine AKS (1993) A note on optimal replacement policy under general repair. European Journal of Operational Research 69:75-82
Malik MAK (1979) Reliable preventive maintenance policy. AIIE Transactions $11 / 3: 221-228$

Mamer JW (1969) Determination of warranty reserves. Management Science $15 / 10: 542-549$

Mamer JW (1982) Costs analysis of pro rata and free-replacement warranties. Naval Research Logistics Quarterly 29:345-356
Mamer JW (1987) Discounted and per unit costs of product warranty. Management Science 33/7:916-930
Mann NR, Grubbs FE (1974) Approximately optimum confidence bounds for system reliability based on component test data. Technometrics 16:335-347
Marcellus R, Projboot B (1996) Design of Warranty Policies to Balance Consumer and Producer Risks and Benefit. In: Blischke WR, Murthy DNP (eds) Product Warranty Handbook. Marcel Dekker, pp 483-510
Markowitz H (1959) Portfolio Selection. Yale University Press, USA
Marseguerra M, Zio E (1993) Nonlinear Monte Carlo reliability analysis with biasing towards top event. Reliability Engineering \& System Safety 40/1:31-42
Marshall CW (1981) Design trade-offs in availability warranties. Proceedings of the Annual Reliability and Maintenance Symposium, pp 95-100
Martz HF, Waller R (1982) Bayesian Reliability Analysis. Wiley
Matteis AD, Pagnutti S (1995) Controlling correlations in parallel Monte Carlo. Parallel Computing 21/1:73-84
Mazumdar M (1975) Importance sampling in reliability estimation. Reliability and Fault Tree Analysis. SIAM, Philadelphia, pp153-163
McCall JJ (1963) Operating characteristics of opportunistic replacement and inspection policies. Management Science 10/1:85-97
McCall JJ (1965) Maintenance policies for stochastically failing equipment: A survey. Management Science 11/5:493-524
McGuire EP (1980) Industrial Product Warranties: Policies and Practices. The Conference Board Inc., New York
Mello JCO, Pereira MVF, Leite da Silva AM (1994) Evaluation of reliability worth in composite systems based on pseudo-sequential Monte Carlo simulation. IEEE Transactions on Power Systems 9/3:1318-1326
Melo ACG, Oliveira GC, Morozowski M, Pereira MVF (1991) Hybrid algorithm for Monte Carlo/enumeration based composite reliability evaluation. Third International Conference on Probabilistic Methods Applied to Electric Power Systems, London, 1991 Jul 3-5Menezes M (1992) An approach for determination of warranty length. International Journal of Research in Marketing 9:177-195
Menipaz E (1978) Optimization of stochastic maintenance policies. European Journal of Operational Research 2/2:97-106
Menzefricke U (1992) On the variance of total warranty claims. Comm. Statist. Theory and Methods 21/3:779-790
Mi J (1996) Warranty and burn-in. Naval Research Logistics 44:199-210
Mi J (1999) Comparisons of renewable warranties. Naval Research Logistics 46:91-106
Misra PN (1983) Software reliability analysis. IBM Systems Journal 22:262-270
Mitra A, Patankar JG (1993) An integrated multicriteria model for warranty cost estimation and production. IEEE Transactions on Engineering Management EM-40/3:300-311
Monga A, Zuo MJ, Toogood R (1997) Reliability based design of systems considering preventive maintenance and minimal repair. International Journal of Reliability, Quality and Safety Engineering 4/1:55-71
Moore AH (1965) Extension of Monte Carlo technique for obtaining system reliability confidence limits from component test data. Proc. National Aerospace Electronics Conf, 1965 May, pp 459-463
Moore AH, Harter HL, Snead RC (1980) A comparison of Monte Carlo technique for obtaining system reliability confidence limits from component test data. IEEE Trans Reliability R-29:327-332
Moore AH, Hobbs JR, Hasaballa MSB (1985) A Monte Carlo method for determining confidence bounds on reliability and availability of maintained systems. IEEE Trans. reliability R-34:497-498
Morimura H (1970) On some preventive maintenance policies for IFR. Journal of the Operations Research Society of Japan 12/3:94-124
Morimura H, Makabe H (1963a) A new policy for preventive maintenance. Journal of the Operations Research Society of Japan 5:110-124
Morimura H, Makabe H (1963b) On some preventive maintenance policies. Journal of the Operations Research Society of Japan 6:17-43
Morse PM (1958) Queues, Inventories, and Maintenance. Wiley, New York
Moskowitz H, Chun YH (1994) A Poisson regression model for two-attribute warranty policies. Naval Research Logistics 41:355-376
Murthy DNP (1991a) A note on minimal repair. IEEE Transactions on Reliability 40/2:245-246
Murthy DNP (1991b) A usage dependent model for warranty costing. European Journal of Operational Research 57/1:89-99
Murthy DNP (1992a) Product warranty management - I: A review of mathematical models. European Journal of Operational Research 62:127-148Murthy DNP (1992b) Product warranty management - II: A review of mathematical models. European Journal of Operational Research 62:261-281
Murthy DNP (1992c) Product warranty management - III: A review of mathematical models. European Journal of Operational Research 62:1-34
Murthy DNP, Asgharizadeh E (1999) Optimal decision making in a maintenance service operation. European Journal of Operational Research 116:259-273
Murthy DNP, Djamaludin I (2002) New product warranty: A literature review. International Journal of Production Economics 79:231-260
Murthy DNP, Hussain AZMO (1993) Warranty and optimal redundancy design. Engineering Optimization 23:301-314
Murthy DNP, Iskandar BP, Wilson RJ (1995) Two dimensional failure-free warranty policies: Two-dimensional point process models. Operations Research 43/2:356-366
Murthy DNP, Jack N (2003) Warranty and Maintenance. In: Pham H (ed) Handbook of Reliability Engineering. Springer, London
Murthy DNP, Nguyen DG (1981) Optimal age policy with imperfect preventive maintenance. IEEE Trans. Reliability R-30:80-81
Murthy DNP, Wilson RJ (1994) Parameter estimation in multi-component systems with failure interaction. Applied Stochastic Models and Data Analysis 10:47-60
Muth EJ (1977) An optimal decision rule for repair vs replacement. IEEE Transactions on Reliability R-26/3:179-181
Musa JD, Iannino A, Okumoto K (1987) Software Reliability: Measurement, Prediction, Application. McGraw-Hill, New York
Nakagawa T (1979a) Optimum policies when preventive maintenance is imperfect. IEEE Transactions on Reliability R-28/4:331-332
Nakagawa T (1979b) Imperfect preventive maintenance. IEEE Transactions on Reliability R-28/5:402
Nakagawa T (1980) A summary of imperfect maintenance policies with minimal repair. RAIRO, Recherche Operationnelle 14:249-255
Nakagawa T (1981) A summary of periodic replacement with minimal repair at failure. Journal of the Operations Research Society of Japan 24:213-228
Nakagawa T (1984a) Periodic inspection policy with preventive maintenance. Naval Research Logistics Quarterly 31:33-40
Nakagawa T (1984b) Optimal policy of continuous and discrete replacement with minimal repair at failure. Naval Research Logistics Quarterly 31/4, 543-550.
Nakagawa T (1985) Optimization problems in $k$-out-of- $n$ systems. IEEE Transactions on Reliability R-34:248-250
Nakagawa T (1986) Periodic and sequential preventive maintenance policies. Journal of Applied Probability 23/2:536-542Nakagawa T (1988) Sequential imperfect preventive maintenance policies. IEEE Trans. Relia. 37/3:295-298
Nakagawa T, Kowada M (1983) Analysis of a system with minimal repair and its application to replacement policy. European Journal of Operational Research 12:176-182
Nakagawa T, Murthy DNP (1993) Optimal replacement policies for a two-unit system with failure interactions. RAIRO: Recherche Operationnelle 27/4:427438
Nakagawa T, Yasui,K. (1987) Optimum policies for a system with imperfect maintenance. IEEE Trans. Reliability R-36/5:631-633.
NAPS document No. 03476-A; 3 pages in this Supplement. Order NAPS document No. 03476, 19 pages. ASIS-NAPS; Microfiche Publications, P.O.Box 3513, Grand Central Station, New York, NY 10017, USA.
Natvig B (1990) On information-based minimal repair and the reduction in remaining system lifetime due to the failure of a specific module. Journal of Applied Probability 27/2:365-375
Nelson BL (1987) Variance reduction for the simulation practitioners. Proc. 1987 Winter Simulation Conference, Atlanta, pp 43-51
Nelson SC, Haire MJ, Schryver JC (1992) Network-simulation modeling of interactions between maintenance and process systems. Proceedings of the 1992 Annual Reliability and Maintainability Symposium, Las Vegas, NV, USA,1992 Jan 21-23, pp 150-156
Neuts MF (1978) Renewal processes of phase type. Naval Logistics Quarterly 25:445-454
Neuts M (1981) Matrix-Geometric Solutions in Stochastic Process. John Hopkins University press, USA
Nguyen DG, Murthy DNG (1981a) Optimal repair limit replacement policies with imperfect repair. Journal of Operational Research Society 32:409-416
Nguyen DG, Murthy DNG (1981b) Optimal maintenance policy with imperfect preventive maintenance. IEEE Trans. Reliability R-30/5:496-497.
Nguyen DG, Murthy DNG (1981c) Optimal preventive maintenance policies for repairable systems. Operations Research 39:1181-1194
Nguyen DG, Murthy DNP (1984a) A general model for estimating warranty costs for repairable products. IIE Transactions 16:379-386
Nguyen DG, Murthy DNP (1984b) Cost analysis of warranty policies. Naval Research Logistics Quarterly 31:525-541
Nguyen DG, Murthy DNP (1988) Optimal reliability allocation for products sold under warranty. Engineering Optimization 13:35-45
Nguyen DG, Murthy DNP (1989) Optimal replacement-repair strategy for servicing products sold under warranty. European Journal of Operational Research 39/2:206-212Nicol DM, Palumbo DL (1995) Reliability analysis of complex models using SURE bounds. IEEE Transactions on Reliability 44/1:46-53
Nicola VF (1990) Fast simulation of dependability models with general failure, repair and maintenance processes. Proceedings of the 20th International Symposium on Fault-tolerant Computing, New Castle Upon Tyne, England, June 1990, pp 491-498
Ohi F (1989) Notes on imperfect repair, Keikaku sugaku to sono kanren bunya. In: Mathematical programming and its related fields. Proceedings of a symposium held at the Research Institute for Mathematical Sciences, Kyoto University, Kyoto, December 8-10, 1988, Kokyuroku No. 680, pp146-154
Ohnishi M, Kawai H, Mine H (1986) An optimal inspection and replacement policy for a deteriorating system. Journal of Applied Probability 23:973-988
Ohnishi M, Ibaraki T, Liu CG, Mine H (1987) Adaptive ( $t, T$ )-minimal repair and replacement policy when failure distribution includes unknown parameter. In: Reliability theory and applications (Shanghai, Xi'an, Beijing, 1987), World Sci. Publishing, Singapore, pp 304-313
Okuda S, Yonezawa M (1995) Structural reliability analysis based on importance sampling simulation defined in failure region. Zairyo/Journal of the Society of Materials Science of Japan 44/500:517-522
Okumoto K, Elsayed EA (1983) An optimum group maintenance policy. Naval Research Logistics Quarterly 30:667-674
Oliveira GC, Pereira MVF, Cunha SHF (1989) Technique for reducing computational effort in Monte-Carlo based composite reliability evaluation. IEEE Transactions on Power Systems 4/4:1309-1315
Osaki S, Nakagawa T (1976) Bibliography for reliability and availability of stochastic systems. IEEE Transactions on Reliability R-25:284-287
Osaki S, Yamada S, Hishitani J (1989) Availability theory for two-unit nonindependent series systems subject to shut-off rules. Reliability Engineering \& System Safety 25/1:33-42
Ozekici S (1988) Optimal periodic replacement of multicomponent reliability systems. Operations Research 36/4:542-552
Ozekici S (ed)(1996) Reliability and maintenance of complex systems. (NATO ASI series, vol. 154) Springer-Verlag, Berlin
Padmanabhan V, Rao RC (1993) Warranty policy and extended service contracts: theory and an application to automobiles. Marketing Science 12/397-117
Pan ZJ, Tai YC (1988) Variance importance of system components by Monte Carlo. IEEE Transactions on Reliability 37/4:421-423
Pandey M, Uddin B, Ferdous J (1992) Reliability estimation of an s-out-of-k system with non-identical component strength: The Weibull case. Reliability Engineering \& System Safety 36/2:109-116
Papadopoulos AS (1993) Hierarchical confidence bounds for the exponential failure model. Microelectronics and Reliability 33/5:719-727Patankar JG, Mitra A (1995) Effect of warranty execution on warranty reserve costs. Management Science 4:395-400

Patankar JG, Worm GH (1981) Prediction intervals for warranty reserves and cash flows. Management Science 27:237-241

Patton AD, Blackstone JH, Balu NJ (1988) Monte Carlo simulation approach to the reliability modeling of generating systems recognizing operating considerations. IEEE Transactions on Power Systems 3/3:1174-1180

Pereira MVF, Maceira MEP, Oliveira GC, Pinto LMVG (1992) Combining analytical models and Monte Carlo techniques in probabilistic power system analysis. IEEE Transactions on Power Systems 7/1:265-272
Pham H (1992) Reliability analysis of a high voltage system with dependent failures and imperfect coverage. Reliability Engineering and System Safety 37/1:25-28.

Pham H (1996) A software cost model with imperfect debugging, random life cycle and penalty cost. International Journal of Systems Science 5:455-463
Pham H (2000) Software Reliability. Springer-Verlag, Singapore
Pham H (2002) A Vtub-shaped hazard rate function with applications to system safety. International Journal of Reliability and Applications 3/1:1-16
Pham H (2003a) Commentary: Steady-state series-system availability. IEEE Trans on Reliability 52/3:146-147
Pham H (2003b) Software reliability and cost models: perspectives, comparison and practice. European Journal of Operational Research 149: 475-489
Pham H (ed)(2003c) Handbook of Reliability Engineering. Springer-Verlag, London

Pham H, Wang HZ (1996) Imperfect maintenance. European Journal of Operational Research 94:425-438
Pham H, Wang HZ (2000) Optimal ( $\tau, T$ ) opportunistic maintenance of a $k$-out-of$n$ :G system with imperfect PM and partial failure. Naval Research Logistics 47:223-239
Pham H, Wang HZ (2001) A quasi-renewal process for software reliability and testing costs. IEEE Transactions on Systems, Man and Cybernetic, Part A: Systems and Humans 31:623-631
Pham H, Xie M (2002) A generalized surveillance model with applications to systems safety. IEEE Trans. on Systems, Man and Cybernetics, Part C 32:485492

Pham H, Suprasad A, Misra RB (1996) Reliability and MTTF prediction of $k$-out-of- $n$ complex systems with components subjected to multiple stages of degradation. International Journal of Systems Science 27/10:995-1000
Pham H, Suprasad A, Misra RB (1997) Availability and mean life time prediction of multi-stage degraded system with partial repairs. Reliability Engineering and System Safety 56:169-173Phelps RI (1981) Replacement policies under minimal repair. Operational Research Society Journal 32/7:549-554

Pierskalla WP, Voelker JA (1976) A survey of maintenance models: the control and surveillance of deteriorating systems. Naval Research Logistics Quarterly 23:353-388

Pignal PI (1987) Analysis of a communication system with imperfect repair. Microelectronics and Reliability 27/1:165-169
Pijnenburg M, Ravichandran N, Regterschot G (1993) Stochastic analysis of a dependent parallel system. European Journal of Operational Research 68/1:90104

Polatoglu H, Sahin I (1998) Probability distribution of cost, revenue and profit over a warranty cycle. European Journal of Operational Research 108:170-183
Popova E, Wilson JG (1999) Group replacement policies for parallel systems whose components have phase distributed failure times. Annals of operations research 91:163-190
Prasad MS, Rattihalli SR (1987) Optimum repair limit replacement policy when the lifetime depends on the number of repairs. Opsearch, The Journal of the Operational Research Society of India 24/3:155-162
Presnell B, Hollander M, Sethuraman J (1994) Testing the minimal repair assumption in an imperfect repair model. Journal of the American Statistical Association 89/425:289-297
Pulat S, Leemis L (1989) Network reliability and availability analysis to minimize downtime costs for communication networks. Microelectronics and Reliability 29/1:37-48

Purohit SG (1994) Testing for the minimal repair model versus additional damage at failures. Communications in Statistics, Simulation and Computation 23/1:89107

Putz RB (1979) A Univariate Monte Carlo technique to approximate reliability confidence limits of systems with components characterized by the Weibull distribution. MS thesis (GOR/MA/79D-7), Air Force Institute of Technology. Available from US NTIS
Ramachandran V, Sankaranarayanan V (1990) Dynamic redundancy allocation using Monte-Carlo optimization. Microelectronics and Reliability 30/6:11311136

Rander R, Jorgenson DW (1963) Opportunistic replacement of a single part in the presence of several monitored parts. Management Science 10/1:70-83
Rander MC, Kumar A, Tuteja RK (1993) Analysis of a two unit cold standby system with imperfect assistant repairman, perfect master repairman and inspection after repair by assistant repairman. Journal of the Indian Association for Productivity, Quality and Reliability 18/1:41-53
Rangan A (1994) Time for failure free tests of systems subject to shocks and imperfect repair. Opsearch 31/3:228-236Rangan A, Grace RE (1989) Optimal replacement policies for a deteriorating system with imperfect maintenance. Advances in Applied Probability 21/4:949951

Rao BM (1995) Algorithms for the free replacement warranty with phase-type lifetime distributions. IIE Transactions 27:348-357
Rardin RL (1998) Optimization in Operations Research. Prentice Hall.
Resende LIP (1988) Computing network reliability using exact and Monte-Carlo method. Ph.D. Dissertation, Dept. of Industrial Engineering and Operations Research, University of California, Berkeley, USA
Rice RE, Moore AH (1983) A Monte Carlo technique for estimating lower confidence limits on system reliability using pass-fail data. IEEE Trans Reliability R-32:366-369
Righter R (1996) Optimal policies for scheduling repairs and allocating heterogeneous servers. Journal of Applied Probability 33/2:536-547
Ritchken PH (1985a) Optimal replacement policies for irreparable warranted item. IEEE Transactions on Reliability,35/5:621-624
Ritchken PH (1985b) Warranty policies for non-repairable items under risk aversion. IEEE Transactions on Reliability 34/2:147-150
Ritchken PH, Tapiero CS (1986) Warranty design under buyer and seller risk aversion. Naval Research Logistics Quarterly 33:657-671
Ritchken PH, Wilson JG (1990) ( $m, T$ ) group maintenance policies. Management Science 36/5:632-639
Roberts WT Jr, Mann L Jr (1993) Failure predictions in repairable multicomponent systems. International Journal of Production Economics 29/1:103110
Rodrigues DJ (1990) Some approximate inspection policies for a system with imperfect inspections. RAIRO, Recherche Operationnelle 24/2:191-199
Rolski T, Schmidli H, Schmidt V, Teugels J (1999) Stochastic Processes for Insurance and Finance. John Wiley and Sons, Chichester
Romeu JL (1989) Small sample Monte Carlo study for four system reliability bounds. Computers \& Industrial Engineering 16/1:117-126
Ross SM (1970) Applied Probability Models with Optimization Applications. Holden-Day
Ross SM (1983) Stochastic Processes. John Wiley and Sons
Rubinstein RY (1981) Simulation and the Monte Carlo Method. . John Wiley and Sons
Rustagi JS (1994) Optimization Techniques in Statistics. Academic Press
Sahin I (1993) Conformance quality and replacement costs under warranty. Production and Operational Management 2:242-261Sahin I, Polatoglu H (1995) Distributions of manufacturer's and user's replacement costs under warranty. Naval Research Logistics 42:1233-1250
Sahin I, Polatoglu H (1996) Maintenance strategies following the expiration of warranty. IEEE Transactions on Reliability 45/2:221-228
Sahin I, Polatoglu H (1998) Quality, Warranty and Preventive Maintenance. Kluwer Academic Publishers, Boston
Sandve K, Aven T (1999) Cost optimal replacement of monotone, repairable systems. European Journal of Operational Research 116:235-248
Savits TH (1988) Some multivariate distributions derived from a nonfatal shock model. Journal of Applied Probability 25/2:383-390
Scarf PA (1997) On the application of mathematical models in maintenance. European Journal of Operational Research 99/4:493-506
Schneeweiss WG (2005) Toward a Deeper Understanding of the Availability of Series-Systems Without Aging During Repairs. IEEE Transactions on Reliability 54/1:98-101
Sengupta B (1980) Maintenance policies under imperfect information. European Journal of Operational Research 5/3:198-204
Shaked M, Shanthikumar JG (1986) Multivariate imperfect repair. Operations Research 34:437-448
Shaked M, Shanthikumar JG (1988) Multivariate conditional hazard rates and the MIFRA and MIFR properties. Journal of Applied Probability 25/1:150-168
Sherif YS, Smith ML (1981) Optimal maintenance models for systems subject to failure - A review. Naval Research Logistics Quarterly 28/1:47-74
Sheu SH (1991) A general age replacement model with minimal repair and general random repair cost. Microelectronics and Reliability 31/5:1009-1017
Sheu SH (1999) Extended optimal replacement model for deteriorating systems. European Journal of Operational Research 112(3):503-516
Sheu SH (2005) Optimal policies with decreasing probability of imperfect maintenance. IEEE Transactions on Reliability 54/2:347-357
Sheu SH, Griffith WS (1992) Multivariate imperfect repair. Journal of Applied Probability 29/4:947-956
Sheu SH, Jhang J (1997) A generalized group maintenance policy. European Journal of Operational Research 96(2):232-247
Sheu SH, Kuo CM, Nakagawa T (1993) Extended optimal age replacement policy with minimal repair. RAIRO Recherche Operationnelle 27/3:337-351
Sheu SH, Griffith WS, Nakagawa T (1995) Extended optimal replacement model with random minimal repair costs. European Journal of Operational Research 85:636-649
Shiraki W (1989) Extension of iterative fast Monte-Carlo (IFM) procedure and its applications to time-variant structural reliability analysis. Proceedings ofICOSSAR '89, the 5th International Conference on Structural Safety and Reliability, Part II, San Francisco, CA, USA, 7-11 Aug 1989
Shreider IA (ed) (1960) The Monte Carlo Method: the Method of Statistical Trials. Pergamon Press, Oxford
Sim SH, Endrenyi J (1993) A failure-repair model with minimal and major maintenance. IEEE Transactions on Reliability 42/1:134-139
Singpurwalla ND, Wilson S (1993) The warranty problem: Its statistical and game theoretic aspects. SIAM Review 35/1:17-42
Smith MAJ, Dekker R (1997) Preventive maintenance in a 1 out of $n$ system: the uptime, downtime and costs. European Journal of Operational Research 99/3:565-583
Soboll IM (1974) The Monte Carlo Method. University of Chicago Press, Chicago
Srivastava MS, Wu Y (1993) Estimation \& testing in an imperfect-inspection model. IEEE Transactions on Reliability 42/2:280-286
Stadje W, Zuckerman D (1990) Optimal strategies for some repair replacement models. Adv. in Appl. Probab. 22/3, 641-656
Stadje W, Zuckerman D (1996) Generalized maintenance model for stochastically deteriorating equipment. European Journal of Operational Research 89/2:285301

Stadje W, Zuckerman D (1999) Optimal surveillance of a failure system. Annals of Operations Research 91:281-288
Su CT, Wu T, Lee T, Huwang C (1986) Capacity planning with flow and reliability evaluation using Monte Carlo simulation. IEEE Trans. Reliability R-35:519-522
Subramanian R, Natarajan R (1990) Two-unit redundant system with different types of failure and 'imperfect' repair'. Microelectronics and Reliability 30/4:697-699
Sumita U, Shanthikumar JG (1988) An age-dependent counting process generated from a renewal process. Advances in Applied Probability 20/4:739-755
Sundt B (2002) Recursive evaluation of aggregate claims distributions. Insurance: Mathematics and Economics 30:297-322
Sundt B, Jewell WS (1981) Further results on recursive evaluation of compound distributions. ASTIN Bulletin 12:27-39
Suresh PV, Chaudhuri D (1994) Preventive maintenance scheduling for a system with assured reliability using fuzzy set theory. International Journal of Reliability, Quality and Safety Engineering 1/4:497-513
Tahara A, Nishida T (1975) Optimal replacement policy for minimal repair model. Journal of Operations Research Society of Japan 18/3-4:113-124
Tanaka T, Kumamoto H, Inoue K (1989a) Evaluation of a dynamic reliability problem based on order of component failure. IEEE Transactions on Reliability 38/5:573-576Tanaka T, Kumamoto H, Inoue K (1989b) Monte Carlo evaluation of a dynamic reliability problem with an application to a case of partial cuts. Annual Reliability and Maintainability Symposium - 1989 Proceedings, Atlanta, GA, USA,1989 Jan 24-26 ( Available from IEEE Service Cent (cat n 89CH2580-9), Piscataway, NJ, USA), pp 108-113
Tango T (1978) Extended block replacement policy with used items. Journal of Applied Probability 15:560-572
Tatsuno K, Ohi F, Nishida T (1983) Opportunistic maintenance policy with minimal repair. Mathematica Japonica 28/3:327-335
Telcordia, GR-1339-CORE, Generic Reliability Requirements for Digital Cross Connect Systems, Issue Number 01, 1997. http://www.telcordia.com/
Thomas MU (1983a) A prediction model of manufacturer warranty reserves. Management Science 35/12:1515-1519
Thomas MU (1983b) Optimum warranty policies for nonreparable items. IEEE Transactions on Reliability 32/3:283-288
Thomas MU, Rao SS (1999) Warranty economic decision models: A summary and some suggested directions for future research. Operation Research 47/6:807820

Tian J, Lu P, Palma J (1995) Test-execution-based reliability measurement and modeling for large commercial software. IEEE Trans. Software Engineering 21/5: 405-414
Tilquin C, Cleroux R (1975a) Periodic replacement with minimal repair at failure and adjustment costs. Naval Res. Logist. Quart. 22/2:243-254
Tilquin C, Cleroux R (1975b) Periodic replacement with minimal repair at failure and general cost function. J. Statist. Comput. and Simulation 4/1:63-77
Uematsu K, Nishida T (1987a) One-unit system with a failure rate depending upon the degree of repair. Mathematica Japonica 32/1:139-147
Uematsu K, Nishida T (1987b) Branching nonhomogeneous Poisson process and its application to a replacement model. Microelectronics and Reliability 27/4:685-691
Valdez-Flores C, Feldman RM (1989) A survey of preventive maintenance models for stochastically deteriorating single-unit systems. Naval Research Logistics 36:419-446
Van Der Duyn Schouten F (1995) Maintenance policies for multicomponent systems. In: Ozekici S (ed) Reliability and maintenance of complex systems. (NATO ASI series, vol. 154) Springer-Verlag, Berlin, pp 117-136
van-Pul MCJ (1993) Statistical analysis of software reliability models. Stichting Mathematisch Centrum, Centrum voor Wiskunde en Informatica, Amsterdam
Venkatakrishnan KS, Venmathi S (1989) Optimal replacement time of an equipment via simulation for truncated failure distributions. Microelectronics and Reliability 29/1:49-52Vergin RC, Scriabin M (1977) Maintenance scheduling for multi-component equipment. AIIE Transactions 9:297-305
Wang C, Sheu S (2005) Optimal lot sizing for products sold under free-repair warranty. European Journal of Operational Research
Wang HZ (1997) Reliability and maintenance modeling for systems with imperfect maintenance and dependence. PhD Dissertation, Rutgers University, USA
Wang HZ (2002) A survey of maintenance policies of deteriorating systems. European Journal of Operational Research 139:469-489
Wang HZ (co-inventors: Kher S, Choudhury N, Rubin H, Franklin P, Remick P, Scarff P, Chien YC) (2004) Method and apparatus for warranty cost calculation. U.S. Patent (pending).
Wang HZ, Pham H (1996a) Optimal age-dependent preventive maintenance policies with imperfect maintenance. International Journal of Reliability, Quality and Safety Engineering 3/2:119-135
Wang HZ, Pham H (1996b) A quasi renewal process and its application in the imperfect maintenance. International Journal of Systems Science 27/10:10551062 and 28/12:1329
Wang HZ, Pham H (1996c) Optimal maintenance policies for several imperfect maintenance models. International Journal of Systems Science 27/6:543-549
Wang HZ, Pham H (1996d) Some new software reliability and cost models. Conference on Performability in Computing Systems, East Brunswick, New Jersey, 25-26 July 1996
Wang HZ, Pham H (1996e) Estimation Methods for Acceleration Factors, International Journal of Modelling \& Simulation16/3:166-172.
Wang HZ, Pham H (1997a) Availability and optimal maintenance of series system subject to imperfect repair. International J. of Plant Engineering and Management 2
Wang HZ, Pham H (1997b) Optimal opportunistic maintenance of a $k$-out-of-n:G System. International Journal of Reliability, Quality and Safety Engineering $4 / 4: 369-386$
Wang HZ, Pham H (1997c) Survey of reliability, availability and MTTF evaluations of complex networks using Monte Carlo techniques. Microelectronics and Reliability 37/2:187-209
Wang HZ, Pham H (1999) Some maintenance models and availability with imperfect maintenance in production systems. Annals of Operations Research 91:305-318.
Wang HZ, Pham H (2003) Optimal imperfect maintenance models. In: Pham (ed) Reliability Engineering Handbook. Springer-Verlag, London
Wang HZ, Pham H (2006) Availability and maintenance of series systems subject to imperfect repair and correlated failure and repair. European Journal of Operational ResearchWang HZ, Pham H, Izundu AE (2001) Optimal preparedness maintenance of multi-unit systems with imperfect maintenance and economic dependence. In: Pham H (ed) Recent Advances in Reliability and Quality Engineering. World Scientific, New Jersey, pp 75-92
Whitaker LP, Samaniego FJ (1989) Estimating the reliability of systems subject to imperfect repair. Journal of American statistical Association 84/405:301-309
Wijnmalen DJD, Hontelez JAM (1997) Coordinated condition-based repair strategies for components of a multi-component maintenance system with discounts. European Journal of Operational Research 98/1:52-63
Wildeman RE, Dekker R, Smit ACJM (1997) A dynamic policy for grouping maintenance activities. European Journal of Operational Research 99:530-551
Wilson JR (1983) Variance Reduction: the Current State, Mathematics and Computers in Simulation XXV. North Holland Publishing Co.
Wu S, Clements-Croome D (2005) Optimal Maintenance Policies Under Different Operational Schedules. IEEE Transactions on Reliability 54/2:338-346
Wu YF, Lewins JD (1991) System reliability perturbation studies by a Monte Carlo method. Annals of Nuclear Energy 18/3:141-146
Wu YF, Lewins JD (1992) Monte Carlo studies of engineering system reliability. Annals of Nuclear Energy 19/10-12:825-859
Xie M (1991) Software reliability modeling. World Scientific, UK.
Xue J, Yang K (1995) Dynamic reliability analysis of coherent multistate systems. IEEE Trans. Reliability 44/4:683-688
Yak YW, Dillon TS, Forward KE (1984) The effect of imperfect periodic maintenance on fault tolerant computer systems. 14th Int. Symp. Fault-Tolerant Computing, pp 67-70
Yang SC, Lin TW (2005) On the application of quasi renewal theory in optimization of imperfect maintenance policies. Proceedings of 2005 Annual Reliability and Maintainability Symposium, pp410-415
Yasui K, Nakagawa T, Osaki S (1988) A summary of optimal replacement policies for a parallel redundant system. Microelectronics and Reliability 28:635-641
Yeh RH, Ho WT (2000) Optimal preventive-maintenance warranty policy for repairable products. European Journal of Operational Research 134:59-69
Yeh RH, Ho WT, Tseng ST (2000) Optimal production run length for products sold with warranty. European Journal of Operational Research 120:575-582
Young HC, Chang SL (1992) Optimal replacement policy for a warranted system with imperfect preventive maintenance operations. Microelectronics and Reliability 32/6:839-843
Yue D, Cao JH (2001) Some results on successive failure times of a system with minimal instantaneous repairs. Operations Research Letters 29:193-197
Yun WY (1989) An age replacement policy with increasing minimal repair cost. Microelectronics and Reliability 29:153-157Yun WY (1997) Expected value and variance of warranty cost of repairable product with two types of warranty. The international Journal of Quality and Reliability Management 14/7:661-668
Yun WY, Bai DS (1987) Cost limit replacement policy under imperfect repair. Reliability Engineering 19/1:23-28
Yun WY, Bai DS (1988) Repair cost limit replacement policy under imperfect inspection. Reliability Engineering \& System Safety 23/1:59-64
Zelen M, Severo NC (1964) Probability functions. In: M. Abramowitz M, Stegun IA (eds) Handbook of Mathematical Functions. Applied Mathematics Series 55, U.S. Department of Commerce, pp 925-995
Zhao M (1994) Availability for repairable components and series system. IEEE Trans. on Reliability 43/2:329-334
Zheng X (1995) All opportunity-triggered replacement policy for multiple-unit system. IEEE Transactions on Reliability 44/4:648-652
Zio E (1995) Biasing the transition probabilities in direct Monte Carlo. Reliability Engineering \& System Safety 47/1:59-63
Zio E, Cammi A., Cioncolini A (2004) Dagger-sampling variance reduction in Monte Carlo reliability analysis. Monte Carlo Methods and Applications 10/34: 641-52
Zuo MJ, Murthy DNP (2000) Replacement-repair policy for multi-state deteriorating products under warranty. European Journal of Operational Research 123:519-530
Zuo MJ, Jiang R, Yam RCM (1999) Approaches for reliability modeling of continuous-state devices. IEEE Trans. Reliability 48/1:9-18# Index 

as bad as old, $3,14,16,29,3851$, $63,68,237$
as good as new, $2,3,5,13,14,16$, $27,29,63,68,114,135,174,188$, 189, 209, 210, 237, 287
asymptotic fractional down time, 91, 98,99
asymptotic number of failures, 96, 99
availability, $2,5,7,8,11,12,15,17$, $21,27,29,34,39,51,66,68,69$, $70,71,72,86,87,91,92,96,98$, $100,101,104,110,112,114,115$, $119,120,123,124,130,132,135$, 139, 140, 145, 149, 151, 158, 161, 166, 171, 186, 275, 276, 286, 287, 290, 291
asymptotic (or limiting) average (system), 51, 65, 69, 71, 74, 86, $94,98,119,130,137,139,140$, $145,161,169$
steady-state, 29, 91, 94, 96
Bayes method, 12, 259, 275, 276, 283, 290, 293
$c d f, 52,53,67,125,140,141,155$, 173, 205, 206, 210, 216, 217, 238, 241, 250, 266, 267
centered moments, 210, 218, 226, 227, 234, 250, 251
$\mathrm{CM}, 2,3,4,5,8,10,11,21,23,24$, $32,33,40,48,81,92,151,152$, $154,155,159,160,162,169,170$, 173, 186, 188, 190, 201, 209
CMW, 205, 255, 256
coherent system, 151, 286, 287
competing failure processes, 11, 171, $172,174,185$
compound Poisson process, 181, 182, 183, 184, 185, 187
condition-based maintenance, 172, 185, 187
confidence intervals, 276, 278, 279, 280, 285
correlated failures, 5, 6, 9, 29, 47
correlated failures and repairs, 6,10 , 29, 94
covariance, 213, 219, 220, 224, 239, 304
critical software fault, 266
cumulative damage shock model, 19
dagger-sampling Monte Carlo, 287, 289
debugging costs, 259, 274
decision variables, $12,33,34,35,36$, $37,38,40,42,43,44,46,47,48$, $65,66,69,72,74,77,79,81,82$, $88,114,139,150,151,152,154$, 166, 167, 170, 171, 186, 187, 196, 197, 199, 201, 254degradation, 12, 171, 172, 173, 174, 177, 187, 285, 302,
degradation path, 175, 186, 188, 201
degradation path function, 187,
degradation process, 11, 12, 171, 172, 173, 174, 175, 176, 177, 179, 180, 185, 186, 190, 199, 302
dependence, 4,29
economic, $2,5,6,7,8,9,10,11$, $29,45,45,111,113,132,133$, 135, 136, 150, 151, 152, 153
failure, $5,6,7,8,9,29,45,47$, 111
structural, 45
DFR, 20, 52, 53, 90, 261
DFRA, 20, 52, 53, 89
DWC, 202, 203, 229, 231, 251
error-free time, 12, 259, 260, 261, 262, 267, 268, 269, 270, 272, 273, 274
EWC, 7, 205, 225, 254
expected rate of expenditure, 120, 122, 123, 131, 147, 148, 149
expected rate of failure, 120, 123, 131, 149
expected rate of PM, 119, 120, 121, 130, 131, 148
expected rate of replacement, 146
expected warranty cost (per cycle), 205, 208, 215, 223, 225, 226, 237, 240, 242, 253
failure limit policy, 25, 26, 31, 32, $38,39,40,44$
failure rate, $2,3,11,14,15,16,17$, $18,21,24,25,32,34,38,39,40$, $43,52,53,61,111,112,120,125$, 136, 137, 140, 146, 150, 152, 153, 154, 155, 168, 171, 172, 207, 226, 230, 245, 250, 251, 260, 262, 284, 285, 288
fault, 4, 12, 259, 260. 262. 262. 263, 266, 267, 270, 272, 273
first moment, 206, 210, 217, 227, 230, 234, 240, 244, 255

FRPW, 9, 12, 204, 205, 235, 255, 256, 257
FRW, 9, 12, 204, 205, 227, 227, 233, 234, 235, 236, 255
geometric distribution, 213, 214, 215, 216, 255, 297
global optimal maintenance policies, 7, 107
hypothesis testing, 51, 57, 59
IFR, 11, 19, 20, 32, 52, 53, 65, 72, $90,133,150,153,168$
IFRA, 20, 52, 89
i.i.d., 18, 45, 52, 53, 64, 77, 153, 156, 159, 162, 173, 180, 187, 210, 213, 227, 234, 238, 248, 252, 261
imperfect maintenance modeling method, 14
improvement factor method, 16, 18,21
multiple $(p, q)$ rule, 22, 28
others, 21, 22
$(p, q)$ rule, 14, 15, 21, 22, 29, 64, $81,114,132,150$,
$(p(t), q(t))$ rule, 15, 16, 22, 24, 124,150
quasi-renewal process, 20,22
shock model, 19, 20, 26
virtual age method, 18,28
inspection, 1, 2, 4, 12, 28, 31, 46, 47, $51,74,135,136,139,150,152$, 171, 172, 173, 174, 186, 187, 188, 196, 201
inspection-maintenance, 11, 171, 172, 185, 186, 188, 196, 201
$k$-out-of- $n$ systems, 8, 151, 152, 169
Laplace transform, 56, 73
LCL, 280, 283, 294
long-run expected maintenance cost per unit time or long-run expected maintenance cost rate, $62,63,65$, $70,73,74,77,81,82,88,102$, $103,114,118,119,120,123,128$,130, 139, 145, 155, 156, 158, 161, 163,166
maintenance, 2, 17, 19, 21, 37, 45, 114,150
corrective, 2, 15
imperfect, $1,2,3,4,5,6,7,8$, $10,11,13,14,15,16,18,20$, $21,22,23,32,35,51,55,61$, $62,76,81,120,132,135,138$, 150, 225, 294
joint, 5, 21, 29, 120, 121, 139, 153
opportunistic, $5,11,31,45,47$, $48,132,135,138,139,146$, $147,148,150,151,152,169$
perfect, $2,3,10,14,16,18,19$, $21,23,27,28,32,34,38,42$, $47,48,49,62,63,65,68,70$, $71,72,94,97,112,114,137$, 139, 161, 204, 209, 210, 218, 225, 255, 287
preventive, 2, 32, 65, 77, 131, 156, 159, 161, 186, 207
worse, 3, 18
worst, 3, 13
maintenance cost, $1,5,6,65,120$, 138, 146, 225
maintenance cost rate, $62,63,65,70$, $73,74,77,81,82,88,102,103$, $114,118,119,120,123,128,130$, 139, 140, 145, 155, 156, 158, 161, 163, 166, 190, 196, 201,
maintenance (repair) degrees, 2, 9, 29,
maintenance optimization, 7, 9
maintenance policies, $2,5,9,11,12$, $17,27,31-37,45-48$
group, 46
inspection, 188, 196
opportunistic, $5,11,45,47,48$, $113,132,138,139,152$
optimal (optimum), 2, 5, 9, 12, 17, $22,34,35,66,74,76,80,87$, $88,107,114,131,138,167$
preparedness, 11, 58, 135-140
major software faults, 266
maximum likelihood, 12, 16, 58, 264, 268, 271, 274, 285
estimates (MLE), 12, 58, 259, 271, 285
method, 58, 264, 268, 274, 276
mean error-free time, 12, 259, 274
minor software faults, 266
monetary utility function, 254
Monte Carlo simulation, 12, 224, 275, 276, 277, 282, 283, 284, 290
MTBF, 2, 11, 12, 275, 276, 277, 286, 288, 290
MTBSF, 7, 8, 96, 98, 104
MTBSR, 8, 96, 98, 104
MTTF, 21, 275, 276, 293, 296, 298
multiple competing failure processes, 11, 171, 172, 174, 185
multi-unit systems, 4, 27, 31, 32, 35, $45,48,111,121,133,135,150$

NBU, 20, 52, 54, 89
NBUE, 52, 54, 89
Nelder-Mead downhill simplex method, 186, 188, 196, 197, 201
non-homogeneous Poisson process (NHPP), 9, 28, 128, 157, 204, 205, 227, 250, 251, 303, 306
nonlinear (integer) programming, 66, $76,82,89,109,120,124,130$, 132, 146, 167, 270
Normal distribution, 58, 66, 168, 180, 234, 241, 242, 245, 252, 264, 278, 280, 299
NWU, 52, 53, 89
NWUE, 52, 54, 89
one-unit system, $4,11,14,16,22$, $32,44,51,111,165$
operating characteristics, 114,120 , 130, 139, 146
optimal maintenance policies, $2,5,7$, $9,12,17,23,34,35,66,74,76$, $80,87,88,107,114,131,138$, 167
optimality criterion, 24-28, 39, 41optimization, $7,9,12,66,67,87,91$, $109,114,123,132,149,166,188$, 196, 199, 246, 252, 259, 272
ordinary renewal processes, 11,15 , $29,51,55,56,240,261,304$
parallel system, $8,11,151,166,298$, 215, 226
parallel-series, 6, 204, 205, 218, 226, 236
pdf, 20, 52, 66, 83, 94, 140, 142, 155, 167, 173, 179, 180, 193, 205207, 227, 230, 250, 267, 296
planning horizon, 9, 10, 17, 23-28, $38,39,55,153$
PM, 2, 3, 14, 17, 21, 23, 24, 25, 37, $44,48,52,63,112,125,129,136$, 155, 159, 169, 192, 201, 207, 224, 256
age-dependent, $8,23,32,35,43$, 76
failure limit, $9,25,32,38,44,111$
periodic, $8,14,19,21,24,25,32$, $35,38,43,62,68,297$
sequential, $9,16,19,21,26,40$, 44,111
pmf, 205, 210, 215, 224, 251
policy
age replacement, $9,28,32,44$, 163
block replacement, 9, 31, 35, 44, 136
failure limit, $9,25,32,38,44,111$
group maintenance, 31, 46
mixed age, $31,34,35$
$(m, T)$ group replacement, 46
no failure replacement, 35
periodic replacement with minimal repairs at failures, 35
random age replacement, 31
reference time, 31,43
repair cost limit, 26, 40, 205, 236
repair number counting, $33,42,43$
repair replacement policy, 28, 34, 44
repair time limit, 26, 40, 42, 256
sequential PM, 16, 19, 21, 26, 40, 111
POS, 92, 94, 99, 109
preparedness maintenance, 11,48 , 133, 150
probability, 14, 15, 17, 21, 24-27, 34, $38,52,112,117,147,183,201$, 233, 246, 266, 280
PRW, 9, 12, 204, 231, 256
PV, 205, 225, 234
quasi-renewal density, 56, 64
quasi-renewal function, 21, 52, 55, $62,63,65,67,262$
quasi-renewal process, $11,20,22$, $51,58,102,110,171,186,237$, 245, 259, 260-262, 274, 303
decreasing, 11, 20, 53, 62, 64, 87, 91, 97
increasing, 12, 20, 53, 64, 76, 89, $92,97,110,255,259$
truncated, 12, 51, 59, 204, 237
random shocks, $11,171,173,185$
random variable, $53,54,115,173$, 208, 224, 229, 258, 268, 283, 289, 303
RCLW, 205, 256, 257
reliability, $1,8,44,48,52,89,92$, 169, 172, 177, 221, 272
reliability architecture (see reliability structure), 10, 48, 204, 275, 283
reliability block diagram (RBD), 277, 280, 284, 286, 292
reliability structure (see reliability architecture), 2, 12, 169, 204, 208, 275,-278, 280, 290
renewal cycle, $52,63,71,77,81$, $112,124,137,140,156,162,174$, 192
renewal process, $11,15,29,51,55$, 56, 240, 261, 304
renewal reward theory, $68,75,77$, $82,86,115,124,140,156,305$
repair, $3,18,99,204$imperfect, $3,15,20,62,63,64$, $68,70,76,81,84,91,94,100$, $110,114,128,204,226,236$, 245, 256, 288, 292,
minimal, $3,15,18,19$
perfect, $2,15,20,99,100$
worse, 3
worst, 3
repair cost limit policy, 26, 40, 205, 236
repair time limit policy, 26, 40, 42, 256
repairable systems, $4,7,29,188$, 286, 291
replacement, $1,9,31,51,118$
RFSW, 9,12, 204, 208
RLRFW, 9, 12, 204, 236
RNLW, 205, 256
RRLRFW, 205, 254
sample size, 12, 57, 275, 285, 290, 297
second moment, 60, 206, 230, 240, 244, 255
series systems, $8,11,91,204,227$, 236
series-parallel, 204, 226, 236, 285, 290
severity levels, 265
shut-off rules, $9,92,95,113,133$, 138,150
software faults, 266
Critical, 266
Major, 266
Minor, 266
software reliability, 2, 8, 12, 51, 259, 274
state-dependent transition rate, 171
system reliability, $1,2,8,12,30,92$, 123, 131, 169, 184, 204, 224, 278, 291
system structure, $6,8,9,12,204$, 208, 226, 236, 280, 287
(software) testing cost, $8,12,51$, 260, 274
tie-sets, 277,-280, 284, 288
variance, $8,53,58,67,180,216$, 221, 259, 281, 289, 297
variance reduction, 2, 12, 277, 285, 289
warranty, 1, 12, 59, 61, 203
warranty cost, $1,6,12,59,203$
warranty cost variance, 216
warranty cycle, 204, 249
warranty service cost, 201
warranty term, 203
Weibull distribution, 43, 79, 167, 222, 231, 245, 276, 278, 285, 293, 300, 302