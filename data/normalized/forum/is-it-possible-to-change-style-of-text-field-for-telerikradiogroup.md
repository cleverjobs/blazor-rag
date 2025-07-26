# Is it possible to change style of text field for TelerikRadioGroup.

## Question

**AliAli** asked on 05 Oct 2023

I want to do something like this:

## Answer

**Hristian Stefanov** answered on 05 Oct 2023

Hi Ali, To change the style of the text field inside the TelerikRadioGroup, use the ItemTemplate exposed by the component. I have also prepared an example for you that demonstrates its usage: <TelerikRadioGroup Data="@RadioOptions" @bind-Value="@RadioValue" ValueField="@nameof(RadioModel.Id)" TextField="@nameof(RadioModel.Text)"> <ItemTemplate> @{
var item=context as RadioModel;
} <strong> @item.Text </strong> with <em style="color:red;"> @item.Description </em> </ItemTemplate> </TelerikRadioGroup> @code {
private List <RadioModel> RadioOptions { get; set; }

private int RadioValue { get; set; }

protected override void OnInitialized()
{
RadioOptions=new List <RadioModel> ();

for (int i=1; i <=3; i++)
{
RadioOptions.Add(new RadioModel()
{
Id=i,
Text=$"Radio option {i}",
Description=$"description {i}"
});
}

base.OnInitialized();
}

public class RadioModel
{
public int Id { get; set; }
public string Text { get; set; }
public string Description { get; set; }
}
} Please run and test the above code snippet to see whether the result covers your needs. Regards, Hristian Stefanov Progress Telerik

### Response

**Ali** commented on 05 Oct 2023

Yes, It does. Thank you very much.
