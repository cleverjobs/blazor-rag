# How do I set the size and color of a specific clicked point on a scatter chart

## Question

**Cha** asked on 26 Mar 2024

I have a ChartSeries and I set the ChartMarkerType. I want to be able to click on the point in the chart and change that single point's size and color. For example, if all the points on the ChartSeries and color:red/size:10, I want to change that point to color:green/size15. The rest of the points stay color:red/size:10

### Response

**Hristian Stefanov** commented on 29 Mar 2024

Hello Chance, I have noticed that my colleague Svetoslav has already answered this question in your other private ticket. I'm pasting here the answer he gave you so the forum community can benefit from it.======The markers are part of a series - in one Chart series, normally, you would have multiple markers. To change the color, the size, or any other customization setting, two open feature requests need to be developed: An event that fires when the user clicks on a Marker - I have opened this on your behalf and your Vote is already in. Visuals for the Series elements - I have added your Vote for this request as well.======Kind Regards, Hristian
