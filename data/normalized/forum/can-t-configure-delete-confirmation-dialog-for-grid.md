# Can't configure delete confirmation dialog for Grid

## Question

**Ste** asked on 03 Sep 2021

Hi, I am using Telerik UI for Blazor 2.25.0 in a Blazor Server project. I am trying to add a delete confirmation dialog to my grid by using the following documentation: [https://docs.telerik.com/blazor-ui/components/treelist/editing/built-in-dialogs/delete-confirmation.](https://docs.telerik.com/blazor-ui/components/treelist/editing/built-in-dialogs/delete-confirmation.) However, there doesn't seem to be a ConfirmDelete parameter available. <TelerikGrid Data="@GridDataArtists" @ref="@Grid" Height="460px" RowHeight="60" PageSize="10" Pageable="true" Sortable="true" Resizable="true" FilterMode="@GridFilterMode.FilterRow" OnRead="@ReadArtists" OnStateInit="@((GridStateEventArgs<Artist> args)=> OnStateInitHandler(args))" OnStateChanged="@((GridStateEventArgs<Artist> args)=> OnStateChangedHandler(args))" TotalCount="@TotalArtists" EditMode="GridEditMode.Popup" OnCreate="@CreateHandler" OnDelete="DeleteHandler" ConfirmDelete="true"> The above code doesn't compile because it cannot find ConfirmDelete: Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.TelerikGrid`1[[MusicApp.Core.Artist, MusicApp.Core, Version=1.0.0.0, Cult
ure=neutral, PublicKeyToken=null]]' does not have a property matching the name 'ConfirmDelete'. Am I not using the correct version?

## Answer

**Matthias** answered on 03 Sep 2021

Hi Stefan Yes, you need 2.26 (release history) regards Matthias
