# TelerikComboBox setting Title

## Question

**TimTim** asked on 03 Feb 2023

I am trying to set the Title property on the TelerikComboBox component. This is then picked up by the Tooltip to display some custom help. I have tried using AdaptiveMode="@AdaptiveMode.Auto" as suggested in the docs., but when I tried inspecting the resulting html in the browser the title is not set on the input element. The ComboxBox itself is working fine. I do the same thing with TelerikTextBox and I can see the title is set in the browser and my custom help displays. This is my code: <TelerikComboBox Width="140px" Title="XYZ" AdaptiveMode="@AdaptiveMode.Auto" ClearButton="false" Data="@HelpFieldNames" Value="@HelpFieldName" ValueChanged="@( (string newValue)=> OnHelpFieldNameChanged(newValue) )" /> Is there some kind of trick required to get this to work? I am using Telerik.UiI.for.Blazor.Trial version 3.7.0 Thank you for any help

## Answer

**Tsvetomir** answered on 08 Feb 2023

Hi Tim, Thank you for the outlined information. Indeed, the title option of the combobox is used for the underlying action sheet used when the mode is set to adaptive. Currently, as per the documentation in MDN, it is not recommended to add a title attribute to input HTML elements. Namely, it states: "While the title can be used to provide a programmatically associated label for an <input> element, this is not good practice. Use a <label> instead." What I can recommend is that you make use of the Telerik UI Blazor Tooltip component instead. Find more information on how to initialize and configure it here: [https://docs.telerik.com/blazor-ui/components/tooltip/overview](https://docs.telerik.com/blazor-ui/components/tooltip/overview) I hope you find this helpful. Kind regards, Tsvetomir

### Response

**Tim** commented on 12 Feb 2023

Thanks for the reply. I have used the "data-" attribute to pass my help text to the component.
