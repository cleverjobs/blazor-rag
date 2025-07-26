# BringIntoView() for Blazor treeview?

## Question

**Sve** asked on 16 Jan 2022

Dear Telerik Team! Is there a way to make the treeview scroll so that a speficic node is visible? I need to make the node visible that was selected by code. So I am looking for a way to do what the .BringIntoView() method in the WPF treeview does... thanks and regards Sven

## Answer

**Dimo** answered on 19 Jan 2022

Hello Sven, The desired behavior requires custom coding and the scrollIntoView JavaScript function. You will need to: Expand the item's parent, if necessary. Refresh the TreeView in this case. Select the item. Execute the custom JavaScript. You can find the TreeView item by its " k-state-selected " CSS class. You may need to use setTimeout to wait for actions 1 and 2 to complete. Update: Here is how to find the selected TreeView item with JavaScript. Note that in UI for Blazor 3.0 the k-state-selected class was renamed to k-selected. If you have multiple TreeViews on the page, use a custom class instead of k-treeview. var item=document.querySelector( ".k-treeview .k-selected" ); if (item) {
item.scrollIntoView();
} Regards, Dimo

### Response

**Sven** commented on 27 Jan 2022

Thanks. But I am a bit struggling with point 3. So far I have expanded and selected the item in my C# code. I think I would need to trigger a javascript function that searches for the selected element in the treeview. Can You give me hint of how to do that? I think it would be a goog idea to add a hidden element with an identifier to my item template. So I need to provide the id to the javascript function as a param.

### Response

**Sven** commented on 28 Jan 2022

Hello Dimo! I nearly solved the problem. But the timing remains a problem. In my case, the javacript function is called before the tree is expanded. Snippets: <TreeViewBinding TextField="Title" ItemsField="Childs" HasChildrenField="HasChildren" ExpandedField="IsExpanded"> I expand the ViewModel. Then I call javascript via @inject IJSRuntime JS

JS.InvokeVoidAsync( "ScrollToNode", itemID); But at the time I call the javascript method 'ScrollToNode' the tree is
not yet exanded in Browser. So, the element does not yet exist in DOM. Do you have any Ideo how I can call the javascript method after(!) client side changes are rendered? Thanks in advance Sven

### Response

**Dimo** commented on 01 Feb 2022

@Sven - a possible approach is to raise a boolean flag where you expand the TreeView, and then use this flag in OnAfterRenderAsync to call the JavaScript code. bool ShouldExecuteJs { get; set; } void SelectAndScroll ( ) { // ... load data, expand TreeView, etc. ... ShouldExecuteJs=true;
}
} protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (ShouldExecuteJs)
{
ShouldExecuteJs=false; await js.InvokeVoidAsync( "ScrollToNode", itemID);
} await base.OnAfterRenderAsync(firstRender);
}

### Response

**Sven** commented on 01 Feb 2022

That seems to work. Thanks for your help!
