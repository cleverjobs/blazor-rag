# MultiSelect DropDown with checkboxes

## Question

**Art** asked on 06 Aug 2020

Hi, I need a MultiSelect DropDownList with checkboxes. I was not able to find this control on the demo page. Thanks, Artem

## Answer

**Marin Bratanov** answered on 06 Aug 2020

Hi Artem, This article shows how to do it: [https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-checkbox-in-dropdown](https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-checkbox-in-dropdown) Regards, Marin Bratanov

### Response

**Aartheeswaran** answered on 22 Dec 2020

Hi Artem, I have implemented this but got error in "AutoClose" property doesn't exist. I have using 2.17.0 version of blazor.

### Response

**Marin Bratanov** answered on 22 Dec 2020

Hi Aartheeswaran, That feature was added in 2.18.0, I recommend you upgrade to the latest to also get a ton of other new features and fixes. Regards, Marin Bratanov

### Response

**SaiSivaSankar** answered on 07 Jan 2021

Hi Team, I added "TelerikMultiSelect" but got this error "The type arguments for method 'TypeInference.CreateTelerikMultiSelect_2". Version: 2.18.0

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hi, An error starting like this indicates a mismatch between some of the types provided to the component. For example, the type of the Value collection is different than the type of the ValueField in the Data models. Or, data/Value is missing (see here ). If this information and article don't help you fix this, please post the full error and a simple runnable snippet that shows how to reproduce it. Regards, Marin Bratanov

### Response

**SaiSivaSankar** answered on 07 Jan 2021

Thank you Marin Bratanov, If i replace List<string> TheValues { get; set; } to IEnumerable<string> TheValues { get; set; }, am getting this error. <TelerikMultiSelect Data="@Options" @bind-Value="@TheValues" TextField="StringRepresentation" ValueField="MyValueField"> <ItemTemplate> <input type="checkbox" id="@( (context as OptionsModel).MyValueField )" class="k-checkbox"> <label class="k-checkbox-label" for="@( (context as OptionsModel).MyValueField)">@context.StringRepresentation</label> </ItemTemplate> </TelerikMultiSelect> IEnumerable<string> TheValues { get; set; } List<OptionsModel> Options { get; set; }=new List<OptionsModel> { new OptionsModel { StringRepresentation="first", MyValueField=1 }, new OptionsModel { StringRepresentation="second", MyValueField=2 }, new OptionsModel { StringRepresentation="third", MyValueField=3 } }; public class OptionsModel { public string StringRepresentation { get; set; } public int MyValueField { get; set; } } Thank you

### Response

**Ramesh** commented on 14 Dec 2023

I have implemented further based on my requirement <TelerikMultiSelect Data="@Options" @bind-Value="@TheValues" TextField="StringRepresentation" ValueField="MyValueField" Context="OptionsModel"> <ItemTemplate> <input type="checkbox" id="@( (context as OptionsModel).MyValueField )" class="k-checkbox k-checkbox-md" checked="@GetChecked(context)"> <label class="k-checkbox-label" for="@((context as OptionsModel).MyValueField)">@context.StringRepresentation</label> </ItemTemplate> </TelerikMultiSelect> List<string> TheValues { get; set; } List<OptionsModel> Options { get; set; }=new List<OptionsModel> { new OptionsModel { StringRepresentation="first", MyValueField=1 }, new OptionsModel { StringRepresentation="second", MyValueField=2 }, new OptionsModel { StringRepresentation="third", MyValueField=3 } }; bool GetChecked(OptionsModel value) { if (TheValues.Any()) { return TheValues!.Contains(value.StringRepresentation); } return false; } public class OptionsModel { public string StringRepresentation { get; set; } public int MyValueField { get; set; } } Thanks & Regards Ramesh Vaduka Sr. DotNet Developer, Team Vertex

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hello, The Value must be a List<TValue> - it is specifically a List, not just IEnumerable. This is stated in the docs and is available in the intellisense (screenshots attached). Regards, Marin Bratanov

### Response

**Stefano** answered on 02 Aug 2022

Hello, I tried this solution but for my needs the result is too far from a real checked combobox (like I can see in your ASP.NET library ). Did you add anything like that in the Blazor library? Thank you.

### Response

**Dimo** commented on 05 Aug 2022

Hi Stefano - for the time being, we have a feature request for built-in checkboxes in the MultiSelect dropdown. I added one vote on your behalf to bump the popularity.
