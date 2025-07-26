# AutoFitAllColumnsAsync works only from the second time on

## Question

**NiV** asked on 18 Aug 2023

Good morning. In my code I've seen that AutoFitAllColumnsAsync works only from the second time on. I'm asking you if I'm missing something or doing something wrong. Follows 2 repl link: in the first one when you click on the upper button to load data, the data are loaded and then AutoFitAllColumnsAsync is called twice and works: [https://blazorrepl.telerik.com/GxkiFivl46gBfE8o57](https://blazorrepl.telerik.com/GxkiFivl46gBfE8o57) in the second one when you click on the upper button to load data, the data are loaded and then AutoFitAllColumnsAsync is called only once and doesn't work: [https://blazorrepl.telerik.com/wdEsbsPF50K99GvR04](https://blazorrepl.telerik.com/wdEsbsPF50K99GvR04) Please note that in the second example if you click again on the load data button the AutoFitAllColumnsAsync is correctly applied (in other words, in my examples AutoFitAllColumnsAsync works only from the second time on). Please let me know if I have to change something in code. Thank you.

## Answer

**Dimo** answered on 21 Aug 2023

Hi Fabio, Auto-fitting Grid columns on initial load is tricky and not officially supported. The documentation provides a workaround that requires JavaScript. However, in your case you can use a Task.Delay(), which is a simpler option. private async Task LoadDataAndAutoFitColumns ( ) {
GridData=GetData(); await Task.Delay( 100 ); await GridRef.AutoFitAllColumnsAsync();
} Regards, Dimo Progress Telerik
