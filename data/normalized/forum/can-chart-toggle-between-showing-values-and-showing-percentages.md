# Can Chart toggle between showing values and showing percentages?

## Question

**Adr** asked on 28 Sep 2021

Hi, I have a WPF app that uses Telerik controls and Telerik charting. This WPF app is now being re-written using Blazor WebAssembly using Telerik Blazor controls and Telerik Blazor charting. Some of the existing WPF charts have custom context menus that allow users to toggle between displaying the charts with values or displaying the values as percentages. It seems that the WPF RadChart control supports different format expressions: [https://docs.telerik.com/devtools/wpf/controls/radchart/features/format-expressions](https://docs.telerik.com/devtools/wpf/controls/radchart/features/format-expressions) The toggling is achieved by changing the series item label formats e.g. Private Sub PercentagesContextItem_Checked(sender As System. Object, e As System.Windows.RoutedEventArgs) For Each objMapping In RadChart1.SeriesMappings
objMapping.SeriesDefinition.ItemLabelFormat="#STPERCENT{P0}" Next End Sub Private Sub PercentagesContextItem_Unchecked(sender As System. Object, e As System.Windows.RoutedEventArgs) Dim strCurrencyMajorSymbol As String=WebContext.Current.User.CurrencyMajorSymbol For Each objMapping In RadChart1.SeriesMappings
objMapping.SeriesDefinition.ItemLabelFormat=strCurrencyMajorSymbol & "#DATAITEM.ValueY{###,###,##0.00}" Next End Sub Is it possible to achieve this in Blazor WebAssembly using the Telerik Blazor charting controls and if so, how?

## Answer

**Marin Bratanov** answered on 28 Sep 2021

Hello Adrian, The Blazor charts also have templates and formats that you can change: [https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format](https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format) If changing them does not re-redner the chart, you can also call its .Refresh() method (you can find a sample of using it here ). Regards, Marin Bratanov Progress Telerik
