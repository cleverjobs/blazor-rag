# Add Item To Grid In Code

## Question

**Gra** asked on 09 Aug 2021

Telerik Grid for Blazor, how to add a row through code. Should be easy, but I cannot find a straightforward answer anywhere. Here's my grid: <TelerikGrid Data=@GridPallets
Height="200px"
FilterMode="@GridFilterMode.None"
Sortable=true
Pageable=true>
<GridColumns>
<GridColumn Field=@nameof(PalletGridModel.Type) />
<GridColumn Field=@nameof(PalletGridModel.Quantity) />
<GridColumn Field=@nameof(PalletGridModel.Weight) />
<GridColumn Field=@nameof(PalletGridModel.DeliveryCharge) Title="Delivery Charge" />
<GridColumn Field=@nameof(PalletGridModel.HubCharge) Title="Hub Charge" />
</GridColumns>
</TelerikGrid> Here's some code on the same page to create a new item to add to the grid: PalletGridModel pgm=new PalletGridModel();

pgm.DeliveryCharge=palletType=="QTR" ? 10 : palletType=="HALF" ? 20 : palletType=="FULL" ? 30 : 40;
pgm.HubCharge=palletType=="QTR" ? 4 : palletType=="HALF" ? 5 : palletType=="FULL" ? 6 : 10;
pgm.Quantity=quantity;
pgm.Type=palletType;
pgm.Weight=weight; Everything I've tried after that to add that new item to the grid doesn't work - from adding the item to the grid data with a simple list.add(item) to trying to use the grid's update handler - but so far, nothing has worked. Surely something as simple and straightforward as this can't be this difficult?

## Answer

**Matthias** answered on 10 Aug 2021

Hi Graham, there are several solutions to this that could fix the problem. a) Use your own method (you probably already do) like LoadList... b) Show the grid after the data is already loaded (as a test, where the problem could be) c) Load the data as follows (also as a test) public ObservableCollection<Models.PalletGridModel> GridPallets { get; set; } public List <Models.PalletGridModel> GridPalletsList { get; set; }=new List<Models.PalletGridModel>(); //..your stuff.... PalletGridModel pgm=new PalletGridModel();

pgm.DeliveryCharge=palletType=="QTR"? 10: palletType=="HALF"? 20: palletType=="FULL"? 30: 40;
pgm.HubCharge=palletType=="QTR"? 4: palletType=="HALF"? 5: palletType=="FULL"? 6: 10;
pgm.Quantity=1;
pgm.Type=palletType;
pgm.Weight=weight; for ( int i=0; i <quantity; i++) GridPalletsList.Add(pgm); // end GridPallets=new ObservableCollection<Models.PalletGridModel>(GridPalletsList); I had never problems with adding rows to the grid as long I use an ObservableCollection.

### Response

**Marin Bratanov** answered on 09 Aug 2021

Hello Graham, Take a look at this article to see how to make the grid re-render after you change its data: [https://docs.telerik.com/blazor-ui/components/grid/refresh-data](https://docs.telerik.com/blazor-ui/components/grid/refresh-data) Regards, Marin Bratanov Progress Telerik

### Response

**Graham** answered on 10 Aug 2021

Martin: thanks for pointing me to that article which I hadn't seen. However, on updating the grid's data, it's still crashing with an error. Here are the key parts of my page: @using System.Collections.ObjectModel <TelerikGrid Data=@GridPallets Height="600px" Sortable=true Pageable=true> <GridColumns> <GridColumn Field=@nameof(PalletGridModel.Type) /> <GridColumn Field=@nameof(PalletGridModel.Quantity) /> <GridColumn Field=@nameof(PalletGridModel.Weight) /> <GridColumn Field=@nameof(PalletGridModel.DeliveryCharge) Title="Delivery Charge" /> <GridColumn Field=@nameof(PalletGridModel.HubCharge) Title="Hub Charge" /> </GridColumns> </TelerikGrid> public ObservableCollection <Models.PalletGridModel> GridPallets { get; set; }

PalletGridModel pgm=new PalletGridModel();

pgm.DeliveryCharge=palletType=="QTR" ? 10 : palletType=="HALF" ? 20 : palletType=="FULL" ? 30 : 40;
pgm.HubCharge=palletType=="QTR" ? 4 : palletType=="HALF" ? 5 : palletType=="FULL" ? 6 : 10;
pgm.Quantity=1;
pgm.Type=palletType;
pgm.Weight=weight;

for (int i=0; i <quantity; i++)
GridPallets.Add(pgm); The moment the line GridPallets.Add(pgm); is run, the page crashes with the error "An unhandled error has occurred. Reload".

### Response

@Matthias Making the grid data type an ObservableCollection instead of a List, your final suggestion, is a good answer - thanks.

### Response

**Matthias** commented on 11 Aug 2021

Thanks for the feedback! Have a nice day. Greetings Matthias
