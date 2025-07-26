# Cannot convert from source type RenderFragment<object> to target type RenderFragment

## Question

**Ste** asked on 01 Dec 2021

Hi, I used the following solution: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template](https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template) for easier reusability in a grid. I want to do the same for the TelerikForm. However, the Template property of FormItem is of type RenderFragment instead of RenderFragment<object>. Because of this, I'm getting an error (see title). I cannot change the return type of the function to RenderFragment either, because then I get the following error on the line that says "return ColumnTemplate": Expected a method with 'void FormTemplate(RenderTreeBuilder)' signature. Is there any way to resolve this?

## Answer

**Svetoslav Dimitrov** answered on 06 Dec 2021

Hello Stefan, I`d like to provide a working example on how to add a template for the FormItem in a similar way to in the dynamic column template KB. After the code snippet, I would provide some additional information on the RenderFragment vs RenderFragment<object> difference. Firstly, as promised the code snippet (and a runnable REPL link ): @using System.ComponentModel.DataAnnotations

<TelerikForm EditContext="@EditContext">
<FormValidation>
<DataAnnotationsValidator></DataAnnotationsValidator>
<ValidationSummary />
</FormValidation>
<FormItems>

<FormItem Template="@GetFormTemplate()"></FormItem>

<FormItem>
<Template>
<label for="country">Destination country:</label>
<TelerikDropDownList @bind-Value="@MyModel.Country" DefaultText="Choose a country" Data="@DropDownData" PopupHeight="" Id="country">
</TelerikDropDownList>
</Template>
</FormItem>
<FormItem>
<Template>
<label for="city">Destination city:</label>
<TelerikComboBox @bind-Value="@MyModel.City" Data="@CityData" PopupHeight="" Id="city">
</TelerikComboBox>
</Template>
</FormItem>

</FormItems>
</TelerikForm>

@code { public TemplateModel MyModel { get; set; }=new TemplateModel(); public EditContext EditContext { get; set; } public RenderFragment GetFormTemplate ( ) {
RenderFragment FormItemEmailTemplate=__builder=>
{
<label for="email-editor">Email:</label>
<TelerikTextBox InputMode="email" Id="email-editor" @bind-Value="@MyModel.Email"></TelerikTextBox>
}; return FormItemEmailTemplate;
} public List <string> DropDownData { get; }=new List<string>()
{ "Bulgaria", "Italy", "Greece" }; public List<string> CityData
{ get { switch (MyModel.Country)
{ case "Bulgaria": return new List<string>() { "Sofia", "Plovdiv", "Varna", "Burgas" }; case "Italy": return new List<string>() { "Rome", "Milan", "Naples", "Turin" }; case "Greece": return new List<string>() { "Athens", "Thessaloniki", "Patras", "Piraeos" }; default: return new List<string>(); break;
}
}
} protected override void OnInitialized ( ) {
EditContext=new EditContext(MyModel); base.OnInitialized();
} public class TemplateModel { public TemplateModel ( ) {

}

[ Required ] public string Email { get; set; }

[ Required ] public string Country { get; set; }

[ Required ] public string City { get; set; }

[ Range(typeof(bool), "true", "true", ErrorMessage="You must confirm first time." ) ] public bool FirstTime { get; set; }
} private void Clear ( ) {
MyModel=new TemplateModel();

EditContext=new EditContext(MyModel);

EditContext.AddDataAnnotationsValidation();
}
} Now, the difference between the ColumnTemplate (<Template>) and the FormItem Template is that the ColumnTemplate provides a context object, thus the RenderFragment<object> (the object is the passed context). Compared to that the FormItem Template does not provide a context object and thus the type is a RenderFragment. This major difference is the reason why there would be no way to create the same dynamic column template for both the Form and the Grid Column (even if we refer to the EditorTemplate). That being said, I will take some time to try to implement a reusable dynamic template for both the Grid Column (editor template) and the FormItem as I can see there is some benefit in reusing the same code across both components. Once I have some additional details, I will get back to you. I hope this helps you understand the scenario better. If any other questions arise, do not hesitate to get in touch with me again. Regards, Svetoslav Dimitrov
