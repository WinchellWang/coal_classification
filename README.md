中国煤类型自动分类器，依据国标制作。

Chinese Coal Type Automatic Classifier, made according to the Chinese standard.

# How to Use? 如何使用？

请编辑'CoalData_Sample.csv'中的数据增加需要检测的煤数据，之后运行'main.py'。

煤的类型取决于'Result.csv'中一行内重复最多次的煤类型。

Please input your coal data as required in 'CoalData_Sample.csv' and run 'main.py.'

The coal type based on each criterion will be displayed in 'Result.csv.' The coal type will depend on the most frequent type shown in a row.

# Chinese Coal Classification
Coal Classification Code based on Chinese Coal Classification Criterion (GB5751)

|类别|代号|编码|分类指标||||||
|---|---|---|---|---|---|---|---|---|
||||V<sub>daf</sub>/%|G|Y/mm|b/%|P<sub>M</sub>/%<sup>b</sup>|Q<sub>gr,maf</sub>/%<sup>c</sup>/(MJ•kg<sup>-1</sup>)|
|无烟煤|WY|01, 02, 03|$$\leq10.0$$|
|贫煤|PM|11|$$>10.0\sim20.0$$|$$\leq5$$|
|贫瘦煤|PS|12|$$>10.0\sim20.0$$|$$>5\sim20$$|
|瘦煤|SM|13, 14|$$>10.0\sim20.0$$|$$>20\sim65$$|
|焦煤|JM|24|$$>20.0\sim28.0$$|$$>50\sim65$$|$$\leq25.0$$|$$\leq150$$|
|焦煤|JM|15, 25|$$>10.0\sim28.0$$|$$>65^a$$|$$\leq25.0$$|$$\leq150$$|
|肥煤|FM|16, 26, 36|$$>10.0\sim37.0$$|$$(>85)^a$$|$$>25.0$$|
|1/3 焦煤|1/3JM|35|$$>28.0\sim37.0$$|$$>65^a$$|$$\leq25.0$$|$$\leq220$$|
|气肥煤|QF|46|$$>37.0$$|$$(>85)^a$$|$$>25.0$$|$$>220$$|
|气煤|QM|34|$$>28\sim37.0$$|$$>50\sim65$$|$$\leq25.0$$|$$\leq220$$|
|气煤|QM|43, 44, 45|$$>37.0$$|$$>35$$|$$\leq25.0$$|$$\leq220$$|
|1/2 中黏煤|1/2ZN|23,  33|$$>20.0\sim37.0$$|$$>30\sim50$$|
|弱黏煤|RN|22, 32|$$>20.0\sim37.0$$|$$>5\sim30$$|
|不黏煤|BN|21, 31|$$>20.0\sim37.0$$|$$\leq5$$|
|长焰煤|CY|41, 42|$$>37.0$$|$$\leq35$$|||$$>50$$|
|褐煤|HM|51|$$>37.0$$||||$$\leq30$$|$$\leq24$$|
|褐煤|HM|52|$$>37.0$$||||$$>30\sim50$$|$$\leq24$$|

> <sup>a</sup> 在G>85的情况下，用Y值或b值来区分肥煤、气肥煤与其他煤类，当Y>25.00 mm时，根据V<sub>daf</sub>的大小可划分为肥煤或气肥煤；当Y≤25.0 mm时，则根据V<sub>daf</sub>的大小可划分为焦煤，1/3 焦煤或气煤。
> 
> 按b值划分类别时，当V<sub>daf</sub>≤28.0%时，b>150%的为肥煤；当V<sub>daf</sub>>28.0%时，b>220%的为肥煤或气肥煤。如按b值和Y值划分的类别有矛盾时，以Y值划分的类别为准。
> 
> <sup>b</sup> 对V<sub>daf</sub>>37.0%，G≤5的煤，再以透光率P<sub>M</sub>来区分其为长焰煤或褐煤。
>
> <sup>c</sup> 对V<sub>daf</sub>>37.0%，P<sub>M</sub>>30%~50%的煤，再测Q<sub>gr,maf</sub>，如其值大于24 MJ/kg，应划分为长焰煤，否则为褐煤。

