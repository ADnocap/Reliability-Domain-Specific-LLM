# D.N. Prabhakar Murthy Marvin Rausand $\cdot$ Trond Østerås 

## Product Reliability

## Specification and Performance# Springer Series in Reliability Engineering# Series Editor 

Professor Hoang Pham
Department of Industrial and Systems Engineering
Rutgers, The State University of New Jersey
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
B.S. Dhillon

Shock and Damage Models in Reliability Theory
Toshio Nakagawa
Risk Management
Terje Aven and Jan Erik Vinnem
Satisfying Safety Goals by Probabilistic Risk Assessment
Hiromitsu Kumamoto
Offshore Risk Assessment (2nd Edition)
Jan Erik Vinnem
The Maintenance Management Framework
Adolfo Crespo Márquez
Human Reliability and Error in Transportation Systems
B.S. Dhillon

Complex System Maintenance Handbook
D.N.P. Murthy and K.A.H. Kobbacy

Recent Advances in Reliability and Quality in Design
Hoang PhamD.N. Prabhakar Murthy $\cdot$ Marvin Rausand

Trond Østerås

# Product Reliability 

Specification and Performance

SpringerD.N. Prabhakar Murthy, PhD<br>Division of Mechanical Engineering<br>The University of Queensland<br>Brisbane<br>QLD 4072<br>Australia

Marvin Rausand, PhD
Trond Østerås, PhD
Department of Production and Quality Engineering
Norwegian University of Science and Technology
S. P. Andersens veg 5

7491 Trondheim
Norway

ISBN 978-1-84800-270-8
e-ISBN 978-1-84800-271-5
DOI 10.1007/978-1-84800-271-5
Springer Series in Reliability Engineering ISSN 1614-7839
British Library Cataloguing in Publication Data
Murthy, D. N. P.
Product reliability : specification and performance. -
(Springer series in reliability engineering)

1. Reliability (Eningeering) 2. Manufactures
I. Title II. Rausand, Marvin III. Osteras, Trond
$658.5^{\prime} 6$
ISBN-13: 9781848002708
Library of Congress Control Number: 2008925347
(C) 2008 Springer-Verlag London Limited

Apart from any fair dealing for the purposes of research or private study, or criticism or review, as permitted under the Copyright, Designs and Patents Act 1988, this publication may only be reproduced, stored or transmitted, in any form or by any means, with the prior permission in writing of the publishers, or in the case of reprographic reproduction in accordance with the terms of licences issued by the Copyright Licensing Agency. Enquiries concerning reproduction outside those terms should be sent to the publishers.

The use of registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant laws and regulations and therefore free for general use.

The publisher makes no representation, express or implied, with regard to the accuracy of the information contained in this book and cannot accept any legal responsibility or liability for any errors or omissions that may be made.

Cover design: deblik, Berlin, Germany
Printed on acid-free paper
987654321
springer.com# Preface 

In modern industrial societies, new products appear on the market at an everincreasing pace. This is due to (i) rapid advances in technology and (ii) constantly increasing demands from customers, with each as a driver to the other. As a result, products are getting more complex and the performance capabilities are increasing with each new product generation.

Product reliability is an indicator that the product will perform satisfactorily over its intended useful life when operated normally. It is of great interest to both customers and manufacturers. From a customer perspective, poor product reliability increases the frequency of failures and implies higher maintenance costs over the life of the product. From a manufacturer perspective, poor reliability affects sales through customer dissatisfaction, results in higher warranty costs, and affects the reputation and the bottom line. Often, the inability of a product to perform satisfactorily can have safety implications. In this case, product reliability needs to be viewed from a societal perspective.

Product reliability is determined by the technical decisions made during the design, development, and production phases of the product life cycle, and has commercial implications for the marketing and post-sale support phases of the product life cycle. Product reliability decisions need to be made from an overall business perspective using a product life cycle framework and an approach which links the various technical and commercial issues.

A life cycle framework for decision making regarding product reliability is proposed in this book. The framework comprises three stages (pre-development, development, and post-development), three levels (business, product, and component), and eight phases (phases 1-8) as indicated in Figure 0.1. A new approach to product reliability performance and specification is proposed based on the life cycle framework. The approach involves defining the desired performance and deriving the specifications that will ensure this performance in a sequential manner. Mathematical models are used to obtain predicted performance and to compare the predicted performance with the desired performance. Using the specifications at the component level of phase 3, the predicted performance is assessed in phases $4-8$ for proper decision making regarding product reliability, over the product life cycle.

Figure 0.1. Framework for decision making regarding product reliability

In stage I of the life cycle, two important questions need to be answered:

1. How to decide on desired reliability performance at the product level?
2. How to specify the reliabilities at the component level that will ensure this?

The answer to the first question depends on the decisions in phases 1 and 2 and the answer to the second question depends on the decisions made in phases 2 and 3 of the proposed framework.

During stage I, the product is a concept that mainly exists as drawings and associated calculations and assessments. Here, the product performance must be predicted based on mathematical models, generic data, and expert judgement. In stage II, physical models and prototypes are built, tested, and evaluated; and in stage III, the product is manufactured and used by the customers. In stages II and III, the actual performance of the product can be determined based on observed data and can be compared with the desired performance.

The book deals with the framework and the approach needed for effective decision making regarding product reliability. It deals with both standard and custombuilt products, highlighting the commonality and the difference between the two.

The book is aimed at both practitioners and researchers involved with reliability. The objectives are to provide (i) senior managers in industry a better view to make proper decisions relating to product reliability, (ii) design engineers an approach to deal effectively with reliability design, and (iii) reliability researchers a starting point to carry out new research into various aspects of product reliability.

Finally, the book can also be used as a reference book for postgraduate programmes in engineering design, reliability, and management.

The book has 11 chapters of which the first four give an overview and an introduction to the many aspects of product reliability. Although we have tried to make the book self-contained, it is aimed primarily at readers with basic knowledge and/or experience in product reliability. For reference, a brief introduction to reliability the-ory is given in Chapter 4. The eight phases of the new framework are described and discussed in Chapters 5 to 9 as indicated in Figure 0.1. Product safety aspects are discussed in Chapter 10 and reliability management systems are discussed in Chapter 11. Two case studies are used throughout the book to illustrate main aspects of product reliability. The first case is a cellular phone, which illustrates aspects related to standard products, or consumer durables. This case study is discussed in several small examples and as a last section in Chapters 4 to 10, where we highlight main issues in the chapter, and give references where interested readers can find more information. The second case is a safety instrumented system, for example a process shutdown system, which illustrates reliability aspects of custom-built, or specialized, products. This case study is included as several small examples illustrating central reliability issues.

The descriptions in the book are rather brief, but a large number of references are provided where interested readers can find more details and extend their knowledge. Symbols used in the book are listed and explained in Appendix A. Acronyms are listed in Appendix B and a glossary is supplied in Appendix C.

Brisbane and
Pradhur
Trondheim,
March 2008

Marvin Rausand
Trond Østerås

Additional information related to the book my be found on http://www.ntnu.no/ross/books/prodrel# Acknowledgements 

Many of the definitions in this book are according to international standards - especially IEC and ISO standards. A list of safety requirements for safety instrumented systems is copied from IEC 61511, and Figures 10.2 and 10.3 are reproduced from ISO 14121-1. IEC and ISO have kindly given us permission to include this material in the book.

The authors thank the International Electrotechnical Commission (IEC) for permission to reproduce information from its International Standard IEC 61511-1 ed.1.0 (2003). All such extracts are copyright of IEC, Geneva, Switzerland. All rights reserved. Further information on the IEC is available from www.iec.ch. IEC has no responsibility for the placement and context in which the extracts and contents are reproduced by the author, nor is IEC in any way responsible for the other content or accuracy therein.

NS-EN ISO 14121-1:2007 Safety of machinery - Risk assessment - Part 1: Principles, Figure 1 and Figure 2, as well as definitions from NS-ISO standards in Annex C are reproduced by the authors of Product Reliability: Specification and Performance with the permission of Pronorm AS 02/2008. (C) All rights reserved.

We are grateful to the Norwegian Research Council for financial support through the research programme P 2005. We would also thank senior editor Anthony Doyle and the staff of Springer for their patience and assistance in completing this text.

Finally, we thank our families for putting up with us during the preparation of this book.
P.M., M.R., and T.Ø.# Contents 

1 An Overview ..... 1
1.1 Introduction ..... 1
1.2 Product Properties and Perspectives ..... 3
1.2.1 Product Properties: Attributes and Characteristics ..... 4
1.2.2 Consumer Perspective ..... 4
1.2.3 Manufacturer's Perspective ..... 5
1.3 Product Reliability ..... 5
1.3.1 Definition of Reliability ..... 5
1.3.2 Consequences of Failures ..... 6
1.4 Product Life Cycle ..... 7
1.5 Product Performance and Specification ..... 7
1.5.1 Product Performance ..... 7
1.5.2 Product Specification ..... 8
1.5.3 Performance-Specification Relationships ..... 8
1.6 Reliability Performance and Specification ..... 8
1.6.1 Methodology for Reliability Performance and Specification ..... 9
1.6.2 Systems Approach ..... 9
1.7 Objectives of the Book ..... 10
1.7.1 Case 1 [Cellular Phone] ..... 10
1.7.2 Case 2 [Safety Instrumented System] ..... 11
1.8 Outline of the Book ..... 12
2 New Product Development ..... 15
2.1 Introduction ..... 15
2.2 Products ..... 15
2.2.1 Product Classification ..... 16
2.2.2 "Newness" of a New Product ..... 18
2.2.3 Product Decomposition ..... 19
2.3 Product Life and Product Life Cycles ..... 21
2.3.1 Product Life ..... 21
2.3.2 Product Life Cycle ..... 212.4 New Product Development ..... 22
2.4.1 New Product Development in the Overall Business Context ..... 22
2.4.2 A Brief Review of New Product Development Models ..... 23
2.5 Product Life Cycle Phases: Basic Concepts and Activities ..... 24
2.5.1 Front-end ..... 24
2.5.2 Design ..... 29
2.5.3 Development ..... 31
2.5.4 Production ..... 32
2.5.5 Post-production ..... 33
2.6 A New Model for Product Performance and Specification ..... 34
3 Product Performance and Specification ..... 37
3.1 Introduction ..... 37
3.2 Requirements, Preferences and Constraints ..... 37
3.2.1 Requirements ..... 37
3.2.2 Preferences ..... 38
3.2.3 Constraints ..... 39
3.3 Product Performance ..... 39
3.3.1 Concept and Notions ..... 39
3.3.2 Types of Performance ..... 40
3.4 Product Specification ..... 42
3.5 Performance and Specification Relationships ..... 43
3.6 Performance and Specification in Stage I ..... 44
3.6.1 Phase 1 ..... 44
3.6.2 Phase 2 ..... 46
3.6.3 Phase 3 ..... 46
3.6.4 Some Comments ..... 48
3.7 Performance in Stage II ..... 49
3.7.1 Phase 4 ..... 49
3.7.2 Phase 5 ..... 50
3.8 Performance in Stage III ..... 50
3.8.1 Phase 6 ..... 51
3.8.2 Phase 7 ..... 51
3.8.3 Phase 8 ..... 52
3.9 Overall Process ..... 52
3.10 Reliability Performance and Specification ..... 53
4 An Introduction to Reliability Theory ..... 55
4.1 Introduction ..... 55
4.2 Basic Concepts ..... 56
4.2.1 Product Functions ..... 56
4.2.2 Failure and Related Concepts ..... 56
4.2.3 Different Notions of Product Reliability ..... 60
4.3 Reliability Science ..... 61
4.4 Reliability Modelling - I ..... 614.4.1 Reliability Modelling of Single Items ..... 61
4.4.2 Physical Modelling ..... 66
4.4.3 System Modelling ..... 67
4.4.4 Modelling Environmental Effects ..... 70
4.5 Reliability Modelling - II ..... 73
4.5.1 Modelling CM Actions ..... 73
4.5.2 Modelling PM Actions ..... 74
4.5.3 Other Approaches ..... 77
4.6 Reliability Analysis ..... 77
4.6.1 Qualitative Analysis ..... 77
4.6.2 Quantitative Analysis ..... 79
4.6.3 Simulation ..... 82
4.7 Reliability Engineering ..... 82
4.7.1 Reliability Allocation ..... 82
4.7.2 Reliability Improvement ..... 83
4.7.3 Root Cause Analysis ..... 85
4.8 Reliability Prediction and Assessment ..... 85
4.8.1 Reliability Prediction ..... 85
4.8.2 Reliability Assessment ..... 86
4.9 Reliability Management ..... 87
4.9.1 Costs ..... 87
4.9.2 Data for Effective Management ..... 87
4.10 Case Study: Cellular Phone ..... 88
5 Performance and Specification in the Front-end Phase ..... 91
5.1 Introduction ..... 91
5.2 Front-end Process for Standard Products ..... 91
5.3 Data Collection and Analysis [Sub-phase 1] ..... 93
5.3.1 Data Collection ..... 93
5.3.2 Data Analysis ..... 94
5.3.3 Outcome of Sub-phase 1 ..... 95
5.4 Idea Generation and Screening [Sub-phase 2] ..... 96
5.4.1 Customer Understanding ..... 96
5.4.2 Idea Generation ..... 97
5.4.3 Screening of Ideas ..... 98
5.4.4 Outcome of Sub-phase 2 ..... 99
5.5 Product Concept Formulation and Evaluation [Sub-phase 3] ..... 99
5.5.1 Defining DP-I ..... 99
5.5.2 Deriving SP-I ..... 103
5.5.3 Evaluating PP-I ..... 104
5.5.4 Models ..... 105
5.5.5 Outcome of Sub-phase 3 ..... 110
5.6 Specialized (Custom-built) Products ..... 110
5.6.1 Performance Requirement ..... 110
5.6.2 Contract ..... 1125.6.3 Reliability Improvement Warranty ..... 113
5.6.4 Idea Generation and Screening ..... 114
5.6.5 DP-I ..... 114
5.6.6 SP-I ..... 115
5.6.7 PP-I ..... 117
5.6.8 Outcome of Phase 1 ..... 117
5.7 Implications for Product Reliability ..... 118
5.8 Case Study: Cellular Phone ..... 118
6 Performance and Specification during Design ..... 121
6.1 Introduction ..... 121
6.2 Phase 2 for Standard Products ..... 121
6.2.1 Defining DP-II ..... 122
6.2.2 Deriving SP-II ..... 123
6.2.3 Evaluating PP-II ..... 126
6.3 Phase 2 for Custom-built Products ..... 127
6.4 Models ..... 128
6.5 An Illustrative Case ..... 129
6.5.1 Option 1 [No Product Variety: Single Design] ..... 129
6.5.2 Option 2 [Product Variety: Two Designs] ..... 132
6.6 Phase 3 for Standard and Custom-built Products ..... 133
6.6.1 Sub-phase 1 ..... 134
6.6.2 Sub-phase $j[j=2,3, \ldots, J-1]$ ..... 136
6.7 Achieving the Allocated Reliability at Component Level ..... 137
6.7.1 Redundancy ..... 139
6.7.2 Preventive Maintenance ..... 140
6.7.3 Reliability Growth through Development ..... 140
6.7.4 Modelling for Optimal Decisions ..... 141
6.8 Outcome of Phase 3 ..... 143
6.9 Case Study: Cellular Phone ..... 143
7 Performance During Development ..... 147
7.1 Introduction ..... 147
7.2 Phase 4 for Standard Products ..... 148
7.3 Reliability Development Testing ..... 149
7.3.1 Reliability Growth Testing ..... 149
7.3.2 Environmental Stress and Design Limit Testing ..... 150
7.3.3 Accelerated Testing ..... 150
7.4 Design of Experiments for Testing ..... 154
7.4.1 Principles of Test Design ..... 154
7.4.2 Relevant Issues ..... 155
7.4.3 Optimal Design of Experiments for Testing ..... 155
7.5 Analysis of Test Data ..... 156
7.5.1 Test Data ..... 156
7.5.2 Qualitative (Engineering) Analysis ..... 1567.5.3 Graphical Analysis ..... 157
7.5.4 Statistical Analysis (Single Stress Level) ..... 158
7.5.5 Statistical Analysis (Multiple Stress Levels) ..... 164
7.6 Reliability Growth Models ..... 165
7.6.1 Discrete Reliability Growth Models ..... 166
7.6.2 Continuous Reliability Growth Models ..... 166
7.7 Bayesian Approach ..... 167
7.8 Risks in Reliability Development Programmes ..... 168
7.9 Phase 5 for Standard Products ..... 169
7.10 Phases 4 and 5 for Custom-built Products ..... 169
7.11 Case Study: Cellular Phone ..... 170
8 Product Performance and Production ..... 173
8.1 Introduction ..... 173
8.2 Phase 6 for Standard Products ..... 174
8.3 Production Process and Occurrence of Non-conforming Items ..... 175
8.3.1 Modelling Occurrence of Non-conforming Items ..... 176
8.4 Effect of Quality Variations on Reliability Performance ..... 177
8.4.1 Variation in Component Quality ..... 178
8.4.2 Variations in Assembly Operations ..... 179
8.4.3 Combined Effects of Non-conformance ..... 179
8.5 Testing During Production ..... 179
8.6 Quality Control ..... 180
8.6.1 Off-line Control of Production Process ..... 181
8.6.2 On-line Control of Production Process ..... 181
8.6.3 Weeding Out Non-conforming Components ..... 184
8.6.4 Acceptance Sampling ..... 185
8.6.5 Sub-set Selection ..... 186
8.6.6 Burn-in ..... 186
8.7 Optimal Quality Control Effort ..... 187
8.8 Case Study: Cellular Phone ..... 187
9 Post-sale Performance ..... 191
9.1 Introduction ..... 191
9.2 Phase 7 for Standard Products ..... 191
9.2.1 Field Performance ..... 192
9.2.2 Decision Process in Phase 7 ..... 193
9.2.3 Data Collection ..... 193
9.2.4 Analysis of Data and Estimating AP-II ..... 195
9.2.5 Root Cause Analysis ..... 202
9.3 Assessing Inherent and Design Reliability ..... 204
9.4 Phase 8 for Standard Products ..... 204
9.4.1 Decision Process in Phase 8 ..... 204
9.4.2 Data Collection ..... 205
9.4.3 Analysis of Data and Estimating AP-I ..... 2069.4.4 Root Cause Analysis ..... 206
9.5 Phases 7 and 8 for Custom-Built Products ..... 209
9.5.1 Phase 7 ..... 209
9.5.2 Phase 8 ..... 210
9.6 Case Study: Cellular Phone ..... 210
10 Product Safety Requirements ..... 211
10.1 Introduction ..... 211
10.2 Safety Requirements ..... 212
10.2.1 Examples of Safety Requirements ..... 212
10.2.2 Essential Health and Safety Requirements ..... 216
10.3 EU Directives ..... 217
10.3.1 New Approach Directives ..... 217
10.3.2 The Machinery Directive ..... 218
10.3.3 The General Product Safety Directive ..... 218
10.3.4 CE Marking ..... 219
10.3.5 Harmonized Standards ..... 220
10.4 Risk Assessment ..... 221
10.5 Technical Construction File ..... 223
10.6 Case Study: Cellular Phone ..... 224
11 Reliability Management System ..... 227
11.1 Introduction ..... 227
11.2 Data, Information, and Knowledge (DIK) ..... 227
11.2.1 Data and Information ..... 227
11.2.2 Knowledge ..... 228
11.2.3 Engineering Knowledge ..... 231
11.2.4 Role and Importance of DIK ..... 231
11.3 DIK in Phase 1 ..... 232
11.3.1 Data and Information ..... 233
11.3.2 Knowledge ..... 233
11.4 DIK in Phases 2 and 3 ..... 233
11.4.1 Data and Information ..... 234
11.4.2 Engineering Knowledge ..... 234
11.5 DIK in Phases 4 and 5 ..... 235
11.5.1 Data and Information ..... 236
11.5.2 Knowledge ..... 236
11.6 DIK in Phases 6-8 ..... 236
11.6.1 Data and Information ..... 236
11.6.2 Knowledge ..... 237
11.7 Reliability Management System ..... 237
11.7.1 Structure of the Reliability Management System ..... 238
11.7.2 Data and Information Module ..... 238
11.7.3 Reliability Databases ..... 244
11.7.4 Knowledge Module ..... 24411.7.5 Interface Module ..... 247
11.8 Implementation Aspects ..... 248
11.8.1 Reliability Manager ..... 248
11.8.2 Reliability Management Department ..... 249
Symbols ..... 251
Acronyms ..... 253
Glossary ..... 257
References ..... 261
Index ..... 279# An Overview 

### 1.1 Introduction

A characteristic feature of modern industrial societies is that new products are appearing at an ever-increasing pace. The drivers for new products are one or more of the following:

Consumers: The requirements and expectations of consumers have been changing - and generally growing - over time.

Technology: The technology is developing with frequent incremental innovations punctuated with less frequent radical innovations. An illustrative example is the increasing number of gates, bits, or transistors in integrated chips over time, as shown in Table 1.1.

Table 1.1. Increasing complexity of integrated chips (adapted from Walsh et al. 2005)

| Period | Number of gates, bits, or <br> transistors per device |
| :-- | :-- |
| $1947-1959$ | 1 |
| $1960-1966$ | $100-1000$ |
| $1966-1970$ | $1000-10,000$ |
| $1970-1980$ | $10,000-100,000$ |
| $1980-1990$ | $100,000-500,000$ |
| $1990-1998$ | $500,000-2,000,000$ |
| $1999-$ | $2,000,000$ and beyond |

Societal and regulatory: New legislation to protect consumers and the environment is being enacted at an increasing pace.

Long-term survival and growth requires manufacturing businesses to continuously develop and commercialize new products, or as a minimum, to redevelop current products to better meet consumer requirements as technologies change and im-prove. New products have a significant impact on sales, revenue, and profits. According to Udell and Baker (1982):
"On the average, fifty percent of a firm's profits come from products not in its line five years ago. Put another way: In five years, fifty percent of the profits the average business will earn will come from products that do not exist today."

The importance of new products for manufacturing businesses is getting more critical.

New product development is a complicated process and involves the interplay between creativity and management of the process on one hand and the varying needs of potential consumers for the new product on the other hand. The process is costly and the outcomes uncertain. As a proportion of profits, the development of new products is very significant and impacts the bottom line of business as illustrated by the following statement from Takeuchi and Nonaka (1984):
"At 3M, the multinational company, products less than five years old account for $25 \%$ of sales. In 1981 a survey of 700 U.S. companies indicated that new products would account for one-third of all profits in the 1980's, an increase from one-fourth in the 1979's."

The product life cycle, from a marketing perspective, is the period from when a product is launched until it is removed from the market. The product life cycle is roughly 5-7 years for consumer durables and roughly 7-10 years for commercial products. For some high-tech products, the product life cycle is sometimes less than two years. ${ }^{1}$

Not all new product development programmes are a success. The failure can be project related (resulting from cost and/or time limits being exceeded) or due to technical problems (existing technological capabilities being inadequate). ${ }^{2}$

Even when a new product is introduced on the market, the product can fail due to commercial factors such as poor sales, low revenue, and so on. Barclay (1992) reports on a study indicating that the three main causes of product failure are: (i) inadequate market analysis, (ii) product problems or defects, and (iii) too high costs. ${ }^{3}$

Cooper (2003) suggested the following classification scheme for characterizing new product failures.

[^0]
[^0]:    ${ }^{1}$ In the computer hard disk drive industry, the result of hundreds of millions of dollars and years of effort is a product life cycle that is only one year and a half (Kumar and McCaffrey, 2003).
    ${ }^{2}$ General Motors, the automobile manufacturer, scrapped the rotary engine project after spending more than 200 million dollars only when it was abundantly clear that it did not have the technology to produce the seals, and the seals could not be developed within a reasonable time (Balachandra, 1984)
    ${ }^{3}$ A survey by Hopkins and Bailey (1971) reports on the percentage of failures due to a variety of causes. Some of the main causes and the percentage of failures attributed to each cause are as follows:- Product related
- Intrinsic: Does not meet performance, reliability, safety or other requirements
- Extrinsic: Unfavourable reception in market, regulatory change
- Project related
- Intrinsic: Violating resource constraints (cost, time schedule)
- Extrinsic: Competitors develop product first

A product is characterized by its properties. Product performance (from a manufacturer, consumer or regulator perspective) is closely linked to the product properties. One of the product properties is product reliability. The product reliability and several other properties are dependent on the product specification that forms the basis for development of the product. As a result, product performance and specification are inter-linked and impact on the success of the new product development.

In this book we focus on reliability performance and specification in new product development. We propose a methodology for effective decision making with respect to reliability performance and specification. It is based on the product life cycle and a systems approach that involves the use of models. The goal is to ensure a high probability of success in the new product development process.

In this chapter we discuss some basic concepts and issues needed to get a better appreciation of the scope and focus of the book. The outline of the chapter is as follows: we start with a general discussion of products, properties, and perspectives in Section 1.2. Section 1.3 deals with product reliability and its importance. In Section 1.4 we discuss the product life cycle and indicate the different stages involved. Following this, we discuss product performance and specification in Section 1.5. These set the background to discuss the proposed methodology for making decisions with respect to reliability performance and specification in Section 1.6 and the scope and focus of the book in Section 1.7, respectively. We conclude the chapter with an outline of the book in Section 1.8 where we briefly discuss the contents of the remaining chapters.

# 1.2 Product Properties and Perspectives 

Most products are complex and can be decomposed into several levels with the product being at the top and components at the lowest level. The number of levels needed depends on the complexity of the product.

| Inadequate market analysis: | $45 \%$ |
| :-- | :--: |
| Product problems or defects: | $25 \%$ |
| Higher cost than anticipated: | $19 \%$ |
| Poor timing of introduction: | $14 \%$ |
| Technical or production problem: | $12 \%$ |

(Note: In some cases there is more than one cause for product failure.)# 1.2.1 Product Properties: Attributes and Characteristics 

Product properties characterize a product. They can be categorized into two groups - internal and external. The internal properties are mainly technical (e.g., the yield stress at which a component fails) and of interest to design engineers. The external properties (e.g., aesthetics, cost of operation) are of greater interest to consumers. Terms such as product features and characteristics are often used instead of product properties. According to Tarasewich and Nair (2000):
"A distinction can be made between product characteristics and attributes. Product characteristics physically define the product and influence the formation of product attributes; product attributes define consumer perceptions and are more abstract than characteristics."

Note that the internal properties correspond to product characteristics, whereas the external properties correspond to product attributes.

### 1.2.2 Consumer Perspective

Consumers view a product in terms of its attributes. According to Levitt (1980):
"To a potential buyer a product is a complex cluster of value satisfactions."
Day et al. (1978) state:
"Consumers seek benefits rather than products per se."
As a result, we have the following relationship:
Attributes (Features) $\rightarrow$ Bundle of benefits $\rightarrow$ Value to the customer
A successful new product:

1. satisfies new (or earlier unsatisfied) needs, wants or desires;
2. possesses a performance that is superior in such need satisfactions, compared with other products on the market.

Each new generation of a (successful) product is intended to be an improvement over the existing and earlier ones. Products are getting more complex in order to meet the growing consumer requirements and expectations. As a result, customers need to be assured that the product will perform satisfactorily over the useful life of the product. One way of providing this assurance is through product warranty. This is a service associated with the product. The following statement from Quality Progress (1986) illustrates the ranking of different product attributes that customers value:

The American Society for Quality Control interviewed around 1000 individuals to determine what attributes were most important to them when selecting a product. A set of predefined attributes were ranked by each customer on a scale from 1 (least important) to 10 (most important). The average scores were:| Attribute | Average score |
| :-- | :--: |
| Performance | 9.5 |
| Lasts a long time (reliability) | 9.0 |
| Service | 8.9 |
| Easily repaired (maintainability) | 8.8 |
| Warranty | 8.4 |
| Easy to use | 8.3 |
| Appearance | 7.7 |
| Brand name | 6.3 |
| Packaging/display | 5.8 |
| Latest model | 5.4 |

Source: Quality Progress, vol. 18 (Nov), pp. 12-17, 1986. Also quoted by Ebeling (1997).

# 1.2.3 Manufacturer's Perspective 

The performance of a new product, from a manufacturer's perspective, can vary depending on the objectives of the business. Barclay (1992) reports a survey that lists many different factors to define a successful new product and percentage of businesses that use the different factors in defining product success. Some factors and associated percentages, according to him are:

| Achieving expected profits: | $46.6 \%$ |
| :-- | :-- |
| Achieving expected market shares: | $26.9 \%$ |
| Meeting required quality standards: | $19.5 \%$ |

Another important factor is consumer satisfaction. It affects product sales, since dissatisfied customers might switch to buying a competitor's products and discourage others from buying the product due to negative word-of-mouth effects.

### 1.3 Product Reliability

Product reliability conveys the concept of dependability, successful operation or performance, and the absence of failures. It is an external property of great interest to both manufacturer and consumer. Unreliability (or lack of reliability) conveys the opposite.

### 1.3.1 Definition of Reliability

The reliability performance of a product is defined as:
"The ability of a product to perform required functions, under given environmental and operational conditions and for a stated period of time."
(Adapted from IEC 60050-191, para. 191-02-06).According to this definition, reliability is a rather vague characterization of the product's ability to perform required functions. Some authors and standards are using the term dependability with the same meaning (e.g., see IEC 60300-1).

In many applications, the term reliability is also used as a measure of the reliability performance, as "the probability that a product will perform one or more specified functions, under given environmental and operational conditions for a stated period of time" (Adapted from IEC 60050-191, para. 191-12-01).

All products degrade with age and/or usage. When the product performance falls below a desired level, then the product is deemed to have failed. Failures occur in an uncertain manner and are influenced by factors such as design, production, installation, operation, and maintenance. In addition, the human factor is also important.

# 1.3.2 Consequences of Failures 

## Customer Point of View

When a failure occurs, no matter how benign, its impact is felt. For customers, the consequences of failures may range from mere nuisance value (e.g., failure of the heating of the driver's seat in a car) via serious economic loss (e.g., car engine breakdown) to something resulting in serious damage to the environment and/or loss of life (e.g., critical brake failure in a car). All of these lead to customer dissatisfaction with the product.

When the customer is a business enterprise, failures lead to downtimes and affect the production of goods and services. This in turn affects the goodwill of the clients as well as the bottom line of the balance sheet.

## Manufacturer Point of View

Lack of reliability affects the manufacturer in a number of different ways. The first is affect on sales due to negative word-of-mouth effects resulting from customer dissatisfaction. This in turn affects the market share and the manufacturer's reputation. The second is higher warranty costs, resulting from servicing of claims under warranty.

Sometimes, regulatory agencies (e.g., the US Federal Transport Authority) can order the manufacturer to recall a product and replace a component that has not been designed properly from a reliability point of view. In some cases, the manufacturer is required to provide compensation for any damage resulting from failures of the product.

There is no way that a manufacturer can completely avoid product failures. Product reliability is determined by pre-production decisions and impacts the postproduction outcomes. The challenge to the manufacturer is to make decisions that achieve a balance between the costs of building-in reliability versus the consequences of the lack of adequate reliability.# 1.4 Product Life Cycle 

From the manufacturer's perspective, the product life cycle consists of the five phases shown in Figure 1.1. The first three phases (front-end, design, and development) are the pre-production phases and the last two phases are production and postproduction.

| Front-end | $\rightarrow$ | Design | $\rightarrow$ | Development | $\rightarrow$ | Production | $\rightarrow$ Post-production |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |

Figure 1.1. Phases of product life cycle

The front-end deals with new product decisions at the business level. Once a decision is made to proceed with new product development, we move to the design phase. The design phase can be broken into two sub-phases (conceptual and detail design) and similarly, the development and production phases can be broken into two sub-phases (component and product).

The outcome of the development phase is a prototype of the product. If this is suitable for release to the market, then we move to the production phase. The postproduction phase consists of marketing the product and providing the post-sale support for products sold.

### 1.5 Product Performance and Specification

### 1.5.1 Product Performance

Product performance is a complex entity involving many dimensions and depends on the customer's and manufacturer's perspectives. For each perspective, it is best characterized as a vector of variables, where each variable is a measurable property of the product or its elements.

## Desired versus Actual Performance

As the name implies, the desired performance is a statement about which performance is desired from a product, that is, what performance the product should have.

For manufacturers, the desired performance forms the basis for a new product development that will achieve their business goals. For customers, the desired performance defines the expectations in their purchase decisions.

The actual performance is defined as the observed performance of a prototype of a product during development or of a manufactured product over its operating life.

The actual performance will usually differ from the desired performance. The more the actual performance deviates from both the manufacturer's and customers' desired performance, the higher is the probability that the product will not satisfy the manufacturer's and/or customers' expectations.# 1.5.2 Product Specification 

The product specification forms the basis for building a prototype to ensure that the product achieves the desired performance before production commences. As we proceed through the design phase (from product level to component level), we need to define a hierarchy of more detailed specifications that are linked to the desired performance. A proper understanding of the links between performance and specification is critical in order to ensure the success of the new product.

### 1.5.3 Performance-Specification Relationships

The specification is derived from the desired performance and depends on the design option selected and the underlying design principles. The predicted performance is derived from the specification using models and data. During the design phase, the data is obtained from engineering handbooks and vendor catalogues and during the development phase, test data is used.

Deriving the specification that will ensure that the predicted performance and the desired performance match, is an iterative process as shown in Figure 1.2. Changes are made to either the specification and/or the desired performance during each iteration cycle. The process stops when we arrive at a specification where the predicted performance matches the desired performance and production can commence.


Figure 1.2. Performance - specification relationships

### 1.6 Reliability Performance and Specification

Reliability performance and specification have not received proper attention in the reliability and the engineering design literature. This is indeed surprising given theimportance of product reliability and the consequences of unreliability for both customers and manufacturers.

Deciding on reliability performance and specification for a new product requires solving a variety of problems. Two major problems are as follows:

1. How to obtain the specification given the desired performance?
2. How to obtain the predicted performance given a specification?

In the process, we need to solve a range of sub-problems relating to different phases of the product life cycle. Some of these involve answering "what if?" questions and others to make the optimal choice. A small sample is given below.

- How do warranty period and sale price affect total sales? (Front-end phase)
- How to determine product reliability in terms of component reliability? (Design phase)
- How to assess component reliability based on data (objective and subjective) from different sources? (Development phases)
- How to determine the expected warranty costs? (Post-production phase)
- What is the optimal choice between repair and replacement to minimize the expected warranty cost? (Post-sale phase)
- What is the optimum number of components to be tested during development? (Development phase)


# 1.6.1 Methodology for Reliability Performance and Specification 

A proper methodology for deciding on the reliability performance and specification for a new product requires the following:

1. A product life cycle perspective so that the different reliability issues are linked in an effective manner
2. An integrated framework where the technical aspects (that determine product reliability) and the commercial aspects (dealing with the consequences of lack of adequate reliability) are integrated
3. An effective approach to solve a wide variety of problems

### 1.6.2 Systems Approach

The systems approach (shown in Figure 1.3) is the most appropriate approach to find solutions to the many relevant problems in reliability performance and specification.

The key feature of the systems approach is the use of models (qualitative as well as quantitative). The building and validation of a model require data and information, and model analysis requires a variety of tools and techniques. ${ }^{4}$

[^0]
[^0]:    ${ }^{4}$ There are many books dealing with the application of the systems approach to solve problems in different disciplines (Roland and Moriarty, 1990; Blanchard and Fabrycky, 1998; Blanchard, 2004).

Figure 1.3. Systems approach to problem solving

# 1.7 Objectives of the Book 

The main objectives of the book are as follows:

1. To develop a methodology for deciding on reliability performance and specification for new products
2. Highlight the role and use of models as a tool in solving decision problems
3. Discuss the tools and techniques needed for model building and model analysis
4. Address other issues, such as data collection, management systems, and so on

We focus primarily on the basic concepts and issues and illustrate them through the following two cases. ${ }^{5}$

### 1.7.1 Case 1 [Cellular Phone]

The term telephone is derived from two Greek words - tele (far) and phone (sound) - to describe any equipment for conveying sound at a distance. The first telephone was built towards the end of the nineteenth century and the basic principles of a telephone have remained unchanged. The voice vibrates the air, which in turn vibrates a diaphragm. This motion produces a variation in an electric signal. This is transmitted over distance and used to vibrate a diaphragm at the receiving end to reproduce the voice.

Until 1947, the transmission of the electric signal was done using copper cables. In 1947 microwave technology was used for the first time to transmit signals. Both of these required the phone being connected to a transmitter. The cellular telephone first appeared in 1973 and has its own transmitter to send and receive electric signals. This, combined with satellites, implied a seamless transmission of voice as long as the telephone sending the message and the one receiving the message were within geographical range of the communication satellite involved.

Millions of people around the world use cellular phones. A modern cellular phone has an array of functions in addition to sending voice. These include:

- Get information (such as news, entertainment, stock quotes) from the Internet
- Send and receive text mail

[^0]
[^0]:    ${ }^{5}$ Throughout the book we provide references where interested readers can find more details.- Send or receive e-mails
- Store contact information details
- Alarm clock
- FM radio
- Make task and to-do lists
- Calendar to keep track of appointments and set reminders
- Carry out simple arithmetic calculations
- Games console to play games
- Integrate other devices such as MP3 players, and so on.

The sales (worldwide) have been growing exponentially with 488 million units sold in 2003 and 620 million units in 2004.

# 1.7.2 Case 2 [Safety Instrumented System] 

A safety instrumented system (SIS) is a protection system that is installed to prevent and/or mitigate risk associated with the operation of many types of hazardous systems. A SIS generally consists of one or more input elements (e.g., sensors, transmitters), one or more logic solvers (e.g., programmable logic controllers, computers, relay logic systems), and one or more final elements (e.g., safety valves, circuit breakers). The main elements of a SIS are illustrated in Figure 1.4.


Figure 1.4. Sketch of a simple safety instrumented system (SIS)

SISs are used in many sectors of modern society, for example, as emergency shutdown systems in chemical plants, fire and gas detection and alarm systems, pressure protection systems, dynamic positioning systems for ships and offshore petroleum platforms, automatic train stop systems, anti-lock brakes in automobiles, and systems for interlocking and controlling the exposure dose of medical radiotherapy machines.

The main functions of a SIS are:

- When a predefined process demand (deviation) occurs, the deviation shall be detected by the SIS input elements, and the required final elements shall be activated and fulfil their intended functions.
- The SIS shall not be activated spuriously, that is, without the presence of a predefined process demand (deviation) in the system.A failure to perform the first system function is called a fail to function, and the failure of the second function is called a spurious trip.

Safety and reliability requirements for the SIS functions are given in the international standard IEC 61508 and related standards. IEC 61508 is a performance-based, generic standard that covers most safety aspects of a SIS.

# 1.8 Outline of the Book 

The book has 11 chapters. A brief summary of the chapters is as follows:
Chapter 1, An Overview: This chapter deals with the importance of product performance and specifications in the context of new product development. The scope and focus (on reliability performance and specifications) of the book are described and an outline of the structure of the book is given. The two illustrative cases that will be used throughout the book are presented.
Chapter 2, New Product Development: The chapter starts with a general discussion of products and then looks at the new product development process and discusses different models proposed in the literature. Following this, it outlines the two-stage, three-level model that is used in later chapters.
Chapter 3, Product Performance and Specification: There are many different notions of product performance and of production specification. The chapter critically reviews the literature, defines the notion that is used in this book, and discusses the relationships between the two. It then develops a hierarchy of performance and specifications based on the model in Chapter 2. It concludes with a methodology for making decisions with regard to performance and specification. This involves the use of models. The data requirements and the tools and techniques needed for decision making are also discussed.
Chapter 4, An Introduction to Reliability Theory: Reliability theory deals with the interdisciplinary use of probability, statistics, and stochastic modelling, combined with engineering insight into the design, and the scientific understanding of the failure mechanisms, to study the various aspects of reliability. As such, it encompasses issues such as (i) reliability modelling, (ii) reliability analysis and optimization, (iii) reliability engineering, (iv) reliability science, (v) reliability technology and (vi) reliability management. All of these are important in the context of reliability performance and specification. The chapter discusses the important concepts and issues that are needed for later chapters.
Chapter 5, Performance and Specification in the Front-end Phase: Product performance from the business perspective is the starting point of a new product development process. This issue is discussed for different kinds of products. It then looks at translating this into alternative sets of product specifications (which define product attributes and features), the technical and commercial implications and to evaluate the economic viability. Product reliability is not addressed explicitly, but the implications of it on the technical and commercial aspects need to be addressed at this phase. Once this is met, the specification is passed on to thedesign group to come up with designs to produce the product. The chapter deals with models, data and, tools and techniques needed to derive the specifications and to evaluate the implications for the business and the economic viability.
Chapter 6, Performance and Specification during Design: The design process involves two sub-phases - conceptual and detailed design. For the conceptual phase, the specification from the front-end phase defines the desired performance. The design group looks at alternative design architectures and their technical and economic implications. If the outcome is favourable, we proceed to the detailed design. In both these phases, the aim is to translate the desired performances (at various sub-levels) into specifications with the specification at a sub-level being linked to performance at the sub-level above it. The reliability issues include reliability allocation, reliability improvement (through development and/or redundancy), maintenance and maintainability. The chapter discusses a variety of reliability related decision problems using a format similar to Chapter 5. The final outcome of the design process is a specification at the lowest level and is used in the fabrication of the product.
Chapter 7, Performance during Development: The development phase involves development at component and at system level. At component level, we may test the actual component reliability performance. If this falls below the desired value, then we need to carry out programmes to improve the reliability. One such is the test-analyse-and-fix (TAAF) programme where products are tested to failure and through a root cause analysis a solution is found to avoid the failure and thus improve the reliability. At the system level, we assess the actual performance of the final prototype through testing. Often, tests are carried out to assess the performance under different environments, the limits of the actual performance, and so on. In addition, we need to carry out tests in accelerated mode so as to reduce the development time. The reliability issues include optimal design of experiments for assessing reliability, planning of accelerated tests, and statistical methods for reliability assessment. The chapter deals with these issues in the context of assessing the actual reliability performance. The focus is on the models needed for designing tests, data collection issues, tools and techniques for data analysis, and models to assess and/or predict actual performance.
Chapter 8, Product Performance and Production: The actual performance of products produced in large numbers will differ from the actual performance of the prototype in the development phase. This is because of quality variations in the inputs (e.g., material, components bought from vendors) and variations in the production process. The chapter looks at the effect of these factors on the performance and techniques to control and/or minimize their effects. The issues include acceptance sampling of components so that the components meet the required reliability specification and assessing reliability variations during production. The techniques for data analysis to assess actual performance are similar to those in Chapter 7.
Chapter 9, Post-sale Performance: The actual performance in the post-sale phase will differ from that during the production phase due to variability in the external factors, such as, usage environment, usage intensity, maintenance, and so on. Themain source of information (for consumer durables) is the claims under warranty. Here again, the focus is on assessing actual performance based on the warranty data and other information. The chapter deals with this topic and the comparison between the actual and the desired performance at the business level, and the implications for changes to product specifications. The reliability issues include warranty cost analysis, data collection, decision making for improvements, and so forth. The chapter also deals with issues such as product recall and warranty logistics.
Chapter 10, Product Safety Requirements: Many products may cause health problems, injuries and/or pollution of the environment. The problems may occur during normal use of the product, transport, cleaning and maintenance, and also due to misuse of the product. Problems caused by product failures may, to some degree, be prevented or mitigated by using the procedures in the previous chapters of this book. Several other hazards are not covered by these procedures, and need to be addressed in separate programmes. The chapter outlines an approach to product safety that can be integrated with the reliability programme. The product safety programme is compatible with the European safety directives, especially the Machinery Safety Directive.
Chapter 11, Reliability Management System: Decisions with regards reliability performance and specification require the linking of decision making at the different stages of the product life cycle. This must be done in an integrated manner. A management system is needed for carrying this out and this topic is addressed in this chapter. The key elements of the management system are: (i) a data collection system, (ii) a package of tools and techniques for data analysis and for model building, analysis and optimization, and (iii) a user interface to assist the manufacturer in making effective decisions. The chapter discusses the issues associated with the collection and analysis of reliability related data.# New Product Development 

### 2.1 Introduction

New product development is a multi-stage process. Many different models with a varying number of stages have been proposed in the literature. We briefly review these models and propose a new model that is better suited to decision making regarding product performance and specification. In this chapter we start with a discussion of products and product life cycle in order to set the background for the later sections of the chapter.

The outline of the chapter is as follows. In Section 2.2 we look at product classification and decomposition. Section 2.3 deals with product life and product life cycle. Section 2.4 gives an overview of new product development and reviews some of the models proposed in the literature. Section 2.5 deals with the concepts and activities in the different phases of the five-phase product life cycle indicated in Figure 1.1. This sets the background for a new model that is appropriate for deciding on performance and specification in the context of new product development. Section 2.6 deals with this new model.

### 2.2 Products

A narrow definition of products is that they are physical and tangible. This is in contrast to services that are intangible. The distinction between products (as defined above) and services is getting blurred and a more commonly accepted definition is that a product generally involves combinations of the tangible and the intangible as indicated below.
"A product can be tangible (e.g., assemblies or processed materials) or intangible (e.g., knowledge or concepts), or a combination thereof. A product can be either intended (e.g., offering to customers) or unintended (e.g., pollutant or unwanted effects)."
(ISO 8402).Consumers buy products for different reasons and can be broadly divided into three categories:
Households: These comprise individuals (or families) buying products, such as food items, cosmetics, clothes, televisions, kitchen appliances, household furniture, and so on.
Industrial and commercial organizations: These comprise businesses buying a range of products (e.g., furniture, computers, telephones) for use in the office; products to deliver services (e.g., X-ray machines in hospitals, trucks to move goods from factory to markets, trains to move people) and products (e.g., lathes, assembly robots, components) to produce other products for sale.
Governments: These not only buy the products consumed by households and industrial and commercial organizations to administer and provide services, but also products (e.g., tanks, ships) to defend the country.

# 2.2.1 Product Classification 

Products can be classified in many different ways, as indicated below.
Classification 1: Based on the type of consumer
This is the most common classification.
Consumer non-durables and durables: These products are bought by households. The non-durables differ from the durables in the sense that the life of a nondurable product (e.g., cosmetic, food) is relatively short, and the product is less complex than a durable product (e.g., cellular phone, television).
Industrial and commercial products: These are standard (off-the-shelf) products used by industrial and commercial organizations for their operations. The technical complexity of such products can vary considerably. The products can be either complete units, such as cars, computers, trucks, pumps, and so forth, or product components needed by a manufacturer, such as batteries, drill bits, electronic modules, and toner cassettes for laser printers.
Specialized defence-related or industrial products: Specialized products (e.g., military aircraft, ships, and rockets) are usually complex and expensive and involve state-of-the-art technology with considerable research and development effort required of the manufacturers. Customers are typically governments or industrial businesses. These products are usually designed and built to the specific requirements of the consumer. Still more complex are large systems (e.g., power stations, chemical plants, computer networks, and communication networks) that are collections of several inter-linked products.

## Classification 2: Standard versus custom-built

Standard products: These are manufactured in anticipation of a subsequent demand. As such, the products are manufactured based on market surveys. Standard products include all consumer non-durables and durables and most commercial and industrial products.Custom-built products: These are manufactured in response to a specific request from a customer, and include specialized defence and industrial products.

# Classification 3: Based on the nature of design and design process 

Parsaei and Sullivan (1993) suggest the following classification:
Creative designs: Creative design is an abstract decomposition of the design problem into a set of levels that represent choices for the problem. An a priori plan for the problem does not exist.
Innovative designs: The decomposition of the problem is known, but the alternatives for each of its sub-parts do not exist, and must be synthesized. Design might be an original or unique combination of existing components. A certain amount of creativity comes into play in the innovative design process.
Redesign: An existing design is modified to meet the required changes in the original functional requirements.
Routine designs: An a priori plan of the solution exists. The sub-parts and alternatives are known in advance, perhaps as the result of either a creative or innovative design process. Routine design involves finding the appropriate alternatives for each sub-part that satisfies the given constraints.

## Classification 4:

Hubka and Eder (1992) suggest a broader classification that captures complexity, usage, appearance, and methods for designing the product. According to their classification, products range from artistic work to industrial plant as indicated below:

1. Artistic works
2. Consumer durables
3. Bulk or continuous engineering products
4. Industry products
5. Industrial products
6. Industrial equipment products
7. Special purpose equipment
8. Industrial plant

Product appearance is more important for products at the top of the list, while methods for designing and use of scientific knowledge are important for products at the bottom of the list. For artistic works, the artist is usually both the designer and manufacturer. Industrial plant is the extreme case of products incorporating other products, and consists of collections of industrial equipment and devices to provide control and/or connections among them.

## Classification 5: New versus used (or second-hand) products

There are several different notions of a new product and these are discussed in the next sub-section. In contrast, an old product is one that has been on the market for some time.We need to differentiate between a new item and a used (or second-hand) item. If the useful life of a product is much greater than the product life cycle (discussed in Section 2.3), customers often replace a working old item (old product) with a new one (new product). As a result, a market for used or second-hand products is created.

# 2.2.2 "Newness" of a New Product 

New products are replacing existing products on a regular basis. The rate at which new products are appearing on the market is growing at an exponential rate. The reasons for this are many and can include one or more of the following:

- Create a differential advantage (product differentiation)
- Support continued growth for the manufacturer
- Capitalize on technological breakthroughs
- Response to changing demographics

There are several different notions of what constitutes a new product. The "newness" of a new product can vary from high to low and depends on whose perspective and what is new.

The different perspectives yield the following:

1. New to the world (e.g., the first aircraft, radio, computer, car)
2. New to the industry (first application in an industry of a product well established in some other industry)
3. New to the manufacturing firm (and familiar to competitors in the industry)
4. New to the market
5. New to the customer

Viewed in terms of what is new, yield the following:

1. New technology (digital computer replacing analogue computer)
2. New process (which reduces the production cost and/or increases the quality of conformance)
3. New features (this is most dramatic in consumer electronics, such as, cellular phones)
4. New uses (chips designed for computers being used in domestic appliances)
5. New design (which reduces the production cost)

The degree of newness is an indicator of the difference between the new product and the existing one. The change (depending on the perspective) can vary from minor or incremental to major or radical. For example, a change that reduces the production cost might be viewed as a major change from the manufacturer's perspective and no change from the customer's perspective. A radical change is due to a new technology (higher speeds resulting from jet engines that was not possible with the earlier propeller engines) whereas an incremental change is due to advances within an existing technology.The newness from the customer perspective deals with improvements in the product attributes (e.g., increase in the fuel efficiency of a car) or new features that meet new requirements or result in greater benefits. ${ }^{1}$

Example 2.1. DNV RP A203 is a guideline for reliability qualification of new technology for the offshore oil and gas industry. The guideline classifies the products to be qualified into four categories as follows:

| Technological <br> status $\rightarrow$ | Proven <br> in use | Limited <br> field history | New or <br> unproven |
| :-- | :--: | :--: | :--: |
| Known application | 1 | 2 | 3 |
| New application | 2 | 3 | 4 |

The categories indicate:

1. No new technological uncertainties

- Both the product, the application, and the environmental conditions are known

2. New technological uncertainties

- The product has a limited field history, but the application and the environmental conditions are new
- The product is well known (proven in use), but the application and/or the environmental conditions are new

3. New technological challenges

- The product is new, but will be used in well-known applications, and under known environmental conditions
- The product is partly known (with limited field history) and will be used for a new application and/or in new environmental conditions

4. Demanding new challenges

- The product is new and both the application and the environmental conditions are new.


# 2.2.3 Product Decomposition 

The complexity of products has been increasing with technological advances. The following example, from Kececioglu (1991), indicates the increase in the numbers of components in a tractor over time.

| Model year | 1935 | 1960 | 1970 | 1980 | 1990 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Number of components | 1200 | 1250 | 2400 | 2600 | 2900 |

For more complex products, the number of parts may be orders of magnitude larger. For example, a Boeing 747 airplane has 4.5 million components (Appel, 1970).

As a result, a product needs to be viewed as a system comprising several elements and can be decomposed into a hierarchy of levels, with the system at the top level and components at the lowest level. There are many ways of describing this hierarchy and the following description is from Blischke and Murthy (2000):

[^0]
[^0]:    ${ }^{1}$ For further discussion on this topic, see Garcia and Calantone (2002).| Level | Characterization |
| :--: | :-- |
| 0 | System |
| 1 | Sub-system |
| 2 | Major assembly |
| 3 | Assembly |
| 4 | Sub-assembly |
| 5 | Component |

The number of levels needed to describe a product from system level down to component level depends on the complexity of the product.

Example 2.2 (Cellular Phone). The cellular phone is a very complex product. The main elements are:

- Circuit board
- Antenna
- Liquid crystal display
- Keyboard
- Microphone
- Speaker
- Battery

Each of these can be decomposed into lower levels. For example, in the case of the circuit board, it is the heart and brain of the system and contains several computer chips and other components. The different chips and components and their functions are as follows:

- Analogue-to-digital and digital-to-analogue chip: It translates the outgoing audio signal from analogue to digital and the incoming signal from digital back to analogue.
- Microprocessor chip: It handles all of the housekeeping chores for the keyboard and display, deals with command and control signalling with the base station and also coordinates the rest of the functions on the board.
- ROM and flash memory chips: These provide storage for the phone's operating system and other features, such as the phone directory.
- Radio frequency and power section: This handles power management and recharging, and also deals with the hundreds of FM channels.
- Radio frequency amplifiers: These handle signals travelling to and from the antenna.

Example 2.3 (Safety Instrumented System). All safety instrumented systems have at least three main sub-systems: (1) input elements, (2) logic solver, and (3) final elements. The number of assemblies and components in each sub-system may range from a single item, to a large number of items. The final elements (e.g., shutdown valves) often have a fail-safe design and are equipped with electric, hydraulic or pneumatic utility systems. The input elements usually have features for diagnostictesting. The logic solver often has a duplex or triplex configuration to facilitate selftesting. The sensors are often configured as a $k$-out-of- $n$ system, meaning that at least $k$ out of $n$ input elements have to give signal to the logic solver to raise an alarm. $\oplus$

# 2.3 Product Life and Product Life Cycles 

### 2.3.1 Product Life

The useful life of a product is the age beyond which the product is deemed to be unsuitable for further use due to its inability to perform satisfactorily. This is a random variable due to variation in manufacturing and/or usage. For a repairable product, a component of the product can fail several times over its useful life and is restored to operational status through corrective maintenance actions.

In the context of new products, a related notion is the time for which a consumer uses the purchased product before it is replaced by a new one. This can be called the period of ownership. This is also a random variable as different consumers keep the purchased product for different lengths. If consumers keep the products for the useful life, then the products are scrapped at the end of their useful life. In this case, there are no second-hand products. If the period of ownership is shorter than the useful life, a market for second-hand products is created.

### 2.3.2 Product Life Cycle

The product life cycle concept is quite different in meaning, intent, and importance for consumers and manufacturers. ${ }^{2}$ From the manufacturer's perspective there are two different notions.

The product life cycle can be viewed in a larger overall context, with important strategic implications (Betz, 1993). Here, the product life cycle is seen as embedded in the technology life cycle where there are several product life cycles within a technology life cycle. Revolutionary technological innovations result in a new technology platform (e.g., internet access) with multitudes of technology generations developing over time (e.g., phone modem, ISDN, ADSL) with each technology generation characterized by four phases: introduction, rapid growth, mature, and decline. Within each technology generation, a multitude of products are developed, following similar product life cycles. The technology platform also follows a similar technology life cycle.

## Consumer Perspective

From the consumer's point of view, the product life cycle is the time from the purchase of an item to its discarding when it reaches the end of its useful life or being replaced earlier due to either technological obsolescence or the item being no longer of any use. The life cycle involves the following three phases:

[^0]
[^0]:    ${ }^{2}$ See Rink and Swan (1979) for more on product life cycle.1. Acquisition
2. Operation and maintenance
3. Discard (and leading to replacement by a new one)

# Manufacturer Perspective 

There are two different notions - marketing and manufacturing.
Marketing: The product life cycle is the period from the instant the product is launched on the market to the time when it is withdrawn from the market and involves the following four phases:

1. Introduction phase (with low sales)
2. Growth phase (with rapid increase in sales)
3. Maturity phase (with near constant sales)
4. Decline phase (with decreasing sales)

Manufacturing: The product life cycle is the period from the initial conception of the product to the final withdrawal of the product from the marketplace. It can be broken into five phases as indicated in Figure 1.1.

### 2.4 New Product Development

The US based Product Development \& Management Association defines new product development as
"A disciplined and defined set of tasks and steps that describe the normal means by which a company repetitively converts embryonic ideas into saleable products or services."
(Belliveau et al., 2002).

### 2.4.1 New Product Development in the Overall Business Context

Businesses use strategic management to achieve their long-term objectives. This requires formulating strategies for various elements of the business in a coherent manner so that they are consistent and integrated. Once this is done, procedures to implement the plans need to be devised. The resulting actions need to be monitored so that changes can be made and the process controlled in an effective manner. Figure 2.1 (adapted from Fairlie-Clarke and Muller, 2003) shows some of the key strategies with product development strategy being one of them. The success of the new product development depends strongly on formulating and implementing strategies.

According to Wheelwright and Clark (1992), companies succeeding in the global and dynamic competition are those that are able to bring new products fast to the market, products that satisfy the expectations of the customer. Those:

1. approaching new product development in a structured manner are more successful than those with an ad-hoc approach
2. emphasizing early stages, have a higher chance of success than those not doing so

Figure 2.1. New product development as part of business processes

# 2.4.2 A Brief Review of New Product Development Models 

A variety of models have been proposed to get better insight into the new product development process and its management. The process starts with an idea to build a product that meets specific requirements (or create new requirements for radically innovative products) defined by customers and/or the manufacturer, and ends when the product is launched on the market. It involves several phases and the number of phases and descriptions of the phases vary from model to model. An illustrative sample is given in Table 2.1. ${ }^{3}$

The diversity in the number of phases, the different terminology used, and different interpretations of the same terms may best be explained by the different contexts, such as (1) type of product (mechanical, electrical, mechatronic, electronic), (2) degree of innovation (redesign vs. routine design), (3) product complexity, (4) production process (manual, highly automated, existing production facilities), (5) type and number of suppliers/original equipment manufacturers (OEMs), (6) tech-

[^0]
[^0]:    ${ }^{3}$ Other models and further discussion can be found in Hubka and Eder (1992); Fairlie-Clarke and Muller (2003); Aoussat et al. (2000); Büyüközkan et al. (2004); Cooper (2001); Cross (1994); Drejer and Gudmundsson (2002); French (1985); Ottoson (2004); Sim and Duffy (2003); Suh (2001); Ullman (2003); Weber et al. (2003)Table 2.1. Different phases for an illustrative sample of new product development models

| Model | Phases |
| :--: | :--: |
| Model 1 <br> (Roozenburg and Eekels, 1995) | Analysis $\rightarrow$ Concept $\rightarrow$ Materialization |
| Model 2 <br> (IEC 60300-1) | Concept and definition $\rightarrow$ Design and development $\rightarrow$ Manufacturing and installation |
| Model 3 <br> (Fox, 1993) | Pre-concept $\rightarrow$ Concept $\rightarrow$ Design $\rightarrow$ <br> Demonstration $\rightarrow$ Production |
| Model 4 <br> (Pahl and Beitz, 1996) | Clarification of task $\rightarrow$ Conceptual design $\rightarrow$ <br> Embodiment design $\rightarrow$ Detail design |
| Model 5 <br> (Cooper, 2005) | Scoping $\rightarrow$ Build business case $\rightarrow$ Development $\rightarrow$ Testing and validation $\rightarrow$ Launch |
| Model 6 <br> (Blanchard, 2004) | Conceptual design $\rightarrow$ Preliminary system design $\rightarrow$ <br> Detailed design and development $\rightarrow$ Construction $\rightarrow$ <br> Production |
| Model 7 <br> (Pugh, 1990) | Market $\rightarrow$ Specification $\rightarrow$ Concept design $\rightarrow$ Detail design $\rightarrow$ Manufacture |
| Model 8 <br> (Andreasen and Hein, 1987) | Recognition of need $\rightarrow$ Investigation of need $\rightarrow$ <br> Product principle $\rightarrow$ Product design $\rightarrow$ <br> Product preparation $\rightarrow$ Execution |

nologies involved, (7) availability of resources (e.g., manpower), and (8) time and budget constraints. ${ }^{4}$

# 2.5 Product Life Cycle Phases: Basic Concepts and Activities 

In this section we discuss the basic concepts and activities in the five different phases of the product life cycle model shown in Figure 1.1. This is needed for a proper understanding of the new model for decision making regarding product performance and specification in new product development.

### 2.5.1 Front-end

## Opportunity, Idea, and Concept

These three terms are closely related and important in the context of new product development, and may be defined as follows (adapted from Belliveau et al. (2002)):

[^0]
[^0]:    ${ }^{4}$ For further discussion on these topics, see Hales (1993); Maffin (1998); Nellore and Balachandra (2001); Song and Montoya-Weiss (1998); Tatikonda and Rosenthal (2000); Veryzer (1998).Opportunity: An identified business or technology gap that exists between the current situation and a potential future that can be exploited to gain competitive advantage or solve a problem.
Idea: The earliest perception of a new product or service. It may be an early view of a solution for taking advantage of the opportunity.
Concept: Has well-defined form and description, and includes an understanding of the technology needed, the primary features, and customer benefits.

The aim of the front-end phase is to process and select ideas that may exploit emerging opportunities, and further develop the selected ideas to feasible concepts. ${ }^{5}$

# New Product Development Drivers 

The trigger (need or opportunity) for a new product idea can be one or more of the following factors:

Technology: Advances in technology (either in-house or outside) provide an opportunity to improve existing products.
Market: The manufacturer has to improve his existing product in response to (i) competitor actions (e.g., reducing the price or an improvement to their product) and/or (ii) feedback from customers through complaints about product performance.
Management: The motivation for improvement could be (i) internal (e.g., to increase market share, or improve profits by reducing warranty cost) and (ii) external (e.g., new legislation related to product performance).

## Screening of Ideas

The new product drivers above generate a continuous flow of new product ideas. Thus, there is also a continuous screening of ideas to decide which ones to pursue further. Screening is concerned with answering the following questions (adapted from Cooper (2001)):

1. Does the idea fit within the business market or technology focus area ?
2. Are the business opportunities attractive (e.g., potential market size and growth)?
3. Is it technically feasible to develop and produce the product?
4. Are there any potential hindrances that may stop the project (e.g., legislative and/or environmental issues)?

Once an idea is selected for further investigation the subsequent activities that need to be carried out can be grouped into three groups: (i) product definition, (ii) project plan, and (iii) project definition review. ${ }^{6}$

[^0]
[^0]:    ${ }^{5}$ This process is very selective, since up to $90 \%$ of the ideas and $80 \%$ of the concepts may be dismissed (Cooper et al., 1998).
    ${ }^{6}$ A review of the literature on front-end indicates a considerable variation in the activities to be carried out in the front-end phase. We include screening of the idea whereas many others view the front-end starting after the ideas have been screened.# Product Definition 

The main task in the product definition is to translate feasible ideas into technically and economically feasible and competitive product concepts as shown in Figure 2.2. An important aspect of this process is the capture of business objectives (presented by internal stakeholders) and customer requirements (presented by external stakeholders) such that a concept meeting these may be developed. This process may be called "requirements capture" (Cooper et al., 1998). The product definition states what characteristics (preferably measurable) that the product should have in order to meet the expectations of both internal and external stakeholders. To establish the product definition is an iterative process involving:

1. Market investigations and market research studies
2. Competitive analyses
3. Business and financial analyses
4. Technical and manufacturing appraisals
5. Resource and capabilities assessments, all aiming at ensuring the feasibility of the concept ${ }^{7}$


Figure 2.2. Deriving product definition

## Business Objectives

The business objectives can be defined as "the overall business goals for the new product development process" or "what the product should do for the business." It can be the required return on investment, desired market share, and so on. The factors that influence the business objectives are as indicated in Figure 2.3.

[^0]
[^0]:    ${ }^{7}$ Refer to Cooper (2001); Khurana and Rosenthal (1998) for more details.

Figure 2.3. Factors influencing business objective

# Customer Requirements 

For consumer durables, customer requirements, wants, and preferences (what the product should do for the customers) are identified through market research. A problem of concern is that customers often state the requirements in a vague manner. This represents a great challenge when conducting market studies and in translating the vague requirements into specific product characteristics. ${ }^{8}$ For custom-built products, the customer usually defines the requirements, wants, and preferences in detail.

## Concept Generation and Screening

The process of generating feasible concept specifications is concerned with

1. Identifying the possible concepts that can be pursued to meet the business objective and the customer requirements
2. Evaluating the most likely candidates in terms of performance
3. Deciding on preferred concept(s)

The concept generation process starts with determining the overall functions (and sub-functions) of the product. What the product should do, is defined through these functions, prior to exploring product concepts and solutions. ${ }^{9}$ Next, solution principles for the sub-functions are generated. A solution principle is
"An idealized (schematic) representation of the structure of a system or a subsystem in which the characteristics of the elements, and the relations

[^0]
[^0]:    ${ }^{8}$ See Urban and Hauser (1993) for the tools and techniques for identifying customer requirements. The quality function deployment (QFD) method is widely used for translating the requirements into specific product characteristics, see ReVelle et al. (1998).
    ${ }^{9}$ For further discussion, see Blanchard (2004); Fox (1993); Pahl and Beitz (1996); Pugh (1990); Suh (2001); Ullman (2003).which are essential to the functioning, are qualitatively determined."
(Roozenburg and Eekels, 1995).
The solution principles for an overall system are determined from the combination of the solution principles developed for the different sub-systems. Further, the overall solution principles form the basis for concept variants. A concept should define the means of performing each major function, as well as the spatial and structural relationships of the principal components. Concepts should also provide sufficient detail for cost and weight approximations (French, 1985). The concept may be given a schematic representation in the form of a function structure, a circuit diagram or a flow chart (Pahl and Beitz, 1996).

The freedom to choose function structures and solutions depends on the degree of product modularization, as dictated by the product platform strategy set out by the manufacturer.

# Product Platforms and Modularization 

Platform strategies and modularization have significant impact on the concept generation process. In the ever tougher global competition manufacturers are facing, many manufacturers attempt to reduce design and production costs by increasing the use of the same parts, or modules, across different products. Product platforms and modularization are common concepts in this context. A broad definition of a platform is (adapted from Meyer and Lehnerd, 1992):
"[...] a relatively large set of product components that are physically connected as a stable sub-assembly and are common to all different products."

Muffatto (1999) describe a module as:
"[...] a large group of components that are physically coherent as a subassembly, which often has standardized interface designs. Modules may be common across different products, but they may also be specific to any one model."

Product platforms allow manufacturers to reduce the number of product specific components, and, in turn reducing the production cost as plants are utilized better, and the logistics are simplified. It also allows manufacturer to better meet individual customer demands.

Long-term benefit from product platforms requires a long-term planning for product development. This allows many products to share the same product platform over some time. ${ }^{10}$

[^0]
[^0]:    ${ }^{10}$ Muffatto and Roveda (2000) discuss this in more detail. Gershenson et al. (2003) and Gershenson et al. (2004) present a review of existing research on measures of modularity and methods to achieve modularity in product development.# Project Plan 

The project plan deals with planning the remainder of the new product development project in detail and deals with issues such as time and resource allocation, scheduling of tasks, and so on. ${ }^{11}$ Blanchard (2004) provides a fairly extensive description of the necessary elements of the planning process and the project plan. The project planning encompasses:

- Activity planning
- Definition of roles and responsibilities
- Resource and service planning
- Risk management planning
- Establishing project performance measures


## Project Definition Review

The project definition review encompass a final review and evaluation of the product definition and project plan, prior to making the decision whether or not to launch a full-scale development project. ${ }^{12}$

Note. Empirical studies show that for most manufacturers, this phase is often the least focused even for high-risk new product development projects, where the success depends very critically on the decisions made during this phase. ${ }^{13}$

### 2.5.2 Design

The design phase is concerned with arriving at product characteristics that may provide the desired product attributes determined in the front-end phase. This phase may consist of several sub-phases and decision points.

The initial efforts of the design phase are concerned with arriving at an optimal product architecture. According to Mikkola and Gassmann (2003), product architecture may be defined as
"[...] the arrangement of the functional elements of a product into several physical building blocks, including the mapping from functional elements to physical components, and the specification of interfaces among interacting physical components."

[^0]
[^0]:    ${ }^{11}$ Some authors suggest the planning and launch decision to occur prior to the concept generation (Pahl and Beitz, 1996; Roozenburg and Eekels, 1995).
    ${ }^{12}$ Khurana and Rosenthal (1998) provide a review of the success factors related to the project plan in the context of new product development.
    ${ }^{13}$ Bulk of the literature deals with products involving incremental innovations and products with discontinuous (radical) innovations has received less attention (Reid and de Brentani, 2004).The product architecture is established by considering the (physical) arrangement of and interaction between each sub-system, assembly, sub-assembly and components in turn. Functional decomposition and the definition of functional relationships between assemblies, sub-assemblies and, later, components is essential in the establishment of the product architecture, in order to clearly understand the interactions between objects. This understanding is particularly important concerning "modular" products.

Having established the product architecture, the detail design may commence. This is where all properties for each component are defined in detail (e.g., forms, dimensions, tolerances, surface properties, and materials). This is documented in assembly and detail drawings and bill of materials. Further, production documents are produced, as well as the transport and operating instructions.

The design phase involves running many design activities in parallel, and many product characteristics need to be considered simultaneously. Decisions made regarding one product characteristic may have implications for other characteristics, and changes in one component may require changes in other components. Thus, the design phase is strongly iterative. Many different approaches have been proposed in this context. These include the problem solving cycle proposed by Roozenburg and Eekels (1995), and the Design for X approach (see Meerkamm, 1990; Van Hemel and Keldmann, 1996). According to (Blanchard, 2004), Design for X is:
"[...] an integrated approach where design for reliability, maintainability, human factors, safety, supportability, interoperability, availability, life cycle cost, flexibility, transportability, producibilty, quality, disposability, environment, and testability are considered throughout the process."

Sim and Duffy (2003) look at the generic design activities and classify them into three categories:
Design definition activities: These activities involve evolving the product design at an ever increasing level of detail, until all details have been laid down, and the product is ready for production.
Design evaluation activities: These activities encompass analysis, evaluation, and comparison of potential design options, aiming at finding the best solution and potential improvements of the chosen solution.
Design management activities: These activities are concerned with coordinating and managing the design definition and evaluation activities throughout the new product development process.

# Design Reviews 

Several formal design reviews may be carried out. In the early design phases, one or more reviews (the number depends on the product complexity ${ }^{14}$ ) may be required to verify the product architecture. Subsequently, more design reviews may be required to verify critical components. A critical design review is usually conducted to verify the final design, prior to the launch of production or construction.

[^0]
[^0]:    ${ }^{14}$ Blanchard (2004), for example, describes the system design reviews in more detail.# 2.5.3 Development 

The development phase is concerned with both component and product prototype testing. Development is mainly necessary when items involve new technologies, or their application is outside the range used in the past.

Tests are conducted using engineering breadboards, bench test models, service test models, rapid prototyping, and the like. The tests may encompass:

Environmental testing/demonstration: Temperature cycling, shock and vibration, humidity, sand and dust, salt spray, acoustic noise, explosion proofing, and electromagnetic interference.
Reliability testing/demonstration: Sequential testing, life testing, environmental stress screening and reliability growth testing.
Pre-production tests/demonstrations: To verify that the component may be produced and to reveal potential production problems, and ensure that the component produced has the desired performance.

When product prototypes become available, a range of tests may be conducted to predict or verify the product performance. The types of tests conducted are product dependent, and may encompass, in addition to those discussed in the previous section, the following:

Maintainability test/demonstration: Verification of maintenance tasks, task times and sequences, maintenance personnel quantities and skill levels, degree of testability and diagnostic provisions, prime equipment - test equipment interfaces, maintenance procedures and maintenance facilities.
Support equipment compatibility: Verification of the compatibility among the prime equipment, test and support equipment, and so on.
Technical data verification: Verification (and validation) of operating procedures, maintenance procedures and supporting data.
Personnel test and evaluation: Ensure compatibility between the human and the equipment, the personnel quantities and skill levels required, and training needs.
Pre-assembly tests and evaluation: Ensure that the product may be assembled as intended, with the equipment and manning specified.
Field tests: Verify that the product can be used and maintained when the specified operating personnel, operational test and support equipment, operational spares and validated operating and maintenance procedures are used.
Market pre-launch: Test the product on small market segments to verify that it meets customer expectations in the case of standard products.

The development phase serves two purposes. For custom-built products, the purpose is often to verify that the desired performance that was agreed as part of the contractual agreements between customer and manufacturer are met. If the actual (predicted performance) falls below the desired performance, the development process involves understanding of the causes of the problem and then coming up with solutions to fix the problem.# 2.5.4 Production 

Having, throughout the design and development phases, found a solution that meets the desired performance, within given constraints, the challenge of the production and assembly/construction phases is to retain the designed-in performance.

Despite the efforts throughout design and development to ensure optimal production and assembly characteristics, ${ }^{15}$ no production system is able to produce two exactly similar outputs. This may be explained by variations in:

- Input materials
- Production process
- Operator skills
- Other factors such as environment (e.g., temperature, humidity)

There are several strategies to ensure that the product performance of the items produced matches that of the prototype. These include the following:

## Process Control

The process state can be either in-control (so that the effects of assignable causes are under control and very few items produced are non-conforming) or out-of-control (due to the effects of assignable causes and resulting in a larger number of nonconforming items being produced). The effect of assignable causes can be eliminated through proper design of the process (e.g., using Taguchi methods) and is referred to as off-line control. Through regular inspection of the items produced and using control charts, we can detect the change from in-control to out-of-control and this is referred to as on-line control. ${ }^{16}$

## Inspections and Testing

In addition to statistical process control, several inspection and testing methods are aimed at ensuring conformance to the built-in performance of produced items. These include:

Acceptance inspection and testing: Inspection and testing of raw materials, parts and components upon receipt from vendors, at any point in the production process, or after the final production, to decide whether or not to accept the items.
Audit inspections: Periodic random inspections of plant or departmental quality processes and results.

## Custom-built (Specialized) Products

For custom-built products, the demands for conformance may be very high (e.g., satellites, submarines, and nuclear power plants). In these cases, the product is subjected to a series of tests (specified in the contract) prior to being handed over to the customer.

[^0]
[^0]:    ${ }^{15}$ See Boothroyd et al. (2002) for a description of design for manufacture and assembly.
    ${ }^{16}$ See Thompson and Koronacki (2002), Smith (2004), and Oakland (2008) for more on statistical process control.# 2.5.5 Post-production 

For standard products, this phase involves two sub-phases - marketing and product support. For custom-built products, this phase comprises only the latter.

## Marketing

This sub-phase deals with issues such as the logistics of getting the product to the markets, sale price, promotion, warranty, channels of distribution, and so on. The strategies that we formulate for some of these (e.g., price) would need to change over the life cycle and in response to external factors such as competitors' actions, economy, customer response, and so on.

## Price

There are two approaches to pricing. The first is based on the cost of manufacture (which includes development, production, and marketing costs) scaled upwards to ensure the desired profit. The second is based on market demand and supply considerations. For a product new to the market, the sale price is generally high at the start of the life cycle and comes down during the later stages partly due to reduced production costs, but also because new competitors appear in the market.

## Promotion

Depending on the product, the manufacturer can use different media (e.g., television, radio, newspapers, magazines, mail brochures, and leaflets) to promote the product. The duration or size of a particular advertisement and the frequency of repetition have an impact on consumer awareness and their decision making processes. For expensive products, the kind of product support that the manufacturer provides can also serve as a very effective promotional tool as well as for differentiating from competitor's products.

Example 2.4 (Cellular Phone). Any advertising slogan or message has a limited life and manufacturers need to come up with new ones. Sohn and Choi (2001) look at the advertising lifetimes for cellular phones sold in South Korea by five different South Korean manufacturers during 1997-1998. The following data (for LG Telecom 019) is extracted from their Table 1.

| Title of advertisement | Duration of advertisement | Advertisement lifetime (days) | Subscribers during the advertising period | Number of advertisements switching by competitors |
| :--: | :--: | :--: | :--: | :--: |
| The birth | 09/08/97 - 31/08/97 | 23 | 88,136 | 0 |
| Family | 01/09/97 - 26/11/97 | 87 | 218,817 | 6 |
| Cradle song | 27/11/97 - 12/03/98 | 106 | 406,223 | 12 |
| The vivid PCS | 19/01/98 - 25/03/98 | 66 | 361,346 | 4 |
| My father | 13/03/98 - 04/08/98 | 145 | 768,433 | 11 |
| Shining PCS | 11/04/98 - 10/09/98 | 153 | 685,103 | 14 |# Product Support 

When making purchases, customers believe that they are buying more than a physical item. These include maintenance, spare parts, training, upgrades, and so forth. They also have expectation about the level of support service subsequent to the sale of the product and this is called product support.

Product support service refers to the different types of services needed over the useful life of a product (consumer non-durable, commercial or industrial) to ensure satisfactory operation of the product. Product support service can add value to the tangible product in several ways:

- Extending the product life cycle
- Maintenance can give a product further use and postpone replacement
- Direct value in initial sale of product
- Delivery, installation, base and extended warranties add value to the product from the customer perspective

Product support service can include one or more of the following activities:

- Parts, information, training
- Installation
- Maintenance/service contracts
- Warranties, extended warranties, service contracts
- Design modification/customization


### 2.6 A New Model for Product Performance and Specification

Even though many new product development models discuss product performance and specifications, no model addresses this in an effective manner. In this section we propose a new model that is more appropriate for making decisions relating to performance and specification in new product development. It is closely linked to the product life cycle model given in Figure 1.1 and involves three stages and three levels. The three stages are as follows:

Stage I (Pre-development): This stage is concerned with a non-physical (or abstract) conceptualization of the product with increasing level of detail.
Stage II (Development): This stage deals with the physical embodiment of the product through research and development and prototyping.
Stage III (Post-development): This stage is concerned with the remainder of the product life cycle (e.g., production, sale, use) subsequent to the new product development.

The three levels are as follows:
Level I (Business level): This level is concerned with linking the business objectives for a new product to desired product attributes.Level II (System, i.e., product level): This level links product attributes to product characteristics - the product is treated as a black-box.
Level III (Component level): This level is concerned with linking product characteristics to lower level product characteristics, at an increasing level of detail.

The new model has eight phases as shown in Figure 2.4. Some of the phases can involve several sub-phases. The activities in the different phases are as follows:


Figure 2.4. New model for product performance and specification

Phase 1 (Stage-I, Level-I): In this phase the need for a new product is identified and the decisions related to the product attributes (customer's view of the product) are made from an overall strategic management level of a business.

Phase 2 (Stage-I, Level-II): In this phase the product attributes are translated into product characteristics (engineer's view of the product).

Phase 3 (Stage-I, Level-III): In this phase the detail design (proceeding from product to component) of the product is carried out in order to arrive at a set of specifications that will ensure that the product has the required characteristics.

Phase 4 (Stage-II, Level-I): This phase deals with product development, from component to product - and ends up with the product prototype.

Phase 5 (Stage-II, Level-II): In this phase the prototype is released to a limited number of consumers to evaluate the customers' assessment of the product features.Phase 6 (Stage-III, Level-III): This phase deals with the production of products starting from component and ending with the product for release to customers.

Phase 7 (Stage-III, Level-II): This phase looks at field performance of the product taking into account the variability in usage intensity, operating environment, and so on, from the customer perspective.

Phase 8 (Stage-III, Level-I): Here the performance of the product released for sale is evaluated from an overall business perspective.

The link between the phases of the new model and the product life cycle phases in Figure 1.1 is indicated in Figure 2.5.

| Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6 | Phase 7 | Phase 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Pre-development |  |  | Development |  | Post-development |  |  |
| Front-end | Design |  | Development |  | Production | Post-production |  |

Figure 2.5. Comparison of the new model and the product life cycle model in Figure 1.1

The activities in the eight phases are sequentially linked as illustrated in Figure 2.4. Decisions must be made at the end of each phase to either move forward or to iterate back (as shown by dotted lines in Figure 2.4) and this is discussed further in Chapter 3.# Product Performance and Specification 

### 3.1 Introduction

A new product development process starts with a requirement statement, that is, a description of the required product functions and their related performance standards. This involves defining the product performance and constraints. Once this is done, we can derive a set of specifications that form the basis for the production of the product. In Chapter 1 we defined desired and predicted performance and in Chapter 2 we indicated that a product is a complex object that can be decomposed into several levels. As a result, we have a hierarchy of performance and specification and these are interlinked. In this chapter we discuss product performance and specification and their links in general and then focus on reliability performance and specification.

The outline of the chapter is as follows. We start with a discussion of requirements and constraints in Section 3.2. Sections 3.3 and 3.4 look at performance and specification in general and the links between them are discussed in Section 3.5. In Sections 3.6 to 3.8, we look at product performance and specification in stages I through III of the new product development process model proposed in Chapter 2. In Section 3.9, we integrate the discussion of Sections 3.6-3.8 and describe the overall process for decision making regarding performance and specification in new product development.

### 3.2 Requirements, Preferences and Constraints

In this section we discuss several issues that are relevant in order to understand product performance and specification.

### 3.2.1 Requirements

According to the Oxford Dictionary (1989):
Requirement, n. That which is required or needed; a want, need.There are many different kinds of requirements in new product development. Requirements provide the basis for defining the need for a new product and for evaluating alternative options for a new product in the front-end phase. Requirements guide the designers towards correct design options, and provide the basis for verification and selection of potential design options during the design and development phases of the new product development. A guide on how to specify dependability requirements is given in IEC 60300-3-4. Gershenson and Stauffer (1999) suggest the following taxonomy for requirements:

Customer requirements: These requirements express the customers' expectations related to the product attributes (e.g., the fuel consumption of a car engine must be low).
Corporate requirements: These are business related requirements and may be related to all aspects of the product life cycle (e.g., the sales of new engines must exceed a certain figure to achieve the desired returns on investment) of concern to the different groups within the manufacturing firm (engineers, managers, marketers, etc.).
Regulatory requirements: These requirements are related to safety/health, environmental/ecological, disposal and/or political issues, and are often imposed by governmental agencies (e.g., the emission level must meet the new standards). This is further discussed in Chapter 10.
Technical requirements: Technical requirements include engineering principles, material properties and physical laws (e.g., the cylinder material must withstand a certain pressure and temperature). These requirements are usually found in handbooks and manuals.

All these requirements have to be addressed. ${ }^{1}$ Another term that is important in the context of new product development is the following:

Functional requirements: According to Lin and Chen (2002):
"This consists of a function and a requirement. A function states 'to do what' and the requirement is defined by a performance measure imposed either by a preference or a bound."
They define two types of requirement:
Type 1: A performance measure and a related preference
Type 2: A performance measure and a related constraint/bound
We will discuss performance in the next section and look at constraints and preferences in this section.

# 3.2.2 Preferences 

The preferences identify what performance the different stakeholders (e.g., customers, corporate representatives) desire from the product, i.e., what performance the product should have.

[^0]
[^0]:    ${ }^{1}$ Gershenson and Stauffer (1999) use the term "customer requirements" to denote the four requirements stated above.According to Prudhomme et al. (2003), preferences are not sufficient to characterize the needs of different stakeholders in the new product development process. They also use "flexibility" to indicate the degree of willingness to modulate the preferences (desired performance) for a given performance measure. ${ }^{2}$

Preferences are also linked to "prioritizing" the requirements according to the importance to customers and/or the different groups within the manufacturing firm. This is needed for trading different performance measures or assessing the overall "value" of alternative solutions for comparison purposes. ${ }^{3}$

# 3.2.3 Constraints 

A constraint is a bound that restricts the range of a variable. In the new product development process there are various kinds of constraints - financial constraints (ability to raise funds for the new project), resource constraints (manpower available), time constraints (new product must be launched by some specified date) to name a few.

In the context of product design, Suh (2001) defines a constraint as a bound on either (1) a single external or internal product property, or (2) the relationship between two or more product properties and identifies two types of constraints: (i) input constraints that are identified at the onset of the new product development process, (e.g., constraints on size, weight, materials, cost) and (ii) system constraints that arise as the development progresses (e.g., the choice of a particular electronic part in one sub-system may impose constraints on the temperature generation in another part of the system).

Note that a preference may appear as a constraint in subsequent phases (e.g., the choice of a particular sub-system may subsequently result in spatial constraints).

### 3.3 Product Performance

### 3.3.1 Concept and Notions

According to the Oxford Dictionary (1989):
Performance, n. The accomplishment, execution, carrying out, working out of anything ordered or undertaken; the doing of any action or work; working, action (personal or mechanical); spec. the capabilities of a machine or device, now esp. those of a motor vehicle or aircraft measured under test and expressed in a specification. Also used attrib. to designate a motor vehicle with very good performance.

A number of different definitions of performance can be found in the technical literature as illustrated by the following sample:

[^0]
[^0]:    ${ }^{2}$ This is similar to differentiating between "demands" and "wishes," in much of the engineering design literature (see Roozenburg and Eekels, 1995).
    ${ }^{3}$ See Blanchard (2004) for further discussion.- "Performance is the measure of function and behaviour - how well the device does what it is designed to do" (Ullman, 2003)
- "How well a product implements its intended functions. Typical product performance characteristics are speed, efficiency, life, accuracy, and noise" (Ulrich and Eppinger, 1995)
- "Product performance is described as the response of a product to external actions in its working environment. The performance of a product is realized through the performance of its constituent components" (Zeng and Gu, 1999)

As can be seen, these definitions imply that product performance is a measure of the functional aspects of the product. When talking about product performance, we must also bring in properties like form, durability, and price. As defined in Chapter 1, product performance is a vector of variables, where each variable is a measurable property of the product or its elements. The performance variables are concerned with both internal and external properties. ${ }^{4}$ The performance variables can be: ${ }^{5}$

- Functional properties (e.g., power, throughput, fuel consumption)
- Reliability properties (defined in terms of failure frequency, mean time to failure, survival probability, etc.)
- Business properties (e.g., profit, return on investment)

The performance of a product depends on several factors. These include usage mode, usage intensity, usage environment, skills of the operator involved, and so on.

# 3.3.2 Types of Performance 

In the context of new product development, we can define three different types of performance.

## Desired Performance (DP)

From a consumer perspective, the desired performance is what the consumer expects from the product. For individual consumers, the desired performance is linked to consumer benefits, pleasure, and satisfaction. In the case of a car, the desired performance can be stated in terms of a maximum level for environmental pollution, minimum level for ride characteristics, and so on. If the consumer is a business, then the desired performance is linked to the business objectives. For example, in the case of an airline operator, the desired performance for a jet engine might be that its fuel efficiency is above some specified value, that is again linked to operating cost.

From a manufacturer perspective, desired performance forms the basis for new product development. The initial desired performance is established in the front-end

[^0]
[^0]:    ${ }^{4}$ As indicated in Section 2.2.2, a product can be decomposed into several levels starting from sub-system level down to component level. We can define performance at each level and Zeng and Gu (1999) state that the performance of a product is realized through the performance of its constituent components.
    ${ }^{5}$ Form (e.g., dimensions, shape, weight) can be viewed as a performance variable in some situations.phase. Establishing the desired performance involves trade-offs between the desired performance and the following interacting factors (Zeng and Gu, 1999):

- Programme expense: Costs incurred in developing the product
- Development speed: Time from concept to launch/operation
- Production cost: The cost of manufacturing/constructing the product
- Economic performance: Revenue generated, and post-sale servicing expenses over the product life cycle

The desired performance that is arrived at will have direct implications for all four factors. However, as mentioned earlier, the desired performance is influenced by the following factors:

- Customer demands
- Technical feasibility
- Performance of earlier products
- Competitors' actions and competitive pressure
- Business economy
- Laws, standards, and directives


# Predicted Performance (PP) 

Predicted performance may be defined as "an estimate of an object's performance, obtained through analysis, simulation, testing, and so on." During the design phase, the manufacturer has to predict the performance of an object based on technical data from handbooks and catalogues. ${ }^{6}$ During the development phase, the data obtained from limited testing forms the basis for predicting the performance of an object. Predicted performance of an object plays an important role in the decision making process, as will be discussed later in the chapter.

The following factors influence the predicted performance (in levels II and III of stage I; see Figure 2.4): (1) choice of design properties, (2) choice of models used for prediction, and (3) the quality of the data used in the prediction.

As physical testing starts at levels III and II of stage II, additional factors that influence the predicted (or estimated) performance (component level through product level) include: (1) test environment (normal versus accelerated testing, environmental testing), (2) test duration, and (3) methods used to analyse the test data.

## Actual Performance (AP)

The actual performance of the product in the field is dependent on several manufacturing factors, such as quality control, production process capability, materials used, and quality of components supplied by vendors. The performance is also influenced by several customer related factors, such as usage intensity, usage environment, and maintenance of the product. Even storage and transport can, in some instances, influence product performance in the field. Therefore, the actual performance will vary from item to item as no two items will have exactly the same actual performance.

[^0]
[^0]:    ${ }^{6}$ An object can represent either the product, or some sub-system, assembly, module or component of it.# 3.4 Product Specification 

According to the Oxford Dictionary (1989):
Specifications, n. A detailed description of the particulars of some projected work in building, engineering, or the like, giving the dimensions, materials, quantities, etc., of the work, together with directions to be followed by the builder or constructor; the document containing this.

Many different definitions of specification can be found in the technical literature as illustrated by the following sample:

- "A document stating requirements" (ISO 9000)
- "A specification is a means of communicating in writing the requirements or intentions of one party to another in relation to a product, service, a procedure or test. A specification may be written by the product supplier, the user, the designer, the constructor or by the manufacturer. [...] A specification may define general characteristics or it may be specific. [...] A specification consists of two parts, the first defines requirements, and the second defines the means by which compliance with requirements can be demonstrated." (BS 5760-4)
- "A specification (singular) consists of a metric and a value. The product specifications (plural) are simply the set of the individual specifications." (Ulrich and Eppinger, 1995)
- "The technical requirements for the system and its elements are documented through a series of specifications [...] top level specification leads into one or more subordinate specifications [...], covering applicable subsystems, configuration items, equipment, software, and other components of the system." (Blanchard and Fabrycky, 1998)
- "A specification is usually a document that prescribes, in a complete, precise, and verifiable manner, the requirements, constraints, expected behaviour, or other characteristics of a product or system." (Kohoutek, 1996)
- "The Product Design Specification (PDS) is a detailed listing of the requirements to be met to produce a successful product or process. The specification should say what the product must do, not what it must be. Whenever possible the specification should be in quantitative terms, and when appropriate it should give limits within acceptable performance lies." (Dieter, 1991)
- "In a design process, design requirements are represented by design specifications. Based on the specifications, candidate product descriptions are generated. Design specifications are the formulation of design requirements, which manifest themselves as a set of desired product descriptions or product performances." (Zeng and Gu, 1999)

As can be seen, the scope and focus of these definitions vary considerably. However, what they have in common is that a specification can be viewed as a means of stating the characteristics of a product at some stage in a development process. The Oxford Dictionary (1989) defines a specification as a document describing a process in detail, subsequent to development of the process. Others, like Dieter (1991), viewthe specification as a document that states the desired characteristics of a product or process prior to its development, a view shared by Zeng and Gu (1999). On the other hand, Ulrich and Eppinger (1995) and Blanchard (2004) define the specification as a document initially serving as input to the design process, but being refined as the design proceeds through different design phases. The initial specification of Blanchard (2004) is the system specification, and the final is the product, process and materials specification.

We define the specification of an object (product or system, sub-system, and down to part level) as:

A set of statements about an object derived during the pre-development stage to achieve some desired performance.

The specifications for the three phases of stage I (pre-development stage) are different and there is a close link between performance and specification at each phase.

Note. In this book we use the terms performance and specification in singular form. The performance and the specification will, however, generally consist of a long list of statements.

# 3.5 Performance and Specification Relationships 

There are two kinds of relationships between performance and specification as indicated in Figure 3.1.


Figure 3.1. Two relationships linking performance and specification

Forward Relationship (Desired Performance to Specification): The desired performance outlines what is to be achieved in the new product development process. The specification describes how this performance can be achieved (using a synthesis process involving evaluation of alternative solutions to select the best solution), with the desired performance as input to the process. Thus, the specification becomes a function of the desired performance. Often there are severalalternative solutions yielding the same desired performance. This results in several specifications (defining alternative solutions) so that the forward relationship is one-to-many. This relationship plays an important role in stage I.
Backward Relationship (Specification to Actual Performance): The predicted performance (of a product to be built to a stated specification) or the actual performance (of prototype or products released for sale), will, in general, differ from the desired performance used in the formulation of the specification. The predicted or actual performance can be viewed as a function of the specification. Note that this is a one-to-one relationship since a given specification leads to a unique actual performance of the product. This relationship plays an important role in stages II and III.

Note. The actual performance is affected by several uncertain factors beyond the control of the manufacturer. In this case, we need to define performance in a statistical sense so that the expected (or average) actual performance is related to the specification through a one-to-one relationship.

# 3.6 Performance and Specification in Stage I 

Stage I involves three levels and we need to deal with performance and specification at each level. These are linked as indicated in Figure 3.2. In this section we discuss each level separately.


Figure 3.2. Performance and specification in stage I

### 3.6.1 Phase 1

The starting point of phase 1 (stage I, level I in Figure 2.4) is the recognition of a need (e.g., lower warranty costs, reverse declining sales) or opportunity (advances in technology, new market) for a new product as discussed in Section 2.5. The generation and screening of ideas, and understanding the customer requirements (often referred to as "requirements capture"7) are important for defining the desired performance DP-I in phase 1.

[^0]
[^0]:    ${ }^{7}$ See Cooper et al. (1998) for a model of the requirements capture process.DP-I: The desired performance of the new product is defined from an overall business perspective. The performance of the product is viewed in terms of business objectives and business strategy and is defined through a number of elements, such as, market share, sales, revenue, return on investment, customer satisfaction, and so on, that define the overall business performance.
SP-I: The specification defines the product attributes (e.g., various functional features, such as speed of CPU, size of memory, and weight in the case of a notebook computer), product support (e.g., warranty, technical support) and other variables (e.g., customer satisfaction, reputation), and so on. As indicated earlier, there can be several SP-Is that can achieve the DP-I. Generating the different SP-Is is linked closely to idea and concept generation.
PP-I: Not all SP-Is will achieve the defined DP-I. We need to use models to determine whether or not an SP-I will achieve the desired DP-I. The model output is the predicted performance PP-I for a given SP-I. This needs to be compared with the defined DP-I to evaluate whether or not the SP-I under consideration will result in the DP-I being achieved. As a result, deriving SP-I is an iterative process that requires iterating back if the evaluation indicates a mismatch between DP-I and PP-I. If not, we move to phase 2 (level II). This process is shown schematically in Figure 3.3.


Figure 3.3. Iterative process for deriving SP

If no SP-I results in a match between PP-I and DP-I, then we either need to revise the DP-I or terminate the project. In the traditional new product development literature this evaluation is the main activity in the front-end phase and has received a lot of attention. The front-end activity is completed when a business either commits to the funding and launch of an new product development project, or decides not to do this. ${ }^{8}$

[^0]
[^0]:    ${ }^{8}$ Khurana and Rosenthal (1998) provide an extensive bibliography concerning the front-end of new product development.# Constraints 

There are many different types of constraints that need to be taken into account when making decisions regarding DP-I and SP-I. Some of these are financial (e.g., limit on the funds available), resource (e.g., limits on technical and marketing manpower), technology (e.g., limits with respect to capabilities), and so on.

### 3.6.2 Phase 2

If the decision at the end of phase 1 is "proceed forward", then SP-I is communicated to the design team involved with phases 2 and 3 (levels II and III of stage I). The objective of phase 2 is to link product attributes to product characteristics that form the basis for designing the product.

DP-II: This is essentially SP-I from phase 1. However, it can include other elements that the design engineer might regard to be relevant in deriving SP-II.
SP-II: This defines the product characteristics. The starting point for the design team is to look at alternative system architectures for the product. Once this is done, we need to identify the relevant characteristics for the design process. The relevant characteristics (defined as technical statements) are scientific and technical in nature (e.g., product reliability to ensure a certain level of customer satisfaction or expected warranty cost to be below a specified value). Note that we may consider several variants of the product (each with different characteristics) to achieve the defined DP-II.
PP-II: A set of technical statements defining an SP-II might not ensure that it achieves the specified DP-II. As in phase 1, we use models to obtain a predicted performance PP-II for an SP-II and then we evaluate SP-II by comparing with DP-II. In other words, deriving SP-II is an iterative process as indicated in Figure 3.3.

## Constraints

In addition to the constraints from phase 1, new technical constraints may arise. These could include, for example, whether the products use existing platforms or not; use of existing technologies or not; in-house versus out-sourcing of design and manufacture, and so on.

### 3.6.3 Phase 3

Phase 3 (stage I, level III) is involved with detail design of the product that will yield the desired product characteristics. A product can be viewed as a system that can be decomposed into many different sub-levels (ranging from sub-system down to component) as indicated in Section 2.2.3.# Functional Analysis 

Functional analysis is a useful tool for allocating requirements (desired performance) that can be assigned to "technical" functions as the design evolves. ${ }^{9}$ Function trees and functional block diagrams are frequently used to support the functional analysis.

The hierarchical nature of requirements (desired performance) and design options (specification) in a design process can be described as follows: ${ }^{10}$

- A function $\mathrm{F}_{j}$ at sub-level $j$ (to level III in phase 3) and its related desired performance $\mathrm{DP}_{j}$ is attainable by a design option (solution) $\mathrm{DS}_{j}$ which is defined by specification $\mathrm{SP}_{j}$.
- $\mathrm{DS}_{j}$ is bounded by constraints $\mathrm{C}_{j}$.
- On the next lower hierarchical sub-level $j+1$, the design option $\mathrm{DS}_{j}$ requires $n_{j+1}$ solution specific functions, $\mathrm{F}_{j+1,1}, \mathrm{~F}_{j+1,2}, \ldots, \mathrm{~F}_{j+1, n_{j+1}}$.
- Desired performances $\mathrm{DP}_{j+1,1}, \mathrm{DP}_{j+1,2}, \ldots, \mathrm{DP}_{j+1, n_{j+1}}$ and constraints $\mathrm{C}_{j+1,1}, \mathrm{C}_{j+1,2}, \ldots, \mathrm{C}_{j+1, n_{j+1}}$ are then allocated to these $n_{j+1}$ functions.

As a result, the functions, requirements (desired performance) and solutions (specifications) evolve in a hierarchical manner, as illustrated in Figure 3.4.


Figure 3.4. Hierarchy of functions, requirements, and solutions

Functional analysis is not only valuable for decomposing requirements from product level down to component level through functional decomposition (see Suh, 2001; Blanchard, 2004), but is also useful for:

[^0]
[^0]:    ${ }^{9}$ See Blanchard (2004); Fox (1993); Pahl and Beitz (1996); Pugh (1990); Suh (2001); Ullman (2003).
    ${ }^{10}$ For more details, e.g., see Suh (2001).Modular design: To understand the functional relationships and interactions between components (Mikkola and Gassmann, 2003). Failure to take into account these relationships and interactions may result in tedious and costly trial-anderror iterations towards the end of new product development, even for nonmodular designs.
Value analysis: To establish the "value" of components, and remove those not contributing to value (Miles, 1972).
Design storage and re-use: To store existing designs at different product levels based on function structures for re-use of the design knowledge (Hashim, 1993).

The performance and specification in phase 3 are:
DP-III: This is a collection of the desired performance for different objects at each of the sub-levels. Let DP-III ${ }_{j}$, for $j \geq 1$, denote the desired performance of objects at sub-level $j$. The number of sub-levels needed, and the number of objects at each sub-level depend on the complexity of the product. At the first sub-level (corresponding to the product level) we have DP-III ${ }_{1} \equiv$ SP-II. As we move down the sub-levels, we have DP-III ${ }_{j+1} \equiv$ SP-III $_{j}$, for $j \geq 1$.
SP-III: This is a collection of specifications for different objects at each of the sublevels. At the lowest sub-level, the specification is concerned with issues, such as geometrical shape, dimensions, tolerances, surface properties, and material. The end result is that all individual components and parts are fully specified and laid down in assembly drawings and parts lists. ${ }^{11}$
PP-III: This is a collection of the predicted performance for different objects at each of the sub-levels based on the specification for the object. This is needed to assess whether or not the specification selected will ensure the desired performance, using the iterative process indicated in Figure 3.3.

The models used are based on the various engineering sciences involved.
Note. The constraints get more detailed as we proceed through the different sublevels.

# 3.6.4 Some Comments 

1. The predicted performance (PP-I to PP-III) is obtained using models. Model building involves selecting the structure of the model and assigning numerical values to the parameters of the model. We can use many different types of models, since a model is a simplified (and approximate) representation of the relevant real world. Model building depends on the data and information that is available to the model builder. The data can vary from hard (technical data obtained from handbooks for models in level III) to soft (subjective data for models in level I).
2. The decision to iterate back (see Figure 3.3) depends on the match between DP and PP. In general, these are vectors as DP involves several elements. We need to define the criteria for deciding whether or not there is a match. One criterion
[^0]
[^0]:    ${ }^{11}$ See Pahl and Beitz (1996) for more on this.would be the relative difference in the DP and PP for an element (as a fraction of the value of DP for the element) being less than some specified value. Another criterion would be that an element of PP must be either greater (e.g., efficiency of an engine) or smaller (e.g., noise level of the engine) than the corresponding element of the DP vector.

# 3.7 Performance in Stage II 

Stage II is concerned with the performance of the physical object (component through to the final product) built to the detailed design specification given by SP-III. The building process starts with components and proceeds through various intermediate sub-levels (corresponding to sub-assembly, assembly, module, sub-system, etc.) and ending up with the final product. Since the performance is an estimate based on limited test data it is a predicted performance at levels II and III and this is shown schematically in Figure 3.5.


Figure 3.5. Performance in stage II

### 3.7.1 Phase 4

PP-III: The predicted performance in phase 4 (stage II, level III) is a set of the performance of objects (component through to product) involving test data as indicated in Figure 3.6.

If the desired performance of a component does not match that of an existing component, we need to carry out research and development to improve the performance. Similarly, if the predicted performance of an object (at an intermediate level) does not match the desired performance of the object, we need to carry out research and development involving a sequence of test-fix-test cycles. If the outcome of the research and development process is a success, we can move forward. If not, we need to iterate back.

At the end of the process, we have the predicted performance of the final product (or prototype) which gives an estimate of the product characteristics. If this matches the desired product characteristics $\left(\mathrm{DP}-\mathrm{III}_{1}\right)$, it is released for field testing.

Figure 3.6. Evaluating PP-III in stage II

# 3.7.2 Phase 5 

PP-II: In phase 5 (stage II, level II) the prototype is released to a small set of customers so that the performance of the product from the customer perspective can be assessed. Since the testing is limited, the inferences drawn yield a predicted value and hence we have the predicted performance PP-II. If this does not match the desired performance DP-II, then we iterate back. On the other hand, if there is a match, the specification SP-III is released for production of the product.

## Comments

1. PP-II and PP-III in stage II are different from those in stage I. In stage I they are based on models using all the historical data available during design. In contrast, in level II they are based on the data generated by the tests carried out.
2. There are various forms of uncertainties that affect the outcome of the test as well as the data collection. As a result, the performance estimates based on the data can be either point estimates or interval estimates. This implies that in the evaluation process we can use either point or interval estimates.

### 3.8 Performance in Stage III

Stage III is concerned with the performance of the product produced (based on SPIII) in numbers that can vary from small (e.g., a few hundred in the case of airplanes)to large (e.g., several million in the case of cellular phones). ${ }^{12}$ The performance in this stage is indicated in Figure 3.7.


Figure 3.7. Performance in stage III

# 3.8.1 Phase 6 

Phase 6 (stage III, level III) is about manufacturing of the product. Until the component production and assembly processes are fine-tuned, the performance of items will, in general, be lower than the performance of the prototype built in stage II. The production process is adjusted so that the performance matches the desired performance and this is referred to as process stabilization. Once this is achieved, full-scale manufacturing commences, and the product is launched to the market.

AP-III: This is the actual performance of the product released to customers, that is, in the field. It has the same elements as DP-III so that it corresponds to technical characteristics from component through to product.

### 3.8.2 Phase 7

In phase 7 (stage III, level II) the focus is on customer evaluation of the product performance in terms of product attributes that formed the basis for the initial purchase.

AP-II: This is the actual performance of the product viewed from the customer perspective. The performance is assessed using data from the field (e.g., warranty claims data, sale of spares for items no longer covered under warranty, customer complaints).

The assessment of the performance needs to be done with care taking into account the heterogeneity of consumers in terms of usage intensity, operating environment, due care, maintenance, and other factors. If the actual performance deviates from DP-II, we need to do root cause analysis to find out the cause. The most common cause is the variability in the components obtained from vendors and/or in the production process. Through effective quality control, we can ensure a reasonable match between AP-II and DP-II.

[^0]
[^0]:    12 This stage is not relevant when only a single custom-built item is produced.# 3.8.3 Phase 8 

Phase 8 (stage III, level I) is the final phase of the new product development model. Here we look at the product performance from the business perspective.

AP-I: This is based on the data (e.g., sales, warranty costs, return of investment) that is collected and analysed on a periodic basis (monthly, quarterly or yearly). This is compared with DP-I and if there is mismatch, we need to iterate back to phase 1 (stage I, level I) for appropriate actions.

### 3.9 Overall Process

The overall process for decision making with regard to product performance and specification is shown in Figure 3.8.


Figure 3.8. Overall process# 3.10 Reliability Performance and Specification 

Reliability performance and specification are a sub-set of the product performance and specification. They require concepts from reliability theory and these are discussed in Chapter 4. The remaining chapters deal with reliability performance and specification in more detail.# An Introduction to Reliability Theory 

### 4.1 Introduction

The study of reliability specification and performance requires a thorough understanding of many different concepts from reliability theory. Reliability theory deals with the interdisciplinary use of probability, statistics, and stochastic modelling, combined with engineering insights into the design and the scientific understanding of the failure mechanisms, to study the various aspects of reliability. It encompasses issues such as:

- Reliability modelling
- Reliability analysis and optimization
- Reliability engineering
- Reliability science
- Reliability technology
- Reliability management

In this chapter we briefly discuss these concepts that will be used in later chapters of the book. For readers who are familiar with reliability theory this chapter serves as a review chapter. For readers who are not familiar with reliability theory, we indicate references where they can get more details of the topic under consideration. The two references that are cited often are Blischke and Murthy (2000) and Rausand and Høyland (2004). Other references are indicated as and when appropriate.

The outline of the chapter is as follows: Section 4.1 defines basic concepts of reliability, like functions, failures, and failure modes and effects. Section 4.2 introduces reliability measures and lifetime models with focus on the exponential and Weibull models. System modelling by means of reliability block diagrams and fault tree analysis is outlined. How to incorporate environmental effects into life models, for example, by using proportional hazards models is also briefly discussed. Section 4.5 deals with modelling of repairable systems with both corrective and preventive maintenance strategies. Qualitative and quantitative reliability analyses are presented in Section 4.6 and reliability engineering issues are discussed in Section 4.7 with a special focus on reliability allocation and reliability growth. Sections 4.8 and 4.9present a brief introduction to reliability prediction and to reliability management issues. The chapter concludes in Section 4.10 with a case study on cellular phones.

In the rest of this chapter we will use the term item to denote any physical entity, be it a large system or a small component.

# 4.2 Basic Concepts 

In Section 1.3.1 we presented the definition of reliability from IEC 60050-191. The concept of reliability is related to one or more product functions that are required or wanted. Some functions are very important, while others may be of the category "nice to have". When we use the term reliability, we should always specify the required functions. The reliability of a product is dependent on the environmental and operational conditions during the product's post-production phase. These conditions have to be properly understood and assessed in order to develop a reliable product.

### 4.2.1 Product Functions

The key term in the definition of reliability is the ability of the item to perform a required function. The different functions of a complex item may be classified as follows (Rausand and Høyland, 2004).

Essential functions: These functions are the intended or primary functions, and may be considered as the reason why the item has been developed. The essential function of a pump is, for example, to pump fluid.
Auxiliary functions: These functions are required to support the essential function. An auxiliary function of a pump is, for example, to contain the fluid and prevent leakage to the environment.
Protective functions: These functions are intended to protect people, material assets, and the environment from damage, negative health effects, and injury.
Information functions: These functions give information from condition monitoring gauges, alarms, and so on.
Interface functions: These functions are related to the interfaces between the item considered and other items.
Superfluous functions: In some cases an item may have functions that are never used. This is sometimes the case with electronic equipment that has a wide range of "nice-to-have" functions that are often not necessary. In some cases, failure of a superfluous function may cause failure of a required function.

### 4.2.2 Failure and Related Concepts

## Failure

A failure occurs when the item is not able to perform one or more of its required functions. Two definitions of failure are:1. The termination of the ability of an item to perform a required function (IEC 60050-191).
2. Equipment fails if it is no longer able to carry out its intended function under the specified operational conditions for which it was designed (Nieuwhof, 1984).

Failures are events that occur in a random manner and are influenced by factors such as design, manufacture or construction, maintenance, and operation.

# Fault 

A fault is the state of the item characterized by its inability to perform its required functions. ${ }^{1}$ A fault is hence a state resulting from a failure.

## Failure Mode

A failure mode is a description of a fault, that is, how we can observe the fault. A failure mode is observed as a deviation from the accepted performance of a function.

Example 4.1. Consider a pump that is required to pump between 100 and 110 litres of water per minute. As long as the pumping rate is kept within these limits, its performance is acceptable. A failure occurs as soon as the output deviates from the acceptable performance. Relevant failure modes of the pump are therefore: (i) No output, (ii) too low pumping rate, i.e., $<100$ litres per minute, and (iii) too high pumping rate, i.e., $>110$ litres per minute.

## Failure Cause

Failure cause is the circumstances during design, manufacture or use which have led to a failure (IEC 60050-191).

Knowledge about failure causes is useful information in order to prevent failures or their recurrence. A classification scheme for failure causes is as follows:

- Design Failure: Due to inadequate design.
- Weakness failure: Due to weakness (inherent or induced) in the system so that the system cannot withstand the stress it encounters in its normal environment.
- Manufacturing failure: Due to non-conformity during manufacturing.
- Aging failure: Due to the effects of age and/or usage.
- Misuse failure: Due to incorrect handling and/or lack of care and maintenance, or due to operating in environments and for purposes for which it was not designed.


## Failure Mechanisms

The physical, chemical or other processes that may lead to a failure (IEC 60050-191). Failure mechanisms are important failure causes.

[^0]
[^0]:    ${ }^{1}$ Note that this excludes situations arising from preventive maintenance or any other intended shutdown during which the system is unable to perform its required function(s).# Failure Classification 

Blache and Shrivastava (1994) suggested the following classification scheme for failure modes:

- Intermittent failures: Failures that last only for a short time.
- Extended failures: Failures that continue until some corrective action rectifies the failure. They can be divided into the following two categories:
- Complete failures that result in total loss of function.
- Partial failures that result in partial loss of function.

Each of these can be further sub-divided into the following:

- Sudden failures: Failures that occur in a very short time and often with limited or no warning.
- Gradual failures: Failures that occur with signals to warn of the occurrence of a failure if properly monitored.

A complete and sudden failure is called a catastrophic failure and a gradual and partial failure is designated a degraded failure.

The failure modes may also be classified according to their failure causes:
Primary failure: A primary failure is a failure caused by natural aging. The failure occurs under stresses and conditions foreseen during the design process. Primary failures can only be prevented by redesigning the physical item.
Secondary failure: A secondary failure is a failure caused by overstress, i.e., stress levels outside the design envelope of the item. These overstresses were not foreseen during design or may be due to deliberate misuse of the item. A secondary failure is also called an overstress failure. To prevent an overstress failure we need to reduce the possibility of excessive stresses (e.g., through better information to users) and/or to make the item more robust to overstress.
Command fault: A command fault is a failure caused by an improper control signal or noise. A command fault does not represent a physical failure of the item. The item is not able to perform a required function because of an erroneous or lacking input signal. When the signal is corrected, the item will be functioning again. A command fault is therefore usually an intermittent failure.

In some applications, it may be useful to classify failures into the two following types (e.g., see IEC 61508):

Random (hardware) failures: A random hardware failure is a failure, occurring at a random time, which results from one or more of the possible degradation mechanisms in the hardware.
Systematic failures: Systematic failures are due to errors in hardware or software, which under some particular combination of inputs or environmental conditions, will permit a failure. Corrective maintenance without modification will usually not eliminate the cause of a systematic failure.

Example 4.2 (Safety Instrumented System). A gas detector in a safety instrumented system that is not able to detect gas because an efficient ventilation system preventsthe gas from reaching the gas detector, has a systematic failure. The same applies to a flame detector that is not able to "see" a flame because the flame is hidden behind some temporary scaffolding.

# Common Cause Failures 

A common cause failure is a multiple component failure that occurs due to a common cause. Common cause failures may be classified in two main types:

1. Multiple failures that occur at the same time due to a common cause (e.g., an external shock)
2. Multiple failures that occur due to a common cause, but not necessarily at the same time

The common cause for type 2 may, for example, be higher than normal temperatures, humidity or vibrations. The time between the failures may in some cases be rather long.

Common cause failures are especially important for redundant components, for example, for multiple input elements in a safety instrumented system.

## Consequences of Failures

When a failure occurs, no matter how benign, its impact is felt. Many different classifications have been proposed to indicate the severity of item failure. The following classification is adapted from Dhudshia (1992):

Level 5: Failure will result in major customer dissatisfaction and cause non-operation of the item or non-compliance with governmental regulations.
Level 4: Failure will result in high degree of customer dissatisfaction and cause non-functionality of the item.
Level 3: Failure will result in customer dissatisfaction and annoyance and/or deterioration of part or item performance.
Level 2: Failure will result in slight customer annoyance and/or slight deterioration of part or item performance.
Level 1: Failure is of such minor nature that the customer (internal or external) is probably unable to detect the failure.

A classification scheme that is often used in applications involving health, safety, and environment (HSE) aspects is the following:

Catastrophic: Failure that results in major injury or death of personnel.
Critical: Failure that results in minor injury to personnel, personnel exposure to harmful chemicals or radiation, or release of chemicals into the environment.
Major: Failure that results in a low level exposure to personnel, or activates a plant alarm system (for items used in such plants).
Minor: Failure that results in minor damage but does not cause injury to personnel, allow any kind of exposure to operational or service personnel or allow any release of chemicals into the environment.# 4.2.3 Different Notions of Product Reliability 

There are several different notions of reliability as indicated in Figure 4.1.


Figure 4.1. Different notions of product reliability

## Design Reliability

The design reliability of a product is the predicted reliability performance of the product at the end of the design and development phase. The prediction may be based on field experience from similar products or parts thereof, testing of the product, expert judgement, and various types of analysis and testing. The prediction is based on nominal environmental and operational conditions used during the design process.

## Inherent Reliability

The reliability of the products produced will tend to differ from the design reliability due to quality variations. The variations result from some of the components not conforming to the design specification and/or assembly errors. The reliability of produced items is often referred to as the inherent reliability.

## Field Reliability

The reliability at sale depends on the inherent reliability and the effects of transportation and storage, as they can degrade the reliability. The field reliability is the reliability of the product subsequent to the sale of the product. The field reliability is calculated based on recorded failures and malfunctions. For some products, like cars, failure data are collected and analysed by various organizations and the field reliability is made public in special journals and on the Internet. The field reliability is also called the actual reliability and is the same as our concept actual (reliability) performance.

Very often, the field reliability of a product differs from the design reliability due to environmental and operational conditions varying from customer to customer and differing from the nominal values used in the design process. It also depends on the maintenance actions carried out by the customers during the use of the product.# 4.3 Reliability Science 

Failure of an item is often a result of deterioration of some characteristics (such as strength). The rate at which the deterioration occurs is a function of time and/or usage intensity. The deterioration process is often a complicated process and varies with the type of item and the materials used. Reliability science is concerned with the properties of materials and the causes of deterioration leading to item failures. It also deals with the effect of manufacturing processes (e.g., casting, annealing) on the reliability of the part or component produced.

### 4.4 Reliability Modelling - I

Reliability modelling deals with model building to obtain solutions to problems in predicting, estimating, and optimizing the survival or performance of an unreliable system, the impact of the unreliability, and actions to mitigate this impact. As such, reliability modelling plays a very important role in reliability performance and specification in new product development.

The modelling of the first failure is different from the modelling of the subsequent failures. This is because the modelling of subsequent failures depends on the corrective maintenance actions taken to restore a failed item into operational state.

In this section we focus on the modelling of the first failure at component and system levels.

### 4.4.1 Reliability Modelling of Single Items

The time to the first failure of a single item (a component or a system) is often modelled by considering only two possible states of the item; a working state and a failed state. When the item is put into operation, it is in working state and when failure occurs, the state changes from working to failed state. The time for which the item is in working state is the time to the first failure, $T$. Since failures occur in a random manner, $T$ is a random variable. The distribution of $T$ may be selected in different ways:

- Based on recorded field data from the same type of items without considering the failure mechanisms involved. This is sometimes referred to as "empirical or data-driven modelling" and is also called a black-box approach.
- Based on a careful consideration of the underlying causes and mechanisms that may lead to item failure, and modelling of the degradation of the item as a function of time. The time to the first failure, $T$, is the time until the degradation passes a specified threshold value. This is referred to as physical modelling and is also called a white-box approach.

In many applications, a combination of these two approaches is used, and may also be combined with expert judgement.# Failure Distribution and Failure Rate Function 

Let $T$ denote the time from when the item is put into operation until the first failure. $T$ is a non-negative random variable that can assume any value in the interval $[0, \infty)$. As such, $T$ can be modelled by an absolutely continuous failure distribution function. The failure distribution function $F(t ; \theta)$ is given by

$$
F(t ; \theta)=\operatorname{Pr}(T \leq t) \quad \text { for } t>0
$$

where $\theta$ is the parameter set of the distribution function. ${ }^{2}$ We note that $F(t)[=$ $F(t ; \theta)]$ is the probability that the first failure will occur in the time interval $(0, t]$.

The probability density function associated with the distribution function $F(t)$ (if $F(t)$ is differentiable) is given by

$$
f(t)=\frac{d F(t)}{d t} \quad \text { for } t>0
$$

The probability density function $f(t)$ can also be expressed by the approximation

$$
\operatorname{Pr}(t<T \leq t+\Delta t) \approx f(t) \cdot \Delta t
$$

when $\Delta t$ is "small". This equation indicates why $f(t)$ is called a density function.
The survivor function, $R(t)$ is given by

$$
R(t)=\operatorname{Pr}(T>t)=1-F(t) \quad \text { for } t>0
$$

and denotes the probability that the item will survive the time interval $(0, t]$, that is, the probability that the item will not fail before it reaches the age $t . R(t)$ is also called the reliability of the item and is sometimes denoted $\bar{F}(t)$.

The conditional probability that the item will fail in the interval $(t, t+\Delta t]$ given that it has not failed prior to time $t$, is given by

$$
\operatorname{Pr}(t<T \leq t+\Delta t \mid T>t)=\frac{F(t+\Delta t)-F(t)}{1-F(t)} \quad \text { for } t>0
$$

The failure rate function, $z(t)$, associated with $F(t)$ is defined as ${ }^{3}$

$$
z(t)=\lim _{\Delta t \rightarrow \infty} \frac{\operatorname{Pr}(t<T \leq t+\Delta t \mid T>t)}{\Delta t}=\frac{f(t)}{1-F(t)}=\frac{f(t)}{R(t)}
$$

Similar to (4.3) the failure rate function can be expressed by the approximation

$$
\operatorname{Pr}(t<T \leq t+\Delta t \mid T>t) \approx z(t) \cdot \Delta t
$$

[^0]
[^0]:    ${ }^{2}$ Often we will suppress the parameter $\theta$ for notational ease and write $F(t)$ instead of $F(t ; \theta)$.
    ${ }^{3}$ A variety of symbols are used in the literature to denote the failure rate function. Among these are $h(t), r(t)$, and $\lambda(t)$.when $\Delta t$ is "small." The expression $z(t) \cdot \Delta t$ denotes the probability that the item will fail in $(t, t+\Delta t]$ when we know that it has not failed prior to $t$. In other words, it characterizes the effect of age on item failure more explicitly than $F(t)$ or $f(t)$. The failure rate function $z(t)$ is also called the hazard rate function or the force of mortality (FOM) to explain that the failure rate indicates the "proneness to failure" of the item after it has reached an age $t$.

The cumulative failure rate function is

$$
Z(t)=\int_{0}^{t} z(u) d u
$$

and it is seen from Equation (4.6) that

$$
R(t)=e^{-\int_{0}^{t} z(u) d u}=e^{-Z(t)}
$$

The mean time to the first failure is given by

$$
\mathrm{MTTF}=\int_{0}^{\infty} t f(t) d t=\int_{0}^{\infty} R(t) d t
$$

Many different types of distributions have been proposed for modelling component failures. Among these are the exponential distribution and the Weibull distribution.

# Exponential Distribution 

Consider an item that is put into operation at time $t=0$. If the time to failure, $T$, has the probability density function

$$
f(t)=\lambda e^{-\lambda t} \quad \text { for } t>0
$$

then $T$ is said to have an exponential life distribution, and we sometimes write $T \sim$ $\exp (\lambda)$. The exponential distribution is the most used - and misused - distribution in the field of reliability. This is mainly due to its mathematical simplicity.

The survivor function is

$$
R(t)=\operatorname{Pr}(T>t)=\int_{t}^{\infty} f(u) d u=e^{-\lambda t} \quad \text { for } t>0
$$

The conditional survivor function at age $x$ is

$$
\begin{aligned}
R(t \mid x) & =\operatorname{Pr}(T>t+x \mid T>x) \\
& =\frac{\operatorname{Pr}(T>t+x)}{\operatorname{Pr}(T>x)}=\frac{e^{-\lambda(t+x)}}{e^{-\lambda x}}=e^{-\lambda t} \quad \text { for } t>0
\end{aligned}
$$

This means that that the probability of surviving a time interval of length $t$ is the same for a used item of age $x$, as it is for a new item. An item with this property is "as good as new" as long as it is functioning. Failures will be pure chance failures and will not depend on the age of the item.The corresponding failure rate function is

$$
z(t)=\frac{f(t)}{R(t)}=\lambda \quad \text { for } t>0
$$

The mean time to failure is

$$
\mathrm{MTTF}=\int_{0}^{\infty} R(t) d t=\int_{0}^{\infty} e^{-\lambda t} d t=\frac{1}{\lambda}
$$

The exponential distribution is often used as a life distribution for electronic components and for high reliability components that are regularly tested and maintained.

# Weibull Distribution 

Another well-known distribution is the two-parameter Weibull distribution given by

$$
F(t)=1-\exp \left(-\left(\frac{t}{\alpha}\right)^{\beta}\right) \text { for } t>0
$$

where $\alpha>0$ and $\beta>0$. The parameter $\alpha$ is called the scale parameter and $\beta$ is called the shape parameter. The parameter $\alpha$ is also called the characteristic life of the item. The probability that an item survives its characteristic life, is from (4.16) seen to be $R(\alpha)=\exp (-1) \approx 0.3679$ for all values of the shape parameter $\beta$.

The probability density function is

$$
f(t)=\frac{\beta}{\alpha^{\beta}} t^{\beta-1} \exp \left(-\left(\frac{t}{\alpha}\right)^{\beta}\right) \quad \text { for } t>0
$$

and the failure rate function is given by

$$
z(t)=\frac{\beta}{\alpha^{\beta}} t^{\beta-1} \quad \text { for } t>0
$$

The failure rate function is seen to be increasing when $\beta>1$, constant when $\beta=1$, and decreasing when $\beta<1$. The mean time to failure is

$$
\mathrm{MTTF}=\alpha \cdot \Gamma\left(\frac{1}{\beta}+1\right)
$$

where $\Gamma(\cdot)$ denotes the Gamma function (Rausand and Høyland, 2004).
The shape of the failure rate function changes significantly as the shape parameter $\beta$ varies. As a result, the Weibull distribution may be used to model many failure patterns and it is widely used in practice. The exponential distribution is a special case of the Weibull distribution with shape parameter $\beta=1$ and scale parameter (characteristic life) $\alpha=1 / \lambda$.

Several other failure distributions may be derived from the Weibull distribution; see, for example Blischke and Murthy (2000). There are many other non-Weibull distributions that have been used in reliability modelling. For more on these, see, for example Murthy et al. (2003) and Rausand and Høyland (2004).# Model Selection 

In the black box approach the model selection is based on an analysis of the data available. The data can be failure times of items that have failed (complete data) and the age of items still working (censored data). Often, item failures are grouped into different intervals and the data available are the number of failures in different groups (grouped data). Various data plotting techniques have been developed to assist the model builder. These include both non-parametric (e.g., histograms, Kaplan Meier plots, hazard plots, and total time on test (TTT) plots) and parametric (e.g., empirical Weibull probability plots). For more on these, see Ansell and Phillips (1994); Crowder et al. (1991); Blischke and Murthy (2000); Rausand and Høyland (2004).

## Bathtub and Roller Coaster Failure Rate Function

Sometimes, the empirical plots of the failure rate function indicate that we need to select a failure distribution that has a bathtub shape (see Figure 4.2) or roller coaster shape (see Figure 4.3) for the failure rate function. The roller coaster failure rate function requires more complicated formulations involving two or more distributions.


Figure 4.2. Bathtub failure rate function

## Parameter Estimation

Once a distribution has been selected, we need to assign numerical values to the parameters of the distribution. Many different methods have been proposed and they can be broadly grouped into two categories - graphical and statistical. The graphical approach uses the plots (e.g., Weibull probability plot) to estimate the parameters. In the case of the two-parameter Weibull distribution, the slope and the intercept are used to obtain the parameter estimates. Methods based on the statistical approach include the method of moments, maximum likelihood, Bayesian, and so forth. These can be found in most books on reliability data analysis, for example, Lawless (1982); Ansell and Phillips (1994); Meeker and Escobar (1998).# Model Validation 

If the data available are extensive, we can divide the data into two sets. The first set is used for model selection and parameter estimation. The second set is used for model validation. Many different statistical tests have been developed to see if the data from the second fits the model derived from the first set. For more on this, see Blischke and Murthy (2000); Murthy et al. (2003).


Figure 4.3. Roller coaster failure rate function

### 4.4.2 Physical Modelling

Physical modelling (white-box approach) requires a thorough understanding of the failure causes and mechanisms that may lead to item failure. This knowledge has to be translated into knowledge about the shape of the failure rate function. A lot of research efforts have been devoted into understanding how specific deterioration mechanisms, like corrosion, wear, and fatigue, progress as a function of time, and hence how they influence the failure rate function (Rausand and Høyland, 2004). If we know that an item will be exposed to a dominating failure mechanism, we have a good basis for selecting an appropriate failure distribution.

In some cases, it may be relevant to use stochastic processes to model the gradual degradation of the item and to derive the distribution of the time to first failure by solving a level-crossing problem. For example, in the case of fatigue failures, we may start by modelling the spread of the crack by a suitable stochastic process. If the spread is due to external shocks, then the occurrence of shocks needs to be modelled by a marked point process where the points corresponds to random time instants when shocks occur and the mark (a random variable) denotes the increase in the crack length due to the shock. The time to failure is the first time instant when the crack length exceeds some critical length.

These types of models involve very complex model formulations and are hence not very relevant in the context of reliability specification. As such, these models will not be discussed any further.# Combined Component Level Modelling 

When we develop models for the time to first failure, $T$, of rather new items, the data available are only related to a short life span of the items. The data will typically be strongly censored and only contain some few failures. By using the black-box approach, it is impossible to conclude anything about the reliability of the item after the observed life span. In most cases it is, for example, impossible to distinguish whether the data fit best to a Weibull distribution or to a lognormal distribution. These two distributions have similar failure rate functions in the first part of the life span, but are very different in the last part of the life span (Rausand and Høyland, 2004). To be able to come up with a realistic model, we have to combine the blackbox and the physical approach.

### 4.4.3 System Modelling

System failure is modelled in terms of the failures of the components of the system. Let $n$ denote the number of components in the system. The linking of component failures to system failures can be done in several ways. Two of these are the reliability block diagram and the fault tree analysis.

## Reliability Block Diagram

A reliability block diagram (RBD) is a success-oriented network describing a function of a system. The diagram has one source (a) and one terminal (b) as illustrated in Figure 4.4. Each block in the diagram represents a function of a component. If the function is available, we have connection through the block, and if the function is failed, there is no connection through the block. If we have connection between (a) and (b), this means that the system is functioning. Note that a reliability block diagram only represents a specified function of a system. Two different systems functions will therefore have two different reliability block diagrams.

Example 4.3 (Safety Instrumented System). Consider a simple safety instrumented system comprising three sensors (components 1,2 , and 3 ) that are connected to a single logic solver (component 4) in a 2 -out-of-3 configuration. The logic solver is connected to two actuating items (components 5 and 6) in a 1-out-of-2 configuration. If a process demand occurs, at least two of the three sensors, the logic solver, and at least one of the two actuating items have to function to have a successful function of the safety instrumented system. A reliability block diagram of the safety function of the safety instrumented function is illustrated in Figure 4.4.

As illustrated in Figure 4.4, the same component may appear at several places in a reliability block diagram. It is important to realize that a reliability block diagram is not a physical layout diagram, but a diagram illustrating a specified system function.

Figure 4.4. Reliability block diagram of the safety instrumented system in Example 4.3

# Structure Function 

Let $X_{i}(t)$ denote the state of component $i$ at time $t$, for $i=1,2, \ldots, n$, where

$$
X_{i}(t)= \begin{cases}1 \text { if component } i \text { is in a working state at time } t \\ 0 \text { if component } i \text { is in a failed state at time } t\end{cases}
$$

where "working state" refers to a specified function.
Let $\mathbf{X}(t)=\left(X_{1}(t), X_{2}(t), \ldots, X_{n}(t)\right)$ denote the state of the $n$ components at time $t$. Let $X_{S}(t)$ (binary random variable) denote the state (working or failed) of the system at time $t$. Then, from the reliability block diagram we can derive an expression of the form

$$
X_{S}(t)=\phi(\mathbf{X}(t))
$$

which links the component states to the system state. $\phi(\cdot)$ is called the structure function.

The reliability block diagrams of (i) a series system, (ii) a parallel system, and (iii) a 2-out-of-3 system are illustrated in Figure 4.5. The series system is functioning


Figure 4.5. Reliability block diagrams (i) a series system, (ii) a parallel system, and (iii) a 2-out-of-3 system
if and only if all the components are functioning, i.e., the state of the system $X_{S}(t)$ is 1 , if and only if $X_{i}(t)=1$ for $i=1,2, \ldots, n$. The structure function of a series system is therefore the product of the state variables of the components.$$
\phi(\mathbf{X}(t))=\prod_{i=1}^{n} X_{i}(t) \quad \text { for the series system }
$$

The parallel system is functioning if at least one of its components is functioning, i.e., the system state $X_{S}(t)$ is 0 if and only if $X_{i}(t)=0$ for all $i=1,2, \ldots, n$. The structure function of the parallel system is therefore

$$
\phi(\mathbf{X}(t))=1-\prod_{i=1}^{n}\left[1-X_{i}(t)\right] \quad \text { for the parallel system }
$$

The 2-out-of-3 system is functioning if at least two of the three components are functioning, and can be considered as a parallel system of three series systems as illustrated in Figure 4.5(iii). The structure function is therefore

$$
\phi(\mathbf{X}(t))=1-\left[1-X_{1}(t) X_{2}(t)\right]\left[1-X_{1}(t) X_{3}(t)\right]\left[1-X_{2}(t) X_{3}(t)\right]
$$

Since $X_{i}(t)$ is a binary variable, then $X_{i}(t)^{2}=X_{i}(t)$. By using this property, the structure function of the 2-out-of-3 system can be reduced to:

$$
\phi(\mathbf{X}(t))=X_{1}(t) X_{2}(t)+X_{1}(t) X_{3}(t)+X_{2}(t) X_{3}(t)-2 X_{1}(t) X_{2}(t) X_{3}(t)
$$

# System Reliability 

Let $R_{S}(t)$ denote the reliability of the system and $\mathbf{R}(t)=\left(R_{1}(t), R_{2}(t), \ldots, R_{n}(t)\right)$ denote the reliabilities of the $n$ components. If the component failures are independent, and the structure function has been reduced to an algebraic expression without any powers of $X_{i}(t)$, we get

$$
R_{S}(t)=\phi(\mathbf{R}(t))
$$

so that we have the system reliability in terms of the component reliabilities (Rausand and Høyland, 2004).

The failure distribution for the time to first time to system failure is given by

$$
F_{S}(t)=1-R_{S}(t)
$$

Example 4.4 (Safety Instrumented System). Reconsider the system in Example 4.3. The structure function of the system is

$$
\begin{aligned}
\phi(\mathbf{X}(t))= & {\left[X_{1}(t) X_{2}(t)+X_{1}(t) X_{3}(t)+X_{2}(t) X_{3}(t)-2 X_{( }(t) X_{2}(t) X_{3}(t)\right] } \\
& \cdot X_{4}(t) \cdot\left[X_{5}(t)+X_{6}(t)-X_{5}(t) X_{6}(t)\right]
\end{aligned}
$$

Let $R_{i}(t)$ denote the reliability of component $i$, for $i=1,2, \ldots, 6$. The system reliability is then

$$
\begin{aligned}
R_{S}(t)= & {\left[R_{1}(t) R_{2}(t)+R_{1}(t) R_{3}(t)+R_{2}(t) R_{3}(t)-2 R_{1}(t) R_{2}(t) R_{3}(t)\right] } \\
& \cdot R_{4}(t) \cdot\left[R_{5}(t)+R_{6}(t)-R_{5}(t) R_{6}(t)\right]
\end{aligned}
$$# Fault Tree Analysis 

A fault tree illustrates the interrelationships between a potential system fault (denoted the TOP event) and the possible causes of this fault. The causes may comprise component faults, human errors, and environmental events/states. The fault tree is a "static picture" of a potential system fault. The fault tree does not illustrate any dynamic properties of the event chain that may lead to a system fault.

The starting point of a fault tree analysis (FTA) is a system fault, that is, the system state after a failure has occurred. The fault tree is developed by repeatedly asking the question "what can the causes of this event be". This is done successively when moving down a tree structure as illustrated in Figure 4.6. The lowest level causes in the fault tree are called basic events. The connections between these causes are done using logic gates, where the output from a gate is determined by the inputs to it. A special set of symbols is used for this purpose. We illustrate this by Example 4.5. More details may be found in Rausand and Høyland (2004); IEC 61025 (1990); NASA (2002).

Example 4.5 (Safety Instrumented System). Reconsider the safety instrumented system (SIS) in Example 4.3. When a process demand occurs (e.g., fire, gas leakage), at least two of the three sensors (components 1, 2, and 3) in Figure 4.4 must respond and send a signal to the logic solver (component 4). The logic solver will then send a signal to the two valves (components 5 and 6). At least one of the valves must close to shut down the process. A fault tree with respect to the TOP event "SIS fails to function on demand" is shown in Figure 4.6.

### 4.4.4 Modelling Environmental Effects

The stress (e.g., voltage, pressure, temperature) on an item affects the time to failure and hence the failure distribution of the item. The effect of increasing the stress is to accelerate the time to failure. Many different models have been developed to model this. Two of the well-known ones are the following:

## Accelerated Failure Time Model

Let $T_{s}$ denote the time to failure at a specified stress level $s$. In the accelerated failure time model the survivor function of $T_{s}$ is given by

$$
R(t ; s)=R_{0}(t / \psi(s))
$$

where $R_{0}(t)$ is a baseline survivor function associated with a reference value of the stress level, $s_{0}$, and $\psi(s)$ is a function of the stress $s$.

In this model the scaled lifetime $T / \psi(s)$ has the survivor function

$$
R_{s}(t)=\operatorname{Pr}\left(T_{s} / \psi(s)>t\right)=\operatorname{Pr}\left(T_{s}>\psi(s) \cdot t\right)=R(\psi(s) \cdot t)=R_{0}(t)
$$

This means that the scaled lifetime $T_{s} / \psi(s)$ will have the same distribution for all stress levels $s$.

Figure 4.6. Fault tree for the TOP event "SIS fails to function on demand" of a safety instrumented system; Example 4.5

A typical choice of $\psi(s)$ is

$$
\psi(s)=e^{\gamma s}
$$

The scaled lifetime $e^{-\gamma s} T_{s}$ then has a distribution that does not depend on the stress level $s$. The mean value of $T_{s}$ is $E\left(T_{s}\right)=e^{\gamma s} \mu_{0}$ where $\mu_{0}=E\left(T_{0}\right)$ is the mean time to failure at the reference stress level $s_{0}$. By taking the logarithm, we get

$$
\ln T_{s}=\mu_{0}+\gamma s+\epsilon
$$

where $\epsilon$ is a random error with a distribution that does not depend on $s$. This is seen to be a linear regression model and we may hence use linear regression methods to estimate the unknown parameters $\mu_{0}$ and $\gamma$ (e.g., see Ansell and Phillips, 1994).

# Proportional Hazards Model 

In the proportional hazards model, the failure rate function of an item with life length $T_{s}$ when operated under stress level $s$ is given by

$$
z(t ; s)=z_{0}(t) \cdot h(s)
$$where $z_{0}(t)$ is a baseline failure rate function associated with a reference stress level $s_{0}$, and $h(s)$ is a function of $s$. By using this model, we split the failure rate function into two parts, one part that is a function of the time $t$ (and not the stress $s$ ), and one part that is a function of the stress level $s$.

The survivor function at stress $s$ is

$$
\begin{aligned}
R(t ; s) & =\exp \left(-\int_{0}^{t} z(u, s) d u\right) \\
& =\left(\exp \left(-\int_{0}^{t} z_{0}(u) d u\right)\right)^{h(s)}=\left(R_{0}(t)\right)^{h(s)}
\end{aligned}
$$

Let $s_{1}$ and $s_{2}$ be two different stress levels. The relationship between the failure rate function at these stress levels may be expressed as

$$
\frac{z\left(t ; s_{1}\right)}{z\left(t ; s_{2}\right)}=\frac{z_{0}(t) \cdot h\left(s_{1}\right)}{z_{0}(t) \cdot h\left(s_{2}\right)}=\frac{h\left(s_{1}\right)}{h\left(s_{2}\right)}
$$

The relation between the two failure rate functions at time $t$ is hence independent of $t$, and only dependent on the stress levels $s_{1}$ and $s_{2}$. This explains why the model is called a proportional hazards (i.e., failure rate) model.

To get a convenient functional form of the failure rate function, we often have to transform the stress levels, for example, by taking logarithms or using power functions. Sometimes, we also combine two or more stresses. If we, for example, have a pipeline that is exposed to erosion caused by sand particles in the fluid in the pipeline, the rate of erosion (and thereby the failure rate function) will depend on the sand content and the flowrate. It is the combined effect that is important, and not the single stresses.

After having transformed and combined the relevant stresses, we get a vector of stressors $\boldsymbol{x}=\left(x_{1}, x_{2}, \ldots, x_{m}\right)$. It is also common to use physical parameters, like the diameter of a tube, as stressors, which are also called covariates or concomitant variables. The proportional hazards model may, alternatively, be expressed by

$$
z(t ; \boldsymbol{x})=z_{0}(t) \cdot \psi(\boldsymbol{x}, \boldsymbol{\beta})
$$

where $\psi(\boldsymbol{x}, \boldsymbol{\beta})$ is a function and $\boldsymbol{\beta}=\left(\beta_{1}, \beta_{2}, \ldots\right)$ is a row vector of unknown parameters.
Example 4.6 (Constant failure rate). Assume that the failure rate is constant, such that, $z(t ; \boldsymbol{x})=\lambda_{0} \cdot \psi(\boldsymbol{x}, \boldsymbol{\beta})$. The survivor function is now

$$
R(t ; \boldsymbol{x})=\exp \left(-\lambda_{0} \cdot \psi(\boldsymbol{x}, \boldsymbol{\beta})\right)
$$

and the mean time to failure is

$$
\mathrm{MTTF}_{s}=\frac{1}{\lambda_{0} \cdot \psi(\boldsymbol{x}, \boldsymbol{\beta})}=\mathrm{MTTF}_{0} \cdot \frac{1}{\psi(\boldsymbol{x}, \boldsymbol{\beta})}
$$

where $\mathrm{MTTF}_{0}$ and $\mathrm{MTTF}_{\boldsymbol{x}}$ are the mean time to failure at the baseline stress and stress level $\boldsymbol{x}$, respectively.

Note that the simple model used in MIL-HDBK-217F to determine the failure rate of electronic components is a special case of this model.The most commonly used form of $\psi(\cdot)$ was introduced by Cox (1972) and has since then been referred to as the Cox model. This model uses

$$
\psi(\boldsymbol{x} ; \boldsymbol{\beta})=\exp (\boldsymbol{\beta} \boldsymbol{x})=\exp \left(\sum_{j=1}^{m} \beta_{j} x_{j}\right)
$$

where $m$ is the dimension of the (column) vector $\boldsymbol{x}$ of stressors. By taking logarithms, we get the linear relationship

$$
\ln z(t ; \boldsymbol{x})=\ln z_{0}(t)+\sum_{j=1}^{m} \beta_{j} x_{j}
$$

Estimators for the unknown parameters may, for example, be found in Ansell and Phillips (1994); Crowder et al. (1991); Kumar and Klefsjø (1994).

# 4.5 Reliability Modelling - II 

The modelling of subsequent failures (at component, system or some intermediate level) depends on the maintenance actions. IEC 60050-191 defines maintenance as "The combinations of all technical and corresponding administrative actions, including supervision actions, intended to retain an entity in, or restore it to, a state in which it can perform its required functions." Maintenance involves one or more of the following actions: servicing (e.g., cleaning and lubrication), testing/inspection, removal/replacement, repair/overhaul, and modification through redesign.

Maintenance actions to control the deterioration process leading to failure of an item are called preventive maintenance (PM) actions and actions to restore a failed item to its functioning state are called corrective maintenance (CM) actions. The time needed to carry out CM and PM actions can vary and needs to be modelled properly. For minor PM and CM actions, the time needed is small relative to the time between failures and can be ignored. For a major overhaul, the time can be significant and cannot be ignored.

### 4.5.1 Modelling CM Actions

The options available depend on whether the failed item is repairable or not.

## Replace by New or Used Item

If the item is non-repairable, then the only CM action is to replace a failed item by a working (new or used) item. If a new item (similar to the failed item) is used in the replacement, then the time to failure is a random variable with the same distribution $F(t)$ as for the initial item, and the repair action has brought the item to an "as good as new" condition, as illustrated in Figure 4.7.

If a used item of age $x$ is used in the replacement, the time to failure is a random variable with conditional failure distribution

$$
F(t \mid x)=\operatorname{Pr}(T \leq t+x \mid T>x) \quad \text { for } t \geq 0
$$

Figure 4.7. Failure rate under imperfect repair

# Minimal Repair 

This model is mainly used for complex items comprising a number of components. If one component fails and causes item failure, only the failed component is repaired. After the repair action is completed, the status of the system is approximately the same as just before the failure. The repair action has a minimal effect on the system, since the likelihood of failure just after the repair action is approximately the same as it was just before the component failed. The repair action is therefore called a minimal repair and the item condition after the minimal repair is often called "as bad as old."

Let $z(t)$ denote the failure rate of a new item. If the item fails at time $t_{i}$ and the time to repair is negligible (so that it can be ignored), then the failure rate of the repaired item is given by $\tilde{z}(t)=z(t)$ for $t>t_{i}$, as illustrated in Figure 4.7.

## Imperfect Repair

An imperfect repair is somewhere between a replacement and a minimal repair, and may also be called a normal repair. Just after an imperfect repair action, the failure rate of the item is greater than for a new item and, in general, less than that under minimal repair (imperfect repair I in Figure 4.7). It is also possible that additional failures are introduced during the maintenance action such that the failure rate after the (imperfect) maintenance action is higher than it was just before the action. This is illustrated as imperfect repair II in Figure 4.7.

Many different models have been proposed for imperfect repair and details can be found in Pham and Wang (1996).

### 4.5.2 Modelling PM Actions

Preventive maintenance (PM) is the set of actions to control the rate of degradation and reduce the likelihood of failure occurrence. As such, these actions are taken when the item is still in operational state as opposed to CM, which is the set of actions that are taken after the item fails. Many different kinds of PM policies are used and these include the following:Age-based policy: PM actions are based on the age of the item.
Clock-based policy: PM actions are carried out at set times.
Usage-based policy: PM actions are based on the usage of the item.
Condition-based policy: PM actions are based on the condition of the item. This involves monitoring one or more variables characterizing the wear process causing the degradation.
Opportunity-based policy: This is applicable for multi-component items, where a CM action for a failed component provides an opportunity to carry out PM actions on one or more of the remaining components.
Design-out policy: This involves re-designing the very unreliable components of an item. As a result, the new item will (hopefully) have better reliability characteristics than the earlier item.

# ROCOF 

The rate of occurrence of failures (ROCOF) is a very useful concept in the modelling of failures over time and the effect of PM (and CM) actions. It characterizes the probability that the system fails in the interval $(t, t+\Delta t)$ given the history, $\mathcal{H}(t)$, of failures and maintenance actions over the interval $(0, t)$ and is given by an intensity function

$$
\lambda(t)=\lim _{\Delta t \rightarrow 0} \frac{\operatorname{Pr}(N(t+\Delta t)-N(t)>1 \mid \mathcal{H}(t))}{\Delta t}
$$

where $N(t)$ is the number of failures in the interval $(0, t)$. Since the probability of two or more failures in the interval $(t, t+\Delta t)$ is zero as $\Delta t \rightarrow 0$, the intensity function is equal to the derivative of the conditional expected number of failures, so that

$$
\lambda(t)=\frac{d}{d t} \mathrm{E}(N(t) \mid \mathcal{H}(t))
$$

The cumulative ROCOF is

$$
\Lambda(t)=\int_{0}^{t} \lambda(u) d u=E(N(t))
$$

Two models of PM actions that have been used extensively in the reliability literature are the following (e.g., see Doyen and Gaudoin, 2004):

## Reduction in Age

This involves the concept of virtual age, which increases linearly with time and every PM action results in a reduction in the virtual age. The ROCOF is a function of the virtual age.

Let $B(t)$ denote the virtual age of the item at time $t$, and let $t_{i}$, for $i=0,1,2, \ldots$, denote the time instants at which PM actions are carried out. After the $i$ th PM action, the reduction in the virtual age is $\tau_{i}$ so that virtual age is given by $B(t)=t-$$\sum_{j=0}^{i} \tau_{j}$, for $t_{i}<t \leq t_{i+1}$ with $\tau_{0}=0$ and $t_{0}=0$. As a result, the ROCOF is given by the intensity function

$$
\lambda(t)=z(B(t))=z\left(t-\sum_{j=0}^{i} \tau_{j}\right) \quad \text { for } t_{i}<t \leq t_{i+1} \text { and } i=0,1,2, \ldots
$$

The reduction in the virtual age at the $i$ th PM action and $i$ are constrained by the relationship

$$
0 \leq \tau_{i}<t_{i}-t_{i-1} \quad \text { for } i=1,2, \ldots
$$

This implies that the item can never be restored to as good as new. Figure 4.8 shows a plot of the virtual age $B(t)$ and the intensity function $\lambda(t)$.


Figure 4.8. ROCOF with age reduction during PM actions

# Reduction in ROCOF 

In this model, there is reduction in the ROCOF associated with each PM action, so that after the $i$ th repair, the ROCOF is given by

$$
\lambda(t)=z(t)-\sum_{j=1}^{i} \delta_{i} \quad \text { for } t_{i}<t \leq t_{i+1}
$$

where $\delta_{i}$ is the reduction in the ROCOF at the $i$ th PM and is constrained by the relationship$$
\lambda(0) \leq \sum_{j=1}^{i} \delta_{i}<\lambda\left(t_{i}\right)
$$

for $t_{i}<t<t_{i+1}$. This ensures that the ROCOF never goes below the failure rate for a new item. Figure 4.9 shows a plot of the intensity function $\lambda(t)$.


Figure 4.9. Reduction in ROCOF with PM actions

Note. When the time needed to carry out a PM action cannot be ignored, then the ROCOF is not defined over the period when PM actions are carried out.

# 4.5.3 Other Approaches 

Many other approaches have been used for modelling failures over time at system level. These include Markov and semi-Markov formulations (Bhat, 1972; Ross, 1996; Limnios and Oprisan, 2001) to name a few.

### 4.6 Reliability Analysis

Reliability analysis can be divided into two broad categories: (i) qualitative and (ii) quantitative. The former is intended to verify the various failure modes and causes that contribute to the unreliability of a system. The latter uses real failure data in conjunction with suitable mathematical models to produce quantitative estimates of system reliability as discussed in the previous section.

### 4.6.1 Qualitative Analysis

The two main topics in the qualitative analysis are (i) FMEA/FMECA and (ii) Fault tree analysis. We discussed briefly fault tree analysis in Section 4.4.3. In this section we discuss FMEA.# Failure Modes and Effects Analysis (FMEA) 

A failure modes and effects analysis (FMEA) is used to identify, analyse, and document the possible failure modes that can exist for a system, and the effects of such failures on the system's performance. If the criticality of each failure mode is analysed, the analysis is called a failure modes, effects, and criticality analysis (FMECA). According to IEEE Std. 352, the basic questions to be answered by FMEA are the following:

- How can each part conceivably fail?
- What mechanisms might produce these modes of failure?
- What could the effects be if the failures did occur?
- How is the failure detected?
- What inherent provisions are provided in the design to compensate for the failure?

For each component at the part level, the failure modes and their effects are usually documented on worksheets. The documentation involves the following:

1. Description of the different parts. This is done through a proper reference number, the intended function of the part and the normal operational mode
2. Characterization of failure. This involves listing the different possible failure modes, failure mechanisms responsible for the different failure modes and the various means of detecting the different failure modes
3. Effect of failure on other components of the system and the system performance.
4. Severity ranking that characterizes the degree of the consequences of each failure mode.

There are two main approaches to FMEA. One is the hardware approach that starts with the hardware components at the lowest level in the system hierarchy and analyses their possible failure modes. The other is the functional approach that focuses on the functions rather than the hardware components. The FMEA may start at the highest system level and proceed down to lower levels (top-down), or start at the lowest part level and proceed to the highest system level (bottom-up). The hardware bottom-up approach is normally used when we are analysing a system where hardware components can be uniquely identified from drawings or other system descriptions. The functional top-down approach is normally used when we analyse a system in an early design phase before all details about hardware components have been decided.

The most critical failure modes are sometimes extracted from the FMEA/FMECA and entered into a critical items list. The critical item list is a living document that provides valuable input to design changes, test planning, safe operational procedures, and so on.

Example 4.7 (Safety Instrumented System). A process shutdown system is a common example of a safety instrumented system. The shutdown action is usually carried out by fail-safe valves, that is, valves that are kept in an open position by hydraulic or pneumatic pressure during normal operation. When the valve receives a signal toclose, the pressure is bled off and the valve will close by some built-in mechanism (e.g., spring force).

The failure modes for the shutdown valve and the effect of the failures are as follows:

| Failure mode | Failure effect |
| :-- | :-- |
| Fail to close | Flow cannot be stopped |
| Leakage in closed position | Flow is partly stopped |
| External leakage | Fluid leaks to the environment |
| Spurious closure | Flow stopped without signal |
| Fail to open | Flow cannot be opened after a closure |

The severity of the various failure modes will depend on the process, the environment, and the type of fluid.

# 4.6.2 Quantitative Analysis 

Quantitative analyses are used to evaluate various performance measures. We briefly discuss some main measures.

## Availability

Let $X(t)$ denote the state of an item at time $t$. It is a binary variable with $X(t)=1$ if the item is in working state and $X(t)=0$ if not. There are several different notions of availability, as indicated below.

- The availability $A(t)$ at time $t$ (also called point availability) is given by

$$
A(t)=\operatorname{Pr}(X(t)=1)=\mathrm{E}(X(t))
$$

- The limiting availability is given by

$$
A=\lim _{t \rightarrow \infty} A(t)
$$

when the limit exists.

- The average (mean) availability in $(0, \tau)$ (also called mission availability) is given by

$$
A(0, \tau)=\frac{1}{\tau} \int_{0}^{\tau} A(t) d t
$$

where $A(0, \tau)$ can be interpreted as the mean proportion of the time in $(0, \tau)$ where the item is in a functioning state.

- The limiting average availability (also called steady state availability) is given by

$$
A_{\infty}=\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_{0}^{\tau} A(t) d t
$$In the special case where the item is repaired to an "as good as new" condition after each failure, such that all up-times are independent and identically distributed, and that also all down-times are independent and identically distributed, the (steady state) average availability is given by

$$
A_{\infty}=\frac{\text { MTTF }}{\text { MTTF }+ \text { MTTR }}
$$

where MTTR denotes the average down-time for a repair action.
The unavailability of an item at time $t, \bar{A}(t)$, is defined as $\bar{A}(t)=1-A(t)$, and similarly for the other availability notions.

# Probability of Failure on Demand 

Consider an item that is put into operation at time $t=0$. Some critical failure modes of the item are hidden. The item is therefore function-tested after regular intervals of length $\tau$. We assume that all failures are detected during the function test. If failures are revealed, they are repaired and the item is considered to be "as good as new" after each test. The test and repair times are considered to be negligible compared to $\tau$. The average unavailability is, in this case, usually called probability of failure on demand (PFD). The PFD can here be determined from (see Rausand and Høyland, 2004)

$$
\operatorname{PFD}=1-\frac{1}{\tau} \int_{0}^{\tau} R(t) d t
$$

## Example 4.8 (Safety Instrumented System).

(a) Consider a safety instrumented system with a single input element (e.g., a sensor) with constant failure rate $\lambda$ with respect to hidden fail-to-function (FTF) failures. The survivor function of the element is $R_{a}(t)=e^{-\lambda t}$. With test interval $\tau$, the PFD becomes

$$
\mathrm{PFD}_{a}=1-\frac{1}{\tau} \int_{0}^{\tau} e^{-\lambda t} d t=1-\frac{1}{\lambda \tau}\left(1-e^{-\lambda \tau}\right) \approx \frac{\lambda \tau}{2}
$$

The approximation is acceptable when $\lambda \tau$ is small (e.g., $\leq 10^{-2}$ ).
If a demand for the safety instrumented system occurs, the PFD denotes the (average) probability that the sensor will not be able to raise alarm.
(b) Consider a safety instrumented system with three identical and independent input elements that are configured as a 2-out-of-3 system. The elements have constant failure rate $\lambda$ and are tested at the same time with test interval $\tau$. The survivor function of the 2 -out-of- 3 system is $R_{b}(t)=3 e^{-2 \lambda t}-2 e^{-3 \lambda t}$ and the PFD is

$$
\mathrm{PFD}_{b}=1-\frac{1}{\tau} \int_{0}^{\tau}\left(3 e^{-2 \lambda t}-2 e^{-3 \lambda t}\right) d t \approx(\lambda \tau)^{2}
$$(c) Consider a safety instrumented system with two independent elements that are configured as a series (2-out-of-2) system. The elements have constant failure rates $\lambda_{1}$ and $\lambda_{2}$, respectively. The survivor function of the system is $R_{c}(t)=$ $e^{\lambda_{1} t} \cdot e^{-\lambda_{2} t}=e^{-\left(\lambda_{1}+\lambda_{2}\right) t}$ and the PFD is

$$
\mathrm{PFD}_{c}=1-\frac{1}{\tau} \int_{0}^{\infty} e^{-\left(\lambda_{1}+\lambda_{2}\right) t} d t \approx \frac{\left(\lambda_{1}+\lambda_{2}\right) \tau}{2}=\mathrm{PFD}_{1}+\mathrm{PFD}_{2}
$$

where $\mathrm{PFD}_{i}$ is the PFD of element $i$ for $1=1,2$.
Safety instrumented systems (SISs) are classified into safety integrity levels (SIL). For a SIS that is operated in a so-called low demand mode, the safety integrity level is (partly) defined from the PFD as given below:

| Safety integrity level (SIL) | PFD |
| :--: | :--: |
| 4 | $\geq 10^{-5}$ to $<10^{-4}$ |
| 3 | $\geq 10^{-4}$ to $<10^{-3}$ |
| 2 | $\geq 10^{-3}$ to $<10^{-2}$ |
| 1 | $\geq 10^{-2}$ to $<10^{-1}$ |

To supply a SIL 3 system, the manufacturer has to verify that the SIS has a PFD $<10^{-3}$. In addition comes a set of qualitative requirements.

Number of Failures in $(0, t)$
Let $N_{\mathrm{f}}(t)$ denote the number of failures in the time interval $(0, t)$. We consider two cases and present the final results and omit the details of the derivation. Interested readers can find details in the references cited.

Non-repairable Item: Consider an item that, upon failure, is replaced by a new item of the same type (i.e., that is statistically identical to the failed item), and assume that the replacement times are negligible. In this case the failures occur according to a renewal process since each failure results in the item getting renewed back to new. Let $p_{n}(t)$ denote the probability of $N_{\mathrm{f}}(t)=n$. Then it can be shown that

$$
p_{n}(t)=F^{(n)}(t)-F^{(n+1)}(t)
$$

where $F^{(n)}(t)$ is the $n$-fold convolution of $F(t)$ with itself. ${ }^{4}$ Let $M(t)$ denote the expected value of $N_{\mathrm{f}}(t)$, then $M(t)$ is given by the solution of the following integral equation (also called the renewal integral equation)

$$
M(t)=F(t)+\int_{0}^{t} M(t-x) f(x) d x
$$

[^0]
[^0]:    ${ }^{4}$ See Ross (1996) for details about convolution formulas.Case (2) Repairable Item: Consider an item that, upon failure, is subject to a minimal repair (see page 74), and assume that the repair times are negligible. In this case, $N_{\mathrm{f}}(t)$ is distributed according to a non-homogeneous Poisson process with intensity function given by $\lambda(t)=z(t)$ so that

$$
p_{n}(t)=\frac{(Z(t))^{n}}{n!} e^{-Z(t)} \quad \text { for } n=0,1,2, \ldots
$$

where $Z(t)$ is the cumulative failure rate function given by Equation (4.8).
The expected number of failures over the interval $(0, t)$ is given by

$$
\mathrm{E}\left(N_{\mathrm{f}}(t)\right)=Z(t)
$$

# 4.6.3 Simulation 

Sometimes, the situation is so complex that we are not able to find the desired solutions by analytical methods. In these situations, we may use so-called next-event Monte Carlo simulation (Mitrani, 1982; Ross, 2002). The Monte Carlo simulation is carried out by simulating "typical" lifetime scenarios on a computer. We start with a model of the system, usually a flow diagram or a reliability block diagram. Component failures, CM and PM actions and other scheduled events and conditional events are included to create a simulated lifetime scenario that is as close to the real lifetime scenario as possible. A set of performance measures (e.g., number of failures, downtime) are calculated from the lifetime scenario.

The simulation is carried out a high number of times and estimates of the performance measures are deducted from the resulting data. The simulator has an internal clock and it is therefore possible to take into account both seasonal variations and long term trends in the simulation.

### 4.7 Reliability Engineering

Reliability engineering deals with the design and construction of systems, taking into account the unreliability of its components. It also includes testing and programmes to improve reliability. Good engineering results in a more reliable end product.

### 4.7.1 Reliability Allocation

Reliability allocation (or reliability apportionment) is the process of allocating product (system level) reliability requirements to sub-systems, and component levels in the design phase. Preliminary reliability allocation is often based on historical performance data, that is, what reliability has been achieved by similar products.

At the component level, the assigned target value can exceed the reliability of commercially available items. In this case we need to improve the reliability of the component or use preventive maintenance where the component is replaced periodically.Example 4.9. Consider a series system of $n$ independent components with survivor functions $R_{1}, R_{2}(t), \ldots, R_{n}(t)$. The system survivor function is then $R_{S}(t)=$ $\prod_{i=1}^{n} R_{i}(t)$. Assume that the system reliability requirement specifies that $R_{S}(t) \geq$ $R^{*}(t)$, for some specified time $t$. If

$$
R_{S}(t)=\prod_{i=1}^{n} R_{i}(t) \geq R^{*}(t)
$$

then the requirement is fulfilled. If not, we have to improve one or more of the $n$ components. In this process we have to take into account the cost, and the relative difficulty, of improving the different components.

Several methods have been developed for this purpose. Among these are:

- Equal apportionment method
- ARINC apportionment method
- AGREE apportionment method
- Feasibility of object method
- Minimum effort algorithm

For more information, see, for example, MIL-HDBK-338B and Ebeling (1997).

# 4.7.2 Reliability Improvement 

There are two basic approaches to improving component (or system) reliability. They are as follows:

## Use of Redundancy

This involves the use of replicates rather than a single item (sub-system to component level). Redundancy can only be used when the functional design of the system allows for the incorporation of replicated components.

Building in redundancy corresponds to using a module of replicated items as opposed to a single item. The manner in which these replicates are put into use depends on the type of redundancy. A module failure occurs only when some or all of the replicates fail. There are two types of redundancy:

Active redundancy: Active redundancy means that all the items in the module are in operational state, or "fully energized," when put into use. In the latter case, the active redundancy is often called hot standby.
Passive redundancy: In passive redundancy, only a part of the items in the module are fully energized. The remaining items are either partially energized (also called partly loaded standby) or kept in reserve and energized when put into use (cold standby). When a fully energized item fails, it is replaced by one of the standby items using a switching mechanism, provided that not all of the items in the module have failed.# Reliability Growth 

The objective of reliability growth testing is to improve the reliability of an item through minor design changes and changes in manufacturing processes and procedures. The reliability growth is achieved through a test, analyse, and fix (TAAF) ${ }^{5}$ programme in an iterative manner. It involves a sequential execution of the four stages shown in Figure 4.10 during each iteration.


Figure 4.10. Test, analyse, and fix (TAAF) cycle

The TAAF process begins in the design phase and consists of tests that are specifically designed to expose the item to all types of stresses the item is expected to encounter during its life cycle. Deficiencies and failures are recorded and carefully analysed by engineers to reveal the root causes of the deficiencies. Design changes are made to remove the failure causes and to prevent the failure modes. The process is repeated until the test results are satisfactory. For further discussion of TAAF, TAAF test design principles, and relationship of TAAF to other testing programmes, see IEC 61014 and Priest (1988, Chapter 9).

A number of reliability growth models have been developed to monitor the progress of the development programme and the improvements in reliability of the item under consideration. The models can be broadly categorized into two types continuous and discrete models. Each of these can be further sub-divided into parametric models (which involve a specified distribution of time to failure) and nonparametric models (which involve specification of a functional form for the reliability improvement relationship apart from the failure distribution). Some well-known reliability growth models are:

- Duane model
- IBM model
- Crow/AMSAA model
- Lloyd and Lipow model
- Jelinski and Moranda model
- Littlewood and Verrall model
- Littlewood model
- Musa model
- Musa-Okumoto model

For further discussion and many additional references, see Lloyd and Lipow (1962); Amstadter (1971); Dhillon (1983); Walls and Quigley (1999); MIL-HDBK338B (1998).

[^0]
[^0]:    ${ }^{5}$ Some authors use the acronym TAFT (test, analyse, fix, test)A failure reporting and corrective action system (FRACAS) is sometimes initiated to record failure data gathered through the testing and improvement programme. The FRACAS is a closed-loop reporting system that is a parallel to the TAAF cycle. Most benefit from the FRACAS is realized when it is implemented early in the test programme and is directly linked to the modelling effort. For more details about FRACAS, see O'Connor (2002); Dhudshia (1992); MIL-STD-2155 (1985). Approaches to statistical analysis of data from reliability growth testing are outlined in IEC 61164.

# 4.7.3 Root Cause Analysis 

A root cause analysis is carried out after a failure has occurred with the intention to learn how and why the failure occurred. The analysis is mainly focused on the fundamental (root) causes of failure. The question "why?" is asked several times until a satisfactory explanation is found. Once the root cause is identified, the problem may be fixed by taking appropriate corrective actions by way of changes to the design or the material selection. For more on root cause analysis of mechanical components, see Nishida (1992) and DOE-NE-STD-1004-92 and for electronic components, see MIL-HDBK-338B.

### 4.8 Reliability Prediction and Assessment

Reliability prediction is a process used for estimating item reliability during the design phase. Reliability predictions provide a basis for deciding on reliability improvement, which can involve reliability growth during the development phase (Meeker and Escobar, 1998; Blischke and Murthy, 2000). Reliability prediction is the reliability potential of an item based on available design information. During the development phase, we can obtain an estimate of the actual reliability by testing. This process is called reliability assessment.

### 4.8.1 Reliability Prediction

Prediction involves models rather than actual systems and provides a basis for test planning, manufacturing, evaluation of reliability growth, maintenance, and other management activities. Reliability predictions should be continually updated when design changes are performed, and when test results become available. Healy et al. (1997) discuss the different purposes for reliability predictions and they include the following:

- Performing trade-off studies
- Setting plans for developmental testing
- Planning for design improvements
- Cost analyses, including life cycle cost studies
- Providing a basis for evaluation of reliability growth
- Studies of maintenance requirements and logistics# 4.8.2 Reliability Assessment 

The most important reason for careful reliability assessment is to verify that the predicted reliability is attained or is attainable. Other reasons for assessment include verification of updated predictions, monitoring of product quality, determination of reliability growth, and so forth. Data generated from testing forms the basis for reliability assessment. The assessment of reliability involves the use of statistical estimation methods which can be found in many books.

During the development phase, data is generated through several types of testing. Meeker and Hamada (1995) discuss the various tests and these include the following:

- Laboratory tests for materials evaluations
- Laboratory life tests of parts, components, and so on
- Environmental stress screening
- Tests of prototypes
- Degradation tests of materials, parts, and so on
- Test results from suppliers
- Qualification testing
- Stress life tests
- Reliability demonstration tests

To ensure data validity and reliability, carefully designed experiments are necessary.
An important additional experimental technique is accelerated testing, that is, testing under conditions involving stresses somewhat or far in excess of those encountered in normal operation. This allows the analyst to obtain data in a shorter time frame, but this can induce new modes of failures that do not exist under normal stress.

Testing during manufacturing is to eliminate manufacturing defects and early part failures. Two types of testing are commonly used:

## Environmental Stress Screening

Environmental stress screening (ESS) is a screening process in which an item is subjected to environmentally generated stresses to precipitate latent item defects. The environmental stresses may be any combination of temperature, vibration or humidity.

## Burn-in Testing

Burn-in is a process used to eliminate the high initial failure rate due to manufacturing defects. It involves putting items on a test bed to detect early failures, so that they can be weeded out before the item is released for sale.# 4.9 Reliability Management 

Reliability management deals with the many different management issues in the context of managing the design, manufacture, and/or operation of reliable products and systems. The manufacturer needs to look at these issues from an overall business perspective, taking into account the issues of concern to customers, such as product reliability, safety, operating costs, warranty, maintenance service contract, and so on. Two topics of great importance in the context of reliability performance and specifications are (1) costs and (ii) data for effective management.

### 4.9.1 Costs

Building reliability into a product is a costly exercise. From the manufacturer's point of view, some of the costs are as follows:

- Design cost
- Development cost
- Production cost
- Post-sale support costs

From the customer point of view, the main cost is the maintenance costs over the useful life of the product.

For an expensive custom-built product, the life cycle cost (LCC) is critical in the customer's decision to proceed with the project. The LCC process involves several steps as illustrated in Figure 4.11. For more on LCC, see IEC 60300-3-3 (2005); Fabrycky and Blanchard (1991); Kawauchi and Rausand (1999).

There are many indirect costs that result from product unreliability. From the manufacturer point of view these include the following:

- Warranty costs
- Loss of sales
- Dissatisfied customers
- Impact on product and business reputations

From the customer point of view, the indirect costs are the costs resulting from unavailability of the product.

### 4.9.2 Data for Effective Management

Many different kinds of data are needed for reliability related decision making in the different stages on the product life cycle. The relevant data will be discussed in Chapters 5 to 9 separately, and then in an integrated manner in Chapter 11.

Figure 4.11. The steps of the LCC process (from Kawauchi and Rausand, 1999)

# 4.10 Case Study: Cellular Phone 

The cellular phone is composed of several elements and the integrated circuit (also known as IC or chip) is an important element. ICs can be classified into three groups: digital, analogue, and mixed signal (both analogue and digital on the same chip). Digital ICs contain a large number of logic gates, flip-flops, multiplexers and other circuits. Analogue ICs (such as sensors, operational amplifiers etc) process continuous signals and are used to perform various functions (e.g., amplification, filtering, demodulation). The mixed signal ICs carry out functions such as A/D and D/A conversions.

ICs are fabricated in a layer process involving the following three steps: (i) imaging, (ii) deposition, and (iii) etching. These processes are supplemented by doping, cleaning, and planarization steps.

The process starts with a mono-crystal silicon wafer as a substrate. Photolithography is used to mark different areas of the substrate to be doped or to deposit polysilicon, insulators or metal tracks. This is done over several layers. The wafer is cut into rectangular blocks, each called a die. The die is then connected to a package.There are many different technologies for packaging. In the flip-chip ball grid array (FCBGA) package, the die is mounted upside down (flipped) and connects to the package balls via a package substrate that is similar to a circuit board rather than by wires. This allows an array of input-output signals to be distributed over the entire die. ${ }^{6}$

The reliability of chips has received a lot of attention since its appearance. Roesch (2006) presents a historical review of IC reliability for silicon and compound semiconductors. The different reliability eras, and the focus of attention in each era, for the silicon case are indicated below.

First era (1975-1980): Learning about material properties of silicon (Si), aluminium $(\mathrm{Al})$, and silicon oxide $\left(\mathrm{SiO}_{2}\right)$ and their various interactions for reliability improvement.
Second era (1980-1985): Identification and study of the mechanisms for the major reliability problems such as electro-migration, stress migration, time-dependent dielectric breakdown (TDDB), cracked die, broken bond wires, and so on.
Third era (1985-1990): Developing degradation models for the different mechanisms (reliability physics) and deriving the acceleration factors for the environmental stresses of temperature cycling and corrosion. ${ }^{7}$
Fourth era (1990-1995): Building-in-reliability (BIR) with a lot of emphasis on wafer-level reliability.
Fifth era (1995-2000): Merging the metrics of reliability and quality with a focus on a major defect-reduction effort.

[^0]
[^0]:    ${ }^{6}$ For more details of IC, see Mead and Conway (1980); Hodges et al. (2003).
    ${ }^{7}$ For more details of the failure mechanisms in semiconductor devices, see Amerasekera and Campbell (1987).# Performance and Specification in the Front-end Phase 



### 5.1 Introduction

The front-end phase is phase 1 (stage-I, level-I) in Figure 2.4. The performance and specification in phase 1 were discussed in Section 3.6.1. In this chapter, we discuss this in more detail. The processes for defining the desired performance DP-I for standard and custom-built products differ slightly. When DP-I has been decided, the processes for deriving the specification SP-I and the predicted performance PP-I are similar.

The outline of the chapter is as follows: Sections 5.2 and 5.3 deal with standard products. We start with a discussion of the overall process in Section 5.2. It involves three sub-phases and each of these is discussed in more detail in the next three sections. Section 5.3 looks at data collection and data analysis, Section 5.4 deals with idea generation and screening, and Section 5.5 deals with product concept formulation and evaluation leading to defining DP-I, and deriving SP-I and PP-I. In Section 5.6 we look at performance and specification for specialized (custom-built) products. Section 5.7 looks at the reliability implications of the decisions made in the front-end phase and forms the link to the next chapter. In Section 5.8, we discuss issues related to the case study on cellular phones.

### 5.2 Front-end Process for Standard Products

The process for deciding on product performance and specification for standard products is shown in Figure 5.1 and involves the three sub-phases indicated below.

Sub-phase 1 - Data collection and analysis: Analysis of data may indicate whether or not there is a need for new product development (NPD). We discuss problems related to data collection and the tools and techniques for data analysis in Section 5.3 and illustrate some typical scenarios leading to new product development.Sub-phase 2 - Idea generation and screening: Some of the basic concepts were discussed in Section 2.5.1. We build on this discussion and focus on the tools and techniques needed for carrying out this in Section 5.4.
Sub-phase 3 - Product concept formulation and evaluation: Some of the basic concepts were discussed in Section 2.5.1. We build on this discussion and focus on defining DP-I based on the outcome of the earlier two sub-phases and then deriving SP-I and PP-I. The process is iterative as shown in Figure 5.1. We discuss tools and techniques, and models that are needed in Section 5.5.


Figure 5.1. Front-end process for standard productsIt is not possible to give the details of all the tools and techniques that are needed in each of the three sub-phases. Instead, we discuss a few important ones and give references where interested readers can get more details. Similarly, it is not possible to discuss all the different models that have been developed. Rather, we focus on some simple models to illustrate the use of models in decision making and cite references where interested readers can get details about other models.

# 5.3 Data Collection and Analysis [Sub-phase 1] 

Many different kinds of data collected by manufacturers are relevant in the context of new product development. Data analysis transforms the data into information and this can be done at many different levels. The information forms the basis for decision making on whether to proceed with new product development or not. Figure 5.2 shows the links between data, analysis, information, and decision making.

| Data |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| Scientific/technical | Customer related | Product related | Market related | Business related |
| $\downarrow$ | $\downarrow$ | $\downarrow$ | $\downarrow$ | $\downarrow$ |
| Data analysis |  |  |  |  |
| Component level |  | Product level | Business level |  |
| $\downarrow$ |  | $\downarrow$ |  | $\downarrow$ |
| Information |  |  |  |  |
| $\downarrow$ |  |  |  |  |
| Decision |  |  |  |  |
| Do not initiate new product development |  | Initiate new product development |  |  |
|  |  | Minor/incremental change | Major/radical change | New product |

Figure 5.2. Data analysis in sub-phase 1

### 5.3.1 Data Collection

The data relevant for decision making in the front-end phase can be broadly grouped into the following categories:

- Scientific/technical data
- Customer related data
- Product related data
- Market related data
- Business related data

The main sources for the data are the following:Management systems: Businesses use many different types of management systems. These, along with examples of the kind of data they provide, include: accounting systems (cost data); project management systems (product-related data during development); production systems (product-related data - e.g., conformance to specification during production); supply management systems (material flow data); customer support systems (customer-related data).
Market surveys: Market surveys are carried out to obtain commercial and customerrelated data. This involves carefully designed questionnaires in order to obtain valid and reliable data.
Warranty servicing and field support: Data from warranty service and field support provide valuable information regarding product performance in the field. If the data are collected properly, it should also provide useful customer-related information such as usage mode and intensity, customer satisfaction and needs.

Data collection is discussed in more detail in Chapter 11.

# 5.3.2 Data Analysis 

Data analysis is the summarization and presentation of the data. Summary values provide concise measures of the basic information content and graphical presentations give the overall picture. These are needed for effective decision making. The analysis depends on the type of data. The tools and techniques needed for analysis are discussed in Chapter 11.

The analysis can be done at three different levels as indicated in Figure 5.2 and we discuss each of these.

## Component Level

The component level analysis deals mainly with technical data related to component performance. In the context of reliability, this includes failure modes and causes of failures (root cause analysis), times to failure, repair times (in the case of repairable components), cost of repairs, and so on. This kind of data is generated during the development and the post-sale phases of the product life cycle. The analysis provides estimates of the component reliability and this helps in deciding whether further development is needed or to replace the component with a more reliable one.

## Product Level

The data at product level can be technical, economic, and usage related. In the context of reliability, the analysis provides information regarding product reliability in the field (technical), warranty costs per item sold (economic) or customer satisfaction (usage related). This can then be used for decision making, such as to improve the production process (if the problem is quality variations in production) or to improve reliability through design changes (e.g., reduce warranty costs, increase customer satisfaction).# Business Level 

The business level data deals with product performance from the business viewpoint and changes in the market that can affect sales and revenue. As such, the analysis of market-related data yields information regarding trends and influence of competitors' actions; technical data provide information regarding the potential for new products, and so on.

### 5.3.3 Outcome of Sub-phase 1

The outcome of sub-phase 1 is a decision whether to initiate a new product development programme or not. In the former case, we proceed to sub-phase 2 and in the latter case we continue with data collection and analysis as indicated in Figure 5.1. We indicate four different scenarios for new product development and these correspond to the "opportunities" in Figure 2.2.

## Scenario 1

Business level analysis indicates that customers are happy with the product, but the warranty costs are higher than expected and hence result in reduced profits. The driver for improvement is top management wanting to improve the overall profit by reducing the warranty costs. The aim of the product development is to improve the reliability of the product by minor changes to the design.

## Scenario 2

Price is an important variable in the marketing of a product. The price needs to decrease with time unless there is periodic product upgrade to counteract the price erosion and ensure the desired profit margin. In this scenario, the product development is to improve the existing product (within the same product platform) and is driven by economic considerations. ${ }^{1}$

## Scenario 3

A competitor has introduced a product that the customers consider to be better and this has affected the sales of the manufacturer's current product. One way for the manufacturer to counteract this is through a new and improved product (with better performance attributes) along with better product support (e.g., longer warranty period). In this case, the driver for the new product is a market factor and the new product needs to be significantly better than the existing product.

[^0]
[^0]:    ${ }^{1}$ Manufacturers of notebook computers based on the 486 CPU upgraded their products periodically, each time incorporating some combination of new screen, CPU, battery, hard drive or RAM. Eventually, the Pentium CPU made platforms based on the 486 CPU obsolete (Wilhelm and Xu, 2002).# Scenario 4 

A new scientific breakthrough indicates the potential to develop a new breakthrough product. ${ }^{2}$ However, it involves developing new technology that is costly and the outcome is uncertain. If the technology can be developed, the new product may have a significant impact and may result in very high returns on investment. In this case, the initial focus of the new product development is to develop the technology needed and come up with a prototype of the product. In this case, the product development is technology driven.

### 5.4 Idea Generation and Screening [Sub-phase 2]

In Section 2.5.1, we defined the notion of "idea" in the context of new product development. In this section, we look at idea generation, screening of ideas, and discuss the relevant tools and techniques needed for these. We start with customer understanding.

### 5.4.1 Customer Understanding

Customer understanding is very important in the context of new products. According to Ulwick (2002):
"An often heard argument is that asking consumers what they want is useless, because they do not know what they want."

According to Flint (2002):
"Many organizations do not know what kinds of customer information they ought to be collecting, do not have the skills to do so even when they do know, do not have formal processes designed to capture important customer information and/or are in too much of a hurry to move from ideation (i.e., idea generation) and screening to development phases of NPD.
Many of the new products floating around firms these days may be unhelpful at best and harmful at worst because they are internally generated creative ideas not well founded in customer understanding that act more as distractions than sources of meaningful opportunities."

This indicates that understanding customer needs is a challenging problem. Some of the techniques and tools developed to assist in this process are the following:

Customer value determination process: This process is designed to capture deep customer knowledge. ${ }^{3}$

[^0]
[^0]:    ${ }^{2}$ For more on breakthrough products, see Deszca et al. (1999)
    ${ }^{3}$ For more details, see Woodruff and Gardial (1996)."It involves qualitative and quantitative research aimed at identifying customer value dimensions, determining strategically important value dimensions, determining satisfaction with value delivery, exploring value delivery problems, all within the target market segments" (Flint, 2002).
Ethnography and participant observations: Here the focus is on understanding the cultural and sociological meaning inherent in the product usage. This is done through spending extended periods of time with customers to gain deep insights into the customer needs and their usage of the products. ${ }^{4}$
"These ethnographic approaches have yielded successful new product ideas because they tap into what we really mean when we say 'the voice of the customer'" (Flint, 2002).
Quality function deployment (QFD): This approach uses a multi-disciplinary team to determine customer needs and translate them into product design through a structured and well documented framework. ${ }^{5}$

# 5.4.2 Idea Generation 

## Sources

There are several sources for idea generation and these include:

- Suppliers, distributors, sales persons
- Trade journals and other published material
- Warranty claims, customer complaints, failures
- Customer surveys, focus groups, interviews
- Field testing, trial users
- Research and development
- Perceptual maps (visual comparison of customer perceptions)
- Benchmarking (comparing product/service against best-in-class)
- Reverse engineering (dismantling competitor's product to improve the product)


## Tools and Techniques

There are many different tools and techniques that are useful for idea generation. ${ }^{6}$ One of these, that is extensively used, is conjoint analysis.

[^0]
[^0]:    ${ }^{4}$ For more details, see Atkinson and Hammersley (1994).
    ${ }^{5}$ For an interesting historical review of QFD, see Akao (1997). For an introductory discussion of the basic concept, see Hauser and Clausing (1988).
    ${ }^{6}$ These include category appraisal, conjoint analysis, emphatic design, focus group, free elicitation, information acceleration, Kelly repertory grid, laddering, lead user technique, Zaltman metaphor elicitation technique. Creativity enhancement techniques such as brainstorming, lateral thinking, synectics and innovation templates help in idea generation. For further details of these, see Kleef et al. (2005).Conjoint analysis is a systematic approach for matching a new product with the needs and wants of customers. It is a way to understand and incorporate the structure of customer preferences into the new product development process. In particular, it enables us to evaluate how customers make trade-offs between various product attributes and is based on the following assumptions:

- Product/service is realistically decomposable into a set of basic attributes
- New product alternatives can be synthesized from basic alternatives
- Product/service alternatives can be realistically described, either verbally or pictorially

The method involves:

- A numerical assessment of the relative importance that customers attach to different attributes of a product category
- The value (utility) provided to customers by each potential feature of a product


# 5.4.3 Screening of Ideas 

For a manufacturer to assess ideas, (i) they must first be defined to a level of detail that allows valid assessments to be made, and (ii) suitable criteria for evaluating the ideas need to be defined. The criteria involve several factors and these can be divided into several different broad categories as indicated below. ${ }^{7}$

Product related: Technical feasibility, type of technology involved, research and development needed, and fit with product platform and technology strategies
Market related: Demand, meet customer needs, sales, new and existing markets, and so on
Financial related: Investment needed, returns, risks
Business related: Fit with long-term business (corporate, technology, marketing strategies)

## Tools, Techniques, and Models

Many different tools, techniques, and models have been developed to help the screening of ideas. Ozer (1999) surveys the different models and approaches for new product evaluation and some of them are given below.

Analogies: This method uses the historical data of similar products to assess the success of a new product.
Expert opinions: Here, experts provide their opinions about the prospect of a new product.
Purchase intentions: In this method, potential customers evaluate the product to state their intentions whether they will purchase or not.

[^0]
[^0]:    ${ }^{7}$ Udell and Baker (1982) suggest 33 factors grouped into several categories - societal factors, business risk factors, demand analysis factors, market acceptance factors, and competitive factors. See also, Brentani (1986) for further discussion on screening factors.Multi-attribute models: Here, consumers evaluate a product based on description of its attributes to evaluate consumer preferences.
Focus groups: This involves a group of consumers (or experts) in an open and indepth discussion about the new product with a moderator leading the discussions.

Some other well-known methods are (i) idea scoring methods (Kleef et al., 2005) and Analytical Hierarchy Process (Calantone et al., 1999).

# 5.4.4 Outcome of Sub-phase 2 

The outcome of sub-phase 2 is a set of feasible ideas that form the basis for product concept formulation and evaluation.

### 5.5 Product Concept Formulation and Evaluation [Sub-phase 3]

The starting point for sub-phase 3 is a product strategy that is a part of the overall business strategy. This defines the desired performance DP-I at the business level. Each product concept defines product specification SP-I in the front-end phase. Models are required to derive the predicted performance PP-I for each SP-I. PP-I is then compared with DP-I to see if a concept is worth pursuing further. This is an iterative process as indicated in Figure 5.1. In this section, we discuss this process in more detail.

### 5.5.1 Defining DP-I

Once a decision is made to proceed with new product development, the starting point is formulating the new product strategy. This requires addressing the following questions:

- What portfolio of product opportunities should be pursued?
- What should be the timing of product development projects?
- Should any product platforms be shared across the products?
- What technologies should be employed in the products?

The choice of product variants (if there is more than one product) must balance heterogeneity in preference among consumers and the economies of standardization in design and production.

DP-I defines what the new product must achieve for the business and this is stated through business objectives. In other words, DP-I is the desired performance at the business level. The business objective involves several elements that can be broadly grouped into four categories as indicated in Figure 5.3. We discuss the salient features of each of these.

Figure 5.3. Key elements of DP-I and SP-I

# Reputation 

Reputation is a complex entity and relates to issues such as business reputation, product image, customer satisfaction and loyalty, and so on. These in turn have an impact on share value of the business and the sales of new products.

## Customer Satisfaction and Loyalty

Satisfaction (or dissatisfaction) is linked to discrepancy between prior expectations and the actual (or perceived) product performance and product support. A customer is satisfied when performance exceeds expectations. The reverse situation leads to a dissatisfied customer. ${ }^{8}$

Consumers' perceived expectations regarding a product (performance and support) depend on several factors and can include different notions of product quality, value-price concept (a more costly product must perform better), manufacturer's reputation, product advertising, and so forth. This is important as customers do not buy products or services as much as they buy expectation.
"As autos get better, consumers are getting pickier about what they identify as a problem. Many automakers have started to take consumer expectations into account when they set out to design a new model. As a result, new autos today are better vehicles than cars produced just a few years ago." (Evanoff, 2002)

Measuring customer satisfaction/dissatisfaction can be done through a properly designed questionnaire using a scale with discrete levels and ranging from strongly

[^0]
[^0]:    ${ }^{8}$ Most books on consumer behaviour (e.g., Neal et al. (1999)) discuss consumer satisfaction in detail.satisfied to strongly dissatisfied. ${ }^{9}$ Another approach is through critical incidents, that is, events that are out of the ordinary in the mainstream of events that may occur. Such an incident may cause a positive or negative adjustment to a customer's opinion of the product performance or its support services. ${ }^{10}$

The level of dissatisfaction depends on the timing of failure and the dissatisfaction decreases with time. Figure 5.4 shows four scenarios where $W$ corresponds to the instant of warranty expiry.
(a) Failure occurring very soon after purchase resulting in high level of dissatisfaction
(b) Failure occurring within the warranty period but not very soon after purchase resulting in medium level of dissatisfaction
(c) Failure occurring very soon after the warranty has expired resulting in high level of dissatisfaction
(d) Failure occurring well after the warranty has expired resulting in low level of dissatisfaction


Figure 5.4. Dissatisfaction level versus timing of failures

The overall dissatisfaction is the cumulative sum of dissatisfaction from all the failures experienced. Satisfaction and loyalty are closely linked. Satisfaction is necessary, but not sufficient, for loyalty. Loyalty relates to repeat purchases and new purchases through referrals (word-of-mouth effect). According to Gitomer (1998),
"The only way to measure loyalty is by the number of unsolicited referrals and re-orders received by the seller."

Customer loyalty impacts on profits:

[^0]
[^0]:    ${ }^{9}$ Measuring satisfaction for consumer durables is different from that for industrial products. For more details regarding satisfaction with consumer durable products, see Oliver (1996). For industrial products, see Homburg and Rudolph (2001).
    ${ }^{10}$ For more on critical incidents, see Flanagan (1954). Archer and Wesolowsky (1996) use this approach to study consumer response to product performance in the case of automobiles."A 5\% increase in customer retention leads to an increase in profits of 25$95 \%$ over 14 different industry sectors." (Reichheld, 1996)

If customers are dissatisfied either with the product or service quality, then they are more likely to switch.

# Sales and Market Share 

In a monopolistic market (with one single manufacturer), the total sales over the life cycle of a product depend on a number of marketing variables. Variables that have a significant impact on the sales are: warranty, sale price, advertising, product characteristics, quality of product, reputation of the manufacturer, and so forth. In a competitive market (with several manufacturers producing nearly similar products) the marketing variables of the other manufacturers determine the market sales and market share for a manufacturer.

## Revenue

The revenue generated depends on the sales and the sale price. It is obtained as the product of total sales at different sale prices and summing over all different sale prices (in the case where the price changes over the product life cycle).

## Profits and Return on Investment

The profit is given by the difference between the revenue and the costs. There are several kinds of costs and the main costs that are relevant to DP-I in the context of reliability are indicated in Figure 5.3. Other important costs include the marketing costs, financial costs, technology acquisition, and so on.

The investment is the initial capital needed to develop the product, the acquisition of technologies from outside, the setting up of the production facilities and the operating costs until the start of revenue income. The return on investment (ROI) is the ratio of the returns (revenue over the product life cycle) to the investment. We would need to use a proper discounting procedure as the investment is done at the start and the revenue is generated over the product life cycle.

The development and production costs are the costs involved during the development and the production of the product. The warranty costs are the costs associated with the servicing of claims under warranty.

## Illustrative Scenarios

Defining DP-I requires linking product performance to business objectives and stating the constraints. In Section 5.3.3, we indicated four scenarios. In Scenario 1, the DP-I is to ensure that the warranty cost (as a fraction of the sale price) for the new product is below some specified value and that the product development must not exceed some cost limit and the project must be completed within some specified time limit. In Scenario 3, the DP-I is to achieve a certain market share subject to ROI exceeding some specified value.# 5.5.2 Deriving SP-I 

SP-I is defined in terms of target values for product attributes and features (including price) and for product support services (warranty, extended warranty, service contracts) that will achieve the desired business objectives (DP-I). In case of product variety, these need to be defined for each product type. We focus our attention on attributes and features that are relevant in the context of reliability design.

## Warranty

A warranty is a manufacturer's assurance to a buyer that a product or service is or shall be as presented. It may be considered to be a contractual agreement between buyer and manufacturer (or seller) which is entered into upon sale of the product or service. A warranty may be implicit or it may be explicitly stated.

In broad terms, the purpose of a warranty is to establish liability of the manufacturer in the event that an item fails or is unable to perform its intended function when properly used. The contract specifies both the performance that is to be expected and the redress available to the buyer if a failure occurs or the performance is unsatisfactory. The warranty is intended to assure the buyer that the product will perform its intended function under normal conditions of use for a specified period of time.

There are many different types of warranty policies and a classification of these can be found in Blischke and Murthy (1994, 1996). Most standard products are sold with one of the following two warranty policies.

## Free Replacement Warranty (FRW) Policy [Policy 1]

The manufacturer agrees to repair or provide replacements for failed items free of charge up to a time (the warranty period) from the time of the initial purchase. The warranty expires at time $W$ after purchase.

## Pro-rata Rebate Warranty (PRW) Policy [Policy 2]

The manufacturer agrees to refund a fraction of the purchase price should the item fail before time $W$ (the warranty period) from the time of the initial purchase. The buyer is not constrained to buy a replacement item. The refund depends on the age of the item at failure, $T$, and the refund can be either a linear or a non-linear function of $(W-T)$, the remaining time in the warranty period. Let $\psi(T)$ denote this function. This defines a family of pro-rata policies which is characterized by the form of the refund function. The most common form is the linear function given by $\psi(T)=$ $[(W-T) / W] P$ where $P$ is the sale price.

Typical applications of these warranties are consumer products, ranging from inexpensive items such as plastic products to relatively expensive repairable items such as automobiles, refrigerators, and expensive non-repairable items such as electronic products.

Of particular interest in this context is warranty elasticity, that is, the ratio of relative change in total sales to relative change in the length of the warranty period. ${ }^{11}$

[^0]
[^0]:    11 Warranty elasticity for Chrysler is claimed to be 0.143 (Padmanabhan, 1996).# Sale Price 

The total sales over the product life cycle depend on the sale price (for monopolistic market) and on the sale prices of the manufacturer and of the competitors (for competitive market). An increase in the price results in a decrease in the sales rate and the total sales over the product life cycle. The sale price can change over the product life cycle.

## Linking to Concept Development

The notion of concept was discussed in Section 2.5.1. According to Krishnan and Ulrich (2001) concept development involves answering the following questions:

- What are the target values of the product attributes, including price?
- What is the core product concept?
- What is the product architecture?
- What variants of the product will be offered?
- Which components will be shared across which variants of the product?
- What will be the overall physical form and industrial design of the product?

Concept screening is similar to idea screening and is a process to ensure that concepts that are not feasible are screened out. Each product concept defines a SP-I.

### 5.5.3 Evaluating PP-I

PP-I is the predicted performance for a given SP-I and is needed for determining whether or not a selected SP-I (e.g., price, warranty) will achieve the DP-I defined in Section 5.5.1. It involves several elements and these are indicated in Figure 5.5. PP-I is obtained using appropriate models. Model building, in turn, involves data and information and model analysis needs a variety of tools and techniques.


Figure 5.5. Linking SP-I and PP-IA large number of models can be found in the literature and they vary in detail and complexity. We focus on some simple deterministic models. These are adequate for a crude analysis to get mainly qualitative and limited quantitative feel for the implications of different SP-I (the decision variables). We can use more refined (complex and/or stochastic) models to get better predictions and we cite some references where interested readers can get more details of such models. However, building such models requires a lot more data and information.

# 5.5.4 Models 

## Customer Satisfaction/Dissatisfaction Models

One of the roles of warranty is to provide assurance that the product will perform satisfactorily. As such, any failure during the warranty period leads to customer dissatisfaction.

Model 5.1: For non-repairable products sold with relatively short warranty period, a customer becomes dissatisfied should the product fail within the warranty period $W$. In this case the probability that a customer becomes dissatisfied is given by

$$
P_{d}=\operatorname{Pr}(T \leq W)=F(W)
$$

where $F(t)=\operatorname{Pr}(T \leq t)$ is the probability distribution function for the time to product failure.

Model 5.2: For repairable products sold with relatively long warranty period, the dissatisfaction depends on the number of failures encountered by the customer. If the failures are repaired minimally and the repair times are negligible, then failures over the warranty period occur with a ROCOF, $\lambda(t)$ so that the probability that a customer is dissatisfied with the purchase is given by

$$
P_{d}=1-\sum_{k=0}^{n_{0}} \frac{[\Lambda(W)]^{k}}{k!} e^{-\Lambda(W)}
$$

where $\Lambda(t)$ is the cumulative ROCOF and $n_{0}$ is some specified non-negative integer. Comment: When $n_{0}=0$, then $P_{d}=1-\exp [-\Lambda(W)]=F(W)$.

## Sales Models

For certain products, there are no repeat purchases as the product life cycle is comparable to the useful life of the product. In this case, we only need to model the first purchase sales. However, when the useful life is much smaller then the product life cycle, then we need to model both first and repeat purchases.

The sale of a new product depends on product attributes (performance, price, warranty) and marketing efforts (advertising) and many different models have beendeveloped. ${ }^{12}$ We focus our attention on "diffusion type" models to model the effect of price and warranty on first purchase sales. ${ }^{13}$

Model 5.3: [Total first purchase sales with fixed price and warranty]
The total (first purchase) sales, $\bar{Q}$, over the life cycle, $L$, is given by

$$
\bar{Q}=K W^{\alpha} P^{\beta}
$$

where $P$ is the sale price of the product, $K$ is a constant, and $\alpha$ and $\beta$ are the warranty and price elasticities given by

$$
\alpha=\frac{\partial L / L}{\partial W / W} \quad \text { and } \quad \beta=\frac{\partial L / L}{\partial P / P}
$$

$\alpha$ and $\beta$ are obtained from the analysis of earlier (similar) products or based on expert (subjective) judgement.
Model 5.4: [First purchase sales with fixed price and warranty]
The sales rate is given by a first-order differential equation

$$
n(t)=\frac{d N(t)}{d t}=(\bar{Q}-N(t))(a+b N(t)), \quad N(0)=0
$$

where $N(t)$ is the number of sales up to time $t$ and $a$ and $b$ capture the advertising and word-of-mouth effects. The sales until time $t$ is obtained by solving Equation (5.5) and is given by

$$
N(t)=\frac{\bar{Q}\left(1-e^{-\phi\left(t-t_{0}\right)}\right)}{1+(b / a) \bar{Q} e^{-\phi\left(t-t_{0}\right)}}
$$

where $\phi=a+b \bar{Q}$. Note that $\lim _{t \rightarrow \infty} N(t)=\bar{Q}$.
Model 5.5: [First purchase sales with changing price and warranty]
Often the price and warranty terms change over the product life cycle as indicated below.

[^0]
[^0]:    ${ }^{12}$ The sales forecasting models include the following: Box-Jenkins, Customer/Market Research, Decision Trees, Delphi Method, Diffusion Models, Experience Curves, Expert Systems, Exponential Smoothing Techniques, Jury of Executive Opinion, Linear Regression, Looks-Like Analysis (Analogous Forecasting), Market Analysis Models (Atar Model, Assumption Based Models), Moving Averages, Neural Networks, Nonlinear Regression, PreCursor Method (Correlation Method), Sales Force Composite, Scenario Analysis, simulation, Trend Like Analysis. See Kahn (2002) where references can be found to get more details of these models.
    ${ }^{13}$ This is the simple Bass-diffusion model first proposed by Bass (1969). Since then, the basic model has been extended to take into account other factors (e.g., advertising effort, price, negative and positive word-of-mouth effects) Details of these models can be found in Mahajan and Wind (1992).| Period | Interval | Price | Warranty period |
| :--: | :-- | :-- | :-- |
| 1 | $\left[0, T_{1}\right)$ | $P_{1}$ | $W_{1}$ |
| 2 | $\left[T_{1}, T_{2}\right)$ | $P_{1}$ | $W_{2}\left(>W_{1}\right)$ |
| 3 | $\left[T_{2}, \infty\right)$ | $P_{2}\left(<P_{1}\right)$ | $W_{2}$ |

The justification for this is as follows. Purchasers in the first period (also called "innovators") are willing to pay a higher price and take a higher risk. Purchasers in the second period need greater assurance (provided through longer warranty period) and those buying in the third period want a lower price.

The sales rates over the three periods are given by:

$$
\begin{array}{ll}
n(t)=\frac{d N(t)}{d t}=\left(\bar{Q}_{1}-N(t)\right)(a+b N(t)), & N(0)=0 \\
n(t)=\frac{d N(t)}{d t}=\left(\bar{Q}_{2}-N(t)\right)(a+b N(t)), & N\left(T_{1}^{+}\right)=N\left(T_{1}^{-}\right) \\
n(t)=\frac{d N(t)}{d t}=\left(\bar{Q}_{3}-N(t)\right)(a+b N(t)), & N\left(T_{2}^{+}\right)=N\left(T_{2}^{-}\right)
\end{array}
$$

respectively with

$$
\bar{Q}_{1}=K P_{1}^{\alpha} W_{1}^{\beta}, \quad \bar{Q}_{2}=K P_{2}^{\alpha} W_{2}^{\beta}, \quad \text { and } \quad \bar{Q}_{3}=K P_{1}^{\alpha} W_{1}^{\beta}
$$

Note that $N\left(T_{1}^{-}\right)$is the total sales at the end of the first period and $N\left(T_{2}^{-}\right)$is the total sales at the end of the second period. $n(t)$ is a discontinuous function (see, Figure 5.6) but $N(t)$ is a continuous function.


Figure 5.6. Sales rate versus time for Model 5.5

Model 5.6 [First purchase with customer dissatisfaction and negative word-of-mouth effect]
Dissatisfied customers can influence potential customers in not buying the product. This is captured through lost customers. Let $S(t)$ denote the number of lost customers by time $t$ and let $s(t)$ denote the customer loss rate. Then

$$
s(t)=\frac{d S(t)}{d t}=(\bar{Q}-S(t)-N(t))\left(\xi P_{d} N(t)\right), \quad S(0)=0
$$where $\zeta$ is a parameter characterizing the impact of negative word-of-mouth. The sales rate is given by

$$
n(t)=\frac{d N(t)}{d t}=(\bar{Q}-S(t)-N(t))\left(a+b\left(1-P_{d}\right) N(t)\right), \quad Q(0)=0
$$

The first purchase sales stop at time $\hat{t}$ given by

$$
(\bar{Q}-S(\hat{t})-N(\hat{t}))=0
$$

The fraction of customers lost is given by $S(\hat{t}) / \bar{Q}$ and the fraction of customers who have bought the product is given by $N(\hat{t}) / \bar{Q}$. The critical parameters are (i) $\zeta$, with larger value implying a higher loss of customers and (ii) $P_{d}$, reflecting the impact of product unreliability.
Model 5.7 [Repeat purchase sales]
This is relevant only when the useful life of the product is smaller than the length of the product life cycle. Let $v_{j}$ denote the probability that a customer who has bought the product for the $j$ th time buys the product again when the purchased item reaches the end of its useful life. An upper limit on the number of repeat purchases is given by the largest integer less than $L / T$. Let $n_{j}(t)$ denote the sales rate for the $j$ th purchase. Then

$$
n_{j+1}(t)=\frac{d N_{j+1}(t)}{d t}=v_{j} n_{j}(t-T) \text { for } j T \leq t<L ; \quad j \geq 1
$$

with the first purchase sale rate given by $n(t)=n_{1}(t)$.

# Cost Models 

The cost elements of relevance in the context of reliability design are (i) warranty costs, (ii) development costs, and (iii) production costs. The modelling of these costs poses challenging problems and a discussion of this can be found in Asiedu and Gu (1998) and Layer et al. (2002).

The warranty servicing cost depends on the product reliability and the warranty servicing strategy. We discuss two simple models. The development cost depends on the complexity and the degree of innovation needed and is discussed in Chapters 6 and 7. The production cost depends on the complexity of the product and the quantities produced, with the production cost per unit coming down as the quantity produced increases. This topic is discussed further in Chapters 6 and 8.
Model 5.8 [Warranty cost - free replacement warranty (FRW) policy]
If the failures are repaired minimally and the repair time is negligible, then failures over the warranty period occur according to a ROCOF with intensity function $\lambda(t)$. Let the (average) cost of a repair be $C_{r}$. Then, the expected warranty cost per unit is given by

$$
c_{W}=C_{r} \int_{0}^{t_{w}} \lambda(t) d t=C_{r} \Lambda(W)
$$

The total expected warranty cost (with total sales $N(L)$ ) is given by

$$
C_{W}(\theta)=N(L) c_{W}=N(L) C_{r} \Lambda(W)
$$Comment: The cost changes if we use imperfect repair instead of minimal repair.
Model 5.9 [Warranty cost - pro-rata rebate warranty (PRW) policy]
The expected warranty cost per unit is given by

$$
c_{W}=\int_{0}^{W} \psi(x) f(x) d x
$$

where $\psi(x)=(W-x) / W$. The cost models for many other types of warranties can be found in Blischke and Murthy (1994).

The total expected warranty cost (with total sales $N(L)$ ) is given by

$$
C_{W}(\theta)=N(L) c_{W}
$$

# Model Parameters 

Numerical values must be assigned to the model parameters in order to carry out quantitative analysis. This requires appropriate data and information. Unfortunately, the data and information available in the front-end phase are rather limited. There are three approaches to determining the values to be assigned to the model parameters.

## Approach 1 [Analogy-based]

Data for similar earlier products, past development programmes, and production costs is used to estimate model parameters. We can either use these estimates directly or after suitable modification to reflect the changed conditions for the new product.

The sales data for the current product are used to estimate the parameters of the diffusion model for the current product. The parameters for the sales model for the new product might need to be modified if the advertising effort differs significantly from that for the earlier product.

For the production and development cost model parameters, we can use data from several earlier or similar products. The cost versus the reliability can be plotted and extrapolated to obtain the cost estimates for the new models. For more on design effort costs, see Bashir and Thomson (2001) and the references cited therein.

## Approach 2 [Expert opinion]

Here, information is sought from several experts using techniques such as the Delphi method. Most books on technology forecasting deal with this and many other methods (Martino, 1992). The costs to achieve different reliability targets or market sales under different price and warranty combinations can, for example, be obtained using this approach. The challenge is to identify a pool of experts who are qualified to provide sensible information.

## Approach 3 [Subjective]

When data and information are very limited, the model builder has to make some guesses - either point estimates or interval estimates for some of the parameters.# 5.5.5 Outcome of Sub-phase 3 

The outcome of sub-phase 3 is the final SP-I (target values for the attributes characterizing product performance and product support) for which PP-I matches DP-I.

### 5.6 Specialized (Custom-built) Products

Characteristics common to almost all custom-built products include the following:

- Complex product (involving either existing or new technologies)
- Clearly defined product performance (reliability and non-reliability related) targets either specified by the customer or jointly negotiated by the manufacturer and the customer
- Evaluation of product performance during manufacture and in field operation
- Design changes if performance targets are not achieved in field operation
- A contract between the customer and the manufacturer (often referred to as "contractor")
- Cost to the buyer

The process for the front-end phase for custom-built products is shown in Figure 5.7, where PP-I(c) is the predicted performance from the customer perspective and PP-I(m) is the predicted performance from the manufacturer perspective. In this section we discuss briefly the different elements of the figure.

### 5.6.1 Performance Requirement

Deciding on the product performance requirements (also referred to as "customer requirements") is an iterative process as indicated in Figure 5.8. Typically, the customer (buyer) sends out a request proposal to one or more manufacturers indicating the performance requirements for the new product along with other information needed to prepare a bid on the project. ${ }^{14}$ Manufacturers respond through an initial bid proposal that indicates how the new product can be realized and gives some indication of the performance levels and crude estimates of various costs (e.g., development, production, operation). This is done using crude models based on limited data. The buyer carries out an evaluation of the proposals and decides on which ones are to be rejected and considers possible revisions to the performance requirements based on the bid proposals. The proposals not rejected go through a second stage where the process is repeated. This iteration continues through one or more iterations until one manufacturer is selected and both buyer and the manufacturer are in agreement regarding performance and costs. The end outcome is the final contract for the manufacturing of the product.

[^0]
[^0]:    14 The manufacturer is often referred to as contractor when the manufacturer is awarded the contract to build the product.

Figure 5.7. Stage I, level I process for custom-built products

Example 5.1 (Safety Instrumented System). Consider a separator on an offshore oil/gas platform in the North Sea. The hazards related to the separator are usually determined through a hazard and operability (HAZOP) study. For each significant hazard, protective features have to be considered. One such hazard is too high pressure in the separator. The risk related to this hazard can be reduced by installing pressure relief valves on the separator. If this protection is not sufficient, we may consider including an instrumented shutdown function on the inlet pipeline. This function is called a safety instrumented function (SIF) and this function has to be implemented through a safety instrumented system comprising one or more pressure sensors/transmitters, a logic solver, and one or more shutdown valves. The reliability requirements to the SIF are specified as a safety integrity level (SIL) that can take four different values. The SIL value may be determined from the overall risk acceptance criteria of the platform, and/or by different SIL allocation methods.

If, for example, SIL 3 is found to be required, a range of more specific requirements are specified in the standard IEC 61508. These imply that the probability of

Figure 5.8. Performance requirements for custom-built products
failure on demand (PFD) must be less than $10^{-3}$ (see Chapter 4) and that the hardware fault tolerance of the system must be according to tables given in IEC 61508. In addition to the SIL 3 requirements, the customer (i.e., the oil company) will also have a set of additional requirements related to spurious trip rate, testability, space and cost constraints. Requirements are negotiated with the manufacturer and a safety requirement specification (SRS) is agreed.

As illustrated in Figure 5.8, detailed models and data need to be used to calculate the system PFD and the various other requirements. Some of these models are indicated in Chapter 4.

# 5.6.2 Contract 

The contract defines the target values for the performance of the product and the constraints. These include both reliability- and non-reliability-related performances. If the objective of the contract is only to ensure that the product performance meets some minimum level, then it is an assurance contract. In this case, the aim of product development is to ensure that the specified level is achieved. In contrast, in some cases the buyer is interested in encouraging the contractor to exceed the minimum level and as such, the contract includes incentive features to achieve this. This is accomplished by tying the payment to the performance level achieved by the manufacturer. The customer is actively involved throughout the product life cycle and the focus is on the total life cycle.

The reliability, maintainability and supportability performance terms may include one or more of the following items:- A guaranteed mean time between failure (MTBF)
- A guaranteed turnaround time for repaired or replaced units
- A supply of consignment spares for use by the buyer at no cost until the guaranteed MTBF is demonstrated
- Accuracy of testability (built-in test (BIT) and other tests)
- A guaranteed system availability (point availability and/or interval availability)

The performance of the product must be defined properly so that there is no scope for ambiguity. Reliability-related performance needs to include the time frame for data collection, the type of data to be collected, and the procedures to assess performance in terms of the data. In the case of MTBF, we must specify whether a point or interval estimate is to be used. Similarly, during development the contract needs to indicate the kind of testing to be carried out and how to translate the test data into assessing performance at component, sub-system or system level. If these are not done properly, it can lead to disputes and litigation at a later time.

# 5.6.3 Reliability Improvement Warranty 

The reliability improvement warranty (referred to as RIW) is a class of warranty policies that are applicable for custom-built products. The intent of an RIW is to provide an incentive to the manufacturer to improve the reliability of the product, thereby reducing long-run repair and maintenance costs for the customer.

The first use of this type of warranty was in purchases of aircraft by commercial airlines. ${ }^{15}$ In military procurement in the United States, the RIW was initially called a "failure free" or "standard" warranty (Trimble, 1974). Some versions of this warranty had been introduced at about the same time as the inception of the airline RIW (Gregory, 1964; Klause, 1979). ${ }^{16}$ The RIW came into wider use during the next several years with a guaranteed MTBF as the predominant feature (Gandara and Rich, 1977) and is now firmly established as a factor in defence acquisition by the US Government. It is also finding greater acceptance in the context of complex industrial and commercial transactions.

The warranty statement addresses one or more of the following questions:

- What is the duration of the warranty period?
- Is it an assurance or incentive warranty?
- What are buyer and contractor obligations?
- What issues are covered?
- What are the exclusions?
${ }^{15}$ The successful use of an RIW by Pan American World Airways in the purchase of Boeing 747s in the late 1960s is discussed in Hiller (1973) and Schmoldas (1977).
${ }^{16}$ The first actual use of an RIW, in 1967, was in procurement of a gyroscope for the F111 aircraft. This warranty included a guaranteed MTBF provision, and it was apparently quite successful, with the target MTBF of 400 hours exceeded (the estimated actual MTBF was 531 hours) and a $40 \%$ reduction in maintenance costs per operational hour achieved (Schmidt, 1976).- How are the spare parts issues addressed? Are they delivered at the start or over the operating life cycle of the product?

Note that this is not an exhaustive list and there may be many other questions. The following RIW policy is from Gandara and Rich (1977). ${ }^{17}$
"Under this policy, the manufacturer agrees to repair or provide replacements free of charge for any failed parts or units until time $W$ after purchase. In addition, the manufacturer guarantees the MTBF of the purchased item to be at least $M$. If the computed MTBF is less than $M$, the manufacturer will provide, at no cost to the buyer, (1) engineering analysis to determine the cause of failure to meet the guaranteed MTBF requirement, (2) engineering change proposals, (3) modification of all existing units in accordance with approved engineering changes, and (4) consignment spares for buyer use until such time as it is shown that the MTBF is at least $M$."

# 5.6.4 Idea Generation and Screening 

The idea generation is similar to that for standard products discussed in Section 5.4. The screening would be different and needs to be done using criteria that involve customer requirements as well as the business objectives of the manufacturer.

### 5.6.5 DP-I

For the manufacturer, as with standard products, DP-I deals with the performance of the product from a business perspective. DP-I can involve one or more of the following variables:

- Costs
- Profits
- Risks
- Outsourcing
- Reputation

One needs to take into account various constraints such as

- Investment needed
- Time
- Expertise needed

We briefly discuss some of these.
${ }^{17}$ Blischke and Murthy (1994) discusses several other types of RIW policies.# Costs 

There are several different types of costs involved. These include the following:

- Development cost
- Production cost
- Support cost (for spares, etc.)
- Warranty cost

The manufacturer needs to take into account all of these costs in the pricing of the contract. The warranty cost must include the provision of replacements, repairs, as well as upgrades. This depends on the duration and other terms of the warranty. Models are needed to predict these costs.

From the buyer's perspective, the cost of interest is the total life cycle cost (LCC). Figure 5.9 indicates the different elements of the LCC.

## Risks

The manufacturer faces several kinds of risk. These include the following:

- Technical risk: This results from not achieving the performance levels stated in the contract and, as a consequence, incurring a large penalty through high warranty costs and/or high cost of engineering design modifications
- Project risk: This results from not delivering the product in time and/or cost overruns during development and production
- Risks associated with outsourcing

These risks can be assessed through a proper scenario analysis where we look at alternative scenarios and assess the probabilities of these occurring and the resulting consequences.

## Outsourcing

Outsourcing can be defined as a process of transferring activities to be performed by others and its main advantage is conceptually based on two strategic considerations:

1. Use of internal resources mainly for the core competencies of the business.
2. Outsourcing of all other activities that are not considered strategic necessities and/or whenever the manufacturer does not possess the adequate competencies and skills.

Complex products require several different kinds of expertise and it is very rare that a manufacturer will have all the skills and competencies needed.

### 5.6.6 SP-I

SP-I defines alternative product concepts and options for building. Different concepts arise due to a multitude of factors and technologies, product architecture, and so on. The options can include outsourcing the design and/or manufacture of one or more of the sub-systems.

Figure 5.9. Components of life cycle cost# 5.6.7 PP-I 

There are two different types of PP-I. The first is PP-I (c) - the customer perspective and the second is PP-I (m) - the manufacturer's perspective.
$P P-I(c)$ : Here, we assess the predicted product performance in terms of the performance variable defined in the customer requirements. If PP-I (c) does not match the customer requirements, we must iterate back and consider a new SP-I. If there is no more SP-I options available, then the exercise comes to an end as the manufacturer is unable to come up with a concept to meet the customer requirements. If PP-I (c) matches the customer requirements, then we need to evaluate the match between PP-I (m) and DP-I.
$P P-I(m)$ : Here, we assess the predicted product performance in terms of the performance variables defined in DP-I. If PP-I (m) does not match DP-I, then the exercise is terminated as it is not in the interest of the manufacturer to proceed further. If PP-I (m) matches DP-I, then the manufacturer tenders for the job.

Many different types of models are needed to evaluate PP-I(c) and PP-I(m). Some of these (involving product reliability) are discussed in Chapter 6.

### 5.6.8 Outcome of Phase 1

If the tender is accepted, the manufacturer and the customer sign a contract. This forms the starting point for the next phase of the process.

## Contract Document

This is a legal document between buyer and manufacturer to ensure that the manufacturer delivers the desired product. To prevent possible misunderstanding between the two parties (relating to reliability aspects) it is important that the contract deals with the following issues:

- Product performance requirements
- Definitions
- Documentation requirements
- Quality control requirements
- Work schedules
- Testing for reliability assessment and verification
- Data collection and analysis

These should be done in an unambiguous manner and should be complete. A proper drafting of such a contract requires a team comprising lawyers, engineers, reliability experts, and managers.# Dispute Resolution 

In most cases, the product as well as the contract are complex. This implies that the contract might not address some issues that can lead to potential problems and disputes after the contract has been signed. Also, the interpretation of the contract (e.g., the testing conditions or operating environment) and other unverifiable factors (e.g., the cause of failure being either due to operator error or design weakness) can lead to possible conflicts. As such, both parties (buyer and manufacturer) need to look at alternative dispute resolution mechanisms as part of the contract.

### 5.7 Implications for Product Reliability

For standard products, product reliability does not appear explicitly in the decision making at the front-end phase. However, many of the variables (warranty costs, development costs, maintenance costs, customer satisfaction) are related to product reliability as will be indicated in the next chapter. In the case of custom-built products, product reliability appears explicitly through various performance measures (e.g., reliability, MTBF) and indirectly through variables such as development cost, LCC, and so on. SP-I and the elements of DP-I (and the constraints) are the inputs to stage II and define DP-II. From this we first decide on product reliability (at the system level) and then decide on component level reliability in the next chapter.

### 5.8 Case Study: Cellular Phone

As indicated in Section 1.1, the drivers for new product development can be one or more of the following:

1. Advances in technology
2. New (real or perceived) customer needs
3. Competitor's action

In this section, we look at the advances in technology and the changing customer needs.

## Advances in Technology

The different elements of a cellular phone are indicated in Section 2.2.3 (Example 2.2).

Integrated circuits: Walsh et al. (2005, Table 1) defines seven epochs based on disruptive and sustaining technology changes in silicon ICs. The increase in the number of gates, bits, or transistors per device is from this source is given in Table 1.1. The changes in (i) device (SSI $\rightarrow$ MSI $\rightarrow$ LSI $\rightarrow$ VLSI $\rightarrow$ ULSI $\rightarrow$ UULSI), (ii) dominant design and production processes (Growth junction $\rightarrow$ Bipolar $\rightarrow$ Bipolar MOS$\rightarrow$ PMOS $\rightarrow$ NMOS $\rightarrow$ CMOS $\rightarrow$ BiMos), (iii) Technological substitutes for silicon (Germanium $\rightarrow$ FZ $\rightarrow$ GaAs SOS $\rightarrow$ Denuded silicon GaAs, SOI GaAs) (iv) semiconductor device product drivers (Transistors, diodes $\rightarrow$ Transistor amplifiers $\rightarrow \mathrm{A} / \mathrm{D}$ devices $\rightarrow$ Logic RAM $\rightarrow$ EPROM), diameter of silicone substrate (from $<$ 2 inches to 6-14 inches) and (v) critical dimension in microns (going down from 10 microns to less than 1 micron).

Display technologies: In addition to the advances in the liquid-crystal display (LCD) there are new alternative technologies, such as the reflective bistable display technologies and the organic emissive displays (OEDs). Kimmel et al. (2002) deal with this topic and the drawbacks of OEDs in the context of cellular phones. From the reliability perspective, the main drawback is the variations in the lifetime of different colour emitters and the long-term reduction in quality. ${ }^{18}$

Batteries: Currently, cellular phones use batteries (lithium, cadmium, nickel, etc.) that need to be recharged (after usage of around 4 hours) and the life (defined through the energy capacity dropping to $80 \%$ of the rated) is typically around 2000-3000 hours. Atkinson (2005) reports that the advances in fuel cell technology give life lengths exceeding 5000 hours. This will likely result in batteries being replaced by fuel cells in the future.

# Customer Needs 

New features to satisfy the ever increasing customer needs have resulted in continuous improvements in the picture resolution, increase in memory for MP3 players and video downloading. A survey in 2005 reported that $53 \%$ are comfortable listening to music on their cellular phones and $38 \%$ are comfortable watching TV or movies.

## Customer Choice

Given the wide range of cellular phones available on the market, the selection of cellular phone is a topic that has received some attention. Isiklar and Buyukozkan (2007) propose a multi-criteria decision making (MCDM) approach to model consumer evaluation of cellular phone alternatives. It uses an Analytical Hierarchy Process (AHP) to determine the relative weights of evaluation criteria and an extension of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) to rank the cellular phone alternatives. They look at two criteria (product related and user related) and three sub-criteria for each.

[^0]
[^0]:    ${ }^{18}$ Szweda (2006) discusses this topic and reports that the drawback associated with the blue colour emitter has been overcome. This implies that the organic light-emitting diodes (OLEDs) will impact on the sales of light emitting diodes (LEDs).# Performance and Specification during Design 



### 6.1 Introduction

This chapter deals with reliability performance and specification during phase 2 (stage I, level II) and phase 3 (stage I, level III) of the product life cycle. In phase 2, the focus is on deriving the technical specifications at product level, that will ensure that the product achieves the objectives defined in phase 1 . The design process involves looking at the technical specifications in ever increasing detail as we proceed from the product level down to the component level. This is the focus of phase 3 where we derive the reliability specifications at the component level and approaches to achieve these.

The outline of the chapter is as follows: Section 6.2 deals with product level specification for standard products, and Section 6.3 with specialized products. Section 6.4 deals with the modelling of some of the elements needed for building meta-models to derive SP-II (the overall product reliability). An illustrative case of such a metamodel is discussed in Section 6.5. Sections 6.6 to 6.8 deal with component level specification for both standard and specialized products. In Section 6.6, we indicate the process involved in phase 3 . Section 6.7 looks at approaches to ensure that the required component level reliabilities are achieved. Section 6.8 discusses the outcomes of phase 3 and these serve as inputs for phase 4 . In Section 6.9 , we discuss issues related to the case study on cellular phones.

### 6.2 Phase 2 for Standard Products

The aim of phase 2 is to derive the overall product reliability SP-II that will ensure that the objectives of phase 1 are achieved. This requires one first to define the desired performance DP-II. To obtain SP-II is an iterative process, as illustrated in Figure 6.1. It involves comparing the predicted performance PP-II with DP-II, and based on the outcome, we either iterate back or proceed to phase 3 as shown in Figure 6.1.

Figure 6.1. Reliability specification at product level (phase 2)

# 6.2.1 Defining DP-II 

The desired performance DP-II is generally a vector with several elements. To define DP-II requires a thorough understanding of the relationship between product reliability (SP-II) and the many other variables in the new product development, some of which we discussed in earlier chapters. Figure 6.2 shows some of these variables and their relationship to product reliability. As can be seen, the relationships can be either direct (first level interaction) or indirect (second or third level interactions).


Figure 6.2. Influence of product reliability on business objectivesThe elements of DP-II are obtained in terms of the elements of DP-I and SP-I. Some of these elements define the objective function for deriving SP-II and others define the constraints that need to be satisfied. This is illustrated by the following two scenarios.

# Scenario 1 

The product market is competitive with several manufacturers producing nearly identical (from a functional point of view) products and the warranty is determined by the legislation. This implies that the price and the warranty terms are not decision variables. The manufacturer may choose to focus on reputation and profits so that these are the two elements of the business objective in phase 1 . The objective function for phase 2 may be to minimize the development, production, and warranty costs and to maximize the customer satisfaction. These will then define DP-II. The specification SP-II needs to be selected to ensure that the stated DP-II is achieved, and at the same time, such that specified constraints are satisfied. A constraint may, for example, be that the development and/or warranty costs do not exceed specified values.

## Scenario 2

The manufacturer is a monopolist and the price and warranty are the decision variables of phase 1 (SP-I) that are selected to achieve some business objectives DP-I in phase 1. Constraints in phase 1 may be that the warranty cost does not exceed a specified value and that the customer satisfaction is above some specified value. In this case, in phase 2 the objective function is the same as in phase 1 so that DP-II = DP-I and SP-II is selected to achieve this and to satisfy the constraints of phase 1.

### 6.2.2 Deriving SP-II

SP-II is the overall product reliability. It can be characterized in one of several different ways. For complex repairable products, the characterization through ROCOF is often the most appropriate. The form of the ROCOF needs to be specified. Here again, there are several options.

## Option1: [Stylized form of ROCOF]

Let the ROCOF function $\lambda(t ; \theta)$ be as shown in Figure 6.3. This is a very stylized form where the parameters of the ROCOF function are given by the set $\theta=\left(\theta_{1}, \theta_{2}, \theta_{3}\right)$. The ROCOF is constant until time $\theta_{1}$ and increases linearly after this point of time. The useful life is the time period over which the ROCOF is below some specified limit, and is $\geq \theta_{1}$. The reliability of the product increases as $\theta_{1}, \theta_{2}$ and/or $\theta_{3}$ increases.

Figure 6.3. ROCOF function (stylized form)

# Option 2: [Weibull ROCOF] 

The ROCOF function is given by

$$
\lambda(t ; \theta)=\frac{\beta}{\alpha^{\beta}} t^{\beta-1}
$$

The parameters are given by the vector $\theta=(\alpha, \beta)$, where $\alpha(>1)$ is the scale parameter and $\beta$ is the shape parameter of the ROCOF. The product reliability increases as $\alpha$ increases and/or $\beta$ decreases.

For a non-repairable product, the most appropriate characterization is the survivor function $R(t ; \theta)$ and here we can choose from a wide range of life distributions, including the exponential and the Weibull distributions.

## Comments:

1. The ROCOF (survivor) function is the nominal function used for making decisions in phase 2. The actual ROCOF (survivor) function will differ from the nominal function. However, if the actual ROCOF (survivor) function is lower (higher) than the nominal function, then the required reliability performance is assured.
2. We will use both the stylized and the Weibull forms of the ROCOF. The advantage of the Weibull form is that it is analytically more tractable.

## Decision Variable

Let $y$ denote the decision variable of the reliability design process in phase 2. Depending on the context, it can be one or more parameters of the nominal ROCOF (survivor) function as indicated by the following illustrative cases.
Case 1: The product is a high-tech product with short life cycle. In this case, the customer keeps the product for a relatively short period $L$ before replacing it. The decision variable $y$ is a vector given by $\left(\theta_{1}, \theta_{2}\right)$. The parameter $\theta_{2}$ needs to be above some specified value (to ensure a minimum customer satisfaction, such that the fraction of customers who experience no failure is greater than some specified value) and $\theta_{1}=L$.Case 2: The product has a long useful life and a long life cycle. In this case, the decision variable $y$ is a vector given by $\left(\theta_{1}, \theta_{2}, \theta_{3}\right)$. These parameters need to be selected to optimize some objective function (DP-II) and to satisfy constraints defined in phase 1.

# Usage Rate 

The usage rate defines the intensity of usage. For example, in the case of a washing machine, it is the average number of washes per week; for a photocopier it is the throughput or volume of copies made per unit time (average number of pages printed per day or week); and for an automobile, it is the average distance travelled per time unit (e.g., kilometres per year). For some products, the usage rate $u$ can vary significantly across the customer population and can be characterized through a usage rate density function $g(u)$ for $u \in\left[u_{1}, u_{2}\right)$ as indicated in Figure 6.4, where $u_{1}$ and $u_{2}$ are the lower and upper limits of usage rate.


Figure 6.4. Usage rate and ROCOF

Let $\bar{Q}$ denote the total potential customer population. Then the fraction of customers with usage rate in the interval $[u, u+\delta u)$ is given by $g(u) \delta u$ and the number of customers with usage rate in the same interval is given by $\bar{Q} g(u) \delta u$.

A product is designed for a nominal usage rate $x$, for example, $x=10$ washes per week in the case of a washing machine. If the product is operated with this usage rate, the ROCOF is given by $\lambda_{0}(t ; x, y)$ where $y$ is the reliability decision variable discussed earlier. The nominal usage rate $x$ can be viewed as an indicator of the "sturdiness" (or robustness) of the product and $y$ can be viewed as an indicator of "inherent reliability" - the reliability when the product is operated at the nominal usage rate. The product is less (more) sturdy as $x$ moves to the left (right) in Figure 6.4.

The rate of the product degradation increases with the usage rate $u$. Customers with usage rate $u>x$ (represented by the area under the curve to the right of the vertical line through $x$ in Figure 6.4) will have more failures (in a statistical sense) compared with those with $u<x$ (represented by the area under the curve to the left of the vertical line through $x$ ). This has implications for reliability design. Let $\lambda(t ; x, y, u)$ denote the ROCOF function for a product designed with nominal usage rate $x$ but operated at usage rate $u$ and the reliability decision variable $y$. Thisfunction is related to the inherent ROCOF $\lambda_{0}(t ; x, y)$ and is important in reliability design for products where the usage rate varies across the population.

Note. If the usage rate does not vary significantly or the variations do not affect the rate of the product degradation, then we only need $\lambda_{0}(t ; x, y)$ and not $\lambda(t ; x, y, u)$ in the reliability design in phase 2 .

# Product Variety 

When the needs vary significantly across the customer population, achieving the business objectives with a single product design might not be possible. In this case, the optimal strategy is to offer a variety of products using a common product platform. Product variety is achieved through variations in the attributes and/or characteristics. ${ }^{1}$

In the context of product reliability, product differentiation occurs when two products differ in terms of $x$ and/or $y$ as the reliability is a function of both $x$ and $y$. A higher value of $x$ implies a more robust (or sturdy) design and a higher value of $y$ implies a more reliable product.

The decision problem in phase 2 is (i) to determine whether or not to have product variety, and (ii) to choose the values for $x$ and $y$ for each product.


Figure 6.5. Linking PP-II and SP-II

### 6.2.3 Evaluating PP-II

Evaluating PP-II requires models that link SP-II to PP-II. The models needed depend on the elements of DP-II, some of which are indicated in Figure 6.5. Models for some elements are discussed in Chapter 5 and these need to be extended to address some of

[^0]
[^0]:    ${ }^{1}$ There is a vast literature on product variety and these deal with many different issues, see for example, Clark and Fujimoto (1991); Wheelwright and Clark (1992); Erens and Hegge (1994); Meyer et al. (1997); Prasad (1998); Chakravarty and Balakrishnan (2001); Salvador et al. (2002); Fujita (2002).the new issues (such as usage rate) discussed in the earlier sub-section. New models for some of the elements are discussed in the next section. These models need to be linked together to define a meta-model to decide on SP-II (product reliability).

# 6.3 Phase 2 for Custom-built Products 

The processes for obtaining the specifications for custom-built products in phase 2 are shown in Figure 6.6. The starting point is the customer requirements (DP-II=SPI) and from this the overall product reliability SP-II is obtained in a manner similar to phase 2 for standard products. DP-II can include variables, such as life cycle cost, availability, and so forth, and we need models to obtain the predicted performance for a given specification.


Figure 6.6. Deriving specifications for custom-built products# 6.4 Models 

The decision variables that need to be selected as part of SP-II are the variables $x$ and $y$. These variables define the inherent reliability and are characterized by the ROCOF function $\lambda_{0}(t ; x, y)$. The effect of the usage rate is characterized through the ROCOF function $\lambda(t ; x, y, u)$. In this section, we look at models for the elements of PP-II with these two decision variables.

## Model 6.1 [Variation in usage rate]

The usage rate is modelled by a density function $g(u)$ for $0 \leq u_{1} \leq u<u_{2} \leq \infty$. The density function can be uni-modal or multi-modal.

## Model 6.2 [Effect of usage rate on ROCOF]

If the actual usage rate is higher (lower) than the nominal usage rate, the rate of degradation is faster (slower). We model this as follows:

$$
\lambda(t ; x, y, u)=\lambda_{0}(t ; x, y) \cdot\left(\frac{u}{x}\right)^{\gamma}
$$

with $\gamma \geq 0$.

## Comments:

1. The model in (6.2) is similar to the accelerated failure time model discussed in Section 4.4.4
2. When $u=x$, we have $\lambda(t ; x, y, u)=\lambda_{0}(t ; x, y)$ as expected.

## Model 6.3 [Product failures]

If the product is used at the nominal design usage rate $x$, then the expected number of failures in the interval $[0, t)$ is given by the cumulative ROCOF function

$$
\Lambda_{0}(t ; x, y)=\int_{0}^{t} \lambda_{0}\left(t^{\prime} ; x, y\right) d t^{\prime}
$$

If the product is used with usage rate $u$, then the expected number of failures in $[0, t)$ is given by

$$
\Lambda(t ; x, y, u)=\int_{0}^{t} \lambda\left(t^{\prime} ; x, y, u\right) d t^{\prime}
$$

## Model 6.4 [Development cost]

The development cost is generally an increasing function of both $x$ and $y$. A possible model for the development cost $C_{D}$ is given by

$$
C_{D}(x, y)=\Psi_{0}+\Psi_{1} y^{\varepsilon} x^{\nu}
$$

with $\varepsilon>1$ and $v>1$.# Model 6.5 [Warranty cost] 

The product is sold with a free replacement warranty (FRW) policy with warranty period $W$. For a given usage rate $u$, the (conditional) expected warranty cost per unit (based on Model 6.2) is given by

$$
C_{W}(x, y \mid u)=C_{r} \int_{0}^{W} \lambda_{0}(t ; x, y) \cdot\left(\frac{u}{x}\right)^{y} d t
$$

where $C_{r}$ is the average cost of a repair. The number of customers with usage rate in the interval $[u, u+\delta u)$ is given by $\bar{Q} g(u) \delta u$ where $\bar{Q}$ is the total sales. As a consequence, the total expected warranty cost $C_{W}(x, y)$ is given by

$$
C_{W}(x, y)=\bar{Q} \int_{u_{1}}^{u_{2}} g(u)\left[C_{r} \int_{0}^{W} \lambda_{0}(t ; x, y)\left(\frac{u}{x}\right)^{y} d t\right] d u
$$

### 6.5 An Illustrative Case

This case corresponds to a competitive market with several manufacturers. As a result, the price of the product is determined by the market outcome resulting from the interaction between manufacturers and customers and is not a decision variable. Similarly, sometimes the legislators set the minimum warranty period (e.g., EU enacting that products have two years base warranty) and manufacturers decide to sell their products with this minimum warranty so that warranty is also not a decision variable.

For a given warranty period, the warranty costs depend on the reliability (or ROCOF ) and this cost can be reduced by higher values for $x$ and/or $y$. However, this is achieved at the expense of higher development cost. The goal is to select $x$ and/or $y$ (decision variables) to minimize the total cost (objective function). We first consider the case of a single product so that there is no product variety. Later, we consider the case of two products resulting in product variety to meet the different usage rates.

## Comments:

1. There can be one or more constraints, for example, that the total development cost must be less than some specified value, the warranty cost must be below some specified value, and so on. We assume that there are no constraints other than $y$ to assume values within the limits for the usage rate.
2. The objective function can include other measures such as customer satisfaction but this would correspond to a different scenario.

### 6.5.1 Option 1 [No Product Variety: Single Design]

Since there is only a single product, the reliability design involves deciding on two variables - the usage rate $x$ and a parameter $y$ of the ROCOF. The meta-model to obtain the optimal values for the decision variables involves three models and these are shown in Figure 6.7.

Figure 6.7. Meta-model for the illustrative example

# Objective Function and Optimal Decision 

The objective function $J(x, y)$ is the sum of the development cost and the total expected warranty costs and is given by

$$
J(x, y)=C_{D}(x, y)+C_{W}(x, y)
$$

Using (6.7) in (6.8) yields

$$
J(x, y)=C_{D}(x, y)+\widetilde{Q} \int_{u_{1}}^{u_{2}} g(u)\left[C_{r} \int_{0}^{W} \lambda_{0}(t ; x, y)\left(\frac{u}{x}\right)^{\gamma} d t\right] d u
$$

The optimization problem is to minimize $J(x, y)$ subject to the constraint $u_{1} \leq$ $x \leq u_{2}$ and $y>0$, and any other constraint, such as a specified upper limit for the development cost, $C_{D}(x, y) \leq \widetilde{C}$. We illustrate through an example.

Example 6.1. The ROCOF with usage rate $u$ is given by the Weibull ROCOF so that

$$
\lambda(t ; x, y, u)=\left(\frac{u}{x}\right)^{\gamma} \frac{\beta t^{\beta-1}}{y^{\beta}}
$$

Let the design cost be given by (6.5). Using this and (6.10) in (6.7) yields

$$
C_{W}(x, y ; W)=\frac{\Psi_{2}}{y^{\beta} x^{\gamma}}
$$

with

$$
\Psi_{2}=\widetilde{Q} C_{r} W^{\beta} \int_{u_{1}}^{u_{2}} u^{\gamma} g(u) d u
$$

Using (6.5) and (6.11) in (6.8) yields$$
J(x, y)=\Psi_{0}+\Psi_{1} y^{\varepsilon} x^{\nu}+\frac{\Psi_{2}}{y^{\beta} x^{\gamma}}
$$

The reliability design involves selecting $x$ and $y$ to minimize $J(x, y)$ given by (6.13) subject to the constraint $u_{1} \leq x \leq u_{2}$ and $y>0$. We use the following two-step approach to obtain the optimal values for the two decision variables of the reliability design.
Step 1: Fix $x$ and obtain the optimal $y$ that minimizes

$$
J_{1}(y \mid x)=\Psi_{0}+\Psi_{1} y^{\varepsilon} x^{\nu}+\frac{\Psi_{2}}{y^{\beta} x^{\gamma}}
$$

Let $y^{*}(x)$ be the optimal value. From the first-order condition we have

$$
\frac{d J_{1}(y \mid x)}{d y}=\varepsilon \Psi_{1} y^{\varepsilon-1} x^{\nu}+\frac{\Psi_{2}(-\beta)}{y^{\beta+1} x^{\gamma}}
$$

This yields

$$
y^{*}(x)=\Psi_{3} x^{-(\gamma+v) /(\varepsilon+\beta)} \text { with } \Psi_{3}=\left(\frac{\Psi_{2} \beta}{\Psi_{1} \varepsilon}\right)^{1 /(\varepsilon+\beta)}
$$

Since $(\gamma+v) /(\varepsilon+\beta)>0$, we see that $y^{*}(x)$ decreases as $x$ increases. This implies that as the product is made sturdier (higher value of $x$ ) the optimal reliability $y^{*}(\mathrm{x})$ decreases.
Step 2: Find the optimal $x$ by minimizing

$$
J_{2}(x)=J\left(x, y^{*}(x)\right)=\Psi_{0}+\Psi_{1}\left(y^{*}(x)\right)^{\varepsilon}+\frac{\Psi_{2}}{\left(y^{*}(x)\right)^{\beta} x^{\gamma}}
$$

Using $y^{*}(x)$ from (6.16), we have

$$
J_{2}(x)=\Psi_{0}+\left(\Psi_{1} \Psi_{3}^{\varepsilon}+\Psi_{2} / \Psi_{3}^{\varepsilon}\right) x^{(v \beta-\varepsilon \gamma) /(\varepsilon+\beta)}
$$

Let $x^{*}$ be the optimal value. Then, it is given by the following:
If $v \beta-\varepsilon<0$, then $x^{*}=u_{2}$ (design based on maximum usage rate)
If $v \beta-\varepsilon>0$, then $x^{*}=u_{1}$ (design based on minimum usage rate)
If $v \beta-\varepsilon=0$, then $x^{*}$ can be any $u$ in the interval $\left[u_{1}, u_{2}\right]$ and we choose $x^{*}=u_{2}$
The optimal value for $y$ is given by $y^{*}=y^{*}\left(x^{*}\right)$. As a result the reliability design involves choosing the decision variables as follows:
(i) $x^{*}=u_{2}$ and $y^{*}=\Psi_{3} u_{2}^{-(\gamma+v) /(\varepsilon+\beta)}$ if $v \beta-\varepsilon \gamma \leq 0$
(ii) $x^{*}=u_{1}$ with $y^{*}=\Psi_{3} u_{1}^{-(\gamma+v) /(\varepsilon+\beta)}$ if $v \beta-\varepsilon \gamma>0$

The optimal investment needed for reliability development is given by $C_{D}\left(x^{*}, y^{*}\right)$. One can carry out a sensitivity analysis to look at the effect of changes in different parameters on $x^{*}$ and $y^{*}$.# 6.5.2 Option 2 [Product Variety: Two Designs] 

Consider the case where the manufacturer decides on two different products (product 1 and 2, respectively). The meta-model is similar to the model in Figure 6.7 except that the decision variables are $\left(x_{1}, y_{1}, x_{2}, y_{2}\right) .^{2}$

## Sales

We need to model the sales for products 1 and 2. This can be done by splitting $g(u)$ as follows. Customers with usage rate $>x_{2}$ all buy product 2 and customers with usage rate $<x_{1}$ all buy product 1 . Customers with usage rate $u$ in the interval $\left[x_{1}, x_{2}\right]$ can either buy product 1 or product 2 . We assume that a fraction $p$ of these customers buy product 1 and that the remaining customers buy product 2 . As a result, the usage rate function for product 1 is given by

$$
g_{1}(u)=\left\{\begin{array}{lr}
g(u), & u_{1} \leq u<x_{1} \\
p g(u), & x_{1} \leq u<x_{2} \\
0, & x_{2} \leq u<u_{2}
\end{array}\right.
$$

and for product 2 by

$$
g_{2}(u)=\left\{\begin{array}{lr}
0, & u_{1} \leq u<x_{1} \\
(1-p) g(u), & x_{1} \leq u<x_{2} \\
g(u), & x_{2} \leq u<u_{2}
\end{array}\right.
$$

The total sales for products 1 and 2 are given by

$$
Q_{1}\left(x_{1}, x_{2}\right)=\bar{Q} \int_{u_{1}}^{u_{2}} g_{1}(u) d u \quad \text { and } \quad Q_{2}\left(x_{1}, x_{2}\right)=\bar{Q} \int_{u_{1}}^{u_{2}} g_{2}(u) d u
$$

## Product Reliability

The ROCOF function for product 1 when operated under nominal usage is given by $\lambda\left(t ; x_{1}, y_{1}\right)$ and for product 2 when operated under nominal usage rate is given by $\lambda\left(t ; x_{2}, y_{2}\right)$ for $u_{1} \leq x_{1}<x_{2} \leq u_{2}$. The ROCOF function, with usage rate $u$ different from the nominal usage rate is modelled by (6.2) with $x_{1}$ and $y_{1}$ in place of $x$ and $y$ in the case of product 1 and with $x_{2}$ and $y_{2}$ in the case of product 2 .

## Expected Warranty Costs

Product 1 (2) is sold with FRW policy with warranty period $W_{1}\left(W_{2}\right)$. The total expected warranty cost using (6.7) is given by

$$
C_{W_{1}}\left(x_{1}, x_{2}, y_{1}\right)=\bar{Q} \int_{u_{1}}^{u_{2}} g_{1}(u)\left[C_{r} \int_{0}^{W_{1}} \lambda_{0}\left(t ; x_{1}, y_{1}\right)\left(\frac{u}{x_{1}}\right)^{\gamma} d t\right] d u
$$

[^0]
[^0]:    ${ }^{2}$ We use subscripts 1 and 2 to denote the variables associated with products 1 and 2, respectively, so that $x_{1}$ and $y_{1}$ are the reliability decision variables for product 1 and 2 and $x_{2}$ and $y_{2}$ for product 2 .for product 1 and by

$$
C_{W_{2}}\left(x_{1}, x_{2}, y_{2}\right)=\bar{Q} \int_{u_{1}}^{u_{2}} g_{2}(u)\left[C_{r} \int_{0}^{W_{2}} \lambda_{0}\left(t ; x_{2}, y_{2}\right)\left(\frac{u}{x_{2}}\right)^{\gamma} d t\right] d u
$$

for product 2 .

# Development Costs 

If only product 1 (2) is developed, the development cost is given by $C_{D 1}\left(x_{1}, y_{1}\right)$ $\left(C_{D 2}\left(x_{2}, y_{2}\right)\right)$. However, when the two are developed concurrently, the development $\operatorname{cost} C_{D}\left(x_{1}, y_{1}, x_{2}, y_{2}\right)<C_{D 1}\left(x_{1}, y_{1}\right)+C_{D 2}\left(x_{2}, y_{2}\right)$ due to commonality of some of the component developments. This can be modelled in several ways, for example

$$
C_{D}\left(x_{1}, y_{1}, x_{2}, y_{2}\right)=C_{D 1}\left(x_{1}, y_{1}\right)+\eta C_{D 2}\left(x_{2}, y_{2}\right)
$$

with $0<\eta<1$. The greater the commonality of components to be developed, the smaller the value of $\eta$.

## Objective Function and Optimal Decisions

The objective function $J\left(x_{1}, y_{1}, x_{2}, y_{2}\right)$ is the sum of the development costs and the total expected warranty costs for the two products and is given by

$$
\begin{aligned}
J\left(x_{1}, y_{1}, x_{2}, y_{2}\right)= & C_{W_{1}}\left(x_{1}, x_{2}, y_{1}\right)+C_{W_{2}}\left(x_{1}, x_{2}, y_{2}\right) \\
& +C_{D}\left(x_{1}, y_{1}, x_{2}, y_{2}\right)
\end{aligned}
$$

The optimization problem is to minimize $J\left(x_{1}, y_{1}, x_{2}, y_{2}\right)$ subject to $u_{1} \leq x_{1}<$ $x_{2} \leq u_{2}, y_{1}>0, y_{2}>0$, and other constraints such as $C_{D 1}\left(x_{1}, y_{1}, x_{2}, y_{2}\right) \leq \bar{C}_{D}$. One would need to use a computational approach to determine the optimal values for the decision variables.

### 6.6 Phase 3 for Standard and Custom-built Products

The processes in phase 3 for standard and custom-built products are identical and we therefore describe them together.

A product can be viewed as a system that can be functionally decomposed into several sub-systems. Each sub-system can be decomposed into major assemblies, each major assembly into assemblies, and so on down to the component level. Let $J$ denote the number of levels with level 1 corresponding to sub-systems and level $J$ corresponding to the component level. ${ }^{3}$ This leads to $J-1$ sub-phases, numbered 1 through $J-1$. The number of sub-phases needed depends on the complexity of the product, and some sub-systems may require more decomposition than others. Each sub-phase involves defining several elements, for example, several sub-systems at level 1 , several assemblies for each sub-system at level 2 , and so on.

[^0]
[^0]:    ${ }^{3}$ Note that $J$ has another meaning here compared with the previous sections.Example 6.2 (Safety Instrumented System). A safety instrumented system has at least three sub-systems: input elements (e.g., sensors, detectors), logic solver (e.g., programmable logic controller), and final elements (e.g., valves, circuit breakers). These are all level 1 in the system hierarchy. A shutdown valve system is, for example, a major assembly that is part of the sub-system final elements and, as such, on level 2 in the system hierarchy. The shutdown valve system has at least three assemblies: control/utility system, actuator, and valve body. All these are on level 3 in the system hierarchy. The valve body can be broken down into valve housing, closing mechanism (ball/gate), valve seats, bonnet seals, and so on, on level 4 on the system hierarchy. Some of these can, again, be broken down into smaller items, and so on. The sub-systems and the assemblies do not need to be broken down into the same number of levels.

# 6.6.1 Sub-phase 1 

The first step in the design process is the initial functional decomposition of the product that leads to the definition of sub-systems at level 1 (see Section 3.6.3). Let $\left\{\overline{\mathrm{F}}_{1}, \overline{\mathrm{~F}}_{2}, \ldots, \overline{\mathrm{F}}_{m_{1}}\right\}$ denote the sets of functions that the product needs to have. These functions will be carried by $m_{1}$ elements (sub-systems on level 1 in the system hierarchy) linked together in a desired manner. Here, $\overline{\mathrm{F}}_{i}$, denotes the set of functions carried by sub-system $i$, for $i=1,2, \ldots, m_{1}$.

Example 6.3 (Safety Instrumented System). In Example 6.2, the safety instrumented system was split into three sub-systems, such that $m_{1}=3$. Sub-system 3 "final elements" may, for example, comprise two shutdown valves in two different pipelines A and B. The sub-system must carry a set of functions $\overline{\mathrm{F}}_{3}$. Among these functions are:

- When there is a demand, the sub-system must close the flow in pipelines A and B, and ensure that there is no significant leakage through the valves
- After a closure of the valves, the system must be able to open the flow again
- The sub-system must prevent leakage of the medium in the pipelines to the environment
- The sub-system must not lead to unintended closures of the flow in pipelines A and B
- and so on

The reliability design in sub-phase 1 involves qualitative analyses by techniques such as fault tree analysis and failure modes, effects, and criticality analysis (FMECA) to identify the critical failure modes. These techniques are discussed in Chapter 4. If the associated risks are unacceptable, then we need to iterate back as shown in Figure 6.8. On the other hand, if the associated risks are acceptable, we proceed to quantitative analysis and this involves deriving the specifications.

The quantitative analysis involves allocating reliabilities to the sub-systems. The input to the allocation process is the desired performance DP-III ${ }_{1}=$ SP-II, the overall reliability of the product obtained from phase 2. The output from this allocation

Figure 6.8. Reliability specification at component level (phase 3)is the specification at level $1, \mathrm{SP}-\mathrm{III}_{1}$, a vector comprising the reliabilities allocated to each of the sub-systems. The dimension of the vector corresponds to the number of sub-systems in the functional decomposition.

One needs to use models to predict the reliability of the product based on the reliability allocated to the elements of sub-phase 2. The structure function and the reliability block diagrams discussed in Chapter 4 are some of the appropriate models for this purpose. If PP-III ${ }_{1}$ and DP-III ${ }_{1}$ match, then we proceed to the next sub-phase. If not, we need to iterate back to make changes to reliability allocation and repeat the process as indicated in Figure 6.8.

Example 6.4 (Safety Instrumented System). The desired reliability of a safety instrumented is usually specified as a safety integrity level (SIL) as discussed in Chapter 4. Assume that the safety instrumented system in Example 6.2 must fulfil a SIL 3 requirement. This means that the average probability of failure on demand (PFD) of the system must be less than $10^{-3}$. The system has three sub-systems: (1) input elements, (2) logic solver, and (3) final elements, and all these must function to perform the safety function in the case of a process demand. The system is therefore a series structure of the three sub-systems and from Chapter 4 we know that the $\mathrm{PFD}_{\mathrm{S}}$ of the system can be expressed as:

$$
\mathrm{PFD}_{\mathrm{S}} \approx \mathrm{PFD}_{1}+\mathrm{PFD}_{2}+\mathrm{PFD}_{3}
$$

where $\mathrm{PFD}_{j}$ is the average probability of failure on demand of sub-system $j$ for $j=1,2,3$. Requirements must now be allocated to the three sub-systems such that $\mathrm{PFD}_{\mathrm{S}}<10^{-3}$. This allocation must be based on the technology available, the cost, and several other constraints. The allocation may, for example, result in the following distribution:

- $35 \%$ to the input elements, such that, $\mathrm{PFD}_{1}<3.5 \cdot 10^{-4}$
- $15 \%$ to the logic solver, such that, $\mathrm{PFD}_{2}<1.5 \cdot 10^{-4}$
- $50 \%$ to the final elements, such that, $\mathrm{PFD}_{3}<5.0 \cdot 10^{-4}$

In addition to this allocation, there are also several qualitative requirements in IEC 61508, for example, related to the degree of redundancy in the various subsystems.

# 6.6.2 Sub-phase $j[j=2,3, \ldots, J-1]$ 

In each sub-phase, we need to define the desired performance and then derive the specifications in the same manner as in sub-phase 1, and as shown in Figure 6.8.

Each sub-phase involves several elements. Let $\left\{E_{j, 1}, E_{j, 2}, \ldots, E_{j, n_{j}}\right\}$ denote the $n_{j}$ elements in sub-phase $j$, for $j=1,2, \ldots, J-1$. Note that $n_{j+1}>n_{j}$, and that the number of elements in the later sub-phases depends on the design of the product. ${ }^{4}$

[^0]
[^0]:    ${ }^{4}$ Note that $n_{j}$ denotes the number of elements in level $j$ of the system hierarchy, while $m_{j}$ is used to denote the number of functions of a system/element.In a similar manner to that sub-phase 1 , it is first necessary to define the different functions that the elements at sub-phase $j$ need to perform. Let $\left\{\overline{\mathrm{F}}_{j, 1}, \overline{\mathrm{~F}}_{j, 1}, \ldots, \overline{\mathrm{F}}_{j, m_{j}}\right\}$ denote these functions. Good design further involves defining the elements at subphase $j+1$ to ensure that the desired performance is achieved.

We need to define the desired reliability for each element in the sub-phase. Let DP-III ${ }_{j v}$ denote the desired reliability of element $E_{j v}$, for $v=1,2, \ldots, n_{j}$. DP-III ${ }_{j}$ is a vector of dimension $n_{j}$ given by DP-III ${ }_{j}=\left(\right.$ DP-III $\left._{j 1}, \mathrm{DP}-\mathrm{III}_{j 2}, \ldots, \mathrm{DP}-\mathrm{III}_{j n_{j}}\right)$.

The design options in sub-phase $j$ are made up of one or more different, feasible combinations of elements. The design options, $\mathrm{DS}_{j \kappa}$, for $\kappa=1,2, \ldots, k_{j}$, that look promising, is the starting point. $\mathrm{DS}_{j}=\left(\mathrm{DS}_{j 1}, \mathrm{DS}_{j 2}, \ldots, \mathrm{DS}_{j k_{j}}\right)$ is a vector of design options at sub-phase $j$. For each option, there can be elements that need no further decomposition while other elements need to be decomposed into two or more elements at sub-phase $j+1$. The various elements at level $j+1$ need to be linked to ensure that all the functions $\overline{\mathrm{F}}_{j i}$, for $i=1,2, \ldots, m_{j}$, at sub-phase $j$ can be achieved.

A design option is selected from $\mathrm{DS}_{j}$ and is first evaluated in a qualitative analysis similar to that of sub-phase 1. If risks are found acceptable, reliabilities are allocated to the elements of sub-phase $j+1$ and these define the specifications SPIII $_{j v}$, for $v=1,2, \ldots, n_{j+1}$. SP-III ${ }_{j}$ is a vector of specifications at sub-phase $j$ (of dimension $n_{j}$ ) with SP-III ${ }_{j}=\left(\right.$ SP-III $\left._{j 1}, \mathrm{SP}-\mathrm{III}_{j 2}, \ldots, \mathrm{SP}-\mathrm{III}_{j n_{j+1}}\right)$.

The reliability prediction at sub-phase $j$ is also similar to that of sub-phase 1 , and is based on the reliability allocated to the elements of sub-phase $j+1$. Again, the structure function and the reliability block diagrams discussed in Chapter 4 may be used. This results in the predicted reliability PP-III ${ }_{j v}$, for element $E_{j v}$, for $v=$ $1,2, \ldots, n_{j}$. PP-III ${ }_{j}$ (a vector of dimension $n_{j}$ ). PP-III ${ }_{j}$ is the predicted reliability of the elements in sub-phase $j$ and is given by PP-III ${ }_{j}=\left(\right.$ PP-III $\left._{j 1}, \mathrm{PP}-\mathrm{III}_{j 2}, \ldots\right.$, PP-III ${ }_{j n_{j+1}}$ ).

The predicted reliability PP-III ${ }_{j}$ is compared to the desired reliability DP-III ${ }_{j}$ to determine whether the two match or not. If they match, we proceed to the next sub-phase with DP-III ${ }_{(j+1) v}=$ SP-III ${ }_{j v}$, for $v=1,2, \ldots, n_{j+1}$ if $j<J-1$, and when $j=J-1$, we have the reliability specifications SP-III at the component level. If the two do not match, we iterate back to the conceptual design if $j=1$ or to the previous sub-phase if $j>1$, as illustrated in Figure 6.8.

# 6.7 Achieving the Allocated Reliability at Component Level 

If the allocated reliability for a component matches the reliability of a standard commercially available component (with similar functional features), then the decision problem is trivial. However, when the allocated reliability is higher (e.g., see Figure 6.9 , where the design requires the reliability to be above 0.99 over the interval $[0, L)$ ), then the manufacturer has three options and these are (i) redundancy, (ii) preventive maintenance, and (iii) reliability growth through development. Figure 6.10 indicates the process for making the choice between the options. In this section, we first discuss these options and then look at the optimal decision problem.

Figure 6.9. Allocated versus actual component reliability


Figure 6.10. Achieving the reliability requirement at the component level# 6.7.1 Redundancy 

Redundancy is a technique used to improve the reliability through the use of replicated components. Redundancy can only be used when the functional design of the system allows for the incorporation of replicated components and is used extensively in electronic products to achieve high reliability when individual components have unacceptably low reliability.

Building in redundancy corresponds to using a module consisting of $M$ replications of a component. The manner in which these replicates are put to use depends on the type of redundancy. In active redundancy, all $M$ components of the module are in their operational state, or "fully energized," when put into use. In contrast, in passive redundancy, only one component is in its fully energized state and the remaining are either partially energized (in the case of warm standby) or kept in reserve and energized when put into use (in the case of cold standby). When the fully energized component fails, it is replaced by one of the partially energized components in the case of warm standby, or, in the case of cold standby, by a component from the reserve using a switching mechanism, provided that not all of the components in the module have failed. If all components in the module have failed, then the module has failed. For further details, see Blischke and Murthy (2000); Rausand and Høyland (2004).

The number of replications needed depends on the actual and the allocated reliability. The reliability increases as the number of replicated components $(M)$ increase (see Figure 6.11). The decision regarding the use of redundancy has implications for production cost and must take into account other constraints such as weight and/or volume. We need to ensure that these constraints are not violated.


Figure 6.11. Achieving allocated reliability target through redundancy

Example 6.5 (Safety Instrumented System). In Example 6.4, the reliability requirement for the sub-system "input elements" was given by $\mathrm{PFD}_{1}<3.5 \cdot 10^{-4}$. To meet this requirement, we may need more than one detector. One option would be to install two independent detectors of the same type in a 1002 configuration. This means that the system is functioning if at least one of the two detectors are functioning.In this case, both detectors are operating in active redundancy and a 1002 logic is implemented in the logic solver.

Another option is to install three independent detectors of the same type. In this case we may let them operate in active redundancy and implement a 2003 logic in the logic solver. An alarm will, in this case, be raised if at least two of the three detectors give a signal to the logic solver. This option will give approximately the same PFD as the 1002 configuration, but will give much fewer false alarms.

# 6.7.2 Preventive Maintenance 

One way of achieving the allocated target for component reliability is through the use of preventive maintenance actions that involve replacing the component periodically. The replacement interval depends on the actual and allocated component reliabilities as indicated in Figure 6.12. The decision regarding the use of preventive maintenance needs to take into account its implications of life cycle cost, availability, and so forth. Let the preventive maintenance actions be carried out periodically with period $T$. Then the number of preventive replacements is given by the largest integer less than $L / T$.


Figure 6.12. Achieving allocated reliability target through preventive maintenance (with maintenance interval $T$ )

### 6.7.3 Reliability Growth through Development

Improvement in component reliability may be achieved through a test-analyse-andfix (TAAF) programme. The process begins with the testing a component, usually under increasing levels of stress until failure. Data related to the test and the failure is then collected (e.g., failure mode, time to failure, failure characteristics) and analysed by engineers to reveal the causes of failure. Corrective actions in the form of changes to the component design are then taken to reduce the frequency of future failures and the process is repeated until the reliability targets are achieved. ${ }^{5}$

[^0]
[^0]:    ${ }^{5}$ For further discussion of TAAF, TAAF test design principles, and relationship of TAAF to other testing programmes, see Priest (1988).The effort (e.g., resources, development time) needed depends on the actual and the allocated reliabilities as shown in Figure 6.13. Note the uncertain outcome of any such development programmes. This has implications in terms of some of the constraints being not satisfied with non-zero probability. Let $\tau$ denote the development time and it depends on the allocated reliability. The development cost $\pi_{\mathrm{D}}(\tau)$ is an increasing function of $\tau$.


Figure 6.13. Achieving allocated reliability target through development

# 6.7.4 Modelling for Optimal Decisions 

For each component there are two decision variables: (i) primary and (ii) secondary. For component $k$ for $k=1,2, \ldots, K$, the primary decision variable is denoted by $\gamma_{k}$ and it can assume one of four values $(0-4)$ as indicated in Table 6.1. When the allocated value is non-zero, we have a set of secondary decision variables that depend on the value allocated to $\gamma_{k}$ and these are also indicated in Table 6.1.

Table 6.1. Secondary decision variables for component $k$

| $\gamma_{k}$ | Options | Secondary decision variable |
| :-- | :-- | :-- |
| 0 | Standard component | None |
| 1 | Use redundancy | $M_{k}$ (Number of replicates) |
| 2 | Use preventive maintenance | $T_{k}$ (Replacement interval) |
| 3 | Initiate development programme | $\tau_{k}$ (Development time) |

When $\gamma_{k}=0$ there is no secondary decision variable. In this case, the allocated reliability $R_{k A}(t)=R_{k C}(t)$, the reliability of the available component selected. The secondary decision variables for the remaining three cases are (i) $M_{k}$, the number of replicates when $\gamma_{k}=1$, (ii) $T_{k}$, the replacement interval when $\gamma_{k}=2$, and (iii) $\tau_{k}$, the development time when $\gamma_{k}=3$. As a result, the set of decision variables is given by $\left\{\gamma_{k}, M_{k}, T_{k}, \tau_{k}\right\}$, for $k=1,2, \ldots, K$.# Optimal Component Reliability Specification 

The choice of decision variables affects various costs. Two costs that are of relevance in reliability design are the following:

1. Production cost per unit given by $C_{P}=\sum_{k=1}^{K} C_{k P}$
2. Total development cost given by $C_{D}=\sum_{k=1}^{K} C_{k D}$
$C_{k P}$ is the production cost associated with component $k$, for $k=1,2, \ldots, K$, and is given by

$$
C_{k P}= \begin{cases}C_{k} & \text { if } \gamma_{k}=0 \\ M_{k} C_{k}+\xi_{k} & \text { if } \gamma_{k}=1 \\ N_{k} C_{k} & \text { if } \gamma_{k}=2 \\ \pi_{P}\left(R_{k A}\right) & \text { if } \gamma_{k}=3\end{cases}
$$

where $C_{k}$ is the purchase price per unit cost of component $k$, for $k=1,2, \ldots, K$, is bought from the ones available on the market. When $\gamma_{k}=1$, the number of replicates in $M_{k}$ and the additional cost $\xi_{k}$ is the extra cost associated with the switching mechanism in the case of cold and warm redundancy. When $\gamma_{k}=2$, the number of spares needed for preventive maintenance action is given by $N_{k}=\left[L / T_{k}\right]$ where $[x]$ is the largest integer $\leq x$ ) and these spares are included into the cost. Finally, when $\gamma_{k}=3$, the cost of production is a function of the allocated reliability and is given by an increasing function $\pi_{P}\left(R_{k A}\right)$, for $k=1,2, \ldots, K$.

The development cost associated with component $k$, for $k=1,2, \ldots, K$ is given by

$$
C_{k D}= \begin{cases}0 & \text { if } \gamma_{k}=0 \\ 0 & \text { if } \gamma_{k}=1 \\ 0 & \text { if } \gamma_{k}=2 \\ \pi_{\mathrm{D}}\left(\tau_{k}\right) & \text { if } \gamma_{k}=3\end{cases}
$$

where the function $\pi_{\mathrm{D}}\left(\tau_{k}\right)$ depends on the gap between the reliability allocated and the current reliability of the component, and the development time. ${ }^{6}$

The optimal component reliability specification is obtained by defining a suitable cost function for minimization. One such function is the total manufacturing cost that is the sum of the production and development costs and given by

$$
J\left(\gamma_{k}, M_{k}, T_{k}, \tau_{k} ; 1 \leq k \leq K\right)=\sum_{k=1}^{K} C_{k P}+\sum_{k=1}^{K} C_{k D}
$$

[^0]
[^0]:    ${ }^{6}$ This is a simple deterministic model. A more realistic model is a stochastic model where the time to achieve the allocated reliability is uncertain.The optimal values are obtained by selecting the decision variables that minimize the above cost function and also satisfies all the constraints. Figure 6.14 shows this in a schematic manner and involves mixed integer optimization. A variety of tools are available for carrying out this optimization.


Figure 6.14. Task 2 decision making

# 6.8 Outcome of Phase 3 

The outcomes of phase 3 are (i) a qualitative analysis (FMECA) of product reliability and (ii) a qualitative analysis that defines the reliability requirement $R_{k A}(t)$ for $k=1,2, \ldots, K$, for the $K$ components and the strategies (redundancy, preventive maintenance and/or reliability development) to achieve these stated requirements.

### 6.9 Case Study: Cellular Phone

The reliability design involves the following two tasks:

- Task 1: Determining product reliability (phase 2) to ensure that the desired business objectives (phase 1) are achieved.
- Task 2: Determining the component reliability (phase 3) that will ensure the desired product reliability (phase 2).


## Product Reliability

In order to achieve the business objectives (DP-I in phase 1), let the product characteristics (SP-I) selected in phase 1, be as follows:
(a) The base warranty period $W=1$ (year).
(b) On the average, not more than 10 customers per 1000 should experience a failure during the warranty period.(c) On the average, not more than 100 customers per 1000 should experience a failure over a five year period.
(d) The expected warranty cost per unit should not exceed $2 \%$ of the sale price.

The product ROCOF is modelled by a function shown in Figure 6.3. The product reliability is a function of three parameters $\theta_{i} ; i=1,2,3$, and these need to be selected as part of the design process to ensure that the desired performance (DP-II $\equiv$ SP-I) are achieved.

Let $\theta_{1}=3$ (years). We select $\theta_{2}$ so as to ensure that the probability of one or more failures during the warranty period is less than 0.99 . This will ensure that the requirement in (b) is satisfied. This implies that $e^{-\left(1 / \theta_{2}\right)} \geq 0.99$ or

$$
1 / \theta_{2} \leq-\ln (0.01)
$$

To satisfy (c) we need to ensure that $\exp \left(-\frac{5}{\theta_{2}}-\frac{5^{2}-3^{2}}{\theta_{3}}\right) \geq 0.90$ which implies

$$
\frac{5}{\theta_{2}}+\frac{9}{\theta_{3}} \leq-\ln (0.90)
$$

The expected warranty cost is given by $C_{r} W / \theta_{2}$ where $C_{r}$ is the average cost of a repair. In order to satisfy (d) we need to ensure that

$$
\frac{C_{r} W}{P \theta_{2}} \leq 0.02
$$

where $P$ is the unit sale price. The smallest values of $\theta_{2}$ and $\theta_{3}$ which satisfy (6.29)(6.31) are the values that define the product reliability.

# Component Level Reliability 

As mentioned earlier, the reliability allocation at the component level is design specific. There is considerable literature dealing with various reliability issues for the different elements of the cellular phone and we discuss a few of them.

Integrated circuits: The failures of ICs over time can be categorized into two groups: (i) abrupt failures (due to mechanisms such as electromigration, time-dependent dielectric breakdown (TDDB), electrostatic discharge (ESD), electrical overstress (EOS), and stress migration) and (ii) gradual wear-out failures resulting from progressive decline in IC performance (due to mechanisms such as hot carrier injection, stress induced leakage current (SLIC)). In the early stages, ICs were built without any consideration for reliability and then tested to assess the reliability performance.

With the concept of "building in reliability," (Mathewson et al., 1999) one can assess the reliability performance through simulation under different types of duty cycles. Minehane et al. (2000) discuss various commercial and in-house reliability simulators for assessing reliability performance by simulating IC failures due to hot-carrier injection, electromigration, and oxide reliability. The simulator input requirements consist of circuit description, degradation constants, and the duty cycle.Solder joint: One of the causes for solder joint failure is thermal fatigue due to thermal cycling. In the case of cellular phones, the thermal cycling experienced depends on the external environmental conditions such as the daily and seasonal changes in heat and temperature. Syed and Doty (1999) discuss life prediction based on a 3-D finite element model and creep analysis. Darveaux et al. (2000) discuss the impact of design and material selection on solder joint fatigue life with fine pitch BGAs. Hiraoka and Niaido (1997) deal with reliability design of current stress in LSI interconnects based on failure due to electromigration. Lau and Pao (1997) discuss the solder joint reliability for different types of assemblies.

Shell (outer casing): The shell of a cellular phone is usually made of plastic. It needs to be designed for some specified life time and withstand the shocks resulting from accidental droppings. Spoormaker (1995) discusses the designing of reliable plastic products based on an understanding of the failure causes and mechanisms. Brostow and Cornelissen (1985) discuss the failure of plastics in more detail. Wang et al. (2005) deal with a finite element model to simulate the drop/impact test so that the reliability performance can be assessed during the design phase.

# Intermediate Level Reliability 

These include reliability design of packing, reliability at board level and many others. ${ }^{7}$

## Failure Mode Analysis (FMA)

FMA is a technique used extensively at component, product and intermediate levels. Atterwalla and Stierman (1994) deal with FMA of ball grid array. Jha and Kaner (2003) catalogue the different failure modes of handheld wireless communication devices.

[^0]
[^0]:    ${ }^{7}$ See, Herard (1999) for packaging reliability. Papers dealing with board level reliability include Hung et al. (2000, 2001); Wu et al. (2002); Tee et al. (2003); Jang et al. (2004).# Performance During Development 



### 7.1 Introduction

This chapter deals with reliability performance during phases 4 (stage II, level III) and 5 (stage II, level II) of the product life cycle. Phase 4 starts at the component level and the focus is on the development process to achieve the desired reliability defined in phase 3. Once this is achieved, the focus shifts to building a prototype and this involves proceeding through several intermediate sub-levels ending up with the product level. The aim is to obtain the predicted performance (PP) based on limited testing at the component and product levels (and possibly at one or more intermediate sub-levels). In phase 5, the prototype is released to a small number of customers so that the reliability performance in the field can be assessed. We first consider standard products and thereafter we briefly look at custom-built products.

The outline of the chapter is as follows. Section 7.2 deals with the development process in phase 4 for standard products. It involves several elements and these are discussed in Sections 7.3 to 7.8. Section 7.3 looks at reliability development testing and, in particular, accelerated testing, and Section 7.4 deals with design of experiments for testing. Section 7.5 discusses the analysis of test data and looks at both graphical and statistical approaches. In Section 7.6, we discuss reliability growth models and these provide estimates of future growth and play an important role in the decision making process. Data from many sources need to be effectively integrated to obtain credible estimates of predicted reliability performance. The Bayesian framework is appropriate for this and is the focus of Section 7.7. The development process is an uncertain process and, as a result, we need to understand the risk implication and these are discussed in Section 7.8. Section 7.9 looks at phase 5 for standard products. In Section 7.10, phases 4 and 5 for custom-built products are briefly discussed. The chapter concludes with a case study on cellular phones in Section 7.11.# 7.2 Phase 4 for Standard Products 

The aim of phase 4 is to ensure that the desired reliability is achieved through a development process. The process was briefly discussed in Section 4.7.2 and involves the execution of the test, analyse, and fix (TAAF) cycle in an iterative manner as indicated in Figure 4.10. Phase 4 has several sub-phases with sub-phase $J$ corresponding to component level, sub-phase 1 to sub-system level and the remaining sub-phases corresponding to sub-assembly, assembly, and so on.

The TAAF process starts at component level and involves testing of components and analysis of the test data. Based on the results from the analysis, changes are made to the design or to the material selection. The process is repeated at one or more of the intermediate levels and finally at the product level where we test the reliability of the product as a whole. This process involves several elements and these are indicated in Figure 7.1.


Figure 7.1. Development process at level III

Since limited testing is done, the reliability performance is the predicted performance at one or more of the sub-phases. PP-III denotes the predicted reliability at thedifferent sub-phases of phase 4 . The predicted performance at sub-phase $j$ given by PP-III ${ }_{j}$ for $j=2,3, \ldots, J-1$, is compared with the desired performance DP-III ${ }_{j}$ for $j=1,2, \ldots, J$ (obtained from phase 3 ) and the TAAF cycle repeated until both match. Only when this occurs, do we proceed to sub-phase $j-1$. Note that in each sub-phase, we need to determine if the constraints are satisfied or not and to iterate back to an earlier sub-phase or to phase 3 if no further development is possible.

Finally, it is worth commenting that PP-III (a vector) in phase 4 is the predicted reliability based on data generated by testing after development. This is different from PP-III in phase 3 where the prediction is based on models using past historical data, expert judgement, and so on.

# 7.3 Reliability Development Testing 

Development testing, in the context of new product development, must be performed to ensure that designs meet requirements for performance, safety, durability, reliability, statutory aspects, and so on. Reliability development tests may be categorized into the following two categories based on the aims of the testing. ${ }^{1}$

1. Reliability growth tests
2. Environmental and design limit tests

Factors, such as product type and complexity dictate the nature of these tests. According to O'Connor (2003):
"Testing is usually the most expensive, time-consuming and difficult activity during the development of engineering products and systems. Testing should be based on a philosophy that would provide a foundation for all plans, methods and decisions related to testing of engineered products and systems."

### 7.3.1 Reliability Growth Testing

Reliability growth testing is the same as TAAF testing of a product early in the development cycle when design changes can be made readily in response to observed failures.

There can be several objectives of reliability growth testing. These include verifying improvements in design reliability, identifying any necessary design changes, and determining if the product design has to be improved to meet the specified reliability.

Reliability growth testing provides a systematic method to conduct development testing, to track the progress of reliability improvement efforts and to predict system

[^0]
[^0]:    ${ }^{1}$ Two other types of tests are (i) reliability qualification tests and (ii) operational tests. The former is discussed in Chapter 8 and the latter in Section 7.10.reliability given the observed (or anticipated) rate of improvement. ${ }^{2}$ Here, the emphasis is on reliability improvement as opposed to reliability assessment. This involves exposing the test item to environmental stresses simulating actual usage stresses until a failure occurs. An analysis of the failure is carried out and the appropriate failure mechanisms and causes are identified. Design modifications are made to prevent or minimize future occurrence of the same failure mechanism.

# 7.3.2 Environmental Stress and Design Limit Testing 

Products are designed for some specified range of operating environment (e.g., temperature, humidity). Environmental stress testing involves testing under different operating environments to determine if the product performs satisfactorily at the extreme conditions of its operating envelope. Test conditions can include temperature, shock, vibration, humidity, and so forth. Design limit testing is to determine the limits of the operating environment beyond which the product performance fails to meet the desired performance.

Environmental stress testing is a process to systematically evaluate product design margins, precipitate latent potential design and assembly weaknesses early in the product development cycle, identify options for corrective action and risk mitigation. This can be done at any level (ranging from component to system and one or more intermediate levels) and should include worst-case operating conditions, including operations at the maximum and minimum specified limits. As with the reliability growth testing, any failures resulting from the test need to be analysed (through root cause analysis) and fixed through design changes.

## Models

The effect of the different environmental stresses (denoted by a vector $\boldsymbol{S}$ or its transformation $\boldsymbol{x}$ ) on product reliability is best modelled using the proportional hazards model discussed in Section 4.4.4. The effect of stresses is captured through a covariate function $\psi(\boldsymbol{x}, \boldsymbol{\beta})$ where $\boldsymbol{\beta}$ is also a vector determined empirically from test data.

### 7.3.3 Accelerated Testing

When a product is very reliable, it is necessary to use accelerated life tests to reduce the time required for testing. This involves putting items on test under environmental conditions that are far more severe than those normally encountered. Such tests are used to evaluate the useful life of a system's critical parts for problem identification and improvement. ${ }^{3}$

[^0]
[^0]:    ${ }^{2}$ Duane (1964) was the first to propose the concept of reliability growth testing in the context of developmental testing of aircraft engines.
    ${ }^{3}$ There are many books dealing with this topic. These include Nelson (1990) and Hobbs (2000).Stress that accelerates the failure process may be applied in many forms, high or low temperatures, humidity, cycling between excessively high and low conditions, excess usage, electrical stress, vibration, and so forth. In order to conduct and analyse an accelerated life test, the challenge is to relate the results obtained under conditions of higher stress to those that would result under normal conditions. This requires an adequate understanding of failure mechanisms and appropriate models that express the relationship. Many different models have been proposed for the scaling relationship (or acceleration factor). We discuss a few of the more commonly used models. ${ }^{4}$

# Arrhenius Acceleration Model 

Here, the stress on the component is thermal stress that can lead to failure, for example, due to increased brittleness of the materials. Applications include electrical insulation, electronic devices, adhesive bonds, batteries, fibres, lubricants, filaments, and plastics. The model is also appropriate for failures of electronic components driven by certain thermo-physical and chemical processes, such as ion drift and intermetallic compound formation.

The Arrhenius reaction rate model is given by

$$
r(\vartheta)=r_{0} \exp \left(-\frac{E}{k \vartheta}\right)
$$

where $r(\vartheta)$ is the reaction rate at temperature $\vartheta, r_{0}$ is a constant that depends on the part geometry, size, and so on, $E$ is the activation energy of the reaction (in electron-volts), $k$ is Boltzmann's constant ( $8.617 \cdot 10^{-5}$ electron-volts per K ), and $\vartheta$ is temperature in kelvin $\left({ }^{\circ} \mathrm{C}+273.16\right)$ and is the stress variable.

The Arrhenius reaction rate model (7.1) is used by MIL-HDBK-217F as a model for the failure rate $(\lambda)$ at temperature $\vartheta$ for electronic components

$$
\lambda=K \exp \left(-\frac{E}{k \vartheta}\right)
$$

where $K$ is a constant.
If we assume that the mean life of a component is proportional to the inverse reaction rate of the process, we get the Arrhenius life-stress model

$$
\mu(\vartheta)=A \exp \left(\frac{E}{k \vartheta}\right)
$$

where $A$ is a constant and $\mu(\vartheta)$ is a life measure, such as the mean time to failure (MTTF) or the median life.

For data analysis, it is often convenient to use the natural logarithm of (7.2)

$$
\ln (\mu(\vartheta))=a+\frac{b}{\vartheta}
$$

[^0]
[^0]:    ${ }^{4}$ For more details, see for example, Yang (2007).where $a=\ln (A)$ and $b=E / k$. The natural logarithm of the life measure $\mu(\vartheta)$ at temperature $\vartheta$ is then a linear function of $1 / \vartheta$. This property is very convenient for fitting the relationship to data and for checking goodness of fit.

Let $\vartheta_{0}$ be a nominal (normal) temperature and let $\vartheta_{1}$ be an accelerated (increased) temperature. The accereration factor ( AF ) is the ratio of the life under normal stress and the life under accelerated stress

$$
\operatorname{AF}\left(\vartheta_{0}, \vartheta_{1}\right)=\frac{\mu\left(\vartheta_{0}\right)}{\mu\left(\vartheta_{1}\right)}=\exp \left(\frac{E}{k}\left(\frac{1}{\vartheta_{0}}-\frac{1}{\vartheta_{1}}\right)\right)
$$

The Arrhenius acceleration factor has been found to be useful in cases where the product operates under constant or near-constant temperature in its field-use and test environments. Some extensions can be found in Kececioglu and Sun (1995).

# Inverse Power Law Model 

Another widely used relationship, with many applications, including electrical, metal products such as ball bearings, metal fatigue, fibre, filaments, and so forth, is the inverse power law model. The basic model is given by

$$
\mu(\vartheta)=\frac{A}{\vartheta^{\beta}}
$$

where $\mu$ is a life measure, such a mean time to failure, MTTF, $\vartheta$ is the stress applied (e.g., voltage), and $A$ and $\beta$ are constants specific to the item being tested and the test procedure. The acceleration factor is given by the expression

$$
\operatorname{AF}\left(\vartheta_{0}, \vartheta_{1}\right)=\frac{\mu\left(\vartheta_{0}\right)}{\mu\left(\vartheta_{1}\right)}=\left(\frac{\vartheta_{1}}{\vartheta_{0}}\right)^{\beta}
$$

where $\vartheta_{0}$ and $\vartheta_{1}$ are the stresses at normal and accelerated level, respectively.
Several different versions of the inverse power law model are discussed in Nelson (1990) and Condra (1993). A detailed analysis of data on ball bearing failures based on the inverse power law model can be found in Lieblein and Zelen (1956).

## Eyring Model

The Eyring model is similar to the Arrhenius model, but is more general in the sense that is may be used to represent a second stress in combination with temperature, for example, electrical stress or relative humidity. It is based on the reaction rate for chemical degradation derived from quantum mechanics. The basic relationship is

$$
\mu(\varphi, \vartheta)=\frac{B}{\varphi} \exp \left(\frac{E}{k \vartheta}\right)
$$

where $\mu$ is a life measure, for example the mean time to failure, $\varphi$ is the applied stress at temperature $\vartheta, B$ is a constant, and the exponential term is as in the Arrhenius model. For this relationship, the acceleration factor becomes$$
\mathrm{AF}=\frac{\mu\left(\varphi_{0}, \vartheta_{0}\right)}{\mu\left(\varphi_{1}, \vartheta_{1}\right)}=\frac{\varphi_{1}}{\varphi_{0}} \exp \left(\frac{E}{k}\left(\frac{1}{T_{0}}-\frac{1}{T_{1}}\right)\right)
$$

where $\mu\left(\varphi_{0}, \vartheta_{0}\right)$ and $\mu\left(\varphi_{1}, \vartheta_{1}\right)$ are the mean time to failure at stress levels $\left(\varphi_{0}, \vartheta_{0}\right)$ and $\left(\varphi_{1}, \vartheta_{1}\right)$, respectively.

The model has applications in many of the same areas as the Arrhenius model, with the added feature of the second stress factor. An example of a model of this type is the Peck (1979) model for failure times of electronic micro-circuits, in which stress is expressed as $\varphi=h^{3}$, where $h$ is percentage relative humidity, and $E$ is taken to be 0.9 . A more general form is $\varphi=h^{\beta}$, where $\beta$ is estimated from test data.

# Other Models 

There are many other models reported in the literature. The Norris-Landzberg acceleration model (Norris and Landzberg, 1969) is appropriate for the testing of surface mount solder interconnections that progressively degrade due to cumulative fatigue damage during operational thermal cycling. This empirical model is a version of the Coffin-Manson fatigue life model ${ }^{5}$ specialized for common solder alloys. The Norris-Landzberg model accounts for the temperature excursion, high temperature extreme, and time-dependent thermo-mechanical behaviour of lead-bearing solder alloys related to stress relaxation. The model accounts for the empirical observation that extended dwell time in low frequency thermal cycling accelerates fatigue damage and induces earlier failure of high-risk solder connections. The MIL-HDBK344A acceleration model accounts for the composite degradation and failure mechanisms during thermal cycling.

## Pitfalls of Accelerated Testing

Meeker and Escobar (1998) discuss nine potential pitfalls of accelerated testing. These are as follows:

1. Multiple (unrecognized) failure modes
2. Failure to quantify uncertainty (in statistical estimates) properly
3. Multiple time scales and multiple factors affecting degradation
4. Masked failure modes
5. Faulty comparison
6. Accelerated variables can cause decelerations
7. Beware of untested design/production changes
8. Beware of drawing conclusions on the basis of specially built prototype test units
9. It is difficult to use accelerated life tests to predict field reliability.

The authors provide interesting real cases to highlight each of the above pitfalls.

[^0]
[^0]:    ${ }^{5}$ For more details of the Coffin-Mason model (appropriate for thermal cycling fatigue) and other models, such as Gunn's law (for humidity), see Foucher et al. (2002).# 7.4 Design of Experiments for Testing 

Testing is often viewed as an engineering issue. Testing in development is done to ensure that the product has the desired reliability. If the desired reliability is not achieved and the product is released, the manufacturer incurs very high costs in terms of product recalls, design changes, customer dissatisfaction, and tarnished reputation. Because of the importance and magnitude of the economic and business aspects, testing is an issue for management. There is often pressure to reduce testing because of the high costs involved (as building in reliability is a costly venture), without appreciation of the downstream commercial implications.

The design of tests is a challenging issue as the different people involved in the new product development view testing differently. This is best summarized in the following quotation from O'Connor (2003),
"The design engineer might feel that there is no need for extensive testing, but the project engineer might think otherwise. The management and finance people will want to minimize the time and cost, and therefore the amount of testing. However, if all can agree on a philosophy that takes account of what is known, what is uncertain, and the other essential factors such as costs, timing, markets, regulations, safety, etc., then at least there will be a foundation for rational planning and decisions. Intrinsic to this philosophy should be the maxim that effective testing should be considered as a valueadding process, not as a cost."

### 7.4.1 Principles of Test Design

Test designs follow the basic principles of design of experiment (DOE). ${ }^{6}$ Particularly appropriate are factorial experiments, with the factor, or factors involved usually being quantitative. Each stress variable is viewed as a factor in the test design. Splitplot experiments of various types are often appropriate if two or more factors are involved, particularly when time is a factor.

An additional concern that must be addressed in designing experiments of this type is the possibility of the excess stress causing failures that would not occur in normal operations, such as melting of materials, weakening of bonds, or expansion of materials with high temperatures. Furthermore, if an item can fail in several ways, acceleration may affect failure rates for the different modes differently. For this and other reasons (e.g., cost and test equipment requirements), accelerated tests are most often done at the part or small component level.

Because of the complexity of relating failures (or failure-related characteristics) to more than one stress factor, accelerated tests most often involve only a single accelerating factor, for example, temperature alone rather than temperature and humidity. Two-factor experiments are not uncommon, but many-factor experiments are not usually appropriate in this context, particularly if interactions (between different factors) are present.

[^0]
[^0]:    ${ }^{6}$ There are many books dealing with design of experiments, for example, see Cox and Reid (2000); Box et al. (2005); Montgomery (2005).# 7.4.2 Relevant Issues 

We confine our attention to the component level and one single factor (or stress variable). The different issues that need to be considered in the design of accelerated test plans include the following: ${ }^{7}$

1. The life distribution for the component: Exponential, Weibull, and so on.
2. Life-stress relationships: The accelerated failure time model may sometimes be adequate.
3. Optimization criteria: Cost, minimum variance of estimates (parameter or some reliability measure), determinant of the covariance matrix (when there are two or more parameters), and so on.
4. Stopping rule: The testing is carried out until all the items fail, or is terminated earlier. The rule for termination can be based on a limit for testing or when the number of failed items reach some specified number. This determines the type of data generated and is discussed further in the next section.
5. Estimation method: Various methods for estimating the parameters can be used. This issue is discussed in Section 7.5.
6. Types of stress loading: In the case of constant stress, the stress level on an item does not change during the test period. In step-stress testing the level can change one or more times during the test period.
7. A number of items to be tested under each stress level if more than one stress level is used.
8. Constraints: These can be on the stress levels, time, cost, and so on.
9. Robustness: The test needs to be robust to failure model errors, loss of test specimens, and so on.

Selection of levels of a factor to use in testing depends on the context (e.g., materials, stresses). Some important considerations are the following:

1. The stress levels are not so extreme that the failure mechanism changes
2. The stress levels are within the range over which the selected model is appropriate
3. Excessive extrapolation is not required

In the first two cases, the model may be invalidated and the test data not relevant to normal conditions. Excessive extrapolation has not only these difficulties, but the added problem that confidence intervals, even if valid, will be so wide that they are useless.

### 7.4.3 Optimal Design of Experiments for Testing

A large number of test plans have been studied in detail. Some of these can be found in books, such as Nelson (1990); Condra (1993); Hobbs (2000); Meeker and Escobar (1998). There are several review papers dealing with this topic. These include Meeker and Escobar (1993) and more recently, Nelson (2005a,b).

[^0]
[^0]:    ${ }^{7}$ Nelson (2005a) discusses many of these issues and gives references to where interested readers can find more details.# 7.5 Analysis of Test Data 

The data from the testing depends on the stopping rule for the test. We first look at this issue and then discuss qualitative and quantitative analysis. The quantitative analysis can be either graphical or statistical.

We confine our discussion to the case where $n$ denotes the number of items put to test under a constant stress. Let $T_{1}, T_{2}, \ldots, T_{n}$ denote the (potential) life times of the $n$ items under test. We consider $T_{1}, T_{2}, \ldots, T_{n}$ to be $n$ independent random variables. If the value of $T_{i}$ can be observed, the actual realized value is denoted $t_{i}$ for $i=1,2, \ldots, n$.

### 7.5.1 Test Data

## Complete Data

The data set available for estimation is the set $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$. In other words, the actual realized values are known for each observation in the data set. This happens when the test is terminated only after all the $n$ items fail.

## Censored Data

In this case the actual realized values for some or all of the variables are not known and this depends on the kind of censoring.

## Right Type I Censoring

Let $v$ denote the time at which the test is terminated if some of the items have not failed by age $v$. For item $i$, the actual realized value of $T_{i}$ is known only if $t_{i} \leq v$. When $t_{i}>v$ the only information available is that $T_{i}>v$.

## Right Type II Censoring

Let $r$ denote a predetermined number such that $r<n$. The test is terminated when the $r$ th failure occurs. The data from the test is given by $t_{i}$ (the actual realized value of $T_{i}$ ) for the $r$ items that failed and that $T_{i}>v$ for the remaining $(n-r)$ data where $v$ is the maximum of the $r$ observed $t_{i} \mathrm{~s}$.

### 7.5.2 Qualitative (Engineering) Analysis

The main qualitative analysis is the root cause analysis of items that fail during the testing. The aim here is to find the fundamental, or root, cause of failure. Any cause higher up is a symptom or a result of the root cause. For example, the root cause of failure of a chip might be overheating due to poor ventilation or material property of contacts. In a sense, root cause analysis can be viewed as carrying out an "autopsy" of failed item(s). The root cause requires asking the question "why?" several times until a satisfactory explanation is found. Once the root cause is identified, the problem canbe fixed by taking appropriate corrective actions by way of changes to the design or the material selection. ${ }^{8}$

# 7.5.3 Graphical Analysis 

## Empirical Distribution Function Plots

The empirical distribution function $F_{n}(t)$ is the cumulative proportion of the data that lie below $t$. There are many different ways of computing $F_{n}(t)$. If the data set is complete (i.e., not censored) and is given as $t_{1}, t_{2}, \ldots, t_{n}$, the empirical distribution function can be computed by

$$
F_{n}(t)=\frac{\text { Number of lifetimes } \leq t}{n}
$$

If the function $F_{n}(t)$ is plotted as a function of $t$, we get the empirical distribution function plot and we note that it is a "step function" having steps of height $1 / n$ at each data point $t_{i}$.

Computating $F_{n}(t)$ is easily done by using the order statistic $t_{(1)}, t_{(2)}, \ldots, t_{(n)}$ (which is a reordering of the data such that $t_{(1)}<t_{(2)}<\cdots<t_{(n)}$ ) with $t_{(0)}=0$ and $t_{(n+1)}=\infty$, so that $F_{n}\left(t_{(i)}\right)=i / n$.
$F_{n}(t)$ is also called the sample cumulative distribution function. There are other approaches to computing the empirical distribution function for a complete data set. In the "mean rank" approach, $F_{n}^{(1)}\left(t_{(i)}\right)=i /(n+1)$. Three other alternatives are as follows:

- $F_{n}^{(2)}\left(t_{(i)}\right)=(i-0.5) / n$ (called the "median rank" estimator)
- $F_{n}^{(3)}\left(t_{(i)}\right)=(i-0.3) /(n+0.4)$
- $F_{n}^{(4)}\left(t_{(i)}\right)=(i-3 / 8) /(n+1 / 4)$

For discussion on computing the empirical distribution function with censored data, see Nelson (1982) and Lawless (1982).

## Probability Plots

Probability plots have been developed as an alternative method of plotting data. As opposed to the sample empirical distribution function, which is a non-parametric procedure, probability plots assume a particular underlying distribution. The idea is to transform the data and/or probability scales so that the plot on the transformed scale is linear (within chance fluctuations). Equivalently, we plot sample fractiles against the fractiles of a specified distribution. As a result, the plots are sometimes referred to as "P-P plots."

[^0]
[^0]:    ${ }^{8}$ There are many books dealing with failure analysis and an illustrative sample is as follows. Nishida (1992) deals with failure analysis of mechanical components, Martin (1999) with electronic components, and Colangelo and Heiser (1987) with analysis of metallurgical failures.Probability plotting papers have been developed for a number of distributions, including the normal and most of the important distributions used in reliability applications: exponential, lognormal, Weibull, gamma, and extreme value. Many statistical computer packages (e.g., Minitab, SPSS, STATA, S, R) include some or all of these plotting options as well.

# Other Plots 

A special class of plots is constructed by plotting the empirical distribution function corresponding to a given distribution against the $t_{(i)}$ after suitable transformation of one or both variables. One commonly used distribution is the Weibull distribution. Let $t_{p}$ denote the $p$-fractile. Then the probability plot is the plot of $\log \left(\log \left(1 /(1-p)\right)\right)$ versus $\log \left(t_{p}\right) .{ }^{9}$

Note. If the plot indicates a linear relationship between the two transformed variables, then the data can be modelled by a two-parameter Weibull distribution. If the plot is not linear, then in some cases the data can be modelled by distributions derived from the two-parameter Weibull distribution. For more on this, see Murthy et al. (2003).

The plotting of the failure rate function and the cumulative failure rate function is used in assessment of reliability performance. These allow us to estimate the fractiles of the distribution, the failure rate as a function of age, and a number of related quantities. For more on this, see Nelson (1982).

### 7.5.4 Statistical Analysis (Single Stress Level)

## Basic Concepts

Let $F(t ; \theta)$ denote the failure distribution under a constant stress. The parameter to be estimated is $\theta$ and is a $k$-dimensional vector. There are two approaches to estimation and several methods for each of them. The two approaches are:

- Point estimation
- Interval (or confidence interval) estimation

In point estimation, a numerical value for $\theta$ is calculated. In interval estimation, a $k$-dimensional region is determined in such a way that the probability that the region contains the true parameter $\theta$ is a specified, predetermined value. If $k=1$, this region is an interval, hence the name.

[^0]
[^0]:    ${ }^{9}$ Using other distributions result in different plots. For more on this, see Lawless (1982), Nelson (1982), and Meeker and Escobar (1998).# Point Estimation 

When the data set is complete, the point estimator $\widehat{\theta}=\widehat{\theta}\left(T_{1}, T_{2}, \ldots, T_{n}\right)$ is some function of $T_{1}, T_{2}, \ldots, T_{n}$, and is hence a random variable. By inserting the actual, observed lifetimes, we get $\widehat{\theta}=\widehat{\theta}\left(t_{1}, t_{2}, \ldots, t_{n}\right)$ which is called a point estimate of $\theta$ and is a numerical value.

In the case of censored or grouped data, the estimate is a function of the observed data and the censoring or grouping values.

An estimator $\widehat{\theta}_{i}$ of $\theta_{i}$ is said to be unbiased if $E\left(\widehat{\theta}_{i}\right)=\theta_{i}$ for all possible values of $\theta_{i} . \widehat{\theta}$ is an unbiased estimator of $\theta$ if $\widehat{\theta}_{i}$ is unbiased for $i=1,2, \ldots, k$. An estimator for which $E\left(\widehat{\theta}_{i}\right) \neq \theta_{i}$ is said to be biased. The bias $\widehat{b}\left(\widehat{\theta}_{i}\right)$ of an estimator $\widehat{\theta}_{i}$ is given by $b\left(\widehat{\theta}_{i}\right)=E\left(\widehat{\theta}_{i}\right)-\theta_{i}$.

Efficiency of an estimator may be assessed relative to another estimator or estimators (relative efficiency) or relative to an absolute standard.

An unbiased estimator $\widehat{\theta}$ of a parameter $\theta$ is minimum variance unbiased if $\operatorname{Var}(\widehat{\theta}) \leq \operatorname{Var}\left(\theta^{*}\right)$ for any other unbiased estimator $\theta^{*}$ and for all possible values of $\theta$, where $\operatorname{Var}(\cdot)$ denotes the variance of the estimator.

## Point Estimation: Methods and Estimators

Moment Estimator: The method of moments is based on expressing $k$ moments in terms of the parameters of the distribution. Using sample moments (obtained from the data available for estimation) in place of the moments in these relationships yields $k$ equations containing the $k$ unknown parameters. Solving these yields the estimates. Note that in most cases, the estimates need to be obtained using numerical techniques. For most models, moment estimators are asymptotically consistent and normally distributed. In general, moment estimators are not efficient.

Percentile Estimator: The percentile estimator is obtained by first obtaining the expression for the percentile in terms of the model parameters and is given by

$$
p=F\left(t_{p}, \theta\right)
$$

Let $0<p_{1}<p_{2}<\cdots<p_{k}<1$. Estimates of the corresponding $k p$-percentiles are obtained from the empirical distribution function using the data. Using these in (7.9) yields $k$ equations containing the $k$ unknown parameters. Solving these yields the parameter estimates. For most models, the percentile estimators are asymptotically consistent and are normally distributed. However, they are usually not efficient.
Maximum Likelihood Estimator: For complete data, the likelihood function is given by

$$
L(\theta)=\prod_{i=1}^{n} f\left(t_{i} ; \theta\right)
$$

The maximum likelihood estimate (MLE) of $\theta$ is the value $\widehat{\theta}$ that maximizes the likelihood function given by (7.10). As a result, the estimate is a function (say,$\psi\left(t_{1}, t_{2}, \ldots, t_{n}\right)$ ) of the data. The corresponding $\psi\left(T_{1}, T_{2}, \ldots, T_{n}\right)$ is called the maximum likelihood estimator. Under certain regularity conditions, maximum likelihood estimators are consistent, asymptotically unbiased, efficient, and normally distributed.

For censored data of Type I, the likelihood function is given by

$$
L(\theta)=\prod_{i=1}^{n}\left(f\left(t_{i}\right)\right)^{\delta_{i}}(1-F(v))^{1-\delta_{i}}
$$

where $\delta_{i}=1$ if the $i$ th obvervation is uncensored $\left(T_{i}=t_{i}<v\right)$ and $=0$ if it is censored $\left(T_{i}>v\right)$. For censored data of Type II (with $r$ failures), the likelihood function is given by

$$
L(\theta)=\left(\prod_{i=1}^{r} f\left(t_{i}\right)\right)\left(1-F\left(t_{r}\right)\right)^{n-r}
$$

where the data has been reordered so that the first $r$ correspond to uncensored and the remaining to censored (at time $t_{r}$ ).
Bayesian Estimator: In the Bayesian approach, the parameter $\theta$ is regarded as a random variable with a distribution that expresses our "degree of belief" about the value of $\theta$. We assume that $\theta$ is one-dimensional, but we can later extend the results to the multi-dimensional case.

Initially, before we carry out any experiments, our degree of belief about $\theta$ can be expressed by the probability density function $g(\theta)$ which is called our prior density, and which we assume to be continuous. Our degree of belief may be formed by previous experience with similar products, expert judgement, and so on. If we have only a vague belief about the value of $\theta$, the prior density is very spread-out with a large variance.

Let $T$ denote the time to failure of the product and let $f(t \mid \theta)$ be the probability density function of $T$. In the Bayesian set-up, this density is a conditional density of $T$, given $\theta$.

Assume that we can observe $n$ independent lifetimes $T_{1}, T_{2}, \ldots, T_{n}$. The probability density function of these $n$ lifetimes given $\theta$ is

$$
f\left(t_{1}, t_{2}, \ldots, t_{n} \mid \theta\right)=\prod_{i=1}^{n} f\left(t_{i} \mid \theta\right)
$$

and is equal to the likelihood function in (7.10).
The joint probability density function of $\theta$ and $\left\{T_{1}, T_{2}, \ldots, T_{n}\right\}$ is given by

$$
f_{t, \theta}\left(t_{1}, t_{2}, \ldots, t_{n}, \theta\right)=\left(\prod_{i=1}^{n} f\left(t_{i} \mid \theta\right)\right) g(\theta)
$$

Note that $f_{t, \theta}$ is the product of the likelihood function and the prior density function. The marginal density function of $\left\{T_{1}, T_{2}, \ldots, T_{n}\right\}$ is given by$$
\begin{aligned}
f\left(t_{1}, t_{2}, \ldots, t_{n}\right) & =\int_{-\infty}^{\infty} f\left(t_{1}, t_{2}, \ldots, t_{n}, \theta\right) d \theta \\
& =\int_{-\infty}^{\infty} f\left(t_{1}, t_{2}, \ldots, t_{n} \mid \theta\right) g(\theta) d \theta
\end{aligned}
$$

Using Bayes theorem (Martz and Waller, 1982), the posterior density function of $\theta$, given the data $t_{1}, t_{2}, \ldots, t_{n}$, is given by

$$
g\left(\theta \mid t_{1}, t_{2}, \ldots, t_{n}\right)=\frac{f_{t, \theta}\left(t_{1}, t_{2}, \ldots, t_{n}, \theta\right)}{f\left(t_{1}, t_{2}, \ldots, t_{n}\right)}
$$

The posterior density of $\theta$ given the data $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ describes our updated belief about the value of $\theta$, after we have observed the data.

The Bayesian point estimate $\widehat{\theta}_{b}$ of a parameter $\theta$ is usually ${ }^{10}$ the conditional mean and is given by

$$
\widehat{\theta}_{b}=E\left(\theta \mid t_{1}, t_{2}, \ldots, t_{n}\right)=\int_{-\infty}^{\infty} \theta \cdot g\left(\theta \mid t_{1}, t_{2}, \ldots, t_{n}\right) d \theta
$$

Example 7.1. A valve is assumed to have constant failure rate $\lambda$. Experience (or belief) leads us to think that the failure rate can be expressed as a random variable with a gamma prior distribution given by

$$
g(\lambda)=\frac{\beta_{1}{ }^{\alpha_{1}}}{\Gamma\left(\alpha_{1}\right)} \lambda^{\alpha_{1}-1} e^{-\lambda \beta_{1}} \quad \text { for } \lambda>0
$$

The mean value of this distribution is (see Rausand and Høyland, 2004)

$$
E(\lambda)=\frac{\alpha_{1}}{\beta_{1}}
$$

Note that $\alpha_{1}$ and $\beta_{1}$ are numerical values that describe our initial belief about the value of $\lambda$ and have to be related to a specified time unit, for example, per hour.

Assume now that we test $n$ independent valves with times to failure $T_{1}, T_{2}, \ldots, T_{n}$ that are exponentially distributed with failure rate $\lambda$. The joint probability density function of $\left\{T_{1}, T_{2}, \ldots, T_{n}\right\}$ and $\lambda$ is from $(7.14)$

$$
f_{t, \lambda}\left(t_{1}, t_{2}, \ldots, t_{n}, \lambda\right)=\lambda^{n} e^{-\lambda \sum_{i=1}^{n} t_{i}} \cdot \frac{\beta_{1}{ }^{\alpha_{1}}}{\Gamma\left(\alpha_{1}\right)} \lambda^{\alpha_{1}-1} e^{-\beta_{1} \lambda}
$$

By using Bayes theorem (7.16) we get

$$
g\left(\lambda \mid t_{1}, t_{2}, \ldots, t_{n}\right)=\frac{\left(\beta_{1}+\sum_{i=1}^{n} t_{i}\right)^{n+\alpha_{1}}}{\Gamma\left(n+\alpha_{1}\right)} \lambda^{\alpha_{1}+n-1} e^{-\lambda\left(\beta_{1}+\sum_{i=1}^{n} t_{i}\right)}
$$

which is recognized to be a gamma density with parameters $\alpha_{2}=\left(\alpha_{1}+n\right)$ and $\beta_{2}=\left(\beta_{1}+\sum_{i=1}^{n} t_{i}\right)$. The Bayesian estimate (7.17) is then

$$
\hat{\lambda}_{b}=\frac{\alpha_{2}}{\beta_{2}}=\frac{\alpha_{1}+n}{\beta_{1}+\sum_{i=1}^{n} t_{i}}
$$

[^0]
[^0]:    ${ }^{10}$ The estimate depends on the loss function used. With a quadratic loss function, the Bayesian point estimate becomes the mean of the posterior distribution.# Special Case: Weibull Failure Distribution 

Consider a product with time to failure $T$ that can be adequately modelled by a two-parameter Weibull distribution, with shape parameter $\beta$ and scale parameter $\alpha$. Presented in Chapter 4, the probability density function of $T$ is ${ }^{11}$

$$
f(t)=\frac{\beta}{\alpha^{\beta}} t^{\beta-1} \exp \left(-\left(\frac{t}{\alpha}\right)^{\beta}\right)
$$

Method of Moments: The estimates can be obtained using the sample mean $\bar{t}$ and sample variance $s^{2}$. In the case of complete data $\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ these are given by

$$
\bar{t}=\frac{1}{n} \sum_{i=1}^{n} t_{i}
$$

and

$$
s^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(t_{i}-\bar{t}\right)^{2}
$$

In (7.19), $n-1$ is used as it yields an unbiased estimate of the sample variance. The estimate $\widehat{\beta}$ is obtained as the solution of

$$
\frac{s^{2}}{\widehat{t}^{2}}=\frac{\Gamma(1+2 / \widehat{\beta})}{\Gamma^{2}(1+1 / \widehat{\beta})}-1
$$

and $\widehat{\alpha}$ is given by

$$
\widehat{\alpha}=\frac{\hat{t}}{\Gamma(1+1 / \widehat{\beta})}
$$

Note that solving (7.20) requires a numerical procedure and involves computing the gamma function.
Method of Percentiles: For the Weibull distribution function, the 63.2th percentile is equal to $\alpha$ and this can be used as a percentile estimator of $\alpha$ so that

$$
\widehat{\alpha}=t_{\left(1-e^{-1}\right)}
$$

where the percentile is calculated from the empirical plot of the distribution function. A percentile estimate of $\beta$ is given by

$$
\widehat{\beta}=\frac{\log [-\log (1-p)]}{\log \left[t_{p} / t_{0.632}\right]}
$$

for $0<t_{p}<t_{0.632}$ and it can be obtained from the empirical distribution function.
${ }^{11}$ A detailed derivation for this case study can be found in Murthy et al. (2003).Method of Maximum Likelihood: For the case of complete data, the likelihood function is given by

$$
L(\alpha, \beta)=\prod_{i=1}^{n}\left(\frac{\beta t_{i}^{\beta-1}}{\alpha^{\beta}}\right) \exp \left(-\left[\frac{t_{i}}{\alpha}\right]^{\beta}\right)
$$

The maximum likelihood estimates are obtained by solving the equations resulting from setting the two partial derivatives of $L(\alpha, \beta)$ to zero. As a result, $\hat{\beta}$ is obtained as the solution of

$$
\frac{\sum_{i=1}^{n} t_{i}^{\hat{\beta}} \log t_{i}}{\sum_{i=1}^{n} t_{i}^{\hat{\beta}}}-\frac{1}{\hat{\beta}}-\frac{1}{n} \sum_{i=1}^{n} \log t_{i}=0
$$

Although an analytical solution is not available, $\hat{\beta}$ can easily be found using a computational approach. Once the shape parameter is estimated, the scale parameter can then be estimated as follows:

$$
\widehat{\alpha}=\left(\frac{1}{n} \sum_{i=1}^{n} t_{i}^{\hat{\beta}}\right)^{1 / \hat{\beta}}
$$

In the case of Type I censoring, the likelihood function is given by

$$
L(\alpha, \beta)=\frac{\beta^{k}}{\alpha^{\beta k}}\left[\prod_{i=1}^{k} t_{i}^{\beta-1}\right] \exp \left(-\frac{1}{\alpha^{\beta}}\left[\sum_{i=1}^{k} t_{i}^{\beta}+(n-k) v^{\beta}\right]\right)
$$

where the data has been reordered so that the first $k$ are uncensored data and the remaining are censored data. The maximum likelihood estimate $\widehat{\beta}$ is obtained as the solution of

$$
\frac{\sum_{i=1}^{n} t_{i}^{\hat{\beta}} \log t_{i}}{\sum_{i=1}^{n} t_{i}^{\hat{\beta}}}-\frac{1}{\hat{\beta}}-\frac{1}{k} \sum_{i=1}^{k} \log t_{i}=0
$$

and the estimate $\widehat{\alpha}$ is given by

$$
\widehat{\alpha}=\left(\frac{1}{n}\left[\sum_{i=1}^{k} t_{i}^{\hat{\beta}}+(n-k) v^{\hat{\beta}}\right]\right)^{1 / \hat{\beta}}
$$

For the case with Type II censoring, the likelihood function is given by,$$
L(\alpha, \beta)=\frac{\beta^{r}}{\alpha^{\beta r}}\left[\prod_{i=1}^{r} t_{i}^{\beta-1}\right] \exp \left(-\frac{1}{\alpha^{\beta}}\left[\sum_{i=1}^{r} t_{i}^{\beta}+(n-r) t_{r}^{\beta}\right]\right)
$$

where the data has been reordered so that the first $r$ in the set are the uncensored observations. The maximum likelihood estimate $\widehat{\beta}$ is obtained by solving

$$
\frac{\sum_{i=1}^{r} t_{i}^{\widehat{\beta}} \log t_{i}+(n-r) t_{r}^{\widehat{\beta}} \log t_{r}}{\sum_{i=1}^{r} t_{i}^{\widehat{\beta}}+(n-r) t_{r}^{\widehat{\beta}}}-\frac{1}{\widehat{\beta}}-\frac{1}{r} \sum_{i=1}^{r} \log t_{i}=0
$$

and using this, the estimate $\widehat{\alpha}$ is obtained from

$$
\widehat{\alpha}^{\widehat{\beta}}=\frac{1}{r}\left(\sum_{i=1}^{r} t_{i}^{\widehat{\beta}}+(n-r) t_{r}^{\widehat{\beta}}\right)
$$

Numerical methods need to be used to obtain the estimates.

# Interval Estimation 

When $\theta$ is a scalar, a confidence interval based on a sample of size $n, T_{1}, T_{2}, \ldots, T_{n}$, is an interval defined by two limits, the lower limit $L_{1}\left(T_{1}, T_{2}, \ldots, T_{n}\right)$ and the upper limit $L_{2}\left(T_{1}, T_{2}, \ldots, T_{n}\right)$ having the property that

$$
\operatorname{Pr}\left(L_{1}\left(T_{1}, T_{2}, \ldots, T_{n}\right)<\theta<L_{2}\left(T_{1}, T_{2}, \ldots, T_{n}\right)\right)=\varepsilon
$$

where $\varepsilon(0 \leq \varepsilon \leq 1)$ is called the confidence coefficient.
Confidence is usually expressed in per cent, for example, if $\varepsilon=0.95$, the result is a $95 \%$ confidence interval for $\theta$. Note that the random variables in expression (7.30) are $L_{1}$ and $L_{2}$, not $\theta$, i.e., this is not a probability statement about $\theta$, but about $L_{1}$ and $L_{2}$. Hence we use the term "confidence" rather than "probability" when discussing this as a statement about $\theta$. The proper interpretation is that the procedure gives a correct result $100 \varepsilon \%$ of the time.

### 7.5.5 Statistical Analysis (Multiple Stress Levels)

For multiple stress levels with a single accelerating variable, a number of approaches have been developed. An approach using graphical methods can be found in Nelson (1990), Condra (1993) and Meeker and Escobar (1998). Included are the exponential, Weibull, and lognormal distributions. Plots of failure data at the different stress levels are done on an appropriate plotting paper, and, assuming that the slopes are the same, differences between the resulting lines are analysed.

Finally, many statistical program packages and many reliability packages include programs for data analysis based on the proportional hazards model and other models used in accelerated tests.# 7.6 Reliability Growth Models 

The aim of reliability growth models is to monitor the progress of the development programme and the improvements in reliability. The models must not only provide a good estimate of current reliability based on the development effort based on the data and information available, but also have the capability to predict future improvements if the development programme were to continue. These models play a critical role in deciding whether to continue with the development programme or to terminate it.

Early in the development cycle, there is often little prior information available and as the development progresses, more information becomes available. As a result, modelling of reliability growth is a combination of art and science requiring good mathematical analyses as well as sound judgement.

A number of reliability growth models have been developed to monitor the progress of the development programme and the improvements in reliability. They are broadly categorized into two types: continuous and discrete. Each of these can be further sub-divided as shown in Figure 7.2. In general, continuous models are used in the context of continuous variables (such as the failure rate in the case of exponential distribution or the mean time to failure) and attempt to describe the reliability improvement as a function of the total test time. Discrete models involve discrete (attribute) data and are concerned with incremental improvements in reliability as a result of design changes. These improvements are expressed as functions of the probability of success in test trials. A trial is defined by a period of operation terminated upon successful completion of the test or the occurrence of a failure.


Figure 7.2. Reliability growth models

Parametric models are those based on a specified distribution of the time to failure, for example, the exponential or Weibull distribution. Non-parametric models involve specification of a functional form for the reliability improvement relationship. Data analysis for parametric models includes estimation of the parameters of the assumed distribution. In the non-parametric case, curve-fitting techniques, such as regression analysis, are often used.# 7.6.1 Discrete Reliability Growth Models 

Many different discrete reliability growth models have been proposed and we discuss a few of them. ${ }^{12}$ The models look at reliability growth in incremental stages, with $R_{j}$ being the reliability of the item at stage $j$. In terms of the reliability function, the general form of these models is

$$
R_{j}=R_{\infty}-\phi g(j)
$$

where $R_{\infty}$ is the maximum attainable reliability as $j \rightarrow \infty, \phi$ is a parameter expressing the rate of growth, and $g(\cdot)$, the growth function, is non-negative and decreasing. We indicate two simple models.

Weiss Reliability Growth Model (Weiss, 1956)
This model assumes that the failure rate $\lambda_{j}$ is constant (implying exponential failure distribution) during the interval between the $(j-1)$ st and $j$ th corrective actions, and is given by

$$
\lambda_{j}=\lambda+\frac{\phi}{j}
$$

Here $\lambda$ is the ultimate lowest possible failure rate, and $\phi / j$ is the maximum remaining improvement (in terms of reduced failure rate) at the $j$ th corrective action. $\phi$ is estimated from the data.

Lloyd-Lipow Reliability Growth Model [Lloyd and Lipow (1962)]
In this model the growth in reliability is in exponential increments and the model is given by

$$
R_{j}=1-\phi e^{-\gamma(j-1)}
$$

where $\phi$ and $\gamma$ are parameters of the growth function to be estimated from the data. The model is derived under the assumption that there is a single failure mode and that the engineer has a fixed probability of fixing the item after any failure.

### 7.6.2 Continuous Reliability Growth Models

Duane Reliability Growth Model [Duane (1964)]
This is a classic and widely used reliability growth model and also called the "Duane learning curve." It was first determined empirically where it was noted that the cumulative failure rate typically plotted as a linear function of cumulative time on test when plotted on the log-log scale. Duane supported this by obtaining several data sets during the equipment development test phases.

[^0]
[^0]:    ${ }^{12}$ For a review of discrete reliability growth models, see Fries and Sun (1996).Let $T$ denote the total time on test and $\mu_{c}$ the cumulative MTBF. Then the Duane model is given by the relationship

$$
\mu_{c}=\phi T^{\beta}
$$

where $\phi$ is a function of the initial MTBF at the start of testing, and $\beta$ is the rate of growth.

Crow (1974) proposed modelling the improvement in reliability growth by a non-homogeneous Poisson process. Since then, many other reliability growth models have been proposed, see for example, Lloyd (1986), Robinson and Dietrich (1987, 1989). ${ }^{13}$

# 7.7 Bayesian Approach 

The Bayesian approach uses information obtained at a given intermediate level to determine a prior distribution for reliability (or a related characteristic) at the next higher level. This requires an understanding of the system structure and provides a logical method of incorporating not only information from previous levels, but also both prior and test information at the current level.

A schematic representation of the process is given in Figure 7.3. It starts with a prior distribution on component reliability for each component. In addition, other information may be available at this level as well, including relevant historical data, subjective evaluations, results of simulations, and so forth. This information is used to form an independent assessment of the prior distribution (a "natural" prior). Weights are assigned to these two prior distributions and they are combined to form a composite prior distribution of the component reliability. Tests are performed and the posterior distribution of the component reliability is determined by using Bayes theorem.


Figure 7.3. Bayesian approach

The process proceeds through the various levels of the system, using the system logic model, up to the formulation of the posterior distribution of the system relia-

[^0]
[^0]:    ${ }^{13}$ For a detailed discussion of continuous reliability growth models, see Sen (1998).bility. The approach uses information obtained at a given level to determine a prior distribution for reliability (or a related characteristic) at the next higher level.

The approach provides the advantage of a logical method of incorporating not only information from previous levels, but also both prior and test information at the current level. The difficulties are that, as always with the Bayesian approach, quantifying the prior information may be highly subjective and therefore subject to criticism, and that the mathematics becomes quite intractable.

# 7.8 Risks in Reliability Development Programmes 

Building in reliability is costly but the consequence of unreliability can be costlier. In the front-end phase the target value for product reliability is determined through a trade-off between cost and risk.

Like any development programme, the outcome of the reliability development programme is uncertain. The assessed reliability is based on limited testing on component, product, and one or more intermediate levels. As a result, the assessed reliability can differ significantly from the actual reliability, an unknown quantity. Figure 7.4 shows four scenarios (A-D).

|  |  | Assessed reliability |  |
| :--: | :--: | :--: | :--: |
|  |  | Less than target value | Equal or greater than target value |
| Actual reliability | Less than target value | A | B (Type I error) |
|  | Equal or greater than target value | C (Type II error) | D |

Figure 7.4. Risk in the reliability development programme

Scenario A: Here, both the actual and the assessed reliabilities are below the target value and hence, further development is needed. Note that if any of the constraints (e.g., development cost and/or development time) are violated the development programme might be terminated.
Scenario B: Here, the assessed reliability indicates that the target value is achieved, but in reality this is not the case. If the actual reliability is well below the target value, then releasing the product on to the market can result in high warranty costs, customer dissatisfaction, and in the worst case, a product recall. ${ }^{14}$
Scenario C: Here, the actual reliability is greater then the target value, but the assessed reliability indicates that this is not so. As a result, the development programme is continued, incurring additional costs that could have been avoided.

[^0]
[^0]:    ${ }^{14}$ For product recall in the automotive industry, see, for example, Bates et al. (2007); Hartman (1987); Rupp and Taylor (2002).Scenario D: In this case the assessed and actual reliabilities exceed the target value and the termination of the programme does not entail any risks.

The risks in scenarios B and C need to be understood and taken into account during the reliability development phase. In addition, there are other kinds of project risks. These include cost and time overruns, losing critical staff, and so forth.

Most of the reliability models do not take into account the trade-offs between cost and risk and the focus is usually on estimation and prediction of product reliability from test data. Quigley (2003) looks at an extension to a Bayesian reliability growth model to incorporate financial costs associated with product unreliability. The model can be used to carry out cost-benefit analysis during product development and is illustrated through a simple case.

# 7.9 Phase 5 for Standard Products 

The testing in phase 4 to assess product performance is usually done in controlled conditions and an environment that mimics the real world in a limited manner. The field performance depends on several factors like operating environment, usage intensity, load (or stress) on the product, and so forth. This varies from customer to customer.

For products produced in large numbers the manufacturer can get some limited feel for field performance by releasing the product to a small number of customers. Phase 5 of the development process deals with this and the testing of the product by customers is also referred to as operational testing. It involves the customers keeping a log of the appropriate information relating to usage mode and intensity, operating environment, and so on, and reporting of any failures that occur during the operation of the product. This information is used to assess field reliability and make design changes to overcome any failure modes not detected during phase 4.

The analysis of failure data needs to done properly due to variations in usage intensity, operating environment, and so on. This topic is discussed further in Chapter 9. The decision to proceed with the manufacturing depends on a proper evaluation of product performance based on the field data.

If the outcomes of phases 4 and 5 are a success, then the final design of the prototype is released for manufacturing.

### 7.10 Phases 4 and 5 for Custom-built Products

Custom-built products are either one of a kind (so that only one unit is produced) or produced in limited numbers. In the former case, the end of phase 4 yields the final product that is released to the customer. In the latter case, the production starts immediately after phase 4 so that we move to phase 6 directly. In general, each item is released soon after they are produced and the delivery of all the items might take several months or years.The execution of phase 4 for custom-built products is very similar to that for standard products. However, the testing is more important and must be carried out in accordance with the contract document. In this context, the term operational tests is important. Operational tests have three objectives:

1. Verification of the reliability studies conducted during the project.
2. Providing appropriate data for justifying operational procedures and policies modifications with respect to reliability and maintainability.
3. Providing appropriate data to be utilized in subsequent phases.

Example 7.2 (Safety Instrumented System). The development activities in phases 4 and 5 are different for the different types of safety instrumented systems. Systems with rather cheap assemblies and components can be tested in the way described earlier in this chapter. Some safety instrumented systems are, however, so complex - or so expensive - that it is not possible to do any degradation testing apart from some minor components. An example is a high integrity pressure protection system (HIPPS) on a subsea oil and gas pipeline. The valves of such a system are so big and so expensive that it is not possible to do any reliability testing at the assembly (valve) level. We, therefore, have to accept the testing of minor parts like seals, material samples, and so forth. A special guideline, DNV RP A203, has been developed for qualifying the reliability of subsea equipment.

A mock-up of the system is often set up in the laboratory to test the input elements and the logic solver. The logic solver contains software and it is hence important to check that this software reacts correctly to all possible signals from the input elements and under all foreseeable disturbances. It is also important to check that the diagnostic part of the logic solver interacts properly with the input elements.

# 7.11 Case Study: Cellular Phone 

The solder joint fatigue life for fine pitch ball grid array packaging depends on the material and design choices. Darveaux et al. (2000) look at the effect of package variables (die size, package size, ball count, pitch, mold compound, and substrate material) and test board variables (thickness, pad configuration, and pad size) on the fatigue life when subjected to thermal cycling and present a summary of their test results based on failure analysis and the number of cycles to failure. Geng (2005) reports on a test to evaluate solder joint shock reliability where the solder joints are subjected to dynamic loads and shock conditions. Hung et al. (2001) report on the effect of die size, board surface finish, substrate gold plating thickness, polymide thickness and underfill material utilization on fatigue life of solder joints under thermal and bend cycle tests.

For chip size packages (CSP), Larsen et al. (2004) report on mechanical bending techniques for assembly weaknesses through a study of board level failures and solder joint failures. Testing to determine board level reliability of a stacked CSPsubjected to cyclic bending is reported in Wu et al. (2002). Tests to evaluate the reliability of wafer level chip size packaging (WL-CSP) with various solder alloys and die thicknesses is reported in Keser et al. (2004).

Tests to evaluate flip chip on board (FCOB) reliability are reported in Jang et al. (2004) and Sillanpää and Okura (2004). The former compares three types of direct chip attachment and the latter looks at tests involving thermal cycling and mechanical shock by drop testing.

Lee and Lo (2004) test the effect of repeated key strokes on the reliability of handheld devices (such as cellular phones). Here, the failure is due to the considerable flexure of the printed circuit board (PCB) resulting from repeated key strokes. These mechanical stresses can cause failure of components through mechanisms such as board trace cracking, solder joint fatigue, and solder pad cracking.

Cavasin et al. (2003) report on tests to improve the reliability of RF amplifiers.# Product Performance and Production 



### 8.1 Introduction

This chapter deals with reliability performance during phase 6 (stage III, level III) of the product life cycle. Phase 6 deals with production - and reliability performance is here the reliability of the items produced. As such, this phase is relevant mainly for standard products (for large volume production of items, such as cellular phones, domestic appliances, cars) and in some cases for custom-built products (for small volume production of items, such as ships, airplanes). Obviously, this is not relevant for a single custom-built product.

Production is the process of transforming inputs (raw materials, components) into finished products. The process is complex and can involve several sub-phases, with one or more operations carried out in each sub-phase. The reliability of the products produced (AP-III) will, in general, differ from that predicted by the design (PP-III of phase 3) or the prototype produced under strict laboratory conditions (PP-III of phase 4) and, in fact, is almost always lower. This difference is due to variability in the operations and in the inputs. Through proper quality control of the inputs and operations, we try to ensure that AP-III is kept close to DP-III. This chapter deals with variability issues that can cause AP-III to deviate from DP-III and quality control techniques to ensure that this does not occur.

The outline of the chapter is as follows. Section 8.2 deals with phase 6 for standard products. Section 8.3 looks at production process and occurrence of nonconforming items, Section 8.4 discusses the effect of quality variations on product reliability, and Section 8.5 deals with testing during production. Section 8.6 looks at alternative approaches to quality control and Section 8.7 deals with optimal quality control. The chapter concludes with a case study on cellular phones in Section 8.8.# 8.2 Phase 6 for Standard Products 

Figure 8.1 shows the key elements that influence the reliability (AP-III) of the produced items. Before production can commence, the manufacturer needs to design the production process. This involves providing the equipment and the resources needed to carry out the operations (e.g., casting, soldering, heating) at several subphases. The number of sub-phases needed depends on the complexity of the product. The production starts at sub-phase $J$ (component level) and proceeds through several sub-phases leading to the sub-phase where the final operations (involving subsystems) take place to assemble the final product. The process state characterizes the condition of the equipment (e.g., cutting tool) and/or the settings (e.g., the temperature of the soldering element). The design process involves defining the acceptable limits for the states for the different equipment and the settings. When the process state is within these limits, it is said to be in control. With age and operations, the state will tend to degrade (e.g., cutting tool becoming blunt due to wear, and temperature setting deviating) and can go outside the specified limits. When this happens, the process is said to be out of control.


Figure 8.1. Key elements of phase 6

Items that meet the design reliability (and/or other) performance are called conforming items and those that do not, are called non-conforming items. Ideally, there should be no non-conforming item produced when the process is in control. However, this is an ideal case and is seldom true. In general, a very small fraction of the items produced can be non-conforming. When the process goes out of control, the fraction of non-conforming items produced increases significantly and this has serious implications for the manufacturer. Non-conforming items are less reliable thanconforming items and, as a result, lead to high customer dissatisfaction and warranty costs. Similarly, when the inputs (components or material obtained from external suppliers) do not meet the specification, the items produced are non-conforming even with the process being in control.

The variation in the output (conforming versus non-conforming) can be categorized into two groups:

1. Variation due to uncontrollable causes. By and large, nothing can be done about this source of variation, except to modify the process.
2. Variation due to assignable causes. This is due to a process going out of control, inputs not conforming to specifications and/or errors by human operators. This can be controlled through effective quality control schemes and process modifications (e.g., machine adjustment, replacement of worn out parts, and additional training of operators).

Quality control deals with controlling the variation resulting from assignable causes. In the case of process control, the approaches used can be broadly grouped into two categories (i) on-line and (ii) off-line. In the case of input quality control, a variety of techniques for accepting/rejecting have been proposed where the aim is to reject bad batches (that contain a high fraction of non-conforming components or the material properties do not meet the required specifications) and accept good batches (that contain a very small fraction of non-conforming components or material properties meet the required specifications).

To ensure that the actual performance AP-III matches the desired performance DP-III requires a proper quality control plan. Figure 8.2 shows the key elements of such a plan. It involves periodic sampling and testing of items (at component, final product, and at one or more intermediate sub-phases), monitoring of the process (inspection of equipment) and operations, to draw inference about input quality, process state and the actual performance AP-III. Inference is drawn on whether AP-III is in agreement with DP-III or not. If they are in agreement, the process continues with no change. If not, a root cause analysis is used to identify the cause and the corrective action needed. These different actions are indicated in Figure 8.2 and can involve on-line or off-line quality control, renegotiating with the supplier or even changing supplier.

# 8.3 Production Process and Occurrence of Non-conforming Items 

The type of manufacturing process used depends on the demand for the product and is determined by economic considerations. If the demand is high, then it is economical to use a continuous production process. If the demand is medium, then it is more economical to use a batch production process, where items are produced in lots (or batches). Finally, if the demand is low, then flexible manufacturing is used.

In all cases, the state of the manufacturing process has a significant impact on the occurrence of non-conforming items. As discussed earlier, the process state can

Figure 8.2. Quality control plan
be modelled as being in one of two possible states: (i) in control and, (ii) out of control. When the process state is in control, all the assignable causes are under control and the probability that an item produced is non-conforming is very small. Usually, this probability can be as small as $10^{-3}$ to $10^{-6}$ for properly designed production processes. The process state changes from in control to out of control due to one or more of the process parameters being no longer within the required interval. This increases the probability that an item is non-conforming.

# 8.3.1 Modelling Occurrence of Non-conforming Items 

The modelling of the occurrence of non-conforming items depends on the type of production process. We consider both continuous and batch production. Let $\phi_{0}$ and$\phi_{1}$ denote the probability that an item produced is conforming when the process is in control and out of control, respectively. In general, $\phi_{0} \gg \phi_{1} .^{1}$

# Continuous Production 

The production process starts in control and after a random length of time it changes to out of control. Once the process state changes from in control to out of control, it remains in that state until it is brought back to in control through some corrective action. The fraction of conforming items produced depends on the relative fractions of time the process is in control and out of control, respectively. This depends on the control plan to detect the change in process state. The change from in control to out of control can be either gradual or sudden as indicated in Figure 8.3.


Figure 8.3. Change in process state

## Batch Production

Let $Q$ denote the lot size. At the start of each lot production, the process state is checked to ensure that it is in control. If the process state is in control at the start of the production of an item, it can change to out of control with probability $1-v$, or stay in control with probability $v$. Once the state changes to out of control, it remains there until completion of the lot.

### 8.4 Effect of Quality Variations on Reliability Performance

We look at the case where the reliability performance of the product is modelled by a ROCOF function. Let the desired ROCOF (obtained from phase 3) be as indicated in Figure 8.4. This reliability is achieved through specifying the desired reliabilities

[^0]
[^0]:    ${ }^{1}$ Porteus (1986) considers the extreme case, $\phi_{0}=1$, implying that all items produced are conforming when the state is in control, and $\phi_{1}=0$, implying that all items produced are non-conforming when the process is out of control. Djamaludin et al. (1994) consider the general case where $0<\phi_{0} \leq 1,0 \leq \phi_{1}<1$ and $\phi_{0}>\phi_{1}$.for the various components of the product. Let $R_{c}(t)$ denote the desired reliability function for some conforming component (an element of DP-III). The associated failure distribution function is given by $F_{c}(t)=1-R_{c}(t)$.


Figure 8.4. Desired ROCOF (from phase 3)

# 8.4.1 Variation in Component Quality 

Let $F_{n}(t)$ denote the failure distribution of a non-conforming component and let $p$ denote the probability that the component is non-conforming. Note that $F_{n}(t)>$ $F_{c}(t)$, implying that the reliability performance of a non-conforming item is inferior to that of a conforming item. Then, the actual failure distribution function of the component (produced or bought from an external source) can be modelled by

$$
F_{a}(t)=(1-p) F_{c}(t)+p F_{n}(t)
$$

The actual component reliability, $R_{a}(t)=1-F_{a}(t)$, is an element of AP-III.
The effect of component non-conformance on the ROCOF is as shown in Figure 8.5. When $p=0$, the hump disappears as the ROCOF is unaffected. As $p$ increases, the hump becomes more pronounced.


Figure 8.5. Effect of component non-conformance on ROCOF# 8.4.2 Variations in Assembly Operations 

Even with all the components conforming to design specification, an item can fail early due to chance errors in the assembly operations (e.g., misalignment, dry solder joint). This failure can be viewed as a new failure mode with a decreasing failure rate. The effect of this failure mode on the ROCOF is as shown in Figure 8.6. As can be seen, this actual ROCOF has a higher value over the initial life of items indicating a higher likelihood of an early failure due to assembly errors which decreases with time. As a result, the ROCOF has a "bathtub" shape. These early failures are also


Figure 8.6. Effect of assembly error on ROCOF
termed "teething problems" or "infant mortality" and are detected within a relative short time period after an item is put into operation. In this case, the actual ROCOF, $\lambda_{a}(t)$ (an element of AP-III), is given by

$$
\lambda_{a}(t)=\lambda_{d}(t)+\lambda_{e}(t)
$$

where $\lambda_{d}(t)$ is the desired ROCOF (an element of DP-III) and $\lambda_{e}(t)$ is the failure rate associated with the failure distribution for the new failure mode with $\lambda_{e}(0)=q$. A higher value of $q$ corresponds to a higher likelihood of failure from assembly errors.

### 8.4.3 Combined Effects of Component Non-conformance and Assembly Errors

Since most products are complex involving several components and many different assembly operations, the net effect of quality variation on the actual ROCOF is as indicated in Figure 8.7. The shape of the ROCOF is often referred to as the "roller coaster" shape (Wong, 1989). Note that there can be several humps.

### 8.5 Testing During Production

The purpose of testing during manufacturing is to eliminate assembly errors, defects, and early component failures. The type of testing to be done depends on the product (electrical, mechanical or electronic). For very expensive products (e.g., commercial satellites) requiring a very high level of reliability, $100 \%$ testing would be employed.

Figure 8.7. Total effect of quality variations on ROCOF

For most other products (particularly consumer durables), only a very small fraction is tested.

The level of testing and the type of tests can change over the period of production. For a new product, in the early stages of production, considerable testing is required to establish the process characteristics and the effect of process parameters on the reliability of the product. As the product matures, the testing requirements are reduced. Testing is also done under various environmental conditions and often the tests are carried in an accelerated mode to reduce the time needed for testing. Two types of testing used are

1. Environmental stress screening
2. Burn-in

Environmental stress screening involves subjecting an item (component or assembly) to various environmental extremes to identify and eliminate manufacturing defects prior to customer use. Typical methods used are temperature cycling, random vibrations, electrical stress, thermal stress, and so on.

Burn-in is a process used to improve outgoing quality and is discussed in a later section.

Note. In some cases the testing takes very little time (e.g., measuring some physical characteristic such as tolerances or solder joint). In other cases, such as life testing, the test duration needs to be defined. In this case the test data is a combination of failure and censored data. For very highly reliable items we tend to use accelerated degradation tests. In this case, the test data is the condition (e.g., wear) of the item under test and from this we infer the useful life of the item. ${ }^{2}$

# 8.6 Quality Control 

The main aim of quality control is to ensure that the effect of quality variations is small so that the actual performance AP-III is fairly close to the desired performance

[^0]
[^0]:    ${ }^{2}$ For more details, see, for example Rausand and Høyland (2004); Nelson (1990).DP-III. This implies ensuring that $p$ in (8.1) and $q\left(=\lambda_{e}(0)\right)$ in (8.2) are below some specified upper limits. For process variations, the control can be achieved through off-line control and/or on-line control. For input quality variations, the control is achieved through proper rules for accepting/rejecting.

# 8.6.1 Off-line Control of Production Process 

As mentioned earlier, a production process is affected by several factors - some controllable and others not. Taguchi (1986) proposed a method for determining optimal settings for the controllable factors, taking into account the influence of the uncontrollable factors. The method uses well-known concepts from design of experiments combined with the concept of "signal-to-noise" ratio from electrical communication engineering. Since the pioneering work of Taguchi, there has been considerable development in the design of optimal and robust manufacturing processes. ${ }^{3}$

### 8.6.2 On-line Control of Production Process

The aim of on-line control is to prevent the occurrence of non-conforming items through actions that attempt to ensure that the process is in control during the production run. The approach used depends on the type of production process.

## Continuous Production

In continuous production, the process begins in control and may change to out of control with the passage of time. The aim is to detect the change and bring the process back in control as fast as possible. Control charts are used for this purpose.

The underlying principle of a control chart is simple. Samples of items are taken periodically and the sample statistics (e.g., sample mean, sample standard deviation, number or fraction non-conforming) are plotted. When the process is in control, the sample statistics should assume values within some specified interval with high probability. When the process goes out of control, it is more likely to assume values outside the specified interval. As such, plotting of the sample statistics provides a means for detecting the change in process state using some rules. Many different rules have been proposed for different charts.

Control charts can be grouped into two broad categories:
Variable charts: These are based on continuous-valued measurements (e.g., physical dimension, hardness).
Attribute charts: These are based on integer-valued measurements (e.g., counts of flaws, such as the number of dry solder joints).

There are many different variable and attribute charts. The more commonly used variable charts are (i) $\bar{X}$ chart, (ii) $R$ chart, and (iii) CUSUM chart, and for the

[^0]
[^0]:    ${ }^{3}$ Details can be found in many books; see for example, Dehnad (1989), Moen et al. (1991), and Peace (1993).attribute charts, the most commonly used charts are (i) $p$ chart and (ii) $n p$ chart. We briefly discuss the $\bar{X}$ chart. ${ }^{4}$ The control chart does not indicate the cause for the change in the state of the process and we need to use tools, such as root cause analysis, to determine the cause.

# $\bar{X}$ Chart 

Here the variable being observed is assumed to be normally distributed with mean $\mu$ and variance $\sigma^{2}$ when the process is in control. When the process goes out of control, either the mean changes and/or the variance increases. A sample of size $n$ is taken at regular intervals. Let $x_{j i}$ denote the observed value for the $i$ th item in sample $j$. Note that $j=1,2, \ldots$ and $i=1,2, \ldots, n$ for each $j$. The sample mean for sample $j$ is given by

$$
\bar{x}_{j}=\frac{1}{n} \sum_{i=1}^{n} x_{j i}
$$

This statistic is plotted on the control chart. The chart has a centre line and two control lines. The centre line is a horizontal line corresponding to the nominal mean $\mu$ or the overall sample mean (the average of the $\bar{x}_{j}$ 's). The two control lines (or control limits) are parallel to the centre line and at a distance $3 \sigma / \sqrt{n}$ on either side of the centre line. The two warning lines (or warning limits) are similarly drawn, but at a distance $2 \sigma / \sqrt{n}$ on either side of the centre line, as indicated in Figure 8.8.


Figure 8.8. Typical control chart

As mentioned earlier, if the sample plots lie within the control limits, we can conclude that the process is in control with high probability and no action is needed. When one or more sample plots fall outside the limits, this is taken as an indicator

[^0]
[^0]:    ${ }^{4}$ Most books on quality control discuss the different charts; see for example, Grant and Leavensworth (1988), Montgomery (1985), Sinha and Willborn (1985), Ryan (1989), and Evans and Lindsay (1996).of a change in the process state from in control to out of control. In fact, many rules have been developed to determine when a process is out of control and action is to be taken. Two such rules are:

Rule 1: A single point falling outside the control limits.
Rule 2: Two out of three points in a row falling above or below the warning line.
The instant at which action is initiated depends on the rule as indicated in Figure 8.8.
When it is inferred that the process is out of control, the process is stopped to check if a change has indeed occurred. If so, corrective actions to restore it to its in control state are initiated. If not, no corrective action is needed and production resumes. For any given stopping rule, there are two types of errors (or wrong decisions):

Type 1 error: A false alarm that leads to a stoppage of the production when the process is in control.
Type 2 error: Corrective action not being initiated for a certain length of time subsequent to the process changing from in control to out of control.

Ideally we would like to have the probabilities of both of these wrong decisions to be zero. Unfortunately, this is not possible and the probabilities depend on the rules used for initiating corrective actions. ${ }^{5}$

# Batch Production 

As indicated earlier, in batch production, the process starts in control and can go to out of control during the production of an item with probability $1-v$. This affects the number of non-conforming items in the lot. Let $N_{c}$ denote the number of conforming items in a lot. This is a random variable which can take on integer values in the interval $[0, Q]$. The expected fraction of conforming items in a lot of size $Q$ is given by $^{6}$

$$
\phi(Q)=\frac{v\left(\phi_{0}-\phi_{1}\right)\left(1-v^{Q}\right)}{(1-v) Q}+\phi_{1}
$$

where $\phi_{0}$ and $\phi_{1}$ denote the probability that an item produced is conforming when the process is in control and out of control, respectively.

It is easily seen that $\phi(Q)$ is a decreasing sequence in $Q$ implying that the expected fraction of conforming items in a batch decreases as the batch size $(Q)$ increases. This implies that the smaller the lot size, the better the outgoing quality. Finally, two special cases are:

$$
\begin{array}{ll}
Q=1: & \phi(Q)=\phi_{0} \\
Q=\infty: & \phi(Q)=\phi_{1}
\end{array}
$$

[^0]
[^0]:    ${ }^{5}$ There is a vast literature dealing with the determination of optimal rules that take into account the economic consequences of these two types of errors. These can be found in most books on statistical quality control.
    ${ }^{6}$ For details of the derivation, see Chapter 13 of Blischke and Murthy (2000).In the latter case, only a finite number of items are produced with the process being in control and an infinite number produced with the state being out of control.

# 8.6.3 Weeding Out Non-conforming Components 

The aim of weeding is to essentially detect non-conforming items through inspection and testing of each item. Testing can be done either at the component level, product level and/or at one or more of the intermediate levels of the production process. Detection of non-conformance at the earliest possible instant is desirable, as this allows for immediate corrective action. Some times a non-conforming item can be transformed into a conforming item by reworking it, and at other times, the item needs to be scrapped.

The quality of inspection and testing is another issue that needs to be considered. If inspection and testing are perfect, then every non-conforming item tested is detected. With imperfect testing and inspection, not only may a non-conforming item not be detected, but a conforming item may be classified as non-conforming. As a result, the outgoing quality (the fraction of conforming items) depends on the level of testing and the quality of testing.

## Component Level Weeding

When there is quality variation at the component level, the actual failure distribution of component lifetimes is given by (8.1). Weeding involves putting each component on a test bed so that it becomes operational. The duration of the test is $\tau$. Components that fail during testing are scrapped. The rationale for this is that non-conforming items are more likely to fail than conforming items and hence are weeded out.

The probability that a conforming (non-conforming) component will fail during testing for a period $\tau$ is given by $F_{c}(\tau)\left[F_{n}(\tau)\right]$. As a result, the probability that a component that survives the test is non-conforming is given by

$$
p_{1}=\frac{p R_{n}(\tau)}{(1-p) R_{c}(\tau)+p R_{n}(\tau)}
$$

where $R_{c}(\tau)=1-F_{c}(\tau)$ and $R_{n}(\tau)=1-F_{n}(\tau)$ denote the survivor functions of conforming and non-conforming components, respectively. Since $R_{c}(\tau)>R_{n}(\tau)$, we have $p_{1}<p$. The failure distribution of an item that survives the test is given by

$$
\bar{F}_{c}(t)=\left(1-p_{1}\right) \bar{F}_{c}(t)+p_{1} \bar{F}_{n}(t)
$$

where $\bar{F}_{c}(t)$ and $\bar{F}_{n}(t)$ are given by

$$
\bar{F}_{c}(t)=\frac{F_{c}(t+\tau)-F_{c}(\tau)}{1-F_{c}(\tau)}
$$

and

$$
\bar{F}_{n}(t)=\frac{F_{n}(t+\tau)-F_{n}(\tau)}{1-F_{n}(\tau)}
$$for $t \geq 0$. Note that as $\tau$ increases, $p_{1}$ (the probability that an item released is nonconforming) decreases, and hence the outgoing quality is improved. However, this is achieved at the expense of the useful life of conforming items released being reduced by an amount $\tau$.

# 8.6.4 Acceptance Sampling 

The input material (raw materials and components) is obtained from external suppliers in batches. The quality for raw material is defined through some characteristics (e.g., strength, chemical composition) and for components it is the reliability. The quality of input material can vary from batch to batch. A batch is defined to be unacceptable if the quality does not meet the specified value (e.g., mean time to failure, or the fraction or number of conforming items in the batch, is below some specified value). Such batches need to be rejected. Batches for which the quality meets or exceeds the specified value (e.g., mean time to failure, or the fraction or number of conforming items, is above some specified value) are to be accepted.

The decision to accept or reject a batch is based on testing a small sample from the batch. This is known as acceptance sampling. A variety of acceptance sampling schemes for attribute (integer valued measurements) and variables (continuousvalued measurements) can be found in the literature. They can be divided into three groups: (i) single-sampling, (ii) multiple-sampling, and (iii) sequential-sampling. ${ }^{7}$

The single sampling by attribute plan involves taking a random sample of $n$ items from a lot of size $N$. Let $d$ (called the sample number) denote the number of items that are non-conforming (e.g., have a defect or fail during the test period). This is compared with a pre-specified number $c$ (called the acceptance number) to decide whether to accept or reject a batch. If $d \leq c$, the batch is accepted and if $d>c$, the batch is rejected.

In a double-sampling scheme, a first sample of size $n_{1}$ is drawn from the batch and tested. Let $d_{1}$ denote the number of non-conforming items. The outcome action is as follows:

If $d_{1} \leq a_{1}$, the batch is accepted.
If $d_{1}>r_{1}$, the batch is rejected.
If $a_{1}<d_{1} \leq r_{1}$, a second sample is drawn.
The second sample involves drawing randomly $n_{2}$ items from the batch. Let $d_{2}$ denote the number of non-conforming items in the sample. The outcome action is as follows:

If $d_{1}+d_{2} \leq a_{2}$, the batch is accepted.
If $d_{1}+d_{2}>a_{2}$, the batch is rejected.
The extension to multiple sampling is a natural extension of this and can involve drawing more than two samples.

[^0]
[^0]:    ${ }^{7}$ Most books on quality control discuss some of the sampling schemes. A detailed discussion of the different schemes can be found in Schilling (1982)In sequential sampling, the sample size is one and the outcome (accept, reject or continue sampling) is decided after each sample is tested.

As in the case of control charts, we can make two types of errors.
Type 1 error: Rejecting a batch that should have been accepted.
Type 2 error: Accepting a batch that should have been rejected.
Ideally, we would like to have the probabilities of both of these wrong decisions to be zero. Unfortunately, this is not possible. In the case of single-sample scheme, the probabilities depend on the parameters $d$ and $c$ (and the duration of test in the case of life testing).

# 8.6.5 Sub-set Selection 

A manufacturer can often select the component supplier from several component manufacturers. The reliability of the components differs across component manufacturers and the problem facing the manufacturer is to select the best component supplier. This problem can be posed as selecting the best population from a collection of populations and is called the sub-set selection problem. In order to do this, we need to define more precisely the notion of "best" and several different notions have been proposed and studied. ${ }^{8}$

### 8.6.6 Burn-in

When variations in assembly operations are significant, the ROCOF function for the product has the bathtub shape (see Figure 8.6). Let $\lambda(t)$ denote this bathtub function with $\lambda(t)$ decreasing for $0 \leq t \leq t_{1}$. As a result, if produced items are released without any further action, a high fraction would fail in the early period, leading to high warranty costs and loss of customer goodwill. In this case, burn-in can be used to improve product reliability by consuming a part of the lifetime. The approach is to test each item for a period $\tau$ prior to its sale. Any items that fail within this period are minimally repaired. If the time to repair is small (in relation to $\tau$ ), so that it can be ignored, then the ROCOF function is unaffected by failure and repair action.

Let the ROCOF function after burn-in be given by $\tilde{\lambda}(t)$. Then $\tilde{\lambda}(t)=\lambda(t+\tau)$ for $t \geq 0$. By choosing $\tau=t_{1}, \tilde{\lambda}(t)$ is no longer bathtub shaped and has a shape similar to that shown in Figure 8.4. For more on burn-in, see Jensen and Peterson (1982).

Burn-in results in additional costs due to (i) fixed set-up cost of the burn-in facility, (ii) variable cost (which increases with $\tau$ ) for testing each item, and (iii) rectification cost for failures during burn-in. Hence, burn-in is worthwhile only if its benefits (measured in terms of the improvements in reliability) exceed the cost of burn-in.

[^0]
[^0]:    ${ }^{8}$ There is an extensive literature on this topic. The earlies paper is by Rademaker and Antle (1975) and looks at the optimal sample size to decide which of the two populations have the larger reliability. Kingston and Patel (1980a,b) focus on selecting the population with the largest reliability based on type II censoring. The shape parameter can be the same or different and needs to be estimated. Later papers include Hsu (1982), Sirvanci (1986), Gupta and Miescke (1987), and Gill and Mehta (1994).# 8.7 Optimal Quality Control Effort 

The quality (defined in terms of conformance) of items produced depends on the quality control effort. The quality improves as the effort is increased, but this is achieved at the expense of increased quality control cost.

In the case of batch production, the quality $\phi(Q)$ increases as the batch size $Q$ increases. This implies that the smaller the lot size, the better the outgoing quality. On the other hand, the size of the lot has implications with regard to unit manufacturing cost, since each batch production results in a fixed set-up cost. This implies that it is necessary to determine the optimal lot size by a proper trade-off between this cost and the benefits derived through better outgoing quality.

In the case of weeding, if a non-conformance is not detected at the earliest possible instant, the effort involved until it is detected is either wasted (if the item has to be scrapped) or the amount of rework required to make it conforming increases (if the non-conforming item can be fixed). Both result in extra cost. On the other hand, testing and inspection also cost money and it is necessary to achieve a suitable balance between these two costs. This implies that the location of inspection and testing stations in a production process needs to be optimally selected.

In the case of burn-in, it is necessary to determine $\tau$ optimally so that a sensible trade-off is achieved between the cost of testing and the benefits derived through improvements in the quality of outgoing products.

Determining the optimal level of quality control effort must take into account the trade-off between the cost of quality control and the benefits derived. In the context of reliability, the benefits of higher quality (conformance) are higher customer satisfaction and lower warranty costs. Figure 8.9 shows the trade-off between warranty costs and quality control costs and we need to build models to determine the optimal quality effort. There is a vast literature on this topic. ${ }^{9}$

### 8.8 Case Study: Cellular Phone

In this section, we discuss the effect of manufacturing on product reliability by looking at manufacturing of chips and shell (outer casing) of a cellular phone.

## Chips

The chip manufacturing involves several stages. The first stage is to produce the wafers. These are then cut to produce dies and these are packaged to produce chips. The chip reliability is strongly influenced by the production process. Kuo and Kim (1999) classify failures of chips into the following three categories:

[^0]
[^0]:    9 - Optimal batch size: Djamaludin et al. (1994, 1995, 1997); Chen et al. (1998); Yeh and Lo (1998); Yeh et al. (2000)

    - Acceptance sampling: Schneider (1989); Kwon (1996); Hisada and Arizino (2002); Huei (1999)
    - Burn-in: Murthy et al. (1993); Blischke and Murthy (1994); Murthy (1996); Mi (1997); Kar and Nachlas (1997)

Figure 8.9. Investment in quality control effort

1. Electrical stress failures (e.g., electrical overstress, electrostatic discharge) are due to design and/or misuse of the chips.
2. Inherent failures (e.g., crystal defects, dislocations and processing defects, gate oxide breakdown, ionic contamination, surface charge spreading) tend to be the result of wafer production.
3. Extrinsic failures (e.g., die attachment failure, particulate contamination) tend to be the result of operations during device packaging.

Early failures are a result of poor design, improper manufacturing and/or incorrect use. This manifests as a failure rate which starts with a high value and decreases over the initial period (referred to as the infant mortality period). This period is typically around one year, after which the failure rate is constant over a fairly long period, which is around $40-50$ years.

# Burn-in 

During manufacturing, infant mortality failures are removed through an accelerated burn-in process. Since the majority of chip failures is due to temperature, the burnin involves applying high temperature and voltage to weed out items prone to early failure. The burn-in (BI) can be done at wafer lever (WLBI), die level (DLBI) or package level (PLBI).

Several questions need to be addressed in deciding on the burn-in strategy to weed out infant mortality failures. These include:

1. What should be the duration of burn-in?
2. What levels of temperature and voltage should be used in burn-in?
3. Should burn-in be done at wafer, die and/or package levels?

A proper cost-benefit analysis is needed to find answers to these questions through use of models. Kuo and Kim (1999) discuss burn-in conditions and types for semiconductor products and compare three types of burn-in.# Yield 

Yield is defined as the ratio of the usable (or conforming) items to the number of items produced. Kuo and Kim (1999) characterize the semiconductor process in terms of the following sub-processes:

- Crystal growth process
- Front-end fabrication process
- Wafer probe
- Assembly and packaging
- Final testing

The wafer process yield is the yield of the first two sub-processes, wafer probe yield, assembly yield and final test yield refers to the yields of the remaining three subprocesses. The overall yield is the product of these four yields. ${ }^{10}$ Typical average figures for the various yields (as reported in Kuo and Kim (1999)) are as given below:

| Wafer process yield | $94 \%$ |
| :-- | :-- |
| Wafer probe yield | $50 \%$ |
| Assembly yield | $96 \%$ |
| Final test yield | $90 \%$ |

Yield and reliability are closely linked as total wafer yield is a measure of good chips per wafer normalized by the number of chip sites per wafer. The yield is assessed through quality control scheme (involving $100 \%$ inspection and testing) and the yield-reliability model helps in assessing the reliability of the end product. ${ }^{11}$

[^0]
[^0]:    ${ }^{10}$ Cunningham et al. (1995) suggest line yield, die yield and final test yield to obtain the overall yield.
    ${ }^{11}$ See Ferris-Prabhu (1992); Hnatek (1995) for more details of yield and modelling yield in semiconductor devices.# Post-sale Performance 



### 9.1 Introduction

This chapter deals with reliability performance during phases 7 (stage III, level II) and 8 (stage III, level I) of the product life cycle. In phase 7, we look at reliability performance in the field (AP-II) after the product has been sold. This performance is influenced by several factors, most of which are beyond the control of the manufacturer. In phase 8 , we look at the impact of the field reliability on the actual overall business performance AP-I. This actual performance needs to be compared with the desired performance DP-II in phase 2 and DP-I in phase 1 to make appropriate decisions. In this chapter, we look at all of these issues for phases 7 and 8 .

The outline of the chapter is as follows. Section 9.2 deals with reliability performance in phase 7 for standard products. We discuss issues related to the field data needed to assess the actual performance AP-II and the process to initiate actions if AP-II differs from the desired performance DP-II. Section 9.3 looks at assessing the design and the inherent reliability based on field data. Section 9.4 deals with reliability performance in phase 8 for standard products. We look at the data needed to assess the actual performance AP-I and the process to initiate actions should this differ from the desired performance DP-I. Section 9.5 looks at the performance in phases 7 and 8 for custom-built products. Finally, a case study on cellular phones is presented in Section 9.6.

### 9.2 Phase 7 for Standard Products

The reliability performance in phase 7 depends on the reliability of the produced product and on several other factors. We discuss these factors and their influence on field reliability first. We then discuss the various elements of the process in phase 7. The assessment of field reliability poses some interesting challenges and these are discussed later in the section.# 9.2.1 Field Performance 

The design reliability depends on the reliability specification that was discussed in Chapter 6, and this in turn depends on the business objectives discussed in Chapter 5. The reliability of the produced item can differ from the design reliability due to assembly errors and component non-conformance as discussed in Chapter 8. This is the inherent reliability of the product.

The product needs to be transported to the market, and often stored for some time, before it is sold. The reliability at sale for a unit depends on the mechanical load (e.g., from vibrations), the impact load (e.g., from mishandling), the duration of storage and the storage environment (e.g., temperature, humidity). ${ }^{1}$ As a result, the reliability at sale can differ from the inherent reliability and the reliability degradation will depend on the influence of the various factors mentioned earlier.

Once an item is sold, it can be either stored for an additional time (e.g., if the unit is used as a spare) or put into operation immediately. As a result, the reliability performance of a unit depends on the length and environment of storage and on several other operational factors such as the usage intensity (which determines the load - electrical, mechanical, thermal, chemical - on the unit), mode (whether used continuously or intermittently) and operating environment (e.g., temperature, humidity, vibration, pollution), and sometimes on the human operator. The reliability performance in operation is often referred to as the field reliability. Figure 9.1 shows how these different reliability notions are sequentially linked and the factors that affect them.


Figure 9.1. Factors influencing field reliability

In Chapter 8, we discussed the influence of the factors in production on the ROCOF. The effect is that the ROCOF of produced items, $\lambda_{p}(t)$, can exhibit a roller coaster shape shown in Figure 9.2 and differ from the desired design ROCOF, $\lambda_{d}(t)$, if the quality control during production is not very effective. The factors affecting

[^0]
[^0]:    ${ }^{1}$ Ramakrishnan and Pecht (2004) discuss the load characterization during transportation.field reliability can push the (field) ROCOF upwards as indicated by $\lambda_{f}(t)$ in the figure. Good reliability design must take these factors into account in the overall design process so that when they are within the specified limits, the inherent and field reliabilities match the desired reliability and any deviations are mainly due to these factors deviating from the specified limits and needing some corrective actions.


Figure 9.2. ROCOF - design, production, and field

# 9.2.2 Decision Process in Phase 7 

The process in phase 7 is shown in Figure 9.3. It involves collecting data on a continuous basis. The data is analysed to assess the field reliability AP-II and this is compared with the desired reliability DP-II (defined in phase 2). If the two are in reasonable agreement, then no corrective action is needed and we continue with the data collection and analysis cycle. However, if there is significant disagreement between the two, then the problem can be either production and/or design related. The detection of the problem involves root cause analysis and based on the outcome, we either revert back to phase 6 (if it is a production problem) or to phase 3 (if it is a design problem) for further actions.

### 9.2.3 Data Collection

Data in phase 7 is collected for the following two purposes:

1. To check if the actual performance AP-II matches the desired performance DP-II or not.
2. To identify the cause if there is a mismatch so that appropriate action to rectify the problem can be initiated.

The data needed for the two are different. For comparing AP-II with DP-II, the data required is the age at failure. This generates information regarding the time between failures and this is used to obtain an estimate of the ROCOF. Often, the observed failure times will differ from the true values due to various uncertainties. Figure 9.4

Figure 9.3. Performance evaluation and decision making in phase 7
shows the various uncertainties associated with the time to first failure. They are as follows:
$\widetilde{Z}_{1}$ : This is uncertainty in the gap between the date of sale and the date of production. This result, because the manufacturer knows the former and not the latter in the case when there is no failure during the warranty period. Should a unit fail within the warranty period, then the manufacturer obtains the sale date through the service agent servicing the warranty.
$\widetilde{Z}_{2}$ : Often, customers might not put the unit into operation soon after purchase. This would be the case when the customer buys a unit as a spare. In this case, the gap between the sale date and the date put into operation is uncertain and the manufacturer can seldom obtain this information.
$\widetilde{Z}_{3}$ : In some instances, the reporting date for a failure can differ from the actual failure date for a variety of reasons. In the case of a cellular phone, this might be the loss of picture transmission that a customer might view as not being critical as the phone is used mainly for sending voice and text messages.
As a result, the observed time to first failure $T_{1}$ differs from the true time to failure $\widetilde{T}_{1}$ with $T_{1}-\widetilde{T}_{1}=\widetilde{Z}_{2}+\widetilde{Z}_{3}$. If these uncertainties are small relative to mean time between failures, then they can be ignored so that $T_{1} \approx \widetilde{T}_{1}$.

The data needed for identifying the cause if there is a mismatch in AP-II and DPII is more detailed. In addition to the age at failure, we need the component(s) that failed, the age of the component(s), the cause of failure and other information such as operating environment and condition. For non-repairable components, the data is used to obtain estimates of the failure distribution for the components.

Here again, there can be various uncertainties similar to that discussed earlier.

Figure 9.4. Delays leading to uncertainties in the data collection

Soon after a product is launched in the market, the data available are the warranty claims data. ${ }^{2}$ These yield information regarding units that fail under warranty. To obtain an estimate of ROCOF, we also need the information about the units that are in operation - their numbers and the age of each. In many cases, the manufacturer might only have aggregated sales (e.g., sales per week, month) and not the sale date for each. In this case, some of the relevant information (e.g., age of individual units) is lost through aggregation and has an impact on the accuracy of the estimate. Once a unit is no longer under warranty, the failure data available to the manufacturer decreases significantly. One of the main reasons is that failed units are often repaired by independent businesses providing the repair services. These businesses do not collect the information that is useful for determining the product reliability. In some instances, the manufacturer can get this information by paying the repair businesses to collect data. However, there can be credibility problems with the data collected as it involves extra time and effort from these repair businesses whose interests are not the same as that of the manufacturer. However, some indirect data are obtained through monitoring the sale of spare parts to retailers. These data are often the aggregated sales of different parts in different time periods. Again, there is uncertainty in terms of number of spares used as retailers often hold inventories of parts to meet customer demands.

As can be seen, there can be several problems with data collection. The main one being that often not all the relevant data are collected. Even if they are collected, they might be stored in different databases that do not communicate with each other. Also, errors in the entry into the database can lead to incorrect data. These issues are discussed further in Chapter 11.

# 9.2.4 Analysis of Data and Estimating AP-II 

The analysis of data for estimating the actual performance AP-II needs to be done at the product level. The two approaches that can be used are (i) parametric and (ii) non-parametric. In the former case, we assume a functional form (for the ROCOF or failure distribution) and estimate the parameters of the formulation using the data.

[^0]
[^0]:    ${ }^{2}$ Jauw and Vassilou (2000) discuss data acquisition systems for collecting data for field reliability information.In the latter case, we compute the empirical ROCOF or the empirical distribution function using the data.

The data consists of failure data and censored data. As mentioned earlier, the main source of data is the warranty data and this provides information about product reliability during the early stages of its life. ${ }^{3}$ Most products are sold with onedimensional warranty (where the product is covered for a period $W$ from the date of sale) and few (e.g., cars, photocopiers) are sold with two-dimensional warranty (with the warranty expiring when the age exceeds $W$ or the usage exceeds $U$ whichever occurs first).

In the case of products sold with one-dimensional warranty, Figure 9.5 shows the failure $\left(T_{1}, T_{2}\right)$ and the censored $(\bar{Z})$ data. As can be seen, we can obtain the censored data given the failure data and the warranty period. Again, there can be uncertainty if a failure close to the end of the warranty, is not executed by the customer. In this case, information about the failure is lost and there is no censoring. In the case of products sold with a two-dimensional warranty, there is a complicating factor. Figure 9.6 illustrates this. Here, the age and usage at first failure are given by $\left(T_{1}, U_{1}\right)$ and there are no further warranty claims. There is uncertainty in the usage (case (b)) should the warranty expire due to the age limit or in the age (case (a)) should the warranty expire due to the usage limit. As a result, the censoring is random.


Figure 9.5. Censored data (1-D warranty)


Figure 9.6. Censored data (2-D warranty)

[^0]
[^0]:    ${ }^{3}$ See Spiegler and Herniter (1993) for a discussion on warranty as a source of information.In the non-parametric approach, the estimate of ROCOF, $\hat{\lambda}(t ; \tau), 0 \leq t<\tau$, is obtained using the data from the interval $[0, \tau)$, where the origin corresponds to the launch of the product in the market. The data available changes with $\tau$ for reasons discussed earlier. This needs to be properly taken into account in order to obtain credible estimates.

When the product is sold in different markets that differ significantly in the operating environment and/or usage profiles of customers, then we should estimate the field reliability for each market separately. By pooling, the effect of the variations in usage intensity and/or operating environment can become dominant and affect the credibility of the estimates.

Estimating field reliability (at product or component levels) taking into account some of the uncertainties discussed earlier has received considerable attention. Books dealing with some of the issues include Lawless (1982), Meeker and Escobar (1998), and Nelson (2003). There are several papers that deal with this topic. ${ }^{4}$

Example 9.1. A modern photocopier ${ }^{5}$ is a complex system involving several components. The data recorded from a four and half-year service history of a photocopier are given in Table 9.1, and consist of the age at failure, the number of copies made at failure and the components that were replaced at failure.

# Product Level Analysis 

From the data, we can compute the times and the number of copies made between failures. The days and copies between failures are strongly correlated $(r=0.916)$.

[^0]
[^0]:    ${ }^{4}$ For a general discussion, see Suzuki (1985a,b), Walls and Bendell (1986), Ansell and Phillips (1989), Kalbfleisch et al. (1991), Robinson and McDonald (1991), Lawless and Kalbfleisch (1992), Suzuki (1995), Lawless (1998), Suzuki et al. (2001), Karim and Suzuki (2005), and Fredette and Lawless (2007). There are many other papers dealing with specific issues and these include:

    - Automotive failure data: Majeske and Herrin (1995), Lawless et al. (1995), Lu (1998), Hipp and Lindner (1999),Guida and Pulcini (2002), Majeske (2003), and Rai and Singh (2003).
    - Case studies: Lyons and Murthy (1996), Iskander and Blischke (2003), and Sander et al. (2003).
    - Censored data: Nachlas and Kumar (1993), Hu et al. (1998), and Escobar and Meeker (1999).
    - Count data: Karim et al. (2001c)
    - Discrete time data: Stevens and Crowder (2004)
    - Grouped data: Coit and Dey (1999) and Coolen and Yan (2003).
    - Post-warranty data: Oh and Bai (2001)
    - Sale data information: Wang and Suzuki (2001a,b), and Wang et al. (2002).
    - Supplementary information on covariates and censoring time:
    - Truncated data: Kalbfleisch and Lawless (1992) and Hu and Lawless (1996).
    - Unclean data: Rai and Singh (2003).
    - Others: Landers and Kolarik (1987) and Suzuki (1987).
    ${ }^{5}$ This example is taken from Bulmer and Eccleston (2003) with permission from the authors.Table 9.1. Photocopier failure data (from Bulmer and Eccleston, 2003)

| Count | Day | Component | Count | Day | Component |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 60152 | 29 | Cleaning web | 769384 | 1165 | Feed rollers |
| 60152 | 29 | Toner filter | 769384 | 1165 | Upper fuser roller |
| 60152 | 29 | Feed rollers | 769384 | 1165 | Optics PS felt |
| 132079 | 128 | Cleaning web | 787106 | 1217 | Cleaning blade |
| 132079 | 128 | Drum cleaning blade | 787106 | 1217 | Drum claws |
| 132079 | 128 | Toner guide | 787106 | 1217 | Toner guide |
| 220832 | 227 | Toner filter | 840494 | 1266 | Feed rollers |
| 220832 | 227 | Cleaning blade | 840494 | 1266 | Ozone filter |
| 220832 | 227 | Dust filter | 851657 | 1281 | Cleaning blade |
| 220832 | 227 | Drum claws | 851657 | 1281 | Toner guide |
| 252491 | 276 | Drum cleaning blade | 872523 | 1312 | Drum claws |
| 252491 | 276 | Cleaning blade | 872523 | 1312 | Drum |
| 252491 | 276 | Drum | 900362 | 1356 | Cleaning web |
| 252491 | 276 | Toner guide | 900362 | 1356 | Upper fuser roller |
| 365075 | 397 | Cleaning web | 900362 | 1356 | Upper roller claws |
| 365075 | 397 | Toner filter | 933637 | 1410 | Feed rollers |
| 365075 | 397 | Drum claws | 933637 | 1410 | Dust filter |
| 365075 | 397 | Ozone filter | 933637 | 1410 | Ozone filter |
| 370070 | 468 | Feed rollers | 933785 | 1412 | Cleaning web |
| 378223 | 492 | Drum | 936597 | 1436 | Drive gear D |
| 390459 | 516 | Upper fuser roller | 938100 | 1448 | Cleaning web |
| 427056 | 563 | Cleaning web | 944235 | 1460 | Dust filter |
| 427056 | 563 | Upper fuser roller | 944235 | 1460 | Ozone filter |
| 449928 | 609 | Toner filter | 984244 | 1493 | Feed rollers |
| 449928 | 609 | Feed rollers | 984244 | 1493 | Charging wire |
| 449928 | 609 | Upper roller claws | 994597 | 1514 | Cleaning web |
| 472320 | 677 | Feed rollers | 994597 | 1514 | Ozone filter |
| 472320 | 677 | Cleaning blade | 994597 | 1514 | Optic PS felt |
| 501550 | 722 | Upper roller claws | 1005842 | 1551 | Upper fuser roller |
| 501550 | 722 | Cleaning web | 1005842 | 1551 | Upper roller claws |
| 501550 | 722 | Dust filter | 1005842 | 1551 | Lower roller |
| 501550 | 722 | Drum | 1014550 | 1560 | Feed rollers |
| 501550 | 722 | Toner guide | 1014550 | 1560 | Drive gear D |
| 533634 | 810 | TS block front | 1045893 | 1583 | Cleaning web |
| 533634 | 810 | Charging wire | 1045893 | 1583 | Toner guide |
| 583981 | 853 | Cleaning blade | 1057844 | 1597 | Cleaning blade |
| 597739 | 916 | Cleaning web | 1057844 | 1597 | Drum |
| 597739 | 916 | Drum claws | 1057844 | 1597 | Charging wire |
| 597739 | 916 | Drum | 1068124 | 1609 | Cleaning web |
| 597739 | 916 | Toner guide | 1068124 | 1609 | Toner filter |
| 624578 | 956 | Charging wire | 1068124 | 1609 | Ozone filter |
| 660958 | 996 | Lower roller | 1072760 | 1625 | Feed rollers |
| 675841 | 1016 | Cleaning web | 1072760 | 1625 | Dust filter |
| 675841 | 1016 | Feed rollers | 1072760 | 1625 | Ozone filter |
| 684186 | 1074 | Toner filter | 1077537 | 1640 | Cleaning web |
| 684186 | 1074 | Ozone filter | 1077537 | 1640 | Optic PS felt |
| 716636 | 1111 | Cleaning web | 1077537 | 1640 | Charging wire |
| 716636 | 1111 | Dust filter | 1099369 | 1650 | TS block front |
| 716636 | 1111 | Upper roller claws | 1099369 | 1650 | Charging wire |

A plot of the time between failures and failure number is indicated in Figure 9.7. This suggests that the reliability of the copier is decreasing with age and that failures over time can be modelled by a ROCOF function given by

$$
\lambda(t)=\left(\frac{t}{\beta}\right)^{\alpha}
$$

with the scale parameter $\beta=157.5$ days and the shape parameter $\alpha=1.55$. A

Figure 9.7. Mean time between failures
plot of the cumulative ROCOF (which gives the expected number of failures) and the count of failures over time are shown in Figure 9.8. As can be seen, the fit is reasonable indicating that the Weibull ROCOF model is appropriate for modelling failures and reliability at the product level.


Figure 9.8. Weibull ROCOF model fit

# Component Level Analysis 

A Pareto plot of the failures is shown in Figure 9.9. As can be seen, the component that had the maximum number of failures was the cleaning web. The age of thephotocopier and number of copies made at different failures of the cleaning web are given in Table 9.2. Whenever the cleaning web fails, it needs to be replaced by a new one. The difference in the age and the copies made yields the age of the cleaning web at failure and the number of copies made before failure.

# Copier Failure Modes 



Figure 9.9. Pareto analysis of failures

Table 9.2. Failure data for cleaning web (from Bulmer and Eccleston, 2003)

| Copies | Age (days) | Copies | Age (days) |
| :--: | :--: | :--: | :--: |
| 60152 | 29 | 900362 | 1356 |
| 132079 | 128 | 933785 | 1412 |
| 365075 | 397 | 938100 | 1448 |
| 427056 | 563 | 994597 | 1514 |
| 501550 | 722 | 1045893 | 1583 |
| 597739 | 916 | 1068124 | 1609 |
| 675841 | 1016 | 1077537 | 1640 |
| 716636 | 1111 |  |  |

The failure distribution can be modelled as a function of age $(t)$ or usage $(u)$ at failure. Let $F(t)$ and $G(u)$ denote these two distributions. Murthy et al. (2004a)discuss different Weibull based models to model this data set. ${ }^{6}$ The best models were as follows.

Based on Age at Failure:

$$
F(t)=\left(1-e^{-\left(t / \beta_{1}\right)^{\alpha_{1}}}\right)\left(1-e^{-\left(t / \beta_{2}\right)^{\alpha_{2}}}\right)
$$

This is the Weibull multiplicative model and the parameter values (obtained by least squares fit) are as follows: $\widehat{\alpha}_{1}=6.62, \widehat{\alpha}_{2}=1.29, \widehat{\beta}_{1}=28.8$, and $\widehat{\beta}_{2}=128$. The WPP plot of the data and of the model is shown in Figure 9.10.


Figure 9.10. WPP plots for Weibull multiplicative model [based on days between failures]

Based on Usage at Failure:

$$
G(u)=p\left(1-e^{-\left(u / \beta_{1}\right)^{\alpha_{1}}}\right)+(1-p)\left(1-e^{-\left(u / \beta_{2}\right)^{\alpha_{2}}}\right)
$$

This is the Weibull mixture model and the parameter values (obtained by least square fit) are as follows: $\widehat{\alpha}_{1}=0.851, \widehat{\alpha}_{2}=5.53, \widehat{\beta}_{1}=79400, \widehat{\beta}_{2}=67900$, and $\widehat{p}=$ 0.674 . The WPP plot of the data and of the model is shown in Figure 9.11.

[^0]
[^0]:    ${ }^{6}$ For a discussion of the different Weibull models, see Murthy et al. (2003).

Figure 9.11. WPP plots for Weibull multiplicative model [based on number of copies between failures]

# 9.2.5 Root Cause Analysis 

The actual performance AP-II can differ from the desired performance DP-II because of one or more problems. Define $\psi(t)=\lambda_{a}(t)-\lambda_{d}(t)$, that is, the difference between the actual and the desired ROCOF.

Assembly error problem: In this case, $\psi(t)$ is a decreasing function of $t$ over the interval $[0 . \tau)$.
Component non-conformance problem: In this case, $\psi(t)$ is a convex function (initially increasing and then decreasing) over one or more intervals along the time axis.
Design problem: In this case, either $\psi(t)$ is a constant (greater than zero) or is an increasing function of $t$ towards the end of the designed life of the product.

Figure 9.12 illustrates the case where all of these problems are present. In region A, the difference is due to assembly error problems; in region B it is due to component non-conformance problem and in regions C and D it is due to design problems.

Note. If there is only assembly error problem, then $\psi(t)$ is close to zero for regions B, C, and D. Similarly, if there is only a component non-conformance problem, then $\psi(t)$ is zero in regions A, C, and D. Finally, if two or more components are nonconforming then can have more then one hump and the actual ROCOF can have more than one peak.

Once the cause of the problem has been identified, the next step is to carry out more detailed analysis. In the case of an assembly error problem, it involves going back to phase 6 to carry out a detailed examination of the production process to identify the cause and come up with corrective actions to fix the problem. In the case of component non-conformance, it involves again going back to phase 6 to either

Figure 9.12. Root cause analysis in phase 7
tighten the acceptance sampling procedure and/or offer better incentive schemes for vendors to deliver high quality components. Finally, in the case of a design problem, we need to go to phase 3 to re-evaluate the design in light of the failure data and to come up with design changes. If the change is minor, then we proceed to phase 4 to make the changes to the production. However, if the changes to be made are major (in the sense that major investment is needed for development and/or new technology acquisition) then we proceed back to phase 1 so that top management can decide on the future course of action.

The tools and techniques used in carrying out the root cause analysis is mainly qualitative - use of Pareto analysis, fish-bone diagrams, and so on. ${ }^{7}$ Various statistical techniques (such as hypothesis testing) play an important role in determining whether the value of $\psi(t)$ (at some point or over an interval) is significantly different from zero or not. There are a few papers that deal with the use of warranty and field data to detect reliability problems. ${ }^{8}$

The analysis for assembly error and component non-conformance problems needs to be done separately for each batch due to variations from batch to batch. Once batches with significant problems are identified, the data from these batches can be pooled to get a better estimate of $\psi(t)$ and to identify the root cause. A design problem affects all batches and as such data from all the batches can be pooled for proper analysis.

[^0]
[^0]:    ${ }^{7}$ Most books on quality improvement (e.g., Wadsworth et al. (2002)) discuss these and other techniques.
    8 These include:

    - Detection of reliability problems: Wu and Meeker (2002)
    - Detecting change-point: Karim et al. (2001b,a)
    - Design changes: Majeske et al. (1997); Majeske and Herrin (1995), and Ward and Christer (2005)# 9.3 Assessing Inherent and Design Reliability 

The analysis in Section 9.2.4 is to assess the field reliability based on warranty and other field data relating to product failures. As indicated in Figure 9.1, the field reliability can be different from the inherent reliability and the design reliability. Often, we are interested in obtaining estimates of these reliabilities based on product data obtained from the field. These are needed to assess the design process and/or the production process. Also, it provides useful information for future improvements in the overall new product development process. This involves discounting for the factors that link inherent reliability to field reliability and the factors that link design reliability to inherent reliability. The process involved is shown in Figure 9.13.


Figure 9.13. Assessing inherent and design reliabilities

The analysis involves additional information relating to the various influencing factors and models that characterize the effects of these factors. In Chapter 8, we discussed the link between inherent reliability and design reliability and the effect of the influencing factors. ${ }^{9}$

### 9.4 Phase 8 for Standard Products

The reliability performance in phase 8 is the actual performance AP-I viewed from the business perspective - in other words, the actual impact of product reliability on the overall business objectives as defined through DP-I in phase 1.

### 9.4.1 Decision Process in Phase 8

The process in phase 8 is indicated in Figure 9.14. It is similar to the process in phase 7 in the sense that data are collected and analysed to assess the actual performance AP-I on a continuous basis. This is then compared with the desired reliability DP-I. If the two are in agreement, then no corrective action is needed and we continue with

[^0]
[^0]:    ${ }^{9}$ The effect of the factors that link the reliability at sale to the inherent reliability has received very little attention and is a topic that needs attention in the future.the data collection and analysis cycle. However, if there is disagreement between the two, then the problem can be product, customer or market related. The identification of the problem involves root cause analysis and based on the outcome, we either revert back to phase 1,6 , or 7 for further actions.


Figure 9.14. Performance evaluation and decision making in phase 8

# 9.4.2 Data Collection 

As in phase 7, the data (in phase 8) are collected for the following two purposes:

1. To check if the actual performance AP-I matches the desired performance DP-I or not.
2. To identify the cause if there is a mismatch so that appropriate action to rectify the problem can be initiated.

Product related data comes from phase 7 and this is discussed in the previous section. The customer related data (regarding satisfaction/dissatisfaction) comes partly from phase 7 (as part of warranty servicing data) but often needs to be collected from other sources such as customer surveys, consumer magazines, consumer groups, and so on. Customer surveys can be costly and the feedback obtained depends on thequestionnaire. ${ }^{10}$ This topic has received a lot of attention in the marketing literature. Market related data can be grouped into two categories - internal data and external data. The internal data consists of sales, revenue, various costs (production, marketing, warranty, etc.) reported on a periodic basis (weekly, monthly or quarterly). The external data comprises relevant competitor related data and other economic data (such as the economy, changing trends, and so on, in different regions where the product is marketed). This information is obtained from various sources such as annual company reports, Bureaus of Statistics reports, industry specific magazines, and so on. A problem with this kind of data is the time lag and unknown errors in the data collection process.

# 9.4.3 Analysis of Data and Estimating AP-I 

The analysis for estimating the actual performance AP-I is usually done on a periodic basis using all the data that are available. The main tool for analysis is the plotting of the data. For example, a time series plot of total sales (revenue) is generated and then compared with the desired sales (revenue) defined in phase 1.

Another kind of analysis involves testing the validity of the models used in phase 1. The outcome of this is the updating of parameters of the models used in phase 1 (if the models used in phase 1 are deemed to be adequate) or to build new models (if the models used in phase 1 are deemed to be inadequate) based on the data available. In either case, the main aim of this analysis is to predict the different elements of DP-I for the remainder of the product life cycle. This kind of analysis is more difficult and involves effective combination of the collected data and subjective evaluation. ${ }^{11}$

### 9.4.4 Root Cause Analysis

When the actual performance AP-I does not match the desired performance DP-I there is a problem that the manufacturer needs to fix. As indicated in Figure 9.14, the root cause of the problem can be one or more of the following: (i) product related (technical), (ii) customer related, and (iii) market related.

## Product Related Problems

This arises when the analysis in phase 7 indicates that a major change in the design and/or the production is needed. The manufacturer needs to address this issue in phase 1 from a business perspective. The outcome, based on re-evaluation of the product from an overall business point of view taking into account the technical and commercial issues and the revised product life cycle, can be one of the following:

[^0]
[^0]:    ${ }^{10}$ Many books on marketing deal with customer surveys, e.g., Churchill (1991); Spunt (2003).
    ${ }^{11}$ Data fusion is the use of techniques that combine data from multiple sources and gather that information in order to achieve inferences, which are more efficient than if they were achieved by means of a single source. For more details, see Torra (2003).1. If the design is not the problem and the cost of changes to the production is acceptable (from a business point of view re-evaluation) then proceed to phase 6 and make the changes.
2. If the problem is a design problem and the cost of changes is acceptable (from a business point of view re-evaluation) then proceed to phase 2.
3. If the cost of changes is not acceptable, then go to phase 1.

# Product Recall 

In some cases, a manufacturer might find it necessary to recall either a fraction or all of the items sold, for some rectification action. This can be either voluntary (driven by litigation or future warranty cost considerations) or forced upon the manufacturer by the rulings of regulatory agencies (when the product is deemed to be unsafe). The recall of only a fraction of the total production arises when some batches contain defective critical items that were not detected as part of quality control. A total recall situation arises due to failure modes not known (or recognized during the design phase) that occur to product malfunctioning under certain conditions and are discovered only after the items have been produced and sold. In such cases, the manufacturer can be held responsible for damages caused under the terms of warranty for fitness and the recall is to replace the defective components or newly designed ones to overcome the malfunctioning problem. ${ }^{12}$

## Customer Related Problems

Customer dissatisfaction can arise due to poor performance of the purchased item and/or the quality of post-sale service provided by the manufacturer. In either case, this has a negative impact on overall business performance since dissatisfied customers can (i) switch to a competitor and/or (ii) influence a potential new customer not to buy through negative word-of-mouth publicity.

## Service Recovery

Service recovery is defined as the process by which the manufacturer attempts to rectify a service- or product-related failure. Recoveries are critical because of the reasons mentioned earlier. According to Maxham and Netemeyer (2002), it is important that the response is perceived as just, as this has a significant impact on the satisfaction with the product and service and the firm itself. They define three kinds of justice and the one important in the context of reliability performance is the distributive justice. ${ }^{13}$

[^0]
[^0]:    ${ }^{12}$ Hartman (1987) discusses product quality in the context of the effect of product recall on the business. There are many papers dealing with product recall in the automotive industry, see for example, Rupp and Taylor (2002) and Bates et al. (2007). Healey (2002) reports a case where Ford Motors recalled 8100 Ford Mustang Cobras after owners found the engines did not produce the advertised 320 hp . Ford blamed changes in mufflers and intake manifolds for the problem and installed new ones free on nearly all the Cobras.
    13 The other two types of justice are:Distributive justice focuses on the role of "equity" where individuals assess the fairness of exchange by comparing their inputs to outcomes. It is defined as the extent to which customers feel that they have been treated fairly with respect to the final outcome. The outcomes of distributive justice can be refunds, discounts, and so on, to compensate for product or service failure. Distributive justice has been used in the automobile industry to recover from problems associated with a product failing to perform as claimed. ${ }^{14}$

If the problem can be fixed through service recovery, then we proceed to phase 7 and implement the desired actions.

In some instances, the problem could be due to poor logistics of service delivery. For example, the time for which a failed item is out of action while undergoing repairs is too long. In this case, the manufacturer might decide to use loaners to overcome the problem. ${ }^{15}$ Another important factor is the inability of the product to meet the changed needs and demands of customers. Finally, if none of the above is viable, then we proceed to phase 1.

# Market Related Problems 

The market related elements are sales, market share and revenue. There can be several causes for the actual performance to differ from the desired performance. It could be (i) competitor actions (launching a better product, lowering the sale price), (ii) new safety and environmental regulations, and (iii) general state of the economy (e.g., currency fluctuations, unemployment).

One way that the manufacturer can react to this is through changes to marketing variables (e.g., lowering the price or spending more on promotion and advertising). If this is not viable, then the only option is to go back to phase 1 and start the process again.

- Procedural justice: This refers to perceived fairness of policies and procedures involving the recovery effort. An example of this is where the manufacturer (or service agent) provides a refund, but the customer has to go through the hassle to get the refund.
- Interactional justice: This indicates the extent to which customers feel they have been treated fairly regarding their personal interaction with the service agents throughout the recovery process. This includes honesty, courtesy, interest in fairness perceived by the customer.
${ }^{14}$ Healey (2003) reports a case where the Maxda RX-8 rotary-engine sports car failed to reach the advertised engine power ( 155 hp ) and this caused customer dissatisfaction. Mazda attributed the drop in power (to 142 hp ) to a last minute change in engine tuning to meet emission rules, but had to act quickly to prevent damage to its reputation. It offered to buy back the car (at full sticker price plus taxes and fees) irrespective of the mileage or to provide free scheduled maintenance for the fourth-year, 50,000-mile warranty period, plus $\$ 500$.
${ }^{15}$ Murthy et al. (2004b) discusses various issues challenges related to the logistics for servicing failures under warranty and contains references where readers can get details. Additional relevant references can be found in Chapter 11 of Murthy and Blischke (2006), which deals with customer issues in the context of servicing product warranty.# 9.5 Phases 7 and 8 for Custom-Built Products 

In phase 7, there are several issues that are common for both custom-built and standard products. In contrast, there is very little common in phase 8 . In this section, we briefly discuss these.

### 9.5.1 Phase 7

The data collection is similar for the two cases. In the case of custom-built products, the contract often specifies the kind of data that the customer and the manufacturer need to collect over the warranty period. Often, where the manufacturer also provides the post-sale maintenance service, the contract can include statements regarding the data to be collected and to be exchanged.

If the actual AP-II and DP-II is in close agreement, then no further action is needed. If not, design changes might need to be made to improve the reliability if the contract includes reliability improvement terms (also referred to as reliability improvement warranties). Murthy and Blischke (2006) discuss this and the process involved is shown in Figure 9.15.


Figure 9.15. Engineering change process for RIW (adapted from Murthy and Blischke (2006))# 9.5.2 Phase 8 

In this phase, the manufacturer needs to carry out a review of phases $1-7$ to evaluate the overall process so that improvements can be made for executing new jobs in the future.

### 9.6 Case Study: Cellular Phone

Luiro (2003) discusses various issues relating to the acquisition and analysis of performance data for mobile devices.

Cellular phone manufacturers usually buy the chips from one or more suppliers. In this case, the customer is the cellular phone manufacturer. The chips are installed into the phone and any defective chip detected during the manufacturing and testing is an issue of importance to both the supplier and the customer. Customers rarely return if the level of fallout (defined as failure to meet expectations) is below some specified limit ( 100 parts per million or $0.01 \%$ ) and this varies from customer to customer. Roesch and Brockett (2007) discuss the topic of fallout returns. The returns allow the supplier to compare the in-house reliability results obtained through accelerated testing with the results obtained from an analysis of returned fallout items. These allow the supplier to evaluate their testing procedures (to simulate performance in field) and for continuous improvement.# Product Safety Requirements 

### 10.1 Introduction

Safety is an important attribute of many products. To protect people and the environment, a number of laws, regulations, and standards give requirements to product safety. Some of these requirements are overlapping with reliability requirements that are discussed in previous chapters of this book. A main difference between safety requirements and the requirements that have been discussed so far, is that safety requirements are often mandatory and cannot be traded based on cost-benefit arguments.

Product hazards arise from many different origins. Many product hazards are linked to component failures. Other hazards stem from the design of the product and may cause injuries and health problems even if the product is without any failure. Examples comprise cutting hazards caused by sharp edges, choking hazards caused by small parts that get loose on childrens' toys, and health hazards caused by poisonous paint on toys. Product hazards may lead to incidents ranging from the nuisance category up to disasters.

Some products are installed to protect against major accidents. One such product is the safety instrumented systems (SIS) that we presented as Case 2 in Section 1.7.2. A failure of a SIS will usually not have any significant safety impact on the SIS as such, but may have fatal effects on the system the SIS is protecting, be it a high speed train, a process plant or a nuclear power station.

Product safety requirements are not only stated for the final product, but are related to the whole life cycle of the product, from early conception until disposal. It is often not sufficient to document that the whole life cycle of the product is safe, the manufacturer must also document the activities taken to ensure that the safety is adequate. Detailed risk analyses of the product in the various life cycles are sometimes required, and the risk analysis reports may have to be part of the product documentation.

The safety requirements are strongly dependent on the type and application of the product. To illustrate the nature of the safety requirements and how they are applied,we will use the EU Machinery Directive as a basis for most of the presentation and discussion in this chapter.

The structure of this chapter differs from the other chapters in the book, because of the different nature of the safety requirements. Product safety requirements are mainly given in laws, regulations, and standards, but may also be stated by the customers of specialized products. Sometimes the requirements may also come from consumer organizations or customer interest groups.

The outline of this chapter is as follows: Section 10.2 gives examples of product safety requirements for some applications that illustrate how differently the requirements can be stated. Section 10.3 gives an overview of product safety legislation in Europe with a focus on the EU Machinery Directive, and how safety requirements are organized. Section 10.4 discusses product risk assessment, while Section 10.5 deals with the requirements of the technical construction file. The chapter concludes with a case study on cellular phones in Section 10.5

# 10.2 Safety Requirements 

Safety requirements may be specified in many different ways and may be qualitative and/or quantitative.

### 10.2.1 Examples of Safety Requirements

To illustrate the different types of safety requirements, we give three examples:

1. Example 10.1 gives the safety requirements for a rather simple mechanical product - the wheel hubs of a bicycle. The requirements are from the Federal regulations to the US Consumer product safety act. The requirements are very specific and related to the physical properties of the product and its strength. Verification of the fulfilment of the requirements can usually be done by simple measurements and analyses.
2. Example 10.2 gives two examples of safety requirements for space products. The first requirement is from the ESA Safety manual ECSS-Q-40B and is related to simultaneous failures and human errors. The second requirement is related to flight safety systems and is from ISO 14620-3. To verify fulfilment of the requirements, we have to carry out detailed analyses for the various life phases of the product.
3. Example 10.3 discusses the various types of safety requirements for safety instrumented systems used in the process industry. The types of requirements are specified in the standard IEC 61511 and have to be defined from a risk-based approach. Both the definition and the verification of the fulfilment of the requirements will require a number of detailed qualitative and quantitative risk and reliability analyses.Example 10.1 (Requirements for wheel hubs of bicycles). The following requirements are from $\S 1512.12$ "Requirements for wheel hubs" of the requirements for bicycles in the Federal regulations to the US Consumer product safety act: ${ }^{1}$

All bicycles (other than sidewalk bicycles) shall meet the following requirements:
(a) Locking devices. Wheels shall be secured to the bicycle frame with a positive lock device. Locking devices on threaded axles shall be tightened to the manufacturer's specifications.

- Rear wheels. There shall be no relative motion between the axle and the frame when a force of $1,780 \mathrm{~N}(400 \mathrm{lbf})$ is applied symmetrically to the axle for a period of 30 seconds in the direction of wheel removal.
- Front wheels. Locking devices, except quick-release devices, shall withstand application of a torque in the direction of removal of 17 $\mathrm{N}-\mathrm{m}(12.5 \mathrm{ft}-\mathrm{lb})$.
(b) Quick-release devices. Lever-operated quick-release devices shall be adjustable to allow setting the lever position for tightness. Quick-release levers shall be clearly visible to the rider and shall indicate whether the levers are in a locked or unlocked position. Quick release clamp action shall emboss the frame or fork when locked.
(c) Front hubs. Front hubs not equipped with lever-operated quick-release devices shall have a positive retention feature that shall be tested in accordance with the front hub retention test, $\S 1512.18(\mathrm{j})(3)$, to assure that when the locking devices are released the wheel will not separate from the fork.

The fulfilment of the safety requirements in Example 10.1 may be verified by rather simple measurements and analyses. Safety requirements that are part of the legislation are "static" and cannot be easily changed with the technological development. It is often claimed that this type of requirements is a hindrance to technological development.

The next example, Example 10.2, is an extract from the safety requirements of more complex space systems.

# Example 10.2 (Requirements for space equipment). 

1. This example is from paragraph 5.3.2 of ECSS-Q-40B:

Fault tolerance is one of the basic safety requirements that are used to control hazards. The design of the system shall meet the following failure tolerance requirements:
(a) No single failure or operator error shall have critical (or catastrophic) consequences.
(b) No combination of

[^0]
[^0]:    ${ }^{1}$ For more information and further requirements, see:
    http://www.cpsc.gov/businfo/cpsa.html- two failures, or
- two operator errors, or
- one failure and one operator error
shall have catastrophic consequences.

2. The following requirement for a space flight safety system (FTS) is from paragraph 6.1.1 of ISO 14620-3:

The FTS flight equipment reliability shall be not less than 0.999 at the $95 \%$ confidence level or shall be compliant with the quantitative flight safety requirement, as required in ISO 14620-2 (see Clause 3), if the latter are more stringent. The reliability should be established by analysis of all components and supporting test data. The reliability of FTS ground equipment (including radio-frequency propagation path as far as the launch vehicle) shall be compatible with the reliability requirement of the flight hardware.

The requirements in Example 10.2 are seen to be rather different from the requirements in Example 10.1. To fulfil the first requirement, we have to carry out a detailed failure analysis (e.g., by FMECA, human error analysis, and common cause failure analysis) for all life phases of the product. The second requirement will require a detailed quantitative reliability analysis.

In Example 10.3 we list the types of safety requirements for safety instrumented systems for the process industry. The example does not list the specific safety requirements, but the types of requirements that have to be established.

Example 10.3 (Case 2 - Safety instrumented system). A SIS for the process industry is normally designed and constructed according to IEC 61511, which requires that a safety requirement specification (SRS) is established covering the whole life cycle of the SIS.

The SRS is a document that summarizes the safety requirements for the SIS and forms a basis for the design, construction, implementation, and use of the SIS. Careful development and use of the SRS are believed to minimize subsequent detail design changes that could impact cost and/or schedule.

The SRS consists of both safety functional requirements and safety integrity requirements. The software safety requirements specification shall be derived from the safety requirements specification and the chosen architecture of the SIS.

IEC 61511 requires a risk-based approach. Specific safety requirements must therefore be deduced from risk and reliability analyses for the various phases of the life cycle of the system.

The SRS should include the following types of requirements (reproduced from IEC 61511 with permission from IEC - see page ix):

- Description of all the safety instrumented functions (SIFs) necessary to achieve the required functional safety
- Requirements to identify and take account of common cause failures
- Definition of the safe state of the process for each identified SIF- Definition of any individually safe process states which, when occurring concurrently, create a separate hazard (e.g., overload of emergency storage, multiple relief to flare system)
- The assumed sources of demand and demand rate on the SIF
- Requirement for proof-test intervals
- Response time requirements for the SIS to bring the process to a safe state
- The SIL target and mode of operation (demand/continuous) for each SIF
- Description of SIS process measurements and their trip points
- Description of SIS process output actions and the criteria for successful operation, for example, requirements for tight shut-off valves
- The functional relationship between process inputs and outputs, including logic, mathematical functions and any required permissives
- Requirements for manual shutdown
- Requirements relating to energize or de-energize to trip
- Requirements for resetting the SIS after a shutdown
- Maximum allowable spurious trip rate
- Failure modes and desired response of the SIS
- Any specific procedure requirements for starting up and restarting the SIS
- All interfaces between the SIS and any other system
- Description of the modes of operation of the plant and identification of the safety instrumented functions required to operate within each mode
- The application software safety requirements
- Requirements for overrides/inhibits/bypasses including how they will be cleared
- The specification of any action necessary to achieve or maintain a safe state in the event of fault(s) being detected in the SIS
- The mean time to repair which is feasible for the SIS
- Identification of the dangerous combinations of output states of the SIS that need to be avoided
- The extremes of all environmental conditions that are likely to be encountered by the SIS shall be identified
- Identification of normal and abnormal modes for both the plant as a whole (for example, plant start-up) and individual plant operational procedures (e.g., equipment maintenance, sensor calibration and/or repair). Additional safety instrumented functions may be required to support these modes of operation
- Definition of the requirements for any safety instrumented function necessary to survive a major accident event, for example, time required for a valve to remain operational in the event of a fire.

These requirements are called safety requirements in IEC 61511, but several of them could as well be referred to as reliability requirements.

Detailed risk and reliability analyses need to be carried out, both to establish the safety requirements to a SIS, and to verify that the set requirements are fulfilled. The process is often started by formulating safety acceptance criteria on plant level. These requirements are next allocated to systems and sub-systems down to a levelcalled equipment under control (EUC). A hazard identification (e.g., by a HAZOP ${ }^{2}$ ) is carried out on each EUC to identify process deviations that may lead to a critical incident. Mechanical and instrumented safety systems are installed to prevent, reveal, and mitigate the effects of the identified process deviations, and safety requirements are defined for the safety instrumented systems in the form of safety integrity levels (SIL).

To verify that a specified SIL is fulfiled, we must, among other things, verify that the probability of failure on demand (PFD) of the system is within the range of the specified SIL. For a SIL 3 requirement, we must, for example, verify that the $\mathrm{PFD} \leq 10^{-3}$. The PFD is a function of the system configuration, the failure rates of the components, the coverage of the diagnostic system, the likelihood of common cause failures, the testing interval, and so on. To verify the fulfilment of a safety requirement will therefore require a set of detailed qualitative as well as quantitative reliability and risk analyses.

# 10.2.2 Essential Health and Safety Requirements 

This section presents some essential health and safety requirements (EHSRs) in the EU Machinery Directive. The approach adopted in the Machinery Directive is representative of other product directives in the EU and also for recent legislation in other parts of the world. We will therefore use the Machinery Directive as an example in the rest of this chapter. The Machinery Directive is briefly described in Section 10.3.2.

A high number of EHSRs are listed in Annex I of the Machinery Directive. The EHSRs in Annex I define the results to be attained, or the risks to be dealt with, but do not specify the technical solutions for doing so. The suppliers are free to choose how the requirements are to be met. The EHSRs are therefore seen to be very different from the requirements in Example 10.1.

The EHSRs are written in such a way that they remain valid over time, and do not become obsolete with technical progress. Assessment of whether requirements have been met should be based on the state of technical know-how at a given moment.

This does not mean that essential requirements are vague. They are drafted in such a way as to give sufficient information to enable assessment of whether or not products meet them.

Some of the requirements are specific and straightforward to fulfil, while other requirements are more complex. This is illustrated by the following sample of requirements (The numbers refer to the paragraphs in the Machinery Directive) :
1.2.1 Safety and reliability of control systems: Control systems must be designed and constructed so that they are safe and reliable, in a way that will prevent a dangerous situation arising. Above all they must be designed and constructed in such a way that:

[^0]
[^0]:    ${ }^{2}$ The HAZOP methodology is described in, for example, IEC 61882.- they can withstand the rigours of normal use and external factors
- errors in logic do not lead to dangerous situations
1.2.3 Starting: It must be possible to start machinery only by voluntary actuation of a control provided for the purpose.
The same requirement applies:
- when restarting the machinery after a stoppage, whatever the cause
- when effecting a significant change in the operating conditions (e.g., speed, pressure, etc.),
unless such restarting or change in operating conditions is without risk to exposed persons.
1.3.3 Risks due to falling or ejected objects: Precautions must be taken to prevent risks from falling or ejected objects (e.g., workpieces, tools, cuttings, fragments, waste, etc.)

The requirements are mandatory, legally binding obligations, and they are enforced. It is not always possible to meet all the requirements. In this case, the machinery must, as far as possible, be designed and constructed with the purpose of approaching the requirements.

# 10.3 EU Directives 

An EU Directive is a "law" that is binding for the member states of the EU. A Directive must be transposed into national laws within a specified time interval after the Directive is issued.

### 10.3.1 New Approach Directives

In 1985, a new approach to the development of EU Directives was introduced. The directives that are developed according to this new approach are called New Approach Directives. They present the main requirements to products and systems, while details are left to so-called harmonized standards that are issued by the standardization organizations (e.g., CEN). A high number of Directives and standards give requirements to product safety. A main objective of these directives is to eliminate differences between national laws, and thereby eliminate trade barriers between the EU Member States. The New Approach Directives provide a basis for technical harmonization. The new scheme is embodied in the regulation on CE Marking (see Section 10.3.4), and incorporates conformity assessment procedures directly into the directives.# 10.3.2 The Machinery Directive 

The Machinery Directive was approved in 1989 and was one of the first New Approach Directives. ${ }^{3}$ The Directive has been amended several times. The current version of the Directive was approved in 1998. A new version of the Machinery Directive was approved in 2006, and will enter into force from 29 December 2009.

The Machinery Directive has two main objectives:

- Promote free movement of machinery within the EU "single market"
- Guarantee a high level of protection to EU workers and citizens

The Machinery Directive promotes harmonization through a combination of mandatory EHSRs and harmonized standards. The Directive applies to new machinery products that are intended to be placed (or put into service) on the EU market for the first time.

Machinery is defined in the Directive as:
"an assembly of linked parts or components, at least one of which moves, with the appropriate actuators, control and power circuits, etc., joined together for a specific application, in particular for the processing, treatment, moving or packaging of a material."

The terms "machinery" and "machine" also cover an assembly of machines which, in order to achieve the same end, are arranged and controlled so that they function as an integral whole. This implies that conformance with the EHSRs has to be documented both for single machinery units (e.g., pumps, cranes) and for complex systems comprising several machines.

The Machinery Directive is only concerned with injuries to persons and health effects. Consequences to the environment and material/financial assets are not covered in the Directive.

Guidance on how to fulfil the EHSRs and technical solutions for this end are given in harmonized EN-standards. Approximately 750 such EN-standards have been prepared to support the Machinery Directive. If the product complies with the harmonized standards, it is presumed that the product fulfils the EHSRs. It is, however, voluntary to use the standards, and it is, at least in principle, possible to conform to the EHSRs without following the standards, but this will require a rather comprehensive documentation.

### 10.3.3 The General Product Safety Directive

The general EU Product Safety Directive applies to engineering products that can be directly used by consumers (e.g., consumer electronics, household appliances, garden machinery). While the safe use of these products is covered by a number of specific technical directives (e.g., Machinery Directive), the Product Safety Directive

[^0]
[^0]:    ${ }^{3}$ For further information see:
    http://ec.europa.eu/enterprise/mechan_equipment/machineryplaces additional post-marketing obligations on manufacturers. This directive has also set up a harmonized rapid alert system, called RAPEX, which helps coordinate national market surveillance against unsafe consumer products.

# 10.3.4 CE Marking 

The CE mark in Figure 10.1 is a mandatory safety mark on many products that are placed on the market in the European Economic Area (EEA).

## CE

Figure 10.1. The CE Mark

Officially, CE has no meaning as an abbreviation, but may have originally stood for Communauté Européenne or Conformité Européenne, French for European Conformity.

The CE mark is a sign of conformity with the EHSRs set out in the EU Directives. To permit the use of a CE mark on a product, proof that the item meets the relevant requirements must be documented.

The Machinery Directive splits machinery into two categories: extremely dangerous machines and normal machines. The dangerous machines are listed in Annex IV of the directive. These products are subject to special requirements that involve a Notified Body. A Notified Body is an organization that has been nominated by a member government and notified by the European Commission. The primary role of a Notified Body is to provide services for conformity assessment related to the conditions set out in the directive in support of CE marking. This normally means assessing the manufacturers conformity to the EHSRs. The conformity assessment can be based on inspection, quality assurance, type examination or design examination, or a combination of these.

For normal machines, the conformity assessment may be done by a companyinternal self-certification process.

The responsible organization (manufacturer, representative, importer) has to issue a Declaration of Conformity indicating his identity (e.g., name, location), the list of European Directives he declares compliance with, a list of standards the product complies with, and a legally binding signature on behalf of the organization. The Declaration of Conformity underlines the sole responsibility of the manufacturer.

The CE mark is aptly called the passport to Europe for products. All manufacturers, European, American, Chinese, or other, are required to affix the CE mark to products that are governed by New Approach Directives. There are about 25 Directives requiring CE marking.# 10.3.5 Harmonized Standards 

The harmonization of standards has greatly simplified technical regulation in Europe. Prior to harmonization, each country developed its own standards through a national standards body. This often created technical trade barriers between the European countries.

In the new system, three standards bodies create standards on a Europe-wide level:

- The European Committee for Standardization (CEN)
- The European Committee for Electrotechnical Standardization (CENELEC)
- The European Telecommunications Standards Institute (ETSI)

These three are the only recognized bodies from which a European standard (EN) can emanate. When the development of a European standard begins in one of these organizations, development of any overlapping national standard must stop. European standards, like European laws and European conformity assessment procedures, preempt national standards, and replace them.

Harmonized standards are standards that support European legislation. They (i) have been mandated by the European Commission, (ii) have been developed by one of the European standards bodies listed above, (iii) address essential requirements of New Approach Directives; and (iv) notification of their development has been published in the Official Journal of the European Communities.

Several harmonized EN standards have later been replaced by standards issued by the International Standardization Organization (ISO) and the International Electrotechnical Commission (IEC). These ISO/IEC standards have the same role as harmonized standards.

The standards supporting the Machinery Directive are classified into four categories:
A-standards: These standards cover aspects applicable to all types of machines (e.g., ISO 14121-1 Safety of machinery - Principles of risk assessment, ISO 12100-1 Safety of machinery - Basic concepts, general principles for design)
$B_{1}$-standards: These standards cover particular safety and ergonomic aspects of machinery (e.g., ISO 13854 Safety of machinery - Minimum distances to avoid crushing parts of the human body)
$B_{2}$-standards: These standards cover safety components and devices
(e.g., ISO 13849-1 Safety of machinery - Safety related parts of control systems General principles for design, ISO 13850 Safety of machinery - Emergency stop - Principles for design)

C-standards: These standards cover specific types or groups of machines, for example, cranes, conveyor belts. These standards are all-inclusive, meaning that if we build a machine according to a C -standard, then relevant EHSRs are fulfiled.# 10.4 Risk Assessment 

To prove conformance with the essential health and safety requirements, risk assessments of the new products may have to be carried out. For some specific types of products, where a C -standard is available, it is possible to claim conformance without a risk assessment. If required, the risk assessment must be carried out according to the standard ISO 14121-1. ${ }^{4}$

The main steps of the risk assessment are:

1. Define machine: This step involves describing the machine, its intended use, space and time limits, and boundaries and interfaces for all life cycle phases. The life cycle phases of a machine are, according to ISO 12100-1:

- Construction
- Transport, assembly and installation
- Commissioning
- Use:
- Setting, teaching/programming or process changeover
- Operation
- Cleaning
- Fault finding
- Maintenance
- De-commissioning, dismantling and, as far as safety is concerned, disposal

2. Identify hazards: Here, all hazards and hazardous situations considering the various aspects of the operator-system relationship, the possible states of the machine and reasonably foreseeable misuse must be identified. Hazards can be classified as continuing hazards, which are inherent in the machine, material or substance; and hazardous events that can result from machine failures and human errors. The concept of reasonably foreseeable misuse is important. It is not sufficient that the product/machine is safe during its intended use conditions. It must also be safe for foreseeable misuse conditions. These include situations where operators make shortcuts and use simplified operating procedures, and where other people use the machine for other purposes, for example, children who play with the machine.
The hazard identification may be done as a preliminary hazard analysis, an FMECA or a HAZOP. For more complex systems, it may also be necessary to use methods like fault tree analysis and event tree analysis. The analysis may be supported by the list of generic hazards in Annex A of ISO 14121-1.
3. Analyse consequences: In this step, the consequences or harm related to potential incidents are identified and analysed. These primarily relate to injury and ill health as a result of exposure to a hazard. It can also be described in terms of economic losses due to interruption to production and asset damage or in terms
[^0]
[^0]:    ${ }^{4}$ This standard was originally a harmonized EN-standard called EN 1050 and is tailor-made for the Machinery Directive. Similar standards are available for other types of products, for example ISO 14971 for medical equipment.of environmental damage. The severity of the consequences must be assessed based on some predefined scale.
4. Estimate risk: Risk is generally defined as a function of the the chance (probability) of the harm being realized and the consequences (severity) of this harm. In ISO 14121-1 risk is a function of:

1. The severity of harm
2. The probability of occurrence of that harm, which is a function of:
a) The exposure of person(s) to the hazard
b) The occurrence of a hazardous event
c) The technical and human possibilities to avoid or limit the harm

The elements of risk are illustrated in Figure 10.2.


Figure 10.2. Elements of risk according to the Machinery Directive (reproduced from ISO 14121-1 with permission from Pronorm AS - see page ix)
5. Evaluate the risk: The risk is evaluated based on some predefined criteria. The purpose of this step is to decide if risk is tolerable or should warrant some corrective or preventive measures.
6. Risk control strategy: If risk is judged to be tolerable, a hierarchy of risk reducing options is set out in the Machinery Directive. In selecting the most appropriate methods, the manufacturer must apply the following principles, in the order given:
(a) Eliminate or reduce risks as far as possible (inherently safe design and construction), see also Kivistö-Rahnasto (2000).
(b) Take the necessary protection measures in relation to risks that cannot be eliminated, e.g., see Kjellén (2000).
(c) Inform the users about the residual risks due to any shortcomings of the protection measures adopted, indicate whether any particular training is required and specify any need to provide personal protection equipment.
7. Verification: There will be a need to review the system following modifications to ensure that these measures will reduce risks to a tolerable level and that no new hazards are generated as a result of design changes.The iterative process to achieve safety as outlined in ISO 14121-1 is illustrated in Figure 10.3.


Figure 10.3. The iterative process to achieve safety (reproduced from ISO 14121-1 with permission from Pronorm AS - see page ix)

# 10.5 Technical Construction File 

The technical construction file is the documented supporting evidence of compliance with the EHSRs. The technical construction file must comprise:

- An overall drawing of the machinery together with drawings of the control circuits
- Full detailed drawings, accompanied by any calculation notes, test results, and so on, required to check the conformity of the machinery with the essential safety requirements- A list of:
- the EHSRs
- harmonized standards
- other standards
- other technical specifications
which were used when the machinery was designed:
- A description of methods adopted to eliminate hazards presented by the machinery
- A technical report or certificate obtained from a competent body or laboratory (optional)
- A copy of the instruction for the machinery. The instructions must be available in the language or the languages of the country in which the machine is to be used
- For series manufacture, the internal measures that will be implemented to ensure that the machinery remains in conformity with the provisions of the Directive

Failure to make available the documentation in response to a duly substantiated request by an enforcement authority may constitute sufficient grounds for doubting the presumption of conformity with the requirements of the EHSRs. The documentation need not permanently exist, but it must be possible to assemble it and make it available within a time commensurate with its importance. The documentation shall be retained and kept available for up to ten years from the time of last manufacture of the machinery.

# 10.6 Case Study: Cellular Phone 

Cellular phones, and the use of the phones, impose several types of hazards. We briefly mention some few of these hazards:

Environmental hazards: The cell phone contains compounds (e.g., leaded solders, brominated fire retardants in the plastic, nickel and cadmium in the batteries). If not disposed properly, they can be a source of contamination and can lead to serious consequences. In the USA, there are currently 500 million cellular phones available for recycling and the stockpile will grow by about 150 million each year. Less than $5 \%$ were returned for recycling in 2005. There is a need for a law requiring that cell phone retailers have in-store take-back programmes.
Explosions and fires: The US Consumer Product Safety Commission has received a high number of reports of cellular phones that has exploded or caught fire. In some cases, the owner/user has been severely burned. ${ }^{5}$ Karabagli et al. (2006) present a case study where a cellular phone user suffered second-degree facial and hand burns as a result of a spontaneously exploding mobile phone during a conversation while the phone was still being charged.

[^0]
[^0]:    ${ }^{5}$ Several accident reports are available on http: / /www. consumeraffairs. com.This problem is often attributed to off-brand (imitations) being used instead of the original brand specified by the original equipment manufacturer (OEM). A major Japanese supplier of cellular phone batteries recently had to call back 1.3 million batteries because it was shown that they might overheat and catch fire. ${ }^{6}$
Increased traffic risk: Brulia (2007) has studied the traffic risk of using a cellular phone, and found that operating a cellular phone while driving a vehicle increases the accident risk 400-500 times compared to intoxicated driving. A high number of similar studies have been conducted in several different countries, see, for example, Beck et al. (2007).
Interference with sensitive equipment: Radiation from cellular phones and from base stations are often reported to interfere with sensitive equipment.
Hietanen and Sibakov (2007) report on problems related to disturbance in hospital devices caused by cellular telephone signals. Such interference has the potential for severe consequences.
Health effects: A possible link between the use of cellular phones and brain cancer has recently been fiercely discussed in the media. Several studies have been conducted, but most of these studies have not come up with any clear conclusions. Otto and von Mühlendahl (2007) discuss the risk of brain cancer both from using cellular phones and from radiation from base stations.

[^0]
[^0]:    ${ }^{6}$ See The New York Times, 13 February 2008.# Reliability Management System 

### 11.1 Introduction

Product reliability is very important in the context of new product development. Building in high reliability is costly and time consuming, but the consequence of unreliability is costlier. This implies that manufacturers need to decide on the optimal reliability performance that achieves a proper trade-off between the two and then derive the reliability specification to ensure the desired performance. A reliability management system is a tool that manufacturers can use to manage this process and achieve the desired results. This chapter deals with the structure of the reliability management system and various related issues.

The outline of the chapter is as follows. Section 11.2 examines data, information, and knowledge. A proper understanding of these terms is important for designing an effective reliability management system. In Section 11.3, we highlight the role of data, information, and knowledge in building models for decision making in general. Sections 11.4 to 11.7 deal with this in the context of the different phases of the new product cycle discussed in earlier chapters. Section 11.8 looks at the reliability management system and its relation to other management systems used in most manufacturing businesses and discusses the three key modules of the reliability management system and relevant issues. Section 11.9 suggests how a business can implement the ideas proposed in this book using a reliability management system.

### 11.2 Data, Information, and Knowledge (DIK)

### 11.2.1 Data and Information

Information and data are two terms used either interchangeably, as synonyms or with only slight differences. Data represents a measurable quantity, such as annual sales, strength of material, and so forth. Information is extracted from data throughanalysis and can be viewed as being comprised of a number of data parts and their descriptions. ${ }^{1}$

In a multi-stage decision making process, information derived at one stage can become the data for a subsequent stage. As an example, the market data (monthly sales) collected can be analysed to extract information regarding sales trends. This information is then used to make decisions regarding changes to production, plant upgrade, product development, and so on.

# 11.2.2 Knowledge 

Knowledge is the ability of individuals to understand the information, and the manner in which the information is used in a specific context. ${ }^{2}$ The link between data, information and knowledge can be characterized through the DIKW (data, information, knowledge, and wisdom) hierarchy - a term, attributed to Ackhoff (1989), which has received some attention in the literature. ${ }^{3}$

Knowledge includes theories, models, tools and techniques, standards, and so forth. We briefly discuss each of these.

## Theories

Encyclopaedia Britannica (1996) defines a theory as follows:
"A theory may be characterized as a postulational system (a set of premises) from which empirical laws are deducible as theorems."
1 "Data represents a fact or statement of an event without relation to other things. Information embodies the understanding of the relationships of some sort, possibly cause and effect" (Bellinger et al., 1997). "Data are raw facts that have not been organized or cannot possibly be interpreted. Information is data that are understood. Information comes from the relationship between pieces of data" (Benyon, 1990). ". . . they do not mean the same thing. Information is wider of the two concepts, comprising as it does not only statements of facts but also explanatory discourse or discussion, whereas data is the plural of datum, defined as a thing known or granted" (Holström, 1971).
2 "Knowledge represents a pattern that connects and generally provides a high level of predictability as to what is described and what will happen next." (Bellinger et al., 1997). "Data gets transformed into information through an understanding of the relationships and information yields knowledge through an understanding of the patterns" (Bellinger et al., 1997).
${ }^{3}$ According to Ackhoff (1989) the content of the human mind can be classified into five categories:
(i) Data: symbols
(ii) Information: data that are processed to be useful; provides answers to "who", "what", "where", and "when" questions
(iii) Knowledge: application of data and information; answers "how" questions
(iv) Understanding: appreciation of "why"
(v) Wisdom: evaluated understanding.A scientific theory is defined as:
"A scientific theory is a systematic ideational structure of broad scope, conceived by the imagination of man, that encompasses a family of empirical (experimental) laws regarding regularities in objects and events, both observed and posited - a structure suggested by these laws and devised to explain them in a scientifically rational manner."

# Models 

Any dictionary reveals that the usage of the word "model" is large and varied as it is used both as a noun and as a verb. Even in technical usage, there is no single accepted meaning for the word. ${ }^{4}$ A definition appropriate for our purpose is the following:
"A model is a representation of a real or abstract system"
(Murthy et al., 1990) ${ }^{5}$
The representation can be physical (e.g., scaled model) or abstract (e.g., verbal or schematic representation or symbolic).

A mathematical model is a symbolic representation involving an abstract mathematical formulation. The symbols have a precise mathematical meaning and the manipulation of the symbols is dictated by the rules of logic and mathematics. The formulation is not a model by itself. Only when the symbols are related to the variables characterising the system does it become a mathematical model.

There can be several different mathematical models for a given system depending on the purpose or goal that the model builder has in mind. An adequate model is a model that is adequate for answering the questions that the modeller has in mind.

## Model Building

The two different approaches to building mathematical models are as follows. ${ }^{6}$
Theory based modelling: Here, the modelling is based on the established theories (from physical, biological, and social sciences) relevant to the problem. This kind of model is also called physics based model or white-box model as the underlying mechanisms form the starting point for the model building.
Empirical modelling: Here, the data available forms the basis for the model building and it does not require an understanding of the underlying mechanisms involved. As such, these models are used when there is insufficient understanding to use the earlier approach. This kind of model is also called data dependent model or black-box model.

[^0]
[^0]:    ${ }^{4}$ See Chapter 4 of Murthy et al. (1990) for a more detailed discussion of this.
    ${ }^{5}$ A system is a collection of objects that are related to one another. The system can be real (a physical entity such as a product) or abstract (the design for a new product).
    ${ }^{6}$ There are many books on mathematical modelling. Chapter 18 of Murthy et al. (1990) reviews the books published prior to 1990. Since then, many more books have appeared.In empirical modelling, the type of mathematical formulations needed for modelling is dictated by a preliminary analysis of data available. If the analysis indicates that there is a high degree of variability, then we need to use models that can capture this variability. This requires probabilistic and stochastic models to model a given data set. The data source often provides a clue to the selection of an appropriate model. In the case of failure data, for example, lognormal or Weibull distributions have been used for modelling failures due to fatigue, and exponential distributions for failure of electronic components. In order to use this knowledge, the model builder must be familiar with the theory of failure modelling of different items.

# Tools and Techniques 

A variety of tools are needed for monitoring and collecting data and information, for example, (i) conducting consumer surveys regarding purchase decisions or needs and, (ii) identifying failure modes through accelerated failure testing. Similarly, a variety of techniques are needed for model building and these include the following:

## Parameter Estimation

Once a model is selected, we need to estimate the model parameters. The estimates are obtained using the data available. A variety of techniques have been developed and these can be broadly divided into two categories - graphical and analytical. The accuracy of the estimate depends on the size of the data and the method used. Graphical methods yield crude estimates while analytical methods yield better estimates and confidence limits for the estimates.

## Model Validation

We can always fit a model to a given data set, but the model might not be appropriate or adequate. An inappropriate model, in general, will not yield the desired solution to the problem. Hence, it is necessary to check the validity of the model selected. There are several methods for doing this, and these can be found in many books (e.g. Blischke and Murthy, 2000; Meeker and Escobar, 1998).

## Model Analysis

There are two types of analysis: qualitative and quantitative. The former deals with qualitative aspects of model properties and is derived from the underlying mathematical formulation used in the model. An example of such an analysis is deriving the conditions under which the failure rate associated with a failure distribution is an increasing function. In the latter, we derive an explicit solution to the model underlying formulation and this in turn yields the solution to the problem under consideration. The solution can be either analytical (where the solution is obtained as a function of the model parameters) or computational (where the solution is obtained for a specified set of parameter values).# Standards 

Common use of the word "standard," in a technical sense, implies that it is a universally agreed upon set of guidelines. Standards are produced by many organizations - some for internal use only, others for use by groups of people, groups of companies, or an entire industry. There are many worldwide standards developed and maintained by organizations such as the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC). ${ }^{7}$ Standards can be

1. De facto (not spelled by law): In this case they are followed for convenience.
2. De jure (by law): In this case they are used because of (more or less) legally binding contracts and documents. The need to conform to specified standards can be a prerequisite for doing business on certain markets (e.g., in the EU), or with certain companies.

### 11.2.3 Engineering Knowledge

The knowledge that engineers need is generated in many different ways. Vincenti (1990) suggests that these can be grouped into the following seven categories:

- Transfer from science
- Invention
- Theoretical engineering research
- Experimental engineering research
- Design practice
- Production
- Direct trial and testing

Example 11.1. The failure time at different stress levels is the data that are collected during testing of a prototype. Correlation analysis indicating that the mean failure time decreases as the stress level increases is the process of extracting information from data. Using this information, we can build a model to characterize this relationship (and validated using the failure data) and this generates knowledge. This knowledge can be used to predict the mean time to failure at levels not tested.

### 11.2.4 Role and Importance of DIK

Models play a very important role in finding solutions to all kinds of decision problems. The role of knowledge and data in this process is shown in Figure 11.1. The DIK needed depends on the problem and we look at this issue in the next four sections for the different phases of the product life cycle. It is impossible to give all the DIKs and discuss them in detail. Instead, we restrict ourselves to listing a small sample for each phase.

[^0]
[^0]:    ${ }^{7}$ ISO standards are technical agreements which provide the framework for compatible technology worldwide.

Figure 11.1. DIK in decision problem solution

# 11.3 DIK in Phase 1 

As discussed in Chapter 5, in phase 1, we first define DP-I and then derive SP-I. Figure 11.2 shows the DIK needed in phase 1.


Figure 11.2. DIK in phase 1# 11.3.1 Data and Information 

- Technical knowledge
- Advances in science - new materials, new theories, and so on
- Developments in technology - improvements (minor/major)
- Commercial data
- Customer related data
- Customer requirement reports
- Purchase decisions surveys
- Market related data
- Time history of sales - for current product, for competitor's products, and so on


### 11.3.2 Knowledge

## Theories

- Consumer behaviour
- Marketing
- Technology forecasting


## Models

- Consumer choice models
- Sales models
- Market share models
- Technology forecasting models
- Cost models (life cycle cost, development, marketing, and so on)
- Risk models


## Tools and Techniques

- Design of questionnaires for consumer surveys
- Data mining of databases
- Simulation of models


### 11.4 DIK in Phases 2 and 3

As discussed in Chapter 6, in phases 2 and 3, we derive SP-II and SP-III, respectively, using DP-II obtained from SP-I of phase 1. Figure 11.3 shows the DIK needed in these two phases.

Figure 11.3. DIK in phases 2 and 3

# 11.4.1 Data and Information 

- Technical data
- Engineering specifications and drawings
- Detailed engineering analysis reports
- Design verification and product reliability reports
- Failure mode and effects analysis reports
- Certificate of compliance
- Original drawings from suppliers
- Computer aided design (CAD) files
- Bill of material (for purchasing components)


### 11.4.2 Engineering Knowledge

According to Ullman (2003), design engineers access and use the following three types of knowledge during the design process:
General knowledge: gained through everyday experience and general education
Domain-specific knowledge: gained through study and experience within a specific domain that the designer works in
Procedural knowledge: gained from experience of how to undertake ones tasks within the enterprise concerned.

Vincenti (1990) proposes six knowledge categories that design engineers should posses or at least have access to, and they are as follows:

- Fundamental design concepts
- Criteria and specifications
- Theoretical tools
- Quantitative data- Practical considerations
- Design instrumentalities


# Theories 

- Science of failure: failure mechanisms for different types of materials
- Reliability theory


## Models

- Failure models
- Component level models
- Stress-strength models
- System level models
- Reliability development models
- Prediction of growth models
- Development time models
- Cost models
- Warranty cost models
- Production cost models


## Tools and Techniques

- Fault tree analysis
- Failure mode and effects analysis
- Design process (conform to relevant standards)
- Design verification


### 11.5 DIK in Phases 4 and 5

As discussed in Chapter 7, in phases 4 and 5, we derive PP-III and PP-II, respectively, using SP-III obtained from phase 3. Figure 11.4 shows the DIK needed in these two phases.


Figure 11.4. DIK in phases 4 and 5# 11.5.1 Data and Information 

- Testing reports
- Inspection logs - regulatory and non-regulatory


### 11.5.2 Knowledge

- Design of experiments
- Accelerated testing


## Models

- Accelerated failure time models
- Proportional hazard model


## Tools and Techniques

- Environmental testing
- Design limit testing
- Estimation of reliability
- Hypothesis testing


### 11.6 DIK in Phases 6-8

As discussed in Chapters 8 and 9, in phases 6-8, we derive AP-III - AP-I based on products built using SP-III obtained from phase 3. Figure 11.5 shows the DIK needed in these two phases.


Figure 11.5. DIK in phases 6-8

### 11.6.1 Data and Information

## Phase 6

- Numerical control files
- Test reports
- Process control reports
- Supplier quality assurancePhase 7

- Warranty claims data
- Warranty servicing reports
- Repair and service manuals
- Customer concerns

Phase 8

- Sales data
- Revenue data
- Data relating to competitor's products


# 11.6.2 Knowledge 

Phase 6

- Quality control models
- Acceptance sampling models
- Process control models

Phase 7

- Warranty cost models
- Product usage models
- Warranty reserves models
- Warranty servicing models

Tools and Techniques

- Statistical estimation
- Data mining
- Root cause analysis


### 11.7 Reliability Management System

Manufacturers use a variety of functional management systems to manage their operations and to make decisions. The key ones are the following:

- Design and development management system - for managing both in-house and out-sourced activities
- Production management system - for managing in-house production and component bought from external vendors
- Marketing management system - for managing retailers and indirectly customers
- Post-sale support management system - for managing in-house activities as well as external service agentsA number of management systems (that integrate these functional systems) have been proposed in the literature and/or used in practice. ${ }^{8}$

Although reliability plays an important role in new product development and is affected by decisions made during the design, development, and production phases, and has a significant impact on the outcomes of the marketing and post-sale support phases, there has been very little discussion on reliability management systems in the literature. In most businesses, it is addressed in one or more of the functional management systems listed above but there is no separate reliability management system.

A reliability management system is a tool that manufacturers can use to make decisions and manage product reliability through the different phases of the new product development process. It needs to be closely linked to the other functional management systems as indicated in Figure 11.6. This section deals with this topic and looks at various issues relating to the reliability management system.

# 11.7.1 Structure of the Reliability Management System 

The reliability management system consists of three interconnected modules as shown in Figure 11.7.

### 11.7.2 Data and Information Module

Data are needed for many different purposes as indicated below:

- For evaluation: Product reliability, production efficiency, performance during design
- For prediction: Future costs, spares needed
- For improvements: In design, production, servicing, and so on.
${ }^{8}$ Two such systems are the following:

1. The Product Data Master Model (PDMM): "The objective of PDMM is to capture all essential and interrelated information and product properties including design data, material properties, geometric and topology models, dimension information, finite element analysis and optimization, process planning, scheduling, manufacturing, purchasing and supply management" Zhang et al. (2004). PDMM sub-models include: Supplier model, functional, concept, design model, manufacture model, assembly model, quality, maintenance model, cost model, evaluation, sales model, optimization model, market model, user model, and so on.
2. PROMISE: "PROMISE will develop appropriate technology, including product lifecycle models, product embedded information devices with associated firmware and software components and tools for decision making based on data gathered through a product life cycle" (Kiritsis et al., 2003).

Figure 11.6. Reliability management system

Figure 11.7. Modules of management system

# Data Sources 

Data and information from many different sources are collected (and stored in databases) for decision making during the different phases. They can be broadly categorized into (i) internal and (ii) external. Some of these sources are indicated in Figure 11.8.

A reliability management system must be able to incorporate data and information from these sources. In the early stage of product development, much of the data and information will be subjective (e.g., based on the judgement of experts) or come from historical records of similar systems or components. As the development progresses, better data become available due to design definition, prototype testing, and trial manufacturing runs. Once the product enters the market, new data relating to product performance, sales, and so on, become available.

For each generation of products, many types of data are generated over the product life cycle. These need to be combined with data from external sources to make proper decisions. As such, the reliability management system database needs to contain all in-house data relating to different generations of products.

## Data Collection

Data can be either laboratory data or field data. Laboratory data are often obtained under controlled environment and based on a properly planned experiment. In contrast, field data suffer from variability in the operating environment and other uncontrollable factors.

The form of data can vary. In the case of reliability data, it could be continuous valued (e.g., life of an individual item) or discrete valued (e.g., number of items failing in a specified interval). In the former case, it could represent failure times or censored times (the lives of non-failed items when data collection was stopped) for items.

Finally, when the data needed for modelling are not available, we need to collect data based on a proper experiment or expert judgement in some cases. The experiment, in general, is discipline specific.

Figure 11.8. Reliability management system - data module# Data Retention 

The different reasons for data retention are as follows:

- Product design re-use
- Service parts
- Legal
- Historical

Bsharah and Lees (2000) suggest that the following questions need to be addressed as part of data retention:

- What kinds of data should be retained?
- What is the intended retention period?
- What is the purpose and reason for retaining the data?
- Who are the users of retained data?


## Flow of Data and Information

Effective reliability management requires flow of information between different phases of the product life cycle. Figure 11.9 shows the flow of information from phase 1 to other phases. However, there is both forward and backward flow of data and information.


Figure 11.9. Data and information flow between the different phases# Database Management 

A database must be maintained and managed to be of value to users. A database management system (DBMS) provides the procedures and mechanisms for maintaining and managing a database. Three main functions of a DBMS are file maintenance, database administration, and information retrieval.

File maintenance involves adding records to tables, updating data in tables, and deleting records from tables. The users of the database are responsible for maintaining the quality of the data that are in the database. In the context of the reliability management system, file maintenance is carried out by operational users at each of the phases of the product life cycle. Engineers would input the results of prototype tests into the reliability management system, financial personnel would input weekly or monthly cost data, service personnel would enter data relating to failure modes, repair activities, and so on.

Database administration involves the creation, deletion, and restrictions on the use of tables. During development of the database, tables are created for storing data. As the design of the database evolves, some tables may become obsolete and require deletion, while additional tables may be required in order to support additional features. It is important that only certain personnel have the ability to make such changes, so that the downstream effects are managed. The database administrator may be a dedicated position or it may be a part-time role of an operational "supervisor", depending on the size of the organization.

## Data Warehousing

A data warehouse is a centralized repository of useful data. It is designed for strategic decision support because it allows the past to be researched and relevant trends to be identified. It is largely built up from data extracted from operational databases. The structure should be:

- Time dependent
- Non-volatile
- Subject oriented
- Integrated

Each record in the database has a date associated with it so that historical trends can be ascertained.

The database must be a static, historical "snapshot" of the operational data. Before data enters the data warehouse from operational databases, the data needs to be "cleaned" so that it is ready for queries.

Only data that are relevant to the decision support purpose should be extracted from operational databases for use in the warehouse. A data warehouse will, by definition, be large, so extraneous data should be avoided. Data for day-to-day use should be accessed through the operational databases.

The data entering the data warehouse must be consistent and integrated from all appropriate sectors of the organization. A single entity may be referred to by different names across the many operational databases, but since the purpose of the warehouse is to facilitate analysis, there must be only one name for each entity.# Problems with Failure Data Collection 

There are several problems associated with failure data collection. These include the following:

1. Data and information are not recorded
2. Data are missing
3. Delay in reporting
4. Pooled or aggregated data (e.g., total sales in different time periods rather than individual sale date)
5. Grouped data: failures over different intervals
6. Censored data - different types of censoring
7. Incorrect reporting (failure causes, times)

### 11.7.3 Reliability Databases

The term reliability database ${ }^{9}$ has two different meanings. The first is an actual computer database that is set up for storing component data (event, engineering, and operating data) for equipment or plants. The second use of the term is in referring to what are also called generic databases or data handbooks. These usually contain the results of analyses performed on the event data that are found within the computer databases or, in some cases, based simply on expert opinion. The result that is usually reported in the handbooks is the failure rate for a specific component class (e.g., a pump). Note here that a component can be anything from a small electronic component to a large compressor.

There are three types of reliability computer databases and the type of data contained in each are quite different. They are as follows:

- Component event databases
- Abnormal or incident-report databases
- Generic component reliability databases

Component event databases are compilations of events (e.g., failure, maintenance undertaken) for use in determining reliability, availability, and maintainability parameters. An incident report database stores information on incidents or accidents, their probability, causes, and effects. A generic component reliability database is essentially a compilation of failure rates for various components.

### 11.7.4 Knowledge Module

The knowledge module consists of many sub-modules dealing with topics such as (i) theories, (ii) procedures (general and specific), (iii) tools and techniques, (iv) engineering standards (company, industry, national/regional/international), (v) models, and so on. The knowledge can be either "public knowledge" or "proprietary (private) knowledge."

[^0]
[^0]:    ${ }^{9}$ The material on databases is taken mainly from Chapter 18 of Blischke and Murthy (2000). For more on reliability databases, see Amendola and Keller (1987); Cannon and Bendell (1991); Akhmedjanov (2001).# Knowledge Discovery in Databases 

Databases contain data which can be converted into information and finally to knowledge. According to Adriaans and Zantinge (1997):
"Knowledge discovery in database is the nontrivial extraction of implicit, previously unknown and potentially useful knowledge from data."

It involves several stages: (i) data selection, (ii) cleaning, (iii) enrichment, (iv) coding, (v) data mining, and (iv) reporting.

## Data Mining

Data mining is a key element of knowledge discovery in databases. It deals with the discovery of hidden knowledge, unexpected patterns, and new rules from large databases. ${ }^{10}$

## Models for Data Mining

Complex data mining projects may require the coordinate efforts of various experts, stakeholders, or departments throughout an entire organization. In the data mining literature, various frameworks (often referred to as models) have been proposed to serve as blueprints for how to organize the process of gathering data, analysing data, disseminating results, implementing results, and monitoring improvements. ${ }^{11}$

## Integration of Knowledge

Integration of knowledge is critical for the success of new product development and in ensuring the desired reliability performance in products produced. Court (1998) deals with issues relating to integration of knowledge in new product development and identifies the following factors as being of importance.

- Medium of presentation
- Manner of presentation
- Location
- Administration
- Punctuality
- Precision and credibility
- Uncertainty
- Protection
${ }^{10}$ There are numerous books that review the theory and practice of data mining and the following is an illustrative sample: Edelstein (1999); Fayyad et al. (1996); Han and Kamber (2000); Hastie et al. (2001); Westphal and Blaxton (1998).
${ }^{11}$ One such framework (or model) called SEMMA and proposed by the SAS Institute uses the following sequence: sample-explore-modify-model-assess.# Models 

Many different kinds of models are needed to assist in the decision making in the different phases of the product life cycle. ${ }^{12}$ This element of the reliability management system is a library of the different models that have been developed either internally or externally. The operational user should be able to select models from within each category and have the parameter values estimated from data sets stored in the system. Conservative default values (and probability profiles) should be offered if data sets are not available (or judgement values solicited).

Often, several models need to be linked to find a solution to a specific decision problem. Also, the reliability management system must have the flexibility that allows for upgrading of models and the addition of new models to the system.

A large number of statistical packages are available for various tasks of model building (e.g., model selection, parameter estimation, model validation). Similarly, a large number of software packages are available for model analysis and optimization.

## Engineering Standards

There are many different reliability related standards. ${ }^{13}$ One group of standards that is widely used, is the IEC standards.

## Tools and Techniques

Data Reduction: The term data reduction in the context of data mining is usually applied to projects where the goal is to aggregate or amalgamate the information contained in large datasets into manageable (smaller) information nuggets. Data reduction methods can include simple tabulation, aggregation (computing descriptive statistics) or more sophisticated techniques like clustering, principal component analysis, and so on.
Data Mining: Data mining uses a variety of techniques and these include: (i) query tools, (ii) statistical techniques, (iii) visualization, (iv) on-line analytical processing, (v) case-based learning ( $k$-nearest neighbours), (vi) decision trees, (vii) association rules, (viii) neural networks, and (ix) genetic algorithms.
Algorithms: An algorithm is a method consisting of well-defined instructions for completing a task starting from a given initial state, proceeding through a welldefined series of successive states, and eventually terminating in an end-state. The transition from one state to the next can be either deterministic or probabilistic (incorporating randomness). An algorithm for processing information involves reading data from an input source or device, writing to an output device, and/or storing for further processing. Stored data are regarded as part of the internal state of the entity performing the algorithm. In practice, the state is stored in a data structure, but an algorithm requires the internal data only for executing specific operations. ${ }^{14}$

[^0]
[^0]:    ${ }^{12}$ Many models can be found in books on reliability, see for example, Blischke and Murthy (2000); Murthy et al. (2008).
    ${ }^{13}$ Chapter 20 of Blischke and Murthy (2000) discusses several different standards.
    14 There are many books dealing with algorithms (e.g., Knuth, 1997; Stone, 1972).# Software for Reliability Analysis 

Software for reliability analysis can be grouped into three categories:

- General statistical software that contain packages for reliability analysis
- Software for general reliability analysis
- Software for specific reliability analysis

Most general statistical packages include programs for descriptive statistics, tables, exploratory data analysis, probability calculations for a wide range of distributions, various plotting routines, regression analysis, ANOVA, ANCOVA, and MANOVA.

### 11.7.5 Interface Module

The reliability management system must allow the user to input requirements (e.g., targets, objectives, models) and view the output results. Operational users will require the ability to access relevant information based on their inputs. Strategic users (the managerial decision makers) will need to retrieve information linking multiple modules so that trade-off decisions can be made. This implies the need for a proper interface module.

Two interface requirements are that the reliability management system should have a user interface and an application interface. The user interface facilitates the flow of information from the user to the reliability management system and back, while the application interface provides the link between a variety of external programs and databases that may be called upon to analyse or upload data to and or download data from the reliability management system.

## User Interface

The problem or objective is first specified, and then data and models from the reliability management system are used to provide information and assistance to solve the problem or to achieve the desired objective.

The reliability management system should present a variety of model options (and state the assumptions underlying each model). If an appropriate model is not available, the reliability management system should guide the user through a model-building process whereby data are imported from the appropriate source (e.g., database or expert opinion), analysed, and parameters estimated. The input values (decision variables or other data) should be clearly displayed as well as the output values and confidence bounds.

Once the component models have been selected, they need to be linked so as to assist in the solving of the problem. This linking is facilitated using a graphical representation, such as a flowchart, whereby icons for different models could be dragged-and-dropped. The output from one model would become the input for the next. Selecting an element of the flow chart would then open it up for more detailed configuration, with the option of viewing underlying data or model assumptions.

The user should be able to specify the form of the outputs. These could be viewed for each of the component models (to ensure they are performing as expected, or tofocus on certain problem areas) or at the objective function (macro) level. Graphs illustrating distributions of variables and the limits on parameters should be available.

It is important for the interface to be easy to learn and easy to use, allowing the operator to define the problem and the elements that are expected to have an impact on the system being studied. In other words, time should be spent solving the problem, not navigating the tool. Two common options are a menu system or a graphical user interface. A combination of the two could be used to make the most of the two types.

# Application Interface 

The interface between external applications and the reliability management system should have the ability to extract data from the reliability management system so that more sophisticated analyses can be performed. It should also have the ability to return data from the external software in such a way that the results are linked to the original data and can be easily referenced if using a model based on that data.

### 11.8 Implementation Aspects

How should a business proceed with the implementation of the process for product reliability suggested in this book? We answer this question in this section through a multi-step process.

Step 1: Create a reliability management department headed by a senior level manager with the title "Reliability manager."
Step 2: Appoint the core members of the reliability management department. They must all have a good understanding of all the different aspects of reliability and expertise in specific aspects. This implies that the members have different background (engineers, scientists, statisticians, information technologists, and so forth).
Step 3: Set up a reliability management system that links effectively with the different existing management systems.

### 11.8.1 Reliability Manager

The Reliability manager is responsible for

- Setting up the reliability management system and ensuring that it is continuously updated.
- Liaise with other functional managers and the CEO in the decision making in phase 1 of the product life cycle.
- Coordinate cross functional groups in later phases involving members of the reliability management department so that reliability issues are addressed properly in these phases and the process outlined in this book is followed.# 11.8.2 Reliability Management Department 

The members of the reliability management department are responsible for

- Interacting with members of different functional groups to deal with product reliability in phases $2-8$.
- Collect relevant reliability data, carry out proper analysis, and give feedback to different departments for continuous improvements.# Symbols 

| $A$ | Limiting availability |
| :-- | :-- |
| $A(t)$ | Availability at time $t$ |
| $A(0, t)$ | Average availability over the time interval $(0, t)$ |
| $B(t)$ | Virtual age at time $t$ (Section 4.5) |
| $C_{D}$ | Development cost |
| $C_{j}$ | Constraint (Section 3.6) |
| $C_{k}$ | Purchase price for component $k$ (Section 6.7) |
| $C_{P}$ | Production cost |
| $C_{r}$ | Average cost of a repair (under warranty) |
| $C_{W}$ | Total expected warranty cost over the product life cycle |
| $C_{W}$ | Expected warranty cost per unit sold |
| $\mathrm{DP}_{j}$ | Desired performance at level $j$ (Section 3.6) |
| $E(X)$ | Expected (mean) value of the random variable $X$ |
| $\epsilon$ | Random error (Chapter 4) |
| $F(t)$ | Probability distribution function, $F(t)=\operatorname{Pr}(T \leq t)$. Also |
|  | called the failure distribution function. |
| $F(t \mid x)$ | Conditional failure distribution of an item that has survived up |
|  | to time $t, F(t \mid x)=\operatorname{Pr}(T \leq t+x \mid T>x)$ |
| $F_{j}$ | Function at level $j$ (Section 3.6) |
| $F_{n}(t)$ | Empirical (failure) distribution function (Section 7.5) |
| $f(t)$ | Probability density function, $f(t)=F^{\prime}(t)$ |
| $g(u)$ | Probability density for usage rate $\left(u_{1} \leq u \leq u_{2}\right)$ |
| $J(x, y)$ | Objective function for phase 2 |
| $J\left(\gamma_{k}, M_{k}, T_{k}, \tau_{k}\right)$ | Objective function for phase 3 |
| $J$ | Number of levels [Section 6.6] |
| $J(x, y)$ | Objective function (Section 6.4.2) |
| $J\left(x_{1}, y_{1}, x_{2}, y_{2}\right)$ | Objective function (Section 6.4.2) |
| $L$ | Product life cycle |
| $L(\theta)$ | Likelihood function |
| $\lambda(t)$ | Rate of occurrence of failures (ROCOF) |
| $\Lambda(t)$ | Cumulative ROCOF, $\Lambda(t)=\int_{0}^{t} \lambda(u) d u$ || $\lambda_{0}(t ; x, y)$ | ROCOF (product used at the nominal design usage rate $x$ ) |
| :--: | :--: |
| $\lambda(t ; x, y, u)$ | ROCOF (product used with usage rate $u$ ) |
| M | Number of replicated components in a redundant system (Chapter 6) |
| $M_{k}$ | Number of replicates (redundancy) |
| $N(t)$ | Number of failures in the time interval $(0, t]$ (Section 4.6) |
| $N(t)$ | Number of first purchase sales up to time $t$ |
| $n(t)$ | Sales rate, $n(t)=N^{\prime}(t)$ |
| $P$ | Sale price (of a product) (Chapter 5) |
| $P_{d}$ | Probability of a customer being dissatisfied with the product |
| $\pi_{\mathrm{D}}(\tau)$ | Development cost with development time $\tau$ (Section 6.7) |
| $\operatorname{Pr}(A)$ | Probability of the event $A$ |
| $\phi(\mathbf{X}(t))$ | Structure function (system state) at time $t$ (Chapter 4) |
| $\psi(s)$ | A function of the stress level $s$ (Section 4.4) |
| $\psi(T)$ | Remaining time (at time $T$ ) of the warranty period (Chapter 5) |
| $\underset{\mathcal{Q}}{\mathcal{Q}}$ | Total sales over the product life cycle |
| $R(t)$ | Total potential customer population |
| $R(t)$ | Survivor function, $R(t)=\operatorname{Pr}(T>t)=1-F(t)$ |
| $R(t ; s)$ | Survivor function at stress level $s$ |
| $\hat{R}$ | Revenue generated over life cycle |
| $s$ | Stress level (Chapter 4) |
| $\mathrm{SP}_{j}$ | Specification at level $j$ (Section 3.6) |
| $S(t)$ | Number of lost customers by time $t$ (Chapter 5) |
| $s(t)$ | Customer loss rate at time $t$ such that $s(t)=S^{\prime}(t)$ (Chapter 5) |
| $T$ | Time to failure. Also called life-length or age at failure. |
| $T$ | Time between preventive maintenance actions (Chapter 6) |
| $\tau$ | Interval between consecutive proof tests (test interval) (Section 4.6) |
| $\tau$ | Development time (Section 6.7) |
| $\tau_{k}$ | Development time |
| $T_{k}$ | Replacement interval (preventive maintenance) |
| $u$ | Usage rate (Chapter 6) |
| $u_{1}$ | Usage rate lower limit (Chapter 6) |
| $u_{2}$ | Usage rate upper limit (Chapter 6) |
| $x$ | Reliability design decision variable (nominal usage rate) |
| $X_{i}(t)$ | State variable of item $i$ at time $t$ (Chapter 4) |
| $y$ | Reliability design decision variable (scale parameter) |
| W | Warranty period |
| $z(t)$ | Failure rate function, $z(t)=f(t) / R(t)$ |
| $z(t ; s)$ | Failure rate function at stress level $s$ (Section 4.4) |
| $Z(t)$ | Cumulative failure rate function, $Z(t)=\int_{0}^{t} z(u) d u$ |

The same symbol is sometimes used to represent different variables, but should not cause any confusion when used in the proper context.# Acronyms 

| ADSL | Asymmetric digital subscriber line |
| :-- | :-- |
| AF | Acceleration factor |
| AHP | Analytical hierarchy process |
| ANOVA | Analysis of variance |
| AP | Actual performance |
| BGA | Ball grid array |
| BI | Burn-in |
| BIR | Built-in reliability |
| BIT | Built-in test |
| CAD | Computer-aided design |
| CDF | Cumulative distribution function |
| CE | Communauté Européenne |
| CEN | European Committee for Standardization |
| CENELEC | European Committee for Electrotechnical Standardization |
| CEO | Chief Executive Officer |
| CM | Corrective maintenance |
| CMS | Complementary MOS |
| CPU | Central processing unit |
| CSP | Chip size package |
| CUSUM | Cumulative sum (of differences) |
| DBMS | Database management system |
| DIK | Data, information, and knowledge |
| DIKW | Data, information, knowledge, and wisdom |
| DLBI | Die level burn-in |
| DNV | Det Norske Veritas |
| DOE | Design of experiments |
| DP | Desired performance |
| DS | Design option (solution) |
| EEA | European Economic Area |
| EHSR | Essential health and safety requirement |
| EN | European norm || EOS | Electrical over-stress |
| :-- | :-- |
| ESA | European Space Agency |
| ESD | Electro-static discharge |
| ESS | Environmental stress screening |
| ETSI | European Telecommunications Standards Institute |
| EU | European Union |
| EUC | Equipment under control |
| FA | Failure analysis |
| FCOB | Flip chip on board |
| FMA | Failure mode analysis |
| FMEA | Failure modes and effects analysis |
| FMECA | Failure modes, effects, and criticality analysis |
| FRACAS | Failure reporting analysis and corrective action system |
| FRW | Free replacement warranty |
| FTA | Fault tree analysis |
| FTF | Fail-to-function |
| FTS | Flight safety system |
| HAZOP | Hazard and operability analysis |
| HSE | Health, safety, and environment |
| IC | Integrated circuit |
| IEC | International Electrotechnical Commission |
| ISDN | Integrated Services Digital Network |
| ISO | International Organization for Standardization |
| LCD | Liquid crystal display |
| LCC | Life cycle cost |
| LED | Light emitting diode |
| LSI | Large scale integration |
| MCDM | Multi-criteria decision making |
| MLE | Maximum likelihood estimate |
| MOS | Metal-oxide semiconductor |
| MRL | Mean residual life |
| MSI | Medium scale integration |
| MTBF | Mean time between failures |
| MTTF | Mean time to failure |
| MTTR | Mean time to repair |
| NPD | New product development |
| NTNU | Norwegian University of Science and Technology |
| OED | Organic emissive display |
| OEM | Original equipment manufacturer |
| OLED | Organic light emitting diode |
| PDMM | Product data master model |
| PDS | Product design specification |
| PFD | Probability of failure on demand |
| PLBI | Package level burn-in |
| PP | Predicted performance |
|  |  || PM | Preventive maintenance |
| :-- | :-- |
| PRW | Pro-rata rebate warranty |
| QFD | Quality function deployment |
| RAM | Random-access memory |
| RAPEX | Rapid exchange of information system |
| RBD | Reliability block diagram |
| RIW | Reliability improvement warranty |
| ROCOF | Rate of occurrence of failures |
| ROI | Return of investment |
| RP | Recommended practice |
| SEMMA | Sample-explore-modify-model-assess |
| SIF | Safety instrumented function |
| SIL | Safety integrity level |
| SIS | Safety instrumented system |
| SLIC | Stress induced leakage current |
| SLSI | Super large scale integration |
| SMT | Surface mount technology |
| SP | Specification |
| SRS | Safety requirement specification |
| SSI | Small scale integration |
| TAAF | Test, analyse, and fix |
| TAFT | Test, analyse, fix, test |
| TDDB | Time-dependent dielectric breakdown |
| TOP | Top event (in a fault tree) |
| TOPSIS | Technique for order preference by similarity to ideal solution |
| TTT | Total time on test |
| ULSI | Ultra large scale integration |
| U.S. | United States (of America) |
| WAF | Wafer acceptance test |
| WLBI | Wafer level burn-in |
| WL-CSP | Wafer level chip size package |
| WP | Wafer probe |# Glossary 

Many of the definitions in this book are according to international standards - especially IEC and ISO standards. Permissions to reproduce these definitions have kindly been given by IEC and ISO (see page ix).

Acceptance test: A test conducted under specified conditions by or on behalf of the customer, using delivered or deliverable items, to determine whether or not the item satisfies specified requirements. Includes acceptance of first production units (MIL-HDBK-338B).
Active redundancy: That redundancy wherein all means for performing a required function are intended to operate simultaneously (IEC 60050-191)
Allocation: The assignment of reliability performance requirements to sub-systems and components within a system that will result in meeting the overall reliability performance requirement for the system if each of these performance requirements is attained.
Black box: Representation of an item whereby its internal composition is not essential to understand its function, and only its interface characteristics are considered (ECSS-Q-30-02A)
Built-in test (BIT): A test approach using self-test hardware and software to test all or part of an equipment item or system. BIT denotes any self-test feature incorporated into the design for the purpose of detecting, diagnosing and isolating failures (NASA-STD-8729.1).
Cold redundancy: Term used to indicate a standby redundancy where the redundant means is not powered, and thus to allow the differentiation of failure rates (on or off) (ECSS-Q-30-02A)
Corrective maintenance: All actions performed as a result of failure, to restore an item to a specified condition. Corrective maintenance can include any or all of the following steps: Localization, Isolation, Disassembly, Interchange, Reassembly, Alignment and Checkout (MIL-HDBK-338B).Dependability: The collective term used to describe the availability performance and its influencing factors: reliability performance, maintainability performance and maintenance support performance (IEC 60050-191).
Dependability management: Coordinated activities to direct and control an organization with regard to dependability (IEC 60300-1)
Design review: Planned, documented independent review of an existing or proposed design (IEC 61160)
Diagnostics: Tools, procedures or software coding used to either identify and troubleshoot system faults or to verify the integrity of a system.
Fail safe: Design property of an item which prevents its failures from resulting in critical faults (ECSS-Q-40B).
Failure: The termination of the ability of an item to perform a required function (IEC 60050-191).
Failure mechanism: The physical, chemical or other processes that may lead to a failure (IEC 60050-191).
Failure mode: The effect by which a failure is observed on a failed item.
Fault: An abnormal condition that may cause a reduction in, or loss of, the capability of a functional unit to perform a required function (IEC 61511).
State of an item characterized by its inability to perform a required function, excluding the inability during preventive maintenance or other planned actions, or due to lack of external resources (IEC 60050-191).
Fault tolerance: The ability of a functional unit to continue to perform a required function in the presence of faults or errors (IEC 61511).
Fault tree analysis: A method for relating a process of system failure to equipment, component or material failure modes using fault trees. A fault tree is a model that graphically and logically represents the various combinations of possible events, faults and normal, occurring in a process or system that leads to the TOP event. Process or system elements may include hardware, software and human and environmental factors.
Harm: Physical injury or damage to health (ISO 12100-1).
Hazard: Existing or potential condition of an item that can result in a mishap (ECSS-Q-40B).
Hazardous event: Occurrence leading to undesired consequences and arising from the triggering by one (or more) initiator events of one (or more) hazards (ECSS-Q-40B).
Hot redundancy: Term used to indicate a standby redundancy where the redundant means is powered (ECSS-Q-30-02A).
Life cycle cost: The total cost of acquisition, operation, maintenance and support of an item throughout its useful life, and including the cost of disposal (NASA-STD-8729.1).
Machinery: Assembly of linked parts or components, at least one of which moves, with the appropriate machine actuators, control and power circuits, joined together for a specific application, in particular for the processing, treatment, moving or packaging of a material (ISO 12100-1).Maintainability: The ability of an item, under stated conditions of use, to be retained in, or restored to, a state in which it can perform its required functions, when maintenance is performed under stated conditions and using prescribed procedures and resources.
Maintenance: The combination of all technical and corresponding administrative actions, including supervision actions, intended to retain an entity in, or restore it to, a state in which it can perform its required functions (IEC 60050-191).
New product development: A disciplined and defined set of tasks and steps that describe the normal means by which a company repetitively converts embryonic ideas into saleable products or services (Belliveau et al., 2002).
Performance: The extent to which the provided functions can be executed under defined operational and environmental conditions (IEC 62347).
Preventive maintenance: All actions performed to retain an item in specified condition by providing systematic inspection, detection, and prevention of incipient failures (MIL-HDBK-338B).
Qualification test: A test conducted under specified conditions, by or on behalf of the customer, using items representative of the production configuration, in order to determine compliance with item design requirements as a basis for production approval (also known as a Demonstration test) (MIL-HDBK-338B).
Reasonably foreseeable misuse: Use of a machine in a way not intended by the designer, but which may result from readily predictable human behaviour (ISO 12100-1).
Redundancy: The existence of more than one means for accomplishing a given function. Each means of accomplishing the function need not necessarily be identical (MIL-HDBK-338B).
Reliability: The ability of a product to perform a required function, under given environmental and operational conditions and for a stated period of time.
Reliability (of a machine): The ability of a machine or its components or equipment, to perform a required function under specified conditions and for a given period of time without failing (ISO 12100-1).
Reliability growth: The improvement in reliability that results when design, material, or part deficiencies are revealed by testing and eliminated or mitigated through corrective action (MIL-HDBK-338B).
Requirement: A condition or capability that must be met or possessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed documents (IEEE Std. 1413.1).
Risk: A combination of the likelihood of an undesirable event occurring and the severity of the consequences of the occurrence (NASA-STD-8729.1).
A combination of the probability of occurrence of harm and the severity of that harm.
Single-point failure: A failure of an item that causes the system to fail and for which no redundancy or alternative operational procedure exists (MIL-HDBK-338B).
Specification (of a object): A set of statements about an object derived during the pre-development stage to achieve some desired performance.Standby redundancy: That redundancy wherein a part of the means for performing a required function is intended to operate, while the remaining part(s) of the means are inoperative until needed (IEC 60050-191).
Systematic failure: Failure related in a deterministic way to a certain cause, which can only be eliminated by a modification of the design or of the manufacturing process, operational procedures, documentation or other relevant factors (IEC 60050-191).
Tangible product: A product can be tangible (e.g., assemblies or produced materials) or intangible (e.g., knowledge or concepts), or a combination thereof. A product can be either intended (e.g., offering to customers) or unintended (e.g., pollutant or unwanted effects).
Test, analyse, and fix (TAAF): A synonym for reliability growth in which the three main elements (test, analyse deficiencies, and take corrective action) for achieving reliability growth are identified (MIL-HDBK-338B).
Validation: Confirmation, through the provision of objective evidence, that the requirements for a specified intended use or application have been fulfilled (ISO 9000).
Verification: Confirmation, through the provision of objective evidence, that specified requirements have been fulfilled (ISO 9000).# References 

Ackhoff, R. L. (1989). From data to wisdom. Journal of Applied Systems Analysis, 16:3-9.
Adriaans, R. L. and Zantinge, D. (1997). Data Mining. Addison Wesley Longman, Harlow, England.
Akao, Y. (1997). QFD; past, present, and future. In Proceedings of the International Symposium on QFD'97, Linköping, Sweden.
Akhmedjanov, F. M. (2001). Reliability databases: State-of-the-art and perspectives. Report R-1235, Risö National Laboratory, Roskilde, Denmark.
Amendola, A. and Keller, A. Z. (1987). Reliability Data Bases. Kluwer Academic Publishers, Amsterdam.
Amerasekera, A. and Campbell, D. S. (1987). Failure Mechanisms in Semiconductor Devices. Wiley, New York.
Amstadter, B. L. (1971). Reliability Mathematics. McGraw-Hill, New York.
Andreasen, M. and Hein, L. (1987). Integrated Product Development. Springer, London.
Ansell, J. I. and Phillips, M. J. (1989). Practical problems in the statistical analysis of reliability data. Applied Statistics, 38:205-247.
Ansell, J. I. and Phillips, M. J. (1994). Practical Methods for Reliability Data Analysis. Oxford University Press, Oxford.
Aoussat, A., Christofol, H., and Le Coq, M. (2000). New product design - a transverse approach. Journal of Engineering Design, 11(4):399-417.
Appel, F. C. (1970). The 747 ushers in a new era. The American Way, pages 25-29.
Archer, N. P. and Wesolowsky, G. O. (1996). Consumer response to service and product quality: A study of motor vehicle owners. Journal of Operations Management, 14:103118 .
Asiedu, Y. and Gu, P. (1998). Product life cycle cost analysis: state of the art review. International Journal of Production Research, 36:883-908.
Atkinson, P. and Hammersley, M. (1994). Ethnography and participant observation. In Denzin, N. K. and Lincoln, Y. S., editors, The Handbook of Qualitative Research. Sage Publications.

Atkinson, S. (2005). Fuel cells for mobile devices. Membrane Technology, December:6-8.
Atterwalla, A. I. and Stierman, R. (1994). Failure mode analysis of a 540 pin plasic ball grid array. In Proceedings SMI, pages 252-257.
Balachandra, R. (1984). Critical signals for making go/no go decisions in new product development. Journal of Product Innovation Management, 2:92-104.Barclay, I. (1992). The new product development process: Part 1 - past evidence and future practical application. $R \& D$ Management, 22:255-263.
Bashir, H. A. and Thomson, V. (2001). An analogy-based model for estimating design effort. Design Studies, 22:157-167.
Bass, F. M. (1969). A new product growth model for consumer durables. Management Science, 15:215-227.
Bates, H., Holweg, M., Lewis, M., and Oliver, N. (2007). Motor vehicle recalls: Trends, patterns and emerging issues. Omega, 35:202-210.
Beck, K. H., Yan, F., and Wang, M. Q. (2007). Cell phone users, reported crash risk, unsafe driving behaviors and dispositions: A survey of motorists in maryland. Journal of Safety Research, 38(6):683-688.
Bellinger, G., Castro, D., and Mills, A. (1997). Data, information, knowledge, and wisdom. Technical report, http://www.outsight.com/systems/dikw/dikw.htm.
Belliveau, P., Griffin, A., and Sommermeyer, S. (2002). The PDMA Toolbook 2 for New Product Development. Wiley, New York.
Benyon, D. (1990). Information and Data Modelling. Alfred Waller, Henley-on-Thames.
Betz, F. (1993). Strategic Technology Management. McGraw-Hill, New York.
Bhat, N. U. (1972). Elements of Applied Stochastic Processes. Wiley, New York.
Blache, K. M. and Shrivastava, A. B. (1994). Defining failure of manufacturing machinery and equipment. In Proceedings Annual Reliability and Maintainability Symposium, pages $69-75$.
Blanchard, B. S. (2004). System Engineering Management. Wiley, New Jersey, 3rd edition.
Blanchard, B. S. and Fabrycky, W. J. (1998). Systems Engineering and Analysis. PrenticeHall, New Jersey, 3rd edition.
Blischke, W. R. and Murthy, D. N. P. (1994). Warranty Cost Analysis. Marcel Dekker, New York.
Blischke, W. R. and Murthy, D. N. P. (1996). Product Warranty Handbook. Marcel Dekker, New York.
Blischke, W. R. and Murthy, D. N. P. (2000). Reliability: Modelling, Prediction and Optimization. Wiley, New York.
Boothroyd, W., Dewhurst, P., and Knight, W. (2002). Product Design for Manufacture and Assembly. Marcel Dekker, New York, 2nd edition.
Box, G. E. P., Hunter, J. S., and Hunter, W. G. (2005). Statistics for Experimenters: Design, Innovation, and Discovery. Wiley, New York, 2nd edition.
Brentani, U. (1986). Do firms need a custom-designed new screening model? Journal of Product Innovation, 3:108-119.
Brostow, W. and Cornelissen, R. D. (1985). Mechanical Failures of Plastics. Carl Hanser Verlag, Munchen.
Brulia, J. (2007). The cell phone: A potential "digital danger". Journal of Explosives Engineering, 24(4):22-23.
BS 5760-4 (1986). Reliability of constructed or manufactured products, systems, equipment and components, Part 4. British Standards Institution.
Bsharah, F. and Lees, M. (2000). Requirements and strategies for the retention of automotive product data. Computer Aided Design, 32:145-158.
Bulmer, M. and Eccleston, J. E. (2003). Photocopier reliability modeling using evolutionary algorithms. In Blischke, W. R. and Murthy, D. N. P., editors, Case Studies in Reliability and Maintenance, chapter 18. Wiley, New York.Büyüközkan, G., Dereli, T., and Baykasoglu, A. (2004). A survey on the methods and tools of concurrent new product development and agile manufacturing. Journal of Intelligent Manufacturing, 15:731-751.
Calantone, R. J., Di Benedetto, A. A., and Schmidt, J. B. (1999). Using the analytical hierarchy process in new product screening. Journal of Product Innovation Management, 16:65-76.
Cannon, A. C. and Bendell, A., editors (1991). Reliability Data Banks. Elsevier, London.
Cavasin, D., Brice-Hearnes, K., and Arab, A. (2003). Improvements in reliability and manufacturability of an integrated power amplifier module system - in package, via implementation of conductive epoxy adhesive for selected SMT components. In Proceedings of the 2003 Electronic Component and Technology Conference, pages 1404-1407.
Chakravarty, A. K. and Balakrishnan, N. (2001). Achieving product variety through optimal choice of module variations. IIE Transactions, 33:587-598.
Chen, J., Yao, D., and Zheng, S. H. (1998). Quality control for products supplied with warranty. Operations Research, 46:107-115.
Churchill, G. A. J. (1991). Marketing Research: Methodological Foundations. The Dryden Press, Orlando, FL, 5th edition.
Clark, K. B. . and Fujimoto, T. (1991). Product Development Performance. Harvard Business School Press, Boston.
Coit, D. W. and Dey, K. A. (1999). Analysis of grouped data from field-failure reporting systems. Reliability Engineering and System Safety, 65:95-101.
Colangelo, V. J. and Heiser, F. A. (1987). Analysis of Metallurgical Failures. Wiley, New York, 2nd. edition.
Condra, L. (1993). Reliability Improvement with Design of Experiments. Marcel Dekker, New York.
Coolen, F. P. A. and Yan, K. J. (2003). Non-parametric predictive inference from grouped lifetime data. Reliability Engineering and System Safety, 80:243-252.
Cooper, L. P. (2003). A new research agenda to reduce risk in new product development through knowledge management: A practitioner perspective. Journal of Engineering and Technology Management, 20:117-140.
Cooper, R., Wootoon, A. B., and Bruce, M. (1998). Requirement capture: Theory and practice. Technovation, 18:497-531.
Cooper, R. G. (2001). Winning at New Products. Perseus, Cambridge MA, 3rd edition.
Cooper, R. G. (2005). New products - what separates the winners from the losers and what drives success. In Kahn, K. B., editor, PDMA Handbook of New Product Development, chapter 1, pages 3-28. Wiley, New Jersey, 2nd edition.
Cox, D. R. (1972). Regression models and life tables (with discussion). Journal of the Royal Statistical Society B, 34:187-220.
Cox, D. R. and Reid, N. (2000). The Theory of the Design of Experiments. Chapman \& Hall, Boca Raton.
Cross, N. (1994). Engineering Design Methods: Strategies for Product Design. Wiley, Chichester, 2nd edition.
Crow, L. H. (1974). Reliability analysis of complex repairable systems. In Proschan, F. and Serfling, R. J., editors, Reliability and Biometry, pages 379-410. SIAM.
Crowder, M. J., Kimber, A. C., Smith, R. L., and Sweeting, T. J. (1991). Statistical Analysis of Reliability Data. Chapman and Hall, London.
Cunningham, S. P., Spanos, C. J., and Voros, K. (1995). Semiconductor yield improvement results: Results and best practices. IEEE Transactions on Semiconductor Manufacturing, 8:103-109.Darveaux, R., Heckman, J., Syed, A., and Mawer, A. (2000). Solder joint fatigue life with fine pitch BGAs - impact of design and material selection. Microelectronics Reliability, 40:1117-1127.
Day, G. S., Shocker, A. D., and Shrivastava, R. K. (1978). Consumer oriented approaches to identifying product markets. Journal of Marketing, 43:9-19.
Dehnad, K. (1989). Quality Control, Robust Design and the Taguchi Method. Wadsworth \& Brooks/Cole, Pacific Grove, California.
Deszca, G., Munro, H., and Noori, H. (1999). Developing breakthrough products: challenges and options for market assessment. Journal of Operations Management, 17:613-630.
Dhillon, B. S. (1983). Reliability Engineering in Systems Design and Operation. Van Nostrand Reinhold Company, Inc., New York.
Dhudshia, V. (1992). Guidelines for Equipment Reliability. Number 92031014A-GEN. SEMATECH.
Dieter, G. E. (1991). Engineering Design - A Materials and Processing Approach. McGrawHill, New York.
Djamaludin, I., Murthy, D. N. P., and Wilson, R. J. (1994). Quality control through lot sizing for items sold with warranty. International Journal of Production Economics, 33:97-107.
Djamaludin, I., Murthy, D. N. P., and Wilson, R. J. (1995). Lot-sizing and testing for items with uncertain quality. Mathematical and Computer Modelling, 22:35-44.
Djamaludin, I., Wilson, R. J., and Murthy, D. N. P. (1997). An optimal quality control scheme for product sold with warranty. In Al-Sultan, K. S. and Rahim, M. A., editors, Optimization in Quality Control, chapter 13. Kluwer Academic Publishers, New York.
DNV RP A203 (2001). Qualification Procedures for New Technology. Det Norske Veritas (DNV).
DOE-NE-STD-1004-92 (1992). Root Cause Analysis Guidance Document. U.S. Department of Energy, Office of Nuclear Energy, Washington, DC.
Doyen, L. and Gaudoin, O. (2004). Classes of imperfect repair modelsbased on reduction of failure intensity or virtual age. Reliability Engineering and System Safety, 84:45-56.
Drejer, A. and Gudmundsson, A. (2002). Towards multiple product development. Technovation, 22:733-745.
Duane, J. T. (1964). Learning curve approach to reliability monitoring. IEEE Transactions on Aerospace, 2:563-566.
Ebeling, C. E. (1997). An Introduction to Reliability and Maintainability Engineering. McGraw-Hill, New York.
ECSS-Q-30-02A (2001). Space product assurance; Failure modes, effects and criticality analysis (FMECA). ESA-ESTEC, Requirements an Standards Division, Noordwijk, The Netherlands.
ECSS-Q-40B (2002). Space product assurance; Safety. ESA-ESTEC, Requirements and Standards Division, Noordwijk, The Netherlands.
Edelstein, H. A. (1999). Introduction to Data Mining and Knowledge Discovery. Two Crows Corporation, Potomac, MD, 3rd edition.
Erens, F. J. and Hegge, H. M. H. (1994). Manufacturing and sales coordination for product variety. International Journal of Production Economics, 37:83-99.
Escobar, L. A. and Meeker, W. Q. (1999). Statistical prediction based on censored life data. Technometrics, 41:113-124.
Evanoff, T. (2002). Today's cars are built to last. USA Today, December 12.
Evans, J. R. and Lindsay, W. M. (1996). The Management and Control of Quality. West Publishing Company, St. Paul, Minnesota.Fabrycky, W. J. and Blanchard, B. S. (1991). Life-cycle cost and economic analysis. Prentice Hall, Englewood Cliffs, New Jersey.
Fairlie-Clarke, T. and Muller, M. (2003). An activity model of the product development process. Journal of Engineering Design, 14(3):247-272.
Fayyad, U. M., Piatetsky-Shapiro, G., Smyth, P., and Uthurusamy, R. (1996). Advances in Knowledge Discovery \& Data Mining. MIT Press, Cambridge, MA.
Ferris-Prabhu, A. V. (1992). Introduction to Semiconductor Device Yield Modeling. Artech House, Boston, MA.
Flanagan, J. C. (1954). The critical incident technique. Psychological Bulletin, 54:327-358.
Flint, D. J. (2002). Compressing new product success-to-success cycle time. Deep customer value understanding and idea generation. Industrial Marketing Management, 31:305-315.
Foucher, B., Boullie, J., Meslet, B., and Das, D. (2002). A review of reliability prediction methods for electronic devices. Microelectronics Reliability, 42:1155-1162.
Fox, J. (1993). Quality Through Design; The Key to Successful Product Delivery. McGrawHill, London.
Fredette, M. and Lawless, J. F. (2007). Finite-horizon prediction of recurrent events, with applications to forecasts of warranty claims. Technometrics, 49:66-80.
French, M. (1985). Conceptual Design for Engineers. The Design Council, London.
Fries, A. and Sun, A. (1996). A survey of discrete reliability-growth models. IEEE Transactions on Reliability, 45:582-604.
Fujita, K. (2002). Product variety optimization under modular architecture. Computer Aided Design, 34:953-965.
Gandara, A. and Rich, M. D. (1977). Reliability improvement warranties for military procurement. Report R-2264-AF, RAND Corp, Santa Monica, CA.
Garcia, R. and Calantone, R. (2002). A critical look at technological innovation typology and innovativeness terminology: A literature review. Journal of Product Innovation Management, 19:110-132.
Geng, P. (2005). Dynamic test and modelling methodology for BGA solder joint shock evaluation. In Proceedings of the 2005 Electronic Component and Technology Conference, pages $654-659$.
Gershenson, J. K., Prasad, G. J., and Zhang, Y. (2003). Product modularity: definitions and benefits. Journal of Engineering Design, 14(3):295-313.
Gershenson, J. K., Prasad, G. J., and Zhang, Y. (2004). Product modularity: measures and design methods. Journal of Engineering Design, 15(1):33-51.
Gershenson, J. K. and Stauffer, L. A. (1999). A taxonomy for design requirements from coporate customers. Research in Engineering Design, 11:103-115.
Gill, A. N. and Mehta, G. P. (1994). A class of subset selection procedures for Weibull populations. IEEE Transactions on Reliability, 43:65-70.
Gitomer, J. (1998). Customer Satisfaction is Worthless: Customer Loyalty is Priceless. Bard Press, Austin, TX.
Grant, E. L. and Leavensworth, R. S. (1988). Statistical Quality Control. McGraw-Hill, New York.
Gregory, W. M. (1964). Air force studies product life warranty. Aviation Week and Space Technology, 2 November.
Guida, M. and Pulcini, G. (2002). Automotive reliability inference based on past data and technical knowledge. Reliability Engineering and System Safety, 76:129-137.
Gupta, S. S. and Miescke, K. L. (1987). Optimum two-stage selection procedures for Weibull populations. Journal of Statistical Planning and Inference, 15:147-156.
Hales, C. (1993). Managing Engineering Design. Longman Scientific \& Technical, Essex.Han, J. and Kamber, M. (2000). Data Mining: Concepts and Techniques. Morgan-Kaufman, New York.
Hartman, R. S. (1987). Product quality and efficiency: The effect of product recalls on resale prices and firm valuation. The Review of Economics and Statistics, 69:367-372.
Hashim, F. M. (1993). Using functional descriptions to assist the redesign process. PhD thesis, Department of Mechanical Engineering, University of Leeds.
Hastie, T., Tibshirari, R., and Friedman, J. H. (2001). The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Springer, New York.
Hauser, J. R. and Clausing, D. (1988). The house of quality. Harvard Business Review, 66:63-73.
Healey, J. R. (2002). No title. USA Today, September 20.
Healey, J. R. (2003). No title. USA Today, September 03.
Healy, J. D., Jain, A. K., and Bennet, J. M. (1997). Reliability prediction; tutorial notes. Annual Reliability and Maintainability Symposium.
Herard, L. (1999). Packaging reliability. Microelectronics Engineering, 49:17-26.
Hietanen, M. and Sibakov, V. (2007). Electromagnetic interference from GSM and TETRA phones with life-support medical devices. Annali dell'Istituto Superiore di Sanita, 43(3):204-207.
Hiller, G. E. (1973). Warranty and product support. the plan and use thereof in a commercial operation. In Proc. Failure Free Warranty Seminar, Philadelphia. US Navy Aviation Supply Office.
Hipp, J. and Lindner, G. (1999). Analysing warranty claims of automobiles. In Proceedings of the 5th International Computer Science Conference (ICSC'99), Hong Kong.
Hiraoka, K. and Niaido, T. (1997). Reliability design of current stress in LSI interconnects using the estimation of failure rate due to electromigration. Microelectronics Reliability, 37:1185-1191.
Hisada, K. and Arizino, F. (2002). Reliability tests for Weibull distribution with varying shapeparameter based on complete data. IEEE Transactions on Reliability, 51(3):331-336.
Hnatek, E. R. (1995). Integrated Circuit Quality and Reliability. Marcel Dekker, New York.
Hobbs, G. (2000). Accelerated Reliability Engineering: HALT and HASS. Wiley, Chichester.
Hodges, D. A., Jackson, H. G., and Saleh, R. (2003). Analysis and Design of Digital Integrated Circuits. McGraw-Hill, New York.
Holström, J. E. (1971). Personal filing and indexing of design data. In Proc. Information Systems for Designers, University of Southampton.
Homburg, C. and Rudolph, B. (2001). Customer satisfaction in industrial markets: dimensional and multiple role issues. Journal of Business Research, 52:15-33.
Hopkins, D. S. and Bailey, E. L. (1971). New product pressures. Conference Board Records B., pages $16-24$.

Hsu, T. A. (1982). On some optimal selection procedures for Weibull populations. Communications in Statistics - Series A: Theory and Methods, 11:2657-2668.
Hu, X. J. and Lawless, J. F. (1996). Estimation from truncated lifetime data with supplementary information on covariates and censoring times. Biometrika, 83:747-761.
Hu, X. J., Lawless, J. F., and Suzuki, K. (1998). Nonparametric estimation of lifetime distribution when censoring times are missing. Technometrics, 40:3-13.
Hubka, V. and Eder, W. E. (1992). Engineering Design. Heurista, Zurich.
Huei, Y. K. (1999). Sampling plans for vehicle component reliability verification. Quality and Reliability Engineering International, 15:363-368.Hung, S. C., Zheng, P. J., Chen, H. N., Lee, S. C., and Lee, J. J. (2000). Board level reliability and chip scale packages. International Journal of Microcircuit Electronic Packaging, 23:118-129.
Hung, S. C., Zheng, P. J., Ho, S. H., Lee, S. C., Chen, H. N., and Wu, J. D. (2001). Board level reliability of PBGA using flex substrate. Microelectronics Reliability, 41:677-687.
IEC 60050-191 (1990). International Electrotechnical Vocabulary - Chapter 191 - Dependability and Quality of Service. International Electrotechnical Commission, Geneva.
IEC 60300-1 (2003). Dependability Management; Part 1: Dependability Assurance of Products. International Electrotechnical Commission, Geneva, 2nd edition.
IEC 60300-3-3 (2005). Dependability Management; Part 3: Application Guide - Section 3: Life Cycle Costing. International Electrotechnical Commission, Geneva.
IEC 60300-3-4 (2007). Dependability Management; Part 3: Application Guide - Section 4: Guide to the Specification of Dependability Requirements. International Electrotechnical Commission, Geneva, 2nd. edition.
IEC 61014 (2003). Programmes for Reliability Growth. International Electrotechnical Commission, Geneva.
IEC 61025 (1990). Fault Tree Analysis (FTA). International Electrotechnical Commission, Geneva.
IEC 61160 (2005). Design Review. International Electrotechnical Commission, Geneva.
IEC 61164 (2004). Reliability Growth - Statistical Test and Estimation Methods. International Electrotechnical Commission, Geneva.
IEC 61508 (1997). Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems. International Electrotechnical Commission, Geneva.
IEC 61511 (2003). Functional Safety - Safety Instrumented Systems for the Process Industry. International Electrotechnical Commission, Geneva.
IEC 61882 (2001). Hazard and Operability Studies (HAZOP Studies) - Application Guide. International Electrotechnical Commission, Geneva.
IEC 62347 (2006). Guidance on System Dependability Specifications. International Electrotechnical Commission, Geneva.
IEEE Std. 1413.1 (2002). IEEE Guide for Selecting and Using Reliability Predictions Based on IEEE 1413. IEEE, New York.
IEEE Std. 352 (1982). IEEE Guide for General Principles of Reliability Analysis of Nuclear Power Generating Station Protection Systems. IEEE, New York.
Isiklar, G. and Buyukozkan, G. (2007). Using a multi-criteria decision approach to evauate mobile phone alternatives. Computer Standards \& Interface, 29:265-274.
Iskander, B. P. and Blischke, W. R. (2003). Reliability and warranty analysis of a motorcycle based on claims data. In Blischke, W. R. and Murthy, D. N. P., editors, Case Studies in Reliability and Maintenance. Wiley, New York.
ISO 12100-1 (2003). Safety of Machinery - Basic Concepts, General Principles for Design - Part 1: Basic Terminology, Methodology. International Standardization Organization, Geneva.
ISO 13849-1 (2006). Safety of Machinery - Safety-Related Parts of Control Systems - Part 1: General Principles for Design. International Standardization Organization, Geneva.
ISO 13850 (2006). Safety of Machinery - Emergency Stop - Principles for Design. International Standardization Organization, Geneva.
ISO 13854 (1996). Safety of Machinery - Minimum Gaps to Avoid Crushing of Parts of the Human Body. International Standardization Organization, Geneva.
ISO 14121-1 (2007). Safety of Machinery - Risk Assessment (Principles). International Standardization Organization, Geneva.ISO 14620-2 (2000). Space Systems - Safety Requirements, Part 2: Launch Site Operations. International Standardization Organization, Geneva.
ISO 14620-3 (2005). Space Systems - Safety Requirements, Part 3: Flight Safety Systems. International Standardization Organization, Geneva.
ISO 14971 (2000). Medical Devices - Application of Risk Management to Medical Devices. International Standardization Organization, Geneva.
ISO 8402 (1986). Quality Vocabulary. International Standardization Organization, Geneva.
ISO 9000 (2000). Quality Management and Assurance Standards. International Standardization Organization, Geneva.
Jang, S. Y., Hong, S. M., Park, M. Y., Kwak, D. O., Jeong, J. W., Roh, S. H., and Moon, Y. J. (2004). FCOB (flip chip on board) reliability study for mobile applications. In Proceedings of the 2004 Electronic Component and Technology Conference, pages 62-67.
Jauw, J. and Vassilou, P. (2000). Field data is reliability information: Implementing an automated data acquisition and analysis system. In Proceedings Annual Reliability and Maintainability Symposium, pages 86-92.
Jensen, F. and Peterson, N. E. (1982). Burn-in. Wiley, New York.
Jha, A. K. and Kaner, C. J. D. (2003). Bugs in the brave new unwired world. http://www. testingeducation.org.
Kahn, K. B. (2002). An exploratory investigation of new product forecasting practices. Journal of Product Innovation Management, 19:133-143.
Kalbfleisch, J. D. and Lawless, J. F. (1992). Some statistical methods for truncated data. Journal of Quality Technology, 24:145-152.
Kalbfleisch, J. D., Lawless, J. F., and Robinson, J. A. (1991). Methods for the analysis and prediction of warranty claims. Technometrics, 33:273-285.
Kar, T. R. and Nachlas, J. A. (1997). Coordinated warranty and burn-in strategies. IEEE Transactions on Reliability, 46:512-518.
Karabagli, Y., Kose, A. A., and Cetin, C. (2006). Partial thickness burns caused by a spontaneously exploding mobile phone. Burns, 32(7):922-924.
Karim, M. R. and Suzuki, K. (2005). Analysis of warranty claim data: a literature review. International Journal of Quality \& Reliability Management, 22:667-686.
Karim, M. R., Yamamoto, W., and Suzuki, K. (2001a). Change-point detection from marginal count failure data. Journal of the Japanese Society for Quality Control, 31:104-124.
Karim, M. R., Yamamoto, W., and Suzuki, K. (2001b). Performance of AIC constrained MLE in detecting a change-point. Bulletin of the University of Electro-Communication, 13:173180 .
Karim, M. R., Yamamoto, W., and Suzuki, K. (2001c). Statistical analysis of marginal count failure data. Lifetime Data Analysis, 7:173-186.
Kawauchi, Y. and Rausand, M. (1999). Life cycle cost (LCC) analysis in oil and chemical process industries. Technical Report ISBN 82-7706-128-5, Department of Quality and Production Engineering, Norwegian University of Science and Technology, NO7491 Trondheim.
Kececioglu, D. (1991). Reliability Engineering Handbook, volume 1. Prentice-Hall, Englewood Cliffs, New Jersey.
Kececioglu, D. and Sun, F. (1995). Environmental Stress Screening: Its Quantification, Optimization, and Management. Prentice-Hall, Englewood Cliffs, New Jersey.
Keser, B., Wetz, L., and White, J. (2004). WL-CSP reliability with various solder alloys and die thicknesses. Microelectronics Reliability, 44:521-531.
Khurana, A. and Rosenthal, S. R. (1998). Towards holistic "front ends" in new product development. Journal of Product Innovation Management, 15:57-74.Kimmel, J., Hautanen, J., and Levola, T. (2002). Display technologies for portable communication devices. Proceedings of IEEE, 94:581-590.
Kingston, J. N. and Patel, J. K. (1980a). A restricted subset selection procedure for Weibull populations. Communications in Statistics - Series A: Theory and Methods, A9:1371-1383.
Kingston, J. N. and Patel, J. K. (1980b). Selecting the best one of several Weibull populations. Communications in Statistics - Series A: Theory and Methods, A9:383-398.
Kiritsis, D., Bufardi, A., and Xirouchakis, P. (2003). Research issues on product lifecycle management and information tracking using smart embedded systems. Advanced Engineering Informatics, 17:189-202.
Kivistö-Rahnasto, J. (2000). Machine safety design; An approach fulfilling European safety requirements. Number 411. VTT Publications, Espoo, Finland.
Kjellén, U. (2000). Prevention of Accidents Through Experience Feedback. Taylor \& Francis, London.
Klause, P. J. (1979). Failure-free warranty idea lauded, wider use desired. Aviation Week and Space Technology, 9 February.
Kleef, E., Trip, H. C. M., and Luning, P. (2005). Consumer research in the early stages of new product development: a critical review of methods and techniques. Food Quality and Preference, 16:181-201.
Knuth, D. (1997). Fundamental Algorithms. Addison-Wesley, Reading, MA, 3rd edition.
Kohoutek, H. J. (1996). Reliability specification and goal setting. In Ireson, W. G., Coombs, C. F., and Moss, R. Y., editors, Handbook of Reliability Engineering and Management. McGraw-Hill, New York.
Krishnan, V. and Ulrich, K. T. (2001). Product development decisions: a review of the literature. Management Science, 47:1-21.
Kumar, D. and Klefsjø, B. (1994). Proportional hazards models: A review. Reliability Engineering and System Safety, 44:177-188.
Kumar, S. and McCaffrey, T. R. (2003). Engineering economics at a hard disk drive manufacturer. Technovation, 23:749-755.
Kuo, W. and Kim, T. (1999). An overview of manufacturing yield and reliability modelling for semiconductor products. Proceedings of IEEE, 87:1329-1344.
Kwon, Y. I. (1996). A Bayesian life test sampling plan for products with Weibull lifetime distribution sold under warranty. Reliability Engineering and System Safety, 53:61-66.
Landers, T. L. and Kolarik, W. J. (1987). Proportional hazards analysis of field warranty data. Reliability Engineering, 18:131-139.
Larsen, M. R., Harvey, I. R., Turner, D., Porter, B., and Ortowski, J. (2004). Mechanical bending technique for determining CSP design and assembly weaknesses. In IPC Printed Circuits Expo, SNEMA Coincil APEX, Designer Summit.
Lau, J. H. and Pao, Y. (1997). Solder Joint Reliability of BGA, CSP, Flip chip and Fine pitch SMT Assemblies. McGraw-Hill, New York.
Lawless, J. F. (1982). Statistical Models and Methods for Lifetime Data. Wiley, New York.
Lawless, J. F. (1998). Statistical analysis of of product warranty data. International Statistical Review, 66:41-60.
Lawless, J. F., Hu, J., and Cao, J. (1995). Methods for estimation of failure distributions and rates from automobile warranty data. Lifetime Data Analysis, 1:227-240.
Lawless, J. F. and Kalbfleisch, J. D. (1992). Some issues in the collection and analysis of field reliability data. In Klein, J. P. and Goel, P. K., editors, Survival Analysis: State of the Art, pages 141-152. Kluwer Academic Publishers, Amsterdam.
Layer, A., Brinke, E. T., Van-Houden, F., and Haasis, S. (2002). Recent and future trends in cost estimation. International Journal of Computer Integrated Manufacturing, 56:499-510.Lee, K. J. and Lo, G. (2004). Use-condition based cyclic bend test development for handheld components. In Proceedings of the 2004 Electronic Component and Technology Conference, pages 1279-1287.
Levitt, T. (1980). Marketing success through differentiation of anything. Harvard Business Review, pages 83-91.
Lieblein, J. and Zelen, M. (1956). Statistical investigation of the fatigue life of deep groove ball bearings. Journal of Research, National Bureau of Standards, 57:273-316.
Limnios, N. and Oprisan, G. (2001). Semi-Markov Processes and Reliability. Birkhauser, Basel.
Lin, L. and Chen, L. C. (2002). Constraints modelling in product design. Journal of Engineering Design, 13(3):205-214.
Lloyd, D. K. (1986). Forecasting reliability growth. Quality and Reliability Engineering International, 2:19-23.
Lloyd, D. K. and Lipow, M. (1962). Reliability; Management, Methods and Mathematics. Prentice Hall, Englewood Cliffs, New Jersey.
Lu, M. W. (1998). Automotive reliability prediction based on early field failure warranty data. Quality and Reliability Engineering International, 14:103-108.
Luiro, V. (2003). Acquisition and Analysis of Performance Data for Mobile Devices. PhD thesis, University of Oulo, Finland.
Lyons, K. and Murthy, D. N. P. (1996). Warranty data analysis: A case study. In Proceedings of the Second Australia-Japan Workshop on Stochastic Models in Engineering, Technology and Management, pages 396-405, Brisbane, Australia. University of Queensland.
Machinery Directive (1998). Directive 98/37/EC of 22 June 1998 on the approximation of the laws of the Member States relating to machinery. Official Journal of the European Communities, Bruxelles, Belgium.
Maffin, D. (1998). Engineering design models: Context, theory and practice. Journal of Engineering Design, 9(4):315-327.
Mahajan, V. and Wind, Y. (1992). New product models: Practice, shortcomings, and desired improvements. Journal of Product Innovation Management, 9:128-139.
Majeske, K. D. (2003). A mixture model for automobile warranty data. Reliability Engineering and System Safety, 81:71-77.
Majeske, K. D. and Herrin, G. D. (1995). Assessing mixture model goodness-of-fit with an application to automobile warranty data. In Proceedings Annual Reliability and Maintainability Symposium, pages 378-383.
Majeske, K. D., Lynch, T. C., and Herrin, G. D. (1997). Evaluating product and process design changes with warranty data. International Journal of Production Economics, 50:79-89.
Martin, P. L. (1999). Electronic Failure Analysis Handbook; Techniques and Applications for Electronic and Electrical Packages, Components, and Assemblies. McGraw-Hill, New York.
Martino, J. P. (1992). Technology Forecasting for Decision Making. McGraw-Hill, New York.
Martz, H. and Waller, R. A. (1982). Bayesian Reliability Analysis. Wiley, New York.
Mathewson, A., O’Sullivan, P., Concannom, A., Foley, S., Minehane, S., Duane, R., and Palser, K. (1999). Modelling and simulation of reliability for design. Microelectronics Engineering, 49:95-117.
Maxham, J. G. I. and Netemeyer, R. G. (2002). Modeling customer perceptions of complaint handling over time: The effect of perceived justice on satisfaction and intent. Journal of Retailing, 78:239-252.
Mead, C. and Conway, L. (1980). Introduction to VLSI Systems. Addison-Wesley, Reading, MA.Meeker, W. Q. and Escobar, L. A. (1993). A review of recent research and current issues in accelerated testing. International Statistical Review, 41:147-168.
Meeker, W. Q. and Escobar, L. A. (1998). Statistical Methods for Reliability Data. Wiley, New York.
Meeker, W. Q. and Hamada, M. (1995). Statistical tools for the rapid development and evaluation of high-reliability products. IEEE Transactions on Reliability, 44:187-198.
Meerkamm, H. (1990). Fertigungsrecht Konstruiren mit CAD Systemen. Konstruktion, 42.
Meyer, M. H. and Lehnerd, A. H. (1992). The Power of Product Platform. The Free Press, New York.
Meyer, M. H., Tertzakian, P., and Utterback, J. M. (1997). Metrics for managing reearch and development in the context of the product family. Sloan management Review, 43(1):88111 .
Mi, J. (1997). Warranty policies and burn-in. Naval Research Logistics Quarterly, 44:199209.

Mikkola, J. H. and Gassmann, O. (2003). Managing modularity of product architectures: Toward an integrated theory. IEEE Transactions on Engineering Management, 50(2):204218.

MIL-HDBK-217F (1991). Reliability Prediction of Electronic Equipment. US Department of Defense, Washington, DC.
MIL-HDBK-338B (1998). Military Handbook: Electronic Reliability Design Handbook. US Department of Defense, Washington, DC.
MIL-HDBK-344A (1993). Environmental Stress Screening (ESS) of Electronic Equipment. US Department of Defense, Washington, DC.
MIL-STD-2155 (1985). Failure Reporting, Analysis and Corrective Action System. US Department of Defense, Washington, DC.
Miles, L. (1972). Techniques in Value Analysis and Engineering. McGraw-Hill, New York.
Minehane, S., Duane, R., O'Sullivan, P., McCarthy, K. G., and Mathewson, A. (2000). Design for reliability. Microelectronics Reliability, 40:1285-1294.
Mitrani, I. (1982). Simulation Techniques for Discrete Events. Cambridge University Press, Cambridge.
Moen, R. D., Nolan, T. W., and Provost, L. P. (1991). Improving Quality Through Planned Experimentation. McGraw-Hill, New York.
Montgomery, D. C. (1985). Introduction to Statistical Quality Control. Wiley, New York.
Montgomery, D. C. (2005). Design and Analysis of Experiments. Wiley, New York, 6th edition.
Muffatto, M. (1999). Introducing a platform strategy in product development. International Journal of Production Economics, 60-61:145-153.
Muffatto, M. and Roveda, M. (2000). Developing product platforms: Analysis of the development process. Technovation, 20:617-630.
Murthy, D. N. P. (1996). Warranty and design. In Blischke, W. R. and Murthy, D. N. P., editors, Product Warranty Handbook. Marcel Dekker, New York.
Murthy, D. N. P. and Blischke, W. R. (2006). Warranty Management and Product Manufacture. Springer, London.
Murthy, D. N. P., Bulmer, M., and Eccleston, J. E. (2004a). Weibull model selection. Reliability Engineering and System Safety, 86:257-267.
Murthy, D. N. P., Djamaludin, I., and Wilson, R. J. (1993). Product warranty and quality control. Quality and Reliability Engineering International, 9:431-443.
Murthy, D. N. P., Hagmark, P. E., and Virtanen, S. (2008). Reliability design - iii: Product variety and reliability requirements. (Submitted for publication).Murthy, D. N. P., Page, N. W., and Rodin, E. Y. (1990). Mathematical Modelling. Pergamon Press, Oxford.
Murthy, D. N. P., Solem, O., and Roren, T. (2004b). Product warranty logistics: Issues and challenges. European Journal of Operational Research, 156:110-126.
Murthy, D. N. P., Xie, M., and Jiang, R. (2003). Weibull Models. Wiley, New York.
Nachlas, J. A. and Kumar, A. (1993). Reliability estimation using doubly-censored field data. IEEE Transactions on Reliability, 42:268-279.
NASA (2002). Fault Tree Handbook. NASA Office of Safety and Mission Assurance, Washington, DC.
NASA-STD-8729.1 (1998). Planning, Developing and Managing an Effective Reliability and Maintainability (R\&M) Program. NASA Technical Standards, Washington, DC.
Neal, C., Quester, P., and Hawkins, D. (1999). Consumer Behavior. McGraw-Hill, New York.
Nellore, R. and Balachandra, R. (2001). Factors influencing success in integrated product development (IPD) projects. IEEE Transactions on Engineering Management, 48(2):164174 .
Nelson, W. B. (1982). Applied Life Data Analysis. Wiley, New York.
Nelson, W. B. (1990). Accelerated Testing. Wiley, New York.
Nelson, W. B. (2003). Recurrent Events Data Analysis for Product Repairs, Disease Recurrence, and Other Applications. ASA-SIAM, Philadelphia.
Nelson, W. B. (2005a). A bibliography of accelerated test plans. IEEE Transactions on Reliability, 54:194-197.
Nelson, W. B. (2005b). A bibliography of accelerated test plans - part ii. IEEE Transactions on Reliability, 54:370-373.
Nieuwhof, G. W. E. (1984). The concept of failure in reliability engineering. Reliability Engineering, 7:53-59.
Nishida, S. I. (1992). Failure Analysis in Engineering Applications. Butterworth-Heinemann, Oxford.
Norris, K. C. and Landzberg, A. H. (1969). Reliability of controlled collapse interconnections. IBM Journal of Research and Development, 13:266-271.
Oakland, J. S. (2008). Statistical Process Control. Elsevier, Amsterdam, 6th edition.
O'Connor, P. (2002). Practical Reliability Engineering. Wiley, Chichester, 4th edition.
O'Connor, P. (2003). Testing for reliability. Quality and Reliability Engineering International, 19:73-84.
Oh, Y. S. and Bai, D. S. (2001). Field data analysis with additional after-warranty failure data. Reliability Engineering and System Safety, 72:1-8.
Oliver, R. L. (1996). Satisfaction: A Behavioral Perspective on the Consumer. McGraw-Hill, New York.
Otto, M. and von Mühlendahl, K. E. (2007). Electromagnetic fields (EMF): Do they play a role in children's environmental health (CEH)? International Journal of Hygiene and Environmental Health, 210(5):635-644.
Ottoson, S. (2004). Dynamic product development - DPD. Technovation, 24:207-217.
Oxford Dictionary (1989). Oxford English Dictionary. Oxford University Press, Oxford, 2nd edition.
Ozer, M. (1999). A survey of new product evaluation models. Journal of Product Innovation Management, 16:77-94.
Padmanabhan, V. (1996). Marketing and warranty. In Blischke, W. R. and Murthy, D. N. P., editors, Product Warranty Handbook. Marcel Dekker, New York.
Pahl, G. and Beitz, W. (1996). Engineering Design: A Systematic Approach. Springer, London, revised 2nd edition.Parsaei, H. R. and Sullivan, W. G. (1993). Concurrent Engineering - Contemporary Issues and Modern Design Tools. Chapman \& Hall, London.
Peace, G. S. (1993). Taguchi Methods. Addison-Wesley, Reading, MA.
Peck, D. S. (1979). New concerns about integrated circuit reliability. IEEE Transactions on Electron Devices, 26:38-43.
Pham, H. and Wang, H. (1996). Imperfect maintenance. European Journal of Operational Research, 94:425-438.
Porteus, E. L. (1986). Optimal lot sizing, process quality improvement and set-up cost reduction. Operations Research, 34:137-144.
Prasad, B. (1998). Designing products for variety and how to manage complexity. Journal of Product and Brand Management, 7:208-222.
Priest, J. W. (1988). Engineering Design for Producibility and Reliability. Marcel Dekker, New York.
Product Safety Directive (2001). Directive 2001/95/EC of 3 December 2001 on general product safety. Official Journal of the European Communities, Bruxelles, Belgium.
Prudhomme, G., Zwolinski, P., and Brissaud, D. (2003). Integrating into the design process the needs of those involved in the product life-cycle. Journal of Engineering Design, 14(3):333-353.
Pugh, S. (1990). Total Design: Integrated Methods for Successful Product Engineering. Addison-Wesley, Wokingham.
Quigley, J. (2003). Cost-benefit modelling for reliability growth. Journal of the Operational Research Society, 54:1234-1241.
Rademaker, A. W. and Antle, C. E. (1975). Sample size for selecting the better of two. IEEE Transactions on Reliability, 24:17-20.
Rai, B. and Singh, N. (2003). Hazard rate estimation from incomplete and unclean warranty data. Reliability Engineering and System Safety, 81:79-92.
Ramakrishnan, A. and Pecht, M. (2004). Load characterization during transportation. Microelectronics Reliability, 44:333-338.
Rausand, M. and Høyland, A. (2004). System Reliability Theory; Models, Statistical Methods, and Applications. Wiley, Hoboken, NJ., 2nd edition.
Reichheld, F. (1996). The Loyalty Effect. Harvard Business School Press, Cambridge MA.
Reid, S. E. and de Brentani, U. (2004). The fuzzy front end of new product development for discontinuous innovations: A theoretical model. Journal of Product Innovation Management, 21:170-184.
ReVelle, J. B., Moran, J. W., and Cox, C. A. (1998). The QFD Handbook. Wiley, New York.
Rink, D. R. and Swan, J. F. (1979). Product life cycle research: A literature review. Journal of Business Research, pages 219-242.
Robinson, D. and Dietrich, D. (1987). A new nonparametric growth model. IEEE Transactions on Reliability, 36:411-418.
Robinson, D. and Dietrich, D. (1989). A nonparametric-Bayes reliability growth model. IEEE Transactions on Reliability, 38:591-598.
Robinson, J. A. and McDonald, G. C. (1991). Issues related to field reliability data. In Liepins, G. E. and Uppuluri, V. R. R., editors, Data Quality Control - Theory and Pragmatics. Marcel Dekker, New York.
Roesch, W. J. (2006). Historical review of compound semiconductor reliability. Microelectronics Reliability Engineering, 46:1218-1227.
Roesch, W. J. and Brockett, S. (2007). Field returns, a source of natural failure mechanisms. Microelectronics Reliability, 47:1156-1165.Roland, H. E. and Moriarty, B. (1990). System Safety Engineering and Management. Wiley, New York, 2nd edition.
Roozenburg, N. F. M. and Eekels, J. (1995). Product Design; Fundamentals and Methods. Wiley, Chichester.
Ross, S. M. (1996). Stochastic Processes. Wiley, New York, 2nd edition.
Ross, S. M. (2002). Simulation. Academic Press, San Diego, 3rd edition.
Rupp, N. and Taylor, C. (2002). Who initiates recalls and who cares? evidence from the automotive industry. Journal of Industrial Economics, 50:123-150.
Ryan, T. P. (1989). Statistical Methods for Quality Improvement. Wiley, New York.
Salvador, F., Forza, C., and Rungtusanatham, M. (2002). Modularity, product variety, production volume, and component sourcing: theorizing beyond generic prescriptions. Journal of Operations Management, 20:549-575.
Sander, P., Toscano, L., Luitejns, S., Huijben, H., and Brombacher, A. C. (2003). Warranty data analysis for assessing product reliability. In Murthy, D. N. P. and Blischke, W. R., editors, Case Studies in Reliability and Maintenance. Wiley, New York.
Schilling, E. G. (1982). Acceptance Sampling in Quality Control. Marcel Dekker, New York.
Schmidt, A. E. (1976). A view of the evolution of the reliability improvement warranty. Report 76-1, Defense Systems Management College, Ft Belvoir, VA.
Schmoldas, A. E. (1977). Improvement of weapon system reliability through reliability improvement warranties. Report 77-1, Defense Systems Management College, Ft Belvoir, VA.
Schneider, H. (1989). Failure-censored variable-sampling plans for log-normal and Weibull distributions. Technometrics, 31:199-206.
Sen, A. (1998). Estimation of current reliability in a duane-based reliability growth model. Technometrics, 40:334-344.
Sillanpää, M. and Okura, J. H. (2004). Flip chip on board: Assessment of reliability in cellular phone application. IEEE Transactions on Components and Packaging Technologies, 27:461-467.
Sim, S. K. and Duffy, A. H. B. (2003). Towards an ontology of generic engineering design activities. Research in Engineering Design, 14:200-223.
Sinha, M. N. and Willborn, W. O. (1985). The Management of Quality Assurance. Wiley, New York.
Sirvanci, M. (1986). Comparison of two Weibull distributions under random censoring. Communications in Statistics - Series A: Theory and Methods, 15:1819-1836.
Smith, G. (2004). Statistical Process Control and Quality Improvement. Prentice-Hall, Upper Saddle River, New Jersey, 5th edition.
Sohn, S. Y. and Choi, H. (2001). Analysis of advertising lifetime for mobile phone. Omega, 29:473-478.
Song, X. M. and Montoya-Weiss, M. M. (1998). Critical development activities for really new versus incremental products. Journal of Product Innovation Management, 15:124-135.
Spiegler, I. and Herniter, J. (1993). Warranty cards as a new source of industrial marketing information. Computers in Industry, 22:273-281.
Spoormaker, J. L. (1995). The role and analysis in establishing design rules for reliable plastic products. Microelectronics Reliability, 35:1275-1284.
Spunt, T. V. (2003). Guide to Customer Surveys. Published Customer Services Group, 2nd edition.
Stevens, D. and Crowder, M. J. (2004). Bayesian analysis of discrete time warranty data. Journal of the Royal Statistical Society C, 53:195-217.Stone, H. S. (1972). Introduction to Computer Organization and Data Structures. McGrawHill, New York.
Suh, N. P. (2001). Axiomatic Design - Advances and Applications. Oxford University Press, New York.
Suzuki, K. (1985a). Estimation of lifetime parameters from incomplete field data. Technometrics, 27:263-271.
Suzuki, K. (1985b). Non-parametric estimation of lifetime distributions from a record of failures and follow-ups. Journal of the American Statistical Association, 80:68-72.
Suzuki, K. (1987). Analysis of field failure datafrom a non-homogeneous poisson process. Rep. Stat. Appl. Res. JUSE, 40:10-20.
Suzuki, K. (1995). Role of field performance data and its analysis. In Balakrisnan, N., editor, Recent Advances in Lif Testing and Reliability. CRC Press, Boca Raton.
Suzuki, K., Karim, M. R., and Yamamoto, W. (2001). Statistical analysis of reliability warranty data. In Balakrisnan, N. and Rao, C. R., editors, Advances in Reliability, pages 585609. Elsevier, Amsterdam.

Syed, A. and Doty, M. (1999). Are we over-designing for solder joint reliability? Field vs. accelerated conditions, realistic vs. specified requirements. In Proceedings of the 1999 Electronic Component and Technology Conference, pages 111-117.
Szweda, R. (2005/2006). Organic light-emitting devices - friend or foe? The Advanced Semiconductor Magazine, December/January:36-39.
Taguchi, G. (1986). Introduction to Quality Engineering: Designing Quality into Products and Processes. Asian Productivity Organization, Tokyo.
Takeuchi, H. and Nonaka, I. (1984). The new product development game. Harvard Business Review, pages 137-146.
Tarasewich, P. and Nair, S. K. (2000). Design for quality. Engineering Management Review, 28(1):76-78.
Tatikonda, M. V. and Rosenthal, S. R. (2000). Successful execution of product development projects: Balancing firmness and flexibility in the innovation process. Journal of Operations Management, 18:401-425.
Tee, T. Y., Ng, H. S., Yap, D., Baraton, X., and Zheng, Z. (2003). Board level solder joint reliability modeling and testing TFBGA packages for telecommunication applications. Microelectronics Reliability, 43:1117-1123.
Thompson, J. R. and Koronacki, J. (2002). Statistical Process Control: The Deming Paradigm and Beyond. Chapman \& Hall, Boca Raton, 2nd edition.
Torra, V., editor (2003). Information Fusion in Data Mining. Springer, New York.
Trimble, R. F. (1974). Interim Reliability Improvement Warranty (RIW) Guidelines. HQ USAF Directorate of Procurement Policy Document, Dept. of the Air Force, Washington, DC.
Udell, G. G. and Baker, K. G. (1982). Evaluating new product ideas ... systematically. Technovation, pages 191-202.
Ullman, D. G. (2003). The Mechanical Design Process. McGraw-Hill, New York, 3rd edition.
Ulrich, K. T. and Eppinger, S. D. (1995). Product Design and Development. McGraw-Hill, New York.
Ulwick, A. W. (2002). Turn customer input into innovation. Harvard Business Review, pages 92-97.
Urban, G. L. and Hauser, J. R. (1993). Design and Marketing of New Products. Prentice-Hall, Englewood Cliffs.
Van Hemel, C. G. and Keldmann, T. (1996). Applying "design for X" experience in design for environment. In Huang, G. Q., editor, Design for X - Concurrent Engineeering Imperatives. Chapman \& Hall, London.Veryzer, R. W. (1998). Discontinuous innovation and the new product development process. Journal of Product Innovation Management, 15:304-321.
Vincenti, W. G. (1990). What Engineers Know and How They Know It: Analytical Studies from Aeronautical Engineering. John Hopkins University Press, Baltimore.
Wadsworth, H. M., Stephens, K. S., and Godfrey, A. B. (2002). Modern Methods for Quality Control and Improvement. Wiley, New York, 2nd edition.
Walls, L. A. and Bendell, A. (1986). The structure and exploration of reliability field data: What to look for and how to analyse it. Reliability Engineering, 15:115-143.
Walls, L. A. and Quigley, J. (1999). Learning to improve reliability during system development. European Journal of Operational Research, 119:495-509.
Walsh, S. T., Boylan, R. L., McDermott, C., and Paulsen, A. (2005). The semiconductor sisicon roadmap: Epochs driven by dynamics between disruptive technologies and core competencies. Technological Forecasting \& Social Change, 72:213-236.
Wang, L. and Suzuki, K. (2001a). Lifetime estimation based on warranty data without date-ofsale information cases where usage time distributions are known. Journal of the Japanese Society for Quality Control, 31:148-167.
Wang, L. and Suzuki, K. (2001b). Non-parametric estimation of lifetime distributions from warranty data without monthly unit sales information. Journal of Reliability Engineering Association of Japan, 23:145-154.
Wang, L., Suzuki, K., and Yamamoto, W. (2002). Age-based warranty data analysis without date-specific sales information. Reliability Engineering and System Safety, 18:323-337.
Wang, Y., Lu, C., Li, X. M., and Tse, Y. C. (2005). Simulation of drop/impact reliability for electronic devices. Finite Elements in Analysis and Design, 41:667-68.
Ward, H. and Christer, A. H. (2005). Modelling the re-design decision for a warranted product. Reliability Engineering and System Safety, 88:181-189.
Weber, C., Werner, H., and Deubel, T. (2003). A different view on product data management / product life cycle management and its future potentials. Journal of Engineering Design, 14(4):447-464.
Weiss, H. K. (1956). Estimation of reliability growth in a complex system with poisson-type failure. Operations Research, 4:532-545.
Westphal, C. and Blaxton, T. (1998). Data Mining Solutions. Wiley, New York.
Wheelwright, S. C. and Clark, K. B. (1992). Revolutionizing Product Development - Quantum Leaps in Speed, Efficiency and Quality. The Free Press, New York.
Wilhelm, W. E. and Xu, K. (2002). Prescribing product upgrades, prices and product levels over time in a stochastic environment. European Journal of Operational Research, $138: 601-621$.
Wong, K. M. (1989). The roller-coaster curve is in. Quality and Reliability Engineering International, 5:29-36.
Woodruff, R. B. and Gardial, S. F. (1996). Know Your Customer: New Approaches to Understanding Customer Value and Satisfaction. Blackwell, Cambridge MA.
Wu, H. and Meeker, W. Q. (2002). Early detection of reliability problems using information from warranty databases. Technometrics, 44:120-133.
Wu, J. D., Ho, S. H., Juang, C. Y., Liao, C. C., Zheng, P. J., and Hung, S. C. (2002). Board level reliability of a stacked CSP subjected to cyclic bending. Microelectronics Reliability, $42: 407-416$.
Yang, G. (2007). Life Cycle Reliability Engineering. Wiley, Hoboken, New Jersey.
Yeh, R. H., Ho, W. T., and Tseng, S. T. (2000). Optimal preventive-maintenance warranty policy for repairable products. European Journal of Operational Research, 129:575-582.Yeh, R. H. and Lo, H. C. (1998). Quality control for products under free repair warranty. International Journal of Quality Management, 4:265-275.
Zeng, Y. and Gu, P. (1999). A science-based approach to product design. Robotics and Computer Integrated Manufacturing, 15:331-352.
Zhang, S., Shen, W., and Ghenniwa, H. (2004). A review of internet-based product information sharing and visualization. Computers in Industry, 54:1-15.# Index 

accelerated failure time, 70, 236
accelerated test, 150, 153, 236
accelerated test model
Arrhenius, 151
Eyring, 152
inverse power law, 152
Norris-Landzberg, 153
acceleration factor, 151, 152
acceptance sampling, 185
age reduction, 75
allocation, 136, 137, 257
analytical hierarchy process, 99
Arrhenius model, 151
assembly error, 179
asymptotically unbiased, 160
availability, 79,113
average, 79
mission, 79
steady state, 79
Bayes theorem, 161, 167
Bayesian approach, 160, 167
Bayesian estimate, 161
black-box model, 67, 229
built-in test, 113
burn-in test, 86, 180, 186, 188
business objectives, 26
case study
cellular phone, 10, 20, 33, 143, 170, 187, 210, 224
safety instrumented system, 11, 20, 58, $67,69,70,78,80,111,134,136,139$, 170,214

CE mark, 217, 219
CEN, 220
CENELEC, 220
Coffin-Manson model, 153
command fault, 58
computer aided design, 234
concept development, 104
confidence coefficient, 164
confidence interval, 164
conforming item, 174
conformity assessment, 219
conjoint analysis, 97, 98
consequence analysis, 222
consequence of failure, 59
constraint, 39, 46
consumer, 4
contract, 112, 117
control chart, 181
cost, 87
design, 87
development, 87, 115, 128, 133, 141, 142
maintenance, 87
post-sale, 87
production, 87, 115, 142
support, 115
cost model, 108
Cox model, 73
critical items list, 78
customer loyalty, 100
customer requirement, 27
customer satisfaction, 100, 105
customer understanding, 96
CUSUM, 181data, 227
censored, 156, 160
complete, 156
data analysis, 94
data collection, 93, 240, 244
data mining, 233, 245, 246
data reduction, 246
database management, 243
de facto, 231
de jure, 231
decision variable, 124, 133, 141
declaration of conformity, 219
degradation, 126
degradation test, 86
degree of belief, 160
Delphi method, 109
dependability, 6, 258
dependability management, 258
design for X, 30
design limit test, 150
design of experiment, 154, 155, 236
design phase, 29
design review, 30, 258
development phase, 31
diagnostic test, 21
diagnostics, 258
DIK, 227, 231-233, 235, 236
directive, 217
machinery, 218
new approach, 217
product safety, 219
distribution
exponential, 63, 155, 165
gamma, 161
Weibull, 64, 124, 155, 158, 162, 165
scale parameter, 64
shape parameter, 64
distribution function
empirical, 157, 196
sample, 157
DNV RP A203, 19
DOE, 154
DOE-NE-STD-1004-92, 85
ECSS-Q-30-02A, 257
ECSS-Q-40B, 212, 258
efficiency of estimator, 159
EHSR, 216, 218-220, 224
environmental stress screening, 86, 180
environmental stress test, 150
environmental test, 31, 236
equipment under control, 216
ESA, 212
estimate, 159
estimator, 159
ETSI, 220
expert judgement, 106
expert opinion, 109
Eyring model, 152
fail safe, 258
failure, 56
common cause, 59
complete, 58
definition, 258
extended, 58
gradual, 58
intermittent, 58
overstress, 58
partial, 58
primary, 58
random hardware, 58
secondary, 58
single point, 259
sudden, 58
systematic, 58, 260
failure cause, 57
failure distribution function, 62
failure mechanism, 57, 258
failure mode, 57, 258
failure mode analysis, 145
failure rate function, 62, 158
bathtub curve, 65
cumulative, 63, 158
roller coaster curve, 65
Weibull, 64
false alarm, 140
fault, 57, 258
fault tolerance, 258
fault tree, 70
fault tree analysis, 134, 235, 258
field test, 31
fish-bone diagram, 203
FMEA/FMECA, 78, 134, 214, 221, 235
force of mortality, 63
FRACAS, 85
free replacement warranty, 103
free replacement warranty policy, 108front-end, 7, 24, 91
function
auxiliary, 56
essential, 56
information, 56
interface, 56
protective, 56
superfluous, 56
functional analysis, 47
functional decomposition, 134, 136
functional requirement, 38
gamma function, 64
graphical analysis, 157
harm, 222, 258
harmonized standard, 217
hazard, 221, 224, 258
hazard and operability study, 111
hazardous event, 258
HAZOP, 111, 216, 221
idea generation, 97
IEC 14620-3, 214
IEC 60050-191, 5, 6, 56, 57, 73, 257-260
IEC 60300-1, 6, 24, 258
IEC 60300-3-3, 87
IEC 61014, 84
IEC 61025, 70
IEC 61160, 258
IEC 61164, 85
IEC 61508, 12, 58, 112
IEC 61511, 212, 214, 215, 258
IEC 61882, 216
IEC 62347, 259
information, 227
interval estimation, 158
inverse power law model, 152
ISO 12100-1, 220, 221, 258, 259
ISO 13849-1, 220
ISO 13850, 220
ISO 14121-1, 220-223
ISO 14620-3, 212
ISO 14971, 221
ISO 8402, 15
ISO 9000, 42, 260
knowledge, 228, 234
LCC, 87, 115, 118, 258
life cycle cost, $87,115,127,258$
life cycle phase, 221
likelihood function, 159, 160, 163
loyalty, 101
machinery
definition, 218, 258
maintainability, 31, 259
maintenance, 73
corrective, 73,257
definition, 259
preventive, 73, 74, 140, 259
maintenance policy
age-based, 75
clock-based, 75
condition-based, 75
design-out, 75
opportunity-based, 75
usage-based, 75
market survey, 94
marketing, 33
Markov model, 77
maximum likelihood estimate, 159, 163
mean time between failures, 113
mean time to failure, 63
exponential, 64
Weibull, 64
median life, 151
method of moments, 159, 162
method of percentiles, 162
MIL-HDBK-217F, 72
MIL-HDBK-338B, 84, 85, 257, 259, 260
MIL-STD 2155, 85
misuse, 221
reasonably foreseeable, 221, 259
model, 229, 233, 235, 246
model analysis, 230
model building, 229
model validation, 66, 230
modular design, 48
moment estimator, 159
Monte Carlo simulation, 82
MTBF, 113, 114, 167
MTTF, 63, 80, 151, 152
MTTR, 80
NASA, 70
new approach directive, 217
new product development, 2, 22, 259drivers, 25
model, 23
newness of product, 18
non-conforming item, 174, 175, 178, 184
non-repairable item, 81
nonparametric model, 165
Norris-Landzberg model, 153
notified body, 219
objective function, 130, 133
operational test, 169
optimal decision, 141
original equipment manufacturer, 225
out of control, 174, 183
outgoing quality, 184
outsourcing, 115
P-P plot, 157
Pareto analysis, 203
percentile, 159, 162
percentile estimator, 159
performance, 39, 259
actual, 7,41
desired, 7, 40, 45, 122
predicted, 41
period of ownership, 21
PFD, 80, 81, 112, 136, 139, 216
physical modelling, 66
point estimation, 158
Poisson process, 82
post-production phase, 33
posterior density, 161
preference, 38
prior density, 160
pro rata rebate warranty, 103
pro rata rebate warranty policy, 109
probability density function, 62
Weibull, 64
probability of failure on demand, 80
probability plot, 157
process control, 32
product, 15
commercial, 16
custom-built, 16, 32, 110, 127, 133
durable, 16
industrial, 16
new, 17
non-durable, 16
second-hand, 17
specialized, 16, 32, 110
standard, 16, 133, 148
tangible, 260
product architecture, 30, 104
product classification, 16
product decomposition, 19
product definition, 26
product failure, 128
product life, 21
product life cycle, 2, 7, 21, 24
product modularization, 28
product performance, 7,39
product platform, 28, 126
product reliability, 5, 132
product safety, 211
product specification, 8,42
product support, 34, 103
product variety, 126, 132
production
batch, 177, 183
continuous, 177, 181
production phase, 32
production process, 181
profit, 102
project risk, 115
proof test, 215
proportional hazards model, 71, 236
QFD, 27, 97
qualification test, 86
quality control, 175, 180, 187
quality function deployment, 27, 97
quality of testing, 184
quality variation, 177, 180, 184
rapair
normal, 74
RAPEX, 219
redundancy, 83, 136, 139, 259
active, 83,257
cold, 257
cold standby, 139
fully energized, 139
hot, 258
passive, 83, 139
standby, 260
warm standby, 139
regression analysis, 165
reliabilitydefinition, 5, 259
design, 60
field, 60
inherent, 60
of machine, 259
reliability allocation, 82,137
reliability apportionment, 82
AGREE, 83
ARINC, 83
equal, 83
feasibility of object, 83
minimum effort, 83
reliability assessment, 85,86
reliability block diagram, 67, 68, 82
2-out-of-3 system, 69
parallel system, 69
series system, 68
reliability database, 244
reliability engineering, 55, 82
reliability growth, 84, 140, 149, 165, 259
Crow/AMSAA, 84
Duane, 84, 166
IBM, 84
Jelinski \& Moranda, 84
Littlewood, 84
Littlewood \& Verrall, 84
Lloyd \& Lipow, 84, 166
Musa, 84
Musa \& Okumoto, 84
Weiss, 166
reliability improvement warranty, 113
reliability management, 55, 87, 227, 237, 238, 248
reliability modelling, 61
reliability performance, 9
reliability prediction, 85
reliability qualification, 170
reliability science, 55, 61
reliability specification, 9,142
reliability test, 31
renewal equation, 81
repair
imperfect, 74
minimal, 74
repairable item, 82
reputation, 100
requirement, 37, 110, 216, 259
customer, 38,110
functional, 38
performance, 110
regulatory, 38
safety, 216
technical, 38
return on investment, 102
revenue, 102
risk, $115,134,168,222$
definition, 222, 259
estimate, 222
risk assessment, 221
risk mitigation, 150
robustness, 155
ROCOF, 75-77, 105, 123-126, 128, 130, $178,179,186,192,193$
cumulative, 75
empirical, 196
root cause analysis, $85,150,156,182,237$
safety instrumented function, 111, 214, 215
safety integrity level, 81,216
safety requirement specification, 112, 214
satisfaction, 100, 101, 105
scientific theory, 229
severity, 222
SIL, 81, 111, 136
specification, $8,42,45$
definition, 259
SRS, 112, 214
standard
EN, 220
harmonized, 218, 220
national, 220
structure function, 68
survivor function, 62
conditional, 63
exponential, 63
proportional hazards, 72
system reliability, 69
systems approach, 9
TAAF, 84, 85, 140, 148, 149, 260
Taguchi method, 32, 181
tangible product, 15
technical construction file, 223
technical risk, 115
technological uncertainty, 19
test
accelerated, 150
acceptance, 257built-in, 257
design limit, 150
environmental stress, 150
qualification, 259
theory, 228
time to failure, 61
type 1 error, 186
type 2 error, 186
unavailability, 80
unbiased estimator, 159
usage rate, 125,128
useful life, 21
validation, 31
value analysis, 48
variance, 159
verification, 31,222
virtual age, 75
warranty, 94, 103
cost, 87
free replacement policy, 103, 108
pro rata rebate policy, 103, 109
reliability improvement, 113
warranty cost, 108, 109, 115, 129, 237
expected, 132
warranty elasticity, 103
warranty period, 103
Weibull, 124
white-box model, 66, 229