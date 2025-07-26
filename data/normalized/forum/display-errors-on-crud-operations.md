# Display errors on CRUD operations

## Question

**boo** asked on 14 Jan 2025

I have a DeleteHandler: private async Task OnDeleteAsync(GridCommandEventArgs args) { if (ViewModel==null) throw new InvalidOperationException("ViewModel==null"); if (!(args.Item is ProductUi product_ui)) throw new InvalidOperationException("!(args.Item is ProductUi product_ui)"); if (product_ui.Id==null) throw new InvalidOperationException("product_ui.Id==null"); var result=await ViewModel.DeleteUiAsync(product_ui.Id.Value); if (result.Error !=null) await Dialogs!.AlertAsync(result.Error, "Delete Error"); } If there is an error I try to display it using one of Telerik's standard Dialogs. If there is an error the dialog is displayed, however the grid then displays a busy spinner and the entire window is disabled. There is now a deadlock, can't close the dialog because the grid has disabled input, the grid is busy because it is waiting for the dialog.

## Answer

**Dimo** answered on 15 Jan 2025

Hello Boone, There are three ways to approach the task and manually render a Dialog in the Grid OnDelete handler. Two of them are demonstrated in the linked KB article. In your case, the Dialog doesn't have to halt the OnDelete handler execution, so you can also display it like this: private async Task OnDeleteAsync ( GridCommandEventArgs args ) { // code that fails with an exception... if (result.Error !=null )
{
_=Task.Run( async ()=>
{ await Dialogs!.AlertAsync(result.Error, "Delete Error" );
});
}
} Regards, Dimo Progress Telerik

### Response

**boone** commented on 16 Jan 2025

Dimo: Before I got your response I tried: _=Dialogs!.AlertAsync(result.Error, "Delete Error"); no await. This worked. Since your response i also tried: _=Task.Run( async ()=>
{ await Dialogs!.AlertAsync(result.Error, "Delete Error" );
}); This also worked. Not sure what the difference is, maybe you could shed some light in this. Also this is a general issue for all CRUD operations, not just delete. In general if there is a CRUD error: Should we set args.IsCancelled=true? Not awaiting a task seams a little hokey however you do it. There should be a better way to handle this and notify the user. Thx

### Response

**Dimo** commented on 16 Jan 2025

Hi Boone, The difference between the two implementations is simply syntax flavor. The end result is the same - executing an async method without awaiting it. Setting args.IsCancelled=true depends on your requirements and goal. For example: Setting it in OnUpdate will keep the user in edit mode. Setting it in OnAdd or OnEdit will not put the Grid in edit mode. Setting it in OnDelete doesn't make much sense, because if you want to prevent deletion, simply don't remove the item from the datasource. Not awaiting a task is a valid approach if nothing else depends on the result of the awaited operation.

### Response

**boone** commented on 16 Jan 2025

Very well ... By the by, your documentation says these dialogs need to be awaited: The DialogFactory methods must be awaited. Do not use them with discard variables ( _ ). If you don't need to await the user response, then use the <TelerikDialog> component declaratively. Still think there should be a better and documented way to handle CRUD errors. You documentation, examples and implementation appear to assume such errors are not possible. Thx

### Response

**Dimo** commented on 16 Jan 2025

Hm, you are right, sorry about the confusion. I also remember why this requirement for predefined Dialogs exists - if they are not awaited, there may be unexpected side effects on subsequent Dialog display. So, the documentation suggestion is valid - use non-awaitable declarative <TelerikDialog> components for alerts that don't need to stop the app execution.
