# DropDownList with build in MRU list

## Question

**Mar** asked on 26 Jan 2023

My form has a DropDownList with products. I would like to have the last 10 used products on top. I will store the 10 last used products in localstorage and then sort the list, so the MRU items are on top. Has anyone implemented something similar? Can I rearrange the items in the DDL without triggering any events. Also can I add a divider between the MRU items and the rest of the products?

## Answer

**Martin Herløv** answered on 31 Jan 2023

This is one way to do it. The code has not matured, but it works 😊 Guess generic would improve it a lot. MruList.cs public class MruList { private readonly ILocalStorageService _localStorage; private readonly string _localeStorageKey; private readonly int _maxItems; public MruList ( ILocalStorageService localStorage, string localeStorageKey, int maxItems=10 ) {
_localStorage=localStorage;
_localeStorageKey=localeStorageKey;
_maxItems=maxItems;
} public async Task<List<Product>> MergeProductsWithMruList(List<Product> products)
{
_lst=await LoadFromLocalStorage() ?? new List<MruItem>(); if (!_lst.Any()) return products; var productsWithMru=_lst.OrderByDescending(x=> x.LastUsed)
.Select(mruItem=> products.FirstOrDefault(x=> x.Id==mruItem.Id))
.Where(p=> p !=default )
.ToList();

productsWithMru.AddRange(products.Where(x=> !_lst.Select(x=> x.Id).Contains(x.Id)).OrderBy(x=> x.Name)); return productsWithMru;
} private async Task<List<MruItem>> LoadFromLocalStorage()
{ return await _localStorage.GetItemAsync<List<MruItem>>(_localeStorageKey);
} private async Task SaveToLocalStorage ( ) { await _localStorage.SetItemAsync(_localeStorageKey, _lst);
} private List<MruItem> _lst=new (); public async Task Add ( int id ) {
Add( new MruItem(id)); await SaveToLocalStorage();
} private void Add ( MruItem item ) { if (_lst.Count>=_maxItems) _lst.RemoveAt(_lst.Count - 1 ); var itemFromList=_lst.FirstOrDefault(x=> x.Id==item.Id); if (itemFromList !=default ) _lst.Remove(itemFromList);
_lst.Insert( 0, item);
}
} MruItem.cs [ DebuggerDisplay( "{Id},{LastUsed}" ) ] public class MruItem { private sealed class IdEqualityComparer: IEqualityComparer <MruItem>
{ public bool Equals ( MruItem x, MruItem y ) { return x.Id==y.Id;
} public int GetHashCode ( MruItem obj ) { return obj.Id;
}
} public static IEqualityComparer<MruItem> IdComparer { get; }=new IdEqualityComparer(); public MruItem ( ) {
} public MruItem ( int id ) : this ( id, DateTime.Now ) {
} public MruItem ( int id, DateTime lastUsed ) {
Id=id;
LastUsed=lastUsed;
} public int Id { get; set; } public DateTime LastUsed { get; set; }
} How to use in razor page private const string LocaleStorageKey="ibex_products"; protected override async Task OnInitializedAsync ( ) {
_mruList=new MruList(LocalStorageService, LocaleStorageKey);
_productsFromServer=await TradeService.GetProducts();
Products=await _mruList.MergeProductsWithMruList(_productsFromServer);
} Save to local storage private async Task CreateTrade ( ) { var success=await TradeService.CreateManualTrade(TradeModel);
Console.WriteLine( $"Trade Created {success} " ); if (success)
{
Notifications.Success( "Trade Created" ); await _mruList.Add(TradeModel.ProductId); await ResetForm();
} else {
Notifications.Error( "Failed to create trade" );
}
}

### Response

**Tsvetomir** answered on 31 Jan 2023

Hi, Martin, The Telerik UI Blazor DropDownList is a UI component intended to display data. Even though it provides interaction with the actual items, it does not apply any processing logic. Therefore, if you would like to see the items sorted in a way, you should preprocess the collection (or query) before supplying it to the DropDownList. The component will handle the visualization on its own. Regarding the separator, you could leverage the ItemTemplate and if you know which is the 10th most used product, you could apply different rendering, e.g. render an additional HTML element with a specific styling. Let me know if further assistance is needed. Kind regards, Tsvetomir
