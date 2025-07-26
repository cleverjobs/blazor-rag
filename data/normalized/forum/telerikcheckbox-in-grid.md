# TelerikCheckBox in Grid

## Question

**Mau** asked on 16 Jun 2020

I have a checkbox of type TelerikCheckBox inside a column in my Grid using the code below. If I press the edit mode of the grid the checkbox can be altered but the type of the checkbox changes from class="k-checkbox telerik-blazor" to type input so the layout changes (see attachment) in my razor.cs file private ObservableCollection<ModelVM> GridData { get; set; } Inside my razor file I have this (simplified) <TelerikGrid Data="@GridData" OnEdit="@EditHandler" OnUpdate="@UpdateHandler"> <GridColumns> <GridColumn Field="isChecked" Title="Selected" Editable="true"> <Template> @{ var isChecked=context as ModelVM; <TelerikCheckBox Value="isChecked.isChecked" /> } </Template> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 16 Jun 2020

Hi Maurice, I made the following page where you can track the enhancement that the grid should use this by default, it also contains a workaround (adding the TelerikCheckBox in the column EditorTemplate): [https://feedback.telerik.com/blazor/1471974-telerikcheckbox-should-be-the-default-in-the-grid-for-editing-boolean-fields](https://feedback.telerik.com/blazor/1471974-telerikcheckbox-should-be-the-default-in-the-grid-for-editing-boolean-fields) Regards, Marin Bratanov

### Response

**Maurice** answered on 16 Jun 2020

I changed it to this and now it works Template and EditorTemplate <GridColumn Field="isChecked" Title="Selected" Editable="true"> <EditorTemplate> @{ var isChecked=context as ModelVM; <TelerikCheckBox Value="isChecked.isChecked" /> } </EditorTemplate> <Template> @{ var isChecked=context as ModelVM; <TelerikCheckBox Value="isChecked.isChecked" /> } </Template> </GridColumn>

### Response

**Fredrich Irian** commented on 24 Aug 2021

Hi, I did try the exact thing you did and I am still getting this error below:. "An unhandled exception has occurred. See browser dev tools for details. Reload " Codes that I have tried so far as below: <GridColumn Field="IsVip" Id="IsVip" Title="Is Vip" Width="120px">
<EditorTemplate>
@{
ProjectToEdit=context as ProjectData;
<TelerikCheckBox Value="ProjectToEdit.IsVip" />
}

</EditorTemplate>
<Template>
@{
ProjectToEdit=context as ProjectData;
<TelerikCheckBox Value="ProjectToEdit.IsVip" />
}
</Template>
</GridColumn> <GridColumn Field="IsVip" Id="IsVip" Title="Is Vip" Width="120px">
<EditorTemplate>
@{ var isChecked=context as ProjectData;
<TelerikCheckBox Value="isChecked.IsVip" />
}

</EditorTemplate>
<Template>
@{ var isChecked=context as ProjectData;
<TelerikCheckBox Value="isChecked.IsVip" />
}
</Template>
</GridColumn> Regards, Fredrich V.

### Response

**Marin Bratanov** answered on 16 Jun 2020

Hi Maurice, You may want to use @bind-Value in the editor template so the changes the user makes go to the model in the grid, so you can, in turn, transfer them to the database in the OnUpdate event. Regards, Marin Bratanov

### Response

**Meindert** commented on 03 Aug 2021

Hello, Can I bind to a ExpandoObject field like below try ? In this case an exception is raised of type unknown <EditorTemplate Context="ctx">
@{ bool b=( bool )((IDictionary<string, object>)ctx)[column.Sname];
<TelerikCheckBox @bind-Value="@(((IDictionary<string, object>)ctx)[column.Sname])" />
@*<input type="checkbox" id=@column.Sname @bind=@b />*@}
</EditorTemplate> kind regards, Meindert

### Response

**Marin Bratanov** commented on 03 Aug 2021

Expando objects are basically dictionaries, so you don't actually get a real field to bind an input to. See for example how even the OnUpdate event needs some work to extract and check data: [https://github.com/telerik/blazor-ui/blob/master/grid/binding-to-expando-object/BindingToExpandoObject/Pages/Index.razor#L62.](https://github.com/telerik/blazor-ui/blob/master/grid/binding-to-expando-object/BindingToExpandoObject/Pages/Index.razor#L62.) Once this works with a regular <input>, it should work with the Telerik one. Perhaps the easiest way would be to use a lambda in the ValueChanged handler, the caveat is building the ValueExpression that the framework requires.