|Category|Symbol|Code|Classification Indicator||||||
|---|---|---|---|---|---|---|---|---|
||||V<sub>daf</sub>/%|G|Y/mm|b/%|P<sub>M</sub>/%<sup>b</sup>|Q<sub>gr,maf</sub>/%<sup>c</sup>/(MJ•kg<sup>-1</sup>)|
|Anthracite|WY|01, 02, 03|$$\leq10.0$$|
|Anthracite Coal|PM|11|$$>10.0\sim20.0$$|$$\leq5$$|
|Anthracite Lean Coal|PS|12|$$>10.0\sim20.0$$|$$>5\sim20$$|
|Lean Coal|SM|13, 14|$$>10.0\sim20.0$$|$$>20\sim65$$|
|Coking Coal|JM|24|$$>20.0\sim28.0$$|$$>50\sim65$$|$$\leq25.0$$|$$\leq150$$|
|Coking Coal|JM|15, 25|$$>10.0\sim28.0$$|$$>65^a$$|$$\leq25.0$$|$$\leq150$$|
|Fertilizer Coal|FM|16, 26, 36|$$>10.0\sim37.0$$|$$(>85)^a$$|$$>25.0$$|
|1/3 Coking Coal|1/3JM|35|$$>28.0\sim37.0$$|$$>65^a$$|$$\leq25.0$$|$$\leq220$$|
|Gas Fertilizer Coal|QF|46|$$>37.0$$|$$(>85)^a$$|$$>25.0$$|$$>220$$|
|Gas Coal|QM|34|$$>28\sim37.0$$|$$>50\sim65$$|$$\leq25.0$$|$$\leq220$$|
|Gas Coal|QM|43, 44, 45|$$>37.0$$|$$>35$$|$$\leq25.0$$|$$\leq220$$|
|1/2 Medium Viscous Coal|1/2ZN|23,  33|$$>20.0\sim37.0$$|$$>30\sim50$$|
|Weakly Viscous Coal|RN|22, 32|$$>20.0\sim37.0$$|$$>5\sim30$$|
|Non-viscous coal|BN|21, 31|$$>20.0\sim37.0$$|$$\leq5$$|
|Long Flame Coal|CY|41, 42|$$>37.0$$|$$\leq35$$|||$$>50$$|
|Lignite|HM|51|$$>37.0$$||||$$\leq30$$|$$\leq24$$|
|Lignite|HM|52|$$>37.0$$||||$$>30\sim50$$|$$\leq24$$|


> <sup>a</sup> In the case of G>85, the Y value or b value is used to separate fertilizer coal, gas fertilizer coal and other coal categories. When Y>25.00 mm, it can be classified as fertilizer coal or gas fertilizer coal according to the size of V<sub>daf</sub>; when Y≤25.0 mm, it can be classified as coking coal, 1/3 coking coal or gas coal according to the size of V<sub>daf</sub>.
> 
> When classified according to b value, when V<sub>daf</sub>≤28.0%, b>150% is fertilizer coal; when V<sub>daf</sub>>28.0%, b>220% is fertilizer coal or gas fertilizer coal. If there is a contradiction between the categories classified according to the b value and the Y value, the category classified according to the Y value shall prevail.
> 
> <sup>b</sup> For coals with V<sub>daf</sub>>37.0% and G≤5, the transmittance P<sub>M</sub> is used to classify them as long flame coals or lignite coals.
>
> <sup>c</sup> For coal with V<sub>daf</sub>>37.0% and P<sub>M</sub>>30%~50%, then measure Q<sub>gr,maf</sub>, if the value is more than 24 MJ/kg, it should be classified as long flame coal, otherwise it is lignite coal.
