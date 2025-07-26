# Unable to Set the Initial Checked State on a TreeView

## Question

**Joh** asked on 02 Oct 2021

Having a great time building with the lattest Blazor Ui components. Though I am having issues setting the initial Checked State on a Heirachical Data Model. Pretty certain everything is setup correctly: I am setting the collection at the OnAfterRenderAsync as I am loading the data from LocalStorage. Unfortunately rather than Checking the Child Notes, the Parent Node is always selected. Note below the circled Itetms are in the CheckedSourceDatas collection but the parent is always checked (below) Any pointede would be greatly appreciated. Thanks in advance.

## Answer

**Nadezhda Tacheva** answered on 06 Oct 2021

Hi John, In case the items you want to programmatically check on initial load of the TreeView are correctly stored in the CheckedSourceDatas collection, then this behavior most likely stems from the component not being re-rendered after you set the CheckedSourceDatas collection. That said, you may try calling StateHasChanged() after the collection is set in the in the OnAfterRenderAsync to force the component to re-render and display the change in the viewport as well. I hope you will this information useful. I you run across any other concerns, please let us know, so we can step in and assist. Regards, Nadezhda Tacheva
