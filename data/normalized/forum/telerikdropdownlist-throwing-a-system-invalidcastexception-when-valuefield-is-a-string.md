# TelerikDropDownList throwing a System.InvalidCastException when ValueField is a string

## Question

**AA** asked on 24 Feb 2020

I have just tested Telerik sample code from : [https://demos.telerik.com/blazor-ui/dropdownlist/overview](https://demos.telerik.com/blazor-ui/dropdownlist/overview) @page "/dropdownlist/overview" @page "/dropdownlist/index" @using TelerikBlazorDemos.Shared <div class="example-box-wrapper"> <div class="example"> <div class="mb-4">T-Shirt size:</div> <TelerikDropDownList Data="@Data" @bind-Value=@SelectedSizeMetric PopupHeight="" DefaultText="Select your T-shirt size" ValueField="SizeMetric" TextField="SizeText"> </TelerikDropDownList> </div> <div class="ml-4"> Selected Size Number: <strong>@SelectedSizeMetric</strong> </div> </div> @code { public IEnumerable<Size> Data { get; set; } public bool AllowCustom { get; set; }=true; public int? SelectedSizeMetric { get; set; } public string SelectedSize { get; set; } public class Size { public string SizeText { get; set; } public int? SizeMetric { get; set; } } protected override void OnInitialized() { List<Size> sizes=new List<Size>(); sizes.Add(new Size() { SizeText="X-Small", SizeMetric=3 }); sizes.Add(new Size() { SizeText="Small", SizeMetric=6 }); sizes.Add(new Size() { SizeText="Medium", SizeMetric=8 }); sizes.Add(new Size() { SizeText="Large", SizeMetric=10 }); sizes.Add(new Size() { SizeText="X-Large", SizeMetric=12 }); Data=sizes.AsQueryable(); base.OnInitialized(); } } It works fine as it is. But if I change: ValueField="SizeMetric" //int type for: ValueField="SizeText" //string type it nolonger works... I get: System.InvalidCastException : 'Unable to cast object of type 'System.String' to type 'System.Nullable`1[System.Int32]'.' The telerik doc ([https://docs.telerik.com/blazor-ui/components/dropdownlist/overview)](https://docs.telerik.com/blazor-ui/components/dropdownlist/overview)) specifies: The Value and ValueField can be of types: number (such as int, double and so on) string Guid Enum

## Answer

**Marin Bratanov** answered on 24 Feb 2020

Hello, The following works fine for me when I change both the Value and ValueField to be strings (I highlighted the changes): <div class="example-box-wrapper">
<div class="example">
<div class="mb-4">T-Shirt size:</div>
<TelerikDropDownList Data="@Data" @bind-Value=@SelectedSizeMetric
PopupHeight="" DefaultText="Select your T-shirt size" ValueField="SizeMetric" TextField="SizeText">
</TelerikDropDownList>
</div>

<div class="ml-4">
Selected Size Number: <strong>@SelectedSizeMetric</strong>
</div>
</div>

@code { public IEnumerable<Size> Data { get; set; } public bool AllowCustom { get; set; }=true; public string SelectedSizeMetric { get; set; } public string SelectedSize { get; set; } public class Size { public string SizeText { get; set; } public string SizeMetric { get; set; }
} protected override void OnInitialized ( ) {
List<Size> sizes=new List<Size>();

sizes.Add( new Size()
{
SizeText="X-Small",
SizeMetric=3. ToString() });

sizes.Add( new Size()
{
SizeText="Small",
SizeMetric=6. ToString() });

sizes.Add( new Size()
{
SizeText="Medium",
SizeMetric=8. ToString() });

sizes.Add( new Size()
{
SizeText="Large",
SizeMetric=10. ToString() });

sizes.Add( new Size()
{
SizeText="X-Large",
SizeMetric=12. ToString() });

Data=sizes.AsQueryable(); base.OnInitialized();
}
} Regards, Marin Bratanov

### Response

**A** answered on 24 Feb 2020

Thanks a ton Marin for your reactivity. It works like a charm! :) A
