# DropDownTree Component

## Question

**Tin** asked on 20 Sep 2023

Hi @all, I am currently trying to create a TreeDropDownComponent. so far it works, but I have the problem that it doesn't make sense inside a grid. I am currently trying to create a TreeDropDownComponent. so far it works, but I have the problem that it doesn't make sense inside a grid. Because this component inside the grid cell and so the popupElement is not above the grid. Does anyone have an idea how I can fix this? here is my css and code: @using Telerik.Blazor
@using Telerik.Blazor.Components

<div id="treeSelectorComponent">
<span class="telerik-blazor k-dropdownlist k-valid k-picker k-picker-solid k-picker-md k-rounded-md" onclick="@ToggleDropdown">
<span class="k-input-inner @( DropDownShown ? " k-state-focused " : " " )">
<span class="k-input-value-text">@GetSelectedItemsText()</span>
</span>
<button class="telerik-blazor k-button k-input-button k-button-solid k-button-md k-button-solid-base k-icon-button" type="button">
<span class="telerik-blazor k-button-icon k-icon k-i-caret-alt-down"></span>
</button>
</span>
<TelerikAnimationContainer @ref="dropdown" Class="k-popup treeView-scrollable-element">
<TelerikTreeView Data="TreeItems" SelectionMode="TreeViewSelectionMode.Single" OnItemClick="OnTreeItemClicked">
<TreeViewBindings>
<TreeViewBinding ParentIdField="ParentId" TextField="Text" IdField="Id">
<ItemTemplate>
@{
TreeItemSelector item=context as TreeItemSelector;
<span>@item!.Text</span>
}
</ItemTemplate>
</TreeViewBinding>
</TreeViewBindings>
</TelerikTreeView>
</TelerikAnimationContainer>
</div>

@code { private bool DropDownShown { get; set; } private TelerikAnimationContainer dropdown;

[ Parameter, EditorRequired ] public List<TreeItemSelector> TreeItems { get; set; }=new List<TreeItemSelector>();
[ Parameter ] public int TreeId { get; set; }=default!;
[ Parameter ] public EventCallback<int> TreeIdChanged { get; set; } async Task ToggleDropdown () {
DropDownShown=!DropDownShown; await dropdown.ToggleAsync();
} string GetSelectedItemsText () { return TreeItems.FirstOrDefault(p=> p.Id==TreeId)?.Text!;
} private async Task OnTreeItemClicked ( TreeViewItemClickEventArgs arg ) { var item=arg.Item as TreeItemSelector;
TreeId=item!.Id; if (TreeIdChanged.HasDelegate) await TreeIdChanged.InvokeAsync(TreeId); await ToggleDropdown();
} public class TreeItemSelector { public int Id { get; set; } public string Text { get; set; } public int? ParentId { get; set; } public bool HasChildren { get; set; }
}
} #treeSelectorComponent {.k-popup {
&.treeView-scrollable-element { overflow-y: auto; max-height: 300px;
}
}
}

### Response

**Tino** commented on 20 Sep 2023

Here you will find this snippet : [https://blazorrepl.telerik.com/wxktGOlm41O7WkVU22](https://blazorrepl.telerik.com/wxktGOlm41O7WkVU22)
