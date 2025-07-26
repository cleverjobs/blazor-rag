# Telerik DatePicker Translates SOME Dates Incorrectly

## Question

**bil** asked on 31 Jan 2022

I have some dates that are being translated into a different date in my C# from what is in the Component. I have the below component (I've tried multiple different formats) <TelerikDatePicker @bind-Value="@this.MyModel.DateOfService" Label="Date of Service" /> When entering the below dates, I get the following outputs. Entered Date 1=11/15/2021 Date 1 Output in C#=1/15/2021 {1/15/2021 12: 11:00 AM} <- Notice the 11 is in the Minutes slot ---------------------- Entered Date 2=05/05/1955 Date 2 Output in C#=1/5/1955 {1/5/1955 12:0 5:00 AM} <- Notice the 5 is in the Minutes slot I'm not performing any translation of the dates. The property is DateTime type and modeled directly to the property, yet it is not interpolating the dates correctly in these cases. Telerik.UI.for.Blazor V 2.27

### Response

**Hristian Stefanov** commented on 03 Feb 2022

Hi Billy, This sounds indeed like an actual issue. I tested the described scenario on my machine. As a result, the date outputs correctly on my end. I'm attaching the project I used for testing. If it's convenient, please modify the attached sample to show the problem and send it back to us. This will allow me to see the behavior first hand and suggest next steps. Thank you. I look forward to your reply.
