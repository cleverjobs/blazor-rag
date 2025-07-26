# Chart gets cut off when printing

## Question

**Hei** asked on 22 Mar 2022

I use blazor chart component and it works quite fine. The problem starts when printing the current html page (CTRL+P) then the chart gets cut off on the right side and does not scale correctly. As you can see in my screenshot the table above the chart is scaled ok but the chart is cut off. What can I do to print the chart in a correct way? Regards Heiko

### Response

**Hristian Stefanov** commented on 25 Mar 2022

Hi Heiko, Most likely, the described result comes due to the size difference between the printed page and the web browser. In such a case, the Chart needs to redraw first with the new dimensions. Calling StateHasChanged() while printing should re-render the component. If this does not help, you can also call the Chart's Refresh() method (perhaps after a small timeout like Task.Delay(20)). Additionally, we have runnable examples for Responsive Chart and Printing Chart: Responsive Chart KB example Printing Chart KB example Use the code from both as a reference, and exclude what is not needed in the actual project. I hope this guides you in the direction of fixing the problem. Please keep me updated on the situation. Thank you.
