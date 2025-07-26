# Value is Not Changing when Dynamic Create Telerik ComboBox or DropDownList

## Question

**Ryd** asked on 26 Jul 2021

Dears , Because of some reason , I need to Customer Telerik Blazor Componet into Custome Componet and then Render it in Dynamic Ways , Like This . FabCombobox.razor (Componet) @typeparam T
@typeparam TResource <div class="row"> <label class="col-md-2"> @Label </label> <div class="col-md-5"> <TelerikComboBox Value="@ResultValue" Data="@Resource" Placeholder="@Placeholder" Filterable="@Filterable" TextField="@TextField" ValueField="@ValueField" Enabled="@Enabled" Id="@ID" Width="100%" ValueChanged="@ResultValueChanged"> </TelerikComboBox> </div> </div> @code {
[Parameter] public bool bBindData { get; set; }=false;
[Parameter] public string Label { get; set; }
[Parameter] public T ResultValue { get; set; }
[Parameter] public List <TResource> Resource { get; set; }
[Parameter] public string Placeholder { get; set; }="Select Item";
[Parameter] public bool Filterable { get; set; }=false;
[Parameter] public string Width { get; set; }="100%";
[Parameter] public string TextField { get; set; }
[Parameter] public string ValueField { get; set; }
[Parameter] public bool Enabled { get; set; }
[Parameter] public string ID { get; set; }="TelerikComboBox" + Guid.NewGuid().ToString();
[Parameter] public EventCallback <T> ResultValueChanged { get; set; }

} DynamicTable.Razor (Componet) @using System.Linq.Expressions <div class="card"> <div class="card-body"> @foreach (var item in Contents)
{
@item
;
} </div> </div> @code {
[Parameter]
public List <Blazor_Dynamic.Shared.FabComponet> Componets { get; set; }

public List <RenderFragment> Contents { get; set; }

protected override void OnInitialized()
{
if (Componets.Count()> 0 && Componets !=null)
{
CreateFragment();
}

base.OnInitialized();
}
public void CreateFragment()
{
int iComponent=0;
List <RenderFragment> RFTs=new List <RenderFragment> ();
foreach (var area in Componets)
{

RenderFragment renderFragment=(builder)=>
{
object o=new object();

builder.OpenComponent(iComponent, area.Type);
int iDic=0;
foreach (var item in area.Dic)
{
builder.AddAttribute(iDic, item.Key, item.Value);
}
builder.CloseComponent();
};
RFTs.Add(renderFragment);
}
Contents=RFTs;
}
} DynamicConnect.razor (Page) @page "/DynamicConnect" <h3> DynamicConnect </h3> @inject IProductRepository IProductRepo <DynamicTable Componets="@liComponets"> </DynamicTable> <p> @CurrentType </p> <p> @CurrentProduct </p> @code {
public List <Product> products { get; set; }
public List <Selection> productTypes { get; set; }
private Selection productType { get; set; }
public Product product { get; set; }
private string CurrentType { get; set; }
private Guid? CurrentProduct { get; set; }
private string sFullProductInfo { get; set; }
public List <FabComponet> liComponets { get; set; }

public class Selection
{
public string id { get; set; }
public string text { get; set; }
}
protected override void OnInitialized()
{
products=IProductRepo.GetProducts();
productTypes=(from w in products group w by w.Type into g select g.First()).Select(x=> new Selection { id=x.Type, text=x.Type }).ToList();

List <FabComponet> FCs=new List <FabComponet> ();
var dic=new Dictionary<string, object>();
dic.Add("Label", "Product Category");
dic.Add("Resource", productTypes);
dic.Add("ResultValue", CurrentType);
dic.Add("Placeholder", "Select Somthing??");
dic.Add("TextField", "id");
dic.Add("ValueField", "text");
dic.Add("Filterable", false);
dic.Add("Enabled", true);
dic.Add("Id", "cbxType");
dic.Add("Width", "100%");
dic.Add("ResultValueChanged", EventCallback.Factory.Create <System.String> (this, str=> TypeSelected(str)));

FabComponet First=new FabComponet() { Type=typeof(FabComboBox<string,Selection>), Row="1", Length="6", Seq="1", Dic=dic };
FCs.Add(First);

var dic2=new Dictionary<string, object>();
dic2.Add("Label", "Product");
dic2.Add("Resource", products);
dic2.Add("ResultValue", CurrentProduct);
dic2.Add("ValueField", nameof(Product.ID));
dic2.Add("TextField", nameof(Product.ProductName));
dic2.Add("Filterable", false);
dic2.Add("Enabled", (CurrentType !=null));
dic2.Add("Id", "cbxProduct");
dic2.Add("Width", "100%");
dic2.Add("ResultValueChanged", EventCallback.Factory.Create<Nullable <System.Guid>>(this, x=> ProductSelected(x)));
FabComponet Sec=new FabComponet() { Type=typeof(FabComboBox<Nullable <Guid>,Product>), Row="1", Length="6", Seq="1", Dic=dic2 };
FCs.Add(Sec);

liComponets=FCs;

base.OnInitialized();
}
public void TypeSelected(string SelectionType)
{
products=IProductRepo.GetProductsByType(SelectionType);
productType=productTypes.Where(x=> x.id==SelectionType).First();
CurrentType=SelectionType;
}
public void ProductSelected(Guid? SelectionProduct)
{
CurrentProduct=SelectionProduct.HasValue ? SelectionProduct.Value : null;
product=products.Where(p=> p.ID==SelectionProduct).First();
}
} But , When I Change the Value of Product Category , it didn't show what I did Selected , but CurrentType is Changed . and Product is still Disabled . Is there any thing went wrong ? I'm , Using .net Core 6.0 and Visual Studio 2019 Preview .

### Response

**Ryder** commented on 28 Jul 2021

Can someone helps me on this problem ?
