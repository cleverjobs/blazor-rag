# TelerikDatePicker in blazor

## Question

**kha** asked on 05 Dec 2019

Hi, i want to bind a DateTimeOffset typed property to TelerikDatePicker is there any way to convert type in bind event ? i just want to pick date if i bind it to TelerikDateTimePicker it would work but i dont want to select time

## Answer

**Marin Bratanov** answered on 05 Dec 2019

Hi, If you want date selection only, you need to use the DatePicker component: [https://demos.telerik.com/blazor-ui/datepicker/overview](https://demos.telerik.com/blazor-ui/datepicker/overview) If you want time selection only, the TimePicker component will serve: [https://demos.telerik.com/blazor-ui/timepicker/overview](https://demos.telerik.com/blazor-ui/timepicker/overview) The DateTimePicker offers both: [https://demos.telerik.com/blazor-ui/datetimepicker/overview](https://demos.telerik.com/blazor-ui/datetimepicker/overview) The idea of having three separate components is so that you can get the user experience you want. All of them require a DateTime object in the view model, however, and you can use its setter to extract the needed information to populate your TimeSpan field. Alternatively, instead of two-way binding, you can use the events the components expose (ValueChanged and/or OnChange, see here, here and here ) and do the same in the event handler. Regards, Marin Bratanov

### Response

**khashayar** answered on 05 Dec 2019

i found this code @result<br /> <TelerikDatePicker ValueChanged="@( (DateTime d)=> MyValueChangeHandler(d) )"></TelerikDatePicker> @code { string result; private void MyValueChangeHandler(DateTime theUserInput){ result=string.Format("The user entered: {0}", theUserInput); } } helpfull but whe i run it i get an error System.InvalidOperationException: Telerik.Blazor.Components.TelerikDatePicker`1[System.DateTime] requires a value for the 'ValueExpression' ValueExpression is provided automatically when using 'bind-Value'.

### Response

**Marin Bratanov** answered on 05 Dec 2019

Hello khashayar, I just tested this example and it does not throw errors for me. Can you confirm you have .NET Core 3.1 RTM installed and that you have updated your Telerik UI for Blazor reference to 2.5.0? If doing so does not help, please open a support ticket and send me a project where I can observe this error. Of course, you can also provide a Value to the component like in the second example in our docs, this can let you define a default value so the user won'd start in January 0001, which would be rather inconvenient for them. Regards, Marin Bratanov

### Response

**khashayar** answered on 05 Dec 2019

my .Net version is 3.1.100-preview3-014645

### Response

**Marin Bratanov** answered on 05 Dec 2019

Hello Khashayar, Try upgrading to the .NET Core 3.1 RTM version and to Telerik UI for Blazor 2.5.0. Regards, Marin Bratanov

### Response

**Robert** answered on 05 Oct 2020

Hello! I'm on .NET Core 3.1.8 and Telerik Blazor 2.17 and I'm still running into the same issue with the following code: <TelerikDatePicker Value="@context.DateEffective.Date" ValueChanged="@((DateTime d)=> context.DateEffective=new DateTimeOffset(d))" Format="d" /> I'm editing a data inside a Grid, hence the use of @context. Am I missing something? Thanks!

### Response

**Marin Bratanov** answered on 06 Oct 2020

Hello Robert, The following article explains the "requires a value for valueexpression" error: [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression.](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression.) The .NET upgrade was useful in the previous case about a year ago when .NET Core 3.1 was still in Preview and that should not be the issue now. For the DatePicker in particular - it has not time portion and as such, a DateTimeOffset does not make sense for it, and it sets the time to 00:00, and the application code must take that into account if you want to use a DateTimeOffset. I added an example of this in the Notes section of the following KnowledgeBase article: [https://docs.telerik.com/blazor-ui/knowledge-base/date-input-picker-datetimeoffset.](https://docs.telerik.com/blazor-ui/knowledge-base/date-input-picker-datetimeoffset.) Regards, Marin Bratanov
