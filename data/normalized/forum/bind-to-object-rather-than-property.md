# Bind to object rather than property

## Question

**Mat** asked on 05 Aug 2021

My question specifically relates to the use of Radio Group, but could apply to other controls as well. Where the documentation talks about value binding vs data binding, this is in relation to the source data (i.e. the collection of options a user can choose from), and not the selected value. Taking the following example: <TelerikRadioGroup @bind-Value=@selectedValue Data=@sourceList TextField="ATextProperty" ValueField="AnIntProperty"> </TelerikRadioGroup> In this case in my code I can have my selectedValue be an int (to match the value field). But lets say, following the example from the documentation, I want to bind the selected object, not a property of the object, like this: <TelerikRadioGroup @bind-Value=@selectedValue Data=@sourceList TextField="GenderText" TValue="GenderModel"> </TelerikRadioGroup> Is there a way to do something like this? I haven't been able to get it work. I have tried using ValueChanged as well, this way: <TelerikRadioGroup @selectedValue Data=@sourceList TextField="ATextProperty" ValueChanged="@((v)=> OnValueChanged(v))"> </TelerikRadioGroup> And this way: <TelerikRadioGroup @selectedValue Data=@sourceList TextField="ATextProperty" ValueChanged="@((GenderModel v)=> OnValueChanged(v))"> </TelerikRadioGroup> But the value passed in to OnValueChanged is always null.

## Answer

**Marin Bratanov** answered on 05 Aug 2021

Hello Matt, Said shortly, you can bind to objects, neither with our components, nor with standard inputs or the native Blazor components. There are many reasons for this and a more detailed account is available here: [https://www.telerik.com/forums/binding-dropdownlist-value-to-complex-model.](https://www.telerik.com/forums/binding-dropdownlist-value-to-complex-model.) That said, the solution is to use a lookup based on the unique identifier (say, int, guid, enum) you get out of the input (radio button, dropdown, combo box,...), here is a sample with the general approach [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model.](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model.) Regards, Marin Bratanov Progress Telerik
