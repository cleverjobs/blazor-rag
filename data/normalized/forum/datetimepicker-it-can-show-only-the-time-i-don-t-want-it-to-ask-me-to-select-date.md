# DateTimePicker it can show only the time, I don't want it to ask me to select date

## Question

**Adh** asked on 09 Jul 2021

DateTimePicker it can show only the time, I don't want it to ask me to select date tanks

## Answer

**Adhemar Franklin** answered on 09 Jul 2021

TimePicker ups

### Response

**Marin Bratanov** answered on 09 Jul 2021

Hi, The TimePicker does not require a date portion: [https://demos.telerik.com/blazor-ui/timepicker/overview](https://demos.telerik.com/blazor-ui/timepicker/overview) The DateTimePicker does, and it must: [https://demos.telerik.com/blazor-ui/datetimepicker/overview](https://demos.telerik.com/blazor-ui/datetimepicker/overview) If you want to switch between them depending on business logic, you can wrap them in an if-else block. Regards, Marin Bratanov
