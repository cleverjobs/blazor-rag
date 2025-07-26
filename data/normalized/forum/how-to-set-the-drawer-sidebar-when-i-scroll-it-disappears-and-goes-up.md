# How to set the Drawer sidebar, when I scroll it disappears and goes up?

## Question

**Jos** asked on 17 Jun 2023

Hello how are you, I have a problem, I guess it's simple, but my css level is low and I don't know how to set the Drawer sidebar, when I scroll it disappears and goes up. I did this to put a sticky on a div that contains it but it doesn't work, it keeps failing. I do it this: <div class="sticky-sidebar"> <TelerikDrawer...> <!-- El contenido de tu Drawer aquí --> </TelerikDrawer> </div> and this: .sticky-sidebar {
position: sticky;
top: 0;
height: 100vh; /* Esto asegura que el contenedor ocupe toda la altura de la vista */
overflow-y: auto; /* Esto permite que el contenido dentro del contenedor se desplace */
} The result is this: This is my MainLaout.razor @*Encabezado*@<div class="custom-toolbar top-row" style="display: flex; justify-content: space-between; z-index:200"> <div class="boton_y_logo" style="white-space:nowrap; "> <TelerikButton Class="hamburguer-button" OnClick="@( ()=> Drawer.ToggleAsync() )"> </TelerikButton> <img src="/logo.jpg" alt="Logo de xxx" style="width: 150px; height: 40px; margin-left: 0px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); line-height:40px" /> <span class="item_seleccionado"> @SelectedItem?.Text </span> </div> </div> <div class="sticky-sidebar"> <TelerikDrawer Data="@Data" Class="my-drawer" @bind-Expanded="@Expanded" MiniMode="false" Mode="@DrawerMode.Push" @ref="@this.Drawer" @bind-SelectedItem="@SelectedItem"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> </div> </Template> <DrawerContent> <div class="main"> <div class="content px-4"> @Body </div> </div> </DrawerContent> </TelerikDrawer> </div> @code {

} and this is my site.css @import url( 'open-iconic/font/css/open-iconic-bootstrap.min.css' ); html, body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
} a,.btn-link { color: #0366d6;
}.btn-primary { color: #fff; background-color: #1b6ec2; border-color: #1861ac;
}.content { padding-top: 1.1rem;
}.valid.modified:not ( [type=checkbox] ) { outline: 1px solid #26b050;
}.invalid { outline: 1px solid red;
}.validation-message { color: red;
} #blazor-error-ui { background: lightyellow; bottom: 0; box-shadow: 0 - 1px 2px rgba ( 0, 0, 0, 0.2 ); display: none; left: 0; padding: 0.6rem 1.25rem 0.7rem 1.25rem; position: fixed; width: 100%; z-index: 1000;
} #blazor-error-ui.dismiss { cursor: pointer; position: absolute; right: 0.75rem; top: 0.5rem;
}.page { position: relative; display: flex; flex-direction: column;
}.main { flex: 1;
}.sidebar { background-image: linear-gradient ( 180deg, rgb ( 5, 39, 103 ) 0%, #3a0647 70% );
}.top-row { background-color: rgb ( 37, 40, 55 )!important; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); /*border-bottom: 0px solid #d6d5d5;*/ justify-content: flex-end; height: 3.5rem; display: flex; align-items: center; /*left: 0;*/ }.top-row::deep a, .top-row .btn-link { white-space: nowrap; /*margin-left: 1.5rem;*/ }.top-row a:first -child { overflow: hidden; text-overflow: ellipsis; /*margin-right: 10px*/ } /* Estilos para modo celular */ @media ( max-width: 640.98px ) {.top-row:not (.auth ) { display: none;
}.top-row.auth { justify-content: space-between;
}.top-row a,.top-row.btn-link { margin-left: 0;
}

} @media ( min-width: 641px ) {.page { flex-direction: row;
}.sidebar { width: 250px; height: 100vh; position: sticky; top: 0;
}.top-row { position: sticky; top: 0; z-index: 1;
}.main> div { padding-left: 2rem!important; padding-right: 1.5rem!important;
}
} /*extra cc*/.k-icon { font-size: 20px;
}.custom-toolbar { width: 100%; line-height: 10px; border-bottom: inset; border-bottom-width: 1px; padding: 3px 8px; color: #a1a1a1; background-color: #252837!important; height: 50px; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); align-content: center; align-items: center; text-decoration: none; position: sticky; top: 0;
}.item_seleccionado { margin-left: 20px; font-weight: bold; font-size: 17px; width: 100%;
} /*Dimensiones de controles*/.margenlados5px { margin: 5px;
}.Altura_total { height: 100%;
} /*íconos de header*/.hamburguer-button { width: 2rem; height: 2rem; background-size: contain;
-webkit- mask-repeat: no-repeat; mask-repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.75; mask-image: url ( "../icons/icons8-menu-24.png" );
-webkit- mask-image: url ( "../icons/icons8-menu-24.png" ); margin-right: 5px; color: white;
}.tb-icon { width: 1rem; height: 1rem; background-size: contain;
-webkit- mask-repeat: no-repeat; mask-repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.7;
}.tb-icon-settings { mask-image: url ( "../icons/setting.png" );
-webkit- mask-image: url ( "../icons/setting.png" ); color: aliceblue;
}.tb-icon-maximizar { mask-image: url ( "../icons/maximizar.png" );
-webkit- mask-image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-info_grid { mask-image: url ( "../icons/informacion.png" );
-webkit- mask-image: url ( "../icons/informacion.png" ); opacity: 1; color: black;
}.tb-icon-logo { mask-image: url ( "../icons/maximizar.png" );
-webkit- mask-image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-refresh { mask-image: url ( "../icons/refresh.png" );
-webkit- mask-image: url ( "../icons/refresh.png" ); color: aliceblue;
} /*fullscreen f11*/ *:fullscreen *:-ms-fullscreen,
*:-webkit-full-screen,
*:-moz-full-screen { overflow: auto!important;
}.drawer-container { width: 100%; height: 100%;
}.borde_cero { margin: 0; padding: 0;
}.texto_drawer { font-size: 10px;
}.k-d-level { display: flex;
}.texto_body { font-size: 14px;
}.item-descr-wrap> span { font-size: 70%;
}.item-descr-wrap { display: flex; flex-direction: column; font-size: 12px; font-family: Arial, Helvetica, sans-serif;
} /*copiado de host*/.k-drawer-content { overflow-x: auto;
}.drawer-hamburger { position: absolute; z-index: 2; margin-top: 13px; margin-left: 30px;
}.k-drawer-item:hover,.k-drawer-item.k-state-hover,.text-info { color: #281f3eb3!important; background-color: #ff6358;
} /*colores defs fondo symbol texto de drawer*/.my-drawer.k-drawer { background-color: #252837; color: white; z-index: 0; height: 100%;

}.my-drawer.k-drawer-item { font-size: 12px; display: flex; align-items: center;

}.my-drawer.k-drawer-item:hover { background-color: #414762; color: antiquewhite!important;
} /*cuadros en ítem principales*/.k-drawer-item-main { box-sizing: border-box; padding: 2px; /*border: 1px solid #000;*/ background-color: #1e3548;
}.sticky-sidebar {
position: sticky;
top: 0;
height: 100vh; /* Esto asegura que el contenedor ocupe toda la altura de la vista */
overflow-y: auto; /* Esto permite que el contenido dentro del contenedor se desplace */
} Please, how to set the Drawer sidebar, when I scroll it disappears and goes up? thanks.

## Answer

**Jose** answered on 26 Jun 2023

Hello, thanks for answering, I tried to place the mentioned CSS but nothing has happened, the same thing is still happening. html, body, app,.my-drawer,.k-drawer-content { width: 100%; height: 100%; max-height: 100%;
}

### Response

**Hristian Stefanov** commented on 27 Jun 2023

Hi Jose, Thank you for providing an update on the issue. I apologize that the solution I suggested in my previous response did not resolve the problem as expected. It appears that there might be some CSS styles conflicting with the "height: 100%;" setting of the Drawer component. In my attempts to replicate the issue using the configuration you provided initially, I was still unable to encounter the scrolling problem on my end. To further investigate and assist you effectively, can you please send a small, runnable sample that reproduces the issue? You can use the REPL platform for your convenience instead of attaching a complete project. Your cooperation is greatly appreciated, and I eagerly await your response. Kind Regards, Hristian

### Response

**Jose** commented on 18 Jul 2023

Hi, i use RPL platform: Blazor RPM sorry for my english. Kind Regards,

### Response

**Hristian Stefanov** commented on 20 Jul 2023

Hi Jose, Thank you once again for your cooperation. I was able to replicate the described behavior using the code from the REPL link you provided in your last message. Now, I'm ready to share my observations and help you resolve the issue. The problem arises from the positioning of the HTML code responsible for the custom toolbar inside the "MainLayout.razor" file. This positioning creates an unnecessary additional scrollbar, causing the custom toolbar to overlap the drawer when scrolling. To fix this problem and eliminate the extra scrollbar, you need to position the custom toolbar inside the "main" div element and apply some additional styles. Below, I've outlined the necessary changes to be made in the updated MainLayout.razor page. Once you implement these changes in your actual project, you should see the desired result. MainLayout.razor @layout TelerikLayout
@inherits LayoutComponentBase
@inject NavigationManager navigationManager

@using Telerik.Blazor.Services;
@using System.Collections.Generic;
@inject ITelerikStringLocalizer Localizer
@inject IJSRuntime JS;
@using Telerik.FontIcons
@using Telerik.SvgIcons;

@inject NavigationManager NavigationManager
@inject NavigationManager NavigationManager
@inject ITelerikStringLocalizer Localizer
@inject IJSRuntime JS;
@using Telerik.Blazor.Components

@*Ocultar SideBar cuando esté con ancho menor a 480px*@<TelerikMediaQuery Media="(max-width: 480px)" OnChange="@(OnChangexx)"> </TelerikMediaQuery> @*Sidebar y Body*@<TelerikDrawer Data="@Data" Class="my-drawer" @bind-Expanded="@Expanded" MiniMode="false" Mode="@DrawerMode.Push" @ref="@this.Drawer" @bind-SelectedItem="@SelectedItem"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> @* <TelerikTooltip TargetSelector=".k-drawer-items span.k-icon[title]" ShowOn="@TooltipShowEvent.Hover" Position="TooltipPosition.Right" /> *@<ul> @foreach (var item in context)
{
var selectedClass=item==SelectedItem ? "k-selected" : string.Empty;
var levelClass=Expanded==true ? $"k-level-{item.Level}" : "";
var mainItemClass=item.Level==0 ? "k-drawer-item-main" : ""; // Asume que los elementos principales tienen Level 0 <li class="k-drawer-item @selectedClass @levelClass @mainItemClass"> @* <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass k-level-@(item.Level)"> *@<TelerikSvgIcon Icon="@item.Icon"> </TelerikSvgIcon> @if (item.Text=="INICIO")
{ <div class="hl"> </div> } <span class="k-item-text"> @item.Text </span> <div class="hl"> </div> @if (item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"> </span> }
else if (!item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"> </span> } </li> } </ul> </div> </Template> <DrawerContent> <div class="main"> <div class="custom-toolbar top-row" style="display: flex; justify-content: space-between; z-index:200; position: absolute;"> <div class="boton_y_logo" style="white-space: nowrap; max-width: calc(100% - 170px); display: flex; align-items: center;"> <TelerikButton Class="hamburguer-button" OnClick="@( ()=> Drawer.ToggleAsync() )"> </TelerikButton> <img src="/logocrn.jpg" alt="Logo de RIOS DEL NORTE" class="logo" style="width: 150px; height: 40px; margin-left: 0px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); line-height:40px" /> <div id="myDiv" style="white-space: normal; text-align: center; "> <span class="item_seleccionado"> @SelectedItem?.Text </span> </div> </div> <div> <TelerikButton Class="tb-icon tb-icon-refresh margenlados5px" Title="Actualizar" OnClick="@( async ()=> await JS.InvokeVoidAsync(" refreshPage ") )"> </TelerikButton> <TelerikButton Class="tb-icon tb-icon-maximizar margenlados5px" Title="Maximizar" OnClick="@( async ()=> await JS.InvokeVoidAsync(" toggleFullScreen ") )"> </TelerikButton> <TelerikButton Class="tb-icon tb-icon-settings margenlados5px" Title="Configurar"> </TelerikButton> </div> </div> <div class="content px-4"> @Body </div> </div> </DrawerContent> </TelerikDrawer> @code {
private bool XSmall { get; set; }
private bool Small { get; set; }
private bool Medium { get; set; }
private bool Large { get; set; }
public bool MiniMode { get; set; }=false;
public bool Expanded { get; set; }=true;
public DrawerItem SelectedItem { get; set; }
public TelerikDrawer <DrawerItem> Drawer { get; set; }
public IEnumerable <DrawerItem> Data { get; set; }

protected override void OnInitialized()
{
base.OnInitialized();

var data=new List <DrawerItem> {
new DrawerItem
{
Text="INICIO",
Url="/",
Icon=SvgIcon.Home
},

new DrawerItem
{
Text="ADMINISTRACION CONTRACTUAL",
Icon=SvgIcon.BloggerBox,
},
new DrawerItem
{
Text="CALIDAD",
Icon=SvgIcon.BloggerBox,
Children=new List <DrawerItem> ()
{
new DrawerItem { Text="CALIDAD", Icon=SvgIcon.BloggerBox, Level=1 },
}
},

};

Data=data;
SelectedItem=Data.First();
}

public class DrawerItem
{

public string Text { get; set; }

public string Url { get; set; }

public ISvgIcon Icon { get; set; }

public bool Separator { get; set; }

public bool Expanded { get; set; }

public int Level { get; set; }

public IEnumerable <DrawerItem> Children { get; set; }
}
void LogoutClick()
{
}

#region para Minimode oculto en modo celular
private string MediaQuery { get; set; }="(max-width: 1440px)";

private void OnChangexx(bool doesMatch)
{
MiniMode=!doesMatch;

}

#endregion

} <style> html, body, app,.k-drawer-container,.k-drawer-content,.main { width: 100%; height: 100%; max-height: 100%;
} html, body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
} a,.btn-link { color: #0366d6;
}.btn-primary { color: #fff; background-color: #1b6ec2; border-color: #1861ac;
}.content { padding-top: 1.1rem;
}.valid.modified:not ( [type=checkbox] ) { outline: 1px solid #26b050;
}.invalid { outline: 1px solid red;
}.validation-message { color: red;
} #blazor-error-ui { background: lightyellow; bottom: 0; box-shadow: 0 - 1px 2px rgba ( 0, 0, 0, 0.2 ); display: none; left: 0; padding: 0.6rem 1.25rem 0.7rem 1.25rem; position: fixed; width: 100%; z-index: 1000;
} #blazor-error-ui.dismiss { cursor: pointer; position: absolute; right: 0.75rem; top: 0.5rem;
}.page { position: relative; display: flex; flex-direction: column;
}.main { flex: 1; overflow-y: auto; }.sidebar { background-image: linear-gradient ( 180deg, rgb ( 5, 39, 103 ) 0%, #3a0647 70% );
}.top-row { background-color: rgb ( 37, 40, 55 )!important; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); /*border-bottom: 0px solid #d6d5d5;*/ justify-content: flex-end; height: 3.5rem; display: flex; align-items: center; left: 0;
}.top-row::deep a, .top-row .btn-link {
white-space: nowrap; /*margin-left: 1.5rem;*/ }.top-row a:first -child { overflow: hidden; text-overflow: ellipsis; /*margin-right: 10px*/ } /* Estilos para modo celular */ /*extra cc*/.k-icon { font-size: 20px;
}.custom-toolbar { width: 100%; line-height: 10px; border-bottom: inset; border-bottom-width: 1px; padding: 3px 8px; color: #a1a1a1; background-color: #252837!important; height: 50px; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); align-content: center; align-items: center; text-decoration: none; position: absolute; top: 0;
}.item_seleccionado { margin-left: 20px; font-weight: bold; font-size: 17px; width: 100%;
} /*Dimensiones de controles*/.margenlados5px { margin: 5px;
}.Altura_total { height: 100%;
} /*íconos de header*/.hamburguer-button { width: 2rem; height: 2rem; background-size: contain;
-webkit- mask -repeat: no-repeat; mask -repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.75; mask -image: url ( "../icons/icons8-menu-24.png" );
-webkit- mask -image: url ( "../icons/icons8-menu-24.png" ); margin-right: 5px; color: white;
}.tb-icon { width: 1rem; height: 1rem; background-size: contain;
-webkit- mask -repeat: no-repeat; mask -repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.7;
}.tb-icon-settings { mask -image: url ( "../icons/setting.png" );
-webkit- mask -image: url ( "../icons/setting.png" ); color: aliceblue;
}.tb-icon-maximizar { mask -image: url ( "../icons/maximizar.png" );
-webkit- mask -image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-info_grid { mask -image: url ( "../icons/informacion.png" );
-webkit- mask -image: url ( "../icons/informacion.png" ); opacity: 1; color: black;
}.tb-icon-logo { mask -image: url ( "../icons/maximizar.png" );
-webkit- mask -image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-refresh { mask -image: url ( "../icons/refresh.png" );
-webkit- mask -image: url ( "../icons/refresh.png" ); color: aliceblue;
} /*fullscreen f11*/ /**:fullscreen
*:-ms-fullscreen,
*:-webkit-full-screen,
*:-moz-full-screen {
overflow: auto !important;
}*/.k-drawer-wrapper { top: 49px; position: sticky; overflow: hidden;
}.drawer-container { width: 100%; height: 100%;
}.borde_cero { margin: 0; padding: 0;
}.texto_drawer { font-size: 10px;
}.k-d-level { display: flex;
}.texto_body { font-size: 14px;
}.item-descr-wrap> span { font-size: 70%;
}.item-descr-wrap { display: flex; flex-direction: column; font-size: 12px; font-family: Arial, Helvetica, sans-serif;
} /*copiado de host*/.k-drawer-content { overflow-x: auto;
}.drawer-hamburger { position: absolute; z-index: 2; margin-top: 13px; margin-left: 30px;
}.k-drawer-item:hover,.k-drawer-item.k-state-hover,.text-info { color: #281f3e b3!important; background-color: #ff6358;
} /*colores defs fondo symbol texto de drawer*/.my-drawer.k-drawer { background-color: #252837; color: white; z-index: 0; height: 100%;
}.my-drawer.k-drawer-item { font-size: 12px; display: flex; align-items: center;
}.my-drawer.k-drawer-item:hover { background-color: #414762; color: antiquewhite!important;
} /*cuadros en ítem principales de sidebar*/.k-drawer-item-main { box-sizing: border-box; padding: 2px; /*border: 1px solid #000;*/ background-color: #1e3548;
}.texto_centrado { text-align: center!important;
} </style> Incorporate these modifications, and feel free to reach out if you need any further assistance. Kind Regards, Hristian

### Response

**Jose** commented on 21 Jul 2023

Hello, it works very well, the detail is that now the sidebar occupies 100% of the height, and is not placed below the header, is it possible to do that without the sidebar occupying the entire height? please.

### Response

**Nadezhda Tacheva** commented on 25 Jul 2023

Hi Jose, With the above configuration, the header (top row) is rendered inside the Drawer. If you want the Drawer to be placed below the header, I can suggest declaring the header outside of the Drawer. In addition, you can set padding-top to the Drawer container equal to the header height to ensure they will not overlap. Here is the modified code: @layout TelerikLayout
@inherits LayoutComponentBase
@inject NavigationManager navigationManager

@using Telerik.Blazor.Services;
@using System.Collections.Generic;
@inject ITelerikStringLocalizer Localizer
@inject IJSRuntime JS;
@using Telerik.FontIcons
@using Telerik.SvgIcons;

@inject NavigationManager NavigationManager
@inject NavigationManager NavigationManager
@inject ITelerikStringLocalizer Localizer
@inject IJSRuntime JS;
@using Telerik.Blazor.Components

@*Ocultar SideBar cuando esté con ancho menor a 480px*@<TelerikMediaQuery Media="(max-width: 480px)" OnChange="@(OnChangexx)"> </TelerikMediaQuery> @*Sidebar y Body*@<div class="custom-toolbar top-row" style="display: flex; justify-content: space-between; z-index:200; position: absolute;"> <div class="boton_y_logo" style="white-space: nowrap; max-width: calc(100% - 170px); display: flex; align-items: center;"> <TelerikButton Class="hamburguer-button" OnClick="@( ()=> Drawer.ToggleAsync() )"> </TelerikButton> <img src="/logocrn.jpg" alt="Logo de RIOS DEL NORTE" class="logo" style="width: 150px; height: 40px; margin-left: 0px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); line-height:40px" /> <div id="myDiv" style="white-space: normal; text-align: center; "> <span class="item_seleccionado"> @SelectedItem?.Text </span> </div> </div> <div> <TelerikButton Class="tb-icon tb-icon-refresh margenlados5px" Title="Actualizar" OnClick="@( async ()=> await JS.InvokeVoidAsync(" refreshPage ") )"> </TelerikButton> <TelerikButton Class="tb-icon tb-icon-maximizar margenlados5px" Title="Maximizar" OnClick="@( async ()=> await JS.InvokeVoidAsync(" toggleFullScreen ") )"> </TelerikButton> <TelerikButton Class="tb-icon tb-icon-settings margenlados5px" Title="Configurar"> </TelerikButton> </div> </div> <TelerikDrawer Data="@Data" Class="my-drawer" @bind-Expanded="@Expanded" MiniMode="false" Mode="@DrawerMode.Push" @ref="@this.Drawer" @bind-SelectedItem="@SelectedItem"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> @* <TelerikTooltip TargetSelector=".k-drawer-items span.k-icon[title]" ShowOn="@TooltipShowEvent.Hover" Position="TooltipPosition.Right" /> *@<ul> @foreach (var item in context)
{
var selectedClass=item==SelectedItem ? "k-selected" : string.Empty;
var levelClass=Expanded==true ? $"k-level-{item.Level}" : "";
var mainItemClass=item.Level==0 ? "k-drawer-item-main" : ""; // Asume que los elementos principales tienen Level 0 <li class="k-drawer-item @selectedClass @levelClass @mainItemClass"> @* <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass k-level-@(item.Level)"> *@<TelerikSvgIcon Icon="@item.Icon"> </TelerikSvgIcon> @if (item.Text=="INICIO")
{ <div class="hl"> </div> } <span class="k-item-text"> @item.Text </span> <div class="hl"> </div> @if (item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"> </span> }
else if (!item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"> </span> } </li> } </ul> </div> </Template> <DrawerContent> <div class="main"> <div class="content px-4"> @Body </div> </div> </DrawerContent> </TelerikDrawer> @code {
private bool XSmall { get; set; }
private bool Small { get; set; }
private bool Medium { get; set; }
private bool Large { get; set; }
public bool MiniMode { get; set; }=false;
public bool Expanded { get; set; }=true;
public DrawerItem SelectedItem { get; set; }
public TelerikDrawer <DrawerItem> Drawer { get; set; }
public IEnumerable <DrawerItem> Data { get; set; }

protected override void OnInitialized()
{
base.OnInitialized();

var data=new List <DrawerItem> {
new DrawerItem
{
Text="INICIO",
Url="/",
Icon=SvgIcon.Home
},

new DrawerItem
{
Text="ADMINISTRACION CONTRACTUAL",
Icon=SvgIcon.BloggerBox,
},
new DrawerItem
{
Text="CALIDAD",
Icon=SvgIcon.BloggerBox,
Children=new List <DrawerItem> ()
{
new DrawerItem { Text="CALIDAD", Icon=SvgIcon.BloggerBox, Level=1 },
}
},

};

Data=data;
SelectedItem=Data.First();
}

public class DrawerItem
{

public string Text { get; set; }

public string Url { get; set; }

public ISvgIcon Icon { get; set; }

public bool Separator { get; set; }

public bool Expanded { get; set; }

public int Level { get; set; }

public IEnumerable <DrawerItem> Children { get; set; }
}
void LogoutClick()
{
}

#region para Minimode oculto en modo celular
private string MediaQuery { get; set; }="(max-width: 1440px)";

private void OnChangexx(bool doesMatch)
{
MiniMode=!doesMatch;

}

#endregion

} <style> html, body, app,.k-drawer-container,.k-drawer-content,.main { width: 100%; height: 100%; max-height: 100%;
} html, body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
} a,.btn-link { color: #0366d6;
}.btn-primary { color: #fff; background-color: #1b6ec2; border-color: #1861ac;
}.content { padding-top: 1.1rem;
}.valid.modified:not ( [type=checkbox] ) { outline: 1px solid #26b050;
}.invalid { outline: 1px solid red;
}.validation-message { color: red;
} #blazor-error-ui { background: lightyellow; bottom: 0; box-shadow: 0 - 1px 2px rgba ( 0, 0, 0, 0.2 ); display: none; left: 0; padding: 0.6rem 1.25rem 0.7rem 1.25rem; position: fixed; width: 100%; z-index: 1000;
} #blazor-error-ui.dismiss { cursor: pointer; position: absolute; right: 0.75rem; top: 0.5rem;
}.page { position: relative; display: flex; flex-direction: column;
}.main { flex: 1; overflow-y: auto;
}.sidebar { background-image: linear-gradient ( 180deg, rgb ( 5, 39, 103 ) 0%, #3a0647 70% );
}.top-row { background-color: rgb ( 37, 40, 55 )!important; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); /*border-bottom: 0px solid #d6d5d5;*/ justify-content: flex-end; height: 3.5rem; display: flex; align-items: center; left: 0;
}.top-row::deep a, .top-row .btn-link {
white-space: nowrap; /*margin-left: 1.5rem;*/ }.top-row a:first -child { overflow: hidden; text-overflow: ellipsis; /*margin-right: 10px*/ } /* Estilos para modo celular */ /*extra cc*/.k-icon { font-size: 20px;
}.custom-toolbar { width: 100%; line-height: 10px; border-bottom: inset; border-bottom-width: 1px; padding: 3px 8px; color: #a1a1a1; background-color: #252837!important; height: 50px; box-shadow: 0 2px 4px rgba ( 0, 0, 0, 0.4 ); align-content: center; align-items: center; text-decoration: none; position: absolute; top: 0;
}.item_seleccionado { margin-left: 20px; font-weight: bold; font-size: 17px; width: 100%;
} /*Dimensiones de controles*/.margenlados5px { margin: 5px;
}.Altura_total { height: 100%;
} /*íconos de header*/.hamburguer-button { width: 2rem; height: 2rem; background-size: contain;
-webkit- mask -repeat: no-repeat; mask -repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.75; mask -image: url ( "../icons/icons8-menu-24.png" );
-webkit- mask -image: url ( "../icons/icons8-menu-24.png" ); margin-right: 5px; color: white;
}.tb-icon { width: 1rem; height: 1rem; background-size: contain;
-webkit- mask -repeat: no-repeat; mask -repeat: no-repeat; background-position: center center; background-color: currentColor; opacity: 0.7;
}.tb-icon-settings { mask -image: url ( "../icons/setting.png" );
-webkit- mask -image: url ( "../icons/setting.png" ); color: aliceblue;
}.tb-icon-maximizar { mask -image: url ( "../icons/maximizar.png" );
-webkit- mask -image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-info_grid { mask -image: url ( "../icons/informacion.png" );
-webkit- mask -image: url ( "../icons/informacion.png" ); opacity: 1; color: black;
}.tb-icon-logo { mask -image: url ( "../icons/maximizar.png" );
-webkit- mask -image: url ( "../icons/maximizar.png" ); color: aliceblue;
}.tb-icon-refresh { mask -image: url ( "../icons/refresh.png" );
-webkit- mask -image: url ( "../icons/refresh.png" ); color: aliceblue;
} /*fullscreen f11*/ /**:fullscreen
*:-ms-fullscreen,
*:-webkit-full-screen,
*:-moz-full-screen {
overflow: auto !important;
}*/.k-drawer-wrapper { top: 49px; position: sticky; overflow: hidden;
}.drawer-container { width: 100%; height: 100%;
}.borde_cero { margin: 0; padding: 0;
}.texto_drawer { font-size: 10px;
}.k-d-level { display: flex;
}.texto_body { font-size: 14px;
}.item-descr-wrap> span { font-size: 70%;
}.item-descr-wrap { display: flex; flex-direction: column; font-size: 12px; font-family: Arial, Helvetica, sans-serif;
} /*copiado de host*/.k-drawer-content { overflow-x: auto;
}.drawer-hamburger { position: absolute; z-index: 2; margin-top: 13px; margin-left: 30px;
}.k-drawer-item:hover,.k-drawer-item.k-state-hover,.text-info { color: #281f3e b3!important; background-color: #ff6358;
}.my-drawer { padding-top: 50px;
} /*colores defs fondo symbol texto de drawer*/.my-drawer.k-drawer { background-color: #252837; color: white; z-index: 0; height: 100%;
}.my-drawer.k-drawer-item { font-size: 12px; display: flex; align-items: center;
}.my-drawer.k-drawer-item:hover { background-color: #414762; color: antiquewhite!important;
} /*cuadros en ítem principales de sidebar*/.k-drawer-item-main { box-sizing: border-box; padding: 2px; /*border: 1px solid #000;*/ background-color: #1e3548;
}.texto_centrado { text-align: center!important;
} </style> Here is the result: I hope you find that useful.

### Response

**Hristian Stefanov** answered on 21 Jun 2023

Hi Jose, Thank you for presenting a comprehensive overview of the scenario. I appreciate your detailed explanation. After a thorough examination of the code you shared, I have identified the root cause of the undesired scroll effect. The problem lies in the component's height not being set. To rectify this behavior and attain the desired outcome, ensure that the Drawer component's height is set to "100%". You can achieve this by applying the following CSS style: html, body, app,.my-drawer,.k-drawer-content { width: 100%; height: 100%; max-height: 100%;
} By incorporating this style, the Drawer will occupy the full height of its container, eliminating the unwanted scroll effect. If you continue to encounter any difficulties during the testing phase or have any further inquiries, please don't hesitate to reach out. I am readily available to assist you and provide any necessary guidance. Regards, Hristian Stefanov

### Response

**Jose** answered on 20 Jul 2023

Thanks, this is what I needed, I appreciate your support and patience. Kind regards.
