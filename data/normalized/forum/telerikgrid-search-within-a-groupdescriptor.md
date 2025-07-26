# TelerikGrid search within a GroupDescriptor ?

## Question

**Jon** asked on 20 May 2024

Data has 6 columns, A, B, C with a value and a date. AValue - double ADate - datetime BValue - double BDate - datetime CValue - double CDate - datetime Client requests that one of the 3 values A, B, C is chosen by drop down. In a code-behind we group by a particular Value and then sort descending so that the highest value is on top of the grouping. Easy. But then inside the grouping of Value are to be rows from the data that are not matched by Value but by a Search based on date range +- 5 minutes. Example: client selects A Grid groups by AValue and then sorts DESC Inside Group[0] the client wants to Search all the GridData and display BValue and CValue that fall within a date range +- 5 minutes from Group[0].ADate Right now I see SearchFilter inside the GridState class (for the whole Grid) but I think for what the client needs we would have a SearchFilter inside of GroupDescriptor (for that Group)? Is this possible? If that is not possible, would it be possible to use 1 GridData as the source for the Grid and another GridData as the source for the Grid that appears inside each grouping? Note: for one row in the data, the max value may be A, B or C. But the date times in that row do not match up. They are 3 different date time values.

### Response

**Jonathan** commented on 20 May 2024

I think DetailTemplate is the answer I am looking for?

### Response

**Hristian Stefanov** commented on 23 May 2024

Hi Jonathan, From the provided information, I can confirm that the DetailTemplate within the Hierarchical Grid configuration seems suitable for this scenario. I remain at your disposal if you face any difficulties with its utilization. Kind Regards, Hristian
