# How do I use a DropDown list for a TelerikForm item?

## Question

**Jef** asked on 16 Dec 2024

Hi, sorry if this is a basic question, but I cannot for the life of me figure out how to get this to work. I can have a DropDown list and a form separately, but when I try to put the DropDown into the form itself, I get a "Object of type 'Telerik.Blazor.Components.FormItem' does not have a property matching the name 'ChildContent'" error. Here's a sample snippet of what I'm trying to do: <TelerikForm Model="@Input" Columns="3" ColumnSpacing="50px" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit">
<FormValidation>
<DataAnnotationsValidator />
</FormValidation>
<FormItems>

<FormItem Field="@nameof(Model.Attribute)"></FormItem>
<FormItem Field="@nameof(Model.Attribute2)">
<TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="Model.Attribute3">
</TelerikDropDownList>
</FormItem>
<FormItem Field="@nameof(Model.Attribute4)"></FormItem>

</FormItems>
</TelerikForm> Sorry for the bad indentation, not sure how else to paste it properly.

## Answer

**Jeff** answered on 16 Dec 2024

Nevermind, sorry for the basic question. Seems like the solution is to use the <Template> tag before the DropDownList, like so: <FormItem Field="@nameof(Model.Attribute)">
<Template>
<TelerikDropDownList Data="@DropDownData" DefaultText="Select status" ValueField="MyValueField" @bind-Value="Input.Attribute">
</TelerikDropDownList>
</Template>
</FormItem>

### Response

**Hristian Stefanov** commented on 16 Dec 2024

Hi Jeff, I'm glad to hear that you have quickly resolved the matter on your own. Indeed, the <Template> tag is required so you can use the DropDownList inside the Form. Thank you for sharing how things turned out publicly so other developers in the same situation can benefit from this. Kind Regards, Hristian

### Response

**Joel** commented on 27 May 2025

Can you explain how the binding works in this scenario? Does the bind-Value always start with "Input."? Does the Attribute point to the same name as the FormItem Field=value?

### Response

**Hristian Stefanov** commented on 28 May 2025

Hi Joel, Here is our documentation regarding templates in the form items, including a fully runnable example you can use as a reference: [https://www.telerik.com/blazor-ui/documentation/components/form/formitems/template](https://www.telerik.com/blazor-ui/documentation/components/form/formitems/template) Let me know if you still need some more information. Kind Regards, Hris
