# Getting @ref from the grid before call to OnStateInit

## Question

**Mar** asked on 13 Dec 2021

Hi I have made a utility class for helping with state management <TelerikButton OnClick="@_gridStateManager.SaveState" Icon="download"> Save State </TelerikButton> <TelerikButton OnClick="@_gridStateManager.LoadState" Icon="upload"> Load State </TelerikButton> <TelerikButton OnClick="@_gridStateManager.ResetState" Icon="reset"> Reset State </TelerikButton> In the code behind file protected override async Task OnInitializedAsync ( ) {
_gridStateManager=new GridStateManager<PortfolioListItem>(LocalStorage, PortfolioListGrid, GetDefaultGridState);
} The problem is that the GridStateManger gets a null reference to the grid. I know that the @ref is only safe to get in OnAfterRender / Async. How can I initialize the GridStateManager with the @ref set and also make it possible for the grid to call : OnStateInit="@((GridStateEventArgs <PortfolioListItem> args)=> _gridStateManager.OnStateInitHandler(args))"> In a safe way? This is the code for my GridStateManager using System; using System.Threading.Tasks; using Blazored.LocalStorage; using Telerik.Blazor.Components; namespace Argus.Client; public class GridStateManager <T> where T: class { private readonly ILocalStorageService _localStorage; private readonly TelerikGrid<T> _grid; private readonly Func<GridState<T>> _getDefaultGridState; private readonly string _stateStorageKey; public GridStateManager ( ILocalStorageService localStorage,
TelerikGrid<T> grid,
Func<GridState<T>> getDefaultGridState ) {
_localStorage=localStorage;
_grid=grid;
_getDefaultGridState=getDefaultGridState;
_stateStorageKey=$"GridStateFor { nameof (T)} ";
} public async Task OnStateInitHandler ( GridStateEventArgs<T> args ) { try { var storageState=await _localStorage.GetItemAsync<GridState<T>>(_stateStorageKey); if (storageState !=null )
args.GridState=storageState; if (storageState==null && _getDefaultGridState !=null )
args.GridState=_getDefaultGridState();
}
catch (Exception e)
{
Console.WriteLine(e);
}
} public async Task SaveState ( ) { var gridState=_grid.GetState(); await _localStorage.SetItemAsync(_stateStorageKey, gridState);
} public async Task LoadState ( ) {
GridState<T> storedState=await _localStorage.GetItemAsync<GridState<T>>(_stateStorageKey); if (storedState !=null )
{ await _grid.SetState(storedState);
}
} public async void ResetState ( ) { if (_getDefaultGridState !=null )
{ await _grid.SetState(_getDefaultGridState());
} await _localStorage.RemoveItemAsync(_stateStorageKey);
}
} If I could get the grid reference in the OnStateInit EventCallBack then I would have solved the problem OnStateInit="@((GridStateEventArgs <PortfolioListItem> args)=> _gridStateManager.OnStateInitHandler(args, @gridRef))"> I then tried to create the GridStateManger in the OnStateInit call from the grid. But I still don't have a valid ref to the grid, why? OnStateInit="@((GridStateEventArgs <PortfolioListItem> args)=> InitGridStateManager(args))"> private async Task InitGridStateManager ( GridStateEventArgs<PortfolioListItem> args ) {
_gridStateManager=new GridStateManager<PortfolioListItem>(LocalStorage, PortfolioListGrid, GetDefaultGridState); await _gridStateManager.OnStateInitHandler(args);
}

### Response

**Martin Herløv** commented on 13 Dec 2021

Ended up wit setting the ref to the grid in OnAfterRender. Not so clean, but it works protected override void OnAfterRender(bool firstRender)
{
if(firstRender)
{
_gridStateManager.Grid=PortfolioListGrid;
}
}

### Response

**Marin Bratanov** commented on 14 Dec 2021

I think that's the only way to do this in Blazor, and the fact that you can't have a @ref sooner is one of the reasons why we made dedicated events for the grid state with suitable arguments. Something else you could consider (but I have not tested and I don't know if it will work) is to use the setter of the field you point the @ref to to populate the service with that reference as well.
