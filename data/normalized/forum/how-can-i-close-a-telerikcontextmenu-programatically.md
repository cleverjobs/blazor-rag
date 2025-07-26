# How can I close a TelerikContextMenu programatically?

## Question

**Víc** asked on 01 Jun 2023

I have a DropDownList where each element has a button to open a TelerikContextMenu as such: The problem is that sometimes the dropdown is closed and the menu not, like so: Here is my code: @namespace Appia.UiKit
@using Telerik.Extensions;
@using Appia.Entidades;
@using static Appia.Tests.Victor.TestWidget;
@inject IViewRepository ViewRepository <TelerikDropDownList @ref="DropDownRef" TItem="ValueWrapper<string>" TValue="string" Data="ListOfViews" Filterable="true" FilterOperator="@StringFilterOperator.Contains" FillMode="@ThemeConstants.DropDownList.FillMode.Flat" Class="" Width="min-content" ItemHeight="38" Value="@ActiveViewId" ValueChanged="OnChange" OnClose="OnClose" AdaptiveMode="@AdaptiveMode.Auto"> <ValueTemplate> @context.Text </ValueTemplate> <NoDataTemplate> No hay ninguna vista disponible </NoDataTemplate> <ItemTemplate> <div class="k-hbox w-100 k-border-bottom k-border-dark"> <div class="k-flex-grow k-align-self-center"> @context.Text </div> <div @onclick:stopPropagation="true"> <TelerikButton Icon="@(AppiaIcons.Stack)" OnClick="@HandleContextMenuButton" FillMode="@ThemeConstants.Button.FillMode.Flat"> </TelerikButton> </div> </div> </ItemTemplate> <FooterTemplate> <div class="k-border-t-only" @onclick:stopPropagation="true"> <TelerikButton Icon="@AppiaIcons.Favourite" Class="w-100 k-text-start" FillMode="@ThemeConstants.Button.FillMode.Flat"> Establecer como predeterminada </TelerikButton> <TelerikButton Icon="@AppiaIcons.Compose" Class="w-100 k-text-start" FillMode="@ThemeConstants.Button.FillMode.Flat"> Editar vista </TelerikButton> <TelerikButton Icon="@AppiaIcons.Globe" Class="w-100 k-text-start" FillMode="@ThemeConstants.Button.FillMode.Flat"> Renombrar vista </TelerikButton> <TelerikButton Icon="@AppiaIcons.Duplicate" Class="w-100 k-text-start" FillMode="@ThemeConstants.Button.FillMode.Flat"> Duplicar vista </TelerikButton> </div> </FooterTemplate> <DropDownListSettings> <DropDownListPopupSettings Height="430px" Width="min-content" Class="shadow-5" AnimationDuration="0" /> </DropDownListSettings> </TelerikDropDownList> <TelerikContextMenu @ref="@ViewItemMenuRef" Data="@ActionItems"> </TelerikContextMenu> @code {
[Parameter] public ViewInstance ViewInstance { get; set; }
public TelerikContextMenu <ActionItem>? ViewItemMenuRef { get; set; }
public TelerikDropDownList<ValueWrapper <string>, string> DropDownRef { get; set; }
public List<ValueWrapper <string>> ListOfViews { get; set; }=new();
public bool IsCancelled=false;
public string? ActiveViewId;

public List <ActionItem> ActionItems { get; set; }=new()
{
new () { Text="Activar", Icon=AppiaIcons.Eye },
new () { Text="Establecer como predeterminada", Icon=AppiaIcons.Favourite },
new () { Text="Editar", Icon=AppiaIcons.Compose },
new () { Text="Renombrar", Icon=AppiaIcons.Information },
new () { Text="Eliminar", Icon=AppiaIcons.Delete },
new () { Text="Duplicar", Icon=AppiaIcons.Duplicate }
};

protected override async Task OnInitializedAsync()
{
ActiveViewId=this.ViewInstance.ActiveView.Id;

this.ListOfViews=await ViewRepository
.ListAvailableAsync(this.ViewInstance.ActiveView.TipoDeVista, this.ViewInstance.ActiveView.EntityType)
.ThenSelect(x=> new ValueWrapper <string> (x.Id, x.Nombre))
.Then( x=> x.ToList() );

await base.OnInitializedAsync();
}

public async Task OnRead(DropDownListReadEventArgs args)=> await ViewRepository.ListAvailableAsync(ViewInstance.ActiveView.TipoDeVista, ViewInstance.ActiveView.EntityType, async db=> await db.ToDataSourceReadEvent(args));

public async Task HandleContextMenuButton( MouseEventArgs args )
{
IsCancelled=true;
await ViewItemMenuRef?.ShowAsync( args.ClientX, args.ClientY );
}

public void OnClose( DropDownListCloseEventArgs args )
{
args.IsCancelled=IsCancelled;
IsCancelled=false;
}

public void Close()
{
IsCancelled=false;
DropDownRef.Close();
IsCancelled=true;
}

public void OnChange( string args )
{
this.ActiveViewId=args;
Close();
}

} Therefore I need a way to close the menu programaticlly that I will fire when the dropdown list is closed. I would als like to have listeners on the TelerikContextMenu to know when it's closed, this way I could close the dropdown. How could I do that? Thanks

## Answer

**Dimo** answered on 06 Jun 2023

Hi Victor, Currently it is possible to close the ContextMenu with JSInterop. This feature request contains an example. Regards, Dimo
