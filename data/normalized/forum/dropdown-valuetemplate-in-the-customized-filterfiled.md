# Dropdown ValueTemplate in the customized FilterFiled

## Question

**SuaSua** asked on 08 Jul 2024

Hi, I saw that this feature [https://feedback.telerik.com/blazor/1561874-filter-value-template](https://feedback.telerik.com/blazor/1561874-filter-value-template) is in status Completed and Release 2024 Q2 (May) . I did update the Telerik library but still the <ValueTemplate> is not recognized from visual studio. I saw the example with : @using Telerik.DataSource @using Telerik.DataSource.Extensions <TelerikFilter Value="@FilterValue" ValueChanged="@OnValueChanged"> <FilterFields> <FilterField Name="@(nameof(Food.Id))" Type="@(typeof(int))" Label="Id" /> <FilterField Name="@(nameof(Food.Name))" Type="@(typeof(string))" Label="Name"> <ValueTemplate> <TelerikAutoComplete Data="@Suggestions" Value="@((string)context.FilterDescriptor.Value)" ValueChanged="@((string value)=> OnFilterValueChanged(context.FilterDescriptor, value))"> </TelerikAutoComplete> </ValueTemplate> </FilterField> <FilterField Name="@(nameof(Food.Price))" Type="@(typeof(decimal))" Label="Price"> <ValueTemplate> <TelerikNumericTextBox Value="@((decimal?)context.FilterDescriptor.Value)" Format="C" Step="0.01m" ValueChanged="@( (decimal? value)=> NumericValueChanged(context.FilterDescriptor, value) )"> </TelerikNumericTextBox> </ValueTemplate> </FilterField> <FilterField Name="@(nameof(Food.IsAvailable))" Type="@(typeof(bool))" Label="Is Available" /> </FilterFields> </TelerikFilter> In my scenario I want to add a Dropdown as ValueTemplate. I have the Telerik.UI.for.Blazor version 6.0.2. Is the ValuteTemplate included in this version? Thanks in advance.

### Response

**Hristian Stefanov** commented on 11 Jul 2024

Hi Sua, I confirm that the ValueTemplate is already available. Here is an example within this REPL link for you to test it. The template seems to appear correctly when you select the "Name" field. Please run the REPL sample to see if you get the same result. Kind Regards, Hristian

### Response

**Sua** commented on 16 Jul 2024

Hi Hristian, I tried doing the same in visual studio but is complaining about the context The name 'context' does not exist in the current context.

### Response

**Hristian Stefanov** commented on 17 Jul 2024

Hi Sua, The error " The name 'context' does not exist in the current context " indicates a syntax issue. Could you confirm if you are testing with the exact same code configuration from the REPL link I provided in my last reply? Kind Regards, Hristian

### Response

**Sua** commented on 17 Jul 2024

yes confirm, copy paste in a complete new blazor component.

### Response

**Hristian Stefanov** commented on 18 Jul 2024

Hi Sua, I'm attaching a runnable project with the same configuration working (see " FilterValueTemplate-sample.zip "). Please test it and use it as a reference. Kind Regards, Hristian

### Response

**Sua** commented on 18 Jul 2024

Something very weird was happening, After I updated the Nuget to the version 6.0.2. In the .csproj the version 6.0.2. was tagged but in the Dependencies in the Packages when in run the version automatically changed to the version 5.1.1, It worked after uninstalling and installing from Nuget Telerik.UI.for.Blazor Version 6.0.2. Thanks a lot for the solution.
