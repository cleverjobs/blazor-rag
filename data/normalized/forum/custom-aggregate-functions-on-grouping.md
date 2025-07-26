# Custom Aggregate functions on Grouping

## Question

**lak** asked on 03 Mar 2020

Does blazor Grid support custom Aggregate functions on grouping with alignment?

## Answer

**Marin Bratanov** answered on 04 Mar 2020

Hello, Please Follow the feature request I made from your previous question about this: [https://feedback.telerik.com/blazor/1456063-group-header-templates-should-expose-aggregates-for-all-the-fields-and-allow-you-to-align-them-with-the-columns](https://feedback.telerik.com/blazor/1456063-group-header-templates-should-expose-aggregates-for-all-the-fields-and-allow-you-to-align-them-with-the-columns) Regards, Marin Bratanov

### Response

**Stefano** commented on 21 Apr 2022

Hello, maybe I'm not understanding something, but I think the responste doesn't give an answer to the question, at least as it is expressed in the title: "Custom Aggregate functions on Grouping". Is is possible to have custom Aggregate functions on Grouping? I have this kind of need. In a column I have values I need to sum, but they area a particular kind of values. Non decimal values but sexadecimal. So I cannot use the default aggregate functions to compute the sum for grand total and group totals (to show in the group footer). How can I get such result? Thank you!

### Response

**Marin Bratanov** commented on 23 Apr 2022

Hi Stefano, The improvement idea I linked is the closest that is likely to be available out of the box. Entirely custom aggregates are unlikely to be officially supported since there is no way to know exactly what they are about. What you could do, however, is to use the appropriate template and, via a bit of code in it (e.g., a lambda or a child component) make a separate async request for the server to provide the required aggregation.
