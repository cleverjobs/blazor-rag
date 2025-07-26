# Are there any options to customise ChartSeries visuals?

## Question

**Mar** asked on 18 Oct 2023

Hi Are there any options to customise ChartSeries visuals beyond colour? Our use-case involves charts rendered with series from multiple sources. We would like to differentiate the sources at a glance. We would prefer not to add more text-based labels. Things we have tried: ChartSeriesOverlay does not create much visual impact for our colour scheme. linear-gradient etc in the Colour parameter causes a black coloured series SVG patterns see REPL Thank you Mark

### Response

**Graig** commented on 19 Oct 2023

You can experiment with adjusting the transparency or opacity of the series. By making one series more transparent than the others, it creates a visual distinction without relying solely on color.

### Response

**Mark** commented on 26 Oct 2023

Thank you for the suggestion, Graig

## Answer

**Svetoslav Dimitrov** answered on 23 Oct 2023

Hello Mark, We have an open feature request for the Custom rendering for series element - visual template. I can see that you already have added your Vote for it and you can click the Follow button to receive email notifications on status updates. Once this feature is implemented you will be able to fully customize the series elements to match your business needs. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Mark** commented on 23 Oct 2023

Hi Svetoslav. Thank you for your answer. Yes, we are hoping that feature may eventually get planned in. But as it has been unplanned since 13 Nov 2019, we are looking for any currently available options we might have missed. Thanks again, Mark

### Response

**Svetoslav Dimitrov** commented on 26 Oct 2023

Hello Mark, I believe that, as Graig mentioned, the Opacity and Transparency might be the best solution until the Visual Template for the series elements is officially released. Regards, Svetoslav
