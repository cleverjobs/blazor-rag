# Format TimeSpan column in OnExcelBeforeExport

## Question

**Dea** asked on 09 Mar 2023

Hi, I have a grid with a nullable TimeSpan column. When exporting to Excel the format shows as 09:02:39. I'd like it just to be 09:02. In OnExcelBeforeExport I have args.Columns[3].NumberFormat=BuiltInNumberFormats.GetHourMinuteAMPM(); but it has no effect. Should it?

## Answer

**Nadezhda Tacheva** answered on 14 Mar 2023

Hi Dean, The GetHourMinuteAMPM() works with DateTime objects. It generates format with hours, minutes and AM/PM that indicates the specific part of the day. The TimeSpan is generally used to indicate duration or difference between DateTime objects. It represents a time period and not a specific time of the day. Thus, the GetHourMinuteAMPM() built-in format is not applicable to it. To achieve the desired result, I can suggest converting the TimeSpan values to DateTime prior to passing data to the Grid. Then, you can use the GetHourMinute() format. I hope you will find the above information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva
