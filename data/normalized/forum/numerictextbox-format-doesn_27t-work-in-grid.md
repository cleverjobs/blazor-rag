# NumericTextbox Format doesn't work in grid

## Question

**Mir** asked on 23 Sep 2020

Hi, I need to display % in my column, but Format="#,## %" doesn't work. What do I have to change? Thanks for your help! Greetings <GridColumn Field="Menge" Title="Menge" Width="100px"> 02. <EditorTemplate> 03. @{ 04. Current=context as Item; 05. if (Current?.Typ !=Typ.H) 06. { 07. <TelerikNumericTextBox T="decimal?" @bind-Value="@Current.Menge" OnChange="@ChangeMengenHandler" Decimals="3" Format="#,## %"> 09. </TelerikNumericTextBox> 10. } 11. } 12. </EditorTemplate> 13. </GridColumn>

## Answer

**Marin Bratanov** answered on 23 Sep 2020

Hi Miriam, The Format affects the display of the numeric textbox when it is not focused. When it is focused, it must only show the number. This is the behavior I get and I am attaching at the end of this post a short video of what I see so you can compare against it, and the snippet I used for testing is below. Am I missing something? By the way, perhaps you are looking for a Masked Input - you can see here and if that's what you need, you can click the Follow button on that page to get email updates. Depending on what you are after and what values you seek, this KnowledgeBase article may also be of interest: Percentage Format Range in the TelerikNumericTextBox <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="300px" OnUpdate="@UpdateHandler">
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="ID" />
<GridColumn Field=@nameof(SampleData.Name) Title="Name" />
<GridColumn Field=@nameof(SampleData.Discount) Title="Discount">
<EditorTemplate>
@{
CurrentlyEditedItem=context as SampleData;
<div style="border: 1px solid black">
@CurrentlyEditedItem.Discount?.ToString( "#,## %" )
</div>
<TelerikNumericTextBox @bind-Value="@CurrentlyEditedItem.Discount" OnChange="@ChangeMengenHandler" Decimals="3" Format="#,## %">
</TelerikNumericTextBox>
}
</EditorTemplate>
</GridColumn>
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { public SampleData CurrentlyEditedItem { get; set; } void ChangeMengenHandler ( object newVal ) {

} public void UpdateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; //perform actual data source operations here //if you have a context added through an @inject statement, you could call its SaveChanges() method //myContext.SaveChanges(); var index=MyData.FindIndex(i=> i.ID==item.ID); if (index !=-1 )
{
MyData[index]=item;
}
} protected override void OnInitialized ( ) {
MyData=new List<SampleData>(); for ( int i=0; i <50; i++)
{
MyData.Add( new SampleData()
{
ID=i,
Name="name " + i,
Discount=i * 1000 / 123 });
}
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public decimal? Discount { get; set; }
} public List<SampleData> MyData { get; set; }
} Regards, Marin Bratanov

### Response

**Miriam** answered on 24 Sep 2020

Hi, thank you for the video! The problem is that I need the result to be displayed in this format. When I am not in edit mode. When I use a usual <Template> then it's working with the same div-tag that you are using, but not in <EditorTemplate>. Is that somehow possible with the NumericTextBox? Best regards

### Response

**Marin Bratanov** answered on 24 Sep 2020

Hi Miriam, For formatting the value in display mode you may also want to check the new DisplayFormat parameter that's coming to the columns in our next release ( link ). For displaying a value in the editor template, an approach like the div element I added in my previous sample is the way to go, though. As for the editor itself - the Format parameter of the numeric textbox is in effect when it does not have focus. When it is focused, it will show only the number with the designated number of Decimals. Here's also a comparison between the behavior of a numeric textbox and a masked input: [http://dojo.telerik.com/iRuZAbET](http://dojo.telerik.com/iRuZAbET) Could you explain what exactly you are expecting the numeric textbox to do that it does not do already and that isn't in the realm of a masked input? Regards, Marin Bratanov

### Response

**Miriam** answered on 25 Sep 2020

Hi, I want the value to be displayed like this: e.g. 1,88 %. After the cell loses focus. "For displaying a value in the editor template, an approach like the div element I added in my previous sample is the way to go, though." Unfortunately that is definitiely not working because it is not possible to add a div-Tag in between the NumericTextbox-Tags. I always get the Exception that the Textbox doesn't support a Childelement. DisplayFormat sounds interesting, though. When will ist be released?

### Response

**Marin Bratanov** answered on 25 Sep 2020

Hi Miriam, You can use the Template to achieve that. The numeric textbox cannot, will not and should not allow a renderfragment between its tags - it is a simple input and has only one content - its Value, just like an <input type=text>. You either need a template, or a masked textbox, I still am not sure which. The DisplayFormat feature is scheduled for our next release - 2.18.0, which is planned for the end of October. Note that it will not affect the edit mode of the cell at all, it is a replacement of the template code below for the display value. <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="300px" OnUpdate="@UpdateHandler">
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="ID" />
<GridColumn Field=@nameof(SampleData.Name) Title="Name" />
<GridColumn Field=@nameof(SampleData.Discount) Title="Discount"> <Template> @( (context as SampleData).Discount?.ToString( "#,## %" ) ) <div>Real value: @( (context as SampleData).Discount )</div> </Template> <EditorTemplate>
@{
CurrentlyEditedItem=context as SampleData;
<TelerikNumericTextBox @bind-Value="@CurrentlyEditedItem.Discount" OnChange="@ChangeMengenHandler" Decimals="3" Format="#,## %">
</TelerikNumericTextBox>
}
</EditorTemplate>
</GridColumn>
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { public SampleData CurrentlyEditedItem { get; set; } void ChangeMengenHandler ( object newVal ) {

} public void UpdateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; //perform actual data source operations here //if you have a context added through an @inject statement, you could call its SaveChanges() method //myContext.SaveChanges(); var index=MyData.FindIndex(i=> i.ID==item.ID); if (index !=-1 )
{
MyData[index]=item;
}
} protected override void OnInitialized ( ) {
MyData=new List<SampleData>(); for ( int i=0; i <50; i++)
{
MyData.Add( new SampleData()
{
ID=i,
Name="name " + i,
Discount=i * 1000 / 12345.67 m
});
}
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public decimal? Discount { get; set; }
} public List<SampleData> MyData { get; set; }
} Regards, Marin Bratanov

### Response

**Miriam** answered on 28 Sep 2020

Thank you very much! Using both templates was the solution but we will change our code as soon as your new release is available. Greetings 01. <Template> 02. @( (context as SampleData).Discount?.ToString( "#,## %" ) ) 03. <div>Real value: @( (context as SampleData).Discount )</div> 04. </Template> 05. <EditorTemplate> 06. @{ 07. CurrentlyEditedItem=context as SampleData; 08. <TelerikNumericTextBox @bind-Value="@CurrentlyEditedItem.Discount" OnChange="@ChangeMengenHandler" Decimals="3" Format="#,## %"> 09. </TelerikNumericTextBox> 10. } 11. </EditorTemplate>
