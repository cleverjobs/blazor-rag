# Is it possible to use StockChartNavigator component outside of StockCharts?

## Question

**Fab** asked on 14 Dec 2021

As per subject, we need to use the StockChartNavigator but we don't want to use StockChart. We basically just want to have that kind of component to be able to select a range between dates. We could even fit it with a simple data serie if it's needed, but we don't want to use it within a stock chart Is it possible? An alternative is the RangeSlider but we'd prefer the graphical aspect of the StockChartNavigat and in case use it binding its range to display non-stock charts Thanks

## Answer

**Nadezhda Tacheva** answered on 17 Dec 2021

Hello Fabiо, Once the range selection is implemented in the chart, you can use it as custom navigator (to filter the data by the selected date range) and you can display it in another pane or chart. An example of such custom implementation you may check in the Angular version of the Chart - Using Selection as Navigator. Having this in mind, I added a vote on your behalf to the range selection feature request to increase its popularity as we are prioritizing the feature requests implementation based on the community interest and demand. The best way to keep in track with its progress is to follow it, so you will receive email notifications when its status changes. I hope you will find the above information useful. Please let us know if any further questions appear. Regards, Nadezhda Tacheva

### Response

**Fabio** commented on 17 Dec 2021

Hello Nadezhda To be frank, what we'd need the most is to have a 1st class citizen control like "TimeSerie Range Selection" that we can use where we like, not specifically bound to charts. This would allow us to bind range to contextual information that could be grid, a list, whatever. So that kind of control should have bindable properties/events to capture the range change. By the way, the implementation like in the demo [https://demos.telerik.com/aspnet-core/chart-api/selection](https://demos.telerik.com/aspnet-core/chart-api/selection) could fit the need if the range events are exposed. If it's ok to mention a competitor implementation, we'd need something like this [https://www.syncfusion.com/blazor-components/blazor-range-selector](https://www.syncfusion.com/blazor-components/blazor-range-selector) P.S. When we bought licenses, we were told that component source control would be available on November. Are they realased? We could create our own custom control that way extending your controls while you ship the new control, because we cannot afford to lose much time. Should I fill a ticket about this? Thanks

### Response

**Nadezhda Tacheva** commented on 22 Dec 2021

Hi Fabio, Thank you for the follow up! I am glad to find out that a range selection would serve to cover your desired scenario for the Chart. However, it is still not available for the Blazor Chart. This is why we have the feature request opened for it - Chart range selection (your vote is already added there and you can follow it, so you are aware of its progress). The proposed custom implementation for using selection as navigator still targets the Chart component. As for range selection in other components, you can either create some custom UI to allow the user filter the component data by date range, or you can use some of the options we provide (for example DateRange Picker ) and incorporate it for such filtering purpose. In regards to the source code, it is indeed distributed as of version 2.29.0 which was released in November. You can get the source code zip from the Downloads section in your Telerik account. In case you need any assistance or you have some additional questions, you can of course submit a ticket and we can cover your concerns there.
