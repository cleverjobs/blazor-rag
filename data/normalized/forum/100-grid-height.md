# 100% Grid Height

## Question

**Ken** asked on 24 May 2019

How does the new 100% grid height work? Does it take the height of it's container? I removed the height styling from some of my pages, but the grid just keeps expanding and you have to use the browser scroll bar to access it. This is better than the fixed height, just trying to understand the new support. Thanks, Kenny

## Answer

**Marin Bratanov** answered on 24 May 2019

Hi Kenny, By default, the grid now has no height. This means that its element will expand to the height of the rows (which depends on the page size or total number of records). If you set Height="100%" this is the style attribute that will be rendered on the wrapping element, so it will take its parent height. You can read more about this in the following article: [https://docs.telerik.com/blazor-ui/common-features/dimensions.](https://docs.telerik.com/blazor-ui/common-features/dimensions.) Here is also an example, and at the end of the post is a screenshot that illustrates how this looks: @using Telerik.Blazor.Components.Grid <div style=" height: 300px; border: 1px solid red; "> <TelerikGrid Data="@MyData" Height="100%" Pageable="true"> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(SampleData.ID))"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> </TelerikGridColumn> </TelerikGridColumns> </TelerikGrid> </div> @functions { //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; } } public IEnumerable<SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData { ID=x, Name="name " + x, HireDate=DateTime.Now.AddDays(-x) }); } Regards, Marin Bratanov

### Response

**Alexandre** answered on 09 Jul 2019

Hi Marin! TelerikGrid expects decimal value, your example is invalid on the current version. Any workaround?

### Response

**Marin Bratanov** answered on 10 Jul 2019

Hello Alexandre, The dimensions properties are strings so you can put valid CSS values in them: [https://docs.telerik.com/blazor-ui/common-features/dimensions.](https://docs.telerik.com/blazor-ui/common-features/dimensions.) This has been the case in the last few versions and if your version expects a number only, then it is using an older version, perhaps up to 1.0.0, because we changed it to string after that. The current latest is 1.3.0 at the time of writing and I advise that you upgrade to it. Regards, Marin Bratanov
