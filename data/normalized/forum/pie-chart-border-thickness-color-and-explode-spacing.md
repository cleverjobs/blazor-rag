# Pie chart border thickness/color and explode spacing

## Question

**Pat** asked on 13 Mar 2023

Hi I'm trying to add some spacing between the pie pieces in a pie chart. I can achieve this by using the ExplodeField property and setting true on all the series items. However i would like to have the spacing between the pieces a bit smaller, is this possible? Also i would like to be able to set stroke color and width of the pieces. I cant find any info on how to achieve this in the documentation. See attached image on what i'm trying to do. I have fiddled with the rendered html in dev tools. Thanks in advance!

## Answer

**Nadezhda Tacheva** answered on 15 Mar 2023

Hi Patrik, Please see my comments on the relevant points as follows: Spacing between the pie pieces You are correct that you can use the ExplodeField property as a workaround. However, we have an opened feature request for allowing configuration of the spaces between all segments. I voted on your behalf to bump the popularity of the request - we prioritize to enhancements based on the community demand. The public post also lists a workaround with CSS that you can use for the time being. Stroke color It is not currently possible to set stroke to the segments but we will expose such an option in a future version of the product through border settings for series in Chart. I added your vote there as well. You may follow the posts to get status updates. This is the best way to track the progress of items. I hope you will find the above information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Patrik** commented on 16 Mar 2023

Thank you for the feedback. I'll follow the two requests.
