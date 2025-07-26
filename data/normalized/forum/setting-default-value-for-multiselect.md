# Setting default value for MultiSelect

## Question

**kha** asked on 06 Feb 2020

Hello, i was wondering if currently there is a way to set some default values as selected in MultiSelect

## Answer

**Marin Bratanov** answered on 06 Feb 2020

Hi, Here is an example in the documentation: [https://docs.telerik.com/blazor-ui/components/multiselect/overview#examples.](https://docs.telerik.com/blazor-ui/components/multiselect/overview#examples.) The component supports Value bindings so you can provide an initial (default) value through it. Regards, Marin Bratanov

### Response

**khashayar** answered on 06 Feb 2020

yes but the take a look at this code <TelerikMultiSelect Data="@MyData" @bind-Value="@Values" Placeholder="Enter" TextField="Name" ValueField="Id" Width="350px" ClearButton="true" /> @if (Values.Count> 0) { <ul> @foreach (var item in Values) { <li>@item</li> } </ul> } @code { List<SomeItem> Values { get; set; }=new List<SomeItem>() { }; public IEnumerable<SomeItem> MyData=Enumerable.Range(1, 50).Select(x=> new SomeItem { Id=x, Name="name " + x }); protected override void OnInitialized() { Values.Add(new SomeItem { Id=2, Name="name 2" }) ; Values.Add(new SomeItem { Id=3, Name="name 3" }) ; base.OnInitialized(); } public class SomeItem { public int Id { get; set; } public string Name { get; set; } } } i want the returned value be of type SomeItem not just string in this case it doesnt work well

### Response

**Marin Bratanov** answered on 06 Feb 2020

Hello khashayar, I made the following article that explains why that is so and how to approach the situation: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) Regards, Marin Bratanov
