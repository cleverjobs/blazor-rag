# Pie Chart Horizontal Align

## Question

**Deb** asked on 05 May 2021

Hello. I have added a pie chart to my initial page (attached code sample and output). The pie chart is skewed to the right side of the page rather than being centered. How can I center it? I've tried putting it in a row and column object but it just skews it right within those. Thanks, Debra

### Response

**Marin Bratanov** commented on 06 May 2021

Hi Debra, I can suggest you start by - making sure that the chart Width matches the layout - by default it centers in its own div, so the parent div size can be important - if it is too wide you could get such behavior - moving the legend to the bottom or top - the pie itself centers in the available space the legend leaves and so the left/right positions take up some space from the overall size left for the chart. You can even consider putting the info from the legent in tooltips or labels on the chart itself, and removing the legend altogether - setting RenderAs to Canvas for the chart to see if custom css rules from the project are interfering - removing all custom CSS from the project in case something from those rules is affecting the chart elements. If this does not help you move forward, I advise you open a support ticket and send us a simple runnable example we can investigate.

### Response

**Debra** commented on 06 May 2021

Thank you so much for your help, Marin. I moved the legend and set RenderAs to Canvas and that seems to have solved the issue. I hope my boss agrees:)

### Response

**Marin Bratanov** commented on 06 May 2021

So do I :)
