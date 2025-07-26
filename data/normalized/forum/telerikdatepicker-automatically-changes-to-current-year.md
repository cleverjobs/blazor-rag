# TelerikDatePicker automatically changes to current year

## Question

**Geo** asked on 29 Nov 2023

I am trying to perform the following in a Blazor app. Default value=DateTime.Now. When a user enters a MMddyy or MMddyyyy I want to automatically format the date to MM/dd/yyyy. But I'm having an issue where the control automatically formats back to the default date value. Below is my layout for the DatePicker. I've tried different variations based on the demos Telerik provides but no luck. Hope someone can help. Thanks! <TelerikDatePicker Id="@CustomComponent.FieldLabel" @bind-Value="theInputValue" Enabled="CustomComponent.IsEnabled" Format="MM/dd/yyyy" OnChange="@OnValueChanged" OnBlur="@OnControlBlur"> </TelerikDatePicker>
