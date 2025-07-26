# DropDownList TextField concatenate

## Question

**Vis** asked on 25 Oct 2020

Hi, I am not able to concatenate value in TextField for selected value eg: (Code+ '-' +Name) <TelerikDropDownList DefaultText="NONE" Data="@categotyTypes" @bind-Value="@Model.Code" TextField="@nameof(CategoryTypes.Name)" ValueField="@nameof(CategoryTypes.Code)" Id="CategoryCode" Width="100%"> <ItemTemplate Context="dlContext"> @($"{dlContext.Code} - {dlContext.Name}") </ItemTemplate> </TelerikDropDownList> Could you please help on this.

## Answer

**Marin Bratanov** answered on 25 Oct 2020

Hi Vishnu, Here's an example based on the documentation: [https://docs.telerik.com/blazor-ui/components/dropdownlist/templates#item-template](https://docs.telerik.com/blazor-ui/components/dropdownlist/templates#item-template) <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" Value="1">
<ItemTemplate>
@{
MyDdlModel currItem=context as MyDdlModel; string textToRender=$" {currItem.MyTextField} - {currItem.ExtraField} ";
@textToRender
}
</ItemTemplate>
</TelerikDropDownList>

@code { public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; } public string ExtraField { get; set; }
}

IEnumerable<MyDdlModel> myDdlData=Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel
{
MyTextField="item " + x,
MyValueField=x,
ExtraField="more item info " + x
}
);
} Regards, Marin Bratanov
