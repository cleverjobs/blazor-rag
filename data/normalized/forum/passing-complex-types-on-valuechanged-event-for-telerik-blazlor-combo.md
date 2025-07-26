# Passing Complex Types on ValueChanged Event For Telerik Blazlor Combo.

## Question

**BL3** asked on 19 May 2022

ValueChanged Event for Complex Types are not firing. Code example as below @using Telerik.Blazor.Components;
<h1>Hello, Telerik REPL for Blazor! @selectedCodeBase.ItemName </h1>

<TelerikComboBox Data="@myComboData" TextField="ItemName" ValueField="ItemKey" TValue="MyDataModel" TItem="MyDataModel" ValueChanged="(MyDataModel s)=>sValueChanged(s)">
</TelerikComboBox>

@code { public class MyDataModel { public string ItemName { get; set;} public long ItemKey { get; set;}
}
IEnumerable<MyDataModel> myComboData=Enumerable.Range( 1, 20 )
.Select(x=> new MyDataModel { ItemName="item " + x, ItemKey=x }); private MyDataModel selectedCodeBase=new MyDataModel(); private async void sValueChanged ( MyDataModel s ) { await Task.CompletedTask;
}

} REPL Example [https://blazorrepl.telerik.com/cmuJFNan441IMFgm37](https://blazorrepl.telerik.com/cmuJFNan441IMFgm37) Please Help. Thank you

## Answer

**Marin Bratanov** answered on 22 May 2022

Hello, You can see the supported types of the Value parameter in the documentation: [https://docs.telerik.com/blazor-ui/components/combobox/overview#parameters](https://docs.telerik.com/blazor-ui/components/combobox/overview#parameters) You can also see how to bind the combo box to a complex type in the following article (key point - the ValueField must be of the primitive type that is supported by Value): [https://docs.telerik.com/blazor-ui/components/combobox/data-bind](https://docs.telerik.com/blazor-ui/components/combobox/data-bind) If you want to get the full model based on selection, you need to extract if from the data source based on the identifier you get in the Value (for more details, see the green note in the article above, this article has a direct example: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) ). Regards, Marin Bratanov Progress Telerik
