## Exercises

### For each of the following questions, formulate a null and alternative hypothesis (be as specific as you can be), then give an example of what a true positive, true negative, type I and type II errors would look like. Note that some of the questions are intentionally phrased in a vague way. It is your job to reword these as more precise questions that could be tested.

#### 1. Has the network latency gone up since we switched internet service providers?
- ISP 1 vs ISP 2 (discrete, boolean, isp_switch)
- Network latency (continuous, net_latency)
- Comparison of means of two groups (t-test)

H{0} : latency (mean a) is less than or equal latency b(mean)

H{a}: latency (mean a) is greater than latency (mean b)

True Positive: Reject H{0} when H{0} is false (latency went up and we said it did)

True Negative: Accept H{0} when H{0} is true (fail to reject H{0} (latency didnt go up and we said it didnt)

Type 1 error: Latency did not go up with ISP switch, but we said it did

Type 2 error: Latency did go up with ISP switch, but we said it didnt

#### 2. Is the website redesign any good?

- Question: Are we getting more traffic on the website since the website redesign?
- Variables: Website redesign (web_redesign),discrete, boolean ('True' or 'False) AND web traffic hits (traffic_rate), continuous variable
- H{0}: There is no difference in website traffic since the website redesign
- H{a}: There is a significant difference in website trafic since the redesign

True Positive: Reject H{0} when H{0} is false (Traffic is greater than before and after website redesign and we said it would be greater)

True Negative: Accept H{0} when H{0} is true (fail to reject H{0}) (Traffic is less than or equal to the rate when website was redesigned, and we said it would be less than or equal)

Type 1 Error: There is no significant increase in website traffic since the redesign, but we conclude that there is a significant increase in website traffic with website redesign (we reject the null)

Type 2 Error: There is a significant increase in website traffic since the redesign, but we conclude that the traffic level is less than or the same as before (we accept the null)




#### 3.  Is our television ad driving more sales?
Question: Did the television add increase sales for the company?

Variables: TV_ad (discrete/categorical), boolean (True, False); Sales figures ('sales'), continuous variable

H{0}: The introduction of a TV add had no significant impact on sales (sales2 <= sales 1)
H{a}: The introduction of a TV add had a significant impact on sales (sales 2 > sales 1)

True Positive: Reject H{0} when H{0} is false (The TV add drove more sales, and we said the TV add drove more sales)

True Negative: Accept H{0} when H{0} is true (The TV add did not drive more sales, and we agreed with (H0) that there was no signficant increase in sales with the new TV add)

Type 1 error: There was no increase in sales with the new TV ad, but we conclude there is a significant increase in sales from the TV ad (we rejected the null)

Type 2 error: There was a significant increase in sales with the new TV ad, but we conclude that there is no significant increase in sales (we accepted the null)

