# DateTimePicker control in Military Time

## Question

**Jam** asked on 09 Feb 2022

Is it possible to have the Time Display in the DateTimePicker control in Military Time? For example, the user doesn't want to see AM/ PM. They would just rather see 1 to 23 (23 being 11PM)

## Answer

**Marin Bratanov** answered on 10 Feb 2022

Hello James, You can control the format of the time and date via the Format parameter of the component and with it you can select between 24h and 12h formats, here is one example (note the capital HH in the format- that denotes 24h format): [https://docs.telerik.com/blazor-ui/components/datetimepicker/overview.](https://docs.telerik.com/blazor-ui/components/datetimepicker/overview.) You can read more about these formats here: [https://docs.telerik.com/blazor-ui/components/dateinput/supported-formats](https://docs.telerik.com/blazor-ui/components/dateinput/supported-formats) Regards, Marin Bratanov
